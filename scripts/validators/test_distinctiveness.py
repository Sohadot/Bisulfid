#!/usr/bin/env python3
"""test_distinctiveness.py — proofs for Gate 12 (Page Distinctiveness & Information Gain).

Run: python3 scripts/validators/test_distinctiveness.py   (stdlib unittest; exit 0 = all pass)
"""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import distinctiveness_core as dc  # noqa: E402

POLICY = dc.load_policy()
RULES = dc._Rules(POLICY)
# The reconstructed canonical MoS2 draft (Reference Production preview of route molybdenum_disulfide).
CONTROL_PATH = os.path.join(dc.ROOT, "main", "content", "en", "pages", "molybdenum-disulfide.md")
CONTROL_ID = dc.rel(CONTROL_PATH)
with open(CONTROL_PATH, encoding="utf-8") as _fh:
    CONTROL_TEXT = _fh.read()
REAL_REGISTRY = dc.load_json(dc.IG_REGISTRY_PATH)
CONTROL_ENTRY = next(e for e in REAL_REGISTRY["pages"] if e["page"] == CONTROL_ID)

# Shared site infrastructure that every generated page carries.
INFRA = """
**Draft status:** This page is a **non-public** pipeline draft. It is **not published**, **not indexable**, **not in the sitemap**, **not in navigation**, and **not publication-ready**. **No claim is approved** for publication from this draft alone.

## Reliability notice

| Field | Value |
| --- | --- |
| knowledge_reliability_level | L2_draft_cautious |
| source_posture | source_required_unresolved |

## Source and claim status

- Source posture: **source_required_unresolved** — factual terminology not asserted as verified in this draft.
- Claim posture: **claim_pending_review** — no approved publication claim from this page alone.
- Source registries: **inactive** for mass publication; individual sources may exist elsewhere.

## Publication blockers

- Route remains `planned`; `indexable: false`; `in_sitemap: false`; `in_navigation: false`.
- `production_can_safely_proceed: no`.

## Internal link placeholders (planning only)

- `route_id`: `en_foundation_sovereign_intro` (planning placeholder — not a live link)

*Non-public pipeline draft — engine v1.*
"""

TEMPLATE_BODY = """## Page purpose

- Compound and entity naming record for {slug} within the governed reference layer of the atlas.
- Naming and identity boundary for {name}, not industrial performance claims or handling advice.
- Academic reference that frames {name} for chemists without asserting unsupported chemical facts.
- Operational handling, procurement and market language about {name} is excluded from this record.

## Terminology layers

- Lexical form of {name}: surface spelling, document language and cross-language boundary questions remain under review.
- Chemical and document form: intended scope of {name} and its boundary to neighbouring terms remain under review.
- Reference layer: nomenclature and boundary oriented, with no operating, procurement, market or safety guidance.
"""


def md(name, body, route=None, extra_front=""):
    slug = name.lower().replace(" ", "_")
    route = route or f"test_{slug}"
    return (f"---\nroute_id: {route}\nstatus: draft\npublication_status: non_public\nindexable: false\n"
            f"language: en\ntitle: {name} — Compound Reference | bisulfid.com\npage_type_id: PT_COMPOUND_ENTITY\n"
            f"{extra_front}---\n# {name} — Compound Reference\n" + INFRA.split("## Reliability notice")[0]
            + body.format(name=name, slug=slug) + "\n## Reliability notice" + INFRA.split("## Reliability notice")[1])


def page(pid, text):
    return dc.parse_markdown(pid, text, POLICY, RULES, page_id=pid)


ENTITIES = ["Actinium Sulfide", "Aluminium Sulfide", "Calcium Sulfide", "Cadmium Sulfide", "Zinc Sulfide"]


def template_universe(extra=()):
    pages = [page(f"t/{e.lower().replace(' ', '-')}.md", md(e, TEMPLATE_BODY)) for e in ENTITIES]
    return dc.Universe(pages + list(extra), POLICY), pages


class IGRegistry:
    """Temporary IG registry for a test (never touches the governed file)."""

    def __init__(self, pages):
        self.tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        json.dump({"pages": pages}, self.tmp)
        self.tmp.close()
        self.ctx = dc.IGContext(self.tmp.name)

    def close(self):
        os.unlink(self.tmp.name)


