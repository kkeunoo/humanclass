# CSS 선택자와 적용 방법

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `01_CSS_선택자와_적용방법.md` |
| 분류 | `02_CSS` |
| 권장 선수 학습 | `01_HTML/08_HTML_시맨틱태그와_페이지구조.md` |
| 다음 학습 | `02_CSS_단위와_색상.md` |
| 원본 기준 | `workspace_me/workspace_html/css/01_selector.html`, `workspace_teacher/workspace_html/css/01_selector.html` |
| 핵심 범위 | CSS 문법, 적용 방법, 기본 선택자, 속성 선택자, 결합자, 가상 클래스, 가상 요소, 상속, 캐스케이드, 명시도 |
| 프로젝트 연결 | 공통 스타일, 메뉴, 폼 상태, 게시판, 컴포넌트 스타일, 유지보수 가능한 CSS |

> 이 문서는 수업 원본의 `01_selector.html`을 중심으로 작성했습니다. 원본에 직접 등장하지 않는 외부 스타일시트, 캐스케이드 계층, 최신 실무 작성 방식은 **확장 학습**으로 구분해 보완했습니다.

---

# 학습 목표

- CSS가 HTML에서 담당하는 역할을 설명한다.
- CSS 규칙의 선택자, 속성, 값 구조를 구분한다.
- 인라인, 내부, 외부 스타일 적용 방식을 비교한다.
- 전체, 타입, 클래스, ID 선택자를 작성한다.
- 그룹 선택자와 복합 선택자를 구분한다.
- 속성 선택자의 주요 연산자를 설명한다.
- 자손, 자식, 인접 형제, 일반 형제 결합자를 구분한다.
- `:hover`, `:active`, `:focus`, `:checked`, `:nth-child()`, `:not()`을 사용한다.
- `::before`, `::after`, `::selection`의 역할을 설명한다.
- 상속과 캐스케이드의 차이를 이해한다.
- 명시도를 단순한 한 줄 순위표가 아닌 계산 규칙으로 설명한다.
- `!important`와 인라인 스타일을 남용하지 않는다.
- 내 코드와 강사님 코드의 차이와 오류를 찾는다.
- 개발자 도구로 적용된 CSS와 덮어쓴 규칙을 확인한다.
- 클래스 중심의 유지보수 가능한 선택자를 설계한다.

---

# 1. CSS란?

CSS는 **Cascading Style Sheets**의 약자입니다.

HTML이 콘텐츠의 구조와 의미를 작성한다면 CSS는 다음과 같은 표현을 담당합니다.

- 글자 색상과 크기
- 배경색과 배경 이미지
- 너비와 높이
- 여백과 테두리
- 요소의 배치
- 반응형 화면
- 전환과 애니메이션
- 사용자 상태에 따른 표현

```html
<h1 class="page-title">Developer Wiki</h1>
```

```css
.page-title {
  color: navy;
  font-size: 2rem;
}
```

HTML의 `class="page-title"`은 요소에 재사용 가능한 이름을 부여합니다.

CSS의 `.page-title`은 그 이름을 가진 요소를 선택합니다.

---

# 2. CSS 기본 문법

CSS 규칙은 다음 구조로 작성합니다.

```css
선택자 {
  속성: 값;
}
```

예시:

```css
h1 {
  color: red;
  font-size: 48px;
}
```

| 구성 | 예시 | 역할 |
| --- | --- | --- |
| 선택자 | `h1` | 스타일을 적용할 요소를 찾는다. |
| 선언 블록 | `{ ... }` | 하나 이상의 선언을 묶는다. |
| 속성 | `color` | 변경할 스타일 종류 |
| 값 | `red` | 속성에 적용할 설정 |
| 콜론 | `:` | 속성과 값을 구분 |
| 세미콜론 | `;` | 선언과 선언을 구분 |

여러 선언은 줄을 나눠 작성하는 것이 읽기 쉽습니다.

```css
.card {
  width: 320px;
  padding: 24px;
  border: 1px solid #ddd;
  background-color: white;
}
```

마지막 선언의 세미콜론은 생략 가능한 경우도 있지만, 수정 과정의 실수를 줄이기 위해 항상 작성하는 습관이 좋습니다.

---

# 3. CSS 주석

CSS 주석은 `/*`와 `*/` 사이에 작성합니다.

```css
/* 한 줄 주석 */
```

```css
/*
  여러 줄
  주석
*/
```

HTML 주석과 문법이 다릅니다.

```html
<!-- HTML 주석 -->
```

```css
/* CSS 주석 */
```

다음은 CSS 주석이 아닙니다.

```css
// JavaScript 방식의 주석은 일반 CSS에서 사용하지 않는다.
```

## 3.1 주석 작성 기준

좋은 주석은 코드 자체만으로 알기 어려운 이유를 설명합니다.

```css
/* 고정 헤더 높이만큼 본문 시작 위치를 확보한다. */
main {
  padding-top: 80px;
}
```

다음처럼 코드 내용을 그대로 반복하는 주석은 유지보수 가치가 낮습니다.

```css
/* 글자색을 빨간색으로 변경 */
.title {
  color: red;
}
```

학습 단계에서는 속성의 의미를 기록하는 주석도 유용하지만, 실무 코드에서는 의도와 예외를 중심으로 남깁니다.

---

# 4. CSS 적용 방법

CSS를 HTML에 적용하는 대표적인 방법은 세 가지입니다.

1. 인라인 스타일
2. 내부 스타일시트
3. 외부 스타일시트

수업 원본은 `<style>`을 사용한 내부 방식과 `style` 속성을 사용한 인라인 방식을 직접 보여 줍니다.

외부 스타일시트 방식은 원본 `01_selector.html`에는 없지만, 실제 프로젝트의 기본 방식이므로 확장 학습으로 포함합니다.

---

# 5. 인라인 스타일

HTML 요소의 `style` 속성에 CSS를 직접 작성합니다.

```html
<div style="border: 1px solid black;">
  우선순위 연습
</div>
```

원본 코드의 `#div2` 요소에도 인라인 `border`가 작성되어 있습니다.

## 5.1 장점

- 한 요소에 즉시 적용할 수 있다.
- 간단한 테스트에서 결과를 빠르게 확인할 수 있다.
- JavaScript 라이브러리가 계산된 값을 삽입할 때 사용되기도 한다.

## 5.2 단점

- HTML과 CSS의 역할이 섞인다.
- 여러 요소에 재사용하기 어렵다.
- 같은 스타일을 반복하게 된다.
- 일반 스타일 규칙보다 명시도가 높아 덮어쓰기 어렵다.
- 상태 선택자나 미디어 쿼리를 직접 작성할 수 없다.

```html
<!-- 반복이 많아지는 예 -->
<p style="color: blue;">첫 번째 문장</p>
<p style="color: blue;">두 번째 문장</p>
<p style="color: blue;">세 번째 문장</p>
```

다음처럼 클래스로 묶는 것이 좋습니다.

```html
<p class="notice-text">첫 번째 문장</p>
<p class="notice-text">두 번째 문장</p>
<p class="notice-text">세 번째 문장</p>
```

```css
.notice-text {
  color: blue;
}
```

---

# 6. 내부 스타일시트

HTML 문서의 `<head>` 안에 `<style>` 요소를 작성합니다.

```html
<head>
  <style>
    .page-title {
      color: navy;
    }
  </style>
</head>
```

수업 원본의 모든 선택자 실습은 이 방식을 사용합니다.

## 6.1 장점

- 하나의 HTML 파일만으로 실습할 수 있다.
- 작은 데모나 단일 문서에 편리하다.
- 선택자와 HTML 구조를 동시에 확인하기 쉽다.

## 6.2 단점

- 여러 페이지에서 재사용하기 어렵다.
- 페이지마다 같은 CSS를 복사하게 될 수 있다.
- HTML 파일이 길어지고 관심사가 섞인다.

`<style>`은 메타데이터 영역인 `<head>` 안에 작성하는 것이 기본입니다.

원본 내 코드에는 “body에 있어도 적용은 됨”이라는 주석이 있습니다. 브라우저가 일부 위치의 `<style>`을 처리할 수는 있지만, 일반 페이지 스타일은 `<head>`에 두어 문서 구조와 로딩 의도를 명확히 하는 것이 좋습니다.

---

# 7. 외부 스타일시트

CSS를 별도 파일에 작성하고 HTML에서 `<link>`로 연결합니다.

```html
<head>
  <link rel="stylesheet" href="asset/css/main.css">
</head>
```

```css
/* asset/css/main.css */
.page-title {
  color: navy;
}
```

## 7.1 장점

- 여러 HTML 페이지가 같은 CSS를 공유할 수 있다.
- HTML과 CSS의 역할이 분리된다.
- 브라우저 캐시를 활용할 수 있다.
- 파일 구조와 유지보수가 좋아진다.
- 팀 작업과 코드 리뷰에 유리하다.

## 7.2 경로 주의

현재 HTML 파일에서 CSS 파일까지의 실제 상대 경로를 작성해야 합니다.

```text
project/
├── index.html
└── asset/
    └── css/
        └── main.css
```

```html
<link rel="stylesheet" href="asset/css/main.css">
```

다음처럼 경로가 틀리면 CSS가 적용되지 않습니다.

```html
<link rel="stylesheet" href="css/main.css">
```

## 7.3 연결 확인

개발자 도구에서 다음을 확인합니다.

- Network 탭에서 CSS 요청이 `200`인지
- Console에 파일 경로 오류가 없는지
- Elements의 Styles 영역에 규칙이 나타나는지

---

# 8. 세 가지 적용 방식 비교

