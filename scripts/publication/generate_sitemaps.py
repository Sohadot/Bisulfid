#!/usr/bin/env python3
"""generate_sitemaps.py — sitemaps from the publication authority only (Recovery-02).

A URL is listed iff Authority.resolve(path, policy)["sitemap"] is true, i.e. the URL resolves to
"index, follow" AND is its own canonical AND is allowed in a sitemap by the policy:
  approved_only (default)  Contract-C index_approved URLs only — the target state
  status_quo               additionally the legacy URLs exactly as they were listed (never more)
Writes sitemap.xml (index) + sitemap-NNN.xml shards (<= 2,500 URLs each) to --out, then re-parses and
validates them: well-formed XML, absolute https://bisulfid.com URLs, no duplicates, every URL resolves
to index + self-canonical. Never writes into site/public unless --authorized-publication is given.
"""

import argparse
import os
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import publication_authority as pa  # noqa: E402

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
SHARD = 2500


def candidate_paths(authority):
    return sorted(set(authority.baseline) | set(authority.postures))


def build(authority, policy):
    return [p for p in candidate_paths(authority) if authority.resolve(p, policy)["sitemap"]]


def write(urls, out):
    os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f.startswith("sitemap") and f.endswith(".xml"):
            os.remove(os.path.join(out, f))
    shards = [urls[i:i + SHARD] for i in range(0, len(urls), SHARD)] or [[]]
    names = []
    for n, shard in enumerate(shards, 1):
        name = f"sitemap-{n:03d}.xml"
        names.append(name)
        body = "".join(f"\n  <url><loc>{pa.SITE}{p}</loc></url>" for p in shard)
        with open(os.path.join(out, name), "w", encoding="utf-8") as fh:
            fh.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="{NS}">{body}\n</urlset>\n')
    body = "".join(f"\n  <sitemap><loc>{pa.SITE}/{n}</loc></sitemap>" for n in names)
    with open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="{NS}">{body}\n</sitemapindex>\n')
    return names


def validate(out, authority, policy):
    errs, seen = [], set()
    idx = ET.parse(os.path.join(out, "sitemap.xml")).getroot()
    for loc in idx.iter(f"{{{NS}}}loc"):
        name = loc.text.rsplit("/", 1)[-1]
        root = ET.parse(os.path.join(out, name)).getroot()
        for u in root.iter(f"{{{NS}}}loc"):
            url = u.text
            if not url.startswith(pa.SITE + "/"):
                errs.append(f"not absolute https: {url}")
            path = url[len(pa.SITE):]
            if path in seen:
                errs.append(f"duplicate: {url}")
            seen.add(path)
            r = authority.resolve(path, policy)
            if not (r["render"] and pa.requests_index(r["robots"]) and r["canonical"] == path):
                errs.append(f"not an indexable self-canonical URL: {url} ({r['basis']})")
    return len(seen), errs


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--policy", choices=("approved_only", "status_quo"), default="approved_only")
    ap.add_argument("--authorized-publication", action="store_true")
    a = ap.parse_args(argv)
    if os.path.abspath(a.out).startswith(os.path.abspath(os.path.join(pa.ROOT, "site", "public"))) \
            and not a.authorized_publication:
        print("REFUSED: writing sitemaps into site/public requires --authorized-publication.")
        return 2
    auth = pa.Authority()
    urls = build(auth, a.policy)
    names = write(urls, a.out)
    n, errs = validate(a.out, auth, a.policy)
    print(f"sitemaps ({a.policy}): {n} URL(s) in {len(names)} shard(s) -> {a.out}")
    for e in errs[:20]:
        print("  INVALID: " + e)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
