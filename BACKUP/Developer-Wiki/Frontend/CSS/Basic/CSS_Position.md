---
title: CSS Position
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS Position

## 문서 정보

| 항목 | 내용 |
|---|---|
| 문서명 | CSS Position |
| 분류 | Frontend / CSS / Basic |
| 난이도 | Basic → Intermediate |
| 선수 지식 | CSS Box Model, CSS Display |
| 핵심 주제 | Position, Containing Block, Offset, z-index, Stacking Context |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

CSS의 `position` 속성은 요소의 위치를 어떤 기준으로 계산할 것인지 결정한다.

```css
.element {
    position: relative;
}
```

요소의 위치를 조정할 때는 단순히 `top`, `left`만 이해해서는 부족하다.

다음 개념을 함께 이해해야 한다.

- 요소가 일반 문서 흐름에 남아 있는지
- 요소가 어느 박스를 기준으로 이동하는지
- 원래 차지하던 공간이 유지되는지
- 스크롤 시 요소가 어떻게 동작하는지
- 다른 요소와 겹칠 때 어떤 순서로 그려지는지
- `z-index`가 왜 동작하지 않는지
- 새로운 Stacking Context가 생성되었는지

`position`은 다음과 같은 UI 구현에서 사용한다.

- 카드 위 배지
- 이미지 위 텍스트
- 드롭다운 메뉴
- 툴팁
- 모달
- 고정 헤더
- 화면 하단 버튼
- Sticky 사이드바
- 테이블 고정 헤더
- 알림 아이콘
- 로딩 오버레이
- Toast 메시지

---

# 핵심 개념

CSS Position에서 이해해야 할 주요 개념은 다음과 같다.

- Normal Flow
- Positioned Element
- `position: static`
- `position: relative`
- `position: absolute`
- `position: fixed`
- `position: sticky`
- Containing Block
- Offset
- `top`
- `right`
- `bottom`
- `left`
- `inset`
- Logical Offset
- `z-index`
- Stacking Order
- Stacking Context
- Scroll Container
- Viewport
- Transform과 Position의 관계

---

# Normal Flow

Normal Flow는 별도의 위치 지정이 없을 때 요소가 배치되는 기본 문서 흐름이다.

일반적인 가로쓰기 문서에서 블록 요소는 위에서 아래로 쌓인다.

```html
<div class="box">
    첫 번째
</div>

<div class="box">
    두 번째
</div>
```

```css
.box {
    border: 1px solid #333;
}
```

배치 결과

```text
첫 번째

두 번째
```

인라인 요소는 텍스트 흐름 안에서 같은 줄에 배치될 수 있다.

```html
<span>HTML</span>
<span>CSS</span>
<span>JavaScript</span>
```

Position 값을 변경하면 요소가 Normal Flow에 남아 있거나 흐름에서 제거될 수 있다.

---

# Positioned Element

일반적으로 `position` 값이 `static`이 아닌 요소를 Positioned Element라고 한다.

```css
.element {
    position: relative;
}
```

다음 값은 Positioned Element를 만든다.

- `relative`
- `absolute`
- `fixed`
- `sticky`

Positioned Element는 다음 기능과 관계가 있다.

- Offset 속성
- `z-index`
- 절대 위치 요소의 기준점
- Stacking Context
- 겹침 순서

---

# position 속성

대표적인 값은 다음과 같다.

| 값 | 문서 흐름 | 위치 기준 | 원래 공간 |
|---|---|---|---|
| `static` | 유지 | 기본 흐름 | 유지 |
| `relative` | 유지 | 자신의 원래 위치 | 유지 |
| `absolute` | 제거 | 가장 가까운 기준 조상 | 제거 |
| `fixed` | 제거 | 주로 Viewport | 제거 |
| `sticky` | 유지 | 평소에는 흐름, 스크롤 시 기준 영역 | 유지 |

---

# position: static

`static`은 `position`의 기본값이다.

```css
.element {
    position: static;
}
```

요소는 Normal Flow에 따라 배치된다.

```html
<div class="first">
    첫 번째
</div>

<div class="second">
    두 번째
</div>
```

```css
.first,
.second {
    position: static;
}
```

두 요소는 일반 블록 흐름에 따라 위에서 아래로 배치된다.

---

# static과 Offset

`position: static`인 요소에는 일반적으로 다음 Offset 속성이 적용되지 않는다.

```css
.element {
    position: static;
    top: 20px;
    left: 30px;
}
```

`top`과 `left`를 작성해도 요소가 이동하지 않는다.

Offset을 사용하려면 `position`을 변경해야 한다.

```css
.element {
    position: relative;
    top: 20px;
    left: 30px;
}
```

---

# static을 명시적으로 사용하는 경우

대부분의 요소는 기본값이 `static`이므로 직접 작성할 필요가 없다.

하지만 기존 Position 설정을 해제할 때 사용할 수 있다.

```css
.element {
    position: absolute;
}

@media (max-width: 768px) {
    .element {
        position: static;
    }
}
```

모바일 환경에서 절대 위치를 해제하고 일반 흐름으로 되돌릴 수 있다.

---

# position: relative

`position: relative`는 요소를 자신의 원래 위치를 기준으로 이동시킨다.

```css
.element {
    position: relative;
    top: 20px;
    left: 30px;
}
```

주요 특징은 다음과 같다.

- Normal Flow에 남아 있다.
- 원래 차지하던 공간이 유지된다.
- 자신의 원래 위치를 기준으로 이동한다.
- 다른 요소는 이동 전 위치를 기준으로 배치된다.
- 절대 위치 자식의 Containing Block이 될 수 있다.
- `z-index`를 사용할 수 있다.

---

# relative 기본 예제

HTML

```html
<div class="box box--first">
    첫 번째
</div>

<div class="box box--second">
    두 번째
</div>
```

CSS

```css
.box {
    width: 200px;
    padding: 1rem;
    border: 1px solid #333;
}

.box--first {
    position: relative;
    top: 30px;
    left: 40px;
}
```

첫 번째 요소는 화면에서 오른쪽 아래로 이동한다.

그러나 두 번째 요소는 첫 번째 요소의 원래 자리를 기준으로 배치된다.

```text
원래 배치 공간은 유지

실제 화면 위치만 이동
```

---

# relative와 공간 유지

다음 코드를 보자.

```css
.first {
    position: relative;
    top: 100px;
}
```

첫 번째 요소가 아래로 이동하더라도 다음 요소가 그 자리를 채우지 않는다.

```text
원래 위치

첫 번째 요소의 공간 유지

↓

실제 요소만 아래로 이동

↓

다른 요소와 겹칠 수 있음
```

따라서 레이아웃의 간격을 만들기 위해 `top`으로 요소를 이동시키는 것은 적절하지 않을 수 있다.

간격이 목적이라면 다음 속성을 먼저 고려한다.

- `margin`
- `padding`
- `gap`
- Flexbox
- Grid

---

# relative의 대표적인 용도

`position: relative`는 요소를 직접 이동시키는 것보다 절대 위치 자식의 기준점을 만들기 위해 더 자주 사용한다.

HTML

```html
<article class="card">

    <span class="card__badge">
        NEW
    </span>

    <h2>
        CSS Position
    </h2>

</article>
```

CSS

```css
.card {
    position: relative;
}

.card__badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
}
```

`card__badge`는 `.card`를 기준으로 배치된다.

---

# relative와 z-index

`position: relative`를 적용하면 `z-index`를 사용할 수 있다.

```css
.element {
    position: relative;
    z-index: 10;
}
```

다만 `z-index`는 단순한 숫자 비교만으로 결정되지 않는다.

요소가 속한 Stacking Context를 함께 확인해야 한다.

---

# position: absolute

`position: absolute`는 요소를 일반적인 문서 흐름에서 제거하고 Containing Block을 기준으로 배치한다.

```css
.element {
    position: absolute;
    top: 0;
    right: 0;
}
```

주요 특징은 다음과 같다.

- Normal Flow에서 제거된다.
- 원래 공간을 차지하지 않는다.
- 다른 요소와 겹칠 수 있다.
- 가장 가까운 기준 조상을 찾는다.
- Offset 속성으로 위치를 지정한다.
- 너비가 콘텐츠에 맞게 줄어드는 방향으로 계산될 수 있다.
- `z-index`를 사용할 수 있다.

---

# absolute 기본 예제

HTML

```html
<div class="container">

    <div class="box">
        절대 위치 요소
    </div>

</div>
```

CSS

```css
.container {
    position: relative;
    width: 400px;
    height: 250px;
    border: 2px solid #333;
}

.box {
    position: absolute;
    top: 20px;
    right: 20px;
}
```

`.box`는 `.container`의 오른쪽 위에서 각각 `20px` 떨어진 위치에 배치된다.

---

# absolute와 문서 흐름 제거

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
    position: absolute;
}
```

첫 번째 요소는 일반 흐름에서 제거된다.

두 번째 요소는 첫 번째 요소가 없었던 것처럼 위쪽으로 이동할 수 있다.

```text
absolute 요소

공간 제거

↓

