# Corpus Automation Next Wave Recommendations

**Sprint:** 5K  
**Date:** 2026-05-27  
**Context:** 126 planned routes, 68 draft-backed, 58 missing drafts, L1 runtime established

---

## Executive recommendation

Proceed in this order:

1. **Sprint 5L — Source and claim boundary review** (50 Sprint 5J drafts + claim registry triage)
2. **Sprint 5M — Draft production wave 2** (40–60 drafts for highest-priority routes without bodies)
3. **Sprint 5N — Route registration wave 2** (80–120 planned routes toward 500-page floor)
4. **Sprint 5O+ — Internal-link wiring wave** (after more draft mass exists; before any publication sprint)

Run `scripts/corpus_validation_runtime_l1.py` and archive results in `CORPUS_L1_VALIDATION_REPORT.md` **before and after** each wave.

---

## Should Sprint 5L be source/claim boundary review?

**Yes — recommended as the immediate next sprint.**

| Rationale | Detail |
| --- | --- |
| **50 new drafts need source discipline** | Sprint 5J created standardized drafts with `[SOURCE REQUIRED]` markers; markers are not satisfied and registries remain inactive |
| **14 pending_review claims** | Claim files exist but no approval path is open; boundary review prevents drift toward implied approval |
| **L1 warnings to resolve** | `sulfur_compounds` and `quality_gate_public_explainer` flagged for language that may treat markers as satisfied |
| **Publication blocker** | Source/claim work is mandatory before any route can graduate from `non_public` draft |

**5L scope (recommended):** Review-only sprint — map markers to future source registry rows, document claim boundaries, emit report. **No** claim approval, **no** registry activation, **no** marker removal unless explicitly chartered in a later sprint.

---

## Should Sprint 5L be draft production wave 2?

**No — defer to Sprint 5M** (after source/claim boundary review).

Adding **40–60** more drafts before reviewing the first **50** wave-1 drafts accumulates **governance debt**: more pages with unresolved markers, more claim-sensitive language to audit, and more legacy-format inconsistency if new waves outpace normalization.

Draft wave 2 remains valuable and should follow quickly after 5L — target the **58** routes still missing draft bodies, prioritized by EN/DE spine and terminology cluster value per `CORPUS_PRODUCTION_WAVE_MODEL.md`.

---

## Should Sprint 5L be route registration wave 2?

**No — defer to Sprint 5N** (after draft wave 2 or in parallel only if editorial capacity allows).

| Current state | Implication |
| --- | --- |
| 58 routes without drafts | Draft debt should shrink before registry grows further |
| 126 / 500 routes | Registry expansion can resume once draft production cadence is stable |
| L1 runtime now available | Route wave 2 can use L1 immediately on merge |

Route registration wave 2 (80–120 routes) is still required toward the **500-page** floor but should not **outrun** draft and source/claim capacity.

---

## Recommended order (summary)

| Order | Sprint | Focus | Wave size |
| --- | --- | --- | --- |
| 1 | **5L** | Source/claim boundary review | 50 drafts + 14 pending claims |
| 2 | **5M** | Draft production wave 2 | 40–60 drafts |
| 3 | **5N** | Route registration wave 2 | 80–120 routes |
| 4 | **5O** | Legacy draft normalization (optional parallel) | 18 pre-5J drafts |
| 5 | **5P** | Internal-link wiring wave 1 | Cluster-scoped edges |
| 6 | **5Q+** | L2 wave runners + CI wiring | Automation charter |

Adjust numbering if owner merges 5O into 5L/5M based on capacity.

---

## Why governance debt must not accumulate

| Debt type | Risk if ignored |
| --- | --- |
| Unreviewed `[SOURCE REQUIRED]` markers | Accidental publication with unsourced claims |
| Draft waves without claim boundaries | Forbidden frames slip into indexable pages later |
| Registry growth without draft bodies | Hollow route records; thin-corpus launch pressure |
| Missing internal links | Broken graph and SEO trust loss at launch |
| Legacy format drift | Two draft standards; L1 warning noise hides real failures |

L1 automation **detects** debt; it does not **pay** it down. Each wave should reduce warnings or document accepted exceptions.

---

## Proceeding toward 500 pages without losing quality

1. **Alternate production and review:** draft wave → L1 run → source/claim sample audit → next draft wave
2. **Keep waves bounded:** 40–60 drafts, 80–120 routes per registration wave (`CORPUS_PRODUCTION_WAVE_MODEL.md`)
3. **Strict on new, warn on legacy:** L1 strict mode for manifest-listed wave targets; legacy drafts normalized in dedicated pass
4. **No publication shortcuts:** 500-page floor, inactive registries, and L1 publication lock remain non-negotiable
5. **Human sample audit:** automation passes are necessary but not sufficient for editorial quality

---

## Recommended wave sizes after L1 automation

| Wave type | Size | Pre-flight | Post-flight |
| --- | --- | --- | --- |
| Draft production | 40–60 | L1 PASS on current corpus | L1 PASS + L0 wave validator |
| Route registration | 80–120 | L1 PASS | L1 PASS + L0 wave validator |
| Source mapping | 20–40 drafts | L1 claims PASS | Updated source review report |
| Claim boundary review | 20–50 drafts | L1 claims PASS | Claim boundary report (no approval) |
| Internal-link wiring | 30–60 edges | L1 references PASS | L1 references PASS + broken-link check |
| Legacy normalization | 18 drafts (one batch) | L1 drafts warnings baseline | Warnings reduced |

---

## Automation reports to check before each future wave

| Report / command | When |
| --- | --- |
| `python scripts/corpus_validation_runtime_l1.py` | Every merge touching routes, content, or registries |
| `main/data/CORPUS_L1_VALIDATION_REPORT.md` | Archive after each validation run |
| `main/data/ROUTE_REGISTRY_L0_VALIDATION_REPORT.md` | After route registration waves |
| `main/data/CONTENT_DRAFTS_L0_VALIDATION_REPORT.md` | After draft production waves |
| `main/data/CORPUS_AUTOMATION_SCRIPT_REGISTRY.md` | When adding scripts or CI |
| Wave-specific manifest + report (e.g. `DRAFT_PRODUCTION_WAVE_*`) | Start and end of each wave |

**Merge block rule (recommended):** Do not merge production waves if L1 runtime reports **FAIL**. Warnings require triage but may merge if documented and accepted by reviewer.

---

## Longer-term automation path

| Layer | Next milestone |
| --- | --- |
| **L1** | Established (Sprint 5K) — corpus-wide read-only validation |
| **L2** | Manifest-driven wave runners for route/draft waves |
| **L3** | Source marker cross-check and claim boundary scanners |
| **L4** | GitHub Actions merge gates; HTML build validation pre-launch |

No L2+ work should precede completion of **5L source/claim boundary review** and at least one **post-L1 draft wave** to prove the runtime under production load.
