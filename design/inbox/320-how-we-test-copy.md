# #320 How we test MarsDawn: all 8 locales

Issue: https://github.com/redtear1115/mars-dawn-website/issues/320
Outline: the issue's latest comment (Una's review, accepted as is), plus Ray's later decisions relayed by Paula (S11, S14).
Status: **proposal**. It goes live only after Ray approves.

## How to read this file

- The bodies below are HTML fragments in the same shape as the other evergreen articles in `scripts/build_pages.py` (`section.intro` → `div.summary` → `h2` sections → Next → Sources).
- **Every number has a source in an HTML comment** (`<!-- src: ... -->`), as #320's acceptance requires.
- **Placeholders**: `{{TBD:...}}`. kit #242's are filled in (merged as 85fe880, PR CI run 40285279080). One is left: the self-hosted MacBook Air run, which comes from kit #240. Don't publish while any are left: `grep -n 'TBD' design/inbox/320-how-we-test-copy.md`.
- Suggested slug: `/how-we-test/` (zh-Hant `/zh-hant/how-we-test/`). It needs to be added to `article_dates.py`'s `ARTICLE_SLUGS` and to the footer `ui` dict. Footer labels are at the end of this file.
- The app repo is private, so app facts are described in the text but not linked. Kit facts link to the public kit repo.

## Facts and sources

| # | Fact | Source |
|---|---|---|
| S1 | The test failed on the MacBook Air: 0.1634 / 0.1648 / 0.1796, limit 0.16. It passed on the Mac mini. Same commit, macOS 26.6.2, Xcode 27.1. | kit #241 body; CI run 40271990387 |
| S2 | The pure-colour probe: sRGB (0.784, 0.278, 0.106) reads back as (0.822, 0.335, 0.179) on the mini and (0.782, 0.395, 0.221) on the Air. | kit #241 body |
| S3 | Independent verification of the fix: `best` 0.0 on both machines. The old path on the mini was off by up to 0.128. With the expected colours set to #0000FF, all 5 callouts fail. Note (#C8471B) and Caution (#B03C0C) are about 0.119 apart. | kit PR #242, comment of 2026-10-26 07:39 UTC |
| S4 | A full run on hosted macOS 15: debug about 32 min plus release about 25 min (run 40196953693). Moving macOS 26 to self-hosted MacBook Airs is expected to cut a normal PR from about 60 min to about 15–20. | kit PR #240 body (**not merged**; the 15–20 min figure is an estimate and is not used in the text) |
| S5 | The timeout went from 30 to 45, then 50, then 70 minutes. macos-15 hit the 50-minute limit twice in the release pass with every test passing (run 39231688388). | kit `.github/workflows/ci.yml` comments, main 8e93930, lines 27–34 |
| S6 | Kit CI matrix: macos-15 (the floor) and macos-26 (what the app ships on), debug and release passes. The PDF corpus runs in its own process. A release suite name that matches no test fails the job. | kit `ci.yml` lines 21–26, 85–129 |
| S7 | App CI: one self-hosted runner, `CODE_SIGNING_ALLOWED=NO`. python 3.9's unittest exits 0 having found no tests, so the job checks that the count is above 0, and guards.sh's summary must read "N passed, 0 failed" with N > 0. | app `.github/workflows/ci.yml` lines 78–108 (private) |
| S8 | That guards.sh check came out of an independent verification of #335 (finding P3). | app #341 (private) |
| S9 | `tools/test.sh --all`: signed and unsigned, each with the paywall off and on, so 4 combinations, run locally on a Mac and a MacBook Air (not in CI). **These are not debug/release × macOS 15/26; that matrix is the kit's CI (S6).** | app `tools/test.sh` lines 9, 24–26; #320 owner comment |
| S10 | kit #242 merged as 85fe880. Its PR CI run is all green. | https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080 |
| S11 | Vibe coding framing: Ray's decision, relayed by Paula on 2026-10-26: vibe coding isn't bad, but software depends on long-term maintenance and security, and people should be choosy about the software they pick. No names of people or products. | #320 / Ray |
| S12 | Red controls: the app's CI expects exactly 11. Each is a copy of the local cleanup script (`tools/cleanup-local.sh`) with one safety guard cut out, and the test suite must FAIL against every one; if a copy passes, CI fails. | app `ci.yml` (`expected 11 red controls caught`); `tools/test-cleanup-local.sh` lines 9–13, 685–713 (private) |
| S13 | PDF goldens: sample documents are exported and each page's text is compared with a recorded copy, per OS build (the `pdf-goldens` CI job). The corpus guards against export silently losing content, the page count changing, and export drifting from the preview. | kit `Tests/MarsDawnExportTests/PDFCorpusTests.swift` lines 10–13, 126–175; `record-pdf-goldens.yml` |
| S14 | Ray's decision, relayed by Paula on 2026-10-26: add back "deliberately break a test to check it catches the error" as a recommended habit, and lead into 「測試是一層一層的網子，有很多種目的，這種紅綠測試的意涵」. | #320 / Ray |
| S15 | Scenario review: UX copy and flows go through a scenario review (`needs-ux` → `replied-ux`) before copy and build; #320 itself went through one. | website #320 labels and comment of 2026-10-26 08:31 UTC |
| S16 | Large inputs. 2 MB of dense Markdown renders within 1.5 s; 5 MB (about a million nodes) falls back to plain source within 1.0 s (release budgets; debug allows 10×). The default byte cap is 16 MiB: one byte over is shown as source, unparsed. About 3 MB of one-line blocks (`- a`, `# a`; ~786,000 lines) is refused by the pre-scan's early stop and falls back as too complex (no timing assertion). There is **no** test aimed at line breaks as such; this is the closest. | kit main 85fe880: `Tests/MarsDawnKitTests/MarkdownParsingTests.swift` lines 375–394 (`largeDocuments`), 396–417; `Tests/MarsDawnKitTests/ByteCapTests.swift` lines 5–7, 73, 103; `Tests/MarsDawnKitTests/NodeBudgetTests.swift` line 218 (`realSizeBlockHeavyDocumentsStopEarly`) |
| S17 | Unclosed markers. 1 MiB of `:::` callout openers with no closers, and 65,536 openers then closers, must each render in under 2× the time of 1 MiB of plain text (+0.05 s). Callout nesting caps at 8. Doubling unmatched `<details>` openings may at most 2.5× the time (release). | kit `Tests/MarsDawnKitTests/CalloutSecurityTests.swift` lines 125–146, 156; `Tests/MarsDawnKitTests/DetailsGroupingCostTests.swift` lines 74–84 |
| S18 | Math (KaTeX in the preview). A bad expression shows an error instead of throwing; over 10,000 characters stays as source; at most 1,000 expressions per update; hostile TeX never becomes markup; `trust: false` gives no link or image. | kit `Tests/MarsDawnKitTests/PreviewMathPageTests.swift` lines 85, 98, 133, 160, 192; `Tests/MarsDawnKitTests/MathRenderingTests.swift` lines 383–387 |
| S19 | Hostile HTML. `script`/`noscript` are removed from the content and nothing runs; a copy with that filter reverted must fail (red control); inline handlers are blocked by the enforced CSP; `link`/`meta`/`base`/`iframe`/`object`/`embed` never reach the page. Remote content: the blocked list stops every request; with remote images allowed only the HTTPS image loads and plain HTTP never connects; preconnects are stopped too. | kit `Tests/MarsDawnKitTests/PreviewFilterAndCSPSecurityTests.swift` lines 43, 54, 96; `Tests/MarsDawnKitTests/PreviewDOMFilterTests.swift` lines 29–31, 98; `Tests/MarsDawnKitTests/ContentRuleBehaviorTests.swift` lines 84, 150, 245 |
| S20 | Hostile theme files are refused, and no message repeats a control character, a link, a mention or more than a capped slice of the input. Theme files over 16,384 bytes are refused unread. | kit `Tests/MarsDawnThemesTests/ThemeFixtureTests.swift` lines 108–123, 128, 145 |

---

## en

- **title**: `How we test MarsDawn: one test, two Macs · MarsDawn`
- **description** (about 150 characters): `A test passed on one Mac and failed on another. The product was fine; the test was reading the screen's colours. How we layer our tests, and four habits you can copy.`

```html
<section class="intro">
  <h1>A test that passes on one Mac may not be testing what you think.</h1>
  <!-- src S11 -->
  <p>Vibe coding isn't a bad thing. Describing what you want and letting an agent build it is how a lot of software starts now, and MarsDawn is built with agents too. But software people rely on is judged by what comes after the first version: years of maintenance, and keeping it secure. An agent can change dozens of files in an evening. So who checks it didn't break anything? Here is one test that showed us how that checking goes wrong, and what we changed.</p>
</section>

<div class="summary"><p><strong>A test passed on a Mac mini and failed on a MacBook Air. The product was fine. The test had been reading colours through the screen's colour profile, and on the Mac mini it had been passing by luck. A second machine found a bug in the test, not in the code.</strong></p></div>

<h2>The test that failed on a MacBook Air</h2>
<!-- src S4: kit PR #240 (not merged), run 40196953693 -->
<p>A full run of the export engine's tests on GitHub's macOS 15 runner takes close to an hour: about 32 minutes for the debug build and about 25 for the release build. To cut that down, we started moving the macOS 26 half onto a MacBook Air of our own (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>).</p>
<!-- src S1: kit #241, run 40271990387 -->
<p>On its first run there, one test failed. It exports a PDF with callouts (Note, Tip, Warning) and checks that each one has a bar at its edge in the right colour, meaning a colour distance under 0.16. On the MacBook Air the distances were 0.1634, 0.1648 and 0.1796. On a Mac mini, with the same commit, macOS and Xcode, the test passed.</p>
<p>Our first guess was that the export had broken. It hadn't. Nothing was wrong with the PDF; what differed between the machines was how the test read it.</p>
<!-- src S1, S2: kit #241 -->
<p>The test turned each PDF page into an image and read the pixels, and macOS draws that image in the colour space of the main display. The Mac mini was connected to an ordinary external monitor; the MacBook Air was using its built-in screen. We filled an image with one orange and read it back: (0.784, 0.278, 0.106) came back as (0.822, 0.335, 0.179) on the Mac mini and (0.782, 0.395, 0.221) on the MacBook Air.</p>
<!-- src S3: kit #242 verification comment -->
<p>Here's the part that matters: on the Mac mini, the test hadn't been reading the right colours either. It was off by as much as 0.128, just inside the 0.16 limit. It passed because of the monitor, not because it measured the bar correctly.</p>
<!-- src S3, S10; {{TBD:mba-run}} = the self-hosted MacBook Air run, from kit #240 -->
<p>The fix (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>) changes only the test: it draws the page into an image with a fixed sRGB colour space, so no screen is involved. Both machines now read the bar colours exactly: the best match is 0.0, on the MacBook Air's built-in screen as well as on the Mac mini. The pull request's CI passed (<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>), and so did the full suite on the MacBook Air runner (run {{TBD:mba-run}}). Then we made it fail on purpose: with every expected colour set to blue, it went red for all five callouts.</p>
<p>It still has a known gap. Note and Caution use two oranges about 0.119 apart, inside the 0.16 limit, so if those two were swapped, the test would probably not notice. We've written that down rather than pretend the test is complete.</p>
<p>A test that can't fail protects nothing, and neither does one that fails for the wrong reason, like a screen's colour profile. Green on one machine tells you the test passed there, not that it measures what its name says.</p>

<h2>What red and green mean</h2>
<!-- src S14 -->
<p>Green means a test passed. That's only worth something if you've seen the same test go red when the thing it checks is actually wrong. So the order matters: break it on purpose, watch it turn red, put it back, watch it turn green. Then you know the test is looking at the right thing. If you've never seen it red, a green check might just mean the test isn't looking.</p>

<h2>Tests are layers of nets</h2>
<p>No single test catches everything. Each layer is a net with a different mesh, and a mistake that slips through one should land in the next:</p>
<ul>
  <!-- src S6 -->
  <li><strong>Unit tests</strong> in the export engine (the open-source <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>, which also powers the <code>marsdawn</code> command): a piece of code that returns the wrong answer.</li>
  <!-- src S13 -->
  <li><strong>Reference PDFs:</strong> sample documents are exported and every page's text is compared with a recorded copy. This catches content that silently goes missing, or a page count that changes.</li>
  <!-- src S6, S9 -->
  <li><strong>Different systems and builds:</strong> the engine runs on macOS 15, the oldest version it supports, and macOS 26, the one the app ships on, each as a debug and a release build. The app's full suite runs in four combinations: signed and unsigned, each with the paywall off and on. This catches what breaks only on an older system, or only in the build customers actually get.</li>
  <!-- src S4, S1 -->
  <li><strong>Real hardware:</strong> besides GitHub's machines, tests run on Macs of our own, including the MacBook Air above. This catches what a server without a screen can't show.</li>
  <!-- src S12 -->
  <li><strong>Red controls:</strong> the app's CI keeps 11 deliberately broken copies of a cleanup script, each missing one safety check, and the tests must fail on every one. If one passes, the test is the thing that's broken.</li>
  <!-- src S3, S15 -->
  <li><strong>A second pair of eyes:</strong> a separate agent verifies each change, and a scenario review checks how people will really use a feature before it's built. This catches "done" that isn't, and code that works but in the wrong situation.</li>
  <li><strong>A person merges.</strong> No change reaches the main branch because an agent said it was done.</li>
</ul>

<h2>What we throw at it</h2>
<p>Those nets are only as good as what goes into them. A few of the inputs the engine's tests feed it, and what each test makes sure happens:</p>
<ul>
  <!-- src S16 -->
  <li><strong>Very large files.</strong> A 2 MB document renders in under a second and a half. A 5 MB one too complex to lay out still opens, as plain text, within a second. Anything over 16 MB is shown as text without being parsed at all.</li>
  <!-- src S16 -->
  <li><strong>Hundreds of thousands of lines.</strong> About 3 MB of one-word lines, close to 800,000 of them, is spotted as too much partway through reading and shown as plain text instead of tying the app up.</li>
  <!-- src S17 -->
  <li><strong>Markers that never close.</strong> A megabyte of section openers with no closers, or tens of thousands nested inside each other, must take no more than about twice as long as a megabyte of plain text. Nesting stops at eight levels.</li>
  <!-- src S18 -->
  <li><strong>Formulas.</strong> A broken formula shows an error where it sits instead of breaking the page. One over 10,000 characters stays as written, only the first 1,000 in a document are drawn at a time, and nothing in a formula can turn into a link, an image or page markup.</li>
  <!-- src S19 -->
  <li><strong>Hostile HTML inside Markdown.</strong> Scripts are removed and never run, and embedded frames are taken out before the page shows them. Remote images stay off unless you allow them, and even then only secure (HTTPS) ones load. One control copy has the script filter taken out, and the test must fail on it.</li>
  <!-- src S20 -->
  <li><strong>A hostile theme file.</strong> It's refused, and the error message never repeats hidden control characters or links from the file. Theme files over 16 KB aren't read at all.</li>
</ul>
<!-- src S5 -->
<p>None of this is free. The time limit for one engine run has gone from 30 minutes to 45, then 50, then 70, and macOS 15 once hit the 50-minute limit twice with every test passing.</p>

<h2>Four habits you can copy</h2>
<ol>
  <li><strong>Keep the agent that writes apart from the agent that checks.</strong> Give the checker the change and what "done" means, not the writer's explanation, and ask it to run the tests itself and say what it didn't check. For kit #242, the verifier ran the old test on the MacBook Air to watch it fail before passing the new one. It costs a second session's tokens, which is still cheaper than fixing a broken change later.</li>
  <li><strong>See every test fail once.</strong> Before you trust a green check, break the thing it guards (or ask the agent to) and make sure it goes red. Agents are good at writing tests that pass; that's exactly why you need to see them fail.</li>
  <li><strong>Run your tests in a second environment.</strong> No second Mac? A CI matrix with two OS versions, or a debug build and a release build, is a fine start. You're looking for tests that pass only by accident.</li>
  <!-- src S7, S8 -->
  <li><strong>Treat "no tests ran" as a failure.</strong> Python 3.9's <code>unittest</code> exits successfully when it finds no tests at all, so a typo in a path gives you a green check. Our CI reads the count and fails on zero, and checks that the summary says "0 failed", not just the exit code. An agent reporting "all tests pass" when none ran is one of the most common false finishes there is.</li>
</ol>

<h2>The short version</h2>
<!-- src S11 -->
<p>Whether an app was vibe coded matters less than whether anyone keeps testing and maintaining it. That's worth checking when you choose software: does it say how it's tested, and when was it last updated?</p>
<p>Let the agent be fast. Leave the checking to tests that measure the right thing, and to a person who reads the result.</p>

<h2>Next</h2>
<ul>
  <li>Why a person still has to read what an agent wrote: <a href="/reviewing-ai-output/">Why AI output still needs a human reader</a>.</li>
  <li>How to read the plans and reports an agent hands back: <a href="/reading-agent-output/">Reading what your agent hands back</a>.</li>
</ul>

<h2>Sources</h2>
<ul>
  <li>The failing test and its cause: <a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>.</li>
  <li>The fix and its independent verification: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>.</li>
  <li>Moving CI onto a MacBook Air, with run times: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>.</li>
  <li>The export engine's CI, with the history of its time limit in the comments: <a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>.</li>
  <li>The app's repository is private; the app details above come from its CI workflow and test scripts.</li>
</ul>
```

