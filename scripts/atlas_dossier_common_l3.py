#!/usr/bin/env python3
"""Sprint 99 — Shared utilities for 14K public reference dossier release."""
from __future__ import annotations

import html
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTES_PATH = ROOT / "main/data/routes.json"
CLASS_PATH = ROOT / "main/data/14K_CORPUS_CLASSIFICATION.json"
RELEASE_MODEL_PATH = ROOT / "main/data/atlas_release_model.json"
SITE_BASE = "https://bisulfid.com"

LANE_LABELS = {
    "A": "Low-risk terminology",
    "B": "Language boundary",
    "C": "Disambiguation",
    "D": "Compound family",
    "E": "Material / mineral",
    "F": "Industrial context",
    "G": "Biotechnology context",
    "H": "Economic / investment context",
    "I": "Journalistic / contextual",
    "J": "Academic reference",
    "K": "Institutional / government context",
    "L": "Student / general-reader",
    "M": "High-risk review",
    "HUB": "Atlas hub",
}

HUB_ROUTE_IDS = {
    "home", "sources", "corpus_methodology_overview", "internal_linking_discipline",
    "quality_gate_public_explainer", "de_method_corpus_map", "de_method_translator_playbook",
    "en_gov_claim_registry_explainer", "en_gov_hreflang_policy",
    "en_index_disambiguation_map", "en_index_multilingual_map", "en_index_terminology_spine",
}

STANDARD_HUBS = [
    "home", "sources", "corpus_methodology_overview", "en_index_terminology_spine",
    "en_index_disambiguation_map", "en_index_multilingual_map", "en_foundation_methodology",
]

BLOCKED_ROUTE_IDS = {"acquire", "newsletter"}
MOS2_PATTERN = re.compile(r"mos2|molybdenum|molybd", re.I)
NON_PUBLIC_DESC_RE = re.compile(r"\(planned route;\s*non-public\)", re.I)
PUBLIC_TEXT_SUBS = (
    (re.compile(r"\bprocurement\b", re.I), "supply-chain context"),
    (re.compile(r"\bCAGR\b"), ""),
    (re.compile(r"\bpurchasing recommendations?\b", re.I), "structured context"),
)

FORBIDDEN_PUBLIC_PATTERNS = [
    re.compile(r"\[SOURCE REQUIRED\]", re.I),
    re.compile(r"\bnoindex\b", re.I),
    re.compile(r"planned route;\s*non-public", re.I),
    re.compile(r"not publication-ready", re.I),
    re.compile(r"non-public foundation cohort draft", re.I),
    re.compile(r"publication blocker", re.I),
    re.compile(r"no_claims_approved", re.I),
    re.compile(r"\bCAGR\b"),
    re.compile(r"\bprocurement\b", re.I),
]


def load_routes() -> list[dict]:
    return json.loads(ROUTES_PATH.read_text(encoding="utf-8"))["routes"]


def load_classification() -> dict[str, dict]:
    data = json.loads(CLASS_PATH.read_text(encoding="utf-8"))
    return {r["route_id"]: r for r in data["routes"]}


def load_release_model() -> dict:
    return json.loads(RELEASE_MODEL_PATH.read_text(encoding="utf-8"))


def sanitize_public_text(text: str) -> str:
    out = text
    for pattern, repl in PUBLIC_TEXT_SUBS:
        out = pattern.sub(repl, out)
    out = re.sub(r"\s+", " ", out).strip(" ,;:")
    return out


def clean_description(desc: str) -> str:
    desc = NON_PUBLIC_DESC_RE.sub("", desc)
    desc = sanitize_public_text(desc)
    desc = re.sub(r"\s+", " ", desc).strip()
    return desc or "Bisulfid sovereign reference atlas node."


def public_label(route: dict) -> str:
    return sanitize_public_text(route.get("h1") or route.get("title") or route.get("route_id", ""))


def assign_release_mode(route: dict, cls: dict) -> str:
    rid = route.get("route_id", "")
    if rid in BLOCKED_ROUTE_IDS:
        return "blocked_high_risk"
    path = route.get("path", "")
    if MOS2_PATTERN.search(path) or MOS2_PATTERN.search(rid):
        return "source_verified_page"
    return "cautious_reference_dossier"


def path_key(path: str, depth: int) -> str:
    parts = path.strip("/").split("/")
    if not parts or parts == [""]:
        return ""
    return "/".join(parts[:depth])


