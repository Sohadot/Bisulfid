#!/usr/bin/env python3
"""route_realization_tests.py — AMD-IG-R03-001 rev 2 (IG policy 1.1.0): positive and adversarial proofs.

A governed Knowledge Object may replace its OWN existing canonical route; it may never create or bless a
sibling URL; still-indexable legacy duplicates create consolidation obligations instead of blocking.
"""

import copy
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "publication"))
import contract_c_derive as cc  # noqa: E402
import route_realization as rr  # noqa: E402

FAILS = []
BASE = rr.Stores()
KOS = ("KO-MOS2-SCIENTIFIC-001", "KO-BISULFID-TERMINOLOGY-001")


def ok(name, cond):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        FAILS.append(name)


def variant(**changes):
    s = copy.copy(BASE)
    for k, v in changes.items():
        setattr(s, k, v)
    return s


def refused(ko, stores, fragment):
    good, why = rr.check(ko, stores)
    return (not good) and any(fragment in w for w in why)


# --- positive
for ko in KOS:
    ok(f"01_{ko}_realizes_its_own_route", rr.check(ko, BASE) == (True, []))
ok("02_posture_normalizes_to_ig_passed_only_via_alias", cc._IG_NORMALIZE["ig_reviewed_route_realization"] == "ig_passed"
   and "ig_reviewed_route_realization" not in cc._IG_ROUTE_ELIGIBLE)
ok("03_contract_c_still_needs_every_other_input",
   cc.derive(governance="reference_draft", evidence="evidence_sufficient", claim="claim_pending", validation="not_validated",
             ig="ig_reviewed_route_realization", release="not_authorized") == ("not_public", "noindex"))
ok("04_indexable_duplicates_do_not_block (no circular prerequisite)",
   all(r["live"] and r["live"]["requests_indexation"] for r in BASE.records
       if r["path"] in {o["duplicate_path"] for o in BASE.obligations}) and rr.check(KOS[0], BASE)[0])
ok("05_every_obligation_is_non_blocking_and_open",
   all(o["blocks_realization"] is False and o["status"] == "open" for o in BASE.obligations))

# --- adversarial
specs_new_route = [dict(x, canonical_route_id="brand_new_route") if x["knowledge_object_id"] == KOS[0] else x for x in BASE.specs]
routes_new = dict(BASE.routes, brand_new_route={"route_id": "brand_new_route", "path": "/new-mos2-page/", "language": "en"})
ok("10_new_url_refused", refused(KOS[0], variant(specs=specs_new_route, routes=routes_new), "governing pair")
   and refused(KOS[0], variant(specs=specs_new_route, routes=routes_new), "not a sealed legacy public URL"))
sib = [dict(x, canonical_route_id="de_core_mos2") if x["knowledge_object_id"] == KOS[0] else x for x in BASE.specs]
ok("11_sibling_route_refused", refused(KOS[0], variant(specs=sib), "governing pair"))
dup_spec = BASE.specs + [dict(BASE.specs[0])]
ok("12_two_specs_for_one_ko_refused", refused(BASE.specs[0]["knowledge_object_id"], variant(specs=dup_spec), "exactly one render spec"))
squat = BASE.specs + [{"knowledge_object_id": "KO-OTHER", "canonical_route_id": "molybdenum_disulfide"}]
ok("13_second_ko_on_same_route_refused", refused(KOS[0], variant(specs=squat), "also bound by"))
pairs = [dict(p, expected_classification="valid_domain_specific_reference")
         if p["pair_id"] == "PAIR-KO-MOS2-SCI-vs-LEGACY-SCI-ROUTE" else p for p in BASE.pairs]
ok("14_non_near_duplicate_pair_refused", refused(KOS[0], variant(pairs=pairs), "governing pair"))
first = next(i for i, o in enumerate(BASE.obligations) if o["knowledge_object_id"] == KOS[0])
ok("15_missing_obligation_refused", refused(KOS[0], variant(obligations=BASE.obligations[:first] + BASE.obligations[first + 1:]),
                                            "without a consolidation obligation"))
blocking = [dict(o, blocks_realization=True) if i == first else o for i, o in enumerate(BASE.obligations)]
ok("16_obligation_marked_blocking_refused", refused(KOS[0], variant(obligations=blocking), "without a consolidation obligation"))
selfobl = BASE.obligations + [{"knowledge_object_id": KOS[0], "duplicate_path": "/molybdenum-disulfide/",
                               "destination_path": "/molybdenum-disulfide/", "action": "canonical_to", "blocks_realization": False}]
ok("17_obligation_on_the_route_itself_refused", refused(KOS[0], variant(obligations=selfobl), "route itself"))
pol = copy.deepcopy(BASE.policy)
pol["amendments"][0]["status"] = "proposed"
ok("18_unratified_policy_refused", refused(KOS[0], variant(policy=pol), "not a ratified posture"))
ok("19_unknown_ko_refused", rr.check("KO-DOES-NOT-EXIST", BASE)[0] is False)

# --- authority integration: fail closed, never a sibling
import publication_authority as pa  # noqa: E402
a = pa.Authority()
bound_paths = set(a.postures)
ok("20_authority_binds_only_spec_routes", {"/molybdenum-disulfide/", "/bisulfid-vs-bisulfide/"} <= bound_paths
   and not any(p.startswith("/en/terminology/") for p in bound_paths))
_orig_load = pa._load


def _pc_realizing(path, default=None):  # every PC claims route realization, as D/E will
    d = _orig_load(path, default)
    if isinstance(d, dict) and "publication_candidate_id" in d:
        d = dict(d, postures=dict(d["postures"], information_gain_posture=rr.POSTURE))
    return d


pa._load = _pc_realizing
try:
    good = pa.Authority()
    bad = pa.Authority()
    bad._rr = variant(obligations=[])
    bad.postures = dict(bad._governed_postures(pa.CERTIFICATIONS_PATH))
finally:
    pa._load = _orig_load
ok("21a_verified_realization_reaches_contract_c_as_ig_pass",
   all(i["ig"] == rr.POSTURE for p, (i, _) in good.postures.items() if p in ("/molybdenum-disulfide/", "/bisulfid-vs-bisulfide/")))
ok("21b_authority_fails_closed_when_check_fails",
   all(i["ig"] == "ig_reviewed_no_new_route" and "route realization refused" in b
       for p, (i, b) in bad.postures.items() if p in ("/molybdenum-disulfide/", "/bisulfid-vs-bisulfide/")))
ok("22_obligations_never_change_a_directive", all(a.resolve(o["duplicate_path"])["basis"] == "legacy_status_quo"
                                                  for o in BASE.obligations[:5]))

print("=" * 56)
print("RESULT: " + ("PASS — route realization holds (positive + adversarial)" if not FAILS else f"FAIL — {FAILS}"))
sys.exit(1 if FAILS else 0)