다음 요소가 빈 공간을 채움
```

---

# 부모에 relative를 사용하는 이유

절대 위치 요소는 가장 가까운 Positioned Ancestor를 기준으로 배치된다.

```html
<div class="card">

    <span class="badge">
        NEW
    </span>

</div>
```

```css
.card {
    position: relative;
}

.badge {
    position: absolute;
    top: 0;
    right: 0;
}
```

`.card`에 `position: relative`가 없으면 `.badge`는 더 상위의 기준 요소나 초기 Containing Block을 기준으로 배치될 수 있다.

따라서 다음 패턴을 자주 사용한다.

```css
.parent {
    position: relative;
}

.child {
    position: absolute;
}
```

부모를 이동시키기 위해 `relative`를 설정하는 것이 아니라 자식의 좌표 기준을 만들기 위한 것이다.

---

# 가장 가까운 Positioned Ancestor

HTML

```html
<div class="outer">

    <div class="middle">

        <div class="inner">
            Absolute
        </div>

    </div>

</div>
```

CSS

```css
.outer {
    position: relative;
}

.middle {
    position: static;
}

.inner {
    position: absolute;
    top: 0;
    left: 0;
}
```

`.inner`는 가장 가까운 Positioned Ancestor인 `.outer`를 기준으로 배치된다.

`.middle`은 `position: static`이므로 기준 조상이 되지 않는다.

---

# Containing Block

Containing Block은 요소의 크기와 위치를 계산할 때 기준이 되는 영역이다.

Position을 제대로 이해하려면 Containing Block을 반드시 이해해야 한다.

다음 속성의 계산 기준이 될 수 있다.

- `top`
- `right`
- `bottom`
- `left`
- 백분율 `width`
- 백분율 `height`
- 백분율 Padding
- 절대 위치 좌표

---

# static과 relative의 Containing Block

일반적인 `static`, `relative`, `sticky` 요소의 크기는 보통 가장 가까운 블록 컨테이너의 Content Box를 기준으로 계산된다.

```html
<div class="parent">

    <div class="child">
        콘텐츠
    </div>

</div>
```

```css
.parent {
    width: 800px;
}

.child {
    width: 50%;
}
```

`.child`의 너비는 일반적으로 `.parent`의 Content Box를 기준으로 계산된다.

---

# absolute의 Containing Block

절대 위치 요소의 Containing Block은 일반적으로 가장 가까운 조상 중 다음 조건을 만족하는 요소에 의해 형성된다.

- `position`이 `static`이 아닌 조상
- 특정 `transform`이 적용된 조상
- 특정 `filter`가 적용된 조상
- `perspective`가 적용된 조상
- 일부 `contain` 속성이 적용된 조상
- 일부 `will-change` 조건

가장 일반적인 패턴은 다음이다.

```css
.parent {
    position: relative;
}

.child {
    position: absolute;
}
```

---

# 기준 조상이 없는 absolute

기준이 되는 Positioned Ancestor가 없다면 절대 위치 요소는 초기 Containing Block을 기준으로 배치된다.

```css
.element {
    position: absolute;
    top: 0;
    left: 0;
}
```

초기 Containing Block은 일반적으로 문서의 초기 레이아웃 영역과 연관된다.

이때 요소가 예상하지 못한 페이지 모서리에 붙는 문제가 자주 발생한다.

---

# absolute의 너비

절대 위치 요소는 블록 요소라도 일반 블록처럼 자동으로 부모 너비 전체를 채우지 않을 수 있다.

```css
.badge {
    position: absolute;
}
```

너비가 `auto`이면 콘텐츠에 맞게 줄어드는 Shrink-to-fit 방식으로 계산될 수 있다.

```html
<span class="badge">
    NEW
</span>
```

```css
.badge {
    position: absolute;
    padding: 0.5rem 1rem;
}
```

배지는 콘텐츠 크기만큼 너비를 가질 수 있다.

---

# absolute Stretch

`left`와 `right`를 동시에 지정하고 `width`가 `auto`이면 요소가 기준 영역을 채우도록 늘어날 수 있다.

```css
.element {
    position: absolute;
    left: 1rem;
    right: 1rem;
}
```

```text
기준 요소 왼쪽에서 1rem

기준 요소 오른쪽에서 1rem

그 사이 너비를 채움
```

위아래도 같은 원리를 사용할 수 있다.

```css
.element {
    position: absolute;
    top: 1rem;
    bottom: 1rem;
}
```

네 방향을 모두 설정할 수도 있다.

```css
.overlay {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
}
```

속기 속성으로 작성하면 다음과 같다.

```css
.overlay {
    position: absolute;
    inset: 0;
}
```

---

# absolute 중앙 정렬

## Transform 방식

```css
.element {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```

계산 과정

```text
top: 50%

기준 영역 높이의 50% 위치

left: 50%

기준 영역 너비의 50% 위치

transform: translate(-50%, -50%)

자신의 너비와 높이 절반만큼 반대 방향 이동
```

---

## inset과 margin: auto 방식

요소의 크기가 정해져 있다면 다음 방식도 사용할 수 있다.

```css
.element {
    position: absolute;
    inset: 0;
    width: 200px;
    height: 100px;
    margin: auto;
}
```

네 방향의 Offset과 자동 Margin을 이용해 중앙 정렬한다.

---

## Grid 방식

단순 중앙 정렬이라면 Position보다 Grid가 더 명확할 수 있다.

```css
.parent {
    display: grid;
    place-items: center;
}
```

Position은 요소를 겹치거나 특정 좌표에 배치해야 할 때 사용한다.

---

# inset 속성

`inset`은 `top`, `right`, `bottom`, `left`의 속기 속성이다.

```css
.element {
    inset: 10px;
}
```

다음과 같다.

```css
.element {
    top: 10px;
    right: 10px;
    bottom: 10px;
    left: 10px;
}
```

---

# inset 값 두 개

```css
.element {
    inset: 10px 20px;
}
```

```text
위아래 10px

좌우 20px
```

---

# inset 값 세 개

```css
.element {
    inset: 10px 20px 30px;
}
```

```text
위 10px

좌우 20px

아래 30px
```

---

# inset 값 네 개

```css
.element {
    inset: 10px 20px 30px 40px;
}
```

```text
위 → 오른쪽 → 아래 → 왼쪽
```

---

# 논리적 Offset

문서의 글쓰기 방향을 기준으로 Offset을 작성할 수 있다.

| 속성 | 일반적인 가로쓰기 기준 |
|---|---|
| `inset-inline-start` | left |
| `inset-inline-end` | right |
| `inset-block-start` | top |
| `inset-block-end` | bottom |
| `inset-inline` | left와 right |
| `inset-block` | top과 bottom |

예제

```css
.badge {
    position: absolute;
    inset-block-start: 1rem;
    inset-inline-end: 1rem;
}
```

다국어와 RTL 환경에 유연하게 대응할 수 있다.

---

# Offset의 auto

Offset의 기본값은 `auto`이다.

```css
.element {
    position: absolute;
    top: auto;
    right: auto;
    bottom: auto;
    left: auto;
}
```

모든 값이 `auto`이면 요소는 Static Position을 참고하여 배치될 수 있다.

일반적으로 실무에서는 필요한 방향만 명시한다.

```css
.badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
}
```

---

# top과 bottom 동시 지정

`top`, `bottom`, `height`가 모두 지정되면 과도하게 제약될 수 있다.

```css
.element {
    position: absolute;
    top: 0;
    bottom: 0;
    height: 100px;
}
```

이처럼 위치와 크기를 모두 지정하면 브라우저가 일부 값을 조정해야 할 수 있다.

일반적으로 다음 중 목적에 맞는 조합을 선택한다.

```css
.element {
    top: 0;
    height: 100px;
}
```

또는

```css
.element {
    top: 0;
    bottom: 0;
}
```

---

# position: fixed

`position: fixed`는 요소를 일반 흐름에서 제거하고 주로 Viewport를 기준으로 배치한다.

```css
.element {
    position: fixed;
    right: 2rem;
    bottom: 2rem;
}
```

주요 특징은 다음과 같다.

- Normal Flow에서 제거된다.
- 일반적으로 Viewport를 기준으로 배치된다.
- 페이지를 스크롤해도 같은 화면 위치에 남는다.
- 원래 공간을 차지하지 않는다.
- 다른 콘텐츠와 겹칠 수 있다.
- `z-index`와 자주 함께 사용한다.

---

# Fixed 버튼

HTML

```html
<a
    href="#top"
    class="top-button"
>
    TOP
</a>
```

CSS

```css
.top-button {
    position: fixed;
    right: 2rem;
    bottom: 2rem;
    padding: 1rem;
    border-radius: 50%;
    background-color: #2563eb;
    color: white;
}
```

사용자가 페이지를 스크롤해도 버튼은 화면 오른쪽 아래에 남는다.

---

# 고정 헤더

```css
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
}
```

고정 헤더는 문서 흐름에서 제거되므로 본문 위에 겹칠 수 있다.

```css
body {
    padding-top: 80px;
}
```

또는 레이아웃 구조에서 헤더 높이만큼 공간을 확보해야 한다.

고정 높이를 직접 반복하기보다 CSS 변수를 활용할 수 있다.

```css
:root {
    --header-height: 5rem;
}

