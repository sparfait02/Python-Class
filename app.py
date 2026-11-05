"""Streamlit UI for the fixed Lab 04/05 agent team."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import streamlit as st

from ui_support import PERSONA_SECTIONS, build_team_command, run_folder_from_output, ui_status


st.set_page_config(page_title="FIN 67110 Agent Team", layout="wide")
st.title("FIN 67110 Agent Team")
st.caption("The full run uses Steps 1–7, the four roles, and the mandatory Verifier.")
with st.expander("Analyst persona files"):
    st.write("Write persona text in these files. The six required parts are:")
    st.code("\n".join(f"{index}. {section}" for index, section in enumerate(PERSONA_SECTIONS, 1)))
    for role in ("research_analyst", "financial_analyst", "investment_advisor"):
        st.write(f"`personas/{role}.md`")

ticker = st.text_input("Ticker", value="")
peer_text = st.text_input("Peers (comma-separated, optional)", value="")
price = st.number_input("Regular-session close (optional)", min_value=0.0, value=0.0, step=0.01)
run_clicked = st.button("Run agent team", type="primary")

if run_clicked:
    if not ticker.strip():
        st.error("Enter a ticker.")
        st.stop()
    peers = [item.strip().upper() for item in peer_text.split(",") if item.strip()]
    supplied_price = price if price > 0 else None
    command = build_team_command(sys.executable, ticker.strip().upper(), peers, supplied_price)
    st.code(" ".join(command), language="powershell")
    log = st.empty()
    lines: list[str] = []
    try:
        process = subprocess.Popen(
            command,
            cwd=Path(__file__).parent,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            env=os.environ.copy(),
        )
        assert process.stdout is not None
        for line in process.stdout:
            lines.append(line.rstrip())
            log.code("\n".join(lines[-80:]), language="text")
        return_code = process.wait()
    except OSError as error:
        return_code = 1
        lines.append(f"UI process error: {type(error).__name__}")
    output = "\n".join(lines)
    folder = run_folder_from_output(output)
    if return_code != 0:
        st.error(ui_status(return_code))
        st.warning("The provider run failed. Offline stub evidence is not a live report.")
    elif folder is None:
        st.error("The run ended without a saved facts folder. No verified report is presented.")
    else:
        st.success(ui_status(return_code))
        st.write(f"Run folder: `{folder}`")
        for name in ("desk_report.md", "verified_report.md", "verification_marks.json"):
            path = folder / name
            if path.exists():
                st.subheader(name)
                st.code(path.read_text(encoding="utf-8"), language="markdown" if name.endswith(".md") else "json")
            else:
                st.info(f"Not saved: {name}")
