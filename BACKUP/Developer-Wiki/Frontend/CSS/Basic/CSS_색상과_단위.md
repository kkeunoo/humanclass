---
title: CSS 색상과 단위
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS 색상과 단위

## 개요

CSS에서는 색상과 크기를 지정하기 위해 다양한 표현 방식과 단위를 사용한다.

색상은 글자, 배경, 테두리, 그림자 등에 적용하며, 단위는 글자 크기, 요소의 너비와 높이, 여백, 위치 등을 지정할 때 사용한다.

```css
.card {
    width: 320px;
    padding: 2rem;
    background-color: #ffffff;
    color: rgb(31, 41, 55);
}
```

위 코드에서는 다음 개념이 사용되었다.

- `320px`: 절대 길이 단위
- `2rem`: 상대 길이 단위
- `#ffffff`: HEX 색상
- `rgb(31, 41, 55)`: RGB 색상

색상과 단위는 CSS의 거의 모든 영역에서 사용되므로 각각의 특징과 사용 목적을 이해해야 한다.

---

# 핵심 개념

CSS 색상과 단위에서 이해해야 할 핵심 내용은 다음과 같다.

- 색상 이름
- HEX 색상
- RGB와 RGBA
- HSL과 HSLA
- 투명도
- 절대 단위
- 상대 단위
- 백분율
- 뷰포트 단위
- 글자 크기 단위
- `calc()`
- `min()`, `max()`, `clamp()`
- CSS 사용자 정의 속성

---

# CSS 색상

CSS 색상은 다음과 같은 속성에 사용할 수 있다.

```css
.title {
    color: royalblue;
}
```

```css
.section {
    background-color: #f8fafc;
}
```

```css
.card {
    border-color: rgb(203, 213, 225);
}
```

```css
.modal {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
```

대표적인 색상 표현 방식은 다음과 같다.

| 방식 | 예제 |
|---|---|
| 색상 이름 | `red` |
| HEX | `#ff0000` |
| RGB | `rgb(255, 0, 0)` |
| RGBA | `rgba(255, 0, 0, 0.5)` |
| HSL | `hsl(0, 100%, 50%)` |
| HSLA | `hsla(0, 100%, 50%, 0.5)` |
| 투명 색상 | `transparent` |
| 현재 글자색 | `currentColor` |

---

# 색상 이름

CSS에서 미리 정의된 색상 이름을 사용할 수 있다.

```css
p {
    color: red;
}
```

```css
button {
    background-color: royalblue;
    color: white;
}
```

대표적인 색상 이름은 다음과 같다.

```text
red
blue
green
black
white
gray
yellow
orange
purple
royalblue
tomato
```

색상 이름은 빠르게 테스트할 때 편리하지만, 정교한 디자인 시스템에서는 HEX, RGB, HSL 등을 더 많이 사용한다.

---

# HEX 색상

HEX는 빨강, 초록, 파랑 값을 16진수로 표현한다.

```css
color: #ff0000;
```

구조는 다음과 같다.

```text
#RRGGBB
```

| 부분 | 의미 |
|---|---|
| RR | 빨강 |
| GG | 초록 |
| BB | 파랑 |

각 값은 `00`부터 `ff`까지 사용할 수 있다.

```css
.red {
    color: #ff0000;
}

.green {
    color: #00ff00;
}

.blue {
    color: #0000ff;
}
```

---

# HEX 축약형

같은 문자가 반복되는 경우 세 자리로 줄여 작성할 수 있다.

```css
color: #ffffff;
```

다음과 같이 축약할 수 있다.

```css
color: #fff;
```

다른 예제

```css
#000000 → #000
#ff0000 → #f00
#00ff00 → #0f0
#0000ff → #00f
```

다음처럼 각 두 자리가 동일하지 않으면 축약할 수 없다.

```css
#12a4ff
```

---

# 투명도를 포함한 HEX

HEX 색상 뒤에 알파값을 추가할 수 있다.

```text
#RRGGBBAA
```

예제

```css
background-color: #00000080;
```

검은색에 약 50%의 투명도를 적용한 표현이다.

축약형으로도 작성할 수 있다.

```text
#RGBA
```

다만 가독성과 협업을 위해 RGBA 방식을 사용하는 경우도 많다.

---

# RGB 색상

RGB는 빨강, 초록, 파랑의 강도를 숫자로 표현한다.

```css
color: rgb(255, 0, 0);
```

각 값은 일반적으로 `0`부터 `255`까지 사용한다.

```css
.red {
    color: rgb(255, 0, 0);
}

.green {
    color: rgb(0, 255, 0);
}

.blue {
    color: rgb(0, 0, 255);
}
```

세 값이 모두 같으면 회색 계열이 된다.

```css
color: rgb(0, 0, 0);
```

검은색

```css
color: rgb(255, 255, 255);
```

흰색

```css
color: rgb(128, 128, 128);
```

회색

---

# RGBA 색상

RGBA는 RGB에 투명도인 Alpha 값을 추가한 표현이다.

```css
background-color: rgba(0, 0, 0, 0.5);
```

Alpha 값은 일반적으로 `0`부터 `1`까지 사용한다.

| 값 | 의미 |
|---:|---|
| `0` | 완전히 투명 |
| `0.5` | 반투명 |
| `1` | 완전히 불투명 |

예제

```css
.overlay {
    background-color: rgba(0, 0, 0, 0.6);
}
```

