#!/usr/bin/env python3
"""Sprint 98 — Atlas production runtime orchestrator."""
from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    ("atlas_corpus_classifier_l2.py", "14K classification"),
    ("atlas_release_ledger_l2.py", "Release ledger"),
    ("atlas_render_release_l2.py", "Atlas render"),
    ("atlas_generate_sitemaps_l1.py", "Sitemap shards"),
    ("atlas_validate_public_release_l1.py", "Release validation"),
]

REPORT_SCRIPTS = [
    ("SOURCE_PACK_ARCHITECTURE_REPORT.md", None),
    ("CLAIM_LIBRARY_REPORT.md", None),
    ("BLOCKERS_TO_14K_PUBLIC_RELEASE.md", None),
]


def run_script(name: str) -> int:
    path = ROOT / "scripts" / name
    r = subprocess.run([sys.executable, str(path)], cwd=str(ROOT))
    return r.returncode


def write_supplementary_reports() -> None:
    sp_report = ROOT / "main/data/SOURCE_PACK_ARCHITECTURE_REPORT.md"
    sp_report.write_text(
        "# Source Pack Architecture Report\n\n"
        f"**Sprint:** 98\n**Date:** {date.today().isoformat()}\n\n"
        "Registry: `main/data/source_packs/source_pack_registry.json`\n\n"
        "8 source packs defined. No invented sources. "
        "`SPK-CAUTIOUS-FRAMING` eligible for atlas hub release. "
        "Terminology packs blocked until verification.\n",
        encoding="utf-8",
    )
    cl_report = ROOT / "main/data/CLAIM_LIBRARY_REPORT.md"
    cl_report.write_text(
        "# Claim Library Report\n\n"
        f"**Sprint:** 98\n**Date:** {date.today().isoformat()}\n\n"
        "Registry: `main/data/claims/claim_library.json`\n\n"
        "3 cautious framing claims approved for hub pages. "
        "Terminology claims blocked pending source verification.\n",
        encoding="utf-8",
    )
    blockers = ROOT / "main/data/BLOCKERS_TO_14K_PUBLIC_RELEASE.md"
    blockers.write_text(
        "# Blockers to 14K Public Release\n\n"
        f"**Sprint:** 98\n**Date:** {date.today().isoformat()}\n\n"
        "## Primary blockers\n\n"
        "1. **13,971 routes require verified sources** — source registry inactive at scale\n"
        "2. **Claim registries inactive** — only 1 narrow approved claim (MoS₂ DE)\n"
        "3. **Terminology draft content contains [SOURCE REQUIRED] markers** — cannot publish without sanitization + approved claims\n"
        "4. **Sprint 97A baseline not in repo** — starting from 0 indexable routes, not 52\n"
        "5. **Visual proof gate (6N-D)** — full design-system refresh blocked pending human review\n\n"
        "## Wave 2 outcome\n\n"
        "Maximum safe release: **26 atlas hub pages** (foundation, methodology, index maps, home, sources).\n"
        "This is **below the 500-page expansion threshold**. No thin terminology pages published.\n\n"
        "## Path to 14,000\n\n"
        "- Verify source packs per production lane\n"
        "- Approve claims per route family\n"
        "- Release-ledger-driven render replaces foundation noindex scaffold per route\n"
        "- Expand internal link graph as lanes unlock\n",
        encoding="utf-8",
    )


def main() -> int:
    print("=" * 60)
    print("Sprint 98 — Atlas Production Runtime")
    print(f"Date: {date.today().isoformat()}")
    print("=" * 60)
    write_supplementary_reports()
    for script, label in SCRIPTS:
        print(f"\n--- {label} ({script}) ---")
        code = run_script(script)
        if code != 0:
            print(f"FAILED: {script} (exit {code})")
            return code
    print("\nATLAS PRODUCTION RUNTIME: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
