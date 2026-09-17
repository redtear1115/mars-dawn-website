# marsdawn.southern-light.dev

The website of [MarsDawn](https://marsdawn.southern-light.dev), a Markdown editor for the Mac: home page, privacy policy and support pages, in English and Traditional Chinese.

## Layout

| Path | What it is |
|---|---|
| `public/` | The site root, served as static files |
| `public/_headers` | Cache rules (theme index short, versioned theme files long) |
| `scripts/build_pages.py` | Generates the privacy and support pages into `public/` |
| `scripts/deploy.sh` | Manual deploy, for emergencies |
| `wrangler.jsonc` | Cloudflare Workers static-assets config |

These URLs are public contracts and must keep working at the same paths:
`/privacy/`, `/support/`, `/zh-hant/privacy/`, `/zh-hant/support/` (linked from the App Store) and everything under `/themes/v1/` (read by the app).

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
