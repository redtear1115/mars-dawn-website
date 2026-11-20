# Von HackMD auf den Mac

Deine Notizen sind schon Markdown, du musst also nichts umwandeln. Wähle unten einen Weg, je nachdem, wie viel du mitnimmst. Bilder brauchen einen eigenen Schritt. Lies diesen Abschnitt, bevor du auf HackMD etwas löschst.

Wir haben das im November 2026 mit einem kostenlosen HackMD-Konto geprüft. HackMD kann sich ändern, und Bezahlpläne und Team-Workspaces haben wir nicht getestet.

| Du möchtest | Dein Weg |
|---|---|
| Alle Notizen mitnehmen | Alle Notizen herunterladen |
| Notizen mitnehmen, die schon auf GitHub liegen | Repository klonen |
| Ein oder zwei Notizen mitnehmen | Eine Notiz herunterladen |

## Alle Notizen herunterladen

In den Notizeinstellungen von HackMD gibt es Download all notes, für persönliche und Team-Workspaces. Du bekommst eine .zip-Datei mit einer .md-Datei pro Notiz, benannt nach ihrem Titel.

- Ordner bleiben nicht erhalten. Alle Notizen liegen auf der obersten Ebene.
- Bilder sind nicht enthalten. Die .md-Dateien verweisen weiter per URL auf sie.
- Die Option für Titel und Tags ist standardmäßig an und fügt jeder Notiz einen Front-Matter-Block hinzu. Schalte sie aus, um jede Notiz genau wie geschrieben zu bekommen.

Entpacke die Datei und wähle in MarsDawn Ablage ▸ Ordner öffnen …, um den Ordner zu öffnen.

## Repository klonen

HackMDs GitHub-Synchronisierung verbindet eine Notiz mit einer Datei. Eine Notiz, die du gepusht hast, liegt also schon im Repository. Klone es und öffne den Ordner mit Ablage ▸ Ordner öffnen …. Die Seitenleiste zeigt das Repository und seinen Branch.

Notizen, die noch nicht auf GitHub liegen, musst du dafür nicht erst verbinden. Jede Notiz muss einzeln verknüpft werden, und der kostenlose Plan erlaubt 20 Pushes im Monat. Mit einem kostenlosen persönlichen Konto haben wir keinen Weg gefunden, einen ganzen Workspace auf einmal zu pushen.

Behandle das Repository nach dem Umzug als Original. Ein Push von HackMD ersetzt, was auf GitHub liegt, auch wenn GitHub neuere Inhalte hat, und warnt dich nicht.

## Eine Notiz herunterladen

Das Notizmenü lädt eine Notiz als .md oder .html herunter. Wähle .md und öffne die Datei in MarsDawn.

## Bilder

Bilder, die du auf HackMD hochgeladen hast, liegen unter `https://hackmd.io/_uploads/...`. Wer sie sehen darf, richtet sich nach der Berechtigung der Notiz.

| Deine Notiz ist | Das passiert auf deinem Mac | Das ist zu tun |
|---|---|---|
| Öffentlich | Das Bild wird von HackMD geladen | Klicke in der Vorschau auf „Bilder laden“ oder schalte Einstellungen ▸ Bilder ▸ Bilder aus dem Web automatisch laden ein |
| Privat | Das Bild liefert einen Fehler, weil MarsDawn nicht bei HackMD angemeldet ist | Sichere das Bild in einem angemeldeten Browser, lege es neben die .md-Datei und ändere den Pfad. Oder mach die Notiz öffentlich, wenn sie jeder lesen darf |

- **Ältere Notizen** verwenden eventuell stattdessen `i.imgur.com`-Adressen.
- **Wenn du eine Notiz löschst, sind auch ihre Bilder weg.** Ihre Adressen funktionieren nicht mehr, sichere die Bilder also vorher.

Wenn MarsDawn ein Bild neben deiner Datei nicht erreicht, gib ihm mit der Taste in der Vorschau Zugriff auf den Ordner.

## So sehen deine Notizen aus

Der Großteil der HackMD-Syntax liest sich gleich: `==Hervorhebung==`, `^hochgestellt^`, `~tiefgestellt~`, `[TOC]`, Bildgrößen wie `=300x200`, Mermaid und KaTeX. `{%youtube %}` erscheint als Link. Um wie bei HackMD jeden Zeilenumbruch zu behalten, schalte Einstellungen ▸ Erscheinungsbild ▸ Einzelne Zeilenumbrüche beibehalten ein.

