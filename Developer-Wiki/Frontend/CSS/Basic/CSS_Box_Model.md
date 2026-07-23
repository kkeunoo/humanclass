---
title: CSS Box Model
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS Box Model

## 개요

브라우저는 대부분의 HTML 요소를 사각형 형태의 박스로 처리한다.

이 박스는 다음 네 영역으로 구성된다.

```text
Margin

└── Border

    └── Padding

        └── Content
```

이를 CSS Box Model이라고 한다.

```css
.card {
    width: 300px;
    padding: 20px;
    border: 2px solid #333;
    margin: 30px;
}
```

위 요소의 실제 크기는 단순히 `width: 300px`만으로 결정되지 않는다.

기본 박스 모델인 `content-box`에서는 `padding`과 `border`가 요소의 크기에 추가된다.

따라서 Box Model을 이해하지 못하면 다음과 같은 문제가 발생할 수 있다.

- 요소의 실제 너비가 예상보다 커짐
- 레이아웃이 부모 영역을 벗어남
- 카드 사이의 간격이 일정하지 않음
- `width: 100%`인데 가로 스크롤이 생김
- 가운데 정렬이 되지 않음
- 세로 `margin`이 예상과 다르게 동작함
- 너비와 높이를 지정해도 크기가 맞지 않음

---

# 핵심 개념

CSS Box Model에서 이해해야 할 주요 개념은 다음과 같다.

- Content
- Padding
- Border
- Margin
- `width`
- `height`
- `min-width`
- `max-width`
- `min-height`
- `max-height`
- `box-sizing`
- `content-box`
- `border-box`
- Margin Collapsing
- `overflow`
- 논리적 속성
- 요소의 실제 크기 계산

---

# Box Model의 구조

Box Model은 다음 네 영역으로 구성된다.

| 영역 | 설명 |
|---|---|
| Content | 실제 콘텐츠가 표시되는 영역 |
| Padding | 콘텐츠와 테두리 사이의 내부 여백 |
| Border | 요소를 둘러싸는 테두리 |
| Margin | 요소와 다른 요소 사이의 외부 여백 |

```text
┌──────────────────────── Margin ────────────────────────┐
│                                                       │
│   ┌──────────────────── Border ────────────────────┐   │
│   │                                               │   │
│   │   ┌──────────────── Padding ───────────────┐   │   │
│   │   │                                       │   │   │
│   │   │              Content                  │   │   │
│   │   │                                       │   │   │
│   │   └───────────────────────────────────────┘   │   │
│   │                                               │   │
│   └───────────────────────────────────────────────┘   │
│                                                       │
└───────────────────────────────────────────────────────┘
```

---

# Content

Content는 실제 콘텐츠가 표시되는 영역이다.

다음과 같은 콘텐츠가 포함될 수 있다.

- 텍스트
- 이미지
- 버튼
- 입력 요소
- 자식 요소
- 영상

```html
<div class="card">
    CSS Box Model
</div>
```

```css
.card {
    width: 300px;
    height: 150px;
}
```

기본 `box-sizing: content-box`에서는 `width`와 `height`가 Content 영역의 크기를 의미한다.

---

# width

`width`는 요소의 너비를 지정한다.

```css
.card {
    width: 300px;
}
```

백분율을 사용할 수도 있다.

```css
.card {
    width: 80%;
}
```

일반적으로 백분율 너비는 부모 요소의 콘텐츠 영역을 기준으로 계산한다.

```html
<div class="container">
    <div class="card">
        콘텐츠
    </div>
</div>
```

```css
.container {
    width: 1000px;
}

.card {
    width: 50%;
}
```

카드의 너비는 일반적으로 `500px`이 된다.

---

# width: auto

블록 요소의 `width` 기본값은 일반적으로 `auto`이다.

```css
.card {
    width: auto;
}
```

블록 요소는 사용 가능한 가로 공간을 채우는 방향으로 동작한다.

`auto`는 단순히 항상 `100%`와 같은 의미는 아니다.

브라우저는 다음 요소들을 함께 고려하여 크기를 계산한다.

- 부모의 사용 가능한 공간
- margin
- padding
- border
- 요소의 표시 방식
- 최소 및 최대 너비

---

# height

`height`는 요소의 높이를 지정한다.

```css
.card {
    height: 200px;
}
```

고정 높이를 지정하면 콘텐츠가 많을 때 요소 밖으로 넘칠 수 있다.

```html
<div class="card">
    매우 긴 콘텐츠...
</div>
```

```css
.card {
    height: 100px;
}
```

콘텐츠 양을 예측하기 어려운 영역에서는 고정 `height`보다 `min-height`를 사용하는 것이 유연하다.

```css
.card {
    min-height: 100px;
}
```

---

# height: auto

대부분의 요소는 기본적으로 콘텐츠의 높이에 맞춰 자동으로 늘어난다.

```css
.card {
    height: auto;
}
```

콘텐츠가 많아지면 요소 높이도 함께 증가한다.

실무에서는 특별한 이유가 없다면 콘텐츠 영역에 고정 높이를 과도하게 지정하지 않는 것이 좋다.

---

# height: 100%

`height: 100%`는 부모 요소의 높이가 명확하게 계산될 수 있어야 동작한다.

```css
.parent {
    height: 500px;
}

.child {
    height: 100%;
}
```

자식 요소의 높이는 `500px`이 된다.

다음처럼 부모 높이가 콘텐츠에 따라 결정되는 `auto`라면 자식의 백분율 높이가 예상대로 계산되지 않을 수 있다.

```css
.parent {
    height: auto;
}

.child {
    height: 100%;
}
```

화면 높이가 목적이라면 다음 단위를 고려한다.

```css
.hero {
    min-height: 100dvh;
}
```

---

# min-width

`min-width`는 요소가 줄어들 수 있는 최소 너비를 지정한다.

```css
.button {
    min-width: 120px;
}
```

요소가 최소 `120px`보다 작아지지 않는다.

```css
.sidebar {
    min-width: 240px;
}
```

---

# max-width

`max-width`는 요소가 커질 수 있는 최대 너비를 제한한다.

```css
.container {
    width: 100%;
    max-width: 1200px;
}
```

화면이 작을 때는 너비가 줄어들고, 화면이 커져도 `1200px` 이상 커지지 않는다.

실무에서 콘텐츠 컨테이너에 자주 사용하는 패턴이다.

```css
.container {
    width: min(100% - 2rem, 75rem);
    margin-inline: auto;
}
```

---

# 이미지와 max-width

반응형 이미지에는 다음 스타일을 자주 사용한다.

```css
img {
    max-width: 100%;
    height: auto;
}
```

이미지가 부모 요소보다 커지는 것을 방지하면서 원본 비율을 유지한다.

---

# min-height

`min-height`는 요소의 최소 높이를 지정한다.

```css
.hero {
    min-height: 100dvh;
}
```

콘텐츠가 적으면 화면 높이만큼 유지하고, 콘텐츠가 많아지면 요소가 더 늘어날 수 있다.

