# Publication Frame QA Next Actions

**Sprint:** 6M-C  
**Date:** 2026-05-30

---

## Is the QA sample sufficient for a larger non-public release candidate?

**Partially.** The 8-page quarantined sample proves frame composition, template bridging, noindex posture, and governance visibility across gateway, terminology, disambiguation, and governance routes. It is **not sufficient alone** for a 100–250 page non-public release candidate — that requires broader route coverage, richer markdown rendering, internal link slot wiring (read-only), and explicit sprint authorization for expanded quarantine or staging output.

---

## Is more template refinement required?

**Yes, incrementally:**

- Replace remaining skeleton files (`glossary.html`, `newsletter.html`, `acquire.html`) with bridge wrappers or hardened frames
- Strengthen markdown/HTML rendering for production-grade output
- Wire hreflang and internal link slots when policies authorize (still non-public)
- CSP meta hardening before any staging exposure

Core publication frames (`base`, `home`, `page`, `reference`, `term`, partials) are **ready for expanded non-public rendering**.

---

## Is route/template mapping now ready?

**Yes for render wiring** — `build.py` resolves all 6 active registry template names via bridge map and wrapper files. **No** for direct registry rename — `routes.json` still references legacy names by design; future sprint may migrate names with full registry integrity gate.

---

## Criteria for 100–250 page non-public release candidate

1. Explicit decision-log authorization for expanded quarantine or staging path
2. Deterministic render mode for selected cohort (not full 1,043 without gate review)
3. All output: `noindex, nofollow`, governance banner, non-public markers
4. Template registry validator + sample output validator PASS at expanded count
5. Route/content alignment strict checks PASS for rendered cohort
6. Still **0** published routes; locks remain LOCKED
7. No sitemap/navigation generation
8. Source/claim registries unchanged; `[SOURCE REQUIRED]` preserved

---

## Criteria for 14,000-page launch corpus preparation

1. Complete draft backing for registered routes (currently 58 missing drafts)
2. Source verification and claim approval per SOURCE_POLICY (not implied by frames)
3. Quality Gate passage per route cohort
4. Explicit publication sprint authorization
5. Sitemap/navigation policy activation only after published routes exist
6. Production build mode with full governance audit trail
7. **14,000-page minimum** remains fixed — not reduced to 500 or pilot scope

---

## Criteria for first public launch sprint

1. `production_can_safely_proceed: yes` with all locks intentionally opened per route
2. Published routes with verified sources and approved claims where required
3. Active sitemap/navigation only for eligible published routes
4. CSP and security Gate 06 complete
5. Corpus Governance CI PASS on release branch
6. No `[SOURCE REQUIRED]` on published factual claims
7. Decision-log launch authorization entry

---

## Why quality gates remain non-negotiable

The corpus targets **14,000+ governed pages** scaling toward **100,000+**. A single premature publication event — indexation leak, sitemap exposure, or implied claim approval — would violate doctrine and damage sovereign reference integrity. QA rendering proves **technical capability**; gates prove **governance readiness**.

---

## Why visibility/publication is now the primary track

Template hardening (6M-B) and registry migration + quarantined render (6M-C) complete the **publication frame pipeline proof**. The next increments focus on **controlled visibility** (larger non-public RC, staging) under unchanged locks — not public launch.

---

## Why this sprint still does not authorize public launch

- 0 published routes; all publication/indexation/sitemap/navigation locks **LOCKED**
- `production_can_safely_proceed: no`
- QA HTML quarantined under `site/_sample/` only
- No source or claim approval
- 14,000-page objective unchanged; 1,043 routes are pipeline progress only

**Recommended next sprint:** 6M-D — expanded non-public release candidate render (100–250 pages) with cohort selection gate, or registry template name migration sprint if authorized separately.
