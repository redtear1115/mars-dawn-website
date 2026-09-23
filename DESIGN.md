---
name: MarsDawn Website
description: A new dawn for Markdown. The website of MarsDawn, extending the app's Quiet Sunrise system to the web.
colors:
  mars-rust: "#C8471B"
  mars-rust-lit: "#FF8A50"
  rust-ink: "#B03C0C"
  ember-ink-lit: "#FF9E6B"
  sunrise-rule: "#D97A4A"
  sunrise-rule-lit: "#E08A5C"
  dawn-paper: "#FFFDFB"
  dawn-sand: "#F6F0EC"
  dawn-ink: "#26211F"
  dawn-dust: "#6F6660"
  dawn-hairline: "#EADFD8"
  night-paper: "#1C1A1F"
  night-sand: "#262229"
  night-ink: "#EBE4DF"
  night-dust: "#A39992"
  night-hairline: "#3A343A"
  scene-sky-1: "#171022"
  scene-sky-2: "#372a3c"
  scene-sky-3: "#86544c"
  scene-sky-4: "#dc9a66"
  scene-glow: "#ffe1ab"
  scene-glow-mid: "#f2925a"
  scene-limb: "#fff4e0"
  scene-planet: "#0e0a13"
  hero-kicker: "#ffd9a3"
  hero-ink: "#fff8ee"
  hero-sub: "#e9dccc"
  print-paper: "#FFFFFF"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Helvetica Neue\", \"PingFang TC\", \"PingFang SC\", sans-serif"
    fontSize: "clamp(2.25rem, 6.4vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Helvetica Neue\", \"PingFang TC\", \"PingFang SC\", sans-serif"
    fontSize: "clamp(2rem, 5vw, 2.75rem)"
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: "-0.02em"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Helvetica Neue\", \"PingFang TC\", \"PingFang SC\", sans-serif"
    fontSize: "1.3rem"
    fontWeight: 650
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  subtitle:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Helvetica Neue\", \"PingFang TC\", \"PingFang SC\", sans-serif"
    fontSize: "1.05rem"
    fontWeight: 650
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Helvetica Neue\", \"PingFang TC\", \"PingFang SC\", sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.7
  lede:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Helvetica Neue\", \"PingFang TC\", \"PingFang SC\", sans-serif"
    fontSize: "1.1rem"
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Helvetica Neue\", \"PingFang TC\", \"PingFang SC\", sans-serif"
    fontSize: "0.78rem"
    fontWeight: 700
    letterSpacing: "0.08em"
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Helvetica Neue\", \"PingFang TC\", \"PingFang SC\", sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
  mono:
    fontFamily: "ui-monospace, \"SF Mono\", Menlo, monospace"
    fontSize: "0.9em"
    lineHeight: 1.45
rounded:
  chip: "4px"
  page: "6px"
  dawn: "8px"
  shot: "10px"
  plate: "16px"
  pill: "999px"
spacing:
  xs: "8px"
  sm: "14px"
  md: "16px"
  lg: "36px"
  xl: "48px"
  xxl: "64px"
  page-end: "96px"
  column: "44rem"
  text: "44rem"
  media: "min(60rem, 100vw - 32px)"
  bleed: "100vw"
  measure: "34rem"
  code-block: "14px 16px"
components:
  summary-block:
    backgroundColor: "{colors.dawn-sand}"
    textColor: "{colors.dawn-ink}"
    rounded: "{rounded.dawn}"
    padding: "20px 22px"
  contact-block:
    textColor: "{colors.dawn-ink}"
    rounded: "{rounded.dawn}"
    padding: "24px 22px"
  store-chip:
    textColor: "{colors.dawn-dust}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  link:
    textColor: "{colors.rust-ink}"
  inline-code:
    backgroundColor: "{colors.dawn-sand}"
    typography: "{typography.mono}"
    rounded: "{rounded.chip}"
    padding: "0.12em 0.36em"
  code-block:
    backgroundColor: "{colors.dawn-sand}"
    typography: "{typography.mono}"
    rounded: "{rounded.dawn}"
    padding: "{spacing.code-block}"
  shot-plate:
    backgroundColor: "{colors.dawn-sand}"
    rounded: "{rounded.plate}"
    padding: "clamp(10px, 2.2vw, 28px)"
  callout-marker:
    backgroundColor: "{colors.mars-rust}"
    textColor: "{colors.dawn-paper}"
    rounded: "{rounded.pill}"
    size: "22px"
  pdf-page:
    backgroundColor: "{colors.print-paper}"
    rounded: "{rounded.page}"
    padding: "clamp(12px, 3vw, 32px)"
