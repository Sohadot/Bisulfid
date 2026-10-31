#!/usr/bin/env python3
"""stage2_legacy_noindex.py — Recovery Stage 2: bring the legacy surface into Contract C RL.

For every page in the sealed Gate-12 legacy hold (main/data/distinctiveness/legacy_surface_hold.json):
  * robots meta  "index, follow"  ->  "noindex, follow"   (URL stays reachable; links still followed)
  * the URL is removed from every sitemap*.xml at the surface root
Nothing else changes: no page is deleted, redirected, re-rendered or re-worded; pages NOT in the
hold (Gate-12 passing pages) are untouched; the substantive body hash of each page is unchanged,
so the result satisfies validate_distinctiveness.py --surface ... --legacy-hold.

SAFETY
  * Writes to --out (a COPY of the surface). Refuses to target site/public unless
    --authorized-stage2 is given; this sprint never passes it.
  * --rollback is trivial: the source surface is untouched; for an in-place run, revert the commit.
  * Prints an exact change manifest (counts + sha256 of the changed-path list).
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
HOLD = os.path.join(ROOT, "main", "data", "distinctiveness", "legacy_surface_hold.json")
ROBOTS_INDEX = re.compile(r'<meta name="robots" content="index, follow">')
ROBOTS_NOINDEX = '<meta name="robots" content="noindex, follow">'


def transform(src, out, hold_path=HOLD):
    hold = json.load(open(hold_path, encoding="utf-8"))
    held = {e["p"] for e in hold["entries"]}
    if os.path.abspath(out) != os.path.abspath(src):
        if os.path.exists(out):
            shutil.rmtree(out)
        shutil.copytree(src, out, ignore=shutil.ignore_patterns("_integration_sample", "_visual_proof_sample"))
    flipped, already, missing = [], 0, []
    for path in sorted(held):
        f = os.path.join(out, path.strip("/"), "index.html") if path != "/" else os.path.join(out, "index.html")
        if not os.path.exists(f):
            missing.append(path)
            continue
        txt = open(f, encoding="utf-8").read()
        new, n = ROBOTS_INDEX.subn(ROBOTS_NOINDEX, txt)
        if n:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new)
            flipped.append(path)
        else:
            already += 1
    removed_urls = 0
    for name in sorted(os.listdir(out)):
        if not (name.startswith("sitemap") and name.endswith(".xml")):
            continue
        f = os.path.join(out, name)
        txt = open(f, encoding="utf-8").read()

        def keep(m):
            nonlocal removed_urls
            loc = re.search(r"<loc>\s*([^<\s]+)\s*</loc>", m.group(0))
            path = re.sub(r"^https?://[^/]+", "", loc.group(1)) if loc else ""
            path = path if path.endswith("/") else path + "/"
            if path in held:
                removed_urls += 1
                return ""
            return m.group(0)
        new = re.sub(r"\s*<url>.*?</url>", keep, txt, flags=re.S)
        if new != txt:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new)
    manifest = {"held_entries": len(held), "robots_flipped_to_noindex": len(flipped),
                "already_noindex": already, "missing_files": missing, "sitemap_urls_removed": removed_urls,
                "flipped_paths_sha256": hashlib.sha256("\n".join(flipped).encode()).hexdigest()}
    return manifest


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=os.path.join(ROOT, "site", "public"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--authorized-stage2", action="store_true",
                    help="required to write into site/public (Stage 2 PR only, after owner authorization)")
    a = ap.parse_args(argv)
    if os.path.abspath(a.out) == os.path.abspath(os.path.join(ROOT, "site", "public")) and not a.authorized_stage2:
        print("REFUSED: writing into site/public requires --authorized-stage2 (Stage 2 PR, owner-authorized).")
        return 2
    m = transform(a.src, a.out)
    print(json.dumps(m, indent=1))
    return 0 if not m["missing_files"] else 1


if __name__ == "__main__":
    sys.exit(main())
