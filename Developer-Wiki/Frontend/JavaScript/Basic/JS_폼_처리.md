---
title: JS_폼_처리
version: v1.0
last_updated: 2026-07-22
status: completed
---

# 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JS_폼_처리 |
| 분야 | Frontend / JavaScript |
| 버전 | v1.0 |
| 작성일 | 2026-07-22 |

---

# 개요

웹 사이트에서 로그인, 회원가입, 게시글 작성, 댓글 등록과 같은 기능은 모두 폼(Form)을 이용하여 데이터를 입력받는다.

JavaScript는 사용자가 입력한 데이터를 읽고 검사하며, 필요한 경우 서버로 전송하기 전에 오류를 확인하거나 제출을 막을 수 있다.

이번 문서에서는 `<form>` 요소의 동작 방식과 `submit` 이벤트, 입력값 검증, `focus`, `blur`, `reset` 등을 학습한다.

---

# 핵심 개념

폼(Form)은 사용자로부터 데이터를 입력받기 위한 HTML 요소이다.

대표적으로 다음 요소들이 함께 사용된다.

- form
- input
- textarea
- select
- button

JavaScript는 이러한 입력 요소의 값을 읽고 검증한 후 적절한 동작을 수행한다.

---

# 폼 처리 흐름

```text
사용자 입력
        ↓
submit 이벤트 발생
        ↓
입력값 검사
        ↓
오류 확인
        ↓
정상 처리 또는 제출
```

---

# 기본 문법

폼 제출 이벤트는 `submit` 이벤트를 사용한다.

```javascript
form.addEventListener(
    "submit",
    function(event){

        event.preventDefault();

    }
);
```

대부분의 경우 `preventDefault()`와 함께 사용한다.

---

# 주요 개념

# form 요소

폼은 여러 입력 요소를 하나의 단위로 묶는다.

```html
<form id="loginForm">

<input
    type="text"
    id="userId"
>

<input
    type="password"
    id="userPw"
>

<button>

로그인

</button>

</form>
```

---

# submit 이벤트

사용자가 제출 버튼을 누르면 발생한다.

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
            "폼 제출"
        );

    }
);
```

---

# 왜 preventDefault()를 사용할까?

폼은 기본적으로 제출과 동시에 페이지를 새로고침한다.

하지만 JavaScript에서 입력값을 검사한 뒤에 제출해야 하는 경우가 많다.

따라서 대부분의 실무 프로젝트에서는 먼저 제출을 막은 후 검증을 수행한다.

---

# value 다시 살펴보기

폼에서는 `value`를 가장 많이 사용한다.

```javascript
console.log(
    userId.value
);
```

입력된 문자열을 가져온다.

---

# 빈 값 검사

```javascript
if (
    userId.value === ""
){

    console.log(
        "아이디를 입력하세요."
    );

}
```

로그인, 회원가입, 검색 기능에서 매우 자주 사용되는 패턴이다.

---

# trim()

사용자가 공백만 입력하는 경우를 방지하기 위해 `trim()`을 사용할 수 있다.

```javascript
if(
    userId.value.trim() === ""
){

    console.log(
        "아이디를 입력하세요."
    );

}
```

`trim()`은 문자열의 앞뒤 공백을 제거한다.

> **실무 팁**  
> 단순히 `value === ""`만 검사하면 `"   "`처럼 공백만 입력한 경우를 걸러내지 못한다. 실무에서는 `trim()`과 함께 사용하는 경우가 많다.

---

# focus()

`focus()`는 특정 입력 요소에 커서를 이동시킨다.

```javascript
userId.focus();
```

입력이 필요한 위치를 사용자에게 바로 안내할 수 있다.

---

# focus() 예제

```javascript
if(
    userId.value.trim() === ""
){

    userId.focus();

}
```

아이디 입력창으로 커서가 이동한다.

---

# blur()

`blur`는 입력 요소에서 커서가 빠져나갈 때 발생하는 이벤트이다.

```javascript
userId.addEventListener(
    "blur",
    function(){

        console.log(
            "입력 종료"
        );

    }
);
```

---

# focus와 blur

| 이벤트 | 의미 |
|---------|------|
| focus | 입력 시작 |
| blur | 입력 종료 |

---

# reset()

폼을 초기 상태로 되돌린다.

```javascript
loginForm.reset();
```

모든 입력값이 초기화된다.

---

---

# 입력값 검증(Validation)

폼을 제출하기 전에 입력값이 올바른지 확인하는 과정을 **유효성 검사(Validation)**라고 한다.

대표적으로 다음과 같은 검사를 수행한다.

- 필수 입력 여부
- 비밀번호 길이
- 비밀번호 확인
- 이메일 형식
- 체크박스 선택 여부

실무에서는 서버에 데이터를 전송하기 전에 반드시 유효성 검사를 수행한다.

---

# 필수 입력 검사

## HTML

```html
<input
    type="text"
    id="userName"
    placeholder="이름"
