---
title: HTML 전역 속성
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# HTML 전역 속성

## 개요

전역 속성(Global Attributes)은 **특정 태그에만 사용하는 속성이 아니라 대부분의 HTML 요소에서 공통적으로 사용할 수 있는 속성**이다.

예를 들어 `class`, `id`, `title`은 `<div>`, `<p>`, `<img>`, `<section>`, `<button>` 등 거의 모든 HTML 요소에 사용할 수 있다.

CSS는 주로 `class`와 `id`를 이용하여 요소를 선택하고, JavaScript는 전역 속성을 이용하여 요소를 찾거나 제어한다.

따라서 전역 속성은 HTML, CSS, JavaScript를 연결하는 가장 중요한 개념 중 하나이다.

---

# 핵심 개념

대표적인 전역 속성은 다음과 같다.

| 속성 | 역할 |
|------|------|
| id | 문서 내부에서 요소를 고유하게 식별 |
| class | 여러 요소를 하나의 그룹으로 묶음 |
| style | 인라인 CSS 작성 |
| title | 추가 설명 제공 |
| lang | 언어 지정 |
| hidden | 요소 숨김 |
| tabindex | 키보드 포커스 순서 지정 |
| data-* | 사용자 정의 데이터 저장 |
| contenteditable | 요소 수정 가능 여부 |
| draggable | 드래그 가능 여부 |
| spellcheck | 맞춤법 검사 |
| translate | 자동 번역 여부 |
| dir | 글자 방향 지정 |

---

# id

`id`는 문서 안에서 **하나의 요소만 가질 수 있는 고유한 식별자**이다.

```html
<h1 id="main-title">
    Developer Academy
</h1>
```

CSS에서는 다음과 같이 선택한다.

```css
#main-title {
    color: royalblue;
}
```

JavaScript에서는 다음과 같이 사용할 수 있다.

```javascript
const title = document.getElementById('main-title');
```

---

## id 사용 규칙

좋은 예

```html
<section id="course-list">
```

좋지 않은 예

```html
<section id="1">
```

```html
<section id="abc def">
```

권장 사항

- 의미 있는 이름 사용
- 공백 사용하지 않기
- 문서 안에서 중복 금지

---

# class

`class`는 여러 요소를 하나의 그룹으로 묶는다.

```html
<p class="text">
```

```html
<button class="button">
```

같은 클래스를 여러 요소에서 사용할 수 있다.

```html
<button class="btn">
저장
</button>

<button class="btn">
삭제
</button>
```

CSS

```css
.btn {
    padding:12px;
}
```

---

## 여러 클래스

여러 클래스를 공백으로 구분하여 작성할 수 있다.

```html
<button class="btn primary large">
```

JavaScript

```javascript
button.classList.add('active');
button.classList.remove('active');
button.classList.toggle('active');
button.classList.contains('active');
```

---

# id와 class 차이

| 구분 | id | class |
|------|----|--------|
| 개수 | 하나 | 여러 개 |
| 중복 | 불가능 | 가능 |
| CSS | # | . |
| JavaScript | getElementById | querySelectorAll |

---

# style

인라인 CSS를 작성한다.

```html
<p style="color:red;">
```

하지만 실무에서는 CSS 파일을 사용한다.

좋지 않은 예

```html
<p style="font-size:18px;color:red;">
```

권장

```css
.notice {

}
```

---

# title

추가 설명을 제공한다.

```html
<button title="회원가입">
```

마우스를 올리면 브라우저에서 툴팁을 표시할 수 있다.

주의할 점은 `title`이 접근 가능한 이름을 대신하지 않는다는 것이다. 중요한 정보는 화면에 보이도록 제공하는 것이 좋다.

---

# lang

문서나 요소의 언어를 지정한다.

```html
<html lang="ko">
```

영어 문장

```html
<p lang="en">
Hello World
</p>
```

화면 낭독기와 번역 기능에 도움이 된다.

---

# hidden

요소를 화면에서 숨긴다.

```html
<p hidden>

숨겨진 내용

</p>
```

브라우저는 일반적으로 `display: none`과 비슷하게 처리한다.

