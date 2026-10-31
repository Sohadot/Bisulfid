#!/usr/bin/env python3
"""documentary_verification.py — evidence-based verification for low-risk references (policy
main/data/release/documentary_verification_policy.json).

evaluate(ko_id) runs the documentary checks D1–D7 against the governed stores and returns a record whose
verification_level is 'documentary_verified' only if every check passes. It reuses completed work
(renderer admission, source-lock checklist L1–L5, Gate 12) instead of repeating it, and it never records
or implies independent human review: 'independently_human_reviewed' reflects only a signed review record.

  documentary_verification.py --write | --check     main/data/release/documentary_verification/<KO>.json
"""

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(ROOT, "main", "data")
OUT_DIR = os.path.join(DATA, "release", "documentary_verification")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts", "reference_production"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "validators"))

# Signals of higher-risk content in rendered statements (fail-closed if any appears).
RISK_PATTERNS = re.compile(
    r"\b(toxic\w*|LD50|lethal|exposure (limit|level)s?|dos(e|es|age)|handl(e|ing) (it|them|the|with)|protective equipment|"
    r"PPE|first aid|antidote|treatment|diagnos\w+|therap\w+|complian(ce|t)|permissible|occupational|operating procedure|"
    r"step \d|guarantee\w*|performance|efficien(cy|t)|yield|price|market share|return on investment|ROI)\b", re.I)
REQUIRED_EXCLUSIONS = ("chemical_safety", "medical")
# A sentence that only DECLARES a topic out of scope is not advice ("Toxicity ... are outside this reference")...
EXCLUSION_STATEMENT = re.compile(r"\b(outside (the scope of )?this reference|not covered (here|by this reference)|"
                                 r"(this|the) reference (does not|gives no|provides no)|not established here|are excluded)\b", re.I)
# ...unless it also instructs or quantifies (then the exemption is void: fail-closed).
INSTRUCTION_OR_QUANTITY = re.compile(r"\b(wear|avoid|apply|mix|heat|store|dilute|keep|pour|inhale|ingest|"
                                     r"do not (exceed|use|mix|inhale|ingest))\b|\d+(\.\d+)?\s?(mg|g|kg|ml|l|ppm|ppb|%|°C|mol)\b", re.I)
# Operational guidance needs no risk keyword: an imperative at the start of a sentence or clause, or a
# dosage/concentration/temperature quantity, is itself a higher-risk signal (never exempted).
OPERATIONAL = re.compile(r"(^|[.;:]\s*)(store|keep|avoid|wear|mix|heat|dilute|pour|apply|add|use|handle|do not|never)\b|"
                         r"\b\d+(\.\d+)?\s?(mg|g|kg|ml|mL|l|L|ppm|ppb|%|°C|mol/L)(?![A-Za-z])", re.I)
# JSON-LD keys that carry identifiers or metadata, not assertions.
LD_METADATA_KEYS = ("@context", "@type", "url", "sameAs", "inLanguage", "@id")
_GATE12_CACHE = {}


def load(*p):
    with open(os.path.join(*p), encoding="utf-8") as fh:
        return json.load(fh)


def policy():
    return load(DATA, "release", "documentary_verification_policy.json")


def policy_adopted(pol=None):
    import release_checks as rc
    p = pol or policy()
    return p.get("status") == "adopted" and bool(p.get("adopted_on")) and not rc._is_agent(p.get("adopted_by"), rc.policy())


def _claims():
    out = {}
    for f in glob.glob(os.path.join(DATA, "claims", "*.json")) + glob.glob(os.path.join(DATA, "pilots", "*claims.json")):
        for c in load(f).get("claims") or []:
            if isinstance(c, dict) and c.get("claim_id"):
                out[c["claim_id"]] = c
    return out


def _spec_for(ko_id):
    for f in glob.glob(os.path.join(DATA, "reference_production", "render_specs", "KO-*.json")):
        s = load(f)
        if s.get("knowledge_object_id") == ko_id:
            return s
    return None


def _pc_for(ko_id):
    for f in glob.glob(os.path.join(DATA, "publication_candidates", "*.json")):
        pc = load(f)
        if pc.get("knowledge_object_id") == ko_id:
            return pc
    return None


