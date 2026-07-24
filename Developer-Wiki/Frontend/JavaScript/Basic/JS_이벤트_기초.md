---
title: JS_이벤트_기초
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_이벤트_기초 |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

웹 페이지는 단순히 화면을 보여주는 것만으로는 충분하지 않다.

사용자가 버튼을 클릭하거나 키보드를 입력하고, 마우스를 움직이는 등의 행동에 반응해야 비로소 동적인 웹 애플리케이션이 된다.

이러한 사용자의 행동을 **이벤트(Event)**라고 하며, JavaScript는 이벤트가 발생했을 때 원하는 코드를 실행할 수 있도록 다양한 기능을 제공한다.

이번 문서에서는 이벤트의 개념과 이벤트 등록 방법, 그리고 가장 많이 사용하는 `addEventListener()`를 중심으로 학습한다.

---

# 핵심 개념

이벤트(Event)는 웹 페이지에서 발생하는 모든 사용자 또는 브라우저의 동작을 의미한다.

예를 들어 다음과 같은 상황이 모두 이벤트이다.

- 버튼 클릭
- 마우스 이동
- 키보드 입력
- 입력창 내용 변경
- 페이지 로드 완료
- 스크롤 이동
- 폼 제출

JavaScript는 이러한 이벤트가 발생했을 때 특정 함수를 실행할 수 있다.

---

# 이벤트 처리 흐름

```text
사용자 동작
        ↓
이벤트 발생
        ↓
JavaScript가 이벤트 감지
        ↓
등록된 함수 실행
        ↓
화면 변경
```

---

# 기본 문법

가장 많이 사용하는 이벤트 등록 방법은 `addEventListener()`이다.

```javascript
element.addEventListener(
    "이벤트이름",
    함수
);
```

또는

```javascript
element.addEventListener(
    "click",
    function () {

        실행할 코드

    }
);
```

---

# 주요 개념

## 이벤트(Event)

이벤트는 사용자의 행동이나 브라우저의 상태 변화를 의미한다.

예를 들어 버튼을 클릭하면 `click` 이벤트가 발생한다.

```html
<button id="btn">
클릭
</button>
```

```javascript
const btn =
    document.querySelector("#btn");

btn.addEventListener(
    "click",
    function () {

        console.log("클릭");

    }
);
```

버튼을 클릭할 때마다 함수가 실행된다.

---

## 이벤트 리스너(Event Listener)

이벤트 리스너(Event Listener)는 특정 이벤트를 기다렸다가 이벤트가 발생하면 함수를 실행하는 기능이다.

```javascript
btn.addEventListener(
    "click",
    function () {

        console.log("Hello");

    }
);
```

여기서

- `"click"` → 이벤트 종류
- `function(){}` → 실행할 함수

이다.

---

## addEventListener()

실무에서 가장 많이 사용하는 이벤트 등록 방법이다.

```javascript
button.addEventListener(
    "click",
    function () {

        alert("안녕하세요");

    }
);
```

하나의 요소에 여러 개의 이벤트를 등록할 수 있다는 장점이 있다.

---

## onclick와의 차이

예전에는 다음과 같이 많이 작성했다.

```javascript
button.onclick = function () {

    console.log("클릭");

};
```

하지만 `onclick`은 하나의 함수만 등록할 수 있다.

반면 `addEventListener()`는 여러 개의 이벤트를 등록할 수 있어 실무에서는 대부분 이 방식을 사용한다.

---

## onclick 예제

```javascript
button.onclick = function () {

    console.log("첫 번째");

};

button.onclick = function () {

    console.log("두 번째");

};
```

실행 결과

```text
두 번째
```

첫 번째 함수는 덮어써진다.

---

## addEventListener 예제

```javascript
button.addEventListener(
    "click",
    function () {

        console.log("첫 번째");

    }
);

button.addEventListener(
    "click",
    function () {

        console.log("두 번째");

    }
);
```

실행 결과

```text
첫 번째
두 번째
```

두 함수가 모두 실행된다.

---

## 이벤트 등록 순서

```text
1. 요소 선택
        ↓
2. 이벤트 등록
        ↓
3. 사용자 동작
        ↓
4. 함수 실행
```

---

## 첫 번째 이벤트 예제

```html
<button id="hello">
인사하기
</button>

<p id="result"></p>
```

```javascript
const hello =
    document.querySelector("#hello");

const result =
    document.querySelector("#result");

hello.addEventListener(
    "click",
    function () {

        result.innerText =
            "안녕하세요!";

    }
);
```

버튼을 클릭하면 문장이 변경된다.

