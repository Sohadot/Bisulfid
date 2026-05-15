# Source Registry Seed Report — Sprint 3

**Date:** 2026-05-15  
**Branch:** claude/sprint-3-source-registry-seed  
**Governed by:** doctrine/SOURCE_POLICY.md

---

## Summary

Sprint 3 seeds the first real entries into `source_registry.json`, assigns candidate `source_ids` to eight ontology terms in `sulfur_terms.json`, and registers five terminology claims and three science claims in the claim registries. No claim has been approved. No route has been published. No [SOURCE REQUIRED] marker has been removed from any content page.

---

## Sources Seeded (8)

All sources carry `status: "seeded"`, `source_lock_status: "candidate"`, and `last_reviewed: "2026-05-15"`. None are final or permanently approved.

| source_id | category | publisher | title |
|---|---|---|---|
| SRC-MW-BISULFIDE | authoritative_dictionary | Merriam-Webster | bisulfide |
| SRC-MW-SULFIDE | authoritative_dictionary | Merriam-Webster | sulfide |
| SRC-MW-BISULFITE | authoritative_dictionary | Merriam-Webster | bisulfite |
| SRC-DUDEN-SULFID | authoritative_dictionary | Duden | Sulfid |
| SRC-IUPAC-HYDROSULFIDES | chemical_nomenclature_standard | IUPAC Gold Book | hydrosulfides |
| SRC-PUBCHEM-HYDROSULFIDE | government_scientific_database | PubChem / NIH | Hydrosulfide |
| SRC-PUBCHEM-SODIUM-HYDROSULFIDE | government_scientific_database | PubChem / NIH | Sodium hydrosulfide |
| SRC-NIST-HYDROGEN-SULFIDE | government_scientific_database | NIST Chemistry WebBook | Hydrogen sulfide |

### Categories represented

- `authoritative_dictionary` — 4 entries (Merriam-Webster ×3, Duden ×1)
- `chemical_nomenclature_standard` — 1 entry (IUPAC Gold Book)
- `government_scientific_database` — 3 entries (PubChem ×2, NIST ×1)

### Categories with no entries this sprint

- `regulatory_body` — no entries (no regulatory claims in scope)
- `peer_reviewed_journal` — no entries (no journal-backed claims in scope)
- `industry_publication` — no entries (industry claims not in scope this sprint)
- `market_report` — no entries (market statistics explicitly excluded)

---

## Why Market Sources Were Excluded

Market data sources (production statistics, trade volumes, pricing data for Gulf, Morocco, China, or other regions) were explicitly excluded from this sprint. No market statistics were added. No acquisition-target company claims were added. `market_claims.json` was not modified. `acquisition_claims.json` was not modified. The blocked source use `market_statistics_without_verified_source` remains in force.

---

## Why No Claims Were Approved

All claims in `terminology_claims.json` and `science_claims.json` carry `status: "pending_review"`. No claim carries `status: "approved"`. Claim approval requires a dedicated source-locking sprint in which URLs are verified, accessed, and confirmed against their stated content. Sprint 3 seeds candidates only — it does not lock or approve them.

The registry-level `status` fields remain `"inactive"` for both claim files and for the source registry itself.

---

## Terminology Claims Registered (5)

All carry `status: "pending_review"`, `claim_type: "terminology"`.

| claim_id | statement summary | source_ids |
|---|---|---|
| CLM-TERM-001 | English 'bisulfide' has MW lexical entry | SRC-MW-BISULFIDE |
| CLM-TERM-002 | English 'sulfide' has MW lexical entry | SRC-MW-SULFIDE |
| CLM-TERM-003 | German 'Sulfid' has Duden lexical entry | SRC-DUDEN-SULFID |
| CLM-TERM-004 | 'bisulfite' is distinct from 'bisulfide' (MW) | SRC-MW-BISULFITE |
| CLM-TERM-005 | 'hydrosulfides' has IUPAC Gold Book entry | SRC-IUPAC-HYDROSULFIDES |

---

## Science Claims Registered (3)

All carry `status: "pending_review"`, `claim_type: "chemical_identity"`.

| claim_id | statement summary | source_ids |
|---|---|---|
| CLM-SCI-001 | PubChem has Hydrosulfide CID 5047209 | SRC-PUBCHEM-HYDROSULFIDE |
| CLM-SCI-002 | PubChem has Sodium hydrosulfide NaHS CID 28015 | SRC-PUBCHEM-SODIUM-HYDROSULFIDE |
| CLM-SCI-003 | NIST WebBook has Hydrogen sulfide H2S entry | SRC-NIST-HYDROGEN-SULFIDE |

**Note on CIDs:** PubChem compound IDs recorded in CLM-SCI-001 and CLM-SCI-002 are candidate values and must be verified directly against PubChem before any source-locking sprint.

---

## Ontology Terms Receiving Candidate Source IDs (8)

All term `status` values remain `"planned"`. No term was marked `verified` or `published`.

| term_id | source_ids added |
|---|---|
| bisulfide | SRC-MW-BISULFIDE |
| sulfide | SRC-MW-SULFIDE |
| sulfid | SRC-DUDEN-SULFID |
| bisulfite_disambiguation | SRC-MW-BISULFITE |
| hydrosulfide | SRC-IUPAC-HYDROSULFIDES, SRC-PUBCHEM-HYDROSULFIDE |
| sodium_hydrosulfide | SRC-PUBCHEM-SODIUM-HYDROSULFIDE |
| sodium_bisulfide | SRC-PUBCHEM-SODIUM-HYDROSULFIDE |
| hydrogen_sulfide | SRC-NIST-HYDROGEN-SULFIDE |

**Note on sodium_bisulfide:** The PubChem Sodium hydrosulfide source is assigned as a candidate synonym/identity source only. It does not confirm the 'sodium bisulfide' name directly. The naming relationship between sodium bisulfide and sodium hydrosulfide requires dedicated source-locking.

### Terms with no source_ids added this sprint

| term_id | reason |
|---|---|
| bisulfid | Center node. No EN/DE dictionary entry directly under 'bisulfid' spelling identified for seeding. Source-locking sprint required. |
| disulfide | No disulfide-specific source in scope this sprint. |
| disulfid | German-form. No Duden 'Disulfid' entry identified for seeding. |
| molybdenum_disulfide | No molybdenum disulfide source in scope this sprint. |
| molybdenum_disulfide_mos2 | Formula alias. No separate source in scope. |
| sulfur | Foundational element. No elemental sulfur source in scope this sprint. |

---

## Remaining Gaps

- `bisulfid` term has no source_ids. This is the center node of the ontology. Source-locking for this term is the highest priority for the next source sprint.
- No DE-language sources for `bisulfid`, `bisulfide` (German chemical contexts), or `disulfid`.
- No IUPAC or authoritative source for the bisulfide/bisulfid spelling boundary itself.
- No peer-reviewed journal sources in registry.
- No market or regulatory sources in registry.
- All claims remain pending_review. No claim is approved.

---

## Publication State

- All draft pages remain `status: draft`, `publication_status: non_public`.
- All draft pages remain `indexable: false`, `in_sitemap: false`.
- All [SOURCE REQUIRED] markers remain in all draft content pages.
- No route has been published.
- The source registry `status` remains `"inactive"`.
- No Quality Gate has been passed.
- This sprint does not constitute publication readiness.
