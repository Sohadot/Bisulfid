# Route Planning Batch 1A Report (Sprint 5D)

## Why this sprint exists

Sprint **5C** defined **55** blueprint-backed concepts and classified them by implementation readiness. Sprint **5D** executes the **smallest safe slice** of that plan: register **only** the concepts marked **`ready_for_route_planning`** in `ROUTE_IMPLEMENTATION_READINESS_MATRIX.md` as **`planned`** routes in `routes.json`—still **non-indexable**, **non-sitemap**, with **no** new Markdown bodies and **no** publication.

## Relationship to Sprint 5C

Batch **1A** is the **`ready_for_route_planning`** subset (**7** concepts) from the Sprint **5C** readiness matrix. No other readiness bucket (`needs_source_mapping_before_route`, *etc.*) was added in this sprint.

## Source documents reviewed

- `main/data/ROUTE_IMPLEMENTATION_READINESS_MATRIX.md` — readiness classifications.
- `main/data/LAUNCH_COHORT_IMPLEMENTATION_BATCH_1.md` — `proposed_route_id`, paths, language, categories, roles, source posture, risk, clusters, priorities.
- `main/data/SPRINT_5C_ROUTE_SELECTION_RATIONALE.md` — batch context (read-only).
- `main/data/CORPUS_LAUNCH_THRESHOLD.md` — launch threshold unchanged (read-only).
- `main/data/routes.json` — existing schema and duplicates check.
- `DECISION_LOG.md` — prior entries preserved; this sprint appended below.

## Selected `ready_for_route_planning` route concepts (7)

| route_id | path | language |
| --- | --- | --- |
| `home` | `/` | en |
| `sources` | `/sources/` | en |
| `corpus_methodology_overview` | `/reference/corpus-methodology/` | en |
| `internal_linking_discipline` | `/reference/internal-linking-discipline/` | en |
| `quality_gate_public_explainer` | `/reference/quality-gate/` | en |
| `de_method_corpus_map` | `/de/reference/corpus-map/` | de |
| `de_method_translator_playbook` | `/de/reference/translator-playbook/` | de |

**Confirmation:** Exactly **7** rows in the matrix use `ready_for_route_planning` (summary table: count **7**). No mismatch; sprint did not stop early.

## Routes added to `routes.json`

**Five** new `route_id` records appended (same field schema as existing routes):

1. `corpus_methodology_overview`
2. `internal_linking_discipline`
3. `quality_gate_public_explainer`
4. `de_method_corpus_map`
5. `de_method_translator_playbook`

Each added record: `status: "planned"`, `indexable: false`, `in_sitemap: false`, `in_navigation: false`, `source_required: false` (governance-meta posture), `risk_level: "low"`, `required_internal_links: []`, `content_file` paths per existing `main/content/{locale}/pages/*.md` convention (**files not created** this sprint). `de_method_translator_playbook` uses `required_claim_groups: ["terminology_claims"]` per matrix note (illustrative terminology); others use `[]`.

`routes.json` does **not** define a `publication_status` field; none was added.

## `route_id`s skipped (already registered)

| route_id | Reason |
| --- | --- |
| `home` | Already present in `routes.json` with matching `path` `/` and `language` `en` — **no duplicate** row inserted. |
| `sources` | Already present with `path` `/sources/` and `language` `en` — **no duplicate** row inserted. |

## Confirmations (Sprint 5D scope)

| Assertion | Status |
| --- | ---: |
| No new content pages created | **Yes** |
| No content pages modified | **Yes** |
| No `internal_links.json` changes | **Yes** |
| No route published (`status` remains `planned` for all) | **Yes** |
| No claim approved / registries untouched | **Yes** (outside sprint scope) |
| **300-page** minimum launch threshold | **Unchanged** (doctrine); this sprint only adds **5** planned records + acknowledges **2** pre-existing |
| This is **not** a public launch | **Yes** |

## Remaining Sprint 5C concepts **not** added to `routes.json`

| Readiness bucket | Count |
| --- | ---: |
| `needs_source_mapping_before_route` | 35 |
| `needs_claim_boundary_before_route` | 8 |
| `needs_merge_or_scope_adjustment` | 3 |
| `defer_until_later_corpus_phase` | 2 |

## Recommended next sprint

**Batch 1B (suggested):** After source-mapping for the **`needs_source_mapping_before_route`** spine (or a documented subset), register the next wave of `route_id` values—still **`planned`**, **`indexable: false`**, **`in_sitemap: false`**—and only then create matching `content_file` bodies. Optionally update `internal_links.json` with **route_id-only** edges in a dedicated linking sprint once route shells exist.

---

*Sprint 5D — route registry only; no publication.*
