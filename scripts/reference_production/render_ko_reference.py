#!/usr/bin/env python3
"""render_ko_reference.py — render a Knowledge Object as the reconstructed body of its
EXISTING canonical route (Reference Production preview; no new URL).

Inputs (all governed, read-only):
  main/data/reference_production/render_specs/<KO>.json   wording/order only (no values)
  main/data/knowledge_objects/knowledge_object_registry.json
  main/data/evidence/*.json, main/data/sources/source_registry.json,
  main/data/originating_work_registry.json, main/data/pilots/*claims.json
  main/data/publication_candidates/<PC>.json                 postures -> Contract C

Outputs (with --write; --check verifies they are up to date and exits 1 if not):
  <route content_file>                          the canonical NON-PUBLIC draft (markdown)
  main/data/reference_production/previews/<slug>/index.html   preview (noindex; outside site/public)
  main/data/distinctiveness/ig_unit_registry.json             IG units for the canonical page

FAIL-CLOSED LAWS
  * every displayed value is a {{EVIDENCE_ID:dotted.path|filter}} placeholder resolved from an
    evidence record; a missing path aborts the render (nothing is invented);
  * every evidence record used must be governed, evidence_verified, about the KO entity, and
    ADMITTED by source_admissibility.admissible() for the declared intended use;
  * every evidence record must belong to the module's claim (KO claim_bindings) or, for a boundary
    module, to the KO boundary_evidence_ids;
  * declared cross-source consistency pairs must agree, or the render aborts;
  * the preview carries robots noindex and is written outside site/public, so it cannot deploy;
  * Contract C is DERIVED from the publication candidate's postures (contract_c_derive.derive)
    and printed; the renderer never changes a posture, route, sitemap, robots or release record.
"""

import argparse
import html
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
sys.path.insert(0, os.path.join(ROOT, "scripts", "governance_scaffolding"))
import contract_c_derive  # noqa: E402
import source_admissibility  # noqa: E402

PLACEHOLDER = re.compile(r"\{\{([A-Z0-9-]+):([A-Za-z0-9_.]+)((?:\|[a-z_]+)*)\}\}")
SITE = "https://bisulfid.com"


class RenderError(Exception):
    pass


