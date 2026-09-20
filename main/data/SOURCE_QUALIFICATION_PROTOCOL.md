# BISULFID — Source Qualification & Evidence Admission Protocol

**Sprint:** source-qualification-evidence-admission · **Date:** 2026-09-19 · **Status:** ratified-design + minimal schema
**Baseline:** commit `41aeb1f56f` (Semantic Integrity Hardening).
**Read-only w.r.t. legacy/live:** no 14K route, release ledger, ontology, public HTML, sitemap, robots, indexation, source status, or claim status modified. No external source acquired. No relationship instance. No registry activated.

The question is no longer *"is this source credible?"* but *"is this specific source qualified to support this specific evidence assertion for this exact use, domain, claim level, jurisdiction/geography and time scope?"*

---

## 1. Final meaning of `source_lock_status` — **Option B**

`source_lock_status` **remains a bibliographic/source-record stability lock** (its historical Sprint 5N-R meaning: `candidate` → `locked` describes whether the *source record itself* is provisional or frozen). It is **explicitly insufficient** on its own: a locked source is *not* usable for every claim. Admissibility now additionally requires a **source-use qualification** (§2–§4). Historical semantics preserved; not silently redefined; the field is **not modified** this sprint (all 15 remain `candidate`).

Rejected: Option A (leave as-is, ambiguous) and Option C (deprecate now — premature; would rewrite history). If a future migration deprecates it, that will be a separate governed step.

## 2. Four-layer source/evidence model (kept permanently distinct)

1. **Source identity** — what source is this (publisher/title/URL/DOI/dates/edition). Owner: `sources/source_registry.json`.
2. **Source category** — what *kind* of source. **Category never grants admissibility.**
3. **Source-use qualification** — what exact evidence/claims this source is qualified to support, scoped. Owner: `source_use_qualification_registry.json` (new).
4. **Evidence assertion** — the exact observation extracted. Owner: `main/data/evidence/`.

Enforced chain: `source identity → source-use qualification → evidence assertion → claim → knowledge object`.

## 3. Chosen qualification architecture