.header {
    position: fixed;
    inset: 0 0 auto;
    height: var(--header-height);
}

main {
    padding-top: var(--header-height);
}
```

---

# Fixed와 transform

Fixed 요소의 조상에 `transform`이 적용되면 Viewport가 아니라 해당 조상을 기준으로 배치되는 것처럼 동작할 수 있다.

HTML

```html
<div class="wrapper">

    <div class="fixed-element">
        Fixed
    </div>

</div>
```

CSS

```css
.wrapper {
    transform: translateZ(0);
}

.fixed-element {
    position: fixed;
    top: 0;
    right: 0;
}
```

`.fixed-element`가 Viewport 대신 `.wrapper`를 기준으로 배치될 수 있다.

Fixed가 예상대로 동작하지 않을 때 조상의 다음 속성을 확인한다.

- `transform`
- `filter`
- `perspective`
- `contain`
- `will-change`

---

# 모바일 환경의 Fixed

모바일 브라우저에서는 주소창, 하단 도구 모음, 가상 키보드 등으로 인해 Viewport 크기가 변할 수 있다.

다음과 같은 문제가 발생할 수 있다.

- 하단 버튼이 브라우저 UI에 가려짐
- 가상 키보드가 입력창이나 버튼을 덮음
- `100vh`와 실제 보이는 영역의 차이
- 화면 회전 후 크기 변화

현대 CSS에서는 동적 Viewport 단위를 고려할 수 있다.

```css
.modal {
    min-height: 100dvh;
}
```

---

# Safe Area

노치나 홈 인디케이터가 있는 기기에서는 Safe Area를 고려할 수 있다.

```css
.bottom-bar {
    position: fixed;
    right: 0;
    bottom: 0;
    left: 0;
    padding-bottom:
        calc(1rem + env(safe-area-inset-bottom));
}
```

대표적인 환경 변수는 다음과 같다.

- `safe-area-inset-top`
- `safe-area-inset-right`
- `safe-area-inset-bottom`
- `safe-area-inset-left`

---

# position: sticky

`position: sticky`는 일반 흐름과 고정 위치의 특징을 결합한 값이다.

```css
.element {
    position: sticky;
    top: 0;
}
```

평소에는 Normal Flow에 따라 배치된다.

스크롤하여 지정한 Offset 위치에 도달하면 해당 스크롤 영역 안에서 고정된 것처럼 동작한다.

주요 특징은 다음과 같다.

- 원래 문서 흐름에 남는다.
- 원래 공간을 유지한다.
- Offset이 반드시 필요하다.
- 가장 가까운 Scroll Container의 영향을 받는다.
- 부모 영역을 벗어나지 않는다.
- 특정 조건에서는 동작하지 않을 수 있다.

---

# Sticky 기본 예제

HTML

```html
<header class="header">
    고정되는 헤더
</header>

<main>
    긴 콘텐츠
</main>
```

CSS

```css
.header {
    position: sticky;
    top: 0;
    z-index: 100;
}
```

헤더가 Viewport 상단에 도달하면 상단에 붙어 스크롤된다.

---

# Sticky와 Fixed의 차이

| 구분 | sticky | fixed |
|---|---|---|
| 문서 흐름 | 유지 | 제거 |
| 원래 공간 | 유지 | 제거 |
| 기준 | Scroll Container와 부모 영역 | 주로 Viewport |
| 부모 영역 제한 | O | 일반적으로 X |
| 스크롤 전 | 일반 흐름 | 처음부터 고정 |
| Offset 필요 | 사실상 필요 | 위치에 따라 필요 |

---

# Sticky 동작 과정

```text
1. 요소가 Normal Flow에 따라 배치됨

↓

2. 사용자가 스크롤함

↓

3. 요소가 top 등의 임계 위치에 도달함

↓

4. 지정된 Offset 위치에 붙음

↓

5. 부모 영역의 끝에 도달하면 함께 이동함
```

---

# Sticky에 Offset이 필요한 이유

다음 코드는 Sticky 상태가 시각적으로 발생하지 않을 수 있다.

```css
.element {
    position: sticky;
}
```

어느 위치에서 붙을지 지정하지 않았기 때문이다.

```css
.element {
    position: sticky;
    top: 0;
}
```

가로 방향 Sticky를 구현할 때는 `left` 또는 논리적 Offset을 사용할 수 있다.

```css
.element {
    position: sticky;
    left: 0;
}
```

---

# Scroll Container

Sticky 요소는 가장 가까운 스크롤 가능한 조상의 영향을 받는다.

다음과 같은 속성이 Scroll Container를 만들 수 있다.

```css
.container {
    overflow: auto;
}
```

```css
.container {
    overflow-y: scroll;
}
```

Sticky 요소는 Viewport가 아니라 해당 컨테이너 안에서 붙을 수 있다.

---

# Sticky가 동작하지 않는 주요 원인

## 1. Offset이 없다

```css
.element {
    position: sticky;
}
```

해결

```css
.element {
    position: sticky;
    top: 0;
}
```

---

## 2. 스크롤할 공간이 없다

부모나 문서의 콘텐츠가 충분히 길지 않으면 Sticky 상태를 확인할 수 없다.

---

## 3. 부모의 높이가 너무 작다

Sticky 요소는 일반적으로 부모 영역을 벗어나지 않는다.

```css
.parent {
    height: 200px;
}
```

부모 높이가 작으면 Sticky 요소가 금방 부모 끝에 도달한다.

---

## 4. 조상에 overflow가 설정되어 있다

```css
.wrapper {
    overflow: hidden;
}
```

예상하지 못한 조상이 Sticky 기준 스크롤 영역이 되거나 Sticky 동작을 제한할 수 있다.

다음 속성을 확인한다.

- `overflow`
- `overflow-x`
- `overflow-y`

---

## 5. Flex 또는 Grid의 Stretch

Flex Item이나 Grid Item이 교차축 방향으로 늘어나 Sticky 이동 공간이 사라질 수 있다.

```css
.layout {
    display: flex;
}
```

필요하면 다음을 고려한다.

```css
.sidebar {
    align-self: flex-start;
    position: sticky;
    top: 1rem;
}
```

---

## 6. Sticky 요소가 부모보다 크다

Sticky 요소의 높이가 부모나 Scroll Container보다 크면 정상적인 고정 범위가 부족할 수 있다.

---

## 7. 잘못된 방향 Offset

세로 스크롤인데 `left`만 설정하면 상단 고정이 되지 않는다.

```css
.element {
    position: sticky;
    left: 0;
}
```

세로 Sticky에는 보통 `top`을 설정한다.

---

## 8. Table 요소의 브라우저별 차이

테이블 헤더에서 Sticky를 사용할 때는 셀 또는 헤더 구조에 맞게 적용해야 한다.

```css
th {
    position: sticky;
    top: 0;
}
```

---

# Sticky 사이드바

HTML

```html
<div class="layout">

    <aside class="sidebar">
        사이드바
    </aside>

    <main class="content">
        긴 콘텐츠
    </main>

</div>
```

CSS

```css
.layout {
    display: grid;
    grid-template-columns: 16rem minmax(0, 1fr);
    gap: 3rem;
    align-items: start;
}

.sidebar {
    position: sticky;
    top: 2rem;
}
```

사이드바는 페이지를 스크롤할 때 상단에서 `2rem` 떨어진 위치에 붙는다.

---

# Sticky Table Header

HTML

```html
<div class="table-wrapper">

    <table>

        <thead>
            <tr>
                <th>이름</th>
                <th>과정</th>
            </tr>
        </thead>

        <tbody>
            ...
        </tbody>

    </table>

</div>
```

CSS

```css
.table-wrapper {
    max-height: 400px;
    overflow: auto;
}

th {
    position: sticky;
    top: 0;
    background-color: white;
    z-index: 1;
}
```

테이블을 스크롤해도 헤더가 컨테이너 상단에 유지된다.

배경색을 지정하지 않으면 아래 콘텐츠가 비쳐 보일 수 있다.

---

# z-index

`z-index`는 겹치는 요소의 쌓임 순서를 제어한다.

```css
.element {
    position: relative;
    z-index: 10;
}
```

일반적으로 값이 큰 요소가 앞쪽에 그려진다.

```css
.first {
    z-index: 1;
}

.second {
    z-index: 2;
}
```

`.second`가 `.first`보다 앞에 표시될 수 있다.

하지만 이것은 같은 Stacking Context 안에서 비교될 때의 이야기이다.

---

# z-index의 기본값

```css
.element {
    z-index: auto;
}
```

`auto`는 별도의 명시적 쌓임 수준을 만들지 않는 방향으로 동작한다.

`0`과 항상 같은 의미는 아니다.

```css
.element {
    position: relative;
    z-index: 0;
}
```

이 설정은 새로운 Stacking Context를 생성할 수 있다.

---

# z-index가 동작하는 요소

전통적으로 `z-index`는 Positioned Element에서 사용한다.

```css
.element {
    position: relative;
    z-index: 10;
}
```

다음 요소에도 Position 없이 `z-index`가 적용될 수 있다.

- Flex Item
- Grid Item

```css
.container {
    display: flex;
}

