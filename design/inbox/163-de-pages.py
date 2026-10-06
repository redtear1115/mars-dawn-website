"""German (de) page copy for the MarsDawn site, tranche 2 (#163).

Same shape as scripts/copy_ja.py: build(k) returns the tables build_pages.py keeps per locale.
Translated from the en copy on main @ 6fe8435. Address: du, as in the app. UI terms follow the
app's de strings (release/1.1.0): Übersicht (Quick Look), Ablage, Darstellung, Sichern, Thema,
Kurzbefehle, Test (trial), freischalten (unlock). Built-in theme names stay English.
Tables that live inline in build_pages.py (HOME, COMPARE_TABLES["pay-once-states"],
EXIT_TABLE_HEAD, EXIT_REMEDY, FIGURES) are returned under their own keys for #162 to merge.
"""


def build(k) -> dict:
    pages = {}
    pages['index'] = {
        "title": 'MarsDawn: ein Markdown-Editor für den Mac, mit Live-Vorschau',
        "description": 'Markdown für Menschen, die agentische Arbeit steuern: ein nativer Mac-Editor mit Live-Vorschau, Mermaid-Diagrammen und PDF-Export. Im Mac App Store.',
        "intro": """
<section class="intro hero">
  <p class="kicker">Pionierwerkzeug für alle, die bauen</p>
  <h1><span>Sichere dir die Karte.</span> <span>Lies das Morgenrot.</span></h1>
  <p>Markdown für Menschen, die agentische Arbeit steuern.</p>
</section>
""",
        "body": """
<h2 class="loop-title">Lies, was dein Agent geschrieben hat.</h2>
<ol class="loop-steps">
  <li><strong>Der Agent schreibt.</strong> Dein Coding-Agent oder Schreibassistent entwirft das Markdown: ein README, eine Spezifikation, ein paar Notizen.</li>
  <li><strong>Du prüfst in MarsDawn.</strong> Öffne die Datei und lies sie gerendert, mit Mermaid-Diagrammen und hervorgehobenem Code, neben dem Quelltext.</li>
  <li><strong>Der Agent überarbeitet.</strong> Bitte um Änderungen. Öffne die überarbeitete Datei und lies sie auf dieselbe Weise.</li>
</ol>
<p><a href="/de/reading-agent-output/">So prüfst du, was dein Agent zurückgibt</a>.</p>
""",
    }
    pages['yours'] = {
        "title": 'Ein Markdown-Editor für den Mac ohne Konto und ohne Cloud · MarsDawn',
        "description": 'MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Deine Markdown-Dokumente bleiben auf deinem Mac, in den Dateien und Ordnern, die du wählst.',
        "intro": """
<section class="intro">
  <h1>Deine Texte bleiben auf deinem Mac.</h1>
  <p>MarsDawn hat kein Konto, keine Synchronisierung und keine Cloud. Es öffnet eine Datei, du schreibst, und es sichert die Datei dort, wo du es festgelegt hast.</p>
</section>
""",
        "body": """
<h2>Was das bedeutet</h2>
<ul>
  <li>Es gibt kein Konto, für das du dich registrieren oder bei dem du dich anmelden musst.</li>
  <li>Nichts wird mit einer Cloud synchronisiert. Deine Dokumente bleiben dort, wo du sie sicherst.</li>
  <li>Nichts wird getrackt. MarsDawn erhebt keinerlei Daten über dich, und das Datenschutzetikett im App Store lautet „Keine Daten erfasst“.</li>
  <li>Bilder aus dem Web bleiben blockiert, bis du sie laden lässt. Wenn du ein Dokument öffnest, erfährt also kein Server, dass du es liest. Lädst du sie doch, dann nur über https.</li>
  <li>Lokale Bilder erscheinen in der Vorschau, sobald du Zugriff auf ihren Ordner erlaubst.</li>
</ul>
<p>Die Einzelheiten stehen in der <a href="/de/privacy/">Datenschutzrichtlinie</a>.</p>
""",
    }
    pages['pay-once'] = {
        "title": 'Kostenlos testen, dann einmal bezahlen · MarsDawn',
        "description": 'MarsDawn ist kostenlos zum Herunterladen. Teste alles 14 Tage lang und schalte es dann einmalig für 4,99 USD frei. Kein Abo, kein Konto.',
        "intro": """
<section class="intro">
  <h1>Teste alles. Dann bezahl einmal.</h1>
  <p>MarsDawn ist ein kostenloser Download. Starte den 14-tägigen Test, und alle Funktionen sind verfügbar. Wenn du es danach weiter nutzen möchtest, schaltet ein einmaliger Kauf für 4,99 USD es frei. Es gibt kein Abo und kein Konto.</p>
</section>
""",
        "body": """
<h2>So funktioniert es</h2>
<ol class="loop-steps">
  <li><strong>Kostenlos laden.</strong> MarsDawn kannst du kostenlos aus dem Mac App Store laden.</li>
  <li><strong>14 Tage lang alles testen.</strong> Starte den Test, und alles in MarsDawn funktioniert 14 Tage lang: jedes Thema und jedes Layout, PDF-Export und Drucken sowie die Aktionen für Siri und Kurzbefehle. Die Übersicht im Finder funktioniert mit und ohne Test.</li>
  <li><strong>Einmal freischalten.</strong> Wenn du es danach weiter nutzen möchtest, schalte es einmalig für 4,99 USD frei. Das ist ein In-App-Kauf, kein Abo: Nichts verlängert sich, und später wird dir nichts berechnet.</li>
</ol>
<ul>
  <li>Auch der Test kostet nichts. Wenn er endet, wird nichts gekauft, es sei denn, du entscheidest dich für die Freischaltung.</li>
  <li>Es gibt kein Konto. MarsDawn verlangt nie, dass du eines anlegst.</li>
</ul>
<h2>Was wann funktioniert</h2>
<!--compare:pay-once-states-->
<p>Bevor du den Test startest, zeigt MarsDawn das Testangebot an. Der Start kostet nichts.</p>
<p>PDF-Dateien, die du in MarsDawn öffnest, werden nach dem Ende des Tests auf dieselbe Weise gesperrt.</p>
<h2>Wenn du nicht freischaltest</h2>
<ul>
  <li>Nach 14 Tagen kannst du Dokumente in MarsDawn nicht mehr lesen, bearbeiten, exportieren oder drucken, bis du freischaltest. Ein Dokument öffnet sich weiterhin, aber sein Inhalt ist verdeckt.</li>
  <li>Deine Dateien ändern sich nicht. Sie sind gewöhnliche Dateien auf deinem Mac, und die Übersicht im Finder zeigt sie weiterhin.</li>
  <li>Das kostenlose <a href="/de/cli/">Befehlszeilenprogramm <code>marsdawn</code></a> exportiert sie weiterhin als PDF, mit oder ohne Test.</li>
  <li>Ist beim Ende des Tests ein Dokument in MarsDawn geöffnet, geht der eingegebene Text nicht verloren: Sichere ihn mit „Ablage“ ▸ „Sichern unter …“.</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": 'Markdown auf dem Mac als PDF exportieren, mit Diagrammen · MarsDawn',
        "description": 'Exportiere Markdown auf deinem Mac als PDF oder drucke es, mit Mermaid-Diagrammen und hervorgehobenem Code. Seitenumbrüche vermeiden es, kurze Codeblöcke und Tabellen zu teilen.',
        "intro": """
<section class="intro">
  <h1>Das PDF sieht aus wie die Seite, die du geschrieben hast.</h1>
  <p>Als PDF exportieren oder drucken, in den hellen Farben deines Themas. Diagramme und hervorgehobener Code bleiben erhalten, und Seitenumbrüche trennen nicht, was zusammengehört.</p>
</section>
""",
        "body": """
<h2>Was das bedeutet</h2>
<ul>
  <li>Mermaid-Diagramme werden ins PDF gezeichnet.</li>
  <li>Codeblöcke behalten ihre Syntaxhervorhebung.</li>
  <li>Seitenumbrüche vermeiden es, eine Überschrift unten auf einer Seite stehen zu lassen oder Code, Tabellen und Diagramme zu teilen.</li>
  <li>In jedem Layout. Der Export funktioniert auch, wenn nur der Quelltext angezeigt wird.</li>
</ul>
<p>Das kostenlose <a href="/de/cli/">Befehlszeilenprogramm marsdawn</a> verwendet denselben Exporter, sodass ein Skript oder ein KI-Agent dasselbe PDF erhält.</p>
""",
    }
    pages['native'] = {
        "title": 'Eine native Markdown-App für den Mac: Tabs, Übersicht · MarsDawn',
        "description": 'Ein Markdown-Editor, der eine echte Mac-App ist: native Fenster und Tabs, automatisches Sichern, Versionsverlauf, Übersicht im Finder und ein Texteditor, der sich wie ein Mac verhält.',
        "intro": """
<section class="intro">
  <h1>Gebaut aus den eigenen Teilen des Mac.</h1>
  <p>Fenster, Tabs, Menüs und Texteditor sind die des Mac. Die gerenderte Seite zeichnet WebKit, die Engine hinter Safari.</p>
</section>
""",
        "body": """
<h2>Was das bedeutet</h2>
<h3>Bearbeiten</h3>
<ul>
  <li>Quelltext, geteilte Ansicht und Vorschau, nur einen Tastendruck voneinander entfernt (<kbd>⌘1</kbd>, <kbd>⌘2</kbd>, <kbd>⌘3</kbd>).</li>
  <li>Die beiden Bereiche scrollen gemeinsam, sodass der Absatz, den du bearbeitest, im Blick bleibt.</li>
  <li>Markdown-Syntaxhervorhebung im Editor, passend zu deinem Vorschau-Thema.</li>
</ul>
<h3>Der Rest des Mac</h3>
<ul>
  <li>Native Fenster, Tabs, automatisches Sichern und Versionsverlauf.</li>
  <li>Übersicht: Drücke im Finder die Leertaste auf einer Markdown-Datei, um eine Vorschau zu sehen, Diagramme inklusive.</li>
  <li>Siri und Kurzbefehle: ein neues Dokument aus einer Vorlage beginnen, eine Zeile zum Notizeingang hinzufügen oder ein zuletzt benutztes Dokument wieder öffnen.</li>
  <li>Englisch, traditionelles Chinesisch, vereinfachtes Chinesisch, Japanisch, Deutsch, Französisch, Spanisch und Koreanisch.</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": 'Was MarsDawn nicht kann · MarsDawn',
        "description": 'Keine Synchronisierung, keine App für iPhone oder iPad, keine Plug-ins, keine Konten. Vier integrierte Themen. Gut zu wissen, bevor du kaufst.',
        "intro": """
<section class="intro">
  <h1>Was MarsDawn nicht kann.</h1>
  <p>Manches fehlt mit Absicht. Wenn du etwas davon brauchst, ist es besser, es jetzt zu wissen als nach dem Kauf.</p>
</section>
""",
        "body": """
<h2>Bewusst weggelassen</h2>
<h3>Geräte und Personen</h3>
<ul>
  <li><strong>Synchronisierung:</strong> MarsDawn synchronisiert deine Dokumente nicht. Sie bleiben dort, wo du sie sicherst. Um eines auf einem anderen Mac zu verwenden, lege es in einen Ordner, den du ohnehin synchronisierst.</li>
  <li><strong>iPhone und iPad:</strong> Dafür gibt es keine App; MarsDawn ist für den Mac.</li>
  <li><strong>Teilen:</strong> Es gibt keine Konten und keine gemeinsame Bearbeitung, denn MarsDawn ist für eine Person an ihrem eigenen Mac.</li>
  <li><strong>System:</strong> MarsDawn benötigt macOS 26 oder neuer.</li>
</ul>
<h3>Dateien und Funktionen</h3>
<ul>
  <li><strong>Bearbeiten:</strong> Du schreibst links Markdown und liest rechts die Seite; die Seite selbst lässt sich nicht bearbeiten.</li>
  <li><strong>Formate:</strong> MarsDawn exportiert PDF und druckt, exportiert aber keine Word-Dateien.</li>
  <li><strong>Andere Dateien:</strong> Reine Textdateien und PDFs werden schreibgeschützt geöffnet.</li>
  <li><strong>Themen:</strong> Enthalten sind Dawn, Classic, Modern und Vivid, jeweils hell und dunkel, und andere lassen sich noch nicht installieren; was geplant ist, steht unter <a href="/de/themes/">Vorschau-Themen und PDF-Export</a>.</li>
  <li><strong>Plug-ins:</strong> MarsDawn hat keine Plug-ins oder Erweiterungen.</li>
</ul>
<h2>Nach dem Test</h2>
<p>Wenn du MarsDawn nach dem Ende des 14-tägigen Tests nicht freischaltest, kannst du darin keine Dokumente mehr lesen, bearbeiten, exportieren oder drucken: Sie öffnen sich mit verdecktem Inhalt. Deine Dateien bleiben, wie sie sind, die Übersicht zeigt sie weiterhin, und das kostenlose Befehlszeilenprogramm exportiert sie weiterhin. Die <a href="/de/pay-once/">Seite zu Test und Freischaltung</a> stellt alle drei Phasen nebeneinander.</p>
""",
    }
    pages['changelog'] = {
        "title": 'Änderungsprotokoll · MarsDawn',
        "description": 'Was sich im kostenlosen Befehlszeilenprogramm marsdawn geändert hat.',
        "body": """
<section class="intro">
  <h1>Änderungsprotokoll</h1>
  <p>Was sich im kostenlosen Befehlszeilenprogramm marsdawn geändert hat. Ein Build von MarsDawn aus dem Mac App Store wird hier nur erwähnt, wenn er eine eigene Zeile hat. Versionen vor 0.5.1 sind nicht aufgeführt.</p>
</section>

<h2>marsdawn 0.6.3</h2>
<p>6. Oktober 2026. MarsDawn ist im Mac App Store.</p>
<ul>
  <li>Wenn die App nicht installiert ist, verweist <code>marsdawn open</code> auf MarsDawn im Mac App Store.</li>
  <li>Das README und der Agent-Skill erklären <code>marsdawn open .</code> und <code>--folder</code>: MarsDawn 1.0.0 zeigt den Ordner in der Seitenleiste des Fensters.</li>
</ul>

<h2>marsdawn 0.5.4</h2>
<p>26. September 2026. Mermaid-Korrekturen, Zeilenangaben bei Diagrammfehlern und die Installation des Skills.</p>
<ul>
  <li>In einem Sequenzdiagramm bleibt eine Nachrichtenbeschriftung, die die Lebenslinien anderer Teilnehmer kreuzt, lesbar, in der Vorschau und in exportierten PDFs.</li>
  <li><code>marsdawn export</code> kommt mit Dokumenten voller Mermaid-Diagramme zurecht. Eines mit 50 Diagrammen, das früher mit Exit-Code 5 scheiterte, wird jetzt exportiert.</li>
  <li><code>marsdawn export --json</code> ergänzt <code>diagramErrorDetails</code> mit Zeilennummern für jeden Diagrammfehler: wo das Diagramm in deinem Dokument beginnt und, wenn Mermaid eine nennt, die Zeile des Fehlers selbst.</li>
  <li><code>marsdawn skill --install</code> installiert den Agent-Skill für Claude Code unter <code>~/.claude/skills/marsdawn/SKILL.md</code> oder mit <code>--dir</code> in einem anderen Ordner. Eine identische Datei lässt es unangetastet, eine abweichende ersetzt es nur mit <code>--force</code>. Andernfalls endet es mit Exit-Code 64 (<code>skill_differs</code>) und ändert nichts.</li>
</ul>

<h2>marsdawn 0.5.3</h2>
<p>25. September 2026. Ordnerstatus, vollständige Mermaid-Fehler und kleinere Korrekturen.</p>
<ul>
  <li><code>marsdawn open --folder</code> kann melden, was mit dem Ordner passiert ist. Bei einer App, die Rückmeldung gibt, wartet es bis zu <code>--wait</code> Sekunden (standardmäßig 2), und <code>--json</code> liefert einen Status wie <code>attached</code> oder <code>needsUser</code>.</li>
  <li>Ein Mermaid-Diagramm, das sich nicht parsen lässt, zeigt die vollständige Fehlermeldung von Mermaid statt nur ihrer ersten Zeile, mit der Zeilennummer vom Anfang deines Dokuments aus gezählt.</li>
  <li>Die Suche nach dem Ende eines Front-Matter-Blocks hört nach 1.000 Zeilen auf, sodass ein nicht geschlossener Block nicht mehr bedeutet, den Rest eines großen Dokuments zu durchsuchen.</li>
  <li>Eine App kann dem Rücklink einer Fußnote für PDF-Export und Drucken eine übersetzte Beschriftung geben. Die Beschriftung wird nicht auf die Seite gedruckt, und <code>marsdawn export</code> behält die englische.</li>
  <li>Das mitgelieferte highlight.js ist jetzt nach Version, Quelle und SHA-256 festgelegt, wie KaTeX und Mermaid.</li>
</ul>

<h2>marsdawn 0.5.2</h2>
<p>24. September 2026. Fußnoten, Kontrast und Ordner.</p>
<ul>
  <li>Fußnoten werden in exportierten PDFs dargestellt: nummerierte Verweise, die Anmerkungen nach dem Haupttext.</li>
  <li>Jedes Thema erfüllt den WCAG-AA-Kontrast, hell und dunkel. Classic ist jetzt schwarz-weiß.</li>
  <li><code>marsdawn skill</code> gibt den Agent-Skill aus, der zum installierten marsdawn passt.</li>
  <li><code>marsdawn open</code> endet mit Exit-Code 6 (<code>app_cannot_open_folders</code>), wenn das gefundene MarsDawn keinen Ordner anzeigen kann, statt Erfolg zu melden.</li>
  <li>Die Platzhalter, die in exportierte Seiten gezeichnet werden, gibt es jetzt auch auf Deutsch, Französisch, Spanisch und Koreanisch.</li>
  <li>Ein Bildplatzhalter zeigt hinter einem sehr langen relativen Pfad nicht mehr den absoluten Pfad.</li>
  <li><code>MARSDAWN_APP_PATH</code> wird nur verwendet, wenn es auf eine MarsDawn-App zeigt.</li>
</ul>

<h2>marsdawn 0.5.1</h2>
<p>19. September 2026. PDF-Export und das Öffnen einer Datei über die Befehlszeile.</p>
<ul>
  <li>Die Textebene eines exportierten PDFs ist für Chinesisch, Japanisch und Koreanisch repariert.</li>
  <li><code>marsdawn open --background</code> öffnet eine Datei, ohne MarsDawn in den Vordergrund zu holen.</li>
  <li><code>marsdawn open</code> kann ein Ordner übergeben werden, und MarsDawn zeigt ihn in der Seitenleiste des Fensters (ab MarsDawn 1.0.0).</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn: ein kostenloses Befehlszeilenprogramm für Markdown zu PDF · MarsDawn',
        "description": 'Das kostenlose Befehlszeilenprogramm marsdawn für den Mac: Markdown aus einer Shell, einem Skript oder einem LLM-Agenten als PDF exportieren, mit JSON-Ausgabe. Installation mit Homebrew.',
        "body": f"""
<section class="intro">
  <h1>Befehlszeile</h1>
  <p>Das kostenlose Befehlszeilenprogramm <code>marsdawn</code>: Markdown aus einer Shell oder einem LLM-Agenten als PDF exportieren und, wenn die App MarsDawn installiert ist, Dateien darin öffnen.</p>
</section>

<div class="summary"><p><strong>marsdawn ist kostenlos und wird getrennt vom Mac App Store vertrieben.</strong> Installiere es mit Homebrew: Auf einem Mac mit Apple Chip ist es sofort einsatzbereit. <code>export</code> funktioniert eigenständig; <code>open</code> braucht die App MarsDawn.</p></div>

<p>Du rufst marsdawn aus einem KI-Agenten oder einem Skript auf? Unter <a href="/de/cli/agents/">marsdawn für Agenten</a> findest du die JSON-Ausgabe, ihre Schemas und alle Exit-Codes, oder unter <a href="/de/cli/mcp/">MCP-Server</a>, wenn dein Agent Tools stattdessen über MCP aufruft.</p>

<h2>Installation</h2>
<p>Mit <a href="https://brew.sh">Homebrew</a>:</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>Du nutzt einen Coding-Agenten? <a href="/de/cli/skill/">Füge den marsdawn-Skill hinzu</a>: eine Datei, die ihm beibringt, das Geschriebene zur Prüfung in MarsDawn zu öffnen und PDFs zu exportieren.</p>
<p>Auf einem Mac mit Apple Chip installiert Homebrew in Sekunden eine vorkompilierte Version, ohne dass sonst etwas installiert werden muss. Auf einem Intel-Mac kompiliert es marsdawn stattdessen aus dem Quellcode. Das dauert ein paar Minuten und erfordert Xcode 26 oder neuer (Swift 6.2). Das Programm läuft unter macOS 15 oder neuer.</p>
<p>Oder kompiliere es mit dem Swift Package Manager aus dem <a href="{k.KIT_URL}">Quellcode</a>:</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>Welche Version du hast, zeigt <code>marsdawn --version</code>.</p>

<h2>Befehle</h2>

<h3>marsdawn open</h3>
<p>Öffnet eine oder mehrere Markdown-Dateien zur Prüfung in der App MarsDawn. Dafür muss die App installiert sein: Ohne sie endet <code>marsdawn open</code> mit Code 3 und meldet, dass MarsDawn nicht installiert ist. <code>export</code> braucht die App nicht. Die App gibt es im <a href="{k.LISTING_URL}">Mac App Store</a>.</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .</code></pre>
<ul>
  <li><code>path:line</code>: bittet MarsDawn, zu dieser Zeile zu springen. Eine Spalte dahinter, wie in <code>notes.md:120:8</code>, wird ignoriert. Gibt es eine Datei mit dem vollständigen Namen, ist das Argument diese Datei.</li>
  <li><code>--line &lt;n&gt;</code>: dasselbe für eine einzelne Datei, und der Weg, eine Zeile für einen Pfad anzugeben, der selbst auf einen Doppelpunkt und Ziffern endet. Erfordert genau eine Datei.</li>
  <li>Zeilen reichen von 1 bis 999999999.</li>
  <li>MarsDawn 1.0 öffnet die Datei in dieser Zeile.</li>
  <li>Ein Ordner als Argument wird in der Seitenleiste des Fensters geöffnet statt als Dokument: <code>marsdawn open .</code> zeigt den aktuellen Ordner. <code>--folder &lt;path&gt;</code> macht dasselbe zusätzlich zu Dateien. Die Seitenleiste eines Fensters zeigt einen Ordner, zwei anzugeben ist daher ein Bedienungsfehler.</li>
  <li><code>--background</code>: öffnen, ohne MarsDawn in den Vordergrund zu holen.</li>
  <li><code>--json</code>: ein JSON-Ergebnis statt Text ausgeben.</li>
</ul>
<p>Zeilen kamen mit marsdawn 0.3.0 hinzu, Ordner und <code>--background</code> mit 0.5.1.</p>

<h3>marsdawn export</h3>
<p>Rendert eine Markdown-Datei als PDF mit Seiten, mit demselben Exporter, den der PDF-Export von MarsDawn selbst verwendet. Die App MarsDawn wird dafür nicht gebraucht. Relative Bilder werden vom Ordner der Eingabedatei aus aufgelöst.</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: wohin das PDF geschrieben wird. Standard ist der Eingabepfad mit der Endung <code>.pdf</code>.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: die helle Palette des Vorschau-Themas. Standard ist <code>$MARSDAWN_THEME</code>, dann <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: Papierformat. Standard ist <code>a4</code>.</li>
  <li><code>--allow-remote-images</code>: beim Rendern Bilder aus dem Web laden. Standardmäßig aus.</li>
  <li><code>--force</code>: die Ausgabedatei ersetzen, falls sie schon existiert.</li>
  <li><code>--json</code>: ein JSON-Ergebnis statt Text ausgeben.</li>
</ul>

<h2>Die Variable $MARSDAWN_THEME</h2>
<p>Wird <code>--theme</code> nicht übergeben, liest <code>export</code> die Umgebungsvariable <code>$MARSDAWN_THEME</code>. Ihr Wert muss <code>dawn</code>, <code>classic</code>, <code>modern</code> oder <code>vivid</code> sein; alles andere fällt auf <code>dawn</code> zurück. Die CLI liest nicht die Thema-Einstellung der App, weil das Lesen des Containers einer anderen App eine Datenschutzabfrage von macOS auslösen kann.</p>

<h2>Dateien überschreiben</h2>
<p><code>export</code> ersetzt keine vorhandene Ausgabedatei, es sei denn, du übergibst <code>--force</code>.</p>

<h2>Exit-Codes</h2>
<!--exit-table-->
<ul>
  <li><code>0</code>: Erfolg.</li>
  <li><code>2</code>: Eingabe nicht gefunden.</li>
  <li><code>3</code>: MarsDawn ist nicht installiert (nur <code>open</code>).</li>
  <li><code>4</code>: Ausgabe existiert bereits (<code>--force</code> übergeben).</li>
  <li><code>5</code>: Export fehlgeschlagen.</li>
  <li><code>6</code>: Dieses MarsDawn kann keinen Ordner anzeigen, daher wurde nichts geöffnet (nur <code>open</code>).</li>
  <li><code>64</code>: Bedienungsfehler, etwa eine Zeile außerhalb des Bereichs, <code>--line</code> mit mehr als einer Datei oder mit einem Ordner, oder mehr als ein Ordner.</li>
</ul>

<h2>--json-Ausgabe</h2>
<p>Bei Erfolg gibt <code>marsdawn open --json</code> <code>ok</code>, <code>opened</code> (eine Liste mit dem <code>path</code> jeder Datei, dazu <code>line</code>, wenn eine Zeile angefragt wurde), <code>app</code> (den Pfad der App) und, wenn ein Ordner angegeben wurde, <code>folder</code> aus. <code>marsdawn export --json</code> gibt <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> und <code>diagramErrors</code> aus. Bei einem Fehler geben beide <code>ok</code>, <code>error</code> und <code>message</code> aus.</p>
""",
    }

    figures = {
        'index': {"alt": 'MarsDawn in geteilter Ansicht: links der Markdown-Quelltext, rechts die gerenderte Seite.', "callouts": []},
        'yours': {"alt": 'MarsDawn zeigt ein Dokument im Thema Classic, die Vorschau füllt das Fenster.',
                  "callouts": ['Eine Datei auf deinem Mac, gesichert, wo du willst.', 'Die ganze Symbolleiste besteht aus Themen und Layouts; anmelden musst du dich nirgends.']},
        'pay-once': {"alt": 'MarsDawn im Thema Vivid, links der Markdown-Quelltext, rechts die gerenderte Seite.',
                     "callouts": ['Markdown-Hervorhebung im Editor, inklusive.', 'Jedes Thema und jedes Layout ist enthalten.', 'Mermaid-Diagramme, inklusive.', 'Code-Hervorhebung, inklusive.']},
        'pdf': {"alt": 'Ein aus MarsDawn exportiertes PDF, geöffnet in seinem PDF-Viewer mit Seitenminiaturen.',
                "callouts": ['Mermaid-Diagramme, ins PDF gezeichnet.', 'Code behält seine Hervorhebung.']},
        'native': {"alt": 'MarsDawn in geteilter Ansicht: links der Markdown-Quelltext, rechts die gerenderte Seite.',
                   "callouts": ['Ein natives Mac-Fenster.', 'Der Texteditor des Mac, mit Markdown-Hervorhebung.', '⌘1 Quelltext, ⌘2 geteilt, ⌘3 Vorschau.', 'Die Seite aktualisiert sich beim Tippen.']},
        'limits': {"alt": 'MarsDawn im dunklen Modus, links der Markdown-Quelltext, rechts die gerenderte Seite.',
                   "callouts": ['Ein Dokument pro Fenster, auf diesem Mac.', 'Hier schreibst du Markdown.', 'Die Symbolleiste enthält Themen und Layouts, und es gibt kein Plug-in-Menü.', 'Die Seite ist zum Lesen da, nicht zum Bearbeiten.']},
    }
    home = {
        "cta_cli": 'Kostenlose CLI installieren',
        "cta_store": 'Im Mac App Store ansehen',
        "install_h": 'Gleich loslegen',
        "install_lede": 'Das kostenlose Befehlszeilenprogramm <code>marsdawn</code> ist schon heute verfügbar. Installiere es mit Homebrew:',
        "install_caps": [
            '<code>marsdawn export</code> macht aus einer Markdown-Datei ein PDF, gerendert wie die Vorschau von MarsDawn. Die App braucht es dafür nicht.',
            '<code>marsdawn open</code> öffnet Dateien in der App MarsDawn, damit du sie prüfen kannst.',
            '<code>--json</code> liefert Skripten und Agenten Ergebnisse, die sie parsen können.',
        ],
        "proof_h": 'Die App, wie sie ist',
    }
    compare_tables = {
        'pay-once-states': {
            "head": ['', 'Test (Tag 1–14)', 'Test beendet, nicht freigeschaltet', 'Freigeschaltet'],
            "rows": [
                ['Ein Dokument in MarsDawn öffnen', 'Ja', 'Öffnet sich, Inhalt verdeckt', 'Ja'],
                ['In MarsDawn lesen und bearbeiten (Quelltext, Vorschau, Mermaid, Formeln)', 'Ja', 'Nein', 'Ja'],
                ['Aus MarsDawn als PDF exportieren und drucken', 'Ja', 'Nein', 'Ja'],
                ['Eingegebenen Text mit „Ablage“ ▸ „Sichern unter …“ behalten', 'Ja', 'Ja, in einem Fenster, das beim Ende des Tests offen war', 'Ja'],
                ['Aktionen für Siri und Kurzbefehle', 'Ja', 'Nein', 'Ja'],
                ['Übersicht im Finder, mit Mermaid-Diagrammen und Formeln', 'Ja', 'Ja, unverändert', 'Ja'],
                ['<code>marsdawn export</code> (kostenloses Befehlszeilenprogramm): PDF mit Diagrammen und Formeln', 'Ja', 'Ja, unverändert', 'Ja'],
                ['Deine Dateien auf dem Datenträger', 'So, wie du sie gesichert hast', 'So, wie du sie gesichert hast; die Sperre ändert sie nie', 'So, wie du sie gesichert hast'],
            ],
        },
    }
    exit_table_head = ['Code', 'Bedeutung', 'Was tun']
    exit_remedy = {
        "0": 'Mit <code>--json</code> die eine JSON-Zeile auf stdout lesen',
        "2": 'Pfad und Dateinamen prüfen',
        "3": 'Die App installieren oder <code>export</code> verwenden, das sie nicht braucht',
        "4": '<code>--force</code> übergeben, um sie zu ersetzen, oder mit <code>-o</code> woandershin schreiben',
        "5": '<code>message</code> im JSON-Ergebnis lesen',
        "64": 'Option oder Wert korrigieren; dieser Fehler erscheint als Text auf stderr, auch mit <code>--json</code>',
    }
    # markdown-to-pdf shows /assets/cli/plan-de.png, which does not exist yet. Before this ships,
    # export example_plan with marsdawn 0.5.0 the way EXAMPLE_PLAN's comment in build_pages.py
    # describes, or fall back to plan-en.png with EXAMPLE_PLAN['en'].
    example_plan = '# Plan: schnellere Exporte\n\nDiesen Plan hat ein Agent geschrieben. Du prüfst ihn und machst daraus ein PDF.\n\n## Schritte\n\n| Schritt | Zuständig | Status |\n|---------|-----------|--------|\n| Langsame Seiten messen | Agent | Erledigt |\n| Gerenderte Diagramme cachen | Agent | In Prüfung |\n\nZiel sind $t < 2\\,\\text{s}$ für ein Dokument mit 50 Seiten:\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  Entwurf --> Prüfung --> Veröffentlichung\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'

    pages['markdown-to-pdf'] = {
        "title": 'Markdown in PDF auf dem Mac, über die Befehlszeile · MarsDawn',
        "description": 'Wandle Markdown auf dem Mac mit dem kostenlosen Befehlszeilenwerkzeug marsdawn in ein PDF um. Mit Homebrew installieren, einen Befehl ausführen: Tabellen, Mathematik, Mermaid und Code.',
        "body": f"""
<section class="intro">
  <h1>Markdown in PDF auf dem Mac, über die Befehlszeile.</h1>
  <p>Das kostenlose Werkzeug <code>marsdawn</code> macht mit einem einzigen Befehl aus einer Markdown-Datei ein PDF. Tabellen, Formeln, Mermaid-Diagramme und hervorgehobener Code sehen so aus, wie sie im Quelltext gemeint sind, und es braucht sonst nichts, nicht einmal die MarsDawn-App.</p>
</section>
<h2>Installieren</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>Auf einem Mac mit Apple Chip installiert Homebrew in Sekunden eine fertig gebaute Kopie. Auf einem Intel-Mac wird stattdessen aus dem Quellcode gebaut. Das dauert ein paar Minuten und erfordert Xcode 26 oder neuer. Das Werkzeug läuft unter macOS 15 oder neuer, und <code>marsdawn --version</code> zeigt die installierte Version an.</p>
<h2>Ein Dokument sichern</h2>
<p>Füge Folgendes in eine Datei namens <code>plan.md</code> ein:</p>
<pre><code>{k.xml_escape(example_plan)}</code></pre>
<h2>Exportieren</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>Es schreibt <code>plan.pdf</code> neben die Quelldatei und gibt aus, wo die Datei gelandet ist:</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>Das ist diese Seite, aufgenommen aus einem echten Lauf von <code>marsdawn</code> 0.5.0:</p>
<p><img class="pdf-page" src="/assets/cli/plan-de.png" alt="Das exportierte PDF: die Überschrift, eine Tabelle mit Schritten, eine Formel im Text und eine abgesetzte Formel, ein Diagramm Entwurf, Prüfung, Veröffentlichung und eine hervorgehobene Zeile Swift." width="989" height="930"></p>
<h2>Thema, Papierformat und Dateiname wählen</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code>: dawn, classic, modern oder vivid, jeweils in den hellen Farben des Themas. Ohne diese Option verwendet <code>export</code> <code>$MARSDAWN_THEME</code> und sonst dawn.</li>
  <li><code>--paper</code>: a4 oder letter. Standard ist a4.</li>
  <li><code>-o</code>: wohin das PDF geschrieben wird, statt neben die Quelldatei.</li>
  <li><code>--allow-remote-images</code>: lädt beim Rendern Bilder aus dem Web. Ohne diese Option bleiben sie aus.</li>
</ul>
<h2>Wenn es nicht klappt</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> Homebrew baut <code>marsdawn</code> aus dem Quellcode, wie auf einem Intel-Mac. Installiere Xcode 26 oder neuer aus dem App Store und starte die Installation erneut.</li>
  <li><code>marsdawn: No such file: …</code> Der Pfad zeigt auf keine Datei. Prüfe den Namen oder führe den Befehl in dem Ordner aus, in dem die Datei liegt.</li>
  <li><code>… already exists. Pass --force to replace it.</code> Ein PDF mit diesem Namen gibt es schon. Füge <code>--force</code> hinzu, um es zu ersetzen, oder <code>-o</code>, um woanders hinzuschreiben.</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> Das Thema oder Papierformat ist unbekannt. Die Themen sind dawn, classic, modern und vivid, das Papier ist a4 oder letter.</li>
</ul>
<h2>Weiter</h2>
<ul>
  <li>Alle Optionen und das JSON, das ausgegeben wird: <a href="/de/cli/">Befehlszeile</a>.</li>
  <li>Wenn ein Coding-Agent das für dich erledigen soll: <a href="/de/cli/skill/">der marsdawn-Agent-Skill</a>.</li>
  <li>Alle vier Vorschauthemen und wohin sich der PDF-Export entwickelt: <a href="/de/themes/">Vorschauthemen und PDF-Export</a>.</li>
  <li>Das PDF an jemanden weitergeben, der kein Markdown nutzt: <a href="/de/sharing-exported-pdfs/">ein PDF teilen</a>.</li>
</ul>
""",
    }

    pages['view-markdown-on-mac'] = {
        "title": 'Eine Markdown-Datei auf dem Mac ansehen · MarsDawn',
        "description": 'Eine .md-Datei ist reiner Text mit Formatierungszeichen. So liest du sie auf dem Mac gerendert: heute als PDF mit dem kostenlosen Befehlszeilenwerkzeug marsdawn und in der MarsDawn-App aus dem Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>Eine Markdown-Datei auf dem Mac ansehen.</h1>
  <p>Eine <code>.md</code>-Datei ist reiner Text. Überschriften, fette Wörter, Tabellen und Diagramme stehen darin als Zeichen: <code>#</code> für eine Überschrift, <code>**</code> um fetten Text, senkrechte Striche für eine Tabelle, ein <code>mermaid</code>-Codeblock für ein Diagramm. In einem einfachen Texteditor liest du die Zeichen. Um die Seite so zu lesen, wie sie gemeint ist, muss sie jemand rendern.</p>
</section>
<h2>Heute und kostenlos: als PDF</h2>
<p>Das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code> rendert eine Markdown-Datei als PDF, das jeder Mac öffnen kann. Tabellen, Formeln, Mermaid-Diagramme und hervorgehobener Code kommen gerendert heraus, und es braucht sonst nichts, nicht einmal die MarsDawn-App.</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> schreibt <code>notes.pdf</code> neben die Markdown-Datei, und <code>open</code> zeigt sie in deinem PDF-Programm an. Erforderlich ist macOS 15 oder neuer. Die Schritt-für-Schritt-Anleitung mit einer echten exportierten Seite findest du unter <a href="/de/markdown-to-pdf/">Markdown in PDF</a>.</p>
<h2>In MarsDawn lesen</h2>
<p>MarsDawn ist ein Markdown-Editor für den Mac, im Mac App Store. Öffne eine <code>.md</code>-Datei und lies die gerenderte Seite neben dem Quelltext:</p>
<ul>
  <li>Die Vorschau aktualisiert sich beim Tippen, und beide Bereiche scrollen gemeinsam.</li>
  <li>Mermaid-Flussdiagramme und Sequenzdiagramme werden in der Vorschau gezeichnet, Codeblöcke werden hervorgehoben.</li>
  <li>Drücke im Finder die Leertaste auf einer Markdown-Datei, um eine Übersicht zu sehen, Diagramme inklusive.</li>
  <li>Wenn du etwas ändern willst, ist der Quelltext direkt da. MarsDawn ist ein Editor, nicht nur ein Viewer.</li>
</ul>
<p>Wenn ein KI-Agent die Datei geschrieben hat, ist das genau der Ablauf, für den MarsDawn gebaut ist: Der Agent schreibt, du liest es gerendert, und er überarbeitet. Siehe <a href="/de/">die Startseite</a> und <a href="/de/cli/agents/">marsdawn für Agenten</a>, wenn ein Agent Dateien für dich öffnen soll. Warum dieses Lesen wichtig ist und wie du einen Plan prüfst, steht unter <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a> und <a href="/de/reviewing-agent-plans/">Einen Agentenplan in fünf Minuten prüfen</a>.</p>
<h2>Weiter</h2>
<ul>
  <li>Alle Optionen des Befehlszeilenwerkzeugs: <a href="/de/cli/">Befehlszeile</a>.</li>
  <li>Was MarsDawn nicht kann: <a href="/de/limits/">die Liste</a>.</li>
  <li>Markdown stattdessen in VS Code, im Browser oder in Claude Desktop lesen: <a href="/de/vs/markdown-preview-tools/">der Vergleich</a>.</li>
</ul>
""",
    }

    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer oder MarsDawn: Viewer oder Editor · MarsDawn',
        "description": 'MacMD Viewer zeigt Markdown nur zum Lesen an, für 19,99 USD. MarsDawn bearbeitet und zeigt die Vorschau daneben, kostenlos testen, dann einmalig 4,99 USD im Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer oder MarsDawn.</h1>
  <p>Beides sind Mac-Apps, um Markdown gerendert zu lesen. MacMD Viewer öffnet eine <code>.md</code>-Datei und zeigt die fertige Seite, bearbeiten kann man sie darin nicht. MarsDawn stellt neben dieselbe Art gerenderter Vorschau einen Editor, sodass du in einem Fenster schreibst und prüfst. Hier die Unterschiede, Funktion für Funktion.</p>
