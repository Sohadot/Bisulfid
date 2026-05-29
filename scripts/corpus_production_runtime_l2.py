#!/usr/bin/env python3
"""Corpus production runtime L2 — orchestrates L2 production validators (Sprint 5O-A).

Read-only. Python standard library only. Does not modify files.
"""
from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

L2_SCRIPTS = (
    "corpus_production_planner_l2.py",
    "validate_production_wave_plan_l2.py",
    "validate_internal_link_graph_plan_l2.py",
    "validate_seo_indexation_plan_l2.py",
    "validate_multilingual_wave_plan_l2.py",
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
    print("Bisulfid Corpus Production Runtime — Layer 2")
    print(f"Date: {date.today().isoformat()}")
    print(f"Root: {ROOT}")
    print("Mode: read-only orchestration / dry-run")
    print("=" * 60)
    print()

    results: list[tuple[str, int, str]] = []

    print("--- L2 Production Validators ---")
    for script in L2_SCRIPTS:
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
        print(f"L2 RUNTIME SUMMARY: FAIL — failures: {', '.join(failed)}")
    else:
        print("L2 RUNTIME SUMMARY: PASS — all L2 production validators passed")
    print("=" * 60)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
