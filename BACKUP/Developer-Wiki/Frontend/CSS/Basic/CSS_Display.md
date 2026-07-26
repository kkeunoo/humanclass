---
title: CSS Display
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS Display

## 개요

CSS의 `display` 속성은 요소가 화면에 어떻게 배치되고, 주변 요소와 어떤 방식으로 관계를 맺는지를 결정한다.

HTML 요소는 기본적으로 각 요소에 맞는 `display` 값을 가지고 있다.

예를 들어 다음 요소들은 일반적으로 블록 요소로 동작한다.

```html
<div>블록 요소</div>
<p>문단</p>
<section>섹션</section>
```

반면 다음 요소들은 일반적으로 인라인 요소로 동작한다.

```html
<span>인라인 요소</span>
<a href="#">링크</a>
<strong>강조</strong>
```

CSS에서는 `display` 속성을 사용하여 요소의 기본 배치 방식을 변경할 수 있다.

```css
a {
    display: block;
}
```

```css
div {
    display: inline;
}
```

하지만 단순히 요소를 줄바꿈시키거나 한 줄에 배치하는 것만으로 `display`를 이해했다고 보기 어렵다.

`display`는 다음과 같은 요소에 영향을 준다.

- 요소가 새 줄에서 시작하는지
- 요소가 사용 가능한 너비를 차지하는지
- `width`와 `height`가 적용되는지
- 상하 `margin`과 `padding`이 배치에 영향을 주는지
- 자식 요소의 배치 방식
- Flexbox 또는 Grid 컨테이너 생성 여부
- 문서 흐름 참여 여부
- 요소의 렌더링 여부
- 접근성 트리에 요소가 포함되는 방식

따라서 `display`는 CSS 레이아웃의 출발점이라고 할 수 있다.

---

# 핵심 개념

CSS Display에서 이해해야 할 주요 개념은 다음과 같다.

- Normal Flow
- Outer Display Type
- Inner Display Type
- Block Box
- Inline Box
- `display: block`
- `display: inline`
- `display: inline-block`
- `display: none`
- `display: flow-root`
- `display: list-item`
- `display: contents`
- `display: table`
- `display: flex`
- `display: inline-flex`
- `display: grid`
- `display: inline-grid`
- Block Formatting Context
- Inline Formatting Context
- Baseline
- Inline Whitespace
- Replaced Element
- `visibility`
- `opacity`
- 접근성과 렌더링 차이

---

# Normal Flow

Normal Flow는 CSS에서 별도의 위치 지정이나 특수한 레이아웃을 적용하지 않았을 때 요소가 배치되는 기본 흐름이다.

한국어의 일반적인 가로쓰기 문서에서는 다음과 같이 동작한다.

```text
블록 요소

↓

위에서 아래로 쌓임
```

```text
인라인 요소

↓

왼쪽에서 오른쪽으로 배치
```

HTML

```html
<div class="box">
    첫 번째 블록
</div>

<div class="box">
    두 번째 블록
</div>
```

CSS

```css
.box {
    border: 1px solid black;
}
```

두 `div` 요소는 위에서 아래로 배치된다.

HTML

```html
<span>HTML</span>
<span>CSS</span>
<span>JavaScript</span>
```

세 개의 `span` 요소는 같은 줄에 배치될 수 있다.

이러한 기본 흐름을 이해해야 `display`, `position`, `float`, Flexbox, Grid의 차이를 이해할 수 있다.

---

# display 속성의 역할

`display`는 크게 두 가지 관점으로 이해할 수 있다.

```text
요소가 바깥쪽에서 어떻게 배치되는가

+

요소의 자식이 내부에서 어떻게 배치되는가
```

이를 각각 다음과 같이 부른다.

- Outer Display Type
- Inner Display Type

---

# Outer Display Type

Outer Display Type은 요소 자신이 주변 요소와 어떤 방식으로 배치되는지를 결정한다.

대표적인 형태는 다음과 같다.

```text
block

inline
```

예를 들어 `display: block`은 요소 자신이 블록 박스로 배치되도록 한다.

```css
.element {
    display: block;
}
```

`display: inline`은 요소 자신이 인라인 박스로 배치되도록 한다.

```css
.element {
    display: inline;
}
```

---

# Inner Display Type

Inner Display Type은 요소의 자식들이 내부에서 어떤 레이아웃 방식으로 배치되는지를 결정한다.

대표적인 형태는 다음과 같다.

```text
flow

flex

grid
```

예를 들어 다음 요소는 바깥쪽에서는 블록 요소로 동작하면서 내부 자식은 Flexbox 방식으로 배치된다.

```css
.container {
    display: flex;
}
```

개념적으로는 다음과 같이 이해할 수 있다.

```text
바깥쪽

block

+

안쪽

flex
```

다음 코드는 바깥쪽에서는 인라인 요소처럼 배치되고 내부는 Flexbox가 된다.

```css
.container {
    display: inline-flex;
}
```

```text
바깥쪽

inline

+

안쪽

flex
```

---

# 기본 display 값

HTML 요소마다 브라우저 기본 스타일에 의해 서로 다른 `display` 값이 적용된다.

대표적인 예시는 다음과 같다.

| 요소 | 일반적인 기본 display |
|---|---|
| `div` | `block` |
| `p` | `block` |
| `section` | `block` |
| `article` | `block` |
| `header` | `block` |
| `footer` | `block` |
| `h1` ~ `h6` | `block` |
| `ul`, `ol` | `block` |
| `li` | `list-item` |
| `span` | `inline` |
| `a` | `inline` |
| `strong` | `inline` |
| `em` | `inline` |
| `img` | `inline` 계열의 Replaced Element |
| `button` | 브라우저에 따라 특수한 인라인 블록 형태 |
| `input` | 브라우저에 따라 특수한 인라인 블록 형태 |
| `table` | `table` |

브라우저와 요소 유형에 따라 세부 동작은 달라질 수 있다.

HTML 태그의 의미와 `display` 값은 별개의 개념이다.

```html
<span class="title">
    제목
</span>
```

```css
.title {
    display: block;
}
```

`span`이 블록처럼 표시되어도 HTML 의미가 `div`로 바뀌는 것은 아니다.

마찬가지로 다음 요소도 문서 의미는 여전히 제목이다.

```html
<h1 class="title">
    페이지 제목
</h1>
```

```css
.title {
    display: inline;
}
```

CSS는 시각적 배치 방식을 바꾸지만 HTML의 의미 구조를 변경하지 않는다.

---

# display: block

`display: block`은 요소를 블록 박스로 만든다.

```css
.element {
    display: block;
}
```

블록 요소의 일반적인 특징은 다음과 같다.

- 새 줄에서 시작한다.
- 사용 가능한 가로 공간을 채우는 방향으로 동작한다.
- `width`와 `height`를 지정할 수 있다.
- 상하좌우 `margin`과 `padding`이 배치에 영향을 준다.
- 블록 요소는 일반적으로 위에서 아래로 쌓인다.

---

# block 기본 예제

HTML

```html
<span class="item">
    HTML
</span>

<span class="item">
    CSS
</span>

<span class="item">
    JavaScript
</span>
```

CSS

```css
.item {
    display: block;
    border: 1px solid #333;
}
```

원래 `span`은 인라인 요소지만 `display: block`을 적용하면 각 요소가 새로운 줄에서 시작한다.

```text
HTML

CSS

JavaScript
```

---

# 블록 요소의 너비

블록 요소에서 `width`의 기본값은 일반적으로 `auto`이다.

```css
.box {
    display: block;
    width: auto;
}
```

`auto`인 블록 요소는 부모의 사용 가능한 공간을 채우는 방향으로 계산된다.

```html
<div class="container">
    <div class="box">
        콘텐츠
    </div>
</div>
```

```css
.container {
    width: 600px;
}

.box {
    display: block;
}
```

`box`는 일반적으로 부모의 사용 가능한 가로 공간을 차지한다.

---

# block과 width: 100% 차이

`width: auto`와 `width: 100%`는 항상 같은 의미가 아니다.

```css
.box {
    width: auto;
}
```

`auto`는 `margin`, `padding`, `border` 등을 고려해 사용 가능한 공간에 맞춰 계산된다.

반면 다음 코드는 Content 영역의 너비를 부모 너비의 `100%`로 설정할 수 있다.

```css
.box {
    width: 100%;
    padding: 20px;
}
```

`content-box`에서는 Padding이 추가되기 때문에 부모보다 커질 수 있다.

```css
.box {
    box-sizing: border-box;
    width: 100%;
    padding: 20px;
}
```

실무에서는 전역 `border-box` 설정과 함께 사용하는 경우가 많다.

---

# block과 margin-inline: auto

블록 요소를 가로 중앙에 배치할 때 다음 패턴을 자주 사용한다.

```css
.container {
    width: 800px;
    margin-inline: auto;
}
```

요소의 계산된 너비가 부모보다 작아야 남는 공간이 발생한다.

```css
.container {
    max-width: 800px;
    margin-inline: auto;
}
```

반면 요소가 부모의 전체 너비를 차지하면 중앙 정렬의 시각적 변화가 없을 수 있다.

```css
.container {
    width: auto;
    margin-inline: auto;
}
```

---

# display: inline

`display: inline`은 요소를 인라인 박스로 만든다.

```css
.element {
    display: inline;
}
```

인라인 요소의 일반적인 특징은 다음과 같다.

- 텍스트 흐름 안에 배치된다.
- 앞뒤 요소와 같은 줄에 배치될 수 있다.
- 콘텐츠 크기만큼 너비를 차지한다.
- 일반적으로 `width`와 `height`가 적용되지 않는다.
- 좌우 `margin`과 `padding`은 적용된다.
- 상하 `margin`은 일반적인 줄 배치에 기대한 방식으로 영향을 주지 않을 수 있다.
- 상하 `padding`과 `border`는 시각적으로 표시되지만 줄 높이와 주변 배치가 예상과 다를 수 있다.

---

# inline 기본 예제

HTML

```html
<div class="item">
    HTML
</div>

<div class="item">
    CSS
</div>

<div class="item">
    JavaScript
</div>
```

CSS

```css
.item {
    display: inline;
    border: 1px solid #333;
}
```

원래 `div`는 블록 요소지만 `display: inline`을 적용하면 한 줄 안에 나란히 배치될 수 있다.

```text
HTML CSS JavaScript
```

---

# inline과 width

