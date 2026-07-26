---
title: JavaScript 소개와 실행환경
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript 소개와 실행환경

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript 소개와 실행환경 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | HTML, CSS |
| 핵심 주제 | JavaScript 개요, 실행 환경, 브라우저와 Node.js |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

JavaScript(JS)는 웹 브라우저에서 동작하는 프로그래밍 언어로 시작하여, 현재는 서버, 모바일, 데스크톱 애플리케이션까지 개발할 수 있는 범용 언어로 발전하였다.

HTML이 웹 페이지의 **구조**를 만들고, CSS가 **디자인**을 담당한다면, JavaScript는 **동작과 상호작용**을 담당한다.

예를 들어 다음과 같은 기능은 대부분 JavaScript로 구현된다.

- 버튼 클릭 이벤트
- 메뉴 열기/닫기
- 슬라이드 배너
- 로그인 검증
- 폼 유효성 검사
- AJAX 데이터 요청
- SPA(Single Page Application)

---

# JavaScript의 역사

1995년 브라우저에 동적인 기능을 추가하기 위해 Brendan Eich가 약 10일 만에 JavaScript의 초기 버전을 개발하였다.

이후 ECMAScript(ES)라는 표준이 제정되었고, JavaScript는 이 표준을 기반으로 발전하고 있다.

주요 버전

| 버전 | 주요 내용 |
|------|-----------|
| ES3 | 초기 표준 |
| ES5 | `strict mode`, JSON 등 |
| ES6 (ES2015) | `let`, `const`, 화살표 함수, 클래스, 모듈 등 |
| ES2016~현재 | 매년 새로운 기능 추가 |

현재 실무에서는 ES6 이상의 문법을 기본으로 사용한다.

---

# JavaScript의 역할

웹 페이지는 일반적으로 다음과 같이 역할을 분담한다.

```text
HTML
↓
구조(Structure)

CSS
↓
디자인(Presentation)

JavaScript
↓
동작(Behavior)
```

예를 들어 회원가입 화면에서는

- HTML → 입력창과 버튼 생성
- CSS → 화면 스타일 적용
- JavaScript → 입력값 검사 및 서버 요청

을 담당한다.

---

# JavaScript의 특징

## 인터프리터 언어

JavaScript는 별도의 컴파일 과정 없이 실행되는 인터프리터 언어이다.

브라우저의 JavaScript 엔진이 코드를 한 줄씩 해석하고 실행한다.

대표적인 엔진

- V8 (Chrome, Edge, Node.js)
- SpiderMonkey (Firefox)
- JavaScriptCore (Safari)

---

## 동적 타입 언어

변수의 자료형을 미리 선언하지 않아도 된다.

```javascript
let value = 10;

value = "Hello";

value = true;
```

동일한 변수에 숫자, 문자열, 불리언을 모두 저장할 수 있다.

---

## 객체 기반 언어

JavaScript는 객체(Object)를 중심으로 동작한다.

배열, 함수도 모두 객체의 특성을 가진다.

---

## 이벤트 기반 프로그래밍

사용자의 행동에 반응하여 코드를 실행할 수 있다.

예를 들어

- 클릭
- 키보드 입력
- 마우스 이동
- 스크롤

등의 이벤트를 처리할 수 있다.

---

# JavaScript 실행 환경

JavaScript는 다양한 환경에서 실행할 수 있다.

```text
JavaScript

├── Browser

└── Node.js
```

각 환경은 목적과 제공하는 기능이 다르다.

---

## 브라우저 환경

웹 페이지를 제어하기 위해 사용된다.

대표적으로

- Chrome
- Edge
- Firefox
- Safari

에서 실행된다.

브라우저 환경에서는 DOM, BOM, Web API 등을 사용할 수 있다.

---

## Node.js 환경

Node.js는 브라우저 밖에서도 JavaScript를 실행할 수 있도록 만든 런타임이다.

이를 통해

- 웹 서버
- API 서버
- CLI 프로그램
- 빌드 도구

등을 JavaScript로 개발할 수 있다.

---

# 브라우저와 Node.js 비교

| 항목 | Browser | Node.js |
|------|----------|----------|
| 목적 | 웹 페이지 실행 | 서버 및 실행 환경 |
| DOM 사용 | 가능 | 불가능 |
| HTML 제어 | 가능 | 불가능 |
| 파일 시스템 | 제한적 | 가능 |
| 서버 개발 | 불가능 | 가능 |

---

# 브라우저에서 JavaScript 실행하기

가장 기본적인 방법은 `<script>` 태그를 사용하는 것이다.

```html
<script>
    console.log("Hello JavaScript");
</script>
```

브라우저는 HTML을 해석하다가 `<script>`를 만나면 JavaScript를 실행한다.

---

# 외부 JavaScript 파일 연결