</section>
<h2>Wenn du nur lesen und nicht bearbeiten musst</h2>
<p>Wenn deine Aufgabe ausschließlich darin besteht, Markdown von anderen zu lesen, und du den Quelltext nie anfassen musst, passt MacMD Viewer gut: Die App ist genau dafür gebaut, jetzt erhältlich und läuft auch unter älteren macOS-Versionen. MarsDawn lohnt sich, sobald Lesen nicht die ganze Arbeit ist, denn das Markdown eines Agenten kommt meist noch einmal zur Überarbeitung zurück.</p>
<h2>Was die Apps können</h2>
<!--compare:macmd-features-->
<h2>Preis und Kauf</h2>
<!--compare:macmd-buying-->
<h2>Heute kostenlos ausprobieren</h2>
<p>MarsDawn ist im Mac App Store erhältlich. Das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code> rendert außerdem jede Markdown-Datei als PDF, mit Mermaid-Diagrammen und hervorgehobenem Code, und braucht sonst nichts:</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>Weiter</h2>
<ul>
  <li>Die vollständige Anleitung: <a href="/de/markdown-to-pdf/">Markdown in PDF</a>.</li>
  <li>Was MarsDawn nicht kann: <a href="/de/limits/">die Liste</a>.</li>
  <li>Alle Optionen des Befehlszeilenwerkzeugs: <a href="/de/cli/">Befehlszeile</a>.</li>
  <li>Im Vergleich dazu Markdown in VS Code, im Browser oder in Claude Desktop lesen: <a href="/de/vs/markdown-preview-tools/">der Vergleich</a>.</li>