다음 코드는 일반적인 인라인 요소에서 의도대로 동작하지 않는다.

```css
.link {
    display: inline;
    width: 200px;
    height: 100px;
}
```

인라인 요소는 콘텐츠 흐름 안에서 텍스트처럼 배치되기 때문에 일반적인 `width`와 `height`가 적용되지 않는다.

HTML

```html
<a
    href="#"
    class="link"
>
    문서 읽기
</a>
```

CSS

```css
.link {
    display: inline;
    width: 300px;
}
```

링크의 너비는 여전히 텍스트 콘텐츠 크기에 따라 결정될 수 있다.

크기를 지정하고 싶다면 `inline-block` 또는 `block`을 고려한다.

```css
.link {
    display: inline-block;
    width: 300px;
}
```

---

# inline과 상하 Margin

다음 코드는 상하 간격이 기대한 방식으로 적용되지 않을 수 있다.

```css
.link {
    display: inline;
    margin-top: 30px;
    margin-bottom: 30px;
}
```

인라인 요소는 줄 상자 안에서 배치되므로 상하 Margin이 주변 줄의 배치에 일반 블록처럼 영향을 주지 않는다.

좌우 Margin은 적용된다.

```css
.link {
    margin-inline: 1rem;
}
```

---

# inline과 Padding

인라인 요소에도 Padding을 적용할 수 있다.

```css
.highlight {
    padding: 0.25em 0.5em;
    background-color: yellow;
}
```

하지만 인라인 요소가 여러 줄로 나뉘면 Padding과 배경이 각 줄에 걸쳐 예상과 다르게 표현될 수 있다.

HTML

```html
<p>
    이 문장에서
    <span class="highlight">
        매우 긴 강조 텍스트가 여러 줄에 걸쳐 표시됩니다.
    </span>
</p>
```

여러 줄 인라인 장식을 각 조각에 복제하려면 다음 속성을 사용할 수 있다.

```css
.highlight {
    padding: 0.2em 0.4em;
    background-color: yellow;
    box-decoration-break: clone;
    -webkit-box-decoration-break: clone;
}
```

---

# Inline Formatting Context

인라인 요소와 텍스트는 Inline Formatting Context 안에서 배치된다.

인라인 콘텐츠는 줄 상자(Line Box)를 형성하며 한 줄의 공간이 부족하면 다음 줄로 이동한다.

```html
<p>
    HTML
    <strong>CSS</strong>
    JavaScript
    React
</p>
```

다음 항목들이 줄의 높이와 배치에 영향을 줄 수 있다.

- `font-size`
- `line-height`
- 인라인 요소의 `vertical-align`
- 이미지의 고유 크기
- 위아래 Padding과 Border
- 기준선

---

# Line Box

Line Box는 인라인 콘텐츠 한 줄이 차지하는 가상의 사각형 영역이다.

예를 들어 다음 텍스트는 한 줄 안에서 여러 인라인 박스로 구성될 수 있다.

```html
<p>
    HTML
    <span>CSS</span>
    <strong>JavaScript</strong>
</p>
```

브라우저는 각 인라인 박스의 글꼴, 높이, 기준선 등을 고려하여 줄 상자의 높이를 계산한다.

---

# Baseline

Baseline은 글자가 정렬되는 기준선이다.

```text
HTML CSS JavaScript
-------------------
       Baseline
```

인라인 요소, 이미지, `inline-block` 요소는 기본적으로 기준선에 맞춰 정렬될 수 있다.

이 때문에 이미지 아래에 작은 여백처럼 보이는 공간이 생길 수 있다.

HTML

```html
<div class="image-wrapper">
    <img
        src="./image.jpg"
        alt=""
    >
</div>
```

이미지가 인라인 요소처럼 기준선에 정렬되면 글자의 아래쪽 공간을 위한 여백이 남을 수 있다.

다음과 같이 해결할 수 있다.

```css
img {
    display: block;
}
```

또는 다음 방법도 가능하다.

```css
img {
    vertical-align: middle;
}
```

이미지 레이아웃에서는 `display: block`을 자주 사용한다.

---

# vertical-align

`vertical-align`은 인라인 요소, 인라인 블록 요소, 테이블 셀의 세로 정렬에 사용한다.

```css
.icon {
    vertical-align: middle;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `baseline` | 기준선에 맞춤 |
| `middle` | 가운데 부근에 맞춤 |
| `top` | 줄 상자의 위쪽에 맞춤 |
| `bottom` | 줄 상자의 아래쪽에 맞춤 |
| `text-top` | 부모 글꼴의 위쪽에 맞춤 |
| `text-bottom` | 부모 글꼴의 아래쪽에 맞춤 |
| `sub` | 아래 첨자 위치 |
| `super` | 위 첨자 위치 |

일반 블록 요소를 컨테이너의 세로 중앙에 배치하는 용도로 사용하는 속성은 아니다.

```css
.box {
    vertical-align: middle;
}
```

일반적인 블록 레이아웃에서는 위 코드만으로 세로 중앙 정렬되지 않는다.

세로 중앙 정렬에는 Flexbox 또는 Grid를 사용한다.

```css
.container {
    display: flex;
    align-items: center;
}
```

---

# display: inline-block

`display: inline-block`은 인라인 요소와 블록 요소의 특징을 일부 결합한 값이다.

```css
.element {
    display: inline-block;
}
```

주요 특징은 다음과 같다.

- 요소끼리 같은 줄에 배치될 수 있다.
- `width`와 `height`를 지정할 수 있다.
- 상하좌우 `padding`과 `margin`이 적용된다.
- 내부에서는 일반적인 블록 컨테이너처럼 콘텐츠를 배치할 수 있다.
- 기본적으로 기준선에 맞춰 정렬될 수 있다.
- HTML 공백이 요소 사이 간격으로 나타날 수 있다.

---

# inline-block 기본 예제

HTML

```html
<a
    href="#"
    class="button"
>
    확인
</a>

<a
    href="#"
    class="button"
>
    취소
</a>
```

CSS

```css
.button {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    border: 1px solid #2563eb;
    border-radius: 0.5rem;
    text-decoration: none;
}
```

두 링크는 같은 줄에 배치될 수 있으며 Padding과 크기를 정상적으로 가질 수 있다.

---

# inline-block과 width, height

```css
.item {
    display: inline-block;
    width: 200px;
    height: 100px;
}
```

`inline`과 달리 지정한 너비와 높이를 사용할 수 있다.

```html
<span class="item">
    HTML
</span>

<span class="item">
    CSS
</span>
```

두 요소가 한 줄에 배치되면서 각각 고정된 크기를 가질 수 있다.

---

# inline-block의 공백 문제

HTML 코드에서 `inline-block` 요소 사이에 공백이나 줄바꿈이 있으면 화면에도 작은 간격이 나타날 수 있다.

```html
<div class="item">HTML</div>
<div class="item">CSS</div>
<div class="item">JavaScript</div>
```

```css
.item {
    display: inline-block;
    width: 33.3333%;
}
```

각 요소의 너비 합계가 `100%`이더라도 HTML의 공백 때문에 마지막 요소가 다음 줄로 내려갈 수 있다.

```text
33.3333%
+
33.3333%
+
33.3333%
+
HTML 공백
```

---

# inline-block 공백 해결 방법

## HTML 요소 사이의 공백 제거

```html
<div class="item">HTML</div><div class="item">CSS</div><div class="item">JavaScript</div>
```

가독성이 떨어질 수 있다.

---

## 부모 font-size를 0으로 설정

```css
.container {
    font-size: 0;
}

.item {
    display: inline-block;
    width: 33.3333%;
    font-size: 1rem;
}
```

자식 글자 크기를 다시 설정해야 하며 유지보수에 주의해야 한다.

---

## Flexbox 사용

```css
.container {
    display: flex;
}

.item {
    flex: 1;
}
```

현대적인 레이아웃에서는 Flexbox나 Grid를 사용하는 것이 더 일반적이다.

---

# inline-block과 Baseline

`inline-block` 요소는 기본적으로 기준선에 맞춰 정렬될 수 있다.

```html
<div class="item item-small">
    작은 요소
</div>

<div class="item item-large">
    큰 요소
</div>
```

```css
.item {
    display: inline-block;
}
```

요소의 아래쪽이 정확히 맞지 않는 것처럼 보일 수 있다.

다음과 같이 정렬 기준을 지정할 수 있다.

```css
.item {
    display: inline-block;
    vertical-align: top;
}
```

또는

```css
.item {
    vertical-align: middle;
}
```

---

# block, inline, inline-block 비교

| 구분 | block | inline | inline-block |
|---|---|---|---|
| 새 줄에서 시작 | O | X | X |
| 같은 줄 배치 | 일반적으로 X | O | O |
| 기본 너비 | 사용 가능한 공간 | 콘텐츠 너비 | 콘텐츠 너비 |
| width 적용 | O | 일반적으로 X | O |
| height 적용 | O | 일반적으로 X | O |
| 좌우 Margin | O | O | O |
| 상하 Margin | O | 배치 영향 제한적 | O |
| Padding | O | 적용되지만 줄 배치 주의 | O |
| 기본 정렬 기준 | 블록 흐름 | Baseline | Baseline |

---

# display: none

`display: none`은 요소를 렌더링하지 않고 문서 레이아웃에서도 제거한다.

```css
.element {
    display: none;
}
```

요소가 차지하던 공간도 사라진다.

HTML

```html
<div class="notice">
    공지사항
</div>

<div class="content">
    본문
</div>
```

CSS

```css
.notice {
    display: none;
}
```

`content` 요소는 `notice`가 없었던 것처럼 위쪽으로 이동한다.

---

# display: none의 특징

- 화면에 표시되지 않는다.
- 레이아웃 공간을 차지하지 않는다.
- 자식 요소도 함께 표시되지 않는다.
- 일반적으로 접근성 트리에서도 제외된다.
- 포커스를 받을 수 없다.
- 화면 판독기가 읽지 않는 경우가 일반적이다.
- JavaScript를 통해 다시 표시할 수 있다.

```javascript
const menu = document.querySelector('.menu');

menu.style.display = 'block';
```

다만 JavaScript로 직접 인라인 스타일을 지정하면 기존 CSS 구조를 덮어쓸 수 있으므로 클래스를 변경하는 방식이 더 관리하기 쉽다.

```javascript
menu.classList.add('is-open');
```

```css
.menu {
    display: none;
}

