# Einen Agentenplan in fünf Minuten prüfen

Dein Agent hat einen Plan geschrieben und wartet auf grünes Licht. Du hast fünf Minuten, keine Stunde. Hier ist ein Weg, sie zu nutzen, der in jedem Editor funktioniert, sogar in einem einfachen Texteditor. MarsDawn hilft bei einigen Schritten, und wir sagen, bei welchen. Beim wichtigsten hilft es nicht.

**Lies den Plan nicht von oben nach unten. Prüfe seine Form, prüfe eine Behauptung, finde, was sich nicht rückgängig machen lässt, sieh dir Diagramme und Umfang an und schreib dann Feedback, mit dem der Agent arbeiten kann. Sechs Schritte, etwa fünf Minuten.**

## Warum vorher prüfen

Chip Huyen erklärt, warum Planung von Ausführung getrennt sein sollte, und benennt die Kosten deutlich: „Ohne Aufsicht kann ein Agent diese Schritte stundenlang ausführen und Zeit und Geld für API-Aufrufe verschwenden, bevor du merkst, dass er nicht vorankommt.“ Unsere Ergänzung: Ein Plan ist der günstigste Ort, einen Fehler zu finden. Eine Zeile in `plan.md` zu korrigieren kostet einen Satz. Zu korrigieren, was der Agent getan hat, nachdem er gelaufen ist, kostet einen Nachmittag.

## Das Beispiel

Du hast einen Agenten gebeten, Benutzer-Avatare in einen Objektspeicher zu verschieben, ohne bestehende Links zu brechen. Er gibt dir das hier zurück:

```
# Plan: move user avatars to object storage

## Goal
Serve avatars from object storage instead of the app server.

## Steps
1. Add a storage client and config. ✅ done
2. Write a script that copies existing avatars to the bucket.
3. Switch the avatar URLs in the templates.
4. Delete `public/avatars/` from the server.
5. Run the copy script.

## Status
All tests pass.
```

Es liest sich gut. Es würde auch jeden Avatar löschen, bevor auch nur einer kopiert ist.

## Die sechs Schritte

**1. Lies nur die Überschriften.** *(etwa eine Minute)* Passt die Gliederung zu dem, worum du gebeten hast? Ein fehlender Abschnitt bedeutet meist fehlende Arbeit. Hier: Goal, Steps, Status. Du wolltest, dass bestehende Links weiter funktionieren, und es gibt keine Überschrift zu alten Links oder dazu, wie man die Änderung rückgängig macht. Das ist dein erster Kommentar.

Im Terminal gibt `grep -n '^#' plan.md` nur die Überschriften aus, und die meisten Editoren können auch eine Gliederung zeigen. In MarsDawn listet der Tab Gliederung in der Seitenleiste (Darstellung ▸ Seitenleiste einblenden, ⌃⌘S) sie auf, und ein Klick springt dorthin.

**2. Finde jede Stelle, die sagt, dass etwas erledigt, bestanden oder geprüft ist, und prüfe eine selbst.** *(etwa eine Minute)* Öffne die Datei, führe den Test aus, zähle die Zeilen. Chip Huyen beschreibt einen Fehler, bei dem „der Agent überzeugt ist, eine Aufgabe erledigt zu haben, obwohl er es nicht hat“. In ihrem Beispiel soll ein Agent 50 Personen auf 30 Hotelzimmer verteilen, bringt 40 unter und besteht darauf, fertig zu sein.

```
grep -n -i -E 'done|pass|verified|✅' plan.md
```

Hier findet das „✅ done“ und „All tests pass.“ Welche Tests? Berührt einer davon die Avatare? Führ sie aus oder frag nach. Diesen Schritt kann MarsDawn dir nicht abnehmen. Das kann niemand außer dir.

**3. Achte auf Schritte, die sich nicht rückgängig machen lassen.** *(etwa eine Minute)* Daten löschen, Migrationen, Force-Pushes, alles, was sendet, bezahlt oder veröffentlicht. Die warten auf dein ausdrückliches Ja. Chip Huyen beschreibt dieselbe Idee von der Seite des Systems aus: „Wenn ein Plan riskante Vorgänge umfasst, etwa eine Datenbank zu aktualisieren oder eine Codeänderung zu mergen, kann das System vor der Ausführung ausdrücklich um menschliche Zustimmung bitten oder die Ausführung dieser Vorgänge Menschen überlassen.“ Hier löscht Schritt 4 die Originale, und er kommt vor Schritt 5, dem Kopieren.

