# Batch 1A Non-Public Draft Creation Report (Sprint 5E)

## Why this sprint exists

Sprint **5D** registered **five** planned `route_id` records (`corpus_methodology_overview`, `internal_linking_discipline`, `quality_gate_public_explainer`, `de_method_corpus_map`, `de_method_translator_playbook`) with `content_file` paths but **created no Markdown bodies**. Sprint **5E** supplies **non-public drafts** so methodology, linking discipline, quality-gate explanation, and German methodology layers have **reviewable text**—still **not** publication, **not** route state changes, **not** registry mutations.

## Relationship to Sprint 5D

This sprint **only** creates files whose paths match `routes.json` `content_file` fields for the **same five** Batch **1A** routes. **`home`** and **`sources`** were part of the readiness cohort but already had content paths outside this batch; they were **not** targets here.

## Target `route_id` list

1. `corpus_methodology_overview`
2. `internal_linking_discipline`
3. `quality_gate_public_explainer`
4. `de_method_corpus_map`
5. `de_method_translator_playbook`

## Route preflight (read-only against `main/data/routes.json`)

| route_id | Present | status | indexable | in_sitemap | in_navigation | content_file match |
| --- | --- | --- | --- | --- | --- | --- |
| corpus_methodology_overview | yes | planned | false | false | false | `main/content/en/pages/corpus-methodology.md` |
| internal_linking_discipline | yes | planned | false | false | false | `main/content/en/pages/internal-linking-discipline.md` |
| quality_gate_public_explainer | yes | planned | false | false | false | `main/content/en/pages/quality-gate.md` |
| de_method_corpus_map | yes | planned | false | false | false | `main/content/de/pages/corpus-map.md` |
| de_method_translator_playbook | yes | planned | false | false | false | `main/content/de/pages/translator-playbook.md` |

No target route was missing. **No pre-existing file** was found at any path before creation; **no overwrites** occurred.

## Files created

| content_file | route_id |
| --- | --- |
| `main/content/en/pages/corpus-methodology.md` | `corpus_methodology_overview` |
| `main/content/en/pages/internal-linking-discipline.md` | `internal_linking_discipline` |
| `main/content/en/pages/quality-gate.md` | `quality_gate_public_explainer` |
| `main/content/de/pages/corpus-map.md` | `de_method_corpus_map` |
| `main/content/de/pages/translator-playbook.md` | `de_method_translator_playbook` |

## Frontmatter per draft

All five files include YAML frontmatter with:

- `route_id` matching the registry row  
- `status: draft`  
- `publication_status: non_public`  
- `indexable: false`  
- `in_sitemap: false`  
- `language`, `locale`, and `source_language` aligned with `routes.json`  

## Why each draft stays non-public

Body copy on **every** page states explicitly: **non-public draft**, **not published**, **not indexable**, **not in sitemap**, **not approved for public use**, **not publication-ready**. Routes remain **`planned`** in `routes.json`; Sprint **5E** **does not** change route registry fields.

## Registries and graph unchanged

- **`routes.json`** — **not modified** (draft sprint only).  
- **`internal_links.json`** — **not modified**; drafts explain that linking remains a separate governed step.  
- **Sitemap / navigation / source / claims / ontology JSON** — **not modified**.  

## Claims and sources

- **No claim** was **approved**; registries stay **inactive**.  
- **`[SOURCE REQUIRED]`** markers remain where factual or doctrinal restatements are not yet registry-backed.  
- Drafts **do not** claim source-locking is complete.

## Output scope

- **No** route was **published**.  
- **No** generated **HTML**.  
- **No** dependencies, workflows, or deploy configs.  
- **Not** a public launch.

## Remaining Batch 1A route planning state

The five routes remain **`planned`**, **`indexable: false`**, **`in_sitemap: false`** in `routes.json`. Draft existence does **not** satisfy the Quality Gate. **`internal_links.json`** still holds whatever edges existed before; future sprints must wire **route_id-only** edges under policy.

## Recommended next sprint

**Suggested Sprint 5F (or equivalent):** (1) Source-mapping sprint for selected `needs_source_mapping_before_route` concepts *or* editorial hardening of these methodology drafts with doctrine citations; (2) optional `internal_links.json` batch that adds **planned** edges referencing **`route_id`** only; (3) continue to forbid publication until gates are met.

---

*Sprint 5E — draft Markdown only.*
