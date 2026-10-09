# Andrew Ng ordnet seine eigenen Entwurfsmuster nach Vorhersagbarkeit

**Über fünf Briefe in The Batch Anfang 2024 beschrieb Andrew Ng vier agentische Entwurfsmuster — Reflexion, Werkzeugnutzung, Planung und Multi-Agenten-Zusammenarbeit — und sagte seinen Lesern ungewöhnlich klar, welche er für verlässlicher hält und welche er schwer vorhersagen kann.**

## Was die Briefe argumentieren

`/agent-design-patterns/` behandelt schon, was jedes der vier Muster ist, welche Dokumente jedes typischerweise zum Lesen übergibt (unsere Folgerung), und Ngs eigenes Urteil zur Planung aus Teil 4: „while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do.“ Diese Notiz ergänzt dieselbe Rangfolge aus den zwei Briefen, die jene Seite auslässt: Teil 3, eine Woche vor Teil 4, wo er die Rangfolge im Voraus nennt, und Teil 5, wo er sie auf das Muster ausdehnt, das Teil 4 nicht nennt — Multi-Agenten-Zusammenarbeit. Zur Einführung von Werkzeugnutzung in Teil 3 schreibt er:

> “In future letters, I’ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable — albeit very exciting — technologies.”

Zwei Wochen später, am Ende der Reihe mit Multi-Agenten-Zusammenarbeit, bestätigt er dieselbe Rangfolge von der anderen Seite:

> “Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.”

Das sagt er darüber, wie gut jedes Muster die Ergebnisse seiner Anwendungen verbessert, nicht darüber, wie sorgfältig eine Person ihre Ausgabe prüfen sollte — nichts in dieser Reihe fordert menschliche Prüfung, und nichts erwähnt MarsDawn oder empfiehlt ein Markdown-Werkzeug.

## Unsere Lesart, nicht die von Ng

Ngs Rangfolge gilt Ausgabequalität und Vorhersagbarkeit vom Stuhl des Bauenden aus, aber sie deckt sich grob damit, wie viel Prüfung die Papierspur jedes Musters von deinem Stuhl aus verdient. Reflexion und Werkzeugnutzung, die beiden, die er für verlässlicher hält, übergeben dir typischerweise etwas, das schon getane Arbeit beschreibt — einen überarbeiteten Entwurf, einen Bericht darüber, was lief — sodass das Prüfen einer Behauptung gegen die echte Ausgabe meist das Risiko abdeckt. Planung und Multi-Agenten-Zusammenarbeit, die beiden, die er schwer vorhersagen kann, übergeben dir typischerweise etwas, das vor der Arbeit geschrieben wurde, oder über mehrere Dateien mehrerer Agenten verteilt ist: einen Plan, der auf ein Go wartet, oder eine Übergabe zwischen Agenten, die die Ausführung noch nicht getestet hat. Nach seiner eigenen Darstellung sind genau das die Dokumente, bei denen die Lücke zwischen Geschriebenem und dem, was wirklich passieren wird, am weitesten ist — derselbe Punkt, den `/reviewing-agent-plans/` aus Chip Huyens Essay im Abschnitt „Warum überhaupt vor dem Lauf“ zieht: Ein Problem zu fangen, bevor etwas gelaufen ist, ist der günstigste Ort, es zu fangen.

## Wo MarsDawn hilft und wo nicht

MarsDawn weiß nicht, welches von Ngs vier Mustern eine gegebene Datei erzeugt hat, ordnet nichts nach Vorhersagbarkeit und hat kein KI-Modell innen — es führt die Prüfung nicht aus, die seine Rangfolge nahelegt. Es hält die Datei lesbar, während du das selbst tust: Der Tab Gliederung (Darstellung ▸ Seitenleiste einblenden, ⌃⌘S) zeigt die Form eines langen Plans, Quelltext und gerenderte Vorschau stehen nebeneinander (⌘2), und für eine Multi-Agenten-Übergabe zeigt das Öffnen des gemeinsamen Ordners mit Ablage ▸ Ordner öffnen … (⇧⌘O) neue Dateien im Tab Dateien innerhalb etwa einer Sekunde, sobald verschiedene Agenten schreiben, und die Kopfzeile nennt den Git-Branch oder Worktree, damit zwei Dateien mit demselben Namen von verschiedenen Agenten nicht verwechselt werden.

## Ausprobieren

MarsDawn ist im Mac App Store erhältlich. Das kostenlose Befehlszeilenwerkzeug `marsdawn` funktioniert schon heute:

```
brew install redtear1115/tap/marsdawn
```

Es exportiert Markdown ohne die App als PDF.

[Befehlszeile](/de/cli/) · Vor dem Kauf wissen: [Was MarsDawn nicht kann](/de/limits/)

## Weiter

- Was jedes Muster dir typischerweise übergibt, vollständig: [Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt](/de/agent-design-patterns/)
- Die Fünf-Minuten-Prüfung eines Plans vor dem Lauf: [Den Plan eines Agenten in fünf Minuten prüfen](/de/reviewing-agent-plans/)
- Zurück zur Reihe: [Lektürenotizen der Redaktion](/de/reading-notes/)

## Quellen

