# Product

<!-- impeccable:product-schema 1 -->

## Inheritance

This file is the website's layer on top of the MarsDawn app's product record, `PRODUCT.md` in `redtear1115/mars-dawn`. That repository is private, and it is the parent: app facts such as features, pricing, themes, requirements and brand commitments are decided there. Here they are mirrored, and only the facts this site needs are carried over. Everything else in this file is about the website itself.

- When an app fact changes, update the parent first, then this file, then the site copy in `scripts/build_pages.py`.
- If this file and the parent disagree about the app, the parent wins. Treat the difference as a bug in this file.
- Last synced with the parent: 2026-09-19.

## Platform

web

(The app itself is a native macOS app. This record covers its website.)

## Users

The app's users (from the parent): developers and technical writers who edit READMEs, project docs and design notes in Markdown, reading and writing in both Traditional Chinese and English.

The site's primary visitors are a narrower group. They are developers who work with AI coding agents or writing assistants (Claude Code, Cursor and the like) and need to review the Markdown those agents write. They are on a Mac, deciding whether MarsDawn deserves a place in their review loop.

Secondary visitors arrive from search with a narrow job, such as "view Markdown on a Mac" or "Markdown to PDF on a Mac". The CLI solves that job today. These visitors matter, but they don't set the site's direction.

AI assistants and crawlers read the site too, through `llms.txt`, `llms-full.txt`, `product-facts.md` and the `index.md` twin of every page.

## Product Purpose

The site is the public home of MarsDawn, a native Mac Markdown editor with live preview, Mermaid diagrams, KaTeX math and PDF export, built for reading what AI agents write. The app will be sold only through the Mac App Store and is coming soon. The free `marsdawn` CLI can be installed today.

While the app is still unreleased, the site succeeds on two things:

1. Building intent to buy the app when it launches.
2. Search and AI visibility: Google and LLMs understand MarsDawn correctly and cite it accurately.

The privacy and support pages also serve App Store review. They must stay stable and reachable.

## Positioning

These are the app's four differentiators, inherited from the parent:

1. **Native feel and speed.** A genuine AppKit and TextKit 2 editor, not Electron or a wrapped web editor.
2. **Siri, Shortcuts and Spotlight integration** through App Intents.
3. **Distinct preview themes**: Dawn, Classic, Modern and Vivid, each with a light and a dark palette.
4. **Free to try, one-time unlock.** No subscription.

The site leads with one angle on top of them. MarsDawn is the careful-read step in an agent loop: the agent writes, you review the source and the rendered page side by side, and the agent revises. Agents can drive the app directly through the free `marsdawn` CLI, which returns JSON. The app is not an AI product: it contains no AI model of its own.

## Operating Context

- Visitors come from search results, AI assistant answers, the App Store (the privacy and support links) and agent tooling (the CLI reference and agent skill pages).
- The site is static and served from Cloudflare Workers static assets. `release` deploys and `main` holds the latest work.
- Page copy lives in `scripts/build_pages.py`, which generates the HTML and a Markdown twin of each page. CI fails if the regenerated output differs from the committed output.

## Capabilities and Constraints

**App facts, from the parent**
- **Pricing**, decided 2026-09-19 but not built yet: a free download with a 14-day trial, then a USD 4.99 unlock. Both are In-App Purchases and both are one-time: no subscription and no account. After day 14 without the unlock, documents still open but their content is covered in the app. The lock never changes files on disk, Quick Look keeps showing them, and the free `marsdawn export` CLI keeps exporting them.
- **Requirements**: the app needs macOS 26 (Tahoe) or later, on Apple silicon or Intel. The `marsdawn` CLI needs macOS 15 or later, and `marsdawn export` works without the app installed.
- **Themes**: four preview themes, Dawn (the default), Classic (典雅), Modern (流行) and Vivid (活潑).
- **Limits**: no sync, no iPhone or iPad app (a read-only iPhone viewer is a future plan), no plugins and no accounts.