def load(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------- display filters

def _f_hm(v):
    """Hermann–Mauguin symbol as recorded ('P 6_3/m m c (No. 194)') -> 'P6₃/mmc (No. 194)'."""
    m = re.match(r"^(.*?)(\s*\(No\.\s*\d+\))?$", str(v).strip())
    sym, num = m.group(1), m.group(2) or ""
    sym = re.sub(r"_(\d)", lambda x: "₀₁₂₃₄₅₆₇₈₉"[int(x.group(1))], sym).replace(" ", "")
    return sym + num


def _f_join(v):
    items = [str(x) for x in v]
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def _f_review_values(v):
    return re.sub(r"\s*\([^)]*\)\s*$", "", str(v)).strip()


def _f_angstrom(v):
    return re.sub(r"(\d)\s+A\b", "\\1 Å", str(v))


FILTERS = {"hm": _f_hm, "join": _f_join, "review_values": _f_review_values, "angstrom": _f_angstrom}


# --------------------------------------------------------------------------- governed context

class Context:
    def __init__(self, spec):
        self.spec = spec
        kos = load("main", "data", "knowledge_objects", "knowledge_object_registry.json")["knowledge_objects"]
        self.ko = next((k for k in kos if k["knowledge_object_id"] == spec["knowledge_object_id"]), None)
        if not self.ko:
            raise RenderError(f"unknown Knowledge Object {spec['knowledge_object_id']}")
        self.entities = list(self.ko["entity_ids"])
        self.evidence = {}
        for eid in set(spec["evidence_uses"]):
            p = os.path.join(DATA, "evidence", eid + ".json")
            if not os.path.exists(p):
                raise RenderError(f"evidence {eid} does not exist")
            self.evidence[eid] = load("main", "data", "evidence", eid + ".json")
        src = load("main", "data", "sources", "source_registry.json")
        self.sources = {s["source_id"]: s for s in (src.get("sources") if isinstance(src, dict) else src)}
        self.works = {w["work_id"]: w for w in load("main", "data", "originating_work_registry.json")["works"]}
        quals = load("main", "data", "source_use_qualification_registry.json")
        self.quals = quals.get("qualifications", quals)
        self.binding_ev = {b["claim_id"]: set(b["evidence_ids"]) for b in self.ko["claim_bindings"]}
        self.boundary_ev = set(self.ko.get("boundary_evidence_ids") or [])
        self.admission = {}
        adm_data = source_admissibility.load_all()
        for eid, use in spec["evidence_uses"].items():
            self.admission[eid] = self._admit(eid, use, adm_data)
        routes = load("main", "data", "routes.json")
        routes = routes if isinstance(routes, list) else routes["routes"]
        self.route = next((r for r in routes if r["route_id"] == spec["canonical_route_id"]), None)
        if not self.route:
            raise RenderError(f"canonical route {spec['canonical_route_id']} not in routes.json (no new URL may be created)")

    def _admit(self, eid, use, adm_data):
        e = self.evidence[eid]
        if not e.get("governed") or e.get("test_fixture"):
            raise RenderError(f"{eid}: not governed evidence")
        if e.get("evidence_review_posture") != "evidence_verified":
            raise RenderError(f"{eid}: not evidence_verified")
        if not set(self.entities) & set(e.get("concept_ids") or []):
            raise RenderError(f"{eid}: not about {' / '.join(self.entities)}")
        if use not in (e.get("allowed_uses") or []) or use in (e.get("prohibited_uses") or []):
            raise RenderError(f"{eid}: intended use '{use}' not allowed by the evidence record")
        for q in self.quals:
            if q["source_id"] == e["source_id"] and use in q.get("allowed_uses", []):
                unit, reason = source_admissibility.build_admission_unit(e, q["qualification_id"], use, adm_data)
                if unit["admitted"]:
                    return {"qualification_id": q["qualification_id"], "intended_use": use, "admitted": True,
                            "source_locked": unit["source_locked"], "originating_work_id": unit["originating_work_id"]}
        raise RenderError(f"{eid}: not admitted by source_admissibility for use '{use}'")

    def value(self, eid, path):
        if eid not in self.evidence:
            raise RenderError(f"placeholder references undeclared evidence {eid}")
        cur = self.evidence[eid]
        for part in path.split("."):
            if not isinstance(cur, dict) or part not in cur or cur[part] in (None, ""):
                raise RenderError(f"{eid}:{path} is not present in the evidence record (no value is invented)")
            cur = cur[part]
        return cur

    def resolve(self, text, allowed):
        def sub(m):
            eid, path, filters = m.group(1), m.group(2), m.group(3)
            if eid not in allowed:
                raise RenderError(f"{eid} used in a block that does not bind it")
            v = self.value(eid, path)
            for f in [x for x in filters.split("|") if x]:
                v = FILTERS[f](v)
            if isinstance(v, (list, dict)):
                raise RenderError(f"{eid}:{path} resolves to a structure; add a filter")
            return str(v)
        out = PLACEHOLDER.sub(sub, text)
        if "{{" in out:
            raise RenderError(f"unresolved placeholder in: {text[:60]}")
        return out

    def unit_entity(self, eids, declared=None):
        """The ONE KO concept an IG unit is specific to: every bound evidence record must be about it."""
        common = [x for x in self.entities if all(x in (self.evidence[e].get("concept_ids") or []) for e in eids)]
        if declared:
            if declared not in common:
                raise RenderError(f"IG unit entity {declared} is not a KO concept shared by {eids}")
            return declared
        if not common:
            raise RenderError(f"IG unit over {eids} is not specific to one KO concept")
        return common[0]

    def check_membership(self, module, eids):
        for eid in eids:
            if module.get("boundary"):
                if eid not in self.boundary_ev:
                    raise RenderError(f"boundary module {module['module_id']}: {eid} is not KO boundary evidence")
            else:
                if eid not in self.binding_ev.get(module["claim_id"], set()):
                    raise RenderError(f"module {module['module_id']}: {eid} is not bound to {module['claim_id']} in the KO")

    def contract_c(self):
        pcs = [f for f in os.listdir(os.path.join(DATA, "publication_candidates")) if f.endswith(".json")]
        for f in pcs:
            pc = load("main", "data", "publication_candidates", f)
            if pc.get("knowledge_object_id") == self.ko["knowledge_object_id"]:
                ps = pc["postures"]
                inputs = {"governance": ps["governance_posture"], "evidence": ps["evidence_posture"],
                          "claim": ps["claim_posture"], "validation": ps["validation_posture"],
                          "ig": ps["information_gain_posture"], "release": ps["release_authorization"]}
                return pc["publication_candidate_id"], inputs, contract_c_derive.derive(**inputs), \
                    pc.get("blockers_before_any_url", [])
        return None, None, ("not_public", "noindex"), ["no publication candidate record"]


# --------------------------------------------------------------------------- render

def build(spec):
    ctx = Context(spec)
    modules, units = [], []
    for m in spec["modules"]:
        paras = []
        for p in m["paragraphs"]:
            ctx.check_membership(m, p["evidence_ids"])
            text = ctx.resolve(p["text"], set(p["evidence_ids"]))
            for a, b in p.get("consistency", []):
                va, vb = ctx.value(*a.split(":", 1)), ctx.value(*b.split(":", 1))
                if str(va).replace(" ", "") != str(vb).replace(" ", ""):
                    raise RenderError(f"consistency check failed: {a}={va!r} vs {b}={vb!r}")
            paras.append({"text": text, "evidence_ids": p["evidence_ids"]})
            if p.get("ig_unit"):
                u = {"unit_id": p["ig_unit"]["unit_id"], "entity_id": ctx.unit_entity(p["evidence_ids"], p["ig_unit"].get("entity_id")),
                     "dimension": p["ig_unit"]["dimension"],
                     "statement": text, "evidence_ids": p["evidence_ids"], "audience_ids": spec["ig_audience_ids"]}
                if m.get("claim_id"):
                    u["claim_id"] = m["claim_id"]
                units.append(u)
        table = None
        if m.get("table"):
            t = m["table"]
            ctx.check_membership(m, t["evidence_ids"])
            table = {"columns": t["columns"],
                     "rows": [[ctx.resolve(c, set(t["evidence_ids"])) for c in row] for row in t["rows"]]}
        modules.append({"module_id": m["module_id"], "heading": m["heading"], "claim_id": m.get("claim_id"),
                        "paragraphs": paras, "table": table})
    glance = []
    for g in spec["at_a_glance"]:
        for eid in g["evidence_ids"]:
            if eid not in ctx.binding_ev_all() and eid not in ctx.boundary_ev:
                raise RenderError(f"at-a-glance {g['label']}: {eid} not in the KO")
        glance.append({"label": g["label"], "value": ctx.resolve(g["value"], set(g["evidence_ids"]))})
    used = sorted({e for m in modules for p in m["paragraphs"] for e in p["evidence_ids"]})
    provenance = []
    for eid in used:
        e = ctx.evidence[eid]
        s = ctx.sources.get(e["source_id"], {})
        w = ctx.works.get(ctx.admission[eid]["originating_work_id"] or "", {})
        loc = e.get("locator") or {}
        lex = e.get("lexical") or {}
        ident = loc.get("record_id") or (f"COD {loc['cod_file']}" if loc.get("cod_file") else None) \
            or (f"CAS {loc['cas']}" if loc.get("cas") else None) or (f"doi:{loc['doi']}" if loc.get("doi") else None) \
            or (f"PubChem CID {lex['cid']}" if lex.get("cid") else None) \
            or (f"{lex['section']}" + (f", PDF p. {', '.join(map(str, loc['pdf_pages']))}" if loc.get("pdf_pages") else "")
                if lex.get("section") else None) \
            or (f"entry “{lex.get('headword') or lex.get('entry')}”" if (lex.get("headword") or lex.get("entry")) else None) \
            or s.get("title", e["source_id"]).split(" — ")[0]
        no_work = ("reference work entry (dictionary, nomenclature standard, teaching text or database record)"
                   if e.get("evidence_kind") == "terminological" else "database record (no separate originating study)")
        provenance.append({
            "evidence_id": eid, "claim_id": e.get("claim_id") or "boundary (no claim)",
            "source_id": e["source_id"], "source_title": s.get("title", ""), "source_url": s.get("url"),
            "originating_work": (f"{'; '.join(w['authors'])} ({w['year']}). {w['title']}. {w['venue']}." if w
                                 else (f"{s['publisher']}: {s['title']}" if s.get("publisher") and s.get("title") else no_work)
                                 if e.get("evidence_kind") == "terminological" else no_work),
            "role": e.get("evidence_role") or "", "record": ident, "retrieval_date": e.get("retrieval_date", ""),
            "intended_use": ctx.admission[eid]["intended_use"], "qualification_id": ctx.admission[eid]["qualification_id"],
            "source_lock_status": s.get("source_lock_status", "unknown")})
    pc_id, cc_inputs, cc, blockers = ctx.contract_c()
    seo = resolve_seo(spec, ctx)
    return {"spec": spec, "ko": ctx.ko, "route": ctx.route, "modules": modules, "glance": glance,
            "provenance": provenance, "units": units, "pc_id": pc_id, "contract_c_inputs": cc_inputs,
            "contract_c": cc, "blockers": blockers, "seo": seo,
            "evidence_as_of": max((p["retrieval_date"] for p in provenance), default=None)}


def resolve_seo(spec, ctx):
    """SEO head data. JSON-LD values are evidence placeholders; sameAs comes from the cited sources;
    every internal link must point at a page that exists on the public surface (no dead links)."""
    seo = spec.get("seo")
    if not seo:
        return None
    ev = set(seo.get("json_ld_evidence_ids", []))
    ld = {"@context": "https://schema.org"}
    def res(v):
        if isinstance(v, str):
            return ctx.resolve(v, ev)
        if isinstance(v, list):
            return [res(x) for x in v]
        if isinstance(v, dict):
            return {k: res(x) for k, x in v.items()}
        return v
    for k, v in seo["json_ld"].items():
        if k == "same_as_evidence":
            ld["sameAs"] = [ctx.sources[ctx.evidence[e]["source_id"]]["url"] for e in v]
        else:
            ld[k] = res(v)
    for link in seo.get("related", []) + seo.get("breadcrumbs", []):
        p = link["path"]
        f = os.path.join(ROOT, "site", "public", p.strip("/"), "index.html") if p != "/" else \
            os.path.join(ROOT, "site", "public", "index.html")
        if not os.path.exists(f):
            raise RenderError(f"internal link {p} does not resolve to a public page")
    return {"title": seo["title"], "description": seo["description"], "json_ld": ld,
            "breadcrumbs": seo.get("breadcrumbs", []), "related": seo.get("related", [])}


def _binding_ev_all(self):
    return set().union(*self.binding_ev.values()) if self.binding_ev else set()


Context.binding_ev_all = _binding_ev_all


def render_markdown(r):
    s, route, ko = r["spec"], r["route"], r["ko"]
    fm = [
        "---", f"route_id: {route['route_id']}", "status: draft", "publication_status: non_public",
        "publication_eligibility: false", "indexable: false", "in_sitemap: false", "in_navigation: false",
        f"language: {route['language']}", f"locale: {route['locale']}", f"source_language: {route['source_language']}",
        f"title: {s['title']}", f"page_type_id: {s.get('page_type_id', 'PT_COMPOUND_ENTITY')}", f"knowledge_object_id: {ko['knowledge_object_id']}",
        f"publication_candidate_id: {r['pc_id']}", f"render_spec: {s['spec_id']}@{s['version']}",
        "generated: true", "engine: render_ko_reference_v1", "reference_production: preview", "---",
    ]
    out = fm + [f"# {s['h1']}", "",
                "**Draft status:** Reference Production preview of the existing canonical route. This page is "
                "**non-public**, **not published**, **not indexable**, **not in the sitemap** and **not publication-ready**. "
                f"Contract C for `{ko['knowledge_object_id']}` derives ({r['contract_c'][0]}, {r['contract_c'][1]}).", "",
                s["summary"], "", "## At a glance", "", "| Property | Governed value |", "| --- | --- |"]
    out += [f"| {g['label']} | {g['value']} |" for g in r["glance"]]
    for m in r["modules"]:
        out += ["", f"## {m['heading']}", ""] if out[-1] != "" else [f"## {m['heading']}", ""]
        for p in m["paragraphs"]:
            out += [p["text"], ""]
        if m["table"]:
            out += ["| " + " | ".join(m["table"]["columns"]) + " |", "|" + " --- |" * len(m["table"]["columns"])]
            out += ["| " + " | ".join(row) + " |" for row in m["table"]["rows"]]
            out += [""]
    out += [f"## {s['not_established']['heading']}", "", s["not_established"]["text"], "",
            "## Evidence trail", "", "| Evidence | Claim | Originating work | Record | Retrieved |", "| --- | --- | --- | --- | --- |"]
    out += [f"| {p['evidence_id']} | {p['claim_id']} | {p['originating_work']} | {p['record']} | {p['retrieval_date']} |"
            for p in r["provenance"]]
    out += ["", "## Source and claim status", "",
            (f"- Claims: pilot, non-operational ({', '.join(ko['claim_ids'])}); not activated in a canonical claim registry."
             if ko["claim_source"] == "pilot_non_operational" else
             f"- Claims: narrowly approved in an INACTIVE claim registry ({', '.join(ko['claim_ids'])}); approval is not activation or publication."),
            "- Sources: every source lock is `candidate`; no source is locked.",
            f"- Contract C inputs: {json.dumps(r['contract_c_inputs'])}.", "",
            "## Publication blockers", ""] + [f"- {b}" for b in r["blockers"]] + ["",
            f"*Rendered by render_ko_reference.py from {s['spec_id']}@{s['version']} — {ko['knowledge_object_id']} — route `{route['route_id']}`.*", ""]
    return "\n".join(out)


def render_html(r):
    s, route, ko = r["spec"], r["route"], r["ko"]
    e = html.escape
    glance = "\n".join(f"<tr><th scope=\"row\">{e(g['label'])}</th><td>{e(g['value'])}</td></tr>" for g in r["glance"])
    mods = []
    for m in r["modules"]:
        body = "\n".join(f"<p>{e(p['text'])}</p>" for p in m["paragraphs"])
        if m["table"]:
            head = "".join(f"<th scope=\"col\">{e(c)}</th>" for c in m["table"]["columns"])
            rows = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in row) + "</tr>" for row in m["table"]["rows"])
            body += f"\n<table class=\"reference-table\"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>"
        tag = f"<p class=\"reference-module__claim\">Claim: <code>{e(m['claim_id'])}</code></p>" if m["claim_id"] \
            else "<p class=\"reference-module__claim\">Boundary record (attached to no claim)</p>"
        mods.append(f"<section class=\"reference-module\" id=\"{e(m['module_id'])}\">\n<h2>{e(m['heading'])}</h2>\n{body}\n{tag}\n</section>")
    prov = "\n".join(
        "<tr>" + f"<td><code>{e(p['evidence_id'])}</code></td><td><code>{e(p['claim_id'])}</code></td>"
        + f"<td>{e(p['originating_work'])}</td>"
        + (f"<td><a href=\"{e(p['source_url'])}\" rel=\"nofollow\">{e(p['record'])}</a></td>" if p["source_url"] else f"<td>{e(p['record'])}</td>")
        + f"<td>{e(p['role'])}</td><td>{e(p['source_lock_status'])}</td><td>{e(p['retrieval_date'])}</td></tr>"
        for p in r["provenance"])
    cc = r["contract_c"]
    seo = r["seo"] or {"title": s["title"], "description": s["summary"], "json_ld": {}, "breadcrumbs": [], "related": []}
    crumbs = " › ".join(f"<a href=\"{e(b['path'])}\">{e(b['label'])}</a>" for b in seo["breadcrumbs"][:-1])
    crumbs = (crumbs + f" › <span aria-current=\"page\">{e(seo['breadcrumbs'][-1]['label'])}</span>") if seo["breadcrumbs"] else ""
    related = "".join(f"<li><a href=\"{e(x['path'])}\">{e(x['label'])}</a> — {e(x['relation'])}</li>" for x in seo["related"])
    return f"""<!DOCTYPE html>
<html lang="{e(route['language'])}" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{e(seo['title'])}</title>
  <meta name="description" content="{e(seo['description'])}">
  <meta name="robots" content="noindex, nofollow">
  <link rel="canonical" href="{SITE}{e(route['path'])}">
  <link rel="stylesheet" href="/assets/bisulfid-design-system/bisulfid-frame.css">
  <script type="application/ld+json">{json.dumps(seo['json_ld'], ensure_ascii=False)}</script>
</head>
<body class="bs-control-room bisulfid-atlas atlas-lane-reference" data-reference-preview="true" data-knowledge-object="{e(ko['knowledge_object_id'])}" data-atlas-lane="{e(s.get('atlas_lane', 'compound'))}">
  <div class="bs-control-room__shell">
    <header class="site-header atlas-header" role="banner">
      <nav aria-label="Atlas navigation">
        <ul class="site-nav-list">
          <li><a href="/" class="site-nav-brand">BISULFID</a></li>
          <li><a href="/atlas/">Atlas</a></li>
          <li><a href="/glossary/">Glossary</a></li>
          <li><a href="/sources/">Sources</a></li>
        </ul>
      </nav>
    </header>
    <nav class="atlas-breadcrumbs breadcrumb" aria-label="Breadcrumb">{crumbs}</nav>
    <main id="main-content" role="main">
      <article class="reference-object public-page" lang="{e(route['language'])}">
        <header class="reference-object__hero">
          <p class="page-kicker">{e(s.get('kicker', 'Scientific reference'))} · preview of {e(route['path'])}</p>
          <h1>{e(s['h1'])}</h1>
          <p class="page-intro">{e(s['summary'])}</p>
          <p class="reference-object__asof">Evidence retrieved {e(r['evidence_as_of'] or 'n/a')} · {len(r['provenance'])} admitted evidence records · values are quoted, never averaged</p>
        </header>
        <section class="reference-glance" id="at-a-glance">
          <h2>At a glance</h2>
          <table class="reference-table"><tbody>
{glance}
          </tbody></table>
        </section>
{chr(10).join(mods)}
        <section class="reference-module" id="not-established">
          <h2>{e(s['not_established']['heading'])}</h2>
          <p>{e(s['not_established']['text'].replace(' [SOURCE REQUIRED]', ''))}</p>
        </section>
        <section class="reference-provenance" id="evidence-trail">
          <h2>Evidence trail</h2>
          <table class="reference-table">
            <thead><tr><th scope="col">Evidence</th><th scope="col">Claim</th><th scope="col">Originating work</th><th scope="col">Record</th><th scope="col">Role</th><th scope="col">Source lock</th><th scope="col">Retrieved</th></tr></thead>
            <tbody>
{prov}
            </tbody>
          </table>
        </section>
        <nav class="reference-related" aria-label="Related records">
          <h2>Related records</h2>
          <ul>{related}</ul>
        </nav>
        <aside class="reference-governance" aria-label="Governance status">
          <h2>Governance status</h2>
          <p>Knowledge Object <code>{e(ko['knowledge_object_id'])}</code> · render spec <code>{e(s['spec_id'])}@{e(s['version'])}</code> · Contract C ({e(cc[0])}, {e(cc[1])}). Preview only: not deployed, not indexable.</p>
        </aside>
      </article>
    </main>
    <footer class="site-footer" role="contentinfo">
      <div class="site-footer__inner"><p class="footer-identity">Bisulfid Sovereign Reference Atlas</p></div>
    </footer>
  </div>
</body>
</html>
"""


