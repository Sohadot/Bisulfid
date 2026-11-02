#!/usr/bin/env python3
"""release_checks_tests.py — the human gates of a reference release cannot be self-granted (Release-01)."""

import copy
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "publication"))
import release_checks as rc  # noqa: E402

FAILS = []
KO = "KO-MOS2-SCIENTIFIC-001"
CLAIMS = rc._ko(KO)["claim_ids"]


def ok(name, cond):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        FAILS.append(name)


GOOD = {"knowledge_object_id": KO, "preparer": "claude-code-agent", "reviews": [{
    "status": "signed", "reviewer": "Dr. Fixture Reviewer", "reviewer_kind": "human", "independence_declared": True,
    "signed_on": "2026-11-01", "claim_verdicts": [{"claim_id": c, "verdict": "confirmed"} for c in CLAIMS], "findings": []}]}


def with_review(**chg):
    r = copy.deepcopy(GOOD)
    r["reviews"][0].update(chg)
    return r


ok("01_complete_independent_human_review_validates", rc.validation_ok(KO, GOOD) == (True, []))
ok("02_no_record_does_not_validate", rc.validation_ok(KO, {"reviews": []})[0] is False)
ok("03_preparer_cannot_review", rc.validation_ok(KO, with_review(reviewer="claude-code-agent"))[0] is False)
ok("04_agent_cannot_review", rc.validation_ok(KO, with_review(reviewer="Claude (automated)", reviewer_kind="agent"))[0] is False)
ok("05_unsigned_review_does_not_count", rc.validation_ok(KO, with_review(status="draft"))[0] is False)
ok("06_partial_claim_coverage_refused",
   rc.validation_ok(KO, with_review(claim_verdicts=[{"claim_id": CLAIMS[0], "verdict": "confirmed"}]))[0] is False)
ok("07_rejected_claim_refused", rc.validation_ok(KO, with_review(claim_verdicts=[{"claim_id": c, "verdict": "rejected"} for c in CLAIMS]))[0] is False)
ok("08_open_finding_refused", rc.validation_ok(KO, with_review(findings=[{"id": "F1", "status": "open"}]))[0] is False)
ok("09_independence_must_be_declared", rc.validation_ok(KO, with_review(independence_declared=False))[0] is False)

srcs = {"S1": {"source_id": "S1", "source_lock_status": "locked"}, "S2": {"source_id": "S2", "source_lock_status": "candidate"}}
signed = {"S1": {"source_id": "S1", "status": "signed", "signed_by": "Registry Owner", "preparer": "claude-code-agent",
                 "checklist": {k: "pass" for k in rc.policy()["source_lock_checklist"]}}}
ok("10_signed_complete_lock_is_honoured", rc.source_lock_ok("S1", signed, srcs) == (True, []))
ok("11_candidate_status_is_not_locked", rc.source_lock_ok("S2", signed, srcs)[0] is False)
ok("12_agent_signed_lock_refused", rc.source_lock_ok("S1", {"S1": dict(signed["S1"], signed_by="claude-code-agent")}, srcs)[0] is False)
ok("13_incomplete_checklist_refused",
   rc.source_lock_ok("S1", {"S1": dict(signed["S1"], checklist=dict(signed["S1"]["checklist"], L6="pending"))}, srcs)[0] is False)

ok("14_no_owner_activation_today", rc.claims_active_ok(KO)[0] is False and rc.release_authorized_ok(KO)[0] is False)
act = [{"knowledge_object_id": KO, "status": "signed", "signed_by": "Site Owner", "signed_on": "2026-11-02", "claim_ids": CLAIMS}]
ok("15_signed_owner_activation_accepted", rc.claims_active_ok(KO, act) == (True, []))
ok("16_activation_must_cover_exact_claims", rc.claims_active_ok(KO, [dict(act[0], claim_ids=CLAIMS[:1])])[0] is False)
ok("17_agent_cannot_activate", rc.claims_active_ok(KO, [dict(act[0], signed_by="claude-code-agent")])[0] is False)

claimed = {"governance_posture": "governed", "evidence_posture": "evidence_locked", "claim_posture": "claim_approved_narrow",
           "validation_posture": "validated", "information_gain_posture": "ig_reviewed_route_realization",
           "release_authorization": "authorized"}