.menu.is-open {
    display: block;
}
```

---

# display 값을 JavaScript로 복원할 때의 문제

다음 코드는 요소의 원래 `display` 값이 무엇인지 모르는 문제가 있다.

```javascript
element.style.display = 'block';
```

원래 요소가 `flex`, `grid`, `inline-block`이었을 수도 있다.

권장 방식은 상태 클래스로 제어하는 것이다.

```css
.navigation {
    display: flex;
}

.navigation.is-hidden {
    display: none;
}
```

```javascript
navigation.classList.toggle('is-hidden');
```

또는 `hidden` 속성을 활용할 수 있다.

```html
<nav hidden>
    ...
</nav>
```

브라우저 기본 스타일은 일반적으로 다음과 유사하다.

```css
[hidden] {
    display: none;
}
```

---

# hidden 속성

HTML의 `hidden` 속성은 현재 관련이 없거나 표시하지 않아야 하는 콘텐츠를 숨길 때 사용할 수 있다.

```html
<section hidden>
    숨겨진 콘텐츠
</section>
```

JavaScript

```javascript
const panel = document.querySelector('.panel');

panel.hidden = false;
```

```javascript
panel.hidden = true;
```

단순 표시 상태를 제어할 때 의미가 분명하고 편리하다.

다만 CSS에서 다음처럼 재정의하면 `hidden` 요소가 보일 수 있으므로 주의해야 한다.

```css
.panel {
    display: block;
}
```

특수성을 고려하여 다음과 같은 기본 규칙을 유지할 수 있다.

```css
[hidden] {
    display: none !important;
}
```

`!important` 사용 여부는 프로젝트 규칙에 따라 결정한다.

---

# display: none과 애니메이션

`display` 속성은 일반적으로 `opacity`처럼 부드럽게 보간되는 속성이 아니다.

다음 코드는 기대한 페이드 효과를 만들지 못한다.

```css
.modal {
    display: none;
    transition: display 300ms;
}

.modal.is-open {
    display: block;
}
```

일반적으로 `opacity`, `visibility`, `transform` 등을 함께 사용한다.

```css
.modal {
    visibility: hidden;
    opacity: 0;
    transform: translateY(1rem);
    pointer-events: none;
    transition:
        opacity 200ms,
        transform 200ms,
        visibility 200ms;
}

.modal.is-open {
    visibility: visible;
    opacity: 1;
    transform: translateY(0);
    pointer-events: auto;
}
```

상황에 따라 애니메이션이 끝난 뒤 `hidden`이나 `display: none`을 적용하는 JavaScript 처리가 필요할 수 있다.

---

# visibility

`visibility`는 요소의 가시성을 제어한다.

```css
.element {
    visibility: hidden;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `visible` | 요소 표시 |
| `hidden` | 요소 숨김 |
| `collapse` | 일부 테이블 요소에서 공간 축소 |

---

# visibility: hidden

`visibility: hidden`은 요소를 보이지 않게 하지만 일반적으로 레이아웃 공간은 유지한다.

```css
.notice {
    visibility: hidden;
}
```

주요 특징은 다음과 같다.

- 화면에 보이지 않는다.
- 요소의 레이아웃 공간은 남는다.
- 일반적으로 포인터로 상호작용할 수 없다.
- 접근성 트리에서 제외될 수 있다.
- 자식 요소에서 `visibility: visible`을 지정하면 보이게 만들 수 있는 경우가 있다.

---

# display: none과 visibility: hidden 비교

| 구분 | display: none | visibility: hidden |
|---|---|---|
| 화면 표시 | X | X |
| 레이아웃 공간 | 제거 | 유지 |
| 자식 표시 | 모두 제거 | 자식이 별도로 visible 가능 |
| 포커스 | 불가능 | 일반적으로 불가능 |
| 접근성 트리 | 일반적으로 제외 | 일반적으로 제외 |
| 전환 활용 | 제한적 | opacity와 조합 가능 |

---

# opacity

`opacity`는 요소 전체의 투명도를 조절한다.

```css
.element {
    opacity: 0;
}
```

`opacity: 0`이면 화면에 보이지 않지만 요소 자체는 여전히 존재한다.

주요 특징은 다음과 같다.

- 레이아웃 공간을 유지한다.
- 포인터 이벤트를 받을 수 있다.
- 키보드 포커스를 받을 수 있다.
- 접근성 트리에 남아 있을 수 있다.
- 자식 요소 전체가 함께 투명해진다.
- Transition을 적용할 수 있다.

---

# opacity: 0의 상호작용 문제

다음 요소는 보이지 않지만 클릭될 수 있다.

```css
.button {
    opacity: 0;
}
```

보이지 않는 요소가 클릭을 가로채는 문제가 발생할 수 있다.

필요하다면 다음을 함께 사용한다.

```css
.button {
    opacity: 0;
    pointer-events: none;
}
```

키보드 포커스와 접근성까지 함께 제어하려면 `hidden`, `inert`, `aria-hidden`, 실제 DOM 상태 등을 목적에 맞게 고려해야 한다.

단순히 `opacity: 0`만으로 콘텐츠를 완전히 숨겼다고 판단하면 안 된다.

---

# display, visibility, opacity 비교

| 속성 | 표시 | 공간 | 클릭 가능성 | 포커스 가능성 | 전환 |
|---|---|---|---|---|---|
| `display: none` | X | X | X | X | 직접 전환 제한적 |
| `visibility: hidden` | X | O | 일반적으로 X | 일반적으로 X | 가능 |
| `opacity: 0` | X | O | 가능 | 가능 | 가능 |

---

# display: list-item

`display: list-item`은 요소를 목록 항목처럼 표시한다.

```css
.element {
    display: list-item;
}
```

`li` 요소의 기본 Display 방식이다.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
</ul>
```

목록 항목에는 Marker Box가 생성될 수 있다.

```text
• HTML
• CSS
```

---

# list-style

목록 마커는 다음 속성으로 제어할 수 있다.

```css
.list {
    list-style: none;
}
```

```css
.list {
    list-style-type: square;
}
```

```css
.list {
    list-style-position: inside;
}
```

대표적인 속성은 다음과 같다.

| 속성 | 설명 |
|---|---|
| `list-style-type` | 마커 형태 |
| `list-style-position` | 마커 위치 |
| `list-style-image` | 이미지 마커 |
| `list-style` | 목록 스타일 속기 |

---

# ::marker

`::marker` 가상 요소를 사용하면 목록 마커를 스타일링할 수 있다.

```css
li::marker {
    color: royalblue;
    font-size: 1.2em;
}
```

```css
li::marker {
    content: "✓ ";
}
```

브라우저 지원과 적용 가능한 속성을 확인해야 한다.

---

# display: flow-root

`display: flow-root`는 요소가 새로운 Block Formatting Context를 생성하도록 한다.

```css
.container {
    display: flow-root;
}
```

주요 활용은 다음과 같다.

- Float된 자식의 높이를 부모가 포함하도록 함
- 자식 Margin과 부모 Margin의 상쇄 방지
- 외부 Float의 영향을 차단
- 독립적인 블록 레이아웃 영역 생성

---

# Block Formatting Context

Block Formatting Context는 블록 요소가 배치되는 독립적인 레이아웃 영역이다.

BFC 내부의 요소 배치는 외부 레이아웃과 일정 부분 분리된다.

다음과 같은 조건에서 새로운 BFC가 생성될 수 있다.

- `display: flow-root`
- `float`가 `none`이 아닌 요소
- 절대 위치 또는 고정 위치 요소
- `overflow`가 `visible`, `clip`이 아닌 블록 요소
- Flex Item
- Grid Item
- `display: inline-block`
- 일부 Table 관련 Display 값

모든 생성 조건을 외우기보다 BFC의 대표적인 효과를 이해하는 것이 중요하다.

---

# Float 부모 높이 문제

HTML

```html
<div class="container">

    <img
        src="./profile.jpg"
        alt=""
        class="profile"
    >

</div>
```

CSS

```css
.profile {
    float: left;
}
```

Float된 요소는 일반적인 블록 흐름에서 빠지므로 부모가 자식 높이를 포함하지 못하는 것처럼 보일 수 있다.

```css
.container {
    display: flow-root;
}
```

부모가 새로운 BFC를 생성하면 Float된 자식을 포함할 수 있다.

과거에는 다음과 같은 Clearfix 방식을 많이 사용했다.

```css
.container::after {
    display: block;
    clear: both;
    content: "";
}
```

현대 CSS에서는 `flow-root`가 의도를 더 직접적으로 표현한다.

---

# Margin Collapsing과 flow-root

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
    margin-top: 3rem;
}
```

부모와 첫 자식 사이에서 세로 Margin이 상쇄될 수 있다.

```css
.section {
    display: flow-root;
}
```

새로운 BFC를 생성하여 자식 Margin이 부모 밖으로 합쳐지는 것을 방지할 수 있다.

내부 여백이 목적이라면 부모의 Padding을 사용하는 방법이 더 자연스러울 수도 있다.

---

# flow-root와 overflow: hidden

과거에는 BFC를 만들기 위해 다음 코드를 사용하기도 했다.

```css
.container {
    overflow: hidden;
}
```

하지만 이 방식은 자식의 그림자, 드롭다운, 포커스 Outline 등을 잘라낼 수 있다.

BFC 생성만이 목적이라면 다음이 더 명확하다.

```css
.container {
    display: flow-root;
}
```

---

# display: contents

`display: contents`는 요소 자신의 박스를 생성하지 않고 자식 요소들이 부모의 자식처럼 배치되도록 한다.

```css
.wrapper {
    display: contents;
}
```

HTML

```html
<div class="grid">

    <div class="wrapper">

        <article class="card">
            HTML
        </article>

        <article class="card">
            CSS
        </article>

    </div>

</div>
```

CSS

```css
.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
}

.wrapper {
    display: contents;
}
```

`wrapper` 자신의 박스는 사라지고 `card` 요소들이 Grid Item처럼 참여할 수 있다.

---

# display: contents의 주의점

요소의 박스가 생성되지 않기 때문에 해당 요소에 적용한 다음 스타일은 시각적으로 기대한 효과를 내지 못할 수 있다.

- `background`
- `border`
- `padding`
- `margin`
- `box-shadow`
- `width`
- `height`

```css
.wrapper {
    display: contents;
    padding: 2rem;
    background-color: yellow;
}
```

`wrapper` 박스가 존재하지 않으므로 Padding과 배경이 표시되지 않는다.

---

# display: contents와 접근성

일부 브라우저와 보조 기술 조합에서는 `display: contents`가 접근성 트리에 영향을 준 사례가 있었다.

의미 있는 요소에 무조건 적용하기보다 실제 지원 환경을 확인해야 한다.

특히 다음 요소에 사용할 때 주의한다.

- 버튼
- 링크
- 목록
- 표 관련 요소
- Form 관련 요소
- 중요한 Landmark 요소

단순한 시각적 Wrapper를 제거하는 용도로 제한적으로 사용하는 것이 안전하다.

HTML 의미 구조를 수정할 수 있다면 불필요한 Wrapper 자체를 제거하는 것이 더 명확할 수 있다.

---

# display: table

`display: table`은 요소를 표 레이아웃과 유사하게 동작하도록 만든다.

```css
.element {
    display: table;
}
```

관련 값은 다음과 같다.

| 값 | 역할 |
|---|---|
| `table` | `table` 요소와 유사 |
| `inline-table` | 인라인 수준의 Table |
| `table-row` | `tr`과 유사 |
| `table-row-group` | `tbody`와 유사 |
| `table-header-group` | `thead`와 유사 |
| `table-footer-group` | `tfoot`과 유사 |
| `table-cell` | `td`, `th`와 유사 |
| `table-caption` | `caption`과 유사 |
| `table-column` | `col`과 유사 |
| `table-column-group` | `colgroup`과 유사 |

---

# CSS Table Layout 예제

HTML

```html
<div class="table">

    <div class="table-row">

        <div class="table-cell">
            이름
        </div>

        <div class="table-cell">
            과정
        </div>

    </div>

    <div class="table-row">

        <div class="table-cell">
            홍길동
        </div>

        <div class="table-cell">
            CSS
        </div>

    </div>

</div>
```

CSS

```css
.table {
    display: table;
    width: 100%;
}

.table-row {
    display: table-row;
}

.table-cell {
    display: table-cell;
    padding: 1rem;
    border: 1px solid #ddd;
}
```

시각적으로 표처럼 배치할 수 있다.

하지만 실제 표 데이터라면 CSS만으로 `div`를 표처럼 만들기보다 의미에 맞는 HTML `table` 요소를 사용해야 한다.

```html
<table>
    ...
</table>
```

CSS Display는 시각적 배치를 변경할 뿐 의미와 접근성 정보를 자동으로 추가하지 않는다.

---

# display: flex

`display: flex`는 요소를 블록 수준의 Flex Container로 만든다.

```css
.container {
    display: flex;
}
```

자식 요소는 Flex Item이 된다.

```html
<div class="container">

    <div class="item">
        HTML
    </div>

    <div class="item">
        CSS
    </div>

</div>
```

주요 특징은 다음과 같다.

- 바깥쪽에서는 블록 요소처럼 동작한다.
- 내부 자식은 Flex Layout으로 배치된다.
- 주축과 교차축을 기준으로 정렬한다.
- 요소의 순서와 간격을 유연하게 제어할 수 있다.
- 기본적으로 자식은 가로 방향으로 배치된다.

```css
.container {
    display: flex;
    gap: 1rem;
}
```

Flexbox의 상세 내용은 별도의 문서에서 다룬다.

---

# display: inline-flex

`display: inline-flex`는 요소 자신은 인라인 수준으로 배치되고 내부는 Flexbox로 동작한다.

```css
.container {
    display: inline-flex;
}
```

예를 들어 아이콘과 텍스트가 포함된 배지를 만들 수 있다.

HTML

```html
<span class="badge">

    <span aria-hidden="true">
        ✓
    </span>

    완료

</span>
```

CSS

```css
.badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5em 1em;
    border-radius: 999px;
    background-color: #dcfce7;
}
```

배지는 콘텐츠 크기만큼 너비를 차지하면서 내부 아이콘과 텍스트는 Flexbox로 정렬된다.

---

# flex와 inline-flex 비교

| 구분 | flex | inline-flex |
|---|---|---|
| 외부 배치 | Block 수준 | Inline 수준 |
| 내부 배치 | Flex | Flex |
| 기본 너비 | 사용 가능한 공간 | 콘텐츠 크기 |
| 같은 줄 배치 | 일반적으로 X | 가능 |
| 자식 | Flex Item | Flex Item |

---

# display: grid

`display: grid`는 요소를 블록 수준의 Grid Container로 만든다.

```css
.container {
    display: grid;
}
```

자식 요소는 Grid Item이 된다.

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}
```

주요 특징은 다음과 같다.

- 바깥쪽에서는 블록 요소처럼 동작한다.
- 내부 자식은 행과 열 기반으로 배치된다.
- 2차원 레이아웃을 구성하기 좋다.
- 요소의 위치와 크기를 명시적으로 제어할 수 있다.
- 암시적 행과 열이 생성될 수 있다.

Grid의 상세 내용은 별도의 문서에서 다룬다.

---

# display: inline-grid

`display: inline-grid`는 요소 자신은 인라인 수준으로 배치되고 내부는 Grid Layout으로 동작한다.

```css
.container {
    display: inline-grid;
}
```

예제

```html
<span class="icon-grid">

    <span>1</span>
    <span>2</span>
    <span>3</span>
    <span>4</span>

