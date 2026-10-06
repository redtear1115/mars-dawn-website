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
        "description": '라이트와 다크 팔레트를 각각 갖춘 미리보기 테마 네 가지, 그리고 지금 쓰는 테마를 그대로 따르는 PDF 내보내기와 프린트. 가져올 수 있는 테마를 더 늘리고, 직접 만든 테마를 공유하는 갤러리도 계획하고 있습니다.',
        "body": f"""
<section class="intro">
  <h1>여덟 가지 모습, 하나의 내보내기.</h1>
  <p>MarsDawn에는 Dawn, Classic, Modern, Vivid 네 가지 미리보기 테마가 있고, 각각 라이트와 다크 팔레트를 갖추고 있습니다. 문서를 읽는 여덟 가지 조합입니다. PDF로 내보내거나 프린트하면, 읽고 있던 바로 그 조합으로 페이지가 나옵니다.</p>
</section>

<div class="summary"><p><strong>테마 네 가지 &#215; 라이트와 다크 = 문서를 읽는 여덟 가지 방법, 그리고 고른 것을 그대로 따르는 하나의 내보내기 경로.</strong> 가져올 수 있는 테마를 더 늘리고 직접 만든 테마를 공유하는 갤러리도 계획하고 있지만, 아직 만들어지지 않았습니다.</p></div>

<h2>네 가지 테마</h2>
<!--theme-gallery-->
<ul>
  <li><strong>Dawn</strong>(기본값): 이 사이트를 이루는 것과 같은 따뜻한 종이 색과 Mars Rust 강조색.</li>
  <li><strong>Classic</strong>: 더 담백하고 문서다운 팔레트.</li>
  <li><strong>Modern</strong>: 더 차분하고 현대적인 팔레트.</li>
  <li><strong>Vivid</strong>: 더 밝고 대비가 강한 팔레트.</li>
</ul>
<p>테마마다 라이트와 다크 변형이 따로 있어서, Mac의 화면 모드를 바꾸면 인터페이스만이 아니라 테마의 팔레트도 함께 바뀝니다.</p>

<h2>PDF 내보내기와 프린트도 같은 테마로</h2>
<p>PDF로 내보내거나 프린트하면 페이지는 테마의 라이트 팔레트를 씁니다. Mermaid 다이어그램이 그대로 그려지고, 코드 블록은 구문 강조를 유지하며, 페이지 나눔은 제목과 본문을 떼어 놓거나 표나 다이어그램을 반으로 자르지 않습니다. 무료 <a href="/ko/cli/">marsdawn 명령줄 도구</a>도 같은 내보내기 엔진을 쓰므로, 스크립트나 에이전트도 <code>--theme</code>으로 네 가지 테마 중 어느 것이든 똑같은 PDF를 만듭니다.</p>

<h2>계획: 더 많은 테마와 갤러리</h2>
<p>아직 출시되지 않았고 나중에 나올 예정입니다. 가져올 수 있는 미리보기 테마를 더 늘리고, 사람들이 직접 만든 테마를 올릴 수 있는 갤러리를 이 사이트에 만들 계획입니다. <code>/themes/v1/</code>은 이미 그 용도로 잡아 두었습니다. 그전까지 MarsDawn에 있는 테마는 기본 테마 네 가지이며, 다른 테마는 설치할 수 없습니다.</p>

<h2>다음</h2>
<ul>
  <li>명령줄에서 PDF로 내보내는 전체 안내: <a href="/ko/markdown-to-pdf/">Markdown을 PDF로</a>.</li>
  <li>MarsDawn이 아직 하지 않는 일: <a href="/ko/limits/">목록</a>.</li>
  <li>Markdown을 쓰지 않는 사람에게 내보낸 PDF 전달하기: <a href="/ko/sharing-exported-pdfs/">PDF 공유하기</a>.</li>
</ul>
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
        '01-split': ('Dawn(기본값)', '분할 화면의 Dawn 테마: 왼쪽은 Markdown 소스, 오른쪽은 렌더링된 페이지.'),
        '02-classic': ('Classic', '미리보기가 윈도우 전체를 채운 Classic 테마.'),
        '04-vivid': ('Vivid', '분할 화면의 Vivid 테마.'),
        '03-dark': ('다크 모드', '다크 모드의 MarsDawn, 분할 화면.'),
    }
    theme_gallery_note = 'Modern은 아직 스크린샷이 없어서, 네 번째 이미지는 대신 다크 모드를 보여 줍니다.'

    app_ui_languages = '영어, 중국어(번체), 중국어(간체), 일본어, 독일어, 프랑스어, 스페인어, 한국어'
    return {
        'pages': pages, 'figures': figures, 'home': home, 'compare_tables': compare_tables,
        'exit_table_head': exit_table_head, 'exit_remedy': exit_remedy, 'app_ui_languages': app_ui_languages, 'example_plan': example_plan,
    }
