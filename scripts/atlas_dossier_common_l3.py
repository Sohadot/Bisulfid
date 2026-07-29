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
    "A": "Terminology Reference",
    "B": "Language Boundary Reference",
    "C": "Disambiguation Reference",
    "D": "Compound Reference",
    "E": "Materials Reference",
    "F": "Industrial Context",
    "G": "Biotechnology Context",
    "H": "Economic and Investment Context",
    "I": "Journalism and Research Context",
    "J": "Academic Reference",
    "K": "Institutional Reference",
    "L": "Student and Public Explanation",
    "HUB": "Public Reference Dossier",
}

LANE_SEMANTIC_CLASS = {
    "A": "atlas-lane-terminology",
    "B": "atlas-lane-language",
    "C": "atlas-lane-terminology",
    "D": "atlas-lane-compound",
    "E": "atlas-lane-material",
    "F": "atlas-lane-industrial",
    "G": "atlas-lane-biotech",
    "H": "atlas-lane-economic",
    "I": "atlas-lane-journalistic",
    "J": "atlas-lane-academic",
    "K": "atlas-lane-institutional",
    "L": "atlas-lane-student",
    "HUB": "atlas-lane-hub",
}

LANE_DOMAIN_CLASS = {
    "A": "domain-chemistry",
    "B": "domain-language",
    "C": "domain-chemistry",
    "D": "domain-chemistry",
    "E": "domain-materials",
    "F": "domain-industry",
    "G": "domain-biotech",
    "H": "domain-economics",
    "I": "domain-journalism",
    "J": "domain-academia",
    "K": "domain-institutional",
    "L": "domain-chemistry",
    "HUB": "domain-chemistry",
}

LANE_SLUG = {
    "A": "terminology",
    "B": "language",
    "C": "terminology",
    "D": "compound",
    "E": "material",
    "F": "industrial",
    "G": "biotech",
    "H": "economic",
    "I": "journalistic",
    "J": "academic",
    "K": "institutional",
    "L": "student",
    "HUB": "hub",
}

CSS_IMPORT_DEPENDENCIES = [
    "tokens/colors.css",
    "tokens/typography.css",
    "tokens/spacing.css",
    "tokens/motion.css",
    "tokens/depth.css",
    "tokens/governance.css",
    "components/governance-banner.css",
    "components/source-crystal.css",
    "components/term-card.css",
    "components/term-node.css",
    "components/language-depth.css",
    "components/relation-lattice.css",
    "public-surface.css",
    "atlas-semantic-interface.css",
]

SOVEREIGN_SHELL_MARKERS = (
    "bs-control-room",
    "bs-control-room__shell",
    "site-header",
    'id="main-content"',
    "site-footer",
)

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
    return PUBLIC_LANE_ROLES.get(lane, "Public Reference Dossier")


def atlas_lane_slug(lane: str) -> str:
    return LANE_SLUG.get(lane, "terminology")


def infer_audience_classes(path: str) -> list[str]:
    low = path.lower()
    classes: list[str] = []
    if any(x in low for x in ("/stu/", "aud-stu", "/child/", "child-stu")):
        classes.append("audience-student")
    if any(x in low for x in ("/ai/", "aud-ai", "air-ai")):
        classes.append("audience-ai")
    if "/acad/" in low or "/res/res" in low or "air-res" in low:
        classes.append("audience-research")
    if "/gov/" in low or "/inst/" in low:
        classes.append("audience-government")
    if "aud-anl" in low or "-anl-" in low:
        classes.append("audience-investor")
    return classes


def semantic_body_classes(lane: str, path: str) -> str:
    parts = [
        LANE_SEMANTIC_CLASS.get(lane, "atlas-lane-terminology"),
        LANE_DOMAIN_CLASS.get(lane, "domain-chemistry"),
    ]
    parts.extend(infer_audience_classes(path))
    return " ".join(parts)


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
            f"A governed {role.lower()} page for {h1}, within the {topic} "
            f"terminology family ({lang}). This page helps {audience} navigate the Bisulfid Atlas."
        )
    return (
        f"A governed {role.lower()} page for {h1} within the Bisulfid Atlas. "
        f"This page helps {audience} locate related terminology and context nodes."
    )


def public_category_label(role: str) -> str:
    return f"{role} · Source-Governed Reference"


def build_atlas_control_strip(lane: str, lang: str) -> str:
    role = public_lane_role(lane)
    return (
        '<div class="atlas-control-strip" aria-hidden="true">'
        '<span class="atlas-control-strip__brand">BISULFID · Chemical-Language Control Room</span>'
        f'<span class="atlas-control-strip__lane">{html.escape(role)}</span>'
        f'<span class="atlas-control-strip__lang">{html.escape(lang.upper())}</span>'
        "</div>"
    )


