---
title: JavaScript DOM 기초
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript DOM 기초

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript DOM 기초 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | HTML 기본 구조, JavaScript 변수, 함수, 배열, 객체 |
| 핵심 주제 | DOM, Document, Element, Node, DOM Tree |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

JavaScript는 계산이나 데이터 처리뿐만 아니라 HTML 문서의 내용을 변경하고 사용자와 상호작용하는 데 사용한다.

예를 들어 JavaScript를 이용하면 다음과 같은 작업을 할 수 있다.

- HTML 요소 찾기
- 글자 내용 변경하기
- 이미지 변경하기
- CSS 스타일 변경하기
- 새로운 HTML 요소 추가하기
- 기존 HTML 요소 삭제하기
- 버튼 클릭 처리하기
- 입력한 값 가져오기
- 메뉴 열기와 닫기
- 이미지 슬라이드 만들기

JavaScript가 HTML 문서를 직접 문자열 형태로 제어하는 것은 아니다.

브라우저는 HTML 문서를 읽은 뒤 JavaScript가 사용할 수 있도록 객체 형태로 변환한다.

이 객체 구조를 **DOM(Document Object Model)** 이라고 한다.

---

# DOM이란?

DOM은 다음 단어의 약자이다.

```text
Document Object Model
```

각 단어는 다음과 같은 의미를 가진다.

| 단어 | 의미 |
|------|------|
| Document | HTML 문서 |
| Object | JavaScript에서 사용할 수 있는 객체 |
| Model | 문서를 표현한 구조 또는 방식 |

DOM은 HTML 문서를 JavaScript에서 사용할 수 있도록 객체 형태로 표현한 것이다.

다음과 같은 HTML 문서가 있다고 가정한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>DOM 기초</title>
</head>
<body>

    <h1>JavaScript</h1>
    <p>DOM을 학습합니다.</p>

</body>
</html>
```

브라우저는 이 HTML 코드를 읽고 다음과 같은 계층 구조로 해석한다.

```text
document
└── html
    ├── head
    │   ├── meta
    │   └── title
    └── body
        ├── h1
        └── p
```

JavaScript는 이렇게 만들어진 DOM 구조를 이용하여 HTML 요소에 접근한다.

---

# DOM이 필요한 이유

JavaScript는 HTML 파일에 작성된 태그 자체를 직접 제어하지 않는다.

브라우저가 HTML을 분석하여 DOM 객체를 만들고, JavaScript는 그 DOM 객체를 사용한다.

다음 HTML이 있다고 가정한다.

```html
<h1 id="title">안녕하세요.</h1>
```

JavaScript에서는 다음과 같이 해당 요소를 찾을 수 있다.

```javascript
const title = document.querySelector("#title");

console.log(title);
```

`title` 변수에는 HTML 문자열이 아니라 브라우저가 만든 요소 객체가 저장된다.

이 객체를 이용하면 내용을 변경할 수 있다.

```javascript
title.innerText = "JavaScript DOM";
```

화면의 결과는 다음과 같이 변경된다.

```text
JavaScript DOM
```

HTML 파일의 원본 코드가 직접 변경되는 것은 아니다.

현재 브라우저 화면에 표시된 DOM 구조가 변경되는 것이다.

---

# HTML과 DOM의 차이

HTML과 DOM은 서로 관련되어 있지만 같은 것은 아니다.

## HTML

HTML은 문서의 구조를 작성하는 코드이다.

```html
<h1>제목</h1>
<p>내용</p>
```

HTML 파일에 작성된 원본 문서라고 볼 수 있다.

---

## DOM

DOM은 브라우저가 HTML을 읽고 JavaScript에서 사용할 수 있도록 객체 구조로 변환한 결과이다.

```text
document
└── html
    └── body
        ├── h1
        └── p
```

JavaScript는 DOM을 통해 `h1`, `p`와 같은 요소를 찾고 변경한다.

---

## HTML과 DOM 비교

| 구분 | HTML | DOM |
|------|------|-----|
| 형태 | 마크업 코드 | 객체 구조 |
| 작성 주체 | 개발자 | 브라우저 |
| 주요 목적 | 문서 구조 작성 | JavaScript에서 문서 제어 |
| 예시 | `<h1>제목</h1>` | `document.querySelector("h1")` |
| 변경 결과 | 원본 파일 수정 | 현재 브라우저 화면 변경 |

---

# 브라우저가 HTML을 처리하는 과정

브라우저는 일반적으로 다음 순서로 HTML 문서를 처리한다.

```text
HTML 파일 읽기
↓
HTML 태그 분석
↓
DOM 객체 생성
↓
화면에 문서 표시
↓
JavaScript가 DOM에 접근
↓
내용 또는 스타일 변경
```

예를 들어 다음 코드가 있다고 가정한다.

```html
<p id="message">기존 내용</p>
```

```javascript
const message = document.querySelector("#message");

message.innerText = "변경된 내용";
```

JavaScript가 실행되면 브라우저가 만든 `p` 요소 객체의 내용이 변경된다.

---

# document 객체

`document`는 현재 브라우저에 표시된 HTML 문서 전체를 나타내는 객체이다.

```javascript
console.log(document);
```

개발자 도구의 콘솔에서 실행하면 현재 페이지의 HTML 문서 구조를 확인할 수 있다.

JavaScript에서 HTML 요소를 찾을 때 대부분 `document` 객체에서 시작한다.

```javascript
document.querySelector("h1");
```

위 코드는 다음과 같은 의미이다.

```text
현재 HTML 문서에서 h1 요소를 찾는다.
```

---

# document 객체의 역할

`document` 객체를 이용하면 다음과 같은 작업을 할 수 있다.

- HTML 요소 찾기
- 요소 내용 읽기
- 요소 내용 변경하기
- 속성 읽기와 변경하기
- CSS 클래스 추가와 삭제
- 새로운 요소 만들기
- 기존 요소 삭제하기
- 사용자 이벤트 연결하기

예제

```html
<h1 id="title">제목</h1>
```

```javascript
const title = document.querySelector("#title");

