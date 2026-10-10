# Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt

Im März 2024 beschrieb Andrew Ng in seinem Newsletter The Batch vier Entwurfsmuster für KI-Agenten: Reflexion, Werkzeugnutzung, Planung und Zusammenarbeit mehrerer Agenten. Meist werden sie aus Sicht der Entwickler besprochen, als Wege, bessere Ergebnisse aus einem Modell zu holen. Dieser Beitrag schaut von der anderen Seite. Wenn du einen Agenten nutzt, der auf einem dieser Muster aufbaut: Was landet in deinem Ordner, und was solltest du zuerst lesen?

**Die vier Muster stammen von Andrew Ng. Welche Dokumente jedes typischerweise übergibt und was du darin prüfen solltest, ist unsere eigene Schlussfolgerung. Er schreibt über beides nicht und plädiert in dieser Reihe nicht für menschliche Prüfung.**

## Die vier Muster in Kürze

Ng beschreibt sie in „Agentic Design Patterns Part 1“. Kurz gesagt: Bei **Reflexion** sieht das Modell seine eigene Arbeit durch und verbessert sie. Bei **Werkzeugnutzung** kann es Werkzeuge wie Websuche oder Codeausführung aufrufen. Bei **Planung** entwirft es einen Plan aus mehreren Schritten und führt ihn aus. Bei der **Zusammenarbeit mehrerer Agenten** teilen sich mehrere Agenten die Arbeit auf und besprechen sie.

In Teil 1 zeigt er den Nutzen anhand eines Coding-Benchmarks, HumanEval, mit Ergebnissen, die sein Team von mehreren Forschungsgruppen zusammengetragen hat: „GPT-3.5 (Zero-Shot) lag zu 48,1 % richtig. GPT-4 (Zero-Shot) schneidet mit 67,0 % besser ab. Die Verbesserung von GPT-3.5 zu GPT-4 verblasst jedoch neben der Einbindung in einen iterativen Agenten-Workflow. In eine Agentenschleife eingebettet erreicht GPT-3.5 sogar bis zu 95,1 %.“ Diese Zahlen beziehen sich auf einen einzigen Coding-Benchmark, und 95,1 % ist der beste Fall („bis zu“). Sie zeigen, dass Agenten-Workflows die Ausgabe verbessern können. Darüber, wer sie prüft, sagen sie nichts.

**Ab hier sind die Dokumente und die Prüfungen unsere Lesart, nicht die von Ng.** Echte Agenten mischen die Muster außerdem. Ein Coding-Agent kann in einer Sitzung planen, Werkzeuge ausführen und seine eigene Arbeit prüfen, du bekommst also oft alle vier Arten von Dateien.

## 1. Reflexion: ein Entwurf, der sich schon selbst geprüft hat

Ngs Beitrag über Reflexion stellt sie als Automatisierung des Feedbacks dar, das sonst ein Mensch geben würde: „Was, wenn man den Schritt automatisiert, kritisches Feedback zu geben, sodass das Modell seine eigene Ausgabe automatisch kritisiert und seine Antwort verbessert?“

**Was es typischerweise übergibt:** ein überarbeitetes Dokument, manchmal mit einem Abschnitt zur Selbstprüfung oder Zeilen wie „Randfälle doppelt geprüft“.

**Was du prüfen solltest:** das Ergebnis gegen *deine* Anfrage, nicht gegen die Selbstkritik des Agenten. Selbstprüfung kann auf ihre eigene Art schiefgehen. Chip Huyen: „Eine interessante Art von Planungsfehler entsteht durch Fehler in der Reflexion. Der Agent ist überzeugt, eine Aufgabe erledigt zu haben, obwohl er es nicht hat.“ Lilian Weng schrieb im Juni 2023 in ihrem Blog Lil’Log, damals bei OpenAI, über die Modelle jener Zeit: „Mangelnde Fachkenntnis kann dazu führen, dass LLMs ihre Schwächen nicht kennen und daher die Richtigkeit von Aufgabenergebnissen nicht gut beurteilen können.“ (In der Studie, die sie beschrieb, stimmten die Bewertung der Ergebnisse durch ein LLM und die durch menschliche Fachleute nicht überein.) Wenn dort „geprüft“ steht, prüfe selbst eine Sache.

## 2. Werkzeugnutzung: ein Bericht darüber, was lief

