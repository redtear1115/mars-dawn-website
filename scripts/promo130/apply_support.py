#!/usr/bin/env python3
"""Puts #246's invitation line into content/legal/support.<locale>.md (after the address paragraph, as
Grok's reply says) and renders those pages the way scripts/render_legal.py does, recording the new
hashes in content/legal/manifest.json. The text is scripts/promo130/data.py's ("support" entries).

Needs macOS and a built tools/hero-render (the renderer scripts/render_legal.py builds); pass the
binary's path, so nothing is built or fetched here:

    python3 -B scripts/promo130/apply_support.py [path/to/hero-render]

Idempotent: a page that already has the line is left alone. Only the support pages' two hashes in the
manifest change; the stylesheets and the privacy pages are not touched.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.dont_write_bytecode = True
import render_legal  # noqa: E402
from promo130 import data  # noqa: E402

ADDRESS = "[support@southern-light.dev](mailto:support@southern-light.dev?subject=MarsDawn%20support)"


def main() -> None:
    binary = Path(sys.argv[1]) if len(sys.argv) > 1 else render_legal.RENDERER / ".build" / "release" / "hero-render"
    assert binary.is_file(), f"{binary} not found: build tools/hero-render first"
    manifest = json.loads(render_legal.MANIFEST.read_text(encoding="utf-8"))
    for locale in render_legal.LOCALES:
        key = locale if locale != "zh-hant" else "zh-hant"
        paragraph = data.DATA["support"][locale]["p_md"]
        source = render_legal.CONTENT / f"support.{locale}.md"
        text = source.read_text(encoding="utf-8")
        if paragraph not in text:
            lines = text.split("\n")
            at = [i for i, line in enumerate(lines) if line == ADDRESS]
            assert len(at) == 1, f"{source.name}: the address paragraph isn't there exactly once"
            lines[at[0] + 1:at[0] + 1] = ["", paragraph]
            text = "\n".join(lines)
            source.write_text(text, encoding="utf-8")
        html = render_legal.clean_fragment(render_legal.render_markdown(binary, text), text)
        out = render_legal.CONTENT / f"support.{locale}.rendered.html"
        out.write_text(render_legal.GENERATED_NOTE.format(source=source.name) + html, encoding="utf-8")
        manifest["pages"][source.name] = {"source_sha256": render_legal.sha256(text), "rendered": out.name,
                                          "rendered_sha256": render_legal.sha256(out.read_text(encoding="utf-8"))}
        print(source.name, "->", out.name)
    render_legal.MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
