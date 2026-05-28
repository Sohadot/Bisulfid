# Candidate Source Discovery Wave 1 — Report

**Sprint:** 5N-C  
**Date:** 2026-05-28  
**Branch:** `claude/sprint-5n-c-candidate-source-discovery-wave-1`

---

## Why this sprint exists

Sprint **5N-A** defined source registration **proposals** for **5** low-risk drafts. Sprint **5N-B** established guardrail automation. Sprint **5N-C** creates the first **candidate source discovery layer** — classifying source families, search targets, authority requirements, and rejection rules without registering sources or implying approval.

---

## Why candidate source discovery comes after source registration proposals

Proposals define **what** future registration would require (evidence types, policy gaps, registry categories). Discovery defines **which source families and search targets** humans should evaluate next — still without writing registry rows or satisfying markers.

---

## Why candidate discovery still comes before source_registry edits

| Reason | Detail |
| --- | --- |
| Registry inactive | `source_registry.json` status **inactive** |
| Candidate ≠ verified | Discovery targets are **not** approved entries |
| Guardrail gate | Sprint **5N-B** runtime must PASS before and after any registry sprint |
| Human charter | Named source verification precedes any row write |
| Marker discipline | `[SOURCE REQUIRED]` remains until audited satisfaction |

---

## Relationship to Sprint 5N-A

Discovery covers exactly the **5** drafts from `SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md`, inheriting proposal statuses, authority tiers, and evidence requirements.

---

## Relationship to Sprint 5N-B guardrail automation

Pre-flight and post-sprint validation: `source_claim_guardrail_runtime_l1.py` and `corpus_validation_runtime_l1.py` both **PASS**. Discovery documents must not trigger guardrail failures (no approval language, no URLs, no registry edits).

---

## Relationship to Sprint 5M source mapping

Sprint **5M** mapped source gaps for cohort-A drafts. Discovery operationalizes mapping + proposal rows into **search targets** and **rejection rules** for human review.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Proposed drafts (5N-A) | **5** |
| Discovery rows this sprint | **5** |
| Registry entries added | **0** |
| Publication-ready | **0** |

Discovery advances **governance readiness** without increasing published surface.

---

## Files reviewed

