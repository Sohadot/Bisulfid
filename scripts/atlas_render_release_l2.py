#!/usr/bin/env python3
"""Sprint 98 — Render atlas release pages (release-ledger driven only)."""
from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "main/data/release_ledger.json"
ROUTES_PATH = ROOT / "main/data/routes.json"
PUBLIC_DIR = ROOT / "site/public"
TEMPLATES = ROOT / "main/templates/atlas"
REPORT_PATH = ROOT / "main/data/PUBLIC_ATLAS_PRODUCTION_REPORT.md"

NON_PUBLIC_DESC_RE = re.compile(r"\(planned route;\s*non-public\)", re.I)


def read_template(rel: str) -> str:
    return (TEMPLATES / rel).read_text(encoding="utf-8")


def substitute(template: str, ctx: dict[str, str]) -> str:
    out = template
    for key, val in ctx.items():
        out = out.replace("{{" + key + "}}", val)
    return out


def clean_description(desc: str) -> str:
    desc = NON_PUBLIC_DESC_RE.sub("", desc)
    desc = re.sub(r"\s+", " ", desc).strip()
    return desc or "Bisulfid sovereign reference atlas."


def public_why_it_matters(route: dict, rec: dict) -> str:
    rid = route.get("route_id", "")
    h1 = route.get("h1", rid)
    layer = route.get("layer", "reference")
    defaults = {
        "home": "Primary gateway into the sovereign sulfur terminology atlas and its reference hubs.",
        "sources": "Documents how source discipline governs what the atlas may publish.",
        "corpus_methodology_overview": "Explains how the atlas corpus is structured, linked, and released.",
        "internal_linking_discipline": "Defines how atlas pages connect so no reference node is orphaned.",
        "quality_gate_public_explainer": "Describes the quality rules that gate public atlas publication.",
    }
    if rid in defaults:
        return defaults[rid]
    if rid.startswith("en_foundation_"):
        return f"Foundation reference for {h1} within the governed atlas architecture."
    if rid.startswith("en_index_"):
        return f"Index hub orienting readers across {h1.lower()} within the terminology atlas."
    if rid.startswith("en_gov_"):
        return f"Governance orientation for {h1} without operational or market advice."
    if rid.startswith("de_method_"):
        return f"German-language methodology orientation for {h1} in the multilingual atlas."
    return f"Reference hub for {h1} ({layer}) in the sovereign sulfur terminology atlas."


def _section(title: str, paragraphs: list[str], bullets: list[str] | None = None) -> str:
    parts = [f"<h2>{html.escape(title)}</h2>"]
    for p in paragraphs:
        parts.append(f"<p>{html.escape(p)}</p>")
    if bullets:
        parts.append("<ul>" + "".join(f"<li>{html.escape(b)}</li>" for b in bullets) + "</ul>")
    return "\n".join(parts)


