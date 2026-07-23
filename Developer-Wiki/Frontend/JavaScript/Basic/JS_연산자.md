---
title: JavaScript 연산자
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript 연산자

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript 연산자 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | JavaScript 소개와 실행환경, 변수와 자료형 |
| 핵심 주제 | 산술, 대입, 비교, 논리, 삼항, Null 병합, 옵셔널 체이닝 |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

연산자(Operator)는 **값이나 변수에 특정한 계산이나 비교를 수행하는 기호**이다.

JavaScript에서는 숫자 계산뿐 아니라 문자열 연결, 값 비교, 논리 판단 등 다양한 연산자를 제공한다.

연산자를 정확히 이해하면 조건문, 반복문, 함수, 객체 등 이후의 모든 문법을 훨씬 쉽게 이해할 수 있다.

---

# 연산자의 종류

JavaScript에서 자주 사용하는 연산자는 다음과 같다.

| 종류 | 예시 |
|------|------|
| 산술 연산자 | `+`, `-`, `*`, `/`, `%`, `**` |
| 대입 연산자 | `=`, `+=`, `-=`, `*=`, `/=` |
| 비교 연산자 | `==`, `===`, `!=`, `!==`, `>`, `<` |
| 논리 연산자 | `&&`, `||`, `!` |
| 삼항 연산자 | `조건 ? A : B` |
| Null 병합 연산자 | `??` |
| 옵셔널 체이닝 | `?.` |

---

# 산술 연산자

숫자를 계산할 때 사용하는 연산자이다.

| 연산자 | 의미 |
|---------|------|
| `+` | 더하기 |
| `-` | 빼기 |
| `*` | 곱하기 |
| `/` | 나누기 |
| `%` | 나머지 |
| `**` | 거듭제곱 |

---

## 더하기(+)

```javascript
console.log(10 + 5);
```

결과

```text
15
```

---

## 빼기(-)

```javascript
console.log(10 - 5);
```

↓

```text
5
```

---

## 곱하기(*)

```javascript
console.log(10 * 5);
```

↓

```text
50
```

---

## 나누기(/)

```javascript
console.log(10 / 2);
```

↓

```text
5
```

---

## 나머지(%)

```javascript
console.log(10 % 3);
```

↓

```text
1
```

### 실무 활용

짝수 판별

```javascript
if(number % 2 === 0){

    console.log("짝수");

}
```

배열을 순환하거나 일정 간격마다 작업을 수행할 때도 자주 사용한다.

---

## 거듭제곱(**)

```javascript
console.log(2 ** 3);
```

↓

```text
8
```

ES2016부터 추가된 연산자이다.

---

# 문자열과 +

`+`는 숫자 계산뿐 아니라 문자열 연결에도 사용된다.

```javascript
console.log("Hello" + " JavaScript");
```

↓

```text
Hello JavaScript
```

---

숫자와 문자열이 함께 있으면 문자열 연결이 우선된다.

```javascript
console.log("10" + 20);
```

↓

```text
1020
```

이 동작은 암시적 형 변환에 의해 발생한다.

---

# 대입 연산자

변수에 값을 저장하거나 계산 결과를 다시 저장할 때 사용한다.

---

## 기본 대입

```javascript
let score = 100;
```

---

## +=

```javascript
let score = 100;

score += 20;
```

↓

```text
120
```

다음 코드와 같다.

```javascript
score = score + 20;
```

---

## -=

```javascript
score -= 10;
```

↓

```text
110
```

---

## *=

```javascript
score *= 2;
```

↓

```text
220
```

---

## /=

```javascript
score /= 2;
```

↓

```text
110
```

---

## %=

```javascript
score %= 3;
```

↓

```text
2
```

---

# 증감 연산자

값을 1 증가하거나 감소시킨다.

---

## 증가(++)

```javascript
let count = 0;

count++;
```

↓

```text
1
```

---

## 감소(--)

```javascript
count--;
```

↓

```text
0
```

---

# 전위 증가와 후위 증가

## 후위 증가

```javascript
let a = 5;

console.log(a++);
```

출력

```text
5
```