모달의 배경이나 이미지 위의 어두운 오버레이에 자주 사용한다.

---

# 현대 RGB 문법

쉼표 없이 공백으로 값을 구분하는 문법도 사용할 수 있다.

```css
color: rgb(255 0 0);
```

Alpha 값은 슬래시(`/`) 뒤에 작성한다.

```css
background-color: rgb(0 0 0 / 50%);
```

기존 문법과 현대 문법은 같은 목적을 가진다.

```css
rgba(0, 0, 0, 0.5);
```

```css
rgb(0 0 0 / 50%);
```

---

# HSL 색상

HSL은 색상, 채도, 명도를 기준으로 색을 표현한다.

```text
HSL

H: Hue
S: Saturation
L: Lightness
```

예제

```css
color: hsl(220, 90%, 56%);
```

| 구성 | 의미 |
|---|---|
| Hue | 색상 각도 |
| Saturation | 채도 |
| Lightness | 명도 |

---

# Hue

Hue는 색상환의 각도를 나타낸다.

| 값 | 대표 색상 |
|---:|---|
| `0` | 빨강 |
| `60` | 노랑 |
| `120` | 초록 |
| `180` | 청록 |
| `240` | 파랑 |
| `300` | 자주색 |
| `360` | 빨강 |

```css
.red {
    color: hsl(0, 100%, 50%);
}

.green {
    color: hsl(120, 100%, 50%);
}

.blue {
    color: hsl(240, 100%, 50%);
}
```

---

# Saturation

채도는 색상의 선명함을 의미한다.

```text
0%   → 회색
100% → 가장 선명한 색
```

```css
color: hsl(220, 0%, 50%);
```

채도가 0%이면 색상 각도와 관계없이 회색 계열이 된다.

---

# Lightness

명도는 색상의 밝기를 의미한다.

```text
0%   → 검은색
50%  → 기본 색상
100% → 흰색
```

```css
.dark {
    color: hsl(220, 90%, 20%);
}

.normal {
    color: hsl(220, 90%, 50%);
}

.light {
    color: hsl(220, 90%, 80%);
}
```

---

# HSLA 색상

HSL에 투명도를 추가한다.

```css
background-color: hsla(220, 90%, 56%, 0.5);
```

현대 문법으로도 작성할 수 있다.

```css
background-color: hsl(220 90% 56% / 50%);
```

HSL은 색상의 밝기나 채도를 단계적으로 조정하기 쉬워 디자인 시스템에서 유용하다.

---

# transparent

`transparent`는 완전히 투명한 색상을 의미한다.

```css
button {
    background-color: transparent;
}
```

```css
input {
    border-color: transparent;
}
```

색상이 존재하지 않는 것처럼 보이지만, 속성 자체가 제거되는 것은 아니다.

---

# currentColor

`currentColor`는 현재 요소의 `color` 속성값을 사용한다.

```css
.button {
    color: royalblue;
    border: 2px solid currentColor;
}
```

위 코드에서 테두리 색상은 글자색과 같은 `royalblue`가 된다.

```css
.icon {
    color: crimson;
    fill: currentColor;
}
```

아이콘과 글자색을 일관되게 관리할 때 유용하다.

---

# opacity

`opacity`는 요소 전체의 투명도를 조절한다.

```css
.card {
    opacity: 0.5;
}
```

`opacity`는 배경뿐만 아니라 다음 항목에도 모두 영향을 준다.

- 글자
- 이미지
- 테두리
- 자식 요소

HTML

```html
<div class="card">
    <h2>제목</h2>
</div>
```

CSS

```css
.card {
    opacity: 0.5;
}
```

부모와 자식 전체가 반투명해진다.

배경색만 투명하게 만들고 싶다면 RGBA나 투명도를 포함한 HSL을 사용하는 것이 좋다.

```css
.card {
    background-color: rgb(0 0 0 / 50%);
}
```

---

# 색상 표현 방식 비교

| 방식 | 장점 | 주요 사용 |
|---|---|---|
| 색상 이름 | 간단함 | 빠른 테스트 |
| HEX | 짧고 익숙함 | 일반적인 디자인 |
| RGB | 색상 채널이 명확함 | 동적 색상 계산 |
| RGBA | 투명도 표현 | 오버레이와 그림자 |
| HSL | 밝기와 채도 조절이 쉬움 | 디자인 시스템 |
| currentColor | 현재 글자색 재사용 | 아이콘과 테두리 |

---

# CSS 단위

CSS 단위는 요소의 크기, 간격, 위치 등을 지정할 때 사용한다.

```css
.card {
    width: 320px;
    padding: 2rem;
    margin-bottom: 5vh;
}
```

CSS 단위는 크게 다음과 같이 구분할 수 있다.

```text
절대 단위

상대 단위

백분율 단위

뷰포트 단위

각도 단위

시간 단위
```

---

# 절대 단위

절대 단위는 다른 요소의 크기와 관계없이 비교적 고정된 값을 사용한다.

대표적인 단위는 `px`이다.

| 단위 | 의미 |
|---|---|
| `px` | CSS 픽셀 |
| `cm` | 센티미터 |
| `mm` | 밀리미터 |
| `in` | 인치 |
| `pt` | 포인트 |
| `pc` | 파이카 |

웹 화면에서는 대부분 `px`를 사용한다.

---

# px

`px`는 CSS에서 가장 많이 사용하는 절대 길이 단위이다.

