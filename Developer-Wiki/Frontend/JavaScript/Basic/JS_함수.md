---
title: JavaScript 함수
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript 함수

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript 함수 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | JavaScript 소개와 실행환경, 변수와 자료형, 연산자, 조건문, 반복문 |
| 핵심 주제 | 함수 선언, 함수 호출, 매개변수, 전달인자, 반환값 |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

함수(Function)는 **특정 작업을 하나로 묶어 필요할 때마다 실행할 수 있는 코드의 집합**이다.

같은 코드를 여러 번 작성하는 대신 함수로 만들어 두면 필요한 곳에서 여러 번 호출하여 사용할 수 있다.

함수를 사용하면

- 코드의 재사용성이 높아진다.
- 유지보수가 쉬워진다.
- 가독성이 좋아진다.
- 프로그램을 기능별로 나눌 수 있다.

JavaScript뿐만 아니라 대부분의 프로그래밍 언어에서 함수는 매우 중요한 개념이다.

---

# 함수가 필요한 이유

다음과 같이 같은 코드를 여러 번 작성한다고 가정해 보자.

```javascript
console.log("안녕하세요.");
console.log("좋은 하루입니다.");

console.log("안녕하세요.");
console.log("좋은 하루입니다.");

console.log("안녕하세요.");
console.log("좋은 하루입니다.");
```

같은 코드가 반복되어 수정해야 할 부분이 생기면 모든 위치를 직접 변경해야 한다.

함수를 사용하면 다음과 같이 작성할 수 있다.

```javascript
function greeting() {

    console.log("안녕하세요.");
    console.log("좋은 하루입니다.");

}

greeting();
greeting();
greeting();
```

하나의 함수만 수정하면 모든 호출 결과가 함께 변경되므로 유지보수가 쉬워진다.

---

# 함수(Function)란?

함수는 **특정 기능을 수행하는 코드의 묶음**이다.

예를 들어 다음과 같은 기능들을 함수로 만들 수 있다.

- 회원 로그인
- 상품 목록 출력
- 주문 금액 계산
- 회원가입 검사
- 이메일 형식 확인
- 인사말 출력

실무 프로젝트에서는 대부분의 기능을 함수 단위로 작성한다.

---

# 함수 선언(Function Declaration)

함수를 만드는 것을 **함수 선언**이라고 한다.

기본 문법

```javascript
function 함수이름() {

    실행할 코드

}
```

---

# 함수 호출(Function Call)

선언한 함수는 이름만 작성해서 실행되지 않는다.

함수를 실행하려면 **호출(Call)** 해야 한다.

```javascript
function hello() {

    console.log("Hello JavaScript!");

}

hello();
```

결과

```text
Hello JavaScript!
```

---

# 실행 순서

다음 코드를 살펴보자.

```javascript
function hello() {

    console.log("Hello");

}

hello();

console.log("End");
```

실행 순서

```text
① 함수 선언

↓

② hello() 호출

↓

③ 함수 내부 실행

↓

④ console.log("End")
```

함수는 선언만으로 실행되지 않으며, 호출하는 순간 실행된다.

---

# 여러 번 호출하기

하나의 함수는 원하는 만큼 여러 번 호출할 수 있다.

```javascript
function printLine() {

    console.log("----------------");

}

printLine();
printLine();
printLine();
```

결과

```text
----------------
----------------
----------------
```

이처럼 반복되는 작업을 함수로 만들면 코드가 훨씬 간결해진다.

---

# 함수 이름 작성 규칙

함수 이름은 **동작을 알 수 있도록 작성하는 것이 좋다.**

좋은 예

```javascript
showMessage()
calculatePrice()
printUser()
openModal()
```

좋지 않은 예

```javascript
aaa()
test()
function1()
abc()
```

함수 이름만 보고도 어떤 기능을 하는지 이해할 수 있도록 작성하는 것이 실무에서 권장되는 방식이다.