p, notes = rc.honoured_postures(KO, claimed)
ok("18_self_declared_green_postures_are_all_downgraded_today",
   (p["validation_posture"], p["evidence_posture"], p["claim_posture"], p["release_authorization"])
   == ("not_validated", "evidence_sufficient", "claim_pending", "not_authorized") and p["governance_posture"] == "reference_draft"
   and p["information_gain_posture"] == "ig_reviewed_no_new_route" and len(notes) == 6)

# L3 needs two documented retrieval events (capture records: HTTP 200 + SHA-256 + own date) on different dates.
L3_SRC, L3_EVS = "SRC-COD-MOS2-DICKINSON-1923", ["EVD-MOS2-STRUCTURE-DICKINSON"]  # evidence retrieval_date 2026-09-20


def cap(day, status=200, sha="ab" * 32):
    return ("fixture.json", {"url": "https://example.org/x", "http_status": status, "sha256": sha, "retrieved_on": day,
                             "fields": [{"field": "f", "stored": "v", "live": "v", "match": True}]})


def l3(caps):
    return rc.lock_checklist(L3_SRC, L3_EVS, captures=caps)["checklist"]["L3"]


ok("19_one_capture_plus_older_evidence_date_is_not_L3", not l3([cap("2026-10-30")]).startswith("pass"))
ok("20_two_captures_on_the_same_date_are_not_L3", not l3([cap("2026-10-30"), cap("2026-10-30")]).startswith("pass"))
ok("21_failed_or_unhashed_retrieval_does_not_count",
   not l3([cap("2026-10-30"), cap("2026-10-31", status=403)]).startswith("pass")
   and not l3([cap("2026-10-30"), cap("2026-10-31", sha=None)]).startswith("pass"))
ok("22_two_documented_captures_on_different_dates_pass_L3", l3([cap("2026-10-30"), cap("2026-10-31")]) == "pass")
ok("23_mismatch_on_the_later_capture_blocks_L3",
   not l3([cap("2026-10-30"), ("fixture.json", dict(cap("2026-10-31")[1], fields=[{"field": "f", "match": False}]))]).startswith("pass"))
_R03 = [(f, c) for f, c in rc._captures().get(L3_SRC, []) if f.endswith("R03_MOS2_RECAPTURE.json")]
ok("24_real_2026_10_30_capture_alone_plus_evidence_date_is_not_L3",
   len(_R03) == 1 and rc.lock_checklist(L3_SRC, L3_EVS, captures=_R03)["capture_dates"] == ["2026-10-30"]
   and not rc.lock_checklist(L3_SRC, L3_EVS, captures=_R03)["checklist"]["L3"].startswith("pass"))

# Append-only recapture (scripts/reference_production/recapture_mos2_values.py), run offline with a fake fetcher.
import datetime  # noqa: E402
import glob  # noqa: E402
import hashlib  # noqa: E402
import tempfile  # noqa: E402
sys.path.insert(0, os.path.join(HERE, "..", "reference_production"))
import recapture_mos2_values as rm  # noqa: E402

GOOD_BODY = {  # minimal genuine-looking responses carrying the stored values
    "cif": lambda f: ("data_x\n" + "\n".join(f"{k} '{v}'" for k, v in f.items()) + "\n").encode(),
}


def fake_ok(url):
    eid = next(k for k, v in rm.CHECKS.items() if v[0] == url)
    _, kind, fields, _ = rm.CHECKS[eid]
    ev = json.load(open(os.path.join(rm.EV, eid + ".json"), encoding="utf-8"))
    q = ev["locator"]["fields_quoted"]
    if kind == "cif":
        return 200, GOOD_BODY["cif"]({k: q[k] for k in fields})
    if kind == "pubchem":
        return 200, json.dumps({"PropertyTable": {"Properties": [{"CID": 14823, **{k: q[k] for k in fields}}]}}).encode()
    return 200, (f"<html><title>molybdenum disulphide</title> CAS 1317-33-5 Formula: {q['Formula']} "
                 f"Molecular weight: {q['molecularWeight'].split()[0]}</html>").encode()


def fake_blocked(url):
    return 200, b"<html><title>Just a moment...</title>Checking your browser</html>"


def fake_503(url):
    return 503, b"Service Unavailable"


import json  # noqa: E402