```css
.card {
    width: 320px;
    border-width: 1px;
    border-radius: 12px;
}
```

주로 다음과 같은 항목에 사용한다.

- 얇은 테두리
- 아이콘 크기
- 고정된 최소 간격
- 둥근 모서리
- 작은 그림자 위치

```css
.button {
    border: 1px solid #ddd;
    border-radius: 8px;
}
```

---

# px의 특징

장점

- 값을 직관적으로 이해하기 쉽다.
- 고정된 크기를 표현하기 편하다.
- 정밀한 디자인에 유용하다.

주의점

- 모든 크기를 `px`로 고정하면 반응형 구현이 어려울 수 있다.
- 사용자의 기본 글자 크기 설정을 충분히 반영하지 못할 수 있다.
- 화면 크기에 따라 유연하게 변하지 않는다.

---

# 상대 단위

상대 단위는 다른 기준값에 따라 실제 크기가 결정된다.

대표적인 상대 단위는 다음과 같다.

| 단위 | 기준 |
|---|---|
| `%` | 부모 또는 관련 기준값 |
| `em` | 현재 요소의 글자 크기 |
| `rem` | 루트 요소의 글자 크기 |
| `vw` | 뷰포트 너비 |
| `vh` | 뷰포트 높이 |
| `vmin` | 뷰포트의 작은 쪽 |
| `vmax` | 뷰포트의 큰 쪽 |

---

# em

`em`은 일반적으로 현재 요소의 `font-size`를 기준으로 계산한다.

```css
.button {
    font-size: 16px;
    padding: 0.75em 1.5em;
}
```

계산 결과

```text
세로 padding

16px × 0.75
= 12px
```

```text
가로 padding

16px × 1.5
= 24px
```

버튼의 글자 크기를 변경하면 내부 여백도 함께 변한다.

```css
.button-large {
    font-size: 20px;
}
```

`em`은 컴포넌트 크기를 글자 크기에 비례하여 조정할 때 유용하다.

---

# em 중첩 문제

`font-size`에 `em`을 사용하면 부모 크기의 영향을 반복적으로 받을 수 있다.

HTML

```html
<div class="parent">
    부모
    <div class="child">
        자식
        <div class="grandchild">
            손자
        </div>
    </div>
</div>
```

CSS

```css
.parent {
    font-size: 1.2em;
}

.child {
    font-size: 1.2em;
}

.grandchild {
    font-size: 1.2em;
}
```

각 단계에서 이전 요소의 글자 크기를 기준으로 다시 계산되므로 글자 크기가 점점 커질 수 있다.

---

# rem

`rem`은 루트 요소인 `<html>`의 `font-size`를 기준으로 계산한다.

```css
html {
    font-size: 16px;
}
```

```css
.title {
    font-size: 2rem;
}
```

계산 결과

```text
16px × 2
= 32px
```

```css
.description {
    font-size: 1.125rem;
}
```

계산 결과

```text
16px × 1.125
= 18px
```

---

# rem의 장점

- 중첩 구조의 영향을 받지 않는다.
- 전체 크기 체계를 일관되게 관리할 수 있다.
- 사용자의 브라우저 글자 크기 설정을 반영하기 쉽다.
- 글자 크기와 간격 시스템을 구성하기 좋다.

```css
html {
    font-size: 100%;
}

body {
    font-size: 1rem;
}

h1 {
    font-size: 2.5rem;
}

section {
    padding: 4rem 2rem;
}
```

실무에서는 글자 크기와 주요 간격에 `rem`을 자주 사용한다.

---

# em과 rem 비교

| 구분 | em | rem |
|---|---|---|
| 기준 | 현재 요소 또는 부모의 글자 크기 | html의 글자 크기 |
| 중첩 영향 | 받을 수 있음 | 받지 않음 |
| 컴포넌트 내부 비율 | 유용 | 가능 |
| 전체 디자인 체계 | 관리가 복잡할 수 있음 | 관리하기 쉬움 |
| 주요 활용 | 버튼 내부 간격 | 글자 크기와 전체 간격 |

---

# 백분율

백분율 `%`은 속성마다 기준이 다를 수 있다.

```css
.container {
    width: 80%;
}
```

일반적으로 `width`의 백분율은 부모 요소의 콘텐츠 너비를 기준으로 계산한다.

HTML

```html
<div class="parent">
    <div class="child">
        콘텐츠
    </div>
</div>
```

CSS

```css
.parent {
    width: 1000px;
}

.child {
    width: 50%;
}
```

자식의 너비는 `500px`이 된다.

---

# height의 백분율

`height: 100%`는 부모의 높이가 명확하게 지정되어 있어야 의도대로 동작하는 경우가 많다.

```css
.parent {
    height: 500px;
}

.child {
    height: 100%;
}
```

부모의 높이가 `auto`라면 자식의 백분율 높이를 계산하기 어려울 수 있다.

---

# padding과 margin의 백분율

`padding`과 `margin`에 백분율을 사용할 경우 일반적으로 포함 블록의 **너비**를 기준으로 계산한다.

```css
.card {
    padding-top: 10%;
}
```

세로 여백임에도 높이가 아니라 너비를 기준으로 계산될 수 있으므로 주의해야 한다.

---

# 뷰포트 단위

뷰포트는 브라우저에서 웹 페이지가 표시되는 영역이다.

