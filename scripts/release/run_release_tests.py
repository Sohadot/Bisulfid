#!/usr/bin/env python3
"""run_release_tests.py — run the CI-equivalent suites and record results for the release package.

Writes main/data/release/TEST_RESULTS.json: one entry per command (exit code + last output line).
Exit 1 if any command fails. The live deploy gate is recorded, not required to pass (it reflects site/public).
"""

import datetime
import json
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CMDS = [
    "scripts/publication/test_publication_authority.py",
    "scripts/governance_scaffolding/route_realization_tests.py",
    "scripts/release/release_checks_tests.py",
    "scripts/publication/build_consolidation_obligations.py --check",
    "scripts/release/build_review_packets.py --check",
    "scripts/reference_production/render_ko_reference.py --check",
    "scripts/reference_production/render_institutional_preview.py --check",
    "scripts/reference_production/seo_preview_check.py",
    "scripts/validators/test_distinctiveness.py",
    "scripts/validators/test_legacy_migration.py",
    "scripts/validators/validate_distinctiveness.py --gate",
    "scripts/validators/validate_distinctiveness.py --check-hold --hold-ratchet-ref origin/main",
    "scripts/recovery/validate_legacy_disposition.py",
    "scripts/governance_scaffolding/validate_scaffolding.py",
    "scripts/governance_scaffolding/validate_concept_lexeme.py",
    "scripts/governance_scaffolding/contract_c_property_tests.py",
    "scripts/governance_scaffolding/ig_governance_tests.py",
    "scripts/governance_scaffolding/reference_production_tests.py",
    "scripts/governance_scaffolding/source_admissibility_tests.py",
    "scripts/corpus_validation_runtime_l1.py",
    "scripts/source_claim_guardrail_runtime_l1.py",
    "scripts/corpus_production_runtime_l2.py",
    "scripts/validate_route_registry_l0.py",
    "scripts/validate_content_drafts_l0.py",
    "scripts/publication/validate_publication_authority.py --surface site/public",
]


def main():
    out = []
    for c in CMDS:
        r = subprocess.run([sys.executable] + c.split(), cwd=ROOT, capture_output=True, text=True)
        lines = [x for x in (r.stdout + r.stderr).splitlines() if x.strip()]
        out.append({"command": c, "exit_code": r.returncode, "last_line": lines[-1][:200] if lines else ""})
        print(f"[{'PASS' if r.returncode == 0 else 'FAIL'}] {c}")
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    with open(os.path.join(ROOT, "main", "data", "release", "TEST_RESULTS.json"), "w", encoding="utf-8") as fh:
        json.dump({"run_on": datetime.date.today().isoformat(), "tree_at_commit": commit, "results": out}, fh, indent=1)
        fh.write("\n")
    return 1 if any(x["exit_code"] for x in out) else 0


if __name__ == "__main__":
    sys.exit(main())