</ul>
""",
    }

    compare_tables['macmd-features'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['Bearbeiten', 'Bewusst nur zum Lesen', 'Bearbeitet den Quelltext, mit der gerenderten Seite daneben'],
            ['Vorschauthemen', '12 Dokumentthemen', '4 Themen, jeweils mit heller und dunkler Farbpalette'],
            ['Diagramme und Mathematik', 'Mermaid und Code-Hervorhebung; die Beschreibung erwähnt keine Mathematik', 'Mermaid, Code-Hervorhebung und KaTeX-Mathematik'],
            ['Übersicht im Finder', 'Ja', 'Ja'],
            ['PDF und Drucken', 'Ja', 'Ja'],
            ['Voraussetzung', 'macOS 14 (Sonoma) oder neuer', 'macOS 26 (Tahoe) oder neuer'],
            ['Sprachen der Oberfläche', 'In den eigenen Unterlagen nicht angegeben', '{langs}'],
        ],
    }
    compare_tables['macmd-buying'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['Wo du es kaufst', 'Eigene Website, Homebrew oder Setapp; nicht im Mac App Store', 'Nur im Mac App Store'],
            ['Preis', 'Einmalig 19,99 USD für einen Mac; Pakete für mehrere Macs kosten mehr', 'Kostenloser Download, dann einmalig 4,99 USD'],
            ['Vorher ausprobieren', 'Keine Testphase; 14 Tage Geld-zurück-Garantie bei Direktkauf', '14 Tage kostenlos testen'],
            ['Rückerstattung und Updates', 'Über die eigene Website', 'Über Apple'],
            ['Account nötig', 'Nein', 'Nein'],
        ],
    }

    schema_notes = {
        "export": "export erfolgreich",
        "open": "open erfolgreich, marsdawn 0.5.1 und neuer, einschließlich eines in der Seitenleiste angezeigten Ordners",
        "open_v2": "open erfolgreich, marsdawn 0.3.0 bis 0.5.0",
        "error": "Fehler, beide Befehle, marsdawn 0.5.2 und neuer",
        "open_v1": "open erfolgreich, marsdawn 0.2.x, wo <code>opened</code> eine Liste von Pfaden war",
        "error_v1": "Fehler, beide Befehle, marsdawn 0.5.1 und älter",
    }

    pages['cli/agents'] = {
        "title": 'marsdawn für Agenten: Markdown in PDF aus Skripten · MarsDawn',
        "description": 'Eine Referenz für KI-Agenten und Skripte, die marsdawn aufrufen, um Markdown in PDF umzuwandeln: Befehle, JSON-Ausgabe, Schemas, Exit-Codes und Voraussetzungen.',
        "body": f"""