---

# 함수 선언과 호출의 관계

```javascript
function welcome() {

    console.log("환영합니다.");

}

welcome();
```

위 코드에서

- `function welcome()` → 함수를 선언
- `welcome()` → 함수를 호출

같은 이름이지만 역할은 서로 다르다.

---

---

# 매개변수(Parameter)

함수는 필요한 데이터를 외부로부터 전달받아 사용할 수 있다.

이때 함수를 선언할 때 작성하는 변수를 **매개변수(Parameter)** 라고 한다.

기본 문법

```javascript
function 함수이름(매개변수) {

    실행할 코드

}
```

---

# 전달인자(Argument)

함수를 호출하면서 전달하는 실제 값을 **전달인자(Argument)** 라고 한다.

```javascript
function hello(name) {

    console.log(`${name}님 환영합니다.`);

}

hello("Kim");
```

위 코드에서

- `name` → 매개변수(Parameter)
- `"Kim"` → 전달인자(Argument)

결과

```text
Kim님 환영합니다.
```

---

# 실행 과정

다음 코드를 살펴보자.

```javascript
function printNumber(num) {

    console.log(num);

}

printNumber(10);
```

실행 순서

```text
① 함수 선언

↓

② printNumber(10) 호출

↓

③ 10이 num에 저장

↓

④ console.log(num)
```

---

# 여러 개의 매개변수

매개변수는 여러 개 사용할 수 있다.

```javascript
function introduce(name, age) {

    console.log(`${name}님의 나이는 ${age}살입니다.`);

}

introduce("Kim", 20);
```

결과

```text
Kim님의 나이는 20살입니다.
```

매개변수의 순서와 전달인자의 순서는 반드시 일치해야 한다.

---

# 전달인자의 개수가 다른 경우

## 전달인자가 부족한 경우

```javascript
function introduce(name, age) {

    console.log(name);
    console.log(age);

}

introduce("Kim");
```

결과

```text
Kim
undefined
```

전달되지 않은 매개변수는 `undefined`가 된다.

---

## 전달인자가 많은 경우

```javascript
function hello(name) {

    console.log(name);

}

hello("Kim", 20, "Seoul");
```

결과

```text
Kim
```

필요한 개수보다 많이 전달된 값은 사용하지 않는다.

> **참고**
>
> 이후 함수 심화 문서에서 `arguments` 객체와 나머지 매개변수(Rest Parameter)를 배우면 전달인자를 더 유연하게 처리할 수 있다.

---

# 기본값(Default Value)

매개변수에 기본값을 지정할 수도 있다.

```javascript
function hello(name = "Guest") {

    console.log(`${name}님 환영합니다.`);

}

hello();
hello("Kim");
```

결과

```text
Guest님 환영합니다.
Kim님 환영합니다.
```

전달인자가 없을 경우 기본값이 사용된다.

> **참고**
>
> 기본값(Default Value)은 ES6에서 추가된 문법이다.
> 교육 과정에서 아직 다루지 않았다면 이 기능은 참고만 하고 넘어가도 된다.

---

# 반환값(Return)

함수는 실행 결과를 호출한 곳으로 돌려줄 수 있다.

이때 사용하는 키워드가 `return`이다.

기본 문법

```javascript
function 함수이름() {

    return 반환값;

}
```

---

# return 사용 예제

```javascript
function add(a, b) {

    return a + b;

}

const result = add(10, 20);

console.log(result);
```

결과

```text
30
```

`return`은 계산 결과를 함수 밖으로 전달한다.

---

# return이 없는 함수

다음 함수는 값을 반환하지 않는다.

```javascript
function hello() {

    console.log("안녕하세요.");

}

const result = hello();

console.log(result);
```

결과

```text
안녕하세요.
undefined
```

`return`이 없으면 함수의 반환값은 `undefined`이다.

---

# return의 특징

