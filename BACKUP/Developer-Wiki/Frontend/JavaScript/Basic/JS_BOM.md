---
title: JS_BOM
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_BOM |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

JavaScript는 HTML(DOM)뿐만 아니라 브라우저 자체도 제어할 수 있다.

브라우저 창, 주소(URL), 뒤로가기, 새로고침, 화면 크기 등 브라우저와 관련된 기능을 제공하는 객체들의 집합을 **BOM(Browser Object Model)** 이라고 한다.

이번 문서에서는 BOM의 대표 객체인 `window`, `location`, `history`, `navigator`, `screen`과 자주 사용하는 브라우저 함수들을 학습한다.

---

# 핵심 개념

브라우저에서 JavaScript가 실행될 때 가장 최상위 객체는 `window`이다.

```text
window

├── document (DOM)

├── location

├── history

├── navigator

├── screen

├── localStorage

├── setTimeout()

├── setInterval()

└── ...
```

지금까지 사용했던 `document`, `localStorage`, `setTimeout()`도 모두 `window` 객체에 포함되어 있다.

---

# DOM과 BOM의 차이

| DOM | BOM |
|------|------|
| HTML 문서 제어 | 브라우저 제어 |
| document 객체 | window 객체 |
| 요소 선택 | 페이지 이동 |
| 내용 변경 | 브라우저 기능 사용 |

---

# window 객체

브라우저의 최상위 객체이다.

```javascript
console.log(window);
```

현재 브라우저에 대한 모든 정보를 확인할 수 있다.

---

# window 생략

다음 두 코드는 동일하다.

```javascript
window.alert("Hello");
```

```javascript
alert("Hello");
```

또는

```javascript
window.setTimeout(function(){

    console.log("실행");

},1000);
```

```javascript
setTimeout(function(){

    console.log("실행");

},1000);
```

대부분의 경우 `window.`는 생략한다.

> **실무 팁**  
> 브라우저 환경에서는 `window`를 생략하는 경우가 많지만, 다른 실행 환경(Node.js 등)에서는 `window`가 존재하지 않는다. 브라우저 전용 코드라는 점을 이해하고 사용하는 것이 중요하다.

---

# alert()

메시지를 출력하는 가장 간단한 함수이다.

```javascript
alert("안녕하세요.");
```

확인 버튼을 누를 때까지 다음 코드가 실행되지 않는다.

---

# confirm()

사용자의 확인 여부를 받을 수 있다.

```javascript
const result =

    confirm(

        "삭제하시겠습니까?"

    );

console.log(result);
```

확인

```text
true
```

취소

```text
false
```

---

# prompt()

사용자의 입력을 받을 수 있다.

```javascript
const name =

    prompt(

        "이름을 입력하세요."

    );

console.log(name);
```

입력

```text
홍길동
```

취소하면

```text
null
```

이 반환된다.

---

# alert(), confirm(), prompt() 비교

| 함수 | 반환값 |
|------|---------|
| alert() | 없음(undefined) |
| confirm() | true / false |
| prompt() | 문자열 또는 null |

---

---

# location 객체

`location` 객체는 현재 페이지의 URL 정보를 확인하거나 다른 페이지로 이동할 때 사용한다.

```javascript
console.log(location);
```

현재 페이지의 주소와 관련된 다양한 정보를 확인할 수 있다.

---

# 현재 URL 확인

```javascript
console.log(
    location.href
);
```

출력 예시

```text
https://example.com/product?id=10
```

`href`는 현재 페이지의 전체 주소(URL)를 반환한다.

---

# 페이지 이동

```javascript
location.href =
    "https://www.naver.com";
```

지정한 주소로 페이지를 이동한다.

---

# 페이지 새로고침

```javascript
location.reload();
```

현재 페이지를 다시 불러온다.

> **실무 팁**  
> AJAX나 Fetch로 데이터를 수정한 뒤 화면을 다시 표시해야 하는 경우 `location.reload()`를 사용할 수 있다. 다만 최근에는 필요한 부분만 갱신하는 방식(DOM 업데이트)을 더 많이 사용한다.

---

# URL의 경로 확인

```javascript
console.log(
    location.pathname
);
```

주소가

```text
https://example.com/product/list
```

이라면

출력

```text
/product/list
```

---

# URL의 Query String 확인

