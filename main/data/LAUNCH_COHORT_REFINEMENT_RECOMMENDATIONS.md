# Launch Cohort Refinement Recommendations (Sprint 5B)

## Purpose

This document translates `LAUNCH_COHORT_BLUEPRINT_QUALITY_REVIEW.md` into **actionable refinement lists** for the **307** proposed concepts. It does **not** register routes or edit `routes.json`.

## Concepts to **keep** (first sovereign reference wave — English + selected German)

Treat as **keep_for_launch_cohort** after normal routing QA (may still be non-public until source-locked):

**English — existing-route-aligned (21 rows; minus utility for reference cohort):**  
`home`, `what_is_sulfur`, `sulfur_compounds`, `sulfur_uses`, `what_is_bisulfid`, `bisulfid_vs_bisulfide`, `sulfid_vs_sulfide`, `bisulfide_hydrosulfide_sulfide`, `sodium_bisulfide`, `disulfide_bonds`, `industrial_sulfur_systems`, `sulfur_safety_context`, `hydrogen_sulfide_risk`, `sds_and_sulfur_terms`, `protein_disulfide_structure`, `molybdenum_disulfide`, `german_english_chemical_terms`, `glossary`, `sources`

`newsletter` and `acquire` (**EN only in `routes.json` today; mirrored in blueprint**) remain **valid routes** for product/strategy but are **excluded from the 300 sovereign reference page** count—see **reject** section.

**English — blueprint-only reference (recommended keep):**  
`bisulfid`, `sulfid`, `hydrosulfide` *(pending future `routes.json` registration per Sprint 4L doctrine)*,  
`corpus_methodology_overview`, `nomenclature_governance_overview`, `translator_playbook_bisulfide_family`, `citation_discipline_primer`, `academic_teaching_source_boundary`, `bisulfite_wall_explainer`,  
`sulfur_element_term_record`, `sulfide_anion_term_record`,  
`sulfate_terminology`, `sulfite_terminology`, `thiosulfate_terminology`, `polysulfide_terminology`, `sulfane_chain_language`,  
`carbon_disulfide_terms`, `carbonyl_sulfide_terms`, `mercaptan_class_language`, `sulfonic_acid_class_language`, `sulfoxide_sulfone_language`,  
`economic_document_language_sulfur`, `supply_chain_vocabulary_sulfur`,  
`claus_process_vocabulary`, `contact_process_vocabulary`, `fgd_document_language`, `hydrotreating_desulfurization_terms`,  
`sodium_sulfide_salts_language`, `iron_sulfides_mineral_language`, `copper_sulfides_language`, `zinc_lead_sulfides_language`,  
`arsenic_antimony_sulfides_language`, `tungsten_disulfide_terms`, `tin_sulfides_terms`, `silver_gold_sulfides_terms`

**English — keep but often non-public early:**  
`multilingual_corpus_map`, `quality_gate_public_explainer`, `ontology_alignment_primer`, `internal_linking_discipline`, `corpus_methodology_overview` *(already governance_meta / signoff-gated)*

**German — priority keep (first non-English wave):**  
`de_home`, `de_what_is_bisulfid`, `de_bisulfide_hydrosulfide_sulfide`, `de_glossary`, `de_bisulfid_vs_bisulfide`, `de_sulfid_vs_sulfide`, `de_german_english_chemical_terms`, `de_what_is_sulfur`, `de_sulfur_compounds`, `de_sulfur_uses`, `de_dis_bisulfite_wall`, `de_gov_nomenclature`, `de_method_corpus_map`, `de_method_translator_playbook`

---

## Concepts to **revise**

| Issue | Affected concepts (examples) | Required fix |
| --- | --- | --- |
| Category mismatch EN vs DE | `de_industrial_sulfur_systems` vs `industrial_sulfur_systems` | Align `corpus_category` with EN **industrial_economic_interpretation** unless intentionally narrower. |
| Inconsistent risk on sources | `de_sources` / `ar_sources` / `zh_sources` / `ja_sources` marked `high` | Re-score: “sources” pages are **governance** surfaces—risk should reflect **factual claims** inside, not automatic high. |
| Translation-spam-prone roles | Most `*_term_*`, `*_core_*` rows: “…localized” | Replace with **controlled terminology record** language; add minimum outline requirement in routing sprint. |
| English slug paths for all locales | All non-EN `/de/what-is-bisulfid/` etc. | Plan **locale-native** paths per `doctrine/MULTILINGUAL_POLICY.md` before `routes.json`. |
| Gateway `strict_registry` | `de_home`, `ar_home`, `zh_home`, `ja_home` | Gateways may mix governance_meta + strict_registry by section; split or clarify in routing spec. |