console.log(title);
```

`document`는 전체 문서를 의미하고, `querySelector()`는 문서 안에서 원하는 요소를 찾는 기능이다.

---

# console에서 document 확인하기

브라우저 개발자 도구의 콘솔에서 다음 코드를 실행할 수 있다.

```javascript
console.log(document);
```

또는 다음과 같이 직접 입력할 수도 있다.

```javascript
document
```

브라우저에 따라 현재 HTML 문서 구조가 출력된다.

다음 코드로 문서의 제목을 확인할 수도 있다.

```javascript
console.log(document.title);
```

HTML의 다음 부분과 연결된다.

```html
<title>DOM 기초</title>
```

문서 제목을 변경할 수도 있다.

```javascript
document.title = "JavaScript 학습";
```

브라우저 탭의 제목이 변경된다.

---

# DOM 객체도 JavaScript 객체이다

DOM을 구성하는 요소들은 JavaScript에서 객체로 다뤄진다.

다음 HTML이 있다고 가정한다.

```html
<h1 id="title">DOM 학습</h1>
```

JavaScript에서 요소를 선택한다.

```javascript
const title = document.querySelector("#title");

console.log(title);
console.log(typeof title);
```

`title`에는 선택된 HTML 요소를 나타내는 객체가 저장된다.

따라서 객체의 프로퍼티와 메서드를 사용하는 것처럼 DOM 요소도 점 표기법을 이용한다.

```javascript
title.innerText
title.id
title.style
title.classList
```

메서드도 사용할 수 있다.

```javascript
title.remove();
```

DOM 학습 전에 JavaScript 객체를 먼저 학습한 이유도 이와 관련되어 있다.

DOM 요소 역시 JavaScript에서 객체로 다루기 때문이다.

---

# Element란?

Element는 HTML 태그를 기반으로 만들어진 요소 객체이다.

다음 HTML이 있다고 가정한다.

```html
<h1>제목</h1>
<p>문단</p>
<button>버튼</button>
```

각각의 태그는 DOM에서 요소 객체가 된다.

```text
h1 Element
p Element
button Element
```

JavaScript에서 특정 요소를 선택하면 Element 객체를 사용할 수 있다.

```javascript
const button = document.querySelector("button");

console.log(button);
```

`button` 변수에는 `<button>` 요소를 나타내는 객체가 저장된다.

---

# Node란?

Node는 DOM을 구성하는 각각의 항목을 의미한다.

DOM에서는 HTML 요소뿐만 아니라 텍스트, 주석 등도 노드로 취급한다.

다음 HTML을 살펴보자.

```html
<p>안녕하세요.</p>
```

이 구조에는 다음과 같은 노드가 존재한다.

```text
p 요소 노드
└── "안녕하세요." 텍스트 노드
```

`p` 태그는 요소 노드이고, 태그 안의 `"안녕하세요."`는 텍스트 노드이다.

---

# Element와 Node의 관계

모든 Element는 Node에 포함되지만, 모든 Node가 Element인 것은 아니다.

```text
Node
├── Document Node
├── Element Node
├── Text Node
└── Comment Node
```

기초 단계에서는 다음과 같이 이해하면 충분하다.

- Node: DOM을 구성하는 모든 항목
- Element: HTML 태그로 만들어진 요소

---

# 주요 노드 종류

| 노드 종류 | 설명 | 예시 |
|----------|------|------|
| Document Node | HTML 문서 전체 | `document` |
| Element Node | HTML 태그 | `<div>`, `<p>` |
| Text Node | 태그 내부의 문자 | `"안녕하세요."` |
| Comment Node | HTML 주석 | `<!-- 주석 -->` |

---

# DOM Tree

DOM은 요소들이 부모와 자식 관계를 가지는 트리 구조로 구성된다.

이를 DOM Tree라고 한다.

다음 HTML을 살펴보자.

```html
<body>

    <main>
        <h1>제목</h1>
        <p>내용</p>
    </main>

</body>
```

DOM Tree로 표현하면 다음과 같다.

```text
body
└── main
    ├── h1
    │   └── "제목"
    └── p
        └── "내용"
```

`body` 안에 `main`이 있고, `main` 안에 `h1`과 `p`가 있다.

HTML 태그의 중첩 구조가 DOM의 부모와 자식 관계로 표현된다.

---

# 부모 요소와 자식 요소

다음 HTML을 살펴보자.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

관계는 다음과 같다.

```text
ul
├── li
├── li
└── li
```

- `ul`은 `li` 요소들의 부모 요소이다.
- 각각의 `li`는 `ul`의 자식 요소이다.
- `li` 요소들은 서로 형제 요소이다.

---

# 부모, 자식, 형제 관계

## 부모 요소

다른 요소를 내부에 포함하는 요소이다.

```html
<div>
    <p>문단</p>
</div>
```

`div`는 `p`의 부모 요소이다.

---

## 자식 요소

다른 요소 내부에 포함된 요소이다.

```html
<div>
    <p>문단</p>
</div>
```

`p`는 `div`의 자식 요소이다.

---

## 형제 요소

같은 부모 요소를 가지는 요소이다.

```html
<div>
    <h2>제목</h2>
    <p>문단</p>
</div>
```

`h2`와 `p`는 서로 형제 요소이다.

---

# DOM Tree를 이해해야 하는 이유

DOM Tree 구조를 이해하면 다음 작업을 수행할 때 도움이 된다.

- 원하는 HTML 요소 찾기
- 부모 요소 찾기
- 자식 요소 찾기
- 형제 요소 찾기
- 특정 위치에 요소 추가하기
- 특정 요소 삭제하기
- 이벤트가 전달되는 구조 이해하기

예를 들어 메뉴 안에 있는 특정 버튼을 찾거나, 클릭한 버튼의 부모 요소를 찾을 때 DOM 관계를 이용한다.

---

# JavaScript 파일 연결

DOM을 조작하려면 JavaScript 파일이 HTML 문서와 연결되어 있어야 한다.

```html
<script src="main.js"></script>
```

일반적으로 `body` 태그가 끝나기 직전에 작성할 수 있다.

```html
<body>

    <h1 id="title">DOM 학습</h1>

    <script src="main.js"></script>
