# RTX Manual ChatGPT Fallback Prompt

**Explicit label:** `MANUAL CHATGPT FALLBACK — RTX`

Use `RTX_FALLBACK_INPUT.md` as the only source packet. Do not browse for extra facts. Do not use a stock price. Do not invent figures, dates, filing references, quotes, or conclusions. If a required fact is missing or unverified, label it `Missing` or `Unverified`.

## Source and report rules

1. Every factual claim must cite the source filing or earnings exhibit, accession number, and source line when a local line reference is provided.
2. Every annual fact must state its tag, unit, current period, prior period, and source statement.
3. Every release figure must state whether it is GAAP or non-GAAP, its unit, period, and source line.
4. Every peer number must use total revenue consistently, cite the peer 10-K accession, and show the period.
5. Show every ratio's formula and inputs. Do not calculate a P/E ratio until a verified price and date are supplied.
6. State the RTX Step 6 parser limitation: release units and columns were not extracted by the automated output, although the source exhibit contains a Q3 table.
7. Keep the first report line in this exact form: `MANUAL CHATGPT FALLBACK — Filings read: [form and accession list]`.
8. Keep the second report line in this exact form: `Run time: [runtime]`.
9. Do not assign human audit marks or partner-check marks.

## Course roles

Run the roles in this order. Treat each role as a separate pass. The Strategy Manager sends each role only a JSON object containing `task`, `context`, and `expected_output`. The role must not use information outside that JSON object.

### 1. Research Analyst

Task: Analyze the business model, competitive position, catalysts, and recent developments from the 10-K Business and MD&A excerpts and the earnings release.

Rules: Every claim must include a short quote and its source line. Separate reported facts from interpretation. Identify missing or unverified evidence. Do not invent a catalyst, competitor, development, or date.

Expected output: JSON with `business_model`, `competitive_position`, `catalysts`, `recent_developments`, `evidence`, and `gaps`.

### 2. Financial Analyst

Task: Analyze the Step 4 annual facts, Step 5 Python ratios, Step 6 Q3 release, and Step 7 peers.

Rules: Every number must include its filing, accession, tag or source line, unit, and period. State the definition whenever the filing provides two definitions. Show the arithmetic for every ratio using the supplied Python results. Never compute new arithmetic in the model. If another ratio is needed, request it from a calculator and do not calculate it in the model. Keep GAAP and non-GAAP measures separate.

Expected output: JSON with `statement_analysis`, `quarter_analysis`, `peer_analysis`, `valuation_insights`, `calculator_requests`, `evidence`, and `gaps`.

### 3. Investment Advisor

Task: Produce a thesis and one recommendation: Buy, Hold, or Sell.

Rules: Use only the Research Analyst and Financial Analyst outputs. Do not use raw filings, outside information, or an unverified price. Identify the one number that decides the recommendation. If the evidence is insufficient, state that no supported recommendation can be made.

Expected output: JSON with `thesis`, `recommendation`, `deciding_number`, `rationale`, `evidence`, and `gaps`.

### 4. Strategy Manager

Task: Check that the five report parts are present and consistent. If a part fails, send that part back to its role once with a JSON object containing `task`, `context`, and `expected_output`. Then compile the final report.

Required report parts, in this order:

1. Overview
2. Market Positioning and Growth Outlook
3. Valuation Insights
4. Future Developments and Strategic Recommendations
5. Investment Recommendation

Rules: Use only the role outputs and the source citations they contain. Do not add unsupported claims. State missing evidence. Keep the explicit fallback label, filings and accessions on line 1, and run time on line 2. Do not assign human audit marks or partner-check marks.

Expected output: Markdown report with the five required headings, source citations, formula-based financial analysis, and an explicit `MANUAL CHATGPT FALLBACK` label.

## Strategy Manager input contract

```json
{
  "task": "Check and compile the RTX manual fallback report.",
  "context": {
    "source_packet": "RTX_FALLBACK_INPUT.md",
    "research_analyst": "[role output]",
    "financial_analyst": "[role output]",
    "investment_advisor": "[role output]"
  },
  "expected_output": "Markdown with the five required report sections and source citations."
}
```

## Final report limitations

- Price and price date: **Missing**.
- P/E: **Unavailable** until a verified price and date are supplied.
- RTX release-table units and columns in automated Step 6 output: **Unverified by parser; available in the source Exhibit 99 excerpt**.
- Financial-statement line references: **Not retained for the XBRL facts; use tags, accessions, periods, and named statements**.
- Human verification and partner checks: **Pending**.
