# Die Arbeit deines Agenten kommt als Markdown-Datei zurück.

Du bittest einen Coding-Agenten, eine Migration zu planen, eine Spezifikation zu schreiben oder einem Bug nachzugehen. Er arbeitet eine Weile allein und gibt dir dann eine Datei: `plan.md`, `SPEC.md`, einen Fortschrittsbericht, eine Recherchezusammenfassung. Soweit du die Arbeit prüfen kannst, ist diese Datei die Arbeit.

**Ob der Agent es richtig gemacht hat, erfährst du, indem du liest, was er zurückgibt. MarsDawn ist eine Mac-App für dieses Lesen.**

## Was Leute sagen, die Agenten bauen

Zitiert wie geschrieben; unsere Lesart folgt danach.

- Anthropics „Building Effective Agents“ (Erik S. und Barry Zhang, Dezember 2024) nennt drei Grundprinzipien für den Bau von Agenten. Eines lautet: „Setze auf Transparenz, indem du die Planungsschritte des Agenten ausdrücklich zeigst.“ Es richtet sich an Leute, die Agenten bauen. Von deiner Seite aus ist diese Transparenz der Plan, den du am Ende liest.
- Derselbe Beitrag: „Agenten können dann an Checkpoints oder bei Hindernissen für menschliches Feedback pausieren.“ Achte auf das Verb: *können*.
- Chip Huyen in „Agents“ (Januar 2025) darüber, warum Planung von Ausführung getrennt sein sollte: „Ohne Aufsicht kann ein Agent diese Schritte stundenlang ausführen und Zeit und Geld für API-Aufrufe verschwenden, bevor du merkst, dass er nicht vorankommt.“ Sie beschreibt auch einen Fehler, bei dem „der Agent überzeugt ist, eine Aufgabe erledigt zu haben, obwohl er es nicht hat“. Soll er 50 Personen auf 30 Hotelzimmer verteilen, bringt er 40 unter und besteht darauf, fertig zu sein.
- Andrew Ng über das Entwurfsmuster Planung in The Batch (April 2024): „Einerseits ist Planung eine sehr mächtige Fähigkeit; andererseits führt sie zu weniger vorhersehbaren Ergebnissen.“ Das ist eine Aussage über Vorhersehbarkeit, kein Aufruf zu menschlicher Prüfung, und er erwartet, dass Planung schnell besser wird.

**Unsere Schlussfolgerung, nicht ihre:** Wenn ein Agent seinen Plan offenlegt und an Checkpoints anhält, liest jemand diesen Plan am Checkpoint, und meistens bist das du. Wenn ein Agent glauben kann, fertig zu sein, obwohl er es nicht ist, braucht auch sein Fertig-Bericht einen Leser. Keiner dieser Autoren erwähnt MarsDawn oder empfiehlt es oder ein anderes Markdown-Werkzeug.

## Warum das Lesen schwerer ist, als es aussieht

Die Datei ist lang, und der wichtige Teil steht selten oben. Sie enthält Mermaid-Diagramme und Formeln, die als Quelltext schwer zu verfolgen sind. Der Agent schreibt sie vielleicht noch um, während du bei der Hälfte bist. Oft ist sie eine von mehreren Dateien, manchmal über Branches oder Worktrees verteilt. Und wenn du ein Problem findest, lässt „der Cache-Teil sieht komisch aus“ den Agenten raten; „`docs/plan.md:42` löscht die alte Tabelle, bevor das Backfill fertig ist“ nicht.

## Wo MarsDawn hilft

- **Lange Dateien:** Der Tab Gliederung in der Seitenleiste (⌃⌘S) listet die Überschriften. Klick auf eine, und beide Bereiche springen dorthin.
- **Diagramme und Formeln:** Mermaid und KaTeX werden in der Vorschau neben dem Quelltext gezeichnet (⌘2), und beide Bereiche scrollen gemeinsam.
- **Umgeschrieben, während du liest:** Wenn der Agent die Datei umschreibt, lädt MarsDawn sie neu und behält deine Stelle, solange du keine eigenen ungesicherten Änderungen hast.
- **Mehrere Dateien:** Öffne den Ordner des Agenten mit Ablage ▸ Ordner öffnen … (⇧⌘O). Neue Dateien erscheinen innerhalb etwa einer Sekunde im Tab Dateien, und bei einem Git-Checkout nennt die Kopfzeile den Branch oder Worktree.
- **Genaues Feedback:** Bearbeiten ▸ Verweis kopieren (⌥⌘C) kopiert deine Stelle als `docs/plan.md:42`. Für KI kopieren (⌃⌥⌘C) fügt den ausgewählten Text darunter ein. Füge beides in den Chat mit dem Agenten ein.

Zwei weitere für den Ablauf: Ein Agent kann `marsdawn open plan.md:42` ausführen, um die Datei in MarsDawn bei Zeile 42 zu öffnen, der Zeile, die du zuerst sehen sollst, und eine geprüfte Datei lässt sich aus der App oder mit dem kostenlosen Befehl `marsdawn export` als PDF exportieren.

