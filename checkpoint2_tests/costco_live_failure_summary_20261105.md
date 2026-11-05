# Costco live run failure and offline request inspection

## Checks that passed

- The user reported that Streamlit opened successfully in the browser.
- Offline UI, graph, and persona checks passed. The offline provider-boundary test confirmed that each completed persona reaches its matching role instruction.
- Both UTF-8 capture tests passed, including malformed bytes, a legacy console, and a nonzero process exit.
- The fixed capture wrapper captured the live run through Steps 1-7 and its terminal error without an encoding crash.

## Unsuccessful live run

- One workflow attempt used `gemini-3.5-flash-lite`, peers WMT/TGT/BJ, and historical practice price USD 992.13 dated October 27, 2026, not the current price.
- Research Analyst failed: HTTP 503, provider status UNAVAILABLE.
- Provider message: This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.
- No analyst role completed. Financial Analyst, Investment Advisor, Strategy Manager, and mandatory Verifier were not reached.
- Exit code: 1. No report, verification marks, model verification, or completed graph trace was produced.
- Execution log: `checkpoint2_tests/costco_live_execution_20261105_083540_127635.txt`.
- Sources, facts, and Step 6 output: `readings/COSTCO WHOLESALE CORP _NEW_20261105_083541/`.
- The preceding attempt failed in its output-capture wrapper; that is separate from this provider failure.

## Offline reconstruction of the Research Analyst request

The request body itself was not saved at failure time. These counts reconstruct its inputs from the current request-building code and that run's saved evidence, with a stub intercepting the generation boundary. No API calls were made for this inspection. Counts are Python Unicode character counts, not token counts or complete HTTP wire sizes.

| Component | Characters |
| --- | ---: |
| Role instructions | 706 |
| Completed persona, stripped as the loader does | 3,125 |
| Persona separator/label | 56 |
| Business excerpt, including line numbers | 20,112 |
| MD&A excerpt, including line numbers | 29,301 |
| Earnings release, including line numbers | 9,182 |
| Structured facts | 0 |
| Other context and JSON serialization overhead | 1,223 |
| Total input text | 63,705 |

System instruction: 3,887 characters. Serialized contents: 59,818 characters. Other context includes the task, expected output, form/accession metadata, file paths, excerpt bounds, and JSON syntax/escaping. Financial and peer facts are prepared by the workflow but are not included in the Research Analyst packet.

## Source coverage and duplication

- Business: 10-K lines 131-219, 89 lines.
- MD&A: 10-K lines 396-538, 143 lines.
- The 10-K has 1,562 lines. The two excerpts do not overlap and stop at the intended section boundaries; neither hits the existing 500-line limit.
- The complete earnings release is included: 144 lines, 8,571 source characters before line numbering. The code intentionally includes the full release.
- No complete 10-K or 10-Q text is included. Listing a filing accession does not include that filing's text.
- No identical source lines of at least 80 characters repeat within or across Business, MD&A, and the release. This exact-line check does not exclude semantic repetition of facts.
- The Insight instruction appears in both the role instructions and persona. This is small instruction repetition, not duplicated source evidence.

## Proposed reduction; not applied

There is no demonstrated unnecessary bulk duplication to remove. A focused candidate is the executive-officer roster and biographies at 10-K lines 200-219 within the Business excerpt. If excluded, retain any management-change evidence relevant to recent developments or company history. Keep original source line numbers and original saved filings. Retain the business model, segments, revenue drivers, MD&A, and release evidence. The small repeated Insight instruction could be consolidated separately if both instruction files remain consistent.

Do not reduce the source evidence merely to respond to this 503: the provider reported high demand, and no evidence establishes that this request's size caused the failure. Source selection and any source-quality issues remain distinct from service availability. The request and source files were not changed by this inspection. No retry, model switch, billing change, commit, or push was performed.
