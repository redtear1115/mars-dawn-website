# Mit deinem Agenten ein Thema erstellen

Eine Referenz für einen KI-Agenten, der ein MarsDawn-Vorschau-Thema erstellt. Der Agent schreibt eine `theme.json`, prüft und rendert sie mit dem Befehlszeilenwerkzeug `marsdawn` und gibt dir einen Link. Du stimmst sie auf der Seite [Ein Thema erstellen](/de/themes/new/) nach Augenmaß ab und reichst sie ein. Die Feldtabellen unten sind direkt aus dem Quelltext des Kits gelesen, und eine Prüfung hält sie damit gleich.

**Schreibe eine `theme.json`, führe `marsdawn theme validate theme.json --require-complete --json` aus, bis der Exit-Code 0 ist, rendere sie mit `marsdawn theme preview` in hell und dunkel und gib der Person dann einen Link.** Ein Thema besteht nur aus Parametern. Es enthält nie CSS.

## Was ein Thema ist

- **Farben** für hell und für dunkel: eine Basispalette sowie optionale Syntax- und Diagrammfarben. Jede ist `#RRGGBB`.
- **Ein Schriftdesign**: `sans`, `serif` oder `rounded`.
- **Ein geschlossener Satz von Stiloptionen**: Zahlen in festen Bereichen und Auswahlen aus festen Listen. Eine Farbe in einer Stiloption ist immer eine Palettenrolle wie `accent`, nie eine feste Farbe.
- **Anzeigetexte**: ein Name und eine Zusammenfassung, optional ein Autor und eine Lizenz.

Ein Schlüssel, der nicht in den Tabellen unten steht, ist ein Fehler, ebenso ein doppelt geschriebener Schlüssel. Die Datei darf höchstens 16.384 Bytes groß sein.

## Prüfen und rendern

Führe diese Befehle in dem Ordner aus, der `theme.json` enthält. Sie brauchen das Werkzeug `marsdawn`: siehe [marsdawn für Agenten](/de/cli/agents/).

```
marsdawn theme validate theme.json --require-complete --json
marsdawn theme css theme.json --json
marsdawn theme preview theme.json --appearance light -o light.png
marsdawn theme preview theme.json --appearance dark -o dark.png
```

- Exit-Codes: 0 gültig, 1 ungültig mit Regel-IDs, 2 Datei nicht gefunden, 64 falsche Verwendung. `preview` kennt zusätzlich 4, wenn die PNG-Datei schon existiert (`--force` übergeben oder einen anderen Namen wählen), und 5, wenn das Rendern fehlschlägt.
- Mit `--json` listet ein ungültiges Thema seine Probleme unter `issues` auf, jedes mit einer `rule`-ID, einem `path` und einer `message`. Behebe sie und führe den Befehl erneut aus.
- `--require-complete` ist die Prüfung für ein Thema, das veröffentlicht werden soll: Es verlangt zusätzlich die Farben `syntax` und `diagram` in beiden Paletten.
- `css` gibt das CSS aus, das die Vorschau verwendet. `preview` rendert ein Beispieldokument als PNG. Beide prüfen zuerst, ein ungültiges Thema wird also nicht gerendert.
- Sieh dir das helle und das dunkle PNG an, bevor du das Thema übergibst.

## Mit einem eingebauten Thema beginnen

Kopiere eines der vier eingebauten Themen und ändere es. Jedes ist eine vollständige, gültige Datei:

- [`/assets/theme-sim/kit/themes/dawn.json`](/assets/theme-sim/kit/themes/dawn.json): der Standard und das Beispiel unten
- [`/assets/theme-sim/kit/themes/classic.json`](/assets/theme-sim/kit/themes/classic.json): eine schlichtere, dokumentartige Palette
- [`/assets/theme-sim/kit/themes/modern.json`](/assets/theme-sim/kit/themes/modern.json): eine kühlere, zeitgemäßere Palette
- [`/assets/theme-sim/kit/themes/vivid.json`](/assets/theme-sim/kit/themes/vivid.json): eine hellere Palette mit mehr Kontrast