def reference_fields(r):
    """Every author-controlled, publicly rendered text field of the reference, taken from the renderer's
    content model (not scraped from HTML), as (field, text). Navigation, identifiers, URLs and citation
    metadata (evidence trail, breadcrumbs, source titles) are deliberately not assessed as statements."""
    s, seo = r["spec"], (r.get("seo") or {})
    out = [("title", s.get("title")), ("h1", s.get("h1")), ("summary", s.get("summary")),
           ("seo.title", seo.get("title")), ("seo.description", seo.get("description"))]

    def ld(v, path):
        if isinstance(v, dict):
            for k, x in v.items():
                if k not in LD_METADATA_KEYS:
                    ld(x, f"{path}.{k}")
        elif isinstance(v, list):
            for i, x in enumerate(v):
                ld(x, f"{path}[{i}]")
        elif isinstance(v, str):
            out.append((path, v))
    ld(seo.get("json_ld") or {}, "json_ld")
    for x in seo.get("related", []):
        out += [("related.label", x.get("label")), ("related.relation", x.get("relation"))]
    for m in r["modules"]:
        out.append((f"module.{m['module_id']}.heading", m["heading"]))
        out += [(f"module.{m['module_id']}.paragraph", p["text"]) for p in m["paragraphs"]]
        if m.get("table"):
            out += [(f"module.{m['module_id']}.table.column", c) for c in m["table"]["columns"]]
            out += [(f"module.{m['module_id']}.table.cell", c) for row in m["table"]["rows"] for c in row]
    for g in r["glance"]:
        out += [("glance.label", g["label"]), ("glance.value", g["value"])]
    syn = r.get("synthesis")
    if syn:
        out += [("synthesis.heading", syn["heading"]), ("synthesis.intro", syn.get("intro"))]
        for g in syn["groups"]:
            out.append((f"synthesis.{g['verdict']}.label", g["label"]))
            out += [(f"synthesis.{g['verdict']}.item", i["text"]) for i in g["items"]]
    ne = s.get("not_established") or {}
    out += [("not_established.heading", ne.get("heading")),
            ("not_established.text", (ne.get("text") or "").replace(" [SOURCE REQUIRED]", ""))]
    return out


REQUIRED_FIELDS = ("title", "h1", "summary", "seo.title", "seo.description", "not_established.text")


def risk_hits(field, text):
    """Higher-risk signals in one field, sentence by sentence. Operational guidance (imperatives, dosage-type
    quantities) always counts. A risk keyword in a sentence that only declares a topic out of scope is exempt
    unless that sentence also instructs or quantifies. Keyword signals cannot establish safety or technical
    correctness; they only route content away from the low-risk pathway (fail-closed)."""
    hits = []
    for sent in re.split(r"(?<=[.;!?])\s+", text or ""):
        hits += [f"{field}: operational '{m.group(0).strip(' .;:')}'" for m in OPERATIONAL.finditer(sent)]
        found = [m.group(0) for m in RISK_PATTERNS.finditer(sent)]
        if not found:
            continue
        if EXCLUSION_STATEMENT.search(sent) and not INSTRUCTION_OR_QUANTITY.search(sent):
            continue
        hits += [f"{field}: {f}" for f in found]
    return hits


def classify_risk(ko, pc, claims, fields, pol):
    """low_risk_informational only if declared, every claim type is eligible, the KO excludes safety and
    medical claims, and no rendered statement carries a higher-risk signal. Otherwise undetermined/higher_risk."""
    reasons = []
    decl = (pc or {}).get("risk_classification") or {}
    if decl.get("class") != "low_risk_informational" or not decl.get("rationale"):
        reasons.append("no low_risk_informational declaration with rationale in the publication candidate")
    bad_types = [c for c in ko["claim_ids"] if (claims.get(c) or {}).get("claim_type") not in pol["eligible_claim_types"]]
    if bad_types:
        reasons.append(f"claim type not eligible or missing: {bad_types}")
    missing = [x for x in REQUIRED_EXCLUSIONS if x not in (ko.get("excluded_claim_classes") or [])]
    if missing:
        reasons.append(f"KO does not exclude {missing}")
    present = {f for f, t in fields if (t or "").strip()}
    absent = [f for f in REQUIRED_FIELDS if f not in present]
    if not fields or absent:
        reasons.append(f"reference content missing or unreadable: {absent or 'no fields'}")
    claim_fields = [(f"claim.{c}", (claims.get(c) or {}).get("statement", "")) for c in ko["claim_ids"]]
    hits = sorted({h for f, t in fields + claim_fields for h in risk_hits(f, t)})
    if hits:
        return "higher_risk", reasons + [f"higher-risk signal(s): {hits}"]
    return ("low_risk_informational", []) if not reasons else ("undetermined", reasons)


