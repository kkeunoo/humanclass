---
title: CSS 선택자
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS 선택자

## 개요

CSS 선택자(Selector)는 HTML 문서에서 **스타일을 적용할 요소를 찾는 문법**이다.

HTML에 여러 요소가 존재하더라도 CSS가 어떤 요소에 스타일을 적용해야 하는지 자동으로 판단할 수는 없다.

따라서 개발자는 선택자를 사용하여 스타일을 적용할 대상을 지정해야 한다.

```css
p {
    color: red;
}
```

위 코드에서 `p`가 선택자이다.

```text
p
↓

HTML 문서의 모든 p 요소 선택

↓

color: red 적용
```

선택자는 CSS의 가장 기본적인 개념이면서, 우선순위, 상속, 레이아웃, JavaScript DOM 선택과도 밀접하게 연결된다.

---

# 핵심 개념

CSS 선택자는 다음과 같은 역할을 한다.

- HTML 태그 선택
- 특정 클래스 선택
- 특정 ID 선택
- 요소의 관계를 기준으로 선택
- 속성을 기준으로 선택
- 요소의 상태를 기준으로 선택
- 요소의 일부 영역을 선택
- 여러 요소를 한 번에 선택

대표적인 선택자 종류는 다음과 같다.

| 종류 | 문법 | 설명 |
|---|---|---|
| 전체 선택자 | `*` | 모든 요소 선택 |
| 태그 선택자 | `p` | 특정 태그 선택 |
| 클래스 선택자 | `.notice` | 특정 클래스를 가진 요소 선택 |
| ID 선택자 | `#header` | 특정 ID를 가진 요소 선택 |
| 그룹 선택자 | `h1, h2` | 여러 선택자를 한 번에 선택 |
| 자손 선택자 | `.menu a` | 내부에 포함된 모든 후손 선택 |
| 자식 선택자 | `.menu > li` | 바로 아래 자식 선택 |
| 인접 형제 선택자 | `h2 + p` | 바로 다음 형제 선택 |
| 일반 형제 선택자 | `h2 ~ p` | 이후에 등장하는 형제 선택 |
| 속성 선택자 | `input[type="text"]` | 속성을 기준으로 선택 |
| 가상 클래스 | `a:hover` | 요소의 상태를 기준으로 선택 |
| 가상 요소 | `p::before` | 요소의 특정 부분 선택 |

---

# 기본 문법

```css
선택자 {
    속성: 값;
}
```

예제

```css
h1 {
    color: royalblue;
}
```

```text
h1
↓

선택자

color
↓

속성

royalblue
↓

값
```

---

# 전체 선택자

전체 선택자 `*`는 문서의 모든 요소를 선택한다.

```css
* {
    margin: 0;
    padding: 0;
}
```

초기 스타일을 정리할 때 자주 사용한다.

```css
* {
    box-sizing: border-box;
}
```

주의할 점은 모든 요소를 대상으로 하므로 필요 이상으로 많은 스타일을 적용하지 않는 것이다.

---

# 태그 선택자

HTML 태그 이름으로 요소를 선택한다.

```css
h1 {
    color: blue;
}
```

```css
p {
    line-height: 1.6;
}
```

```css
button {
    cursor: pointer;
}
```

태그 선택자는 해당 태그가 사용된 모든 요소에 스타일을 적용한다.

HTML

```html
<p>첫 번째 문단</p>
<p>두 번째 문단</p>
```

CSS

```css
p {
    color: gray;
}
```

두 문단 모두 회색으로 표시된다.

---

# 클래스 선택자

클래스 선택자는 마침표(`.`)와 클래스 이름을 사용한다.

HTML

```html
<p class="notice">
    공지사항입니다.
</p>
```

CSS

```css
.notice {
    color: red;
}
```

하나의 클래스는 여러 요소에서 재사용할 수 있다.

```html
<button class="button">저장</button>
<button class="button">취소</button>
<a href="#" class="button">더보기</a>
```

```css
.button {
    padding: 10px 20px;
}
```

실무에서는 스타일을 재사용하기 쉽기 때문에 클래스 선택자를 가장 많이 사용한다.

---

# 여러 클래스 사용

하나의 요소에 여러 클래스를 지정할 수 있다.

```html
<button class="button button-primary button-large">
    회원가입
</button>
```

각 클래스에 역할을 나누어 스타일을 작성할 수 있다.

```css
.button {
    border: 0;
    cursor: pointer;
}

.button-primary {
    background-color: royalblue;
    color: white;
}

.button-large {
    padding: 16px 24px;
    font-size: 18px;
}
```