**4. Lies die Diagramme gerendert und prüfe jeden Pfeil gegen den Text.** Ein Flussdiagramm, das „kopieren → prüfen → löschen“ sagt, während die Schritte etwas anderes sagen, ist ein Befund. Dieser Plan hat kein Diagramm, also fällt der Schritt heute weg. Wenn es eines gibt, sieh dir das Bild an, nicht den Mermaid-Quelltext: Viele Editoren haben eine Vorschau, und [Eine Markdown-Datei auf dem Mac ansehen](/de/view-markdown-on-mac/) und [Markdown anderswo ansehen](/de/vs/markdown-preview-tools/) zeigen die Möglichkeiten. In MarsDawn steht das gerenderte Diagramm neben seinem Quelltext (⌘2), und ein fehlerhaftes Diagramm zeigt seinen Quelltext mit dem Fehler darunter, was einen eigenen Kommentar wert ist.

**5. Liste die Dateien und Systeme auf, die der Plan berührt, und frag nach allem, worum du nicht gebeten hast.** *(Schritte 4 und 5 zusammen, etwa eine Minute)* Hier: die Speicherkonfiguration, die Templates, ein Ordner auf dem Server, ein Bucket. Wer kann den Bucket lesen? Du hast nicht gesagt, dass er öffentlich sein soll. Wenn du den Arbeitsordner des Agenten in MarsDawn geöffnet hast (Ablage ▸ Ordner öffnen …, ⇧⌘O), erscheinen neue Dateien, die er schreibt, innerhalb etwa einer Sekunde im Tab Dateien, und die Kopfzeile nennt den Git-Branch oder Worktree, damit du weißt, welchen Checkout du prüfst.

**6. Schreib Feedback als Stelle, Problem, Lösung, ein Problem pro Zeile.** *(die letzte Minute)*

```
plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.
```

Jeder Editor mit Zeilennummern genügt. In MarsDawn kopiert Bearbeiten ▸ Verweis kopieren (⌥⌘C) deine Stelle als `plan.md:10`, und Für KI kopieren (⌃⌥⌘C) fügt den ausgewählten Text darunter ein.

## Wenn du nur eine Minute hast

Mach Schritt 2. Dort fliegt ein Agent auf, der glaubt, fertig zu sein.

## Wenn fünf Minuten nicht reichen

Manchmal kannst du nicht beurteilen, ob ein Schritt richtig ist, weil er außerhalb deines Wissens liegt. Jess Ou bringt es in LangChains Erklärtext über Agenten von 2026 in zwei Sätzen auf den Punkt: „Lagere kein Urteil aus, das du nicht bewerten kannst. Wenn du eine richtige Antwort nicht erkennen würdest, erkennt der Agent sie auch nicht.“ Unsere Folgerung: Wenn du einen Schritt nicht beurteilen kannst, ist das kein Grund, ihn schneller freizugeben. Es ist ein Grund, jemanden zu fragen, der es kann.

## Was MarsDawn hier tut und was nicht

In MarsDawn steckt kein KI-Modell. Es findet die Probleme in diesem Plan nicht und übernimmt weder Schritt 2 noch Schritt 3. Es hält die Datei lesbar, während du arbeitest: die Gliederung für Schritt 1, gerenderte Diagramme für Schritt 4, den Tab Dateien für Schritt 5, Zeilenverweise für Schritt 6. Und wenn der Agent den Plan überarbeitet, während du liest, lädt MarsDawn ihn neu und behält deine Stelle, solange du keine eigenen ungesicherten Änderungen hast.

Wenn der Plan steht und jemand anderes ihn sehen muss, zeigen [Exportierte PDFs teilen](/de/sharing-exported-pdfs/) und [Markdown in PDF](/de/markdown-to-pdf/), wie du ihn als PDF weitergibst.

## Ausprobieren