---

## zh-Hant

- **title**: `MarsDawn 怎麼測試：同一個測試，兩台 Mac · MarsDawn`
- **description**: `同一個測試，在一台 Mac 通過、在另一台失敗。產品沒壞，是測試讀到了螢幕的色彩。我們怎麼一層一層地測試，以及你也能照做的四個習慣。`

```html
<section class="intro">
  <h1>在一台 Mac 上通過的測試，不一定在測你以為的東西。</h1>
  <!-- src S11 -->
  <p>vibe coding 不是壞事。把想要的東西說出來、讓 agent 做出來，現在很多軟體都是這樣起頭的，MarsDawn 也是用 agent 開發的。但要讓人長期依賴的軟體，看的是第一版之後的事：多年的維護，以及安全。agent 一個晚上就能改幾十個檔案，那誰來確認它沒改壞？下面是一個讓我們看清楚「檢查」會怎麼出錯的測試，以及我們改了什麼。</p>
</section>

<div class="summary"><p><strong>同一個測試，在 Mac mini 上通過，在 MacBook Air 上失敗。產品沒壞。是測試透過螢幕的色彩描述檔在讀顏色，它在 Mac mini 上通過只是運氣好。換一台機器，抓到的是測試的 bug，不是程式的 bug。</strong></p></div>

<h2>只在 MacBook Air 上失敗的測試</h2>
<!-- src S4: kit PR #240（未合併）、run 40196953693 -->
<p>輸出引擎的測試，在 GitHub 的 macOS 15 機器上完整跑一次將近一小時：debug 版約 32 分鐘，release 版約 25 分鐘。為了縮短時間，我們開始把 macOS 26 那一半移到自己的 MacBook Air 上跑（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>）。</p>
<!-- src S1: kit #241、run 40271990387 -->
<p>在那台機器上第一次跑，就有一個測試失敗。這個測試會輸出一份帶有提示框（Note、Tip、Warning）的 PDF，檢查每個提示框邊上的色條顏色對不對，也就是色差要小於 0.16。在 MacBook Air 上，色差是 0.1634、0.1648 和 0.1796。換到 Mac mini，同一個 commit、同樣的 macOS 和 Xcode，測試通過。</p>
<p>我們第一個懷疑是輸出壞了。結果不是：PDF 本身沒問題，兩台機器不一樣的，是測試讀它的方式。</p>
<!-- src S1, S2: kit #241 -->
<p>這個測試會把 PDF 每一頁畫成圖片再讀像素，而 macOS 畫這張圖時，用的是主螢幕的色彩空間。Mac mini 接的是一般的外接螢幕，MacBook Air 用的是內建螢幕。我們拿一張填滿同一種橘色的圖片讀回來：(0.784, 0.278, 0.106) 在 Mac mini 上讀成 (0.822, 0.335, 0.179)，在 MacBook Air 上讀成 (0.782, 0.395, 0.221)。</p>
<!-- src S3: kit #242 驗證留言 -->
<p>重點在這裡：在 Mac mini 上，測試讀到的顏色其實也不對，最多差了 0.128，只是剛好落在 0.16 的上限內。它會通過，靠的是那台螢幕，不是因為它真的量對了色條。</p>
<!-- src S3, S10；{{TBD:mba-run}}＝自架 MacBook Air 的 run，來自 kit #240 -->
<p>修正（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>）只改測試：把頁面畫進一張固定使用 sRGB 色彩空間的圖片，完全不經過螢幕。現在兩台機器都能準確讀出色條的顏色：不論是 MacBook Air 的內建螢幕還是 Mac mini，最接近的色差都是 0.0。這個 pull request 的 CI 全部通過（<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>），MacBook Air 機器上的完整測試也通過了（run {{TBD:mba-run}}）。接著我們故意讓它失敗：把每個預期顏色都改成藍色，五個提示框全部變紅。</p>
<p>它還有一個已知的漏洞：Note 和 Caution 用的兩種橘色只差約 0.119，在 0.16 的上限內，所以這兩個顏色如果對調，測試多半不會發現。我們把這件事記了下來，沒有假裝這個測試已經完整。</p>
<p>一個不會失敗的測試，什麼也保護不了；因為錯的理由而失敗的測試（例如螢幕的色彩描述檔）也一樣。一台機器上的綠燈，只代表測試在那台機器上通過，不代表它測的就是名字上寫的那件事。</p>

<h2>紅燈和綠燈代表什麼</h2>
<!-- src S14 -->
<p>綠燈代表測試通過。但只有在你看過同一個測試，在它檢查的東西真的出錯時亮紅燈，這個綠燈才有意義。所以順序很重要：先故意弄壞，看它變紅；再改回來，看它變綠。這樣你才知道測試盯著的是對的地方。如果從來沒看過它變紅，綠燈可能只代表測試根本沒在看。</p>

<h2>測試是一層一層的網子</h2>
<p>沒有一個測試能抓到所有問題。每一層都是一張網目不同的網，從這一層漏掉的錯，應該要被下一層接住：</p>
<ul>
  <!-- src S6 -->
  <li><strong>單元測試</strong>，在輸出引擎裡（開源的 <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>，<code>marsdawn</code> 指令也用它）：抓某一段程式算錯答案。</li>
  <!-- src S13 -->
  <li><strong>參考 PDF：</strong>把一組樣本文件輸出成 PDF，每一頁的文字都和事先記錄的版本比對。抓內容悄悄不見，或頁數突然改變。</li>
  <!-- src S6, S9 -->
  <li><strong>不同的系統和版本：</strong>引擎在 macOS 15（支援的最舊版本）和 macOS 26（App 實際出貨的版本）上都要跑，各跑 debug 和 release 兩種版本。App 的完整測試則跑四種組合：簽章與不簽章，各自再分付費牆開與關。抓只在舊系統上壞掉，或只在使用者實際拿到的版本裡壞掉的問題。</li>
  <!-- src S4, S1 -->
  <li><strong>真的硬體：</strong>除了 GitHub 的機器，測試也在我們自己的 Mac 上跑，包括上面那台 MacBook Air。抓沒有螢幕的伺服器看不出來的問題。</li>
  <!-- src S12 -->
  <li><strong>紅燈對照組：</strong>App 的 CI 固定放著 11 份故意弄壞的清理腳本，每份都拿掉一道安全檢查，測試碰到每一份都必須失敗。只要有一份通過，壞掉的就是測試本身。</li>
  <!-- src S3, S15 -->
  <li><strong>另一雙眼睛：</strong>每個改動都由另一個 agent 驗證；功能動工前，也會先做情境審查，看大家實際會怎麼用。抓「說做完了其實沒做完」，以及程式能跑、卻用錯了場合。</li>
  <li><strong>最後由人合併。</strong>沒有任何改動是因為 agent 說「做完了」就進到主分支。</li>
</ul>

<h2>我們丟給它的東西</h2>
<p>網子好不好，要看丟進去的是什麼。下面是引擎測試會餵給它的幾種輸入，以及每個測試確保會發生的事：</p>
<ul>
  <!-- src S16 -->
  <li><strong>超大的檔案。</strong>2 MB 的文件要在一秒半內顯示完。5 MB、複雜到排不了版的文件照樣打得開，一秒內以純文字顯示。超過 16 MB 的檔案完全不解析，直接以文字顯示。</li>
  <!-- src S16 -->
  <li><strong>幾十萬行。</strong>大約 3 MB、每行只有一個字的文件，將近 80 萬行，讀到一半就會被判定太多，改以純文字顯示，不會把 App 卡住。</li>
  <!-- src S17 -->
  <li><strong>永遠不關的標記。</strong>1 MB 只開不關的區塊標記，或幾萬層互相包住的區塊，花的時間不能超過同樣 1 MB 純文字的兩倍左右。巢狀最多到八層。</li>
  <!-- src S18 -->
  <li><strong>數學公式。</strong>寫錯的公式就在原處顯示錯誤，不會讓整頁壞掉。超過一萬個字元的公式保留原樣；一份文件一次最多畫前 1,000 個；公式裡的內容也不會變成連結、圖片或網頁標籤。</li>
  <!-- src S19 -->
  <li><strong>藏在 Markdown 裡的惡意 HTML。</strong>指令碼會被移除，絕不執行；內嵌的框架在頁面顯示前就被拿掉。遠端圖片預設不載入，就算你允許，也只載入安全連線（HTTPS）的圖片。另有一份拿掉指令碼過濾的對照版本，測試碰到它必須失敗。</li>
  <!-- src S20 -->
  <li><strong>惡意的主題檔。</strong>會被拒絕，錯誤訊息也不會重複檔案裡隱藏的控制字元或連結。超過 16 KB 的主題檔直接不讀。</li>
</ul>
<!-- src S5 -->
<p>這些都有代價。引擎單次執行的時間上限從 30 分鐘拉到 45、50，再到 70 分鐘；macOS 15 還曾在測試全部通過的情況下，兩次撞到 50 分鐘的上限。</p>

<h2>你也能照做的四個習慣</h2>
<ol>
  <li><strong>寫的 agent 和驗的 agent 分開。</strong>只給驗證的那個改動本身和「怎樣才算完成」，不要給寫的人的說明，請它自己跑測試，並列出沒驗到的地方。驗 kit #242 時，驗證的 agent 先在 MacBook Air 上跑舊測試、親眼看它失敗，才讓新測試過關。這要多花一個 session 的 token，但比起事後修一個壞掉的改動，還是便宜。</li>
  <li><strong>每個測試都要看它失敗一次。</strong>相信綠燈之前，先把它守著的東西弄壞（或請 agent 弄壞），確認它會變紅。agent 很會寫出會通過的測試，正因為這樣，你才需要看到它失敗。</li>
  <li><strong>測試至少在第二個環境跑一次。</strong>沒有第二台 Mac 也沒關係，CI 裡跑兩個 OS 版本，或 debug 和 release 各跑一次，就是不錯的起點。要找的是那些靠運氣才通過的測試。</li>
  <!-- src S7, S8 -->
  <li><strong>「一個測試都沒跑」要算失敗。</strong>Python 3.9 的 <code>unittest</code> 一個測試都沒找到時，還是會回報成功，所以路徑打錯一個字，你照樣拿到綠燈。我們的 CI 會讀測試數量，是 0 就失敗，也會檢查摘要寫的是「0 failed」，不只看結束代碼。agent 回報「測試全部通過」，其實一個都沒跑，是最常見的假完成之一。</li>
</ol>

<h2>一句話</h2>
<!-- src S11 -->
<p>一個 App 是不是 vibe coding 做的，沒那麼重要；重要的是有沒有人持續在測試、在維護。選軟體的時候值得看一眼：它有沒有說明自己怎麼測試？最近一次更新是什麼時候？</p>
<p>速度交給 agent，把關留給真的量對東西的測試，以及讀過結果的人。</p>

<h2>接下來</h2>
<ul>
  <li>為什麼 agent 寫的東西還是要有人讀過：<a href="/zh-hant/reviewing-ai-output/">為什麼 AI 寫的東西還是需要人讀過</a>。</li>
  <li>怎麼讀 agent 交回來的計畫和報告：<a href="/zh-hant/reading-agent-output/">讀懂 agent 交回來的 Markdown</a>。</li>
</ul>

<h2>資料來源</h2>
<ul>
  <li>失敗的測試和原因：<a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>。</li>
  <li>修正和獨立驗證：<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>。</li>
  <li>把 CI 移到 MacBook Air，附執行時間：<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>。</li>
  <li>輸出引擎的 CI，時間上限的調整歷史寫在註解裡：<a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>。</li>
  <li>App 的程式碼庫不公開；上面關於 App 的內容，來自它的 CI 設定和測試腳本。</li>
</ul>
```