<section class="intro">
  <h1>marsdawn für Agenten</h1>
  <p>Eine Referenz für KI-Agenten und Skripte, die das Befehlszeilenwerkzeug <code>marsdawn</code> aufrufen. Jedes Beispiel auf dieser Seite wurde mit dem aus dem aktuellen Quellcode gebauten Werkzeug ausgeführt.</p>
</section>

<div class="summary"><p><strong>Um eine Markdown-Datei in ein PDF umzuwandeln, führe <code>marsdawn export notes.md --json</code> aus und lies ein JSON-Objekt von stdout.</strong> Mermaid-Diagramme und hervorgehobener Code werden genauso gerendert wie in der MarsDawn-App. <code>export</code> braucht die App nicht, <code>open</code> schon.</p></div>

<h2>Was es tut</h2>
<ul>
  <li><code>export</code> rendert eine Markdown-Datei mit demselben Exporter wie die MarsDawn-App zu einem PDF mit Seitenumbrüchen. Es öffnet sich kein Fenster.</li>
  <li><code>open</code> öffnet eine oder mehrere Markdown-Dateien in der MarsDawn-App, damit ein Mensch sie prüfen kann. Es kann für jede Datei die Zeile angeben, bei der sie aufgehen soll, und einen Ordner in der Seitenleiste des Fensters anzeigen.</li>
