"""route_realization.py — verify the IG posture ig_reviewed_route_realization (policy 1.1.0).

A governed Knowledge Object may replace the body of its OWN existing canonical route. This module checks
the four conditions of AMD-IG-R03-001 rev 2 against the governed stores and returns (ok, reasons).
It is fail-closed: any missing input is a reason. It never authorizes a new or sibling URL, and still
indexable legacy duplicates are NOT a reason (they must be listed as consolidation obligations instead).
"""

import glob
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
POSTURE = "ig_reviewed_route_realization"


def _load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


class Stores:
    """Everything the check reads; tests substitute fields to build adversarial cases."""

    def __init__(self):
        self.policy = _load(os.path.join(DATA, "information_gain", "ig_governance_policy.json"))
        self.pairs = _load(os.path.join(DATA, "information_gain", "calibration_pairs.json"))["pairs"]
        self.kos = {k["knowledge_object_id"]: k for k in
                    _load(os.path.join(DATA, "knowledge_objects", "knowledge_object_registry.json"))["knowledge_objects"]}
        self.specs = [_load(f) for f in sorted(glob.glob(os.path.join(DATA, "reference_production", "render_specs", "KO-*.json")))]
        routes = _load(os.path.join(DATA, "routes.json"))
        self.routes = {r["route_id"]: r for r in (routes if isinstance(routes, list) else routes["routes"])}
        self.baseline_paths = {e["p"] for e in _load(os.path.join(DATA, "distinctiveness", "legacy_surface_hold.json"))["entries"]}
        self.obligations = _load(os.path.join(DATA, "publication", "consolidation_obligations.json"))["obligations"]
        self.records = [json.loads(line) for line in
                        open(os.path.join(DATA, "recovery", "legacy_disposition_registry.jsonl"), encoding="utf-8")]


def known_duplicates(ko_id, route, records):
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "bco", os.path.join(ROOT, "scripts", "publication", "build_consolidation_obligations.py"))
    bco = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bco)
    return set(bco.duplicates_for(ko_id, route, records))


def ratified(policy):
    """AMD-IG-R03-001 counts only with a recorded owner ratification: status 'ratified', a named
    human in ratified_by (never an automated agent) and a date. Opening or merging a PR is not one."""
    amend = next((a for a in policy.get("amendments", []) if a.get("amendment_id") == "AMD-IG-R03-001"), None)
    who = ((amend or {}).get("ratified_by") or "").lower()
    return (POSTURE in policy.get("posture_ids", []) and bool(amend) and amend.get("status") == "ratified"
            and bool(who) and not any(x in who for x in ("claude", "agent", "automated")) and bool(amend.get("ratified_on")))


def check(ko_id, stores=None):
    """Full check used by the publication authority: ratification AND the four structural conditions."""
    s = stores or Stores()
    good, reasons = check_structure(ko_id, s)
    if not ratified(s.policy):
        reasons = ["policy: AMD-IG-R03-001 (ig_reviewed_route_realization) awaits owner ratification"] + reasons
    return (good and not reasons), reasons


def check_structure(ko_id, stores=None):
    """The four structural conditions only (what validators verify before ratification)."""
    s = stores or Stores()
    reasons = []
    ko = s.kos.get(ko_id)
    if not ko:
        return False, reasons + [f"unknown Knowledge Object {ko_id}"]
    bound = [x for x in s.specs if x.get("knowledge_object_id") == ko_id]
    if len(bound) != 1:
        return False, reasons + [f"{ko_id}: must be bound by exactly one render spec (found {len(bound)})"]
    route_id = bound[0].get("canonical_route_id")
    route = s.routes.get(route_id)
    # (1) governing pair: KO vs its own route, near_duplicate
    gov = (ko.get("ig_resolution") or {}).get("new_route_governing_comparison")
    pair = next((p for p in s.pairs if p.get("pair_id") == gov), None)
    if not pair or pair.get("object_a") != ko_id or pair.get("route_b") != route_id \
            or pair.get("expected_classification") != "near_duplicate":
        reasons.append(f"{ko_id}: governing pair must compare the KO with its own route {route_id} as near_duplicate")
    # (2) no other KO binds the same route
    others = [x["knowledge_object_id"] for x in s.specs if x.get("canonical_route_id") == route_id
              and x.get("knowledge_object_id") != ko_id]
    if others:
        reasons.append(f"route {route_id} is also bound by {others}")
    # (3) the route already exists publicly at an unchanged path
    if not route:
        return False, reasons + [f"route {route_id} is not in routes.json (a new URL cannot be realized)"]
    if route["path"] not in s.baseline_paths:
        reasons.append(f"{route['path']} is not a sealed legacy public URL: realization never creates a URL")
    # (4) every known same-task duplicate carries a consolidation obligation (it does not block)
    obl = {o["duplicate_path"] for o in s.obligations
           if o.get("knowledge_object_id") == ko_id and o.get("destination_path") == route["path"]
           and o.get("action") in ("canonical_to", "noindex") and o.get("blocks_realization") is False}
    if any(o.get("duplicate_path") == route["path"] for o in s.obligations if o.get("knowledge_object_id") == ko_id):
        reasons.append("an obligation may not target the realized route itself")
    missing = sorted(known_duplicates(ko_id, route, s.records) - obl)
    if missing:
        reasons.append(f"{len(missing)} same-task duplicate(s) without a consolidation obligation, e.g. {missing[:2]}")
    return not reasons, reasons