with tempfile.TemporaryDirectory() as tmp:
    capd, rawd = os.path.join(tmp, "captures"), os.path.join(tmp, "raw")
    os.makedirs(capd)
    earlier = os.path.join(capd, "R03_MOS2_RECAPTURE.json")
    real = os.path.join(rm.CAPTURES, "R03_MOS2_RECAPTURE.json")
    open(earlier, "wb").write(open(real, "rb").read())
    before = hashlib.sha256(open(earlier, "rb").read()).hexdigest()
    d1 = datetime.datetime(2026, 11, 3, 9, 30, tzinfo=datetime.timezone.utc)
    rc1, p1 = rm.run(now=d1, fetcher=fake_ok, captures_dir=capd, raw_root=rawd)
    ok("25_recapture_writes_a_new_dated_file_and_keeps_earlier_captures",
       rc1 == 0 and p1.endswith("MOS2_RECAPTURE_2026-11-03.json")
       and hashlib.sha256(open(earlier, "rb").read()).hexdigest() == before
       and sorted(os.path.basename(x) for x in glob.glob(os.path.join(capd, "*.json")))
       == ["MOS2_RECAPTURE_2026-11-03.json", "R03_MOS2_RECAPTURE.json"])
    first = open(p1, "rb").read()
    rc2, p2 = rm.run(now=d1.replace(hour=15), fetcher=fake_503, captures_dir=capd, raw_root=rawd)
    ok("26_same_day_recapture_is_refused_and_nothing_is_replaced", rc2 == 2 and p2 is None and open(p1, "rb").read() == first)
    doc = json.load(open(p1, encoding="utf-8"))["captures"]
    cif = doc["EVD-MOS2-STRUCTURE-DICKINSON"]
    nist = doc["EVD-MOS2-FORMULA-NIST"]
    ok("27_capture_records_utc_time_hash_bytes_and_raw_artifact_policy",
       cif["retrieved_at_utc"] == "2026-11-03T09:30:00Z" and len(cif["sha256"]) == 64 and cif["bytes"] > 0
       and hashlib.sha256(open(os.path.join(rm.ROOT, cif["raw_artifact"]), "rb").read()).hexdigest() == cif["sha256"]
       and nist["raw_artifact"] is None and len(nist["sha256"]) == 64)
    rc3, p3 = rm.run(now=d1 + datetime.timedelta(days=1), fetcher=fake_503, captures_dir=capd, raw_root=rawd)
    rc4, p4 = rm.run(now=d1 + datetime.timedelta(days=2), fetcher=fake_blocked, captures_dir=capd, raw_root=rawd)
    bad503 = json.load(open(p3, encoding="utf-8"))["captures"]["EVD-MOS2-STRUCTURE-DICKINSON"]
    badbot = json.load(open(p4, encoding="utf-8"))["captures"]["EVD-MOS2-STRUCTURE-DICKINSON"]
    ok("28_failed_or_anti_bot_responses_get_no_hash_and_exit_nonzero",
       rc3 == 1 and rc4 == 1 and "sha256" not in bad503 and "sha256" not in badbot
       and badbot["content_verified"] is False and bad503["content_verified"] is False)
    real_first = ("R03", json.load(open(real, encoding="utf-8"))["captures"]["EVD-MOS2-STRUCTURE-DICKINSON"])
    ok("29_failed_or_anti_bot_recapture_cannot_pass_L2_or_L3",
       not l3([real_first, ("x", bad503)]).startswith("pass") and not l3([real_first, ("x", badbot)]).startswith("pass")
       and rc.lock_checklist(L3_SRC, L3_EVS, captures=[("x", badbot)])["checklist"]["L2"] != "pass")
    drift = dict(cif, fields=[dict(x, live="9.99", match=False) for x in cif["fields"]])
    ok("29b_genuine_response_with_a_changed_value_blocks_L2_and_L3",
       rc.lock_checklist(L3_SRC, L3_EVS, captures=[real_first, ("new", drift)])["checklist"]["L2"] != "pass"
       and not l3([real_first, ("new", drift)]).startswith("pass"))
    ok("29c_failed_recapture_neither_passes_nor_erases_earlier_L2",
       rc.lock_checklist(L3_SRC, L3_EVS, captures=[real_first, ("x", bad503)])["checklist"]["L2"] == "pass")
    ok("30_two_valid_dated_captures_pass_L3_one_does_not",
       l3([real_first, ("new", cif)]) == "pass" and not l3([("new", cif)]).startswith("pass"))

print("=" * 56)
print("RESULT: " + ("PASS — release gates cannot be self-granted" if not FAILS else f"FAIL — {FAILS}"))
sys.exit(1 if FAILS else 0)
