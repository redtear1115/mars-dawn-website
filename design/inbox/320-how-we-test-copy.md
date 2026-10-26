# #320 How we test MarsDawn: en and zh-Hant first draft

Issue: https://github.com/redtear1115/mars-dawn-website/issues/320
Outline: the issue's latest comment (Una's review, accepted as is).
Status: **proposal**. It goes live only after Ray approves.

## How to read this file

- The bodies below are HTML fragments in the same shape as the other evergreen articles in `scripts/build_pages.py` (`section.intro` → `div.summary` → `h2` sections → Next → Sources).
- **Every number has a source in an HTML comment** (`<!-- src: ... -->`), as #320's acceptance requires.
- **Placeholders**: `{{TBD:...}}`. Fill them in after kit #242 is merged, using that CI run. Don't publish while any are left: `grep -n 'TBD' design/inbox/320-how-we-test-copy.md`.
- Suggested slug: `/how-we-test/` (zh-Hant `/zh-hant/how-we-test/`). It needs to be added to `article_dates.py`'s `ARTICLE_SLUGS` and to the footer `ui` dict. Footer labels are at the end of this file.
- The app repo is private, so app facts are described in the text but not linked. Kit facts link to the public kit repo.

## Facts and sources

| # | Fact | Source |
|---|---|---|
| S1 | The test failed on the MacBook Air: 0.1634 / 0.1648 / 0.1796, limit 0.16. It passed on the Mac mini. Same commit, macOS 26.6.2, Xcode 27.1. | kit #241 body; CI run 40271990387 |
| S2 | The pure-colour probe: sRGB (0.784, 0.278, 0.106) reads back as (0.822, 0.335, 0.179) on the mini and (0.782, 0.395, 0.221) on the Air. | kit #241 body |
| S3 | Independent verification of the fix: `best` 0.0 on both machines. The old path on the mini was off by up to 0.128. With the expected colours set to #0000FF, all 5 callouts fail. Note and Caution are about 0.119 apart. | kit PR #242, comment of 2026-10-26 07:39 UTC |
| S4 | A full run on hosted macOS 15: debug about 32 min plus release about 25 min (run 40196953693). Moving macOS 26 to self-hosted MacBook Airs is expected to cut a normal PR from about 60 min to about 15–20. | kit PR #240 body (**not merged**; the 15–20 min figure is an estimate) |
| S5 | The timeout went from 30 to 45, then 50, then 70 minutes. macos-15 hit the 50-minute limit twice in the release pass with every test passing (run 39231688388). | kit `.github/workflows/ci.yml` comments, main 8e93930, lines 27–34 |
| S6 | Kit CI matrix: macos-15 (the floor) and macos-26 (what the app ships on), debug and release passes. The PDF corpus runs in its own process. A release suite name that matches no test fails the job. | kit `ci.yml` lines 21–26, 85–129 |
| S7 | App CI: one self-hosted runner, `CODE_SIGNING_ALLOWED=NO`. "An exit code is not a result": python 3.9's unittest exits 0 having found no tests, so the job checks the count is above 0, and guards.sh's summary must read "N passed, 0 failed" with N > 0. | app `.github/workflows/ci.yml` lines 78–108 (private) |
| S8 | That guards.sh check came out of an independent verification of #335 (finding P3). | app #341 (private) |
| S9 | `tools/test.sh --all`: signed and unsigned, each with the paywall off and on, so 4 combinations, run locally on a Mac and a MacBook Air (not in CI). | app `tools/test.sh` lines 9, 24–26; #320 owner comment |

---

## en

- **title**: `How we test MarsDawn: one test, two Macs · MarsDawn`
- **description** (about 150 characters): `A test passed on one Mac and failed on another. The product was fine; the test was reading the screen's colours. How we check agent-written code, and three habits you can copy.`

