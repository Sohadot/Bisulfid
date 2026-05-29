# Supporting Source Boundary Proposal Draft — Wave 1

**Sprint:** 5N-I  
**Scope:** PubChem, NIST, Chemie.de for `de_core_mos2` proposal context  
**Date:** 2026-05-29

---

## PubChem proposed support boundary

| Field | Boundary |
| --- | --- |
| Candidate target | PubChem — Molybdenum disulfide / CID 14823 |
| Proposal classification | `supporting_database_boundary_only`, `not_primary_german_authority`, `not_registry_primary_for_de_core_mos2_now` |
| Proposed optional registry role | Supporting database identity reference — secondary row if execution sprint includes it |
| Proposed optional `source_id` (draft label) | `SRC-PUBCHEM-MOS2-CID14823` — **not in registry** |
| Scope if executed | MoS2 chemical identity / CID-level corroboration |
| Excluded scope | German lexical authority; primary DE document-language citation |

---

## Why PubChem is database support only

PubChem is an international chemical database providing compound identity context in English/database framing. It does not provide German specialist lexicon authority required for DE terminology governance on `de_core_mos2`.

---

## Why PubChem is not primary German lexical authority

| Reason | Detail |
| --- | --- |
| Language | English/international database — not DE specialist lexicon |
| Authority class | `scientific_database_authority` — identity tier |
| Verification (5N-H) | **`rejected_as_primary_german_authority`** |
| Proposal rule | Must not be registry primary for `de_core_mos2` |

---

## NIST proposed support boundary

| Field | Boundary |
| --- | --- |
| Candidate target | NIST Chemistry WebBook — molybdenum disulphide |
| Proposal classification | `supporting_technical_boundary_only`, `not_primary_german_authority`, `not_registry_primary_for_de_core_mos2_now` |
| Proposed optional registry role | Supporting technical data reference — secondary row if execution includes it |
| Proposed optional `source_id` (draft label) | `SRC-NIST-MOS2-TECH` — **not in registry** |
| Scope if executed | Formula, CAS, thermochemistry, technical reference context |
| Excluded scope | German lexical authority; prescriptive safety or operational use |

---

## Why NIST is technical data support only

NIST Chemistry WebBook is a technical data compendium — not a German specialist chemistry lexicon. It may corroborate technical properties within bounded lines only.

---

## Why NIST is not primary German lexical authority

| Reason | Detail |
| --- | --- |
| Reference type | Technical data — not DE lexicon |
| Language | English technical context |
| Verification (5N-H) | **`rejected_as_primary_german_authority`** |
| Proposal rule | Must not replace Spektrum as primary |

---

## Chemie.de proposed support boundary

| Field | Boundary |
| --- | --- |
| Candidate target | Chemie.de Lexikon — Molybdän(IV)-sulfid |
| Proposal classification | `secondary_german_support_boundary_only`, `not_primary_authority`, `not_registry_primary_for_de_core_mos2_now` |
| Proposed optional registry role | Secondary DE cross-check — tertiary row if execution includes it |
| Proposed optional `source_id` (draft label) | `SRC-CHEMIE-DE-MOS2-SEC` — **not in registry** |
| Scope if executed | Secondary German vocabulary cross-check |
| Excluded scope | Primary lexical authority; sole citation for strict-registry lines |

---

## Why Chemie.de is secondary German support only

Web-based chemistry lexicon tier is secondary cross-check — not specialist reference lexicon primary tier. Spektrum remains sole primary proposal.

---

## Why supporting candidates cannot replace Spektrum as primary German authority

| Risk | Mitigation |
| --- | --- |
| Database substituted for lexicon | PubChem/NIST explicitly not registry primary |
| Web lexicon elevated | Chemie.de explicitly secondary-only |
| Thin authority stack | DE strict-registry requires specialist lexicon primary |
| Proposal integrity | Primary row reserved for Spektrum only |

Supporting proposal rows **supplement** Spektrum — they do **not** **replace** it.

---

## Why supporting candidates do not approve claims

| Reason | Detail |
| --- | --- |
| Claim registries inactive | **0** approved claims |
| Proposal ≠ claim activation | Draft documents registry intent only |
| Database identity ≠ terminology claim | PubChem CID does not authorize lexical claims |
| Secondary lexicon ≠ claim approval | Chemie.de cross-check does not activate claims |

---

## Why supporting candidates do not make the page source-locked

| Reason | Detail |
| --- | --- |
| No registry rows | Supporting candidates not in `source_registry.json` |
| No audited linkage | Draft retains `[SOURCE REQUIRED]` markers |
| Proposal only | Boundary documentation — not execution |

---

## Why supporting candidates do not make the page publication-ready

| Gate | Status |
| --- | --- |
| Primary proposal | Draft only — not approved |
| Supporting rows | Optional — not approved |
| Route | `planned`, non-indexable |
| Launch threshold | **126** / **500** |
| `production_can_safely_proceed` | **no** |

---

## Related documents

- `SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1_REPORT.md`
- `SOURCE_REGISTRY_PROPOSAL_DRAFT_MATRIX_WAVE_1.md`
- `SPEKTRUM_SOURCE_REGISTRY_PROPOSAL_DRAFT_WAVE_1.md`
- `SUPPORTING_CANDIDATE_BOUNDARY_REVIEW_WAVE_1.md`