.item {
    z-index: 1;
}
```

---

# 음수 z-index

```css
.element {
    position: relative;
    z-index: -1;
}
```

요소를 뒤쪽에 배치할 수 있다.

하지만 부모 배경 뒤로 들어가거나 클릭할 수 없는 위치에 배치될 수 있다.

음수 `z-index`는 Stacking Context 구조를 정확히 이해하고 사용해야 한다.

---

# 큰 z-index가 항상 이기지 않는 이유

다음 구조를 보자.

HTML

```html
<div class="parent-a">

    <div class="child-a">
        A
    </div>

</div>

<div class="parent-b">

    <div class="child-b">
        B
    </div>

</div>
```

CSS

```css
.parent-a {
    position: relative;
    z-index: 1;
}

.child-a {
    position: absolute;
    z-index: 9999;
}

.parent-b {
    position: relative;
    z-index: 2;
}

.child-b {
    position: absolute;
    z-index: 1;
}
```

`.child-a`의 `z-index`는 `9999`이지만 `.parent-a`의 Stacking Context 안에 갇혀 있다.

`.parent-b`의 Stacking Context가 `.parent-a`보다 위에 있으므로 `.child-b`가 앞에 표시될 수 있다.

```text
부모 Stacking Context 비교

parent-a: 1

parent-b: 2

↓

parent-b 전체가 parent-a 전체보다 위
```

---

# Stacking Order

같은 Stacking Context 안에서 요소는 대략 다음과 같은 계층으로 그려질 수 있다.

```text
Stacking Context의 배경과 테두리

↓

음수 z-index 요소

↓

일반 Block 요소

↓

Float 요소

↓

Inline 콘텐츠

↓

z-index: auto 또는 0인 Positioned 요소

↓

양수 z-index 요소
```

실제 Paint Order는 더 복잡하지만 개념적으로 위 순서를 이해하면 도움이 된다.

---

# Stacking Context

Stacking Context는 요소들이 서로의 쌓임 순서를 비교하는 독립적인 계층이다.

한 Stacking Context 안의 자식은 외부 Stacking Context의 요소와 직접 `z-index` 숫자를 비교하지 않는다.

```text
페이지 Root Stacking Context

├── Header Stacking Context
│   └── Dropdown
│
└── Main Stacking Context
    └── Card Overlay
```

Dropdown의 `z-index`가 매우 커도 Header Stacking Context 자체가 Main보다 아래라면 앞으로 나오지 못할 수 있다.

---

# Stacking Context 생성 조건

대표적인 생성 조건은 다음과 같다.

- 문서의 Root 요소
- Positioned Element + `z-index`가 `auto`가 아닌 경우
- `position: fixed`
- `position: sticky`
- Flex Item + `z-index`가 `auto`가 아닌 경우
- Grid Item + `z-index`가 `auto`가 아닌 경우
- `opacity`가 `1`보다 작은 경우
- `transform`이 `none`이 아닌 경우
- `filter`가 `none`이 아닌 경우
- `perspective`가 `none`이 아닌 경우
- `isolation: isolate`
- 일부 `mix-blend-mode`
- 일부 `contain`
- 관련 속성이 지정된 `will-change`

---

# opacity와 Stacking Context

```css
.element {
    opacity: 0.99;
}
```

`opacity`가 `1`보다 작으면 새로운 Stacking Context가 생성될 수 있다.

단순히 투명도만 변경했다고 생각했지만 `z-index` 동작이 달라질 수 있다.

---

# transform과 Stacking Context

```css
.element {
    transform: translateY(0);
}
```

실제 이동이 없어 보여도 `transform`이 `none`이 아니므로 새로운 Stacking Context가 생성될 수 있다.

또한 절대 위치 및 Fixed 요소의 Containing Block에 영향을 줄 수 있다.

---

# isolation: isolate

`isolation: isolate`는 의도적으로 새로운 Stacking Context를 생성한다.

```css
.component {
    isolation: isolate;
}
```

컴포넌트 내부의 음수 또는 양수 `z-index`가 외부 레이어에 영향을 주지 않도록 분리할 때 유용하다.

```css
.card {
    position: relative;
    isolation: isolate;
}

.card::before {
    position: absolute;
    z-index: -1;
    content: "";
}
```

가상 요소를 카드 배경 뒤에 두면서 페이지 전체 뒤로 빠지는 것을 방지할 수 있다.

---

# z-index 시스템

프로젝트에서는 임의의 큰 숫자를 계속 추가하기보다 레이어 체계를 정의하는 것이 좋다.

```css
:root {
    --z-base: 0;
    --z-dropdown: 100;
    --z-sticky: 200;
    --z-fixed: 300;
    --z-overlay: 400;
    --z-modal: 500;
    --z-toast: 600;
}
```

사용 예제

```css
.header {
    z-index: var(--z-sticky);
}

.modal-overlay {
    z-index: var(--z-overlay);
}

.modal {
    z-index: var(--z-modal);
}
```

다만 CSS 변수의 값보다 Stacking Context 구조가 우선이다.

---

# Position과 Transform 이동

요소를 시각적으로 이동하는 방법에는 Position Offset과 Transform이 있다.

```css
.element {
    position: relative;
    top: 10px;
    left: 20px;
}
```

```css
.element {
    transform: translate(20px, 10px);
}
```

둘 다 화면상 이동할 수 있지만 동작과 성능 특성이 다르다.

---

# top과 left 이동

```css
.element {
    position: relative;
    top: 20px;
}
```

레이아웃 계산과 Paint에 영향을 줄 수 있다.

상태에 따라 주변 레이아웃 계산 비용이 발생할 수 있다.

---

# transform 이동

```css
.element {
    transform: translateY(20px);
}
```

Transform은 일반적으로 요소의 시각적 표현을 변경하며 원래 레이아웃 공간은 유지한다.

애니메이션에서 브라우저가 합성 단계로 처리하기 유리한 경우가 많다.

```css
.element {
    transition: transform 200ms;
}

.element:hover {
    transform: translateY(-4px);
}
```

---

# top/left와 transform 비교

| 구분 | top/left | transform |
|---|---|---|
| Position 필요 | O | X |
| 원래 공간 유지 | relative에서는 O | O |
| 레이아웃 계산 영향 | 발생 가능 | 상대적으로 적을 수 있음 |
| 애니메이션 활용 | 가능하지만 비용 주의 | 자주 권장 |
| Stacking Context 생성 | Position 조건에 따라 | 생성 가능 |
| Fixed 기준 영향 | 일반적 영향 없음 | 조상에 적용 시 영향 가능 |

---

# 실무 Position 패턴

# 카드 배지

HTML

```html
<article class="card">

    <span class="card__badge">
        NEW
    </span>

    <h2>
        CSS Position
    </h2>

</article>
```

CSS

```css
.card {
    position: relative;
}

.card__badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
    padding: 0.4em 0.8em;
    border-radius: 999px;
    background-color: #dc2626;
    color: white;
}
```

---

# 이미지 오버레이

HTML

```html
<figure class="thumbnail">

    <img
        src="./course.jpg"
        alt="CSS 강의 화면"
    >

    <figcaption class="thumbnail__caption">
        CSS Course
    </figcaption>

</figure>
```

CSS

```css
.thumbnail {
    position: relative;
    overflow: hidden;
}

.thumbnail img {
    display: block;
    width: 100%;
}

.thumbnail__caption {
    position: absolute;
    right: 0;
    bottom: 0;
    left: 0;
    padding: 2rem 1rem 1rem;
    background:
        linear-gradient(
            transparent,
            rgb(0 0 0 / 75%)
        );
    color: white;
}
```

---

# 알림 아이콘

HTML

```html
<button
    type="button"
    class="notification-button"
    aria-label="알림 3개"
>

    <span aria-hidden="true">
        🔔
    </span>

    <span class="notification-button__count">
        3
    </span>

</button>
```

CSS

```css
.notification-button {
    position: relative;
}

.notification-button__count {
    position: absolute;
    top: -0.35rem;
    right: -0.35rem;
    display: grid;
    min-width: 1.25rem;
    min-height: 1.25rem;
    padding-inline: 0.25rem;
    border-radius: 999px;
    background-color: #dc2626;
    color: white;
    font-size: 0.75rem;
    place-items: center;
}
```

---

# 드롭다운

HTML

```html
<div class="dropdown">

    <button
        type="button"
        class="dropdown__button"
    >
        메뉴
    </button>

    <ul class="dropdown__menu">
        <li>
            <a href="#">
                프로필
            </a>
        </li>
        <li>
            <a href="#">
                로그아웃
            </a>
        </li>
    </ul>

</div>
```

CSS

```css
.dropdown {
    position: relative;
}

