# Der beste Markdown-Viewer für den Mac (2026)

Welcher Markdown-Viewer der beste ist, hängt davon ab, was du liest. Für eigene Notizen reicht eine Alles-in-einem-Notiz-App. Bei langen Dokumenten mit Diagrammen und Formeln oder bei Dateien, die ein KI-Agent immer wieder neu schreibt, solltest du prüfen, wie jede App mit Live-Neuladen, Mermaid und PDF umgeht. Die Apps stehen in alphabetischer Reihenfolge, jeweils mit Zielgruppe, einem ehrlichen Nachteil und Preis.

## MacDown 3000

Das ursprüngliche MacDown wird nicht mehr gepflegt. MacDown 3000 ist die Fortführung durch die Community: kostenlos und Open Source (MIT), nativ, mit Mermaid, MathJax, PDF-Export, Live-Neuladen und Übersicht.

- Für: alle, die eine kostenlose native geteilte Ansicht wollen.
- Nachteil: Ein Öffnen an einer bestimmten Zeile über die Befehlszeile ist nicht dokumentiert.
- Preis: kostenlos.

## Marked

Marked 3 ist eine Vorschau-App für Markdown, das du in einer anderen App schreibst. Sie lädt neu, sobald sich die Datei ändert, beherrscht MathJax und KaTeX und druckt PDFs mit Seitenumbrüchen und Seitenzahlen. Marked 2 wird weiterhin verkauft.

- Für: Schreibende, die ihr eigenes Schreibwerkzeug behalten und eine saubere Vorschau mit Druck wollen.
- Nachteil: Die Übersicht ist eine separate App, Marked QL (9,99 USD).
- Preis: Marked 3 ist ein kostenloser Download, danach 2,99 USD/Monat, 29,99 USD/Jahr oder 69,99 USD einmalig. Marked 2 kostet direkt 14,99 USD, im Mac App Store 13,99 USD.

## MarkEdit

Eine schlanke, kostenlose native App (CodeMirror in einer Web-View) mit Übersicht.

- Für: alle, die ein schnelles Klartext-Werkzeug wollen, das sich nach Mac anfühlt.
- Nachteil: Mermaid und Formeln brauchen die offiziellen Erweiterungen, PDF-Export braucht Pandoc.
- Preis: kostenlos.

## MarsDawn

Eine native Mac-App, die Quelltext und Live-Vorschau nebeneinander zeigt, mit eingebautem Mermaid und KaTeX. Speichert ein Agent die Datei, übernimmt das offene Fenster die Änderung als ein einziges „Von Festplatte aktualisieren“, das du rückgängig machen kannst. `marsdawn open notes.md:120` öffnet eine Datei an einer Zeile, dazu gibt es einen Skill und einen MCP-Server für Agenten. Die Übersicht funktioniert mit und ohne Test. Mit „Für KI kopieren“ und „Verweis kopieren“ gibst du Text an einen Agenten weiter. Nichts verlässt deinen Mac, außer du willst es.

- Für: alle, die Markdown prüfen, das KI-Agenten schreiben.
- Nachteil: Der PDF-Export hat keine Seitenzahlen.
- Preis: kostenloser Download mit 14 Tagen Test, danach einmalig 4,99 USD. Kein Konto. Nur im Mac App Store.

## Obsidian

Eine Notiz-App rund um einen Vault aus verlinkten Markdown-Dateien, mit Mermaid, MathJax, PDF-Export und Live-Neuladen.

- Für: alle, die aus eigenen Notizen eine Wissensdatenbank aufbauen.
- Nachteil: Es ist eine Electron-App und funktioniert am besten mit Dateien in einem Vault.
- Preis: kostenlos. Sync und Publish kosten extra.

## QLMarkdown

Eine Erweiterung für die Übersicht: Wähle im Finder eine .md-Datei aus und drücke die Leertaste. Mermaid und MathJax sind optional.

- Für: alle, die Dateien im Finder nur kurz ansehen wollen.
- Nachteil: Es ist keine App zum Lesen oder Bearbeiten, und ein PDF-Export ist nicht dokumentiert.
- Preis: kostenlos (GPL-3.0).

## Typora

Ein nahtloses Schreibwerkzeug, bei dem die Vorschau das Dokument ist, mit Mermaid, MathJax und PDF-Export mit Seitenzahlen in Kopf- oder Fußzeile.

- Für: alle, die lieber in einer WYSIWYG-artigen Ansicht schreiben.
- Nachteil: Quelltext und Vorschau stehen nicht nebeneinander.
- Preis: einmalig 14,99 USD, für bis zu 3 Geräte.

## VS-Code-Vorschau

Die eingebaute Markdown-Vorschau, mit Mermaid ab 1.121 und KaTeX. `code -g file:line` öffnet eine Datei an einer Zeile.

