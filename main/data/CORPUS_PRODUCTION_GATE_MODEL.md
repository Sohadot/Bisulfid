# Corpus Production Gate Model — Layer 2

**Sprint:** 5O-A  
**Date:** 2026-05-29

---

## Purpose

Define **production gates** that must pass before corpus scale-up and before any route becomes public. Gates are **sequential** and **non-bypassable** by automation.

---

## Route gate

- Route exists in `routes.json` with complete metadata
- `status: planned` until Quality Gate passes
- `indexable: false`, `in_sitemap: false`, `in_navigation: false` until authorized
- `route_id` unique and stable

---

## Draft gate

- `content_file` exists for draft-backed routes
- Frontmatter: `status: draft`, `publication_status: non_public`
- `[SOURCE REQUIRED]` markers preserved where factual lines are open
- No thin placeholder bodies; no generic AI glossary pages
- Anti-thin-content and anti-generic-content rules enforced

---

## Source gate

- Factual claims require verified `source_registry.json` entries per `SOURCE_POLICY.md`
- No source entry = no published claim
- Source mapping precedes marker satisfaction audits
- Registry remains **inactive** until execution sprint chartered
- **0** invented bibliographic details

---

## Claim gate

- Claim registries **inactive** until governed activation
- **0** `status: approved` without verified source linkage
- `required_claim_groups` satisfied before publication
- Claim boundary reports precede activation

---

## Internal link gate

- Internal link planning **required before publication**
- No public route publication-ready **without** internal link role in cluster
- `route_id` references preferred in planning stages
- No broken public links; no plan assumes unpublished routes are live links
- Hub, terminology record, disambiguation, source/governance, multilingual map, and index pages covered

---

## SEO metadata gate

- Title, description, H1 validated per route before publication
- Canonical discipline documented
- Anti-thin SEO rules enforced
- Route count is **not** treated as SEO quality

---

## Multilingual gate

- Multilingual pages are **controlled terminology records**, not simple translations
- hreflang and translation registry planning before multilingual publication
- ar/zh/ja expansion **deferred** until source, hreflang, and terminology governance ready
- Anti-translation-spam rules enforced

---

## Sitemap gate

- **Sitemap lock** — no `in_sitemap: true` before publication gates
- `sitemap_policy.json` remains inactive/planned until launch authorization
- No active sitemap URLs pre-launch

---

## Indexation gate

- **Indexation lock** — no `indexable: true` before publication gates
- noindex rules apply to all pre-launch routes
- Search console readiness documented before launch indexation sequence

---

## Technical/security gate

- Build validation passes
- No unauthorized indexation toggles
- No generated public HTML until all gates pass for launch cohort
- Security regression checks before publication waves

---

## Publication gate

- **Minimum 500 governed pages** pass **all** gates in `CORPUS_LAUNCH_THRESHOLD.md`
- No public launch below **500** governed pages
- Quality Gate + editorial signoff
- Page count is **not** more important than authority

---

## Rollback gate

- Any gate failure triggers rollback review — not silent bypass
- Published routes with broken sources/claims removed until remediated
- Audit trail required for publication authorization reversals

---

## Audit gate

- Every production wave produces validation report
- L1 corpus runtime + source/claim guardrail + L2 production runtime before merge
- Human review for registry, claim, and publication actions

---

*Sprint 5O-A — Corpus Production Gate Model Layer 2*
