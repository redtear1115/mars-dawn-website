# 개인정보 처리방침

macOS용 Markdown 편집기 MarsDawn이 사용자의 정보를 어떻게 다루는지 설명합니다.

최종 업데이트: 2026-09-28

> **MarsDawn 앱은 사용자에 관한 데이터를 일절 수집하지 않습니다.** 계정도, 광고도, 추적도 없습니다. 문서와 설정은 사용자의 Mac에 남습니다.

## 웹사이트

앱과 이 웹사이트는 서로 다릅니다. 앱은 아무것도 수집하지 않습니다. 방문 기록이 남을 수 있는 곳은 이곳 marsdawn.southern-light.dev뿐입니다.

이 사이트는 **Google Tag Manager**를 통해 불러오는 **Google Analytics 4**를 사용합니다. 모든 방문자는 분석이 거부된 상태로 시작합니다. 배너에서 *수락*을 선택하기 전까지 Google의 동의 모드(Consent Mode)는 분석 쿠키나 영구 식별자 없이 쿠키 없는 핑만 보냅니다. *거부*를 선택하거나 아무것도 선택하지 않으면 이 상태가 유지되며, 이전에 *수락*한 뒤 *거부*를 선택하면 분석이 즉시 다시 꺼지고 아래의 쿠키가 삭제됩니다. 선택은 모든 페이지 하단의 ‘쿠키 설정’ 링크에서 언제든지 바꿀 수 있습니다. 선택 자체는 브라우저의 로컬 저장소에만 저장되며, 저희 쿠키에는 절대 저장되지 않습니다.

수락하면 Google Analytics가 자체 쿠키(`_ga` 및 `_ga_<measurement id>`)를 설정하고 다음을 기록합니다.

- **페이지 조회 및 리퍼러.** 어떤 페이지를 보았는지, 그리고 브라우저가 보내는 경우 이전 페이지의 주소.
- **대략적인 위치, 기기 및 브라우저.** IP 주소에서 추정한 대략적인 위치(최대 도시 수준), 기기 유형, 운영 체제 및 브라우저. 어느 것도 사용자를 식별할 만큼 정확하지 않습니다.
- **외부 링크 클릭 및 스크롤 깊이.** Google Analytics의 향상된 측정 기능은 Mac App Store 링크처럼 사이트를 떠나는 클릭과, 페이지를 얼마나 아래로 스크롤했는지를 기록합니다.
- **IP 주소.** Google Analytics 4는 IP 주소를 기록하거나 저장하지 않습니다.
- **기록하지 않는 것.** 사이트에 계정이 없으므로 계정 정보는 없습니다. 문서도, 입력한 내용도 기록하지 않습니다. 교차 사이트 광고도, 사용자 프로필도 없습니다. 앱이 `/themes/` 아래의 테마 파일을 요청하는 경우는 제외되며, 전달되지 않습니다. `/themes/new/`와 `/themes/gallery/`의 테마 시뮬레이터와 갤러리는 전적으로 브라우저에서 실행되며, 테마 데이터를 Google Analytics로 보내지도 않습니다.
- **보관 기간.** Google은 이 데이터를 14개월 동안 보관한 뒤 삭제합니다.
- **처리 위치.** Google Tag Manager와 Google Analytics는 Google이 운영합니다. 데이터는 미국을 비롯해 Google이 사업을 운영하는 다른 국가에서 처리될 수 있습니다.
- **호스팅 업체.** 이 사이트는 Cloudflare가 호스팅하며, 여느 호스팅 업체와 마찬가지로 요청에 응답하는 동안 IP 주소를 보게 됩니다. 그 로그는 호스팅 업체의 것이며, 위에서 설명한 분석과는 별개입니다.

## Mac에 남는 것

- **문서.** MarsDawn은 사용자가 열거나 저장하거나 선택한 파일과 폴더만 읽고 씁니다. 앱이 이를 어딘가로 업로드하는 일은 없습니다.
- **설정.** 화면 모드, 미리보기 테마, 윈도우 레이아웃 및 이미지 설정은 Mac에 있는 앱 자체 환경설정에 저장됩니다.
- **허용한 폴더 접근.** MarsDawn이 폴더의 이미지나 페이지 파일을 보여주도록 허용하거나 메모 폴더를 선택하면, 앱은 그 폴더를 다시 열 수 있도록 macOS 책갈피를 보관합니다. 사이드바에서 연 폴더는 윈도우가 열려 있는 동안만이 아니라, 설정에서 제거할 때까지 MarsDawn이 읽고 쓸 수 있는 상태로 유지됩니다. 폴더는 언제든지 MarsDawn › 설정에서 제거할 수 있습니다.

