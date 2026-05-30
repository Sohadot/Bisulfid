# Sovereign Route Inventory — No Publication Guardrail — Wave 1

**Sprint:** 6B  
**Posture:** Master inventory model only — all publication locks unchanged

---

## Sprint boundary

| Action | Performed? |
| --- | --- |
| Master inventory schema created | **Yes** |
| Generation matrix created | **Yes** |
| reference_layer registry created | **Yes** |
| `routes.json` modified | **No** |
| Route publication | **No** |
| Content pages created | **No** |
| Public HTML generated | **No** |
| `indexable: true` | **No** |
| `in_sitemap: true` | **No** |
| `in_navigation: true` | **No** |
| Fake / placeholder public pages | **No** |
| `[SOURCE REQUIRED]` marker removal | **No** |
| Source-lock / claim approval / new sources | **No** |

---

## Inventory vs production separation

| Layer | File | 6B status |
| --- | --- | --- |
| Production routes | `main/data/routes.json` | **126 rows — unchanged** |
| Master inventory model | Schema + matrix (future `corpus_master_inventory.json`) | **Model defined; rows not emitted** |
| `production_route_registry` | Schema field | **Must remain `false`** until merge charter |

---

## Anti-fake page guardrails

1. **Data completeness** — No public route without required schema fields.
2. **Source/claim eligibility** — No indexation without verified source + approved claim where required.
3. **Sitemap/navigation** — Blocked until publication gates clear.
4. **Shallow duplication** — reference_layer must differentiate purpose; anti_duplication_rule enforced.
5. **Comparison safety** — PT_DIFFERENCE_COMPARISON requires comparison_reference_mode + both sides sourced.
6. **Economic/logistical layers** — No unsupported market, procurement, transport, or handling claims.
7. **Free LLM generation** — Forbidden as production method.

---

## Route and indexation state defaults

| Field | Default for all inventory rows |
| --- | --- |
| `route_state` | `inventory_planned` or `publication_blocked` |
| `indexation_state` | `noindex_default` |
| `indexable` | **false** |
| `in_sitemap` | **false** |
| `in_navigation` | **false** |
| `status` (inventory) | `inventory_planned` |

---

## Locked gates (unchanged)

| Gate | Status |
| --- | --- |
| Route publication | **LOCKED** |
| Indexation | **LOCKED** |
| Sitemap | **LOCKED** |
| Navigation | **LOCKED** |
| `production_can_safely_proceed` | **no** |
| Source registry file | **inactive** |
| Claim registries | **inactive** |

---

## Explicit non-claims

This sprint does **not** claim:

- 14,000 routes exist in production
- Master inventory rows are generated (model only in 6B)
- Corpus is publication-ready
- Reference layers are populated with content
- Any route is indexable or public

---

## Validator posture

Existing L0/L1/L2 validators **unchanged**. No weakening. Schema and matrix are documentation/model files — not consumed by validators until 6C+ integration charter.

---

## Merge policy for future inventory → routes.json

Requires separate charter with:

- Duplicate path check against 126 existing routes
- Batch validator pass
- Owner DECISION_LOG entry
- `production_route_registry: true` only after review