Auch `:::`-Blöcke funktionieren. `:::info`, `:::success`, `:::warning` und `:::danger` erscheinen als Blöcke mit farbigem Balken und einer Überschrift. Standardmäßig lautet sie Hinweis, Tipp, Warnung oder Gefahr; schreibst du hinter den Namen eine eigene Überschrift, wird diese verwendet. `:::spoiler` erscheint als reduzierbarer Block, der sich mit einem Klick öffnet. Ein `:::`-Block mit einem anderen Namen oder ohne schließendes `:::` erscheint so, wie du ihn getippt hast.

Ein paar Dinge sehen anders aus:

- `++eingefügt++` und Emoji-Codes wie `:sparkles:` erscheinen so, wie du sie getippt hast.
- `{%hackmd id %}` wird nicht aufgelöst.
- `<i class="fa ...">`-Symbole erscheinen nicht.

## Für Skripte: hackmd-cli

`hackmd-cli` hat keinen Befehl, der alles auf einmal exportiert. Es exportiert eine Notiz und gibt sie aus. Du listest also zuerst deine Notizen auf und gehst sie in einer Schleife durch. Du brauchst Node.js, `jq` und einen API-Token aus deinen HackMD-Einstellungen. Wenn du kein Skript brauchst, ist Download all notes einfacher.

```
npm install -g @hackmd/hackmd-cli
export HMD_API_ACCESS_TOKEN=<dein Token>
hackmd-cli notes --output json | jq -r '.[].id' | while read -r id; do
  hackmd-cli export --noteId="$id" > "$id.md"
done
```

- **Ordner kommen nicht mit.** Die Notizliste sagt nicht, in welchem Ordner eine Notiz liegt, also landen alle Dateien an einem Ort.
- **Bilder bleiben `hackmd.io`-Links.** Behandle sie wie oben im Abschnitt „Bilder“.
- **Die Dateinamen sind Notiz-IDs,** keine Titel.
- **Der kostenlose Plan erlaubt 400 API-Aufrufe alle 30 Tage.** Die Liste braucht einen Aufruf, jede Notiz einen weiteren.

Wir haben das nur mit einem Konto mit wenigen Notizen ausprobiert. Wie sich eine sehr lange Liste verhält, wissen wir nicht. Lösche den Token danach in deinen HackMD-Einstellungen.

## Gemeinsam schreiben

MarsDawn hat kein gemeinsames Bearbeiten. Wenn ihr live zusammen schreibt, bleib bei HackMD. Wenn dein Team Dokumente in git hält, kann jede Person dasselbe Repository in ihrem eigenen MarsDawn öffnen, und ihr stellt das Dokument gemeinsam fertig. Siehe Dokumente im Team mit git prüfen.

## Fragen

### Kann ich alle meine HackMD-Notizen auf einmal herunterladen?

Ja. Download all notes liefert dir eine .zip-Datei mit .md-Dateien. Ordner bleiben nicht erhalten, und Bilder sind nicht enthalten.

### Warum fehlen meine Bilder in MarsDawn?

MarsDawn hält Bilder aus dem Web zurück, bis du auf „Bilder laden“ klickst. Ist die Notiz privat, lässt sich das Bild gar nicht laden. Sichere es dann neben deiner Datei.

### Muss ich HackMD verlassen?

