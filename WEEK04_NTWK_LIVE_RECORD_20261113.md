Filings read: 10-K 0001493152-26-044483; 10-Q 0001493152-26-051310; 8-K 0001493152-26-051655

# Week 4 live record ? NETSOL Technologies (NTWK)

**Evidence and timing.** This final copy reviews the November 13, 2026 earnings 8-K, accession **0001493152-26-051655**, Accepted **2026-11-13 14:39:11 Eastern**. Its Exhibit 99.1 is the release dated November 12, 2026, for fiscal Q1 2027, the three months ended September 30, 2026. The public release date precedes the EDGAR Accepted date; filing time is not asserted to be the first public release time. The saved draft's compilation time was 2026-11-13T16:22:42. This is retrospective finalization; no new before-reaction prediction or scored hit-rate observation is claimed.

**Verification provenance. Purdue verified the prior revision, not this final copy.** The prior revision and raw model response are preserved under `checkpoint2_tests/ntwk_revised_verification_20261113/`. This final copy receives only deterministic local verification. The prior 11 Correct core marks were comparisons with selected saved XBRL facts; they do not override a different definition in the filing. No analysts were rerun.

**Source keys.** K = saved `10_K_0001493152-26-044483.txt`; E = saved `8_K_Exhibit_99_1_0001493152-26-051655_ex99-1.htm.txt`. Line references below identify the original saved converted texts, not browser line numbers. Original files remain in `readings/NETSOL TECHNOLOGIES INC_20261113_161649/`.

