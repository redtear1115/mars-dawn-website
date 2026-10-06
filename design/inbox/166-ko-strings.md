# #166 한국어 (ko) — tranche 1: terms, site chrome, 404

Source: English read programmatically from `scripts/build_pages.py` / `scripts/templates_pages.py` / `public/404.html` on `main` @ `6fe8435`; app terms from `MarsDawn/Resources/Localizable.xcstrings` on app `release/1.1.0`. Legal pages are in the sibling files `166-privacy.ko.md` and `166-support.ko.md`.

## 1. Terms checked against the app (release/1.1.0)

| en (app) | ko (app) | xcstrings key |
|---|---|---|
| Window | 윈도우 | `Window` |
| Show Sidebar | 사이드바 보기 | `Show Sidebar` |
| Preview | 미리보기 | `Preview` |
| Editor | 편집기 | `Editor` |
| Source Only | 소스만 | `Source Only` |
| Preview Only | 미리보기만 | `Preview Only` |
| Split | 분할 | `Split` |
| Layout | 레이아웃 | `Layout` |
| Theme | 테마 | `Theme` |
| Preview Theme | 미리보기 테마 | `Preview Theme` |
| Appearance | 화면 모드 | `Appearance` |
| Settings | 설정 | `Settings` |
| Export as PDF… | PDF로 내보내기… | `Export as PDF…` |
| Print… | 프린트… | `Print…` |
| Save As… | 별도 저장… | `Save As…` |
| File | 파일 | `File` |
| View | 보기 | `View` |
| Open Folder… | 폴더 열기… | `Open Folder…` |
| Folder Access | 폴더 접근 | `Folder Access` |
| Grant Folder Access… | 폴더 접근 허용… | `Grant Folder Access…` |
| Load Images | 이미지 불러오기 | `Load Images` |
| Load remote images automatically | 원격 이미지 자동으로 불러오기 | `Load remote images automatically` |
| Notes Folder | 메모 폴더 | `Notes Folder` |
| Run This Document | 이 문서 실행 | `Run This Document` |
| Template | 템플릿 | `Template` |
| Copy for AI | AI용으로 복사 | `Copy for AI` |
| About %@ | %@에 관하여 | `About %@` |
| Start 14-day trial | 14일 체험 시작 | `paywall.button.startTrial` |
| Your free trial has ended | 무료 체험이 종료되었습니다 | `paywall.ended.headline` |
| One-time unlock… | 1회 잠금 해제… | `paywall.button.unlock` |
| Unlock MarsDawn… | MarsDawn 잠금 해제… | `paywall.menu.unlock` |
| MarsDawn is unlocked. Thank you. | MarsDawn이 잠금 해제되었습니다. 감사합니다. | `paywall.settings.unlocked` |
| Restore Purchases | 구입 항목 복원 | `paywall.button.restore` |
| Quick Look | 훑어보기 | in `paywall.ended.body` |
| Shortcuts (app) | 단축어 | in `Notes you add with Siri or Shortcuts go ` |
| trial (noun) | 체험 | in `paywall.unconfirmed.trialNote` |
| subscription | 구독 | in `paywall.unconfirmed.trialNote` |

## 2. Site chrome (`UI`, `STORE_CHIP`, `TRAIT_LINK`, …)

