---
title: JS_이벤트_객체
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_이벤트_객체 |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

이벤트를 등록하면 함수가 실행되는 것까지는 이전 문서에서 학습했다.

하지만 실제 프로젝트에서는 **어떤 요소에서 이벤트가 발생했는지**, **기본 동작을 막아야 하는지**, **현재 클릭한 요소가 무엇인지**를 알아야 하는 경우가 많다.

JavaScript는 이러한 정보를 **이벤트 객체(Event Object)**를 통해 제공한다.

이번 문서에서는 이벤트 객체의 개념과 `event.target`, `event.currentTarget`, `preventDefault()` 등을 학습한다.

---

# 핵심 개념

이벤트가 발생하면 브라우저는 이벤트와 관련된 다양한 정보를 담은 객체를 자동으로 생성한다.

이를 **이벤트 객체(Event Object)**라고 한다.

이 객체에는 다음과 같은 정보가 저장된다.

- 어떤 이벤트가 발생했는가
- 어떤 요소에서 발생했는가
- 마우스 위치
- 입력한 키
- 기본 동작 정보
- 이벤트를 발생시킨 요소

이벤트 객체는 이벤트 리스너의 매개변수로 전달받을 수 있다.

---

# 이벤트 처리 흐름

```text
사용자 클릭
        ↓
이벤트 발생
        ↓
브라우저가 Event 객체 생성
        ↓
이벤트 리스너로 전달
        ↓
JavaScript에서 사용
```

---

# 기본 문법

이벤트 객체는 함수의 매개변수로 받을 수 있다.

```javascript
element.addEventListener(
    "click",
    function(event){

    }
);
```

매개변수 이름은 `event`가 가장 많이 사용되지만 `e`처럼 다른 이름을 사용해도 된다.

```javascript
button.addEventListener(
    "click",
    function(e){

    }
);
```

---

# 주요 개념

## Event 객체 확인하기

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
    function(event){

        console.log(event);

    }
);
```

버튼을 클릭하면 Event 객체가 출력된다.

브라우저 개발자 도구에서 다양한 속성을 확인할 수 있다.

---

# event.type

`event.type`은 발생한 이벤트의 종류를 나타낸다.

```javascript
btn.addEventListener(
    "click",
    function(event){

        console.log(
            event.type
        );

    }
);
```

결과

```text
click
```

---

# event.target

`event.target`은 **실제로 이벤트가 발생한 요소**를 반환한다.

```javascript
btn.addEventListener(
    "click",
    function(event){

        console.log(
            event.target
        );

    }
);
```

결과

```text
<button id="btn">
```

---

# event.target 활용

텍스트를 변경할 수도 있다.

```javascript
btn.addEventListener(
    "click",
    function(event){

        event.target.innerText =
            "완료";

    }
);
```

클릭한 버튼의 글자가 변경된다.

---

# event.target과 변수 비교

다음 두 코드는 같은 결과를 만든다.

```javascript
btn.innerText =
    "완료";
```

```javascript
event.target.innerText =
    "완료";
```

하지만 여러 요소에서 하나의 이벤트를 처리하는 경우에는 `event.target`이 훨씬 유용하다.

---

# event.currentTarget

`event.currentTarget`은 **이벤트 리스너가 등록된 요소**를 반환한다.

대부분의 단순한 예제에서는 `event.target`과 같은 값을 가진다.

```javascript
btn.addEventListener(
    "click",
    function(event){

        console.log(
            event.currentTarget
        );

    }
);
```

---

# event.target과 event.currentTarget

현재 단계에서는 대부분 같은 요소를 가리킨다.

| 속성 | 의미 |
|------|------|
| event.target | 실제 이벤트가 발생한 요소 |
| event.currentTarget | 이벤트가 등록된 요소 |

이후 **이벤트 버블링(Event Bubbling)**을 배우면 두 속성의 차이를 명확하게 이해할 수 있다.

> **실무 팁**  
> 현재 단계에서는 `event.target`을 중심으로 익히고, `event.currentTarget`은 "이벤트가 등록된 요소"를 반환한다는 정도만 이해해도 충분하다. 이벤트 전파(Event Bubbling)는 이후 문서에서 자세히 다룬다.

---

---

# preventDefault()

브라우저에는 요소마다 기본적으로 수행되는 동작이 있다.

예를 들어

- 링크(`<a>`)를 클릭하면 페이지가 이동한다.
- `<form>`을 제출하면 페이지가 새로고침된다.

이러한 기본 동작을 막고 싶을 때 사용하는 메서드가 `preventDefault()`이다.

---

## 기본 문법

```javascript
element.addEventListener(
    "click",
    function(event){

        event.preventDefault();

    }
);
```

---

# 링크 이동 막기

## HTML

```html
<a
    href="https://google.com"
    id="google"