- Andrew Ng, “Agentic Design Patterns Part 1,” The Batch, March 20, 2024: [https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng, “Agentic Design Patterns Part 3: Tool Use,” The Batch, April 3, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/) (abgerufen und zitiert am 2026-09-26).
- Andrew Ng, “Agentic Design Patterns Part 4: Planning,” The Batch, April 10, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/) (Zitat wörtlich aus `design/inbox/276-agent-blog-series.md`, bereits auf `/agent-design-patterns/` zitiert).
- Andrew Ng, “Agentic Design Patterns Part 5, Multi-Agent Collaboration,” The Batch, April 17, 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/) (abgerufen und zitiert am 2026-09-26).

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau neben dem Quelltext, Mermaid, KaTeX, Übersicht, PDF-Export. Gratis testen, einmalig 4,99 USD.
- [Deine Texte bleiben auf deinem Mac](https://marsdawn.southern-light.dev/de/yours/index.md): MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.
- [Kostenlos testen, einmal bezahlen](https://marsdawn.southern-light.dev/de/pay-once/index.md): MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.
- [PDF-Export](https://marsdawn.southern-light.dev/de/pdf/index.md): Exportiere Markdown auf deinem Mac als PDF oder drucke es, mit Mermaid-Diagrammen und hervorgehobenem Code. Seitenumbrüche vermeiden es, kurze Codeblöcke und Tabellen zu teilen.
- [Eine Mac-App](https://marsdawn.southern-light.dev/de/native/index.md): Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.
- [Was MarsDawn nicht kann](https://marsdawn.southern-light.dev/de/limits/index.md): Keine Synchronisierung, keine App für iPhone oder iPad, keine Plug-ins, keine Konten. Vier integrierte Themen. Gut zu wissen, bevor du kaufst.
- [Support](https://marsdawn.southern-light.dev/de/support/index.md): Hilfe zu MarsDawn, dem Markdown-Editor für macOS.
- [Datenschutzrichtlinie](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [Markdown auf dem Mac ansehen](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): Eine .md-Datei ist reiner Text mit Formatierungszeichen. So liest du sie auf dem Mac gerendert: heute als PDF mit dem kostenlosen Befehlszeilenwerkzeug marsdawn und in der MarsDawn-App aus dem Mac App Store.
- [Quick Look für Markdown](https://marsdawn.southern-light.dev/de/quicklook/index.md): Drücke im Finder die Leertaste auf einer Markdown-Datei und lies sie gerendert, mit Mermaid-Diagrammen, KaTeX-Formeln und hervorgehobenem Code. Die Übersicht von MarsDawn ist durch den Test nicht gesperrt.
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
- [Vorlagen](https://marsdawn.southern-light.dev/de/templates/index.md): Markdown-Vorlagen für die Dokumente, die ein Agent schreibt und du liest: eine Spezifikation, ein Flussdiagramm und ein Protokoll, jeweils mit einem Prompt für deinen Agenten.
- [Spezifikationsvorlage](https://marsdawn.southern-light.dev/de/templates/spec/index.md): Eine Markdown-Vorlage für Spezifikationen mit Anforderungen, einem Mermaid-Ablaufdiagramm und Akzeptanzkriterien. Dein Agent füllt sie aus, du prüfst sie in MarsDawn.
- [Flussdiagramm-Vorlage](https://marsdawn.southern-light.dev/de/templates/flowchart/index.md): Eine Mermaid-Flussdiagramm-Vorlage in Markdown, darunter die Schritte ausgeschrieben. Auf dem Mac in der Vorschau ansehen und als PDF exportieren.
- [Protokollvorlage](https://marsdawn.southern-light.dev/de/templates/meeting-notes/index.md): Eine Markdown-Vorlage für Besprechungsprotokolle mit Entscheidungen und Aufgaben, jeweils mit einer verantwortlichen Person. Dein Agent schreibt es, du prüfst es in MarsDawn.
- [English](https://marsdawn.southern-light.dev/reading-notes/andrew-ng-design-patterns/index.md): Across five letters in The Batch, Andrew Ng ranks reflection, tool use, planning and multi-agent collaboration by how reliable and predictable he finds each one — and what that ranking suggests about how closely to check each one's output.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章裡，Andrew Ng 依可靠與可預測的程度，幫 reflection、tool use、planning 和 multi-agent collaboration 排序——這個排序，對你該多仔細檢查哪一種的產出，有什麼提示。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reading-notes/andrew-ng-design-patterns/index.md): 在 The Batch 的五篇文章里，Andrew Ng 依可靠与可预测的程度，帮 reflection、tool use、planning 和 multi-agent collaboration 排序——这个排序，对你该多仔细检查哪一种的产出，有什么提示。
- [日本語](https://marsdawn.southern-light.dev/ja/reading-notes/andrew-ng-design-patterns/index.md): The Batch の 5 本の手紙のなかで、Andrew Ng は reflection、tool use、planning、multi-agent collaboration を、信頼性と予測可能性でランク付けしている。そのランク付けが、どのパターンの出力をどれだけ注意深くチェックすべきかについて、何を示唆しているか。
- [Français](https://marsdawn.southern-light.dev/fr/reading-notes/andrew-ng-design-patterns/index.md): Sur cinq lettres dans The Batch, Andrew Ng classe réflexion, usage d’outils, planification et collaboration multi-agents selon le degré de fiabilité et de prévisibilité qu’il trouve à chacun — et ce que ce classement suggère sur la rigueur avec laquelle lire la sortie de chacun.
- [Español](https://marsdawn.southern-light.dev/es/reading-notes/andrew-ng-design-patterns/index.md): A lo largo de cinco cartas en The Batch, Andrew Ng ordena reflexión, uso de herramientas, planificación y colaboración multiagente según lo fiables y predecibles que le parecen — y qué sugiere ese orden sobre con cuánto cuidado conviene comprobar la salida de cada uno.
- [한국어](https://marsdawn.southern-light.dev/ko/reading-notes/andrew-ng-design-patterns/index.md): The Batch의 편지 다섯 편에서 Andrew Ng은 성찰, 도구 사용, 계획, 다중 에이전트 협업을 각각 얼마나 믿을 만하고 예측 가능한지로 순위를 매깁니다 — 그리고 그 순위가 각 패턴의 출력을 얼마나 자세히 볼지에 대해 시사하는 바.