</body>
```

이렇게 작성하면 HTML 요소가 먼저 생성된 후 JavaScript가 실행된다.

---

# script 위치와 DOM 접근

다음과 같이 `head` 안에 JavaScript 파일을 연결하면 JavaScript가 HTML 요소보다 먼저 실행될 수 있다.

```html
<head>
    <script src="main.js"></script>
</head>
```

JavaScript

```javascript
const title = document.querySelector("#title");

console.log(title);
```

JavaScript 실행 시점에 `#title` 요소가 아직 생성되지 않았다면 결과는 다음과 같을 수 있다.

```text
null
```

이 문제를 줄이기 위해 기초 단계에서는 `script` 태그를 `body`의 마지막에 작성하는 방법을 주로 사용한다.

```html
<body>

    <h1 id="title">DOM 학습</h1>

    <script src="main.js"></script>
</body>
```

---

# defer 속성

외부 JavaScript 파일을 `head`에서 연결하면서 HTML 분석이 끝난 뒤 실행하려면 `defer` 속성을 사용할 수 있다.

```html
<head>
    <script src="main.js" defer></script>
</head>
```

`defer`를 사용하면 브라우저가 HTML 문서를 분석하는 동안 JavaScript 파일을 불러오고, DOM 생성이 끝난 뒤 JavaScript를 실행한다.

기초 단계에서는 다음 두 방법을 사용할 수 있다.

## body 마지막에 연결

```html
<body>

    <h1 id="title">제목</h1>

    <script src="main.js"></script>
</body>
```

## head에서 defer 사용

```html
<head>
    <script src="main.js" defer></script>
</head>
```

---

# 기본 DOM 예제

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>DOM 기초</title>
    <script src="main.js" defer></script>
</head>
<body>

    <h1 id="title">기존 제목</h1>

</body>
</html>
```

## JavaScript

```javascript
const title = document.querySelector("#title");

console.log(title);

title.innerText = "변경된 제목";
```

실행 결과

```text
변경된 제목
```

JavaScript는 다음 순서로 동작한다.

```text
document 객체 사용
↓
#title 요소 찾기
↓
title 변수에 요소 객체 저장
↓
innerText 프로퍼티 변경
↓
브라우저 화면 변경
```

---

# DOM 조작의 기본 흐름

DOM을 조작할 때는 일반적으로 다음 순서를 사용한다.

```text
1. HTML 요소 선택
2. 선택 결과를 변수에 저장
3. 요소의 프로퍼티 또는 메서드 사용
4. 화면의 내용이나 상태 변경
```

예제

```javascript
const message = document.querySelector("#message");

message.innerText = "안녕하세요.";
```

각 코드의 의미는 다음과 같다.

```javascript
const message
```

선택한 요소를 저장할 변수를 선언한다.

```javascript
document.querySelector("#message")
```

현재 문서에서 `id`가 `message`인 요소를 찾는다.

```javascript
message.innerText = "안녕하세요.";
```

선택한 요소의 글자 내용을 변경한다.

---

---

# 개발자 도구에서 DOM 확인하기

브라우저 개발자 도구를 사용하면 현재 페이지의 DOM 구조를 직접 확인할 수 있다.

Chrome 기준으로 다음과 같이 개발자 도구를 열 수 있다.

```text
F12
```

또는

```text
Ctrl + Shift + I
```

개발자 도구의 `Elements` 탭에서는 현재 브라우저에 만들어진 DOM 구조를 확인할 수 있다.

HTML 파일에 작성된 코드와 비슷하게 보이지만, 실제로는 브라우저가 해석한 현재 DOM 상태이다.

JavaScript를 이용하여 요소를 추가하거나 내용을 변경하면 `Elements` 탭에도 변경된 결과가 나타난다.

---

# Elements 탭에서 요소 확인하기

다음 HTML이 있다고 가정한다.

```html
<h1 id="title">기존 제목</h1>
```

JavaScript에서 내용을 변경한다.

```javascript
const title = document.querySelector("#title");

title.innerText = "변경된 제목";
```

개발자 도구의 `Elements` 탭에서는 다음과 같이 확인할 수 있다.

```html
<h1 id="title">변경된 제목</h1>
```

HTML 원본 파일이 변경된 것은 아니지만, 현재 브라우저가 관리하는 DOM은 변경된 상태이다.

페이지를 새로고침하면 HTML 원본을 다시 읽기 때문에 JavaScript 실행 결과에 따라 DOM이 다시 만들어진다.

---

# Console 탭에서 요소 확인하기

선택한 DOM 요소는 `console.log()`를 이용하여 확인할 수 있다.

```html
<h1 id="title">DOM 학습</h1>
```

```javascript
const title = document.querySelector("#title");

console.log(title);
```

출력 결과는 브라우저에 따라 다음과 비슷하게 표시된다.

```html
<h1 id="title">DOM 학습</h1>
```

출력된 요소를 펼치거나 클릭하면 해당 요소의 프로퍼티와 구조를 확인할 수 있다.

---

# console.dir()

DOM 요소를 객체 형태로 자세히 확인할 때는 `console.dir()`를 사용할 수 있다.

```javascript
const title = document.querySelector("#title");

console.dir(title);
```

`console.log()`는 HTML 요소의 형태를 중심으로 보여주는 경우가 많고, `console.dir()`는 객체의 프로퍼티를 중심으로 확인할 때 유용하다.

```javascript
console.log(title);
console.dir(title);
```

두 출력 방식을 함께 비교하면 DOM 요소가 JavaScript 객체라는 점을 더 쉽게 확인할 수 있다.

---

# 요소 선택 결과 확인

DOM 요소를 선택하면 선택 결과를 변수에 저장하는 경우가 많다.

```javascript
const title = document.querySelector("#title");
```

선택 결과를 확인할 때는 다음과 같이 출력한다.

```javascript
console.log(title);
```

요소가 정상적으로 선택되었다면 해당 HTML 요소가 출력된다.

```html
<h1 id="title">제목</h1>
```

요소를 찾지 못했다면 `null`이 출력된다.

```text
null
```

---

# null이란?

`null`은 값이 없다는 것을 나타내는 값이다.

DOM 요소 선택에서 `null`이 반환되었다면 조건에 맞는 요소를 찾지 못했다는 의미이다.

다음 HTML이 있다고 가정한다.

```html
<h1 id="title">제목</h1>
```

JavaScript에서 존재하지 않는 요소를 선택한다.

```javascript
const message = document.querySelector("#message");