| 구분 | 인라인 | 내부 스타일 | 외부 스타일 |
| --- | --- | --- | --- |
| 위치 | 요소의 `style` 속성 | HTML의 `<style>` | 별도 `.css` 파일 |
| 재사용 | 매우 낮음 | 한 문서 | 여러 문서 |
| 유지보수 | 어려움 | 소규모에 적합 | 가장 유리 |
| 상태 선택자 | 불가 | 가능 | 가능 |
| 미디어 쿼리 | 직접 작성 불가 | 가능 | 가능 |
| 대표 용도 | 임시 값, 동적 계산 | 실습, 단일 데모 | 실제 프로젝트 |
| 일반 권장도 | 제한적 | 상황에 따라 | 기본 선택 |

실무 기본 원칙:

```text
외부 스타일시트 중심
→ 컴포넌트 클래스 사용
→ 인라인 스타일은 명확한 이유가 있을 때만
```

---

# 9. 선택자란?

선택자는 CSS를 적용할 HTML 요소를 찾는 표현식입니다.

```css
h1 {
  color: red;
}
```

여기서 `h1`이 선택자입니다.

```css
#li1 {
  color: black;
}
```

여기서 `#li1`은 `id="li1"`인 요소를 선택합니다.

```css
.c1 {
  background-color: green;
}
```

여기서 `.c1`은 `class="c1"`을 가진 모든 요소를 선택합니다.

---

# 10. 전체 선택자 `*`

모든 요소를 선택합니다.

```css
* {
  color: red;
}
```

원본 코드에서는 모든 요소의 `color`를 빨간색으로 지정하는 실습에 사용했습니다.

## 10.1 정확히 이해하기

`*`는 문서의 요소들을 선택하지만, 모든 CSS 속성이 모든 요소에 같은 방식으로 보이는 것은 아닙니다.

예를 들어 `color`는 상속되는 속성이므로 부모에서 지정해도 자식 텍스트에 영향을 줄 수 있습니다.

```css
body {
  color: red;
}
```

초기 공통 설정에는 다음 패턴이 자주 사용됩니다.

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

전체 선택자는 편리하지만 모든 속성을 무차별적으로 지정하는 용도로 남용하지 않습니다.

---

# 11. 타입 선택자

HTML 태그 이름으로 요소를 선택합니다.

```css
h1 {
  font-size: 300%;
}
```

```css
h2 {
  font-size: 300%;
}
```

원본 코드에는 같은 선언을 각각 작성한 뒤 그룹 선택자로 합치는 과정이 있습니다.

타입 선택자는 다음과 같은 기본 스타일에 적합합니다.

```css
body {
  margin: 0;
}

img {
  max-width: 100%;
}

button {
  font: inherit;
}
```

하지만 특정 컴포넌트만 꾸미려는 경우 타입 선택자만 사용하면 적용 범위가 지나치게 넓을 수 있습니다.

```css
/* 모든 div에 영향을 줌 */
div {
  border: 1px solid red;
}
```

실무에서는 역할을 나타내는 클래스를 사용하는 편이 안전합니다.

```css
.priority-box {
  border: 1px solid red;
}
```

---

# 12. 그룹 선택자 `,`

여러 선택자에 같은 선언을 적용합니다.

```css
h1,
h2 {
  font-size: 300%;
}
```

쉼표는 각각의 독립된 선택자를 묶습니다.

```css
.page-title,
.section-title,
.card-title {
  font-weight: 700;
}
```

다음 두 코드는 의미가 다릅니다.

```css
h1,
h2 {
  color: red;
}
```

- 모든 `h1`
- 모든 `h2`

```css
h1 h2 {
  color: red;
}
```

- `h1` 내부에 있는 `h2`

제목 태그를 서로 중첩하는 구조는 일반적으로 사용하지 않으므로 두 번째 선택자는 실제로 매칭되지 않을 가능성이 큽니다.

---

# 13. ID 선택자 `#`

`id` 값 앞에 `#`을 붙입니다.

```css
#li1 {
  color: black;
}
```

```html
<li id="li1">li 1</li>
```

`id`는 한 문서에서 고유해야 합니다.

## 13.1 장점

- 특정 요소를 정확하게 선택할 수 있다.
- 내부 링크, `label`, JavaScript 식별에도 사용할 수 있다.

## 13.2 CSS에서의 주의점

ID 선택자는 명시도가 높습니다.

```css
#login-button {
  background-color: blue;
}
```

다른 클래스 규칙으로 덮어쓰기 어려워질 수 있습니다.

```css
.button {
  background-color: gray;
}
```

두 규칙이 같은 요소에 적용되면 ID 선택자의 배경색이 우선합니다.

재사용 가능한 UI 스타일은 클래스 중심으로 작성합니다.

```css
.button {
  /* 공통 버튼 */
}

.button--primary {
  /* 주요 버튼 */
}
```

ID는 다음 목적에 남겨 두는 경우가 많습니다.

- 문서 내 앵커
- 폼의 `label for`
- 접근성 연결
- JavaScript에서 고유 요소 식별

---

# 14. 클래스 선택자 `.`

클래스 값 앞에 `.`을 붙입니다.

```css
.c1 {
  background-color: green;
}
```

```html
<li class="c1">li 1</li>
```

클래스는 여러 요소에 반복 사용할 수 있습니다.

```html
<li class="menu-item">HTML</li>
<li class="menu-item">CSS</li>
<li class="menu-item">JavaScript</li>
```

```css
.menu-item {
  padding: 8px 12px;
}
```

하나의 요소가 여러 클래스를 가질 수도 있습니다.

```html
<li class="c1 bigText c2">li 2</li>
```

공백으로 클래스 이름을 구분합니다.

```text
c1
bigText
c2
```

실무 CSS는 대부분 클래스 선택자를 중심으로 설계합니다.

---

# 15. 여러 조건을 동시에 만족하는 복합 선택자

선택자를 공백 없이 붙이면 같은 요소가 모든 조건을 만족해야 합니다.

```css
h2.c1 {
  color: rgb(200, 100, 0);
}
```

의미:

- `h2` 요소이고
- `c1` 클래스를 가진 요소

```html
<h2 class="c1">부제목</h2>
```

여러 클래스도 붙일 수 있습니다.

```css
li.c1.c2 {
  background-color: yellow;
}
```

의미:

- `li` 요소이고
- `c1` 클래스가 있고
- `c2` 클래스도 있는 요소

```html
<li class="c1 bigText c2">li 2</li>
```

다음과 혼동하지 않습니다.

```css
.c1 .c2 {
  /* c1 요소 내부의 c2 요소 */
}
```

```css
.c1.c2 {
  /* 한 요소가 c1과 c2를 모두 가짐 */
}
```

---

# 16. 속성 선택자

속성 선택자는 요소의 속성 존재 여부나 값의 패턴으로 선택합니다.

원본 코드에는 다음 선택자가 등장합니다.

- `[readonly]`
- `[type=password]`
- `[id=li3]`
- `[href^=https]`
- `[href$=com]`
- `[class~=bigText]`
- `[human]`
- `[id^=title_]`

---

# 17. 속성 존재 선택자 `[attr]`

특정 속성이 존재하는 요소를 선택합니다.

```css
[readonly] {
  background-color: yellow;
}
```

```html
<input type="text" readonly>
```

속성값이 무엇인지와 관계없이 `readonly` 속성이 있으면 매칭됩니다.

실무 예:

```css
[disabled] {
  cursor: not-allowed;
  opacity: 0.6;
}
```

```css
[aria-current] {
  font-weight: 700;
}
```

---

# 18. 속성값 일치 선택자 `[attr=value]`

속성과 값이 정확히 일치하는 요소를 선택합니다.

```css
[type="password"] {
  background-color: pink;
}
```

원본은 다음처럼 따옴표 없이 작성했습니다.

```css
[type=password] {
  background-color: pink;
}
```

이 값은 식별자로 해석 가능한 단순 문자열이므로 동작할 수 있습니다. 그러나 공백이나 특수문자가 포함될 수 있는 값까지 일관되게 표현하려면 따옴표를 사용하는 습관이 좋습니다.

```css
input[type="checkbox"] {
  accent-color: green;
}
```

---

# 19. ID 선택자와 속성 선택자의 관계

원본에는 다음 설명이 있습니다.

```css
#li3 {
  /* id="li3" */
}
```

```css
[id="li3"] {
  /* id 속성값이 li3 */
}
```

두 선택자는 같은 요소를 선택할 수 있지만 **명시도는 다릅니다**.

| 선택자 | 분류 | 명시도 |
| --- | --- | --- |
| `#li3` | ID 선택자 | 높음 |
| `[id="li3"]` | 속성 선택자 | 클래스 계열 |

따라서 단순히 “완전히 같은 선택자”라고 이해하면 안 됩니다.

매칭 대상은 같을 수 있지만 캐스케이드에서의 힘은 다릅니다.

---

# 20. 시작 문자열 선택자 `^=`

속성값이 특정 문자열로 시작하는 요소를 선택합니다.

```css
[href^="https"] {
  color: purple;
}
```

```html
<a href="https://example.com">보안 연결</a>
```

실무 예:

```css
a[href^="mailto:"] {
  text-decoration-style: dotted;
}
```

```css
a[href^="tel:"] {
  white-space: nowrap;
}
```

---

# 21. 끝 문자열 선택자 `$=`

속성값이 특정 문자열로 끝나는 요소를 선택합니다.

```css
[href$=".pdf"] {
  font-weight: 700;
}
```

원본 예시는 다음과 같습니다.

```css
[href$="com"] {
  font-size: 30px;
}
```

주의할 점:

```html
<a href="https://example.com/path">
```

위 주소는 `com`이 아니라 `path`로 끝나므로 매칭되지 않습니다.

파일 확장자 표시에 유용합니다.

```css
a[href$=".zip"]::after {
  content: " ZIP";
}
```

---

