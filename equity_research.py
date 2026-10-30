"""SEC data pipeline for an equity-research desk.

The pipeline is intentionally limited to data collection and arithmetic. It does
not make an investment recommendation or use a company name in the source code.
"""

from __future__ import annotations

import argparse
import html
import io
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv


SEC_DATA = "https://data.sec.gov"
SEC_ARCHIVES = "https://www.sec.gov/Archives/edgar/data"
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"


class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.in_script = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"script", "style"}:
            self.in_script = True
        elif tag.lower() in {"br", "p", "div", "tr", "li", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style"}:
            self.in_script = False
        elif tag.lower() in {"p", "div", "tr", "li", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.in_script:
            self.parts.append(data)


def plain_text(content: str) -> str:
    parser = TextParser()
    parser.feed(content)
    text = html.unescape("".join(parser.parts))
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line) + "\n"


@dataclass
class Filing:
    form: str
    accession: str
    filing_date: str
    primary_document: str
    accepted: str
    items: str = ""
    index_url: str = ""


class SecClient:
    def __init__(self, user_agent: str) -> None:
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip, deflate",
        })

    def get(self, url: str) -> requests.Response:
        response = self.session.get(url, timeout=30)
        response.raise_for_status()
        return response

    def json(self, url: str) -> Any:
        return self.get(url).json()


def normalize_ticker(value: str) -> str:
    return value.strip().upper()


def resolve_ticker(client: SecClient, ticker: str) -> tuple[str, str]:
    rows = client.json(TICKERS_URL)
    wanted = normalize_ticker(ticker)
    for row in rows.values():
        if normalize_ticker(str(row["ticker"])) == wanted:
            return str(row["cik_str"]).zfill(10), str(row["title"])
    raise ValueError(f"Ticker not found in SEC company_tickers.json: {wanted}")


def accession_without_dashes(accession: str) -> str:
    return accession.replace("-", "")


def filing_index_url(cik: str, accession: str) -> str:
    return f"{SEC_ARCHIVES}/{int(cik)}/{accession_without_dashes(accession)}/{accession}-index.html"


def accepted_time(client: SecClient, cik: str, accession: str) -> str:
    source = client.get(filing_index_url(cik, accession)).text
    # The index page labels this field "Accepted". Keep the complete displayed value.
    match = re.search(r"Accepted\s*</td>\s*<td[^>]*>\s*([^<]+)", source, re.I)
    if not match:
        match = re.search(r"Accepted\s*</div>\s*<div[^>]*>\s*([^<]+)", source, re.I)
    return html.unescape(re.sub(r"\s+", " ", match.group(1).strip())) if match else "not found"


def submissions(client: SecClient, cik: str) -> dict[str, Any]:
    return client.json(f"{SEC_DATA}/submissions/CIK{cik}.json")


def list_filings(client: SecClient, cik: str) -> tuple[dict[str, Any], list[Filing]]:
    data = submissions(client, cik)
    recent = data["filings"]["recent"]
    rows = [dict(zip(recent.keys(), values)) for values in zip(*recent.values())]

    def make(row: dict[str, Any]) -> Filing:
        accession = row["accessionNumber"]
        return Filing(
            form=row["form"], accession=accession, filing_date=row["filingDate"],
            primary_document=row["primaryDocument"],
            accepted=accepted_time(client, cik, accession), items=row.get("items", ""),
            index_url=filing_index_url(cik, accession),
        )

    tens = [row for row in rows if row["form"] == "10-K"]
    qs = [row for row in rows if row["form"] == "10-Q"]
    releases = [row for row in rows if row["form"] == "8-K" and "2.02" in str(row.get("items", ""))]
    if not tens or not qs or not releases:
        raise ValueError("The SEC submissions data does not contain all required filings.")
    selected = [make(max(tens, key=lambda row: row["filingDate"])),
                make(max(qs, key=lambda row: row["filingDate"])),
                make(max(releases, key=lambda row: row["filingDate"]))]
    return data, selected


def archive_url(cik: str, accession: str, filename: str) -> str:
    return f"{SEC_ARCHIVES}/{int(cik)}/{accession_without_dashes(accession)}/{filename}"