이후 `a`의 값은 `6`이 된다.

---

## 전위 증가

```javascript
let b = 5;

console.log(++b);
```

출력

```text
6
```

증가 후 출력한다.

---

# 언제 사용할까?

반복문에서 가장 많이 사용된다.

```javascript
for(let i = 0; i < 10; i++){

    console.log(i);

}
```

---

---

# 비교 연산자

비교 연산자는 **두 값을 비교하여 `true` 또는 `false`를 반환하는 연산자**이다.

조건문(`if`), 반복문(`while`), 삼항 연산자 등에서 매우 자주 사용된다.

| 연산자 | 의미 |
|---------|------|
| `==` | 값만 비교 |
| `===` | 값과 자료형 비교 |
| `!=` | 값이 다르면 true |
| `!==` | 값 또는 자료형이 다르면 true |
| `>` | 크다 |
| `<` | 작다 |
| `>=` | 크거나 같다 |
| `<=` | 작거나 같다 |

---

# == (동등 비교)

`==`는 **자료형이 달라도 값이 같으면 `true`**를 반환한다.

```javascript
console.log(10 == "10");
```

결과

```text
true
```

JavaScript가 내부적으로 형 변환을 수행하기 때문이다.

---

또 다른 예제

```javascript
console.log(false == 0);
```

↓

```text
true
```

---

```javascript
console.log(true == 1);
```

↓

```text
true
```

---

```javascript
console.log("" == false);
```

↓

```text
true
```

이처럼 예상하지 못한 결과가 발생할 수 있다.

---

# === (일치 비교)

`===`는 **값과 자료형이 모두 같아야 `true`**를 반환한다.

```javascript
console.log(10 === "10");
```

↓

```text
false
```

---

```javascript
console.log(10 === 10);
```

↓

```text
true
```

---

## 실무에서는 === 사용

실무에서는 거의 항상 `===`를 사용한다.

```javascript
if(userAge === 20){

    console.log("성인");

}
```

형 변환으로 인한 오류를 예방할 수 있기 때문이다.

---

# !=

값이 다르면 `true`를 반환한다.

```javascript
console.log(10 != "10");
```

↓

```text
false
```

---

# !==

값 또는 자료형이 다르면 `true`를 반환한다.

```javascript
console.log(10 !== "10");
```

↓

```text
true
```

실무에서는 `!==` 역시 `!=`보다 많이 사용한다.

---

# 크기 비교

## >

```javascript
console.log(20 > 10);
```

↓

```text
true
```

---

## <

```javascript
console.log(20 < 10);
```

↓

```text
false
```

---

## >=

```javascript
console.log(20 >= 20);
```

↓

```text
true
```

---

## <=

```javascript
console.log(10 <= 20);
```

↓

```text
true
```

---

# 문자열 비교

문자열도 비교할 수 있다.

```javascript
console.log("apple" < "banana");
```

↓

```text
true
```

문자열은 **유니코드(Unicode)** 값을 기준으로 비교된다.

예를 들어,

```javascript
console.log("A" < "B");
```

↓

```text
true
```

---

# 논리 연산자

논리 연산자는 여러 조건을 조합하거나 반전할 때 사용한다.

| 연산자 | 의미 |
|---------|------|
| `&&` | AND |
| `||` | OR |
| `!` | NOT |

---

# AND (&&)

모든 조건이 참이어야 `true`이다.

```javascript
let age = 25;

let isMember = true;

console.log(age >= 20 && isMember);
```

↓

```text
true
```

---

하나라도 거짓이면

```javascript
console.log(true && false);
```

↓

```text
false
```

---

## 실무 예제

```javascript
if(user.isLogin && user.isAdmin){

    console.log("관리자 페이지");

}
```

로그인했고 관리자일 때만 실행된다.

---

# OR (||)

하나라도 참이면 `true`이다.

```javascript
console.log(true || false);
```

↓

```text
true
```

---

```javascript
console.log(false || false);
```

↓

```text
false
```

---

## 실무 예제

```javascript
if(isAdmin || isManager){

    console.log("접근 가능");

}
```

관리자 또는 매니저라면 실행된다.

---

# NOT (!)