.dropdown__menu {
    position: absolute;
    top: calc(100% + 0.5rem);
    right: 0;
    z-index: 100;
    min-width: 12rem;
    margin: 0;
    padding: 0.5rem;
    border: 1px solid #e5e7eb;
    border-radius: 0.75rem;
    background-color: white;
    box-shadow: 0 1rem 2rem rgb(0 0 0 / 15%);
    list-style: none;
}
```

`top: 100%`는 기준 요소 높이만큼 아래로 이동한다.

`calc(100% + 0.5rem)`을 사용하여 버튼 아래에 간격을 추가한다.

---

# 툴팁

HTML

```html
<span class="tooltip">

    <button
        type="button"
        aria-describedby="tooltip-description"
    >
        도움말
    </button>

    <span
        id="tooltip-description"
        role="tooltip"
        class="tooltip__content"
    >
        상세 설명입니다.
    </span>

</span>
```

CSS

```css
.tooltip {
    position: relative;
    display: inline-block;
}

.tooltip__content {
    position: absolute;
    bottom: calc(100% + 0.75rem);
    left: 50%;
    width: max-content;
    max-width: 16rem;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;
    background-color: #111827;
    color: white;
    transform: translateX(-50%);
}
```

툴팁은 화면 밖으로 넘칠 수 있으므로 실제 프로젝트에서는 JavaScript 기반 위치 계산 또는 Popover API 등을 고려할 수 있다.

---

# 모달 오버레이

HTML

```html
<div class="modal-layer">

    <div
        class="modal"
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
    >

        <h2 id="modal-title">
            저장 확인
        </h2>

        <p>
            변경 내용을 저장하시겠습니까?
        </p>

    </div>

</div>
```

CSS

```css
.modal-layer {
    position: fixed;
    inset: 0;
    z-index: 500;
    display: grid;
    padding: 1rem;
    background-color: rgb(0 0 0 / 60%);
    place-items: center;
}

.modal {
    width: min(100%, 32rem);
    max-height: calc(100dvh - 2rem);
    overflow-y: auto;
    padding: 2rem;
    border-radius: 1rem;
    background-color: white;
}
```

모달은 시각적 배치뿐 아니라 다음 접근성 처리가 필요하다.

- 열릴 때 모달 내부로 포커스 이동
- 닫힐 때 원래 요소로 포커스 복귀
- Escape로 닫기
- 배경 상호작용 차단
- 의미 있는 제목 연결
- Focus Trap 검토

---

# Toast 메시지

```css
.toast-container {
    position: fixed;
    top: 1rem;
    right: 1rem;
    z-index: 600;
    display: grid;
    gap: 0.75rem;
    width: min(calc(100% - 2rem), 24rem);
}

.toast {
    padding: 1rem;
    border-radius: 0.75rem;
    background-color: #111827;
    color: white;
    box-shadow: 0 1rem 2rem rgb(0 0 0 / 20%);
}
```

모바일에서는 화면 가장자리 간격을 고려해야 한다.

```css
.toast-container {
    right: max(1rem, env(safe-area-inset-right));
}
```

---

# Loading Overlay

HTML

```html
<div class="content" aria-busy="true">

    <div class="loading-overlay">

        <span class="spinner" aria-hidden="true"></span>

        <span class="visually-hidden">
            로딩 중
        </span>

    </div>

</div>
```

CSS

```css
.content {
    position: relative;
}

.loading-overlay {
    position: absolute;
    inset: 0;
    display: grid;
    background-color: rgb(255 255 255 / 75%);
    place-items: center;
}
```

부모 영역만 덮는 경우 `absolute`를 사용한다.

화면 전체를 덮는 경우 `fixed`를 고려한다.

---

# Skip Navigation

키보드 사용자가 반복되는 메뉴를 건너뛸 수 있도록 Skip Link를 제공할 수 있다.

HTML

```html
<a
    href="#main-content"
    class="skip-link"
>
    본문 바로가기
</a>
```

CSS

```css
.skip-link {
    position: fixed;
    top: 1rem;
    left: 1rem;
    z-index: 1000;
    padding: 0.75rem 1rem;
    background-color: #111827;
    color: white;
    transform: translateY(-200%);
}

.skip-link:focus {
    transform: translateY(0);
}
```

화면에서는 숨겨져 있다가 키보드 포커스를 받으면 표시된다.

---

# Position과 접근성

Position으로 요소를 화면 밖에 숨기는 경우 접근성을 함께 고려해야 한다.

```css
.element {
    position: absolute;
    left: -9999px;
}
```

과거에 화면 판독기용 텍스트에 사용되었지만 다음 문제가 발생할 수 있다.

- 매우 큰 스크롤 영역 생성 가능
- RTL 환경 문제
- 포커스 시 화면 이동
- 유지보수 어려움

현대적인 Visually Hidden 패턴을 사용하는 것이 좋다.

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

---

# 화면 순서와 DOM 순서

Position으로 요소의 시각적 위치를 크게 변경하더라도 키보드 포커스와 화면 판독기 순서는 DOM 순서를 따를 수 있다.

```html
<button>
    첫 번째
</button>

<button>
    두 번째
