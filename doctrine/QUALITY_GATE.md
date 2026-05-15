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

## The 11 Gates

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

Validator: `validate_seo.py`

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
