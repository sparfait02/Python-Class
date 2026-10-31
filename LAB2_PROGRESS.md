# FIN 671 Lab 2 Progress

Date: 2026-10-29

Professor's revised Checkpoint 1 deadline: November 3, 2026, 11:59 p.m. Eastern.

## Completed work

- Partner confirmed RTX as the company for the report on October 31, 2026. The partner's two source checks are still pending.
- Completed LMT and NOC revenue and operating-income XBRL-tag checks against `PEER_XBRL_EVIDENCE.md` and matching SEC records retrieved by ChatGPT. The partner's two checks remain pending.
- Copied only the Costco and Walmart `facts.json` outputs into tracked `submission_data/` with provenance-preserving filenames.
- Updated Step 6 to label each release column as Quarterly, Annual, or Interim.
- Preserved the source week or month count, the ending date, and the release table units.
- The label logic does not require a 13-week quarter.
- Step 6 output is saved beside `facts.json` as `step6_output.txt`.
- Confirmed that the saved Costco folder contains the 10-K, 10-Q, 8-K, Exhibit 99.1, `facts.json`, and `step6_output.txt`.
- Reran `COST --peers WMT,TGT,BJ` without `--price`.
- The rerun completed successfully with exit code 0 and no reported errors.
- Confirmed diluted EPS for Costco and Walmart, current debt for Target, and aligned prior-year debt dates for BJ's.

## Latest output folder

`readings/COSTCO WHOLESALE CORP _NEW_20261029_221033`

## Costco Lab 3 fallback

- Created `COST_FALLBACK_INPUT.md` from the latest complete saved Costco run.
- Created `COST_FALLBACK_PROMPT.md` for the manual ChatGPT fallback.
- No Gemini API calls were made for the Costco fallback.
- The input includes the saved Costco filings, annual facts, Step 6 output,
  corrected WMT/TGT/BJ peer facts, source references, and missing-evidence labels.
- Walmart uses the corrected `Revenues` tag for consolidated total revenues,
  not net sales. Its current operating margin is 4.182073%.
- Verified Costco's October 27, 2026 regular-session Close as $992.13 from the
  FinancialContent historical-price page. The calculation is $992.13 / $20.76 =
  47.790462x using FY2026 GAAP diluted EPS.
- The input records that the peer facts JSON does not retain peer Accepted
  timestamps and that the 10-Q was identified but not substantively reviewed.

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
- No billing or account settings were changed. Student audit checks are recorded; remaining student audit items, partner checks, and desk-report review remain pending.

## Unresolved issues

- Remaining student audit items are pending where not recorded in RTX_AUDIT.md.
- Partner selection is complete: the partner confirmed RTX as the report company.
- Two partner checks are still pending.
- LMT and NOC value, margin, disposal-gain, and revenue/operating-income XBRL-tag checks are recorded as complete.
- Outstanding Costco practice-report and audit work remains.
- No Costco practice-report or audit document was found in the workspace; only Costco run artifacts and Lab 2 worksheets were found.
- `submission_data/` contains `COSTCO_WHOLESALE_CORP__facts__run_20261029_221033.json` from the Costco run and `Walmart_Inc__facts__run_20261031_162405.json` from the Walmart SEC data run.
- Remaining unmarked student audit items are not assigned new marks here.

## RTX audit summary

- Existing audit marks, excluding the duplicate equity row labeled `Covered by Core Claim 6`: Correct `36`; Wrong `0`; Unsupported `0`; Missing `0`.
- Errors, calculated as Wrong plus Unsupported: `0`.
- Missing is reported separately: `0`.
- The duplicate equity row is excluded from pending-item counts.
- Partner fields and final error count remain blank.

## Next steps

- Complete the student audit against the saved 10-K, 10-Q, 8-K, and Exhibit 99.1 files.
- Complete the two partner source checks.
- Complete the outstanding Costco practice-report and audit work.
- Complete final commit, push, and submission by November 3, 2026, 11:59 p.m. Eastern.
- Record any approved corrections after those checks.