---

## 여러 요소에 이벤트 등록

```html
<button class="menu">
HTML
</button>

<button class="menu">
CSS
</button>

<button class="menu">
JavaScript
</button>
```

```javascript
const menus =
    document.querySelectorAll(".menu");

menus.forEach(function(menu){

    menu.addEventListener(
        "click",
        function(){

            console.log(
                menu.innerText
            );

        }
    );

});
```

각 버튼을 클릭하면 해당 버튼의 텍스트가 출력된다.

---

# 자주 사용하는 이벤트 종류

| 이벤트 | 설명 |
|---------|------|
| click | 클릭 |
| dblclick | 더블 클릭 |
| mouseenter | 마우스를 올림 |
| mouseleave | 마우스를 벗어남 |
| input | 입력값 변경 |
| change | 값 변경 완료 |
| submit | 폼 제출 |
| keydown | 키를 누름 |
| keyup | 키에서 손을 뗌 |

---

# 이벤트 등록 디버깅

이벤트가 실행되지 않는다면 다음을 확인한다.

```text
1. 요소를 제대로 선택했는가?
2. addEventListener()의 이벤트 이름을 올바르게 작성했는가?
3. JavaScript가 HTML보다 먼저 실행되지 않았는가?
4. 이벤트를 등록하기 전에 요소가 존재하는가?
5. console.log()로 함수가 실행되는지 확인했는가?
```

---

---

# click 이벤트

`click` 이벤트는 사용자가 요소를 한 번 클릭했을 때 발생한다.

가장 많이 사용하는 이벤트이며 버튼, 링크, 이미지 등 거의 모든 요소에서 사용할 수 있다.

## HTML

```html
<button id="btn">
클릭
</button>

<p id="result"></p>
```

## JavaScript

```javascript
const btn =
    document.querySelector("#btn");

const result =
    document.querySelector("#result");

btn.addEventListener(
    "click",
    function () {

        result.innerText =
            "버튼을 클릭했습니다.";

    }
);
```

---

# dblclick 이벤트

`dblclick` 이벤트는 요소를 빠르게 두 번 클릭했을 때 발생한다.

## JavaScript

```javascript
btn.addEventListener(
    "dblclick",
    function () {

        console.log(
            "더블 클릭"
        );

    }
);
```

실무에서는 이미지 확대, 카드 뒤집기 등의 기능에서 사용할 수 있다.

---

# mouseenter 이벤트

마우스가 요소 안으로 들어올 때 발생한다.

```javascript
box.addEventListener(
    "mouseenter",
    function () {

        console.log(
            "마우스 진입"
        );

    }
);
```

---

# mouseleave 이벤트

마우스가 요소 밖으로 나갈 때 발생한다.

```javascript
box.addEventListener(
    "mouseleave",
    function () {

        console.log(
            "마우스 종료"
        );

    }
);
```

---

# Hover 효과 구현

## HTML

```html
<div id="card">
상품 카드
</div>
```

## JavaScript

```javascript
const card =
    document.querySelector("#card");

card.addEventListener(
    "mouseenter",
    function () {

        card.style.backgroundColor =
            "skyblue";

    }
);

card.addEventListener(
    "mouseleave",
    function () {

        card.style.backgroundColor =
            "";

    }
);
```

실무에서는 카드 강조, 메뉴 표시, 툴팁 등에 활용된다.

---

# input 이벤트

`input` 이벤트는 사용자가 입력하는 동안 계속 발생한다.

## HTML

```html
<input
    id="userName"
>

<p id="preview"></p>
```

## JavaScript

```javascript
const userName =
    document.querySelector(
        "#userName"
    );

const preview =
    document.querySelector(
        "#preview"
    );

userName.addEventListener(
    "input",
    function () {

        preview.innerText =
            userName.value;

    }
);
```

입력할 때마다 화면이 실시간으로 변경된다.

---

# input 이벤트 활용

- 실시간 검색
- 글자 수 표시
- 비밀번호 강도 검사
- 자동 완성
- 닉네임 미리보기

실시간으로 반응해야 하는 기능에서 많이 사용된다.

---

# change 이벤트

`change` 이벤트는 값의 변경이 완료되었을 때 발생한다.

## HTML

```html
<select id="city">

<option>서울</option>
<option>부산</option>
<option>대전</option>

</select>
```

## JavaScript

```javascript
const city =
    document.querySelector(
        "#city"
    );

city.addEventListener(
    "change",
    function () {

        console.log(
            city.value
        );

    }
);
```

선택을 변경하면 이벤트가 실행된다.

---