def exhibit_991(client: SecClient, cik: str, filing: Filing) -> tuple[str, str]:
    index = client.get(filing.index_url).text
    # SEC index tables expose the exhibit description and document filename.
    matches = re.findall(r"<tr[^>]*>(.*?)</tr>", index, re.I | re.S)
    for row in matches:
        if re.search(r"Exhibit\s*99(?:\.1)?|EX-99(?:\.1)?|99\.1", row, re.I):
            href = re.search(r'href=["\']([^"\']+)["\']', row, re.I)
            if href:
                filename = href.group(1).rsplit("/", 1)[-1]
                return archive_url(cik, filing.accession, filename), filename
    # Some index pages use a direct document table without a textual description.
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', index, re.I)
    for href in hrefs:
        filename = href.rsplit("/", 1)[-1]
        if re.search(r"(?:99[-.]1|exhibit99)", filename, re.I):
            return archive_url(cik, filing.accession, filename), filename
    raise ValueError(f"Exhibit 99.1 was not found for {filing.accession}.")


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._ -]+", "_", value).strip(" .")


def save_documents(client: SecClient, cik: str, company: str, filings: list[Filing], output: Path) -> dict[str, str]:
    run_folder = output / f"{safe_name(company)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    run_folder.mkdir(parents=True, exist_ok=False)
    saved: dict[str, str] = {}
    for filing in filings[:2]:
        url = archive_url(cik, filing.accession, filing.primary_document)
        text = plain_text(client.get(url).text)
        path = run_folder / f"{filing.form.replace('-', '_')}_{filing.accession}.txt"
        path.write_text(text, encoding="utf-8")
        saved[filing.form] = str(path)
    filing = filings[2]
    filing_url = archive_url(cik, filing.accession, filing.primary_document)
    filing_text = plain_text(client.get(filing_url).text)
    filing_path = run_folder / f"8_K_{filing.accession}_{safe_name(filing.primary_document)}.txt"
    filing_path.write_text(filing_text, encoding="utf-8")
    saved["8-K"] = str(filing_path)
    release_url, exhibit_name = exhibit_991(client, cik, filing)
    release_text = plain_text(client.get(release_url).text)
    release_path = run_folder / f"8_K_Exhibit_99_1_{filing.accession}_{safe_name(exhibit_name)}.txt"
    release_path.write_text(release_text, encoding="utf-8")
    saved["8-K Exhibit 99.1"] = str(release_path)
    return saved


CONCEPTS: dict[str, list[str]] = {
    # Prefer the broad consolidated Revenues concept when it is available for
    # the selected fiscal period. Some filers report net sales in
    # RevenueFromContractWithCustomerExcludingAssessedTax and report
    # membership or other income separately. The candidate order is used only
    # as a tie-break after fiscal year, period end, and filing date.
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
    "operating_income": ["OperatingIncomeLoss"],
    "net_income": ["NetIncomeLoss"],
    "diluted_eps": ["EarningsPerShareDiluted"],
    "stockholders_equity": ["StockholdersEquity"],
    "long_term_debt": [
        "LongTermDebtNoncurrent",
        "LongTermDebtAndCapitalLeaseObligations",
        "LongTermDebt",
    ],
    "current_portion_debt": [
        "LongTermDebtAndCapitalLeaseObligationsCurrent",
        "LongTermDebtCurrent",
        "OtherLongTermDebtCurrent",
    ],
    "cash_from_operations": ["NetCashProvidedByUsedInOperatingActivities"],
    "additions_to_property_and_equipment": ["PaymentsToAcquirePropertyPlantAndEquipment"],
}

CONCEPT_UNITS: dict[str, str] = {
    "revenue": "USD",
    "operating_income": "USD",
    "net_income": "USD",
    "diluted_eps": "USD/shares",
    "stockholders_equity": "USD",
    "long_term_debt": "USD",
    "current_portion_debt": "USD",
    "cash_from_operations": "USD",
    "additions_to_property_and_equipment": "USD",
}


def annual_facts(client: SecClient, cik: str) -> dict[str, Any]:
    return client.json(f"{SEC_DATA}/api/xbrl/companyfacts/CIK{cik}.json")


def annual_rows(facts: dict[str, Any], tag: str, unit: str) -> list[dict[str, Any]]:
    tag_data = facts.get("facts", {}).get("us-gaap", {}).get(tag, {})
    unit_rows = tag_data.get("units", {}).get(unit, [])
    rows: list[dict[str, Any]] = []
    for source in unit_rows:
        if source.get("form") == "10-K" and source.get("fy") and source.get("fp") == "FY":
            row = dict(source)
            row["unit"] = unit
            row["concept_label"] = tag_data.get("label")
            row["concept_description"] = tag_data.get("description")
            rows.append(row)
    return rows