</ul>

<h2>Was es nicht tut</h2>
<ul>
  <li>Es liest kein Markdown von stdin. Übergib einen Dateipfad.</li>
  <li>Es schreibt das PDF nicht nach stdout. Das PDF landet immer in einer Datei; stdout enthält nur das Ergebnis.</li>
  <li>Es ersetzt keine vorhandene Datei, außer du übergibst <code>--force</code>.</li>
  <li>Es lädt keine Bilder aus dem Web, außer du übergibst <code>--allow-remote-images</code>, und dann nur über https.</li>
  <li><code>open</code> funktioniert nicht ohne installierte MarsDawn-App und endet mit Code 3. <code>export</code> braucht die App nicht. Die App gibt es im <a href="{k.LISTING_URL}">Mac App Store</a>.</li>
  <li>MarsDawn 1.0 öffnet die Datei in der Zeile, die <code>open</code> angibt.</li>
  <li>Es läuft nur unter macOS.</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p>Schreibt <code>notes.pdf</code> neben <code>notes.md</code>. Optionen:</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: wohin das PDF geschrieben wird. Standard ist der Eingabepfad mit der Endung <code>.pdf</code>.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: die helle Farbpalette des Themas. Standard ist <code>$MARSDAWN_THEME</code>, sonst <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: Papierformat. Standard ist <code>a4</code>.</li>
  <li><code>--allow-remote-images</code>: lädt beim Rendern https-Bilder aus dem Web.</li>
  <li><code>--force</code>: ersetzt die Ausgabedatei, falls sie existiert.</li>
  <li><code>--json</code>: gibt statt Text ein JSON-Objekt auf stdout aus.</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>Erfolg, Exit-Code 0:</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code>: absoluter Pfad des geschriebenen PDFs.</li>
  <li><code>pages</code>: Anzahl der Seiten.</li>
  <li><code>theme</code> und <code>paper</code>: die verwendeten Werte.</li>
  <li><code>diagramErrors</code>: eine Meldung pro Mermaid-Diagramm, das nicht gerendert werden konnte. Das PDF wird trotzdem geschrieben.</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json</code></pre>
<ul>
  <li><code>path:line</code> gibt die Zeile an, bei der die Datei aufgehen soll. Eine Spalte dahinter, wie in <code>notes.md:120:8</code>, wird ignoriert. Ein Argument, das eine existierende Datei benennt, gilt immer als ganzer Dateiname, eine Datei namens <code>weird:12</code> öffnet sich also als sie selbst.</li>
  <li><code>--line &lt;n&gt;</code> gibt die Zeile für eine einzelne Datei an, auch für einen Pfad, der selbst auf Doppelpunkt und Ziffern endet. Es braucht genau eine Datei.</li>
  <li>Zeilen reichen von 1 bis 999999999. Alles andere ist ein Bedienungsfehler.</li>
  <li>Zeilen kamen mit marsdawn 0.3.0 hinzu. MarsDawn 1.0 öffnet die Datei in dieser Zeile.</li>
  <li>Ein Ordner als Argument öffnet sich in der Seitenleiste des Fensters statt als Dokument, <code>marsdawn open .</code> zeigt also den aktuellen Ordner; <code>--folder &lt;path&gt;</code> tut dasselbe zusätzlich zu Dateien. Die Seitenleiste eines Fensters zeigt einen Ordner: Zwei anzugeben ist ein Bedienungsfehler, ebenso <code>--folder</code> zweimal, selbst für denselben Ordner; derselbe Ordner noch einmal als Argument zählt einmal. <code>--line</code> mit einem Ordner ist ein Bedienungsfehler, da ein Ordner keine Zeile hat. Es gibt kein <code>-a</code>: Wer es übergibt, bekommt einen Bedienungsfehler mit Verweis auf <code>--folder</code>.</li>
  <li><code>--background</code> öffnet, ohne MarsDawn in den Vordergrund zu holen, für einen Agenten, der Dateien öffnet, während der Mensch woanders arbeitet. Das JSON ist in beiden Fällen gleich.</li>
  <li>Ordner und <code>--background</code> kamen mit marsdawn 0.5.1 hinzu.</li>
