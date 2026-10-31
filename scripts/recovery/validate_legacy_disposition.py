#!/usr/bin/env python3
"""validate_legacy_disposition.py — invariants of the Recovery-01 legacy disposition registry.

Checks (exit 1 on any violation):
  * every routes.json route has exactly one record; every site/public page without a route has one;
  * every record has exactly one of the six governed recovery categories and a known reason code;
  * route identity and historical release records are preserved verbatim (route_id/path/language,
    routes.json status/indexable, release_ledger subset);
  * consolidation targets exist, are not self-references, and are themselves canonical surfaces
    (never another variant), so a later consolidation cannot chain;
  * a Knowledge Object is only referenced where the governed binding allows it;
  * the registry authorizes nothing: no route is marked published/indexable by it.
"""

import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_legacy_disposition import CATEGORIES, KO_BINDINGS, REASON_CODES  # noqa: E402

CANONICAL_CATEGORIES = {"independent_reference_candidate", "valid_language_or_domain_specific_reference_candidate",
                        "evidence_pending_knowledge_entity", "unresolved_requires_review"}


def main():
    errors = []
    recs = [json.loads(l) for l in open(os.path.join(DATA, "recovery", "legacy_disposition_registry.jsonl"), encoding="utf-8")]
    routes = json.load(open(os.path.join(DATA, "routes.json"), encoding="utf-8"))
    routes = routes if isinstance(routes, list) else routes["routes"]
    ledger = {x["route_id"]: x for x in json.load(open(os.path.join(DATA, "release_ledger.json"), encoding="utf-8"))["records"]}
    by_route = {}
    for r in recs:
        if r["record_type"] == "route":
            if r["route_id"] in by_route:
                errors.append(f"duplicate record for {r['route_id']}")
            by_route[r["route_id"]] = r
    for rt in routes:
        r = by_route.get(rt["route_id"])
        if not r:
            errors.append(f"route {rt['route_id']} has no disposition record")
            continue
        for k in ("path", "language"):
            if r[k] != rt[k]:
                errors.append(f"{rt['route_id']}: {k} not preserved")
        if r["registry"] != {"status": rt["status"], "indexable": rt["indexable"]}:
            errors.append(f"{rt['route_id']}: routes.json posture not preserved")
        lg = ledger.get(rt["route_id"], {})
        if any(r["ledger"].get(k) != lg.get(k) for k in ("release_status", "public_status", "indexable", "sitemap_file")):
            errors.append(f"{rt['route_id']}: release record not preserved verbatim")
    if len(by_route) != len(routes):
        errors.append(f"{len(by_route)} route records for {len(routes)} routes")
    route_paths = {rt["path"] for rt in routes}
    html = set()
    pub = os.path.join(ROOT, "site", "public")
    for dp, dn, fn in os.walk(pub):
        if os.path.abspath(dp) == os.path.abspath(pub):
            dn[:] = [d for d in dn if d not in ("_integration_sample", "_visual_proof_sample", "assets")]
        if "index.html" in fn:
            rel = os.path.relpath(dp, pub)
            html.add("/" if rel == "." else "/" + rel.replace(os.sep, "/") + "/")
    extra = {r["path"] for r in recs if r["record_type"] == "non_route_legacy_surface"}
    if extra != html - route_paths:
        errors.append(f"non-route surface records {len(extra)} != {len(html - route_paths)} public pages without a route")
    keyed = {(r["route_id"] or r["path"]): r for r in recs}
    for r in recs:
        rid = r["route_id"] or r["path"]
        if r["category"] not in CATEGORIES:
            errors.append(f"{rid}: unknown category {r['category']}")
        if r["reason_code"] not in REASON_CODES:
            errors.append(f"{rid}: unknown reason code {r['reason_code']}")
        if r["target"] is not None:
            t = keyed.get(r["target"])
            if t is None:
                errors.append(f"{rid}: target {r['target']} does not exist")
            elif r["target"] == rid:
                errors.append(f"{rid}: self-targeting")
            elif t["category"] not in CANONICAL_CATEGORIES:
                errors.append(f"{rid}: target {r['target']} is not a canonical surface ({t['category']})")
        if r["ko"] and not (r["route_id"] in KO_BINDINGS or (r["category"] == "module_of_existing_knowledge_object"
                                                               and r["target"] in KO_BINDINGS)):
            errors.append(f"{rid}: references {r['ko']} without a governed binding")
        if r["category"] == "duplicate_or_redundant_presentation_surface" and r["reason_code"] != "INTERNAL_PIPELINE_STATUS" \
                and r["target"] is None:
            errors.append(f"{rid}: redundant surface without a consolidation target")
        if r["registry"] and (r["registry"]["status"] != "planned" or r["registry"]["indexable"]):
            errors.append(f"{rid}: registry posture changed (the disposition registry authorizes nothing)")
    print(f"legacy disposition registry: {len(recs)} records ({len(by_route)} routes + {len(extra)} non-route surfaces); "
          f"{len(errors)} violation(s)")
    for e in errors[:50]:
        print("  " + e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
