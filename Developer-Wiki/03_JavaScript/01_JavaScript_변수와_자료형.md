---
title: JavaScript 변수와 자료형
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# JavaScript 변수와 자료형

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `01_JavaScript_변수와_자료형.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/01_var.html`, `workspace_teacher/workspace_html/javascript/01_var.html` |
| 핵심 범위 | JavaScript 실행, 주석, 콘솔, `var`, `let`, `const`, 동적 타입, `undefined`, `Infinity`, `NaN`, Boolean, 문자열, 템플릿 리터럴, 형 변환, 산술 계산 |
| 실습 범위 | 변수 선언·재할당, 문자열과 숫자 변환, 단위 계산, 회식비 분배, 브라우저 대화상자 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 한 번에 나열하지 않는다.  
> 변수와 자료형을 이해하는 데 필요한 부분만 발췌하고, 코드의 실행 결과·차이·오류 원인·실무 개선 방향을 함께 설명한다.

---

# 개요

JavaScript는 웹 페이지에 동작과 로직을 추가하는 프로그래밍 언어다.

```text
HTML
→ 문서 구조

CSS
→ 디자인과 배치

JavaScript
→ 계산, 조건 판단, 이벤트, 화면 변경
```

이번 문서에서는 JavaScript 코드를 실행하고, 값을 변수에 저장하며, 값의 자료형을 확인하고 변환하는 기본 흐름을 학습한다.

```text
값 준비
    ↓
변수에 저장
    ↓
필요하면 자료형 변환
    ↓
계산
    ↓
콘솔에서 결과 확인
```

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `<script>` | HTML 문서 안에서 JavaScript 실행 |
| `console.log()` | 개발자 도구 콘솔에 값 출력 |
| `var` | 재선언·재할당이 가능한 오래된 변수 선언 방식 |
| `let` | 재할당이 필요한 블록 스코프 변수 |
| `const` | 재할당하지 않는 블록 스코프 변수 |
| 동적 타입 | 변수에 저장되는 값의 타입이 실행 중 바뀔 수 있음 |
| `undefined` | 값이 아직 할당되지 않은 상태 |
| `null` | 의도적으로 값이 없음을 표현 |
| `Infinity` | 유한 범위를 넘어선 무한대 값 |
| `NaN` | 유효한 숫자 결과가 아님 |
| 템플릿 리터럴 | 백틱으로 문자열과 표현식을 함께 작성 |
| `Number()` | 전체 값을 숫자로 변환 |
| `parseInt()` | 문자열 앞부분에서 정수를 해석 |
| `String()` | 값을 문자열로 변환 |
| `typeof` | 값의 자료형 확인 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- HTML 문서에서 JavaScript를 실행할 수 있다.
- 한 줄 주석과 여러 줄 주석을 작성할 수 있다.
- `console.log()`와 `console.error()`의 역할을 구분할 수 있다.
- `alert()`, `confirm()`, `prompt()`의 반환값을 설명할 수 있다.
- 선언·할당·초기화·재할당·재선언을 구분할 수 있다.
- `var`, `let`, `const`의 차이를 설명할 수 있다.
- 실무에서 `const`를 우선 사용하는 이유를 이해한다.
- 선언 없이 값을 할당하는 코드의 위험을 설명할 수 있다.
- JavaScript가 동적 타입 언어라는 의미를 이해한다.
- `undefined`, `null`, `Infinity`, `NaN`을 구분할 수 있다.
- `typeof`로 값의 자료형을 확인할 수 있다.
- 문자열 연결과 템플릿 리터럴을 사용할 수 있다.
- `Number()`, `parseInt()`, `String()`의 차이를 설명할 수 있다.
- 나눗셈·나머지·몫 계산을 작성할 수 있다.
- 복합 대입 연산자를 사용할 수 있다.
- camelCase와 JavaScript 식별자 규칙을 이해한다.
- 계산 결과를 의미 있는 변수명과 단위로 출력할 수 있다.

---

# 1. JavaScript 실행 구조

## 1-1. 내 코드와 강사님 코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >
    <title>Document</title>

    <script>
        console.log("hello world")
    </script>
</head>
<body>
</body>
</html>
```

두 원본은 같은 HTML 구조에서 `<head>` 내부의 `<script>`로 JavaScript를 실행한다.

## 1-2. 실행 결과

브라우저 화면에는 별도 내용이 나타나지 않고 개발자 도구의 Console에 다음 값이 출력된다.

```text
hello world
```

## 1-3. 실무에서는?

JavaScript 코드가 길어지면 HTML과 분리한다.

```html
<script src="main.js" defer></script>
```

`defer`를 사용하면 HTML 파싱을 막지 않고 문서 구조가 준비된 뒤 스크립트를 실행할 수 있다.

---

# 2. 문서 언어와 제목

원본:

```html
<html lang="en">
<title>Document</title>
```

학습 문서가 한국어이고 주제도 명확하므로 다음처럼 개선할 수 있다.

```html
<html lang="ko">
<title>JavaScript 변수와 자료형</title>
```

`lang`은 문서의 기본 언어를 나타내며 접근성 도구와 검색 엔진이 문서를 이해하는 데 도움을 준다.

---

# 3. 한 줄 주석

## 3-1. 원본 코드

```javascript
// 한줄 주석
```

`//`부터 줄 끝까지 실행되지 않는다.

