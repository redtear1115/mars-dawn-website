# MacMD Viewer oder MarsDawn.

Beides sind Mac-Apps, um Markdown gerendert zu lesen. MacMD Viewer öffnet eine `.md`-Datei und zeigt die fertige Seite, bearbeiten kann man sie darin nicht. MarsDawn stellt neben dieselbe Art gerenderter Vorschau einen Editor, sodass du in einem Fenster schreibst und prüfst. Hier die Unterschiede, Funktion für Funktion.

## Wenn du nur lesen und nicht bearbeiten musst

Wenn deine Aufgabe ausschließlich darin besteht, Markdown von anderen zu lesen, und du den Quelltext nie anfassen musst, passt MacMD Viewer gut: Die App ist genau dafür gebaut, jetzt erhältlich und läuft auch unter älteren macOS-Versionen. MarsDawn lohnt sich, sobald Lesen nicht die ganze Arbeit ist, denn das Markdown eines Agenten kommt meist noch einmal zur Überarbeitung zurück.

## Was die Apps können

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Bearbeiten | Bewusst nur zum Lesen | Bearbeitet den Quelltext, mit der gerenderten Seite daneben |
| Vorschauthemen | 12 Dokumentthemen | 4 Themen, jeweils mit heller und dunkler Farbpalette |
| Diagramme und Mathematik | Mermaid und Code-Hervorhebung; die Beschreibung erwähnt keine Mathematik | Mermaid, Code-Hervorhebung und KaTeX-Mathematik |
| Übersicht im Finder | Ja | Ja |
| PDF und Drucken | Ja | Ja |
| Voraussetzung | macOS 14 (Sonoma) oder neuer | macOS 26 (Tahoe) oder neuer |
| Sprachen der Oberfläche | In den eigenen Unterlagen nicht angegeben | Englisch, traditionelles Chinesisch, vereinfachtes Chinesisch, Japanisch, Deutsch, Französisch, Spanisch und Koreanisch |

## Preis und Kauf

|  | MacMD Viewer | MarsDawn |
|---|---|---|
| Wo du es kaufst | Eigene Website, Homebrew oder Setapp; nicht im Mac App Store | Nur im Mac App Store |
| Preis | Einmalig 19,99 USD für einen Mac; Pakete für mehrere Macs kosten mehr | Kostenloser Download, dann einmalig 4,99 USD |
| Vorher ausprobieren | Keine Testphase; 14 Tage Geld-zurück-Garantie bei Direktkauf | 14 Tage kostenlos testen |
| Rückerstattung und Updates | Über die eigene Website | Über Apple |
| Account nötig | Nein | Nein |

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
- [Lektürenotizen: Andrew Ng](https://marsdawn.southern-light.dev/de/reading-notes/andrew-ng-design-patterns/index.md): Über fünf Briefe in The Batch ordnet Andrew Ng Reflexion, Werkzeugnutzung, Planung und Multi-Agenten-Zusammenarbeit danach, wie verlässlich und vorhersagbar er jedes findet — und was diese Rangfolge dazu nahelegt, wie genau man die Ausgabe jedes Musters prüfen sollte.
- [Vorlagen](https://marsdawn.southern-light.dev/de/templates/index.md): Markdown-Vorlagen für die Dokumente, die ein Agent schreibt und du liest: eine Spezifikation, ein Flussdiagramm und ein Protokoll, jeweils mit einem Prompt für deinen Agenten.
- [Spezifikationsvorlage](https://marsdawn.southern-light.dev/de/templates/spec/index.md): Eine Markdown-Vorlage für Spezifikationen mit Anforderungen, einem Mermaid-Ablaufdiagramm und Akzeptanzkriterien. Dein Agent füllt sie aus, du prüfst sie in MarsDawn.
- [Flussdiagramm-Vorlage](https://marsdawn.southern-light.dev/de/templates/flowchart/index.md): Eine Mermaid-Flussdiagramm-Vorlage in Markdown, darunter die Schritte ausgeschrieben. Auf dem Mac in der Vorschau ansehen und als PDF exportieren.
- [Protokollvorlage](https://marsdawn.southern-light.dev/de/templates/meeting-notes/index.md): Eine Markdown-Vorlage für Besprechungsprotokolle mit Entscheidungen und Aufgaben, jeweils mit einer verantwortlichen Person. Dein Agent schreibt es, du prüfst es in MarsDawn.
- [English](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/vs/macmd-viewer/index.md): MacMD Viewer 是唯讀檢視器，直接購買 USD 19.99。MarsDawn 邊編輯邊預覽，免費試用後在 Mac App Store 一次解鎖 USD 4.99。逐項比較功能、價格和購買方式。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/vs/macmd-viewer/index.md): MacMD Viewer 是只读查看器，直接购买 USD 19.99。MarsDawn 边编辑边预览，免费试用后在 Mac App Store 一次解锁 USD 4.99。逐项比较功能、价格和购买方式。
- [日本語](https://marsdawn.southern-light.dev/ja/vs/macmd-viewer/index.md): MacMD Viewer は読み取り専用で Markdown をレンダリングし、USD 19.99。MarsDawn は編集とプレビューを並べて表示し、無料で試したあと Mac App Store で USD 4.99 の一度きりの購入です。
- [Français](https://marsdawn.southern-light.dev/fr/vs/macmd-viewer/index.md): MacMD Viewer affiche le Markdown en lecture seule pour 19,99 USD. MarsDawn modifie et affiche l’aperçu côte à côte, gratuit à l’essai puis 4,99 USD une seule fois sur le Mac App Store.
- [Español](https://marsdawn.southern-light.dev/es/vs/macmd-viewer/index.md): MacMD Viewer muestra Markdown solo para lectura por 19,99 USD. MarsDawn edita y muestra la vista previa lado a lado: pruébalo gratis y luego paga 4,99 USD una sola vez en el Mac App Store.
- [한국어](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 Markdown을 읽기 전용으로 렌더링하며 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 무료로 체험한 뒤 Mac App Store에서 USD 4.99에 한 번만 구입하면 됩니다.
