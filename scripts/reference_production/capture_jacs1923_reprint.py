#!/usr/bin/env python3
"""capture_jacs1923_reprint.py — append-only capture of the Caltech archival reprint of Dickinson & Pauling (1923).

Linus Pauling's 1925 Caltech thesis (https://thesis.caltech.edu/1791/) reproduces "The Crystal Structure of
Molybdenite", J. Am. Chem. Soc. 45, 1466-1471 (1923), as a reprint. That reprint is another manifestation of
WORK-DICKINSON-PAULING-1923, the same originating work as COD 1010993: never an independent experiment.

One plain request (no credentials, no access-control workaround). Records the UTC time, HTTP status, media
type, byte count, SHA-256, Last-Modified and ETag; checks that the response is the expected PDF containing
the reprinted article; and checks that the quotation stored in EVD-MOS2-MOLYBDENITE-JACS1923-EXCERPT is
present in the PDF text layer (whitespace, line-break hyphenation and footnote markers normalised).
If an earlier capture by this script has the same SHA-256, the bytes, and so every passage, are reproduced.

The PDF itself is not stored in the repository (quotation scope, checklist L5): the URL, hash, size and
server validators are the audit reference. Each run writes a NEW file
  main/data/evidence/captures/JACS1923_CALTECH_REPRINT_<YYYY-MM-DD>.json
created exclusively; an existing file for that date is never replaced (exit 2).
"""

import datetime
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EV = os.path.join(ROOT, "main", "data", "evidence")
CAPTURES = os.path.join(EV, "captures")
EID = "EVD-MOS2-MOLYBDENITE-JACS1923-EXCERPT"
URL = "https://thesis.caltech.edu/1791/3/Pauling_L_1925.pdf"
UA = "Mozilla/5.0 (bisulfid.com source verification)"
PREFIX = "JACS1923_CALTECH_REPRINT_"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()
    except (urllib.error.URLError, OSError) as e:
        return None, {}, str(e).encode()


def normalise(s):
    s = re.sub(r"-\s*\n\s*", "", s)                        # line-break hyphenation
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"(?<=[A-Za-z]) \d{1,2}(?= [a-z])", "", s)  # footnote markers ("described 2 as")
    s = re.sub(r"(?<=[a-z])\.\d{1,2}(?= [A-Z])", ".", s)   # footnote markers after a full stop
    return re.sub(r" ([,.;:])", r"\1", s).strip()


def pdf_pages(raw):
    """Text layer per page via pdftotext (the PDF carries an OCR text layer)."""
    with tempfile.NamedTemporaryFile(suffix=".pdf") as fh:
        fh.write(raw)
        fh.flush()
        out = subprocess.run(["pdftotext", "-layout", fh.name, "-"], capture_output=True, text=True, check=True).stdout
    return out.split("\f")


def run(now=None, fetcher=fetch, captures_dir=CAPTURES, pages_of=pdf_pages):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    day = now.date().isoformat()
    out_path = os.path.join(captures_dir, f"{PREFIX}{day}.json")
    if os.path.exists(out_path):
        print(f"REFUSED: {out_path} already exists; captures are append-only")
        return 2, None
    status, headers, raw = fetcher(URL)
    rec = {"url": URL, "http_status": status, "retrieved_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "retrieved_on": day, "media_type": headers.get("Content-Type"), "bytes": len(raw),
           "last_modified": headers.get("Last-Modified"), "etag": headers.get("ETag"),
           "manifestation": "Caltech thesis repository reprint (Pauling 1925 PhD thesis) of J. Am. Chem. Soc. 45, "
                            "1466-1471 (1923); same originating work as COD 1010993, not an independent experiment",
           "content_verified": False, "passages": []}
    article_page = None
    if status == 200 and raw[:5] == b"%PDF-":
        pages = pages_of(raw)
        article_page = next((i + 1 for i, p in enumerate(pages)
                             if "CRYSTAL STRUCTURE OF MOLYBDENITE" in p and "Reprinted" in p.replace("R.eorintcd", "Reprinted")), None)
        rec["content_verified"] = article_page is not None
        rec["content_check"] = (f"PDF; reprinted article title found on PDF page {article_page}" if article_page
                                else "PDF without the reprinted molybdenite article")
        ev = json.load(open(os.path.join(EV, EID + ".json"), encoding="utf-8"))
        quote = ev["locator"]["verbatim"]
        hay = normalise(" ".join(pages))
        rec["passages"].append({"evidence_id": EID, "quote": quote, "found": normalise(quote) in hay,
                                "method": "normalised PDF text layer (OCR); confirm visually on the page image"})
    else:
        rec["content_check"] = f"HTTP {status}" if status != 200 else "response is not a PDF"
    if rec["content_verified"]:
        rec["sha256"] = hashlib.sha256(raw).hexdigest()
        earlier = []
        for f in sorted(glob.glob(os.path.join(captures_dir, PREFIX + "*.json"))):
            c = json.load(open(f, encoding="utf-8"))["captures"].get(EID, {})
            if c.get("sha256") == rec["sha256"] and c.get("retrieved_on") != day:
                earlier.append({"file": os.path.basename(f), "retrieved_on": c["retrieved_on"]})
        rec["identical_bytes_to_earlier_captures"] = earlier
    doc = {"capture_id": f"JACS1923-CALTECH-REPRINT-{day}", "generated_by": "scripts/reference_production/capture_jacs1923_reprint.py",
           "note": "Append-only capture of an archival reprint. It does not lock the source and is not an independent "
                   "experiment; COD 1010993 and this reprint are manifestations of the same 1923 work.",
           "captures": {EID: rec}}
    with open(out_path, "x", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    ok = rec["content_verified"] and all(p["found"] for p in rec["passages"])
    print(f"{EID}: HTTP {status}; {rec['content_check']}; passages "
          + ("found" if ok else "NOT found") + f"; sha256 {rec.get('sha256', '-')}; wrote {os.path.relpath(out_path, ROOT)}")
    return (0 if ok else 1), out_path


if __name__ == "__main__":
    sys.exit(run()[0])
