# Make a theme with your agent

A reference for an AI agent that makes a MarsDawn preview theme. The agent writes one `theme.json`, checks and renders it with the `marsdawn` command-line tool, and hands you a link. You tune it by eye on the [Build a theme](/themes/new/) page and submit it. The field tables below are read from the kit's own source, and a check keeps them equal to it.

**Write one `theme.json`, run `marsdawn theme validate theme.json --require-complete --json` until it exits 0, render it with `marsdawn theme preview` in light and dark, then give the person a link.** A theme is parameters only. It never contains CSS.

## What a theme is

- **Colours** for light and for dark: a base palette, and optional syntax and diagram colours. Each is `#RRGGBB`.
- **A font design**: `sans`, `serif` or `rounded`.
- **A closed set of style options**: numbers inside fixed ranges, and choices from fixed lists. A colour in a style option is always a palette role such as `accent`, never a literal colour.
- **Display strings**: a name and a summary, and optionally an author and a licence.

A key that is not in the tables below is an error, and so is a key written twice. The file is at most 16,384 bytes.

## Check and render

Run these in the folder that holds `theme.json`. They need the `marsdawn` tool: see [marsdawn for agents](/cli/agents/).

```
marsdawn theme validate theme.json --require-complete --json
marsdawn theme css theme.json --json
marsdawn theme preview theme.json --appearance light -o light.png
marsdawn theme preview theme.json --appearance dark -o dark.png
```

- Exit codes: 0 valid, 1 invalid with rule ids, 2 file not found, 64 usage error. `preview` adds 4 when the PNG already exists (pass `--force` or choose another name) and 5 when rendering fails.
- With `--json`, an invalid theme lists its problems under `issues`, each with a `rule` id, a `path` and a `message`. Fix them and run it again.
- `--require-complete` is the check for a theme that will be published: it also requires the `syntax` and `diagram` colours in both palettes.
- `css` prints the CSS the preview serves. `preview` renders a sample document to a PNG. Both validate first, so an invalid theme renders nothing.
- Look at the light and the dark PNG before handing the theme over.

## Start from a built-in

Copy one of the four built-in themes and change it. Each is a complete, valid file:

- [`/assets/theme-sim/kit/themes/dawn.json`](/assets/theme-sim/kit/themes/dawn.json): the default, and the example below
- [`/assets/theme-sim/kit/themes/classic.json`](/assets/theme-sim/kit/themes/classic.json): a plainer, document-like palette
- [`/assets/theme-sim/kit/themes/modern.json`](/assets/theme-sim/kit/themes/modern.json): a cooler, more contemporary palette
- [`/assets/theme-sim/kit/themes/vivid.json`](/assets/theme-sim/kit/themes/vivid.json): a brighter, higher-contrast palette

### Example: Dawn

This is `dawn.json`, byte for byte. Its only style option is a thin accent rule for `hr`.

```
{
  "schemaVersion": 1,
  "id": "dawn",
  "version": "1.0.0",
  "name": { "en": "Dawn" },
  "summary": { "en": "Warm Martian sunrise" },
  "fontDesign": "sans",
  "scenarios": ["agent-review"],
  "light": {
    "background": "#FFFDFB", "surface": "#F6F0EC", "text": "#26211F", "muted": "#6F6660",
    "border": "#EADFD8", "heading": "#26211F", "accent": "#C8471B", "link": "#B03C0C", "quote": "#D97A4A",
    "syntax": { "keyword": "#B03C0C", "string": "#2F6F5E", "comment": "#746B66", "number": "#9A5B00", "function": "#5B3E8C", "type": "#1F6FB2" },
    "diagram": { "node": "#FBE9E0", "nodeBorder": "#CA6C3C", "text": "#26211F", "line": "#8A6A5C", "secondary": "#E6F1EE", "tertiary": "#FFF6F1", "note": "#FFF1D6" }
  },
  "dark": {
    "background": "#1C1A1F", "surface": "#262229", "text": "#EBE4DF", "muted": "#A39992",
    "border": "#3A343A", "heading": "#F4EEEA", "accent": "#FF8A50", "link": "#FF9E6B", "quote": "#E08A5C",
    "syntax": { "keyword": "#FF9E6B", "string": "#7FD1B9", "comment": "#938A84", "number": "#F2C572", "function": "#C7A6F5", "type": "#6CB6FF" },
    "diagram": { "node": "#3A2A26", "nodeBorder": "#E08A5C", "text": "#EBE4DF", "line": "#B8A69C", "secondary": "#23332F", "tertiary": "#2B2427", "note": "#3D3322" }
  },
  "style": {
    "hr": { "style": { "type": "line", "color": "accent", "thickness": 1 } }
  }
}
```

