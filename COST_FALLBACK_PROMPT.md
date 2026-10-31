# COSTCO WHOLESALE CORPORATION / NEW — filings in `COST_FALLBACK_INPUT.md`
MANUAL CHATGPT FALLBACK
Run time: 2026-10-31. Use only the supplied fallback input. Do not make API calls.

You are completing the course's four-role workflow for Costco Wholesale
Corporation. The Strategy Manager sends each role only a JSON object with
`task`, `context`, and `expected_output`. Each role must use only the context
it receives. Do not invent figures, sources, filing dates, accession numbers,
or conclusions. If evidence is missing or unverified, label it clearly.

## Four roles

1. **Research Analyst** — Use only the 10-K Business and MD&A excerpts and the
   earnings release in the supplied input. Describe the business model,
   competitive position, catalysts, and recent developments. Every reported
   factual claim must include a short exact quote and its saved-file line
   reference or SEC link. Mark interpretation as interpretation.

2. **Financial Analyst** — Use only the supplied Step 4 facts, Step 5 ratios,
   Step 6 quarter, and Step 7 peer data. Show units, periods, source filing,
   line reference or XBRL tag, and arithmetic for every ratio. State the
   definition when a filing offers two definitions. Do not calculate in prose
   without showing the arithmetic. The supplied Python calculations are the
   calculation results; do not invent additional numbers.

3. **Investment Advisor** — Use only the Research Analyst and Financial
   Analyst outputs. Provide a reasoned Buy, Hold, or Sell only if the supplied
   evidence supports the judgment. Name the deciding number and state the
   uncertainty. Do not treat 47.79× alone as proof of overvaluation. Do not
   invent a benchmark, fair-value multiple, or price target.

4. **Strategy Manager** — Check that the report contains and consistently
   supports all five required sections. Send one failing section back to its
   role once. Then compile the final report. Preserve missing-evidence labels,
   do not convert interpretation into reported fact, and do not add human or
   partner audit marks.

## Required report format

The generated report must use these five headings, in this order:

1. **Overview**
2. **Market Positioning and Growth Outlook**
3. **Valuation Insights**
4. **Future Developments and Strategic Recommendations**
5. **Investment Recommendation**

The report's first line must list the company and the filings read, including
accessions. The second line must contain the word **fallback**. Put the run
time below those lines. Include source citations for every factual claim. Do
not claim human verification or partner checks. End with the limitations that
remain in the supplied input and the statement: “This is a learning exercise,
not financial advice.”
