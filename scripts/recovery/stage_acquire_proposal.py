#!/usr/bin/env python3
"""stage_acquire_proposal.py — Recovery-03 A: STAGED /acquire/ correction (never applied here).

/acquire/ was served "index, follow"; the release ledger blocks it (blocked_high_risk) and the
publication-authority deploy gate therefore reports BLOCK_DIRECTIVE_ESCALATION. The fix is to
make the served page match the governed directive, NOT to edit the ledger:

  robots  index, follow  ->  noindex, follow     (page stays public; links still followed)
  sitemap not listed     ->  not listed          (unchanged)
  canonical, body, contact (mailto) unchanged

Outputs (with --write; --check exits 1 if stale):
  main/data/recovery/staged/acquire/index.html   the proposed page (outside site/public: cannot deploy)
  main/data/recovery/staged/acquire.patch        unified diff against the live file
Applying it to site/public requires owner approval of URL-DEC-R03-ACQUIRE-001 in
main/data/publication/url_decisions.json (status 'proposed' until then).
"""

import difflib
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LIVE = os.path.join(ROOT, "site", "public", "acquire", "index.html")
OUT_DIR = os.path.join(ROOT, "main", "data", "recovery", "staged")
OLD = '<meta name="robots" content="index, follow">'
NEW = '<meta name="robots" content="noindex, follow">'


def build():
    live = open(LIVE, encoding="utf-8").read()
    if live.count(OLD) != 1:
        raise SystemExit(f"expected exactly one '{OLD}' in {LIVE}; live page changed, re-review the proposal")
    staged = live.replace(OLD, NEW)
    patch = "".join(difflib.unified_diff(live.splitlines(True), staged.splitlines(True),
                                         "a/site/public/acquire/index.html", "b/site/public/acquire/index.html"))
    return {os.path.join(OUT_DIR, "acquire", "index.html"): staged, os.path.join(OUT_DIR, "acquire.patch"): patch}


def main(argv=None):
    mode = (argv or sys.argv[1:] or ["--check"])[0]
    stale = []
    for path, text in build().items():
        cur = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if cur != text:
            stale.append(os.path.relpath(path, ROOT))
            if mode == "--write":
                os.makedirs(os.path.dirname(path), exist_ok=True)
                open(path, "w", encoding="utf-8").write(text)
    print(("wrote: " if mode == "--write" else "STALE: ") + ", ".join(stale) if stale else "staged /acquire/ proposal up to date")
    return 1 if (stale and mode == "--check") else 0


if __name__ == "__main__":
    sys.exit(main())
