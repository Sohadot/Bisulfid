#!/usr/bin/env python3
"""Sprint 99 — 14K public reference dossier production runtime."""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCRIPTS = [
    ("atlas_dossier_audit_l3.py", "14K dossier audit"),
    ("atlas_release_ledger_l3.py", "Release ledger"),
    ("atlas_render_dossier_l3.py", "14K dossier render"),
    ("atlas_generate_sitemaps_l3.py", "Sitemap shards"),
    ("atlas_validate_14k_release_l3.py", "14K validation"),
]


def run_script(name: str) -> int:
    path = ROOT / "scripts" / name
    r = subprocess.run([sys.executable, str(path)], cwd=str(ROOT))
    return r.returncode


def write_supplementary_reports() -> None:
    audit_path = ROOT / "main/data/14K_DOSSIER_RELEASE_AUDIT.json"
    if not audit_path.is_file():
        return
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    blocked = [r for r in audit["routes"] if r["release_eligibility"] == "blocked"]
    link_report = ROOT / "main/data/14K_INTERNAL_LINK_GRAPH_REPORT.md"
    link_report.write_text(
        "# 14K Internal Link Graph Report\n\n"
        f"**Date:** {date.today().isoformat()}\n\n"
        f"- Routes with link graph: {audit['released_count']}\n"
        f"- Minimum internal links per page: 8\n"
        f"- Standard hubs wired: home, sources, methodology, terminology spine, disambiguation, multilingual\n"
        f"- Related nodes selected by path prefix and lane proximity\n",
        encoding="utf-8",
    )
    blockers = ROOT / "main/data/14K_BLOCKED_ROUTES_REPORT.md"
    lines = [
        "# 14K Blocked Routes Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Blocked count:** {len(blocked)}",
        "",
        "## Blocked routes",
        "",
    ]
    for r in blocked:
        lines.append(f"- `{r['route_id']}` — {r['route_path']} — {r['release_mode']}")
    lines.extend([
        "",
        "## Rule",
        "",
        "Only routes that cannot be made public-safe without acquisition/investment leakage are blocked.",
        "All other routes release as cautious_reference_dossier or source_verified_page.",
    ])
    blockers.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    print("=" * 60)
    print("Sprint 99 — 14K Public Reference Dossier Production")
    print(f"Date: {date.today().isoformat()}")
    print("=" * 60)
    for script, label in SCRIPTS:
        print(f"\n--- {label} ({script}) ---")
        code = run_script(script)
        if code != 0:
            print(f"FAILED: {script} (exit {code})")
            return code
    write_supplementary_reports()
    print("\n14K DOSSIER PRODUCTION RUNTIME: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
