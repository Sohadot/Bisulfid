# Pages Artifact Sample Exclusion Patch Report — Sprint 6N-C-P1

**Date:** 2026-06-01  
**Branch:** `claude/sprint-6n-c-p1-pages-artifact-sample-exclusion-patch`

## Why the Pages deploy failed

After Sprint 6N-C merged, the **Pages public deploy** workflow failed at the artifact verification step. The workflow counted **14,007** `index.html` files under `site/public/` and rejected the deployment because the expected count is exactly **14,000**.

## Why 14,007 pages were detected

Sprint 6N-B added a **7-route design-system integration pilot** under `site/public/_integration_sample/`. Sprint 6N-C refreshed the **14,000 foundation pages** but **preserved** the integration sample in the repository. The pre-patch workflow uploaded the entire `site/public/` tree:

```
14,000 foundation pages + 7 integration sample pages = 14,007 HTML pages
```

The deployment gate correctly treated this as an artifact boundary violation.

## Why the 7 integration sample pages must not be deployed

The integration sample is a **local validation and template pilot artifact**, not part of the governed public foundation corpus. It exists to prove design-system integration before full refresh; it is not authorized for live public visibility on `bisulfid.com`. Deploying it would:

- Expose non-foundation routes on the live domain
- Blur the boundary between pilot output and production public foundation
- Violate the 14,000-page deployment contract established in Sprint 6M-G/H

## Why this is a deployment-artifact issue, not a corpus defect

- **14,000 routes** remain in `routes.json` — unchanged
- **14,000 foundation pages** remain correctly rendered under `site/public/` — unchanged
- **7 integration sample pages** are intentionally retained in-repo for validator and integration checks
- The failure is **protective**: the workflow stopped before publishing an oversized artifact
- No content, registry, design refresh, or gate posture change is required

## Chosen artifact staging approach

1. Keep `site/public/` as the **repository source of truth** (unchanged on disk)
2. During workflow execution only, **stage** a temporary artifact directory under `${RUNNER_TEMP}/pages-artifact`
3. **Copy** `site/public/` into staging with `rsync -a --exclude='_integration_sample/'`
4. **Verify** staged artifact contains exactly **14,000** `index.html` files and excludes `_integration_sample/`
5. **Upload** the staged directory to GitHub Pages — never commit staging output to the repository

## What is excluded

| Path | Reason |
|------|--------|
| Repository root | Not a public artifact |
| `site/_sample/` | Quarantined QA sample |
| `site/public/_integration_sample/` | 7-route integration pilot — repo-only |

## What remains deployed

- **14,000** design-system-integrated foundation HTML pages
- `public_launch_manifest.json` (6N-C metadata)
- `CNAME` (`bisulfid.com`)
- `.nojekyll` (Jekyll bypass)
- `assets/bisulfid-design-system/` (local design-system bundle)

## Why indexation, sitemap, and navigation remain closed

This sprint patches **deployment artifact boundaries only**. It does not authorize publication, crawling, sitemap generation, or navigation opening. All pages retain `noindex,nofollow`; no sitemap or navigation artifacts are generated or deployed.

## Why source and claim gates remain closed

No registry, content, or approval data is modified. `[SOURCE REQUIRED]` markers and non-approval posture on public pages are unchanged. The patch ensures the live site serves the correct 14,000-page foundation — not that sources or claims are approved.

## Next step

Merge → run **Pages public deploy** → **Sprint 6M-J — Post-Refresh Live Site Verification**.
