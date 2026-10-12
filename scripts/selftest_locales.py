"""The self-test behind `check_locales.py --self-test` (website #162): proves the enabled path of a
planned locale, and that each rule of the checks catches its own break.

It works in a scratch copy of the site (a temporary directory; the checkout is never touched) and
never commits or leaves English under a de/fr/es/ko URL. The throwaway locale is "de", built from
the Japanese copy relabelled as German: different from en (so the English-copy rule has nothing to
flag) and real enough to go through every table, page and link. It is a fixture, not a translation.

Steps, each printed:
  1. the scratch site (de, fr, es and ko put back to COMPLETE = False, nothing of theirs served: see
     unship_planned) builds without any of them, and a second build changes nothing;
  2. with the fixture's COMPLETE = True it builds again, every en page exists under /de/, a second
     build changes nothing, and check_hreflang, check_links, check_invariants, check_locales,
     check_offers, check_hero and check_legal_render pass on it;
  3. the build refuses a COMPLETE = True locale with a string empty, a key missing, a legal page,
     the hero snapshot or an image absent, and says which;
  4. a planted break of each rule is caught, by that rule's own message and no other rule.
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOCALE = "de"


def sh(scratch: Path, *args, check=False) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], cwd=scratch, capture_output=True, text=True, check=check)


def tree_hash(path: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(path.rglob("*")):
        if p.is_file():
            h.update(str(p.relative_to(path)).encode())
            h.update(p.read_bytes())
    return h.hexdigest()


def make_scratch(tmp: Path) -> Path:
    scratch = tmp / "site"
    ignore = shutil.ignore_patterns("__pycache__", ".build", ".git", ".claude")
    for name in ("scripts", "content", "public", "vendor", "themes"):
        shutil.copytree(REPO / name, scratch / name, ignore=ignore)
    (scratch / "tools" / "hero-render").mkdir(parents=True)
    shutil.copy(REPO / "tools" / "hero-render" / "Package.swift", scratch / "tools" / "hero-render" / "Package.swift")
    unship_planned(scratch)
    return scratch


def unship_planned(scratch: Path) -> None:
    """Puts the scratch copy back in the state this test is written for: de, fr, es and ko known but
    not complete, with nothing of theirs served. Once a real locale ships (COMPLETE = True, its pages,
    legal sources, images and hero snapshot in the checkout) the test would otherwise find five
    locales where it plants one, and its "nothing changes" step would have nothing to compare."""
    for locale in ("de", "fr", "es", "ko"):
        copy = scratch / "scripts" / f"copy_{locale}.py"
        copy.write_text(copy.read_text(encoding="utf-8").replace("COMPLETE = True", "COMPLETE = False"), encoding="utf-8")
        shutil.rmtree(scratch / "public" / locale, ignore_errors=True)
        for path in list((scratch / "public" / "assets").rglob(f"*-{locale}.png")):
            path.unlink()
        for path in list((scratch / "content" / "legal").glob(f"*.{locale}.*")):
            path.unlink()
    legal = scratch / "content" / "legal" / "manifest.json"
    manifest = json.loads(legal.read_text(encoding="utf-8"))
    manifest["pages"] = {name: v for name, v in manifest["pages"].items() if not re.search(r"\.(de|fr|es|ko)\.md$", name)}
    legal.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    hero = scratch / "scripts" / "hero_sources.json"
    src = json.loads(hero.read_text(encoding="utf-8"))
    for table in ("labels", "sample"):
        for locale in ("de", "fr", "es", "ko"):
            src[table].pop(locale, None)
    for theme in src["themes"]:
        for field in ("names", "summaries"):
            for locale in ("de", "fr", "es", "ko"):
                theme[field].pop(locale, None)
    hero.write_text(json.dumps(src, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


FIXTURE_WRITER = r'''
import json, sys
sys.path.insert(0, "scripts")
sys.dont_write_bytecode = True
import build_pages as b, copy_ja
t = copy_ja.build(b._make_k("ja"))
t["ui"] = {key: v for key, v in t["ui"].items() if key not in b.templates_pages.UI_LABELS["en"]}
t["pages"].setdefault("themes/gallery", b.GALLERY_PAGES[("ja", "themes/gallery")])
t["tables"] = b.locale_tables("ja")
t["tables"]["hero_window_markdown"] = {"template": "Fixture {looks} / {themes} / {layouts}", "sep": ", "}
for slug in ("privacy", "support"):
    t["pages"][slug]["body"] = "@@LEGAL:" + slug
src = repr(t).replace("'@@LEGAL:privacy'", "k.render_legal_body('privacy', 'de')").replace("'@@LEGAL:support'", "k.render_legal_body('support', 'de')")
open("scripts/copy_de.py", "w", encoding="utf-8").write(
    '"""Self-test fixture: ja copy under a de label. Never committed."""\nCOMPLETE = True\n\n\ndef build(k):\n    return ' + src + "\n")
'''


def make_fixture(scratch: Path) -> None:
    sh(scratch, "-c", FIXTURE_WRITER, check=True)
    legal = scratch / "content" / "legal"
    manifest = json.loads((legal / "manifest.json").read_text(encoding="utf-8"))
    for slug in ("privacy", "support"):
        md = (legal / f"{slug}.ja.md").read_text(encoding="utf-8")
        (legal / f"{slug}.{LOCALE}.md").write_text(md, encoding="utf-8")
        rendered = (legal / f"{slug}.ja.rendered.html").read_text(encoding="utf-8").replace(f"{slug}.ja.md", f"{slug}.{LOCALE}.md")
        (legal / f"{slug}.{LOCALE}.rendered.html").write_text(rendered, encoding="utf-8")
        manifest["pages"][f"{slug}.{LOCALE}.md"] = {
            "source_sha256": hashlib.sha256(md.encode()).hexdigest(), "rendered": f"{slug}.{LOCALE}.rendered.html",
            "rendered_sha256": hashlib.sha256(rendered.encode()).hexdigest()}
    (legal / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    hero = scratch / "scripts" / "hero_sources.json"
    src = json.loads(hero.read_text(encoding="utf-8"))
    src["labels"][LOCALE], src["sample"][LOCALE] = src["labels"]["ja"], src["sample"]["ja"]
    for theme in src["themes"]:
        theme["names"][LOCALE], theme["summaries"][LOCALE] = theme["names"]["ja"], theme["summaries"]["ja"]
    hero.write_text(json.dumps(src, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    assets = scratch / "public" / "assets"
    for case in ("spec", "flowchart", "meeting-notes"):
        shutil.copy(assets / "templates" / f"{case}-ja.png", assets / "templates" / f"{case}-{LOCALE}.png")
    shutil.copy(assets / "cli" / "plan-ja.png", assets / "cli" / f"plan-{LOCALE}.png")


class Run:
    def __init__(self):
        self.failures = 0

    def expect(self, ok: bool, label: str, detail: str = "") -> None:
        print(f"  {'ok     ' if ok else 'FAILED '} {label}" + (f"\n{detail}" if detail and not ok else ""))
        self.failures += not ok


def edit(path: Path, fn):
    """Applies fn to the file's text and returns a function that puts the original back."""
    original = path.read_bytes()
    path.write_text(fn(path.read_text(encoding="utf-8")), encoding="utf-8")
    return lambda: path.write_bytes(original)