>
Google
</a>
```

## JavaScript

```javascript
const google =
    document.querySelector(
        "#google"
    );

google.addEventListener(
    "click",
    function(event){

        event.preventDefault();

        console.log(
            "링크 이동 취소"
        );

    }
);
```

Google 페이지로 이동하지 않고 콘솔만 출력된다.

---

# Form 제출 막기

회원가입이나 로그인 화면에서는 입력값 검사가 끝난 뒤에만 서버로 전송해야 한다.

이때 `preventDefault()`를 많이 사용한다.

## HTML

```html
<form id="loginForm">

<input
    type="text"
    id="userId"
>

<button>
로그인
</button>

</form>
```

---

## JavaScript

```javascript
const loginForm =
    document.querySelector(
        "#loginForm"
    );

loginForm.addEventListener(
    "submit",
    function(event){

        event.preventDefault();

        console.log(
            "폼 제출 중지"
        );

    }
);
```

---

# 언제 사용하는가?

대표적으로 다음과 같은 상황에서 사용한다.

- 로그인 유효성 검사
- 회원가입 입력 검사
- 게시글 작성 검사
- 댓글 작성
- AJAX 요청
- SPA(Single Page Application) 화면 전환

실무에서는 `submit` 이벤트와 함께 사용하는 경우가 매우 많다.

---

# this와 event.target

이벤트 함수 안에서는 `this`도 사용할 수 있다.

```javascript
button.addEventListener(
    "click",
    function(event){

        console.log(this);

        console.log(
            event.target
        );

    }
);
```

현재 단계에서는 두 값이 동일하게 보인다.

---

# this 사용 예제

```javascript
button.addEventListener(
    "click",
    function(){

        this.innerText =
            "완료";

    }
);
```

---

# event.target 사용 예제

```javascript
button.addEventListener(
    "click",
    function(event){

        event.target.innerText =
            "완료";

    }
);
```

동일한 결과가 출력된다.

---

# this와 event.target 비교

| this | event.target |
|------|--------------|
| 이벤트 리스너가 등록된 요소 | 실제 이벤트가 발생한 요소 |

현재 단계에서는 대부분 같은 요소를 가리킨다.

이후 이벤트 버블링을 배우면 차이를 이해할 수 있다.

> **실무 팁**  
> 화살표 함수(`() => {}`)에서는 `this`가 일반 함수와 다르게 동작한다. 현재 단계에서는 일반 함수(`function(){}`)를 기준으로 학습하고, 화살표 함수와 `this`의 관계는 이후 문서에서 자세히 다룬다.

---

# 여러 버튼 처리하기

## HTML

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

---

## JavaScript

```javascript
const menus =
    document.querySelectorAll(
        ".menu"
    );

menus.forEach(function(menu){

    menu.addEventListener(
        "click",
        function(event){

            console.log(
                event.target.innerText
            );

        }
    );

});
```

클릭한 버튼의 글자만 출력된다.

---

# 이미지 변경하기

## HTML

```html
<img

id="profile"

src="user.png"

width="200"

>
```

## JavaScript

```javascript
const profile =
    document.querySelector(
        "#profile"
    );

profile.addEventListener(
    "click",
    function(event){

        event.target.setAttribute(
            "src",
            "admin.png"
        );

    }
);
```

이미지를 클릭하면 다른 이미지로 변경된다.

---

# 입력창 포커스 이동

## HTML

```html
<input id="name">

<input id="email">
```

## JavaScript

```javascript
const nameInput =
    document.querySelector(
        "#name"
    );