---

# Design System: MarsDawn Website

## Inheritance

This system extends the app's design system, `DESIGN.md` in `redtear1115/mars-dawn`. That repository is private, and its file is the parent. The parent's North Star, palette, token names, type philosophy and brand rules apply here unless this file lists a site exception. The palette's normative source is the kit's `PreviewTheme.swift` (Dawn theme). The site mirrors those values by hand in `public/assets/site.css`.

- **Inherited unchanged:** the Dawn palette and its night variant, the Ember Rule, the Warm Neutral Rule, the System Face Rule, the AA Pair Rule, the sand-or-hairline way of separating content, and Dawn's 8px radius.
- **Site-only additions:** the scene palette (`scene-*`, `hero-*`), the one-time dawn animation, the hero's interactive app window, the annotated screenshot and the marketing layout. Each is listed under "Site exceptions" below.
- **Sync rule:** change a brand color in `PreviewTheme.swift` first, then the parent DESIGN.md, then this frontmatter and `site.css`. Last synced: 2026-09-19.

The CSS custom properties in `site.css` use short names. This is how they map to the parent's tokens:

| `site.css` | Light | Dark |
|---|---|---|
| `--ember` | `mars-rust` | `mars-rust-lit` |
| `--link` | `rust-ink` | `ember-ink-lit` |
| `--rule` | `sunrise-rule` | `sunrise-rule-lit` |
| `--paper` | `dawn-paper` | `night-paper` |
| `--sand` | `dawn-sand` | `night-sand` |
| `--ink` | `dawn-ink` | `night-ink` |
| `--dust` | `dawn-dust` | `night-dust` |
| `--hairline` | `dawn-hairline` | `night-hairline` |
| `--dawn-sky-*`, `--dawn-glow*`, `--dawn-limb`, `--dawn-planet*`, `--dawn-star` | `scene-*` (site-only) | darker scene values in `site.css` |

`--rule` (Sunrise Rule) is inherited but not used by any site component yet. Keep it so the mirror stays complete.

## Overview

**Creative North Star: "The Quiet Sunrise"** (inherited). The site expresses it as **Mars at Sunrise**.

The parent describes a native Mac window with the first light of a Martian morning inside the document: stock chrome, all the warmth in the content. The website takes the same idea one step further out. The page is the document: warm Dawn paper, brown-black ink and a single ember of Mars Rust. The sunrise, which the app only hints at in its icon, is shown at full scale exactly twice: as the full-bleed scene that opens the home page and as the band of light that closes it. Everything between them reads like a Dawn-themed Markdown page.

The mood is cinematic, restrained and honest. The hero is staged like a film's opening shot: a graded sky, a planet's dark mass, a limb of light. It plays once and then holds still. The rest of the site is quiet. It has one text column, hairline rules instead of cards, real app screenshots instead of illustrations, and system fonts, so the site feels like the app and not a web template. Because the site says what the app doesn't do, it also hides nothing about itself: the design needs no script, analytics wait for the visitor's consent and the privacy page says so, and nothing pretends to be interactive when it isn't.

Light and dark mode are designed as two separate palettes, as in the parent. The page tokens swap. The dawn scene stays dark at the top in both modes, because the scene is always night turning into dawn.

**Key Characteristics:**
- The Dawn theme, extended into a website: the same paper, ink, sand, hairline and Mars Rust as the app's default preview.
- One authored motion moment per surface. It runs once, never loops and is optional. The loop animation under the home page's loop steps is the one exception (see Loop Animation).
- Full-bleed dawn at the opening and close of the home page. Dawn-paper reading everywhere else.
- Hairline rules and sand plates carry the structure. There are no cards and no shadows on interface elements.
- System fonts only, and a strict CSP: no web fonts or inline styles, and no script in the design itself. The only scripts are the consent banner and consented analytics.