```javascript
const userCount = 3 // 현재 로그인 사용자 수
```

## 3-2. 주석 작성 기준

좋지 않은 예:

```javascript
const userCount = 3 // userCount에 3을 넣는다
```

개선:

```javascript
// 관리자 계정은 집계에서 제외한다.
const userCount = 3
```

> [!TIP]
> 주석은 코드가 **무엇을 하는지** 반복하기보다 **왜 이렇게 작성했는지** 설명할 때 더 유용하다.

---

# 4. 여러 줄 주석

## 4-1. 원본 코드

```javascript
/*
    여러줄 주석
    범위 주석
*/
```

`/*`와 `*/` 사이를 주석 처리한다.

## 4-2. 주의점

JavaScript 여러 줄 주석은 일반적으로 중첩할 수 없다.

```text
/*
    바깥 주석
    /* 안쪽 주석 */
*/
```

중간의 `*/`에서 주석이 먼저 종료되어 문법 문제가 생길 수 있다.

---

# 5. `console.log()`

## 5-1. 원본 코드

```javascript
console.log("hello world")
console.log(a)
console.log(11)
```

`console.log()`는 개발자 도구 콘솔에 값을 출력한다.

## 5-2. 여러 값 출력

```javascript
const userName = "Kim"
const userAge = 21

console.log("이름:", userName, "나이:", userAge)
```

## 5-3. 출력 결과

```text
이름: Kim 나이: 21
```

객체나 배열을 확인할 때는 문자열로 억지로 연결하기보다 값을 별도 인자로 전달하는 방식이 편리하다.

---

# 6. `console.error()`

## 6-1. 원본 코드

```javascript
console.error("아무거나")
```

내 코드에는 다음 설명이 추가되어 있다.

```javascript
// error처럼 보이게 강제로 출력할 수 있다
```

`console.error()`는 오류 스타일의 메시지를 콘솔에 출력한다.

```javascript
console.error("사용자 정보를 불러오지 못했습니다.")
```

> [!IMPORTANT]
> `console.error()`를 호출했다고 실제 JavaScript 오류가 발생한 것은 아니다.
>
> 메시지를 오류 형태로 표시할 뿐, 기본적으로 다음 코드는 계속 실행된다.

---

# 7. `alert()`

## 7-1. 원본 코드

```javascript
// alert("hello 엔터\n world")
```

`alert()`는 확인 버튼이 있는 브라우저 대화상자를 표시한다.

```javascript
alert("첫 번째 줄\n두 번째 줄")
```

`\n`은 줄바꿈 문자다.

## 7-2. 실무에서는?

`alert()`는 사용자가 닫을 때까지 화면 상호작용을 막는다.

실제 서비스에서는 다음 요소를 더 자주 사용한다.

- 모달
- 토스트 메시지
- 화면 내부 오류 문구
- 알림 컴포넌트

---

# 8. `confirm()`

## 8-1. 원본 코드

```javascript
// const result = confirm("할래말래")
// console.log("confirm 결과:", result)
```

## 8-2. 반환값

```text
확인
→ true

취소
→ false
```

## 8-3. 실행 예시

```javascript
const shouldDelete = confirm("정말 삭제하시겠습니까?")

console.log(shouldDelete)
```

사용자의 선택 결과는 Boolean 값으로 저장된다.

---

# 9. `prompt()`

## 9-1. 원본 코드

```javascript
// const password = prompt("비번을 입력하세요")
// console.log("prompt 결과:", password, "입니다")
```

## 9-2. 반환값

```text
문자 입력 후 확인
→ string

빈칸으로 확인
→ ""

취소
→ null
```

## 9-3. 주의점

`prompt()`로 숫자를 입력해도 결과는 문자열이다.

```javascript
const age = prompt("나이를 입력하세요")

console.log(typeof age)
```

입력값이 `20`이어도 결과:

```text
string
```

---

# 10. 변수란?

변수는 값을 저장하고 다시 사용할 수 있도록 이름을 붙인 식별자다.

```javascript
let count = 10
```

## 10-1. 구성

| 요소 | 의미 |
| --- | --- |
| `let` | 변수 선언 키워드 |
| `count` | 변수 이름 |
| `=` | 오른쪽 값을 왼쪽 변수에 할당 |
| `10` | 저장할 Number 값 |

---

# 11. 선언·할당·초기화

선언:

```javascript
let count
```

할당:

```javascript
count = 10
```

선언과 동시에 초기화:

```javascript
let count = 10
```

```text
선언
→ 변수 이름 준비

할당
→ 값 저장

초기화
→ 선언 후 처음 값 저장
```

---

# 12. 원본의 첫 번째 `a = 15`

## 12-1. 원본 코드

```javascript
a = 15
console.log(a)

var a = 10
```

