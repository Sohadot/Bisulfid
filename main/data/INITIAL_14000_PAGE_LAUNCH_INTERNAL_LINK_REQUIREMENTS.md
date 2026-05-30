# Initial 14,000-Page Launch Internal Link Requirements

**Sprint:** 6G  
**Date:** 2026-05-30  
**Posture:** Link density and graph discipline at launch scale

---

## Purpose

Define minimum internal-link requirements so 14,000 pages form a **coherent sovereign reference graph** — not orphaned doorway pages or SEO dilution clusters.

Aligned with: `CORPUS_PRODUCTION_LINK_GRAPH_MODEL.md`, `SOVEREIGN_FOUNDATION_COHORT_01_INTERNAL_LINK_GRAPH.md`, `SOVEREIGN_SEO_INTERNAL_LINKING_SECURITY_MODEL_WAVE_1.md`.

---

## Universal link rules

| Rule | Requirement |
| --- | --- |
| Orphan prevention | Every launch page has **≥ 1 inbound** required edge |
| Hub anchor | Every cycle includes a Tier-0/1 hub in shortest path |
| route_id binding | All planning edges use `route_id` — not raw URLs |
| Unpublished discipline | No live markdown links until indexation charter |
| Broken-link block | All `required_internal_links` targets must exist in registry |
| Cross-cohort links | Target must be registered before source page indexation |

---

## Minimum required links by page family

| page_type_id | Min outbound required | Min inbound required | Primary link role |
| --- | ---: | ---: | --- |
| PT_FOUNDATION | 3 | 1 | language_hub |
| PT_METHODOLOGY_GOVERNANCE | 2 | 2 | governance spine |
| PT_TERM_CANONICAL | 2 | 1 | term_spine |
| PT_DIFFERENCE_COMPARISON | 3 | 1 | comparison_cluster |
| PT_AUDIENCE_EXPLAINER | 2 | 1 | audience_cluster |
| PT_MULTILINGUAL_EQUIV | 2 | 1 | language_hub |
| PT_MULTILINGUAL_HUB | 5 | 1 | language_hub |
| PT_COMPOUND_ENTITY | 2 | 1 | term_spine |
| PT_GLOSSARY_CLUSTER | 4 | 1 | glossary_cluster |
| PT_CHILD_SAFE_EDU | 2 | 1 | child_safe_cluster |
| PT_AI_READABLE | 2 | 1 | ai_readable_cluster |
| PT_SOURCE_BOUND | 2 | 1 | source_cluster |
| PT_CLAIM_BOUNDARY | 2 | 1 | claim_cluster |
| PT_SOURCE_STATUS | 2 | 1 | source_cluster |
| PT_CLAIM_STATUS | 2 | 1 | claim_cluster |
| PT_CORPUS_STATUS | 2 | 1 | status hub |
| PT_GOVERNMENT_POLICY | 2 | 1 | audience_cluster |
| PT_INVESTOR_ECONOMIC | 2 | 1 | audience_cluster |
| PT_COMPANY_INDUSTRY | 2 | 1 | audience_cluster |

---

## Hub hierarchy (launch graph)

### Tier 0 — Site entry hubs (per language)

- Language home / sovereign intro equivalent
- Multilingual map hub (PT_MULTILINGUAL_HUB)

### Tier 1 — Spine hubs

- Terminology spine hub (glossary_cluster root)
- Comparison cluster index
- Foundation / governance root (COHORT_01: `en_foundation_sovereign_intro`)

### Tier 2 — Cluster hubs

- Source cluster hub
- Claim cluster hub
- Audience cluster index per major audience
- AI-readable index
- Child-safe education index

### Tier 3 — Record pages

- Term canonical, compound entity, audience explainer, comparison pages

---

## Link density targets (launch corpus)

| Graph zone | Pages (approx) | Avg required edges per page | Max optional edges |
| --- | ---: | ---: | ---: |
| Foundation / governance | 700 | 3 | 2 |
| Terminology spine | 2,800 | 3 | 3 |
| Comparison cluster | 1,400 | 4 | 2 |
| Audience explainers | 2,450 | 3 | 2 |
| Multilingual layer | 1,050 | 4 | 3 |
| Source / claim | 1,400 | 3 | 1 |
| Compound / entity | 1,400 | 3 | 2 |
| Glossary / clusters | 1,400 | 5 | 2 |
| Government / economic | 1,400 | 2 | 1 |
| Child-safe / AI-readable | 1,400 | 3 | 2 |

**Total required edges (estimate):** ~42,000 planning edges across 14,000 pages (~3.0 avg).

---

## Per-cohort link requirements

| Cohort | Link requirement before next cohort |
| --- | --- |
| COHORT_01 | Foundation graph complete (0 orphans) — **done** |
| COHORT_02 | Each term links to glossary hub + foundation methodology |
| COHORT_03 | Each comparison links to both term records + comparison hub |
| COHORT_04 | hreflang_group edges planned; no live cross-lang links until validated |
| COHORT_05 | Each explainer links to term spine + audience hub |
| COHORT_06 | reference_layer siblings cross-linked where anti-duplication allows |
| COHORT_07 | Compound pages link to term spine + compound cluster |
| COHORT_08 | Status pages link to governance spine + registry object |
| COHORT_09–10 | Language hub links to EN institutional equivalent |

---

## Prohibited link patterns (14k scale)

- Unpublished routes as public navigation targets
- Terminology pages presented as resolved without source
- Market/safety/procurement URLs in body
- Doorway loops without hub anchor
- Cross-language equivalence without hreflang_group
- Link farms (>8 outbound required edges without hub justification)

---

## SEO dilution prevention

1. **Cluster coherence:** Pages index only within validated cluster (terminology, comparison, audience).
2. **Canonical discipline:** One canonical URL per indexable route per language.
3. **noindex_governance:** Governance pages never compete with terminology SERP targets.
4. **Comparison canonical:** Comparison route canonical — not duplicate term pages.
5. **Partitioned sitemaps:** By language and page family — not single 14k flat sitemap.

---

## Validation at scale

- **Pre-registration:** Orphan audit on cohort subgraph
- **Pre-indexation:** Full edge consistency vs `routes.json` required_internal_links
- **Post-render (future):** HTML link checker on public cohort only

---

*Sprint 6G — Launch Internal Link Requirements*
