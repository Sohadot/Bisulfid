# Launch Cohort Blueprint Quality Review (Sprint 5B)

## Why this sprint exists

Sprint **5A** produced `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` with **307** proposed page concepts toward a **≥ 300 governed page** first public launch cohort. Sprint **5B** is a **read-only blueprint quality-review sprint**: it evaluates whether those concepts are **strong enough** to serve as the foundation of a **sovereign-grade** first launch corpus—without creating routes, drafts, registry edits, or publication.

## Files reviewed

- `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` (full table, 307 data rows)
- `main/data/SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`
- `main/data/CORPUS_EXPANSION_MODEL.md`
- `main/data/CORPUS_LAUNCH_THRESHOLD.md`
- `main/data/routes.json` (contrast existing planned routes vs blueprint-only rows)
- `main/data/internal_links.json` (link-graph context; unchanged this sprint)
- `doctrine/SOURCE_POLICY.md`
- `DECISION_LOG.md`

## Total proposed concept count

**307** (per blueprint footer; 63 English + 61 German + 61 Arabic + 61 Chinese + 61 Japanese rows in the data table).

## Review methodology

1. **Full pass** of all 307 rows in the blueprint table (route_id, path, language, category, role, source level, risk, eligibility, cluster, priority).
2. **Cross-check** against Sprint 5A architecture: chemical-language thesis, anti-thin / anti-generic posture, multilingual = **controlled terminology records** (not translation spam).
3. **Contrast** EN rows that mirror existing `routes.json` entries vs blueprint-only EN rows vs multilingual mirrors.
4. **Risk triage**: safety-adjacent, industrial document language, high-claim chemistry, and **operational utility** pages (newsletter, acquire).
5. **Classification** applied **per row** under the five buckets in §“Classification summary” using explicit rules (documented in `LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`).

## Quality criteria used

Aligned with `CORPUS_LAUNCH_THRESHOLD.md`, `CORPUS_EXPANSION_MODEL.md`, and `SOVEREIGN_REFERENCE_CORPUS_ARCHITECTURE.md`:

- **Thesis fit:** Concept must clearly serve **chemical-language reference** (terminology, disambiguation, governance, or defensible document/sector **language**—not market, procurement, medical, or operational manuals).
- **Non-thin:** Role implies substance beyond a stub; industrial rows must stay **non-operational** and **non-statistical**.
- **Source realism:** `strict_registry` rows must be plausible to support without stretching `SOURCE_POLICY` categories.
- **Claim realism:** High `claim_risk_level` rows need explicit safety/industry/safety_claim discipline before any public eligibility.
- **Multilingual discipline:** Non-English rows must be **authored as terminology records** with language-appropriate authorities—not English copy pasted with “localized” in the role field.
- **Duplicate / overlap:** Near-duplicate H₂S and MoS₂ concepts collapse into fewer public pages where possible.
- **Internal linking:** Clusters (`terminology_spine`, `de_en_bridge`, `disambiguation`, etc.) are coherent; multilingual mirrors must not create **orphan** clusters before hreflang and hub wiring (`multilingual_corpus_map` remains non-public until wired).

## Classification summary

Every blueprint row was assigned **exactly one** primary disposition. Counts below **sum to 307** (merge guidance is noted separately—it refines rows already counted under **revise** or **keep**, not an extra bucket on top).

| Classification | Row count | Meaning |
| --- | ---: | --- |
| **keep_for_launch_cohort** | 68 | Strong **EN reference** core (minus utility) + **15** priority **DE** hub concepts for the first implementation wave after light QA. |
| **revise_before_launch_cohort** | 46 | EN/DE rows that need **category**, **path**, **risk**, or **role** fixes before they can count toward launch cohort quality (includes industrial/safety neighbors and remaining DE mirrors). |
| **merge_with_related_concept** | — | **Applies to ~35–40 blueprint rows** (H₂S family, MoS₂/WS₂ duplicates, bisulfite governance twins)—execute merges **inside** the keep/revise stream to reduce net public pages. |
| **defer_to_later_corpus_phase** | 183 | All **ar + zh + ja** mirror rows (**61×3**): pursue only after **EN+DE** spine is source-locked and hreflang policy is wired. |
| **reject_as_too_thin_or_generic_for_reference_cohort** | 10 | `newsletter` and `acquire` ×**5** languages: valid **utility** concepts but **excluded from the 300 sovereign reference page** launch cohort definition. |