- Für: Entwicklerinnen und Entwickler, die ohnehin in VS Code arbeiten.
- Nachteil: Es ist eine Electron-App, und ein PDF-Export ist nicht eingebaut.
- Preis: kostenlos.

## Vergleich

| App | Preis | Mermaid | Formeln | PDF | Live-Neuladen | CLI an Zeile | Übersicht | Bauart |
|---|---|---|---|---|---|---|---|---|
| MacDown 3000 | Kostenlos | Ja | MathJax | Ja | Ja | Nicht dokumentiert | Ja | Nativ |
| Marked 3 | Ab 2,99 USD/Monat | Ja | MathJax, KaTeX | Ja, Seitenzahlen | Ja | Nicht dokumentiert | Marked QL, 9,99 USD | Nativ |
| MarkEdit | Kostenlos | Erweiterung | KaTeX (Erweiterung) | Pandoc | Nicht dokumentiert | Nicht dokumentiert | Ja | Nativ (Web-View) |
| MarsDawn | Einmalig 4,99 USD | Ja | KaTeX | Ja, ohne Seitenzahlen | Ja, rückgängig machbar | Ja | Ja | Nativ |
| Obsidian | Kostenlos | Ja | MathJax | Ja | Ja | Nicht dokumentiert | Nicht dokumentiert | Electron |
| QLMarkdown | Kostenlos | Optional | MathJax (optional) | Nicht dokumentiert | Entfällt | Entfällt | Ist selbst eine | Nativ |
| Typora | Einmalig 14,99 USD | Ja | MathJax | Ja, Seitenzahlen | Nicht dokumentiert | Nicht dokumentiert | Nicht dokumentiert | Nativ |
| VS Code | Kostenlos | Ja (ab 1.121) | KaTeX | Nein | Nicht dokumentiert | Ja | Nicht dokumentiert | Electron |

## Für wen MarsDawn nichts ist

- Du brauchst Seitenzahlen im PDF. Typora und Marked 3 fügen sie hinzu, MarsDawn nicht.
- Du pflegst eine verlinkte Wissensdatenbank aus eigenen Notizen. Dafür ist Obsidian gebaut.
- Du verlässt VS Code nie. Die eingebaute Vorschau ist kostenlos, und VS Code ergänzt sein Agents-Fenster um eine experimentelle Markdown-Ansicht.
- Du willst nur eine Vorschau im Finder. QLMarkdown ist kostenlos.

## Häufige Fragen

### Welche kostenlosen Markdown-Viewer für den Mac können Mermaid?

MacDown 3000, Obsidian und VS Code (ab 1.121) haben es eingebaut. QLMarkdown bietet es als Option, MarkEdit über eine Erweiterung.

### Welche exportieren PDF mit Seitenzahlen?

Typora und Marked 3. MarsDawn exportiert PDF ohne Seitenzahlen.

### Welche öffnen eine Datei über die Befehlszeile an einer bestimmten Zeile?

MarsDawn (`marsdawn open notes.md:120`) und VS Code (`code -g file:line`). Bei den anderen ist es nicht dokumentiert.

### Welche sind native Mac-Apps statt Electron?

Alle außer Obsidian und VS Code. MarkEdit ist nativ, sein Editorbereich läuft in einer Web-View.

[Jetzt laden und testen](https://apps.apple.com/app/id6812925073)

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
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer ist ein Markdown-Viewer nur zum Lesen für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben: 14 Tage kostenlos, dann einmalig 4,99 USD.
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
- [Änderungsprotokoll](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich in jeder Version der MarsDawn-App und des kostenlosen Befehlszeilenprogramms marsdawn geändert hat.
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
- [English](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/best-markdown-viewer-mac/index.md): 比較 8 款 Mac Markdown 檢視器的價格、Mermaid、數學式、PDF、自動重新載入、快速查看與原生／Electron，並說明各自適合誰。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/best-markdown-viewer-mac/index.md): 比较 8 款 Mac Markdown 查看器的价格、Mermaid、数学公式、PDF、自动重新载入、快速查看与原生／Electron，并说明各自适合谁。
- [日本語](https://marsdawn.southern-light.dev/ja/best-markdown-viewer-mac/index.md): Mac向けMarkdownビューア8本を、価格、Mermaid、数式、PDF、自動再読み込み、クイックルック、ネイティブかElectronかで比較し、それぞれ誰に向くかをまとめました。
- [Français](https://marsdawn.southern-light.dev/fr/best-markdown-viewer-mac/index.md): Huit lecteurs Markdown pour Mac comparés : prix, Mermaid, maths, PDF, rechargement en direct, Coup d’œil, natif ou Electron, et à qui chacun convient.
- [Español](https://marsdawn.southern-light.dev/es/best-markdown-viewer-mac/index.md): Ocho visores de Markdown para Mac comparados por precio, Mermaid, fórmulas, PDF, recarga en vivo, Vista rápida y nativo o Electron, y para quién es cada uno.
- [한국어](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
