# LMT and NOC XBRL Evidence

This file presents the saved SEC company-facts records for total revenue and operating income. No human marks, partner marks, or error counts are assigned.

## LMT — Lockheed Martin Corporation

SEC data source: https://data.sec.gov/api/xbrl/companyfacts/CIK0000936468.json

Saved statement source: `readings/LOCKHEED MARTIN CORP_20261029_230917/10_K_0001628280-26-004195.txt`, lines 853-870.

### Revenue

- Tag: `Revenues`
- Label: `Revenues`
- Unit: `USD`
- Description: `Amount of revenue recognized from goods sold, services rendered, insurance premiums, or other activities that constitute an earning process. Includes, but is not limited to, investment and interest income before deduction of interest expense when recognized as a component of revenue, and sales and trading gain (loss).`

| Fiscal period | Start | End | Value | Form | Accession |
|---|---|---|---:|---|---|
| FY2025 | 2025-01-01 | 2025-12-31 | 75048000000 | 10-K | 0001628280-26-004195 |
| FY2024 | 2024-01-01 | 2024-12-31 | 71043000000 | 10-K | 0000936468-25-000009 |

### Operating income

- Tag: `OperatingIncomeLoss`
- Label: `Operating Income (Loss)`
- Unit: `USD`
- Description: `The net result for the period of deducting operating expenses from operating revenues.`

| Fiscal period | Start | End | Value | Form | Accession |
|---|---|---|---:|---|---|
| FY2025 | 2025-01-01 | 2025-12-31 | 7731000000 | 10-K | 0001628280-26-004195 |
| FY2024 | 2024-01-01 | 2024-12-31 | 7013000000 | 10-K | 0000936468-25-000009 |

Statement comparison: the saved LMT statement reports `Total sales 75,048 71,043 67,571` at line 861 and `Operating profit 7,731 7,013 8,507` at line 870, with `(in millions, except per share data)` at line 855. The XBRL values match the checked statement values after conversion from dollars to millions.

## NOC — Northrop Grumman Corporation

SEC data source: https://data.sec.gov/api/xbrl/companyfacts/CIK0001133421.json

Saved statement source: `readings/NORTHROP GRUMMAN CORP _DE__20261029_230920/10_K_0001133421-26-000003.txt`, lines 1076-1090.

### Revenue

- Tag: `Revenues`
- Label: `Revenues`
- Unit: `USD`
- Description: `Amount of revenue recognized from goods sold, services rendered, insurance premiums, or other activities that constitute an earning process. Includes, but is not limited to, investment and interest income before deduction of interest expense when recognized as a component of revenue, and sales and trading gain (loss).`

| Fiscal period | Start | End | Value | Form | Accession |
|---|---|---|---:|---|---|
| FY2025 | 2025-01-01 | 2025-12-31 | 41954000000 | 10-K | 0001133421-26-000003 |
| FY2024 | 2024-01-01 | 2024-12-31 | 41033000000 | 10-K | 0001133421-25-000006 |

### Operating income

- Tag: `OperatingIncomeLoss`
- Label: `Operating Income (Loss)`
- Unit: `USD`
- Description: `The net result for the period of deducting operating expenses from operating revenues.`

| Fiscal period | Start | End | Value | Form | Accession |
|---|---|---|---:|---|---|
| FY2025 | 2025-01-01 | 2025-12-31 | 4511000000 | 10-K | 0001133421-26-000003 |
| FY2024 | 2024-01-01 | 2024-12-31 | 4370000000 | 10-K | 0001133421-25-000006 |

Statement comparison: the saved NOC statement reports `Total sales 41,954 41,033 39,290` at line 1082 and `Operating income 4,511 4,370 2,537` at line 1090, with `$ in millions, except per share amounts` at line 1078. The XBRL values match the checked statement values after conversion from dollars to millions.

NOC limitation: the statement also reports a $231 million gain on sale of business at lines 1088-1090. The operating-income XBRL value remains the reported GAAP operating income. This evidence does not create an adjusted operating-income measure.