console.log(message);
```

결과

```text
null
```

현재 HTML 문서에 `id="message"`인 요소가 없기 때문에 `null`이 반환된다.

---

# null 상태에서 프로퍼티 사용하기

요소를 찾지 못한 상태에서 프로퍼티를 사용하면 오류가 발생한다.

```javascript
const message = document.querySelector("#message");

message.innerText = "안녕하세요.";
```

`message`에 `null`이 저장되어 있다면 다음과 비슷한 오류가 발생할 수 있다.

```text
Cannot set properties of null
```

또는 다음과 같은 오류가 발생할 수 있다.

```text
Cannot read properties of null
```

이는 `null`에는 `innerText`와 같은 프로퍼티가 존재하지 않기 때문이다.

---

# Cannot set properties of null

다음 코드를 살펴보자.

```javascript
const orderPrice = document.querySelector("#orderPrice");

orderPrice.innerText = "10000원";
```

HTML에 `id="orderPrice"`인 요소가 없다면 `orderPrice`에는 `null`이 저장된다.

따라서 다음 코드에서 오류가 발생한다.

```javascript
orderPrice.innerText = "10000원";
```

오류의 의미는 다음과 같다.

```text
null인 값의 innerText 프로퍼티에 값을 설정할 수 없다.
```

이 오류가 발생하면 먼저 선택 결과를 출력해야 한다.

```javascript
console.log(orderPrice);
```

결과가 `null`이라면 선택자와 HTML 구조를 확인한다.

---

# DOM 요소를 선택하지 못하는 주요 원인

## 1. 선택자 오타

HTML

```html
<h1 id="title">제목</h1>
```

잘못된 JavaScript

```javascript
const title = document.querySelector("#tittle");
```

`title`과 `tittle`의 철자가 다르기 때문에 요소를 찾지 못한다.

올바른 코드

```javascript
const title = document.querySelector("#title");
```

---

## 2. `#`과 `.` 사용 오류

HTML

```html
<p class="message">안녕하세요.</p>
```

잘못된 코드

```javascript
const message = document.querySelector("#message");
```

`message`는 `id`가 아니라 `class`이므로 `.`을 사용해야 한다.

```javascript
const message = document.querySelector(".message");
```

---

## 3. HTML에 요소가 존재하지 않음

JavaScript

```javascript
const button = document.querySelector("#button");
```

HTML 문서에 `id="button"`인 요소가 없다면 `null`이 반환된다.

---

## 4. JavaScript가 너무 일찍 실행됨

HTML 요소가 만들어지기 전에 JavaScript가 실행되면 요소를 찾지 못할 수 있다.

```html
<head>
    <script src="main.js"></script>
</head>
<body>
    <h1 id="title">제목</h1>
</body>
```

`main.js`가 먼저 실행되면 `#title` 요소가 아직 만들어지지 않았을 수 있다.

---

## 5. JavaScript 파일 연결 오류

HTML에서 JavaScript 파일 경로가 잘못되면 코드 자체가 실행되지 않는다.

```html
<script src="js/main.js"></script>
```

실제 파일 경로와 `src` 경로가 일치하는지 확인해야 한다.

---

# null 오류 확인 순서

DOM 관련 오류가 발생하면 다음 순서로 확인할 수 있다.

```text
1. 선택한 값을 console.log()로 출력한다.
2. 출력 결과가 null인지 확인한다.
3. HTML에 해당 요소가 존재하는지 확인한다.
4. id와 class 선택자가 맞는지 확인한다.
5. 선택자 철자를 확인한다.
6. script 실행 위치를 확인한다.
7. JavaScript 파일 연결 경로를 확인한다.
```

예제

```javascript
const orderChk = document.querySelector("#orderChk");
const orderPrice = document.querySelector("#orderPrice");

console.log(orderChk);
console.log(orderPrice);
```

두 값 중 어떤 것이 `null`인지 먼저 확인하면 오류 원인을 빠르게 찾을 수 있다.

---

# JavaScript 실행 시점

JavaScript가 언제 실행되는지는 DOM 요소 선택에 큰 영향을 준다.

브라우저는 HTML 문서를 위에서 아래로 읽는다.

다음 구조를 살펴보자.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <script src="main.js"></script>
</head>
<body>

    <h1 id="title">제목</h1>

</body>
</html>
```

브라우저는 `script` 태그를 만났을 때 JavaScript 파일을 실행할 수 있다.

이 시점에는 아직 `body` 내부의 `h1`을 읽지 않았기 때문에 다음 코드는 `null`을 반환할 수 있다.

```javascript
const title = document.querySelector("#title");

console.log(title);
```

---

# script를 body 마지막에 작성하기

기초 단계에서 가장 쉽게 사용할 수 있는 방법은 `script` 태그를 `body` 마지막에 작성하는 것이다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>DOM</title>
</head>
<body>

    <h1 id="title">제목</h1>

    <script src="main.js"></script>
</body>
</html>
```

이 구조에서는 `h1` 요소가 먼저 만들어진 뒤 JavaScript가 실행된다.

```javascript
const title = document.querySelector("#title");

console.log(title);
```

정상적으로 요소를 선택할 수 있다.

---

# defer를 사용하기

`script` 태그를 `head`에 작성하면서 DOM 생성 이후에 실행하려면 `defer` 속성을 사용한다.

```html
<head>
    <script src="main.js" defer></script>
</head>
```

전체 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>DOM</title>
    <script src="main.js" defer></script>
