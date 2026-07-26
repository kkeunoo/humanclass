---
title: CSS 텍스트와 폰트
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS 텍스트와 폰트

## 개요

CSS에서는 HTML 문서의 글꼴, 크기, 굵기, 줄 간격, 정렬, 장식, 줄바꿈 등을 제어할 수 있다.

```css
.article {
    color: #1f2937;
    font-family: Arial, sans-serif;
    font-size: 1rem;
    line-height: 1.7;
}
```

텍스트 스타일은 단순히 글자를 꾸미는 역할만 하지 않는다.

적절한 텍스트 스타일은 다음 요소에 직접적인 영향을 준다.

- 가독성
- 정보의 중요도 표현
- 콘텐츠 구조
- 브랜드 이미지
- 반응형 디자인
- 웹 접근성
- 사용자 경험

---

# 핵심 개념

CSS 텍스트와 폰트에서 이해해야 하는 주요 개념은 다음과 같다.

- `font-family`
- `font-size`
- `font-weight`
- `font-style`
- `line-height`
- `letter-spacing`
- `word-spacing`
- `text-align`
- `text-decoration`
- `text-transform`
- `text-indent`
- `text-shadow`
- `white-space`
- `overflow-wrap`
- `word-break`
- `text-overflow`
- 웹 폰트
- `@font-face`

---

# 폰트와 텍스트 속성

폰트 관련 속성은 글자 자체의 모양을 제어한다.

```css
.title {
    font-family: Arial, sans-serif;
    font-size: 2rem;
    font-weight: 700;
}
```

텍스트 관련 속성은 글자의 정렬, 장식, 줄바꿈 등을 제어한다.

```css
.description {
    text-align: center;
    text-decoration: none;
    white-space: normal;
}
```

---

# font-family

`font-family`는 요소에 적용할 글꼴을 지정한다.

```css
body {
    font-family: Arial;
}
```

여러 글꼴을 순서대로 지정할 수 있다.

```css
body {
    font-family: Arial, Helvetica, sans-serif;
}
```

브라우저는 왼쪽부터 글꼴을 확인하고, 사용할 수 있는 첫 번째 글꼴을 적용한다.

```text
Arial 확인

↓

없으면 Helvetica 확인

↓

없으면 시스템의 sans-serif 글꼴 사용
```

---

# 폰트 스택

여러 대체 글꼴을 순서대로 작성한 것을 폰트 스택(Font Stack)이라고 한다.

```css
body {
    font-family:
        "Noto Sans KR",
        "Apple SD Gothic Neo",
        "Malgun Gothic",
        Arial,
        sans-serif;
}
```

글꼴 이름에 공백이 포함되어 있다면 따옴표로 감싸는 것이 좋다.

```css
font-family: "Noto Sans KR", sans-serif;
```

---

# 범용 글꼴 계열

마지막에는 일반적으로 범용 글꼴 계열을 작성한다.

| 값 | 설명 |
|---|---|
| `serif` | 글자 끝에 장식이 있는 글꼴 |
| `sans-serif` | 장식이 없는 글꼴 |
| `monospace` | 모든 글자의 너비가 같은 글꼴 |
| `cursive` | 손글씨 형태 |
| `fantasy` | 장식적인 글꼴 |
| `system-ui` | 운영체제 기본 UI 글꼴 |

예제

```css
body {
    font-family: system-ui, sans-serif;
}
```

```css
code {
    font-family: Consolas, Monaco, monospace;
}
```

---

# serif와 sans-serif

## serif

글자 끝에 작은 장식이 있는 글꼴이다.

```css
.article {
    font-family: Georgia, serif;
}
```

긴 본문이나 인쇄물에서 사용되는 경우가 많다.

## sans-serif

글자 끝의 장식이 없는 글꼴이다.

```css
body {
    font-family: Arial, sans-serif;
}
```

웹과 모바일 UI에서 널리 사용된다.

---

# font-size

`font-size`는 글자의 크기를 지정한다.

```css
p {
    font-size: 16px;
}
```

상대 단위를 사용할 수 있다.

```css
p {
    font-size: 1rem;
}
```

```css
.hero-title {
    font-size: clamp(2.5rem, 8vw, 5rem);
}
```

실무에서는 글자 크기에 `rem`을 많이 사용한다.

---

# 기본 글자 크기

일반적인 브라우저의 기본 글자 크기는 `16px`이다.

```text
1rem = 16px
```

기본 설정을 변경하지 않았다면 다음과 같다.

| 값 | 계산 크기 |
|---|---:|
| `0.75rem` | 12px |
| `0.875rem` | 14px |
| `1rem` | 16px |
| `1.125rem` | 18px |
| `1.25rem` | 20px |
| `1.5rem` | 24px |
| `2rem` | 32px |

사용자의 브라우저 설정에 따라 실제 크기는 달라질 수 있다.

---

# 반응형 글자 크기

`clamp()`를 사용하면 글자 크기에 최소값과 최대값을 지정할 수 있다.

```css
.hero-title {
    font-size: clamp(2rem, 6vw, 5rem);
}
```

```text
최소 2rem

↓

화면 크기에 따라 6vw

↓

최대 5rem
```

화면 크기가 변해도 글자가 지나치게 작거나 커지는 것을 방지할 수 있다.

---

# font-weight

`font-weight`는 글자의 굵기를 지정한다.

```css
.title {
    font-weight: bold;
}
```

숫자로도 작성할 수 있다.

```css
.title {
    font-weight: 700;
}
```

대표적인 값은 다음과 같다.

| 값 | 의미 |
|---:|---|
| `100` | 매우 얇음 |
| `200` | 얇음 |
| `300` | Light |
| `400` | Normal |
| `500` | Medium |
| `600` | Semi Bold |
| `700` | Bold |
| `800` | Extra Bold |
| `900` | 매우 굵음 |

---

# normal과 bold

```css
p {
    font-weight: normal;
}
```

