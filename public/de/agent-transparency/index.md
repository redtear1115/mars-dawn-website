# Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?

Im Dezember 2024 veröffentlichte Anthropic „Building Effective Agents“, einen Leitfaden für Leute, die KI-Agenten bauen. Seine Zusammenfassung nennt drei Prinzipien, und eines davon ist Transparenz. In diesem Beitrag geht es um das andere Ende dieses Prinzips: Sobald ein Agent seine Schritte offenlegt, muss sie jemand lesen.

**Transparenz ist etwas, das der Agent tut. Lesen ist etwas, das du tust. Anthropic bittet die Entwickler, die Planungsschritte eines Agenten zu zeigen; für die meisten, die einen Coding-Agenten steuern, kommen diese Schritte als Markdown-Datei an, die jemand im richtigen Moment lesen muss.**

## Was der Leitfaden sagt

Erik S. und Barry Zhang fassen ihren Rat so zusammen:

> „Bei der Umsetzung von Agenten versuchen wir, drei Grundprinzipien zu folgen: Halte das Design deines Agenten einfach. Setze auf Transparenz, indem du die Planungsschritte des Agenten ausdrücklich zeigst. Gestalte die Schnittstelle zwischen Agent und Computer (ACI) sorgfältig, mit gründlicher Werkzeugdokumentation und gründlichen Tests.“

Das sind Entwurfsprinzipien für Leute, die Agenten bauen, keine Anleitung für die Person, die einen benutzt. Das Prinzip verlangt, dass die Schritte gezeigt werden. Es sagt nicht, wer sie liest.

Derselbe Beitrag beschreibt, was ein Agent tut, sobald er eine Aufgabe hat: „Sobald die Aufgabe klar ist, planen und handeln Agenten selbstständig und kehren möglicherweise zum Menschen zurück, um weitere Informationen oder eine Einschätzung einzuholen.“ Und: „Agenten können dann an Checkpoints oder bei Hindernissen für menschliches Feedback pausieren.“ Achte auf die Wörter *möglicherweise* und *können*. Checkpoints werden als etwas beschrieben, das ein Agent haben kann, nicht haben muss.

## Das meiste Prüfen machst nicht du

Das lässt sich leicht übertreiben, darum hier, was der Leitfaden tatsächlich an erste Stelle setzt. Der Agent prüft sich selbst an der Welt: „Während der Ausführung ist es entscheidend, dass die Agenten bei jedem Schritt ‚Ground Truth‘ aus der Umgebung erhalten (etwa Ergebnisse von Werkzeugaufrufen oder Codeausführung), um ihren Fortschritt zu beurteilen.“ In diesem Satz meint Ground Truth Testergebnisse und Werkzeugausgaben. Es meint keinen Menschen.

Der Leitfaden ist auch beim Risiko direkt: „Die autonome Natur von Agenten bedeutet höhere Kosten und die Gefahr sich aufschaukelnder Fehler.“ Seine Antwort sind ausgiebige Tests in abgeschotteten Umgebungen, mit Schutzvorkehrungen. Er sagt nicht „lies sorgfältiger“.

Ein Mensch kommt später doch ins Spiel, im Anhang über Coding-Agenten: „Während automatisierte Tests helfen, die Funktion zu prüfen, bleibt menschliche Prüfung entscheidend, um sicherzustellen, dass Lösungen zu den umfassenderen Systemanforderungen passen.“ Dieser Satz handelt von Code. Die Lücke, auf die er zeigt, kennt man aber von jedem Agenten: Ein Test kann dir sagen, dass etwas funktioniert, nicht, dass es das ist, was du gemeint hast.

## Wo die Schritte landen

**Ab hier ist das unsere Lesart, nicht die von Anthropic.**

Wenn du täglich mit einem Coding-Agenten arbeitest, tauchen seine Planungsschritte meist nicht in einem Dashboard auf. Sie tauchen als Dateien auf: `plan.md`, eine Aufgabenliste mit Kontrollkästchen, eine Fortschrittsdatei, die der Agent ständig umschreibt, eine Zusammenfassung am Ende. Transparenz heißt von deiner Seite aus: mehr zu lesen.

Die Schritte zu zeigen ist die Hälfte des Agenten. Die andere Hälfte ist ein Mensch, der sie liest, wenn es darauf ankommt: bevor die Migration läuft, bevor der Branch gemergt wird, bevor „fertig“ akzeptiert wird. Ein Agent, der alles in einer Datei mit 600 Zeilen offenlegt, die niemand öffnet, ist auf dem Papier transparent und in der Praxis unbeaufsichtigt.