| key | en | ko |
|---|---|---|
| `home` | MarsDawn | MarsDawn |
| `privacy` | Privacy Policy | 개인정보 처리방침 |
| `support` | Support | 지원 |
| `cli` | Command Line | 명령줄 |
| `agents` | marsdawn for agents | 에이전트를 위한 marsdawn |
| `using_cli` | Using the CLI | CLI 사용하기 |
| `markdown-to-pdf` | Markdown to PDF | Markdown을 PDF로 |
| `skill` | Agent skill | 에이전트 스킬 |
| `view-markdown-on-mac` | View Markdown on a Mac | Mac에서 Markdown 보기 |
| `vs-macmd-viewer` | MacMD Viewer vs. MarsDawn | MacMD Viewer와 MarsDawn 비교 |
| `updated` | Last updated {UPDATED} | 최종 업데이트: {UPDATED} |
| `tagline` | Read what your agent wrote. | 에이전트가 쓴 글을 읽으세요. |
| `slogan` | A new dawn for Markdown. | Markdown의 새로운 새벽. |
| `footer_store` | MarsDawn is on the <a href="{LISTING_URL}">Mac App Store</a>. | MarsDawn은 <a href="{LISTING_URL}">Mac App Store</a>에서 구입할 수 있습니다. |
| `footer_nav` | Site | 사이트 |
| `more` | More | 더 보기 |
| `yours` | Your writing stays on your Mac | 내 글은 내 Mac에 |
| `pay-once` | Try free, pay once | 무료로 체험하고, 한 번만 구입 |
| `pdf` | PDF export | PDF 내보내기 |
| `native` | A Mac app | Mac 앱 |
| `limits` | What MarsDawn doesn't do | MarsDawn이 하지 않는 일 |
| `mcp` | MCP server | MCP 서버 |
| `token-efficient-review` | Token-efficient review | 토큰을 아끼는 검토 |
| `vs-markdown-preview-tools` | Viewing Markdown elsewhere vs. MarsDawn | 다른 도구로 Markdown 보기와 MarsDawn 비교 |
| `themes` | Preview themes and PDF export | 미리보기 테마와 PDF 내보내기 |
| `sharing-exported-pdfs` | Sharing exported PDFs | 내보낸 PDF 공유하기 |
| `reviewing-ai-output` | Why AI output still needs a human reader | AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유 |
| `reading-agent-output` | Reading what your agent hands back | 에이전트가 돌려준 결과 읽기 |
| `agent-transparency` | Agent transparency | 에이전트의 투명성 |
| `reviewing-agent-plans` | Reviewing an agent plan | 에이전트의 계획 검토하기 |
| `agent-design-patterns` | Agent design patterns | 에이전트 설계 패턴 |
| `changelog` | Changelog | 변경 내역 |
| `consent_text` | This site uses analytics cookies to see how visitors use it. They stay off unless you accept. | 이 사이트는 방문자가 사이트를 어떻게 이용하는지 파악하기 위해 분석 쿠키를 사용합니다. 수락하지 않으면 이 쿠키는 꺼진 상태로 유지됩니다. |
| `consent_accept` | Accept | 수락 |
| `consent_decline` | Decline | 거부 |
| `consent_aria` | Cookie consent | 쿠키 동의 |
| `cookie_settings` | Cookie settings | 쿠키 설정 |
| `view_markdown_source` | View the Markdown source | Markdown 소스 보기 |
| `templates` | Templates | 템플릿 |
| `templates-spec` | Spec template | 명세서 템플릿 |
| `templates-flowchart` | Flowchart template | 순서도 템플릿 |
| `templates-meeting-notes` | Meeting notes template | 회의록 템플릿 |
| `STORE_CHIP` | On the Mac App Store | Mac App Store에서 판매 중 |
| `TRAIT_LINK.yours` title | Your writing stays on your Mac | 내 글은 내 Mac에 |
| `TRAIT_LINK.yours` line | No account, no sync, no cloud. | 계정도, 동기화도, 클라우드도 없습니다. |
| `TRAIT_LINK.pay-once` title | Try free, pay once | 무료로 체험하고, 한 번만 구입 |
| `TRAIT_LINK.pay-once` line | Free for 14 days, then USD 4.99 once. No subscription. | 14일 무료, 이후 USD 4.99 1회 구입. 구독이 아닙니다. |
| `TRAIT_LINK.pdf` title | PDF export | PDF 내보내기 |
| `TRAIT_LINK.pdf` line | Diagrams, highlighted code, careful page breaks. | 다이어그램, 코드 하이라이트, 세심한 페이지 나눔. |
| `TRAIT_LINK.native` title | A Mac app | Mac 앱 |
| `TRAIT_LINK.native` line | Native windows, tabs, autosave, Quick Look. | 네이티브 윈도우와 탭, 자동 저장, 훑어보기. |
| `TRAIT_LINK.limits` title | What MarsDawn doesn't do | MarsDawn이 하지 않는 일 |
| `TRAIT_LINK.limits` line | Know before you buy. | 구입 전에 알아 둘 점. |
| `TRAIT_NAV_HEADING` | What to expect from MarsDawn | MarsDawn에서 기대할 수 있는 것 |
| `FIGURE_LIST_LABEL` | In this screenshot | 이 스크린샷의 내용 |
| `SKIP_LABEL` | Skip to content | 본문으로 건너뛰기 |
| `TOC_LABEL.privacy` | On this page | 이 페이지의 내용 |
| `TOC_LABEL.support` | Jump to a question | 질문으로 이동 |
| `LOCALES.label` | English | 한국어 |
| `html_lang` / `OG_LOCALE` | en / en_US | ko / ko_KR |

