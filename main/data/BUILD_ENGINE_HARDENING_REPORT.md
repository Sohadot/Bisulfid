# Sovereign Build Engine Hardening Report

**Sprint:** 6M-A  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-6m-a-sovereign-build-engine-hardening-layer`  
**Status:** Complete — build engine hardened; no public HTML generated

---

## Why this sprint exists

After Sprint 6L confirmed **1,043** governed routes with zero publication leakage, the next strategic risk is not route registration — it is **uncontrolled output generation**. A naive build script could infer publishability from file existence, emit indexable HTML, populate sitemaps, or expose navigation before Quality Gate and source/claim boundaries are satisfied.

Sprint **6M-A** hardens `scripts/build.py` into a **sovereign build engine** before any serious HTML generation or public-output sprint.

---

## Why build.py must be hardened before output generation

| Risk without hardening | Mitigation in 6M-A |
| --- | --- |
| Draft existence treated as publish permission | Render eligibility requires `status: published` plus config gates |
| Silent skeleton template use | Template readiness checks; strict mode fails on missing blocks |
| Accidental sitemap/navigation exposure | Global + per-route gates enforced; generation disabled |
| Non-deterministic output | Deterministic route ordering, fixed output path mapping |
| Fail-open on missing assets | Strict mode fails on missing template/content/duplicate paths |
| Unaudited build runs | Console summary + optional audit JSON; policy documents |

---

## Current corpus scale

| Metric | Value |
| --- | --- |
| Total routes | **1,043** |
| Draft-backed routes | **985** |
| Missing drafts | **58** (pre-existing Wave 1) |
| Published routes | **0** |
| Indexable routes | **0** |
| In sitemap | **0** |
| In navigation | **0** |
| `production_can_safely_proceed` | **no** |

---

## Relationship to 500-page launch threshold

The corpus has **exceeded** the 500-page advisory threshold (1,043 routes). The threshold now governs **publication readiness planning**, not route registration volume. The build engine treats threshold exceedance as a reason for **stricter** output lock enforcement — not as implicit launch permission.

---

## Relationship to 14,000+ governed corpus goal

The sovereign build engine is designed to scale from hundreds to **tens of thousands** of pages without changing governance semantics:

- Per-route flag evaluation is O(n) and deterministic
- Output path collision detection scales with route count
- Dry-run mode supports full-corpus inspection without writes
- Sample mode supports controlled micro-renders before mass output

Build hardening is a prerequisite for any future wave that approaches the 14,000-page launch corpus target.

---

## Relationship to L1/L2 automation

| Layer | Role for build engine |
| --- | --- |
| **L1** (`corpus_validation_runtime_l1.py`) | Validates route registry, publication locks, drafts, claims |
| **L1** (`source_claim_guardrail_runtime_l1.py`) | Enforces source/claim registry posture |
| **L1** (`validate_build_engine_l1.py`) | **New** — validates build.py safety and governance references |
| **L2** (`corpus_production_runtime_l2.py`) | Production wave planning validators |
| **L2** (`corpus_production_planner_l2.py`) | Dry-run production status summary |

The build engine **consumes** L1/L2 lock posture; it does not replace corpus validators.

---

## Relationship to Corpus Governance CI

GitHub branch protection runs `.github/workflows/corpus-governance-ci.yml` on pull requests to `main`, requiring L1 corpus validation, source/claim guardrails, and L2 production runtime **PASS** before merge. Build engine validation (`validate_build_engine_l1.py`) is recommended for a future CI step but was not added to workflows in this sprint per scope constraints.

---

## Current build.py findings (pre-hardening)

The pre-6M-A `scripts/build.py`:

- Wrote `site/build-status.json` on every invocation (implicit write)
- Did not inspect templates or output plans
- Did not classify route eligibility or blocked routes
- Did not expose dry-run, strict, or sample modes
- Did not enforce sitemap/navigation/indexation gates
- Did not produce audit classifications or strict failure behavior

---

## Changes made

1. **Rewrote `scripts/build.py`** as sovereign build engine with:
   - `--dry-run` — full inspection, zero public HTML
   - `--strict` — fail-closed validation
   - `--sample N` — deterministic sample planning (no HTML in locked posture)
   - `--write-build-status` — explicit audit artifact write only
   - Default (no flags) — help only, **no file writes**
2. **Created `scripts/validate_build_engine_l1.py`** — read-only L1 validator
3. **Updated `scripts/serve.py`** — documents build engine lock posture; not for public deployment
4. **Created build engine policy and model documents** (this file and companions)

---

## Dry-run support status

**IMPLEMENTED**

- Inspects 1,043 routes, templates, and output plan
- Reports eligible (0), blocked (1,043), missing drafts (58), non-public, non-indexable, out-of-sitemap, out-of-navigation
- Confirms `production_can_safely_proceed: no`
- Generates zero public HTML

---

## Strict mode support status

**IMPLEMENTED**

- Fails on missing template (when referenced)
- Fails on missing content for sample candidates
- Fails on duplicate output paths
- Fails on route/content mismatch (frontmatter `route_id`, language fields, publication posture, registry `content_file`)
- Fails on unsafe publication flag combinations
- Fails on indexable/sitemap/navigation conflicts with publication locks
- Fails on missing required route metadata
- **Post-hardening strict dry-run: PASS** (985 route/content alignments checked; skeleton templates pass block checks)

---

## Sample mode support status

**IMPLEMENTED (planning only)**

- `--sample N` selects first N routes by deterministic `route_id` sort
- Does not change route status
- Does not generate HTML while publication locks active
- Output labeling policy documented for future sample renders

---

## Template readiness findings

| Finding | Count / detail |
| --- | --- |
| Required templates present | **15/15** under `main/templates/` |
| Placeholder-like (below 800 bytes) | **9** — expected skeleton phase |
| Governance markers present | All page templates include SKELETON / Quality Gate warnings |
| Missing production blocks | Title, canonical, CSP in `head.html` marked FUTURE |
| Strict mode | PASS after partial-template check refinement |

Templates are **not production-ready** for public launch; they are correctly gated.

---

## Output safety findings

| Check | Result |
| --- | --- |
| Public HTML in `site/` | **0 files** (`.gitkeep` only) |
| Default build invocation writes | **None** (help only) |
| Dry-run writes | **None** |
| Sitemap generation | **Disabled** |
| Navigation generation | **Disabled** |
| Registry mutation | **None** |
| Content mutation | **None** |

---

## What this sprint does not authorize

- Public route publication
- Public HTML generation or commit
- Sitemap or navigation activation
- Indexation enablement
- Source or claim approval
- Registry or content modification
- Removal of `[SOURCE REQUIRED]` markers
- Production build or public launch
- Workflow changes (Corpus Governance CI unchanged)

---

## Remaining blockers

1. **Templates** — skeleton-only; production blocks (title, canonical, CSP) not implemented
2. **Publication locks** — all 1,043 routes planned; zero published
3. **Source registry** — inactive; 0 verified sources
4. **Claim registries** — predominantly inactive; 1 approved claim only
5. **58 missing drafts** — pre-existing Wave 1 gap
6. **`production_can_safely_proceed`** — remains **no**

---

## Recommended next sprint

**Sprint 6M-B — Template Hardening and Governed Sample Render Planning**

1. Harden templates from skeleton to governed render-ready (head metadata, noindex defaults, governance partials)
2. Authorize first **non-public sample HTML** under `site/_sample/` with explicit noindex labeling
3. Integrate `validate_build_engine_l1.py` into CI (optional, if workflow change approved)
4. Continue corpus production toward 14,000 pages under existing source/claim gates