</ul>
<p>Erfolg, Exit-Code 0:</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>: ein Objekt pro Datei, in der angegebenen Reihenfolge. <code>path</code> ist der absolute Pfad der Datei; <code>line</code> erscheint nur, wenn eine Zeile angefragt wurde.</li>
  <li><code>app</code>: Pfad der MarsDawn-App, die sie geöffnet hat.</li>
</ul>
<p>Mit einem Ordner (marsdawn 0.5.1 und neuer), Exit-Code 0:</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","folder":{{"path":"/path/to/project","requested":true}},"ok":true,"opened":[{{"path":"/path/to/project/notes.md"}}]}}</code></pre>
<ul>
  <li><code>folder</code>: nur vorhanden, wenn ein Ordner angegeben wurde. <code>path</code> ist sein absoluter Pfad. <code>requested</code> ist immer <code>true</code>: marsdawn hat MarsDawn gebeten, den Ordner anzuzeigen, und kann nicht wissen, ob die Seitenleiste ihn zeigt, denn die App fragt den Menschen womöglich erst nach Zugriff. Melde es als angefragt, nicht als erledigt.</li>
  <li><code>opened</code> ist leer, wenn nur ein Ordner angegeben wurde.</li>
</ul>
<p>marsdawn 0.2.x gab <code>opened</code> als Liste von Pfad-Strings aus. Prüfe <code>marsdawn --version</code>, wenn du beides verarbeiten musst.</p>

<h2>Dateien öffnen, während Claude Code sie bearbeitet</h2>
<p>Ein optionaler <a href="https://code.claude.com/docs/en/hooks">Claude Code Hook</a>: Nachdem Claude eine Markdown-Datei geschrieben oder bearbeitet hat, öffnet er diese Datei im Hintergrund in MarsDawn, einmal pro Datei und Sitzung. Er ist aus, bis du ihn hinzufügst, Projekt für Projekt, denn ein Fenster, um das du nicht gebeten hast, kostet Aufmerksamkeit. Er führt einen Shell-Befehl aus und kostet keine Modell-Tokens.</p>
<p>Er braucht marsdawn 0.5.1 oder neuer, wegen <code>--background</code>, und die MarsDawn-App.</p>
<p>Sichere das als <code>.claude/hooks/marsdawn-open.sh</code> in deinem Projekt und mach es mit <code>chmod +x</code> ausführbar:</p>
<pre><code>#!/bin/sh
# Claude Code PostToolUse hook: open a Markdown file Claude just wrote or edited in MarsDawn,
# in the background, once per file per session. Never blocks Claude: every path exits 0.
input=$(cat)
file=$(printf '%s' "$input" | /usr/bin/jq -r '.tool_input.file_path // empty' 2&gt;/dev/null)
session=$(printf '%s' "$input" | /usr/bin/jq -r '.session_id // "unknown"' 2&gt;/dev/null)

case "$file" in
  *.md|*.markdown) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0
# A hook runs with Claude Code's PATH, which may not include Homebrew's.
marsdawn=$(command -v marsdawn || {{ [ -x /opt/homebrew/bin/marsdawn ] &amp;&amp; echo /opt/homebrew/bin/marsdawn; }}) || exit 0
[ -n "$marsdawn" ] || exit 0

# One list per session, so a file opens once however often Claude edits it.
seen="${{TMPDIR:-/tmp}}/marsdawn-hook/$session"
mkdir -p "$(dirname "$seen")"
grep -qxF "$file" "$seen" 2&gt;/dev/null &amp;&amp; exit 0
echo "$file" &gt;&gt; "$seen"

"$marsdawn" open --background "$file" &gt;/dev/null 2&gt;&amp;1 || true
exit 0</code></pre>
<p>Füge den Hook dann zu <code>.claude/settings.json</code> im Projekt hinzu, oder zu <code>.claude/settings.local.json</code>, wenn er nur für dich gelten soll:</p>
<pre><code>{{
  "hooks": {{
    "PostToolUse": [
      {{
        "matcher": "Write|Edit",
        "hooks": [
          {{ "type": "command", "command": "\\"$CLAUDE_PROJECT_DIR\\"/.claude/hooks/marsdawn-open.sh" }}
        ]
      }}
    ]
  }}
}}</code></pre>
<ul>
  <li>Er läuft nach Claudes Write- und Edit-Werkzeugen. Dateien, die nicht auf <code>.md</code> oder <code>.markdown</code> enden, bleiben unberührt.</li>
  <li>Jede Datei öffnet sich einmal pro Claude-Code-Sitzung, egal wie oft Claude sie bearbeitet. Die Liste liegt in <code>$TMPDIR/marsdawn-hook/</code>, eine Datei pro Sitzung, eine neue Sitzung öffnet die Datei also erneut.</li>
  <li><code>--background</code> hält MarsDawn im Hintergrund: Das Fenster, in dem du gearbeitet hast, behält den Fokus.</li>
  <li>Er kommt Claude nie in die Quere. Jeder Pfad endet mit 0, und wenn marsdawn oder die MarsDawn-App nicht installiert ist, passiert nichts.</li>
  <li>Er liest die Eingabe des Hooks mit <code>/usr/bin/jq</code>, das bei macOS 26 dabei ist, der Version, die die MarsDawn-App braucht.</li>
  <li>Zum Abschalten entferne den Eintrag aus der Einstellungsdatei.</li>
</ul>

<h2>Fehler</h2>
<p>Mit <code>--json</code> gibt ein Fehler ein JSON-Objekt auf stdout aus und endet mit seinem Code:</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>, <code>input_not_found</code>: Die Eingabe existiert nicht, ist ein Ordner oder ist kein UTF-8-Text; oder ein <code>--folder</code>-Pfad existiert nicht oder ist kein Ordner.</li>
  <li><code>3</code>, <code>app_not_installed</code>: MarsDawn ist nicht installiert. Nur <code>open</code> liefert das.</li>
  <li><code>4</code>, <code>output_exists</code>: Die Ausgabedatei existiert. Übergib <code>--force</code>.</li>
  <li><code>5</code>, <code>export_failed</code>: Der Export selbst ist fehlgeschlagen.</li>
  <li><code>6</code>, <code>app_cannot_open_folders</code>: Dieses MarsDawn kann keinen Ordner anzeigen, also wurde nichts geöffnet. Nur <code>open</code> liefert das.</li>
  <li><code>64</code>: Bedienungsfehler, etwa eine unbekannte Option, ein ungültiger Wert, eine Zeile außerhalb des Bereichs, <code>--line</code> mit mehr als einer Datei oder mit einem Ordner, mehr als ein Ordner oder <code>-a</code>. Dieser wird als Text auf stderr ausgegeben, auch mit <code>--json</code>.</li>
</ul>

<h2>JSON-Schemas</h2>
<p>JSON Schema (Draft 2020-12) für jedes <code>--json</code>-Ergebnis:</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>Umgebungsvariablen</h2>
<ul>
  <li><code>MARSDAWN_THEME</code>: das Thema, das <code>export</code> verwendet, wenn <code>--theme</code> nicht übergeben wird. Ein unbekannter Wert fällt ohne Fehler auf <code>dawn</code> zurück.</li>
</ul>

<h2>Voraussetzungen</h2>
<ul>
  <li>Das Werkzeug läuft unter macOS 15 oder neuer. Auf Apple Chips installiert Homebrew eine fertig gebaute Bottle, und sonst wird nichts gebraucht. Selbst bauen, auf einem Intel-Mac oder aus dem Quellcode, erfordert Swift 6.2 oder neuer, das mit Xcode 26 oder neuer kommt.</li>
  <li>Die MarsDawn-App erfordert macOS 26 oder neuer.</li>
</ul>

<h2>Installieren</h2>
<p>Mit Homebrew. Auf Apple Chips installiert es in Sekunden eine fertig gebaute Bottle, ganz ohne Xcode. Auf einem Intel-Mac kompiliert es marsdawn aus dem Quellcode, was ein paar Minuten dauert und Xcode 26 oder neuer erfordert.</p>
<pre><code>brew tap redtear1115/tap && brew install marsdawn
marsdawn --version</code></pre>
<p>Oder bau es aus <a href="{k.KIT_URL}">dem Quellcode</a>. Der erste Build lädt Abhängigkeiten und kompiliert, was ebenfalls ein paar Minuten dauert.</p>
<pre><code>git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> gibt die Versionsnummer aus, etwa <code>0.3.0</code>, und endet mit Code 0.</p>

<h2>Weiter</h2>
<ul>
  <li>Ein Skill in einer Datei für Agenten, die Anweisungen lesen statt eine Shell zu benutzen: <a href="/de/cli/skill/">der marsdawn-Skill</a>.</li>
  <li>Ein MCP-Server, der genau dieses <code>export</code> umschließt: <a href="/de/cli/mcp/">marsdawn-mcp</a>.</li>
  <li>Warum dieses JSON-Ergebnis für den eigenen Kontext eines Agenten günstig bleibt: <a href="/de/token-efficient-review/">Token-sparsames Prüfen</a>.</li>
</ul>
""",
    }

    pages['cli/skill'] = {
        "title": 'Ein Coding-Agent-Skill für Markdown in PDF · MarsDawn',
        "description": 'Eine Datei, die dein Coding-Agent lädt, um geschriebenes Markdown zur Prüfung in MarsDawn zu öffnen, marsdawn zu installieren, Markdown als PDF zu exportieren und das JSON-Ergebnis zu lesen.',
        "body": f"""
<section class="intro">
  <h1>Lass deinen Agenten zeigen, was er geschrieben hat, und das PDF erstellen.</h1>
  <p>Dieser Skill ist eine Markdown-Datei. Er bringt einem Coding-Agenten bei, ein Dokument, das er geschrieben hat, zur Prüfung für dich in MarsDawn zu öffnen, <code>marsdawn</code> zu installieren, zu prüfen, ob es funktioniert, ein Dokument als PDF zu exportieren und das Ergebnis zu lesen.</p>
