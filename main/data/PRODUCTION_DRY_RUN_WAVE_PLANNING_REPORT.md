# Production Dry-Run Wave Planning — Report

**Sprint:** 5O-B  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5o-b-production-dry-run-wave-planning`  
**Status:** Planning-only dry-run — execution not approved

---

## Why this sprint exists

Sprint **5O-B** tests the Corpus Production Automation Layer 2 against a **real planning wave** before any Route Registration Wave 2 execution. Wave 1 registered **126** planned routes; **58** still lack drafts. Registering another 80–120 routes without L2 dry-run discipline would increase registry surface area without proportional draft, source, claim, or link-graph readiness.

This sprint **prepares** a disciplined candidate set, validates it against sovereign launch doctrine, and documents why execution must wait — without modifying `routes.json`, content, or registries.

---

## Why L2 dry-run planning comes before Route Registration Wave 2 execution

Sprint **5O-A** established read-only L2 planners and validators for wave control, gates, link graph, SEO/indexation, and multilingual discipline. A dry-run wave proves those tools against a concrete candidate cohort **before** registry mutation:

1. Candidate eligibility can be scored against blueprint, risk, and language policy.
2. Source/claim gate requirements can be mapped per candidate without creating content obligations.
3. Link-graph and indexation locks can be verified as still **LOCKED** after planning.
4. Human reviewers receive a manifest, matrix, risk review, and blocker list — not an implicit execution approval.

Route registration execution remains a **separate sprint** with explicit gate clearance.

---

## Relationship to Sprint 5O-A

| 5O-A deliverable | 5O-B use |
| --- | --- |
| `corpus_production_planner_l2.py` | Pre-flight and validation — confirms locks and `production_can_safely_proceed: no` |
| `corpus_production_runtime_l2.py` | Orchestration PASS required before and after dry-run documentation |
| Wave control / gate / link / SEO / multilingual models | Selection and exclusion methodology for Wave 2 candidates |
| L2 validation report pattern | Extended in `PRODUCTION_DRY_RUN_VALIDATION_REPORT.md` |

5O-A built the automation layer; 5O-B applies it to **Route Registration Wave 2 planning** without executing registration.

---

## Relationship to the 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Minimum launch threshold | **500** governed pages |
| Current registered routes | **126** |
| Dry-run Wave 2 candidates (not registered) | **83** |
| Hypothetical total if wave executed later | **209** |
| Remaining toward 500 after hypothetical wave | **291** |

Dry-run candidates are chosen to **strengthen launch architecture** (terminology spine, DE/EN bridge, disambiguation, governance, index maps) without treating route count as authority. The **500-page threshold** still requires draft production, source lock, claim governance, and publication gates — not registry inflation alone.

---

## Relationship to source/claim guardrails

- `source_registry.json` remains **inactive** (0 verified entries).
- All claim registries remain **inactive**; **0** approved claims.
- Dry-run candidates requiring `strict_registry` source class are flagged **source gate required: yes**.
- Terminology and disambiguation rows are flagged **claim gate required: yes**.
- No `[SOURCE REQUIRED]` markers were removed; no sources or claims were added or approved.

Wave 2 registration execution must not proceed until 5N-G / claim-boundary work clears named candidates for priority drafts.

---

## Relationship to future 1,000+ / 3,000+ / massive corpus scale

L2 dry-run planning establishes repeatable wave discipline for sovereign-scale growth:

- **English/German-first** spine before ar/zh/ja mass expansion (deferred in this dry-run).
- **Category quotas** prevent thin generic chemistry surfaces at scale.
- **Per-candidate gate flags** scale to larger waves without bypassing source/claim authority.
- **Link-graph and indexation locks** prevent SEO leakage during multi-thousand-page build-out.

Each future wave should follow the same prepare → validate → gate-clear → execute pattern established here.

---

## Files reviewed

- `main/data/CORPUS_PRODUCTION_AUTOMATION_LAYER_2_REPORT.md`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_SCRIPT_REGISTRY.md`
- `main/data/CORPUS_PRODUCTION_WAVE_CONTROL_MODEL.md`
- `main/data/CORPUS_PRODUCTION_GATE_MODEL.md`
- `main/data/CORPUS_PRODUCTION_LINK_GRAPH_MODEL.md`
- `main/data/CORPUS_PRODUCTION_SEO_INDEXATION_MODEL.md`
- `main/data/CORPUS_PRODUCTION_MULTILINGUAL_MODEL.md`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_VALIDATION_REPORT.md`
- `main/data/CORPUS_PRODUCTION_AUTOMATION_NEXT_ACTIONS.md`
- `main/data/FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`
- `main/data/CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`
- `main/data/ROUTE_REGISTRATION_WAVE_1_REPORT.md`
- `main/data/DRAFT_PRODUCTION_WAVE_1_REPORT.md`
- `main/data/DRAFT_WAVE_1_SOURCE_CLAIM_BOUNDARY_REVIEW.md`
- `main/data/SOURCE_CLAIM_AUTOMATION_GUARDRAIL_REPORT.md`
- `main/data/SOURCE_REGISTRY_PROPOSAL_READINESS_WAVE_1_REPORT.md`
- `scripts/corpus_production_runtime_l2.py`
- `scripts/corpus_production_planner_l2.py`
- `scripts/corpus_validation_runtime_l1.py`
- `scripts/source_claim_guardrail_runtime_l1.py`
- `main/data/routes.json`
- `main/data/internal_links.json`
- `main/data/sources/source_registry.json`
- `main/data/claims/terminology_claims.json`
- `DECISION_LOG.md`

---

## Current corpus posture (from pre-flight)

| Metric | Value |
| --- | ---: |
| Current route count | **126** |
| Draft-backed routes | **68** |
| Missing drafts | **58** |
| Published routes | **0** |
| Indexable routes | **0** |
| Routes in sitemap | **0** |
| Routes in navigation | **0** |

| Lock | Status |
| --- | --- |
| Route publication lock | **LOCKED** (all `planned`) |
| Indexation lock | **LOCKED** |
| Sitemap lock | **LOCKED** |
| Navigation lock | **LOCKED** |
| Source registry | **inactive** |
| Claim registries | **inactive** |
| `production_can_safely_proceed` | **no** |

---

## Dry-run candidate summary

| Metric | Value |
| --- | ---: |
| Target future wave size | **80–120** (preferred **100**) |
| Actual dry-run candidate count | **83** |
| Rationale for &lt;100 | Blueprint rows not already in `routes.json` that pass EN/DE-first, low-risk, non-safety, non-deferred eligibility filters exhaust at **83** safely eligible candidates; remaining unregistered blueprint rows are utility/acquisition, safety, ar/zh/ja, or high-risk deferred |

### Language split

| Language | Candidates |
| --- | ---: |
| `en` | **72** |
| `de` | **11** |

### Category split (blueprint corpus_category)

| Category | Count |
| --- | ---: |
| `core_terminology` | **62** |
| `industrial_economic_interpretation` | **9** |
| `index_map` | **5** |
| `disambiguation_authority` | **2** |
| `methodology_reference` | **2** |
| `source_governance` | **2** |
| `documentation_compliance` | **1** |

### Production category split (dry-run classification)

| Production category | Count |
| --- | ---: |
| `core_terminology` | **62** |
| `controlled_industrial_language` | **9** |
| `index_map` | **5** |
| `disambiguation_authority` | **2** |
| `governance_methodology` | **3** |
| `source_claim_governance` | **2** |

### Candidate status split

| Status | Count |
| --- | ---: |
| `dry_run_candidate` | **74** |
| `dry_run_candidate_needs_review` | **9** |

---

## Selection methodology

1. Parsed all **500** blueprint table rows from `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`.
2. Excluded **126** existing `route_id` values in `routes.json` → **373** unregistered blueprint rows.
3. Scored unregistered rows: **English and German first**; low claim risk; core terminology, DE/EN bridge, disambiguation, governance, index maps; controlled industrial document-language when low/medium risk and non-market.
4. **Primary tier** (score ≥35): terminology spine, governance, index maps, low-risk disambiguation.
5. **Secondary tier** (score ≥15, needs review): medium-risk controlled industrial document-language pages only.
6. **Hard exclusions**: ar/zh/ja mass expansion, safety_context, high claim risk, `deferred_high_risk_review`, newsletter/acquire utility routes, procurement/market/medical/handling concepts.
7. Selected top **83** eligible candidates — within **80–120** band, below preferred **100** because safely eligible blueprint inventory is exhausted under current gates.

Full per-row detail: `ROUTE_REGISTRATION_WAVE_2_CANDIDATE_MATRIX.md`.

---

## Exclusion methodology

Deferred or rejected from Wave 2 dry-run (not in candidate matrix):

- **Arabic, Chinese, Japanese** large-scale expansion → `defer_to_later_wave` / `multilingual_later_phase`
- **Safety-heavy** pages (`safety_context`, H2S risk, SDS handling) → `defer_to_later_wave`
- **Procurement, production, trade, market, CAGR, investment, acquisition** pages → excluded
- **Medical or handling-instruction** surfaces → excluded
- **Utility** routes (`newsletter`, `acquire`) → excluded from Wave 2 dry-run
- **High claim risk** and **`deferred_high_risk_review`** blueprint rows → excluded
- Blueprint rows **already in `routes.json`** (Wave 1 cohort) → not candidates

---

## Why no routes were added

Route Registration Wave 2 **execution is not approved**. This sprint is dry-run only. Adding routes would increase the **58-route draft backlog** without draft, source, or claim readiness and would violate the sprint boundary.

---

## Why routes.json was not modified

Registry mutation requires a dedicated execution sprint after blockers clear (`ROUTE_REGISTRATION_WAVE_2_EXECUTION_BLOCKERS.md`). L2 dry-run validates planning discipline without side effects on the live route registry.

---

## Why no content pages were created

Content creation implies source/claim obligations and publication pipeline activation. Wave 2 dry-run identifies **future** registration candidates only; draft production remains blocked until Wave 1 draft backlog and source gates progress.

---

## Why no sources were added

`source_registry.json` remains inactive. Only **1** conditional proposal-readiness candidate (`de_core_mos2`) exists from Sprint 5N-F. Adding sources without 5N-G named candidate intake would bypass human verification doctrine.

---

## Why no claims were approved

Claim registries are inactive by design until source-backed terminology claims pass boundary review. Dry-run planning must not imply claim authority for **83** proposed routes.

---

## Why no routes were published

All **126** routes remain `planned`, non-indexable, out of sitemap and navigation. Publication lock is **LOCKED** per L2 planner. Dry-run does not change publication posture.

---

## How dry-run planning protects quality

### SEO quality

- No routes marked indexable; sitemap and navigation locks verified **LOCKED**.
- Candidates favor governed terminology and reference architecture over thin generic chemistry blog surfaces.
- SEO/indexation model from 5O-A applied before any future indexation decision.

### Internal link integrity

- Index/map and terminology-spine candidates flagged **internal link role required: yes**.
- Dry-run defers registration until link-graph roles are assigned in a future controlled sprint.
- Prevents orphan routes and broken hub/spoke structure at scale.

### Multilingual quality

- EN/DE-first selection; ar/zh/ja deferred to later phase.
- German candidates flagged **multilingual governance required: yes** for hreflang and translation registry discipline.

### Source/claim authority

- Per-candidate source and claim gate flags documented in matrix.
- No `[SOURCE REQUIRED]` markers removed; no registry activation.
- Route count is not treated as authority.

---

## Execution blocker summary

See `ROUTE_REGISTRATION_WAVE_2_EXECUTION_BLOCKERS.md`. Summary:

- **58** missing drafts from Wave 1
- Source registry inactive; 0 verified sources
- 0 approved claims; registries inactive
- Publication/indexation/sitemap/navigation locks **LOCKED**
- `production_can_safely_proceed`: **no**
- **9** dry-run candidates require human review before registration

---

## Recommended next sprint

**Sprint 5N-G** — named source candidate intake (`de_core_mos2` priority).  
**Parallel:** Draft Wave 1 backlog reduction (58 missing drafts) before Draft Wave 2 or Route Registration Wave 2 **execution**.  
**Not recommended now:** Route Registration Wave 2 execution, Draft Wave 2 execution, or registry modification.

Dry-run refinement sprint is **optional** only if blueprint cohort changes; current **83** candidates are documented and validated.

---

## Sprint 5O-B deliverables

| File | Purpose |
| --- | --- |
| `PRODUCTION_DRY_RUN_WAVE_PLANNING_REPORT.md` | This report |
| `ROUTE_REGISTRATION_WAVE_2_DRY_RUN_MANIFEST.md` | Wave manifest and posture |
| `ROUTE_REGISTRATION_WAVE_2_CANDIDATE_MATRIX.md` | Per-candidate matrix (**83** rows) |
| `ROUTE_REGISTRATION_WAVE_2_RISK_REVIEW.md` | Risk analysis |
| `ROUTE_REGISTRATION_WAVE_2_EXECUTION_BLOCKERS.md` | Execution blockers |
| `PRODUCTION_DRY_RUN_VALIDATION_REPORT.md` | Runtime validation |
| `PRODUCTION_DRY_RUN_NEXT_ACTIONS.md` | Next sprint guidance |

**Not modified:** `routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, source/claim registries, content pages, workflows, dependencies, root `README.md`.
