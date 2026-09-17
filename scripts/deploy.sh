#!/bin/sh
# Manual deploy of public/ to https://marsdawn.southern-light.dev (Cloudflare Workers static assets).
# The normal path is a push to the `release` branch, which deploys through GitHub Actions.
# Needs CLOUDFLARE_ACCOUNT_ID in the environment and a `wrangler login` session.
set -eu
cd "$(dirname "$0")/.."
: "${CLOUDFLARE_ACCOUNT_ID:?Set CLOUDFLARE_ACCOUNT_ID first}"
python3 scripts/build_pages.py >/dev/null
test -z "$(git status --porcelain public)" || { echo "public/ differs from the commit; commit the regenerated pages first" >&2; exit 1; }
wrangler deploy