`return`을 실행하면 함수는 즉시 종료된다.

```javascript
function test() {

    console.log("A");

    return;

    console.log("B");

}

test();
```

결과

```text
A
```

`return` 아래에 있는 코드는 실행되지 않는다.

---

# 조건문과 return

조건문과 함께 사용하면 특정 조건에서 함수를 종료할 수 있다.

```javascript
function printUser(isLogin) {

    if (!isLogin) {

        console.log("로그인이 필요합니다.");

        return;

    }

    console.log("회원 정보");

}

printUser(false);
```

결과

```text
로그인이 필요합니다.
```

이러한 작성 방식을 **Guard Clause**라고 하며, 중첩을 줄이고 코드의 흐름을 명확하게 만드는 데 자주 사용한다.

---

# 함수의 실행 흐름

```javascript
function multiply(a, b) {

    return a * b;

}

const result = multiply(3, 4);

console.log(result);
```

실행 순서

```text
① 함수 선언

↓

② multiply(3, 4) 호출

↓

③ a = 3, b = 4

↓

④ return 12

↓

⑤ result에 12 저장

↓

⑥ console.log(result)
```

---

---

# 함수의 재사용

함수의 가장 큰 장점은 **한 번 작성한 코드를 여러 곳에서 재사용할 수 있다는 것**이다.

예를 들어 인사말을 출력하는 함수를 작성하면 필요한 곳마다 호출하여 사용할 수 있다.

```javascript
function greeting() {

    console.log("안녕하세요.");

}

greeting();
greeting();
greeting();
```

같은 코드를 여러 번 작성하는 것보다 유지보수가 훨씬 쉽다.

---

# 함수를 사용하는 이유

함수를 사용하는 대표적인 이유는 다음과 같다.

- 같은 코드를 여러 번 작성하지 않아도 된다.
- 프로그램을 기능별로 나눌 수 있다.
- 유지보수가 쉬워진다.
- 코드의 가독성이 높아진다.
- 오류를 수정하기 쉽다.

실무에서는 대부분의 기능을 함수 단위로 작성한다.

---

# 지역 변수(Local Variable)

함수 안에서 선언한 변수는 **지역 변수(Local Variable)** 라고 한다.

지역 변수는 **해당 함수 내부에서만 사용할 수 있다.**

```javascript
function hello() {

    let message = "안녕하세요.";

    console.log(message);

}

hello();
```

결과

```text
안녕하세요.
```

---

함수 밖에서는 사용할 수 없다.

```javascript
function hello() {

    let message = "안녕하세요.";

}

console.log(message);
```

결과

```text
ReferenceError
```

`message`는 함수 내부에서만 존재하기 때문이다.

---

# 전역 변수(Global Variable)

함수 밖에서 선언한 변수는 **전역 변수(Global Variable)** 라고 한다.

```javascript
let message = "안녕하세요.";

function hello() {

    console.log(message);

}

hello();
```

결과

```text
안녕하세요.
```

전역 변수는 함수 내부에서도 사용할 수 있다.

---

# 지역 변수와 전역 변수 비교

| 구분 | 지역 변수 | 전역 변수 |
|------|----------|----------|
| 선언 위치 | 함수 내부 | 함수 외부 |
| 사용 범위 | 해당 함수 내부 | 프로그램 전체 |
| 생명 주기 | 함수 실행 중 | 프로그램 종료 전까지 |

실무에서는 **전역 변수의 사용을 최소화**하는 것이 권장된다.

---

# 변수의 유효 범위(Scope)

변수를 사용할 수 있는 범위를 **Scope(스코프)** 라고 한다.

```javascript
let a = 10;

function test() {

    let b = 20;

    console.log(a);
    console.log(b);

}

test();
```

결과

```text
10
20
```

---

반대로

```javascript
let a = 10;

function test() {

    let b = 20;

}

console.log(a);
console.log(b);
```

결과

