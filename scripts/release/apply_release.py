#!/usr/bin/env python3
"""apply_release.py — copy ONE staged release candidate into site/public, only when governance allows it.

  apply_release.py --page /molybdenum-disulfide/ [--dry-run]

Refuses unless, at the moment of the call:
  * the staged candidate is current (its renderer --check passes);
  * knowledge reference: the publication authority resolves Contract C (public_indexable, index_approved),
    which in turn requires the signed records (independent review, source locks, owner claim activation
    and release authorization) — nothing can be simulated here;
  * institutional page: a signed R11 certification binds the URL, and every publication dependency
    (linked governed reference) is itself index-approved.
It changes only the one file and never touches robots, sitemaps or other pages. Run the deploy gate
(validate_publication_authority.py --surface site/public) afterwards; deployment stays manual.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "publication"))
import publication_authority as pa  # noqa: E402

STAGED = os.path.join(ROOT, "main", "data", "release", "staged")
RENDERERS = {"knowledge_reference": "render_ko_reference.py", "institutional": "render_institutional_preview.py"}


def refusals(page):
    slug = page.strip("/") or "home"
    man_p = os.path.join(STAGED, slug, "release.json")
    if not os.path.exists(man_p):
        return [f"no staged release candidate for {page}"], None
    man = json.load(open(man_p, encoding="utf-8"))
    why = []
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "reference_production", RENDERERS[man["kind"]]), "--check"],
                       capture_output=True, text=True)
    if r.returncode:
        why.append("staged candidate is stale (re-render first)")
    auth = pa.Authority()
    cc, basis = auth.contract_c(page)
    if cc != ("public_indexable", "index_approved"):
        why.append(f"Contract C for {page} is {cc} ({basis}); publication needs (public_indexable, index_approved)")
    for dep in man.get("publication_dependencies", []):
        dcc, _ = auth.contract_c(dep)
        if dcc != ("public_indexable", "index_approved"):
            why.append(f"dependency {dep} is not public yet ({dcc})")
    return why, slug


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    why, slug = refusals(a.page)
    if why:
        print(f"REFUSED {a.page}:")
        for w in why:
            print(f"  - {w}")
        return 2
    dest = os.path.join(ROOT, "site", "public", "" if slug == "home" else slug, "index.html")
    if a.dry_run:
        print(f"would copy main/data/release/staged/{slug}/index.html -> {os.path.relpath(dest, ROOT)}")
        return 0
    shutil.copyfile(os.path.join(STAGED, slug, "index.html"), dest)
    print(f"applied {a.page}; now run: python3 scripts/publication/validate_publication_authority.py --surface site/public")
    return 0


if __name__ == "__main__":
    sys.exit(main())