def latest_candidate(facts: dict[str, Any], metric: str, candidates: list[str]) -> tuple[str, dict[str, Any]] | None:
    choices: list[tuple[int, str, dict[str, Any]]] = []
    for index, tag in enumerate(candidates):
        rows = annual_rows(facts, tag, CONCEPT_UNITS[metric])
        if rows:
            latest = max(rows, key=lambda row: (int(row["fy"]), row.get("end", ""), row.get("filed", "")))
            choices.append((index, tag, latest))
    if not choices:
        return None
    _, tag, row = max(choices, key=lambda item: (int(item[2]["fy"]), item[2].get("end", ""), item[2].get("filed", ""), -item[0]))
    return tag, row


def same_fy_values(
    facts: dict[str, Any],
    metric: str,
    tag: str,
    fy: int,
    period_ends: dict[int, str | None] | None = None,
) -> dict[int, dict[str, Any]]:
    rows = [
        row for row in annual_rows(facts, tag, CONCEPT_UNITS[metric])
        if int(row["fy"]) in {fy, fy - 1}
    ]
    result: dict[int, dict[str, Any]] = {}
    for row in rows:
        year = int(row["fy"])
        target_end = (period_ends or {}).get(year)
        if target_end and any(candidate.get("end") == target_end for candidate in rows if int(candidate["fy"]) == year):
            if row.get("end") != target_end:
                continue
        if year not in result or (row.get("filed", ""), row.get("end", "")) > (
            result[year].get("filed", ""), result[year].get("end", "")
        ):
            result[year] = row
    return result


def build_fact_report(facts: dict[str, Any]) -> dict[str, Any]:
    revenue_choice = latest_candidate(facts, "revenue", CONCEPTS["revenue"])
    if not revenue_choice:
        raise ValueError("No annual revenue fact was found.")
    revenue_tag, revenue_row = revenue_choice
    fy = int(revenue_row["fy"])
    revenue_values = same_fy_values(facts, "revenue", revenue_tag, fy, {fy: revenue_row.get("end")})
    period_ends = {
        fy: revenue_values.get(fy, revenue_row).get("end"),
        fy - 1: revenue_values.get(fy - 1, {}).get("end"),
    }
    report: dict[str, Any] = {"fiscal_year": fy, "metrics": {}}
    for metric, candidates in CONCEPTS.items():
        choice = latest_candidate(facts, metric, candidates)
        if not choice:
            report["metrics"][metric] = {"tag": None, "current": None, "prior": None}
            continue
        tag, _ = choice
        values = same_fy_values(facts, metric, tag, fy, period_ends)
        report["metrics"][metric] = {
            "tag": tag,
            "unit": CONCEPT_UNITS[metric],
            "description": values.get(fy, values.get(fy - 1, {})).get("concept_description"),
            "current": values.get(fy),
            "prior": values.get(fy - 1),
        }
    return report


def number(report: dict[str, Any], metric: str, period: str = "current") -> float | None:
    row = report["metrics"].get(metric, {}).get(period)
    return float(row["val"]) if row else None


def ratio(numerator: float | None, denominator: float | None) -> float | None:
    return numerator / denominator if numerator is not None and denominator not in (None, 0) else None


def debt_total(report: dict[str, Any], period: str = "current") -> tuple[float | None, str]:
    long_term_row = report["metrics"].get("long_term_debt", {}).get(period)
    current_row = report["metrics"].get("current_portion_debt", {}).get(period)
    long_term = float(long_term_row["val"]) if long_term_row else None
    current = float(current_row["val"]) if current_row else None
    if long_term is None:
        return None, "unavailable: long-term debt is missing"
    description = str(report["metrics"].get("long_term_debt", {}).get("description") or "").lower()
    is_noncurrent = "noncurrent" in description or "excluding current" in description
    if is_noncurrent:
        if current is None:
            return None, "unavailable: current portion is missing"
        return long_term + current, f"{long_term} + {current}"
    # A total-debt concept already includes current maturities. Do not add the
    # current portion a second time.
    return long_term, f"{long_term} (current maturities already included)"