```text
10
ReferenceError
```

`b`는 함수 내부에서만 사용할 수 있다.

---

# 함수 안에서 함수 호출

함수는 다른 함수를 호출할 수도 있다.

```javascript
function printLine() {

    console.log("----------------");

}

function printMenu() {

    printLine();

    console.log("메뉴");

    printLine();

}

printMenu();
```

결과

```text
----------------
메뉴
----------------
```

이처럼 기능을 작은 단위로 나누면 코드가 훨씬 읽기 쉬워진다.

---

# 함수를 나누는 기준

좋은 함수는 **하나의 기능만 수행**하도록 작성하는 것이 좋다.

좋은 예

```javascript
function login() {

}

function logout() {

}

function calculatePrice() {

}
```

각 함수가 하나의 역할만 담당한다.

---

좋지 않은 예

```javascript
function processAll() {

    // 로그인

    // 주문

    // 결제

    // 이메일 발송

    // 로그 저장

}
```

하나의 함수가 너무 많은 일을 하면 유지보수가 어려워진다.

---

# 함수 이름 작성 원칙

함수 이름은 **동사를 포함하여 기능을 명확하게 표현**하는 것이 좋다.

좋은 예

```javascript
getUser()

printMenu()

calculateTotal()

showModal()

saveData()
```

좋지 않은 예

```javascript
test()

aaa()

temp()

data()
```

이름만 보고도 어떤 기능인지 이해할 수 있도록 작성하는 것이 중요하다.

---

# 함수 작성 원칙

실무에서는 다음과 같은 원칙을 자주 사용한다.

- 하나의 함수는 하나의 기능만 담당한다.
- 함수 이름은 역할을 알 수 있도록 작성한다.
- 함수를 너무 길게 작성하지 않는다.
- 중복 코드는 함수로 분리한다.
- 필요한 값은 매개변수로 전달한다.
- 결과는 `return`으로 반환한다.

---

# 실무에서 자주 사용하는 함수 패턴

## 가격 계산

```javascript
function calculatePrice(price, count) {

    return price * count;

}

const total = calculatePrice(1000, 3);

console.log(total);
```

---

## 로그인 확인

```javascript
function checkLogin(isLogin) {

    if (!isLogin) {

        return;

    }

    console.log("로그인 완료");

}
```

---

## 인사말 출력

```javascript
function greeting(name) {

    console.log(`${name}님 환영합니다.`);

}

greeting("Kim");
```

---

# 함수 사용 시 주의사항

- 함수 이름은 기능을 알 수 있게 작성한다.
- 함수 하나에 너무 많은 기능을 넣지 않는다.
- 지역 변수와 전역 변수를 구분하여 사용한다.
- 중복되는 코드는 함수로 분리한다.
- `return` 이후의 코드는 실행되지 않는다는 점을 기억한다.

---

---

# 실무 예제 프로젝트

다음은 상품의 가격과 수량을 전달받아 총 금액을 계산하는 간단한 함수 예제이다.

## HTML

```html
<h2>주문 금액</h2>

<p id="result"></p>
```

---

## JavaScript

```javascript
function calculateTotal(price, quantity) {

    return price * quantity;

}

const total = calculateTotal(12000, 3);

const result = document.querySelector("#result");

result.textContent = `총 결제 금액 : ${total.toLocaleString()}원`;
```

> **참고**
>
> `toLocaleString()`은 숫자를 읽기 쉬운 형식(예: `36,000`)으로 표시하는 메서드이다.
> 메서드(Method)는 이후 문서에서 자세히 학습한다.

---

## 학습한 내용

- 함수 선언(Function Declaration)
- 함수 호출(Function Call)
- 매개변수(Parameter)
- 전달인자(Argument)
- 반환값(Return)
- 지역 변수(Local Variable)
- 전역 변수(Global Variable)
- Scope(유효 범위)

---

# 실무 활용

