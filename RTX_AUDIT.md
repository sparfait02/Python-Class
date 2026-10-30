# RTX Report Audit Worksheet

Purpose: manual review of `RTX_FALLBACK_REPORT.md` against the saved source files and course report requirements.

All human marks, error counts, and partner fields are intentionally blank. This worksheet does not state that any claim has been verified.

## Source register

- RTX 2025 10-K: [SEC filing](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) — saved file: `readings/RTX Corp_20261029_222258/10_K_0000101829-26-000006.txt`
- RTX October earnings Exhibit 99.1: [SEC exhibit](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) — saved file: `readings/RTX Corp_20261029_222258/8_K_Exhibit_99_1_0000101829-26-000030_a2026-10x208xkerexhibit99.htm.txt`
- RTX 10-Q index: [SEC index](https://www.sec.gov/Archives/edgar/data/101829/000010182926000031/0000101829-26-000031-index.htm) — identified, not substantively reviewed.
- Price source: [StockAnalysis RTX history](https://stockanalysis.com/stocks/rtx/history/)
- LMT FY2025 10-K: [SEC index](https://www.sec.gov/Archives/edgar/data/936468/000162828026004195/0001628280-26-004195-index.htm) — saved file: `readings/LOCKHEED MARTIN CORP_20261029_230917/10_K_0001628280-26-004195.txt`
- NOC FY2025 10-K: [SEC index](https://www.sec.gov/Archives/edgar/data/1133421/000113342126000003/0001133421-26-000003-index.htm) — saved file: `readings/NORTHROP GRUMMAN CORP _DE__20261029_230920/10_K_0001133421-26-000003.txt`

## Audit fields

- Auditor: ____________________
- Date started: ____________________
- Date completed: ____________________
- Total errors: ____________________
- Partner name: ____________________
- Partner check 1: ____________________
- Partner check 2: ____________________

## Eleven core claims

For each row, compare the report claim with the cited saved text, units, periods, tags, and arithmetic. Do not treat the saved XBRL tag as proof that the statement label is correct without checking the statement.

| # | Report claim | Source link | Saved-file line reference | What to compare | Human mark | Error count | Partner field |
|---:|---|---|---|---|---|---|---|
| 1 | Annual total revenue: FY2025 $88,603 million; FY2024 $80,738 million; tag `RevenueFromContractWithCustomerExcludingAssessedTax`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1086-1110; local `10_K_0000101829-26-000006.txt` | Compare the consolidated statement title, units, year columns, total net sales label, both values, and tag selection. |  |  |  |
| 2 | Annual revenue growth: `(88,603 - 80,738) / 80,738 = 9.7414%`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1086-1110; Python calculation in report | Recalculate with the two annual total-revenue values. Compare sign, denominator, rounding, and period alignment. |  |  |  |
| 3 | Operating income and operating margin: $9,300 million; `$9,300 / $88,603 = 10.4963%`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1086-1110 and MD&A lines 470-475 | Compare operating-profit label, units, periods, and the formula with total net sales. Check that no adjusted operating measure was used. |  |  |  |
| 4 | Attributable net income: FY2025 $6,732 million; FY2024 $4,774 million; tag `NetIncomeLoss`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1106-1108; saved facts metadata for concept label | Compare consolidated net income, noncontrolling interest, and net income attributable to common shareowners. Check that the report does not call $6,732/$4,774 million consolidated net income. |  |  |  |
| 5 | Annual GAAP diluted EPS: FY2025 $4.96; FY2024 $3.55; tag `EarningsPerShareDiluted`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1108-1110 | Compare diluted EPS label, USD/share unit, annual columns, attributable-to-common-shareowners definition, and GAAP status. |  |  |  |
| 6 | Return on average equity: `$6,732 / (($65,245 + 60,156) / 2) = 10.7368%`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1106-1108 and 1140-1180; Python calculation in report | Compare numerator definition, beginning and ending equity dates, average-equity formula, units, and rounding. |  |  |  |
| 7 | Debt/equity including current long-term debt: `($34,288 + $3,412) / $65,245 = 0.5778`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1140-1180; Python calculation in report | Compare noncurrent debt, current long-term debt, equity denominator, balance-sheet date, and whether other liabilities were incorrectly added. |  |  |  |
| 8 | CFO minus capex: `$10,567 - $2,627 = $7,940 million` course-defined FCF. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1200-1213; Python calculation in report | Compare CFO and capital-expenditure lines, signs, units, annual periods, and the label that this is a course calculation rather than necessarily RTX’s reported FCF. |  |  |  |
| 9 | Quarterly total revenue: Q3 2026 $24,965 million; Q3 2025 $22,478 million. | [RTX Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) | Exhibit lines 131-135 | Compare statement title, quarter ended September 30, units, current/prior columns, and total sales label. |  |  |  |
| 10 | Quarterly revenue growth: release 11%; Python `(24,965 - 22,478) / 22,478 = 11.0642%`. | [RTX Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) | Exhibit lines 14-16 and 131-135; Python calculation in report | Compare the release’s rounded 11% with the independently recalculated exact percentage. Check the comparable quarter and denominator. |  |  |  |
| 11 | Quarterly GAAP diluted EPS: Q3 2026 $1.89; Q3 2025 $1.41. | [RTX Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) | Exhibit lines 150-152 | Compare diluted EPS row, current/prior quarter columns, USD/share unit, quarter ended September 30, and GAAP status. |  |  |  |

## Supporting annual inputs

| Report claim | Source link | Saved-file lines | What to compare | Human mark | Error count | Partner field |
|---|---|---|---|---|---|---|
| Stockholders’ equity: $65,245 million current; $60,156 million prior; tag `StockholdersEquity`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1140-1180 | Compare total shareowners’ equity, units, year-end dates, and denominator used in ROAE. |  |  |  |
| Long-term debt: $34,288 million current; $38,726 million prior; tag `LongTermDebtAndCapitalLeaseObligations`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1140-1180 | Compare noncurrent long-term debt and balance-sheet columns. |  |  |  |
| Current long-term debt: $3,412 million current; $2,352 million prior; tag `LongTermDebtAndCapitalLeaseObligationsCurrent`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1140-1180 | Compare the current portion of long-term debt, not short-term borrowings or all current liabilities. |  |  |  |
| Cash from operations: $10,567 million current; $7,159 million prior; tag `NetCashProvidedByUsedInOperatingActivities`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1200-1213 | Compare cash-flow statement line, units, years, and sign. |  |  |  |
| Capital expenditures: $2,627 million current; $2,625 million prior; tag `PaymentsToAcquirePropertyPlantAndEquipment`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1200-1213 | Compare capital-expenditure line and whether the subtraction uses the positive magnitude shown in the report. |  |  |  |

## Other financial numbers in the report

| Report number or claim | Source link | Saved-file line reference | What to compare | Human mark | Error count | Partner field |
|---|---|---|---|---|---|---|
| Annual operating margin definition: operating profit divided by total net sales; reported 2025 margin 10.5%. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 470-475 | Compare the MD&A metric names, units, and reported rounded percentage with the report’s calculated percentage. |  |  |  |
| Annual backlog: $268 billion at December 31, 2025; $218 billion at December 31, 2024; approximately 25% expected as revenue over next 12 months. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 171-172 and 477 | Compare dates, definition of firm orders/RPO, and management-expectation wording. |  |  |  |
| Earnings-release sales: $25.0 billion, up 11% versus prior year; GAAP EPS $1.89; adjusted EPS $2.26; operating cash flow $2.9 billion; free cash flow $2.1 billion. | [RTX Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) | Lines 14-19 | Compare reported GAAP/non-GAAP labels, units, quarter, and whether adjusted figures are kept separate. |  |  |  |
| Earnings-release backlog and awards: $340 billion total, including $176 billion commercial and $164 billion defense; Tomahawk and AMRAAM contracts. | [RTX Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) | Lines 20-21 | Compare exact wording, current quarter, and whether the report treats awards as potential activity rather than guaranteed earnings. |  |  |  |
| Price: $194.60 regular-session unadjusted Close on October 27, 2026. | [StockAnalysis RTX history](https://stockanalysis.com/stocks/rtx/history/) | External source; no RTX filing line | Compare date, regular-session Close, and unadjusted Close. Do not substitute Adjusted Close. |  |  |  |
| Price divided by FY2025 GAAP diluted EPS: `$194.60 / $4.96 = 39.2338709677`, or 39.23x. | [StockAnalysis RTX history](https://stockanalysis.com/stocks/rtx/history/) and [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Price external; EPS 10-K lines 1108-1110; Python calculation | Recalculate. Confirm this is not forward P/E or trailing-four-quarter P/E. |  |  |  |
| LMT peer: total sales $75,048 million current and $71,043 million prior; operating profit $7,731 million current and $7,013 million prior; margin 10.3014%. | [LMT 10-K index](https://www.sec.gov/Archives/edgar/data/936468/000162828026004195/0001628280-26-004195-index.htm) | Saved LMT 10-K lines 853-870 | Compare statement units, total-sales label, operating-profit label, periods, and Python formula. |  |  |  |
| NOC peer: total sales $41,954 million current and $41,033 million prior; operating income $4,511 million current and $4,370 million prior; margin 10.7523%. | [NOC 10-K index](https://www.sec.gov/Archives/edgar/data/1133421/000113342126000003/0001133421-26-000003-index.htm) | Saved NOC 10-K lines 1076-1090 | Compare statement units, total-sales label, operating-income label, periods, and Python formula. |  |  |  |
| NOC gain on sale of business: $231 million. | [NOC 10-K index](https://www.sec.gov/Archives/edgar/data/1133421/000113342126000003/0001133421-26-000003-index.htm) | Saved NOC 10-K lines 1088-1090 | Confirm the gain is included in reported GAAP operating income and that no adjusted figure is substituted. |  |  |  |

## Template and report-structure checks

| Requirement | Report evidence to inspect | What to compare | Human mark | Error count | Partner field |
|---|---|---|---|---|---|
| Company and filings on line one | Report line 1 | Confirm RTX and all listed filing accessions appear on the first line. |  |  |  |
| Fallback label on line two | Report line 2 | Confirm `MANUAL CHATGPT FALLBACK` appears on line two. |  |  |  |
| Run time below headers | Report line 3 | Confirm the run time is below the first two lines. |  |  |  |
| Five required report parts | Sections 1 through 5 | Confirm Overview; Market Positioning and Growth Outlook; Valuation Insights; Future Developments and Strategic Recommendations; Investment Recommendation. |  |  |  |
| Sources and accession numbers | Source register and claim tables | Confirm factual claims identify a source filing or market-data source and accession where applicable. |  |  |  |
| GAAP/non-GAAP separation | Financial tables and narrative | Confirm GAAP facts are not replaced by adjusted EPS, adjusted operating profit, or company-reported non-GAAP FCF. |  |  |  |
| Missing or unverified evidence | Remaining requirements | Confirm the limited 10-Q review, parser limitation, peer verification, and pending checks are disclosed. |  |  |  |
| Human and partner fields | Entire report | Confirm the report does not claim human verification, partner selection, or completed partner checks. |  |  |  |

## Recommendation checks

| Check | Report evidence to inspect | What to compare | Human mark | Error count | Partner field |
|---|---|---|---|---|---|
| Recommendation is explicit | Section 5: HOLD, explicitly provisional | Confirm the recommendation is labeled provisional. |  |  |  |
| Deciding number is named | Section 5: 39.23x price divided by FY2025 GAAP diluted EPS | Recalculate `$194.60 / $4.96`; confirm it is not presented as proof of overvaluation or fair value. |  |  |  |
| Uncertainty is stated | Section 5 uncertainty paragraph | Confirm no fair-value benchmark, required return, price target, or comparable valuation is invented. |  |  |  |
| Evidence supports reasoning | Sections 2-5 | Compare operating evidence, peer margins, NOC gain limitation, and valuation uncertainty with the provisional HOLD rationale. |  |  |  |
| No unsupported target | Valuation Insights and Recommendation | Confirm no fair-value multiple, price target, or implied upside is supplied. |  |  |  |

## Review notes

- Human verification status: ____________________
- Partner-check status: ____________________
- Additional issue notes: ________________________________________________________________
- Final error count: ____________________
