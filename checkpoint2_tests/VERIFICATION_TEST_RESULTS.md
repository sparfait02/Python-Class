# FIN 67110 Checkpoint 2 verifier tests

Date: November 4, 2026

Verifier command used for both tests:

```powershell
.\.venv\Scripts\python.exe equity_research.py --verify-only PATH
```

## Seeded EPS test

Folder: `checkpoint2_tests/costco_seeded_eps/`

The copied report changes FY2026 annual diluted EPS from `$20.76` to `$21.76`,
including the seeded quoted source line. The copied `facts.json`, 10-K, 10-Q,
8-K, and Exhibit 99.1 were not changed.

Result: `Correct=10; Wrong=1; Unsupported=0; Errors=1`.

Core Claim 5 was marked Wrong. The verifier cited the copied 10-K text at line
639: `Diluted$20.76 $18.21 $16.56`.

Saved marks: `checkpoint2_tests/costco_seeded_eps/verification_marks.json`

Saved output: `checkpoint2_tests/costco_seeded_eps/verification_output.txt`

Saved verified report: `checkpoint2_tests/costco_seeded_eps/verified_report.md`

## Clean-report test

Folder: `checkpoint2_tests/costco_clean/`

Result: `Correct=11; Wrong=0; Unsupported=0; Errors=0`.

Saved marks: `checkpoint2_tests/costco_clean/verification_marks.json`

Saved output: `checkpoint2_tests/costco_clean/verification_output.txt`

Saved verified report: `checkpoint2_tests/costco_clean/verified_report.md`

## Seeded annual revenue-growth test

Folder: `checkpoint2_tests/costco_seeded_revenue_growth/`

The copied report adds a sentence claiming annual revenue growth of 14.143695%
from the quoted FY2026 and FY2025 total revenues. The underlying filing and
facts remain unchanged.

Result: `Correct=11; Wrong=1; Unsupported=0; Errors=1`.

The added annual revenue-growth claim was marked Wrong. The verifier cited the
10-K total-revenue line at line 626: `Total revenue303,154 275,235 254,453`.

Saved marks: `checkpoint2_tests/costco_seeded_revenue_growth/verification_marks.json`

Saved output: `checkpoint2_tests/costco_seeded_revenue_growth/verification_output.txt`

Saved verified report: `checkpoint2_tests/costco_seeded_revenue_growth/verified_report.md`

## Offline graph test

Test script: `checkpoint2_tests/test_agent_graph_offline.py`

Saved output: `checkpoint2_tests/graph_offline_test_output.txt`

The fixed LangGraph trace was Step 1 through Step 7, Research Analyst,
Financial Analyst, Investment Advisor, Strategy Manager review, one Research
Analyst repair, Strategy Manager compile, and Verifier. The Verifier was the
final node. Attempts were Research Analyst 2, Financial Analyst 1, Investment
Advisor 1, and Strategy Manager 2. The test also confirmed the Verifier packet
contained only the compiled report, saved filings, and saved facts.

## Evidence integrity

SHA-256 comparisons confirmed that `facts.json`, the 10-K text, and Exhibit
99.1 text in both test folders match the latest saved Costco run. The seeded
change is limited to the copied report.

Model-based checking is untested. These tests used deterministic local checks
only and made no API calls. No human or partner sign-off was recorded.
