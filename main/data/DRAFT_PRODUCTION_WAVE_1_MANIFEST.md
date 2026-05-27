# Draft Production Wave 1 — Manifest

**Sprint:** 5J  
**Branch:** `claude/sprint-5j-draft-production-wave-1`  
**Date:** 2026-05-27

---

## Why this wave exists

Sprint **5I-B** registered **100** new planned routes (126 total). The corpus must now move from **route registration** (S1) to **draft production** (S2) under the automation control doctrine—creating **non-public draft bodies** for the safest eligible routes without publishing, approving claims, or modifying the route registry.

---

## Relationship to Sprint 5H 500-page threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Routes registered | **126** |
| Draft-backed routes after wave 1 | **68** |
| Gap to threshold | **432** pages still need registration and/or draft work |

Draft production scales governed page bodies toward the threshold while publication remains locked.

---

## Relationship to Sprint 5I-A automation control layer

This wave executes **Stage S2 — Draft production** per `CORPUS_AUTOMATION_WAVE_PROTOCOL.md`:

- Wave size: **50 drafts** (within 40–60 band)
- Validation gate: **L0** (`validate_content_drafts_l0.py`)
- Publication lock: **held**
- Claim lock: **held**
- `routes.json` lock: **held** — no registry edits

---

## Relationship to Sprint 5I-B route registration wave

All **50** targets are **Sprint 5I-B** registered routes with **no pre-existing content file**. Selection prioritizes low-risk structural foundation routes from that wave.

---

## Draft count target

| Metric | Value |
| --- | ---: |
| Target | **50** (within 40–60) |
| Created | **50** |
| Skipped (overwrite) | **0** |

---

## Selected route categories

| Category | Count |
| --- | ---: |
| `core_terminology` | 22 |
| `disambiguation_authority` | 6 |
| `source_governance` | 5 |
| `de_en_chemical_language` | 5 |
| `industrial_economic_interpretation` | 3 |
| `documentation_compliance` | 3 |
| `index_map` | 3 |
| `methodology_reference` | 2 |
| `gateway` | 1 |

---

## Selected language distribution

| Language | Drafts |
| --- | ---: |
| English (`en`) | 30 |
| German (`de`) | 20 |

EN terminology spine, disambiguation, governance, and index routes are prioritized first; DE bridge, lexical, and gateway mirrors follow.

---

## Excluded categories

| Excluded | Reason |
| --- | --- |
| Routes with existing content files | No-overwrite rule |
| Safety / H2S / SDS routes | High risk; source-locking required first |
| Utility (`newsletter`, `acquire`) | Not structural drafts |
| ar/zh/ja mirrors | Deferred per 5I-B charter |
| Market / procurement / medical / handling | Sprint exclusion |
| High-risk / `deferred_high_risk_review` | Not safe for draft without source lock |

---

## Selection rules

1. Prefer Sprint **5I-B** routes missing `content_file` bodies.
2. Score by priority (P0–P3), language (EN structural first), and category (terminology → disambiguation → governance → DE bridge → DE lexical).
3. Use **exact** `content_file` paths from `routes.json`.
4. Skip any path that already exists on disk.
5. No invented `route_id` values.

---

## No-overwrite rule

If a selected `content_file` already exists, **do not overwrite**; skip and document. Sprint 5J created **0** overwrites.

---

## Exact routes.json content_file rule

Every draft path **must equal** the registered `content_file` for its `route_id`. No alternate slugs or directories.

---

## No-publication rule

- No route `status` changes.
- No `published` state.
- Drafts are `non_public` only.

---

## Non-indexable / non-sitemap rule

Frontmatter on every draft: `indexable: false`, `in_sitemap: false`. Routes remain non-indexable in `routes.json`.

---

## Source marker policy

- `[SOURCE REQUIRED]` on factual or authority-sensitive lines.
- No assertion that source-locking is complete.
- No removal of existing `[SOURCE REQUIRED]` markers on pre-existing pages.

---

## Claim approval prohibition

Claim registries remain **inactive**. Drafts must not approve or imply approval of any claim.

---

## Internal reference policy

- **No raw URLs.**
- **No markdown links** to unpublished routes.
- **Plain `route_id` references** or plain text only.

---

## Validation method

1. `scripts/validate_content_drafts_l0.py` — read-only L0 draft validator.
2. Report: `CONTENT_DRAFTS_L0_VALIDATION_REPORT.md`.
3. Human review checkpoint before draft wave 2 or route publication planning.

---

## Human review checkpoint

- Sample 10–15 drafts for tone, boundary discipline, and source-marker coverage.
- Confirm no safety/market/procurement drift.
- Confirm `routes.json` unchanged.

---

## Rollback expectations

Revert Sprint 5J commit to remove new draft files and documentation. No registry rollback required. Pre-existing 18 drafts remain untouched.

---

## Wave 1 draft target registry (machine-readable)

```json
["bisulfid", "sulfid", "hydrosulfide", "sulfide_anion_term_record", "sulfur_element_term_record", "bisulfite_wall_explainer", "nomenclature_governance_overview", "translator_playbook_bisulfide_family", "carbon_disulfide_terms", "carbonyl_sulfide_terms", "copper_sulfides_language", "sulfate_terminology", "academic_teaching_source_boundary", "citation_discipline_primer", "en_dis_carbon_disulfide_bisulfide", "en_dis_sulfate_sulfite", "en_dis_sulfide_sulfite", "en_dis_thiosulfate_sulfite", "en_gov_claim_registry_explainer", "en_gov_hreflang_policy", "en_gov_ontology_governance", "en_index_disambiguation_map", "en_index_multilingual_map", "en_index_terminology_spine", "de_glossary", "de_what_is_bisulfid", "de_bisulfide_hydrosulfide_sulfide", "claus_process_vocabulary", "contact_process_vocabulary", "economic_document_language_sulfur", "en_compliance_customs_sulfur_lang", "en_compliance_export_doc_lang", "en_compliance_reach_language", "de_bisulfid_vs_bisulfide", "de_bridge_en_de_suffix", "de_bridge_iupac_de", "de_german_english_chemical_terms", "de_home", "de_sulfid_vs_sulfide", "de_core_amines_gas_treat", "de_core_biogenic_lang", "de_core_cas", "de_core_cds", "de_core_cus", "de_core_fes", "de_core_k2s", "de_core_liquid_sulfur", "de_core_mos2", "de_core_na2s", "de_core_oleum"]
```

---

*Sprint 5J — Draft Production Wave 1 Manifest*
