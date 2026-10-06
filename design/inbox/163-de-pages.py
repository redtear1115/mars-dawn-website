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

    app_ui_languages = 'Englisch, traditionelles Chinesisch, vereinfachtes Chinesisch, Japanisch, Deutsch, Französisch, Spanisch und Koreanisch'
    return {
        'pages': pages, 'figures': figures, 'home': home, 'compare_tables': compare_tables,
        'exit_table_head': exit_table_head, 'exit_remedy': exit_remedy, 'app_ui_languages': app_ui_languages, 'example_plan': example_plan,
    }
