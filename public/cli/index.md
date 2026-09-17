# Command Line

The free `marsdawn` command-line tool: open Markdown files in MarsDawn, or export them to PDF from a shell or an LLM agent.

**marsdawn is free and distributed separately from the Mac App Store.** Homebrew isn't published yet, so build it from source with Swift Package Manager. Both commands need the MarsDawn app installed.

## Install

Clone [the source](https://github.com/redtear1115/mars-dawn-kit) and run it with Swift Package Manager:

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift run marsdawn open notes.md
```

## Commands

### marsdawn open

Opens one or more Markdown files in MarsDawn for review. Needs MarsDawn installed.

```
marsdawn open notes.md
```

- `--json`: print a JSON result instead of text.

### marsdawn export

Renders a Markdown file to a paginated PDF, with the same exporter MarsDawn's own PDF export uses. Also needs MarsDawn installed. Relative images resolve against the input file's folder.

```
marsdawn export notes.md -o notes.pdf --theme classic --paper a4
```

- `-o, --output <path>`: where to write the PDF. Defaults to the input path with a `.pdf` extension.
- `--theme <dawn|classic|modern|vivid>`: the preview theme's light palette. Defaults to `$MARSDAWN_THEME`, then `dawn`.
- `--paper <a4|letter>`: paper size. Defaults to `a4`.
- `--allow-remote-images`: load images from the web while rendering. Off by default.
- `--force`: replace the output file if it already exists.
- `--json`: print a JSON result instead of text.

## The $MARSDAWN_THEME variable

When `--theme` isn't passed, `export` reads the `$MARSDAWN_THEME` environment variable. Its value must be one of `dawn`, `classic`, `modern` or `vivid`; anything else falls back to `dawn`. The CLI doesn't read the app's own theme setting, because reading another app's container can trigger a macOS privacy prompt.

## Overwriting files

`export` refuses to replace an existing output file unless you pass `--force`.

## Exit codes

- `0`: success.
- `2`: input not found.
- `3`: MarsDawn is not installed.
- `4`: output exists (pass `--force`).
- `5`: export failed.
- `64`: usage error.

## --json output

On success, `marsdawn open --json` prints `ok`, `opened` (the file paths) and `app` (the app path). `marsdawn export --json` prints `ok`, `output`, `pages`, `theme`, `paper` and `diagramErrors`. On failure, both print `ok`, `error` and `message`.

## MarsDawn must be installed

Both `open` and `export` need the MarsDawn app installed from the Mac App Store; `export` renders through the same code the app uses, but still checks that the app is present first.