```javascript
console.log(
    location.search
);
```

주소가

```text
https://example.com/product?id=100
```

이라면

출력

```text
?id=100
```

검색 조건이나 상품 번호를 확인할 때 자주 사용한다.

---

# history 객체

`history` 객체는 브라우저의 방문 기록을 제어한다.

---

# 이전 페이지

```javascript
history.back();
```

브라우저의 뒤로가기와 동일하다.

---

# 다음 페이지

```javascript
history.forward();
```

브라우저의 앞으로가기와 동일하다.

---

# 특정 페이지 이동

```javascript
history.go(-2);
```

두 페이지 이전으로 이동한다.

```javascript
history.go(1);
```

한 페이지 앞으로 이동한다.

---

# navigator 객체

`navigator`는 브라우저와 운영체제 정보를 제공한다.

```javascript
console.log(
    navigator
);
```

---

# 브라우저 정보

```javascript
console.log(
    navigator.userAgent
);
```

출력 예시

```text
Mozilla/5.0 ...
```

현재 브라우저의 정보를 확인할 수 있다.

---

# 사용 언어 확인

```javascript
console.log(
    navigator.language
);
```

출력 예시

```text
ko-KR
```

브라우저에서 사용하는 언어를 확인할 수 있다.

---

# 온라인 여부 확인

```javascript
console.log(
    navigator.onLine
);
```

출력

```text
true
```

또는

```text
false
```

인터넷 연결 여부를 확인할 수 있다.

---

# screen 객체

`screen` 객체는 사용자의 화면 정보를 제공한다.

---

# 화면 너비

```javascript
console.log(
    screen.width
);
```

출력 예시

```text
1920
```

---

# 화면 높이

```javascript
console.log(
    screen.height
);
```

출력 예시

```text
1080
```

---

# 사용 가능한 화면 크기

```javascript
console.log(
    screen.availWidth
);

console.log(
    screen.availHeight
);
```

운영체제의 작업 표시줄 등을 제외한 실제 사용 가능한 화면 크기를 반환한다.

---

# window.open()

새 창 또는 새 탭을 연다.

```javascript
window.open(
    "https://www.naver.com"
);
```

브라우저 설정에 따라 새 창 또는 새 탭으로 열린다.

---

# window.close()

현재 창을 닫는다.

```javascript
window.close();
```

> **주의**  
> 일반적으로 JavaScript가 직접 연 창은 `close()`로 닫을 수 있지만, 사용자가 직접 연 브라우저 탭은 보안상의 이유로 닫을 수 없는 경우가 많다.

---

# 실무 활용

BOM은 다음과 같은 기능에서 자주 사용된다.

- 로그인 후 페이지 이동
- 상품 상세 페이지 이동
- 이전 페이지 버튼
- 브라우저 언어 확인
- 화면 크기 확인
- 모바일 여부 판단
- 팝업 창 열기
- 페이지 새로고침

---

# BOM 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. location.href를 올바르게 작성했는가?
2. URL이 올바른가?
3. history에 이동할 페이지가 존재하는가?
4. navigator 정보는 브라우저마다 다를 수 있다는 점을 이해했는가?
5. window.close()가 보안 정책에 의해 제한될 수 있는가?
```

---

---

# scrollTo()

`scrollTo()`는 페이지를 지정한 위치로 이동시키는 함수이다.

기본 문법

```javascript
window.scrollTo(
    x,
    y
);
```

예제

```javascript
window.scrollTo(
    0,
    500
);
```

페이지의 세로 위치를 500px까지 이동한다.

---

# scrollBy()

`scrollBy()`는 현재 위치를 기준으로 이동한다.

기본 문법

```javascript
window.scrollBy(
    x,
    y
);
```

예제

```javascript
window.scrollBy(
    0,
    300
);
```

현재 위치에서 아래로 300px 이동한다.

---

# 부드러운 스크롤

```javascript
window.scrollTo({

    top : 800,

    behavior : "smooth"

});
```

부드럽게 해당 위치까지 이동한다.

---

# resize 이벤트

브라우저 크기가 변경되면 발생하는 이벤트이다.

```javascript
window.addEventListener(

    "resize",

    function(){

        console.log(

            window.innerWidth

        );

    }

);
```

브라우저의 너비가 변경될 때마다 현재 너비를 출력한다.

---

# 현재 브라우저 크기

```javascript
console.log(
    window.innerWidth
);