def remove(path: Path):
    original = path.read_bytes()
    path.unlink()
    return lambda: path.write_bytes(original)


def run() -> int:
    r = Run()
    with tempfile.TemporaryDirectory(prefix="locales-selftest-") as tmpdir:
        scratch = make_scratch(Path(tmpdir))
        pub = scratch / "public"

        print("1. A planned locale that isn't complete changes nothing")
        out = sh(scratch, "scripts/build_pages.py")
        committed = tree_hash(pub)
        out2 = sh(scratch, "scripts/build_pages.py")
        r.expect(out.returncode == 0 and out2.returncode == 0 and tree_hash(pub) == committed
                 and not any((pub / l).exists() for l in ("de", "fr", "es", "ko")),
                 "the build, with de, fr, es and ko not complete, serves none of them and changes nothing on a second run", out.stderr[-600:])
        out = sh(scratch, "scripts/check_locales.py")
        r.expect(out.returncode == 0 and "0 problems" in out.stdout, "check_locales is clean", out.stdout + out.stderr)
        out = sh(REPO, "scripts/new_locale.py", "--check")  # the checkout's own modules: the scratch copy has their legal pages removed
        r.expect(out.returncode == 0, "the four modules have en's structure", out.stdout + out.stderr)

        print("2. With a complete locale (throwaway fixture under /de/)")
        make_fixture(scratch)
        out = sh(scratch, "scripts/build_pages.py")
        r.expect(out.returncode == 0, "the build succeeds", out.stdout[-300:] + out.stderr[-1500:])
        if out.returncode != 0:
            return 1
        built = tree_hash(pub)
        en_pages = sorted(p.parent.relative_to(pub) for p in pub.rglob("index.html")
                          if p.relative_to(pub).parts[0] not in ("zh-hant", "zh-hans", "ja", "de", "assets"))
        r.expect(all((pub / "de" / p / "index.html").is_file() for p in en_pages) and len(en_pages) == 39,
                 f"all {len(en_pages)} en pages exist under /de/ with the same slugs")
        sh(scratch, "scripts/build_pages.py")
        r.expect(tree_hash(pub) == built, "a second build changes nothing")
        home = (pub / "de" / "index.html").read_text(encoding="utf-8")
        r.expect('<html lang="de"' in home and all(f'hreflang="{l}"' in home for l in ("en", "zh-Hant", "zh-Hans", "ja", "de", "x-default")),
                 "<html lang=de>, and hreflang names all five locales and x-default")
        sitemap = (pub / "sitemap.xml").read_text(encoding="utf-8")
        r.expect(sitemap.count("<loc>https://marsdawn.southern-light.dev/de/") == 39, "the sitemap lists 39 /de/ URLs")
        urls = sh(scratch, "scripts/indexnow_urls.py", "--sitemap").stdout
        r.expect(urls.count("/de/") == 39, "indexnow_urls.py --sitemap lists them")
        r.expect("/de/" in (pub / "llms.txt").read_text(encoding="utf-8"), "llms.txt links /de/")
        checks = [("check_hreflang.py",), ("check_links.py",), ("check_invariants.py",), ("check_locales.py",), ("check_offers.py",),
                  ("check_hero.py",), ("check_legal_render.py", "--self-test"), ("check_legal_render.py",)]
        for check in checks:
            out = sh(scratch, "scripts/" + check[0], *check[1:])
            r.expect(out.returncode == 0, "passes on it: " + " ".join(check), out.stdout[-800:] + out.stderr[-800:])
        copy_path = scratch / "scripts" / "copy_de.py"

        print("3. The build refuses an incomplete locale that says COMPLETE = True")
        build_plants = [
            ("an unexpected key", lambda: edit(copy_path, lambda s: s.replace("'cta_cli': '", "'cta_cli': '', 'x_': '", 1)), "unexpected key 'x_'"),
            ("a key missing", lambda: edit(copy_path, lambda s: s.replace("'cta_cli': ", "'cta_cli_gone': ", 1)), "missing key 'cta_cli'"),
            ("a legal page missing", lambda: remove(scratch / "content" / "legal" / "support.de.rendered.html"), "content/legal/support.de.rendered.html is missing"),
            ("the hero snapshot missing the locale", lambda: edit(scratch / "scripts" / "hero_sources.json", lambda s: s.replace('"de"', '"xx"')), "hero_sources.json has no labels['de']"),
            ("a template image missing", lambda: remove(pub / "assets" / "templates" / "spec-de.png"), "public/assets/templates/spec-de.png is missing"),
        ]
        for label, plant, message in build_plants:
            undo = plant()
            out = sh(scratch, "scripts/build_pages.py")
            undo()
            r.expect(out.returncode != 0 and "COMPLETE = True, but de is not complete" in out.stderr and message in out.stderr,
                     f"refused ({label}): {message}", out.stderr[-700:])
        undo = edit(copy_path, lambda s: re.sub(r"'(title|description)': '[^']*'", lambda m: f"'{m.group(1)}': ''", s, count=1))
        out = sh(scratch, "scripts/build_pages.py")
        undo()
        r.expect(out.returncode != 0 and "empty, en has text" in out.stderr, "refused (an empty string): empty, en has text", out.stderr[-700:])
        out = sh(scratch, "scripts/build_pages.py")
        r.expect(out.returncode == 0 and tree_hash(pub) == built, "and with every plant undone it builds the same again")

        print("4. Each rule catches its own break, and only its own")
        de = pub / "de"
        en_native = (pub / "native" / "index.html").read_text(encoding="utf-8")
        loc_plants = [
            ("parity", "a missing page", lambda: remove(de / "pdf" / "index.html"), "de is missing /pdf/"),
            ("parity", "a missing Markdown twin", lambda: remove(de / "pdf" / "index.md"), "de is missing /pdf/index.md"),
            ("parity", "a missing 404", lambda: remove(de / "404.html"), "de is missing 404.html"),
            ("parity", "an extra page", lambda: _write(de / "extra" / "index.html", "x"), "de has /extra/"),
            ("legal", "a missing source", lambda: remove(scratch / "content" / "legal" / "privacy.de.md"), "content/legal/privacy.de.md is missing"),
            ("legal", "a missing rendering", lambda: remove(scratch / "content" / "legal" / "support.de.rendered.html"), "support.de.rendered.html is missing"),
            ("legal", "a missing manifest entry", lambda: edit(scratch / "content" / "legal" / "manifest.json", lambda s: s.replace('"support.de.md"', '"support.xx.md"')), "manifest.json has no support.de.md"),
            ("copy", "an English page under /de/", lambda: edit(de / "native" / "index.html", lambda s: re.sub(r"<main\b.*?</main>", lambda _m: re.search(r"<main\b.*?</main>", en_native, re.S).group(0), s, flags=re.S)), "/de/native/ is English"),
            ("copy", "an empty title", lambda: edit(de / "pdf" / "index.html", lambda s: re.sub(r"<title>.*?</title>", "<title></title>", s, count=1, flags=re.S)), "/de/pdf/ has no title text"),
            ("assets", "a missing image", lambda: remove(pub / "assets" / "templates" / "flowchart-de.png"), "flowchart-de.png is missing"),
            ("sitemap", "a page left out of the sitemap", lambda: edit(pub / "sitemap.xml", lambda s: re.sub(r"<url>\s*<loc>[^<]*/de/pdf/</loc>.*?</url>", "", s, count=1, flags=re.S)), "/de/pdf/ is not in the sitemap"),
            ("parity", "complete but never built", lambda: _move(de, pub / "de.gone"), "de is complete"),
            ("unlisted", "built but not complete", lambda: edit(copy_path, lambda s: s.replace("COMPLETE = True", "COMPLETE = False", 1)), "de is not complete"),
            ("unlisted", "a stray page for a locale that isn't", lambda: _write(pub / "ko" / "index.html", "<html lang=\"ko\"></html>"), "ko is not complete"),
            ("unlisted", "a link into a locale that isn't", lambda: edit(pub / "pdf" / "index.html", lambda s: s.replace("</main>", '<a href="/fr/pdf/">x</a></main>', 1)), "mentions fr, which is not complete"),
        ]
        for rule, label, plant, message in loc_plants:
            undo = plant()
            out = sh(scratch, "scripts/check_locales.py")
            undo()
            rules = set(re.findall(r"check_locales: (\w+):", out.stdout))
            if label == "built but not complete":
                ok_rules = rules == {"unlisted"}
            else:
                ok_rules = rules == {rule}
            r.expect(out.returncode == 1 and message in out.stdout and ok_rules, f"{rule}: {label} -> {message!r}, rules {sorted(rules)}", out.stdout[-900:])
        r.expect(sh(scratch, "scripts/check_locales.py").returncode == 0, "with every plant undone check_locales is clean again")

        other_plants = [
            ("check_hreflang", "a de alternate left out of a page", lambda: edit(pub / "pdf" / "index.html", lambda s: re.sub(r'<link rel="alternate" hreflang="de"[^>]*>\s*', "", s, count=1)), "hreflang set is off (missing ['de']"),
            ("check_hreflang", "the wrong <html lang> on a de page", lambda: edit(de / "pdf" / "index.html", lambda s: s.replace('<html lang="de"', '<html lang="en"', 1)), "<html lang='en'>, expected 'de'"),
            ("check_hreflang", "a de page missing from the sitemap's alternates", lambda: edit(pub / "sitemap.xml", lambda s: s.replace('hreflang="de"', 'hreflang="xx"', 1)), "lists different alternates from its HTML"),
            ("check_invariants", "a missing de page", lambda: remove(de / "pdf" / "index.html"), "de is missing pdf/index.html"),
            ("check_invariants", "a de page without the footer's store line", lambda: edit(de / "pdf" / "index.html", lambda s: s.replace("apps.apple.com", "example.com")), "no de footer Mac App Store line"),
            ("check_legal_render", "a de legal page edited since its render", lambda: edit(scratch / "content" / "legal" / "support.de.md", lambda s: s + "\nx\n"), "support.de.md: edited since the last render"),
        ]
        for script, label, plant, message in other_plants:
            undo = plant()
            out = sh(scratch, f"scripts/{script}.py")
            undo()
            r.expect(out.returncode == 1 and message in out.stdout + out.stderr, f"{script}: {label} -> {message!r}", (out.stdout + out.stderr)[-700:])
        for check in checks:
            out = sh(scratch, "scripts/" + check[0], *check[1:])
            r.expect(out.returncode == 0, "clean again: " + " ".join(check), out.stdout[-500:] + out.stderr[-500:])
    print(f"self-test: {'FAILED, ' + str(r.failures) + ' step(s)' if r.failures else 'every step passed'}")
    return 1 if r.failures else 0


def _move(src: Path, dst: Path):
    src.rename(dst)
    return lambda: dst.rename(src)


def _write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return lambda: shutil.rmtree(path.parent)