실무에서는 JavaScript를 별도의 파일로 분리하여 관리한다.

```html
<script src="main.js"></script>
```

이 방식은 코드의 재사용성과 유지보수성을 높여준다.

---

---

# `<script>` 태그의 위치

JavaScript는 HTML을 해석하는 도중 실행된다.

따라서 `<script>` 태그의 위치에 따라 실행 결과가 달라질 수 있다.

---

## 1. `<head>`에서 실행

```html
<!DOCTYPE html>

<html>

<head>

    <script src="main.js"></script>

</head>

<body>

    <button>Click</button>

</body>

</html>
```

이 경우 HTML이 모두 만들어지기 전에 JavaScript가 먼저 실행된다.

따라서 아래와 같은 코드는 오류가 발생할 수 있다.

```javascript
const button = document.querySelector("button");

console.log(button);
```

브라우저는 아직 `<button>`을 만들지 않았기 때문이다.

---

## 2. `<body>` 마지막에서 실행

실무에서 오래전부터 가장 많이 사용하던 방식이다.

```html
<body>

    ...

    <script src="main.js"></script>

</body>
```

브라우저가 HTML을 모두 생성한 후 JavaScript를 실행한다.

따라서 DOM 요소를 바로 사용할 수 있다.

---

## 3. defer 사용

현재 가장 많이 사용하는 방법이다.

```html
<script src="main.js" defer></script>
```

특징

- HTML을 먼저 해석한다.
- HTML 해석이 끝난 뒤 JavaScript를 실행한다.
- 여러 개의 Script도 순서를 유지한다.

```text
HTML Parsing

↓

완료

↓

Script 실행
```

실무에서는 `defer` 사용을 권장한다.

---

## 4. async 사용

```html
<script src="main.js" async></script>
```

특징

- HTML을 읽는 동시에 Script 다운로드
- 다운로드가 끝나는 즉시 실행
- 실행 순서를 보장하지 않는다.

```text
HTML

↓↓↓

Script 실행
```

여러 개의 JavaScript 파일이 서로 의존한다면 적합하지 않다.

---

# defer와 async 비교

| 항목 | defer | async |
|------|--------|--------|
| HTML Parsing | 계속 진행 | 계속 진행 |
| 실행 시점 | HTML 완료 후 | 다운로드 즉시 |
| 실행 순서 | 유지 | 보장되지 않음 |
| 실무 사용 | ⭐⭐⭐⭐⭐ | ⭐⭐ |

대부분의 프로젝트에서는 `defer`를 사용하는 것이 일반적이다.

---

# Console

JavaScript 개발에서 가장 많이 사용하는 도구이다.

```javascript
console.log("Hello");
```

브라우저 개발자 도구(Console)에 출력된다.

---

## console.log()

가장 많이 사용하는 출력 함수이다.

```javascript
let name = "Kim";

console.log(name);
```

출력

```text
Kim
```

---

## console.error()

오류 메시지를 출력한다.

```javascript
console.error("Error");
```

---

## console.warn()

경고 메시지를 출력한다.

```javascript
console.warn("Warning");
```

---

## console.table()

객체나 배열을 표 형태로 출력한다.

```javascript
const users = [

    {name:"Kim", age:20},

    {name:"Lee", age:30}

];

console.table(users);
```

개발 중 데이터를 확인할 때 매우 편리하다.

---

## console.dir()

객체의 속성을 자세히 확인할 수 있다.

```javascript
console.dir(document.body);
```

DOM 객체를 탐색할 때 자주 사용한다.

---

# 개발자 도구(Developer Tools)

대부분의 브라우저는 개발자 도구를 제공한다.

Chrome 기준

```
F12

또는

Ctrl + Shift + I
```

---

## 주요 기능

### Elements

HTML과 CSS를 확인할 수 있다.

---

### Console

JavaScript 출력과 오류를 확인한다.

---

### Network

서버 요청과 응답을 확인한다.

---

### Sources

JavaScript 파일을 디버깅한다.

---

### Application

Local Storage, Session Storage, Cookie 등을 확인할 수 있다.

---

### Performance

성능을 분석한다.

---

# JavaScript 주석

주석(Comment)은 실행되지 않는 설명이다.

---

## 한 줄 주석

```javascript
// 한 줄 주석
```

---

## 여러 줄 주석

```javascript
/*

여러 줄

주석

*/
```

주석은 코드의 의도를 설명하거나 임시로 코드를 비활성화할 때 사용한다.

---

# Strict Mode

JavaScript의 엄격한 실행 모드이다.

```javascript
"use strict";
```

파일의 가장 위에 작성한다.

---

## 사용하는 이유

JavaScript는 오래된 문법도 많이 지원한다.

Strict Mode는 이러한 문제를 줄여준다.

예를 들어

```javascript
x = 100;
```