**Was es typischerweise übergibt:** eine Zusammenfassung dessen, was der Agent ausgeführt oder gesucht hat und was zurückkam. „Testsuite ausgeführt: alles grün.“ Eine Ergebnistabelle. Gefundene Links.

Anthropics Leitfaden beschreibt Werkzeugergebnisse als die Selbstkontrolle des Agenten: „Während der Ausführung ist es entscheidend, dass die Agenten bei jedem Schritt ‚Ground Truth‘ aus der Umgebung erhalten (etwa Ergebnisse von Werkzeugaufrufen oder Codeausführung), um ihren Fortschritt zu beurteilen.“ Diese Kontrolle findet im Agenten statt. Was bei dir ankommt, ist die Nacherzählung des Agenten davon.

**Was du prüfen solltest:** dass sich jede Behauptung auf eine Ausgabe zurückführen lässt, die du sehen kannst. Gleiche eine Zahl in der Zusammenfassung mit der echten Ausgabe ab. Öffne einen der Links.

## 3. Planung: `plan.md`

**Was es typischerweise übergibt:** einen Plan, eine Spezifikation, eine Aufgabenliste mit Kontrollkästchen, die der Agent unterwegs abhakt.

Ng äußert sich in Teil 4 offen über dieses Muster:

> „Einerseits ist Planung eine sehr mächtige Fähigkeit; andererseits führt sie zu weniger vorhersehbaren Ergebnissen. Meiner Erfahrung nach kann ich die agentischen Entwurfsmuster Reflexion und Werkzeugnutzung zuverlässig zum Laufen bringen und damit die Leistung meiner Anwendungen verbessern, doch Planung ist eine weniger ausgereifte Technik, und es fällt mir schwer, vorab vorherzusagen, was sie tun wird.“

Er ist aber auch zuversichtlich: „Doch das Gebiet entwickelt sich weiterhin rasant, und ich bin zuversichtlich, dass die Planungsfähigkeiten sich schnell verbessern werden.“

**Was du prüfen solltest:** den Plan, bevor er läuft, mit [der Fünf-Minuten-Prüfung](/de/reviewing-agent-plans/): Form, eine Behauptung, Schritte, die sich nicht rückgängig machen lassen, Diagramme, Umfang. Wenn der Agent den Plan mittendrin umschreibt, vergleiche ihn mit der Fassung, die du freigegeben hast; liegt er in Git, zeigt `git diff plan.md`, was sich geändert hat. In MarsDawn zeigt der Tab Gliederung die Form eines langen Plans, und ein umgeschriebener Plan wird neu geladen, ohne dass du deine Stelle verlierst, solange du keine eigenen ungesicherten Änderungen hast.

## 4. Zusammenarbeit mehrerer Agenten: mehrere Dateien, mehrere Autoren

**Was es typischerweise übergibt:** eine Spezifikation von einem Agenten, Umsetzungsnotizen von einem zweiten, eine Prüfung von einem dritten und Zusammenfassungen, die zwischen ihnen weitergereicht werden. Manchmal arbeitet jeder in einem eigenen Branch oder Worktree.

**Was du prüfen solltest:** die Übergaben. Wo ein Agent die Arbeit eines anderen zusammenfasst, such nach einer Anforderung, die nicht mit hinübergekommen ist. Such nach zwei Dateien, die sich widersprechen, und entscheide, welche die maßgebliche ist, bevor jemand auf der anderen aufbaut. Öffne in MarsDawn den gemeinsamen Ordner mit Ablage ▸ Ordner öffnen … (⇧⌘O): Neue Dateien erscheinen innerhalb etwa einer Sekunde im Tab Dateien, während die Agenten sie schreiben, und bei einem Git-Checkout nennt die Kopfzeile den Branch oder Worktree, damit zwei Fenster mit demselben Dateinamen aus verschiedenen Branches nicht gleich aussehen. Wenn das Ergebnis an Leute gehen muss, die kein Markdown lesen, zeigt [Exportierte PDFs teilen](/de/sharing-exported-pdfs/) diesen Schritt.

## Auf einen Blick

