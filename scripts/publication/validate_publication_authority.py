#!/usr/bin/env python3
"""validate_publication_authority.py — deploy gate for a public surface (Recovery-02).

Compares what a surface SERVES (robots meta, sitemap membership, rel=canonical, page existence,
substantive body) with what publication_authority.Authority RESOLVES, and applies the Gate 12 /
Gate 12-I vetoes.

States (BLOCK_* fail the run):
  GOVERNED_INDEX            Contract-C index_approved and Gate 12 (or 12-I + R11) PASS
  GOVERNED_NOINDEX          Contract C public_noindex
  LEGACY_STATUS_QUO         sealed legacy page, body unchanged, directives <= what it was served with
  LEGACY_REPAIR_NOINDEX     sealed legacy page whose body changed, served noindex and out of sitemaps
  BLOCK_UNAUTHORIZED_PAGE   page exists but nothing authorizes it (new page without Contract-C approval)
  BLOCK_DIRECTIVE_ESCALATION   robots requests index where the authority resolves noindex
  BLOCK_SITEMAP_ESCALATION  sitemap lists a URL the authority does not allow in a sitemap
  BLOCK_CANONICAL_MISMATCH  rel=canonical differs from the resolved canonical
  BLOCK_CANONICAL_CONFLICT  noindex combined with a cross-URL canonical, or canonical to a non-indexable URL
  BLOCK_MODIFIED_INDEXED    legacy page with a changed body still requests indexation
  BLOCK_GATE12_VETO         index-approved page that fails Gate 12 / 12-I
  BLOCK_UNAPPROVED_REMOVAL  a sealed legacy URL is missing without an approved redirect/retire decision

Usage:
  validate_publication_authority.py --surface DIR [--sitemap-policy status_quo|approved_only] [--json OUT]
"""

import argparse
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "validators"))
import publication_authority as pa  # noqa: E402
import distinctiveness_core as dc  # noqa: E402


def check_surface(surface, authority, policy, sitemap_policy="status_quo", verdicts=None, pages=None):
    if pages is None:
        pages = dc.load_html_pages(policy, surface)
    if verdicts is None:
        import validate_distinctiveness as vd
        _, verdicts, _ = vd.analyse_universe("surface", pages, policy, dc.IGContext())
    sitemap = dc.sitemap_paths(surface)
    out = []
    present = set()
    for page, v in zip(pages, verdicts):
        path = dc.surface_url_path(page, surface)
        present.add(path)
        r = authority.resolve(path, sitemap_policy)
        served_index = pa.requests_index(page.robots)
        served_sm = path in sitemap
        served_canon = pa.canonical_path(page.canonical)
        base = authority.baseline.get(path)
        unchanged = bool(base) and base["h"] == dc.body_hash_hex(page)
        problems = []
        if not r["render"]:
            problems.append("BLOCK_UNAUTHORIZED_PAGE")
        else:
            if served_index and not pa.requests_index(r["robots"]):
                problems.append("BLOCK_DIRECTIVE_ESCALATION")
            if served_sm and not r["sitemap"]:
                problems.append("BLOCK_SITEMAP_ESCALATION")
            if served_canon != r["canonical"]:
                problems.append("BLOCK_CANONICAL_MISMATCH")
            status_quo_canon = r["basis"] == "legacy_status_quo" and base and served_canon == base.get("c")
            if served_canon and served_canon != path and not served_index and not status_quo_canon:
                problems.append("BLOCK_CANONICAL_CONFLICT")
            if r["basis"].startswith("contract_c") and pa.requests_index(r["robots"]) and v["verdict"] != "PASS":
                problems.append("BLOCK_GATE12_VETO")
            if r["basis"] == "legacy_status_quo" and not unchanged and (served_index or served_sm):
                problems.append("BLOCK_MODIFIED_INDEXED")
        if problems:
            state = problems[0]
        elif r["basis"].startswith("contract_c"):
            state = "GOVERNED_INDEX" if served_index else "GOVERNED_NOINDEX"
        else:
            state = "LEGACY_STATUS_QUO" if unchanged else "LEGACY_REPAIR_NOINDEX"
        out.append({"path": path, "state": state, "problems": problems, "basis": r["basis"], "notes": r["notes"],
                    "served": {"robots": page.robots, "sitemap": served_sm, "canonical": served_canon},
                    "resolved": {"robots": r["robots"], "sitemap": r["sitemap"], "canonical": r["canonical"]},
                    "gate12": v["verdict"], "page_class": v.get("page_class")})
    for path in sorted(set(authority.baseline) - present):
        d = authority.decisions.get(path)
        if not (d and d["decision"] in ("redirect_to", "retire")):
            out.append({"path": path, "state": "BLOCK_UNAPPROVED_REMOVAL", "problems": ["BLOCK_UNAPPROVED_REMOVAL"],
                        "basis": "legacy_status_quo", "notes": ["sealed legacy URL missing without approved decision"]})
    return out


def summarize(states):
    c = Counter(s["state"] for s in states)
    debt = sum(1 for s in states if s["state"] == "LEGACY_STATUS_QUO" and s["served"]["robots"]
               and pa.requests_index(s["served"]["robots"]) and s["gate12"] != "PASS")
    return {"counts": dict(c), "blocking": sum(v for k, v in c.items() if k.startswith("BLOCK")),
            "contract_c_rl_debt_indexed_legacy_failing_gate12": debt}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--surface", required=True)
    ap.add_argument("--sitemap-policy", choices=("status_quo", "approved_only"), default="status_quo")
    ap.add_argument("--json")
    ap.add_argument("--show", type=int, default=15)
    a = ap.parse_args(argv)
    policy = dc.load_policy()
    states = check_surface(a.surface, pa.Authority(), policy, a.sitemap_policy)
    s = summarize(states)
    print("=" * 72)
    print(f"Publication authority — surface {a.surface} (sitemap policy {a.sitemap_policy})")
    for k, v in sorted(s["counts"].items()):
        print(f"  {k:28s} {v}")
    print(f"  Contract C RL debt (indexed legacy pages failing Gate 12): {s['contract_c_rl_debt_indexed_legacy_failing_gate12']}")
    for st in [x for x in states if x["problems"]][:a.show]:
        print(f"  [{st['state']}] {st['path']} served={st.get('served')} resolved={st.get('resolved')} {st['notes']}")
    if a.json:
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump({"summary": s, "blocking": [x for x in states if x["problems"]][:5000]}, fh, indent=1)
    if s["blocking"]:
        print(f"PUBLICATION AUTHORITY FAIL: {s['blocking']} blocking page(s).")
        return 1
    print("PUBLICATION AUTHORITY PASS: nothing escalates, nothing new is unauthorized, nothing modified requests index.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