# 22. 공백 구분 단어 선택자 `~=`

속성값을 공백으로 나눈 단어 중 하나가 정확히 일치할 때 선택합니다.

```css
[class~="bigText"] {
  color: blue;
}
```

```html
<li class="c1 bigText c2">li 2</li>
```

`class` 속성이 공백으로 여러 이름을 구분하기 때문에 `.bigText`와 비슷한 요소를 선택할 수 있습니다.

```css
.bigText {
  color: blue;
}
```

다만 `.bigText`가 더 간결하고 의도가 명확하므로 클래스에는 클래스 선택자를 사용합니다.

`~=`는 클래스에만 사용할 수 있는 연산자가 아닙니다.

공백으로 구분된 토큰을 가진 다른 속성에도 사용할 수 있습니다.

---

# 23. 추가 속성 선택자 확장

원본에는 직접 등장하지 않지만 함께 알아둘 연산자입니다.

| 선택자 | 의미 |
| --- | --- |
| `[attr]` | 속성이 존재 |
| `[attr="value"]` | 값이 정확히 일치 |
| `[attr^="value"]` | 값으로 시작 |
| `[attr$="value"]` | 값으로 끝남 |
| `[attr*="value"]` | 값을 포함 |
| `[attr~="value"]` | 공백 구분 단어 중 일치 |
| `[attr|="value"]` | 정확히 일치하거나 `value-`로 시작 |

예시:

```css
[class*="button"] {
  /* class 문자열 안에 button 포함 */
}
```

문자열 포함 선택자는 예상보다 넓게 매칭될 수 있으므로 명확한 클래스 선택자가 가능하면 클래스를 우선합니다.

---

# 24. 결합자란?

결합자는 요소 사이의 구조적 관계를 표현합니다.

| 결합자 | 이름 | 의미 |
| --- | --- | --- |
| 공백 | 자손 | 내부 모든 깊이 |
| `>` | 자식 | 바로 아래 한 단계 |
| `+` | 인접 형제 | 바로 다음 형제 하나 |
| `~` | 일반 형제 | 뒤에 오는 형제들 |

원본에는 자손, 자식, 인접 형제 결합자가 직접 등장합니다.

---

# 25. 자손 결합자

선택자 사이를 공백으로 구분합니다.

```css
div strong {
  color: blue;
}
```

의미:

- `div` 내부에 있는
- 모든 깊이의 `strong`

다음 두 요소가 모두 선택됩니다.

```html
<div>
  <strong>바로 아래 strong</strong>
</div>
```

```html
<div>
  <a href="#">
    <strong>더 깊이 있는 strong</strong>
  </a>
</div>
```

자손 선택자는 적용 범위가 넓습니다.

실무에서는 페이지 전체의 우연한 중첩에 의존하지 않도록 컴포넌트 클래스를 함께 사용합니다.

```css
.card strong {
  color: blue;
}
```

---

# 26. 자식 결합자 `>`

바로 아래 한 단계의 자식만 선택합니다.

```css
div > strong {
  font-size: 40px;
}
```

선택됨:

```html
<div>
  <strong>직접 자식</strong>
</div>
```

선택되지 않음:

```html
<div>
  <a href="#">
    <strong>손자 요소</strong>
  </a>
</div>
```

구조가 명확하고 직접 자식만 대상으로 삼아야 할 때 사용합니다.

```css
.menu > li {
  display: inline-block;
}
```

중첩 메뉴 안의 모든 `li`까지 선택하지 않고 최상위 메뉴 항목만 선택할 수 있습니다.

---

# 27. 인접 형제 결합자 `+`

기준 요소의 바로 다음 형제 하나를 선택합니다.

```css
input[type="checkbox"]:checked + span {
  text-decoration: line-through;
}
```

```html
<input type="checkbox">
<span>점심 먹기</span>
```

체크박스가 체크되면 바로 뒤의 `span`에 스타일이 적용됩니다.

다음처럼 사이에 다른 요소가 들어가면 선택되지 않습니다.

```html
<input type="checkbox">
<br>
<span>점심 먹기</span>
```

`+`는 “어떤 요소든 뒤에 있음”이 아니라 **바로 다음 형제**입니다.

---

# 28. 일반 형제 결합자 `~`

기준 요소 뒤에 오는 같은 부모의 형제들을 선택합니다.

```css
.toggle:checked ~ .panel {
  display: block;
}
```

```html
<input class="toggle" type="checkbox">
<p>설명</p>
<div class="panel">패널</div>
```

`panel`이 체크박스 바로 다음에 있지 않아도 같은 부모의 뒤쪽 형제이면 선택됩니다.

`+`와 비교:

```text
A + B  → A 바로 다음의 B
A ~ B  → A 뒤에 오는 형제 B
```

---

# 29. 가상 클래스

가상 클래스는 요소의 상태나 구조적 조건을 선택합니다.

콜론 하나를 사용합니다.

```css
선택자:가상클래스 {
  속성: 값;
}
```

원본에 등장하는 가상 클래스:

- `:hover`
- `:active`
- `:focus`
- `:checked`
- `:nth-child()`
- `:not()`

---

# 30. `:hover`

포인터가 요소 위에 올라간 상태를 선택합니다.

```css
#div1:hover {
  background-color: yellow;
}
```

실무 예:

```css
.button:hover {
  background-color: #1d4ed8;
}
```

주의:

- 터치 기기에는 마우스 호버와 같은 경험이 없을 수 있다.
- 중요한 정보나 기능을 호버에서만 제공하지 않는다.
- 링크와 버튼의 기본 상태도 명확해야 한다.

---

# 31. `:active`

요소가 활성화되는 순간, 일반적으로 마우스 버튼을 누르고 있는 동안의 상태입니다.

```css
#div1:active {
  background-color: green;
}
```

버튼을 눌렀을 때의 피드백에 사용할 수 있습니다.

```css
.button:active {
  transform: translateY(1px);
}
```

원본 내 코드에는 “자바스크립트로 적용하여 거의 쓰지 않음”이라는 주석이 있습니다. 그러나 `:active`는 JavaScript 없이도 즉각적인 눌림 상태를 표현하는 유효한 CSS 기능입니다. 사용 빈도는 디자인 시스템에 따라 달라지며, “거의 쓰지 않는다”로 일반화하기는 어렵습니다.

---

# 32. `:focus`

키보드, 마우스, 스크립트 등으로 요소가 포커스를 받은 상태입니다.

```css
.text1:focus {
  background-color: yellow;
}
```

접근성에서 매우 중요합니다.

```css
.form-input:focus {
  outline: 3px solid #93c5fd;
  outline-offset: 2px;
}
```

다음처럼 포커스 표시를 제거하고 대체 스타일을 제공하지 않으면 키보드 사용자가 현재 위치를 알기 어렵습니다.

```css
/* 권장하지 않음 */
button:focus {
  outline: none;
}
```

대체 포커스 스타일을 반드시 제공합니다.

---

# 33. `:focus-visible`

확장 학습입니다.

키보드 탐색처럼 포커스 표시가 특히 필요한 상황에서 스타일을 적용할 수 있습니다.

```css
.button:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}
```

프로젝트에서는 다음처럼 사용할 수 있습니다.

```css
.button:focus {
  /* 구형 환경을 위한 기본 포커스 */
}

.button:focus-visible {
  /* 명확한 키보드 포커스 */
}
```

포커스 디자인은 제거 대상이 아니라 설계 대상입니다.

---

# 34. `:checked`

체크박스나 라디오 버튼이 선택된 상태입니다.

```css
input[type="checkbox"]:checked {
  width: 20px;
  height: 20px;
}
```

원본에서는 체크 상태에 따라 입력 요소 크기를 변경했습니다.

다음처럼 인접 형제와 조합할 수 있습니다.

```css
.todo-checkbox:checked + .todo-label {
  color: #777;
  text-decoration: line-through;
}
```

```html
<input
  class="todo-checkbox"
  id="todo-lunch"
  type="checkbox"
>
<label class="todo-label" for="todo-lunch">
  점심 먹기
</label>
```

원본은 `span`을 사용했지만, 실제 체크박스 설명은 `label`을 연결하는 것이 접근성에 더 좋습니다.

---

# 35. `:nth-child()`

같은 부모의 자식 중 위치 조건에 맞는 요소를 선택합니다.

```css
#ul1 > li:nth-child(4) {
  color: black;
}
```

네 번째 자식이면서 `li`인 요소를 선택합니다.

## 35.1 홀수와 짝수

```css
#ul1 > li:nth-child(2n + 1) {
  background-color: gray;
}
```

`n`에 0, 1, 2, 3…이 들어갑니다.

```text
2 × 0 + 1 = 1
2 × 1 + 1 = 3
2 × 2 + 1 = 5
```

홀수 번째가 선택됩니다.

더 읽기 쉬운 키워드도 있습니다.

```css
li:nth-child(odd) {
  background-color: gray;
}
```

```css
li:nth-child(even) {
  background-color: #eee;
}
```

---

# 36. `:nth-child()`의 흔한 오해

```css
.card:nth-child(2) {
  ...
}
```

이는 “두 번째 `.card`”가 아니라 “부모의 두 번째 자식이면서 `.card`인 요소”를 뜻합니다.

```html
<div class="container">
  <h2>제목</h2>
  <article class="card">첫 번째 카드</article>
  <article class="card">두 번째 카드</article>
</div>
```

```css
.card:nth-child(2) {
  /* 첫 번째 card가 선택됨: 부모의 두 번째 자식이기 때문 */
}
```

타입별 위치가 필요하면 `:nth-of-type()`도 검토합니다.

```css
article:nth-of-type(2) {
  /* 두 번째 article */
}
```

---

# 37. `:not()`

괄호 안 조건에 해당하지 않는 요소를 선택합니다.