</button>
```

CSS로 두 번째 버튼을 화면 왼쪽 위에 배치해도 키보드 포커스는 DOM 순서대로 이동한다.

따라서 Position으로 콘텐츠의 논리 순서를 뒤섞지 않는 것이 좋다.

---

# Position과 Focus

고정 헤더가 Anchor 이동 대상이나 포커스 요소를 가릴 수 있다.

```css
section {
    scroll-margin-top: 6rem;
}
```

Anchor 링크 이동 시 고정 헤더 높이만큼 여백을 확보할 수 있다.

```css
:focus-visible {
    scroll-margin-top: 6rem;
}
```

---

# Scroll Padding

스크롤 컨테이너 전체에 고정 헤더 높이를 반영할 수 있다.

```css
html {
    scroll-padding-top: 5rem;
}
```

Anchor 이동이나 `scrollIntoView()`에서 상단 여백을 고려하는 데 유용하다.

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

    <title>CSS Position</title>

</head>

<body id="top">

    <a
        href="#main-content"
        class="skip-link"
    >
        본문 바로가기
    </a>

    <header class="header">

        <div class="header__inner">

            <a
                href="#top"
                class="logo"
            >
                Developer Wiki
            </a>

            <nav aria-label="주요 메뉴">

                <ul class="navigation">

                    <li>
                        <a href="#position-types">
                            Position
                        </a>
                    </li>

                    <li>
                        <a href="#stacking">
                            Stacking
                        </a>
                    </li>

                    <li>
                        <a href="#practice">
                            Practice
                        </a>
                    </li>

                </ul>

            </nav>

        </div>

    </header>

    <main id="main-content">

        <section class="hero">

            <div class="hero__content">

                <span class="hero__badge">
                    CSS Basic
                </span>

                <h1 class="hero__title">
                    CSS Position
                </h1>

                <p class="hero__description">
                    요소의 좌표 기준과 문서 흐름,
                    z-index와 Stacking Context를 학습합니다.
                </p>

                <a
                    href="#position-types"
                    class="button"
                >
                    학습 시작
                </a>

            </div>

            <div
                class="hero__decoration hero__decoration--one"
                aria-hidden="true"
            ></div>

            <div
                class="hero__decoration hero__decoration--two"
                aria-hidden="true"
            ></div>

        </section>

        <div class="content-layout">

            <aside class="sidebar">

                <nav aria-label="문서 목차">

                    <h2 class="sidebar__title">
                        목차
                    </h2>

                    <ul class="sidebar__list">

                        <li>
                            <a href="#position-types">
                                Position 종류
                            </a>
                        </li>

                        <li>
                            <a href="#stacking">
                                Stacking Context
                            </a>
                        </li>

                        <li>
                            <a href="#practice">
                                실무 활용
                            </a>
                        </li>

                    </ul>

                </nav>

            </aside>

            <div class="content">

                <section
                    id="position-types"
                    class="section"
                >

                    <span class="section__number">
                        01
                    </span>

                    <h2 class="section__title">
                        Position 종류
                    </h2>

                    <div class="card-grid">

                        <article class="card">

                            <span class="card__badge">
                                Flow
                            </span>

                            <h3 class="card__title">
                                Relative
                            </h3>

                            <p>
                                자신의 원래 위치를 기준으로 이동하고
                                원래 공간을 유지합니다.
                            </p>

                        </article>

                        <article class="card">

                            <span class="card__badge">
                                Out of Flow
                            </span>

                            <h3 class="card__title">
                                Absolute
                            </h3>

                            <p>
                                일반 흐름에서 제거되고 가장 가까운
                                기준 조상을 따라 배치됩니다.
                            </p>

                        </article>

                        <article class="card">

                            <span class="card__badge">
                                Viewport
                            </span>

                            <h3 class="card__title">
                                Fixed
                            </h3>

                            <p>
                                주로 Viewport를 기준으로 같은 화면 위치에
                                고정됩니다.
                            </p>

                        </article>

                    </div>

                </section>

                <section
                    id="stacking"
                    class="section"
                >

                    <span class="section__number">
                        02
                    </span>

                    <h2 class="section__title">
                        Stacking Context
                    </h2>

                    <div class="stack-demo">

                        <div class="stack-demo__item stack-demo__item--one">
                            z-index 1
                        </div>

                        <div class="stack-demo__item stack-demo__item--two">
                            z-index 2
                        </div>

                        <div class="stack-demo__item stack-demo__item--three">
                            z-index 3
                        </div>

                    </div>

                </section>

                <section
                    id="practice"
                    class="section"
                >

                    <span class="section__number">
                        03
                    </span>

                    <h2 class="section__title">
                        실무 활용
                    </h2>

                    <div class="image-card">

                        <img
                            src="./images/css-position.jpg"
                            alt="CSS Position 학습 화면"
                            class="image-card__image"
                        >

                        <div class="image-card__overlay">

                            <span class="image-card__category">
                                Frontend
                            </span>

                            <h3 class="image-card__title">
                                이미지 오버레이
                            </h3>

                        </div>

                    </div>

                </section>

            </div>

        </div>

    </main>

    <a
        href="#top"
        class="top-button"
        aria-label="페이지 상단으로 이동"
    >
        ↑
    </a>

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

    --header-height: 4.5rem;
    --content-width: 75rem;

    --z-base: 0;
    --z-decoration: 1;
    --z-content: 10;
    --z-sticky: 100;
    --z-fixed: 200;
    --z-skip: 1000;
}

html {
    box-sizing: border-box;
    scroll-padding-top: calc(var(--header-height) + 1rem);
    scroll-behavior: smooth;
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

img {
    display: block;
    max-width: 100%;
}

a {
    color: inherit;
}

.skip-link {
    position: fixed;
    top: 1rem;
    left: 1rem;
    z-index: var(--z-skip);
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;
    background-color: #111827;
    color: white;
    font-weight: 700;
    text-decoration: none;
    transform: translateY(-200%);
    transition: transform 150ms;
}

.skip-link:focus {
    transform: translateY(0);
}

.header {
    position: sticky;
    top: 0;
    z-index: var(--z-sticky);
    border-bottom: 1px solid var(--color-border);
    background-color: rgb(255 255 255 / 90%);
    backdrop-filter: blur(12px);
}

.header__inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: min(100% - 2rem, var(--content-width));
    min-height: var(--header-height);
    margin-inline: auto;
}

.logo {
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

.navigation a {
    display: inline-block;
    padding-block: 0.5rem;
    font-weight: 600;
    text-decoration: none;
}

.navigation a:hover {
    color: var(--color-primary);
}

.navigation a:focus-visible,
.button:focus-visible,
.top-button:focus-visible {
    outline: 3px solid var(--color-primary);
    outline-offset: 4px;
}

.hero {
    position: relative;
    isolation: isolate;
    display: grid;
    min-height: min(48rem, calc(100dvh - var(--header-height)));
    overflow: hidden;
    padding: clamp(5rem, 12vw, 10rem) max(1rem, 5vw);
    background:
        linear-gradient(
            135deg,
            #eff6ff,
            #dbeafe
        );
    place-items: center;
}

.hero__content {
    position: relative;
    z-index: var(--z-content);
    max-width: 55rem;
    text-align: center;
}

.hero__badge {
    display: inline-block;
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
    letter-spacing: -0.05em;
    line-height: 1;
}

.hero__description {
    max-width: 48ch;
    margin-inline: auto;
    color: var(--color-muted);
    font-size: clamp(1rem, 2vw, 1.25rem);
}

.button {
    display: inline-block;
    margin-top: 2rem;
    padding: 0.875em 1.75em;
    border-radius: 0.5rem;
    background-color: var(--color-primary);
    color: white;
    font-weight: 700;
    text-decoration: none;
}

.button:hover {
    background-color: var(--color-primary-dark);
}

.hero__decoration {
    position: absolute;
    z-index: var(--z-decoration);
    border-radius: 50%;
    filter: blur(2px);
    opacity: 0.55;
}

.hero__decoration--one {
    top: 10%;
    left: 5%;
    width: clamp(8rem, 20vw, 18rem);
    aspect-ratio: 1;
    background-color: #93c5fd;
}

.hero__decoration--two {
    right: 8%;
    bottom: 5%;
    width: clamp(10rem, 25vw, 22rem);
    aspect-ratio: 1;
    background-color: #bfdbfe;
}

.content-layout {
    display: grid;
    grid-template-columns: 15rem minmax(0, 1fr);
    gap: clamp(2rem, 6vw, 5rem);
    align-items: start;
    width: min(100% - 2rem, var(--content-width));
    margin-inline: auto;
    padding-block: clamp(4rem, 10vw, 8rem);
}

.sidebar {
    position: sticky;
    top: calc(var(--header-height) + 2rem);
}

.sidebar__title {
    margin-top: 0;
    color: var(--color-heading);
    font-size: 1rem;
}

.sidebar__list {
    display: grid;
    gap: 0.5rem;
    margin: 0;
    padding: 0;
    list-style: none;
}

.sidebar__list a {
    display: block;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;
    text-decoration: none;
}

.sidebar__list a:hover {
    background-color: #dbeafe;
    color: var(--color-primary-dark);
}

.content {
    min-width: 0;
}

.section {
    scroll-margin-top: calc(var(--header-height) + 2rem);
}

.section + .section {
    margin-top: clamp(5rem, 12vw, 10rem);
}

.section__number {
    color: var(--color-primary);
    font-size: 0.875rem;
    font-weight: 700;
}

.section__title {
    margin-block: 0.75rem 2rem;
    color: var(--color-heading);
    font-size: clamp(2rem, 5vw, 3.5rem);
    line-height: 1.2;
}

.card-grid {
    display: grid;
    grid-template-columns:
        repeat(
            auto-fit,
            minmax(
                min(100%, 16rem),
                1fr
            )
        );
    gap: 1.5rem;
}

.card {
    position: relative;
    min-height: 16rem;
    padding: 2rem;
    border: 1px solid var(--color-border);
    border-radius: 1rem;
    background-color: var(--color-surface);
    box-shadow: 0 1rem 3rem rgb(15 23 42 / 8%);
}

.card__badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
    padding: 0.35em 0.7em;
    border-radius: 999px;
    background-color: #dbeafe;
    color: var(--color-primary-dark);
    font-size: 0.75rem;
    font-weight: 700;
}

.card__title {
    margin-top: 3rem;
    color: var(--color-heading);
    font-size: 1.5rem;
}

.stack-demo {
    position: relative;
    isolation: isolate;
    min-height: 22rem;
    border: 1px solid var(--color-border);
    border-radius: 1rem;
    background-color: var(--color-surface);
}

.stack-demo__item {
    position: absolute;
    display: grid;
    width: 12rem;
    aspect-ratio: 1;
    border-radius: 1rem;
    color: white;
    font-weight: 700;
    place-items: center;
}

.stack-demo__item--one {
    top: 2rem;
    left: 2rem;
    z-index: 1;
    background-color: #60a5fa;
}

.stack-demo__item--two {
    top: 5rem;
    left: 7rem;
    z-index: 2;
    background-color: #2563eb;
}

.stack-demo__item--three {
    top: 8rem;
    left: 12rem;
    z-index: 3;
    background-color: #1e3a8a;
}

.image-card {
    position: relative;
    overflow: hidden;
    border-radius: 1rem;
    background-color: #111827;
}

.image-card__image {
    width: 100%;
    min-height: 24rem;
    object-fit: cover;
}

.image-card__overlay {
    position: absolute;
    right: 0;
    bottom: 0;
    left: 0;
    padding: 6rem 2rem 2rem;
    background:
        linear-gradient(
            transparent,
            rgb(0 0 0 / 85%)
        );
    color: white;
}

.image-card__category {
    font-size: 0.875rem;
    font-weight: 700;
}

.image-card__title {
    margin-block: 0.75rem 0;
    font-size: clamp(1.75rem, 5vw, 3rem);
}

.top-button {
    position: fixed;
    right: max(1rem, env(safe-area-inset-right));
    bottom:
        max(
            1rem,
            env(safe-area-inset-bottom)
        );
    z-index: var(--z-fixed);
    display: grid;
    width: 3rem;
    aspect-ratio: 1;
    border-radius: 50%;
    background-color: var(--color-primary);
    color: white;
    font-size: 1.25rem;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 0.75rem 2rem rgb(37 99 235 / 35%);
    place-items: center;
}

.top-button:hover {
    background-color: var(--color-primary-dark);
    transform: translateY(-3px);
}

@media (max-width: 48rem) {
    .navigation {
        display: none;
    }

    .content-layout {
        grid-template-columns: 1fr;
    }

    .sidebar {
        position: static;
    }

    .stack-demo__item {
        width: 9rem;
    }

    .stack-demo__item--three {
        left: 9rem;
    }
}

@media (prefers-reduced-motion: reduce) {
    html {
        scroll-behavior: auto;
    }

    *,
    *::before,
    *::after {
        scroll-behavior: auto;
        transition-duration: 0.01ms !important;
    }
}
```

---

# 예제 분석

```css
.header {
    position: sticky;
    top: 0;
}
```

헤더는 일반 흐름에 남아 있다가 Viewport 상단에 도달하면 붙는다.

---

```css
.hero {
    position: relative;
    isolation: isolate;
}
```