---

# 여러 클래스를 모두 가진 요소 선택

선택자 사이에 공백을 작성하지 않고 연결하면 여러 클래스를 동시에 가진 요소를 선택한다.

```html
<button class="button active">
    선택됨
</button>

<button class="button">
    선택되지 않음
</button>
```

```css
.button.active {
    background-color: royalblue;
}
```

`.button.active`는 `button` 클래스와 `active` 클래스를 모두 가진 요소를 선택한다.

다음 선택자와 의미가 다르다.

```css
.button .active {
}
```

`.button .active`는 `button` 클래스를 가진 요소 내부의 `active` 요소를 선택한다.

---

# ID 선택자

ID 선택자는 샵(`#`)과 ID 이름을 사용한다.

HTML

```html
<header id="header">
    헤더
</header>
```

CSS

```css
#header {
    background-color: black;
    color: white;
}
```

ID는 HTML 문서 안에서 하나의 요소를 고유하게 구분할 때 사용한다.

```html
<section id="course">
</section>
```

하나의 문서에서 같은 ID를 여러 번 사용하는 것은 피해야 한다.

---

# 클래스와 ID 선택자 비교

| 구분 | 클래스 선택자 | ID 선택자 |
|---|---|---|
| 문법 | `.class-name` | `#id-name` |
| 중복 사용 | 가능 | 문서에서 고유해야 함 |
| 재사용 | 높음 | 낮음 |
| CSS 우선순위 | ID보다 낮음 | 클래스보다 높음 |
| 실무 스타일링 | 주로 사용 | 제한적으로 사용 |
| JavaScript | 여러 요소 선택에 유용 | 고유 요소 선택에 유용 |

실무에서는 스타일링 목적으로 클래스 선택자를 우선 사용하는 것이 일반적이다.

---

# 그룹 선택자

쉼표(`,`)를 사용하면 여러 선택자에 같은 스타일을 적용할 수 있다.

```css
h1,
h2,
h3 {
    font-weight: 700;
}
```

다음과 같이 각각 작성한 것과 같은 결과이다.

```css
h1 {
    font-weight: 700;
}

h2 {
    font-weight: 700;
}

h3 {
    font-weight: 700;
}
```

중복 코드를 줄일 수 있다는 장점이 있다.

---

# 결합 선택자

결합 선택자는 HTML 요소 사이의 관계를 기준으로 대상을 선택한다.

대표적인 결합 선택자는 다음과 같다.

| 선택자 | 이름 | 설명 |
|---|---|---|
| `A B` | 자손 선택자 | A 내부의 모든 B |
| `A > B` | 자식 선택자 | A의 바로 아래 B |
| `A + B` | 인접 형제 선택자 | A 바로 다음의 B |
| `A ~ B` | 일반 형제 선택자 | A 이후에 있는 모든 형제 B |

---

# 자손 선택자

공백을 사용하여 요소 내부의 모든 후손 요소를 선택한다.

HTML

```html
<nav class="navigation">
    <ul>
        <li>
            <a href="#">홈</a>
        </li>
    </ul>
</nav>
```

CSS

```css
.navigation a {
    color: black;
}
```

`.navigation` 내부에 존재하는 모든 `<a>` 요소를 선택한다.

직접 자식뿐만 아니라 더 깊은 단계의 후손도 선택한다.

```text
.navigation
└── ul
    └── li
        └── a ← 선택
```

---

# 자식 선택자

`>`를 사용하여 바로 아래에 있는 자식 요소만 선택한다.

HTML

```html
<ul class="menu">
    <li>
        메뉴 1

        <ul>
            <li>하위 메뉴</li>
        </ul>
    </li>
</ul>
```

CSS

```css
.menu > li {
    border-bottom: 1px solid #ddd;
}
```

`.menu`의 바로 아래에 있는 `<li>`만 선택한다.

하위 `<ul>` 내부의 `<li>`는 선택하지 않는다.

---

# 자손 선택자와 자식 선택자 비교

```css
.menu li {
}
```

`.menu` 내부의 모든 `li`를 선택한다.

```css
.menu > li {
}
```

`.menu`의 바로 아래에 있는 `li`만 선택한다.

| 선택자 | 선택 범위 |
|---|---|
| `.menu li` | 모든 후손 |
| `.menu > li` | 바로 아래 자식 |

---

# 인접 형제 선택자

`+`를 사용하여 특정 요소의 바로 다음 형제 요소를 선택한다.

HTML

```html
<h2>제목</h2>
<p>첫 번째 문단</p>
<p>두 번째 문단</p>
```