</head>
<body>

    <h1 id="title">제목</h1>

</body>
</html>
```

JavaScript

```javascript
const title = document.querySelector("#title");

console.log(title);
```

`defer`를 사용하면 HTML 문서 분석이 완료된 후 JavaScript가 실행된다.

---

# DOMContentLoaded 이벤트

HTML 문서의 DOM 생성이 완료된 뒤 코드를 실행하는 방법도 있다.

```javascript
document.addEventListener("DOMContentLoaded", function() {

    const title = document.querySelector("#title");

    console.log(title);

});
```

`DOMContentLoaded`는 HTML 문서의 DOM 구조가 모두 만들어졌을 때 발생하는 이벤트이다.

다만 현재 단계에서는 다음 두 방법을 우선 사용하는 것이 좋다.

```text
1. script를 body 마지막에 작성하기
2. head에서 defer 사용하기
```

`DOMContentLoaded`는 이벤트 문서에서 다시 자세히 다룬다.

---

# window 객체

`window`는 브라우저 창 전체를 나타내는 객체이다.

브라우저 환경에서 JavaScript를 실행하면 가장 바깥쪽에 `window` 객체가 존재한다.

```javascript
console.log(window);
```

`window` 객체에는 브라우저와 관련된 다양한 기능이 포함되어 있다.

예를 들면 다음과 같다.

```javascript
window.alert();
window.setTimeout();
window.location;
window.document;
```

---

# window와 document의 관계

`document` 객체는 `window` 객체의 프로퍼티이다.

```javascript
console.log(window.document);
```

다음 두 코드는 같은 문서를 가리킨다.

```javascript
document
```

```javascript
window.document
```

브라우저에서는 `window`를 생략할 수 있기 때문에 보통 다음과 같이 작성한다.

```javascript
document.querySelector("#title");
```

원래 구조를 표현하면 다음과 같다.

```javascript
window.document.querySelector("#title");
```

---

# window 생략

브라우저 환경에서는 `window` 객체의 프로퍼티와 메서드를 사용할 때 `window`를 생략할 수 있다.

다음 두 코드는 같은 의미이다.

```javascript
window.alert("안녕하세요.");
```

```javascript
alert("안녕하세요.");
```

다음 두 코드도 같은 의미이다.

```javascript
window.setTimeout(function() {
    console.log("실행");
}, 1000);
```

```javascript
setTimeout(function() {
    console.log("실행");
}, 1000);
```

`document`도 같은 원리로 사용할 수 있다.

---

# DOM과 BOM

브라우저에서 JavaScript로 제어할 수 있는 대상은 DOM뿐만이 아니다.

브라우저 자체의 기능을 제어하기 위한 객체 구조를 BOM이라고 한다.

```text
Browser Object Model
```

---

# DOM

DOM은 HTML 문서와 관련된 객체 구조이다.

```javascript
document.querySelector("#title");
document.title;
document.body;
```

DOM으로 수행할 수 있는 작업은 다음과 같다.

- HTML 요소 선택
- 텍스트 변경
- 속성 변경
- 스타일 변경
- 요소 생성
- 요소 삭제
- 이벤트 연결

---

# BOM

BOM은 브라우저 창과 관련된 객체 구조이다.

```javascript
window.alert("안녕하세요.");
window.location;
window.history;
window.navigator;
```

BOM으로 수행할 수 있는 작업은 다음과 같다.

- 현재 주소 확인
- 페이지 이동
- 이전 페이지와 다음 페이지 이동
- 브라우저 정보 확인
- 알림창 출력
- 일정 시간 후 코드 실행

---

# DOM과 BOM 비교

| 구분 | DOM | BOM |
|------|-----|-----|
| 전체 이름 | Document Object Model | Browser Object Model |
| 대상 | HTML 문서 | 브라우저 |
| 대표 객체 | `document` | `window` |
| 주요 기능 | 요소 선택과 변경 | 브라우저 기능 제어 |
| 예시 | `document.querySelector()` | `window.location` |

현재 문서에서는 DOM을 중심으로 학습한다.

BOM은 별도의 문서에서 자세히 정리한다.

---

# DOM을 활용하는 기본 사례

## 글자 변경

HTML

```html
<h1 id="title">기존 제목</h1>
```

JavaScript

```javascript
const title = document.querySelector("#title");

title.innerText = "새로운 제목";
```

---

## 문단 내용 변경

HTML

```html
<p id="message">기존 메시지</p>
```

JavaScript

```javascript
const message = document.querySelector("#message");

message.innerText = "변경된 메시지";
```

---

## 버튼 비활성화

HTML

```html
<button id="submitButton">전송</button>
```

JavaScript

```javascript
const submitButton = document.querySelector("#submitButton");

submitButton.disabled = true;
```

---

## 입력창 값 확인

HTML

```html
<input type="text" id="userName">
```

JavaScript

```javascript
const userName = document.querySelector("#userName");

console.log(userName.value);
```

입력 요소의 현재 값은 `value` 프로퍼티로 확인한다.

---

## 이미지 경로 변경

HTML

```html
<img id="profileImage" src="image1.jpg" alt="프로필 이미지">
```

JavaScript

```javascript
const profileImage = document.querySelector("#profileImage");

profileImage.src = "image2.jpg";
```

---

## 스타일 변경

HTML

```html
<p id="message">안녕하세요.</p>
```

JavaScript

```javascript
const message = document.querySelector("#message");

message.style.fontSize = "30px";
```

DOM 요소의 `style` 프로퍼티를 이용하면 인라인 스타일을 변경할 수 있다.

---

# DOM 조작 코드 읽기

다음 코드를 살펴보자.

```javascript
const title = document.querySelector("#title");

title.innerText = "JavaScript";
```

코드는 다음 순서로 해석할 수 있다.

```text
document
현재 HTML 문서에서

querySelector("#title")
id가 title인 요소를 찾아서

const title
title 변수에 저장하고

title.innerText
해당 요소의 글자 내용을

