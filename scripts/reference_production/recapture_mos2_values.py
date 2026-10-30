#!/usr/bin/env python3
"""recapture_mos2_values.py — Recovery-03 C: re-verify the MoS2 displayed values against the live sources.

For every field quoted by a KO-MOS2-SCIENTIFIC-001 evidence record it fetches the machine-readable
artifact openly (COD CIF, PubChem PUG REST, NIST WebBook page), records HTTP status, sha256 and the
live field value, and compares it with the value stored in the evidence record. Nothing is
corrected automatically: a drift is reported for review. No credentials; no access-control bypass.

Output: main/data/evidence/captures/R03_MOS2_RECAPTURE.json. Exit 1 on drift or a failed fetch.
"""

import datetime
import hashlib
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EV = os.path.join(ROOT, "main", "data", "evidence")
OUT = os.path.join(EV, "captures", "R03_MOS2_RECAPTURE.json")
UA = "Mozilla/5.0 (bisulfid.com source verification)"

# evidence_id -> (artifact url, kind, {stored-field-name: live-extractor-key})
CHECKS = {
    "EVD-MOS2-STRUCTURE-DICKINSON": ("https://www.crystallography.net/cod/1010993.cif", "cif",
                                     ["_symmetry_space_group_name_H-M", "_space_group_IT_number", "_cell_length_a",
                                      "_cell_length_c", "_chemical_name_mineral"]),
    "EVD-MOS2-STRUCTURE-ACTACRYST": ("https://www.crystallography.net/cod/9007660.cif", "cif",
                                     ["_symmetry_space_group_name_H-M", "_cell_length_a", "_cell_length_c",
                                      "_chemical_name_mineral"]),
    "EVD-MOS2-FORMULA-PUBCHEM": ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/14823/property/MolecularFormula,MolecularWeight,Title/JSON",
                                 "pubchem", ["MolecularFormula", "MolecularWeight"]),
    "EVD-MOS2-FORMULA-NIST": ("https://webbook.nist.gov/cgi/cbook.cgi?ID=1317-33-5", "nist", ["Formula", "molecularWeight"]),
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def cif_field(text, name):
    m = re.search(r"^" + re.escape(name) + r"\s+(.+)$", text, re.M)
    return m.group(1).strip().strip("'\"") if m else None


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


def main():
    out, failed = {}, []
    for eid, (url, kind, fields) in CHECKS.items():
        ev = json.load(open(os.path.join(EV, eid + ".json"), encoding="utf-8"))
        status, raw = fetch(url)
        rec = {"url": url, "http_status": status, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
               "retrieved_on": datetime.date.today().isoformat(), "fields": []}
        text = raw.decode("utf-8", errors="replace")
        for f in fields:
            live = live_value(kind, text, f) if status == 200 else None
            stored = stored_value(ev, f)
            same = live is not None and stored is not None and live.replace(" ", "") == stored.replace(" ", "")
            rec["fields"].append({"field": f, "stored": stored, "live": live, "match": same})
            if not same:
                failed.append(f"{eid} {f}: stored {stored!r} live {live!r}")
        out[eid] = rec
        print(f"{eid}: HTTP {status}; " + ", ".join(f"{x['field']}={'ok' if x['match'] else 'DRIFT'}" for x in rec["fields"]))
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"capture_id": "R03-MOS2-RECAPTURE", "generated_by": "scripts/reference_production/recapture_mos2_values.py",
                   "note": "Live re-verification of stored evidence values. A match confirms the stored value still equals the "
                           "source; it does not lock the source (source_lock_status stays candidate).",
                   "captures": out}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    for f in failed:
        print("DRIFT/FAIL " + f)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