## Colors

The Dawn palette, inherited whole, plus a scene palette that exists only on the website.

### Primary (inherited)
- **Mars Rust** (`mars-rust` / `mars-rust-lit`): the brand ember. On the site it marks callout markers, list bullets, focus outlines, text selection and the lit middle step of the loop. It is never a fill larger than a marker dot.
- **Rust Ink** (`rust-ink` / `ember-ink-lit`): the link color, a deeper sibling of Mars Rust that holds AA contrast for text (5.9:1 on Dawn Paper, 8.5:1 on Night Paper).
- **Sunrise Rule** (`sunrise-rule` / `sunrise-rule-lit`): decorative only, never used for text. The site doesn't use it yet.

### Neutral (inherited)
- **Dawn Paper / Night Paper**: the page background. Light mode is a warm white, never `#FFFFFF`. Dark mode is a violet-tinged night.
- **Dawn Sand / Night Sand**: the one tonal step up, used for the summary block, code, `pre` and the screenshot plate.
- **Dawn Ink / Night Ink**: body text and headings (15.7:1 on paper).
- **Dawn Dust / Night Dust**: secondary text such as ledes, captions, footer, the language switch and trait descriptions (5.5:1 on paper, 5.0:1 on sand).
- **Dawn Hairline / Night Hairline**: every rule and border.

### Scene (site-only)
- **Sky** (`scene-sky-1` to `scene-sky-4`): a graded night-to-dawn sky, from deep violet-black through mauve to an apricot horizon. Dark mode deepens it and makes the horizon burn toward Mars Rust.
- **Glow and Limb** (`scene-glow`, `scene-glow-mid`, `scene-limb`): the horizon's light and the thin bright rim along the planet's edge. These are the same idea as the app icon's sun on its ridge.
- **Planet** (`scene-planet`): the planet's near-black mass. It is also the soft scrim behind the hero copy.
- **Hero Text** (`hero-kicker`, `hero-ink`, `hero-sub`): fixed, light, warm text colors for anything set on the scene.
- **Print Paper** (`print-paper`): pure white, used only behind an exported PDF page. It matches the parent's rule that print and PDF output use white paper.

### Named Rules
**The Ember Rule** (inherited). Mars Rust appears only where attention belongs: markers, bullets, focus, selection and the lit loop step. It never fills a background.

**The Warm Neutral Rule** (inherited). Neutrals lean toward rust in light mode and violet in dark mode. There is no pure white or black, except Print Paper, which depicts a printed sheet.

**The Fixed Sky Rule** (site). Anything set on the scene uses the hero text palette in both color schemes. Page tokens are never used on the sky.

## Typography

**Font:** Dawn's system stack (SF Pro through `-apple-system`), with PingFang TC/SC fallbacks, for every text role. Mono is SF Mono (`ui-monospace`), falling back to Menlo. Han characters differ by language, so `site.css` swaps the CJK font by `lang`: PingFang TC for zh-Hant, PingFang SC for zh-Hans, Hiragino Sans for ja. The language-switch links carry their own `lang` and follow the same rule.

**Character:** one native family doing all the work, as in the app's Dawn theme. Hierarchy comes from weight (400, 650, 700), size and slightly tightened tracking on large sizes.

### Hierarchy
- **Display** (`typography.display`): the home page hero headline only. It carries a soft text shadow so it holds up against the sky.
- **Headline** (`typography.headline`): the `h1` on every other page, set with `text-wrap: balance`.
- **Title** (`typography.title`): section headings (`h2`). The home page's loop heading steps up to `clamp(1.6rem, 3.6vw, 2.15rem)`.
- **Subtitle** (`typography.subtitle`): `h3`, and the step names in the loop.
- **Body** (`typography.body`): running text in a column capped at 44rem. Bold is 650, as in the parent.
- **Lede** (`typography.lede`): the intro paragraph under each `h1`, in Dust, capped at 34rem.
- **Label** (`typography.label`): the uppercase kicker above the hero headline. It is the only uppercase text in the system, apart from the footer's origin mark ("© 2026 · MADE IN TAIWAN"), which the owner set in capitals and leaves untranslated on purpose.
- **Caption** (`typography.caption`): the date stamp, figure labels, footer and language switch.