"JavaScript"
JavaScript라는 값으로 변경한다.
```

DOM 코드를 읽을 때는 다음 세 부분으로 나누면 이해하기 쉽다.

```text
1. 어떤 요소를 선택했는가?
2. 어떤 프로퍼티나 메서드를 사용했는가?
3. 어떤 값으로 변경하거나 어떤 동작을 실행했는가?
```

---

# DOM 요소 선택 전 확인사항

DOM 요소를 선택하기 전에 다음 내용을 확인하면 오류를 줄일 수 있다.

- HTML에 대상 요소가 존재하는가?
- `id`와 `class` 이름이 정확한가?
- 선택자에 `#` 또는 `.`을 올바르게 사용했는가?
- JavaScript 파일이 정상적으로 연결되었는가?
- JavaScript가 DOM 생성 후 실행되는가?
- 같은 `id`를 여러 요소에 사용하지 않았는가?
- 선택 결과를 `console.log()`로 확인했는가?

---

# 기본 디버깅 예제

HTML

```html
<h2 id="orderTitle">주문 정보</h2>
<p id="orderPrice"></p>
```

JavaScript

```javascript
const orderTitle = document.querySelector("#orderTitle");
const orderPrice = document.querySelector("#orderPrice");

console.log(orderTitle);
console.log(orderPrice);

orderTitle.innerText = "피자 주문";
orderPrice.innerText = "결제 금액: 20000원";
```

요소 선택 코드 뒤에 `console.log()`를 작성하면 정상적으로 요소가 선택되었는지 먼저 확인할 수 있다.

---

# 선택 결과 검사하기

요소가 존재할 때만 코드를 실행하도록 조건문을 사용할 수 있다.

```javascript
const message = document.querySelector("#message");

if (message !== null) {

    message.innerText = "안녕하세요.";

}
```

간단하게 다음처럼 작성할 수도 있다.

```javascript
if (message) {

    message.innerText = "안녕하세요.";

}
```

DOM 요소가 정상적으로 선택되면 객체이므로 조건식에서 `true`로 평가된다.

`null`은 조건식에서 `false`로 평가된다.

다만 요소가 반드시 존재해야 하는 상황에서는 조건문으로 오류를 숨기기보다 선택자가 틀린 원인을 먼저 찾는 것이 중요하다.

---

---

# DOM 요소 선택의 기초

DOM을 조작하려면 먼저 HTML 요소를 선택해야 한다.

다음 HTML이 있다고 가정한다.

```html
<h1 id="title">제목</h1>
<p class="message">안녕하세요.</p>
```

JavaScript에서는 `document.querySelector()`를 사용하여 요소를 선택할 수 있다.

```javascript
const title = document.querySelector("#title");
const message = document.querySelector(".message");
```

선택된 요소는 각각 변수에 저장된다.

```javascript
console.log(title);
console.log(message);
```

---

# querySelector()

`querySelector()`는 CSS 선택자를 이용하여 조건에 맞는 첫 번째 요소 하나를 선택하는 메서드이다.

기본 문법

```javascript
document.querySelector("CSS 선택자");
```

예제

```javascript
const title = document.querySelector("#title");
```

위 코드는 현재 문서에서 `id`가 `title`인 요소를 찾는다.

---

# 태그 선택자 사용

HTML

```html
h1>제목</h1>
```

JavaScript

```javascript
const title = document.querySelector("h1");

console.log(title);
```

태그 이름을 선택자로 사용하면 해당 태그 중 첫 번째 요소가 선택된다.

---

# id 선택자 사용

HTML

```html
<h1 id="title">제목</h1>
```

JavaScript

```javascript
const title = document.querySelector("#title");
```

CSS에서 `id` 선택자를 작성할 때 사용하는 `#`을 그대로 사용한다.

---

# class 선택자 사용

HTML

```html
<p class="message">안녕하세요.</p>
```

JavaScript

```javascript
const message = document.querySelector(".message");
```

CSS에서 `class` 선택자를 작성할 때 사용하는 `.`을 그대로 사용한다.

---

# 복합 선택자 사용

`querySelector()`에서는 CSS에서 사용하는 복합 선택자도 사용할 수 있다.

HTML

```html
<section id="profile">

    <p class="name">홍길동</p>

</section>
```

JavaScript

```javascript
const name = document.querySelector("#profile .name");

console.log(name);
```

`#profile` 내부에 있는 `.name` 요소를 선택한다.

---

# 자식 선택자 사용

HTML

```html
<ul id="menu">
    <li>HTML</li>
    <li>CSS</li>
</ul>
```

JavaScript

```javascript
const menuItem = document.querySelector("#menu > li");

console.log(menuItem);
```

조건에 맞는 첫 번째 `li` 요소만 선택된다.

---

# 여러 요소 중 첫 번째 요소 선택

다음 HTML을 살펴보자.

```html
<p class="item">첫 번째</p>
<p class="item">두 번째</p>
<p class="item">세 번째</p>
```

JavaScript

```javascript
const item = document.querySelector(".item");

console.log(item);
```

`querySelector()`는 조건에 맞는 요소가 여러 개 있어도 첫 번째 요소만 반환한다.

결과

```html
<p class="item">첫 번째</p>
```

여러 요소를 모두 선택하는 방법은 이후 요소 선택 문서에서 학습한다.

---

# CSS 선택자와 DOM 선택자의 관계

`querySelector()`에 전달하는 문자열은 CSS 선택자 규칙을 따른다.

| 선택 대상 | CSS 선택자 | JavaScript |
|-----------|------------|------------|
| 태그 | `h1` | `document.querySelector("h1")` |
| id | `#title` | `document.querySelector("#title")` |
| class | `.message` | `document.querySelector(".message")` |
| 자손 요소 | `.box p` | `document.querySelector(".box p")` |
| 자식 요소 | `.box > p` | `document.querySelector(".box > p")` |

CSS 선택자를 잘 이해하면 DOM 요소를 선택할 때도 그대로 활용할 수 있다.

---

# 선택한 요소의 내용 읽기

요소를 선택한 뒤 `innerText`를 사용하면 화면에 표시되는 글자 내용을 읽을 수 있다.

