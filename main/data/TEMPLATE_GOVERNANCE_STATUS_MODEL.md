# Template Governance Status Model

**Sprint:** 6M-B

---

## Visible governance layers

Every non-public render must surface:

| Layer | Source | Default display |
| --- | --- | --- |
| Route status | `routes.json` | `planned` |
| Publication posture | build engine | `non_public` |
| Robots | build engine | `noindex, nofollow` |
| Indexation | route + build | `false` |
| Sitemap | route + policy | `false` / inactive |
| Navigation | route + config | `false` / inactive |
| Source required | route | visible when true |
| Claim approval | claim registries | `none_approved` |

---

## governance_banner.html

Always rendered for QA and pre-publication builds. States:

- Not a launch
- Not a reduced publication target
- 14,000-page frame context
- Active lock summary

---

## source_bar.html

| State | Display |
| --- | --- |
| `source_required: true`, 0 verified | Posture message + [SOURCE REQUIRED] reminder |
| Verified sources exist (future) | List from registry — still no implied claim approval |
| No sources | Empty list; no fake citations |

---

## claim_approval_state values

| Value | Meaning |
| --- | --- |
| `none_approved` | Default — no claim approved for this render |
| `pending_review` | Draft content under review |
| `approved_narrow` | Future — explicit sprint authorization only |

Build frame **never** sets `approved` without registry + sprint gate.

---

## QA artifact flag

`qa_artifact_flag=true` for `site/_sample/` local renders — must also show governance banner.

---

## What templates must never imply

- Public launch readiness
- Indexation authorization
- Sitemap inclusion
- Navigation inclusion
- Source-lock completion
- Claim approval
- 500-page launch sufficiency
