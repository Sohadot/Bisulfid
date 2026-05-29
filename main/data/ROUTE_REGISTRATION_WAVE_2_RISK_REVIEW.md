# Route Registration Wave 2 — Risk Review

**Sprint:** 5O-B  
**Date:** 2026-05-27  
**Scope:** Dry-run planning risk analysis — **does not approve execution**

---

## Executive summary

Registering **83** additional routes without draft, source, claim, and link-graph readiness would increase registry surface area by **66%** (126 → 209) while **58** Wave 1 routes still lack drafts. Dry-run planning identifies and classifies candidates; it **does not** authorize registration. This document records risks that execution must mitigate.

---

## Systemic risks

### Risk of registering too many routes before drafts

| Factor | Assessment |
| --- | --- |
| Current missing drafts | **58** / 126 routes |
| Hypothetical post-wave registry | **209** routes |
| Risk | Registry inflation creates content debt; automation and human review cannot scale quality linearly with route count |
| Mitigation | Complete Draft Wave 1 backlog reduction before Route Registration Wave 2 execution; do not register 83 routes until draft pipeline can absorb increment |

### Risk of route count being mistaken for authority

| Factor | Assessment |
| --- | --- |
| Launch threshold | **500** governed pages |
| Current progress | **126** registered, **0** publication-ready |
| Risk | Stakeholders may interpret 209 planned routes as launch progress |
| Mitigation | Dry-run manifest states **execution status: not approved**; governed pages require source lock + editorial sign-off, not registry rows alone |

### Risk of thin pages

| Factor | Assessment |
| --- | --- |
| Candidate profile | **62** core terminology class pages |
| Risk | Bulk terminology registration without ontology/source backing yields stub pages |
| Mitigation | Exclude generic chemistry blog patterns; require source gate before draft assignment; terminology spine linked to `sulfur_terms.json` governance (unchanged this sprint) |

### Risk of generic chemistry content

| Factor | Assessment |
| --- | --- |
| Excluded | Market stats, handling instructions, medical claims, acquisition framing |
| Risk | Element/compound vocabulary pages drift into textbook summaries |
| Mitigation | Blueprint page roles limit scope to **vocabulary and document language**; industrial interpretation rows flagged **needs_review** |

### Risk of source/claim gates being bypassed

| Factor | Assessment |
| --- | --- |
| Source registry | **inactive**, 0 verified |
| Claims | **0** approved |
| Risk | Registration sprint pressure to "fill the wave" skips source/claim mapping |
| Mitigation | Matrix flags source/claim gates per row; guardrail runtime **PASS** with locks enforced; execution blockers document mandatory gates |

### Risk of weak internal link graph planning

| Factor | Assessment |
| --- | --- |
| Index/map candidates | **5** |
| Terminology spine | **62** |
| Risk | Orphan routes, broken hub/spoke, uneven PageRank to thin nodes |
| Mitigation | `internal_links.json` unchanged until link roles assigned; L2 link graph validator required pre-execution |

### Risk of multilingual translation spam

| Factor | Assessment |
| --- | --- |
| ar/zh/ja | **Excluded** from dry-run |
| DE candidates | **11** — require hreflang governance |
| Risk | Premature locale expansion without translation registry discipline |
| Mitigation | EN/DE-first dry-run; DE rows flagged **multilingual governance required: yes**; massive locale expansion deferred |

### Risk of SEO over-expansion

| Factor | Assessment |
| --- | --- |
| Indexation lock | **LOCKED** |
| Risk | Accidental indexable/sitemap flags during bulk registration |
| Mitigation | All routes remain `planned`; L2 SEO/indexation validator; sitemap/navigation locks verified in validation report |

### Risk of broken public links

| Factor | Assessment |
| --- | --- |
| Published routes | **0** |
| Risk | Future partial launch surfaces 404s from registered-but-undrafted routes |
| Mitigation | Publication lock held; no HTML generation; registration execution paired with draft minimum viable set policy (future sprint) |

### Risk of future sitemap/indexation leakage

| Factor | Assessment |
| --- | --- |
| Current posture | 0 indexable, 0 in sitemap, 0 in navigation |
| Risk | Automation or manual error sets flags during wave execution |
| Mitigation | L1 publication lock validator + L2 SEO plan validator in execution sprint; dry-run does not touch policy files |

---

## Per-category risk notes

### `core_terminology` (62 candidates)

- **Risk:** Terminology stubs without ontology linkage and source validation.
- **Gate:** Source + claim gates required for strict-registry pages.
- **Posture:** `future_route_registration_candidate` or `needs_claim_gate_first`.

### `controlled_industrial_language` (9 candidates)

- **Risk:** Drift into market data, procurement advice, or operational guidance despite blueprint constraints.
- **Gate:** **9** rows marked `dry_run_candidate_needs_review`; medium claim risk.
- **Posture:** `needs_source_gate_first` — document-language only.

### `index_map` (5 candidates)

- **Risk:** Thin hub pages with insufficient outbound governed links.
- **Gate:** Internal link role assignment mandatory before registration.
- **Posture:** `needs_link_graph_role_first`.

### `disambiguation_authority` (2 candidates)

- **Risk:** Authority walls without sufficient sibling terminology context.
- **Gate:** Claim precision + link graph to triad/boundary pages.
- **Posture:** `needs_multilingual_governance_first` for DE row; claim gate for EN.

### `governance_methodology` (3 candidates)

- **Risk:** Governance pages published before editorial sign-off eligibility met.
- **Gate:** Source gate; some rows require `non_public_until_editorial_signoff`.
- **Posture:** `needs_source_gate_first`.

### `source_claim_governance` (2 candidates)

- **Risk:** Source governance pages referencing inactive registry as if authoritative.
- **Gate:** Source registry activation blocked until verified entries exist.
- **Posture:** `needs_source_gate_first`; `do_not_register_now` until registry has verified entries.

---

## Why dry-run planning does not approve execution

1. **`production_can_safely_proceed: no`** — L2 planner pre-flight and validation.
2. **58 missing drafts** — Wave 1 content debt unresolved.
3. **0 verified sources, 0 approved claims** — authority gates closed.
4. **9 candidates need human review** — secondary industrial-language tier.
5. **Publication/indexation/sitemap/navigation locks** — must remain LOCKED through planning.
6. **Sprint 5O-B charter** — planning-only; explicit prohibition on `routes.json` modification.

Dry-run output is input to a **future execution sprint** with separate authorization — not permission to register routes now.

---

## Related documents

- `ROUTE_REGISTRATION_WAVE_2_EXECUTION_BLOCKERS.md`
- `ROUTE_REGISTRATION_WAVE_2_CANDIDATE_MATRIX.md`
- `PRODUCTION_DRY_RUN_WAVE_PLANNING_REPORT.md`