---

## zh-Hans

- **title**: `MarsDawn 怎么测试：同一个测试，两台 Mac · MarsDawn`
- **description**: `同一个测试，在一台 Mac 上通过，在另一台上失败。产品没坏，是测试读到了屏幕的色彩。我们怎么一层一层地测试，以及你也能照做的四个习惯。`

```html
<section class="intro">
  <h1>在一台 Mac 上通过的测试，不一定在测你以为的东西。</h1>
  <!-- src S11 -->
  <p>vibe coding 不是坏事。把想要的东西说出来、让代理做出来，现在很多软件都是这样起步的，MarsDawn 也是用代理开发的。但让人长期依赖的软件，看的是第一版之后的事：多年的维护，以及安全。代理一个晚上就能改几十个文件，那谁来确认它没改坏？下面是一个让我们看清“检查”会怎么出错的测试，以及我们改了什么。</p>
</section>

<div class="summary"><p><strong>同一个测试，在 Mac mini 上通过，在 MacBook Air 上失败。产品没坏。是测试通过屏幕的颜色描述文件在读颜色，它在 Mac mini 上通过只是运气好。换一台机器，抓到的是测试的 bug，不是代码的 bug。</strong></p></div>

<h2>只在 MacBook Air 上失败的测试</h2>
<!-- src S4: kit PR #240 (not merged), run 40196953693 -->
<p>导出引擎的测试，在 GitHub 的 macOS 15 机器上完整跑一次将近一小时：debug 版约 32 分钟，release 版约 25 分钟。为了缩短时间，我们开始把 macOS 26 那一半移到自己的 MacBook Air 上跑（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>）。</p>
<!-- src S1: kit #241, run 40271990387 -->
<p>在那台机器上第一次跑，就有一个测试失败。这个测试会导出一份带提示框（Note、Tip、Warning）的 PDF，检查每个提示框边上的色条颜色对不对，也就是色差要小于 0.16。在 MacBook Air 上，色差是 0.1634、0.1648 和 0.1796。换到 Mac mini，同一个 commit、同样的 macOS 和 Xcode，测试通过。</p>
<p>我们第一个怀疑是导出坏了。结果不是：PDF 本身没问题，两台机器不一样的，是测试读它的方式。</p>
<!-- src S1, S2: kit #241 -->
<p>这个测试会把 PDF 每一页画成图像再读像素，而 macOS 画这张图时，用的是主显示器的色彩空间。Mac mini 接的是普通的外接显示器，MacBook Air 用的是内建显示屏。我们拿一张填满同一种橙色的图像读回来：(0.784, 0.278, 0.106) 在 Mac mini 上读成 (0.822, 0.335, 0.179)，在 MacBook Air 上读成 (0.782, 0.395, 0.221)。</p>
<!-- src S3: kit #242 verification comment -->
<p>关键在这里：在 Mac mini 上，测试读到的颜色其实也不对，最多差了 0.128，只是刚好落在 0.16 的上限内。它能通过，靠的是那台显示器，而不是真的量对了色条。</p>
<!-- src S3, S10; {{TBD:mba-run}} = the self-hosted MacBook Air run, from kit #240 -->
<p>修复（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>）只改测试：把页面画进一张固定使用 sRGB 色彩空间的图像，完全不经过屏幕。现在两台机器都能准确读出色条的颜色：无论是 MacBook Air 的内建显示屏还是 Mac mini，最接近的色差都是 0.0。这个 pull request 的 CI 全部通过（<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>），MacBook Air 机器上的完整测试也通过了（run {{TBD:mba-run}}）。接着我们故意让它失败：把每个预期颜色都改成蓝色，五个提示框全部变红。</p>
<p>它还有一个已知的漏洞：Note 和 Caution 用的两种橙色只差约 0.119，在 0.16 的上限内，所以这两个颜色如果对调，测试多半发现不了。我们把这件事记了下来，没有假装这个测试已经完整。</p>
<p>一个不会失败的测试，什么也保护不了；因为错误的理由而失败的测试（比如屏幕的颜色描述文件）也一样。一台机器上的绿灯，只说明测试在那台机器上通过，不说明它测的就是名字上写的那件事。</p>

<h2>红灯和绿灯代表什么</h2>
<!-- src S14 -->
<p>绿灯代表测试通过。但只有在你见过同一个测试在它检查的东西真的出错时亮红灯，这个绿灯才有意义。所以顺序很重要：先故意弄坏，看它变红；再改回来，看它变绿。这样你才知道测试盯着的是对的地方。如果从来没见过它变红，绿灯可能只说明测试根本没在看。</p>

<h2>测试是一层一层的网</h2>
<p>没有哪个测试能抓到所有问题。每一层都是一张网眼不同的网，从这一层漏掉的错，应该被下一层接住：</p>
<ul>
  <!-- src S6 -->
  <li><strong>单元测试</strong>，在导出引擎里（开源的 <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>，<code>marsdawn</code> 命令也用它）：抓某段代码算错答案。</li>
  <!-- src S13 -->
  <li><strong>参考 PDF：</strong>把一组样本文稿导出成 PDF，每一页的文字都和事先记录的版本比对。抓内容悄悄丢失，或页数突然改变。</li>
  <!-- src S6, S9 -->
  <li><strong>不同的系统和版本：</strong>引擎在 macOS 15（支持的最低版本）和 macOS 26（App 实际发布的版本）上都要跑，各跑 debug 和 release 两种版本。App 的完整测试则跑四种组合：签名与不签名，各自再分付费墙开与关。抓只在旧系统上出错，或只在用户实际拿到的版本里出错的问题。</li>
  <!-- src S4, S1 -->
  <li><strong>真实硬件：</strong>除了 GitHub 的机器，测试也在我们自己的 Mac 上跑，包括上面那台 MacBook Air。抓没有屏幕的服务器看不出来的问题。</li>
  <!-- src S12 -->
  <li><strong>红灯对照组：</strong>App 的 CI 固定放着 11 份故意弄坏的清理脚本，每份都去掉一道安全检查，测试碰到每一份都必须失败。只要有一份通过，坏掉的就是测试本身。</li>
  <!-- src S3, S15 -->
  <li><strong>另一双眼睛：</strong>每个改动都由另一个代理验证；功能动工前，还会先做情境审查，看大家实际会怎么用。抓“说做完了其实没做完”，以及代码能跑、却用错了场合。</li>
  <li><strong>最后由人合并。</strong>没有任何改动是因为代理说“做完了”就进入主分支。</li>
</ul>

<h2>我们丢给它的东西</h2>
<p>网好不好，要看丢进去的是什么。下面是引擎测试会喂给它的几种输入，以及每个测试确保会发生的事：</p>
<ul>
  <!-- src S16 -->
  <li><strong>超大的文件。</strong>2 MB 的文稿要在一秒半内显示完。5 MB、复杂到排不了版的文稿照样能打开，一秒内以纯文本显示。超过 16 MB 的文件完全不解析，直接以文本显示。</li>
  <!-- src S16 -->
  <li><strong>几十万行。</strong>大约 3 MB、每行只有一个词的文稿，将近 80 万行，读到一半就会被判定太多，改以纯文本显示，不会把 App 卡住。</li>
  <!-- src S17 -->
  <li><strong>永远不闭合的标记。</strong>1 MB 只开不关的区块标记，或几万层互相嵌套的区块，花的时间不能超过同样 1 MB 纯文本的两倍左右。嵌套最多到八层。</li>
  <!-- src S18 -->
  <li><strong>数学公式。</strong>写错的公式就在原处显示错误，不会让整页坏掉。超过一万个字符的公式保留原样；一份文稿一次最多渲染前 1,000 个；公式里的内容也不会变成链接、图像或网页标签。</li>
  <!-- src S19 -->
  <li><strong>藏在 Markdown 里的恶意 HTML。</strong>脚本会被移除，绝不执行；嵌入的框架在页面显示前就被拿掉。远程图像默认不加载，即使你允许，也只加载安全连接（HTTPS）的图像。另有一份去掉脚本过滤的对照版本，测试碰到它必须失败。</li>
  <!-- src S20 -->
  <li><strong>恶意的主题文件。</strong>会被拒绝，错误信息也不会重复文件里隐藏的控制字符或链接。超过 16 KB 的主题文件直接不读。</li>
</ul>
<!-- src S5 -->
<p>这些都有代价。引擎单次运行的时间上限从 30 分钟拉到 45、50，再到 70 分钟；macOS 15 还曾在测试全部通过的情况下，两次撞上 50 分钟的上限。</p>

<h2>你也能照做的四个习惯</h2>
<ol>
  <li><strong>写的代理和验的代理分开。</strong>只给验证的那个改动本身和“怎样才算完成”，不要给写的那个的说明，请它自己跑测试，并列出没验到的地方。验 kit #242 时，验证的代理先在 MacBook Air 上跑旧测试、亲眼看它失败，才让新测试过关。这要多花一个会话的 token，但比起事后修一个改坏的改动，还是便宜。</li>
  <li><strong>每个测试都要看它失败一次。</strong>相信绿灯之前，先把它守着的东西弄坏（或请代理弄坏），确认它会变红。代理很会写出能通过的测试，正因为这样，你才需要看到它失败。</li>
  <li><strong>测试至少在第二个环境跑一次。</strong>没有第二台 Mac 也没关系，CI 里跑两个系统版本，或 debug 和 release 各跑一次，就是不错的起点。要找的是那些靠运气才通过的测试。</li>
  <!-- src S7, S8 -->
  <li><strong>“一个测试都没跑”要算失败。</strong>Python 3.9 的 <code>unittest</code> 一个测试都没找到时，还是会报告成功，所以路径打错一个字，你照样拿到绿灯。我们的 CI 会读测试数量，是 0 就失败，也会检查摘要写的是“0 failed”，不只看退出码。代理报告“测试全部通过”，其实一个都没跑，是最常见的假完成之一。</li>
</ol>

<h2>一句话</h2>
<!-- src S11 -->
<p>一个 App 是不是 vibe coding 做的，没那么重要；重要的是有没有人持续在测试、在维护。选软件的时候值得看一眼：它有没有说明自己怎么测试？最近一次更新是什么时候？</p>
<p>速度交给代理，把关留给真正量对东西的测试，以及读过结果的人。</p>

<h2>接下来</h2>
<ul>
  <li>为什么代理写的东西还是要有人读过：<a href="/zh-hans/reviewing-ai-output/">为什么 AI 写的东西还是需要人读过</a>。</li>
  <li>怎么读代理交回来的计划和报告：<a href="/zh-hans/reading-agent-output/">读懂代理交回来的 Markdown</a>。</li>
</ul>

<h2>资料来源</h2>
<ul>
  <li>失败的测试和原因：<a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>。</li>
  <li>修复和独立验证：<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>。</li>
  <li>把 CI 移到 MacBook Air，附运行时间：<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>。</li>
  <li>导出引擎的 CI，时间上限的调整历史写在注释里：<a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>。</li>
  <li>App 的代码仓库不公开；上面关于 App 的内容，来自它的 CI 配置和测试脚本。</li>
</ul>
```

---

## ja

- **title**: `MarsDawn のテストのしかた：ひとつのテスト、2 台の Mac · MarsDawn`
- **description**: `あるテストが 1 台の Mac では通り、もう 1 台では失敗しました。製品は壊れておらず、テストが画面の色を読んでいたのです。テストを何層にも重ねるやり方と、まねできる 4 つの習慣。`

