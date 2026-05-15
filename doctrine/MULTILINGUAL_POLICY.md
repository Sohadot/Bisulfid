# MULTILINGUAL POLICY

This document governs language architecture and hreflang integrity for bisulfid.com.

It is subordinate to `ASSET_THESIS.md` and `PROJECT_DOCTRINE.md`.

---

## Language Priority

1. **English (EN)** — primary scientific, institutional, and global source layer.
2. **German (DE)** — core linguistic and industrial identity layer; Bisulfid is the German-form spelling; Germany is a major chemical-industry authority.
3. **Arabic (AR)** — first market-chain expansion layer; Gulf sulfur supply + Morocco phosphate-linked sulfur demand + real Arabic reference gap.
4. **Chinese (ZH)** — large-scale sulfur production and chemical-market layer.
5. **Japanese (JA)** — advanced chemical, materials, electronics, and industrial technology layer.
6. **French (FR)** — European industrial chemistry + TotalEnergies, Air Liquide, Morocco/OCP francophone relevance.
7. **Spanish (ES)** — Spain and Latin America public, educational, and industrial expansion layer.

Language priority is recorded in: `main/data/languages.json`

---

## Why German Has Identity Priority

German is not only a translation layer. German is the asset's linguistic and industrial identity layer.

The name Bisulfid derives its conceptual force from German chemical compression:

- Oxide → Oxid
- Chloride → Chlorid
- Sulfide → Sulfid
- Bisulfide → Bisulfid

Germany is a major chemical-industry center. The German layer gives bisulfid.com buyer relevance in specialty chemicals, industrial terminology, sulfur derivatives, technical translation, and European chemical authority.

---

## Why Arabic Has Market-Chain Priority

Arabic is not a secondary cultural layer. Arabic is the first market-chain expansion layer.

The Arabic layer matters because the sulfur supply chain connects two strategic Arabic-speaking poles:

- Gulf sulfur supply relevance (oil, gas, refining, sour-gas processing)
- Morocco phosphate-linked sulfur demand (phosphate and fertilizer production)

This creates a real Arabic reference gap for engineers, procurement teams, students, researchers, and industrial readers.

Arabic pages must be governed reference pages with controlled bilingual terminology. They must not be low-quality translations.

---

## Launch Rules

- No language launches until complete.
- A partial language is not a launched language.
- A machine-translated page is not a published reference page.
- Every language must increase at least one of: public reference value, scientific clarity, industrial buyer logic, safety understanding, terminology authority, or strategic acquisition value.

---

## hreflang Rules

Every multilingual page must implement:

- Correct `hreflang` attributes for all published language versions.
- Self-referencing `hreflang` tag.
- `x-default` hreflang pointing to English.
- All `hreflang` targets must resolve to live, published pages.

Unpublished languages do not appear in `hreflang` tags or sitemaps.

---

## Content Integrity Rules

A translated page fails multilingual integrity if:

- `hreflang` targets do not resolve.
- HTML `lang` attribute is incorrect.
- Arabic pages do not use `dir="rtl"`.
- Alternate routes point to unpublished pages.
- Translated pages introduce unapproved claims.
- Translated pages remove required disclaimers.
- Translated pages weaken safety restrictions.
- Language sitemap sections contain draft URLs.
- Translated content is partial, placeholder, or unreviewed machine output.

---

## Terminology Governance

All language layers must use the governed terminology from:

`main/data/ontology/sulfur_terms.json`

No language layer may introduce alternative spellings or translations not approved in the ontology.

---

## Safety Restrictions Across All Languages

All languages must carry equivalent safety restrictions. No language version may:

- Publish handling instructions.
- Publish dosage advice.
- Present safety thresholds as prescriptive advice.
- Make medical or therapeutic claims.

Safety restrictions may not be weakened in any translated layer.

---

## Sitemap Governance

- Language sitemap sections must not contain draft URLs.
- Alternate language routes are registered before publication.
- Unpublished languages do not appear in `hreflang` tags or sitemaps.

Validated by: `validate_hreflang.py`, `validate_language_routes.py`, `validate_translations.py`
