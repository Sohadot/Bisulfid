#!/usr/bin/env python3
"""build_consolidation_obligations.py — Release-01: consolidation obligations for route realization.

When a governed Knowledge Object realizes its own existing canonical route (IG posture
ig_reviewed_route_realization), every same-task legacy duplicate of that route becomes an OBLIGATION:
it must later be consolidated onto the route (canonical_to). The obligation is recorded, never executed
here, and it never blocks the realization (that would be circular: duplicates can only be consolidated
onto an index-approved destination).

Duplicates are taken from the Recovery-01 disposition registry: same-language records whose target is the
KO's canonical route_id or whose KO binding is the KO (MODULE_OF_KNOWLEDGE_OBJECT, VARIANT_OF_CANONICAL).

Output: main/data/publication/consolidation_obligations.json (deterministic). --check exits 1 if stale.
"""

import glob
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
OUT = os.path.join(DATA, "publication", "consolidation_obligations.json")
DUP_CODES = ("MODULE_OF_KNOWLEDGE_OBJECT", "VARIANT_OF_CANONICAL")


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def duplicates_for(ko_id, route, records):
    return sorted(r["path"] for r in records
                  if r["reason_code"] in DUP_CODES and r["path"] != route["path"] and r["language"] == route["language"]
                  and (r.get("target") == route["route_id"] or r.get("ko") == ko_id))


def build():
    routes = load(os.path.join(DATA, "routes.json"))
    routes = {r["route_id"]: r for r in (routes if isinstance(routes, list) else routes["routes"])}
    records = [json.loads(line) for line in open(os.path.join(DATA, "recovery", "legacy_disposition_registry.jsonl"), encoding="utf-8")]
    out = []
    for f in sorted(glob.glob(os.path.join(DATA, "reference_production", "render_specs", "KO-*.json"))):
        spec = load(f)
        route = routes[spec["canonical_route_id"]]
        for i, path in enumerate(duplicates_for(spec["knowledge_object_id"], route, records), 1):
            out.append({"obligation_id": f"OBL-{spec['knowledge_object_id']}-{i:03d}",
                        "knowledge_object_id": spec["knowledge_object_id"], "destination_route_id": route["route_id"],
                        "destination_path": route["path"], "duplicate_path": path, "action": "canonical_to",
                        "status": "open",
                        "executable_when": "destination Contract C = (public_indexable, index_approved) AND the destination "
                                           "is served with the KO body AND an approved url_decisions.json canonical_to record "
                                           "exists for the duplicate",
                        "blocks_realization": False})
    return {"registry_id": "CONSOLIDATION-OBLIGATIONS", "version": "1.0.0",
            "governed_by": ["main/data/information_gain/ig_governance_policy.json (1.1.0, ig_reviewed_route_realization)",
                            "scripts/publication/build_consolidation_obligations.py", "DECISION_LOG.md"],
            "purpose": "Same-task legacy duplicates of a route realized by a Knowledge Object. Each is a duty to consolidate "
                       "AFTER the destination is index-approved. Not read by the publication authority: nothing here "
                       "changes a directive.",
            "obligations": out}


def main(argv=None):
    mode = (argv or sys.argv[1:] or ["--check"])[0]
    text = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    cur = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else None
    if mode == "--write":
        if cur != text:
            open(OUT, "w", encoding="utf-8").write(text)
        print(f"consolidation obligations: {len(json.loads(text)['obligations'])}")
        return 0
    print("up to date" if cur == text else "STALE: re-run --write")
    return 0 if cur == text else 1


if __name__ == "__main__":
    sys.exit(main())
