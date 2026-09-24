# #87 — `.mdw` liquid-glass chrome (design inbox)

For Claude. Implement on `main`; **do not merge** unless the owner asks. Parent issue: https://github.com/redtear1115/mars-dawn-website/issues/87

## Goal

Make the hero’s interactive MarsDawn window (`.mdw`) read like **macOS 26 liquid-glass window chrome**: thin, warm, translucent title bar and rim over the dawn scene. **Document panes stay opaque Dawn paper.**

## Do / Don’t

| Do | Don’t |
|----|--------|
| Glass on `.mdw-bar` + outer `.mdw` rim | Frost the page, masthead, footer, loop, install block |
| Opaque `.mdw-source` / `.mdw-preview` | Translucent editor/preview (kills AA + “real app” read) |
| Warm Dawn-tinted fill + blur + bright edge | Cold grey iOS glass, rainbow refraction, liquid morph |
| `backdrop-filter` in `hero.css` / `site.css` | Inline styles that break CSP; third-party assets |
| Reduced-motion / narrow → opaque fallback | Blur-only design with no fallback |

## Suggested CSS approach (non-normative sketch)

Claude may adjust tokens to match `site.css` / `hero.css` variables.

```css
/* Desktop + motion OK */
@media (min-width: 700px) and (prefers-reduced-motion: no-preference) {
  .mdw {
    /* keep existing depth shadow; add bright rim */
    box-shadow:
      0 0 0 1px color-mix(in srgb, var(--hero-ink) 22%, transparent),
      /* existing hero window shadows… */;
    background: color-mix(in srgb, var(--paper, #fffdfb) 55%, transparent);
  }
  .mdw-bar {
    background: color-mix(in srgb, var(--paper, #fffdfb) 42%, transparent);
    backdrop-filter: blur(28px) saturate(1.4);
    -webkit-backdrop-filter: blur(28px) saturate(1.4);
    border-bottom: 1px solid color-mix(in srgb, var(--hero-ink) 12%, transparent);
    /* optional top specular */
    box-shadow: inset 0 1px 0 color-mix(in srgb, #fff 55%, transparent);
  }
  .mdw-panes,
  .mdw-source,
  .mdw-preview {
    background: var(--paper); /* solid — do not glass */
  }
}

/* Fallback: reduced motion or narrow */
@media (max-width: 699px), (prefers-reduced-motion: reduce) {
  .mdw-bar {
    background: var(--sand); /* or solid paper */
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }
}
```

Dark mode: use night paper / night sand mixes so glass stays warm-violet, not blue-grey.

## Verification

1. EN home, light + dark, ~1280px: title bar shows dawn through blur; panes readable.
2. 375px or reduced-motion: no reliance on blur; no CLS jump.
3. Keyboard focus on theme/layout controls still visible (ember/accent ring).
4. `check_hero.py --kit --self-test` and site CI green; CSP unchanged unless a deliberate hash/update is required (prefer none).

## Out of scope

Copy/CTA changes; annotated screenshots; `1001-go-live` merge work.

Co-authored-by: Grok <grok@southern-light.dev>