</section>
<div class="summary"><p><strong>Eine Markdown-Datei unter <code>~/.claude/skills/marsdawn/SKILL.md</code>.</strong> Damit installiert dein Agent <code>marsdawn</code>, exportiert als PDF und liest das JSON-Ergebnis, und er fragt trotzdem, bevor er etwas ausführt.</p></div>
<h2>In Claude Code installieren</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL https://marsdawn.southern-light.dev/cli/skill/SKILL.md -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code lädt ihn, wenn eine Aufgabe ein PDF verlangt oder wenn es ein Markdown-Dokument zum Lesen für dich geschrieben oder überarbeitet hat, und du kannst ihn selbst als <code>/marsdawn</code> aufrufen. Es ist <a href="/cli/skill/SKILL.md">eine kurze Datei</a>, lies sie also, bevor du sie installierst.</p>
<p>Andere Agenten können dieselbe Datei verwenden. Sie ist reines Markdown, Anweisungen und Befehle, also verweise deinen Agenten auf die URL oder füge sie ein.</p>
<h2>Was er beibringt</h2>
<ul>
  <li><code>marsdawn</code> mit Homebrew installieren, falls es fehlt, und es dann mit <code>marsdawn --version</code> prüfen, statt eine Version anzunehmen.</li>
  <li>Mit <code>marsdawn export … --json</code> exportieren und das Ergebnis lesen: wo das PDF gelandet ist, wie viele Seiten es hat und welches Mermaid-Diagramm nicht gerendert wurde.</li>
  <li>Fehler am Exit-Code unterscheiden: keine solche Datei, ein PDF ist schon da, ein fehlgeschlagener Export, eine falsche Option.</li>
  <li>Ein geschriebenes Dokument mit <code>marsdawn open file.md:line</code> öffnen, bei der ersten Änderung, und nur einmal: Spätere Änderungen erscheinen von selbst im offenen Fenster.</li>
  <li>Wenn die MarsDawn-App nicht installiert ist, das einmal sagen und weitermachen, ohne es erneut zu versuchen. Nie <code>open</code> verwenden, um ein PDF zu erstellen.</li>
  <li>Mit <code>--folder</code> (marsdawn 0.5.1 und neuer) den Ordner als angefragt melden, nicht als angezeigt: Die App entscheidet, und nichts meldet zurück.</li>
</ul>
<h2>Was er nicht tut</h2>
<ul>
  <li>Er gibt sich nicht selbst die Erlaubnis, etwas auszuführen. Dein Agent fragt weiterhin, bevor er <code>marsdawn</code> installiert oder ausführt, wie bei jedem anderen Befehl.</li>
  <li>Er schickt deine Dokumente nirgendwohin. <code>marsdawn</code> rendert auf deinem Mac und lässt Bilder aus dem Web weg, außer du übergibst <code>--allow-remote-images</code>.</li>
</ul>
<p>Der vollständige Vertrag, jedes Feld und jeder Code, steht unter <a href="/de/cli/agents/">marsdawn für Agenten</a>. Für einen Agenten, der Werkzeuge über MCP aufruft, statt eine Skill-Datei zu lesen, gibt es außerdem <a href="/de/cli/mcp/">einen MCP-Server</a>.</p>
""",
    }

    pages['cli/mcp'] = {
        "title": 'Drei Wege, marsdawn aufzurufen: CLI, Skill-Datei, MCP-Server · MarsDawn',
        "description": 'marsdawn hat kein eigenes KI-Modell, daher ist egal, welcher Agent das Markdown geschrieben hat. Ruf es über die CLI, eine Skill-Datei oder den MCP-Server marsdawn-mcp auf: Alle drei führen denselben Export aus.',
        "body": f"""
<section class="intro">
  <h1>Drei Wege, marsdawn aufzurufen.</h1>
  <p>MarsDawn hat kein eigenes KI-Modell: Es ist gebaut, um Markdown zu prüfen, nicht um es zu schreiben, daher ist egal, welcher Agent oder welches Modell die Datei erzeugt hat. Es gibt drei Wege, wie ein Agent oder ein Skript <code>marsdawn</code> aufrufen kann, und alle drei führen am Ende dasselbe <code>export</code> aus.</p>
</section>

<div class="summary"><p><strong>Nimm, was deine Werkzeuge unterstützen: die kostenlose <code>marsdawn</code>-CLI, eine Skill-Datei in reinem Markdown oder den MCP-Server <a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a>.</strong> Alle drei rufen dasselbe <code>marsdawn export</code> auf und liefern dasselbe JSON-Ergebnis.</p></div>

<h2>Welchen Weg nehmen</h2>
<!--compare:mcp-choice-->

<h2>Die CLI</h2>
<p><code>marsdawn export notes.md --json</code> kann jeder Agent und jedes Skript aufrufen, das einen Shell-Befehl ausführen kann, und ist damit von Haus aus modellunabhängig. Jedes Feld, das es liefert, ist unter <a href="/de/cli/agents/">marsdawn für Agenten</a> dokumentiert. Das ist die maßgebliche Quelle für das JSON-Schema, auf die die beiden anderen Wege unten verweisen.</p>

<h2>Die Skill-Datei</h2>
<p>Für einen Agenten, der Anweisungen in reinem Markdown liest, statt direkt eine Shell aufzurufen (heute Claude Code), ist <a href="/de/cli/skill/">der marsdawn-Skill</a> eine Datei, die ihm beibringt, marsdawn zu installieren, <code>export</code> auszuführen und das Ergebnis zu lesen. Sie ist reines Markdown, also können andere Agenten, die Anweisungsdateien laden, dieselbe verwenden.</p>

<h2>Der MCP-Server</h2>
<p><a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a> ist ein eigenes, öffentliches Repository unter Apache-2.0. Es ist ein MCP-Server mit zwei Werkzeugen, <code>export_markdown_to_pdf</code> und <code>open_in_marsdawn</code>, die <code>marsdawn export --json</code> und <code>marsdawn open --json</code> umschließen: Richte einen MCP-Client darauf, und ein Werkzeugaufruf liefert dasselbe JSON wie die CLI.</p>
<ul>
  <li><strong>Bezugsquelle:</strong> als MCP Bundle, <code>marsdawn.mcpb</code>, angehängt an <a href="https://github.com/redtear1115/marsdawn-mcp/releases">sein GitHub-Release</a>, oder indem du den Server aus dem Quellcode über stdio startest.</li>
  <li><strong>Registry:</strong> noch nicht in der MCP Registry gelistet (aktuelles Release: 0.2.1). Prüfe den aktuellen Stand im Repository, bevor du dich auf die Suche über die Registry verlässt.</li>
  <li><strong>Hosting:</strong> nur selbst gehostet. Es gibt keinen gehosteten marsdawn-mcp-Dienst; der Server läuft auf deinem eigenen Rechner, neben marsdawn selbst.</li>
  <li><strong>Voraussetzungen:</strong> macOS, marsdawn 0.5.0 oder neuer und Node.js 20 oder neuer, um den Server auszuführen.</li>
</ul>

<h2>Auf Ordner beschränkt, die du erlaubst</h2>
<p>Beide Werkzeuge greifen nur auf Ordner zu, die du erlaubst: die Einstellung <strong>Allowed folders</strong> der Erweiterung, die leer und ohne Voreinstellung beginnt, oder stattdessen die Roots, die dein MCP-Client anbietet. Ist beides nicht gesetzt, wird jeder Aufruf abgelehnt, und die Meldung sagt, wie du das behebst. Jeder Pfad muss absolut sein, und <code>export_markdown_to_pdf</code> schreibt immer nur eine <code>.pdf</code>-Datei, nie über einen symbolischen Link.</p>
<p><strong>Sicherheit:</strong> Aktualisiere auf <a href="https://github.com/redtear1115/marsdawn-mcp/releases/tag/v0.2.1">0.2.1</a>. Mit 0.1.0 und 0.2.0 konnte ein Aufruf ein PDF an jeden Pfad schreiben, auf den dein Benutzerkonto schreiben durfte; behoben als <a href="https://github.com/redtear1115/marsdawn-mcp/security/advisories/GHSA-fqgj-hcxc-34qc">GHSA-fqgj-hcxc-34qc</a>.</p>

<h2>Derselbe Export, drei Türen</h2>
<p>Egal, welcher Weg es aufruft, das Verhalten darunter ändert sich nicht: derselbe Exporter, dieselben Themen und Papierformate, dieselben <code>diagramErrors</code>, wenn ein Mermaid-Diagramm nicht gerendert werden kann. Diese Seite wiederholt diesen Vertrag nicht; das tut <a href="/de/cli/agents/">marsdawn für Agenten</a>, vollständig.</p>

<h2>Weiter</h2>
<ul>
  <li>Das vollständige JSON-Schema und jeder Exit-Code: <a href="/de/cli/agents/">marsdawn für Agenten</a>.</li>
  <li>Der Skill in einer Datei für Claude Code und ähnliche Agenten: <a href="/de/cli/skill/">der marsdawn-Skill</a>.</li>
  <li>Warum ein kompaktes JSON-Ergebnis für den eigenen Kontext deines Agenten zählt: <a href="/de/token-efficient-review/">Token-sparsames Prüfen</a>.</li>
</ul>
""",
    }

    pages['vs/markdown-preview-tools'] = {
        "title": 'Markdown anderswo ansehen oder in MarsDawn · MarsDawn',
        "description": 'Wie sich MarsDawn mit dem Lesen von Markdown in der eingebauten Vorschau von VS Code, einer Browsererweiterung oder der Dateivorschau von Claude Desktop vergleicht: was jeweils gerendert wird und was es braucht, eine Datei zu öffnen.',
        "body": f"""
<section class="intro">
  <h1>Markdown anderswo ansehen oder in MarsDawn.</h1>
  <p>Wenn du VS Code, einen Browser oder Claude Desktop ohnehin offen hast, liegt es nahe, damit kurz in eine Markdown-Datei zu schauen. Hier siehst du, was jedes davon tatsächlich rendert und was es kostet, dorthin zu kommen, im Vergleich dazu, dieselbe Datei in MarsDawn zu öffnen.</p>
</section>

<h2>Auf einen Blick</h2>
<!--compare:preview-tools-->

