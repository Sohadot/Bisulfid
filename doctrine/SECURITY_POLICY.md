# SECURITY POLICY

This document governs security posture for bisulfid.com.

It is subordinate to `ASSET_THESIS.md` and `PROJECT_DOCTRINE.md`.

---

## Core Posture

bisulfid.com is a static sovereign reference asset.

Security posture: static-first, dependency-minimal, trust-governed.

---

## Architecture Rules

- Static HTML, CSS, and vanilla JavaScript only.
- No public CMS.
- No server-side login.
- No server-side code execution in production.
- No database in production.
- No unverified external scripts.
- No inline JavaScript in production pages.
- No secrets in the repository.

---

## Content Security Policy

A Content Security Policy (CSP) header is required before production launch.

CSP must:

- Restrict script sources to trusted, named origins only.
- Block `eval()` and inline scripts.
- Restrict style sources.
- Restrict frame sources.
- Report violations.

No deployment proceeds without a verified CSP.

---

## Dependency Rules

- No dependency is added without doctrine review.
- Build-time dependencies must be minimal and auditable.
- No runtime dependencies from external CDNs without trust verification and SRI hash pinning.
- All external resources are reviewed before inclusion.

---

## Repository Rules

- No secrets, credentials, API keys, or tokens are committed to the repository.
- No environment files with secrets are committed.
- The repository is public. All committed content is treated as public.

---

## DNS and Hosting

- DNS managed through Cloudflare.
- TLS enforced at all layers.
- Cloudflare security settings reviewed before launch.
- No mixed content.

---

## Supply Chain

- No build tool is added without review.
- Build tools are pinned to specific versions.

Validator: `validate_supply_chain.py`

---

## Reporting

Security issues are reported to: agent@sohadot.com

This address is for verified security concerns. It is not a general inquiry address.

---

## Validation

Security gate is validated by `validate_security.py`.

Gate 06 of the Quality Gate requires zero security policy violations before deployment.