def calculations(report: dict[str, Any], price: float | None) -> dict[str, float | None]:
    revenue, prior_revenue = number(report, "revenue"), number(report, "revenue", "prior")
    op, net = number(report, "operating_income"), number(report, "net_income")
    equity, prior_equity = number(report, "stockholders_equity"), number(report, "stockholders_equity", "prior")
    debt, _ = debt_total(report)
    capex = number(report, "additions_to_property_and_equipment")
    # SEC cash-flow facts normally store payments as negative values. Use the
    # positive addition amount so the requested FCF arithmetic is CFO - capex.
    additions = abs(capex) if capex is not None else None
    return {
        "revenue_growth": ratio((revenue - prior_revenue) if revenue is not None and prior_revenue is not None else None, prior_revenue),
        "operating_margin": ratio(op, revenue),
        "return_on_average_equity": ratio(net, ((equity + prior_equity) / 2) if equity is not None and prior_equity is not None else None),
        "debt_to_equity": ratio(debt, equity),
        "free_cash_flow": number(report, "cash_from_operations") - additions if number(report, "cash_from_operations") is not None and additions is not None else None,
        "pe": ratio(price, number(report, "diluted_eps")),
    }


def print_filings(filings: list[Filing]) -> None:
    for filing in filings:
        print(f"{filing.form}: accession={filing.accession}; Accepted={filing.accepted}")


def print_report(report: dict[str, Any], title: str = "Facts") -> None:
    print(f"{title}; fiscal year={report['fiscal_year']}")
    for metric, value in report["metrics"].items():
        print(f"{metric}: tag={value['tag']}; unit={value.get('unit')}")
        for period in ("current", "prior"):
            row = value[period]
            if row:
                print(f"  {period}: value={row['val']}; period_end={row.get('end')}; filing={row.get('accn')}")
            else:
                print(f"  {period}: unavailable")


def print_calculations(report: dict[str, Any], price: float | None) -> None:
    values = calculations(report, price)
    revenue = number(report, "revenue")
    prior_revenue = number(report, "revenue", "prior")
    operating_income = number(report, "operating_income")
    net_income = number(report, "net_income")
    equity = number(report, "stockholders_equity")
    prior_equity = number(report, "stockholders_equity", "prior")
    debt, debt_expression = debt_total(report)
    cfo = number(report, "cash_from_operations")
    capex = number(report, "additions_to_property_and_equipment")
    additions = abs(capex) if capex is not None else None
    average_equity = ((equity + prior_equity) / 2) if equity is not None and prior_equity is not None else None
    print(f"revenue_growth: ({revenue} - {prior_revenue}) / {prior_revenue} = {values['revenue_growth']}")
    print(f"operating_margin: {operating_income} / {revenue} = {values['operating_margin']}")
    print(f"return_on_average_equity: {net_income} / (({equity} + {prior_equity}) / 2) = {values['return_on_average_equity']}")
    print(f"debt_to_equity: ({debt_expression}) / {equity} = {values['debt_to_equity']}")
    print(f"free_cash_flow: {cfo} - {additions} = {values['free_cash_flow']}")
    if price is None:
        print("pe: not calculated (closing price was not supplied)")
    else:
        print(f"pe: {price} / {number(report, 'diluted_eps')} = {values['pe']}")


def release_period_label(period: str) -> str:
    match = re.search(
        r"(?P<number>\d+|three|six|nine|twelve)\s+(?P<unit>weeks?|months?|years?)",
        period,
        re.I,
    )
    if not match:
        return "Period"
    number_text = match.group("number").lower()
    number_words = {
        "three": 3,
        "six": 6,
        "nine": 9,
        "twelve": 12,
    }
    number = int(number_text) if number_text.isdigit() else number_words[number_text]
    unit = match.group("unit").lower()
    if unit.startswith("year") or (unit.startswith("month") and number >= 12) or (
        unit.startswith("week") and number >= 48
    ):
        return "Annual"
    if (unit.startswith("month") and number <= 3) or (unit.startswith("week") and number <= 20):
        return "Quarterly"
    return "Interim"


