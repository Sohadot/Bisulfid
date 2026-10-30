"""release_checks.py — fail-closed checks for the two human postures of a reference release (Release-01).

  validation_ok(ko_id)        a signed, independent, complete review exists (policy validation_rule)
  source_lock_ok(source_id)   a signed L1–L6 lock record exists (policy lock_rule)
  evidence_locked_ok(ko_id)   every source behind the KO's bound evidence is honoured as locked
  lock_checklist(source_id)   machine-checkable L1–L5 status per source (L6 is always a human signature)

The preparer of an object is never accepted as its reviewer or lock signer, and automated agents are
never accepted as either.
"""

import glob
import json
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "main", "data")


def _load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as fh:
        return json.load(fh)


def policy():
    return _load("release", "release_review_policy.json")


def _ko(ko_id):
    return next((k for k in _load("knowledge_objects", "knowledge_object_registry.json")["knowledge_objects"]
                 if k["knowledge_object_id"] == ko_id), None)


def _is_agent(name, pol):
    n = (name or "").lower()
    return not n or any(a in n for a in pol["automated_preparer_ids"]) or "claude" in n or "agent" in n


def review_record(ko_id):
    p = os.path.join(DATA, "release", "reviews", f"{ko_id}.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None


def validation_ok(ko_id, record=None):
    pol, ko = policy(), _ko(ko_id)
    rec = record if record is not None else review_record(ko_id)
    if not ko or not rec:
        return False, ["no review record"]
    why = []
    claims = set(ko["claim_ids"])
    signed = [r for r in rec.get("reviews", []) if r.get("status") == "signed"]
    if not signed:
        why.append("no signed review")
    for r in signed:
        bad = []
        if r.get("reviewer_kind") != "human" or _is_agent(r.get("reviewer"), pol):
            bad.append("reviewer is not a named human")
        if r.get("reviewer") in (rec.get("preparer"), None) or r.get("reviewer") == rec.get("preparer_id"):
            bad.append("reviewer is the preparer")
        if not r.get("independence_declared"):
            bad.append("independence not declared")
        if not r.get("signed_on"):
            bad.append("no signature date")
        verdicts = {v["claim_id"]: v.get("verdict") for v in r.get("claim_verdicts", [])}
        if set(verdicts) != claims:
            bad.append(f"claims not all reviewed ({len(set(verdicts) & claims)}/{len(claims)})")
        if any(v != "confirmed" for v in verdicts.values()):
            bad.append("a claim is not confirmed")
        if any(f.get("status") != "resolved" for f in r.get("findings", [])):
            bad.append("open finding")
        if not bad:
            return True, []
        why += bad
    return False, why


def _lock_records():
    return {r["source_id"]: r for r in _load("sources", "source_lock_records.json")["records"]}


def source_lock_ok(source_id, records=None, sources=None):
    pol = policy()
    rec = (records if records is not None else _lock_records()).get(source_id)
    src = (sources or {s["source_id"]: s for s in _load("sources", "source_registry.json")["sources"]}).get(source_id, {})
    if src.get("source_lock_status") != "locked":
        return False, [f"{source_id}: source_lock_status is {src.get('source_lock_status')!r}"]
    if not rec or rec.get("status") != "signed":
        return False, [f"{source_id}: no signed lock record"]
    why = [f"{source_id}: {k} not pass" for k in pol["source_lock_checklist"] if (rec.get("checklist") or {}).get(k) != "pass"]
    if _is_agent(rec.get("signed_by"), pol) or rec.get("signed_by") == rec.get("preparer"):
        why.append(f"{source_id}: lock signer is not an independent human")
    return not why, why


def ko_sources(ko_id):
    ko = _ko(ko_id)
    eids = set(ko.get("evidence_ids", [])) if ko else set()
    out = set()
    for eid in eids:
        p = os.path.join(DATA, "evidence", eid + ".json")
        if os.path.exists(p):
            out.add(json.load(open(p, encoding="utf-8"))["source_id"])
    return sorted(out)


def evidence_locked_ok(ko_id):
    why = []
    for sid in ko_sources(ko_id):
        why += source_lock_ok(sid)[1]
    return (not why and bool(ko_sources(ko_id))), why


# --- machine-checkable part of the lock checklist (L1–L5); L6 is a human signature ---------------

def _captures():
    out = {}
    for f in glob.glob(os.path.join(DATA, "evidence", "captures", "*.json")):
        d = json.load(open(f, encoding="utf-8"))
        for k, v in d.get("captures", {}).items():
            key = k.split("#")[0]
            ev = os.path.join(DATA, "evidence", key + ".json")
            if key.startswith("EVD-") and os.path.exists(ev):  # recapture files are keyed by evidence id
                key = json.load(open(ev, encoding="utf-8"))["source_id"]
            out.setdefault(key, []).append((os.path.relpath(f, ROOT), v))
    return out


def lock_checklist(source_id, evidence_ids):
    src = {s["source_id"]: s for s in _load("sources", "source_registry.json")["sources"]}.get(source_id, {})
    caps = _captures().get(source_id, [])
    evs = [json.load(open(os.path.join(DATA, "evidence", e + ".json"), encoding="utf-8")) for e in evidence_ids]
    dates = {e.get("retrieval_date") for e in evs} | {c.get("retrieved_on") for _, c in caps}
    dates.discard(None)
    ok_caps = [c for _, c in caps if c.get("http_status") == 200 and c.get("sha256")]
    passages_ok = all(p.get("found") for _, c in caps for p in c.get("passages", [])) and \
        all(x.get("match") for _, c in caps for x in c.get("fields", []))
    ident = any(src.get(k) for k in ("isbn", "edition")) or any(
        (e.get("locator") or {}).get(k) for e in evs for k in ("record_id", "cod_file", "cas", "doi")) or \
        any(lx in json.dumps(e.get("lexical", {})) for e in evs for lx in ("cid",))
    res = {
        "L1": "pass" if src.get("status") == "verified" else "fail",
        "L2": "pass" if ok_caps and passages_ok else "pending",
        "L3": "pass" if len(dates) >= 2 and ok_caps and passages_ok else "pending (needs a re-fetch on a later date)",
        "L4": "pass" if ident or ok_caps else "pending",
        "L5": "pass (short attributed quotations/values only)",
        "L6": "pending (human signature required)",
    }
    return {"source_id": source_id, "checklist": res, "captures": [f for f, _ in caps], "dates_seen": sorted(dates)}


# --- owner acts: claim activation and release authorization ----------------------------------------

def _owner_record(kind, ko_id, records=None):
    recs = records if records is not None else _load("release", "owner_acts.json")[kind]
    return next((r for r in recs if r.get("knowledge_object_id") == ko_id and r.get("status") == "signed"), None)


def claims_active_ok(ko_id, records=None):
    pol, ko = policy(), _ko(ko_id)
    r = _owner_record("claim_activations", ko_id, records)
    if not ko or not r:
        return False, ["no signed owner claim activation"]
    why = []
    if set(r.get("claim_ids", [])) != set(ko["claim_ids"]):
        why.append("activation does not cover exactly the KO claims")
    if _is_agent(r.get("signed_by"), pol) or not r.get("signed_on"):
        why.append("activation not signed by a named human owner")
    return not why, why


def release_authorized_ok(ko_id, records=None):
    pol = policy()
    r = _owner_record("release_authorizations", ko_id, records)
    if not r:
        return False, ["no signed owner release authorization"]
    if _is_agent(r.get("signed_by"), pol) or not r.get("signed_on"):
        return False, ["release not signed by a named human owner"]
    return True, []


def honoured_postures(ko_id, postures):
    """Downgrade any human-gated posture that lacks its signed record (fail-closed). Returns (postures, notes)."""
    p, notes = dict(postures), []
    checks = (("validation_posture", ("validated",), "not_validated", validation_ok),
              ("evidence_posture", ("evidence_locked",), "evidence_sufficient", evidence_locked_ok),
              ("claim_posture", ("claim_approved", "claim_approved_narrow"), "claim_pending", claims_active_ok),
              ("release_authorization", ("authorized",), "not_authorized", release_authorized_ok),
              ("governance_posture", ("governed",), "reference_draft", release_authorized_ok))
    for field, claimed, fallback, fn in checks:
        if p.get(field) in claimed:
            good, why = fn(ko_id)
            if not good:
                notes.append(f"{field} {p[field]} not honoured ({'; '.join(why)[:160]})")
                p[field] = fallback
    return p, notes
