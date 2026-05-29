# Supporting Candidate Boundary Review — Wave 1

**Sprint:** 5N-H  
**Scope:** PubChem, NIST Chemistry WebBook, Chemie.de for `de_core_mos2`  
**Date:** 2026-05-27

---

## PubChem support boundary

| Field | Boundary |
| --- | --- |
| Candidate target | PubChem — Molybdenum disulfide / CID 14823 |
| Classification | `supporting_database_candidate_only`, `supports_identity_not_german_lexical_authority`, `rejected_as_primary_german_authority` |
| Allowed scope | MoS2 chemical identity reference; CID-level database context |
| Forbidden scope | German lexical authority; document-language primary citation; market or application claims |
| Primary authority | **No** |
| Proposal role | Supporting database reference row only — if included in future proposal |

---

## Why PubChem supports identity/database context but not German lexical authority

| Reason | Detail |
| --- | --- |
| Language | PubChem is an **English/international** chemical database — not a DE specialist lexicon |
| Authority class | `scientific_database_authority` — identity tier, not `authoritative_dictionary` (DE) |
| DE page requirement | `de_core_mos2` lexical lines require German-verifiable specialist dictionary authority |
| Drift risk | Database compound records can be misused for industrial lubricant or application framing — blocked |
| Verification finding | Explicitly **rejected as primary German authority** |

PubChem may corroborate **what compound** MoS2 refers to at database identity level. It cannot establish **how German specialist lexicon documents** name or frame the compound for DE terminology governance.

---

## NIST support boundary

| Field | Boundary |
| --- | --- |
| Candidate target | NIST Chemistry WebBook — molybdenum disulphide |
| Classification | `supporting_technical_data_candidate_only`, `supports_technical_context_not_german_lexical_authority`, `rejected_as_primary_german_authority` |
| Allowed scope | Formula, CAS, thermochemistry, technical reference data context |
| Forbidden scope | German lexical authority; primary citation for document-language lines; prescriptive safety or operational use |
| Primary authority | **No** |
| Proposal role | Supporting technical data reference only — if included in future proposal |

---

## Why NIST supports technical data context but not German lexical authority

| Reason | Detail |
| --- | --- |
| Reference type | NIST Chemistry WebBook is a **technical data compendium** — not a DE lexicon |
| Language | English technical reference context |
| Scope fit | Supports formula/CAS/physical property context where draft requires technical corroboration |
| Lexical gap | Does not provide German specialist compound naming authority for DE terminology page |
| Verification finding | Explicitly **rejected as primary German authority** |

NIST may support **technical corroboration** within bounded lines. It cannot replace Spektrum for German lexical authority.

---

## Chemie.de support boundary

| Field | Boundary |
| --- | --- |
| Candidate target | Chemie.de Lexikon — Molybdän(IV)-sulfid |
| Classification | `secondary_german_support_only`, `not_primary_authority`, `rejected_as_primary_authority` |
| Allowed scope | Secondary German-language cross-check; supplementary DE vocabulary context |
| Forbidden scope | Primary lexical authority; replacement for Spektrum; sole citation for strict-registry lines |
| Primary authority | **No** |
| Proposal role | Secondary DE support reference only — if included in future proposal |

---

## Why Chemie.de is secondary German support only

| Reason | Detail |
| --- | --- |
| Authority tier | Web-based chemistry lexicon — secondary tier, not specialist reference lexicon |
| Primary candidate | Spektrum verified as primary DE specialist lexicon candidate |
| Elevation risk | Using Chemie.de as primary would bypass specialist lexicon discipline |
| Consistency | DE support must not contradict Spektrum primary lines without human resolution |
| Verification finding | **`not_primary_authority`**, **`rejected_as_primary_authority`** |

Chemie.de may assist **cross-checking** German surface forms. It must not become the governing lexical authority for `de_core_mos2`.

---

## Why supporting candidates cannot replace primary authority

| Risk | Mitigation |
| --- | --- |
| Database substituted for lexicon | PubChem/NIST explicitly rejected as primary German authority |
| Web lexicon elevated to primary | Chemie.de explicitly secondary-only |
| Thin authority stack | DE strict-registry page requires specialist lexicon primary tier |
| Corpus-wide precedent | Supporting-only discipline must hold for all future DE terminology routes |
| Launch integrity | **500-page** threshold requires authority discipline at source layer |

Supporting candidates **supplement** Spektrum — they do not **replace** it.

---

## Why supporting candidates do not approve claims

| Reason | Detail |
| --- | --- |
| Claim registries inactive | **0** approved claims |
| Database identity ≠ terminology claim | PubChem CID does not authorize lexical claims |
| Technical data ≠ lexical claim | NIST thermochemistry does not authorize German naming claims |
| Secondary lexicon ≠ claim approval | Chemie.de cross-check does not activate claim registry |
| Verification scope | Role boundaries only — no claim boundary registration in 5N-H |

---

## Why supporting candidates do not make the page source-locked

| Reason | Detail |
| --- | --- |
| No registry rows | Supporting candidates not entered in `source_registry.json` |
| No audited linkage | Draft lines retain `[SOURCE REQUIRED]` markers |
| Verification ≠ locking | Boundary confirmation does not create source-to-line mapping |
| Content unchanged | `de_core_mos2` draft not modified |

---

## Why supporting candidates do not make the page publication-ready

| Gate | Status |
| --- | --- |
| Primary candidate | Verified for proposal — **not approved** |
| Supporting candidates | Bounded — **not approved** |
| Route | `planned`, non-indexable |
| Launch threshold | **126** / **500** |
| `production_can_safely_proceed` | **no** |

Supporting boundary review preserves publication blockers — it does not clear them.

---

## Related documents

- `NAMED_CANDIDATE_HUMAN_VERIFICATION_WAVE_1_REPORT.md`
- `NAMED_CANDIDATE_HUMAN_VERIFICATION_MATRIX_WAVE_1.md`
- `SPEKTRUM_CANDIDATE_AUTHORITY_REVIEW_WAVE_1.md`
- `NAMED_SOURCE_CANDIDATE_REJECTION_RULES_WAVE_1.md`