```css
.card {
    min-height: 200px;
}
```

카드의 최소 높이를 맞추면서 긴 콘텐츠도 수용할 수 있다.

---

# max-height

`max-height`는 요소의 최대 높이를 제한한다.

```css
.dropdown {
    max-height: 300px;
    overflow-y: auto;
}
```

콘텐츠가 최대 높이를 넘으면 세로 스크롤을 제공할 수 있다.

---

# Padding

`padding`은 콘텐츠와 테두리 사이의 내부 여백이다.

```css
.card {
    padding: 20px;
}
```

Padding 영역에도 요소의 배경색이 표시된다.

```css
.card {
    padding: 20px;
    background-color: #f8fafc;
}
```

내부 콘텐츠와 요소의 경계 사이에 공간을 만들 때 사용한다.

---

# Padding 개별 속성

네 방향을 각각 지정할 수 있다.

```css
.card {
    padding-top: 10px;
    padding-right: 20px;
    padding-bottom: 30px;
    padding-left: 40px;
}
```

| 속성 | 방향 |
|---|---|
| `padding-top` | 위 |
| `padding-right` | 오른쪽 |
| `padding-bottom` | 아래 |
| `padding-left` | 왼쪽 |

---

# Padding 속기 문법

## 값 한 개

```css
.card {
    padding: 20px;
}
```

네 방향에 모두 `20px`이 적용된다.

```text
위    20px
오른쪽 20px
아래   20px
왼쪽   20px
```

---

## 값 두 개

```css
.card {
    padding: 20px 40px;
}
```

```text
첫 번째 값 → 위, 아래
두 번째 값 → 왼쪽, 오른쪽
```

```text
위    20px
오른쪽 40px
아래   20px
왼쪽   40px
```

---

## 값 세 개

```css
.card {
    padding: 10px 20px 30px;
}
```

```text
첫 번째 값 → 위
두 번째 값 → 왼쪽, 오른쪽
세 번째 값 → 아래
```

```text
위    10px
오른쪽 20px
아래   30px
왼쪽   20px
```

---

## 값 네 개

```css
.card {
    padding: 10px 20px 30px 40px;
}
```

시계 방향으로 적용된다.

```text
위 → 오른쪽 → 아래 → 왼쪽
```

```text
위    10px
오른쪽 20px
아래   30px
왼쪽   40px
```

---

# Padding에 음수 사용

`padding`에는 음수 값을 사용할 수 없다.

잘못된 예

```css
.card {
    padding: -20px;
}
```

내부 콘텐츠를 경계 밖으로 이동해야 한다면 다른 속성을 검토해야 한다.

- `margin`
- `transform`
- `position`

---

# Padding의 백분율

Padding의 백분율 값은 일반적으로 포함 블록의 인라인 크기, 즉 가로쓰기 환경에서는 부모의 너비를 기준으로 계산한다.

```css
.card {
    padding-top: 10%;
}
```

세로 방향 Padding이라도 부모의 높이가 아니라 너비를 기준으로 계산될 수 있다.

따라서 백분율 Padding을 사용할 때는 계산 기준을 주의해야 한다.

---

# Border

`border`는 Padding과 Margin 사이에 있는 테두리 영역이다.

```css
.card {
    border: 1px solid #ddd;
}
```

Border를 표시하려면 일반적으로 다음 세 가지 값이 필요하다.

```text
두께
스타일
색상
```

```css
.card {
    border: 2px solid royalblue;
}
```

---

# Border 개별 속성

```css
.card {
    border-width: 2px;
    border-style: solid;
    border-color: royalblue;
}
```

| 속성 | 설명 |
|---|---|
| `border-width` | 테두리 두께 |
| `border-style` | 테두리 형태 |
| `border-color` | 테두리 색상 |

---

# Border Style

대표적인 테두리 스타일은 다음과 같다.

| 값 | 설명 |
|---|---|
| `none` | 테두리 없음 |
| `solid` | 실선 |
| `dashed` | 파선 |
| `dotted` | 점선 |
| `double` | 이중선 |

```css
.solid {
    border-style: solid;
}

.dashed {
    border-style: dashed;
}

.dotted {
    border-style: dotted;
}
```

`border-style`을 지정하지 않으면 두께와 색상을 지정해도 테두리가 표시되지 않을 수 있다.

---

# 방향별 Border

특정 방향에만 테두리를 적용할 수 있다.

```css
.header {
    border-bottom: 1px solid #ddd;
}
```

```css
blockquote {
    border-left: 4px solid royalblue;
}
```

논리적 속성으로 작성할 수도 있다.

```css
blockquote {
    border-inline-start: 4px solid royalblue;
}
```

---

# border-radius

`border-radius`는 요소의 모서리를 둥글게 만든다.

```css
.card {
    border-radius: 12px;
}
```

완전한 원을 만들 수도 있다.

```css
.profile-image {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}
```

너비와 높이가 같아야 원 형태가 된다.

---

# 캡슐 모양

버튼이나 배지를 캡슐 형태로 만들 때 큰 값을 사용한다.

```css
.badge {
    border-radius: 9999px;
}
```

```css
.button {
    border-radius: 999px;
}
```

---

# outline과 border

`outline`은 요소의 바깥쪽에 표시되는 선이다.

```css
.button:focus-visible {
    outline: 3px solid royalblue;
}
```

`outline`은 일반적으로 Box Model의 크기 계산에 포함되지 않는다.

| 구분 | border | outline |
|---|---|---|
| Box Model 포함 | O | 일반적으로 X |
| 공간 차지 | O | 일반적으로 X |
| 방향별 설정 | 가능 | 제한적 |
| 주요 활용 | 요소 테두리 | 포커스 표시 |

접근성을 위해 포커스 `outline`을 대안 없이 제거하면 안 된다.

---

# Margin

`margin`은 요소의 테두리 바깥쪽에 있는 외부 여백이다.

```css
.card {
    margin: 20px;
}
```

요소와 주변 요소 사이의 간격을 만들 때 사용한다.

Margin 영역에는 일반적으로 요소의 배경색이 적용되지 않는다.

---

# Margin 개별 속성

```css
.card {
    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 30px;
    margin-left: 40px;
}
```

| 속성 | 방향 |
|---|---|
| `margin-top` | 위 |
| `margin-right` | 오른쪽 |
| `margin-bottom` | 아래 |
| `margin-left` | 왼쪽 |

---

# Margin 속기 문법

Padding과 동일한 순서로 동작한다.

## 값 한 개

```css
.card {
    margin: 20px;
}
```

네 방향에 모두 적용된다.

## 값 두 개

```css
.card {
    margin: 20px 40px;
}
```

```text
위아래 20px
좌우   40px
```

## 값 세 개

```css
.card {
    margin: 10px 20px 30px;
}
```

```text
위     10px
좌우   20px
아래   30px
```

## 값 네 개

```css
.card {
    margin: 10px 20px 30px 40px;
}
```

```text
위 → 오른쪽 → 아래 → 왼쪽
```

