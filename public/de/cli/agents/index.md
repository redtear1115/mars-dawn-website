# marsdawn für Agenten

Eine Referenz für KI-Agenten und Skripte, die das Befehlszeilenwerkzeug `marsdawn` aufrufen. Jedes Beispiel auf dieser Seite wurde mit dem aus dem aktuellen Quellcode gebauten Werkzeug ausgeführt.

**Um eine Markdown-Datei in ein PDF umzuwandeln, führe `marsdawn export notes.md --json` aus und lies ein JSON-Objekt von stdout.** Mermaid-Diagramme und hervorgehobener Code werden genauso gerendert wie in der MarsDawn-App. `export` braucht die App nicht, `open` schon.

## Was es tut

- `export` rendert eine Markdown-Datei mit demselben Exporter wie die MarsDawn-App zu einem PDF mit Seitenumbrüchen. Es öffnet sich kein Fenster.
- `open` öffnet eine oder mehrere Markdown-Dateien in der MarsDawn-App, damit ein Mensch sie prüfen kann. Es kann für jede Datei die Zeile angeben, bei der sie aufgehen soll, und einen Ordner in der Seitenleiste des Fensters anzeigen.

## Was es nicht tut

- Es liest kein Markdown von stdin. Übergib einen Dateipfad.
- Es schreibt das PDF nicht nach stdout. Das PDF landet immer in einer Datei; stdout enthält nur das Ergebnis.
- Es ersetzt keine vorhandene Datei, außer du übergibst `--force`.
- Es lädt keine Bilder aus dem Web, außer du übergibst `--allow-remote-images`, und dann nur über https.
- `open` funktioniert nicht ohne installierte MarsDawn-App und endet mit Code 3. `export` braucht die App nicht. Die App gibt es im [Mac App Store](https://apps.apple.com/app/id6812925073).
- MarsDawn 1.0 öffnet die Datei in der Zeile, die `open` angibt.
- Es läuft nur unter macOS.

## export

```
marsdawn export notes.md --json
```

Schreibt `notes.pdf` neben `notes.md`. Optionen:

- `-o, --output <path>`: wohin das PDF geschrieben wird. Standard ist der Eingabepfad mit der Endung `.pdf`.
- `--theme <dawn|classic|modern|vivid>`: die helle Farbpalette des Themas. Standard ist `$MARSDAWN_THEME`, sonst `dawn`.
- `--paper <a4|letter>`: Papierformat. Standard ist `a4`.
- `--allow-remote-images`: lädt beim Rendern https-Bilder aus dem Web.
- `--force`: ersetzt die Ausgabedatei, falls sie existiert.
- `--json`: gibt statt Text ein JSON-Objekt auf stdout aus.

```
marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json
```

Erfolg, Exit-Code 0:

```
{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}
```

- `output`: absoluter Pfad des geschriebenen PDFs.
- `pages`: Anzahl der Seiten.
- `theme` und `paper`: die verwendeten Werte.
- `diagramErrors`: eine Meldung pro Mermaid-Diagramm, das nicht gerendert werden konnte. Das PDF wird trotzdem geschrieben.

## open

```
marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json
```

- `path:line` gibt die Zeile an, bei der die Datei aufgehen soll. Eine Spalte dahinter, wie in `notes.md:120:8`, wird ignoriert. Ein Argument, das eine existierende Datei benennt, gilt immer als ganzer Dateiname, eine Datei namens `weird:12` öffnet sich also als sie selbst.
- `--line <n>` gibt die Zeile für eine einzelne Datei an, auch für einen Pfad, der selbst auf Doppelpunkt und Ziffern endet. Es braucht genau eine Datei.
- Zeilen reichen von 1 bis 999999999. Alles andere ist ein Bedienungsfehler.
- Zeilen kamen mit marsdawn 0.3.0 hinzu. MarsDawn 1.0 öffnet die Datei in dieser Zeile.
- Ein Ordner als Argument öffnet sich in der Seitenleiste des Fensters statt als Dokument, `marsdawn open .` zeigt also den aktuellen Ordner; `--folder <path>` tut dasselbe zusätzlich zu Dateien. Die Seitenleiste eines Fensters zeigt einen Ordner: Zwei anzugeben ist ein Bedienungsfehler, ebenso `--folder` zweimal, selbst für denselben Ordner; derselbe Ordner noch einmal als Argument zählt einmal. `--line` mit einem Ordner ist ein Bedienungsfehler, da ein Ordner keine Zeile hat. Es gibt kein `-a`: Wer es übergibt, bekommt einen Bedienungsfehler mit Verweis auf `--folder`.
- `--background` öffnet, ohne MarsDawn in den Vordergrund zu holen, für einen Agenten, der Dateien öffnet, während der Mensch woanders arbeitet. Das JSON ist in beiden Fällen gleich.
- Ordner und `--background` kamen mit marsdawn 0.5.1 hinzu.

Erfolg, Exit-Code 0:

```
{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{"line":120,"path":"/path/to/notes.md"}]}
```

- `opened`: ein Objekt pro Datei, in der angegebenen Reihenfolge. `path` ist der absolute Pfad der Datei; `line` erscheint nur, wenn eine Zeile angefragt wurde.
- `app`: Pfad der MarsDawn-App, die sie geöffnet hat.

Mit einem Ordner (marsdawn 0.5.1 und neuer), Exit-Code 0:

```
{"app":"/Applications/MarsDawn.app","folder":{"path":"/path/to/project","requested":true},"ok":true,"opened":[{"path":"/path/to/project/notes.md"}]}
```

- `folder`: nur vorhanden, wenn ein Ordner angegeben wurde. `path` ist sein absoluter Pfad. `requested` ist immer `true`: marsdawn hat MarsDawn gebeten, den Ordner anzuzeigen, und kann nicht wissen, ob die Seitenleiste ihn zeigt, denn die App fragt den Menschen womöglich erst nach Zugriff. Melde es als angefragt, nicht als erledigt.
- `opened` ist leer, wenn nur ein Ordner angegeben wurde.

marsdawn 0.2.x gab `opened` als Liste von Pfad-Strings aus. Prüfe `marsdawn --version`, wenn du beides verarbeiten musst.

## Dateien öffnen, während Claude Code sie bearbeitet

Ein optionaler [Claude Code Hook](https://code.claude.com/docs/en/hooks): Nachdem Claude eine Markdown-Datei geschrieben oder bearbeitet hat, öffnet er diese Datei im Hintergrund in MarsDawn, einmal pro Datei und Sitzung. Er ist aus, bis du ihn hinzufügst, Projekt für Projekt, denn ein Fenster, um das du nicht gebeten hast, kostet Aufmerksamkeit. Er führt einen Shell-Befehl aus und kostet keine Modell-Tokens.

Er braucht marsdawn 0.5.1 oder neuer, wegen `--background`, und die MarsDawn-App.

Sichere das als `.claude/hooks/marsdawn-open.sh` in deinem Projekt und mach es mit `chmod +x` ausführbar:

```
#!/bin/sh
# Claude Code PostToolUse hook: open a Markdown file Claude just wrote or edited in MarsDawn,
# in the background, once per file per session. Never blocks Claude: every path exits 0.
input=$(cat)
file=$(printf '%s' "$input" | /usr/bin/jq -r '.tool_input.file_path // empty' 2>/dev/null)
session=$(printf '%s' "$input" | /usr/bin/jq -r '.session_id // "unknown"' 2>/dev/null)

case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0
# A hook runs with Claude Code's PATH, which may not include Homebrew's.
marsdawn=$(command -v marsdawn || { [ -x /opt/homebrew/bin/marsdawn ] && echo /opt/homebrew/bin/marsdawn; }) || exit 0
[ -n "$marsdawn" ] || exit 0

# One list per session, so a file opens once however often Claude edits it.
seen="${TMPDIR:-/tmp}/marsdawn-hook/$session"
mkdir -p "$(dirname "$seen")"
grep -qxF "$file" "$seen" 2>/dev/null && exit 0
echo "$file" >> "$seen"

"$marsdawn" open --background "$file" >/dev/null 2>&1 || true
exit 0
```

Füge den Hook dann zu `.claude/settings.json` im Projekt hinzu, oder zu `.claude/settings.local.json`, wenn er nur für dich gelten soll:

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/marsdawn-open.sh" }
        ]
      }
    ]
  }
}
```

- Er läuft nach Claudes Write- und Edit-Werkzeugen. Dateien, die nicht auf `.md` oder `.markdown` enden, bleiben unberührt.
- Jede Datei öffnet sich einmal pro Claude-Code-Sitzung, egal wie oft Claude sie bearbeitet. Die Liste liegt in `$TMPDIR/marsdawn-hook/`, eine Datei pro Sitzung, eine neue Sitzung öffnet die Datei also erneut.
- `--background` hält MarsDawn im Hintergrund: Das Fenster, in dem du gearbeitet hast, behält den Fokus.
- Er kommt Claude nie in die Quere. Jeder Pfad endet mit 0, und wenn marsdawn oder die MarsDawn-App nicht installiert ist, passiert nichts.
- Er liest die Eingabe des Hooks mit `/usr/bin/jq`, das bei macOS 26 dabei ist, der Version, die die MarsDawn-App braucht.
- Zum Abschalten entferne den Eintrag aus der Einstellungsdatei.

## Fehler

Mit `--json` gibt ein Fehler ein JSON-Objekt auf stdout aus und endet mit seinem Code:

```
{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}
```

- `2`, `input_not_found`: Die Eingabe existiert nicht, ist ein Ordner oder ist kein UTF-8-Text; oder ein `--folder`-Pfad existiert nicht oder ist kein Ordner.
- `3`, `app_not_installed`: MarsDawn ist nicht installiert. Nur `open` liefert das.
- `4`, `output_exists`: Die Ausgabedatei existiert. Übergib `--force`.
- `5`, `export_failed`: Der Export selbst ist fehlgeschlagen.
- `6`, `app_cannot_open_folders`: Dieses MarsDawn kann keinen Ordner anzeigen, also wurde nichts geöffnet. Nur `open` liefert das.
- `64`: Bedienungsfehler, etwa eine unbekannte Option, ein ungültiger Wert, eine Zeile außerhalb des Bereichs, `--line` mit mehr als einer Datei oder mit einem Ordner, mehr als ein Ordner oder `-a`. Dieser wird als Text auf stderr ausgegeben, auch mit `--json`.

## JSON-Schemas

JSON Schema (Draft 2020-12) für jedes `--json`-Ergebnis:

- [export.v1.json](/schemas/cli/export.v1.json): export erfolgreich
- [open.v3.json](/schemas/cli/open.v3.json): open erfolgreich, marsdawn 0.5.1 und neuer, einschließlich eines in der Seitenleiste angezeigten Ordners
- [error.v2.json](/schemas/cli/error.v2.json): Fehler, beide Befehle, marsdawn 0.5.2 und neuer
- [open.v2.json](/schemas/cli/open.v2.json): open erfolgreich, marsdawn 0.3.0 bis 0.5.0
- [open.v1.json](/schemas/cli/open.v1.json): open erfolgreich, marsdawn 0.2.x, wo `opened` eine Liste von Pfaden war
- [error.v1.json](/schemas/cli/error.v1.json): Fehler, beide Befehle, marsdawn 0.5.1 und älter

## Umgebungsvariablen

- `MARSDAWN_THEME`: das Thema, das `export` verwendet, wenn `--theme` nicht übergeben wird. Ein unbekannter Wert fällt ohne Fehler auf `dawn` zurück.

## Voraussetzungen

- Das Werkzeug läuft unter macOS 15 oder neuer. Auf Apple Chips installiert Homebrew eine fertig gebaute Bottle, und sonst wird nichts gebraucht. Selbst bauen, auf einem Intel-Mac oder aus dem Quellcode, erfordert Swift 6.2 oder neuer, das mit Xcode 26 oder neuer kommt.
- Die MarsDawn-App erfordert macOS 26 oder neuer.

## Installieren

Mit Homebrew. Auf Apple Chips installiert es in Sekunden eine fertig gebaute Bottle, ganz ohne Xcode. Auf einem Intel-Mac kompiliert es marsdawn aus dem Quellcode, was ein paar Minuten dauert und Xcode 26 oder neuer erfordert.

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn --version
```

