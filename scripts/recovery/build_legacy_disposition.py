#!/usr/bin/env python3
"""build_legacy_disposition.py — Recovery-01 legacy disposition registry.

Classifies every legacy route (main/data/routes.json, 14,000) and every non-route legacy HTML
surface (site/public pages with no route record) into ONE governed recovery category:

  independent_reference_candidate              a Knowledge Object is bound to this canonical route
  module_of_existing_knowledge_object          same concept as a bound KO; belongs inside it as a module
  valid_language_or_domain_specific_reference_candidate
                                               distinct language/domain object with its own governed evidence
  evidence_pending_knowledge_entity            the ONE canonical surface of a curated concept; no KO yet
  duplicate_or_redundant_presentation_surface  audience/layer/cohort variant of another surface, a duplicate
                                               institutional function, or an internal pipeline-status page
  unresolved_requires_review                   identity unverified (generated entity) or institutional review

It is a CLASSIFICATION ONLY: it authorizes nothing, and it never deletes, redirects, de-indexes or
publishes a URL. Route identities and historical release records are copied verbatim.

Inputs: routes.json, release_ledger.json, cohort inventories, ontology/claims/evidence, the
Gate-12 per-page audit (CORPUS_DISTINCTIVENESS_PAGES.tsv), the institutional registry, the legacy
hold, site/public (robots + sitemaps).
Outputs (main/data/recovery/): legacy_disposition_registry.jsonl, legacy_disposition_summary.json.
Deterministic: same inputs, same bytes.
"""

import ast
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
OUT = os.path.join(DATA, "recovery")
PUBLIC = os.path.join(ROOT, "site", "public")
sys.path.insert(0, os.path.join(ROOT, "scripts", "validators"))

CATEGORIES = (
    "independent_reference_candidate",
    "module_of_existing_knowledge_object",
    "valid_language_or_domain_specific_reference_candidate",
    "evidence_pending_knowledge_entity",
    "duplicate_or_redundant_presentation_surface",
    "unresolved_requires_review",
)

# Explicit, governed bindings (basis recorded). Nothing else is ever bound to a KO by inference.
KO_BINDINGS = {
    "molybdenum_disulfide": {
        "category": "independent_reference_candidate", "knowledge_object_id": "KO-MOS2-SCIENTIFIC-001",
        "basis": "PC-MOS2-SCIENTIFIC-001 disposition governed_reference_no_new_route + IG PAIR-KO-MOS2-SCI-vs-LEGACY-SCI-ROUTE "
                 "(near_duplicate => realize the KO at the EXISTING route, no new URL); render spec RSPEC-KO-MOS2-SCIENTIFIC-001"},
    "de_core_mos2": {
        "category": "valid_language_or_domain_specific_reference_candidate", "knowledge_object_id": None,
        "lexical_object": {"lexeme_id": "LEX-DE-MOS2-001", "claim_id": "CLM-TERM-MOS2-DE-001", "evidence_id": "EVD-MOS2-DE-001"},
        "basis": "IG PAIR-KO-MOS2-SCI-vs-DE-LEXICAL = valid_domain_specific_reference; CLM-TERM-MOS2-DE-001 approved; "
                 "related_routes [de_core_mos2]"},
}