---

# Margin의 auto

`auto`는 브라우저가 여백을 자동으로 계산하도록 한다.

블록 요소를 가로 가운데 정렬할 때 자주 사용한다.

```css
.container {
    width: 800px;
    margin-left: auto;
    margin-right: auto;
}
```

속기 형태는 다음과 같다.

```css
.container {
    width: 800px;
    margin: 0 auto;
}
```

논리적 속성을 사용하면 다음과 같이 작성할 수 있다.

```css
.container {
    width: 800px;
    margin-inline: auto;
}
```

---

# margin-inline: auto의 조건

가운데 정렬하려는 요소의 너비가 부모보다 작아야 남는 공간을 나눌 수 있다.

```css
.card {
    width: 400px;
    margin-inline: auto;
}
```

다음처럼 블록 요소가 이미 가로 공간을 모두 사용하면 시각적인 변화가 없을 수 있다.

```css
.card {
    width: auto;
    margin-inline: auto;
}
```

---

# 음수 Margin

Margin에는 음수 값을 사용할 수 있다.

```css
.card {
    margin-top: -20px;
}
```

요소를 주변 방향으로 당기는 효과를 만들 수 있다.

다만 음수 Margin은 요소 겹침과 레이아웃 문제를 만들 수 있으므로 의도를 명확하게 이해하고 사용해야 한다.

```css
.profile-card {
    margin-top: -3rem;
}
```

---

# Padding과 Margin의 차이

| 구분 | Padding | Margin |
|---|---|---|
| 위치 | 콘텐츠와 Border 사이 | Border 바깥 |
| 배경색 적용 | 적용됨 | 적용되지 않음 |
| 음수 값 | 사용할 수 없음 | 사용할 수 있음 |
| 역할 | 내부 여백 | 외부 여백 |
| 클릭 영역 | 포함됨 | 포함되지 않음 |

버튼의 클릭 영역을 넓히려면 Margin보다 Padding을 사용하는 것이 적절하다.

```css
.button {
    padding: 12px 20px;
}
```

---

# 요소의 실제 너비 계산

기본 `box-sizing: content-box`에서 요소의 실제 너비는 다음과 같이 계산한다.

```text
실제 너비

=

margin-left
+ border-left
+ padding-left
+ width
+ padding-right
+ border-right
+ margin-right
```

Margin을 제외한 요소 자체의 렌더링 너비는 다음과 같다.

```text
요소의 전체 너비

=

width
+ 좌우 padding
+ 좌우 border
```

---

# content-box 계산 예제

```css
.card {
    width: 300px;
    padding: 20px;
    border: 5px solid black;
}
```

계산

```text
Content

300px
```

```text
좌우 Padding

20px + 20px
= 40px
```

```text
좌우 Border

5px + 5px
= 10px
```

```text
요소의 전체 너비

300px + 40px + 10px
= 350px
```

`margin`까지 각각 `10px`이라면 차지하는 전체 가로 공간은 다음과 같다.

```text
350px + 10px + 10px
= 370px
```

---

# 요소의 실제 높이 계산

기본 `content-box`에서는 다음과 같이 계산한다.

```text
요소의 전체 높이

=

height
+ 위아래 padding
+ 위아래 border
```

예제

```css
.card {
    height: 100px;
    padding: 20px;
    border: 5px solid black;
}
```

```text
100px
+ 40px
+ 10px

=

150px
```

---

# box-sizing

`box-sizing`은 `width`와 `height`가 Box Model의 어느 영역까지 포함하는지를 결정한다.

대표적인 값은 다음 두 가지이다.

| 값 | 설명 |
|---|---|
| `content-box` | width와 height가 Content 영역만 포함 |
| `border-box` | width와 height가 Content, Padding, Border 포함 |

---

# content-box

`content-box`는 기본값이다.

```css
.card {
    box-sizing: content-box;
    width: 300px;
    padding: 20px;
    border: 5px solid black;
}
```

전체 너비

```text
300px + 40px + 10px
= 350px
```

`width: 300px`은 Content 영역만 의미한다.

---

# border-box

`border-box`에서는 지정한 `width` 안에 Padding과 Border가 포함된다.

```css
.card {
    box-sizing: border-box;
    width: 300px;
    padding: 20px;
    border: 5px solid black;
}
```

전체 너비는 `300px`이다.

Content 너비는 다음과 같이 계산된다.

```text
300px
- 좌우 Padding 40px
- 좌우 Border 10px

=

250px
```

---

# content-box와 border-box 비교

다음 두 요소 모두 `width: 300px`이다.

```css
.content-box {
    box-sizing: content-box;
    width: 300px;
    padding: 20px;
    border: 5px solid;
}
```

```css
.border-box {
    box-sizing: border-box;
    width: 300px;
    padding: 20px;
    border: 5px solid;
}
```

| 구분 | content-box | border-box |
|---|---:|---:|
| 지정 width | 300px | 300px |
| Content 너비 | 300px | 250px |
| Padding 포함 | 추가됨 | width 안에 포함 |
| Border 포함 | 추가됨 | width 안에 포함 |
| 실제 요소 너비 | 350px | 300px |

---

# 전역 border-box 설정

실무에서는 크기 계산을 쉽게 하기 위해 다음 설정을 자주 사용한다.

```css
* {
    box-sizing: border-box;
}
```

가상 요소까지 포함하려면 다음과 같이 작성할 수 있다.

```css
*,
*::before,
*::after {
    box-sizing: border-box;
}
```

상속을 이용한 방식도 있다.

```css
html {
    box-sizing: border-box;
}

*,
*::before,
*::after {
    box-sizing: inherit;
}
```

---

# width: 100%와 Padding 문제

기본 `content-box`에서 다음 코드는 부모 너비를 벗어날 수 있다.

```css
.input {
    width: 100%;
    padding: 16px;
    border: 1px solid #ddd;
}
```

`width: 100%`에 Padding과 Border가 추가되기 때문이다.

```text
부모 너비 100%

+

좌우 Padding

+

좌우 Border
```

`border-box`를 적용하면 지정한 너비 안에 Padding과 Border가 포함된다.

```css
.input {
    box-sizing: border-box;
    width: 100%;
    padding: 16px;
    border: 1px solid #ddd;
}
```

---

# Margin Collapsing

Margin Collapsing은 블록 요소의 세로 Margin이 서로 합쳐지는 현상이다.

한국어로는 다음과 같이 부른다.

- 마진 상쇄
- 마진 겹침
- 마진 병합

인접한 블록 요소의 위아래 Margin은 단순히 더해지지 않고 더 큰 값 하나가 적용될 수 있다.

---

# 인접 형제의 Margin Collapsing

HTML

```html
<div class="first">
    첫 번째
</div>

<div class="second">
    두 번째
</div>
```

CSS

```css
.first {
    margin-bottom: 30px;
}

.second {
    margin-top: 50px;
}
```

예상하기 쉬운 값

```text
30px + 50px
= 80px
```

