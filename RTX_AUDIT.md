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
| 1 | Annual total revenue: FY2025 $88,603 million; FY2024 $80,738 million; tag `RevenueFromContractWithCustomerExcludingAssessedTax`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1086-1110; local `10_K_0000101829-26-000006.txt` | Human check recorded for statement units and year columns: FY2025 $88,603 million and FY2024 $80,738 million. XBRL tag check recorded as Correct: tag, USD unit, annual periods, values, and accessions matched records retrieved directly from SEC by ChatGPT and matched the checked total-net-sales statement figures. | Correct |  |  |
| 2 | Annual revenue growth: `(88,603 - 80,738) / 80,738 = 9.7414%`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1086-1110; Python calculation in report | Human check recorded using Windows Calculator: `(88,603 - 80,738) / 80,738 x 100`, approximately 9.7414%. | Correct |  |  |
| 3 | Operating income and operating margin: $9,300 million; `$9,300 / $88,603 = 10.4963%`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1086-1110 and MD&A lines 470-475 | Human check recorded for FY2025 operating profit of $9,300 million and independent operating-margin calculation of approximately 10.4963%. Compare the operating-profit label, units, periods, and formula with total net sales. | Correct |  |  |
| 4 | Attributable net income: FY2025 $6,732 million; FY2024 $4,774 million; tag `NetIncomeLoss`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1106-1108; saved facts metadata for concept label | Human check recorded for FY2025 net income attributable to common shareowners of $6,732 million and FY2024 of $4,774 million after noncontrolling interest. XBRL tag check recorded as Correct: attributable-to-parent label, USD unit, annual periods, values, and accessions matched records retrieved directly from SEC by ChatGPT. | Correct |  |  |
| 5 | Annual GAAP diluted EPS: FY2025 $4.96; FY2024 $3.55; tag `EarningsPerShareDiluted`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1108-1110 | Human check recorded for the annual diluted EPS row: FY2025 $4.96 and FY2024 $3.55, attributable to common shareowners. XBRL tag check recorded as Correct: extracted tag, unit, annual periods, values, and accessions matched records retrieved directly from SEC by ChatGPT. | Correct |  |  |
| 6 | Return on average equity: `$6,732 / (($65,245 + 60,156) / 2) = 10.7368%`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1106-1108 and 1140-1180; Python calculation in report | Human check recorded: 2025 equity $65,245 million and 2024 equity $60,156 million average to $62,700.5 million; `6,732 / 62,700.5 x 100` is approximately 10.7368%. Compare numerator definition, dates, units, and rounding. | Correct |  |  |
| 7 | Debt/equity including current long-term debt: `($34,288 + $3,412) / $65,245 = 0.5778`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1140-1180; Python calculation in report | Human check recorded: FY2025 long-term debt $34,288 million, current portion $3,412 million, and shareowners' equity $65,245 million; `(34,288 + 3,412) / 65,245` is approximately 0.5778x. Compare balance-sheet date and whether other liabilities were included. | Correct |  |  |
| 8 | CFO minus capex: `$10,567 - $2,627 = $7,940 million` course-defined FCF. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | RTX 10-K lines 1200-1213; Python calculation in report | Human check recorded: FY2025 operating cash flow $10,567 million less capital expenditures $2,627 million gives course-defined FCF of $7,940 million. Compare signs, units, annual period, and the label that this is a course calculation rather than necessarily RTX’s reported FCF. | Correct |  |  |
| 9 | Quarterly total revenue: Q3 2026 $24,965 million; Q3 2025 $22,478 million. | [RTX Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) | Exhibit lines 131-135 | Human check recorded: quarterly net sales are $24,965 million for Q3 2026 and $22,478 million for Q3 2025, using the quarter-ended-September-30 columns and the statement's units. | Correct |  |  |
| 10 | Quarterly revenue growth: release 11%; Python `(24,965 - 22,478) / 22,478 = 11.0642%`. | [RTX Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) | Exhibit lines 14-16 and 131-135; Python calculation in report | Human check recorded: `(24,965 - 22,478) / 22,478 x 100` is approximately 11.0642%, consistent with the release's rounded 11%. Compare the comparable quarter, denominator, units, and rounding. | Correct |  |  |
| 11 | Quarterly GAAP diluted EPS: Q3 2026 $1.89; Q3 2025 $1.41. | [RTX Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) | Exhibit lines 150-152 | Human check recorded: quarterly GAAP diluted EPS is $1.89 for Q3 2026 and $1.41 for Q3 2025 in the quarter-ended-September-30 columns. Compare the USD/share unit and GAAP status. | Correct |  |  |

