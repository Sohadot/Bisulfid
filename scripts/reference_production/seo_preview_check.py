#!/usr/bin/env python3
"""seo_preview_check.py — SEO-quality checks for reference previews (Recovery-02).

Gate 12 PASS is necessary, not sufficient. For each preview this checks the things a search engine
and a reader see, and records Gate 12 / 12-I against the live public surface:
  head        title 30–65 chars; meta description 70–160; one canonical (absolute, intended path);
              robots present; html lang; JSON-LD parses with schema.org @context
  structure   exactly one h1; no heading level skipped; substantive words; no [SOURCE REQUIRED] or
              template placeholders leaking into HTML
  links       every internal href resolves to a public page or to a reference preview
  intent      every declared search intent is served by a module/section that exists
  gate 12     nearest similarity, template-sentence ratio and shared skeleton vs the 14,041 public
              pages; Gate 12 verdict (knowledge reference) or Gate 12-I verdict (institutional)
Writes main/data/reference_production/SEO_PREVIEW_ASSESSMENT.json. Exit 1 if a check fails.
"""

import html.parser
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
SITE = "https://bisulfid.com"
sys.path.insert(0, os.path.join(ROOT, "scripts", "validators"))
import distinctiveness_core as dc  # noqa: E402

PREVIEWS = [
    {"name": "MoS2 canonical reference", "file": "main/data/reference_production/previews/molybdenum-disulfide/index.html",
     "path": "/molybdenum-disulfide/", "spec": "main/data/reference_production/render_specs/KO-MOS2-SCIENTIFIC-001.json",
     "markdown": "main/content/en/pages/molybdenum-disulfide.md", "class": "knowledge_reference"},
    {"name": "Bisulfid / bisulfide terminology reference", "file": "main/data/reference_production/previews/bisulfid-vs-bisulfide/index.html",
     "path": "/bisulfid-vs-bisulfide/", "spec": "main/data/reference_production/render_specs/KO-BISULFID-TERMINOLOGY-001.json",
     "markdown": "main/content/en/pages/bisulfid-vs-bisulfide.md", "class": "knowledge_reference"},
    {"name": "Homepage", "file": "main/data/reference_production/previews/home/index.html", "path": "/",
     "spec": "main/data/reference_production/render_specs/INST-HOME-EN.json", "class": "institutional", "route_id": "home"},
    {"name": "Homepage (DE)", "file": "main/data/reference_production/previews/de/index.html", "path": "/de/",
     "spec": "main/data/reference_production/render_specs/INST-HOME-DE.json", "class": "institutional", "route_id": "de_home"},
]


