# Template Multilingual Rendering Model

**Sprint:** 6M-B  
**Target:** 14,000-page multilingual governed corpus

---

## Language readiness matrix

| Language | Code | Direction | Frame readiness |
| --- | --- | --- | --- |
| English | `en` | LTR | **Ready** (primary source) |
| German | `de` | LTR | **Ready** (identity priority) |
| Arabic | `ar` | RTL | **Ready** (`dir="rtl"`) |
| French | `fr` | LTR | **Future-ready** |
| Spanish | `es` | LTR | **Future-ready** |
| Japanese | `ja` | LTR | **Future-ready** |
| Chinese | `zh` | LTR | **Future-ready** |

---

## Shell requirements

```html
<html lang="{{language}}" dir="{{text_direction}}">
<article lang="{{language}}" dir="{{text_direction}}">
```

Build engine must set `text_direction` from language policy:

- `ar` → `rtl`
- all others in current scope → `ltr`

---

## hreflang partial

- Status: **inactive** (no tags emitted)
- Activates only when:
  1. `hreflang_groups.json` status active
  2. Two or more published language routes in group
  3. x-default points to EN source route

---

## Footer and governance strings

Future sprint adds localized governance strings. Frame uses `{{language}}` slot; English default in 6M-B.

---

## Scale note

14,000 pages span multiple language waves. Template frame is **language-agnostic** — content and route registries carry locale metadata; shell preserves locks per route regardless of language.

---

## RTL layout checklist

- [x] `dir="{{text_direction}}"` on html and article
- [x] No hard-coded LTR-only CSS in templates (no CSS in 6M-B)
- [ ] RTL typography polish (future UI sprint)
- [ ] Arabic governance string localization (future)

---

## Translation status boundaries

| `translation_status` (route) | Template behavior |
| --- | --- |
| `source_planned`, `draft`, `planned` | Render as non-public; no hreflang emission |
| `published` (future) | Only then may alternate language links activate under hreflang gate |
| Missing field | Do not assume published; use route `status` and locks |

Templates must **never** treat `translation_status` alone as permission to render indexable or public output.

---

## Empty language folder boundaries

| Condition | Template / build rule |
| --- | --- |
| Language directory exists but has zero published routes | **Not published content** — do not list in nav, sitemap, or hreflang |
| Language folder with drafts only | Render only under quarantined QA with governance banner |
| Empty `main/content/{lang}/` tree | **No inference** — absence of files is not a launch blocker display in templates |

**Empty language folders must not be treated as published content.** The frame remains language-ready via `{{language}}` and `{{text_direction}}`; content presence is a separate governed fact from route registry and publication locks.
