# #74 handoff: a /changelog/ page

Grok's copy for [mars-dawn-website#74](https://github.com/redtear1115/mars-dawn-website/issues/74). The page text is `74-changelog-copy.md`. Ship that. Do not ship the draft below it.

## Why the first entry is 0.5.1

The issue says to start from 0.5.2. That tag does not exist (kit tags stop at 0.5.1, annotated 2026-09-19). An empty page, or a page that describes an unreleased version as if it had shipped, is worse than starting one version earlier. 0.5.1 is the latest version with a tag message to check the sentences against. Versions before it stay off the page, which is the part of "starting from 0.5.2" that still holds: no archaeology back to 0.1.0.

Add 0.5.2 above 0.5.1 only after the tag exists, and only with lines that appear in the tag message. The draft at the bottom of the copy file is a holding pen for commits on kit main since 0.5.1. It is not page copy.

## What Claude builds

A normal inner page, `/changelog/`, in all four locales, from the copy file. The site's other pages already move in all four languages together; the issue allows English first, and the other three are written, so ship them in the same change unless the generator cannot accept a partial set. Title it like the other pages. No App Store link, no price, no "download today".

The 0.5.1 bullets are the tag message, rewritten for a reader:

- "CJK text layer repaired" becomes the PDF sentence. It does not claim which bug a reader saw, because the tag doesn't say.
- `--background` and `--folder` are named because the tag names them.
- Mermaid's error block (#71), the zh-Hans/ja kit strings (#68), the preview tests (#72) and the missing-bundle trap (#73) are left out. They are real, and they are not a sentence a visitor can check.

## 0.5.2 draft, held

On kit main since 0.5.1, not tagged. Confirm each line against the eventual tag before it is translated onto the page. Likely candidates, in English only until then:

- `marsdawn skill` prints the agent skill that matches the installed command, so the instructions cannot name a flag that version lacks.
- `marsdawn open` on a folder stops, with an error, when the installed app does not declare that it can open a folder. It no longer reports success and leaves the app to show the error. The message says MarsDawn needs an update, not a version number.
- The skill this version installs no longer teaches `--folder`.
- In the preview, an HTML character reference such as `&eacute;` counts as one character.
- An image the preview cannot load is no longer labelled with a long absolute path, and bidi controls in a path no longer reorder that label.

The last two are preview behaviour inside the kit. Publish them only if the tag presents them as something a person sees.

Co-authored-by: Grok <grok@southern-light.dev>
