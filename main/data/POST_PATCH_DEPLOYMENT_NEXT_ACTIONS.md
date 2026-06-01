# Post-Patch Deployment Next Actions — Sprint 6N-C-P1

**Date:** 2026-06-01

## 1. Run Pages public deploy after merge

After Sprint 6N-C-P1 merges to `main`:

1. Confirm `validate_pages_deployment_gate_l1.py` — **PASS** on `main`
2. Trigger **Pages public deploy** workflow (`workflow_dispatch`)
3. Confirm workflow stages artifact with exactly **14,000** pages
4. Confirm workflow excludes `_integration_sample/` from upload

## 2. Verify workflow succeeds

Expected workflow outcome:

- Foundation count in repo: **14,000**
- Integration sample in repo (not deployed): **7**
- Staged artifact count: **14,000**
- Deploy step completes without artifact boundary failure

## 3. Verify bisulfid.com serves 6N-C design-system output

After deploy completes:

- `https://bisulfid.com/` loads design-system-integrated HTML (not browser-default)
- Local design-system CSS (`/assets/bisulfid-design-system/bisulfid-frame.css`) loads
- `bs-control-room` / governance banner structure visible
- No raw Markdown or QA placeholder text on live sample routes

## 4. Verify public_launch_manifest.json still reports 6N-C

- Manifest deployed at site root reports `design_system_refresh: true`
- Sprint metadata: **6N-C**
- `rendered_count`: **14,000**

## 5. Verify _integration_sample is not reachable live

Confirm these return **404** on the live domain:

- `https://bisulfid.com/_integration_sample/`
- Any path under `/_integration_sample/`

Integration sample remains in the repository for local validators only.

## 6. Proceed to 6M-J post-refresh live verification

**Sprint 6M-J — Post-Refresh Live Site Verification:**

1. Run `validate_live_site_visibility_l1.py`
2. Run `validate_14000_design_system_public_refresh_l1.py` against deployed posture
3. Close or downgrade DEF-01 through DEF-05 based on live evidence
4. Update defect register if live PASS confirmed

**Important:** Indexation, sitemap, and navigation remain **CLOSED** after deploy and after 6M-J unless explicitly authorized in a future sprint.
