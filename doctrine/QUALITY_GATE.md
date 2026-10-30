# QUALITY GATE

This document defines the launch conditions for bisulfid.com.

It is subordinate to `ASSET_THESIS.md` and `PROJECT_DOCTRINE.md`.

---

## Core Rule

> One gate fails = no deployment.
> No partial launches.
> No "we will fix it after."

Gates are conditions, not goals.

---

## The 12 Gates

### Gate 01 — Internal Links

Zero broken internal links.

All internal links resolve to published, live pages. No link targets a draft, redirect-only, or removed page.

Validator: `validate_links.py`

### Gate 02 — Content Completeness

Zero placeholder content.

No lorem ipsum. No "[content coming soon]". No stub pages in navigation or sitemap.

Validator: `validate_content.py`

### Gate 03 — Navigation Integrity

Zero draft pages in sitemap or navigation.

All pages accessible from navigation or sitemap are complete and published.

Validator: `validate_routes.py`

### Gate 04 — Source Coverage

Zero unsourced published claims.

Every factual claim on every page has a verified entry in the source registry.

Validator: `validate_sources.py`, `validate_claims.py`

### Gate 05 — SEO Integrity

Zero SEO violations.

All pages have canonical tags, correct meta descriptions, and valid structured data. No duplicate content. No thin pages in the sitemap.

Validator: `validate_seo.py` (placeholder). Duplicate and thin content are enforced by Gate 12.

### Gate 06 — Security Policy

Zero security policy violations.

CSP headers are in place. No inline JavaScript in production. No secrets in the repository. No unverified external scripts.

Validator: `validate_security.py`

### Gate 07 — Accessibility

Zero critical accessibility violations.

WCAG 2.1 AA minimum. All images have alt text. All interactive elements are keyboard-accessible.

Validator: `validate_accessibility.py`

### Gate 08 — Orphan Pages

Zero orphaned pages.

Every published page is reachable from at least one other published page via internal link.

Validator: `validate_links.py`

### Gate 09 — Content Standards

All pages meet minimum content standards as defined in `doctrine/GLOBAL_REFERENCE_STANDARD.md`.

Validator: `validate_content.py`

### Gate 10 — Acquisition Surface

`/acquire/` is live and strategically correct.

The acquisition page is not a placeholder. It communicates strategic asset value without naming buyers.

### Gate 11 — Multilingual Integrity

All multilingual pages pass the integrity check.

A multilingual page fails Gate 11 if:

- `hreflang` targets do not resolve.
- HTML `lang` attribute is incorrect.
- Arabic pages do not use `dir="rtl"`.
- Alternate routes point to unpublished pages.
- Translated pages introduce unapproved claims.
- Translated pages remove required disclaimers.
- Translated pages weaken safety restrictions.
- Language sitemap sections contain draft URLs.
- Translated content is partial, placeholder, or unreviewed machine output.

Validator: `validate_hreflang.py`, `validate_translations.py`, `validate_language_routes.py`

### Gate 12 — Page Distinctiveness & Information Gain

> A page may not become publication-eligible merely because it is complete, sourced, grammatically different, or has a unique title. It must contain materially distinct knowledge.

Gate 12 is **blocking** and is a reference-quality and commercial-asset-quality gate, not an SEO-only gate. A failure prohibits publication and indexation.

Infrastructure is separated from substance before comparison: front matter, route IDs, draft/publication-status notices, navigation, footer, provenance labels, standard disclaimers, citation trails and governance notices are excluded by explicitly registered patterns (`main/data/distinctiveness/gate12_policy.json`). Text is never excluded merely because it recurs.

A page fails Gate 12 if any of the following holds:

- **Near duplicate** — entity-masked substantive similarity `S >= 0.70` with another page (`S = max(Jaccard, overlap coefficient)` over word 5-gram shingles). `0.55 <= S < 0.70` requires production review and is not publication-eligible. `S < 0.55` passes only the textual component.
- **Structural template** — the substantive section skeleton is shared with sibling pages and filled with template prose or similar text (entity-slot substitution).
- **Template prose** — at least half of the substantive sentence tokens are sentences that recur (entity-masked) on three or more pages.
- **Thin body** — fewer than 60 substantive tokens after infrastructure exclusion.
- **Information Gain** — fewer than three valid Information Gain units. A unit is page-specific, bound to governed verified evidence (and its claim), not boilerplate, not an entity substitution, rendered on the page, and useful to a governed audience (`main/data/distinctiveness/ig_unit_registry.json`). Facts are never invented to reach three.

Translations are evaluated for language integrity by Gate 11; a declared localization inherits its source page's Gate-12 status and cannot create distinctiveness. Synonym swapping, sentence reordering, renamed headings, generic introductions or FAQs, longer disclaimers, padding and unsourced "unique" facts do not solve similarity.

**Publication contract.** A route is publication/indexation-eligible only when evidence, claim, Information Gain, Gate 12 and release authorization all pass. Gate 12 does not override Contract C (`scripts/governance_scaffolding/contract_c_derive.py`); Contract C does not override Gate 12.

**Gate 12-I — institutional surfaces.** A registered non-factual institutional surface (home, methodology, policy, navigation hub; `main/data/distinctiveness/institutional_surface_registry.json`) replaces only the Information-Gain requirement with a closed, one-per-language function check. The near-duplicate, review-band, template-prose, structural-template and thin-body rules still apply. Gate 04 and Contract C (R11 for non-factual indexation) are not relaxed.

**Legacy migration (bounded, Contract C RL).** Pages publicly deployed before Gate 12 are sealed in `main/data/distinctiveness/legacy_surface_hold.json` (path + substantive-body hash; count + sha256; shrink-only). A held page that fails Gate 12 may stay reachable only if its body is unchanged, its robots meta is `noindex` and it is absent from every sitemap. A new failing page, or a modified failing legacy page, always blocks. An indexed held page blocks unless an owner-authorized freeze exception of at most 30 days is active; that exception is a reported Contract-C deviation and admits nothing new.

Validator: `validate_distinctiveness.py` (real enforcement; `--gate` for publication candidates, `--surface DIR [--legacy-hold FILE]` for a deploy surface, `--check-hold` for baseline integrity and the shrink-only ratchet, `--audit` for the whole-corpus report).

---

## Gate Status

Status values:

- `PASS` — condition met, verified by validator.
- `FAIL` — condition not met, blocks deployment.
- `PENDING` — not yet evaluated.

No deployment proceeds while any gate is `FAIL` or `PENDING`.

---

## Running All Gates

```
python scripts/validators/validate_all.py
```

Gate failures produce a blocking error with the gate number and condition that failed.

Gates 01–11 are currently placeholder validators. Gate 12 performs real enforcement.