이 코드가 실행되는 이유는 같은 스코프의 `var a` 선언이 호이스팅되기 때문이다.

개념적으로 다음과 비슷하다.

```javascript
var a

a = 15
console.log(a)

a = 10
```

## 12-2. 주의점

초기화 값 `10`까지 위로 이동하는 것은 아니다.

> [!WARNING]
> 호이스팅에 의존해 선언 전에 변수를 사용하는 코드는 실행 순서를 이해하기 어렵게 만든다.
>
> 변수는 사용 전에 선언한다.

---

# 13. `var`

## 13-1. 원본 코드

```javascript
var a = 10
var b = 20
```

`var`의 특징:

- 같은 스코프에서 재선언 가능
- 재할당 가능
- 함수 스코프
- 선언이 호이스팅됨

현대 JavaScript에서는 일반적으로 `const`와 `let`을 우선 사용한다.

---

# 14. `var` 재할당

```javascript
var a = 10

a = 30

console.log(a)
```

출력:

```text
30
```

이미 선언한 변수에 새 값을 저장하는 것을 재할당이라고 한다.

---

# 15. `var` 재선언

## 15-1. 원본 코드

```javascript
var a = 10
var a = 40

console.log(a)
```

## 15-2. 출력 결과

```text
40
```

같은 스코프에서 재선언해도 오류가 발생하지 않는다.

이 특성은 오타나 중복 선언을 놓치기 쉽게 만든다.

---

# 16. 선언 없는 할당

## 16-1. 원본 코드

```javascript
c = 50

console.log(c)
```

원본의 `// 타입 없음`이라는 설명은 정확하지 않다.

`50`은 Number 타입이다. 문제는 **선언 키워드 없이 값을 할당했다는 것**이다.

## 16-2. 위험

- 의도하지 않은 전역 속성 생성
- 변수명 충돌
- 오타 탐지 어려움
- strict mode에서 오류
- ES module에서 오류

## 16-3. 개선

```javascript
const c = 50
```

값이 바뀐다면:

```javascript
let c = 50
```

---

# 17. Strict mode

```javascript
"use strict"

c = 50
```

발생 결과:

```text
ReferenceError: c is not defined
```

Strict mode는 선언하지 않은 변수 사용처럼 오류 가능성이 높은 동작을 제한한다.

ES module은 기본적으로 Strict mode로 실행된다.

---

# 18. `let`

## 18-1. 원본 코드

```javascript
let d = 60

console.log(d)
```

`let`의 특징:

- 같은 스코프에서 재선언 불가
- 재할당 가능
- 블록 스코프
- 선언 전에 접근할 수 없음

값이 이후에 바뀌어야 할 때 사용한다.

---

# 19. `let` 재할당

```javascript
let d = 60

d = 65

console.log(d)
```

출력:

```text
65
```

`let`은 재선언을 막지만 재할당은 허용한다.

---

# 20. `let` 재선언 오류

```text
let d = 60
let d = 70
```

발생 결과:

```text
SyntaxError: Identifier 'd' has already been declared
```

같은 스코프에서 동일한 이름을 다시 선언할 수 없다.

---

# 21. `const`

## 21-1. 원본 코드

```javascript
const e = 70

console.log(e)
```

`const`의 특징:

- 같은 스코프에서 재선언 불가
- 재할당 불가
- 블록 스코프
- 선언과 동시에 초기화 필요

> [!IMPORTANT]
> 실무에서는 기본적으로 `const`를 먼저 사용하고, 값이 다시 할당되어야 할 때만 `let`을 사용한다.

---

# 22. `const` 재할당 오류

```text
const e = 70
e = 75
```

발생 결과:

```text
TypeError: Assignment to constant variable.
```

변수 바인딩을 다른 값으로 바꿀 수 없다.

---

# 23. `const` 초기값

## 23-1. 원본의 오류 예제

```text
const f
f = 80
```

발생 결과:

```text
SyntaxError: Missing initializer in const declaration
```

올바른 코드:

```javascript
const f = 80
```

---

# 24. `const` 객체의 내부 변경

`const`는 값 전체를 완전히 불변으로 만드는 문법이 아니다.

```javascript
const user = {
    name: "Kim",
}

user.name = "Lee"

console.log(user.name)
```

출력:

```text
Lee
```

불가능한 것은 변수에 새로운 객체를 재할당하는 것이다.

```text
user = {}
```

발생 결과:

```text
TypeError
```

---

# 25. `var`, `let`, `const` 비교

| 항목 | `var` | `let` | `const` |
| --- | --- | --- | --- |
| 재선언 | 가능 | 불가 | 불가 |
| 재할당 | 가능 | 가능 | 불가 |
| 스코프 | 함수 | 블록 | 블록 |
| 선언 시 초기값 | 선택 | 선택 | 필수 |
| 현대 코드 권장 | 제한적 | 값 변경 시 | 기본 우선 |

실무 선택 기준:

```text
기본
→ const

값을 다시 대입해야 함
→ let

기존 코드 유지보수 등 특별한 이유
→ var
```

---

# 26. 동적 타입

## 26-1. 원본 코드