def evaluate(ko_id, overrides=None):
    """overrides (tests only): dict of replacements for 'ko', 'pc', 'claims', 'spec', 'lock_checklist'."""
    import release_checks as rc
    import render_ko_reference as rk
    ov = overrides or {}
    pol = policy()
    ko = ov.get("ko") or rc._ko(ko_id)
    pc = ov.get("pc", _pc_for(ko_id))
    claims = ov.get("claims") or _claims()
    spec = ov.get("spec") or _spec_for(ko_id)
    checks = {}
    if not ko or not spec:
        return {"knowledge_object_id": ko_id, "verification_level": "not_verified", "failures": ["no KO or render spec"]}
    # D2/D3 via the renderer: admission per declared use, membership, consistency (raises on any failure)
    try:
        r = rk.build(spec)
        bound = {e for b in ko["claim_bindings"] for e in b["evidence_ids"]}
        rendered = {p["evidence_id"] for p in r["provenance"]}
        d2 = [f"bound evidence {e} is not rendered/admitted" for e in sorted(bound - rendered)]
        d3 = [f"{p['evidence_id']}: use {p['intended_use']} not qualified" for p in r["provenance"] if not p.get("qualification_id")]
        statements = reference_fields(r)
    except Exception as exc:  # noqa: BLE001 — any refusal is a failed check
        r, d2, d3, statements = None, [f"renderer refused: {exc}"], [], []
    checks["D2_evidence"], checks["D3_scope"] = d2, d3
    # D1 claims
    d1 = []
    for cid in ko["claim_ids"]:
        c = claims.get(cid)
        b = next((x for x in ko["claim_bindings"] if x["claim_id"] == cid), None)
        if not c:
            d1.append(f"{cid}: does not exist")
            continue
        if c.get("status") not in ("approved", "approved_narrow"):
            d1.append(f"{cid}: status {c.get('status')}")
        if not b or not b.get("evidence_ids"):
            d1.append(f"{cid}: no bound evidence")
        sup = set(c.get("supporting_evidence_ids") or [])
        if not sup or not sup <= set((b or {}).get("evidence_ids", [])):
            d1.append(f"{cid}: supporting evidence not bound by the KO")
    checks["D1_claims"] = d1
    # D4 reproducibility: L1–L5 for every source
    d4 = []
    lc = ov.get("lock_checklist") or rc.lock_checklist
    for sid in rc.ko_sources(ko_id):
        evs = [e for e in ko["evidence_ids"] if load(DATA, "evidence", e + ".json")["source_id"] == sid]
        cl = lc(sid, evs)["checklist"]
        bad = [k for k in ("L1", "L2", "L3", "L4", "L5") if not str(cl[k]).startswith("pass")]
        if bad:
            d4.append(f"{sid}: {', '.join(bad)} not pass")
    checks["D4_reproducible"] = d4
    # D5 conflicts and transparency
    d5 = []
    for eid in ko["evidence_ids"] + ko.get("boundary_evidence_ids", []):
        e = load(DATA, "evidence", eid + ".json")
        if e.get("contradiction_status") == "unresolved" or e.get("conflicts_with"):
            d5.append(f"{eid}: unresolved contradiction")
    for cid in ko["claim_ids"]:
        if (claims.get(cid) or {}).get("contradiction_status") == "unresolved":
            d5.append(f"{cid}: unresolved contradiction")
    if ko.get("unresolved_fields"):
        groups = {g["verdict"] for g in ((r or {}).get("synthesis") or {}).get("groups", [])}
        if "open" not in groups or not spec.get("not_established", {}).get("text"):
            d5.append("unresolved fields exist but the reference does not state them (open group + not-established)")
    checks["D5_conflicts"] = d5
    # D6 quality: Gate 12 on the canonical draft + distinctiveness review
    d6 = []
    try:
        import distinctiveness_core as dc
        route = r["route"] if r else None
        md = os.path.join(ROOT, route["content_file"]) if route else None
        md_text = open(md, encoding="utf-8").read()
        if md_text not in _GATE12_CACHE:  # the verdict depends only on the draft and the corpus on disk
            pol12 = dc.load_policy()
            page = dc.parse_markdown(md, md_text, pol12)
            u = dc.Universe(dc.load_markdown_pages(pol12), pol12)
            ctx = dc.IGContext()
            _GATE12_CACHE[md_text] = dc.gate12_verdict(page, u, pol12, ctx, unit_index=dc.unit_statement_index(ctx, pol12, u.by_id))
        v = _GATE12_CACHE[md_text]
        if v["verdict"] != "PASS":
            d6.append(f"Gate 12 {v['verdict']}: {v['failures']}")
        ig_valid = v["information_gain"]["valid_units"]
    except Exception as exc:  # noqa: BLE001
        d6.append(f"Gate 12 not evaluable: {exc}")
        ig_valid = 0
    if not (pc or {}).get("distinctiveness_review"):
        d6.append("no distinctiveness review recorded in the publication candidate")
    checks["D6_quality"] = d6
    # D7 risk
    risk, why = classify_risk(ko, pc, claims, statements, pol)
    checks["D7_risk"] = [] if risk == "low_risk_informational" else [f"risk class {risk}"] + why
    failures = [f"{k}: {m}" for k, v in checks.items() for m in v]
    human, _ = rc.validation_ok(ko_id)
    src_bad = {m.split(":")[0] for m in checks["D4_reproducible"]}
    outcomes = []
    for b in ko["claim_bindings"]:
        cid = b["claim_id"]
        srcs = sorted({load(DATA, "evidence", e + ".json")["source_id"] for e in b["evidence_ids"]})
        own = [m for m in checks["D1_claims"] if m.startswith(cid)] + [m for m in checks["D2_evidence"] if any(e in m for e in b["evidence_ids"])] \
            + [f"source {x} not reproducible" for x in srcs if x in src_bad]
        outcomes.append({"claim_id": cid, "evidence_ids": b["evidence_ids"], "sources": srcs,
                         "outcome": "documentary_verified" if not own and risk == "low_risk_informational" else "not_verified",
                         "reasons": own})
    return {"knowledge_object_id": ko_id, "policy": f"{pol['policy_id']}@{pol['version']}",
            "policy_status": pol["status"], "policy_adopted": policy_adopted(pol),
            "verification_level": "documentary_verified" if not failures else "not_verified",
            "independently_human_reviewed": bool(human),
            "label": ("documentary_verified: automated evidence checks; not independent peer review" if not failures
                      else "not_verified"),
            "risk_class": risk, "claims_assessed": len(ko["claim_ids"]),
            "sources_assessed": len(rc.ko_sources(ko_id)), "ig_valid_units": ig_valid,
            "checks": {k: ("pass" if not v else v) for k, v in checks.items()}, "failures": failures,
            "claim_outcomes": outcomes,
            "never_implied": ["independent human peer review", "L6 human signature", "owner claim activation",
                              "owner release authorization", "AMD-IG-R03-001 ratification"]}