>

<button id="join">
가입
</button>

<p id="result"></p>
```

---

## JavaScript

```javascript
const userName =
    document.querySelector(
        "#userName"
    );

const join =
    document.querySelector(
        "#join"
    );

const result =
    document.querySelector(
        "#result"
    );

join.addEventListener(
    "click",
    function(){

        if(
            userName.value.trim() === ""
        ){

            result.innerText =
                "이름을 입력해주세요.";

            userName.focus();

            return;

        }

        result.innerText =
            "입력이 완료되었습니다.";

    }
);
```

---

# 비밀번호 길이 검사

비밀번호는 일정 길이 이상 입력하도록 제한하는 경우가 많다.

```javascript
if(
    password.value.length < 8
){

    result.innerText =
        "비밀번호는 8자 이상 입력하세요.";

    password.focus();

    return;

}
```

`length`를 사용하면 문자열의 길이를 확인할 수 있다.

---

# 비밀번호 확인

회원가입에서는 비밀번호를 두 번 입력받는 경우가 많다.

## HTML

```html
<input
    type="password"
    id="pw"
>

<input
    type="password"
    id="pwCheck"
>
```

---

## JavaScript

```javascript
if(
    pw.value !==
    pwCheck.value
){

    result.innerText =
        "비밀번호가 일치하지 않습니다.";

    pwCheck.focus();

    return;

}
```

---

# 체크박스 검사

약관 동의 여부를 확인하는 예제이다.

```html
<label>

<input
    type="checkbox"
    id="agree"
>

약관 동의

</label>
```

```javascript
if(
    !agree.checked
){

    result.innerText =
        "약관에 동의해주세요.";

    return;

}
```

---

# focus() 활용

입력이 필요한 위치로 커서를 이동시킬 수 있다.

```javascript
email.focus();
```

사용자는 어떤 항목을 수정해야 하는지 바로 알 수 있다.

---

# blur 이벤트 활용

입력을 마친 뒤 간단한 검사를 수행할 수도 있다.

```javascript
email.addEventListener(
    "blur",
    function(){

        if(
            email.value.trim() === ""
        ){

            console.log(
                "이메일을 입력하세요."
            );

        }

    }
);
```

실무에서는 입력이 끝난 시점에 오류 메시지를 보여주는 경우가 많다.

---

# reset() 활용

폼을 처음 상태로 되돌린다.

```javascript
joinForm.reset();
```

회원가입 취소 버튼이나 초기화 버튼에서 자주 사용한다.

---

# 회원가입 예제

## HTML

```html
<form id="joinForm">

<input
    id="name"
    placeholder="이름"
>

<input
    id="email"
    placeholder="이메일"
>

<button>

가입하기

</button>

</form>

<p id="result"></p>
```

---

## JavaScript

```javascript
const joinForm =
    document.querySelector(
        "#joinForm"
    );

const name =
    document.querySelector(
        "#name"
    );

const email =
    document.querySelector(
        "#email"
    );

const result =
    document.querySelector(
        "#result"
    );

