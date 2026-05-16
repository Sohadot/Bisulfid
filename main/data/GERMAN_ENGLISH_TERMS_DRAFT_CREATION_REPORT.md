# German-English Terms Draft Creation Report

## Why This Sprint Exists

Sprint 4G confirmed that `routes.json` already defines `german_english_chemical_terms` with `content_file` `main/content/en/pages/german-english-chemical-terms.md`, but that file was missing. Sprint 4H creates that **non-public** English draft so route/content alignment can proceed in future governance sprints **without** publishing the route, changing route metadata files, or approving claims.

## What Was Created

- **route_id addressed:** `german_english_chemical_terms`
- **File created:** `main/content/en/pages/german-english-chemical-terms.md`
- **Frontmatter (key fields):** `status: draft`, `publication_status: non_public`, `indexable: false`, `in_sitemap: false`, `language: en`, `locale: en`, `source_language: en`, `route_id: german_english_chemical_terms`

## Why the Page Remains Non-Public

The draft explicitly states it is **not publication-ready**. Frontmatter keeps `publication_status: non_public`, `indexable: false`, and `in_sitemap: false`. All routes in `routes.json` remain `planned`; this sprint did not change routing or publication flags in that file. The page is terminology-control copy for **draft review** only.

## Why `routes.json` Was Not Modified

Route governance was already correct in Sprint 4G: the issue was a **missing content file**, not route configuration. Modifying `routes.json` was out of scope and would risk unintended publication semantics. Aligning `content_file` on disk with the existing route definition resolves the file gap without touching route data.

## Why No Claim Was Approved

Terminology claims require registry activation, source-locking, and review workflows that this sprint does not run. The draft adds cautious framing and `[SOURCE REQUIRED]` markers instead of advancing any claim to an approved state. **`terminology_claims.json` was not modified.**

## Why `[SOURCE REQUIRED]` Markers Remain

Markers indicate **source-locking required** before public-ready factual language. No sources were newly bound to this page in this sprint, so markers stay on both this page and all other drafts. This sprint **did not remove** markers from any file.

## How This Resolves the Sprint 4G Missing-Draft Finding

Sprint 4G reported that `main/content/en/pages/german-english-chemical-terms.md` did not exist while the route pointed to that path. Sprint 4H **creates** that path-aligned file with governed frontmatter and cautious terminology language, closing the specific **missing draft file** finding. The **broader** inventory of other planned routes still lacking drafts (documented in Sprint 4G) is unchanged and out of scope here.

## Remaining Blockers Before Publication

- Source registration and **source-locking** for each statement intended to go public.
- Quality Gate and route lifecycle steps (`routes.json` still shows `planned` for this route)
- Review of `[SOURCE REQUIRED]` density and claim alignment when registries are activated under separate sprints
- No assumption that academic teaching PDFs substitute for DIN or official German IUPAC authority text

## Recommended Next Sprint

A **terminology source-locking** or **claim-boundary** sprint that maps specific rows in the new draft to permitted `terminology_claims` entries and registered sources - still **without** approving claims until registry rules and sources permit - or a sprint to audit the next highest-priority missing draft from the Sprint 4G inventory list.

## Files Touched in Sprint 4H

- **Created:** `main/content/en/pages/german-english-chemical-terms.md`
- **Created:** `main/data/GERMAN_ENGLISH_TERMS_DRAFT_CREATION_REPORT.md` (this file)
- **Updated:** `DECISION_LOG.md`

## Files Explicitly Not Modified

`routes.json`, `internal_links.json`, `sitemap_policy.json`, `navigation.json`, `hreflang_groups.json`, `translation_registry.json`, `source_registry.json`, `terminology_claims.json`, `sulfur_terms.json`, templates, other content pages, root `README.md`, package manifests, workflows, deployment configs, generated HTML.
