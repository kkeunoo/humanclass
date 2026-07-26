---
title: JavaScript 조건문
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript 조건문

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript 조건문 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | JavaScript 소개와 실행환경, 변수와 자료형, 연산자 |
| 핵심 주제 | if, else, else if, switch, break, 조건식 작성 |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

조건문(Conditional Statement)은 **조건의 결과에 따라 서로 다른 코드를 실행하는 문법**이다.

예를 들어 다음과 같은 상황에서 사용된다.

- 로그인 여부 확인
- 성인/미성년자 구분
- 관리자 권한 확인
- 입력값 검증
- 메뉴 선택
- 점수에 따른 등급 계산

실무에서는 거의 모든 프로젝트에서 조건문을 사용한다고 해도 과언이 아니다.

---

# 조건문이 필요한 이유

조건문이 없다면 모든 코드가 순서대로 실행된다.

예를 들어,

```javascript
console.log("로그인 확인");

console.log("관리자 페이지");
```

로그인을 하지 않았더라도 관리자 페이지 코드가 실행된다.

하지만 조건문을 사용하면 필요한 경우에만 코드를 실행할 수 있다.

```javascript
const isLogin = true;

if (isLogin) {

    console.log("관리자 페이지");

}
```

---

# if 문

가장 기본적인 조건문이다.

조건이 `true`이면 블록 내부의 코드가 실행된다.

기본 문법

```javascript
if (조건식) {

    실행할 코드

}
```

---

## 예제 1

```javascript
const age = 20;

if (age >= 19) {

    console.log("성인입니다.");

}
```

결과

```text
성인입니다.
```

조건이 참이므로 실행된다.

---

## 예제 2

```javascript
const age = 15;

if (age >= 19) {

    console.log("성인입니다.");

}
```

결과

```text
(출력 없음)
```

조건이 거짓이므로 실행되지 않는다.

---

# 조건식

`if` 안에는 **참(`true`) 또는 거짓(`false`)으로 평가되는 식**이 들어간다.

예를 들어

```javascript
age >= 20
```

```javascript
score === 100
```

```javascript
isLogin
```

모두 조건식이 될 수 있다.

---

# Boolean 변수 활용

Boolean 값을 저장한 변수는 그대로 조건식으로 사용할 수 있다.

```javascript
const isLogin = true;

if (isLogin) {

    console.log("로그인 성공");

}
```

굳이 다음과 같이 작성할 필요는 없다.

```javascript
if (isLogin === true) {

}
```

위 코드보다

```javascript
if (isLogin) {

}
```

처럼 작성하는 것이 더 간결하고 실무에서도 많이 사용된다.

---

# else

조건이 거짓일 때 실행되는 부분이다.

기본 문법

```javascript
if (조건식) {

    실행

} else {

    실행

}
```

---

## 예제

```javascript
const age = 17;

if (age >= 19) {

    console.log("성인");

} else {

    console.log("미성년자");

}
```

결과

```text
미성년자
```

---

# else if

여러 개의 조건을 순차적으로 검사할 때 사용한다.

기본 문법

```javascript
if (조건1) {

} else if (조건2) {

} else if (조건3) {

} else {

}
```

---

## 예제

```javascript
const score = 85;

if (score >= 90) {

    console.log("A");

} else if (score >= 80) {

    console.log("B");

} else if (score >= 70) {

    console.log("C");

} else {

    console.log("F");

}
```

결과

```text
B
```

---

# 조건문의 실행 순서

조건문은 **위에서 아래로 순서대로 검사**한다.

```javascript
const score = 95;

if (score >= 60) {

    console.log("합격");

} else if (score >= 90) {

    console.log("A");

}
```

결과

```text
합격
```

`95`는 `90` 이상이지만, 첫 번째 조건(`60 이상`)이 먼저 만족되었기 때문에 이후 조건은 검사하지 않는다.

따라서 **더 구체적인 조건을 먼저 작성해야 한다.**

올바른 예

```javascript
if (score >= 90) {

    console.log("A");

} else if (score >= 60) {

    console.log("합격");

}
```

---

# 여러 조건 함께 사용하기

논리 연산자를 함께 사용하면 여러 조건을 조합할 수 있다.

```javascript
const age = 22;

const isMember = true;

if (age >= 20 && isMember) {

    console.log("입장 가능");

}
```

`&&`는 모든 조건이 참이어야 실행된다.

---

---

# 중첩 조건문 (Nested if)

조건문 안에 또 다른 조건문을 작성하는 것을 **중첩 조건문(Nested if)** 이라고 한다.

