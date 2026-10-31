# COST Report Audit Worksheet

Purpose: audit `COST_FALLBACK_REPORT.md` only. Earlier source checks are not
transferred into report-audit marks. Human marks, partner fields, and final
error counts remain blank unless explicitly recorded below.

## Sources

- K: [Costco 10-K, accession 0000909832-26-000093](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm); saved `readings/COSTCO WHOLESALE CORP _NEW_20261029_221033/10_K_0000909832-26-000093.txt`.
- E: [Costco Exhibit 99.1, accession 0000909832-26-000084](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/costex9918-k92426.htm); saved `readings/COSTCO WHOLESALE CORP _NEW_20261029_221033/8_K_Exhibit_99_1_0000909832-26-000084_costex9918-k92426.htm.txt`.
- P: [FinancialContent COST history](https://www.financialcontent.com/quote/NQ%3ACOST/historical).
- W: [Walmart 10-K index](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm).
- T: [Target 10-K index](https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/0000027419-26-000016-index.htm).
- B: [BJ's 10-K index](https://www.sec.gov/Archives/edgar/data/1531152/000153115226000007/0001531152-26-000007-index.htm).

Saved packet: `readings/COSTCO WHOLESALE CORP _NEW_20261029_221033/`.
Peer facts are in its `facts.json`, line 1. Separate TGT/BJ text files were not
saved. The Costco `LAB2_VERIFICATION.md` human and partner fields are blank.

## Recorded grouped human review

- TGT and BJ figures, USD units, exact year-ending periods, revenue definitions,
  operating income, and calculated margins: reviewed and acceptable.
- Costco's four pending XBRL tags, annual records, values, and units: reviewed
  and acceptable. This records the user's review of the evidence. ChatGPT's
  independent SEC retrieval is separate supporting evidence; it is not claimed
  as retrieval performed by the user.
- Report headers, five required sections, provisional HOLD reasoning, and
  limitation disclosures: reviewed and acceptable.

These grouped reviews do not complete partner fields or the final error count.

## Audit fields

- Auditor: Samuel Parfait
- Date started: October 31, 2026
- Date completed: October 31, 2026
- Total errors: 0
- Partner name: ____________________
- Partner check 1: ____________________
- Partner check 2: ____________________

## Final student-audit summary

Final recorded review items, counted at the individual-check level:

- Correct: `32` — eleven core claims; four FY2025 supporting inputs; Walmart;
  two valuation checks; planned capex; CFO discrepancy; four TGT/BJ checks;
  four Costco XBRL-tag checks; and four grouped format/recommendation/limitation
  checks.
- Wrong: `0`.
- Unsupported: `0`.
- Missing: `0`.
- Student errors, calculated as Wrong plus Unsupported: `0`.

No new marks are assigned. Pending partner checks are excluded from these
totals. Partner name and both partner checks remain blank.

Reconciliation note: the grouped review already recorded in this worksheet
supersedes stale table wording that described the four Costco XBRL checks as
pending. It also records the headers, five sections, provisional HOLD reasoning,
and limitation disclosures as reviewed and acceptable.

Unresolved limitations: the 10-Q was identified but not substantively reviewed;
peer Accepted times were not retained; separate TGT/BJ text files were not
saved; the CFO discrepancy's cause remains unresolved; and partner checks are
pending. Correct disclosure of a limitation does not remove the limitation.

## Core claims

The following exact statement and arithmetic checks were recorded from the
user's confirmations. Tag checks are separate and are not marked complete by
these confirmations.

| # | Report claim | Source and saved lines | Units and period | Human mark | Tag status |
|---:|---|---|---|---|---|
| 1 | Total revenue: FY2026 $303,154 million; FY2025 $275,235 million. | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), 10-K lines 615–643; `facts.json` line 1 | USD millions; 52 weeks ended Aug. 30, 2026 and Aug. 31, 2025 | Correct — statement figures | XBRL pending |
| 2 | Revenue growth: `(303,154 - 275,235) / 275,235 × 100 = 10.143695%`. | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 615–643; report Section 3 | Percentage; FY2026 over FY2025 | Correct | Not applicable |
| 3 | Operating income $11,685 million; margin `11,685 / 303,154 × 100 = 3.854477%`. | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 615–643; `facts.json` line 1 | USD millions and percentage; FY2026 | Correct — figure and arithmetic | XBRL pending |
| 4 | Net income: FY2026 $9,226 million; FY2025 $8,099 million. | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 615–643; `facts.json` line 1 | USD millions; FY2026 and FY2025 | Correct — statement figures | XBRL pending |
| 5 | Diluted EPS: FY2026 $20.76; FY2025 $18.21. | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 637–642; `facts.json` line 1 | USD/share; FY2026 and FY2025 | Correct — statement figures | XBRL pending |
| 6 | ROE: `9,226 / ((35,803 + 29,164) / 2) × 100 = 28.402112%`. | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 664–706 and 615–643; report Section 3 | Percentage; FY2026 income over average equity at Aug. 31, 2025 and Aug. 30, 2026 | Correct | Supporting inputs covered here |
| 7 | Debt/equity: `(3,914 + 2,248) / 35,803 = 0.172108×`. | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 682–706; report Section 3 | Ratio; Aug. 30, 2026 balance sheet | Correct | Supporting inputs covered here |
| 8 | Course-defined FCF: `15,817 - 6,435 = $9,382 million`. | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 747–794; report Section 3 | USD millions; FY2026 52 weeks | Correct | Supporting inputs covered here |
| 9 | Quarterly total revenue: $95,723 million versus $86,156 million. | [E](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/costex9918-k92426.htm), lines 31–43; `step6_output.txt` lines 1–13 | USD millions; 16 weeks ended Aug. 30, 2026 and Aug. 31, 2025; unaudited | Correct | Supporting input covered here |
| 10 | Total-revenue growth: `(95,723 - 86,156) / 86,156 × 100 = 11.104276%`, distinct from 11.2% net-sales growth. | [E](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/costex9918-k92426.htm), lines 10 and 40–43; report Section 2 | Percentage; comparable 16-week quarters | Correct | Not applicable |
| 11 | Quarterly GAAP diluted EPS: $6.75 versus $5.87. | [E](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/costex9918-k92426.htm), lines 31–39 and 54–59; `step6_output.txt` lines 1–20 | USD/share; 16 weeks ended Aug. 30, 2026 and Aug. 31, 2025; unaudited | Correct | Supporting input covered here |

## Remaining numerical checks

Only figures stated in `COST_FALLBACK_REPORT.md` are listed. Completed core
duplicates are referenced above and are not repeated as new checks.

| Report location | Remaining report claim | Source | Expected value; units and period | Calculator or comparison instruction | Human mark |
|---|---|---|---|---|---|
| Section 1 annual table | FY2025 supporting inputs: equity, noncurrent debt, current debt, CFO, and capex | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 664–706 and 747–794 | Equity $29,164m; noncurrent debt $5,713m; current debt $75m; CFO $13,335m; capex $(5,498)m; FY2025 at Aug. 31, 2025 | Equity is covered by completed Core Claim 6. Compare each other value with the statement label, unit, date, and cash-outflow sign. | Equity: covered by Core Claim 6; noncurrent debt: Correct; current debt: Correct; CFO: Correct; capex: Correct |
| Section 3 peer comparison | WMT revenue $713,163m / $680,985m; operating income $29,825m / $29,348m; margin `29,825 / 713,163 × 100 = 4.182073%` | [W](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm); `facts.json`, line 1 | USD millions; years ended Jan. 31, 2026 and Jan. 31, 2025; revenue tag `Revenues` | Confirm consolidated total revenue, not Walmart net sales; recalculate margin. | Correct |
| Section 3 peer comparison | TGT revenue $104,780m / $106,566m; operating income $5,117m / $5,566m; margin `5,117 / 104,780 × 100 = 4.883566%` | [T](https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/0000027419-26-000016-index.htm); `facts.json`, line 1 | USD millions; years ended Jan. 31, 2026 and Feb. 1, 2025 | Confirm revenue and operating-income tags, periods, units, and margin. |  |
| Section 3 peer comparison | BJ revenue $21,457.274m / $20,501.804m; operating income $816.604m / $772.206m; margin `816.604 / 21,457.274 × 100 = 3.805721%` | [B](https://www.sec.gov/Archives/edgar/data/1531152/000153115226000007/0001531152-26-000007-index.htm); `facts.json`, line 1 | USD millions after conversion from source thousands; years ended Jan. 31, 2026 and Feb. 1, 2025 | Confirm source-unit conversion, tags, periods, and margin. |  |
| Section 3 valuation | Regular-session Close $992.13 on Oct. 27, 2026 | [P](https://www.financialcontent.com/quote/NQ%3ACOST/historical) | USD/share; unadjusted Close | Confirm date, ticker, regular-session Close, and that Adjusted Close was not used. | Correct |
| Section 3 valuation and Section 5 recommendation | Price divided by latest annual GAAP diluted EPS: `$992.13 / $20.76 = 47.790462×`, or 47.79× | [P](https://www.financialcontent.com/quote/NQ%3ACOST/historical) and [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 637–642 | Ratio; Oct. 27, 2026 price / FY2026 EPS | Recalculate and confirm the label is not forward P/E or trailing-four-quarter P/E. | Correct |
| Section 4 planning statement | Planned FY2027 capital expenditure approximately $7,500m, subject to change | [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 513–514 | USD millions; management intention for FY2027 | Confirm it is a stated plan, not realized spending or a guaranteed forecast. | Correct |
| Section 4 evidence discrepancy | Release CFO $15,825m versus audited 10-K CFO $15,817m; FY2025 release and 10-K both $13,335m | [E](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/costex9918-k92426.htm), lines 108–124; [K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm), lines 747–767 and 810 | USD millions; FY2026 and FY2025 | Confirm the $8m difference and that the report states the cause is unresolved. Do not claim the reclassification note proves the cause. | Correct |

## Format and recommendation checks

| Report location | Check | Source or evidence | Comparison instruction | Human mark |
|---|---|---|---|---|
| Lines 1–3 | Company/filings on line one; `fallback` on line two; run time below | `COST_FALLBACK_REPORT.md` lines 1–3 | Confirm company, accessions, fallback label, and run date. |  |
| Sections 1–5 | Required headings and eleven claims | Report headings and core table | Confirm all five sections and all core claims are present. |  |
| Sections 1–5 | Source register and GAAP/non-GAAP separation | K, E, P, W, T, B links; report limitations | Confirm direct sources, GAAP EPS, and the release benefit are not presented as adjusted EPS. |  |
| Section 5 | Provisional HOLD and deciding number | P/K; `$992.13 / $20.76 = 47.79×` | Confirm no benchmark, fair-value multiple, target price, or claim that 47.79× alone proves overvaluation. |  |
| Section 5 | Uncertainty and limitations | Report Section 5 and ending disclosures | Confirm limited 10-Q review, peer-file limitations, unresolved CFO discrepancy, and pending human/partner review. |  |

## Review notes

- Human verification status: ____________________
- Partner-check status: ____________________
- Additional issue notes: ________________________________________________________________
- Final error count: ____________________