<h2>Die eingebaute Vorschau von VS Code</h2>
<p>Drück in VS Code <kbd>&#8984;&#8679;V</kbd>, und es rendert die Markdown-Datei in einem eingebauten Vorschaubereich, kostenlos und ohne etwas zu installieren. Seit VS Code 1.121 (Mai 2026) rendert diese Vorschau auch Mermaid-Diagramme direkt: Microsoft hat eine Mermaid-Erweiterung in VS Code selbst übernommen, was früher eine eigene Erweiterung brauchte, jetzt nicht mehr. Was sie nicht tut: Sie ist ein Vorschaubereich in einem Editor, kein Editor, der zum Lesen gebaut ist. Der Bereich sitzt neben einem Dateibaum, einem Terminal und jedem anderen Panel, das VS Code anzeigen kann, und VS Code selbst ist eine Electron-App, die du als ganze Entwicklungsumgebung installierst, nichts, was du öffnest, um eine Datei zu lesen.</p>

<h2>Eine Browsererweiterung für lokale Dateien</h2>
<p>Keine einzelne Browsererweiterung dominiert beim Lesen einer lokalen <code>.md</code>-Datei: Local Markdown Viewer, Markdown Viewer, MarkView und andere tun ungefähr dasselbe, und keine ist Standard. Jede braucht denselben zusätzlichen Schritt, bevor sie etwas öffnen kann: „Zugriff auf Datei-URLs zulassen“ für diese Erweiterung einschalten, weil Browser Erweiterungen standardmäßig daran hindern, <code>file://</code>-Seiten zu lesen. Diese Berechtigung erteilst du einmal pro Erweiterung, und man vergisst leicht, dass man es getan hat, oder warum. Ist sie an, wird die Datei in einem Browser-Tab gerendert, du lässt also einen vollständigen Browser laufen, um eine Datei anzusehen.</p>

<h2>Die Dateivorschau von Claude Desktop</h2>
<p>Claude Desktop zeigt eine Datei, die schon in einem Projekt oder einer Unterhaltung ist. Wofür es nicht gebaut ist: beliebige Dateien auf der Festplatte zu durchsuchen. Ansehen kannst du, was die Unterhaltung schon enthält, nicht einen Ordner mit Notizen, den du neben deiner Arbeit offen hältst. Anthropics eigene Liste <a href="https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai">der Dokumenttypen, die du hochladen kannst</a>, umfasst PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON und XLSX: Markdown steht nicht darauf.</p>

<h2>Eine Browser-Engine, um eine Datei zu lesen</h2>
<p>VS Code ist eine Electron-App: ein mitgeliefertes Chromium samt Node.js-Laufzeit, keine native Mac-App. Der Weg über die Browsererweiterung läuft in einem echten Browser. So oder so läuft eine vollständige Browser-Engine, nur um eine Markdown-Datei anzuzeigen. MarsDawn ist eine native AppKit-App: keine mitgelieferte Browser-Laufzeit, sie öffnet jede lokale Datei direkt, ohne Erweiterung zum Installieren und ohne Berechtigung, an die man denken muss.</p>

<h2>Weiter</h2>
<ul>
  <li>Was MarsDawn auch nicht kann: <a href="/de/limits/">die Liste</a>.</li>
  <li>Jede Markdown-Datei heute kostenlos in ein PDF verwandeln: <a href="/de/markdown-to-pdf/">Markdown in PDF</a>.</li>
  <li>Im Vergleich mit einem nativen Mac-Viewer: <a href="/de/vs/macmd-viewer/">MacMD Viewer oder MarsDawn</a>.</li>
</ul>
""",
    }

    pages['themes'] = {
        "title": 'Vorschauthemen und PDF-Export in MarsDawn · MarsDawn',
        "description": 'Vier Vorschauthemen mit je einer hellen und einer dunklen Palette und ein PDF- und Druckexport, der zum gewählten Thema passt. Weitere importierbare Themen und eine Galerie zum Teilen eigener Themen sind geplant.',
        "body": f"""
<section class="intro">
  <h1>Acht Looks, ein Export.</h1>
  <p>MarsDawn bringt vier Vorschauthemen mit, Dawn, Classic, Modern und Vivid, jedes mit einer hellen und einer dunklen Palette: acht Kombinationen, um ein Dokument zu lesen. Exportierst du als PDF oder druckst, kommt die Seite in dem Thema heraus, in dem du gerade gelesen hast.</p>
</section>

<div class="summary"><p><strong>Vier Themen &#215; hell und dunkel = acht Arten, ein Dokument zu lesen, und ein Exportweg, der zu deiner Wahl passt.</strong> Weitere importierbare Themen und eine Galerie zum Teilen eigener Themen sind geplant, aber noch nicht gebaut.</p></div>

<h2>Die vier Themen</h2>
<!--theme-gallery-->
<ul>
  <li><strong>Dawn</strong>, der Standard: dasselbe warme Papier und derselbe Akzent in Mars Rust, aus denen diese Website gebaut ist.</li>
  <li><strong>Classic</strong>: eine schlichtere Palette, die an ein Dokument erinnert.</li>
  <li><strong>Modern</strong>: eine kühlere, zeitgemäßere Palette.</li>
  <li><strong>Vivid</strong>: eine hellere Palette mit stärkerem Kontrast.</li>
</ul>
<p>Jedes hat seine eigene helle und dunkle Variante: Wechselst du das Erscheinungsbild deines Macs, wechselt die Palette des Themas mit, nicht nur die Oberfläche drumherum.</p>

<h2>PDF-Export und Drucken verwenden dasselbe Thema</h2>
<p>Exportierst du als PDF oder druckst, verwendet die Seite die helle Palette deines Themas: Mermaid-Diagramme werden hineingezeichnet, Codeblöcke behalten ihre Syntaxhervorhebung, und Seitenumbrüche trennen keine Überschrift von ihrem Abschnitt und schneiden keine Tabelle und kein Diagramm in der Mitte durch. Das kostenlose <a href="/de/cli/">Befehlszeilenwerkzeug marsdawn</a> verwendet denselben Exporter, ein Skript oder ein Agent erzeugt also mit <code>--theme</code> das identische PDF, in jedem der vier Themen.</p>

<h2>Geplant: mehr Themen und eine Galerie</h2>
<p>Kommt später, noch nicht veröffentlicht: weitere importierbare Vorschauthemen und eine Galerie auf dieser Website, in der man eigene Themen einreichen kann. <code>/themes/v1/</code> ist dafür schon reserviert. Bis dahin hat MarsDawn die vier eingebauten Themen, und du kannst keine anderen installieren.</p>

<h2>Weiter</h2>
<ul>
  <li>Die vollständige Anleitung zum PDF-Export über die Befehlszeile: <a href="/de/markdown-to-pdf/">Markdown in PDF</a>.</li>
  <li>Was MarsDawn noch nicht kann: <a href="/de/limits/">die Liste</a>.</li>
  <li>Ein exportiertes PDF an jemanden weitergeben, der kein Markdown nutzt: <a href="/de/sharing-exported-pdfs/">ein PDF teilen</a>.</li>
</ul>
""",
    }

    compare_tables['mcp-choice'] = {
        'head': ['Wenn dein Agent', 'Nimm', 'Braucht'],
        'rows': [
            ['Einen Shell-Befehl ausführen kann', '<a href="{root}cli/agents/">Die CLI</a>', 'macOS 15 oder neuer'],
            ['Anweisungsdateien lädt, wie Claude Code', '<a href="{root}cli/skill/">Die Skill-Datei</a>', 'Die CLI, die der Skill installiert'],
            ['Werkzeuge über MCP aufruft', '<a href="{mcp}">marsdawn-mcp</a>', 'marsdawn-mcp 0.2.1 oder neuer, marsdawn 0.5.0 oder neuer und Node.js 20 oder neuer'],
        ],
    }
    compare_tables['preview-tools'] = {
        'head': ['', 'VS-Code-Vorschau', 'Browsererweiterung', 'Claude Desktop', 'MarsDawn'],
        'rows': [
            ['Öffnet eine Markdown-Datei von der Festplatte', 'Ja', 'Ja, sobald der Dateizugriff erlaubt ist', 'Nein: Markdown steht nicht auf der Upload-Liste', 'Ja'],
            ['Vor der ersten Datei', 'VS Code installieren, eine ganze Entwicklungsumgebung', 'Eine Erweiterung installieren, dann „Zugriff auf Datei-URLs zulassen“ einschalten', 'Es kann keine Dateien auf der Festplatte durchsuchen', 'MarsDawn installieren'],
            ['Gebaut für', 'Code schreiben; die Vorschau ist ein Bereich unter vielen', 'Im Web surfen', 'Unterhaltungen mit Claude', 'Markdown lesen und bearbeiten'],
            ['Zeichnet die Seite mit', 'Electron: ein mitgeliefertes Chromium samt Node.js', 'Einem vollständigen Browser', 'Der Claude-Desktop-App', 'Einer nativen AppKit-App; WebKit zeichnet die Seite'],
        ],
    }
    theme_shots = {
        '01-split': ('Dawn (Standard)', 'Das Thema Dawn in geteilter Ansicht: links der Markdown-Quelltext, rechts die gerenderte Seite.'),
        '02-classic': ('Classic', 'Das Thema Classic, die Vorschau füllt das Fenster.'),
        '04-vivid': ('Vivid', 'Das Thema Vivid in geteilter Ansicht.'),
        '03-dark': ('Dunkelmodus', 'MarsDawn im Dunkelmodus, geteilte Ansicht.'),
    }
    theme_gallery_note = 'Modern ist noch nicht abgebildet; das vierte Bild zeigt stattdessen den Dunkelmodus.'

    app_ui_languages = 'Englisch, traditionelles Chinesisch, vereinfachtes Chinesisch, Japanisch, Deutsch, Französisch, Spanisch und Koreanisch'
    return {
        'pages': pages, 'figures': figures, 'home': home, 'compare_tables': compare_tables,
        'exit_table_head': exit_table_head, 'exit_remedy': exit_remedy, 'app_ui_languages': app_ui_languages, 'example_plan': example_plan,
    }
