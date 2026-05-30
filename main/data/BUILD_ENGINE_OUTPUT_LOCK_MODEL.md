# Build Engine Output Lock Model

**Sprint:** 6M-A  
**Output root:** `site/` (per `main/config/build.json`)

---

## site/ output policy

| Rule | Current state |
| --- | --- |
| Committed public HTML | **None** (`.gitkeep` only) |
| Default build writes | **None** |
| Audit artifacts | Only with `--write-build-status` |
| Sample artifacts (future) | Restricted subdirectory, non-public |

The `site/` directory is reserved for build output but remains **empty of HTML** until an authorized sprint explicitly generates governed artifacts.

---

## No public HTML by default

- Default CLI invocation prints help and exits without writes.
- `--dry-run` generates zero HTML files.
- `--sample N` plans sample routes but generates zero HTML while locks active.
- `public_pages_generated` is always **0** in locked posture.

---

## No overwrite without explicit mode

- Build engine does not delete `site/` contents.
- Build engine does not bulk-overwrite HTML without explicit production mode (not implemented in 6M-A).
- `--write-build-status` writes only `site/build-status.json` when explicitly requested.

---

## No sitemap generation without sitemap authorization

Requires **all** of:

1. `main/data/sitemap_policy.json` status active
2. Non-empty authorized `urls` array OR governed generation mode (future)
3. Route `in_sitemap: true`
4. Route `indexable: true`
5. Route `status: published`

**Current:** all conditions false — sitemap generation **locked**.

---

## No navigation generation without navigation authorization

Requires **all** of:

1. `main/config/navigation.json` status active
2. Non-empty `items` array OR governed generation mode (future)
3. Route `in_navigation: true`
4. Route `status: published`

**Current:** all conditions false — navigation generation **locked**.

---

## No indexable output without indexation authorization

- HTML `robots` meta must be `noindex, nofollow` for non-published routes.
- Indexable output requires route `indexable: true` **and** `status: published`.
- Strict mode fails on indexable + non-published combinations.

---

## Sample output restrictions

When sample rendering is authorized (future sprint):

| Restriction | Requirement |
| --- | --- |
| Path | `site/_sample/` or equivalent quarantine prefix |
| Labeling | Visible dry-run/sample/non-public banner in output |
| Robots | `noindex, nofollow` mandatory |
| Route status | Unchanged (remains planned) |
| Commit policy | Sample HTML not committed unless sprint explicitly allows |
| Count | Small N via `--sample N` only |

---

## Future production output prerequisites

1. Templates hardened from skeleton to production-ready
2. Strict dry-run PASS on full corpus
3. Target routes published via governed sprint (not build engine)
4. Source/claim gates satisfied per route
5. L1 + L2 + build engine validators PASS
6. Explicit `--production` mode (future) authorized by decision log
7. `production_can_safely_proceed: yes`

---

## Future public launch prerequisites

All production prerequisites **plus**:

- Sitemap policy activated under doctrine
- Navigation policy activated under doctrine
- Security gates (CSP, SRI, etc.)
- Corpus launch threshold and 14,000-page strategic target alignment
- Zero publication/indexation/sitemap/navigation leakage in CI
- Public launch entry in `DECISION_LOG.md`

**Sprint 6M-A authorizes none of the above.**
