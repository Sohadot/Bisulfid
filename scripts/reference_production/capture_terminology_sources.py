#!/usr/bin/env python3
"""capture_terminology_sources.py — Recovery-03 source identity verification + verbatim capture.

For every terminology source of the BISULFID / bisulfide boundary it fetches the declared URL
(openly; no credentials, no bypass of access controls — checklist C6), records HTTP status, media
type, byte size and sha256 (C1/C2), and asserts that every quoted passage used by an evidence
record is present VERBATIM in the retrieved artifact after whitespace normalization (C5).
A passage that is not found fails the capture; nothing is quoted from memory.

Output: main/data/evidence/captures/R03_TERMINOLOGY_CAPTURES.json (deterministic order); with
--recapture (run on a LATER date, source-lock checklist L3) captures/TERMINOLOGY_RECAPTURE_<date>.json.
Network required. Exit 1 if any check fails or a declared artifact is unreachable.
"""

import datetime
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "main", "data", "evidence", "captures", "R03_TERMINOLOGY_CAPTURES.json")
UA = "Mozilla/5.0 (bisulfid.com source verification; no automation of gated content)"

# source_id -> (url, kind, [verbatim passages]); kind: html | pdf | json
SOURCES = {
    "SRC-MW-BISULFIDE": ("https://www.merriam-webster.com/dictionary/bisulfide", "html",
                         ["bisulfide noun", ": disulfide", "First Known Use 1831"]),
    "SRC-MW-SULFIDE": ("https://www.merriam-webster.com/dictionary/sulfide", "html",
                       ["1 : any of various organic compounds characterized by a sulfur atom attached to two carbon atoms",
                        "2 : a binary compound (such as CuS) of sulfur usually with a more electropositive element or group : a salt of hydrogen sulfide",
                        "First Known Use 1836"]),
    "SRC-MW-BISULFITE": ("https://www.merriam-webster.com/dictionary/bisulfite", "html",
                         ["bisulfite noun", ": an acid sulfite", "First Known Use 1819"]),
    "SRC-MW-DISULFIDE": ("https://www.merriam-webster.com/dictionary/disulfide", "html",
                         ["1 : a compound containing two atoms of sulfur combined with an element or radical",
                          "2 : an organic compound containing the divalent group SS composed of two sulfur atoms",
                          "First Known Use 1869"]),
    "SRC-DUDEN-SULFID": ("https://www.duden.de/rechtschreibung/Sulfid", "html",
                         ["Worttrennung Sul|fid", "Bedeutung ⓘ salzartige Verbindung des Schwefelwasserstoffs"]),
    "SRC-DWDS-SULFID": ("https://www.dwds.de/wb/Sulfid", "html",
                        ["Bedeutung eWDG 1976 Chemie Salz des Schwefelwasserstoffs"]),
    "SRC-DWDS-BISULFID": ("https://www.dwds.de/wb/Bisulfid", "html",
                          ["Es tut uns leid, Ihre Anfrage Bisulfid ist nicht in unseren gegenwartssprachlichen lexikalischen Quellen vorhanden.",
                           "Nominativ Plural: Bisulfide (computergeneriert)"]),
    "SRC-DWDS-HYDROGENSULFID": ("https://www.dwds.de/wb/Hydrogensulfid", "html",
                                ["Es tut uns leid, Ihre Anfrage Hydrogensulfid ist nicht in unseren gegenwartssprachlichen lexikalischen Quellen vorhanden."]),
    "SRC-SPEKTRUM-SCHWEFELWASSERSTOFF-DE": ("https://www.spektrum.de/lexikon/chemie/schwefelwasserstoff/8309", "html",
                                            ["S. bildet zwei Reihen von Salzen, die Hydrogensulfide M I HS und die Sulfide M I 2 S."]),
    "SRC-IUPAC-RED-BOOK-2005": ("https://iupac.org/wp-content/uploads/2016/07/Red_Book_2005.pdf", "pdf",
                                ["NOMENCLATURE OF INORGANIC CHEMISTRY IUPAC Recommendations 2005",
                                 "3. HS sulfanide (substitutive), or hydridosulfate(1 ) (additive)",
                                 "8. S22 disulﬁde(2 )",
                                 "12. S2 disulfanediide",
                                 "It is strongly recommended that this list be viewed as limiting due to the ambiguities that may arise in many other cases.",
                                 "HSO3 hydrogensulﬁte hydrogen(trioxidosulfate)(1 )"]),
    "SRC-FH-MUENSTER-ANORGANISCHE-NOMENKLATUR": (
        "https://www-backend.fh-muenster.de/ciw/downloads-ciw/personenprofile/juestel/wissenswertes/chemie/Anorganische-Nomenklatur.pdf",
        "pdf", ["Regeln zur Nomenklatur Anorganischer Verbindungen",
                "Das nachgestellte Nichtmetallatom bzw. -ion binärer Verbindungen mit negativer Oxidationszahl endet auf -id.",
                "a) Einatomige Anionen mit Endung -id", "S2- Sulfid"]),
    "SRC-PUBCHEM-HYDROSULFIDE": ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5047209/property/MolecularFormula,IUPACName,Title,Charge/JSON",
                                 "json", ['"MolecularFormula": "HS-"', '"IUPACName": "sulfanide"', '"Title": "Hydrosulfide"']),
    "SRC-PUBCHEM-HYDROSULFIDE#synonyms": ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5047209/synonyms/JSON",
                                          "json", ['"bisulfide"', '"sulfanide"', '"hydrosulfide"']),
    "SRC-PUBCHEM-BISULFITE": ("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/104748/property/MolecularFormula,IUPACName,Title,Charge/JSON",
                              "json", ['"MolecularFormula": "HO3S-"', '"IUPACName": "hydrogen sulfite"', '"Title": "Bisulfite"']),
    "SRC-BADGER-BISULFID-H2S": ("https://www.badgermeter.com/de-de/parameter-zur-uberwachung-der-wasserqualitat/hs-h2s/", "html",
                                ["Bisulfid und Schwefelwasserstoff (HS- / H₂S)",
                                 "Bisulfid hingegen ist seine konjugierte Base"]),
    # Recorded so the boundary is reproducible: these declared artifacts could not be verified openly.
    "SRC-IUPAC-HYDROSULFIDES": ("https://goldbook.iupac.org/terms/view/H02910", "html", []),
    "SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN": (
        "https://www.lkv.uni-rostock.de/storages/uni-rostock/Alle_MNF/Chemie_Koeckerling/Materialdesign_12_Nomenklatur.pdf", "pdf", []),
}
EXPECTED_UNREACHABLE = {"SRC-IUPAC-HYDROSULFIDES", "SRC-UNI-ROSTOCK-NOMENKLATUR-ID-ANIONEN"}