참과 거짓을 반전시킨다.

```javascript
console.log(!true);
```

↓

```text
false
```

---

```javascript
console.log(!false);
```

↓

```text
true
```

---

## 실무 예제

```javascript
if(!isLogin){

    console.log("로그인이 필요합니다.");

}
```

로그인하지 않은 경우 실행된다.

---

# 단축 평가(Short Circuit Evaluation)

JavaScript의 `&&`와 `||`는 **Boolean만 반환하는 것이 아니라, 평가가 끝난 시점의 값을 그대로 반환**한다.

이 특성은 실무에서 매우 자주 활용된다.

---

## &&의 단축 평가

```javascript
console.log(true && "Hello");
```

↓

```text
Hello
```

---

```javascript
console.log(false && "Hello");
```

↓

```text
false
```

앞의 값이 `false`이면 뒤는 평가하지 않는다.

---

## ||의 단축 평가

```javascript
console.log(false || "Guest");
```

↓

```text
Guest
```

---

```javascript
console.log("Admin" || "Guest");
```

↓

```text
Admin
```

앞의 값이 Truthy라면 뒤를 평가하지 않는다.

---

# 실무 활용

기본값을 지정할 때 자주 사용한다.

```javascript
const userName = inputValue || "익명";
```

단, `0`이나 `""`도 Falsy이므로 의도와 다르게 동작할 수 있다.

이 문제를 해결하기 위해 `??` 연산자가 도입되었다.

---

---

# Null 병합 연산자 (??)

Null 병합 연산자(Nullish Coalescing Operator)는 **왼쪽 값이 `null` 또는 `undefined`인 경우에만** 오른쪽 값을 반환한다.

기본 문법은 다음과 같다.

```javascript
const result = value ?? "기본값";
```

---

## 기본 예제

```javascript
const name = null;

console.log(name ?? "Guest");
```

결과

```text
Guest
```

---

```javascript
const name = "Kim";

console.log(name ?? "Guest");
```

↓

```text
Kim
```

---

# || 와 ?? 차이

실무에서 가장 많이 헷갈리는 부분이다.

```javascript
const value = 0;

console.log(value || 100);
```

↓

```text
100
```

`0`은 Falsy이므로 오른쪽 값이 선택된다.

---

반면

```javascript
const value = 0;

console.log(value ?? 100);
```

↓

```text
0
```

`??`는 `null`과 `undefined`만 검사하기 때문이다.

---

## 빈 문자열

```javascript
const name = "";

console.log(name || "Guest");
```

↓

```text
Guest
```

---

```javascript
const name = "";

console.log(name ?? "Guest");
```

↓

```text

```

(빈 문자열 출력)

---

# 언제 ??를 사용할까?

사용자의 입력값이

- 0
- false
- ""

도 정상적인 값일 수 있다면 `??`를 사용하는 것이 적절하다.

예를 들어

```javascript
const quantity = userInput ?? 1;
```

처럼 작성하면 실제 값이 없을 때만 기본값을 사용할 수 있다.

---

# 옵셔널 체이닝 (?.)

옵셔널 체이닝(Optional Chaining)은 **객체가 존재하는지 안전하게 확인하면서 속성에 접근하는 연산자**이다.

ES2020에서 추가되었다.

---

## 문제 상황

```javascript
const user = null;

console.log(user.name);
```

결과

```text
TypeError
```

객체가 없는데 속성에 접근했기 때문이다.

---

## 옵셔널 체이닝 사용

```javascript
const user = null;

console.log(user?.name);
```

↓

```text
undefined
```

오류가 발생하지 않는다.

---

## 객체가 존재하는 경우

```javascript
const user = {

    name: "Kim"

};

console.log(user?.name);
```

↓

```text
Kim
```

---

# 중첩 객체

옵셔널 체이닝은 중첩 객체에서도 유용하다.

```javascript
const user = {

    profile: {

        address: {

            city: "Seoul"

        }

    }

};
```

접근

```javascript
console.log(user?.profile?.address?.city);
```

↓

```text
Seoul
```

---

객체가 없는 경우

```javascript
const user = {};

console.log(user?.profile?.address?.city);
```