## Supporting annual inputs

| Report claim | Source link | Saved-file lines | What to compare and completed-core reference | Human mark | Error count | Partner field |
|---|---|---|---|---|---|---|
| Covered by Core Claim 6 — stockholders' equity: FY2025 $65,245 million; FY2024 $60,156 million; tag `StockholdersEquity`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1140-1180 | Duplicate input covered by completed Core Claim 6; excluded from pending-item counts. No additional check is requested here. |  |  |  |
| Long-term debt: FY2025 $34,288 million; FY2024 $38,726 million; tag `LongTermDebtAndCapitalLeaseObligations`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1140-1180 | Duplicate input. FY2025 $34,288 million is covered by completed Core Claim 7. Human check recorded for FY2024 $38,726 million. | Correct |  |  |
| Current long-term debt: FY2025 $3,412 million; FY2024 $2,352 million; tag `LongTermDebtAndCapitalLeaseObligationsCurrent`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1140-1180 | Duplicate input. FY2025 $3,412 million is covered by completed Core Claim 7. Human check recorded for FY2024 $2,352 million. | Correct |  |  |
| Cash from operations: FY2025 $10,567 million; FY2024 $7,159 million; tag `NetCashProvidedByUsedInOperatingActivities`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1200-1213 | Duplicate input. FY2025 $10,567 million is covered by completed Core Claim 8. Human check recorded for FY2024 $7,159 million. | Correct |  |  |
| Capital expenditures: FY2025 $2,627 million; FY2024 $(2,625) million cash outflow; tag `PaymentsToAcquirePropertyPlantAndEquipment`. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 1200-1213 | Duplicate input. FY2025 $2,627 million is covered by completed Core Claim 8. Human check recorded for FY2024 $(2,625) million cash outflow. | Correct |  |  |

## Other financial numbers in the report