## Fields

Every object below is read the same way. `required` means the key must be present, and a key that is not listed is an error.

Types: `string`, `integer`, `number`, `boolean`, `map` (language tag to text), `enum` (one of the listed values), `role` (a palette role) and `object` (the table it links to). A `[]` after a type means a list.

### `theme.json`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `schemaVersion` | `integer` | `required` | Always `1`. |
| `id` | `string` | `required` | 1 to 32 characters: lowercase letters and digits, in runs joined by single hyphens, such as `calm-green`. |
| `version` | `string` | `required` | `MAJOR.MINOR.PATCH`, such as `1.0.0`. |
| `name` | `map` | `required` | Language tag to text. `en` is required; other keys are language tags such as `zh-Hant`. Each text is at most 48 characters, with no links or line breaks. |
| `summary` | `map` | `required` | The same shape as `name`, at most 120 characters per text. |
| `fontDesign` | `enum` | `required` | `sans`, `serif`, `rounded` |
| `scenarios` | `enum[]` | `required` | `agent-review`, `technical-docs`, `formal-output`, `notes-sharing` — One or two, no repeats. They set how much contrast the theme must reach. |
| `author` | `object` | `optional` | [`author`](#t-author) |
| `license` | `string` | `optional` | An SPDX identifier, such as `Apache-2.0`. Submitted themes are released under Apache-2.0. |
| `light` | `object` | `required` | [`light, dark`](#t-palette) |
| `dark` | `object` | `required` | [`light, dark`](#t-palette) |
| `style` | `object` | `optional` | [`style`](#t-style) |

### `author`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `name` | `string` | `required` | At most 64 characters, with no links. |
| `github` | `string` | `optional` | A GitHub login. For a submission, set it to the submitter's own. |

### `light, dark`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `background` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `surface` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `text` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `muted` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `border` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `heading` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `accent` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `link` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `quote` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `syntax` | `object` | `optional` (required to publish, with `--require-complete`) | [`syntax`](#t-syntax-colors) |
| `diagram` | `object` | `optional` (required to publish, with `--require-complete`) | [`diagram`](#t-diagram-colors) |

### `syntax`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `keyword` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `string` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `comment` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `number` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `function` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `type` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |

### `diagram`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `node` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `nodeBorder` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `text` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `line` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `secondary` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `tertiary` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |
| `note` | `string` | `required` | `#` and six hex digits, such as `#1C1C1C`. |

### `style`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `bodySize` | `number` | `optional` | [range](#t-numbers) |
| `lineHeight` | `number` | `optional` | [range](#t-numbers) |
| `headingWeight` | `number` | `optional` | [range](#t-numbers) |
| `radius` | `number` | `optional` | [range](#t-numbers) |
| `maxWidth` | `number` | `optional` | [range](#t-numbers) |
| `h1` | `object` | `optional` | [`style.h1`](#t-style-h1) |
| `h2` | `object` | `optional` | [`style.h2`](#t-style-h2) |
| `blockquote` | `object` | `optional` | [`style.blockquote`](#t-style-blockquote) |
| `hr` | `object` | `optional` | [`style.hr`](#t-style-hr) |
| `table` | `object` | `optional` | [`style.table`](#t-style-table) |
| `listMarker` | `role` | `optional` | [a palette role](#roles) |
| `inlineCode` | `role` | `optional` | [a palette role](#roles) — Only `text` or a syntax role: `keyword`, `string`, `comment`, `number`, `function` or `type`. |
| `link` | `object` | `optional` | [`style.link`](#t-style-link) |
| `syntax` | `object` | `optional` | [`style.syntax`](#t-style-syntax) |

### `style.h1`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `size` | `number` | `optional` | [range](#t-numbers) |
| `letterSpacing` | `number` | `optional` | [range](#t-numbers) |
| `align` | `enum` | `optional` | `left`, `center` |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |

### `style.h2`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `letterSpacing` | `number` | `optional` | [range](#t-numbers) |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.blockquote`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.hr`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |

### `style.table`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `header` | `object` | `optional` | [`type`](#t-kinds) |
| `verticalRules` | `boolean` | `optional` | `true`, `false` |
| `rounded` | `boolean` | `optional` | `true`, `false` |

### `style.link`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `underline` | `boolean` | `optional` | `true`, `false` |

### `style.syntax`

| Field | Type | Presence | Values and notes |
|---|---|---|---|
| `boldKeywords` | `boolean` | `optional` | `true`, `false` |

### Options with a type

These style options are objects with a `type`. Each `type` takes the fields listed for it and no others.

| Option | type | Field | Presence | Type |
|---|---|---|---|---|
| `style.h1.decoration` | `rule` | — | — | — |
| `style.h1.decoration` | `none` | — | — | — |
| `style.h1.decoration` | `shortRule` | `color` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `from` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `to` | `required` | `role` |
| `style.h2.decoration` | `rule` | — | — | — |
| `style.h2.decoration` | `none` | — | — | — |
| `style.h2.decoration` | `dot` | `color` | `required` | `role` |
| `style.blockquote.style` | `bar` | `width` | `optional` | `number` [range](#t-numbers) |
| `style.blockquote.style` | `panel` | — | — | — |
| `style.hr.style` | `line` | `color` | `optional` | `role` |
| `style.hr.style` | `line` | `thickness` | `optional` | `number` [range](#t-numbers) |
| `style.hr.style` | `shortCentered` | `color` | `required` | `role` |
| `style.hr.style` | `gradient` | `colors` | `required` | `role[]` Two or three roles. |
| `style.table.header` | `surface` | — | — | — |
| `style.table.header` | `accentRule` | `color` | `required` | `role` |
| `style.table.header` | `filled` | `background` | `required` | `role` |
| `style.table.header` | `filled` | `text` | `required` | `role` |
| `style.table.header` | `filled` | `border` | `optional` | `role` |

### Palette roles

A palette role is one of these names:

`background`, `surface`, `text`, `muted`, `border`, `heading`, `accent`, `link`, `quote`, `keyword`, `string`, `comment`, `number`, `function`, `type`

### Numbers

A number is snapped to the nearest multiple of its step, and must then lie between min and max. Otherwise the rule is `number.range`.

| Field | Min | Max | Step |
|---|---|---|---|
| `style.bodySize` | `14` | `18` | `1` |
| `style.lineHeight` | `1.4` | `1.9` | `0.05` |
| `style.headingWeight` | `400` | `900` | `50` |
| `style.radius` | `0` | `16` | `1` |
| `style.maxWidth` | `600` | `1000` | `1` |
| `style.h1.size` | `1.8` | `2.4` | `0.1` |
| `style.h1.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.h2.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.blockquote.style.width` | `2` | `4` | `1` |
| `style.hr.style.thickness` | `1` | `4` | `1` |

## What else is checked

- **Contrast.** Each pair of colours the preview draws, such as `text` on `background`, must reach 4.5:1 for text and 3:1 for lines and other non-text. The scenarios you list raise some colours to 4.5:1. The message names the pair, its ratio and what it needs.
- **Strings.** A name, summary or author name that is empty, too long, or holds a link, a control character or an invisible or bidirectional format character is refused.
- **Rule ids.** Each problem carries one, such as `contrast.pair`, `color.hex`, `number.range`, `id.pattern`, `schema.unknownKey` or `palette.incomplete`. Fix the file by what the id and the `path` say.

## Hand it over as a link

The [Build a theme](/themes/new/) page opens a theme from a link, so the person can tune it by eye. The link is that page's address, then `#theme=`, then the file's bytes in base64url without padding. The file can be at most 16,384 bytes. This one line builds the link in zsh and in bash, on macOS and Linux:

```
printf 'https://marsdawn.southern-light.dev/themes/new/#theme=%s\n' "$(base64 < theme.json | tr -d '\n=' | tr '+/' '-_')"
```

The theme travels after a `#`, which a browser does not send to the site, and the site does not send it anywhere. The link does stay in your shell history and in the browser's history, and anyone you paste it to can read the theme.

## Submit it

The agent prepares the file and the link. The person submits. Both routes ask for the Developer Certificate of Origin and the Apache-2.0 release, and the person makes that certification: the agent does not tick the box or sign off for them.

- **Issue.** The person opens the link and presses **Submit** on the Build a theme page, or opens the [issue form](https://github.com/redtear1115/mars-dawn-website/issues/new?template=theme-submission.yml) and pastes the JSON into *Theme*. A workflow checks the theme and replies.
- **Pull request.** Change only `themes/<id>/theme.json`, set `author.github` to the pull request author's login, and sign off every commit with `git commit -s`. The rules are in [CONTRIBUTING.md](https://github.com/redtear1115/mars-dawn-website/blob/main/CONTRIBUTING.md).

A submitted theme's author name, name, summary and GitHub login become public permanently, so set `author.name` to a name the person is happy to publish.

## Published themes

To see what published themes look like, browse [the theme gallery](/themes/gallery/).

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Read and review the Markdown your agent wrote, natively on Mac: live split preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
- [Features](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.
- [PDF export](https://marsdawn.southern-light.dev/pdf/index.md): Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no editing on iPhone or iPad, no plugins, no accounts. Themes, but no custom CSS. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [How to open .md files on Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): How to open a .md file on a Mac: double-click, set a default app, preview in Finder. For .md files an AI agent wrote, read them rendered in MarsDawn.
- [Mermaid preview on Mac](https://marsdawn.southern-light.dev/mermaid-preview-mac/index.md): See Mermaid diagrams drawn next to your Markdown on a Mac: live preview, Quick Look and PDF export. A broken diagram shows its error and the line.
- [Quick Look for Markdown](https://marsdawn.southern-light.dev/quicklook/index.md): MarsDawn's Quick Look renders Markdown in Finder when you press Space, with Mermaid, KaTeX and highlighted code. It keeps working after the trial ends.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MarsDawn compared: VS Code preview, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/vs/index.md): For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on Support.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [Best Markdown viewer for Mac (2026)](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Themes](https://marsdawn.southern-light.dev/themes/index.md): Four built-in preview themes, each light and dark, plus a curated gallery you open from Settings in MarsDawn for Mac. Quick Look uses your theme.
- [Build a theme](https://marsdawn.southern-light.dev/themes/new/index.md): Pick colours and a handful of style options, see them applied to a sample document live, and submit your theme as a GitHub issue. No install, no git.
- [Theme gallery](https://marsdawn.southern-light.dev/themes/gallery/index.md): Browse preview themes for MarsDawn, each reviewed by the developer, filter them by scenario, and report a problem with one. Build your own in the browser.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Reading what your agent hands back](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [Agent transparency](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [Roadmap](https://marsdawn.southern-light.dev/roadmap/index.md): What's in progress and what's next for MarsDawn on Mac, iPhone and iPad, by version. No dates, and unscheduled ideas are marked.
- [Editor's reading notes](https://marsdawn.southern-light.dev/reading-notes/index.md): Six short notes on what the people building AI agents actually argue — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain and Andrew Ng — and what each one means for the person who has to read what such an agent hands back.
- [Reading notes: Anthropic](https://marsdawn.southern-light.dev/reading-notes/anthropic-building-effective-agents/index.md): Anthropic's December 2024 guide for people building agents separates workflows from agents and describes five workflow patterns, including one where a second LLM call reviews the first. What that means for what lands in your folder.
- [Reading notes: Chip Huyen](https://marsdawn.southern-light.dev/reading-notes/chip-huyen-agents/index.md): Chip Huyen's January 2025 essay on agents splits their actions into read-only and write actions. Why that split is a fast way to spot the line in a plan worth a closer look before you approve it.
- [Reading notes: Lilian Weng](https://marsdawn.southern-light.dev/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng's widely cited 2023 survey describes an LLM agent as a brain plus planning, memory and tool use. What each part tends to leave behind for you to read, and the limitation she names in plans that don't adjust to surprises.
- [Reading notes: Harrison Chase](https://marsdawn.southern-light.dev/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase's 2024 definition of an agent and his spectrum of agentic behavior, and his case for observability as a system moves along it — read from the side of whoever reads the file it hands back.
- [Reading notes: LangChain (Jess Ou)](https://marsdawn.southern-light.dev/reading-notes/langchain-what-is-an-agent/index.md): LangChain's 2026 “What is an AI agent?” by Jess Ou echoes Harrison Chase's 2024 definition and describes a pipeline for evaluating agents automatically. Where that pipeline still hands a step to a person, and where it doesn't.
- [Reading notes: Andrew Ng](https://marsdawn.southern-light.dev/reading-notes/andrew-ng-design-patterns/index.md): Across five letters in The Batch, Andrew Ng ranks reflection, tool use, planning and multi-agent collaboration by how reliable and predictable he finds each one — and what that ranking suggests about how closely to check each one's output.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI 代理的 MarsDawn 主题制作参考：theme.json 每个字段的类型与范围、检查并渲染的 CLI 流程、交给人的链接，以及怎么投稿。
- [日本語](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [Deutsch](https://marsdawn.southern-light.dev/de/themes/agents/index.md): MarsDawn-Themen-Referenz für KI-Agenten: jedes Feld der theme.json mit Typ und Bereich, Prüfen und Rendern per CLI, ein Übergabe-Link und die Einreichung.
- [Français](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
- [Español](https://marsdawn.southern-light.dev/es/themes/agents/index.md): Referencia de temas de MarsDawn para agentes de IA: cada campo de theme.json con tipo y rango, comprobación y renderizado por CLI, enlace de entrega y envío.
- [한국어](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
