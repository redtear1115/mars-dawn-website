# A test that passes on one Mac may not be testing what you think.

Black Friday: the one-time unlock is half price, USD 2.49 instead of USD 4.99, through 30 November. It returns to USD 4.99 on 1 December. <!-- sale-line -->

Vibe coding isn't a bad thing, and MarsDawn is built with agents too. But software you rely on is judged by what comes after the first version: years of maintenance and security, which start with checking that a change didn't break anything.

**A test passed on a Mac mini and failed on a MacBook Air. The product was fine. The test had been reading colours through the screen's colour profile, and on the Mac mini it had been passing by luck. A second machine found a bug in the test, not in the code.**

Only want to know which extreme or hostile files MarsDawn is tested against? Skip to [What we throw at it](#inputs).

## The test that failed on a MacBook Air

A full run of the export engine's tests on GitHub's macOS 15 runner takes close to an hour: about 32 minutes for the debug build and about 25 for the release build. To cut that down, we tried moving the macOS 26 half onto a MacBook Air of our own ([kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240)).

On its first run there, one test failed. It exports a PDF with callouts (Note, Tip, Warning) and checks that each one has a bar at its edge in the right colour, meaning a colour distance under 0.16. On the MacBook Air the distances were 0.1634, 0.1648 and 0.1796. On a Mac mini, with the same commit, macOS and Xcode, the test passed.

Our first guess was that the export had broken. It hadn't. Nothing was wrong with the PDF; what differed between the machines was how the test read it.

The test turned each PDF page into an image and read the pixels, and macOS draws that image in the colour space of the main display. The Mac mini was connected to an ordinary external monitor; the MacBook Air was using its built-in screen. We filled an image with one orange and read it back: (0.784, 0.278, 0.106) came back as (0.822, 0.335, 0.179) on the Mac mini and (0.782, 0.395, 0.221) on the MacBook Air.

Here's the part that matters: on the Mac mini, the test hadn't been reading the right colours either. It was off by as much as 0.128, just inside the 0.16 limit. It passed because of the monitor, not because it measured the bar correctly.

The fix ([kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242)) changes only the test: it draws the page into an image with a fixed sRGB colour space, so no screen is involved. Both machines now read the bar colours exactly, with a distance of 0.0, on the MacBook Air's built-in screen as well as on the Mac mini. The pull request's CI passed ([run 40285279080](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080)), and once the fix reached the MacBook Air runner branch, the full suite passed there too ([run 40315907904](https://github.com/redtear1115/mars-dawn-kit/actions/runs/40315907904)). Then we made it fail on purpose: with every expected colour set to blue, it went red for all five callouts.

It still has a known gap. Note and Caution use two oranges about 0.119 apart, inside the 0.16 limit, so if those two were swapped, the test would probably not notice. We've written that down rather than pretend the test is complete.

A test that can't fail protects nothing, and neither does one that fails for the wrong reason, like a screen's colour profile. Green on one machine tells you the test passed there, not that it measures what its name says.

## Tests are layers of nets

No single test catches everything. Each layer is a net with a different mesh, and a mistake that slips through one should land in the next:

- **Reference PDFs:** the export engine (the open-source [mars-dawn-kit](https://github.com/redtear1115/mars-dawn-kit), which also powers the `marsdawn` command) exports sample documents, and every page's text is compared with a recorded copy. This catches content that silently goes missing, or a page count that changes.
- **Different systems and builds:** the engine runs on macOS 15, the oldest version it supports, and macOS 26, the one the app ships on, each as a debug and a release build. The app's full suite runs in four combinations: signed and unsigned, each with the paywall off and on. This catches what breaks only on an older system, or only in the build customers actually get.
- **Real hardware:** the app's CI runs on Macs of our own (both the Mac mini and the MacBook Air), and trying the engine's suite on that MacBook Air ([kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240), still an open draft) is what caught the colour-profile bug above. A second machine catches tests that pass only because of the machine they run on.
- **Red controls:** the app's CI keeps 22 deliberately broken copies of a cleanup script and 20 of its test runner script, each missing one safety check, and the tests must fail on every one. The cleanup script removes old builds and working copies from a Mac, so one missing check could remove the wrong thing. If a broken copy passes, the test is what's broken.
- **A second pair of eyes:** our practice is to have a separate agent verify a change before it's merged, as with kit #242, and changes to how people use the app get a scenario review first. This catches "done" that isn't, and code that works but in the wrong situation.
- **A person merges.** The developer behind MarsDawn reviews and merges every change; no agent or bot merges anything.

## What we throw at it

Those nets are only as good as what goes into them. A few of the inputs the engine's tests feed it, and what each test makes sure happens:

- **Very large files.** On our test machine, in a release build, a 2 MB document renders in under a second and a half, and a 5 MB one too complex to lay out still opens as plain text within a second. Anything over 16 MB is shown as text without being parsed at all.
- **Hundreds of thousands of lines.** About 3 MB of one-word lines, close to 800,000 of them, is spotted as too much partway through: the engine stops reading there and shows the file as plain text.
- **Markers that never close.** A megabyte of section openers with no closers, or tens of thousands stacked inside each other, must take no more than about twice as long as a megabyte of plain text. Past eight levels, nothing nests any deeper.
- **Formulas.** A broken formula shows an error where it sits instead of breaking the page. One over 10,000 characters stays as written, only the first 1,000 in a document are drawn at a time, and nothing in a formula can turn into a link, an image or page markup.
- **Hostile HTML inside Markdown.** Scripts are removed and never run, and embedded frames are taken out before the page shows them. Remote images stay off unless you allow them, and even then only secure (HTTPS) ones load. One control copy has the script filter taken out, and the test must fail on it.
- **A hostile theme file.** It's refused, and the error message never repeats hidden control characters or links from the file. Theme files over 16 KB aren't read at all.

None of this is free. The time limit for one engine run has gone from 30 minutes to 45, then 50, then 70, and now 90; macOS 15 hit the 50-minute limit twice with every test passing, and later hit 70 minutes in its final step with every step before it passing.

## Four habits you can copy

1. **Keep the agent that writes apart from the agent that checks.** Give the checker the change and what "done" means, not the writing agent's explanation, and ask it to run the tests itself and say what it didn't check. For kit #242, the verifier ran the old test on the MacBook Air to watch it fail before passing the new one. It costs a second session's tokens.
2. **See every test fail once.** Green only means something if you've seen the same test go red when the thing it checks was really wrong. So before you trust a green check, break what it guards (or ask the agent to), watch it go red, put it back, and watch it go green. Agents are good at writing tests that pass; that's exactly why you need to see them fail.
3. **Run your tests in a second environment.** No second Mac? A CI matrix with two OS versions, or a debug build and a release build, is a fine start. You're looking for tests that pass only by accident.
4. **Treat "no tests ran" as a failure.** Python 3.9's `unittest` exits successfully when it finds no tests at all, so a typo in a path gives you a green check. Our CI reads the count and fails on zero, and checks that the summary says "0 failed", not just the exit code. We added that check after an independent verification caught the gap in our own CI.

## The short version

Whether an app was vibe coded matters less than whether anyone keeps testing and maintaining it. That's worth checking when you choose software: does it say how it's tested, and when was it last updated?

Let the agent be fast. Leave the checking to tests that measure the right thing, and to a person who reads the result.

## Next

- Why a person still has to read what an agent wrote: [Why AI output still needs a human reader](/reviewing-ai-output/).
- How to read the plans and reports an agent hands back: [Reading what your agent hands back](/reading-agent-output/).

## Sources

- The failing test and its cause: [mars-dawn-kit #241](https://github.com/redtear1115/mars-dawn-kit/issues/241).
- The fix and its independent verification: [mars-dawn-kit #242](https://github.com/redtear1115/mars-dawn-kit/pull/242).
- Trying CI on a MacBook Air (open draft), with run times: [mars-dawn-kit #240](https://github.com/redtear1115/mars-dawn-kit/pull/240).
- The export engine's CI, with the history of its time limit in the comments: [ci.yml](https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml).
- The app's repository is private; the app details above come from its CI workflow and test scripts.

## More

- [MarsDawn](https://marsdawn.southern-light.dev/index.md): Read and review your agent's Markdown, JSON and YAML natively on Mac: live preview, Mermaid, KaTeX, Quick Look, PDF export. Free to try, USD 2.49 once.
- [Features](https://marsdawn.southern-light.dev/features/index.md): A native Mac editor for Markdown, JSON and YAML: live preview, Mermaid and math, themes, plus clean PDF and print pages for meetings and records.
- [Your writing stays on your Mac](https://marsdawn.southern-light.dev/yours/index.md): MarsDawn has no account, no sync and no cloud. Your Markdown documents stay on your Mac, in the files and folders you choose.
- [Try free, pay once](https://marsdawn.southern-light.dev/pay-once/index.md): MarsDawn is free to download. Try everything for 14 days, then unlock it once for USD 2.49. No subscription, no account.
- [Print & PDF](https://marsdawn.southern-light.dev/pdf/index.md): Preview your Markdown, then print it or save it as a PDF on your Mac, in Document, Handbook or Handout layout, with diagrams and code colors intact.
- [A Mac app](https://marsdawn.southern-light.dev/native/index.md): A Markdown editor that is a real Mac app: native windows and tabs, autosave, version history, Quick Look in Finder and a text editor that behaves like a Mac.
- [What MarsDawn doesn't do](https://marsdawn.southern-light.dev/limits/index.md): No sync, no editing on iPhone or iPad, no plugins, no accounts. Themes, but no custom CSS. Know before you buy.
- [Support](https://marsdawn.southern-light.dev/support/index.md): Get help with MarsDawn, the Markdown editor for macOS.
- [Privacy Policy](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [How to open .md files on Mac](https://marsdawn.southern-light.dev/view-markdown-on-mac/index.md): How to open a .md file on a Mac: double-click, set a default app, preview in Finder. For .md files an AI agent wrote, read them rendered in MarsDawn.
- [Mermaid preview on Mac](https://marsdawn.southern-light.dev/mermaid-preview-mac/index.md): See Mermaid diagrams drawn next to your Markdown on a Mac: live preview, Quick Look and PDF export. A broken diagram shows its error and the line.
- [Quick Look for Markdown](https://marsdawn.southern-light.dev/quicklook/index.md): MarsDawn's Quick Look renders Markdown in Finder when you press Space, with Mermaid, KaTeX and highlighted code. It keeps working after the trial ends.
- [Copy for AI](https://marsdawn.southern-light.dev/copy-for-ai/index.md): Copy selected text with its file path and line numbers, then paste it into Claude Code or any agent. MarsDawn does this on your Mac, with no IDE or plugin.
- [Move from HackMD to your Mac](https://marsdawn.southern-light.dev/from-hackmd/index.md): Download your HackMD notes as .md files and read them in MarsDawn on your Mac. How to download every note, use a GitHub repo, and keep your images working.
- [Markdown to PDF](https://marsdawn.southern-light.dev/markdown-to-pdf/index.md): Convert Markdown to PDF on a Mac with the free marsdawn command-line tool. Install it with Homebrew and run one command: tables, math, Mermaid and code.
- [MarsDawn compared: VS Code preview, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/vs/index.md): For anyone choosing how to read and review Markdown on a Mac, often what an agent wrote. Every cell below comes from the vendor's own pages or our own check, all on 16 October 2026, except MarsDawn's PDF cell, updated on 7 November 2026; products change, so a cell can go stale. If you spot a mistake, write to the address on Support.
- [MacMD Viewer vs. MarsDawn](https://marsdawn.southern-light.dev/vs/macmd-viewer/index.md): MacMD Viewer is a read-only Markdown viewer for USD 19.99. MarsDawn edits and previews side by side: free for 14 days, then USD 2.49 once.
- [Best Markdown viewer for Mac (2026)](https://marsdawn.southern-light.dev/best-markdown-viewer-mac/index.md): Eight Markdown viewers for Mac compared by price, Mermaid, math, PDF, live reload, Quick Look and native vs Electron, with who each one suits.
- [Command Line](https://marsdawn.southern-light.dev/cli/index.md): The free marsdawn command-line tool for Mac: export Markdown to PDF from a shell, a script or an LLM agent, with JSON output. Install it with Homebrew.
- [marsdawn for agents](https://marsdawn.southern-light.dev/cli/agents/index.md): A reference for AI agents and scripts that call marsdawn to turn Markdown into PDF: commands, JSON output, schemas, exit codes and requirements.
- [Agent skill](https://marsdawn.southern-light.dev/cli/skill/index.md): One file your coding agent loads to open Markdown it wrote in MarsDawn for your review, and to install marsdawn, export Markdown to PDF and read the JSON result.
- [MCP server](https://marsdawn.southern-light.dev/cli/mcp/index.md): marsdawn has no AI model of its own, so it doesn't matter which agent wrote the Markdown. Call it from the CLI, a skill file, or the marsdawn-mcp MCP server: all three run the same export.
- [Token-efficient review](https://marsdawn.southern-light.dev/token-efficient-review/index.md): A person reviews the rendered page in MarsDawn, never read back into the agent's context. The tool call itself returns a compact JSON result, not the rendered content, so calling it is cheap too.
- [Viewing Markdown elsewhere vs. MarsDawn](https://marsdawn.southern-light.dev/vs/markdown-preview-tools/index.md): How MarsDawn compares to reading Markdown in VS Code's built-in preview, a browser extension, or Claude Desktop's file preview: what each renders, and what it takes to open one file.
- [Themes](https://marsdawn.southern-light.dev/themes/index.md): Four built-in preview themes, each light and dark, plus a curated gallery you open from Settings in MarsDawn for Mac. Quick Look uses your theme.
- [Build a theme](https://marsdawn.southern-light.dev/themes/new/index.md): Pick colours and a handful of style options, see them applied to a sample document live, and submit your theme as a GitHub issue. No install, no git.
- [Make a theme with your agent](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [Theme gallery](https://marsdawn.southern-light.dev/themes/gallery/index.md): Browse preview themes for MarsDawn, each reviewed by the developer, filter them by scenario, and report a problem with one. Build your own in the browser.
- [Sharing exported PDFs](https://marsdawn.southern-light.dev/sharing-exported-pdfs/index.md): Export an agent's Markdown to PDF and hand it to a colleague who doesn't read Markdown and won't install anything. No syntax, no app and no account needed to open it.
- [Why AI output still needs a human reader](https://marsdawn.southern-light.dev/reviewing-ai-output/index.md): AI-written Markdown still has to be understood by a person, not trusted on sight. MarsDawn pairs the rendered page with the source, and draws Mermaid diagrams and KaTeX math, so structure is legible at a glance.
- [Reading what your agent hands back](https://marsdawn.southern-light.dev/reading-agent-output/index.md): AI agents hand back their work as Markdown: plans, specs, progress reports. What people who build agents say about checkpoints and failures, why that output is hard to read, and a five-minute checklist for reviewing a plan.
- [Agent transparency](https://marsdawn.southern-light.dev/agent-transparency/index.md): Anthropic's guide to building agents asks for transparency: show the planning steps. What it says, what it doesn't, and why the steps usually end up as a Markdown file someone has to read.
- [Reviewing an agent plan](https://marsdawn.southern-light.dev/reviewing-agent-plans/index.md): A six-step way to review the plan an AI agent hands you before it runs, in about five minutes and in any editor, with a worked example.
- [Agent design patterns](https://marsdawn.southern-light.dev/agent-design-patterns/index.md): Reflection, tool use, planning and multi-agent collaboration, as Andrew Ng described them, and what each tends to hand back for you to read.
- [Changelog](https://marsdawn.southern-light.dev/changelog/index.md): What changed in each version of the MarsDawn app and the free marsdawn CLI.
- [Roadmap](https://marsdawn.southern-light.dev/roadmap/index.md): What's in progress and what's next for MarsDawn on Mac, iPhone and iPad, by version. No dates, and unscheduled ideas are marked.
- [Editor's reading notes](https://marsdawn.southern-light.dev/reading-notes/index.md): Six short notes on what the people building AI agents actually argue — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain and Andrew Ng — and what each one means for the person who has to read what such an agent hands back.
- [Reading notes: Anthropic](https://marsdawn.southern-light.dev/reading-notes/anthropic-building-effective-agents/index.md): Anthropic's December 2024 guide for people building agents separates workflows from agents and describes five workflow patterns, including one where a second LLM call reviews the first. What that means for what lands in your folder.
- [Reading notes: Chip Huyen](https://marsdawn.southern-light.dev/reading-notes/chip-huyen-agents/index.md): Chip Huyen's January 2025 essay on agents splits their actions into read-only and write actions. Why that split is a fast way to spot the line in a plan worth a closer look before you approve it.
- [Reading notes: Lilian Weng](https://marsdawn.southern-light.dev/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng's widely cited 2023 survey describes an LLM agent as a brain plus planning, memory and tool use. What each part tends to leave behind for you to read, and the limitation she names in plans that don't adjust to surprises.
- [Reading notes: Harrison Chase](https://marsdawn.southern-light.dev/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase's 2024 definition of an agent and his spectrum of agentic behavior, and his case for observability as a system moves along it — read from the side of whoever reads the file it hands back.
- [Reading notes: LangChain (Jess Ou)](https://marsdawn.southern-light.dev/reading-notes/langchain-what-is-an-agent/index.md): LangChain's 2026 “What is an AI agent?” by Jess Ou echoes Harrison Chase's 2024 definition and describes a pipeline for evaluating agents automatically. Where that pipeline still hands a step to a person, and where it doesn't.
- [Reading notes: Andrew Ng](https://marsdawn.southern-light.dev/reading-notes/andrew-ng-design-patterns/index.md): Across five letters in The Batch, Andrew Ng ranks reflection, tool use, planning and multi-agent collaboration by how reliable and predictable he finds each one — and what that ranking suggests about how closely to check each one's output.
- [Templates](https://marsdawn.southern-light.dev/templates/index.md): Markdown templates for the documents an agent writes and you read: a spec, a flowchart and meeting notes, each with a prompt for your agent.
- [Spec template](https://marsdawn.southern-light.dev/templates/spec/index.md): A Markdown spec template with requirements, a Mermaid flow diagram and acceptance criteria. Your agent fills it in; you review it in MarsDawn.
- [Flowchart template](https://marsdawn.southern-light.dev/templates/flowchart/index.md): A Mermaid flowchart template in Markdown, with the steps written out below it. Preview it on a Mac and export it to PDF.
- [Meeting notes template](https://marsdawn.southern-light.dev/templates/meeting-notes/index.md): A Markdown meeting notes template with decisions and action items, each with an owner. Your agent writes it up; you check it in MarsDawn.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/how-we-test/index.md): 同一個測試，在一台 Mac 通過、在另一台失敗。產品沒壞，是測試讀到了螢幕的色彩。我們怎麼一層一層地測試，以及你也能照做的四個習慣。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/how-we-test/index.md): 同一个测试，在一台 Mac 上通过，在另一台上失败。产品没坏，是测试读到了屏幕的色彩。我们怎么一层一层地测试，以及你也能照做的四个习惯。
- [日本語](https://marsdawn.southern-light.dev/ja/how-we-test/index.md): あるテストが 1 台の Mac では通り、もう 1 台では失敗しました。製品は壊れておらず、テストが画面の色を読んでいたのです。テストを何層にも重ねるやり方と、まねできる 4 つの習慣。
- [Deutsch](https://marsdawn.southern-light.dev/de/how-we-test/index.md): Ein Test bestand auf einem Mac und schlug auf einem anderen fehl. Das Produkt war in Ordnung; der Test las die Farben des Bildschirms. Wie wir Tests schichten, und vier Gewohnheiten zum Nachmachen.
- [Français](https://marsdawn.southern-light.dev/fr/how-we-test/index.md): Un test passait sur un Mac et échouait sur un autre. Le produit allait bien ; le test lisait les couleurs de l’écran. Comment nous superposons nos tests, et quatre habitudes à reprendre.
- [Español](https://marsdawn.southern-light.dev/es/how-we-test/index.md): Una prueba pasaba en un Mac y fallaba en otro. El producto estaba bien; la prueba leía los colores de la pantalla. Cómo apilamos nuestras pruebas, y cuatro hábitos que puedes copiar.
- [한국어](https://marsdawn.southern-light.dev/ko/how-we-test/index.md): 한 Mac에서 통과한 테스트가 다른 Mac에서는 실패했습니다. 제품은 멀쩡했고, 테스트가 화면의 색을 읽고 있었습니다. 테스트를 여러 겹으로 쌓는 방법과 따라 할 수 있는 네 가지 습관.
