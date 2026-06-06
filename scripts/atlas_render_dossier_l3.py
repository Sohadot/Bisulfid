#!/usr/bin/env python3
"""Sprint 99/99A/99B/99C — Render full 14K public reference dossier output."""
from __future__ import annotations

import html
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from atlas_dossier_common_l3 import (  # noqa: E402
    STYLESHEET_PATH,
    atlas_lane_slug,
    audience_layers_html,
    build_atlas_control_strip,
    build_audience_panel_html,
    build_breadcrumbs,
    build_dossier_body,
    build_internal_links_html,
    build_lane_interface_prelude,
    build_role_panel_html,
    public_category_label,
    public_lane_role,
    public_label,
    public_summary,
    semantic_body_classes,
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
    print("Sprint 99C — 14K Conceptual Interface Dossier Render")
    print("=" * 60)
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
    routes_by_id = {r["route_id"]: r for r in routes}
    classification = {}
    class_path = ROOT / "main/data/14K_CORPUS_CLASSIFICATION.json"
    if class_path.is_file():
        classification = {
            r["route_id"]: r
            for r in json.loads(class_path.read_text(encoding="utf-8"))["routes"]
        }
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
        cls = classification.get(rec["route_id"], {"proposed_production_lane": rec.get("production_lane", "A")})
        lane = cls.get("proposed_production_lane", rec.get("production_lane", "A"))
        release_mode = rec.get("release_mode", "cautious_reference_dossier")
        role = public_lane_role(lane)
        body_html = build_dossier_body(route, cls, release_mode)
        links_html = build_internal_links_html(rec.get("internal_link_targets", []), routes_by_id)
        h1 = public_label(route)
        summary = public_summary(route, cls)
        page_title = h1
        if "bisulfid.com" not in page_title.lower():
            page_title = f"{h1} — Bisulfid Atlas"
        path = route.get("path", "/")
        lang = route.get("language", "en")
        ctx = {
            "language": lang,
            "text_direction": "ltr",
            "page_title": html.escape(page_title),
            "meta_description": html.escape(summary),
            "canonical_url": f"https://bisulfid.com{path}",
            "page_h1": html.escape(h1),
            "atlas_role": html.escape(role),
            "atlas_lane_slug": atlas_lane_slug(lane),
            "body_semantic_classes": semantic_body_classes(lane, path),
            "atlas_category": html.escape(public_category_label(role)),
            "reference_summary": html.escape(summary),
            "atlas_control_strip": build_atlas_control_strip(lane, lang),
            "lane_interface_prelude": build_lane_interface_prelude(lane, route, cls),
            "role_panel_body": build_role_panel_html(route, cls, release_mode),
            "page_body": body_html,
            "source_posture_text": (
                "This page is a Source-Governed Reference Page within the Bisulfid Atlas. "
                "It does not provide medical, safety, market, investment, or operational purchasing guidance. "
                "Verified source packs govern factual terminology publication across the atlas."
            ),
            "audience_layers": audience_layers_html(route, cls),
            "audience_panel": build_audience_panel_html(lane, path),
            "internal_links": links_html,
            "breadcrumb_items": build_breadcrumbs(route),
            "atlas_footer_nav": footer_nav,
        }
        article = substitute(dossier_tpl, ctx)
        ctx["content"] = article
        ctx["breadcrumbs"] = substitute(breadcrumb_tpl, ctx)
        page = substitute(base_tpl, ctx)
        if STYLESHEET_PATH not in page:
            errors.append(f"{rec['route_id']}: missing absolute stylesheet")
        raw_path = route.get("path", "/").strip("/")
        out_path = PUBLIC_DIR / ("index.html" if not raw_path else f"{raw_path}/index.html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page, encoding="utf-8")
        written += 1
        if (i + 1) % 2000 == 0:
            print(f"  Rendered {i + 1}/{len(released)}...")
    print(f"Rendered: {written}")
    if errors:
        for e in errors[:20]:
            print(f"  ERROR: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
