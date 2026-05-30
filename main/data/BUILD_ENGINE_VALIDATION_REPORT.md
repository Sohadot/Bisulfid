# Build Engine Validation Report

**Sprint:** 6M-A  
**Validation date:** 2026-05-30  
**Branch:** `claude/sprint-6m-a-sovereign-build-engine-hardening-layer`

---

## Verdict

**PASS** — build engine hardened; all required runtimes PASS; no public HTML generated; no registries modified.

---

## Files checked

| File | Action |
| --- | --- |
| `scripts/build.py` | Rewritten — sovereign build engine |
| `scripts/serve.py` | Updated — safe preview documentation |
| `scripts/validate_build_engine_l1.py` | Created — L1 validator |
| `main/config/build.json` | Read-only inspection |
| `main/data/routes.json` | Read-only inspection |
| `main/data/sitemap_policy.json` | Read-only inspection |
| `main/config/navigation.json` | Read-only inspection |
| `main/templates/**` | Template readiness inspection |
| `site/` | Output lock verification |

---

## Scripts run

| Script | Result |
| --- | --- |
| `corpus_production_runtime_l2.py` | **PASS** |
| `corpus_validation_runtime_l1.py` | **PASS** |
| `source_claim_guardrail_runtime_l1.py` | **PASS** |
| `corpus_production_planner_l2.py` | **PASS** |
| `validate_build_engine_l1.py` | **PASS** |
| `build.py` (default/help) | **PASS** (exit 0, no writes) |
| `build.py --dry-run` | **PASS** (exit 0, 0 public HTML) |
| `build.py --dry-run --strict` | **PASS** (exit 0 post partial-check fix) |
| `build.py --sample 3 --dry-run` | **PASS** (planning only) |

**Not run:** full production build (explicitly forbidden).

---

## build.py hardening status

| Requirement | Status |
| --- | --- |
| Deterministic | **Yes** — sorted route_id sample selection, fixed output mapping |
| Fail-closed | **Yes** — strict mode; zero eligible routes in locked posture |
| Route governance flags | **Yes** — status, indexable, in_sitemap, in_navigation |
| No infer publication from file existence | **Yes** |
| Draft routes not publishable | **Yes** — 0 eligible |
| noindex preserved | **Yes** — noindex for all non-published |
| No sitemap/navigation without authorization | **Yes** |
| Audit reports | **Yes** — console + optional JSON |
| Dry-run mode | **Yes** |
| Sample mode | **Yes** (planning) |
| Strict validation | **Yes** |
| No source/registry/content mutation | **Confirmed** |

---

## validate_build_engine_l1.py result

```
VALIDATION SUMMARY: PASS
build.py present: True
build.py size: 27478 bytes
help/default: PASS
--dry-run: PASS
```

---

## L2 runtime result

**PASS** — all L2 production validators passed.

---

## L1 corpus runtime result

**PASS** — all L1 validators passed.

---

## Source/claim guardrail result

**PASS** — all source/claim guardrail validators passed.

---

## Planner result

| Field | Value |
| --- | --- |
| current_route_count | **1,043** |
| draft_backed_route_count | **985** |
| missing_draft_count | **58** |
| route_publication_lock | LOCKED (all planned) |
| indexation_lock | LOCKED (none indexable) |
| sitemap_lock | LOCKED (none in_sitemap) |
| navigation_lock | LOCKED (none in_navigation) |
| source_registry_lock | inactive (15 entries, 0 verified) |
| claim_registry_lock | 6 inactive registries, 0 active, 1 approved claims |
| production_can_safely_proceed | **no** |

---

## Route count

**1,043** total routes.

---

## Draft-backed route count

**985** routes with existing `content_file`.

---

## Missing draft count

**58** (pre-existing Wave 1; not COHORT_02).

---

## Publication lock result

**LOCKED** — 0 published routes.

---

## Indexation lock result

**LOCKED** — 0 indexable routes.

---

## Sitemap lock result

**LOCKED** — sitemap policy inactive; 0 routes with `in_sitemap: true`.

---

## Navigation lock result

**LOCKED** — navigation inactive; 0 routes with `in_navigation: true`.

---

## Source registry posture

**inactive** — 15 entries, 0 verified.

---

## Claim registry posture

6 inactive registries, 0 active, **1** approved claim.

---

## Generated output result

| Artifact | Count |
| --- | --- |
| Public HTML | **0** |
| Sitemap XML | **0** |
| Navigation artifacts | **0** |
| `site/build-status.json` | Not written (dry-run only; no `--write-build-status`) |

---

## Corpus Governance CI

`.github/workflows/corpus-governance-ci.yml` requires L1 corpus validation, source/claim guardrails, and L2 production runtime on PRs to `main`. **Unchanged in this sprint.**

---

## Final validation conclusion

Sprint **6M-A** successfully hardened the sovereign build engine. The build layer is ready for future governed dry-run sample rendering after template hardening. **No publication, indexation, sitemap, or navigation exposure occurred.** `production_can_safely_proceed` remains **no**.