```javascript
let d = 60

d = "문자"

console.log(d)
```

## 26-2. 출력 결과

```text
문자
```

같은 변수에 Number를 저장했다가 String을 다시 저장할 수 있다.

JavaScript는 타입이 없는 언어가 아니라 **동적 타입 언어**다.

```text
변수에 고정 타입이 붙는 것이 아님
    ↓
현재 저장된 값이 타입을 가짐
```

---

# 27. `typeof`

```javascript
console.log(typeof 10)
console.log(typeof "10")
console.log(typeof true)
console.log(typeof undefined)
```

출력:

```text
number
string
boolean
undefined
```

`typeof`는 값의 자료형을 문자열로 반환한다.

---

# 28. Number 타입

JavaScript의 일반 숫자는 정수와 실수를 구분하지 않고 대부분 `number` 타입으로 처리한다.

```javascript
console.log(typeof 10)
console.log(typeof 10.5)
```

출력:

```text
number
number
```

---

# 29. String 타입

```javascript
const userName = "Kim"
const message = 'Hello'

console.log(typeof userName)
console.log(typeof message)
```

출력:

```text
string
string
```

작은따옴표와 큰따옴표 모두 문자열을 만든다.

---

# 30. Boolean 타입

## 30-1. 원본 코드

```javascript
const isActive = true
const isDeleted = false
```

Boolean은 참과 거짓을 표현한다.

실무 예:

```javascript
const isLoggedIn = true
const hasPermission = false
```

변수명에 `is`, `has`, `can`, `should` 등을 사용하면 Boolean 값임을 알기 쉽다.

---

# 31. `undefined`

## 31-1. 원본 코드

```javascript
let y

console.log(y)
```

## 31-2. 출력 결과

```text
undefined
```

변수는 선언되었지만 값이 할당되지 않았다.

```javascript
console.log(typeof y)
```

출력:

```text
undefined
```

---

# 32. `not defined`와 `undefined`

원본에는 다음 코드가 주석 처리되어 있다.

```javascript
// console.log(z)
```

`z`가 선언되지 않았다면 다음 오류가 발생한다.

```text
ReferenceError: z is not defined
```

차이:

```text
let y
→ 선언됨, 값 없음
→ undefined

z
→ 선언 자체가 없음
→ ReferenceError
```

---

# 33. `null`

`null`은 개발자가 의도적으로 값이 없음을 표현할 때 사용한다.

```javascript
const selectedUser = null
```

`prompt()`에서 취소를 눌러도 `null`이 반환된다.

## 33-1. `typeof null`

```javascript
console.log(typeof null)
```

출력:

```text
object
```

이는 오래된 JavaScript의 역사적 동작이다.

`null` 확인에는 다음처럼 직접 비교한다.

```javascript
selectedUser === null
```

---

# 34. `Infinity`

## 34-1. 원본 코드

```javascript
console.log(7 / 0)
```

## 34-2. 출력 결과

```text
Infinity
```

JavaScript의 Number 연산에서는 0으로 나눌 때 예외가 아니라 `Infinity`가 나올 수 있다.

검사:

```javascript
const result = 7 / 0

console.log(Number.isFinite(result))
```

출력:

```text
false
```

---

# 35. `NaN`

## 35-1. 원본 코드

```javascript
console.log(7 * "문자")
```

## 35-2. 출력 결과

```text
NaN
```

`NaN`은 Not a Number의 약자이며 유효한 숫자 결과가 아님을 나타낸다.

```javascript
console.log(typeof NaN)
```

출력:

```text
number
```

> [!IMPORTANT]
> `NaN`은 이름과 달리 Number 타입의 특수값이다.

---

# 36. `NaN` 검사

```javascript
const result = Number("10개")

console.log(Number.isNaN(result))
```

출력:

```text
true
```

다음 비교는 사용할 수 없다.

```javascript
result === NaN
```

항상 `false`다.

권장:

```javascript
Number.isNaN(result)
```

---

# 37. 템플릿 리터럴

## 37-1. 원본 코드

```javascript
console.log(`백틱
엔터 가능
${a}
`)
```

백틱 `` ` `` 으로 문자열을 만들면 줄바꿈과 표현식 삽입이 가능하다.

## 37-2. 실행

```javascript
const userName = "Kim"
const age = 21

console.log(`${userName}님의 나이는 ${age}세입니다.`)
```

## 37-3. 출력 결과

```text
Kim님의 나이는 21세입니다.
```

---

# 38. 문자열 연결과 템플릿 리터럴

원본:

```javascript
console.log("a :" + a)
console.log(`a : ${a}`)
```

비교:

| 방식 | 특징 |
| --- | --- |
| `"a: " + a` | 문자열 연결 |
| `` `a: ${a}` `` | 값의 위치가 명확함 |

여러 값을 포함하는 문자열은 템플릿 리터럴이 더 읽기 쉬운 경우가 많다.

---

# 39. 문자열과 숫자의 `+`

## 39-1. 원본 코드

```javascript
const strA = "10.1"