# input와 change의 차이

| input | change |
|--------|---------|
| 입력 중 계속 발생 | 변경 완료 후 발생 |
| 실시간 처리 | 최종 값 처리 |
| 검색 | 선택 완료 |

---

# keydown 이벤트

키를 누르는 순간 발생한다.

```javascript
document.addEventListener(
    "keydown",
    function () {

        console.log(
            "키 입력"
        );

    }
);
```

---

# keyup 이벤트

누른 키를 떼는 순간 발생한다.

```javascript
document.addEventListener(
    "keyup",
    function () {

        console.log(
            "키를 뗌"
        );

    }
);
```

---

# keydown과 keyup 비교

| 이벤트 | 발생 시점 |
|----------|-----------|
| keydown | 키를 누름 |
| keyup | 키를 뗌 |

게임이나 단축키는 `keydown`을 많이 사용하며, 입력 완료 확인은 `keyup`을 사용하는 경우가 많다.

---

# 이벤트 등록 위치

가장 일반적인 순서는 다음과 같다.

```javascript
const button =
    document.querySelector(
        "#button"
    );

button.addEventListener(
    "click",
    function () {

        console.log("실행");

    }
);
```

1. 요소를 선택한다.
2. 이벤트를 등록한다.
3. 이벤트가 발생하면 함수가 실행된다.

---

# 실무 예제 ① 좋아요 버튼

## HTML

```html
<button id="like">
🤍 좋아요
</button>
```

## JavaScript

```javascript
const like =
    document.querySelector(
        "#like"
    );

like.addEventListener(
    "click",
    function () {

        like.innerText =
            "❤️ 좋아요";

    }
);
```

---

# 실무 예제 ② 글자 수 표시

## HTML

```html
<textarea
    id="content">
</textarea>

<p id="count">
0
</p>
```

## JavaScript

```javascript
const content =
    document.querySelector(
        "#content"
    );

const count =
    document.querySelector(
        "#count"
    );

content.addEventListener(
    "input",
    function () {

        count.innerText =
            content.value.length;

    }
);
```

입력할 때마다 현재 글자 수가 표시된다.

---

# 실무 예제 ③ 메뉴 Hover

```javascript
menu.addEventListener(
    "mouseenter",
    function () {

        menu.style.color =
            "red";

    }
);

menu.addEventListener(
    "mouseleave",
    function () {

        menu.style.color =
            "";

    }
);
```

마우스를 올렸을 때만 스타일을 변경할 수 있다.

---

# 이벤트 디버깅 체크리스트

이벤트가 정상적으로 동작하지 않는다면 다음 사항을 확인한다.

```text
1. 이벤트 이름(click, input 등)을 정확히 작성했는가?
2. querySelector()가 null을 반환하지 않았는가?
3. addEventListener()를 요소 선택 후 호출했는가?
4. defer 또는 DOMContentLoaded를 사용하여 HTML이 먼저 로드되었는가?
5. 함수 내부에 console.log()를 넣어 실행 여부를 확인했는가?
```

---

---

# 실무 활용

이벤트는 사용자의 행동에 반응하는 기능이므로 대부분의 웹 서비스에서 사용된다.

대표적인 활용 사례는 다음과 같다.

- 로그인 버튼 클릭
- 회원가입 폼 제출
- 검색창 실시간 검색
- 메뉴 Hover 효과
- 상품 이미지 변경
- 좋아요 버튼
- 장바구니 수량 변경
- 다크 모드 전환
- 모달 창 열기 및 닫기

웹 페이지가 사용자와 상호작용하는 거의 모든 기능은 이벤트를 기반으로 동작한다.

---

# 실무 예제 프로젝트

이번 예제에서는 간단한 로그인 화면을 구현해본다.

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>로그인</title>
    <script src="main.js" defer></script>
</head>
<body>

<h1>로그인</h1>

<input
    type="text"
    id="userId"
    placeholder="아이디"
>

<br><br>

<input
    type="password"
    id="userPw"
    placeholder="비밀번호"
>

<br><br>

<button id="loginButton">
로그인
</button>

<p id="result"></p>

</body>
</html>
```

---

## JavaScript

```javascript
const userId =
    document.querySelector(
        "#userId"
    );

const userPw =
    document.querySelector(
        "#userPw"
    );

const loginButton =
    document.querySelector(
        "#loginButton"
    );

const result =
    document.querySelector(
        "#result"
    );

