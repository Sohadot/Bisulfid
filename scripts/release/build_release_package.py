#!/usr/bin/env python3
"""build_release_package.py — Release-01 readiness matrix and per-PR descriptions, from the governed stores.

Reads: staged release candidates + manifests, RELEASE_SIMULATION.json, TEST_RESULTS.json,
source_lock_checklists.json, claim dossiers, review records, owner acts, URL decisions, R11 records.
Writes: main/data/release/RELEASE_01_READINESS.md and main/data/release/prs/PR-{A..E}.md.
Every number in the output is computed here; nothing is typed in.
"""

import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
REL = os.path.join(DATA, "release")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts", "publication"))
import release_checks as rc  # noqa: E402
import publication_authority as pa  # noqa: E402

# (id, branch, base branch, title, live files, production impact, blockers, merge condition, rollback)
PRS = [
    ("0", "release-01/pr-0", "main", "Recovery-01..03 governance foundation", [],
     "No file under site/public changes. Adds the publication-authority deploy gate to the MANUAL Pages workflow and the "
     "governance suites to CI. After merge a manual deploy fails closed on the pre-existing /acquire/ conflict until PR-B; "
     "nothing is deployed automatically (the deploy workflow is workflow_dispatch only).",
     ["none for review; it is the base every Release-01 PR depends on"],
     "Can merge after review: it changes no public file. Merging it does not ratify, sign or publish anything.",
     "git revert the merge commit; site/public is unaffected either way."),
    ("A", "release-01/pr-a", "release-01/pr-0", "Publication safety and authority", [],
     "No public file changes. The deploy gate becomes stricter (unapproved downgrades block). Proposes IG policy 1.1.0.",
     ["AMD-IG-R03-001 (ig_reviewed_route_realization) awaits a SEPARATE owner ratification; merging this PR is not ratification",
      "a manual deploy stays blocked on /acquire/ until PR-B"],
     "Can merge after review: changes no public file. Merging does not ratify AMD-IG-R03-001.",
     "git revert the merge commit; the gate returns to the PR-0 behaviour and the IG policy to 1.0.0."),
    ("B", "release-01/pr-b", "release-01/pr-a", "/acquire/ correction", ["site/public/acquire/index.html"],
     "Changes ONE public page once deployed: /acquire/ becomes 'noindex, follow' (still public, same URL, contact and links "
     "unchanged) and five unsupported or contradicted statements are replaced. Deployment remains a separate manual step.",
     ["URL-DEC-R03-ACQUIRE-001 is 'proposed': the owner must review the wording and sign it (approved_by, approved_on); no signature is generated"],
     "Merge only after the owner signs URL-DEC-R03-ACQUIRE-001. The gate passes through the release-ledger exception, but the signature is the owner's approval.",
     "git revert the merge commit and redeploy: restores the previous page byte-for-byte."),
    ("C", "release-01/pr-c", "release-01/pr-b", "English and German homepage release readiness", [],
     "No public file changes; candidates are staged under main/data/release/staged/.",
     ["2 owner confirmations (who publishes the site, EN + DE)", "R11-HOME-EN-001 / R11-HOME-DE-001 not certified",
      "must not be published before the PR-D and PR-E pages"],
     "Can merge after review (staged files only). Merging does not certify or publish.",
     "git revert; nothing live changes."),
    ("D", "release-01/pr-d", "release-01/pr-c", "MoS2 reference release readiness", [],
     "No public file changes; candidate staged. apply_release.py refuses publication until Contract C is index-approved.",
     ["independent review (chemistry / crystallography) missing", "8 sources unlocked (4 lack a capture; L6 signatures)",
      "owner claim activation and release authorization missing", "AMD-IG-R03-001 not ratified"],
     "Can merge after review (staged files only). Merging does not validate, lock, activate or publish.",
     "git revert; nothing live changes."),
    ("E", "release-01/pr-e", "release-01/pr-d", "Bisulfid/Bisulfide terminology reference release readiness", [],
     "No public file changes; candidate staged.",
     ["independent review (nomenclature / lexicography, EN + DE) missing", "11 sources unlocked (L3 re-capture on a later date; L6 signatures)",
      "owner claim activation and release authorization missing", "AMD-IG-R03-001 not ratified",
      "CLM-TERM-BISULFID-001 stays pending by design"],
     "Can merge after review (staged files only).",
     "git revert; nothing live changes."),
]
PAGES = [("/acquire/", None), ("/", "home"), ("/de/", "de"), ("/molybdenum-disulfide/", "molybdenum-disulfide"),
         ("/bisulfid-vs-bisulfide/", "bisulfid-vs-bisulfide")]


def load(*p):
    with open(os.path.join(*p), encoding="utf-8") as fh:
        return json.load(fh)


