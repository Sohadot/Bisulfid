# Route Registry — Duplicate and Path Collision Audit

**Sprint:** 6L  
**Date:** 2026-05-30  
**Scope:** Collision audit across all **1,043** routes in `routes.json`

---

## Verdict

**PASS** — zero duplicate `route_id`, zero duplicate `route_path`, zero duplicate `content_file` across the full registry.

---

## Duplicate route_id audit

| Check | Collisions | Status |
| --- | ---: | --- |
| Unique `route_id` values | **0** | **PASS** |
| Total routes | 1,043 | — |
| Distinct route_ids | 1,043 | ✓ |

---

## Duplicate route_path audit

| Check | Collisions | Status |
| --- | ---: | --- |
| Unique `path` values | **0** | **PASS** |
| Total paths | 1,043 | — |
| Distinct paths | 1,043 | ✓ |

### Sprint 6K comparison path disambiguation (resolved)

Sprint 6H inventory contained **12** comparison base paths shared by **4** reference-layer variants each (**48** routes). Sprint 6K disambiguated by appending `{ref}/{aud}/` segments. Sprint 6L confirms **no residual path collisions**.

**Example (bisulfid vs bisulfide):**

| route_id | path |
| --- | --- |
| `cohort02_en_bisulfid_vs_bisulfide_chem_ling` | `/en/terminology/compare/bisulfid-vs-bisulfide/chem/ling/` |
| `cohort02_en_bisulfid_vs_bisulfide_res_res` | `/en/terminology/compare/bisulfid-vs-bisulfide/res/res/` |
| `cohort02_en_bisulfid_vs_bisulfide_stu_edu` | `/en/terminology/compare/bisulfid-vs-bisulfide/stu/edu/` |
| `cohort02_en_bisulfid_vs_bisulfide_ai_tech` | `/en/terminology/compare/bisulfid-vs-bisulfide/ai/tech/` |

---

## Duplicate content_file audit

| Check | Collisions | Status |
| --- | ---: | --- |
| Unique `content_file` values | **0** | **PASS** |
| COHORT_02 1:1 route_id ↔ filename | 902/902 | ✓ |

---

## Broken draft path audit

### COHORT_02 (902 routes)

| Check | Broken | Status |
| --- | ---: | --- |
| Draft file missing | **0** | **PASS** |

### Pre-COHORT + COHORT_01 (141 routes)

| Check | Broken | Status |
| --- | ---: | --- |
| Draft file missing | **58** | **Pre-existing** (not introduced by 6K) |
| COHORT_01 foundation drafts missing | **0** | **PASS** (15/15 exist) |
| Pre-COHORT EN drafts missing | **8** | Pre-existing planned inventory |
| Pre-COHORT DE drafts missing | **50** | Pre-existing planned inventory |

**Note:** The 58 missing drafts are **planned routes without content files** — expected pre-launch posture for Wave 1 inventory rows not yet drafted. **Not a collision or duplicate defect.**

---

## Internal-link target collision audit

| Check | Broken targets | Status |
| --- | ---: | --- |
| `required_internal_links` → registered route_id | **0** | **PASS** |
| Total internal-link edges validated | 2,756+ | ✓ |

---

## hreflang_group collision audit

No duplicate `hreflang_group` values detected that would imply unintended route merging. COHORT_02 groups are entity-scoped per inventory design.

---

## Summary

| Category | Issues |
| --- | ---: |
| route_id duplicates | 0 |
| route_path duplicates | 0 |
| content_file duplicates | 0 |
| COHORT_02 broken draft paths | 0 |
| Broken internal-link refs | 0 |
| **Overall** | **PASS** |

No `routes.json` corrections required.

---

*Sprint 6L — Route Registry Duplicate and Path Collision Audit*