Harrison Chase machte 2024 einen verwandten Punkt, als er darüber schrieb, wie Agenten-Frameworks funktionieren sollten, nicht über Dokumente: „Du wirst beobachten können wollen, was im Inneren vor sich geht, da die genauen Schritte vorher womöglich nicht bekannt sind.“ Er sprach über Werkzeuge für die Leute, die Agenten bauen. Wenn du derjenige bist, der den Agenten steuert, ist die schlichte Datei, die er ständig schreibt, oft der Teil, den du beobachten kannst.

Keiner dieser Autoren erwähnt MarsDawn, und keiner empfiehlt es oder ein anderes Markdown-Werkzeug.

## Warum dieses Lesen schwerer ist, als es aussieht

Die Datei ist lang, und das Wichtige steht selten oben. Das Diagramm, das die Änderung erklärt, ist Mermaid-Quelltext, kein Bild (wie du es gezeichnet siehst, steht unter [Eine Markdown-Datei auf dem Mac ansehen](/de/view-markdown-on-mac/)). Der Agent schreibt die Datei vielleicht um, während du bei der Hälfte bist. Oft gibt es mehr als eine Datei, manchmal auf verschiedenen Branches oder Worktrees. Und wenn du ein Problem entdeckst, lässt „der Cache-Teil sieht komisch aus“ den Agenten raten. Die längere Version davon steht unter [Lesen, was dein Agent zurückgibt](/de/reading-agent-output/).

## Wo MarsDawn passt und wo nicht

MarsDawn ist eine Mac-App für dieses Lesen. Es macht einen Agenten nicht transparenter, und es steckt kein KI-Modell darin: Es fasst den Plan nicht zusammen und sagt dir nicht, ob er stimmt. Was es tut:

- **Lange Dateien:** Darstellung ▸ Seitenleiste einblenden (⌃⌘S) öffnet den Tab Gliederung, der die Überschriften listet. Klick auf eine, um dorthin zu springen.
- **Diagramme und Formeln:** Quelltext und gerenderte Seite stehen nebeneinander (⌘2) und scrollen gemeinsam, mit gezeichnetem Mermaid und KaTeX. Ist ein Diagramm fehlerhaft, zeigt die Vorschau seinen Quelltext mit dem Fehler darunter.
- **Umgeschrieben, während du liest:** Wenn der Agent die Datei umschreibt, lädt MarsDawn sie neu und behält deine Stelle, solange du keine eigenen ungesicherten Änderungen hast.
- **Mehrere Dateien:** Öffne den Ordner des Agenten mit Ablage ▸ Ordner öffnen … (⇧⌘O). Neue Dateien erscheinen innerhalb etwa einer Sekunde im Tab Dateien, und bei einem Git-Checkout nennt die Kopfzeile den Branch oder Worktree.
- **Auf eine Zeile zeigen:** Bearbeiten ▸ Verweis kopieren (⌥⌘C) kopiert deine Stelle als `docs/plan.md:42`, und Für KI kopieren (⌃⌥⌘C) fügt den ausgewählten Text darunter ein, bereit zum Einfügen in den Chat mit dem Agenten.

Lesen musst du trotzdem selbst. MarsDawn hält eine lange, sich ändernde Datei lesbar, während du es tust.

## Ausprobieren