def norm(s):
    return " ".join(s.split())


def html_text(raw):
    s = raw.decode("utf-8", errors="replace")
    s = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return norm(html.unescape(s))


def pdf_text(raw):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "a.pdf")
        open(p, "wb").write(raw)
        subprocess.run(["pdftotext", "-layout", p, p + ".txt"], check=True)
        pages = open(p + ".txt", encoding="utf-8", errors="replace").read().split("\f")
    return pages


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type", ""), e.read()


def main():
    global OUT
    today = datetime.date.today().isoformat()
    if "--recapture" in sys.argv:  # L3 (source-lock checklist): a later, separate capture; never overwrite the first
        OUT = os.path.join(os.path.dirname(OUT), f"TERMINOLOGY_RECAPTURE_{today}.json")
    out, failed = {}, []
    for sid, (url, kind, quotes) in SOURCES.items():
        status, ctype, raw = fetch(url)
        rec = {"url": url, "retrieved_on": today, "http_status": status, "content_type": ctype.split(";")[0],
               "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "passages": []}
        if status != 200:
            rec["verification"] = "unreachable (C1 fail); not bypassed (C6)"
            if sid not in EXPECTED_UNREACHABLE:
                failed.append(f"{sid}: HTTP {status}")
            out[sid] = rec
            continue
        if kind == "pdf":
            pages = pdf_text(raw)
            for q in quotes:
                hit = next((i + 1 for i, p in enumerate(pages) if norm(q) in norm(p)), None)
                rec["passages"].append({"quote": q, "found": hit is not None, "pdf_page": hit})
        else:
            text = html_text(raw) if kind == "html" else norm(raw.decode("utf-8"))
            for q in quotes:
                rec["passages"].append({"quote": q, "found": norm(q) in text})
        missing = [p["quote"] for p in rec["passages"] if not p["found"]]
        rec["verification"] = "verbatim passages present (C5)" if not missing else f"MISSING: {missing}"
        if missing:
            failed.append(f"{sid}: {missing}")
        out[sid] = rec
        print(f"{sid}: HTTP {status} {rec['content_type']} {len(raw)} bytes; {len(quotes) - len(missing)}/{len(quotes)} passages")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"capture_id": "R03-TERMINOLOGY-CAPTURES", "generated_by": "scripts/reference_production/capture_terminology_sources.py",
                   "note": "Identity + verbatim capture only. Raw artifacts are not stored; sha256 fixes the retrieved bytes. "
                           "PDF text is extracted with pdftotext, which drops superscript charge signs (e.g. 'hydridosulfate(1 )' "
                           "is printed in the source as 'hydridosulfate(1−)').",
                   "captures": out}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    for f in failed:
        print("FAIL " + f)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
