# 에이전트와 함께 테마 만들기

MarsDawn 미리보기 테마를 만드는 AI 에이전트를 위한 참고 자료입니다. 에이전트는 `theme.json` 하나를 쓰고 명령줄 도구 `marsdawn`으로 검사하고 렌더링한 뒤 링크를 건넵니다. 사람은 [테마 만들기](/ko/themes/new/) 페이지에서 눈으로 다듬어 제출합니다. 아래 필드 표는 kit의 소스 코드에서 직접 읽은 것이며, 검사가 둘이 같음을 보장합니다.

**`theme.json`을 쓰고, 종료 코드가 0이 될 때까지 `marsdawn theme validate theme.json --require-complete --json`을 실행하고, `marsdawn theme preview`로 라이트와 다크를 렌더링한 뒤 사람에게 링크를 건네세요.** 테마는 매개변수일 뿐이며 CSS를 담지 않습니다.

## 테마란 무엇인가

- 라이트와 다크 각각의 **색**: 기본 팔레트와 선택 사항인 구문 색, 다이어그램 색. 모두 `#RRGGBB` 형식입니다.
- **글꼴 디자인**: `sans`, `serif`, `rounded` 중 하나.
- **닫힌 스타일 옵션 집합**: 고정된 범위의 숫자와 고정된 목록에서 고르는 값. 스타일 옵션의 색은 항상 `accent` 같은 팔레트 역할이며 색 값을 직접 쓰지 않습니다.
- **표시 문자열**: 이름과 요약, 그리고 선택 사항인 작성자와 라이선스.

아래 표에 없는 키는 오류이며, 같은 키를 두 번 쓰는 것도 오류입니다. 파일은 최대 16,384바이트입니다.

## 검사하고 렌더링하기

`theme.json`이 있는 폴더에서 실행하세요. `marsdawn` 도구가 필요합니다. [에이전트를 위한 marsdawn](/ko/cli/agents/)을 보세요.

```
marsdawn theme validate theme.json --require-complete --json
marsdawn theme css theme.json --json
marsdawn theme preview theme.json --appearance light -o light.png
marsdawn theme preview theme.json --appearance dark -o dark.png
```

- 종료 코드: 0은 유효, 1은 규칙 ID와 함께 무효, 2는 파일 없음, 64는 사용법 오류입니다. `preview`에는 PNG가 이미 있을 때의 4(`--force`를 주거나 다른 이름을 고르세요)와 렌더링 실패의 5가 더해집니다.
- `--json`을 주면 무효한 테마는 `issues` 아래에 문제를 나열하며, 각각 `rule` ID, `path`, `message`가 있습니다. 고친 뒤 다시 실행하세요.
- `--require-complete`는 게시할 테마를 위한 검사입니다. 두 팔레트 모두에 `syntax`와 `diagram` 색도 요구합니다.
- `css`는 미리보기가 쓰는 CSS를 출력하고, `preview`는 예시 문서를 PNG로 렌더링합니다. 둘 다 먼저 검증하므로 무효한 테마는 렌더링되지 않습니다.
- 테마를 건네기 전에 라이트와 다크 PNG를 둘 다 확인하세요.

## 기본 제공 테마에서 시작하기

기본 제공 테마 네 가지 중 하나를 복사해 고치세요. 모두 완전하고 유효한 파일입니다.

- [`/assets/theme-sim/kit/themes/dawn.json`](/assets/theme-sim/kit/themes/dawn.json): 기본값이며 아래 예시
- [`/assets/theme-sim/kit/themes/classic.json`](/assets/theme-sim/kit/themes/classic.json): 더 차분한 문서 같은 팔레트
- [`/assets/theme-sim/kit/themes/modern.json`](/assets/theme-sim/kit/themes/modern.json): 더 차갑고 현대적인 팔레트
- [`/assets/theme-sim/kit/themes/vivid.json`](/assets/theme-sim/kit/themes/vivid.json): 더 밝고 대비가 큰 팔레트

### 예시: Dawn

`dawn.json`을 한 바이트도 바꾸지 않고 옮긴 것입니다. 스타일 옵션은 `hr`의 얇은 강조색 선 하나뿐입니다.

