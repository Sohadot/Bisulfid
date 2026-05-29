# Corpus Production SEO and Indexation Model — Layer 2

**Sprint:** 5O-A  
**Date:** 2026-05-29

---

## Purpose

Define SEO metadata, sitemap, and indexation discipline for sovereign-scale production without thin SEO expansion or premature search visibility.

---

## SEO metadata requirements

- Every route requires validated **title**, **description**, and **H1** before publication
- Metadata must reflect real **corpus role** — not keyword stuffing
- SEO metadata gate precedes publication gate
- Structured data readiness documented per template type

---

## Title/description discipline

- Titles identify governed reference role and site identity
- Descriptions state planned/non-public posture in pre-launch drafts
- No misleading “published” language in metadata for planned routes

---

## Canonical discipline

- One canonical URL per public route when published
- hreflang alternates coordinated with multilingual model
- No duplicate canonical targets across language layers without hreflang group

---

## Sitemap lock

- **Sitemap lock** enforced: `in_sitemap: false` on all routes until launch authorization
- `sitemap_policy.json` status inactive/planned pre-launch
- Sitemap/indexation must remain locked until **500 governed pages** pass all gates
- No sitemap URLs activated before publication readiness wave

---

## Indexation lock

- **Indexation lock** enforced: `indexable: false` on all routes until launch authorization
- **noindex** rules apply to entire pre-launch corpus
- No `indexable: true` before publication gates — automation must fail if detected

---

## noindex rules before publication

- All planned routes treated as non-indexable
- Generated public HTML forbidden pre-gate — implicit noindex by non-existence
- Search console readiness documented; no premature submission of thin cohorts

---

## Anti-thin SEO rules

- **No thin SEO pages** — minimum substance per `CORPUS_LAUNCH_THRESHOLD.md`
- No generic AI glossary pages
- No placeholder “visibility” copy
- Anti-thin-content enforcement applies to metadata and body

---

## Anti-random SEO rules

- **No random SEO expansion** — waves are chartered vertical slices
- Route count is **not** treated as SEO quality
- No mass page generation without source/claim/link gates

---

## Structured data readiness requirements

- Template-aligned structured data planned per route type
- No structured data claiming verified claims without registry support
- Structured data validation in technical/security gate

---

## Search console readiness

- Document indexation sequence for launch cohort only
- Pre-launch: verify locks, not live indexation
- Post-launch: phased indexation per sitemap policy authorization

---

## Launch indexation sequence

```
1. 500 governed pages pass all gates (CORPUS_LAUNCH_THRESHOLD.md)
2. Publication readiness wave authorizes cohort
3. Sitemap policy activation (chartered)
4. Indexation flags enabled route-by-route under policy
5. Search console submission of authorized sitemap only
6. Ongoing audit — rollback gate on gate failure
```

**Public launch below 500 governed pages is forbidden.**

---

*Sprint 5O-A — Corpus Production SEO Indexation Model Layer 2*