### Beispiel: Dawn

Das ist `dawn.json`, Byte für Byte. Ihre einzige Stiloption ist eine dünne Linie in der Akzentfarbe für `hr`.

```
{
  "schemaVersion": 1,
  "id": "dawn",
  "version": "1.0.0",
  "name": { "en": "Dawn" },
  "summary": { "en": "Warm Martian sunrise" },
  "fontDesign": "sans",
  "scenarios": ["agent-review"],
  "light": {
    "background": "#FFFDFB", "surface": "#F6F0EC", "text": "#26211F", "muted": "#6F6660",
    "border": "#EADFD8", "heading": "#26211F", "accent": "#C8471B", "link": "#B03C0C", "quote": "#D97A4A",
    "syntax": { "keyword": "#B03C0C", "string": "#2F6F5E", "comment": "#746B66", "number": "#9A5B00", "function": "#5B3E8C", "type": "#1F6FB2" },
    "diagram": { "node": "#FBE9E0", "nodeBorder": "#CA6C3C", "text": "#26211F", "line": "#8A6A5C", "secondary": "#E6F1EE", "tertiary": "#FFF6F1", "note": "#FFF1D6" }
  },
  "dark": {
    "background": "#1C1A1F", "surface": "#262229", "text": "#EBE4DF", "muted": "#A39992",
    "border": "#3A343A", "heading": "#F4EEEA", "accent": "#FF8A50", "link": "#FF9E6B", "quote": "#E08A5C",
    "syntax": { "keyword": "#FF9E6B", "string": "#7FD1B9", "comment": "#938A84", "number": "#F2C572", "function": "#C7A6F5", "type": "#6CB6FF" },
    "diagram": { "node": "#3A2A26", "nodeBorder": "#E08A5C", "text": "#EBE4DF", "line": "#B8A69C", "secondary": "#23332F", "tertiary": "#2B2427", "note": "#3D3322" }
  },
  "style": {
    "hr": { "style": { "type": "line", "color": "accent", "thickness": 1 } }
  }
}
```

## Felder

Jedes Objekt unten wird auf dieselbe Weise gelesen. `required` heißt, der Schlüssel muss vorhanden sein, und ein Schlüssel, der nicht aufgeführt ist, ist ein Fehler.

Typen: `string`, `integer`, `number`, `boolean`, `map` (Sprach-Tag auf Text), `enum` (einer der aufgeführten Werte), `role` (eine Palettenrolle) und `object` (die Tabelle, auf die verlinkt wird). Ein `[]` hinter einem Typ bedeutet eine Liste.