loginButton.addEventListener(
    "click",
    function () {

        if (
            userId.value === ""
        ) {

            result.innerText =
                "아이디를 입력해주세요.";

            return;

        }

        if (
            userPw.value === ""
        ) {

            result.innerText =
                "비밀번호를 입력해주세요.";

            return;

        }

        result.innerText =
            "로그인 성공";

    }
);
```

---

# 이벤트 처리 흐름

```text
사용자 클릭
        ↓
click 이벤트 발생
        ↓
addEventListener()가 감지
        ↓
등록된 함수 실행
        ↓
입력값 검사
        ↓
화면 변경
```

---

# 여러 이벤트 함께 사용하기

하나의 요소에는 여러 이벤트를 등록할 수 있다.

```javascript
const input =
    document.querySelector(
        "#userName"
    );

input.addEventListener(
    "focus",
    function () {

        console.log(
            "입력 시작"
        );

    }
);

input.addEventListener(
    "input",
    function () {

        console.log(
            input.value
        );

    }
);

input.addEventListener(
    "blur",
    function () {

        console.log(
            "입력 종료"
        );

    }
);
```

입력창에 커서를 두고, 값을 입력하고, 다른 곳을 클릭하면 세 이벤트가 순서대로 발생한다.

---

# 이벤트 등록 시 주의사항

## 같은 요소를 여러 번 선택하지 않기

좋지 않은 예

```javascript
document.querySelector("#btn")
    .addEventListener("click", function () {

        document.querySelector("#result")
            .innerText = "완료";

    });
```

좋은 예

```javascript
const btn =
    document.querySelector(
        "#btn"
    );

const result =
    document.querySelector(
        "#result"
    );

btn.addEventListener(
    "click",
    function () {

        result.innerText =
            "완료";

    }
);
```

요소를 변수에 저장하면 코드의 가독성과 유지보수성이 좋아진다.

---

# 이벤트 등록 순서 권장 방식

실무에서는 다음과 같은 순서를 많이 사용한다.

```text
1. 필요한 요소 선택
        ↓
2. 변수 선언
        ↓
3. 이벤트 등록
        ↓
4. 함수 내부에서 로직 작성
```

이 순서를 지키면 코드의 구조를 이해하기 쉽다.

---

# 이번 문서에서 새롭게 배운 내용

- 이벤트(Event)의 개념
- 이벤트 리스너(Event Listener)
- `addEventListener()` 사용법
- `onclick`과의 차이
- `click`
- `dblclick`
- `mouseenter`
- `mouseleave`
- `input`
- `change`
- `keydown`
- `keyup`
- 여러 이벤트 등록 방법
- 이벤트 처리 흐름

---

# 자주 하는 실수

- 이벤트 이름을 잘못 작성한다.
- 요소를 선택하기 전에 이벤트를 등록한다.
- `querySelector()`가 `null`을 반환하는데 그대로 사용한다.
- `onclick`과 `addEventListener()`를 혼동한다.
- 같은 요소를 반복해서 선택한다.
- `input`과 `change`의 차이를 이해하지 못한다.
- `keydown`과 `keyup`을 상황에 맞게 구분하지 않는다.

---

# 면접 포인트

### Event란 무엇인가?

사용자의 동작이나 브라우저의 상태 변화와 같이 JavaScript가 감지할 수 있는 모든 사건을 의미한다.

---

### addEventListener()를 사용하는 이유는?

하나의 요소에 여러 이벤트를 등록할 수 있고, 코드의 유지보수성이 높기 때문에 실무에서 가장 많이 사용한다.

---

### onclick과 addEventListener()의 차이는?

`onclick`은 하나의 함수만 등록할 수 있다.

`addEventListener()`는 여러 개의 이벤트 리스너를 등록할 수 있다.

---

### input과 change의 차이는?

`input`은 입력 중에도 계속 발생한다.

`change`는 입력 또는 선택이 완료된 후 발생한다.

---

### keydown과 keyup의 차이는?

`keydown`은 키를 누르는 순간 발생한다.

`keyup`은 키에서 손을 떼는 순간 발생한다.

---

# 핵심 정리

- 이벤트는 사용자와 브라우저의 동작을 의미한다.
- 이벤트가 발생하면 등록된 함수가 실행된다.
- `addEventListener()`는 가장 많이 사용하는 이벤트 등록 방법이다.
- 하나의 요소에 여러 이벤트를 등록할 수 있다.
- `click`, `input`, `change`, `keydown` 등은 자주 사용하는 이벤트이다.
- 요소를 먼저 선택한 후 이벤트를 등록하는 것이 일반적인 작성 순서이다.
- 이벤트를 활용하면 정적인 HTML을 동적인 웹 페이지로 만들 수 있다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