```css
#ul1 li:not(.c3) {
  font-size: 32px;
}
```

의미:

- `#ul1` 안의 `li`
- 단, `.c3` 클래스는 제외

실무 예:

```css
.menu-item:not(:last-child) {
  margin-right: 16px;
}
```

```css
.form-input:not([disabled]) {
  background-color: white;
}
```

복잡한 제외 규칙을 늘리기보다 명확한 클래스 구조로 해결할 수 있는지도 검토합니다.

---

# 38. 가상 요소

가상 요소는 요소의 특정 부분이나 생성된 표현 영역을 선택합니다.

일반적으로 콜론 두 개를 사용합니다.

```css
선택자::가상요소 {
  속성: 값;
}
```

원본에 등장하는 가상 요소:

- `::before`
- `::after`
- `::selection`

---

# 39. `::before`

요소 내용 앞에 생성된 상자를 만듭니다.

```css
h3::before {
  content: "before";
  color: black;
}
```

`content`가 필요합니다.

```css
.required-label::before {
  content: "*";
  color: red;
  margin-right: 4px;
}
```

중요한 정보는 가상 요소의 `content`에만 의존하지 않는 것이 좋습니다. 보조 기술과 복사 동작에서 기대와 다를 수 있기 때문입니다.

---

# 40. `::after`

요소 내용 뒤에 생성된 상자를 만듭니다.

```css
h3::after {
  content: "after";
  color: blue;
  font-size: 10px;
}
```

실무 예:

```css
.external-link::after {
  content: "↗";
  margin-left: 0.25em;
}
```

장식용으로 사용할 때는 의미 있는 본문을 대체하지 않습니다.

---

# 41. 가상 요소와 DOM

원본 내 코드에는 가상 요소를 “렌더링 요소”, 일반 요소를 “document 요소”로 구분하며 JavaScript가 가상 요소를 건드릴 수 없다고 기록했습니다.

더 정확한 설명은 다음과 같습니다.

- `::before`와 `::after`는 HTML에 실제 자식 노드로 추가되지 않는다.
- 일반적인 DOM 탐색으로 가상 요소 노드를 직접 얻을 수 없다.
- JavaScript는 클래스나 CSS 사용자 지정 속성을 변경해 가상 요소의 스타일을 간접 제어할 수 있다.
- `getComputedStyle(element, "::before")`로 계산된 스타일 일부를 읽을 수 있다.

```js
const title = document.querySelector(".title");
title.classList.add("title--new");
```

```css
.title--new::after {
  content: "NEW";
}
```

따라서 “JavaScript가 전혀 건드릴 수 없다”보다는 “독립적인 DOM 노드처럼 직접 선택·조작할 수 없다”가 정확합니다.

---

# 42. `::selection`

사용자가 텍스트를 드래그해 선택한 영역을 꾸밉니다.

```css
::selection {
  background-color: aqua;
}
```

범위를 제한할 수도 있습니다.

```css
.article-content::selection {
  color: white;
  background-color: navy;
}
```

지원되는 속성은 일반 요소보다 제한적일 수 있으므로 색상 중심으로 사용합니다.

---

# 43. 상속

상속은 일부 CSS 속성값이 부모에서 자식으로 전달되는 동작입니다.

```css
body {
  color: navy;
}
```

```html
<body>
  <p>이 글자는 navy를 상속받을 수 있다.</p>
</body>
```

대표적으로 상속되는 속성:

- `color`
- `font-family`
- `font-size`
- `font-weight`
- `line-height`
- `text-align`

대표적으로 상속되지 않는 속성:

- `width`
- `height`
- `margin`
- `padding`
- `border`
- `background-color`
- `display`

원본 01에서는 `color`가 여러 요소에 적용되는 모습이 나타나며, 다음 단원인 `02`에서는 `font-size` 상속과 상대 단위를 더 자세히 다룹니다.

---

# 44. 배경색이 자식에게 보이는 이유

부모의 `background-color`는 자식에게 상속되는 속성이 아닙니다.

```css
.parent {
  background-color: red;
}
```

자식 배경이 기본적으로 투명하기 때문에 부모의 빨간 배경이 뒤에서 보일 수 있습니다.

```css
.child {
  background-color: transparent;
}
```

이는 자식이 빨간색을 상속받은 것이 아닙니다.

자식에게 다른 배경을 지정하면 부모 배경을 가립니다.

```css
.child {
  background-color: white;
}
```

---

# 45. 캐스케이드

CSS의 `Cascading`은 여러 스타일 규칙이 한 요소의 같은 속성을 지정할 때 최종값을 결정하는 과정입니다.

단순히 “나중에 쓴 것이 이긴다”만으로 결정되지 않습니다.

브라우저는 대략 다음 요소를 고려합니다.

1. 출처와 중요도
2. 캐스케이드 레이어
3. 명시도
4. 범위 근접성 등 적용 조건
5. 코드 순서

입문 단계에서는 다음 세 가지를 우선 이해합니다.

- `!important` 여부
- 선택자의 명시도
- 같은 명시도라면 뒤에 작성된 규칙

---

# 46. 명시도

명시도는 선택자가 얼마나 구체적인지를 계산하는 규칙입니다.

간단히 다음 세 그룹으로 비교할 수 있습니다.

```text
ID 개수 - 클래스/속성/가상 클래스 개수 - 타입/가상 요소 개수
```

예시:

| 선택자 | 계산 | 비교 |
| --- | --- | --- |
| `div` | `0-0-1` | 타입 1 |
| `.c4` | `0-1-0` | 클래스 1 |
| `[human]` | `0-1-0` | 속성 1 |
| `#div2` | `1-0-0` | ID 1 |
| `#table .no` | `1-1-0` | ID 1 + 클래스 1 |
| `#table [id^="title_"]` | `1-1-0` | ID 1 + 속성 1 |
| `li.c1.c2` | `0-2-1` | 클래스 2 + 타입 1 |

각 자리의 숫자를 독립적으로 비교합니다.

`1-0-0`은 `0-100-100`보다 우선합니다. 단순히 점수를 100, 10, 1처럼 더하는 방식은 교육용 비유일 뿐 정확한 일반 규칙은 아닙니다.

---

# 47. 원본 우선순위 실습 분석

원본 요소:

```html
<div
  class="c4"
  id="div2"
  human="천안"
  style="border: 1px solid black;"
>
  우선 순위 연습
</div>
```

적용 후보:

```css
#div2 {
  border: 1px solid aqua;
}

[human] {
  border: 1px solid pink !important;
}

.c4 {
  border: 1px solid blue;
}

div {
  border: 1px solid red;
}
```

일반 선언만 비교하면:

```text
인라인 style
> #div2
> .c4 또는 [human]
> div
```

하지만 `[human]` 선언에 `!important`가 있으므로 최종 결과는 분홍색 테두리가 됩니다.

```css
[human] {
  border: 1px solid pink !important;
}
```

---

# 48. 원본의 한 줄 우선순위표 보완

원본에는 다음 취지의 주석이 있습니다.

```text
!important
> style 속성
> #id
> .class = 속성
> 태그
> *
> 브라우저 기본값
```

입문 설명으로 방향은 유용하지만 다음을 보완해야 합니다.

- `!important`는 선택자 종류가 아니라 선언의 중요도 표시다.
- 인라인 스타일에도 `!important`가 있을 수 있다.
- 사용자 스타일과 브라우저 스타일 등 출처도 영향을 준다.
- 명시도는 선택자의 구성 개수를 비교한다.
- `:not()` 자체는 명시도에 더해지지 않지만 내부 선택자는 영향을 준다.
- `:where()`는 내부 선택자가 있어도 명시도가 0이다.
- 상속값은 직접 매칭된 일반 선언보다 약하다.

초기 학습에서는 다음 흐름으로 판단하면 좋습니다.

```text
1. 같은 속성인가?
2. !important 여부가 같은가?
3. 명시도가 더 높은가?
4. 명시도도 같다면 뒤에 작성됐는가?
```

---

# 49. `!important`

```css
[human] {
  border: 1px solid pink !important;
}
```

해당 선언의 중요도를 높입니다.

## 49.1 문제점

- 일반 명시도 규칙으로 덮어쓰기 어렵다.
- 새로운 `!important`를 더 추가하게 된다.
- 컴포넌트 상태별 수정이 복잡해진다.
- 스타일의 출처를 추적하기 어려워진다.

## 49.2 제한적으로 고려할 상황

- 제어하기 어려운 외부 스타일을 임시로 덮어쓸 때
- 유틸리티 클래스 정책에서 의도적으로 사용하도록 설계했을 때
- 접근성을 위한 사용자 강제 스타일
- 매우 명확한 예외 규칙

대부분의 일반 컴포넌트 스타일에서는 선택자 구조와 CSS 순서를 먼저 개선합니다.

---

# 50. 같은 명시도라면 뒤의 선언

```css
.notice {
  color: blue;
}

.notice {
  color: red;
}
```

두 선택자의 명시도가 같고 중요도도 같으므로 뒤의 `red`가 적용됩니다.

한 규칙 안에서도 같은 속성을 반복하면 뒤의 값이 적용됩니다.

```css
.notice {
  color: blue;
  color: red;
}
```

이 패턴은 브라우저 지원을 위한 폴백에 의도적으로 쓰일 수 있지만, 이유 없는 중복은 제거합니다.

---

# 51. 직접 지정한 값과 상속값

```css
.parent {
  color: red;
}

.child {
  color: blue;
}
```

```html
<div class="parent">
  <span class="child">텍스트</span>
</div>
```

`child`에는 직접 지정한 파란색이 적용됩니다.

부모의 높은 명시도 선택자가 상속한 값보다 자식에 직접 매칭되는 낮은 명시도 규칙이 우선할 수 있습니다.

