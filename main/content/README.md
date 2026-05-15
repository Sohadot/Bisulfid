# Content Directory

This directory contains the governed multilingual content for bisulfid.com.

## Content presence does not mean publication

A content file may exist in this directory and remain completely non-public.
Public publication is controlled exclusively by `main/data/routes.json`.

A page is not published until all of the following are true in `routes.json`:

- `status: published`
- `indexable: true`
- `in_sitemap: true`
- All 11 Quality Gate conditions have passed

Do not treat the presence of a file in this directory as evidence that it is live, indexed, or publicly accessible.

---

## Directory Structure

Each language directory contains three subdirectories:

- `pages/` — full reference pages mapped to routes in `main/data/routes.json`
- `term-records/` — individual term definitions and ontology-linked records
- `fragments/` — reusable content fragments: introductions, summaries, shared blocks

Shared content lives under `main/content/shared/`:

- `canonical-claims/` — canonical factual claim texts referenced by the claim registry
- `disclaimers/` — editorial, safety, translation, sponsorship, and acquisition disclaimers
- `source-notes/` — source attribution notes for inclusion in published pages

---

## Language Layers

1. **English (EN)** — source layer. All factual claims originate in English and are verified against the source registry before translation.
2. **German (DE)** — identity layer. The linguistic and industrial identity of the asset. German content is not merely a translation of English; it is a governed reference layer with its own cultural and industrial authority.
3. **Arabic (AR)** — first market-chain layer. Arabic content must preserve controlled bilingual scientific terminology, use RTL layout (`dir="rtl"`), and be reviewed independently against the claim registry.
4. **Chinese (ZH)** — structured expansion layer.
5. **Japanese (JA)** — structured expansion layer.
6. **French (FR)** — structured expansion layer.
7. **Spanish (ES)** — structured expansion layer.

---

## Governing Rules

- Translated content may not introduce claims absent from the claim registry (`main/data/claims/`).
- Arabic content must preserve controlled bilingual scientific terminology and RTL requirements.
- No placeholder content may be used as published content.
- No machine-translated content may be published without human review.
- Shared disclaimers and source notes live under `main/content/shared/`.
- Generated output in `site/` must never be edited manually.
- Content files in this directory do not activate routes, navigation, or sitemap entries.

---

**Governed by:** `doctrine/PROJECT_DOCTRINE.md`, `doctrine/MULTILINGUAL_POLICY.md`
**Route registry:** `main/data/routes.json`
**Claim registry:** `main/data/claims/`
**Source registry:** `main/data/sources/source_registry.json`