- [K: annual filing index](https://www.sec.gov/Archives/edgar/data/1039280/000149315226044483/0001493152-26-044483-index.html)
- [E: earnings exhibit](https://www.sec.gov/Archives/edgar/data/1039280/000149315226051655/ex99-1.htm)
- [November 13 earnings 8-K index](https://www.sec.gov/Archives/edgar/data/1039280/000149315226051655/0001493152-26-051655-index.html); the saved 8-K identifies the earnings release as Exhibit 99.1 at lines 81-84 and 91-93. Accepted time is retained in the saved `filing_price.json`.

## Overview

**Read this qualification before the retained core register.** To preserve the prior 11 core claims and their citations, the register below is unchanged. Its annual revenue inputs are **reportable-segment revenue before intersegment eliminations**, not consolidated net revenue. Its growth calculation uses those inputs, and its retained operating-margin calculation divides consolidated operating income by that pre-elimination segment total. Those three labels must not be interpreted as independently validated consolidated measures. The source reconciliation immediately after the register gives the filing's consolidated figures. The local cached-fact Verifier cannot resolve this source-definition issue.

<!-- core-financials:start -->
**Required financial claims (Python calculations).**

Annual flow periods: 2025-07-01 through 2026-06-30 versus 2024-07-01 through 2025-06-30. ROE uses average equity; leverage uses ending equity.
Release annual columns: Missing.
USD millions except EPS (USD/share), percentages, and leverage (multiple).

| Fact | Current annual | Prior annual |
| --- | ---: | ---: |
| Total revenue | 78.145875 | 73.088687 |
| Operating income | 6.946665 | 3.501718 |
| Attributable net income | 2.950353 | 2.923233 |
| GAAP diluted EPS, USD/share | 0.25 | 0.25 |

| Calculation | Formula | Result |
| --- | --- | ---: |
| Revenue growth | (78.145875 - 73.088687) / 73.088687 * 100 | 6.919249% |
| Operating margin | 6.946665 / 78.145875 * 100 | 8.889356% |
| Return on average equity | 2.950353 / ((41.593925 + 37.833765) / 2) * 100 | 7.429029% |
| Debt/equity | (0.208107 + 8.18717) / 41.593925 | 0.201839 |
| Course-defined free cash flow | 13.884176 - 2.007114 | 11.877062 |

Quarterly periods (release; audit status not stated): Quarterly — Three Months Ended (September 30, 2026); Quarterly — Three Months Ended (September 30, 2025). Revenue below is in USD millions; GAAP diluted EPS is USD/share. Native dollar amounts are divided by 1,000,000 for the revenue table; EPS is not scaled.

| Quarterly fact | Current quarter | Prior quarter |
| --- | ---: | ---: |
| Total revenue | 16.41246 | 15.011923 |
| GAAP diluted EPS | 0.01 | -0.21 |

Calculator-checked total-revenue growth (native dollar inputs): (16,412,460 - 15,011,923) / 15,011,923 * 100 = 9.329498%.

Sources (selected fact accessions; prior records may differ from the comparative filing):
- P1: 10-K 0001493152-26-044483, 2025-07-01 to 2026-06-30, USD
- P2: 10-K 0001493152-25-015950, 2024-07-01 to 2025-06-30, USD
- P3: 10-K 0001493152-26-044483, 2025-07-01 to 2026-06-30, USD/shares
- P4: 10-K 0001493152-25-015950, 2024-07-01 to 2025-06-30, USD/shares
- P5: 10-K 0001493152-26-044483, balance at 2026-06-30, USD
- P6: 10-K 0001493152-25-015950, balance at 2025-06-30, USD
- S1: P1/P2, Revenues
- S2: P1/P2, OperatingIncomeLoss
- S3: P1/P2, NetIncomeLoss
- S4: P3/P4, EarningsPerShareDiluted
- S5: P5/P6, StockholdersEquity
- S6: P5/P6, LongTermDebtNoncurrent
- S7: P5/P6, LongTermDebtAndCapitalLeaseObligationsCurrent
- S8: P1/P2, NetCashProvidedByUsedInOperatingActivities
- S9: P1/P2, PaymentsToAcquirePropertyPlantAndEquipment
- S10: 8_K_Exhibit_99_1_0001493152-26-051655_ex99-1.htm.txt, filing 0001493152-26-051655: lines 300-302 give the three-month periods; lines 313-315 state Total net revenues, $16,412,460 / $15,011,923. The source uses dollar-sign cells with no in-millions scaling header.
- S11: 8_K_Exhibit_99_1_0001493152-26-051655_ex99-1.htm.txt, filing 0001493152-26-051655: lines 367 and 371-373 identify net income (loss) per common share, Diluted, $0.01 / $(0.21). These are GAAP diluted figures; basic EPS and adjusted EBITDA are not substitutes.
- Claim 1: S1
- Claim 2: S1
- Claim 3: S2, S1
- Claim 4: S3
- Claim 5: S4
- Claim 6: S3, S5
- Claim 7: S6, S7, S5
- Claim 8: S8, S9
- Claim 9: S10
- Claim 10: S10
- Claim 11: S11
<!-- core-financials:end -->

**Annual source rows and measurement reconciliation.** Annual comparisons are for the years ended June 30, 2026 and June 30, 2025; balances are at those dates. Source tables contain native dollars; report monetary amounts are divided by 1,000,000 where labeled millions. EPS is not scaled. The selected prior fact accession remains preserved in P2/P4/P6 above; K also presents the comparative period.

| Retained source key / claim | Exact rows in K | What the saved filing supports |
| --- | --- | --- |
| S1; claims 1 and 2; denominator in claim 3 | 7957-7968 and 7991-8016; comparative 8202-8225 | Pre-elimination segment totals 78.145875m / 73.088687m; intersegment eliminations 3.774495m / 7.000458m; consolidated totals 74.371380m / 66.088229m. |
| S2; operating-income part of claim 3 | Periods 5336-5344; income 5384-5387 | Operating income 6.946665m / 3.501718m. The retained explicit margin row is present; the model's missing-row warning was not a reason to invent a new margin. Its denominator basis still needs the qualification above. |
| S3; claim 4 and numerator in claim 6 | 5426-5429 | Net income attributable to NETSOL 2.950353m / 2.923233m, distinct from consolidated net income before non-controlling interests at 5418-5425. |
| S4; claim 5 | 5430-5439 | GAAP diluted EPS 0.25 / 0.25, from the Diluted row at 5437-5439; basic EPS and diluted share counts are not substitutes. |
| S5; claim 6 and denominator in claim 7 | Dates 5192-5200; NETSOL equity 5315-5318 | Parent-attributable equity 41.593925m / 37.833765m. Total equity including non-controlling interests is a different row, 5323-5326. |
| S6/S7; numerator in claim 7 | 5259-5262; Note 13 dates/columns 7214-7226 and components 7272-7289 | Current loans/finance leases 8.187170m; noncurrent loans before the subsidiary-finance-lease row 0.208107m. See the lease-coverage qualification below. |
| S8/S9; claim 8 | Periods 5748-5757; CFO 5804-5807; PPE purchases 5810-5813 | CFO 13.884176m / 0.447267m and PPE cash outflows 2.007114m / 1.382770m. Course-defined FCF subtracts the positive PPE outflow magnitude from CFO. |
| S10/S11; claims 9-11 | E 300-302, 313-315, 367 and 371-373 | Comparable three-month revenue and GAAP diluted EPS, including the prior loss per share. Audit status is not stated in this saved table. |

**Consolidated basis, separately disclosed.** K's statement at 5336-5361 gives consolidated net revenues of 74.371380m / 66.088229m. Note 17 reconciles the retained segment figures: `78.145875 - 3.774495 = 74.371380` and `73.088687 - 7.000458 = 66.088229` (USD millions; K 7991-8011 and 8202-8220). On this consolidated basis, the sales change is `(74.371380 - 66.088229) / 66.088229 * 100 = 12.533474%`, and the operating-income percentage is `6.946665 / 74.371380 * 100 = 9.340508%`. These are source-review reconciliations, not silent replacements in the preserved prior core register. The cached revenue selection and associated core labels require a source-aware correction/reverification before they can be presented as consolidated measures.

**Debt coverage.** The retained numerator is `0.208107 + 8.187170 = 8.395277` million. Note 13 separately identifies noncurrent subsidiary finance leases of 0.004875m and totals including those leases of 8.400152m (current 8.187170m plus noncurrent 0.212982m; K 7278-7289). The retained metric therefore includes current finance leases but excludes that noncurrent finance-lease amount. It is not a uniform all-loans-and-finance-leases measure. No operating-lease amounts have been silently included. This definition limitation remains disclosed; it is not marked passed by the local arithmetic match.

**FCF scope.** The course figure 11.877062m is CFO less PPE purchases, not cash remaining after every investment. K 5822-5825 separately reports a 2.686392m intangible-asset outflow, and Note 11 at 7157-7174 identifies capitalized internal-use software. That separate software spending is not deducted in the preserved course formula. K 3173-3180 attributes much of the annual CFO improvement to working-capital movements and advance collections. Annual FCF does not establish future liquidity or quarterly cash generation.

**Insight:** Annual operating cash generation needs to be read with billing timing and separate software investment, rather than treated as a guaranteed recurring cushion. [K 3173-3180, 5804-5825, 7157-7174.]

## Market Positioning and Growth Outlook

The release describes software and services for OEMs, dealerships, and financial institutions. It reports subscription/support revenue of $9.5 million versus $9.0 million, a 6.1% increase, and total quarterly revenue of $16.4 million versus $15.0 million in its rounded narrative. The precise comparable amounts and calculated growth remain in the core table above. These are the three months ended September 30, 2026 / 2025, not calendar Q1. [E 11-13, 35-43, 300-315.]

Quarterly gross margin was reported as 50.5% versus 39.4%. The release attributes improvement to revenue mix and approximately $1.0 million of capitalized software development costs versus none in the prior-year quarter. This is management's reported explanation; it does not establish that the annual margin had the same drivers or that the change will persist. [E 44-56.]

A quantitative competitive ranking, market-share comparison, and independently supported future growth rate remain **Missing** from this report. Qualitative release language does not establish competitive dominance. No new numerical forecast is introduced.

## Valuation Insights

**Share price: Missing from the filing-only evidence adopted in this final copy. P/E: Missing; no market-price multiple is asserted.** The prior unsupported price and P/E statements, the comparison of a multiple with ROE, and the valuation arguments depending on them have been removed. The older saved LSEG record is not substituted for filing evidence in this review, as requested.

A fair-value range, DCF assumptions, required return, price target, and prospective upside/downside remain **Missing**. Historical revenue, income, equity, debt, and the explicitly defined FCF calculation are available above, with their source qualifications; they do not by themselves establish an attractive entry price.

**Insight:** A completed arithmetic check is not a valuation method. The segment/consolidated revenue distinction and debt-coverage limit must be resolved before these retained ratios support a price-relative conclusion. [K 7991-8011, 8202-8220, 7278-7289; calculation scope disclosed above.]

## Future Developments and Strategic Recommendations

The proposed repurchase belongs to the Pakistan-listed, majority-owned **NETSOL Technologies Limited**, not a demonstrated repurchase of the U.S. parent's shares. Its board recommended up to 4,000,000 of the subsidiary's shares, approximately 4.45% of issued capital, funded from distributable profits, subject to shareholder approval on December 3, 2026. The release assigns no financial benefit at this stage. A parent EPS benefit is not assumed. [E 90-94.]

NETSOL Technologies Europe Limited began evaluating alternatives for Virtual Lease Services, including a potential sale or wind-down. No plan was approved or agreement executed. The release says a completed transaction may produce a disposal loss and exit costs that could not be estimated; this copy removes the unsupported gain possibility and does not claim a completed divestiture. [E 95-100.]

The release reports quarterly operating cash use of approximately $5.6 million versus $5.3 million provided in the prior-year quarter. Management describes delivery against advance billings as a main driver. This is kept distinct from the annual positive CFO and course-defined FCF figures. A supported cash-flow forecast, incremental return on planned spending, and guaranteed future profitability remain **Missing**. [E 78-84, 122-127; K 3173-3180.]

## Investment Recommendation

**Prior recorded view: Hold.** This is the prior Investment Advisor's research judgment, retained for record continuity, not a filing fact or a newly issued recommendation. Its market-price-based rationale has been removed. This final copy establishes no fair value or price-relative forward view, and it is not represented as a before-reaction prediction.

**Insight:** The quarter shows improved reported revenue and profitability, but the supplied evidence does not turn that observation into a supported expected stock return. The missing valuation inputs and identified definition limits remain open; no scored live-view success is claimed. [E 35-67; limitations above.]

**Disposition of the prior six Purdue gaps.**

| Prior gap | Final-copy treatment |
| --- | --- |
| 1. Separate operating-margin claim | Explicit calculation already retained; exact operating-income and revenue rows added. Source review qualifies its pre-elimination denominator. No absent figure invented. |
| 2. Share-price source | Statement and dependent rationale removed. Filing-only market price remains Missing. |
| 3. P/E source | Statement and dependent rationale removed. No replacement multiple asserted. |
| 4. Annual income/EPS/revenue row location | Exact rows supplied above. Income/EPS match; Note 17 explains the revenue basis difference. Cached consolidated labeling and affected ratio validation remain unresolved. |
| 5. Debt/equity/average-equity row location | Exact balance-sheet and Note 13 rows supplied. Parent-equity basis is explicit; mixed finance-lease coverage in the retained debt ratio remains qualified. |
| 6. CFO/capex definition row location | Exact cash-flow and software-note rows supplied. Course PPE-only FCF is retained; separate software investment is disclosed, with no broader cash-availability claim. |

The old blanket repair notices claiming that quarterly rows and all source citations were absent are superseded by the exact source references in this final copy. No blanket all-issues pass is asserted. Genuine remaining limits are: corrected consolidated-versus-segment core mapping/source-aware verification; a uniform debt-coverage definition; filing-only price/valuation inputs; forecasts, competitive comparisons, and a before-reaction view/reaction record. The earnings table's audit status is not stated. Annual columns are not supplied by the short quarterly release; the annual figures come from K.

**Validation limit.** The local Verifier compares the preserved register with cached facts and printed arithmetic. Its marks do not independently validate those facts' consolidation scope, reconcile finance-lease definitions, verify every narrative sentence, or supply missing market data. Purdue's completed review applies only to the prior revision, not to this final copy.

AI assistance: saved-source comparison and editorial revision; no analyst rerun or new model review. No human or partner verification is claimed.

screens, not recommendations.