`normal`은 일반적으로 `400`에 해당한다.

```css
strong {
    font-weight: bold;
}
```

`bold`는 일반적으로 `700`에 해당한다.

---

# 폰트가 굵기를 지원하지 않는 경우

모든 폰트가 `100`부터 `900`까지 모든 굵기를 지원하는 것은 아니다.

예를 들어 폰트가 `400`과 `700`만 제공한다면 다음 값은 가장 가까운 굵기로 표현될 수 있다.

```css
.title {
    font-weight: 600;
}
```

웹 폰트를 불러올 때 실제로 사용할 굵기를 함께 제공해야 한다.

---

# font-style

`font-style`은 글자의 기울임 스타일을 지정한다.

```css
em {
    font-style: italic;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `normal` | 기본 형태 |
| `italic` | 이탤릭체 |
| `oblique` | 글자를 기울여 표시 |

예제

```css
.quote {
    font-style: italic;
}
```

---

# italic과 oblique

`italic`은 폰트에 별도로 설계된 이탤릭 글꼴을 사용한다.

`oblique`는 일반 글꼴을 기울여 표현하는 방식이다.

실제 결과는 사용하는 폰트에 따라 다를 수 있다.

---

# font-variant

`font-variant`는 글자의 변형 표현을 지정한다.

```css
.abbreviation {
    font-variant: small-caps;
}
```

`small-caps`는 소문자를 작은 대문자 형태로 표현한다.

한국어 중심의 일반 웹 프로젝트에서는 사용 빈도가 높지 않다.

---

# font 속기 속성

여러 폰트 속성을 한 번에 작성할 수 있다.

```css
.title {
    font: italic 700 2rem/1.4 Arial, sans-serif;
}
```

구조

```text
font-style
font-weight
font-size / line-height
font-family
```

`font-size`와 `font-family`는 반드시 포함해야 한다.

가독성과 유지보수를 위해 속성을 나누어 작성하는 경우도 많다.

```css
.title {
    font-family: Arial, sans-serif;
    font-size: 2rem;
    font-style: italic;
    font-weight: 700;
    line-height: 1.4;
}
```

---

# line-height

`line-height`는 텍스트 한 줄의 높이를 지정한다.

```css
p {
    line-height: 1.6;
}
```

단위 없는 숫자로 작성하면 현재 요소의 글자 크기를 기준으로 계산한다.

```text
font-size: 16px
line-height: 1.6

16px × 1.6
= 25.6px
```

---

# line-height 사용 기준

본문에서는 일반적으로 `1.5`에서 `1.8` 정도를 자주 사용한다.

```css
body {
    line-height: 1.6;
}
```

제목은 본문보다 줄 간격을 좁게 설정하는 경우가 많다.

```css
h1 {
    line-height: 1.15;
}
```

```css
p {
    line-height: 1.7;
}
```

절대적인 규칙은 아니며 글꼴과 글자 크기에 따라 조정해야 한다.

---

# 단위 없는 line-height

다음처럼 단위 없는 값을 사용하는 것이 권장되는 경우가 많다.

```css
body {
    line-height: 1.6;
}
```

부모의 `line-height`가 자식에게 상속되어도 자식 요소 자신의 글자 크기를 기준으로 다시 계산된다.

```css
body {
    font-size: 16px;
    line-height: 1.6;
}