## MarsDawn이 인터넷을 사용하는 경우

MarsDawn은 완전히 오프라인으로 작동합니다. 웹을 참조하는 문서에 대해 **사용자가 선택한 경우에만** 인터넷에 연결합니다.

- **Markdown 문서.** 웹 이미지는 기본적으로 차단됩니다. 미리보기에서 *이미지 불러오기*를 클릭하거나 설정에서 *원격 이미지 자동으로 불러오기*를 켠 경우에만 불러옵니다. 그 외에 Markdown 문서가 참조하는 어떤 것도 웹에서 불러오지 않습니다.
- **HTML 문서.** HTML 문서는 정적인 상태로 열립니다. 코드가 실행되지 않으며 웹에서 아무것도 불러오지 않습니다. 실행될 수 있는 코드가 문서에 포함되어 있으면, 해당 문서에 대해 *보기 › 이 문서 실행*을 선택할 수 있습니다. 그러면 사용자가 중단하거나, 문서가 다시 로드되거나, 윈도우를 닫을 때까지 문서 자체의 코드가 실행됩니다. 이 선택은 기억되지 않으며, 설정 항목도 아닙니다. 실행되는 동안 문서는 네트워크로 데이터를 보낼 수 있고, 문서가 있는 폴더와 그 하위 폴더의 이미지, 스타일시트, 서체 및 미디어를 읽을 수 있습니다. 웹에서 다운로드한 코드는 절대 실행되지 않습니다.

MarsDawn은 https로만 웹 콘텐츠를 불러옵니다. 일반 http 주소는 어떤 설정에서도 불러오지 않으며, MarsDawn이 이를 https로 바꿔 쓰지도 않습니다. Markdown 문서에서는 미리보기가 그 자리에 자리 표시자를 보여줍니다.

웹 콘텐츠를 불러올 때는 Mac이 해당 콘텐츠를 호스팅하는 서버에 직접 요청합니다. 다른 웹 요청과 마찬가지로, 이 서버들은 사용자의 IP 주소와 요청한 내용을 볼 수 있습니다. MarsDawn 개발자는 이 정보를 전혀 받지 않습니다.

미리보기에서 클릭한 링크는 기본 웹 브라우저에서 열리며, 해당 브라우저의 개인정보 처리 관행을 따릅니다. 오디오와 비디오는 절대 저절로 재생되지 않습니다.

## Siri, 단축어 및 Spotlight

