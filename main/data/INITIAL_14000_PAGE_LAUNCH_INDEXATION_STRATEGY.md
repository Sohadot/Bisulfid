# Initial 14,000-Page Launch Indexation Strategy

**Sprint:** 6G  
**Date:** 2026-05-30  
**Posture:** Controlled indexation plan — **no activation in Sprint 6G**

---

## Principle

**No public indexation before validation.** All 14,000 launch pages begin as `non_indexable` / `noindex_default`. Indexation is a **launch gate**, not a generation default.

Current state: **141 routes, 0 indexable** — unchanged by this charter.

---

## Indexation state model (launch)

| indexation_state | Meaning | Launch default |
| --- | --- | --- |
| `noindex_default` | Draft / pre-launch | **Yes** — all new inventory |
| `noindex_governance` | Governance pages — noindex even post-launch | Foundation, methodology, status |
| `indexation_candidate` | Gates nearly satisfied; awaiting charter | Terminology, comparison (after validation) |
| `indexation_approved` | Owner launch charter only | None until launch sprint |
| `indexation_blocked` | Missing source/claim/link gates | Unresolved factual pages |

---

## Pre-launch phase (current → inventory complete)

| Control | Setting |
| --- | --- |
| `indexable` | **false** on all routes |
| `in_sitemap` | **false** |
| `in_navigation` | **false** |
| robots (if any accidental output) | noindex, nofollow |
| hreflang tags | **Not emitted** |
| sitemap files | **Not created** |

---

## Launch gate requirements (before any indexation)

All must pass for a page to become `indexation_candidate`:

1. **G0–G7** validation gates pass
2. **Knowledge reliability profile** complete
3. **Source posture** ≥ source_verified for factual pages
4. **Claim posture** ≥ claim_approved_narrow for registered claims
5. **Internal links:** all `required_internal_links` targets registered
6. **Orphan audit:** zero orphans in cluster
7. **Human sample audit:** ≥10% cohort review pass
8. **Launch charter:** explicit owner approval for indexation wave
9. **`production_can_safely_proceed`:** evaluated — not assumed yes at 14k registration

---

## Controlled indexation rollout (post-gate)

### Wave I — English core SEO (estimated 600–800 pages)

| Page family | Indexation eligible | Condition |
| --- | --- | --- |
| PT_DIFFERENCE_COMPARISON | Candidate | Source + claim gates + comparison validation |
| PT_TERM_CANONICAL | Candidate | Source_locked or verified + narrow claim approval |
| PT_MULTILINGUAL_EQUIV | Candidate | hreflang alternates validated |

**Not in Wave I:** governance, status, unresolved `[SOURCE REQUIRED]` pages.

### Wave II — English audience + compound (estimated 1,000–1,500 pages)

| Page family | Indexation eligible | Condition |
| --- | --- | --- |
| PT_AUDIENCE_EXPLAINER | Candidate | Per-audience claim boundary pass |
| PT_COMPOUND_ENTITY | Candidate | Source verified |
| PT_GLOSSARY_CLUSTER | Candidate | Hub coherence validated |

### Wave III — Multilingual (estimated 4,000+ pages)

- Index only when **both** EN institutional page and language alternate validated
- hreflang_group complete for theme
- x-default → English institutional path

### Wave IV — Remainder + gap fill

- Government / economic pages: **only** with REF_ECONOMIC source_verified
- Child-safe: educational review gate
- AI-readable: structured provenance validated

---

## Permanent noindex classes (even after launch)

| Class | Reason |
| --- | --- |
| PT_METHODOLOGY_GOVERNANCE | noindex_governance doctrine |
| PT_CORPUS_STATUS | Status / lock posture — not SERP targets |
| PT_SOURCE_STATUS / PT_CLAIM_STATUS | Registry state pages |
| COHORT_01 foundation (until charter override) | Institutional governance |
| Any page with `source_required_unresolved` | Unresolved evidence |
| Any page with forbidden claim class content | Policy violation |
| AUD_CHILD_EDU with handling risk | Child-safe policy |
| Draft / planned routes | Until publication charter |

---

## Sitemap strategy (not activated)

| Phase | Strategy |
| --- | --- |
| Pre-launch | No sitemap entries |
| Launch Wave I | `sitemap-en-core.xml` — comparison + verified terminology only |
| Launch Wave II | `sitemap-en-audience.xml`, `sitemap-en-compound.xml` |
| Launch Wave III | Per-language partitioned sitemaps (`sitemap-de.xml`, etc.) |
| 14k full | Sitemap index; ≤50k URLs per file; by language partition |

**Governance pages excluded** from all sitemaps by default.

---

## Navigation strategy (not activated)

| Slot | Eligible routes | Activation |
| --- | --- | --- |
| Foundation strip | COHORT_01 (post-charter) | Deferred |
| Terminology nav | PT_TERM_CANONICAL hubs | Launch Wave I |
| Comparison nav | PT_DIFFERENCE_COMPARISON index | Launch Wave I |
| Governance footer | Status pages only | noindex; optional footer links |

---

## robots / canonical rules

- **Canonical:** One per indexable route from `routes.json` path
- **Non-indexable drafts:** No canonical in public output
- **Comparison pages:** Canonical on comparison route
- **hreflang:** Only for `indexation_approved` routes with complete alternates

---

## SEO dilution controls

1. Staged indexation — not 14,000 pages at once
2. noindex_governance for non-SERP pages
3. Cluster-scoped sitemaps
4. Comparison canonical discipline
5. No indexation of thin or duplicate reference_layer siblings
6. Launch metrics gate: index only pages with L3+ reliability minimum

---

## Sprint 6G posture

| Action | Status |
| --- | --- |
| Indexation strategy defined | **Yes** |
| indexable set true | **No** |
| Sitemap activated | **No** |
| Navigation activated | **No** |
| routes.json modified | **No** |

---

*Sprint 6G — Launch Indexation Strategy*