def build_public_hub_body(route: dict, rec: dict) -> str:
    """Curated public-safe body — never dump governance draft markdown."""
    rid = route.get("route_id", "")
    h1 = route.get("h1", rid)
    desc = clean_description(route.get("description", ""))
    cautious = (
        "This page uses cautious framing only. Terminology factual claims elsewhere "
        "in the atlas require verified source packs before publication."
    )
    sections: list[str] = []

    if rid == "home":
        sections.append(_section("Atlas gateway", [
            "Bisulfid.com is a sovereign sulfur terminology reference atlas under governed publication rules.",
            "BISULFID is the sovereign domain and asset identifier; BISULFIDE is the conventional English "
            "spelling family; the missing final E is a governed spelling boundary.",
        ]))
        sections.append(_section("What this atlas covers", [
            desc,
        ], [
            "Terminology and nomenclature across German and English spelling boundaries",
            "Multilingual reference architecture and disambiguation",
            "Methodology, source discipline, and internal linking",
            "Foundation orientation for researchers, students, and institutional readers",
        ]))
        sections.append(_section("Corpus posture", [
            "The atlas scaffold contains thousands of planned reference routes. "
            "Only routes that pass release validation appear in public sitemaps.",
            cautious,
        ]))
    elif rid == "sources":
        sections.append(_section("Source discipline", [
            "The atlas publishes factual claims only when backed by verified source packs.",
            desc or "Source registry orientation for the sovereign reference atlas.",
        ], [
            "Verified sources are cited in approved claim library entries",
            "Unverified terminology routes remain blocked from public release",
            "Foundation and methodology pages explain source posture without inventing citations",
        ]))
    elif rid in {"corpus_methodology_overview", "internal_linking_discipline", "quality_gate_public_explainer"}:
        sections.append(_section("Methodology orientation", [desc or f"Methodology hub: {h1}."]))
        sections.append(_section("Release discipline", [
            cautious,
            "Public pages require title, meta description, canonical URL, breadcrumbs, "
            "and at least six meaningful internal links.",
        ]))
    elif rid.startswith("en_foundation_"):
        sections.append(_section("Foundation reference", [
            desc or f"Foundation orientation: {h1}.",
            "This page explains atlas architecture and publication doctrine. "
            "It does not provide chemical, medical, safety, or investment advice.",
        ]))
        sections.append(_section("Scope", [
            cautious,
        ], [
            "Orient readers to the sovereign reference mission",
            "Explain how terminology routes relate to methodology and sources",
            "Clarify what the atlas does and does not claim",
        ]))
    elif rid.startswith("en_index_"):
        sections.append(_section("Index hub", [
            desc or f"Atlas index: {h1}.",
            "Use this hub to navigate terminology spine, disambiguation, and multilingual layers.",
        ]))
        sections.append(_section("Navigation role", [cautious]))
    elif rid.startswith("en_gov_"):
        sections.append(_section("Governance orientation", [
            desc or f"Governance reference: {h1}.",
            "This page documents atlas governance rules. It is not legal or operational guidance.",
        ]))
    elif rid.startswith("de_method_"):
        sections.append(_section("Deutschsprachige Methodik", [
            desc or f"Methodik-Referenz: {h1}.",
            "Diese Seite orientiert im mehrsprachigen Referenzatlas ohne unbelegte Fachbehauptungen.",
        ]))
    else:
        sections.append(_section("Reference hub", [desc or f"Atlas hub: {h1}.", cautious]))

    sections.append(_section("Atlas role", [
        f"Production lane: {rec.get('production_lane', 'HUB')}. "
        f"Page type: {rec.get('page_type', 'atlas_hub')}.",
    ]))
    return "\n".join(sections)


def build_internal_links_html(targets: list[str], routes_by_id: dict) -> str:
    items = []
    for tid in targets:
        route = routes_by_id.get(tid)
        if not route:
            continue
        path = route.get("path", "/").rstrip("/") or ""
        label = route.get("h1") or route.get("title") or tid
        items.append(f'<li><a href="{html.escape(path + "/")}">{html.escape(label)}</a></li>')
    return "<ul>" + "".join(items) + "</ul>" if items else ""


def build_breadcrumbs(route: dict) -> str:
    path = route.get("path", "/").strip("/")
    parts = path.split("/") if path else []
    items = []
    acc = ""
    for part in parts:
        acc += "/" + part
        items.append(f'<li><span>{html.escape(part.replace("-", " ").title())}</span></li>')
    return "".join(items)


def audience_layers_html(route: dict) -> str:
    layer = route.get("layer", "reference")
    rid = route.get("route_id", "")
    return (
        f'<div class="atlas-layer atlas-layer--reference"><h3>Reference summary</h3>'
        f'<p>Governed atlas orientation for {html.escape(route.get("h1", rid))}.</p></div>'
        f'<div class="atlas-layer atlas-layer--technical"><h3>Technical layer</h3>'
        f'<p>Technical terminology context is provided without unsupported factual claims on this hub page.</p></div>'
        f'<div class="atlas-layer atlas-layer--language"><h3>Language layer</h3>'
        f'<p>Language: {html.escape(route.get("language", "en").upper())}. Spelling-boundary pages use cautious framing.</p></div>'
        f'<div class="atlas-layer atlas-layer--context"><h3>Context layer</h3>'
        f'<p>Atlas layer: {html.escape(layer)}. Part of the sovereign 14,000-route reference scaffold.</p></div>'
        f'<div class="atlas-layer atlas-layer--research"><h3>Research layer</h3>'
        f'<p>For researchers: use linked methodology and source pages before citing terminology routes.</p></div>'
        f'<div class="atlas-layer atlas-layer--student"><h3>Student / public layer</h3>'
        f'<p>Clear explanatory framing without simplifying into unsupported chemical claims.</p></div>'
    )