CSS

```css
h2 + p {
    color: royalblue;
}
```

`h2` 바로 다음에 있는 첫 번째 `p`만 선택한다.

```text
h2
p ← 선택
p
```

---

# 일반 형제 선택자

`~`를 사용하여 특정 요소 이후에 등장하는 같은 부모의 형제 요소를 선택한다.

HTML

```html
<h2>제목</h2>
<p>첫 번째 문단</p>
<div>중간 콘텐츠</div>
<p>두 번째 문단</p>
```

CSS

```css
h2 ~ p {
    color: royalblue;
}
```

`h2` 이후에 등장하는 모든 형제 `p` 요소가 선택된다.

---

# 형제 선택자의 조건

형제 선택자는 반드시 같은 부모 요소를 가져야 한다.

```html
<section>
    <h2>제목</h2>
    <p>선택 가능</p>
</section>
```

다음처럼 부모가 다르면 형제 관계가 아니다.

```html
<section>
    <h2>제목</h2>
</section>

<div>
    <p>형제 관계가 아님</p>
</div>
```

---

# 속성 선택자

속성 선택자는 HTML 요소의 속성이나 속성값을 기준으로 선택한다.

```css
input[type="text"] {
    border: 1px solid gray;
}
```

HTML

```html
<input type="text">
<input type="password">
```

`type="text"`를 가진 요소만 선택한다.

---

# 속성 존재 선택자

특정 속성을 가진 요소를 선택한다.

```css
[disabled] {
    opacity: 0.5;
}
```

```html
<button disabled>사용 불가</button>
<button>사용 가능</button>
```

---

# 속성값 일치 선택자

속성값이 정확히 일치하는 요소를 선택한다.

```css
input[type="email"] {
    background-color: #f5f5f5;
}
```

---

# 속성값 포함 선택자

| 문법 | 의미 |
|---|---|
| `[attr~="value"]` | 공백으로 구분된 단어 중 일치 |
| `[attr|="value"]` | 값이 일치하거나 `value-`로 시작 |
| `[attr^="value"]` | 해당 값으로 시작 |
| `[attr$="value"]` | 해당 값으로 끝남 |
| `[attr*="value"]` | 해당 값을 포함 |

---

## 특정 값으로 시작

```css
a[href^="https"] {
    color: green;
}
```

`href` 값이 `https`로 시작하는 링크를 선택한다.

---

## 특정 값으로 끝남

```css
a[href$=".pdf"] {
    font-weight: bold;
}
```

PDF 파일 링크를 선택할 수 있다.

---

## 특정 값을 포함

```css
a[href*="github"] {
    color: black;
}
```

`href`에 `github`가 포함된 링크를 선택한다.

---

# 가상 클래스

가상 클래스(Pseudo-class)는 요소의 상태나 위치를 기준으로 선택한다.

콜론 하나(`:`)를 사용한다.

```css
a:hover {
    color: red;
}
```

대표적인 가상 클래스는 다음과 같다.

| 선택자 | 설명 |
|---|---|
| `:hover` | 마우스를 올린 상태 |
| `:active` | 요소를 누르는 상태 |
| `:focus` | 포커스를 받은 상태 |
| `:focus-visible` | 키보드 탐색 등으로 포커스가 표시되어야 하는 상태 |
| `:checked` | 체크된 상태 |
| `:disabled` | 비활성화된 상태 |
| `:enabled` | 활성화된 상태 |
| `:required` | 필수 입력 요소 |
| `:valid` | 유효성 검사를 통과한 상태 |
| `:invalid` | 유효성 검사를 통과하지 못한 상태 |
| `:first-child` | 첫 번째 자식 |
| `:last-child` | 마지막 자식 |
| `:nth-child()` | 순서를 기준으로 선택 |
| `:not()` | 특정 조건 제외 |
| `:is()` | 여러 조건을 하나로 묶음 |
| `:where()` | 여러 조건을 낮은 우선순위로 묶음 |

---

# hover

마우스 포인터가 요소 위에 올라간 상태를 선택한다.

```css
.button:hover {
    background-color: navy;
}
```

모바일 환경에는 마우스 hover가 없을 수 있으므로 중요한 기능을 hover에만 의존하면 안 된다.

---

# active

마우스나 터치로 요소를 누르는 순간의 상태이다.

```css
.button:active {
    transform: scale(0.98);
}
```

---

# focus

입력 요소나 버튼이 포커스를 받은 상태이다.

```css
input:focus {
    border-color: royalblue;
    outline: 2px solid royalblue;
}
```

