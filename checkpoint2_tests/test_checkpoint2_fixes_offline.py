"""Targeted Checkpoint 2 checks; all model calls are stubs."""

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import equity_research as er
import test_agent_graph_offline as graph_test


class CheckpointFixesTest(unittest.TestCase):
    def test_role_files_and_personas_preserved(self):
        for role, filename in er.ROLE_FILES.items():
            instructions = er.role_instruction(role)
            original = (ROOT / "roles" / filename).read_text(encoding="utf-8")
            if role in er.PERSONA_FILES:
                persona = (ROOT / "personas" / er.PERSONA_FILES[role]).read_text(encoding="utf-8").strip()
                self.assertTrue(instructions.startswith(original))
                self.assertIn(persona, instructions)
            else:
                self.assertEqual(instructions, original)

    def test_graph_node_evidence_and_redaction(self):
        with tempfile.TemporaryDirectory() as folder:
            graph_test.RUN_FOLDER = Path(folder)
            graph_test.repair_sent = False
            graph_test.calls.clear()
            (Path(folder) / "facts.json").write_text('{"api_key": "fixture-key"}', encoding="utf-8")
            output = io.StringIO()
            original = graph_test.stub_role_call
            def stub(role, packet):
                self.assertIn("Node: " + role, output.getvalue())
                result = original(role, packet)
                result["api_key"] = "fixture-key"
                return result
            with patch.object(graph_test, "stub_role_call", stub), contextlib.redirect_stdout(output):
                graph_test.main()
            nodes = sorted((Path(folder) / "node_evidence").glob("*/*"))
            self.assertEqual(len(nodes), 14)
            for node in nodes:
                for filename in ("input.json", "output.json"):
                    text = (node / filename).read_text(encoding="utf-8")
                    self.assertIn("OFFLINE STUB", text)
                    self.assertNotIn("fixture-key", text)
                    json.loads(text)
            role_inputs = list((Path(folder) / "node_evidence").glob("*/*/role_input.json"))
            self.assertEqual(len(role_inputs), 7)
            for path in role_inputs:
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(set(data["packet"]), {"task", "context", "expected_output"})
                if data["role"] == "Verifier":
                    self.assertEqual(set(data["packet"]["context"]), {"compiled_report", "saved_filings", "saved_facts"})
            self.assertIn("OFFLINE STUB", (Path(folder) / "desk_report.md").read_text(encoding="utf-8"))

    def test_failed_node_is_logged_before_call(self):
        with tempfile.TemporaryDirectory() as folder:
            output = io.StringIO()
            def fail(role, packet):
                self.assertIn("Node: Research Analyst", output.getvalue())
                raise ValueError("token=private-fixture")
            graph = er.build_agent_graph(fail, offline_stub=True)
            with contextlib.redirect_stdout(output), self.assertRaises(ValueError):
                graph.invoke({"run_folder": folder, "role_packets": {"Research Analyst": {}},
                              "role_outputs": {}, "attempts": {}})
            path = next((Path(folder) / "node_evidence").glob("*/08_Research Analyst/output.json"))
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["status"], "failed")
            self.assertNotIn("private-fixture", data["error"])

    def test_environment_fields_and_long_source(self):
        source = "source line\n" * 1000
        with patch.dict(os.environ, {"TEST_SECRET": "credential-fixture"}):
            result = er.safe_node_evidence({".env": "never-save-fixture", "environment": {"x": "never-save-fixture"},
                                           "file_record": {"file": "private/.env", "lines": "never-save-fixture"},
                                           "source": source, "message": "credential-fixture"})
        text = json.dumps(result)
        self.assertNotIn("never-save-fixture", text)
        self.assertNotIn("credential-fixture", text)
        self.assertEqual(result["source"], source)

    def test_model_marks_stay_under_filings(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "facts.json").write_text("{}", encoding="utf-8")
            def stub(role, packet):
                if role == "Strategy Manager" and "Compile" in packet["task"]:
                    return {"report_markdown": "\n".join("# " + part for part in er.REPORT_PARTS)}
                if role == "Strategy Manager":
                    return {"repair_packets": []}
                return {"checks": [], "gaps": []}
            def local(folder):
                report = (root / "desk_report.md").read_text(encoding="utf-8")
                (root / "verified_report.md").write_text(er.place_verification_marks(report, [], []), encoding="utf-8")
                return "offline verifier stub"
            with contextlib.redirect_stdout(io.StringIO()):
                er.build_agent_graph(stub, local_verifier=local, offline_stub=True).invoke({
                    "run_folder": folder, "accession_line": "offline fixture", "role_outputs": {}, "attempts": {},
                    "role_packets": {role: {} for role in ("Research Analyst", "Financial Analyst")},
                })
            report = (root / "verified_report.md").read_text(encoding="utf-8")
            self.assertEqual(report.count("## Verification marks"), 1)
            self.assertEqual(report.count("### Model-based period and definition checks"), 1)
            self.assertLess(report.index("Model-based period"), report.index("<!-- verification-marks:end -->"))
            self.assertLess(report.index("<!-- verification-marks:end -->"), report.index("# Overview"))
            self.assertIn("OFFLINE STUB", report)

    def test_marks_placement_replacement_and_content(self):
        original = "Filings read: fixture\nRun time: fixture\n\n# Overview\nKeep this paragraph.\n"
        checks = [{"claim": "5", "status": "Wrong", "source_line": 639}]
        legacy = original + "\n## Verification marks\n\n- old marks\n"
        first = er.place_verification_marks(legacy, checks, ["Corrected EPS."])
        second = er.place_verification_marks(first, checks, ["Corrected EPS."])
        self.assertEqual(first, second)
        self.assertEqual(first.splitlines()[0], original.splitlines()[0])
        self.assertEqual(first.splitlines()[1], "<!-- verification-marks:start -->")
        self.assertEqual(first.count("## Verification marks"), 1)
        self.assertIn("Run time: fixture\n\n# Overview\nKeep this paragraph.", first)

    def test_minimal_seeded_package_reproduces(self):
        source = ROOT / "checkpoint2_tests" / "costco_seeded_eps"
        names = ["COST_FALLBACK_REPORT.md", "facts.json", "10_K_0000909832-26-000093.txt",
                 "8_K_Exhibit_99_1_0000909832-26-000084_costex9918-k92426.htm.txt"]
        before = {name: hashlib.sha256((source / name).read_bytes()).hexdigest() for name in names}
        with tempfile.TemporaryDirectory() as folder:
            for name in names:
                shutil.copyfile(source / name, Path(folder) / name)
            with contextlib.redirect_stdout(io.StringIO()):
                er.verify_saved_run(folder)
            marks = json.loads((Path(folder) / "verification_marks.json").read_text(encoding="utf-8"))
            self.assertEqual(marks["summary"], {"correct": 10, "wrong": 1, "unsupported": 0, "errors": 1})
            report = (Path(folder) / "verified_report.md").read_text(encoding="utf-8")
            body = report.split("<!-- verification-marks:end -->", 1)[1]
            self.assertNotIn("21.76", body)
            self.assertIn("20.76", body)
            self.assertIn("corrected 21.76 to 20.76", report)
            self.assertEqual(report.count("## Verification marks"), 1)
            self.assertEqual(report.splitlines()[1], "<!-- verification-marks:start -->")
        self.assertEqual(before, {name: hashlib.sha256((source / name).read_bytes()).hexdigest() for name in names})


if __name__ == "__main__":
    unittest.main()