joinForm.addEventListener(
    "submit",
    function(event){

        event.preventDefault();

        if(
            name.value.trim() === ""
        ){

            result.innerText =
                "이름을 입력하세요.";

            name.focus();

            return;

        }

        if(
            email.value.trim() === ""
        ){

            result.innerText =
                "이메일을 입력하세요.";

            email.focus();

            return;

        }

        result.innerText =
            "회원가입 완료";

    }
);
```

---

# 입력값 검사 순서

실무에서는 보통 다음 순서대로 검사한다.

```text
1. 공백 여부 확인
        ↓
2. 길이 확인
        ↓
3. 형식 확인
        ↓
4. 비밀번호 확인
        ↓
5. 체크박스 확인
        ↓
6. 서버 전송
```

---

# 실무 활용

폼 검증은 거의 모든 웹 서비스에서 사용된다.

대표적인 예는 다음과 같다.

- 로그인
- 회원가입
- 게시글 작성
- 댓글 작성
- 검색 기능
- 주문하기
- 결제하기
- 문의하기

입력값을 검증하지 않으면 잘못된 데이터가 서버로 전송될 수 있다.

---

# 폼 처리 디버깅

문제가 발생하면 다음 사항을 확인한다.

```text
1. submit 이벤트가 등록되었는가?
2. preventDefault()를 호출했는가?
3. value를 사용하여 입력값을 읽고 있는가?
4. trim()으로 공백을 제거했는가?
5. focus()가 올바른 요소를 가리키는가?
6. console.log()로 값을 확인했는가?
```

---

---

# 실무 활용

폼 처리는 대부분의 웹 서비스에서 가장 중요한 기능 중 하나이다.

회원가입, 로그인뿐 아니라 게시글 작성, 댓글 등록, 상품 주문, 예약, 문의하기 등 거의 모든 사용자 입력 화면에서 사용된다.

실무에서는 다음과 같은 순서로 처리하는 경우가 많다.

```text
사용자 입력
        ↓
공백 검사
        ↓
형식 검사
        ↓
비밀번호 확인
        ↓
약관 동의 확인
        ↓
서버 전송
```

---

# 실무 예제 프로젝트

이번 예제에서는 회원가입 폼의 기본적인 유효성 검사를 구현한다.

## HTML

```html
<form id="joinForm">

<input
    type="text"
    id="userName"
    placeholder="이름"
>

<input
    type="password"
    id="password"
    placeholder="비밀번호"
>

<input
    type="password"
    id="passwordCheck"
    placeholder="비밀번호 확인"
>

<label>

<input
    type="checkbox"
    id="agree"
>

약관 동의

</label>

<button>

회원가입

</button>

</form>

<p id="result"></p>
```

---

## JavaScript

```javascript
const joinForm =
    document.querySelector(
        "#joinForm"
    );

const userName =
    document.querySelector(
        "#userName"
    );

const password =
    document.querySelector(
        "#password"
    );

const passwordCheck =
    document.querySelector(
        "#passwordCheck"
    );

const agree =
    document.querySelector(
        "#agree"
    );

const result =
    document.querySelector(
        "#result"
    );

joinForm.addEventListener(
    "submit",
    function(event){

        event.preventDefault();

        if(
            userName.value.trim() === ""
        ){

            result.innerText =
                "이름을 입력하세요.";

            userName.focus();

            return;

        }

        if(
            password.value.length < 8
        ){

            result.innerText =
                "비밀번호는 8자 이상 입력하세요.";

            password.focus();

            return;

        }

        if(
            password.value !==
            passwordCheck.value
        ){

            result.innerText =
                "비밀번호가 일치하지 않습니다.";

            passwordCheck.focus();

            return;

        }

        if(
            !agree.checked
        ){

            result.innerText =
                "약관에 동의해주세요.";

            return;

        }

        result.innerText =
            "회원가입 완료";

    }
);
```

---

# 예제 코드 흐름

```text
폼 제출
      ↓
submit 이벤트 발생
      ↓
preventDefault()
      ↓
이름 검사
      ↓
비밀번호 길이 검사
      ↓
비밀번호 확인
      ↓
약관 동의 확인
      ↓
