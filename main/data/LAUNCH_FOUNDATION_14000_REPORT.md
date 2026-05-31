# Launch Foundation 14,000 Report — Sprint 6M-G

**Date:** 2026-05-31  
**Branch:** `claude/sprint-6m-g-14000-page-controlled-public-launch-foundation`  
**Status:** Complete — 14,000-page controlled public launch foundation

## Why this sprint exists

Sprint 6M-F proved the governed corpus and render pipeline at 7,500 non-public RC scale. Bisulfid must now move from backstage quarantine testing into the first **controlled public launch foundation** — visible HTML with strict gate separation, not another hidden-only QA experiment.

## Why move beyond backstage quarantine

The 7,500-page RC experiment validated expansion mechanics, template frames, and validator coverage. Keeping 14,000 pages trapped in `site/_sample/` would misrepresent the strategic objective: a governed public reference asset, not perpetual engineering quarantine.

## Why the 7,500-page RC test is complete

All 6M-F validators passed. The 7,500-page stage was a scale test on the path to 14,000 — not the final objective. RC HTML remains under `site/_sample/` for regression comparison; the launch foundation lives under `site/public/`.

## Why 14,000 pages is the first controlled public launch foundation

14,000 is the fixed initial public launch corpus size defined in the publication pipeline. This sprint delivers that foundation with full governance: planned routes, noindex posture, no sitemap/navigation exposure, and truthful source/claim status.

## Why 14,000 is a small beginning

Bisulfid's long-term target is 100,000+ governed pages and eventually hundreds of thousands. The 14,000-page foundation is the first visible public beginning — not a reduced blog, glossary, or pilot.

## Why this is not uncontrolled publication

- Explicit build command only: `python scripts/build.py --render-public-launch-foundation --limit 14000`
- Dry-run generates no public HTML
- All routes remain `planned` (not `published`)
- Indexation, sitemap, and navigation gates remain closed
- Source and claim registries unmodified
- No false approval language

## Corpus before sprint

| Metric | Count |
|--------|------:|
| Routes | 7,500 |
| Draft-backed | 7,500 |
| Missing drafts | 0 |
| Published | 0 |
| Indexable | 0 |
| In sitemap | 0 |
| In navigation | 0 |

## Corpus expansion performed

- **COHORT_05:** +6,500 governed planned routes via `generate_14000_corpus_expansion_v1.py`
- 806 EN entity bases × 8 variants + 52 single routes
- All new routes: draft-backed, `planned`, non-indexable, outside sitemap/navigation

## Corpus after sprint

| Metric | Count |
|--------|------:|
| Routes | 14,000 |
| Draft-backed | 14,000 |
| Missing drafts | 0 |
| Duplicate route_ids | 0 |
| Duplicate route_paths | 0 |

## Public output

| Metric | Value |
|--------|-------|
| Public output pages | 14,000 |
| Skipped | 0 |
| Output location | `site/public/` |
| Manifest | `site/public/public_launch_manifest.json` |

## Selected route families

| Family | Count |
|--------|------:|
| en_terminology | 13,566 |
| de_terminology | 222 |
| reference_governance | 119 |
| gateway | 59 |
| disambiguation | 23 |
| reference | 10 |
| acquisition | 1 |

## Selected languages

| Language | Count |
|----------|------:|
| en | 13,730 |
| de | 270 |

## Selected page types

Primarily terminology reference pages (`reference_page.html` / bridge frames), plus gateway, disambiguation, governance reference, and acquisition inquiry routes.

## Source-required coverage

All 14,000 public pages preserve visible source posture; manifest reports `source_required_visible: yes` on all rendered pages where content carries `[SOURCE REQUIRED]` markers.

## Governance/status coverage

Every public page includes: route ID, route status (`planned`), publication posture (`public_visible_foundation`), indexable/sitemap/navigation flags (`false`), claim approval state (`no_claims_approved`), and public launch foundation banner.

## Indexation posture

**CLOSED** — `noindex,nofollow` on all public foundation pages; no routes with `indexable: true`.

## Sitemap posture

**CLOSED** — no sitemap artifacts generated; no routes with `in_sitemap: true`.

## Navigation posture

**CLOSED** — navigation slot inactive; no routes with `in_navigation: true`.

## What rendered correctly

- 14,000 deterministic public HTML pages under `site/public/{route_path}/index.html`
- Governance banners, metadata, and source-required visibility preserved
- Quarantined 7,500 RC batch under `site/_sample/` unchanged

## What failed or remains weak

- Production markdown-to-HTML body rendering remains frame-level (content sections present but not full rich rendering)
- Multilingual coverage is EN/DE weighted; AR/FR/ES/JA/ZH expansion remains future work
- Source registry verification remains at 0 verified entries

## Blockers before wider indexation

- Explicit indexation authorization sprint
- Source evidence resolution for `[SOURCE REQUIRED]` pages
- Robots/canonical policy review for public foundation → indexable transition
- Claim boundary review for terminology pages

## Blockers before sitemap publication

- `sitemap_policy.json` activation with governed URL selection
- Per-route `in_sitemap` authorization
- Indexation gate must precede or co-ordinate with sitemap

## Blockers before navigation exposure

- `navigation.json` curation model for governed subsets
- Editorial selection — not mass dump of 14,000 routes
- Claim/source approval for navigated pages

## Relationship to future 100,000+ expansion

COHORT_05 entity catalog and render pipeline are designed for continued deterministic expansion. Public foundation proves visibility at 14,000 scale before scaling corpus production waves.

## Relationship to hundreds-of-thousands expansion

The gate model (visibility ≠ indexation ≠ sitemap ≠ navigation ≠ source ≠ claim) scales to any corpus size. This sprint establishes the first public visibility layer without compromising long-term governance.
