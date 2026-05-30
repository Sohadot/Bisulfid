# Sovereign Batch Production Transition Plan — Wave 1

**Sprint:** 6A  
**Scope:** Transition from micro-sprints to batch-governed corpus production

---

## Problem statement

Manual one-source-one-page month-long cycles cannot reach 14,000 governed pages. Sprints 5A–5N proved governance; Sprint 6A+ must **scale production without scaling risk**.

---

## End of micro-sprint era

| Micro-sprint pattern | Batch production replacement |
| --- | --- |
| One route, one source, one claim per month | Route cohort waves (100–500 pages/day benchmark) |
| Ad hoc content creation | Generator reads inventory + registries |
| Manual validator runs | Automated L1/L2 runtime on every cohort |
| Discussion-first | Architecture-first (6A) → inventory (6B) → generator (6C) |

---

## Batch production pipeline

```
ONTOLOGY + REGISTRIES
        ↓
ROUTE INVENTORY (6B: 14k model)
        ↓
GENERATOR (6C: schema-constrained)
        ↓
DRAFT COHORT (6D: non-public)
        ↓
INTERNAL-LINK GRAPH (6E)
        ↓
VALIDATION RUNTIME (L0/L1/L2)
        ↓
VISIBILITY PLAN (6F) — owner authorized only
```

---

## Generator input contract (6C design target)

```json
{
  "route_id": "...",
  "language": "...",
  "term_entity_id": "...",
  "page_type_id": "...",
  "audience_id": "...",
  "source_ids": ["..."],
  "claim_ids": ["..."],
  "template_id": "...",
  "indexation_posture": "non_indexable"
}
```

Generator **must not** run without complete input. Missing source/claim → `[SOURCE REQUIRED]` or reject.

---

## Throughput benchmarks

| Milestone | Target |
| --- | --- |
| Generator stable (minimum) | **100 pages/day** governed drafts |
| Generator mature | **500 pages/day** with full validator pass |
| Wave size | Cohort-based; not single-page |

---

## Quality gates (prevent thin pages at scale)

1. Page type `required_data_fields` check
2. Anti-thin word/section minimums per family
3. Forbidden claim class scan (L1)
4. Source/claim posture alignment
5. Internal-link target existence
6. Sample human audit ≥10% per cohort
7. Merge blocked on severity-1 failures

---

## What batch production never automates

- `status: published`
- `indexable: true` / `in_sitemap: true`
- Claim approval
- Source registry activation
- Marker removal
- Public HTML before S8

---

## Sprint 6B next-action plan (execution focus)

**Charter:** 14,000-route master inventory model — **not further discussion**.

### 6B deliverables (proposed)

1. `corpus_master_inventory_model.json` — schema for 14k route rows
2. `CORPUS_MASTER_INVENTORY_6B_CHARTER.md` — wave size, eligibility filters
3. Inventory generator script design (read-only spec; implementation 6C)
4. Eligibility report: count valid intersections per language toward 2,000
5. Duplicate and thin-route rejection rules encoded
6. hreflang_group and internal_link_role assignment spec
7. Validation report against existing L1/L2 runtimes

### 6B forbidden

- No content file creation
- No route publication
- No `routes.json` bulk merge without review charter (prefer separate inventory file first)
- No HTML generation

### 6B success criteria

- Machine-readable inventory model validated
- ≥14,000 eligible route rows documented (planned posture)
- Per-language count ≥2,000 in model
- All rows map to page_type + audience + formula dimensions
- Validators PASS on repo (no regression)

---

## Phased roadmap

| Sprint | Deliverable |
| --- | --- |
| **6A** ✓ | Architecture codification |
| **6B** | 14,000-route master inventory model |
| **6C** | Schemas, templates, generator |
| **6D** | First large governed draft cohort |
| **6E** | Internal-link graph + validation expansion |
| **6F** | Controlled public visibility plan |

---

## Current locks (unchanged after 6A)

| Lock | Status |
| --- | --- |
| Publication | LOCKED |
| Indexation | LOCKED |
| Sitemap / navigation | LOCKED |
| `production_can_safely_proceed` | **no** |
| Registered routes | 126 (inventory expansion in 6B) |

---

## Decision

Sprint 6A completes strategic codification. **Proceed to 6B inventory generation** as the immediate next execution sprint.