console.log(strA + 2)
```

## 39-2. 출력 결과

```text
10.12
```

한쪽이 문자열이면 `+`는 숫자 덧셈이 아니라 문자열 연결로 동작할 수 있다.

```text
"10.1" + 2
→ "10.1" + "2"
→ "10.12"
```

---

# 40. `Number()`

## 40-1. 원본 코드

```javascript
const strA = "10.1"

const numA = Number(strA) + 2

console.log(numA)
```

## 40-2. 출력 결과

```text
12.1
```

`Number()`는 문자열 전체가 유효한 숫자 형식인지 해석한다.

```javascript
console.log(Number("10개"))
```

출력:

```text
NaN
```

---

# 41. `parseInt()`

## 41-1. 원본 코드

```javascript
console.log(parseInt("10.1"))
console.log(parseInt("10개"))
```

## 41-2. 출력 결과

```text
10
10
```

`parseInt()`는 문자열 앞부분에서 정수로 해석할 수 있는 부분을 읽는다.

```text
"10.1"
→ 10

"10개"
→ 10

"개10"
→ NaN
```

---

# 42. `Number()`와 `parseInt()` 비교

| 입력 | `Number()` | `parseInt()` |
| --- | ---: | ---: |
| `"10"` | `10` | `10` |
| `"10.1"` | `10.1` | `10` |
| `"10개"` | `NaN` | `10` |
| `""` | `0` | `NaN` |
| `"개10"` | `NaN` | `NaN` |

선택 기준:

```text
전체 문자열이 숫자여야 함
→ Number()

앞쪽 정수만 추출하는 요구사항
→ parseInt()
```

> [!WARNING]
> 사용자 입력 검증을 위해 무조건 `parseInt()`를 사용하면 `"10개"` 같은 잘못된 값도 `10`으로 통과할 수 있다.

---

# 43. 진법 지정

`parseInt()`의 두 번째 인자로 진법을 명시할 수 있다.

```javascript
console.log(parseInt("10", 10))
console.log(parseInt("10", 2))
```

출력:

```text
10
2
```

일반적인 십진 정수 변환에는 다음처럼 작성한다.

```javascript
parseInt(value, 10)
```

---

# 44. `String()`

## 44-1. 원본 코드

```javascript
console.log(String(numA))
console.log("" + numA)
```

두 방식 모두 숫자를 문자열로 만들 수 있다.

## 44-2. 권장 방식

```javascript
const text = String(numA)
```

명시적 변환은 코드의 의도를 더 잘 보여 준다.

템플릿 리터럴을 사용할 수도 있다.

```javascript
const text = `${numA}`
```

---

# 45. 암시적 형 변환

JavaScript는 연산 과정에서 값을 자동 변환하기도 한다.

```javascript
console.log("5" - 2)
console.log("5" * 2)
console.log("5" + 2)
```

출력:

```text
3
10
52
```

`+`는 문자열 연결에도 사용되므로 다른 산술 연산자와 결과가 다를 수 있다.

> [!IMPORTANT]
> 암시적 형 변환에 의존하면 결과를 예측하기 어려울 수 있다.
>
> 사용자 입력은 계산 전에 명시적으로 변환하고 검증한다.

---

# 46. 변수 이름 표기법

## 46-1. camelCase

원본:

```javascript
let salesCount = 1
```

JavaScript 변수와 함수 이름에 일반적으로 사용한다.

```text
userName
totalPrice
isLoggedIn
```

## 46-2. snake_case

원본:

```javascript
let sales_count = 1
```

문법적으로 사용할 수 있지만 프로젝트 규칙을 일관되게 따른다.

## 46-3. kebab-case

원본:

```javascript
// let font-size = 2
```

JavaScript 변수명에는 사용할 수 없다.

`-`가 빼기 연산자로 해석되기 때문이다.

kebab-case는 주로 다음에 사용한다.

- CSS 클래스명
- HTML 속성값
- 파일명
- URL 경로

---

# 47. 식별자 규칙

JavaScript 식별자는 일반적으로 다음 문자를 사용할 수 있다.

- 영문자
- 숫자
- `_`
- `$`
- 유니코드 문자

숫자로 시작할 수 없다.

```javascript
const count1 = 1
const _count = 2
const $count = 3
const 잔고 = 15000
```

잘못된 예:

```text
const 1count = 1
```

---

# 48. 한글 변수명

원본:

```javascript
let 밭 = 10
let 잔고 = 15000
let 번돈 = 100000
```

JavaScript는 한글 식별자를 허용한다.

학습 예제에서는 의미를 빠르게 이해할 수 있지만, 실무에서는 팀 규칙과 생태계 일관성을 고려해 영어 camelCase를 많이 사용한다.

개선:

```javascript
const fieldSize = 10
let balance = 15000
const earnedMoney = 100000
```

---

# 49. 산술 연산

```javascript
console.log(7 / 3)
console.log(7 % 3)
```

출력:

```text
2.3333333333333335
1
```

| 연산자 | 의미 |
| --- | --- |
| `+` | 덧셈 |
| `-` | 뺄셈 |
| `*` | 곱셈 |
| `/` | 나눗셈 |
| `%` | 나머지 |
| `**` | 거듭제곱 |

---

# 50. 몫 구하기

## 50-1. 원본 코드

```javascript
console.log("몫:", parseInt(7 / 3))
```

출력:

```text
몫: 2
```

양수 계산에서는 원하는 결과가 나오지만, 숫자를 문자열 파싱 함수인 `parseInt()`로 처리하는 것은 목적이 명확하지 않다.

권장:

```javascript
console.log(Math.trunc(7 / 3))
```

출력:

```text
2
```

## 50-2. 음수 주의

```javascript
console.log(Math.trunc(-7 / 3))
console.log(Math.floor(-7 / 3))
```

출력:

```text
-2
-3
```

`Math.trunc()`는 소수 부분 제거, `Math.floor()`는 아래 정수로 내린다.

---

# 51. 복합 대입 연산자

## 51-1. 원본 코드

```javascript
let balance = 15000
const earnedMoney = 100000

