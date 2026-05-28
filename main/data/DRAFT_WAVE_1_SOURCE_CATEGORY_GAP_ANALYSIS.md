# Draft Wave 1 — Source Category Gap Analysis

**Sprint:** 5M  
**Date:** 2026-05-27  
**Scope:** Source mapping wave 1 (12 cohort-A drafts) + registry/policy review

---

## Purpose

Identify which source **categories** are sufficient today, which require **future discovery**, and how gaps block publication, claim approval, or hardening only.

Registry reviewed: `main/data/sources/source_registry.json` (**inactive**, read-only). Policy reviewed: `doctrine/SOURCE_POLICY.md`.

---

## Categories currently sufficient

### Doctrine / internal governance only

| Category | Sufficiency | Applies to |
| --- | --- | --- |
| `doctrine_internal_only` | **Sufficient** for framing and process description | Future governance/index pages (not in cohort A) |
| Internal SOURCE_POLICY references | **Sufficient** for explaining rules | Citation discipline, registry explainers (deferred cohort) |

Cohort A drafts are **terminology pages**—doctrine alone is **not** sufficient for their factual markers.

### Existing registry categories (policy-level; not mapped)

| Registry category | Status | Cohort A relevance |
| --- | --- | --- |
| `authoritative_dictionary` | Seeded EN rows exist; **candidate** only | Partial pattern for EN terms; no row mapped to cohort A |
| `chemical_nomenclature_standard` | Seeded IUPAC rows; **candidate** | Needed for salt/compound naming drafts |
| `government_scientific_database` | Seeded entries; **candidate** | Relevant to `sulfur_element_term_record` |
| `academic_teaching_reference` | Seeded teaching rows; **candidate** | Teaching-tier only; cannot alone lock formal claims |

**Finding:** Categories exist in policy/registry schema but **no cohort-A draft** has completed marker-to-row mapping.

---

## Categories needing later external source discovery

| Mapping category | Drafts | Discovery need |
| --- | ---: | --- |
| `English_chemical_terminology_authority_needed` | 1 | Element + specialist EN naming references |
| `German_lexical_authority_needed` | 5 | DE dictionary / lexical references |
| `multilingual_terminology_authority_needed` | 2 | Bilingual glossary / bridge references |
| `terminology_dictionary_needed` | 6 | Specialist compound and mineral naming |
| `external_source_discovery_needed` (all cohort A) | **12** | Every mapped draft |

---

## Categories needing formal nomenclature authority

| Draft | Need |
| --- | --- |
| `de_core_cas` | IUPAC-aligned salt naming (CaS) |
| `carbonyl_sulfide_terms` | Systematic compound naming |
| `copper_sulfides_language` | Mineral/formula naming conventions |
| `de_bridge_en_de_suffix` | Morphological rules (non-normative framing) |
| `de_core_cus`, `de_core_fes`, `de_core_mos2` | Localized systematic names |

**Gap:** `chemical_nomenclature_standard` rows are seeded but **not verified**, **not linked** to draft markers, registry **inactive**.

---

## Categories needing German lexical or dictionary authority

| Draft | Need |
| --- | --- |
| `sulfid` | DE Sulfid lexical record |
| `de_glossary` | DE glossary chamber |
| `de_core_cus`, `de_core_fes` | DE mineral naming |
| `de_german_english_chemical_terms` | DE side of crosswalk |

**Gap:** No governed **DE authoritative_dictionary** bundle; existing MW rows are **EN only**.

---

## Categories needing English chemical terminology authority

| Draft | Need |
| --- | --- |
| `sulfur_element_term_record` | Element identity |
| `carbonyl_sulfide_terms` | COS compound |
| `copper_sulfides_language` | EN mineral vocabulary |
| `sulfid` | EN-side DE-lexical bridge context |

---

## Categories needing multilingual terminology authority

| Draft | Need |
| --- | --- |
| `de_bridge_en_de_suffix` | Suffix bridge |
| `de_german_english_chemical_terms` | Crosswalk table |
| `de_glossary` | DE chamber with EN spine coupling |

**Gap:** No hreflang/translation source governance active; multilingual mapping must wait on EN source plans for mirrored terms.

---

## Categories needing industry/compliance document-language support

**Not in cohort A** (mapped in Sprint 5L medium-risk prep only):

| Category | Drafts (deferred) |
| --- | ---: |
| `industry_document_language_source_needed` | 3 industrial + 2 DE industrial-adjacent |
| `compliance_document_language_source_needed` | 3 compliance |

These require claim-boundary work **before** source mapping per Sprint **5M** medium-risk prep.

---

## Gaps in current source registry

| Registry gap | Blocker type |
| --- | --- |
| Registry status **inactive** | Blocks all publication and claim approval |
| All rows `candidate` / not verified | Blocks marker satisfaction |
| No DE lexical source rows mapped to drafts | Blocks DE cohort publication |
| No row-level marker mapping manifest | Blocks source-lock sprints |
| No linked_claims wiring | Blocks claim approval path |
| Seeded URLs exist but registry edits forbidden this sprint | Blocks immediate registration |

---

## Gaps in current source policy

| Policy gap | Impact |
| --- | --- |
| `academic_teaching_reference` cannot alone approve formal claims | Cohort A needs stronger tiers for many markers |
| No governed DE dictionary category separate from EN | DE drafts lack explicit policy path |
| Multilingual authority not a distinct approved category | Bridge/table pages rely on composite discovery |
| Biogenic/environmental tier underspecified | `de_core_biogenic_lang` needs policy extension or teaching-tier scoping |

**Recommendation:** Future `source_policy_extension_needed` sprint to document DE lexical tier and biogenic vocabulary rules before registration wave.

---

## Gap impact matrix

| Gap | Blocks publication | Blocks claim approval | Blocks hardening only |
| --- | --- | --- | --- |
| Inactive registry | **Yes** | **Yes** | — |
| Unverified candidate sources | **Yes** | **Yes** | — |
| Missing DE lexical rows | **Yes** | **Yes** | Partial mapping prep OK |
| Missing marker-to-row mapping | **Yes** | **Yes** | — |
| Medium-risk claim boundaries undefined | **Yes** | **Yes** | Source mapping prep blocked for 20 drafts |
| Unwired internal links | **Yes** | No | Index/hardening |
| Legacy draft structure (18 pre-5J) | **Yes** | Partial | Hardening sprint |

---

## Recommended future source registration sprint

**Sprint 5N-A — Source registration proposal wave 1** (report-only):

| Parameter | Value |
| --- | --- |
| Batch size | **4–6** drafts |
| First candidates | `sulfur_element_term_record`, `de_core_biogenic_lang`, `copper_sulfides_language`, `de_core_cus` |
| Output | Candidate row **proposals** with marker mapping manifest |
| Forbidden | Registry activation without charter; marker removal; verified status without human review |

Follow with broader registration only after claim-boundary report (5N-B) and L1 PASS.

---

*Sprint 5M — Source Category Gap Analysis*