### `theme.json`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `schemaVersion` | `integer` | `required` | Immer `1`. |
| `id` | `string` | `required` | 1 bis 32 Zeichen: Kleinbuchstaben und Ziffern, in Abschnitten, die durch einzelne Bindestriche verbunden sind, etwa `calm-green`. |
| `version` | `string` | `required` | `MAJOR.MINOR.PATCH`, etwa `1.0.0`. |
| `name` | `map` | `required` | Sprach-Tag auf Text. `en` ist erforderlich; andere Schlüssel sind Sprach-Tags wie `zh-Hant`. Jeder Text hat höchstens 48 Zeichen, ohne Links und Zeilenumbrüche. |
| `summary` | `map` | `required` | Dieselbe Form wie `name`, höchstens 120 Zeichen pro Text. |
| `fontDesign` | `enum` | `required` | `sans`, `serif`, `rounded` |
| `scenarios` | `enum[]` | `required` | `agent-review`, `technical-docs`, `formal-output`, `notes-sharing` — Eins oder zwei, ohne Wiederholung. Sie legen fest, wie viel Kontrast das Thema erreichen muss. |
| `author` | `object` | `optional` | [`author`](#t-author) |
| `license` | `string` | `optional` | Eine SPDX-Kennung, etwa `Apache-2.0`. Eingereichte Themen werden unter Apache-2.0 veröffentlicht. |
| `light` | `object` | `required` | [`light, dark`](#t-palette) |
| `dark` | `object` | `required` | [`light, dark`](#t-palette) |
| `style` | `object` | `optional` | [`style`](#t-style) |

### `author`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `name` | `string` | `required` | Höchstens 64 Zeichen, ohne Links. |
| `github` | `string` | `optional` | Ein GitHub-Login. Bei einer Einreichung trägst du den der einreichenden Person ein. |

### `light, dark`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `background` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `surface` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `text` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `muted` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `border` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `heading` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `accent` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `link` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `quote` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `syntax` | `object` | `optional` (zum Veröffentlichen erforderlich, mit `--require-complete`) | [`syntax`](#t-syntax-colors) |
| `diagram` | `object` | `optional` (zum Veröffentlichen erforderlich, mit `--require-complete`) | [`diagram`](#t-diagram-colors) |

### `syntax`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `keyword` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `string` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `comment` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `number` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `function` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `type` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |

### `diagram`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `node` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `nodeBorder` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `text` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `line` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `secondary` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `tertiary` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |
| `note` | `string` | `required` | `#` und sechs Hexziffern, etwa `#1C1C1C`. |

### `style`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `bodySize` | `number` | `optional` | [Bereich](#t-numbers) |
| `lineHeight` | `number` | `optional` | [Bereich](#t-numbers) |
| `headingWeight` | `number` | `optional` | [Bereich](#t-numbers) |
| `radius` | `number` | `optional` | [Bereich](#t-numbers) |
| `maxWidth` | `number` | `optional` | [Bereich](#t-numbers) |
| `h1` | `object` | `optional` | [`style.h1`](#t-style-h1) |
| `h2` | `object` | `optional` | [`style.h2`](#t-style-h2) |
| `blockquote` | `object` | `optional` | [`style.blockquote`](#t-style-blockquote) |
| `hr` | `object` | `optional` | [`style.hr`](#t-style-hr) |
| `table` | `object` | `optional` | [`style.table`](#t-style-table) |
| `listMarker` | `role` | `optional` | [eine Palettenrolle](#roles) |
| `inlineCode` | `role` | `optional` | [eine Palettenrolle](#roles) — Nur `text` oder eine Syntaxrolle: `keyword`, `string`, `comment`, `number`, `function` oder `type`. |
| `link` | `object` | `optional` | [`style.link`](#t-style-link) |
| `syntax` | `object` | `optional` | [`style.syntax`](#t-style-syntax) |

### `style.h1`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `size` | `number` | `optional` | [Bereich](#t-numbers) |
| `letterSpacing` | `number` | `optional` | [Bereich](#t-numbers) |
| `align` | `enum` | `optional` | `left`, `center` |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |

### `style.h2`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `letterSpacing` | `number` | `optional` | [Bereich](#t-numbers) |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.blockquote`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.hr`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |

### `style.table`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `header` | `object` | `optional` | [`type`](#t-kinds) |
| `verticalRules` | `boolean` | `optional` | `true`, `false` |
| `rounded` | `boolean` | `optional` | `true`, `false` |

### `style.link`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `underline` | `boolean` | `optional` | `true`, `false` |

### `style.syntax`

| Feld | Typ | Pflicht | Werte und Hinweise |
|---|---|---|---|
| `boldKeywords` | `boolean` | `optional` | `true`, `false` |

### Optionen mit einem Typ

Diese Stiloptionen sind Objekte mit einem `type`. Jeder `type` nimmt genau die für ihn aufgeführten Felder und keine anderen.

| Option | type | Feld | Pflicht | Typ |
|---|---|---|---|---|
| `style.h1.decoration` | `rule` | — | — | — |
| `style.h1.decoration` | `none` | — | — | — |
| `style.h1.decoration` | `shortRule` | `color` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `from` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `to` | `required` | `role` |
| `style.h2.decoration` | `rule` | — | — | — |
| `style.h2.decoration` | `none` | — | — | — |
| `style.h2.decoration` | `dot` | `color` | `required` | `role` |
| `style.blockquote.style` | `bar` | `width` | `optional` | `number` [Bereich](#t-numbers) |
| `style.blockquote.style` | `panel` | — | — | — |
| `style.hr.style` | `line` | `color` | `optional` | `role` |
| `style.hr.style` | `line` | `thickness` | `optional` | `number` [Bereich](#t-numbers) |
| `style.hr.style` | `shortCentered` | `color` | `required` | `role` |
| `style.hr.style` | `gradient` | `colors` | `required` | `role[]` Zwei oder drei Rollen. |
| `style.table.header` | `surface` | — | — | — |
| `style.table.header` | `accentRule` | `color` | `required` | `role` |
| `style.table.header` | `filled` | `background` | `required` | `role` |
| `style.table.header` | `filled` | `text` | `required` | `role` |
| `style.table.header` | `filled` | `border` | `optional` | `role` |

### Palettenrollen

Eine Palettenrolle ist einer dieser Namen:

`background`, `surface`, `text`, `muted`, `border`, `heading`, `accent`, `link`, `quote`, `keyword`, `string`, `comment`, `number`, `function`, `type`

### Zahlen

Eine Zahl wird auf das nächste Vielfache ihres Schritts gerundet und muss dann zwischen Min und Max liegen. Sonst lautet die Regel `number.range`.

| Feld | Min | Max | Schritt |
|---|---|---|---|
| `style.bodySize` | `14` | `18` | `1` |
| `style.lineHeight` | `1.4` | `1.9` | `0.05` |
| `style.headingWeight` | `400` | `900` | `50` |
| `style.radius` | `0` | `16` | `1` |
| `style.maxWidth` | `600` | `1000` | `1` |
| `style.h1.size` | `1.8` | `2.4` | `0.1` |
| `style.h1.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.h2.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.blockquote.style.width` | `2` | `4` | `1` |
| `style.hr.style.thickness` | `1` | `4` | `1` |

## Was sonst noch geprüft wird

- **Kontrast.** Jedes Farbpaar, das die Vorschau zeichnet, etwa `text` auf `background`, muss für Text 4,5:1 und für Linien und anderes Nicht-Text 3:1 erreichen. Die Szenarien, die du angibst, heben manche Farben auf 4,5:1. Die Meldung nennt das Paar, sein Verhältnis und das geforderte.
- **Texte.** Ein Name, eine Zusammenfassung oder ein Autorenname, der leer oder zu lang ist oder einen Link, ein Steuerzeichen oder ein unsichtbares oder bidirektionales Formatzeichen enthält, wird abgelehnt.
- **Regel-IDs.** Jedes Problem trägt eine, etwa `contrast.pair`, `color.hex`, `number.range`, `id.pattern`, `schema.unknownKey` oder `palette.incomplete`. Korrigiere die Datei nach dem, was die ID und der `path` sagen.

## Als Link übergeben

Die Seite [Ein Thema erstellen](/de/themes/new/) öffnet ein Thema aus einem Link, damit die Person es nach Augenmaß abstimmen kann. Der Link besteht aus der Adresse der Seite, dann `#theme=`, dann den Bytes der Datei als base64url ohne Auffüllzeichen. Die Datei darf höchstens 16.384 Bytes groß sein. Diese eine Zeile baut den Link in zsh und in bash, auf macOS und Linux:

```
printf 'https://marsdawn.southern-light.dev/de/themes/new/#theme=%s\n' "$(base64 < theme.json | tr -d '\n=' | tr '+/' '-_')"
```

Das Thema steht hinter einem `#`, das ein Browser nicht an die Website sendet, und die Website leitet es nirgendwohin weiter. Der Link bleibt aber im Verlauf deiner Shell und des Browsers, und jede Person, der du ihn schickst, kann das Thema lesen.

## Einreichen

Der Agent bereitet die Datei und den Link vor. Die Person reicht ein. Beide Wege verlangen das Developer Certificate of Origin und die Veröffentlichung unter Apache-2.0, und diese Bestätigung gibt die Person ab: Der Agent setzt das Häkchen nicht und unterschreibt nicht für sie.

- **Issue.** Die Person öffnet den Link und klickt auf der Seite „Ein Thema erstellen“ auf **Submit** oder öffnet das [Issue-Formular](https://github.com/redtear1115/mars-dawn-website/issues/new?template=theme-submission.yml) und fügt das JSON in *Theme* ein. Ein Workflow prüft das Thema und antwortet.
- **Pull Request.** Ändere nur `themes/<id>/theme.json`, setze `author.github` auf den Login des Pull-Request-Autors und signiere jeden Commit mit `git commit -s` (Sign-off). Die Regeln stehen in [CONTRIBUTING.md](https://github.com/redtear1115/mars-dawn-website/blob/main/CONTRIBUTING.md).

Autorenname, Name, Zusammenfassung und GitHub-Login eines eingereichten Themas werden dauerhaft öffentlich. Setze `author.name` daher auf einen Namen, den die Person gern veröffentlicht.

## Veröffentlichte Themen

Wie veröffentlichte Themen aussehen, siehst du in der [Themengalerie](/de/themes/gallery/).

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): Lies Markdown, JSON und YAML deines Agenten nativ auf dem Mac: Live-Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Funktionen](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Mac-Editor für Markdown, JSON und YAML: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen und Papierakten.
- [Deine Texte bleiben auf deinem Mac](https://marsdawn.southern-light.dev/de/yours/index.md): MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.
- [Kostenlos testen, einmal bezahlen](https://marsdawn.southern-light.dev/de/pay-once/index.md): MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.
- [PDF-Export](https://marsdawn.southern-light.dev/de/pdf/index.md): Exportiere Markdown auf deinem Mac als PDF oder drucke es, mit Mermaid-Diagrammen und hervorgehobenem Code. Seitenumbrüche vermeiden es, kurze Codeblöcke zu teilen.
- [Eine Mac-App](https://marsdawn.southern-light.dev/de/native/index.md): Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.
- [Was MarsDawn nicht kann](https://marsdawn.southern-light.dev/de/limits/index.md): Keine Synchronisierung, kein Bearbeiten auf iPhone oder iPad, keine Plug-ins, keine Konten. Themen, aber kein eigenes CSS. Vor dem Kauf gut zu wissen.
- [Support](https://marsdawn.southern-light.dev/de/support/index.md): Hilfe zu MarsDawn, dem Markdown-Editor für macOS.
- [Datenschutzrichtlinie](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [So öffnest du .md-Dateien auf dem Mac](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): So öffnest du eine .md-Datei auf dem Mac: Doppelklick, Standard-App, Übersicht im Finder. Von einem KI-Agenten geschriebene .md liest du gerendert in MarsDawn.
- [Mermaid-Vorschau auf dem Mac](https://marsdawn.southern-light.dev/de/mermaid-preview-mac/index.md): Mermaid-Diagramme auf dem Mac neben deinem Markdown: Live-Vorschau, Übersicht und PDF-Export. Ein fehlerhaftes Diagramm zeigt den Fehler und die Zeile.
- [Übersicht für Markdown](https://marsdawn.southern-light.dev/de/quicklook/index.md): Mit MarsDawn zeigt die Übersicht Markdown im Finder per Leertaste gerendert: Mermaid, KaTeX, hervorgehobener Code. Sie funktioniert auch nach dem Test weiter.
- [Markdown zu PDF](https://marsdawn.southern-light.dev/de/markdown-to-pdf/index.md): Wandle Markdown auf dem Mac mit dem kostenlosen Befehlszeilenwerkzeug marsdawn in ein PDF um. Mit Homebrew installieren, einen Befehl ausführen: Tabellen, Mathematik, Mermaid und Code.
- [MarsDawn im Vergleich: VS-Code-Vorschau, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/de/vs/index.md): Für alle, die entscheiden, wie sie Markdown auf dem Mac lesen und prüfen, oft das, was ein Agent geschrieben hat. Jede Zelle unten stammt von den Seiten des Herstellers oder aus unserer eigenen Prüfung, alles am 16. Oktober 2026; Produkte ändern sich, also kann eine Zelle veralten. Wenn du einen Fehler findest, schreib an die Adresse auf Support.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer ist ein Markdown-Viewer nur zum Lesen für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben: 14 Tage kostenlos, dann einmalig 4,99 USD.
- [Der beste Markdown-Viewer für den Mac (2026)](https://marsdawn.southern-light.dev/de/best-markdown-viewer-mac/index.md): Acht Markdown-Viewer für den Mac im Vergleich: Preis, Mermaid, Formeln, PDF, Live-Neuladen, Übersicht, nativ oder Electron, und für wen sich jeder eignet.
- [Befehlszeile](https://marsdawn.southern-light.dev/de/cli/index.md): Das kostenlose Befehlszeilenprogramm marsdawn für den Mac: Markdown aus einer Shell, einem Skript oder einem LLM-Agenten als PDF exportieren, mit JSON-Ausgabe. Installation mit Homebrew.
- [marsdawn für Agenten](https://marsdawn.southern-light.dev/de/cli/agents/index.md): Eine Referenz für KI-Agenten und Skripte, die marsdawn aufrufen, um Markdown in PDF umzuwandeln: Befehle, JSON-Ausgabe, Schemas, Exit-Codes und Voraussetzungen.
- [Agent-Skill](https://marsdawn.southern-light.dev/de/cli/skill/index.md): Eine Datei, die dein Coding-Agent lädt, um geschriebenes Markdown zur Prüfung in MarsDawn zu öffnen, marsdawn zu installieren, Markdown als PDF zu exportieren und das JSON-Ergebnis zu lesen.
- [MCP-Server](https://marsdawn.southern-light.dev/de/cli/mcp/index.md): marsdawn hat kein eigenes KI-Modell, daher ist egal, welcher Agent das Markdown geschrieben hat. Ruf es über die CLI, eine Skill-Datei oder den MCP-Server marsdawn-mcp auf: Alle drei führen denselben Export aus.
- [Review mit wenigen Tokens](https://marsdawn.southern-light.dev/de/token-efficient-review/index.md): Ein Mensch prüft die gerenderte Seite in MarsDawn, sie wird nie in den Kontext des Agenten zurückgelesen. Der Werkzeugaufruf selbst liefert ein kompaktes JSON-Ergebnis statt des gerenderten Inhalts, auch der Aufruf ist also günstig.
- [Markdown anderswo ansehen vs. MarsDawn](https://marsdawn.southern-light.dev/de/vs/markdown-preview-tools/index.md): Wie sich MarsDawn mit dem Lesen von Markdown in der eingebauten Vorschau von VS Code, einer Browsererweiterung oder der Dateivorschau von Claude Desktop vergleicht: was jeweils gerendert wird und was es braucht, eine Datei zu öffnen.
- [Themen](https://marsdawn.southern-light.dev/de/themes/index.md): Vier integrierte Vorschauthemen in Hell und Dunkel sowie eine kuratierte Galerie in den Einstellungen von MarsDawn für Mac. Die Übersicht nutzt das Thema.
- [Ein Thema erstellen](https://marsdawn.southern-light.dev/de/themes/new/index.md): Wähle Farben und ein paar Stiloptionen, sieh sie live auf einem Beispieldokument und reiche dein Thema als GitHub-Issue ein. Keine Installation, kein git.
- [Themen-Galerie](https://marsdawn.southern-light.dev/de/themes/gallery/index.md): Geprüfte Vorschauthemen für MarsDawn durchsuchen, nach Szenario filtern oder ein Problem melden. Eigenes Thema im Browser erstellen, ohne git.
- [Exportierte PDFs teilen](https://marsdawn.southern-light.dev/de/sharing-exported-pdfs/index.md): Exportiere das Markdown eines Agenten als PDF und gib es einer Kollegin, die kein Markdown liest und nichts installieren wird. Zum Öffnen braucht es keine Syntax, keine App und keinen Account.
- [Warum KI-Ergebnisse weiterhin einen menschlichen Leser brauchen](https://marsdawn.southern-light.dev/de/reviewing-ai-output/index.md): Von KI geschriebenes Markdown muss ein Mensch verstehen, nicht auf den ersten Blick glauben. MarsDawn stellt die gerenderte Seite neben den Quelltext und zeichnet Mermaid-Diagramme und KaTeX-Formeln, damit die Struktur auf einen Blick lesbar ist.
- [Lesen, was dein Agent zurückgibt](https://marsdawn.southern-light.dev/de/reading-agent-output/index.md): KI-Agenten geben ihre Arbeit als Markdown zurück: Pläne, Spezifikationen, Fortschrittsberichte. Was Leute, die Agenten bauen, über Checkpoints und Fehler sagen, warum diese Ausgabe schwer zu lesen ist, und eine Checkliste, um einen Plan in fünf Minuten zu prüfen.
- [Transparenz von Agenten](https://marsdawn.southern-light.dev/de/agent-transparency/index.md): Anthropics Leitfaden zum Bau von Agenten verlangt Transparenz: Zeig die Planungsschritte. Was er sagt, was nicht, und warum die Schritte meist als Markdown-Datei enden, die jemand lesen muss.
- [Den Plan eines Agenten prüfen](https://marsdawn.southern-light.dev/de/reviewing-agent-plans/index.md): Ein Weg in sechs Schritten, den Plan eines KI-Agenten zu prüfen, bevor er läuft, in etwa fünf Minuten und in jedem Editor, mit einem durchgespielten Beispiel.
- [Entwurfsmuster für Agenten](https://marsdawn.southern-light.dev/de/agent-design-patterns/index.md): Reflexion, Werkzeugnutzung, Planung und Zusammenarbeit mehrerer Agenten, wie Andrew Ng sie beschrieben hat, und was jedes Muster dir typischerweise zum Lesen zurückgibt.
- [Änderungsprotokoll](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich in jeder Version der MarsDawn-App und des kostenlosen Befehlszeilenprogramms marsdawn geändert hat.
- [Roadmap](https://marsdawn.southern-light.dev/de/roadmap/index.md): Woran wir bei MarsDawn für Mac, iPhone und iPad arbeiten und was als Nächstes kommt, nach Version. Ohne Termine; Ideen ohne Zeitplan sind markiert.
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
- [English](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI 代理的 MarsDawn 主题制作参考：theme.json 每个字段的类型与范围、检查并渲染的 CLI 流程、交给人的链接，以及怎么投稿。
- [日本語](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [Français](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
- [Español](https://marsdawn.southern-light.dev/es/themes/agents/index.md): Referencia de temas de MarsDawn para agentes de IA: cada campo de theme.json con tipo y rango, comprobación y renderizado por CLI, enlace de entrega y envío.
- [한국어](https://marsdawn.southern-light.dev/ko/themes/agents/index.md): MarsDawn 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. theme.json의 모든 필드와 타입, 범위, CLI 검사·렌더링 절차, 넘겨줄 링크, 제출 방법을 담았습니다.