MarsDawn은 문서 만들기나 메모 추가 같은 Siri, 단축어 앱 및 Spotlight용 동작을 제공합니다. 이 동작을 사용하면 입력한 텍스트가 Mac의 MarsDawn에 전달되어, 동작이 지정한 위치(새로운 문서 또는 선택한 메모 폴더의 `Inbox.md` 파일)에만 저장됩니다. Siri에 받아쓰게 한 음성은 [Apple 개인정보 처리방침](https://www.apple.com/legal/privacy/)에 따라 Apple이 처리합니다.

## 내보내기 및 프린트

PDF 내보내기와 프린트는 Mac에서 이루어집니다. PDF는 사용자가 선택한 위치에 저장됩니다. 프린트는 macOS를 거쳐 사용자가 고른 프린터로 전송됩니다.

## marsdawn 명령줄 도구

별도로 배포되는 선택 사항인 `marsdawn` 명령줄 도구도 전적으로 Mac에서 실행됩니다. 지정한 Markdown 파일을 읽고 요청한 PDF를 씁니다. 웹 이미지는 `--allow-remote-images`를 전달한 경우에만 불러옵니다.

## 아동

MarsDawn 앱은 아동을 포함해 누구의 데이터도 수집하지 않습니다. 웹사이트에 기록된 방문은 계정이 아니며, 누군가를 식별하는 데 사용되지 않습니다.

## 구입

MarsDawn은 Mac App Store를 통해 판매됩니다. 구입은 Apple이 자체 약관에 따라 처리하며, 개발자는 결제 정보를 절대 받지 않습니다.

## 이 방침의 변경

MarsDawn이 데이터를 다르게 처리하게 되는 경우, 해당 버전이 출시되기 전에 이 페이지를 업데이트하고 상단의 날짜를 변경합니다.

## 문의

개인정보 관련 문의: [support@southern-light.dev](mailto:support@southern-light.dev)

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): Mac용 네이티브 Markdown 편집기: 소스 옆 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험, 한 번만 USD 4.99.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록과 표를 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지입니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [Mac에서 Markdown 보기](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): .md 파일은 서식 기호가 들어 있는 일반 텍스트입니다. Mac에서 렌더링된 상태로 읽는 방법을 소개합니다. 지금 바로 무료 marsdawn 명령줄 도구로 PDF를 만들 수 있고, Mac App Store의 MarsDawn 앱에서 읽을 수도 있습니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): Finder에서 Markdown 파일을 선택하고 스페이스 바를 누르면 Mermaid 다이어그램, KaTeX 수식, 강조된 코드까지 렌더링된 모습으로 읽을 수 있습니다. MarsDawn의 훑어보기는 체험 기간의 제한을 받지 않습니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 Markdown을 읽기 전용으로 렌더링하며 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 무료로 체험한 뒤 Mac App Store에서 USD 4.99에 한 번만 구입하면 됩니다.
- [명령줄](https://marsdawn.southern-light.dev/ko/cli/index.md): Mac용 무료 marsdawn 명령줄 도구. 셸, 스크립트, LLM 에이전트에서 Markdown을 PDF로 내보내고 JSON으로 결과를 받으세요. Homebrew로 설치합니다.
- [에이전트를 위한 marsdawn](https://marsdawn.southern-light.dev/ko/cli/agents/index.md): marsdawn을 호출해 Markdown을 PDF로 바꾸는 AI 에이전트와 스크립트를 위한 레퍼런스입니다. 명령, JSON 출력, 스키마, 종료 코드, 요구 사항을 다룹니다.
- [에이전트 스킬](https://marsdawn.southern-light.dev/ko/cli/skill/index.md): 코딩 에이전트가 불러오는 파일 하나로, 에이전트가 쓴 Markdown을 MarsDawn에서 열어 검토하게 하고, marsdawn을 설치해 Markdown을 PDF로 내보내고 JSON 결과를 읽게 합니다.
- [MCP 서버](https://marsdawn.southern-light.dev/ko/cli/mcp/index.md): marsdawn에는 자체 AI 모델이 없으므로 어떤 에이전트가 Markdown을 썼는지는 상관없습니다. CLI, 스킬 파일, MCP 서버 marsdawn-mcp 중 어디서 호출하든 세 가지 모두 같은 내보내기를 실행합니다.
- [토큰을 아끼는 검토](https://marsdawn.southern-light.dev/ko/token-efficient-review/index.md): 렌더링된 페이지는 사람이 MarsDawn에서 검토하며, 에이전트의 컨텍스트로 다시 읽어 들이지 않습니다. 도구 호출은 렌더링된 내용이 아니라 간결한 JSON 결과를 돌려주므로 호출 자체도 부담이 적습니다.
- [다른 도구로 Markdown 보기와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/markdown-preview-tools/index.md): VS Code의 기본 미리보기, 브라우저 확장 프로그램, Claude Desktop의 파일 미리보기에서 Markdown을 읽는 것과 MarsDawn을 비교합니다. 각각 무엇을 렌더링하는지, 파일 하나를 여는 데 무엇이 필요한지 살펴보세요.
- [미리보기 테마와 PDF 내보내기](https://marsdawn.southern-light.dev/ko/themes/index.md): 라이트와 다크 팔레트를 각각 갖춘 미리보기 테마 네 가지, 그리고 지금 쓰는 테마를 그대로 따르는 PDF 내보내기와 프린트. 브라우저에서 테마를 직접 만들고, 커뮤니티 갤러리도 둘러보세요.
- [테마 만들기](https://marsdawn.southern-light.dev/ko/themes/new/index.md): 색과 몇 가지 스타일 옵션을 고르면 샘플 문서에 바로 반영됩니다. 만든 테마는 GitHub 이슈로 제출할 수 있습니다. 설치도 git도 필요 없습니다.
- [테마 갤러리](https://marsdawn.southern-light.dev/ko/themes/gallery/index.md): 커뮤니티가 MarsDawn에 제출한 미리보기 테마를 둘러보고, 용도로 걸러 보고, 문제가 있으면 신고하세요. 브라우저에서 직접 만드세요. 설치도 git도 필요 없습니다.
- [내보낸 PDF 공유하기](https://marsdawn.southern-light.dev/ko/sharing-exported-pdfs/index.md): 에이전트가 쓴 Markdown을 PDF로 내보내, Markdown을 읽지 않고 아무것도 설치하지 않을 동료에게 전달하세요. 문법도, 앱도, 계정도 없이 열립니다.
- [AI가 만든 결과물에 여전히 사람의 읽기가 필요한 이유](https://marsdawn.southern-light.dev/ko/reviewing-ai-output/index.md): AI가 쓴 Markdown은 보자마자 믿을 것이 아니라 사람이 이해해야 합니다. MarsDawn은 렌더링된 페이지를 원본 옆에 두고 Mermaid 다이어그램과 KaTeX 수식을 그려 주어, 구조를 한눈에 읽을 수 있게 합니다.
- [에이전트가 돌려준 결과 읽기](https://marsdawn.southern-light.dev/ko/reading-agent-output/index.md): AI 에이전트는 계획, 사양서, 진행 보고서 같은 결과를 Markdown으로 돌려줍니다. 에이전트를 만드는 사람들이 체크포인트와 실패에 대해 하는 말, 그 결과물이 읽기 어려운 이유, 그리고 계획을 5분 만에 검토하는 체크리스트를 소개합니다.
- [에이전트의 투명성](https://marsdawn.southern-light.dev/ko/agent-transparency/index.md): Anthropic의 에이전트 구축 가이드는 투명성, 즉 계획 단계를 보여 줄 것을 요구합니다. 가이드가 말하는 것과 말하지 않는 것, 그리고 그 단계들이 왜 대개 누군가 읽어야 하는 Markdown 파일로 끝나는지 살펴봅니다.
- [에이전트의 계획 검토하기](https://marsdawn.southern-light.dev/ko/reviewing-agent-plans/index.md): AI 에이전트가 넘긴 계획을 실행 전에 약 5분 동안, 어떤 에디터에서든 검토하는 6단계 방법을 예시와 함께 소개합니다.
- [에이전트 설계 패턴](https://marsdawn.southern-light.dev/ko/agent-design-patterns/index.md): Andrew Ng이 설명한 리플렉션, 도구 사용, 계획, 멀티 에이전트 협업과, 각 패턴이 보통 읽을거리로 넘기는 것을 정리했습니다.
- [변경 내역](https://marsdawn.southern-light.dev/ko/changelog/index.md): 무료 marsdawn 명령줄 도구에서 바뀐 점입니다.
- [편집자의 독서 노트](https://marsdawn.southern-light.dev/ko/reading-notes/index.md): AI 에이전트를 만드는 사람들이 실제로 무엇을 주장하는지 살피는 짧은 노트 여섯 편 — Anthropic, Chip Huyen, Lilian Weng, Harrison Chase, LangChain, Andrew Ng — 그리고 각각이 그런 에이전트가 돌려준 것을 읽어야 하는 사람에게 무엇을 의미하는지.
- [독서 노트: Anthropic](https://marsdawn.southern-light.dev/ko/reading-notes/anthropic-building-effective-agents/index.md): 2024년 12월 Anthropic이 에이전트를 만드는 사람을 위해 낸 가이드는 workflow와 agent를 나누고, 그중 하나가 두 번째 LLM 호출로 첫 번째를 검토하는 다섯 가지 workflow 패턴을 설명합니다. 그게 폴더에 떨어지는 파일에 무엇을 뜻하는지.
- [독서 노트: Chip Huyen](https://marsdawn.southern-light.dev/ko/reading-notes/chip-huyen-agents/index.md): Chip Huyen의 2025년 1월 에세이 «Agents»는 에이전트 행동을 read-only와 write로 나눕니다. 그 구분이 계획에서 승인 전에 더 자세히 볼 줄을 빠르게 짚는 방법이 되는 이유.
- [독서 노트: Lilian Weng](https://marsdawn.southern-light.dev/ko/reading-notes/lilian-weng-llm-agents/index.md): Lilian Weng의 널리 인용되는 2023년 서베이는 LLM 에이전트를 뇌와 계획·기억·도구 사용으로 그립니다. 각 부분이 당신에게 남기기 쉬운 파일, 그리고 예상치 못한 일에 조정되지 않는 계획에서 그녀가 짚는 한계.
- [독서 노트: Harrison Chase](https://marsdawn.southern-light.dev/ko/reading-notes/harrison-chase-what-is-an-agent/index.md): Harrison Chase의 2024년 에이전트 정의와 agentic 행동의 스펙트럼, 그리고 시스템이 그 위를 따라갈수록 관측 가능성이 필요하다는 주장 — 에이전트가 돌려준 파일을 읽는 쪽에서의 읽기.
- [독서 노트: LangChain(Jess Ou)](https://marsdawn.southern-light.dev/ko/reading-notes/langchain-what-is-an-agent/index.md): LangChain의 2026년 «What is an AI agent?»(Jess Ou)는 Harrison Chase의 2024년 정의를 이어받고, 에이전트를 자동으로 평가하는 파이프라인을 그립니다. 그 파이프라인이 아직 사람에게 넘기는 단계, 그리고 넘기지 않는 단계.
- [독서 노트: Andrew Ng](https://marsdawn.southern-light.dev/ko/reading-notes/andrew-ng-design-patterns/index.md): The Batch의 편지 다섯 편에서 Andrew Ng은 성찰, 도구 사용, 계획, 다중 에이전트 협업을 각각 얼마나 믿을 만하고 예측 가능한지로 순위를 매깁니다 — 그리고 그 순위가 각 패턴의 출력을 얼마나 자세히 볼지에 대해 시사하는 바.
- [템플릿](https://marsdawn.southern-light.dev/ko/templates/index.md): 에이전트가 쓰고 여러분이 읽는 문서를 위한 Markdown 템플릿입니다. 명세서, 순서도, 회의록이 있으며, 각각 에이전트에게 줄 프롬프트가 함께 제공됩니다.
- [명세서 템플릿](https://marsdawn.southern-light.dev/ko/templates/spec/index.md): 요구 사항, Mermaid 흐름도, 인수 기준이 들어 있는 Markdown 명세서 템플릿입니다. 에이전트가 채우고, 여러분은 MarsDawn에서 검토하세요.
- [순서도 템플릿](https://marsdawn.southern-light.dev/ko/templates/flowchart/index.md): Markdown으로 쓰는 Mermaid 순서도 템플릿으로, 다이어그램 아래에 단계를 풀어 씁니다. Mac에서 미리 보고 PDF로 내보내세요.
- [회의록 템플릿](https://marsdawn.southern-light.dev/ko/templates/meeting-notes/index.md): 결정 사항과 담당자가 정해진 실행 항목을 정리하는 Markdown 회의록 템플릿입니다. 에이전트가 쓰고, 여러분은 MarsDawn에서 확인하세요.
- [English](https://marsdawn.southern-light.dev/privacy/index.md): MarsDawn does not collect personal data. Your documents and settings stay on your Mac.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/privacy/index.md): MarsDawn 不收集任何個人資料，你的文件與設定都留在你的 Mac 上。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/privacy/index.md): MarsDawn 不收集任何个人数据，你的文稿与设置都留在你的 Mac 上。
- [日本語](https://marsdawn.southern-light.dev/ja/privacy/index.md): MarsDawn は個人データを収集しません。文書と設定はあなたの Mac 上に残ります。
- [Deutsch](https://marsdawn.southern-light.dev/de/privacy/index.md): MarsDawn erhebt keine personenbezogenen Daten. Deine Dokumente und Einstellungen bleiben auf deinem Mac.
- [Français](https://marsdawn.southern-light.dev/fr/privacy/index.md): MarsDawn ne collecte aucune donnée personnelle. Vos documents et vos réglages restent sur votre Mac.
- [Español](https://marsdawn.southern-light.dev/es/privacy/index.md): MarsDawn no recopila datos personales. Tus documentos y tus ajustes se quedan en tu Mac.
