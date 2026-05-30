# Non-Public Release Candidate Batch 01 Report

**Sprint:** 6M-D  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-6m-d-14k-pipeline-non-public-release-candidate-batch-01`  
**Render command:** `python scripts/build.py --render-quarantined-rc-batch --limit 250`

---

## Why this sprint exists

Sprint **6M-C** proved the publication frame with an **8-page** quarantined QA sample. Sprint **6M-D** expands that proof to a **larger deterministic non-public release candidate batch** inside the fixed **14,000-page** publication pipeline — validating that the hardened build engine and template layer can render a broader governed corpus slice before scaling toward full launch preparation.

---

## Why RC Batch 01 follows the 8-page quarantined QA render

The 8-page sample validated frame composition, template bridging, and governance markers across gateway, terminology, disambiguation, and governance routes. RC Batch 01 stress-tests **batch selection**, **render throughput**, **multilingual mix**, **source-required visibility at scale**, and **validator coverage** across 250 pages — still quarantined, still non-public.

---

## Why this batch is inside the 14,000-page execution pipeline

Bisulfid.com targets a **minimum 14,000 governed pages** at launch. RC Batch 01 is an **engineering release candidate** step — not launch authorization — proving the render pipeline can process a meaningful cohort of the current **1,043 planned routes** (985 draft-backed) without weakening publication locks.

---

## Why this is not a public launch

- 0 published routes; all publication/indexation/sitemap/navigation locks **LOCKED**
- `production_can_safely_proceed: no`
- All output under `site/_sample/` only
- Every page: `noindex, nofollow`, not publication-ready, NOT A LAUNCH
- No sitemap or navigation output

---

## Why this is not a reduced publication target

The batch renders **250 pages** for pipeline proof only. The **14,000-page minimum launch corpus** objective is unchanged. This is not a 250-page launch, pilot site, glossary, or blog substitute.

---

## Batch selection methodology

Deterministic stratified selection via `select_rc_batch_routes()` in `build.py`:

1. **Tier 0** — Sprint 6M-C QA proof routes (8 fixed `route_id`s)
2. **Round-robin** from stratified buckets sorted by `route_id`:
   - gateway → de_terminology → disambiguation → reference_governance → en_terminology → acquisition → reference
3. **Fill** remaining slots by `route_id` sort until limit reached
4. **Eligibility** — draft-backed content exists, template mappable via `TEMPLATE_FRAME_BRIDGE`, route status `planned`

---

## Target batch size

**250** (upper bound of 100–250 sprint target)

---

## Actual rendered count

**250** pages

---

## Skipped count

**0** (all selected routes rendered successfully)

---

## Selected route families

| Page type | Count |
|---|---:|
| en_terminology | 168 |
| reference_governance | 33 |
| disambiguation | 21 |
| de_terminology | 18 |
| reference | 5 |
| gateway | 4 |
| acquisition | 1 |

---

## Selected languages

| Language | Count |
|---|---:|
| English (`en`) | 228 |
| German (`de`) | 22 |

---

## Selected page types

Gateway/home, EN terminology, DE terminology, disambiguation authority, methodology/reference/governance, foundation routes, cohort-02 terminology waves, acquisition surface (1 route).

---

## Source-required coverage

**249** pages visibly preserve `[SOURCE REQUIRED]` or source-required markers in rendered HTML; **1** page without visible marker (gateway frame excerpt limitation — documented weakness).

---

## Governance / status coverage

All pages: route status **planned**, publication posture **non_public**, indexable/sitemap/navigation **false**, claim approval **no_claims_approved**.

---

## noindex posture

Every page includes `<meta name="robots" content="noindex, nofollow">` and governance banner robots line.

---

## Sitemap / navigation exclusion posture

Every page states outside sitemap and outside navigation; nav partial inactive; no sitemap XML generated.

---

## What rendered correctly

- 250/250 pages under `site/_sample/{route_id}.html`
- Template bridge across reference_page, term_page, home, acquire templates
- RC Batch 01 markers, manifest (`rc_batch_manifest.json`), and matrix generated
- Multilingual DE cohort included (22 pages)
- Disambiguation and governance families represented

---

## What failed or remains weak

- **Minimal markdown renderer** — not production-grade (tables, nested lists limited)
- **Home/gateway frames** — full body not always rendered; `[SOURCE REQUIRED]` in source markdown may not appear in gateway excerpt
- **Empty slots** — term map, hreflang, internal links remain inactive under locks
- **glossary/newsletter skeleton templates** — still bridged at build time, not individually wrapper-hardened

---

## Blockers before larger RC batches

1. Production-grade markdown/content rendering
2. Explicit cohort authorization for 500+ page batches
3. Gateway/home frame body rendering for full source-required visibility
4. Validator performance review for 500+ HTML file scans
5. Remaining skeleton template wrapper hardening (glossary, newsletter)

---

## Blockers before the 14,000-page launch corpus

1. Complete draft backing (58 missing drafts remain)
2. Source verification and claim approval per SOURCE_POLICY
3. Quality Gate passage per route cohort
4. Explicit publication sprint authorization
5. Sitemap/navigation policy activation only after published routes exist
6. **14,000-page minimum** remains fixed — not reduced to 500 pilot scope

---

## Relationship to future 100,000+ expansion

Batch selection and render modes are **route-count-agnostic** and **name-agnostic**. The same quarantine contract, template bridge map, and governance markers scale toward 100,000+ governed pages without relitigating the 14,000-page launch floor.