| 단위 | 의미 |
|---|---|
| `vw` | 뷰포트 너비의 1% |
| `vh` | 뷰포트 높이의 1% |
| `vmin` | 너비와 높이 중 작은 값의 1% |
| `vmax` | 너비와 높이 중 큰 값의 1% |

---

# vw

`1vw`는 뷰포트 너비의 1%이다.

```css
.hero-title {
    font-size: 5vw;
}
```

뷰포트 너비가 `1000px`이면 다음과 같다.

```text
1vw = 10px
5vw = 50px
```

화면 너비에 따라 유동적인 값을 만들 수 있다.

---

# vh

`1vh`는 뷰포트 높이의 1%이다.

```css
.hero {
    min-height: 100vh;
}
```

화면 전체 높이를 차지하는 Hero 영역 등에 사용한다.

다만 모바일 브라우저에서는 주소창과 도구 모음의 변화 때문에 `100vh`가 예상과 다르게 보일 수 있다.

---

# 동적 뷰포트 단위

모바일 브라우저의 UI 변화에 대응하기 위한 뷰포트 단위도 있다.

| 단위 | 의미 |
|---|---|
| `svh` | 작은 뷰포트 높이 |
| `lvh` | 큰 뷰포트 높이 |
| `dvh` | 현재 동적 뷰포트 높이 |

예제

```css
.hero {
    min-height: 100dvh;
}
```

모바일 브라우저의 주소창이 나타나거나 사라질 때 현재 화면 높이를 반영하는 데 유용하다.

---

# vmin

`vmin`은 뷰포트 너비와 높이 중 더 작은 값을 기준으로 한다.

```css
.logo {
    width: 20vmin;
    height: 20vmin;
}
```

가로와 세로 방향 모두에서 크기를 일정한 비율로 유지하는 데 유용하다.

---

# vmax

`vmax`는 뷰포트 너비와 높이 중 더 큰 값을 기준으로 한다.

```css
.background-shape {
    width: 50vmax;
    height: 50vmax;
}
```

큰 장식 요소 등에 사용할 수 있다.

---

# ch

`ch`는 현재 글꼴에서 숫자 `0` 한 글자의 너비를 기준으로 한다.

```css
.article {
    max-width: 65ch;
}
```

본문 한 줄의 길이를 제한할 때 유용하다.

```css
input {
    width: 20ch;
}
```

대략 20자 정도의 입력 너비를 표현할 수 있다.

글꼴에 따라 실제 너비는 달라질 수 있다.

---

# ex

`ex`는 현재 글꼴의 소문자 `x` 높이를 기준으로 한다.

```css
.element {
    height: 2ex;
}
```

실무에서는 `rem`, `em`, `ch`보다 사용 빈도가 낮다.

---

# line-height의 단위 없는 값

`line-height`는 단위를 생략한 숫자로 작성하는 것이 권장되는 경우가 많다.

```css
body {
    line-height: 1.6;
}
```

현재 요소의 글자 크기에 `1.6`을 곱하여 줄 높이를 계산한다.

```text
font-size: 16px

16px × 1.6
= 25.6px
```

단위 없는 값은 자식 요소가 자신의 글자 크기에 맞는 줄 높이를 계산하도록 상속된다.

---

# 각도 단위

회전이나 그라디언트에서 각도 단위를 사용한다.

| 단위 | 의미 |
|---|---|
| `deg` | 도 |
| `rad` | 라디안 |
| `grad` | 그라디안 |
| `turn` | 한 바퀴 |

예제

```css
.icon {
    transform: rotate(45deg);
}
```

```css
.loader {
    transform: rotate(0.5turn);
}
```

```text
1turn = 360deg
```

---

# 시간 단위

애니메이션과 전환 효과에서 시간 단위를 사용한다.

| 단위 | 의미 |
|---|---|
| `s` | 초 |
| `ms` | 밀리초 |

```css
.button {
    transition: background-color 0.3s;
}
```

```css
.modal {
    animation-duration: 500ms;
}
```

```text
1s = 1000ms
```

---

# calc()

`calc()`는 서로 다른 단위를 계산할 수 있는 CSS 함수이다.

```css
.main {
    width: calc(100% - 240px);
}
```

전체 너비에서 사이드바 너비를 제외할 수 있다.

```css
.card {
    padding: calc(1rem + 1vw);
}
```

연산자 앞뒤에는 공백을 작성하는 것이 안전하다.

권장

```css
width: calc(100% - 20px);
```

좋지 않은 예

```css
width: calc(100%-20px);
```

---

# calc() 연산

다음 연산을 사용할 수 있다.

```text
+
-
*
/
```

가장 흔히 사용하는 연산은 더하기와 빼기이다.

```css
height: calc(100dvh - 80px);
```

헤더 높이를 제외한 화면 높이를 계산할 수 있다.

---

# min()

`min()`은 전달된 값 중 더 작은 값을 사용한다.

```css
.container {
    width: min(100% - 32px, 1200px);
}
```

다음 두 조건 중 작은 너비를 사용한다.

- 화면 너비에서 32px을 제외한 값
- 1200px

화면이 작을 때는 화면에 맞게 줄어들고, 큰 화면에서는 최대 1200px까지만 커진다.

---

# max()

`max()`는 전달된 값 중 더 큰 값을 사용한다.

```css
.section {
    padding-inline: max(20px, 5vw);
}
```

화면이 작아도 최소 `20px`의 좌우 여백을 유지하고, 화면이 커지면 `5vw`를 적용한다.

