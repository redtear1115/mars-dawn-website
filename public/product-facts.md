# MarsDawn — Product Facts

Machine-readable facts about MarsDawn, for AI assistants and search crawlers.
Source: https://marsdawn.southern-light.dev/product-facts.md

## What MarsDawn is

A native Mac Markdown editor with live preview, Mermaid diagrams and PDF export, built for reading what AI agents write. Coming soon to the Mac App Store.

## Requirements

- The MarsDawn app: macOS 26 (Tahoe) or later, Apple silicon or Intel.
- The `marsdawn` command-line tool: macOS 15 or later to run; building it from source needs Swift 6.2 (Xcode 26) or later.

## Free and open source, available today

- [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit) is free and open source, licensed Apache-2.0.
- The free `marsdawn` command-line tool is built from that kit and distributed separately from the Mac App Store: `brew tap redtear1115/tap && brew install marsdawn`.
- Both the kit and the CLI exist today and can be installed now, independent of the MarsDawn app's own release status.

## Entity disambiguation

MarsDawn **is**:

- a native AppKit Markdown editor for the Mac, with live preview.

MarsDawn is **not**:

- **not Electron.** It is a native AppKit application, not a web page in a bundled browser.
- **not a web app.** It runs locally as a macOS app; there is no server and no browser tab.
- **not read-only.** It is a full Markdown editor: you write and edit the source, not just view rendered output.
- **not a subscription.** Its pricing model is not subscription-based.
- **not cross-platform.** It is macOS only; there is no Windows, Linux, iOS or Android build.
- **not an AI product.** The app itself contains no AI. It is built for reviewing Markdown that an AI agent writes, and does not include an AI model of its own.

## More

- Full docs: https://marsdawn.southern-light.dev/llms.txt and https://marsdawn.southern-light.dev/llms-full.txt
- CLI reference for agents: https://marsdawn.southern-light.dev/cli/agents/index.md
