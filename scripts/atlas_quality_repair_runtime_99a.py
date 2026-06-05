#!/usr/bin/env python3
"""Sprint 99A — Public quality repair runtime (no corpus expansion)."""
from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCRIPTS = [
    ("atlas_render_dossier_l3.py", "Quality repair render"),
    ("atlas_validate_14k_quality_repair_l3.py", "Quality repair validation"),
]


def run_script(name: str) -> int:
    path = ROOT / "scripts" / name
    return subprocess.run([sys.executable, str(path)], cwd=str(ROOT)).returncode


def main() -> int:
    print("=" * 60)
    print("Sprint 99A — 14K Public Quality Repair Gate")
    print(f"Date: {date.today().isoformat()}")
    print("=" * 60)
    for script, label in SCRIPTS:
        print(f"\n--- {label} ({script}) ---")
        code = run_script(script)
        if code != 0:
            print(f"FAILED: {script} (exit {code})")
            return code
    print("\n99A QUALITY REPAIR RUNTIME: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