```html
<section class="intro">
  <h1>ある Mac で通るテストが、思っているものをテストしているとは限りません。</h1>
  <!-- src S11 -->
  <p>バイブコーディング（vibe coding）は悪いことではありません。ほしいものを言葉で伝えて、エージェントに作ってもらう。いまは多くのソフトウェアがそうやって始まり、MarsDawn もエージェントと一緒に作っています。ただ、人が長く頼るソフトウェアは、最初のバージョンのあとで評価されます。何年にもわたるメンテナンスと、安全を保ち続けることです。エージェントはひと晩で何十ものファイルを変更できます。では、何も壊していないことを誰が確かめるのでしょうか。ここでは、その確認がどう失敗するかを教えてくれたひとつのテストと、私たちが変えたことを紹介します。</p>
</section>

<div class="summary"><p><strong>あるテストが Mac mini では通り、MacBook Air では失敗しました。製品に問題はありませんでした。テストが画面のカラープロファイルを通して色を読んでいて、Mac mini で通っていたのはたまたまでした。2 台目のマシンが見つけたのは、コードではなくテストのバグです。</strong></p></div>

<h2>MacBook Air でだけ失敗したテスト</h2>
<!-- src S4: kit PR #240 (not merged), run 40196953693 -->
<p>書き出しエンジンのテストを GitHub の macOS 15 ランナーで一通り実行すると、1 時間近くかかります。debug ビルドで約 32 分、release ビルドで約 25 分です。これを短くするため、macOS 26 の分を自前の MacBook Air に移し始めました（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>）。</p>
<!-- src S1: kit #241, run 40271990387 -->
<p>そこでの最初の実行で、テストがひとつ失敗しました。コールアウト（Note、Tip、Warning）を含む PDF を書き出し、それぞれの端にある色の帯が正しい色か、つまり色差が 0.16 未満かを確かめるテストです。MacBook Air での色差は 0.1634、0.1648、0.1796 でした。Mac mini では、同じコミット、同じ macOS と Xcode で、テストは通りました。</p>
<p>最初は書き出しが壊れたのだと思いました。違いました。PDF には何の問題もなく、2 台で違っていたのは、テストがそれを読む方法でした。</p>
<!-- src S1, S2: kit #241 -->
<p>このテストは PDF の各ページを画像にしてピクセルを読みます。macOS はその画像を、メインディスプレイのカラースペースで描きます。Mac mini はふつうの外部ディスプレイにつながっていて、MacBook Air は内蔵ディスプレイを使っていました。1 色のオレンジで塗りつぶした画像を読み戻すと、(0.784, 0.278, 0.106) が Mac mini では (0.822, 0.335, 0.179)、MacBook Air では (0.782, 0.395, 0.221) になりました。</p>
<!-- src S3: kit #242 verification comment -->
<p>大事なのはここからです。Mac mini でも、テストは正しい色を読めていませんでした。ずれは最大 0.128 で、0.16 の上限にぎりぎり収まっていただけです。通っていたのはディスプレイのおかげで、帯の色を正しく測れていたからではありません。</p>
<!-- src S3, S10; {{TBD:mba-run}} = the self-hosted MacBook Air run, from kit #240 -->
<p>修正（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>）で変えたのはテストだけです。ページを sRGB に固定したカラースペースの画像に描くので、画面はまったく関わりません。いまは 2 台とも帯の色を正確に読めます。いちばん近い色差は、MacBook Air の内蔵ディスプレイでも Mac mini でも 0.0 です。プルリクエストの CI は通り（<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>）、MacBook Air のランナーでの全テストも通りました（run {{TBD:mba-run}}）。そのあと、わざと失敗させました。期待する色をすべて青にすると、5 つのコールアウトすべてで赤になりました。</p>
<p>既知の穴もまだあります。Note と Caution は色差が約 0.119 の 2 つのオレンジを使っていて、0.16 の上限より内側です。この 2 色が入れ替わっても、テストはおそらく気づきません。テストが完全なふりはせず、このことを記録に残しました。</p>
<p>失敗しようのないテストは何も守りません。画面のカラープロファイルのような、間違った理由で失敗するテストも同じです。1 台のマシンでの緑は、そこでテストが通ったことを示すだけで、名前どおりのものを測っているという意味ではありません。</p>

<h2>赤と緑が意味すること</h2>
<!-- src S14 -->
<p>緑はテストが通ったという意味です。それに価値があるのは、確かめている対象が本当に間違っているときに、同じテストが赤になるのを見たことがある場合だけです。だから順番が大切です。わざと壊して赤になるのを見る。元に戻して緑になるのを見る。そうして初めて、テストが正しいところを見ているとわかります。赤を一度も見ていないなら、その緑はテストが何も見ていないだけかもしれません。</p>

<h2>テストは何層にも重ねた網</h2>
<p>すべてを捕まえるテストはひとつもありません。層ごとに網目の違う網があり、ひとつをすり抜けた間違いは次の網にかかるはずです。</p>
<ul>
  <!-- src S6 -->
  <li><strong>単体テスト</strong>：書き出しエンジン（オープンソースの <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>。<code>marsdawn</code> コマンドもこれで動いています）の中にあります。コードの一部が間違った答えを返すことを捕まえます。</li>
  <!-- src S13 -->
  <li><strong>参照 PDF：</strong>サンプルの書類を書き出し、各ページのテキストを記録済みのものと比べます。内容が知らないうちに消えることや、ページ数が変わることを捕まえます。</li>
  <!-- src S6, S9 -->
  <li><strong>異なるシステムとビルド：</strong>エンジンは、サポートする最も古い macOS 15 と、アプリを出荷している macOS 26 の両方で、それぞれ debug と release のビルドとして実行します。アプリの全テストは 4 通りの組み合わせで実行します。署名ありと署名なし、それぞれペイウォールのオフとオンです。古いシステムでだけ、あるいはお客さまが実際に受け取るビルドでだけ壊れるものを捕まえます。</li>
  <!-- src S4, S1 -->
  <li><strong>実機：</strong>GitHub のマシンに加えて、上の MacBook Air を含む自前の Mac でもテストを実行します。画面のないサーバーでは見えないものを捕まえます。</li>
  <!-- src S12 -->
  <li><strong>赤になるべき対照群：</strong>アプリの CI には、わざと壊したクリーンアップスクリプトのコピーが 11 個あり、それぞれ安全チェックがひとつずつ抜いてあります。テストはそのすべてで失敗しなければなりません。ひとつでも通れば、壊れているのはテストのほうです。</li>
  <!-- src S3, S15 -->
  <li><strong>もうひとつの目：</strong>変更はそれぞれ別のエージェントが検証し、機能を作る前には、人が実際にどう使うかをシナリオレビューで確かめます。「完了」と言いながら終わっていないことや、動くけれど使われる場面を間違えているコードを捕まえます。</li>
  <li><strong>マージするのは人です。</strong>エージェントが終わったと言ったからといって、変更がメインブランチに入ることはありません。</li>
</ul>

<h2>テストに投げ込むもの</h2>
<p>網が役に立つかどうかは、何を投げ込むかで決まります。エンジンのテストが与える入力の一部と、それぞれのテストが保証することです。</p>
<ul>
  <!-- src S16 -->
  <li><strong>とても大きなファイル。</strong>2 MB の書類は 1.5 秒以内に表示されます。レイアウトしきれないほど複雑な 5 MB の書類も、1 秒以内にプレーンテキストとして開きます。16 MB を超えるものは、まったく解析せずにテキストとして表示します。</li>
  <!-- src S16 -->
  <li><strong>何十万もの行。</strong>1 行 1 語で約 3 MB、80 万行近い書類は、読んでいる途中で多すぎると判断され、アプリを止めずにプレーンテキストとして表示されます。</li>
  <!-- src S17 -->
  <li><strong>閉じない記号。</strong>閉じのないブロックの開始記号が 1 MB 分あっても、何万層にも入れ子になったブロックでも、同じ 1 MB のプレーンテキストのおよそ 2 倍より長くかかってはいけません。入れ子は 8 階層で止まります。</li>
  <!-- src S18 -->
  <li><strong>数式。</strong>間違った数式は、ページを壊さずにその場所にエラーを表示します。10,000 文字を超える数式は書かれたまま残し、一度に描くのは書類の最初の 1,000 個までです。数式の中身がリンクや画像、ページのマークアップになることはありません。</li>
  <!-- src S19 -->
  <li><strong>Markdown に紛れ込んだ悪意のある HTML。</strong>スクリプトは取り除かれ、実行されることはありません。埋め込みフレームも、ページに表示される前に取り除かれます。リモート画像は許可しないかぎり読み込まず、許可しても安全な（HTTPS の）ものだけを読み込みます。スクリプトのフィルタを外した対照用のコピーもあり、テストはそこで失敗しなければなりません。</li>
  <!-- src S20 -->
  <li><strong>悪意のあるテーマファイル。</strong>拒否され、エラーメッセージがファイル内の隠れた制御文字やリンクを繰り返すこともありません。16 KB を超えるテーマファイルは読み込みもしません。</li>
</ul>
<!-- src S5 -->
<p>どれもただではありません。エンジン 1 回分の制限時間は 30 分から 45 分、50 分、70 分と延び、macOS 15 は全テストが通っていたのに 50 分の上限に 2 回達したことがあります。</p>

<h2>まねできる 4 つの習慣</h2>
<ol>
  <li><strong>書くエージェントと確かめるエージェントを分ける。</strong>確かめる側には、書いた側の説明ではなく、変更そのものと「完了」の条件を渡し、テストを自分で実行して、確かめなかったことを挙げてもらいます。kit #242 では、検証したエージェントが新しいテストを通す前に、MacBook Air で古いテストを実行して失敗するのを確かめました。2 つ目のセッションのトークン代はかかりますが、壊れた変更をあとで直すよりは安上がりです。</li>
  <li><strong>どのテストも一度は失敗するのを見る。</strong>緑を信じる前に、そのテストが守っているものを壊して（またはエージェントに壊してもらって）、赤になることを確かめます。エージェントは通るテストを書くのが得意です。だからこそ、失敗するところを見る必要があります。</li>
  <li><strong>テストを 2 つ目の環境で実行する。</strong>2 台目の Mac がなくてもかまいません。2 つの OS バージョン、あるいは debug ビルドと release ビルドの CI マトリクスで十分なスタートです。探すのは、偶然に通っているだけのテストです。</li>
  <!-- src S7, S8 -->
  <li><strong>「テストが 1 つも実行されなかった」を失敗として扱う。</strong>Python 3.9 の <code>unittest</code> は、テストが 1 つも見つからなくても成功として終了します。パスを 1 文字打ち間違えただけで緑になるわけです。私たちの CI はテストの数を読んで 0 なら失敗にし、終了コードだけでなく、まとめに「0 failed」と書かれていることも確かめます。何も実行していないのにエージェントが「すべてのテストが通りました」と報告するのは、いちばんよくある見せかけの完了のひとつです。</li>
</ol>

<h2>まとめ</h2>
<!-- src S11 -->
<p>アプリがバイブコーディングで作られたかどうかより、誰かがテストとメンテナンスを続けているかどうかのほうが大事です。ソフトウェアを選ぶときに確かめる価値があります。テストのしかたを説明しているか。最後に更新されたのはいつか。</p>
<p>速さはエージェントに任せましょう。確認は、正しいものを測るテストと、結果を読む人に任せます。</p>

<h2>次に</h2>
<ul>
  <li>エージェントが書いたものを、それでも人が読まなければならない理由：<a href="/ja/reviewing-ai-output/">AI の出力を人が確認する理由</a>。</li>
  <li>エージェントが返してくる計画やレポートの読み方：<a href="/ja/reading-agent-output/">エージェントが返してくるものを読む</a>。</li>
</ul>

<h2>出典</h2>
<ul>
  <li>失敗したテストとその原因：<a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>。</li>
  <li>修正と独立した検証：<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>。</li>
  <li>CI を MacBook Air に移す作業と実行時間：<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>。</li>
  <li>書き出しエンジンの CI。制限時間の変遷はコメントにあります：<a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>。</li>
  <li>アプリのリポジトリは非公開です。上のアプリに関する内容は、その CI ワークフローとテストスクリプトにもとづいています。</li>
</ul>
```

---

## ko

- **title**: `MarsDawn을 테스트하는 방법: 테스트 하나, Mac 두 대 · MarsDawn`
- **description**: `한 Mac에서 통과한 테스트가 다른 Mac에서는 실패했습니다. 제품은 멀쩡했고, 테스트가 화면의 색을 읽고 있었습니다. 테스트를 여러 겹으로 쌓는 방법과 따라 할 수 있는 네 가지 습관.`

