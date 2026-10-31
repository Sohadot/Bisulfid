#!/usr/bin/env python3
"""validate_distinctiveness.py — Gate 12: Page Distinctiveness & Information Gain (BLOCKING).

Real enforcement (not a placeholder). Policy: main/data/distinctiveness/gate12_policy.json.
Engine: scripts/validators/distinctiveness_core.py.

Modes
-----
  (default) --gate         Publication candidates in the markdown corpus (front matter
                           publication_eligibility/indexable/in_sitemap/public status, or
                           routes.json indexable/published) are compared EXHAUSTIVELY against
                           the whole markdown corpus (drafts included). Exit 1 if any
                           candidate is not Gate-12 PASS.
  --surface DIR            Every indexable HTML page under DIR (robots index) is a live
                           publication surface. LSH audit universe. Exit 1 if any fails.
  --page PATH              Evaluate one markdown page exhaustively; print diagnostics.
  --audit                  Whole-corpus audit (markdown corpus + site/public surface +
                           reference-production pages). Writes the durable reports under main/data/distinctiveness/.
                           Exit 0: the audit measures; it never changes publication state.

Common: --json OUT writes the machine-readable result.
"""

import argparse
import json
import re
import os
import statistics
import sys
import time
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import distinctiveness_core as dc  # noqa: E402

OUT_DIR = os.path.join(dc.DATA, "distinctiveness")
TS = dc.ROOT


def _routes_candidates():
    path = os.path.join(dc.DATA, "routes.json")
    if not os.path.exists(path):
        return set()
    d = dc.load_json(path)
    routes = d if isinstance(d, list) else d.get("routes", [])
    out = set()
    for r in routes:
        if r.get("indexable") is True or r.get("in_sitemap") is True or \
                str(r.get("status", "")).lower() in ("published", "live", "released"):
            if r.get("content_file"):
                out.add(os.path.normpath(r["content_file"]))
    return out


def _print_verdict(v, verbose=True):
    print(f"[{v['verdict']}] {v['page']}")
    if not verbose:
        return
    t = v["text"]
    print(f"    text: S={t['similarity']:.3f} (jaccard {t['jaccard']:.3f}, overlap "
          f"{t['overlap_coefficient'] if t['overlap_coefficient'] is not None else 'n/a'}) "
          f"closest={t['closest_page']} -> {t['status']}")
    s = v["structure"]
    print(f"    structure: skeleton shared with {s['shared_with_pages']} page(s), best ratio "
          f"{s['best_sequence_ratio']}, structural_template={s['structural_template']}")
    print(f"    boilerplate: template_sentence_ratio={v['boilerplate']['template_sentence_ratio']}")
    ig = v["information_gain"]
    print(f"    information gain: {ig['valid_units']}/{ig['registered_units']} valid unit(s), "
          f"required {ig['required']} -> {ig['status']}")
    for u in ig.get("units", []):
        if not u["valid"]:
            print(f"      - {u['unit_id']}: " + "; ".join(u["reasons"]))
    print(f"    substantive tokens={v['substantive_tokens']} infra tokens={v['infra_tokens']} "
          f"entity_substitution={v['entity_substitution_detected']}")
    for f in v["failures"]:
        print(f"    FAIL   {f}")
    for r in v["reviews"]:
        print(f"    REVIEW {r}")


def _write_json(path, obj):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, ensure_ascii=False, sort_keys=False)
        fh.write("\n")


# --------------------------------------------------------------------------- gate modes

def run_gate(policy, args):
    t0 = time.time()
    pages = dc.load_markdown_pages(policy)
    universe = dc.Universe(pages, policy)
    ctx = dc.IGContext()
    uidx = dc.unit_statement_index(ctx, policy, universe.by_id)
    from_routes = _routes_candidates()
    cands = [p for p in pages if p.publication_candidate or os.path.normpath(p.id) in from_routes]
    print("=" * 72)
    print("Gate 12 — Page Distinctiveness & Information Gain (BLOCKING)")
    print(f"policy {policy['version']}; markdown corpus {len(pages)} pages; publication candidates {len(cands)}")
    print("=" * 72)
    results = [dc.gate12_verdict(p, universe, policy, ctx, unit_index=uidx) for p in cands]
    for v in results:
        _print_verdict(v)
    blocked = [v for v in results if v["verdict"] != "PASS"]
    out = {"gate": 12, "mode": "gate", "policy_version": policy["version"], "corpus_pages": len(pages),
           "publication_candidates": len(cands), "blocked": len(blocked),
           "runtime_seconds": round(time.time() - t0, 2), "results": results}
    if args.json:
        _write_json(args.json, out)
    print("-" * 72)
    if blocked:
        print(f"GATE 12 FAIL: {len(blocked)} publication candidate(s) blocked (publication/indexation prohibited).")
        return 1
    print(f"GATE 12 PASS: {len(cands)} publication candidate(s); none blocked.")
    if not cands:
        print("NOTE: no markdown page is currently a publication candidate; every draft remains non-public.")
    return 0