---

# clamp()

`clamp()`는 최소값, 선호값, 최대값을 한 번에 지정한다.

```css
font-size: clamp(2rem, 5vw, 4rem);
```

구조

```text
clamp(최소값, 선호값, 최대값)
```

동작 방식

```text
최소 2rem

↓

화면 크기에 따라 5vw 적용

↓

최대 4rem
```

반응형 글자 크기를 만들 때 매우 유용하다.

```css
.hero-title {
    font-size: clamp(2.25rem, 6vw, 5rem);
}
```

미디어 쿼리를 많이 작성하지 않고도 부드러운 크기 변화를 만들 수 있다.

---

# 단위 사용 기준

모든 상황에 하나의 단위만 사용하는 것은 적절하지 않다.

대표적인 사용 기준은 다음과 같다.

| 대상 | 추천 단위 |
|---|---|
| 글자 크기 | `rem` |
| 줄 높이 | 단위 없는 숫자 |
| 컴포넌트 내부 간격 | `em`, `rem` |
| 전체 레이아웃 간격 | `rem` |
| 테두리 | `px` |
| 최대 콘텐츠 너비 | `px`, `rem`, `ch` |
| 부모 기준 너비 | `%` |
| 화면 기준 크기 | `vw`, `vh`, `dvh` |
| 유동적인 글자 크기 | `clamp()` |
| 계산된 레이아웃 | `calc()` |

이 표는 절대적인 규칙이 아니라 일반적인 기준이다.

---

# 62.5% 글자 크기 설정

다음과 같은 코드를 사용하는 경우가 있다.

```css
html {
    font-size: 62.5%;
}
```

브라우저의 기본 글자 크기가 `16px`이라면 다음과 같이 계산된다.

```text
16px × 62.5%
= 10px
```

따라서 다음 값이 계산하기 쉬워진다.

```css
font-size: 1.6rem;
```

```text
1.6rem = 16px
```

다만 이 방식은 프로젝트 규칙에 따라 선택적으로 사용하며 반드시 적용해야 하는 표준은 아니다.

사용자의 기본 설정과 접근성을 고려하여 다음처럼 기본값을 유지하는 방식도 많이 사용한다.

```css
html {
    font-size: 100%;
}
```

---

# CSS 사용자 정의 속성

반복되는 색상과 크기는 CSS 사용자 정의 속성으로 관리할 수 있다.

```css
:root {
    --color-primary: #2563eb;
    --color-text: #1f2937;
    --color-background: #f8fafc;

    --spacing-small: 0.5rem;
    --spacing-medium: 1rem;
    --spacing-large: 2rem;
}
```

사용 방법

```css
.button {
    padding: var(--spacing-medium);
    background-color: var(--color-primary);
    color: white;
}
```

---

# :root

`:root`는 문서의 최상위 요소를 선택한다.

HTML 문서에서는 사실상 `<html>` 요소를 의미한다.

```css
:root {
    --color-primary: royalblue;
}
```

전역에서 사용할 색상, 크기, 간격 등을 선언하는 데 자주 사용한다.

---

# var()

`var()` 함수로 사용자 정의 속성값을 가져온다.

```css
.title {
    color: var(--color-primary);
}
```

기본값도 지정할 수 있다.

```css
.title {
    color: var(--color-primary, royalblue);
}
```

`--color-primary`가 정의되지 않았다면 `royalblue`를 사용한다.

---

# 디자인 토큰

색상과 단위를 변수로 관리하면 디자인 토큰처럼 사용할 수 있다.

```css
:root {
    --color-primary-500: #3b82f6;
    --color-primary-600: #2563eb;

    --color-gray-100: #f3f4f6;
    --color-gray-900: #111827;

    --font-size-small: 0.875rem;
    --font-size-base: 1rem;
    --font-size-large: 1.25rem;

    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-4: 1rem;
    --space-8: 2rem;
}
```

이러한 값은 프로젝트 전체의 시각적 일관성을 유지하는 데 도움이 된다.

---

# 접근성과 색상

색상은 디자인뿐만 아니라 정보 전달과 접근성에도 영향을 준다.

다음 사항을 고려해야 한다.

- 글자와 배경 사이의 충분한 명도 대비
- 색상 하나에만 의존하지 않는 상태 표현
- 링크와 일반 텍스트의 구분
- 포커스 표시의 명확성
- 비활성화 상태의 가독성

좋지 않은 예

```html
<p class="error">
    비밀번호를 확인하세요.
</p>
```

```css
.error {
    color: red;
}
```

색상만으로 오류를 표현하면 색을 구분하기 어려운 사용자가 상태를 인식하기 어려울 수 있다.

권장 예

```html
<p class="error">
    ⚠ 비밀번호를 확인하세요.
</p>
```

```css
.error {
    color: #b91c1c;
    font-weight: 700;
}
```

아이콘, 문구, 굵기 등을 함께 사용할 수 있다.

---

# 실무 활용

색상과 단위는 다음과 같은 상황에서 활용한다.

- 브랜드 색상 관리
- 디자인 시스템 구축
- 반응형 글자 크기
- 유동적인 컨테이너 너비
- 모바일 전체 화면 구성
- 버튼과 카드 간격
- 모달 오버레이
- 테마와 다크 모드
- 애니메이션 시간
- 회전과 그라디언트 각도

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

    <title>CSS 색상과 단위</title>

</head>