HTML

```html
<h1 id="title">JavaScript DOM</h1>
```

JavaScript

```javascript
const title = document.querySelector("#title");

console.log(title.innerText);
```

결과

```text
JavaScript DOM
```

---

# innerText

`innerText`는 요소 안의 화면에 표시되는 글자 내용을 읽거나 변경할 때 사용한다.

## 내용 읽기

```javascript
const title = document.querySelector("#title");

console.log(title.innerText);
```

## 내용 변경

```javascript
title.innerText = "변경된 제목";
```

HTML 화면은 다음과 같이 변경된다.

```html
<h1 id="title">변경된 제목</h1>
```

---

# innerText에 HTML 태그 작성하기

`innerText`에 HTML 태그 형태의 문자열을 넣어도 실제 태그로 해석되지 않는다.

```javascript
const message = document.querySelector("#message");

message.innerText = "<strong>안녕하세요.</strong>";
```

화면에는 다음 문자열이 그대로 표시된다.

```text
<strong>안녕하세요.</strong>
```

HTML 태그를 실제 요소로 해석하려면 `innerHTML`을 사용해야 한다.

---

# textContent

`textContent`도 요소 안의 텍스트를 읽거나 변경할 때 사용한다.

```javascript
const title = document.querySelector("#title");

console.log(title.textContent);

title.textContent = "새로운 제목";
```

`innerText`와 비슷하지만 처리 방식에 차이가 있다.

---

# innerText와 textContent 차이

`innerText`는 일반적으로 화면에 실제로 표시되는 텍스트를 기준으로 동작한다.

`textContent`는 요소 내부의 텍스트 노드 전체를 기준으로 동작한다.

HTML

```html
<div id="box">
    안녕하세요.
    <span style="display: none;">숨겨진 내용</span>
</div>
```

JavaScript

```javascript
const box = document.querySelector("#box");

console.log(box.innerText);
console.log(box.textContent);
```

브라우저와 공백 처리 방식에 따라 차이가 있을 수 있지만, 일반적으로 다음처럼 이해할 수 있다.

```text
innerText
화면에 보이는 텍스트 중심

textContent
요소 안의 전체 텍스트 중심
```

기초 단계에서 화면의 글자를 단순히 변경할 때는 `innerText`를 자주 사용한다.

---

# innerHTML

`innerHTML`은 요소 안의 HTML 내용을 문자열 형태로 읽거나 변경할 때 사용한다.

HTML

```html
<div id="result"></div>
```

JavaScript

```javascript
const result = document.querySelector("#result");

result.innerHTML = "<strong>주문 완료</strong>";
```

화면에는 굵은 글자로 다음 내용이 표시된다.

```text
주문 완료
```

`<strong>` 태그가 실제 HTML 요소로 해석된다.

---

# innerText와 innerHTML 비교

HTML

```html
<div id="result"></div>
```

## innerText 사용

```javascript
result.innerText = "<strong>완료</strong>";
```

화면 결과

```text
<strong>완료</strong>
```

## innerHTML 사용

```javascript
result.innerHTML = "<strong>완료</strong>";
```

화면 결과

```text
완료
```

| 구분 | `innerText` | `innerHTML` |
|------|-------------|-------------|
| 문자열 처리 | 텍스트 | HTML |
| 태그 해석 | 하지 않음 | 해석함 |
| 주요 용도 | 글자 변경 | HTML 구조 삽입 |
| 주의점 | 비교적 단순함 | 외부 입력 사용 시 주의 |

---

# innerHTML 사용 시 주의사항

`innerHTML`은 문자열 안의 HTML 태그를 실제 요소로 변환한다.

```javascript
result.innerHTML = `
    <h2>결과</h2>
    <p>처리가 완료되었습니다.</p>
`;
```

정해진 HTML 구조를 출력할 때는 편리하지만, 사용자가 직접 입력한 값을 그대로 넣는 것은 주의해야 한다.

```javascript
const userInput = document.querySelector("#userInput");

result.innerHTML = userInput.value;
```

사용자 입력에는 예상하지 못한 HTML 코드가 포함될 수 있다.

단순한 글자를 출력할 때는 `innerText` 또는 `textContent`를 사용하는 것이 더 적절하다.

---

# DOM 기본 실습 1

## 제목 변경

HTML

```html
<h1 id="title">기존 제목</h1>
```

JavaScript

```javascript
const title = document.querySelector("#title");

title.innerText = "JavaScript DOM 기초";
```

---

# DOM 기본 실습 2

## 문단 내용 읽기

HTML

```html
<p id="message">DOM을 학습하고 있습니다.</p>
```

JavaScript

```javascript
const message = document.querySelector("#message");

console.log(message.innerText);
```

결과

```text
DOM을 학습하고 있습니다.
```

---

# DOM 기본 실습 3

## HTML 구조 추가

HTML

```html
<div id="profile"></div>
```

JavaScript

```javascript
const profile = document.querySelector("#profile");

profile.innerHTML = `
    <h2>회원 정보</h2>
    <p>이름: 홍길동</p>
    <p>나이: 20</p>
`;
```

---

# DOM 기본 실습 4

## 객체 데이터 출력

JavaScript 객체의 데이터를 DOM에 출력할 수 있다.

HTML

```html
<div id="userInfo"></div>
```

JavaScript

```javascript
const user = {
    name: "홍길동",
    age: 20,
    email: "user@example.com"
};

const userInfo = document.querySelector("#userInfo");

userInfo.innerHTML = `
    <h2>${user.name}</h2>
    <p>나이: ${user.age}</p>
    <p>이메일: ${user.email}</p>
`;
```

객체와 DOM을 함께 사용하면 데이터를 화면에 구조적으로 표시할 수 있다.

---

# DOM 기본 실습 5

## 배열 데이터 출력

HTML

```html
<ul id="languageList"></ul>
```

JavaScript

