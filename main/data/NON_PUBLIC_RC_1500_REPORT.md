# Non-Public RC 1,500 Report

**Sprint:** 6M-E  
**Date:** 2026-05-31  
**Status:** Complete — 1,500-page non-public RC rendered under quarantine

---

## Why this sprint exists

Sprint **6M-D** proved a **250-page** quarantined non-public release candidate inside the fixed **14,000-page** publication pipeline. Sprint **6M-E** advances directly to a **1,500-page** non-public RC — skipping intermediate **500-page** and **1,000-page** RC stages per strategic decision — to stress-test corpus expansion, batch selection, render throughput, multilingual mix, source-required visibility, and validator scale at a materially larger engineering cohort while preserving all publication locks.

## Why we skipped directly from 250 to 1,500

The **500-page** and **1,000-page** RC stages were planning checkpoints, not mandatory gates. Accelerating to **1,500 pages** validates the same governance contract (quarantine-only output, noindex, no publication) at scale more representative of the path toward **7,500** and **14,000** without relitigating the launch floor or weakening locks.

## Why this is inside the 14,000-page pipeline

Bisulfid.com targets a **minimum 14,000 governed pages** at launch. The 1,500-page RC is an **engineering release candidate** inside that pipeline — proving route expansion, draft generation, deterministic batch render, and validator coverage. It is **not** launch authorization.

## Why this is not a public launch

All **1,500** rendered pages are under `site/_sample/` only, carry **noindex,nofollow**, state **NOT A LAUNCH**, and remain **outside sitemap and navigation**. Zero routes are published; zero routes are indexable.

## Why this is not a reduced publication target

The batch renders **1,500 pages** for pipeline proof only. The **14,000-page minimum launch corpus** objective is unchanged. This is not a 1,500-page launch, pilot site, glossary substitute, or blog.

---

## Corpus count before sprint

| Metric | Before 6M-E |
|--------|-------------|
| Routes | 1,043 |
| Draft-backed | 985 |
| Missing drafts | 58 |
| Published | 0 |
| Indexable | 0 |

## Corpus expansion performed

1. **Missing-draft backfill** — 58 governed drafts for routes already in `routes.json` (EN gateway gaps + DE terminology wave).
2. **COHORT_03 pipeline expansion** — 457 new planned routes with governed non-public drafts (EN terminology fan-out, DE terminology, disambiguation, governance/index pages).
3. **Duplicate-path remediation** — removed overlapping cohort03 paths against COHORT_02 (`sulfur_dioxide`, `sulfur_trioxide` fan-out) and DE lead-sulfide collision; replaced with unique `/en/pipeline-expansion/` terminology routes.

## Route/draft-backed count after sprint

| Metric | After 6M-E |
|--------|------------|
| Routes | **1,500** |
| Draft-backed | **1,500** |
| Missing drafts | **0** |
| Published | **0** |
| Indexable | **0** |

---

## Render results

| Field | Value |
|-------|-------|
| Target | 1,500 |
| Rendered | **1,500** |
| Skipped | **0** |
| Output | `site/_sample/` only |

### Language split (rendered)

| Language | Count |
|----------|-------|
| EN | 1,400 |
| DE | 100 |

### Page-type / route-family distribution (rendered)

| Family | Count |
|--------|-------|
| EN terminology | 1,318 |
| DE terminology | 82 |
| Reference/governance | 52 |
| Disambiguation | 23 |
| Gateway/index/hub | 14 |
| Reference | 10 |
| Acquisition | 1 |

### Source-required coverage

**1,499 / 1,500** pages visibly preserve `[SOURCE REQUIRED]` or equivalent unresolved-source state in rendered HTML. **1** page without visible marker (`home` gateway frame excerpt limitation — documented weakness from 6M-C/6M-D).

---

## Governance posture

- **noindex,nofollow** on all 1,500 RC pages
- **Outside sitemap** and **outside navigation** markers present
- **Not publication-ready** stated on all pages
- **No source approval** or **claim approval** implied
- Publication / indexation / sitemap / navigation locks remain **LOCKED**
- `production_can_safely_proceed: **no**`

---

## What rendered correctly

- Deterministic stratified selection across terminology, disambiguation, governance, gateway, and DE pages
- Template bridge map and publication frame at 1,500-page scale
- Manifest + matrix generation
- All L1/L2 validators and runtimes **PASS**

## What failed or remains weak

- Gateway/home frames may not surface full body `[SOURCE REQUIRED]` in HTML excerpt (1/1,500)
- Markdown rendering remains minimal (stdlib excerpt) — production-grade rendering deferred
- Duplicate-path collision with COHORT_02 required remediation during sprint (resolved)

---

## Blockers before 7,500-page RC

1. Production-grade markdown/content rendering in `build.py`
2. Gateway frame body rendering for full source-required visibility
3. Template registry name migration (if separately chartered)
4. Continued source/claim boundary discipline at 5× scale
5. CI/runtime validation at 7,500-page HTML volume

## Blockers before 14,000-page launch corpus

1. Full draft coverage for remaining launch inventory (~12,500+ pages beyond current 1,500)
2. Source verification and narrow claim approval where chartered
3. Publication lock lift only after explicit launch sprint authorization
4. Sitemap/navigation/indexation gates remain closed until launch charter
5. **14,000-page minimum** remains fixed

## Relationship to future 100,000+ expansion

Batch selection, quarantine contract, template bridge map, and governance markers are **route-count-agnostic**. The same non-public RC discipline scales toward **100,000+** governed pages without relitigating the **14,000-page** launch floor.