### Named Rules
**The System Face Rule** (inherited). No bundled or web fonts. The site's CSP enforces this too.

**The Weight-Not-Size Rule** (site). Subheadings step up in weight (650) before they step up in size. The type scale stays compact under the headline.

## Layout

The site is a single reading column: `max-width: 44rem`, centered, with a 16px side gutter and 96px of space at the end of the page. Ledes and the closing band's paragraph narrow to a 34rem measure. The vertical rhythm is set by section breaks: 48px above each `h2`, 36px around blocks such as the summary, contact and screenshot, and 64px before the footer and the trait list.

Widths come in exactly three tiers, one per kind of content, as tokens on `:root` in `site.css`. Every block on every page takes one of them, and all of them share one centre axis:

| Tier | Token | Value | What takes it |
|---|---|---|---|
| Text | `--w-text` | `44rem` (a 42rem measure inside the 16px gutter) | Prose, the loop steps, the install block, the trait list, masthead and footer |
| Media | `--w-media` | `min(60rem, 100vw - 32px)` | Every picture of the app: the hero window, the loop animation's plate, each screenshot's sand plate |
| Bleed | `--w-bleed` | `100vw` | The dawn scene and the closing band |

A new block picks a tier by what it is, never a width of its own. Media never goes narrower than the text column, and the media edges line up with each other at every width, because they all subtract the same 32px. The dawn scene and the closing band are centred with a negative margin (`margin-left: calc(50% - 50vw)`), not a transform, because a transform would trap the theme menu's full-page click-catcher inside the hero; and `html { overflow-x: hidden }` absorbs the rounding from classic scrollbars. Ledes and the closing band's paragraph narrow to the 34rem measure inside their tier; that is a measure, not a fourth tier.

Screenshot callouts sit *outside* the media plate, in a 12rem gutter on each side, so the figure is 84rem wide in that mode. Leader lines appear only from 1392px (60rem + 24rem of gutters + room for a classic scrollbar). Narrower, the plate keeps its full media width and the markers are numbered, with the list below. The plate never shrinks to make room for labels.

Responsive behavior is planned, not just squeezed. Below 480px the masthead wraps the brand onto its own line. Below 720px the three-step loop stacks. At 1392px the annotated screenshots change from numbered markers with a list below to leader lines with labels in the gutter.

## Elevation & Depth

The interface is flat and tonal, as in the parent. Depth comes from one tonal step (paper to sand) and hairline rules. The site makes one exception, because it shows things the app doesn't: pictures of physical objects cast shadows, and nothing else does.

### Shadow Vocabulary (site exception)
- **Screenshot rest** (`0 1px 2px` at 12% black, then `0 14px 34px -14px` at 35% black): an app window on its sand plate.
- **Hero window** (a 22% black 1px ring, a 12% white inset top edge, `0 40px 64px -28px` at 70% black and `0 14px 28px -14px` at 55% black): the interactive app window resting on the dawn scene.
- **Printed page** (`0 1px 2px` at 10% black, then `0 12px 28px -14px` at 30% black): an exported PDF page.
- **Marker halo** (a `3px` paper-colored ring, then `0 1px 3px` at 30% ink): separates a callout dot from the screenshot underneath.

### Named Rules
**The Flat Page Rule** (inherited). Interface elements never get shadows, blur or glass. Use the sand tone or a hairline instead.

**The Real Objects Rule** (site exception). Only depicted objects cast shadows: screenshots, the hero's app window, printed pages and markers pinned to them. Blocks, chips, links and lists never do, and hover never adds one.

## Shapes

