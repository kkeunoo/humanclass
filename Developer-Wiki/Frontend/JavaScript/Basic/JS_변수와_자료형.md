---
title: JavaScript 변수와 자료형
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# JavaScript 변수와 자료형

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | JavaScript 변수와 자료형 |
| 분류 | Frontend / JavaScript / Basic |
| 난이도 | Beginner |
| 선수 지식 | JavaScript 소개와 실행환경 |
| 핵심 주제 | 변수, 자료형, 선언 키워드, 동적 타입 |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

프로그램은 데이터를 저장하고 처리하는 과정의 연속이다.

JavaScript에서는 데이터를 저장하기 위해 **변수(Variable)** 를 사용하며, 저장되는 데이터의 종류를 **자료형(Data Type)** 이라고 한다.

변수와 자료형은 모든 JavaScript 코드의 기반이 되며, 이후 배우게 될 함수, 객체, 배열, DOM 조작에서도 계속 사용된다.

---

# 변수(Variable)란?

변수는 **데이터를 저장하기 위한 이름이 붙은 메모리 공간**이다.

예를 들어 다음과 같은 코드를 보자.

```javascript
let userName = "Kim";
```

이 코드는 문자열 `"Kim"`을 메모리에 저장하고, 그 위치를 `userName`이라는 이름으로 참조하도록 만든다.

즉,

```text
userName
    │
    ▼
+-------------+
|    "Kim"    |
+-------------+
```

변수를 사용하면 값을 반복해서 사용할 수 있으며, 필요에 따라 값을 변경하거나 참조할 수 있다.

---

# 변수가 필요한 이유

변수가 없다면 같은 값을 여러 번 직접 작성해야 한다.

```javascript
console.log("Kim");
console.log("Kim");
console.log("Kim");
```

변수를 사용하면 다음과 같이 한 곳만 수정하면 된다.

```javascript
let name = "Kim";

console.log(name);
console.log(name);
console.log(name);
```

유지보수성과 가독성이 크게 향상된다.

---

# 메모리와 변수

변수는 메모리의 특정 위치를 가리킨다.

```javascript
let age = 20;
```

개념적으로는 다음과 같이 이해할 수 있다.

```text
변수명

age
 │
 ▼

메모리

+------+
|  20  |
+------+
```

실제 메모리 주소를 직접 다루지는 않지만, JavaScript 엔진이 내부적으로 관리한다.

---

# 변수 선언

변수를 사용하려면 먼저 선언해야 한다.

JavaScript에는 세 가지 선언 키워드가 있다.

```javascript
var
let
const
```

현재 실무에서는 `let`과 `const`를 사용하는 것이 일반적이다.

---

# let

값을 변경할 수 있는 변수를 선언한다.

```javascript
let score = 80;

score = 90;
```

결과적으로 `score`에는 `90`이 저장된다.

---

# const

재할당이 불가능한 변수를 선언한다.

```javascript
const pi = 3.141592;
```

다음과 같이 값을 변경하려고 하면 오류가 발생한다.

```javascript
const pi = 3.14;

pi = 3;
```

`const`는 상수뿐 아니라 **재할당되지 않아야 하는 모든 변수**에 사용하는 것이 권장된다.

---

# var

과거 JavaScript에서 사용하던 변수 선언 방식이다.

```javascript
var message = "Hello";
```

현재는 호이스팅과 함수 스코프 등의 특성으로 인해 예상치 못한 동작을 만들 수 있어, 새로운 코드에서는 사용을 권장하지 않는다.

기존 프로젝트나 레거시 코드에서 자주 볼 수 있다.

---

# var, let, const 비교

| 항목 | var | let | const |
|------|-----|-----|------|
| 재선언 | 가능 | 불가능 | 불가능 |
| 재할당 | 가능 | 가능 | 불가능 |
| 스코프 | 함수(Function) | 블록(Block) | 블록(Block) |
| 호이스팅 | O | O(초기화 전 접근 불가) | O(초기화 전 접근 불가) |
| 실무 사용 | 거의 사용하지 않음 | 자주 사용 | 가장 많이 사용 |

