# Änderungsprotokoll

Was sich in jeder Version der MarsDawn-App aus dem Mac App Store und des kostenlosen Befehlszeilenprogramms marsdawn geändert hat. Bei der App ist das Datum der Tag, an dem die Version im Mac App Store erschien.

Was als Nächstes kommt, steht in der [Roadmap](/de/roadmap/).

## MarsDawn-App

### MarsDawn 1.1.1

15. Oktober 2026

- Auf Deutsch, Japanisch, Spanisch und Französisch zeigt Einstellungen > Erscheinungsbild > „Weitere Themes laden …“ den Szenario-Filter jetzt als Einblendmenü mit der Beschriftung „Szenario“, damit die fünf Optionen Platz haben. Auf Englisch, Koreanisch und Chinesisch bleibt es beim segmentierten Steuerelement.
- Wenn ein Theme aus der Galerie zurückgezogen wird, nennt der Hinweis in „Weitere Themes laden …“ jetzt den Namen des Themes (zum Beispiel Inkwell Ivory) statt seiner internen ID.
- Ausklappbare details-Abschnitte im GitHub-Stil beginnen in der Vorschau und in der Übersicht jetzt eingeklappt mit sichtbarer Zusammenfassung und öffnen sich per Klick. Der PDF-Export druckt weiterhin den Inhalt aller Abschnitte.
- Dokumente, die du aus dem Finder, dem Dock, über Ablage > „Öffnen …“ oder mit dem Befehl marsdawn open öffnest, öffnen sich jetzt als Tabs im vordersten Fenster, ebenso neue Dokumente. Um das bisherige Verhalten beizubehalten, wähle „Systemeinstellung folgen“ unter Einstellungen > Erscheinungsbild.

Frühere Versionen sind nur auf Englisch beschrieben: [zum englischen Änderungsprotokoll](/changelog/).

## Befehlszeilenprogramm marsdawn

Versionen vor 0.5.1 sind nicht aufgeführt.

### marsdawn 0.7.2

20. Oktober 2026. Das Handbuch-Layout, Hinweisboxen und japanische Schriften.

- Der Wert für `--layout` heißt jetzt `handbook`, wie das Layout „Handbuch“ der App: `marsdawn export --layout handbook`. `--layout manual` funktioniert weiterhin, ist aber veraltet.
- Hinweisboxen werden dargestellt, in der Vorschau und in exportierten PDFs: GitHub-Alerts wie `> [!NOTE]` und `> [!WARNING]` und HackMD-Container wie `:::info` und `:::warning`. `:::spoiler` ergibt einen ausklappbaren Abschnitt.
- Ein japanisches Dokument verwendet japanische Schriften für Kana und Kanji. marsdawn erkennt die Sprache an `lang: ja` im Front Matter oder am Kana-Anteil des Textes.
- Nach einem erfolgreichen `export` oder `open` im Terminal zeigt marsdawn einmalig einen Tipp auf stderr, wenn der Agent-Skill fehlt oder veraltet ist. Die Ausgabe auf stdout und mit `--json` ändert sich nicht. Mit `MARSDAWN_NO_SKILL_HINT=1` schaltest du den Tipp ab.

### marsdawn 0.7.1

20. Oktober 2026. Ein Handbuch-Layout und eine Größengrenze.

- `marsdawn export --layout manual` druckt ein Handbuch: breitere Ränder, 25 mm Bundsteg und jede Überschrift der obersten Ebene auf einer neuen Seite, dazu ein Deckblatt aus title, subtitle, version, date, author und logo des Front Matter, ein Inhaltsverzeichnis der Überschriften der Ebenen 1 und 2 mit Seitenzahlen, Seitenzahlen als `n / N` und PDF-Lesezeichen. `--toc-title` legt die Überschrift des Inhaltsverzeichnisses fest. Standard bleibt `--layout document`.
- `<!--BREAK-->` allein in einer Zeile beginnt eine neue Seite, in beiden Layouts.
- `marsdawn export` lehnt Dateien über 16 MiB ab: Es endet mit Exit-Code 5, meldet mit `--json` `input_too_large` und schreibt nichts.
- Die Vorschauseite entfernt script- und noscript-Elemente; ein neu gezeichnetes Mermaid-Diagramm behält sein eigenes SVG.
- Ein Zeichenverweis, der zu `=` oder `^` decodiert wird, etwa `&#61;`, bildet kein Paar mehr mit einer HackMD-Markierung.

