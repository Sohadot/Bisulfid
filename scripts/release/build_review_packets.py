#!/usr/bin/env python3
"""build_review_packets.py — claim-by-claim approval evidence and independent-review packets (Release-01).

For every Knowledge Object with a render spec it writes, deterministically:
  main/data/release/claim_dossiers/<KO>.json   per claim: statement, scope, every bound evidence record with
                                               source identity, qualification, live admissibility result,
                                               locator/verbatim and capture status; boundary records
  main/data/release/review_packets/<KO>.md     the same, readable by an independent reviewer, with a
                                               per-claim checklist and an UNSIGNED signature block
  main/data/release/reviews/<KO>.json          review record skeleton (preparer recorded; reviews: [])
                                               — created once, never overwritten (a reviewer fills it)
  main/data/release/source_lock_checklists.json  machine-checkable L1–L5 per source; L6 always pending

The preparer is recorded as preparer and nowhere as reviewer. --check exits 1 if a generated file is stale.
"""

import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts", "reference_production"))
import release_checks as rc  # noqa: E402
import render_ko_reference as rk  # noqa: E402

PREPARER = "claude-code-agent"


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def all_claims():
    out = {}
    for f in glob.glob(os.path.join(DATA, "claims", "*.json")) + glob.glob(os.path.join(DATA, "pilots", "*claims.json")):
        for c in load(f).get("claims") or []:
            if isinstance(c, dict) and c.get("claim_id"):
                out[c["claim_id"]] = dict(c, _file=os.path.relpath(f, ROOT))
    return out


def ev_summary(eid, r, sources):
    e = load(os.path.join(DATA, "evidence", eid + ".json"))
    prov = next((p for p in r["provenance"] if p["evidence_id"] == eid), None)
    s = sources.get(e["source_id"], {})
    loc = e.get("locator") or {}
    return {"evidence_id": eid, "source_id": e["source_id"], "source_title": s.get("title"), "publisher": s.get("publisher"),
            "source_status": s.get("status"), "source_lock_status": s.get("source_lock_status"),
            "url": s.get("url") or loc.get("url"), "evidence_role": e.get("evidence_role"),
            "review_posture": e.get("evidence_review_posture"), "retrieval_date": e.get("retrieval_date"),
            "admitted_for": prov and prov["intended_use"], "qualification_id": prov and prov["qualification_id"],
            "rendered_on_page": prov is not None,
            "verbatim_or_fields": loc.get("verbatim") or loc.get("fields_quoted") or e.get("lexical"),
            "record": prov and prov["record"], "capture": loc.get("capture_file") or loc.get("system")}


def build(spec_path, sources, claims):
    spec = load(spec_path)
    r = rk.build(spec)
    ko = r["ko"]
    items = []
    for b in ko["claim_bindings"]:
        c = claims.get(b["claim_id"], {})
        items.append({"claim_id": b["claim_id"], "component": b.get("component"), "claim_file": c.get("_file"),
                      "status_in_store": c.get("status") or c.get("outcome"),
                      "statement": c.get("statement") or c.get("proposition"),
                      "scope": c.get("scope_guard") or c.get("form_scope") or c.get("claim_scope") or ko["scope"][:200],
                      "evidence": [ev_summary(e, r, sources) for e in b["evidence_ids"]],
                      "preparer_assessment": "every bound record is evidence_verified and admitted for its declared use; "
                                             "the statement does not exceed the quoted passages/values",
                      "reviewer_questions": ["Does each quoted passage/value appear in the cited source as recorded?",
                                             "Does the statement say no more than the evidence supports (scope, form, polytype, language)?",
                                             "Is the source an appropriate authority for this kind of claim?",
                                             "Is the rendered wording on the page faithful to the claim?"]})
    boundary = [ev_summary(e, r, sources) for e in ko.get("boundary_evidence_ids", [])]
    return spec, r, ko, {"knowledge_object_id": ko["knowledge_object_id"], "render_spec": f"{spec['spec_id']}@{spec['version']}",
                         "route": r["route"]["path"], "preparer": PREPARER, "claims": items, "boundary_evidence": boundary,
                         "not_established": spec["not_established"]["text"], "unresolved_fields": ko.get("unresolved_fields", []),
                         "excluded_claim_classes": ko.get("excluded_claim_classes", [])}


