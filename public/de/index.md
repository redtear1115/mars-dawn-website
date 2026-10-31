Pionierwerkzeug für alle, die bauen

# Sichere dir die Karte. Lies das Morgenrot.

Markdown für Menschen, die agentische Arbeit steuern.

MarsDawn ist eine native macOS-App zum Lesen und Prüfen von Markdown, mit geteilter Live-Vorschau, Mermaid-Diagrammen, KaTeX-Formeln, Übersicht und PDF-Export, 14 Tage kostenlos testbar und einmalig für 4,99 USD freigeschaltet.

Die Seite zeigt ein bedienbares MarsDawn-Fenster mit einem Ausschnitt aus der Einführung der App. Im Palettenmenü wählst du ein Erscheinungsbild (System, Hell, Dunkel) und für Hell und Dunkel je eines von vier Vorschau-Themen (Morgenrot, Klassisch, Modern, Lebhaft), in der Symbolleiste eines von drei Layouts (Quelltext, Geteilt, Vorschau).

## Lies, was dein Agent geschrieben hat, auch fern vom Schreibtisch

1. Lass deinen Agent auf dem Mac seine Dateien in einem Ordner in iCloud Drive speichern.
2. Öffne MarsDawn auf iPhone oder iPad und wähle die Datei aus.
3. Zum Bearbeiten oder für den PDF-Export gehst du zurück an den Mac.

Auf iPhone und iPad ist MarsDawn nur zum Lesen da und öffnet nur Markdown- und reine Textdateien.

