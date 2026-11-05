"""Offline UI test. It does not start the provider or run SEC requests."""

from pathlib import Path
import sys

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from equity_research import role_instruction  # noqa: E402
from ui_support import PERSONA_SECTIONS, build_team_command, run_folder_from_output, ui_status  # noqa: E402


def main() -> None:
    app = AppTest.from_file(str(ROOT / "app.py")).run(timeout=10)
    assert app.button[0].label == "Run agent team"
    assert list(PERSONA_SECTIONS) == [
        "Identity", "How it reads a company", "What it is given",
        "Criteria it scores", "What would change its view", "Output",
    ]
    for role in ("Research Analyst", "Financial Analyst", "Investment Advisor"):
        assert "PERSONA (student-authored file; use it when present)" in role_instruction(role)
    command = build_team_command("python.exe", "TEST", ["AAA", "BBB"], 12.34)
    assert command[-1] == "--desk"
    assert "--price" in command
    stub_output = "Node: Step 1\nNode: Verifier\nSaved facts: readings\\offline_stub"
    assert run_folder_from_output(stub_output) == Path("readings/offline_stub")
    assert ui_status(0, offline_stub=True) == "OFFLINE STUB: completed"
    assert "no verified report" in ui_status(1, offline_stub=True)
    print("UI offline stub test passed; no provider call; no live report presented.")


if __name__ == "__main__":
    main()