실제 세로 간격은 일반적으로 더 큰 값인 `50px`이 된다.

```text
max(30px, 50px)
= 50px
```

---

# 부모와 첫 번째 자식의 Margin Collapsing

부모에 Border, Padding, 인라인 콘텐츠 등이 없다면 첫 번째 자식의 `margin-top`이 부모 밖으로 합쳐질 수 있다.

HTML

```html
<section class="section">
    <h2 class="title">
        제목
    </h2>
</section>
```

CSS

```css
.title {
    margin-top: 40px;
}
```

`section` 내부 여백처럼 보이기를 기대했지만 부모 요소 바깥쪽으로 Margin이 나타날 수 있다.

---

# Margin Collapsing 해결 방법

상황에 따라 다음 방법을 사용할 수 있다.

## 부모에 Padding 적용

```css
.section {
    padding-top: 1px;
}
```

실무에서는 실제 디자인에 맞는 Padding 값을 사용하는 것이 좋다.

---

## 부모에 Border 적용

```css
.section {
    border-top: 1px solid transparent;
}
```

다만 단순히 Margin 상쇄를 막기 위한 편법보다는 구조에 맞는 방법을 선택한다.

---

## display: flow-root 사용

```css
.section {
    display: flow-root;
}
```

새로운 Block Formatting Context를 형성하여 자식 Margin이 부모 밖으로 상쇄되는 것을 방지할 수 있다.

---

## Flexbox 또는 Grid 사용

```css
.section {
    display: flex;
    flex-direction: column;
}
```

Flexbox와 Grid 컨테이너 내부에서는 일반적인 세로 Margin 상쇄가 발생하지 않는다.

---

## Margin 대신 부모 Padding 사용

내부 여백이 목적이라면 자식의 Margin보다 부모 Padding을 사용하는 것이 더 명확하다.

```css
.section {
    padding-top: 40px;
}
```

---

# 음수 Margin의 상쇄

양수와 음수 Margin이 만나는 경우에는 계산 방식이 더 복잡해진다.

```css
.first {
    margin-bottom: 40px;
}

.second {
    margin-top: -10px;
}
```

일반적으로 양수 Margin과 음수 Margin을 조합하여 간격이 계산된다.

음수 Margin과 Margin Collapsing이 함께 사용되면 레이아웃을 이해하기 어려워질 수 있으므로 주의해야 한다.

---

# Margin Collapsing이 발생하지 않는 주요 경우

다음 상황에서는 일반적인 Margin Collapsing이 발생하지 않는다.

- 가로 Margin
- Flex Item 사이
- Grid Item 사이
- 절대 위치 요소
- Floating 요소
- 부모와 자식 사이에 Padding이나 Border가 있는 경우
- 새로운 Block Formatting Context가 생성된 경우

---

# overflow

`overflow`는 콘텐츠가 요소의 영역을 넘을 때 처리 방법을 지정한다.

```css
.card {
    width: 300px;
    height: 100px;
    overflow: hidden;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `visible` | 넘친 콘텐츠를 그대로 표시 |
| `hidden` | 넘친 콘텐츠를 숨김 |
| `scroll` | 항상 스크롤바 표시 |
| `auto` | 필요할 때 스크롤바 표시 |
| `clip` | 넘친 콘텐츠를 잘라냄 |

---

# overflow: visible

기본값이다.

```css
.card {
    overflow: visible;
}
```

콘텐츠가 요소 밖으로 넘쳐도 표시된다.

---

# overflow: hidden

넘친 콘텐츠를 숨긴다.

```css
.thumbnail {
    overflow: hidden;
    border-radius: 1rem;
}
```

이미지를 둥근 카드 영역 안에서 잘라낼 때 사용할 수 있다.

```css
.thumbnail img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

주의할 점은 포커스 표시, 드롭다운, 그림자 등이 잘릴 수 있다는 것이다.

---

# overflow: auto

필요한 경우에만 스크롤바를 제공한다.

```css
.modal__content {
    max-height: 70dvh;
    overflow-y: auto;
}
```

---

# overflow: scroll

콘텐츠가 넘치지 않아도 스크롤 영역을 생성한다.

```css
.code-block {
    overflow-x: scroll;
}
```

일반적으로 필요할 때만 스크롤바가 나타나는 `auto`를 더 많이 사용한다.

---

# overflow-x와 overflow-y

가로와 세로 방향을 따로 지정할 수 있다.

```css
.table-wrapper {
    overflow-x: auto;
    overflow-y: hidden;
}
```

```css
.dropdown {
    overflow-x: hidden;
    overflow-y: auto;
}
```

---

# 가로 스크롤 테이블

작은 화면에서 넓은 표를 처리할 때 래퍼 요소를 사용한다.

```html
<div class="table-wrapper">
    <table>
        ...
    </table>
</div>
```

```css
.table-wrapper {
    overflow-x: auto;
}

table {
    min-width: 800px;
}
```

표 자체를 작게 압축하지 않고 필요한 경우 가로 스크롤을 제공한다.

---

# box-shadow

`box-shadow`는 요소에 그림자를 적용한다.

```css
.card {
    box-shadow: 0 10px 30px rgb(15 23 42 / 10%);
}
```

기본 구조는 다음과 같다.

```text
가로 위치
세로 위치
흐림 정도
퍼짐 정도
색상
```

```css
.card {
    box-shadow: 0 10px 30px 0 rgb(0 0 0 / 15%);
}
```

---

# inset 그림자

`inset`을 사용하면 요소 내부에 그림자가 표시된다.

```css
.input {
    box-shadow: inset 0 1px 3px rgb(0 0 0 / 10%);
}
```

---

# 여러 그림자

쉼표로 여러 그림자를 적용할 수 있다.

```css
.card {
    box-shadow:
        0 1px 2px rgb(0 0 0 / 5%),
        0 10px 30px rgb(0 0 0 / 10%);
}
```

그림자는 Box Model의 레이아웃 크기에 포함되지 않는다.

다만 시각적으로 주변 요소와 겹칠 수 있다.

---

# outline, shadow와 실제 크기

다음 속성들은 일반적으로 요소의 Box Model 크기에 포함되지 않는다.

- `outline`
- `box-shadow`

```css
.card {
    width: 300px;
    outline: 5px solid red;
    box-shadow: 0 0 20px black;
}
```

요소의 계산된 너비는 그대로지만 화면에는 바깥쪽으로 더 넓게 보일 수 있다.

---

# 논리적 속성

논리적 속성은 `top`, `right`, `bottom`, `left` 대신 문서의 글쓰기 방향을 기준으로 여백과 크기를 지정한다.

대표적인 개념은 다음과 같다.

| 개념 | 설명 |
|---|---|
| inline | 글자가 진행되는 방향 |
| block | 줄이 쌓이는 방향 |
| start | 시작 방향 |
| end | 끝 방향 |

한국어의 일반적인 가로쓰기에서는 다음과 유사하게 동작한다.

```text
inline-start  → left
inline-end    → right
block-start   → top
block-end     → bottom
```

