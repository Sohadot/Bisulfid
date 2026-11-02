#!/usr/bin/env python3
"""recapture_mos2_values.py — re-verify the MoS2 displayed values against the live sources (append-only).

For every field quoted by a KO-MOS2-SCIENTIFIC-001 evidence record it fetches the machine-readable
artifact openly (COD CIF, PubChem PUG REST, NIST WebBook page) with a plain request, records the UTC
retrieval time, HTTP status, SHA-256 and byte count of the raw response, checks that the response is the
expected scientific record (not an error or anti-bot page), and compares each live field with the value
stored in the evidence record. Nothing is corrected automatically: a drift is reported for review.
No credentials; no access-control bypass.

Append-only: every run writes a NEW date-stamped file,
  main/data/evidence/captures/MOS2_RECAPTURE_<YYYY-MM-DD>.json
created exclusively — if that file already exists the run is refused and nothing is written. Earlier
captures (including R03_MOS2_RECAPTURE.json of 2026-10-30) are never modified.

Raw bytes are kept where reuse is permitted (COD CIFs: CC0; PubChem: public-domain US-government data)
under main/data/evidence/raw_captures/<date>/. NIST WebBook data is copyrighted Standard Reference Data,
so for NIST only the SHA-256, byte count and URL are kept as the auditable reference.

Exit 0 when every fetch succeeded and every field matched; 1 on drift or a failed fetch; 2 on a collision.
"""

import datetime
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EV = os.path.join(ROOT, "main", "data", "evidence")
CAPTURES = os.path.join(EV, "captures")
RAW = os.path.join(EV, "raw_captures")
UA = "Mozilla/5.0 (bisulfid.com source verification)"

