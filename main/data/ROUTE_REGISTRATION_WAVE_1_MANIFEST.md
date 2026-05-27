# Route Registration Wave 1 — Manifest

**Sprint:** 5I-B  
**Branch:** `claude/sprint-5i-b-route-registration-wave-1`  
**Date:** 2026-05-27

---

## Why this wave exists

Bisulfid.com must move from **strategy** into **controlled route-scale production** under the automation control doctrine. Sprint **5H** established **500 governed pages** as the minimum public launch threshold. Sprint **5I-A** established the corpus automation control layer (stages S0–S9, wave protocol, validation gates, publication locks). This wave is the **first large route-registration pass**: it adds **planned route records only** toward that threshold without creating content, publishing routes, or activating claims.

---

## Relationship to Sprint 5H and 5I-A

| Prior sprint | Contribution to this wave |
| --- | --- |
| **5H** | 500-page blueprint (`CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md`); 193-concept expansion register; production wave model (80–120 routes per registration wave). |
| **5I-A** | Automation control layer; wave sizes; L0 validation requirement; locks on publication, claim approval, and registry mutation outside declared scope. |

This wave executes **S1 route registration** under the automation manifest: registry records only, all routes remain non-public.

---

## Route count target

| Metric | Value |
| ---: | ---: |
| Target new routes | **100** (preferred; within 80–120 band) |
| Actual new routes | **100** |
| Routes before wave | **26** |
| Routes after wave | **126** |

---

## Selected concept categories

| Category | Count (wave 1) | Role |
| --- | ---: | --- |
| `core_terminology` | 64 | English terminology spine + German lexical records |
| `disambiguation_authority` | 8 | EN/DE boundary and triad disambiguation |
| `source_governance` | 6 | Nomenclature, citation, teaching-source boundaries |
| `de_en_chemical_language` | 5 | German–English bridge and suffix/IUPAC boundaries |
| `industrial_economic_interpretation` | 5 | Document-language / vocabulary only (no market data) |
| `documentation_compliance` | 3 | Export/customs/REACH **terminology** framing |
| `index_map` | 3 | Terminology spine, disambiguation, multilingual layer maps |
| `methodology_reference` | 2 | Translator playbook, academic teaching boundary |
| `gateway` | 4 | DE gateway mirrors (home, compounds, uses, glossary) |

---

## Selected language distribution

| Language | New routes | Share |
| --- | ---: | ---: |
| English (`en`) | 30 | 30% |
| German (`de`) | 70 | 70% |

**Rationale:** Wave 1 prioritizes the **German lexical and methodology boundary layer** (Sprint 5B/5C recommendations) plus **English terminology spine, disambiguation, governance, and index infrastructure**. Arabic, Chinese, and Japanese mirror routes are **deferred** to later controlled waves per sprint charter.

---

## Excluded categories

| Excluded | Reason |
| --- | --- |
| `safety_context` | Safety instruction / high-risk substance context — deferred until source-locking and dedicated review |
| `utility` (`newsletter`, `acquire`) | Reference-count / revenue routes — not structural foundation |
| `acquisition` | Strategic acquisition framing — out of wave-1 scope |
| High-risk / `deferred_high_risk_review` | H2S, SDS compliance, sour-gas, aqueous H2S, etc. |
| `ar` / `zh` / `ja` mirrors | Not controlled terminology infrastructure for wave 1; avoid translation-spam registration |
| Market / trade / CAGR / procurement / production data | Explicit sprint exclusion |
| Medical / handling / dosage routes | Explicit sprint exclusion |
| Duplicate blueprint rows | e.g. duplicate `de_term_mercaptan` — deduplicated at registration |

---

## Route selection rules

1. Source: `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` (Sprint 5A table + Sprint 5H expansion register).
2. Prefer `keep_for_launch_cohort` / P0–P2 priority rows aligned with Sprint 5B/5C readiness matrix.
3. Low and medium claim risk only; no `high` risk level.
4. Eligibility must not be `deferred_high_risk_review`.
5. English and German only in this wave.
6. Industrial/compliance pages limited to **document-language / terminology** roles.
7. No route_id already present in `routes.json` before this sprint.

---

## Duplicate prevention rules

- Pre-flight collection of all existing `route_id` and `path` values from `routes.json` (26 routes).
- Blueprint parse deduplication by `route_id` (blueprint contained one duplicate `de_term_mercaptan` row).
- Post-registration L0 validator checks duplicate `route_id`, duplicate `path`, and duplicate `content_file` targets among wave-1 rows.
- Replacement route `sulfate_terminology` added after deduplication to maintain 100-route target.

---

## Planned-only route policy

Every new route:

- `status: planned`
- No publication, no sitemap activation, no navigation wiring

---

## Non-indexable / non-sitemap policy

Every new route:

- `indexable: false`
- `in_sitemap: false`
- `in_navigation: false`

---

## No-content-created policy

This wave **registers routes only**. No Markdown bodies, no HTML, no generated public output. `content_file` paths are **future-facing** placeholders under `main/content/en/pages/` and `main/content/de/pages/`.

---

## Validation method

1. `scripts/validate_route_registry_l0.py` — read-only stdlib validator (JSON parse, duplicates, required fields, status/indexable/sitemap/navigation, content_file patterns, forbidden-keyword screen, content-file existence warnings).
2. Human review checkpoint: owner/editorial review of wave manifest and route_id list before draft-production wave (recommended Sprint 5I-C).
3. Validation report: `ROUTE_REGISTRY_L0_VALIDATION_REPORT.md`.

---

## Human review checkpoint

Before any draft-production wave:

- Confirm wave-1 route_id list matches strategic intent.
- Confirm excluded high-risk routes remain unregistered or planned-only.
- Confirm no claim registry activation or source registry edits occurred.
- Sample audit 10–15 routes for path/content_file consistency.

---

## Rollback expectations

Rollback is **registry-only**:

1. Revert commit `feat(routes): add route registration wave 1` on branch.
2. Restore `routes.json` to 26-route state.
3. Remove wave-1 validator and manifest/report artifacts if full sprint rollback required.
4. No content or published pages to unpublish — none were created.

---

*Sprint 5I-B — Route Registration Wave 1 Manifest*