balance = balance + earnedMoney
balance += earnedMoney
```

`+=`는 기존 값에 더한 결과를 같은 변수에 다시 저장한다.

```javascript
balance += earnedMoney
```

다음 코드와 같은 의미다.

```javascript
balance = balance + earnedMoney
```

기타 예:

```javascript
count -= 1
price *= 2
total /= 3
```

---

# 52. 원본의 증가 계산

```javascript
a = 10
a = a + 1
```

복합 대입:

```javascript
a += 1
```

증감 연산자:

```javascript
a++
```

세 방식 모두 값을 1 증가시킬 수 있지만, 반환값 차이가 필요한 상황이 아니라면 `a += 1`이 의도를 명확하게 보여 주는 경우가 많다.

---

# 53. 단위 계산

## 53-1. 원본 코드

```javascript
const pyeongSquareMeter = 3.3
const acreSquareMeter = 4046.8
const fieldSize = 10

console.log(
    "단위가 평일 때:",
    fieldSize * pyeongSquareMeter,
)

console.log(
    "단위가 에이커일 때:",
    fieldSize * acreSquareMeter,
)
```

## 53-2. 출력 결과

```text
단위가 평일 때: 33
단위가 에이커일 때: 40468
```

## 53-3. 82제곱미터를 평으로 변환

```javascript
const squareMeters = 82
const pyeong = squareMeters / pyeongSquareMeter

console.log(pyeong)
```

출력 근사값:

```text
24.84848484848485
```

표시 자리수를 제한하려면:

```javascript
console.log(pyeong.toFixed(2))
```

출력:

```text
24.85
```

---

# 54. 회식비 나누기

## 54-1. 내 코드

```javascript
const totalCost = 100000
const peopleCount = 9

const remainder = totalCost % peopleCount
const pricePerPerson = Math.trunc(
    totalCost / peopleCount,
)

const organizerPrice = (
    pricePerPerson + remainder
)

console.log("나머지:", remainder)
console.log("인당:", pricePerPerson)
console.log("주최자:", organizerPrice)
```

## 54-2. 출력 결과

```text
나머지: 1
인당: 11111
주최자: 11112
```

## 54-3. 강사님 코드

강사님 원본에는 계산 문제의 안내만 있고 결과식은 비어 있다.

```javascript
console.log("인당:")
console.log("주최자가 조금 더 낼 때 얼마?")
```

내 코드는 나머지를 주최자가 부담하는 방식으로 계산을 완성했다.

## 54-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `%` | 균등 분배 후 남는 금액 계산 |
| `/` | 1인당 금액 계산 |
| `Math.trunc()` | 소수 부분 제거 |
| `const` | 계산 중 다시 할당하지 않는 값 |
| 의미 있는 변수명 | 금액의 역할을 명확하게 표현 |

---

# 55. 여러 변수 선언

## 55-1. 원본 코드

```javascript
let a1 = 10
let a2 = 20
let a3 = 30
```

쉼표로 이어서 선언할 수도 있다.

```javascript
let b1 = 10,
    b2 = 20,
    b3 = 30
