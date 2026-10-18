#!/usr/bin/env python3
"""One-shot (#262 P1): replace each locale's consent_text with Grok's approved short copy.

The strings are read from issuecomment-6243180186 (pinned by sha256 + updated_at), never typed.
Run: python3 -I -B scripts/consent_copy_262.py            # rewrite the copy files
     python3 -I -B scripts/consent_copy_262.py --check    # compare each built page's banner <p> to the comment
Kept for provenance; it is not part of the site check job.
"""
import hashlib, html, json, re, subprocess, sys
from pathlib import Path

COMMENT = "repos/redtear1115/mars-dawn-website/issues/comments/6243180186"
SHA256 = "2b5d0b7d821c2151710a87d085b04bc38793aeb23c10e34e9d8dac12dfc4aad7"
UPDATED_AT = "2026-10-17T23:38:13Z"
ROOT = Path(__file__).resolve().parent.parent
# locale label in the comment -> (copy file, public dir prefix)
LOCALES = {
    "en": ("build_pages.py", ""), "zh-Hant": ("build_pages.py", "zh-hant/"),
    "ja": ("copy_ja.py", "ja/"), "zh-Hans": ("copy_zh_hans.py", "zh-hans/"),
    "de": ("copy_de.py", "de/"), "fr": ("copy_fr.py", "fr/"),
    "es": ("copy_es.py", "es/"), "ko": ("copy_ko.py", "ko/"),
}

def fetch():
    d = json.loads(subprocess.run(["gh", "api", COMMENT], check=True, capture_output=True, text=True).stdout)
    assert d["updated_at"] == UPDATED_AT, d["updated_at"]
    assert hashlib.sha256(d["body"].encode()).hexdigest() == SHA256, "comment body changed"
    out = {}
    for label in LOCALES:
        m = re.findall(r"\*\*" + re.escape(label) + r"\*\*\n```\n(.*?)\n```", d["body"])
        assert len(m) == 1, (label, m)
        out[label] = m[0]
    return out

def main():
    new = fetch()
    if "--check" in sys.argv:
        bad = 0
        for label, (_, pref) in LOCALES.items():
            # every built page of the locale (the en tree is everything outside the other locales' folders)
            others = tuple("public/" + q for _, (_, q) in LOCALES.items() if q)
            pages = [f for f in (ROOT / "public" / pref).rglob("*.html")
                     if pref or not str(f.relative_to(ROOT)).startswith(others)]
            n_ok = 0
            for f in pages:
                ps = re.findall(r'id="consent-banner"[^>]*>\s*<p>(.*?)</p>', f.read_text(encoding="utf-8"), re.S)
                n_ok += len(ps) == 1 and html.unescape(ps[0]) == new[label]
            ok = n_ok == len(pages) and pages
            print(("ok  " if ok else "FAIL"), label, f"{n_ok}/{len(pages)} pages carry the comment's string byte-for-byte")
            bad += not ok
        sys.exit(1 if bad else 0)
    for label, (fname, _) in LOCALES.items():
        p = ROOT / "scripts" / fname
        src = p.read_text(encoding="utf-8")
        pat = re.compile(r"""(?P<k>['"])consent_text(?P=k): (?P<q>['"])(?P<v>(?:(?!(?P=q)).)*)(?P=q)""")
        ms = list(pat.finditer(src))
        # build_pages.py holds two locales (en, zh-Hant): pick by position, en first
        if fname == "build_pages.py":
            assert len(ms) == 2, ms
            m = ms[0] if label == "en" else ms[1]
        else:
            assert len(ms) == 1, (fname, ms)
            m = ms[0]
        q = m.group("q")
        assert q not in new[label], (label, "quote clash")
        src = src[:m.start("v")] + new[label] + src[m.end("v"):]
        p.write_text(src, encoding="utf-8")
        print("replaced", label, "in", fname)

main()