In MarsDawn steckt kein KI-Modell. Es fasst den Plan nicht zusammen, bewertet ihn nicht und sagt dir nicht, was falsch ist. Du liest; es hält eine lange, sich ändernde Datei lesbar und lässt dich auf die genaue Zeile zeigen.

## Einen Agentenplan in fünf Minuten prüfen

Das funktioniert in jedem Editor.

1. Lies nur die Überschriften. Passt die Gliederung zu dem, worum du gebeten hast? Ein fehlender Abschnitt bedeutet meist fehlende Arbeit.
2. Finde jede Stelle, die sagt, dass etwas erledigt, bestanden oder geprüft ist, und prüfe eine selbst: Öffne die Datei, führe den Test aus, zähle die Zeilen.
3. Achte auf Schritte, die sich nicht rückgängig machen lassen: Daten löschen, Migrationen, Force-Pushes, alles, was sendet, bezahlt oder veröffentlicht. Die warten auf dein ausdrückliches Ja.
4. Lies die Diagramme gerendert und prüfe jeden Pfeil gegen den Text.
5. Liste die Dateien und Systeme auf, die der Plan berührt. Frag nach allem, worum du nicht gebeten hast, bevor es läuft.
6. Schreib Feedback als Stelle, Problem, Lösung: „`plan.md:88`: Das Backfill läuft nach dem Löschen. Tausche die Schritte 4 und 5.“ Ein Problem pro Zeile.

Wenig Zeit? Mach Schritt 2. Dort fliegt ein Agent auf, der glaubt, fertig zu sein. Die ausführliche Version mit einem durchgespielten Beispiel: [Einen Agentenplan in fünf Minuten prüfen](/de/reviewing-agent-plans/).

## Ausprobieren

MarsDawn gibt es im [Mac App Store](https://apps.apple.com/app/id6812925073). Dazu kommt das kostenlose Befehlszeilenwerkzeug `marsdawn`:

```
brew install redtear1115/tap/marsdawn
```

Es exportiert Markdown ohne die App als PDF, und mit `marsdawn open` kann dein Agent Dateien für dich in MarsDawn öffnen.

[Befehlszeile](/de/cli/) · [marsdawn für Agenten](/de/cli/agents/) · Vor dem Kauf wissen: [Was MarsDawn nicht kann](/de/limits/)

## Weiter

- Die kurze Begründung, KI-Ausgaben überhaupt zu lesen: [Warum KI-Ausgaben immer noch menschliche Leser brauchen](/de/reviewing-ai-output/).
- Den Kontext des Agenten klein halten, während du prüfst: [Token-sparsames Prüfen](/de/token-efficient-review/).
- Warum Agenten ihre Pläne überhaupt offenlegen: [Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?](/de/agent-transparency/)
- Die Checkliste oben, Schritt für Schritt mit einem Beispiel: [Einen Agentenplan in fünf Minuten prüfen](/de/reviewing-agent-plans/).
- Welche Dokumente verschiedene Arten von Agenten dir übergeben: [Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt](/de/agent-design-patterns/).

## Quellen

- Erik S. und Barry Zhang, „Building Effective Agents“, Anthropic, 19. Dezember 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (zitiert nach der am 26.09.2026 online verfügbaren Fassung; der Beitrag weist inzwischen darauf hin, dass sich vieles an den beschriebenen Werkzeugen seit Dezember 2024 geändert hat).
- Chip Huyen, „Agents“, 7. Januar 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Andrew Ng, „Agentic Design Patterns Part 4, Planning“, The Batch, 10. April 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)

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
- [English](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：計畫、規格、進度報告。做 agent 的人怎麼談檢查點和失敗、這些產出為什麼難讀，以及五分鐘審完一份計畫的檢查清單。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-agent-output/index.md): AI agent 把工作成果交成 Markdown：计划、规格、进度报告。做 agent 的人怎么谈检查点和失败、这些产出为什么难读，以及五分钟审完一份计划的检查清单。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-agent-output/index.md): AI エージェントは仕事の成果を Markdown で返します：計画、仕様書、進捗報告。エージェントを作る人たちがチェックポイントや失敗について何を言うか、その出力がなぜ読みづらいのか、そして計画を 5 分でレビューするチェックリスト。
- [Français](https://marsdawn.southern-light.dev/fr/reading-agent-output/index.md): Les agents IA rendent leur travail en Markdown : plans, spécifications, rapports d’avancement. Ce que disent ceux qui construisent des agents sur les points de contrôle et les échecs, pourquoi ces fichiers sont difficiles à lire, et une liste de vérification pour relire un plan en cinq minutes.
- [Español](https://marsdawn.southern-light.dev/es/reading-agent-output/index.md): Los agentes de IA entregan su trabajo en Markdown: planes, especificaciones, informes de avance. Qué dicen quienes construyen agentes sobre los puntos de control y los fallos, por qué ese resultado cuesta leerlo y una lista para revisar un plan en cinco minutos.
- [한국어](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