def run_page(policy, args):
    pages = dc.load_markdown_pages(policy)
    universe = dc.Universe(pages, policy)
    ctx = dc.IGContext()
    with open(args.page, encoding="utf-8") as fh:
        page = dc.parse_markdown(args.page, fh.read(), policy)
    v = dc.gate12_verdict(page, universe, policy, ctx, unit_index=dc.unit_statement_index(ctx, policy, universe.by_id))
    _print_verdict(v)
    if args.json:
        _write_json(args.json, v)
    return 0 if v["verdict"] == "PASS" else 1


# --------------------------------------------------------------------------- audit machinery

class _UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def _route_for_path():
    d = dc.load_json(os.path.join(dc.DATA, "routes.json"))
    return {r["path"]: r["route_id"] for r in (d if isinstance(d, list) else d["routes"])}


def institutional_bindings(pages, inst):
    """Gate 12-I binding per page (None for knowledge-reference pages)."""
    rfp = _route_for_path()
    out = []
    for p in pages:
        if p.surface == "html":
            out.append(inst.lookup(route_id=rfp.get(p.route_id), path=p.route_id))
        else:
            out.append(inst.lookup(route_id=p.route_id))
    return out


def analyse_universe(name, pages, policy, ctx, inst=None):
    """LSH audit of one surface. Returns (summary dict, per-page verdict list, universe)."""
    t0 = time.time()
    u = dc.Universe(pages, policy)
    confirmed, pair_stats = u.audit_pairs()
    ts = policy["text_similarity"]
    size = {u.rep_of_hash[h]: len(m) for h, m in u.groups.items()}
    rep_of_page = {}
    for h, members in u.groups.items():
        for m in members:
            rep_of_page[m] = members[0]

    # Best cross-group neighbour per representative.
    best = {}
    for i, j, s, jac, oc in confirmed:
        for a, b in ((i, j), (j, i)):
            if a not in best or s > best[a][0]:
                best[a] = (s, jac, oc, b)

    # Page-level nearest neighbour (exact-group sibling => 1.0).
    page_text = {}
    for idx, p in enumerate(pages):
        r = rep_of_page.get(idx)
        if r is None:
            page_text[idx] = {"similarity": 0.0, "jaccard": 0.0, "overlap_coefficient": None, "closest_page": None}
            continue
        members = u.groups[p.body_hash]
        if len(members) > 1:
            other = members[1] if members[0] == idx else members[0]
            page_text[idx] = {"similarity": 1.0, "jaccard": 1.0, "overlap_coefficient": 1.0,
                              "closest_page": pages[other].id}
        elif r in best:
            s, jac, oc, b = best[r]
            page_text[idx] = {"similarity": round(s, 4), "jaccard": round(jac, 4),
                              "overlap_coefficient": None if oc is None else round(oc, 4),
                              "closest_page": pages[b].id}
        else:
            page_text[idx] = {"similarity": 0.0, "jaccard": 0.0, "overlap_coefficient": None,
                              "closest_page": None, "note": "no LSH candidate (below detection floor)"}

    uidx = dc.unit_statement_index(ctx, policy, u.by_id)
    inst = inst or dc.InstitutionalRegistry()
    binds = institutional_bindings(pages, inst)
    verdicts = [dc.gate12_verdict(p, u, policy, ctx, text=page_text[i], unit_index=uidx, institutional=binds[i])
                for i, p in enumerate(pages)]

    # Pair distribution at page-pair level (exact groups expand combinatorially).
    def pairs_at_or_above(lo, hi=1.01):
        n = 0
        if lo <= 1.0 < hi:
            n += sum(k * (k - 1) // 2 for k in size.values())
        for i, j, s, _, _ in confirmed:
            if lo <= s < hi:
                n += size[i] * size[j]
        return n

    raw_groups = Counter(dc.h64(" ".join(p.raw_tokens)) for p in pages if p.raw_tokens)
    exact_raw_dup_pages = sum(c for c in raw_groups.values() if c > 1)
    masked_ident_pages = sum(len(m) for m in u.groups.values() if len(m) > 1)

    # Clusters at >= 0.90 / 0.80 / 0.70 (union-find over representatives).
    clusters = {}
    for thr in (0.90, 0.80, 0.70):
        uf = _UF()
        for r in u.reps:
            uf.find(r)
        for i, j, s, _, _ in confirmed:
            if s >= thr:
                uf.union(i, j)
        comp = defaultdict(list)
        for r in u.reps:
            comp[uf.find(r)].append(r)
        sizes = sorted((sum(size[r] for r in reps), root, reps) for root, reps in comp.items())
        sizes.reverse()
        multi = [x for x in sizes if x[0] > 1]
        clusters[thr] = {"clusters": len(multi), "pages_in_clusters": sum(x[0] for x in multi), "detail": multi}

    maxsims = sorted(v["text"]["similarity"] for v in verdicts)

    def pct(q):
        if not maxsims:
            return None
        k = min(len(maxsims) - 1, max(0, int(round(q * (len(maxsims) - 1)))))
        return round(maxsims[k], 4)

    cross = [c[2] for c in confirmed]
    fails = [v for v in verdicts if v["verdict"] == "FAIL"]
    comp_fail = Counter()
    for v in verdicts:
        for f in v["failures"]:
            comp_fail[f.split(":", 1)[0]] += 1
    text_only = Counter(v["text"]["status"] for v in verdicts)

    # Families with highest boilerplate ratio.
    fam = defaultdict(list)
    for v in verdicts:
        fam[v["family"]].append(v["boilerplate"]["template_sentence_ratio"])
    fam_rank = sorted(((statistics.mean(x), len(x), f) for f, x in fam.items() if len(x) >= 10), reverse=True)

    # Top repeated substantive sentences.
    sent_text = {}
    for p in pages:
        for h, _, s in p.sentences:
            sent_text.setdefault(h, s)
    top_sent = [{"pages": c, "share_of_corpus": round(c / len(pages), 4), "sentence_entity_masked": sent_text[h]}
                for h, c in u.sent_df.most_common(25)]

    by_lang = defaultdict(Counter)
    by_cohort = defaultdict(Counter)
    by_kofam = defaultdict(Counter)
    for v in verdicts:
        nd = v["text"]["similarity"] >= ts["fail_at_or_above"]
        for bucket, key in ((by_lang, v["language"] or "?"), (by_cohort, v["family"].split("|")[1]),
                            (by_kofam, v["ko_family"])):
            bucket[key]["pages"] += 1
            bucket[key]["near_duplicate_ge_0_70"] += int(nd)
            bucket[key]["gate12_fail"] += int(v["verdict"] == "FAIL")

    def table(b):
        return {k: dict(c, near_duplicate_share=round(c["near_duplicate_ge_0_70"] / c["pages"], 4))
                for k, c in sorted(b.items(), key=lambda kv: -kv[1]["pages"])}

    summary = {
        "surface": name,
        "total_pages_scanned": len(pages),
        "substantive_pages_compared": sum(1 for p in pages if p.masked_tokens),
        "pages_with_empty_substantive_body": sum(1 for p in pages if not p.masked_tokens),
        "distinct_entity_masked_bodies": len(u.groups),
        "distinct_raw_bodies": len(raw_groups),
        "exact_duplicate_pages_raw_text": exact_raw_dup_pages,
        "entity_masked_identical_pages": masked_ident_pages,
        "candidate_discovery": pair_stats,
        "confirmed_pairs_between_distinct_bodies_ge_0_30": len(confirmed),
        "page_pairs": {
            "ge_0_90": pairs_at_or_above(0.90),
            "ge_0_80": pairs_at_or_above(0.80),
            "ge_0_70": pairs_at_or_above(0.70),
            "review_band_0_55_to_0_70": pairs_at_or_above(0.55, 0.70),
            "total_possible_pairs": len(pages) * (len(pages) - 1) // 2,
        },
        "clusters": {f"ge_{str(t).replace('.', '_')}": {"clusters": c["clusters"], "pages_in_clusters": c["pages_in_clusters"],
                                                        "largest_cluster_size": c["detail"][0][0] if c["detail"] else 0}
                     for t, c in clusters.items()},
        "page_max_similarity_percentiles": {"p10": pct(0.10), "p25": pct(0.25), "p50": pct(0.50), "p75": pct(0.75),
                                             "p90": pct(0.90), "p99": pct(0.99), "max": pct(1.0),
                                             "note": ("per-page nearest-neighbour S (exact-confirmed over all distinct bodies)"
                                                      if "exhaustive_pairs" in pair_stats else
                                                      "per-page nearest-neighbour S; pages without an LSH candidate count as 0 (lower bound)")},
        "page_max_similarity_histogram": {
            "eq_1_00": sum(1 for x in maxsims if x >= 0.99995),
            "0_90_to_1_00": sum(1 for x in maxsims if 0.90 <= x < 0.99995),
            "0_80_to_0_90": sum(1 for x in maxsims if 0.80 <= x < 0.90),
            "0_70_to_0_80": sum(1 for x in maxsims if 0.70 <= x < 0.80),
            "0_55_to_0_70": sum(1 for x in maxsims if 0.55 <= x < 0.70),
            "0_30_to_0_55": sum(1 for x in maxsims if 0.30 <= x < 0.55),
            "below_0_30": sum(1 for x in maxsims if x < 0.30)},
        "highest_similarity_between_distinct_bodies": round(max(cross), 4) if cross else None,
        "pages_ge_0_70_nearest_neighbour": sum(1 for x in maxsims if x >= ts["fail_at_or_above"]),
        "pages_in_review_band": sum(1 for x in maxsims if ts["review_at_or_above"] <= x < ts["fail_at_or_above"]),
        "pages_below_0_55": sum(1 for x in maxsims if x < ts["review_at_or_above"]),
        "gate12_verdicts": dict(Counter(v["verdict"] for v in verdicts)),
        "gate12_fail_count": len(fails),
        "failure_components": dict(comp_fail),
        "text_component_status": dict(text_only),
        "pages_failing_without_information_gain_component": sum(
            1 for v in verdicts if any(not f.startswith("information_gain") for f in v["failures"])),
        "publication_candidates_in_surface": sum(1 for v in verdicts if v["publication_candidate"]),
        "publication_candidates_failing": sum(1 for v in verdicts if v["publication_candidate"] and v["verdict"] != "PASS"),
        "drafts_audited": sum(1 for v in verdicts if v["is_draft"]),
        "mean_template_sentence_ratio": round(statistics.mean(v["boilerplate"]["template_sentence_ratio"] for v in verdicts), 4),
        "median_substantive_tokens": statistics.median(v["substantive_tokens"] for v in verdicts),
        "families_highest_boilerplate": [{"family": f, "pages": n, "mean_template_sentence_ratio": round(m, 4)}
                                         for m, n, f in fam_rank[:15]],
        "top_repeated_substantive_sentences": top_sent,
        "by_language": table(by_lang),
        "by_cohort": table(by_cohort),
        "by_knowledge_object_family": table(by_kofam),
        "runtime_seconds": round(time.time() - t0, 2),
    }
    summary["largest_clusters_ge_0_70"] = describe_clusters(clusters[0.70]["detail"][:12], u, size, verdicts, pages)
    return summary, verdicts, u


def _slots(a, b, limit=8):
    """Differing token spans between two raw substantive bodies (the variable slots)."""
    import difflib
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            out.append({"a": " ".join(a[i1:i2])[:80], "b": " ".join(b[j1:j2])[:80]})
            if len(out) >= limit:
                break
    return out, round(sm.ratio(), 4)


def describe_clusters(detail, u, size, verdicts, pages):
    vby = {v["page"]: v for v in verdicts}
    out = []
    for total, root, reps in detail:
        member_idx = [m for r in reps for m in u.groups[u.pages[r].body_hash]]
        members = [pages[m] for m in member_idx]
        biggest_rep = max(reps, key=lambda r: size[r])
        rep_page = pages[biggest_rep]
        sk = Counter(p.skeleton for p in members).most_common(1)[0][0]
        a = rep_page
        b = next((p for p in members if p.id != a.id and p.raw_tokens != a.raw_tokens), None)
        slots, raw_ratio = _slots(a.raw_tokens, b.raw_tokens) if b else ([], 1.0)
        langs = Counter(p.language or "?" for p in members)
        fams = Counter(p.family for p in members)
        kof = Counter(p.ko_family for p in members)
        ratios = [vby[p.id]["boilerplate"]["template_sentence_ratio"] for p in members]
        entities = Counter(dc.entity_key(p) for p in members)
        public = sum(1 for p in members if p.public_indexable)
        drafts = sum(1 for p in members if p.is_draft)
        out.append({
            "cluster_size": total,
            "distinct_entity_masked_bodies": len(reps),
            "distinct_entities": len(entities),
            "representative_page": rep_page.id,
            "shared_substantive_skeleton": list(sk),
            "representative_substantive_body_entity_masked": " ".join(rep_page.masked_tokens)[:600],
            "variable_slots_example": {"page_a": a.id, "page_b": b.id if b else None, "slots": slots,
                                       "raw_text_similarity_ratio": raw_ratio},
            "estimated_repeated_text_ratio": round(statistics.mean(ratios), 4),
            "what_genuinely_differs": ("only entity-name/variant slots; entity-masked bodies are identical"
                                       if len(reps) == 1 else
                                       f"entity slots plus {len(reps)} template variants (audience/layer bullets); no evidence-backed knowledge units"),
            "languages": dict(langs.most_common()),
            "families": dict(fams.most_common(6)),
            "knowledge_object_families": dict(kof.most_common()),
            "sample_entities": [e for e, _ in entities.most_common(8)],
            "public_indexable_members": public,
            "draft_members": drafts,
            "recommendation": _recommend(members, entities, public),
        })
    return out


def _recommend(members, entities, public):
    recs = []
    if public:
        recs.append("withdraw from indexation candidates (Gate 12 FAIL on a live indexable surface); rebuild only from Knowledge Objects")
    if len(entities) < len(members) / 2:
        recs.append("consolidate: many audience/layer variants of the same entity -> one Knowledge Object with modules")
    else:
        recs.append("rebuild/convert to Knowledge Objects only where governed evidence exists; otherwise remain non-public")
    recs.append("remove from publication candidates without deleting the underlying planned entity; no route deletion in this sprint")
    return recs


LEGACY_BASELINE_COMMIT = "9d944d736d"  # last commit before Reference Production replaced the MoS2 draft


def _legacy_text(path):
    """The pre-reconstruction version of a content file (git), or None."""
    import subprocess
    try:
        return subprocess.run(["git", "show", f"{LEGACY_BASELINE_COMMIT}:{path}"], cwd=dc.ROOT, capture_output=True,
                              text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def control_report(policy, md_pages, md_u, html_pages, html_u, ctx):
    """Reference-production pages (IG-registry entries bound to a Knowledge Object): Gate 12 against
    both universes, before/after versus the legacy versions of the SAME route, and combined eligibility."""
    out = []
    oc_min = policy["text_similarity"]["overlap_coefficient_min_shingles"]
    uidx = dc.unit_statement_index(ctx, policy, md_u.by_id)
    for entry in ctx.registry.get("pages", []):
        if not entry.get("knowledge_object_id"):
            continue
        path = os.path.join(dc.ROOT, entry["page"])
        page = md_u.by_id.get(entry["page"])
        if page is None:
            with open(path, encoding="utf-8") as fh:
                page = dc.parse_markdown(path, fh.read(), policy)
        md_v = dc.gate12_verdict(page, md_u, policy, ctx, unit_index=uidx)
        html_near = html_u.nearest(page) if html_u else None
        before = {}
        legacy = _legacy_text(entry["page"])
        if legacy:
            q = dc.parse_markdown(path, legacy, policy, page_id=entry["page"] + "@" + LEGACY_BASELINE_COMMIT)
            qv = dc.gate12_verdict(q, md_u, policy, ctx, exclude_ids=(entry["page"],))
            s_, j, _ = dc.similarity(page.shingle_set, q.shingle_set, oc_min)
            before["legacy_markdown_draft@" + LEGACY_BASELINE_COMMIT] = {
                "similarity_to_reconstruction": round(s_, 4), "old_page_verdict": qv["verdict"],
                "old_page_failures": qv["failures"], "old_page_nearest": qv["text"],
                "old_page_substantive_tokens": qv["substantive_tokens"],
                "old_page_template_sentence_ratio": qv["boilerplate"]["template_sentence_ratio"]}
        for pid in ("main/content/de/pages/molybdenum-disulfide.md", "main/content/de/pages/terminology/molybdenum-disulfide.md"):
            q = md_u.by_id.get(pid)
            if q:
                before[pid] = {"similarity_to_reconstruction": round(dc.similarity(page.shingle_set, q.shingle_set, oc_min)[0], 4)}
        route_path = page.front.get("route_id")
        preview = None
        if html_u:
            routes = dc.load_json(os.path.join(dc.DATA, "routes.json"))
            routes = routes if isinstance(routes, list) else routes["routes"]
            rpath = next((r["path"] for r in routes if r["route_id"] == route_path), None)
            live_id = f"site/public{rpath}index.html" if rpath else None
            if live_id and live_id in html_u.by_id:
                q = html_u.by_id[live_id]
                qv = dc.gate12_verdict(q, html_u, policy, ctx)
                before["live_html" + rpath] = {
                    "similarity_to_reconstruction": round(dc.similarity(page.shingle_set, q.shingle_set, oc_min)[0], 4),
                    "live_verdict": qv["verdict"], "live_nearest": qv["text"], "live_substantive_tokens": qv["substantive_tokens"],
                    "live_template_sentence_ratio": qv["boilerplate"]["template_sentence_ratio"]}
            ppath = os.path.join(dc.DATA, "reference_production", "previews", (rpath or "/").strip("/"), "index.html")
            if os.path.exists(ppath):
                with open(ppath, encoding="utf-8") as fh:
                    pv = dc.parse_html(ppath, fh.read(), policy)
                near = html_u.nearest(pv, exclude_ids=(live_id,))
                preview = {"preview": dc.rel(ppath), "robots_noindex": not pv.public_indexable,
                           "nearest_in_public_html_surface": near,
                           "template_sentence_ratio_vs_surface": round(html_u.template_ratio(pv), 4),
                           "skeleton_shared_with_surface_pages": html_u.skeleton_match(pv)[0],
                           "substantive_tokens": len(pv.masked_tokens)}
        cc_inputs = None
        pc_id = entry.get("publication_candidate_id")
        if pc_id:
            pc = dc.load_json(os.path.join(dc.DATA, "publication_candidates", pc_id + ".json"))
            ps = pc["postures"]
            cc_inputs = {"governance": ps["governance_posture"], "evidence": ps["evidence_posture"],
                         "claim": ps["claim_posture"], "validation": ps["validation_posture"],
                         "ig": ps["information_gain_posture"], "release": ps["release_authorization"]}
        out.append({"control_page": page.id, "knowledge_object_id": entry["knowledge_object_id"],
                    "gate12_vs_markdown_corpus": md_v, "nearest_in_html_surface": html_near, "before_after": before,
                    "html_preview": preview,
                    "combined_publication_eligibility": dc.combined_publication_eligibility(md_v, cc_inputs),
                    "contract_c_inputs": cc_inputs})
    return out


def run_audit(policy, args):
    t0 = time.time()
    ctx = dc.IGContext()
    t = time.time()
    md_pages = dc.load_markdown_pages(policy)
    md_parse = time.time() - t
    md_summary, md_verdicts, md_u = analyse_universe("markdown_corpus", md_pages, policy, ctx)
    md_summary["parse_seconds"] = round(md_parse, 2)
    html_summary = html_verdicts = html_u = html_pages = None
    surface = os.path.join(dc.ROOT, policy["scope"]["html_surface_root"])
    if not args.no_html and os.path.isdir(surface):
        t = time.time()
        html_pages = dc.load_html_pages(policy, surface)
        html_parse = time.time() - t
        html_summary, html_verdicts, html_u = analyse_universe("public_html_surface", html_pages, policy, ctx)
        html_summary["parse_seconds"] = round(html_parse, 2)
        html_summary["indexable_pages"] = sum(1 for p in html_pages if p.public_indexable)
        html_summary["indexable_pages_failing_gate12"] = sum(
            1 for v in html_verdicts if v["public_indexable"] and v["verdict"] != "PASS")
    controls = control_report(policy, md_pages, md_u, html_pages, html_u, ctx)

    examples = {}
    for pid in ("main/content/de/pages/cohort-04-expansion/de/cohort04-de-actinium-sulfid.md",
                "main/content/de/pages/cohort-04-expansion/de/cohort04-de-aluminium-sulfid.md",
                "main/content/de/pages/cohort-04-expansion/de/cohort04-de-calcium-sulfid.md",
                "main/content/de/pages/molybdenum-disulfide.md",
                "main/content/en/pages/molybdenum-disulfide.md"):
        v = next((x for x in md_verdicts if x["page"] == pid), None)
        if v:
            examples[pid] = {k: v[k] for k in ("verdict", "failures", "text", "boilerplate", "structure",
                                                 "substantive_tokens", "infra_tokens", "entity_substitution_detected")}

    report = {
        "report_id": "CORPUS-DISTINCTIVENESS-AUDIT",
        "gate": 12,
        "policy_version": policy["version"],
        "generated_by": "scripts/validators/validate_distinctiveness.py --audit",
        "baseline_note": "Audit of the corpus as committed; drafts included; audit does not change publication state.",
        "markdown_corpus": md_summary,
        "public_html_surface": html_summary,
        "controls": controls,
        "representative_examples": examples,
        "runtime_seconds_total": round(time.time() - t0, 2),
    }
    os.makedirs(OUT_DIR, exist_ok=True)
    json_path = args.json or os.path.join(OUT_DIR, "CORPUS_DISTINCTIVENESS_AUDIT.json")
    _write_json(json_path, report)
    tsv_path = os.path.join(OUT_DIR, "CORPUS_DISTINCTIVENESS_PAGES.tsv")
    codes = {"near_duplicate": "N", "structural_template": "S", "template_prose": "T", "thin_body": "B",
             "information_gain": "I"}

    def short(pid):
        if not pid:
            return ""
        for pre in ("main/content/", "site/public/"):
            if pid.startswith(pre):
                pid = pid[len(pre):]
        return pid[:-len("/index.html")] + "/" if pid.endswith("/index.html") else pid

    with open(tsv_path, "w", encoding="utf-8") as fh:
        fh.write("# Gate 12 per-page verdicts. surface md = main/content/<path>, html = site/public/<path>index.html. "
                 "failures: N=near_duplicate S=structural_template T=template_prose B=thin_body I=information_gain\n")
        fh.write("surface\tpage\tverdict\tS\tclosest\ttemplate_ratio\tskeleton_shared\tig_units\tsubst_tokens\t"
                 "draft\tindexable\tfailures\n")
        for v in md_verdicts + (html_verdicts or []):
            comps = "".join(sorted({codes.get(f.split(":", 1)[0], "?") for f in v["failures"]}))
            fh.write("\t".join(str(x) for x in (
                "md" if v["surface"] == "markdown" else "html", short(v["page"]), v["verdict"], v["text"]["similarity"],
                short(v["text"]["closest_page"]), v["boilerplate"]["template_sentence_ratio"],
                v["structure"]["shared_with_pages"], v["information_gain"]["valid_units"], v["substantive_tokens"],
                int(v["is_draft"]), int(v["public_indexable"]), comps)) + "\n")
    print(json.dumps({"markdown": {k: md_summary[k] for k in ("total_pages_scanned", "gate12_fail_count", "page_pairs",
                                                              "clusters", "page_max_similarity_percentiles")},
                      "html": None if not html_summary else
                      {k: html_summary[k] for k in ("total_pages_scanned", "indexable_pages", "indexable_pages_failing_gate12",
                                                    "page_pairs", "clusters")},
                      "controls": [{"page": c["control_page"], "verdict": c["gate12_vs_markdown_corpus"]["verdict"],
                                    "eligibility": c["combined_publication_eligibility"]} for c in controls],
                      "runtime_seconds_total": report["runtime_seconds_total"]}, indent=1))
    print(f"wrote {dc.rel(json_path)} and {dc.rel(tsv_path)}")
    return 0


def _load_hold_at_ref(ref):
    import subprocess
    rel_path = os.path.relpath(dc.LEGACY_HOLD_PATH, dc.ROOT)
    try:
        txt = subprocess.run(["git", "show", f"{ref}:{rel_path}"], cwd=dc.ROOT, capture_output=True, text=True,
                             check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return json.loads(txt)


def run_surface(policy, args):
    """Surface gate. Strict by default; with --legacy-hold, the bounded Contract-C-RL migration rule."""
    import datetime
    ctx = dc.IGContext()
    pages = dc.load_html_pages(policy, args.surface)
    summary, verdicts, _ = analyse_universe("html_surface", pages, policy, ctx)
    print("=" * 72)
    print("Gate 12 — public surface check (BLOCKING)")
    if not args.legacy_hold:
        idx = [v for v in verdicts if v["public_indexable"]]
        bad = [v for v in idx if v["verdict"] != "PASS"]
        print(f"mode strict; surface {args.surface}: {len(pages)} pages, {len(idx)} indexable, {len(bad)} failing Gate 12")
        for v in bad[:args.show]:
            _print_verdict(v, verbose=False)
            for f in v["failures"][:4]:
                print(f"    FAIL {f}")
        if len(bad) > args.show:
            print(f"... {len(bad) - args.show} more")
        if args.json:
            _write_json(args.json, {"mode": "strict", "summary": summary, "failing": [v["page"] for v in bad]})
        if bad:
            print(f"GATE 12 FAIL: {len(bad)} indexable page(s) fail distinctiveness; publication/indexation prohibited.")
            return 1
        print("GATE 12 PASS: no indexable page fails distinctiveness.")
        return 0

    hold = dc.load_json(args.legacy_hold)
    errs = dc.verify_hold(hold)
    ratchet = None
    if args.hold_ratchet_ref:
        old = _load_hold_at_ref(args.hold_ratchet_ref)
        if old is None:
            ratchet = {"note": f"no legacy hold at {args.hold_ratchet_ref} (baseline introduced by this change)"}
        else:
            r_errs, ratchet = dc.hold_ratchet(hold, old)
            errs += r_errs
    today = datetime.date.fromisoformat(args.today) if args.today else datetime.date.today()
    states, meta = dc.apply_legacy_hold(pages, verdicts, args.surface, hold, policy, today)
    counts = Counter(s["state"] for s in states)
    blocking = [s for s in states if s["state"].startswith("BLOCK")]
    print(f"mode legacy-hold ({dc.rel(args.legacy_hold)}, {hold.get('entry_count')} sealed entries); "
          f"surface {args.surface}: {len(pages)} pages")
    for k in ("PASS", "LEGACY_HOLD_NOINDEX", "LEGACY_FREEZE_INDEXED", "BLOCK_LEGACY_INDEXED",
              "BLOCK_MODIFIED_LEGACY", "BLOCK_NEW_FAILING"):
        print(f"  {k:24s} {counts.get(k, 0)}")
    print(f"  {meta['freeze_exception']}")
    if counts.get("LEGACY_FREEZE_INDEXED"):
        print(f"  CONTRACT C DEVIATION (reported): {counts['LEGACY_FREEZE_INDEXED']} legacy page(s) remain indexable under the freeze exception")
    if meta["stale_baseline_entries"]:
        print(f"  {len(meta['stale_baseline_entries'])} stale baseline entr(y/ies) (page gone or now passing): remove them (ratchet)")
    if ratchet:
        print(f"  ratchet: {ratchet}")
    for e in errs:
        print(f"  HOLD INVALID: {e}")
    shown = 0
    for s in blocking:
        if shown >= args.show:
            break
        print(f"  [{s['state']}] {s['path']} (robots_index={s['robots_index']}, in_sitemap={s['in_sitemap']})")
        shown += 1
    if len(blocking) > shown:
        print(f"  ... {len(blocking) - shown} more")
    if args.json:
        _write_json(args.json, {"mode": "legacy_hold", "counts": dict(counts), "meta": meta, "hold_errors": errs,
                                "ratchet": ratchet, "blocking": blocking[:2000]})
    if errs or blocking:
        print(f"GATE 12 FAIL: {len(blocking)} blocking page(s){' + invalid hold' if errs else ''}.")
        return 1
    print("GATE 12 PASS (legacy-hold mode): no new, modified or indexation-requesting failing page.")
    return 0


def run_check_hold(policy, args):
    """PR-time check of the sealed legacy hold: integrity, default-closed freeze exception, shrink-only ratchet."""
    import datetime
    hold = dc.load_json(dc.LEGACY_HOLD_PATH)
    errs = dc.verify_hold(hold)
    today = datetime.date.fromisoformat(args.today) if args.today else datetime.date.today()
    active, reason = dc.freeze_exception_status(hold, policy, today)
    ratchet = None
    if args.hold_ratchet_ref:
        old = _load_hold_at_ref(args.hold_ratchet_ref)
        if old is None:
            ratchet = {"note": f"no legacy hold at {args.hold_ratchet_ref} (baseline introduced by this change)"}
        else:
            r_errs, ratchet = dc.hold_ratchet(hold, old)
            errs += r_errs
    print(f"legacy hold {dc.rel(dc.LEGACY_HOLD_PATH)}: {hold.get('entry_count')} sealed entries, sealed from "
          f"{hold.get('sealed_from')}; {reason}; ratchet: {ratchet or 'not checked'}")
    for e in errs:
        print(f"  HOLD INVALID: {e}")
    return 1 if errs else 0


def run_build_hold(policy, args):
    """Seal the legacy baseline from the CURRENT surface: every page that fails Gate 12 today.
    Writes main/data/distinctiveness/legacy_surface_hold.json with the freeze exception NOT authorized."""
    import subprocess
    ctx = dc.IGContext()
    root = os.path.join(dc.ROOT, policy["scope"]["html_surface_root"])
    pages = dc.load_html_pages(policy, root)
    _, verdicts, _ = analyse_universe("html_surface", pages, policy, ctx)
    rfp = _route_for_path()
    sitemap = dc.sitemap_paths(root)
    entries = []
    for p, v in zip(pages, verdicts):
        path = dc.surface_url_path(p, root)
        canon = re.sub(r"^https?://[^/]+", "", p.canonical) if p.canonical else None
        entries.append({"p": path, "h": dc.body_hash_hex(p), "r": rfp.get(path), "g": v["verdict"],
                        "robots": p.robots, "sm": path in sitemap, "c": canon})
    entries.sort(key=lambda e: e["p"])
    # The surface's own provenance: the last commit that changed site/public (not HEAD).
    commit = subprocess.run(["git", "log", "-1", "--format=%h", "--abbrev=10", "--",
                             policy["scope"]["html_surface_root"]], cwd=dc.ROOT, capture_output=True,
                            text=True).stdout.strip()
    hold = {
        "hold_id": "GATE12-LEGACY-SURFACE-HOLD", "version": "1.0.0", "policy_version": policy["version"],
        "sealed_from": {"surface": policy["scope"]["html_surface_root"], "commit": commit},
        "contract_c_basis": "RL legacy_public_holding -> (public_noindex, noindex); IP-16.2 pre-ratification public routes only",
        "meaning": "Every page publicly deployed before Gate 12, with its substantive-body hash and the directives it was "
                   "SERVED with (robots, sitemap membership, canonical). It is the status-quo record for the publication-"
                   "authority resolver: a legacy page may keep at most these directives (never escalate) while its body is "
                   "unchanged. Entries with g != PASS are the Gate-12 legacy hold. The list may only shrink.",
        "entry_fields": {"p": "URL path", "h": "Gate-12 substantive body hash (entity-masked)",
                         "r": "route_id or null (non-route legacy surface)", "g": "Gate-12 verdict at sealing",
                         "robots": "robots meta as served", "sm": "listed in a sitemap as served",
                         "c": "rel=canonical path as served"},
        "freeze_exception": {"state": "not_authorized", "authorized_by": None, "authorized_on": None, "expires_on": None,
                             "reason": None, "max_days_policy": policy["legacy_migration"]["freeze_exception"]["max_days"]},
        "entry_count": len(entries), "entries_sha256": dc.hold_entries_digest(entries), "entries": entries,
    }
    head = {k: v for k, v in hold.items() if k != "entries"}
    with open(dc.LEGACY_HOLD_PATH, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(head, indent=1, ensure_ascii=False)[:-2] + ',\n "entries": [\n')
        fh.write(",\n".join(json.dumps(e, ensure_ascii=False, separators=(",", ":")) for e in entries))
        fh.write("\n ]\n}\n")
    print(f"sealed {len(entries)} legacy entries from {policy['scope']['html_surface_root']} @ {commit} -> {dc.rel(dc.LEGACY_HOLD_PATH)}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--gate", action="store_true", help="publication-candidate gate (default)")
    g.add_argument("--audit", action="store_true", help="whole-corpus audit; writes reports")
    g.add_argument("--surface", metavar="DIR", help="block if any indexable HTML page under DIR fails")
    g.add_argument("--page", metavar="PATH", help="evaluate one markdown page")
    g.add_argument("--build-legacy-hold", action="store_true", help="seal the legacy baseline from site/public")
    g.add_argument("--check-hold", action="store_true", help="verify the sealed legacy hold (integrity + ratchet)")
    ap.add_argument("--json", metavar="OUT", help="write machine-readable JSON")
    ap.add_argument("--no-html", action="store_true", help="audit: skip the site/public surface")
    ap.add_argument("--show", type=int, default=20, help="surface: failing pages to list")
    ap.add_argument("--legacy-hold", metavar="FILE", help="surface: apply the bounded Contract-C-RL legacy hold")
    ap.add_argument("--hold-ratchet-ref", metavar="REF", help="surface: the hold may only shrink relative to REF")
    ap.add_argument("--today", metavar="YYYY-MM-DD", help="surface: evaluation date for the freeze exception")
    args = ap.parse_args(argv)
    policy = dc.load_policy()
    if args.audit:
        return run_audit(policy, args)
    if args.surface:
        return run_surface(policy, args)
    if args.page:
        return run_page(policy, args)
    if args.build_legacy_hold:
        return run_build_hold(policy, args)
    if args.check_hold:
        return run_check_hold(policy, args)
    return run_gate(policy, args)


if __name__ == "__main__":
    raise SystemExit(main())
