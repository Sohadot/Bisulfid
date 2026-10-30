#!/usr/bin/env python3
"""render_institutional_preview.py — non-public preview of an institutional page (Recovery-02).

Renders main/data/reference_production/render_specs/INST-*.json into
main/data/reference_production/previews/<route path>/index.html (outside site/public; robots noindex).
Institutional pages assert no chemistry/terminology facts; numbers about the site's own governed
content come from {{GOV:key}} placeholders computed here from the registries, never typed in. Every
link must resolve to a public page or to a reference preview. --check verifies the output is current.
"""

import argparse
import glob
import html
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
SITE = "https://bisulfid.com"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class RenderError(Exception):
    pass


SPEC_DIR = os.path.join(DATA, "reference_production", "render_specs")


def gov_values():
    import render_ko_reference as rk

    def ko(name):
        return rk.build(json.load(open(os.path.join(SPEC_DIR, name), encoding="utf-8")))
    mos2, term = ko("KO-MOS2-SCIENTIFIC-001.json"), ko("KO-BISULFID-TERMINOLOGY-001.json")
    claims = json.load(open(os.path.join(DATA, "claims", "terminology_claims.json"), encoding="utf-8"))["claims"]
    pending = [c for c in claims if c["status"] == "pending_review"
               and {"bisulfid", "bisulfide"} & set(c.get("related_terms") or [])]
    return {"mos2_admitted_evidence": str(len(mos2["provenance"])), "bisulfid_claims_pending": str(len(pending)),
            "term_evidence": str(len(term["provenance"])), "term_claims_approved": str(len(term["ko"]["claim_ids"])),
            "knowledge_objects": str(len(json.load(open(os.path.join(DATA, "knowledge_objects", "knowledge_object_registry.json")))["knowledge_objects"]))}


def alternates(spec):
    """Reciprocal hreflang: emitted only if every declared alternate has an INST spec of the same
    institutional function that declares exactly the same set (no one-sided or guessed pairs)."""
    alt = spec.get("alternates")
    if not alt:
        return []
    specs = [json.load(open(f, encoding="utf-8")) for f in glob.glob(os.path.join(SPEC_DIR, "INST-*.json"))]
    for lang, path in alt.items():
        if lang == "x-default":
            continue
        other = next((x for x in specs if x.get("path") == path and x.get("language") == lang), None)
        if not other or other.get("institutional_function") != spec["institutional_function"] or other.get("alternates") != alt:
            raise RenderError(f"hreflang {lang} -> {path} is not reciprocated by an equivalent INST spec")
    return sorted(alt.items())


def resolve(text, gov):
    def sub(m):
        if m.group(1) not in gov:
            raise RenderError(f"unknown governed value {m.group(1)}")
        return gov[m.group(1)]
    out = re.sub(r"\{\{GOV:([a-z0-9_]+)\}\}", sub, text)
    if "{{" in out:
        raise RenderError("unresolved placeholder")
    return out


def link_ok(path):
    pub = os.path.join(ROOT, "site", "public", path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "site", "public", "index.html")
    return os.path.exists(pub)


RELEASE_DIR = os.path.join(DATA, "release", "staged")