필요한 경우에 사용할 수 있지만, 중첩이 깊어질수록 가독성이 떨어질 수 있다.

기본 문법

```javascript
if (조건1) {

    if (조건2) {

        실행할 코드;

    }

}
```

---

## 예제

```javascript
const isLogin = true;
const isAdmin = true;

if (isLogin) {

    if (isAdmin) {

        console.log("관리자 페이지");

    }

}
```

결과

```text
관리자 페이지
```

로그인되어 있고, 관리자일 때만 실행된다.

---

## 논리 연산자로 변경

위 코드는 다음과 같이 작성하는 것이 더 간결하다.

```javascript
if (isLogin && isAdmin) {

    console.log("관리자 페이지");

}
```

실무에서는 불필요한 중첩을 줄이기 위해 `&&`를 적극적으로 활용한다.

---

# switch 문

여러 개의 값 중 하나를 선택하여 실행할 때 사용하는 조건문이다.

주로 **하나의 변수 값을 여러 경우(case)와 비교**할 때 사용한다.

기본 문법

```javascript
switch (값) {

    case 값1:

        실행;

        break;

    case 값2:

        실행;

        break;

    default:

        실행;

}
```

---

# switch 실행 과정

예를 들어

```javascript
const menu = 2;
```

이라면

```javascript
switch (menu) {

    case 1:

        console.log("피자");

        break;

    case 2:

        console.log("햄버거");

        break;

    case 3:

        console.log("파스타");

        break;

}
```

결과

```text
햄버거
```

`menu`의 값과 같은 `case`를 찾아 실행한다.

---

# break

`break`는 현재 `case`의 실행을 종료한다.

```javascript
switch (2) {

    case 1:

        console.log("A");

        break;

    case 2:

        console.log("B");

        break;

    case 3:

        console.log("C");

        break;

}
```

결과

```text
B
```

---

# break를 생략하면?

```javascript
switch (2) {

    case 1:

        console.log("A");

    case 2:

        console.log("B");

    case 3:

        console.log("C");

}
```

결과

```text
B

C
```

`case 2`부터 아래의 모든 코드가 계속 실행된다.

이러한 동작을 **Fall-through(폴스루)** 라고 한다.

---

# Fall-through

일반적으로는 실수의 원인이 되므로 `break`를 사용하는 것이 좋다.

하지만 여러 `case`를 하나로 묶고 싶을 때는 의도적으로 사용할 수도 있다.

```javascript
const month = 1;

switch (month) {

    case 12:
    case 1:
    case 2:

        console.log("겨울");

        break;

}
```

결과

```text
겨울
```

12월, 1월, 2월 모두 같은 코드를 실행한다.

---

# default

어떤 `case`와도 일치하지 않을 경우 실행된다.

```javascript
const menu = 5;

switch (menu) {

    case 1:

        console.log("피자");

        break;

    case 2:

        console.log("햄버거");

        break;

    default:

        console.log("없는 메뉴");

}
```

결과

```text
없는 메뉴
```

`default`는 `else`와 비슷한 역할을 한다.

---

# if와 switch의 차이

두 조건문은 비슷하지만 사용하는 목적이 다르다.

| if | switch |
|----|---------|
| 조건식을 비교 | 하나의 값을 비교 |
| 범위 비교 가능 | 같은 값 비교에 적합 |
| `>`, `<`, `>=` 사용 가능 | `case` 값과 비교 |
| 실무에서 가장 많이 사용 | 메뉴, 상태값 등에 사용 |

---

## if가 적합한 경우

```javascript
const score = 85;

if (score >= 90) {

    console.log("A");

} else if (score >= 80) {

    console.log("B");

}
```

범위를 비교해야 하므로 `if`가 적합하다.

---

## switch가 적합한 경우

```javascript
const color = "red";

switch (color) {

    case "red":

        console.log("빨강");

        break;

    case "blue":

        console.log("파랑");

        break;

    default:

        console.log("기타");

}
```

하나의 값과 여러 경우를 비교하므로 `switch`가 적합하다.

---

# switch의 비교 방식

`switch`는 내부적으로 **엄격한 비교(`===`)** 를 사용한다.

```javascript
const num = 10;

switch (num) {

    case "10":

        console.log("문자열");

        break;

    case 10:

        console.log("숫자");

        break;

}
```

결과

```text
숫자
```

문자열 `"10"`과 숫자 `10`은 다른 값으로 취급된다.

---

---

# 조건문 작성 원칙

조건문은 단순히 동작만 하는 것이 아니라 **읽기 쉽고 유지보수하기 쉬운 코드**를 작성하는 것이 중요하다.