def _trunc_label(text: str, limit: int = 42) -> str:
    clean = sanitize_public_text(text)
    return clean if len(clean) <= limit else clean[: limit - 1] + "…"


def build_lane_interface_prelude(lane: str, route: dict, cls: dict) -> str:
    h1 = public_label(route)
    label = html.escape(_trunc_label(h1))
    path = route.get("path", "/").rstrip("/")
    lang = route.get("language", "en")

    if path in {"/methodology", "/sources"}:
        return (
            '<section class="atlas-lane-prelude atlas-lane-prelude--governance" aria-hidden="true">'
            '<p class="atlas-lane-prelude__signal">Governed source posture</p>'
            '<div class="bs-source-crystal atlas-source-crystal-prelude">'
            '<div class="bs-source-crystal__content">'
            '<p class="bs-source-crystal__label">Source-governed reference</p>'
            '<p class="bs-source-crystal__state">Cautious public framing without unsupported claims.</p>'
            "</div></div></section>"
        )
    if lane == "HUB":
        return (
            '<section class="atlas-lane-prelude atlas-lane-prelude--command" aria-hidden="true">'
            '<p class="atlas-lane-prelude__signal">Atlas command entry</p>'
            '<div class="bs-relation-lattice atlas-command-lattice">'
            '<div class="bs-relation-lattice__nodes">'
            '<span class="bs-term-node"><span class="bs-term-node__meta">Hub</span>'
            '<span class="bs-term-node__label">Atlas</span></span>'
            '<span class="bs-relation-lattice__edge"></span>'
            f'<span class="bs-term-node bs-term-node--center"><span class="bs-term-node__label">{label}</span></span>'
            "</div></div></section>"
        )
    if lane in {"A", "C"}:
        return (
            '<section class="atlas-lane-prelude atlas-lane-prelude--terminology" aria-hidden="true">'
            '<p class="atlas-lane-prelude__signal">Term-node lattice surface</p>'
            '<div class="bs-relation-lattice atlas-term-lattice">'
            '<div class="bs-relation-lattice__nodes">'
            f'<span class="bs-term-node bs-term-node--center"><span class="bs-term-node__meta">Term</span>'
            f'<span class="bs-term-node__label">{label}</span></span>'
            "</div></div></section>"
        )
    if lane == "B" or lang == "de":
        return (
            '<section class="atlas-lane-prelude atlas-lane-prelude--language" aria-hidden="true">'
            '<p class="atlas-lane-prelude__signal">DE/EN boundary logic</p>'
            '<div class="bs-missing-e-boundary-system">'
            '<p class="bs-missing-e-boundary-system__family">Missing-E boundary</p>'
            '<div class="bs-missing-e-boundary-system__row">'
            '<span class="bs-missing-e-boundary-system__name">BISULFIDE</span>'
            '<span class="bs-missing-e-boundary-system__boundary"></span>'
            '<span class="bs-missing-e-boundary-system__ghost">'
            '<span class="bs-missing-e-boundary-system__ghost-letter">E</span></span>'
            '<span class="bs-missing-e-boundary-system__boundary"></span>'
            '<span class="bs-missing-e-boundary-system__name">BISULFID</span>'
            "</div>"
            '<p class="bs-missing-e-boundary-system__caption">Language-boundary reference</p>'
            "</div>"
            '<div class="bs-language-depth">'
            '<span class="bs-language-depth__layer bs-language-depth__layer--de">DE</span>'
            '<span class="bs-language-depth__depth-indicator">boundary</span>'
            '<span class="bs-language-depth__layer bs-language-depth__layer--en">EN</span>'
            "</div></section>"
        )
    if lane == "D":
        return (
            '<section class="atlas-lane-prelude atlas-lane-prelude--compound" aria-hidden="true">'
            '<p class="atlas-lane-prelude__signal">Compound-family crystal map</p>'
            '<div class="atlas-compound-crystal" role="presentation">'
            '<span class="atlas-compound-crystal__cell atlas-compound-crystal__cell--parent"></span>'
            '<span class="atlas-compound-crystal__bond"></span>'
            '<span class="atlas-compound-crystal__cell atlas-compound-crystal__cell--child"></span>'
            '<span class="atlas-compound-crystal__cell atlas-compound-crystal__cell--child"></span>'
            "</div></section>"
        )
    if lane == "E":
        return (
            '<section class="atlas-lane-prelude atlas-lane-prelude--material" aria-hidden="true">'
            '<p class="atlas-lane-prelude__signal">Material / strata logic</p>'
            '<div class="atlas-material-strata" role="presentation">'
            '<span class="atlas-material-strata__layer atlas-material-strata__layer--ore"></span>'
            '<span class="atlas-material-strata__layer atlas-material-strata__layer--compound"></span>'
            '<span class="atlas-material-strata__layer atlas-material-strata__layer--context"></span>'
            "</div></section>"
        )
    if lane in {"F", "G", "H", "I"}:
        return (
            '<section class="atlas-lane-prelude atlas-lane-prelude--context" aria-hidden="true">'
            '<p class="atlas-lane-prelude__signal">Context-layer positioning</p>'
            '<div class="atlas-context-beacon" role="presentation">'
            f'<span class="atlas-context-beacon__core">{label}</span>'
            "</div></section>"
        )
    if lane in {"J", "K"}:
        return (
            '<section class="atlas-lane-prelude atlas-lane-prelude--governance" aria-hidden="true">'
            '<p class="atlas-lane-prelude__signal">Governed source posture</p>'
            '<div class="bs-source-crystal atlas-source-crystal-prelude">'
            '<div class="bs-source-crystal__content">'
            '<p class="bs-source-crystal__label">Source-governed reference</p>'
            '<p class="bs-source-crystal__state">Cautious public framing without unsupported claims.</p>'
            "</div></div></section>"
        )
    if lane == "L":
        return (
            '<section class="atlas-lane-prelude atlas-lane-prelude--audience" aria-hidden="true">'
            '<p class="atlas-lane-prelude__signal">Audience-layer positioning</p>'
            '<div class="atlas-audience-beacon" role="presentation">'
            '<span class="atlas-audience-beacon__ring"></span>'
            f'<span class="atlas-audience-beacon__core">{label}</span>'
            "</div></section>"
        )
    return (
        '<section class="atlas-lane-prelude atlas-lane-prelude--reference" aria-hidden="true">'
        '<p class="atlas-lane-prelude__signal">Reference control surface</p>'
        "</section>"
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


def build_role_panel_html(route: dict, cls: dict, release_mode: str) -> str:
    lane = cls.get("proposed_production_lane", "A")
    role = public_lane_role(lane)
    lang = route.get("language", "en").upper()
    return (
        f'<p class="atlas-role-panel__text">{html.escape(dossier_role_text(route, cls, release_mode))}</p>'
        f'<ul class="atlas-role-panel__meta">'
        f"<li>{html.escape(role)}</li>"
        f"<li>{html.escape(lang)}</li>"
        f"<li>{html.escape(parent_hub_label(route))}</li>"
        f"<li>Source-Governed Reference</li>"
        f"</ul>"
    )


def build_audience_panel_html(lane: str, path: str) -> str:
    items = who_this_helps(lane, path)
    return "<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in items) + "</ul>"


def build_dossier_body(route: dict, cls: dict, release_mode: str) -> str:
    h1 = public_label(route)
    topic = path_topic_hint(route.get("path", ""))
    sections: list[str] = []

    def sec(title: str, paras: list[str], bullets: list[str] | None = None) -> None:
        parts = [f"<h2>{html.escape(title)}</h2>"]
        for p in paras:
            parts.append(f"<p>{html.escape(p)}</p>")
        if bullets:
            parts.append("<ul>" + "".join(f"<li>{html.escape(b)}</li>" for b in bullets) + "</ul>")
        sections.append("\n".join(parts))

    sec("Term and topic boundary", [topic_boundary_text(route, cls)])
    sec("Related atlas nodes", [
        f"Use the links below to move from {h1} to neighbouring terminology, language, and hub routes.",
        "Internal navigation is designed for researchers, journalists, students, and institutional readers.",
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
        f"<p>{html.escape(role)} surface for {html.escape(h1)}.</p></div>"
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


def build_breadcrumbs(route: dict, valid_paths: set[str] | None = None) -> str:
    """Build breadcrumb list items for a route.

    Intermediate path segments are only rendered as links when they resolve to a
    real, generated page. When ``valid_paths`` is provided, an intermediate
    segment whose accumulated path is not in that set is emitted as plain text
    instead of an anchor, so crawlers never follow a link to a directory URL that
    has no ``index.html`` (which would return a 404). Passing ``None`` keeps the
    legacy behaviour of linking every intermediate segment.
    """
    path = route.get("path", "/").strip("/")
    parts = path.split("/") if path else []
    items = []
    acc = ""
    for i, part in enumerate(parts):
        acc = f"{acc}/{part}" if acc else part
        label = sanitize_public_text(part.replace("-", " ").title())
        if i == len(parts) - 1:
            items.append(f'<li><span aria-current="page">{html.escape(label)}</span></li>')
        elif valid_paths is not None and acc not in valid_paths:
            # Intermediate level has no generated page — render as text, not a
            # dead link, to avoid emitting a crawlable 404 target.
            items.append(f'<li><span>{html.escape(label)}</span></li>')
        else:
            href = f"/{acc}/"
            items.append(f'<li><a href="{html.escape(href)}">{html.escape(label)}</a></li>')
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