def build(spec, release=False):
    """Preview (noindex, outside the site) or RELEASE candidate: same body, directives from the
    publication authority, the site footer, and a list of links whose destinations are governed
    references not yet public (publication dependencies)."""
    gov = gov_values()
    e = html.escape
    secs = []
    for s in spec["sections"]:
        for l in s["links"]:
            if not link_ok(l["path"]):
                raise RenderError(f"link {l['path']} does not resolve")
        paras = "".join(f"<p>{e(resolve(p, gov))}</p>" for p in s["paragraphs"])
        links = ("<ul class=\"home-links\">" + "".join(f"<li><a href=\"{e(l['path'])}\">{e(l['label'])}</a></li>" for l in s["links"]) + "</ul>") if s["links"] else ""
        secs.append(f"<section class=\"home-section\">\n<h2>{e(s['heading'])}</h2>\n{paras}\n{links}\n</section>")
    seo = spec["seo"]
    ld = dict({"@context": "https://schema.org"}, **seo["json_ld"])
    path = spec["path"]
    nav = "".join(f"<li><a href=\"{e(n['path'])}\"{' class=\"site-nav-brand\"' if i == 0 else ''}>{e(n['label'])}</a></li>"
                  for i, n in enumerate(spec["nav"]))
    for n in spec["nav"]:
        if not link_ok(n["path"]):
            raise RenderError(f"nav link {n['path']} does not resolve")
    hl = "".join(f"\n  <link rel=\"alternate\" hreflang=\"{e(lang)}\" href=\"{SITE}{e(p)}\">" for lang, p in alternates(spec))
    robots, canonical, mode, deps = "noindex, nofollow", f"{SITE}{path}", "preview", []
    footer = "<footer class=\"site-footer\" role=\"contentinfo\"><div class=\"site-footer__inner\"><p class=\"footer-identity\">BISULFID</p></div></footer>"
    if release:
        sys.path.insert(0, os.path.join(ROOT, "scripts", "publication"))
        import publication_authority as pa
        auth = pa.Authority()
        robots, canonical = auth.render_directives(path)
        mode = "release"
        for l in [x for sec in spec["sections"] for x in sec["links"]] + spec["nav"]:
            cc, basis = auth.contract_c(l["path"])
            if cc and cc != ("public_indexable", "index_approved") and l["path"] not in deps:
                deps.append(l["path"])
        f = spec["footer"]
        fnav = "".join(f"<a href=\"{e(x['path'])}\">{e(x['label'])}</a>" for x in f["nav"])
        for x in f["nav"]:
            if not link_ok(x["path"]):
                raise RenderError(f"footer link {x['path']} does not resolve")
        footer = (f"<footer class=\"site-footer\" role=\"contentinfo\"><div class=\"site-footer__inner\">"
                  f"<nav class=\"footer-nav\" aria-label=\"{e(spec.get('nav_label', 'Site navigation'))} (footer)\">{fnav}</nav>"
                  f"<p class=\"footer-identity\">{e(f['identity'])}</p><p class=\"footer-copyright\">&copy; 2026 bisulfid.com</p></div></footer>")
    page = f"""<!DOCTYPE html>
<html lang="{e(spec['language'])}" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{e(seo['title'])}</title>
  <meta name="description" content="{e(seo['description'])}">
  <meta name="robots" content="{e(robots)}">
  <link rel="canonical" href="{e(canonical)}">{hl}
  <link rel="stylesheet" href="/assets/bisulfid-design-system/bisulfid-frame.css">
  <script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body class="bs-control-room bisulfid-atlas" data-institutional-{mode}="{e(spec['spec_id'])}@{e(spec['version'])}">
  <div class="bs-control-room__shell">
    <header class="site-header atlas-header" role="banner">
      <nav aria-label="{e(spec.get('nav_label', 'Site navigation'))}"><ul class="site-nav-list">{nav}</ul></nav>
    </header>
    <main id="main-content" role="main">
      <article class="home public-page" lang="{e(spec['language'])}">
        <header class="home__hero"><h1>{e(spec['h1'])}</h1><p class="page-intro">{e(spec['lead'])}</p></header>
{chr(10).join(secs)}
      </article>
    </main>
    {footer}
  </div>
</body>
</html>
"""
    return (path, page, deps) if release else (path, page)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", help="one INST spec (default: every INST-*.json)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    paths = [a.spec] if a.spec else sorted(glob.glob(os.path.join(SPEC_DIR, "INST-*.json")))
    return max(run(json.load(open(p, encoding="utf-8")), a) for p in paths)


def run(spec, a):
    try:
        path, page = build(spec)
        _, rel, deps = build(spec, release=True)
    except (RenderError, PermissionError) as exc:
        print(f"RENDER REFUSED: {exc}")
        return 1
    slug = path.strip("/") or "home"
    manifest = json.dumps({"page": path, "spec": f"{spec['spec_id']}@{spec['version']}", "kind": "institutional",
                           "publication_dependencies": deps,
                           "dependency_rule": "publish only after every listed governed reference is itself public "
                                              "(otherwise the page would point readers at legacy pages it describes as governed)"},
                          indent=1) + "\n"
    outs = {os.path.join(DATA, "reference_production", "previews", slug, "index.html"): page,
            os.path.join(RELEASE_DIR, slug, "index.html"): rel, os.path.join(RELEASE_DIR, slug, "release.json"): manifest}
    stale = 0
    for dest, text in outs.items():
        cur = open(dest, encoding="utf-8").read() if os.path.exists(dest) else None
        if cur == text:
            continue
        stale += 1
        if a.check:
            print(f"STALE: {os.path.relpath(dest, ROOT)}")
        else:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, "w", encoding="utf-8").write(text)
            print(f"wrote {os.path.relpath(dest, ROOT)}")
    if a.check and not stale:
        print("up to date")
    return 1 if (a.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
