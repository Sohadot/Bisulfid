---
route_id: internal_linking_discipline
status: draft
publication_status: non_public
indexable: false
in_sitemap: false
language: en
locale: en
source_language: en
---

# Internal linking discipline (non-public draft)

**Draft status:** This page is a **non-public draft**. It is **not published**, **not indexable**, **not in the sitemap**, **not approved for public use**, and **not publication-ready**. It is intended for **draft review** by editors building the sovereign reference corpus.

## Internal links as governance infrastructure

Internal links are **not decoration**. In this corpus model, they are part of **governance infrastructure**: they express which `route_id` targets participate in hub, spine, and disambiguation roles. A link pattern that treats internal routes as “just URLs” invites **broken mental models** and **thin networks** that weaken authority.

## Route_id-based discipline

Editors should conceptualize links as **route_id → route_id** relationships to be realized later through the governed graph (for example `internal_links.json`). This draft **does not** modify `internal_links.json`. Sprint 5E intentionally leaves that registry unchanged until linking batches are executed with explicit governance.

## Why unpublished-route assumptions are dangerous

Assuming a target is live because a `route_id` exists or a draft file exists is **unsafe**. **Planned** routes remain non-public until route state, sources, claims, and Quality Gate conditions say otherwise. This draft uses **plain text `route_id` mentions only**—no markdown hyperlinks, no raw URLs, and no behavior that implies publication.

## Hub, spine, and support relationships

- **Hubs** gather authoritative entry surfaces (for example compound-family gateways when those pages are eligible).
- **Spines** are dense, repeatable terminology sequences that should not devolve into list-only glossaries.
- **Support** pages supply boundaries and governance context (methodology, quality gate, sources posture).

Links should appear when the **target’s corpus role** is defined and the link density rule passes editorial review—not to inflate outbound counts.

## Broken links and thin networks

Broken or aspirational links (targets not yet eligible) erode trust. Thin networks—many pages with few meaningful edges—simulate coverage without sovereign depth. Both are rejected in draft review.

## Relationship to other route_ids (references only)

Illustrative `route_id` relationships for future linking work:

- `glossary`
- `sulfur_compounds`
- `german_english_chemical_terms`
- `corpus_methodology_overview`
- `quality_gate_public_explainer`

[SOURCE REQUIRED] Future iterations may cite doctrine on link density; this draft does not claim source-locking is complete.

This sprint **did not** modify `internal_links.json`, **did not** create live links, and **does not** assume any route is published.