실무에서는 다음과 같은 원칙을 자주 사용한다.

- 조건을 명확하게 작성한다.
- 중첩을 최소화한다.
- 의미 있는 변수명을 사용한다.
- 복잡한 조건은 변수로 분리한다.

---

# 좋은 조건식 작성

다음과 같은 코드는 의미를 이해하기 어렵다.

```javascript
if (score >= 60 && score <= 100 && age >= 20 && isLogin) {

    console.log("통과");

}
```

조건을 변수로 분리하면 훨씬 읽기 쉽다.

```javascript
const isPassScore = score >= 60;
const isAdult = age >= 20;

if (isPassScore && isAdult && isLogin) {

    console.log("통과");

}
```

---

# 중첩을 줄이는 방법

다음과 같이 중첩된 조건문은 읽기 어렵다.

```javascript
if (isLogin) {

    if (isAdmin) {

        console.log("관리자");

    }

}
```

논리 연산자를 사용하면 더 간결하게 작성할 수 있다.

```javascript
if (isLogin && isAdmin) {

    console.log("관리자");

}
```

---

# Guard Clause

Guard Clause는 **조건을 먼저 검사하여 함수나 코드의 실행을 빠르게 종료하는 방식**이다.

중첩을 줄이고 가독성을 높이는 데 자주 사용된다.

예를 들어,

```javascript
function printUser(isLogin) {

    if (!isLogin) {

        console.log("로그인이 필요합니다.");
        return;

    }

    console.log("회원 정보");

}
```

로그인하지 않은 경우 바로 함수를 종료한다.

---

## Guard Clause의 장점

- 중첩을 줄일 수 있다.
- 코드의 흐름이 명확해진다.
- 유지보수가 쉬워진다.

실무 프로젝트에서 매우 자주 사용하는 작성 방식이다.

> **참고**
>
> `return`과 함수(Function)는 이후 문서에서 자세히 학습한다.
> 현재는 "조건이 맞지 않으면 실행을 종료할 수 있다." 정도로 이해하면 충분하다.

---

# 삼항 연산자와 if문의 선택

간단한 조건은 삼항 연산자가 적합하다.

```javascript
const result =
    score >= 60
        ? "합격"
        : "불합격";
```

---

여러 줄의 처리가 필요한 경우에는 `if`문이 더 적합하다.

```javascript
if (score >= 60) {

    console.log("합격");
    console.log("축하합니다.");

} else {

    console.log("불합격");

}
```

---

# 언제 switch를 사용할까?

다음처럼 **하나의 값을 여러 경우와 비교**할 때 적합하다.

```javascript
switch (grade) {

    case "A":

        console.log("매우 우수");

        break;

    case "B":

        console.log("우수");

        break;

    default:

        console.log("재시험");

}
```

---

반대로 범위를 비교해야 한다면 `if`를 사용하는 것이 적합하다.

```javascript
if (score >= 90) {

    console.log("A");

} else if (score >= 80) {

    console.log("B");

}
```

---

# 실무에서 자주 사용하는 조건문 패턴

## 로그인 여부 확인

```javascript
if (!isLogin) {

    alert("로그인이 필요합니다.");

}
```

---

## 입력값 확인

```javascript
if (userName === "") {

    alert("이름을 입력하세요.");

}
```

---

## 관리자 권한 확인

```javascript
if (user.role === "admin") {

    console.log("관리자 메뉴");

}
```

---

## 여러 조건 확인

```javascript
if (isLogin && isMember) {

    console.log("서비스 이용 가능");

}
```

---

## 메뉴 선택

```javascript
switch (menu) {

    case "pizza":

        console.log("피자 주문");

        break;

    case "burger":

        console.log("햄버거 주문");

        break;

    default:

        console.log("메뉴 선택");

}
```

---

# 조건문 작성 시 체크리스트

조건문을 작성한 후 다음 항목을 확인하면 실수를 줄일 수 있다.

- `===`를 사용했는가?
- 불필요한 중첩은 없는가?
- 조건의 순서가 올바른가?
- `switch`에서 `break`를 빠뜨리지 않았는가?
- 복잡한 조건을 변수로 분리할 수 있는가?
- 간단한 조건이라면 삼항 연산자가 더 적합하지 않은가?

---

---

# 실무 예제 프로젝트

다음은 사용자의 로그인 여부와 권한을 확인하여 다른 메시지를 출력하는 예제이다.

## HTML

```html
<h2>회원 정보</h2>

<p id="result"></p>
```

---

## JavaScript