console.log(
    window.innerHeight
);
```

출력 예시

```text
1280

720
```

브라우저 창의 현재 크기를 확인할 수 있다.

---

# 실무 예제 프로젝트

이번 예제에서는 페이지 맨 위로 이동하는 버튼을 구현한다.

## HTML

```html
<button id="topBtn">

TOP

</button>
```

---

## JavaScript

```javascript
const topBtn =

    document.querySelector(

        "#topBtn"

    );

topBtn.addEventListener(

    "click",

    function(){

        window.scrollTo({

            top : 0,

            behavior : "smooth"

        });

    }

);
```

사용자가 버튼을 누르면 페이지의 맨 위로 부드럽게 이동한다.

---

# 예제 코드 흐름

```text
TOP 버튼 클릭
        ↓
click 이벤트
        ↓
window.scrollTo()
        ↓
페이지 상단 이동
```

---

# 자주 하는 실수

## scrollTo()와 scrollBy()를 혼동하는 경우

```javascript
window.scrollTo(
    0,
    300
);
```

항상 절대 위치(300px)로 이동한다.

```javascript
window.scrollBy(
    0,
    300
);
```

현재 위치에서 300px 더 이동한다.

---

## location.reload()를 남용하는 경우

```javascript
location.reload();
```

데이터 일부만 변경하면 되는 상황에서도 페이지 전체를 다시 불러오는 경우가 있다.

실무에서는 필요한 DOM만 업데이트하는 방식을 더 많이 사용한다.

---

## alert()를 과도하게 사용하는 경우

```javascript
alert("완료");
```

사용자가 확인 버튼을 누를 때까지 화면이 멈춘다.

실무에서는 토스트 메시지나 모달을 사용하는 경우가 많다.

---

## window.close()가 동작하지 않는 경우

사용자가 직접 연 브라우저 탭은 보안 정책에 따라 닫을 수 없는 경우가 있다.

JavaScript가 `window.open()`으로 연 창에서 주로 사용된다.

---

# 디버깅 체크리스트

```text
1. location.href가 올바른 URL인가?
2. history 이동 가능한 페이지가 존재하는가?
3. navigator 정보는 브라우저마다 달라질 수 있는가?
4. scrollTo()와 scrollBy()를 구분했는가?
5. resize 이벤트가 정상 등록되었는가?
6. window.close()의 동작 제한을 이해했는가?
```

---

# 이번 문서에서 배운 내용

- BOM 개념
- window 객체
- alert()
- confirm()
- prompt()
- location
- history
- navigator
- screen
- window.open()
- window.close()
- scrollTo()
- scrollBy()
- resize 이벤트

---

# 면접 포인트

### BOM이란 무엇인가?

브라우저 자체를 제어하기 위한 객체들의 집합이다.

대표적으로 `window`, `location`, `history`, `navigator`, `screen` 등이 있다.

---

### DOM과 BOM의 차이점은?

- DOM은 HTML 문서를 제어한다.
- BOM은 브라우저 자체를 제어한다.

---

### location.href는 언제 사용하는가?

현재 URL을 확인하거나 다른 페이지로 이동할 때 사용한다.

---

### history.back()은 어떤 기능인가?

브라우저의 뒤로가기와 동일한 기능을 수행한다.

---

### navigator 객체는 언제 사용하는가?

브라우저 정보, 운영체제 정보, 언어 설정, 온라인 여부 등을 확인할 때 사용한다.

---

### scrollTo()와 scrollBy()의 차이점은?

- `scrollTo()`는 절대 위치로 이동한다.
- `scrollBy()`는 현재 위치를 기준으로 이동한다.

---

# 핵심 정리

- BOM은 브라우저를 제어하는 객체들의 집합이다.
- `window`는 브라우저의 최상위 객체이다.
- `location`은 URL과 페이지 이동을 담당한다.
- `history`는 방문 기록을 제어한다.
- `navigator`는 브라우저 정보를 제공한다.
- `screen`은 화면 정보를 제공한다.
- `scrollTo()`와 `scrollBy()`는 스크롤을 제어한다.
- BOM은 로그인, 페이지 이동, 반응형 UI, 팝업 등 다양한 기능에서 활용된다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