```
{
  "schemaVersion": 1,
  "id": "dawn",
  "version": "1.0.0",
  "name": { "en": "Dawn" },
  "summary": { "en": "Warm Martian sunrise" },
  "fontDesign": "sans",
  "scenarios": ["agent-review"],
  "light": {
    "background": "#FFFDFB", "surface": "#F6F0EC", "text": "#26211F", "muted": "#6F6660",
    "border": "#EADFD8", "heading": "#26211F", "accent": "#C8471B", "link": "#B03C0C", "quote": "#D97A4A",
    "syntax": { "keyword": "#B03C0C", "string": "#2F6F5E", "comment": "#746B66", "number": "#9A5B00", "function": "#5B3E8C", "type": "#1F6FB2" },
    "diagram": { "node": "#FBE9E0", "nodeBorder": "#CA6C3C", "text": "#26211F", "line": "#8A6A5C", "secondary": "#E6F1EE", "tertiary": "#FFF6F1", "note": "#FFF1D6" }
  },
  "dark": {
    "background": "#1C1A1F", "surface": "#262229", "text": "#EBE4DF", "muted": "#A39992",
    "border": "#3A343A", "heading": "#F4EEEA", "accent": "#FF8A50", "link": "#FF9E6B", "quote": "#E08A5C",
    "syntax": { "keyword": "#FF9E6B", "string": "#7FD1B9", "comment": "#938A84", "number": "#F2C572", "function": "#C7A6F5", "type": "#6CB6FF" },
    "diagram": { "node": "#3A2A26", "nodeBorder": "#E08A5C", "text": "#EBE4DF", "line": "#B8A69C", "secondary": "#23332F", "tertiary": "#2B2427", "note": "#3D3322" }
  },
  "style": {
    "hr": { "style": { "type": "line", "color": "accent", "thickness": 1 } }
  }
}
```

## 필드

아래의 모든 객체는 같은 방식으로 읽힙니다. `required`는 키가 반드시 있어야 한다는 뜻이며, 나열되지 않은 키는 오류입니다.

타입: `string`, `integer`, `number`, `boolean`, `map`(언어 태그에서 텍스트로), `enum`(나열된 값 중 하나), `role`(팔레트 역할), `object`(연결된 표). 타입 뒤의 `[]`는 목록을 뜻합니다.

