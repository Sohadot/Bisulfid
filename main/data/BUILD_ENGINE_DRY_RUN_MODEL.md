# Build Engine Dry-Run Model

**Sprint:** 6M-A  
**Engine:** `scripts/build.py --dry-run`

---

## Dry-run purpose

Dry-run provides a **full-corpus build inspection** without writing public HTML or modifying governed data. It answers: *If we were to build, what would happen, what would be blocked, and are locks still intact?*

Dry-run is the **default safe inspection mode** for CI, local development, and pre-sprint validation.

---

## Dry-run inputs

| Input | Path / source |
| --- | --- |
| Build config | `main/config/build.json` |
| Route registry | `main/data/routes.json` |
| Sitemap policy | `main/data/sitemap_policy.json` |
| Navigation config | `main/config/navigation.json` |
| Templates | `main/templates/**` |
| Content files | Referenced by `content_file` (existence check only) |
| CLI flags | `--dry-run`, optional `--strict`, optional `--sample N` |

---

## Dry-run outputs

| Output | Destination |
| --- | --- |
| Console summary | stdout |
| Optional audit JSON | `--write-audit-report PATH` |
| Public HTML | **None** |
| Sitemap XML | **None** |
| Navigation artifacts | **None** |
| Registry changes | **None** |

---

## Dry-run summary fields

```
Mode
Timestamp (UTC)
Routes loaded
Draft-backed routes
Missing drafts
Eligible for render
Blocked routes
Non-public routes
Non-indexable (planned)
Out of sitemap
Out of navigation
Sample planned (if --sample N)
Publication lock
Indexation lock
Sitemap lock
Navigation lock
production_can_safely_proceed
Public HTML generated
Sitemap generated
Navigation generated
Placeholder-like templates
Output plan notes
```

---

## Route eligibility classes

| Class | Meaning |
| --- | --- |
| `eligible_published` | Published route passing all gates (currently 0) |
| `eligible_planned_override` | Would render only if config explicitly allows planned routes |
| `non_public` | Planned or otherwise non-published |
| `blocked_missing_assets` | Missing template or content file |
| `blocked_unsafe_flags` | Conflicting indexable/sitemap/navigation flags |
| `blocked_planned` | Not published; publication gate closed |

---

## Blocked route classes

All **1,043** routes are currently blocked from render with reason **route not published; publication gate closed**.

Additional block reasons detected per route:

- `missing content_file` (58 routes)
- `missing template` (if template reference broken)
- Unsafe flag combinations (strict mode; currently 0 in registry)

---

## Template check classes

| Class | Description |
| --- | --- |
| `exists` | Template file present |
| `placeholder_like` | Below 800-byte skeleton threshold |
| `missing_blocks` | Required slots absent (strict mode) |
| `governance_present` | SKELETON / Quality Gate markers found |
| `issues` | Aggregated template readiness notes |

---

## Output planning classes

| Plan element | Current posture |
| --- | --- |
| `output_dir` | `site/` |
| `public HTML generation` | DISABLED |
| `sitemap generation` | DISABLED |
| `navigation generation` | DISABLED |
| `robots_directive` | `noindex, nofollow` for all non-published |
| `sample labeling` | dry-run/sample/non-public (future) |

---

## Failure conditions

Strict dry-run (`--dry-run --strict`) fails when:

- Missing referenced template
- Missing content for sample candidate
- Duplicate output path collision
- Unsafe publication flag combination
- Missing required route metadata
- Template missing required blocks (page templates; partials exempt)

Non-strict dry-run reports issues but exits 0 unless config/routes missing.

---

## Why dry-run does not equal build approval

Dry-run is **observational**. It does not:

- Publish routes
- Approve sources or claims
- Activate sitemap or navigation
- Authorize HTML generation
- Change `production_can_safely_proceed`

A passing dry-run means the engine **correctly respects locks**, not that output **should** proceed.

---

## Why dry-run does not equal publication readiness

Publication readiness requires:

- Quality Gate pass per route
- Source verification where `source_required: true`
- Claim registry approval for required claim groups
- Explicit route status change to `published`
- L1/L2 runtime PASS with zero leakage
- Sprint-level authorization in `DECISION_LOG.md`

Dry-run confirms **absence of accidental exposure**, not **presence of launch readiness**.