### marsdawn 0.7.0

18. Oktober 2026. HackMD-Markdown, Zeilenumbrüche und Grenzen für sehr große Dokumente.

- HackMDs Inline-Markierungen werden dargestellt: `==mark==`, `^sup^` und `~sub~`. Ein Absatz, der nur aus `[TOC]` besteht, wird zum Inhaltsverzeichnis, HackMDs Bildgrößen werden übernommen, Embed-Tags werden zu einfachen https-Links, und die Sprache eines Codeblocks wird vor HackMD-Optionen wie `js=` gelesen.
- `marsdawn export --breaks` macht wie HackMD jeden Zeilenumbruch in einem Absatz zu einem Zeilenumbruch. Ohne die Option fällt ein Zeilenumbruch zwischen zwei chinesischen oder japanischen Zeichen weg, sodass sich die Zeilen wie ein Satz lesen. Koreanisch behält sein Leerzeichen, weil es Wörter durch Leerzeichen trennt.
- Sehr große Dokumente haben Grenzen, in der Vorschau und in exportierten PDFs. Ein Codeblock über 128K Zeichen wird nicht hervorgehoben, und nach insgesamt 256K Zeichen endet die Hervorhebung. Pro Aktualisierung werden bis zu 100 Mermaid-Diagramme und 1.000 Formeln dargestellt; die übrigen Diagramme zeigen ihren Quelltext mit einem Hinweis, auch wenn sie schon einmal gezeichnet waren.
- In einem Sequenzdiagramm bekommt eine Nachrichtenbeschriftung in einem `rect`-Block einen Rand in der Farbe des Blocks.
- Ein Fußnotenverweis direkt über einer Tabelle bringt `marsdawn export` nicht mehr zum Absturz.
- `marsdawn skill --install` endet mit Exit-Code 7 (`skill_install_failed`), wenn es den Ordner nicht anlegen oder die Datei nicht schreiben kann, und lässt eine vorhandene SKILL.md unverändert.

### marsdawn 0.6.4

13. Oktober 2026. Ausklappbare `<details>`-Blöcke.

- Ein `<details>`-Block im GitHub-Stil mit Leerzeilen darin wird als ein ausklappbares Element dargestellt, in der Vorschau und in exportierten PDFs. Bisher zerfiel er an der ersten Leerzeile.
- Der PDF-Export öffnet vor dem Drucken jeden `<details>`-Block, außer dem Front Matter.
- Die Vorschau behält ihre Scrollposition, wenn du einen `<details>`-Block öffnest oder schließt.

### marsdawn 0.6.3

6. Oktober 2026. MarsDawn ist im Mac App Store.

- Wenn die App nicht installiert ist, verweist `marsdawn open` auf MarsDawn im Mac App Store.
- Das README und der Agent-Skill erklären `marsdawn open .` und `--folder`: MarsDawn 1.0.0 zeigt den Ordner in der Seitenleiste des Fensters.

### marsdawn 0.6.1

29. September 2026. Themen prüfen.

- `marsdawn theme validate` prüft eine `theme.json` nach den Regeln der App. Es endet mit Exit-Code 0, wenn das Thema gültig ist, und mit 1, wenn nicht, und listet jedes Problem auf. `--require-complete` verlangt zusätzlich die Syntax- und Diagrammfarben.
- `marsdawn theme css` gibt das CSS aus, das die Vorschau für ein gültiges Thema verwendet, und `marsdawn theme preview` rendert damit ein Beispieldokument als PNG, hell oder dunkel.

### marsdawn 0.5.4

26. September 2026. Mermaid-Korrekturen, Zeilenangaben bei Diagrammfehlern und die Installation des Skills.

- In einem Sequenzdiagramm bleibt eine Nachrichtenbeschriftung, die die Lebenslinien anderer Teilnehmer kreuzt, lesbar, in der Vorschau und in exportierten PDFs.
- `marsdawn export` kommt mit Dokumenten voller Mermaid-Diagramme zurecht. Eines mit 50 Diagrammen, das früher mit Exit-Code 5 scheiterte, wird jetzt exportiert.
- `marsdawn export --json` ergänzt `diagramErrorDetails` mit Zeilennummern für jeden Diagrammfehler: wo das Diagramm in deinem Dokument beginnt und, wenn Mermaid eine nennt, die Zeile des Fehlers selbst.
- `marsdawn skill --install` installiert den Agent-Skill für Claude Code unter `~/.claude/skills/marsdawn/SKILL.md` oder mit `--dir` in einem anderen Ordner. Eine identische Datei lässt es unangetastet, eine abweichende ersetzt es nur mit `--force`. Andernfalls endet es mit Exit-Code 64 (`skill_differs`) und ändert nichts.