```javascript
const languages = [
    "HTML",
    "CSS",
    "JavaScript"
];

const languageList = document.querySelector("#languageList");

let html = "";

for (let i = 0; i < languages.length; i++) {

    html += `<li>${languages[i]}</li>`;

}

languageList.innerHTML = html;
```

실행 결과

```text
HTML
CSS
JavaScript
```

---

# 실무 예제 프로젝트

## 회원 카드 출력

객체 데이터를 DOM에 출력하는 간단한 회원 카드 예제이다.

### HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>회원 카드</title>
    <script src="main.js" defer></script>
</head>
<body>

    <section id="memberCard"></section>

</body>
</html>
```

### JavaScript

```javascript
const member = {
    name: "홍길동",
    age: 20,
    email: "hong@example.com",
    isMember: true
};

const memberCard = document.querySelector("#memberCard");

memberCard.innerHTML = `
    <h2>${member.name}</h2>
    <p>나이: ${member.age}</p>
    <p>이메일: ${member.email}</p>
    <p>회원 여부: ${member.isMember ? "회원" : "비회원"}</p>
`;
```

---

## 코드 흐름

```text
1. 회원 정보를 객체로 생성한다.
2. memberCard 요소를 선택한다.
3. 객체의 프로퍼티 값을 템플릿 리터럴에 넣는다.
4. innerHTML로 HTML 구조를 출력한다.
5. 브라우저 화면에 회원 카드가 표시된다.
```

이 예제는 객체에 저장된 데이터를 HTML 화면에 출력하는 기본적인 형태이다.

---

# 실무 활용

DOM은 실제 웹 페이지의 거의 모든 동적인 기능에 사용된다.

## 텍스트 변경

```javascript
title.innerText = "새로운 제목";
```

## 입력값 출력

```javascript
result.innerText = input.value;
```

## 객체 데이터 출력

```javascript
profile.innerHTML = `
    <h2>${user.name}</h2>
`;
```

## 목록 출력

```javascript
list.innerHTML = html;
```

## 상태에 따른 화면 변경

```javascript
if (user.isLogin) {

    message.innerText = "로그인 상태입니다.";

} else {

    message.innerText = "로그인이 필요합니다.";

}
```

---

# 이번 문서에서 새롭게 배운 내용

- DOM은 HTML 문서를 JavaScript에서 사용할 수 있도록 객체 구조로 표현한 것이다.
- 브라우저는 HTML을 읽고 DOM Tree를 생성한다.
- `document`는 현재 HTML 문서 전체를 나타내는 객체이다.
- HTML 태그는 DOM에서 Element 객체가 된다.
- Node는 DOM을 구성하는 모든 항목을 의미한다.
- DOM 요소는 부모, 자식, 형제 관계를 가진다.
- `querySelector()`는 CSS 선택자를 이용하여 요소 하나를 선택한다.
- 요소를 찾지 못하면 `null`이 반환된다.
- JavaScript 실행 시점에 따라 요소 선택 결과가 달라질 수 있다.
- `innerText`, `textContent`, `innerHTML`로 요소 내용을 읽거나 변경할 수 있다.

---

# 자주 하는 실수

- HTML과 DOM을 완전히 같은 것으로 생각한다.
- `document`가 HTML 파일 자체라고 생각한다.
- `querySelector()`의 선택자에 `#`이나 `.`을 빠뜨린다.
- 여러 요소가 있어도 `querySelector()`가 모두 선택한다고 생각한다.
- 선택 결과가 `null`인지 확인하지 않고 프로퍼티를 사용한다.
- JavaScript가 HTML 요소보다 먼저 실행되도록 연결한다.
- `innerText`와 `innerHTML`의 차이를 구분하지 않는다.
- 단순 텍스트를 출력하면서 무조건 `innerHTML`을 사용한다.
- DOM을 변경하면 HTML 원본 파일도 변경된다고 생각한다.

---

# 면접 포인트

### DOM이란?

HTML 문서를 JavaScript에서 제어할 수 있도록 객체 구조로 표현한 것이다.

브라우저는 HTML을 분석한 뒤 DOM Tree를 생성한다.

---

### document 객체란?

현재 브라우저에 표시된 HTML 문서 전체를 나타내는 객체이다.

DOM 요소를 선택하거나 생성하고 변경할 때 사용한다.

---

### Element와 Node의 차이는?

Node는 DOM을 구성하는 모든 항목을 의미한다.

Element는 HTML 태그를 기반으로 만들어진 요소 노드이다.

모든 Element는 Node이지만, 모든 Node가 Element인 것은 아니다.

---

### querySelector()란?

CSS 선택자를 이용하여 조건에 맞는 첫 번째 요소 하나를 반환하는 메서드이다.

요소를 찾지 못하면 `null`을 반환한다.

---

### DOM 요소 선택 결과가 null인 이유는?

- 선택자가 잘못되었거나
- HTML에 요소가 없거나
- JavaScript가 DOM 생성 전에 실행되었을 가능성이 있다.

---

### innerText와 innerHTML의 차이는?

`innerText`는 값을 텍스트로 처리한다.

`innerHTML`은 문자열 안의 HTML 태그를 실제 요소로 해석한다.

---

### DOM과 BOM의 차이는?

DOM은 HTML 문서를 제어하기 위한 객체 구조이다.

BOM은 브라우저 창과 브라우저 기능을 제어하기 위한 객체 구조이다.

---

# 핵심 정리

- DOM은 HTML 문서를 객체 구조로 표현한 것이다.
- 브라우저는 HTML을 분석하여 DOM Tree를 생성한다.
- `document`는 현재 문서 전체를 나타낸다.
- DOM 요소도 JavaScript 객체이다.
- HTML 태그는 Element 객체가 된다.
- DOM은 부모, 자식, 형제 관계를 가진다.
- 요소 선택은 주로 `document.querySelector()`에서 시작한다.
- 요소를 찾지 못하면 `null`이 반환된다.
- DOM 조작 전에는 JavaScript 실행 시점을 확인해야 한다.
- `innerText`, `textContent`, `innerHTML`로 내용을 제어할 수 있다.
- DOM은 사용자와 상호작용하는 웹 기능의 기반이다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