The site uses Dawn's gentle rounding and scales it by object: 4px for inline code and `kbd`, 6px for a printed page, 8px (Dawn's radius) for the summary, contact and code blocks, 10px for a screenshot inside its plate, 14px for a depicted macOS window (the hero window, the loop's window; the hero window steps down to 12px on phones, where it is drawn smaller), 16px (`--r-plate`) for every sand plate (screenshots and the loop animation), and a full pill for the store chip and markers. Borders are always 1px hairlines. The only exception is `kbd`, which has a 2px bottom border so it reads as a physical key. Recurring shapes are the circle (callout markers, loop dots, numbered list badges) and the horizontal rule (masthead, loop steps, trait list, footer).

## Components

### Links
Links use Rust Ink and a 1px underline at a 0.18em offset. On hover the underline thickens to 2px. Focus shows a 2px Mars Rust outline with a 3px offset. Footer and language-switch links use Dust.

### Store Chip
A quiet status pill: a hairline border, Dust text in the caption size and no fill. It is a statement ("Coming soon to the Mac App Store"), not a button, and it has no hover state.

**Launch exception (owner, 2026-09-20, confirmed 2026-09-23):** on and after launch, the trait pages' store chip links to the App Store listing; everywhere else a chip is still a statement. The linked chip keeps the pill look, with no underline and no fill, and gains what a link needs: a tap target at least 24px tall, a hover that darkens the border to Dust and the text to Ink, and the same 2px Mars Rust focus ring as every other link.

### Summary Block
The one-line answer people came for, on a sand plate with Dawn's 8px radius and no border, in slightly larger text (1.05rem).

### Install Block (the one card)
The home page's CLI install is a sand plate at the text width, with Dawn's 8px radius, a heading, the command on paper, and a row of links. It is the only block on the site that works like a card, and it is allowed because it is the one thing a visitor can do today. Nothing else gets this treatment. The closing band ends with a plain link back to it, in the hero palette.

### Contact Block
A hairline-bordered box with an 8px radius on the support pages. The email address is shown larger, at `clamp(1.05rem, 5.5vw, 1.25rem)`, so it fits on one line on the narrowest phones.

### Code, Pre and Kbd
These use the same treatment as the app's Dawn preview: sand background and SF Mono, with `pre` padded `14px 16px`. Short tokens are kept whole with `inline-block` so they wrap as a unit. `pre` scrolls horizontally instead of wrapping. `kbd` is a small paper-colored keycap with a heavier bottom edge.

### Navigation
The masthead has the app icon (40px) and the name set in 650 weight on the left, with the store chip and the language switch on the right, over a hairline underline. The current language is shown in Ink at 600 weight with `aria-current`. Every tap target is at least 24px tall. The footer is a wrapping row of Dust links under a hairline rule.

### Annotated Screenshot (site signature)
A real app screenshot sits on a sand plate at the media width. Mars Rust markers are pinned to points on the app. At 1392px and wider, thin 1px Mars Rust leader lines run from each marker to a label in the side gutter, and the caption list stays available for screen readers only. Below that width, the markers are numbered and the labels become a numbered list with matching badges. Marker positions are generated into `annotations.css` so no inline style is needed. Below 1392px the numbered list sits on the text tier under the plate, because it is prose. A screenshot follows the Mac's appearance once a Dark Mode capture of the same window, document and crop is saved beside it as `<image>-dark-<width>.png` at both widths; `build_pages.py` then wraps it in a `<picture>`. Until then it stays light, which is why the dark-mode page still shows light screenshots. As the page settles, each marker sends out a single ring.

### The Loop (site signature)
The home page presents the agent loop as three stops along one horizon line, not as three cards. Each step has a hairline top rule with a small Dust dot. The middle step, where the person reads, is lit: its rule is tinted with Mars Rust and its dot is Mars Rust with a soft halo.

### Loop Animation (site exception)
Under the three steps, a 10-second drawing plays the loop, at the owner's request (2026-09-24): a terminal types `marsdawn open launch-note.md`, a MarsDawn window opens beside it, the reader clicks one outline row and changes the launch day, the agent changes the other two sections to match, and the window folds back into the terminal. The last frame is the first, so it loops without a jump. It breaks two rules on purpose: it loops, and it is a drawing rather than a screenshot. Everything else holds. It is HTML and CSS from `scripts/loop_anim.py` (generated into `loop.css`), with no script and no inline style. Its lengths are in a container-query unit, so it scales without measuring. Every word is page text in the visitor's language; the sidebar's tab names are the app's own strings, and the command and file name stay English as in the app. A pause control (a checkbox read with `:has()`) sits under the frame, as WCAG 2.2.2 asks of motion longer than five seconds. With `prefers-reduced-motion` the drawing holds on the edited note and the control is hidden. It takes the media width, the same edges as the hero window, on a `--sand` plate with the plate radius. The window follows the Mac's appearance, as the hero window does: the Dawn theme's light palette, or its night one (owner, 2026-09-25). The terminal is dark in both. The loop starts with the window already open (`--t: 2.4s`), so the frame never scrolls into view empty. Below 820px the whole stage would set its text under 10px, so the frame crops to the source and preview panes at a larger scale, with the terminal docked along their foot. Below 560px it crops again, to the source pane alone, where both the reader's edit and the agent's show, with a narrower terminal under it. That keeps the text at about 15px on a phone. The outline pane and the pointer fall outside both crops, and the story (edit one day, the agent fixes the rest) still reads. The terminal's reply lands only after both of the agent's edits have. The pause control sits under the frame's right edge, which is the media tier's edge. Its Mars Rust tab and selected row depict the app's own accent, so the Ember Rule's limit on fills doesn't apply inside the drawing, as it doesn't inside a screenshot.

### Trait List
Links to the other pages, set as a ruled list: a 600-weight link and a Dust description on one baseline, separated by hairlines. It uses no cards and no icons.

### Interactive App Window (site signature, site exception)
The home page hero shows a working MarsDawn window instead of a screenshot, at the owner's request (2026-09-21), drawn as close to the app's macOS 26 window as the page allows (owner, 2026-09-22). The title bar has the coloured traffic lights and the document's title as the app gives it to the Welcome guide. The toolbar has the app's two controls, icons only: a palette button with a chevron that opens the app's Theme menu (`StyleMenu.combinedMenu()`, issue #100), and and a three-segment Layout control (source, split, preview icons, the active segment tinted), whose tooltips are the app's own ("Source Only (⌘1)"). The icons are drawn for this site in the app's spirit, not copied from SF Symbols. The menu is laid out as the app's is, in its order: an Appearance section (System, Light, Dark), a Preview Theme section with a Light and a Dark subsection that each list the four themes, and Settings…. It is drawn as a native menu: section headers, a checkmark column, separators, 22px rows, and the highlighted row in the system accent. Each theme's tooltip is the kit's summary. Settings… is shown only for the likeness: it is dimmed, hidden from assistive technology, and does nothing, because the page has no settings to open. The menu never runs past the window's foot; if it would, it scrolls. The theme section for the appearance that isn't showing steps back to a muted colour that still holds 4.5:1. It stays choosable, because the choice takes effect when the appearance changes, but it isn't read as a click that did nothing. A click anywhere outside the open menu closes it, as a native menu's does: a clear, full-page layer behind the menu turns that click into one on the palette button (Escape would need a script). For the layer to reach the whole page, no ancestor of the window may have a transform, and the loop drawing isolates its own stacking so none of its layers rise above it. On touch screens the rows grow from 22px to 24px, which meets WCAG 2.5.8. The window's panes are never shorter than the open menu needs (380px, 410px on touch and on phones), so the menu never has to scroll. The checked row in the muted section keeps its full colour, so the current choice there stays readable. Appearance and both theme choices are radio groups, like the Layout control, and the CSS reads them with `:has()`. Light or Dark sets the window's own `color-scheme`, and System follows the Mac. Every colour in the window is `light-dark()` of the theme picked for Light and the one picked for Dark, so the window shows the theme chosen for the appearance it is in, as the app does. A theme's font and shapes are not colours, so `hero_window.window_css()` writes them for each way that theme can be on show. The window has no colour transition: Chrome doesn't restart one when only the color-scheme under a `light-dark()` value changes, and the app switches instantly too. The menu is a `<details>`, so it opens and closes from the keyboard. The window needs no script and no inline style, keeps the browser's own keyboard handling (Tab into a group, arrow keys to choose) and draws its focus ring in the chosen theme's accent. It opens on System, Dawn for both appearances, and Split. Below 500px it shows one pane, Split shows the rendered page, and the title gives way to the toolbar.

It is a depiction of the real app, not a mockup of an imagined one, and that is what the exception rests on: every fact it shows comes from the app or the kit, never from this site. The themes' colours and fonts are the kit's `PreviewTheme.swift` at the kit tag the app ships, generated into `hero.css`; the theme and control names are the app's strings in each language; the document is an excerpt of the app's own Welcome guide (the title, the Layouts table and the Writing section; the title's paragraph is left out because it invites an edit the page can't take), rendered by the kit's renderer. `scripts/sync_hero_sources.py` copies them into `scripts/hero_sources.json`, and CI (`scripts/check_hero.py`) fails if the page and the snapshot disagree. The source pane is the app's editor: its monospaced font, and its highlighting taken from `MarkdownHighlighter.swift` (the patterns, their order and what each one styles) and `EditorTheme.swift` (which palette colour each role uses). The themes' shapes follow the kit's `preview.css`. The title bar, toolbar and menu are the system's, not the theme's, as in the app: white in light appearance and a dark glass in dark appearance whatever the theme, following the appearance chosen in the menu as well as the Mac's. Their colours were measured pixel by pixel from the app captures in `assets/screens/` (01-split, 03-dark), not chosen, and are the one set of values here that no source file holds. Page tokens never reach inside the window: it is the app's palette and the Mac's chrome, not the site's.

### Dawn Scene and Dawn Close (site signature, site exception)
The hero is an inline SVG: a graded sky, a horizon glow, the planet's mass with a lit rim, and three star layers. The kicker, headline, lede and the app window sit on top of it, over a feathered radial scrim in the planet's dark tone. On load the night veil lifts, the glow rises, the stars go out faintest first and the limb lights from the center outward. It takes 4.5s or less, runs once and animates only opacity, transform and clip-path. The resting state is the final frame, so visitors with `prefers-reduced-motion` see the finished dawn. The page closes with a full-bleed band in the same sky, with a sunrise glow low beneath the tagline.

## Do's and Don'ts

### Do:
- **Do** take brand colors from the parent's Dawn palette and keep `site.css` in sync with `PreviewTheme.swift`. Every new token needs a light and a dark value.
- **Do** keep Mars Rust (`#C8471B` / `#FF8A50`) as the only accent. It marks, points and focuses.
- **Do** keep every page to one 44rem reading column, and break out of it only for the dawn scene, the closing band and screenshots.
- **Do** keep text on the scene in the fixed hero palette in both color schemes.
- **Do** show the real app. Use actual screenshots annotated with markers and leader lines, not illustrations or mockups. The hero's interactive window is the one exception, and only because everything it shows is generated from the app and the kit (see Interactive App Window).
- **Do** make any motion a single authored moment that plays once, animates only compositor-friendly properties and has a finished resting state under `prefers-reduced-motion`. The loop animation is the one that repeats, and it can be paused.
- **Do** keep text contrast at WCAG AA or better in both schemes, and keep tap targets at least 24px tall.

### Don't:
- **Don't** use cards, drop shadows or hover lifts on interface elements. Structure comes from hairlines and sand plates.
- **Don't** add web fonts, scripts, inline styles or third-party resources beyond the consent banner and Google Tag Manager. The CSP in `public/_headers` forbids them.
- **Don't** give a block a width of its own. Pick the text, media or bleed tier.
- **Don't** add a second accent hue, or use Mars Rust as a large fill.
- **Don't** use pure white or black outside Print Paper, or cool greys anywhere.
- **Don't** loop, repeat or scroll-trigger animation, apart from the loop animation (owner, 2026-09-24). The dawn happens once.
- **Don't** invert the dawn scene for dark mode. The sky is always night breaking to dawn.
- **Don't** introduce a site-specific token for a color the parent already defines.