---

# 어떤 것을 사용해야 할까?

실무에서는 다음 기준을 많이 사용한다.

1. **기본적으로 `const`를 사용한다.**
2. 값이 변경되어야 한다면 `let`을 사용한다.
3. `var`는 특별한 이유가 없다면 사용하지 않는다.

예를 들어

```javascript
const company = "OpenAI";

let count = 0;

count++;
```

처럼 작성하는 것이 일반적인 패턴이다.

---

# 변수 선언과 초기화

변수를 선언만 할 수도 있다.

```javascript
let user;
```

이 상태에서 `user`의 값은 `undefined`이다.

초기화는 선언과 동시에 값을 저장하는 것을 의미한다.

```javascript
let user = "Alice";
```

---

# 변수 이름 규칙

변수명은 다음 규칙을 따라야 한다.

- 문자, 숫자, `_`, `$`를 사용할 수 있다.
- 숫자로 시작할 수 없다.
- 공백을 사용할 수 없다.
- 예약어(`if`, `for`, `class` 등)는 사용할 수 없다.

올바른 예

```javascript
userName

user_age

$total

count2
```

잘못된 예

```javascript
2user

user name

for

class
```

---

# 변수 이름 작성 관례

실무에서는 **camelCase**를 가장 많이 사용한다.

```javascript
userName

userAge

orderPrice

totalCount
```

상수처럼 변하지 않는 값을 별도로 강조해야 하는 경우에는 대문자와 `_`를 사용하기도 한다.

```javascript
const MAX_SIZE = 10;
```

---

---

# 자료형(Data Type)

자료형(Data Type)은 **변수에 저장되는 데이터의 종류**를 의미한다.

JavaScript는 크게 두 가지 자료형으로 구분한다.

```text
Data Type

├── Primitive Type (원시 타입)

└── Reference Type (참조 타입)
```

---

# Primitive Type (원시 타입)

원시 타입은 하나의 값만 저장하는 가장 기본적인 자료형이다.

JavaScript에는 다음과 같은 원시 타입이 있다.

- Number
- String
- Boolean
- Undefined
- Null
- Symbol
- BigInt

원시 타입은 값 자체를 저장하며, 비교적 단순한 구조를 가진다.

---

# Reference Type (참조 타입)

참조 타입은 객체(Object)를 기반으로 하는 자료형이다.

대표적인 예는 다음과 같다.

- Object
- Array
- Function
- Date
- Map
- Set

참조 타입은 **값 자체가 아닌 객체의 참조(Reference)** 를 저장한다.

이 내용은 객체(Object) 문서에서 자세히 다룬다.

---

# Number

숫자를 저장하는 자료형이다.

JavaScript는 정수와 실수를 구분하지 않고 모두 `Number` 타입으로 처리한다.

```javascript
let age = 20;

let price = 19900;

let pi = 3.141592;
```

---

## Number 특징

```javascript
console.log(typeof 10);
```

결과

```text
number
```

정수

```javascript
100
```

실수

```javascript
3.14
```

모두 Number 타입이다.

---

## 특수한 Number 값

### Infinity

무한대를 의미한다.

```javascript
console.log(10 / 0);
```

결과

```text
Infinity
```

---

### -Infinity

음의 무한대이다.

```javascript
console.log(-10 / 0);
```

---

### NaN

Not a Number의 약자이다.

숫자가 아닌 연산 결과를 의미한다.

```javascript
console.log("Hello" * 10);
```

결과

```text
NaN
```

---

# String

문자열을 저장하는 자료형이다.

```javascript
let name = "Kim";

let city = 'Seoul';
```

작은따옴표와 큰따옴표 모두 사용할 수 있다.

---

## 문자열 연결

```javascript
let first = "Hello";

let second = "World";

console.log(first + " " + second);
```

결과

```text
Hello World
```

---

## 문자열 길이

```javascript
let text = "JavaScript";

console.log(text.length);
```

결과

```text
10
```

---

## Template Literal

ES6에서 추가된 문자열 문법이다.

백틱(``)을 사용한다.