def release_lines(path: str) -> None:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    units_index = next(
        (index for index, line in enumerate(lines) if re.search(r"\(dollars? in .*except per share data", line, re.I)),
        None,
    )
    units = lines[units_index] if units_index is not None else "not stated"
    header_window = "".join(lines[max(0, (units_index or 0) + 1):(units_index or 0) + 7])
    periods = re.findall(
        r"((?:\d+|three|six|nine|twelve)\s+(?:weeks?|months?|years?)\s+ended)",
        header_window,
        re.I,
    )
    dates = re.findall(
        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s*\d{4}",
        header_window,
        re.I,
    )
    columns = []
    if periods and dates:
        for index, date in enumerate(dates):
            period = periods[min(index // 2, len(periods) - 1)]
            clean_date = re.sub(r"\s+", " ", date).replace(",", ", ")
            columns.append(f"{release_period_label(period)} — {period} ({clean_date})")
    output = [f"Release table units: {units}", "Release table columns:"]
    for index, column in enumerate(columns, start=1):
        output.append(f"  {index}: {column}")

    eps_section = False
    for line in lines:
        if re.search(r"net income per common share", line, re.I):
            eps_section = True
        label = None
        if re.match(r"total\s+revenue", line, re.I):
            label = "Total revenue"
        elif eps_section and re.match(r"diluted", line, re.I):
            label = "Diluted EPS"
            eps_section = False
        if label:
            values_text = re.sub(rf"^{re.escape(label.split()[0])}(?:\s+revenue)?", "", line, flags=re.I).strip()
            values = re.findall(r"(?:\$?\(?[\d,]+(?:\.\d+)?\)?|—)", values_text)
            output.append(f"{label}:")
            if columns and len(values) == len(columns):
                for column, value in zip(columns, values):
                    output.append(f"  {column}: {value}")
            else:
                output.append(f"  {line}")
    print("\n".join(output))


GEMINI_MODEL = "gemini-3.8-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"
REPORT_PARTS = [
    "Overview",
    "Market Positioning and Growth Outlook",
    "Valuation Insights",
    "Future Developments and Strategic Recommendations",
    "Investment Recommendation",
]
SOURCE_STATEMENTS = {
    "revenue": "Consolidated Statements of Income",
    "operating_income": "Consolidated Statements of Income",
    "net_income": "Consolidated Statements of Income",
    "diluted_eps": "Consolidated Statements of Income; Net Income Per Common Share",
    "stockholders_equity": "Consolidated Balance Sheets",
    "long_term_debt": "Consolidated Balance Sheets",
    "current_portion_debt": "Consolidated Balance Sheets",
    "cash_from_operations": "Consolidated Statements of Cash Flows",
    "additions_to_property_and_equipment": "Consolidated Statements of Cash Flows",
}


ROLE_INSTRUCTIONS = {
    "Research Analyst": (
        "You are the Research Analyst. Use only the evidence in the JSON packet. "
        "Analyze the business model, competitive position, catalysts, and recent developments. "
        "Use the supplied 10-K Business and MD&A excerpts and earnings-release excerpts. "
        "Every factual claim must include a short exact quote and its source file and line number. "
        "Do not invent facts, sources, prices, or citations. Return JSON with keys "
        "business_model, competitive_position, catalysts, recent_developments, evidence, gaps."
    ),
    "Financial Analyst": (
        "You are the Financial Analyst. Use only the evidence in the JSON packet. "
        "Analyze the supplied Step 4 facts, Step 5 ratios, Step 6 release, and Step 7 peers. "
        "Every number must include its filing, XBRL tag or source line, and period. "
        "State a definition whenever a filing offers two definitions. Show arithmetic for every ratio "
        "using the supplied calculator results. Never compute arithmetic in the model. "
        "If another ratio is needed, return it in calculator_requests instead of calculating it. "
        "Return JSON with keys statement_analysis, quarter_analysis, peer_analysis, valuation_insights, "
        "calculator_requests, evidence, gaps."
    ),
    "Investment Advisor": (
        "You are the Investment Advisor. Use only the Research Analyst and Financial Analyst outputs "
        "in this JSON packet. Do not use outside information or raw filings. Produce a thesis and exactly "
        "one of Buy, Hold, or Sell. Identify the one number that decides the recommendation and explain why. "
        "If the supplied evidence does not support a recommendation, state that limitation clearly. "
        "Return JSON with keys thesis, recommendation, deciding_number, rationale, evidence, gaps."
    ),
    "Strategy Manager": (
        "You are the Strategy Manager. Use only the JSON packet. Check that the five required parts are "
        "present and consistent: Overview; Market Positioning and Growth Outlook; Valuation Insights; "
        "Future Developments and Strategic Recommendations; Investment Recommendation. "
        "For a review task, return JSON with keys failed_parts and repair_packets. Each repair packet must "
        "contain role, task, context, and expected_output. Send a failing part back to its role at most once. "
        "For a compile task, return JSON with keys report_markdown, section_status, and gaps. The report must "
        "contain exactly the five required headings and must not add unsupported facts."
    ),
}


def line_numbered_excerpt(path: str, start_pattern: str, end_pattern: str, max_lines: int = 500) -> dict[str, Any]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    start = next((i for i, line in enumerate(lines) if re.search(start_pattern, line, re.I)), None)
    if start is None:
        return {"file": path, "lines": "", "line_start": None, "line_end": None, "missing": True}
    end = next(
        (i for i in range(start + 1, len(lines)) if re.search(end_pattern, lines[i], re.I)),
        min(len(lines), start + max_lines),
    )
    end = min(end, start + max_lines)
    numbered = "\n".join(f"{i + 1}: {lines[i]}" for i in range(start, end))
    return {"file": path, "lines": numbered, "line_start": start + 1, "line_end": end}


def fact_context(report: dict[str, Any], accession: str, filing: str) -> dict[str, Any]:
    result: dict[str, Any] = {
        "filing": filing,
        "accession": accession,
        "fiscal_year": report.get("fiscal_year"),
        "metrics": {},
    }
    for metric, value in report.get("metrics", {}).items():
        result["metrics"][metric] = {
            "tag": value.get("tag"),
            "unit": value.get("unit"),
            "source_statement": SOURCE_STATEMENTS.get(metric),
            "current": value.get("current"),
            "prior": value.get("prior"),
        }
    return result


def role_packet(task: str, context: dict[str, Any], expected_output: str) -> dict[str, Any]:
    return {"task": task, "context": context, "expected_output": expected_output}


def parse_json_response(text: str, role: str) -> dict[str, Any]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.I)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        value = json.loads(cleaned)
    except json.JSONDecodeError as error:
        raise ValueError(f"{role} returned invalid JSON: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"{role} returned JSON that was not an object.")
    return value


def call_gemini(client: Any, role: str, model: str, packet: dict[str, Any]) -> dict[str, Any]:
    print(f"Role: {role}")
    from google.genai import types

    try:
        response = client.models.generate_content(
            model=model,
            contents=json.dumps(packet, ensure_ascii=False),
            config=types.GenerateContentConfig(
                system_instruction=ROLE_INSTRUCTIONS[role],
                response_mime_type="application/json",
                temperature=0.2,
            ),
        )
    except Exception as error:
        raise ValueError(f"{role} Gemini call failed ({type(error).__name__}).") from error
    if not response.text:
        raise ValueError(f"{role} returned an empty response.")
    return parse_json_response(response.text, role)


def desk_report(
    args: argparse.Namespace,
    company: str,
    cik: str,
    filings: list[Filing],
    saved: dict[str, str],
    report: dict[str, Any],
    peer_reports: dict[str, Any],
    facts_folder: Path,
    step6_text: str,
) -> Path:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is missing from .env; desk calls were not started.")
    from google import genai
    from google.genai import types

    gemini = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=60000))
    model = args.gemini_model or GEMINI_MODEL
    filing_map = {filing.form: filing for filing in filings}
    ten_k = filing_map.get("10-K")
    release = Path(saved["8-K Exhibit 99.1"])
    business = line_numbered_excerpt(saved["10-K"], r"^Item\s+1\s*[^\w\s]\s*Business", r"^Item\s+1A\s*[^\w\s]")
    mda = line_numbered_excerpt(
        saved["10-K"],
        r"^Item\s+7\s*[^\w\s]\s*Management.?s Discussion",
        r"^Item\s+7A\s*[^\w\s]|^Item\s+8\s*[^\w\s]",
    )
    release_lines_context = "\n".join(
        f"{i + 1}: {line}" for i, line in enumerate(release.read_text(encoding="utf-8").splitlines())
    )
    primary_accession = ten_k.accession if ten_k else "unavailable"
    primary_facts = fact_context(report, primary_accession, "10-K")
    peer_facts = {
        ticker: fact_context(value["report"], "see peer 10-K accession in facts", "10-K")
        for ticker, value in peer_reports.items()
    }
    ratio_context = {
        "price": args.price,
        "calculations": calculations(report, args.price),
        "inputs": {
            "revenue": number(report, "revenue"),
            "prior_revenue": number(report, "revenue", "prior"),
            "operating_income": number(report, "operating_income"),
            "net_income": number(report, "net_income"),
            "equity": number(report, "stockholders_equity"),
            "prior_equity": number(report, "stockholders_equity", "prior"),
            "long_term_debt": number(report, "long_term_debt"),
            "current_portion_debt": number(report, "current_portion_debt"),
            "cash_from_operations": number(report, "cash_from_operations"),
            "additions_to_property_and_equipment": number(report, "additions_to_property_and_equipment"),
        },
    }
    research = call_gemini(
        gemini,
        "Research Analyst",
        model,
        role_packet(
            "Analyze the business model, competitive position, catalysts, and recent developments.",
            {
                "source_filings": [{"form": f.form, "accession": f.accession} for f in filings],
                "business_section": business,
                "mda_section": mda,
                "earnings_release": {
                    "file": str(release),
                    "accession": filing_map.get("8-K").accession if filing_map.get("8-K") else None,
                    "lines": release_lines_context,
                },
            },
            "JSON with evidence-backed business_model, competitive_position, catalysts, recent_developments, evidence, and gaps.",
        ),
    )
    financial = call_gemini(
        gemini,
        "Financial Analyst",
        model,
        role_packet(
            "Analyze statements, ratios, the earnings-release quarter, peers, and valuation inputs.",
            {
                "primary_facts": primary_facts,
                "ratios": ratio_context,
                "step6_output": step6_text,
                "peer_facts": peer_facts,
                "peer_operating_margins": {
                    ticker: calculations(value["report"], None)["operating_margin"]
                    for ticker, value in peer_reports.items()
                },
            },
            "JSON with statement_analysis, quarter_analysis, peer_analysis, valuation_insights, calculator_requests, evidence, and gaps. Do not calculate ratios in the model.",
        ),
    )
    advisor = call_gemini(
        gemini,
        "Investment Advisor",
        model,
        role_packet(
            "Form an investment thesis and recommendation from the two analyst outputs only.",
            {"research_analyst": research, "financial_analyst": financial},
            "JSON with thesis, recommendation, deciding_number, rationale, evidence, and gaps.",
        ),
    )
    manager_context = {
        "required_parts": REPORT_PARTS,
        "research_analyst": research,
        "financial_analyst": financial,
        "investment_advisor": advisor,
    }
    review = call_gemini(
        gemini,
        "Strategy Manager",
        model,
        role_packet(
            "Check the three role outputs for the five required report parts and identify missing or inconsistent parts.",
            manager_context,
            "JSON with failed_parts and repair_packets. Return an empty list when no repair is needed.",
        ),
    )
    repair_count: dict[str, int] = {}
    for repair in review.get("repair_packets", []):
        if not isinstance(repair, dict):
            continue
        role = repair.get("role")
        if role not in {"Research Analyst", "Financial Analyst", "Investment Advisor"}:
            continue
        if repair_count.get(role, 0) >= 1:
            continue
        packet = {key: repair.get(key) for key in ("task", "context", "expected_output")}
        if any(value is None for value in packet.values()):
            continue
        repaired = call_gemini(gemini, role, model, packet)
        repair_count[role] = 1
        if role == "Research Analyst":
            research = repaired
        elif role == "Financial Analyst":
            financial = repaired
        else:
            advisor = repaired
    final = call_gemini(
        gemini,
        "Strategy Manager",
        model,
        role_packet(
            "Compile the final report after the consistency check and any one-time role repairs.",
            {
                "required_parts": REPORT_PARTS,
                "research_analyst": research,
                "financial_analyst": financial,
                "investment_advisor": advisor,
                "initial_review": review,
            },
            "JSON with report_markdown, section_status, and gaps. Include exactly the five required headings.",
        ),
    )
    report_markdown = str(final.get("report_markdown", "")).strip()
    if not report_markdown:
        raise ValueError("Strategy Manager returned no report markdown.")
    missing_parts = [part for part in REPORT_PARTS if not re.search(rf"^#+\s*{re.escape(part)}\s*$", report_markdown, re.I | re.M)]
    if missing_parts:
        raise ValueError("Strategy Manager report is missing required parts: " + ", ".join(missing_parts))
    accession_line = "; ".join(f"{filing.form} {filing.accession}" for filing in filings)
    report_path = facts_folder / "desk_report.md"
    report_path.write_text(
        f"Filings read: {accession_line}\nRun time: {datetime.now().isoformat(timespec='seconds')}\n\n{report_markdown}\n",
        encoding="utf-8",
    )
    print(f"Saved desk report: {report_path}")
    return report_path