<body>

    <main class="main">

        <section class="hero">

            <div class="hero__content">

                <span class="hero__badge">
                    Frontend Course
                </span>

                <h1 class="hero__title">
                    Developer Academy
                </h1>

                <p class="hero__description">
                    HTML, CSS, JavaScript를 학습하여
                    실무형 웹 개발자로 성장합니다.
                </p>

                <a
                    href="#courses"
                    class="button"
                >
                    과정 살펴보기
                </a>

            </div>

        </section>

        <section
            id="courses"
            class="courses"
        >

            <h2 class="courses__title">
                교육 과정
            </h2>

            <article class="course-card">

                <h3 class="course-card__title">
                    CSS Basic
                </h3>

                <p class="course-card__description">
                    선택자, 색상, 단위, 레이아웃을 학습합니다.
                </p>

            </article>

        </section>

    </main>

</body>

</html>
```

## CSS

```css
:root {
    --color-primary: hsl(221 83% 53%);
    --color-primary-dark: hsl(224 76% 38%);
    --color-heading: hsl(222 47% 11%);
    --color-text: hsl(215 25% 27%);
    --color-surface: #ffffff;
    --color-background: hsl(210 40% 98%);
    --color-border: hsl(214 32% 91%);

    --space-small: 0.75rem;
    --space-medium: 1.5rem;
    --space-large: 3rem;

    --radius-medium: 0.75rem;
    --content-width: 75rem;
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
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

.hero {
    display: grid;
    min-height: 100dvh;
    padding: max(2rem, 5vw);
    background:
        linear-gradient(
            rgb(15 23 42 / 75%),
            rgb(15 23 42 / 75%)
        ),
        url("./images/hero.jpg") center / cover;
    color: white;
    place-items: center;
}

.hero__content {
    width: min(100%, 60rem);
    text-align: center;
}

.hero__badge {
    display: inline-block;
    padding: 0.5em 1em;
    border: 1px solid currentColor;
    border-radius: 999px;
    font-size: 0.875rem;
}

.hero__title {
    margin-block: 1.5rem 1rem;
    font-size: clamp(2.5rem, 8vw, 6rem);
    line-height: 1.1;
}

.hero__description {
    max-width: 45ch;
    margin-inline: auto;
    font-size: clamp(1rem, 2vw, 1.25rem);
}

.button {
    display: inline-block;
    margin-top: 2rem;
    padding: 0.875em 1.75em;
    border-radius: var(--radius-medium);
    background-color: var(--color-primary);
    color: white;
    font-weight: 700;
    text-decoration: none;
    transition: background-color 200ms;
}

.button:hover {
    background-color: var(--color-primary-dark);
}

.button:focus-visible {
    outline: 3px solid currentColor;
    outline-offset: 4px;
}

.courses {
    width: min(100% - 2rem, var(--content-width));
    margin-inline: auto;
    padding-block: clamp(4rem, 10vw, 8rem);
}

.courses__title {
    margin-top: 0;
    color: var(--color-heading);
    font-size: clamp(2rem, 5vw, 3.5rem);
}

.course-card {
    padding: clamp(1.5rem, 4vw, 3rem);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-medium);
    background-color: var(--color-surface);
    box-shadow: 0 1rem 3rem rgb(15 23 42 / 8%);
}

.course-card__title {
    margin-top: 0;
    color: var(--color-primary);
    font-size: 1.5rem;
}

