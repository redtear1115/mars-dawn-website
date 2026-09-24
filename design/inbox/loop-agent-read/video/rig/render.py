#!/usr/bin/env python3
"""Cuts take-015346 into the homepage video. Hard cuts only; push-ins are deterministic
crop/zoom keyframes (zoompan on a 2x upscale), never a generative model, so no glyph is redrawn."""
import subprocess, sys, os
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = f"{S}/rec/take-015346/take.mov"
OUT = f"{S}/post"
W, H = 1600, 900
BG = "0x181a1c"
# Terminal content below the title bar (which carries local paths), padded 20px, then scaled.
TERM = f"crop=1240:698:0:60,pad=1280:720:20:20:color={BG},scale={W}:{H}:flags=lanczos"
# Menu bar + window; the status items at x>=1420 (clock, recorder indicator) are covered by a
# copy of the empty menu bar from x=1000.
MENU = ("split[a][b];[b]crop=180:30:1000:0[p];[a][p]overlay=1420:0,"
        f"crop={W}:{H}:0:0")
APP = f"crop={W}:{H}:0:30"

def push(base, rect, dur):
    """base (a filter giving WxH) then a smooth push from the full frame to rect=(x,y,w) in
    base coordinates (h = w*9/16)."""
    x, y, w = rect
    n = int(round(dur * 60))
    p = f"(min(on/{n-1},1))"
    e = f"({p}*{p}*(3-2*{p}))"
    z = f"({W}/({W}+({w}-{W})*{e}))"
    # fps first: the recording is variable-rate, and zoompan emits one frame per input frame.
    return (f"fps=60,{base},scale={2*W}:{2*H}:flags=lanczos,"
            f"zoompan=z='{z}':x='{2*x}*{e}':y='{2*y}*{e}':d=1:s={W}x{H}:fps=60")

# (name, start, end, filter, speed)
SEGS = [
    ("s1-ask",      1.90,  6.60, TERM, 1.25),
    ("s2-open",     6.60, 12.40, TERM, 1.25),
    ("s3-opens",   13.70, 18.20, None, 1.0),   # push, filled below
    ("s4-outline", 18.60, 26.60, MENU, 1.3),
    ("s5-edit",    26.70, 33.70, None, 1.3),   # push
    ("s6-handback",34.75, 41.25, TERM, 1.25),
    ("s7a-reply",  41.25, 44.00, TERM, 1.0),
    ("s7b-update", 44.12, 48.77, None, 1.0),   # push
    ("s8-reread",  48.87, 55.67, APP,  1.3),
    ("s9a-export", 56.07, 62.97, MENU, 1.3),
    ("s9b-pdf",    67.37, 71.27, APP,  1.0),
]
PUSH = {
    "s3-opens":   (APP, (80, 45, 1440)),
    "s5-edit":    (APP, (100, 40, 1400)),
    "s7b-update": (APP, (60, 40, 1440)),
}

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit(f"ffmpeg failed: {' '.join(cmd)}\n{r.stderr[-2000:]}")

parts = []
for name, a, b, vf, speed in SEGS:
    dur = b - a
    if name in PUSH:
        base, rect = PUSH[name]
        vf = push(base, rect, dur)
    if speed != 1.0:
        vf += f",setpts=PTS/{speed}"
    vf += ",fps=60,format=yuv420p"
    out = f"{OUT}/{name}.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a}", "-t", f"{dur}", "-i", SRC,
         "-filter_complex", f"[0:v]{vf}[v]", "-map", "[v]", "-an",
         "-c:v", "libx264", "-crf", "12", "-preset", "slow", out])
    parts.append(out)
    print(f"{name}: {dur/speed:.2f}s")

with open(f"{OUT}/list.txt", "w") as f:
    for p in parts: f.write(f"file '{p}'\n")
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{OUT}/list.txt",
     "-c", "copy", f"{OUT}/master.mp4"])
print("master done")
