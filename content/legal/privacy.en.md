# Privacy Policy

How MarsDawn, the Markdown editor for macOS, handles your information.

Last updated 2026-09-23

> **The MarsDawn app does not collect any data about you.** There is no account, no advertising and no tracking. Your documents and settings stay on your Mac.

## The website

The app and this website are two different things. The app collects nothing. A visit can be recorded only here, on marsdawn.southern-light.dev.

This site uses **Google Analytics 4**, loaded through **Google Tag Manager**. Every visitor starts with analytics denied: Google's Consent Mode sends only a cookieless ping with no analytics cookie and no persistent identifier, until you choose *Accept* in the banner. Choosing *Decline*, or making no choice at all, keeps it that way, and choosing *Decline* after a prior *Accept* turns analytics back off immediately and removes the cookies below. Change your choice at any time with the "Cookie settings" link in the footer of every page. The choice itself is stored only in your browser's local storage, never in a cookie of ours.

Once you accept, Google Analytics sets its own cookies (`_ga` and `_ga_<measurement id>`) and records:

- **Page views and referrer.** Which page was viewed, and the referring address when the browser sends one.
- **Approximate location, device and browser.** A coarse location derived from your IP address (city level at most), your device type, operating system and browser — none of it precise enough to identify you.
- **Outbound clicks and scroll depth.** Google Analytics' enhanced measurement records clicks that leave the site, such as the link to the Mac App Store, and how far you scroll down a page.
- **IP addresses.** Google Analytics 4 does not log or store IP addresses.
- **What is not recorded.** No account, because the site has none. No document, and nothing you type. No cross-site advertising, and no profile of you. Requests the app makes for theme files under `/themes/` are skipped, and are not sent on.
- **Retention.** Google keeps this data for 14 months, then deletes it.
- **Where it's processed.** Google Tag Manager and Google Analytics are operated by Google; your data may be processed in the United States as well as other countries where Google operates.
- **The host.** Cloudflare hosts the site and, like any host, sees your IP address while it answers the request. That log belongs to the host. It is not the analytics above.

## What stays on your Mac

- **Your documents.** MarsDawn reads and writes only the files and folders you open, save or choose. They are never uploaded anywhere by the app.
- **Your settings.** Appearance, preview theme, window layout and the image preference are stored in the app's own preferences on your Mac.
- **Folder access you grant.** When you let MarsDawn show images or page files from a folder, or choose a notes folder, the app keeps a macOS bookmark so it can open that folder again. A folder you open in the sidebar stays readable and writable by MarsDawn until you remove it in Settings, not just while its window is open. You can remove folders at any time in MarsDawn › Settings.

## When MarsDawn uses the internet

MarsDawn works fully offline. It connects to the internet only **when you choose to**, for a document that refers to the web:

- **Markdown documents.** Web images are blocked by default. They load only after you click *Load Images* in the preview, or if you turn on *Load remote images automatically* in Settings. Nothing else a Markdown document refers to is loaded from the web.
- **HTML documents.** An HTML document opens static: its code doesn't run and nothing is loaded from the web. If a document contains code that could run, you can choose *View › Run This Document* for that document. Its own code then runs until you stop it, the document reloads or you close the window. That choice is never remembered, and it isn't a setting. While it runs, the document can send data over the network, and read images, style sheets, fonts and media in its folder and the folders inside it. Code downloaded from the web never runs.

MarsDawn loads web content over https only. A plain http address is never loaded, in any setting, and MarsDawn does not rewrite it to https. In a Markdown document, the preview shows a placeholder in its place.

When web content loads, your Mac requests it directly from the servers that host it. Like any web request, this lets those servers see your IP address and what was requested. MarsDawn's developer receives none of this information.

Links you click in the preview open in your default web browser, under that browser's own privacy practices. Audio and video never play by themselves.

## Siri, Shortcuts and Spotlight

MarsDawn offers actions for Siri, the Shortcuts app and Spotlight, such as creating a document or adding a note. When you use them, the text you provide is passed to MarsDawn on your Mac and saved only where the action says (a new document, or the `Inbox.md` file in the notes folder you chose). Speech you dictate to Siri is handled by Apple under [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).

## Exporting and printing

PDF export and printing happen on your Mac. The PDF is saved where you choose. Printing goes through macOS to the printer you pick.

## The marsdawn command-line tool

The optional `marsdawn` command-line tool, distributed separately, also runs entirely on your Mac. It reads the Markdown file you name and writes the PDF you ask for. It loads web images only when you pass `--allow-remote-images`.

## Children

The MarsDawn app does not collect data from anyone, including children. A visit recorded on the website is not an account, and it is not used to identify anyone.

## Purchases

MarsDawn will be sold through the Mac App Store. Apple will process the purchase under its own terms, and the developer never receives your payment details.

## Changes to this policy

If MarsDawn ever starts handling data differently, this page will be updated before that version is released, and the date at the top will change.

## Contact

Questions about privacy: [support@southern-light.dev](mailto:support@southern-light.dev)