### `theme.json`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `schemaVersion` | `integer` | `required` | 항상 `1`. |
| `id` | `string` | `required` | 1자에서 32자: 소문자와 숫자가 하이픈 하나로 이어진 덩어리, 예: `calm-green`. |
| `version` | `string` | `required` | `MAJOR.MINOR.PATCH`, 예: `1.0.0`. |
| `name` | `map` | `required` | 언어 태그에서 텍스트로. `en`은 필수이며, 다른 키는 `zh-Hant` 같은 언어 태그입니다. 각 텍스트는 최대 48자이며 링크와 줄바꿈을 넣을 수 없습니다. |
| `summary` | `map` | `required` | `name`과 같은 형식이며 텍스트당 최대 120자. |
| `fontDesign` | `enum` | `required` | `sans`, `serif`, `rounded` |
| `scenarios` | `enum[]` | `required` | `agent-review`, `technical-docs`, `formal-output`, `notes-sharing` — 하나 또는 둘, 중복 불가. 테마가 달성해야 하는 대비 수준을 정합니다. |
| `author` | `object` | `optional` | [`author`](#t-author) |
| `license` | `string` | `optional` | SPDX 식별자, 예: `Apache-2.0`. 제출된 테마는 Apache-2.0으로 게시됩니다. |
| `light` | `object` | `required` | [`light, dark`](#t-palette) |
| `dark` | `object` | `required` | [`light, dark`](#t-palette) |
| `style` | `object` | `optional` | [`style`](#t-style) |

### `author`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `name` | `string` | `required` | 최대 64자, 링크 불가. |
| `github` | `string` | `optional` | GitHub 로그인. 제출할 때는 제출하는 사람의 것을 넣으세요. |

### `light, dark`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `background` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `surface` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `text` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `muted` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `border` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `heading` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `accent` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `link` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `quote` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `syntax` | `object` | `optional` (게시하려면 필수, `--require-complete`로 검사) | [`syntax`](#t-syntax-colors) |
| `diagram` | `object` | `optional` (게시하려면 필수, `--require-complete`로 검사) | [`diagram`](#t-diagram-colors) |

### `syntax`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `keyword` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `string` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `comment` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `number` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `function` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `type` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |

### `diagram`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `node` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `nodeBorder` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `text` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `line` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `secondary` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `tertiary` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |
| `note` | `string` | `required` | `#`과 16진수 여섯 자리, 예: `#1C1C1C`. |

### `style`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `bodySize` | `number` | `optional` | [범위](#t-numbers) |
| `lineHeight` | `number` | `optional` | [범위](#t-numbers) |
| `headingWeight` | `number` | `optional` | [범위](#t-numbers) |
| `radius` | `number` | `optional` | [범위](#t-numbers) |
| `maxWidth` | `number` | `optional` | [범위](#t-numbers) |
| `h1` | `object` | `optional` | [`style.h1`](#t-style-h1) |
| `h2` | `object` | `optional` | [`style.h2`](#t-style-h2) |
| `blockquote` | `object` | `optional` | [`style.blockquote`](#t-style-blockquote) |
| `hr` | `object` | `optional` | [`style.hr`](#t-style-hr) |
| `table` | `object` | `optional` | [`style.table`](#t-style-table) |
| `listMarker` | `role` | `optional` | [팔레트 역할](#roles) |
| `inlineCode` | `role` | `optional` | [팔레트 역할](#roles) — `text` 또는 구문 역할만 가능: `keyword`, `string`, `comment`, `number`, `function`, `type`. |
| `link` | `object` | `optional` | [`style.link`](#t-style-link) |
| `syntax` | `object` | `optional` | [`style.syntax`](#t-style-syntax) |

### `style.h1`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `size` | `number` | `optional` | [범위](#t-numbers) |
| `letterSpacing` | `number` | `optional` | [범위](#t-numbers) |
| `align` | `enum` | `optional` | `left`, `center` |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |

### `style.h2`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `letterSpacing` | `number` | `optional` | [범위](#t-numbers) |
| `decoration` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.blockquote`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |
| `italic` | `boolean` | `optional` | `true`, `false` |

### `style.hr`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `style` | `object` | `optional` | [`type`](#t-kinds) |

### `style.table`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `header` | `object` | `optional` | [`type`](#t-kinds) |
| `verticalRules` | `boolean` | `optional` | `true`, `false` |
| `rounded` | `boolean` | `optional` | `true`, `false` |

### `style.link`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `underline` | `boolean` | `optional` | `true`, `false` |

### `style.syntax`

| 필드 | 타입 | 필수 여부 | 값과 참고 |
|---|---|---|---|
| `boldKeywords` | `boolean` | `optional` | `true`, `false` |

### type이 있는 옵션

이 스타일 옵션은 `type`이 있는 객체입니다. 각 `type`은 그것에 나열된 필드만 받고 다른 필드는 받지 않습니다.

| 옵션 | type | 필드 | 필수 여부 | 타입 |
|---|---|---|---|---|
| `style.h1.decoration` | `rule` | — | — | — |
| `style.h1.decoration` | `none` | — | — | — |
| `style.h1.decoration` | `shortRule` | `color` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `from` | `required` | `role` |
| `style.h1.decoration` | `gradientBar` | `to` | `required` | `role` |
| `style.h2.decoration` | `rule` | — | — | — |
| `style.h2.decoration` | `none` | — | — | — |
| `style.h2.decoration` | `dot` | `color` | `required` | `role` |
| `style.blockquote.style` | `bar` | `width` | `optional` | `number` [범위](#t-numbers) |
| `style.blockquote.style` | `panel` | — | — | — |
| `style.hr.style` | `line` | `color` | `optional` | `role` |
| `style.hr.style` | `line` | `thickness` | `optional` | `number` [범위](#t-numbers) |
| `style.hr.style` | `shortCentered` | `color` | `required` | `role` |
| `style.hr.style` | `gradient` | `colors` | `required` | `role[]` 역할 둘 또는 셋. |
| `style.table.header` | `surface` | — | — | — |
| `style.table.header` | `accentRule` | `color` | `required` | `role` |
| `style.table.header` | `filled` | `background` | `required` | `role` |
| `style.table.header` | `filled` | `text` | `required` | `role` |
| `style.table.header` | `filled` | `border` | `optional` | `role` |

### 팔레트 역할

팔레트 역할은 다음 이름 중 하나입니다.

`background`, `surface`, `text`, `muted`, `border`, `heading`, `accent`, `link`, `quote`, `keyword`, `string`, `comment`, `number`, `function`, `type`

### 숫자

숫자는 가장 가까운 간격의 배수로 맞춰진 뒤 최소와 최대 사이에 있어야 합니다. 그렇지 않으면 규칙은 `number.range`입니다.

| 필드 | 최소 | 최대 | 간격 |
|---|---|---|---|
| `style.bodySize` | `14` | `18` | `1` |
| `style.lineHeight` | `1.4` | `1.9` | `0.05` |
| `style.headingWeight` | `400` | `900` | `50` |
| `style.radius` | `0` | `16` | `1` |
| `style.maxWidth` | `600` | `1000` | `1` |
| `style.h1.size` | `1.8` | `2.4` | `0.1` |
| `style.h1.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.h2.letterSpacing` | `-0.03` | `0.03` | `0.005` |
| `style.blockquote.style.width` | `2` | `4` | `1` |
| `style.hr.style.thickness` | `1` | `4` | `1` |

## 그 밖에 검사하는 것

- **대비.** `background` 위의 `text`처럼 미리보기가 그리는 모든 색 쌍은 텍스트는 4.5:1, 선과 그 밖의 비텍스트는 3:1을 만족해야 합니다. 지정한 시나리오는 일부 색을 4.5:1로 올립니다. 메시지에는 해당 쌍과 그 비율, 필요한 비율이 나옵니다.
- **문자열.** 이름, 요약, 작성자 이름이 비어 있거나 너무 길거나, 링크, 제어 문자, 보이지 않는 문자 또는 양방향 서식 문자를 포함하면 거부됩니다.
- **규칙 ID.** 모든 문제에는 `contrast.pair`, `color.hex`, `number.range`, `id.pattern`, `schema.unknownKey`, `palette.incomplete` 같은 ID가 붙습니다. ID와 `path`가 가리키는 대로 파일을 고치세요.

## 링크로 건네기

[테마 만들기](/ko/themes/new/) 페이지는 링크로 테마를 열어 사람이 눈으로 다듬을 수 있게 합니다. 링크는 그 페이지의 주소, `#theme=`, 그리고 패딩 없는 base64url로 인코딩한 파일 바이트로 이루어집니다. 파일은 최대 16,384바이트입니다. 이 한 줄이 macOS와 Linux의 zsh와 bash에서 링크를 만들어 줍니다.

```
printf 'https://marsdawn.southern-light.dev/ko/themes/new/#theme=%s\n' "$(base64 < theme.json | tr -d '\n=' | tr '+/' '-_')"
```

테마는 브라우저가 사이트로 보내지 않는 `#` 뒤에 담기며, 사이트는 이를 어디에도 보내지 않습니다. 다만 링크는 셸과 브라우저의 기록에 남고, 링크를 받은 사람은 누구나 테마를 읽을 수 있습니다.

## 제출하기

에이전트는 파일과 링크를 준비하고, 제출은 사람이 합니다. 두 방법 모두 Developer Certificate of Origin과 Apache-2.0 게시에 대한 확인이 필요하며, 이 확인은 사람이 직접 합니다. 에이전트가 상자에 체크하거나 대신 서명하지 않습니다.

- **이슈.** 사람이 링크를 열어 “테마 만들기” 페이지에서 **Submit**을 누르거나, [이슈 양식](https://github.com/redtear1115/mars-dawn-website/issues/new?template=theme-submission.yml)을 열어 JSON을 *Theme*에 붙여 넣습니다. 워크플로가 테마를 검사하고 답합니다.
- **풀 리퀘스트.** `themes/<id>/theme.json`만 바꾸고, `author.github`를 풀 리퀘스트 작성자의 로그인으로 설정하고, 모든 커밋을 `git commit -s`로 서명하세요. 규칙은 [CONTRIBUTING.md](https://github.com/redtear1115/mars-dawn-website/blob/main/CONTRIBUTING.md)에 있습니다.

제출된 테마의 작성자 이름, 이름, 요약, GitHub 로그인은 영구적으로 공개됩니다. `author.name`에는 그 사람이 공개해도 좋다고 한 이름을 넣으세요.

## 게시된 테마

게시된 테마가 어떻게 생겼는지는 [테마 갤러리](/ko/themes/gallery/)에서 볼 수 있습니다.

## 더 보기

- [MarsDawn](https://marsdawn.southern-light.dev/ko/index.md): 에이전트가 쓴 Markdown을 읽고 검토하는 Mac 네이티브 앱. 분할 실시간 미리보기, Mermaid, KaTeX, 훑어보기, PDF 내보내기. 무료로 체험하고, 잠금 해제는 한 번 USD 4.99.
- [기능 한눈에 보기](https://marsdawn.southern-light.dev/ko/features/index.md): Mac 네이티브 Markdown 편집기: 실시간 미리보기, Mermaid와 수식, 테마, 그리고 회의와 여백 메모, 종이 기록에 쓸 수 있는 깔끔한 PDF와 프린트 페이지.
- [내 글은 내 Mac에](https://marsdawn.southern-light.dev/ko/yours/index.md): MarsDawn에는 계정도, 동기화도, 클라우드도 없습니다. Markdown 문서는 직접 고른 파일과 폴더에 담겨 Mac에 남습니다.
- [무료로 체험하고, 한 번만 구입](https://marsdawn.southern-light.dev/ko/pay-once/index.md): MarsDawn은 무료로 다운로드할 수 있습니다. 14일 동안 모든 기능을 체험한 뒤 USD 4.99에 한 번만 잠금 해제하세요. 구독도, 계정도 없습니다.
- [PDF 내보내기](https://marsdawn.southern-light.dev/ko/pdf/index.md): Mac에서 Markdown을 PDF로 내보내거나 프린트하세요. Mermaid 다이어그램과 하이라이트된 코드도 그대로입니다. 페이지 나눔은 짧은 코드 블록을 가르지 않도록 합니다.
- [Mac 앱](https://marsdawn.southern-light.dev/ko/native/index.md): 진짜 Mac 앱인 Markdown 편집기. 네이티브 윈도우와 탭, 자동 저장, 버전 기록, Finder의 훑어보기, 그리고 Mac답게 동작하는 텍스트 편집기를 갖췄습니다.
- [MarsDawn이 하지 않는 일](https://marsdawn.southern-light.dev/ko/limits/index.md): 동기화도, iPhone이나 iPad 앱도, 플러그인도, 계정도 없습니다. 기본 테마는 네 가지이고, 갤러리에 더 있습니다. 구입 전에 알아 두세요.
- [지원](https://marsdawn.southern-light.dev/ko/support/index.md): macOS용 Markdown 편집기 MarsDawn에 관한 도움말입니다.
- [개인정보 처리방침](https://marsdawn.southern-light.dev/ko/privacy/index.md): MarsDawn은 개인정보를 수집하지 않습니다. 문서와 설정은 사용자의 Mac에 남습니다.
- [Mac에서 .md 파일 여는 방법](https://marsdawn.southern-light.dev/ko/view-markdown-on-mac/index.md): Mac에서 .md 파일을 여는 방법: 더블 클릭, 기본 앱 지정, Finder 훑어보기. AI 에이전트가 쓴 .md 파일은 MarsDawn에서 렌더링된 모습으로 읽으세요.
- [Mac에서 Mermaid 미리보기](https://marsdawn.southern-light.dev/ko/mermaid-preview-mac/index.md): Mac에서 Mermaid 다이어그램을 Markdown 옆에 그려서 보세요: 실시간 미리보기, 훑어보기, PDF 내보내기. 다이어그램에 오류가 있으면 오류와 해당 줄이 표시됩니다.
- [Markdown 훑어보기](https://marsdawn.southern-light.dev/ko/quicklook/index.md): MarsDawn의 훑어보기로 Finder에서 스페이스 바를 누르면 Markdown이 렌더링되어 보입니다. Mermaid, KaTeX, 강조된 코드도 표시됩니다. 체험이 끝난 뒤에도 계속 작동합니다.
- [Markdown을 PDF로](https://marsdawn.southern-light.dev/ko/markdown-to-pdf/index.md): 무료 marsdawn 명령줄 도구로 Mac에서 Markdown을 PDF로 변환하세요. Homebrew로 설치하고 명령 하나만 실행하면 됩니다. 표, 수식, Mermaid, 코드까지 지원합니다.
- [MarsDawn 비교: VS Code 미리보기, Obsidian, QLMarkdown, LynxOffice](https://marsdawn.southern-light.dev/ko/vs/index.md): Mac에서 Markdown을, 대개는 에이전트가 쓴 글을 읽고 검토할 방법을 고르는 분을 위한 페이지입니다. 아래 표의 각 칸은 각 회사의 공식 페이지나 저희가 직접 확인한 내용이며, 모두 2026년 10월 16일 기준입니다. 제품은 바뀌므로 내용이 오래될 수 있습니다. 틀린 내용을 발견하면 지원 페이지의 주소로 알려 주세요.
- [MacMD Viewer와 MarsDawn 비교](https://marsdawn.southern-light.dev/ko/vs/macmd-viewer/index.md): MacMD Viewer는 읽기 전용 Markdown 뷰어로 USD 19.99입니다. MarsDawn은 편집과 미리보기를 나란히 보여 주며, 14일 무료 체험 후 USD 4.99를 한 번만 내면 됩니다. 항목별 비교, 출처 포함.
- [Mac용 Markdown 뷰어 추천 (2026)](https://marsdawn.southern-light.dev/ko/best-markdown-viewer-mac/index.md): Mac용 Markdown 뷰어 8종을 가격, Mermaid, 수식, PDF, 자동 새로 고침, 훑어보기, 네이티브/Electron으로 비교하고 각각 누구에게 맞는지 정리했습니다.
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
- [변경 내역](https://marsdawn.southern-light.dev/ko/changelog/index.md): MarsDawn 앱과 무료 marsdawn 명령줄 도구의 버전별 변경 사항입니다.
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
- [English](https://marsdawn.southern-light.dev/themes/agents/index.md): MarsDawn theme reference for AI agents: each theme.json field with type and range, the CLI loop that checks and renders it, a hand-off link, and how to submit.
- [繁體中文](https://marsdawn.southern-light.dev/zh-hant/themes/agents/index.md): 給 AI agent 的 MarsDawn 主題製作參考：theme.json 每個欄位的型別與範圍、檢查並渲染的 CLI 流程、交給人的連結，以及怎麼投稿。
- [简体中文](https://marsdawn.southern-light.dev/zh-hans/themes/agents/index.md): 给 AI 代理的 MarsDawn 主题制作参考：theme.json 每个字段的类型与范围、检查并渲染的 CLI 流程、交给人的链接，以及怎么投稿。
- [日本語](https://marsdawn.southern-light.dev/ja/themes/agents/index.md): MarsDawn のテーマを作る AI エージェント向けの参考資料。theme.json の全フィールドの型と範囲、検証とレンダリングの CLI 手順、人に渡すリンク、投稿の方法。
- [Deutsch](https://marsdawn.southern-light.dev/de/themes/agents/index.md): MarsDawn-Themen-Referenz für KI-Agenten: jedes Feld der theme.json mit Typ und Bereich, Prüfen und Rendern per CLI, ein Übergabe-Link und die Einreichung.
- [Français](https://marsdawn.southern-light.dev/fr/themes/agents/index.md): Référence des thèmes MarsDawn pour agents IA : chaque champ de theme.json avec type et plage, vérification et rendu en CLI, lien à transmettre, soumission.
- [Español](https://marsdawn.southern-light.dev/es/themes/agents/index.md): Referencia de temas de MarsDawn para agentes de IA: cada campo de theme.json con tipo y rango, comprobación y renderizado por CLI, enlace de entrega y envío.
