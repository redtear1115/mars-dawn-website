#!/usr/bin/env python3
"""OCR key frames of the cut and compare them with the source texts, word for word.
Expected strings come from the fixtures and from replay.sh, read from disk, never retyped."""
import subprocess, sys, os, re, json
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = sys.argv[1] if len(sys.argv) > 1 else f"{S}/post/master.mp4"
FIX = os.path.expanduser("~/Obsidian/vault/MarsDawn Product Loop Video fixtures")
v1, v2, v3 = (open(f"{FIX}/launch-note.{n}.md").read() for n in ("v1", "v2-user", "v3-agent"))
replay = open(f"{S}/rec/replay.sh").read()
typed = re.findall(r"type_line ['\"](.+?)['\"]\n", replay)
typed = [t.replace('\\"', '"') for t in typed]
said = [s.replace('\\"', '"') for s in re.findall(r'"((?:Saved|Done|Design)[^"\\]*(?:\\"[^"\\]*)*)"', replay)]
said += re.findall(r"'(Saved launch-note\.md[^']*)'", replay)

def norm(s):
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[`*\u2022]", "", s)
    s = s.replace("—", "-").replace("–", "-")
    return re.sub(r"\s+", " ", s).strip()

def para(md, starts):
    for line in md.splitlines():
        if line.startswith(starts): return norm(line)
    raise SystemExit(f"fixture has no line starting {starts!r}")

# Segment start times in the cut, from the rendered parts in list.txt order.
starts, acc = {}, 0.0
for line in open(f"{S}/post/list.txt"):
    f = line.split("'")[1]
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                             capture_output=True, text=True).stdout)
    starts[os.path.basename(f)[:-4]] = (acc, d); acc += d

def ocr(t, crop=None):
    png = f"{S}/post/v-{t:.2f}.png"
    vf = ["-vf", f"crop={crop}"] if crop else []
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", V, "-frames:v", "1", *vf, png], check=True)
    return norm(" ".join(subprocess.run([f"{S}/post/ocr", png], capture_output=True, text=True).stdout.splitlines()))

# Hyphenated wraps in a narrow pane read as "sign- in"; join them before comparing.
def dehyph(s): return re.sub(r"(\w)- (\w)", r"\1-\2", s)

checks = json.load(open(f"{S}/post/checks.json"))
ok = True
for c in checks:
    st, d = starts[c["seg"]]
    c["t"] = round(st + (d + c["at"] if c["at"] < 0 else c["at"]), 2)
    text = dehyph(ocr(c["t"], c.get("crop")))
    for key in c.get("must", []):
        want = dehyph(norm(eval(key)))
        hit = want in text
        ok &= hit
        print(f"{'PASS' if hit else 'FAIL'} t={c['t']} {c['what']}: {want[:70]!r}")
    for bad in c.get("never", []):
        hit = bad in text
        ok &= not hit
        print(f"{'FAIL' if hit else 'PASS'} t={c['t']} {c['what']}: must not show {bad!r}")
    if not all(dehyph(norm(eval(k))) in text for k in c.get("must", [])):
        print("   OCR:", text[:400])
print("ALL PASS" if ok else "SOME FAILED")
sys.exit(0 if ok else 1)
