# Build Scripts — scripts/

## Status: Build Skeleton

The scripts in this directory form the build skeleton for bisulfid.com.
All scripts use Python standard library only. No external dependencies are present or required at this stage.

## Scripts

| File | Description |
|------|-------------|
| build.py | Static build orchestrator. Reads routes.json. Generates site/build-status.json only. |
| generate_sitemap.py | Generates site/sitemap.xml with zero URLs (prelaunch). |
| generate_robots.py | Generates site/robots.txt with full Disallow (prelaunch). |
| serve.py | Local development server using http.server. |

## Validators

Validator stubs are in `scripts/validators/`. They are placeholders from Sprint 0D
and are not yet enforcing any quality gates. See `scripts/validators/README.md`.

## Important

- **No public pages are generated** until routes have `status: published` and all 11 Quality Gates pass.
- **Sitemap contains zero URLs.** Routes are planned, not published.
- **robots.txt blocks all indexing.** Prelaunch policy is enforced until Quality Gate passes.
- **Validators remain placeholders** from Sprint 0D and are not launch proof.
- **No dependencies.** Do not add package.json, requirements.txt (with packages), or pip install calls.
- **No GitHub Actions.** Build and serve commands run locally only at this stage.

## Usage

```bash
# Build (generates site/build-status.json only)
python scripts/build.py

# Generate sitemap (prelaunch: 0 URLs)
python scripts/generate_sitemap.py

# Generate robots.txt (prelaunch: full Disallow)
python scripts/generate_robots.py

# Serve locally
python scripts/serve.py
```

## Doctrine Reference

- Route publication: `doctrine/QUALITY_GATE.md`
- Build security: `doctrine/SECURITY_POLICY.md`
- Source discipline: `doctrine/SOURCE_POLICY.md`