</span>
```

```css
.icon-grid {
    display: inline-grid;
    grid-template-columns: repeat(2, 1rem);
    gap: 0.25rem;
}
```

---

# grid와 inline-grid 비교

| 구분 | grid | inline-grid |
|---|---|---|
| 외부 배치 | Block 수준 | Inline 수준 |
| 내부 배치 | Grid | Grid |
| 기본 너비 | 사용 가능한 공간 | 콘텐츠 크기 |
| 같은 줄 배치 | 일반적으로 X | 가능 |
| 자식 | Grid Item | Grid Item |

---

# 다중 키워드 display 문법

현대 CSS에서는 `display` 값을 외부와 내부 유형으로 나누어 작성할 수 있다.

```css
.element {
    display: block flex;
}
```

의미는 다음과 같다.

```text
바깥쪽

block

+

안쪽

flex
```

기존 문법과 비교하면 다음과 유사하다.

```css
.element {
    display: flex;
}
```

인라인 수준 Flex Container는 다음처럼 작성할 수 있다.

```css
.element {
    display: inline flex;
}
```

기존 문법은 다음과 같다.

```css
.element {
    display: inline-flex;
}
```

Grid도 같은 방식으로 표현할 수 있다.

```css
.element {
    display: block grid;
}
```

```css
.element {
    display: inline grid;
}
```

실무에서는 브라우저 지원 범위와 팀 규칙을 고려해 기존 단일 키워드 문법을 계속 사용하는 경우가 많다.

---

# Replaced Element

Replaced Element는 요소의 내부 콘텐츠가 일반적인 CSS 박스 생성 방식이 아니라 외부 리소스나 브라우저의 특별한 표현으로 대체되는 요소이다.

대표적인 예시는 다음과 같다.

- `img`
- `video`
- `iframe`
- `embed`
- 일부 `input` 요소

```html
<img
    src="./image.jpg"
    alt="예제 이미지"
>
```

이미지는 원본 너비, 높이, 비율을 가질 수 있다.

---

# 이미지의 display

`img`는 일반적으로 인라인 수준 요소처럼 텍스트 기준선에 맞춰 배치된다.

```css
img {
    display: inline;
}
```

이미지 아래에 작은 여백이 보이는 문제를 해결하고, 레이아웃 요소로 사용하기 위해 다음 스타일을 자주 적용한다.

```css
img {
    display: block;
    max-width: 100%;
    height: auto;
}
```

---

# object-fit

Replaced Element의 콘텐츠를 지정된 박스 안에서 어떻게 맞출지 결정한다.

```css
.thumbnail img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `fill` | 박스에 맞게 늘림 |
| `contain` | 전체 콘텐츠가 보이도록 맞춤 |
| `cover` | 박스를 채우도록 확대하고 일부 잘라냄 |
| `none` | 원본 크기 유지 |
| `scale-down` | `none`과 `contain` 중 작은 결과 사용 |

---

# display와 Semantic HTML

`display`를 변경해도 HTML의 의미는 바뀌지 않는다.

다음 코드는 링크를 블록 요소로 만들지만 여전히 링크이다.

```html
<a
    href="/courses"
    class="course-card"
>
    과정 보기
</a>
```

```css
.course-card {
    display: block;
}
```

다음 코드는 `div`를 버튼처럼 보이게 만들지만 실제 버튼은 아니다.

```html
<div class="button">
    저장
</div>
```

```css
.button {
    display: inline-block;
    padding: 1rem 2rem;
    background-color: royalblue;
    color: white;
}
```

마우스로 클릭 가능하게 만들더라도 다음 기능이 자동으로 제공되지 않는다.

- 키보드 포커스
- Enter 또는 Space 활성화
- 버튼 역할 전달
- 비활성화 상태
- Form 제출 기능

실제 동작이 버튼이라면 다음처럼 작성한다.

```html
<button type="button">
    저장
</button>
```

CSS는 의미 있는 HTML 요소를 원하는 형태로 표시하는 데 사용해야 한다.

---

# display와 접근성

요소를 숨기거나 표시 방식을 변경할 때는 시각적 결과뿐 아니라 접근성도 고려해야 한다.

특히 다음 속성은 동작이 다르다.

- `display: none`
- `visibility: hidden`
- `opacity: 0`
- `hidden`
- `aria-hidden`
- `inert`

---

# aria-hidden

`aria-hidden="true"`는 해당 요소를 보조 기술의 접근성 트리에서 숨기도록 요청한다.

```html
<span aria-hidden="true">
    ★
</span>
```

하지만 시각적으로는 그대로 표시된다.

```text
시각 사용자

보임

스크린 리더

일반적으로 무시
```

`aria-hidden`은 CSS의 표시 여부를 제어하지 않는다.

```html
<div aria-hidden="true">
    시각적으로는 보이는 콘텐츠
</div>
```

포커스 가능한 요소에 `aria-hidden="true"`를 적용하면 키보드 사용자는 포커스할 수 있는데 화면 판독기에서는 의미를 알 수 없는 문제가 생길 수 있다.

---

# inert

`inert` 속성은 요소와 하위 콘텐츠가 사용자 상호작용 및 포커스 대상이 되지 않도록 할 때 사용할 수 있다.