def packet_md(d):
    L = [f"# Independent review packet — {d['knowledge_object_id']}", "",
         f"Route: `{d['route']}` · render spec `{d['render_spec']}` · prepared by `{d['preparer']}` (automated; "
         "**cannot** act as reviewer).", "",
         "## Reviewer requirements", "",
         "- A named person who did not prepare this object, with competence in the subject domain.",
         "- Declare conflicts of interest. Check every claim below against the cited source itself.",
         f"- Record the result in `main/data/release/reviews/{d['knowledge_object_id']}.json` "
         "(policy: `main/data/release/release_review_policy.json`). Verdicts: confirmed, confirmed_with_wording_change, "
         "rejected, out_of_competence. Validation counts only when every claim is `confirmed` and no finding is open.", ""]
    for i, c in enumerate(d["claims"], 1):
        L += [f"## Claim {i}: `{c['claim_id']}`", "", f"**Statement:** {c['statement']}", "", f"**Scope:** {c['scope']}", "",
              "| Evidence | Source | Status / lock | Admitted for | Record | Retrieved |", "|---|---|---|---|---|---|"]
        for e in c["evidence"]:
            L.append(f"| `{e['evidence_id']}` | {e['publisher'] or ''}: {e['source_title'] or e['source_id']} | "
                     f"{e['source_status']} / {e['source_lock_status']} | {e['admitted_for'] or 'not rendered'} | "
                     f"{e['record'] or ''} | {e['retrieval_date']} |")
        L += ["", "Quoted passages / values:", ""]
        for e in c["evidence"]:
            L.append(f"- `{e['evidence_id']}`: {json.dumps(e['verbatim_or_fields'], ensure_ascii=False)[:600]}")
        L += ["", "Reviewer checklist:", ""] + [f"- [ ] {q}" for q in c["reviewer_questions"]] + \
             ["", "Verdict: ☐ confirmed ☐ confirmed with wording change ☐ rejected ☐ out of competence", ""]
    L += ["## Boundary records (support no claim)", ""] + \
         [f"- `{e['evidence_id']}` ({e['source_title']}): {json.dumps(e['verbatim_or_fields'], ensure_ascii=False)[:300]}"
          for e in d["boundary_evidence"]] + ["", "## Stated as NOT established on the page", "", d["not_established"], "",
                                               "## Signature", "", "Reviewer (name): ______  Affiliation: ______  "
                                               "Independent of preparer: ☐ yes  Date: ______", ""]
    return "\n".join(L)


def outputs():
    sources = {s["source_id"]: s for s in load(os.path.join(DATA, "sources", "source_registry.json"))["sources"]}
    claims = all_claims()
    files, locks = {}, {}
    for f in sorted(glob.glob(os.path.join(DATA, "reference_production", "render_specs", "KO-*.json"))):
        spec, r, ko, d = build(f, sources, claims)
        kid = ko["knowledge_object_id"]
        files[os.path.join(DATA, "release", "claim_dossiers", kid + ".json")] = json.dumps(d, indent=1, ensure_ascii=False) + "\n"
        files[os.path.join(DATA, "release", "review_packets", kid + ".md")] = packet_md(d)
        for sid in rc.ko_sources(kid):
            evs = [e for e in ko["evidence_ids"] if load(os.path.join(DATA, "evidence", e + ".json"))["source_id"] == sid]
            locks[sid] = dict(rc.lock_checklist(sid, evs), used_by=sorted(set(locks.get(sid, {}).get("used_by", [])) | {kid}),
                              lock_status=sources[sid].get("source_lock_status"))
    files[os.path.join(DATA, "release", "source_lock_checklists.json")] = json.dumps(
        {"note": "Machine-checkable part of the L1–L6 lock checklist (release_review_policy.json). L6 is a human signature "
                 "and is never filled here; no source is locked by this file.", "sources": dict(sorted(locks.items()))},
        indent=1, ensure_ascii=False) + "\n"
    return files


def main(argv=None):
    mode = (argv or sys.argv[1:] or ["--check"])[0]
    stale = []
    for path, text in outputs().items():
        cur = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if cur != text:
            stale.append(os.path.relpath(path, ROOT))
            if mode == "--write":
                os.makedirs(os.path.dirname(path), exist_ok=True)
                open(path, "w", encoding="utf-8").write(text)
    if mode == "--write":  # review record skeletons: created once, never overwritten
        for f in sorted(glob.glob(os.path.join(DATA, "reference_production", "render_specs", "KO-*.json"))):
            kid = load(f)["knowledge_object_id"]
            p = os.path.join(DATA, "release", "reviews", kid + ".json")
            if not os.path.exists(p):
                json.dump({"knowledge_object_id": kid, "preparer": PREPARER, "packet": f"main/data/release/review_packets/{kid}.md",
                           "reviews": []}, open(p, "w", encoding="utf-8"), indent=2)
                stale.append(os.path.relpath(p, ROOT))
    print(("wrote: " if mode == "--write" else "STALE: ") + ", ".join(stale) if stale else "review packets up to date")
    return 1 if (stale and mode == "--check") else 0


if __name__ == "__main__":
    sys.exit(main())
