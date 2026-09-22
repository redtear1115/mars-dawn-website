# #70 copy: the website section of the privacy policy

Four locales. Replace the opening paragraph, insert the section under it, and replace the children paragraph. Slots in `{{ }}` are owner fills; see `70-analytics-README.md`.

## en

Opening, replaces the current bold paragraph:

**The MarsDawn app does not collect any data about you.** There is no account, no advertising and no tracking. Your documents and settings stay on your Mac.

New section, directly under that paragraph:

## The website

The app and this website are two different things. The app collects nothing. A visit can be recorded only here, on marsdawn.southern-light.dev.

**This is not on yet.** This website sends nothing to an analytics service today. The list below is what it will record once that is switched on. It is published now so the description is already public before the first event. On the day it is switched on, delete this paragraph and leave the list.

Once it is on:

- **Page views.** The server records that a page was requested, and the referring address when the browser sends one.
- **Clicks that leave through this site.** A click that goes out through a redirect on this site, such as the link to the Mac App Store, is recorded. The destination is a fixed address, and the redirect adds no tracking parameters.
- **What is not recorded.** No cookies, no local storage, and no analytics script in the page. No account, because the site has none. No document, and nothing you type. No cross-site advertising, and no profile of you. Requests the app makes for theme files under `/themes/` are skipped, and are not sent on.
- **A visit is only a page view.** Each request is given a new random id, used for that request and not again. The site cannot recognise you on a later visit.
- **Where it goes.** The site's own server sends these events to PostHog, in the {{POSTHOG_REGION}} region. Your browser does not contact PostHog. PostHog keeps the events for {{RETENTION}}. The full IP address is not forwarded.
- **The host.** Cloudflare hosts the site and, like any host, sees your IP address while it answers the request. That log belongs to the host. It is not the analytics above.

Children, replaces the current sentence:

The MarsDawn app does not collect data from anyone, including children. A visit recorded on the website is not an account, and it is not used to identify anyone.

## zh-Hant

Opening:

**MarsDawn app 不收集任何關於你的資料。**沒有帳號、沒有廣告，也不追蹤。你的文件與設定都留在你的 Mac 上。

New section:

## 這個網站

App 和這個網站是兩件事。App 不收集資料。會記下造訪的，只有 marsdawn.southern-light.dev。

**目前還沒有開啟。**這個網站今天不會把任何東西送到分析服務。下面是開啟之後會記錄的內容，先寫在這裡，讓第一筆記錄出現之前，說明就已經公開。開啟的那天，刪掉這一段，其餘留下。

開啟之後：

- **頁面瀏覽。**伺服器會記錄某個頁面被請求，以及瀏覽器有送出來源網址時的那個網址。
- **經由本站轉出去的點擊。**經由本站轉址才離開的點擊會被記錄，例如前往 Mac App Store 的連結。目的地是固定網址，轉址不會附加追蹤參數。
- **不會記錄的。**沒有 cookie，也不使用瀏覽器的本地儲存，頁面裡沒有分析程式。沒有帳號，因為這個網站不需要帳號。沒有你的文件，也沒有你打的字。沒有跨站廣告，也不會建立你的個人檔案。App 向 `/themes/` 索取主題檔案的請求會被略過，不會送出。
- **一次造訪只是一次瀏覽。**每個請求配一組只用一次的隨機編號，用完即棄。網站無法在你下次來時認出你。
- **資料去哪裡。**這些事件由網站自己的伺服器送給 PostHog（{{POSTHOG_REGION}} 區）。你的瀏覽器不會連到 PostHog。PostHog 會把這些事件保留 {{RETENTION}}。完整的 IP 位址不會轉送過去。
- **主機。**網站放在 Cloudflare。和任何主機一樣，它在回應請求時會看到你的 IP 位址。那是主機自己的日誌，不是上面的分析。

兒童:

MarsDawn app 不向任何人收集資料，包括兒童。網站上記下的造訪不是帳號，也不用來辨認任何人。

## zh-Hans

Opening:

**MarsDawn app 不收集任何关于你的数据。**没有账户、没有广告，也不追踪。你的文稿与设置都留在你的 Mac 上。