def main() -> int:
    print("=" * 60)
    print("Sprint 98 — Atlas Public Release Render")
    print("=" * 60)
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    routes = json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]
    routes_by_id = {r["route_id"]: r for r in routes}
    released = [r for r in ledger["records"] if r["release_status"] == "released"]
    # Real page paths, so breadcrumb ancestors without a generated page render as
    # plain text instead of a link that would resolve to a 404.
    valid_paths = {r.get("route_path", routes_by_id.get(r["route_id"], {}).get("path", "/")).strip("/") for r in released}
    for existing in PUBLIC_DIR.rglob("index.html"):
        rel = existing.parent.relative_to(PUBLIC_DIR).as_posix()
        valid_paths.add("" if rel == "." else rel)
    written = []
    errors = []
    hub_tpl = read_template("hub.html")
    base_tpl = read_template("base.html")
    breadcrumb_tpl = read_template("partials/breadcrumbs.html")
    footer_nav = read_template("partials/footer_nav.html")
    for rec in released:
        route = routes_by_id.get(rec["route_id"])
        if not route:
            errors.append(f"missing route: {rec['route_id']}")
            continue
        content_path = ROOT / route.get("content_file", "")
        if not content_path.is_file():
            errors.append(f"missing content: {rec['route_id']}")
            continue
        body_html = build_public_hub_body(route, rec)
        links_html = build_internal_links_html(rec.get("internal_link_targets", []), routes_by_id)
        ctx = {
            "language": route.get("language", "en"),
            "text_direction": "ltr",
            "route_id": route["route_id"],
            "page_title": route.get("title", route["route_id"]).replace("planned route; non-public", "").strip(),
            "meta_description": html.escape(clean_description(route.get("description", ""))),
            "canonical_url": f"https://bisulfid.com{route.get('path', '/')}",
            "page_h1": route.get("h1", route["route_id"]),
            "atlas_role": f"Atlas hub · {rec.get('production_lane', 'HUB')}",
            "reference_summary": clean_description(route.get("description", "")),
            "why_it_matters": public_why_it_matters(route, rec),
            "page_body": body_html,
            "source_posture_text": "Cautious framing only. Terminology factual claims require verified source packs.",
            "audience_layers": audience_layers_html(route),
            "internal_links": links_html,
            "breadcrumb_items": build_breadcrumbs(route, valid_paths),
            "atlas_footer_nav": footer_nav,
        }
        for k in list(ctx.keys()):
            if k not in ("meta_description",) and isinstance(ctx[k], str):
                pass
        hub_html = substitute(hub_tpl, ctx)
        ctx["content"] = hub_html
        ctx["breadcrumbs"] = substitute(breadcrumb_tpl, ctx)
        page = substitute(base_tpl, ctx)
        raw_path = route.get("path", "/").strip("/")
        out_path = PUBLIC_DIR / ("index.html" if not raw_path else f"{raw_path}/index.html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page, encoding="utf-8")
        written.append(str(out_path.relative_to(ROOT)).replace("\\", "/"))
    lines = [
        "# Public Atlas Production Report",
        "",
        f"**Date:** {date.today().isoformat()}",
        f"**Released pages rendered:** {len(written)}",
        f"**Errors:** {len(errors)}",
        "",
        "## Rendered routes",
        "",
    ]
    for w in written:
        lines.append(f"- `{w}`")
    if errors:
        lines.extend(["", "## Errors", ""])
        for e in errors:
            lines.append(f"- {e}")
    lines.extend([
        "",
        "## Posture",
        "",
        "- Only release-ledger `released` routes rendered",
        "- 13,971+ terminology routes remain blocked (source required)",
        "- Full 14,000-page atlas not claimed live",
    ])
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Rendered: {len(written)}")
    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        return 1
    print(f"Report: {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
