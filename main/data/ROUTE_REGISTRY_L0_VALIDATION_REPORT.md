# Route Registry L0 Validation Report

**Sprint:** 5I-B  
**Validation date:** 2026-05-27

---

## Validator

| Field | Value |
| --- | --- |
| Validator file | `scripts/validate_route_registry_l0.py` |
| Mode | Read-only (stdlib only; no file modifications) |
| Network | Not required |

---

## Files checked

- `main/data/routes.json`

---

## routes.json parse result

**PASS** — Valid JSON; `routes` array present with **126** records.

---

## Route counts

| Metric | Count |
| --- | ---: |
| Routes before wave 1 | 26 |
| New routes (Sprint 5I-B marker in notes) | 100 |
| Routes after wave 1 | 126 |

---

## Validation results

| Check | Result |
| --- | --- |
| Duplicate `route_id` | **PASS** — none |
| Duplicate `path` | **PASS** — none |
| Required fields | **PASS** — all routes complete |
| `status: planned` | **PASS** — all 126 routes |
| `indexable: false` | **PASS** — all routes |
| `in_sitemap: false` | **PASS** — all routes |
| `in_navigation: false` | **PASS** — all routes |
| `content_file` path pattern (EN/DE) | **PASS** — all wave-1 routes use `main/content/en/pages/` or `main/content/de/pages/` |
| High-risk keyword screen (wave-1 routes) | **PASS** — no forbidden keywords in new route_id, path, title, description, or h1 |
| Content file creation | **PASS** — no new Markdown content files created for wave-1 routes |

---

## Unresolved warnings

Pre-existing routes (registered before Sprint 5I-B) contain keywords flagged by the L0 screen. These are **not** wave-1 additions and remain planned/non-public:

| route_id | Warning |
| --- | --- |
| `industrial_sulfur_systems` | `procurement` appears in metadata (pre-existing) |
| `sulfur_safety_context` | `handling instruction` context (pre-existing; safety route) |
| `hydrogen_sulfide_risk` | `handling instruction` context (pre-existing; safety route) |
| `newsletter` | utility route keyword (pre-existing) |
| `acquire` | acquisition utility route (pre-existing) |

**Wave-1 routes:** zero content_file paths exist on disk (no collision with draft bodies).

---

## Final validation conclusion

**PASS**

Sprint 5I-B route registration wave 1 meets L0 validation requirements. Registry is valid JSON, contains **100** new planned routes, has no duplicate identifiers or paths, and all routes remain non-indexable, out of sitemap, and outside navigation.

---

*Generated from `py scripts/validate_route_registry_l0.py` — 2026-05-27*