## 1. 주문 금액 계산

```javascript
function calculatePrice(price, count) {

    return price * count;

}

const total = calculatePrice(15000, 2);

console.log(total);
```

---

## 2. 로그인 여부 확인

```javascript
function checkLogin(isLogin) {

    if (!isLogin) {

        return;

    }

    console.log("로그인 성공");

}
```

Guard Clause를 이용해 불필요한 중첩을 줄일 수 있다.

---

## 3. 인사말 출력

```javascript
function greeting(name) {

    console.log(`${name}님 환영합니다.`);

}

greeting("Kim");
```

---

## 4. 할인 금액 계산

```javascript
function getDiscountPrice(price, discount) {

    return price - discount;

}

console.log(getDiscountPrice(20000, 3000));
```

---

## 5. 합계 계산

```javascript
function add(a, b) {

    return a + b;

}

console.log(add(10, 20));
```

---

# 이번 문서에서 새롭게 배운 내용

- 함수는 특정 기능을 하나로 묶은 코드의 집합이다.
- 함수는 선언과 호출을 통해 사용한다.
- 매개변수는 데이터를 전달받기 위한 변수이다.
- 전달인자는 함수를 호출할 때 전달하는 실제 값이다.
- `return`은 실행 결과를 호출한 곳으로 반환한다.
- `return`을 만나면 함수는 즉시 종료된다.
- 함수 내부에서 선언한 변수는 지역 변수이다.
- 함수 밖에서 선언한 변수는 전역 변수이다.
- 변수는 선언된 범위(Scope) 안에서만 사용할 수 있다.
- 하나의 함수는 하나의 역할만 담당하도록 작성하는 것이 좋다.

---

# 자주 하는 실수

- 함수를 선언만 하고 호출하지 않는다.
- 매개변수와 전달인자의 개념을 혼동한다.
- `return`과 `console.log()`를 같은 의미로 생각한다.
- `return` 이후에도 코드가 실행된다고 생각한다.
- 지역 변수를 함수 밖에서 사용하려고 한다.
- 하나의 함수에 너무 많은 기능을 작성한다.
- 함수 이름을 `test()`, `aaa()`처럼 의미 없이 작성한다.

---

# 면접 포인트

### 함수(Function)란 무엇인가?

특정 기능을 하나로 묶어 필요할 때마다 호출하여 사용할 수 있는 코드의 집합이다.

---

### 매개변수(Parameter)와 전달인자(Argument)의 차이는?

- **매개변수(Parameter)**: 함수를 선언할 때 작성하는 변수
- **전달인자(Argument)**: 함수를 호출할 때 전달하는 실제 값

---

### `return`의 역할은 무엇인가?

- 함수의 실행 결과를 반환한다.
- `return`을 실행하면 함수는 즉시 종료된다.

---

### 지역 변수와 전역 변수의 차이는?

- **지역 변수**는 함수 내부에서만 사용할 수 있다.
- **전역 변수**는 프로그램 전체에서 사용할 수 있다.

실무에서는 전역 변수 사용을 최소화하는 것이 권장된다.

---

### 좋은 함수의 조건은?

- 하나의 기능만 수행한다.
- 이름만 보고 역할을 알 수 있다.
- 중복 코드를 줄일 수 있다.
- 필요한 값은 매개변수로 전달하고, 결과는 `return`으로 반환한다.

---

# 핵심 정리

- 함수는 코드의 재사용성과 유지보수성을 높여 준다.
- 함수는 선언 후 호출해야 실행된다.
- 매개변수와 전달인자를 통해 데이터를 주고받는다.
- `return`은 값을 반환하고 함수를 종료한다.
- 지역 변수는 함수 내부에서만 사용할 수 있다.
- 전역 변수는 편리하지만 남용하지 않는 것이 좋다.
- 하나의 함수는 하나의 역할만 수행하도록 작성하는 것이 바람직하다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
