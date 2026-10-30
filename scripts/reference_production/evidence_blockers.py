#!/usr/bin/env python3
"""evidence_blockers.py — exact evidence blockers for a reference plan (Recovery-02).

For every module claim in a plan (main/data/reference_production/plans/<PLAN>.json) it checks the real
governance stores, in admission order, and reports the FIRST missing step and all later ones:
  1 claim exists            main/data/claims/*.json, main/data/pilots/*claims.json
  2 claim approved          status approved | approved_narrow (Contract C claim input)
  3 source verified         source_registry status verified (identity checklist)
  4 source-use qualified    source_use_qualification_registry entry in an admitting state
  5 evidence record         main/data/evidence/EVD-*.json bound to the claim and source
  6 evidence admitted       source_admissibility.admissible() for the record's intended use
  7 evidence verified       evidence_review_posture = evidence_verified
A module is renderable only when every claim passes 1-7. Writes
main/data/reference_production/blockers/<PLAN>_BLOCKERS.json and prints a summary. Never writes content.
"""

import glob
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
sys.path.insert(0, os.path.join(ROOT, "scripts", "governance_scaffolding"))
import source_admissibility as sa  # noqa: E402

APPROVED = ("approved", "approved_narrow")


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def stores():
    claims = {}
    for f in glob.glob(os.path.join(DATA, "claims", "*.json")) + glob.glob(os.path.join(DATA, "pilots", "*claims.json")):
        for c in (load(f).get("claims") or []):
            if isinstance(c, dict) and c.get("claim_id"):
                claims[c["claim_id"]] = c
    srcd = load(os.path.join(DATA, "sources", "source_registry.json"))
    sources = {s["source_id"]: s for s in (srcd.get("sources") if isinstance(srcd, dict) else srcd)}
    q = load(os.path.join(DATA, "source_use_qualification_registry.json"))
    quals = q.get("qualifications", q)
    evidence = [load(f) for f in glob.glob(os.path.join(DATA, "evidence", "EVD-*.json"))]
    return claims, sources, quals, evidence


def claim_blockers(cid, claims, sources, quals, evidence, adm):
    steps = []
    c = claims.get(cid)
    if not c:
        return [{"step": 1, "blocker": f"claim {cid} does not exist"}]
    status = c.get("status") or c.get("outcome")
    if status not in APPROVED:
        steps.append({"step": 2, "blocker": f"claim status is '{status}', not approved/approved_narrow",
                      "required": "claim review against admitted evidence (owner: claim registry)"})
    for sid in c.get("source_ids") or []:
        s = sources.get(sid)
        if not s:
            steps.append({"step": 3, "source_id": sid, "blocker": "source not registered"})
            continue
        if s.get("status") != "verified":
            steps.append({"step": 3, "source_id": sid, "blocker": f"source status '{s.get('status')}' (lock '{s.get('source_lock_status')}')",
                          "required": "identity verification per main/data/SOURCE_IDENTITY_VERIFICATION_CHECKLIST.md "
                                      "(publisher, title, URL/DOI, retrieval date, captured locator)"})
        sq = [x for x in quals if x["source_id"] == sid]
        if not sq:
            steps.append({"step": 4, "source_id": sid, "blocker": "no source-use qualification",
                          "required": f"qualification record with allowed_uses for this claim (source use_for: {s.get('use_for')})"})
        ev = [e for e in evidence if e.get("source_id") == sid and e.get("claim_id") == cid]
        if not ev:
            steps.append({"step": 5, "source_id": sid, "blocker": "no evidence record",
                          "required": "EVD record: claim_scope, locator with the verbatim passage, retrieval_date, "
                                      "allowed_uses/prohibited_uses, governed=true"})
        for e in ev:
            ok = False
            for qq in sq:
                for use in e.get("allowed_uses", []):
                    unit, reason = sa.build_admission_unit(e, qq["qualification_id"], use, adm)
                    ok = ok or unit["admitted"]
            if not ok:
                steps.append({"step": 6, "evidence_id": e["evidence_id"], "blocker": "not admitted by admissible()"})
            if e.get("evidence_review_posture") != "evidence_verified":
                steps.append({"step": 7, "evidence_id": e["evidence_id"], "blocker": "evidence not verified"})
    if not c.get("source_ids"):
        steps.append({"step": 3, "blocker": "claim cites no source"})
    return steps


def main(argv=None):
    plan_path = (argv or sys.argv[1:] or [os.path.join(DATA, "reference_production", "plans", "PLAN-BISULFID-BISULFIDE-BOUNDARY.json")])[0]
    plan = load(plan_path)
    claims, sources, quals, evidence = stores()
    adm = sa.load_all()
    modules = []
    for m in plan["modules"]:
        per = {cid: claim_blockers(cid, claims, sources, quals, evidence, adm) for cid in m["claim_ids"]}
        modules.append({"module_id": m["module_id"], "heading": m["heading"], "renderable": not any(per.values()),
                        "claims": {cid: {"status": (claims.get(cid) or {}).get("status"), "blockers": b} for cid, b in per.items()}})
    renderable = [m for m in modules if m["renderable"]]
    out = {"plan_id": plan["plan_id"], "canonical_route_id": plan["canonical_route_id"],
           "renderable_modules": len(renderable), "modules": modules,
           "verdict": "RENDERABLE" if len(renderable) >= 3 else "BLOCKED_ON_EVIDENCE",
           "note": "A preview is produced only when >= 3 modules are renderable; no prose is written around missing evidence."}
    dest = os.path.join(DATA, "reference_production", "blockers", plan["plan_id"] + "_BLOCKERS.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    n_claims = sum(len(m["claims"]) for m in modules)
    steps = {}
    for m in modules:
        for b in m["claims"].values():
            for s in b["blockers"]:
                steps[s["step"]] = steps.get(s["step"], 0) + 1
    print(f"{plan['plan_id']}: {len(renderable)}/{len(modules)} modules renderable; {n_claims} claim bindings; "
          f"blockers by step {dict(sorted(steps.items()))} -> {out['verdict']}")
    return 0 if out["verdict"] == "RENDERABLE" else 3


if __name__ == "__main__":
    sys.exit(main())
