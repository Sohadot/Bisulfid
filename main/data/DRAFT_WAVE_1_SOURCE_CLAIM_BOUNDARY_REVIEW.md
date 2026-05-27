# Draft Wave 1 — Source and Claim Boundary Review

**Sprint:** 5L  
**Date:** 2026-05-27  
**Branch:** `claude/sprint-5l-draft-wave-1-source-claim-boundary-review`

---

## Why this sprint exists

Sprint **5J** created **50** standardized non-public drafts. Sprint **5K** established the **L1 corpus automation runtime** and documented pre-existing governance debt as warnings, not auto-fixes. Before another **40–60** draft wave (Sprint 5M+), the corpus must classify **source-locking requirements**, **claim-risk posture**, and **publication blockers** for every Sprint 5J draft so governance debt does not compound toward the **500-page sovereign launch threshold**.

This sprint is **review and classification only**. No content, routes, registries, or markers were modified.

---

## Why source/claim boundary review must happen before draft wave 2

| Risk if skipped | Consequence |
| --- | --- |
| Unmapped `[SOURCE REQUIRED]` markers | Implied authority without registry support |
| Unclassified claim risk | Industrial/compliance drafts drift toward forbidden frames |
| Draft wave 2 before boundaries | **100+** drafts with unresolved source/claim debt |
| Publication pressure at scale | Quality Gate bypass attempts as route count grows |

Sprint **5K** recommended **5L before 5M**. This review executes that recommendation.

---

## Relationship to Sprint 5J

Sprint **5J** produced **50** non-public Markdown drafts at exact `routes.json` `content_file` paths for Sprint **5I-B** routes. All targets use Sprint 5J frontmatter template, non-public notices, publication blockers sections, and `[SOURCE REQUIRED]` markers on authority-sensitive lines. This sprint **reads** those drafts; it does **not** edit them.

---

## Relationship to Sprint 5K automation runtime

Pre-flight validation: `python scripts/corpus_validation_runtime_l1.py` — **PASS** (2026-05-27).

L1 confirms structural discipline on wave-1 strict targets. Sprint 5L adds **governance classification** that L1 does not automate: source category need, claim-risk tier, publication blocker taxonomy, and readiness for future source-mapping / claim-boundary registration sprints.

---

## Relationship to 500-page sovereign launch threshold

| Metric | Value |
| --- | ---: |
| Launch threshold | **500** governed pages |
| Routes registered | **126** |
| Draft-backed routes | **68** |
| Sprint 5J drafts reviewed | **50** |
| Publication-ready drafts | **0** |

No draft from wave 1 is publication-ready. All remain blocked by planned route status, unresolved markers, inactive registries, and missing internal-link wiring.

---

## Files reviewed

- `main/data/routes.json`
- `main/data/DRAFT_PRODUCTION_WAVE_1_MANIFEST.md`
- `main/data/DRAFT_PRODUCTION_WAVE_1_REPORT.md`
- `main/data/CONTENT_DRAFTS_L0_VALIDATION_REPORT.md`
- `main/data/CORPUS_L1_VALIDATION_REPORT.md`
- `main/data/CORPUS_AUTOMATION_NEXT_WAVE_RECOMMENDATIONS.md`
- `main/data/CORPUS_AUTOMATION_VALIDATION_REQUIREMENTS.md`
- `main/data/CORPUS_LAUNCH_THRESHOLD.md`
- `main/data/FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md`
- `main/data/CORPUS_PRODUCTION_WAVE_MODEL.md`
- All **50** Sprint 5J draft content files (read-only)

---

## Pre-flight confirmation

| Check | Result |
| --- | --- |
| Wave-1 target count | **50** route_ids from manifest JSON |
| Draft files exist on disk | **50/50** |
| Matching `route_id` in `routes.json` | **50/50** |
| Frontmatter `status: draft` | **50/50** |
| `publication_status: non_public` | **50/50** |
| `indexable: false` / `in_sitemap: false` | **50/50** |
| L1 runtime | **PASS** |
| Content pages modified | **0** |
| `[SOURCE REQUIRED]` markers removed | **0** |
| Claims approved | **0** |