---

# margin-inline

가로쓰기 기준 좌우 Margin을 지정한다.

```css
.container {
    margin-inline: auto;
}
```

개별 방향도 지정할 수 있다.

```css
.element {
    margin-inline-start: 1rem;
    margin-inline-end: 2rem;
}
```

---

# margin-block

가로쓰기 기준 위아래 Margin을 지정한다.

```css
.section {
    margin-block: 4rem;
}
```

```css
.title {
    margin-block-start: 0;
    margin-block-end: 1rem;
}
```

---

# padding-inline

가로쓰기 기준 좌우 Padding을 지정한다.

```css
.section {
    padding-inline: 2rem;
}
```

```css
.button {
    padding-inline: 1.5em;
}
```

---

# padding-block

가로쓰기 기준 위아래 Padding을 지정한다.

```css
.section {
    padding-block: 4rem;
}
```

```css
.button {
    padding-block: 0.75em;
}
```

---

# inline-size와 block-size

논리적 크기 속성도 사용할 수 있다.

```css
.card {
    inline-size: 300px;
    block-size: 200px;
}
```

일반적인 가로쓰기에서는 다음과 유사하다.

```text
inline-size → width
block-size  → height
```

최소 및 최대 크기도 사용할 수 있다.

```css
.container {
    max-inline-size: 75rem;
    min-block-size: 100dvh;
}
```

---

# 논리적 속성의 장점

- 다국어 문서 대응
- 오른쪽에서 왼쪽으로 쓰는 언어 지원
- 세로쓰기 대응
- 방향을 중심으로 한 일관된 스타일 작성
- `left`, `right`에 대한 의존 감소

일반적인 프로젝트에서도 다음 속성은 자주 활용할 수 있다.

```css
margin-inline: auto;
padding-inline: 2rem;
margin-block: 3rem;
```

---

# display와 Box Model

요소의 `display` 값에 따라 너비, 높이, Margin, Padding의 동작이 달라질 수 있다.

대표적인 요소 유형은 다음과 같다.

| 유형 | 특징 |
|---|---|
| Block | 새 줄에서 시작하고 사용 가능한 너비를 차지 |
| Inline | 콘텐츠 흐름 안에 배치 |
| Inline-block | 인라인 흐름에 배치되지만 크기 지정 가능 |

---

# 인라인 요소의 Box Model

`span`, `a` 등의 인라인 요소는 가로 방향 Margin과 Padding은 적용되지만 세로 방향 크기와 배치가 예상과 다를 수 있다.

```css
.link {
    width: 200px;
    height: 100px;
}
```

일반적인 인라인 요소에는 `width`와 `height`가 의도대로 적용되지 않는다.

크기를 지정하려면 `inline-block` 등을 고려한다.

```css
.link {
    display: inline-block;
    width: 200px;
    padding: 1rem;
}
```

자세한 내용은 Display 문서에서 다룬다.

---

# Replaced Element

이미지, 입력 요소 등 일부 요소는 일반 요소와 크기 계산 방식이 다를 수 있다.

대표적인 Replaced Element는 다음과 같다.

- `img`
- `video`
- `iframe`
- 일부 Form 요소

이미지에는 원본 크기와 비율이 존재한다.

```css
img {
    display: block;
    max-width: 100%;
    height: auto;
}
```

`display: block`은 이미지 아래에 발생할 수 있는 인라인 기준선 여백을 제거할 때 자주 사용한다.

---

# aspect-ratio

`aspect-ratio`는 요소의 가로세로 비율을 지정한다.

```css
.thumbnail {
    aspect-ratio: 16 / 9;
}
```

너비가 결정되면 높이를 비율에 따라 계산할 수 있다.

```css
.profile-image {
    width: 120px;
    aspect-ratio: 1;
}
```

정사각형 비율을 만든다.

```css
.profile-image {
    border-radius: 50%;
    object-fit: cover;
}
```

---

# box-decoration-break

인라인 요소가 여러 줄로 나뉘었을 때 배경과 테두리의 처리 방식을 지정할 수 있다.

```css
.highlight {
    padding: 0.2em 0.4em;
    background-color: yellow;
    box-decoration-break: clone;
}
```

브라우저 호환을 위해 접두사를 함께 사용하는 경우가 있다.

```css
.highlight {
    -webkit-box-decoration-break: clone;
    box-decoration-break: clone;
}
```

초급 단계에서는 사용 빈도가 높지 않지만 여러 줄 인라인 강조 디자인에서 활용할 수 있다.

---

# DevTools로 Box Model 확인하기

브라우저 개발자 도구의 Elements 또는 Inspector 패널에서 요소를 선택하면 Box Model 정보를 확인할 수 있다.

다음 값을 시각적으로 확인할 수 있다.

- Content 크기
- Padding
- Border
- Margin
- 계산된 width와 height
- 적용된 `box-sizing`
- 넘침 여부

CSS 요소의 크기가 예상과 다를 때는 다음 순서로 확인한다.

```text
1. 요소 선택

↓

2. Computed 또는 Layout 패널 확인

↓

3. Content 크기 확인

↓

4. Padding과 Border 확인

↓

5. box-sizing 확인

↓

6. 부모 너비와 max-width 확인

↓

7. overflow와 Margin Collapsing 확인
```

---

# 실무 활용

Box Model은 다음과 같은 상황에서 사용된다.

- 콘텐츠 컨테이너 너비 설정
- 카드 내부 및 외부 여백
- 버튼 클릭 영역 조절
- 입력 요소 너비 설정
- 반응형 이미지 처리
- 모달 최대 높이와 스크롤
- 가로 스크롤 테이블
- 프로필 이미지 비율 유지
- 카드 테두리와 그림자
- 중앙 정렬
- 섹션 간격 시스템
- 레이아웃 넘침 문제 해결

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

    <title>CSS Box Model</title>

</head>

