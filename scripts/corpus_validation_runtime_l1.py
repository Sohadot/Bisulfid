#!/usr/bin/env python3
"""Corpus validation runtime L1 — orchestrates L1 + optional L0 checks (Sprint 5K).

Read-only. Python standard library only. Does not modify files.
"""
from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

L1_SCRIPTS = (
    "validate_corpus_routes_l1.py",
    "validate_corpus_drafts_l1.py",
    "validate_corpus_publication_lock_l1.py",
    "validate_corpus_claims_l1.py",
    "validate_corpus_references_l1.py",
)

L0_SCRIPTS = (
    "validate_route_registry_l0.py",
    "validate_content_drafts_l0.py",
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
    print("Bisulfid Corpus Validation Runtime — Layer 1")
    print(f"Date: {date.today().isoformat()}")
    print(f"Root: {ROOT}")
    print("Mode: read-only orchestration")
    print("=" * 60)
    print()

    results: list[tuple[str, int, str]] = []

    print("--- L1 Validators ---")
    for script in L1_SCRIPTS:
        code, output = run_script(script)
        results.append((script, code, output))
        status = "PASS" if code == 0 else "FAIL"
        print(f"[{status}] {script} (exit {code})")
    print()

    print("--- L0 Validators (informational) ---")
    for script in L0_SCRIPTS:
        code, output = run_script(script)
        results.append((script, code, output))
        status = "PASS" if code == 0 else "FAIL"
        print(f"[{status}] {script} (exit {code})")
    print()

    failed = [name for name, code, _ in results if code != 0]
    l1_failed = [name for name, code, _ in results if code != 0 and name in L1_SCRIPTS]

    print("=" * 60)
    print("DETAILED OUTPUT (L1 failures first, then all L1)")
    print("=" * 60)
    for script in L1_SCRIPTS:
        code = next(c for n, c, _ in results if n == script)
        if code != 0:
            print()
            print(f"--- {script} ---")
            out = next(o for n, c, o in results if n == script)
            print(out.encode("ascii", errors="replace").decode("ascii"))

    print()
    print("=" * 60)
    if l1_failed:
        print(f"RUNTIME SUMMARY: FAIL — L1 failures: {', '.join(l1_failed)}")
    else:
        print("RUNTIME SUMMARY: PASS — all L1 validators passed")
    l0_fail = [n for n, c, _ in results if c != 0 and n in L0_SCRIPTS]
    if l0_fail:
        print(f"L0 note: {', '.join(l0_fail)} reported warnings/errors (informational)")
    print("=" * 60)

    return 1 if l1_failed else 0


if __name__ == "__main__":
    sys.exit(main())