---

## Review scope

| Dimension | Value |
| --- | ---: |
| Drafts reviewed | **50** |
| English (`en`) | **30** |
| German (`de`) | **20** |

### Route categories reviewed (by layer)

| Category | Count |
| --- | ---: |
| Core terminology | 22 |
| Disambiguation authority | 6 |
| Source / governance utility | 5 |
| DE/EN chemical language bridge | 5 |
| Industrial document language | 3 |
| Compliance document language | 3 |
| Index / map | 3 |
| Methodology reference | 2 |
| DE gateway | 1 |

---

## Methodology

1. Load wave-1 target list from `DRAFT_PRODUCTION_WAVE_1_MANIFEST.md` JSON block.
2. Cross-check each target against `routes.json` registry fields (`layer`, `risk_level`, `required_claim_groups`, `source_required`).
3. Read each draft frontmatter and body (read-only) for marker count, non-public posture, and boundary-sensitive framing.
4. Classify each draft across source requirement level, claim risk level, publication blocker type, and readiness (see matrices).
5. Group findings into safest / medium-risk / blocked-deferred cohorts.
6. Run L1 runtime as structural pre-flight; do not modify validators or drafts.

---

## Source boundary principles

- **Doctrine-only pages** may remain on internal policy references until publication planning; no external source registry rows required yet.
- **Terminology and nomenclature pages** require formal or dictionary-tier authority candidates before markers can be satisfied.
- **Multilingual bridge pages** require bilingual authority discipline separate from EN spine source-locking.
- **Industrial and compliance document-language pages** require sector/regulatory **language** references—not operational, legal, or market claims.
- **No source registry modification** in this sprint; classification only.
- **`[SOURCE REQUIRED]` markers remain** on all authority-sensitive lines.

---

## Claim boundary principles

- Claim registries remain **inactive**; **claim approval allowed now: always no**.
- **Low doctrine claims** — governance explainers and index maps; must not imply live systems.
- **Terminology claims** — candidate support language only; `terminology_claims` dependency when registry activates.
- **Document-language claims** — industrial/compliance vocabulary; `industry_claims` / `market_claims` boundaries enforced.
- **High-risk frames blocked** — safety handling, medical, procurement, market data, production/trade statistics.
- **CS2 and economic-document routes** — elevated drift risk; blocked from publication until reframe and source lock.

---

## Publication blocker principles

Every wave-1 draft carries **publication eligibility: not ready**. Common blockers:

| Blocker | Drafts affected (approx.) |
| --- | ---: |
| Unresolved `[SOURCE REQUIRED]` markers | 12 |
| Missing claim boundary registration | 9 |
| Safety / market drift risk | 8 |
| Multilingual governance needed | 6 |
| Formal nomenclature authority needed | 4 |
| Route still `planned` | all 50 |
| Internal links not wired | index maps + all (pre-wiring) |

---

## Overall findings

| Finding | Detail |
| --- | --- |
| Drafts publication-ready | **0** |
| Ready for source-mapping sprint (next) | **12** |
| Needs claim boundary review first | **20** |
| Needs formal authority before progress | **6** |
| Defer until later corpus phase | **5** |
| Blocked from publication (reframe required) | **3** |
| Doctrine-only (structure hardening only) | **4** |
| Source mapping can begin in next wave (subset) | **40** candidates; **12** lowest risk first |

All **50** drafts retain correct non-public posture. No draft implies claim approval or complete source-locking.

---

## Safest draft groups (source-mapping cohort A — 12 drafts)

Lowest claim risk; terminology dictionary or doctrine-adjacent; suitable for **first source-mapping batch (10–15 pages)** after claim boundary notes:

`sulfid`, `sulfur_element_term_record`, `carbonyl_sulfide_terms`, `copper_sulfides_language`, `de_glossary`, `de_bridge_en_de_suffix`, `de_german_english_chemical_terms`, `de_core_biogenic_lang`, `de_core_cas`, `de_core_cus`, `de_core_fes`, `de_core_mos2`

---

