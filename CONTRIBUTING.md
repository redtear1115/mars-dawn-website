# Contributing

This repo is the site at marsdawn.southern-light.dev: home page, privacy policy and support pages,
in English and Traditional Chinese. It's the right place for copy changes, page structure, the
build script and deploy workflow.

## What goes elsewhere

- Bugs in the `marsdawn` CLI, the Markdown renderer or PDF export —
  [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit).
- Questions or feedback about the MarsDawn Mac app itself —
  [discussions on this repo](https://github.com/redtear1115/mars-dawn-website/discussions).

## Build and test locally

Edit the copy in `scripts/build_pages.py`, then regenerate and commit the output:

```sh
python3 scripts/build_pages.py
```

CI re-runs the same command and fails if the regenerated pages don't match what you committed, so
always regenerate before opening a PR.

Preview locally:

```sh
python3 -m http.server 8765 --directory public   # http://localhost:8765/
```

If `public/themes/v1/index.json` exists, CI also checks it's valid JSON.

UI labels quoted on the pages must match the app's strings in each language — check them by hand
when either side changes; nothing automated catches a mismatch there.

The URLs `/privacy/`, `/support/`, `/zh-hant/privacy/` and `/zh-hant/support/` are public contracts
that must keep working at the same paths. Don't move or remove them without a redirect plan.

## Issues and pull requests

Pull requests target `main`. A small, focused PR is easier to review than one that bundles several
changes — say what changed and why in the description.

CI must be green: it regenerates the pages and diffs them against your commit, and checks the theme
index JSON when present. Deploys happen separately, by fast-forwarding `release` to `main`, and
aren't something a contributing PR needs to do.

## Security

Please report vulnerabilities as described in [SECURITY.md](SECURITY.md), not in a public issue.

## License

By contributing, you agree that your contribution is licensed under this repository's applicable
license, on an inbound = outbound basis:

- Code (`scripts/`, workflows, config) is Apache-2.0 — see [LICENSE](LICENSE).
- Site copy and images under `public/` are covered by [LICENSE-CONTENT](LICENSE-CONTENT).