```html
<main inert>
    ...
</main>
```

모달이 열린 동안 배경 콘텐츠의 포커스와 상호작용을 막는 상황에 활용할 수 있다.

다만 표시 상태 자체를 숨기는 속성은 아니다.

```text
inert

상호작용 차단

display

렌더링 방식 결정
```

---

# 시각적으로만 숨기기

화면에서는 숨기되 화면 판독기에는 제공해야 하는 콘텐츠가 있을 수 있다.

예를 들어 아이콘 버튼의 텍스트 레이블이다.

```html
<button type="button">

    <span aria-hidden="true">
        🔍
    </span>

    <span class="visually-hidden">
        검색
    </span>

</button>
```

CSS

```css
.visually-hidden {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    overflow: hidden;
    border: 0;
    margin: -1px;
    clip-path: inset(50%);
    white-space: nowrap;
}
```

이 경우 `display: none`을 사용하면 화면 판독기에서도 텍스트가 제거되므로 목적에 맞지 않는다.

---

# pointer-events

`pointer-events`는 포인터 이벤트의 대상 여부를 제어한다.

```css
.element {
    pointer-events: none;
}
```

요소가 마우스 또는 터치 입력을 받지 않도록 할 수 있다.

하지만 다음 사항은 별도로 고려해야 한다.

- 키보드 포커스
- 접근성 트리
- 레이아웃 공간
- 시각적 표시

```css
.button {
    opacity: 0;
    pointer-events: none;
}
```

보이지 않는 버튼의 마우스 클릭은 막을 수 있지만 키보드 포커스까지 자동으로 해결하는 것은 아니다.

---

# display와 DOM

`display: none`은 요소를 DOM에서 제거하지 않는다.

HTML

```html
<div class="menu">
    메뉴
</div>
```

CSS

```css
.menu {
    display: none;
}
```

JavaScript에서는 여전히 요소를 찾을 수 있다.

```javascript
const menu = document.querySelector('.menu');

console.log(menu);
```

DOM에는 존재하지만 렌더링 박스가 생성되지 않는 것이다.

요소를 실제 DOM에서 제거하려면 JavaScript의 DOM 메서드를 사용해야 한다.

```javascript
menu.remove();
```

---

# getComputedStyle

JavaScript에서 최종 계산된 `display` 값을 확인할 수 있다.

```javascript
const element = document.querySelector('.element');

const style = getComputedStyle(element);

console.log(style.display);
```

CSS 클래스, 브라우저 기본 스타일, 미디어 쿼리 등이 모두 반영된 계산 결과를 확인할 수 있다.

---

# offsetParent를 이용한 표시 여부 확인의 한계

일부 코드에서 다음 방식으로 요소가 보이는지 확인하기도 한다.

```javascript
const isVisible = element.offsetParent !== null;
```

하지만 다음 상황에서는 정확하지 않을 수 있다.

- `position: fixed`
- SVG 요소
- `display: contents`
- 숨겨진 조상 요소
- 요소가 렌더링되지만 `offsetParent`가 없는 특수 상황

가시성은 목적에 따라 다르게 정의해야 한다.

```text
레이아웃 박스가 존재하는가

실제로 화면 안에 있는가

투명하지 않은가

사용자와 상호작용 가능한가

접근성 트리에 존재하는가
```

한 가지 속성만으로 모든 가시성을 판단하기 어렵다.

---

# display 변경과 Layout

`display` 값이 변경되면 브라우저는 요소의 박스 구조와 레이아웃을 다시 계산해야 할 수 있다.

```javascript
element.style.display = 'none';
```

```javascript
element.style.display = 'block';
```

많은 요소의 Display를 반복해서 변경하면 성능 비용이 발생할 수 있다.

다만 일반적인 UI에서 메뉴, 모달, 탭을 여닫는 정도는 흔한 작업이다.

성능 최적화가 필요할 때는 다음을 고려한다.

- DOM 변경을 묶어서 처리
- 불필요한 반복 읽기와 쓰기 방지
- 클래스 단위로 상태 변경
- 대규모 목록에서는 렌더링 범위 제한
- 애니메이션에는 `transform`과 `opacity` 우선 검토

---

# display와 Media Query

화면 크기에 따라 Display를 변경할 수 있다.

```css
.mobile-menu {
    display: none;
}

@media (max-width: 768px) {
    .mobile-menu {
        display: block;
    }
}
```

```css
.desktop-navigation {
    display: flex;
}

@media (max-width: 768px) {
    .desktop-navigation {
        display: none;
    }
}
```

다만 모바일과 데스크톱용으로 동일한 콘텐츠를 두 번 작성하고 한쪽을 숨기는 방식은 다음 문제를 만들 수 있다.

- 중복된 DOM
- 중복된 ID
- 접근성 혼란
- 유지보수 증가
- JavaScript 상태 불일치

가능하면 하나의 DOM 구조를 CSS로 재배치하는 방법을 우선 검토한다.

---

# display와 Print CSS

인쇄 시 특정 요소를 숨길 수 있다.

```css
@media print {
    .navigation,
    .advertisement,
    .button {
        display: none;
    }
}
```

본문 콘텐츠만 인쇄되도록 구성할 수 있다.

---

# display와 콘텐츠 보안

`display: none`은 콘텐츠 보안 기능이 아니다.

HTML에 민감한 정보가 포함되어 있고 CSS로만 숨긴 경우 사용자는 개발자 도구나 소스 코드에서 확인할 수 있다.

```html
<div class="secret">
    관리자 전용 정보
</div>
```

```css
.secret {
    display: none;
}
```

권한이 없는 사용자의 정보는 서버에서 전달하지 않아야 한다.

CSS는 표시만 제어할 뿐 데이터 접근을 보호하지 않는다.

---

# DevTools에서 Display 확인하기

브라우저 개발자 도구에서 요소를 선택하면 적용된 `display` 값을 확인할 수 있다.

확인할 항목은 다음과 같다.

- Styles 패널의 `display`
- Computed 패널의 최종 `display`
- 사용자 에이전트 스타일
- 덮어쓰기된 규칙
- Flex 또는 Grid 배지
- Layout 패널
- 요소가 `display: none`인 조상 아래에 있는지
- 미디어 쿼리 적용 여부

---

# display가 적용되지 않을 때 확인 순서

```text
1. 선택자가 요소를 정확히 선택하는지 확인

↓

2. display 선언이 취소선인지 확인

↓

3. 더 높은 명시도의 규칙 확인

↓

4. !important 여부 확인

↓

5. 미디어 쿼리 조건 확인

↓

6. 부모 또는 조상이 display: none인지 확인

↓

7. HTML hidden 속성 확인

↓

8. JavaScript 인라인 스타일 확인

↓

9. 요소의 기본 동작 및 Replaced Element 여부 확인
```

---

# 실무 활용

`display` 속성은 다음과 같은 상황에서 사용한다.

- 내비게이션 메뉴 배치
- 카드 링크를 블록 전체로 확장
- 버튼과 배지의 크기 조절
- 모바일 메뉴 표시와 숨김
- 탭 패널 전환
- 모달 표시 상태 관리
- 이미지 아래 여백 제거
- 목록 마커 표현
- Float 레이아웃의 부모 높이 복구
- Flexbox와 Grid 컨테이너 생성
- 표와 유사한 레이아웃
- 반응형 요소 표시
- 인쇄 시 불필요한 UI 제거
- 화면 판독기용 텍스트 제공

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

    <script
        src="./main.js"
        defer
    ></script>

    <title>CSS Display</title>

</head>

<body>

    <header class="header">

        <div class="header__inner">

            <a
                href="#"
                class="logo"
            >
                Developer Wiki
            </a>

            <nav
                class="desktop-navigation"
                aria-label="주요 메뉴"
            >

                <ul class="navigation-list">

                    <li>
                        <a href="#courses">
                            Courses
                        </a>
                    </li>

                    <li>
                        <a href="#concepts">
                            Concepts
                        </a>
                    </li>

                    <li>
                        <a href="#contact">
                            Contact
                        </a>
                    </li>

                </ul>

            </nav>

            <button
                type="button"
                class="menu-button"
                aria-expanded="false"
                aria-controls="mobile-navigation"
            >

                <span aria-hidden="true">
                    ☰
                </span>

                <span class="visually-hidden">
                    메뉴 열기
                </span>

            </button>

        </div>

        <nav
            id="mobile-navigation"
            class="mobile-navigation"
            aria-label="모바일 메뉴"
            hidden
        >

            <ul class="mobile-navigation__list">

                <li>
                    <a href="#courses">
                        Courses
                    </a>
                </li>

                <li>
                    <a href="#concepts">
                        Concepts
                    </a>
                </li>

                <li>
                    <a href="#contact">
                        Contact
                    </a>
                </li>

            </ul>

        </nav>

    </header>

    <main>

        <section class="hero">

            <div class="hero__content">

                <span class="badge">

                    <span aria-hidden="true">
                        ✓
                    </span>

                    CSS Basic

                </span>

                <h1 class="hero__title">
                    CSS Display
                </h1>

                <p class="hero__description">
                    block, inline, inline-block과 요소의
                    렌더링 방식을 학습합니다.
                </p>

                <div class="hero__actions">

                    <a
                        href="#courses"
                        class="button button--primary"
                    >
                        학습 시작하기
                    </a>

                    <a
                        href="#concepts"
                        class="button button--secondary"
                    >
                        핵심 개념 보기
                    </a>

                </div>

            </div>

        </section>

        <section
            id="courses"
            class="courses"
        >

            <div class="section-header">

                <span class="section-header__category">
                    Display Types
                </span>

                <h2 class="section-header__title">
                    주요 Display 값
                </h2>

            </div>

            <div class="course-grid">

                <article class="course-card">

                    <span class="course-card__number">
                        01
                    </span>

                    <h3 class="course-card__title">
                        Block
                    </h3>

                    <p class="course-card__description">
                        새 줄에서 시작하고 사용 가능한 공간을
                        차지하는 블록 박스를 학습합니다.
                    </p>

                    <a
                        href="#block"
                        class="course-card__link"
                    >
                        자세히 보기
                    </a>

                </article>

                <article class="course-card">

                    <span class="course-card__number">
                        02
                    </span>

                    <h3 class="course-card__title">
                        Inline
                    </h3>

                    <p class="course-card__description">
                        텍스트 흐름 안에 배치되는 인라인 박스와
                        기준선 개념을 학습합니다.
                    </p>

                    <a
                        href="#inline"
                        class="course-card__link"
                    >
                        자세히 보기
                    </a>

                </article>

                <article class="course-card">

                    <span class="course-card__number">
                        03
                    </span>

                    <h3 class="course-card__title">
                        Inline Block
                    </h3>

                    <p class="course-card__description">
                        한 줄에 배치되면서 크기를 가질 수 있는
                        인라인 블록을 학습합니다.
                    </p>

                    <a
                        href="#inline-block"
                        class="course-card__link"
                    >
                        자세히 보기
                    </a>

                </article>

            </div>

        </section>

        <section
            id="concepts"
            class="concepts"
        >

            <div class="concepts__content">

                <h2 class="concepts__title">
                    display에 따른 요소 크기
                </h2>

                <p>
                    동일한 요소라도 display 값에 따라
                    width, height, margin의 동작이 달라집니다.
                </p>

            </div>

            <div class="display-demo">

                <span class="display-demo__inline">
                    inline
                </span>

                <span class="display-demo__inline">
                    inline
                </span>

                <span class="display-demo__inline-block">
                    inline-block
                </span>

                <span class="display-demo__inline-block">
                    inline-block
                </span>

                <span class="display-demo__block">
                    block
                </span>

                <span class="display-demo__block">
                    block
                </span>

            </div>

        </section>

        <section class="notice-section">

            <div class="notice-section__inner">

                <div class="notice">

                    <span
                        class="notice__icon"
                        aria-hidden="true"
                    >
                        !
                    </span>

                    <div>

                        <h2 class="notice__title">
                            display: none 주의
                        </h2>

                        <p class="notice__description">
                            요소는 화면뿐 아니라 레이아웃과
                            접근성 트리에서도 제거될 수 있습니다.
                        </p>

                    </div>

                </div>

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
    --color-primary-light: #dbeafe;
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
    font-family:
        Arial,
        sans-serif;
    line-height: 1.6;
}