```

## 55-2. 실무에서는?

각 변수의 의미가 다르면 한 줄에 하나씩 선언하는 편이 수정과 코드 리뷰에 유리하다.

```javascript
const minScore = 10
const maxScore = 20
const defaultScore = 30
```

---

# 56. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기본 구조 | 동일 | 동일 |
| 변수 선언 | `var·let·const` 비교 | 동일 |
| 선언 없는 할당 | `타입 없음` 메모 | 동일 |
| 특수값 | `undefined`, `Infinity`, `NaN` | 동일 |
| 형 변환 | `Number()`, `parseInt()`, `String()` | 동일 |
| 회식비 문제 | 실제 계산식 완성 | 문제 문구만 출력 |
| 나머지 연산 | 역할 설명 추가 | 기본 출력 |
| `prompt()` | 취소 시 `null` 설명 추가 | 실행 예제 중심 |
| 다중 선언 | 쉼표 선언 설명 추가 | 선언 코드 중심 |
| `console.error()` | 오류처럼 표시된다는 설명 추가 | 기본 호출 |

## 56-1. 내 코드의 장점

- 회식비 분배 문제를 실제 계산식으로 완성했다.
- `prompt()` 취소 시 `null` 반환을 기록했다.
- 나머지 연산과 다중 변수 선언의 의미를 메모했다.
- `console.error()`가 오류 스타일 메시지를 출력한다는 점을 기록했다.

## 56-2. 내 코드의 개선점

- 선언 없는 `c = 50`은 “타입 없음”이 아니라 선언 누락이다.
- 몫 계산에는 `parseInt()`보다 `Math.trunc()`가 목적에 맞다.
- 한글 변수명은 영어 camelCase로 정리하면 협업에 유리하다.
- 같은 변수 `a`를 여러 개념에 반복 사용하면 실행 흐름을 추적하기 어렵다.
- 기본은 `const`, 재할당이 필요할 때만 `let`을 사용하면 의도가 명확하다.

## 56-3. 강사님 코드의 장점

- JavaScript 첫 수업에서 변수·자료형·형 변환·계산을 한 흐름으로 확인할 수 있다.
- 오류 가능성이 있는 코드를 주석 처리해 정상 코드와 비교할 수 있다.
- 브라우저 대화상자와 콘솔 출력까지 함께 실습한다.

## 56-4. 강사님 코드의 보충점

- `var`·`let`·`const`의 스코프와 현대 코드 선택 기준이 필요하다.
- 선언 없는 할당과 Strict mode의 관계를 설명할 필요가 있다.
- `NaN`과 `Infinity`를 검사하는 방법을 보충할 수 있다.
- 회식비 문제에 실제 계산 결과가 있으면 학습 효과가 높다.

---

# 57. 기존 코드에서 개선 코드로 바꾼 이유

## 57-1. `var`에서 `const`·`let`으로

기존:

```javascript
var a = 10
var b = 20
```

개선:

```javascript
let currentValue = 10
const limit = 20
```

이유:

- 재선언 실수를 방지한다.
- 값이 변경되는지 코드에서 바로 알 수 있다.
- 블록 스코프로 변수 범위를 줄일 수 있다.

## 57-2. 선언 없는 할당 제거

기존:

```javascript
c = 50
```

개선:

```javascript
const c = 50
```

## 57-3. 문자열 연결 개선

기존:

```javascript
console.log("a : " + a)
```

개선:

```javascript
console.log(`a: ${a}`)
```

## 57-4. 몫 계산 개선

기존:

```javascript
parseInt(totalCost / peopleCount)
```

개선:

```javascript
Math.trunc(
    totalCost / peopleCount,
)
```

---

# 58. 실무형 예제: 주문 금액 계산

```javascript
const productName = "키보드"
const unitPrice = 45000
const quantityText = "2"

const quantity = Number(quantityText)

if (
    Number.isNaN(quantity)
    || quantity <= 0
) {
    console.error(
        "수량은 1 이상의 숫자여야 합니다.",
    )
} else {
    const totalPrice = (
        unitPrice * quantity
    )

    console.log(
        `${productName} ${quantity}개`,
    )

    console.log(
        `총 결제 금액: ${totalPrice.toLocaleString()}원`,
    )
}
```

## 58-1. 입력값

```text
quantityText = "2"
```

## 58-2. 출력 결과

```text
키보드 2개
총 결제 금액: 90,000원
```

## 58-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `const` | 계산 중 다시 할당하지 않는 값 |
| `Number()` | 문자열 수량을 숫자로 변환 |
| `Number.isNaN()` | 숫자 변환 실패 검사 |
| `if` | 잘못된 수량과 정상 수량 분기 |
| 템플릿 리터럴 | 값이 포함된 메시지 작성 |
| `toLocaleString()` | 천 단위 구분 기호 표시 |

---

# 59. 대표 오류로 이해하기

## 59-1. 선언되지 않은 변수

```text
console.log(userName)
```

발생 결과:

```text
ReferenceError: userName is not defined
```

---

## 59-2. `let` 재선언

```text
let count = 1
let count = 2
```

발생 결과:

```text
SyntaxError
```

---

## 59-3. `const` 재할당

```text
const count = 1
count = 2
```

발생 결과:

```text
TypeError
```

---

## 59-4. `const` 초기값 누락

```text
const count
```

발생 결과:

```text
SyntaxError
```

---

## 59-5. 숫자 변환 실패

```javascript
const result = Number("10개")