def control_entry(units=None, page_id=CONTROL_ID, **kw):
    e = json.loads(json.dumps(CONTROL_ENTRY))
    e["page"] = page_id
    if units is not None:
        e["units"] = units
    e.update(kw)
    return e


ALL_GREEN = {"governance": "governed", "evidence": "evidence_locked", "claim": "claim_approved",
             "validation": "validated", "ig": "ig_passed", "release": "authorized"}


class Gate12Tests(unittest.TestCase):

    def setUp(self):
        self.empty = IGRegistry([])

    def tearDown(self):
        self.empty.close()

    def verdict(self, p, universe, ctx=None):
        ctx = ctx or self.empty.ctx
        return dc.gate12_verdict(p, universe, POLICY, ctx, unit_index=dc.unit_statement_index(ctx, POLICY, universe.by_id))

    # 1
    def test_01_exact_duplicate_fails(self):
        a = page("x/a.md", md("Actinium Sulfide", TEMPLATE_BODY))
        b = page("x/b.md", md("Actinium Sulfide", TEMPLATE_BODY))
        u = dc.Universe([a, b], POLICY)
        v = self.verdict(a, u)
        self.assertEqual(v["text"]["similarity"], 1.0)
        self.assertEqual(v["text"]["status"], "FAIL")
        self.assertEqual(v["verdict"], "FAIL")
        self.assertTrue(any(f.startswith("near_duplicate") for f in v["failures"]))

    # 2
    def test_02_entity_substitution_clone_fails(self):
        u, pages = template_universe()
        v = self.verdict(pages[0], u)
        self.assertEqual(v["text"]["similarity"], 1.0, "entity-masked bodies must compare identical")
        self.assertTrue(v["entity_substitution_detected"])
        raw = dc.similarity(pages[0].raw_shingle_set, pages[1].raw_shingle_set, 20)[0]
        self.assertLess(raw, 1.0, "raw text differs only by the entity name")
        self.assertEqual(v["verdict"], "FAIL")

    # 3
    def test_03_synonym_paraphrase_light_clone_fails(self):
        u0, pages = template_universe()
        light = (TEMPLATE_BODY.replace("governed", "controlled").replace("unsupported", "unverified")
                 .replace("excluded", "omitted").replace("neighbouring", "adjacent"))
        p = page("x/paraphrase.md", md("Barium Sulfide", light))
        u = dc.Universe(pages + [p], POLICY)
        v = self.verdict(p, u)
        self.assertIn(v["text"]["status"], ("FAIL", "REVIEW"))
        self.assertTrue(v["structure"]["structural_template"], v["structure"])
        self.assertEqual(v["verdict"], "FAIL")

    # 4
    def test_04_identical_section_skeleton_detected(self):
        u, pages = template_universe()
        v = self.verdict(pages[2], u)
        self.assertEqual(v["structure"]["skeleton"], ["page purpose", "terminology layers"])
        self.assertGreaterEqual(v["structure"]["shared_with_pages"], 4)
        self.assertTrue(v["structure"]["structural_template"])
        self.assertTrue(any(f.startswith("structural_template") for f in v["failures"]))

    def test_04b_shared_structure_alone_is_permitted(self):
        # Same headings, genuinely different prose: skeleton is shared but not a template failure.
        a = page("x/sa.md", md("Zinc Sulfide", "## Page purpose\n\nSphalerite and wurtzite are the two zinc sulfide "
                 "structures discussed by mineralogists, and the cubic form dominates natural ore deposits worldwide.\n\n"
                 "## Terminology layers\n\nThe mineral names differ from the systematic chemical name used in "
                 "inorganic nomenclature and in customs schedules of several jurisdictions.\n"))
        b = page("x/sb.md", md("Lead Sulfide", "## Page purpose\n\nGalena is the principal ore of lead and was "
                 "historically used as a crystal detector in early radio receivers built by amateurs.\n\n"
                 "## Terminology layers\n\nPlumbic and plumbous naming survives in older trade literature while "
                 "modern texts prefer oxidation-state notation for the sulfide.\n"))
        u = dc.Universe([a, b], POLICY)
        v = self.verdict(a, u)
        self.assertEqual(v["structure"]["shared_with_pages"], 1)
        self.assertFalse(v["structure"]["structural_template"])
        self.assertLess(v["text"]["similarity"], 0.55)

    # 5
    def test_05_shared_navigation_and_disclaimer_do_not_trigger(self):
        a = page("x/na.md", md("Zinc Sulfide", "## Mineral forms\n\nSphalerite and wurtzite are the two zinc sulfide "
                 "structures discussed by mineralogists, and the cubic form dominates natural ore deposits worldwide.\n"))
        b = page("x/nb.md", md("Lead Sulfide", "## Ore history\n\nGalena is the principal ore of lead and was "
                 "historically used as a crystal detector in early radio receivers built by amateurs.\n"))
        self.assertGreater(a.infra_tokens, 80)
        self.assertGreater(b.infra_tokens, 80)
        u = dc.Universe([a, b], POLICY)
        v = self.verdict(a, u)
        self.assertLess(v["text"]["similarity"], 0.10, v["text"])
        whole = dc.similarity(dc.shingles(dc.tokens(dc.normalize_text(md("Zinc Sulfide", ""))), 5),
                              dc.shingles(dc.tokens(dc.normalize_text(md("Lead Sulfide", ""))), 5), 20)[0]
        self.assertGreater(whole, 0.70, "the infrastructure itself is near-identical, yet it is excluded")

    # 6
    def test_06_genuinely_different_evidence_backed_page_passes(self):
        reg = IGRegistry([control_entry()])
        try:
            u, _ = template_universe()
            c = page(CONTROL_ID, CONTROL_TEXT)
            v = self.verdict(c, u, reg.ctx)
            self.assertEqual(v["verdict"], "PASS", v["failures"] + v["reviews"])
            self.assertEqual(v["information_gain"]["valid_units"], len(CONTROL_ENTRY["units"]))
            self.assertGreaterEqual(len(CONTROL_ENTRY["units"]), 3)
        finally:
            reg.close()

    # 7
    def test_07_low_similarity_alone_is_insufficient_without_ig(self):
        u, _ = template_universe()
        c = page(CONTROL_ID, CONTROL_TEXT)
        v = self.verdict(c, u)  # no IG units registered
        self.assertEqual(v["text"]["status"], "PASS_TEXT_ONLY")
        self.assertEqual(v["verdict"], "FAIL")
        self.assertTrue(any(f.startswith("information_gain") for f in v["failures"]))
        self.assertEqual(dc.combined_publication_eligibility(v, ALL_GREEN)["publication_state"], "not_public")

    # 8
    def test_08_similarity_at_or_above_0_70_blocks_publication(self):
        self.assertEqual(dc.classify_similarity(0.70, POLICY), "FAIL")
        self.assertEqual(dc.classify_similarity(0.9999, POLICY), "FAIL")
        reg = IGRegistry([control_entry()])
        try:
            c = page(CONTROL_ID, CONTROL_TEXT)
            twin = page("x/twin.md", CONTROL_TEXT.replace("## What this reference does not establish", "## Open questions"))
            u = dc.Universe([twin], POLICY)
            v = self.verdict(c, u, reg.ctx)
            self.assertGreaterEqual(v["text"]["similarity"], 0.70)
            self.assertEqual(v["verdict"], "FAIL")
            elig = dc.combined_publication_eligibility(v, ALL_GREEN)
            self.assertEqual((elig["publication_state"], elig["indexation_state"]), ("not_public", "noindex"))
            self.assertFalse(elig["eligible"])
        finally:
            reg.close()

    # 9
    def test_09_review_band_requires_review(self):
        self.assertEqual(dc.classify_similarity(0.55, POLICY), "REVIEW")
        self.assertEqual(dc.classify_similarity(0.6999, POLICY), "REVIEW")
        self.assertEqual(dc.classify_similarity(0.5499, POLICY), "PASS_TEXT_ONLY")
        reg = IGRegistry([control_entry()])
        try:
            c = page(CONTROL_ID, CONTROL_TEXT)
            shared = ("The formula states composition only: one molybdenum to two sulfur. It says nothing about how "
                      "the atoms are arranged in the solid, and the database field name \"MolecularFormula\" should not "
                      "be read as implying that MoS2 forms discrete molecules. This description belongs to the bulk "
                      "crystal. Single layers and few-layer flakes are separate forms whose properties this reference "
                      "does not cover. The values agree within the stated uncertainty of the 1923 value and are kept "
                      "as separate determinations rather than averaged into one number.")
            filler_words = ("ore flotation circuits recover concentrate from crushed rock before roasting converts "
                            "sulfide minerals into oxides for smelting in rotary kilns at remote mining sites").split()
            hit = None
            for n in range(5, 400, 3):
                filler = " ".join(filler_words[i % len(filler_words)] + str(i // len(filler_words)) for i in range(n))
                nb = page("x/neighbour.md", md("Neighbour Topic", "## Notes\n\n" + shared + "\n\n" + filler + "\n"))
                s = dc.similarity(c.shingle_set, nb.shingle_set, 20)[0]
                if 0.55 <= s < 0.70:
                    hit = nb
                    break
            self.assertIsNotNone(hit, "could not construct a review-band neighbour")
            u = dc.Universe([hit], POLICY)
            v = self.verdict(c, u, reg.ctx)
            self.assertEqual(v["text"]["status"], "REVIEW")
            self.assertEqual(v["verdict"], "REVIEW", v["failures"])
            self.assertFalse(dc.combined_publication_eligibility(v, ALL_GREEN)["eligible"])
        finally:
            reg.close()

    # 10
    def test_10_three_valid_page_specific_units_satisfy_minimum(self):
        reg = IGRegistry([control_entry(units=CONTROL_ENTRY["units"][:3])])
        try:
            u, _ = template_universe()
            v = self.verdict(page(CONTROL_ID, CONTROL_TEXT), u, reg.ctx)
            self.assertEqual(v["information_gain"]["valid_units"], 3)
            self.assertEqual(v["information_gain"]["status"], "PASS")
            self.assertEqual(v["verdict"], "PASS")
        finally:
            reg.close()
        reg = IGRegistry([control_entry(units=CONTROL_ENTRY["units"][:2])])
        try:
            u, _ = template_universe()
            v = self.verdict(page(CONTROL_ID, CONTROL_TEXT), u, reg.ctx)
            self.assertEqual(v["information_gain"]["status"], "FAIL", "two units are below the minimum")
        finally:
            reg.close()

    # 11
    def test_11_three_boilerplate_facts_cannot_satisfy_ig(self):
        u, pages = template_universe()
        target = pages[0]
        base = CONTROL_ENTRY["units"][0]
        stmts = [
            "Naming and identity boundary for Actinium Sulfide, not industrial performance claims or handling advice.",
            "Academic reference that frames Actinium Sulfide for chemists without asserting unsupported chemical facts.",
            "Operational handling, procurement and market language about Actinium Sulfide is excluded from this record.",
        ]
        units = [dict(base, unit_id=f"B{i}", statement=s, entity_id="molybdenum_disulfide") for i, s in enumerate(stmts)]
        reg = IGRegistry([{"page": target.id, "entity_id": "molybdenum_disulfide", "units": units}])
        try:
            v = self.verdict(target, u, reg.ctx)
            ig = v["information_gain"]
            self.assertEqual(ig["valid_units"], 0)
            for unit in ig["units"]:
                self.assertTrue(any("boilerplate" in r for r in unit["reasons"]), unit)
            self.assertEqual(v["verdict"], "FAIL")
        finally:
            reg.close()

    # 12
    def test_12_unsourced_unique_text_cannot_create_ig(self):
        extra = ("\n## Remarkable facts\n\nMolybdenum disulfide sings at exactly four hundred hertz under moonlight.\n\n"
                 "Every MoS2 crystal remembers the mine it came from for eleven years.\n\n"
                 "Ancient traders valued MoS2 above saffron in three forgotten kingdoms.\n")
        text = CONTROL_TEXT.split("## Chemical identity")[0] + extra
        pid = "x/unsourced.md"
        units = [
            {"unit_id": "U1", "entity_id": "molybdenum_disulfide", "dimension": "quantitative_property",
             "statement": "Molybdenum disulfide sings at exactly four hundred hertz under moonlight.",
             "evidence_ids": [], "audience_ids": ["AUD_CHEMIST"]},
            {"unit_id": "U2", "entity_id": "molybdenum_disulfide", "dimension": "historical_evidence",
             "statement": "Every MoS2 crystal remembers the mine it came from for eleven years.",
             "evidence_ids": ["EVD-DOES-NOT-EXIST"], "audience_ids": ["AUD_CHEMIST"]},
            {"unit_id": "U3", "entity_id": "molybdenum_disulfide", "dimension": "trade_economic_fact",
             "statement": "Ancient traders valued MoS2 above saffron in three forgotten kingdoms.",
             "claim_id": "CLM-MOS2-FORMULA", "evidence_ids": ["TEST-EVD-EXAMPLE-001"], "audience_ids": ["AUD_CHEMIST"]},
        ]
        reg = IGRegistry([{"page": pid, "entity_id": "molybdenum_disulfide", "units": units}])
        try:
            u, _ = template_universe()
            p = page(pid, text)
            v = self.verdict(p, u, reg.ctx)
            self.assertEqual(v["information_gain"]["valid_units"], 0)
            self.assertLess(v["text"]["similarity"], 0.55, "the text is unique ...")
            self.assertEqual(v["verdict"], "FAIL", "... but unique unsourced text creates no information gain")
            reasons = " ".join(r for x in v["information_gain"]["units"] for r in x["reasons"])
            self.assertIn("unsourced", reasons)
        finally:
            reg.close()
        # Unregistered unique text: no units at all.
        v = self.verdict(page("x/unregistered.md", text), dc.Universe([], POLICY))
        self.assertEqual(v["information_gain"]["registered_units"], 0)
        self.assertEqual(v["verdict"], "FAIL")

    # 13
    def test_13_translation_cannot_fake_uniqueness(self):
        de_text = ("---\nroute_id: x_de_mos2\nstatus: draft\npublication_status: non_public\nlanguage: de\n"
                   "title: Molybdändisulfid (MoS2) — Wissenschaftliche Identität\n---\n# Molybdändisulfid (MoS2)\n\n"
                   "## Chemische Identität\n\nDie Formel von Molybdändisulfid ist MoS2, unabhängig erfasst in den "
                   "Datenbanken PubChem und NIST.\n\n## Schichtstruktur\n\nKompaktes MoS2 ist ein Schichtmaterial, "
                   "dessen Schichten jeweils aus drei Atomlagen S–Mo–S bestehen.\n\n## Polytyp 2H\n\nIm Polytyp 2H "
                   "kristallisiert kompaktes MoS2 in der hexagonalen Raumgruppe P6₃/mmc (Nr. 194) mit einer "
                   "c-Achse nahe 12,3 Å.\n")
        de_id = "x/de/mos2.md"
        de_units = [dict(u, statement=s) for u, s in zip(CONTROL_ENTRY["units"][:3], [
            "Die Formel von Molybdändisulfid ist MoS2, unabhängig erfasst in den Datenbanken PubChem und NIST.",
            "Kompaktes MoS2 ist ein Schichtmaterial, dessen Schichten jeweils aus drei Atomlagen S–Mo–S bestehen.",
            "Im Polytyp 2H kristallisiert kompaktes MoS2 in der hexagonalen Raumgruppe P6₃/mmc (Nr. 194) mit einer c-Achse nahe 12,3 Å."])]
        en = page(CONTROL_ID, CONTROL_TEXT)
        de = page(de_id, de_text)
        u = dc.Universe([en], POLICY)
        self.assertLess(dc.similarity(de.shingle_set, en.shingle_set, 20)[0], 0.10, "lexically disjoint across languages")
        # (a) declared localization -> LOCALIZATION (Gate 11), never an independent PASS.
        reg = IGRegistry([control_entry(), {"page": de_id, "entity_id": "molybdenum_disulfide",
                                            "localization_of": CONTROL_ID, "units": de_units}])
        try:
            v = self.verdict(de, u, reg.ctx)
            self.assertEqual(v["verdict"], "LOCALIZATION")
            self.assertTrue(v["gate12_blocks_publication"])
            self.assertFalse(dc.combined_publication_eligibility(v, ALL_GREEN)["eligible"])
        finally:
            reg.close()
        # (b) undeclared translation reusing the same governed knowledge -> cross-page duplicate -> FAIL.
        reg = IGRegistry([control_entry(), {"page": de_id, "entity_id": "molybdenum_disulfide", "units": de_units}])
        try:
            v = self.verdict(de, u, reg.ctx)
            self.assertEqual(v["information_gain"]["valid_units"], 0)
            self.assertTrue(all(any("cross-page duplicate" in r for r in x["reasons"]) for x in v["information_gain"]["units"]))
            self.assertEqual(v["verdict"], "FAIL")
        finally:
            reg.close()

    # 14
    def test_14_drafts_are_audited_but_not_published(self):
        u, pages = template_universe()
        verdicts = [self.verdict(p, u) for p in pages]
        self.assertEqual(len(verdicts), len(pages), "every draft is audited")
        self.assertTrue(all(v["is_draft"] and not v["publication_candidate"] for v in verdicts))
        cand = page("x/cand.md", md("Actinium Sulfide", TEMPLATE_BODY, extra_front="publication_eligibility: true\n"))
        self.assertTrue(cand.publication_candidate)
        self.assertFalse(pages[0].publication_candidate)
        # A draft that passes Gate 12 is still not public: Gate 12 never grants publication.
        reg = IGRegistry([control_entry()])
        try:
            c = page(CONTROL_ID, CONTROL_TEXT)
            v = self.verdict(c, u, reg.ctx)
            self.assertEqual(v["verdict"], "PASS")
            self.assertFalse(c.publication_candidate)
            self.assertFalse(dc.combined_publication_eligibility(v, None)["eligible"])
        finally:
            reg.close()

    def test_14b_real_control_is_not_a_publication_candidate(self):
        c = page(CONTROL_ID, CONTROL_TEXT)
        self.assertTrue(c.is_draft)
        self.assertFalse(c.publication_candidate)
        pc = dc.load_json(os.path.join(dc.DATA, "publication_candidates", "PC-MOS2-SCIENTIFIC-001.json"))
        ps = pc["postures"]
        inputs = {"governance": ps["governance_posture"], "evidence": ps["evidence_posture"], "claim": ps["claim_posture"],
                  "validation": ps["validation_posture"], "ig": ps["information_gain_posture"],
                  "release": ps["release_authorization"]}
        elig = dc.combined_publication_eligibility("PASS", inputs)
        self.assertEqual((elig["publication_state"], elig["indexation_state"]), ("not_public", "noindex"))

    # 15
    def test_15_contract_c_remains_authoritative(self):
        sys.path.insert(0, os.path.join(dc.ROOT, "scripts", "governance_scaffolding"))
        import contract_c_derive
        green = contract_c_derive.derive(**ALL_GREEN)
        self.assertNotEqual(green, ("not_public", "noindex"))
        # Gate 12 PASS + Contract C green -> exactly Contract C's output (Gate 12 adds nothing).
        self.assertEqual(tuple(dc.combined_publication_eligibility("PASS", ALL_GREEN)["contract_c"]), green)
        self.assertEqual((dc.combined_publication_eligibility("PASS", ALL_GREEN)["publication_state"],
                          dc.combined_publication_eligibility("PASS", ALL_GREEN)["indexation_state"]), green)
        # Gate 12 PASS cannot override a Contract-C denial.
        for k, bad in (("release", "not_authorized"), ("claim", "claim_pending"), ("validation", "not_validated"),
                       ("ig", "ig_failed"), ("governance", "reference_draft")):
            r = dc.combined_publication_eligibility("PASS", dict(ALL_GREEN, **{k: bad}))
            self.assertEqual(r["publication_state"], "not_public", k)
        # Contract C green cannot override a Gate-12 FAIL / REVIEW / LOCALIZATION.
        for verdict in ("FAIL", "REVIEW", "LOCALIZATION"):
            r = dc.combined_publication_eligibility(verdict, ALL_GREEN)
            self.assertEqual((r["publication_state"], r["indexation_state"]), ("not_public", "noindex"))
        # Unknown Contract-C inputs fail closed.
        self.assertFalse(dc.combined_publication_eligibility("PASS", None)["eligible"])

    # ---- no-gaming proofs (section 16)
    def test_16a_padding_does_not_dilute_similarity(self):
        u, pages = template_universe()
        pad = "\n## Introduction\n\n" + " ".join(f"generic{i} introductory{i} words{i}" for i in range(150)) + "\n"
        p = page("x/padded.md", md("Barium Sulfide", pad + TEMPLATE_BODY))
        v = self.verdict(p, dc.Universe(pages + [p], POLICY))
        self.assertLess(v["text"]["jaccard"], 0.70, "padding lowers Jaccard ...")
        self.assertGreaterEqual(v["text"]["similarity"], 0.70, "... but the overlap coefficient still blocks")
        self.assertEqual(v["verdict"], "FAIL")

    def test_16b_renamed_headings_and_reordered_sentences_still_fail(self):
        u, pages = template_universe()
        body = TEMPLATE_BODY.replace("## Page purpose", "## Overview").replace("## Terminology layers", "## Naming")
        lines = body.split("\n")
        p = page("x/renamed.md", md("Barium Sulfide", "\n".join(lines[:2] + lines[2:6][::-1] + lines[6:])))
        v = self.verdict(p, dc.Universe(pages + [p], POLICY))
        self.assertEqual(v["verdict"], "FAIL")
        self.assertGreaterEqual(v["boilerplate"]["template_sentence_ratio"], 0.5)

    def test_16c_longer_disclaimers_do_not_create_distinctiveness(self):
        u, pages = template_universe()
        longer = md("Barium Sulfide", TEMPLATE_BODY).replace(
            "## Publication blockers\n", "## Publication blockers\n\n- " + " ".join(["Additional caution."] * 60) + "\n")
        p = page("x/longer.md", longer)
        v = self.verdict(p, dc.Universe(pages + [p], POLICY))
        self.assertEqual(v["text"]["similarity"], 1.0)
        self.assertEqual(v["verdict"], "FAIL")

    def test_16d_generic_faq_does_not_count(self):
        u, pages = template_universe()
        faq = ("\n## FAQ\n\n- What is this page? It is a governed reference entry in the atlas.\n"
               "- Is this safety advice? No, it is not safety advice of any kind.\n")
        clones = [page(f"x/faq{i}.md", md(e, TEMPLATE_BODY + faq)) for i, e in enumerate(["Barium Sulfide", "Iron Sulfide", "Tin Sulfide"])]
        u = dc.Universe(pages + clones, POLICY)
        v = self.verdict(clones[0], u)
        self.assertEqual(v["verdict"], "FAIL")
        self.assertGreaterEqual(v["text"]["similarity"], 0.70)

    # ---- engine properties
    def test_lsh_finds_near_duplicates_and_is_deterministic(self):
        u, pages = template_universe()
        light = TEMPLATE_BODY.replace("governed", "controlled")
        extra = [page(f"x/l{i}.md", md(f"Element{i} Sulfide", light + f"\nUnique closing remark number {i} about nothing.\n"))
                 for i in range(4)]
        u = dc.Universe(pages + extra, POLICY)
        pairs1, stats1 = u.audit_pairs()
        pairs2, stats2 = u.audit_pairs()
        self.assertEqual(pairs1, pairs2)
        self.assertEqual(stats1, stats2)
        self.assertEqual(stats1.get("lsh_recall_ge_0_7"), 1.0)

    def test_html_infrastructure_is_excluded(self):
        html = ("<html lang='en'><head><title>Zinc Sulfide — Bisulfid Atlas</title>"
                "<meta name='robots' content='index, follow'></head><body data-atlas-lane='terminology'>"
                "<header><nav><a href='/'>Home</a></nav></header><main>"
                "<div aria-hidden='true'>decorative lattice label</div><h1>Zinc Sulfide</h1>"
                "<h2>Mineral forms</h2><p>Sphalerite and wurtzite are the two zinc sulfide structures.</p>"
                "<h2>Navigation</h2><p>Return to atlas hubs via the Terminology Spine.</p></main>"
                "<footer>footer text</footer></body></html>")
        p = dc.parse_html("site/public/zinc-sulfide/index.html", html, POLICY, RULES)
        self.assertTrue(p.public_indexable)
        self.assertEqual(p.skeleton, ("mineral forms",))
        body = " ".join(p.masked_tokens)
        self.assertNotIn("decorative", body)
        self.assertNotIn("footer", body)
        self.assertNotIn("return", body)
        self.assertIn("sphalerite", body)


if __name__ == "__main__":
    unittest.main(verbosity=2)