**Pricing copy ahead of launch:** the site describes the decided model (free download, 14-day trial, USD 4.99 one-time unlock) before the app or its purchase ships. That is intentional: every page says the app is coming soon, so this copy previews the model rather than claiming it is live. Keep it in step with the parent if the model changes again.

**Site constraints**
- The site ships in four languages: English, Traditional Chinese (`/zh-hant/`), Simplified Chinese (`/zh-hans/`) and Japanese (`/ja/`). English and Traditional Chinese are the primary editions. From 1.0.0 the app's interface ships in eight languages (these four plus German, French, Spanish and Korean); the site publishes in four, and states the app's languages only through `APP_UI_LANGUAGES` (see the UI-labels rule below).
- The CSP in `public/_headers` allows no scripts, same-origin stylesheets and images and system fonts only. No web fonts, inline styles, forms, frames or third-party resources. Anything that needs one of these must change the CSP deliberately.
- `/privacy/`, `/support/`, `/zh-hant/privacy/`, `/zh-hant/support/`, `/zh-hans/privacy/`, `/zh-hans/support/`, `/ja/privacy/` and `/ja/support/` are public contracts linked from the App Store. They must stay at the same paths.
- `/themes/v1/` is reserved for the future theme gallery.
- UI labels quoted on the pages must match the app's strings in the page's language (the app ships all four of the site's languages from 1.0.0). Nobody checks this automatically, except in the home page's interactive window: its theme names, control labels, colours and sample document come from the app and the kit through `scripts/hero_sources.json`, and CI checks the page against it (`scripts/check_hero.py`). When a page in Simplified Chinese or Japanese needs to state which languages the app's interface comes in, use the single `APP_UI_LANGUAGES` constant in `scripts/build_pages.py` rather than writing a new sentence — it already carries the correct phrasing for every locale.

## Brand Commitments

These are inherited from the parent and binding:
- The name is **MarsDawn**.
- The slogan is **"A new dawn for Markdown."**
- The brand palette is Mars rust and orange with a dawn gradient. The accent is Mars Rust, `#C8471B` in light mode and `#FF8A50` in dark mode.

These are specific to the site:
- The CLI is `marsdawn` in lowercase. The open-source kit is mars-dawn-kit, licensed Apache-2.0.
- The voice is plain, factual and specific. The site says what the app doesn't do before anyone buys ("Know before you buy").
- The MarsDawn name and app icon are not covered by the site's licenses. Site copy and images are CC BY 4.0.

## Evidence on Hand

- App screenshots in `public/assets/screens/`: split view, the Classic, dark and Vivid themes, and a PDF export, each at two widths.
- CLI assets in `public/assets/cli/`.
- The app icon (`public/assets/icon-192.png`, `favicon-64.png`): a sun cresting a dark ridge.
- The mars-dawn-kit repository and the Homebrew install (`brew tap redtear1115/tap && brew install marsdawn`).
- Not available: the app is unreleased, so there are no testimonials, reviews, user counts, press or ratings. None may be invented, and no claim may go beyond what the parent confirms.

## Product Principles

1. **Tell the truth, especially about limits.** Accurate beats persuasive. What MarsDawn doesn't do is part of the pitch.
2. **Built for the agent loop.** Every page should make the loop of write, review and revise feel concrete.
3. **Readable by machines as well as people.** Keep the Markdown twins, `llms.txt` and the product facts accurate and in sync with the HTML and with the parent.
4. **Static, private and fast.** No scripts, no tracking and no third parties, the same privacy stance as the app.
5. **Two languages, one product.** English and Traditional Chinese are equal editions, not a primary and a translation. This is inherited from the parent and describes the *app's* interface. The site additionally publishes in Simplified Chinese and Japanese (see Site constraints) to reach readers beyond the app's own UI languages — that extension is the site's own choice, not a claim about the app.

## Accessibility & Inclusion

- The site must meet WCAG AA. The version (2.1 or 2.2) hasn't been confirmed, so WCAG 2.2 AA is the working target. The parent requires AA text contrast for every theme, and the site holds its own pages to the same bar.
- Both language editions must meet it, including correct `lang` attributes.
- Motion must respect `prefers-reduced-motion`, as the app respects Reduce Motion.