접근성을 위해 포커스 표시를 아무 대안 없이 제거하지 않는 것이 중요하다.

좋지 않은 예

```css
button:focus {
    outline: none;
}
```

포커스 스타일을 제거했다면 명확한 대체 스타일을 제공해야 한다.

---

# focus-visible

키보드 탐색처럼 포커스 표시가 필요한 상황에 적용할 수 있다.

```css
button:focus-visible {
    outline: 3px solid royalblue;
    outline-offset: 3px;
}
```

마우스로 클릭했을 때보다 키보드 사용자를 중심으로 포커스 스타일을 제공할 수 있다.

---

# checked

체크된 라디오 버튼이나 체크박스를 선택한다.

```css
input:checked {
    accent-color: royalblue;
}
```

```html
<input type="checkbox" checked>
```

---

# disabled

비활성화된 입력 요소를 선택한다.

```css
button:disabled {
    cursor: not-allowed;
    opacity: 0.5;
}
```

---

# required

`required` 속성을 가진 입력 요소를 선택한다.

```css
input:required {
    border-left: 4px solid red;
}
```

---

# valid와 invalid

폼 입력값의 유효성 상태를 선택한다.

```css
input:valid {
    border-color: green;
}

input:invalid {
    border-color: red;
}
```

사용자가 입력하기 전부터 오류 스타일이 나타날 수 있으므로 실제 적용 시 사용자 경험을 고려해야 한다.

---

# first-child

부모 요소 안에서 첫 번째 자식인 요소를 선택한다.

```css
li:first-child {
    font-weight: bold;
}
```

HTML

```html
<ul>
    <li>첫 번째</li>
    <li>두 번째</li>
</ul>
```

첫 번째 `li`가 선택된다.

---

# last-child

부모 요소 안에서 마지막 자식인 요소를 선택한다.

```css
li:last-child {
    border-bottom: 0;
}
```

---

# nth-child

자식의 순서를 기준으로 선택한다.

```css
li:nth-child(2) {
    color: red;
}
```

두 번째 자식인 `li`를 선택한다.

---

## 홀수와 짝수 선택

```css
tr:nth-child(odd) {
    background-color: #f5f5f5;
}
```

```css
tr:nth-child(even) {
    background-color: white;
}
```

---

## 일정한 규칙 선택

```css
li:nth-child(3n) {
    color: red;
}
```

3의 배수 번째 요소를 선택한다.

```css
li:nth-child(3n + 1) {
    font-weight: bold;
}
```

1, 4, 7, 10번째 요소를 선택한다.

---

# nth-of-type

같은 태그 종류를 기준으로 순서를 계산한다.

```css
p:nth-of-type(2) {
    color: red;
}
```

`nth-child()`는 모든 자식 요소의 순서를 기준으로 하고, `nth-of-type()`은 같은 태그끼리의 순서를 기준으로 한다.

---

# not

특정 조건을 제외하고 선택한다.

```css
button:not(.primary) {
    background-color: gray;
}
```

`primary` 클래스를 가지지 않은 버튼을 선택한다.

```css
input:not([type="checkbox"]) {
    width: 100%;
}
```

---

# is

여러 선택자를 간단하게 묶을 수 있다.

```css
header h1,
main h1,
footer h1 {
    font-size: 32px;
}
```

다음과 같이 줄일 수 있다.

```css
:is(header, main, footer) h1 {
    font-size: 32px;
}
```

---

# where

`:where()`는 `:is()`처럼 여러 선택자를 묶지만, 선택자 자체의 우선순위가 `0`이라는 특징이 있다.

```css
:where(header, main, footer) a {
    color: inherit;
}
```

기본 스타일이나 쉽게 재정의해야 하는 스타일을 작성할 때 유용하다.

---

# 가상 요소

가상 요소(Pseudo-element)는 요소의 특정 부분이나 가상의 콘텐츠를 선택한다.

콜론 두 개(`::`)를 사용한다.

대표적인 가상 요소는 다음과 같다.

| 선택자 | 설명 |
|---|---|
| `::before` | 요소 내용 앞에 가상 요소 생성 |
| `::after` | 요소 내용 뒤에 가상 요소 생성 |
| `::first-letter` | 첫 번째 글자 선택 |
| `::first-line` | 첫 번째 줄 선택 |
| `::selection` | 사용자가 선택한 텍스트 영역 |
| `::placeholder` | 입력 요소의 placeholder 선택 |
| `::marker` | 목록의 마커 선택 |

---

# before

요소의 내용 앞에 가상의 콘텐츠를 생성한다.

```css
.required-label::before {
    content: "*";
}
```

