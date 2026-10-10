"""German copy for the MarsDawn site (#163, tracking #168), integrated for #162's plumbing.

The text is Grok's, from draft PR #170 (design/inbox/163-de-pages.py and 163-de-strings.md),
carried over unchanged; only the return shape is the plumbing's (see scripts/new_locale.py). Written
here and not in Grok's material: the privacy page's description, the hero window's label and its
Markdown-twin sentence. The privacy and support titles are the legal pages' own h1. Legal pages:
content/legal/<slug>.de.md.
"""

# True: the build checks the shape, the legal pages, the hero snapshot and the images before it serves the locale.
COMPLETE = True


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
        "description": 'Keine Synchronisierung, keine iPhone- oder iPad-App, keine Plug-ins, keine Konten. Vier integrierte Themen, mehr in der Galerie. Gut zu wissen, bevor du kaufst.',
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
  <li><strong>Themen:</strong> Enthalten sind Morgenrot, Klassisch, Modern und Lebhaft, jeweils hell und dunkel. Weitere findest du in der <a href="/de/themes/gallery/">Themengalerie</a>: Installiere eines über Einstellungen › Erscheinungsbild › Weitere Themes laden …, oder <a href="/de/themes/new/">bau dein eigenes</a> im Browser. Ein Thema besteht aus Farben und Stileinstellungen, es ist kein Plug-in.</li>
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
  <li>Jedes Thema erfüllt den WCAG-AA-Kontrast, hell und dunkel. Klassisch ist jetzt schwarz-weiß.</li>
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
        'yours': {"alt": 'MarsDawn zeigt ein Dokument im Thema Klassisch, die Vorschau füllt das Fenster.',
                  "callouts": ['Eine Datei auf deinem Mac, gesichert, wo du willst.', 'Die ganze Symbolleiste besteht aus Themen und Layouts; anmelden musst du dich nirgends.']},
        'pay-once': {"alt": 'MarsDawn im Thema Lebhaft, links der Markdown-Quelltext, rechts die gerenderte Seite.',
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
        "cta_try": 'Jetzt laden und testen',
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
  <li><strong>Registry:</strong> in der <a href="https://registry.modelcontextprotocol.io/v0/servers/dev.southern-light.mcp%2Fmarsdawn/versions/latest">MCP Registry</a> als <code>dev.southern-light.mcp/marsdawn</code> gelistet (aktuelles Release: 0.2.4).</li>
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
        "description": 'Vier Vorschauthemen mit je einer hellen und einer dunklen Palette und ein PDF- und Druckexport, der zum gewählten Thema passt. Bau dein eigenes Thema im Browser und sieh dir die Community-Galerie an.',
        "body": f"""
<section class="intro">
  <h1>Acht Looks, ein Export.</h1>
  <p>MarsDawn bringt vier Vorschauthemen mit, Morgenrot, Klassisch, Modern und Lebhaft, jedes mit einer hellen und einer dunklen Palette: acht Kombinationen, um ein Dokument zu lesen. Exportierst du als PDF oder druckst, kommt die Seite in dem Thema heraus, in dem du gerade gelesen hast.</p>
</section>

<div class="summary"><p><strong>Vier Themen &#215; hell und dunkel = acht Arten, ein Dokument zu lesen, und ein Exportweg, der zu deiner Wahl passt.</strong> <a href="/de/themes/new/">Bau dein eigenes</a> im Browser, oder <a href="/de/themes/gallery/">sieh dir die Galerie an</a>, was andere eingereicht haben.</p></div>

<h2>Die vier Themen</h2>
<!--theme-gallery-->
<ul>
  <li><strong>Morgenrot</strong>, der Standard: dasselbe warme Papier und derselbe Akzent in Mars Rust, aus denen diese Website gebaut ist.</li>
  <li><strong>Klassisch</strong>: eine schlichtere Palette, die an ein Dokument erinnert.</li>
  <li><strong>Modern</strong>: eine kühlere, zeitgemäßere Palette.</li>
  <li><strong>Lebhaft</strong>: eine hellere Palette mit stärkerem Kontrast.</li>
</ul>
<p>Jedes hat seine eigene helle und dunkle Variante: Wechselst du das Erscheinungsbild deines Macs, wechselt die Palette des Themas mit, nicht nur die Oberfläche drumherum.</p>

<h2>PDF-Export und Drucken verwenden dasselbe Thema</h2>
<p>Exportierst du als PDF oder druckst, verwendet die Seite die helle Palette deines Themas: Mermaid-Diagramme werden hineingezeichnet, Codeblöcke behalten ihre Syntaxhervorhebung, und Seitenumbrüche trennen keine Überschrift von ihrem Abschnitt und schneiden keine Tabelle und kein Diagramm in der Mitte durch. Das kostenlose <a href="/de/cli/">Befehlszeilenwerkzeug marsdawn</a> verwendet denselben Exporter, ein Skript oder ein Agent erzeugt also mit <code>--theme</code> das identische PDF, in jedem der vier Themen.</p>

<h2>Bau dein eigenes, und sieh dir an, was andere gemacht haben</h2>
<p><a href="/de/themes/new/">Bau ein Thema in deinem Browser</a>: wähle Farben und ein paar Stiloptionen, sieh sie live angewendet und reiche es als GitHub-Issue zur Prüfung ein &#8212; keine Installation, kein git. <a href="/de/themes/gallery/">Die Galerie</a> zeigt jedes eingereichte Thema, das ein Maintainer geprüft und gemerged hat, filterbar nach Verwendungszweck. Installiere eines in der App über Einstellungen › Erscheinungsbild › Weitere Themes laden …, dann verwendet es auch die Übersicht im Finder.</p>

<h2>Weiter</h2>
<ul>
  <li>Die vollständige Anleitung zum PDF-Export über die Befehlszeile: <a href="/de/markdown-to-pdf/">Markdown in PDF</a>.</li>
  <li>Was MarsDawn noch nicht kann: <a href="/de/limits/">die Liste</a>.</li>
  <li>Ein exportiertes PDF an jemanden weitergeben, der kein Markdown nutzt: <a href="/de/sharing-exported-pdfs/">ein PDF teilen</a>.</li>
</ul>
""",
    }


    pages['themes/new'] = {
        "title": "Im Browser ein MarsDawn-Thema erstellen · MarsDawn",
        "description": "Wähle Farben und ein paar Stiloptionen, sieh sie live auf einem Beispieldokument und reiche dein Thema als GitHub-Issue ein. Keine Installation, kein git.",
        "body": """
<section class="intro">
  <h1>Ein Thema erstellen</h1>
  <p>Wähle unten eine Palette und ein paar Stiloptionen. Das Beispieldokument rechts aktualisiert sich laufend, hell und dunkel, und jede Prüfung, die die CI der Galerie ausführt, erscheint auch hier &#8212; ein Thema, das das Einreichungs-Issue erreicht, hat die Checks also meist schon bestanden.</p>
  <p>Zum Einreichen brauchst du ein GitHub-Konto. Für diese Seite selbst sind weder Installation noch git nötig.</p>
</section>
<div id="theme-sim-app" data-locale="de"><p>Diese Seite braucht JavaScript, um ein Thema zu erstellen und in der Vorschau zu zeigen.</p></div>
""",
    }
    pages['themes/gallery'] = {
        "title": "Themen-Galerie: Community-Themen für MarsDawn · MarsDawn",
        "description": "Durchsuche Vorschau-Themen, die die Community für MarsDawn eingereicht hat, filtere nach Szenario und melde ein Problem. Bau dein eigenes im Browser, ohne Installation und ohne git.",
        "body": f"""
<section class="intro">
  <h1>Themen-Galerie</h1>
  <p>Vorschau-Themen, die die Community eingereicht hat; jedes wurde vom Entwickler geprüft und gemerged, bevor es hier erscheint. Filtere nach Szenario, oder <a href="/de/themes/new/">baue dein eigenes</a> im Browser &#8212; keine Installation, kein git.</p>
</section>
<!--community-theme-gallery-->
<h2>Credits &amp; Lizenz</h2>
<p>Dracula, Nord, Gruvbox und Solarized basieren auf Open-Source-Farbschemata; Urheberrecht und vollständiger Lizenztext jedes Projekts stehen in den <a href="/themes/third-party-notices.html">Hinweisen zu Drittanbietern</a>.</p>
<h2>Stimmt etwas an einem Thema nicht?</h2>
<p>Nutze den Button „Melden“ auf seiner Karte (braucht JavaScript), oder schreib direkt an <a href="mailto:{k.EMAIL}">{k.EMAIL}</a> mit Name und Version, mit oder ohne JavaScript. Meldungen werden von Hand geprüft; ein bestätigtes Problem führt dazu, dass das Thema innerhalb eines Tages entfernt wird.</p>
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
        '01-split': ('Morgenrot (Standard)', 'Das Thema Morgenrot in geteilter Ansicht: links der Markdown-Quelltext, rechts die gerenderte Seite.'),
        '02-classic': ('Klassisch', 'Das Thema Klassisch, die Vorschau füllt das Fenster.'),
        '04-vivid': ('Lebhaft', 'Das Thema Lebhaft in geteilter Ansicht.'),
        '03-dark': ('Dunkelmodus', 'MarsDawn im Dunkelmodus, geteilte Ansicht.'),
    }
    theme_gallery_note = 'Modern ist noch nicht abgebildet; das vierte Bild zeigt stattdessen den Dunkelmodus.'

    pages['token-efficient-review'] = {
        "title": 'Die Ausgabe von MarsDawn prüfen, ohne die Tokens deines Agenten zu verbrauchen · MarsDawn',
        "description": 'Ein Mensch prüft die gerenderte Seite in MarsDawn, sie wird nie in den Kontext des Agenten zurückgelesen. Der Werkzeugaufruf selbst liefert ein kompaktes JSON-Ergebnis statt des gerenderten Inhalts, auch der Aufruf ist also günstig.',
        "body": f"""
<section class="intro">
  <h1>Prüfen, ohne die Tokens deines Agenten zu verbrauchen.</h1>
  <p>Zwei verschiedene Dinge bleiben in diesem Ablauf günstig: was der Agent vom Werkzeugaufruf zurückbekommt und was es braucht, um zu bestätigen, dass das Ergebnis stimmt.</p>
</section>

<div class="summary"><p><strong>Der Werkzeugaufruf liefert ein kleines JSON-Objekt, nicht die gerenderte Seite, und die gerenderte Seite selbst prüft ein Mensch in MarsDawn. Sie wird nie in den Kontext des Agenten zurückgelesen.</strong></p></div>

<h2>Der Werkzeugaufruf selbst ist günstig</h2>
<p>Ruf <code>marsdawn export</code> auf, über die CLI, den Skill oder <a href="/de/cli/mcp/">den MCP-Server</a>, und zurück kommt <a href="/de/cli/agents/">ein kompaktes JSON-Objekt</a>: <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> und <code>diagramErrors</code>. Das vollständige Schema ist <a href="/schemas/cli/export.v1.json">export.v1.json</a>. Nichts davon ist das gerenderte Dokument. Ein PDF mit 50 Seiten und einem Dutzend Mermaid-Diagrammen liefert dieselben paar Felder wie eine Notiz mit einer Seite.</p>

<h2>Geprüft wird nebenan</h2>
<p>Sobald das PDF existiert, öffnet es ein Mensch, in MarsDawn oder einem beliebigen PDF-Programm, und liest Diagramme, Formeln und Layout gerendert. Der Agent muss diese gerenderte Ausgabe nie in sein eigenes Kontextfenster zurücklesen, um zu bestätigen, dass sie stimmt: Geprüft wird in einem eigenen Fenster, auf einem eigenen Bildschirm, nicht in einer weiteren Runde von Tokens, die beschreiben, wie ein Diagramm aussieht.</p>

<h2>Was das vermeidet</h2>
<ul>
  <li>Gerendertes Markdown, einen Screenshot oder die Beschreibung davon in die Unterhaltung zurückzukopieren, nur damit der Agent bestätigen kann, dass der Export geklappt hat.</li>
  <li>Einen Agenten, der rekonstruieren muss, wie ein Mermaid-Diagramm oder eine KaTeX-Formel gerendert aussieht, statt dass ein Mensch einfach hinschaut.</li>
  <li>Einen zweiten Werkzeugaufruf, um den Inhalt des PDFs zu holen, nachdem der erste schon Erfolg gemeldet hat.</li>
</ul>

<h2>Weiter</h2>
<ul>
  <li>Die drei Wege, marsdawn aufzurufen, CLI, Skill-Datei, MCP-Server: <a href="/de/cli/mcp/">drei Zugänge</a>.</li>
  <li>Jedes Feld im JSON-Ergebnis: <a href="/de/cli/agents/">marsdawn für Agenten</a>.</li>
  <li>Warum ein Mensch trotzdem lesen muss, was ein Agent geschrieben hat: <a href="/de/reviewing-ai-output/">Warum Prüfen nötig ist</a>.</li>
  <li>Die ausführlichere Begründung, Agentenausgaben zu lesen, mit einer Checkliste: <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a>.</li>
</ul>
""",
    }

    pages['sharing-exported-pdfs'] = {
        "title": 'Teilen, was ein Agent geschrieben hat, ohne Markdown zu erklären · MarsDawn',
        "description": 'Exportiere das Markdown eines Agenten als PDF und gib es einer Kollegin, die kein Markdown liest und nichts installieren wird. Zum Öffnen braucht es keine Syntax, keine App und keinen Account.',
        "body": f"""
<section class="intro">
  <h1>Gib ihnen das PDF, nicht das Markdown.</h1>
  <p>Ein Agent stellt ein Dokument fertig, du prüfst und überarbeitest es, und dann muss es auch jemand außerhalb der Technik lesen: eine Führungskraft, ein Kunde, jemand aus einem anderen Team. Diese Leute müssen nicht wissen, was <code>##</code> oder eine Tabelle aus senkrechten Strichen bedeutet. Exportiere als PDF und gib ihnen stattdessen das.</p>
</section>

<div class="summary"><p><strong>Exportiere das geprüfte Dokument als PDF und schick diese Datei.</strong> Sie öffnet sich überall, braucht kein Markdown-Wissen und keine Installation und sieht so aus, wie du sie in der Vorschau gesehen hast, mit Diagrammen, Tabellen und Formatierung.</p></div>

<h2>Warum nicht einfach die .md-Datei schicken</h2>
<p>Eine rohe <code>.md</code>-Datei zeigt in einem einfachen Texteditor die Zeichen, nicht die Seite: <code>#</code> für eine Überschrift, <code>**</code> um fetten Text, einen abgegrenzten Block für ein Mermaid-Diagramm, das nicht gezeichnet wird. Wer kein Markdown schreibt, liest nichts davon so, wie es gemeint ist, und zu verlangen, zuerst einen Viewer zu installieren, ist für ein einziges Dokument viel verlangt.</p>

<h2>Warum kein Screenshot</h2>
<p>Ein Screenshot friert einen Bildschirm voll eines Dokuments ein, das mehrere Seiten lang sein kann, lässt sich weder durchsuchen noch markieren und wird schlechter lesbar, wenn er ein paarmal komprimiert und weitergeleitet wurde. Ein PDF erhält Text, Diagramme und Seitenumbrüche, bei jeder Länge.</p>

<h2>Was ein PDF dir bringt</h2>
<ul>
  <li>Es öffnet sich in dem, was die Empfänger schon haben, Vorschau, ein Browser, Acrobat, ihr Telefon, ganz ohne Markdown-Werkzeug.</li>
  <li>Mermaid-Diagramme sind gezeichnet, nicht als Code stehen gelassen; Codeblöcke behalten ihre Hervorhebung.</li>
  <li>Seitenumbrüche sind so gewählt, dass keine Überschrift allein unten auf einer Seite landet und keine Tabelle und kein Diagramm auf zwei Seiten verteilt wird.</li>
  <li>Dieselbe Datei, ob sie aus der MarsDawn-App kommt oder aus der kostenlosen Befehlszeile; die Anleitung dazu steht unter <a href="/de/markdown-to-pdf/">Markdown in PDF</a>.</li>
</ul>

<h2>Weiter</h2>
<ul>
  <li>Die Themen und Layouts, aus denen der Export kommen kann: <a href="/de/themes/">Vorschauthemen und PDF-Export</a>.</li>
  <li>Aus einem Skript oder von einem Agenten exportieren statt aus der App: <a href="/de/cli/agents/">marsdawn für Agenten</a>.</li>
  <li>Warum ein Mensch das Dokument zuerst lesen muss: <a href="/de/reviewing-ai-output/">Warum Prüfen nötig ist</a>.</li>
  <li>Übergaben zwischen mehreren Agenten sind eine natürliche Quelle für PDFs zum Teilen: <a href="/de/agent-design-patterns/">Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt</a>.</li>
</ul>
""",
    }

    pages['reviewing-ai-output'] = {
        "title": 'Warum KI-Ausgaben immer noch menschliche Leser brauchen · MarsDawn',
        "description": 'Von KI geschriebenes Markdown muss ein Mensch verstehen, nicht auf den ersten Blick glauben. MarsDawn stellt die gerenderte Seite neben den Quelltext und zeichnet Mermaid-Diagramme und KaTeX-Formeln, damit die Struktur auf einen Blick lesbar ist.',
        "body": f"""
<section class="intro">
  <h1>Ein Agent schreibt es. Verstehen musst du es trotzdem.</h1>
  <p>Ein KI-Agent entwirft schnell einen Plan, eine Spezifikation oder Notizen. Was er erzeugt, muss trotzdem der Mensch verstehen, der danach handelt, statt ihm zu glauben, nur weil es sich flüssig liest.</p>
</section>

<div class="summary"><p><strong>MarsDawn ist für genau dieses Lesen gebaut: die gerenderte Seite neben dem Quelltext, mit gezeichneten Mermaid-Diagrammen und KaTeX-Formeln statt bloßer Zeichen, damit die Struktur eines Dokuments auf einen Blick lesbar ist.</strong></p></div>

<h2>Flüssig ist nicht dasselbe wie richtig</h2>
<p>Simon Willison schrieb über KI-gestütztes Programmieren und Code, an dem weitergearbeitet wird, statt ihn wegzuwerfen: „Die Qualität und Verständlichkeit des zugrunde liegenden Codes ist entscheidend“ (<a href="https://simonwillison.net/2025/Mar/6/vibe-coding/">Vibe coding</a>, 2025). Für ein Dokument gilt dasselbe: Der Entwurf eines Agenten, der sich glatt liest, kann trotzdem Struktur, Zahlen oder Logik falsch haben, und flüssige Sätze verraten nicht, welche Teile man prüfen muss.</p>

<h2>Schlussfolgern, nicht kompilieren</h2>
<p>Birgitta Böckeler zieht für Thoughtworks die Grenze klar: „LLMs sind KEINE Compiler, Interpreter, Transpiler oder Assembler natürlicher Sprache, sie ziehen Schlüsse“ (<a href="https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html">I still care about the code</a>). Ein Compiler nimmt deine Eingabe entweder an oder meldet einen Fehler; ein Agent kann etwas zurückgeben, das läuft oder sich liest, ohne richtig zu sein. Jemand muss es trotzdem prüfen.</p>

<h2>Was MarsDawn diesem Leser gibt</h2>
<ul>
  <li>Die gerenderte Seite neben dem Quelltext, aktualisiert, wenn sich eine der beiden Seiten ändert, sodass eine Aussage im Text und ihre Struktur gleichzeitig im Blick sind.</li>
  <li>Gezeichnete Mermaid-Diagramme: Ein Flussdiagramm, das ein Agent in Text beschrieben hat, wird zu einer Form, der du tatsächlich folgen kannst.</li>
  <li>Gerenderte KaTeX-Formeln statt einer Kette von Backslashes: Eine Formel liest sich wie eine Formel.</li>
  <li>Nichts läuft von allein. MarsDawn bewertet, fasst zusammen oder markiert das Dokument nicht für dich; es legt dir die Struktur vor, damit du es kannst.</li>
</ul>

<h2>Weiter</h2>
<ul>
  <li>Wie dieses Prüfen für den eigenen Kontext des Agenten günstig bleibt: <a href="/de/token-efficient-review/">Token-sparsames Prüfen</a>.</li>
  <li>Das geprüfte Dokument an jemand anderen weitergeben: <a href="/de/sharing-exported-pdfs/">ein PDF teilen</a>.</li>
  <li>Warum das Lesen schwer ist und wie es geht: <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a>.</li>
  <li>Warum Agenten ihre Pläne überhaupt offenlegen: <a href="/de/agent-transparency/">Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?</a></li>
  <li>Was MarsDawn ist, auf einer Seite: <a href="/de/">die Startseite</a>.</li>
</ul>
""",
    }

    pages['reading-agent-output'] = {
        "title": 'Lesen, was dein Agent zurückgibt · MarsDawn',
        "description": 'KI-Agenten geben ihre Arbeit als Markdown zurück: Pläne, Spezifikationen, Fortschrittsberichte. Was Leute, die Agenten bauen, über Checkpoints und Fehler sagen, warum diese Ausgabe schwer zu lesen ist, und eine Checkliste, um einen Plan in fünf Minuten zu prüfen.',
        "body": f"""
<section class="intro">
  <h1>Die Arbeit deines Agenten kommt als Markdown-Datei zurück.</h1>
  <p>Du bittest einen Coding-Agenten, eine Migration zu planen, eine Spezifikation zu schreiben oder einem Bug nachzugehen. Er arbeitet eine Weile allein und gibt dir dann eine Datei: <code>plan.md</code>, <code>SPEC.md</code>, einen Fortschrittsbericht, eine Recherchezusammenfassung. Soweit du die Arbeit prüfen kannst, ist diese Datei die Arbeit.</p>
</section>

<div class="summary"><p><strong>Ob der Agent es richtig gemacht hat, erfährst du, indem du liest, was er zurückgibt. MarsDawn ist eine Mac-App für dieses Lesen.</strong></p></div>

<h2>Was Leute sagen, die Agenten bauen</h2>
<p>Zitiert wie geschrieben; unsere Lesart folgt danach.</p>
<ul>
  <li>Anthropics „Building Effective Agents“ (Erik S. und Barry Zhang, Dezember 2024) nennt drei Grundprinzipien für den Bau von Agenten. Eines lautet: „Setze auf Transparenz, indem du die Planungsschritte des Agenten ausdrücklich zeigst.“ Es richtet sich an Leute, die Agenten bauen. Von deiner Seite aus ist diese Transparenz der Plan, den du am Ende liest.</li>
  <li>Derselbe Beitrag: „Agenten können dann an Checkpoints oder bei Hindernissen für menschliches Feedback pausieren.“ Achte auf das Verb: <em>können</em>.</li>
  <li>Chip Huyen in „Agents“ (Januar 2025) darüber, warum Planung von Ausführung getrennt sein sollte: „Ohne Aufsicht kann ein Agent diese Schritte stundenlang ausführen und Zeit und Geld für API-Aufrufe verschwenden, bevor du merkst, dass er nicht vorankommt.“ Sie beschreibt auch einen Fehler, bei dem „der Agent überzeugt ist, eine Aufgabe erledigt zu haben, obwohl er es nicht hat“. Soll er 50 Personen auf 30 Hotelzimmer verteilen, bringt er 40 unter und besteht darauf, fertig zu sein.</li>
  <li>Andrew Ng über das Entwurfsmuster Planung in The Batch (April 2024): „Einerseits ist Planung eine sehr mächtige Fähigkeit; andererseits führt sie zu weniger vorhersehbaren Ergebnissen.“ Das ist eine Aussage über Vorhersehbarkeit, kein Aufruf zu menschlicher Prüfung, und er erwartet, dass Planung schnell besser wird.</li>
</ul>
<p><strong>Unsere Schlussfolgerung, nicht ihre:</strong> Wenn ein Agent seinen Plan offenlegt und an Checkpoints anhält, liest jemand diesen Plan am Checkpoint, und meistens bist das du. Wenn ein Agent glauben kann, fertig zu sein, obwohl er es nicht ist, braucht auch sein Fertig-Bericht einen Leser. Keiner dieser Autoren erwähnt MarsDawn oder empfiehlt es oder ein anderes Markdown-Werkzeug.</p>

<h2>Warum das Lesen schwerer ist, als es aussieht</h2>
<p>Die Datei ist lang, und der wichtige Teil steht selten oben. Sie enthält Mermaid-Diagramme und Formeln, die als Quelltext schwer zu verfolgen sind. Der Agent schreibt sie vielleicht noch um, während du bei der Hälfte bist. Oft ist sie eine von mehreren Dateien, manchmal über Branches oder Worktrees verteilt. Und wenn du ein Problem findest, lässt „der Cache-Teil sieht komisch aus“ den Agenten raten; „<code>docs/plan.md:42</code> löscht die alte Tabelle, bevor das Backfill fertig ist“ nicht.</p>

<h2>Wo MarsDawn hilft</h2>
<ul>
  <li><strong>Lange Dateien:</strong> Der Tab Gliederung in der Seitenleiste (&#8963;&#8984;S) listet die Überschriften. Klick auf eine, und beide Bereiche springen dorthin.</li>
  <li><strong>Diagramme und Formeln:</strong> Mermaid und KaTeX werden in der Vorschau neben dem Quelltext gezeichnet (&#8984;2), und beide Bereiche scrollen gemeinsam.</li>
  <li><strong>Umgeschrieben, während du liest:</strong> Wenn der Agent die Datei umschreibt, lädt MarsDawn sie neu und behält deine Stelle, solange du keine eigenen ungesicherten Änderungen hast.</li>
  <li><strong>Mehrere Dateien:</strong> Öffne den Ordner des Agenten mit Ablage &#9656; Ordner öffnen &#8230; (&#8679;&#8984;O). Neue Dateien erscheinen innerhalb etwa einer Sekunde im Tab Dateien, und bei einem Git-Checkout nennt die Kopfzeile den Branch oder Worktree.</li>
  <li><strong>Genaues Feedback:</strong> Bearbeiten &#9656; Verweis kopieren (&#8997;&#8984;C) kopiert deine Stelle als <code>docs/plan.md:42</code>. Für KI kopieren (&#8963;&#8997;&#8984;C) fügt den ausgewählten Text darunter ein. Füge beides in den Chat mit dem Agenten ein.</li>
</ul>
<p>Zwei weitere für den Ablauf: Ein Agent kann <code>marsdawn open plan.md:42</code> ausführen, um die Datei in MarsDawn bei Zeile 42 zu öffnen, der Zeile, die du zuerst sehen sollst, und eine geprüfte Datei lässt sich aus der App oder mit dem kostenlosen Befehl <code>marsdawn export</code> als PDF exportieren.</p>
<p>In MarsDawn steckt kein KI-Modell. Es fasst den Plan nicht zusammen, bewertet ihn nicht und sagt dir nicht, was falsch ist. Du liest; es hält eine lange, sich ändernde Datei lesbar und lässt dich auf die genaue Zeile zeigen.</p>

<h2>Einen Agentenplan in fünf Minuten prüfen</h2>
<p>Das funktioniert in jedem Editor.</p>
<ol>
  <li>Lies nur die Überschriften. Passt die Gliederung zu dem, worum du gebeten hast? Ein fehlender Abschnitt bedeutet meist fehlende Arbeit.</li>
  <li>Finde jede Stelle, die sagt, dass etwas erledigt, bestanden oder geprüft ist, und prüfe eine selbst: Öffne die Datei, führe den Test aus, zähle die Zeilen.</li>
  <li>Achte auf Schritte, die sich nicht rückgängig machen lassen: Daten löschen, Migrationen, Force-Pushes, alles, was sendet, bezahlt oder veröffentlicht. Die warten auf dein ausdrückliches Ja.</li>
  <li>Lies die Diagramme gerendert und prüfe jeden Pfeil gegen den Text.</li>
  <li>Liste die Dateien und Systeme auf, die der Plan berührt. Frag nach allem, worum du nicht gebeten hast, bevor es läuft.</li>
  <li>Schreib Feedback als Stelle, Problem, Lösung: „<code>plan.md:88</code>: Das Backfill läuft nach dem Löschen. Tausche die Schritte 4 und 5.“ Ein Problem pro Zeile.</li>
</ol>
<p>Wenig Zeit? Mach Schritt 2. Dort fliegt ein Agent auf, der glaubt, fertig zu sein. Die ausführliche Version mit einem durchgespielten Beispiel: <a href="/de/reviewing-agent-plans/">Einen Agentenplan in fünf Minuten prüfen</a>.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn gibt es im <a href="{k.LISTING_URL}">Mac App Store</a>. Dazu kommt das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code>:</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Es exportiert Markdown ohne die App als PDF, und mit <code>marsdawn open</code> kann dein Agent Dateien für dich in MarsDawn öffnen.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; <a href="/de/cli/agents/">marsdawn für Agenten</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Die kurze Begründung, KI-Ausgaben überhaupt zu lesen: <a href="/de/reviewing-ai-output/">Warum KI-Ausgaben immer noch menschliche Leser brauchen</a>.</li>
  <li>Den Kontext des Agenten klein halten, während du prüfst: <a href="/de/token-efficient-review/">Token-sparsames Prüfen</a>.</li>
  <li>Warum Agenten ihre Pläne überhaupt offenlegen: <a href="/de/agent-transparency/">Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?</a></li>
  <li>Die Checkliste oben, Schritt für Schritt mit einem Beispiel: <a href="/de/reviewing-agent-plans/">Einen Agentenplan in fünf Minuten prüfen</a>.</li>
  <li>Welche Dokumente verschiedene Arten von Agenten dir übergeben: <a href="/de/agent-design-patterns/">Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt</a>.</li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Erik S. und Barry Zhang, „Building Effective Agents“, Anthropic, 19. Dezember 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (zitiert nach der am 26.09.2026 online verfügbaren Fassung; der Beitrag weist inzwischen darauf hin, dass sich vieles an den beschriebenen Werkzeugen seit Dezember 2024 geändert hat).</li>
  <li>Chip Huyen, „Agents“, 7. Januar 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Andrew Ng, „Agentic Design Patterns Part 4, Planning“, The Batch, 10. April 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
</ul>
""",
    }

    pages['agent-transparency'] = {
        "title": 'Agenten sollen transparent sein. Wer liest, was sie zeigen? · MarsDawn',
        "description": 'Anthropics Leitfaden zum Bau von Agenten verlangt Transparenz: Zeig die Planungsschritte. Was er sagt, was nicht, und warum die Schritte meist als Markdown-Datei enden, die jemand lesen muss.',
        "body": f"""
<section class="intro">
  <h1>Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?</h1>
  <p>Im Dezember 2024 veröffentlichte Anthropic „Building Effective Agents“, einen Leitfaden für Leute, die KI-Agenten bauen. Seine Zusammenfassung nennt drei Prinzipien, und eines davon ist Transparenz. In diesem Beitrag geht es um das andere Ende dieses Prinzips: Sobald ein Agent seine Schritte offenlegt, muss sie jemand lesen.</p>
</section>

<div class="summary"><p><strong>Transparenz ist etwas, das der Agent tut. Lesen ist etwas, das du tust. Anthropic bittet die Entwickler, die Planungsschritte eines Agenten zu zeigen; für die meisten, die einen Coding-Agenten steuern, kommen diese Schritte als Markdown-Datei an, die jemand im richtigen Moment lesen muss.</strong></p></div>

<h2>Was der Leitfaden sagt</h2>
<p>Erik S. und Barry Zhang fassen ihren Rat so zusammen:</p>
<blockquote><p>„Bei der Umsetzung von Agenten versuchen wir, drei Grundprinzipien zu folgen: Halte das Design deines Agenten einfach. Setze auf Transparenz, indem du die Planungsschritte des Agenten ausdrücklich zeigst. Gestalte die Schnittstelle zwischen Agent und Computer (ACI) sorgfältig, mit gründlicher Werkzeugdokumentation und gründlichen Tests.“</p></blockquote>
<p>Das sind Entwurfsprinzipien für Leute, die Agenten bauen, keine Anleitung für die Person, die einen benutzt. Das Prinzip verlangt, dass die Schritte gezeigt werden. Es sagt nicht, wer sie liest.</p>
<p>Derselbe Beitrag beschreibt, was ein Agent tut, sobald er eine Aufgabe hat: „Sobald die Aufgabe klar ist, planen und handeln Agenten selbstständig und kehren möglicherweise zum Menschen zurück, um weitere Informationen oder eine Einschätzung einzuholen.“ Und: „Agenten können dann an Checkpoints oder bei Hindernissen für menschliches Feedback pausieren.“ Achte auf die Wörter <em>möglicherweise</em> und <em>können</em>. Checkpoints werden als etwas beschrieben, das ein Agent haben kann, nicht haben muss.</p>

<h2>Das meiste Prüfen machst nicht du</h2>
<p>Das lässt sich leicht übertreiben, darum hier, was der Leitfaden tatsächlich an erste Stelle setzt. Der Agent prüft sich selbst an der Welt: „Während der Ausführung ist es entscheidend, dass die Agenten bei jedem Schritt ‚Ground Truth‘ aus der Umgebung erhalten (etwa Ergebnisse von Werkzeugaufrufen oder Codeausführung), um ihren Fortschritt zu beurteilen.“ In diesem Satz meint Ground Truth Testergebnisse und Werkzeugausgaben. Es meint keinen Menschen.</p>
<p>Der Leitfaden ist auch beim Risiko direkt: „Die autonome Natur von Agenten bedeutet höhere Kosten und die Gefahr sich aufschaukelnder Fehler.“ Seine Antwort sind ausgiebige Tests in abgeschotteten Umgebungen, mit Schutzvorkehrungen. Er sagt nicht „lies sorgfältiger“.</p>
<p>Ein Mensch kommt später doch ins Spiel, im Anhang über Coding-Agenten: „Während automatisierte Tests helfen, die Funktion zu prüfen, bleibt menschliche Prüfung entscheidend, um sicherzustellen, dass Lösungen zu den umfassenderen Systemanforderungen passen.“ Dieser Satz handelt von Code. Die Lücke, auf die er zeigt, kennt man aber von jedem Agenten: Ein Test kann dir sagen, dass etwas funktioniert, nicht, dass es das ist, was du gemeint hast.</p>

<h2>Wo die Schritte landen</h2>
<p><strong>Ab hier ist das unsere Lesart, nicht die von Anthropic.</strong></p>
<p>Wenn du täglich mit einem Coding-Agenten arbeitest, tauchen seine Planungsschritte meist nicht in einem Dashboard auf. Sie tauchen als Dateien auf: <code>plan.md</code>, eine Aufgabenliste mit Kontrollkästchen, eine Fortschrittsdatei, die der Agent ständig umschreibt, eine Zusammenfassung am Ende. Transparenz heißt von deiner Seite aus: mehr zu lesen.</p>
<p>Die Schritte zu zeigen ist die Hälfte des Agenten. Die andere Hälfte ist ein Mensch, der sie liest, wenn es darauf ankommt: bevor die Migration läuft, bevor der Branch gemergt wird, bevor „fertig“ akzeptiert wird. Ein Agent, der alles in einer Datei mit 600 Zeilen offenlegt, die niemand öffnet, ist auf dem Papier transparent und in der Praxis unbeaufsichtigt.</p>
<p>Harrison Chase machte 2024 einen verwandten Punkt, als er darüber schrieb, wie Agenten-Frameworks funktionieren sollten, nicht über Dokumente: „Du wirst beobachten können wollen, was im Inneren vor sich geht, da die genauen Schritte vorher womöglich nicht bekannt sind.“ Er sprach über Werkzeuge für die Leute, die Agenten bauen. Wenn du derjenige bist, der den Agenten steuert, ist die schlichte Datei, die er ständig schreibt, oft der Teil, den du beobachten kannst.</p>
<p>Keiner dieser Autoren erwähnt MarsDawn, und keiner empfiehlt es oder ein anderes Markdown-Werkzeug.</p>

<h2>Warum dieses Lesen schwerer ist, als es aussieht</h2>
<p>Die Datei ist lang, und das Wichtige steht selten oben. Das Diagramm, das die Änderung erklärt, ist Mermaid-Quelltext, kein Bild (wie du es gezeichnet siehst, steht unter <a href="/de/view-markdown-on-mac/">Eine Markdown-Datei auf dem Mac ansehen</a>). Der Agent schreibt die Datei vielleicht um, während du bei der Hälfte bist. Oft gibt es mehr als eine Datei, manchmal auf verschiedenen Branches oder Worktrees. Und wenn du ein Problem entdeckst, lässt „der Cache-Teil sieht komisch aus“ den Agenten raten. Die längere Version davon steht unter <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a>.</p>

<h2>Wo MarsDawn passt und wo nicht</h2>
<p>MarsDawn ist eine Mac-App für dieses Lesen. Es macht einen Agenten nicht transparenter, und es steckt kein KI-Modell darin: Es fasst den Plan nicht zusammen und sagt dir nicht, ob er stimmt. Was es tut:</p>
<ul>
  <li><strong>Lange Dateien:</strong> Darstellung &#9656; Seitenleiste einblenden (&#8963;&#8984;S) öffnet den Tab Gliederung, der die Überschriften listet. Klick auf eine, um dorthin zu springen.</li>
  <li><strong>Diagramme und Formeln:</strong> Quelltext und gerenderte Seite stehen nebeneinander (&#8984;2) und scrollen gemeinsam, mit gezeichnetem Mermaid und KaTeX. Ist ein Diagramm fehlerhaft, zeigt die Vorschau seinen Quelltext mit dem Fehler darunter.</li>
  <li><strong>Umgeschrieben, während du liest:</strong> Wenn der Agent die Datei umschreibt, lädt MarsDawn sie neu und behält deine Stelle, solange du keine eigenen ungesicherten Änderungen hast.</li>
  <li><strong>Mehrere Dateien:</strong> Öffne den Ordner des Agenten mit Ablage &#9656; Ordner öffnen &#8230; (&#8679;&#8984;O). Neue Dateien erscheinen innerhalb etwa einer Sekunde im Tab Dateien, und bei einem Git-Checkout nennt die Kopfzeile den Branch oder Worktree.</li>
  <li><strong>Auf eine Zeile zeigen:</strong> Bearbeiten &#9656; Verweis kopieren (&#8997;&#8984;C) kopiert deine Stelle als <code>docs/plan.md:42</code>, und Für KI kopieren (&#8963;&#8997;&#8984;C) fügt den ausgewählten Text darunter ein, bereit zum Einfügen in den Chat mit dem Agenten.</li>
</ul>
<p>Lesen musst du trotzdem selbst. MarsDawn hält eine lange, sich ändernde Datei lesbar, während du es tust.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn gibt es im <a href="{k.LISTING_URL}">Mac App Store</a>. Dazu kommt das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code>:</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Es exportiert Markdown ohne die App als PDF.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Warum Agentenausgaben schwer zu lesen sind, mit einer Checkliste: <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a>.</li>
  <li>Die Checkliste Schritt für Schritt mit einem Beispiel: <a href="/de/reviewing-agent-plans/">Einen Agentenplan in fünf Minuten prüfen</a>.</li>
  <li>Welche Dokumente verschiedene Arten von Agenten dir übergeben: <a href="/de/agent-design-patterns/">Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt</a>.</li>
  <li>Die kurze Begründung, KI-Ausgaben überhaupt zu lesen: <a href="/de/reviewing-ai-output/">Warum KI-Ausgaben immer noch menschliche Leser brauchen</a>.</li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Erik S. und Barry Zhang, „Building Effective Agents“, Anthropic, 19. Dezember 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (zitiert nach der am 26.09.2026 online verfügbaren Fassung; der Beitrag weist inzwischen darauf hin, dass sich vieles an den beschriebenen Werkzeugen seit Dezember 2024 geändert hat).</li>
  <li>Harrison Chase, „What is an agent?“, LangChain, 28. Juni 2024, archivierte Kopie: <a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a> (unter der ursprünglichen Adresse steht inzwischen ein anderer Artikel von 2026).</li>
</ul>
""",
    }

    pages['reviewing-agent-plans'] = {
        "title": 'Einen Agentenplan in fünf Minuten prüfen · MarsDawn',
        "description": 'Ein Weg in sechs Schritten, den Plan eines KI-Agenten zu prüfen, bevor er läuft, in etwa fünf Minuten und in jedem Editor, mit einem durchgespielten Beispiel.',
        "body": f"""
<section class="intro">
  <h1>Einen Agentenplan in fünf Minuten prüfen</h1>
  <p>Dein Agent hat einen Plan geschrieben und wartet auf grünes Licht. Du hast fünf Minuten, keine Stunde. Hier ist ein Weg, sie zu nutzen, der in jedem Editor funktioniert, sogar in einem einfachen Texteditor. MarsDawn hilft bei einigen Schritten, und wir sagen, bei welchen. Beim wichtigsten hilft es nicht.</p>
</section>

<div class="summary"><p><strong>Lies den Plan nicht von oben nach unten. Prüfe seine Form, prüfe eine Behauptung, finde, was sich nicht rückgängig machen lässt, sieh dir Diagramme und Umfang an und schreib dann Feedback, mit dem der Agent arbeiten kann. Sechs Schritte, etwa fünf Minuten.</strong></p></div>

<h2>Warum vorher prüfen</h2>
<p>Chip Huyen erklärt, warum Planung von Ausführung getrennt sein sollte, und benennt die Kosten deutlich: „Ohne Aufsicht kann ein Agent diese Schritte stundenlang ausführen und Zeit und Geld für API-Aufrufe verschwenden, bevor du merkst, dass er nicht vorankommt.“ Unsere Ergänzung: Ein Plan ist der günstigste Ort, einen Fehler zu finden. Eine Zeile in <code>plan.md</code> zu korrigieren kostet einen Satz. Zu korrigieren, was der Agent getan hat, nachdem er gelaufen ist, kostet einen Nachmittag.</p>

<h2>Das Beispiel</h2>
<p>Du hast einen Agenten gebeten, Benutzer-Avatare in einen Objektspeicher zu verschieben, ohne bestehende Links zu brechen. Er gibt dir das hier zurück:</p>
<pre><code># Plan: move user avatars to object storage

## Goal
Serve avatars from object storage instead of the app server.

## Steps
1. Add a storage client and config. &#9989; done
2. Write a script that copies existing avatars to the bucket.
3. Switch the avatar URLs in the templates.
4. Delete `public/avatars/` from the server.
5. Run the copy script.

## Status
All tests pass.</code></pre>
<p>Es liest sich gut. Es würde auch jeden Avatar löschen, bevor auch nur einer kopiert ist.</p>

<h2>Die sechs Schritte</h2>
<p><strong>1. Lies nur die Überschriften.</strong> <em>(etwa eine Minute)</em> Passt die Gliederung zu dem, worum du gebeten hast? Ein fehlender Abschnitt bedeutet meist fehlende Arbeit. Hier: Goal, Steps, Status. Du wolltest, dass bestehende Links weiter funktionieren, und es gibt keine Überschrift zu alten Links oder dazu, wie man die Änderung rückgängig macht. Das ist dein erster Kommentar.</p>
<p>Im Terminal gibt <code>grep -n '^#' plan.md</code> nur die Überschriften aus, und die meisten Editoren können auch eine Gliederung zeigen. In MarsDawn listet der Tab Gliederung in der Seitenleiste (Darstellung &#9656; Seitenleiste einblenden, &#8963;&#8984;S) sie auf, und ein Klick springt dorthin.</p>
<p><strong>2. Finde jede Stelle, die sagt, dass etwas erledigt, bestanden oder geprüft ist, und prüfe eine selbst.</strong> <em>(etwa eine Minute)</em> Öffne die Datei, führe den Test aus, zähle die Zeilen. Chip Huyen beschreibt einen Fehler, bei dem „der Agent überzeugt ist, eine Aufgabe erledigt zu haben, obwohl er es nicht hat“. In ihrem Beispiel soll ein Agent 50 Personen auf 30 Hotelzimmer verteilen, bringt 40 unter und besteht darauf, fertig zu sein.</p>
<pre><code>grep -n -i -E 'done|pass|verified|&#9989;' plan.md</code></pre>
<p>Hier findet das „&#9989; done“ und „All tests pass.“ Welche Tests? Berührt einer davon die Avatare? Führ sie aus oder frag nach. Diesen Schritt kann MarsDawn dir nicht abnehmen. Das kann niemand außer dir.</p>
<p><strong>3. Achte auf Schritte, die sich nicht rückgängig machen lassen.</strong> <em>(etwa eine Minute)</em> Daten löschen, Migrationen, Force-Pushes, alles, was sendet, bezahlt oder veröffentlicht. Die warten auf dein ausdrückliches Ja. Chip Huyen beschreibt dieselbe Idee von der Seite des Systems aus: „Wenn ein Plan riskante Vorgänge umfasst, etwa eine Datenbank zu aktualisieren oder eine Codeänderung zu mergen, kann das System vor der Ausführung ausdrücklich um menschliche Zustimmung bitten oder die Ausführung dieser Vorgänge Menschen überlassen.“ Hier löscht Schritt 4 die Originale, und er kommt vor Schritt 5, dem Kopieren.</p>
<p><strong>4. Lies die Diagramme gerendert und prüfe jeden Pfeil gegen den Text.</strong> Ein Flussdiagramm, das „kopieren &#8594; prüfen &#8594; löschen“ sagt, während die Schritte etwas anderes sagen, ist ein Befund. Dieser Plan hat kein Diagramm, also fällt der Schritt heute weg. Wenn es eines gibt, sieh dir das Bild an, nicht den Mermaid-Quelltext: Viele Editoren haben eine Vorschau, und <a href="/de/view-markdown-on-mac/">Eine Markdown-Datei auf dem Mac ansehen</a> und <a href="/de/vs/markdown-preview-tools/">Markdown anderswo ansehen</a> zeigen die Möglichkeiten. In MarsDawn steht das gerenderte Diagramm neben seinem Quelltext (&#8984;2), und ein fehlerhaftes Diagramm zeigt seinen Quelltext mit dem Fehler darunter, was einen eigenen Kommentar wert ist.</p>
<p><strong>5. Liste die Dateien und Systeme auf, die der Plan berührt, und frag nach allem, worum du nicht gebeten hast.</strong> <em>(Schritte 4 und 5 zusammen, etwa eine Minute)</em> Hier: die Speicherkonfiguration, die Templates, ein Ordner auf dem Server, ein Bucket. Wer kann den Bucket lesen? Du hast nicht gesagt, dass er öffentlich sein soll. Wenn du den Arbeitsordner des Agenten in MarsDawn geöffnet hast (Ablage &#9656; Ordner öffnen&#160;&#8230;, &#8679;&#8984;O), erscheinen neue Dateien, die er schreibt, innerhalb etwa einer Sekunde im Tab Dateien, und die Kopfzeile nennt den Git-Branch oder Worktree, damit du weißt, welchen Checkout du prüfst.</p>
<p><strong>6. Schreib Feedback als Stelle, Problem, Lösung, ein Problem pro Zeile.</strong> <em>(die letzte Minute)</em></p>
<pre><code>plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.</code></pre>
<p>Jeder Editor mit Zeilennummern genügt. In MarsDawn kopiert Bearbeiten &#9656; Verweis kopieren (&#8997;&#8984;C) deine Stelle als <code>plan.md:10</code>, und Für KI kopieren (&#8963;&#8997;&#8984;C) fügt den ausgewählten Text darunter ein.</p>

<h2>Wenn du nur eine Minute hast</h2>
<p>Mach Schritt 2. Dort fliegt ein Agent auf, der glaubt, fertig zu sein.</p>

<h2>Wenn fünf Minuten nicht reichen</h2>
<p>Manchmal kannst du nicht beurteilen, ob ein Schritt richtig ist, weil er außerhalb deines Wissens liegt. Jess Ou bringt es in LangChains Erklärtext über Agenten von 2026 in zwei Sätzen auf den Punkt: „Lagere kein Urteil aus, das du nicht bewerten kannst. Wenn du eine richtige Antwort nicht erkennen würdest, erkennt der Agent sie auch nicht.“ Unsere Folgerung: Wenn du einen Schritt nicht beurteilen kannst, ist das kein Grund, ihn schneller freizugeben. Es ist ein Grund, jemanden zu fragen, der es kann.</p>

<h2>Was MarsDawn hier tut und was nicht</h2>
<p>In MarsDawn steckt kein KI-Modell. Es findet die Probleme in diesem Plan nicht und übernimmt weder Schritt 2 noch Schritt 3. Es hält die Datei lesbar, während du arbeitest: die Gliederung für Schritt 1, gerenderte Diagramme für Schritt 4, den Tab Dateien für Schritt 5, Zeilenverweise für Schritt 6. Und wenn der Agent den Plan überarbeitet, während du liest, lädt MarsDawn ihn neu und behält deine Stelle, solange du keine eigenen ungesicherten Änderungen hast.</p>
<p>Wenn der Plan steht und jemand anderes ihn sehen muss, zeigen <a href="/de/sharing-exported-pdfs/">Exportierte PDFs teilen</a> und <a href="/de/markdown-to-pdf/">Markdown in PDF</a>, wie du ihn als PDF weitergibst.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn gibt es im <a href="{k.LISTING_URL}">Mac App Store</a>. Dazu kommt das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code>:</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Es exportiert Markdown ohne die App als PDF.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Warum Agentenausgaben überhaupt schwer zu lesen sind: <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a>.</li>
  <li>Warum Agenten ihre Pläne überhaupt offenlegen: <a href="/de/agent-transparency/">Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?</a></li>
  <li>Pläne sind nicht das Einzige, was Agenten zurückgeben: <a href="/de/agent-design-patterns/">Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt</a>.</li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Chip Huyen, „Agents“, 7. Januar 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Jess Ou, „What is an AI agent?“, LangChain, 31. Juli 2026: <a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a></li>
</ul>
""",
    }

    pages['agent-design-patterns'] = {
        "title": 'Vier Agenten-Entwurfsmuster und die Dokumente, die sie dir übergeben · MarsDawn',
        "description": 'Reflexion, Werkzeugnutzung, Planung und Zusammenarbeit mehrerer Agenten, wie Andrew Ng sie beschrieben hat, und was jedes Muster dir typischerweise zum Lesen zurückgibt.',
        "body": f"""
<section class="intro">
  <h1>Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt</h1>
  <p>Im März 2024 beschrieb Andrew Ng in seinem Newsletter The Batch vier Entwurfsmuster für KI-Agenten: Reflexion, Werkzeugnutzung, Planung und Zusammenarbeit mehrerer Agenten. Meist werden sie aus Sicht der Entwickler besprochen, als Wege, bessere Ergebnisse aus einem Modell zu holen. Dieser Beitrag schaut von der anderen Seite. Wenn du einen Agenten nutzt, der auf einem dieser Muster aufbaut: Was landet in deinem Ordner, und was solltest du zuerst lesen?</p>
</section>

<div class="summary"><p><strong>Die vier Muster stammen von Andrew Ng. Welche Dokumente jedes typischerweise übergibt und was du darin prüfen solltest, ist unsere eigene Schlussfolgerung. Er schreibt über beides nicht und plädiert in dieser Reihe nicht für menschliche Prüfung.</strong></p></div>

<h2>Die vier Muster in Kürze</h2>
<p>Ng beschreibt sie in „Agentic Design Patterns Part 1“. Kurz gesagt: Bei <strong>Reflexion</strong> sieht das Modell seine eigene Arbeit durch und verbessert sie. Bei <strong>Werkzeugnutzung</strong> kann es Werkzeuge wie Websuche oder Codeausführung aufrufen. Bei <strong>Planung</strong> entwirft es einen Plan aus mehreren Schritten und führt ihn aus. Bei der <strong>Zusammenarbeit mehrerer Agenten</strong> teilen sich mehrere Agenten die Arbeit auf und besprechen sie.</p>
<p>In Teil 1 zeigt er den Nutzen anhand eines Coding-Benchmarks, HumanEval, mit Ergebnissen, die sein Team von mehreren Forschungsgruppen zusammengetragen hat: „GPT-3.5 (Zero-Shot) lag zu 48,1 % richtig. GPT-4 (Zero-Shot) schneidet mit 67,0 % besser ab. Die Verbesserung von GPT-3.5 zu GPT-4 verblasst jedoch neben der Einbindung in einen iterativen Agenten-Workflow. In eine Agentenschleife eingebettet erreicht GPT-3.5 sogar bis zu 95,1 %.“ Diese Zahlen beziehen sich auf einen einzigen Coding-Benchmark, und 95,1 % ist der beste Fall („bis zu“). Sie zeigen, dass Agenten-Workflows die Ausgabe verbessern können. Darüber, wer sie prüft, sagen sie nichts.</p>
<p><strong>Ab hier sind die Dokumente und die Prüfungen unsere Lesart, nicht die von Ng.</strong> Echte Agenten mischen die Muster außerdem. Ein Coding-Agent kann in einer Sitzung planen, Werkzeuge ausführen und seine eigene Arbeit prüfen, du bekommst also oft alle vier Arten von Dateien.</p>

<h2>1. Reflexion: ein Entwurf, der sich schon selbst geprüft hat</h2>
<p>Ngs Beitrag über Reflexion stellt sie als Automatisierung des Feedbacks dar, das sonst ein Mensch geben würde: „Was, wenn man den Schritt automatisiert, kritisches Feedback zu geben, sodass das Modell seine eigene Ausgabe automatisch kritisiert und seine Antwort verbessert?“</p>
<p><strong>Was es typischerweise übergibt:</strong> ein überarbeitetes Dokument, manchmal mit einem Abschnitt zur Selbstprüfung oder Zeilen wie „Randfälle doppelt geprüft“.</p>
<p><strong>Was du prüfen solltest:</strong> das Ergebnis gegen <em>deine</em> Anfrage, nicht gegen die Selbstkritik des Agenten. Selbstprüfung kann auf ihre eigene Art schiefgehen. Chip Huyen: „Eine interessante Art von Planungsfehler entsteht durch Fehler in der Reflexion. Der Agent ist überzeugt, eine Aufgabe erledigt zu haben, obwohl er es nicht hat.“ Lilian Weng schrieb im Juni 2023 in ihrem Blog Lil’Log, damals bei OpenAI, über die Modelle jener Zeit: „Mangelnde Fachkenntnis kann dazu führen, dass LLMs ihre Schwächen nicht kennen und daher die Richtigkeit von Aufgabenergebnissen nicht gut beurteilen können.“ (In der Studie, die sie beschrieb, stimmten die Bewertung der Ergebnisse durch ein LLM und die durch menschliche Fachleute nicht überein.) Wenn dort „geprüft“ steht, prüfe selbst eine Sache.</p>

<h2>2. Werkzeugnutzung: ein Bericht darüber, was lief</h2>
<p><strong>Was es typischerweise übergibt:</strong> eine Zusammenfassung dessen, was der Agent ausgeführt oder gesucht hat und was zurückkam. „Testsuite ausgeführt: alles grün.“ Eine Ergebnistabelle. Gefundene Links.</p>
<p>Anthropics Leitfaden beschreibt Werkzeugergebnisse als die Selbstkontrolle des Agenten: „Während der Ausführung ist es entscheidend, dass die Agenten bei jedem Schritt ‚Ground Truth‘ aus der Umgebung erhalten (etwa Ergebnisse von Werkzeugaufrufen oder Codeausführung), um ihren Fortschritt zu beurteilen.“ Diese Kontrolle findet im Agenten statt. Was bei dir ankommt, ist die Nacherzählung des Agenten davon.</p>
<p><strong>Was du prüfen solltest:</strong> dass sich jede Behauptung auf eine Ausgabe zurückführen lässt, die du sehen kannst. Gleiche eine Zahl in der Zusammenfassung mit der echten Ausgabe ab. Öffne einen der Links.</p>

<h2>3. Planung: <code>plan.md</code></h2>
<p><strong>Was es typischerweise übergibt:</strong> einen Plan, eine Spezifikation, eine Aufgabenliste mit Kontrollkästchen, die der Agent unterwegs abhakt.</p>
<p>Ng äußert sich in Teil 4 offen über dieses Muster:</p>
<blockquote><p>„Einerseits ist Planung eine sehr mächtige Fähigkeit; andererseits führt sie zu weniger vorhersehbaren Ergebnissen. Meiner Erfahrung nach kann ich die agentischen Entwurfsmuster Reflexion und Werkzeugnutzung zuverlässig zum Laufen bringen und damit die Leistung meiner Anwendungen verbessern, doch Planung ist eine weniger ausgereifte Technik, und es fällt mir schwer, vorab vorherzusagen, was sie tun wird.“</p></blockquote>
<p>Er ist aber auch zuversichtlich: „Doch das Gebiet entwickelt sich weiterhin rasant, und ich bin zuversichtlich, dass die Planungsfähigkeiten sich schnell verbessern werden.“</p>
<p><strong>Was du prüfen solltest:</strong> den Plan, bevor er läuft, mit <a href="/de/reviewing-agent-plans/">der Fünf-Minuten-Prüfung</a>: Form, eine Behauptung, Schritte, die sich nicht rückgängig machen lassen, Diagramme, Umfang. Wenn der Agent den Plan mittendrin umschreibt, vergleiche ihn mit der Fassung, die du freigegeben hast; liegt er in Git, zeigt <code>git diff plan.md</code>, was sich geändert hat. In MarsDawn zeigt der Tab Gliederung die Form eines langen Plans, und ein umgeschriebener Plan wird neu geladen, ohne dass du deine Stelle verlierst, solange du keine eigenen ungesicherten Änderungen hast.</p>

<h2>4. Zusammenarbeit mehrerer Agenten: mehrere Dateien, mehrere Autoren</h2>
<p><strong>Was es typischerweise übergibt:</strong> eine Spezifikation von einem Agenten, Umsetzungsnotizen von einem zweiten, eine Prüfung von einem dritten und Zusammenfassungen, die zwischen ihnen weitergereicht werden. Manchmal arbeitet jeder in einem eigenen Branch oder Worktree.</p>
<p><strong>Was du prüfen solltest:</strong> die Übergaben. Wo ein Agent die Arbeit eines anderen zusammenfasst, such nach einer Anforderung, die nicht mit hinübergekommen ist. Such nach zwei Dateien, die sich widersprechen, und entscheide, welche die maßgebliche ist, bevor jemand auf der anderen aufbaut. Öffne in MarsDawn den gemeinsamen Ordner mit Ablage &#9656; Ordner öffnen&#160;&#8230; (&#8679;&#8984;O): Neue Dateien erscheinen innerhalb etwa einer Sekunde im Tab Dateien, während die Agenten sie schreiben, und bei einem Git-Checkout nennt die Kopfzeile den Branch oder Worktree, damit zwei Fenster mit demselben Dateinamen aus verschiedenen Branches nicht gleich aussehen. Wenn das Ergebnis an Leute gehen muss, die kein Markdown lesen, zeigt <a href="/de/sharing-exported-pdfs/">Exportierte PDFs teilen</a> diesen Schritt.</p>

<h2>Auf einen Blick</h2>
<table>
<thead><tr><th>Muster (Ng)</th><th>Was es typischerweise übergibt (unsere Schlussfolgerung)</th><th>Zuerst lesen (unser Vorschlag)</th></tr></thead>
<tbody>
<tr><td>Reflexion</td><td>Ein überarbeiteter Entwurf, vielleicht mit Selbstprüfung</td><td>Das Ergebnis gegen deine eigene Anfrage; ein „geprüft“ selbst prüfen</td></tr>
<tr><td>Werkzeugnutzung</td><td>Ein Bericht darüber, was lief und was zurückkam</td><td>Eine Behauptung bis zur echten Ausgabe zurückverfolgen</td></tr>
<tr><td>Planung</td><td><code>plan.md</code>, eine Spezifikation, eine Aufgabenliste</td><td>Die Fünf-Minuten-Prüfung, bevor er läuft</td></tr>
<tr><td>Zusammenarbeit mehrerer Agenten</td><td>Mehrere Dateien von mehreren Agenten, vielleicht auf mehreren Branches</td><td>Die Übergaben und welche Datei die maßgebliche ist</td></tr>
</tbody>
</table>
<p>Keiner der hier zitierten Autoren erwähnt MarsDawn, und keiner empfiehlt es oder ein anderes Markdown-Werkzeug. In MarsDawn steckt kein KI-Modell: Es weiß nicht, welches Muster eine Datei erzeugt hat, und es übernimmt diese Prüfungen nicht für dich. Es hält die Dateien lesbar, während du sie machst.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn gibt es im <a href="{k.LISTING_URL}">Mac App Store</a>. Dazu kommt das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code>:</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>Es exportiert Markdown ohne die App als PDF: siehe <a href="/de/markdown-to-pdf/">Markdown in PDF</a>.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Warum Agentenausgaben schwer zu lesen sind, mit einer Checkliste: <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a>.</li>
  <li>Die Planungsprüfung vollständig: <a href="/de/reviewing-agent-plans/">Einen Agentenplan in fünf Minuten prüfen</a>.</li>
  <li>Was Transparenz von dir verlangt und was nicht: <a href="/de/agent-transparency/">Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?</a></li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Andrew Ng, „Agentic Design Patterns Part 1“, The Batch, 20. März 2024: <a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng, „Agentic Design Patterns Part 2, Reflection“, The Batch, 27. März 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/</a></li>
  <li>Andrew Ng, „Agentic Design Patterns Part 4, Planning“, The Batch, 10. April 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
  <li>Chip Huyen, „Agents“, 7. Januar 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Lilian Weng, „LLM Powered Autonomous Agents“, Lil’Log, 23. Juni 2023: <a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a></li>
  <li>Erik S. und Barry Zhang, „Building Effective Agents“, Anthropic, 19. Dezember 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (zitiert nach der am 26.09.2026 online verfügbaren Fassung).</li>
</ul>
""",
    }

    # /templates/ pages (scripts/templates_pages.py), one entry per table there, for #162 to merge.
    # The downloads are TEMPLATES byte for byte; Mermaid node labels are translated, as in ja.
    templates = {
        'ui_labels': {"templates": "Vorlagen", "templates-spec": "Spezifikationsvorlage",
                      "templates-flowchart": "Flussdiagramm-Vorlage", "templates-meeting-notes": "Protokollvorlage"},
        'labels': {"template": "Die Vorlage", "download": "{file} herunterladen", "looks": "So sieht sie aus",
                   "ask": "Frag deinen Agenten", "share": "Als PDF teilen", "doesnt": "Was sie nicht kann",
                   "faq": "Fragen", "more": "Weitere Vorlagen", "sep": ": ",
                   "img_alt": "Die erste Seite von {file}, mit marsdawn export als PDF exportiert."},
        'hub': {"title": "Markdown-Vorlagen · MarsDawn",
                "description": "Markdown-Vorlagen für die Dokumente, die ein Agent schreibt und du liest: eine Spezifikation, ein Flussdiagramm und ein Protokoll, jeweils mit einem Prompt für deinen Agenten.",
                "h1": "Markdown-Vorlagen",
                "lede": "Für die Dokumente, die ein Agent schreibt und du liest. Zu jeder Vorlage gehört ein Prompt für deinen Agenten. Öffne die ausgefüllte Datei in MarsDawn und lies, was er geschrieben hat.",
                "items": {"spec": ("Spezifikation (PRD)", "Problem, Ziele, Anforderungen, ein Ablaufdiagramm und Akzeptanzkriterien."),
                          "flowchart": ("Flussdiagramm", "ein Mermaid-Diagramm, darunter die Schritte ausgeschrieben."),
                          "meeting-notes": ("Protokoll", "Entscheidungen und Aufgaben, jeweils mit einer verantwortlichen Person.")}},
        'pages': {
            "spec": {
                "title": "Markdown-Vorlage für Spezifikationen (PRD) · MarsDawn",
                "description": "Eine Markdown-Vorlage für Spezifikationen mit Anforderungen, einem Mermaid-Ablaufdiagramm und Akzeptanzkriterien. Dein Agent füllt sie aus, du prüfst sie in MarsDawn.",
                "h1": "Markdown-Vorlage für Spezifikationen (PRD)",
                "lede": "Eine Spezifikation, die dein Agent ausfüllen und du in einem Rutsch lesen kannst: Problem, Ziele, Anforderungen, ein Ablaufdiagramm und Akzeptanzkriterien. Wenn du eine Anforderung änderst, bitte den Agenten, den Rest anzugleichen.",
                "caption": "Exportiert mit <code>marsdawn export spec.md</code>. Das kostenlose Befehlszeilenwerkzeug rendert wie die Vorschau von MarsDawn, Diagramm inklusive.",
                "prompt": "Schreib eine Spezifikation für [die Funktion] in spec.md und nutze dafür die Vorlage unter {url}. Gib jeder Anforderung eine ID und verwende dieselben IDs im Ablauf und in den Akzeptanzkriterien. Wenn du fertig bist, führe marsdawn open spec.md aus.",
                "share": "<code>marsdawn export spec.md</code> schreibt spec.pdf daneben, für alle, die kein Markdown lesen.",
                "doesnt": "MarsDawn zeigt die Spezifikation, die Tabelle und das Diagramm. Es prüft nicht, ob die Akzeptanzkriterien jede Anforderung abdecken. Das ist die Aufgabe des Agenten, und deine beim Lesen.",
                "faq": [("Muss für das Ablaufdiagramm etwas installiert sein?", "Nein. MarsDawn und <code>marsdawn export</code> zeichnen Mermaid selbst, auch offline."),
                        ("Kann ich die Spezifikation in MarsDawn bearbeiten?", "Ja. Es ist ein Markdown-Editor mit der Vorschau neben dem Quelltext. Der Agent sieht deine Änderung, wenn er die Datei das nächste Mal liest.")],
            },
            "flowchart": {
                "title": "Markdown-Vorlage für Flussdiagramme (Mermaid) · MarsDawn",
                "description": "Eine Mermaid-Flussdiagramm-Vorlage in Markdown, darunter die Schritte ausgeschrieben. Auf dem Mac in der Vorschau ansehen und als PDF exportieren.",
                "h1": "Markdown-Vorlage für Flussdiagramme",
                "lede": "Ein Mermaid-Flussdiagramm, darunter die Schritte ausformuliert, damit sich Diagramm und Text gegenseitig prüfen lassen. Nimm einen Schritt heraus und bitte den Agenten, den Rest zu korrigieren.",
                "caption": "Exportiert mit <code>marsdawn export flowchart.md</code>. Das kostenlose Befehlszeilenwerkzeug rendert wie die Vorschau von MarsDawn, Diagramm inklusive.",
                "prompt": "Zeichne den Ablauf für [den Prozess] in flowchart.md und nutze dafür die Vorlage unter {url}. Ein nummerierter Schritt pro Knoten, in derselben Reihenfolge. Wenn du fertig bist, führe marsdawn open flowchart.md aus.",
                "share": "<code>marsdawn export flowchart.md</code> – das Diagramm wird ins PDF gezeichnet.",
                "doesnt": "MarsDawn zeichnet, was im Mermaid steht. Es lässt dich das Diagramm nicht von Hand anordnen und hält die nummerierten Schritte nicht mit den Knoten synchron. Enthält das Mermaid einen Fehler, zeigt die Vorschau den Fehler statt eines Diagramms.",
                "faq": [("Welche Diagramme funktionieren?", "Alles, was Mermaid zeichnet: Flussdiagramme, Sequenzdiagramme, Zustandsdiagramme und mehr."),
                        ("Warum die Schritte zusätzlich ausschreiben?", "Wer überfliegt, sieht das Diagramm; wer prüft, braucht den Text. Der Agent kann beides im Gleichschritt halten.")],
            },
            "meeting-notes": {
                "title": "Markdown-Vorlage für Besprechungsprotokolle · MarsDawn",
                "description": "Eine Markdown-Vorlage für Besprechungsprotokolle mit Entscheidungen und Aufgaben, jeweils mit einer verantwortlichen Person. Dein Agent schreibt es, du prüfst es in MarsDawn.",
                "h1": "Markdown-Vorlage für Besprechungsprotokolle",
                "lede": "Zuerst die Entscheidungen, dann die Aufgaben, jeweils mit einer verantwortlichen Person. Lass deinen Agenten das Protokoll aus dem Transkript schreiben und lies es, bevor es rausgeht. Wenn sich eine Entscheidung ändert, bitte den Agenten, die Aufgaben anzugleichen.",
                "caption": "Exportiert mit <code>marsdawn export meeting-notes.md</code>. Das kostenlose Befehlszeilenwerkzeug rendert wie die Vorschau von MarsDawn.",
                "prompt": "Fasse diese Besprechung in meeting-notes.md zusammen und nutze dafür die Vorlage unter {url}. Zuerst die Entscheidungen, je eine Zeile; jede Aufgabe bekommt genau eine verantwortliche Person und ein Datum. Wenn du fertig bist, führe marsdawn open meeting-notes.md aus.",
                "share": "<code>marsdawn export meeting-notes.md</code> schreibt ein PDF, das du an die Nachfass-Mail hängen kannst.",
                "doesnt": "MarsDawn nimmt die Besprechung weder auf noch transkribiert es sie, und es verfolgt die Aufgaben nicht. Es zeigt das Protokoll so, wie es gelesen wird.",
                "faq": [("Funktionieren die Kontrollkästchen?", "Sie erscheinen in der Vorschau und im PDF als Kontrollkästchen. Zum Abhaken änderst du im Quelltext <code>[ ]</code> in <code>[x]</code>."),
                        ("Kann der Agent Protokoll und Aufgaben im Gleichschritt halten?", "Ja, genau darum geht es in der Schleife: Ändere das eine und bitte ihn, den Rest anzupassen. MarsDawn zeigt dir das Ergebnis.")],
            },
        },
        'templates': {
            "spec": """# Spezifikation: Name der Funktion

Status: Entwurf · Verantwortlich: Name · Aktualisiert: Datum

## Problem

_Was heute nicht stimmt, für wen, und woher wir das wissen._

## Ziele

- _Was gilt, wenn das ausgeliefert ist._

## Nicht-Ziele

- _Was das bewusst nicht tut._

## Anforderungen

| ID | Anforderung | Priorität |
|----|-------------|-----------|
| R1 | _Anforderung_ | Muss |
| R2 | _Anforderung_ | Soll |

## Ablauf

```mermaid
flowchart LR
  A[Start] --> B[Schritt] --> C[Ergebnis]
```

## Akzeptanzkriterien

- [ ] R1: _Wie wir es prüfen._
- [ ] R2: _Wie wir es prüfen._

## Offene Fragen

- _Frage._
""",
            "flowchart": """# Name des Ablaufs

_Ein Satz: was hineingeht, was herauskommt._

## Diagramm

```mermaid
flowchart LR
  A[Erster Schritt] --> B[Zweiter Schritt]
  B --> C[Dritter Schritt]
  C --> D[Fertig]
```

## Schritte

1. **Erster Schritt:** _wer ihn erledigt und was er weitergibt._
2. **Zweiter Schritt:** _…_
3. **Dritter Schritt:** _…_
4. **Fertig:** _was „fertig“ hier bedeutet._
""",
            "meeting-notes": """# Name der Besprechung, Datum

Teilnehmende: _Namen_

## Entscheidungen

- _Was entschieden wurde, je eine Zeile._

## Aufgaben

- [ ] Name: _was, bis wann._
- [ ] Name: _was, bis wann._

## Notizen

- _Alles, was sich zu behalten lohnt und weder Entscheidung noch Aufgabe ist._
""",
        },
        'scene_text': {
            "spec": {"title": "Spezifikation: Login-Codes", "req": "Anforderungen", "flow": "Ablauf", "acc": "Akzeptanz",
                     "r1": "R1: Sechsstelligen Code mailen.", "r2": "R2: Der Code gilt 10 Min.",
                     "r3": "R3: Zweiten Faktor abfragen.", "n1": "E-Mail", "n2": "Code", "n3": "Zweiter Faktor",
                     "n4": "Angemeldet", "a1": "R1: Code kommt binnen 1 Min.", "a3": "R3: Einmal pro Gerät.",
                     "ask": "Ich habe R3 gestrichen. Gleiche Ablauf und Akzeptanzkriterien an.",
                     "reply": "Erledigt. Der Ablauf überspringt den zweiten Faktor, und die Prüfung für R3 ist weg.",
                     "alt": "Ein Terminal öffnet spec.md in MarsDawn. Die lesende Person löscht die Anforderung R3, und der Agent entfernt ihren Schritt aus dem Ablaufdiagramm und ihre Akzeptanzprüfung."},
            "flowchart": {"title": "Veröffentlichungsablauf", "diagram": "Diagramm", "steps": "Schritte",
                          "n1": "Entwurf", "n2": "Lektorat", "n3": "Recht", "n4": "Veröffentlichen",
                          "s1": "1. Entwurf: der erste Wurf.", "s2": "2. Lektorat: jemand liest gegen.",
                          "s3": "3. Recht: prüft die Aussagen.", "s4": "{c}. Veröffentlichen: geht live.",
                          "ask": "Ich habe Recht aus dem Diagramm genommen. Korrigiere die Kante und die Schritte.",
                          "reply": "Erledigt. Lektorat führt direkt zu Veröffentlichen, und die Schritte sind neu nummeriert.",
                          "alt": "Ein Terminal öffnet flowchart.md in MarsDawn. Die lesende Person entfernt den Schritt Recht aus dem Mermaid-Diagramm, und der Agent verbindet das Diagramm neu und nummeriert die Schritte darunter neu."},
            "meeting-notes": {"title": "Wochenmeeting, 5. Okt.", "decisions": "Entscheidungen", "actions": "Aufgaben",
                              "d1": "Beta für {u} Personen öffnen.", "d2": "Am Freitag ausliefern.",
                              "t1": "Mia: {a} Einladungen senden.", "t2": "Leo: {b} Plätze hinzufügen.", "t3": "Ana: Support für {c} Personen.",
                              "ask": "Die Beta hat jetzt 80 Personen. Passe die Aufgaben an.",
                              "reply": "Erledigt. Alle drei Aufgaben sagen jetzt 80.",
                              "alt": "Ein Terminal öffnet meeting-notes.md in MarsDawn. Die lesende Person ändert eine Entscheidung von 50 auf 80 Personen, und der Agent passt die drei Aufgaben an."},
        },
    }
    # The homepage loop (scripts/loop_anim.py COPY). Tab names follow the app's de strings; the two
    # days have the same width (tabular digits), as the stacked swap needs.
    loop_copy = {
        "outline": "Gliederung", "files": "Dateien",
        "title": "Launch-Notiz",
        "sections": [("Was sich ändert", "Die Anmeldeseite beginnt mit der E-Mail. Sie kommt am {a}."),
                     ("Wann es live geht", "{u}, mittags."),
                     ("Wer was macht", "Engineering schaltet das Flag am {b} ein.")],
        "old": "7. Okt.", "new": "9. Okt.",
        "ask": "Ich habe den Launch verschoben. Gleiche die anderen Abschnitte an.",
        "reply": "Erledigt. Beide Abschnitte sagen jetzt 9. Okt.",
        "alt": "Ein Terminal öffnet launch-note.md in MarsDawn. Die lesende Person verschiebt den Launch "
               "vom 7. auf den 9. Oktober, der Agent passt die beiden anderen Abschnitte an, und "
               "die Schleife beginnt von vorn.",
        "pause": "Animation anhalten", "pause_short": "Pause",
    }

    app_ui_languages = 'Englisch, traditionelles Chinesisch, vereinfachtes Chinesisch, Japanisch, Deutsch, Französisch, Spanisch und Koreanisch'
    ui = {'home': 'MarsDawn', 'privacy': 'Datenschutzrichtlinie', 'support': 'Support', 'cli': 'Befehlszeile', 'agents': 'marsdawn für Agenten', 'using_cli': 'Die CLI verwenden', 'markdown-to-pdf': 'Markdown zu PDF', 'skill': 'Agent-Skill', 'view-markdown-on-mac': 'Markdown auf dem Mac ansehen', 'vs-macmd-viewer': 'MacMD Viewer vs. MarsDawn', 'updated': f'Zuletzt aktualisiert am {k.UPDATED}', 'tagline': 'Lies, was dein Agent geschrieben hat.', 'slogan': 'Ein neuer Morgen für Markdown.', 'footer_store': f'MarsDawn gibt es im <a href="{k.LISTING_URL}">Mac App Store</a>.', 'footer_nav': 'Website', 'more': 'Mehr', 'yours': 'Deine Texte bleiben auf deinem Mac', 'pay-once': 'Kostenlos testen, einmal bezahlen', 'pdf': 'PDF-Export', 'native': 'Eine Mac-App', 'limits': 'Was MarsDawn nicht kann', 'mcp': 'MCP-Server', 'token-efficient-review': 'Review mit wenigen Tokens', 'vs-markdown-preview-tools': 'Markdown anderswo ansehen vs. MarsDawn', 'themes': 'Vorschau-Themen und PDF-Export', 'themes-new': 'Ein Thema erstellen', 'themes-gallery': 'Themen-Galerie', 'sharing-exported-pdfs': 'Exportierte PDFs teilen', 'reviewing-ai-output': 'Warum KI-Ergebnisse weiterhin einen menschlichen Leser brauchen', 'reading-agent-output': 'Lesen, was dein Agent zurückgibt', 'agent-transparency': 'Transparenz von Agenten', 'reviewing-agent-plans': 'Den Plan eines Agenten prüfen', 'agent-design-patterns': 'Entwurfsmuster für Agenten', 'changelog': 'Änderungsprotokoll', 'reading-notes': 'Lektürenotizen der Redaktion', 'reading-notes-anthropic': 'Lektürenotizen: Anthropic', 'reading-notes-chip-huyen': 'Lektürenotizen: Chip Huyen', 'reading-notes-lilian-weng': 'Lektürenotizen: Lilian Weng', 'reading-notes-harrison-chase': 'Lektürenotizen: Harrison Chase', 'reading-notes-langchain': 'Lektürenotizen: LangChain (Jess Ou)', 'reading-notes-andrew-ng': 'Lektürenotizen: Andrew Ng', 'consent_text': 'Diese Website verwendet Analyse-Cookies, um zu sehen, wie Besucher sie nutzen. Sie bleiben aus, solange du nicht zustimmst.', 'consent_accept': 'Akzeptieren', 'consent_decline': 'Ablehnen', 'consent_aria': 'Cookie-Einwilligung', 'cookie_settings': 'Cookie-Einstellungen', 'view_markdown_source': 'Markdown-Quelltext ansehen'}
    store_chip = 'Im Mac App Store'
    trait_link = {'yours': ('Deine Texte bleiben auf deinem Mac', 'Kein Konto, keine Synchronisierung, keine Cloud.'), 'pay-once': ('Kostenlos testen, einmal bezahlen', '14 Tage kostenlos, danach einmalig 4,99 USD. Kein Abo.'), 'pdf': ('PDF-Export', 'Diagramme, hervorgehobener Code, saubere Seitenumbrüche.'), 'native': ('Eine Mac-App', 'Native Fenster und Tabs, automatisches Sichern, Übersicht.'), 'limits': ('Was MarsDawn nicht kann', 'Gut zu wissen, bevor du kaufst.')}
    trait_nav_heading = 'Was du von MarsDawn erwarten kannst'
    figure_list_label = 'Auf diesem Bildschirmfoto'


    pages['reading-notes'] = {
        "title": "Lektürenotizen der Redaktion · MarsDawn",
        "description": "Sechs kurze Notizen dazu, was die Leute, die KI-Agenten bauen, tatsächlich argumentieren — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain und Andrew Ng — und was das jeweils für die Person bedeutet, die lesen muss, was so ein Agent zurückgibt.",
        "body": f"""
<section class="intro">
  <h1>Lektürenotizen der Redaktion</h1>
  <p>Sechs Personen haben darüber geschrieben, wie KI-Agenten funktionieren: woraus sie gebaut sind, was ein System „agentic“ macht, welche Entwurfsmuster in der Praxis halten und welche noch nicht. Keine hat darüber geschrieben, wie man liest, was ein Agent zurückgibt, und keine erwähnt MarsDawn oder empfiehlt ein Markdown-Werkzeug. Wir haben jeden Text für sich gelesen, klar markiert, wo unsere eigene Lesart beginnt, und an jede Quelle dieselbe Frage gestellt: Welches Dokument landet wegen dieses Texts typischerweise in deinem Ordner, und wo hilft MarsDawn beim Lesen?</p>
</section>

<p>Wenn du zuerst die kurze, praktische Fassung willst, fang mit <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a> und <a href="/de/reviewing-agent-plans/">Den Plan eines Agenten in fünf Minuten prüfen</a> an. Diese sechs Notizen gehen näher an die Quellen hinter diesen Seiten. Jede steht für sich; lies sie in beliebiger Reihenfolge.</p>

<ul>
  <li><a href="/de/reading-notes/anthropic-building-effective-agents/">Anthropic zieht eine Linie zwischen Workflows und Agenten. Wo liegt dein Lesen?</a> &#8212; Anthropics Leitfaden für Leute, die Agenten bauen, trennt eine feste Pipeline von einem Modell, das den nächsten Schritt selbst steuert, und beschreibt einen Workflow, in dem der „Reviewer“ ein zweiter LLM-Aufruf ist, keine Person.</li>
  <li><a href="/de/reading-notes/chip-huyen-agents/">Chip Huyens Aufteilung in read-only- und write-Aktionen, und warum sie zählt, bevor du etwas freigibst</a> &#8212; ihre schlichte Definition eines Agenten und die Unterscheidung zwischen Aktionen, die nur schauen, und solchen, die etwas ändern: genau dort lohnt sich eine Fünf-Minuten-Prüfung.</li>
  <li><a href="/de/reading-notes/lilian-weng-llm-agents/">Lilian Wengs Agenten-Bauplan von 2023 und die Datei, die jeder Teil hinterlässt</a> &#8212; Gehirn, Planung, Gedächtnis, Werkzeugnutzung: ihr eigenes Gerüst dafür, woraus ein Agent besteht, und die Grenze, die sie bei Plänen nennt, die sich bei Fehlern nicht anpassen.</li>
  <li><a href="/de/reading-notes/harrison-chase-what-is-an-agent/">Harrison Chases Spektrum: je agentischer, desto mehr willst du zusehen</a> &#8212; seine technische Definition eines Agenten und sein Plädoyer für Beobachtbarkeit, je weiter ein System auf diesem Spektrum wandert.</li>
  <li><a href="/de/reading-notes/langchain-what-is-an-agent/">Jess Ous Eval-Pipeline und der eine Schritt, der noch bei dir liegt</a> &#8212; im Juli 2026 veröffentlichte LangChain unter der Adresse von Harrison Chases Beitrag von 2024 einen neuen Text „What is an AI agent?“ von Jess Ou; ihre Definition ist fast wörtlich die seine, und sie beschreibt, wo automatische Bewertung endet und eine Person eingreifen muss.</li>
  <li><a href="/de/reading-notes/andrew-ng-design-patterns/">Andrew Ng ordnet seine eigenen Entwurfsmuster nach Vorhersagbarkeit</a> &#8212; über fünf Briefe in The Batch sagt er klar, welche er für verlässlicher hält und welche er schwer vorhersagen kann.</li>
</ul>

<p>Keiner dieser sechs Texte argumentiert, man solle die Ausgabe eines Agenten sorgfältiger lesen, und keiner handelt von MarsDawn. Die Verbindung, wo wir sie ziehen, ist unsere, und jede Notiz sagt das.</p>
""",
    }


    pages['reading-notes/anthropic-building-effective-agents'] = {
        "title": 'Anthropic zieht eine Linie zwischen Workflows und Agenten. Wo liegt dein Lesen? · MarsDawn',
        "description": 'Anthropics Leitfaden vom Dezember 2024 für Leute, die Agenten bauen, trennt Workflows von Agenten und beschreibt fünf Workflow-Muster, darunter eines, bei dem ein zweiter LLM-Aufruf den ersten prüft. Was das für Dateien in deinem Ordner bedeutet.',
        "body": f"""
<section class="intro">
  <h1>Anthropic zieht eine Linie zwischen Workflows und Agenten. Wo liegt dein Lesen?</h1>
</section>

<div class="summary"><p><strong>Anthropics Leitfaden vom Dezember 2024 für Leute, die KI-Agenten bauen, beginnt damit, zwei Dinge zu trennen, die er „Workflows“ und „Agenten“ nennt, empfiehlt dann, mit dem Einfachsten zu starten, das funktioniert &#8212; möglicherweise gar keinem agentischen System &#8212; und greift erst zu einem seiner fünf Workflow-Muster, wenn das nicht reicht. Eines dieser Muster setzt einen zweiten LLM-Aufruf auf den Platz des Reviewers. Diese Notiz handelt von diesem Muster und davon, was die anderen vier dir zum Lesen hinterlassen.</strong></p></div>

<h2>Was der Leitfaden argumentiert</h2>
<p>Erik S. und Barry Zhang schrieben „Building Effective Agents“ für Ingenieure, die entscheiden, wie sie mit LLMs bauen. Es beginnt mit einer Definition:</p>
<blockquote><p>&#8220;Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.&#8221;</p></blockquote>
<p>Dann setzt der Rat bei Zurückhaltung an:</p>
<blockquote><p>&#8220;When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.&#8221;</p></blockquote>
<p>Wenn mehr Struktur nötig ist, beschreiben sie fünf Workflow-Muster: Prompt Chaining (eine Aufgabe als Folge von Aufrufen, mit optionalen Checks dazwischen), Routing, Parallelisierung, Orchestrator-Workers (ein LLM zerlegt eine Aufgabe, übergibt sie an Worker-LLMs und fügt die Ergebnisse zusammen) und Evaluator-Optimizer. Letzteres:</p>
<blockquote><p>&#8220;In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.&#8221;</p></blockquote>
<p>Anthropic erwähnt MarsDawn in diesem Leitfaden nirgends und empfiehlt kein Markdown-Werkzeug. <code>/agent-transparency/</code> behandelt das Transparenzprinzip dieses Leitfadens und seine „Checkpoints“-Sprache schon ausführlich &#8212; diese Notiz wiederholt das nicht. Dort steht auch die Stelle des Leitfadens zur menschlichen Code-Review, im richtigen Kontext (ein Anhang speziell zu Coding-Agenten).</p>

<h2>Unsere Lesart, nicht die von Anthropic</h2>
<p>Anthropic sagt nicht, wer die Endausgabe eines Workflows prüft, sobald er fertig ist, und nichts davon beschreibt überhaupt ein Dokument &#8212; es ist eine Architekturentscheidung für Leute, die das System bauen. Aber die fünf Muster erzeugen nicht dieselbe Art von Datei zum Lesen. Prompt Chaining und Routing sind meist unsichtbare Verdrahtung; wenn dich etwas erreicht, ist es der letzte Output der Kette, wie jede andere Einzelantwort. Orchestrator-Workers ist anders: nutzt dein Coding-Agent dieses Muster intern, kann in deinem Ordner ein Dokument landen, das aus mehreren Worker-Aufrufen zusammengenäht wurde, und ein Fehler in einem Worker-Stück ist in einer Zusammenfassung, die sich von Anfang bis Ende flüssig liest, leicht zu übersehen.</p>
<p>Evaluator-Optimizer ist der Grund zum Innehalten, weil der Leitfaden einen zweiten LLM-Aufruf dorthin setzt, wo sonst ein menschlicher Reviewer sitzen könnte. Das ist ein legitimer Weg, eine Klasse von Fehlern günstig zu fangen, aber es bleibt ein Modell, das ein Modell an den gegebenen Kriterien prüft &#8212; derselbe Vorbehalt, den andere Autoren hier zu einem Modell äußern, das die Arbeit von sich selbst oder einem anderen Modell beurteilt. Nichts im Leitfaden sagt, eine Person solle das Urteil des Evaluators noch einmal prüfen; dazu nimmt er gar keine Stellung. Wenn du liest, was davon zurückkommt, sind „die Schleife hat es freigegeben“ und „ich habe es geprüft“ nicht derselbe Satz, auch wenn die Datei vor dir in beiden Fällen identisch aussieht.</p>

<h2>Wo MarsDawn hilft und wo nicht</h2>
<p>MarsDawn weiß nicht, welches Workflow-Muster eine Datei erzeugt hat, und hat kein KI-Modell innen &#8212; es führt keinen eigenen Evaluator-Schritt aus und sagt dir nicht, ob der von Anthropic beschriebene seine Arbeit getan hat. Was es tut: Der Tab Gliederung in der Seitenleiste (Darstellung &#9656; Seitenleiste einblenden, &#8963;&#8984;S) listet die Überschriften einer langen, vom Orchestrator zusammengefügten Datei, und ein Klick springt dorthin. Quelltext und gerenderte Seite stehen nebeneinander (&#8984;2) und scrollen zusammen, mit gezeichneten Mermaid-Diagrammen und KaTeX-Formeln statt Rohquelle. Überarbeitet der Agent die Datei während du liest, lädt MarsDawn sie neu und behält deine Stelle, solange du keine eigenen ungesicherten Änderungen hast. Bearbeiten &#9656; Verweis kopieren (&#8997;&#8984;C) kopiert deine Stelle als <code>docs/plan.md:42</code>, bereit zum Einfügen in den Chat mit dem Agenten.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn ist im Mac App Store erhältlich. Das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code> funktioniert schon heute:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Es exportiert Markdown ohne die App als PDF.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Der Rest des Transparenzprinzips und der Checkpoints-Sprache dieses Leitfadens: <a href="/de/agent-transparency/">Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?</a></li>
  <li>Warum Agentenausgaben im Allgemeinen schwer zu lesen sind: <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a></li>
  <li>Zurück zur Reihe: <a href="/de/reading-notes/">Lektürenotizen der Redaktion</a></li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Erik S. and Barry Zhang, &#8220;Building Effective Agents,&#8221; Anthropic, December 19, 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (abgerufen und zitiert am 2026-09-26).</li>
</ul>
""",
    }


    pages['reading-notes/chip-huyen-agents'] = {
        "title": 'Chip Huyens Aufteilung in read-only- und write-Aktionen, und warum sie zählt, bevor du etwas freigibst · MarsDawn',
        "description": 'Chip Huyens Essay „Agents“ vom Januar 2025 teilt Aktionen von Agenten in read-only und write. Warum diese Aufteilung ein schneller Weg ist, in einem Plan die Zeile zu finden, die vor der Freigabe einen genaueren Blick verdient.',
        "body": f"""
<section class="intro">
  <h1>Chip Huyens Aufteilung in read-only- und write-Aktionen, und warum sie zählt, bevor du etwas freigibst</h1>
</section>

<div class="summary"><p><strong>Chip Huyens Essay „Agents“ vom Januar 2025 beginnt bei der Lehrbuchdefinition und gelangt zu etwas Spezifischerem: Die Aktionen eines Agenten teilen sich in solche, die die Welt nur anschauen, und solche, die sie verändern. Diese Aufteilung ist ein guter Weg, in den fünf Minuten, die du hast, zu entscheiden, welche Zeilen eines Plans vor dem Ja einen genaueren Blick verdienen.</strong></p></div>

<h2>Was der Text argumentiert</h2>
<p>Huyen öffnet schlicht:</p>
<blockquote><p>&#8220;An agent is anything that can perceive its environment and act upon that environment.&#8221;</p></blockquote>
<p>Von dort baut sie aus, was ein Agent braucht: eine Umgebung zum Handeln und einen Satz Werkzeuge &#8212; sein „tool inventory“ &#8212;, der bestimmt, was er tun kann. Sie benennt die Unterscheidung zwischen Aktionen, die einen Agenten nur wahrnehmen lassen („read-only actions“), und Aktionen, die ihn auf die Umgebung einwirken lassen („write actions“). Zum Risiko der zweiten Art ist sie klar: „Write actions enable a system to do more“, aber „the prospect of giving AI the ability to automatically alter our lives is frightening“ &#8212; in ihren Worten: „you shouldn’t allow an unreliable AI to initiate bank transfers.“ Ebenso offen zur schwersten Stelle eines Agenten:</p>
<blockquote><p>&#8220;If you’ve ever been in any planning meeting, you know that planning is hard.&#8221;</p></blockquote>
<p>Huyen erwähnt MarsDawn in diesem Essay nirgends und empfiehlt kein Markdown-Werkzeug. <code>/reviewing-agent-plans/</code> zitiert schon drei ihrer Sätze aus demselben Essay: die Kosten fehlender Aufsicht vor dem Lauf eines Plans, den Agenten, der glaubt fertig zu sein, obwohl er es nicht ist, und in Schritt 3 der Checkliste ihre Zeile, dass ein System vor einer riskanten Operation „can ask for explicit human approval before executing“. Diese Notiz wiederholt diese Zitate nicht; wenn du die Seite noch nicht gelesen hast, ist sie unten verlinkt.</p>

<h2>Unsere Lesart, nicht die von Huyen</h2>
<p>Huyens Aufteilung in read-only und write ist nicht als Review-Rat geschrieben &#8212; sie klassifiziert, was ein Werkzeug tut. Aber sie ist ein schlichter, allgemeiner Test für genau die Art riskanter Zeile, bei der Schritt 3 jener Checkliste dich schon bittet, langsamer zu werden: eine Datei lesen, eine Suche starten, ein Verzeichnis listen sind read-only, und ein schiefgehender read-only-Schritt kostet dich einen neuen Lauf; Daten löschen, Force-Push, einen Branch mergen, eine E-Mail senden, eine Karte belasten sind write actions, und &#8212; wie sie sagt &#8212; ein schiefgehender write-Schritt ist die beängstigende Art, und wenn du den Bericht des Agenten liest, kann er schon geschehen sein. Ihr Punkt, dass Planung selbst für Menschen im Raum schwer ist, ist ein nützlicher Check dagegen, von einem Plan mehr Präzision zu erwarten, als das Format tragen kann: ein selbstsicher lesender Plan ist nicht dasselbe wie ein richtiger Plan.</p>

<h2>Wo MarsDawn hilft und wo nicht</h2>
<p>MarsDawn kann in einem Plan keinen read-only- von einem write-Schritt unterscheiden &#8212; das ist ein Urteil, das der Text nicht etikettiert, und nichts in der App liest auf Bedeutung. Es hat kein KI-Modell innen: es markiert die riskante Zeile nicht für dich, führt den „Planung-ist-schwer“-Check nicht aus und bewertet den Plan nicht. Was es tut: die Datei lesbar halten, während du dieses Urteil selbst fällst. Der Tab Gliederung (Darstellung &#9656; Seitenleiste einblenden, &#8963;&#8984;S) lässt dich die Form eines Plans scannen, bevor du Zeile für Zeile liest; Quelltext und gerenderte Seite stehen nebeneinander (&#8984;2), damit ein Diagramm der Schritte nicht als rohes Mermaid stecken bleibt; und Bearbeiten &#9656; Verweis kopieren (&#8997;&#8984;C) macht aus deiner Stelle <code>plan.md:10</code>, bereit als Feedback, sobald du eine write action in der falschen Reihenfolge siehst.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn ist im Mac App Store erhältlich. Das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code> funktioniert schon heute:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Es exportiert Markdown ohne die App als PDF.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Die vollständige Sechs-Schritte-Checkliste in fünf Minuten aus demselben Essay: <a href="/de/reviewing-agent-plans/">Den Plan eines Agenten in fünf Minuten prüfen</a></li>
  <li>Warum Agentenausgaben im Allgemeinen schwer zu lesen sind: <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a></li>
  <li>Zurück zur Reihe: <a href="/de/reading-notes/">Lektürenotizen der Redaktion</a></li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Chip Huyen, &#8220;Agents,&#8221; January 7, 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a> (abgerufen und zitiert am 2026-09-26).</li>
</ul>
""",
    }


    pages['reading-notes/lilian-weng-llm-agents'] = {
        "title": 'Lilian Wengs Agenten-Bauplan von 2023 und die Datei, die jeder Teil hinterlässt · MarsDawn',
        "description": 'Lilian Wengs viel zitierte Umfrage von 2023 beschreibt einen LLM-Agenten als Gehirn plus Planung, Gedächtnis und Werkzeugnutzung. Was jeder Teil dir typischerweise zum Lesen hinterlässt, und die Grenze, die sie bei Plänen nennt, die sich Überraschungen nicht anpassen.',
        "body": f"""
<section class="intro">
  <h1>Lilian Wengs Agenten-Bauplan von 2023 und die Datei, die jeder Teil hinterlässt</h1>
</section>

<div class="summary"><p><strong>Im Juni 2023, damals bei OpenAI, veröffentlichte Lilian Weng auf ihrem Blog Lil’Log eine lange Umfrage: ein LLM-gestützter Agent als Gehirn (das Modell) plus drei Komponenten &#8212; Planung, Gedächtnis und Werkzeugnutzung. Es ist ein früh und breit zitiertes Gerüst dafür, woraus ein Agent besteht, und offen dazu, wo dieses Gerüst noch bricht.</strong></p></div>

<h2>Was der Beitrag argumentiert</h2>
<p>Wengs Überblick setzt den Rahmen für den ganzen Text:</p>
<blockquote><p>&#8220;In a LLM-powered autonomous agent system, LLM functions as the agent&#8217;s brain, complemented by several key components: Planning ... Memory ... Tool use&#8221;.</p></blockquote>
<p>Planung umfasst bei ihr sowohl das Zerlegen einer Aufgabe in Teilziele als auch das Reflektieren über vergangene Aktionen, um künftige zu verbessern. Gedächtnis teilt sich in kurzfristig (Kontext, den das Modell gerade sieht &#8212; in-context) und langfristig (meist außerhalb des Modells, in einem durchsuchbaren Vector Store). Werkzeugnutzung lässt das Modell alles holen, was ein eingefrorener Gewichtssatz allein nicht liefern kann &#8212; aktuelle Informationen, Codeausführung, andere APIs. Gegen Ende, unter „Challenges“, benennt sie eine Grenze klar:</p>
<blockquote><p>&#8220;LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.&#8221;</p></blockquote>
<p>An anderer Stelle, in einer Fallstudie zum Chemie-Agenten ChemCrow, markiert sie ein engeres Problem: eine LLM-basierte Bewertung setzte ihn etwa gleich mit GPT-4, während menschliche Experten ChemCrow bei der Korrektheit weit besser fanden. Ihre Schlussfolgerung betrifft die Selbstbewertung, nicht speziell ihre „reflection“-Komponente:</p>
<blockquote><p>&#8220;The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.&#8221;</p></blockquote>
<p>Weng erwähnt MarsDawn in diesem Beitrag nirgends und empfiehlt kein Markdown-Werkzeug.</p>

<h2>Unsere Lesart, nicht die von Weng</h2>
<p>Weng beschreibt Agentenarchitektur 2023, nicht das Lesen von Agentenausgaben &#8212; sie erwähnt gar keine Person, die eine Datei prüft. Aber ihre drei Komponenten lassen sich auf drei verschiedene Dinge abbilden, die du zu lesen bekommst. Planung hinterlässt dir typischerweise ein Dokument vor dem Lauf &#8212; den Plan selbst, manchmal mit schon eingefalteter „reflection“ oder Selbstprüfung. Gedächtnis ist meist unsichtbar, es sei denn, der Agent führt eine laufende Scratch-Datei als Langzeitspeicher; dann lohnt es sich, sie für sich zu öffnen, weil sie eine alte, falsche Annahme über viele spätere Schritte tragen kann, ohne es zu sagen. Werkzeugnutzung hinterlässt eher einen Bericht darüber, was lief und was zurückkam &#8212; näher an einem Transkript als an einem Plan.</p>
<p>Ihr Punkt, dass Pläne sich unerwarteten Fehlern nicht anpassen, ist von deiner Seite gelesen ein Grund, warum ein gestern freigegebener Plan heute veraltet sein kann: ist zwischenzeitlich etwas passiert, das der Plan nicht vorsah, kann der Agent trotzdem weiterlaufen statt neu zu planen, und der Schlussbericht beschreibt den Erfolg des Originalplans, ohne den Umweg. Das ist unsere Folgerung, kein Anspruch von ihr &#8212; sie schreibt über die Robustheit des Modells, nicht darüber, worauf eine lesende Person achten soll.</p>

<h2>Wo MarsDawn hilft und wo nicht</h2>
<p>MarsDawn hat kein KI-Modell innen, kann also nicht sagen, ob ein Plan still vom Tatsächlichen abgewichen ist, und unterscheidet auch keine Planungs-, Gedächtnis- oder Werkzeugnutzungs-Datei &#8212; das ist eine Lesart des Inhalts, und die liegt bei dir. Was es tut: Der Tab Gliederung (Darstellung &#9656; Seitenleiste einblenden, &#8963;&#8984;S) zeigt die Form eines langen Plans auf einen Blick, Quelltext und gerenderte Vorschau stehen nebeneinander (&#8984;2) mit gezeichnetem Mermaid und KaTeX, und wenn der Agent die Datei mitten im Lesen umschreibt, lädt MarsDawn sie neu und behält deine Stelle, solange du keine eigenen ungesicherten Änderungen hast &#8212; nützlich gerade deshalb, weil ein still überarbeiteter Plan genau der Fehlermodus ist, den ihr Abschnitt „Challenges“ von der Modellseite beschreibt.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn ist im Mac App Store erhältlich. Das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code> funktioniert schon heute:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Es exportiert Markdown ohne die App als PDF.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Welche Dokumente verschiedene Agenten-Entwurfsmuster dir typischerweise übergeben: <a href="/de/agent-design-patterns/">Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt</a></li>
  <li>Die Fünf-Minuten-Prüfung eines Plans vor dem Lauf: <a href="/de/reviewing-agent-plans/">Den Plan eines Agenten in fünf Minuten prüfen</a></li>
  <li>Zurück zur Reihe: <a href="/de/reading-notes/">Lektürenotizen der Redaktion</a></li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Lilian Weng, &#8220;LLM Powered Autonomous Agents,&#8221; Lil’Log, June 23, 2023: <a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a> (abgerufen und zitiert am 2026-09-26; sie war damals bei OpenAI, hier nur so beschrieben, wie sie damals war).</li>
</ul>
""",
    }


    pages['reading-notes/harrison-chase-what-is-an-agent'] = {
        "title": 'Harrison Chases Spektrum: je agentischer, desto mehr willst du zusehen · MarsDawn',
        "description": 'Harrison Chases Definition eines Agenten von 2024 und sein Spektrum agentischen Verhaltens, und sein Plädoyer für Beobachtbarkeit, je weiter ein System darauf wandert — gelesen von der Seite der Person, die die Datei liest, die er zurückgibt.',
        "body": f"""
<section class="intro">
  <h1>Harrison Chases Spektrum: je agentischer, desto mehr willst du zusehen</h1>
</section>

<div class="summary"><p><strong>Im Juni 2024 eröffnete LangChains Harrison Chase eine neue Reihe mit einer täuschend kleinen Frage &#8212; „What is an agent?“ &#8212; und antwortete mit einer technischen Definition und einem Spektrum „agentischen“ Verhaltens. Je mehr davon ein System einnimmt, argumentiert er, desto mehr musst du hineinsehen können, während es läuft.</strong></p></div>

<h2>Was der Beitrag argumentiert</h2>
<p>Chases eigene Definition, mit dem Vorbehalt, dass sie technischer und breiter ist als die meisten Vorstellungen von einem Agenten:</p>
<blockquote><p>&#8220;An agent is a system that uses an LLM to decide the control flow of an application.&#8221;</p></blockquote>
<p>Control flow heißt nur, welcher Schritt als Nächstes läuft. Er räumt sofort ein, die Definition sei unperfekt &#8212; ein einfaches System, in dem ein LLM zwischen zwei Pfaden routet, zählt nach seiner Definition als Agent, trifft aber die Intuition der meisten Leute von „Agent“ nicht. Statt um das Label zu streiten, greift er einen Vorschlag von Andrew Ng auf, dessen Tweet er direkt zitiert und zuschreibt: „rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic.“ Chases eigener Kommentar: „I really agree with this viewpoint and I think Andrew expressed it nicely.“ Von dort: Ein System ist umso „agentischer“, je mehr ein LLM entscheidet, wie es sich verhält &#8212; von einem festen Router über eine Zustandsmaschine bis zu einem voll autonomen Agenten, der eigene Werkzeuge baut und erinnert. Sein praktisches Argument folgt aus diesem Spektrum &#8212; je agentischer ein System, desto wichtiger bestimmte Infrastruktur, vor allem Beobachtbarkeit:</p>
<blockquote><p>&#8220;You&#8217;ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.&#8221;</p></blockquote>
<p>Er dehnt das auf Eingreifen aus, nicht nur Zuschauen: Du willst auch den Zustand oder die Anweisungen eines laufenden Agenten an einem Punkt ändern können, um ihn zurück auf Kurs zu schubsen, wenn er abdriftet. Chase erwähnt MarsDawn in diesem Beitrag nirgends und empfiehlt kein Markdown-Werkzeug.</p>

<h2>Unsere Lesart, nicht die von Chase</h2>
<p>Chase schreibt über Werkzeuge für Leute, die Agenten-Frameworks bauen &#8212; LangGraph und LangSmith namentlich &#8212; nicht über eine Person, die ein fertiges Dokument liest. Aber sein Spektrum gibt eine nützliche Art, vor dem Lesen einzuschätzen, was vor dir liegt: Je agentischer das System, das eine Datei erzeugt hat, desto weniger solltest du die Schritte allein aus dem Prompt vorhersagen können, und desto eher lohnt es sich, die Datei als Aufzeichnung dessen zu lesen, was wirklich geschah, nicht dessen, was geschehen sollte.
Sein „observe what is going on inside“ gilt den Innereien eines laufenden Systems &#8212; Traces (ein aufgezeichnetes Log von allem, was der Agent in einem Lauf tat), Zwischenschritte, Werkzeugaufrufe &#8212; nicht dem Lesen eines Markdown-Plans hinterher. Aber der Grund, den er nennt &#8212; dass die genauen Schritte im Voraus nicht bekannt sein können &#8212; gilt genauso für das Dokument, das ein Agent dir am Ende übergibt: Waren die Schritte vorher nicht vorhersagbar, ist der Bericht hinterher der einzige Ort, sie zu prüfen.</p>

<h2>Wo MarsDawn hilft und wo nicht</h2>
<p>MarsDawn beobachtet die Innereien eines laufenden Agenten nicht &#8212; es hat kein KI-Modell innen und keine Verbindung zum Framework, das die Datei erzeugt hat, und kann dir nicht sagen, wo auf Chases Spektrum ein gegebener Agent saß. Es arbeitet an dem Dokument, das danach landet: der Tab Gliederung (Darstellung &#9656; Seitenleiste einblenden, &#8963;&#8984;S) für die Form eines langen Berichts, Quelltext und gerenderte Vorschau nebeneinander (&#8984;2) für Diagramme und Formeln, und Live-Neuladen, das deine Stelle behält, wenn der Agent die Datei umschreibt, solange du keine eigenen ungesicherten Änderungen hast &#8212; die Dateiebene davon, etwas zu beobachten, das sich noch bewegt. Bearbeiten &#9656; Verweis kopieren (&#8997;&#8984;C) und Für KI kopieren (&#8963;&#8997;&#8984;C) lassen dich genau zeigen, wo ein Schritt vom Kurs abkam &#8212; das Dokument-Äquivalent dazu, einen laufenden Agenten zurückzustoßen.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn ist im Mac App Store erhältlich. Das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code> funktioniert schon heute:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Es exportiert Markdown ohne die App als PDF.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Die ausführlichere Behandlung von Transparenz und Checkpoints in dieser Reihe: <a href="/de/agent-transparency/">Anthropic sagt, Agenten sollen transparent sein. Wer liest, was sie offenlegen?</a></li>
  <li>LangChains Beitrag von 2026 unter derselben Adresse, mit einer fast identischen Definition: <a href="/de/reading-notes/langchain-what-is-an-agent/">Jess Ous Eval-Pipeline und der eine Schritt, der noch bei dir liegt</a></li>
  <li>Zurück zur Reihe: <a href="/de/reading-notes/">Lektürenotizen der Redaktion</a></li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Harrison Chase, &#8220;What is an agent?,&#8221; LangChain, June 28, 2024, Archivkopie: <a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a> (abgerufen und zitiert am 2026-09-26 über die Wayback Machine; die Originaladresse zeigt jetzt einen Beitrag von Jess Ou aus 2026).</li>
</ul>
""",
    }


    pages['reading-notes/langchain-what-is-an-agent'] = {
        "title": 'Jess Ous Eval-Pipeline und der eine Schritt, der noch bei dir liegt · MarsDawn',
        "description": 'LangChains „What is an AI agent?“ von Jess Ou (2026) greift Harrison Chases Definition von 2024 auf und beschreibt eine Pipeline zur automatischen Bewertung von Agenten. Wo diese Pipeline noch einen Schritt an eine Person übergibt — und wo nicht.',
        "body": f"""
<section class="intro">
  <h1>Jess Ous Eval-Pipeline und der eine Schritt, der noch bei dir liegt</h1>
</section>

<div class="summary"><p><strong>Im Juli 2026 veröffentlichte LangChain unter der Adresse von Harrison Chases Beitrag „What is an agent?“ von 2024 einen neuen Text „What is an AI agent?“ von Jess Ou, mit einer Definition, die fast wörtlich die seine ist. Der Großteil ihres Beitrags gilt etwas, das seiner nicht abdeckte: einer ganzen Pipeline zur automatischen Bewertung von Agenten. Ihr Text ist offen dazu, wo diese Pipeline noch eine Person braucht — und wo nicht.</strong></p></div>

<h2>Was der Beitrag argumentiert</h2>
<p>Ous Definition greift Chases eng auf:</p>
<blockquote><p>&#8220;An AI agent is a system that uses a large language model to decide the control flow of an application.&#8221;</p></blockquote>
<p>Control flow heißt wieder nur, welcher Schritt als Nächstes läuft. Von dort beschreibt sie LangChains Agent Development Lifecycle &#8212; build, test, deploy, monitor &#8212; und einen geschichteten Ansatz, die Arbeit eines Agenten zu prüfen, ohne dass eine Person jeden Lauf liest: Online-Evals sampeln Produktions-Traces (aufgezeichnete Logs echter Läufe) auf Regressionen, Offline-Evals laufen gegen kuratierte Datensätze, um eine schlechte Änderung vor dem Ship zu fangen, und „LLM-as-a-judge“ bewertet die Ausgabe eines Laufs an von einer Person vorab definierten Kriterien, in einem Maßstab, den manuelle Prüfung nicht erreicht. Wo in dieser Pipeline noch eine Person hingehört, sagt sie klar:</p>
<blockquote><p>&#8220;For sensitive or irreversible actions, we recommend human-in-the-loop controls that pause the agent for approval, edits, rejection, or clarification.&#8221;</p></blockquote>
<p>Sie hat auch eine Zeile zum Urteil, das sich nicht wegskalieren lässt, egal wie gut die Pipeline wird: „Do not outsource judgment you cannot evaluate. If you wouldn’t recognize a correct answer, neither will the agent.“ <code>/reviewing-agent-plans/</code> baut schon auf genau diesem Satz auf &#8212; diese Notiz wiederholt diese Diskussion nicht. Ou erwähnt MarsDawn nirgends und empfiehlt kein Markdown-Werkzeug. Chase nennt sie auch nie; was die beiden Beiträge verbindet, ist, dass LangChain den ihren 2026 unter der Adresse veröffentlichte, die sein Beitrag von 2024 einnahm, mit einer nahezu identischen Definition &#8212; eine Beobachtung von uns, nicht von ihr.</p>

<h2>Unsere Lesart, nicht die von Ou</h2>
<p>Ous Human-in-the-loop-Zeile gilt dem Gate bestimmter Aktionen vor dem Lauf &#8212; eine write action zur Freigabe anhalten, dieselbe Idee, auf die Chip Huyens Aufteilung in read-only und write aus einem anderen Winkel zeigt &#8212; nicht dem Lesen eines fertigen Berichts hinterher. Genau gelesen ist der Großteil ihrer Pipeline dafür gebaut, eine Person aus der Routineprüfung herauszunehmen, nicht hinein: Online- und Offline-Evals und LLM-as-a-judge existieren gerade deshalb, damit ein Team nicht jeden Trace manuell lesen muss.
Das ist keine Kritik am Text &#8212; es ist ihr erklärtes Ziel, und in Produktionsmaßstab vernünftig. Aber es bedeutet: Die Prüfung, die du von Hand tust &#8212; einen Plan oder Bericht lesen, den ein Agent dir direkt übergibt &#8212; ist genau die Art Check, die ihre Pipeline reduzieren, nicht ersetzen soll. Ihre eigene Urteils-Zeile setzt dieser Reduktion einen Boden: Wo du selbst richtige von falscher Antwort nicht unterscheiden kannst, musst du trotzdem selbst lesen.</p>

<h2>Wo MarsDawn hilft und wo nicht</h2>
<p>MarsDawn ist keine Eval-Pipeline und hat kein KI-Modell innen &#8212; es bewertet keinen Trace, führt keinen LLM-as-a-judge-Durchlauf aus und entscheidet nicht, welche Aktionen sensibel genug zum Anhalten sind. Es ist für den Moment gebaut, den ihre Pipeline noch einer Person übergibt: die Sache direkt lesen. Der Tab Gliederung (Darstellung &#9656; Seitenleiste einblenden, &#8963;&#8984;S) listet die Überschriften eines langen Berichts, Quelltext und gerenderte Vorschau stehen nebeneinander (&#8984;2) mit gezeichnetem Mermaid und KaTeX, und Bearbeiten &#9656; Verweis kopieren (&#8997;&#8984;C) mit Für KI kopieren (&#8963;&#8997;&#8984;C) machen aus einem Spot-Check präzises Feedback, mit dem der Agent arbeiten kann.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn ist im Mac App Store erhältlich. Das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code> funktioniert schon heute:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Es exportiert Markdown ohne die App als PDF.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Die vollständige Checkliste, die zum Teil aus ihrer „outsource judgment“-Zeile gebaut ist: <a href="/de/reviewing-agent-plans/">Den Plan eines Agenten in fünf Minuten prüfen</a></li>
  <li>Wo dieselbe Definition 2024 anfing: <a href="/de/reading-notes/harrison-chase-what-is-an-agent/">Harrison Chases Spektrum: je agentischer, desto mehr willst du zusehen</a></li>
  <li>Zurück zur Reihe: <a href="/de/reading-notes/">Lektürenotizen der Redaktion</a></li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Jess Ou, &#8220;What is an AI agent?,&#8221; LangChain, July 31, 2026: <a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a> (abgerufen und zitiert am 2026-09-26).</li>
</ul>
""",
    }


    pages['reading-notes/andrew-ng-design-patterns'] = {
        "title": 'Andrew Ng ordnet seine eigenen Entwurfsmuster nach Vorhersagbarkeit · MarsDawn',
        "description": 'Über fünf Briefe in The Batch ordnet Andrew Ng Reflexion, Werkzeugnutzung, Planung und Multi-Agenten-Zusammenarbeit danach, wie verlässlich und vorhersagbar er jedes findet — und was diese Rangfolge dazu nahelegt, wie genau man die Ausgabe jedes Musters prüfen sollte.',
        "body": f"""
<section class="intro">
  <h1>Andrew Ng ordnet seine eigenen Entwurfsmuster nach Vorhersagbarkeit</h1>
</section>

<div class="summary"><p><strong>Über fünf Briefe in The Batch Anfang 2024 beschrieb Andrew Ng vier agentische Entwurfsmuster &#8212; Reflexion, Werkzeugnutzung, Planung und Multi-Agenten-Zusammenarbeit &#8212; und sagte seinen Lesern ungewöhnlich klar, welche er für verlässlicher hält und welche er schwer vorhersagen kann.</strong></p></div>

<h2>Was die Briefe argumentieren</h2>
<p><code>/agent-design-patterns/</code> behandelt schon, was jedes der vier Muster ist, welche Dokumente jedes typischerweise zum Lesen übergibt (unsere Folgerung), und Ngs eigenes Urteil zur Planung aus Teil 4: „while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do.“ Diese Notiz ergänzt dieselbe Rangfolge aus den zwei Briefen, die jene Seite auslässt: Teil 3, eine Woche vor Teil 4, wo er die Rangfolge im Voraus nennt, und Teil 5, wo er sie auf das Muster ausdehnt, das Teil 4 nicht nennt &#8212; Multi-Agenten-Zusammenarbeit. Zur Einführung von Werkzeugnutzung in Teil 3 schreibt er:</p>
<blockquote><p>&#8220;In future letters, I&#8217;ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable &#8212; albeit very exciting &#8212; technologies.&#8221;</p></blockquote>
<p>Zwei Wochen später, am Ende der Reihe mit Multi-Agenten-Zusammenarbeit, bestätigt er dieselbe Rangfolge von der anderen Seite:</p>
<blockquote><p>&#8220;Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.&#8221;</p></blockquote>
<p>Das sagt er darüber, wie gut jedes Muster die Ergebnisse seiner Anwendungen verbessert, nicht darüber, wie sorgfältig eine Person ihre Ausgabe prüfen sollte &#8212; nichts in dieser Reihe fordert menschliche Prüfung, und nichts erwähnt MarsDawn oder empfiehlt ein Markdown-Werkzeug.</p>

<h2>Unsere Lesart, nicht die von Ng</h2>
<p>Ngs Rangfolge gilt Ausgabequalität und Vorhersagbarkeit vom Stuhl des Bauenden aus, aber sie deckt sich grob damit, wie viel Prüfung die Papierspur jedes Musters von deinem Stuhl aus verdient. Reflexion und Werkzeugnutzung, die beiden, die er für verlässlicher hält, übergeben dir typischerweise etwas, das schon getane Arbeit beschreibt &#8212; einen überarbeiteten Entwurf, einen Bericht darüber, was lief &#8212; sodass das Prüfen einer Behauptung gegen die echte Ausgabe meist das Risiko abdeckt. Planung und Multi-Agenten-Zusammenarbeit, die beiden, die er schwer vorhersagen kann, übergeben dir typischerweise etwas, das vor der Arbeit geschrieben wurde, oder über mehrere Dateien mehrerer Agenten verteilt ist:
einen Plan, der auf ein Go wartet, oder eine Übergabe zwischen Agenten, die die Ausführung noch nicht getestet hat. Nach seiner eigenen Darstellung sind genau das die Dokumente, bei denen die Lücke zwischen Geschriebenem und dem, was wirklich passieren wird, am weitesten ist &#8212; derselbe Punkt, den <code>/reviewing-agent-plans/</code> aus Chip Huyens Essay im Abschnitt „Warum überhaupt vor dem Lauf“ zieht: Ein Problem zu fangen, bevor etwas gelaufen ist, ist der günstigste Ort, es zu fangen.</p>

<h2>Wo MarsDawn hilft und wo nicht</h2>
<p>MarsDawn weiß nicht, welches von Ngs vier Mustern eine gegebene Datei erzeugt hat, ordnet nichts nach Vorhersagbarkeit und hat kein KI-Modell innen &#8212; es führt die Prüfung nicht aus, die seine Rangfolge nahelegt. Es hält die Datei lesbar, während du das selbst tust: Der Tab Gliederung (Darstellung &#9656; Seitenleiste einblenden, &#8963;&#8984;S) zeigt die Form eines langen Plans, Quelltext und gerenderte Vorschau stehen nebeneinander (&#8984;2), und für eine Multi-Agenten-Übergabe zeigt das Öffnen des gemeinsamen Ordners mit Ablage &#9656; Ordner öffnen&#160;&#8230; (&#8679;&#8984;O) neue Dateien im Tab Dateien innerhalb etwa einer Sekunde, sobald verschiedene Agenten schreiben, und die Kopfzeile nennt den Git-Branch oder Worktree, damit zwei Dateien mit demselben Namen von verschiedenen Agenten nicht verwechselt werden.</p>

<h2>Ausprobieren</h2>
<p>MarsDawn ist im Mac App Store erhältlich. Das kostenlose Befehlszeilenwerkzeug <code>marsdawn</code> funktioniert schon heute:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>Es exportiert Markdown ohne die App als PDF.</p>
<p><a href="/de/cli/">Befehlszeile</a> &#183; Vor dem Kauf wissen: <a href="/de/limits/">Was MarsDawn nicht kann</a></p>

<h2>Weiter</h2>
<ul>
  <li>Was jedes Muster dir typischerweise übergibt, vollständig: <a href="/de/agent-design-patterns/">Vier Agenten-Entwurfsmuster und die Dokumente, die jedes dir übergibt</a></li>
  <li>Die Fünf-Minuten-Prüfung eines Plans vor dem Lauf: <a href="/de/reviewing-agent-plans/">Den Plan eines Agenten in fünf Minuten prüfen</a></li>
  <li>Zurück zur Reihe: <a href="/de/reading-notes/">Lektürenotizen der Redaktion</a></li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 1,&#8221; The Batch, March 20, 2024: <a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 3: Tool Use,&#8221; The Batch, April 3, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/</a> (abgerufen und zitiert am 2026-09-26).</li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 4: Planning,&#8221; The Batch, April 10, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a> (Zitat wörtlich aus <code>design/inbox/276-agent-blog-series.md</code>, bereits auf <code>/agent-design-patterns/</code> zitiert).</li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 5, Multi-Agent Collaboration,&#8221; The Batch, April 17, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/</a> (abgerufen und zitiert am 2026-09-26).</li>
</ul>
""",
    }

    pages['privacy'] = {
        "title": 'Datenschutzrichtlinie · MarsDawn',
        "description": 'MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.',
        "body": k.render_legal_body("privacy", "de"),
    }
    pages['support'] = {
        "title": 'Support · MarsDawn',
        "description": 'Hilfe zu MarsDawn, dem Markdown-Editor für macOS.',
        "body": k.render_legal_body("support", "de"),
    }
    tables = {
        'app_ui_languages': app_ui_languages,
        'home': home,
        'compare': {key: {'head': t['head'], 'rows': t['rows']} for key, t in compare_tables.items()},
        'exit_table_head': exit_table_head,
        'exit_remedy': exit_remedy,
        'theme_shots': {image: {'name': name, 'alt': alt} for image, (name, alt) in theme_shots.items()},
        'theme_gallery_note': theme_gallery_note,
        'skip_label': 'Zum Inhalt springen',
        'toc_label': {'privacy': 'Auf dieser Seite', 'support': 'Zu einer Frage springen'},
        'not_found': {'title': 'Seite nicht gefunden · MarsDawn', 'headline': 'Verloren zwischen den Sternen.', 'body': 'Dieser Weg ist auf keiner Karte verzeichnet. Ein stiller Nachbar hat den Heimweg gezeigt.', 'home': 'Zurück zu MarsDawn', 'alt': 'Ein kleines Raumschiff treibt durch den Morgenhimmel über dem Mars, während ein freundlicher Außerirdischer auf den hellen Rand des Planeten zeigt.'},
        # Not in Grok's material (the window label and the Markdown twin's sentence): written for #162.
        'hero_window_label': 'Ein bedienbares MarsDawn-Fenster: Wähle ein Thema und ein Layout',
        'hero_window_markdown': {'template': 'Die Seite zeigt ein bedienbares MarsDawn-Fenster mit einem Ausschnitt aus der Einführung der App. Im Palettenmenü wählst du ein Erscheinungsbild ({looks}) und für Hell und Dunkel je eines von vier Vorschau-Themen ({themes}), in der Symbolleiste eines von drei Layouts ({layouts}).', 'sep': ', '},
        'loop': loop_copy,
        'templates': templates,
    }
    return {
        'ui': ui, 'store_chip': store_chip, 'schema_notes': schema_notes, 'example_plan': example_plan,
        'trait_link': trait_link, 'trait_nav_heading': trait_nav_heading, 'figure_list_label': figure_list_label,
        'figures': figures, 'pages': pages, 'tables': tables,
    }