```html
<section class="intro">
  <h1>A test that passes on one Mac may not be testing what you think.</h1>
  <p>MarsDawn is built with agents, and an agent can change dozens of files in an evening. So who checks it didn't break anything? Here is one test that showed us how that checking goes wrong, and what we changed.</p>
</section>

<div class="summary"><p><strong>A test passed on a Mac mini and failed on a MacBook Air. The product was fine. The test had been reading colours through the screen's colour profile, and on the Mac mini it had been passing by luck. A second machine found a bug in the test, not in the code.</strong></p></div>

<h2>The test that failed on a MacBook Air</h2>
<!-- src S4: kit PR #240 (not merged), run 40196953693 -->
<p>A full run of the export engine's tests on GitHub's macOS 15 runner takes close to an hour: about 32 minutes for the debug build and about 25 for the release build. To cut that down, we started moving the macOS 26 half onto a MacBook Air of our own (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>).</p>
<!-- src S1: kit #241, run 40271990387 -->
<p>On its first run there, one test failed. It exports a PDF with callouts (Note, Tip, Warning) and checks that each one has a coloured bar at its edge, in the right colour. "Right" means a colour distance under 0.16. On the MacBook Air the distances were 0.1634, 0.1648 and 0.1796. On a Mac mini, the same commit with the same macOS and Xcode, the test passed.</p>
<p>Our first guess was that the export had broken. It hadn't. Nothing was wrong with the PDF; what differed between the machines was how the test read it.</p>
<!-- src S1, S2: kit #241 -->
<p>The test turned each PDF page into an image and read the pixels. macOS draws that image in the colour space of the main display. The Mac mini was connected to an ordinary external monitor; the MacBook Air was using its built-in screen. We filled an image with one orange and read it back: (0.784, 0.278, 0.106) came back as (0.822, 0.335, 0.179) on the Mac mini and (0.782, 0.395, 0.221) on the MacBook Air.</p>
<!-- src S3: kit #242 verification comment -->
<p>Then came the part that matters. On the Mac mini, the test hadn't been reading the right colours either. It was off by as much as 0.128, just inside the 0.16 limit. It had been passing because of the monitor, not because it was measuring the bar correctly.</p>
<!-- src S3; {{TBD:242-run}} = the CI run after kit #242 is merged -->
<p>The fix (<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>) changes only the test: it draws the page into an image with a fixed sRGB colour space, so no screen is involved. Now both machines read the bar colours with a distance of {{TBD:distance, expected 0}} (CI run {{TBD:242-run}}). To check that it still catches mistakes, we set every expected colour to blue, and it failed for all five callouts.</p>
<p>It still has a known gap. Note and Caution use two oranges about 0.119 apart, inside the 0.16 limit, so if those two were swapped, the test would probably not notice. We've written that down rather than pretend the test is complete.</p>
<p>What we took from it: green on one machine tells you the test passed on that machine. It doesn't tell you the test measures what its name says. A second environment finds bugs in the tests, not only in the product.</p>

<h2>Who checks, and where</h2>
<p><strong>The agent that writes a change doesn't verify it.</strong> A separate session gets the pull request and its acceptance list, not the writer's reasoning, and has to run things itself. For kit #242, the verifier ran the old test on the MacBook Air to watch it fail, ran the new one on both machines, and broke the expected colours on purpose to see the test go red. It also found the Note and Caution gap above and listed what it had not checked.</p>
<!-- src S6, S5: kit ci.yml -->
<p><strong>The export engine</strong> (the open-source <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>, which also powers the <code>marsdawn</code> command) runs on macOS 15, the oldest version it supports, and on macOS 26, the one the app ships on. Each runs a debug pass and a release pass, and a corpus of sample PDFs is checked in a process of its own. That isn't free: the time limit for a run has gone from 30 minutes to 45, then 50, then 70, and macOS 15 once hit the 50-minute limit twice with every test passing.</p>
<!-- src S7, S9: app ci.yml, tools/test.sh (private) -->
<p><strong>The app</strong> runs its CI on one Mac of our own, unsigned. Its full suite also runs locally on two Macs in four combinations: signed and unsigned, each with the paywall off and on, because the shipping build has the paywall on and a development build doesn't.</p>
<p><strong>A person merges.</strong> No change reaches the main branch because an agent said it was done.</p>

<h2>Three habits you can copy</h2>
<ol>
  <li><strong>Keep the agent that writes apart from the agent that checks.</strong> Give the checker the change and what "done" means, not the writer's explanation, and ask it to run the tests itself and say what it didn't check. Otherwise the second agent tends to approve whatever the first one wrote. It costs a second session's tokens; on a change you'd have to fix later, it's cheaper.</li>
  <li><strong>Run your tests in a second environment.</strong> No second Mac? A CI matrix with two OS versions, or a debug build and a release build, is enough to start. You're looking for tests that pass only by accident.</li>
  <!-- src S7, S8 -->
  <li><strong>Treat "no tests ran" as a failure.</strong> Python 3.9's <code>unittest</code> exits successfully when it finds no tests at all, so a typo in a path gives you a green check. Our CI reads the count and fails if it's zero; it also checks the summary says "0 failed", not just the exit code. That second check came out of the independent verification of an earlier change. An agent reporting "all tests pass" when none ran is one of the most common false finishes there is.</li>
</ol>

<h2>The short version</h2>
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
  <li>The app's repository is private; the app details above come from its CI workflow and test script.</li>
</ul>
```

