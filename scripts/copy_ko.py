"""Korean copy for the MarsDawn site (#166, tracking #168), integrated for #162's plumbing.

The text is Grok's, from draft PR #173 (design/inbox/166-ko-pages.py and 166-ko-strings.md),
carried over unchanged; only the return shape is the plumbing's (see scripts/new_locale.py). Written
here and not in Grok's material: the privacy page's description, the hero window's label and its
Markdown-twin sentence. The privacy and support titles are the legal pages' own h1. Legal pages:
content/legal/<slug>.ko.md.
"""

# True: the build checks the shape, the legal pages, the hero snapshot and the images before it serves the locale.
COMPLETE = True


def build(k) -> dict:
    pages = {}
    pages['index'] = {
        "title": 'MarsDawn: 실시간 미리보기가 있는 Mac용 Markdown 편집기',
        "description": '에이전트의 작업을 이끄는 사람을 위한 Markdown. 실시간 미리보기, Mermaid 다이어그램, PDF 내보내기를 갖춘 Mac 네이티브 편집기입니다. Mac App Store에서 구입할 수 있습니다.',
        "intro": """
<section class="intro hero">
  <p class="kicker">만드는 사람을 위한 개척자의 도구</p>
  <h1><span>지도를 손에 쥐세요.</span> <span>새벽을 읽으세요.</span></h1>
  <p>에이전트의 작업을 이끄는 사람을 위한 Markdown.</p>
</section>
""",
        "body": """
<h2 class="loop-title">에이전트가 쓴 글을 읽으세요.</h2>
<ol class="loop-steps">
  <li><strong>에이전트가 씁니다.</strong> 코딩 에이전트나 글쓰기 도우미가 README, 명세서, 메모 같은 Markdown 초안을 작성합니다.</li>
  <li><strong>MarsDawn에서 검토합니다.</strong> 파일을 열고, Mermaid 다이어그램과 하이라이트된 코드까지 렌더링된 페이지를 소스 옆에 두고 읽으세요.</li>
  <li><strong>에이전트가 고칩니다.</strong> 수정을 요청하세요. 고친 파일을 열어 같은 방식으로 읽으면 됩니다.</li>
</ol>
<p><a href="/ko/reading-agent-output/">에이전트가 돌려준 결과를 검토하는 방법</a>.</p>
""",
    }
    pages['yours'] = {
        "title": '계정도 클라우드도 없는 Mac용 Markdown 편집기 · MarsDawn',
        "description": 'MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.',
        "intro": """
<section class="intro">
  <h1>내 글은 내 Mac에 남습니다.</h1>
  <p>MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. 파일을 열고, 글을 쓰면, 고른 위치에 파일을 저장합니다.</p>
</section>
""",
        "body": """
<h2>무슨 뜻인가요</h2>
<ul>
  <li>가입하거나 로그인할 계정이 없습니다.</li>
  <li>클라우드로 동기화되는 것이 없습니다. 문서는 저장한 곳에 그대로 있습니다.</li>
  <li>추적하지 않습니다. MarsDawn은 사용자에 관한 데이터를 일절 수집하지 않으며, App Store 개인정보 보호 라벨도 ‘데이터가 수집되지 않음’입니다.</li>
  <li>웹 이미지는 불러오기로 선택할 때까지 차단되므로, 문서를 연다고 해서 어떤 서버도 내가 그 문서를 읽는다는 사실을 알 수 없습니다. 불러올 때도 https로만 불러옵니다.</li>
  <li>로컬 이미지는 해당 폴더에 대한 접근을 허용하면 미리보기에 표시됩니다.</li>
</ul>
<p>자세한 내용은 <a href="/ko/privacy/">개인정보 처리방침</a>에 있습니다.</p>
""",
    }
    pages['pay-once'] = {
        "title": '무료로 체험하고, 한 번만 구입하세요 · MarsDawn',
        "description": 'MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.',
        "intro": """
<section class="intro">
  <h1>전부 써 보세요. 그다음 한 번만 구입하세요.</h1>
  <p>MarsDawn은 무료로 다운로드할 수 있습니다. 14일 체험을 시작하면 모든 기능을 쓸 수 있고, 그 후에도 계속 쓰려면 USD 4.99 한 번 구입으로 잠금 해제됩니다. 구독도, 계정도 없습니다.</p>
</section>
""",
        "body": """
<h2>이렇게 진행됩니다</h2>
<ol class="loop-steps">
  <li><strong>무료로 다운로드하세요.</strong> MarsDawn은 Mac App Store에서 무료로 다운로드할 수 있습니다.</li>
  <li><strong>14일 동안 전부 체험하세요.</strong> 체험을 시작하면 14일 동안 MarsDawn의 모든 기능이 작동합니다. 모든 테마와 레이아웃, PDF 내보내기와 프린트, Siri 및 단축어 동작까지 포함됩니다. Finder의 훑어보기는 체험 여부와 관계없이 작동합니다.</li>
  <li><strong>한 번만 잠금 해제하세요.</strong> 그 후에도 계속 쓰려면 USD 4.99에 한 번만 잠금 해제하세요. 구독이 아닌 앱 내 구입이므로, 갱신되는 것도 나중에 청구되는 것도 없습니다.</li>
</ol>
<ul>
  <li>체험에도 요금이 청구되지 않습니다. 체험이 끝나도 잠금 해제를 선택하지 않는 한 아무것도 구입되지 않습니다.</li>
  <li>계정이 없습니다. MarsDawn은 계정을 만들라고 요구하지 않습니다.</li>
</ul>
<h2>단계별로 쓸 수 있는 기능</h2>
<!--compare:pay-once-states-->
<p>체험을 시작하기 전에는 MarsDawn이 체험 안내를 보여줍니다. 체험을 시작하는 데는 비용이 들지 않습니다.</p>
<p>MarsDawn에서 연 PDF 파일도 체험이 끝나면 같은 방식으로 잠깁니다.</p>
<h2>잠금 해제하지 않으면</h2>
<ul>
  <li>14일이 지나면 잠금 해제하기 전까지 MarsDawn에서 문서를 읽거나 편집하거나 내보내거나 프린트할 수 없습니다. 문서는 열리지만 내용이 가려집니다.</li>
  <li>파일은 바뀌지 않습니다. Mac에 있는 평범한 파일이고, Finder의 훑어보기에서 계속 볼 수 있습니다.</li>
  <li>무료 <a href="/ko/cli/"><code>marsdawn</code> 명령줄 도구</a>는 체험 여부와 관계없이 계속 PDF로 내보낼 수 있습니다.</li>
  <li>체험이 끝날 때 MarsDawn에 문서가 열려 있었다면 입력한 텍스트는 사라지지 않습니다. 파일 ▸ 별도 저장…으로 저장하세요.</li>
</ul>
""",
    }
    pages['pdf'] = {
        "title": 'Mac에서 Markdown을 PDF로 내보내기, 다이어그램까지 · MarsDawn',
        "description": 'Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록과 표를 가르지 않도록 합니다.',
        "intro": """
<section class="intro">
  <h1>PDF가 내가 쓴 페이지 그대로 보입니다.</h1>
  <p>테마의 라이트 색상으로 PDF로 내보내거나 프린트하세요. 다이어그램과 하이라이트된 코드가 그대로 담기고, 페이지 나눔은 함께 있어야 할 것을 떼어 놓지 않습니다.</p>
</section>
""",
        "body": """
<h2>무슨 뜻인가요</h2>
<ul>
  <li>Mermaid 다이어그램이 PDF 안에 그려집니다.</li>
  <li>코드 블록은 구문 하이라이트를 유지합니다.</li>
  <li>페이지 나눔은 제목이 페이지 맨 아래에 홀로 남거나 코드, 표, 다이어그램이 갈라지지 않도록 합니다.</li>
  <li>어떤 레이아웃에서든 됩니다. 소스만 보이는 상태에서도 내보낼 수 있습니다.</li>
</ul>
<p>무료 <a href="/ko/cli/">marsdawn 명령줄 도구</a>도 같은 내보내기 엔진을 쓰므로, 스크립트나 AI 에이전트도 같은 PDF를 얻습니다.</p>
""",
    }
    pages['native'] = {
        "title": 'Mac 네이티브 Markdown 앱: 탭, 훑어보기 · MarsDawn',
        "description": '진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.',
        "intro": """
<section class="intro">
  <h1>Mac의 부품으로 만들었습니다.</h1>
  <p>윈도우, 탭, 메뉴, 텍스트 편집기는 모두 Mac의 것입니다. 렌더링된 페이지는 Safari의 엔진인 WebKit이 그립니다.</p>
</section>
""",
        "body": """
<h2>무슨 뜻인가요</h2>
<h3>편집</h3>
<ul>
  <li>소스, 분할, 미리보기 레이아웃을 키 하나로 오갑니다(<kbd>⌘1</kbd>, <kbd>⌘2</kbd>, <kbd>⌘3</kbd>).</li>
  <li>두 패널이 함께 스크롤되어, 편집 중인 문단이 계속 화면에 보입니다.</li>
  <li>편집기의 Markdown 구문 하이라이트는 미리보기 테마에 맞춰집니다.</li>
</ul>
<h3>나머지도 Mac 그대로</h3>
<ul>
  <li>네이티브 윈도우와 탭, 자동 저장, 버전 기록.</li>
  <li>훑어보기: Finder에서 Markdown 파일을 선택하고 스페이스 바를 누르면 다이어그램까지 포함된 미리보기가 나타납니다.</li>
  <li>Siri와 단축어: 템플릿으로 새로운 문서를 시작하거나, 메모 수신함에 한 줄을 추가하거나, 최근 문서를 다시 열 수 있습니다.</li>
  <li>영어, 중국어(번체), 중국어(간체), 일본어, 독일어, 프랑스어, 스페인어, 한국어.</li>
</ul>
""",
    }
    pages['limits'] = {
        "title": 'MarsDawn이 하지 않는 일 · MarsDawn',
        "description": '동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지입니다. 구입 전에 알아 두세요.',
        "intro": """
<section class="intro">
  <h1>MarsDawn이 하지 않는 일.</h1>
  <p>일부러 넣지 않은 것들이 있습니다. 그중 필요한 것이 있다면, 구입한 뒤보다 지금 아는 편이 낫습니다.</p>
</section>
""",
        "body": """
<h2>넣지 않은 것</h2>
<h3>기기와 사람</h3>
<ul>
  <li><strong>동기화:</strong> MarsDawn은 문서를 동기화하지 않습니다. 문서는 저장한 곳에 있으므로, 다른 Mac에서 쓰려면 이미 동기화하고 있는 폴더에 두세요.</li>
  <li><strong>iPhone과 iPad:</strong> 이들을 위한 앱은 없습니다. MarsDawn은 Mac용입니다.</li>
  <li><strong>공유:</strong> MarsDawn은 자기 Mac을 쓰는 한 사람을 위한 앱이라 계정도 공동 편집도 없습니다.</li>
  <li><strong>시스템:</strong> MarsDawn은 macOS 26 이상이 필요합니다.</li>
</ul>
<h3>파일과 기능</h3>
<ul>
  <li><strong>편집:</strong> 왼쪽에서 Markdown을 쓰고 오른쪽에서 페이지를 읽습니다. 페이지 자체는 편집할 수 없습니다.</li>
  <li><strong>형식:</strong> MarsDawn은 PDF로 내보내고 프린트할 수 있지만, Word 파일로는 내보내지 않습니다.</li>
  <li><strong>기타 파일:</strong> 일반 텍스트 파일과 PDF는 읽기 전용으로 열립니다.</li>
  <li><strong>테마:</strong> 새벽, 클래식, 모던, 비비드가 각각 라이트와 다크로 들어 있으며, 아직 다른 테마는 설치할 수 없습니다. 계획은 <a href="/ko/themes/">미리보기 테마와 PDF 내보내기</a>에서 확인하세요.</li>
  <li><strong>플러그인:</strong> MarsDawn에는 플러그인이나 확장 기능이 없습니다.</li>
</ul>
<h2>체험이 끝난 뒤</h2>
<p>14일 체험이 끝난 뒤 MarsDawn을 잠금 해제하지 않으면, MarsDawn에서 문서를 읽거나 편집하거나 내보내거나 프린트할 수 없습니다. 문서는 내용이 가려진 채로 열립니다. 파일은 그대로이고, 훑어보기로 계속 볼 수 있으며, 무료 명령줄 도구로 계속 내보낼 수 있습니다. <a href="/ko/pay-once/">체험과 잠금 해제 페이지</a>에서 세 단계를 나란히 비교해 보세요.</p>
""",
    }
    pages['changelog'] = {
        "title": '변경 내역 · MarsDawn',
        "description": '무료 marsdawn 명령줄 도구에서 바뀐 점입니다.',
        "body": """
<section class="intro">
  <h1>변경 내역</h1>
  <p>무료 marsdawn 명령줄 도구에서 바뀐 점입니다. Mac App Store의 MarsDawn 빌드는 따로 적을 내용이 있을 때만 여기에 언급합니다. 0.5.1 이전 버전은 싣지 않았습니다.</p>
</section>

<h2>marsdawn 0.6.3</h2>
<p>2026년 10월 6일. MarsDawn이 Mac App Store에 출시되었습니다.</p>
<ul>
  <li>앱이 설치되어 있지 않으면 <code>marsdawn open</code>이 Mac App Store의 MarsDawn을 안내합니다.</li>
  <li>README와 에이전트 스킬에서 <code>marsdawn open .</code>과 <code>--folder</code> 사용법을 안내합니다. MarsDawn 1.0.0은 윈도우의 사이드바에 폴더를 보여줍니다.</li>
</ul>

<h2>marsdawn 0.5.4</h2>
<p>2026년 9월 26일. Mermaid 수정, 다이어그램 오류의 줄 번호, 스킬 설치.</p>
<ul>
  <li>시퀀스 다이어그램에서 다른 참여자의 생명선을 가로지르는 메시지 레이블이 미리보기와 내보낸 PDF 모두에서 읽기 쉽게 유지됩니다.</li>
  <li><code>marsdawn export</code>가 Mermaid 다이어그램이 가득한 문서도 처리합니다. 예전에는 종료 코드 5로 실패하던 다이어그램 50개짜리 문서도 이제 내보내집니다.</li>
  <li><code>marsdawn export --json</code>에 <code>diagramErrorDetails</code>가 추가되어 다이어그램 오류마다 줄 번호를 알려줍니다. 문서에서 다이어그램이 시작하는 위치와, Mermaid가 지목하는 경우 오류가 난 줄 자체입니다.</li>
  <li><code>marsdawn skill --install</code>은 Claude Code용 에이전트 스킬을 <code>~/.claude/skills/marsdawn/SKILL.md</code>에, 또는 <code>--dir</code>로 지정한 다른 폴더에 설치합니다. 같은 파일이 있으면 그대로 두고, 다른 파일은 <code>--force</code>를 줄 때만 바꿉니다. 그렇지 않으면 종료 코드 64(<code>skill_differs</code>)로 끝나며 아무것도 바꾸지 않습니다.</li>
</ul>

<h2>marsdawn 0.5.3</h2>
<p>2026년 9월 25일. 폴더 상태, Mermaid 오류 전문, 작은 수정들.</p>
<ul>
  <li><code>marsdawn open --folder</code>가 폴더에 어떤 일이 있었는지 알려줄 수 있습니다. 응답을 보내는 앱이라면 최대 <code>--wait</code>초(기본값 2초) 동안 기다리고, <code>--json</code>은 <code>attached</code>나 <code>needsUser</code> 같은 상태를 돌려줍니다.</li>
  <li>파싱되지 않는 Mermaid 다이어그램은 오류 메시지의 첫 줄만이 아니라 Mermaid의 오류 메시지 전체를 보여주며, 줄 번호는 문서 맨 위부터 셉니다.</li>
  <li>프런트 매터 블록의 끝을 찾는 검색이 1,000줄에서 멈추므로, 닫히지 않은 블록 때문에 큰 문서의 나머지를 끝까지 훑는 일이 더는 없습니다.</li>
  <li>앱이 PDF 내보내기와 프린트용으로 각주 되돌아가기 링크에 번역된 레이블을 붙일 수 있습니다. 이 레이블은 페이지에 인쇄되지 않으며, <code>marsdawn export</code>는 영어 레이블을 유지합니다.</li>
  <li>함께 들어 있는 highlight.js가 이제 KaTeX, Mermaid처럼 버전, 출처, SHA-256으로 고정됩니다.</li>
</ul>

<h2>marsdawn 0.5.2</h2>
<p>2026년 9월 24일. 각주, 대비, 폴더.</p>
<ul>
  <li>내보낸 PDF에 각주가 표시됩니다. 번호가 붙은 참조가 들어가고, 주석은 본문 뒤에 옵니다.</li>
  <li>모든 테마가 라이트와 다크 모두에서 WCAG AA 대비 기준을 충족합니다. 클래식은 이제 흑백입니다.</li>
  <li><code>marsdawn skill</code>은 설치된 marsdawn에 맞는 에이전트 스킬을 출력합니다.</li>
  <li><code>marsdawn open</code>은 찾은 MarsDawn이 폴더를 보여줄 수 없을 때 성공을 보고하는 대신 종료 코드 6(<code>app_cannot_open_folders</code>)으로 끝납니다.</li>
  <li>내보낸 페이지에 그려지는 자리 표시자가 독일어, 프랑스어, 스페인어, 한국어로도 나옵니다.</li>
  <li>이미지 자리 표시자가 아주 긴 상대 경로 뒤에 있는 절대 경로를 더는 보여주지 않습니다.</li>
  <li><code>MARSDAWN_APP_PATH</code>는 MarsDawn 앱을 가리킬 때만 사용됩니다.</li>
</ul>

<h2>marsdawn 0.5.1</h2>
<p>2026년 9월 19일. PDF 내보내기와 명령줄에서 파일 열기.</p>
<ul>
  <li>내보낸 PDF의 텍스트 레이어가 중국어, 일본어, 한국어에서 바르게 고쳐졌습니다.</li>
  <li><code>marsdawn open --background</code>는 MarsDawn을 앞으로 가져오지 않고 파일을 엽니다.</li>
  <li><code>marsdawn open</code>에 폴더를 줄 수 있으며, MarsDawn이 그 폴더를 윈도우의 사이드바에 보여줍니다(MarsDawn 1.0.0 이상).</li>
</ul>
""",
    }
    pages['cli'] = {
        "title": 'marsdawn: Markdown을 PDF로 바꾸는 무료 명령줄 도구 · MarsDawn',
        "description": 'Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.',
        "body": f"""
<section class="intro">
  <h1>명령줄</h1>
  <p>무료 <code>marsdawn</code> 명령줄 도구입니다. 셸이나 LLM 에이전트에서 Markdown을 PDF로 내보내고, MarsDawn 앱이 설치되어 있으면 앱에서 파일을 열 수 있습니다.</p>
</section>

<div class="summary"><p><strong>marsdawn은 무료이며 Mac App Store와 별도로 배포됩니다.</strong> Homebrew로 설치하세요. Apple 실리콘 Mac에서는 바로 실행할 수 있는 상태로 설치됩니다. <code>export</code>는 단독으로 작동하고, <code>open</code>은 MarsDawn 앱이 필요합니다.</p></div>

<p>AI 에이전트나 스크립트에서 marsdawn을 호출하나요? JSON 출력과 스키마, 모든 종료 코드는 <a href="/ko/cli/agents/">에이전트를 위한 marsdawn</a>에서, 에이전트가 MCP로 도구를 호출한다면 <a href="/ko/cli/mcp/">MCP 서버</a>에서 확인하세요.</p>

<h2>설치</h2>
<p><a href="https://brew.sh">Homebrew</a>를 사용하는 경우:</p>
<pre><code>{k.BREW_TAP_INSTALL}</code></pre>
<p>코딩 에이전트를 쓰고 있나요? <a href="/ko/cli/skill/">marsdawn 스킬을 추가하세요</a>. 파일 하나로, 에이전트가 자기가 쓴 것을 MarsDawn에서 열어 검토를 받고 PDF로 내보내는 법을 익힙니다.</p>
<p>Apple 실리콘 Mac에서는 Homebrew가 미리 빌드된 버전을 몇 초 만에 설치하며, 따로 설치할 것이 없습니다. Intel Mac에서는 대신 소스에서 marsdawn을 빌드하므로 몇 분이 걸리고 Xcode 26 이상(Swift 6.2)이 필요합니다. 이 도구는 macOS 15 이상에서 실행됩니다.</p>
<p>또는 Swift Package Manager로 <a href="{k.KIT_URL}">소스</a>에서 빌드하세요.</p>
<pre><code>git clone {k.KIT_URL}.git
cd mars-dawn-kit
swift build -c release --product marsdawn</code></pre>
<p>설치된 버전은 <code>marsdawn --version</code>으로 확인할 수 있습니다.</p>

<h2>명령</h2>

<h3>marsdawn open</h3>
<p>Markdown 파일 하나 이상을 MarsDawn 앱에서 열어 검토할 수 있게 합니다. 앱이 설치되어 있어야 합니다. 앱이 없으면 <code>marsdawn open</code>은 코드 3으로 종료하며 MarsDawn이 설치되어 있지 않다고 알립니다. <code>export</code>는 앱이 필요 없습니다. 앱은 <a href="{k.LISTING_URL}">Mac App Store</a>에 있습니다.</p>
<pre><code>marsdawn open notes.md
marsdawn open notes.md:120
marsdawn open notes.md --line 120
marsdawn open .
marsdawn open notes.md --folder .</code></pre>
<ul>
  <li><code>path:line</code>: MarsDawn에 해당 줄로 이동하도록 요청합니다. <code>notes.md:120:8</code>처럼 뒤에 붙은 열 번호는 무시됩니다. 전체 이름 그대로의 파일이 있으면 인수는 그 파일을 가리킵니다.</li>
  <li><code>--line &lt;n&gt;</code>: 파일 하나에 대해 같은 일을 하며, 경로 자체가 콜론과 숫자로 끝날 때 줄을 지정하는 방법입니다. 파일이 정확히 하나여야 합니다.</li>
  <li>줄 번호는 1부터 999999999까지입니다.</li>
  <li>MarsDawn 1.0은 해당 줄에서 파일을 엽니다.</li>
  <li>폴더를 인수로 주면 문서가 아니라 윈도우의 사이드바에 열립니다. <code>marsdawn open .</code>은 현재 폴더를 보여줍니다. <code>--folder &lt;path&gt;</code>는 파일과 함께 같은 일을 합니다. 윈도우의 사이드바는 폴더 하나만 보여주므로, 두 개를 지정하면 사용법 오류입니다.</li>
  <li><code>--background</code>: MarsDawn을 앞으로 가져오지 않고 엽니다.</li>
  <li><code>--json</code>: 텍스트 대신 JSON 결과를 출력합니다.</li>
</ul>
<p>줄 지정은 marsdawn 0.3.0에서, 폴더와 <code>--background</code>는 0.5.1에서 추가되었습니다.</p>

<h3>marsdawn export</h3>
<p>MarsDawn 자체의 PDF 내보내기와 같은 엔진으로 Markdown 파일을 페이지가 나뉜 PDF로 렌더링합니다. MarsDawn 앱은 필요 없습니다. 상대 경로의 이미지는 입력 파일이 있는 폴더를 기준으로 찾습니다.</p>
<pre><code>marsdawn export notes.md -o notes.pdf --theme classic --paper a4</code></pre>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: PDF를 쓸 위치입니다. 기본값은 입력 경로에 <code>.pdf</code> 확장자를 붙인 것입니다.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: 미리보기 테마의 라이트 팔레트입니다. 기본값은 <code>$MARSDAWN_THEME</code>, 그다음 <code>dawn</code>입니다.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: 용지 크기입니다. 기본값은 <code>a4</code>입니다.</li>
  <li><code>--allow-remote-images</code>: 렌더링하는 동안 웹 이미지를 불러옵니다. 기본값은 꺼짐입니다.</li>
  <li><code>--force</code>: 출력 파일이 이미 있으면 바꿉니다.</li>
  <li><code>--json</code>: 텍스트 대신 JSON 결과를 출력합니다.</li>
</ul>

<h2>$MARSDAWN_THEME 변수</h2>
<p><code>--theme</code>를 주지 않으면 <code>export</code>는 <code>$MARSDAWN_THEME</code> 환경 변수를 읽습니다. 값은 <code>dawn</code>, <code>classic</code>, <code>modern</code>, <code>vivid</code> 중 하나여야 하며, 그 밖의 값은 <code>dawn</code>으로 처리됩니다. 다른 앱의 컨테이너를 읽으면 macOS 개인정보 보호 확인 창이 뜰 수 있기 때문에, CLI는 앱 자체의 테마 설정을 읽지 않습니다.</p>

<h2>파일 덮어쓰기</h2>
<p><code>export</code>는 <code>--force</code>를 주지 않는 한 기존 출력 파일을 바꾸지 않습니다.</p>

<h2>종료 코드</h2>
<!--exit-table-->
<ul>
  <li><code>0</code>: 성공.</li>
  <li><code>2</code>: 입력을 찾을 수 없음.</li>
  <li><code>3</code>: MarsDawn이 설치되어 있지 않음(<code>open</code>만 해당).</li>
  <li><code>4</code>: 출력 파일이 이미 있음(<code>--force</code>를 주세요).</li>
  <li><code>5</code>: 내보내기 실패.</li>
  <li><code>6</code>: 이 MarsDawn은 폴더를 보여줄 수 없어 아무것도 열지 않았음(<code>open</code>만 해당).</li>
  <li><code>64</code>: 사용법 오류. 범위를 벗어난 줄 번호, 파일 둘 이상이나 폴더와 함께 쓴 <code>--line</code>, 폴더 둘 이상 등이 포함됩니다.</li>
</ul>

<h2>--json 출력</h2>
<p>성공하면 <code>marsdawn open --json</code>은 <code>ok</code>, <code>opened</code>(각 파일의 <code>path</code>와, 줄을 요청한 경우 <code>line</code>이 담긴 목록), <code>app</code>(앱 경로), 그리고 폴더를 준 경우 <code>folder</code>를 출력합니다. <code>marsdawn export --json</code>은 <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code>, <code>diagramErrors</code>를 출력합니다. 실패하면 둘 다 <code>ok</code>, <code>error</code>, <code>message</code>를 출력합니다.</p>
""",
    }

    figures = {
        'index': {"alt": '분할 보기의 MarsDawn: 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.', "callouts": []},
        'yours': {"alt": '클래식 테마로 문서를 보여주는 MarsDawn. 미리보기가 윈도우를 가득 채우고 있습니다.',
                  "callouts": ['내 Mac에 있는 파일이고, 고른 곳에 저장됩니다.', '도구 막대에는 테마와 레이아웃뿐이고, 로그인할 곳은 없습니다.']},
        'pay-once': {"alt": '비비드 테마의 MarsDawn. 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.',
                     "callouts": ['편집기의 Markdown 하이라이트, 포함.', '모든 테마와 모든 레이아웃이 포함됩니다.', 'Mermaid 다이어그램, 포함.', '코드 하이라이트, 포함.']},
        'pdf': {"alt": 'MarsDawn에서 내보낸 PDF를 페이지 축소판과 함께 PDF 뷰어로 연 모습.',
                "callouts": ['Mermaid 다이어그램이 PDF 안에 그려집니다.', '코드는 하이라이트를 유지합니다.']},
        'native': {"alt": '분할 보기의 MarsDawn: 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.',
                   "callouts": ['네이티브 Mac 윈도우.', 'Markdown 하이라이트가 더해진 Mac의 텍스트 편집기.', '⌘1 소스, ⌘2 분할, ⌘3 미리보기.', '입력하는 대로 페이지가 바뀝니다.']},
        'limits': {"alt": '다크 모드의 MarsDawn. 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.',
                   "callouts": ['이 Mac에서, 윈도우 하나에 문서 하나.', '여기에서 Markdown을 씁니다.', '도구 막대에는 테마와 레이아웃이 있고, 플러그인 메뉴는 없습니다.', '이 페이지는 읽기용이며 편집할 수 없습니다.']},
    }
    home = {
        "cta_cli": '무료 CLI 설치하기',
        "cta_try": '지금 다운로드하고 체험하기',
        "cta_store": 'Mac App Store에서 보기',
        "install_h": '지금 바로 해 보세요',
        "install_lede": '무료 <code>marsdawn</code> 명령줄 도구는 지금 바로 쓸 수 있습니다. Homebrew로 설치하세요.',
        "install_caps": [
            '<code>marsdawn export</code>는 Markdown 파일을 MarsDawn의 미리보기처럼 렌더링된 PDF로 만듭니다. 앱은 필요 없습니다.',
            '<code>marsdawn open</code>은 검토할 수 있도록 MarsDawn 앱에서 파일을 엽니다.',
            '<code>--json</code>은 스크립트와 에이전트가 파싱할 수 있는 결과를 돌려줍니다.',
        ],
        "proof_h": '앱의 실제 모습',
    }
    compare_tables = {
        'pay-once-states': {
            "head": ['', '체험 기간(1~14일 차)', '체험 종료, 잠금 해제 안 함', '잠금 해제됨'],
            "rows": [
                ['MarsDawn에서 문서 열기', '가능', '열리지만 내용이 가려짐', '가능'],
                ['MarsDawn에서 읽기와 편집(소스, 미리보기, Mermaid, 수식)', '가능', '불가', '가능'],
                ['MarsDawn에서 PDF로 내보내기와 프린트', '가능', '불가', '가능'],
                ['파일 ▸ 별도 저장…으로 입력한 텍스트 보관', '가능', '가능(체험이 끝날 때 열려 있던 윈도우)', '가능'],
                ['Siri 및 단축어 동작', '가능', '불가', '가능'],
                ['Finder의 훑어보기(Mermaid 다이어그램과 수식 포함)', '가능', '가능(변화 없음)', '가능'],
                ['<code>marsdawn export</code>(무료 명령줄 도구): 다이어그램과 수식이 들어간 PDF', '가능', '가능(변화 없음)', '가능'],
                ['디스크에 있는 내 파일', '저장한 그대로', '저장한 그대로(잠금은 파일을 바꾸지 않음)', '저장한 그대로'],
            ],
        },
    }
    exit_table_head = ['코드', '의미', '해결 방법']
    exit_remedy = {
        "0": '<code>--json</code>을 줬다면 stdout의 JSON 한 줄을 읽으세요',
        "2": '경로와 파일 이름을 확인하세요',
        "3": '앱을 설치하거나, 앱이 필요 없는 <code>export</code>를 쓰세요',
        "4": '<code>--force</code>로 바꾸거나, <code>-o</code>로 다른 곳에 쓰세요',
        "5": 'JSON 결과의 <code>message</code>를 읽으세요',
        "64": '옵션이나 값을 고치세요. 이 오류는 <code>--json</code>을 줘도 stderr에 텍스트로 나옵니다',
    }
    # markdown-to-pdf shows /assets/cli/plan-ko.png, which does not exist yet. Before this ships,
    # export example_plan with marsdawn 0.5.0 the way EXAMPLE_PLAN's comment in build_pages.py
    # describes, or fall back to plan-en.png with EXAMPLE_PLAN['en'].
    example_plan = '# 계획: 더 빠른 내보내기\n\n이 계획은 에이전트가 작성했습니다. 검토한 다음 PDF로 만드세요.\n\n## 단계\n\n| 단계 | 담당 | 상태 |\n|------|------|------|\n| 느린 페이지 측정 | 에이전트 | 완료 |\n| 렌더링한 다이어그램 캐시 | 에이전트 | 검토 중 |\n\n목표는 50페이지 문서를 $t < 2\\,\\text{s}$ 안에 처리하는 것입니다.\n\n$$\nt_{\\text{total}} = \\sum_{i=1}^{n} t_i\n$$\n\n```mermaid\ngraph LR\n  초안 --> 검토 --> 배포\n```\n\n```swift\nlet pdf = try export("plan.md")\n```\n'

    pages['markdown-to-pdf'] = {
        "title": 'Mac의 명령줄에서 Markdown을 PDF로 · MarsDawn',
        "description": '무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.',
        "body": f"""
<section class="intro">
  <h1>Mac의 명령줄에서 Markdown을 PDF로.</h1>
  <p>무료 도구 <code>marsdawn</code>은 명령 하나로 Markdown 파일을 PDF로 바꿉니다. 표, 수식, Mermaid 다이어그램, 강조 표시된 코드가 원본에서 읽히는 그대로 나오며, 다른 것은 아무것도 설치할 필요가 없습니다. MarsDawn 앱조차 필요 없습니다.</p>
</section>
<h2>설치하기</h2>
<pre><code>{k.INSTALL}
marsdawn --version</code></pre>
<p>Apple 실리콘 Mac에서는 Homebrew가 미리 빌드된 사본을 몇 초 만에 설치합니다. Intel Mac에서는 대신 소스에서 빌드하므로 몇 분이 걸리고 Xcode 26 이상이 필요합니다. macOS 15 이상에서 실행되며, <code>marsdawn --version</code>으로 설치된 버전을 확인할 수 있습니다.</p>
<h2>문서 저장하기</h2>
<p>다음 내용을 <code>plan.md</code>라는 파일에 붙여 넣으세요.</p>
<pre><code>{k.xml_escape(example_plan)}</code></pre>
<h2>내보내기</h2>
<pre><code>marsdawn export plan.md</code></pre>
<p>원본 옆에 <code>plan.pdf</code>를 쓰고, 저장된 위치를 출력합니다.</p>
<pre><code>Exported /Users/you/plan.pdf (1 page)</code></pre>
<p>아래는 <code>marsdawn</code> 0.5.0을 실제로 실행해서 캡처한 바로 그 페이지입니다.</p>
<p><img class="pdf-page" src="/assets/cli/plan-ko.png" alt="내보낸 PDF: 제목, 단계 표, 본문 속 수식과 별도 줄의 수식, 초안, 검토, 배포 다이어그램, 강조 표시된 Swift 코드 한 줄." width="989" height="930"></p>
<h2>테마, 용지 크기, 파일 이름 선택하기</h2>
<pre><code>marsdawn export plan.md --theme classic --paper letter -o handout.pdf</code></pre>
<ul>
  <li><code>--theme</code>: dawn, classic, modern, vivid 중 하나이며, 테마의 라이트 색상을 사용합니다. 지정하지 않으면 <code>export</code>는 <code>$MARSDAWN_THEME</code>을, 그것도 없으면 dawn을 사용합니다.</li>
  <li><code>--paper</code>: a4 또는 letter. 기본값은 a4입니다.</li>
  <li><code>-o</code>: 원본 옆 대신 PDF를 쓸 위치입니다.</li>
  <li><code>--allow-remote-images</code>: 렌더링하는 동안 웹에서 이미지를 불러옵니다. 이 옵션을 주지 않으면 꺼진 상태로 유지됩니다.</li>
</ul>
<h2>잘 안 될 때</h2>
<ul>
  <li><code>A full installation of Xcode.app 26.0 is required to compile this software.</code> Intel Mac에서처럼 Homebrew가 <code>marsdawn</code>을 소스에서 빌드하고 있습니다. App Store에서 Xcode 26 이상을 설치한 다음 설치를 다시 실행하세요.</li>
  <li><code>marsdawn: No such file: …</code> 경로가 파일을 가리키지 않습니다. 이름을 확인하거나, 파일이 있는 폴더에서 명령을 실행하세요.</li>
  <li><code>… already exists. Pass --force to replace it.</code> 같은 이름의 PDF가 이미 있습니다. 바꾸려면 <code>--force</code>를, 다른 곳에 쓰려면 <code>-o</code>를 추가하세요.</li>
  <li><code>Error: The value '…' is invalid for '--theme &lt;theme&gt;'.</code> 알 수 없는 테마나 용지 크기입니다. 테마는 dawn, classic, modern, vivid이고, 용지는 a4 또는 letter입니다.</li>
</ul>
<h2>다음</h2>
<ul>
  <li>모든 옵션과 출력되는 JSON: <a href="/ko/cli/">명령줄</a>.</li>
  <li>코딩 에이전트에게 이 작업을 맡기려면: <a href="/ko/cli/skill/">marsdawn 에이전트 스킬</a>.</li>
  <li>네 가지 미리보기 테마와 PDF 내보내기의 방향: <a href="/ko/themes/">미리보기 테마와 PDF 내보내기</a>.</li>
  <li>Markdown을 쓰지 않는 사람에게 PDF 전달하기: <a href="/ko/sharing-exported-pdfs/">PDF 공유하기</a>.</li>
</ul>
""",
    }

    pages['view-markdown-on-mac'] = {
        "title": 'Mac에서 Markdown 파일을 보는 방법 · MarsDawn',
        "description": '.md 파일은 서식 기호가 들어 있는 일반 텍스트입니다. Mac에서 렌더링된 상태로 읽는 방법을 소개합니다. 지금 바로 무료 marsdawn 명령줄 도구로 PDF를 만들 수 있고, Mac App Store의 MarsDawn 앱에서 읽을 수도 있습니다.',
        "body": f"""
<section class="intro">
  <h1>Mac에서 Markdown 파일을 보는 방법.</h1>
  <p><code>.md</code> 파일은 일반 텍스트입니다. 제목, 굵은 글씨, 표, 다이어그램은 기호로 적혀 있습니다. 제목은 <code>#</code>, 굵은 글씨는 <code>**</code>로 감싸고, 표는 세로 막대로, 다이어그램은 <code>mermaid</code> 코드 블록으로 씁니다. 일반 텍스트 편집기로 열면 이 기호들이 그대로 보입니다. 작성자가 의도한 대로 페이지를 읽으려면 무언가가 렌더링해 줘야 합니다.</p>
</section>
<h2>지금 무료로: PDF로 바꾸기</h2>
<p>무료 <code>marsdawn</code> 명령줄 도구는 Markdown 파일을 어떤 Mac에서든 열 수 있는 PDF로 렌더링합니다. 표, 수식, Mermaid 다이어그램, 강조 표시된 코드가 렌더링된 상태로 나오며, 다른 것은 아무것도 설치할 필요가 없습니다. MarsDawn 앱조차 필요 없습니다.</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<p><code>export</code>는 Markdown 파일 옆에 <code>notes.pdf</code>를 쓰고, <code>open</code>은 그 파일을 PDF 뷰어에서 보여 줍니다. macOS 15 이상이 필요합니다. 실제로 내보낸 페이지와 함께 보는 단계별 안내는 <a href="/ko/markdown-to-pdf/">Markdown을 PDF로</a>에 있습니다.</p>
<h2>MarsDawn에서 읽기</h2>
<p>MarsDawn은 Mac App Store에 있는 Mac용 Markdown 편집기입니다. <code>.md</code> 파일을 열고 원본 옆에서 렌더링된 페이지를 읽으세요.</p>
<ul>
  <li>입력하는 동안 미리보기가 업데이트되고, 두 패널이 함께 스크롤됩니다.</li>
  <li>Mermaid 순서도와 시퀀스 다이어그램이 미리보기에 그려지고, 코드 블록은 강조 표시됩니다.</li>
  <li>Finder에서 Markdown 파일을 선택하고 스페이스 바를 누르면 다이어그램까지 포함된 훑어보기 미리보기가 나타납니다.</li>
  <li>무언가를 고치고 싶을 때 원본이 바로 옆에 있습니다. MarsDawn은 뷰어만이 아니라 편집기입니다.</li>
</ul>
<p>AI 에이전트가 쓴 파일이라면, 이것이 바로 MarsDawn이 만들어진 이유인 반복 과정입니다. 에이전트가 쓰고, 여러분이 렌더링된 결과를 읽고, 에이전트가 고칩니다. <a href="/ko/">홈페이지</a>를 참고하고, 에이전트가 대신 파일을 열게 하려면 <a href="/ko/cli/agents/">에이전트를 위한 marsdawn</a>을 참고하세요. 이렇게 읽는 일이 왜 중요한지, 계획은 어떻게 검토하는지는 <a href="/ko/reading-agent-output/">에이전트가 돌려준 결과 읽기</a>와 <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 만에 검토하기</a>에서 확인하세요.</p>
<h2>다음</h2>
<ul>
  <li>명령줄 도구의 모든 옵션: <a href="/ko/cli/">명령줄</a>.</li>
  <li>MarsDawn이 하지 않는 일: <a href="/ko/limits/">목록</a>.</li>
  <li>VS Code, 브라우저, Claude Desktop에서 Markdown을 읽는 경우: <a href="/ko/vs/markdown-preview-tools/">비교해 보기</a>.</li>
</ul>
""",
    }

    pages['vs/macmd-viewer'] = {
        "title": 'MacMD Viewer와 MarsDawn: 뷰어인가, 편집기인가 · MarsDawn',
        "description": 'MacMD Viewer는 Markdown을 읽기 전용으로 렌더링하며 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 무료로 체험한 뒤 Mac App Store에서 USD 4.99에 한 번만 구입하면 됩니다.',
        "body": f"""
<section class="intro">
  <h1>MacMD Viewer와 MarsDawn.</h1>
  <p>둘 다 Markdown을 렌더링해서 읽기 위한 Mac 앱입니다. MacMD Viewer는 <code>.md</code> 파일을 열어 완성된 페이지를 보여 주지만, 편집은 하지 않습니다. MarsDawn은 같은 종류의 렌더링된 미리보기 옆에 편집기를 두어, 한 윈도우에서 쓰고 검토할 수 있게 합니다. 기능별로 어떻게 다른지 살펴보세요.</p>
</section>
<h2>편집하지 않고 읽기만 한다면</h2>
<p>다른 사람이 쓴 Markdown을 읽기만 하고 원본은 전혀 건드릴 필요가 없다면, MacMD Viewer도 괜찮은 선택입니다. 바로 그 용도로 만들어졌고, 지금 구할 수 있으며, 더 오래된 macOS에서도 동작합니다. 읽는 것만으로 일이 끝나지 않을 때 MarsDawn이 가치를 발휘합니다. 에이전트의 Markdown은 대개 한 번 더 손볼 일이 생기기 때문입니다.</p>
<h2>각 앱이 하는 일</h2>
<!--compare:macmd-features-->
<h2>가격과 구입 방법</h2>
<!--compare:macmd-buying-->
<h2>지금 무료로 사용해 보세요</h2>
<p>MarsDawn은 Mac App Store에 있습니다. 무료 <code>marsdawn</code> 명령줄 도구도 어떤 Markdown 파일이든 Mermaid 다이어그램과 강조 표시된 코드를 포함한 PDF로 렌더링하며, 다른 것은 아무것도 설치할 필요가 없습니다.</p>
<pre><code>{k.BREW_TAP_INSTALL}
marsdawn export notes.md
open notes.pdf</code></pre>
<h2>다음</h2>
<ul>
  <li>전체 안내: <a href="/ko/markdown-to-pdf/">Markdown을 PDF로</a>.</li>
  <li>MarsDawn이 하지 않는 일: <a href="/ko/limits/">목록</a>.</li>
  <li>명령줄 도구의 모든 옵션: <a href="/ko/cli/">명령줄</a>.</li>
  <li>VS Code, 브라우저, Claude Desktop에서 Markdown을 읽는 경우와 비교: <a href="/ko/vs/markdown-preview-tools/">비교해 보기</a>.</li>
</ul>
""",
    }

    compare_tables['macmd-features'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['편집', '설계상 읽기 전용', '렌더링된 페이지를 옆에 두고 원본을 편집'],
            ['미리보기 테마', '문서 테마 12개', '테마 4개, 각각 라이트와 다크 팔레트 제공'],
            ['다이어그램과 수식', 'Mermaid와 코드 강조 표시. 앱 설명에 수식 언급은 없음', 'Mermaid, 코드 강조 표시, KaTeX 수식'],
            ['Finder에서 훑어보기', '예', '예'],
            ['PDF와 프린트', '예', '예'],
            ['요구 사항', 'macOS 14(Sonoma) 이상', 'macOS 26(Tahoe) 이상'],
            ['인터페이스 언어', '자체 자료에 명시되지 않음', '{langs}'],
        ],
    }
    compare_tables['macmd-buying'] = {
        'head': ['', 'MacMD Viewer', 'MarsDawn'],
        'rows': [
            ['구입처', '자체 사이트, Homebrew 또는 Setapp. Mac App Store에는 없음', 'Mac App Store에서만'],
            ['가격', 'Mac 1대용 USD 19.99 일회성 결제. 여러 대용 패키지는 더 비쌈', '무료 다운로드 후 USD 4.99 일회성 결제'],
            ['먼저 사용해 보기', '체험판 없음. 직접 구입 시 14일 환불 보장', '14일 무료 체험'],
            ['환불과 업데이트', '자체 사이트를 통해', 'Apple을 통해'],
            ['계정 필요', '아니요', '아니요'],
        ],
    }

    schema_notes = {
        "export": "export 성공",
        "open": "open 성공, marsdawn 0.5.1 이상, 사이드바에 표시되는 폴더 포함",
        "open_v2": "open 성공, marsdawn 0.3.0~0.5.0",
        "error": "실패, 두 명령 공통, marsdawn 0.5.2 이상",
        "open_v1": "open 성공, marsdawn 0.2.x, 이때 <code>opened</code>는 경로 목록이었음",
        "error_v1": "실패, 두 명령 공통, marsdawn 0.5.1 이하",
    }

    pages['cli/agents'] = {
        "title": '에이전트를 위한 marsdawn: 스크립트에서 Markdown을 PDF로 · MarsDawn',
        "description": 'marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.',
        "body": f"""
<section class="intro">
  <h1>에이전트를 위한 marsdawn</h1>
  <p><code>marsdawn</code> 명령줄 도구를 호출하는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 이 페이지의 모든 예시는 현재 소스로 빌드한 도구에서 실제로 실행했습니다.</p>
</section>

<div class="summary"><p><strong>Markdown 파일을 PDF로 바꾸려면 <code>marsdawn export notes.md --json</code>을 실행하고 stdout에서 JSON 객체 하나를 읽으세요.</strong> Mermaid 다이어그램과 강조 표시된 코드는 MarsDawn 앱에서와 똑같이 렌더링됩니다. <code>export</code>에는 앱이 필요 없고, <code>open</code>에는 필요합니다.</p></div>

<h2>하는 일</h2>
<ul>
  <li><code>export</code>는 MarsDawn 앱과 같은 내보내기 엔진으로 Markdown 파일 하나를 페이지가 나뉜 PDF로 렌더링합니다. 윈도우는 열리지 않습니다.</li>
  <li><code>open</code>은 사람이 검토할 수 있도록 하나 이상의 Markdown 파일을 MarsDawn 앱에서 엽니다. 각 파일이 열릴 줄을 지정할 수 있고, 윈도우 사이드바에 폴더를 표시할 수도 있습니다.</li>
</ul>

<h2>하지 않는 일</h2>
<ul>
  <li>stdin에서 Markdown을 읽지 않습니다. 파일 경로를 전달하세요.</li>
  <li>PDF를 stdout에 쓰지 않습니다. PDF는 항상 파일로 저장되고, stdout에는 결과만 나옵니다.</li>
  <li><code>--force</code>를 주지 않으면 기존 파일을 덮어쓰지 않습니다.</li>
  <li><code>--allow-remote-images</code>를 주지 않으면 웹에서 이미지를 불러오지 않으며, 줄 때도 https로만 불러옵니다.</li>
  <li><code>open</code>은 MarsDawn 앱이 설치되어 있지 않으면 동작하지 않고 코드 3으로 종료합니다. <code>export</code>에는 앱이 필요 없습니다. 앱은 <a href="{k.LISTING_URL}">Mac App Store</a>에 있습니다.</li>
  <li>MarsDawn 1.0은 <code>open</code>이 지정한 줄에서 파일을 엽니다.</li>
  <li>macOS에서만 실행됩니다.</li>
</ul>

<h2>export</h2>
<pre><code>marsdawn export notes.md --json</code></pre>
<p><code>notes.md</code> 옆에 <code>notes.pdf</code>를 씁니다. 옵션:</p>
<ul>
  <li><code>-o, --output &lt;path&gt;</code>: PDF를 쓸 위치. 기본값은 입력 경로에 확장자 <code>.pdf</code>를 붙인 것입니다.</li>
  <li><code>--theme &lt;dawn|classic|modern|vivid&gt;</code>: 테마의 라이트 팔레트. 기본값은 <code>$MARSDAWN_THEME</code>, 그것도 없으면 <code>dawn</code>입니다.</li>
  <li><code>--paper &lt;a4|letter&gt;</code>: 용지 크기. 기본값은 <code>a4</code>입니다.</li>
  <li><code>--allow-remote-images</code>: 렌더링하는 동안 웹에서 https 이미지를 불러옵니다.</li>
  <li><code>--force</code>: 출력 파일이 있으면 덮어씁니다.</li>
  <li><code>--json</code>: 텍스트 대신 stdout에 JSON 객체 하나를 출력합니다.</li>
</ul>
<pre><code>marsdawn export notes.md -o out.pdf --theme classic --paper letter --force --json</code></pre>
<p>성공, 종료 코드 0:</p>
<pre><code>{{"diagramErrors":[],"ok":true,"output":"/path/to/out.pdf","pages":1,"paper":"letter","theme":"classic"}}</code></pre>
<ul>
  <li><code>output</code>: 저장된 PDF의 절대 경로.</li>
  <li><code>pages</code>: 페이지 수.</li>
  <li><code>theme</code>과 <code>paper</code>: 실제로 사용된 값.</li>
  <li><code>diagramErrors</code>: 렌더링에 실패한 Mermaid 다이어그램마다 메시지 하나. PDF는 그래도 저장됩니다.</li>
</ul>

<h2>open</h2>
<pre><code>marsdawn open notes.md --json
marsdawn open notes.md:120 --json
marsdawn open notes.md --line 120 --json
marsdawn open . --json
marsdawn open notes.md --folder . --background --json</code></pre>
<ul>
  <li><code>path:line</code>은 열릴 줄을 지정합니다. <code>notes.md:120:8</code>처럼 뒤에 붙은 열 번호는 무시됩니다. 존재하는 파일을 가리키는 인수는 항상 그 전체가 파일 이름이므로, <code>weird:12</code>라는 파일은 그 파일 자체로 열립니다.</li>
  <li><code>--line &lt;n&gt;</code>은 파일 하나의 줄을 지정하며, 경로 자체가 콜론과 숫자로 끝나는 경우에도 쓸 수 있습니다. 파일이 정확히 하나여야 합니다.</li>
  <li>줄 번호는 1부터 999999999까지입니다. 그 밖의 값은 사용법 오류입니다.</li>
  <li>줄 지정은 marsdawn 0.3.0에서 추가되었습니다. MarsDawn 1.0은 그 줄에서 파일을 엽니다.</li>
  <li>폴더 인수는 문서가 아니라 윈도우 사이드바에 열리므로, <code>marsdawn open .</code>은 현재 폴더를 보여 줍니다. <code>--folder &lt;path&gt;</code>는 파일과 함께 같은 일을 합니다. 윈도우 사이드바에는 폴더가 하나만 표시되므로, 폴더를 두 개 지정하면 사용법 오류이고, 같은 폴더라도 <code>--folder</code>를 두 번 쓰면 사용법 오류입니다. 같은 폴더를 인수로 한 번 더 주면 한 번으로 셉니다. 폴더에는 줄이 없으므로 폴더와 함께 <code>--line</code>을 쓰면 사용법 오류입니다. <code>-a</code>는 없습니다. 이를 주면 <code>--folder</code>를 안내하는 사용법 오류가 납니다.</li>
  <li><code>--background</code>는 MarsDawn을 앞으로 가져오지 않고 엽니다. 사람이 다른 곳에서 일하는 동안 에이전트가 파일을 여는 경우를 위한 옵션입니다. JSON은 어느 쪽이든 같습니다.</li>
  <li>폴더와 <code>--background</code>는 marsdawn 0.5.1에서 추가되었습니다.</li>
</ul>
<p>성공, 종료 코드 0:</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","ok":true,"opened":[{{"line":120,"path":"/path/to/notes.md"}}]}}</code></pre>
<ul>
  <li><code>opened</code>: 파일마다 객체 하나, 주어진 순서대로. <code>path</code>는 파일의 절대 경로이고, <code>line</code>은 줄을 요청했을 때만 나타납니다.</li>
  <li><code>app</code>: 파일을 연 MarsDawn 앱의 경로.</li>
</ul>
<p>폴더를 준 경우(marsdawn 0.5.1 이상), 종료 코드 0:</p>
<pre><code>{{"app":"/Applications/MarsDawn.app","folder":{{"path":"/path/to/project","requested":true}},"ok":true,"opened":[{{"path":"/path/to/project/notes.md"}}]}}</code></pre>
<ul>
  <li><code>folder</code>: 폴더를 줬을 때만 나타납니다. <code>path</code>는 폴더의 절대 경로입니다. <code>requested</code>는 항상 <code>true</code>입니다. marsdawn은 MarsDawn에 폴더를 보여 달라고 요청했을 뿐이고, 앱이 먼저 사람에게 접근 권한을 물을 수 있으므로 사이드바에 실제로 표시됐는지는 알 수 없습니다. 완료가 아니라 요청됨으로 보고하세요.</li>
  <li>폴더만 줬을 때 <code>opened</code>는 비어 있습니다.</li>
</ul>
<p>marsdawn 0.2.x는 <code>opened</code>를 경로 문자열 목록으로 출력했습니다. 두 형식을 모두 처리해야 한다면 <code>marsdawn --version</code>을 확인하세요.</p>

<h2>Claude Code가 편집하는 파일 바로 열기</h2>
<p>선택해서 쓰는 <a href="https://code.claude.com/docs/en/hooks">Claude Code 훅</a>입니다. Claude가 Markdown 파일을 쓰거나 편집하면 그 파일을 MarsDawn에서 백그라운드로 엽니다. 세션마다 파일당 한 번입니다. 요청하지 않은 윈도우는 주의를 빼앗기 때문에, 직접 추가하기 전까지는 꺼져 있고 프로젝트별로 하나씩 켭니다. 셸 명령을 실행할 뿐이라 모델 토큰은 들지 않습니다.</p>
<p><code>--background</code>를 쓰므로 marsdawn 0.5.1 이상과 MarsDawn 앱이 필요합니다.</p>
<p>다음을 프로젝트의 <code>.claude/hooks/marsdawn-open.sh</code>로 저장하고 <code>chmod +x</code>로 실행 권한을 주세요.</p>
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
<p>그런 다음 프로젝트의 <code>.claude/settings.json</code>에 훅을 추가하세요. 나만 쓰려면 <code>.claude/settings.local.json</code>에 추가하면 됩니다.</p>
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
  <li>Claude의 Write와 Edit 도구 다음에 실행됩니다. <code>.md</code>나 <code>.markdown</code>으로 끝나지 않는 파일은 건드리지 않습니다.</li>
  <li>Claude가 몇 번을 편집하든 각 파일은 Claude Code 세션마다 한 번만 열립니다. 목록은 <code>$TMPDIR/marsdawn-hook/</code>에 세션마다 파일 하나로 저장되므로, 새 세션에서는 파일이 다시 열립니다.</li>
  <li><code>--background</code> 덕분에 MarsDawn이 앞으로 나오지 않습니다. 작업하던 윈도우가 포커스를 유지합니다.</li>
  <li>Claude를 방해하지 않습니다. 모든 경로가 0으로 끝나며, marsdawn이나 MarsDawn 앱이 설치되어 있지 않으면 아무 일도 일어나지 않습니다.</li>
  <li>훅의 입력은 <code>/usr/bin/jq</code>로 읽습니다. jq는 MarsDawn 앱이 요구하는 macOS 26에 기본으로 들어 있습니다.</li>
  <li>끄려면 설정 파일에서 해당 항목을 지우세요.</li>
</ul>

<h2>실패</h2>
<p><code>--json</code>을 주면 실패 시 stdout에 JSON 객체 하나를 출력하고 해당 코드로 종료합니다.</p>
<pre><code>{{"error":"output_exists","message":"/path/to/notes.pdf already exists. Pass --force to replace it.","ok":false}}</code></pre>
<ul>
  <li><code>2</code>, <code>input_not_found</code>: 입력이 없거나, 폴더이거나, UTF-8 텍스트가 아닙니다. 또는 <code>--folder</code> 경로가 없거나 폴더가 아닙니다.</li>
  <li><code>3</code>, <code>app_not_installed</code>: MarsDawn이 설치되어 있지 않습니다. <code>open</code>만 이 코드를 반환합니다.</li>
  <li><code>4</code>, <code>output_exists</code>: 출력 파일이 이미 있습니다. <code>--force</code>를 주세요.</li>
  <li><code>5</code>, <code>export_failed</code>: 내보내기 자체가 실패했습니다.</li>
  <li><code>6</code>, <code>app_cannot_open_folders</code>: 이 버전의 MarsDawn은 폴더를 표시할 수 없어서 아무것도 열지 않았습니다. <code>open</code>만 이 코드를 반환합니다.</li>
  <li><code>64</code>: 사용법 오류. 알 수 없는 옵션, 잘못된 값, 범위를 벗어난 줄, 파일 두 개 이상이나 폴더와 함께 쓴 <code>--line</code>, 폴더 두 개 이상, <code>-a</code> 등이 해당합니다. 이 오류는 <code>--json</code>을 줘도 stderr에 텍스트로 출력됩니다.</li>
</ul>

<h2>JSON 스키마</h2>
<p>모든 <code>--json</code> 결과에 대한 JSON Schema(draft 2020-12):</p>
<ul>
{k.schema_links_from(schema_notes)}
</ul>

<h2>환경 변수</h2>
<ul>
  <li><code>MARSDAWN_THEME</code>: <code>--theme</code>을 주지 않았을 때 <code>export</code>가 쓰는 테마. 알 수 없는 값이면 오류 없이 <code>dawn</code>으로 돌아갑니다.</li>
</ul>

<h2>요구 사항</h2>
<ul>
  <li>이 도구는 macOS 15 이상에서 실행됩니다. Apple 실리콘에서는 Homebrew가 미리 빌드된 bottle을 설치하므로 다른 것은 필요 없습니다. Intel Mac에서나 소스로 직접 빌드하려면 Swift 6.2 이상이 필요하며, 이는 Xcode 26 이상에 들어 있습니다.</li>
  <li>MarsDawn 앱은 macOS 26 이상이 필요합니다.</li>
</ul>

<h2>설치</h2>
<p>Homebrew로 설치합니다. Apple 실리콘에서는 미리 빌드된 bottle을 몇 초 만에 설치하며 Xcode가 필요 없습니다. Intel Mac에서는 marsdawn을 소스에서 컴파일하므로 몇 분이 걸리고 Xcode 26 이상이 필요합니다.</p>
<pre><code>brew tap redtear1115/tap && brew install marsdawn
marsdawn --version</code></pre>
<p>또는 <a href="{k.KIT_URL}">소스</a>에서 직접 빌드하세요. 첫 빌드는 의존성을 가져와 컴파일하므로 역시 몇 분이 걸립니다.</p>
<pre><code>git clone https://github.com/redtear1115/mars-dawn-kit.git
cd mars-dawn-kit
swift build -c release --product marsdawn
.build/release/marsdawn export notes.md --json</code></pre>
<p><code>marsdawn --version</code>은 <code>0.3.0</code> 같은 버전 번호를 출력하고 코드 0으로 종료합니다.</p>

<h2>다음</h2>
<ul>
  <li>셸 대신 지침 파일을 읽는 에이전트를 위한 파일 하나짜리 스킬: <a href="/ko/cli/skill/">marsdawn 스킬</a>.</li>
  <li>이 <code>export</code>를 그대로 감싼 MCP 서버: <a href="/ko/cli/mcp/">marsdawn-mcp</a>.</li>
  <li>이 JSON 결과가 에이전트 자신의 컨텍스트에 부담이 적은 이유: <a href="/ko/token-efficient-review/">토큰을 아끼는 검토</a>.</li>
</ul>
""",
    }

    pages['cli/skill'] = {
        "title": 'Markdown을 PDF로 만드는 코딩 에이전트 스킬 · MarsDawn',
        "description": '코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.',
        "body": f"""
<section class="intro">
  <h1>에이전트가 쓴 글을 직접 보여 주고, PDF도 만들게 하세요.</h1>
  <p>이 스킬은 Markdown 파일 하나입니다. 코딩 에이전트에게 자신이 쓴 문서를 MarsDawn에서 열어 여러분이 검토하게 하는 법, 그리고 <code>marsdawn</code>을 설치하고, 동작을 확인하고, 문서를 PDF로 내보내고, 결과를 읽는 법을 가르칩니다.</p>
</section>
<div class="summary"><p><strong><code>~/.claude/skills/marsdawn/SKILL.md</code>에 두는 Markdown 파일 하나.</strong> 이 파일이 있으면 에이전트가 <code>marsdawn</code>을 설치하고, PDF로 내보내고, JSON 결과를 읽습니다. 무언가를 실행하기 전에는 여전히 먼저 묻습니다.</p></div>
<h2>Claude Code에 설치하기</h2>
<pre><code>mkdir -p ~/.claude/skills/marsdawn
curl -fsSL https://marsdawn.southern-light.dev/cli/skill/SKILL.md -o ~/.claude/skills/marsdawn/SKILL.md</code></pre>
<p>Claude Code는 PDF가 필요한 작업일 때, 또는 여러분이 읽을 Markdown 문서를 쓰거나 고쳤을 때 이 스킬을 불러옵니다. <code>/marsdawn</code>으로 직접 실행할 수도 있습니다. <a href="/cli/skill/SKILL.md">짧은 파일 하나</a>이니 설치하기 전에 읽어 보세요.</p>
<p>다른 에이전트도 같은 파일을 쓸 수 있습니다. 지침과 명령으로 된 일반 Markdown이므로, 에이전트에게 URL을 알려 주거나 내용을 붙여 넣으세요.</p>
<h2>가르치는 내용</h2>
<ul>
  <li><code>marsdawn</code>이 없으면 Homebrew로 설치하고, 버전을 짐작하지 말고 <code>marsdawn --version</code>으로 확인하기.</li>
  <li><code>marsdawn export … --json</code>으로 내보내고 결과 읽기: PDF가 저장된 위치, 페이지 수, 렌더링되지 않은 Mermaid 다이어그램.</li>
  <li>종료 코드로 실패를 구분하기: 파일 없음, PDF가 이미 있음, 내보내기 실패, 잘못된 옵션.</li>
  <li>자신이 쓴 문서를 <code>marsdawn open file.md:line</code>으로 첫 번째 변경 위치에서, 한 번만 열기. 이후의 편집은 열린 윈도우에 알아서 반영됩니다.</li>
  <li>MarsDawn 앱이 설치되어 있지 않으면 한 번만 알리고, 다시 시도하지 말고 계속 진행하기. PDF를 만들 때 <code>open</code>은 절대 쓰지 않기.</li>
  <li><code>--folder</code>(marsdawn 0.5.1 이상)를 쓸 때는 폴더를 표시됨이 아니라 요청됨으로 보고하기. 앱이 결정하고, 결과를 알려 주는 것은 없습니다.</li>
</ul>
<h2>하지 않는 일</h2>
<ul>
  <li>스스로에게 실행 권한을 주지 않습니다. 에이전트는 다른 명령과 마찬가지로 <code>marsdawn</code>을 설치하거나 실행하기 전에 여전히 묻습니다.</li>
  <li>문서를 어디에도 보내지 않습니다. <code>marsdawn</code>은 여러분의 Mac에서 렌더링하며, <code>--allow-remote-images</code>를 주지 않으면 웹 이미지를 빼고 렌더링합니다.</li>
</ul>
<p>모든 필드와 코드를 포함한 전체 규약은 <a href="/ko/cli/agents/">에이전트를 위한 marsdawn</a>에 있습니다. 스킬 파일을 읽는 대신 MCP로 도구를 호출하는 에이전트라면 <a href="/ko/cli/mcp/">MCP 서버</a>도 있습니다.</p>
""",
    }

    pages['cli/mcp'] = {
        "title": 'marsdawn을 호출하는 세 가지 방법: CLI, 스킬 파일, MCP 서버 · MarsDawn',
        "description": 'marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.',
        "body": f"""
<section class="intro">
  <h1>marsdawn을 호출하는 세 가지 방법.</h1>
  <p>MarsDawn에는 자체 AI 모델이 없습니다. Markdown을 쓰는 것이 아니라 검토하려고 만든 앱이므로, 어떤 에이전트나 모델이 파일을 만들었는지는 상관없습니다. 에이전트나 스크립트가 <code>marsdawn</code>을 호출하는 방법은 세 가지이며, 세 가지 모두 결국 같은 <code>export</code>를 실행합니다.</p>
</section>

<div class="summary"><p><strong>쓰는 도구가 지원하는 것을 고르세요. 무료 <code>marsdawn</code> CLI, 일반 Markdown으로 된 스킬 파일, MCP 서버 <a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a>.</strong> 세 가지 모두 같은 <code>marsdawn export</code>를 호출하고 같은 JSON 결과를 돌려줍니다.</p></div>

<h2>무엇을 쓸까</h2>
<!--compare:mcp-choice-->

<h2>CLI</h2>
<p><code>marsdawn export notes.md --json</code>은 셸 명령을 실행할 수 있는 에이전트나 스크립트라면 무엇이든 호출할 수 있으므로, 구조상 특정 모델에 묶이지 않습니다. 반환하는 모든 필드는 <a href="/ko/cli/agents/">에이전트를 위한 marsdawn</a>에 문서화되어 있으며, 아래의 다른 두 방법도 JSON 스키마는 이 문서를 기준으로 삼습니다.</p>

<h2>스킬 파일</h2>
<p>셸을 직접 호출하지 않고 일반 Markdown 지침을 읽는 에이전트(현재는 Claude Code)를 위해, <a href="/ko/cli/skill/">marsdawn 스킬</a>은 marsdawn을 설치하고 <code>export</code>를 실행하고 결과를 읽는 법을 가르치는 파일 하나입니다. 일반 Markdown이므로 지침 파일을 불러오는 다른 에이전트도 같은 파일을 쓸 수 있습니다.</p>

<h2>MCP 서버</h2>
<p><a href="https://github.com/redtear1115/marsdawn-mcp">marsdawn-mcp</a>는 Apache-2.0 라이선스의 별도 공개 저장소입니다. <code>export_markdown_to_pdf</code>와 <code>open_in_marsdawn</code> 두 도구를 가진 MCP 서버로, 각각 <code>marsdawn export --json</code>과 <code>marsdawn open --json</code>을 감쌉니다. MCP 클라이언트가 이 서버를 가리키게 하면 도구 호출이 CLI와 같은 JSON을 돌려줍니다.</p>
<ul>
  <li><strong>받는 곳:</strong> MCP Bundle인 <code>marsdawn.mcpb</code>를 <a href="https://github.com/redtear1115/marsdawn-mcp/releases">GitHub 릴리스</a>에서 받거나, 소스에서 stdio로 서버를 실행합니다.</li>
  <li><strong>레지스트리:</strong> 아직 MCP Registry에 등록되지 않았습니다(현재 릴리스: 0.2.1). 레지스트리 검색에 의존하기 전에 저장소에서 현재 상태를 확인하세요.</li>
  <li><strong>호스팅:</strong> 직접 호스팅만 가능합니다. 호스팅된 marsdawn-mcp 서비스는 없으며, 서버는 marsdawn과 함께 여러분의 컴퓨터에서 실행됩니다.</li>
  <li><strong>요구 사항:</strong> macOS, marsdawn 0.5.0 이상, 그리고 서버를 실행할 Node.js 20 이상.</li>
</ul>

<h2>허용한 폴더 안에서만</h2>
<p>두 도구 모두 여러분이 허용한 폴더 안에만 접근합니다. 확장 프로그램의 <strong>Allowed folders</strong> 설정(처음에는 비어 있고 기본값도 없음)이나, 그 대신 MCP 클라이언트가 제공하는 루트가 기준입니다. 둘 다 설정되어 있지 않으면 모든 호출이 거부되며, 거부 메시지에 해결 방법이 나옵니다. 모든 경로는 절대 경로여야 하고, <code>export_markdown_to_pdf</code>는 <code>.pdf</code> 파일만 쓰며 심볼릭 링크를 통해서는 절대 쓰지 않습니다.</p>
<p><strong>보안:</strong> <a href="https://github.com/redtear1115/marsdawn-mcp/releases/tag/v0.2.1">0.2.1</a>로 업데이트하세요. 0.1.0과 0.2.0에서는 호출 한 번으로 여러분의 계정이 쓸 수 있는 어떤 경로에든 PDF를 쓸 수 있었으며, <a href="https://github.com/redtear1115/marsdawn-mcp/security/advisories/GHSA-fqgj-hcxc-34qc">GHSA-fqgj-hcxc-34qc</a>로 수정되었습니다.</p>

<h2>같은 내보내기, 세 개의 문</h2>
<p>어느 쪽에서 호출하든 그 아래의 동작은 바뀌지 않습니다. 같은 내보내기 엔진, 같은 테마와 용지 크기, Mermaid 다이어그램 렌더링이 실패했을 때의 같은 <code>diagramErrors</code>. 이 페이지에서는 그 규약을 반복하지 않습니다. 전체 내용은 <a href="/ko/cli/agents/">에이전트를 위한 marsdawn</a>에 있습니다.</p>

<h2>다음</h2>
<ul>
  <li>전체 JSON 스키마와 모든 종료 코드: <a href="/ko/cli/agents/">에이전트를 위한 marsdawn</a>.</li>
  <li>Claude Code와 비슷한 에이전트를 위한 파일 하나짜리 스킬: <a href="/ko/cli/skill/">marsdawn 스킬</a>.</li>
  <li>간결한 JSON 결과가 에이전트 자신의 컨텍스트에 중요한 이유: <a href="/ko/token-efficient-review/">토큰을 아끼는 검토</a>.</li>
</ul>
""",
    }

    pages['vs/markdown-preview-tools'] = {
        "title": '다른 도구로 Markdown 보기와 MarsDawn 비교 · MarsDawn',
        "description": 'VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.',
        "body": f"""
<section class="intro">
  <h1>다른 도구로 Markdown 보기와 MarsDawn.</h1>
  <p>VS Code, 브라우저, Claude Desktop이 이미 열려 있다면 Markdown 파일을 잠깐 볼 때 그중 하나를 쓰는 것도 자연스럽습니다. 각각이 실제로 무엇을 렌더링하는지, 거기까지 가는 데 무엇이 드는지를 같은 파일을 MarsDawn에서 여는 것과 비교해 보세요.</p>
</section>

<h2>한눈에 보기</h2>
<!--compare:preview-tools-->

<h2>VS Code의 기본 미리보기</h2>
<p>VS Code에서 <kbd>&#8984;&#8679;V</kbd>를 누르면 기본 미리보기 패널에 Markdown 파일이 렌더링됩니다. 무료이고 따로 설치할 것도 없습니다. VS Code 1.121(2026년 5월)부터는 이 미리보기가 Mermaid 다이어그램도 기본으로 렌더링합니다. Microsoft가 Mermaid 확장 프로그램을 VS Code 자체에 넣었기 때문에, 예전에는 별도 확장 프로그램이 필요했지만 이제는 필요 없습니다. 하지 않는 일: 이것은 편집기 안의 미리보기 패널이지, 읽기 위해 만든 편집기가 아닙니다. 패널 옆에는 파일 트리, 터미널, 그 밖에 VS Code가 보여 줄 수 있는 온갖 패널이 있고, VS Code 자체는 파일 하나를 읽으려고 여는 앱이 아니라 개발 환경 전체로 설치하는 Electron 앱입니다.</p>

<h2>로컬 파일용 브라우저 확장 프로그램</h2>
<p>로컬 <code>.md</code> 파일을 읽는 데 압도적으로 쓰이는 브라우저 확장 프로그램은 없습니다. Local Markdown Viewer, Markdown Viewer, MarkView 등이 거의 같은 일을 하며, 어느 것도 기본으로 깔려 있지 않습니다. 모두 무언가를 열기 전에 같은 단계가 하나 더 필요합니다. 브라우저는 기본적으로 확장 프로그램이 <code>file://</code> 페이지를 읽지 못하게 막기 때문에, 해당 확장 프로그램에서 ‘파일 URL에 대한 액세스 허용’을 켜야 합니다. 확장 프로그램마다 한 번 주는 권한이라, 줬다는 사실이나 그 이유를 잊기 쉽습니다. 권한을 켜면 파일이 브라우저 탭에 렌더링됩니다. 즉, 파일 하나를 보려고 브라우저 전체를 실행하는 셈입니다.</p>

<h2>Claude Desktop의 파일 미리보기</h2>
<p>Claude Desktop은 이미 프로젝트나 대화에 들어 있는 파일을 보여 줍니다. 디스크의 아무 파일이나 둘러보는 용도로 만든 것은 아닙니다. 볼 수 있는 것은 대화에 이미 들어 있는 것이지, 작업 옆에 열어 두는 노트 폴더가 아닙니다. Anthropic이 직접 밝힌 <a href="https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai">업로드할 수 있는 문서 유형</a>은 PDF, DOCX, CSV, TXT, HTML, ODT, RTF, EPUB, JSON, XLSX이며, Markdown은 목록에 없습니다.</p>

<h2>파일 하나를 읽으려고 브라우저 엔진을</h2>
<p>VS Code는 Electron 앱입니다. Chromium과 Node.js 런타임을 통째로 담고 있으며, 네이티브 Mac 앱이 아닙니다. 브라우저 확장 프로그램은 실제 브라우저 안에서 실행됩니다. 어느 쪽이든 Markdown 파일 하나를 보려고 브라우저 엔진 전체가 돌아갑니다. MarsDawn은 네이티브 AppKit 앱입니다. 브라우저 런타임을 담고 있지 않으며, 설치할 확장 프로그램이나 기억해야 할 권한 설정 없이 로컬 파일을 바로 엽니다.</p>

<h2>다음</h2>
<ul>
  <li>MarsDawn도 하지 않는 일: <a href="/ko/limits/">목록</a>.</li>
  <li>지금 무료로 어떤 Markdown 파일이든 PDF로 바꾸기: <a href="/ko/markdown-to-pdf/">Markdown을 PDF로</a>.</li>
  <li>네이티브 Mac 뷰어와 비교하기: <a href="/ko/vs/macmd-viewer/">MacMD Viewer와 MarsDawn</a>.</li>
</ul>
""",
    }

    pages['themes'] = {
        "title": 'MarsDawn의 미리보기 테마와 PDF 내보내기 · MarsDawn',
        "description": '라이트와 다크 팔레트를 각각 갖춘 미리보기 테마 네 가지, 그리고 지금 쓰는 테마를 그대로 따르는 PDF 내보내기와 프린트. 브라우저에서 테마를 직접 만들고, 커뮤니티 갤러리도 둘러보세요.',
        "body": f"""
<section class="intro">
  <h1>여덟 가지 모습, 하나의 내보내기.</h1>
  <p>MarsDawn에는 새벽, 클래식, 모던, 비비드 네 가지 미리보기 테마가 있고, 각각 라이트와 다크 팔레트를 갖추고 있습니다. 문서를 읽는 여덟 가지 조합입니다. PDF로 내보내거나 프린트하면, 읽고 있던 바로 그 조합으로 페이지가 나옵니다.</p>
</section>

<div class="summary"><p><strong>테마 네 가지 &#215; 라이트와 다크 = 문서를 읽는 여덟 가지 방법, 그리고 고른 것을 그대로 따르는 하나의 내보내기 경로.</strong> <a href="/ko/themes/new/">브라우저에서 직접 만들거나</a>, <a href="/ko/themes/gallery/">갤러리</a>에서 다른 사람이 올린 것을 둘러보세요.</p></div>

<h2>네 가지 테마</h2>
<!--theme-gallery-->
<ul>
  <li><strong>새벽</strong>, 기본 테마: 이 사이트를 이루는 것과 같은 따뜻한 종이 색과 Mars Rust 강조색.</li>
  <li><strong>클래식</strong>: 더 담백하고 문서다운 팔레트.</li>
  <li><strong>모던</strong>: 더 차분하고 현대적인 팔레트.</li>
  <li><strong>비비드</strong>: 더 밝고 대비가 강한 팔레트.</li>
</ul>
<p>테마마다 라이트와 다크 변형이 따로 있어서, Mac의 화면 모드를 바꾸면 인터페이스만이 아니라 테마의 팔레트도 함께 바뀝니다.</p>

<h2>PDF 내보내기와 프린트도 같은 테마로</h2>
<p>PDF로 내보내거나 프린트하면 페이지는 테마의 라이트 팔레트를 씁니다. Mermaid 다이어그램이 그대로 그려지고, 코드 블록은 구문 강조를 유지하며, 페이지 나눔은 제목과 본문을 떼어 놓거나 표나 다이어그램을 반으로 자르지 않습니다. 무료 <a href="/ko/cli/">marsdawn 명령줄 도구</a>도 같은 내보내기 엔진을 쓰므로, 스크립트나 에이전트도 <code>--theme</code>으로 네 가지 테마 중 어느 것이든 똑같은 PDF를 만듭니다.</p>

<h2>직접 만들고, 다른 사람이 만든 것도 둘러보세요</h2>
<p><a href="/ko/themes/new/">브라우저에서 테마를 만드세요</a>. 색과 몇 가지 스타일 옵션을 고르고, 실시간으로 적용된 모습을 본 뒤, 검토용 GitHub 이슈로 제출하면 됩니다. 설치도 git도 필요 없습니다. <a href="/ko/themes/gallery/">갤러리</a>에는 유지 관리자가 검토하고 병합한 제출 테마가 나열됩니다. 검토 창구가 막 열렸기 때문에 오늘은 비어 있지만, 통과한 테마는 여기에 나타나며 용도로 걸러 볼 수 있습니다.</p>

<h2>다음</h2>
<ul>
  <li>명령줄에서 PDF로 내보내는 전체 안내: <a href="/ko/markdown-to-pdf/">Markdown을 PDF로</a>.</li>
  <li>MarsDawn이 아직 하지 않는 일: <a href="/ko/limits/">목록</a>.</li>
  <li>Markdown을 쓰지 않는 사람에게 내보낸 PDF 전달하기: <a href="/ko/sharing-exported-pdfs/">PDF 공유하기</a>.</li>
</ul>
""",
    }


    pages['themes/new'] = {
        "title": "브라우저에서 MarsDawn 테마 만들기 · MarsDawn",
        "description": "색과 몇 가지 스타일 옵션을 고르면 샘플 문서에 바로 반영됩니다. 만든 테마는 GitHub 이슈로 제출할 수 있습니다. 설치도 git도 필요 없습니다.",
        "body": """
<section class="intro">
  <h1>테마 만들기</h1>
  <p>아래에서 팔레트와 몇 가지 스타일 옵션을 고르세요. 오른쪽 샘플 문서가 라이트와 다크 모두에서 바로바로 바뀌고, 테마 갤러리 CI가 돌리는 검사도 여기에 표시됩니다. 제출용 이슈에 도착할 즈음에는 대개 이미 통과한 상태입니다.</p>
  <p>제출하려면 GitHub 계정이 필요합니다. 이 페이지 자체는 설치도 git도 필요 없습니다.</p>
</section>
<div id="theme-sim-app" data-locale="ko"><p>이 페이지에서 테마를 만들고 미리 보려면 JavaScript가 필요합니다.</p></div>
""",
    }
    pages['themes/gallery'] = {
        "title": "테마 갤러리: MarsDawn 커뮤니티 테마 · MarsDawn",
        "description": "커뮤니티가 MarsDawn에 제출한 미리보기 테마를 둘러보고, 용도로 걸러 보고, 문제가 있으면 신고하세요. 브라우저에서 직접 만드세요. 설치도 git도 필요 없습니다.",
        "body": f"""
<section class="intro">
  <h1>테마 갤러리</h1>
  <p>커뮤니티가 제출한 미리보기 테마입니다. 각각 개발자가 검토하고 병합한 뒤에야 여기에 나타납니다. 용도로 걸러 보거나, <a href="/ko/themes/new/">브라우저에서 직접 만드세요</a>. 설치도 git도 필요 없습니다.</p>
</section>
<!--community-theme-gallery-->
<h2>크레딧 및 라이선스</h2>
<p>Dracula, Nord, Gruvbox, Solarized는 오픈 소스 배색 프로젝트를 바탕으로 합니다. 각 프로젝트의 저작권 표시와 전체 라이선스 본문은 <a href="/themes/third-party-notices.html">서드파티 고지</a>에서 확인하세요.</p>
<h2>테마에 문제가 있나요?</h2>
<p>카드의 «신고» 버튼을 쓰거나(JavaScript 필요), 테마 이름과 버전을 적어 <a href="mailto:{k.EMAIL}">{k.EMAIL}</a>로 직접 메일을 보내세요. JavaScript 여부와 관계없습니다. 신고는 사람이 직접 검토하며, 문제로 확인되면 하루 안에 목록에서 내립니다.</p>
""",
    }

    compare_tables['mcp-choice'] = {
        'head': ['에이전트가', '쓸 것', '필요한 것'],
        'rows': [
            ['셸 명령을 실행할 수 있다면', '<a href="{root}cli/agents/">CLI</a>', 'macOS 15 이상'],
            ['Claude Code처럼 지침 파일을 불러온다면', '<a href="{root}cli/skill/">스킬 파일</a>', 'CLI(스킬이 설치해 줌)'],
            ['MCP로 도구를 호출한다면', '<a href="{mcp}">marsdawn-mcp</a>', 'marsdawn-mcp 0.2.1 이상, marsdawn 0.5.0 이상, Node.js 20 이상'],
        ],
    }
    compare_tables['preview-tools'] = {
        'head': ['', 'VS Code 미리보기', '브라우저 확장 프로그램', 'Claude Desktop', 'MarsDawn'],
        'rows': [
            ['디스크의 Markdown 파일 열기', '예', '예, 파일 접근을 허용한 뒤', '아니요. Markdown이 업로드 목록에 없음', '예'],
            ['첫 파일을 열기 전에', '개발 환경 전체인 VS Code 설치', '확장 프로그램 설치 후 ‘파일 URL에 대한 액세스 허용’ 켜기', '디스크의 파일을 둘러볼 수 없음', 'MarsDawn 설치'],
            ['만든 목적', '코드 작성. 미리보기는 여러 패널 중 하나', '웹 브라우징', 'Claude와의 대화', 'Markdown 읽기와 편집'],
            ['페이지를 그리는 방식', 'Electron: Chromium과 Node.js 내장', '브라우저 전체', 'Claude Desktop 앱', '네이티브 AppKit 앱. 페이지는 WebKit이 그림'],
        ],
    }
    theme_shots = {
        '01-split': ('새벽(기본 테마)', '분할 화면의 새벽 테마: 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.'),
        '02-classic': ('클래식', '미리보기가 윈도우 전체를 채운 클래식 테마.'),
        '04-vivid': ('비비드', '분할 화면의 비비드 테마.'),
        '03-dark': ('다크 모드', '다크 모드의 MarsDawn, 분할 화면.'),
    }
    theme_gallery_note = '모던은 아직 스크린샷이 없어서, 네 번째 이미지는 대신 다크 모드를 보여 줍니다.'

    pages['token-efficient-review'] = {
        "title": '에이전트의 토큰을 쓰지 않고 MarsDawn의 결과 검토하기 · MarsDawn',
        "description": '렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.',
        "body": f"""
<section class="intro">
  <h1>에이전트의 토큰을 쓰지 않고 검토하세요.</h1>
  <p>이 반복 과정에서는 서로 다른 두 가지가 저렴하게 유지됩니다. 에이전트가 도구를 호출하고 돌려받는 것, 그리고 결과가 제대로 나왔는지 확인하는 데 드는 것입니다.</p>
</section>

<div class="summary"><p><strong>도구 호출은 렌더링된 페이지가 아니라 작은 JSON 객체를 돌려주고, 렌더링된 페이지는 사람이 MarsDawn에서 검토합니다. 에이전트의 컨텍스트로 다시 읽어 들이는 일은 없습니다.</strong></p></div>

<h2>도구 호출 자체가 저렴합니다</h2>
<p><code>marsdawn export</code>를 CLI, 스킬, <a href="/ko/cli/mcp/">MCP 서버</a> 중 어디서든 호출하면 돌아오는 것은 <a href="/ko/cli/agents/">간결한 JSON 객체</a>입니다. <code>ok</code>, <code>output</code>, <code>pages</code>, <code>theme</code>, <code>paper</code>, <code>diagramErrors</code>. 전체 스키마는 <a href="/schemas/cli/export.v1.json">export.v1.json</a>입니다. 이 중 어느 것도 렌더링된 문서가 아닙니다. Mermaid 다이어그램이 열두 개 들어 있는 50페이지짜리 PDF도 한 페이지짜리 메모와 똑같은 몇 개의 필드만 돌려줍니다.</p>

<h2>검토는 옆에서 이루어집니다</h2>
<p>PDF가 만들어지면 사람이 MarsDawn이나 아무 PDF 뷰어에서 열어 렌더링된 다이어그램, 수식, 레이아웃을 읽습니다. 제대로 나왔는지 확인하려고 에이전트가 렌더링 결과를 자신의 컨텍스트 윈도우로 다시 읽어 들일 필요는 전혀 없습니다. 검토는 다이어그램이 어떻게 생겼는지 설명하느라 토큰을 한 번 더 주고받는 방식이 아니라, 별도의 윈도우와 별도의 화면에서 이루어집니다.</p>

<h2>이렇게 하면 피할 수 있는 것</h2>
<ul>
  <li>내보내기가 잘 됐는지 에이전트가 확인하게 하려고 렌더링된 Markdown, 스크린샷, 또는 그 설명을 대화에 다시 붙여 넣는 일.</li>
  <li>사람이 그냥 보면 될 것을, Mermaid 다이어그램이나 KaTeX 수식이 어떻게 렌더링되는지 에이전트가 재구성해야 하는 일.</li>
  <li>첫 번째 호출이 이미 성공을 알렸는데도 PDF 내용을 가져오려고 도구를 한 번 더 호출하는 일.</li>
</ul>

<h2>다음</h2>
<ul>
  <li>marsdawn을 호출하는 세 가지 방법, CLI, 스킬 파일, MCP 서버: <a href="/ko/cli/mcp/">세 가지 입구</a>.</li>
  <li>JSON 결과의 모든 필드: <a href="/ko/cli/agents/">에이전트를 위한 marsdawn</a>.</li>
  <li>에이전트가 쓴 글을 여전히 사람이 읽어야 하는 이유: <a href="/ko/reviewing-ai-output/">검토가 필요한 이유</a>.</li>
  <li>에이전트의 결과를 읽어야 하는 이유를 더 자세히, 체크리스트와 함께: <a href="/ko/reading-agent-output/">에이전트가 돌려준 결과 읽기</a>.</li>
</ul>
""",
    }

    pages['sharing-exported-pdfs'] = {
        "title": 'Markdown을 가르치지 않고 에이전트가 쓴 글 공유하기 · MarsDawn',
        "description": '에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.',
        "body": f"""
<section class="intro">
  <h1>Markdown 말고 PDF를 건네세요.</h1>
  <p>에이전트가 문서를 끝내고, 여러분이 검토하고 고친 다음, 엔지니어링 밖의 누군가도 읽어야 할 때가 있습니다. 관리자, 고객, 다른 팀 사람 같은 경우입니다. 그들은 <code>##</code>이나 세로 막대로 만든 표가 무슨 뜻인지 알 필요가 없습니다. PDF로 내보내서 그것을 건네세요.</p>
</section>

<div class="summary"><p><strong>검토를 마친 문서를 PDF로 내보내고 그 파일을 보내세요.</strong> 어디서든 열리고, Markdown 지식도 설치도 필요 없으며, 다이어그램, 표, 서식까지 미리보기에서 본 모습 그대로입니다.</p></div>

<h2>.md 파일을 그냥 보내면 안 되는 이유</h2>
<p>원본 <code>.md</code> 파일을 일반 텍스트 편집기로 열면 페이지가 아니라 기호가 보입니다. 제목을 뜻하는 <code>#</code>, 굵은 글씨를 감싼 <code>**</code>, 그려지지 않은 Mermaid 다이어그램의 코드 블록. Markdown을 쓰지 않는 사람은 이 중 어느 것도 의도대로 읽지 못하며, 문서 하나 때문에 뷰어부터 설치해 달라고 하기는 무리입니다.</p>

<h2>스크린샷이 아닌 이유</h2>
<p>스크린샷은 여러 페이지일 수 있는 문서를 한 화면 분량으로 굳혀 버리고, 검색이나 선택도 안 되며, 몇 번 압축되고 전달되면 더 읽기 어려워집니다. PDF는 길이와 상관없이 텍스트, 다이어그램, 페이지 나눔을 그대로 지킵니다.</p>

<h2>PDF로 얻는 것</h2>
<ul>
  <li>받는 사람이 이미 가진 것, 미리보기, 브라우저, Acrobat, 휴대폰에서 열립니다. Markdown 도구는 필요 없습니다.</li>
  <li>Mermaid 다이어그램은 코드로 남지 않고 그려져 있으며, 코드 블록은 강조 표시를 유지합니다.</li>
  <li>페이지 나눔은 제목이 페이지 맨 아래에 홀로 남지 않도록, 표나 다이어그램이 두 페이지로 갈라지지 않도록 정해집니다.</li>
  <li>MarsDawn 앱에서 만들든 무료 명령줄에서 만들든 같은 파일입니다. 단계별 안내는 <a href="/ko/markdown-to-pdf/">Markdown을 PDF로</a>를 참고하세요.</li>
</ul>

<h2>다음</h2>
<ul>
  <li>내보내기에 쓸 수 있는 테마와 레이아웃: <a href="/ko/themes/">미리보기 테마와 PDF 내보내기</a>.</li>
  <li>앱 대신 스크립트나 에이전트에서 내보내기: <a href="/ko/cli/agents/">에이전트를 위한 marsdawn</a>.</li>
  <li>사람이 먼저 문서를 읽어야 하는 이유: <a href="/ko/reviewing-ai-output/">검토가 필요한 이유</a>.</li>
  <li>여러 에이전트 사이의 인수인계는 공유할 PDF가 자연스럽게 생기는 곳입니다: <a href="/ko/agent-design-patterns/">네 가지 에이전트 설계 패턴과 각각이 건네는 문서</a>.</li>
</ul>
""",
    }

    pages['reviewing-ai-output'] = {
        "title": 'AI의 결과물에 여전히 사람 독자가 필요한 이유 · MarsDawn',
        "description": 'AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.',
        "body": f"""
<section class="intro">
  <h1>에이전트가 씁니다. 이해하는 것은 여전히 여러분의 몫입니다.</h1>
  <p>AI 에이전트는 계획, 사양서, 메모를 빠르게 써 냅니다. 하지만 그 결과물은 매끄럽게 읽힌다는 이유로 믿을 것이 아니라, 그것을 바탕으로 행동할 사람이 이해해야 합니다.</p>
</section>

<div class="summary"><p><strong>MarsDawn은 바로 그 읽기를 위해 만들어졌습니다. 렌더링된 페이지를 원본 옆에 두고, Mermaid 다이어그램과 KaTeX 수식을 기호로 남기지 않고 그려 주어, 문서의 구조를 한눈에 읽을 수 있게 합니다.</strong></p></div>

<h2>매끄럽다고 맞는 것은 아닙니다</h2>
<p>AI의 도움을 받는 코딩에 관해 쓰면서, Simon Willison은 버리지 않고 계속 손볼 코드에 대해 이렇게 말했습니다. “바탕이 되는 코드의 품질과 이해 가능성이 결정적이다”(<a href="https://simonwillison.net/2025/Mar/6/vibe-coding/">Vibe coding</a>, 2025). 문서도 마찬가지입니다. 매끄럽게 읽히는 에이전트의 초안도 구조, 숫자, 논리를 틀릴 수 있으며, 유창한 문장은 어느 부분을 확인해야 하는지 알려 주지 않습니다.</p>

<h2>컴파일이 아니라 추론</h2>
<p>Thoughtworks에 글을 쓴 Birgitta Böckeler는 그 차이를 분명히 짚습니다. “LLM은 자연어의 컴파일러, 인터프리터, 트랜스파일러, 어셈블러가 아니다. 추론기다”(<a href="https://martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html">I still care about the code</a>). 컴파일러는 입력을 받아들이거나 오류를 보고하지만, 에이전트는 맞지 않으면서도 실행되거나 읽히는 무언가를 돌려줄 수 있습니다. 누군가는 여전히 확인해야 합니다.</p>

<h2>MarsDawn이 그 독자에게 주는 것</h2>
<ul>
  <li>렌더링된 페이지를 원본 옆에 두고 어느 쪽이 바뀌든 함께 업데이트해, 본문의 주장과 그 구조를 동시에 볼 수 있습니다.</li>
  <li>Mermaid 다이어그램을 그려 줍니다. 에이전트가 글로 설명한 순서도가 실제로 따라갈 수 있는 모양이 됩니다.</li>
  <li>KaTeX 수식을 백슬래시 문자열로 남기지 않고 렌더링합니다. 수식이 수식으로 읽힙니다.</li>
  <li>저절로 실행되는 것은 없습니다. MarsDawn은 문서를 대신 평가하거나 요약하거나 표시하지 않습니다. 여러분이 할 수 있도록 구조를 눈앞에 보여 줄 뿐입니다.</li>
</ul>

<h2>다음</h2>
<ul>
  <li>그 검토가 에이전트 자신의 컨텍스트에 부담을 주지 않는 방법: <a href="/ko/token-efficient-review/">토큰을 아끼는 검토</a>.</li>
  <li>검토한 문서를 다른 사람에게 전달하기: <a href="/ko/sharing-exported-pdfs/">PDF 공유하기</a>.</li>
  <li>왜 읽기 어려운지, 어떻게 읽으면 되는지: <a href="/ko/reading-agent-output/">에이전트가 돌려준 결과 읽기</a>.</li>
  <li>에이전트가 애초에 계획을 펼쳐 보이는 이유: <a href="/ko/agent-transparency/">Anthropic은 에이전트가 투명해야 한다고 말합니다. 그럼 펼쳐 놓은 것은 누가 읽을까요?</a></li>
  <li>MarsDawn이 무엇인지 한 페이지로: <a href="/ko/">홈페이지</a>.</li>
</ul>
""",
    }

    pages['reading-agent-output'] = {
        "title": '에이전트가 돌려준 결과 읽기 · MarsDawn',
        "description": 'AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.',
        "body": f"""
<section class="intro">
  <h1>에이전트의 작업은 Markdown 파일로 돌아옵니다.</h1>
  <p>코딩 에이전트에게 마이그레이션 계획, 사양서 작성, 버그 추적을 맡깁니다. 에이전트는 한동안 혼자 일한 다음 파일 하나를 건넵니다. <code>plan.md</code>, <code>SPEC.md</code>, 진행 보고서, 조사 요약. 여러분이 작업을 확인할 수 있는 범위에서는 그 파일이 곧 작업입니다.</p>
</section>

<div class="summary"><p><strong>에이전트가 제대로 했는지는 에이전트가 돌려준 것을 읽어 봐야 압니다. MarsDawn은 그 읽기를 위한 Mac 앱입니다.</strong></p></div>

<h2>에이전트를 만드는 사람들이 하는 말</h2>
<p>쓰인 그대로 인용하고, 우리의 해석은 그 뒤에 적습니다.</p>
<ul>
  <li>Anthropic의 “Building Effective Agents”(Erik S., Barry Zhang, 2024년 12월)는 에이전트를 만드는 세 가지 핵심 원칙을 제시합니다. 그중 하나는 “에이전트의 계획 단계를 명시적으로 보여 줌으로써 투명성을 우선하라”입니다. 이 글은 에이전트를 만드는 사람을 위해 쓰였습니다. 여러분 쪽에서 보면 그 투명성은 결국 여러분이 읽게 되는 계획입니다.</li>
  <li>같은 글에서: “그러면 에이전트는 체크포인트에서 또는 장애물을 만났을 때 사람의 피드백을 받기 위해 멈출 수 있다.” 동사에 주목하세요. <em>할 수 있다</em>입니다.</li>
  <li>Chip Huyen은 “Agents”(2025년 1월)에서 계획을 실행과 분리해야 하는 이유를 이렇게 설명합니다. “감독이 없으면 에이전트는 그 단계들을 몇 시간 동안 실행하며 API 호출에 시간과 돈을 낭비할 수 있고, 여러분은 그제야 그것이 아무 데도 가지 못하고 있음을 깨닫는다.” 또 “에이전트가 작업을 끝내지 않았는데도 끝냈다고 확신하는” 실패도 설명합니다. 50명을 호텔 객실 30개에 배정하라고 하면 40명만 배정하고 다 했다고 우깁니다.</li>
  <li>Andrew Ng은 The Batch(2024년 4월)에서 계획 설계 패턴에 대해 이렇게 말합니다. “한편으로 계획은 매우 강력한 능력이지만, 다른 한편으로는 결과를 덜 예측 가능하게 만든다.” 이는 예측 가능성에 관한 지적이지 사람의 검토를 요구하는 말이 아니며, 그는 계획 능력이 빠르게 나아질 것으로 봅니다.</li>
</ul>
<p><strong>그들의 말이 아니라 우리의 추론입니다.</strong> 에이전트가 계획을 펼쳐 보이고 체크포인트에서 멈춘다면, 누군가는 그 체크포인트에서 계획을 읽어야 하고, 대개 그 사람은 여러분입니다. 에이전트가 끝나지 않았는데도 끝났다고 생각할 수 있다면, ‘완료’ 보고에도 읽는 사람이 필요합니다. 이 저자들 중 누구도 MarsDawn을 언급하거나 MarsDawn 또는 다른 Markdown 도구를 추천하지 않습니다.</p>

<h2>보기보다 읽기 어려운 이유</h2>
<p>파일은 길고, 중요한 부분은 위쪽에 있는 경우가 드뭅니다. 소스로는 따라가기 어려운 Mermaid 다이어그램과 수식이 들어 있습니다. 여러분이 절반쯤 읽는 동안에도 에이전트가 파일을 고쳐 쓰고 있을 수 있습니다. 여러 파일 중 하나인 경우가 많고, 때로는 여러 브랜치나 워크트리에 흩어져 있습니다. 그리고 문제를 발견했을 때 “캐시 부분이 좀 이상해”라고 하면 에이전트는 짐작할 수밖에 없지만, “<code>docs/plan.md:42</code>에서 백필이 끝나기 전에 이전 테이블을 삭제함”이라고 하면 그렇지 않습니다.</p>

<h2>MarsDawn이 돕는 부분</h2>
<ul>
  <li><strong>긴 파일:</strong> 사이드바의 개요 탭(&#8963;&#8984;S)에 제목이 나열됩니다. 하나를 클릭하면 두 패널이 모두 그곳으로 이동합니다.</li>
  <li><strong>다이어그램과 수식:</strong> Mermaid와 KaTeX가 소스 옆 미리보기에 그려지고(&#8984;2), 두 패널이 함께 스크롤됩니다.</li>
  <li><strong>읽는 동안 고쳐 쓰일 때:</strong> 에이전트가 파일을 고쳐 쓰면 MarsDawn이 다시 불러오고 읽던 위치를 유지합니다. 여러분이 저장하지 않은 편집이 없는 한 그렇습니다.</li>
  <li><strong>여러 파일:</strong> 파일 &#9656; 폴더 열기&#8230;(&#8679;&#8984;O)로 에이전트의 폴더를 여세요. 새 파일은 약 1초 안에 파일 탭에 나타나고, git 체크아웃이라면 헤더에 브랜치나 워크트리 이름이 표시됩니다.</li>
  <li><strong>정확한 피드백:</strong> 편집 &#9656; 참조 복사(&#8997;&#8984;C)는 현재 위치를 <code>docs/plan.md:42</code> 형식으로 복사합니다. AI용으로 복사(&#8963;&#8997;&#8984;C)는 그 아래에 선택한 텍스트를 덧붙입니다. 어느 쪽이든 에이전트와의 채팅에 붙여 넣으세요.</li>
</ul>
<p>반복 과정에 쓸 것이 두 가지 더 있습니다. 에이전트는 <code>marsdawn open plan.md:42</code>를 실행해 여러분이 가장 먼저 봤으면 하는 42번째 줄에서 MarsDawn으로 파일을 열 수 있고, 검토를 마친 파일은 앱에서 또는 무료 <code>marsdawn export</code> 명령으로 PDF로 내보낼 수 있습니다.</p>
<p>MarsDawn 안에는 AI 모델이 없습니다. 계획을 요약하거나, 평가하거나, 무엇이 틀렸는지 알려 주지 않습니다. 읽는 것은 여러분이고, MarsDawn은 길고 계속 바뀌는 파일을 읽기 좋게 유지하며 정확한 줄을 가리킬 수 있게 해 줍니다.</p>

<h2>에이전트의 계획을 5분 만에 검토하기</h2>
<p>어떤 편집기에서든 쓸 수 있는 방법입니다.</p>
<ol>
  <li>제목만 읽으세요. 개요가 요청한 내용과 맞나요? 빠진 섹션은 대개 빠진 작업을 뜻합니다.</li>
  <li>무언가가 완료되었다, 통과했다, 확인했다고 말하는 곳을 모두 찾아 하나는 직접 확인하세요. 파일을 열고, 테스트를 실행하고, 행을 세어 보세요.</li>
  <li>되돌릴 수 없는 단계를 찾으세요. 데이터 삭제, 마이그레이션, 강제 푸시, 무언가를 보내거나 결제하거나 게시하는 모든 것. 이런 단계는 여러분의 명시적인 승인을 기다려야 합니다.</li>
  <li>다이어그램을 렌더링된 상태로 읽고, 화살표 하나하나를 본문과 대조하세요.</li>
  <li>계획이 건드리는 파일과 시스템을 나열하세요. 요청하지 않은 것이 있으면 실행되기 전에 물어보세요.</li>
  <li>피드백은 위치, 문제, 해결책 순서로 쓰세요. “<code>plan.md:88</code>: 백필이 삭제 다음에 실행됨. 4단계와 5단계를 바꿀 것.” 한 줄에 문제 하나씩.</li>
</ol>
<p>시간이 없다면 2단계만 하세요. 끝났다고 착각하는 에이전트는 거기서 잡힙니다. 실제 예시를 곁들인 긴 버전: <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 만에 검토하기</a>.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 <a href="{k.LISTING_URL}">Mac App Store</a>에 있습니다. 무료 <code>marsdawn</code> 명령줄 도구도 있습니다.</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>앱 없이 Markdown을 PDF로 내보내며, <code>marsdawn open</code>을 쓰면 에이전트가 여러분 대신 MarsDawn에서 파일을 열 수 있습니다.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; <a href="/ko/cli/agents/">에이전트를 위한 marsdawn</a> &#183; 구입 전에 알아 두세요: <a href="/ko/limits/">MarsDawn이 하지 않는 일</a></p>

<h2>다음</h2>
<ul>
  <li>AI의 결과물을 왜 읽어야 하는지 짧게: <a href="/ko/reviewing-ai-output/">AI의 결과물에 여전히 사람 독자가 필요한 이유</a>.</li>
  <li>검토하는 동안 에이전트의 컨텍스트를 작게 유지하기: <a href="/ko/token-efficient-review/">토큰을 아끼는 검토</a>.</li>
  <li>에이전트가 애초에 계획을 펼쳐 보이는 이유: <a href="/ko/agent-transparency/">Anthropic은 에이전트가 투명해야 한다고 말합니다. 그럼 펼쳐 놓은 것은 누가 읽을까요?</a></li>
  <li>위 체크리스트를 예시와 함께 단계별로: <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 만에 검토하기</a>.</li>
  <li>여러 종류의 에이전트가 건네는 문서: <a href="/ko/agent-design-patterns/">네 가지 에이전트 설계 패턴과 각각이 건네는 문서</a>.</li>
</ul>

<h2>출처</h2>
<ul>
  <li>Erik S., Barry Zhang, “Building Effective Agents”, Anthropic, 2024년 12월 19일: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (2026-09-26 기준 온라인 버전에서 인용. 현재 이 글에는 설명된 도구 중 상당수가 2024년 12월 이후 바뀌었다는 안내가 붙어 있습니다.)</li>
  <li>Chip Huyen, “Agents”, 2025년 1월 7일: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Andrew Ng, “Agentic Design Patterns Part 4, Planning”, The Batch, 2024년 4월 10일: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
</ul>
""",
    }

    pages['agent-transparency'] = {
        "title": '에이전트는 투명해야 합니다. 보여 준 것은 누가 읽을까요? · MarsDawn',
        "description": 'Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.',
        "body": f"""
<section class="intro">
  <h1>Anthropic은 에이전트가 투명해야 한다고 말합니다. 그럼 펼쳐 놓은 것은 누가 읽을까요?</h1>
  <p>2024년 12월 Anthropic은 AI 에이전트를 만드는 사람들을 위한 가이드 “Building Effective Agents”를 발표했습니다. 요약에는 세 가지 원칙이 나오고, 그중 하나가 투명성입니다. 이 글은 그 원칙의 반대편 끝에 관한 이야기입니다. 에이전트가 단계를 펼쳐 놓으면, 누군가는 그것을 읽어야 합니다.</p>
</section>

<div class="summary"><p><strong>투명성은 에이전트가 하는 일이고, 읽기는 여러분이 하는 일입니다. Anthropic은 만드는 사람들에게 에이전트의 계획 단계를 보여 달라고 합니다. 코딩 에이전트를 부리는 대부분의 사람에게 그 단계는 누군가 적절한 순간에 읽어야 하는 Markdown 파일로 도착합니다.</strong></p></div>

<h2>가이드가 말하는 것</h2>
<p>Erik S.와 Barry Zhang은 조언을 이렇게 요약합니다.</p>
<blockquote><p>“에이전트를 구현할 때 우리는 세 가지 핵심 원칙을 따르려고 한다. 에이전트의 설계를 단순하게 유지하라. 에이전트의 계획 단계를 명시적으로 보여 줌으로써 투명성을 우선하라. 철저한 도구 문서화와 테스트를 통해 에이전트와 컴퓨터 사이의 인터페이스(ACI)를 신중하게 설계하라.”</p></blockquote>
<p>이는 에이전트를 만드는 사람을 위한 설계 원칙이지, 에이전트를 쓰는 사람을 위한 지침이 아닙니다. 원칙은 단계를 보여 달라고 요구할 뿐, 누가 읽는지는 말하지 않습니다.</p>
<p>같은 글은 에이전트가 작업을 받은 뒤 하는 일을 이렇게 설명합니다. “작업이 명확해지면 에이전트는 독립적으로 계획하고 실행하며, 추가 정보나 판단이 필요할 경우 사람에게 돌아올 수도 있다.” 그리고 “그러면 에이전트는 체크포인트에서 또는 장애물을 만났을 때 사람의 피드백을 받기 위해 멈출 수 있다.” <em>수도 있다</em>와 <em>수 있다</em>라는 표현을 보세요. 체크포인트는 에이전트가 반드시 가져야 하는 것이 아니라 가질 수 있는 것으로 설명됩니다.</p>

<h2>확인의 대부분은 여러분이 하지 않습니다</h2>
<p>이 부분은 과장하기 쉬우니, 가이드가 실제로 무엇을 앞세우는지 보겠습니다. 에이전트는 바깥 세계에 비추어 스스로를 확인합니다. “실행 중에는 에이전트가 진행 상황을 평가하기 위해 각 단계에서 환경으로부터 ‘실측 정보(ground truth)’(도구 호출 결과나 코드 실행 결과 등)를 얻는 것이 매우 중요하다.” 이 문장에서 실측 정보란 테스트 결과와 도구 출력이지, 사람이 아닙니다.</p>
<p>가이드는 위험에 대해서도 직설적입니다. “에이전트의 자율적인 특성은 더 높은 비용과 오류가 누적될 가능성을 뜻한다.” 그에 대한 답은 샌드박스 환경에서의 광범위한 테스트와 안전장치입니다. “더 꼼꼼히 읽으라”고는 하지 않습니다.</p>
<p>사람은 뒤쪽, 코딩 에이전트에 관한 부록에서 등장합니다. “하지만 자동화된 테스트가 기능 검증을 돕는다 해도, 해결책이 더 넓은 시스템 요구 사항에 부합하는지 확인하려면 사람의 검토가 여전히 매우 중요하다.” 이 문장은 코드에 관한 것입니다. 하지만 이 문장이 가리키는 빈틈은 어떤 에이전트에서든 익숙합니다. 테스트는 무언가가 동작한다는 것을 알려 줄 수는 있어도, 그것이 여러분이 의도한 것인지는 알려 주지 못합니다.</p>

<h2>단계는 어디로 가는가</h2>
<p><strong>여기서부터는 Anthropic이 아니라 우리의 해석입니다.</strong></p>
<p>코딩 에이전트를 매일 쓴다면, 에이전트의 계획 단계는 대개 대시보드에 나타나지 않습니다. 파일로 나타납니다. <code>plan.md</code>, 체크박스가 달린 작업 목록, 에이전트가 계속 고쳐 쓰는 진행 파일, 마지막의 요약. 여러분 쪽에서 투명성이란 읽을 것이 늘어난다는 뜻입니다.</p>
<p>단계를 보여 주는 것은 에이전트의 몫입니다. 나머지 절반은 중요한 순간에 그것을 읽는 사람입니다. 마이그레이션이 실행되기 전, 브랜치가 병합되기 전, ‘완료’를 받아들이기 전. 아무도 열어 보지 않는 600줄짜리 파일에 모든 것을 펼쳐 놓는 에이전트는 서류상으로는 투명하지만 실제로는 감독받지 않는 셈입니다.</p>
<p>Harrison Chase도 2024년에 비슷한 이야기를 했습니다. 문서가 아니라 에이전트 프레임워크가 어떻게 동작해야 하는지에 관한 글이었습니다. “정확히 어떤 단계를 밟을지 미리 알 수 없을 수 있으므로, 내부에서 무슨 일이 일어나는지 관찰할 수 있기를 원하게 될 것이다.” 그는 에이전트를 만드는 사람을 위한 도구를 말하고 있었습니다. 에이전트를 부리는 사람이 여러분이라면, 에이전트가 계속 써 나가는 평범한 파일이 여러분이 지켜볼 수 있는 부분인 경우가 많습니다.</p>
<p>이 저자들 중 누구도 MarsDawn을 언급하지 않으며, MarsDawn이나 다른 Markdown 도구를 추천하지도 않습니다.</p>

<h2>그 읽기가 보기보다 어려운 이유</h2>
<p>파일은 길고, 중요한 내용은 위쪽에 있는 경우가 드뭅니다. 변경 사항을 설명하는 다이어그램은 그림이 아니라 Mermaid 소스입니다(그려진 모습을 보는 방법은 <a href="/ko/view-markdown-on-mac/">Mac에서 Markdown 파일을 보는 방법</a>에 있습니다). 여러분이 절반쯤 읽는 동안 에이전트가 파일을 고쳐 쓸 수도 있습니다. 파일이 하나가 아닌 경우가 많고, 때로는 서로 다른 브랜치나 워크트리에 있습니다. 그리고 문제를 발견해도 “캐시 부분이 좀 이상해”라고 하면 에이전트는 짐작할 수밖에 없습니다. 더 자세한 내용은 <a href="/ko/reading-agent-output/">에이전트가 돌려준 결과 읽기</a>에 있습니다.</p>

<h2>MarsDawn이 맞는 곳과 맞지 않는 곳</h2>
<p>MarsDawn은 이 읽기를 위한 Mac 앱입니다. 에이전트를 더 투명하게 만들지는 않으며, 안에 AI 모델도 없습니다. 계획을 요약하거나 맞는지 알려 주지 않습니다. 하는 일은 다음과 같습니다.</p>
<ul>
  <li><strong>긴 파일:</strong> 보기 &#9656; 사이드바 보기(&#8963;&#8984;S)를 선택하면 제목이 나열된 개요 탭이 열립니다. 하나를 클릭하면 그곳으로 이동합니다.</li>
  <li><strong>다이어그램과 수식:</strong> 소스와 렌더링된 페이지가 나란히 놓이고(&#8984;2) 함께 스크롤되며, Mermaid와 KaTeX가 그려집니다. 다이어그램에 오류가 있으면 미리보기에 소스와 그 아래 오류가 표시됩니다.</li>
  <li><strong>읽는 동안 고쳐 쓰일 때:</strong> 에이전트가 파일을 고쳐 쓰면 MarsDawn이 다시 불러오고 읽던 위치를 유지합니다. 여러분이 저장하지 않은 편집이 없는 한 그렇습니다.</li>
  <li><strong>여러 파일:</strong> 파일 &#9656; 폴더 열기&#8230;(&#8679;&#8984;O)로 에이전트의 폴더를 여세요. 새 파일은 약 1초 안에 파일 탭에 나타나고, git 체크아웃이라면 헤더에 브랜치나 워크트리 이름이 표시됩니다.</li>
  <li><strong>줄 가리키기:</strong> 편집 &#9656; 참조 복사(&#8997;&#8984;C)는 현재 위치를 <code>docs/plan.md:42</code> 형식으로 복사하고, AI용으로 복사(&#8963;&#8997;&#8984;C)는 그 아래에 선택한 텍스트를 덧붙여 에이전트와의 채팅에 바로 붙여 넣을 수 있게 합니다.</li>
</ul>
<p>읽는 것은 여전히 여러분입니다. MarsDawn은 그동안 길고 계속 바뀌는 파일을 읽기 좋게 유지합니다.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 <a href="{k.LISTING_URL}">Mac App Store</a>에 있습니다. 무료 <code>marsdawn</code> 명령줄 도구도 있습니다.</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>앱 없이 Markdown을 PDF로 내보냅니다.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; 구입 전에 알아 두세요: <a href="/ko/limits/">MarsDawn이 하지 않는 일</a></p>

<h2>다음</h2>
<ul>
  <li>에이전트의 결과물이 읽기 어려운 이유와 체크리스트: <a href="/ko/reading-agent-output/">에이전트가 돌려준 결과 읽기</a>.</li>
  <li>체크리스트를 예시와 함께 단계별로: <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 만에 검토하기</a>.</li>
  <li>여러 종류의 에이전트가 건네는 문서: <a href="/ko/agent-design-patterns/">네 가지 에이전트 설계 패턴과 각각이 건네는 문서</a>.</li>
  <li>AI의 결과물을 왜 읽어야 하는지 짧게: <a href="/ko/reviewing-ai-output/">AI의 결과물에 여전히 사람 독자가 필요한 이유</a>.</li>
</ul>

<h2>출처</h2>
<ul>
  <li>Erik S., Barry Zhang, “Building Effective Agents”, Anthropic, 2024년 12월 19일: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (2026-09-26 기준 온라인 버전에서 인용. 현재 이 글에는 설명된 도구 중 상당수가 2024년 12월 이후 바뀌었다는 안내가 붙어 있습니다.)</li>
  <li>Harrison Chase, “What is an agent?”, LangChain, 2024년 6월 28일, 보관된 사본: <a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a> (원래 주소에는 현재 2026년의 다른 글이 있습니다.)</li>
</ul>
""",
    }

    pages['reviewing-agent-plans'] = {
        "title": '에이전트의 계획을 5분 안에 검토하는 법 · MarsDawn',
        "description": 'AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.',
        "body": f"""
<section class="intro">
  <h1>에이전트의 계획을 5분 안에 검토하는 법</h1>
  <p>에이전트가 계획을 작성하고 승인을 기다리고 있습니다. 주어진 시간은 한 시간이 아니라 5분입니다. 일반 텍스트 에디터를 포함해 어떤 에디터에서든 통하는 활용법을 소개합니다. MarsDawn은 몇몇 단계에서 도움이 되며, 어느 단계인지 함께 알려 드립니다. 가장 중요한 단계에서는 도움이 되지 않습니다.</p>
</section>

<div class="summary"><p><strong>계획을 위에서부터 차례로 읽지 마세요. 구조를 확인하고, 주장 하나를 직접 검증하고, 되돌릴 수 없는 작업을 찾고, 다이어그램과 범위를 살핀 다음, 에이전트가 바로 반영할 수 있는 피드백을 쓰세요. 6단계, 약 5분입니다.</strong></p></div>

<h2>실행 전에 신경 써야 하는 이유</h2>
<p>Chip Huyen은 계획과 실행을 분리해야 하는 이유를 설명하며 비용을 단도직입적으로 말합니다. “감독이 없으면 에이전트는 그 단계들을 몇 시간이고 실행하며 API 호출에 시간과 돈을 낭비할 수 있고, 그동안 여러분은 그것이 아무 데도 이르지 못한다는 사실을 깨닫지 못할 수 있습니다.” 저희가 덧붙이자면, 계획은 실수를 잡아내기에 가장 저렴한 곳입니다. <code>plan.md</code>의 한 줄을 고치는 데는 문장 하나면 됩니다. 에이전트가 실행한 뒤에 고치려면 오후 한나절이 걸립니다.</p>

<h2>예시</h2>
<p>사용자 아바타를 기존 링크가 깨지지 않게 오브젝트 스토리지로 옮겨 달라고 에이전트에게 요청했다고 해 봅시다. 에이전트가 이런 계획을 돌려줍니다.</p>
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
<p>깔끔하게 읽힙니다. 그런데 이대로라면 아바타를 하나도 복사하기 전에 전부 삭제하게 됩니다.</p>

<h2>6단계</h2>
<p><strong>1. 제목만 읽으세요.</strong> <em>(약 1분)</em> 계획이 요청한 내용과 맞나요? 섹션이 빠져 있다면 대개 작업도 빠져 있습니다. 여기에는 Goal, Steps, Status가 있습니다. 기존 링크가 계속 작동해야 한다고 요청했는데, 기존 링크나 변경을 되돌리는 방법을 다루는 제목이 없습니다. 이것이 첫 번째 코멘트입니다.</p>
<p>터미널에서는 <code>grep -n '^#' plan.md</code>로 제목만 볼 수 있고, 대부분의 에디터도 개요를 보여 줍니다. MarsDawn에서는 사이드바의 개요 탭(보기 &#9656; 사이드바 보기, &#8963;&#8984;S)에 제목이 나열되고, 클릭하면 해당 위치로 이동합니다.</p>
<p><strong>2. 무언가가 완료됐다, 통과했다, 확인됐다고 주장하는 곳을 모두 찾고, 그중 하나를 직접 확인하세요.</strong> <em>(약 1분)</em> 파일을 열고, 테스트를 실행하고, 행 수를 세어 보세요. Chip Huyen은 “에이전트가 작업을 완료하지 않았는데도 완료했다고 확신하는” 실패를 설명합니다. 그의 예시에서는 50명을 호텔 객실 30개에 배정하라는 요청을 받은 에이전트가 40명만 배정하고 완료했다고 말합니다.</p>
<pre><code>grep -n -i -E 'done|pass|verified|&#9989;' plan.md</code></pre>
<p>여기서는 “&#9989; done”과 “All tests pass.”가 걸립니다. 어떤 테스트일까요? 그중 아바타와 관련된 테스트가 있나요? 직접 실행하거나 물어보세요. 이 단계는 MarsDawn이 대신할 수 없습니다. 여러분 말고는 아무도 할 수 없습니다.</p>
<p><strong>3. 되돌릴 수 없는 단계를 찾으세요.</strong> <em>(약 1분)</em> 데이터 삭제, 마이그레이션, force-push, 무언가를 보내거나 결제하거나 게시하는 모든 작업입니다. 이런 단계는 여러분의 명시적인 승인을 기다려야 합니다. Chip Huyen은 같은 생각을 시스템 쪽에서 설명합니다. “계획에 데이터베이스 업데이트나 코드 변경 병합처럼 위험한 작업이 포함되어 있다면, 시스템은 실행 전에 사람의 명시적 승인을 요청하거나 사람이 직접 실행하도록 할 수 있습니다.” 여기서는 4단계가 원본을 삭제하는데, 복사하는 5단계보다 앞에 있습니다.</p>
<p><strong>4. 렌더링된 다이어그램을 읽고, 화살표 하나하나를 본문과 대조하세요.</strong> 순서도에는 “복사 &#8594; 확인 &#8594; 삭제”라고 되어 있는데 단계 설명은 다르다면, 그것이 발견입니다. 이 계획에는 다이어그램이 없으니 오늘은 넘어갑니다. 다이어그램이 있다면 Mermaid 소스가 아니라 이미지를 보세요. 미리 보기를 지원하는 에디터가 많으며, <a href="/ko/view-markdown-on-mac/">Mac에서 Markdown 파일 보는 법</a>과 <a href="/ko/vs/markdown-preview-tools/">다른 곳에서 Markdown 보기</a>에서 선택지를 살펴볼 수 있습니다. MarsDawn에서는 렌더링된 다이어그램이 소스 옆에 표시되고(&#8984;2), 깨진 다이어그램은 소스와 그 아래 오류를 보여 주는데, 그 자체로 코멘트할 거리입니다.</p>
<p><strong>5. 계획이 건드리는 파일과 시스템을 나열하고, 요청하지 않은 것은 무엇이든 질문하세요.</strong> <em>(4단계와 5단계를 합쳐 약 1분)</em> 여기서는 스토리지 설정, 템플릿, 서버의 폴더 하나, 버킷 하나입니다. 버킷은 누가 읽을 수 있나요? 공개로 해 달라고 한 적은 없습니다. 에이전트의 작업 폴더를 MarsDawn에서 열어 두었다면(파일 &#9656; 폴더 열기&#8230;, &#8679;&#8984;O) 에이전트가 쓰는 새 파일이 1초 정도 안에 파일 탭에 나타나고, 헤더에 git 브랜치나 worktree가 표시되어 어느 체크아웃을 검토하고 있는지 알 수 있습니다.</p>
<p><strong>6. 피드백은 위치, 문제, 수정 방법의 형식으로, 한 줄에 문제 하나씩 쓰세요.</strong> <em>(마지막 1분)</em></p>
<pre><code>plan.md:10: deletes the avatars before step 5 copies them. Copy first, check the count, then delete, and wait for my OK before deleting.
plan.md:14: which tests? Add one that loads an old avatar URL after the switch.
plan.md:6: nothing about keeping old links working. Add a step for that, and a way to undo the switch.</code></pre>
<p>줄 번호가 있는 에디터라면 무엇이든 괜찮습니다. MarsDawn에서는 편집 &#9656; 참조 복사(&#8997;&#8984;C)로 현재 위치를 <code>plan.md:10</code> 형식으로 복사하고, AI용으로 복사(&#8963;&#8997;&#8984;C)로 선택한 텍스트를 그 아래에 덧붙일 수 있습니다.</p>

<h2>1분밖에 없다면</h2>
<p>2단계를 하세요. 끝났다고 믿는 에이전트를 잡아내는 곳이 바로 여기입니다.</p>

<h2>5분으로 부족할 때</h2>
<p>어떤 단계가 맞는지 알 수 없을 때가 있습니다. 여러분이 아는 범위를 벗어나기 때문입니다. Jess Ou는 2026년 LangChain의 에이전트 해설 글에서 이를 두 문장으로 말합니다. “평가할 수 없는 판단은 위임하지 마세요. 좋은 답을 알아보지 못한다면 에이전트도 마찬가지입니다.” 저희의 결론은 이렇습니다. 어떤 단계를 판단할 수 없다는 것은 더 빨리 승인할 이유가 아니라, 판단할 수 있는 사람에게 물어볼 이유입니다.</p>

<h2>여기서 MarsDawn이 하는 일과 하지 않는 일</h2>
<p>MarsDawn에는 AI 모델이 들어 있지 않습니다. 이 계획의 문제를 찾아내지 않으며, 2단계도 3단계도 하지 않습니다. 작업하는 동안 파일을 읽기 쉽게 유지해 줄 뿐입니다. 1단계에는 개요를, 4단계에는 렌더링된 다이어그램을, 5단계에는 파일 탭을, 6단계에는 줄 참조를 제공합니다. 그리고 읽는 도중에 에이전트가 계획을 수정하면, 저장하지 않은 변경 사항이 없는 한 MarsDawn이 파일을 다시 불러오면서 읽던 위치를 유지합니다.</p>
<p>계획이 확정된 뒤 다른 사람도 봐야 한다면, <a href="/ko/sharing-exported-pdfs/">내보낸 PDF 공유하기</a>와 <a href="/ko/markdown-to-pdf/">Markdown을 PDF로</a>에서 PDF로 보내는 방법을 확인하세요.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 <a href="{k.LISTING_URL}">Mac App Store</a>에 있습니다. 무료 명령줄 도구 <code>marsdawn</code>도 있습니다.</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>앱 없이 Markdown을 PDF로 내보냅니다.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; 구매 전에 알아 두세요: <a href="/ko/limits/">MarsDawn이 하지 않는 것</a></p>

<h2>더 읽어 보기</h2>
<ul>
  <li>에이전트가 넘긴 결과물이 읽기 어려운 이유: <a href="/ko/reading-agent-output/">에이전트가 넘긴 결과물 읽기</a></li>
  <li>에이전트가 계획을 드러내는 이유: <a href="/ko/agent-transparency/">Anthropic은 투명한 에이전트를 원합니다. 그런데 드러낸 것은 누가 읽을까요?</a></li>
  <li>에이전트가 넘기는 것은 계획만이 아닙니다: <a href="/ko/agent-design-patterns/">에이전트 디자인 패턴 네 가지와 각각이 넘기는 문서</a></li>
</ul>

<h2>출처</h2>
<ul>
  <li>Chip Huyen, “Agents”, 2025년 1월 7일: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Jess Ou, “What is an AI agent?”, LangChain, 2026년 7월 31일: <a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a></li>
</ul>
""",
    }

    pages['agent-design-patterns'] = {
        "title": '에이전트 디자인 패턴 네 가지와 각각이 넘기는 문서 · MarsDawn',
        "description": 'Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.',
        "body": f"""
<section class="intro">
  <h1>에이전트 디자인 패턴 네 가지와 각각이 넘기는 문서</h1>
  <p>2024년 3월, Andrew Ng은 자신의 뉴스레터 The Batch에서 AI 에이전트의 디자인 패턴 네 가지를 소개했습니다. 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업입니다. 이 패턴들은 보통 에이전트를 만드는 쪽의 시각에서, 모델에서 더 나은 결과를 끌어내는 방법으로 설명됩니다. 이 글은 반대편에서 봅니다. 이런 패턴으로 만들어진 에이전트를 쓴다면, 폴더에는 무엇이 들어오고, 무엇부터 읽어야 할까요?</p>
</section>

<div class="summary"><p><strong>네 가지 패턴은 Andrew Ng의 것입니다. 각 패턴이 보통 넘기는 문서와 그 안에서 확인할 점은 저희의 추론입니다. 그는 둘 중 어느 것에 대해서도 쓰지 않았고, 이 시리즈에서 사람의 검토를 주장하지도 않습니다.</strong></p></div>

<h2>네 가지 패턴 간단히 보기</h2>
<p>Ng은 “Agentic Design Patterns Part 1”에서 이 패턴들을 설명합니다. 요약하면 이렇습니다. <strong>리플렉션</strong>에서는 모델이 자기 작업을 검토하고 개선합니다. <strong>도구 사용</strong>에서는 웹 검색이나 코드 실행 같은 도구를 호출할 수 있습니다. <strong>계획</strong>에서는 여러 단계의 계획을 세워 실행합니다. <strong>멀티 에이전트 협업</strong>에서는 여러 에이전트가 일을 나누고 논의합니다.</p>
<p>Part 1에서 그는 코딩 벤치마크 HumanEval에서의 향상을, 그의 팀이 여러 연구 그룹에서 모은 결과로 보여 줍니다. “GPT-3.5(zero-shot)는 48.1%를 맞혔습니다. GPT-4(zero-shot)는 67.0%로 더 낫습니다. 그러나 GPT-3.5에서 GPT-4로의 향상은 반복적인 에이전트 워크플로를 도입했을 때의 향상에 비하면 미미합니다. 실제로 에이전트 루프로 감싸면 GPT-3.5는 최대 95.1%를 달성합니다.” 이 수치는 코딩 벤치마크 하나에 대한 것이고, 95.1%는 최선의 경우(“최대”)입니다. 에이전트 워크플로가 결과물을 개선할 수 있다는 것을 보여 줄 뿐, 그것을 누가 확인하는지에 대해서는 아무것도 말하지 않습니다.</p>
<p><strong>여기서부터 문서와 확인 사항은 Ng이 아니라 저희의 해석입니다.</strong> 또한 실제 에이전트는 여러 패턴을 섞어 씁니다. 코딩 에이전트는 한 세션 안에서 계획을 세우고, 도구를 실행하고, 자기 작업을 검토하기도 하므로 네 종류의 파일을 모두 받게 되는 경우가 많습니다.</p>

<h2>1. 리플렉션: 이미 스스로 검토를 거친 초안</h2>
<p>리플렉션에 관한 Ng의 글은 이 패턴을, 원래라면 사람이 했을 피드백을 자동화하는 것으로 설명합니다. “비판적 피드백을 주는 단계를 자동화해서, 모델이 자기 출력을 자동으로 비판하고 응답을 개선하게 하면 어떨까요?”</p>
<p><strong>보통 넘기는 것:</strong> 수정된 문서. 때로는 자기 평가 섹션이나 “엣지 케이스를 다시 확인함” 같은 문장이 붙어 있습니다.</p>
<p><strong>확인할 점:</strong> 에이전트의 자기 비판이 아니라 <em>여러분의</em> 요청과 결과를 비교하세요. 자기 평가도 나름의 방식으로 틀릴 수 있습니다. Chip Huyen은 이렇게 말합니다. “흥미로운 계획 실패 유형 하나는 리플렉션의 오류에서 비롯됩니다. 에이전트가 작업을 완료하지 않았는데도 완료했다고 확신하는 것입니다.” 당시 OpenAI에 있던 Lilian Weng은 2023년 6월 블로그 Lil’Log에서 그 시기의 모델에 대해 이렇게 썼습니다. “전문 지식이 부족하면 LLM은 자기 결함을 알지 못하고, 따라서 작업 결과가 옳은지 제대로 판단하지 못할 수 있습니다.” (그가 소개한 연구에서는 LLM의 결과 평가와 인간 전문가의 평가가 일치하지 않았습니다.) “확인됨”이라고 쓰여 있다면, 하나는 직접 확인하세요.</p>

<h2>2. 도구 사용: 무엇을 실행했는지에 대한 보고</h2>
<p><strong>보통 넘기는 것:</strong> 에이전트가 무엇을 실행하거나 검색했고 무엇이 나왔는지에 대한 요약. “테스트 스위트를 실행함: 모두 통과.” 결과 표. 찾아낸 링크들.</p>
<p>Anthropic의 가이드는 도구 결과를 에이전트가 스스로를 확인하는 수단으로 설명합니다. “실행 중에는 에이전트가 진행 상황을 평가하기 위해 각 단계에서 환경으로부터 ‘실측 정보’(도구 호출 결과나 코드 실행 등)를 얻는 것이 중요합니다.” 그 확인은 에이전트 내부에서 일어납니다. 여러분에게 도착하는 것은 그에 대한 에이전트의 설명입니다.</p>
<p><strong>확인할 점:</strong> 모든 주장이 여러분이 볼 수 있는 출력으로 거슬러 올라가는지. 요약에 있는 숫자 하나를 실제 출력과 비교하세요. 링크 하나를 열어 보세요.</p>

<h2>3. 계획: <code>plan.md</code></h2>
<p><strong>보통 넘기는 것:</strong> 계획, 명세, 에이전트가 하나씩 체크해 나가는 작업 목록.</p>
<p>Ng은 Part 4에서 이 패턴에 대해 솔직하게 말합니다.</p>
<blockquote><p>“한편으로 계획은 매우 강력한 능력이지만, 다른 한편으로는 결과를 예측하기 어렵게 만듭니다. 제 경험상 리플렉션과 도구 사용이라는 에이전트 디자인 패턴은 안정적으로 작동시켜 애플리케이션의 성능을 높일 수 있지만, 계획은 아직 덜 성숙한 기술이라 그것이 무엇을 할지 미리 예측하기가 어렵습니다.”</p></blockquote>
<p>그는 낙관적이기도 합니다. “하지만 이 분야는 계속 빠르게 발전하고 있으며, 계획 능력도 빠르게 향상될 것이라고 확신합니다.”</p>
<p><strong>확인할 점:</strong> 실행되기 전의 계획. <a href="/ko/reviewing-agent-plans/">5분 검토법</a>으로 구조, 주장 하나, 되돌릴 수 없는 단계, 다이어그램, 범위를 확인하세요. 에이전트가 도중에 계획을 다시 쓰면 승인한 버전과 비교하세요. git으로 관리 중이라면 <code>git diff plan.md</code>로 무엇이 바뀌었는지 볼 수 있습니다. MarsDawn에서는 개요 탭으로 긴 계획의 구조를 볼 수 있고, 다시 쓰인 계획은 저장하지 않은 변경 사항이 없는 한 읽던 위치를 잃지 않고 다시 불러옵니다.</p>

<h2>4. 멀티 에이전트 협업: 여러 파일, 여러 작성자</h2>
<p><strong>보통 넘기는 것:</strong> 한 에이전트의 명세, 다른 에이전트의 구현 노트, 세 번째 에이전트의 검토, 그리고 그 사이를 오가는 요약. 각자 자기 브랜치나 worktree에서 작업하기도 합니다.</p>
<p><strong>확인할 점:</strong> 인계 지점. 한 에이전트가 다른 에이전트의 작업을 요약한 곳에서 빠진 요구 사항이 없는지 찾아보세요. 서로 모순되는 두 파일을 찾고, 누군가 다른 쪽을 바탕으로 작업하기 전에 어느 쪽이 기준인지 정하세요. MarsDawn에서 파일 &#9656; 폴더 열기&#8230;(&#8679;&#8984;O)로 공유 폴더를 열면, 에이전트가 새 파일을 쓰는 대로 1초 정도 안에 파일 탭에 나타나고, git 체크아웃에서는 헤더에 브랜치나 worktree가 표시되므로 서로 다른 브랜치에서 같은 이름의 파일을 연 두 창이 똑같아 보이지 않습니다. Markdown을 읽지 않는 사람들에게 결과를 전달해야 한다면 <a href="/ko/sharing-exported-pdfs/">내보낸 PDF 공유하기</a>에서 그 단계를 다룹니다.</p>

<h2>한눈에 보기</h2>
<table>
<thead><tr><th>패턴(Ng)</th><th>보통 넘기는 것(저희의 추론)</th><th>먼저 읽을 것(저희의 제안)</th></tr></thead>
<tbody>
<tr><td>리플렉션</td><td>수정된 초안, 경우에 따라 자기 평가 포함</td><td>요청 대비 결과, “확인됨” 하나 직접 검증</td></tr>
<tr><td>도구 사용</td><td>무엇을 실행했고 무엇이 나왔는지에 대한 보고</td><td>주장 하나를 실제 출력까지 추적</td></tr>
<tr><td>계획</td><td><code>plan.md</code>, 명세, 작업 목록</td><td>실행 전 5분 검토</td></tr>
<tr><td>멀티 에이전트 협업</td><td>여러 에이전트의 여러 파일, 경우에 따라 여러 브랜치</td><td>인계 지점과 기준이 되는 파일</td></tr>
</tbody>
</table>
<p>여기 인용된 저자 중 누구도 MarsDawn을 언급하거나 추천하지 않으며, 다른 어떤 Markdown 도구도 추천하지 않습니다. MarsDawn에는 AI 모델이 들어 있지 않습니다. 어떤 모델이 파일을 만들었는지 알지 못하고, 이런 확인을 대신 해 주지도 않습니다. 여러분이 확인하는 동안 파일을 읽기 쉽게 유지해 줄 뿐입니다.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 <a href="{k.LISTING_URL}">Mac App Store</a>에 있습니다. 무료 명령줄 도구 <code>marsdawn</code>도 있습니다.</p>
<pre><code>brew install redtear1115/tap/marsdawn</code></pre>
<p>앱 없이 Markdown을 PDF로 내보냅니다. <a href="/ko/markdown-to-pdf/">Markdown을 PDF로</a>를 참고하세요.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; 구매 전에 알아 두세요: <a href="/ko/limits/">MarsDawn이 하지 않는 것</a></p>

<h2>더 읽어 보기</h2>
<ul>
  <li>에이전트가 넘긴 결과물이 읽기 어려운 이유와 체크리스트: <a href="/ko/reading-agent-output/">에이전트가 넘긴 결과물 읽기</a></li>
  <li>계획 확인의 전체 과정: <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 안에 검토하는 법</a></li>
  <li>투명성이 여러분에게 요구하는 것과 요구하지 않는 것: <a href="/ko/agent-transparency/">Anthropic은 투명한 에이전트를 원합니다. 그런데 드러낸 것은 누가 읽을까요?</a></li>
</ul>

<h2>출처</h2>
<ul>
  <li>Andrew Ng, “Agentic Design Patterns Part 1”, The Batch, 2024년 3월 20일: <a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng, “Agentic Design Patterns Part 2, Reflection”, The Batch, 2024년 3월 27일: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/</a></li>
  <li>Andrew Ng, “Agentic Design Patterns Part 4, Planning”, The Batch, 2024년 4월 10일: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a></li>
  <li>Chip Huyen, “Agents”, 2025년 1월 7일: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a></li>
  <li>Lilian Weng, “LLM Powered Autonomous Agents”, Lil’Log, 2023년 6월 23일: <a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a></li>
  <li>Erik S., Barry Zhang, “Building Effective Agents”, Anthropic, 2024년 12월 19일: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (2026년 9월 26일 기준 온라인 버전에서 인용)</li>
</ul>
""",
    }

    # /templates/ pages (scripts/templates_pages.py), one entry per table there, for #162 to merge.
    # The downloads are TEMPLATES byte for byte; Mermaid node labels are translated, as in ja.
    templates = {
        'ui_labels': {"templates": "템플릿", "templates-spec": "명세서 템플릿",
                      "templates-flowchart": "순서도 템플릿", "templates-meeting-notes": "회의록 템플릿"},
        'labels': {"template": "템플릿", "download": "{file} 다운로드", "looks": "보이는 모습",
                   "ask": "에이전트에게 맡기기", "share": "PDF로 공유하기", "doesnt": "하지 않는 일",
                   "faq": "자주 묻는 질문", "more": "다른 템플릿", "sep": ": ",
                   "img_alt": "{file}를 marsdawn export로 내보낸 PDF의 첫 페이지."},
        'hub': {"title": "Markdown 템플릿 · MarsDawn",
                "description": "에이전트가 쓰고 여러분이 읽는 문서를 위한 Markdown 템플릿입니다. 명세서, 순서도, 회의록이 있으며, 각각 에이전트에게 줄 프롬프트가 함께 제공됩니다.",
                "h1": "Markdown 템플릿",
                "lede": "에이전트가 쓰고 여러분이 읽는 문서를 위한 템플릿입니다. 템플릿마다 에이전트에게 줄 프롬프트가 함께 있습니다. 채워진 파일을 MarsDawn에서 열어 에이전트가 쓴 내용을 읽어 보세요.",
                "items": {"spec": ("명세서(PRD)", "문제, 목표, 요구 사항, 흐름도, 인수 기준."),
                          "flowchart": ("순서도", "Mermaid 다이어그램과 그 아래에 풀어 쓴 단계."),
                          "meeting-notes": ("회의록", "결정 사항과 실행 항목, 항목마다 담당자 한 명.")}},
        'pages': {
            "spec": {
                "title": "Markdown 명세서(PRD) 템플릿 · MarsDawn",
                "description": "요구 사항, Mermaid 흐름도, 인수 기준이 들어 있는 Markdown 명세서 템플릿입니다. 에이전트가 채우고, 여러분은 MarsDawn에서 검토하세요.",
                "h1": "Markdown 명세서(PRD) 템플릿",
                "lede": "에이전트가 채우고 여러분이 한 번에 읽을 수 있는 명세서입니다. 문제, 목표, 요구 사항, 흐름도, 인수 기준으로 이루어져 있습니다. 요구 사항을 바꿨다면 나머지를 맞춰 달라고 에이전트에게 요청하세요.",
                "caption": "<code>marsdawn export spec.md</code>로 내보냈습니다. 무료 명령줄 도구는 다이어그램을 포함해 MarsDawn의 미리 보기와 똑같이 렌더링합니다.",
                "prompt": "{url} 템플릿을 사용해 [기능]의 명세를 spec.md에 작성해 주세요. 모든 요구 사항에 ID를 붙이고, 흐름도와 인수 기준에서도 같은 ID를 사용해 주세요. 다 쓰면 marsdawn open spec.md를 실행해 주세요.",
                "share": "<code>marsdawn export spec.md</code>를 실행하면 옆에 spec.pdf가 생깁니다. Markdown을 읽지 않는 사람에게 건네세요.",
                "doesnt": "MarsDawn은 명세, 표, 다이어그램을 보여 줍니다. 인수 기준이 모든 요구 사항을 빠짐없이 다루는지는 확인하지 않습니다. 그것은 에이전트의 일이고, 여러분이 읽으며 확인할 일입니다.",
                "faq": [("흐름도를 그리려면 무언가를 설치해야 하나요?", "아니요. MarsDawn과 <code>marsdawn export</code>가 Mermaid를 직접 그리며, 오프라인에서도 됩니다."),
                        ("MarsDawn에서 명세를 편집할 수 있나요?", "네. 소스 옆에 미리 보기가 있는 Markdown 편집기입니다. 에이전트는 다음에 파일을 읽을 때 여러분의 수정 내용을 보게 됩니다.")],
            },
            "flowchart": {
                "title": "Markdown 순서도 템플릿(Mermaid) · MarsDawn",
                "description": "Markdown으로 쓰는 Mermaid 순서도 템플릿으로, 다이어그램 아래에 단계를 풀어 씁니다. Mac에서 미리 보고 PDF로 내보내세요.",
                "h1": "Markdown 순서도 템플릿",
                "lede": "Mermaid 순서도 아래에 단계를 하나하나 적어 두어, 다이어그램과 글을 서로 대조할 수 있습니다. 단계를 하나 빼고, 나머지를 고쳐 달라고 에이전트에게 요청하세요.",
                "caption": "<code>marsdawn export flowchart.md</code>로 내보냈습니다. 무료 명령줄 도구는 다이어그램을 포함해 MarsDawn의 미리 보기와 똑같이 렌더링합니다.",
                "prompt": "{url} 템플릿을 사용해 [프로세스]의 흐름을 flowchart.md에 그려 주세요. 노드마다 번호 붙은 단계를 하나씩, 같은 순서로 적어 주세요. 다 쓰면 marsdawn open flowchart.md를 실행해 주세요.",
                "share": "<code>marsdawn export flowchart.md</code>: 다이어그램이 PDF 안에 그려집니다.",
                "doesnt": "MarsDawn은 Mermaid에 적힌 대로 그립니다. 다이어그램을 손으로 배치할 수는 없고, 번호 붙은 단계와 노드를 맞춰 주지도 않습니다. Mermaid에 오류가 있으면 미리 보기에 다이어그램 대신 오류가 표시됩니다.",
                "faq": [("어떤 다이어그램을 쓸 수 있나요?", "Mermaid가 그리는 것이라면 무엇이든 됩니다. 순서도, 시퀀스 다이어그램, 상태 다이어그램 등입니다."),
                        ("왜 단계도 따로 적나요?", "훑어보는 사람은 다이어그램을 보고, 확인하는 사람은 글이 필요합니다. 에이전트가 둘을 맞춰 둘 수 있습니다.")],
            },
            "meeting-notes": {
                "title": "Markdown 회의록 템플릿 · MarsDawn",
                "description": "결정 사항과 담당자가 정해진 실행 항목을 정리하는 Markdown 회의록 템플릿입니다. 에이전트가 쓰고, 여러분은 MarsDawn에서 확인하세요.",
                "h1": "Markdown 회의록 템플릿",
                "lede": "결정 사항을 먼저, 그다음 실행 항목을 적고, 항목마다 담당자를 정합니다. 녹취록을 바탕으로 에이전트가 회의록을 쓰게 하고, 보내기 전에 읽어 보세요. 결정이 바뀌면 실행 항목을 맞춰 달라고 에이전트에게 요청하세요.",
                "caption": "<code>marsdawn export meeting-notes.md</code>로 내보냈습니다. 무료 명령줄 도구는 MarsDawn의 미리 보기와 똑같이 렌더링합니다.",
                "prompt": "{url} 템플릿을 사용해 이 회의를 meeting-notes.md에 정리해 주세요. 결정 사항을 먼저 한 줄씩 쓰고, 실행 항목마다 담당자 한 명과 날짜를 정해 주세요. 다 쓰면 marsdawn open meeting-notes.md를 실행해 주세요.",
                "share": "<code>marsdawn export meeting-notes.md</code>를 실행하면 PDF가 생깁니다. 회의 후 보내는 메일에 첨부하세요.",
                "doesnt": "MarsDawn은 회의를 녹음하거나 받아 적지 않고, 실행 항목을 추적하지도 않습니다. 읽는 사람이 보게 될 모습 그대로 회의록을 보여 줍니다.",
                "faq": [("체크박스가 작동하나요?", "미리 보기와 PDF에서 체크박스로 표시됩니다. 체크하려면 소스에서 <code>[ ]</code>를 <code>[x]</code>로 바꾸세요."),
                        ("에이전트가 회의록과 실행 항목을 맞춰 둘 수 있나요?", "네, 그것이 이 루프의 핵심입니다. 하나를 바꾸고 나머지를 업데이트해 달라고 요청하세요. MarsDawn이 결과를 보여 줍니다.")],
            },
        },
        'templates': {
            "spec": """# 명세: 기능 이름

상태: 초안 · 담당: 이름 · 업데이트: 날짜

## 문제

_지금 무엇이 문제인지, 누구에게 문제인지, 어떻게 알게 됐는지._

## 목표

- _출시되면 달라져 있을 것._

## 하지 않을 것

- _이번에 일부러 하지 않는 것._

## 요구 사항

| ID | 요구 사항 | 우선순위 |
|----|-----------|----------|
| R1 | _요구 사항_ | 필수 |
| R2 | _요구 사항_ | 권장 |

## 흐름

```mermaid
flowchart LR
  A[시작] --> B[단계] --> C[결과]
```

## 인수 기준

- [ ] R1: _확인 방법._
- [ ] R2: _확인 방법._

## 미결 질문

- _질문._
""",
            "flowchart": """# 흐름 이름

_한 문장으로: 무엇이 들어가고 무엇이 나오는지._

## 다이어그램

```mermaid
flowchart LR
  A[첫 번째 단계] --> B[두 번째 단계]
  B --> C[세 번째 단계]
  C --> D[완료]
```

## 단계

1. **첫 번째 단계:** _누가 맡고, 다음 단계에 무엇을 넘기는지._
2. **두 번째 단계:** _…_
3. **세 번째 단계:** _…_
4. **완료:** _여기서 ‘완료’가 무슨 뜻인지._
""",
            "meeting-notes": """# 회의 이름, 날짜

참석자: _이름_

## 결정 사항

- _결정된 내용, 한 줄에 하나씩._

## 실행 항목

- [ ] 이름: _무엇을, 언제까지._
- [ ] 이름: _무엇을, 언제까지._

## 메모

- _결정 사항도 실행 항목도 아니지만 남겨 둘 만한 내용._
""",
        },
        'scene_text': {
            "spec": {"title": "명세: 로그인 코드", "req": "요구 사항", "flow": "흐름", "acc": "인수 기준",
                     "r1": "R1: 6자리 코드를 메일로 보낸다.", "r2": "R2: 코드는 10분 후 만료.",
                     "r3": "R3: 2단계 인증을 요구한다.", "n1": "이메일", "n2": "코드", "n3": "2단계 인증",
                     "n4": "로그인 완료", "a1": "R1: 1분 안에 코드 도착.", "a3": "R3: 기기당 한 번만.",
                     "ask": "R3를 뺐어요. 흐름과 인수 기준을 맞춰 주세요.",
                     "reply": "완료했어요. 흐름에서 2단계 인증을 건너뛰고, R3 확인 항목도 지웠어요.",
                     "alt": "터미널에서 MarsDawn으로 spec.md를 엽니다. 읽는 사람이 요구 사항 R3를 지우면, 에이전트가 흐름도의 해당 단계와 인수 기준의 확인 항목을 함께 지웁니다."},
            "flowchart": {"title": "게시 흐름", "diagram": "다이어그램", "steps": "단계",
                          "n1": "초안", "n2": "검토", "n3": "법무", "n4": "게시",
                          "s1": "1. 초안: 작성자의 첫 버전.", "s2": "2. 검토: 편집자가 읽는다.",
                          "s3": "3. 법무: 표현을 확인한다.", "s4": "{c}. 게시: 공개된다.",
                          "ask": "다이어그램에서 법무를 뺐어요. 연결과 단계를 고쳐 주세요.",
                          "reply": "완료했어요. 검토에서 바로 게시로 이어지고, 단계 번호도 다시 매겼어요.",
                          "alt": "터미널에서 MarsDawn으로 flowchart.md를 엽니다. 읽는 사람이 Mermaid 다이어그램에서 법무 단계를 빼면, 에이전트가 다이어그램을 다시 연결하고 아래 단계의 번호를 다시 매깁니다."},
            "meeting-notes": {"title": "주간 회의, 10/5", "decisions": "결정 사항", "actions": "실행 항목",
                              "d1": "베타를 {u}명에게 공개.", "d2": "금요일에 출시.",
                              "t1": "Mia: 초대장 {a}통 발송.", "t2": "Leo: {b}석 추가.", "t3": "Ana: {c}명 지원 준비.",
                              "ask": "베타가 80명으로 늘었어요. 실행 항목을 업데이트해 주세요.",
                              "reply": "완료했어요. 실행 항목 세 개 모두 80으로 바꿨어요.",
                              "alt": "터미널에서 MarsDawn으로 meeting-notes.md를 엽니다. 읽는 사람이 결정 사항을 50명에서 80명으로 바꾸면, 에이전트가 실행 항목 세 개를 그에 맞게 고칩니다."},
        },
    }
    # The homepage loop (scripts/loop_anim.py COPY). Tab names follow the app's ko strings; the two
    # days have the same width (tabular digits), as the stacked swap needs.
    loop_copy = {
        "outline": "개요", "files": "파일",
        "title": "출시 노트",
        "sections": [("바뀌는 점", "로그인 화면이 이메일부터 묻습니다. {a}에 출시합니다."),
                     ("출시 일정", "{u} 정오."),
                     ("담당", "{b}에 엔지니어링이 플래그를 켭니다.")],
        "old": "10월 7일", "new": "10월 9일",
        "ask": "출시일을 옮겼어요. 다른 섹션도 맞춰 주세요.",
        "reply": "완료했어요. 두 섹션 모두 10월 9일로 바꿨어요.",
        "alt": "터미널에서 MarsDawn으로 launch-note.md를 엽니다. 읽는 사람이 출시일을 10월 7일에서 "
               "10월 9일로 바꾸면, 에이전트가 나머지 두 섹션을 맞추고, 루프가 처음부터 다시 시작됩니다.",
        "pause": "애니메이션 일시 정지", "pause_short": "일시 정지",
    }

    app_ui_languages = '영어, 중국어(번체), 중국어(간체), 일본어, 독일어, 프랑스어, 스페인어, 한국어'
    ui = {'home': 'MarsDawn', 'privacy': '개인정보 처리방침', 'support': '지원', 'cli': '명령줄', 'agents': '에이전트를 위한 marsdawn', 'using_cli': 'CLI 사용하기', 'markdown-to-pdf': 'Markdown을 PDF로', 'skill': '에이전트 스킬', 'view-markdown-on-mac': 'Mac에서 Markdown 보기', 'vs-macmd-viewer': 'MacMD Viewer와 MarsDawn 비교', 'updated': f'최종 업데이트: {k.UPDATED}', 'tagline': '에이전트가 쓴 글을 읽으세요.', 'slogan': 'Markdown의 새로운 새벽.', 'footer_store': f'MarsDawn은 <a href="{k.LISTING_URL}">Mac App Store</a>에서 구입할 수 있습니다.', 'footer_nav': '사이트', 'more': '더 보기', 'yours': '내 글은 내 Mac에', 'pay-once': '무료로 체험하고, 한 번만 구입', 'pdf': 'PDF 내보내기', 'native': 'Mac 앱', 'limits': 'MarsDawn이 하지 않는 일', 'mcp': 'MCP 서버', 'token-efficient-review': '토큰을 아끼는 검토', 'vs-markdown-preview-tools': '다른 도구로 Markdown 보기와 MarsDawn 비교', 'themes': '미리보기 테마와 PDF 내보내기', 'themes-new': '테마 만들기', 'themes-gallery': '테마 갤러리', 'sharing-exported-pdfs': '내보낸 PDF 공유하기', 'reviewing-ai-output': 'AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유', 'reading-agent-output': '에이전트가 돌려준 결과 읽기', 'agent-transparency': '에이전트의 투명성', 'reviewing-agent-plans': '에이전트의 계획 검토하기', 'agent-design-patterns': '에이전트 설계 패턴', 'changelog': '변경 내역', 'reading-notes': '편집자의 독서 노트', 'reading-notes-anthropic': '독서 노트: Anthropic', 'reading-notes-chip-huyen': '독서 노트: Chip Huyen', 'reading-notes-lilian-weng': '독서 노트: Lilian Weng', 'reading-notes-harrison-chase': '독서 노트: Harrison Chase', 'reading-notes-langchain': '독서 노트: LangChain(Jess Ou)', 'reading-notes-andrew-ng': '독서 노트: Andrew Ng', 'consent_text': '이 사이트는 방문자가 사이트를 어떻게 이용하는지 파악하기 위해 분석 쿠키를 사용합니다. 수락하지 않으면 이 쿠키는 꺼진 상태로 유지됩니다.', 'consent_accept': '수락', 'consent_decline': '거부', 'consent_aria': '쿠키 동의', 'cookie_settings': '쿠키 설정', 'view_markdown_source': 'Markdown 소스 보기'}
    store_chip = 'Mac App Store에서 판매 중'
    trait_link = {'yours': ('내 글은 내 Mac에', '계정도, 동기화도, 클라우드도 없습니다.'), 'pay-once': ('무료로 체험하고, 한 번만 구입', '14일 무료, 이후 USD 4.99 1회 구입. 구독이 아닙니다.'), 'pdf': ('PDF 내보내기', '다이어그램, 코드 하이라이트, 세심한 페이지 나눔.'), 'native': ('Mac 앱', '네이티브 윈도우와 탭, 자동 저장, 훑어보기.'), 'limits': ('MarsDawn이 하지 않는 일', '구입 전에 알아 둘 점.')}
    trait_nav_heading = 'MarsDawn에서 기대할 수 있는 것'
    figure_list_label = '이 스크린샷의 내용'


    pages['reading-notes'] = {
        "title": "편집자의 독서 노트 · MarsDawn",
        "description": "AI 에이전트를 만드는 사람들이 실제로 무엇을 주장하는지 살피는 짧은 노트 여섯 편 — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain, Andrew Ng — 그리고 각각이 그런 에이전트가 돌려준 것을 읽어야 하는 사람에게 무엇을 의미하는지.",
        "body": f"""
<section class="intro">
  <h1>편집자의 독서 노트</h1>
  <p>AI 에이전트가 어떻게 작동하는지에 대해 여섯 사람이 글을 썼습니다. 무엇으로 만들어지는지, 무엇이 시스템을 «agentic»하게 만드는지, 어떤 설계 패턴이 실제로 버티고 어떤 것은 아직 아닌지. 누구도 «에이전트가 돌려준 것을 어떻게 읽을지»는 쓰지 않았고, 누구도 MarsDawn을 언급하거나 Markdown 도구를 추천하지 않습니다. 우리는 각 글을 그 글의 조건으로 읽고, 우리 자신의 해석이 어디서 시작되는지 분명히 표시한 뒤, 모든 출처에 같은 질문을 던졌습니다. 이 글 때문에 폴더에 어떤 문서가 떨어지기 쉬운지, 그리고 그것을 읽을 때 MarsDawn은 어디에 도움이 되는가.</p>
</section>

<p>먼저 짧고 실용적인 쪽부터 보고 싶다면 <a href="/ko/reading-agent-output/">에이전트가 돌려준 결과 읽기</a>와 <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 만에 검토하기</a>부터 시작하세요. 이 여섯 노트는 그 페이지 뒤의 출처에 더 가까이 갑니다. 각각 단독으로 읽을 수 있으니 순서는 상관없습니다.</p>

<ul>
  <li><a href="/ko/reading-notes/anthropic-building-effective-agents/">Anthropic은 workflow와 agent를 나눕니다. 당신의 읽기는 어디에 가깝나요?</a> &#8212; 에이전트를 만드는 사람을 위한 Anthropic 가이드는 고정된 파이프라인과 다음 단계를 스스로 정하는 모델을 구분하고, «검토자»가 사람이 아니라 두 번째 LLM 호출인 workflow 하나를 그립니다.</li>
  <li><a href="/ko/reading-notes/chip-huyen-agents/">Chip Huyen의 read-only/write action 구분, 승인하기 전에 왜 중요한지</a> &#8212; 에이전트에 대한 그녀의 담백한 정의, 그리고 보기만 하는 행동과 무언가를 바꾸는 행동의 차이. 5분 검토에서 가장 시간을 들일 만한 지점입니다.</li>
  <li><a href="/ko/reading-notes/lilian-weng-llm-agents/">Lilian Weng이 2023년에 그린 에이전트 설계도, 각 부분이 남기는 파일</a> &#8212; 뇌, 계획, 기억, 도구 사용: 에이전트가 무엇으로 되어 있는지에 대한 그녀 자신의 틀, 그리고 문제가 생겼을 때 조정되지 않는 계획에서 그녀가 짚는 한계.</li>
  <li><a href="/ko/reading-notes/harrison-chase-what-is-an-agent/">Harrison Chase의 스펙트럼: agentic할수록 더 지켜보고 싶어진다</a> &#8212; 에이전트에 대한 그의 기술적 정의, 그리고 시스템이 그 스펙트럼을 따라 갈수록 관측 가능성이 필요하다는 그의 주장.</li>
  <li><a href="/ko/reading-notes/langchain-what-is-an-agent/">Jess Ou의 평가 파이프라인, 그중 한 단계는 여전히 당신의 일</a> &#8212; 2026년 7월 LangChain은 Harrison Chase의 2024년 글이 있던 주소에 Jess Ou가 쓴 새 «What is an AI agent?»를 올렸습니다. 정의는 거의 그의 것과 한 글자 같고, 자동 평가가 어디서 멈추고 어디서부터 사람이 나서야 하는지를 이어서 설명합니다.</li>
  <li><a href="/ko/reading-notes/andrew-ng-design-patterns/">Andrew Ng이 자신의 설계 패턴을 예측 가능성으로 순위를 매깁니다</a> &#8212; The Batch의 편지 다섯 편에서, 어떤 패턴을 더 믿을 만하고 어떤 것을 예측하기 어렵다고 보는지 분명히 말합니다.</li>
</ul>

<p>이 여섯 편 중 어느 것도 에이전트 출력을 더 주의 깊게 읽어야 한다고 주장하지 않으며, 어느 것도 MarsDawn에 관한 글이 아닙니다. 그 연결을 짓는 것은 우리이고, 각 노트가 그렇게 말합니다.</p>
""",
    }


    pages['reading-notes/anthropic-building-effective-agents'] = {
        "title": 'Anthropic은 workflow와 agent를 나눕니다. 당신의 읽기는 어디에 가깝나요? · MarsDawn',
        "description": '2024년 12월 Anthropic이 에이전트를 만드는 사람을 위해 낸 가이드는 workflow와 agent를 나누고, 그중 하나가 두 번째 LLM 호출로 첫 번째를 검토하는 다섯 가지 workflow 패턴을 설명합니다. 그게 폴더에 떨어지는 파일에 무엇을 뜻하는지.',
        "body": f"""
<section class="intro">
  <h1>Anthropic은 workflow와 agent를 나눕니다. 당신의 읽기는 어디에 가깝나요?</h1>
</section>

<div class="summary"><p><strong>2024년 12월 Anthropic이 AI 에이전트를 만드는 사람을 위해 낸 가이드는 맨 앞에서 «workflow»와 «agent»라는 두 가지를 나눈 뒤, 되는 것 중 가장 단순한 것부터 시작하라고 &#8212; 어쩌면 agentic 시스템을 아예 만들지 않는 것까지 포함해 &#8212; 권하고, 그것으로 부족할 때만 정리된 다섯 workflow 패턴 중 하나에 손을 뻗으라고 합니다. 그중 하나는 두 번째 LLM 호출을 검토자 자리에 앉힙니다. 이 노트는 그 패턴, 그리고 나머지 넷이 당신에게 무엇을 읽히게 남기는지에 관한 것입니다.</strong></p></div>

<h2>가이드가 주장하는 것</h2>
<p>Erik S.와 Barry Zhang이 «Building Effective Agents»를 쓴 대상은 LLM으로 어떻게 시스템을 만들지 정하려는 엔지니어입니다. 정의부터 시작합니다.</p>
<blockquote><p>&#8220;Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.&#8221;</p></blockquote>
<p>이어지는 조언은 절제에서 시작합니다.</p>
<blockquote><p>&#8220;When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all.&#8221;</p></blockquote>
<p>더 많은 구조가 필요할 때를 위해 다섯 workflow 패턴을 설명합니다. prompt chaining(작업을 일련의 호출로 나누고 단계 사이에 선택적으로 검사를 넣는 것), routing, parallelization, orchestrator-workers(하나의 LLM이 작업을 쪼개 worker LLM에 넘긴 뒤 결과를 합침), evaluator-optimizer. 마지막 것은 이렇게 말합니다.</p>
<blockquote><p>&#8220;In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.&#8221;</p></blockquote>
<p>Anthropic은 이 가이드 어디에서도 MarsDawn을 언급하지 않고, Markdown 도구도 추천하지 않습니다. <code>/agent-transparency/</code>가 이미 이 가이드의 투명성 원칙과 «checkpoints» 표현을 자세히 다루므로 &#8212; 이 노트는 그 땅을 다시 밟지 않습니다. 사람 코드 리뷰에 관한 가이드의 문장도, 코딩 에이전트에 한정된 부록이라는 맥락에서, 그 페이지에 있습니다.</p>

<h2>우리의 읽기이지 Anthropic의 것이 아님</h2>
<p>Anthropic은 workflow가 끝난 뒤 최종 출력을 누가 확인하는지는 말하지 않고, 이 중 어느 것도 문서를 묘사하지 않습니다 &#8212; 시스템을 만드는 사람을 위한 아키텍처 결정입니다. 하지만 다섯 패턴이 남기는 읽을 파일의 종류는 같지 않습니다. Prompt chaining과 routing은 대개 보이지 않는 배관이고, 당신에게 닿는 것이 있다면 체인의 마지막 출력으로, 다른 단일 응답과 같습니다. Orchestrator-workers는 다릅니다. 코딩 에이전트가 내부에서 이 패턴을 쓰면, 폴더에 떨어지는 것은 여러 worker 호출을 오케스트레이터가 이어 붙인 문서일 수 있고, 처음부터 끝까지 매끄럽게 읽히는 요약 안에서 한 worker 조각의 실수는 놓치기 쉽습니다.</p>
<p>Evaluator-optimizer는 특히 멈출 가치가 있습니다. 가이드가 사람 검토자가 앉았을 자리에 두 번째 LLM 호출을 두기 때문입니다. 어떤 종류의 실수를 값싸게 잡는 타당한 방법이지만, 결국 모델이 주어진 기준으로 다른 모델을 검사하는 것일 뿐입니다 &#8212; 이 시리즈의 다른 저자들도 모델이 자신이나 다른 모델의 결과를 판정하는 일에 같은 주의를 겁니다. 가이드는 사람이 evaluator의 판정을 다시 확인해야 한다고 어디에도 쓰지 않으며, 그 점에 대해 입장을 취하지도 않습니다. 이 일련의 과정이 돌려준 것을 마지막으로 읽는 사람이 당신이라면, «루프가 통과시켰다»와 «내가 확인했다»는 같은 문장이 아닙니다. 앞의 파일이 두 경우 모두 똑같이 보여도 말입니다.</p>

<h2>MarsDawn이 돕는 곳, 돕지 않는 곳</h2>
<p>MarsDawn은 어떤 workflow 패턴이 파일을 만들었는지 모르고, 안에 AI 모델도 없습니다 &#8212; 스스로 evaluator 단계를 돌리지도 않고, Anthropic이 그린 그 평가가 제 일을 했는지 알려 주지도 않습니다. 하는 일은 이렇습니다. 사이드바(보기 &#9656; 사이드바 보기, &#8963;&#8984;S)의 개요 탭이 오케스트레이터가 이어 붙인 긴 파일의 제목을 나열하고, 클릭하면 그곳으로 이동합니다. 소스와 렌더링된 페이지는 나란히(⌘2) 함께 스크롤되며, Mermaid 다이어그램과 KaTeX 수식도 소스로 두지 않고 그립니다. 읽는 도중에 에이전트가 파일을 고치면, 저장하지 않은 변경이 없는 한 MarsDawn이 다시 불러오면서 읽던 위치를 유지합니다. 편집 &#9656; 참조 복사 (&#8997;&#8984;C)는 지금 자리를 <code>docs/plan.md:42</code> 형식으로 복사해, 에이전트와의 채팅에 바로 붙여 넣을 수 있게 합니다.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 곧 Mac App Store에 올라갑니다. 무료 <code>marsdawn</code> 명령줄 도구는 오늘부터 쓸 수 있습니다:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>앱 없이 Markdown을 PDF로 내보냅니다.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; 구입 전에: <a href="/ko/limits/">MarsDawn이 하지 않는 일</a></p>

<h2>다음</h2>
<ul>
  <li>이 가이드의 투명성 원칙과 체크포인트 표현의 나머지: <a href="/ko/agent-transparency/">Anthropic은 에이전트가 투명해야 한다고 말합니다. 그럼 펼쳐 놓은 것은 누가 읽을까요?</a></li>
  <li>에이전트 출력이 일반적으로 왜 읽기 어려운지: <a href="/ko/reading-agent-output/">에이전트가 돌려준 결과 읽기</a></li>
  <li>시리즈로 돌아가기: <a href="/ko/reading-notes/">편집자의 독서 노트</a></li>
</ul>

<h2>출처</h2>
<ul>
  <li>Erik S. and Barry Zhang, &#8220;Building Effective Agents,&#8221; Anthropic, December 19, 2024: <a href="https://www.anthropic.com/engineering/building-effective-agents">https://www.anthropic.com/engineering/building-effective-agents</a> (2026-09-26에 가져와 인용).</li>
</ul>
""",
    }


    pages['reading-notes/chip-huyen-agents'] = {
        "title": 'Chip Huyen의 read-only/write action 구분, 승인하기 전에 왜 중요한지 · MarsDawn',
        "description": 'Chip Huyen의 2025년 1월 에세이 «Agents»는 에이전트 행동을 read-only와 write로 나눕니다. 그 구분이 계획에서 승인 전에 더 자세히 볼 줄을 빠르게 짚는 방법이 되는 이유.',
        "body": f"""
<section class="intro">
  <h1>Chip Huyen의 read-only/write action 구분, 승인하기 전에 왜 중요한지</h1>
</section>

<div class="summary"><p><strong>Chip Huyen의 2025년 1월 에세이 «Agents»는 교과서적 정의에서 시작해 더 구체적인 데로 갑니다. 에이전트의 행동은 세상을 보기만 하는 것과 바꾸는 것으로 나뉩니다. 그 구분은 주어진 5분 안에서, 계획의 어떤 줄이 승인 전에 더 자세히 볼 가치가 있는지 정하는 좋은 방법입니다.</strong></p></div>

<h2>글이 주장하는 것</h2>
<p>Huyen은 담백하게 엽니다.</p>
<blockquote><p>&#8220;An agent is anything that can perceive its environment and act upon that environment.&#8221;</p></blockquote>
<p>거기서 에이전트에 필요한 것을 쌓아 올립니다. 행동할 환경, 그리고 할 수 있는 일을 정하는 도구 집합 &#8212; «tool inventory». 환경을 지각만 하게 하는 행동(«read-only actions»)과 환경에 작용하게 하는 행동(«write actions»)을 구분합니다. 두 번째 종류의 위험에 대해서도 직설적입니다. «Write actions enable a system to do more»이지만 «the prospect of giving AI the ability to automatically alter our lives is frightening» &#8212; 그녀의 말로 «you shouldn’t allow an unreliable AI to initiate bank transfers.» 에이전트에서 가장 맞추기 어려운 부분에 대해서도 솔직합니다.</p>
<blockquote><p>&#8220;If you’ve ever been in any planning meeting, you know that planning is hard.&#8221;</p></blockquote>
<p>Huyen은 이 에세이 어디에서도 MarsDawn을 언급하지 않고 Markdown 도구도 추천하지 않습니다. <code>/reviewing-agent-plans/</code>는 이미 같은 에세이에서 그녀 문장 셋을 인용합니다. 계획이 돌기 전에 감독을 건너뛰는 비용, 끝나지 않았는데 끝났다고 믿는 에이전트, 그리고 체크리스트 3단계 안의 «위험한 작업 앞에서 시스템 can ask for explicit human approval before executing»라는 줄. 이 노트는 그 인용을 반복하지 않습니다. 그 페이지를 아직 안 읽었다면 아래에 링크가 있습니다.</p>

<h2>우리의 읽기이지 Huyen의 것이 아님</h2>
<p>Huyen의 read-only/write 구분은 검토 조언으로 쓰인 것이 아닙니다 &#8212; 도구가 무엇을 하는지 분류하는 방식입니다. 하지만 그 체크리스트 3단계가 이미 천천히 보라고 하는, 위험한 작업 줄을 짚는 담백하고 범용적인 검사입니다. 파일 읽기, 검색 실행, 디렉터리 나열은 read-only이고, read-only 단계가 잘못되면 다시 돌리는 비용입니다. 데이터 삭제, force-push, 브랜치 병합, 메일 발송, 카드 결제는 write action이고 &#8212; 그녀가 말하듯 &#8212; write 단계가 잘못되면 무서운 쪽이며, 에이전트 보고서를 읽을 즈음에는 이미 벌어졌을 수 있습니다. 방에 모인 사람에게도 계획이 어렵다는 지적은, 형식이 감당할 수 있는 것보다 더 정밀한 계획을 기대하지 말라는 점검이 됩니다. 자신 있게 읽히는 계획이 곧 맞는 계획은 아닙니다.</p>

<h2>MarsDawn이 돕는 곳, 돕지 않는 곳</h2>
<p>MarsDawn은 계획에서 read-only 단계와 write 단계를 구분하지 못합니다 &#8212; 텍스트가 라벨을 붙이지 않은 판단이고, 앱 안에는 의미를 읽는 기능이 없습니다. AI 모델도 없습니다. 위험한 줄을 대신 표시해 주지도, «계획은 어렵다» 검사를 돌리지도, 계획에 점수를 매기지도 않습니다. 하는 일은 당신이 그 판단을 하는 동안 파일을 읽기 쉽게 유지하는 것입니다. 개요 탭(보기 &#9656; 사이드바 보기, &#8963;&#8984;S)으로 줄마다 읽기 전에 계획의 형태를 훑을 수 있고, 소스와 렌더링된 페이지를 나란히(⌘2) 두어 단계 다이어그램이 날 Mermaid로 남지 않게 하며, 편집 &#9656; 참조 복사 (&#8997;&#8984;C)는 자리를 <code>plan.md:10</code>으로 만들어, 잘못된 순서의 write action을 보는 순간 피드백으로 붙여 넣을 수 있게 합니다.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 곧 Mac App Store에 올라갑니다. 무료 <code>marsdawn</code> 명령줄 도구는 오늘부터 쓸 수 있습니다:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>앱 없이 Markdown을 PDF로 내보냅니다.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; 구입 전에: <a href="/ko/limits/">MarsDawn이 하지 않는 일</a></p>

<h2>다음</h2>
<ul>
  <li>같은 에세이에서 나온 6단계·5분 체크리스트 전체: <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 만에 검토하기</a></li>
  <li>에이전트 출력이 일반적으로 왜 읽기 어려운지: <a href="/ko/reading-agent-output/">에이전트가 돌려준 결과 읽기</a></li>
  <li>시리즈로 돌아가기: <a href="/ko/reading-notes/">편집자의 독서 노트</a></li>
</ul>

<h2>출처</h2>
<ul>
  <li>Chip Huyen, &#8220;Agents,&#8221; January 7, 2025: <a href="https://huyenchip.com/2025/01/07/agents.html">https://huyenchip.com/2025/01/07/agents.html</a> (2026-09-26에 가져와 인용).</li>
</ul>
""",
    }


    pages['reading-notes/lilian-weng-llm-agents'] = {
        "title": 'Lilian Weng이 2023년에 그린 에이전트 설계도, 각 부분이 남기는 파일 · MarsDawn',
        "description": 'Lilian Weng의 널리 인용되는 2023년 서베이는 LLM 에이전트를 뇌와 계획·기억·도구 사용으로 그립니다. 각 부분이 당신에게 남기기 쉬운 파일, 그리고 예상치 못한 일에 조정되지 않는 계획에서 그녀가 짚는 한계.',
        "body": f"""
<section class="intro">
  <h1>Lilian Weng이 2023년에 그린 에이전트 설계도, 각 부분이 남기는 파일</h1>
</section>

<div class="summary"><p><strong>2023년 6월, 당시 OpenAI에 있던 Lilian Weng은 블로그 Lil’Log에 긴 서베이를 올렸습니다. LLM 기반 에이전트를 뇌(모델)와 세 구성요소 &#8212; 계획, 기억, 도구 사용 &#8212; 로 그립니다. 에이전트가 무엇으로 되어 있는지에 대한 초기이자 널리 인용되는 틀이며, 그 틀이 아직 어디서 깨지는지도 솔직합니다.</strong></p></div>

<h2>글이 주장하는 것</h2>
<p>Weng의 개요는 글 전체의 틀을 잡습니다.</p>
<blockquote><p>&#8220;In a LLM-powered autonomous agent system, LLM functions as the agent&#8217;s brain, complemented by several key components: Planning ... Memory ... Tool use&#8221;.</p></blockquote>
<p>계획에는 작업을 하위 목표로 나누는 일과, 지난 행동을 돌아보며 다음을 낫게 하는 일이 모두 들어갑니다. 기억은 단기(모델이 지금 보는 맥락, in-context)와 장기(대개 모델 밖, 검색 가능한 벡터 저장소)로 나뉩니다. 도구 사용은 고정된 가중치만으로는 못 주는 것 &#8212; 최신 정보, 코드 실행, 다른 API &#8212; 을 모델이 밖으로 부르게 합니다. 끝부분 «Challenges»에서 한계를 분명히 짚습니다.</p>
<blockquote><p>&#8220;LLMs struggle to adjust plans when faced with unexpected errors, making them less robust compared to humans who learn from trial and error.&#8221;</p></blockquote>
<p>화학 에이전트 ChemCrow 사례에서는 더 좁은 문제도 짚습니다. LLM 기반 평가는 GPT-4와 거의 같다고 매겼지만, 사람 전문가는 정확성에서 ChemCrow가 훨씬 낫다고 봤습니다. 결론은 «reflection» 구성요소만이 아니라 자기 평가에 관한 것입니다.</p>
<blockquote><p>&#8220;The lack of expertise may cause LLMs not knowing its flaws and thus cannot well judge the correctness of task results.&#8221;</p></blockquote>
<p>Weng은 이 글 어디에서도 MarsDawn을 언급하지 않고 Markdown 도구도 추천하지 않습니다.</p>

<h2>우리의 읽기이지 Weng의 것이 아님</h2>
<p>Weng은 2023년의 에이전트 아키텍처를 설명할 뿐, 에이전트 출력을 읽는 사람을 쓰지 않습니다 &#8212; 파일을 확인하는 사람도 언급하지 않습니다. 하지만 세 구성요소는 당신이 읽게 될 수 있는 서로 다른 세 가지에 대응합니다. 계획은 대개 실행 전에 읽을 문서를 남깁니다 &#8212; 계획 자체, 때로는 이미 접혀 든 «reflection»이나 자기 검토와 함께. 기억은 대개 보이지 않지만, 에이전트가 장기 저장으로 스크래치 파일을 유지하면 그 파일만 따로 열어 볼 가치가 있습니다. 옛 잘못된 가정이 이후 여러 단계에 말없이 실릴 수 있기 때문입니다. 도구 사용은 무엇이 돌았고 무엇이 돌아왔는지에 대한 보고서를 남기기 쉽습니다 &#8212; 계획보다 전사에 가깝습니다.</p>
<p>예상치 못한 오류에 계획이 조정되지 않는다는 지적은, 당신 쪽에서 보면 어제 승인한 계획이 오늘은 이미 낡았을 수 있는 이유입니다. 계획이 예상하지 못한 일이 중간에 생겨도 에이전트는 다시 계획하지 않고 그대로 갈 수 있고, 마지막 보고는 우회를 말하지 않은 채 원래 계획의 성공만 그릴 수 있습니다. 이는 우리의 추론이지 그녀의 주장이 아닙니다 &#8212; 그녀는 모델 자체의 견고함을 쓰고, 읽는 사람이 무엇을 봐야 하는지는 쓰지 않습니다.</p>

<h2>MarsDawn이 돕는 곳, 돕지 않는 곳</h2>
<p>MarsDawn 안에는 AI 모델이 없어 계획이 실제로 일어난 일에서 조용히 벗어났는지 말해 주지 못하고, 계획 파일·기억 파일·도구 사용 보고서도 구분하지 않습니다 &#8212; 내용에 대한 읽기이고, 그 판단은 당신 몫입니다. 하는 일은 이렇습니다. 개요 탭(보기 &#9656; 사이드바 보기, &#8963;&#8984;S)이 긴 계획의 형태를 한눈에 보여 주고, 소스와 렌더링된 미리보기가 나란히(⌘2) Mermaid와 KaTeX를 그리며, 읽는 도중에 에이전트가 파일을 다시 쓰면 저장하지 않은 변경이 없는 한 위치를 유지한 채 다시 불러옵니다 &#8212; 말없이 고쳐진 계획이 바로 그녀가 «Challenges»에서 모델 쪽에서 묘사한 실패 모드이기 때문에 특히 쓸모 있습니다.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 곧 Mac App Store에 올라갑니다. 무료 <code>marsdawn</code> 명령줄 도구는 오늘부터 쓸 수 있습니다:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>앱 없이 Markdown을 PDF로 내보냅니다.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; 구입 전에: <a href="/ko/limits/">MarsDawn이 하지 않는 일</a></p>

<h2>다음</h2>
<ul>
  <li>서로 다른 에이전트 설계 패턴이 남기기 쉬운 문서: <a href="/ko/agent-design-patterns/">에이전트 설계 패턴 네 가지와 각각이 건네는 문서</a></li>
  <li>계획이 돌기 전 5분 검토법: <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 만에 검토하기</a></li>
  <li>시리즈로 돌아가기: <a href="/ko/reading-notes/">편집자의 독서 노트</a></li>
</ul>

<h2>출처</h2>
<ul>
  <li>Lilian Weng, &#8220;LLM Powered Autonomous Agents,&#8221; Lil’Log, June 23, 2023: <a href="https://lilianweng.github.io/posts/2023-06-23-agent/">https://lilianweng.github.io/posts/2023-06-23-agent/</a> (2026-09-26에 가져와 인용; 쓸 당시 OpenAI에 있었으며, 여기서는 그때의 소속만 적습니다).</li>
</ul>
""",
    }


    pages['reading-notes/harrison-chase-what-is-an-agent'] = {
        "title": 'Harrison Chase의 스펙트럼: agentic할수록 더 지켜보고 싶어진다 · MarsDawn',
        "description": 'Harrison Chase의 2024년 에이전트 정의와 agentic 행동의 스펙트럼, 그리고 시스템이 그 위를 따라갈수록 관측 가능성이 필요하다는 주장 — 에이전트가 돌려준 파일을 읽는 쪽에서의 읽기.',
        "body": f"""
<section class="intro">
  <h1>Harrison Chase의 스펙트럼: agentic할수록 더 지켜보고 싶어진다</h1>
</section>

<div class="summary"><p><strong>2024년 6월 LangChain의 Harrison Chase는 겉보기엔 작은 질문 &#8212; «What is an agent?» &#8212; 으로 새 시리즈를 열었고, 기술적 정의와 «agentic» 행동의 스펙트럼으로 답했습니다. 시스템이 그 스펙트럼을 더 많이 차지할수록, 그는 말합니다, 돌아가는 동안 안을 볼 수 있어야 합니다.</strong></p></div>

<h2>글이 주장하는 것</h2>
<p>Chase 자신의 정의는, 대부분의 사람이 생각하는 에이전트보다 더 기술적이고 더 넓다는 단서와 함께 나옵니다.</p>
<blockquote><p>&#8220;An agent is a system that uses an LLM to decide the control flow of an application.&#8221;</p></blockquote>
<p>Control flow는 프로그램이 다음에 어떤 단계를 돌릴지일 뿐입니다. 그는 바로 정의가 불완전하다고 인정합니다 &#8212; LLM이 두 경로 사이를 라우팅만 하는 단순 시스템도 그의 정의로는 에이전트지만, 대부분의 «에이전트» 직관과는 맞지 않습니다. 라벨을 두고 싸우기보다 Andrew Ng의 제안을 받아들입니다. 트윗을 직접 인용하고 출처를 밝힙니다. «rather than arguing over which work to include or exclude as being a true agent, we can acknowledge that there are different degrees to which systems can be agentic.» Chase의 코멘트: «I really agree with this viewpoint and I think Andrew expressed it nicely.» 거기서부터, 시스템이 «agentic»한 정도는 LLM이 행동을 얼마나 결정하느냐에 따라, 고정 라우터에서 상태 기계, 자신의 도구를 만들고 기억하는 완전 자율 에이전트까지입니다. 실용적 주장은 그 스펙트럼에서 나옵니다 &#8212; 더 agentic할수록 특정 인프라가 더 중요하고, 그중 으뜸이 관측 가능성입니다.</p>
<blockquote><p>&#8220;You&#8217;ll want the ability to observe what is going on inside, since the exact steps taken may not be known ahead of time.&#8221;</p></blockquote>
<p>보기만이 아니라 개입까지 확장합니다. 실행 중인 에이전트의 상태나 지시를 특정 지점에서 바꿔, 의도한 길에서 벗어나면 다시 밀어 넣을 수 있어야 한다는 것입니다. Chase는 이 글 어디에서도 MarsDawn을 언급하지 않고 Markdown 도구도 추천하지 않습니다.</p>

<h2>우리의 읽기이지 Chase의 것이 아님</h2>
<p>Chase가 쓰는 대상은 에이전트 프레임워크를 만드는 사람을 위한 도구 &#8212; 이름으로 LangGraph와 LangSmith &#8212; 이지, 끝난 문서를 읽는 사람이 아닙니다. 하지만 그 스펙트럼은 읽기 전에 앞에 놓인 것을 가늠하는 유용한 방법입니다. 파일을 만든 시스템이 더 agentic할수록, 프롬프트만으로 단계를 예측하기 어렵고, 앞의 파일은 «되어야 할 일»보다 «실제로 일어난 일»의 기록으로 다룰 가치가 커집니다.
«observe what is going on inside»는 실행 중 시스템의 내부 &#8212; 트레이스(한 번의 실행에서 에이전트가 한 일의 기록), 중간 단계, 도구 호출 &#8212; 에 관한 것이지, 끝난 뒤 Markdown 계획을 읽는 일이 아닙니다. 하지만 그가 드는 이유, 정확한 단계를 미리 알 수 없을 수 있다는 점은, 에이전트가 끝난 뒤 건네는 문서에도 그대로 적용됩니다. 들어가는 쪽에서 단계가 예측되지 않았다면, 나오는 쪽 보고서가 그 단계를 확인할 유일한 자리입니다.</p>

<h2>MarsDawn이 돕는 곳, 돕지 않는 곳</h2>
<p>MarsDawn은 실행 중 에이전트의 내부를 관측하지 않습니다 &#8212; 안에 AI 모델도 없고 파일을 만든 프레임워크와도 연결되어 있지 않아, 주어진 에이전트가 Chase의 스펙트럼 어디에 있었는지 말해 줄 수 없습니다. 나중에 떨어지는 문서를 다룹니다. 긴 보고서의 형태를 위한 개요 탭(보기 &#9656; 사이드바 보기, &#8963;&#8984;S), 다이어그램과 수식을 위한 소스·렌더 나란히(⌘2), 에이전트가 파일을 다시 쓸 때 저장하지 않은 변경이 없는 한 위치를 유지하는 다시 불러오기 &#8212; 아직 움직이는 것을 지켜보는 일의 파일 버전입니다. 편집 &#9656; 참조 복사 (&#8997;&#8984;C)와 AI용으로 복사 (&#8963;&#8997;&#8984;C)로 단계가 빗나간 곳을 정확히 가리킬 수 있습니다 &#8212; 실행 중 에이전트를 다시 밀어 넣는 일의 문서 쪽 대응입니다.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 곧 Mac App Store에 올라갑니다. 무료 <code>marsdawn</code> 명령줄 도구는 오늘부터 쓸 수 있습니다:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>앱 없이 Markdown을 PDF로 내보냅니다.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; 구입 전에: <a href="/ko/limits/">MarsDawn이 하지 않는 일</a></p>

<h2>다음</h2>
<ul>
  <li>이 시리즈에서 투명성과 체크포인트를 더 자세히 다룬 글: <a href="/ko/agent-transparency/">Anthropic은 에이전트가 투명해야 한다고 말합니다. 그럼 펼쳐 놓은 것은 누가 읽을까요?</a></li>
  <li>같은 주소의 2026년 LangChain 글, 거의 같은 정의: <a href="/ko/reading-notes/langchain-what-is-an-agent/">Jess Ou의 평가 파이프라인, 그중 한 단계는 여전히 당신의 일</a></li>
  <li>시리즈로 돌아가기: <a href="/ko/reading-notes/">편집자의 독서 노트</a></li>
</ul>

<h2>출처</h2>
<ul>
  <li>Harrison Chase, &#8220;What is an agent?,&#8221; LangChain, June 28, 2024, 아카이브 사본: <a href="http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/">http://web.archive.org/web/20240724003401/https://blog.langchain.dev/what-is-an-agent/</a> (2026-09-26에 Wayback Machine으로 가져와 인용; 원래 주소에는 이제 Jess Ou의 2026년 글이 있습니다).</li>
</ul>
""",
    }


    pages['reading-notes/langchain-what-is-an-agent'] = {
        "title": 'Jess Ou의 평가 파이프라인, 그중 한 단계는 여전히 당신의 일 · MarsDawn',
        "description": 'LangChain의 2026년 «What is an AI agent?»(Jess Ou)는 Harrison Chase의 2024년 정의를 이어받고, 에이전트를 자동으로 평가하는 파이프라인을 그립니다. 그 파이프라인이 아직 사람에게 넘기는 단계, 그리고 넘기지 않는 단계.',
        "body": f"""
<section class="intro">
  <h1>Jess Ou의 평가 파이프라인, 그중 한 단계는 여전히 당신의 일</h1>
</section>

<div class="summary"><p><strong>2026년 7월 LangChain은 Harrison Chase의 2024년 «What is an agent?»가 있던 주소에 Jess Ou가 쓴 새 «What is an AI agent?»를 올렸습니다. 정의는 거의 그의 것과 한 글자 같습니다. 글의 대부분은 그의 글이 다루지 않았던 것, 에이전트를 자동으로 평가하는 파이프라인 전체에 관한 것입니다. 그 파이프라인이 아직 사람이 필요한 곳과 아닌 곳을 솔직히 말합니다.</strong></p></div>

<h2>글이 주장하는 것</h2>
<p>Ou의 정의는 Chase의 것과 가깝게 맞닿습니다.</p>
<blockquote><p>&#8220;An AI agent is a system that uses a large language model to decide the control flow of an application.&#8221;</p></blockquote>
<p>Control flow는 다시, 다음에 어떤 단계가 도는지일 뿐입니다. 이어서 LangChain의 Agent Development Lifecycle &#8212; build, test, deploy, monitor &#8212; 과, 사람이 매번 실행을 읽지 않고도 에이전트 일을 검사하는 층위 접근을 설명합니다. 온라인 eval은 프로덕션 트레이스(실제 실행의 기록)를 샘플링해 회귀를 찾고, 오프라인 eval은 큐레이션된 데이터셋으로 배포 전 나쁜 변경을 잡으며, «LLM-as-a-judge»는 사람이 미리 정한 기준으로 실행 출력을 채점해 수동 검토가 못 미치는 규모를 감당합니다. 그 파이프라인에 사람이 남는 자리를 분명히 말합니다.</p>
<blockquote><p>&#8220;For sensitive or irreversible actions, we recommend human-in-the-loop controls that pause the agent for approval, edits, rejection, or clarification.&#8221;</p></blockquote>
<p>파이프라인이 아무리 좋아져도 스케일되지 않는 판단에 대한 문장도 있습니다. «Do not outsource judgment you cannot evaluate. If you wouldn’t recognize a correct answer, neither will the agent.» <code>/reviewing-agent-plans/</code>가 이미 바로 그 문장 위에 세워져 있으므로 &#8212; 이 노트는 그 논의를 반복하지 않습니다. Ou는 MarsDawn을 언급하지 않고 Markdown 도구도 추천하지 않습니다. Chase의 이름도 부르지 않습니다. 두 글을 잇는 것은 LangChain이 2026년에 그의 2024년 글이 있던 주소에, 거의 같은 정의로 그녀의 글을 올렸다는 점 &#8212; 그녀가 아니라 우리가 하는 관찰입니다.</p>

<h2>우리의 읽기이지 Ou의 것이 아님</h2>
<p>Ou의 human-in-the-loop 줄은 특정 행동을 실행 전에 막는 일에 관한 것입니다 &#8212; write action을 승인 위해 멈추는 것, Chip Huyen의 read-only/write 구분이 다른 각도에서 가리키는 같은 아이디어 &#8212; 이지, 끝난 보고서를 나중에 읽는 일이 아닙니다. 자세히 읽으면 파이프라인의 대부분은 사람을 일상 검사에서 빼내도록 설계되어 있습니다. 넣도록이 아니라. 온라인·오프라인 eval과 LLM-as-a-judge는 팀이 모든 트레이스를 손으로 검토하지 않아도 되게 하려고 있습니다.
글에 대한 비판이 아닙니다 &#8212; 그것이 명시된 목표이고, 프로덕션 규모에서는 합리적입니다. 하지만 손으로 하는 검토 &#8212; 에이전트가 직접 건네는 계획이나 보고서를 읽는 일 &#8212; 은 바로 그 파이프라인이 줄이려 하지, 대체하려 하지 않는 종류의 확인입니다. 판단에 대한 그녀 자신의 문장은 그 축소에 바닥을 둡니다. 옳은 답과 틀린 답을 스스로 구별할 수 없는 곳에서는, 여전히 직접 읽어야 합니다.</p>

<h2>MarsDawn이 돕는 곳, 돕지 않는 곳</h2>
<p>MarsDawn은 eval 파이프라인이 아니고 안에 AI 모델도 없습니다 &#8212; 트레이스를 채점하지도, LLM-as-a-judge를 돌리지도, 어떤 행동이 멈출 만큼 민감한지 정하지도 않습니다. 그 파이프라인이 아직 사람에게 넘기는 순간, 즉 직접 읽는 일을 위해 만들어졌습니다. 개요 탭(보기 &#9656; 사이드바 보기, &#8963;&#8984;S)이 긴 보고서의 제목을 나열하고, 소스와 렌더 미리보기가 나란히(⌘2) Mermaid와 KaTeX를 그리며, 편집 &#9656; 참조 복사 (&#8997;&#8984;C)와 AI용으로 복사 (&#8963;&#8997;&#8984;C)가 한곳 확인을 에이전트가 움직일 수 있는 정확한 피드백으로 바꿉니다.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 곧 Mac App Store에 올라갑니다. 무료 <code>marsdawn</code> 명령줄 도구는 오늘부터 쓸 수 있습니다:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>앱 없이 Markdown을 PDF로 내보냅니다.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; 구입 전에: <a href="/ko/limits/">MarsDawn이 하지 않는 일</a></p>

<h2>다음</h2>
<ul>
  <li>그녀의 «outsource judgment» 줄에서 일부 나온 체크리스트 전체: <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 만에 검토하기</a></li>
  <li>같은 정의가 2024년에 처음 적힌 곳: <a href="/ko/reading-notes/harrison-chase-what-is-an-agent/">Harrison Chase의 스펙트럼: agentic할수록 더 지켜보고 싶어진다</a></li>
  <li>시리즈로 돌아가기: <a href="/ko/reading-notes/">편집자의 독서 노트</a></li>
</ul>

<h2>출처</h2>
<ul>
  <li>Jess Ou, &#8220;What is an AI agent?,&#8221; LangChain, July 31, 2026: <a href="https://www.langchain.com/blog/what-is-an-agent">https://www.langchain.com/blog/what-is-an-agent</a> (2026-09-26에 가져와 인용).</li>
</ul>
""",
    }


    pages['reading-notes/andrew-ng-design-patterns'] = {
        "title": 'Andrew Ng이 자신의 설계 패턴을 예측 가능성으로 순위를 매깁니다 · MarsDawn',
        "description": 'The Batch의 편지 다섯 편에서 Andrew Ng은 성찰, 도구 사용, 계획, 다중 에이전트 협업을 각각 얼마나 믿을 만하고 예측 가능한지로 순위를 매깁니다 — 그리고 그 순위가 각 패턴의 출력을 얼마나 자세히 볼지에 대해 시사하는 바.',
        "body": f"""
<section class="intro">
  <h1>Andrew Ng이 자신의 설계 패턴을 예측 가능성으로 순위를 매깁니다</h1>
</section>

<div class="summary"><p><strong>2024년 초 The Batch의 편지 다섯 편에서 Andrew Ng은 네 가지 agentic 설계 패턴 &#8212; 성찰, 도구 사용, 계획, 다중 에이전트 협업 &#8212; 을 설명하고, 드물게도 어떤 것을 더 믿을 만하고 어떤 것을 예측하기 어렵다고 보는지 독자에게 분명히 말했습니다.</strong></p></div>

<h2>편지가 주장하는 것</h2>
<p><code>/agent-design-patterns/</code>는 이미 네 패턴이 각각 무엇인지, 각각이 읽히게 남기기 쉬운 문서(우리의 추론), 그리고 4부에서 인용한 계획에 대한 Ng 자신의 판정을 다룹니다. «while I can get the agentic design patterns of Reflection and Tool Use to work reliably and improve my applications’ performance, Planning is a less mature technology, and I find it hard to predict in advance what it will do.» 이 노트는 그 페이지가 빼놓은 편지 두 편에서 같은 순위를 보탭니다. 4부 일주일 전인 3부에서 미리 순위를 말하고, 4부가 언급하지 않은 패턴 &#8212; 다중 에이전트 협업 &#8212; 까지 5부에서 확장합니다. 3부에서 도구 사용을 소개하며 이렇게 씁니다.</p>
<blockquote><p>&#8220;In future letters, I&#8217;ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable &#8212; albeit very exciting &#8212; technologies.&#8221;</p></blockquote>
<p>이틀 주 뒤, 다중 에이전트 협업으로 시리즈를 닫으며 같은 순위를 반대쪽에서 확인합니다.</p>
<blockquote><p>&#8220;Like the design pattern of Planning, I find the output quality of multi-agent collaboration hard to predict, especially when allowing agents to interact freely and providing them with multiple tools. The more mature patterns of Reflection and Tool Use are more reliable.&#8221;</p></blockquote>
<p>이는 각 패턴이 애플리케이션 결과를 얼마나 잘 개선하는지에 관한 말이지, 사람이 출력을 얼마나 자세히 봐야 하는지에 관한 말이 아닙니다 &#8212; 이 시리즈 어디에도 사람 검토를 요구하지 않고, MarsDawn을 언급하거나 Markdown 도구를 추천하지도 않습니다.</p>

<h2>우리의 읽기이지 Ng의 것이 아님</h2>
<p>Ng의 순위는 만드는 사람 자리에서의 출력 품질과 예측 가능성에 관한 것이지만, 대략 당신 자리에서 각 패턴의 종이 흔적을 얼마나 자세히 볼지에 맞춰집니다. 그가 더 믿을 만하다고 보는 성찰과 도구 사용은 대개 이미 끝난 일을 적는 것을 건넵니다 &#8212; 고쳐진 초안, 무엇이 돌았는지에 대한 보고서 &#8212; 그래서 주장 하나를 실제 출력과 맞춰 보면 대개 위험을 덮습니다. 예측하기 어렵다고 보는 계획과 다중 에이전트 협업은 대개 일이 일어나기 전에 쓰인 것, 또는 여러 에이전트의 여러 파일에 나뉜 것을 건넵니다.
승인을 기다리는 계획, 또는 실행이 아직 시험하지 않은 에이전트 간 인수인계. 그 자신의 말로, 바로 그 두 문서에서 적힌 것과 실제로 일어날 일 사이의 틈이 가장 넓습니다 &#8212; <code>/reviewing-agent-plans/</code>가 Chip Huyen 에세이의 «왜 돌리기 전에 보나» 절에서 끌어오는 같은 지점입니다. 아무것도 돌기 전에 문제를 잡는 것이 가장 값싼 자리입니다.</p>

<h2>MarsDawn이 돕는 곳, 돕지 않는 곳</h2>
<p>MarsDawn은 Ng의 네 패턴 중 어느 것이 주어진 파일을 만들었는지 모르고, 예측 가능성으로 순위를 매기지도 않으며, 안에 AI 모델도 없습니다 &#8212; 그 순위가 시사하는 확인을 대신 해 주지 않습니다. 당신이 하는 동안 파일을 읽기 쉽게 유지합니다. 개요 탭(보기 &#9656; 사이드바 보기, &#8963;&#8984;S)이 긴 계획의 형태를 보여 주고, 소스와 렌더 미리보기가 나란히(⌘2) 있으며, 다중 에이전트 인수인계에서는 파일 &#9656; 폴더 열기&#8230; (&#8679;&#8984;O)으로 공유 폴더를 열면 서로 다른 에이전트가 쓸 때 약 1초 안에 파일 탭에 새 파일이 나타나고, 헤더가 git 브랜치나 worktree 이름을 보여 같은 이름의 파일이 서로 다른 에이전트 것인데 헷갈리지 않게 합니다.</p>

<h2>사용해 보기</h2>
<p>MarsDawn은 곧 Mac App Store에 올라갑니다. 무료 <code>marsdawn</code> 명령줄 도구는 오늘부터 쓸 수 있습니다:</p>
<pre><code>{k.INSTALL}</code></pre>
<p>앱 없이 Markdown을 PDF로 내보냅니다.</p>
<p><a href="/ko/cli/">명령줄</a> &#183; 구입 전에: <a href="/ko/limits/">MarsDawn이 하지 않는 일</a></p>

<h2>다음</h2>
<ul>
  <li>각 패턴이 건네기 쉬운 문서 전체: <a href="/ko/agent-design-patterns/">에이전트 설계 패턴 네 가지와 각각이 건네는 문서</a></li>
  <li>계획이 돌기 전 5분 검토법: <a href="/ko/reviewing-agent-plans/">에이전트의 계획을 5분 만에 검토하기</a></li>
  <li>시리즈로 돌아가기: <a href="/ko/reading-notes/">편집자의 독서 노트</a></li>
</ul>

<h2>출처</h2>
<ul>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 1,&#8221; The Batch, March 20, 2024: <a href="https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/">https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/</a></li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 3: Tool Use,&#8221; The Batch, April 3, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/</a> (2026-09-26에 가져와 인용).</li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 4: Planning,&#8221; The Batch, April 10, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/</a> (<code>design/inbox/276-agent-blog-series.md</code>에서 그대로 재사용, 이미 <code>/agent-design-patterns/</code>에 인용됨).</li>
  <li>Andrew Ng, &#8220;Agentic Design Patterns Part 5, Multi-Agent Collaboration,&#8221; The Batch, April 17, 2024: <a href="https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/">https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-5-multi-agent-collaboration/</a> (2026-09-26에 가져와 인용).</li>
</ul>
""",
    }

    pages['privacy'] = {
        "title": '개인정보 처리방침 · MarsDawn',
        "description": 'MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.',
        "body": k.render_legal_body("privacy", "ko"),
    }
    pages['support'] = {
        "title": '지원 · MarsDawn',
        "description": 'macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.',
        "body": k.render_legal_body("support", "ko"),
    }
    tables = {
        'app_ui_languages': app_ui_languages,
        'home': home,
        'compare': {key: {'head': t['head'], 'rows': t['rows']} for key, t in compare_tables.items()},
        'exit_table_head': exit_table_head,
        'exit_remedy': exit_remedy,
        'theme_shots': {image: {'name': name, 'alt': alt} for image, (name, alt) in theme_shots.items()},
        'theme_gallery_note': theme_gallery_note,
        'skip_label': '본문으로 건너뛰기',
        'toc_label': {'privacy': '이 페이지의 내용', 'support': '질문으로 이동'},
        'not_found': {'title': '페이지를 찾을 수 없음 · MarsDawn', 'headline': '별들 사이에서 길을 잃었습니다.', 'body': '이 길은 지도에 없습니다. 조용한 이웃이 집으로 가는 길을 가리켜 주었습니다.', 'home': 'MarsDawn으로 돌아가기', 'alt': '화성의 새벽하늘에 작은 우주선이 떠 있고, 친근한 외계인이 행성의 밝은 가장자리를 가리키고 있습니다.'},
        # Not in Grok's material (the window label and the Markdown twin's sentence): written for #162.
        'hero_window_label': '직접 조작할 수 있는 MarsDawn 창: 테마와 레이아웃을 고르세요',
        'hero_window_markdown': {'template': '이 페이지에는 앱의 시작 가이드 일부를 보여 주는, 직접 조작할 수 있는 MarsDawn 창이 있습니다. 팔레트 메뉴에서 화면 모드({looks})를 고르고, 라이트와 다크에 각각 네 가지 미리보기 테마({themes}) 중 하나를 지정할 수 있으며, 도구 막대에서는 세 가지 레이아웃({layouts}) 중 하나를 고를 수 있습니다.', 'sep': ', '},
        'loop': loop_copy,
        'templates': templates,
    }
    return {
        'ui': ui, 'store_chip': store_chip, 'schema_notes': schema_notes, 'example_plan': example_plan,
        'trait_link': trait_link, 'trait_nav_heading': trait_nav_heading, 'figure_list_label': figure_list_label,
        'figures': figures, 'pages': pages, 'tables': tables,
    }