## Medium-risk draft groups (claim boundary before source lock — 20+ drafts)

Disambiguation boundaries, multilingual bridges, industrial/compliance document-language, medium terminology records:

Includes all **6** EN disambiguation routes, **5** DE bridge routes, **3** compliance routes, **3** industrial vocabulary routes, core EN terminology (`bisulfid`, `hydrosulfide`, etc.), and selected DE core records (`de_core_cds`, `de_core_k2s`, `de_core_na2s`, `de_core_oleum`, `de_core_liquid_sulfur`, `de_core_amines_gas_treat`).

**Action:** Claim boundary registration sprint (report-only) before source-mapping.

---

## Blocked or deferred draft groups

### Blocked from publication (3)

`carbon_disulfide_terms`, `en_dis_carbon_disulfide_bisulfide`, `economic_document_language_sulfur`

CS2 substance attention and economic filing language carry **high scientific** or **high market/procurement** drift risk. Require reframe confirmation and dedicated source-lock planning before any mapping.

### Deferred until later corpus phase (5)

`en_gov_hreflang_policy`, `en_index_disambiguation_map`, `en_index_multilingual_map`, `en_index_terminology_spine`, `de_home`

Index maps and multilingual gateway depend on spine completeness and hreflang governance not yet active.

---

## Whether any draft is publication-ready

**No.** All **50** drafts remain `non_public` with unresolved markers, inactive registries, unwired internal links, and `planned` route status. **Zero** drafts meet Quality Gate, source-lock, claim, or 500-page threshold requirements.

---

## Why no claims were approved

Claim registries are **inactive** by governance charter. Sprint 5L is classification only. Approving claims would violate Sprint boundaries and `CORPUS_AUTOMATION_CONTROL_LAYER.md` automation anti-rules.

---

## Why no source entries were modified

`source_registry.json` remains inactive. Source-mapping is a **future sprint** (5M recommended). This sprint produces requirement matrices only.

---

## Why no content pages were modified

Editing drafts would blur review vs production. Marker removal or satisfaction is explicitly forbidden until a dedicated source-locking sprint with human authorization.

---

## Why `[SOURCE REQUIRED]` markers remain

Markers indicate **unresolved authority lines**. Satisfying them requires registered sources and human review—not automation or boundary review sprints.

---

## Why no routes were published

Publication requires 500-page program authorization, active source/claim gates, and Quality Gate signoff. All **126** routes remain `planned`, non-indexable, out of sitemap and navigation.

---

## Unresolved governance debt

| Debt | Scope | Owner sprint |
| --- | --- | --- |
| Legacy pre-5J draft structure | 18 drafts (L1 warnings) | Future normalization sprint |
| Safety-route metadata keywords | 4 routes (L1 warnings) | Route metadata review |
| `[SOURCE REQUIRED]` satisfaction language | 2 legacy drafts | Editorial review |
| Wave-1 marker resolution | 50 drafts | Source-mapping waves |
| Claim boundary registration | 40+ drafts | Claim boundary sprint |
| Internal link wiring | 68 draft-backed routes | Link wiring wave |

---

## Deliverables

| Artifact | Purpose |
| --- | --- |
| `DRAFT_WAVE_1_SOURCE_REQUIREMENT_MATRIX.md` | Per-draft source requirement classification |
| `DRAFT_WAVE_1_CLAIM_RISK_MATRIX.md` | Per-draft claim risk classification |
| `DRAFT_WAVE_1_PUBLICATION_BLOCKER_MATRIX.md` | Per-draft publication blocker classification |
| `DRAFT_WAVE_1_NEXT_ACTIONS.md` | Recommended sprint order and batch sizes |

---

## Recommended next sprint

**Sprint 5M — Source mapping wave 1** for the **12** lowest-risk terminology drafts (cohort A), paired with **claim boundary registration report** for the **20** medium-risk drafts. **Defer draft production wave 2** until source-mapping batch 1 completes and L1 passes.

See `DRAFT_WAVE_1_NEXT_ACTIONS.md` for full ordering rationale.

---

*Sprint 5L — Draft Wave 1 Source and Claim Boundary Review*
