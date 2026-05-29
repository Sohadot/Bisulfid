# Corpus Production Link Graph Model — Layer 2

**Sprint:** 5O-A  
**Date:** 2026-05-29

---

## Purpose

Define internal link graph discipline for sovereign-scale production — protecting link integrity, cluster coherence, and publication safety.

---

## Hub-to-record linking

- Gateway and terminology **hubs** link to **terminology records** by `route_id`
- Hubs do not deep-link to unpublished targets as if public
- Each hub documents cluster scope in planning metadata

---

## Record-to-disambiguation linking

- Terminology records link to **disambiguation pages** where homonym or scope collision exists
- Disambiguation edges are bidirectional in planning graph where appropriate
- No disambiguation page without inbound hub or record context

---

## Disambiguation-to-source linking

- Disambiguation pages may link to **source/governance** and methodology pages
- Source pages explain evidence posture — not live bibliographic dumps in planning docs
- Governance-to-methodology linking documents claim/source doctrine paths

---

## Source/governance-to-methodology linking

- Source policy, claim boundary, and methodology pages form governance spine
- Links use `route_id` names in drafts; markdown links only when targets are authorized public

---

## Multilingual map linking

- hreflang groups connect controlled records across languages
- Multilingual map pages index language-layer entry points
- No automatic cross-language equivalence links without verified terminology governance

---

## Index/map pages

- Index and map routes aggregate cluster navigation
- Index pages must not orphan terminology records
- Map pages document planned edges — not fabricated live URLs

---

## Forbidden link patterns

- Links to unpublished routes presented as public navigation
- Broken public links to missing `route_id` targets
- Raw external URLs in draft planning where policy forbids
- Market, safety, procurement, or acquisition-target framing via link context
- SEO doorway pages with link farms

---

## Unpublished route link discipline

- **Unpublished routes are not live links** in public output
- Planning graph may reference `route_id` for future wiring
- Validators must reject plans treating unpublished routes as public href targets
- Publication-ready requires internal link role satisfied — **not** optional

---

## Broken-link prevention

- Pre-publication link graph validation required
- Every required internal link target must exist as route + (when draft-backed) content file
- Cluster audits before publication readiness waves
- Anti-broken-link enforcement is merge-blocking for publication sprints

---

## Future link graph validation rules

- L2: planning document and policy validation (this sprint)
- L3: automated edge consistency against `internal_links.json` + `routes.json`
- L4: rendered HTML link checker against public cohort only post-launch authorization

---

*Sprint 5O-A — Corpus Production Link Graph Model Layer 2*