```javascript
let name = "Kim";

console.log(`안녕하세요 ${name}님`);
```

결과

```text
안녕하세요 Kim님
```

실무에서는 문자열 연결보다 Template Literal을 더 많이 사용한다.

---

# Boolean

참(True)과 거짓(False)을 나타내는 자료형이다.

```javascript
let isLogin = true;

let isAdmin = false;
```

주로 조건문에서 사용된다.

```javascript
if(isLogin){

    console.log("로그인 성공");

}
```

---

# Undefined

값이 아직 할당되지 않은 상태를 의미한다.

```javascript
let user;

console.log(user);
```

결과

```text
undefined
```

JavaScript 엔진이 자동으로 부여하는 값이다.

---

# Null

값이 없음을 **의도적으로 표현**하는 자료형이다.

```javascript
let selectedUser = null;
```

예를 들어

```javascript
let image = null;
```

은

"현재 선택된 이미지가 없다."

라는 의미를 표현할 수 있다.

---

# Undefined와 Null 차이

| Undefined | Null |
|------------|------|
| 자동으로 부여 | 개발자가 직접 지정 |
| 아직 값이 없음 | 의도적으로 비어 있음 |

예제

```javascript
let a;

let b = null;
```

결과

```javascript
console.log(a); // undefined

console.log(b); // null
```

실무에서는 둘의 의미를 명확히 구분하는 것이 중요하다.

---

# Symbol

고유한 값을 생성하는 자료형이다.

```javascript
const id1 = Symbol();

const id2 = Symbol();
```

비교

```javascript
console.log(id1 === id2);
```

결과

```text
false
```

주로 객체의 고유한 속성 키를 만들 때 사용한다.

일반적인 웹 개발에서는 자주 사용하지 않지만, 라이브러리나 프레임워크 내부 구현에서 활용된다.

---

# BigInt

매우 큰 정수를 표현하기 위한 자료형이다.

```javascript
const num = 9007199254740993n;
```

끝에 `n`을 붙여 작성한다.

```javascript
console.log(typeof num);
```

결과

```text
bigint
```

일반적인 웹 서비스에서는 사용할 일이 많지 않지만, 금융·암호화·대용량 정수 계산 등에서 사용된다.

---

# typeof

변수의 자료형을 확인하는 연산자이다.

```javascript
let age = 20;

console.log(typeof age);
```

결과

```text
number
```

---

## 다양한 typeof 결과

```javascript
typeof 10
```

↓

```text
number
```

```javascript
typeof "Hello"
```

↓

```text
string
```

```javascript
typeof true
```

↓

```text
boolean
```

```javascript
typeof undefined
```

↓

```text
undefined
```

```javascript
typeof Symbol()
```

↓

```text
symbol
```

```javascript
typeof 100n
```

↓

```text
bigint
```

---

## typeof null

JavaScript에서 유명한 특징 중 하나이다.

```javascript
console.log(typeof null);
```

결과

```text
object
```

이는 JavaScript 초창기부터 존재한 역사적인 설계상의 이유로 남아 있는 동작이다.

실제로 `null`은 객체가 아니지만, `typeof null`의 결과는 `"object"`이다.

면접에서도 자주 등장하는 질문 중 하나이다.

---

---

# 동적 타입(Dynamic Typing)

JavaScript는 **동적 타입(Dynamic Typing)** 언어이다.

즉, 변수의 자료형을 미리 선언하지 않아도 되며, 실행 중에도 자료형이 변경될 수 있다.

예제

```javascript
let value = 100;

console.log(typeof value);
```

결과

```text
number
```

이후 같은 변수에 문자열을 저장할 수도 있다.

```javascript
value = "Hello";

console.log(typeof value);
```

결과

```text
string
```

Boolean도 저장 가능하다.

```javascript
value = true;

console.log(typeof value);
```

결과

```text
boolean
```

---

# 동적 타입의 장점

동적 타입은 코드 작성이 빠르고 유연하다.

예를 들어

```javascript
let data;

data = "Kim";

data = 30;

data = false;
```

처럼 자유롭게 값을 변경할 수 있다.