| Muster (Ng) | Was es typischerweise übergibt (unsere Schlussfolgerung) | Zuerst lesen (unser Vorschlag) |
|---|---|---|
| Reflexion | Ein überarbeiteter Entwurf, vielleicht mit Selbstprüfung | Das Ergebnis gegen deine eigene Anfrage; ein „geprüft“ selbst prüfen |
| Werkzeugnutzung | Ein Bericht darüber, was lief und was zurückkam | Eine Behauptung bis zur echten Ausgabe zurückverfolgen |
| Planung | `plan.md`, eine Spezifikation, eine Aufgabenliste | Die Fünf-Minuten-Prüfung, bevor er läuft |
| Zusammenarbeit mehrerer Agenten | Mehrere Dateien von mehreren Agenten, vielleicht auf mehreren Branches | Die Übergaben und welche Datei die maßgebliche ist |

Keiner der hier zitierten Autoren erwähnt MarsDawn, und keiner empfiehlt es oder ein anderes Markdown-Werkzeug. In MarsDawn steckt kein KI-Modell: Es weiß nicht, welches Muster eine Datei erzeugt hat, und es übernimmt diese Prüfungen nicht für dich. Es hält die Dateien lesbar, während du sie machst.

## Ausprobieren

MarsDawn gibt es im [Mac App Store](https://apps.apple.com/app/id6812925073). Dazu kommt das kostenlose Befehlszeilenwerkzeug `marsdawn`:

```
brew install redtear1115/tap/marsdawn
```

Es exportiert Markdown ohne die App als PDF: siehe [Markdown in PDF](/de/markdown-to-pdf/).

[Befehlszeile](/de/cli/) · Vor dem Kauf wissen: [Was MarsDawn nicht kann](/de/limits/)

## Weiter

- Warum Agentenausgaben schwer zu lesen sind, mit einer Checkliste: [Lesen, was dein Agent zurückgibt](/de/reading-agent-output/).
- Die Planungsprüfung vollständig: [Einen Agentenplan in fünf Minuten prüfen](/de/reviewing-agent-plans/).
- Was Transparenz von dir verlangt und was nicht: [Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?](/de/agent-transparency/)

## Quellen

- Andrew Ng, „Agentic Design Patterns Part 1“, The Batch, 20. März 2024: [https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/)
- Andrew Ng, „Agentic Design Patterns Part 2, Reflection“, The Batch, 27. März 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/)
- Andrew Ng, „Agentic Design Patterns Part 4, Planning“, The Batch, 10. April 2024: [https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/)
- Chip Huyen, „Agents“, 7. Januar 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Lilian Weng, „LLM Powered Autonomous Agents“, Lil’Log, 23. Juni 2023: [https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)
- Erik S. und Barry Zhang, „Building Effective Agents“, Anthropic, 19. Dezember 2024: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents) (zitiert nach der am 26.09.2026 online verfügbaren Fassung).

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
- [Transparenz von Agenten](https://marsdawn.southern-light.dev/de/agent-transparency/index.md): Anthropics Leitfaden zum Bau von Agenten verlangt Transparenz: Zeig die Planungsschritte. Was er sagt, was nicht, und warum die Schritte meist als Markdown-Datei enden, die jemand lesen muss.
- [Den Plan eines Agenten prüfen](https://marsdawn.southern-light.dev/de/reviewing-agent-plans/index.md): Ein Weg in sechs Schritten, den Plan eines KI-Agenten zu prüfen, bevor er läuft, in etwa fünf Minuten und in jedem Editor, mit einem durchgespielten Beispiel.
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
- [English](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/agent-design-patterns/index.md): Andrew Ng 提出的四種 agent 設計模式：reflection、tool use、planning、multi-agent collaboration，以及每一種通常會交回什麼要你讀的文件。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/agent-design-patterns/index.md): Andrew Ng 提出的四种 agent 设计模式：reflection、tool use、planning、multi-agent collaboration，以及每一种通常会交回什么要你读的文件。
- [日本語](https://marsdawn.southern-light.dev/ja/agent-design-patterns/index.md): Andrew Ng が描いた reflection、tool use、planning、multi-agent collaboration という 4 つの設計パターン、それぞれがどんな文書を返してくる傍向があるか。
- [Français](https://marsdawn.southern-light.dev/fr/agent-design-patterns/index.md): Réflexion, utilisation d’outils, planification et collaboration multi-agents, tels qu’Andrew Ng les a décrits, et ce que chacun vous rend généralement à lire.
- [Español](https://marsdawn.southern-light.dev/es/agent-design-patterns/index.md): Reflexión, uso de herramientas, planificación y colaboración multiagente, tal como los describió Andrew Ng, y lo que cada uno suele entregarte para leer.
- [한국어](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