MarsDawn gibt es im [Mac App Store](https://apps.apple.com/app/id6812925073). Dazu kommt das kostenlose Befehlszeilenwerkzeug `marsdawn`:

```
brew install redtear1115/tap/marsdawn
```

Es exportiert Markdown ohne die App als PDF.

[Befehlszeile](/de/cli/) · Vor dem Kauf wissen: [Was MarsDawn nicht kann](/de/limits/)

## Weiter

- Warum Agentenausgaben überhaupt schwer zu lesen sind: [Lesen, was dein Agent zurückgibt](/de/reading-agent-output/).
- Warum Agenten ihre Pläne überhaupt offenlegen: [Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?](/de/agent-transparency/)
- Pläne sind nicht das Einzige, was Agenten zurückgeben: [Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt](/de/agent-design-patterns/).

## Quellen

- Chip Huyen, „Agents“, 7. Januar 2025: [https://huyenchip.com/2025/01/07/agents.html](https://huyenchip.com/2025/01/07/agents.html)
- Jess Ou, „What is an AI agent?“, LangChain, 31. Juli 2026: [https://www.langchain.com/blog/what-is-an-agent](https://www.langchain.com/blog/what-is-an-agent)

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): Markdown für Menschen, die agentische Arbeit steuern: ein nativer Mac-Editor mit Live-Vorschau, Mermaid-Diagrammen und PDF-Export. Im Mac App Store.
- [Deine Texte bleiben auf deinem Mac](https://marsdawn.southern-light.dev/de/yours/index.md): MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.
- [Kostenlos testen, einmal bezahlen](https://marsdawn.southern-light.dev/de/pay-once/index.md): MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.
- [PDF-Export](https://marsdawn.southern-light.dev/de/pdf/index.md): Exportiere Markdown auf deinem Mac als PDF oder drucke es, mit Mermaid-Diagrammen und hervorgehobenem Code. Seitenumbrüche vermeiden es, kurze Codeblöcke und Tabellen zu teilen.
- [Eine Mac-App](https://marsdawn.southern-light.dev/de/native/index.md): Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.
- [Was MarsDawn nicht kann](https://marsdawn.southern-light.dev/de/limits/index.md): Keine Synchronisierung, keine App für iPhone oder iPad, keine Plug-ins, keine Konten. Vier integrierte Themen. Gut zu wissen, bevor du kaufst.
- [Support](https://marsdawn.southern-light.dev/de/support/index.md): Hilfe zu MarsDawn, dem Markdown-Editor für macOS.
- [Datenschutzrichtlinie](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [Markdown auf dem Mac ansehen](https://marsdawn.southern-light.dev/de/view-markdown-on-mac/index.md): Eine .md-Datei ist reiner Text mit Formatierungszeichen. So liest du sie auf dem Mac gerendert: heute als PDF mit dem kostenlosen Befehlszeilenwerkzeug marsdawn und in der MarsDawn-App aus dem Mac App Store.
- [Markdown zu PDF](https://marsdawn.southern-light.dev/de/markdown-to-pdf/index.md): Wandle Markdown auf dem Mac mit dem kostenlosen Befehlszeilenwerkzeug marsdawn in ein PDF um. Mit Homebrew installieren, einen Befehl ausführen: Tabellen, Mathematik, Mermaid und Code.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/de/vs/macmd-viewer/index.md): MacMD Viewer zeigt Markdown nur zum Lesen an, für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben, kostenlos testen, dann einmalig 4,99 USD im Mac App Store.
- [Befehlszeile](https://marsdawn.southern-light.dev/de/cli/index.md): Das kostenlose Befehlszeilenprogramm marsdawn für den Mac: Markdown aus einer Shell, einem Skript oder einem LLM-Agenten als PDF exportieren, mit JSON-Ausgabe. Installation mit Homebrew.
- [marsdawn für Agenten](https://marsdawn.southern-light.dev/de/cli/agents/index.md): Eine Referenz für KI-Agenten und Skripte, die marsdawn aufrufen, um Markdown in PDF umzuwandeln: Befehle, JSON-Ausgabe, Schemas, Exit-Codes und Voraussetzungen.
- [Agent-Skill](https://marsdawn.southern-light.dev/de/cli/skill/index.md): Eine Datei, die dein Coding-Agent lädt, um geschriebenes Markdown zur Prüfung in MarsDawn zu öffnen, marsdawn zu installieren, Markdown als PDF zu exportieren und das JSON-Ergebnis zu lesen.
- [MCP-Server](https://marsdawn.southern-light.dev/de/cli/mcp/index.md): marsdawn hat kein eigenes KI-Modell, daher ist egal, welcher Agent das Markdown geschrieben hat. Ruf es über die CLI, eine Skill-Datei oder den MCP-Server marsdawn-mcp auf: Alle drei führen denselben Export aus.
- [Review mit wenigen Tokens](https://marsdawn.southern-light.dev/de/token-efficient-review/index.md): Ein Mensch prüft die gerenderte Seite in MarsDawn, sie wird nie in den Kontext des Agenten zurückgelesen. Der Werkzeugaufruf selbst liefert ein kompaktes JSON-Ergebnis statt des gerenderten Inhalts, auch der Aufruf ist also günstig.
- [Markdown anderswo ansehen vs. MarsDawn](https://marsdawn.southern-light.dev/de/vs/markdown-preview-tools/index.md): Wie sich MarsDawn mit dem Lesen von Markdown in der eingebauten Vorschau von VS Code, einer Browsererweiterung oder der Dateivorschau von Claude Desktop vergleicht: was jeweils gerendert wird und was es braucht, eine Datei zu öffnen.
- [Vorschau-Themen und PDF-Export](https://marsdawn.southern-light.dev/de/themes/index.md): Vier Vorschauthemen mit je einer hellen und einer dunklen Palette und ein PDF- und Druckexport, der zum gewählten Thema passt. Weitere importierbare Themen und eine Galerie zum Teilen eigener Themen sind geplant.
- [Exportierte PDFs teilen](https://marsdawn.southern-light.dev/de/sharing-exported-pdfs/index.md): Exportiere das Markdown eines Agenten als PDF und gib es einer Kollegin, die kein Markdown liest und nichts installieren wird. Zum Öffnen braucht es keine Syntax, keine App und keinen Account.
- [Warum KI-Ergebnisse weiterhin einen menschlichen Leser brauchen](https://marsdawn.southern-light.dev/de/reviewing-ai-output/index.md): Von KI geschriebenes Markdown muss ein Mensch verstehen, nicht auf den ersten Blick glauben. MarsDawn stellt die gerenderte Seite neben den Quelltext und zeichnet Mermaid-Diagramme und KaTeX-Formeln, damit die Struktur auf einen Blick lesbar ist.
- [Lesen, was dein Agent zurückgibt](https://marsdawn.southern-light.dev/de/reading-agent-output/index.md): KI-Agenten geben ihre Arbeit als Markdown zurück: Pläne, Spezifikationen, Fortschrittsberichte. Was Leute, die Agenten bauen, über Checkpoints und Fehler sagen, warum diese Ausgabe schwer zu lesen ist, und eine Checkliste, um einen Plan in fünf Minuten zu prüfen.
- [Transparenz von Agenten](https://marsdawn.southern-light.dev/de/agent-transparency/index.md): Anthropics Leitfaden zum Bau von Agenten verlangt Transparenz: Zeig die Planungsschritte. Was er sagt, was nicht, und warum die Schritte meist als Markdown-Datei enden, die jemand lesen muss.
- [Entwurfsmuster für Agenten](https://marsdawn.southern-light.dev/de/agent-design-patterns/index.md): Reflexion, Werkzeugnutzung, Planung und Zusammenarbeit mehrerer Agenten, wie Andrew Ng sie beschrieben hat, und was jedes Muster dir typischerweise zum Lesen zurückgibt.
- [Änderungsprotokoll](https://marsdawn.southern-light.dev/de/changelog/index.md): Was sich im kostenlosen Befehlszeilenprogramm marsdawn geändert hat.
- [Vorlagen](https://marsdawn.southern-light.dev/de/templates/index.md): Markdown-Vorlagen für die Dokumente, die ein Agent schreibt und du liest: eine Spezifikation, ein Flussdiagramm und ein Protokoll, jeweils mit einem Prompt für deinen Agenten.
- [Spezifikationsvorlage](https://marsdawn.southern-light.dev/de/templates/spec/index.md): Eine Markdown-Vorlage für Spezifikationen mit Anforderungen, einem Mermaid-Ablaufdiagramm und Akzeptanzkriterien. Dein Agent füllt sie aus, du prüfst sie in MarsDawn.
- [Flussdiagramm-Vorlage](https://marsdawn.southern-light.dev/de/templates/flowchart/index.md): Eine Mermaid-Flussdiagramm-Vorlage in Markdown, darunter die Schritte ausgeschrieben. Auf dem Mac in der Vorschau ansehen und als PDF exportieren.
- [Protokollvorlage](https://marsdawn.southern-light.dev/de/templates/meeting-notes/index.md): Eine Markdown-Vorlage für Besprechungsprotokolle mit Entscheidungen und Aufgaben, jeweils mit einer verantwortlichen Person. Dein Agent schreibt es, du prüfst es in MarsDawn.
- [English](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/reviewing-agent-plans/index.md): agent 交出計畫、還沒開始執行之前，用六個步驟、大約五分鐘把它審完。什麼編輯器都能用，附一份實際的例子。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/reviewing-agent-plans/index.md): agent 交出计划、还没开始执行之前，用六个步骤、大约五分钟把它审完。什么编辑器都能用，附一份实际的例子。
- [日本語](https://marsdawn.southern-light.dev/ja/reviewing-agent-plans/index.md): AI エージェントが実行前に渡してくる計画を、どのエディタでも使える 6 ステップの方法で、実例を交えて約 5 分でレビューする。
- [Français](https://marsdawn.southern-light.dev/fr/reviewing-agent-plans/index.md): Une méthode en six étapes pour relire le plan qu’un agent IA vous remet avant qu’il ne s’exécute, en cinq minutes environ et dans n’importe quel éditeur, avec un exemple détaillé.
- [Español](https://marsdawn.southern-light.dev/es/reviewing-agent-plans/index.md): Un método de seis pasos para revisar el plan que te entrega un agente de IA antes de que se ejecute, en unos cinco minutos y en cualquier editor, con un ejemplo detallado.
- [한국어](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