장점

- 문법이 간단하다.
- 개발 속도가 빠르다.
- 프로토타입 제작이 쉽다.

---

# 동적 타입의 단점

자료형이 실행 중 변경되기 때문에 예상하지 못한 오류가 발생할 수 있다.

예제

```javascript
let price = 100;

price = "100";
```

겉보기에는 같은 값처럼 보이지만

```javascript
console.log(typeof price);
```

결과

```text
string
```

이 된다.

실무에서는 이러한 문제를 방지하기 위해 변수명을 명확하게 작성하고, 필요한 경우 자료형을 검사한다.

---

# 형 변환(Type Conversion)

형 변환은 **자료형을 다른 자료형으로 변경하는 것**을 의미한다.

JavaScript는

- 암시적 형 변환(Implicit Conversion)
- 명시적 형 변환(Explicit Conversion)

두 가지 방식을 제공한다.

---

# 암시적 형 변환

JavaScript 엔진이 자동으로 자료형을 변환한다.

예제

```javascript
console.log("10" + 5);
```

결과

```text
105
```

숫자 `5`가 문자열 `"5"`로 변환되어 문자열 연결이 이루어진다.

---

또 다른 예제

```javascript
console.log("10" - 5);
```

결과

```text
5
```

`-` 연산은 숫자 계산만 가능하므로 문자열 `"10"`이 숫자 `10`으로 변환된다.

---

## 다양한 예제

```javascript
console.log(true + 1);
```

↓

```text
2
```

---

```javascript
console.log(false + 1);
```

↓

```text
1
```

---

```javascript
console.log(null + 1);
```

↓

```text
1
```

---

```javascript
console.log(undefined + 1);
```

↓

```text
NaN
```

이처럼 암시적 형 변환은 예상하지 못한 결과를 만들 수 있으므로 주의해야 한다.

---

# 명시적 형 변환

개발자가 직접 자료형을 변환하는 방법이다.

실무에서는 암시적 형 변환보다 명시적 형 변환을 권장한다.

---

## Number()

문자열을 숫자로 변환한다.

```javascript
let value = "100";

let num = Number(value);

console.log(num);
```

결과

```text
100
```

자료형

```javascript
console.log(typeof num);
```

↓

```text
number
```

---

## String()

다른 자료형을 문자열로 변환한다.

```javascript
let num = 100;

let text = String(num);
```

결과

```text
"100"
```

---

## Boolean()

Boolean으로 변환한다.

```javascript
Boolean(1)
```

↓

```text
true
```

---

```javascript
Boolean(0)
```

↓

```text
false
```

---

```javascript
Boolean("")
```

↓

```text
false
```

---

```javascript
Boolean("JavaScript")
```

↓

```text
true
```

---

# parseInt()

문자열을 정수(Integer)로 변환한다.

```javascript
parseInt("100")
```

↓

```text
100
```

---

```javascript
parseInt("100px")
```

↓

```text
100
```

숫자가 아닌 문자를 만나면 변환을 종료한다.

---

# parseFloat()

실수를 변환한다.

```javascript
parseFloat("3.14")
```

↓

```text
3.14
```

---

```javascript
parseFloat("10.5px")
```

↓

```text
10.5
```

---

# Number()와 parseInt() 차이

```javascript
Number("100px")
```

↓

```text
NaN
```

---

```javascript
parseInt("100px")
```

↓

```text
100
```

실무에서는 입력값의 형태에 따라 적절한 함수를 선택해야 한다.

---

# Truthy와 Falsy

JavaScript에서는 Boolean이 아닌 값도 조건문에서 참과 거짓으로 평가된다.

이를

- Truthy
- Falsy

라고 한다.

---

## Falsy 값

다음 값들은 모두 거짓으로 평가된다.

```javascript
false
```

```javascript
0
```

```javascript
-0
```

```javascript
0n
```

```javascript
""
```

```javascript
null
```

```javascript
undefined
```

```javascript
NaN
```

위 값을 제외한 대부분의 값은 Truthy이다.

---

## Truthy 예제

```javascript
if("Hello"){

    console.log("실행");

}
```

