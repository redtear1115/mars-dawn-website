# marsdawn.southern-light.dev

The website of [MarsDawn](https://marsdawn.southern-light.dev), a Markdown editor for the Mac: home page, privacy policy and support pages, in English and Traditional Chinese, with the privacy policy and support pages also in Simplified Chinese and Japanese.

## Layout

| Path | What it is |
|---|---|
| `public/` | The site root, served as static files |
| `public/_headers` | Security headers for every page (strict CSP with no scripts, nosniff, no referrer) and cache rules (theme index short, versioned theme files long). Anything that adds a script, inline style, web font or third-party resource must update the CSP |
| `scripts/build_pages.py` | Generates every page into `public/`, with the en and zh-Hant copy |
| `scripts/copy_zh_hans.py`, `scripts/copy_ja.py` | The zh-Hans and ja copy, merged in by `build_pages.py`. For now they have the privacy policy and support pages only; a locale may have only some pages, and nothing links to one it doesn't have |
| `scripts/check_hreflang.py` | Checks that every page's hreflang set is complete (every locale that has the page) and reciprocal, in the HTML and the sitemap (runs in CI) |
| `scripts/check_links.py` | Checks that every same-site link in the built site points at a file that exists (runs in CI) |
| `scripts/deploy.sh` | Manual deploy, for emergencies |
| `wrangler.jsonc` | Cloudflare Workers static-assets config |

These URLs are public contracts and must keep working at the same paths:
`/privacy/`, `/support/`, `/zh-hant/privacy/`, `/zh-hant/support/`, `/zh-hans/privacy/`, `/zh-hans/support/`, `/ja/privacy/`, `/ja/support/` (linked from the App Store).

`/themes/v1/` is **reserved** for the theme gallery, whose design is `docs/theme-ecosystem-design.md` in the app repository. Nothing is served there yet, and neither the app nor the `marsdawn` CLI reads it. Once the gallery ships and the app reads it, it becomes a contract too. Until then, the cache rules in `public/_headers` and the CI check below, which runs only when the index exists, are preparation.

## Editing

Edit the copy in `scripts/build_pages.py`, then regenerate and commit the output:

```sh
python3 scripts/build_pages.py
```

UI labels quoted on the pages must match the app's strings in each language. Check them by hand when either side changes.

Preview locally:

```sh
python3 -m http.server 8765 --directory public   # http://localhost:8765/
```

After a deploy, open every page in a private window. They must load without a login or redirect.

## Branches and deploys

- `main` holds the latest work. Pull requests target `main`.
- `release` is what the site serves. A push to `release` deploys through GitHub Actions (`production` environment). To publish, fast-forward `release` to `main`:

  ```sh
  git push origin main:release
  ```

- Every push and pull request runs the check: the regenerated pages must match the commit, and `public/themes/v1/index.json`, when present, must be valid JSON.

The deploy needs two settings on the `production` environment:

| Kind | Name |
|---|---|
| Secret | `CLOUDFLARE_API_TOKEN` (Workers Scripts: Edit only) |
| Variable | `CLOUDFLARE_ACCOUNT_ID` |

## License

- Code (`scripts/`, workflows, config): Apache-2.0, see [LICENSE](LICENSE).
- Site copy and images (`public/`): CC BY 4.0, see [LICENSE-CONTENT](LICENSE-CONTENT).

The MarsDawn name and app icon are not covered by either license.

Security issues: see [SECURITY.md](SECURITY.md).