Hero 내부 절대 위치 장식의 기준을 만들고 새로운 Stacking Context를 명시적으로 생성한다.

---

```css
.hero__decoration {
    position: absolute;
}
```

장식 요소를 일반 흐름에서 제거하고 Hero 내부의 특정 좌표에 배치한다.

---

```css
.sidebar {
    position: sticky;
    top: calc(var(--header-height) + 2rem);
}
```

고정 헤더 아래에서 사이드바가 Sticky 상태로 유지된다.

---

```css
.card {
    position: relative;
}
```

카드 내부 배지의 Containing Block을 만든다.

---

```css
.card__badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
}
```

배지를 카드의 오른쪽 위에 배치한다.

---

```css
.stack-demo {
    isolation: isolate;
}
```

예제 내부의 Stacking Context를 외부 레이어와 분리한다.

---

```css
.image-card__overlay {
    position: absolute;
    right: 0;
    bottom: 0;
    left: 0;
}
```

오버레이가 이미지 하단의 전체 너비를 채운다.

---

```css
.top-button {
    position: fixed;
}
```

스크롤 위치와 관계없이 화면 오른쪽 아래에 유지된다.

---

```css
scroll-margin-top:
    calc(var(--header-height) + 2rem);
```

Anchor 이동 시 Sticky 헤더가 섹션 제목을 가리지 않도록 여백을 확보한다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|---|---|
| Position | 요소의 위치 계산 방식을 결정하는 속성 |
| Positioned Element | position이 static이 아닌 요소 |
| Normal Flow | 요소가 기본적으로 배치되는 문서 흐름 |
| static | 기본 문서 흐름에 따라 배치 |
| relative | 자신의 원래 위치를 기준으로 이동 |
| absolute | 흐름에서 제거되고 기준 조상을 따라 배치 |
| fixed | 주로 Viewport 기준으로 고정 |
| sticky | 흐름에 남다가 스크롤 임계점에서 고정 |
| Containing Block | 요소의 좌표와 크기 계산 기준 |
| Offset | top, right, bottom, left 위치 값 |
| inset | 네 방향 Offset 속기 |
| Logical Offset | 글쓰기 방향 기준 Offset |
| Viewport | 사용자가 보는 브라우저 표시 영역 |
| Scroll Container | 자체 스크롤 영역을 형성하는 요소 |
| z-index | 요소의 쌓임 수준 |
| Stacking Order | 요소가 그려지는 순서 |
| Stacking Context | 독립적으로 쌓임 순서를 계산하는 계층 |
| isolation | 새로운 Stacking Context를 의도적으로 생성 |
| Safe Area | 노치와 시스템 UI를 피해야 하는 화면 영역 |
| scroll-margin | 요소로 스크롤할 때 확보하는 외부 간격 |
| scroll-padding | 스크롤 컨테이너 내부의 기준 간격 |
| Shrink-to-fit | 콘텐츠에 맞춰 너비를 계산하는 방식 |
| Out of Flow | 일반 문서 흐름에서 제거된 상태 |

---

# 자주 하는 실수

## 1. top과 left를 작성했는데 요소가 움직이지 않는다

```css
.element {
    top: 10px;
    left: 20px;
}
```

`position` 기본값은 `static`이다.

```css
.element {
    position: relative;
    top: 10px;
    left: 20px;
}
```

---

## 2. relative 이동으로 레이아웃 간격을 만든다

```css
.element {
    position: relative;
    top: 50px;
}
```

원래 공간은 그대로 남아 다른 요소와 겹칠 수 있다.

간격이 목적이라면 `margin`, `padding`, `gap`을 사용한다.

---

## 3. absolute 자식의 부모에 기준을 만들지 않는다

```css
.badge {
    position: absolute;
    top: 0;
    right: 0;
}
```

예상과 다른 조상을 기준으로 배치될 수 있다.

```css
.card {
    position: relative;
}
```

---

## 4. 모든 부모에 position: relative를 적용한다

필요하지 않은 요소까지 Positioned Element와 Stacking Context 관련 복잡성을 늘릴 수 있다.

절대 위치 자식의 기준이 필요한 부모에만 적용한다.

---

## 5. absolute 요소가 공간을 유지한다고 생각한다

절대 위치 요소는 일반 흐름에서 제거된다.

다음 요소가 해당 공간을 채울 수 있다.

---

## 6. absolute 요소의 width가 항상 부모 전체라고 생각한다

`width: auto`인 절대 위치 요소는 콘텐츠 크기에 맞게 줄어들 수 있다.

전체 너비가 필요하면 다음과 같이 설정한다.

```css
.element {
    position: absolute;
    left: 0;
    right: 0;
}
```

---

## 7. fixed 헤더가 본문을 가린다

Fixed 요소는 흐름에서 제거된다.

헤더 높이만큼 본문 공간을 확보해야 한다.

---

## 8. fixed 요소가 Viewport 기준으로 동작하지 않는다

조상에 다음 속성이 있는지 확인한다.

- `transform`
- `filter`
- `perspective`
- `contain`
- `will-change`

---

## 9. sticky에 top을 지정하지 않는다

```css
.element {
    position: sticky;
}
```

```css
.element {
    position: sticky;
    top: 0;
}
```

---

## 10. sticky가 동작하지 않는데 overflow를 확인하지 않는다

조상의 `overflow`가 Sticky의 Scroll Container를 변경할 수 있다.

---

## 11. sticky 부모의 높이가 너무 작다

Sticky 요소는 부모 영역을 벗어나지 않는다.

부모 높이가 짧으면 고정 구간도 짧아진다.

---

## 12. Flex Item의 Sticky가 동작하지 않는다

교차축 Stretch로 인해 이동 공간이 부족할 수 있다.

```css
.sidebar {
    align-self: flex-start;
}
```

---

## 13. z-index 숫자만 계속 크게 만든다

```css
.element {
    z-index: 999999;
}
```

다른 Stacking Context 안에 있다면 숫자를 높여도 해결되지 않는다.

부모 Stacking Context 구조를 확인해야 한다.

---

## 14. opacity가 Stacking Context를 만든다는 점을 모른다

```css
.parent {
    opacity: 0.99;
}
```

자식의 `z-index` 동작이 외부와 분리될 수 있다.

---

## 15. transform이 Position 기준에 영향을 준다는 점을 모른다

조상의 `transform`은 Absolute 또는 Fixed 요소의 Containing Block에 영향을 줄 수 있다.

---

## 16. 모달을 absolute로 배치한다

페이지 전체를 덮어야 하는 모달은 보통 `fixed`가 적절하다.

```css
.modal-layer {
    position: fixed;
    inset: 0;
}
```

---

## 17. absolute로 모든 레이아웃을 만든다

콘텐츠 크기와 화면 크기 변화에 취약하다.

일반 레이아웃은 Normal Flow, Flexbox, Grid로 만들고 겹침이 필요한 요소만 Position을 사용한다.

---

## 18. Offset만으로 중앙 정렬한다

```css
.element {
    top: 50%;
    left: 50%;
}
```

요소의 왼쪽 위 모서리가 중앙에 위치한다.

```css
.element {
    transform: translate(-50%, -50%);
}
```

---

## 19. Fixed 하단 버튼에서 Safe Area를 고려하지 않는다

모바일 기기의 홈 인디케이터에 버튼이 가려질 수 있다.

```css
bottom:
    max(
        1rem,
        env(safe-area-inset-bottom)
    );
```

---

## 20. Position으로 DOM 순서를 무시한다

시각적 위치와 키보드 포커스 순서가 달라져 접근성이 떨어질 수 있다.

---

## 21. Sticky 헤더가 Anchor 제목을 가린다

```css
html {
    scroll-padding-top: 5rem;
}
```

또는

```css
section {
    scroll-margin-top: 5rem;
}
```

---

## 22. 툴팁이 overflow: hidden 부모에 잘린다

절대 위치 요소도 조상의 Overflow 영역 밖에서는 잘릴 수 있다.

DOM 위치 변경, Portal, Popover API 등을 검토한다.

---

## 23. Fixed 요소에 너무 낮은 z-index를 사용한다

다른 Stacking Context 뒤에 가려질 수 있다.

레이어 시스템과 부모 Context를 함께 확인한다.

---

## 24. z-index: auto와 z-index: 0을 같다고 생각한다

`z-index: 0`은 새로운 Stacking Context를 만들 수 있다.

---

## 25. 애니메이션에 top과 left만 사용한다

빈번한 위치 애니메이션에는 `transform`을 우선 검토한다.

```css
.element {
    transform: translateY(-4px);
}
```

---

# 면접 포인트

### Q1. position 속성의 주요 값을 설명해 보세요.

- `static`: 기본 문서 흐름
- `relative`: 원래 위치 기준 이동
- `absolute`: 흐름에서 제거되고 기준 조상을 따라 배치
- `fixed`: 주로 Viewport 기준 고정
- `sticky`: 흐름에 남다가 스크롤 임계점에서 고정

---

### Q2. relative와 absolute의 차이는 무엇인가요?

`relative`는 문서 흐름과 원래 공간을 유지한다.