```html
<section class="intro">
  <h1>한 Mac에서 통과한 테스트가 생각하는 것을 테스트하고 있다는 보장은 없습니다.</h1>
  <!-- src S11 -->
  <p>바이브 코딩(vibe coding)은 나쁜 것이 아닙니다. 원하는 것을 말로 설명하고 에이전트가 만들게 하는 것. 요즘 많은 소프트웨어가 그렇게 시작하고, MarsDawn도 에이전트와 함께 만듭니다. 하지만 사람들이 오래 의지하는 소프트웨어는 첫 버전 이후로 평가받습니다. 몇 년에 걸친 유지보수, 그리고 보안을 지켜 가는 일입니다. 에이전트는 하룻저녁에 파일 수십 개를 바꿀 수 있습니다. 그렇다면 아무것도 망가지지 않았는지는 누가 확인할까요? 그 확인이 어떻게 어긋나는지 보여 준 테스트 하나와, 우리가 바꾼 것을 소개합니다.</p>
</section>

<div class="summary"><p><strong>한 테스트가 Mac mini에서는 통과하고 MacBook Air에서는 실패했습니다. 제품에는 문제가 없었습니다. 테스트가 화면의 색상 프로파일을 거쳐 색을 읽고 있었고, Mac mini에서 통과한 것은 운이 좋았을 뿐입니다. 두 번째 기기가 찾아낸 것은 코드가 아니라 테스트의 버그였습니다.</strong></p></div>

<h2>MacBook Air에서만 실패한 테스트</h2>
<!-- src S4: kit PR #240 (not merged), run 40196953693 -->
<p>내보내기 엔진의 테스트를 GitHub의 macOS 15 러너에서 전부 돌리면 거의 한 시간이 걸립니다. debug 빌드가 약 32분, release 빌드가 약 25분입니다. 이 시간을 줄이려고 macOS 26 쪽을 우리 MacBook Air로 옮기기 시작했습니다(<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>).</p>
<!-- src S1: kit #241, run 40271990387 -->
<p>그곳에서 처음 돌렸을 때 테스트 하나가 실패했습니다. 콜아웃(Note, Tip, Warning)이 들어간 PDF를 내보내고, 각 콜아웃 가장자리의 색 막대가 올바른 색인지, 즉 색 차이가 0.16 미만인지 확인하는 테스트입니다. MacBook Air에서 색 차이는 0.1634, 0.1648, 0.1796이었습니다. Mac mini에서는 같은 커밋, 같은 macOS와 Xcode로 테스트가 통과했습니다.</p>
<p>처음에는 내보내기가 망가졌다고 생각했습니다. 아니었습니다. PDF에는 아무 문제가 없었고, 두 기기에서 달랐던 것은 테스트가 그것을 읽는 방식이었습니다.</p>
<!-- src S1, S2: kit #241 -->
<p>이 테스트는 PDF의 각 페이지를 이미지로 바꿔 픽셀을 읽는데, macOS는 그 이미지를 주 디스플레이의 색 공간으로 그립니다. Mac mini는 평범한 외장 모니터에 연결되어 있었고, MacBook Air는 내장 디스플레이를 쓰고 있었습니다. 주황색 한 가지로 채운 이미지를 다시 읽어 보니, (0.784, 0.278, 0.106)이 Mac mini에서는 (0.822, 0.335, 0.179), MacBook Air에서는 (0.782, 0.395, 0.221)로 돌아왔습니다.</p>
<!-- src S3: kit #242 verification comment -->
<p>중요한 건 여기부터입니다. Mac mini에서도 테스트는 올바른 색을 읽지 못하고 있었습니다. 최대 0.128까지 어긋나 있었고, 0.16 한도 안에 겨우 들어왔을 뿐입니다. 통과한 건 모니터 덕분이지, 막대를 제대로 측정해서가 아니었습니다.</p>
<!-- src S3, S10; {{TBD:mba-run}} = the self-hosted MacBook Air run, from kit #240 -->
<p>수정(<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>)은 테스트만 바꿉니다. 페이지를 sRGB로 고정한 색 공간의 이미지에 그리기 때문에 화면이 전혀 끼어들지 않습니다. 이제 두 기기 모두 막대 색을 정확하게 읽습니다. 가장 가까운 색 차이는 MacBook Air의 내장 디스플레이에서도, Mac mini에서도 0.0입니다. 풀 리퀘스트의 CI가 통과했고(<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>), MacBook Air 러너에서 전체 테스트도 통과했습니다(run {{TBD:mba-run}}). 그다음 일부러 실패시켰습니다. 기대하는 색을 모두 파란색으로 바꾸자 콜아웃 다섯 개 모두에서 빨간불이 들어왔습니다.</p>
<p>알려진 빈틈도 아직 있습니다. Note와 Caution은 색 차이가 약 0.119인 두 주황색을 쓰는데, 0.16 한도 안쪽입니다. 그래서 두 색이 서로 바뀌어도 테스트는 아마 알아차리지 못할 것입니다. 테스트가 완벽한 척하지 않고 이 사실을 기록해 두었습니다.</p>
<p>실패할 수 없는 테스트는 아무것도 지켜 주지 못합니다. 화면의 색상 프로파일처럼 엉뚱한 이유로 실패하는 테스트도 마찬가지입니다. 한 기기에서의 초록불은 테스트가 거기서 통과했다는 뜻일 뿐, 이름에 적힌 것을 측정한다는 뜻은 아닙니다.</p>

<h2>빨간불과 초록불이 뜻하는 것</h2>
<!-- src S14 -->
<p>초록불은 테스트가 통과했다는 뜻입니다. 그것이 의미가 있으려면, 확인하는 대상이 정말로 잘못됐을 때 같은 테스트가 빨간불로 바뀌는 것을 본 적이 있어야 합니다. 그래서 순서가 중요합니다. 일부러 망가뜨려 빨간불을 보고, 되돌려 초록불을 봅니다. 그래야 테스트가 올바른 곳을 보고 있다는 걸 알 수 있습니다. 빨간불을 한 번도 보지 못했다면, 그 초록불은 테스트가 아무것도 보고 있지 않다는 뜻일 수도 있습니다.</p>

<h2>테스트는 여러 겹의 그물입니다</h2>
<p>모든 것을 잡아내는 테스트는 없습니다. 겹마다 그물코가 다른 그물이 있고, 한 그물을 빠져나간 실수는 다음 그물에 걸려야 합니다.</p>
<ul>
  <!-- src S6 -->
  <li><strong>단위 테스트</strong>: 내보내기 엔진(오픈 소스인 <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>, <code>marsdawn</code> 명령도 이것으로 돌아갑니다) 안에 있습니다. 코드 일부가 틀린 답을 내는 것을 잡아냅니다.</li>
  <!-- src S13 -->
  <li><strong>기준 PDF:</strong> 샘플 문서를 내보내고 페이지마다 텍스트를 기록해 둔 사본과 비교합니다. 내용이 조용히 사라지거나 페이지 수가 바뀌는 것을 잡아냅니다.</li>
  <!-- src S6, S9 -->
  <li><strong>다른 시스템과 빌드:</strong> 엔진은 지원하는 가장 오래된 버전인 macOS 15와, 앱이 출시되는 macOS 26에서 각각 debug와 release 빌드로 돌아갑니다. 앱의 전체 테스트는 네 가지 조합으로 돕니다. 서명한 것과 서명하지 않은 것, 각각 페이월을 끈 것과 켠 것입니다. 오래된 시스템에서만, 또는 고객이 실제로 받는 빌드에서만 망가지는 것을 잡아냅니다.</li>
  <!-- src S4, S1 -->
  <li><strong>실제 하드웨어:</strong> GitHub의 기기 말고도 위의 MacBook Air를 포함한 우리 Mac에서 테스트를 돌립니다. 화면 없는 서버에서는 보이지 않는 것을 잡아냅니다.</li>
  <!-- src S12 -->
  <li><strong>빨간불 대조군:</strong> 앱의 CI에는 일부러 망가뜨린 정리 스크립트 사본 11개가 있고, 사본마다 안전 검사가 하나씩 빠져 있습니다. 테스트는 그 모두에서 실패해야 합니다. 하나라도 통과하면 망가진 것은 테스트입니다.</li>
  <!-- src S3, S15 -->
  <li><strong>또 하나의 눈:</strong> 변경마다 다른 에이전트가 검증하고, 기능을 만들기 전에는 시나리오 리뷰로 사람들이 실제로 어떻게 쓸지 확인합니다. 끝났다고 했지만 끝나지 않은 것, 그리고 동작은 하지만 잘못된 상황에 쓰인 코드를 잡아냅니다.</li>
  <li><strong>병합은 사람이 합니다.</strong> 에이전트가 끝났다고 말했다는 이유로 메인 브랜치에 들어가는 변경은 없습니다.</li>
</ul>

<h2>테스트에 던져 넣는 것들</h2>
<p>그물이 얼마나 쓸모 있는지는 무엇을 던져 넣느냐에 달려 있습니다. 엔진 테스트가 넣는 입력 몇 가지와, 각 테스트가 보장하는 것입니다.</p>
<ul>
  <!-- src S16 -->
  <li><strong>아주 큰 파일.</strong> 2MB 문서는 1.5초 안에 표시됩니다. 레이아웃하기에 너무 복잡한 5MB 문서도 1초 안에 일반 텍스트로 열립니다. 16MB가 넘는 것은 아예 파싱하지 않고 텍스트로 보여 줍니다.</li>
  <!-- src S16 -->
  <li><strong>수십만 줄.</strong> 한 줄에 한 단어씩, 약 3MB에 80만 줄 가까운 문서는 읽는 도중에 너무 많다고 판단되어, 앱을 붙잡아 두지 않고 일반 텍스트로 표시됩니다.</li>
  <!-- src S17 -->
  <li><strong>닫히지 않는 표시.</strong> 닫는 짝이 없는 블록 시작 표시 1MB, 또는 수만 겹으로 중첩된 블록도 같은 1MB 일반 텍스트의 약 두 배보다 오래 걸리면 안 됩니다. 중첩은 8단계에서 멈춥니다.</li>
  <!-- src S18 -->
  <li><strong>수식.</strong> 잘못된 수식은 페이지를 망가뜨리지 않고 그 자리에 오류를 표시합니다. 10,000자가 넘는 수식은 쓴 그대로 두고, 한 번에 문서의 처음 1,000개까지만 그립니다. 수식 안의 내용이 링크나 이미지, 페이지 마크업이 되는 일은 없습니다.</li>
  <!-- src S19 -->
  <li><strong>Markdown 속에 숨은 악의적인 HTML.</strong> 스크립트는 제거되어 절대 실행되지 않고, 삽입된 프레임도 페이지에 보이기 전에 제거됩니다. 원격 이미지는 허용하지 않는 한 불러오지 않으며, 허용해도 안전한(HTTPS) 이미지만 불러옵니다. 스크립트 필터를 뺀 대조용 사본도 있어서, 테스트는 그 사본에서 실패해야 합니다.</li>
  <!-- src S20 -->
  <li><strong>악의적인 테마 파일.</strong> 거부되며, 오류 메시지가 파일 속 숨은 제어 문자나 링크를 그대로 되풀이하지도 않습니다. 16KB가 넘는 테마 파일은 아예 읽지 않습니다.</li>
</ul>
<!-- src S5 -->
<p>이 모든 것에는 비용이 듭니다. 엔진 한 번 실행의 제한 시간은 30분에서 45분, 50분, 70분으로 늘었고, macOS 15는 모든 테스트가 통과했는데도 50분 한도에 두 번 걸린 적이 있습니다.</p>

<h2>따라 할 수 있는 네 가지 습관</h2>
<ol>
  <li><strong>작성하는 에이전트와 확인하는 에이전트를 나누세요.</strong> 확인하는 쪽에는 작성한 쪽의 설명이 아니라 변경 자체와 '완료'의 기준을 주고, 테스트를 직접 돌려 확인하지 않은 것을 말해 달라고 하세요. kit #242에서는 검증한 에이전트가 새 테스트를 통과시키기 전에 MacBook Air에서 예전 테스트를 돌려 실패하는 것을 확인했습니다. 두 번째 세션의 토큰 비용이 들지만, 망가진 변경을 나중에 고치는 것보다는 쌉니다.</li>
  <li><strong>모든 테스트가 한 번은 실패하는 것을 보세요.</strong> 초록불을 믿기 전에, 그 테스트가 지키는 것을 망가뜨려 보고(또는 에이전트에게 맡기고) 빨간불이 들어오는지 확인하세요. 에이전트는 통과하는 테스트를 잘 씁니다. 바로 그래서 실패하는 모습을 봐야 합니다.</li>
  <li><strong>테스트를 두 번째 환경에서 돌리세요.</strong> 두 번째 Mac이 없어도 괜찮습니다. OS 버전 두 개, 또는 debug와 release 빌드로 된 CI 매트릭스면 충분한 출발점입니다. 찾는 것은 우연히 통과하는 테스트입니다.</li>
  <!-- src S7, S8 -->
  <li><strong>'테스트가 하나도 돌지 않음'을 실패로 처리하세요.</strong> Python 3.9의 <code>unittest</code>는 테스트를 하나도 찾지 못해도 성공으로 끝납니다. 그래서 경로에 오타 하나만 있어도 초록불을 받습니다. 우리 CI는 테스트 수를 읽어 0이면 실패시키고, 종료 코드만이 아니라 요약에 "0 failed"라고 적혀 있는지도 확인합니다. 아무것도 돌지 않았는데 에이전트가 "모든 테스트 통과"라고 보고하는 것은 가장 흔한 가짜 완료 중 하나입니다.</li>
</ol>

<h2>짧게 말하면</h2>
<!-- src S11 -->
<p>앱이 바이브 코딩으로 만들어졌는지보다, 누군가 계속 테스트하고 유지보수하는지가 더 중요합니다. 소프트웨어를 고를 때 확인해 볼 만합니다. 어떻게 테스트하는지 밝히고 있는지, 마지막 업데이트는 언제였는지.</p>
<p>속도는 에이전트에게 맡기세요. 확인은 올바른 것을 측정하는 테스트와, 결과를 읽는 사람에게 맡기세요.</p>

<h2>다음</h2>
<ul>
  <li>에이전트가 쓴 것을 여전히 사람이 읽어야 하는 이유: <a href="/ko/reviewing-ai-output/">AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유</a>.</li>
  <li>에이전트가 돌려준 계획과 보고서를 읽는 방법: <a href="/ko/reading-agent-output/">에이전트가 돌려준 결과 읽기</a>.</li>
</ul>

<h2>출처</h2>
<ul>
  <li>실패한 테스트와 원인: <a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>.</li>
  <li>수정과 독립 검증: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>.</li>
  <li>CI를 MacBook Air로 옮기는 작업과 실행 시간: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>.</li>
  <li>내보내기 엔진의 CI. 제한 시간이 바뀐 내력은 주석에 있습니다: <a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>.</li>
  <li>앱 저장소는 비공개입니다. 위의 앱 관련 내용은 앱의 CI 워크플로와 테스트 스크립트에서 가져왔습니다.</li>
</ul>
```

---

## de

- **title**: `Wie wir MarsDawn testen: ein Test, zwei Macs · MarsDawn`
- **description**: `Ein Test bestand auf einem Mac und schlug auf einem anderen fehl. Das Produkt war in Ordnung; der Test las die Farben des Bildschirms. Wie wir Tests schichten, und vier Gewohnheiten zum Nachmachen.`