| Report number or claim | Source link | Saved-file line reference | What to compare | Human mark | Error count | Partner field |
|---|---|---|---|---|---|---|
| Annual operating margin definition: operating profit divided by total net sales; reported 2025 margin 10.5%. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 470-475 | Human check recorded: the filing defines operating profit margin as operating profit divided by total net sales and reports 10.5% for FY2025, consistent with the calculated 10.4963%. | Correct |  |  |
| Annual backlog: $268 billion at December 31, 2025; $218 billion at December 31, 2024; approximately 25% expected as revenue over next 12 months. | [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Lines 171-172 and 477 | Human check recorded: $268 billion at December 31, 2025; $218 billion at December 31, 2024; approximately 25% expected to become revenue over the following 12 months. This is management's expectation, not realized revenue. | Correct |  |  |
| Earnings-release backlog and awards: $340 billion total, including $176 billion commercial and $164 billion defense; Tomahawk and AMRAAM contracts. | [RTX Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/101829/000010182926000030/a2026-10x208xkerexhibit99.htm) | Lines 20-21 | Human check recorded: source release reports $340 billion total, including $176 billion commercial and $164 billion defense; `176 + 164 = 340`. Compare exact wording, current quarter, and whether the report treats awards as potential activity rather than guaranteed earnings. | Correct |  |  |
| Price: $194.60 regular-session unadjusted Close on October 27, 2026. | [StockAnalysis RTX history](https://stockanalysis.com/stocks/rtx/history/) | External source; no RTX filing line | Human check recorded: regular-session Close on October 27, 2026 was $194.60. Compare date, regular-session Close, and unadjusted Close. Do not substitute Adjusted Close. | Correct |  |  |
| Price divided by FY2025 GAAP diluted EPS: `$194.60 / $4.96 = 39.2338709677`, or 39.23x. | [StockAnalysis RTX history](https://stockanalysis.com/stocks/rtx/history/) and [RTX 10-K](https://www.sec.gov/Archives/edgar/data/101829/000010182926000006/rtx-20251231.htm) | Price external; EPS 10-K lines 1108-1110; Python calculation | Human check recorded: `$194.60 / $4.96` is approximately 39.23x. Keep the label as price divided by FY2025 GAAP diluted EPS, not forward P/E or trailing-four-quarter P/E. | Correct |  |  |
| LMT peer: total sales $75,048 million current and $71,043 million prior; operating profit $7,731 million current and $7,013 million prior; margin 10.3014%. | [LMT 10-K index](https://www.sec.gov/Archives/edgar/data/936468/000162828026004195/0001628280-26-004195-index.htm) | Saved LMT 10-K lines 853-870 | Human checks recorded: FY2025/FY2024 total sales are $75,048 million / $71,043 million; operating profit is $7,731 million / $7,013 million; `7,731 / 75,048 x 100` is approximately 10.3014%. XBRL-tag check recorded as Correct for revenue and operating-income tags, USD units, annual dates, values, and accessions, based on `PEER_XBRL_EVIDENCE.md` and matching SEC records retrieved by ChatGPT. | Correct |  |  |
| NOC peer: total sales $41,954 million current and $41,033 million prior; operating income $4,511 million current and $4,370 million prior; margin 10.7523%. | [NOC 10-K index](https://www.sec.gov/Archives/edgar/data/1133421/000113342126000003/0001133421-26-000003-index.htm) | Saved NOC 10-K lines 1076-1090 | Human checks recorded: FY2025/FY2024 sales are $41,954 million / $41,033 million; operating income is $4,511 million / $4,370 million; `4,511 / 41,954 x 100` is approximately 10.7523%. XBRL-tag check recorded as Correct for revenue and operating-income tags, USD units, annual dates, values, and accessions, based on `PEER_XBRL_EVIDENCE.md` and matching SEC records retrieved by ChatGPT. | Correct |  |  |
| NOC gain on sale of business: $231 million. | [NOC 10-K index](https://www.sec.gov/Archives/edgar/data/1133421/000113342126000003/0001133421-26-000003-index.htm) | Saved NOC 10-K lines 1088-1090 | Human check recorded: FY2025 gain on sale of business was $231 million and was included in reported operating income. Confirm no adjusted figure is substituted. | Correct |  |  |

Duplicate core inputs are not repeated as new checks: quarterly revenue is covered by Core Claim 9, and quarterly GAAP diluted EPS is covered by Core Claim 11. Adjusted EPS and quarterly cash-flow figures are not used in the current `RTX_FALLBACK_REPORT.md`; no audit rows are assigned to those absent measures.

## Template and report-structure checks

| Requirement | Report evidence to inspect | What to compare | Human mark | Error count | Partner field |
|---|---|---|---|---|---|
| Company and filings on line one | Report line 1 | Reviewed and acceptable: RTX and the listed filing accessions appear on the first line. | Correct |  |  |
| Fallback label on line two | Report line 2 | Reviewed and acceptable: `MANUAL CHATGPT FALLBACK` appears on line two. | Correct |  |  |
| Run time below headers | Report line 3 | Reviewed and acceptable: the run time is below the first two lines. | Correct |  |  |
| Five required report parts | Sections 1 through 5 | Reviewed and acceptable: Overview; Market Positioning and Growth Outlook; Valuation Insights; Future Developments and Strategic Recommendations; Investment Recommendation. | Correct |  |  |
| Sources and accession numbers | Source register and claim tables | Review recorded as acceptable for the displayed source-register wording. This is not blanket verification of every citation or peer XBRL mapping. | Correct |  |  |
| GAAP/non-GAAP separation | Financial tables and narrative | Review recorded as acceptable for the displayed GAAP/non-GAAP wording. This is not blanket verification of every citation or peer XBRL mapping. | Correct |  |  |
| Missing or unverified evidence | Remaining requirements | Review recorded as acceptable for the displayed evidence-limitations wording. This is not blanket verification of every citation or peer XBRL mapping. | Correct |  |  |
| Human and partner fields | Entire report | Review recorded as acceptable for the displayed human/partner-status wording. This is not blanket verification of every citation or peer XBRL mapping. | Correct |  |  |

## Recommendation checks

| Check | Report evidence to inspect | What to compare | Human mark | Error count | Partner field |
|---|---|---|---|---|---|
| Recommendation is explicit | Section 5: HOLD, explicitly provisional | Reviewed and acceptable: the recommendation is labeled provisional. | Correct |  |  |
| Deciding number is named | Section 5: 39.23x price divided by FY2025 GAAP diluted EPS | Reviewed and acceptable: `$194.60 / $4.96` is named and is not presented as proof of overvaluation or fair value. | Correct |  |  |
| Uncertainty is stated | Section 5 uncertainty paragraph | Reviewed and acceptable: no fair-value benchmark, required return, price target, or comparable valuation is invented. | Correct |  |  |
| Evidence supports reasoning | Sections 2-5 | Reviewed and acceptable: operating evidence, peer margins, NOC gain limitation, and valuation uncertainty are connected to the provisional HOLD rationale. | Correct |  |  |
| No unsupported target | Valuation Insights and Recommendation | Reviewed and acceptable: no fair-value multiple, price target, or implied upside is supplied. | Correct |  |  |

## Review notes

- Human verification status: ____________________
- Partner-check status: ____________________
- Additional issue notes: ________________________________________________________________
- Final error count: ____________________