a {
    color: inherit;
}

button {
    font: inherit;
}

.visually-hidden {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    overflow: hidden;
    border: 0;
    margin: -1px;
    clip-path: inset(50%);
    white-space: nowrap;
}

.header {
    position: relative;
    border-bottom: 1px solid var(--color-border);
    background-color: var(--color-surface);
}

.header__inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: min(100% - 2rem, var(--content-width));
    margin-inline: auto;
    padding-block: 1rem;
}

.logo {
    display: inline-block;
    color: var(--color-heading);
    font-size: 1.25rem;
    font-weight: 700;
    text-decoration: none;
}

.navigation-list,
.mobile-navigation__list {
    margin: 0;
    padding: 0;
    list-style: none;
}

.navigation-list {
    display: flex;
    align-items: center;
    gap: 2rem;
}

.navigation-list a {
    display: inline-block;
    padding-block: 0.5rem;
    color: var(--color-text);
    font-weight: 600;
    text-decoration: none;
}

.navigation-list a:hover {
    color: var(--color-primary);
}

.navigation-list a:focus-visible,
.mobile-navigation a:focus-visible,
.button:focus-visible,
.menu-button:focus-visible {
    outline: 3px solid var(--color-primary);
    outline-offset: 4px;
}

.menu-button {
    display: none;
    padding: 0.5rem;
    border: 0;
    background: none;
    color: var(--color-heading);
    cursor: pointer;
    font-size: 1.5rem;
}

.mobile-navigation {
    border-top: 1px solid var(--color-border);
    background-color: var(--color-surface);
}

.mobile-navigation__list {
    display: grid;
}

.mobile-navigation a {
    display: block;
    padding: 1rem max(1rem, 5vw);
    text-decoration: none;
}

.mobile-navigation a:hover {
    background-color: var(--color-primary-light);
    color: var(--color-primary-dark);
}

.hero {
    display: grid;
    min-height: 75dvh;
    padding-block: clamp(5rem, 12vw, 10rem);
    padding-inline: max(1rem, 5vw);
    background:
        linear-gradient(
            135deg,
            #eff6ff,
            #dbeafe
        );
    place-items: center;
}

.hero__content {
    max-width: 55rem;
    text-align: center;
}

.badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5em 1em;
    border: 1px solid var(--color-primary);
    border-radius: 999px;
    color: var(--color-primary-dark);
    font-size: 0.875rem;
    font-weight: 700;
}

.hero__title {
    margin-block: 1.5rem 1rem;
    color: var(--color-heading);
    font-size: clamp(3rem, 10vw, 7rem);
    letter-spacing: -0.04em;
    line-height: 1;
}

.hero__description {
    max-width: 45ch;
    margin-inline: auto;
    color: var(--color-muted);
    font-size: clamp(1rem, 2vw, 1.25rem);
}

.hero__actions {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
}

.button {
    display: inline-block;
    padding: 0.875em 1.75em;
    border: 2px solid transparent;
    border-radius: var(--radius-small);
    font-weight: 700;
    text-decoration: none;
}

.button--primary {
    border-color: var(--color-primary);
    background-color: var(--color-primary);
    color: white;
}

.button--primary:hover {
    border-color: var(--color-primary-dark);
    background-color: var(--color-primary-dark);
}

.button--secondary {
    border-color: var(--color-primary);
    background-color: transparent;
    color: var(--color-primary);
}

.button--secondary:hover {
    background-color: var(--color-primary-light);
}

.courses,
.concepts {
    width: min(100% - 2rem, var(--content-width));
    margin-inline: auto;
    padding-block: clamp(4rem, 10vw, 8rem);
}

.section-header {
    margin-bottom: 2.5rem;
}

.section-header__category {
    display: inline-block;
    color: var(--color-primary);
    font-size: 0.875rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.section-header__title {
    margin-block: 0.75rem 0;
    color: var(--color-heading);
    font-size: clamp(2rem, 5vw, 3.5rem);
    line-height: 1.2;
}

.course-grid {
    display: grid;
    grid-template-columns:
        repeat(
            auto-fit,
            minmax(
                min(100%, 18rem),
                1fr
            )
        );
    gap: 1.5rem;
}

.course-card {
    display: flex;
    flex-direction: column;
    padding: clamp(1.5rem, 4vw, 2.5rem);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-medium);
    background-color: var(--color-surface);
    box-shadow: 0 1rem 3rem rgb(15 23 42 / 8%);
}

.course-card__number {
    display: inline-block;
    color: var(--color-primary);
    font-size: 0.875rem;
    font-weight: 700;
}

.course-card__title {
    margin-block: 1rem 0.75rem;
    color: var(--color-heading);
    font-size: 1.5rem;
    line-height: 1.3;
}

.course-card__description {
    margin-block: 0 1.5rem;
    color: var(--color-muted);
}

.course-card__link {
    display: inline-block;
    align-self: flex-start;
    margin-top: auto;
    color: var(--color-primary);
    font-weight: 700;
    text-underline-offset: 0.25em;
}

.concepts {
    display: grid;
    grid-template-columns:
        minmax(0, 1fr)
        minmax(0, 1.2fr);
    gap: clamp(2rem, 6vw, 5rem);
    align-items: center;
    border-top: 1px solid var(--color-border);
}

.concepts__title {
    margin-top: 0;
    color: var(--color-heading);
    font-size: clamp(2rem, 5vw, 3.5rem);
    line-height: 1.2;
}

.display-demo {
    padding: 2rem;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-medium);
    background-color: var(--color-surface);
    font-size: 0;
}

.display-demo__inline,
.display-demo__inline-block,
.display-demo__block {
    padding: 0.75rem;
    border: 1px solid var(--color-primary);
    background-color: var(--color-primary-light);
    color: var(--color-primary-dark);
    font-size: 1rem;
}

.display-demo__inline {
    display: inline;
}

.display-demo__inline-block {
    display: inline-block;
    width: 9rem;
    margin-block: 1rem;
}

.display-demo__block {
    display: block;
    margin-block-start: 1rem;
}

.notice-section {
    background-color: #111827;
    color: white;
}

.notice-section__inner {
    width: min(100% - 2rem, var(--content-width));
    margin-inline: auto;
    padding-block: clamp(3rem, 8vw, 6rem);
}

.notice {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
}

.notice__icon {
    display: inline-grid;
    flex: 0 0 auto;
    width: 2.5rem;
    aspect-ratio: 1;
    border: 2px solid currentColor;
    border-radius: 50%;
    font-weight: 700;
    place-items: center;
}

.notice__title {
    margin-block: 0 0.5rem;
    font-size: 1.5rem;
}

.notice__description {
    max-width: 55ch;
    margin: 0;
    color: #cbd5e1;
}

@media (max-width: 48rem) {
    .desktop-navigation {
        display: none;
    }

    .menu-button {
        display: inline-block;
    }

    .concepts {
        grid-template-columns: 1fr;
    }
}
```

## JavaScript

```javascript
'use strict';

const menuButton =
    document.querySelector('.menu-button');

const mobileNavigation =
    document.querySelector('#mobile-navigation');

