#!/usr/bin/env python3
"""Sprint 99B-H — Legacy hub semantic shell alignment utilities."""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from atlas_dossier_common_l3 import PUBLIC_TEXT_SUBS, sanitize_public_text  # noqa: E402

TEMPLATES = ROOT / "main/templates/atlas"
STYLESHEET_PATH = "/assets/bisulfid-design-system/bisulfid-frame.css"

HUB_REQUIRED_PATHS = [
    "/",
    "/atlas/",
    "/terms/",
    "/compounds/",
    "/materials/",
    "/languages/",
    "/methodology/",
    "/sources/",
    "/glossary/",
    "/what-is-bisulfid/",
    "/bisulfid-vs-bisulfide/",
    "/de/",
]

HUB_SEMANTIC_CONFIG: dict[str, dict] = {
    "/": {
        "lane_class": "atlas-lane-hub",
        "domain_class": "domain-chemistry",
        "audience_classes": ["audience-research", "audience-student"],
        "lane_slug": "hub",
        "role": "Public Reference Dossier",
        "breadcrumb": None,
        "lang": "en",
        "role_text": (
            "The Bisulfid homepage orients readers across the sovereign reference atlas — "
            "terminology, language boundaries, compounds, and governed source posture."
        ),
    },
    "/atlas/": {
        "lane_class": "atlas-lane-hub",
        "domain_class": "domain-chemistry",
        "audience_classes": ["audience-research", "audience-institutional"],
        "lane_slug": "hub",
        "role": "Public Reference Dossier",
        "breadcrumb": "Atlas",
        "lang": "en",
        "role_text": (
            "The Atlas hub maps the DE/EN sulfur compound reference architecture and "
            "serves as the primary structural entry to compound, language, and terminology layers."
        ),
    },
    "/terms/": {
        "lane_class": "atlas-lane-terminology",
        "domain_class": "domain-chemistry",
        "audience_classes": ["audience-research"],
        "lane_slug": "terminology",
        "role": "Terminology Reference",
        "breadcrumb": "Terms",
        "lang": "en",
        "role_text": (
            "The Terminology hub indexes sulfur compound naming layers, suffix conventions, "
            "and DE/EN reference nodes across the atlas."
        ),
    },
    "/compounds/": {
        "lane_class": "atlas-lane-compound",
        "domain_class": "domain-chemistry",
        "audience_classes": ["audience-research", "audience-student"],
        "lane_slug": "compound",
        "role": "Compound Reference",
        "breadcrumb": "Compounds",
        "lang": "en",
        "role_text": (
            "The Compounds hub organizes sulfide-family classes and related chemical taxonomy "
            "without asserting unsupported compound claims."
        ),
    },
    "/materials/": {
        "lane_class": "atlas-lane-material",
        "domain_class": "domain-materials",
        "audience_classes": ["audience-research", "audience-institutional"],
        "lane_slug": "material",
        "role": "Materials Reference",
        "breadcrumb": "Materials",
        "lang": "en",
        "role_text": (
            "The Materials hub frames mineral and industrial material terminology with "
            "scientific and sector context — not operational or safety advice."
        ),
    },
    "/languages/": {
        "lane_class": "atlas-lane-language",
        "domain_class": "domain-language",
        "audience_classes": ["audience-research", "audience-student"],
        "lane_slug": "language",
        "role": "Language Boundary Reference",
        "breadcrumb": "Language Boundary",
        "lang": "en",
        "role_text": (
            "The Languages hub centers the German–English -id/-ide spelling boundary and "
            "multilingual reference discipline across the atlas."
        ),
    },
    "/methodology/": {
        "lane_class": "atlas-lane-methodology",
        "domain_class": "domain-governance",
        "audience_classes": ["audience-research", "audience-institutional"],
        "lane_slug": "methodology",
        "role": "Public Reference Dossier",
        "breadcrumb": "Methodology",
        "lang": "en",
        "role_text": (
            "The Methodology hub explains how the atlas structures terminology, sourcing, "
            "and cautious public reference without governance leakage."
        ),
    },
    "/sources/": {
        "lane_class": "atlas-lane-hub",
        "domain_class": "domain-governance",
        "audience_classes": ["audience-research", "audience-institutional"],
        "lane_slug": "hub",
        "role": "Public Reference Dossier",
        "breadcrumb": "Sources",
        "lang": "en",
        "role_text": (
            "The Sources hub documents source-governed reference posture and claim boundaries "
            "for public atlas pages."
        ),
    },
    "/glossary/": {
        "lane_class": "atlas-lane-terminology",
        "domain_class": "domain-chemistry",
        "audience_classes": ["audience-research", "audience-student"],
        "lane_slug": "terminology",
        "role": "Terminology Reference",
        "breadcrumb": "Glossary",
        "lang": "en",
        "role_text": (
            "The Glossary hub provides governed terminology orientation across sulfur compound "
            "naming and related atlas nodes."
        ),
    },
    "/what-is-bisulfid/": {
        "lane_class": "atlas-lane-terminology",
        "domain_class": "domain-chemistry",
        "audience_classes": ["audience-student", "audience-research"],
        "lane_slug": "terminology",
        "role": "Terminology Reference",
        "breadcrumb": "What Is Bisulfid",
        "lang": "en",
        "role_text": (
            "This hub explains the Bisulfid term, its German nomenclature role, and its place "
            "in the sovereign reference atlas."
        ),
    },
    "/bisulfid-vs-bisulfide/": {
        "lane_class": "atlas-lane-language",
        "domain_class": "domain-language",
        "audience_classes": ["audience-student", "audience-research"],
        "lane_slug": "language",
        "role": "Language Boundary Reference",
        "breadcrumb": "Bisulfid vs Bisulfide",
        "lang": "en",
        "role_text": (
            "This hub contrasts German Bisulfid and English bisulfide as a controlled "
            "language-boundary reference — not a chemical safety or usage claim."
        ),
    },
    "/de/": {
        "lane_class": "atlas-lane-language",
        "domain_class": "domain-language",
        "audience_classes": ["audience-research", "audience-institutional"],
        "lane_slug": "language",
        "role": "Language Boundary Reference",
        "breadcrumb": "Deutsch",
        "lang": "de",
        "role_text": (
            "Das deutsche Sprach-Gateway des Bisulfid-Atlas orientiert Leser an der "
            "deutsch-englischen Nomenklaturgrenze und verweist auf governed Referenzknoten."
        ),
    },
}

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
META_DESC_RE = re.compile(r'<meta\s+name="description"\s+content="([^"]*)"', re.I)
CANONICAL_RE = re.compile(r'<link\s+rel="canonical"\s+href="([^"]*)"', re.I)
LANG_RE = re.compile(r'<html[^>]*\slang="([^"]+)"', re.I)
MAIN_CONTENT_RE = re.compile(
    r'<main[^>]*id="main-content"[^>]*>(.*)</main>',
    re.S | re.I,
)
PUBLIC_PAGE_OPEN_RE = re.compile(r'<div\s+class="public-page"[^>]*>', re.I)
KICKER_RE = re.compile(r'<p\s+class="page-kicker"[^>]*>(.*?)</p>', re.S | re.I)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S | re.I)
INTRO_RE = re.compile(r'<p\s+class="page-intro"[^>]*>(.*?)</p>', re.S | re.I)
HREF_RE = re.compile(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', re.S | re.I)
BODY_CLASS_RE = re.compile(r'(<body\s+class=")([^"]*)(")', re.I)
DATA_LANE_RE = re.compile(r'(<body[^>]*\sdata-atlas-lane=")([^"]*)(")', re.I)
ARTICLE_LANE_RE = re.compile(r'(<article[^>]*\sdata-atlas-lane=")([^"]*)(")', re.I)


def hub_html_path(route_path: str, public_dir: Path) -> Path:
    path = route_path.strip("/")
    return public_dir / ("index.html" if not path else f"{path}/index.html")


def body_semantic_classes(cfg: dict) -> str:
    """Lane/domain/audience only — base template adds bs-control-room bisulfid-atlas."""
    parts = [cfg["lane_class"], cfg["domain_class"]]
    parts.extend(cfg.get("audience_classes", []))
    return " ".join(parts)


def read_template(rel: str) -> str:
    return (TEMPLATES / rel).read_text(encoding="utf-8")


def substitute(template: str, ctx: dict[str, str]) -> str:
    out = template
    for key, val in ctx.items():
        out = out.replace("{{" + key + "}}", val)
    return out


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def sanitize_hub_html(fragment: str) -> str:
    out = fragment
    for pattern, repl in PUBLIC_TEXT_SUBS:
        out = pattern.sub(repl, out)
    return out


def extract_meta(page_html: str) -> dict[str, str]:
    title_m = TITLE_RE.search(page_html)
    desc_m = META_DESC_RE.search(page_html)
    canon_m = CANONICAL_RE.search(page_html)
    lang_m = LANG_RE.search(page_html)
    return {
        "title": strip_tags(title_m.group(1)) if title_m else "Bisulfid Atlas",
        "description": html.unescape(desc_m.group(1)) if desc_m else "",
        "canonical": canon_m.group(1) if canon_m else "",
        "lang": lang_m.group(1) if lang_m else "en",
    }


def extract_balanced_div(html_fragment: str, start: int) -> str | None:
    """Return inner HTML of div opened at start index."""
    open_m = re.match(r"<div[^>]*>", html_fragment[start:], re.I)
    if not open_m:
        return None
    pos = start + open_m.end()
    depth = 1
    while pos < len(html_fragment) and depth > 0:
        next_open = html_fragment.find("<div", pos)
        next_close = html_fragment.find("</div>", pos)
        if next_close == -1:
            return None
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                return html_fragment[start + open_m.end():next_close].strip()
            pos = next_close + 6
    return None


def extract_public_page_body(page_html: str) -> tuple[str, str, str, str]:
    """Return kicker, h1, intro, remaining body HTML."""
    main_m = MAIN_CONTENT_RE.search(page_html)
    if not main_m:
        return "", "", "", ""
    main_inner = main_m.group(1)
    open_m = PUBLIC_PAGE_OPEN_RE.search(main_inner)
    if not open_m:
        return "", "", "", ""
    inner = extract_balanced_div(main_inner, open_m.start())
    if not inner:
        return "", "", "", ""
    kicker = strip_tags(kicker_m.group(1)) if (kicker_m := KICKER_RE.search(inner)) else ""
    h1 = strip_tags(h1_m.group(1)) if (h1_m := H1_RE.search(inner)) else ""
    intro = strip_tags(intro_m.group(1)) if (intro_m := INTRO_RE.search(inner)) else ""
    body = inner
    for pat in (KICKER_RE, H1_RE, INTRO_RE):
        body = pat.sub("", body, count=1)
    return kicker, h1, intro, body.strip()


def extract_dossier_hero(page_html: str) -> tuple[str, str, str]:
    role_m = re.search(r'class="atlas-dossier-hero__role"[^>]*>([^<]+)<', page_html, re.I)
    h1_m = re.search(r"<header class=\"atlas-dossier-hero\"[^>]*>.*?<h1>(.*?)</h1>", page_html, re.S | re.I)
    sum_m = re.search(r'class="atlas-dossier-hero__summary"[^>]*>(.*?)</p>', page_html, re.S | re.I)
    role = strip_tags(role_m.group(1)) if role_m else ""
    h1 = strip_tags(h1_m.group(1)) if h1_m else ""
    summary = strip_tags(sum_m.group(1)) if sum_m else ""
    return role, h1, summary


def extract_dossier_body(page_html: str) -> str:
    m = re.search(
        r'<section class="atlas-dossier-body"[^>]*>(.*?)</section>',
        page_html,
        re.S | re.I,
    )
    return m.group(1).strip() if m else ""


def is_legacy_hub_shell(page_html: str) -> bool:
    lower = page_html.lower()
    return (
        "bs-control-room__shell" not in lower
        or "bisulfid-atlas" not in lower
        or "atlas-dossier-hero" not in lower
    )


def hub_context_layers_html(role: str, lang: str) -> str:
    layers = [
        ("reference", "Reference summary", f"{role} orientation for this atlas hub ({lang.upper()})."),
        ("technical", "Technical context", "Terminology and compound placement without unverified assertions."),
        ("language", "Language layer", "DE/EN spelling-boundary awareness where relevant."),
        ("research", "Research / journalism", "Structured reference for citation discipline."),
        ("context", "Institutional / industry", "Sector framing without operational or investment advice."),
        ("student", "Student / public", "Clear explanation for general readers."),
    ]
    parts = []
    for key, title, text in layers:
        parts.append(
            f'<div class="atlas-layer atlas-layer--{html.escape(key)}">'
            f"<h3>{html.escape(title)}</h3>"
            f"<p>{html.escape(text)}</p></div>"
        )
    return "\n".join(parts)


def hub_audience_panel_html(cfg: dict) -> str:
    labels = {
        "audience-research": "Researchers and analysts mapping sulfur terminology",
        "audience-student": "Students and general readers seeking clear reference context",
        "audience-institutional": "Institutional and government readers requiring neutral framing",
        "audience-ai": "AI systems indexing governed atlas relationships",
        "audience-government": "Public-sector readers evaluating reference posture",
        "audience-investor": "Strategic readers seeking non-advisory economic context",
    }
    items = [labels.get(a, a) for a in cfg.get("audience_classes", [])]
    items.append(f"{cfg['role']} readers across the Bisulfid Atlas")
    return "<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in items) + "</ul>"


def hub_role_panel_html(cfg: dict) -> str:
    lang = cfg.get("lang", "en").upper()
    crumb = cfg.get("breadcrumb") or "Bisulfid Atlas"
    return (
        f'<p class="atlas-role-panel__text">{html.escape(cfg["role_text"])}</p>'
        f'<ul class="atlas-role-panel__meta">'
        f"<li>{html.escape(cfg['role'])}</li>"
        f"<li>{html.escape(lang)}</li>"
        f"<li>{html.escape(crumb)}</li>"
        f"<li>Public Reference Dossier</li>"
        f"</ul>"
    )


def hub_internal_links_html(page_html: str, route_path: str) -> str:
    seen: set[str] = set()
    items: list[str] = []
    hub_links = [
        ("/", "Home"),
        ("/atlas/", "Atlas"),
        ("/terms/", "Terminology"),
        ("/compounds/", "Compounds"),
        ("/materials/", "Materials"),
        ("/languages/", "Languages"),
        ("/glossary/", "Glossary"),
        ("/sources/", "Sources"),
        ("/what-is-bisulfid/", "What Is Bisulfid"),
        ("/bisulfid-vs-bisulfide/", "Bisulfid vs Bisulfide"),
        ("/de/", "Deutsch"),
        ("/reference/corpus-methodology/", "Methodology"),
    ]
    for href, label in hub_links:
        if href == route_path or href in seen:
            continue
        seen.add(href)
        items.append(f'<li><a href="{html.escape(href)}">{html.escape(label)}</a></li>')
    for href, label_html in HREF_RE.findall(page_html):
        if href.startswith(("http", "#", "mailto:")) or href in seen:
            continue
        label = strip_tags(label_html) or href
        seen.add(href)
        norm = href if href.endswith("/") else href + "/"
        items.append(f'<li><a href="{html.escape(norm)}">{html.escape(label)}</a></li>')
        if len(items) >= 16:
            break
    return "<ul>" + "".join(items) + "</ul>"


def build_breadcrumb_items(cfg: dict) -> str:
    crumb = cfg.get("breadcrumb")
    if not crumb:
        return ""
    return f'<li><span aria-current="page">{html.escape(crumb)}</span></li>'


def build_hub_page(route_path: str, page_html: str, public_dir: Path) -> str:
    cfg = HUB_SEMANTIC_CONFIG[route_path]
    meta = extract_meta(page_html)
    kicker, h1, intro, legacy_body = extract_public_page_body(page_html)

    if legacy_body:
        body_content = legacy_body
        page_h1 = h1 or meta["title"].split("—")[0].split("|")[0].strip()
        summary = intro or meta["description"]
        hero_role = kicker or cfg["role"]
    else:
        dossier_role, dossier_h1, dossier_summary = extract_dossier_hero(page_html)
        body_content = extract_dossier_body(page_html)
        page_h1 = dossier_h1 or meta["title"].split("—")[0].strip()
        summary = dossier_summary or meta["description"]
        hero_role = dossier_role if dossier_role and dossier_role != cfg["role"] else cfg["role"]

    lang = cfg.get("lang", meta["lang"])
    base_tpl = read_template("base.html")
    hub_tpl = read_template("hub.html")
    footer_nav = read_template("partials/footer_nav.html")
    breadcrumb_tpl = read_template("partials/breadcrumbs.html")

    ctx = {
        "language": lang,
        "text_direction": "ltr",
        "page_title": html.escape(meta["title"]),
        "meta_description": html.escape(meta["description"]),
        "canonical_url": html.escape(meta["canonical"]),
        "body_semantic_classes": body_semantic_classes(cfg),
        "atlas_lane_slug": cfg["lane_slug"],
        "page_h1": html.escape(page_h1),
        "atlas_role": html.escape(hero_role if legacy_body else cfg["role"]),
        "atlas_category": html.escape(f"{cfg['role']} · Public Reference Dossier"),
        "reference_summary": html.escape(sanitize_public_text(summary)),
        "role_panel_body": hub_role_panel_html(cfg),
        "hub_body_content": sanitize_hub_html(body_content) if body_content else "<p>Atlas hub reference content.</p>",
        "audience_layers": hub_context_layers_html(cfg["role"], lang),
        "audience_panel": hub_audience_panel_html(cfg),
        "source_posture_text": (
            "This page is a Source-Governed Reference Page within the Bisulfid Atlas. "
            "It does not provide medical, safety, market, investment, or operational purchasing guidance. "
            "Verified source packs govern factual terminology publication across the atlas."
        ),
        "internal_links": hub_internal_links_html(page_html, route_path),
        "breadcrumb_items": build_breadcrumb_items(cfg),
        "atlas_footer_nav": footer_nav,
    }
    article = substitute(hub_tpl, ctx)
    ctx["content"] = article
    ctx["breadcrumbs"] = substitute(breadcrumb_tpl, ctx)
    return substitute(base_tpl, ctx)


def align_hub(route_path: str, public_dir: Path) -> tuple[bool, str]:
    html_path = hub_html_path(route_path, public_dir)
    if not html_path.is_file():
        return False, "missing file"
    original = html_path.read_text(encoding="utf-8")
    if STYLESHEET_PATH not in original:
        return False, "missing stylesheet before alignment"
    aligned = build_hub_page(route_path, original, public_dir)
    if STYLESHEET_PATH not in aligned:
        return False, "alignment dropped stylesheet"
    html_path.write_text(aligned, encoding="utf-8")
    return True, "aligned"