A **separate** registry, `main/data/source_use_qualification_registry.json`, preserving one-fact-one-owner: a qualification references exactly one `source_id` and **duplicates no bibliographic metadata** (forbidden fields enforced by validator). Qualification belongs neither inside the source record (which owns identity, not use-scope) nor in evidence (which owns a single observation, not the source's whole permitted scope).

## 4. Qualification states

`candidate → reviewed → qualified_narrow → qualified`, with `suspended` and `superseded` as regressions. Each state has entry requirements, owner (source governance), allowed transitions, regression rules, and effect on admission (only `qualified`/`qualified_narrow` admit). **No state authorizes route publication.** Full table in the registry.

## 5. Evidence roles (authority is question-dependent)

`primary_authoritative`, `official_record`, `primary_scientific`, `secondary_scholarly`, `corroborating`, `contextual`, `historical`. No universal "best source": a dictionary is primary for lexical existence; customs data primary for recorded imports; the governing instrument required for current law.

## 6. Ratified source categories

- **Confirmed existing (8):** authoritative_dictionary, chemical_nomenclature_standard, government_scientific_database, regulatory_body, peer_reviewed_journal, industry_publication, market_report, academic_teaching_reference.
- **Newly ratified into policy vocabulary (7):** official_customs_data, official_trade_statistics, national_statistical_authority, intergovernmental_trade_database, official_production_statistics, regulatory_instrument, official_standard — each with a distinct evidentiary role. **Policy vocabulary only** — not written into `source_registry.json` approved categories and no source uses them yet.
- **Evaluated, not ratified:** official_environmental_database, official_health_authority, patent_database, technical_standard (no distinct system need yet / revisit with the relevant domain).

## 7. Domain admissibility (source class/role → evidence)

Machine-readable in `source_admissibility_policy.json`: terminology/linguistics (dictionary/nomenclature, single-authoritative-sufficient); chemistry/materials/physics (primary_scientific or authoritative database/standard; dictionaries forbidden *alone* for concept facts); biology/biomedical (primary literature + authorities, no medical advice); trade/economics (official records required; market/industry contextual-only); regulation/government (governing instrument required for current-law); industry (industry pubs establish scoped observed context, never national totals/current law/sovereign stats/universal performance).

## 8. Evidence sufficiency patterns

`single_authoritative_sufficient`, `primary_plus_corroborating`, `multi_source_synthesis`, `original_instrument_required`, `explicit_source_exclusion`. Model is **claim/evidence class → required evidence pattern**, never "claim → some source exists".

## 9. Deterministic admissibility

`admissible(source, qualification, evidence_context) → (bool, reason)` (`scripts/governance_scaffolding/source_admissibility.py`). Inputs: category, qualification scope, permitted/prohibited use, subject_domain, evidence_kind, claim_level, geography, jurisdiction, temporal_scope, source_version, evidence_role. **Category alone never returns admissible.** Admissibility never implies claim approval, activation, or publication.

## 10. Evidence-review lifecycle (transitions)

`unreviewed → extracted` (faithful extraction + locator) `→ scope_reviewed` (no scope exceedance; correct target level/domain/boundary) `→ evidence_verified` (valid source-use qualification + provenance complete for the source type + no prohibited-use conflict). **`evidence_verified` must NOT imply** claim approval, claim-registry activation, route publication, or indexation.

## 11. Citation-grade locators, temporal/version governance, regression, conflict

Type-specific locators (`evidence_admission_policy.json`) so a serious reader can reconstruct provenance. No universal expiry — per-class revalidation triggers. Regression (`qualified → reviewed/suspended/superseded`, never deleted) moves downstream privilege **equal or lower, never higher**. Conflicting evidence is represented, not resolved by preference (competing records, temporal/jurisdiction splits, contested/unresolved status). Quantitative, legal/regulatory, and scientific admission each carry kind-specific required provenance; scientific scope-inflation is prohibited.

## 12. Claim approval / activation architecture

Four independent layers (`claim_activation_policy.json`): **claim review** → **claim approval** → **registry operational activation** → **route publication**. Finding: registry-wide `inactive/active` is too coarse. **Proposal** (not applied): per-claim operational activation gated on approval + all supporting evidence `evidence_verified` with valid qualification + no prohibited-use conflict; regresses if any support regresses. **Nothing activated this sprint.**

## 13. 15-source audit

Full audit in `SOURCE_REGISTRY_QUALIFICATION_AUDIT.md`. Summary: 14 sources `seeded`/`candidate` → **no qualification granted** (remain pending); 1 source (`SRC-SPEKTRUM-MOS2-DE`, verified) receives **one narrow qualification** (`QUAL-SPEKTRUM-MOS2-DE-001`, `qualified_narrow`) mirroring its already-reviewed German MoS₂ dictionary-entry scope — **broadening nothing**. No `use_for` broadened; no source promoted for reputation.

## 14. MoS₂ proof

`SRC-SPEKTRUM-MOS2-DE` → `QUAL-SPEKTRUM-MOS2-DE-001` (qualified_narrow, terminology/lexeme, de) → `EVD-MOS2-DE-001` (lexeme-level, `scope_reviewed`) → `CLM-TERM-MOS2-DE-001` (approved, registry inactive). `admissible()` returns **True** for the reviewed German dictionary-entry terminology boundary only, and **False** for concept/scientific/economic/publication uses. Source status, lock, claim, activation, route, and release are **unchanged**. `EVD-MOS2-DE-001` stays `scope_reviewed` (not upgraded to `evidence_verified`). **Contract-C derived state remains `(not_public, noindex)`.**

## 15. Unresolved decisions before real evidence acquisition

- Admission rules for the 7 newly-ratified categories into `source_registry.json` (a Source Qualification *acquisition* sprint).
- The scoped per-claim activation mechanism (design only here).
- Whether `source_lock_status` is eventually deprecated (Option C migration).
- Corroboration thresholds for `primary_plus_corroborating`/`multi_source_synthesis` (how many independent records, per domain).
- Biomedical claim-restriction specifics before any biology/biomedical program.