h1 {
    font-size: 40px;
}
```

`h1`의 줄 높이는 자신의 `40px`을 기준으로 계산된다.

---

# letter-spacing

`letter-spacing`은 글자 사이의 간격을 지정한다.

```css
.title {
    letter-spacing: 0.05em;
}
```

간격을 줄일 수도 있다.

```css
.hero-title {
    letter-spacing: -0.03em;
}
```

제목의 큰 글자는 글자 사이가 넓어 보일 수 있어 음수 값을 사용하는 경우가 있다.

---

# letter-spacing 사용 시 주의점

본문의 자간을 지나치게 줄이면 가독성이 떨어질 수 있다.

좋지 않은 예

```css
p {
    letter-spacing: -0.1em;
}
```

대문자로 구성된 짧은 레이블에는 자간을 넓히는 경우가 많다.

```css
.badge {
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
```

---

# word-spacing

`word-spacing`은 단어 사이의 간격을 지정한다.

```css
p {
    word-spacing: 0.2em;
}
```

한국어 문서에서는 영어 문서보다 사용 효과가 제한적일 수 있다.

---

# text-align

`text-align`은 인라인 콘텐츠의 수평 정렬을 지정한다.

```css
.title {
    text-align: center;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `left` | 왼쪽 정렬 |
| `right` | 오른쪽 정렬 |
| `center` | 가운데 정렬 |
| `justify` | 양쪽 정렬 |
| `start` | 글쓰기 방향의 시작점 |
| `end` | 글쓰기 방향의 끝점 |

---

# start와 end

`start`와 `end`는 문서의 글쓰기 방향을 반영한다.

```css
.article {
    text-align: start;
}
```

왼쪽에서 오른쪽으로 쓰는 문서에서는 `start`가 왼쪽처럼 동작한다.

오른쪽에서 왼쪽으로 쓰는 문서에서는 반대로 동작할 수 있다.

다국어 웹에서는 `left`, `right`보다 논리적 값인 `start`, `end`가 유용하다.

---

# text-align의 적용 대상

`text-align`은 블록 요소 자체를 이동시키는 속성이 아니다.

```css
.container {
    text-align: center;
}
```

부모 안의 텍스트나 인라인 요소가 가운데 정렬된다.

블록 요소 자체를 가운데 정렬하려면 다음과 같은 방법을 사용한다.

```css
.card {
    width: 400px;
    margin-inline: auto;
}
```

---

# justify

양쪽 정렬은 텍스트의 양쪽 끝을 맞춘다.

```css
.article {
    text-align: justify;
}
```

단어 사이 간격이 지나치게 벌어질 수 있어 짧은 영역이나 모바일 화면에서는 주의해야 한다.

---

# vertical-align

`vertical-align`은 인라인 요소나 테이블 셀의 세로 정렬에 사용한다.

```css
.icon {
    vertical-align: middle;
}
```

```css
td {
    vertical-align: top;
}
```

일반 블록 레이아웃의 세로 중앙 정렬을 위한 속성은 아니다.

블록 요소의 정렬에는 Flexbox나 Grid를 사용하는 것이 일반적이다.

---

# text-decoration

`text-decoration`은 텍스트에 밑줄, 윗줄, 취소선 등을 적용한다.

```css
a {
    text-decoration: none;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `none` | 장식 제거 |
| `underline` | 밑줄 |
| `overline` | 윗줄 |
| `line-through` | 취소선 |

---

# 링크 밑줄

```css
a {
    color: royalblue;
    text-decoration: underline;
}
```

링크 밑줄을 제거할 수 있다.

```css
a {
    text-decoration: none;
}
```

다만 링크가 일반 텍스트와 구분되지 않으면 접근성이 떨어질 수 있다.

```css
a {
    color: royalblue;
    text-decoration: underline;
}

a:hover {
    text-decoration-thickness: 2px;
}
```

---

# text-decoration 세부 속성

텍스트 장식을 세부적으로 제어할 수 있다.

```css
a {
    text-decoration-line: underline;
    text-decoration-color: currentColor;
    text-decoration-style: solid;
    text-decoration-thickness: 2px;
    text-underline-offset: 0.2em;
}
```

| 속성 | 설명 |
|---|---|
| `text-decoration-line` | 장식 종류 |
| `text-decoration-color` | 장식 색상 |
| `text-decoration-style` | 장식 선의 형태 |
| `text-decoration-thickness` | 장식 선의 두께 |
| `text-underline-offset` | 밑줄과 글자 사이 거리 |

---

# text-transform

`text-transform`은 영문자의 대소문자 표현을 변경한다.

```css
.badge {
    text-transform: uppercase;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `none` | 변경하지 않음 |
| `uppercase` | 대문자로 표시 |
| `lowercase` | 소문자로 표시 |
| `capitalize` | 각 단어의 첫 글자를 대문자로 표시 |

HTML의 실제 텍스트가 변경되는 것은 아니며 화면 표시만 달라진다.

---

# text-indent

`text-indent`는 첫 번째 줄의 들여쓰기를 지정한다.

```css
.article p {
    text-indent: 2em;
}
```

본문 문단의 첫 줄을 들여쓸 때 사용할 수 있다.

UI 중심의 웹 페이지에서는 사용 빈도가 높지 않지만 기사나 전자책 형태의 콘텐츠에서 활용할 수 있다.

---

# text-shadow

`text-shadow`는 글자에 그림자를 적용한다.

```css
.hero-title {
    text-shadow: 0 4px 12px rgb(0 0 0 / 40%);
}
```

구조

```text
가로 위치
세로 위치
흐림 정도
색상
```

```css
.title {
    text-shadow: 2px 2px 4px #000;
}
```

그림자를 여러 개 사용할 수도 있다.

```css
.title {
    text-shadow:
        0 1px 2px rgb(0 0 0 / 40%),
        0 4px 12px rgb(0 0 0 / 20%);
}
```

지나친 그림자는 글자의 가독성을 떨어뜨릴 수 있다.

---

# white-space

`white-space`는 공백과 줄바꿈을 처리하는 방법을 지정한다.

| 값 | 공백 유지 | 줄바꿈 유지 | 자동 줄바꿈 |
|---|---|---|---|
| `normal` | X | X | O |
| `nowrap` | X | X | X |
| `pre` | O | O | X |
| `pre-wrap` | O | O | O |
| `pre-line` | X | O | O |

---

# normal

기본값이다.

```css
p {
    white-space: normal;
}
```

여러 공백은 하나로 합쳐지고 요소 너비에 따라 자동 줄바꿈된다.

---

# nowrap

텍스트를 자동으로 줄바꿈하지 않는다.

```css
.navigation__link {
    white-space: nowrap;
}
```

공간이 부족하면 요소 밖으로 넘칠 수 있다.

말줄임표와 자주 함께 사용한다.

---

# pre

HTML의 공백과 줄바꿈을 그대로 유지한다.

```css
.code {
    white-space: pre;
}
```

자동 줄바꿈은 적용되지 않는다.

---

# pre-wrap

공백과 줄바꿈을 유지하면서 요소 너비에 따라 자동 줄바꿈한다.

```css
.message {
    white-space: pre-wrap;
}
```

사용자가 작성한 여러 줄 텍스트를 표시할 때 유용하다.

---

# pre-line

연속된 공백은 하나로 합치지만 줄바꿈은 유지한다.

```css
.description {
    white-space: pre-line;
}
```

---

# overflow-wrap

`overflow-wrap`은 긴 단어나 URL이 요소를 벗어날 때 줄바꿈할 수 있도록 한다.

```css
.article {
    overflow-wrap: break-word;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `normal` | 일반적인 줄바꿈 규칙 사용 |
| `break-word` | 필요한 경우 긴 단어를 줄바꿈 |
| `anywhere` | 가능한 위치에서 적극적으로 줄바꿈 |

```css
.url {
    overflow-wrap: anywhere;
}
```

긴 URL이나 연속된 문자열이 레이아웃을 깨뜨리는 것을 방지할 수 있다.

---

# word-break

`word-break`는 단어 내부의 줄바꿈 규칙을 지정한다.

```css
.text {
    word-break: keep-all;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `normal` | 기본 줄바꿈 규칙 |
| `break-all` | 글자 단위로 줄바꿈 가능 |
| `keep-all` | 한중일 텍스트의 단어 단위 줄바꿈 유지 |

---

# keep-all

한국어 문장에서 단어 중간이 잘리는 것을 줄이고 싶을 때 사용할 수 있다.

```css
.article-title {
    word-break: keep-all;
}
```

다만 긴 영문 문자열이나 URL이 넘칠 수 있으므로 다음과 같이 함께 사용할 수 있다.

```css
.article-title {
    overflow-wrap: break-word;
    word-break: keep-all;
}
```

---

# break-all

글자 단위로 줄바꿈할 수 있다.

```css
.code-string {
    word-break: break-all;
}
```

일반 본문에 사용하면 단어가 부자연스럽게 잘릴 수 있으므로 주의해야 한다.

---

# text-overflow

`text-overflow`는 넘치는 텍스트를 표시하는 방식을 지정한다.

```css
.title {
    text-overflow: ellipsis;
}
```

`ellipsis`는 넘치는 텍스트를 말줄임표로 표시한다.

단독으로는 동작하지 않으며 일반적으로 다음 속성과 함께 사용한다.

```css
.title {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
```

---

# 한 줄 말줄임표

```css
.card__title {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
```

```text
프론트엔드 개발자를 위한 CSS 학습 과정

↓

프론트엔드 개발자를 위한...
```

요소에 계산 가능한 너비가 있어야 한다.

---

# 여러 줄 말줄임표

여러 줄 뒤에 말줄임표를 표시할 수 있다.

```css
.card__description {
    display: -webkit-box;
    overflow: hidden;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
}
```

세 줄 이후의 텍스트를 숨긴다.

```css
.card__description {
    line-clamp: 3;
}
```

프로젝트의 브라우저 지원 범위를 확인하여 사용한다.

---

# direction

`direction`은 텍스트가 작성되는 방향을 지정한다.

```css
.element {
    direction: rtl;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `ltr` | 왼쪽에서 오른쪽 |
| `rtl` | 오른쪽에서 왼쪽 |

일반적으로 HTML의 `dir` 속성을 사용하는 것이 문서 의미 전달에 더 적절하다.

```html
<p dir="rtl">
    ...
</p>
```

---

# writing-mode

`writing-mode`는 글쓰기 방향을 지정한다.

```css
.vertical-text {
    writing-mode: vertical-rl;
}
```

세로 텍스트나 특수한 디자인에 사용할 수 있다.

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `horizontal-tb` | 가로쓰기 |
| `vertical-rl` | 세로쓰기, 오른쪽에서 왼쪽 |
| `vertical-lr` | 세로쓰기, 왼쪽에서 오른쪽 |

---

# 사용자 선택 제어

`user-select`는 사용자가 텍스트를 드래그하여 선택할 수 있는지를 제어한다.

```css
.button {
    user-select: none;
}
```

버튼이나 드래그 UI에서 텍스트가 불필요하게 선택되는 것을 방지할 수 있다.

본문 텍스트에는 선택을 막지 않는 것이 좋다.

---

# 웹 폰트

사용자의 컴퓨터에 설치되지 않은 글꼴을 웹에서 불러와 사용할 수 있다.

대표적인 방법은 다음과 같다.

- 외부 폰트 서비스 연결
- `@font-face` 사용
- 프로젝트에 폰트 파일 포함

---

# 외부 스타일시트 방식

HTML의 `<link>`로 폰트 스타일시트를 연결할 수 있다.

```html
<link
    rel="preconnect"
    href="https://fonts.googleapis.com"
>

<link
    rel="preconnect"
    href="https://fonts.gstatic.com"
    crossorigin
>

<link
    href="폰트 스타일시트 주소"
    rel="stylesheet"
>
```

CSS

```css
body {
    font-family: "Noto Sans KR", sans-serif;
}
```

외부 서비스 사용 시 네트워크, 개인정보 보호, 서비스 정책, 성능 등을 고려해야 한다.

---

# @font-face

`@font-face`를 사용하면 프로젝트 내부의 폰트 파일을 직접 연결할 수 있다.

```css
@font-face {
    font-family: "Pretendard";
    src: url("./fonts/Pretendard-Regular.woff2") format("woff2");
    font-style: normal;
    font-weight: 400;
    font-display: swap;
}
```

사용 방법

```css
body {
    font-family: "Pretendard", sans-serif;
}
```

---

# 폰트 굵기별 등록

굵기마다 별도의 폰트 파일이 있다면 각각 등록한다.

```css
@font-face {
    font-family: "MyFont";
    src: url("./fonts/MyFont-Regular.woff2") format("woff2");
    font-style: normal;
    font-weight: 400;
    font-display: swap;
}

@font-face {
    font-family: "MyFont";
    src: url("./fonts/MyFont-Bold.woff2") format("woff2");
    font-style: normal;
    font-weight: 700;
    font-display: swap;
}
```

CSS에서는 동일한 글꼴 이름과 필요한 굵기를 지정한다.

```css
body {
    font-family: "MyFont", sans-serif;
}

.title {
    font-weight: 700;
}
```

---

# font-display

`font-display`는 웹 폰트가 로딩되는 동안 텍스트를 어떻게 표시할지 지정한다.

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `auto` | 브라우저 기본 동작 |
| `block` | 일정 시간 텍스트를 숨기고 폰트를 기다림 |
| `swap` | 기본 폰트를 먼저 표시하고 이후 교체 |
| `fallback` | 짧게 기다린 후 대체 폰트 사용 |
| `optional` | 네트워크 상황에 따라 웹 폰트를 사용하지 않을 수 있음 |

일반적인 웹 프로젝트에서는 `swap`을 자주 사용한다.

```css
font-display: swap;
```

---

# 웹 폰트 형식

대표적인 웹 폰트 형식은 다음과 같다.

| 형식 | 설명 |
|---|---|
| `woff2` | 압축률이 높고 현대 브라우저에서 널리 사용 |
| `woff` | 이전 브라우저 호환에 사용 |
| `ttf` | 일반 폰트 형식 |
| `otf` | OpenType 폰트 |

웹에서는 보통 `woff2`를 우선 사용한다.

---

# 가변 폰트

가변 폰트(Variable Font)는 하나의 폰트 파일에 여러 굵기나 형태를 포함할 수 있다.

```css
@font-face {
    font-family: "MyVariableFont";
    src: url("./fonts/MyVariableFont.woff2") format("woff2");
    font-weight: 100 900;
    font-style: normal;
    font-display: swap;
}
```

```css
.title {
    font-family: "MyVariableFont", sans-serif;
    font-weight: 650;
}
```

파일 수를 줄이고 다양한 굵기를 사용할 수 있다는 장점이 있다.

---

# 폰트 로딩과 화면 변화

웹 폰트가 늦게 로딩되면 처음에는 기본 글꼴이 보이다가 웹 폰트로 교체될 수 있다.

글꼴마다 글자 너비와 높이가 다르므로 레이아웃이 움직일 수 있다.

이를 줄이기 위해 다음을 고려한다.

- 필요한 굵기만 불러오기
- `woff2` 사용
- `font-display` 설정
- 비슷한 형태의 대체 글꼴 사용
- 사용하지 않는 글자 범위 제외
- 지나치게 많은 웹 폰트 사용 방지

---

# 폰트 크기와 접근성

본문 글자를 지나치게 작게 작성하면 읽기 어렵다.

좋지 않은 예

```css
body {
    font-size: 10px;
}
```

일반적으로 본문은 브라우저 기본 크기를 존중하는 것이 좋다.

```css
html {
    font-size: 100%;
}

body {
    font-size: 1rem;
}
```

사용자가 브라우저 글자 크기를 조정할 수 있도록 상대 단위를 활용한다.

---

# 텍스트 대비

텍스트와 배경색 사이에는 충분한 대비가 필요하다.

좋지 않은 예

```css
p {
    background-color: white;
    color: #ddd;
}
```

매우 연한 회색은 흰색 배경에서 읽기 어렵다.

```css
p {
    background-color: white;
    color: #374151;
}
```

색상뿐 아니라 크기와 굵기도 가독성에 영향을 준다.

---

# 본문 너비

본문의 한 줄 길이가 지나치게 길면 다음 줄을 찾기 어렵다.

```css
.article {
    max-width: 65ch;
}
```

`ch` 단위를 이용하면 글자 수를 기준으로 대략적인 본문 너비를 제한할 수 있다.

```css
.article p {
    line-height: 1.7;
}
```

본문 너비와 줄 간격을 함께 조절하면 읽기 편한 콘텐츠를 만들 수 있다.

---

# 제목 계층

HTML의 제목 태그 계층과 CSS의 글자 크기는 별개의 개념이다.

```html
<h1 class="page-title">
    페이지 제목
</h1>
```

```css
.page-title {
    font-size: 2.5rem;
}
```

디자인을 위해 제목 태그의 순서를 바꾸면 안 된다.

제목 태그는 문서 구조에 맞게 사용하고 크기는 CSS로 조정한다.

---

# 실무 활용

텍스트와 폰트 속성은 다음 상황에서 사용한다.

- 사이트 기본 글꼴 설정
- 제목과 본문의 위계 표현
- 버튼과 메뉴 텍스트
- 카드 제목 말줄임표
- 게시판 본문 줄바꿈
- 사용자 입력 내용 표시
- 웹 폰트 적용
- 반응형 글자 크기
- 링크 스타일
- 접근성 높은 본문 구성
- 코드와 일반 텍스트 구분
- 다국어 사이트 구성

---

# 실무 예제 프로젝트

## HTML

```html
<!DOCTYPE html>

<html lang="ko">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <link
        rel="stylesheet"
        href="./style.css"
    >

    <title>CSS 텍스트와 폰트</title>

</head>

<body>

    <header class="header">

        <a
            href="#"
            class="header__logo"
        >
            Developer Wiki
        </a>

        <nav aria-label="주요 메뉴">

            <ul class="navigation">

                <li>
                    <a
                        href="#article"
                        class="navigation__link"
                    >
                        Article
                    </a>
                </li>

                <li>
                    <a
                        href="#courses"
                        class="navigation__link"
                    >
                        Courses
                    </a>
                </li>

            </ul>

        </nav>

    </header>

    <main class="main">

        <article
            id="article"
            class="article"
        >

            <span class="article__category">
                CSS Basic
            </span>

            <h1 class="article__title">
                읽기 좋은 웹 문서를 만드는
                CSS 텍스트와 폰트
            </h1>

            <p class="article__summary">
                적절한 글꼴과 줄 간격, 본문 너비는
                콘텐츠의 가독성과 사용자 경험에 큰 영향을 줍니다.
            </p>

            <div class="article__meta">

                <span>
                    작성일 2026-07-22
                </span>

                <span aria-hidden="true">
                    ·
                </span>

                <span>
                    읽는 시간 8분
                </span>

            </div>

            <section class="article__content">

                <h2>
                    가독성 높은 본문
                </h2>

                <p>
                    본문의 글자 크기, 줄 간격, 한 줄의 길이는
                    함께 고려해야 합니다. 한 줄이 지나치게 길거나
                    줄 간격이 너무 좁으면 다음 줄을 찾기 어렵습니다.
                </p>

                <blockquote>
                    좋은 타이포그래피는 사용자가 디자인보다
                    콘텐츠에 집중할 수 있도록 돕습니다.
                </blockquote>

                <h2>
                    긴 문자열 처리
                </h2>

                <p class="article__url">
                    https://example.com/developer-wiki/frontend/css/basic/text-and-font/very-long-address
                </p>

            </section>

        </article>

        <section
            id="courses"
            class="courses"
        >

            <h2 class="courses__title">
                관련 학습 문서
            </h2>

            <article class="course-card">

                <span class="course-card__category">
                    CSS
                </span>

                <h3 class="course-card__title">
                    CSS 선택자와 우선순위를 함께 이해하는 방법
                </h3>

                <p class="course-card__description">
                    선택자와 명시도, 상속의 관계를 학습합니다.
                    실무에서 스타일 충돌을 분석하는 방법도 함께 정리합니다.
                </p>

                <a
                    href="#"
                    class="course-card__link"
                >
                    문서 읽기
                </a>

            </article>

        </section>

    </main>

</body>

</html>
```

## CSS

```css
@font-face {
    font-family: "WikiFont";
    src: url("./fonts/WikiFont-Regular.woff2") format("woff2");
    font-style: normal;
    font-weight: 400;
    font-display: swap;
}

@font-face {
    font-family: "WikiFont";
    src: url("./fonts/WikiFont-Bold.woff2") format("woff2");
    font-style: normal;
    font-weight: 700;
    font-display: swap;
}

:root {
    --color-primary: #2563eb;
    --color-heading: #111827;
    --color-text: #374151;
    --color-muted: #6b7280;
    --color-border: #e5e7eb;
    --color-background: #f8fafc;
    --color-surface: #ffffff;
}

* {
    box-sizing: border-box;
}

html {
    font-size: 100%;
}

body {
    margin: 0;
    background-color: var(--color-background);
    color: var(--color-text);
    font-family:
        "WikiFont",
        "Noto Sans KR",
        system-ui,
        sans-serif;
    font-size: 1rem;
    line-height: 1.7;
    word-break: keep-all;
}

a {
    color: inherit;
}

.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.25rem max(1.25rem, 5vw);
    border-bottom: 1px solid var(--color-border);
    background-color: var(--color-surface);
}

.header__logo {
    color: var(--color-heading);
    font-size: 1.25rem;
    font-weight: 700;
    text-decoration: none;
}

.navigation {
    display: flex;
    gap: 1.5rem;
    margin: 0;
    padding: 0;
    list-style: none;
}

.navigation__link {
    color: var(--color-text);
    font-size: 0.9375rem;
    font-weight: 500;
    text-decoration: none;
}

.navigation__link:hover {
    color: var(--color-primary);
    text-decoration: underline;
    text-underline-offset: 0.25em;
}

.navigation__link:focus-visible {
    outline: 3px solid var(--color-primary);
    outline-offset: 4px;
}

.main {
    width: min(100% - 2rem, 75rem);
    margin-inline: auto;
    padding-block: clamp(3rem, 8vw, 7rem);
}

.article {
    max-width: 68ch;
    margin-inline: auto;
}

.article__category,
.course-card__category {
    color: var(--color-primary);
    font-size: 0.8125rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.article__title {
    margin-block: 1rem;
    color: var(--color-heading);
    font-size: clamp(2.25rem, 6vw, 4.5rem);
    letter-spacing: -0.04em;
    line-height: 1.12;
    text-wrap: balance;
}

.article__summary {
    margin-block: 0 1.5rem;
    color: var(--color-muted);
    font-size: clamp(1.125rem, 2vw, 1.375rem);
    line-height: 1.65;
}

.article__meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--color-border);
    color: var(--color-muted);
    font-size: 0.875rem;
}

.article__content {
    padding-top: 2rem;
}

.article__content h2 {
    margin-block: 3rem 1rem;
    color: var(--color-heading);
    font-size: clamp(1.5rem, 3vw, 2rem);
    line-height: 1.3;
}

.article__content p {
    margin-block: 0 1.5rem;
}

.article__content blockquote {
    margin: 2rem 0;
    padding: 1.5rem;
    border-inline-start: 4px solid var(--color-primary);
    background-color: var(--color-surface);
    color: var(--color-heading);
    font-size: 1.125rem;
    font-style: italic;
    line-height: 1.7;
}

.article__url {
    overflow-wrap: anywhere;
    color: var(--color-primary);
}

.courses {
    margin-top: clamp(5rem, 12vw, 10rem);
}

.courses__title {
    color: var(--color-heading);
    font-size: clamp(1.75rem, 4vw, 2.5rem);
    line-height: 1.3;
}

.course-card {
    max-width: 38rem;
    padding: 2rem;
    border: 1px solid var(--color-border);
    border-radius: 1rem;
    background-color: var(--color-surface);
}

.course-card__title {
    display: -webkit-box;
    overflow: hidden;
    margin-block: 0.75rem;
    color: var(--color-heading);
    font-size: 1.5rem;
    line-height: 1.4;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
}

.course-card__description {
    display: -webkit-box;
    overflow: hidden;
    margin-block: 0 1.5rem;
    color: var(--color-muted);
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
}

.course-card__link {
    color: var(--color-primary);
    font-weight: 700;
    text-decoration-thickness: 2px;
    text-underline-offset: 0.25em;
}
```

---

# 예제 분석

```css
font-family:
    "WikiFont",
    "Noto Sans KR",
    system-ui,
    sans-serif;
```

웹 폰트를 우선 적용하고 사용할 수 없는 경우 대체 글꼴을 순서대로 적용한다.

```css
line-height: 1.7;
```

현재 글자 크기를 기준으로 줄 높이를 계산한다.

```css
word-break: keep-all;
```

한국어 단어가 중간에서 부자연스럽게 줄바꿈되는 것을 줄인다.

```css
font-size: clamp(2.25rem, 6vw, 4.5rem);
```

화면 크기에 따라 제목 크기를 유동적으로 조절한다.

```css
letter-spacing: -0.04em;
```

큰 제목의 글자 사이 간격을 조금 줄인다.

```css
max-width: 68ch;
```

본문 한 줄의 길이가 지나치게 길어지는 것을 방지한다.

```css
overflow-wrap: anywhere;
```

긴 URL이 레이아웃 밖으로 넘치는 것을 방지한다.

```css
-webkit-line-clamp: 2;
```

카드 제목을 최대 두 줄까지만 표시한다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|---|---|
| Font Family | 적용할 글꼴 지정 |
| Font Stack | 대체 글꼴을 순서대로 작성한 목록 |
| Generic Family | 범용 글꼴 계열 |
| Serif | 장식이 있는 글꼴 |
| Sans-serif | 장식이 없는 글꼴 |
| Monospace | 모든 글자 너비가 같은 글꼴 |
| font-size | 글자 크기 |
| font-weight | 글자 굵기 |
| font-style | 글자 기울임 |
| line-height | 한 줄의 높이 |
| letter-spacing | 글자 사이 간격 |
| word-spacing | 단어 사이 간격 |
| text-align | 인라인 콘텐츠 정렬 |
| text-decoration | 밑줄과 취소선 등의 장식 |
| text-transform | 영문 대소문자 표현 변경 |
| text-indent | 첫 줄 들여쓰기 |
| text-shadow | 글자 그림자 |
| white-space | 공백과 줄바꿈 처리 |
| overflow-wrap | 긴 문자열 줄바꿈 |
| word-break | 단어 내부 줄바꿈 규칙 |
| text-overflow | 넘치는 텍스트 표현 |
| ellipsis | 말줄임표 |
| @font-face | 사용자 정의 웹 폰트 등록 |
| font-display | 웹 폰트 로딩 중 표시 방식 |
| Variable Font | 하나의 파일로 여러 굵기를 지원하는 폰트 |

---

# 자주 하는 실수

## 1. font-family에 대체 글꼴을 작성하지 않는다

좋지 않은 예

```css
body {
    font-family: "MyFont";
}
```

권장 예

```css
body {
    font-family: "MyFont", system-ui, sans-serif;
}
```

---

## 2. 공백이 있는 글꼴 이름을 따옴표 없이 작성한다

좋지 않은 예

```css
font-family: Noto Sans KR, sans-serif;
```

권장 예

```css
font-family: "Noto Sans KR", sans-serif;
```

---

## 3. 폰트가 지원하지 않는 굵기를 무조건 사용한다

```css
.title {
    font-weight: 600;
}
```

폰트가 해당 굵기를 제공하는지 확인해야 한다.

---

## 4. 본문의 font-size를 지나치게 작게 설정한다

```css
body {
    font-size: 10px;
}
```

작은 글자는 가독성과 접근성을 떨어뜨린다.

---

## 5. line-height에 너무 작은 값을 사용한다

```css
p {
    line-height: 1;
}
```

본문의 줄이 서로 붙어 읽기 어려워질 수 있다.

---

## 6. line-height를 모든 요소에 고정 px로 지정한다

```css
body {
    line-height: 24px;
}
```

자식 요소의 글자 크기가 달라지면 적절하지 않을 수 있다.

```css
body {
    line-height: 1.6;
}
```

---

## 7. text-align: center로 블록 요소 자체를 가운데 배치하려고 한다

```css
.container {
    text-align: center;
}
```

이 속성은 내부의 인라인 콘텐츠를 정렬한다.

블록 요소 자체를 가운데 배치하려면 다음을 고려한다.

```css
.card {
    margin-inline: auto;
}
```

---

## 8. vertical-align으로 일반 블록을 세로 중앙 정렬하려고 한다

`vertical-align`은 주로 인라인 요소와 테이블 셀에서 사용한다.

일반 레이아웃은 Flexbox나 Grid를 사용한다.

---

## 9. 링크의 밑줄과 색상을 모두 제거한다

```css
a {
    color: inherit;
    text-decoration: none;
}
```

일반 텍스트와 링크를 구분하기 어려워질 수 있다.

---

## 10. white-space: nowrap을 사용하고 넘침 처리를 하지 않는다

```css
.title {
    white-space: nowrap;
}
```

요소 밖으로 텍스트가 넘칠 수 있다.

```css
.title {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
```

---

## 11. text-overflow: ellipsis만 작성한다

```css
.title {
    text-overflow: ellipsis;
}
```

일반적으로 다음 속성도 함께 필요하다.

```css
.title {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
```

---

## 12. word-break: break-all을 모든 본문에 적용한다

```css
body {
    word-break: break-all;
}
```

단어가 부자연스럽게 잘릴 수 있다.

한국어 본문에서는 `keep-all`과 `overflow-wrap`의 조합을 고려한다.

---

## 13. 웹 폰트의 모든 굵기를 불러온다

사용하지 않는 굵기까지 모두 불러오면 파일 용량과 로딩 시간이 증가한다.

실제로 사용하는 굵기만 선택한다.

---

## 14. @font-face의 font-weight를 모두 같은 값으로 작성한다

각 폰트 파일에 맞는 굵기를 지정해야 한다.

```css
font-weight: 400;
```

```css
font-weight: 700;
```

---

## 15. font-display를 고려하지 않는다

웹 폰트가 로딩될 때 텍스트가 보이지 않거나 늦게 표시될 수 있다.

```css
font-display: swap;
```

---

## 16. 제목 태그를 글자 크기 기준으로 선택한다

`h1`, `h2`, `h3`는 문서 구조에 따라 사용한다.

글자 크기는 CSS로 조절한다.

---

## 17. 한 줄의 본문 너비를 지나치게 넓게 만든다

읽는 동안 다음 줄을 찾기 어려워질 수 있다.

```css
.article {
    max-width: 65ch;
}
```

---

## 18. 텍스트 그림자를 지나치게 많이 사용한다

과도한 `text-shadow`는 글자의 경계를 흐리게 하고 가독성을 떨어뜨린다.

---

# 면접 포인트

### Q1. font-family에 여러 글꼴을 작성하는 이유는 무엇인가요?

첫 번째 글꼴을 사용할 수 없는 환경에서 다음 대체 글꼴을 사용하기 위해서이다.

---

### Q2. 폰트 스택이란 무엇인가요?

적용할 글꼴과 대체 글꼴을 우선순위에 따라 나열한 목록이다.

```css
font-family: Arial, Helvetica, sans-serif;
```

---

### Q3. serif와 sans-serif의 차이는 무엇인가요?

`serif`는 글자 끝에 장식이 있는 글꼴이고, `sans-serif`는 장식이 없는 글꼴이다.

---

### Q4. font-weight: 700과 bold의 차이는 무엇인가요?

일반적으로 같은 굵기를 의미한다.

`bold`는 보통 숫자값 `700`에 해당한다.

---

### Q5. line-height를 단위 없는 숫자로 사용하는 이유는 무엇인가요?

자식 요소가 자신의 글자 크기를 기준으로 줄 높이를 계산할 수 있기 때문이다.

---

### Q6. text-align: center는 요소 자체를 가운데 정렬하나요?

아니다.

블록 요소 내부의 텍스트나 인라인 콘텐츠를 가운데 정렬한다.

---

### Q7. 한 줄 말줄임표를 구현하려면 어떤 속성이 필요한가요?

```css
overflow: hidden;
text-overflow: ellipsis;
white-space: nowrap;
```

일반적으로 위 세 속성을 함께 사용한다.

---

### Q8. white-space: nowrap의 역할은 무엇인가요?

텍스트의 자동 줄바꿈을 방지한다.

---

### Q9. word-break와 overflow-wrap의 차이는 무엇인가요?

`word-break`는 단어 내부의 줄바꿈 규칙을 지정한다.

`overflow-wrap`은 긴 단어나 문자열이 요소 밖으로 넘칠 때 줄바꿈을 허용한다.

---

### Q10. 한국어 본문에서 word-break: keep-all을 사용하는 이유는 무엇인가요?

단어 중간에서 부자연스럽게 줄바꿈되는 현상을 줄이기 위해서이다.

---

### Q11. @font-face는 무엇인가요?

외부 또는 프로젝트 내부의 폰트 파일을 CSS에서 사용할 수 있도록 등록하는 규칙이다.

---

### Q12. font-display: swap은 어떻게 동작하나요?

웹 폰트가 로딩되기 전에는 대체 글꼴로 텍스트를 표시하고, 로딩이 완료되면 웹 폰트로 교체한다.

---

### Q13. 웹 폰트를 사용할 때 성능을 개선하는 방법은 무엇인가요?

- 필요한 굵기만 불러오기
- `woff2` 사용
- `font-display` 설정
- 지나치게 많은 글꼴 사용 방지
- 적절한 대체 글꼴 사용

---

### Q14. rem을 글자 크기에 사용하는 이유는 무엇인가요?

루트 요소의 글자 크기를 기준으로 계산되어 크기 체계를 일관되게 관리하기 쉽고 사용자 설정을 반영하기 좋기 때문이다.

---

### Q15. text-transform은 실제 HTML 텍스트를 변경하나요?

아니다.

화면에 표시되는 형태만 변경하며 실제 문서의 문자열은 바뀌지 않는다.

---

### Q16. text-overflow: ellipsis가 동작하지 않는 이유는 무엇인가요?

요소의 너비가 제한되지 않았거나 `overflow`, `white-space` 등 필요한 조건이 함께 설정되지 않았을 수 있다.

---

### Q17. 본문 가독성을 높이기 위해 고려할 요소는 무엇인가요?

글자 크기, 줄 높이, 글자색 대비, 한 줄의 길이, 폰트 종류, 자간 등을 함께 고려해야 한다.

---

# 핵심 정리

- `font-family`는 적용할 글꼴과 대체 글꼴을 순서대로 지정한다.
- 글꼴 이름에 공백이 있다면 따옴표를 사용하는 것이 좋다.
- 폰트 스택의 마지막에는 범용 글꼴 계열을 작성한다.
- `font-size`에는 접근성과 일관성을 위해 `rem`을 자주 사용한다.
- `font-weight`는 폰트가 실제로 지원하는 굵기를 사용해야 한다.
- `line-height`는 본문에서 단위 없는 숫자를 사용하는 것이 유용하다.
- `letter-spacing`은 글자 사이, `word-spacing`은 단어 사이 간격을 조절한다.
- `text-align`은 인라인 콘텐츠를 정렬하며 블록 요소 자체를 이동시키지 않는다.
- 링크 스타일을 제거할 때는 일반 텍스트와 구분 가능한 대체 표현이 필요하다.
- `white-space`는 공백과 줄바꿈 처리 방식을 결정한다.
- 긴 문자열에는 `overflow-wrap`을 사용할 수 있다.
- 한국어 본문에는 `word-break: keep-all`을 고려할 수 있다.
- 한 줄 말줄임표는 `overflow`, `text-overflow`, `white-space`를 함께 사용한다.
- `@font-face`를 사용하면 프로젝트 내부의 폰트 파일을 등록할 수 있다.
- 웹 폰트는 필요한 굵기만 불러오고 `font-display`를 설정하는 것이 좋다.
- 본문은 글자 크기, 줄 높이, 한 줄 너비와 색상 대비를 함께 고려해야 한다.
- HTML 제목 태그는 디자인이 아니라 문서 구조에 맞게 사용한다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-22 | 최초 작성 |
| v1.0 | 2026-07-22 | font-family와 폰트 스택 설명 추가 |
| v1.0 | 2026-07-22 | font-size, font-weight, font-style 정리 |
| v1.0 | 2026-07-22 | line-height와 텍스트 간격 속성 추가 |
| v1.0 | 2026-07-22 | 텍스트 정렬과 장식 속성 설명 추가 |
| v1.0 | 2026-07-22 | white-space와 줄바꿈 속성 정리 |
| v1.0 | 2026-07-22 | 한 줄 및 여러 줄 말줄임표 구현 추가 |
| v1.0 | 2026-07-22 | @font-face와 웹 폰트 적용 방법 추가 |
| v1.0 | 2026-07-22 | 폰트 로딩 성능과 접근성 내용 추가 |
| v1.0 | 2026-07-22 | 실무 예제 프로젝트 및 예제 분석 추가 |
| v1.0 | 2026-07-22 | 자주 하는 실수와 면접 포인트 추가 |