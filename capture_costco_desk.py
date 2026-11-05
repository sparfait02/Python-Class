"""Capture one Costco practice run with UTF-8 and sanitized diagnostics."""

import logging
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime

from dotenv import load_dotenv
from equity_research import redact_provider_diagnostic


ROOT = Path(__file__).resolve().parent


def capture(command, log_path, console, metadata=(), cwd=ROOT):
    # Set both sides of the pipe: Windows Python otherwise uses its locale.
    environment = os.environ.copy()
    environment.update(PYTHONIOENCODING="utf-8:replace", PYTHONUTF8="1")
    with Path(log_path).open("x", encoding="utf-8", errors="replace") as log:
        def record(line):
            safe = redact_provider_diagnostic(line)
            log.write(safe + "\n")
            log.flush()
            # A redirected or legacy console must not interrupt log capture.
            try:
                console.write(safe + "\n")
                console.flush()
            except (UnicodeError, OSError):
                pass

        for line in metadata:
            record(line)
        record("Command: " + subprocess.list2cmdline(command))
        with subprocess.Popen(
            command, cwd=cwd, env=environment,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, encoding="utf-8", errors="replace",
        ) as process:
            for line in process.stdout:
                record(line.rstrip("\r\n"))
            code = process.wait()
        record("Process exit code: " + str(code))
        return code


def main():
    logging.disable(logging.CRITICAL)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    load_dotenv(ROOT / ".env", override=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    log_path = ROOT / "checkpoint2_tests" / f"costco_live_execution_{stamp}.txt"
    command = [sys.executable, "-u", str(ROOT / "equity_research.py"), "COST",
               "--peers", "WMT", "TGT", "BJ", "--price", "992.13", "--desk",
               "--model", "gemini-3.5-flash-lite"]
    return capture(command, log_path, sys.stdout, metadata=(
        "Historical practice price: USD 992.13, October 27, 2026; not current price.",
        "Execution log: " + str(log_path),
    ))


if __name__ == "__main__":
    sys.exit(main())