`absolute`는 일반 흐름에서 제거되어 원래 공간을 차지하지 않는다.

---

### Q3. 부모에 position: relative를 적용하는 이유는 무엇인가요?

절대 위치 자식의 Containing Block을 부모로 설정하기 위해서이다.

---

### Q4. Containing Block이란 무엇인가요?

요소의 위치, 크기, 백분율 값 등을 계산할 때 기준이 되는 영역이다.

---

### Q5. absolute 요소는 어떤 조상을 기준으로 배치되나요?

일반적으로 가장 가까운 조상 중 `position`이 `static`이 아닌 요소를 기준으로 배치된다.

Transform 등 다른 속성이 기준을 형성할 수도 있다.

---

### Q6. absolute 요소의 width: auto는 어떻게 동작하나요?

일반 블록처럼 전체 너비를 채우지 않고 콘텐츠에 맞는 Shrink-to-fit 너비로 계산될 수 있다.

---

### Q7. left와 right를 동시에 지정하면 어떻게 되나요?

`width`가 `auto`라면 두 Offset 사이의 공간을 채우도록 너비가 늘어날 수 있다.

---

### Q8. fixed와 absolute의 차이는 무엇인가요?

`absolute`는 기준 조상을 따라 배치된다.

`fixed`는 일반적으로 Viewport를 기준으로 배치되어 스크롤해도 같은 화면 위치에 남는다.

---

### Q9. fixed가 Viewport 기준으로 동작하지 않는 경우는 무엇인가요?

조상에 `transform`, `filter`, `perspective`, `contain` 등이 적용되어 새로운 Containing Block이 형성된 경우이다.

---

### Q10. sticky와 fixed의 차이는 무엇인가요?

`sticky`는 문서 흐름과 공간을 유지하며 부모 영역 안에서만 고정된다.

`fixed`는 흐름에서 제거되고 일반적으로 Viewport에 고정된다.

---

### Q11. Sticky가 동작하지 않는 대표적인 이유는 무엇인가요?

- Offset이 없음
- 스크롤 공간 부족
- 부모 높이 부족
- 조상 Overflow
- Flex/Grid Stretch
- Sticky 요소가 너무 큼

---

### Q12. z-index는 무엇인가요?

겹치는 요소들의 쌓임 수준을 지정하는 속성이다.

---

### Q13. z-index가 큰데도 요소가 뒤에 표시되는 이유는 무엇인가요?

다른 Stacking Context 안에 속해 있기 때문이다.

부모 Stacking Context의 순서가 먼저 비교된다.

---

### Q14. Stacking Context란 무엇인가요?

내부 요소의 쌓임 순서를 독립적으로 계산하는 계층이다.

한 Context의 자식은 다른 Context의 자식과 직접 `z-index` 값을 비교하지 않는다.

---

### Q15. Stacking Context를 만드는 대표적인 속성은 무엇인가요?

- Position + 명시적 `z-index`
- `position: fixed`
- `position: sticky`
- `opacity < 1`
- `transform`
- `filter`
- `isolation: isolate`

---

### Q16. z-index: auto와 z-index: 0의 차이는 무엇인가요?

`auto`는 별도의 명시적 쌓임 수준을 만들지 않는 반면 `0`은 새로운 Stacking Context를 생성할 수 있다.

---

### Q17. isolation: isolate는 왜 사용하나요?

컴포넌트 내부의 Stacking Context를 외부와 분리하기 위해 사용한다.

---

### Q18. inset 속성은 무엇인가요?

`top`, `right`, `bottom`, `left`를 한 번에 지정하는 속기 속성이다.

---

### Q19. 절대 위치 중앙 정렬 방법을 설명해 보세요.

```css
.element {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
```

기준 영역의 중앙으로 이동한 뒤 자신의 크기 절반만큼 반대 방향으로 이동한다.

---

### Q20. Position과 Transform 이동의 차이는 무엇인가요?

Position Offset은 위치 계산 및 Paint에 영향을 줄 수 있다.

Transform은 시각적 변형으로 처리되며 애니메이션에 더 유리한 경우가 많다.

---

### Q21. Position을 언제 사용하고 Flexbox나 Grid를 언제 사용하나요?

일반적인 행과 열 레이아웃은 Flexbox나 Grid를 사용한다.

Position은 겹침, 오버레이, 특정 좌표 배치, 고정 UI에 사용한다.

---

### Q22. Sticky Table Header를 구현하는 방법은 무엇인가요?

```css
.table-wrapper {
    overflow: auto;
}

th {
    position: sticky;
    top: 0;
}
```

---

### Q23. Fixed Header가 Anchor 콘텐츠를 가릴 때 해결 방법은 무엇인가요?

`scroll-padding-top` 또는 `scroll-margin-top`을 사용한다.

---

### Q24. 모달에 position: fixed를 사용하는 이유는 무엇인가요?

문서 스크롤 위치와 관계없이 Viewport 전체를 덮고 화면 중앙에 유지하기 위해서이다.

---

### Q25. Position으로 요소를 화면 밖에 숨길 때 주의할 점은 무엇인가요?

키보드 포커스, 화면 판독기 노출, 스크롤 영역, RTL 환경을 고려해야 한다.

---

# 핵심 정리

- `position`은 요소의 좌표 계산 방식과 문서 흐름 참여 여부를 결정한다.
- `static`은 기본값이며 Offset이 적용되지 않는다.
- `relative`는 원래 위치를 기준으로 이동하고 원래 공간을 유지한다.
- `relative`는 절대 위치 자식의 기준을 만들 때 자주 사용한다.
- `absolute`는 일반 흐름에서 제거되고 가장 가까운 기준 조상을 따라 배치된다.
- 절대 위치 요소는 원래 공간을 차지하지 않는다.
- `left`와 `right`를 동시에 지정하면 요소를 가로로 Stretch할 수 있다.
- `inset`은 네 방향 Offset을 한 번에 지정한다.
- `fixed`는 일반적으로 Viewport 기준으로 고정된다.
- 조상의 `transform` 등은 Fixed의 기준을 변경할 수 있다.
- 모바일 Fixed UI에서는 동적 Viewport와 Safe Area를 고려한다.
- `sticky`는 흐름을 유지하다가 스크롤 임계점에서 고정된다.
- Sticky에는 `top` 등의 Offset이 필요하다.
- Sticky는 Scroll Container와 부모 영역의 영향을 받는다.
- `z-index`는 같은 Stacking Context 안에서만 단순하게 비교할 수 있다.
- 큰 `z-index` 숫자보다 Stacking Context 구조가 더 중요하다.
- `opacity`, `transform`, `filter`, `isolation` 등은 새로운 Stacking Context를 만들 수 있다.
- 프로젝트에서는 z-index 레이어 체계를 정의하는 것이 좋다.
- 단순 레이아웃은 Flexbox와 Grid를 우선 사용한다.
- Position은 배지, 오버레이, 모달, 툴팁, Sticky UI처럼 겹침이 필요한 상황에 사용한다.
- Position으로 시각적 순서를 바꿀 때 DOM 순서와 키보드 포커스를 고려해야 한다.
- 고정 헤더가 콘텐츠를 가릴 때 `scroll-margin`과 `scroll-padding`을 사용할 수 있다.
- 위치 애니메이션에는 `transform`을 우선 검토한다.
- Position 문제는 DevTools에서 Containing Block, Overflow, Stacking Context를 함께 확인해야 한다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-22 | 최초 작성 |
| v1.0 | 2026-07-22 | Normal Flow와 Positioned Element 개념 추가 |
| v1.0 | 2026-07-22 | static, relative, absolute 차이 정리 |
| v1.0 | 2026-07-22 | Containing Block 계산 원리 추가 |
| v1.0 | 2026-07-22 | absolute 너비와 Stretch 패턴 추가 |
| v1.0 | 2026-07-22 | Offset과 inset 논리적 속성 정리 |
| v1.0 | 2026-07-22 | fixed와 Viewport, Transform 관계 추가 |
| v1.0 | 2026-07-22 | 모바일 Safe Area와 Dynamic Viewport 추가 |
| v1.0 | 2026-07-22 | sticky와 Scroll Container 원리 추가 |
| v1.0 | 2026-07-22 | Sticky가 동작하지 않는 원인 정리 |
| v1.0 | 2026-07-22 | z-index와 Stacking Order 설명 추가 |
| v1.0 | 2026-07-22 | Stacking Context 생성 조건 추가 |
| v1.0 | 2026-07-22 | isolation과 레이어 시스템 추가 |
| v1.0 | 2026-07-22 | Position과 Transform 성능 비교 추가 |
| v1.0 | 2026-07-22 | 카드 배지, 툴팁, 드롭다운 패턴 추가 |
| v1.0 | 2026-07-22 | 모달, Toast, Loading Overlay 예제 추가 |
| v1.0 | 2026-07-22 | Skip Navigation과 접근성 내용 추가 |
| v1.0 | 2026-07-22 | 실무 예제 프로젝트 추가 |
| v1.0 | 2026-07-22 | 자주 하는 실수와 면접 포인트 추가 |