# Human Source Rejection Decisions — Wave 1

**Sprint:** 5N-D  
**Date:** 2026-05-28

---

## General rejection decisions for weak or misaligned candidate sources

**Reject for registry consideration now** any candidate that:

- Cannot be named to publisher/institution/database class by human verification
- Lacks SOURCE_POLICY category fit
- Would partially satisfy markers while implying full source-lock
- Primary purpose is aggregation, marketing, or uncited summarization
- Conflicts with doctrine blocked_source_uses

**Decision:** All **5** drafts remain **rejected for source_registry_now** until named verified candidates pass acceptance criteria.

---

## Rejection decisions for unsourced web content

**Reject:** blogs, forums, uncited wikis, user-editable pages without governance charter.

**Rationale:** No stable authority chain for terminology claims.

---

## Rejection decisions for AI-generated summaries

**Reject:** AI summaries, tool output, or generated text presented as bibliographic sources.

**Rationale:** Aligns with SOURCE_POLICY `AI_summary_as_source` blocked use and Sprint **5N-B** guardrails.

---

## Rejection decisions for commercial pages without authority

**Reject:** commercial landing pages, product marketing, vendor pages without dictionary/database/nomenclature authority structure.

**Rationale:** Terminology pages require governed reference tiers — not commercial framing.

---

## Rejection decisions for safety/medical/procurement/market content

**Reject** candidates whose primary content is:

- SDS sheets, handling instructions, exposure thresholds
- Medical or therapeutic claims
- Market research, CAGR, pricing, investment, commodity statistics
- Procurement, assay, ore-grade, or trade language

**Per-draft sensitivity:** `de_core_fes` (pyrite/commodity), `de_core_mos2` (lubricant market), `de_core_biogenic_lang` (climate/emissions).

---

## Rejection decisions for teaching sources used as formal authority

**Reject** when teaching reference is:

- Sole authority for element identity (`sulfur_element_term_record`)
- Sole authority for IUPAC/systematic names (`copper_sulfides_language`, `de_core_fes`, `de_core_mos2`)
- Used to justify marker removal without paired stronger tier

**Allow:** `suitable_for_teaching_context_only` as **supporting** tier after human verification.

---

## Rejection decisions for dictionaries used as chemical authority

**Reject** when dictionary is used to prove:

- Chemical reactivity, safety, or toxicology
- Market or trade classifications
- Formal nomenclature rules without nomenclature-standard tier

**Allow:** dictionary for **naming and lexical usage** lines only.

---

## Rejection decisions for multilingual equivalents used as universal equivalence

**Reject:**

- Blanket EN↔DE equivalence from one dictionary pair
- EN dictionary assigned to DE-only naming without DE lexical review
- Suffix-bridge rules applied to core naming pages

**Note:** DE drafts require **independent** DE lexical verification — not EN mirror inference.

---

## Rejection decisions for document-language sources used as legal or compliance advice

**Reject** when industry/compliance document-language sources:

- Provide legal verdicts, customs determinations, or export guidance
- Are applied to core terminology naming drafts in this wave

---

## Per-draft rejection or caution notes

| route_id | Rejection / caution decision |
| --- | --- |
| `sulfur_element_term_record` | **Caution:** reject teaching-only element identity; **defer** until human names scientific database tier |
| `de_core_biogenic_lang` | **Block:** registry until SOURCE_POLICY extension; reject climate/market/regulatory-primary sources |
| `copper_sulfides_language` | **Caution:** reject mining/procurement sources; require split dictionary + nomenclature tiers |
| `de_core_fes` | **Caution:** reject commodity/pyrite market sources; require DE lexical + formal nomenclature split |
| `de_core_mos2` | **Caution:** reject lubricant/application market sources; **review_candidate_ready** pending named DE lexicon verification |

---

## Why rejected or blocked candidates must not enter source_registry.json

- Registry rows create governed audit artifacts
- Blocked/rejected candidates would pollute trust root
- Inactive registry must not accumulate unverified rows
- Guardrail and SOURCE_POLICY alignment would fail or require cleanup

---

## Why rejected or blocked candidates must not be used to remove `[SOURCE REQUIRED]` markers

- Markers denote unresolved authority — not missing prose
- Blocked candidates (`de_core_biogenic_lang`) lack policy and verification completion
- Deferred candidates lack named human-verified sources
- Claim registries remain **inactive**
- Publication remains blocked for all **5** drafts

---

*Sprint 5N-D — Human Source Rejection Decisions Wave 1*
