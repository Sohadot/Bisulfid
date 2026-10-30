#!/usr/bin/env python3
"""validate_all.py — Quality Gate orchestrator.

Gates 01-11 are still placeholders. Gate 12 (Page Distinctiveness & Information Gain)
is REAL, BLOCKING enforcement: validate_distinctiveness.py checks markdown publication
candidates and every indexable page of the site/public surface, and exits non-zero on failure.

Runs all validators in Quality Gate order.
Prints a non-enforcement warning for the placeholder gates before and after running.

This file uses subprocess to run local validator files safely.
No network calls. No file writes. No external dependencies.
"""

import os
import subprocess
import sys

# TODO: When validators are fully implemented, this orchestrator should:
# TODO: Run validators in strict Quality Gate order (Gate 01 through Gate 12)
# TODO: Collect exit codes and emit a structured per-gate pass/fail report
# TODO: Exit non-zero immediately if any validator reports a real failure
# TODO: Produce a machine-readable summary (JSON) for CI integration
# TODO: Accept --gate <n> flag to run a single gate in isolation
# TODO: Integrate with build system pipeline as a pre-deploy blocker

VALIDATORS = [
    # Gate 01 + Gate 08 — links and orphans
    "validate_links.py",
    # Gate 02 + Gate 09 — content quality and placeholders
    "validate_content.py",
    # Gate 03 — sitemap and indexation
    "validate_indexation.py",
    # Gate 04 — source registry
    "validate_sources.py",
    # Gate 04 + blocked-claim patterns
    "validate_claims.py",
    # Gate 05 — SEO
    "validate_seo.py",
    # Gate 06 — security posture
    "validate_security.py",
    # Gate 07 — accessibility
    "validate_accessibility.py",
    # Route governance (prerequisite to all gates)
    "validate_routes.py",
    # Structured data
    "validate_schema.py",
    # Gate 11 — hreflang correctness
    "validate_hreflang.py",
    # Gate 11 — translation integrity
    "validate_translations.py",
    # Gate 11 — language route governance
    "validate_language_routes.py",
    # Supply chain security
    "validate_supply_chain.py",
    # Gate 12 — page distinctiveness & information gain (REAL, BLOCKING)
    ("validate_distinctiveness.py", "--gate"),
    ("validate_distinctiveness.py", "--surface", "site/public"),
]

# Validators that perform real enforcement (their exit 0 is meaningful).
ENFORCING = {"validate_distinctiveness.py"}


def main():
    print("=" * 60)
    print("Gates 01-11: validator skeleton only. Full enforcement is not active yet.")
    print("Placeholder validators do not confirm production readiness.")
    print("Gate 12 (distinctiveness & information gain) is REAL, BLOCKING enforcement.")
    print("=" * 60)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    all_passed = True
    enforcing_failed = []

    for entry in VALIDATORS:
        validator, args = (entry, ()) if isinstance(entry, str) else (entry[0], entry[1:])
        path = os.path.join(script_dir, validator)
        if not os.path.isfile(path):
            print(f"  MISSING: {validator}")
            all_passed = False
            continue
        result = subprocess.run(
            [sys.executable, path, *args],
            capture_output=False,
            cwd=repo_root,
        )
        if result.returncode != 0:
            label = " ".join((validator,) + tuple(args))
            print(f"  FAILED:  {label} exited {result.returncode}")
            all_passed = False
            if validator in ENFORCING:
                enforcing_failed.append(label)

    print("=" * 60)
    if all_passed:
        print("All validators exited 0.")
        print("NOTE: Gates 01-11 are placeholders; only Gate 12's pass is enforced.")
    else:
        print("One or more validators are missing or exited non-zero.")
        for label in enforcing_failed:
            print(f"  BLOCKING (real enforcement): {label}")
    print("=" * 60)

    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
