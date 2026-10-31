# Markdown auf dem Mac lesen: MarsDawn und andere Wege

Für alle, die entscheiden, wie sie Markdown auf dem Mac lesen und prüfen, oft das, was ein Agent geschrieben hat. Jede Zelle unten stammt von den Seiten des Herstellers oder aus unserer eigenen Prüfung, alles am 16. Oktober 2026; Produkte ändern sich, also kann eine Zelle veralten. Wenn du einen Fehler findest, schreib an die Adresse auf [Support](/de/support/).

|  | MarsDawn | VS-Code-Vorschau | Obsidian | QLMarkdown | LynxOffice |
|---|---|---|---|---|---|
| Lokale .md öffnen | Ja, bearbeitet die Datei direkt [app 1.1.1] | Ja, Vorschau mit ⇧⌘V [[8](#v8)] | Vom Hersteller nicht angegeben [[21](#v21)] | Nur Vorschau: "for viewing Markdown files" [[22](#v22)] | "Markdown opens rendered and saves back verbatim." [[3](#v3)] |
| Mermaid | Integriert [[1](#v1)] | Integriert [[8](#v8)] | Integriert, Notizsyntax [[16](#v16)] | Integriert, `mermaid`-Blöcke [[22](#v22)] | "diagram blocks are not rendered" [[3](#v3)] |
| Formeln | KaTeX, `$…$` und `$$…$$` [[kit](#kit)] | KaTeX [[8](#v8)] | MathJax [[16](#v16)] | MathJax [[22](#v22)] | "Footnotes, math, and diagram blocks are not rendered." [[3](#v3)] |
| Plan eines Agenten prüfen / zu einer Zeile springen | `marsdawn open file:line`; Von Festplatte aktualisieren; Verweis kopieren [/cli/, /features/] | Markdown-Diff-Vorschau, geänderte Zeilen hervorgehoben [[8](#v8)]; `code -g file:line` [[14](#v14)] | Kein Zeilenparameter in `obsidian://open` [[20](#v20)] | Vom Hersteller nicht angegeben | CLI und MCP-Server; Sprung zur Zeile nicht angegeben [[4](#v4), [5](#v5)] |
| PDF: Seitenumbrüche, Seitenzahlen | Umbrüche teilen keine kurzen Codeblöcke [/pdf/]; keine Seitenzahlen [Prüfung] | Vom Hersteller nicht angegeben [[8](#v8)] | Papierformat, Ränder; Umbrüche und Zahlen nicht angegeben [[17](#v17)] | Vom Hersteller nicht angegeben [[22](#v22)] | PDF "including tables"; Umbrüche und Zahlen nicht angegeben [[3](#v3)] |
| Preis | Kostenloser Download; Freischaltung einmal 4,99 USD; 14 Tage Test [[1](#v1)] | Vom Hersteller nicht angegeben [[12](#v12), [13](#v13)] | Privat: "Free without limits"; kommerzielle Lizenz optional [[15](#v15)] | Kostenlos, GPL-3.0 [[22](#v22)] | "Free while in early release." [[2](#v2)] |
| Systemvoraussetzungen | macOS 26.0 oder neuer [[1](#v1)] | "the latest release and the two previous versions" [[9](#v9)] | Vom Hersteller nicht angegeben [[18](#v18)] | macOS 12.0 oder neuer [[23](#v23)] | macOS 13 oder neuer [[2](#v2)] |
| Konto nötig | Nein [/privacy/] | Vom Hersteller nicht angegeben | "No sign-up required" [[15](#v15)] | Vom Hersteller nicht angegeben | Nein [[2](#v2)] |

Jede Zelle wurde am 16. Oktober 2026 an der Quelle in Klammern geprüft (die V-Nummern stehen unten; [Prüfung] ist unser eigener Export mit marsdawn 0.6.4). Zitate der Hersteller bleiben im Original. „Vom Hersteller nicht angegeben“ heißt, dass die gelesenen Seiten dazu schweigen, nicht dass die Funktion fehlt. Keine Zelle bewertet die Produkte. Die Spalte von MarsDawn selbst wurde am 29. Oktober 2026 für die iPhone- und iPad-App aktualisiert.

## Quellen

- 1 · [Mac App Store](https://apps.apple.com/app/id6812925073)
- 2 · [https://lynxoffice.com/](https://lynxoffice.com/)
- 3 · [https://lynxoffice.com/markdown/](https://lynxoffice.com/markdown/)
- 4 · [https://lynxoffice.com/cli/](https://lynxoffice.com/cli/)
- 5 · [https://lynxoffice.com/mcp/](https://lynxoffice.com/mcp/)
- 6 · [https://lynxoffice.com/release-notes/](https://lynxoffice.com/release-notes/)
- 8 · [https://code.visualstudio.com/docs/languages/markdown](https://code.visualstudio.com/docs/languages/markdown)
- 9 · [https://code.visualstudio.com/docs/supporting/requirements](https://code.visualstudio.com/docs/supporting/requirements)
- 11 · [https://code.visualstudio.com/updates/v1_142](https://code.visualstudio.com/updates/v1_142)
- 12 · [https://code.visualstudio.com/license](https://code.visualstudio.com/license)
- 13 · [https://code.visualstudio.com/](https://code.visualstudio.com/)
- 14 · [https://code.visualstudio.com/docs/configure/command-line](https://code.visualstudio.com/docs/configure/command-line)
- 15 · [https://obsidian.md/pricing](https://obsidian.md/pricing)
- 16 · [https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax](https://obsidian.md/help/Editing+and+formatting/Advanced+formatting+syntax)
- 17 · [https://obsidian.md/help/pdf](https://obsidian.md/help/pdf)
- 18 · [https://obsidian.md/download](https://obsidian.md/download)
- 19 · [https://obsidian.md/changelog/](https://obsidian.md/changelog/)
- 20 · [https://obsidian.md/help/uri](https://obsidian.md/help/uri)
- 21 · [https://obsidian.md/help/Getting+started/Create+a+vault](https://obsidian.md/help/Getting+started/Create+a+vault)
- 22 · [https://github.com/sbarex/QLMarkdown](https://github.com/sbarex/QLMarkdown)
- 23 · [https://github.com/sbarex/QLMarkdown/releases](https://github.com/sbarex/QLMarkdown/releases)
- 24 · [https://api.github.com/repos/sbarex/QLMarkdown/releases](https://api.github.com/repos/sbarex/QLMarkdown/releases)
- kit · [https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7](https://github.com/redtear1115/mars-dawn-kit/blob/0.6.4/README.md?plain=1#L7)

Was MarsDawn fehlt. Es braucht macOS 26 oder neuer. Auf iPhone und iPad liest es nur: Bearbeiten und PDF-Export gibt es dort nicht. Kein gemeinsames Bearbeiten, keine Synchronisierung und kein Konto. Die Vorschau lässt sich nicht bearbeiten; du bearbeitest den Markdown-Quelltext daneben. Kein Word-Export und keine Plug-ins. Die PDFs haben keine Seitenzahlen. Es gibt keine Diff-Ansicht: Sichert ein Agent eine Änderung, aktualisiert sich das offene Fenster von der Festplatte in einem Schritt, den du widerrufen kannst, hebt aber nicht hervor, was sich geändert hat. Nach dem 14-tägigen Test öffnen sich Dokumente mit verdecktem Inhalt, bis du freischaltest.

## Wann du MarsDawn nicht brauchst

- Du arbeitest ohnehin in VS Code, und eine Vorschau reicht: Sie rendert Mermaid und KaTeX, hat eine Markdown-Diff-Vorschau und springt mit code -g zu einer Zeile.
- Du willst nur eine Vorschau per Leertaste im Finder: QLMarkdown ist eine kostenlose Übersicht-Erweiterung für Markdown.
- Dein Mac hat ein älteres macOS: QLMarkdown braucht 12.0 oder neuer, LynxOffice 13 oder neuer. Das kostenlose Tool marsdawn braucht macOS 15 und exportiert PDF ohne die App.
- Du führst einen Vault verknüpfter Notizen: Dafür ist Obsidian gemacht.
- Du willst auf iPhone oder iPad bearbeiten oder brauchst gemeinsames Bearbeiten oder Word-Export.
- Ein Agent soll Tabellen, Word-Dateien und PDFs bearbeiten: LynxOffice dokumentiert dafür einen MCP-Server.

- [MacMD Viewer oder MarsDawn](/de/vs/macmd-viewer/): ein reiner Viewer neben MarsDawn, Zelle für Zelle, mit der Frage, wann welches passt.
- [Markdown-Vorschau-Tools](/de/vs/markdown-preview-tools/): die VS-Code-Vorschau, eine Browser-Erweiterung und die Dateivorschau von Claude Desktop.
- [Der beste Markdown-Viewer für den Mac (2026)](/de/best-markdown-viewer-mac/)

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
- [English](https://marsdawn.southern-light.dev/vs/index.md): For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on Support.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/index.md): 寫給正在挑選工具、要在 Mac 上讀 Markdown（常常是 agent 寫的）的人。下表每一格都出自廠商自己的頁面或我們實際的檢查，日期都是 2026 年 10 月 16 日；產品會變，格子也可能過時。發現錯誤，請寫信到支援頁上的地址。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/index.md): 写给正在挑选工具、要在 Mac 上读 Markdown（常常是代理写的）的人。下表每一格都出自厂商自己的页面或我们实际的检查，日期都是 2026 年 10 月 16 日；产品会变，格子也可能过时。发现错误，请写信到支持页上的地址。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/index.md): Mac で Markdown を、多くはエージェントが書いたものを読んで確かめる方法を選ぶ人へ。表の各セルは、各社の公式ページか私たちの確認によるもので、いずれも 2026 年 10 月 16 日時点です。製品は変わるので、古くなることがあります。誤りに気づいたら、サポートのアドレスまでお知らせください。
- [Français](https://marsdawn.southern-light.dev/fr/vs/index.md): Pour celles et ceux qui choisissent comment lire et relire du Markdown sur Mac, souvent écrit par un agent. Chaque cellule ci-dessous vient des pages du fournisseur ou de notre propre vérification, toutes au 16 octobre 2026 ; les produits évoluent, une cellule peut donc vieillir. Si vous repérez une erreur, écrivez à l’adresse indiquée sur Assistance.
- [Español](https://marsdawn.southern-light.dev/es/vs/index.md): Para quien elige cómo leer y revisar Markdown en un Mac, a menudo lo que escribió un agente. Cada celda viene de las páginas del propio fabricante o de nuestra propia comprobación, todas del 16 de octubre de 2026; los productos cambian, así que una celda puede quedar desfasada. Si ves un error, escribe a la dirección que aparece en Soporte.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