nameInput.addEventListener(
    "keydown",
    function(event){

        console.log(
            event.type
        );

    }
);
```

키를 누를 때마다 이벤트 객체를 통해 어떤 이벤트가 발생했는지 확인할 수 있다.

---

# 이벤트 객체 확인하기

개발자 도구에서 이벤트 객체를 출력해 보면 다양한 정보를 확인할 수 있다.

```javascript
document.addEventListener(
    "click",
    function(event){

        console.log(event);

    }
);
```

대표적인 속성은 다음과 같다.

| 속성 | 설명 |
|------|------|
| type | 이벤트 종류 |
| target | 이벤트가 발생한 요소 |
| currentTarget | 이벤트가 등록된 요소 |
| preventDefault() | 기본 동작 취소 |

---

# 실무 활용

이벤트 객체는 다음과 같은 기능에서 자주 사용된다.

- 클릭한 상품 확인
- 메뉴 선택
- 게시글 수정
- 삭제 버튼 처리
- 이미지 변경
- 로그인 폼 검사
- 회원가입 입력 검사
- 링크 이동 제어

사용자가 어떤 요소와 상호작용했는지 확인해야 하는 대부분의 상황에서 이벤트 객체가 활용된다.

---

# 이벤트 객체 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. event 매개변수를 선언했는가?
2. preventDefault()를 필요한 위치에서 호출했는가?
3. event.target과 currentTarget을 혼동하지 않았는가?
4. this를 화살표 함수에서 사용하고 있지는 않은가?
5. console.log(event)로 객체를 확인했는가?
```

---

---

# 실무 활용

이벤트 객체는 단순히 이벤트 발생 여부를 확인하는 용도가 아니다.

실무에서는 **어떤 요소에서 이벤트가 발생했는지**, **브라우저의 기본 동작을 제어해야 하는지**, **이벤트 종류가 무엇인지**를 확인하기 위해 매우 자주 사용한다.

대표적인 활용 사례는 다음과 같다.

- 메뉴 선택
- 게시글 수정/삭제 버튼
- 이미지 클릭 확대
- 쇼핑몰 상품 선택
- 로그인 및 회원가입 폼 검사
- 댓글 등록
- 링크 이동 제어
- 페이지 새로고침 방지

---

# 실무 예제 프로젝트

이번 예제에서는 게시글 목록에서 클릭한 게시글의 제목을 출력해본다.

## HTML

```html
<ul>

<li class="post">
HTML 기초
</li>

<li class="post">
CSS 기초
</li>

<li class="post">
JavaScript 기초
</li>

</ul>

<p id="result"></p>
```

---

## JavaScript

```javascript
const posts =
    document.querySelectorAll(
        ".post"
    );

const result =
    document.querySelector(
        "#result"
    );

posts.forEach(function(post){

    post.addEventListener(
        "click",
        function(event){

            result.innerText =
                event.target.innerText;

        }
    );

});
```

---

# 예제 코드 흐름

```text
1. 게시글 목록 선택
        ↓
2. 결과 출력 요소 선택
        ↓
3. 각 게시글에 클릭 이벤트 등록
        ↓
4. 클릭 발생
        ↓
5. event.target으로 클릭한 요소 확인
        ↓
6. 제목 출력
```

---

# preventDefault() 활용 예제

회원가입 화면에서는 입력값이 올바를 때만 폼을 제출하는 경우가 많다.

```javascript
joinForm.addEventListener(
    "submit",
    function(event){

        if (
            userName.value === ""
        ) {

            event.preventDefault();

            alert(
                "이름을 입력하세요."
            );

        }

    }
);
```

조건을 만족하지 않으면 폼 제출이 중단된다.

---

# 이벤트 객체를 사용하는 이유

이벤트 객체를 사용하면 이벤트가 발생한 요소를 직접 확인할 수 있다.

예를 들어 여러 버튼이 있는 경우에도 각각의 버튼에 대해 별도의 변수를 만들 필요 없이 처리할 수 있다.

```javascript
buttons.forEach(function(button){

    button.addEventListener(
        "click",
        function(event){

            console.log(
                event.target.innerText
            );

        }
    );

});
```