.course-card__description {
    max-width: 60ch;
    margin-bottom: 0;
}
```

---

# 예제 분석

```css
--color-primary: hsl(221 83% 53%);
```

대표 색상을 CSS 사용자 정의 속성으로 관리한다.

```css
min-height: 100dvh;
```

모바일 브라우저의 현재 뷰포트 높이를 반영한다.

```css
padding: max(2rem, 5vw);
```

최소 `2rem`의 여백을 유지하면서 화면 크기에 따라 여백을 늘린다.

```css
width: min(100%, 60rem);
```

요소가 부모 너비를 넘지 않으면서 최대 `60rem`까지만 커지도록 한다.

```css
font-size: clamp(2.5rem, 8vw, 6rem);
```

화면 크기에 따라 제목 크기를 유동적으로 조정하면서 최소값과 최대값을 제한한다.

```css
max-width: 45ch;
```

본문 한 줄이 지나치게 길어지는 것을 방지한다.

```css
padding: 0.875em 1.75em;
```

버튼의 내부 여백을 글자 크기에 비례하여 설정한다.

```css
box-shadow: 0 1rem 3rem rgb(15 23 42 / 8%);
```

RGB 색상에 투명도를 적용하여 부드러운 그림자를 만든다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|---|---|
| Named Color | 이름으로 지정하는 색상 |
| HEX | 16진수 색상 표현 |
| RGB | 빨강, 초록, 파랑 기반 색상 |
| RGBA | RGB에 투명도를 추가한 색상 |
| HSL | 색상, 채도, 명도 기반 표현 |
| HSLA | HSL에 투명도를 추가한 표현 |
| Alpha | 색상의 투명도 |
| transparent | 완전히 투명한 색상 |
| currentColor | 현재 글자색 사용 |
| opacity | 요소 전체 투명도 |
| px | CSS 픽셀 단위 |
| em | 현재 글자 크기 기준 단위 |
| rem | 루트 글자 크기 기준 단위 |
| % | 관련 기준값에 대한 백분율 |
| vw | 뷰포트 너비 기준 단위 |
| vh | 뷰포트 높이 기준 단위 |
| dvh | 동적 뷰포트 높이 단위 |
| vmin | 뷰포트의 작은 쪽 기준 |
| vmax | 뷰포트의 큰 쪽 기준 |
| ch | 숫자 0의 글자 너비 기준 |
| deg | 각도 단위 |
| s / ms | 시간 단위 |
| calc() | CSS 값 계산 함수 |
| min() | 작은 값 선택 함수 |
| max() | 큰 값 선택 함수 |
| clamp() | 최소, 선호, 최대값 지정 함수 |
| Custom Property | CSS 사용자 정의 속성 |
| var() | 사용자 정의 속성 사용 함수 |
| Design Token | 반복되는 디자인 값을 체계화한 값 |

---

# 자주 하는 실수

## 1. HEX 색상의 샵을 생략한다

잘못된 예

```css
color: ff0000;
```

올바른 예

```css
color: #ff0000;
```

---

## 2. RGB 값의 범위를 잘못 이해한다

일반적인 RGB 채널값은 `0`부터 `255`까지 사용한다.

```css
color: rgb(255, 0, 0);
```

---

## 3. Alpha 값을 0부터 100으로 작성한다

기존 RGBA 문법에서는 다음과 같이 `0`부터 `1`을 사용한다.

```css
background-color: rgba(0, 0, 0, 0.5);
```

백분율 문법도 사용할 수 있다.

```css
background-color: rgb(0 0 0 / 50%);
```

---

## 4. opacity로 배경만 투명하게 만들려고 한다

```css
.card {
    opacity: 0.5;
}
```

자식 요소를 포함한 전체가 반투명해진다.

배경만 투명하게 하려면 다음처럼 색상의 Alpha 값을 사용한다.

```css
.card {
    background-color: rgb(0 0 0 / 50%);
}
```

---

## 5. em과 rem을 같은 기준으로 생각한다

- `em`: 현재 요소의 글자 크기와 관련
- `rem`: 루트 요소의 글자 크기 기준

---

## 6. em을 중첩하여 글자가 계속 커진다

부모의 글자 크기를 기준으로 반복 계산될 수 있다.

전체 글자 크기 체계에는 `rem`을 고려한다.

---

## 7. height: 100%가 항상 화면 전체 높이라고 생각한다

`height: 100%`는 부모의 높이가 명확해야 계산되는 경우가 많다.

화면 높이가 목적이라면 `100vh` 또는 `100dvh`를 검토한다.

---

## 8. vw만 사용하여 글자가 지나치게 작거나 커진다

```css
font-size: 8vw;
```

작은 화면이나 매우 큰 화면에서 읽기 어려운 크기가 될 수 있다.

다음처럼 최소값과 최대값을 제한한다.

```css
font-size: clamp(2rem, 8vw, 5rem);
```

---

## 9. calc() 연산자 주변의 공백을 생략한다

좋지 않은 예

```css
width: calc(100%-20px);
```

권장 예

```css
width: calc(100% - 20px);
```

---

## 10. 모든 값을 px로 고정한다

반응형 디자인과 사용자 설정 대응이 어려워질 수 있다.

요소의 목적에 따라 `%`, `rem`, `em`, 뷰포트 단위를 함께 사용한다.

---

## 11. line-height에 고정된 px만 사용한다

```css
body {
    line-height: 24px;
}
```

자식 요소의 글자 크기가 달라질 때 적절하지 않을 수 있다.

```css
body {
    line-height: 1.6;
}
```

단위 없는 값을 고려한다.

---

## 12. 색상만으로 상태를 전달한다

오류, 성공, 선택 상태 등을 색상만으로 표현하면 접근성이 떨어질 수 있다.

아이콘, 텍스트, 테두리, 굵기 등을 함께 사용한다.

---

## 13. 사용자 정의 속성 이름을 일관성 없이 작성한다

좋지 않은 예

```css
:root {
    --blue: #2563eb;
    --mainText: #111827;
    --large_space: 32px;
}
```

권장 예

```css
:root {
    --color-primary: #2563eb;
    --color-text: #111827;
    --space-large: 2rem;
}
```

---

## 14. CSS 사용자 정의 속성과 Sass 변수를 같은 것으로 생각한다

CSS 사용자 정의 속성은 브라우저에서 실행 시점에 계산되며 상속과 JavaScript 조작이 가능하다.

Sass 변수는 CSS로 변환되는 과정에서 처리된다.

---

## 15. currentColor를 별도의 고정 색상으로 생각한다

`currentColor`는 현재 요소에 적용된 `color` 값을 의미한다.

```css
.icon {
    color: royalblue;
    border-color: currentColor;
}
```

---

# 면접 포인트

### Q1. CSS에서 색상을 표현하는 방법에는 무엇이 있나요?

색상 이름, HEX, RGB, RGBA, HSL, HSLA 등의 방식이 있다.

---

### Q2. RGB와 HSL의 차이는 무엇인가요?

RGB는 빨강, 초록, 파랑의 강도를 기반으로 색을 표현한다.

HSL은 색상, 채도, 명도를 기준으로 색을 표현하므로 밝기와 채도를 조절하기 쉽다.

---

### Q3. opacity와 Alpha 색상의 차이는 무엇인가요?

`opacity`는 요소와 모든 자식의 투명도에 영향을 준다.

RGBA나 HSLA의 Alpha 값은 해당 색상에만 투명도를 적용한다.

---

### Q4. px, em, rem의 차이는 무엇인가요?

- `px`: 비교적 고정된 CSS 픽셀 단위
- `em`: 현재 요소의 글자 크기를 기준으로 하는 상대 단위
- `rem`: 루트 요소의 글자 크기를 기준으로 하는 상대 단위

---

### Q5. em보다 rem이 전체 글자 크기 관리에 유리한 이유는 무엇인가요?

`rem`은 부모 요소의 중첩에 영향을 받지 않고 항상 루트 요소를 기준으로 계산되므로 일관된 크기 체계를 만들기 쉽다.

---

### Q6. width: 50%는 무엇을 기준으로 계산하나요?

일반적으로 포함 블록, 즉 부모 요소의 콘텐츠 너비를 기준으로 계산한다.

---

### Q7. height: 100%가 동작하지 않는 이유는 무엇인가요?

부모 요소의 높이가 명확하게 지정되지 않으면 자식 요소가 백분율 높이의 기준을 계산하기 어려울 수 있기 때문이다.

---

### Q8. vw와 vh는 무엇인가요?

- `vw`: 뷰포트 너비의 1%
- `vh`: 뷰포트 높이의 1%

---

### Q9. vh와 dvh의 차이는 무엇인가요?

`vh`는 전통적인 뷰포트 높이 단위이고, `dvh`는 모바일 브라우저 UI의 변화까지 반영하는 동적 뷰포트 높이 단위이다.

---

### Q10. calc()는 언제 사용하나요?

서로 다른 CSS 단위를 조합하거나 전체 크기에서 특정 크기를 제외하는 등 계산된 값을 지정할 때 사용한다.

```css
width: calc(100% - 240px);
```

---

### Q11. clamp()는 어떻게 동작하나요?

최소값, 선호값, 최대값을 지정하여 값이 해당 범위 안에서 유동적으로 변하도록 한다.

```css
font-size: clamp(2rem, 5vw, 4rem);
```

---

### Q12. currentColor는 무엇인가요?

현재 요소에 적용된 `color` 속성값을 의미한다.

테두리, 아이콘, SVG 색상을 글자색과 일치시킬 때 유용하다.

---

### Q13. CSS 사용자 정의 속성은 무엇인가요?

`--이름` 형태로 선언하고 `var()` 함수로 사용하는 재사용 가능한 CSS 값이다.

```css
:root {
    --color-primary: royalblue;
}
```

```css
.button {
    background-color: var(--color-primary);
}
```

---

### Q14. ch 단위는 언제 유용한가요?

글자 너비를 기준으로 요소의 최대 너비를 제한할 때 유용하다.

본문의 한 줄 길이를 제한하는 용도로 자주 사용한다.

```css
.article {
    max-width: 65ch;
}
```

---

### Q15. 반응형 글자 크기를 구현하는 방법은 무엇인가요?

뷰포트 단위와 `clamp()`를 조합할 수 있다.

```css
font-size: clamp(2rem, 5vw, 4rem);
```

---

# 핵심 정리

- CSS 색상은 이름, HEX, RGB, HSL 등의 방식으로 표현할 수 있다.
- Alpha 값은 색상의 투명도를 조절한다.
- `opacity`는 자식 요소를 포함한 요소 전체에 영향을 준다.
- `currentColor`는 현재 요소의 글자색을 다른 속성에서 재사용한다.
- `px`는 고정된 크기에, `rem`은 전체 글자와 간격 체계에 유용하다.
- `em`은 현재 글자 크기에 비례하는 컴포넌트 크기를 만들 때 유용하다.
- `%`는 속성에 따라 기준이 달라질 수 있다.
- `vw`, `vh`, `dvh`는 뷰포트 크기를 기준으로 계산한다.
- `ch`는 본문의 읽기 좋은 줄 길이를 제한할 때 유용하다.
- `calc()`는 서로 다른 단위의 값을 계산할 수 있다.
- `min()`, `max()`, `clamp()`를 사용하면 유동적인 반응형 값을 만들 수 있다.
- CSS 사용자 정의 속성을 사용하면 색상과 간격을 일관성 있게 관리할 수 있다.
- 단위는 하나로 통일하기보다 목적에 따라 적절하게 선택해야 한다.
- 상태를 표현할 때 색상 하나에만 의존하지 않아야 한다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-22 | 최초 작성 |
| v1.0 | 2026-07-22 | 색상 이름, HEX, RGB, HSL 표현 방식 정리 |
| v1.0 | 2026-07-22 | Alpha, opacity, transparent, currentColor 설명 추가 |
| v1.0 | 2026-07-22 | 절대 단위와 상대 단위 비교 추가 |
| v1.0 | 2026-07-22 | px, em, rem, 백분율 단위 설명 추가 |
| v1.0 | 2026-07-22 | 뷰포트 및 동적 뷰포트 단위 정리 |
| v1.0 | 2026-07-22 | ch, 각도, 시간 단위 설명 추가 |
| v1.0 | 2026-07-22 | calc(), min(), max(), clamp() 함수 추가 |
| v1.0 | 2026-07-22 | CSS 사용자 정의 속성과 디자인 토큰 개념 추가 |
| v1.0 | 2026-07-22 | 접근성 및 실무 예제 프로젝트 추가 |
| v1.0 | 2026-07-22 | 자주 하는 실수와 면접 포인트 추가 |