```html
<section class="intro">
  <h1>Ein Test, der auf einem Mac besteht, testet vielleicht nicht, was du denkst.</h1>
  <!-- src S11 -->
  <p>Vibe Coding ist nichts Schlechtes. Beschreiben, was man will, und einen Agenten bauen lassen: So beginnt heute viel Software, und auch MarsDawn entsteht mit Agenten. Aber Software, auf die sich Menschen verlassen, wird an dem gemessen, was nach der ersten Version kommt: jahrelange Wartung und Sicherheit, die hält. Ein Agent kann an einem Abend Dutzende Dateien ändern. Wer prüft also, dass er nichts kaputt gemacht hat? Hier ist ein Test, der uns gezeigt hat, wie diese Prüfung schiefgehen kann, und was wir geändert haben.</p>
</section>

<div class="summary"><p><strong>Ein Test bestand auf einem Mac mini und schlug auf einem MacBook Air fehl. Das Produkt war in Ordnung. Der Test hatte Farben durch das Farbprofil des Bildschirms gelesen, und auf dem Mac mini hatte er nur durch Glück bestanden. Ein zweites Gerät fand einen Fehler im Test, nicht im Code.</strong></p></div>

<h2>Der Test, der auf einem MacBook Air fehlschlug</h2>
<!-- src S4: kit PR #240 (not merged), run 40196953693 -->
<p>Ein kompletter Durchlauf der Tests der Export-Engine dauert auf dem macOS-15-Runner von GitHub fast eine Stunde: etwa 32 Minuten für den Debug-Build und etwa 25 für den Release-Build. Um das zu verkürzen, haben wir begonnen, die macOS-26-Hälfte auf ein eigenes MacBook Air zu verlegen (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>).</p>
<!-- src S1: kit #241, run 40271990387 -->
<p>Beim ersten Lauf dort schlug ein Test fehl. Er exportiert ein PDF mit Hinweisboxen (Note, Tip, Warning) und prüft, ob jede am Rand einen Balken in der richtigen Farbe hat, also mit einem Farbabstand unter 0,16. Auf dem MacBook Air lagen die Abstände bei 0,1634, 0,1648 und 0,1796. Auf einem Mac mini, mit demselben Commit und denselben macOS- und Xcode-Versionen, bestand der Test.</p>
<p>Unser erster Verdacht: Der Export ist kaputt. War er nicht. Mit dem PDF war alles in Ordnung; was sich zwischen den Geräten unterschied, war die Art, wie der Test es las.</p>
<!-- src S1, S2: kit #241 -->
<p>Der Test wandelte jede PDF-Seite in ein Bild um und las die Pixel, und macOS zeichnet dieses Bild im Farbraum des Hauptbildschirms. Der Mac mini hing an einem gewöhnlichen externen Monitor, das MacBook Air nutzte sein eingebautes Display. Wir füllten ein Bild mit einem einzigen Orange und lasen es zurück: Aus (0,784; 0,278; 0,106) wurde auf dem Mac mini (0,822; 0,335; 0,179) und auf dem MacBook Air (0,782; 0,395; 0,221).</p>
<!-- src S3: kit #242 verification comment -->
<p>Jetzt kommt der entscheidende Teil: Auch auf dem Mac mini hatte der Test nicht die richtigen Farben gelesen. Er lag um bis zu 0,128 daneben, knapp innerhalb der Grenze von 0,16. Er bestand wegen des Monitors, nicht weil er den Balken richtig gemessen hätte.</p>
<!-- src S3, S10; {{TBD:mba-run}} = the self-hosted MacBook Air run, from kit #240 -->
<p>Der Fix (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>) ändert nur den Test: Er zeichnet die Seite in ein Bild mit festem sRGB-Farbraum, sodass kein Bildschirm beteiligt ist. Beide Geräte lesen die Balkenfarben jetzt exakt: Die beste Übereinstimmung ist 0,0, auf dem eingebauten Display des MacBook Air genauso wie auf dem Mac mini. Die CI des Pull Requests lief durch (<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>), ebenso die komplette Testsuite auf dem MacBook-Air-Runner (run {{TBD:mba-run}}). Dann haben wir ihn absichtlich scheitern lassen: Mit Blau als erwarteter Farbe überall wurde er für alle fünf Hinweisboxen rot.</p>
<p>Eine bekannte Lücke hat er noch. Note und Caution verwenden zwei Orangetöne, die etwa 0,119 auseinanderliegen, also innerhalb der Grenze von 0,16. Würden die beiden vertauscht, würde der Test es wahrscheinlich nicht merken. Das haben wir aufgeschrieben, statt so zu tun, als wäre der Test vollständig.</p>
<p>Ein Test, der nicht fehlschlagen kann, schützt nichts, und einer, der aus dem falschen Grund fehlschlägt, etwa wegen des Farbprofils eines Bildschirms, ebenso wenig. Grün auf einem Gerät heißt nur, dass der Test dort bestanden hat, nicht, dass er misst, was sein Name sagt.</p>

<h2>Was Rot und Grün bedeuten</h2>
<!-- src S14 -->
<p>Grün heißt: Ein Test hat bestanden. Das ist nur etwas wert, wenn du denselben Test schon rot gesehen hast, als das, was er prüft, wirklich falsch war. Deshalb kommt es auf die Reihenfolge an: absichtlich kaputt machen, rot werden sehen, zurücksetzen, grün werden sehen. Dann weißt du, dass der Test auf das Richtige schaut. Hast du ihn nie rot gesehen, heißt ein grüner Haken vielleicht nur, dass der Test gar nicht hinschaut.</p>

<h2>Tests sind Netze in Schichten</h2>
<p>Kein einzelner Test fängt alles. Jede Schicht ist ein Netz mit anderer Maschenweite, und ein Fehler, der durch eines rutscht, sollte im nächsten landen:</p>
<ul>
  <!-- src S6 -->
  <li><strong>Unit-Tests</strong> in der Export-Engine (dem quelloffenen <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>, auf dem auch der Befehl <code>marsdawn</code> läuft): ein Stück Code, das die falsche Antwort liefert.</li>
  <!-- src S13 -->
  <li><strong>Referenz-PDFs:</strong> Beispieldokumente werden exportiert, und der Text jeder Seite wird mit einer gespeicherten Fassung verglichen. Das fängt Inhalte, die still verschwinden, oder eine Seitenzahl, die sich ändert.</li>
  <!-- src S6, S9 -->
  <li><strong>Verschiedene Systeme und Builds:</strong> Die Engine läuft auf macOS 15, der ältesten unterstützten Version, und auf macOS 26, mit dem die App ausgeliefert wird, jeweils als Debug- und als Release-Build. Die komplette Testsuite der App läuft in vier Kombinationen: signiert und unsigniert, jeweils mit ausgeschalteter und eingeschalteter Paywall. Das fängt, was nur auf einem älteren System kaputtgeht oder nur in dem Build, den die Kundschaft tatsächlich bekommt.</li>
  <!-- src S4, S1 -->
  <li><strong>Echte Hardware:</strong> Neben den Maschinen von GitHub laufen die Tests auf eigenen Macs, darunter das MacBook Air von oben. Das fängt, was ein Server ohne Bildschirm nicht zeigen kann.</li>
  <!-- src S12 -->
  <li><strong>Negativkontrollen:</strong> Die CI der App hält 11 absichtlich kaputte Kopien eines Aufräumskripts bereit, jeder fehlt eine Sicherheitsprüfung, und die Tests müssen bei jeder einzelnen fehlschlagen. Besteht eine, ist der Test das, was kaputt ist.</li>
  <!-- src S3, S15 -->
  <li><strong>Ein zweites Paar Augen:</strong> Ein separater Agent prüft jede Änderung, und ein Szenario-Review klärt, wie Menschen eine Funktion wirklich nutzen werden, bevor sie gebaut wird. Das fängt „fertig“, das es nicht ist, und Code, der funktioniert, aber in der falschen Situation.</li>
  <li><strong>Zusammenführen tut ein Mensch.</strong> Keine Änderung landet im Hauptbranch, nur weil ein Agent sagt, sie sei fertig.</li>
</ul>

<h2>Was wir hineinwerfen</h2>
<p>Die Netze sind nur so gut wie das, was hineinkommt. Ein paar der Eingaben, mit denen die Tests die Engine füttern, und was jeder Test sicherstellt:</p>
<ul>
  <!-- src S16 -->
  <li><strong>Sehr große Dateien.</strong> Ein 2-MB-Dokument wird in weniger als anderthalb Sekunden dargestellt. Ein 5-MB-Dokument, das zu komplex für das Layout ist, öffnet sich trotzdem, als reiner Text, innerhalb einer Sekunde. Alles über 16 MB wird als Text angezeigt, ohne überhaupt geparst zu werden.</li>
  <!-- src S16 -->
  <li><strong>Hunderttausende Zeilen.</strong> Etwa 3 MB Zeilen mit je einem Wort, knapp 800.000 davon, werden schon während des Lesens als zu viel erkannt und als reiner Text angezeigt, statt die App zu blockieren.</li>
  <!-- src S17 -->
  <li><strong>Markierungen, die nie schließen.</strong> Ein Megabyte öffnender Abschnittsmarken ohne Gegenstück oder Zehntausende ineinander verschachtelte dürfen höchstens etwa doppelt so lange brauchen wie ein Megabyte reiner Text. Die Verschachtelung endet bei acht Ebenen.</li>
  <!-- src S18 -->
  <li><strong>Formeln.</strong> Eine fehlerhafte Formel zeigt an ihrer Stelle einen Fehler, statt die Seite kaputt zu machen. Eine mit mehr als 10.000 Zeichen bleibt, wie sie geschrieben ist, es werden jeweils nur die ersten 1.000 eines Dokuments gezeichnet, und nichts in einer Formel kann zu einem Link, einem Bild oder Seiten-Markup werden.</li>
  <!-- src S19 -->
  <li><strong>Feindseliges HTML in Markdown.</strong> Skripte werden entfernt und nie ausgeführt, eingebettete Frames werden entfernt, bevor die Seite sie zeigt. Bilder aus dem Netz bleiben aus, solange du sie nicht erlaubst, und auch dann laden nur sichere (HTTPS). In einer Kontrollkopie ist der Skriptfilter entfernt, und der Test muss an ihr fehlschlagen.</li>
  <!-- src S20 -->
  <li><strong>Eine feindselige Theme-Datei.</strong> Sie wird abgelehnt, und die Fehlermeldung wiederholt nie versteckte Steuerzeichen oder Links aus der Datei. Theme-Dateien über 16 KB werden gar nicht erst gelesen.</li>
</ul>
<!-- src S5 -->
<p>Nichts davon ist umsonst. Das Zeitlimit für einen Engine-Lauf ist von 30 Minuten auf 45, dann 50, dann 70 gestiegen, und macOS 15 ist einmal zweimal an das 50-Minuten-Limit gestoßen, obwohl jeder Test bestand.</p>

<h2>Vier Gewohnheiten zum Nachmachen</h2>
<ol>
  <li><strong>Trenne den Agenten, der schreibt, von dem, der prüft.</strong> Gib dem prüfenden die Änderung und was „fertig“ heißt, nicht die Erklärung des schreibenden, und lass ihn die Tests selbst ausführen und sagen, was er nicht geprüft hat. Bei kit #242 ließ der prüfende Agent den alten Test auf dem MacBook Air laufen, um ihn scheitern zu sehen, bevor er den neuen durchgehen ließ. Das kostet die Tokens einer zweiten Sitzung, ist aber immer noch billiger, als später eine kaputte Änderung zu reparieren.</li>
  <li><strong>Sieh jeden Test einmal fehlschlagen.</strong> Bevor du einem grünen Haken traust, mach kaputt, was er bewacht (oder lass den Agenten das tun), und vergewissere dich, dass er rot wird. Agenten sind gut darin, Tests zu schreiben, die bestehen; genau deshalb musst du sie scheitern sehen.</li>
  <li><strong>Lass deine Tests in einer zweiten Umgebung laufen.</strong> Kein zweiter Mac? Eine CI-Matrix mit zwei OS-Versionen oder mit einem Debug- und einem Release-Build ist ein guter Anfang. Du suchst Tests, die nur zufällig bestehen.</li>
  <!-- src S7, S8 -->
  <li><strong>Werte „keine Tests gelaufen“ als Fehlschlag.</strong> <code>unittest</code> in Python 3.9 beendet sich erfolgreich, wenn es überhaupt keine Tests findet; ein Tippfehler im Pfad bringt dir also einen grünen Haken. Unsere CI liest die Anzahl, schlägt bei null fehl und prüft, dass die Zusammenfassung „0 failed“ sagt, statt nur auf den Exit-Code zu schauen. Ein Agent, der „alle Tests bestanden“ meldet, obwohl keiner lief, ist eines der häufigsten falschen „Fertig“, die es gibt.</li>
</ol>

<h2>Kurz gesagt</h2>
<!-- src S11 -->
<p>Ob eine App per Vibe Coding entstanden ist, zählt weniger als die Frage, ob jemand sie weiter testet und pflegt. Das lohnt sich bei der Wahl von Software zu prüfen: Steht irgendwo, wie sie getestet wird, und wann wurde sie zuletzt aktualisiert?</p>
<p>Lass den Agenten schnell sein. Das Prüfen überlass Tests, die das Richtige messen, und einem Menschen, der das Ergebnis liest.</p>

<h2>Weiter</h2>
<ul>
  <li>Warum ein Mensch trotzdem lesen muss, was ein Agent geschrieben hat: <a href="/de/reviewing-ai-output/">Warum KI-Ergebnisse weiterhin einen menschlichen Leser brauchen</a>.</li>
  <li>Wie du die Pläne und Berichte liest, die ein Agent zurückgibt: <a href="/de/reading-agent-output/">Lesen, was dein Agent zurückgibt</a>.</li>
</ul>

<h2>Quellen</h2>
<ul>
  <li>Der fehlschlagende Test und seine Ursache: <a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>.</li>
  <li>Der Fix und seine unabhängige Prüfung: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>.</li>
  <li>Die CI auf ein MacBook Air verlegen, mit Laufzeiten: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>.</li>
  <li>Die CI der Export-Engine, mit der Geschichte ihres Zeitlimits in den Kommentaren: <a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>.</li>
  <li>Das Repository der App ist privat; die Angaben zur App oben stammen aus ihrem CI-Workflow und ihren Testskripten.</li>
</ul>
```