class Scan(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title, self.meta, self.links, self.hrefs, self.headings, self.ld, self.lang = "", {}, [], [], [], [], None
        self._in, self._buf, self._ld = None, [], False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "meta" and a.get("name"):
            self.meta[a["name"].lower()] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.links.append(a.get("href"))
        if tag == "a" and a.get("href"):
            self.hrefs.append(a["href"])
        if tag == "title" or re.fullmatch(r"h[1-6]", tag):
            self._in, self._buf = tag, []
        if tag == "script" and a.get("type") == "application/ld+json":
            self._ld, self._buf = True, []

    def handle_endtag(self, tag):
        if tag == self._in:
            text = " ".join("".join(self._buf).split())
            if tag == "title":
                self.title = text
            else:
                self.headings.append((int(tag[1]), text))
            self._in = None
        if tag == "script" and self._ld:
            self.ld.append("".join(self._buf))
            self._ld = False

    def handle_data(self, data):
        if self._in or self._ld:
            self._buf.append(data)


def resolves(href):
    if not href.startswith("/"):
        return True  # external (provenance links)
    p = href.split("#")[0]
    pub = os.path.join(ROOT, "site", "public", p.strip("/"), "index.html") if p != "/" else os.path.join(ROOT, "site", "public", "index.html")
    prev = os.path.join(DATA, "reference_production", "previews", p.strip("/") or "home", "index.html")
    return os.path.exists(pub) or os.path.exists(prev)


def check(pv, html_u, policy, ctx):
    txt = open(os.path.join(ROOT, pv["file"]), encoding="utf-8").read()
    s = Scan()
    s.feed(txt)
    spec = json.load(open(os.path.join(ROOT, pv["spec"]), encoding="utf-8"))
    res = {"name": pv["name"], "preview": pv["file"], "intended_path": pv["path"], "checks": {}, "measures": {}}
    c = res["checks"]
    c["title_30_65"] = 30 <= len(s.title) <= 65
    d = s.meta.get("description", "")
    c["description_70_160"] = 70 <= len(d) <= 160
    c["one_canonical_absolute_intended"] = s.links == [SITE + pv["path"]]
    c["robots_present_noindex_preview"] = "noindex" in s.meta.get("robots", "")
    c["html_lang"] = bool(s.lang)
    try:
        lds = [json.loads(x) for x in s.ld]
        c["json_ld_valid"] = bool(lds) and all(x.get("@context") == "https://schema.org" and x.get("@type") for x in lds)
    except ValueError:
        c["json_ld_valid"] = False
    levels = [h[0] for h in s.headings]
    c["exactly_one_h1"] = levels.count(1) == 1
    c["no_skipped_heading_level"] = all(b - a <= 1 for a, b in zip(levels, levels[1:]))
    c["no_source_required_or_placeholder_leak"] = "[SOURCE REQUIRED]" not in txt and "{{" not in txt
    bad = [h for h in s.hrefs if not resolves(h)]
    c["internal_links_resolve"] = not bad
    if bad:
        res["unresolved_links"] = bad
    served = {m["module_id"] for m in spec.get("modules", [])} | {"at_a_glance"}
    intents = spec.get("seo", {}).get("search_intents", [])
    unserved = [i["query_class"] for i in intents if i.get("served_by") and not set(i["served_by"]) <= served]
    c["declared_intents_served"] = not unserved
    page = dc.parse_html(os.path.join(ROOT, pv["file"]), txt, policy, page_id=pv["file"])
    near = html_u.nearest(page, exclude_ids=(f"site/public{pv['path']}index.html",))
    tr = html_u.template_ratio(page)
    shared, _ = html_u.skeleton_match(page)
    m = res["measures"]
    m.update({"title": s.title, "title_chars": len(s.title), "description_chars": len(d),
              "headings": s.headings, "substantive_words": len(page.masked_tokens),
              "nearest_public_page": near, "template_sentence_ratio_vs_public": round(tr, 4),
              "skeleton_shared_with_public_pages": shared, "internal_links": len([h for h in s.hrefs if h.startswith("/")]),
              "external_provenance_links": len([h for h in s.hrefs if h.startswith("http")])})
    if pv["class"] == "institutional":
        inst = dc.InstitutionalRegistry().lookup(route_id=pv["route_id"])
        v = dc.gate12_verdict(page, html_u, policy, ctx, text=near, institutional=inst)
        res["gate12"] = {"class": "Gate 12-I", "function": inst and inst["function"], "verdict": v["verdict"], "failures": v["failures"]}
    else:
        md_path = os.path.join(ROOT, pv["markdown"])
        mdp = dc.parse_markdown(md_path, open(md_path, encoding="utf-8").read(), policy)
        md_u = dc.Universe(dc.load_markdown_pages(policy), policy)
        v = dc.gate12_verdict(mdp, md_u, policy, ctx, unit_index=dc.unit_statement_index(ctx, policy, md_u.by_id))
        res["gate12"] = {"class": "Gate 12 (knowledge reference; IG from the canonical draft)", "verdict": v["verdict"],
                         "failures": v["failures"], "ig_valid_units": v["information_gain"]["valid_units"]}
    c["gate12_pass"] = res["gate12"]["verdict"] == "PASS"
    c["distinct_from_public_surface"] = near["similarity"] < 0.55 and tr < 0.30
    res["pass"] = all(c.values())
    return res


def main():
    policy = dc.load_policy()
    ctx = dc.IGContext()
    html_u = dc.Universe(dc.load_html_pages(policy, os.path.join(ROOT, "site", "public")), policy)
    results = [check(pv, html_u, policy, ctx) for pv in PREVIEWS]
    blockers = os.path.join(DATA, "reference_production", "blockers", "PLAN-BISULFID-BISULFIDE-BOUNDARY_BLOCKERS.json")
    if os.path.exists(blockers):
        b = json.load(open(blockers, encoding="utf-8"))
        term = next(r for r in results if r["intended_path"] == "/bisulfid-vs-bisulfide/")
        term["plan_blockers"] = {"verdict": b["verdict"], "renderable_modules": b["renderable_modules"],
                                 "modules": len(b["modules"]), "still_blocked": [m["module_id"] for m in b["modules"] if not m["renderable"]],
                                 "file": "main/data/reference_production/blockers/PLAN-BISULFID-BISULFIDE-BOUNDARY_BLOCKERS.json"}
    with open(os.path.join(DATA, "reference_production", "SEO_PREVIEW_ASSESSMENT.json"), "w", encoding="utf-8") as fh:
        json.dump({"note": "Automated checks only; search intent, competitors and accuracy review are in RECOVERY_02_REPORT.md. "
                           "No ranking, traffic or Google verdict is claimed.", "results": results}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    for r in results:
        failed = [k for k, v in r.get("checks", {}).items() if not v]
        print(f"[{'PASS' if r['pass'] else 'FAIL' if r.get('checks') else r.get('status')}] {r['name']}"
              + (f" failed={failed}" if failed else "")
              + (f" gate12={r['gate12']['verdict']} words={r['measures']['substantive_words']} "
                 f"nearest={r['measures']['nearest_public_page']['similarity']}" if r.get("checks") else ""))
    return 0 if all(r["pass"] for r in results if r.get("checks")) else 1


if __name__ == "__main__":
    sys.exit(main())