*See `LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md` for named groupings.*

## Strongest concept groups

- **Core EN terminology & gateway alignment:** `glossary`, `what_is_bisulfid`, `bisulfide_hydrosulfide_sulfide`, `bisulfid_vs_bisulfide`, `sulfid_vs_sulfide`, `german_english_chemical_terms`, `sources`, `home`, gateway trio `what_is_sulfur` / `sulfur_compounds` / `sulfur_uses`.
- **EN methodology & governance:** `corpus_methodology_overview`, `nomenclature_governance_overview`, `translator_playbook_bisulfide_family`, `citation_discipline_primer`, `academic_teaching_source_boundary`, `bisulfite_wall_explainer`.
- **EN terminology expansion (disciplined):** Sulfur family records (`sulfate_terminology`, `sulfite_terminology`, `thiosulfate_terminology`, `elemental`/`allotrope` language, class pages for mercaptan/sulfonic/sulfoxide) **if** kept strictly reference-shaped.
- **Industrial/economic interpretation (EN):** `economic_document_language_sulfur`, `supply_chain_vocabulary_sulfur`, Claus/FGD/contact vocabulary **when** framed as document language only (already stated in roles).
- **German layer (conceptual):** `de_glossary`, `de_what_is_bisulfid`, `de_bisulfide_hydrosulfide_sulfide`, `de_bisulfid_vs_bisulfide`, `de_sulfid_vs_sulfide`, `de_german_english_chemical_terms`, `de_home`—**provided** paths and categories are corrected to match DE-first naming conventions in a future routing sprint.

## Weak or risky concept groups

- **Operational utility in a reference cohort:** `newsletter`, `acquire` (all languages)—risk **diluting** the “300 governed **reference** pages” standard.
- **H₂S / safety cluster density:** `hydrogen_sulfide_risk`, `hydrogen_sulfide_term_record`, `de_term_hydrogen_sulfide`, `*_core_h2s_aware`, and related rows—**duplicate narrative risk** and **safety-manual drift** if not merged and tightly bounded.
- **MoS₂ / WS₂ duplication:** `molybdenum_disulfide` vs `*_core_mos2` and `tungsten_disulfide_terms` vs `*_core_ws2` propose **two paths** per language for the same material focus.
- **Multilingual “localized” phrasing:** ~200 rows reuse English URL slugs and the word **localized**—**high translation-spam risk** if implemented as bulk MT without per-language authority plans.
- **Category mismatches (example):** `de_industrial_sulfur_systems` labeled `core_terminology` while EN is `industrial_economic_interpretation`—undermines governance tracking.
- **`de_sources` risk flag:** `claim_risk_level: high` while EN `sources` is low/governance_meta—likely **blueprint inconsistency**; sources face is sensitive but not automatically “high claim risk” in the same sense as H₂S operational pages.
- **P3 breadth:** `frasch_process_vocabulary`, esoteric sulfide mineral pages—easy to write as **thin encyclopedia** unless tightly scoped as **naming/terminology** only.

## Duplicate or merge candidates

| Merge theme | Example route_id families | Intent |
| --- | --- | --- |

| H₂S terminology vs safety context | `hydrogen_sulfide_term_record` + `hydrogen_sulfide_risk` + `*_term_hydrogen_sulfide` + `*_core_h2s_aware` | One **identity/disambiguation** record + one **non-manual safety context** per language max; cross-link instead of four pages. |
| MoS₂ | `molybdenum_disulfide` vs `*_core_mos2` | Single canonical **material terminology** page per language. |
| WS₂ | `tungsten_disulfide_terms` vs `*_core_ws2` | Same. |
| Bisulfite boundary | `bisulfite_wall_explainer` vs `*_dis_bisulfite_wall` | Keep EN authoritative first; others as **controlled translations** after EN lock. |
| Nomenclature governance | `nomenclature_governance_overview` vs `*_gov_nomenclature` | EN first; multilingual follows doctrine. |