---

## fr

- **title**: `Comment nous testons MarsDawn : un test, deux Mac · MarsDawn`
- **description**: `Un test passait sur un Mac et échouait sur un autre. Le produit allait bien ; le test lisait les couleurs de l’écran. Comment nous superposons nos tests, et quatre habitudes à reprendre.`

```html
<section class="intro">
  <h1>Un test qui passe sur un Mac ne teste peut-être pas ce que vous croyez.</h1>
  <!-- src S11 -->
  <p>Le vibe coding n’a rien de mal. Décrire ce que l’on veut et laisser un agent le construire : c’est ainsi que naissent aujourd’hui beaucoup de logiciels, et MarsDawn est lui aussi développé avec des agents. Mais un logiciel sur lequel on compte se juge à ce qui vient après la première version : des années de maintenance, et une sécurité tenue dans la durée. Un agent peut modifier des dizaines de fichiers en une soirée. Alors, qui vérifie qu’il n’a rien cassé ? Voici un test qui nous a montré comment cette vérification peut déraper, et ce que nous avons changé.</p>
</section>

<div class="summary"><p><strong>Un test passait sur un Mac mini et échouait sur un MacBook Air. Le produit allait bien. Le test lisait les couleurs à travers le profil colorimétrique de l’écran, et sur le Mac mini, il passait par chance. Une deuxième machine a trouvé un bug dans le test, pas dans le code.</strong></p></div>

<h2>Le test qui échouait sur un MacBook Air</h2>
<!-- src S4: kit PR #240 (not merged), run 40196953693 -->
<p>Une exécution complète des tests du moteur d’export sur le runner macOS 15 de GitHub prend près d’une heure : environ 32 minutes pour le build debug et environ 25 pour le build release. Pour réduire ce temps, nous avons commencé à déplacer la moitié macOS 26 sur un MacBook Air à nous (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>).</p>
<!-- src S1: kit #241, run 40271990387 -->
<p>À la première exécution, un test a échoué. Il exporte un PDF avec des encadrés (Note, Tip, Warning) et vérifie que chacun porte sur son bord une barre de la bonne couleur, c’est-à-dire avec un écart de couleur inférieur à 0,16. Sur le MacBook Air, les écarts étaient de 0,1634, 0,1648 et 0,1796. Sur un Mac mini, avec le même commit, le même macOS et le même Xcode, le test passait.</p>
<p>Notre première idée : l’export était cassé. Il ne l’était pas. Le PDF n’avait aucun problème ; ce qui différait d’une machine à l’autre, c’était la façon dont le test le lisait.</p>
<!-- src S1, S2: kit #241 -->
<p>Le test transformait chaque page du PDF en image et en lisait les pixels, et macOS dessine cette image dans l’espace colorimétrique de l’écran principal. Le Mac mini était branché sur un moniteur externe ordinaire ; le MacBook Air utilisait son écran intégré. Nous avons rempli une image d’un seul orange et l’avons relue : (0,784 ; 0,278 ; 0,106) revenait en (0,822 ; 0,335 ; 0,179) sur le Mac mini et en (0,782 ; 0,395 ; 0,221) sur le MacBook Air.</p>
<!-- src S3: kit #242 verification comment -->
<p>Voici ce qui compte : sur le Mac mini non plus, le test ne lisait pas les bonnes couleurs. Il se trompait de 0,128 au plus, juste sous la limite de 0,16. Il passait grâce au moniteur, pas parce qu’il mesurait correctement la barre.</p>
<!-- src S3, S10; {{TBD:mba-run}} = the self-hosted MacBook Air run, from kit #240 -->
<p>Le correctif (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>) ne modifie que le test : il dessine la page dans une image à l’espace colorimétrique sRGB fixe, sans aucun écran en jeu. Les deux machines lisent désormais exactement les couleurs des barres : la meilleure correspondance est de 0,0, sur l’écran intégré du MacBook Air comme sur le Mac mini. La CI de la pull request est passée (<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>), tout comme la suite complète sur le runner du MacBook Air (run {{TBD:mba-run}}). Puis nous l’avons fait échouer exprès : avec du bleu comme couleur attendue partout, il est passé au rouge pour les cinq encadrés.</p>
<p>Il lui reste une faille connue. Note et Caution utilisent deux oranges séparés d’environ 0,119, sous la limite de 0,16 : si on les intervertissait, le test ne le remarquerait probablement pas. Nous l’avons noté plutôt que de faire comme si le test était complet.</p>
<p>Un test qui ne peut pas échouer ne protège rien, pas plus qu’un test qui échoue pour une mauvaise raison, comme le profil colorimétrique d’un écran. Le vert sur une machine vous dit que le test y est passé, pas qu’il mesure ce que dit son nom.</p>

<h2>Ce que veulent dire le rouge et le vert</h2>
<!-- src S14 -->
<p>Le vert signifie qu’un test est passé. Cela ne vaut quelque chose que si vous avez vu ce même test passer au rouge quand ce qu’il vérifie était vraiment faux. L’ordre compte donc : casser exprès, le voir passer au rouge, remettre en place, le voir passer au vert. Vous savez alors que le test regarde au bon endroit. Si vous ne l’avez jamais vu rouge, une coche verte veut peut-être seulement dire que le test ne regarde pas.</p>

<h2>Les tests sont des filets superposés</h2>
<p>Aucun test ne rattrape tout. Chaque couche est un filet aux mailles différentes, et une erreur qui passe à travers l’un devrait tomber dans le suivant :</p>
<ul>
  <!-- src S6 -->
  <li><strong>Tests unitaires</strong> dans le moteur d’export (le projet open source <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>, qui fait aussi tourner la commande <code>marsdawn</code>) : un morceau de code qui renvoie une mauvaise réponse.</li>
  <!-- src S13 -->
  <li><strong>PDF de référence :</strong> des documents d’exemple sont exportés, et le texte de chaque page est comparé à une copie enregistrée. Cela rattrape le contenu qui disparaît sans bruit, ou un nombre de pages qui change.</li>
  <!-- src S6, S9 -->
  <li><strong>Systèmes et builds différents :</strong> le moteur tourne sous macOS 15, la plus ancienne version prise en charge, et sous macOS 26, celle avec laquelle l’app est livrée, chaque fois en build debug et en build release. La suite complète de l’app tourne en quatre combinaisons : signée et non signée, chacune avec le paywall désactivé puis activé. Cela rattrape ce qui ne casse que sur un système plus ancien, ou seulement dans le build que reçoivent réellement les clients.</li>
  <!-- src S4, S1 -->
  <li><strong>Vrai matériel :</strong> en plus des machines de GitHub, les tests tournent sur nos propres Mac, dont le MacBook Air ci-dessus. Cela rattrape ce qu’un serveur sans écran ne peut pas montrer.</li>
  <!-- src S12 -->
  <li><strong>Contrôles négatifs :</strong> la CI de l’app garde 11 copies volontairement cassées d’un script de nettoyage, chacune privée d’une vérification de sécurité, et les tests doivent échouer sur chacune. Si l’une passe, c’est le test qui est cassé.</li>
  <!-- src S3, S15 -->
  <li><strong>Un deuxième regard :</strong> un agent distinct vérifie chaque changement, et une revue de scénarios examine comment les gens utiliseront vraiment une fonction avant qu’elle soit construite. Cela rattrape le « terminé » qui ne l’est pas, et le code qui marche, mais dans la mauvaise situation.</li>
  <li><strong>Une personne fusionne.</strong> Aucun changement n’arrive sur la branche principale simplement parce qu’un agent a dit qu’il était terminé.</li>
</ul>

<h2>Ce que nous lui faisons subir</h2>
<p>Ces filets ne valent que ce qu’on y jette. Voici quelques-unes des entrées que les tests donnent au moteur, et ce que chaque test garantit :</p>
<ul>
  <!-- src S16 -->
  <li><strong>Des fichiers très volumineux.</strong> Un document de 2 Mo s’affiche en moins d’une seconde et demie. Un document de 5 Mo trop complexe à mettre en page s’ouvre quand même, en texte brut, en moins d’une seconde. Au-delà de 16 Mo, le fichier s’affiche en texte sans être analysé du tout.</li>
  <!-- src S16 -->
  <li><strong>Des centaines de milliers de lignes.</strong> Environ 3 Mo de lignes d’un seul mot, près de 800 000, sont repérés comme trop lourds en cours de lecture et affichés en texte brut au lieu de bloquer l’app.</li>
  <!-- src S17 -->
  <li><strong>Des balises jamais fermées.</strong> Un mégaoctet de marques d’ouverture de section sans fermeture, ou des dizaines de milliers imbriquées les unes dans les autres, ne doit pas prendre plus d’environ deux fois le temps d’un mégaoctet de texte brut. L’imbrication s’arrête à huit niveaux.</li>
  <!-- src S18 -->
  <li><strong>Des formules.</strong> Une formule erronée affiche une erreur à sa place au lieu de casser la page. Une formule de plus de 10 000 caractères reste telle qu’elle est écrite, seules les 1 000 premières d’un document sont dessinées à la fois, et rien dans une formule ne peut devenir un lien, une image ou du balisage de page.</li>
  <!-- src S19 -->
  <li><strong>Du HTML hostile dans le Markdown.</strong> Les scripts sont retirés et ne s’exécutent jamais, et les cadres intégrés sont enlevés avant que la page les affiche. Les images distantes restent désactivées tant que vous ne les autorisez pas, et même alors, seules les images sécurisées (HTTPS) se chargent. Dans une copie témoin, le filtre de scripts est retiré, et le test doit échouer sur elle.</li>
  <!-- src S20 -->
  <li><strong>Un fichier de thème hostile.</strong> Il est refusé, et le message d’erreur ne répète jamais les caractères de contrôle cachés ni les liens du fichier. Les fichiers de thème de plus de 16 Ko ne sont même pas lus.</li>
</ul>
<!-- src S5 -->
<p>Rien de tout cela n’est gratuit. La limite de temps d’une exécution du moteur est passée de 30 minutes à 45, puis 50, puis 70, et macOS 15 a un jour atteint deux fois la limite de 50 minutes alors que tous les tests passaient.</p>

<h2>Quatre habitudes à reprendre</h2>
<ol>
  <li><strong>Séparez l’agent qui écrit de l’agent qui vérifie.</strong> Donnez au vérificateur le changement et ce que « terminé » veut dire, pas l’explication de celui qui a écrit, et demandez-lui de lancer lui-même les tests et de dire ce qu’il n’a pas vérifié. Pour kit #242, l’agent vérificateur a lancé l’ancien test sur le MacBook Air pour le voir échouer avant de valider le nouveau. Cela coûte les tokens d’une deuxième session, ce qui reste moins cher que de réparer plus tard un changement cassé.</li>
  <li><strong>Voyez chaque test échouer une fois.</strong> Avant de faire confiance à une coche verte, cassez ce qu’elle protège (ou demandez à l’agent de le faire) et vérifiez qu’elle passe au rouge. Les agents savent très bien écrire des tests qui passent ; c’est justement pour cela qu’il faut les voir échouer.</li>
  <li><strong>Lancez vos tests dans un deuxième environnement.</strong> Pas de deuxième Mac ? Une matrice de CI avec deux versions de l’OS, ou avec un build debug et un build release, est un bon début. Vous cherchez les tests qui ne passent que par hasard.</li>
  <!-- src S7, S8 -->
  <li><strong>Considérez « aucun test lancé » comme un échec.</strong> L’outil <code>unittest</code> de Python 3.9 se termine avec succès quand il ne trouve aucun test, si bien qu’une faute de frappe dans un chemin vous donne une coche verte. Notre CI lit le nombre de tests et échoue à zéro, et vérifie que le résumé indique « 0 failed », sans se fier au seul code de sortie. Un agent qui annonce « tous les tests passent » alors qu’aucun n’a tourné : c’est l’un des faux « terminé » les plus courants.</li>
</ol>

<h2>En bref</h2>
<!-- src S11 -->
<p>Qu’une app ait été faite en vibe coding compte moins que de savoir si quelqu’un continue de la tester et de la maintenir. Cela vaut la peine de le vérifier au moment de choisir un logiciel : dit-il comment il est testé, et quand a-t-il été mis à jour pour la dernière fois ?</p>
<p>Laissez l’agent aller vite. Confiez la vérification à des tests qui mesurent la bonne chose, et à une personne qui lit le résultat.</p>

<h2>Pour aller plus loin</h2>
<ul>
  <li>Pourquoi une personne doit encore lire ce qu’un agent a écrit : <a href="/fr/reviewing-ai-output/">Pourquoi ce que produit l’IA a encore besoin d’un lecteur humain</a>.</li>
  <li>Comment lire les plans et les rapports qu’un agent vous rend : <a href="/fr/reading-agent-output/">Lire ce que votre agent vous rend</a>.</li>
</ul>

<h2>Sources</h2>
<ul>
  <li>Le test qui échouait et sa cause : <a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>.</li>
  <li>Le correctif et sa vérification indépendante : <a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>.</li>
  <li>Le passage de la CI sur un MacBook Air, avec les temps d’exécution : <a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>.</li>
  <li>La CI du moteur d’export, avec l’historique de sa limite de temps dans les commentaires : <a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>.</li>
  <li>Le dépôt de l’app est privé ; les détails sur l’app ci-dessus viennent de son workflow de CI et de ses scripts de test.</li>
</ul>
```

---

## es

