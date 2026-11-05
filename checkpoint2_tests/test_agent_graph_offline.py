"""Offline Lab 04 graph test. It makes no provider or SEC calls."""

from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from equity_research import REPORT_PARTS, build_agent_graph, role_packet


RUN_FOLDER = Path(__file__).resolve().parent / "costco_graph_offline"
calls: list[tuple[str, dict]] = []
repair_sent = False


def stub_role_call(role: str, packet: dict) -> dict:
    global repair_sent
    assert set(packet) == {"task", "context", "expected_output"}, (role, packet.keys())
    calls.append((role, packet))
    if role == "Research Analyst":
        return {"business_model": "stub", "evidence": [], "gaps": []}
    if role == "Financial Analyst":
        return {"statement_analysis": "stub", "quarter_analysis": "stub", "peer_analysis": "stub", "gaps": []}
    if role == "Investment Advisor":
        return {"recommendation": "Hold", "thesis": "stub", "deciding_number": "stub", "gaps": []}
    if role == "Strategy Manager":
        if "Compile" not in packet["task"] and not repair_sent:
            repair_sent = True
            return {"failed_parts": ["Overview"], "repair_packets": [{
                "role": "Research Analyst",
                "task": "Repair Overview once.",
                "context": {"only": "manager-supplied"},
                "expected_output": "JSON with evidence and gaps.",
            }]}
        if "Compile" not in packet["task"]:
            return {"failed_parts": [], "repair_packets": []}
        return {"report_markdown": "\n".join(f"# {part}" for part in REPORT_PARTS), "section_status": {}, "gaps": []}
    if role == "Verifier":
        assert set(packet["context"]) == {"compiled_report", "saved_filings", "saved_facts"}
        assert "investment_advisor" not in packet["context"]
        return {"checks": [], "corrections": [], "gaps": []}
    raise AssertionError(role)


def offline_verifier(path: str) -> str:
    return "offline-code-verifier"


def main() -> None:
    graph = build_agent_graph(stub_role_call, local_verifier=offline_verifier)
    result = graph.invoke({
        "run_folder": str(RUN_FOLDER),
        "accession_line": "stub filings",
        "role_packets": {
            "Research Analyst": role_packet("Research task", {"source": "manager"}, "research JSON"),
            "Financial Analyst": role_packet("Financial task", {"source": "manager"}, "financial JSON"),
        },
        "role_outputs": {},
        "attempts": {},
    })
    order = result["node_order"]
    assert order[0:10] == ["Step 1", "Step 2", "Step 3", "Step 4", "Step 5", "Step 6", "Step 7", "Research Analyst", "Financial Analyst", "Investment Advisor"]
    assert order[-2:] == ["Strategy Manager (compile)", "Verifier"], order
    assert order.index("Verifier") == len(order) - 1
    assert result["attempts"]["Research Analyst"] == 2
    assert result["attempts"]["Financial Analyst"] == 1
    assert result["attempts"]["Investment Advisor"] == 1
    assert result["attempts"]["Strategy Manager"] == 2
    assert "Verifier" in order
    print(json.dumps({"node_order": order, "attempts": result["attempts"], "mandatory_verifier": True, "packet_boundaries": True}, indent=2))


if __name__ == "__main__":
    main()
