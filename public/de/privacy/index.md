# Datenschutzrichtlinie

Wie MarsDawn, der Markdown-Editor für macOS, mit deinen Daten umgeht.

Zuletzt aktualisiert am 2026-10-10

> **Die App MarsDawn erhebt keinerlei Daten über dich.** Es gibt kein Konto, keine Werbung und kein Tracking. Deine Dokumente und Einstellungen bleiben auf deinem Mac.

## Die Website

Die App und diese Website sind zwei verschiedene Dinge. Die App erhebt nichts. Ein Besuch kann nur hier erfasst werden, auf marsdawn.southern-light.dev.

Diese Website verwendet **Google Analytics 4**, geladen über den **Google Tag Manager**. Für alle Besucher ist die Analyse zunächst abgelehnt: Der Einwilligungsmodus (Consent Mode) von Google sendet nur einen cookielosen Ping, ohne Analyse-Cookie und ohne dauerhafte Kennung, bis du im Banner *Akzeptieren* wählst. Wählst du *Ablehnen* oder triffst du gar keine Wahl, bleibt es dabei. Wählst du *Ablehnen*, nachdem du zuvor *Akzeptieren* gewählt hast, wird die Analyse sofort wieder abgeschaltet, und die unten genannten Cookies werden entfernt. Du kannst deine Wahl jederzeit über den Link „Cookie-Einstellungen“ in der Fußzeile jeder Seite ändern. Die Wahl selbst wird nur im lokalen Speicher deines Browsers abgelegt, nie in einem Cookie von uns.

Sobald du zustimmst, setzt Google Analytics eigene Cookies (`_ga` und `_ga_<measurement id>`) und erfasst:

- **Seitenaufrufe und Referrer.** Welche Seite aufgerufen wurde, und die verweisende Adresse, wenn der Browser sie mitsendet.
- **Ungefährer Standort, Gerät und Browser.** Ein grober Standort, abgeleitet aus deiner IP-Adresse (höchstens auf Stadtebene), dein Gerätetyp, dein Betriebssystem und dein Browser. Nichts davon ist genau genug, um dich zu identifizieren.
- **Klicks nach außen und Scrolltiefe.** Die erweiterten Messfunktionen von Google Analytics erfassen Klicks, mit denen du die Website verlässt, etwa auf den Link zum Mac App Store, und wie weit du auf einer Seite nach unten scrollst.
- **IP-Adressen.** Google Analytics 4 protokolliert oder speichert keine IP-Adressen.
- **Was nicht erfasst wird.** Kein Konto, denn die Website hat keine. Kein Dokument und nichts, was du eingibst. Keine websiteübergreifende Werbung und kein Profil von dir. Anfragen der App nach Themadateien unter `/themes/` werden ausgelassen und nicht weitergegeben. Der Themensimulator und die Galerie unter `/themes/new/` und `/themes/gallery/` laufen vollständig in deinem Browser und senden ebenfalls keine Themendaten an Google Analytics.
- **Aufbewahrung.** Google bewahrt diese Daten 14 Monate lang auf und löscht sie dann.
- **Wo die Daten verarbeitet werden.** Google Tag Manager und Google Analytics werden von Google betrieben. Deine Daten können in den Vereinigten Staaten sowie in anderen Ländern verarbeitet werden, in denen Google tätig ist.
- **Der Hoster.** Cloudflare hostet die Website und sieht, wie jeder Hoster, deine IP-Adresse, während die Anfrage beantwortet wird. Dieses Protokoll gehört dem Hoster. Es ist nicht die oben beschriebene Analyse.

## Was auf deinem Mac bleibt

- **Deine Dokumente.** MarsDawn liest und schreibt nur die Dateien und Ordner, die du öffnest, sicherst oder auswählst. Die App lädt sie nirgendwohin hoch.
- **Deine Einstellungen.** Erscheinungsbild, Vorschau-Thema, Fensterlayout und die Einstellung für Bilder werden in den eigenen Einstellungen der App auf deinem Mac gespeichert.
- **Ordnerzugriff, den du erlaubst.** Wenn du MarsDawn Bilder oder Seitendateien aus einem Ordner anzeigen lässt oder einen Notizordner auswählst, behält die App ein macOS-Lesezeichen, damit sie diesen Ordner wieder öffnen kann. Ein Ordner, den du in der Seitenleiste öffnest, bleibt für MarsDawn lesbar und beschreibbar, bis du ihn in den Einstellungen entfernst, nicht nur, solange sein Fenster offen ist. Du kannst Ordner jederzeit unter „MarsDawn“ › „Einstellungen“ entfernen.

## Wann MarsDawn das Internet nutzt

MarsDawn funktioniert vollständig offline. Es verbindet sich nur dann mit dem Internet, **wenn du dich dafür entscheidest**, und zwar für ein Dokument, das auf das Web verweist, oder für die Themengalerie. Für Dokumente gilt:

- **Markdown-Dokumente.** Bilder aus dem Web sind standardmäßig blockiert. Sie werden erst geladen, wenn du in der Vorschau auf *Bilder laden* klickst oder in den Einstellungen *Bilder aus dem Web automatisch laden* aktivierst. Sonst wird nichts, worauf ein Markdown-Dokument verweist, aus dem Web geladen.
- **HTML-Dokumente.** Ein HTML-Dokument öffnet sich statisch: Sein Code läuft nicht, und nichts wird aus dem Web geladen. Enthält ein Dokument Code, der laufen könnte, kannst du für dieses Dokument *Darstellung › Dieses Dokument ausführen* wählen. Sein eigener Code läuft dann, bis du ihn stoppst, das Dokument neu geladen wird oder du das Fenster schließt. Diese Wahl wird nie gespeichert, und sie ist keine Einstellung. Während der Code läuft, kann das Dokument Daten über das Netzwerk senden sowie Bilder, Stylesheets, Schriften und Medien in seinem Ordner und den darin enthaltenen Ordnern lesen. Code, der aus dem Web geladen wird, läuft nie.

