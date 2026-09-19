"""Japanese (ja) copy for the MarsDawn site, translated from the en copy in build_pages.py.

build(k) returns the same tables build_pages.py keeps for en and zh-hant, for this one locale.
k carries the shared constants (EMAIL, KIT_URL, BREW_TAP_INSTALL, ...), so they are written once.
"""


def build(k) -> dict:
    ui = {'home': 'MarsDawn', 'privacy': 'Privacy Policy', 'support': 'Support', 'cli': 'Command Line', 'agents': 'marsdawn for agents', 'using_cli': 'Using the CLI', 'markdown-to-pdf': 'Markdown to PDF', 'skill': 'Agent skill', 'view-markdown-on-mac': 'View Markdown on a Mac', 'vs-macmd-viewer': 'MacMD Viewer vs. MarsDawn', 'updated': f"Last updated {k.UPDATED}", 'tagline': 'Read what your agent wrote.', 'footer_store': 'MarsDawn is coming soon to the Mac App Store.', 'more': 'More', 'yours': 'Your writing stays on your Mac', 'pay-once': 'Try free, pay once', 'pdf': 'PDF export', 'native': 'A Mac app', 'limits': "What MarsDawn doesn't do"}
    store_chip = 'Coming soon to the Mac App Store'
    schema_notes = {'export': 'export success', 'open': 'open success, marsdawn 0.3.0 and later', 'error': 'failure, both commands', 'open_v1': 'open success, marsdawn 0.2.x, where <code>opened</code> was a list of paths'}
    example_plan = '# Plan: faster exports\n\nAn agent wrote this plan. You review it, then turn it into a PDF.\n\n## Steps\n\n| Step | Owner | Status |\n|------|-------|--------|\n| Measure the slow pages | Agent | Done |\n| Cache rendered diagrams | Agent | In review |\n\nThe target is $t < 2\\,\\text{s}$ for a 50-page document:\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  Draft --> Review --> Ship\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'
    trait_link = {'yours': ('Your writing stays on your Mac', 'No account, no sync, no cloud.'), 'pay-once': ('Try free, pay once', 'Free for 14 days, then USD 4.99 once. No subscription.'), 'pdf': ('PDF export', 'Diagrams, highlighted code, careful page breaks.'), 'native': ('A Mac app', 'Native windows, tabs, autosave, Quick Look.'), 'limits': ("What MarsDawn doesn't do", 'Know before you buy.')}
    trait_nav_heading = 'What to expect from MarsDawn'
    figure_list_label = 'In this screenshot'
    figures = {
        'index': {
            "alt": 'MarsDawn in split view: the Markdown source on the left, the rendered page on the right.',
            "callouts": [],
        },
        'yours': {
            "alt": 'MarsDawn showing a document in the Classic theme, with the preview filling the window.',
            "callouts": ['A file on your Mac, saved where you choose.', 'The whole toolbar is themes and layouts; there is nothing to sign in to.'],
        },
        'pay-once': {
            "alt": 'MarsDawn in the Vivid theme, with Markdown source on the left and the rendered page on the right.',
            "callouts": ['Markdown highlighting in the editor, included.', 'Every theme and every layout is included.', 'Mermaid diagrams, included.', 'Code highlighting, included.'],
        },
        'pdf': {
            "alt": 'A PDF exported from MarsDawn, open in its PDF viewer with page thumbnails.',
            "callouts": ['Mermaid diagrams, drawn into the PDF.', 'Code keeps its highlighting.'],
        },
        'native': {
            "alt": 'MarsDawn in split view: the Markdown source on the left, the rendered page on the right.',
            "callouts": ['A native Mac window.', "The Mac's text editor, with Markdown highlighting.", '⌘1 source, ⌘2 split, ⌘3 preview.', 'The page updates as you type.'],
        },
        'limits': {
            "alt": 'MarsDawn in dark mode, with Markdown source on the left and the rendered page on the right.',
            "callouts": ['One document per window, on this Mac.', 'You write Markdown here.', 'The toolbar holds themes and layouts, and there is no plugins menu.', 'The page is for reading, not editing.'],
        },
    }
    pages = {}
    pages['index'] = {
        "title": 'MarsDawn: a Markdown editor for Mac, with live preview',
        "description": 'A native Mac Markdown editor with live preview, Mermaid diagrams and PDF export, built for reading what AI agents write. Coming soon to the Mac App Store.',
        "intro": f"""
<section class="intro hero">
  <p class="kicker">Built for the AI workflow</p>
  <h1>Where an agent's Markdown gets a careful read.</h1>
  <p>An AI agent writes the Markdown. You review it in MarsDawn, source and rendered page side by side, then send it back for changes.</p>
</section>
""",
        "body": f"""
<h2 class="loop-title">The loop</h2>
<ol class="loop-steps">
  <li><strong>The agent writes.</strong> Your coding agent or writing assistant drafts the Markdown: a README, a spec, a set of notes.</li>
  <li><strong>You review in MarsDawn.</strong> Open the file and read it rendered, with Mermaid diagrams and highlighted code, next to the source.</li>
  <li><strong>The agent revises.</strong> Ask for changes. Open the revised file and read it the same way.</li>
</ol>
<p>Agents can drive MarsDawn directly: the free <a href="/ja/cli/">marsdawn</a> command-line tool opens a file for review or exports a PDF, with JSON output built for scripts. See <a href="/ja/cli/agents/">marsdawn for agents</a> for the details.</p>
""",
    }
    pages['yours'] = {
        "title": 'A Mac Markdown editor with no account and no cloud · MarsDawn',
        "description": 'MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.',
        "intro": f"""
<section class="intro">
  <h1>Your writing stays on your Mac.</h1>
  <p>MarsDawn has no account, no sync and no cloud. It opens a file, you write, and it saves the file where you chose.</p>
</section>
""",
        "body": f"""
<h2>What that means</h2>
<ul>
  <li>There is no account to sign up for or sign in to.</li>
  <li>Nothing syncs to a cloud. Your documents stay where you save them.</li>
  <li>Nothing is tracked. MarsDawn does not collect any data about you, and its App Store privacy label is "Data Not Collected".</li>
  <li>Web images stay blocked until you choose to load them, so opening a document never tells a server you read it. When you do load them, they load over https only.</li>
  <li>Local images show in the preview once you grant access to their folder.</li>
</ul>
<p>The details are in the <a href="/ja/privacy/">privacy policy</a>.</p>
""",
    }
    pages['pay-once'] = {
        "title": 'Try it free, then pay once · MarsDawn',
        "description": 'MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 4.99. No subscription, no account.',
        "intro": f"""
<section class="intro">
  <h1>Try all of it. Then pay once.</h1>
  <p>MarsDawn is a free download. Start the 14-day trial and every feature works; to keep using it after that, one purchase of USD 4.99 unlocks it. There is no subscription and no account.</p>
</section>
""",
        "body": f"""
<h2>How it works</h2>
<ul>
  <li>MarsDawn is free to download from the Mac App Store.</li>
  <li>Start the trial and everything works for 14 days: every theme and layout, PDF export and printing, Quick Look, and the Siri and Shortcuts actions.</li>
  <li>To keep using it after that, unlock it once for USD 4.99. It's an in-app purchase, not a subscription, so nothing renews and nothing charges you later.</li>
  <li>The trial doesn't charge you either. When it ends, nothing is bought unless you choose to unlock.</li>
  <li>There is no account. MarsDawn never asks you to create one.</li>
</ul>
<h2>If you don't unlock</h2>
<ul>
  <li>After 14 days, until you unlock it, you can't read, edit, export or print documents in MarsDawn. A document still opens, but its content is covered.</li>
  <li>Your files don't change. They're ordinary files on your Mac, and Quick Look in Finder keeps showing them.</li>
  <li>The free <a href="/ja/cli/"><code>marsdawn</code> command-line tool</a> keeps exporting them to PDF, trial or not.</li>
  <li>If a document is open in MarsDawn when the trial ends, the text you typed isn't lost: use File ▸ Save As… to keep it.</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": 'Export Markdown to PDF on a Mac, diagrams included · MarsDawn',
        "description": 'Export Markdown as a PDF or print it on your Mac, with Mermaid diagrams and highlighted code. Page breaks avoid splitting short code blocks and tables.',
        "intro": f"""
<section class="intro">
  <h1>The PDF looks like the page you wrote.</h1>
  <p>Export as PDF or print, in your theme's light colors. Diagrams and highlighted code come through, and page breaks avoid splitting what belongs together.</p>
</section>
""",
        "body": f"""
<h2>What that means</h2>
<ul>
  <li>Mermaid diagrams are drawn into the PDF.</li>
  <li>Code blocks keep their syntax highlighting.</li>
  <li>Page breaks avoid leaving a heading at the bottom of a page or splitting code, tables and diagrams.</li>
  <li>Any layout. Export works even while only the source is showing.</li>
</ul>
<p>The free <a href="/ja/cli/">marsdawn command-line tool</a> uses the same exporter, so a script or an AI agent gets the same PDF.</p>
""",
    }
    pages['native'] = {
        "title": 'A native Markdown app for Mac: tabs, Quick Look · MarsDawn',
        "description": 'A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.',
        "intro": f"""
<section class="intro">
  <h1>Built out of the Mac's own parts.</h1>
  <p>The windows, tabs, menus and text editor are the Mac's own. The rendered page is drawn by WebKit, the engine behind Safari.</p>
</section>
""",
        "body": f"""
<h2>What that means</h2>
<ul>
  <li>Source, split and preview layouts, one keystroke apart (<kbd>⌘1</kbd>, <kbd>⌘2</kbd>, <kbd>⌘3</kbd>).</li>
  <li>The two panes scroll together, so the paragraph you are editing stays in view.</li>
  <li>Markdown syntax highlighting in the editor, matched to your preview theme.</li>
  <li>Native windows, tabs, autosave and version history.</li>
  <li>Quick Look: press Space on a Markdown file in Finder for a preview, diagrams included.</li>
  <li>Siri and Shortcuts: start a new document from a template, add a line to your notes inbox, or reopen a recent document.</li>
  <li>{k.APP_UI_LANGUAGES}.</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": "What MarsDawn doesn't do · MarsDawn",
        "description": 'No sync, no iPhone or iPad app, no plugins, no accounts. Four built-in themes. Know before you buy.',
        "intro": f"""
<section class="intro">
  <h1>What MarsDawn doesn't do.</h1>
  <p>Some things are left out on purpose. If you need one of them, it's better to know now than after you buy.</p>
</section>
""",
        "body": f"""
<h2>Left out</h2>
<ul>
  <li><strong>Sync:</strong> MarsDawn doesn't sync your documents. They stay where you save them, so to use one on another Mac, keep it in a folder you already sync.</li>
  <li><strong>iPhone and iPad:</strong> there is no app for them; MarsDawn is for the Mac.</li>
  <li><strong>Plugins:</strong> MarsDawn has no plugins or extensions.</li>
  <li><strong>Sharing:</strong> there are no accounts and no shared editing, because MarsDawn is for one person on their own Mac.</li>
  <li><strong>Editing:</strong> you write Markdown on the left and read the page on the right; the page itself can't be edited.</li>
  <li><strong>Formats:</strong> MarsDawn exports PDF and prints, and doesn't export Word files.</li>
  <li><strong>Themes:</strong> it comes with Dawn, Classic, Modern and Vivid, each in light and dark, and you can't install others.</li>
  <li><strong>Other files:</strong> plain text files and PDFs open read-only.</li>
  <li><strong>After the trial:</strong> if you don't unlock MarsDawn once the 14-day trial ends, you can't read or edit documents in it: they open with their content covered. Your files stay as they are, Quick Look still shows them, and the free command-line tool still exports them.</li>
  <li><strong>System:</strong> MarsDawn needs macOS 26 or later.</li>
</ul>
""",
    }
    pages['support'] = {
        "title": 'Support · MarsDawn',
        "description": 'Get help with MarsDawn, the Markdown editor for macOS.',
        "body": f"""
<section class="intro">
  <h1>Support</h1>
  <p>Help with MarsDawn, the Markdown editor for macOS.</p>
</section>

<section class="contact">
  <h2>Write to us</h2>
  <a class="email" href="mailto:{k.EMAIL}?subject=MarsDawn%20support">{k.EMAIL}</a>
  <p>Please include your macOS version and your MarsDawn version (MarsDawn › About MarsDawn). If something looks wrong, a screenshot or a small sample document helps a lot.</p>
</section>

<section class="faq">
  <h2>Common questions</h2>

  <h3>What do I need to run MarsDawn?</h3>
  <p>A Mac with macOS 26 Tahoe or later, on Apple silicon or Intel.</p>

  <h3>How do I switch between the editor and the preview?</h3>
  <p>Press <kbd>⌘1</kbd> for the source only, <kbd>⌘2</kbd> for side by side, and <kbd>⌘3</kbd> for the preview only. The same choices are in the View menu and the toolbar.</p>

  <h3>An image in my document doesn't show.</h3>
  <ul>
    <li><strong>Image on your Mac:</strong> save the document first, then click <em>Grant Folder Access…</em> in the preview and choose the folder that holds the image. MarsDawn remembers the folder. You can review granted folders in MarsDawn › Settings › Folder Access.</li>
    <li><strong>Image from the web:</strong> web images are blocked until you click <em>Load Images</em> at the top of the preview. To always load them, turn on <em>Load remote images automatically</em> in Settings.</li>
  </ul>

  <h3>How do I add an image?</h3>
  <p>Drag it into the editor, or paste it. The document must be saved first: MarsDawn copies the image into an <code>assets</code> folder next to the document and writes the Markdown link for you.</p>

  <h3>A Mermaid diagram shows an error.</h3>
  <p>MarsDawn shows the diagram's source with the first line of Mermaid's error message underneath. Check the line it names, for example for an arrow with nothing after it or a bracket that isn't closed.</p>

  <h3>How do I make a PDF?</h3>
  <p>Choose File › Export as PDF… (<kbd>⌥⌘E</kbd>). The PDF uses the light version of your preview theme and is split into pages, whichever layout you are in. File › Print… prints the same pages.</p>

  <h3>How do I use MarsDawn with Siri or Shortcuts?</h3>
  <p>Open the Shortcuts app and search for MarsDawn to find <em>New Markdown Document</em>, <em>Add Note to Inbox</em> and <em>Open Recent Document</em>. Before adding notes, choose a notes folder in MarsDawn › Settings › Notes Folder. Notes are added to <code>Inbox.md</code> in that folder.</p>

  <h3>Where are my settings?</h3>
  <p>MarsDawn › Settings (<kbd>⌘,</kbd>) has appearance, images, the notes folder, folder access and the preview theme.</p>

  <h3>How do I get a refund?</h3>
  <p>Purchases are handled by Apple. Request a refund at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
</section>
""",
    }
    pages['privacy'] = {
        "title": 'Privacy Policy · MarsDawn',
        "description": 'MarsDawn does not collect personal data. Your documents and settings stay on your Mac.',
        "body": f"""
<section class="intro">
  <h1>Privacy Policy</h1>
  <p>How MarsDawn, the Markdown editor for macOS, handles your information.</p>
  <p class="updated">Last updated {k.PRIVACY_UPDATED}</p>
</section>

<div class="summary"><p><strong>MarsDawn does not collect any data about you.</strong> There is no account, no analytics, no advertising and no tracking. Your documents and settings stay on your Mac.</p></div>

<h2>What stays on your Mac</h2>
<ul>
  <li><strong>Your documents.</strong> MarsDawn reads and writes only the files and folders you open, save or choose. They are never uploaded anywhere by the app.</li>
  <li><strong>Your settings.</strong> Appearance, preview theme, window layout and the image preference are stored in the app's own preferences on your Mac.</li>
  <li><strong>Folder access you grant.</strong> When you let MarsDawn show images or page files from a folder, or choose a notes folder, the app keeps a macOS bookmark so it can open that folder again. A folder you open in the sidebar stays readable and writable by MarsDawn until you remove it in Settings, not just while its window is open. You can remove folders at any time in MarsDawn › Settings.</li>
</ul>

<h2>When MarsDawn uses the internet</h2>
<p>MarsDawn works fully offline. It connects to the internet only <strong>when you choose to</strong>, for a document that refers to the web:</p>
<ul>
  <li><strong>Markdown documents.</strong> Web images are blocked by default. They load only after you click <em>Load Images</em> in the preview, or if you turn on <em>Load remote images automatically</em> in Settings. Nothing else a Markdown document refers to is loaded from the web.</li>
  <li><strong>HTML documents.</strong> An HTML document opens static: its code doesn't run and nothing is loaded from the web. If a document contains code that could run, you can choose <em>View › Run This Document</em> for that document. Its own code then runs until you stop it, the document reloads or you close the window. That choice is never remembered, and it isn't a setting. While it runs, the document can send data over the network, and read images, style sheets, fonts and media in its folder and the folders inside it. Code downloaded from the web never runs.</li>
</ul>
<p>MarsDawn loads web content over https only. A plain http address is never loaded, in any setting, and MarsDawn does not rewrite it to https. In a Markdown document, the preview shows a placeholder in its place.</p>
<p>When web content loads, your Mac requests it directly from the servers that host it. Like any web request, this lets those servers see your IP address and what was requested. MarsDawn's developer receives none of this information.</p>
<p>Links you click in the preview open in your default web browser, under that browser's own privacy practices. Audio and video never play by themselves.</p>

<h2>Siri, Shortcuts and Spotlight</h2>
<p>MarsDawn offers actions for Siri, the Shortcuts app and Spotlight, such as creating a document or adding a note. When you use them, the text you provide is passed to MarsDawn on your Mac and saved only where the action says (a new document, or the <code>Inbox.md</code> file in the notes folder you chose). Speech you dictate to Siri is handled by Apple under <a href="https://www.apple.com/legal/privacy/">Apple's Privacy Policy</a>.</p>

<h2>Exporting and printing</h2>
<p>PDF export and printing happen on your Mac. The PDF is saved where you choose. Printing goes through macOS to the printer you pick.</p>

<h2>The marsdawn command-line tool</h2>
<p>The optional <code>marsdawn</code> command-line tool, distributed separately, also runs entirely on your Mac. It reads the Markdown file you name and writes the PDF you ask for. It loads web images only when you pass <code>--allow-remote-images</code>.</p>

<h2>Children</h2>
<p>MarsDawn does not collect data from anyone, including children.</p>

<h2>Purchases</h2>
<p>MarsDawn will be sold through the Mac App Store. Apple will process the purchase under its own terms, and the developer never receives your payment details.</p>

<h2>Changes to this policy</h2>
<p>If MarsDawn ever starts handling data differently, this page will be updated before that version is released, and the date at the top will change.</p>

<h2>Contact</h2>
<p>Questions about privacy: <a href="mailto:{k.EMAIL}">{k.EMAIL}</a></p>
""",
    }
    pages['view-markdown-on-mac'] = {
        "title": 'How to view a Markdown file on a Mac · MarsDawn',
        "description": 'A .md file is plain text with formatting marks in it. Here is how to read it rendered on a Mac: as a PDF with the free marsdawn command-line tool today, and in the MarsDawn app, coming soon to the Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>How to view a Markdown file on a Mac.</h1>
  <p>A <code>.md</code> file is plain text. The headings, bold words, tables and diagrams are written as marks: <code>#</code> for a heading, <code>**</code> around bold, pipes for a table, a <code>mermaid</code> code block for a diagram. Open it in a plain text editor and you read the marks. To read the page the way its author meant, something has to render it.</p>
</section>
<h2>Today, for free: turn it into a PDF</h2>
<p>The free <code>marsdawn</code> command-line tool renders a Markdown file to a PDF, which any Mac can open. Tables, math, Mermaid diagrams and highlighted code come out rendered, and it needs nothing else installed, not even the MarsDawn app.</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code> writes <code>notes.pdf</code> next to the Markdown file, and <code>open</code> shows it in your PDF viewer. It needs macOS 15 or later. The walk-through, with a real exported page, is on <a href="/ja/markdown-to-pdf/">Markdown to PDF</a>.</p>
<h2>Coming soon: read it in MarsDawn</h2>
<p>MarsDawn is a Markdown editor for the Mac, coming soon to the Mac App Store. Open a <code>.md</code> file and read the rendered page next to the source:</p>
<ul>
  <li>The preview updates as you type, and the two panes scroll together.</li>
  <li>Mermaid flowcharts and sequence diagrams are drawn in the preview, and code blocks are highlighted.</li>
  <li>In Finder, press Space on a Markdown file for a Quick Look preview, diagrams included.</li>
  <li>When you want to change something, the source is right there. MarsDawn is an editor, not only a viewer.</li>
</ul>
<p>If an AI agent wrote the file, this is the loop MarsDawn is built for: the agent writes, you read it rendered, and it revises. See <a href="/ja/">the home page</a>, and <a href="/ja/cli/agents/">marsdawn for agents</a> for letting an agent open files for you.</p>
<h2>Next</h2>
<ul>
  <li>Every option of the command-line tool: <a href="/ja/cli/">Command Line</a>.</li>
  <li>What MarsDawn doesn't do: <a href="/ja/limits/">the list</a>.</li>
</ul>
""",
    }
    pages['markdown-to-pdf'] = {
        "title": 'Markdown to PDF on a Mac, from the command line · MarsDawn',
        "description": 'Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.',
        "body": f"""
<section class="intro">
  <h1>Markdown to PDF on a Mac, from the command line.</h1>
  <p>The free <code>marsdawn</code> tool turns a Markdown file into a PDF with one command. Tables, math, Mermaid diagrams and highlighted code come out the way they read in the source, and it needs nothing else installed, not even the MarsDawn app.</p>
</section>
<h2>Install it</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>On an Apple silicon Mac, Homebrew installs a prebuilt copy in seconds. On an Intel Mac it builds from source instead, which takes a few minutes and needs Xcode 26 or later. It runs on macOS 15 or later, and <code>marsdawn --version</code> prints the version you got.</p>
<h2>Save a document</h2>
<p>Paste this into a file named <code>plan.md</code>:</p>
<pre><code>{k.xml_escape(example_plan)}</code></pre>
<h2>Export it</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>It writes <code>plan.pdf</code> next to the source and prints where it went:</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>This is that page, captured from a real run of <code>marsdawn</code> 0.5.0:</p>
<p><img class="pdf-page" src="/assets/cli/plan-ja.png" alt="The exported PDF: the heading, a table of steps, an inline and a displayed formula, a Draft, Review, Ship diagram, and a highlighted line of Swift." width="989" height="930"></p>
<h2>Choose a theme, paper size and file name</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code>: dawn, classic, modern or vivid, in the theme's light colors. Without it, <code>export</code> uses <code>$MARSDAWN_THEME</code>, then dawn.</li>
  <li><code>--paper</code>: a4 or letter. The default is a4.</li>
  <li><code>-o</code>: where to write the PDF, instead of next to the source.</li>
  <li><code>--allow-remote-images</code>: load images from the web while rendering. They stay off unless you pass it.</li>
</ul>
<h2>If it doesn't work</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> Homebrew is building <code>marsdawn</code> from source, as it does on an Intel Mac. Install Xcode 26 or later from the App Store, then run the install again.</li>
  <li><code>marsdawn: No such file: …</code> The path doesn't point at a file. Check the name, or run the command from the folder the file is in.</li>
  <li><code>… already exists. Pass --force to replace it.</code> A PDF with that name is already there. Add <code>--force</code> to replace it, or <code>-o</code> to write it somewhere else.</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> The theme or paper size isn't one it knows. The themes are dawn, classic, modern and vivid; the paper is a4 or letter.</li>
</ul>
<h2>Next</h2>
<ul>
  <li>Every option and the JSON it prints: <a href="/ja/cli/">Command Line</a>.</li>
  <li>To have a coding agent do this for you: <a href="/ja/cli/skill/">the marsdawn agent skill</a>.</li>
</ul>
""",
    }
    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer vs. MarsDawn: a viewer or an editor · MarsDawn',
        "description": 'MacMD Viewer renders Markdown read-only for USD 19.99. MarsDawn edits and previews side by side, free to try then USD 4.99 once on the Mac App Store.',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer vs. MarsDawn.</h1>
  <p>Both are Mac apps for reading Markdown rendered. MacMD Viewer opens a <code>.md</code> file and shows the finished page; it doesn't edit it. MarsDawn puts an editor next to the same kind of rendered preview, so you write and review in one window. Here's how they differ, feature by feature.</p>
</section>
<h2>If you only need to read, not edit</h2>
<p>If your job is strictly reading Markdown someone else wrote, and you never need to touch the source, MacMD Viewer is a reasonable fit: it's built for exactly that, is available now and works down to an older macOS. MarsDawn is worth it once reading isn't the whole job, because an agent's Markdown usually comes back for another pass.</p>
<h2>What each app does</h2>
<ul>
  <li><strong>Editing:</strong> MacMD Viewer is read-only by design. MarsDawn edits the source and renders it side by side, so a change shows up as you type.</li>
  <li><strong>Preview themes:</strong> MacMD Viewer ships 12 document themes. MarsDawn ships four, Dawn, Classic, Modern and Vivid, each with a light and a dark palette.</li>
  <li><strong>Diagrams and math:</strong> both render Mermaid diagrams and highlight code. MarsDawn also renders KaTeX math; MacMD Viewer's own listing doesn't mention math rendering.</li>
  <li><strong>Finder integration:</strong> both add a Quick Look extension, so pressing Space on a <code>.md</code> file in Finder shows the rendered page.</li>
  <li><strong>PDF and print:</strong> both export or print a PDF of the rendered page.</li>
  <li><strong>System requirements:</strong> MacMD Viewer needs macOS 14 (Sonoma) or later. MarsDawn needs macOS 26 (Tahoe) or later.</li>
  <li><strong>Languages:</strong> MarsDawn's interface ships in {k.APP_UI_LANGUAGES}. MacMD Viewer's own materials don't state a UI language, so this page doesn't compare that.</li>
</ul>
<h2>Pricing and how you buy it</h2>
<ul>
  <li><strong>Where you buy it:</strong> MacMD Viewer is a direct download from its own site, also on Homebrew and Setapp; it isn't on the Mac App Store. MarsDawn is Mac App Store only.</li>
  <li><strong>Price:</strong> MacMD Viewer is USD 19.99 once for one Mac (a 3-Mac pack and volume packs cost more). MarsDawn is a free download, then a USD 4.99 one-time unlock.</li>
  <li><strong>Trying it first:</strong> MacMD Viewer has no free trial; direct purchases carry a 14-day money-back guarantee instead. MarsDawn gives you a 14-day trial before you pay anything.</li>
  <li><strong>Refunds and updates:</strong> MacMD Viewer's refunds and updates run through its own site. MarsDawn's purchase goes through Apple, so refunds and updates use Apple's standard process.</li>
  <li><strong>Accounts:</strong> neither app needs an account to use.</li>
</ul>
<h2>Try it today, free</h2>
<p>MarsDawn is coming soon to the Mac App Store, not on sale yet. Until then, the free <code>marsdawn</code> command-line tool renders any Markdown file to a PDF today, with Mermaid diagrams and highlighted code, and needs nothing else installed:</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>Next</h2>
<ul>
  <li>The full walk-through: <a href="/ja/markdown-to-pdf/">Markdown to PDF</a>.</li>
  <li>What MarsDawn doesn't do: <a href="/ja/limits/">the list</a>.</li>
  <li>Every option of the command-line tool: <a href="/ja/cli/">Command Line</a>.</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn: a free Markdown to PDF command-line tool · MarsDawn',
        "description": 'The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.',
        "body": f"""
<section class="intro">
  <h1>Command Line</h1>
  <p>The free <code>marsdawn</code> command-line tool: export Markdown to PDF from a shell or an LLM agent, and, with the MarsDawn app installed, open files in it.</p>
</section>

<div class="summary"><p><strong>marsdawn is free and distributed separately from the Mac App Store.</strong> Install it with Homebrew: on an Apple silicon Mac it arrives ready to run. <code>export</code> works on its own; <code>open</code> needs the MarsDawn app.</p></div>

<p>Calling marsdawn from an AI agent or a script? See <a href="/ja/cli/agents/">marsdawn for agents</a> for the JSON output, its schemas and every exit code.</p>

<h2>Install</h2>
<p>With <a href="https://brew.sh">Homebrew</a>:</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>On an Apple silicon Mac, Homebrew installs a prebuilt copy in seconds, with nothing else to install. On an Intel Mac it builds marsdawn from source instead, which takes a few minutes and needs Xcode 26 or later (Swift 6.2). The tool runs on macOS 15 or later.</p>
<p>Or build it from <a href="{k.KIT_URL}">the source</a> with Swift Package Manager:</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>Check which version you have with <code>marsdawn --version</code>.</p>

<h2>Commands</h2>

<h3>marsdawn open</h3>
<p>Opens one or more Markdown files in the MarsDawn app for review. It needs the app installed: without it, <code>marsdawn open</code> exits with code 3 and says MarsDawn isn't installed. <code>export</code> doesn't need the app.</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120</code></pre>
<ul>
  <li><code>path:line</code>: asks MarsDawn to land on that line. A column after it, as in <code>notes.md:120:8</code>, is ignored. If a file with the whole name exists, the argument is that file.</li>
  <li><code>--line &lt;n&gt;</code>: the same for a single file, and the way to ask for a line on a path that itself ends in a colon and digits. Needs exactly one file.</li>
  <li>Lines run from 1 to 999999999.</li>
  <li>MarsDawn 1.0 opens the file but doesn't jump to the line yet.</li>
  <li><code>--json</code>: print a JSON result instead of text.</li>
</ul>
<p>Lines were added in marsdawn 0.3.0.</p>

<h3>marsdawn export</h3>
<p>Renders a Markdown file to a paginated PDF, with the same exporter MarsDawn's own PDF export uses. It doesn't need the MarsDawn app. Relative images resolve against the input file's folder.</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: where to write the PDF. Defaults to the input path with a <code>.pdf</code> extension.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: the preview theme's light palette. Defaults to <code>$MARSDAWN_THEME</code>, then <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: paper size. Defaults to <code>a4</code>.</li>
  <li><code>--allow-remote-images</code>: load images from the web while rendering. Off by default.</li>
  <li><code>--force</code>: replace the output file if it already exists.</li>
  <li><code>--json</code>: print a JSON result instead of text.</li>
</ul>

<h2>The $MARSDAWN_THEME variable</h2>
<p>When <code>--theme</code> isn't passed, <code>export</code> reads the <code>$MARSDAWN_THEME</code> environment variable. Its value must be one of <code>dawn</code>, <code>classic</code>, <code>modern</code> or <code>vivid</code>; anything else falls back to <code>dawn</code>. The CLI doesn't read the app's own theme setting, because reading another app's container can trigger a macOS privacy prompt.</p>

<h2>Overwriting files</h2>
<p><code>export</code> refuses to replace an existing output file unless you pass <code>--force</code>.</p>

<h2>Exit codes</h2>
<ul>
  <li><code>0</code>: success.</li>
  <li><code>2</code>: input not found.</li>
  <li><code>3</code>: MarsDawn is not installed (<code>open</code> only).</li>
  <li><code>4</code>: output exists (pass <code>--force</code>).</li>
  <li><code>5</code>: export failed.</li>
  <li><code>64</code>: usage error, including a line out of range or <code>--line</code> with more than one file.</li>
</ul>

<h2>--json output</h2>
<p>On success, <code>marsdawn open --json</code> prints <code>ok</code>, <code>opened</code> (a list with each file's <code>path</code>, plus <code>line</code> when one was asked for) and <code>app</code> (the app path). <code>marsdawn export --json</code> prints <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code> and <code>diagramErrors</code>. On failure, both print <code>ok</code>, <code>error</code> and <code>message</code>.</p>
""",
    }
    pages['cli/agents'] = {
        "title": 'marsdawn for agents: Markdown to PDF from scripts · MarsDawn',
        "description": 'A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.',
        "body": f"""
<section class="intro">
  <h1>marsdawn for agents</h1>
  <p>A reference for AI agents and scripts that call the <code>marsdawn</code> command-line tool. Every example on this page was run against the tool built from the current source.</p>
</section>

<div class="summary"><p><strong>To turn a Markdown file into a PDF, run <code>marsdawn export notes.md --json</code> and read one JSON object from stdout.</strong> Mermaid diagrams and highlighted code are rendered the same way as in the MarsDawn app. <code>export</code> doesn't need the app; <code>open</code> does.</p></div>

<h2>What it does</h2>
<ul>
  <li><code>export</code> renders one Markdown file to a paginated PDF with the same exporter as the MarsDawn app. No window opens.</li>
  <li><code>open</code> opens one or more Markdown files in the MarsDawn app, so a person can review them, and can name the line each file should land on.</li>
</ul>

<h2>What it does not do</h2>
<ul>
  <li>It doesn't read Markdown from stdin. Pass a file path.</li>
  <li>It doesn't write the PDF to stdout. The PDF always goes to a file; stdout carries only the result.</li>
  <li>It doesn't replace an existing file unless you pass <code>--force</code>.</li>
  <li>It doesn't load images from the web unless you pass <code>--allow-remote-images</code>, and then only over https.</li>
  <li><code>open</code> doesn't work without the MarsDawn app installed; it exits with code 3. <code>export</code> doesn't need the app.</li>
  <li>MarsDawn 1.0 doesn't jump to the line <code>open</code> names yet. It opens the file at the top.</li>
  <li>It runs on macOS only.</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p>Writes <code>notes.pdf</code> next to <code>notes.md</code>. Options:</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: where to write the PDF. Defaults to the input path with a <code>.pdf</code> extension.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: the theme's light palette. Defaults to <code>$MARSDAWN_THEME</code>, then <code>dawn</code>.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: paper size. Defaults to <code>a4</code>.</li>
  <li><code>--allow-remote-images</code>: load https images from the web while rendering.</li>
  <li><code>--force</code>: replace the output file if it exists.</li>
  <li><code>--json</code>: print one JSON object on stdout instead of text.</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>Success, exit code 0:</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code>: absolute path of the PDF that was written.</li>
  <li><code>pages</code>: number of pages.</li>
  <li><code>theme</code> and <code>paper</code>: the values used.</li>
  <li><code>diagramErrors</code>: one message per Mermaid diagram that failed to render. The PDF is still written.</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json</code></pre>
<ul>
  <li><code>path:line</code> names the line to land on. A column after it, as in <code>notes.md:120:8</code>, is ignored. An argument that names a file which exists is always that whole filename, so a file called <code>weird:12</code> opens as itself.</li>
  <li><code>--line &lt;n&gt;</code> names the line for a single file, including a path that itself ends in a colon and digits. It needs exactly one file.</li>
  <li>Lines run from 1 to 999999999. Anything else is a usage error.</li>
  <li>Lines were added in marsdawn 0.3.0. MarsDawn 1.0 opens the file but doesn't jump to the line yet.</li>
</ul>
<p>Success, exit code 0:</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>: one object per file, in the order given. <code>path</code> is the file's absolute path; <code>line</code> appears only when a line was asked for.</li>
  <li><code>app</code>: path of the MarsDawn app that opened them.</li>
</ul>
<p>marsdawn 0.2.x printed <code>opened</code> as a list of path strings. Check <code>marsdawn --version</code> if you need to handle both.</p>

<h2>Failures</h2>
<p>With <code>--json</code>, a failure prints one JSON object on stdout and exits with its code:</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>, <code>input_not_found</code>: the input doesn't exist, is a folder, or isn't UTF-8 text.</li>
  <li><code>3</code>, <code>app_not_installed</code>: MarsDawn isn't installed. Only <code>open</code> returns this.</li>
  <li><code>4</code>, <code>output_exists</code>: the output file exists. Pass <code>--force</code>.</li>
  <li><code>5</code>, <code>export_failed</code>: the export itself failed.</li>
  <li><code>64</code>: usage error, such as an unknown option, an invalid value, a line out of range or <code>--line</code> with more than one file. This one is printed as text on stderr, even with <code>--json</code>.</li>
</ul>

<h2>JSON Schemas</h2>
<p>JSON Schema (draft 2020-12) for every <code>--json</code> result:</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>Environment variables</h2>
<ul>
  <li><code>MARSDAWN_THEME</code>: the theme <code>export</code> uses when <code>--theme</code> isn't passed. An unknown value falls back to <code>dawn</code> without an error.</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>The tool runs on macOS 15 or later. On Apple silicon, Homebrew installs a prebuilt bottle and nothing else is needed. Building it yourself, on an Intel Mac or from the source, needs Swift 6.2 or later, which comes with Xcode 26 or later.</li>
  <li>The MarsDawn app needs macOS 26 or later.</li>
</ul>

<h2>Install</h2>
<p>With Homebrew. On Apple silicon it pours a prebuilt bottle in seconds, with no Xcode needed. On an Intel Mac it compiles marsdawn from source, which takes a few minutes and needs Xcode 26 or later.</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn --version</code></pre>
<p>Or build it from <a href="{k.KIT_URL}">the source</a>. The first build fetches dependencies and compiles, which also takes a few minutes.</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code> prints the version number, such as <code>0.3.0</code>, and exits with code 0.</p>
""",
    }
    pages['cli/skill'] = {
        "title": 'A coding-agent skill for Markdown to PDF · MarsDawn',
        "description": 'One file your coding agent loads to install marsdawn, check it works, export Markdown to PDF and read the JSON result.',
        "body": f"""
<section class="intro">
  <h1>Let your agent make the PDF.</h1>
  <p>This skill is one Markdown file. It teaches a coding agent to install <code>marsdawn</code>, check that it works, export a document to PDF and read the result, so the agent that wrote the Markdown can hand you the PDF as well.</p>
</section>
<h2>Install it in Claude Code</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL {k.SKILL_URL} -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code loads it when a task calls for a PDF, and you can run it yourself as <code>/marsdawn</code>. It's <a href="/cli/skill/SKILL.md">one short file</a>, so read it before you install it.</p>
<p>Other agents can use the same file. It's plain Markdown, instructions and commands, so point yours at the URL or paste it in.</p>
<h2>What it teaches</h2>
<ul>
  <li>Install <code>marsdawn</code> with Homebrew if it's missing, then check it with <code>marsdawn --version</code> instead of assuming a version.</li>
  <li>Export with <code>marsdawn export … --json</code>, and read the result: where the PDF went, how many pages it has, and any Mermaid diagram that didn't render.</li>
  <li>Tell the failures apart by exit code: no such file, a PDF already there, a failed export, a bad option.</li>
  <li>Use <code>open</code> only when the MarsDawn app is installed, and never to make a PDF.</li>
</ul>
<h2>What it doesn't do</h2>
<ul>
  <li>It doesn't give itself permission to run anything. Your agent still asks before it installs <code>marsdawn</code> or runs it, as it would for any other command.</li>
  <li>It doesn't send your documents anywhere. <code>marsdawn</code> renders on your Mac, and it leaves out images from the web unless you pass <code>--allow-remote-images</code>.</li>
</ul>
<p>The whole contract, every field and every code, is in <a href="/ja/cli/agents/">marsdawn for agents</a>.</p>
""",
    }
    return {
        'ui': ui,
        'store_chip': store_chip,
        'schema_notes': schema_notes,
        'example_plan': example_plan,
        'trait_link': trait_link,
        'trait_nav_heading': trait_nav_heading,
        'figure_list_label': figure_list_label,
        'figures': figures,
        'pages': pages,
    }
