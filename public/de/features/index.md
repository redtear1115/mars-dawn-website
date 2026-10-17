# Alles, was MarsDawn kann, auf einer Seite.

MarsDawn ist ein Markdown-Editor für den Mac. Auf der einen Seite schreibst du, auf der anderen liest du die gerenderte Seite, mit eingezeichneten Diagrammen, Formeln und Code. Er hat kein eigenes KI-Modell: Er ist dafür gemacht, zu lesen, was ein Agent geschrieben hat, und eigene Texte zu schreiben. Und wenn die Arbeit an einen Tisch, in eine Besprechung oder in einen Aktenschrank wandert, druckt und exportiert er saubere Seiten.

Jeder Abschnitt unten sagt, was die App kann, und verlinkt auf die Seite, die mehr dazu erklärt.

![MarsDawn in geteilter Ansicht: links der Markdown-Quelltext, rechts die gerenderte Seite.](https://marsdawn.southern-light.dev/assets/screens/01-split-1180.png)

Auf diesem Bildschirmfoto:

1. Ein natives Mac-Fenster.
2. Der Texteditor des Mac, mit Markdown-Hervorhebung.
3. ⌘1 Quelltext, ⌘2 geteilt, ⌘3 Vorschau.
4. Die Seite aktualisiert sich beim Tippen.

## Lesen, was dein Agent geschrieben hat

### Quelltext und Vorschau nebeneinander

Öffne eine Markdown-Datei und lies die gerenderte Seite neben ihrem Quelltext (⌘2) oder wechsle zu „Nur Quelltext“ (⌘1) oder „Nur Vorschau“ (⌘3). Beide Bereiche scrollen gemeinsam, und die Seite aktualisiert sich beim Tippen.

[Eine Mac-App](/de/native/)

### Gliederung und Dateien in der Seitenleiste

Der Tab „Gliederung“ der Seitenleiste listet die Überschriften eines Dokuments auf; mit einem Klick springst du dorthin. Öffne einen Ordner, dann listet der Tab „Dateien“ auf, was darin liegt, und neue Dateien erscheinen von selbst, während ein Agent hineinschreibt. Ist der Ordner ein Git-Checkout, nennt die Kopfzeile den Branch oder Worktree.

[Lesen, was dein Agent zurückgibt](/de/reading-agent-output/)

### Auf die genaue Zeile zeigen

Bearbeiten ▸ Verweis kopieren kopiert deine Position als Pfad und Zeile, etwa `docs/plan.md:42`. Für KI kopieren fügt darunter den ausgewählten Text hinzu. Setze beides in den Chat des Agenten ein.

[Lesen, was dein Agent zurückgibt](/de/reading-agent-output/)

### Links zwischen Dateien folgen

Klicke in der Vorschau auf einen Link zu einer anderen Markdown-Datei, und MarsDawn öffnet sie oder holt sie nach vorn, falls sie schon geöffnet ist, und scrollt zur Überschrift.

## Auf Papier, unter Menschen

Nicht alle Arbeit passiert auf einem Bildschirm. Die Seiten, die MarsDawn druckt und exportiert, sind dieselben, die du am Bildschirm liest. Sie funktionieren daher dort, wo Menschen sich treffen, lesen und Aufzeichnungen aufbewahren.

### In der Besprechung

Drucke die Seiten aus oder schicke allen dasselbe PDF, dann arbeitet die ganze Runde mit demselben Dokument statt an einem gemeinsamen Bildschirm. Wer dieselbe Datei hat, hat dieselben Seitenumbrüche, sodass „die Tabelle auf Seite 3“ für alle dasselbe meint. Dann halten die Leute die Beschlüsse fest, auf dem Ausdruck oder in Notizen. Die Vorlage für Besprechungsnotizen beginnt mit den Beschlüssen und gibt jedem Aktionspunkt eine verantwortliche Person.

[PDF-Export](/de/pdf/) · [Protokollvorlage](/de/templates/meeting-notes/)

### Mit dem Stift lesen

Manche nehmen Dinge besser mit einem Stift auf: unterstreichen, an den Rand schreiben, damit es hängen bleibt. Drucke das Dokument aus und tu das auf Papier. MarsDawn hat kein eigenes Werkzeug für Anmerkungen. Wenn du das PDF lieber digital markieren möchtest, nimm die PDF-App, die du ohnehin hast.

[PDF-Export](/de/pdf/)

### Papierakten

In manchen Bereichen wird weiterhin Papier abgelegt, etwa in der Buchhaltung. MarsDawn erhebt keinen Anspruch auf Archivierung oder Compliance. Es druckt und exportiert saubere Seiten mit Seitenumbrüchen: Diagramme eingezeichnet, kurze Codeblöcke am Stück, in den hellen Farben des Themes. Nutze sie überall dort, wo Papier noch die Akte ist.

[PDF-Export](/de/pdf/)

### Für Menschen, die kein Markdown nutzen

Ein PDF lässt sich überall öffnen und setzt keine Markdown-Kenntnisse voraus, daher eignet es sich auch zum Versand an Vorgesetzte oder Kundschaft.

[Exportierte PDFs teilen](/de/sharing-exported-pdfs/)

## Schreiben und gestalten

### Reines Markdown, hervorgehoben

Fett, kursiv, durchgestrichen, Inline-Code, Links, Zitate und Aufgabenlisten funktionieren alle. Der Editor färbt die Markdown-Syntax ein, und die Farben passen zum Theme deiner Vorschau.

[Eine Mac-App](/de/native/)

### Zoom, Zeilennummern und eine Statusleiste

Zoome Quelltext und Vorschau gemeinsam von 50 % bis 300 %. Neben dem Quelltext läuft eine Spalte mit Zeilennummern, und die Statusleiste zeigt Zeile und Spalte sowie Wort- und Zeichenzahl und die Lesezeit für das Dokument oder deine Auswahl.

### Bilder

Sichere das Dokument und ziehe dann ein Bild in den Editor oder setze es ein. MarsDawn kopiert es in einen Ordner assets neben dem Dokument und schreibt den Link. Bilder aus dem Web bleiben ausgeblendet, bis du auf „Bilder laden“ klickst, sodass das Öffnen eines Dokuments keinem Server verrät, dass du es liest.

[Deine Texte bleiben auf deinem Mac](/de/yours/)

### Front Matter bleibt aus dem Weg

Ein Front-Matter-Block am Dateianfang erscheint in der Vorschau und in der Übersicht als eingeklappter Abschnitt „Dokumentinfo“ und wird im PDF weggelassen.

### Acht Sprachen

Die App gibt es auf Englisch, traditionellem Chinesisch, vereinfachtem Chinesisch, Japanisch, Deutsch, Französisch, Spanisch und Koreanisch.

[Eine Mac-App](/de/native/)

## Diagramme, Code und Formeln

### Mermaid-Diagramme

Ein mit `mermaid` markierter Codeblock wird als Diagramm gezeichnet. Enthält das Diagramm einen Fehler, zeigt die Vorschau seinen Quelltext mit dem Fehler darunter, und ein Klick auf die Meldung springt zu dieser Zeile.

[Mermaid-Vorschau auf dem Mac](/de/mermaid-preview-mac/)

### Hervorgehobener Code

Codeblöcke werden für die meisten gängigen Sprachen hervorgehoben. Nenne die Sprache nach dem öffnenden `````.

### Formeln

In KaTeX-Syntax geschriebene Formeln werden in der Vorschau und in der Übersicht gezeichnet und kommen im exportierten PDF an.

[Warum KI-Ergebnisse weiterhin einen menschlichen Leser brauchen](/de/reviewing-ai-output/)

## Themes, PDF und Druck

### Vier Themes, hell und dunkel

Morgenrot, Klassisch, Modern und Lebhaft gibt es jeweils in einer hellen und einer dunklen Version, und MarsDawn folgt dem Erscheinungsbild deines Mac, sofern du in den Einstellungen keines wählst. Wähle über Darstellung ▸ Vorschau-Thema oder mit der Palettentaste in der Symbolleiste.

[Vorschau-Themen und PDF-Export](/de/themes/)

### Weitere Themes

Einstellungen ▸ Erscheinungsbild ▸ Weitere Themes laden … öffnet eine Galerie mit zusätzlichen Vorschau-Themes. Installiere eines, dann erscheint es unter Darstellung ▸ Vorschau-Thema; mit Entfernen nimmst du es wieder heraus. Die Galerie geht nur online, solange sie geöffnet ist.

[Themen-Galerie](/de/themes/gallery/) · [Ein Thema erstellen](/de/themes/new/)

### Als PDF exportieren oder drucken

Ablage ▸ Als PDF exportieren … sichert ein PDF mit Seitenumbrüchen, und Ablage ▸ Drucken … druckt dieselben Seiten. Mermaid-Diagramme werden eingezeichnet, Code behält seine Hervorhebung, und Seitenumbrüche trennen keine Überschrift von ihrem Abschnitt und zerschneiden keinen kurzen Codeblock und kein Diagramm. Das PDF verwendet immer die hellen Farben des Themes, auch wenn du im Dunkeln gelesen hast.

[PDF-Export](/de/pdf/)

![Ein aus MarsDawn exportiertes PDF, geöffnet in seinem PDF-Viewer mit Seitenminiaturen.](https://marsdawn.southern-light.dev/assets/screens/05-pdf-980.png)

Auf diesem Bildschirmfoto:

1. Mermaid-Diagramme, ins PDF gezeichnet.
2. Code behält seine Hervorhebung.

## Dateien, Tabs und Übersicht

### Fenster und Tabs

Jedes Dokument öffnet in einem eigenen Fenster. Wähle Fenster ▸ Alle Fenster zusammenführen, um geöffnete Fenster als Tabs eines Fensters zu sammeln. Das Sichern läuft automatisch beim Tippen.

[Eine Mac-App](/de/native/)

### Übersicht im Finder

Wähle im Finder eine Markdown-Datei aus und drücke die Leertaste, um sie gerendert zu lesen, samt Diagrammen. Die Übersicht verwendet das Theme, das du in MarsDawn gewählt hast, und folgt dessen Einstellung für das Erscheinungsbild.

[Eine Mac-App](/de/native/) · [Übersicht für Markdown](/de/quicklook/)

### Andere Dateien

MarsDawn öffnet auch reine Textdateien (`.txt`, `.log`, Quellcode) und PDFs. UTF-8-Text öffnet sich bearbeitbar, nur als Quelltext. PDFs öffnen sich in einem Viewer mit Seitenminiaturen, Zoom und Suche.

### Deine Dateien bleiben deine

Es gibt kein Konto, keine Synchronisierung und keine Cloud. Dokumente bleiben dort, wo du sie sicherst, und MarsDawn erhebt keine Daten über dich.

[Deine Texte bleiben auf deinem Mac](/de/yours/)

## Für Agenten und Skripte

### Ein kostenloses Befehlszeilenwerkzeug

Das kostenlose Werkzeug `marsdawn` wird separat mit Homebrew installiert. `marsdawn export` macht aus einer Markdown-Datei ein PDF, gerendert wie die Vorschau von MarsDawn; die App braucht es dafür nicht. Mit `--theme` wählst du ein Theme, als Papierformat A4 oder Letter. `marsdawn open` öffnet Dateien in der App, damit du sie prüfen kannst, auf Wunsch an einer bestimmten Zeile, und braucht die installierte App.

[Befehlszeile](/de/cli/)

### Ausgabe, die ein Skript lesen kann

Mit `--json` liefern beide Befehle ein Ergebnis, das ein Agent oder ein Skript auswerten kann.

[marsdawn für Agenten](/de/cli/agents/)

### Skill und MCP-Server

Eine Agent-Skill-Datei bringt einem Coding-Agenten bei, das von ihm Geschriebene in MarsDawn zu öffnen, damit du es prüfst. Für Clients ohne Shell führt ein separater MCP-Server denselben Export aus.

[Agent-Skill](/de/cli/skill/) · [MCP-Server](/de/cli/mcp/)

### Keine KI drin

MarsDawn hat kein eigenes KI-Modell. Es fasst nicht zusammen und bewertet nicht, was ein Agent geschrieben hat; es hält eine lange, sich ändernde Datei lesbar, damit du lesen kannst.

[Was MarsDawn nicht kann](/de/limits/)

## Siri und Kurzbefehle

Suche in der App „Kurzbefehle“ nach MarsDawn, um drei Aktionen zu finden: Neues Markdown-Dokument (aus einer Vorlage), Notiz zum Eingang hinzufügen und Zuletzt benutztes Dokument öffnen. Notizen landen in `Inbox.md` in dem Ordner, den du unter MarsDawn ▸ Einstellungen … ▸ Notizordner wählst.

[Eine Mac-App](/de/native/)

## Nachdem die Seite gedruckt ist

Eine Besprechung rund um gedruckte Seiten, ein Stift am Rand, eine Papierakte im Ordner.

[MarsDawn-Film (Englisch), 88 Sekunden](https://marsdawn.southern-light.dev/assets/film/marsdawn-themes-film-en-1080p30.mp4)

## Probier es auf deinem Mac aus

MarsDawn ist kostenlos erhältlich. Teste alles 14 Tage lang und schalte es danach einmalig für 4,99 USD frei. Kein Abo, kein Konto. Es braucht macOS 26 oder neuer.

[Jetzt laden und testen](https://apps.apple.com/app/id6812925073)

So funktioniert die Testphase: [Kostenlos testen, einmal bezahlen](/de/pay-once/). Was bewusst fehlt: [Was MarsDawn nicht kann](/de/limits/).

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): Lies und prüfe das Markdown deines Agenten nativ auf dem Mac: geteilte Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
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
- [English](https://marsdawn.southern-light.dev/features/index.md): A native Mac Markdown editor: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings, margin notes and paper records.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/features/index.md): Mac 原生的 Markdown 編輯器：即時預覽、Mermaid 與數學式、主題，輸出和列印的頁面可以拿去開會、用筆加註，或當紙本保存。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/features/index.md): Mac 原生的 Markdown 编辑器：实时预览、Mermaid 与数学公式、主题，导出和打印的页面可以拿去开会、用笔批注，或当纸质存档。
- [日本語](https://marsdawn.southern-light.dev/ja/features/index.md): Mac ネイティブの Markdown エディタ：リアルタイムプレビュー、Mermaid と数式、テーマに加え、会議や書き込み、紙での保管に使える PDF とプリントのページ。
- [Français](https://marsdawn.southern-light.dev/fr/features/index.md): Éditeur Markdown natif pour Mac : aperçu en direct, Mermaid, formules, thèmes et pages PDF ou imprimées pour réunions, notes en marge et dossiers papier.
- [Español](https://marsdawn.southern-light.dev/es/features/index.md): Editor de Markdown nativo para Mac: vista previa, Mermaid, fórmulas, temas y páginas en PDF o impresas para reuniones, notas al margen y registros en papel.
- [한국어](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
