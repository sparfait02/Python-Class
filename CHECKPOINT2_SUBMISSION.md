# Checkpoint 2 submission evidence

Review date: November 5, 2026. Individual submission: Samuel Parfait.
Repository commit permalink and Brightspace upload: pending; this file does not establish submission.

The [Checkpoint 2 checkout](https://cinderzhang.github.io/FIN67110-Fall2026/week-03/lab-05-make-the-team-yours.html) calls for the agent team and seeded-error verifier marks. Successful lab runs and partner checks remain separate demonstrations. The [schedule](https://cinderzhang.github.io/FIN67110-Fall2026/schedule.html) sets the Session 5 deadline at November 5, 2026, 11:59 p.m. Eastern.

| Requirement or demonstration | Evidence | Status |
| --- | --- | --- |
| Fixed graph with mandatory Verifier | [Graph implementation](equity_research.py), [offline graph test](checkpoint2_tests/test_agent_graph_offline.py) | Passed offline; no successful live graph established |
| Seeded EPS error, wrong source quote, and correction from real source | [Incorrect input](checkpoint2_tests/costco_seeded_eps/COST_FALLBACK_REPORT.md), [marks](checkpoint2_tests/costco_seeded_eps/verification_marks.json), [corrected report](checkpoint2_tests/costco_seeded_eps/verified_report.md) | Passed deterministic offline check: 10 Correct, 1 Wrong, 0 Unsupported, 1 Error |
| Invented growth and clean report checks | [Saved earlier results](checkpoint2_tests/VERIFICATION_TEST_RESULTS.md) | Previously passed offline; not rerun during this fix |
| Three analyst personas delivered to matching roles; Manager/Verifier retain role instructions | [Personas](personas/), [provider-boundary tests](checkpoint2_tests/test_provider_errors_offline.py), [fix tests](checkpoint2_tests/test_checkpoint2_fixes_offline.py) | Passed offline; persona wording preserved |
| Node-start logging and saved executed-node inputs/outputs | `node_evidence/<session>/<sequence>_<node>/` under each run; [fix tests](checkpoint2_tests/test_checkpoint2_fixes_offline.py) | Passed offline, including failed-node evidence and credential redaction |
| Marks directly below the original filings line, without duplicate sections | [Corrected seeded report](checkpoint2_tests/costco_seeded_eps/verified_report.md), [fix tests](checkpoint2_tests/test_checkpoint2_fixes_offline.py) | Passed offline; model-mark placement tested with a stub only |
| Streamlit browser launch | [Recorded browser confirmation](checkpoint2_tests/costco_live_failure_summary_20261105.md) | User reported successful launch; not evidence of a verified report through UI |
| Full live provider-backed run and mandatory live Verifier | [Live-failure summary](checkpoint2_tests/costco_live_failure_summary_20261105.md) | Unsuccessful: Research Analyst HTTP 503 UNAVAILABLE; no analyst completed and Verifier was not reached |
| Ryan checks seeded-EPS marks against the 10-K | No completed Checkpoint 2 partner-check record | Pending; earlier RTX checks are separate |
| Partner-pick UI report and two hand-checked claims | No successful Lab 05 verified run or corresponding partner marks | Not demonstrated |

## Reproduce the seeded-EPS check without network access

From the repository root after installing `requirements.txt` in your Python environment:

```powershell
.\.venv\Scripts\python.exe -X utf8 equity_research.py --verify-only checkpoint2_tests/costco_seeded_eps
```

Expected: Core Claim 5 Wrong, observed 21.76 versus expected 20.76, citing 10-K line 639. Summary: Correct=10; Wrong=1; Unsupported=0; Errors=1. These statuses describe the original incorrect input; the corrected report retains that audit trail.

The smallest demonstrated data package for the existing verifier has seven files in `checkpoint2_tests/costco_seeded_eps/`:

1. `COST_FALLBACK_REPORT.md` — original incorrect input, unchanged.
2. `facts.json` — saved XBRL evidence, unchanged.
3. `10_K_0000909832-26-000093.txt` — original saved 10-K, including EPS source line 639, unchanged.
4. `8_K_Exhibit_99_1_0000909832-26-000084_costex9918-k92426.htm.txt` — original release required for the verifier's quarterly checks, unchanged.
5. `verification_marks.json` — deterministic marks.
6. `verification_output.txt` — deterministic execution results.
7. `verified_report.md` — corrected report with marks below the first line.

Only the first four files are required inputs; the last three are reproducible outputs. A temporary-directory test verified these four inputs are sufficient. The full 10-K and release preserve original source line numbering. No 10-Q, base 8-K, Step 6 transcript, live log, or model key is needed. This is the smallest demonstrated file set for the current verifier, not a claim that the source files contain no unused text. The repository code and dependencies are also required.

## Limits and remaining work

- [Current offline results](checkpoint2_tests/CHECKPOINT2_OFFLINE_RESULTS.md) distinguish stub checks from deterministic checks on saved real evidence.
- Node evidence saves the graph state plus each executed role's actual instruction/JSON request and returned result. Failed nodes save a sanitized failure. Steps 1-7 are existing graph markers after data preparation; these changes do not relocate the upstream SEC operations into those nodes.
- Stub graph tests use temporary folders and explicitly label generated artifacts OFFLINE STUB. Their artifacts are removed after the tests; their results are recorded, not represented as live reports.
- No new model-based period/definition check or live report was produced. The latest preserved live log is `checkpoint2_tests/costco_live_execution_20261105_083540_127635.txt`; it is not needed in the minimal tracked evidence package.
- Historical practice price: USD 992.13, October 27, 2026, not a current market price.
- Persona wording remains the student's existing text, including the RTX example. Company-neutral wording remains for the student to review; no authorship or human audit is invented here.
- The generic verifier's broader handling of arbitrary report layouts, unsupported claims, and all sourced numbers remains outside what these saved seeded tests prove.
- Ryan's pending Checkpoint 2 check, successful verified live demonstrations, publication of the submission commit, and Brightspace submission remain outstanding.

This is a learning exercise, not financial advice.
AI assistance: ChatGPT and Codex assisted implementation, testing, and this evidence index. Automated checks do not establish human or partner source verification; human judgments remain with the student.
Any remaining errors are my own.
