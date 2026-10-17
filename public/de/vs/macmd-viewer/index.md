# MacMD Viewer oder MarsDawn.

Beides sind Mac-Apps, um Markdown als fertige Seite zu lesen. MacMD Viewer öffnet eine `.md`-Datei und zeigt sie an; die App ist bewusst nur zum Lesen gedacht und speichert nie Änderungen an deiner Datei. MarsDawn stellt neben dieselbe Art gerenderter Vorschau einen Editor, sodass du in einem Fenster schreibst und prüfst. Diese Seite stellt beide Zeile für Zeile nebeneinander, mit einer Quelle für jede Aussage über MacMD Viewer, und nennt auch, wann MacMD Viewer die bessere Wahl ist.

Geprüft gegen die eigene Website und das Repository von MacMD Viewer am 15. Oktober 2026 (Version 1.7.0, veröffentlicht am 10. Oktober 2026). Wenn etwas hier veraltet ist, schreib uns an die Adresse auf der [Support-Seite](/de/support/).

## Was es ist und was es kann

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Was es ist | Ein Viewer: „nur zum Lesen, speichert nie Änderungen an deiner Quelldatei“ [[S1](#s1), [S9](#s9)] | Ein Editor mit Live-Vorschau: links Markdown, rechts die gerenderte Seite, in drei Ansichten (Quelltext, geteilt, Vorschau) |
| Bearbeiten | Nein [[S1](#s1), [S7](#s7), [S9](#s9)] | Ja. Die gerenderte Seite selbst lässt sich nicht bearbeiten; du bearbeitest den Quelltext daneben |
| Live-Vorschau | Rendert die Datei; lädt neu, wenn ein anderer Editor die Datei sichert [[S9](#s9)] | Aktualisiert sich beim Tippen. Ändert eine andere App die Datei, lädt MarsDawn sie neu und behält deine Stelle, solange du selbst keine ungesicherten Änderungen hast. |
| Mermaid | Ja: Flussdiagramme, Sequenz- und Zustandsdiagramme, Gantt-Diagramme, Kreisdiagramme und mehr, offline [[S1](#s1), [S3](#s3), [S7](#s7)] | Ja |
| Mathematik | Nein: Die README sagt, die App „rendert keine Mathematik (LaTeX/KaTeX)“ [[S7](#s7)] | Ja, KaTeX |
| Code-Hervorhebung | Ja [[S1](#s1), [S9](#s9)] | Ja |
| Themes | 12 Dokumentthemen [[S1](#s1), [S7](#s7)] | 4 eingebaute (Morgenrot, Klassisch, Modern, Lebhaft), jeweils mit heller und dunkler Palette, dazu weitere in der Themengalerie |
| Tabs | Ja, optional und standardmäßig aus (seit 1.6.0) [[S5](#s5), [S8](#s8)] | Ja |
| PDF-Export | Ja, eine durchgehende Seite, im aktuellen Theme, ohne Wasserzeichen [[S3](#s3), [S9](#s9)] | Ja, umbrochene Seiten in der hellen Palette des Themes; Seitenumbrüche vermeiden es, kurze Codeblöcke zu teilen |
| Drucken | Ja, über den macOS-Drucken-Dialog [[S3](#s3), [S9](#s9)] | Ja |
| Übersicht im Finder | Ja, enthalten; du aktivierst sie in den Systemeinstellungen; nutzt dein Theme [[S4](#s4)] | Ja, funktioniert mit und ohne Testphase; nutzt dein Theme |
| Mermaid und Mathematik in der Übersicht | Mermaid: ja [[S4](#s4)]. Mathematik: nein, sie wird nicht gerendert [[S7](#s7)] | Ja, beides wird gezeichnet |
| Befehlszeile | Es wird kein eigenständiges Befehlszeilenwerkzeug beschrieben. Es gibt ein URL-Schema `markdownviewer://` und ein Claude-Code-Plug-in samt Hooks, die Dateien im Viewer öffnen [[S6](#s6)] | Das kostenlose Werkzeug `marsdawn`: `marsdawn export` erzeugt ein PDF ohne die App, `marsdawn open` öffnet eine Datei bei einer Zeile |
| Sprachen der Oberfläche | In den eigenen Unterlagen nicht angegeben [[S1](#s1), [S3](#s3), [S7](#s7)] | Englisch, traditionelles Chinesisch, vereinfachtes Chinesisch, Japanisch, Deutsch, Französisch, Spanisch und Koreanisch |
| Voraussetzung | macOS 14 (Sonoma) oder neuer; Apple Silicon und Intel [[S1](#s1), [S7](#s7)] | macOS 26 (Tahoe) oder neuer |
| Andere Plattformen | Nur Mac [[S1](#s1)] | Nur Mac. Keine App für iPhone oder iPad |

## Preis und Kauf

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Wo du es kaufst | Eigene Website, Homebrew oder Setapp; kein Eintrag im Mac App Store [[S2](#s2), [S7](#s7)] | Nur im Mac App Store |
| Preis | Einmalig 19,99 USD für einen aktiven Mac (auf einen anderen Mac übertragbar); Family Pack 39,99 USD für 3; 10 Schlüssel 129 USD [[S2](#s2)] | Kostenloser Download, dann einmalig 4,99 USD |
| Vorher ausprobieren | Keine Testphase und keine kostenlose Stufe; 14 Tage volle Rückerstattung bei Direktkauf [[S2](#s2)] | 14 Tage kostenlos testen, mit allen Funktionen |
| Rückerstattung | Über den eigenen Support, innerhalb von 14 Tagen [[S2](#s2)] | Über Apple |
| Updates | Updates innerhalb der aktuellen Hauptversion sind kostenlos [[S2](#s2)]; der direkte Download aktualisiert sich selbst mit Sparkle [[S7](#s7)] | Über den Mac App Store |
| Account nötig | Nein [[S2](#s2)] | Nein |
| Abo | Nein [[S1](#s1), [S2](#s2)] | Nein |

## Was sich ändert, wenn du nicht mehr testest oder zahlst

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Danach | Keine Testphase; nach dem Kauf funktioniert es dauerhaft | Wenn du nach 14 Tagen nicht freischaltest, öffnen sich Dokumente mit verdecktem Inhalt; deine Dateien bleiben unberührt, die Übersicht und der kostenlose `marsdawn`-Export funktionieren weiter |

## Quellen

- S1 · [https://macmdviewer.com/](https://macmdviewer.com/)
- S2 · [https://macmdviewer.com/pricing](https://macmdviewer.com/pricing)
- S3 · [https://macmdviewer.com/features](https://macmdviewer.com/features)
- S4 · [https://macmdviewer.com/quicklook](https://macmdviewer.com/quicklook)
- S5 · [https://macmdviewer.com/changelog](https://macmdviewer.com/changelog)
- S6 · [https://macmdviewer.com/docs/integrations](https://macmdviewer.com/docs/integrations)
- S7 · [https://github.com/macmdviewer/MacMDViewer](https://github.com/macmdviewer/MacMDViewer)
- S8 · [https://macmdviewer.com/press](https://macmdviewer.com/press)
- S9 · [https://macmdviewer.com/product-facts.md](https://macmdviewer.com/product-facts.md)
- S10 · [https://github.com/macmdviewer/MacMDViewer/releases](https://github.com/macmdviewer/MacMDViewer/releases)

## Welche du wählen solltest

**Wähle MacMD Viewer, wenn** du Markdown nur liest und garantiert haben willst, dass deine Datei nie verändert wird: Die App speichert nie Änderungen daran [[S1](#s1)]. Sie passt auch besser, wenn dein Mac macOS 14 oder 15 nutzt, denn MarsDawn braucht macOS 26 [[S1](#s1), [S7](#s7)]; wenn du lieber auf der Website des Entwicklers, über Homebrew oder Setapp kaufst als im Mac App Store [[S2](#s2), [S7](#s7)]; wenn Dateien, die ein Agent bearbeitet, automatisch im Viewer aufgehen sollen, was über Hooks für Claude Code, Cursor und Windsurf klappt [[S6](#s6)]; oder wenn du ein PDF aus einer durchgehenden Seite statt umbrochener Seiten willst [[S9](#s9)]. Es gibt keine Testphase, aber 14 Tage Rückerstattung [[S2](#s2)].

**Wähle MarsDawn, wenn** das Markdown für eine weitere Runde zurückkommt. Der Plan, die README oder die Spezifikation eines Agenten braucht meist eine Korrektur, eine umformulierte Zeile oder einen neuen Abschnitt, und in MarsDawn machst du das in dem Fenster, in dem du ohnehin liest. Es deckt auch Mathematik (KaTeX) ab, die MacMD Viewer nach eigener Aussage nicht rendert [[S7](#s7)]; es hat acht Oberflächensprachen; es hat eine kostenlose `marsdawn`-Befehlszeile, die ein PDF ohne die App exportiert; und der Preis liegt bei 4,99 USD nach einer 14-tägigen Testphase, in der alles funktioniert.

**Beides geht, wenn** du Markdown auf einem aktuellen Mac liest, Mermaid-Diagramme ordentlich gezeichnet haben willst und die Übersicht im Finder nutzen möchtest. Das können beide.

**Und du kannst beide nutzen.** Sie schließen sich nicht aus: Nichts hindert dich daran, einen reinen Viewer für das zu behalten, was du nur liest, und einen Editor für das, was du schreibst.

## Fragen

### Bearbeitet MacMD Viewer Dateien?

Nein. Die App ist nur zum Lesen da und speichert, in ihren eigenen Worten, nie Änderungen an deiner Quelldatei [[S1](#s1), [S9](#s9)]. Sie kann die Datei in deinem Texteditor öffnen (Menü „Ablage“, ⇧⌘E, seit 1.7.0), was die Datei an eine andere App übergibt [[S5](#s5)].

### Ist MacMD Viewer im Mac App Store?

Die eigenen Seiten nennen die Website, Homebrew und Setapp und erwähnen den Mac App Store nicht [[S2](#s2), [S7](#s7)]. MarsDawn gibt es nur im Mac App Store.

### Kann MarsDawn dieselben Dateien öffnen?

Ja. Es öffnet `.md`-Dateien, außerdem reine Textdateien und PDFs: Text öffnet sich bearbeitbar als UTF-8, PDFs öffnen sich in einem Viewer.

### Was, wenn ich macOS 14 oder 15 nutze?

MacMD Viewer läuft ab macOS 14 [[S1](#s1)]. MarsDawn braucht macOS 26 oder neuer, und das kostenlose Befehlszeilenwerkzeug `marsdawn` kann trotzdem ein PDF exportieren.

### Warum kostet das eine 19,99 USD und das andere 4,99 USD?

Sie unterscheiden sich darin, was du bekommst und wie du zahlst. MacMD Viewer ist ein Einmalkauf mit 14 Tagen Rückerstattung und ohne Testphase [[S2](#s2)]. MarsDawn ist ein kostenloser Download mit 14 Tagen Testphase, danach einmalig freischalten. Keines von beiden ist ein Abo.

## Heute kostenlos ausprobieren

MarsDawn ist im Mac App Store erhältlich. Das kostenlose Befehlszeilenwerkzeug `marsdawn` rendert außerdem jede Markdown-Datei als PDF, mit Mermaid-Diagrammen und hervorgehobenem Code, und braucht sonst nichts:

```
brew tap redtear1115/tap && brew install marsdawn
marsdawn export notes.md
open notes.pdf
```

## Weiter

- Die vollständige Anleitung: [Markdown in PDF](/de/markdown-to-pdf/).
- Was MarsDawn nicht kann: [die Liste](/de/limits/).
- Alle Optionen des Befehlszeilenwerkzeugs: [Befehlszeile](/de/cli/).
- Im Vergleich dazu Markdown in VS Code, im Browser oder in Claude Desktop lesen: [der Vergleich](/de/vs/markdown-preview-tools/).
- Alles, was MarsDawn kann, auf einer Seite: [Funktionen](/de/features/).

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): Lies und prüfe das Markdown deines Agenten nativ auf dem Mac: geteilte Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Funktionen](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
- [Deine Texte bleiben auf deinem Mac](https://marsdawn.southern-light.dev/de/yours/index.md): MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.
- [Kostenlos testen, einmal bezahlen](https://marsdawn.southern-light.dev/de/pay-once/index.md): MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.
- [PDF-Export](https://marsdawn.southern-light.dev/de/pdf/index.md): Exportiere Markdown auf deinem Mac als PDF oder drucke es, mit Mermaid-Diagrammen und hervorgehobenem Code. Seitenumbrüche vermeiden es, kurze Codeblöcke zu teilen.
- [Eine Mac-App](https://marsdawn.southern-light.dev/de/native/index.md): Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.
- [Was MarsDawn nicht kann](https://marsdawn.southern-light.dev/de/limits/index.md): Keine Synchronisierung, keine iPhone- oder iPad-App, keine Plug-ins, keine Konten. Vier integrierte Themen, mehr in der Galerie. Gut zu wissen, bevor du kaufst.
- [Support](https://marsdawn.southern-light.dev/de/support/index.md): Hilfe zu MarsDawn, dem Markdown-Editor für macOS.
- [Datenschutzrichtlinie](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [So öffnest du .md-Dateien auf dem Mac](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): So öffnest du eine .md-Datei auf dem Mac: Doppelklick, Standard-App, Übersicht im Finder. Von einem KI-Agenten geschriebene .md liest du gerendert in MarsDawn.
- [Mermaid-Vorschau auf dem Mac](https://marsdawn.southern-light.dev/de/mermaid-preview-mac/index.md): Mermaid-Diagramme auf dem Mac neben deinem Markdown: Live-Vorschau, Übersicht und PDF-Export. Ein fehlerhaftes Diagramm zeigt den Fehler und die Zeile.
- [Übersicht für Markdown](https://marsdawn.southern-light.dev/de/quicklook/index.md): Mit MarsDawn zeigt die Übersicht Markdown im Finder per Leertaste gerendert: Mermaid, KaTeX, hervorgehobener Code. Sie funktioniert auch nach dem Test weiter.
- [Markdown zu PDF](https://marsdawn.southern-light.dev/de/markdown-to-pdf/index.md): Wandle Markdown auf dem Mac mit dem kostenlosen Befehlszeilenwerkzeug marsdawn in ein PDF um. Mit Homebrew installieren, einen Befehl ausführen: Tabellen, Mathematik, Mermaid und Code.
- [MarsDawn im Vergleich: VS-Code-Vorschau, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/de/vs/index.md): Für alle, die entscheiden, wie sie Markdown auf dem Mac lesen und prüfen, oft das, was ein Agent geschrieben hat. Jede Zelle unten stammt von den Seiten des Herstellers oder aus unserer eigenen Prüfung, alles am 16. Oktober 2026; Produkte ändern sich, also kann eine Zelle veralten. Wenn du einen Fehler findest, schreib an die Adresse auf Support.
- [Der beste Markdown-Viewer für den Mac (2026)](https://marsdawn.southern-light.dev/de/best-markdown-viewer-mac/index.md): Acht Markdown-Viewer für den Mac im Vergleich: Preis, Mermaid, Formeln, PDF, Live-Neuladen, Übersicht, nativ oder Electron, und für wen sich jeder eignet.
- [Befehlszeile](https://marsdawn.southern-light.dev/de/cli/index.md): Das kostenlose Befehlszeilenprogramm marsdawn für den Mac: Markdown aus einer Shell, einem Skript oder einem LLM-Agenten als PDF exportieren, mit JSON-Ausgabe. Installation mit Homebrew.
- [marsdawn für Agenten](https://marsdawn.southern-light.dev/de/cli/agents/index.md): Eine Referenz für KI-Agenten und Skripte, die marsdawn aufrufen, um Markdown in PDF umzuwandeln: Befehle, JSON-Ausgabe, Schemas, Exit-Codes und Voraussetzungen.
- [Agent-Skill](https://marsdawn.southern-light.dev/de/cli/skill/index.md): Eine Datei, die dein Coding-Agent lädt, um geschriebenes Markdown zur Prüfung in MarsDawn zu öffnen, marsdawn zu installieren, Markdown als PDF zu exportieren und das JSON-Ergebnis zu lesen.
- [MCP-Server](https://marsdawn.southern-light.dev/de/cli/mcp/index.md): marsdawn hat kein eigenes KI-Modell, daher ist egal, welcher Agent das Markdown geschrieben hat. Ruf es über die CLI, eine Skill-Datei oder den MCP-Server marsdawn-mcp auf: Alle drei führen denselben Export aus.
- [Review mit wenigen Tokens](https://marsdawn.southern-light.dev/de/token-efficient-review/index.md): Ein Mensch prüft die gerenderte Seite in MarsDawn, sie wird nie in den Kontext des Agenten zurückgelesen. Der Werkzeugaufruf selbst liefert ein kompaktes JSON-Ergebnis statt des gerenderten Inhalts, auch der Aufruf ist also günstig.
- [Markdown anderswo ansehen vs. MarsDawn](https://marsdawn.southern-light.dev/de/vs/markdown-preview-tools/index.md): Wie sich MarsDawn mit dem Lesen von Markdown in der eingebauten Vorschau von VS Code, einer Browsererweiterung oder der Dateivorschau von Claude Desktop vergleicht: was jeweils gerendert wird und was es braucht, eine Datei zu öffnen.
- [Vorschau-Themen und PDF-Export](https://marsdawn.southern-light.dev/de/themes/index.md): Vier Vorschauthemen mit je einer hellen und einer dunklen Palette und ein PDF- und Druckexport, der zum gewählten Thema passt. Bau dein eigenes Thema im Browser und sieh dir die Community-Galerie an.
- [Ein Thema erstellen](https://marsdawn.southern-light.dev/de/themes/new/index.md): Wähle Farben und ein paar Stiloptionen, sieh sie live auf einem Beispieldokument und reiche dein Thema als GitHub-Issue ein. Keine Installation, kein git.
- [Mit deinem Agenten ein Thema erstellen](https://marsdawn.southern-light.dev/de/themes/agents/index.md): MarsDawn-Themen-Referenz für KI-Agenten: jedes Feld der theme.json mit Typ und Bereich, Prüfen und Rendern per CLI, ein Übergabe-Link und die Einreichung.
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
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 4.99 once.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀的 Markdown 檢視器，USD 19.99。MarsDawn 邊編輯邊預覽，免費試用 14 天，之後 USD 4.99 解鎖一次。逐項比較，附來源。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读的 Markdown 查看器，USD 19.99。MarsDawn 边编辑边预览，免费试用 14 天，之后 USD 4.99 解锁一次。逐项比较，附来源。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用の Markdown ビューアで USD 19.99。MarsDawn は編集とプレビューを並べて表示し、14 日間無料、その後 USD 4.99 を一度だけ。項目ごとの比較、出典つき。
- [Français](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer est une visionneuse Markdown en lecture seule à 19,99 USD. MarsDawn modifie avec l’aperçu à côté : 14 jours gratuits, puis 4,99 USD une seule fois.
- [Español](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer es un visor de Markdown de solo lectura por 19,99 USD. MarsDawn edita con la vista previa al lado: 14 días gratis y luego 4,99 USD una sola vez.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
