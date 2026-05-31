# Non-Public RC 7,500 Report

**Sprint:** 6M-F  
**Date:** 2026-05-31  
**Status:** Complete — 7,500-page non-public RC rendered under quarantine

---

## Why this sprint exists

Sprint **6M-E** proved a **1,500-page** quarantined non-public release candidate inside the fixed **14,000-page** publication pipeline. Sprint **6M-F** advances directly to a **7,500-page** non-public RC to stress-test governed corpus expansion, deterministic stratified batch selection, render throughput at scale, multilingual mix, source-required visibility, and validator coverage at a cohort materially closer to the launch floor — while preserving all publication locks.

## Why we moved directly from 1,500 to 7,500

Intermediate RC stages (e.g. 2,500 or 5,000 pages) were planning checkpoints, not mandatory gates. Accelerating to **7,500 pages** validates the same governance contract (quarantine-only output, noindex, no publication) at scale more representative of the path toward **14,000** without relitigating the launch floor or weakening locks.

## Why this is inside the 14,000-page pipeline

Bisulfid.com targets a **minimum 14,000 governed pages** at launch. The 7,500-page RC is an **engineering release candidate** inside that pipeline — proving route expansion, draft generation, deterministic batch render, and validator coverage. It is **not** launch authorization.

## Why this is not a public launch

All **7,500** rendered pages are under `site/_sample/` only, carry **noindex,nofollow**, state **NOT A LAUNCH**, and remain **outside sitemap and navigation**. Zero routes are published; zero routes are indexable.

## Why this is not a reduced publication target

The batch renders **7,500 pages** for pipeline proof only. The **14,000-page minimum launch corpus** objective is unchanged. This is not a 7,500-page launch, pilot site, glossary substitute, or blog.

---

## Corpus count before sprint

| Metric | Before 6M-F |
|--------|-------------|
| Routes | 1,500 |
| Draft-backed | 1,500 |
| Missing drafts | 0 |
| Published | 0 |
| Indexable | 0 |

## Corpus expansion performed

1. **COHORT_04 pipeline expansion** — **6,000** new planned routes with governed non-public drafts:
   - **725** EN terminology entities × **8** deterministic variants = **5,800** EN multi-variant routes
   - **200** single routes: **120** DE terminology, **30** disambiguation, **15** governance, **35** gateway/index/hub
2. **Stratified families** — metal sulfide language, organosulfur, inorganic sulfur, industrial controlled language, mineral/geology language, disambiguation prep, DE terminology, governance, and gateway pages
3. **Slug discipline remediation** — four DE cohort04 routes with umlaut route_ids corrected to ASCII slug-safe identifiers (`molybdaen`, `schwefelsaeure`, etc.)

## Route/draft-backed count after sprint

| Metric | After 6M-F |
|--------|------------|
| Routes | **7,500** |
| Draft-backed | **7,500** |
| Missing drafts | **0** |
| Published | **0** |
| Indexable | **0** |

---

## Render results

| Field | Value |
|-------|-------|
| Target | 7,500 |
| Rendered | **7,500** |
| Skipped | **0** |
| Batch ID | `rc_7500` |
| Output | `site/_sample/` only |

### Language split (rendered)

| Language | Count |
|----------|-------|
| EN | 7,258 |
| DE | 242 |

### Page-type / route-family distribution (rendered)

| Family | Count |
|--------|-------|
| EN terminology (COHORT_04 + prior cohorts) | 7,069 |
| DE terminology | 202 |
| Reference/governance | 119 |
| Disambiguation | 55 |
| Gateway/index/hub | 44 |
| Reference (legacy) | 10 |
| Acquisition (legacy) | 1 |

### Source-required coverage

**7,499 / 7,500** pages visibly preserve `[SOURCE REQUIRED]` or equivalent unresolved-source state in rendered HTML. **1** page without visible marker (`home` gateway frame excerpt limitation — documented weakness from 6M-C/6M-D/6M-E).

---

## Governance posture

- **noindex,nofollow** on all 7,500 RC pages
- **Outside sitemap** and **outside navigation** markers present
- **Not publication-ready** stated on all pages
- **No source approval** or **claim approval** implied
- Publication / indexation / sitemap / navigation locks remain **LOCKED**
- `production_can_safely_proceed`: **no**

---

## What rendered correctly

- Deterministic stratified selection across EN/DE terminology, disambiguation, governance, gateway, industrial language, and mineral language families
- Template bridge map and publication frame at 7,500-page scale
- Manifest `batch_id: rc_7500` with 7,500 page records
- Matrix generation (7,500 rows)
- All L1/L2 validators and runtimes **PASS** (after DE slug remediation)

## What failed or remains weak

- Four DE route_ids initially used umlaut characters violating content slug discipline — remediated during sprint
- Gateway/home frames may not surface full body `[SOURCE REQUIRED]` in HTML excerpt (1/7,500)
- Markdown rendering remains minimal (stdlib excerpt) — production-grade rendering deferred
- Render at 7,500 pages takes ~54s on current hardware — acceptable for RC but needs monitoring toward 14,000+

---

## Blockers before 14,000-page launch corpus candidate

1. **~6,500 additional governed routes** and drafts required (7,500 → 14,000)
2. Source/claim boundary audit across full 14,000 inventory
3. Production-grade markdown/content rendering in build engine
4. Template registry migration and gateway full-body rendering (if chartered)
5. Duplicate-path and slug-discipline checks at 14,000 scale
6. Source-required visibility ≥98% with documented exceptions

## Blockers before first public launch sprint

1. Explicit launch authorization in DECISION_LOG
2. `production_can_safely_proceed: yes` only after all locks lifted by charter
3. Sitemap/navigation/indexation policy activation with governance sign-off
4. Source verification and claim approval where required per route class
5. No `[SOURCE REQUIRED]` on publish-eligible pages without documented exception process
6. Public HTML outside quarantine with full Quality Gate pass

## Relationship to future 100,000+ expansion

The 7,500-page RC validates deterministic cohort expansion, stratified fan-out, and quarantined batch render at scale. Architecture must continue to support hundreds of thousands of governed pages — COHORT_04 entity×variant patterns, slug discipline, and validator throughput are stepping stones, not the final corpus shape.
