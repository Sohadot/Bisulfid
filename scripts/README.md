# scripts/

This directory contains Python scripts for building and validating bisulfid.com.

All scripts use the Python standard library only. No external dependencies are permitted
until explicitly approved via the decision log.

## Scripts

| Script | Purpose |
|--------|--------|
| `build.py` | Static build orchestrator. Reads config and routes; generates `site/build-status.json`. |
| `generate_robots.py` | Generates `site/robots.txt` with prelaunch full-disallow policy. |
| `generate_sitemap.py` | Generates `site/sitemap.xml`. Only includes published + indexable + in_sitemap routes. |
| `generate_placeholders.py` | Generates placeholder HTML skeletons for planned routes (dev use only). |

## Validators

See [`validators/README.md`](validators/README.md) for the Quality Gate validator surface.

## Constraints

- Python standard library only.
- No `pip install`, no `requirements.txt` with external packages, no `package.json`.
- No GitHub Actions workflows in this directory.
- No deployment config.
- Scripts must exit 0 on success, non-zero on failure.
- No script may mark a route as published or set `indexable: true`.