### marsdawn 0.5.3

25. September 2026. Ordnerstatus, vollständige Mermaid-Fehler und kleinere Korrekturen.

- `marsdawn open --folder` kann melden, was mit dem Ordner passiert ist. Bei einer App, die Rückmeldung gibt, wartet es bis zu `--wait` Sekunden (standardmäßig 2), und `--json` liefert einen Status wie `attached` oder `needsUser`.
- Ein Mermaid-Diagramm, das sich nicht parsen lässt, zeigt die vollständige Fehlermeldung von Mermaid statt nur ihrer ersten Zeile, mit der Zeilennummer vom Anfang deines Dokuments aus gezählt.
- Die Suche nach dem Ende eines Front-Matter-Blocks hört nach 1.000 Zeilen auf, sodass ein nicht geschlossener Block nicht mehr bedeutet, den Rest eines großen Dokuments zu durchsuchen.
- Eine App kann dem Rücklink einer Fußnote für PDF-Export und Drucken eine übersetzte Beschriftung geben. Die Beschriftung wird nicht auf die Seite gedruckt, und `marsdawn export` behält die englische.
- Das mitgelieferte highlight.js ist jetzt nach Version, Quelle und SHA-256 festgelegt, wie KaTeX und Mermaid.

### marsdawn 0.5.2

24. September 2026. Fußnoten, Kontrast und Ordner.

- Fußnoten werden in exportierten PDFs dargestellt: nummerierte Verweise, die Anmerkungen nach dem Haupttext.
- Jedes Thema erfüllt den WCAG-AA-Kontrast, hell und dunkel. Klassisch ist jetzt schwarz-weiß.
- `marsdawn skill` gibt den Agent-Skill aus, der zum installierten marsdawn passt.
- `marsdawn open` endet mit Exit-Code 6 (`app_cannot_open_folders`), wenn das gefundene MarsDawn keinen Ordner anzeigen kann, statt Erfolg zu melden.
- Die Platzhalter, die in exportierte Seiten gezeichnet werden, gibt es jetzt auch auf Deutsch, Französisch, Spanisch und Koreanisch.
- Ein Bildplatzhalter zeigt hinter einem sehr langen relativen Pfad nicht mehr den absoluten Pfad.
- `MARSDAWN_APP_PATH` wird nur verwendet, wenn es auf eine MarsDawn-App zeigt.

### marsdawn 0.5.1

19. September 2026. PDF-Export und das Öffnen einer Datei über die Befehlszeile.

- Die Textebene eines exportierten PDFs ist für Chinesisch, Japanisch und Koreanisch repariert.
- `marsdawn open --background` öffnet eine Datei, ohne MarsDawn in den Vordergrund zu holen.
- `marsdawn open` kann ein Ordner übergeben werden, und MarsDawn zeigt ihn in der Seitenleiste des Fensters (ab MarsDawn 1.0.0).

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): Lies und prüfe das Markdown deines Agenten nativ auf dem Mac: geteilte Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Funktionen](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
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
- [English](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/changelog/index.md): MarsDawn App 與免費的 marsdawn 命令列工具，每個版本改了什麼。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/changelog/index.md): MarsDawn App 与免费的 marsdawn 命令行工具，每个版本改了什么。
- [日本語](https://marsdawn.southern-light.dev/ja/changelog/index.md): MarsDawn アプリと無料の marsdawn コマンドラインツールの、バージョンごとの変更点です。
- [Français](https://marsdawn.southern-light.dev/fr/changelog/index.md): Ce qui a changé dans chaque version de l’app MarsDawn et de l’outil en ligne de commande gratuit marsdawn.
- [Español](https://marsdawn.southern-light.dev/es/changelog/index.md): Qué cambió en cada versión de la app MarsDawn y de la herramienta de línea de comandos gratuita marsdawn.
- [한국어](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
