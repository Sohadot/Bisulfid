# Sovereign Batch Generation Automation Design — Wave 1

**Sprint:** 6C  
**Purpose:** Design batch-governed automation for 100–500 pages/day without micro-sprints.

---

## Automation stack (future)

```
corpus_master_inventory.json
        ↓
sovereign_corpus_generator_v1 (registry read-only)
        ↓
draft cohort output (markdown + manifest)
        ↓
validation runtime (G0–G7)
        ↓
human sample audit (≥10%)
        ↓
merge charter (no routes.json auto-write)
```

---

## Throughput model

| Phase | Pages/day | Cohort size |
| --- | ---: | --- |
| Generator stable (minimum) | **100** | 500–1,000 rows/wave |
| Validator mature (target) | **500** | 2,000 rows/wave |
| Micro-sprint routine families | **0** | Replaced by cohort waves |

---

## Batch unit: cohort wave

Each wave specifies:

- `cohort_id` (from 6B cohort model)
- `inventory_row_filter`
- `template_bindings`
- `validation_gates_required`
- `human_review_sample_rate`
- `max_pages_per_run`

Generator processes rows **sequentially or parallel** with shared registry cache — never LLM free-form batch.

---

## Generator inputs (read-only)

| Registry | Use |
| --- | --- |
| corpus_master_inventory.json | Route rows |
| page_type_registry.json | Page family rules |
| audience_layer_registry.json | Audience constraints |
| reference_layer_registry.json | Reference layer rules |
| source_registry.json | source_ids, hierarchy |
| terminology_claims.json | claim_ids, boundaries |
| sulfur_terms.json | term/entity data |
| SOVEREIGN_TEMPLATE_CONTRACT_MODEL_WAVE_1.json | Template binding |
| SOVEREIGN_EVIDENCE_GRADE_REGISTRY_WAVE_1.json | evidence_grade |
| SOVEREIGN_SOURCE_HIERARCHY_MODEL_WAVE_1.json | hierarchy ranks |
| corpus_production_rules.md | Production rules |

---

## Generator outputs (6D)

| Output | Description |
| --- | --- |
| `content_file` draft markdown | Non-public; frontmatter + template sections |
| `generation_manifest.json` | Per-row reliability profile + gate results |
| `cohort_validation_report.md` | Wave summary |

**Not output:** public HTML, routes.json patches, indexable flags.

---

## Parallelization safety

- Registry snapshots at wave start — no mid-wave registry writes  
- Idempotent row processing via `inventory_row_id`  
- Failed rows logged; do not block entire wave unless severity-1 threshold exceeded  
- Duplicate hash check before write  

---

## Cohort priority for 6D (proposed)

1. **COHORT_01_FOUNDATION_GOV** — low source dependency; proves pipeline  
2. **COHORT_02_CORE_TERMINOLOGY** — high value; strict KR gates  
3. **COHORT_05_COMPARISON** — core SEO; comparative_boundary grade  

---

## Monitoring metrics

| Metric | Target |
| --- | --- |
| Gate pass rate | ≥95% first pass after mature |
| Thin page reject rate | tracked; target ↓ over time |
| KR-01–KR-15 failure rate | 0 severity-1 at merge |
| Human review findings | ↓ per cohort iteration |

---

## Explicit prohibitions

- Free-form LLM generation as production method  
- Auto-publish or auto-index  
- routes.json bulk write without charter  
- Marker removal in batch  
- Claim/source registration in generator  

---

## Sprint 6D handoff checklist

- [ ] Generator schema validated  
- [ ] Template contracts for first cohort complete  
- [ ] KR validation requirements implemented as script  
- [ ] Cohort charter written  
- [ ] Sample audit protocol defined  
- [ ] production_can_safely_proceed still **no** expected  
