---
title: CSS 소개와 문법
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS 소개와 문법

## 개요

CSS(Cascading Style Sheets)는 HTML 문서의 **모양(Style)** 을 정의하는 스타일 시트 언어이다.

HTML이 웹 페이지의 **구조(Structure)** 를 담당한다면 CSS는 **디자인(Presentation)** 을 담당한다.

예를 들어 HTML에서는 제목과 문단을 작성하고, CSS에서는 글자 크기, 색상, 여백, 배치, 애니메이션 등을 지정한다.

```text
HTML
↓

웹 페이지의 구조

↓

CSS

↓

웹 페이지의 디자인

↓

JavaScript

↓

웹 페이지의 동작
```

현대 웹 개발에서는 HTML, CSS, JavaScript를 함께 사용하여 하나의 완성된 웹 페이지를 만든다.

---

# 핵심 개념

CSS의 역할은 다음과 같다.

- 글자 색상 변경
- 글꼴 변경
- 배경 설정
- 여백 조절
- 크기 지정
- 정렬
- 반응형 웹 구현
- 애니메이션 구현

---

# CSS란?

CSS는 HTML 요소를 선택하여 스타일을 적용한다.

```css
h1{

    color:red;

}
```

위 코드는 모든 `<h1>` 요소를 빨간색으로 표시한다.

---

# CSS의 구성

CSS는 다음과 같이 작성한다.

```css
선택자{

    속성:값;

}
```

예제

```css
h1{

    color:blue;

}
```

| 구성 | 설명 |
|------|------|
| 선택자 | 스타일을 적용할 대상 |
| 속성 | 변경할 스타일 |
| 값 | 속성에 적용할 내용 |

---

# CSS 문법

```css
p{

    color:red;

    font-size:20px;

}
```

여러 속성은 세미콜론(`;`)으로 구분한다.

---

# 선택자

가장 기본적인 선택자이다.

```css
h1{

}
```

```css
p{

}
```

```css
img{

}
```

CSS는 선택자를 통해 HTML 요소를 찾는다.

---

# 선언(Declaration)

다음 한 줄을 선언이라고 한다.

```css
color:red;
```

선언은

- 속성(Property)
- 값(Value)

으로 구성된다.

---

# 규칙(Rule Set)

```css
h1{

    color:red;

}
```

전체를 하나의 규칙(Rule Set)이라고 한다.

---

# CSS 주석

```css
/*

주석입니다.

*/
```

한 줄도

```css
/* 색상 변경 */
```

가능하다.

---

# CSS 작성 방법

CSS는 세 가지 방법으로 작성할 수 있다.

| 방법 | 사용 여부 |
|------|-----------|
| Inline CSS | 가능하지만 거의 사용하지 않음 |
| Internal CSS | 학습 및 간단한 예제 |
| External CSS | 실무에서 가장 많이 사용 |

---

# Inline CSS

HTML 요소에 직접 작성한다.

```html
<h1 style="color:red;">

HTML

</h1>
```

장점

- 빠른 테스트

단점

- 유지보수 어려움
- 재사용 불가능
- 실무에서는 거의 사용하지 않음

---

# Internal CSS

```html
<head>

<style>

h1{

color:red;

}

</style>

</head>
```

장점

- 작은 프로젝트

단점

- CSS 재사용 어려움

---

# External CSS

가장 많이 사용하는 방식이다.

```html
<head>

<link
rel="stylesheet"
href="./style.css"
>

</head>
```

style.css

```css
h1{

color:red;

}
```

장점

- 유지보수
- 재사용
- 캐싱
- 협업

실무에서는 거의 모두 이 방식을 사용한다.

---

# CSS 파일 연결

```html
<link
rel="stylesheet"
href="./css/style.css"
>
```

경로는 HTML 기준으로 작성한다.

---

# 브라우저 동작 과정

```text
HTML 다운로드

↓

CSS 다운로드

↓

CSS 파싱

↓

DOM + CSSOM 생성

↓

Render Tree 생성

↓

Layout

↓

Paint

↓

화면 출력
```

브라우저는 HTML만 읽는 것이 아니라 CSS도 함께 해석하여 화면을 만든다.

---

# CSS 적용 순서

브라우저는 여러 CSS를 읽는다.

예

- 브라우저 기본 스타일
- 사용자 스타일
- 개발자가 작성한 스타일

이후 우선순위(Cascade)에 따라 최종 스타일이 결정된다.

자세한 내용은 이후 **CSS 우선순위와 상속** 문서에서 학습한다.

---

# CSS와 HTML 관계

```text
HTML

↓

요소 생성

↓

CSS

↓

스타일 적용

↓

브라우저 출력
```

HTML이 없으면 CSS를 적용할 대상이 없다.

---

# CSS의 장점

- 디자인과 구조 분리
- 유지보수 향상
- 코드 재사용
- 협업 효율 증가
- 반응형 웹 구현 가능
- 애니메이션 지원

---

# CSS 사용 예

HTML

```html
<h1>

Developer Academy

</h1>
```

CSS

```css
h1{

color:royalblue;

font-size:48px;

}
```

