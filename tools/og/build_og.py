#!/usr/bin/env python3
"""Writes tools/og/og-en.html: the social card, drawn by the site's own hero.

The card is the homepage's dawn scene (the same SVG, from build_pages.py) with the
wordmark and the headline, set in site.css. Render it to public/assets/og-en.png at
1200x630 in a real browser with reduced motion, so it is the scene's resting frame:

    python3 tools/og/build_og.py
    (serve the repository root, open /tools/og/og-en.html at 1200x630, save a PNG)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
import build_pages  # noqa: E402

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>MarsDawn social card</title>
<link rel="stylesheet" href="/public/assets/site.css">
<link rel="stylesheet" href="/tools/og/og.css">
</head>
<body>
<main class="og">
<section class="hero-scene">
{build_pages.DAWN_HERO_SVG}
<div class="og-copy hero">
  <p class="og-brand"><img src="/public/assets/icon-192.png" alt="" width="64" height="64"><span>MarsDawn</span></p>
  <h1><span>Claim the map.</span> <span>Read the dawn.</span></h1>
  <p class="og-lede">Markdown for humans who steer agentic work.</p>
</div>
<p class="og-url">marsdawn.southern-light.dev</p>
</section>
</main>
</body>
</html>
"""

if __name__ == "__main__":
    (ROOT / "tools" / "og" / "og-en.html").write_text(HTML, encoding="utf-8")
    print("wrote tools/og/og-en.html")