동일한 로직을 여러 요소에서 재사용할 수 있다는 장점이 있다.

---

# 오류 분석

## 오류 1

```javascript
button.addEventListener(
    "click",
    function(){

        console.log(event);

    }
);
```

일부 환경에서는 `event`를 자동으로 사용할 수 있지만, 항상 동작하는 것은 아니다.

올바른 코드

```javascript
button.addEventListener(
    "click",
    function(event){

        console.log(event);

    }
);
```

이벤트 객체는 매개변수로 전달받아 사용하는 습관을 들이는 것이 좋다.

---

## 오류 2

```javascript
event.preventDefault;
```

괄호를 작성하지 않으면 함수가 실행되지 않는다.

올바른 코드

```javascript
event.preventDefault();
```

---

## 오류 3

```javascript
event.target.innerHTML =
    userInput;
```

사용자가 입력한 문자열을 그대로 `innerHTML`에 넣으면 의도하지 않은 HTML이 생성될 수 있다.

일반적인 텍스트를 출력할 때는 `innerText`를 사용하는 것이 안전하다.

---

## 오류 4

```javascript
event.currentTarget
```

과

```javascript
event.target
```

을 같은 의미로 사용하는 경우가 많다.

현재 단계에서는 대부분 같은 결과를 확인하지만, 이후 이벤트 버블링을 배우면 서로 다른 값을 가질 수 있다는 점을 기억해 두자.

---

# 이벤트 객체 디버깅 체크리스트

```text
1. event 매개변수를 선언했는가?
2. console.log(event)를 출력해 보았는가?
3. event.target을 올바르게 사용했는가?
4. preventDefault()를 호출했는가?
5. this와 event.target을 혼동하지 않았는가?
6. 이벤트가 실제로 발생하고 있는가?
```

---

# 이번 문서에서 새롭게 배운 내용

- Event Object의 개념
- Event 객체 생성 과정
- event.type
- event.target
- event.currentTarget
- preventDefault()
- this와 event.target 비교
- 여러 요소에서 Event 객체 활용
- 이벤트 객체 디버깅 방법

---

# 자주 하는 실수

- event 매개변수를 선언하지 않는다.
- preventDefault()를 호출하지 않는다.
- preventDefault 뒤에 괄호를 생략한다.
- event.target과 currentTarget을 같은 개념으로 이해한다.
- 일반 함수와 화살표 함수의 this를 혼동한다.
- 이벤트 객체를 출력하지 않고 추측만으로 디버깅한다.

---

# 면접 포인트

### Event Object란 무엇인가?

브라우저가 이벤트 발생 시 자동으로 생성하여 이벤트 리스너에 전달하는 객체이다.

이벤트 종류, 발생한 요소, 기본 동작 등 다양한 정보를 포함한다.

---

### event.target은 무엇인가?

실제로 이벤트가 발생한 요소를 반환하는 프로퍼티이다.

클릭한 버튼이나 선택한 요소를 확인할 때 자주 사용한다.

---

### event.currentTarget은 무엇인가?

이벤트 리스너가 등록된 요소를 반환한다.

이벤트 버블링이 발생하는 상황에서 `event.target`과 다른 값을 가질 수 있다.

---

### preventDefault()는 언제 사용하는가?

브라우저의 기본 동작(링크 이동, 폼 제출 등)을 막고 직접 원하는 동작을 구현할 때 사용한다.

---

### this와 event.target의 차이는?

현재 단계에서는 대부분 같은 요소를 가리키지만, 이벤트 전파와 화살표 함수에서는 차이가 발생할 수 있다.

---

# 핵심 정리

- 브라우저는 이벤트가 발생하면 Event 객체를 생성한다.
- Event 객체는 이벤트와 관련된 다양한 정보를 담고 있다.
- `event.target`은 실제 이벤트가 발생한 요소를 나타낸다.
- `event.currentTarget`은 이벤트가 등록된 요소를 나타낸다.
- `preventDefault()`를 사용하면 브라우저의 기본 동작을 막을 수 있다.
- Event 객체를 활용하면 하나의 로직으로 여러 요소를 효율적으로 처리할 수 있다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