```javascript
const user = {
    name: "Kim",
    isLogin: true,
    role: "admin"
};

const result = document.querySelector("#result");

if (!user.isLogin) {

    result.textContent = "로그인이 필요합니다.";

} else if (user.role === "admin") {

    result.textContent = `${user.name}님은 관리자입니다.`;

} else {

    result.textContent = `${user.name}님 환영합니다.`;

}
```

---

## 학습한 내용

- if
- else
- else if
- 논리 연산자
- 비교 연산자
- Template Literal
- DOM 출력

---

# 실무 활용

## 1. 로그인 여부 확인

```javascript
if (!isLogin) {

    location.href = "/login";

}
```

로그인하지 않은 사용자를 로그인 페이지로 이동시킬 수 있다.

---

## 2. 입력값 검증

```javascript
if (userName === "") {

    alert("이름을 입력하세요.");

}
```

폼(Form) 검증에서 가장 많이 사용하는 형태이다.

---

## 3. 권한에 따른 화면 표시

```javascript
if (user.role === "admin") {

    console.log("관리자 메뉴");

} else {

    console.log("일반 사용자");

}
```

---

## 4. 메뉴 선택

```javascript
switch (menu) {

    case "pizza":

        console.log("피자");

        break;

    case "burger":

        console.log("햄버거");

        break;

    default:

        console.log("메뉴 없음");

}
```

---

## 5. 여러 조건 확인

```javascript
if (isLogin && isMember) {

    console.log("서비스 이용");

}
```

회원이면서 로그인한 사용자만 서비스를 이용할 수 있다.

---

# 이번 문서에서 새롭게 배운 내용

- `if` 문을 사용하여 조건에 따라 코드를 실행할 수 있다.
- `else`를 이용해 조건이 거짓일 때의 동작을 작성할 수 있다.
- `else if`로 여러 조건을 순차적으로 검사할 수 있다.
- 조건문의 순서는 결과에 큰 영향을 미친다.
- 중첩 조건문보다 논리 연산자를 활용하면 가독성이 좋아진다.
- `switch` 문은 하나의 값을 여러 경우와 비교할 때 적합하다.
- `break`를 생략하면 Fall-through가 발생한다.
- Guard Clause는 중첩을 줄이는 데 도움이 된다.
- 상황에 따라 `if`, `switch`, 삼항 연산자를 적절히 선택해야 한다.

---

# 자주 하는 실수

- `=`(대입)과 `===`(비교)를 혼동한다.
- 조건문의 순서를 잘못 작성한다.
- `switch`에서 `break`를 빠뜨린다.
- 불필요하게 조건문을 중첩한다.
- Boolean 값을 `=== true`와 비교하여 작성한다.
- 너무 복잡한 조건을 한 줄에 작성하여 가독성을 떨어뜨린다.
- 간단한 조건도 모두 `if`로 작성하거나, 반대로 복잡한 조건을 무리하게 삼항 연산자로 작성한다.

---

# 면접 포인트

### `if`와 `switch`의 차이는 무엇인가?

- `if`는 범위 비교나 복합 조건을 처리하기 적합하다.
- `switch`는 하나의 값을 여러 경우와 비교할 때 적합하다.

---

### `switch`에서 `break`가 필요한 이유는?

`break`가 없으면 다음 `case`까지 계속 실행되는 Fall-through가 발생하기 때문이다.

---

### Guard Clause란?

조건을 먼저 검사하여 더 이상 실행할 필요가 없는 경우 빠르게 종료하는 작성 방식이다.

중첩을 줄이고 코드의 가독성을 높이는 데 도움이 된다.

---

### 중첩 조건문은 항상 나쁜가?

아니다.

필요한 경우 사용할 수 있지만, 과도한 중첩은 가독성을 떨어뜨리므로 논리 연산자나 Guard Clause를 활용하여 줄이는 것이 좋다.

---

### 조건문의 순서가 중요한 이유는?

조건문은 위에서부터 순서대로 검사하고, 처음으로 만족하는 조건만 실행하기 때문이다.

더 구체적인 조건을 먼저 작성하는 것이 일반적이다.

---

# 핵심 정리

- `if`는 가장 기본적인 조건문이다.
- `else`, `else if`를 이용해 다양한 분기를 만들 수 있다.
- 조건문의 순서는 매우 중요하다.
- `switch`는 하나의 값을 여러 경우와 비교할 때 적합하다.
- `break`를 생략하면 Fall-through가 발생한다.
- 논리 연산자를 활용하면 중첩을 줄일 수 있다.
- Guard Clause는 코드의 흐름을 단순하게 만드는 데 유용하다.
- 상황에 맞는 조건문을 선택하는 것이 좋은 코드 작성의 시작이다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