<body>

    <header class="header">

        <div class="header__inner">

            <a
                href="#"
                class="header__logo"
            >
                Developer Wiki
            </a>

        </div>

    </header>

    <main class="main">

        <section class="hero">

            <div class="hero__content">

                <span class="hero__badge">
                    CSS Basic
                </span>

                <h1 class="hero__title">
                    CSS Box Model
                </h1>

                <p class="hero__description">
                    Content, Padding, Border, Margin을 이해하고
                    요소의 실제 크기를 정확하게 계산합니다.
                </p>

                <a
                    href="#courses"
                    class="button"
                >
                    학습 시작하기
                </a>

            </div>

        </section>

        <section
            id="courses"
            class="courses"
        >

            <div class="courses__header">

                <h2 class="courses__title">
                    학습 과정
                </h2>

                <p class="courses__description">
                    Box Model을 적용한 반응형 카드 예제입니다.
                </p>

            </div>

            <div class="course-list">

                <article class="course-card">

                    <div class="course-card__image-wrapper">

                        <img
                            src="./images/css.jpg"
                            alt="CSS 코드 화면"
                            class="course-card__image"
                        >

                    </div>

                    <div class="course-card__content">

                        <span class="course-card__category">
                            Frontend
                        </span>

                        <h3 class="course-card__title">
                            CSS Box Model 기초
                        </h3>

                        <p class="course-card__description">
                            요소의 크기와 내부 여백, 외부 여백,
                            테두리의 관계를 학습합니다.
                        </p>

                        <a
                            href="#"
                            class="course-card__link"
                        >
                            문서 읽기
                        </a>

                    </div>

                </article>

                <article class="course-card">

                    <div class="course-card__image-wrapper">

                        <img
                            src="./images/layout.jpg"
                            alt="웹 페이지 레이아웃"
                            class="course-card__image"
                        >

                    </div>

                    <div class="course-card__content">

                        <span class="course-card__category">
                            Layout
                        </span>

                        <h3 class="course-card__title">
                            반응형 크기 설계
                        </h3>

                        <p class="course-card__description">
                            min-width, max-width와 상대 단위를 이용해
                            유연한 요소 크기를 구현합니다.
                        </p>

                        <a
                            href="#"
                            class="course-card__link"
                        >
                            문서 읽기
                        </a>

                    </div>

                </article>

            </div>

        </section>

        <section class="table-section">

            <h2 class="table-section__title">
                수강 정보
            </h2>

            <div class="table-wrapper">

                <table>

                    <thead>

                        <tr>
                            <th>과정명</th>
                            <th>교육 기간</th>
                            <th>교육 시간</th>
                            <th>수강료</th>
                        </tr>

                    </thead>

                    <tbody>

                        <tr>
                            <td>CSS Basic</td>
                            <td>4주</td>
                            <td>40시간</td>
                            <td>무료</td>
                        </tr>

                    </tbody>

                </table>

            </div>

        </section>

    </main>

</body>

</html>
```

## CSS

```css
:root {
    --color-primary: #2563eb;
    --color-primary-dark: #1d4ed8;
    --color-heading: #111827;
    --color-text: #374151;
    --color-muted: #6b7280;
    --color-border: #e5e7eb;
    --color-background: #f8fafc;
    --color-surface: #ffffff;

    --radius-small: 0.5rem;
    --radius-medium: 1rem;
    --content-width: 75rem;
}

html {
    box-sizing: border-box;
}

*,
*::before,
*::after {
    box-sizing: inherit;
}

body {
    margin: 0;
    background-color: var(--color-background);
    color: var(--color-text);
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

img {
    display: block;
    max-width: 100%;
}

.header {
    border-bottom: 1px solid var(--color-border);
    background-color: var(--color-surface);
}

.header__inner {
    width: min(100% - 2rem, var(--content-width));
    margin-inline: auto;
    padding-block: 1.25rem;
}

.header__logo {
    color: var(--color-heading);
    font-size: 1.25rem;
    font-weight: 700;
    text-decoration: none;
}

.main {
    overflow: hidden;
}

.hero {
    min-height: 70dvh;
    padding-block: clamp(5rem, 12vw, 10rem);
    padding-inline: max(1rem, 5vw);
    background-color: #dbeafe;
}

.hero__content {
    max-inline-size: 50rem;
    margin-inline: auto;
    text-align: center;
}

.hero__badge {
    display: inline-block;
    padding-block: 0.5em;
    padding-inline: 1em;
    border: 1px solid currentColor;
    border-radius: 999px;
    color: var(--color-primary);
    font-size: 0.875rem;
    font-weight: 700;
}

.hero__title {
    margin-block: 1.5rem 1rem;
    color: var(--color-heading);
    font-size: clamp(2.5rem, 8vw, 6rem);
    line-height: 1.1;
}

.hero__description {
    max-inline-size: 50ch;
    margin-inline: auto;
    color: var(--color-muted);
    font-size: 1.125rem;
}

.button {
    display: inline-block;
    margin-block-start: 2rem;
    padding-block: 0.875em;
    padding-inline: 1.75em;
    border: 2px solid var(--color-primary);
    border-radius: var(--radius-small);
    background-color: var(--color-primary);
    color: white;
    font-weight: 700;
    text-decoration: none;
}

.button:hover {
    border-color: var(--color-primary-dark);
    background-color: var(--color-primary-dark);
}

.button:focus-visible {
    outline: 3px solid var(--color-primary);
    outline-offset: 4px;
}

.courses {
    width: min(100% - 2rem, var(--content-width));
    margin-inline: auto;
    padding-block: clamp(4rem, 10vw, 8rem);
}

.courses__header {
    margin-block-end: 2rem;
}

.courses__title,
.table-section__title {
    margin-block: 0 0.75rem;
    color: var(--color-heading);
    font-size: clamp(2rem, 5vw, 3rem);
    line-height: 1.2;
}

.courses__description {
    margin: 0;
    color: var(--color-muted);
}

.course-list {
    display: grid;
    grid-template-columns:
        repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
    gap: 1.5rem;
}

.course-card {
    overflow: hidden;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-medium);
    background-color: var(--color-surface);
    box-shadow: 0 1rem 3rem rgb(15 23 42 / 8%);
}

.course-card__image-wrapper {
    aspect-ratio: 16 / 9;
    overflow: hidden;
}

.course-card__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.course-card__content {
    padding: clamp(1.25rem, 4vw, 2rem);
}

.course-card__category {
    color: var(--color-primary);
    font-size: 0.8125rem;
    font-weight: 700;
}

.course-card__title {
    margin-block: 0.75rem;
    color: var(--color-heading);
    font-size: 1.5rem;
    line-height: 1.3;
}

.course-card__description {
    min-height: 4.8em;
    margin-block: 0 1.5rem;
    color: var(--color-muted);
}

.course-card__link {
    display: inline-block;
    color: var(--color-primary);
    font-weight: 700;
    text-underline-offset: 0.25em;
}

.table-section {
    width: min(100% - 2rem, var(--content-width));
    margin-inline: auto;
    padding-block-end: 8rem;
}

.table-wrapper {
    overflow-x: auto;
    margin-block-start: 2rem;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-small);
}

table {
    width: 100%;
    min-width: 45rem;
    border-collapse: collapse;
    background-color: var(--color-surface);
}

th,
td {
    padding-block: 1rem;
    padding-inline: 1.25rem;
    border-bottom: 1px solid var(--color-border);
    text-align: start;
}

th {
    background-color: #f1f5f9;
    color: var(--color-heading);
}
```

---

# 예제 분석

```css
html {
    box-sizing: border-box;
}

