# Sovereign SEO, Internal Linking, and Security Model — Wave 1

**Sprint:** 6A  
**Scope:** Codified architecture for SEO, link graph, and technical/security requirements at 14,000-page scale

---

## SEO architecture

### Canonical rules

- One canonical URL per indexable route per language.
- Canonical derives from `routes.json` `path` + site base.
- Non-indexable drafts: no canonical in public output until indexation approved.
- Comparison pages (`PT_DIFFERENCE_COMPARISON`): canonical on comparison route, not duplicate term pages.

### hreflang rules

- `hreflang_group` links language alternates for the same dimensional subject.
- Implement `en`, `ar`, `de`, `fr`, `es`, `ja`, `zh`, and `x-default` (English institutional).
- hreflang only for routes with `indexation_posture: indexable_approved`.
- `PT_MULTILINGUAL_HUB` maintains alternate route maps.

### Title patterns

| Page type | Pattern (illustrative) |
| --- | --- |
| PT_TERM_CANONICAL | `{term} — terminology reference \| bisulfid.com` |
| PT_DIFFERENCE_COMPARISON | `{side_a} vs {side_b} — difference reference \| bisulfid.com` |
| PT_AUDIENCE_EXPLAINER | `{term} for {audience} — reference \| bisulfid.com` |
| PT_MULTILINGUAL_HUB | `{scope} — multilingual reference hub \| bisulfid.com` |

Titles must match route record `title`; validator checks alignment.

### Meta description rules

- Derived from route `description` field.
- Must state reference/governance posture for drafts.
- No unsupported factual claims in description.
- Comparison pages: state distinction intent, not conclusion without source.

### Sitemap index strategy

- **Phase 1 (pre-launch):** no public sitemap entries (`in_sitemap: false` globally).
- **Phase 2 (launch cohort):** sitemap index by language and page family.
- **Phase 3 (14k scale):** partitioned sitemaps (≤50k URLs each) by language layer.
- Governance pages (`PT_METHODOLOGY_GOVERNANCE`, `PT_CORPUS_STATUS`): `noindex_governance` default.

### robots / noindex logic

| Posture | robots |
| --- | --- |
| planned / draft / non_public | noindex, nofollow in any accidental public output |
| indexable_approved | index, follow |
| noindex_governance | noindex; may follow for internal discovery |

### Structured data model (6C+ design target)

- `WebPage` + `inLanguage` for reference pages.
- `DefinedTerm` or `Article` for terminology pages where schema fits claim boundary.
- Explicit `citation` / `isBasedOn` linking to source registry IDs.
- No structured data implying medical, safety, or market claims without sources.

---

## Internal-link architecture

### Hub types

| Hub | Role | page_type / cluster |
| --- | --- | --- |
| Language hubs | Entry per language layer | PT_MULTILINGUAL_HUB, language_hub |
| Term hubs | Terminology spine navigation | term_spine |
| Source hubs | Provenance clusters | source_cluster |
| Claim hubs | Claim boundary clusters | claim_cluster |
| Audience hubs | Audience explainer index | audience_cluster |
| Glossary hubs | Term cluster navigation | glossary_cluster |
| Comparison hubs | High-intent distinction index | comparison_cluster |
| AI-readable hubs | Machine reference index | ai_readable_cluster |
| Child-safe education hubs | Educational slice index | child_safe_cluster |

### Link rules

1. Every internal link uses `route_id`—no raw URL sprawl in content body.
2. Target `route_id` must exist in inventory (validator enforced).
3. Orphan routes forbidden (`orphan_forbidden` internal_link_role rejected).
4. Comparison pages must link to both side term pages and source/claim status where applicable.
5. Hub pages must link to ≥3 valid spokes or fail thin-hub gate.

### Graph validation (6E expansion)

- L2 `validate_internal_link_graph_plan_l2.py` baseline exists.
- 6E expands to full 14k inventory graph checks.

---

## Technical and security requirements

| Requirement | Rule |
| --- | --- |
| No broken links | Static validation on every cohort merge |
| Generated HTML validation | Build check before any public deploy |
| CSP / security posture | No regression in deployment config; charter-governed changes only |
| No external dependency drift | No new packages in architecture sprints |
| Validator coverage | No generated route without L0/L1 validator coverage plan |
| Publication accident prevention | Automation never sets indexable/published without gate |

---

## SEO priority: comparison intent

`PT_DIFFERENCE_COMPARISON` receives:

- Dedicated comparison hubs
- High-intent title/description patterns
- comparison_cluster internal links
- hreflang across languages for same comparison pair

This is core SEO architecture—not a blog afterthought.

---

## Current baseline

- 126 routes; all `planned`; none indexable.
- Internal link graph: partial (existing `internal_links.json`).
- Public HTML: none generated.
- Sitemap/navigation: LOCKED.

---

## Implementation sprints

| Sprint | SEO/link/security work |
| --- | --- |
| 6B | Inventory with hreflang_group and internal_link_role per row |
| 6C | Template and structured data schema |
| 6E | Full graph validation at scale |
| 6F | Controlled visibility and sitemap activation plan |
