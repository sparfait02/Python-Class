"""Provider diagnostics tested with local SDK errors and a stub, never a client."""

from pathlib import Path
import json
import os
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from google.genai.errors import ServerError
from equity_research import call_gemini, gemini_error_diagnostic


class ProviderDiagnosticsTest(unittest.TestCase):
    def test_server_error_at_request_boundary(self):
        secret = "offline-test-credential"
        error = ServerError(503, {"error": {
            "status": "UNAVAILABLE", "message": f"Service busy; API_KEY={secret}",
        }})
        with patch.dict(os.environ, {"API_KEY": secret}):
            with patch.object(SimpleNamespace(), "generate_content", create=True,
                              side_effect=error) as generate:
                client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
                with self.assertRaises(ValueError) as caught:
                    call_gemini(client, "Research Analyst", "offline-model", {"task": "test"})
        message = str(caught.exception)
        for expected in ("503", "UNAVAILABLE", "Service busy", "offline-model", "Research Analyst"):
            self.assertIn(expected, message)
        self.assertNotIn(secret, message)
        self.assertTrue(caught.exception.__suppress_context__)
        generate.assert_called_once()

    def test_unconfigured_credentials_are_redacted(self):
        error = RuntimeError('URL ?key=unknown-key&x=1 Bearer unknown-token '
                             '{"api_key": "unknown-json-key"} AIzaUnknownGoogleKey')
        message = gemini_error_diagnostic(error, "Research Analyst", "offline-model")
        for secret in ("unknown-key", "unknown-token", "unknown-json-key", "AIzaUnknownGoogleKey"):
            self.assertNotIn(secret, message)

    def test_http_response_fallback(self):
        error = RuntimeError("Gateway failed")
        error.response = SimpleNamespace(status_code=502)
        self.assertIn("502", gemini_error_diagnostic(error, "Research Analyst", "offline-model"))

    def test_successful_request_keeps_persona_and_config(self):
        for role, filename in (("Research Analyst", "research_analyst.md"),
                               ("Financial Analyst", "financial_analyst.md"),
                               ("Investment Advisor", "investment_advisor.md")):
            with patch.object(SimpleNamespace(), "generate_content", create=True,
                              return_value=SimpleNamespace(text='{"ok": true}')) as generate:
                client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
                self.assertEqual(call_gemini(client, role, "offline-model", {"task": "test"}), {"ok": True})
            args = generate.call_args.kwargs
            persona = (Path(__file__).resolve().parents[1] / "personas" / filename).read_text(encoding="utf-8").strip()
            self.assertIn(persona, args["config"].system_instruction)
            self.assertEqual(args["model"], "offline-model")
            self.assertEqual(json.loads(args["contents"]), {"task": "test"})
            self.assertEqual(args["config"].response_mime_type, "application/json")
            self.assertEqual(args["config"].temperature, 0.2)


if __name__ == "__main__":
    unittest.main()