```css
#parent {
  color: red;
}

span {
  color: blue;
}
```

자식 `span`에는 직접 지정된 `blue`가 적용됩니다.

명시도는 **같은 요소에 직접 매칭된 선언들 사이**에서 비교해야 합니다.

---

# 52. 테이블 선택자 실습

원본 코드:

```css
#table .no {
  background-color: yellow;
}
```

의미:

- `id="table"` 요소 안에서
- `class="no"`인 요소 선택

```css
#table [id^="title_"] {
  border: 1px solid red;
}
```

의미:

- `id="table"` 요소 안에서
- `id` 값이 `title_`로 시작하는 요소 선택

원본 HTML:

```html
<table id="table">
  <tr>
    <td class="no">No</td>
    <td id="title_0">제목</td>
    <td>글쓴이</td>
  </tr>
</table>
```

실무에서는 반복되는 셀마다 고유 ID를 만드는 대신 역할 기반 클래스를 사용할 수도 있습니다.

```html
<td class="post-number">1</td>
<td class="post-title">제목 1</td>
```

```css
.post-number {
  background-color: yellow;
}

.post-title {
  border: 1px solid red;
}
```

데이터 식별이 필요하면 `data-*` 속성을 고려합니다.

```html
<td data-column="title">제목</td>
```

```css
[data-column="title"] {
  border: 1px solid red;
}
```

---

# 53. 사용자 정의 속성 주의

원본에는 다음 속성이 있습니다.

```html
<div human="천안">
```

브라우저가 속성을 보존하고 CSS의 `[human]`으로 선택할 수는 있지만, 사용자 정의 데이터를 표현할 때는 `data-*` 속성을 사용합니다.

```html
<div data-region="천안">
```

```css
[data-region] {
  border: 1px solid pink;
}
```

JavaScript에서도 표준 `dataset` 인터페이스로 접근할 수 있습니다.

```js
const element = document.querySelector("[data-region]");
console.log(element.dataset.region);
```

---

# 54. 선택자 작성 시 따옴표

원본:

```css
[type=password]
[href^=https]
[id^=title_]
```

다음처럼 작성하는 것이 일관되고 읽기 쉽습니다.

```css
[type="password"]
[href^="https"]
[id^="title_"]
```

따옴표 없이 사용할 수 있는 값도 있지만, 문자열이라는 사실을 명확히 하고 특수문자 문제를 줄일 수 있습니다.

---

# 55. My Code 분석

내 코드는 강사님 코드에 학습 과정의 해석과 관찰을 상세하게 추가했습니다.

## 55.1 장점

- 선택자마다 한국어 설명을 추가했다.
- 전체, 태그, ID, 클래스 선택자의 기호를 정리했다.
- 자손과 자식 선택자의 깊이 차이를 기록했다.
- 체크 상태와 인접 형제 선택자의 연결을 설명했다.
- `nth-child(2n + 1)` 계산 과정을 기록했다.
- 명시도 순서를 직접 주석으로 정리했다.
- 원본 결과를 확인하기 위한 HTML 예제를 보존했다.
- 강사님 코드보다 `readonly="readonly"`처럼 속성 형태를 명시적으로 실습했다.
- 테이블 선택자의 목적을 주석으로 표시했다.

학습 노트로서 “왜 적용되는가”를 기록한 점이 좋습니다.

---

# 56. My Code 개선점

## 56.1 `lang="en"`

문서 본문 대부분이 한국어이므로 다음이 적절합니다.

```html
<html lang="ko">
```

## 56.2 `style` 위치 설명

“body에 있어도 적용은 됨”보다는 다음 기준이 좋습니다.

```text
일반 문서 스타일은 head의 style 또는 외부 CSS에 작성한다.
```

브라우저가 잘못된 위치를 처리한다고 해서 권장 구조가 되는 것은 아닙니다.

## 56.3 전체 선택자 설명

```css
* {
  color: red;
}
```

`*`는 요소를 선택합니다. “head와 body가 모두 빨간색으로 보인다”기보다, 실제 시각 결과는 렌더링되는 요소와 상속 가능한 속성의 영향을 함께 받습니다.

## 56.4 `.을 빼면 일반 태그처럼 사용`

원본 주석의 이 표현은 오해할 수 있습니다.

```css
.c1 {
  /* class="c1" */
}
```

```css
c1 {
  /* 이름이 c1인 HTML 요소 */
}
```

마침표를 제거하면 같은 클래스를 선택하는 것이 아니라 `c1`이라는 타입 선택자로 해석됩니다.

표준 HTML 요소가 아닌 사용자 정의 요소처럼 매칭될 수 있으므로 의미가 완전히 달라집니다.

## 56.5 세미콜론 누락

```css
h2.c1 {
  color: rgb(200, 100, 0)
}
```

마지막 선언이라 동작할 수 있지만 다음처럼 세미콜론을 작성합니다.

```css
h2.c1 {
  color: rgb(200, 100, 0);
}
```

## 56.6 `:active` 설명

`:active`는 JavaScript로 대체해야 하는 낡은 기능이 아닙니다.

버튼을 누르는 순간의 시각 피드백에 여전히 유용합니다.

## 56.7 가상 요소 설명

가상 요소는 일반 DOM 노드로 직접 선택할 수 없지만 JavaScript로 관련 클래스나 사용자 지정 속성을 변경해 간접적으로 제어할 수 있습니다.

## 56.8 `grey`와 `gray`

두 키워드 모두 CSS에서 사용할 수 있습니다.

프로젝트에서는 하나의 표기를 일관되게 사용합니다.

```css
background-color: gray;
```

## 56.9 `human` 속성

사용자 정의 데이터는 다음처럼 작성합니다.

```html
<div data-human="천안">
```

또는 의미에 맞게:

```html
<div data-region="천안">
```

## 56.10 인라인 스타일

```html
<div style="border: 1px solid black;">
```

우선순위 실습에는 의미가 있지만 실제 컴포넌트에서는 클래스로 분리합니다.

---

# 57. Teacher Code 분석

강사님 코드는 선택자 학습 범위를 한 파일 안에서 순서대로 보여 줍니다.

진행 순서:

1. CSS 주석
2. 전체 선택자
3. 타입 선택자
4. 그룹 선택자
5. ID와 클래스
6. 속성 선택자
7. 복합 선택자
8. 자손과 자식
9. 상태 가상 클래스
10. 인접 형제
11. 구조 가상 클래스
12. 가상 요소
13. 우선순위
14. 테이블 응용

간결한 코드로 브라우저 결과를 빠르게 확인하기 좋습니다.

---

# 58. Teacher Code 개선점

## 58.1 중복 타입 선택자

```css
h2 {
  font-size: 300%;
}

h1 {
  font-size: 300%;
}

h1,
h2 {
  font-size: 300%;
}
```

그룹 선택자 학습을 위한 단계적 실습으로 이해할 수 있습니다.

최종 실무 코드에서는 중복 선언을 제거합니다.

```css
h1,
h2 {
  font-size: 300%;
}
```

## 58.2 속성값 따옴표

```css
[type=password]
```

다음 형태가 더 일관됩니다.

```css
[type="password"]
```

## 58.3 `human` 비표준 속성

속성 선택자 실습 자체는 동작하지만 데이터 목적이면 `data-*`를 권장합니다.

## 58.4 `border` HTML 속성

```html
<table id="table" border="1">
```

테두리 표현은 CSS로 이동합니다.

```html
<table id="table">
```

```css
#table {
  border-collapse: collapse;
}

#table th,
#table td {
  border: 1px solid #333;
}
```

## 58.5 문서 언어

```html
<html lang="en">
```

한국어 실습 문서라면 `lang="ko"`가 적절합니다.

## 58.6 닫는 구조 확인

강사님 원본 출력 범위에서는 마지막 `</body>`와 `</html>`이 보이지 않습니다. 실제 파일도 해당 닫는 태그가 누락되어 있습니다.

HTML에서는 브라우저가 자동 보정할 수 있지만 명시적으로 닫는 구조를 작성합니다.

```html
  </body>
</html>
```

---

# 59. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 전체 선택자 설명 | 적용 범위를 상세 기록 | 핵심 이름만 기록 |
| ID·클래스 | 고유성과 중복 사용 설명 | 예제 중심 |
| 속성 선택자 | 연산자 의미를 자세히 풀이 | 간결한 정의 |
| 자손·자식 | 깊이 차이를 문장으로 설명 | 예제와 짧은 주석 |
| `:active` | JavaScript로 거의 쓰지 않는다고 기록 | 클릭 상태라고 설명 |
| 가상 요소 | DOM과 렌더링 요소 해석 추가 | 콘텐츠 앞뒤 생성 설명 |
| 명시도 | 구체적일수록 우선이라는 설명 추가 | 순위표 중심 |
| HTML 주석 | 결과 관찰과 구조 설명이 많음 | 실습에 필요한 최소 주석 |
| `readonly` | `readonly="readonly"` | 불리언 속성 축약 |
| 테이블 | 각 선택 결과를 주석으로 표시 | Emmet 생성 주석 포함 |
| 닫는 태그 | `body`, `html` 닫힘 | 원본에서 누락 |
| 학습 성격 | 복습 노트형 | 수업 진행형 |

두 코드의 핵심 선택자와 실습 구조는 거의 같습니다. 내 코드는 강사님 코드에 학습 해설을 추가한 형태입니다.

---

# 60. 불리언 속성 표기

내 코드:

```html
<input type="text" readonly="readonly">
```

강사님 코드:

```html
<input type="text" readonly>
```

HTML에서는 둘 다 `readonly` 상태를 나타낼 수 있습니다.

일반적인 HTML 작성에서는 축약형이 간결합니다.