*,
*::before,
*::after {
    box-sizing: inherit;
}
```

모든 요소와 가상 요소가 `border-box` 크기 계산 방식을 상속받도록 한다.

```css
width: min(100% - 2rem, var(--content-width));
```

작은 화면에서는 좌우 여백을 유지하고, 큰 화면에서는 최대 콘텐츠 너비를 제한한다.

```css
margin-inline: auto;
```

남는 좌우 공간을 동일하게 분배하여 요소를 가운데 배치한다.

```css
padding-block: clamp(5rem, 12vw, 10rem);
```

섹션의 위아래 내부 여백을 화면 크기에 따라 유동적으로 조절한다.

```css
padding-inline: max(1rem, 5vw);
```

화면이 작아도 최소 좌우 Padding을 유지한다.

```css
aspect-ratio: 16 / 9;
```

이미지 영역의 가로세로 비율을 일정하게 유지한다.

```css
overflow: hidden;
```

이미지가 둥근 모서리 밖으로 넘치는 것을 숨긴다.

```css
max-width: 100%;
```

이미지가 부모 요소보다 커지는 것을 방지한다.

```css
overflow-x: auto;
```

작은 화면에서 테이블이 넘치면 가로 스크롤을 제공한다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|---|---|
| Box Model | 요소의 크기와 여백을 구성하는 모델 |
| Content | 실제 콘텐츠가 표시되는 영역 |
| Padding | 콘텐츠와 Border 사이의 내부 여백 |
| Border | 요소를 둘러싸는 테두리 |
| Margin | 요소 바깥쪽의 외부 여백 |
| width | 요소의 너비 |
| height | 요소의 높이 |
| min-width | 최소 너비 |
| max-width | 최대 너비 |
| min-height | 최소 높이 |
| max-height | 최대 높이 |
| content-box | width와 height가 Content만 포함 |
| border-box | width와 height가 Padding과 Border까지 포함 |
| box-sizing | 크기 계산 방식을 지정하는 속성 |
| Margin Collapsing | 세로 Margin이 합쳐지는 현상 |
| overflow | 넘친 콘텐츠 처리 방식 |
| box-shadow | 요소의 그림자 |
| outline | Box Model 크기에 포함되지 않는 외곽선 |
| Logical Property | 문서 방향을 기준으로 한 속성 |
| margin-inline | 인라인 방향 Margin |
| margin-block | 블록 방향 Margin |
| padding-inline | 인라인 방향 Padding |
| padding-block | 블록 방향 Padding |
| inline-size | 논리적 너비 |
| block-size | 논리적 높이 |
| aspect-ratio | 요소의 가로세로 비율 |
| flow-root | 새로운 Block Formatting Context 생성 |

---

# 자주 하는 실수

## 1. width가 요소의 최종 너비라고 생각한다

기본 `content-box`에서는 Padding과 Border가 추가된다.

```css
.card {
    width: 300px;
    padding: 20px;
    border: 5px solid;
}
```

실제 요소 너비는 `350px`이다.

---

## 2. width: 100%에 Padding을 추가하고 가로 스크롤이 생긴다

```css
.input {
    width: 100%;
    padding: 1rem;
}
```

`content-box`에서는 부모 너비보다 커질 수 있다.

```css
.input {
    box-sizing: border-box;
    width: 100%;
    padding: 1rem;
}
```

---

## 3. Padding과 Margin의 역할을 혼동한다

- Padding은 요소 내부 여백
- Margin은 요소 외부 여백

버튼의 클릭 영역을 늘리려면 Padding을 사용한다.

---

## 4. Padding에 음수 값을 사용한다

```css
.card {
    padding: -20px;
}
```

Padding에는 음수를 사용할 수 없다.

---

## 5. margin: 0 auto만 작성하면 항상 가운데 정렬된다고 생각한다

요소가 부모보다 작은 계산 가능한 너비를 가져야 한다.

```css
.card {
    width: 400px;
    margin-inline: auto;
}
```

---

## 6. 세로 Margin이 항상 더해진다고 생각한다

```css
.first {
    margin-bottom: 30px;
}

.second {
    margin-top: 50px;
}
```

일반적인 블록 흐름에서는 `80px`이 아니라 `50px`으로 상쇄될 수 있다.

---

## 7. 부모 내부 간격을 자식의 margin-top으로 만든다

첫 번째 자식의 Margin이 부모 밖으로 상쇄될 수 있다.

내부 여백이 목적이라면 부모의 Padding을 사용한다.

```css
.parent {
    padding-top: 2rem;
}
```

---

## 8. 모든 요소에 고정 height를 지정한다

콘텐츠가 많아지면 넘침이 발생할 수 있다.

```css
.card {
    min-height: 200px;
}
```

유동적인 콘텐츠에는 `min-height`를 고려한다.

---

## 9. height: 100%가 항상 화면 높이를 의미한다고 생각한다

부모의 높이가 명확해야 한다.

화면 높이가 목적이라면 `100dvh` 등을 고려한다.

---

## 10. overflow: hidden을 문제 해결용으로 무조건 사용한다

넘치는 요소뿐만 아니라 다음 내용도 잘릴 수 있다.

- 포커스 Outline
- 그림자
- 드롭다운
- 툴팁
- 위치가 이동된 자식 요소

---

## 11. Border에 style을 작성하지 않는다

```css
.card {
    border-width: 1px;
    border-color: black;
}
```

`border-style`이 없으면 표시되지 않을 수 있다.

```css
.card {
    border: 1px solid black;
}
```

---

## 12. border-radius: 50%만 사용하면 원이 된다고 생각한다

너비와 높이가 같아야 원 형태가 된다.

```css
.avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}
```

---

## 13. outline과 border를 같은 것으로 생각한다

`border`는 요소 크기에 포함되지만 `outline`은 일반적으로 레이아웃 공간을 차지하지 않는다.

---

## 14. 인라인 요소에 width와 height를 지정한다

일반적인 인라인 요소에는 크기가 의도대로 적용되지 않을 수 있다.

```css
.link {
    display: inline-block;
    width: 200px;
}
```

---

## 15. 이미지에 width와 height를 모두 고정하여 비율이 깨진다

```css
img {
    width: 300px;
    height: 100px;
}
```

의도적인 Crop이 아니라면 다음처럼 비율을 유지한다.

```css
img {
    max-width: 100%;
    height: auto;
}
```

---

## 16. max-width 없이 큰 고정 너비만 사용한다

```css
.container {
    width: 1200px;
}
```

작은 화면에서 가로 스크롤이 발생할 수 있다.

```css
.container {
    width: min(100% - 2rem, 1200px);
}
```

---

## 17. Margin으로 버튼의 클릭 영역을 늘리려고 한다

Margin은 클릭 가능한 요소 영역에 포함되지 않는다.

```css
.button {
    padding: 0.75rem 1.5rem;
}
```

Padding을 사용한다.

---

## 18. box-shadow가 요소의 레이아웃 크기를 늘린다고 생각한다

그림자는 시각적으로 바깥에 표시되지만 일반적으로 레이아웃 크기 계산에는 포함되지 않는다.

---

# 면접 포인트

### Q1. CSS Box Model이란 무엇인가요?

HTML 요소를 Content, Padding, Border, Margin 영역으로 나누어 크기와 간격을 계산하는 모델이다.

---

### Q2. Box Model의 구성 요소를 설명해 보세요.

- Content: 실제 콘텐츠 영역
- Padding: 콘텐츠와 Border 사이의 내부 여백
- Border: 요소의 테두리
- Margin: 요소 바깥쪽의 외부 여백

---

### Q3. content-box와 border-box의 차이는 무엇인가요?

`content-box`에서는 지정한 `width`와 `height`가 Content 영역만 의미한다.

`border-box`에서는 지정한 크기에 Padding과 Border가 포함된다.

---

### Q4. 다음 요소의 실제 너비는 얼마인가요?

```css
.card {
    width: 300px;
    padding: 20px;
    border: 5px solid;
}
```

기본 `content-box`에서는 다음과 같다.

```text
300px
+ 좌우 Padding 40px
+ 좌우 Border 10px