if (menuButton && mobileNavigation) {
    menuButton.addEventListener('click', function () {
        const isExpanded =
            menuButton.getAttribute('aria-expanded') === 'true';

        menuButton.setAttribute(
            'aria-expanded',
            String(!isExpanded)
        );

        mobileNavigation.hidden = isExpanded;

        const label =
            menuButton.querySelector('.visually-hidden');

        if (label) {
            label.textContent =
                isExpanded
                    ? '메뉴 열기'
                    : '메뉴 닫기';
        }
    });
}
```

---

# 예제 분석

```css
.header__inner {
    display: flex;
}
```

헤더 내부의 로고와 메뉴를 Flexbox로 배치한다.

바깥쪽에서는 블록 요소로 동작하고 내부 자식은 Flex Item이 된다.

---

```css
.logo {
    display: inline-block;
}
```

링크가 인라인 흐름에 참여하면서 Padding과 크기를 안정적으로 가질 수 있게 한다.

---

```css
.menu-button {
    display: none;
}
```

기본 데스크톱 화면에서는 모바일 메뉴 버튼을 렌더링하지 않는다.

---

```css
@media (max-width: 48rem) {
    .menu-button {
        display: inline-block;
    }
}
```

모바일 화면에서는 버튼을 다시 표시한다.

---

```css
.mobile-navigation a {
    display: block;
}
```

링크가 모바일 메뉴의 가로 영역 전체를 클릭할 수 있도록 블록 요소로 변경한다.

---

```css
.badge {
    display: inline-flex;
}
```

배지는 콘텐츠 크기만큼 너비를 차지하고 내부의 아이콘과 텍스트는 Flexbox로 정렬된다.

---

```css
.hero {
    display: grid;
    place-items: center;
}
```

Hero 영역 내부 콘텐츠를 Grid로 가운데 정렬한다.

---

```css
.button {
    display: inline-block;
}
```

링크를 버튼처럼 표현하면서 한 줄에 배치될 수 있게 한다.

---

```css
.course-grid {
    display: grid;
}
```

학습 카드를 행과 열 기반의 Grid Layout으로 배치한다.

---

```css
.course-card {
    display: flex;
    flex-direction: column;
}
```

카드 내부를 세로 방향 Flexbox로 만들고 링크를 카드 아래쪽에 배치할 수 있게 한다.

---

```css
.display-demo {
    font-size: 0;
}
```

예제 안의 `inline-block` 요소 사이에 HTML 공백으로 생기는 간격을 제거한다.

자식 요소에는 다시 `font-size: 1rem`을 지정한다.

실제 레이아웃에서는 Flexbox나 Grid를 사용하는 것이 더 일반적이다.

---

```css
.display-demo__inline {
    display: inline;
}
```

텍스트 흐름 안에 배치되며 지정한 너비와 높이가 일반적으로 적용되지 않는다.

---

```css
.display-demo__inline-block {
    display: inline-block;
    width: 9rem;
}
```

한 줄에 배치되면서 지정한 너비를 가질 수 있다.

---

```css
.display-demo__block {
    display: block;
}
```

새로운 줄에서 시작하고 블록 흐름으로 배치된다.

---

```html
<nav
    id="mobile-navigation"
    hidden
>
```

모바일 내비게이션은 초기 상태에서 `hidden` 속성으로 숨겨진다.

JavaScript에서 다음과 같이 상태를 변경한다.

```javascript
mobileNavigation.hidden = false;
```

---

```javascript
menuButton.setAttribute(
    'aria-expanded',
    String(!isExpanded)
);
```

버튼이 제어하는 메뉴의 열림 상태를 보조 기술에 전달한다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|---|---|
| Display | 요소의 외부 및 내부 배치 방식을 결정하는 속성 |
| Normal Flow | 요소가 기본적으로 배치되는 문서 흐름 |
| Outer Display Type | 요소 자신이 주변 요소와 배치되는 방식 |
| Inner Display Type | 요소 내부 자식이 배치되는 방식 |
| Block Box | 새 줄에서 시작하는 블록 박스 |
| Inline Box | 텍스트 흐름 안에 배치되는 박스 |
| Inline Formatting Context | 인라인 콘텐츠가 줄 상자 안에 배치되는 환경 |
| Line Box | 인라인 콘텐츠 한 줄이 차지하는 영역 |
| Baseline | 인라인 콘텐츠가 정렬되는 기준선 |
| block | 블록 수준의 배치 |
| inline | 인라인 수준의 배치 |
| inline-block | 인라인 배치와 크기 지정을 결합한 형태 |
| none | 렌더링 박스를 생성하지 않음 |
| list-item | 목록 항목 박스 생성 |
| flow-root | 새로운 Block Formatting Context 생성 |
| contents | 자신의 박스를 제거하고 자식만 배치에 참여 |
| table | 표 형식의 레이아웃 생성 |
| flex | 블록 수준 Flex Container |
| inline-flex | 인라인 수준 Flex Container |
| grid | 블록 수준 Grid Container |
| inline-grid | 인라인 수준 Grid Container |
| BFC | 독립적인 블록 배치 영역 |
| Replaced Element | 외부 콘텐츠나 브라우저 표현으로 대체되는 요소 |
| visibility | 공간을 유지하면서 가시성 제어 |
| opacity | 요소 전체의 투명도 제어 |
| hidden | HTML 요소의 표시 상태를 숨기는 속성 |
| aria-hidden | 보조 기술에서 콘텐츠를 숨기는 속성 |
| inert | 하위 콘텐츠의 상호작용과 포커스를 비활성화하는 속성 |
| pointer-events | 포인터 이벤트 대상 여부 제어 |
| visually-hidden | 화면에서는 숨기고 보조 기술에는 제공하는 패턴 |

---

# 자주 하는 실수

## 1. block 요소는 항상 width: 100%라고 생각한다

블록 요소의 기본 너비는 일반적으로 `auto`이다.

`auto`는 사용 가능한 공간과 Margin, Padding, Border를 고려하여 계산된다.

```css
.box {
    display: block;
    width: auto;
}
```

`width: 100%`와 항상 같은 결과는 아니다.

---

## 2. 인라인 요소에 width와 height를 지정한다

```css
.link {
    display: inline;
    width: 300px;
    height: 100px;
}
```

일반적인 인라인 요소에는 지정한 크기가 의도대로 적용되지 않는다.

```css
.link {
    display: inline-block;
    width: 300px;
}
```

---

## 3. 인라인 요소의 상하 Margin으로 줄 간격을 만들려고 한다

```css
.link {
    margin-top: 2rem;
    margin-bottom: 2rem;
}
```

인라인 요소의 상하 Margin은 일반 블록처럼 주변 줄을 밀어내지 않을 수 있다.

요소의 목적에 따라 `inline-block`, `block`, `line-height` 등을 고려한다.

---

## 4. inline-block 요소 사이의 공백을 계산하지 않는다

```css
.item {
    display: inline-block;
    width: 33.3333%;
}
```

HTML의 공백 때문에 마지막 요소가 다음 줄로 내려갈 수 있다.

현대 레이아웃에서는 Flexbox나 Grid를 고려한다.

---

## 5. inline-block 요소의 아래쪽이 맞지 않는 이유를 모른다

`inline-block`은 기본적으로 Baseline에 정렬될 수 있다.

```css
.item {
    display: inline-block;
    vertical-align: top;
}
```

---

## 6. 이미지 아래의 작은 여백을 Margin 문제로 생각한다

이미지가 인라인 기준선에 맞춰 배치되어 아래쪽 공간이 남는 경우가 있다.

```css
img {
    display: block;
}
```

---

## 7. display: none과 visibility: hidden을 같은 것으로 생각한다

- `display: none`: 레이아웃 공간 제거
- `visibility: hidden`: 공간 유지

---

## 8. opacity: 0이면 요소가 완전히 제거된다고 생각한다

```css
.element {
    opacity: 0;
}
```

요소는 공간을 차지하며 클릭과 포커스를 받을 수 있다.

```css
.element {
    opacity: 0;
    pointer-events: none;
}
```

상호작용과 접근성은 목적에 맞게 별도로 처리해야 한다.

---

## 9. display: none에 Transition을 적용하려고 한다

```css
.modal {
    display: none;
    transition: display 300ms;
}
```

일반적인 부드러운 전환이 만들어지지 않는다.

`opacity`, `visibility`, `transform` 등을 활용한다.

---

## 10. JavaScript에서 항상 display: block으로 복원한다

```javascript
element.style.display = 'block';
```

원래 요소가 `flex`, `grid`, `inline-block`이었을 수 있다.

상태 클래스를 사용하는 방식이 더 안전하다.

```javascript
element.classList.remove('is-hidden');
```

---

## 11. display 변경으로 HTML 의미도 바뀐다고 생각한다

```css
div {
    display: table;
}
```

시각적으로 표처럼 보여도 실제 표의 의미와 접근성 정보는 생성되지 않는다.

표 데이터에는 HTML `table`을 사용한다.

---

## 12. div에 display: inline-block을 적용하면 버튼이 된다고 생각한다

```html
<div class="button">
    저장
</div>
```

시각적인 형태만 버튼처럼 보일 뿐 키보드와 접근성 기능은 제공되지 않는다.

```html
<button type="button">
    저장
</button>
```

---

## 13. display: contents에 Padding과 Background를 적용한다

```css
.wrapper {
    display: contents;
    padding: 2rem;
    background-color: yellow;
}
```

자신의 박스를 생성하지 않으므로 기대한 시각적 스타일이 나타나지 않는다.

---

## 14. 의미 있는 요소에 display: contents를 무조건 사용한다

브라우저 및 보조 기술에 따라 접근성 트리에 영향을 줄 수 있다.

단순한 시각적 Wrapper에 제한적으로 사용하고 실제 환경에서 테스트한다.

---

## 15. BFC를 만들기 위해 항상 overflow: hidden을 사용한다

```css
.container {
    overflow: hidden;
}
```

자식의 그림자, 포커스 Outline, 드롭다운이 잘릴 수 있다.

BFC 생성만이 목적이라면 다음을 고려한다.

```css
.container {
    display: flow-root;
}
```

---

## 16. display: none을 보안 기능으로 사용한다

CSS로 숨긴 데이터는 DOM과 소스 코드에서 확인할 수 있다.

권한이 없는 정보는 서버에서 전달하지 않아야 한다.

---

## 17. 모바일과 데스크톱 콘텐츠를 중복 작성하고 한쪽을 숨긴다

중복된 ID, 상태 불일치, 접근성 문제와 유지보수 증가가 발생할 수 있다.

가능하면 하나의 DOM을 재배치한다.

---

## 18. visually-hidden 콘텐츠에 display: none을 사용한다

```css
.visually-hidden {
    display: none;
}
```

화면 판독기에서도 제거된다.

화면에서만 숨기는 전용 패턴을 사용한다.

---

## 19. aria-hidden으로 요소를 화면에서도 숨길 수 있다고 생각한다

```html
<div aria-hidden="true">
    콘텐츠