console.log(result)
```

출력:

```text
NaN
```

예외가 발생하지 않으므로 `Number.isNaN()`으로 직접 검사해야 한다.

---

## 59-6. kebab-case 변수명

```text
const total-price = 1000
```

발생 결과:

```text
SyntaxError
```

JavaScript에서는 `totalPrice`를 사용한다.

---

# 60. 자주 하는 실수

## 60-1. `var`를 기본 변수 선언으로 사용

현대 코드에서는 `const`와 `let`을 우선 고려한다.

## 60-2. 값이 바뀌지 않는데 `let` 사용

재할당 의도가 없다면 `const`가 더 명확하다.

## 60-3. 선언 키워드 없이 값 할당

전역 오염이나 `ReferenceError`의 원인이 된다.

## 60-4. JavaScript는 타입이 없다고 이해

값은 각각 자료형을 가진다.

## 60-5. `undefined`와 미선언 변수를 같은 상태로 이해

미선언 변수 접근은 `ReferenceError`가 발생한다.

## 60-6. `null`의 `typeof`가 `"null"`이라고 생각

실제 결과는 역사적 이유로 `"object"`다.

## 60-7. `NaN === NaN`으로 검사

항상 `false`이므로 `Number.isNaN()`을 사용한다.

## 60-8. `Number()`와 `parseInt()`를 같은 함수로 이해

문자열 전체 변환과 앞부분 정수 해석이라는 차이가 있다.

## 60-9. `prompt()` 결과를 바로 숫자로 계산

문자열 또는 `null`이므로 먼저 검사하고 변환한다.

## 60-10. 숫자와 문자열의 `+`를 항상 덧셈으로 생각

문자열 연결이 될 수 있다.

## 60-11. 몫 계산에 `parseInt()` 사용

숫자 소수 부분 제거는 `Math.trunc()`가 더 직접적이다.

## 60-12. `const` 객체는 내부 값도 바꿀 수 없다고 생각

재할당은 불가능하지만 객체 속성은 변경될 수 있다.

---

# 61. 핵심 요약

```text
var
→ 재선언·재할당 가능
→ 현대 코드에서는 사용 최소화

let
→ 재할당 가능
→ 블록 스코프

const
→ 재할당 불가
→ 기본 우선
```

```text
undefined
→ 선언되었지만 값 없음

null
→ 의도적으로 값 없음

Infinity
→ 무한대 값

NaN
→ 유효한 숫자 결과가 아님
```

```text
Number()
→ 전체 값을 숫자로 변환

parseInt()
→ 앞부분에서 정수 해석

String()
→ 문자열 변환

typeof
→ 자료형 확인
```

```text
`${value}`
→ 템플릿 리터럴

%
→ 나머지

Math.trunc()
→ 소수 부분 제거

+=
→ 기존 값에 더해 재할당
```

---

# 62. 최종 체크리스트

- [ ] HTML 문서에서 JavaScript를 실행할 수 있는가?
- [ ] 한 줄·여러 줄 주석을 작성할 수 있는가?
- [ ] `console.log()`와 `console.error()`를 구분할 수 있는가?
- [ ] `alert()`, `confirm()`, `prompt()`의 반환값을 설명할 수 있는가?
- [ ] 선언·할당·초기화·재할당·재선언을 구분할 수 있는가?
- [ ] `var`, `let`, `const`의 차이를 설명할 수 있는가?
- [ ] 기본적으로 `const`를 우선 사용할 수 있는가?
- [ ] 선언 없는 할당의 위험을 이해했는가?
- [ ] 동적 타입의 의미를 설명할 수 있는가?
- [ ] `typeof`로 자료형을 확인할 수 있는가?
- [ ] `undefined`와 미선언 변수를 구분할 수 있는가?
- [ ] `null`, `Infinity`, `NaN`을 설명할 수 있는가?
- [ ] `Number.isNaN()`으로 변환 실패를 확인할 수 있는가?
- [ ] 템플릿 리터럴로 값을 문자열에 삽입할 수 있는가?
- [ ] 문자열과 숫자의 `+` 동작을 예측할 수 있는가?
- [ ] `Number()`, `parseInt()`, `String()`을 구분할 수 있는가?
- [ ] camelCase로 의미 있는 변수명을 작성할 수 있는가?
- [ ] `%`로 나머지를 계산할 수 있는가?
- [ ] `Math.trunc()`로 몫의 정수 부분을 구할 수 있는가?
- [ ] 복합 대입 연산자를 사용할 수 있는가?
- [ ] 사용자 입력을 계산 전에 검사하고 변환할 수 있는가?

---

# 마무리

변수와 자료형의 핵심은 값을 단순히 저장하는 것에서 끝나지 않는다.

```text
값의 목적에 맞는 이름을 만들고
    ↓
const와 let을 올바르게 선택하고
    ↓
현재 값의 자료형을 이해하고
    ↓
필요한 시점에 명시적으로 변환하고
    ↓
검증된 값으로 계산하는 것
```

이 기본 흐름을 이해하면 다음 연산자 문서에서 값의 비교와 논리 판단을 더 안정적으로 작성할 수 있다.
# V3 실행 추적 카드 — 리터럴/입력 → 값과 변수

`let`은 재할당 가능, `const`는 이름의 재할당을 막는다. `prompt()`와 폼의 `value`는 숫자처럼 보여도 문자열이므로 계산 전 `Number()` 등으로 변환한다.

`const raw = "10"; console.log(raw + 1, Number(raw) + 1, typeof raw);`의 Console 결과는 `101 11 string`이다. 선언 전 접근, 잘못된 변환에서 `ReferenceError` 또는 `NaN`을 확인한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/01_var.html`에서 실제 사용 위치와 차이를 확인한다.
