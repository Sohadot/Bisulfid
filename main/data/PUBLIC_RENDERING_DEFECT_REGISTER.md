# Public Rendering Defect Register — Sprint 6M-I

**Date:** 2026-05-31  
**Scope:** First live visibility defects on bisulfid.com (site/public/ foundation)

## Summary

| ID | Defect | Severity | Files affected (local scan) | Fix sprint |
|----|--------|----------|----------------------------|------------|
| DEF-01 | Default browser styling | High | 14,000 / 14,000 | 6N-B |
| DEF-02 | Raw Markdown rendering | Medium | 4 | 6N-B + render pipeline |
| DEF-03 | QA placeholder leakage | High | 228 | 6N-B + build/template |
| DEF-04 | Governance overload (raw text) | Medium | 14,000 | 6N-B |
| DEF-05 | Design system not integrated | High | 14,000 | 6N-B |

---

## DEF-01: Default styling defect

**Description:** Pages render with browser default typography and layout. No `bisulfid-design-system` tokens or components are linked. Live site lacks sovereign visual identity.

**Evidence:** Zero public HTML files reference `bisulfid-design-system/`. User-visible unstyled governance blocks and term frames.

**Severity:** High — undermines brand and readability at scale.

**Blocks indexation:** Yes — presentation not sovereign-grade.

**Recommended fix sprint:** **6N-B** — integrate tokens/components into publication frames; controlled re-render pilot.

---

## DEF-02: Raw Markdown rendering defect

**Description:** Markdown bold markers (`**text**`) appear literally in public HTML instead of being rendered to `<strong>` or governed emphasis.

**Evidence (local):** 4 files including `glossary/index.html`, `german-english-chemical-terms/index.html`, `index.html`, `bisulfide-hydrosulfide-sulfide/index.html`.

**Example:** `**source-locking required**`, `**bisulfide**`, `**not**` visible to visitors.

**Severity:** Medium — signals unfinished content pipeline; confusing on high-traffic gateway pages.

**Blocks indexation:** Yes — on affected gateway/glossary routes.

**Recommended fix sprint:** **6N-B** (presentation) + follow-on render pipeline sprint for Markdown-to-HTML body conversion.

---

## DEF-03: QA placeholder leakage defect

**Description:** Public pages display engineering placeholder text: `Slot reserved — not populated in QA render.`

**Evidence (local):** **228** of 14,000 HTML files contain QA slot empty markers (typically internal-links and related slots).

**Severity:** High — explicitly QA language on a publicly visible site.

**Blocks indexation:** Yes — placeholder text must not appear in indexable output.

**Recommended fix sprint:** **6N-B** + template/build fix to suppress or populate slots before wide re-render.

---

## DEF-04: Governance-overload visual defect

**Description:** Governance status appears as dense raw text (multiple banners, lock lists, route metadata) without structured design-system UI. Truthful but visually heavy.

**Evidence:** Duplicate governance surfaces per page (governance banner + public launch foundation notice + source bar + nav inactive note).

**Severity:** Medium — acceptable for foundation visibility; not suitable as final public presentation.

**Blocks indexation:** Partial — does not hide truth, but hurts UX and trust at search exposure.

**Recommended fix sprint:** **6N-B** — `.bs-governance-banner`, `.bs-source-crystal`, structured hierarchy.

---

## DEF-05: Design-system-not-integrated defect

**Description:** Sprint 6N-A created `bisulfid-design-system/` but templates/public HTML do not reference it.

**Evidence:** 14,000/14,000 pages without design-system CSS/JS links.

**Severity:** High — strategic asset exists but is not deployed to live presentation layer.

**Blocks indexation:** Yes — indexation should follow sovereign presentation integration.

**Recommended fix sprint:** **6N-B** — Design System Template Integration Pilot.

---

## Why these defects block indexation opening

Indexation gate opening requires presentation suitable for public discovery: no QA placeholders, no raw Markdown, sovereign styling, structured governance UI. Current live state correctly remains `noindex,nofollow` while defects are registered and remediated.

## Gate preservation note

Defect registration does not authorize indexation, sitemap, navigation, or source/claim approval. All gates remain **CLOSED**.
