# FIN 671 Lab 2 Progress

Date: 2026-10-29

## Completed work

- Updated Step 6 to label each release column as Quarterly, Annual, or Interim.
- Preserved the source week or month count, the ending date, and the release table units.
- The label logic does not require a 13-week quarter.
- Step 6 output is saved beside `facts.json` as `step6_output.txt`.
- Confirmed that the saved Costco folder contains the 10-K, 10-Q, 8-K, Exhibit 99.1, `facts.json`, and `step6_output.txt`.
- Reran `COST --peers WMT,TGT,BJ` without `--price`.
- The rerun completed successfully with exit code 0 and no reported errors.
- Confirmed diluted EPS for Costco and Walmart, current debt for Target, and aligned prior-year debt dates for BJ's.

## Latest output folder

`readings/COSTCO WHOLESALE CORP _NEW_20261029_212627`

## Revenue-selection correction

- Corrected the general-purpose revenue candidate priority to prefer the broad SEC XBRL `Revenues` concept when it is available for the latest fiscal period. The existing fiscal-period and filing-date selection remains in effect, and no company or value is hardcoded.
- Walmart now uses `Revenues`: current `713,163,000,000` and prior `680,985,000,000`, instead of net sales from `RevenueFromContractWithCustomerExcludingAssessedTax`.
- Walmart's corrected operating margin is `29,825,000,000 / 713,163,000,000 = 0.0418207338`.
- Costco, Target, and BJ's continue to use `RevenueFromContractWithCustomerExcludingAssessedTax` for their selected current fiscal periods because a newer current-period `Revenues` fact was not available.
- Reran `COST --peers WMT,TGT,BJ` after the correction. The run completed successfully with exit code 0 and no reported errors.

## Four-role desk

- Added the Research Analyst, Financial Analyst, Investment Advisor, and Strategy Manager workflow on top of the seven Lab 2 steps.
- Added the official `google-genai` package to the existing `.venv` and `requirements.txt`.
- The configured model is `gemini-3.8-flash`; the desk reads `API_KEY` from `.env` without displaying it.
- The desk command is `.\.venv\Scripts\python.exe .\equity_research.py TICKER --peers PEER1,PEER2 --price PRICE --desk`.
- Python compilation and CLI help checks passed.
- An end-to-end API test did not produce a report: `gemini-2.5-flash` was unavailable to new users, and a minimal request to `gemini-3.8-flash` returned a Google `504 DEADLINE_EXCEEDED`. Quota and billing availability are unknown.
- The model-availability check listed `gemini-3.8-flash` and `gemini-2.5-flash-lite`. A bounded fallback command can select `gemini-2.5-flash-lite` with `--model`; that fallback was prepared but not tested.
- No billing or account settings were changed. Human verification, partner checks, and desk-report review remain pending.

## Unresolved issues

- Human verification against the source filings is still pending.
- Partner checks are still pending.
- No human audit marks have been assigned.

## Next steps

- Complete human verification against the saved 10-K, 10-Q, 8-K, and Exhibit 99.1 files.
- Complete partner checks.
- Record any approved corrections after those checks.
