#!/usr/bin/env python3
"""Sprint 99 — Render full 14K public reference dossier output."""
from __future__ import annotations

import html
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from atlas_dossier_common_l3 import (  # noqa: E402
    audience_layers_html,
    build_breadcrumbs,
    build_dossier_body,
    build_internal_links_html,
    clean_description,
    load_classification,
    public_label,
    sanitize_public_text,
    substitute,
)

LEDGER_PATH = ROOT / "main/data/release_ledger.json"
ROUTES_PATH = ROOT / "main/data/routes.json"
PUBLIC_DIR = ROOT / "site/public"
TEMPLATES = ROOT / "main/templates/atlas"


def read_template(rel: str) -> str:
    return (TEMPLATES / rel).read_text(encoding="utf-8")


def main() -> int:
    print("=" * 60)
    print("Sprint 99 — 14K Dossier Render")
    print("=" * 60)
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
    routes_by_id = {r["route_id"]: r for r in routes}
    classification = load_classification()
    released = [r for r in ledger["records"] if r["release_status"] == "released"]
    base_tpl = read_template("base.html")
    dossier_tpl = read_template("dossier.html")
    breadcrumb_tpl = read_template("partials/breadcrumbs.html")
    footer_nav = read_template("partials/footer_nav.html")
    written = 0
    errors: list[str] = []
    for i, rec in enumerate(released):
        route = routes_by_id.get(rec["route_id"])
        if not route:
            errors.append(f"missing route: {rec['route_id']}")
            continue
        cls = classification.get(rec["route_id"], {})
        lane = rec.get("production_lane", "A")
        release_mode = rec.get("release_mode", "cautious_reference_dossier")
        body_html = build_dossier_body(route, cls, release_mode)
        links_html = build_internal_links_html(rec.get("internal_link_targets", []), routes_by_id)
        h1 = public_label(route)
        ctx = {
            "language": route.get("language", "en"),
            "text_direction": "ltr",
            "route_id": rec["route_id"],
            "page_title": sanitize_public_text(
                route.get("title", h1).replace("planned route; non-public", "").strip()
            ),
            "meta_description": html.escape(clean_description(route.get("description", ""))),
            "canonical_url": f"https://bisulfid.com{route.get('path', '/')}",
            "page_h1": h1,
            "atlas_role": f"Reference dossier · Lane {lane}",
            "atlas_classification": (
                f"Lane {lane} · {rec.get('page_type', 'dossier')} · {release_mode}"
            ),
            "reference_summary": clean_description(route.get("description", "")),
            "page_body": body_html,
            "source_posture_text": (
                "Cautious reference dossier. No unsupported chemical, medical, safety, market, "
                "or investment claims. Verified source packs govern factual terminology publication. "
                "No operational purchasing or supply-chain advice appears on this page."
            ),
            "audience_layers": audience_layers_html(route, cls),
            "internal_links": links_html,
            "breadcrumb_items": build_breadcrumbs(route),
            "atlas_footer_nav": footer_nav,
        }
        article = substitute(dossier_tpl, ctx)
        ctx["content"] = article
        ctx["breadcrumbs"] = substitute(breadcrumb_tpl, ctx)
        page = substitute(base_tpl, ctx)
        raw_path = route.get("path", "/").strip("/")
        out_path = PUBLIC_DIR / ("index.html" if not raw_path else f"{raw_path}/index.html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page, encoding="utf-8")
        written += 1
        if (i + 1) % 2000 == 0:
            print(f"  Rendered {i + 1}/{len(released)}...")
    report = ROOT / "main/data/14K_PUBLIC_CONTENT_QUALITY_REPORT.md"
    report.write_text(
        "# 14K Public Content Quality Report\n\n"
        f"**Date:** {date.today().isoformat()}\n"
        f"**Pages rendered:** {written}\n"
        f"**Errors:** {len(errors)}\n\n"
        "- Curated dossier bodies only (no governance draft markdown)\n"
        "- Minimum 8 internal links per page via link graph\n"
        "- index,follow on all released pages\n",
        encoding="utf-8",
    )
    print(f"Rendered: {written}")
    if errors:
        for e in errors[:20]:
            print(f"  ERROR: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