## 3. 404 page (`public/404.html`)

| element | en | ko |
|---|---|---|
| title | Page not found · MarsDawn | 페이지를 찾을 수 없음 · MarsDawn |
| h1 | Lost among the stars. | 별들 사이에서 길을 잃었습니다. |
| body | This path isn’t on the map. A quiet neighbor pointed the way home. | 이 길은 지도에 없습니다. 조용한 이웃이 집으로 가는 길을 가리켜 주었습니다. |
| back | Back to MarsDawn | MarsDawn으로 돌아가기 |
| alt | A small craft drifts in a Martian dawn sky while a friendly alien points toward the planet’s bright limb. | 화성의 새벽하늘에 작은 우주선이 떠 있고, 친근한 외계인이 행성의 밝은 가장자리를 가리키고 있습니다. |
| aria_language | Language | 언어 |
| aria_site | Site | 사이트 |

## 4. Paste-ready for `copy_ko.py` (same shape as `copy_ja.py`)

```python
    ui = {'home': 'MarsDawn', 'privacy': '개인정보 처리방침', 'support': '지원', 'cli': '명령줄', 'agents': '에이전트를 위한 marsdawn', 'using_cli': 'CLI 사용하기', 'markdown-to-pdf': 'Markdown을 PDF로', 'skill': '에이전트 스킬', 'view-markdown-on-mac': 'Mac에서 Markdown 보기', 'vs-macmd-viewer': 'MacMD Viewer와 MarsDawn 비교', 'updated': f'최종 업데이트: {k.UPDATED}', 'tagline': '에이전트가 쓴 글을 읽으세요.', 'slogan': 'Markdown의 새로운 새벽.', 'footer_store': f'MarsDawn은 <a href="{k.LISTING_URL}">Mac App Store</a>에서 구입할 수 있습니다.', 'footer_nav': '사이트', 'more': '더 보기', 'yours': '내 글은 내 Mac에', 'pay-once': '무료로 체험하고, 한 번만 구입', 'pdf': 'PDF 내보내기', 'native': 'Mac 앱', 'limits': 'MarsDawn이 하지 않는 일', 'mcp': 'MCP 서버', 'token-efficient-review': '토큰을 아끼는 검토', 'vs-markdown-preview-tools': '다른 도구로 Markdown 보기와 MarsDawn 비교', 'themes': '미리보기 테마와 PDF 내보내기', 'sharing-exported-pdfs': '내보낸 PDF 공유하기', 'reviewing-ai-output': 'AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유', 'reading-agent-output': '에이전트가 돌려준 결과 읽기', 'agent-transparency': '에이전트의 투명성', 'reviewing-agent-plans': '에이전트의 계획 검토하기', 'agent-design-patterns': '에이전트 설계 패턴', 'changelog': '변경 내역', 'consent_text': '이 사이트는 방문자가 사이트를 어떻게 이용하는지 파악하기 위해 분석 쿠키를 사용합니다. 수락하지 않으면 이 쿠키는 꺼진 상태로 유지됩니다.', 'consent_accept': '수락', 'consent_decline': '거부', 'consent_aria': '쿠키 동의', 'cookie_settings': '쿠키 설정', 'view_markdown_source': 'Markdown 소스 보기'}
    store_chip = 'Mac App Store에서 판매 중'
    trait_link = {'yours': ('내 글은 내 Mac에', '계정도, 동기화도, 클라우드도 없습니다.'), 'pay-once': ('무료로 체험하고, 한 번만 구입', '14일 무료, 이후 USD 4.99 1회 구입. 구독이 아닙니다.'), 'pdf': ('PDF 내보내기', '다이어그램, 코드 하이라이트, 세심한 페이지 나눔.'), 'native': ('Mac 앱', '네이티브 윈도우와 탭, 자동 저장, 훑어보기.'), 'limits': ('MarsDawn이 하지 않는 일', '구입 전에 알아 둘 점.')}
    trait_nav_heading = 'MarsDawn에서 기대할 수 있는 것'
    figure_list_label = '이 스크린샷의 내용'
    # templates_pages.py UI entries
    templates_ui = {'templates': '템플릿', 'templates-spec': '명세서 템플릿', 'templates-flowchart': '순서도 템플릿', 'templates-meeting-notes': '회의록 템플릿'}
```

Co-authored-by: Grok <grok@southern-light.dev>