def documentary_ok(ko_id):
    """For release_checks: (ok, reasons). Only an ADOPTED policy can let documentary verification stand in
    for a signed review or L6 signatures; the evaluation is recomputed live (never trusted from a file)."""
    if not policy_adopted():
        return False, ["documentary verification policy not adopted by the owner"]
    rec = evaluate(ko_id)
    if rec["verification_level"] != "documentary_verified" or rec["risk_class"] != "low_risk_informational":
        return False, rec["failures"] or [f"risk class {rec['risk_class']}"]
    return True, []


def main(argv=None):
    mode = (argv or sys.argv[1:] or ["--check"])[0]
    stale = []
    for f in sorted(glob.glob(os.path.join(DATA, "reference_production", "render_specs", "KO-*.json"))):
        kid = load(f)["knowledge_object_id"]
        text = json.dumps(evaluate(kid), indent=1, ensure_ascii=False) + "\n"
        p = os.path.join(OUT_DIR, kid + ".json")
        cur = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        if cur != text:
            stale.append(os.path.relpath(p, ROOT))
            if mode == "--write":
                os.makedirs(OUT_DIR, exist_ok=True)
                open(p, "w", encoding="utf-8").write(text)
        print(f"{kid}: {json.loads(text)['verification_level']} ({json.loads(text)['risk_class']})")
    if stale:
        print(("wrote: " if mode == "--write" else "STALE: ") + ", ".join(stale))
    return 1 if (stale and mode == "--check") else 0


if __name__ == "__main__":
    sys.exit(main())