```html
<input type="text" readonly>
```

CSS 속성 존재 선택자는 두 형태 모두 선택합니다.

```css
[readonly] {
  background-color: yellow;
}
```

---

# 61. 실무 선택자 설계 원칙

## 61.1 클래스 중심

```css
.card {
  ...
}

.card-title {
  ...
}

.card-link {
  ...
}
```

## 61.2 HTML 구조에 지나치게 의존하지 않기

취약한 예:

```css
main section div ul li a {
  color: blue;
}
```

HTML 중간 구조가 바뀌면 선택자가 깨질 수 있습니다.

개선:

```css
.learning-link {
  color: blue;
}
```

## 61.3 지나치게 높은 명시도 피하기

```css
#app main .content .card .card-title {
  ...
}
```

개선:

```css
.card-title {
  ...
}
```

## 61.4 역할이 보이는 이름

```css
/* 모양만 나타내는 이름 */
.blue-text {
  color: blue;
}
```

색상이 바뀌면 이름과 실제 스타일이 어긋날 수 있습니다.

```css
/* 역할 중심 */
.help-text {
  color: blue;
}
```

모든 경우에 역할 이름만 정답은 아니며, 프로젝트의 디자인 시스템과 유틸리티 정책에 맞춰 일관성을 유지하는 것이 중요합니다.

---

# 62. BEM 기초

BEM은 클래스 이름을 구조화하는 방식 중 하나입니다.

```text
Block__Element--Modifier
```

예시:

```html
<article class="card card--featured">
  <h2 class="card__title">HTML</h2>
  <p class="card__description">HTML 문서입니다.</p>
</article>
```

```css
.card {
  border: 1px solid #ddd;
}

.card__title {
  font-size: 1.5rem;
}

.card--featured {
  border-color: gold;
}
```

| 구분 | 예 | 의미 |
| --- | --- | --- |
| Block | `.card` | 독립 컴포넌트 |
| Element | `.card__title` | 블록 내부 구성요소 |
| Modifier | `.card--featured` | 상태·변형 |

BEM은 필수 규칙이 아니라 선택 가능한 명명 방법입니다. 핵심은 팀이 이해할 수 있는 일관된 클래스 체계입니다.

---

# 63. 상태 클래스

JavaScript와 CSS가 협력할 때 상태를 클래스로 표현할 수 있습니다.

```html
<nav class="menu is-open">
```

```css
.menu {
  display: none;
}

.menu.is-open {
  display: block;
}
```

상태 이름 예:

- `.is-open`
- `.is-active`
- `.is-disabled`
- `.has-error`
- `.is-loading`

HTML의 실제 상태 속성을 사용할 수 있다면 먼저 검토합니다.

```html
<button aria-expanded="true">
  메뉴
</button>
```

```css
.menu-button[aria-expanded="true"] {
  background-color: #eee;
}
```

접근성 상태와 시각 상태를 하나의 속성으로 연결할 수 있습니다.

---

# 64. 선택자 깊이 줄이기

다음 선택자는 동작하지만 너무 깊습니다.

```css
#app .page main section .card-list article .title {
  color: navy;
}
```

문제점:

- HTML 구조 변경에 취약
- 명시도가 높음
- 재사용 어려움
- 덮어쓰기 어려움

개선:

```css
.card-title {
  color: navy;
}
```

컴포넌트 안에서 범위를 제한해야 한다면 짧게 유지합니다.

```css
.card .card-title {
  color: navy;
}
```

---

# 65. 선택자 성능에 대한 현실적인 기준

브라우저는 일반적인 규모의 페이지에서 대부분의 단순 선택자를 충분히 빠르게 처리합니다.

초보 단계에서 다음처럼 지나치게 미세한 성능 차이보다 유지보수성과 범위를 먼저 고려합니다.

```text
ID가 무조건 빠르니 ID만 사용
클래스보다 태그가 느리니 태그 금지
```

실제 우선순위:

1. 올바른 요소가 선택되는가?
2. 범위가 예상 가능한가?
3. 구조 변경에 견디는가?
4. 명시도가 관리 가능한가?
5. 코드가 읽기 쉬운가?
6. 실제 성능 문제가 측정되었는가?

매우 큰 DOM이나 반복적인 동적 렌더링에서 문제가 측정되면 프로파일링 후 개선합니다.

---

# 66. CSS Reset과 기본 스타일

브라우저는 요소마다 기본 스타일을 제공합니다.

예:

- `body`의 기본 여백
- 제목의 글자 크기와 여백
- 목록의 들여쓰기
- 링크 색상과 밑줄
- 버튼의 기본 글꼴

간단한 초기화 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
}

img,
picture,
video {
  display: block;
  max-width: 100%;
}

button,
input,
textarea,
select {
  font: inherit;
}
```

모든 기본 스타일을 무조건 제거하기보다 프로젝트에 필요한 기준을 정의합니다.

접근성에 유용한 포커스와 링크 구분까지 무분별하게 제거하지 않습니다.

---

# 67. CSS 파일 구조 예

작은 프로젝트:

```text
asset/
└── css/
    └── style.css
```

규모가 커지면 역할별로 나눌 수 있습니다.

```text
asset/
└── css/
    ├── reset.css
    ├── base.css
    ├── layout.css
    ├── components.css
    └── pages/
        └── home.css
```

HTML:

```html
<link rel="stylesheet" href="asset/css/reset.css">
<link rel="stylesheet" href="asset/css/base.css">
<link rel="stylesheet" href="asset/css/layout.css">
<link rel="stylesheet" href="asset/css/components.css">
```

파일을 너무 잘게 나누는 것이 항상 좋은 것은 아닙니다. 빌드 도구, 프로젝트 규모, 팀 규칙에 맞춰 결정합니다.

---

# 68. 권장 통합 예제

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
  <title>CSS 선택자 실습</title>
  <link rel="stylesheet" href="asset/css/selector.css">
</head>
<body>
  <main class="page">
    <h1 class="page__title">CSS 선택자</h1>

    <section class="selector-demo">
      <h2 class="selector-demo__title">
        할 일 목록
      </h2>

      <ul class="todo-list">
        <li class="todo-list__item">
          <input
            class="todo-list__checkbox"
            id="todo-study"
            type="checkbox"
          >
          <label
            class="todo-list__label"
            for="todo-study"
          >
            CSS 선택자 공부하기
          </label>
        </li>

        <li class="todo-list__item">
          <input
            class="todo-list__checkbox"
            id="todo-review"
            type="checkbox"
          >
          <label
            class="todo-list__label"
            for="todo-review"
          >
            문제 복습하기
          </label>
        </li>
      </ul>

      <a
        class="reference-link"
        href="https://example.com/selector.pdf"
      >
        선택자 참고 자료
      </a>
    </section>
  </main>
</body>
</html>
```

## CSS

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  color: #222;
  font-family: sans-serif;
}

.page {
  width: min(100% - 32px, 720px);
  margin-inline: auto;
}

.page__title,
.selector-demo__title {
  line-height: 1.2;
}

.todo-list {
  padding: 0;
  list-style: none;
}

.todo-list__item:not(:last-child) {
  margin-bottom: 12px;
}

.todo-list__checkbox:checked
+ .todo-list__label {
  color: #777;
  text-decoration: line-through;
}

.todo-list__checkbox:focus-visible
+ .todo-list__label {
  outline: 3px solid #93c5fd;
  outline-offset: 3px;
}

.reference-link[href^="https"] {
  color: #5b21b6;
}

.reference-link[href$=".pdf"]::after {
  content: " PDF";
  font-size: 0.75em;
}
```

---

# 69. 개발자 도구로 선택자 확인하기

## 69.1 Elements 탭

확인할 요소를 선택합니다.

다음 정보를 볼 수 있습니다.

- HTML 구조
- 클래스와 ID
- 인라인 스타일
- 브라우저가 보정한 DOM

## 69.2 Styles 영역

- 어떤 선택자가 매칭됐는가?
- 어떤 선언이 취소선 처리됐는가?
- 어느 파일 몇 번째 줄에서 왔는가?
- `!important`가 있는가?
- 가상 클래스 상태를 강제로 켤 수 있는가?

## 69.3 Computed 영역

최종 계산된 속성값을 확인합니다.

예:

```text
border-top-color
font-size
background-color
```

속성을 펼치면 어떤 규칙에서 왔는지 추적할 수 있습니다.

## 69.4 상태 강제 적용

개발자 도구에서 다음 상태를 강제로 켤 수 있습니다.

- `:hover`
- `:active`
- `:focus`
- `:focus-visible`

마우스를 계속 올려 두지 않고도 상태 스타일을 검수할 수 있습니다.

---

# 70. CSS가 적용되지 않을 때 점검 순서

1. CSS 파일 경로가 맞는가?
2. `<link rel="stylesheet">`가 있는가?
3. 선택자가 실제 HTML과 일치하는가?
4. 클래스의 철자가 같은가?
5. 속성명과 값에 오타가 없는가?
6. 중괄호와 세미콜론이 올바른가?
7. 더 높은 명시도 규칙이 덮고 있는가?
8. `!important`가 있는가?
9. 미디어 쿼리 조건 밖인가?
10. 브라우저 캐시 때문에 이전 파일이 보이는가?

예:

```html
<div class="big-text">텍스트</div>
```

```css
.bigText {
  font-size: 30px;
}
```

클래스 이름이 다르므로 적용되지 않습니다.

CSS 클래스는 대소문자를 일관되게 작성합니다.

---

# 71. 자주 하는 실수

## 71.1 클래스 기호 누락

```css
c1 {
  background-color: green;
}
```

이는 클래스가 아니라 `c1` 요소를 선택합니다.

```css
.c1 {
  background-color: green;
}
```

## 71.2 ID 기호 누락

```css
li1 {
  color: black;
}
```

```css
#li1 {
  color: black;
}
```

## 71.3 쉼표 누락

```css
h1 h2 {
  font-size: 300%;
}
```

이는 `h1` 안의 `h2`를 선택합니다.

```css
h1,
h2 {
  font-size: 300%;
}
```

## 71.4 공백 유무 혼동

```css
.c1.c2 {
  /* 같은 요소 */
}
```

```css
.c1 .c2 {
  /* c1 내부의 c2 */
}
```

## 71.5 자식과 자손 혼동

```css
div strong {
  /* 모든 깊이 */
}
```

```css
div > strong {
  /* 바로 아래 */
}
```

## 71.6 `+` 사이에 요소 삽입

```html
<input type="checkbox">
<br>
<span>할 일</span>
```

```css
input:checked + span {
  /* br 때문에 매칭되지 않음 */
}
```

## 71.7 `nth-child()`를 같은 타입의 순번으로 오해

부모의 전체 자식 순서를 기준으로 판단합니다.

## 71.8 `!important`로 모든 문제 해결

선택자 구조, 파일 순서, 명시도를 먼저 확인합니다.

## 71.9 ID 중심 스타일링

재사용이 어렵고 명시도가 높아집니다.

## 71.10 포커스 제거

```css
input:focus {
  outline: none;
}
```

대체 표시 없이 제거하지 않습니다.

---

# 72. 실무 개선 전후

## 개선 전

```html
<div id="content">
  <div id="list">
    <div class="item">
      <span>HTML</span>
    </div>
  </div>
