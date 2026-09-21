#!/usr/bin/env python3
"""Renders the social card, public/assets/og-en.png (1200x630), from the site's own hero.

The card is the homepage's dawn scene (the same SVG as build_pages.py) with the wordmark,
the English headline and lede (read from the home page's copy, so they can't drift apart)
and the address, set in site.css plus og.css. This writes tools/og/og-en.html, then opens
it in Google Chrome (a real, headed window with a throwaway profile), holds the scene at its
reduced-motion resting frame and saves the 1200x630 capture:

    python3 tools/og/build_og.py            # writes og-en.html and public/assets/og-en.png
    python3 tools/og/build_og.py --html     # only the HTML

Needs Google Chrome in /Applications. Run it again whenever the hero's copy or scene changes.
"""
import argparse
import base64
import json
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import build_pages  # noqa: E402
from cdp import CDP  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 9339
OUT = ROOT / "public" / "assets" / "og-en.png"


def card_html() -> str:
    headline, lede = build_pages.hero_copy("en")
    lines = " ".join(f"<span>{line}</span>" for line in headline)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>MarsDawn social card</title>
<link rel="stylesheet" href="../../public/assets/site.css">
<link rel="stylesheet" href="og.css">
</head>
<body>
<main class="og">
<section class="hero-scene">
{build_pages.DAWN_HERO_SVG}
<div class="og-copy hero">
  <p class="og-brand"><img src="../../public/assets/icon-192.png" alt="" width="64" height="64"><span>MarsDawn</span></p>
  <h1>{lines}</h1>
  <p class="og-lede">{lede}</p>
</div>
<p class="og-url">{build_pages.BASE_URL.split("://", 1)[1]}</p>
</section>
</main>
</body>
</html>
"""


def render(html_path: Path, out: Path) -> None:
    profile = tempfile.mkdtemp(prefix="marsdawn-og-")
    chrome = subprocess.Popen([CHROME, f"--user-data-dir={profile}", f"--remote-debugging-port={PORT}",
                               "--no-first-run", "--no-default-browser-check", "about:blank"],
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        page = None
        for _ in range(150):
            try:
                tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json"))
                page = next(t for t in tabs if t["type"] == "page")
                break
            except Exception:
                time.sleep(0.2)
        if page is None:
            sys.exit("build_og: Chrome didn't start")
        c = CDP(page["webSocketDebuggerUrl"])
        c.call("Page.enable")
        c.call("Emulation.setEmulatedMedia", features=[{"name": "prefers-reduced-motion", "value": "reduce"},
                                                       {"name": "prefers-color-scheme", "value": "light"}])
        c.call("Emulation.setDeviceMetricsOverride", width=1200, height=630, deviceScaleFactor=1, mobile=False)
        c.call("Page.navigate", url=html_path.as_uri())
        time.sleep(2)
        shot = c.call("Page.captureScreenshot", format="png", clip={"x": 0, "y": 0, "width": 1200, "height": 630, "scale": 1})
        out.write_bytes(base64.b64decode(shot["data"]))
    finally:
        chrome.terminate()
        try:
            chrome.wait(10)
        except subprocess.TimeoutExpired:
            chrome.kill()
        shutil.rmtree(profile, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--html", action="store_true", help="write the HTML only, don't render")
    args = parser.parse_args()
    html_path = HERE / "og-en.html"
    html_path.write_text(card_html(), encoding="utf-8")
    print(html_path.relative_to(ROOT))
    if not args.html:
        render(html_path, OUT)
        print(OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