[![Laden im App Store](/assets/badges/app-store-de.svg)](https://apps.apple.com/app/id6812925073)

[Mehr zu MarsDawn auf iPhone und iPad](/de/features/#iphone-ipad)

## Lies, was dein Agent geschrieben hat.

1. **Der Agent schreibt.** Dein Coding-Agent oder Schreibassistent entwirft das Markdown: ein README, eine Spezifikation, ein paar Notizen.
2. **Du prüfst in MarsDawn.** Öffne die Datei und lies sie gerendert, mit [Mermaid-Diagrammen](/de/mermaid-preview-mac/) und hervorgehobenem Code, neben dem Quelltext.
3. **Der Agent überarbeitet.** Bitte um Änderungen. Öffne die überarbeitete Datei und lies sie auf dieselbe Weise.

[So prüfst du, was dein Agent zurückgibt](/de/reading-agent-output/) · [So öffnest du .md-Dateien auf dem Mac](/de/view-markdown-on-mac/)

## Prüfe den Plan deines Agenten, bevor er läuft.

Finde den Schritt in der falschen Reihenfolge, zeig auf seine Zeile und gib ihn zurück.

1. Sehen, was sich geändert hat: Sichert der Agent den Plan, aktualisiert sich das offene Fenster von der Festplatte, in einem Schritt, den du widerrufen kannst.
2. Zur Zeile springen: marsdawn open plan-checkout-v2.md:10 bringt das Fenster zu Zeile 10 und lässt den passenden Block aufblinken.
3. Zurückgeben: „Verweis kopieren“ (⌥⌘C) kopiert plan-checkout-v2.md:10; füge es mit deiner Notiz in den Chat des Agenten ein.

## Gleich loslegen

Das kostenlose Befehlszeilenprogramm `marsdawn` ist schon heute verfügbar. Installiere es mit Homebrew:

```
brew install redtear1115/tap/marsdawn
```

- `marsdawn export` macht aus einer Markdown-Datei ein PDF, gerendert wie die Vorschau von MarsDawn. Die App braucht es dafür nicht.
- `marsdawn open` öffnet Dateien in der App MarsDawn, damit du sie prüfen kannst.
- `--json` liefert Skripten und Agenten Ergebnisse, die sie parsen können.

[Befehlszeile](/de/cli/) · [marsdawn für Agenten](/de/cli/agents/) · [Agent-Skill](/de/cli/skill/) · [MCP-Server](/de/cli/mcp/)

## Was du von MarsDawn erwarten kannst

- [Eine Mac-App](/de/native/): Native Fenster und Tabs, automatisches Sichern, [Übersicht](/de/quicklook/).
- [Deine Texte bleiben auf deinem Mac](/de/yours/): Kein Konto, keine Synchronisierung, keine Cloud.
- [Kostenlos testen, einmal bezahlen](/de/pay-once/): 14 Tage kostenlos, danach einmalig 4,99 USD. Kein Abo.
- [Funktionen](/de/features/): Alles, was MarsDawn kann, auf einer Seite.
- [Themen](/de/themes/): Vier integriert, mehr in der Galerie.

Gut zu wissen, bevor du kaufst. [Was MarsDawn nicht kann](/de/limits/)

## Wie die Teile zusammenpassen

Was jeder Teil heute kann, Stand MarsDawn 1.1.1, marsdawn 0.6.4 und marsdawn-mcp v0.2.4.

| Funktion | In der App | CLI | MCP / Skill | Status |
|---|---|---|---|---|
| An einer Zeile öffnen | Springt zur Zeile, Vorschaublock blinkt | `marsdawn open notes.md:120` (`--background` lässt den Fokus) | `open_in_marsdawn`; der Skill öffnet einmal | Verfügbar |
| PDF-Export | Ablage ▸ Als PDF exportieren … (⌥⌘E) | `marsdawn export`, ohne App | `export_markdown_to_pdf`; Skill | Verfügbar |
| JSON-Ergebnis | — | `--json` bei open und export | MCP liefert dasselbe JSON | Verfügbar |
| Agent-Skill | — | `marsdawn skill --install` | Lehrt: einmal öffnen, exportieren | Verfügbar |
| MCP-Server | — | Läuft darunter | marsdawn-mcp: zwei Tools, nur erlaubte Ordner | Verfügbar |
| Für KI kopieren, Verweis kopieren | Bearbeiten ▸ Für KI kopieren (⌃⌥⌘C), Verweis kopieren (⌥⌘C) | — | — (in jeden Agenten einfügen) | Verfügbar |
| Neu laden beim Sichern | Übernimmt die gesicherte Änderung, einmal widerrufbar | — | Skill: nicht erneut öffnen | Verfügbar |
| Claude-Code-Hook | — | Nutzt `open --background` | Hook-Skript von /cli/agents/ | Dokumentiert, optional |

Verfügbar: in der oben genannten Version enthalten. Dokumentiert, optional: Anleitung auf dieser Website, die du selbst einrichtest; nicht im Tool enthalten. Geplant: noch nicht gebaut, ohne Datum. Geplant: eine Ordner-Option im MCP-Tool `open_in_marsdawn`. Weitere Optionen wie `--folder` stehen unter [Befehlszeile](/de/cli/).

## Wenn du Mac-Apps mit einem Coding-Agenten baust

Für Indie-Mac-Entwickler: wie dein Agent das, was er geschrieben hat, heute in MarsDawn öffnet.

| Tool | So arbeiten sie zusammen | Einrichtung |
|---|---|---|
| Claude Code | Der Skill lässt ihn das Geschriebene einmal öffnen, an der Zeile: `marsdawn open plan.md:42`. Ein optionaler Hook öffnet jede .md, die er schreibt, im Hintergrund | `marsdawn skill --install`; das Hook-Skript von /cli/agents/ |
| Codex, Cursor, Xcode | Noch keine Anleitung. Alles, was einen Shell-Befehl ausführen kann, kann `marsdawn open file:line --json` aufrufen; ein Agent, der Anweisungsdateien lädt, kann SKILL.md (`--dir`) nutzen, ein reiner MCP-Client marsdawn-mcp | `brew install redtear1115/tap/marsdawn` |

Hook und Befehle: [marsdawn für Agenten](/de/cli/agents/) · [Agent-Skill](/de/cli/skill/) · [Was MarsDawn nicht kann](/de/limits/)

Du schwankst zwischen MarsDawn, der VS-Code-Vorschau, Obsidian, QLMarkdown und LynxOffice? Der Vergleich zeigt, was jeder Hersteller angibt, was MarsDawn fehlt und wann du es nicht brauchst. [Zum Vergleich](/de/vs/)

## Deine Dokumente bleiben auf deinem Mac

Auf deinem Mac. Lesen, Bearbeiten, Rendern, [PDF-Export](/de/privacy/#exporting-and-printing) und [das Befehlszeilenprogramm marsdawn](/de/privacy/#the-marsdawn-command-line-tool) laufen hier, auch offline; die App lädt deine Dokumente nie hoch.

Mehr dazu: [Datenschutzrichtlinie](/de/privacy/#what-stays-on-your-mac)

Standardmäßig ohne Netz. Bilder aus dem Web laden nur, wenn du auf „Bilder laden“ klickst oder in den Einstellungen „Bilder aus dem Web automatisch laden“ aktivierst; ein HTML-Dokument öffnet sich statisch, sein Code läuft nicht.

Mehr dazu: [Datenschutzrichtlinie](/de/privacy/#when-marsdawn-uses-the-internet)

Nach außen nur, wenn du es wählst. „Für KI kopieren“ legt Text nur in die Zwischenablage, einfügen tust du; ein Theme-Download, ein Dokument, das du mit „Darstellung › Dieses Dokument ausführen“ startest, und die Datei, die du deinen Agenten lesen lässt, gehen nur auf deine Entscheidung hinaus.

Mehr dazu: [Datenschutzrichtlinie](/de/privacy/#when-marsdawn-uses-the-internet)

## Fragen und Antworten

### Was ist MarsDawn?

MarsDawn ist eine native Mac-App, mit der du das Markdown liest und prüfst, das dein Agent geschrieben hat, mit dem Quelltext neben einer Live-Vorschau. Sie zeichnet Mermaid und KaTeX, zeigt .md-Dateien in der Übersicht und exportiert PDF; den Quelltext kannst du auch bearbeiten.

### Ist MarsDawn ein Abo?

Nein. MarsDawn ist ein kostenloser Download mit 14 Tagen Test aller Funktionen. Danach schaltet ein einmaliger In-App-Kauf für 4,99 USD die App dauerhaft frei. Nichts verlängert sich, und es gibt kein Konto.

### Läuft MarsDawn auf dem iPhone oder iPad?

Ja, zum Lesen. Auf iPhone und iPad öffnet MarsDawn Markdown- und reine Textdateien und stellt Mermaid-Diagramme, Formeln, Code und Tabellen dar, mit Gliederung und Themen. Bearbeiten und PDF-Export gibt es dort nicht. Es braucht iOS 26 oder iPadOS 26 oder neuer. Mit demselben Apple Account gelten ein Test und eine Freischaltung für MarsDawn auf Mac, iPhone und iPad.

Mehr dazu: [Roadmap](/de/roadmap/)

### Kann Claude Code Dateien in MarsDawn öffnen?

Ja. Das kostenlose Befehlszeilenprogramm marsdawn hat einen Befehl open, der eine Markdown-Datei in MarsDawn öffnet. Claude Code oder jeder Agent, der einen Shell-Befehl ausführen kann, kann ihn aufrufen. Ein optionaler Claude-Code-Hook kann jede Markdown-Datei öffnen, die Claude schreibt oder bearbeitet.

### Lädt MarsDawn meine Dokumente hoch?

Nein. Die App lädt deine Dokumente nie hoch, erfasst keine Daten über dich und hat kein Konto; Dokumente und Einstellungen bleiben auf deinem Mac. Verweist ein Dokument auf das Web und du lädst diese Inhalte, holt dein Mac sie direkt von den Servern, auf denen sie liegen; der Entwickler von MarsDawn erhält davon nichts.

Mehr dazu: [Datenschutzrichtlinie](/de/privacy/#what-stays-on-your-mac)

### Wer sieht meine Dateien bei MCP oder dem Skill?

MarsDawn selbst sendet nichts. Der Skill ist eine Textdatei mit Anweisungen, das Befehlszeilenprogramm marsdawn und der MCP-Server laufen auf deinem Mac, und der MCP-Server arbeitet nur in Ordnern, die du erlaubst. Wer deine Dateien liest, ist dein Agent; was er und sein Modellanbieter damit tun, regelt die Richtlinie dieses Agenten, die MarsDawn weder steuert noch beschreibt.

Mehr dazu: [MCP](/de/cli/mcp/)

### Ist es sicher, HTML zu öffnen, das mir jemand geschickt hat?

Standardmäßig öffnet es sich statisch: Sein Code läuft nicht, und nichts wird aus dem Web geladen. Wählst du „Darstellung › Dieses Dokument ausführen“, läuft dieses Dokument und kann Daten über das Netzwerk senden sowie Bilder, Stylesheets, Schriften und Medien in seinem Ordner lesen. Die Wahl wird nie gespeichert, beim nächsten Öffnen ist es wieder statisch.

Mehr dazu: [Datenschutzrichtlinie](/de/privacy/#when-marsdawn-uses-the-internet)

### Hat das Analyse-Cookie der Website mit der App zu tun?

Nein. App und Website sind getrennt: Die App erfasst nichts, und ein Besuch kann nur auf marsdawn.southern-light.dev erfasst werden. Google Analytics startet auf der Website abgelehnt und setzt Cookies erst, wenn du im Banner „Akzeptieren“ wählst; über „Cookie-Einstellungen“ in der Fußzeile änderst du das. Anfragen der App nach Theme-Dateien unter /themes/ werden nicht erfasst.

Mehr dazu: [Datenschutzrichtlinie](/de/privacy/#the-website)

### Warum MarsDawn und nicht eine andere App?

Vielleicht brauchst du MarsDawn gar nicht. Wenn du vor allem eigene Notizen schreibst, passt eine Notiz-App wie Obsidian besser. Wenn du den ganzen Tag in VS Code arbeitest, ist die eingebaute Vorschau kostenlos. Wenn du Dateien im Finder nur kurz ansehen willst, reicht eine kostenlose Erweiterung für die Übersicht. Wenn deine PDFs Seitenzahlen brauchen: Die fügt MarsDawn nicht hinzu. MarsDawn ist zum Lesen und Prüfen von Markdown da, das ein Agent geschrieben hat: der Quelltext neben einer Live-Vorschau, eine Änderung deines Agenten, die du in einem Schritt widerrufst, und eine Datei, die genau an der angegebenen Zeile aufgeht. Wenn es nicht zu dir passt, schreib uns, warum.

Mehr dazu: [MarsDawn im Vergleich](/de/vs/) · [Der beste Markdown-Viewer für den Mac](/de/best-markdown-viewer-mac/)

### Wird MarsDawn weiter gepflegt?

Ja. Jedes Update, seit MarsDawn im Mac App Store erschienen ist, steht im Änderungsprotokoll, und seit dem 28. Oktober 2026 gibt es MarsDawn auch auf iPhone und iPad, zum Lesen. Der Rendering-Kern von MarsDawn und das kostenlose Befehlszeilenprogramm marsdawn sind bereits unter der Lizenz Apache-2.0 als Open Source verfügbar, in mars-dawn-kit. Und falls der Entwickler von MarsDawn die App einmal nicht mehr pflegt, wird ihr eigener Quellcode unter einer Open-Source-Lizenz veröffentlicht, damit andere sie weiterführen können.

Mehr dazu: [Änderungsprotokoll](/de/changelog/) · [Roadmap](/de/roadmap/) · [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit)

## Die App, wie sie ist

### [Eine Mac-App](/de/native/)

![MarsDawn in geteilter Ansicht: links der Markdown-Quelltext, rechts die gerenderte Seite.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

Auf diesem Bildschirmfoto:

1. Ein natives Mac-Fenster.
2. Der Texteditor des Mac, mit Markdown-Hervorhebung.
3. ⌘1 Quelltext, ⌘2 geteilt, ⌘3 Vorschau.
4. Die Seite aktualisiert sich beim Tippen.

### [PDF-Export](/de/pdf/)

![Ein aus MarsDawn exportiertes PDF, geöffnet in seinem PDF-Viewer mit Seitenminiaturen.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

Auf diesem Bildschirmfoto:

1. Mermaid-Diagramme, ins PDF gezeichnet.
2. Code behält seine Hervorhebung.

## Mehr

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
- [Mit deinem Agenten ein Thema erstellen](https://marsdawn.southern-light.dev/de/themes/agents/index.md): MarsDawn-Themen-Referenz für KI-Agenten: jedes Feld der theme.json mit Typ und Bereich, Prüfen und Rendern per CLI, ein Übergabe-Link und die Einreichung.
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
- [English](https://marsdawn.southern-light.dev/index.md): Read and review your agent's Markdown, JSON and YAML natively on Mac: live preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/index.md): 檢查 agent 寫的 Markdown、JSON、YAML：Mac 原生 app，即時預覽、Mermaid、KaTeX、快速查看、PDF。免費試用，之後一次 USD 4.99。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/index.md): 检查代理写的 Markdown、JSON、YAML：Mac 原生 app，实时预览、Mermaid、KaTeX、快速查看、PDF。免费试用，之后一次 USD 4.99。
- [日本語](https://marsdawn.southern-light.dev/ja/index.md): エージェントが書いた Markdown・JSON・YAML を確かめる Mac ネイティブアプリ。ライブプレビュー、Mermaid、KaTeX、クイックルック、PDF。無料で試せて、一度だけ USD 4.99。
- [Français](https://marsdawn.southern-light.dev/fr/index.md): Relisez le Markdown, JSON et YAML de votre agent sur Mac : aperçu en direct, Mermaid, KaTeX, Coup d’œil, export PDF. Essai gratuit, puis 4,99 USD une fois.
- [Español](https://marsdawn.southern-light.dev/es/index.md): Revisa el Markdown, JSON y YAML de tu agente en tu Mac: vista previa en vivo, Mermaid, KaTeX, Vista rápida y PDF. Pruébalo gratis y luego 4,99 USD una vez.
- [한국어](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown, JSON, YAML을 검토하는 Mac 네이티브 앱. 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료 체험 후 한 번만 USD 4.99.