</div>
```

```css
#content #list .item span {
  color: blue !important;
}
```

문제:

- ID가 중첩되어 명시도가 높다.
- HTML 구조에 강하게 의존한다.
- `!important`가 추가됐다.
- 재사용이 어렵다.

## 개선 후

```html
<article class="learning-card">
  <h2 class="learning-card__title">
    HTML
  </h2>
</article>
```

```css
.learning-card__title {
  color: blue;
}
```

선택자가 짧고 역할이 명확합니다.

---

# 73. 면접·복습 포인트

## Q1. CSS의 Cascading은 무엇인가요?

여러 CSS 선언이 같은 요소의 같은 속성에 적용될 때 중요도, 명시도, 순서 등의 규칙으로 최종값을 결정하는 과정입니다.

## Q2. 클래스 선택자와 ID 선택자의 차이는 무엇인가요?

클래스는 여러 요소에 재사용할 수 있고 CSS 컴포넌트 스타일에 적합합니다. ID는 문서에서 고유해야 하며 명시도가 더 높습니다.

## Q3. 자손 선택자와 자식 선택자의 차이는 무엇인가요?

자손 선택자는 내부 모든 깊이를 선택하고, 자식 선택자는 바로 아래 한 단계만 선택합니다.

## Q4. `.a.b`와 `.a .b`는 어떻게 다른가요?

`.a.b`는 한 요소가 두 클래스를 모두 가진 경우이고, `.a .b`는 `.a` 요소 내부의 `.b` 요소입니다.

## Q5. `:hover`와 `::before`의 콜론 수가 다른 이유는 무엇인가요?

`:hover`는 요소의 상태를 선택하는 가상 클래스이고, `::before`는 생성된 부분을 선택하는 가상 요소입니다.

## Q6. `!important`를 남용하면 안 되는 이유는 무엇인가요?

일반적인 명시도와 순서로 덮어쓰기 어려워지고 예외 규칙이 연쇄적으로 늘어나 유지보수가 어려워집니다.

## Q7. `[id="li3"]`과 `#li3`은 완전히 같은가요?

같은 요소를 매칭할 수 있지만 선택자 분류와 명시도가 다릅니다. `#li3`이 더 높은 명시도를 가집니다.

## Q8. 인라인 스타일보다 외부 스타일시트를 권장하는 이유는 무엇인가요?

재사용, 관심사 분리, 캐시, 유지보수, 상태 선택자와 반응형 작성에 유리하기 때문입니다.

## Q9. `background-color`는 상속되나요?

일반적으로 상속되지 않습니다. 자식 배경이 투명하면 부모 배경이 뒤에서 보일 수 있습니다.

## Q10. `:nth-child(2)`는 무엇을 기준으로 하나요?

선택 대상의 부모가 가진 전체 자식 중 두 번째 위치를 기준으로 합니다.

---

# Problems

## 문제 1. CSS 기본 문법

`h1`의 글자색을 `navy`, 글자 크기를 `40px`로 설정하세요.

## 문제 2. 외부 CSS 연결

다음 구조에서 `index.html`에 `style.css`를 연결하세요.

```text
project/
├── index.html
└── asset/
    └── css/
        └── style.css
```

## 문제 3. 선택자 작성

다음 요소를 각각 선택하는 CSS 선택자를 작성하세요.

1. 모든 `p`
2. `id="main-title"`
3. `class="card"`
4. `readonly` 속성이 있는 요소

## 문제 4. 그룹 선택자

`h1`, `h2`, `h3`에 모두 `font-weight: 700`을 적용하세요.

## 문제 5. 복합 선택자

`button` 요소이면서 `primary` 클래스를 가진 요소만 선택하세요.

## 문제 6. 여러 클래스

`card`와 `featured` 클래스를 모두 가진 하나의 요소만 선택하세요.

## 문제 7. 속성 선택자

다음 조건의 선택자를 작성하세요.

1. `type="password"`인 입력
2. `href`가 `https`로 시작하는 링크
3. `href`가 `.pdf`로 끝나는 링크
4. `id`가 `title_`로 시작하는 요소

## 문제 8. 자손과 자식

다음 HTML에서 모든 깊이의 `strong`을 선택하는 규칙과 직접 자식 `strong`만 선택하는 규칙을 각각 작성하세요.

```html
<div class="box">
  <strong>직접 자식</strong>
  <p>
    <strong>손자 요소</strong>
  </p>
</div>
```

## 문제 9. 체크된 할 일

체크박스가 체크되면 바로 뒤의 `label`에 취소선을 적용하세요.

```html
<input id="todo" type="checkbox">
<label for="todo">복습하기</label>
```

## 문제 10. 홀수 행

`.list`의 직접 자식 `li` 중 홀수 번째 항목의 배경색을 `#eee`로 지정하세요.

## 문제 11. 제외 선택자

`.menu-item` 중 `.is-active`가 아닌 요소만 선택하세요.

## 문제 12. 가상 요소

`.required` 요소 앞에 빨간색 `*` 문자를 추가하세요.

## 문제 13. 명시도 비교

다음 선택자를 명시도가 낮은 순서대로 나열하세요.

```css
div
.card
#app
div.card
#app .card
[data-state="open"]
```

## 문제 14. 최종 테두리 예측

다음 요소의 최종 테두리 색상을 작성하세요.

```html
<div
  id="box"
  class="item"
  style="border-color: black;"
>
  박스
</div>
```

```css
div {
  border: 1px solid red;
}

.item {
  border-color: blue;
}

#box {
  border-color: green;
}
```

## 문제 15. `!important` 포함 결과

다음에서 최종 테두리 색상을 작성하세요.

```css
#box {
  border-color: green;
}

.item {
  border-color: purple !important;
}
```

```html
<div
  id="box"
  class="item"
  style="border: 1px solid black;"
>
  박스
</div>
```

## 문제 16. 오류 찾기

다음 코드의 문제를 모두 찾아 수정하세요.

```html
<html lang="en">
<head>
  <link href="asset/style.css">
</head>
<body>
  <h1 class="pageTitle">제목</h1>
</body>
</html>
```

```css
pageTitle {
  color red
  font-size: 40px
}
```

## 문제 17. 접근 가능한 체크박스

원본의 다음 구조를 `label`을 사용하도록 개선하고, 체크 시 텍스트에 취소선을 적용하세요.

```html
<input type="checkbox">
<span>점심 먹기</span>
```

## 문제 18. 사용자 정의 데이터 속성

다음 비표준 속성을 `data-*` 형식으로 개선하고 해당 요소를 선택하세요.

```html
<div human="천안">천안 지점</div>
```

## 문제 19. 선택자 리팩터링

다음 선택자를 클래스 중심으로 단순화하세요.

```css
#app main section div ul li a {
  color: blue;
}
```

HTML도 필요한 만큼 수정하세요.

## 문제 20. 종합 실습

다음 요구사항을 만족하는 할 일 목록을 작성하세요.

- 외부 CSS 연결
- 항목 4개
- 체크박스와 `label` 연결
- 체크된 항목에 취소선
- 홀수 항목 배경색
- 마지막 항목을 제외하고 아래 여백
- 키보드 포커스 표시
- 클래스 중심의 선택자
- `!important` 사용 금지

---

# Answers & Explanations

## 정답 1

```css
h1 {
  color: navy;
  font-size: 40px;
}
```

선택자는 `h1`, 선언은 `color`와 `font-size`입니다.

## 정답 2

```html
<link rel="stylesheet" href="asset/css/style.css">
```

`rel="stylesheet"`와 현재 HTML 기준의 상대 경로가 필요합니다.

## 정답 3

```css
p {
}
```

```css
#main-title {
}
```

```css
.card {
}
```

```css
[readonly] {
}
```

## 정답 4

```css
h1,
h2,
h3 {
  font-weight: 700;
}
```

쉼표로 독립된 선택자를 묶습니다.

## 정답 5

```css
button.primary {
}
```

공백 없이 붙여 같은 요소의 두 조건을 표현합니다.

## 정답 6

```css
.card.featured {
}
```

`.card .featured`는 내부 자손을 의미하므로 다릅니다.

## 정답 7

```css
input[type="password"] {
}
```

```css
a[href^="https"] {
}
```