MarsDawn gibt es im [Mac App Store](https://apps.apple.com/app/id6812925073). Dazu kommt das kostenlose Befehlszeilenwerkzeug `marsdawn`:

```
brew install redtear1115/tap/marsdawn
```

Es exportiert Markdown ohne die App als PDF.

[Befehlszeile](/de/cli/) · Vor dem Kauf wissen: [Was MarsDawn nicht kann](/de/limits/)

## Weiter

- Warum Agentenausgaben schwer zu lesen sind, mit einer Checkliste: [Lesen, was dein Agent zurückgibt](/de/reading-agent-output/).
- Die Checkliste Schritt für Schritt mit einem Beispiel: [Einen Agentenplan in fünf Minuten prüfen](/de/reviewing-agent-plans/).
- Welche Dokumente verschiedene Arten von Agenten dir übergeben: [Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt](/de/agent-design-patterns/).
- Die kurze Begründung, KI-Ausgaben überhaupt zu lesen: [Warum KI-Ausgaben immer noch menschliche Leser brauchen](/de/reviewing-ai-output/).

## Quellen

- Erik S. und Barry Zhang, „Building Effective Agents“, Anthropic, 19. Dezember 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (zitiert nach der am 26.09.2026 online verfügbaren Fassung; der Beitrag weist inzwischen darauf hin, dass sich vieles an den beschriebenen Werkzeugen seit Dezember 2024 geändert hat).
- Harrison Chase, „What is an agent?“, LangChain, 28. Juni 2024, archivierte Kopie: [http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/](http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/) (unter der ursprünglichen Adresse steht inzwischen ein anderer Artikel von 2026).

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): MarsDawn ist ein nativer Markdown-Editor für Mac: Live-Vorschau neben dem Quelltext, Mermaid, KaTeX, Übersicht, PDF-Export. Gratis testen, einmalig 4,99 USD.
- [Deine Texte bleiben auf deinem Mac](https://marsdawn.southern-light.dev/de/yours/index.md): MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.
- [Kostenlos testen, einmal bezahlen](https://marsdawn.southern-light.dev/de/pay-once/index.md): MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.
- [PDF-Export](https://marsdawn.southern-light.dev/de/pdf/index.md): Exportiere Markdown auf deinem Mac als PDF oder drucke es, mit Mermaid-Diagrammen und hervorgehobenem Code. Seitenumbrüche vermeiden es, kurze Codeblöcke und Tabellen zu teilen.
- [Eine Mac-App](https://marsdawn.southern-light.dev/de/native/index.md): Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.
- [Was MarsDawn nicht kann](https://marsdawn.southern-light.dev/de/limits/index.md): Keine Synchronisierung, keine App für iPhone oder iPad, keine Plug-ins, keine Konten. Vier integrierte Themen. Gut zu wissen, bevor du kaufst.
- [Support](https://marsdawn.southern-light.dev/de/support/index.md): Hilfe zu MarsDawn, dem Markdown-Editor für macOS.
- [Datenschutzrichtlinie](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [Markdown auf dem Mac ansehen](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): Eine .md-Datei ist reiner Text mit Formatierungszeichen. So liest du sie auf dem Mac gerendert: heute als PDF mit dem kostenlosen Befehlszeilenwerkzeug marsdawn und in der MarsDawn-App aus dem Mac App Store.
- [Quick Look für Markdown](https://marsdawn.southern-light.dev/de/quicklook/index.md): Mit MarsDawn zeigt die Übersicht Markdown im Finder per Leertaste gerendert: Mermaid, KaTeX, hervorgehobener Code. Sie funktioniert auch nach dem Test weiter.
- [Markdown zu PDF](https://marsdawn.southern-light.dev/de/markdown-to-pdf/index.md): Wandle Markdown auf dem Mac mit dem kostenlosen Befehlszeilenwerkzeug marsdawn in ein PDF um. Mit Homebrew installieren, einen Befehl ausführen: Tabellen, Mathematik, Mermaid und Code.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer zeigt Markdown nur zum Lesen an, für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben, kostenlos testen, dann einmalig 4,99 USD im Mac App Store.
- [Befehlszeile](https://marsdawn.southern-light.dev/de/cli/index.md): Das kostenlose Befehlszeilenprogramm marsdawn für den Mac: Markdown aus einer Shell, einem Skript oder einem LLM-Agenten als PDF exportieren, mit JSON-Ausgabe. Installation mit Homebrew.
- [marsdawn für Agenten](https://marsdawn.southern-light.dev/de/cli/agents/index.md): Eine Referenz für KI-Agenten und Skripte, die marsdawn aufrufen, um Markdown in PDF umzuwandeln: Befehle, JSON-Ausgabe, Schemas, Exit-Codes und Voraussetzungen.
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
- [English](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-transparency/index.md): Anthropic 談打造 agent 的指南要求透明：把規劃步驟攤開來。它說了什麼、沒說什麼，以及為什麼這些步驟最後多半變成一份要有人讀的 Markdown。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-transparency/index.md): Anthropic 谈打造 agent 的指南要求透明：把规划步骤摊开来。它说了什么、没说什么，以及为什么这些步骤最后多半变成一份要有人读的 Markdown。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-transparency/index.md): Anthropic のエージェント構築ガイドは透明性を求めている：計画のステップを示せと。そこに何が書いてあり、何が書いてないか、そしてそのステップがなぜ結局読む必要のある Markdown ファイルになるのか。
- [Français](https://marsdawn.southern-light.dev/fr/agent-transparency/index.md): Le guide d’Anthropic pour construire des agents demande de la transparence : montrer les étapes de planification. Ce qu’il dit, ce qu’il ne dit pas, et pourquoi ces étapes finissent généralement dans un fichier Markdown que quelqu’un doit lire.
- [Español](https://marsdawn.southern-light.dev/es/agent-transparency/index.md): La guía de Anthropic para construir agentes pide transparencia: mostrar los pasos de planificación. Qué dice, qué no dice y por qué esos pasos suelen terminar en un archivo Markdown que alguien tiene que leer.
- [한국어](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
