# Ein Test, der auf einem Mac besteht, testet vielleicht nicht, was du denkst.

Vibe Coding ist nichts Schlechtes, und auch MarsDawn entsteht mit Agenten. Aber Software, auf die man sich verlässt, wird an dem gemessen, was nach der ersten Version kommt: jahrelange Wartung und Sicherheit, und die beginnen mit der Prüfung, dass eine Änderung nichts kaputt gemacht hat.

**Ein Test bestand auf einem Mac mini und schlug auf einem MacBook Air fehl. Das Produkt war in Ordnung. Der Test hatte Farben durch das Farbprofil des Bildschirms gelesen, und auf dem Mac mini hatte er nur durch Glück bestanden. Ein zweites Gerät fand einen Fehler im Test, nicht im Code.**

Du willst nur wissen, mit welchen extremen oder feindseligen Dateien MarsDawn getestet wird? Dann spring direkt zu [Was wir hineinwerfen](#inputs).

## Der Test, der auf einem MacBook Air fehlschlug

Ein kompletter Durchlauf der Tests der Export-Engine dauert auf dem macOS-15-Runner von GitHub fast eine Stunde: etwa 32 Minuten für den Debug-Build und etwa 25 für den Release-Build. Um das zu verkürzen, haben wir versucht, die macOS-26-Hälfte auf ein eigenes MacBook Air zu verlegen ([kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)).

Beim ersten Lauf dort schlug ein Test fehl. Er exportiert ein PDF mit Hinweisboxen (Note, Tip, Warning) und prüft, ob jede am Rand einen Balken in der richtigen Farbe hat, also mit einem Farbabstand unter 0,16. Auf dem MacBook Air lagen die Abstände bei 0,1634, 0,1648 und 0,1796. Auf einem Mac mini, mit demselben Commit und denselben macOS- und Xcode-Versionen, bestand der Test.

Unser erster Verdacht: Der Export ist kaputt. War er nicht. Mit dem PDF war alles in Ordnung; was sich zwischen den Geräten unterschied, war die Art, wie der Test es las.

Der Test wandelte jede PDF-Seite in ein Bild um und las die Pixel, und macOS zeichnet dieses Bild im Farbraum des Hauptbildschirms. Der Mac mini hing an einem gewöhnlichen externen Monitor, das MacBook Air nutzte sein eingebautes Display. Wir füllten ein Bild mit einem einzigen Orange und lasen es zurück: Aus (0,784; 0,278; 0,106) wurde auf dem Mac mini (0,822; 0,335; 0,179) und auf dem MacBook Air (0,782; 0,395; 0,221).

Jetzt kommt der entscheidende Teil: Auch auf dem Mac mini hatte der Test nicht die richtigen Farben gelesen. Er lag um bis zu 0,128 daneben, knapp innerhalb der Grenze von 0,16. Er bestand wegen des Monitors, nicht weil er den Balken richtig gemessen hätte.

Der Fix ([kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)) ändert nur den Test: Er zeichnet die Seite in ein Bild mit festem sRGB-Farbraum, sodass kein Bildschirm beteiligt ist. Beide Geräte lesen die Balkenfarben jetzt exakt, mit einem Farbabstand von 0,0, auf dem eingebauten Display des MacBook Air genauso wie auf dem Mac mini. Die CI des Pull Requests lief durch ([run 40285279080](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080)), und sobald der Fix den Runner-Zweig des MacBook Air erreichte, bestand dort auch die komplette Testsuite ([run 40315907904](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40315907904)). Dann haben wir ihn absichtlich scheitern lassen: Mit Blau als erwarteter Farbe überall wurde er für alle fünf Hinweisboxen rot.

Eine bekannte Lücke hat er noch. Note und Caution verwenden zwei Orangetöne, die etwa 0,119 auseinanderliegen, also innerhalb der Grenze von 0,16. Würden die beiden vertauscht, würde der Test es wahrscheinlich nicht merken. Das haben wir aufgeschrieben, statt so zu tun, als wäre der Test vollständig.

Ein Test, der nicht fehlschlagen kann, schützt nichts, und einer, der aus dem falschen Grund fehlschlägt, etwa wegen des Farbprofils eines Bildschirms, ebenso wenig. Grün auf einem Gerät heißt nur, dass der Test dort bestanden hat, nicht, dass er misst, was sein Name sagt.

## Tests sind Netze in Schichten

Kein einzelner Test fängt alles. Jede Schicht ist ein Netz mit anderer Maschenweite, und ein Fehler, der durch eines rutscht, sollte im nächsten landen:

- **Referenz-PDFs:** Die Export-Engine (das quelloffene [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit), auf dem auch der Befehl `marsdawn` läuft) exportiert Beispieldokumente, und der Text jeder Seite wird mit einer gespeicherten Fassung verglichen. Das fängt Inhalte, die still verschwinden, oder eine Seitenzahl, die sich ändert.
- **Verschiedene Systeme und Builds:** Die Engine läuft auf macOS 15, der ältesten unterstützten Version, und auf macOS 26, mit dem die App ausgeliefert wird, jeweils als Debug- und als Release-Build. Die komplette Testsuite der App läuft in vier Kombinationen: signiert und unsigniert, jeweils mit ausgeschalteter und eingeschalteter Paywall. Das fängt, was nur auf einem älteren System kaputtgeht oder nur in dem Build, den die Kundschaft tatsächlich bekommt.
- **Echte Hardware:** Die CI der App läuft auf eigenen Macs (sowohl dem Mac mini als auch dem MacBook Air), und der Versuch, die Testsuite der Engine auf diesem MacBook Air laufen zu lassen ([kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240), weiterhin ein offener Entwurf), hat den Farbprofil-Fehler oben gefunden. Ein zweites Gerät fängt Tests, die nur wegen des Geräts bestehen, auf dem sie laufen.
- **Negativkontrollen:** Die CI der App hält 22 absichtlich kaputte Kopien eines Aufräumskripts und 20 eines Test-Runner-Skripts bereit, jeder fehlt eine Sicherheitsprüfung, und die Tests müssen bei jeder einzelnen fehlschlagen. Das Aufräumskript löscht alte Builds und Arbeitskopien auf einem Mac, eine fehlende Prüfung könnte also das Falsche löschen. Besteht eine kaputte Kopie, ist der Test das, was kaputt ist.
- **Ein zweites Paar Augen:** Bei uns prüft in der Regel ein separater Agent eine Änderung, bevor sie zusammengeführt wird, wie bei kit #242, und Änderungen an Abläufen in der App bekommen vorher ein Szenario-Review. Das fängt „fertig“, das es nicht ist, und Code, der funktioniert, aber in der falschen Situation.
- **Zusammenführen tut ein Mensch.** Jede Änderung wird von der Person, die MarsDawn entwickelt, selbst geprüft und zusammengeführt; kein Agent und kein Bot führt etwas zusammen.

## Was wir hineinwerfen

Die Netze sind nur so gut wie das, was hineinkommt. Ein paar der Eingaben, mit denen die Tests die Engine füttern, und was jeder Test sicherstellt:

- **Sehr große Dateien.** Auf unserem Testgerät, im Release-Build gemessen, wird ein 2-MB-Dokument in weniger als anderthalb Sekunden dargestellt, und ein 5-MB-Dokument, das zu komplex für das Layout ist, öffnet sich trotzdem innerhalb einer Sekunde als reiner Text. Alles über 16 MB wird als Text angezeigt, ohne überhaupt geparst zu werden.
- **Hunderttausende Zeilen.** Etwa 3 MB Zeilen mit je einem Wort, knapp 800.000 davon, werden unterwegs als zu viel erkannt: Die Engine hört dort auf zu lesen und zeigt die Datei als reinen Text.
- **Markierungen, die nie schließen.** Ein Megabyte öffnender Abschnittsmarken ohne Gegenstück oder Zehntausende übereinandergestapelte dürfen höchstens etwa doppelt so lange brauchen wie ein Megabyte reiner Text. Ab der achten Ebene wird nichts mehr tiefer verschachtelt.
- **Formeln.** Eine fehlerhafte Formel zeigt an ihrer Stelle einen Fehler, statt die Seite kaputt zu machen. Eine mit mehr als 10.000 Zeichen bleibt, wie sie geschrieben ist, es werden jeweils nur die ersten 1.000 eines Dokuments gezeichnet, und nichts in einer Formel kann zu einem Link, einem Bild oder Seiten-Markup werden.
- **Feindseliges HTML in Markdown.** Skripte werden entfernt und nie ausgeführt, eingebettete Frames werden entfernt, bevor die Seite sie zeigt. Bilder aus dem Netz bleiben aus, solange du sie nicht erlaubst, und auch dann laden nur sichere (HTTPS). In einer Kontrollkopie ist der Skriptfilter entfernt, und der Test muss an ihr fehlschlagen.
- **Eine feindselige Theme-Datei.** Sie wird abgelehnt, und die Fehlermeldung wiederholt nie versteckte Steuerzeichen oder Links aus der Datei. Theme-Dateien über 16 KB werden gar nicht erst gelesen.

Nichts davon ist umsonst. Das Zeitlimit für einen Engine-Lauf ist von 30 Minuten auf 45, dann 50, dann 70 und jetzt auf 90 gestiegen. macOS 15 ist zweimal an das 50-Minuten-Limit gestoßen, obwohl jeder Test bestand, und später im letzten Schritt auf 70 Minuten gekommen, während jeder Schritt davor bestanden hatte.

## Vier Gewohnheiten zum Nachmachen

1. **Trenne den Agenten, der schreibt, von dem, der prüft.** Gib dem prüfenden die Änderung und was „fertig“ heißt, ohne die Erklärung des schreibenden Agenten, und lass ihn die Tests selbst ausführen und sagen, was er nicht geprüft hat. Bei kit #242 ließ der prüfende Agent den alten Test auf dem MacBook Air laufen, um ihn scheitern zu sehen, bevor er den neuen durchgehen ließ. Das kostet die Tokens einer zweiten Sitzung.
2. **Sieh jeden Test einmal fehlschlagen.** Grün ist nur etwas wert, wenn du denselben Test schon rot gesehen hast, als das, was er prüft, wirklich falsch war. Bevor du einem grünen Haken traust, mach also kaputt, was er bewacht (oder lass den Agenten das tun), sieh ihn rot werden, setz es zurück und sieh ihn grün werden. Agenten sind gut darin, Tests zu schreiben, die bestehen; genau deshalb musst du sie scheitern sehen.
3. **Lass deine Tests in einer zweiten Umgebung laufen.** Kein zweiter Mac? Eine CI-Matrix mit zwei OS-Versionen oder mit einem Debug- und einem Release-Build ist ein guter Anfang. Du suchst Tests, die nur zufällig bestehen.
4. **Werte „keine Tests gelaufen“ als Fehlschlag.** `unittest` in Python 3.9 beendet sich erfolgreich, wenn es überhaupt keine Tests findet; ein Tippfehler im Pfad bringt dir also einen grünen Haken. Unsere CI liest die Anzahl, schlägt bei null fehl und prüft, dass die Zusammenfassung „0 failed“ sagt, statt nur auf den Exit-Code zu schauen. Diese Kontrolle kam dazu, nachdem eine unabhängige Verifikation genau diese Lücke in unserer eigenen CI gefunden hatte.

## Kurz gesagt

Ob eine App per Vibe Coding entstanden ist, zählt weniger als die Frage, ob jemand sie weiter testet und pflegt. Das lohnt sich bei der Wahl von Software zu prüfen: Steht irgendwo, wie sie getestet wird, und wann wurde sie zuletzt aktualisiert?

Lass den Agenten schnell sein. Das Prüfen überlass Tests, die das Richtige messen, und einem Menschen, der das Ergebnis liest.

## Weiter

- Warum ein Mensch trotzdem lesen muss, was ein Agent geschrieben hat: [Warum KI-Ergebnisse weiterhin einen menschlichen Leser brauchen](/de/reviewing-ai-output/).
- Wie du die Pläne und Berichte liest, die ein Agent zurückgibt: [Lesen, was dein Agent zurückgibt](/de/reading-agent-output/).

## Quellen

- Der fehlschlagende Test und seine Ursache: [mars-dawn-kit #241](https://github.com/redtear1115/mars-dawn-kit/issues/241).
- Der Fix und seine unabhängige Prüfung: [mars-dawn-kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242).
- Die CI auf einem MacBook Air ausprobieren (offener Entwurf), mit Laufzeiten: [mars-dawn-kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240).
- Die CI der Export-Engine, mit der Geschichte ihres Zeitlimits in den Kommentaren: [ci.yml](https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml).
- Das Repository der App ist privat; die Angaben zur App oben stammen aus ihrem CI-Workflow und ihren Testskripten.

## Mehr

- [MarsDawn](https://marsdawn.southern-light.dev/de/index.md): Lies und prüfe das Markdown deines Agenten nativ auf dem Mac: geteilte Vorschau, Mermaid, KaTeX, Übersicht, PDF-Export. Kostenlos testen, dann einmal 4,99 USD.
- [Funktionen](https://marsdawn.southern-light.dev/de/features/index.md): Nativer Markdown-Editor für den Mac: Live-Vorschau, Mermaid, Formeln, Themes und saubere PDF- und Druckseiten für Besprechungen, Randnotizen und Papierakten.
- [Deine Texte bleiben auf deinem Mac](https://marsdawn.southern-light.dev/de/yours/index.md): MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.
- [Kostenlos testen, einmal bezahlen](https://marsdawn.southern-light.dev/de/pay-once/index.md): MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.
- [PDF-Export](https://marsdawn.southern-light.dev/de/pdf/index.md): Exportiere Markdown auf deinem Mac als PDF oder drucke es, mit Mermaid-Diagrammen und hervorgehobenem Code. Seitenumbrüche vermeiden es, kurze Codeblöcke zu teilen.
- [Eine Mac-App](https://marsdawn.southern-light.dev/de/native/index.md): Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.
- [Was MarsDawn nicht kann](https://marsdawn.southern-light.dev/de/limits/index.md): Keine Synchronisierung, keine iPhone- oder iPad-App, keine Plug-ins, keine Konten. Themen, aber kein eigenes CSS. Vor dem Kauf gut zu wissen.
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
- [English](https://marsdawn.southern-light.dev/how-we-test/index.md): A test passed on one Mac and failed on another. The product was fine; the test was reading the screen's colours. How we layer our tests, and four habits you can copy.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/how-we-test/index.md): 同一個測試，在一台 Mac 通過、在另一台失敗。產品沒壞，是測試讀到了螢幕的色彩。我們怎麼一層一層地測試，以及你也能照做的四個習慣。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/how-we-test/index.md): 同一个测试，在一台 Mac 上通过，在另一台上失败。产品没坏，是测试读到了屏幕的色彩。我们怎么一层一层地测试，以及你也能照做的四个习惯。
- [日本語](https://marsdawn.southern-light.dev/ja/how-we-test/index.md): あるテストが 1 台の Mac では通り、もう 1 台では失敗しました。製品は壊れておらず、テストが画面の色を読んでいたのです。テストを何層にも重ねるやり方と、まねできる 4 つの習慣。
- [Français](https://marsdawn.southern-light.dev/fr/how-we-test/index.md): Un test passait sur un Mac et échouait sur un autre. Le produit allait bien ; le test lisait les couleurs de l’écran. Comment nous superposons nos tests, et quatre habitudes à reprendre.
- [Español](https://marsdawn.southern-light.dev/es/how-we-test/index.md): Una prueba pasaba en un Mac y fallaba en otro. El producto estaba bien; la prueba leía los colores de la pantalla. Cómo apilamos nuestras pruebas, y cuatro hábitos que puedes copiar.
- [한국어](https://marsdawn.southern-light.dev/ko/how-we-test/index.md): 한 Mac에서 통과한 테스트가 다른 Mac에서는 실패했습니다. 제품은 멀쩡했고, 테스트가 화면의 색을 읽고 있었습니다. 테스트를 여러 겹으로 쌓는 방법과 따라 할 수 있는 네 가지 습관.
