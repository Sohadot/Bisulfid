#!/usr/bin/env python3
"""Sprint 99C — Validate sovereign conceptual interface restoration."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import atlas_validate_14k_semantic_interface_l3 as v99b  # noqa: E402
from atlas_dossier_common_l3 import strip_machine_content_for_audit  # noqa: E402
from atlas_hub_semantic_99bh import HUB_REQUIRED_PATHS  # noqa: E402

PUBLIC_DIR = ROOT / "site/public"
LEDGER_PATH = ROOT / "main/data/release_ledger.json"

CONCEPTUAL_MARKERS = (
    "atlas-control-strip",
    "atlas-control-room-hero",
    "bs-control-room-hero",
    "atlas-lane-prelude",
    "atlas-control-room-page",
)

DOSSIER_DOSSIER_RE = re.compile(r"\bdossier\s+dossier\b", re.I)


def validate_conceptual(rec: dict, public_paths: set[str]) -> tuple[list[str], dict]:
    errs, warns, meta = v99b.validate_page(rec, public_paths)
    if not meta.get("html_exists"):
        return errs, meta
    text = v99b.html_path_for(rec.get("route_path", "/")).read_text(encoding="utf-8")
    lower = text.lower()
    visible = strip_machine_content_for_audit(text)
    meta["conceptual_markers"] = {m: m in lower for m in CONCEPTUAL_MARKERS}
    for marker, ok in meta["conceptual_markers"].items():
        if not ok:
            errs.append(f"missing conceptual marker: {marker}")
    if DOSSIER_DOSSIER_RE.search(visible):
        errs.append("forbidden: dossier dossier duplication")
    meta["status"] = "PASS" if not errs else "FAIL"
    return errs, meta


def main() -> int:
    print("=" * 60)
    print("Sprint 99C — Conceptual Interface Validator")
    print("=" * 60)
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    released = [r for r in ledger["records"] if r["release_status"] == "released"]
    public_paths: set[str] = set()
    released_paths: set[str] = set()
    for rec in released:
        path = rec.get("route_path", "/").strip("/")
        norm = "/" if not path else f"/{path}/"
        public_paths.add(norm)
        released_paths.add(norm)

    css_errors, css_import_status = v99b.audit_css_imports()
    all_errors: list[str] = list(css_errors)
    conceptual_fail = 0
    dossier_dup_fail = 0

    for rec in released:
        errs, meta = validate_conceptual(rec, public_paths)
        if not all(meta.get("conceptual_markers", {}).values()):
            conceptual_fail += 1
        for e in errs:
            if "dossier dossier" in e:
                dossier_dup_fail += 1
            all_errors.append(f"{rec['route_id']}: {e}")

    sitemap_urls, sitemap_errors = v99b.sitemap_audit(released_paths)
    all_errors.extend(sitemap_errors)

    hub_fail = 0
    hub_rows: list[dict] = []
    for hub_path in v99b.hub_sample_paths():
        errs, meta = validate_conceptual(
            {"route_id": f"hub:{hub_path.strip('/') or 'home'}", "route_path": hub_path},
            public_paths,
        )
        if errs:
            hub_fail += 1
            for e in errs:
                all_errors.append(f"hub:{hub_path}: {e}")
        hub_rows.append(meta | {"route_path": hub_path, "errors": errs})

    sample = v99b.sample_routes(released)
    sample_errors = 0
    for rec in sample:
        errs, _ = validate_conceptual(rec, public_paths)
        if errs:
            sample_errors += 1

    summary_pass = not all_errors
    today = date.today().isoformat()

    restore_report = [
        "# 14K Conceptual Interface Restoration Report",
        "",
        f"**Date:** {today}",
        f"**Sprint:** 99C",
        "",
        "## Restoration applied",
        "",
        "- Control-room hero shell (`bs-control-room-hero`) on all dossier and hub pages",
        "- Chemical-language control strip in sovereign shell",
        "- Lane-specific interface preludes (terminology lattice, language boundary, compound crystal, material strata, governance crystal)",
        "- Copy repair: removed duplicated \"dossier dossier\" phrasing",
        "- Strengthened lane atmosphere in `atlas-semantic-interface.css`",
        "",
        f"**Released pages:** {len(released)}",
        f"**Conceptual marker failures:** {conceptual_fail}",
        f"**Dossier duplication failures:** {dossier_dup_fail}",
        f"**Hub failures:** {hub_fail}",
        f"**Sitemap URLs:** {sitemap_urls}",
        "",
        f"**Summary:** {'PASS' if summary_pass else 'FAIL'}",
    ]
    (ROOT / "main/data/14K_CONCEPTUAL_INTERFACE_RESTORATION_REPORT.md").write_text(
        "\n".join(restore_report) + "\n", encoding="utf-8"
    )

    audit_lines = [
        "# 14K Conceptual Interface Audit",
        "",
        f"**Date:** {today}",
        "",
        "## Required conceptual markers",
        "",
    ]
    for m in CONCEPTUAL_MARKERS:
        audit_lines.append(f"- `{m}`")
    audit_lines.extend([
        "",
        "## Hub conceptual status",
        "",
        "| Path | Status | Control strip | Control hero | Lane prelude |",
        "|------|--------|:-------------:|:------------:|:------------:|",
    ])
    for row in hub_rows:
        cm = row.get("conceptual_markers", {})
        audit_lines.append(
            f"| `{row.get('route_path', '')}` | {row.get('status', 'FAIL')} | "
            f"{'yes' if cm.get('atlas-control-strip') else 'no'} | "
            f"{'yes' if cm.get('atlas-control-room-hero') or cm.get('bs-control-room-hero') else 'no'} | "
            f"{'yes' if cm.get('atlas-lane-prelude') else 'no'} |"
        )
    audit_lines.extend(["", f"**Summary:** {'PASS' if hub_fail == 0 and conceptual_fail == 0 else 'FAIL'}"])
    (ROOT / "main/data/14K_CONCEPTUAL_INTERFACE_AUDIT.md").write_text(
        "\n".join(audit_lines) + "\n", encoding="utf-8"
    )

    val_lines = [
        "# 14K Validation After Conceptual Interface Restoration",
        "",
        f"**Date:** {today}",
        f"**Released routes:** {len(released)}",
        f"**Hub routes:** {len(HUB_REQUIRED_PATHS)}",
        f"**Sitemap URLs:** {sitemap_urls}",
        f"**Errors:** {len(all_errors)}",
        f"**Conceptual failures:** {conceptual_fail}",
        f"**Hub failures:** {hub_fail}",
        f"**Sample failures:** {sample_errors}",
        "",
        f"**Summary:** {'PASS' if summary_pass else 'FAIL'}",
    ]
    if all_errors:
        val_lines.extend(["", "## Errors (first 40)", ""])
        for e in all_errors[:40]:
            val_lines.append(f"- {e}")
    (ROOT / "main/data/14K_VALIDATION_AFTER_CONCEPTUAL_INTERFACE_RESTORATION.md").write_text(
        "\n".join(val_lines) + "\n", encoding="utf-8"
    )

    print(f"Released: {len(released)}")
    print(f"Sitemap URLs: {sitemap_urls}")
    print(f"Conceptual failures: {conceptual_fail}")
    print(f"Dossier dup failures: {dossier_dup_fail}")
    print(f"Hub failures: {hub_fail}")
    print(f"Errors: {len(all_errors)}")
    if all_errors:
        for e in all_errors[:15]:
            print(f"  ERROR: {e}")
        print("VALIDATION SUMMARY: FAIL")
        return 1
    print("VALIDATION SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