↓

```text
undefined
```

오류 없이 종료된다.

---

# 실무 활용

API 응답은 일부 데이터가 없을 수 있다.

예를 들어

```javascript
const user = response.data;
```

다음과 같이 안전하게 사용할 수 있다.

```javascript
console.log(user?.profile?.image);
```

React에서도 매우 자주 사용하는 문법이다.

---

# 삼항 연산자

삼항 연산자는 조건에 따라 두 값 중 하나를 선택한다.

문법

```javascript
조건 ? 참일 때 : 거짓일 때
```

---

## 기본 예제

```javascript
const age = 20;

const result = age >= 19 ? "성인" : "미성년자";

console.log(result);
```

↓

```text
성인
```

---

## if문과 비교

다음 코드는

```javascript
if(age >= 19){

    result = "성인";

}else{

    result = "미성년자";

}
```

삼항 연산자로 작성하면

```javascript
const result = age >= 19 ? "성인" : "미성년자";
```

처럼 한 줄로 표현할 수 있다.

---

# 중첩 삼항 연산자

```javascript
const score = 85;

const grade =
score >= 90
? "A"
: score >= 80
? "B"
: "C";
```

결과

```text
B
```

---

## 주의

중첩이 많아질수록 가독성이 크게 떨어진다.

다음과 같은 경우에는

- 조건이 많다.
- 여러 줄의 처리가 필요하다.
- 유지보수가 중요하다.

`if`문을 사용하는 것이 좋다.

---

# 연산자 우선순위

JavaScript는 연산자마다 우선순위가 존재한다.

예를 들어

```javascript
console.log(10 + 5 * 2);
```

↓

```text
20
```

곱셈이 먼저 수행된다.

---

괄호를 사용하면

```javascript
console.log((10 + 5) * 2);
```

↓

```text
30
```

---

## 자주 사용하는 우선순위

| 우선순위 | 연산자 |
|----------|---------|
| 높음 | `()` |
| ↑ | `!`, `++`, `--` |
| ↑ | `*`, `/`, `%` |
| ↑ | `+`, `-` |
| ↑ | `>`, `<`, `>=`, `<=` |
| ↑ | `==`, `===`, `!=`, `!==` |
| ↑ | `&&` |
| ↑ | `||` |
| 낮음 | `??`, `=` |

복잡한 수식에서는 우선순위를 외우기보다 **괄호를 사용하는 습관**이 실수를 줄인다.

---

# 실무에서 자주 사용하는 패턴

## 기본값 설정

```javascript
const nickname = user.nickname ?? "익명";
```

---

## 안전한 객체 접근

```javascript
const image = user?.profile?.image;
```

---

## 로그인 여부

```javascript
if(user?.isLogin){

    console.log("로그인 완료");

}
```

---

## 조건에 따른 클래스 지정

```javascript
const className =
isActive
? "active"
: "inactive";
```

---

---

# 실무 예제 프로젝트

다음은 로그인 여부와 관리자 권한을 확인하여 화면에 메시지를 출력하는 예제이다.

## HTML

```html
<h2>로그인 상태</h2>

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

const message =
    user?.isLogin && user?.role === "admin"
        ? `${user.name}님은 관리자입니다.`
        : "접근 권한이 없습니다.";

result.textContent = message;
```

### 학습한 내용

- 비교 연산자(`===`)
- 논리 연산자(`&&`)
- 삼항 연산자
- 옵셔널 체이닝(`?.`)
- Template Literal
- DOM 출력

---

# 실무 활용

## 1. 입력값 검증

```javascript
if (userName === "") {

    alert("이름을 입력해주세요.");

}
```

문자열 비교는 `===`를 사용하는 것이 안전하다.

---

## 2. 기본값 지정

```javascript
const page = currentPage ?? 1;
```

`0`도 정상적인 값이라면 `??`를 사용하는 것이 적절하다.

---

## 3. API 응답 처리

```javascript
const image = response?.data?.profile?.image;
```

객체가 존재하지 않아도 오류 없이 처리할 수 있다.

---

## 4. 조건부 클래스 지정

