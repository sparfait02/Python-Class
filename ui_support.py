"""Small, testable helpers for the Lab 05 UI."""

from __future__ import annotations

import re
from pathlib import Path

PERSONA_SECTIONS = (
    "Identity",
    "How it reads a company",
    "What it is given",
    "Criteria it scores",
    "What would change its view",
    "Output",
)


def build_team_command(python_executable: str, ticker: str, peers: list[str], price: float | None) -> list[str]:
    command = [python_executable, "-u", "equity_research.py", ticker, "--peers", *peers]
    if price is not None:
        command.extend(["--price", str(price)])
    command.append("--desk")
    return command


def run_folder_from_output(output: str) -> Path | None:
    match = re.search(r"Saved facts: (.+)", output)
    return Path(match.group(1).strip()) if match else None


def ui_status(return_code: int, offline_stub: bool = False) -> str:
    label = "OFFLINE STUB" if offline_stub else "LIVE PROVIDER"
    return f"{label}: completed" if return_code == 0 else f"{label}: failed; no verified report is presented"