일반 모드에서는 암묵적으로 전역 변수가 생성될 수 있다.

하지만 Strict Mode에서는 오류가 발생한다.

---

## 장점

- 실수를 빠르게 발견
- 안전한 코드 작성
- 최신 JavaScript 문법과 호환성 향상

실무에서는 ES Module을 사용하면 자동으로 Strict Mode가 적용된다.

---

# JavaScript 실행 과정

브라우저에서 JavaScript는 다음 순서로 실행된다.

```text
JavaScript 코드

↓

Parsing

↓

AST(Abstract Syntax Tree)

↓

컴파일

↓

실행
```

최신 JavaScript 엔진은 단순히 한 줄씩 읽는 것이 아니라 내부적으로 최적화 과정을 거친다.

---

# JavaScript 엔진

브라우저마다 JavaScript 엔진이 존재한다.

대표적인 엔진

| 브라우저 | 엔진 |
|----------|------|
| Chrome | V8 |
| Edge | V8 |
| Firefox | SpiderMonkey |
| Safari | JavaScriptCore |

이 엔진들이 JavaScript 코드를 해석하고 실행한다.

---

# 실행 컨텍스트(Execution Context)

JavaScript는 코드를 실행할 때 실행 컨텍스트라는 실행 환경을 생성한다.

실행 컨텍스트에는 다음과 같은 정보가 저장된다.

- 변수
- 함수
- this
- 스코프 정보

실행 컨텍스트는 JavaScript의 동작 원리를 이해하는 핵심 개념이며, 이후 함수와 스코프 문서에서 자세히 다룬다.

---

# Call Stack

JavaScript는 함수를 Call Stack이라는 자료구조에 저장하며 실행한다.

예를 들어

```javascript
function first(){

    second();

}

function second(){

    console.log("Hello");

}

first();
```

실행 순서

```text
Global

↓

first()

↓

second()

↓

console.log()

↓

종료
```

함수가 종료되면 Stack에서 제거된다.

---

---

# 브라우저 렌더링과 JavaScript

브라우저는 HTML, CSS, JavaScript를 읽어 화면을 구성한다.

전체 과정은 다음과 같다.

```text
HTML 다운로드

↓

HTML Parsing

↓

DOM 생성

↓

CSS Parsing

↓

CSSOM 생성

↓

Render Tree 생성

↓

Layout

↓

Paint

↓

화면 출력
```

JavaScript는 이 과정 중 DOM을 수정하거나 새로운 요소를 추가할 수 있다.

예를 들어

```javascript
const title = document.querySelector("h1");

title.textContent = "Hello JavaScript";
```

처럼 작성하면 이미 생성된 DOM을 수정하여 화면 내용을 변경할 수 있다.

---

# DOM이란?

DOM(Document Object Model)은 HTML 문서를 객체(Object) 형태로 표현한 구조이다.

예를 들어 다음 HTML이 있다.

```html
<body>

    <h1>Hello</h1>

    <button>Click</button>

</body>
```

브라우저는 이를 다음과 같이 객체 구조로 관리한다.

```text
Document

└── body

    ├── h1

    └── button
```

JavaScript는 이 구조를 통해 요소를 선택하고 수정한다.

---

# BOM이란?

BOM(Browser Object Model)은 브라우저 자체를 제어하기 위한 객체이다.

대표적인 객체

- window
- location
- history
- navigator
- screen

예제

```javascript
console.log(window.innerWidth);
```

현재 브라우저의 가로 크기를 출력한다.

---

# Web API

브라우저는 JavaScript에 다양한 기능을 제공한다.

대표적인 Web API

- DOM API
- Fetch API
- Timer API
- Storage API
- Geolocation API

예를 들어

```javascript
setTimeout(() => {

    console.log("3초 후 실행");

}, 3000);
```

`setTimeout()`은 브라우저가 제공하는 Timer API이다.

---

# 동기(Synchronous)

JavaScript는 기본적으로 **동기 방식**으로 동작한다.

코드는 위에서 아래 순서대로 실행된다.

```javascript
console.log("A");

console.log("B");

console.log("C");
```

결과

```text
A

B

C
```

앞의 코드가 끝나야 다음 코드가 실행된다.

---

# 비동기(Asynchronous)

시간이 오래 걸리는 작업은 비동기로 처리할 수 있다.

```javascript
console.log("Start");

setTimeout(() => {

    console.log("Timer");

}, 1000);

console.log("End");
```

실행 결과

```text
Start

End

Timer
```

Timer가 끝날 때까지 기다리지 않고 다음 코드를 먼저 실행한다.

---

# 이벤트 루프(Event Loop)

JavaScript는 한 번에 하나의 작업만 수행하는 **싱글 스레드(Single Thread)** 언어이다.

그럼에도 비동기 처리가 가능한 이유는 이벤트 루프(Event Loop) 덕분이다.