```css
a[href$=".pdf"] {
}
```

```css
[id^="title_"] {
}
```

## 정답 8

```css
.box strong {
  color: blue;
}
```

```css
.box > strong {
  font-size: 32px;
}
```

첫 번째는 모든 깊이, 두 번째는 직접 자식입니다.

## 정답 9

```css
input[type="checkbox"]:checked + label {
  text-decoration: line-through;
}
```

`label`은 입력 바로 다음 형제이므로 `+`를 사용할 수 있습니다.

## 정답 10

```css
.list > li:nth-child(odd) {
  background-color: #eee;
}
```

`2n + 1`로 작성해도 같습니다.

## 정답 11

```css
.menu-item:not(.is-active) {
}
```

`.is-active` 클래스를 가진 요소를 제외합니다.

## 정답 12

```css
.required::before {
  content: "*";
  color: red;
  margin-right: 0.25em;
}
```

`::before`와 `::after`에는 일반적으로 `content`가 필요합니다.

## 정답 13

낮은 순서:

```text
div
.card = [data-state="open"]
div.card
#app
#app .card
```

계산:

```text
div                  0-0-1
.card                 0-1-0
[data-state="open"]  0-1-0
div.card              0-1-1
#app                  1-0-0
#app .card            1-1-0
```

`.card`와 속성 선택자는 명시도가 같습니다. 같은 속성을 지정하면 뒤에 나온 규칙이 적용됩니다.

## 정답 14

최종 `border-color`는 `black`입니다.

인라인 스타일이 일반 ID, 클래스, 타입 선택자보다 높은 명시도를 가집니다.

`div`의 `border` 단축 속성은 초기 테두리를 만들고, 다른 규칙들이 색상 부분을 덮지만 최종적으로 인라인의 `border-color: black`이 적용됩니다.

## 정답 15

최종 색상은 `purple`입니다.

```css
.item {
  border-color: purple !important;
}
```

일반 인라인 선언에는 `!important`가 없으므로 중요한 선언이 우선합니다.

## 정답 16

### 수정 HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <link
    rel="stylesheet"
    href="asset/style.css"
  >
</head>
<body>
  <h1 class="pageTitle">제목</h1>
</body>
</html>
```

### 수정 CSS

```css
.pageTitle {
  color: red;
  font-size: 40px;
}
```

수정 사항:

1. `DOCTYPE` 추가
2. 한국어 문서에 `lang="ko"`
3. `<link>`에 `rel="stylesheet"` 추가
4. 클래스 선택자에 `.` 추가
5. 속성과 값 사이에 `:` 추가
6. 선언 끝에 `;` 추가

프로젝트 명명 규칙에 따라 `.page-title`처럼 케밥 케이스를 사용할 수도 있습니다.

## 정답 17

```html
<input
  class="todo-checkbox"
  id="todo-lunch"
  type="checkbox"
>
<label
  class="todo-label"
  for="todo-lunch"
>
  점심 먹기
</label>
```

```css
.todo-checkbox:checked + .todo-label {
  text-decoration: line-through;
}
```

텍스트를 클릭해도 체크박스를 변경할 수 있습니다.

## 정답 18

```html
<div data-region="천안">천안 지점</div>
```

```css
[data-region="천안"] {
  border: 1px solid pink;
}
```

사용자 정의 데이터는 `data-*` 속성으로 표현합니다.

## 정답 19

```html
<a class="learning-link" href="/html">
  HTML 학습
</a>
```

```css
.learning-link {
  color: blue;
}
```

HTML 중간 구조와 ID에 의존하지 않습니다.

## 정답 20

### HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>할 일 목록</title>
  <link rel="stylesheet" href="asset/css/todo.css">
</head>
<body>
  <main class="todo">
    <h1 class="todo__title">오늘의 할 일</h1>

    <ul class="todo__list">
      <li class="todo__item">
        <input
          class="todo__checkbox"
          id="todo-1"
          type="checkbox"
        >
        <label class="todo__label" for="todo-1">
          HTML 복습
        </label>
      </li>

      <li class="todo__item">
        <input
          class="todo__checkbox"
          id="todo-2"
          type="checkbox"
        >
        <label class="todo__label" for="todo-2">
          CSS 선택자 학습
        </label>
      </li>

      <li class="todo__item">
        <input
          class="todo__checkbox"
          id="todo-3"
          type="checkbox"
        >
        <label class="todo__label" for="todo-3">
          문제 풀이
        </label>
      </li>

      <li class="todo__item">
        <input
          class="todo__checkbox"
          id="todo-4"
          type="checkbox"
        >
        <label class="todo__label" for="todo-4">
          학습 기록 정리
        </label>
      </li>
    </ul>
  </main>
</body>
</html>
```

### CSS

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  color: #222;
  font-family: sans-serif;
}

.todo {
  width: min(100% - 32px, 640px);
  margin-inline: auto;
}

.todo__list {
  padding: 0;
  list-style: none;
}

.todo__item {
  padding: 12px;
}

.todo__item:nth-child(odd) {
  background-color: #eee;
}

.todo__item:not(:last-child) {
  margin-bottom: 8px;
}

.todo__checkbox:checked + .todo__label {
  color: #777;
  text-decoration: line-through;
}

.todo__checkbox:focus-visible + .todo__label {
  outline: 3px solid #60a5fa;
  outline-offset: 3px;
}
```

---

# Final Checklist

## CSS 문법

- [ ] 선택자 뒤에 중괄호를 작성했다.
- [ ] 속성과 값 사이에 콜론을 작성했다.
- [ ] 각 선언 끝에 세미콜론을 작성했다.
- [ ] CSS 주석을 `/* */`로 작성했다.
- [ ] 중괄호가 올바르게 닫혔다.

## 적용 방법

- [ ] 실제 프로젝트에서는 외부 스타일시트를 기본으로 사용했다.
- [ ] `<link rel="stylesheet">`를 작성했다.
- [ ] CSS 파일 경로를 확인했다.
- [ ] 인라인 스타일을 불필요하게 반복하지 않았다.
- [ ] 일반 `<style>`은 `<head>`에 배치했다.

## 선택자

- [ ] 클래스는 `.`으로 선택했다.
- [ ] ID는 `#`으로 선택했다.
- [ ] 그룹 선택자에 쉼표를 사용했다.
- [ ] 공백 유무에 따른 의미 차이를 확인했다.
- [ ] 자손과 자식 선택자를 구분했다.
- [ ] `+`가 바로 다음 형제만 선택함을 확인했다.
- [ ] 속성값을 따옴표로 명확하게 작성했다.
- [ ] `:nth-child()`가 부모의 전체 자식 순서를 기준으로 함을 확인했다.

## 접근성

- [ ] `:focus` 또는 `:focus-visible` 표시를 제거하지 않았다.
- [ ] 체크박스와 라디오에 `label`을 연결했다.
- [ ] 호버 상태에서만 중요한 정보를 제공하지 않았다.
- [ ] 가상 요소가 핵심 텍스트를 대체하지 않았다.
- [ ] 링크는 링크, 동작은 버튼을 사용했다.

## 유지보수

- [ ] 클래스 중심으로 스타일을 작성했다.
- [ ] ID 선택자를 스타일 목적으로 남용하지 않았다.
- [ ] 선택자 깊이가 지나치게 길지 않다.
- [ ] HTML 구조에 불필요하게 의존하지 않는다.
- [ ] `!important`를 습관적으로 사용하지 않았다.
- [ ] 비표준 사용자 속성 대신 `data-*`를 사용했다.
- [ ] 같은 선언의 중복을 제거했다.
- [ ] 개발자 도구에서 덮어쓴 규칙을 확인했다.

---

# Key Summary

- CSS는 HTML 콘텐츠의 표현과 배치를 담당한다.
- CSS 규칙은 `선택자 { 속성: 값; }` 구조로 작성한다.
- 실제 프로젝트에서는 외부 스타일시트를 기본으로 사용한다.
- 인라인 스타일은 재사용과 유지보수가 어려우며 명시도가 높다.
- 전체 선택자는 `*`, 타입 선택자는 태그 이름을 사용한다.
- 클래스는 `.class`, ID는 `#id` 형식으로 선택한다.
- 쉼표는 여러 독립 선택자를 그룹으로 묶는다.
- 선택자를 붙이면 같은 요소의 복수 조건, 공백을 넣으면 자손 관계다.
- 속성 선택자는 존재, 정확한 값, 시작, 끝, 토큰 등의 조건을 표현한다.
- 자손은 모든 깊이, 자식은 바로 아래 한 단계다.
- `+`는 바로 다음 형제, `~`는 뒤쪽 일반 형제를 선택한다.
- 가상 클래스는 상태와 위치를, 가상 요소는 요소의 특정 표현 부분을 선택한다.
- `:focus` 스타일은 키보드 접근성에 중요하다.
- `::before`와 `::after`는 독립 DOM 노드가 아니다.
- 상속과 캐스케이드는 서로 다른 개념이다.
- 명시도는 ID, 클래스·속성·가상 클래스, 타입·가상 요소의 구성으로 비교한다.
- `[id="li3"]`과 `#li3`은 같은 요소를 선택할 수 있지만 명시도가 다르다.
- `!important`는 선택자가 아니라 선언 중요도이며 남용하면 유지보수가 어려워진다.
- 같은 중요도와 명시도라면 뒤에 작성된 선언이 적용된다.
- 실무에서는 짧고 역할이 분명한 클래스 중심 선택자를 사용한다.
- 원본의 `human` 속성은 학습 실습에는 동작하지만 실제 데이터에는 `data-*`가 적절하다.
- 원본 내 코드의 자세한 주석은 복습에 유용하지만 일부 표현은 CSS와 DOM의 정확한 동작에 맞게 보완해야 한다.