CSS에서 다시 표시할 수도 있다.

---

# tabindex

키보드 포커스 순서를 지정한다.

```html
<input tabindex="1">
```

```html
<button tabindex="2">
```

대표적인 값

| 값 | 의미 |
|------|------|
| 0 | 기본 순서 포함 |
| -1 | Tab 이동 제외 |
| 1 이상 | 직접 순서 지정(권장하지 않음) |

실무에서는 **0**과 **-1**만 사용하는 경우가 대부분이다.

---

# data-*

사용자 정의 데이터를 저장한다.

```html
<button
data-id="100"
data-name="html"
>
```

JavaScript

```javascript
button.dataset.id;
button.dataset.name;
```

대표적인 사용

- 상품 번호
- 회원 번호
- 게시글 번호
- 상태값

---

# contenteditable

사용자가 내용을 수정할 수 있다.

```html
<p contenteditable="true">

수정 가능

</p>
```

간단한 메모 기능 등에 사용할 수 있다.

---

# draggable

드래그 가능 여부를 지정한다.

```html
<img
draggable="true"
>
```

JavaScript Drag & Drop API와 함께 사용한다.

---

# spellcheck

맞춤법 검사

```html
<textarea spellcheck="true">
```

비밀번호처럼 맞춤법 검사가 필요 없는 경우에는 비활성화할 수 있다.

```html
<input
type="password"
spellcheck="false"
>
```

---

# translate

자동 번역 여부를 지정한다.

```html
<p translate="no">

Developer Academy

</p>
```

브랜드명, 코드, 제품명 등에 사용할 수 있다.

---

# dir

글자 방향을 지정한다.

```html
<p dir="ltr">
```

```html
<p dir="rtl">
```

대표 값

- ltr
- rtl
- auto

---

# 접근성과 전역 속성

전역 속성은 접근성과도 밀접한 관련이 있다.

예를 들어

- `lang`
- `tabindex`
- `title`
- `hidden`

등은 화면 낭독기와 키보드 탐색에 영향을 준다.

잘못 사용하면 접근성이 떨어질 수 있으므로 의미를 이해하고 사용해야 한다.

---

# data-*와 JavaScript

실무에서 가장 많이 사용하는 전역 속성 중 하나이다.

```html
<button
class="delete-btn"
data-user-id="15"
>
삭제
</button>
```

```javascript
const button = document.querySelector('.delete-btn');

console.log(button.dataset.userId);
```

---

# 실무 활용

전역 속성은 다음과 같은 상황에서 자주 사용한다.

- CSS 스타일 적용
- JavaScript 이벤트 처리
- 사용자 데이터 저장
- 접근성 향상
- 다국어 지원
- 키보드 탐색
- 드래그 기능

---

# 실무 예제 프로젝트

```html
<header id="header">

    <h1 class="logo">
        Developer Academy
    </h1>

    <nav
        class="navigation"
        aria-label="주요 메뉴"
    >

        <button
            class="menu-btn"
            data-menu="mobile"
            title="메뉴 열기"
        >

            메뉴

        </button>

    </nav>

</header>

<main>

<section
id="courses"
class="section"
>

<h2>

교육 과정

</h2>

<article
class="card"
data-course-id="101"
>

<h3>

HTML

</h3>

<p
contenteditable="true"
>

메모를 작성하세요.

</p>

<button
class="apply-btn"
data-course="html"
>

신청

</button>

</article>

</section>

</main>
```

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|------|------|
| Global Attribute | 대부분의 요소에서 공통 사용 |
| id | 고유 식별자 |
| class | 그룹 지정 |
| style | 인라인 CSS |
| title | 추가 설명 |
| lang | 언어 지정 |
| hidden | 요소 숨김 |
| tabindex | 포커스 제어 |
| data-* | 사용자 데이터 |
| dataset | JavaScript 접근 |
| contenteditable | 수정 가능 |
| draggable | 드래그 |
| spellcheck | 맞춤법 검사 |
| translate | 자동 번역 |
| dir | 글 방향 |

---

# 자주 하는 실수

## 1.

