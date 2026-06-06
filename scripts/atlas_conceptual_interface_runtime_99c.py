#!/usr/bin/env python3
"""Sprint 99C — Sovereign conceptual interface restoration runtime."""
from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCRIPTS = [
    ("atlas_render_dossier_l3.py", "Conceptual interface dossier render"),
    ("atlas_align_legacy_hubs_99bh.py", "Legacy hub shell alignment"),
    ("atlas_validate_14k_conceptual_interface_99c.py", "Conceptual interface validation"),
]


def run_script(name: str) -> int:
    path = ROOT / "scripts" / name
    return subprocess.run([sys.executable, str(path)], cwd=str(ROOT)).returncode


def main() -> int:
    print("=" * 60)
    print("Sprint 99C — Sovereign Conceptual Interface Restoration")
    print(f"Date: {date.today().isoformat()}")
    print("=" * 60)
    for script, label in SCRIPTS:
        print(f"\n--- {label} ({script}) ---")
        code = run_script(script)
        if code != 0:
            print(f"FAILED: {script} (exit {code})")
            return code
    print("\n99C CONCEPTUAL INTERFACE RUNTIME: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
