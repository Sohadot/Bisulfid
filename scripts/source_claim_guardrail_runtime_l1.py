#!/usr/bin/env python3
"""Source and claim guardrail runtime L1 — orchestrates specialized validators (Sprint 5N-B).

Read-only. Python standard library only. Does not modify files.
"""
from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GUARDRAIL_SCRIPTS = (
    "validate_source_registration_proposals_l1.py",
    "validate_source_evidence_requirements_l1.py",
    "validate_claim_boundary_preparation_l1.py",
    "validate_source_registry_lock_l1.py",
    "validate_claim_registry_lock_l1.py",
)


def run_script(name: str) -> tuple[int, str]:
    path = ROOT / "scripts" / name
    if not path.exists():
        return 1, f"MISSING: {name}"
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output


def main() -> int:
    print("=" * 60)
    print("Bisulfid Source & Claim Guardrail Runtime — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Root: {ROOT}")
    print("Mode: read-only orchestration")
    print("=" * 60)
    print()

    results: list[tuple[str, int, str]] = []

    print("--- Source/Claim Guardrail Validators ---")
    for script in GUARDRAIL_SCRIPTS:
        code, output = run_script(script)
        results.append((script, code, output))
        status = "PASS" if code == 0 else "FAIL"
        print(f"[{status}] {script} (exit {code})")
    print()

    failed = [name for name, code, _ in results if code != 0]

    print("=" * 60)
    print("DETAILED OUTPUT (failures first)")
    print("=" * 60)
    for script, code, output in results:
        if code != 0:
            print()
            print(f"--- {script} ---")
            print(output.encode("ascii", errors="replace").decode("ascii"))

    print()
    print("=" * 60)
    if failed:
        print(f"GUARDRAIL SUMMARY: FAIL — failures: {', '.join(failed)}")
    else:
        print("GUARDRAIL SUMMARY: PASS — all source/claim guardrail validators passed")
    print("=" * 60)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
