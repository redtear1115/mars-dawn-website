"""Korean (ko) page copy for the MarsDawn site, tranche 2 (#166).

Same shape as scripts/copy_ja.py: build(k) returns the tables build_pages.py keeps per locale.
Translated from the en copy on main @ 6fe8435. Marketing pages: 합니다 statements with 세요
requests; legal/support stay 합니다/하십시오. UI terms follow the app's ko strings
(release/1.1.0): 훑어보기 (Quick Look), 파일, 보기, 설정, 단축어, 윈도우, 프린트, 내보내기,
체험 (trial), 잠금 해제 (unlock), 구입. ASCII punctuation. Built-in theme names stay English.
Inline build_pages.py tables are returned under their own keys.
"""


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
  <li><strong>테마:</strong> Dawn, Classic, Modern, Vivid가 각각 라이트와 다크로 들어 있으며, 아직 다른 테마는 설치할 수 없습니다. 계획은 <a href="/ko/themes/">미리보기 테마와 PDF 내보내기</a>에서 확인하세요.</li>
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
  <li>모든 테마가 라이트와 다크 모두에서 WCAG AA 대비 기준을 충족합니다. Classic은 이제 흑백입니다.</li>
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
        'yours': {"alt": 'Classic 테마로 문서를 보여주는 MarsDawn. 미리보기가 윈도우를 가득 채우고 있습니다.',
                  "callouts": ['내 Mac에 있는 파일이고, 고른 곳에 저장됩니다.', '도구 막대에는 테마와 레이아웃뿐이고, 로그인할 곳은 없습니다.']},
        'pay-once': {"alt": 'Vivid 테마의 MarsDawn. 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.',
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
    app_ui_languages = '영어, 중국어(번체), 중국어(간체), 일본어, 독일어, 프랑스어, 스페인어, 한국어'
    return {
        'pages': pages, 'figures': figures, 'home': home, 'compare_tables': compare_tables,
        'exit_table_head': exit_table_head, 'exit_remedy': exit_remedy, 'app_ui_languages': app_ui_languages,
    }