간단한 동작 순서는 다음과 같다.

```text
Call Stack

↓

Web API

↓

Callback Queue

↓

Event Loop

↓

Call Stack
```

동작 과정

1. 함수가 Call Stack에서 실행된다.
2. `setTimeout()`과 같은 작업은 Web API로 전달된다.
3. 작업이 완료되면 Callback Queue에 등록된다.
4. Call Stack이 비어 있으면 Event Loop가 Callback Queue의 작업을 Stack으로 이동시킨다.
5. 이동된 작업이 실행된다.

이벤트 루프는 이후 비동기 문서에서 더욱 자세히 다룬다.

---

# JavaScript 파일 구성

실무에서는 기능별로 파일을 분리하여 관리한다.

예시

```text
js/

├── main.js

├── user.js

├── product.js

├── api.js

└── utils.js
```

파일을 목적에 따라 분리하면 유지보수가 쉬워지고 협업에도 유리하다.

---

# 실무 예제 프로젝트

다음은 버튼 클릭 시 텍스트를 변경하는 간단한 예제이다.

## HTML

```html
<h1 id="title">Welcome</h1>

<button id="changeBtn">

    Change Text

</button>
```

---

## JavaScript

```javascript
const title = document.querySelector("#title");

const button = document.querySelector("#changeBtn");

button.addEventListener("click", function(){

    title.textContent = "Hello JavaScript";

});
```

학습한 내용

- `<script>`
- DOM 선택
- 이벤트 등록
- 함수 실행
- 화면 변경

---

# 이번 문서에서 새롭게 배운 내용

- JavaScript는 웹의 동작을 담당하는 프로그래밍 언어이다.
- 브라우저와 Node.js는 서로 다른 실행 환경이다.
- `defer`는 실무에서 가장 권장되는 Script 로딩 방식이다.
- Console과 개발자 도구를 활용하면 디버깅이 쉬워진다.
- Strict Mode는 안전한 코드 작성을 돕는다.
- 브라우저는 HTML을 DOM으로 변환하여 관리한다.
- Web API와 Event Loop를 통해 비동기 처리가 이루어진다.
- JavaScript는 DOM을 조작하여 화면을 동적으로 변경할 수 있다.

---

# 자주 하는 실수

- `<head>`에서 DOM이 생성되기 전에 요소를 선택한다.
- `defer`와 `async`의 차이를 이해하지 못한다.
- Console 출력만 믿고 실제 DOM 상태를 확인하지 않는다.
- 개발자 도구를 적극적으로 활용하지 않는다.
- Strict Mode 없이 코드를 작성하여 암묵적인 전역 변수를 만든다.
- 브라우저 API와 JavaScript 자체 기능을 혼동한다.
- Node.js에서도 DOM을 사용할 수 있다고 생각한다.

---

# 면접 포인트

### JavaScript의 역할은 무엇인가?

HTML과 CSS로 구성된 웹 페이지에 동적인 기능과 사용자 상호작용을 추가하는 역할을 한다.

---

### JavaScript는 어디에서 실행되는가?

대표적으로 브라우저와 Node.js 환경에서 실행된다.

---

### `defer`와 `async`의 차이는?

- `defer`는 HTML 파싱이 끝난 뒤 순서를 유지하며 실행된다.
- `async`는 다운로드가 끝나는 즉시 실행되므로 실행 순서가 보장되지 않는다.

---

### DOM이란?

HTML 문서를 객체 형태로 표현한 구조이며 JavaScript가 화면을 제어하는 대상이다.

---

### BOM이란?

브라우저 자체를 제어하기 위한 객체 모델이다.

---

### Web API란?

브라우저가 JavaScript에 제공하는 기능으로 DOM, Timer, Fetch, Storage API 등이 있다.

---

### JavaScript가 비동기 처리를 할 수 있는 이유는?

Web API와 Callback Queue, Event Loop가 함께 동작하기 때문이다.

---

### Node.js에서 DOM을 사용할 수 있는가?

기본적으로 사용할 수 없다. DOM은 브라우저 환경에서 제공되는 기능이다.

---

# 핵심 정리

- JavaScript는 웹의 동작을 담당하는 프로그래밍 언어이다.
- 브라우저와 Node.js는 서로 다른 실행 환경이다.
- `defer`는 현재 가장 권장되는 Script 로딩 방식이다.
- DOM은 HTML 문서를 객체로 표현한 구조이다.
- BOM은 브라우저를 제어하기 위한 객체 모델이다.
- Web API는 브라우저가 JavaScript에 제공하는 기능이다.
- JavaScript는 기본적으로 동기적으로 실행되지만, Event Loop를 통해 비동기 작업을 처리할 수 있다.
- 개발자 도구와 Console은 디버깅의 핵심 도구이다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |

