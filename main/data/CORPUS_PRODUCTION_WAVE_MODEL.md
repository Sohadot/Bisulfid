# Corpus Production Wave Model (Sprint 5H)

## Purpose

This document defines **how Bisulfid.com will actually produce** a **500-page sovereign launch cohort**—and continue toward **1,000+** and **3,000+** pages—without collapsing into thin content, translation spam, or fake publication readiness.

Small batches (5-page sprints, 20-page sprints) were **useful as governance tests** (Sprints 5E, 5G). They are **insufficient as the long-term production pace** for a 500-page minimum launch.

---

## Why small batches were only governance tests

| Batch size | Role | Limitation |
| --- | --- | --- |
| **3–5 pages** | Prove draft discipline, frontmatter, marker posture | Cannot build cluster depth or multilingual layers |
| **~20 pages** | Batch route planning or boundary review | Still far below launch threshold; risks one-off editorial inconsistency |
| **Ad hoc sprints** | Unblock specific routes | No repeatable wave rhythm; link graph lags |

**At 18 draft-backed routes today (post–5G),** the repository needs **wave-based production** with explicit sizes, sequences, and validation— not occasional micro-batches.

---

## Future production wave sizes

| Wave type | Recommended size | Output |
| --- | --- | --- |
| **Route planning / registration waves** | **80–120 routes** | New `planned` rows in `routes.json`; no publication |
| **Draft production waves** | **40–60 pages** | Non-public `content_file` bodies with markers |
| **Source mapping waves** | **40–60 pages** | Registry rows + marker resolution planning |
| **Claim-boundary waves** | **40–60 pages** | Boundary reports; claim scoping; no approval unless activation sprint |
| **Internal-link wiring waves** | **40–60 edges** | `internal_links.json` cluster slices; route_id only |
| **Validation waves** | **Full cohort sample + cluster audits** | Pre-launch link, SEO, metadata, technical/security checks |

Waves may **overlap in planning** but **must not skip sequence gates** (e.g., no public link wiring for unpublished targets).

---

## Production sequence (mandatory order per concept batch)

```
1. Route registration      → planned rows only; indexable/in_sitemap false
2. Draft creation          → non-public bodies; [SOURCE REQUIRED] where needed
3. Source mapping          → source_registry alignment; marker resolution plan
4. Claim boundary review   → forbidden-claim lists; required_claim_groups clarity
5. Internal-link architecture → cluster edges; no broken route_id targets
6. Metadata / SEO validation → title, description, H1, hreflang coherence
7. Technical / security validation → build, indexation guards, security checks
8. Pre-publication review  → Quality Gate; owner/editorial signoff
9. Launch                  → ONLY after ≥ 500 pages pass ALL gates
```

**Launch is step 9 only.** Steps 1–8 repeat in waves until the **500-page threshold** is met.

---

## Batch rules

1. **Vertical slices preferred:** Complete a **cluster** (e.g., DE terminology spine slice) before random horizontal stubs.
2. **One wave charter per sprint:** Each sprint declares wave type, size, and forbidden surfaces.
3. **No mixed wave types without explicit charter:** Do not register 100 routes and draft 60 pages in the same sprint unless charter allows both and validation covers both.
4. **Audit sample:** Every draft wave ends with **≥ 10% sampled** editorial audit (minimum 3 pages).
5. **Stop-the-line:** If audit finds marker stripping, thin pages, or claim drift—**halt wave** and fix before continuing.
6. **Registry discipline:** Route registration waves do **not** imply draft obligation in the same sprint.

---

## Quality gates (per wave)

| Gate | Applies to |
| --- | --- |
| Anti-thin structure | Draft production waves |
| Markers preserved until source-lock sprint | Draft production waves |
| No route publication | All waves until launch sprint |
| No indexable/in_sitemap true | All pre-launch waves |
| Source category match | Source mapping waves |
| Forbidden claim patterns documented | Claim-boundary waves |
| No dead route_id in internal_links | Link wiring waves |
| SEO metadata complete | Validation waves |
| Technical/security pass | Validation waves |

Full launch gates: `CORPUS_LAUNCH_THRESHOLD.md`.

---

## Rejected shortcuts

| Shortcut | Why rejected |
| --- | --- |
| Mass MT EN→DE/AR/ZH/JA | Translation spam; destroys multilingual authority |
| AI bulk generation without ontology | Generic glossary tone; unsourceable claims |
| Publish hub pages before spokes exist | Broken graph; fake readiness |
| Strip `[SOURCE REQUIRED]` for tone | Violates source governance |
| Approve claims to “ unblock ” drafts | Registry integrity collapse |
| Index partial cohort (< 500) | Violates no-publication-before-500 rule |
| Market data / CAGR / share in industrial pages | SOURCE_POLICY and launch drift |
| Safety handling copy in reference pages | Safety manual drift |
| 300-page “good enough” launch | Superseded by Sprint 5H — **500 minimum** |
| Horizontal 500 one-page stubs | Thin corpus; SEO failure with professional users |

---

## How to avoid mass AI spam

1. **Ontology-first:** Terminology pages tie to `sulfur_terms.json` workflow (when activated)—not free-form generation.
2. **Category templates:** Each corpus category has required sections (scope, boundaries, source posture, related terms).
3. **Human terminology editor sign-off** per wave sample and per language layer.
4. **Marker discipline:** Unresolved factual lines stay marked until source-mapping wave.
5. **Pruning:** Weak concepts dropped in planning waves—not patched at publication.
6. **Rate caps:** Do not exceed **40–60 draft pages per wave** without audit capacity.

---

## How to preserve sovereign-grade quality at scale

| Mechanism | Function |
| --- | --- |
| Wave sizing | Prevents editorial overload and inconsistent standards |
| Sequence gates | Source and claims before publication |
| Cluster completion | Internal links reflect real corpus structure |
| Multilingual independence | DE/AR/ZH/JA records authored under language discipline |
| Validation waves | Catch broken links, SEO gaps, security/indexation errors |
| Expansion model caps | 1,000 / 3,000 / 5,000+ only with audits (`CORPUS_EXPANSION_MODEL.md`) |
| Decision log + reports | Every wave leaves audit trail |

---

## Illustrative path to 500 pages (planning math)

| Phase | Waves (indicative) | Cumulative pages (indicative) |
| --- | --- | --- |
| Current state (post–5G) | — | **18** draft-backed routes |
| Route registration waves | ~4–5 × 80–120 routes | **500+** planned routes registered |
| Draft production waves | ~8–10 × 40–60 pages | **500** non-public drafts |
| Source mapping waves | ~8–10 × 40–60 pages | Markers resolved per page |
| Claim-boundary waves | ~8–10 reviews | Boundaries documented |
| Link wiring waves | ~8–10 cluster slices | Graph ready |
| Validation + launch | 1+ validation cycles | **≥ 500** public-eligible |

*Numbers are **planning estimates**; actual wave counts depend on blueprint priority and audit findings.*

---

## Relationship to other documents

- `FIVE_HUNDRED_PAGE_SOVEREIGN_LAUNCH_PROGRAM.md` — strategic thesis and layer allocation.
- `CORPUS_LAUNCH_THRESHOLD.md` — **500-page** launch gates.
- `CORPUS_ROUTE_BLUEPRINT_LAUNCH_COHORT.md` — **≥ 500** proposed concepts.
- `CORPUS_EXPANSION_MODEL.md` — post-launch scale horizons.

---

## Sprint 5H note

This model was **authored in Sprint 5H** as architecture-only documentation. **No** routes were published; **no** content was created; **no** registries were modified; **no** workflows or dependencies were added.

---

*Sprint 5H — production wave architecture. Execute in future chartered sprints only.*