New section:

## 这个网站

App 和这个网站是两件事。App 不收集数据。会记下访问的，只有 marsdawn.southern-light.dev。

**目前还没有开启。**这个网站今天不会把任何东西送到分析服务。下面是开启之后会记录的内容，先写在这里，让第一笔记录出现之前，说明就已经公开。开启的那天，删掉这一段，其余留下。

开启之后：

- **页面浏览。**服务器会记录某个页面被请求，以及浏览器有送来源网址时的那个网址。
- **经由本站转出去的点击。**经由本站跳转才离开的点击会被记录，例如前往 Mac App Store 的链接。目的地是固定网址，跳转不会附加追踪参数。
- **不会记录的。**没有 cookie，也不使用浏览器的本地存储，页面里没有分析脚本。没有账户，因为这个网站不需要账户。没有你的文稿，也没有你打的字。没有跨站广告，也不会建立你的个人档案。App 向 `/themes/` 索取主题文件的请求会被跳过，不会送出。
- **一次访问只是一次浏览。**每个请求配一组只用一次的随机编号，用完即弃。网站无法在你下次来时认出你。
- **数据去哪里。**这些事件由网站自己的服务器送给 PostHog（{{POSTHOG_REGION}} 区）。你的浏览器不会连到 PostHog。PostHog 会将这些事件保留 {{RETENTION}}。完整的 IP 地址不会转发过去。
- **主机。**网站放在 Cloudflare 上。和任何主机一样，它在响应请求时会看到你的 IP 地址。那是主机自己的日志，不是上面的分析。

儿童:

MarsDawn app 不向任何人收集数据，包括儿童。网站上记下的访问不是账户，也不用来辨认任何人。

## ja

Opening:

**MarsDawn アプリは、あなたに関するデータを一切収集しません。**アカウントも、広告も、トラッキングもありません。文書と設定はあなたの Mac 上に残ります。

New section:

## このウェブサイト

アプリとこのウェブサイトは別のものです。アプリはデータを収集しません。訪問が記録され得るのは、marsdawn.southern-light.dev だけです。

**まだ有効になっていません。**このウェブサイトは、今日はアナリティクスのサービスへ何も送りません。以下は、有効にしたあとに記録する内容です。最初の記録より前に公開しておくため、ここに書いてあります。有効にする日にはこの段落だけを削除し、リストは残します。

有効にしたあと：

- **ページの閲覧。**サーバーは、ページがリクエストされたことと、ブラウザが参照元のアドレスを送った場合はそのアドレスを記録します。
- **このサイト経由で外へ出るクリック。**このサイト上のリダイレクトを通って離れるクリックを記録します。Mac App Store へのリンクがその例です。行き先は固定のアドレスで、リダイレクトにトラッキング用のパラメータは付きません。
- **記録しないもの。**Cookie も、ブラウザのローカルストレージも、ページ内のアナリティクス用スクリプトもありません。アカウントはありません。このサイトにアカウント機能がないためです。文書も、入力した文字も記録しません。サイトをまたいだ広告もなく、あなたのプロフィールも作りません。アプリが `/themes/` 以下のテーマファイルを取りに行くリクエストは対象外で、送られません。
- **訪問はページの閲覧でしかありません。**リクエストごとに新しいランダムな番号を一つ割り当て、そのリクエストにだけ使い、再利用しません。次に訪れたときに、あなただと分かることはありません。
- **どこへ送られるか。**これらのイベントは、このサイト自身のサーバーから PostHog（{{POSTHOG_REGION}} リージョン）へ送られます。ブラウザが PostHog に接続することはありません。PostHog の保持期間は {{RETENTION}} です。完全な IP アドレスは転送しません。
- **ホスティング。**サイトは Cloudflare 上にあります。どのホストとも同じく、リクエストに応答する間は IP アドレスを見ます。それはホスト自身のログであり、上のアナリティクスではありません。

子ども:

MarsDawn アプリは、子どもを含め、誰からもデータを収集しません。ウェブサイトに記録される訪問はアカウントではなく、誰かを識別するためにも使いません。