Oder bau es aus [dem Quellcode](https://github.com/redtear1115/mars-dawn-kit). Der erste Build lädt Abhängigkeiten und kompiliert, was ebenfalls ein paar Minuten dauert.

```
git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json
```

`marsdawn --version` gibt die Versionsnummer aus, etwa `0.3.0`, und endet mit Code 0.

## Weiter

- Ein Skill in einer Datei für Agenten, die Anweisungen lesen statt eine Shell zu benutzen: [der marsdawn-Skill](/de/cli/skill/).
- Ein MCP-Server, der genau dieses `export` umschließt: [marsdawn-mcp](/de/cli/mcp/).
- Warum dieses JSON-Ergebnis für den eigenen Kontext eines Agenten günstig bleibt: [Token-sparsames Prüfen](/de/token-efficient-review/).

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): Markdown für Menschen, die agentische Arbeit steuern: ein nativer Mac-Editor mit Live-Vorschau, Mermaid-Diagrammen und PDF-Export. Im Mac App Store.
- [Deine Texte bleiben auf deinem Mac](https://marsdawn.southern-light.dev/de/yours/index.md): MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.
- [Kostenlos testen, einmal bezahlen](https://marsdawn.southern-light.dev/de/pay-once/index.md): MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.
- [PDF-Export](https://marsdawn.southern-light.dev/de/pdf/index.md): Exportiere Markdown auf deinem Mac als PDF oder drucke es, mit Mermaid-Diagrammen und hervorgehobenem Code. Seitenumbrüche vermeiden es, kurze Codeblöcke und Tabellen zu teilen.
- [Eine Mac-App](https://marsdawn.southern-light.dev/de/native/index.md): Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.
- [Was MarsDawn nicht kann](https://marsdawn.southern-light.dev/de/limits/index.md): Keine Synchronisierung, keine App für iPhone oder iPad, keine Plug-ins, keine Konten. Vier integrierte Themen. Gut zu wissen, bevor du kaufst.
- [Support](https://marsdawn.southern-light.dev/de/support/index.md): Hilfe zu MarsDawn, dem Markdown-Editor für macOS.
- [Datenschutzrichtlinie](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [Markdown auf dem Mac ansehen](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): Eine .md-Datei ist reiner Text mit Formatierungszeichen. So liest du sie auf dem Mac gerendert: heute als PDF mit dem kostenlosen Befehlszeilenwerkzeug marsdawn und in der MarsDawn-App aus dem Mac App Store.
- [Markdown zu PDF](https://marsdawn.southern-light.dev/de/markdown-to-pdf/index.md): Wandle Markdown auf dem Mac mit dem kostenlosen Befehlszeilenwerkzeug marsdawn in ein PDF um. Mit Homebrew installieren, einen Befehl ausführen: Tabellen, Mathematik, Mermaid und Code.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer zeigt Markdown nur zum Lesen an, für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben, kostenlos testen, dann einmalig 4,99 USD im Mac App Store.
- [Befehlszeile](https://marsdawn.southern-light.dev/de/cli/index.md): Das kostenlose Befehlszeilenprogramm marsdawn für den Mac: Markdown aus einer Shell, einem Skript oder einem LLM-Agenten als PDF exportieren, mit JSON-Ausgabe. Installation mit Homebrew.
- [Agent-Skill](https://marsdawn.southern-light.dev/de/cli/skill/index.md): Eine Datei, die dein Coding-Agent lädt, um geschriebenes Markdown zur Prüfung in MarsDawn zu öffnen, marsdawn zu installieren, Markdown als PDF zu exportieren und das JSON-Ergebnis zu lesen.
- [MCP-Server](https://marsdawn.southern-light.dev/de/cli/mcp/index.md): marsdawn hat kein eigenes KI-Modell, daher ist egal, welcher Agent das Markdown geschrieben hat. Ruf es über die CLI, eine Skill-Datei oder den MCP-Server marsdawn-mcp auf: Alle drei führen denselben Export aus.
- [Review mit wenigen Tokens](https://marsdawn.southern-light.dev/de/token-efficient-review/index.md): Ein Mensch prüft die gerenderte Seite in MarsDawn, sie wird nie in den Kontext des Agenten zurückgelesen. Der Werkzeugaufruf selbst liefert ein kompaktes JSON-Ergebnis statt des gerenderten Inhalts, auch der Aufruf ist also günstig.
- [Markdown anderswo ansehen vs. MarsDawn](https://marsdawn.southern-light.dev/de/vs/markdown-preview-tools/index.md): Wie sich MarsDawn mit dem Lesen von Markdown in der eingebauten Vorschau von VS Code, einer Browsererweiterung oder der Dateivorschau von Claude Desktop vergleicht: was jeweils gerendert wird und was es braucht, eine Datei zu öffnen.
- [Vorschau-Themen und PDF-Export](https://marsdawn.southern-light.dev/de/themes/index.md): Vier Vorschauthemen mit je einer hellen und einer dunklen Palette und ein PDF- und Druckexport, der zum gewählten Thema passt. Bau dein eigenes Thema im Browser und sieh dir die Community-Galerie an.
- [Ein Thema erstellen](https://marsdawn.southern-light.dev/de/themes/new/index.md): Wähle Farben und ein paar Stiloptionen, sieh sie live auf einem Beispieldokument und reiche dein Thema als GitHub-Issue ein. Keine Installation, kein git.
- [Themen-Galerie](https://marsdawn.southern-light.dev/de/themes/gallery/index.md): Durchsuche Vorschau-Themen, die die Community für MarsDawn eingereicht hat, filtere nach Szenario und melde ein Problem. Bau dein eigenes im Browser, ohne Installation und ohne git.
- [Exportierte PDFs teilen](https://marsdawn.southern-light.dev/de/sharing-exported-pdfs/index.md): Exportiere das Markdown eines Agenten als PDF und gib es einer Kollegin, die kein Markdown liest und nichts installieren wird. Zum Öffnen braucht es keine Syntax, keine App und keinen Account.
- [Warum KI-Ergebnisse weiterhin einen menschlichen Leser brauchen](https://marsdawn.southern-light.dev/de/reviewing-ai-output/index.md): Von KI geschriebenes Markdown muss ein Mensch verstehen, nicht auf den ersten Blick glauben. MarsDawn stellt die gerenderte Seite neben den Quelltext und zeichnet Mermaid-Diagramme und KaTeX-Formeln, damit die Struktur auf einen Blick lesbar ist.
- [Lesen, was dein Agent zurückgibt](https://marsdawn.southern-light.dev/de/reading-agent-output/index.md): KI-Agenten geben ihre Arbeit als Markdown zurück: Pläne, Spezifikationen, Fortschrittsberichte. Was Leute, die Agenten bauen, über Checkpoints und Fehler sagen, warum diese Ausgabe schwer zu lesen ist, und eine Checkliste, um einen Plan in fünf Minuten zu prüfen.
- [Transparenz von Agenten](https://marsdawn.southern-light.dev/de/agent-transparency/index.md): Anthropics Leitfaden zum Bau von Agenten verlangt Transparenz: Zeig die Planungsschritte. Was er sagt, was nicht, und warum die Schritte meist als Markdown-Datei enden, die jemand lesen muss.
- [Den Plan eines Agenten prüfen](https://marsdawn.southern-light.dev/de/reviewing-agent-plans/index.md): Ein Weg in sechs Schritten, den Plan eines KI-Agenten zu prüfen, bevor er läuft, in etwa fünf Minuten und in jedem Editor, mit einem durchgespielten Beispiel.
- [Entwurfsmuster für Agenten](https://marsdawn.southern-light.dev/de/agent-design-patterns/index.md): Reflexion, Werkzeugnutzung, Planung und Zusammenarbeit mehrerer Agenten, wie Andrew Ng sie beschrieben hat, und was jedes Muster dir typischerweise zum Lesen zurückgibt.
- [Änderungsprotokoll](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich im kostenlosen Befehlszeilenprogramm marsdawn geändert hat.
- [Lektürenotizen der Redaktion](https://marsdawn.southern-light.dev/de/reading-notes/index.md): Sechs kurze Notizen dazu, was die Leute, die KI-Agenten bauen, tatsächlich argumentieren — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain und Andrew Ng — und was das jeweils für die Person bedeutet, die lesen muss, was so ein Agent zurückgibt.
- [Lektürenotizen: Anthropic](https://marsdawn.southern-light.dev/de/reading-notes/anthropic-building-effective-agents/index.md): Anthropics Leitfaden vom Dezember 2024 für Leute, die Agenten bauen, trennt Workflows von Agenten und beschreibt fünf Workflow-Muster, darunter eines, bei dem ein zweiter LLM-Aufruf den ersten prüft. Was das für Dateien in deinem Ordner bedeutet.
- [Lektürenotizen: Chip Huyen](https://marsdawn.southern-light.dev/de/reading-notes/chip-huyen-agents/index.md): Chip Huyens Essay „Agents“ vom Januar 2025 teilt Aktionen von Agenten in read-only und write. Warum diese Aufteilung ein schneller Weg ist, in einem Plan die Zeile zu finden, die vor der Freigabe einen genaueren Blick verdient.
- [Lektürenotizen: Lilian Weng](https://marsdawn.southern-light.dev/de/reading-notes/lilian-weng-llm-agents/index.md): Lilian Wengs viel zitierte Umfrage von 2023 beschreibt einen LLM-Agenten als Gehirn plus Planung, Gedächtnis und Werkzeugnutzung. Was jeder Teil dir typischerweise zum Lesen hinterlässt, und die Grenze, die sie bei Plänen nennt, die sich Überraschungen nicht anpassen.
- [Lektürenotizen: Harrison Chase](https://marsdawn.southern-light.dev/de/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chases Definition eines Agenten von 2024 und sein Spektrum agentischen Verhaltens, und sein Plädoyer für Beobachtbarkeit, je weiter ein System darauf wandert — gelesen von der Seite der Person, die die Datei liest, die er zurückgibt.
- [Lektürenotizen: LangChain (Jess Ou)](https://marsdawn.southern-light.dev/de/reading-notes/langchain-what-is-an-agent/index.md): LangChains „What is an AI agent?“ von Jess Ou (2026) greift Harrison Chases Definition von 2024 auf und beschreibt eine Pipeline zur automatischen Bewertung von Agenten. Wo diese Pipeline noch einen Schritt an eine Person übergibt — und wo nicht.
- [Lektürenotizen: Andrew Ng](https://marsdawn.southern-light.dev/de/reading-notes/andrew-ng-design-patterns/index.md): Über fünf Briefe in The Batch ordnet Andrew Ng Reflexion, Werkzeugnutzung, Planung und Multi-Agenten-Zusammenarbeit danach, wie verlässlich und vorhersagbar er jedes findet — und was diese Rangfolge dazu nahelegt, wie genau man die Ausgabe jedes Musters prüfen sollte.
- [Vorlagen](https://marsdawn.southern-light.dev/de/templates/index.md): Markdown-Vorlagen für die Dokumente, die ein Agent schreibt und du liest: eine Spezifikation, ein Flussdiagramm und ein Protokoll, jeweils mit einem Prompt für deinen Agenten.
- [Spezifikationsvorlage](https://marsdawn.southern-light.dev/de/templates/spec/index.md): Eine Markdown-Vorlage für Spezifikationen mit Anforderungen, einem Mermaid-Ablaufdiagramm und Akzeptanzkriterien. Dein Agent füllt sie aus, du prüfst sie in MarsDawn.
- [Flussdiagramm-Vorlage](https://marsdawn.southern-light.dev/de/templates/flowchart/index.md): Eine Mermaid-Flussdiagramm-Vorlage in Markdown, darunter die Schritte ausgeschrieben. Auf dem Mac in der Vorschau ansehen und als PDF exportieren.
- [Protokollvorlage](https://marsdawn.southern-light.dev/de/templates/meeting-notes/index.md): Eine Markdown-Vorlage für Besprechungsprotokolle mit Entscheidungen und Aufgaben, jeweils mit einer verantwortlichen Person. Dein Agent schreibt es, du prüfst es in MarsDawn.
- [English](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/cli/agents/index.md): 給呼叫 marsdawn 把 Markdown 轉成 PDF 的 AI agent 與腳本的參考：指令、JSON 輸出、Schema、離開代碼與系統需求。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/cli/agents/index.md): 给调用 marsdawn 把 Markdown 转成 PDF 的 AI agent 与脚本的参考：命令、JSON 输出、Schema、退出代码与系统需求。
- [日本語](https://marsdawn.southern-light.dev/ja/cli/agents/index.md): marsdawn を呼び出して Markdown を PDF に変換する AI エージェントとスクリプトのためのリファレンス：コマンド、JSON 出力、スキーマ、終了コード、必要環境。
- [Français](https://marsdawn.southern-light.dev/fr/cli/agents/index.md): Une référence pour les agents IA et les scripts qui appellent marsdawn pour convertir du Markdown en PDF : commandes, sortie JSON, schémas, codes de sortie et configuration requise.
- [Español](https://marsdawn.southern-light.dev/es/cli/agents/index.md): Una referencia para agentes de IA y scripts que llaman a marsdawn para convertir Markdown en PDF: comandos, salida JSON, esquemas, códigos de salida y requisitos.
- [한국어](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