---

## Concepts to **merge**

| Keep canonical (conceptual) | Merge away / redirect planning |
| --- | --- |
| `hydrogen_sulfide_risk` (safety context) | `hydrogen_sulfide_term_record`; `*_term_hydrogen_sulfide`; `*_core_h2s_aware` → cross-link or fold into one terminology + one safety max per language |
| `molybdenum_disulfide` | `*_core_mos2` |
| `tungsten_disulfide_terms` | `*_core_ws2` |
| `bisulfite_wall_explainer` | Duplicate **authority** with `*_dis_bisulfite_wall` once EN is source-locked |
| `nomenclature_governance_overview` | `*_gov_nomenclature` as dependent translations |

---

## Concepts to **defer**

- **All** `ar_*`, `zh_*`, `ja_*` rows **except** optional **single** `*_home` / `*_glossary` / `*_what_is_bisulfid` stubs—until **EN + DE** spine pages are source-locked and hreflang policy is wired.
- **P3** English breadth: `frasch_process_vocabulary`, marginal mineral sulfide pages—defer until core sulfur/terminology spine is dense.
- **Duplicate industrial twins** after merge analysis completes.

---

## Concepts to **reject** (for the **300 sovereign reference page** launch cohort count)

These may still exist as **planned routes** for product/strategy reasons but **must not** be treated as part of the **300 governed chemical-language reference pages**:

- `newsletter`, `acquire` — **each language** (`en`, `de`, `ar`, `zh`, `ja`) → **10 rows total** excluded from reference cohort accounting.

*Alternative:* define a separate **`utility_cohort`** cap in `CORPUS_LAUNCH_THRESHOLD.md` in a future sprint (out of scope for 5B implementation).

---

## Recommended first route-implementation batch (after refinement)

**Scope:** **English-only** or **English + narrow German hub**—no AR/ZH/JA implementation until refinement pass closes.

**Recommended page-count target:** **40–55** `route_id` registrations + `content_file` bodies in the **first implementation batch** (well under 300 intentionally): enough to complete the **EN terminology spine**, **disambiguation**, and **governance** skeleton without triggering thin-page mass production.

**Suggested EN priority bands:**

1. **P0–P1 reference:** `glossary`, `what_is_bisulfid`, `bisulfide_hydrosulfide_sulfide`, `german_english_chemical_terms`, `sources`, `bisulfid_vs_bisulfide`, `sulfid_vs_sulfide`, gateway trio, `bisulfite_wall_explainer`, `nomenclature_governance_overview`.  
2. **P1 terminology expansion:** sulfate/sulfite/thiosulfate/polysulfide/sulfane family pages.  
3. **P2 industrial language:** Claus/FGD/economic document language—only after band 1 draft quality is proven.

---

## Source governance notes

- No blueprint row may remove the rule: **no published factual claim without `source_registry.json` support** (`SOURCE_POLICY.md`).
- Multilingual pages need **language-appropriate** authority—not English-only citations “translated.”
- Teaching references remain **candidate-only** for formal normative claims.

## Claim governance notes

- Registries stay **inactive** until an explicit activation sprint; high-risk pages should list **`required_claim_groups`** explicitly when routes are registered.
- Merging H₂S-related concepts **reduces** duplicate pending claims.

## Multilingual governance notes

- **Phase 1:** EN  
- **Phase 2:** DE (identity layer)  
- **Phase 3:** AR / ZH / JA in **batched vertical slices** with native-language editor review  
- Forbid **MT-only** public pages; cap batch size per `CORPUS_EXPANSION_MODEL.md`.

## Anti-thin-content recommendations

- Minimum sections per terminology record: scope, boundaries, **what this page does not claim**, source posture, related terms, internal links.
- Ban list-only pages without definitional prose in public tier.

## Anti-generic-content recommendations

- Ban undifferentiated “explainer blog” tone; tie every page to **Bisulfid thesis**: German–English chemical language, bisulfide/sulfide family, or documented governance scope.

## Recommended Sprint 5C direction

1. **Option A — Refinement sprint:** Publish `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT_v2.md` (or supersede table) with merged IDs, fixed categories, phased multilingual scope, and explicit **reference_cohort** boolean column.  
2. **Option B — Implementation sprint (narrow):** Register **≤55** EN routes from refined list + draft non-public bodies—**only** if refinement output is accepted first.

---

*Sprint 5B — recommendations only; no repository mutation beyond strategy Markdown + decision log.*
