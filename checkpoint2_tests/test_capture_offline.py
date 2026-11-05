"""Exercise actual pipes with Unicode and malformed bytes, without network."""

import io
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from capture_costco_desk import capture


class CaptureTest(unittest.TestCase):
    def test_unicode_invalid_bytes_and_secrets(self):
        with tempfile.TemporaryDirectory() as folder:
            log = Path(folder) / "execution.txt"
            console = io.StringIO()
            script = ("import os,sys; "
                      "print('Unicode: \\u2014 \\u2019 \\ufffd'); "
                      "print(os.environ['PYTHONIOENCODING']); "
                      "print(os.environ['CAPTURE_TEST_SECRET']); "
                      "sys.stdout.flush(); "
                      "sys.stdout.buffer.write(b'invalid: \\xff\\n'); "
                      "sys.stderr.write('stderr captured\\n')")
            with patch.dict(os.environ, {"CAPTURE_TEST_SECRET": "offline-only-value"}):
                code = capture([sys.executable, "-c", script], log, console)
            text = log.read_text(encoding="utf-8")
            self.assertEqual(code, 0)
            self.assertIn("Unicode: — ’ �", text)
            self.assertIn("invalid: �", text)
            self.assertIn("utf-8:replace", text)
            self.assertIn("stderr captured", text)
            self.assertNotIn("offline-only-value", text)
            self.assertEqual(text, console.getvalue())

    def test_legacy_console_and_nonzero_exit(self):
        with tempfile.TemporaryDirectory() as folder:
            log = Path(folder) / "execution.txt"
            console = io.TextIOWrapper(io.BytesIO(), encoding="cp1252", errors="strict")
            code = capture([sys.executable, "-c",
                            "import sys; print('\\ufffd'); sys.exit(7)"], log, console)
            self.assertEqual(code, 7)
            self.assertIn("�", log.read_text(encoding="utf-8"))
            self.assertIn("Process exit code: 7", log.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