---

# 실무 프로젝트 예제

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
href="./css/style.css"
>

<title>

Developer Academy

</title>

</head>

<body>

<header>

<h1>

Developer Academy

</h1>

<p>

실무 중심 웹 개발 교육

</p>

</header>

</body>

</html>
```

style.css

```css
body{

    font-family:Arial,sans-serif;

    margin:0;

}

header{

    background:#1f2937;

    color:white;

    padding:60px;

}

h1{

    font-size:48px;

}

p{

    font-size:20px;

}
```

---

# 예제 구조 분석

```text
index.html

↓

<link>

↓

style.css

↓

브라우저가 CSS 적용

↓

화면 출력
```

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|------|------|
| CSS | 스타일 시트 |
| Selector | 선택자 |
| Property | 속성 |
| Value | 값 |
| Declaration | 선언 |
| Rule Set | 규칙 |
| Inline CSS | 인라인 작성 |
| Internal CSS | style 태그 |
| External CSS | 외부 CSS |
| link | CSS 연결 |
| CSSOM | CSS 객체 모델 |
| Render Tree | 렌더 트리 |
| Layout | 레이아웃 계산 |
| Paint | 화면 그리기 |

---

# 자주 하는 실수

## 1.

세미콜론을 생략한다.

```css
color:red
font-size:20px;
```

→ 속성은 세미콜론으로 구분한다.

---

## 2.

콜론 대신 등호를 사용한다.

```css
color=red;
```

↓

```css
color:red;
```

---

## 3.

CSS 파일을 연결하지 않는다.

```html
<link rel="stylesheet" href="./style.css">
```

를 확인한다.

---

## 4.

HTML 기준이 아닌 CSS 기준으로 경로를 작성한다.

`href`는 **HTML 파일 기준**으로 작성한다.

---

## 5.

Inline CSS를 남용한다.

유지보수가 어려워지므로 External CSS를 사용한다.

---

## 6.

CSS와 HTML 역할을 혼동한다.

HTML은 구조, CSS는 디자인이다.

---

## 7.

속성 이름을 잘못 작성한다.

```css
font-colour:red;
```

↓

```css
color:red;
```

---

## 8.

속성과 값을 붙여 쓴다.

```css
colorred;
```

↓

```css
color:red;
```

---

## 9.

CSS 파일 확장자를 잘못 작성한다.

```text
style.cs
```

↓

```text
style.css
```

---

## 10.

브라우저 캐시 때문에 수정 사항이 보이지 않는다고 생각한다.

강력 새로고침(Ctrl + F5 또는 Shift + 새로고침)을 통해 캐시 문제를 확인한다.

---

# 면접 포인트

### Q1.

CSS란 무엇인가요?

→ HTML 문서의 스타일을 정의하는 스타일 시트 언어이다.

---

### Q2.

HTML과 CSS의 역할 차이는?

- HTML: 구조
- CSS: 디자인

---

### Q3.

CSS는 어떻게 HTML과 연결하나요?

```html
<link
rel="stylesheet"
href="./style.css"
>
```

---

### Q4.

실무에서 가장 많이 사용하는 CSS 작성 방식은?

→ External CSS

---

### Q5.

CSS는 어떤 구조로 작성하나요?

```css
선택자{

속성:값;

}
```

---

### Q6.

CSSOM은 무엇인가요?

→ 브라우저가 CSS를 파싱하여 만든 객체 모델이다.

---

### Q7.

Render Tree란 무엇인가요?

→ DOM과 CSSOM을 결합하여 화면에 표시할 요소만 모아 만든 구조이다.

---

### Q8.

왜 HTML과 CSS를 분리하나요?

→ 유지보수, 재사용성, 협업 효율을 높이기 위해서이다.

---

# 핵심 정리

- CSS는 HTML 요소의 스타일을 정의하는 언어이다.
- HTML은 구조, CSS는 디자인을 담당한다.
- CSS는 **선택자 + 선언 블록**으로 구성된다.
- 선언은 **속성(Property)** 과 **값(Value)** 으로 이루어진다.
- CSS 작성 방식에는 Inline, Internal, External이 있으며, 실무에서는 External CSS를 주로 사용한다.
- HTML에서는 `<link>` 태그를 사용해 CSS 파일을 연결한다.
- 브라우저는 HTML과 CSS를 각각 파싱하여 DOM과 CSSOM을 만들고 이를 결합해 Render Tree를 생성한 뒤 화면을 그린다.
- 구조와 디자인을 분리하면 유지보수와 협업이 쉬워진다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
| v1.0 | 2026-07-22 | CSS 개념 및 역할 정리 |
| v1.0 | 2026-07-22 | CSS 문법과 구성 요소 설명 추가 |
| v1.0 | 2026-07-22 | Inline, Internal, External CSS 비교 |
| v1.0 | 2026-07-22 | 브라우저 렌더링 과정(CSSOM, Render Tree) 추가 |
| v1.0 | 2026-07-22 | 실무 프로젝트 예제 추가 |
| v1.0 | 2026-07-22 | 자주 하는 실수와 면접 포인트 추가 |