MarsDawn lädt Webinhalte nur über https. Eine einfache http-Adresse wird nie geladen, bei keiner Einstellung, und MarsDawn schreibt sie auch nicht in https um. In einem Markdown-Dokument zeigt die Vorschau an ihrer Stelle einen Platzhalter.

Wenn Webinhalte geladen werden, fordert dein Mac sie direkt bei den Servern an, die sie bereitstellen. Wie bei jeder Webanfrage sehen diese Server dadurch deine IP-Adresse und was angefordert wurde. Der Entwickler von MarsDawn erhält keine dieser Informationen.

Links, auf die du in der Vorschau klickst, öffnen sich in deinem Standard-Webbrowser, nach dessen eigenen Datenschutzpraktiken. Audio und Video spielen nie von selbst ab.

Wenn du *Einstellungen › Erscheinungsbild › Weitere Themes laden …* öffnest, *Nach Theme-Updates suchen* wählst oder ein Theme installierst oder aktualisierst, lädt MarsDawn die Theme-Liste, Vorschauen und Theme-Dateien von marsdawn.southern-light.dev herunter. Themes werden nur bei diesen Downloads automatisch aktualisiert, nie im Hintergrund. Die Anfrage enthält kein Konto, keine Kennung, kein Cookie und keine Dokumentdaten; wie bei jeder Webanfrage sieht unser Hoster Cloudflare deine IP-Adresse und welche Dateien angefordert wurden. *Theme melden…* sendet keine Anfrage aus der App: Der Befehl öffnet nur einen GitHub- oder E-Mail-Link in deinem Browser oder deiner Mail-App.

## Siri, Kurzbefehle und Spotlight

MarsDawn bietet Aktionen für Siri, die App „Kurzbefehle“ und Spotlight, etwa zum Erstellen eines Dokuments oder zum Hinzufügen einer Notiz. Wenn du sie verwendest, wird der Text, den du angibst, an MarsDawn auf deinem Mac übergeben und nur dort gesichert, wo die Aktion es angibt (ein neues Dokument oder die Datei `Inbox.md` in dem von dir gewählten Notizordner). Sprache, die du Siri diktierst, verarbeitet Apple gemäß der [Datenschutzrichtlinie von Apple](https://www.apple.com/legal/privacy/).

## Exportieren und Drucken

PDF-Export und Drucken finden auf deinem Mac statt. Das PDF wird dort gesichert, wo du es festlegst. Gedruckt wird über macOS auf dem Drucker, den du auswählst.

## Das Befehlszeilenprogramm marsdawn

Das optionale Befehlszeilenprogramm `marsdawn`, das separat vertrieben wird, läuft ebenfalls vollständig auf deinem Mac. Es liest die Markdown-Datei, die du angibst, und schreibt das PDF, das du anforderst. Bilder aus dem Web lädt es nur, wenn du `--allow-remote-images` übergibst.

## Kinder

Die App MarsDawn erhebt von niemandem Daten, auch nicht von Kindern. Ein auf der Website erfasster Besuch ist kein Konto und wird nicht verwendet, um jemanden zu identifizieren.

## Käufe

MarsDawn wird über den Mac App Store verkauft. Apple wickelt den Kauf nach eigenen Bedingungen ab, und der Entwickler erhält nie deine Zahlungsdaten.

## Änderungen dieser Richtlinie

Falls MarsDawn jemals beginnt, Daten anders zu verarbeiten, wird diese Seite aktualisiert, bevor diese Version erscheint, und das Datum oben ändert sich.

## Kontakt

Fragen zum Datenschutz: [support@southern-light.dev](mailto:support@southern-light.dev)

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): MarsDawn ist ein nativer Markdown-Editor für Mac: Live-Vorschau neben dem Quelltext, Mermaid, KaTeX, Übersicht, PDF-Export. Gratis testen, einmalig 4,99 USD.
- [Deine Texte bleiben auf deinem Mac](https://marsdawn.southern-light.dev/de/yours/index.md): MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.
- [Kostenlos testen, einmal bezahlen](https://marsdawn.southern-light.dev/de/pay-once/index.md): MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.
- [PDF-Export](https://marsdawn.southern-light.dev/de/pdf/index.md): Exportiere Markdown auf deinem Mac als PDF oder drucke es, mit Mermaid-Diagrammen und hervorgehobenem Code. Seitenumbrüche vermeiden es, kurze Codeblöcke und Tabellen zu teilen.
- [Eine Mac-App](https://marsdawn.southern-light.dev/de/native/index.md): Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.
- [Was MarsDawn nicht kann](https://marsdawn.southern-light.dev/de/limits/index.md): Keine Synchronisierung, keine App für iPhone oder iPad, keine Plug-ins, keine Konten. Vier integrierte Themen. Gut zu wissen, bevor du kaufst.
- [Support](https://marsdawn.southern-light.dev/de/support/index.md): Hilfe zu MarsDawn, dem Markdown-Editor für macOS.
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
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [日本語](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Français](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Español](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
- [한국어](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