```javascript
const buttonClass =
    isActive
        ? "btn-primary"
        : "btn-secondary";
```

React, Vue 등에서도 자주 사용하는 패턴이다.

---

## 5. 권한 확인

```javascript
if (user.isLogin && user.role === "admin") {

    console.log("관리자 메뉴");

}
```

실무에서는 여러 조건을 `&&`로 조합하는 경우가 매우 많다.

---

# 이번 문서에서 새롭게 배운 내용

- 산술 연산자의 종류와 활용 방법
- 대입 연산자를 이용한 간결한 코드 작성
- 증감 연산자의 전위/후위 차이
- `==`와 `===`의 차이
- `!=`와 `!==`의 차이
- 논리 연산자(`&&`, `||`, `!`)의 동작 방식
- 단축 평가(Short Circuit Evaluation)
- `??`와 `||`의 차이
- 옵셔널 체이닝(`?.`)을 이용한 안전한 객체 접근
- 삼항 연산자로 조건을 간결하게 표현하는 방법
- 연산자 우선순위와 괄호의 중요성

---

# 자주 하는 실수

- `==`를 사용하여 의도하지 않은 형 변환이 발생한다.
- `=`(대입)과 `===`(비교)를 혼동한다.
- `||`와 `??`의 차이를 이해하지 못한다.
- 옵셔널 체이닝 없이 존재하지 않는 객체의 속성에 접근한다.
- 복잡한 조건을 삼항 연산자로 작성하여 가독성을 떨어뜨린다.
- 전위 증가(`++i`)와 후위 증가(`i++`)의 차이를 이해하지 못한다.
- 연산자 우선순위를 잘못 이해하여 예상과 다른 결과가 나온다.

---

# 면접 포인트

### `==`와 `===`의 차이는 무엇인가?

- `==`는 자료형을 변환한 뒤 값을 비교한다.
- `===`는 자료형과 값을 모두 비교한다.

실무에서는 예측 가능한 비교를 위해 `===`를 사용하는 것이 일반적이다.

---

### `&&`와 `||`의 단축 평가란?

`&&`는 첫 번째 Falsy 값을 반환하거나, 모두 Truthy이면 마지막 값을 반환한다.

`||`는 첫 번째 Truthy 값을 반환하거나, 모두 Falsy이면 마지막 값을 반환한다.

이를 이용해 기본값 설정이나 조건부 실행을 간결하게 작성할 수 있다.

---

### `??`와 `||`의 차이는?

- `||`는 모든 Falsy 값을 기준으로 판단한다.
- `??`는 `null`과 `undefined`만 기준으로 판단한다.

`0`, `false`, `""`도 유효한 값일 수 있다면 `??`를 사용하는 것이 적절하다.

---

### 옵셔널 체이닝(`?.`)은 언제 사용하는가?

객체나 중첩된 속성이 존재하지 않을 가능성이 있을 때 안전하게 접근하기 위해 사용한다.

---

### 삼항 연산자는 언제 사용하는가?

간단한 조건에 따라 값을 선택할 때 사용한다.

복잡한 분기나 여러 줄의 로직에는 `if`문이 더 적합하다.

---

### 연산자 우선순위를 모두 외워야 하는가?

기본적인 우선순위는 알고 있는 것이 좋지만, 실무에서는 **괄호를 적극적으로 사용하여 의도를 명확히 표현하는 것**이 더 중요하다.

---

# 핵심 정리

- 산술 연산자는 숫자 계산에 사용한다.
- 대입 연산자는 계산과 저장을 함께 수행할 수 있다.
- 비교는 `===`, `!==`를 사용하는 것이 안전하다.
- `&&`, `||`, `!`는 조건을 조합하거나 반전할 때 사용한다.
- 단축 평가는 기본값 설정과 조건부 실행에 자주 활용된다.
- `??`는 `null`과 `undefined`만 검사한다.
- `?.`는 객체 접근 시 발생할 수 있는 오류를 방지한다.
- 삼항 연산자는 간단한 조건식을 표현할 때 유용하다.
- 복잡한 식은 괄호를 사용해 가독성을 높이는 것이 좋다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
