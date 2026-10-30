#!/usr/bin/env python3
"""build_seo_disposition.py — Recovery-02 per-URL SEO migration disposition (PROPOSALS ONLY).

Maps every Recovery-01 legacy disposition record (14,041 URLs) to one SEO class and one recommended
action, using measured signals rather than category alone:

  true_duplicate_valid_canonical     same-language variant whose canonical destination is live, served
                                     "index, follow", self-canonical, and RAW (un-masked) substantive
                                     similarity >= 0.80 to the variant -> rel=canonical, NOT noindex
  duplicate_without_valid_canonical  a variant whose destination fails one of those checks -> status quo
  needs_reconstruction               canonical surface of a curated concept, no Knowledge Object yet
  independent_reference_potential    governed KO / language-specific object bound to the route
  institutional_navigation           Gate 12-I institutional surfaces and internal pipeline-status pages
  generated_unverified_identity      combinatorially generated entity names (canonical + their variants)
  unmatched_non_route                public HTML with no route record and no concept match

Nothing here is applied. Approved per-URL decisions go to main/data/publication/url_decisions.json.
Inputs: main/data/recovery/legacy_disposition_registry.jsonl, site/public, routes.json.
Outputs: main/data/recovery/seo_url_disposition.jsonl + seo_url_disposition_summary.json.
"""

import json
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
sys.path.insert(0, os.path.join(ROOT, "scripts", "validators"))
import distinctiveness_core as dc  # noqa: E402

CANONICAL_MIN_RAW_SIMILARITY = 0.80
# Brand/identity surfaces: likely candidates for the 3 URLs Search Console reported as indexed
# (which 3 is UNKNOWN). They are never noindexed without the Search Console page export.
BRAND_PATHS = {"/", "/de/", "/bisulfid/", "/what-is-bisulfid/", "/de/what-is-bisulfid/", "/bisulfid-vs-bisulfide/",
               "/de/bisulfid-vs-bisulfide/", "/en/terminology/bisulfid/term/chem/acad/"}

ACTION = {
    "true_duplicate_valid_canonical": "rel_canonical_to_target (head-only; keeps the URL reachable; no noindex)",
    "duplicate_without_valid_canonical": "status_quo until the destination is rebuilt or a valid destination exists",
    "needs_reconstruction": "status_quo, then rebuild in place from a Knowledge Object (priority = governed evidence)",
    "independent_reference_potential": "rebuild in place; promote only via Contract C (preview exists for MoS2)",
    "institutional_navigation": "re-render (Gate 12-I) and certify via Contract C R11; duplicates canonicalize to the holder",
    "internal_pipeline_status": "targeted noindex candidate (internal build state; no search intent)",
    "generated_unverified_identity": "identity review first; then rebuild (entity exists) or retire with its variants (it does not)",
    "unmatched_non_route": "register as a route (if it is the better URL for a concept) or retire after link review",
}


STAGE2_APPROPRIATE = {
    "true_duplicate_valid_canonical": "no: use rel=canonical (consolidates signals; noindex discards them)",
    "duplicate_without_valid_canonical": "no: wait for a valid destination",
    "needs_reconstruction": "no: canonical concept surface; rebuild instead",
    "independent_reference_potential": "no",
    "institutional_navigation": "no for holders; canonical for duplicates",
    "internal_pipeline_status": "yes (targeted, after review)",
    "generated_unverified_identity": "only after identity review shows the entity does not exist",
    "unmatched_non_route": "no: decide register vs retire first",
}