---

## zh-Hant

- **title**: `MarsDawn 怎麼測試：同一個測試，兩台 Mac · MarsDawn`
- **description**: `同一個測試，在一台 Mac 通過、在另一台失敗。產品沒壞，是測試讀到了螢幕的色彩。我們怎麼檢查 agent 寫的程式，以及你也能照做的三個習慣。`

```html
<section class="intro">
  <h1>在一台 Mac 上通過的測試，不一定在測你以為的東西。</h1>
  <p>MarsDawn 是用 agent 開發的，而 agent 一個晚上就能改幾十個檔案。那誰來確認它沒改壞？下面是一個讓我們看清楚「檢查」會怎麼出錯的測試，以及我們改了什麼。</p>
</section>

<div class="summary"><p><strong>同一個測試，在 Mac mini 上通過，在 MacBook Air 上失敗。產品沒壞。是測試透過螢幕的色彩描述檔在讀顏色，它在 Mac mini 上通過只是運氣好。換一台機器，抓到的是測試的 bug，不是程式的 bug。</strong></p></div>

<h2>只在 MacBook Air 上失敗的測試</h2>
<!-- src S4: kit PR #240（未合併）、run 40196953693 -->
<p>輸出引擎的測試，在 GitHub 的 macOS 15 機器上完整跑一次將近一小時：debug 版約 32 分鐘，release 版約 25 分鐘。為了縮短時間，我們開始把 macOS 26 那一半移到自己的 MacBook Air 上跑（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/240">kit #240</a>）。</p>
<!-- src S1: kit #241、run 40271990387 -->
<p>在那台機器上第一次跑，就有一個測試失敗。這個測試會輸出一份帶有提示框（Note、Tip、Warning）的 PDF，檢查每個提示框邊上都有一條顏色正確的色條。「正確」的意思是色差小於 0.16。在 MacBook Air 上，色差是 0.1634、0.1648 和 0.1796。換到 Mac mini，同一個 commit、同樣的 macOS 和 Xcode，測試通過。</p>
<p>我們第一個懷疑是輸出壞了。結果不是：PDF 本身沒問題，兩台機器不一樣的，是測試讀它的方式。</p>
<!-- src S1, S2: kit #241 -->
<p>這個測試會把 PDF 每一頁畫成圖片，再讀像素。macOS 畫這張圖時，用的是主螢幕的色彩空間。Mac mini 接的是一般的外接螢幕，MacBook Air 用的是內建螢幕。我們拿一張填滿同一種橘色的圖片讀回來：(0.784, 0.278, 0.106) 在 Mac mini 上讀成 (0.822, 0.335, 0.179)，在 MacBook Air 上讀成 (0.782, 0.395, 0.221)。</p>
<!-- src S3: kit #242 驗證留言 -->
<p>接下來才是重點：在 Mac mini 上，測試讀到的顏色其實也不對，最多差了 0.128，只是剛好落在 0.16 的上限內。它會通過，靠的是那台螢幕，不是因為它真的量對了色條。</p>
<!-- src S3；{{TBD:242-run}}＝kit #242 合併後的 CI run -->
<p>修正（<a href="https://github.com/redtear1115/mars-dawn-kit/pull/242">kit #242</a>）只改測試：把頁面畫進一張固定使用 sRGB 色彩空間的圖片，完全不經過螢幕。現在兩台機器讀到的色條色差都是 {{TBD:色差，預期 0}}（CI run {{TBD:242-run}}）。為了確認它還抓得到錯，我們把每個預期顏色都改成藍色，五個提示框全部失敗。</p>
<p>它還有一個已知的漏洞：Note 和 Caution 用的兩種橘色只差約 0.119，在 0.16 的上限內，所以這兩個顏色如果對調，測試多半不會發現。我們把這件事記了下來，沒有假裝這個測試已經完整。</p>
<p>我們從中學到的是：一台機器上的綠燈，只代表測試在那台機器上通過，不代表它測的就是名字上寫的那件事。多一個環境，抓到的不只是產品的 bug，也會抓到測試自己的 bug。</p>

<h2>誰來驗，在哪裡驗</h2>
<p><strong>寫改動的 agent 不驗自己的改動。</strong>另開一個 session，只拿到 pull request 和它的驗收清單，拿不到寫的人的思路，而且要自己動手跑。驗 kit #242 時，驗證的 agent 先在 MacBook Air 上跑舊的測試，親眼看它失敗，再在兩台機器上跑新的測試，還故意把預期顏色改錯，確認測試會變紅。上面 Note 和 Caution 的漏洞也是它找到的，它也列出了自己沒驗到的項目。</p>
<!-- src S6, S5: kit ci.yml -->
<p><strong>輸出引擎</strong>（開源的 <a href="https://github.com/redtear1115/mars-dawn-kit">mars-dawn-kit</a>，<code>marsdawn</code> 指令也用它）在 macOS 15 和 macOS 26 上都要跑：前者是它支援的最舊版本，後者是 App 實際出貨的版本。每個版本都要跑 debug 和 release 兩輪，另外還有一組 PDF 樣本，在獨立的行程裡檢查。這要付出時間：單次執行的時間上限從 30 分鐘拉到 45、50，再到 70 分鐘；macOS 15 還曾在測試全部通過的情況下，兩次撞到 50 分鐘的上限。</p>
<!-- src S7, S9: app ci.yml、tools/test.sh（私有） -->
<p><strong>App</strong> 的 CI 跑在我們自己的一台 Mac 上，不簽章。完整的測試還會在兩台 Mac 上手動跑四種組合：簽章與不簽章，各自再分付費牆開與關。因為出貨的版本有付費牆，開發中的版本沒有。</p>
<p><strong>最後由人合併。</strong>沒有任何改動是因為 agent 說「做完了」就進到主分支。</p>

<h2>你也能照做的三個習慣</h2>
<ol>
  <li><strong>寫的 agent 和驗的 agent 分開。</strong>只給驗證的那個改動本身和「怎樣才算完成」，不要給寫的人的說明，請它自己跑測試，並列出沒驗到的地方。不然第二個 agent 很容易變成只負責蓋章。這要多花一個 session 的 token，但比起事後修一個壞掉的改動，還是便宜。</li>
  <li><strong>測試至少在第二個環境跑一次。</strong>沒有第二台 Mac 也沒關係，CI 裡跑兩個 OS 版本，或 debug 和 release 各跑一次，就是不錯的起點。要找的是那些靠運氣才通過的測試。</li>
  <!-- src S7, S8 -->
  <li><strong>「一個測試都沒跑」要算失敗。</strong>Python 3.9 的 <code>unittest</code> 一個測試都沒找到時，還是會回報成功，所以路徑打錯一個字，你照樣拿到綠燈。我們的 CI 會讀測試數量，是 0 就失敗；也會檢查摘要寫的是「0 failed」，不只看結束代碼。第二項檢查，就是之前驗證另一次改動時提出來的。agent 回報「測試全部通過」，其實一個都沒跑，是最常見的假完成之一。</li>
</ol>

<h2>一句話</h2>
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

## Footer label (`ui` dict, `how-we-test`)

| en | zh-Hant |
|---|---|
| How we test | 我們怎麼測試 |

The other six languages (zh-Hans, ja, ko, de, fr, es) come after en and zh-Hant are approved and the TBDs are filled in, so they aren't translated twice.

Co-authored-by: Grok <grok@southern-light.dev>