## Multilingual quality assessment

- **Numerical balance:** Even 61-row blocks per **de / ar / zh / ja** create **false parity**: German should lead non-English per architecture; Arabic/Chinese/Japanese should **trail** EN+DE source-locking, not ship in parallel at full breadth.
- **URL policy:** Using English slugs under `/de/`, `/ar/`, etc. may conflict with future **locale-appropriate** paths in `MULTILINGUAL_POLICY.md`—needs **revision before routing**.
- **Translation spam risk:** **High** if teams interpret “localized” rows as “translate EN paragraph-by-paragraph.” Mitigation: **controlled terminology record** template, minimum section schema, per-batch editor sign-off (per 5A expansion model).

## Source-risk assessment

- **Lower risk (still non-trivial):** Pure terminology with dictionary / IUPAC / PubChem-class support (when registered).
- **Elevated risk:** Industrial filing / HS-code language pages—must never absorb **market statistics**; must cite **documentary** or **classification** sources only.
- **High risk:** Safety-context and substance-industrial pages (`sodium_bisulfide`, `sour_gas_document_language`, H₂S cluster)—**regulatory** and **high-liability** vocabulary; requires dedicated review tracks before public eligibility.

## Claim-risk assessment

- Blueprint marks many rows `eligible_after_full_source_lock` while **claim registries are inactive** (`routes.json` / doctrine unchanged): **accurate**—publication remains impossible until claim workflow activates.
- High-risk rows must assume **`safety_claims`**, **`industry_claims`**, and **`terminology_claims`** intersections; multilingual mirrors **multiply** approval burden.

## Internal-linking readiness assessment

- English clusters (`terminology_spine`, `de_en_bridge`, `disambiguation`) are **conceptually sound**.
- Multilingual clusters (`multilingual_*`) are **not ready** until `internal_links.json` and hreflang wiring exist; `multilingual_corpus_map` is correctly flagged **non-public until hreflang wiring**.

## Is the 307-concept blueprint launch-cohort-ready?

**No—not as-is.** The blueprint is a strong **quantity scaffold** and encodes the right **thesis-shaped** mix on the English side, but it requires:

1. **Separation of reference vs utility** pages for the **300 reference page** threshold.
2. **Merge and de-duplication** of H₂S and disulfide material concepts.
3. **Revision** of multilingual rows (paths, categories, risk flags, “localized” roles) before any routing sprint.
4. **Phased multilingual rollout**: DE next after EN spine; AR/ZH/JA largely **deferred** for first launch cohort unless paired with native-language authority plans.

## What must be fixed before routes are added

See **`LAUNCH_COHORT_REFINEMENT_RECOMMENDATIONS.md`** for actionable lists. In summary: fix category/risk inconsistencies, merge duplicates, reclassify utility pages, localize URL strategy per language, and produce a **numbered** launch-cohort subset whose rows each pass anti-thin review.

## Why no routes were created

Sprint 5B is **review-only**; routing remains blocked until blueprint refinement and a dedicated **route registration** sprint.

## Why no content pages were created

Drafting is out of scope; **source and claim posture** is not yet launch-ready.

## Why no claims were approved

Claim registries remain **inactive** per project state; this sprint does not activate workflows.

## Publication readiness conclusion

**Not ready for publication.** This sprint produces **governance reports only**—no output that could be indexed or served publicly.

## Recommended next sprint

**Sprint 5C (recommended):** **Blueprint refinement**—produce an updated `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` (or a v2 cohort table) with merged rows, corrected categories/risks, explicit “reference cohort” vs “utility cohort” tagging, and phased multilingual scope; *or* a **narrow English-only route registration sprint** if the owner prefers implementation first—but only against a **refined** minimum cohort list.

---

*Sprint 5B — review documentation only. No registry or content edits.*