def run(args: argparse.Namespace) -> None:
    load_dotenv(Path(__file__).with_name(".env"), override=True)
    user_agent = os.getenv("SEC_USER_AGENT")
    if not user_agent:
        raise ValueError("SEC_USER_AGENT is missing from .env")
    client = SecClient(user_agent)
    if args.desk and args.step is not None:
        raise ValueError("--desk runs all seven Lab 2 steps and cannot be combined with --step.")
    selected = set(range(1, 8)) if args.step is None or args.desk else {args.step}
    args.peers = [peer for value in args.peers for peer in value.split(",") if peer.strip()]
    cik, company = resolve_ticker(client, args.ticker)
    if 1 in selected:
        print("Step 1: resolve ticker")
        print(f"Company resolved: {company}; ticker={normalize_ticker(args.ticker)}; CIK={cik}")
    filings: list[Filing] = []
    facts: dict[str, Any] | None = None
    report: dict[str, Any] | None = None
    saved: dict[str, str] = {}
    peer_reports: dict[str, Any] = {}
    step6_text = ""
    if 2 in selected or 3 in selected or 6 in selected:
        _, filings = list_filings(client, cik)
    if 2 in selected:
        print("Step 2: select filings")
        print_filings(filings)
    if 3 in selected or 6 in selected:
        saved = save_documents(client, cik, company, filings, Path("readings"))
    if 3 in selected:
        print("Step 3: download and convert documents")
        for kind, path in saved.items():
            print(f"Saved {kind}: {path}")
    if 4 in selected or 5 in selected:
        facts = annual_facts(client, cik)
        report = build_fact_report(facts)
    if 4 in selected:
        print("Step 4: collect XBRL facts")
        print_report(report)
    if 5 in selected:
        print("Step 5: calculate research metrics")
        print_calculations(report, args.price)
    if 6 in selected:
        print("Step 6: read earnings release")
        step6_output = io.StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = step6_output
            release_lines(saved["8-K Exhibit 99.1"])
        finally:
            sys.stdout = original_stdout
        step6_text = step6_output.getvalue()
        print(step6_text, end="")
        step6_path = Path(saved["10-K"]).parent / "step6_output.txt"
        step6_path.write_text(step6_text, encoding="utf-8")
        print(f"Saved Step 6 output: {step6_path}")
    if 7 in selected:
        print("Step 7: collect peer facts")
        for peer in args.peers:
            peer_cik, peer_company = resolve_ticker(client, peer)
            peer_report = build_fact_report(annual_facts(client, peer_cik))
            peer_reports[normalize_ticker(peer)] = {
                "company": peer_company,
                "cik": peer_cik,
                "report": peer_report,
            }
            print_report(peer_report, f"Peer {peer_company} ({normalize_ticker(peer)})")
            print(f"operating_margin: {calculations(peer_report, None)['operating_margin']}")
    facts_folder: Path | None = None
    # Facts are saved beside the downloaded texts when a complete run is used.
    if selected & {4, 5, 7} and 3 in selected:
        facts_folder = Path(saved["10-K"]).parent
        facts_payload = {
            "primary": {"company": company, "cik": cik, "report": report or facts},
            "peers": peer_reports,
        }
        (facts_folder / "facts.json").write_text(json.dumps(facts_payload, indent=2), encoding="utf-8")
        print(f"Saved facts: {facts_folder / 'facts.json'}")
    elif selected & {4, 5, 7}:
        facts_folder = Path("readings") / f"{safe_name(company)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        facts_folder.mkdir(parents=True, exist_ok=False)
        facts_payload = {
            "primary": {"company": company, "cik": cik, "report": report or facts},
            "peers": peer_reports,
        }
        (facts_folder / "facts.json").write_text(json.dumps(facts_payload, indent=2), encoding="utf-8")
        print(f"Saved facts: {facts_folder / 'facts.json'}")
    if args.desk:
        if facts_folder is None or report is None:
            raise ValueError("The desk requires the complete seven-step run and saved facts.")
        desk_report(args, company, cik, filings, saved, report, peer_reports, facts_folder, step6_text)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect SEC equity-research data.")
    parser.add_argument("ticker")
    parser.add_argument("--peers", nargs="*", default=[], metavar="TICKER")
    parser.add_argument("--price", type=float)
    parser.add_argument("--step", type=int, choices=range(1, 8))
    parser.add_argument("--desk", action="store_true", help="Run the seven Lab 2 steps and the four-role desk.")
    parser.add_argument(
        "--model",
        dest="gemini_model",
        help=f"Gemini model for --desk (default: {GEMINI_MODEL}; fallback: {GEMINI_FALLBACK_MODEL}).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    try:
        run(parse_args())
    except (requests.RequestException, ValueError, OSError, KeyError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
