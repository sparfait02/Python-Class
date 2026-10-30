# FIN 671 Lab 2 Human-Review Worksheet

This worksheet uses the latest Costco run:

`readings/COSTCO WHOLESALE CORP _NEW_20261029_212627`

The worksheet records run results for review. It does not state that any item was verified. Leave the `Human check` and `Partner check` cells blank until review is complete.

## Step 1 - Resolve ticker

Result to check: `COST` resolved to `COSTCO WHOLESALE CORP /NEW`; CIK `0000909832`.

Source: [SEC company tickers JSON](https://www.sec.gov/files/company_tickers.json)

Evidence instructions: Search the SEC JSON for ticker `COST`. Confirm the company name and CIK. Compare the result with the Step 1 terminal output in the run record.

| Human check | Partner check | Notes |
|---|---|---|
|  |  |  |

## Step 2 - Select filings

Result to check: The run selected the latest available filings shown below.

| Filing | Accession | Filing date / accepted time | SEC source | Human check | Partner check |
|---|---|---|---|---|---|
| 10-K | `0000909832-26-000093` | 2026-10-06 / 2026-10-06 21:13:15 | [SEC filing index](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/0000909832-26-000093-index.htm) |  |  |
| 10-Q | `0000909832-26-000051` | 2026-06-03 / 2026-06-03 16:43:00 | [SEC filing index](https://www.sec.gov/Archives/edgar/data/909832/000090983226000051/0000909832-26-000051-index.htm) |  |  |
| 8-K, Item 2.02 | `0000909832-26-000084` | 2026-09-24 / 2026-09-24 16:17:37 | [SEC filing index](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/0000909832-26-000084-index.htm) |  |  |

Evidence instructions: Open each SEC filing index. Confirm the form, accession, filing date, accepted time, and 8-K Item 2.02 selection. Do not use the saved text file as the only evidence for this step.

## Step 3 - Download and convert documents

Result to check: The latest folder contains the 10-K, 10-Q, 8-K, Exhibit 99.1, `facts.json`, and `step6_output.txt`.

| Saved evidence | Local file | Direct SEC source | Human check | Partner check |
|---|---|---|---|---|
| 10-K | `10_K_0000909832-26-000093.txt` | [10-K filing index](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/0000909832-26-000093-index.htm) |  |  |
| 10-Q | `10_Q_0000909832-26-000051.txt` | [10-Q filing index](https://www.sec.gov/Archives/edgar/data/909832/000090983226000051/0000909832-26-000051-index.htm) |  |  |
| 8-K | `8_K_0000909832-26-000084_cost-20260924.htm.txt` | [8-K primary document](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/cost-20260924.htm) |  |  |
| Exhibit 99.1 | `8_K_Exhibit_99_1_0000909832-26-000084_costex9918-k92426.htm.txt` | [Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/costex9918-k92426.htm) |  |  |
| Facts | `facts.json` | [SEC companyfacts JSON](https://data.sec.gov/api/xbrl/companyfacts/CIK0000909832.json) |  |  |
| Step 6 output | `step6_output.txt` | [Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/costex9918-k92426.htm) |  |  |

Evidence instructions: Open the local folder and confirm that the 8-K and Exhibit 99.1 are separate files. Open each direct SEC source and compare the saved text with the source document. The saved run does not include a separate conversion-quality assessment; record any issue in `Notes`.

## Step 4 - Collect financial facts

Source facts: `facts.json`, from [Costco SEC companyfacts](https://data.sec.gov/api/xbrl/companyfacts/CIK0000909832.json). The SEC companyfacts data provides the XBRL tags and periods. The saved `facts.json` does not store the source statement heading. The statement names below are the statements to locate and confirm in the 10-K.

Periods: current FY 2026 ended 2026-08-30; prior FY 2025 ended 2025-08-31. Amounts are USD unless stated otherwise.

| Fact | XBRL tag | Unit | Current | Prior | Expected source statement | Human check | Partner check |
|---|---|---:|---:|---:|---|---|---|
| Revenue | `RevenueFromContractWithCustomerExcludingAssessedTax` | USD | 303,154,000,000 | 275,235,000,000 | Consolidated Statements of Income |  |  |
| Operating income | `OperatingIncomeLoss` | USD | 11,685,000,000 | 10,383,000,000 | Consolidated Statements of Income |  |  |
| Net income | `NetIncomeLoss` | USD | 9,226,000,000 | 8,099,000,000 | Consolidated Statements of Income |  |  |
| Diluted EPS | `EarningsPerShareDiluted` | USD/shares | 20.76 | 18.21 | Consolidated Statements of Income; Net Income Per Common Share |  |  |
| Stockholders' equity | `StockholdersEquity` | USD | 35,803,000,000 | 29,164,000,000 | Consolidated Balance Sheets |  |  |
| Long-term debt | `LongTermDebtNoncurrent` | USD | 3,914,000,000 | 5,713,000,000 | Consolidated Balance Sheets |  |  |
| Current portion of debt | `LongTermDebtCurrent` | USD | 2,248,000,000 | 75,000,000 | Consolidated Balance Sheets |  |  |
| Cash from operations | `NetCashProvidedByUsedInOperatingActivities` | USD | 15,817,000,000 | 13,335,000,000 | Consolidated Statements of Cash Flows |  |  |
| Additions to property and equipment | `PaymentsToAcquirePropertyPlantAndEquipment` | USD | 6,435,000,000 | 5,498,000,000 | Consolidated Statements of Cash Flows |  |  |

Evidence instructions: In the SEC 10-K, locate each named statement and confirm the displayed units, fiscal-year columns, period-end dates, and values. Then compare those values with `facts.json`. Confirm whether the cash-flow capex value is presented as an addition or as a cash outflow before using it in the free-cash-flow formula.

## Step 5 - Calculate research metrics

Use the Step 4 Costco values above. No closing price was supplied, so P/E was not calculated.

| Metric | Formula and inputs from the run | Result to check | Human check | Partner check |
|---|---|---:|---|---|
| Revenue growth | `(303,154,000,000 - 275,235,000,000) / 275,235,000,000` | `0.1014369534` |  |  |
| Operating margin | `11,685,000,000 / 303,154,000,000` | `0.0385447660` |  |  |
| Return on average equity | `9,226,000,000 / ((35,803,000,000 + 29,164,000,000) / 2)` | `0.2840211184` |  |  |
| Debt-to-equity | `(3,914,000,000 + 2,248,000,000) / 35,803,000,000` | `0.1721084825` |  |  |
| Free cash flow | `15,817,000,000 - 6,435,000,000` | `9,382,000,000` |  |  |
| P/E | `not calculated: no closing price supplied` |  |  |  |

Evidence instructions: Recalculate each formula with the stated inputs. Confirm the sign convention for capex against the Consolidated Statements of Cash Flows. Confirm that the ratios use current-year values except where the formula explicitly uses prior-year equity.

## Step 6 - Read earnings release

Result to check: The saved output identifies the release units and labels the 16-week columns as quarterly and the 52-week columns as annual. It retains the dates and does not require a 13-week quarter.

Sources: [8-K filing index](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/0000909832-26-000084-index.htm) and [Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/909832/000090983226000084/costex9918-k92426.htm).

Evidence instructions: Open Exhibit 99.1. Locate the unaudited Consolidated Statements of Income. Confirm the units line, the four column headings, the Total revenue row, and the Diluted EPS row. Compare the source with the local `step6_output.txt` file.

Human check:  
Partner check:  

## Step 7 - Collect peer facts

Peer periods: WMT FY 2026 and FY 2025 ended 2026-01-31 and 2025-01-31; TGT FY 2025 and prior year ended 2026-01-31 and 2025-02-01; BJ FY 2025 and prior year ended 2026-01-31 and 2025-02-01. Amounts are USD unless stated otherwise. Diluted EPS is USD/shares.

Use the current and prior 10-K links below, and the [SEC companyfacts endpoint for Walmart](https://data.sec.gov/api/xbrl/companyfacts/CIK0000104169.json), [Target](https://data.sec.gov/api/xbrl/companyfacts/CIK0000027419.json), and [BJ's](https://data.sec.gov/api/xbrl/companyfacts/CIK0001531152.json).

| Peer | Current 10-K | Prior 10-K | Human check | Partner check |
|---|---|---|---|---|
| WMT | [2026 10-K](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) | [2025 10-K](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |  |  |
| TGT | [2026 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741926000016/0000027419-26-000016-index.htm) | [2025 10-K](https://www.sec.gov/Archives/edgar/data/27419/000002741925000018/0000027419-25-000018-index.htm) |  |  |
| BJ | [2026 10-K](https://www.sec.gov/Archives/edgar/data/1531152/000153115226000007/0001531152-26-000007-index.htm) | [2025 10-K](https://www.sec.gov/Archives/edgar/data/1531152/000153115225000013/0001531152-25-000013-index.htm) |  |  |

Peer facts to check:

| Peer | Fact | Unit | Current | Prior | Expected source statement | Human check | Partner check |
|---|---|---:|---:|---:|---|---|---|
| WMT | Revenue (`Revenues`) | USD | 713,163,000,000 | 680,985,000,000 | Consolidated Statements of Income |  |  |
| WMT | Operating income | USD | 29,825,000,000 | 29,348,000,000 | Consolidated Statements of Income |  |  |
| WMT | Diluted EPS | USD/shares | 2.73 | 2.41 | Consolidated Statements of Income; EPS section |  |  |
| WMT | Long-term debt | USD | 34,624,000,000 | 33,401,000,000 | Consolidated Balance Sheets |  |  |
| WMT | Current portion of debt | USD | 3,542,000,000 | 2,598,000,000 | Consolidated Balance Sheets |  |  |
| TGT | Revenue | USD | 104,780,000,000 | 106,566,000,000 | Consolidated Statements of Income |  |  |
| TGT | Operating income | USD | 5,117,000,000 | 5,566,000,000 | Consolidated Statements of Income |  |  |
| TGT | Diluted EPS | USD/shares | 8.13 | 8.86 | Consolidated Statements of Income; EPS section |  |  |
| TGT | Long-term debt | USD | 14,326,000,000 | 14,304,000,000 | Consolidated Balance Sheets |  |  |
| TGT | Current portion of debt | USD | 2,130,000,000 | 1,636,000,000 | Consolidated Balance Sheets |  |  |
| BJ | Revenue | USD | 21,457,274,000 | 20,501,804,000 | Consolidated Statements of Income |  |  |
| BJ | Operating income | USD | 816,604,000 | 772,206,000 | Consolidated Statements of Income |  |  |
| BJ | Diluted EPS | USD/shares | 4.38 | 4.00 | Consolidated Statements of Income; EPS section |  |  |
| BJ | Long-term debt | USD | 399,099,000 | 398,807,000 | Consolidated Balance Sheets |  |  |
| BJ | Current portion of debt | USD | 120,000,000 | 175,000,000 | Consolidated Balance Sheets |  |  |

Revenue-tag note: Walmart uses the SEC XBRL `Revenues` tag for consolidated total revenues. Its `RevenueFromContractWithCustomerExcludingAssessedTax` tag reports net sales of 706,413,000,000 current and 674,538,000,000 prior, so it is not used for Walmart's consolidated-revenue margin. For Costco, Target, and BJ's, the selected current-period candidate remains `RevenueFromContractWithCustomerExcludingAssessedTax` because a current-period `Revenues` fact was not available or was older.

Peer operating-margin results to recalculate:

- WMT: `29,825,000,000 / 713,163,000,000 = 0.0418207338`.
- TGT: `5,117,000,000 / 104,780,000,000 = 0.0488356557`.
- BJ: `816,604,000 / 21,457,274,000 = 0.0380572108`.

Evidence instructions: In each peer's current and prior 10-K, locate the named statements, confirm the fiscal period-end dates, and compare the values with the peer objects in `facts.json`. For BJ's, specifically compare the debt dates with the revenue dates. The saved output does not include partner confirmation or human verification.

## Missing evidence and review status

- No human right/wrong marks are present.
- No partner-check fields are completed.
- The saved run does not contain page numbers or source-statement-heading metadata for each XBRL fact.
- The saved run contains the SEC source documents and the Step 6 transcript, but it does not contain completed human or partner review notes.