</div>
```

시각적으로는 그대로 표시된다.

`aria-hidden`은 보조 기술 노출을 제어한다.

---

## 20. opacity: 0 요소가 클릭을 가로채는 원인을 찾지 못한다

투명해도 요소는 포인터 이벤트를 받을 수 있다.

```css
.overlay {
    opacity: 0;
    pointer-events: none;
}
```

---

# 면접 포인트

### Q1. CSS의 display 속성은 무엇을 결정하나요?

요소가 주변 요소와 어떻게 배치되는지와 자식 요소가 내부에서 어떤 레이아웃 방식으로 배치되는지를 결정한다.

---

### Q2. block 요소의 주요 특징은 무엇인가요?

- 새 줄에서 시작한다.
- 사용 가능한 가로 공간을 채우는 방향으로 동작한다.
- `width`, `height`를 지정할 수 있다.
- 상하좌우 Margin과 Padding이 배치에 영향을 준다.

---

### Q3. inline 요소의 주요 특징은 무엇인가요?

- 텍스트 흐름 안에 배치된다.
- 같은 줄에 여러 요소가 배치될 수 있다.
- 일반적으로 `width`, `height`가 적용되지 않는다.
- 좌우 Margin과 Padding은 적용된다.
- Baseline을 기준으로 정렬될 수 있다.

---

### Q4. inline과 inline-block의 차이는 무엇인가요?

둘 다 같은 줄에 배치될 수 있지만 `inline-block`은 `width`, `height`, 상하 Margin과 Padding을 정상적으로 지정할 수 있다.

---

### Q5. inline-block 요소 사이에 공백이 생기는 이유는 무엇인가요?

HTML 요소 사이의 공백과 줄바꿈이 인라인 텍스트 공백처럼 렌더링되기 때문이다.

---

### Q6. 이미지 아래에 작은 여백이 생기는 이유는 무엇인가요?

이미지가 기본적으로 인라인 수준 요소로서 텍스트 Baseline에 정렬되고 글자의 아래쪽 공간이 남을 수 있기 때문이다.

```css
img {
    display: block;
}
```

---

### Q7. display: none과 visibility: hidden의 차이는 무엇인가요?

`display: none`은 요소를 레이아웃에서 제거한다.

`visibility: hidden`은 요소를 보이지 않게 하지만 레이아웃 공간은 유지한다.

---

### Q8. opacity: 0과 display: none의 차이는 무엇인가요?

`opacity: 0`은 요소가 투명해질 뿐 공간, 상호작용, 포커스 가능성이 남을 수 있다.

`display: none`은 렌더링 박스와 공간을 제거한다.

---

### Q9. display: none인 요소는 DOM에서도 제거되나요?

아니다.

DOM에는 존재하지만 렌더링 박스를 생성하지 않는다.

JavaScript로 여전히 선택할 수 있다.

---

### Q10. display: flow-root는 무엇인가요?

새로운 Block Formatting Context를 생성하는 Display 값이다.

Float된 자식을 포함하거나 Margin Collapsing을 방지하는 데 사용할 수 있다.

---

### Q11. Block Formatting Context란 무엇인가요?

블록 요소들이 배치되는 독립적인 레이아웃 환경이다.

내부 Float를 포함하고 외부 Float의 영향을 차단하거나 Margin 상쇄에 영향을 줄 수 있다.

---

### Q12. display: contents는 어떻게 동작하나요?

요소 자신의 박스를 생성하지 않고 자식 요소가 상위 레이아웃에 직접 참여하는 것처럼 만든다.

해당 요소의 Padding, Border, Background 등 박스 스타일은 표시되지 않는다.

---

### Q13. display: contents를 사용할 때 주의할 점은 무엇인가요?

브라우저와 보조 기술에 따라 접근성 트리에 영향을 줄 수 있으며, 요소 자신의 박스가 없어져 크기와 배경 스타일이 적용되지 않는다.

---

### Q14. display: flex와 inline-flex의 차이는 무엇인가요?

둘 다 내부 자식을 Flex Item으로 배치한다.

`flex`는 바깥쪽에서 블록 수준으로 동작하고, `inline-flex`는 인라인 수준으로 동작한다.

---

### Q15. display: grid와 inline-grid의 차이는 무엇인가요?

둘 다 내부 자식을 Grid Item으로 배치한다.

`grid`는 블록 수준, `inline-grid`는 인라인 수준으로 주변 요소와 배치된다.

---

### Q16. display를 변경하면 HTML의 의미도 변경되나요?

아니다.

CSS는 시각적인 박스와 배치 방식만 변경하며 HTML 요소의 의미와 기본 접근성 역할은 변경하지 않는다.

---

### Q17. display: table을 div에 적용하면 실제 표가 되나요?

아니다.

시각적인 Table Layout은 만들 수 있지만 표의 의미와 접근성 구조는 생성되지 않는다.

실제 표 데이터에는 `table`, `tr`, `th`, `td`를 사용한다.

---

### Q18. display: none을 애니메이션할 수 있나요?

일반적으로 `opacity`처럼 연속적인 값으로 보간되지 않으므로 단순한 Transition으로 부드러운 효과를 만들기 어렵다.

`opacity`, `visibility`, `transform` 등을 함께 사용한다.

---

### Q19. visually-hidden 패턴은 언제 사용하나요?

화면에서는 숨기지만 화면 판독기 사용자에게는 제공해야 하는 레이블이나 설명에 사용한다.

---

### Q20. aria-hidden과 display: none의 차이는 무엇인가요?

`aria-hidden`은 보조 기술에서 요소를 숨기지만 시각적으로는 표시될 수 있다.

`display: none`은 시각적 렌더링과 레이아웃에서 요소를 제거하며 일반적으로 접근성 트리에서도 제외된다.

---

### Q21. hidden 속성은 무엇인가요?

HTML에서 요소가 현재 표시되지 않아야 함을 나타내는 속성이다.

브라우저에서는 일반적으로 `display: none`과 유사하게 처리된다.

---

### Q22. opacity: 0 요소가 클릭되는 이유는 무엇인가요?

투명도만 0으로 설정했을 뿐 요소의 박스와 포인터 이벤트는 그대로 존재하기 때문이다.

---

### Q23. block 요소의 width: auto와 width: 100%는 같은가요?

항상 같지 않다.

`auto`는 Margin, Padding, Border와 사용 가능한 공간을 고려해 계산하지만 `100%`는 속성의 기준 너비에 따라 Content 크기를 명시적으로 지정할 수 있다.

---

### Q24. Outer Display Type과 Inner Display Type은 무엇인가요?

Outer Display Type은 요소가 주변 요소와 배치되는 방식을 의미한다.

Inner Display Type은 요소의 자식이 내부에서 배치되는 방식을 의미한다.

---

# 핵심 정리

- `display`는 요소의 외부 배치 방식과 내부 자식 배치 방식을 결정한다.
- HTML 요소마다 기본 Display 값이 있지만 CSS로 변경할 수 있다.
- Display를 변경해도 HTML 요소의 의미는 바뀌지 않는다.
- `block` 요소는 새 줄에서 시작하고 사용 가능한 가로 공간을 차지하는 방향으로 동작한다.
- `inline` 요소는 텍스트 흐름 안에 배치되며 일반적으로 `width`와 `height`가 적용되지 않는다.
- `inline-block`은 같은 줄에 배치되면서 크기와 상하 여백을 가질 수 있다.
- 인라인 요소는 Line Box와 Baseline을 기준으로 배치된다.
- 이미지 아래의 여백은 Baseline 정렬 때문에 발생할 수 있다.
- `inline-block` 사이에는 HTML 공백으로 인한 간격이 생길 수 있다.
- `display: none`은 요소의 렌더링 박스와 레이아웃 공간을 제거한다.
- `visibility: hidden`은 요소를 숨기지만 공간을 유지한다.
- `opacity: 0`은 요소를 투명하게 하지만 공간과 상호작용 가능성이 남을 수 있다.
- `display: flow-root`는 새로운 Block Formatting Context를 생성한다.
- `flow-root`는 Float된 자식을 포함하거나 Margin Collapsing을 방지할 때 유용하다.
- `display: contents`는 요소 자신의 박스를 제거하고 자식만 레이아웃에 참여하게 한다.
- `display: contents`는 박스 스타일과 접근성 영향을 주의해야 한다.
- `display: flex`와 `display: grid`는 각각 Flexbox와 Grid Container를 생성한다.
- `inline-flex`와 `inline-grid`는 인라인 수준의 외부 배치와 Flex/Grid 내부 배치를 결합한다.
- `display: table`은 시각적 표 레이아웃을 만들지만 HTML 의미를 추가하지 않는다.
- 실제 버튼, 링크, 표에는 의미에 맞는 HTML 요소를 사용해야 한다.
- 화면에서만 텍스트를 숨기고 보조 기술에는 제공해야 한다면 `display: none` 대신 visually-hidden 패턴을 사용한다.
- `aria-hidden`은 접근성 노출을 제어하며 시각적 표시 여부는 변경하지 않는다.
- `display: none`은 보안 기능이 아니므로 민감한 데이터를 숨기는 용도로 사용하면 안 된다.
- JavaScript에서는 `display: block`을 직접 지정하기보다 상태 클래스나 `hidden` 속성을 사용하는 것이 관리하기 쉽다.
- CSS가 적용되지 않을 때 DevTools에서 최종 Display 값과 조상 요소의 상태를 확인해야 한다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-22 | 최초 작성 |
| v1.0 | 2026-07-22 | Normal Flow와 Display 기본 개념 정리 |
| v1.0 | 2026-07-22 | Outer Display Type과 Inner Display Type 설명 추가 |
| v1.0 | 2026-07-22 | block, inline, inline-block 특징과 비교 추가 |
| v1.0 | 2026-07-22 | Inline Formatting Context, Line Box, Baseline 설명 추가 |
| v1.0 | 2026-07-22 | inline-block 공백 및 Baseline 문제 해결 방법 추가 |
| v1.0 | 2026-07-22 | display: none, visibility, opacity 비교 추가 |
| v1.0 | 2026-07-22 | hidden 속성과 JavaScript 상태 관리 예제 추가 |
| v1.0 | 2026-07-22 | display: list-item와 ::marker 설명 추가 |
| v1.0 | 2026-07-22 | display: flow-root와 Block Formatting Context 정리 |
| v1.0 | 2026-07-22 | display: contents의 동작과 접근성 주의점 추가 |
| v1.0 | 2026-07-22 | Table 관련 Display 값 정리 |
| v1.0 | 2026-07-22 | flex, inline-flex, grid, inline-grid 비교 추가 |
| v1.0 | 2026-07-22 | Replaced Element와 이미지 Display 설명 추가 |
| v1.0 | 2026-07-22 | Semantic HTML과 접근성 관련 내용 추가 |
| v1.0 | 2026-07-22 | visually-hidden, aria-hidden, inert 개념 추가 |
| v1.0 | 2026-07-22 | 반응형 Display와 Print CSS 활용 추가 |
| v1.0 | 2026-07-22 | DevTools 분석 순서와 실무 프로젝트 추가 |
| v1.0 | 2026-07-22 | 자주 하는 실수와 면접 포인트 추가 |