# evidence_id -> (artifact url, kind, stored fields, raw-byte retention permitted)
CHECKS = {
    "EVD-MOS2-STRUCTURE-DICKINSON": ("https://www.crystallography.net/cod/1010993.cif", "cif",
                                     ["_symmetry_space_group_name_H-M", "_space_group_IT_number", "_cell_length_a",
                                      "_cell_length_c", "_chemical_name_mineral"], True),
    "EVD-MOS2-STRUCTURE-ACTACRYST": ("https://www.crystallography.net/cod/9007660.cif", "cif",
                                     ["_symmetry_space_group_name_H-M", "_cell_length_a", "_cell_length_c",
                                      "_chemical_name_mineral"], True),
    "EVD-MOS2-FORMULA-PUBCHEM": ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/14823/property/MolecularFormula,MolecularWeight,Title/JSON",
                                 "pubchem", ["MolecularFormula", "MolecularWeight"], True),
    "EVD-MOS2-FORMULA-NIST": ("https://webbook.nist.gov/cgi/cbook.cgi?ID=1317-33-5", "nist", ["Formula", "molecularWeight"], False),
}
EXT = {"cif": "cif", "pubchem": "json", "nist": "html"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except (urllib.error.URLError, OSError) as e:
        return None, str(e).encode()


def cif_field(text, name):
    m = re.search(r"^" + re.escape(name) + r"\s+(.+)$", text, re.M)
    return m.group(1).strip().strip("'\"") if m else None


def content_check(kind, text):
    """Is this the expected scientific record, not an error, login or anti-bot page? Returns (ok, reason)."""
    if kind == "cif":
        ok = re.search(r"^data_\S+", text, re.M) and "_cell_length_a" in text and "<html" not in text.lower()
        return bool(ok), "CIF data block with cell parameters" if ok else "not a CIF data block"
    if kind == "pubchem":
        try:
            props = json.loads(text)["PropertyTable"]["Properties"][0]
            return props.get("CID") == 14823, "PUG REST PropertyTable for CID 14823"
        except (ValueError, KeyError, IndexError, TypeError):
            return False, "not a PUG REST PropertyTable"
    if kind == "nist":
        low = text.lower()  # the WebBook title reads "molybdenum disulphide" (British spelling, lower case)
        ok = ("molybdenum disulfide" in low or "molybdenum disulphide" in low) and "1317-33-5" in text \
            and "Formula" in text
        return ok, "WebBook record for CAS 1317-33-5" if ok else "not the WebBook record for CAS 1317-33-5"
    return False, "unknown kind"


def live_value(kind, text, field):
    if kind == "cif":
        return cif_field(text, field)
    if kind == "pubchem":
        props = json.loads(text)["PropertyTable"]["Properties"][0]
        return str(props.get(field)) if field in props else None
    if kind == "nist":
        plain = " ".join(re.sub(r"<[^>]+>", "", text).split())
        if field == "Formula":
            m = re.search(r"Formula:\s*([A-Za-z0-9]+)", plain)
        else:
            m = re.search(r"Molecular weight:\s*([0-9.]+)", plain)
        return m.group(1) if m else None


def stored_value(ev, field):
    q = (ev.get("locator") or {}).get("fields_quoted") or {}
    v = q.get(field)
    return v.split()[0] if (field == "molecularWeight" and v) else v


def capture_one(eid, url, kind, fields, keep_raw, now, fetcher, raw_dir):
    ev = json.load(open(os.path.join(EV, eid + ".json"), encoding="utf-8"))
    status, raw = fetcher(url)
    text = raw.decode("utf-8", errors="replace")
    good, why = content_check(kind, text) if status == 200 else (False, f"HTTP {status}")
    rec = {"url": url, "http_status": status, "retrieved_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "retrieved_on": now.date().isoformat(), "bytes": len(raw), "content_verified": good, "content_check": why,
           "fields": []}
    if status == 200 and good:  # a hash is recorded only for a genuine retrieval of the expected record
        rec["sha256"] = hashlib.sha256(raw).hexdigest()
        if keep_raw:
            rel = os.path.join(raw_dir, f"{eid}.{EXT[kind]}")
            rec["raw_artifact"] = os.path.relpath(rel, ROOT)
            rec["_raw_bytes"] = raw
        else:
            rec["raw_artifact"] = None
            rec["raw_artifact_note"] = "bytes not retained (NIST Standard Reference Data copyright); SHA-256, byte count and URL are the audit reference"
    for f in fields:
        live = live_value(kind, text, f) if (status == 200 and good) else None
        stored = stored_value(ev, f)
        same = live is not None and stored is not None and live.replace(" ", "") == stored.replace(" ", "")
        rec["fields"].append({"field": f, "stored": stored, "live": live, "match": same})
    return rec


def run(now=None, fetcher=fetch, captures_dir=CAPTURES, raw_root=RAW):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    day = now.date().isoformat()
    out_path = os.path.join(captures_dir, f"MOS2_RECAPTURE_{day}.json")
    raw_dir = os.path.join(raw_root, day)
    if os.path.exists(out_path) or os.path.exists(raw_dir):
        print(f"REFUSED: {os.path.relpath(out_path, ROOT)} or {os.path.relpath(raw_dir, ROOT)} already exists; "
              "captures are append-only and are never replaced")
        return 2, None
    out, failed = {}, []
    for eid, (url, kind, fields, keep_raw) in CHECKS.items():
        rec = capture_one(eid, url, kind, fields, keep_raw, now, fetcher, raw_dir)
        out[eid] = rec
        if not rec["content_verified"]:
            failed.append(f"{eid}: {rec['content_check']}")
        failed += [f"{eid} {x['field']}: stored {x['stored']!r} live {x['live']!r}" for x in rec["fields"] if not x["match"]]
        print(f"{eid}: HTTP {rec['http_status']}; {rec['content_check']}; "
              + ", ".join(f"{x['field']}={'ok' if x['match'] else 'DRIFT'}" for x in rec["fields"]))
    doc = {"capture_id": f"MOS2-RECAPTURE-{day}", "generated_by": "scripts/reference_production/recapture_mos2_values.py",
           "note": "Append-only live re-verification of stored evidence values. A match confirms the stored value still "
                   "equals the source on this date; it does not lock the source (source_lock_status stays candidate).",
           "captures": {k: {x: y for x, y in v.items() if x != "_raw_bytes"} for k, v in out.items()}}
    with open(out_path, "x", encoding="utf-8") as fh:  # exclusive create: never overwrite
        json.dump(doc, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    for v in out.values():
        if v.get("_raw_bytes") is not None:
            os.makedirs(raw_dir, exist_ok=True)
            with open(os.path.join(ROOT, v["raw_artifact"]), "xb") as fh:
                fh.write(v["_raw_bytes"])
    print("wrote: " + os.path.relpath(out_path, ROOT))
    for f in failed:
        print("DRIFT/FAIL " + f)
    return (1 if failed else 0), out_path


def main():
    return run()[0]


if __name__ == "__main__":
    sys.exit(main())
