# Template Registry Migration Report

**Sprint:** 6M-C  
**Date:** 2026-05-30  
**Branch:** `claude/sprint-6m-c-template-registry-migration-and-quarantined-qa-render`

---

## Why this sprint exists

Sprint **6M-B** hardened the sovereign publication frame templates (`base.html`, `home.html`, `page.html`, `reference.html`, `term.html`, and partials) for the fixed **14,000-page** minimum launch corpus. The route registry (`routes.json`) was intentionally **not** modified in 6M-B. Legacy registry template names (`reference_page.html`, `term_page.html`) still pointed at skeleton placeholders, blocking safe render wiring.

Sprint **6M-C** resolves that mismatch without registry mutation and produces the first **quarantined non-public QA HTML** under `site/_sample/` to prove the publication frame can render visible output without weakening locks.

---

## Why migration follows template hardening

Template hardening (6M-B) defined the governed frame contract: governance banner, noindex posture, source/claim non-approval language, multilingual slots, and 14,000-page corpus scale markers. Registry migration (6M-C) connects **existing route template references** to those hardened frames so `build.py` can render QA samples without relitigating route records or publication posture.

---

## Legacy template references found

| Registry template | Routes | Pre-migration state |
|---|---:|---|
| `reference_page.html` | 980 | Skeleton placeholder |
| `term_page.html` | 59 | Skeleton placeholder |
| `home.html` | 1 | Hardened frame (6M-B) |
| `glossary.html` | 1 | Skeleton (bridged via build map) |
| `newsletter.html` | 1 | Skeleton (bridged via build map) |
| `acquire.html` | 1 | Skeleton (bridged via build map) |

**Total active template names:** 6  
**Primary mismatch:** 1,039 routes referenced legacy skeleton names (`reference_page.html` / `term_page.html`).

---

## Hardened template targets

| Frame | Role |
|---|---|
| `reference.html` | Reference-layer publication frame |
| `term.html` | Terminology publication frame |
| `home.html` | Gateway homepage frame |
| `page.html` | Generic governed page frame |
| `base.html` | Institutional shell composing partials |

All partials from Sprint 6M-B remain unchanged (`governance_banner.html`, `head.html`, `source_bar.html`, etc.).

---

## Migration / bridge strategy

1. **Wrapper bridge files** — `reference_page.html` and `term_page.html` were converted from skeleton placeholders into registry bridge files that delegate to the hardened `reference.html` / `term.html` slot contract (same article frames, bridge metadata comments, no skeleton markers).

2. **Build engine map** — `scripts/build.py` defines `TEMPLATE_FRAME_BRIDGE` mapping legacy registry names to hardened frames:

   | Registry name | Resolved frame |
   |---|---|
   | `reference_page.html` | `reference.html` |
   | `term_page.html` | `term.html` |
   | `home.html` | `home.html` |
   | `glossary.html` | `reference.html` |
   | `newsletter.html` | `page.html` |
   | `acquire.html` | `page.html` |

3. **Quarantined render mode** — `--render-quarantined-sample` writes deterministic QA HTML to `site/_sample/{route_id}.html` only. No production output. No sitemap. No navigation.

4. **Validator** — `scripts/validate_template_registry_l1.py` fails if active legacy bridges remain unresolved skeletons or if hardened targets are missing.

---

## Why routes.json was not modified

Route registry integrity is governed separately. This sprint proves **template path resolution** without changing route status, indexation flags, sitemap membership, navigation membership, or content assignments. Registry template migration to direct hardened names may occur in a future governed sprint with explicit route-registry authorization.

---

## How build.py maps templates after this sprint

1. Read `route.template` from `routes.json` (unchanged legacy name).
2. Resolve via `resolve_frame_template()` / `TEMPLATE_FRAME_BRIDGE`.
3. Prefer bridged wrapper file when not skeleton; fall back to hardened frame file.
4. Compose `base.html` + partials + inner frame with governance context.
5. For QA only: write flat `{route_id}.html` under `site/_sample/`.

---

## Remaining template risks

| Risk | Mitigation |
|---|---|
| `glossary.html`, `newsletter.html`, `acquire.html` remain skeleton files on disk | Build bridge maps to hardened frames; validator warns |
| Full corpus render not yet authorized | Quarantined sample only (8 routes) |
| Markdown renderer is minimal QA subset | Production build will need richer rendering |
| CSP meta is placeholder | Gate 06 before public launch |
| Hreflang / internal links inactive | Expected under publication locks |

---

## Relationship to the fixed 14,000-page launch objective

The **14,000-page minimum launch corpus** remains the fixed objective. This sprint does not reduce, pilot, or substitute that target. QA output proves the **publication frame** scales conceptually across gateway, terminology, disambiguation, and governance routes — not that the launch corpus is complete (1,043 routes planned; 985 draft-backed; 58 missing drafts).

---

## Relationship to 100,000+ future expansion

Bridge mapping and frame composition are **name-agnostic** and **route-count-agnostic**. The same `TEMPLATE_FRAME_BRIDGE` + hardened partial contract supports future cohort waves without requiring per-route template renames at render time.

---

## What this sprint does not authorize

- Public launch or production build
- Route publication or indexation
- Sitemap or navigation exposure
- Source or claim approval
- `[SOURCE REQUIRED]` removal
- Registry or content modification
- HTML outside `site/_sample/`
- Reduced launch target (500-page pilot, blog, etc.)
