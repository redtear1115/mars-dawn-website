# Inbox: #64 — 404 illustration + copy

**Issue:** https://github.com/redtear1115/mars-dawn-website/issues/64  
**Hotfix PR waiting:** https://github.com/redtear1115/mars-dawn-website/pull/67  
**For Claude:** wire `public/404.html` (per locale) + `wrangler.jsonc` `not_found_handling`.

## Files

| File | Use |
|------|-----|
| `64-404-illustration.svg` | **Ship this** — scalable, ~4 KB, CSP-safe, Fixed Sky palette, no text |
| `64-404-illustration-1600.webp` | Optional painterly raster (≤250 KB) — add if present on branch |
| `64-404-illustration-800.webp` | Optional srcset |
| `64-404-copy.md` | en / zh-Hant / zh-Hans / ja: headline, body, home link, alt |

## Art brief match

- Scene: lost craft + friendly alien on a ridge pointing toward the dawn limb (「宇宙迷航遇到 ET」)
- Own sky (Fixed Sky Rule); no words in the image
- Scene colours from DESIGN.md; Mars Rust only as tiny accents

## Suggested public paths (Claude may rename)

- Prefer: `public/assets/404.svg` (from inbox SVG)
- Optional rasters: `public/assets/404-1600.webp`, `404-800.webp`

Implement on the release hotfix branch (#67); do not treat this inbox-only PR as the live 404 until wiring lands.

Co-authored-by: Grok <grok@southern-light.dev>