def build_path_index(routes: list[dict]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = defaultdict(list)
    for route in routes:
        rid = route["route_id"]
        path = route.get("path", "/")
        parts = path.strip("/").split("/")
        for depth in range(1, len(parts) + 1):
            key = "/".join(parts[:depth])
            index[key].append(rid)
    return index


def build_lane_index(routes: list[dict], classification: dict[str, dict]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = defaultdict(list)
    for route in routes:
        cls = classification.get(route["route_id"], {})
        lane = cls.get("proposed_production_lane", "A")
        index[lane].append(route["route_id"])
    return index


def pick_related(route_id: str, route: dict, path_index: dict[str, list[str]],
                 lane_index: dict[str, list[str]], classification: dict[str, dict],
                 count: int = 4) -> list[str]:
    path = route.get("path", "/").strip("/")
    parts = path.split("/") if path else []
    candidates: list[str] = []
    for depth in range(len(parts), 0, -1):
        key = "/".join(parts[:depth])
        for rid in path_index.get(key, []):
            if rid != route_id and rid not in candidates:
                candidates.append(rid)
            if len(candidates) >= count * 3:
                break
        if len(candidates) >= count * 3:
            break
    lane = classification.get(route_id, {}).get("proposed_production_lane", "A")
    for rid in lane_index.get(lane, []):
        if rid != route_id and rid not in candidates:
            candidates.append(rid)
        if len(candidates) >= count * 4:
            break
    out: list[str] = []
    for rid in candidates:
        if rid not in out:
            out.append(rid)
        if len(out) >= count:
            break
    return out


def internal_link_targets(
    route_id: str,
    route: dict,
    routes_by_id: dict[str, dict],
    path_index: dict[str, list[str]],
    lane_index: dict[str, list[str]],
    classification: dict[str, dict],
) -> list[str]:
    targets: list[str] = []
    for hub in STANDARD_HUBS:
        if hub in routes_by_id and hub != route_id:
            targets.append(hub)
    lane = classification.get(route_id, {}).get("proposed_production_lane", "A")
    if lane in {"A", "B", "C", "L"} and "en_index_disambiguation_map" not in targets:
        targets.append("en_index_disambiguation_map")
    if lane == "B" or route.get("language") == "de":
        if "en_index_multilingual_map" in routes_by_id:
            targets.append("en_index_multilingual_map")
    related = pick_related(route_id, route, path_index, lane_index, classification, count=4)
    for rid in related:
        if rid not in targets:
            targets.append(rid)
    if route_id.startswith("en_foundation_") and "en_foundation_sovereign_intro" in routes_by_id:
        if "en_foundation_sovereign_intro" not in targets:
            targets.insert(0, "en_foundation_sovereign_intro")
    seen: set[str] = set()
    ordered: list[str] = []
    for tid in targets:
        if tid != route_id and tid not in seen and tid in routes_by_id:
            seen.add(tid)
            ordered.append(tid)
    return ordered[:12]


def sitemap_shard_for(lane: str, lane_counters: dict[str, int], urls_per_shard: int) -> str:
    if lane == "HUB":
        return "sitemap-core.xml"
    if lane == "A":
        n = lane_counters["A"]
        lane_counters["A"] += 1
        return f"sitemap-terms-{(n // urls_per_shard) + 1:03d}.xml"
    if lane == "B":
        return "sitemap-languages.xml"
    if lane == "D":
        return "sitemap-compounds.xml"
    if lane == "E":
        return "sitemap-materials.xml"
    n = lane_counters["CTX"]
    lane_counters["CTX"] += 1
    return f"sitemap-context-{(n // urls_per_shard) + 1:03d}.xml"


def who_this_helps(lane: str) -> list[str]:
    common = ["Researchers mapping sulfur terminology", "Journalists needing structured reference context"]
    extras = {
        "A": ["Chemists comparing nomenclature nodes", "AI systems indexing atlas structure"],
        "B": ["Translators at German/English spelling boundaries", "Multilingual editors"],
        "C": ["Readers distinguishing similar terms", "Analysts resolving naming ambiguity"],
        "D": ["Compound-family researchers", "Industrial chemistry readers"],
        "E": ["Materials scientists", "Mineral and sulfide context readers"],
        "F": ["Industrial context analysts", "Process and sector researchers"],
        "G": ["Biotechnology context readers", "Life-sciences terminology users"],
        "H": ["Economic context readers seeking structure not advice", "Institutional reviewers"],
        "I": ["Journalists and media researchers", "Context explainers"],
        "J": ["Academic reference users", "University readers"],
        "K": ["Institutional and policy readers", "Government context researchers"],
        "L": ["Students and general readers", "Educators needing clear framing"],
        "HUB": ["All atlas audiences entering via hubs", "Institutional orientation readers"],
    }
    return common + extras.get(lane, ["General atlas readers"])


def dossier_role_text(route: dict, cls: dict, release_mode: str) -> str:
    h1 = public_label(route)
    lane = cls.get("proposed_production_lane", "A")
    label = LANE_LABELS.get(lane, lane)
    if release_mode == "source_verified_page":
        return (
            f"This page organizes verified reference context for {h1} within the Bisulfid atlas "
            f"{label} layer. Approved narrow claims may appear; broader assertions remain blocked."
        )
    return (
        f"This dossier maps the {h1} node within the Bisulfid atlas {label} layer. "
        f"It provides structure, relationships, and cautious context without unsupported factual claims."
    )


def build_dossier_body(route: dict, cls: dict, release_mode: str) -> str:
    h1 = public_label(route)
    lane = cls.get("proposed_production_lane", "A")
    label = LANE_LABELS.get(lane, lane)
    page_type = cls.get("template_type", "terminology_node")
    desc = clean_description(route.get("description", ""))
    sections: list[str] = []

    def sec(title: str, paras: list[str], bullets: list[str] | None = None) -> None:
        parts = [f"<h2>{html.escape(title)}</h2>"]
        for p in paras:
            parts.append(f"<p>{html.escape(p)}</p>")
        if bullets:
            parts.append("<ul>" + "".join(f"<li>{html.escape(b)}</li>" for b in bullets) + "</ul>")
        sections.append("\n".join(parts))

    sec("Public reference summary", [
        desc or f"Reference dossier for {h1} in the Bisulfid sovereign sulfur terminology atlas.",
        "This page organizes atlas structure and relationships. "
        "Where factual claims require specialist sources, Bisulfid separates structure from unsupported assertion.",
    ])
    sec("Role in the Bisulfid Atlas", [dossier_role_text(route, cls, release_mode)], [
        f"Atlas lane: {lane} — {label}",
        f"Page type: {page_type}",
        f"Release mode: {release_mode}",
        "Part of the 14,000-route sovereign reference scaffold",
    ])
    sec("Related terms and boundaries", [
        f"This node helps distinguish how {h1} relates to nearby terminology, language, and context routes.",
        "Use linked nodes to navigate spelling boundaries, compound families, and parallel atlas layers.",
    ])
    sec("Context layers", [], [
        "Reference summary — atlas orientation for this node",
        "Technical context — terminology placement without unverified chemical assertions",
        "Language / terminology layer — multilingual and spelling-boundary awareness",
        "Research and journalism layer — structured context for citation discipline",
        "Institutional / industry context — sector framing without operational advice",
        "Student / general-reader layer — clear explanation without oversimplifying chemistry",
    ])
    sec("Who this page helps", [], who_this_helps(lane))
    sec("Source and claim posture", [
        "Cautious framing applies unless this route is explicitly tied to a verified source pack and approved claim.",
        "This dossier does not provide medical, safety, market, investment, or operational purchasing guidance.",
        "Terminology factual claims require verified source packs before they may appear on public pages.",
    ])
    return "\n".join(sections)


def audience_layers_html(route: dict, cls: dict) -> str:
    h1 = public_label(route)
    lane = cls.get("proposed_production_lane", "A")
    lang = route.get("language", "en").upper()
    return (
        f'<div class="atlas-layer atlas-layer--reference"><h3>Reference summary</h3>'
        f"<p>Atlas dossier for {html.escape(h1)}.</p></div>"
        f'<div class="atlas-layer atlas-layer--technical"><h3>Technical context</h3>'
        f"<p>Lane {html.escape(lane)} node — structure and terminology placement only.</p></div>"
        f'<div class="atlas-layer atlas-layer--language"><h3>Language layer</h3>'
        f"<p>Language: {html.escape(lang)}. Spelling-boundary awareness where relevant.</p></div>"
        f'<div class="atlas-layer atlas-layer--research"><h3>Research / journalism</h3>'
        f"<p>Structured reference for analysts and journalists; not a primary source citation.</p></div>"
        f'<div class="atlas-layer atlas-layer--context"><h3>Institutional / industry</h3>'
        f"<p>Context framing without operational, market, or investment advice.</p></div>"
        f'<div class="atlas-layer atlas-layer--student"><h3>Student / public</h3>'
        f"<p>Clear explanatory framing without childish simplification or unsupported claims.</p></div>"
    )


def build_breadcrumbs(route: dict) -> str:
    path = route.get("path", "/").strip("/")
    parts = path.split("/") if path else []
    items = ['<li><a href="/">Atlas</a></li>']
    for part in parts:
        label = sanitize_public_text(part.replace("-", " ").title())
        items.append(f"<li><span>{html.escape(label)}</span></li>")
    return "".join(items)


def build_internal_links_html(targets: list[str], routes_by_id: dict[str, dict]) -> str:
    items = []
    for tid in targets:
        r = routes_by_id.get(tid)
        if not r:
            continue
        path = r.get("path", "/").rstrip("/") or ""
        href = path + "/" if path else "/"
        label = public_label(r) if r.get("h1") or r.get("title") else tid
        items.append(f'<li><a href="{html.escape(href)}">{html.escape(label)}</a></li>')
    return "<ul>" + "".join(items) + "</ul>" if items else "<ul></ul>"


def substitute(template: str, ctx: dict[str, str]) -> str:
    out = template
    for key, val in ctx.items():
        out = out.replace("{{" + key + "}}", val)
    return out
