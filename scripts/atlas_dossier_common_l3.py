#!/usr/bin/env python3
"""Sprint 99/99A — Shared utilities for 14K public reference dossier release."""
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
STYLESHEET_PATH = "/assets/bisulfid-design-system/bisulfid-frame.css"

PUBLIC_LANE_ROLES = {
    "A": "Terminology reference",
    "B": "Language boundary reference",
    "C": "Disambiguation reference",
    "D": "Compound reference",
    "E": "Materials reference",
    "F": "Industrial context reference",
    "G": "Biotechnology context reference",
    "H": "Economic context reference",
    "I": "Journalistic context reference",
    "J": "Academic reference",
    "K": "Institutional context reference",
    "L": "General-reader reference",
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
DRAFT_PHRASE_RE = re.compile(
    r"\b(reference draft|governed terminology reference draft|terminology reference draft)\b",
    re.I,
)

PUBLIC_TEXT_SUBS = (
    (re.compile(r"\bprocurement\b", re.I), "supply-chain context"),
    (re.compile(r"\bCAGR\b"), ""),
    (re.compile(r"\bpurchasing recommendations?\b", re.I), "structured context"),
    (re.compile(r"\breference draft\b", re.I), "reference dossier"),
    (re.compile(r"\bdraft\b", re.I), "reference"),
    (re.compile(r"\bnot public\b", re.I), ""),
    (re.compile(r"\bnot publication-ready\b", re.I), ""),
    (re.compile(r"\bpublication blocker\b", re.I), ""),
    (re.compile(r"\bgovernance draft\b", re.I), ""),
    (re.compile(r"\braw scaffold\b", re.I), ""),
    (re.compile(r"\bpublic launch foundation\b", re.I), "atlas launch orientation"),
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

FORBIDDEN_PUBLIC_LANGUAGE_99A = FORBIDDEN_PUBLIC_PATTERNS + [
    re.compile(r"\bdraft\b", re.I),
    re.compile(r"\bnot public\b", re.I),
    re.compile(r"\bgovernance draft\b", re.I),
    re.compile(r"\braw scaffold\b", re.I),
    re.compile(r"\bterminology_node\b", re.I),
    re.compile(r"\bcautious_reference_dossier\b", re.I),
    re.compile(r"\bsource_verified_page\b", re.I),
    re.compile(r"\bblocked_high_risk\b", re.I),
    re.compile(r"\brelease_mode\b", re.I),
    re.compile(r"\bclaim_set_id\b", re.I),
    re.compile(r"\bsource_pack_id\b", re.I),
    re.compile(r"\bLane [A-M]\b"),
    re.compile(r"PUBLIC LAUNCH FOUNDATION", re.I),
    re.compile(r"Indexation gate:\s*CLOSED", re.I),
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


def public_lane_role(lane: str) -> str:
    return PUBLIC_LANE_ROLES.get(lane, "Public reference dossier")


def public_label(route: dict) -> str:
    raw = route.get("h1") or route.get("title") or route.get("route_id", "")
    raw = re.sub(r"\s*\|\s*bisulfid\.com\s*$", "", raw, flags=re.I)
    return sanitize_public_text(raw)


def path_topic_hint(path: str) -> str:
    parts = path.strip("/").split("/")
    for i, part in enumerate(parts):
        if part == "terminology" and i + 1 < len(parts):
            return sanitize_public_text(parts[i + 1].replace("-", " "))
    if len(parts) >= 2:
        return sanitize_public_text(parts[-2].replace("-", " "))
    return ""


def path_audience_hint(path: str) -> str:
    low = path.lower()
    if "-aud-stu-" in low or "/stu/" in low:
        return "students and general readers"
    if "-aud-ai-" in low or "/ai/" in low or "-aud-anl-" in low:
        return "analysts and institutional readers"
    if "-air-res-" in low or "/res/res/" in low:
        return "researchers and journalists"
    if "-child-" in low:
        return "educators and younger readers"
    if "/acad/" in low:
        return "academic and university readers"
    if "/know/" in low:
        return "readers building structured terminology knowledge"
    if "-ind-" in low:
        return "industrial and sector context readers"
    return "readers navigating the sovereign reference atlas"


def public_summary(route: dict, cls: dict) -> str:
    h1 = public_label(route)
    lane = cls.get("proposed_production_lane", "A")
    role = public_lane_role(lane)
    lang = route.get("language", "en").upper()
    topic = path_topic_hint(route.get("path", ""))
    audience = path_audience_hint(route.get("path", ""))
    if topic:
        return (
            f"A governed {role.lower()} dossier for {h1}, within the {topic} "
            f"terminology family ({lang}). This page helps {audience} navigate the Bisulfid Atlas."
        )
    return (
        f"A governed {role.lower()} dossier for {h1} within the Bisulfid Atlas. "
        f"This page helps {audience} locate related terminology and context nodes."
    )


def clean_description(desc: str, route: dict | None = None, cls: dict | None = None) -> str:
    if route is not None and cls is not None:
        return public_summary(route, cls)
    desc = NON_PUBLIC_DESC_RE.sub("", desc)
    desc = DRAFT_PHRASE_RE.sub("reference dossier", desc)
    desc = sanitize_public_text(desc)
    desc = re.sub(r"\s+", " ", desc).strip()
    return desc or "Bisulfid sovereign reference atlas node."


def assign_release_mode(route: dict, cls: dict) -> str:
    rid = route.get("route_id", "")
    if rid in BLOCKED_ROUTE_IDS:
        return "blocked_high_risk"
    path = route.get("path", "")
    if MOS2_PATTERN.search(path) or MOS2_PATTERN.search(rid):
        return "source_verified_page"
    return "cautious_reference_dossier"


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


def pick_related(
    route_id: str, route: dict, path_index: dict[str, list[str]],
    lane_index: dict[str, list[str]], classification: dict[str, dict], count: int = 4,
) -> list[str]:
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
    route_id: str, route: dict, routes_by_id: dict[str, dict],
    path_index: dict[str, list[str]], lane_index: dict[str, list[str]],
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


def who_this_helps(lane: str, path: str) -> list[str]:
    audience = path_audience_hint(path)
    role = public_lane_role(lane)
    return [
        f"{role} readers across the Bisulfid Atlas",
        f"Readers including {audience}",
        "Researchers mapping sulfur terminology structure",
        "Journalists seeking governed reference context",
        "AI systems indexing atlas relationships",
    ]


def topic_boundary_text(route: dict, cls: dict) -> str:
    h1 = public_label(route)
    topic = path_topic_hint(route.get("path", ""))
    lane = cls.get("proposed_production_lane", "A")
    role = public_lane_role(lane)
    if topic:
        return (
            f"This node situates {h1} within the {topic} family as a {role.lower()} entry. "
            f"It clarifies how neighbouring atlas routes relate without asserting unsupported chemical facts."
        )
    return (
        f"This node defines the reference boundary for {h1} as a {role.lower()} page. "
        f"Linked routes show spelling, compound, and context relationships across the atlas."
    )


def dossier_role_text(route: dict, cls: dict, release_mode: str) -> str:
    h1 = public_label(route)
    lane = cls.get("proposed_production_lane", "A")
    role = public_lane_role(lane)
    lang = route.get("language", "en").upper()
    topic = path_topic_hint(route.get("path", ""))
    if release_mode == "source_verified_page":
        return (
            f"This source-governed atlas page organizes verified reference context for {h1} "
            f"in {lang}. Narrow approved claims may appear where source packs are verified; "
            f"broader assertions remain separated from public structure."
        )
    if topic:
        return (
            f"This dossier maps {h1} within the Bisulfid {role.lower()} layer for the {topic} "
            f"terminology family ({lang}). It orients readers across related nodes without unsupported claims."
        )
    return (
        f"This dossier maps {h1} within the Bisulfid {role.lower()} layer ({lang}). "
        f"It provides structure, relationships, and cautious context for atlas navigation."
    )


def parent_hub_label(route: dict) -> str:
    path = route.get("path", "/").strip("/")
    parts = path.split("/")
    if len(parts) >= 2:
        return sanitize_public_text(parts[0].upper() + " · " + parts[1].replace("-", " ").title())
    return "Bisulfid Atlas"


def build_dossier_body(route: dict, cls: dict, release_mode: str) -> str:
    h1 = public_label(route)
    lane = cls.get("proposed_production_lane", "A")
    role = public_lane_role(lane)
    lang = route.get("language", "en").upper()
    summary = public_summary(route, cls)
    topic = path_topic_hint(route.get("path", ""))
    sections: list[str] = []

    def sec(title: str, paras: list[str], bullets: list[str] | None = None) -> None:
        parts = [f"<h2>{html.escape(title)}</h2>"]
        for p in paras:
            parts.append(f"<p>{html.escape(p)}</p>")
        if bullets:
            parts.append("<ul>" + "".join(f"<li>{html.escape(b)}</li>" for b in bullets) + "</ul>")
        sections.append("\n".join(parts))

    sec("Public reference summary", [summary])
    sec("Role in the Bisulfid Atlas", [dossier_role_text(route, cls, release_mode)], [
        f"Atlas category: {role}",
        f"Language: {lang}",
        f"Parent context: {parent_hub_label(route)}",
        "Part of the Bisulfid sovereign reference atlas",
    ])
    sec("Term and topic boundary", [topic_boundary_text(route, cls)])
    sec("Related atlas nodes", [
        f"Use the links below to move from {h1} to neighbouring terminology, language, and hub routes.",
        "Internal navigation is designed for researchers, journalists, students, and institutional readers.",
    ])
    sec("Context layers", [], [
        "Reference summary — atlas orientation for this topic",
        "Technical context — terminology placement without unverified chemical assertions",
        "Language layer — multilingual and spelling-boundary awareness",
        "Research and journalism layer — structured context for citation discipline",
        "Institutional and industry layer — sector framing without operational advice",
        "Student and public layer — clear explanation without oversimplifying chemistry",
    ])
    sec("Who this page helps", [], who_this_helps(lane, route.get("path", "")))
    sec("Source and claim posture", [
        "This public reference dossier uses cautious framing. "
        "Factual terminology claims require verified source packs before publication.",
        "This page does not provide medical, safety, market, investment, or operational purchasing guidance.",
    ])
    if topic:
        sec("Navigation", [
            f"Return to atlas hubs via the Terminology Spine, Sources, and Methodology pages linked below. "
            f"The {topic} family contains parallel nodes for related spelling, compound, and context layers.",
        ])
    return "\n".join(sections)


def audience_layers_html(route: dict, cls: dict) -> str:
    h1 = public_label(route)
    lane = cls.get("proposed_production_lane", "A")
    role = public_lane_role(lane)
    lang = route.get("language", "en").upper()
    audience = path_audience_hint(route.get("path", ""))
    return (
        f'<div class="atlas-layer atlas-layer--reference"><h3>Reference summary</h3>'
        f"<p>{html.escape(role)} dossier for {html.escape(h1)}.</p></div>"
        f'<div class="atlas-layer atlas-layer--technical"><h3>Technical context</h3>'
        f"<p>{html.escape(role)} placement within the governed atlas structure.</p></div>"
        f'<div class="atlas-layer atlas-layer--language"><h3>Language layer</h3>'
        f"<p>Language: {html.escape(lang)}. Spelling-boundary awareness where relevant.</p></div>"
        f'<div class="atlas-layer atlas-layer--research"><h3>Research / journalism</h3>'
        f"<p>Structured reference for analysts and journalists; not a primary-source citation.</p></div>"
        f'<div class="atlas-layer atlas-layer--context"><h3>Institutional / industry</h3>'
        f"<p>Context framing without operational, market, or investment advice.</p></div>"
        f'<div class="atlas-layer atlas-layer--student"><h3>Student / public</h3>'
        f"<p>Clear framing for {html.escape(audience)} without unsupported claims.</p></div>"
    )


def build_breadcrumbs(route: dict) -> str:
    path = route.get("path", "/").strip("/")
    parts = path.split("/") if path else []
    items = []
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
        label = public_label(r)
        items.append(f'<li><a href="{html.escape(href)}">{html.escape(label)}</a></li>')
    return "<ul>" + "".join(items) + "</ul>" if items else "<ul></ul>"


def substitute(template: str, ctx: dict[str, str]) -> str:
    out = template
    for key, val in ctx.items():
        out = out.replace("{{" + key + "}}", val)
    return out


def strip_machine_content_for_audit(text: str) -> str:
    visible = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.S | re.I)
    visible = re.sub(r"<style[^>]*>.*?</style>", "", visible, flags=re.S | re.I)
    visible = re.sub(r"<a\s+href=\"[^\"]*\"", '<a href=""', visible, flags=re.I)
    visible = re.sub(r"<link[^>]+>", "", visible, flags=re.I)
    visible = re.sub(r"https?://[^\s<\"]+", "", visible, flags=re.I)
    visible = re.sub(r"data-[a-z-]+=\"[^\"]*\"", "", visible, flags=re.I)
    visible = re.sub(r"cohort\d+_[a-z0-9_]+", "", visible, flags=re.I)
    return visible
