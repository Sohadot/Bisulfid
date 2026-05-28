# Source Registration Proposal Wave 1 — Report

**Sprint:** 5N-A  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5n-a-source-registration-proposals-wave-1`

---

## Why this sprint exists

Sprint **5M** mapped **12** cohort-A drafts but explicitly forbade `source_registry.json` edits. Sprint **5N-A** prepares the first **source registration proposal wave** for **5** lowest-gap drafts—defining what future registry rows would require without adding entries, satisfying markers, or implying source-lock completion.

---

## Why source registration proposals come before source_registry edits

| Reason | Detail |
| --- | --- |
| Registry inactive | `source_registry.json` status **inactive** |
| Candidate ≠ verified | Seeded rows are **candidate** only |
| Marker alignment | Proposals must map evidence types before rows are written |
| Human governance | SOURCE_POLICY requires verified entries; proposals precede human charter |
| Accident prevention | Premature registry edits could imply false authority |

---

## Relationship to Sprint 5M

Sprint **5M** produced mapping matrices and identified **12** drafts with source gaps. Sprint **5N-A** selects **5** from that cohort and produces registration **proposals** only. **7** mapped drafts deferred (see Selection).

---

## Relationship to Sprint 5L

Sprint **5L** classified all **50** wave-1 drafts. Cohort-A **5** were `ready_for_source_mapping`. Proposals inherit 5L/5M risk tiers; no 5L classifications changed.

---

## Relationship to Sprint 5K automation runtime

Pre-flight: `python scripts/corpus_validation_runtime_l1.py` — **PASS** (2026-05-27).

L1 confirms structural discipline. Proposals are governance artifacts outside L1 scope.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Cohort-A mapped (5M) | **12** |
| Proposals this sprint | **5** |
| Registry entries added | **0** |
| Publication-ready | **0** |

Proposals advance **governance readiness**, not publication eligibility.

---

## Files reviewed

- `main/data/routes.json`
- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_WAVE_1_REPORT.md`
- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_MATRIX.md`
- `main/data/DRAFT_WAVE_1_SOURCE_CATEGORY_GAP_ANALYSIS.md`
- `main/data/DRAFT_WAVE_1_MEDIUM_RISK_CLAIM_BOUNDARY_PREP.md`
- `main/data/DRAFT_WAVE_1_SOURCE_MAPPING_NEXT_ACTIONS.md`
- `main/data/DRAFT_WAVE_1_SOURCE_CLAIM_BOUNDARY_REVIEW.md`
- `main/data/DRAFT_WAVE_1_SOURCE_REQUIREMENT_MATRIX.md`
- `main/data/DRAFT_WAVE_1_CLAIM_RISK_MATRIX.md`
- `main/data/DRAFT_WAVE_1_PUBLICATION_BLOCKER_MATRIX.md`
- `main/data/CORPUS_L1_VALIDATION_REPORT.md`
- `doctrine/SOURCE_POLICY.md`
- `main/data/sources/source_registry.json` (read-only)
- `main/data/claims/terminology_claims.json` (read-only)
- **5** selected draft content files (read-only)

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Branch based on main after Sprint 5M | **Yes** |
| 12 mapped drafts in 5M matrix | **Yes** |
| Selected drafts exist | **5/5** |
| Match `routes.json` | **5/5** |
| `draft` / `non_public` / non-indexable | **5/5** |
| L1 runtime | **PASS** |
| Content modified | **0** |
| Registry modified | **0** |

---

## Selected draft count

**5** drafts (preferred target within 4–6 band).

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

## Deferred from cohort-A (7)

| route_id | Reason |
| --- | --- |
| `sulfid` | DE lexical authority discovery must precede EN bridge proposal |
| `carbonyl_sulfide_terms` | Formal authority + toxicology-adjacent drift risk |
| `de_glossary` | Glossary chamber needs row-level mapping plan |
| `de_bridge_en_de_suffix` | Multilingual morphological authority |
| `de_german_english_chemical_terms` | Crosswalk requires per-row mapping |
| `de_core_cas` | Formal nomenclature authority blocked until discovery |
| `de_core_cus` | Deferred until EN `copper_sulfides_language` proposal completes |

---

## Language split (selected)

| Language | Count |
| --- | ---: |
| English (`en`) | **2** |
| German (`de`) | **3** |

---

## Route category / layer split

| Category | Count |
| --- | ---: |
| Core terminology (`terminology_system`) | **5** |

---

## Selection methodology

1. Start from Sprint **5M** cohort-A (**12** drafts).
2. Exclude blocked, multilingual-bridge, chamber-table, and formal-authority-first drafts.
3. Prioritize Sprint **5M** “closest to future source registration” list.
4. Prefer `formal authority needed later: no` where available.
5. Select **5** with clearest dictionary/element/mineral naming paths.
6. Defer DE mirror (`de_core_cus`) until EN copper proposal completes.

---

## Source proposal methodology

1. Read Sprint **5M** mapping row per selected draft.
2. Read draft markers and section structure (read-only).
3. Review `SOURCE_POLICY.md` approved categories.
4. Review existing registry **categories** and seeded rows (no edits).
5. Assign proposal status, authority level, and registration readiness.
6. Document evidence requirements and risks.
7. Confirm **no** registry entry, claim approval, or marker satisfaction.

---

## What a source registration proposal means in this sprint

- Defines **future** registry category and source **family** per draft
- Specifies **evidence standards** and acceptable/unacceptable source classes
- Identifies **policy/registry gaps** blocking registration
- Prepares human-reviewed charter for a future registration execution sprint

---

## What a source registration proposal does not mean

| Not implied | Reason |
| --- | --- |
| Source-lock complete | Markers remain |
| Candidate = approved | Registry inactive |
| Publication-ready | Quality Gate not met |
| Claim approved | Registries inactive |
| Registry row exists | No entries added |
| Content may be edited | Proposal sprint only |

---

## Why no source entries were added

Sprint charter: **proposal-only**. Registry modification requires separate human-chartered execution sprint after discovery and review.

---

## Why source_registry.json was not modified

Explicit sprint rule. Registry remains **inactive** with seeded **candidate** rows only.

---

## Why no claims were approved

Claim registries **inactive**. Proposals assign `terminology_claim_candidate_later` at most—no approval path.

---

## Why terminology_claims.json was not modified

Claim boundary registration is Sprint **5N-B** scope. This sprint is source proposals only.

---

## Why no content pages were modified

Editing drafts would conflate proposal with production. `[SOURCE REQUIRED]` markers remain.

---

## Why `[SOURCE REQUIRED]` markers remain

Proposals identify evidence needed; they do not satisfy authority lines.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, out of sitemap/navigation.

---

## Candidate source category findings

| Draft | Proposed registry category | Candidate family |
| --- | --- | --- |
| `sulfur_element_term_record` | `government_scientific_database` | Element identity reference |
| `de_core_biogenic_lang` | `authoritative_dictionary` | DE biogenic/environmental lexicon |
| `copper_sulfides_language` | `authoritative_dictionary` | Mineral naming + nomenclature support |
| `de_core_fes` | `authoritative_dictionary` | DE mineral naming |
| `de_core_mos2` | `authoritative_dictionary` | DE specialist compound naming |

---

## Source policy gaps

- DE lexical authority path underspecified vs EN dictionary rows
- Biogenic/environmental vocabulary tier needs policy extension (`de_core_biogenic_lang`)
- Teaching references cannot alone satisfy formal nomenclature claims
- Multilingual equivalence rules not needed for this **5**-draft subset but remain corpus-wide gap

---

## Source registry gaps

- No marker-to-row mapping manifest for any selected draft
- All rows **candidate** / not verified
- Registry **inactive**
- No DE-specific dictionary rows linked to selected DE drafts
- No biogenic vocabulary category usage in registry

---

## Claim boundary gaps

- All **5** drafts: `terminology_claim_candidate_later` only
- **20** medium-risk drafts still await 5N-B claim-boundary report
- No claim registry activation path open

---

## Publication blocker summary

| Blocker | All 5 drafts |
| --- | --- |
| Unresolved markers | **Yes** |
| Registry inactive | **Yes** |
| Route `planned` | **Yes** |
| No internal link wiring | **Yes** |
| Publication-ready | **No** |

---

## Recommended next sprint

**Sprint 5N-B — Claim boundary registration report** (20 medium-risk drafts) **in parallel with Sprint 5N-C — Candidate source discovery wave 1** for the **5** proposed drafts (identify concrete candidate sources for human review, still **no** registry edits unless chartered).

See `SOURCE_REGISTRATION_NEXT_ACTIONS_WAVE_1.md`.

---

*Sprint 5N-A — Source Registration Proposal Wave 1 Report*