Nein. Zum gemeinsamen Schreiben bleibt HackMD die bessere Wahl. MarsDawn ist zum Lesen und Prüfen auf deinem Mac da.

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): Lies Markdown, JSON und YAML deines Agenten nativ auf dem Mac: Live-Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Funktionen](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Mac-Editor für Markdown, JSON und YAML: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen und Papierakten.
- [Deine Texte bleiben auf deinem Mac](https://marsdawn.southern-light.dev/de/yours/index.md): MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.
- [Kostenlos testen, einmal bezahlen](https://marsdawn.southern-light.dev/de/pay-once/index.md): MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.
- [Drucken und PDF](https://marsdawn.southern-light.dev/de/pdf/index.md): Sieh dir dein Markdown in der Vorschau an, drucke es dann oder sichere es als PDF, im Layout Dokument, Handbuch oder Handout, mit Diagrammen und farbigem Code.
- [Eine Mac-App](https://marsdawn.southern-light.dev/de/native/index.md): Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.
- [Was MarsDawn nicht kann](https://marsdawn.southern-light.dev/de/limits/index.md): Keine Synchronisierung, kein Bearbeiten auf iPhone oder iPad, keine Plug-ins, keine Konten. Themen, aber kein eigenes CSS. Vor dem Kauf gut zu wissen.
- [Support](https://marsdawn.southern-light.dev/de/support/index.md): Hilfe zu MarsDawn, dem Markdown-Editor für macOS.
- [Datenschutzrichtlinie](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [So öffnest du .md-Dateien auf dem Mac](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): So öffnest du eine .md-Datei auf dem Mac: Doppelklick, Standard-App, Übersicht im Finder. Von einem KI-Agenten geschriebene .md liest du gerendert in MarsDawn.
- [Mermaid-Vorschau auf dem Mac](https://marsdawn.southern-light.dev/de/mermaid-preview-mac/index.md): Mermaid-Diagramme auf dem Mac neben deinem Markdown: Live-Vorschau, Übersicht und PDF-Export. Ein fehlerhaftes Diagramm zeigt den Fehler und die Zeile.
- [Übersicht für Markdown](https://marsdawn.southern-light.dev/de/quicklook/index.md): Mit MarsDawn zeigt die Übersicht Markdown im Finder per Leertaste gerendert: Mermaid, KaTeX, hervorgehobener Code. Sie funktioniert auch nach dem Test weiter.
- [Für KI kopieren](https://marsdawn.southern-light.dev/de/copy-for-ai/index.md): Kopiere ausgewählten Text mit Dateipfad und Zeilennummern und füge ihn in Claude Code oder einen anderen Agenten ein. Das geht auf dem Mac, ohne IDE oder Plugin.
- [Markdown zu PDF](https://marsdawn.southern-light.dev/de/markdown-to-pdf/index.md): Wandle Markdown auf dem Mac mit dem kostenlosen Befehlszeilenwerkzeug marsdawn in ein PDF um. Mit Homebrew installieren, einen Befehl ausführen: Tabellen, Mathematik, Mermaid und Code.
- [MarsDawn im Vergleich: VS-Code-Vorschau, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/de/vs/index.md): Für alle, die entscheiden, wie sie Markdown auf dem Mac lesen und prüfen, oft das, was ein Agent geschrieben hat. Jede Zelle unten stammt von den Seiten des Herstellers oder aus unserer eigenen Prüfung, alles am 16. Oktober 2026, außer der PDF-Zelle von MarsDawn, aktualisiert am 7. November 2026; Produkte ändern sich, also kann eine Zelle veralten. Wenn du einen Fehler findest, schreib an die Adresse auf Support.
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
- [English](https://marsdawn.southern-light.dev/from-hackmd/index.md): Download your HackMD notes as .md files and read them in MarsDawn on your Mac. How to download every note, use a GitHub repo, and keep your images working.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/from-hackmd/index.md): 把 HackMD 筆記下載成 .md，在 Mac 上用 MarsDawn 讀。下載所有筆記、從 GitHub repo 搬，以及圖片怎麼處理。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/from-hackmd/index.md): 把 HackMD 笔记下载成 .md，在 Mac 上用 MarsDawn 阅读。下载所有笔记、从 GitHub 仓库搬，以及图片怎么处理。
- [日本語](https://marsdawn.southern-light.dev/ja/from-hackmd/index.md): HackMD のノートを .md でダウンロードして、Mac の MarsDawn で読む方法。全ノートのダウンロード、GitHub リポジトリからの移行、画像の扱いをまとめました。
- [Français](https://marsdawn.southern-light.dev/fr/from-hackmd/index.md): Téléchargez vos notes HackMD en .md et lisez-les dans MarsDawn sur votre Mac. Comment tout télécharger, partir d’un dépôt GitHub et garder vos images.
- [Español](https://marsdawn.southern-light.dev/es/from-hackmd/index.md): Descarga tus notas de HackMD como .md y léelas en MarsDawn en tu Mac. Cómo descargar todas las notas, partir de un repositorio de GitHub y conservar tus imágenes.
- [한국어](https://marsdawn.southern-light.dev/ko/from-hackmd/index.md): HackMD 노트를 .md로 내려받아 Mac의 MarsDawn에서 읽는 방법입니다. 모든 노트 다운로드, GitHub 저장소에서 옮기기, 이미지 처리 방법을 정리했습니다.