=

350px
```

---

### Q5. 실무에서 box-sizing: border-box를 자주 사용하는 이유는 무엇인가요?

지정한 너비와 높이 안에 Padding과 Border가 포함되어 요소의 최종 크기를 예측하고 관리하기 쉽기 때문이다.

---

### Q6. Padding과 Margin의 차이는 무엇인가요?

Padding은 콘텐츠와 Border 사이의 내부 여백이고, Margin은 요소의 Border 바깥쪽 외부 여백이다.

---

### Q7. Padding과 Margin 중 음수 값을 사용할 수 있는 것은 무엇인가요?

Margin은 음수 값을 사용할 수 있지만 Padding은 사용할 수 없다.

---

### Q8. margin-inline: auto는 언제 요소를 가운데 정렬하나요?

블록 요소가 부모보다 작은 계산 가능한 너비를 가지고 있어 좌우에 남는 공간이 있을 때 가운데 정렬할 수 있다.

---

### Q9. Margin Collapsing이란 무엇인가요?

일반적인 블록 흐름에서 인접한 세로 Margin이 더해지지 않고 하나의 Margin으로 합쳐지는 현상이다.

---

### Q10. Margin Collapsing을 방지하는 방법에는 무엇이 있나요?

- 부모에 Padding이나 Border 적용
- `display: flow-root` 사용
- Flexbox 또는 Grid 사용
- 내부 간격을 부모 Padding으로 처리

---

### Q11. height: 100%가 동작하지 않는 이유는 무엇인가요?

부모 요소의 높이가 명확하게 계산되지 않으면 자식의 백분율 높이 기준을 결정할 수 없기 때문이다.

---

### Q12. min-height와 height의 차이는 무엇인가요?

`height`는 요소의 높이를 지정한다.

`min-height`는 최소 높이만 제한하고 콘텐츠가 많으면 요소가 더 커질 수 있다.

---

### Q13. overflow: hidden을 사용할 때 주의할 점은 무엇인가요?

넘친 콘텐츠뿐 아니라 포커스 Outline, 그림자, 툴팁, 드롭다운 등이 잘릴 수 있다.

---

### Q14. outline과 border의 차이는 무엇인가요?

`border`는 Box Model의 크기에 포함되며 공간을 차지한다.

`outline`은 일반적으로 요소 외부에 표시되고 레이아웃 공간을 차지하지 않는다.

---

### Q15. max-width: 100%를 이미지에 사용하는 이유는 무엇인가요?

이미지가 부모 요소보다 커지는 것을 방지하여 작은 화면에서 레이아웃이 넘치는 것을 줄이기 위해서이다.

---

### Q16. aspect-ratio의 역할은 무엇인가요?

요소의 가로세로 비율을 지정하여 한쪽 크기가 결정되었을 때 다른 쪽 크기를 비율에 따라 계산하도록 한다.

---

### Q17. 논리적 속성을 사용하는 이유는 무엇인가요?

문서의 글쓰기 방향을 기준으로 스타일을 지정할 수 있어 다국어, RTL, 세로쓰기 환경에 대응하기 쉽기 때문이다.

---

### Q18. box-shadow는 Box Model 크기에 포함되나요?

일반적으로 포함되지 않는다.

시각적으로 요소 밖에 표시될 수 있지만 레이아웃 크기 계산에는 영향을 주지 않는다.

---

# 핵심 정리

- 브라우저는 대부분의 HTML 요소를 사각형 박스로 처리한다.
- Box Model은 Content, Padding, Border, Margin으로 구성된다.
- Padding은 내부 여백이고 Margin은 외부 여백이다.
- Padding에는 배경이 표시되지만 Margin에는 일반적으로 표시되지 않는다.
- Padding은 음수를 사용할 수 없지만 Margin은 음수를 사용할 수 있다.
- 기본 `content-box`에서는 Padding과 Border가 지정한 크기에 추가된다.
- `border-box`에서는 Padding과 Border가 지정한 크기 안에 포함된다.
- 실무에서는 요소 크기를 예측하기 위해 전역 `border-box` 설정을 자주 사용한다.
- `max-width`는 반응형 콘텐츠 너비와 이미지 크기를 제한할 때 유용하다.
- 콘텐츠 양을 예측하기 어려운 영역에서는 고정 `height`보다 `min-height`가 유연하다.
- `height: 100%`는 부모 높이가 명확해야 한다.
- `margin-inline: auto`는 남는 좌우 공간을 분배하여 요소를 가운데 배치한다.
- 일반 블록 요소의 세로 Margin은 상쇄될 수 있다.
- 내부 간격이 목적이라면 부모 Padding을 사용하는 것이 명확하다.
- `overflow`는 콘텐츠가 요소 영역을 넘을 때의 처리 방법을 지정한다.
- `outline`과 `box-shadow`는 일반적으로 Box Model의 크기에 포함되지 않는다.
- 논리적 속성을 사용하면 문서 방향에 유연하게 대응할 수 있다.
- `aspect-ratio`를 사용하면 요소의 가로세로 비율을 유지할 수 있다.
- Box Model 문제는 DevTools의 Computed 또는 Layout 패널에서 확인할 수 있다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-22 | 최초 작성 |
| v1.0 | 2026-07-22 | Content, Padding, Border, Margin 구조 정리 |
| v1.0 | 2026-07-22 | width, height 및 최소·최대 크기 속성 설명 추가 |
| v1.0 | 2026-07-22 | Padding과 Margin 속기 문법 정리 |
| v1.0 | 2026-07-22 | 요소의 실제 너비와 높이 계산 예제 추가 |
| v1.0 | 2026-07-22 | content-box와 border-box 비교 추가 |
| v1.0 | 2026-07-22 | 전역 box-sizing 설정 방법 추가 |
| v1.0 | 2026-07-22 | Margin Collapsing 원리와 해결 방법 추가 |
| v1.0 | 2026-07-22 | overflow와 스크롤 처리 방법 추가 |
| v1.0 | 2026-07-22 | box-shadow, outline, aspect-ratio 설명 추가 |
| v1.0 | 2026-07-22 | 논리적 Margin, Padding, 크기 속성 추가 |
| v1.0 | 2026-07-22 | 실무 예제 프로젝트 및 DevTools 활용법 추가 |
| v1.0 | 2026-07-22 | 자주 하는 실수와 면접 포인트 추가 |