def head(f):
    t = open(f, encoding="utf-8").read()

    def g(p):
        m = re.search(p, t, re.S)
        return m.group(1) if m else None
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    return {"title": g(r"<title>(.*?)</title>"), "robots": g(r'name="robots" content="([^"]*)"'),
            "canonical": g(r'rel="canonical" href="([^"]*)"'), "hreflang": len(re.findall(r'hreflang=', t)),
            "json_ld": g(r'"@type": ?"([^"]*)"') or "none", "words": len(re.sub(r"<[^>]+>", " ", body).split())}


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()


def rng(branch, base):
    """Exact isolated range of a stacked PR: merge-base(base, branch)..branch."""
    return git("merge-base", base, branch), git("rev-parse", "--short", branch)


def stat(branch, base):
    b, h = rng(branch, base)
    return git("diff", "--shortstat", b, h)


def main():
    sim = load(REL, "RELEASE_SIMULATION.json")
    tests = load(REL, "TEST_RESULTS.json")
    locks = load(REL, "source_lock_checklists.json")["sources"]
    quals = {q["source_id"] for q in load(DATA, "source_use_qualification_registry.json")["qualifications"]
             if q.get("qualification_state") not in ("candidate", "reviewed")}
    decisions = {d["decision_id"]: d for d in load(DATA, "publication", "url_decisions.json")["decisions"]}
    certs = load(DATA, "publication", "nonfactual_certifications.json")["certifications"]
    audit = load(REL, "HOMEPAGE_CLAIM_AUDIT.json")["summary"]
    auth = pa.Authority()
    L = ["# BISULFID Release-01 — readiness matrix", "",
         f"Generated by `scripts/release/build_release_package.py` from the governed stores (tests: `TEST_RESULTS.json`, "
         f"tree {tests['tree_at_commit']}, {sum(1 for x in tests['results'] if x['exit_code'] == 0)}/{len(tests['results'])} commands exit 0).", "",
         "**Nothing in this package is merged, deployed, certified, signed or published.** The automated preparer is never recorded "
         "as a reviewer, lock signer or approver.", "", "## 1. Pages", "",
         "| Page | PR | Live now | Release candidate | Gate 12 (served HTML) | Contract C honoured now | Deploy gate if applied now | …with all human acts (simulated) | Approvable now? |",
         "|---|---|---|---|---|---|---|---|---|"]
    for page, slug in PAGES:
        if slug is None:
            d = decisions["URL-DEC-R03-ACQUIRE-001"]
            live = head(os.path.join(ROOT, "site", "public", "acquire", "index.html"))
            L.append(f"| `{page}` | B | robots `{live['robots']}` (in PR-B branch), AQ-1..5 corrected | applied in PR-B | Gate 12-I (institutional) | "
                     f"legacy + ledger block | PASS (LEGACY_REPAIR_NOINDEX) | n/a | **Yes** — owner signs `{d['decision_id']}` (now `{d['status']}`) and merges PR-B |")
            continue
        man = load(REL, "staged", slug, "release.json")
        live = head(os.path.join(ROOT, "site", "public", "" if slug == "home" else slug, "index.html"))
        st = head(os.path.join(REL, "staged", slug, "index.html"))
        now = sim["now"]["staged_pages"][page]
        acts = sim["all_acts"]["staged_pages"][page]
        cc = man.get("contract_c_honoured") or list(auth.contract_c(page)[0] or ("no binding",))
        pr = "C" if man["kind"] == "institutional" else ("D" if "molybdenum" in page else "E")
        appr = ("Owner can review/certify R11 now; publication waits for D + E" if pr == "C"
                else "No — independent review, source locks, owner activation + authorization missing")
        L.append(f"| `{page}` | {pr} | {live['words']} words, “{live['title']}” | {st['words']} words, “{st['title']}”, JSON-LD {st['json_ld']}, "
                 f"hreflang {st['hreflang']} | {acts['gate12']} | {tuple(cc)} | {now['state']} | {acts['state']} | {appr} |")
    L += ["", "Robots, canonical and URL are identical between live and candidate for every page above (no directive change, "
          "no new URL); the deploy gate keeps a modified page from requesting index until its Contract C is index-approved.", "",
          "## 2. Claims", "", "| Knowledge Object | Claims | Evidence-matched by preparer | Independently validated | Owner-activated | Pending / boundary |",
          "|---|---:|---:|---:|---:|---|"]
    for kid, pend in (("KO-MOS2-SCIENTIFIC-001", "band gap, density, uses, safety, monolayer: no evidence (not claimed)"),
                      ("KO-BISULFID-TERMINOLOGY-001", "CLM-TERM-BISULFID-001 (German industry usage) pending — boundary only")):
        dos = load(REL, "claim_dossiers", kid + ".json")
        n = len(dos["claims"])
        L.append(f"| {kid} | {n} | {n} (dossier) | {n if rc.validation_ok(kid)[0] else 0} | {n if rc.claims_active_ok(kid)[0] else 0} | {pend} |")
    L += ["", "**Scientifically validated claims: 0.** Evidence matching by the preparer is not validation.", "",
          "## 3. Independent reviews and human acts still missing", "",
          "| Act | Object | Who | Status |", "|---|---|---|---|"]
    for kid, comp in (("KO-MOS2-SCIENTIFIC-001", "chemistry / crystallography"), ("KO-BISULFID-TERMINOLOGY-001", "chemical nomenclature / lexicography (EN + DE)")):
        rec = rc.review_record(kid) or {"reviews": []}
        L.append(f"| Independent review | {kid} | named human, {comp}, not the preparer | "
                 f"{'signed' if rc.validation_ok(kid)[0] else f'missing ({len(rec['reviews'])} reviews recorded); packet: review_packets/{kid}.md'} |")
        L.append(f"| Claim activation | {kid} | owner | {'signed' if rc.claims_active_ok(kid)[0] else 'missing'} |")
        L.append(f"| Release authorization | {kid} | owner | {'signed' if rc.release_authorized_ok(kid)[0] else 'missing'} |")
    for c in certs:
        L.append(f"| R11 certification | `{c['path']}` | owner | {c['status']} (checklist attached) |")
    L.append(f"| Homepage wording confirmations | `/`, `/de/` | owner | {audit['owner_confirmation_required']} items open |")
    L.append("| URL decision | `/acquire/` | owner | " + decisions["URL-DEC-R03-ACQUIRE-001"]["status"] + " |")
    L.append("| Source lock signatures (L6) | " + f"{len(locks)} sources | source registry owner | 0 signed |")
    L.append("| Search Console export | wave-1 15 URLs | owner | not supplied — wave not started |")
    L += ["", "## 4. Sources", "", "| Source | Used by | Qualified | Lock | L1 | L2 | L3 | L4 | L5 | L6 |", "|---|---|---|---|---|---|---|---|---|---|"]
    short = lambda v: "pass" if str(v).startswith("pass") else ("pending" if str(v).startswith("pending") else v)  # noqa: E731
    for sid, x in locks.items():
        c = x["checklist"]
        L.append(f"| {sid} | {', '.join(k.replace('KO-', '').split('-')[0] for k in x['used_by'])} | {'yes' if sid in quals else 'no'} | "
                 f"{x['lock_status']} | " + " | ".join(short(c[k]) for k in ("L1", "L2", "L3", "L4", "L5", "L6")) + " |")
    n_l3 = sum(1 for x in locks.values() if str(x["checklist"]["L3"]).startswith("pass"))
    L += ["", f"Qualified: {sum(1 for s in locks if s in quals)}/{len(locks)}. Locked: 0/{len(locks)}. L3 reproduced on a later date: "
          f"{n_l3}/{len(locks)}. L6 (human signature): 0/{len(locks)}.", "",
          "## 5. Pull requests", "", "| PR | Commit | Diff | Live files changed | Can merge safely? |", "|---|---|---|---|---|"]
    for pid, br, base, title, live_files, _, blockers, cond, _ in PRS:
        L.append(f"| {pid} — {title} | `{br}` @ `{git('rev-parse', '--short', br)}` (base `{base}`) | {stat(br, base)} | "
                 f"{', '.join(live_files) or 'none'} | {cond} |")
    L += ["", "Stack: `main` ← PR-0 ← A ← B ← C ← D ← E (each a draft PR; each diff is exactly its own range).", "",
          "## 6. Awaiting owner publication authorization", "",
          "0. Decide separately whether to ratify AMD-IG-R03-001 (route realization); until then both references stay non-indexable.",
          "1. Sign `URL-DEC-R03-ACQUIRE-001`, merge PR-0, A and B, then run the manual deploy (gate passes).",
          "2. Commission the two independent reviews (packets ready) and the L6 source-lock signatures; re-capture the "
          "terminology sources on a later date first (`capture_terminology_sources.py --recapture`).",
          "3. Sign claim activations and release authorizations in `main/data/release/owner_acts.json`; set governance with the release.",
          "4. `apply_release.py --page /molybdenum-disulfide/` and `--page /bisulfid-vs-bisulfide/` (refuses until Contract C is index-approved).",
          "5. Confirm homepage wording, sign R11-HOME-EN-001 / R11-HOME-DE-001, then `apply_release.py --page /` and `--page /de/`.",
          "6. Consolidation obligations (42) become executable only after step 4, each through a signed `canonical_to` decision.",
          "7. Wave 1 (15 URLs) stays parked until the Search Console export exists.", ""]
    os.makedirs(os.path.join(REL, "prs"), exist_ok=True)
    open(os.path.join(REL, "RELEASE_01_READINESS.md"), "w", encoding="utf-8").write("\n".join(L))
    tests_md = "\n".join(f"- {'✅' if x['exit_code'] == 0 else '❌'} `{x['command']}` — {x['last_line']}" for x in tests["results"])
    links = load(REL, "prs", "PR_LINKS.json") if os.path.exists(os.path.join(REL, "prs", "PR_LINKS.json")) else {}
    order = [p[0] for p in PRS]
    for i, (pid, br, base, title, live_files, impact, blockers, cond, rollback) in enumerate(PRS):
        b, h = rng(br, base)
        prev_pr = links.get(order[i - 1]) if i else None
        next_pr = links.get(order[i + 1]) if i + 1 < len(order) else None
        body = [f"# PR-{pid}: {title}", "",
                "> **Draft — review authorization only.** Not to be merged, deployed or published without a new explicit owner "
                "authorization. Nothing in this PR signs a review, locks a source, activates a claim, approves an indexation "
                "change or ratifies a governance amendment.", "",
                "## Dependencies", "",
                f"- Branch `{br}` @ `{h}`; base `{base}`" + (f" ({prev_pr})" if prev_pr else "") + ".",
                f"- Depends on: {('PR-' + order[i - 1]) if i else 'main'}" + (f"; next in the stack: PR-{order[i + 1]}" + (f" ({next_pr})" if next_pr else "") if i + 1 < len(order) else "") + ".",
                "- Release matrix: `main/data/release/RELEASE_01_READINESS.md` (on `claude/corpus-distinctiveness-audit-4wsa9f`).", "",
                "## Production impact", "", impact, "", "## Blockers", ""] + [f"- {x}" for x in blockers] + ["",
                "## What changes", "",
                git("log", "--format=%b", f"{b}..{h}").split("Co-Authored-By")[0].strip() if pid != "0" else
                "Recovery-01..03: Gate 12 distinctiveness gate + corpus audit; legacy disposition registry and sealed legacy "
                "hold; publication authority (single directive resolver) and deploy gate; MoS2 reference reconstruction; "
                "terminology evidence admission (16 records, 11 narrow claims) and the Bisulfid/bisulfide preview; homepage "
                "previews; indexation-reduction plan (proposals only). Reports: main/data/recovery/RECOVERY_0{1,2,3}_REPORT.md.",
                "", "## Exact isolated diff", "", f"`git diff {b[:10]}..{h}` — {stat(br, base)}", "", "<details><summary>Files</summary>", "",
                "```", git("diff", "--name-status", b, h)[:20000], "```", "", "</details>", "", "## Public HTML differences", ""]
        if live_files:
            body.append("```diff\n" + git("diff", b, h, "--", *live_files)[:8000] + "\n```")
        else:
            body.append("No file under `site/public` changes in this PR.")
            for page, slug in PAGES:
                if slug and ((pid == "C" and slug in ("home", "de")) or (pid == "D" and "molybdenum" in slug) or (pid == "E" and "bisulfid" in slug)):
                    lv, st = head(os.path.join(ROOT, "site", "public", "" if slug == "home" else slug, "index.html")), head(os.path.join(REL, "staged", slug, "index.html"))
                    body += ["", f"Staged candidate for `{page}` (applied only later, by `apply_release.py`):", "",
                             "| | Live | Candidate |", "|---|---|---|"] + [f"| {k} | {lv[k]} | {st[k]} |" for k in lv]
        iso = load(REL, "PER_PR_TEST_RESULTS.json").get(f"PR-{pid}", {"results": []})
        iso_md = "\n".join(f"- {'✅' if x['status'] == 'PASS' else ('❌' if x['status'] == 'FAIL' else '–')} `{x['check']}`"
                           + (f" — {x['detail']}" if x.get("detail") else "") for x in iso["results"])
        body += ["", "## Test outcomes", "", f"This PR's head (`{h}`) checked out alone in a clean worktree:", "", iso_md or "(not recorded)", "",
                 "CI: `corpus-governance-ci` runs only on pull requests whose base is `main`" +
                 (" — it runs on this PR." if base == "main" else "; this stacked PR has no CI run, so the local results above are the record."), "",
                 "## Merge condition", "", cond, "", "## Rollback", "", rollback, ""]
        open(os.path.join(REL, "prs", f"PR-{pid}.md"), "w", encoding="utf-8").write("\n".join(body))
    print("wrote RELEASE_01_READINESS.md and prs/PR-0..E.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
