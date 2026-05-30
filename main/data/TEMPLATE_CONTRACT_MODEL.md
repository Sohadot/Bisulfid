# Template Contract Model

**Sprint:** 6M-B  
**Scope:** 14,000-page governed launch corpus publication frame

---

## Frame hierarchy

```
base.html
├── partials/head.html (+ hreflang slot)
├── partials/governance_banner.html
├── partials/nav.html
├── partials/breadcrumbs.html
├── {{content}} ← page-type frame
│   ├── home.html
│   ├── page.html
│   ├── reference.html
│   └── term.html
└── partials/footer.html
```

---

## Required variables (build-time)

| Variable | Purpose |
| --- | --- |
| `language` | ISO language code (en, de, ar, fr, es, ja, zh) |
| `text_direction` | `ltr` or `rtl` |
| `robots_directive` | Default `noindex, nofollow` until published |
| `page_title` | Document title |
| `meta_description` | Meta description |
| `canonical_url` | Withheld or non-public until publication |
| `canonical_mode` | `withheld-non-public` or `published` |
| `route_id` | Registry route_id |
| `route_path` | Registry path |
| `route_status` | `planned` until publication sprint |
| `publication_posture` | `non_public` default |
| `indexable_flag` | `false` default |
| `in_sitemap_flag` | `false` default |
| `in_navigation_flag` | `false` default |
| `source_required_flag` | From route registry |
| `claim_approval_state` | `none_approved` default |
| `page_h1` | Primary heading |

---

## Slot rules

1. **No invented internal links** — `internal_links.json` only, published pairs only
2. **No source bar without verified sources** — slot may render posture message only
3. **No navigation items** while `navigation.json` inactive
4. **No hreflang tags** while hreflang groups inactive
5. **Governance banner mandatory** for non-public renders

---

## Page-type contracts

| Template | Required slots |
| --- | --- |
| `page.html` | `page_body`, `source_bar`, `internal_links` |
| `reference.html` | `reference_body`, `source_bar`, `safety_notice`, `internal_links` |
| `term.html` | `term_definition`, `related_terms`, `disambiguation_notice`, `source_bar`, `internal_links` |
| `home.html` | `interactive_term_map`, `language_entry_points`, `internal_links` |

---

## Fail-closed defaults

- Missing variable → build strict mode fails (future render sprint)
- Missing template → build strict mode fails
- Publication flags true on planned route → build strict mode fails