같은 id를 여러 번 사용한다.

```html
<div id="menu"></div>

<div id="menu"></div>
```

→ id는 고유해야 한다.

---

## 2.

스타일을 모두 style 속성에 작성한다.

→ CSS 파일을 사용한다.

---

## 3.

class와 id를 같은 용도로 사용한다.

→ id는 고유, class는 그룹이다.

---

## 4.

tabindex를 1,2,3...으로 모두 지정한다.

→ 기본 Tab 순서를 깨뜨릴 수 있다.

---

## 5.

data-* 대신 의미 없는 class를 저장소처럼 사용한다.

```html
<div class="id15">
```

→

```html
<div data-id="15">
```

---

## 6.

hidden과 CSS 숨김을 같은 개념으로 생각한다.

사용 목적이 다를 수 있다.

---

## 7.

title만으로 설명을 제공한다.

중요한 정보는 화면에서도 확인할 수 있어야 한다.

---

## 8.

contenteditable을 저장 기능 없이 사용한다.

사용자가 수정한 내용이 자동 저장되는 것은 아니다.

---

## 9.

translate를 브랜드명에도 허용한다.

브랜드명은 `translate="no"`를 고려한다.

---

## 10.

lang을 지정하지 않는다.

```html
<html lang="ko">
```

는 거의 항상 작성하는 것이 좋다.

---

# 면접 포인트

### Q1.

전역 속성이란?

→ 대부분의 HTML 요소에서 공통으로 사용할 수 있는 속성이다.

---

### Q2.

id와 class의 차이는?

→ id는 고유 식별자, class는 그룹이다.

---

### Q3.

data-*는 언제 사용하나요?

→ JavaScript에서 사용할 사용자 정의 데이터를 저장할 때 사용한다.

---

### Q4.

tabindex는 왜 사용하나요?

→ 키보드 포커스를 제어하기 위해 사용한다.

---

### Q5.

lang은 왜 중요하나요?

→ 화면 낭독기, 번역 기능, 검색 엔진이 문서의 언어를 이해하는 데 도움이 된다.

---

### Q6.

hidden과 display:none의 차이는?

→ `hidden`은 HTML 의미를 가진 전역 속성이고, `display: none`은 CSS 표현 방식이다.

---

### Q7.

title 속성은 접근성을 보장하나요?

→ 아니다. `title`은 보조 정보이며, 레이블이나 화면에 보이는 설명을 대신할 수 없다.

---

### Q8.

contenteditable은 언제 사용하나요?

→ 간단한 편집 기능이 필요한 경우 사용할 수 있으며, 저장과 검증은 별도로 구현해야 한다.

---

# 핵심 정리

- 전역 속성은 대부분의 HTML 요소에서 사용할 수 있다.
- `id`는 고유 식별자, `class`는 여러 요소를 묶는 그룹이다.
- `style`보다 외부 CSS 파일을 사용하는 것이 유지보수에 유리하다.
- `lang`은 문서의 언어를 지정하며 접근성과 번역에 도움이 된다.
- `hidden`은 요소를 의미적으로 숨기는 전역 속성이다.
- `tabindex`는 키보드 포커스를 제어하며 `0`과 `-1`을 주로 사용한다.
- `data-*`는 JavaScript와 데이터를 연결하는 실무 핵심 속성이다.
- `contenteditable`, `draggable`은 브라우저의 기본 기능을 활성화할 수 있다.
- `title`은 보조 설명일 뿐 중요한 정보를 대신해서는 안 된다.
- 전역 속성은 HTML, CSS, JavaScript를 연결하는 중요한 역할을 한다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
| v1.0 | 2026-07-22 | 주요 전역 속성 정리 |
| v1.0 | 2026-07-22 | id와 class 비교 추가 |
| v1.0 | 2026-07-22 | data-*와 dataset 설명 추가 |
| v1.0 | 2026-07-22 | 접근성 관련 전역 속성 정리 |
| v1.0 | 2026-07-22 | 실무 예제 프로젝트 추가 |
| v1.0 | 2026-07-22 | 자주 하는 실수와 면접 포인트 추가 |