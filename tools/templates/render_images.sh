#!/bin/sh
# Renders public/assets/templates/<case>-<locale>.png: the first page of each /templates/ template,
# exported with `marsdawn export` (the renderer MarsDawn's preview uses), 1000 px wide.
# Run on a Mac after changing a template. MARSDAWN picks the binary (default: marsdawn on PATH).
set -eu
MARSDAWN=${MARSDAWN:-marsdawn}
root=$(cd "$(dirname "$0")/../.." && pwd)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
echo "marsdawn $("$MARSDAWN" --version)"
python3 - "$tmp" "$root/scripts" <<'PY'
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[2])
import templates_pages as t
for locale, cases in t.TEMPLATES.items():
    for case, text in cases.items():
        out = Path(sys.argv[1]) / locale / t.FILES[case]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
PY
for dir in "$tmp"/*/; do
  locale=$(basename "$dir")
  for md in "$dir"*.md; do
    case=$(basename "$md" .md)
    "$MARSDAWN" export "$md" -o "$dir$case.pdf" --json >/dev/null
    swift "$root/tools/templates/pdf2png.swift" "$dir$case.pdf" "$root/public/assets/templates/$case-$locale.png" 1000
    echo "$case-$locale.png"
  done
done
