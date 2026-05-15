# PROJECT DOCTRINE

This document governs all operations for bisulfid.com.

It is subordinate only to `ASSET_THESIS.md`.

---

## Doctrine Hierarchy

1. `ASSET_THESIS.md` — defines what this asset is.
2. `PROJECT_DOCTRINE.md` — governs all operations. *(this document)*
3. `SOURCE_POLICY.md` — governs claims and sources.
4. `QUALITY_GATE.md` — defines launch conditions.
5. `MULTILINGUAL_POLICY.md` — governs language architecture and hreflang integrity.

No lower document may contradict a higher document.

AI-assisted tools may be used, but no tool-specific instruction file overrides doctrine.

---

## Identity Rules

- bisulfid.com is a sovereign reference asset, not a content farm.
- bisulfid.com is not a blog, a personal site, or a domain-for-sale page.
- All decisions are tested against the Asset Thesis before execution.
- The governing sentence is: *Keep the interface. Harden the claims. Govern the links. Then launch.*

---

## Content Rules

- No placeholder content is published.
- No thin multilingual pages are published.
- No unsourced claims are published.
- Every factual claim requires a verified entry in the source registry.
- AI-assisted tools may be used for drafting and analysis. No tool output is published without human review.
- Tool choices are recorded in `DECISION_LOG.md`.

### What bisulfid.com Publishes

- Sulfur terminology reference pages
- Chemical-language context
- Industrial sulfur intelligence
- Safety context (governed, non-prescriptive)
- Multilingual reference layers
- Acquisition surface

### What bisulfid.com Does Not Publish

- Chemical handling instructions
- Dosage advice
- Safety thresholds as prescriptive advice
- Medical or therapeutic claims
- Competitor targeting language
- Company names as acquisition targets in public pages
- Market statistics without a verified source

---

## Build Rules

- Stack: Python, Jinja2, static HTML, static CSS, vanilla JavaScript.
- Output lives in `site/`.
- Generated files are never edited manually.
- No dependency is added without doctrine review.
- No external scripts are included without trust verification and SRI hash pinning.
- All validators must pass before deployment.

---

## Security Rules

- Static-first architecture.
- No public CMS.
- No server-side login.
- No server-side code execution in production.
- No secrets in the repository.
- CSP required before production launch.

Full policy: `doctrine/SECURITY_POLICY.md`

---

## Quality Rules

- All 11 quality gates must pass before deployment.
- One gate fails = no deployment.
- No partial launches.
- No "we will fix it after."

Full gate definitions: `doctrine/QUALITY_GATE.md`

---

## Language Rules

- No language launches until complete.
- A partial language is not a launched language.
- A machine-translated page is not a published reference page.
- Every language layer must increase reference value, not just SEO volume.

Full policy: `doctrine/MULTILINGUAL_POLICY.md`

---

## Revenue Rules

- Revenue that raises trust is permitted.
- Revenue that lowers trust is forbidden.
- No ads on `/acquire/` or authority pages.
- No affiliate links to chemical suppliers.
- No popups.
- No sponsored content disguised as editorial content.

---

## Repository Governance

- All structural changes to the repository require doctrine review.
- All changes to doctrine require a `DECISION_LOG.md` entry.
- Version changes to published content require source review.
- No generated file is edited manually.