- `main/data/SOURCE_REGISTRATION_PROPOSAL_WAVE_1_REPORT.md`
- `main/data/SOURCE_REGISTRATION_PROPOSAL_MATRIX_WAVE_1.md`
- `main/data/SOURCE_EVIDENCE_REQUIREMENT_MATRIX_WAVE_1.md`
- `main/data/SOURCE_REGISTRATION_RISK_REVIEW_WAVE_1.md`
- `main/data/SOURCE_REGISTRATION_NEXT_ACTIONS_WAVE_1.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_SCRIPT_REGISTRY.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_VALIDATION_REPORT.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_NEXT_ACTIONS.md`
- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_MATRIX.md`
- `main/data/DRAFT_WAVE_1_SOURCE_CATEGORY_GAP_ANALYSIS.md`
- `doctrine/SOURCE_POLICY.md`
- `main/data/sources/source_registry.json` (read-only)
- `main/data/claims/terminology_claims.json` (read-only)
- **5** selected draft content files (read-only)

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5N-B | **Yes** |
| Guardrail runtime | **PASS** |
| Corpus L1 runtime | **PASS** |
| Selected drafts exist | **5/5** |
| Match `routes.json` | **5/5** |
| draft / non_public / non-indexable | **5/5** |
| Registry unchanged pre-sprint | **Yes** |
| Content modified | **0** |

---

## Selected draft count

**5** drafts.

---

## Selected route_id list

```
sulfur_element_term_record
de_core_biogenic_lang
copper_sulfides_language
de_core_fes
de_core_mos2
```

---

## Language split

| Language | Count |
| --- | ---: |
| English (`en`) | **2** |
| German (`de`) | **3** |

---

## Source discovery methodology

1. Read Sprint **5N-A** proposal and evidence matrix rows per draft.
2. Read Sprint **5M** mapping row and draft markers (read-only).
3. Review `SOURCE_POLICY.md` approved categories and seeded registry **families** (no new rows).
4. Assign candidate discovery status, source family, and search target **without URLs or bibliographic fabrication**.
5. Document authority requirements and rejection rules.
6. Confirm guardrail + corpus L1 **PASS** after document creation.

---

## Candidate source family principles

- Name **families** and **search target types**, not verified registry rows.
- Prefer categories already in SOURCE_POLICY (`government_scientific_database`, `authoritative_dictionary`, `academic_teaching_reference`, `chemical_nomenclature_standard`).
- DE drafts require **German_lexical_dictionary_reference** discovery where applicable.
- Teaching references are **supporting** tiers only unless paired with stronger authority.
- Seeded registry rows are **reference patterns**, not discovery approvals.

---

## Authority requirement principles

- Match Sprint **5N-A** evidence matrix formal/dictionary/teaching flags.
- Block doctrine-only satisfaction for external factual lines.
- Require formal nomenclature discovery where systematic mineral/compound names are in scope.
- Scope DE lexical authority to naming and usage — not compliance or market claims.

---

## What candidate source discovery means in this sprint

- Defines **where to look** (source family + search target type)
- Defines **what to reject** before registry consideration
- Defines **what humans must verify** before any registry proposal
- Prepares a future **human candidate source review** or **registry execution** sprint

---

## What candidate source discovery does not mean

| Not implied | Reason |
| --- | --- |
| Source approved | Candidates are discovery targets only |
| Source-lock complete | Markers remain |
| Registry row exists | No entries added |
| Claim approved | Registries inactive |
| Publication-ready | All posture flags **no** |
| Bibliographic certainty | No invented publisher/edition/URL |

---

## Why no source entries were added

Sprint charter: **discovery-planning only**. Registry modification requires separate human-chartered execution after named source verification.

---

## Why source_registry.json was not modified

Explicit sprint rule. Registry remains **inactive** with **14** seeded **candidate** rows.

---

## Why no claims were approved

Claim registries **inactive**. Discovery does not activate or approve claims.

---

## Why terminology_claims.json was not modified

Discovery sprint only. Claim boundary work remains separate.

---

## Why no content pages were modified

Editing drafts would conflate discovery with production. `[SOURCE REQUIRED]` markers remain.

---

## Why `[SOURCE REQUIRED]` markers remain

Discovery identifies targets; it does not satisfy authority lines.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, out of sitemap/navigation.

---

## Candidate discovery findings by draft

| route_id | Discovery status | Primary family | Search target summary |
| --- | --- | --- | --- |
| `sulfur_element_term_record` | needs_primary_authority_discovery | scientific_database_reference | Named government/scientific element-record database tier |
| `de_core_biogenic_lang` | needs_dictionary_or_lexical_discovery | German_lexical_dictionary_reference | DE biogenic/environmental controlled lexicon |
| `copper_sulfides_language` | needs_formal_nomenclature_discovery | chemistry_dictionary_reference | Mineral variant dictionary + nomenclature teaching support |
| `de_core_fes` | needs_dictionary_or_lexical_discovery | German_lexical_dictionary_reference | DE mineral naming lexicon for iron sulfide variants |
| `de_core_mos2` | discovery_ready | chemistry_dictionary_reference | DE specialist compound naming lexicon for MoS2 |

---

## Candidate source family gaps

- No DE biogenic tier in SOURCE_POLICY (flagged in 5N-A)
- No element-tier row mapped to `sulfur_element_term_record` markers
- No DE iron sulfide or MoS2 naming rows in registry
- Mineral variant lines unmapped for `copper_sulfides_language`

---

## Authority gaps

- `sulfur_element_term_record`: element identity database discovery not yet named by human review
- `de_core_biogenic_lang`: DE lexical path underspecified vs EN dictionary rows
- `copper_sulfides_language`, `de_core_fes`, `de_core_mos2`: formal nomenclature support needed alongside dictionary tier

---

## Registry blockers

- Registry **inactive**
- No marker-to-row mapping manifest
- No human-verified named candidates
- Policy extension may be required (`de_core_biogenic_lang`)
- Guardrail runtime must PASS at execution time

---

## Publication blocker summary

| Blocker | All 5 drafts |
| --- | --- |
| Unresolved markers | **Yes** |
| Registry inactive | **Yes** |
| Route `planned` | **Yes** |
| Discovery ≠ verification | **Yes** |
| Publication-ready | **No** |

---

## Recommended next sprint

**Sprint 5N-D — Human candidate source review wave 1**: evaluate named candidates against rejection rules; still **no** registry edits unless chartered execution sprint follows. Run guardrail + corpus L1 before and after.

See `CANDIDATE_SOURCE_DISCOVERY_NEXT_ACTIONS_WAVE_1.md`.

---

*Sprint 5N-C — Candidate Source Discovery Wave 1 Report*