- **title**: `Cómo probamos MarsDawn: una prueba, dos Mac · MarsDawn`
- **description**: `Una prueba pasaba en un Mac y fallaba en otro. El producto estaba bien; la prueba leía los colores de la pantalla. Cómo apilamos nuestras pruebas, y cuatro hábitos que puedes copiar.`

```html
<section class="intro">
  <h1>Una prueba que pasa en un Mac quizá no esté probando lo que crees.</h1>
  <!-- src S11 -->
  <p>El vibe coding no es algo malo. Describir lo que quieres y dejar que un agente lo construya es como empieza hoy mucho software, y MarsDawn también se desarrolla con agentes. Pero el software del que la gente depende se juzga por lo que viene después de la primera versión: años de mantenimiento y seguir siendo seguro. Un agente puede cambiar decenas de archivos en una noche. Entonces, ¿quién comprueba que no ha roto nada? Aquí va una prueba que nos enseñó cómo puede fallar esa comprobación, y lo que cambiamos.</p>
</section>

<div class="summary"><p><strong>Una prueba pasaba en un Mac mini y fallaba en un MacBook Air. El producto estaba bien. La prueba leía los colores a través del perfil de color de la pantalla, y en el Mac mini pasaba por suerte. Una segunda máquina encontró un error en la prueba, no en el código.</strong></p></div>

<h2>La prueba que fallaba en un MacBook Air</h2>
<!-- src S4: kit PR #240 (not merged), run 40196953693 -->
<p>Una ejecución completa de las pruebas del motor de exportación en el runner de macOS 15 de GitHub tarda cerca de una hora: unos 32 minutos para la compilación debug y unos 25 para la release. Para acortarlo, empezamos a pasar la mitad de macOS 26 a un MacBook Air propio (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>).</p>
<!-- src S1: kit #241, run 40271990387 -->
<p>En su primera ejecución allí, falló una prueba. Exporta un PDF con recuadros de aviso (Note, Tip, Warning) y comprueba que cada uno tenga en el borde una barra del color correcto, es decir, con una distancia de color menor que 0,16. En el MacBook Air, las distancias fueron 0,1634, 0,1648 y 0,1796. En un Mac mini, con el mismo commit, el mismo macOS y el mismo Xcode, la prueba pasaba.</p>
<p>Lo primero que pensamos fue que la exportación se había roto. No era así. El PDF no tenía ningún problema; lo que cambiaba entre las dos máquinas era cómo lo leía la prueba.</p>
<!-- src S1, S2: kit #241 -->
<p>La prueba convertía cada página del PDF en una imagen y leía los píxeles, y macOS dibuja esa imagen en el espacio de color de la pantalla principal. El Mac mini estaba conectado a un monitor externo corriente; el MacBook Air usaba su pantalla integrada. Llenamos una imagen con un solo naranja y la volvimos a leer: (0,784; 0,278; 0,106) volvía como (0,822; 0,335; 0,179) en el Mac mini y como (0,782; 0,395; 0,221) en el MacBook Air.</p>
<!-- src S3: kit #242 verification comment -->
<p>Esto es lo importante: en el Mac mini, la prueba tampoco leía los colores correctos. Se desviaba hasta 0,128, justo dentro del límite de 0,16. Pasaba gracias al monitor, no porque midiera bien la barra.</p>
<!-- src S3, S10; {{TBD:mba-run}} = the self-hosted MacBook Air run, from kit #240 -->
<p>La corrección (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>) solo cambia la prueba: dibuja la página en una imagen con un espacio de color sRGB fijo, así que no interviene ninguna pantalla. Ahora las dos máquinas leen los colores de las barras con exactitud: la mejor coincidencia es 0,0, tanto en la pantalla integrada del MacBook Air como en el Mac mini. La CI del pull request pasó (<a href="https://github.com/redtear1115/mars-dawn-kit/actions/runs/40285279080">run 40285279080</a>), y también la batería completa en el runner del MacBook Air (run {{TBD:mba-run}}). Después la hicimos fallar a propósito: con todos los colores esperados en azul, se puso en rojo en los cinco recuadros de aviso.</p>
<p>Todavía tiene un hueco conocido. Note y Caution usan dos naranjas separados por unos 0,119, dentro del límite de 0,16, así que si se intercambiaran, la prueba probablemente no lo notaría. Lo dejamos por escrito en lugar de fingir que la prueba es completa.</p>
<p>Una prueba que no puede fallar no protege nada, y tampoco una que falla por el motivo equivocado, como el perfil de color de una pantalla. El verde en una máquina te dice que la prueba pasó allí, no que mida lo que dice su nombre.</p>

<h2>Qué significan el rojo y el verde</h2>
<!-- src S14 -->
<p>Verde significa que una prueba pasó. Eso solo vale algo si has visto esa misma prueba ponerse en rojo cuando lo que comprueba estaba realmente mal. Por eso el orden importa: rómpelo a propósito, mira cómo se pone en rojo, déjalo como estaba, mira cómo se pone en verde. Entonces sabes que la prueba mira donde debe. Si nunca la has visto en rojo, una marca verde puede significar solo que la prueba no está mirando.</p>

<h2>Las pruebas son capas de redes</h2>
<p>Ninguna prueba lo atrapa todo. Cada capa es una red con una malla distinta, y un error que se escapa por una debería caer en la siguiente:</p>
<ul>
  <!-- src S6 -->
  <li><strong>Pruebas unitarias</strong> en el motor de exportación (el proyecto de código abierto <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>, que también hace funcionar el comando <code>marsdawn</code>): un trozo de código que devuelve la respuesta equivocada.</li>
  <!-- src S13 -->
  <li><strong>PDF de referencia:</strong> se exportan documentos de ejemplo y el texto de cada página se compara con una copia guardada. Esto atrapa contenido que desaparece sin avisar o un número de páginas que cambia.</li>
  <!-- src S6, S9 -->
  <li><strong>Sistemas y compilaciones distintos:</strong> el motor se ejecuta en macOS 15, la versión más antigua que admite, y en macOS 26, con la que se distribuye la app, cada uno como compilación debug y release. La batería completa de la app se ejecuta en cuatro combinaciones: firmada y sin firmar, cada una con el paywall desactivado y activado. Esto atrapa lo que solo se rompe en un sistema más antiguo, o solo en la compilación que reciben de verdad los clientes.</li>
  <!-- src S4, S1 -->
  <li><strong>Hardware real:</strong> además de las máquinas de GitHub, las pruebas se ejecutan en Mac propios, incluido el MacBook Air de arriba. Esto atrapa lo que un servidor sin pantalla no puede mostrar.</li>
  <!-- src S12 -->
  <li><strong>Controles negativos:</strong> la CI de la app guarda 11 copias rotas a propósito de un script de limpieza, a cada una le falta una comprobación de seguridad, y las pruebas tienen que fallar con todas. Si una pasa, lo que está roto es la prueba.</li>
  <!-- src S3, S15 -->
  <li><strong>Otro par de ojos:</strong> un agente aparte verifica cada cambio, y una revisión de escenarios comprueba cómo usará de verdad la gente una función antes de construirla. Esto atrapa el «terminado» que no lo está, y el código que funciona, pero en la situación equivocada.</li>
  <li><strong>Una persona fusiona.</strong> Ningún cambio llega a la rama principal solo porque un agente haya dicho que estaba terminado.</li>
</ul>

<h2>Lo que le echamos</h2>
<p>Esas redes valen tanto como lo que se echa en ellas. Algunas de las entradas con las que las pruebas alimentan al motor, y lo que cada prueba garantiza:</p>
<ul>
  <!-- src S16 -->
  <li><strong>Archivos muy grandes.</strong> Un documento de 2 MB se muestra en menos de un segundo y medio. Uno de 5 MB demasiado complejo para maquetar se abre igualmente, como texto sin formato, en menos de un segundo. Lo que pase de 16 MB se muestra como texto sin analizarlo en absoluto.</li>
  <!-- src S16 -->
  <li><strong>Cientos de miles de líneas.</strong> Unos 3 MB de líneas de una sola palabra, cerca de 800 000, se detectan como demasiado a mitad de la lectura y se muestran como texto sin formato en lugar de bloquear la app.</li>
  <!-- src S17 -->
  <li><strong>Marcas que nunca se cierran.</strong> Un megabyte de marcas de apertura de sección sin cierre, o decenas de miles anidadas unas dentro de otras, no debe tardar más de unas dos veces lo que tarda un megabyte de texto sin formato. El anidamiento se detiene en ocho niveles.</li>
  <!-- src S18 -->
  <li><strong>Fórmulas.</strong> Una fórmula mal escrita muestra un error en su sitio en lugar de romper la página. Una de más de 10 000 caracteres se queda tal como está escrita, solo se dibujan a la vez las primeras 1000 de un documento, y nada dentro de una fórmula puede convertirse en un enlace, una imagen o marcado de la página.</li>
  <!-- src S19 -->
  <li><strong>HTML hostil dentro de Markdown.</strong> Los scripts se eliminan y nunca se ejecutan, y los marcos incrustados se quitan antes de que la página los muestre. Las imágenes remotas siguen desactivadas a menos que las permitas, e incluso entonces solo cargan las seguras (HTTPS). Una copia de control tiene quitado el filtro de scripts, y la prueba tiene que fallar con ella.</li>
  <!-- src S20 -->
  <li><strong>Un archivo de tema hostil.</strong> Se rechaza, y el mensaje de error nunca repite caracteres de control ocultos ni enlaces del archivo. Los archivos de tema de más de 16 KB ni siquiera se leen.</li>
</ul>
<!-- src S5 -->
<p>Nada de esto es gratis. El límite de tiempo de una ejecución del motor ha pasado de 30 minutos a 45, luego a 50 y luego a 70, y macOS 15 llegó una vez dos veces al límite de 50 minutos con todas las pruebas pasando.</p>

<h2>Cuatro hábitos que puedes copiar</h2>
<ol>
  <li><strong>Separa el agente que escribe del agente que comprueba.</strong> Dale al que comprueba el cambio y lo que significa «terminado», no la explicación del que lo escribió, y pídele que ejecute él mismo las pruebas y diga qué no comprobó. En kit #242, el agente verificador ejecutó la prueba antigua en el MacBook Air para verla fallar antes de dar por buena la nueva. Cuesta los tokens de una segunda sesión, que sigue siendo más barato que arreglar después un cambio roto.</li>
  <li><strong>Mira fallar cada prueba una vez.</strong> Antes de fiarte de una marca verde, rompe lo que protege (o pídeselo al agente) y asegúrate de que se pone en rojo. Los agentes escriben muy bien pruebas que pasan; justo por eso necesitas verlas fallar.</li>
  <li><strong>Ejecuta tus pruebas en un segundo entorno.</strong> ¿No tienes un segundo Mac? Una matriz de CI con dos versiones del sistema, o con una compilación debug y otra release, es un buen comienzo. Buscas pruebas que solo pasan por casualidad.</li>
  <!-- src S7, S8 -->
  <li><strong>Trata «no se ejecutó ninguna prueba» como un fallo.</strong> El <code>unittest</code> de Python 3.9 termina con éxito cuando no encuentra ninguna prueba, así que una errata en una ruta te da una marca verde. Nuestra CI lee el número de pruebas y falla si es cero, y comprueba que el resumen diga «0 failed», no solo el código de salida. Un agente que informa de que «todas las pruebas pasan» cuando no se ejecutó ninguna es uno de los falsos «terminado» más comunes que hay.</li>
</ol>

<h2>En pocas palabras</h2>
<!-- src S11 -->
<p>Que una app se haya hecho con vibe coding importa menos que si alguien sigue probándola y manteniéndola. Vale la pena comprobarlo al elegir software: ¿explica cómo se prueba?, ¿cuándo se actualizó por última vez?</p>
<p>Deja que el agente sea rápido. La comprobación, déjasela a pruebas que miden lo correcto y a una persona que lee el resultado.</p>

<h2>Siguiente</h2>
<ul>
  <li>Por qué una persona todavía tiene que leer lo que escribió un agente: <a href="/es/reviewing-ai-output/">Por qué lo que produce la IA todavía necesita un lector humano</a>.</li>
  <li>Cómo leer los planes e informes que te devuelve un agente: <a href="/es/reading-agent-output/">Leer lo que te devuelve tu agente</a>.</li>
</ul>

<h2>Fuentes</h2>
<ul>
  <li>La prueba que fallaba y su causa: <a href="https://github.com/redtear1115/mars-dawn-kit/issues/241">mars-dawn-kit #241</a>.</li>
  <li>La corrección y su verificación independiente: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">mars-dawn-kit #242</a>.</li>
  <li>Cómo pasamos la CI a un MacBook Air, con tiempos de ejecución: <a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">mars-dawn-kit #240</a>.</li>
  <li>La CI del motor de exportación, con el historial de su límite de tiempo en los comentarios: <a href="https://github.com/redtear1115/mars-dawn-kit/blob/main/.github/workflows/ci.yml">ci.yml</a>.</li>
  <li>El repositorio de la app es privado; los detalles de la app que aparecen arriba salen de su flujo de CI y de sus scripts de prueba.</li>
</ul>
```

---

## Footer label (`ui` dict, `how-we-test`)

| en | zh-Hant | zh-Hans | ja | ko | de | fr | es |
|---|---|---|---|---|---|---|---|
| How we test | 我們怎麼測試 | 我们怎么测试 | テストのしかた | 테스트하는 방법 | So testen wir | Comment nous testons | Cómo probamos |

en and zh-Hant: approved by Ray as of 57f26b8 (「ok 文案可以」). zh-Hans, ja, ko, de, fr, es: translated from that approved text, en and zh-Hant unchanged. All eight still carry `{{TBD:mba-run}}` (one place each, in the fix paragraph); fill it in every locale before publishing.

Co-authored-by: Grok <grok@southern-light.dev>
