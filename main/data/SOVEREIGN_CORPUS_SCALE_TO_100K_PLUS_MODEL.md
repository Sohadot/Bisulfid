# Sovereign Corpus Scale to 100K+ Model

**Sprint:** 6G  
**Date:** 2026-05-30  
**Scope:** Architecture for scaling beyond 14,000 pages to 100,000+ and 300,000+ governed reference pages

---

## Scale phases

| Phase | Page target | Purpose |
| --- | ---: | --- |
| **Launch minimum** | **14,000** | Initial sovereign multilingual reference corpus |
| **Phase 2 expansion** | **100,000** | Deep terminology, compound, audience, and multilingual coverage |
| **Phase 3 expansion** | **300,000+** | Full dimensional matrix + regional and specialty layers |

Each phase reuses the same dimensional architecture — **no architectural rewrite**.

---

## Why 14k is minimum, not maximum

Bisulfid.com is **sovereign reference infrastructure**. The launch corpus establishes:

- 7 language layers × 2,000 pages = institutional credibility floor
- Full page-family and reference-layer coverage at seed depth
- Validator and automation pipeline proven at cohort scale

Expansion adds **depth** (more entities, more intersections) — not a different product.

---

## Architectural invariants (all scales)

1. **Registry-constrained generation** — no LLM free-form at any scale
2. **Dimensional intersection** — reject Cartesian inflation
3. **reference_layer anti-duplication** — distinct purpose per page
4. **Hub-spoke link graph** — orphan forbidden at all scales
5. **Source/claim posture on every route** — epistemic transparency
6. **Knowledge reliability profile** — required on every page
7. **Cohort-wave validation** — G0–G7 + human sample audit
8. **Partitioned registries** — master inventory separate from production routes.json

---

## Registry partitioning (100k+)

| Artifact | 14k launch | 100k+ scale |
| --- | --- | --- |
| `corpus_master_inventory.json` | Single partition | **Language × page_family partitions** |
| `routes.json` | 141 → ~14k merge waves | **Merge charters per wave** — never bulk auto-write |
| `internal_links.json` | Planning edges per cohort | **Partitioned edge stores** by cluster |
| Sitemaps | None → language partitions | **Sitemap index + ≤50k URL files** |
| Validators | L1/L2 runtime | **Partition-scoped validation** + aggregate runtime |

---

## Throughput at scale

| Scale | Draft pages/day | Cohort wave size | Validation model |
| --- | ---: | ---: | --- |
| 14k build | 100 → 500 | 500–2,000 | Full L1/L2 per wave |
| 100k expansion | 500 | 2,000–5,000 | Partition validators + sample audit |
| 300k expansion | 500–1,000 | 5,000–10,000 | Automated G0–G5; human G6–G7 sample |

Automation engine lineage: Content Automation Engine v1 → sovereign_corpus_generator_v2 (future) with same registry read-only inputs.

---

## Link graph at scale

### Problem

100k+ pages risk: link decay, orphan proliferation, SEO dilution, hub collapse.

### Solution

| Mechanism | Implementation |
| --- | --- |
| **Hub depth limit** | Max 3 hops from Tier-0 hub to record page |
| **Cluster boundaries** | Terminology, comparison, audience clusters isolated |
| **Partitioned link validation** | Validate subgraph per cohort before merge |
| **Broken-link CI** | Rendered HTML checker on public partitions only |
| **Link budget** | Max 8 required outbound edges per page (exceptions: hubs) |
| **Stale edge retirement** | Deprecation charter for removed route_id targets |

---

## SEO at scale

| Risk | Mitigation |
| --- | --- |
| Thin content dilution | Family minimum quality thresholds (6G) |
| Duplicate reference_layer pages | Anti-duplication hash rule (6B) |
| Doorway clusters | Hub anchor + orphan prevention |
| Sitemap bloat | Language × family partitioned sitemaps |
| hreflang errors | Index only complete alternate groups |
| Governance SERP competition | Permanent noindex_governance class |

---

## Source/claim at scale

| Scale | Source registry | Claim registry |
| --- | --- | --- |
| 14k | Incremental verification waves | Narrow approval batches |
| 100k | Partitioned source stores by domain | Claim class registries per ontology slice |
| 300k | Automated bibliographic intake + human verify | Claim boundary automation with human escalation |

**Invariant:** No page indexation without posture ≥ source_verified + claim_approved_narrow for factual content.

---

## Language expansion at scale

| Phase | Languages | Notes |
| --- | --- | --- |
| Launch | 7 | 2,000 each |
| 100k | 7 + specialty locales (future registry) | Depth per language |
| 300k | Extended locale registry | New languages via registry charter only |

Cross-language links require hreflang_group + verified terminology governance — never automatic MT equivalence.

---

## Governance failure modes (prevented)

| Failure | Prevention |
| --- | --- |
| Architectural collapse | Partitioned inventory; no monolithic routes.json |
| Validator weakening | Charter forbids weakening; new gates additive only |
| Fake pages | Registry intersection reject |
| Thin pages | Family word/section minimums |
| Link decay | Partitioned link validation + CI |
| SEO dilution | Staged indexation + noindex_governance |
| Epistemic overreach | Reliability profile + evidence grade on every page |

---

## Milestone map

```text
14,000  ──► Launch gate (validated indexation Wave I–IV)
100,000 ──► Deep corpus (terminology + compound + audience saturation)
300,000+ ──► Full sovereign reference matrix (specialty + regional expansion)
```

---

## Relation to Sprint 6G charter

This model ensures the **14,000-page launch corpus** is the **foundation slab** — not a ceiling. COHORT_01 (15 pages) → COHORT_02 (500–1,000) → … → 14,000 → 100,000+ uses the same engines, registries, and validators.

---

*Sprint 6G — Sovereign Corpus Scale Model*