def main():
    recs = [json.loads(l) for l in open(os.path.join(DATA, "recovery", "legacy_disposition_registry.jsonl"), encoding="utf-8")]
    routes = json.load(open(os.path.join(DATA, "routes.json"), encoding="utf-8"))
    routes = routes if isinstance(routes, list) else routes["routes"]
    path_of = {r["route_id"]: r["path"] for r in routes}
    policy = dc.load_policy()
    surface = os.path.join(ROOT, "site", "public")
    pages = {dc.surface_url_path(p, surface): p for p in dc.load_html_pages(policy, surface)}
    key_of = {(r["route_id"] or r["path"]): r for r in recs}
    # A short non-route URL that already exists for the same concept is a better canonical URL.
    nonroute_by_concept = defaultdict(list)
    for r in recs:
        if r["record_type"] != "route":
            nonroute_by_concept[(r["entity"]["key"], r["language"])].append(r["path"])

    out = []
    for r in recs:
        code = r["reason_code"]
        path = r["path"]
        tgt_path = None
        sim = None
        checks = {}
        if r["target"]:
            tgt_path = path_of.get(r["target"], r["target"] if str(r["target"]).startswith("/") else None)
        if code in ("GOVERNED_KO_BINDING", "GOVERNED_LEXICAL_BINDING"):
            cls = "independent_reference_potential"
        elif code == "INTERNAL_PIPELINE_STATUS":
            cls = "internal_pipeline_status"
        elif code in ("INSTITUTIONAL_GATE12I_REVIEW", "DUPLICATE_INSTITUTIONAL_FUNCTION"):
            cls = "institutional_navigation"
        elif code == "CANONICAL_CURATED_CONCEPT_NO_KO":
            cls = "needs_reconstruction"
        elif code == "GENERATED_ENTITY_IDENTITY_UNVERIFIED" or r["entity"]["key"].startswith(("generated:", "de:")) \
                and not r["entity"]["recognized"]:
            cls = "generated_unverified_identity"
        elif code == "NON_ROUTE_SURFACE_UNMATCHED":
            cls = "unmatched_non_route"
        else:  # VARIANT_OF_CANONICAL, MODULE_OF_KNOWLEDGE_OBJECT, DUPLICATE_OF_GOVERNED_LEXICAL_OBJECT
            a, b = pages.get(path), pages.get(tgt_path)
            checks = {"target_live": b is not None,
                      "target_served_index": bool(b) and "noindex" not in (b.robots or "noindex"),
                      "target_self_canonical": bool(b) and dc.surface_url_path(b, surface) == (
                          (b.canonical or "").replace("https://bisulfid.com", "") or None)}
            if a is not None and b is not None:
                sim = round(dc.similarity(a.raw_shingle_set, b.raw_shingle_set, 20)[0], 4)
            checks["raw_similarity_ok"] = sim is not None and sim >= CANONICAL_MIN_RAW_SIMILARITY
            cls = "true_duplicate_valid_canonical" if all(checks.values()) else "duplicate_without_valid_canonical"
        if cls == "institutional_navigation" and code == "DUPLICATE_INSTITUTIONAL_FUNCTION":
            action = "rel_canonical_to_holder after the holder is re-rendered and passes Gate 12-I"
        else:
            action = ACTION[cls]
        rec = {"path": path, "route_id": r["route_id"], "seo_class": cls,
               "canonical_destination": tgt_path, "raw_similarity_to_destination": sim}
        if action != ACTION[cls]:
            rec["recommended_action"] = action
        if checks and not all(checks.values()):
            rec["failed_canonical_checks"] = [k for k, v in checks.items() if not v]
        better = nonroute_by_concept.get((r["entity"]["key"], r["language"]))
        if better and r["record_type"] == "route" and cls in ("needs_reconstruction", "true_duplicate_valid_canonical"):
            rec["shorter_existing_url_for_concept"] = better
        if path in BRAND_PATHS:
            rec["risk"] = "brand_or_identity_surface: never noindex without the Search Console indexed-page export"
        rec["stage2_would_noindex"] = bool(r["legacy_hold"]) and bool((r["live"] or {}).get("requests_indexation"))
        out.append(rec)

    with open(os.path.join(DATA, "recovery", "seo_url_disposition.jsonl"), "w", encoding="utf-8") as fh:
        for rec in sorted(out, key=lambda x: x["path"]):
            fh.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n")
    by_cls = Counter(x["seo_class"] for x in out)
    stage2 = Counter(x["seo_class"] for x in out if x["stage2_would_noindex"])
    fails = Counter(f for x in out for f in x.get("failed_canonical_checks", []))
    sims = sorted(x["raw_similarity_to_destination"] for x in out if x["raw_similarity_to_destination"] is not None)
    summary = {
        "registry_id": "RECOVERY-02-SEO-URL-DISPOSITION", "version": "1.0.0",
        "generated_by": "scripts/recovery/build_seo_disposition.py",
        "authorizes": "nothing — proposals only; approved decisions live in main/data/publication/url_decisions.json",
        "canonical_min_raw_similarity": CANONICAL_MIN_RAW_SIMILARITY,
        "urls": len(out), "by_seo_class": dict(by_cls),
        "stage2_noindex_by_seo_class": dict(stage2),
        "stage2_noindex_judged_appropriate": sum(v for k, v in stage2.items() if k == "internal_pipeline_status"),
        "stage2_noindex_judged_inappropriate_or_premature": sum(v for k, v in stage2.items() if k != "internal_pipeline_status"),
        "brand_surfaces_stage2_would_noindex": sorted(x["path"] for x in out if x.get("risk") and x["stage2_would_noindex"]),
        "canonical_check_failures": dict(fails),
        "raw_similarity_variant_to_destination": {
            "n": len(sims), "min": sims[0] if sims else None, "median": sims[len(sims) // 2] if sims else None,
            "share_ge_0_80": round(sum(1 for s in sims if s >= 0.80) / len(sims), 4) if sims else None},
        "concepts_with_shorter_existing_url": sorted({x["route_id"] for x in out if x.get("shorter_existing_url_for_concept")
                                                      and x["seo_class"] == "needs_reconstruction"}),
        "actions": ACTION,
        "stage2_appropriate_by_class": STAGE2_APPROPRIATE,
        "record_fields": "path, route_id (joins routes.json and legacy_disposition_registry.jsonl), seo_class "
                         "(recommended action = actions[seo_class] unless recommended_action is set), canonical_destination, "
                         "raw_similarity_to_destination, failed_canonical_checks, shorter_existing_url_for_concept, risk, "
                         "stage2_would_noindex",
    }
    with open(os.path.join(DATA, "recovery", "seo_url_disposition_summary.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(json.dumps({k: summary[k] for k in ("by_seo_class", "stage2_noindex_by_seo_class",
                                              "brand_surfaces_stage2_would_noindex", "canonical_check_failures",
                                              "raw_similarity_variant_to_destination")}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