결과

```text
실행
```

---

```javascript
if(100){

    console.log("실행");

}
```

결과

```text
실행
```

---

# 실무에서 자주 사용하는 패턴

입력값이 존재하는지 확인할 때 자주 사용한다.

```javascript
if(userName){

    console.log("입력 완료");

}
```

`userName`이 빈 문자열이라면 조건문은 실행되지 않는다.

---

# Null 병합 연산자와의 관계

Falsy와 관련하여 자주 혼동하는 연산자가 있다.

```javascript
const result = value ?? "기본값";
```

`??`는 **`null` 또는 `undefined`인 경우에만** 오른쪽 값을 사용한다.

반면 `||`는 모든 Falsy 값을 기준으로 판단한다.

```javascript
const a = 0 || 10;   // 10

const b = 0 ?? 10;   // 0
```

이 차이는 실무에서 매우 중요하며, 연산자 문서에서 다시 자세히 다룬다.

---

---

# 메모리 관점에서 변수 이해

변수는 단순히 값을 저장하는 이름이 아니라 **메모리에 저장된 데이터를 참조하는 식별자(Identifier)** 이다.

예를 들어 다음 코드를 살펴보자.

```javascript
let score = 100;
```

개념적으로는 다음과 같이 이해할 수 있다.

```text
변수

score
  │
  ▼

+---------+
|   100   |
+---------+
```

이후 값을 변경하면

```javascript
score = 200;
```

다음과 같이 새로운 값으로 갱신된다.

```text
변수

score
  │
  ▼

+---------+
|   200   |
+---------+
```

JavaScript 엔진은 내부적으로 메모리를 관리하며 개발자는 변수명을 통해 값에 접근한다.

---

# 원시 타입과 참조 타입 비교

JavaScript의 자료형은 크게 **원시 타입(Primitive Type)** 과 **참조 타입(Reference Type)** 으로 나뉜다.

| 항목 | Primitive | Reference |
|------|-----------|-----------|
| 저장 방식 | 값(Value) | 참조(Reference) |
| 대표 자료형 | Number, String, Boolean | Object, Array, Function |
| 복사 방식 | 값 복사 | 참조 복사 |
| 비교 | 값 비교 | 참조 비교 |

---

## 원시 타입 복사

```javascript
let a = 10;

let b = a;

b = 20;

console.log(a);
console.log(b);
```

결과

```text
10

20
```

`a`와 `b`는 서로 독립적인 값을 가진다.

---

## 참조 타입 복사

```javascript
const user1 = {

    name: "Kim"

};

const user2 = user1;

user2.name = "Lee";

console.log(user1.name);
```

결과

```text
Lee
```

두 변수가 **같은 객체를 참조**하고 있기 때문이다.

이 개념은 객체(Object) 문서에서 더욱 자세히 다룬다.

---

# 실무 예제 프로젝트

다음은 회원 정보를 저장하고 출력하는 간단한 예제이다.

## HTML

```html
<h2>회원 정보</h2>

<p id="result"></p>
```

---

## JavaScript

```javascript
const userName = "Kim";

let age = 27;

const isDeveloper = true;

const result = document.querySelector("#result");

result.textContent =
`${userName} / ${age}세 / 개발자 여부 : ${isDeveloper}`;
```

학습한 내용

- const
- let
- String
- Number
- Boolean
- Template Literal
- DOM 출력

---

# 실무 활용

## 1. 상수는 const 사용

```javascript
const API_URL = "https://example.com";
```

변경되지 않는 값은 `const`를 사용하면 실수를 줄일 수 있다.

---

## 2. 반복적으로 변경되는 값은 let 사용

```javascript
let currentPage = 1;

currentPage++;
```

페이지 번호, 카운트, 점수 등은 `let`이 적합하다.

---

## 3. 입력값은 명시적으로 형 변환

```javascript
const age = Number(input.value);
```

브라우저의 `<input>` 값은 항상 문자열이므로, 필요한 자료형으로 변환하는 습관을 들이는 것이 좋다.

---

## 4. typeof를 활용한 디버깅