# Hand-authored root routes -> concept key (EN unless 'de:' prefix). Basis: alias_table.
ROOT_ALIASES = {
    "what_is_bisulfid": "bisulfid", "de_what_is_bisulfid": "de:bisulfid", "bisulfide_hydrosulfide_sulfide": "bisulfide|hydrosulfide|sulfide",
    "de_bisulfide_hydrosulfide_sulfide": "de:bisulfide|hydrosulfide|sulfide", "sulfide_anion_term_record": "sulfide_anion",
    "sulfur_element_term_record": "sulfur_element", "carbon_disulfide_terms": "carbon_disulfide", "carbonyl_sulfide_terms": "carbonyl_sulfide",
    "copper_sulfides_language": "copper_sulfides", "sulfate_terminology": "sulfate", "polysulfide_terminology": "polysulfide",
    "tin_sulfides_terms": "tin_sulfides", "silver_gold_sulfides_terms": "silver_gold_sulfides",
    "sodium_sulfide_salts_language": "sodium_sulfide_salts", "en_term_polysulfide_salts": "polysulfide_salts",
    "en_term_sulfite_salts": "sulfite_salts", "bisulfite_wall_explainer": "bisulfite_disambiguation",
    "de_dis_bisulfite_wall": "de:bisulfite_disambiguation", "de_term_molybdaensulfid": "de:molybdenum_disulfide",
    "de_molybdenum_disulfide": "de:molybdenum_disulfide", "claus_process_vocabulary": "claus_process",
    "contact_process_vocabulary": "contact_process", "de_term_claus": "de:claus_process",
    "what_is_sulfur": "sulfur", "de_what_is_sulfur": "de:sulfur", "sulfid_vs_sulfide": "sulfid|sulfide",
    "bisulfid_vs_bisulfide": "bisulfid|bisulfide", "de_sulfid_vs_sulfide": "de:sulfid|sulfide",
    "de_bisulfid_vs_bisulfide": "de:bisulfid|bisulfide",
}
DE_CORE_FORMULAS = {"mos2": "molybdenum_disulfide", "cds": "cadmium_sulfide", "cus": "copper_sulfides", "fes": "iron_sulfides",
                    "k2s": "potassium_sulfide", "na2s": "sodium_sulfide", "pbs": "lead_sulfide", "zns": "zinc_sulfide",
                    "ws2": "tungsten_disulfide"}
PIPELINE_STATUS = re.compile(r"^(cohort0[45]_(en|de)_(gov|index)_|en_foundation_(1500|7500|14000)_|en_gov_rc_pipeline_status$|"
                             r"en_gov_batch_render_discipline$|en_index_cohort03_spine$|en_multilingual_de_expansion_hub$)")
VARIANT_SUFFIXES = ("term_chem_know", "term_chem_acad", "term_res_res", "aud_stu_edu", "aud_ai_tech", "cmp_chem_acad",
                    "air_res_res", "child_stu_edu")
CATEGORY_PREFIXES = ("inorg_", "organo_", "ind_", "min_", "metal_", "dis_")


def load(*p):
    with open(os.path.join(ROOT, *p), encoding="utf-8") as fh:
        return json.load(fh)


def cohort03_entities():
    src = open(os.path.join(ROOT, "scripts", "generate_1500_corpus_expansion_v1.py"), encoding="utf-8").read()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "EN_ENTITIES" for t in node.targets):
            return set(ast.literal_eval(node.value))
    return set()


