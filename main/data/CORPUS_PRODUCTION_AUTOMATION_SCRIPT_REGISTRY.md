# Corpus Production Automation Script Registry — Layer 2

**Sprint:** 5O-A  
**Date:** 2026-05-29

---

## L2 scripts

| Script | Role |
| --- | --- |
| `scripts/corpus_production_planner_l2.py` | Dry-run production status summary (console only) |
| `scripts/validate_production_wave_plan_l2.py` | Production wave plan and threshold validation |
| `scripts/validate_internal_link_graph_plan_l2.py` | Internal link graph planning validation |
| `scripts/validate_seo_indexation_plan_l2.py` | SEO and indexation planning validation |
| `scripts/validate_multilingual_wave_plan_l2.py` | Multilingual wave planning validation |
| `scripts/corpus_production_runtime_l2.py` | L2 orchestration runtime |

---

## Role, inputs, and write restrictions

| Script | Reads | Must not modify |
| --- | --- | --- |
| `corpus_production_planner_l2.py` | `routes.json`, `source_registry.json`, `claims/*.json`, threshold/wave docs | Any file |
| `validate_production_wave_plan_l2.py` | Wave model docs, launch threshold, sovereign program, next-actions docs | Any file |
| `validate_internal_link_graph_plan_l2.py` | Link graph model, `routes.json`, `internal_links.json` | Any file |
| `validate_seo_indexation_plan_l2.py` | SEO model, `routes.json`, `sitemap_policy.json`, threshold doc | Any file |
| `validate_multilingual_wave_plan_l2.py` | Multilingual model | Any file |
| `corpus_production_runtime_l2.py` | Invokes all L2 scripts above | Any file |

---

## Read-only / dry-run status

| Script | Modifies files | Network | Dependencies |
| --- | --- | --- | --- |
| All L2 scripts | **No** | **No** | **stdlib only** |

Planner output is **console-only** in Sprint 5O-A.

---

## Relationship to L1 corpus runtime

| Runtime | Command | Scope |
| --- | --- | --- |
| L1 | `python scripts/corpus_validation_runtime_l1.py` | Route/draft/publication/claim/reference locks |
| L2 | `python scripts/corpus_production_runtime_l2.py` | Production planning governance |

**Both** should pass before production scale-up merges. L2 does not replace L1.

---

## Relationship to source/claim guardrail runtime

| Runtime | Command | Scope |
| --- | --- | --- |
| Guardrail | `python scripts/source_claim_guardrail_runtime_l1.py` | Source registration proposals, evidence, claim boundaries, registry locks |

Run guardrail before/after source sprints. L2 wave planning assumes source/claim gates remain mandatory.

---

## Merge-blocking role

| Failure type | Blocks merge |
| --- | --- |
| L2 runtime **FAIL** | Yes — for sprints touching production planning docs or L2 scripts |
| L1 runtime **FAIL** | Yes — always for corpus sprints |
| Guardrail **FAIL** | Yes — for source/claim sprints |

---

## Publication-blocking role

L2 validators do **not** authorize publication. They **block** planning merges that violate wave/gate discipline. Publication requires L1 publication lock PASS + 500-page threshold + human signoff.

---

## Future L3/L4 production automation layers

| Layer | Planned scope |
| --- | --- |
| **L3** | Automated edge consistency (`internal_links.json` + `routes.json`); draft wave manifest validators |
| **L4** | Rendered output link checker; post-launch indexation audit bots (chartered only) |

L3/L4 require separate sprints; not created in 5O-A.

---

## Human review requirement

| Action | Automation | Human |
| --- | --- | --- |
| Production planning doc updates | L2 validate | Review wave charter |
| Route registration wave 2 | L2 plan | Approve manifest |
| Draft production | L1 validate | Editorial charter |
| Source registry writes | Guardrail | Always |
| Claim approval | Guardrail | Always |
| Publication | L1 + L2 + gates | Quality Gate + owner |

---

*Sprint 5O-A — Corpus Production Automation Script Registry Layer 2*