회원가입 완료
```

---

# 오류 분석

## 오류 1

```javascript
if(
    userName.value === ""
)
```

공백만 입력한 경우를 검사하지 못한다.

올바른 코드

```javascript
if(
    userName.value.trim() === ""
)
```

---

## 오류 2

```javascript
joinForm.submit();
```

직접 `submit()`을 호출하면 `submit` 이벤트 리스너가 실행되지 않는 상황이 발생할 수 있다.

사용자의 제출 동작을 기준으로 처리하거나, 필요한 경우 이벤트 흐름을 고려하여 사용해야 한다.

---

## 오류 3

```javascript
password.value =
passwordCheck.value
```

`=`는 값을 대입하는 연산자이다.

비교할 때는

```javascript
password.value ===
passwordCheck.value
```

를 사용해야 한다.

---

## 오류 4

```javascript
agree.value
```

체크 여부를 확인하려면 `value`가 아니라 `checked`를 사용해야 한다.

```javascript
agree.checked
```

---

# 폼 처리 디버깅 체크리스트

```text
1. submit 이벤트가 등록되었는가?
2. preventDefault()를 호출했는가?
3. value로 입력값을 가져왔는가?
4. trim()으로 공백을 제거했는가?
5. focus()를 올바른 위치에서 호출했는가?
6. checked를 사용하여 체크박스를 검사했는가?
7. console.log()로 입력값을 확인했는가?
```

---

# 이번 문서에서 새롭게 배운 내용

- form 요소의 역할
- submit 이벤트
- preventDefault()를 이용한 제출 제어
- value를 이용한 입력값 읽기
- trim()을 이용한 공백 제거
- focus()
- blur 이벤트
- reset()
- 입력값 유효성 검사(Validation)
- 비밀번호 확인
- 체크박스 검사

---

# 자주 하는 실수

- submit 이벤트 대신 click 이벤트만 사용하는 경우
- preventDefault()를 호출하지 않는 경우
- 공백 입력을 검사하지 않는 경우
- `=`와 `===`를 혼동하는 경우
- `checked` 대신 `value`를 사용하는 경우
- 오류 발생 후 `return`을 작성하지 않아 다음 코드가 계속 실행되는 경우
- focus()를 호출할 요소를 잘못 선택하는 경우

---

# 면접 포인트

### Form이란 무엇인가?

사용자의 입력 데이터를 하나의 단위로 묶어 서버로 전송하기 위한 HTML 요소이다.

---

### submit 이벤트는 언제 발생하는가?

폼이 제출될 때 발생하는 이벤트이다.

---

### preventDefault()를 사용하는 이유는?

폼 제출이나 링크 이동과 같은 브라우저의 기본 동작을 막고, JavaScript에서 입력값을 검증한 뒤 원하는 시점에 처리하기 위해 사용한다.

---

### trim()은 왜 사용하는가?

문자열의 앞뒤 공백을 제거하여 공백만 입력한 경우도 빈 입력으로 처리하기 위해 사용한다.

---

### focus()는 언제 사용하는가?

입력이 필요한 요소로 커서를 이동시켜 사용자에게 수정해야 할 위치를 안내할 때 사용한다.

---

### checked는 무엇인가?

체크박스나 라디오 버튼이 선택되었는지를 나타내는 Boolean 프로퍼티이다.

---

# 핵심 정리

- 폼은 사용자 입력을 처리하는 가장 기본적인 HTML 요소이다.
- `submit` 이벤트는 폼 제출 시 발생한다.
- `preventDefault()`를 이용하여 기본 제출을 제어할 수 있다.
- `value`를 이용하여 입력값을 읽는다.
- `trim()`을 사용하면 공백만 입력한 경우도 검사할 수 있다.
- `focus()`는 입력이 필요한 요소로 커서를 이동시킨다.
- `checked`는 체크박스와 라디오 버튼의 선택 여부를 확인할 때 사용한다.
- 폼 검증은 서버 전송 전에 반드시 수행하는 것이 일반적이다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|-----------|
| v1.0 | 2026-07-22 | 최초 작성 |
