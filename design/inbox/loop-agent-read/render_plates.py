#!/usr/bin/env python3
"""Render the three loop plates and their silent clips from plate.html.

    python3 render_plates.py --proof     # nine frames: each scene at 0, 0.5 and 1
    python3 render_plates.py             # 1600×900 stills and 5s silent mp4s

Needs Google Chrome and ffmpeg. Frames stay in a temp directory.
The still is the last frame of each clip, so the picture and the video agree.
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
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools" / "og"))
from cdp import CDP  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PORT = 9347
W, H = 1600, 900
FPS = 12
FRAMES = 60  # 5 seconds
SCENES = ("1", "2", "3")
NAMES = {"1": "01-write", "2": "02-read", "3": "03-revise"}


def start_chrome(profile: str) -> subprocess.Popen:
    proc = subprocess.Popen(
        [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
         "--no-first-run", "--no-default-browser-check",
         f"--user-data-dir={profile}", f"--remote-debugging-port={PORT}",
         f"--window-size={W},{H}", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(150):
        try:
            tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json"))
            page = next(t for t in tabs if t["type"] == "page")
            return proc, page
        except Exception:
            time.sleep(0.2)
    proc.terminate()
    sys.exit("render_plates: Chrome didn't start")


def shoot(cdp, scene: str, progress: float, path: Path) -> None:
    cdp.call(
        "Runtime.evaluate",
        expression=(
            "document.body.dataset.scene = '%s';"
            "document.body.style.setProperty('--p', '%s');"
            "new Promise(r => requestAnimationFrame(() => requestAnimationFrame(() => r(1))))"
        ) % (scene, f"{progress:.4f}"),
        awaitPromise=True,
    )
    shot = cdp.call(
        "Page.captureScreenshot", format="png",
        clip={"x": 0, "y": 0, "width": W, "height": H, "scale": 1})
    path.write_bytes(base64.b64decode(shot["data"]))


def encode(frame_dir: Path, out: Path) -> None:
    subprocess.run(
        ["ffmpeg", "-y", "-framerate", str(FPS), "-i", str(frame_dir / "frame-%03d.png"),
         "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "slow",
         "-crf", "16", "-tune", "animation", "-movflags", "+faststart", str(out)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--proof", action="store_true", help="write nine proof frames and stop")
    args = parser.parse_args()
    profile = tempfile.mkdtemp(prefix="marsdawn-loop-")
    proc, page = start_chrome(profile)
    try:
        cdp = CDP(page["webSocketDebuggerUrl"])
        cdp.call("Page.enable")
        cdp.call("Emulation.setEmulatedMedia", features=[
            {"name": "prefers-color-scheme", "value": "light"}])
        cdp.call("Emulation.setDeviceMetricsOverride",
                 width=W, height=H, deviceScaleFactor=1, mobile=False)
        cdp.call("Page.navigate", url=(HERE / "plate.html").as_uri())
        cdp.call("Runtime.evaluate", expression="document.fonts.ready.then(() => 1)",
                 awaitPromise=True)
        time.sleep(0.3)
        if args.proof:
            proof = HERE / "_proof"
            proof.mkdir(exist_ok=True)
            for scene in SCENES:
                for progress in (0, 0.5, 1):
                    shoot(cdp, scene, progress, proof / f"{NAMES[scene]}-{progress:.1f}.png")
                    print(f"proof {NAMES[scene]} {progress}")
            return
        for scene in SCENES:
            frame_dir = Path(tempfile.mkdtemp(prefix=f"marsdawn-loop-{scene}-"))
            try:
                for i in range(FRAMES):
                    shoot(cdp, scene, i / (FRAMES - 1), frame_dir / f"frame-{i:03d}.png")
                still = HERE / f"{NAMES[scene]}.png"
                shutil.copyfile(frame_dir / f"frame-{FRAMES - 1:03d}.png", still)
                encode(frame_dir, HERE / f"{NAMES[scene]}.mp4")
                print(still.name)
            finally:
                shutil.rmtree(frame_dir, ignore_errors=True)
    finally:
        proc.terminate()
        try:
            proc.wait(10)
        except subprocess.TimeoutExpired:
            proc.kill()
        shutil.rmtree(profile, ignore_errors=True)


if __name__ == "__main__":
    main()
