# Bisulfid Motion Engine

Vanilla JS motion governance for the design system.

## Sprint 6N-A scope

- `motion-governor.js` — visual motion states only
- Respects `prefers-reduced-motion`
- No network calls, no analytics, no DOM mutation of source/claim truth
- Fail-safe when JS disabled (static CSS remains)

## WebGL / WebXR boundary (deferred)

WebGL and WebXR are **not** implemented in Sprint 6N-A. Future prototypes must:

1. Wait until static token/component system is integrated and validated on live pages
2. Never override source-required visibility or governance banners
3. Remain optional progressive enhancement
4. Use separate engine module under `bisulfid-design-system/engine/webgl/` (future sprint)
5. Pass dedicated validators before any public integration

Static chemical-space depth uses CSS tokens in `tokens/depth.css` only.