class Inputs:
    def __init__(self):
        r = load("main", "data", "routes.json")
        self.routes = r if isinstance(r, list) else r["routes"]
        self.ledger = {x["route_id"]: x for x in load("main", "data", "release_ledger.json")["records"]}
        self.inv = {}
        for f in ("COHORT_02_EN_TERMINOLOGY_ROUTE_INVENTORY.json", "COHORT_04_7500_EXPANSION_INVENTORY.json",
                  "COHORT_05_14000_EXPANSION_INVENTORY.json"):
            for row in load("main", "data", f)["rows"]:
                self.inv[row["route_id"]] = row
        c2 = [x for x in self.inv.values() if x["route_id"].startswith("cohort02")]
        self.recognized = {x["term_entity_id"] for x in c2 if x.get("page_type_id") != "PT_DIFFERENCE_COMPARISON"}
        self.recognized |= {t["term_id"] for t in load("main", "data", "ontology", "sulfur_terms.json")["terms"]}
        self.recognized |= cohort03_entities()
        self.recognized |= {v for v in ROOT_ALIASES.values() if not v.startswith("de:") and "|" not in v}
        self.recognized |= set(DE_CORE_FORMULAS.values())
        self.recognized |= {"molybdenum_disulfide", "sulfur", "disulfide_bonds", "protein_disulfide_structure"}
        self.claims_by_route = defaultdict(list)
        for f in ("terminology_claims.json", "science_claims.json"):
            for c in load("main", "data", "claims", f)["claims"]:
                for rid in c.get("related_routes") or []:
                    self.claims_by_route[rid].append(f"{c['claim_id']}:{c['status']}")
        self.evidence_by_concept = defaultdict(list)
        for f in sorted(os.listdir(os.path.join(DATA, "evidence"))):
            if f.startswith("EVD-") and f.endswith(".json"):
                e = load("main", "data", "evidence", f)
                for c in e.get("concept_ids") or []:
                    self.evidence_by_concept[c].append(e["evidence_id"])
        self.g12 = {}
        tsv = os.path.join(DATA, "distinctiveness", "CORPUS_DISTINCTIVENESS_PAGES.tsv")
        with open(tsv, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("#") or line.startswith("surface\t"):
                    continue
                c = line.rstrip("\n").split("\t")
                self.g12[(c[0], c[1])] = {"verdict": c[2], "S": float(c[3]), "closest": c[4] or None,
                                          "template_ratio": float(c[5]), "ig_units": int(c[7]),
                                          "substantive_tokens": int(c[8]), "failures": c[11]}
        hold = load("main", "data", "distinctiveness", "legacy_surface_hold.json")
        # Gate-12 legacy hold = sealed entries that failed Gate 12 (the baseline also records passing pages).
        self.hold = {e["p"] for e in hold["entries"] if e.get("g", "FAIL") != "PASS"}
        self.hold_meta = {k: hold[k] for k in ("hold_id", "sealed_from", "entry_count", "entries_sha256")}
        inst = load("main", "data", "distinctiveness", "institutional_surface_registry.json")
        self.inst = {}
        holders = {}
        for b in inst["bindings"]:
            key = b.get("route_id") or b.get("path")
            fk = (b["function_id"], b["language"])
            holders.setdefault(fk, key)
            self.inst[key] = dict(b, holder=holders[fk])
        self.robots, self.html_paths = {}, set()
        for dp, dn, fn in os.walk(PUBLIC):
            if os.path.abspath(dp) == os.path.abspath(PUBLIC):
                dn[:] = [d for d in dn if d not in ("_integration_sample", "_visual_proof_sample", "assets")]
            if "index.html" in fn:
                rel_dir = os.path.relpath(dp, PUBLIC)
                path = "/" if rel_dir == "." else "/" + rel_dir.replace(os.sep, "/") + "/"
                self.html_paths.add(path)
                head = open(os.path.join(dp, "index.html"), encoding="utf-8", errors="replace").read(2000)
                m = re.search(r'<meta name="robots" content="([^"]+)"', head)
                self.robots[path] = m.group(1) if m else None
        self.sitemap = set()
        for f in os.listdir(PUBLIC):
            if f.startswith("sitemap") and f.endswith(".xml"):
                for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", open(os.path.join(PUBLIC, f), encoding="utf-8").read()):
                    if loc.endswith(".xml"):
                        continue
                    p = re.sub(r"^https?://[^/]+", "", loc) or "/"
                    self.sitemap.add(p if p.endswith("/") else p + "/")


def split_pair(s, vocab):
    toks = s.split("_")
    for i in range(1, len(toks)):
        a, b = "_".join(toks[:i]), "_".join(toks[i:])
        if a in vocab and b in vocab:
            return "|".join(sorted((a, b)))
    return None


def entity_key(route, inp):
    """(concept_key, language, basis, recognized, kind) — kind: concept | comparison | pipeline | institutional."""
    rid, lang = route["route_id"], route["language"]
    if PIPELINE_STATUS.match(rid):
        return (rid, lang, "pipeline_status_pattern", False, "pipeline")
    if rid in ROOT_ALIASES:
        k = ROOT_ALIASES[rid]
        return (k if k.startswith("de:") else k, lang, "alias_table", True, "comparison" if "|" in k else "concept")
    m = re.match(r"^de_core_(.+)$", rid)
    if m:
        base = DE_CORE_FORMULAS.get(m.group(1), m.group(1))
        return ("de:" + base, "de", "de_core_formula_table" if m.group(1) in DE_CORE_FORMULAS else "route_id_parse", True, "concept")
    m = re.match(r"^(?:cohort0[45]_)?de_(?:term_)?(?!dis_)(.+)$", rid) if lang == "de" else None
    if m:
        name = m.group(1)
        generated = rid.startswith("cohort0")
        en = name if name in inp.recognized else (name + "e" if name + "e" in inp.recognized else None)
        return ("de:" + (en or name), "de", "route_id_parse", (en is not None) or not generated, "concept")
    inv = inp.inv.get(rid)
    if inv and rid.startswith("cohort02"):
        tid = inv["term_entity_id"]
        if inv.get("page_type_id") == "PT_DIFFERENCE_COMPARISON":
            sides = inv.get("comparison_sides") or tid.split("_vs_")
            return ("|".join(sorted(sides)), lang, "inventory", all(s in inp.recognized for s in sides), "comparison")
        tid = "molybdenum_disulfide" if tid == "molybdenum_disulfide_mos2" else tid
        return (tid, lang, "inventory", True, "concept")
    m = re.match(r"^cohort0[45]_en_dis_(.+)_boundary$", rid) or re.match(r"^(?:en|de)_dis_(.+)$", rid)
    if m:
        pair = split_pair(m.group(1), inp.recognized | {"sulfone", "sulfoxide", "thiolate", "mercaptan", "thioether",
                                                       "sulfenyl", "sulfinyl", "sulfonyl", "sulfonic", "native_sulfur",
                                                       "elemental_sulfur", "inorganic", "organosulfur", "sulfide_salt",
                                                       "sulfuric", "sulfate", "sulfite", "thiosulfate", "carbide", "halide",
                                                       "oxide", "mineral", "synthetic_sulfide", "ore", "concentrate_sulfide",
                                                       "alkyl", "aryl_sulfide", "sulfonate", "bisulfide", "hydrogen_sulfide"})
        pre = "de:" if lang == "de" else ""
        curated = not rid.startswith("cohort0")
        if pair:
            return (pre + pair, lang, "route_id_parse", True, "comparison")
        return (pre + m.group(1), lang, "route_id_parse", curated, "comparison")
    if inv and rid.startswith(("cohort04_en_", "cohort05_en_")):
        t = re.sub(r"^c0[45]_", "", inv["term_or_entity"])
        stripped = next((t[len(p):] for p in CATEGORY_PREFIXES if t.startswith(p)), t)
        if stripped in inp.recognized:
            return (stripped, lang, "inventory+category_strip", True, "concept")
        return ("generated:" + t, lang, "inventory", False, "concept")
    m = re.match(r"^cohort03_en_(.+)_(" + "|".join(VARIANT_SUFFIXES) + ")$", rid)
    if m:
        return (m.group(1), lang, "route_id_parse", m.group(1) in inp.recognized, "concept")
    base = re.sub(r"^(en_term_|en_)", "", rid)
    # A hand-authored (non-cohort) route is a curated registry entry by construction.
    return (base, lang, "route_id", base in inp.recognized or not rid.startswith("cohort0"), "concept")


def canonical_rank(route, inp):
    rid = route["route_id"]
    gen_md = inp.g12.get(("md", route["content_file"].replace("main/content/", "")), {})
    tier = (0 if rid in KO_BINDINGS else 1 if not rid.startswith("cohort0") else
            2 if rid.startswith("cohort02") and rid.endswith(("_term_chem_acad", "_cmp_chem_acad")) else
            3 if rid.startswith("cohort02") else 4 if rid.startswith("cohort03") else 5 if rid.startswith("cohort04") else 6)
    return (tier, -gen_md.get("substantive_tokens", 0), len(route["path"]), rid)


def build():
    inp = Inputs()
    records, groups = [], defaultdict(list)
    for r in inp.routes:
        key = entity_key(r, inp)
        rec = {"record_type": "route", "route_id": r["route_id"], "path": r["path"], "language": r["language"],
               "content_file": r["content_file"],
               "registry": {"status": r["status"], "indexable": r["indexable"]},
               "ledger": {k: inp.ledger.get(r["route_id"], {}).get(k) for k in
                          ("release_status", "public_status", "indexable", "sitemap_file")},
               "_key": key}
        records.append(rec)
        if key[4] in ("concept", "comparison"):
            groups[(key[0], key[1])].append(rec)
    route_paths = {r["path"] for r in inp.routes}
    for path in sorted(inp.html_paths - route_paths):
        slug = path.strip("/").replace("-", "_") or "home"
        key = (slug, "de" if path.startswith("/de/") else "en", "path_slug", slug in inp.recognized, "concept")
        rec = {"record_type": "non_route_legacy_surface", "route_id": None, "path": path, "language": key[1],
               "content_file": None, "registry": None, "ledger": None, "_key": key}
        records.append(rec)
        groups[(key[0], key[1])].append(rec)

    canonical = {}
    for gk, members in groups.items():
        routed = [m for m in members if m["route_id"]]
        if routed:
            best = min(routed, key=lambda m: canonical_rank(next(r for r in inp.routes if r["route_id"] == m["route_id"]), inp))
            canonical[gk] = best["route_id"]

    mos2_targets = {("molybdenum_disulfide", "en"): "molybdenum_disulfide", ("de:molybdenum_disulfide", "de"): "de_core_mos2"}

    def g12(v):
        return None if not v else f"{v['verdict']}|{v['S']}|{v['failures'] or '-'}|{v['ig_units']}"

    for rec in records:
        key, lang = rec.pop("_key"), rec["language"]
        content_file = rec.pop("content_file")
        concept, basis, recognized, kind = key[0], key[2], key[3], key[4]
        rid, path = rec["route_id"], rec["path"]
        target, ko, detail = None, None, None
        live = path in inp.html_paths
        md = inp.g12.get(("md", content_file.replace("main/content/", ""))) if content_file else None
        html = inp.g12.get(("html", path.lstrip("/") or "index.html")) if live else None
        inst = inp.inst.get(rid) or inp.inst.get(path)
        gk = (concept, lang)
        if rid in KO_BINDINGS:
            b = KO_BINDINGS[rid]
            cat, ko, detail = b["category"], b.get("knowledge_object_id"), b["basis"]
            code = "GOVERNED_KO_BINDING" if ko else "GOVERNED_LEXICAL_BINDING"
        elif inst and inst["holder"] == (rid or path):
            cat, code, detail = "unresolved_requires_review", "INSTITUTIONAL_GATE12I_REVIEW", inst["function_id"]
        elif inst:
            cat, code, target, detail = ("duplicate_or_redundant_presentation_surface", "DUPLICATE_INSTITUTIONAL_FUNCTION",
                                         inst["holder"], inst["function_id"])
        elif kind == "pipeline":
            cat, code = "duplicate_or_redundant_presentation_surface", "INTERNAL_PIPELINE_STATUS"
        elif gk in mos2_targets and rid != mos2_targets[gk]:
            if lang == "en":
                cat, code, target, ko = ("module_of_existing_knowledge_object", "MODULE_OF_KNOWLEDGE_OBJECT",
                                         "molybdenum_disulfide", "KO-MOS2-SCIENTIFIC-001")
            else:
                cat, code, target = ("duplicate_or_redundant_presentation_surface", "DUPLICATE_OF_GOVERNED_LEXICAL_OBJECT",
                                     "de_core_mos2")
        elif rid is not None and canonical.get(gk) == rid:
            cat, code = (("evidence_pending_knowledge_entity", "CANONICAL_CURATED_CONCEPT_NO_KO") if recognized else
                         ("unresolved_requires_review", "GENERATED_ENTITY_IDENTITY_UNVERIFIED"))
        elif canonical.get(gk):
            cat, code, target = "duplicate_or_redundant_presentation_surface", "VARIANT_OF_CANONICAL", canonical[gk]
        else:
            cat, code = "unresolved_requires_review", "NON_ROUTE_SURFACE_UNMATCHED"
        evid = sorted(set(inp.evidence_by_concept.get(concept.replace("de:", ""), [])))
        rec.update({
            "entity": {"key": concept, "kind": kind, "basis": basis, "recognized": recognized},
            "category": cat, "reason_code": code, "target": target, "ko": ko,
            "live": None if not live else {
                "robots": inp.robots.get(path), "in_sitemap": path in inp.sitemap,
                "requests_indexation": ("noindex" not in (inp.robots.get(path) or "")) or path in inp.sitemap},
            "gate12": {"md": g12(md), "html": g12(html)},
            "legacy_hold": path in inp.hold,
        })
        if detail:
            rec["detail"] = detail
        if evid:
            rec["governed_evidence_n"] = len(evid)
        if inp.claims_by_route.get(rid):
            rec["claims"] = inp.claims_by_route[rid]
    return records, inp


REASON_CODES = {
    "GOVERNED_KO_BINDING": "a Knowledge Object is explicitly bound to this EXISTING canonical route (no new URL)",
    "GOVERNED_LEXICAL_BINDING": "a governed language-specific object (approved claim + lexeme + evidence) is scoped to this route",
    "INSTITUTIONAL_GATE12I_REVIEW": "registered institutional surface (detail = function); judged by Gate 12-I, not as a knowledge entity",
    "DUPLICATE_INSTITUTIONAL_FUNCTION": "a second surface for an institutional function already held by `target`",
    "INTERNAL_PIPELINE_STATUS": "exposes internal cohort/pipeline build state already held in governance records",
    "MODULE_OF_KNOWLEDGE_OBJECT": "same concept as `ko`; its content belongs inside that object at `target` (IG module_relationship)",
    "DUPLICATE_OF_GOVERNED_LEXICAL_OBJECT": "same-language duplicate of the governed lexical surface at `target`",
    "CANONICAL_CURATED_CONCEPT_NO_KO": "the one canonical surface of a curated concept; awaits governed evidence and a Knowledge Object",
    "GENERATED_ENTITY_IDENTITY_UNVERIFIED": "canonical surface of a combinatorially generated name; confirm the entity exists before KO work",
    "VARIANT_OF_CANONICAL": "audience/layer/cohort variant of the canonical surface `target`",
    "NON_ROUTE_SURFACE_UNMATCHED": "public HTML with no route record and no matching concept; register or retire after review",
}


def summarize(records, inp):
    routes = [r for r in records if r["record_type"] == "route"]
    extra = [r for r in records if r["record_type"] != "route"]
    by_cat = Counter(r["category"] for r in routes)
    by_cat_all = Counter(r["category"] for r in records)
    live_req = Counter(r["category"] for r in records if r["live"] and r["live"]["requests_indexation"])
    stage2_noindex = sum(1 for r in records if r["legacy_hold"] and r["live"] and r["live"]["requests_indexation"])
    canon = [r for r in records if r["category"] in ("evidence_pending_knowledge_entity", "independent_reference_candidate",
                                                              "valid_language_or_domain_specific_reference_candidate")]
    with_evidence = [r["route_id"] or r["path"] for r in canon if r.get("governed_evidence_n")]
    targets = Counter(r["target"] for r in records if r["target"])
    return {
        "registry_id": "RECOVERY-01-LEGACY-DISPOSITION", "version": "1.0.0",
        "generated_by": "scripts/recovery/build_legacy_disposition.py",
        "authorizes": "nothing — classification only; no URL is deleted, redirected, de-indexed or published",
        "baseline": {
            "routes_json_routes": len(inp.routes),
            "routes_json_status": dict(Counter(r["status"] for r in inp.routes)),
            "routes_json_indexable_true": sum(1 for r in inp.routes if r["indexable"]),
            "release_ledger_records": len(inp.ledger),
            "release_ledger_released": sum(1 for x in inp.ledger.values() if x["release_status"] == "released"),
            "release_ledger_blocked": sorted(k for k, x in inp.ledger.items() if x["release_status"] != "released"),
            "generated_html_pages": len(inp.html_paths),
            "html_pages_without_route": len(extra),
            "html_robots_index": sum(1 for v in inp.robots.values() if v and "noindex" not in v),
            "html_robots_noindex": sorted(p for p, v in inp.robots.items() if v and "noindex" in v),
            "sitemap_urls": len(inp.sitemap),
            "ledger_blocked_but_html_indexable": sorted(k for k, x in inp.ledger.items() if x["release_status"] != "released"
                                                        and "noindex" not in (inp.robots.get(x.get("route_path", ""), "noindex"))),
            "legacy_hold": inp.hold_meta,
        },
        "counts": {
            "routes_by_category": {c: by_cat.get(c, 0) for c in CATEGORIES},
            "non_route_surfaces_by_category": dict(Counter(r["category"] for r in extra)),
            "all_records_by_category": {c: by_cat_all.get(c, 0) for c in CATEGORIES},
            "routes_by_category_and_language": {c: dict(Counter(r["language"] for r in routes if r["category"] == c))
                                                for c in CATEGORIES},
            "by_reason_code": dict(Counter(r["reason_code"] for r in records)),
            "entity_key_basis": dict(Counter(r["entity"]["basis"] for r in records)),
        },
        "migration_impact": {
            "live_surfaces_requesting_indexation_by_category": {c: live_req.get(c, 0) for c in CATEGORIES},
            "stage2_noindex_and_sitemap_removal": stage2_noindex,
            "stage2_urls_deleted_or_redirected": 0,
            "indexable_after_stage2_gate12_minimum": sorted(r["path"] for r in records if r["live"]
                                                            and r["live"]["requests_indexation"] and not r["legacy_hold"]),
            "canonical_knowledge_surfaces": len(canon),
            "canonical_surfaces_with_governed_evidence_today": sorted(with_evidence),
            "consolidation_targets": len(targets),
            "largest_consolidation_targets": targets.most_common(10),
            "knowledge_objects_bound": sorted({r["ko"] for r in records if r["ko"]}),
        },
        "reason_codes": REASON_CODES,
        "governed_evidence_by_concept": {k: sorted(set(v)) for k, v in sorted(inp.evidence_by_concept.items())},
        "record_fields": {
            "registry": "routes.json posture (verbatim)", "ledger": "release_ledger.json record (verbatim subset)",
            "route_id": "joins routes.json (content_file, template, layer, h1 ... stay owned there)",
            "governed_evidence_n": "number of governed evidence records about the concept (see governed_evidence_by_concept)",
            "live": "site/public robots meta + sitemap membership", "gate12": "verdict|S|failure letters|IG units "
            "(N near-duplicate, S structural template, T template prose, B thin body, I information gain)",
            "legacy_hold": "path is in the sealed Gate-12 legacy baseline (Contract C RL eligible)",
            "entity": "concept key + how it was derived (basis) + whether the identity is curated (recognized)"},
    }


def main():
    records, inp = build()
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "legacy_disposition_registry.jsonl"), "w", encoding="utf-8") as fh:
        for r in sorted(records, key=lambda r: (r["record_type"], r["route_id"] or "", r["path"])):
            fh.write(json.dumps(r, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n")
    summary = summarize(records, inp)
    with open(os.path.join(OUT, "legacy_disposition_summary.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(json.dumps(summary["counts"]["all_records_by_category"], indent=1))
    print(json.dumps(summary["migration_impact"], indent=1)[:1500])
    return 0


if __name__ == "__main__":
    sys.exit(main())
