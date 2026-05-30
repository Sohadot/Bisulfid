# Template Hardening Report

**Sprint:** 6M-B  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-6m-b-fourteen-thousand-publication-frame-template-layer`  
**Status:** Complete — publication frame hardened; all locks preserved

---

## Why this sprint exists

Sprint **6M-A** hardened the sovereign build engine. Before governed rendering at **14,000-page** scale, the **template layer** must become a publication frame that preserves publication, indexation, sitemap, navigation, source, and claim locks across languages and page types.

This sprint is **not** a launch, sample launch, or reduced target exercise. It prepares the rendering shell inside the fixed **14,000-page minimum launch corpus** pipeline.

---

## Strategic constraint

| Rule | Posture |
| --- | --- |
| Minimum launch corpus | **14,000 governed pages** (fixed) |
| 500-page threshold | Advisory readiness gate only — **not** a launch target downgrade |
| Sample rendering | Engineering QA inside the 14k pipeline only |
| Public launch | **Not authorized** |

---

## Current corpus scale (unchanged)

| Metric | Value |
| --- | --- |
| Routes | **1,043** |
| Draft-backed | **985** |
| Missing drafts | **58** |
| Published | **0** |
| Indexable / sitemap / navigation | **0** |
| `production_can_safely_proceed` | **no** |

---

## Changes made

### Publication frame templates (new / hardened)

| File | Role |
| --- | --- |
| `base.html` | Institutional shell — lang/dir, governance banner, breadcrumbs, slots |
| `home.html` | Gateway frame for 14k corpus entry |
| `page.html` | Generic governed page frame |
| `reference.html` | Reference-layer frame |
| `term.html` | Terminology frame (COHORT-scale ready) |

### Hardened partials

| Partial | Purpose |
| --- | --- |
| `head.html` | Title, description, robots, canonical (non-public mode), governance meta |
| `governance_banner.html` | Draft/planned/non-public visibility |
| `breadcrumbs.html` | Route context without invented links |
| `nav.html` | Inactive navigation slot |
| `footer.html` | 14k frame governance language |
| `source_bar.html` | Source-required visibility; no approval implied |
| `internal_links.html` | Empty-safe link slot |
| `hreflang.html` | Multilingual-ready, inactive by default |
| `safety_notice.html` | Safety boundary slot |

### Validation

- `scripts/validate_template_layer_l1.py` — frame contract checks
- `scripts/validate_sample_output_l1.py` — quarantined output checks (when used)

### Quarantine path

- `site/_sample/` — reserved for **local uncommitted** QA renders only
- No HTML committed: L1 publication lock scans `site/**/*.html`
- Frame proof validated via template L1 validator and build dry-run

---

## Legacy templates

Registry still references skeleton templates (`reference_page.html`, `term_page.html`, etc.). Migration to publication frame templates occurs in a future sprint **without** modifying `routes.json` in this sprint.

---

## What this sprint does not authorize

- Route publication, indexation, sitemap, or navigation activation
- Source or claim approval
- Registry or content modification
- Public launch or production build
- Reduced launch target (500 pages is not the objective)

---

## Remaining blockers before 14,000-page render/publish

1. Registry template migration (`reference_page.html` → `reference.html`, etc.)
2. Build engine render pass wiring to publication frame
3. Source verification for `source_required` routes
4. Claim registry activation per route requirements
5. Template CSP production values (Gate 06)
6. Multilingual wave content and hreflang activation
7. `production_can_safely_proceed: yes` (not achieved)

---

## Recommended next sprint

**6M-C — Governed render wiring + local quarantined sample render** (uncommitted under `site/_sample/`), publication lock exception for `_sample/` if CI requires committed QA proofs.