def registry_with_units(r, page_id):
    reg = load("main", "data", "distinctiveness", "ig_unit_registry.json")
    ents = r["ko"]["entity_ids"]
    entry = {"page": page_id, **({"entity_id": ents[0]} if len(ents) == 1 else {"entity_ids": ents}),
             "knowledge_object_id": r["ko"]["knowledge_object_id"],
             "publication_candidate_id": r["pc_id"], "localization_of": None,
             "role": "canonical route reconstruction preview (non-public; rendered by render_ko_reference.py)",
             "units": r["units"]}
    mine = [i for i, p in enumerate(reg["pages"]) if p["page"] == page_id
            or p.get("knowledge_object_id") == r["ko"]["knowledge_object_id"]]
    pages = [p for i, p in enumerate(reg["pages"]) if i not in mine]
    at = mine[0] if mine else len(pages)  # replace in place: output is stable across specs
    reg["pages"] = pages[:at] + [entry] + pages[at:]
    return reg


def outputs(spec_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    r = build(spec)
    md_path = os.path.join(ROOT, r["route"]["content_file"])
    slug = r["route"]["path"].strip("/") or "home"
    html_path = os.path.join(DATA, "reference_production", "previews", slug, "index.html")
    reg_path = os.path.join(DATA, "distinctiveness", "ig_unit_registry.json")
    reg = registry_with_units(r, r["route"]["content_file"])
    return r, {md_path: render_markdown(r), html_path: render_html(r),
               reg_path: json.dumps(reg, indent=2, ensure_ascii=False) + "\n"}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", help="one render spec (default: every KO-*.json render spec)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    sdir = os.path.join(DATA, "reference_production", "render_specs")
    specs = [args.spec] if args.spec else [os.path.join(sdir, f) for f in sorted(os.listdir(sdir))
                                           if f.startswith("KO-") and f.endswith(".json")]
    return max(run_spec(p, args) for p in specs)


def run_spec(spec_path, args):
    try:
        r, files = outputs(spec_path)
    except RenderError as exc:
        print(f"RENDER REFUSED: {exc}")
        return 1
    stale = []
    for path, text in files.items():
        cur = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if cur != text:
            stale.append(os.path.relpath(path, ROOT))
            if args.write:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(text)
    print(f"{r['ko']['knowledge_object_id']} -> route {r['route']['route_id']} ({r['route']['path']}): "
          f"{len(r['modules'])} modules, {len(r['units'])} IG units, {len(r['provenance'])} admitted evidence records; "
          f"Contract C {tuple(r['contract_c'])}")
    if args.check and stale:
        print("STALE (re-run --write): " + ", ".join(stale))
        return 1
    print(("wrote: " + ", ".join(stale)) if (args.write and stale) else "up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