```javascript
console.log(typeof value);
```

예상과 다른 자료형이 들어왔는지 빠르게 확인할 수 있다.

---

# 이번 문서에서 새롭게 배운 내용

- 변수는 메모리에 저장된 데이터를 참조하는 식별자이다.
- `let`, `const`, `var`의 차이와 사용 기준을 이해했다.
- JavaScript는 동적 타입 언어이다.
- 자료형은 원시 타입과 참조 타입으로 구분된다.
- `typeof`를 이용해 자료형을 확인할 수 있다.
- `undefined`와 `null`은 의미가 다르다.
- `Number()`, `String()`, `Boolean()` 등을 이용해 명시적으로 형 변환할 수 있다.
- `parseInt()`와 `parseFloat()`는 문자열에서 숫자를 추출할 때 사용한다.
- Truthy와 Falsy를 이해하면 조건문을 간결하게 작성할 수 있다.

---

# 자주 하는 실수

- `const`로 선언한 변수를 재할당하려고 한다.
- `var`를 새로운 코드에서도 사용한다.
- `==`와 `===`의 차이를 고려하지 않고 비교한다.
- `typeof null`이 `"null"`이라고 생각한다.
- `<input>`의 값을 숫자로 변환하지 않고 계산한다.
- `parseInt()`와 `Number()`의 차이를 이해하지 못한다.
- `undefined`와 `null`을 같은 의미로 사용한다.
- Truthy와 Falsy를 고려하지 않은 조건문을 작성한다.

---

# 면접 포인트

### 변수란 무엇인가?

메모리에 저장된 데이터를 참조하기 위한 이름(식별자)이다.

---

### `var`, `let`, `const`의 차이는?

- `var`는 함수 스코프이며 재선언이 가능하다.
- `let`은 블록 스코프이며 재할당이 가능하다.
- `const`는 블록 스코프이며 재할당이 불가능하다.

실무에서는 `const`를 기본으로 사용하고, 변경이 필요한 경우에만 `let`을 사용한다.

---

### JavaScript가 동적 타입 언어라는 의미는?

변수의 자료형이 실행 중에도 변경될 수 있다는 의미이다.

---

### 원시 타입과 참조 타입의 차이는?

원시 타입은 값을 직접 저장하고, 참조 타입은 객체의 참조를 저장한다.

---

### `undefined`와 `null`의 차이는?

- `undefined`는 값이 아직 할당되지 않은 상태이다.
- `null`은 개발자가 의도적으로 비어 있음을 표현한 값이다.

---

### `typeof null`의 결과가 `"object"`인 이유는?

JavaScript 초기 구현에서 비롯된 역사적인 호환성 문제로, 현재까지 유지되고 있다.

---

### `Number()`와 `parseInt()`의 차이는?

- `Number()`는 문자열 전체를 숫자로 변환하며 변환할 수 없으면 `NaN`을 반환한다.
- `parseInt()`는 앞에서부터 숫자를 읽다가 숫자가 아닌 문자를 만나면 변환을 종료한다.

---

### Truthy와 Falsy란?

조건문에서 `true` 또는 `false`처럼 평가되는 값의 특성을 의미한다.

대표적인 Falsy 값은 다음과 같다.

- `false`
- `0`
- `-0`
- `0n`
- `""`
- `null`
- `undefined`
- `NaN`

---

# 핵심 정리

- 변수는 데이터를 저장하고 참조하기 위한 식별자이다.
- `const`를 기본으로 사용하고 필요한 경우 `let`을 사용한다.
- JavaScript는 동적 타입 언어이다.
- 자료형은 원시 타입과 참조 타입으로 나뉜다.
- `typeof`로 자료형을 확인할 수 있다.
- `undefined`와 `null`은 서로 다른 의미를 가진다.
- 명시적 형 변환을 사용하는 것이 예측 가능한 코드를 작성하는 데 도움이 된다.
- Truthy와 Falsy를 이해하면 조건문을 더 효율적으로 작성할 수 있다.
- 원시 타입은 값이 복사되고, 참조 타입은 참조가 복사된다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