```html
<label class="required-label">
    이름
</label>
```

`::before`와 `::after`를 사용할 때는 일반적으로 `content` 속성이 필요하다.

---

# after

요소의 내용 뒤에 가상의 콘텐츠를 생성한다.

```css
.external-link::after {
    content: " ↗";
}
```

```html
<a href="#" class="external-link">
    외부 사이트
</a>
```

---

# first-letter

첫 번째 글자를 선택한다.

```css
.article p::first-letter {
    font-size: 32px;
    font-weight: bold;
}
```

---

# first-line

텍스트의 첫 번째 줄을 선택한다.

```css
.article p::first-line {
    font-weight: bold;
}
```

화면 크기에 따라 첫 번째 줄의 범위가 달라질 수 있다.

---

# selection

사용자가 드래그하여 선택한 텍스트의 스타일을 변경한다.

```css
::selection {
    background-color: black;
    color: white;
}
```

---

# placeholder

입력 요소의 placeholder를 선택한다.

```css
input::placeholder {
    color: #999;
}
```

placeholder는 레이블을 대체하지 않는다.

---

# marker

목록 앞의 숫자나 불릿을 선택한다.

```css
li::marker {
    font-weight: bold;
}
```

---

# 가상 클래스와 가상 요소 차이

| 구분 | 가상 클래스 | 가상 요소 |
|---|---|---|
| 문법 | `:` | `::` |
| 대상 | 요소의 상태나 조건 | 요소의 일부 또는 가상 영역 |
| 예시 | `:hover` | `::before` |
| 예시 | `:checked` | `::after` |
| 예시 | `:nth-child()` | `::placeholder` |

---

# 선택자 조합

여러 선택자를 조합하여 구체적인 요소를 선택할 수 있다.

HTML

```html
<section class="course">
    <article class="card featured">
        <h2>HTML 과정</h2>
        <a href="#" class="button">신청하기</a>
    </article>
</section>
```

CSS

```css
.course .card.featured > .button:hover {
    background-color: royalblue;
}
```

선택 과정은 다음과 같다.

```text
.course
↓

course 클래스 내부

.card.featured
↓

card와 featured 클래스를 모두 가진 요소

> .button
↓

바로 아래 자식인 button 클래스

:hover
↓

마우스를 올린 상태
```

선택자를 지나치게 길게 작성하면 유지보수가 어려워질 수 있다.

---

# 선택자 이름 작성 방법

클래스와 ID 이름은 요소의 모양보다 역할이나 의미를 중심으로 작성하는 것이 좋다.

좋지 않은 예

```html
<div class="red-box">
```

색상이 변경되면 이름과 실제 스타일이 맞지 않을 수 있다.

권장 예

```html
<div class="error-message">
```

---

# 클래스 이름 표기 방식

대표적인 표기 방식은 다음과 같다.

## 케밥 케이스

```css
.course-card {
}
```

CSS 클래스 이름에서는 케밥 케이스를 많이 사용한다.

---

## 스네이크 케이스

```css
.course_card {
}
```

---

## 카멜 케이스

```css
.courseCard {
}
```

프로젝트 규칙에 따라 사용할 수 있지만 CSS에서는 케밥 케이스가 일반적이다.

---

# BEM 방법론

BEM은 클래스 이름을 구조적으로 작성하는 방법 중 하나이다.

```text
Block__Element--Modifier
```

예제

```html
<article class="card card--featured">
    <h2 class="card__title">
        HTML 과정
    </h2>

    <button class="card__button">
        신청하기
    </button>
</article>
```

```css
.card {
}

.card__title {
}

.card__button {
}

.card--featured {
}
```

| 구분 | 의미 |
|---|---|
| Block | 독립적인 컴포넌트 |
| Element | 블록 내부 구성 요소 |
| Modifier | 상태나 변형 |

BEM은 필수 규칙은 아니지만 클래스 이름 충돌을 줄이고 구조를 파악하는 데 도움이 된다.

---

# 선택자와 성능

브라우저는 선택자를 해석하여 해당하는 요소를 찾는다.

현대 브라우저에서는 일반적인 규모의 웹 페이지에서 선택자 성능보다 유지보수성과 명확성이 더 중요한 경우가 많다.

다만 다음과 같이 불필요하게 깊은 선택자는 피하는 것이 좋다.

```css
body main section article div ul li a span {
}
```

권장

```css
.navigation-label {
}
```

---

# 실무 활용

CSS 선택자는 다음과 같은 상황에서 사용한다.

- 공통 버튼 스타일
- 내비게이션 메뉴
- 카드 컴포넌트
- 폼 상태 표현
- 테이블 줄무늬
- 활성 메뉴 표시
- 모바일 메뉴 상태
- 접근성 포커스 표시
- 체크박스와 라디오 버튼 상태
- 가상 요소를 이용한 아이콘이나 장식

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

    <title>교육 과정</title>

</head>

<body>

    <header class="header">

        <h1 class="header__logo">
            Developer Academy
        </h1>

        <nav
            class="navigation"
            aria-label="주요 메뉴"
        >

            <ul class="navigation__list">

                <li class="navigation__item">

                    <a
                        href="#html"
                        class="navigation__link active"
                    >
                        HTML
                    </a>

                </li>

                <li class="navigation__item">

                    <a
                        href="#css"
                        class="navigation__link"
                    >
                        CSS
                    </a>

                </li>

                <li class="navigation__item">

                    <a
                        href="#javascript"
                        class="navigation__link"
                    >
                        JavaScript
                    </a>

                </li>

            </ul>

        </nav>

    </header>

    <main class="main">

        <section class="course-section">

            <h2 class="course-section__title">
                교육 과정
            </h2>

            <article
                id="html"
                class="course-card featured"
                data-level="basic"
            >

                <h3 class="course-card__title">
                    HTML
                </h3>

                <p class="course-card__description">
                    웹 페이지의 구조와 시맨틱 마크업을 학습합니다.
                </p>

                <button
                    type="button"
                    class="button button--primary"
                >
                    신청하기
                </button>

            </article>

            <article
                id="css"
                class="course-card"
                data-level="basic"
            >

                <h3 class="course-card__title">
                    CSS
                </h3>

                <p class="course-card__description">
                    웹 페이지의 디자인과 레이아웃을 학습합니다.
                </p>

                <button
                    type="button"
                    class="button button--primary"
                    disabled
                >
                    준비 중
                </button>

            </article>

        </section>

    </main>

</body>

</html>
```

## CSS

```css
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
}

.header {
    padding: 24px;
    background-color: #1f2937;
    color: white;
}

.header__logo {
    margin: 0;
}

.navigation__list {
    display: flex;
    gap: 20px;
    padding: 0;
    list-style: none;
}

.navigation__link {
    color: white;
    text-decoration: none;
}

.navigation__link:hover {
    text-decoration: underline;
}

.navigation__link.active {
    font-weight: bold;
}

.navigation__link:focus-visible {
    outline: 3px solid white;
    outline-offset: 4px;
}

.main {
    padding: 40px;
}

.course-card {
    padding: 24px;
    border: 1px solid #ddd;
}

.course-card + .course-card {
    margin-top: 20px;
}

.course-card.featured {
    border-color: royalblue;
}

.course-card[data-level="basic"] {
    background-color: #f8fafc;
}

.course-card__title::before {
    content: "📘 ";
}

.button {
    padding: 12px 20px;
    border: 0;
    cursor: pointer;
}

.button--primary {
    background-color: royalblue;
    color: white;
}

.button--primary:hover {
    background-color: navy;
}

