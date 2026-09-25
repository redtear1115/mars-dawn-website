---
name: marsdawn
description: Export Markdown to PDF with the marsdawn command-line tool on macOS, and read its JSON result. Use when asked to turn a Markdown file into a PDF, or to render Markdown with tables, math, Mermaid diagrams or highlighted code into a PDF.
---

# marsdawn

`marsdawn export` renders a Markdown file to PDF on macOS 15 or later. It needs nothing else
installed, not even the MarsDawn app.

## Install and check

```sh
command -v marsdawn || brew install redtear1115/tap/marsdawn
marsdawn --version
```

Use the version it prints. Don't assume one. On Apple silicon Homebrew pours a prebuilt bottle;
on an Intel Mac it builds from source and needs Xcode 26 or later. If the install stops with
"A full installation of Xcode.app 26.0 is required", say so rather than retrying.

## Export

```sh
marsdawn export input.md --json
```

Options: `-o out.pdf` (default: beside the input), `--theme dawn|classic|modern|vivid`,
`--paper a4|letter`, `--force` to replace an existing PDF, and
`--allow-remote-images` to load web images, which are left out by default.

On success it exits 0 and prints one JSON line:

- `ok`: always true
- `output`: Absolute path of the PDF that was written.
- `pages`: Number of pages in the PDF.
- `theme`: Theme used for the export.
- `paper`: Paper size used for the export.
- `diagramErrors`: One message per Mermaid diagram that failed to render. The PDF is still written.
- `diagramErrorDetails`: One entry per diagramErrors entry, in the same order, with the document line each error is on when known.

If `diagramErrors` isn't empty, the PDF was still written: tell the user which diagrams failed.

## Exit codes

On failure with `--json` it prints `{"ok": false, "error": <kind>, "message": ...}`.

| Code | `error` | Meaning |
|---|---|---|
| 0 | — | Success. With --json, stdout is one JSON line. |
| 2 | `input_not_found` | The input file isn't there. |
| 3 | `app_not_installed` | MarsDawn isn't installed. Only `open` returns this. |
| 4 | `output_exists` | The PDF already exists. Pass --force to replace it, or -o to write elsewhere. |
| 5 | `export_failed` | Rendering failed. |
| 64 | — | Usage error: a bad option or value. Printed as text on stderr, never as JSON. |

## open

`marsdawn open file.md` opens a file in the MarsDawn app for review. It needs the app; without
it, it exits 3. Never use it to make a PDF: that's `export`.

## Full contract

Every field, schema and code: https://marsdawn.southern-light.dev/cli/agents/
