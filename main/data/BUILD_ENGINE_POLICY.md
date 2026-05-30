# Build Engine Policy

**Sprint:** 6M-A  
**Authority:** `scripts/build.py` (sovereign build engine)  
**Governed by:** `doctrine/PROJECT_DOCTRINE.md`, `main/data/routes.json`, `main/config/build.json`

---

## Build engine authority rules

1. The build engine is the **only authorized orchestrator** for static HTML output planning and (when gates open) generation.
2. Default invocation performs **no file writes**.
3. All output modes require **explicit CLI flags**.
4. The build engine is **read-only** with respect to routes, content, sources, claims, and navigation registries.
5. Build decisions must be **deterministic** given the same inputs.

---

## Publication lock rules

- Only routes with `status: "published"` may produce public HTML output.
- `generate_only_published_routes: true` in `main/config/build.json` is mandatory in current posture.
- `publish_planned_routes: false` must remain unless explicitly authorized by sprint decision.
- File existence of a draft **does not** imply publish permission.
- All 1,043 routes are currently **planned** — zero render-eligible routes.

---

## Indexation lock rules

- `indexable: true` requires `status: published` and explicit publication gate approval.
- Non-public outputs must use **`noindex, nofollow`** robots directive.
- Build must fail in strict mode if `indexable: true` while `status != published`.

---

## Sitemap lock rules

- Per-route: `in_sitemap: true` requires `indexable: true`, `status: published`, and global sitemap authorization.
- Global: `main/data/sitemap_policy.json` status must be **active** with authorized URLs before sitemap generation.
- Current posture: sitemap policy **inactive**, `urls: []` — sitemap generation **forbidden**.

---

## Navigation lock rules

- Per-route: `in_navigation: true` requires `status: published` and global navigation authorization.
- Global: `main/config/navigation.json` status must be **active** with items before navigation artifact generation.
- Current posture: navigation **inactive**, `items: []` — navigation generation **forbidden**.

---

## Source/claim lock rules

- Build must not approve sources or claims.
- Build must not remove `[SOURCE REQUIRED]` markers from content.
- Build must not bypass `source_required: true` route flags.
- Routes requiring verified claims must not render as publication-ready without claim registry approval (future render phase).

---

## Template readiness rules

- Referenced templates must exist before render (strict mode fails otherwise).
- Templates must include governance markers during skeleton phase.
- Required structural slots: head, metadata hooks, language/dir, content body, source/governance partials, internal links, footer (via `base.html` composition).
- Placeholder-like templates (below size threshold) are reported but do not authorize silent production use in strict mode without explicit sprint waiver.

---

## Output directory rules

- Default output directory: `site/` per `main/config/build.json`.
- Build must not delete `site/` unexpectedly.
- Build must not overwrite unrelated files without explicit mode.
- Sample output (future): restricted subdirectory (e.g. `site/_sample/`) with non-public labeling.
- No committed public HTML in Sprint 6M-A.

---

## Dry-run rules

- `--dry-run` inspects routes, templates, and output plan.
- Dry-run writes **no public HTML**.
- Dry-run may write audit JSON only with `--write-audit-report PATH`.
- Dry-run confirms lock posture and `production_can_safely_proceed`.

---

## Sample-render rules

- `--sample N` plans N routes deterministically; does not change route status.
- Sample render (future sprint) requires explicit authorization, non-public output path, and noindex labeling.
- Sample mode does not imply publication readiness.

---

## Production-build rules

Prerequisites (all required):

1. Zero strict-mode validation errors
2. Templates production-ready (not skeleton)
3. Published routes with Quality Gate pass
4. Source/claim boundaries satisfied for target routes
5. Explicit sprint authorization
6. `production_can_safely_proceed: yes` from L2 planner consensus

---

## Public-launch rules

Public launch requires additional gates beyond production build:

- 14,000-page governed corpus target progress (strategic)
- 500-page threshold satisfied with full gate compliance
- Sitemap and navigation policies activated under doctrine
- Security policy gates (CSP, etc.)
- Explicit launch sprint decision in `DECISION_LOG.md`

---

## What build.py may never infer

- Draft file existence → publish permission
- Route registration → indexation permission
- Content completeness → source verification
- Template file presence → production readiness
- Corpus size → launch authorization
- Absence of CI failure locally → production safety

---

## What build.py may never modify

- `main/data/routes.json`
- `main/data/internal_links.json`
- `main/data/sitemap_policy.json`
- `main/data/navigation.json` / `main/config/navigation.json`
- `main/data/sources/source_registry.json`
- `main/data/claims/*.json`
- Any file under `main/content/**`
- Route `status`, `indexable`, `in_sitemap`, or `in_navigation` fields