.button:disabled {
    cursor: not-allowed;
    opacity: 0.5;
}
```

---

# 예제 선택자 분석

```css
.navigation__link.active {
}
```

`navigation__link`와 `active` 클래스를 모두 가진 요소를 선택한다.

```css
.course-card + .course-card {
}
```

`course-card` 바로 다음에 위치한 형제 `course-card`를 선택한다.

```css
.course-card[data-level="basic"] {
}
```

`course-card` 클래스와 `data-level="basic"` 속성을 모두 가진 요소를 선택한다.

```css
.button:disabled {
}
```

비활성화된 버튼을 선택한다.

```css
.course-card__title::before {
}
```

과정 제목 앞에 가상 콘텐츠를 생성한다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|---|---|
| Selector | 스타일 적용 대상을 찾는 문법 |
| Universal Selector | 모든 요소 선택 |
| Type Selector | 태그 이름으로 선택 |
| Class Selector | 클래스 이름으로 선택 |
| ID Selector | ID로 선택 |
| Group Selector | 여러 선택자를 한 번에 선택 |
| Descendant Selector | 모든 후손 선택 |
| Child Selector | 바로 아래 자식 선택 |
| Adjacent Sibling Selector | 바로 다음 형제 선택 |
| General Sibling Selector | 이후의 같은 부모 형제 선택 |
| Attribute Selector | 속성을 기준으로 선택 |
| Pseudo-class | 상태나 조건으로 선택 |
| Pseudo-element | 요소의 일부나 가상 영역 선택 |
| `:nth-child()` | 자식 순서를 기준으로 선택 |
| `:not()` | 특정 조건 제외 |
| `:is()` | 여러 조건을 묶어 선택 |
| `:where()` | 우선순위 없이 조건을 묶어 선택 |
| BEM | 클래스 이름 작성 방법론 |

---

# 자주 하는 실수

## 1. 클래스 선택자에서 마침표를 생략한다

잘못된 예

```css
notice {
    color: red;
}
```

올바른 예

```css
.notice {
    color: red;
}
```

---

## 2. ID 선택자에서 샵을 생략한다

잘못된 예

```css
header {
}
```

위 코드는 `<header>` 태그를 선택한다.

ID를 선택하려면 다음처럼 작성한다.

```css
#header {
}
```

---

## 3. 여러 클래스를 연결할 때 공백을 넣는다

```css
.button .active {
}
```

이 선택자는 `.button` 내부의 `.active` 요소를 의미한다.

두 클래스를 모두 가진 하나의 요소를 선택하려면 다음처럼 작성한다.

```css
.button.active {
}
```

---

## 4. 자손 선택자와 자식 선택자를 혼동한다

```css
.menu li {
}
```

모든 후손 `li`를 선택한다.

```css
.menu > li {
}
```

바로 아래 자식 `li`만 선택한다.

---

## 5. 그룹 선택자에 쉼표를 작성하지 않는다

```css
h1 h2 {
}
```

이 선택자는 `h1` 내부의 `h2`를 의미한다.

두 태그를 함께 선택하려면 쉼표를 사용한다.

```css
h1,
h2 {
}
```

---

## 6. hover에 중요한 기능을 전부 의존한다

모바일 환경이나 키보드 사용자에게는 동일한 경험이 제공되지 않을 수 있다.

---

## 7. focus 스타일을 대안 없이 제거한다

```css
button:focus {
    outline: none;
}
```

키보드 사용자가 현재 위치를 알기 어려워진다.

---

## 8. nth-child가 태그 종류만 계산한다고 생각한다

`:nth-child()`는 부모의 모든 자식 순서를 기준으로 계산한다.

같은 태그 종류만 계산하려면 `:nth-of-type()`을 고려한다.

---

## 9. before와 after에 content를 작성하지 않는다

```css
.icon::before {
}
```

가상 요소가 표시되지 않을 수 있다.

```css
.icon::before {
    content: "";
}
```

---

## 10. placeholder를 label 대신 사용한다

placeholder는 입력 후 사라지므로 입력 항목의 명확한 이름을 제공하기 어렵다.

---

## 11. ID 선택자를 스타일링에 과도하게 사용한다

ID 선택자는 우선순위가 높고 재사용하기 어려우므로 컴포넌트 스타일에는 클래스를 우선 고려한다.

---

## 12. 선택자를 지나치게 길게 작성한다

```css
body main section article div ul li a {
}
```

HTML 구조가 조금만 바뀌어도 스타일이 깨질 수 있다.

---

## 13. 클래스 이름을 모양만으로 작성한다

```css
.red-text {
}
```

스타일이 변경되면 클래스 이름과 역할이 맞지 않을 수 있다.

```css
.error-message {
}
```

역할 중심의 이름이 유지보수에 유리하다.

---

## 14. 속성 선택자에 따옴표를 잘못 작성한다

```css
input[type=text] {
}
```

일부 값에서는 동작할 수 있지만 일관성을 위해 문자열 값에 따옴표를 사용하는 것이 좋다.

```css
input[type="text"] {
}
```

---

## 15. 형제 선택자가 부모가 다른 요소도 선택한다고 생각한다

`+`와 `~`는 같은 부모를 가진 형제 사이에서만 동작한다.

---

# 면접 포인트

### Q1. CSS 선택자란 무엇인가요?

HTML 문서에서 스타일을 적용할 요소를 찾기 위한 문법이다.

---

### Q2. 클래스 선택자와 ID 선택자의 차이는 무엇인가요?

클래스는 여러 요소에서 재사용할 수 있고, ID는 문서 안에서 하나의 요소를 고유하게 식별하는 데 사용한다.

CSS 스타일링에는 일반적으로 클래스를 더 많이 사용한다.

---

### Q3. 자손 선택자와 자식 선택자의 차이는 무엇인가요?

자손 선택자는 특정 요소 내부의 모든 후손을 선택하고, 자식 선택자는 바로 아래 단계의 자식만 선택한다.

```css
.parent p {
}
```

모든 후손 `p`를 선택한다.

```css
.parent > p {
}
```

바로 아래 자식 `p`만 선택한다.

---

### Q4. 인접 형제 선택자와 일반 형제 선택자의 차이는 무엇인가요?

`A + B`는 A 바로 다음의 B 하나를 선택한다.

`A ~ B`는 A 이후에 등장하는 같은 부모의 모든 B를 선택한다.

---

### Q5. 속성 선택자는 언제 사용하나요?

`type`, `href`, `disabled`, `data-*`와 같은 HTML 속성이나 속성값을 기준으로 요소를 선택할 때 사용한다.

---

### Q6. 가상 클래스와 가상 요소의 차이는 무엇인가요?

가상 클래스는 요소의 상태나 조건을 선택하고, 가상 요소는 요소의 일부 영역이나 가상의 콘텐츠를 선택한다.

```css
.button:hover {
}
```

```css
.button::before {
}
```

---

### Q7. `:nth-child()`와 `:nth-of-type()`의 차이는 무엇인가요?

`:nth-child()`는 부모의 모든 자식을 기준으로 순서를 계산한다.

`:nth-of-type()`은 같은 태그 종류끼리 순서를 계산한다.

---

### Q8. `:focus`가 중요한 이유는 무엇인가요?

키보드 사용자가 현재 포커스된 요소를 확인할 수 있게 해 주므로 웹 접근성에 중요하다.

---

### Q9. `:is()`와 `:where()`의 차이는 무엇인가요?

둘 다 여러 선택자를 묶을 수 있다.

`:is()`는 내부 선택자 중 가장 높은 우선순위를 반영하지만, `:where()`의 선택자 우선순위는 항상 `0`이다.

---

### Q10. 실무에서 클래스 선택자를 주로 사용하는 이유는 무엇인가요?

스타일 재사용이 쉽고, ID보다 우선순위 관리가 편하며, 컴포넌트 단위로 구조화하기 좋기 때문이다.

---

### Q11. `::before`와 `::after`를 사용할 때 필요한 속성은 무엇인가요?

일반적으로 `content` 속성이 필요하다.

```css
.badge::before {
    content: "";
}
```

---

### Q12. 선택자를 지나치게 구체적으로 작성하면 어떤 문제가 있나요?

HTML 구조에 강하게 의존하고 우선순위가 높아져 재사용과 스타일 재정의가 어려워질 수 있다.

---

# 핵심 정리

- CSS 선택자는 HTML에서 스타일을 적용할 요소를 찾는 문법이다.
- 전체 선택자는 `*`, 클래스 선택자는 `.`, ID 선택자는 `#`을 사용한다.
- 실무 스타일링에서는 재사용하기 쉬운 클래스 선택자를 주로 사용한다.
- 쉼표는 여러 선택자를 그룹으로 묶는다.
- 공백은 모든 후손, `>`는 바로 아래 자식을 선택한다.
- `+`는 바로 다음 형제, `~`는 이후의 모든 형제를 선택한다.
- 속성 선택자는 HTML 속성이나 속성값을 기준으로 요소를 선택한다.
- 가상 클래스는 상태나 조건을 나타내며 콜론 하나를 사용한다.
- 가상 요소는 요소의 일부나 가상 콘텐츠를 나타내며 콜론 두 개를 사용한다.
- `:hover`, `:focus`, `:checked`, `:disabled`는 실무에서 자주 사용한다.
- `:nth-child()`와 `:nth-of-type()`은 순서를 계산하는 기준이 다르다.
- `::before`와 `::after`에는 일반적으로 `content` 속성이 필요하다.
- 선택자는 짧고 명확하며 재사용하기 쉽게 작성하는 것이 좋다.
- 클래스 이름은 색상이나 위치보다 요소의 역할과 의미를 중심으로 작성한다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-22 | 최초 작성 |
| v1.0 | 2026-07-22 | 기본 선택자와 그룹 선택자 정리 |
| v1.0 | 2026-07-22 | 자손, 자식, 형제 결합 선택자 설명 추가 |
| v1.0 | 2026-07-22 | 속성 선택자 문법과 활용 예제 추가 |
| v1.0 | 2026-07-22 | 가상 클래스와 폼 상태 선택자 정리 |
| v1.0 | 2026-07-22 | 가상 요소와 content 속성 설명 추가 |
| v1.0 | 2026-07-22 | 클래스 이름 작성 방법과 BEM 개념 추가 |
| v1.0 | 2026-07-22 | 실무 예제 프로젝트 및 선택자 분석 추가 |
| v1.0 | 2026-07-22 | 자주 하는 실수와 면접 포인트 추가 |