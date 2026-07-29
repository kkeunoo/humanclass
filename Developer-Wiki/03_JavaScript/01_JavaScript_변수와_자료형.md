# JavaScript 변수와 자료형

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `01_JavaScript_변수와_자료형.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `02_CSS/15_CSS_Flexbox와_유연한_레이아웃.md` |
| 다음 학습 | `02_JavaScript_연산자.md` |
| 원본 기준 | `workspace_me/workspace/workspace_html/javascript/01_var.html`, `workspace_teacher/workspace_teacher/workspace_html/javascript/01_var.html` |
| 핵심 범위 | 주석, 콘솔 출력, `var`, `let`, `const`, 재선언·재할당, 동적 타입, `undefined`, `Infinity`, `NaN`, 문자열, 템플릿 리터럴, 형 변환, 산술 계산 |
| 프로젝트 연결 | 사용자 입력 저장, 계산 결과 출력, 폼 값 변환, 금액 계산, 디버깅, 상태값 관리 |

> 이 문서는 내 코드와 강사님 코드의 `01_var.html`을 직접 비교해 작성했습니다. 두 파일은 대부분 동일하지만, 내 코드에는 나머지 연산 설명, 회식비 문제 풀이, `confirm`·`prompt` 설명, 다중 변수 선언 설명, `console.error()` 설명이 추가되어 있습니다. 강사님 원본의 `100000만원` 표현은 그대로 기록하고, 내 코드에서 `100,000원`으로 바뀐 차이를 설명합니다.

---

# 학습 목표

- JavaScript를 HTML 문서 안에서 실행하는 기본 구조를 이해한다.
- 한 줄 주석과 여러 줄 주석을 작성한다.
- `console.log()`, `console.error()`, `alert()`, `confirm()`, `prompt()`의 역할을 구분한다.
- 변수 선언과 값 할당의 차이를 설명한다.
- `var`, `let`, `const`의 재선언과 재할당 차이를 이해한다.
- 선언 없이 식별자에 값을 넣는 코드가 왜 위험한지 설명한다.
- JavaScript가 동적 타입 언어라는 의미를 이해한다.
- `undefined`, `Infinity`, `NaN`, Boolean 값을 구분한다.
- 문자열 연결과 템플릿 리터럴을 작성한다.
- `Number()`, `parseInt()`, `String()`의 차이를 설명한다.
- 나눗셈, 나머지, 몫 계산을 작성한다.
- 복합 할당 연산자를 사용한다.
- 변수 이름의 camelCase, snake_case, kebab-case 차이를 이해한다.
- 내 코드와 강사님 코드의 차이 및 원본의 부정확한 표현을 찾는다.
- 원본 코드를 수정하지 않고 문제점과 개선안을 구분해 설명한다.

---

# 1. JavaScript란?

JavaScript는 웹 페이지에 동작과 로직을 추가하는 프로그래밍 언어입니다.

HTML이 구조를 만들고 CSS가 디자인을 담당한다면 JavaScript는 다음과 같은 기능을 처리합니다.

```text
버튼 클릭 처리
사용자 입력 확인
계산
화면 내용 변경
서버와 데이터 통신
조건에 따른 동작
```

원본은 HTML 문서의 `<head>` 안에 `<script>`를 작성해 JavaScript를 실행합니다.

```html
<head>
  ...
  <script>
    console.log("hello world")
  </script>
</head>
```

---

# 2. 원본 문서 구조

내 코드와 강사님 코드 모두 다음 구조를 사용합니다.

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
    ...
  </script>
</head>
<body>
</body>
</html>
```

본문은 비어 있고 모든 결과를 개발자 도구 콘솔에서 확인합니다.

---

# 3. 문서 언어와 제목

원본:

```html
<html lang="en">
<title>Document</title>
```

주석과 학습 내용이 한국어이므로 다음처럼 개선할 수 있습니다.

```html
<html lang="ko">
<title>JavaScript 변수와 자료형</title>
```

JavaScript 동작 자체에는 직접 영향을 주지 않지만 문서 의미와 접근성을 개선합니다.

---

# 4. Script 위치

원본은 `<head>` 안에 script를 작성합니다.

```html
<head>
  <script>
    ...
  </script>
</head>
```

현재 코드는 DOM 요소를 찾지 않으므로 이 위치에서도 문제없이 실행됩니다.

나중에 body 요소를 선택하는 코드가 생기면 다음 방식을 검토합니다.

```html
<script src="main.js" defer></script>
```

`defer`는 HTML 파싱을 막지 않고 문서 파싱 후 스크립트를 실행하게 합니다.

---

# 5. 한 줄 주석

원본:

```js
// 한줄 주석
```

`//` 뒤부터 해당 줄 끝까지 실행되지 않습니다.

```js
let count = 1 // 현재 상품 수량
```

주석은 코드의 이유와 의도를 설명하는 데 사용합니다.

---

# 6. 여러 줄 주석

원본:

```js
/*
  여러줄 주석
  범위 주석
*/
```

`/*`와 `*/` 사이의 내용을 주석으로 처리합니다.

주의:

JavaScript의 여러 줄 주석은 일반적으로 중첩할 수 없습니다.

```js
/*
  바깥 주석
  /* 안쪽 주석 */
*/
```

이런 구조는 문법 문제가 생길 수 있습니다.

---

# 7. `console.log()`

원본:

```js
console.log("hello world")
console.log(a)
console.log(11)
```

`console.log()`는 개발자 도구 콘솔에 값을 출력합니다.

여러 값을 쉼표로 전달할 수 있습니다.

```js
console.log("b :", b)
```

문자열 연결도 가능합니다.

```js
console.log("a : " + a)
```

디버깅할 때 변수 값과 실행 흐름을 확인하는 데 자주 사용합니다.

---

# 8. 문자열 연결과 쉼표 출력

원본에는 두 가지 방식이 있습니다.

```js
console.log("a : " + a)
console.log("b :", b)
```

차이:

```text
+ 연결
→ 하나의 문자열로 변환해 결합

쉼표 전달
→ 여러 값을 console.log의 별도 인수로 전달
```

객체나 배열을 확인할 때는 쉼표 방식이 원래 자료형을 유지해 보기 편할 수 있습니다.

---

# 9. `console.error()`

두 원본 모두 마지막에 다음 코드가 있습니다.

```js
console.error("아무거나")
```

내 코드에는 설명 주석이 추가되어 있습니다.

```js
// error처럼 보이게 강제로 출력할 수 있다
```

`console.error()`는 오류 형태의 스타일로 콘솔 메시지를 출력합니다.

중요:

```text
console.error()를 호출했다
≠ JavaScript 실행 오류가 실제로 발생했다
```

오류 메시지처럼 표시할 뿐, 기본적으로 코드 실행을 중단시키지 않습니다.

---

# 10. `alert()`

원본 주석 처리 코드:

```js
// alert('hello 엔터\n world')
```

`alert()`는 브라우저에 확인 버튼이 있는 대화상자를 표시합니다.

`\n`은 문자열 내부 줄바꿈 문자입니다.

```js
alert("첫 번째 줄\n두 번째 줄")
```

사용자가 대화상자를 닫기 전까지 페이지 상호작용을 막을 수 있으므로 실제 서비스에서는 남용하지 않습니다.

---

# 11. `confirm()`

원본:

```js
// let h = confirm('할래말래')
// console.log('confirm 결과 : ', h)
```

`confirm()`은 확인과 취소 버튼이 있는 대화상자를 표시합니다.

반환값:

```text
확인 → true
취소 → false
```

따라서 Boolean 값을 변수에 저장할 수 있습니다.

---

# 12. `prompt()`

원본:

```js
// let i = prompt('비번을 입력하세요')
// console.log('prompt 결과 : ', i, '입니다')
```

`prompt()`는 사용자가 문자열을 입력할 수 있는 대화상자를 표시합니다.

반환값:

```text
입력 후 확인 → 문자열
취소 → null
```

내 코드 주석:

```js
// prompt는 취소를 눌렀을 때 값이 들어가지 않아 null이 들어간다
```

핵심은 정확하지만 “값이 들어가지 않아”보다 다음 표현이 더 명확합니다.

```text
취소를 누르면 prompt()가 null을 반환한다.
```

빈 문자열을 입력하고 확인하는 것과 취소는 다릅니다.

---

# 13. 변수란?

변수는 값을 저장하고 다시 사용할 수 있도록 이름을 붙인 공간입니다.

```js
let count = 10
```

구분:

```text
let
→ 선언 키워드

count
→ 변수 이름

=
→ 할당 연산자

10
→ 저장할 값
```

---

# 14. 선언과 할당

선언:

```js
let count
```

할당:

```js
count = 10
```

선언과 동시에 초기화:

```js
let count = 10
```

`const`는 선언할 때 값을 함께 넣어야 합니다.

```js
const limit = 10
```

---

# 15. 원본의 첫 번째 `a = 15`

원본은 `var a` 선언보다 먼저 다음 코드를 실행합니다.

```js
a = 15
console.log(a)
```

뒤에는 다음 선언이 있습니다.

```js
var a = 10
```

`var a` 선언은 현재 스크립트의 전역 스코프에서 끌어올려지는 것처럼 처리되므로 이 원본에서는 `a = 15`가 실행 가능합니다.

개념적으로 단순화하면:

```js
var a

a = 15
console.log(a)

a = 10
```

단, 초기화 값 `10`까지 위로 이동하는 것은 아닙니다.

---

# 16. Hoisting 주의

`var` 선언은 선언 위치보다 앞에서 접근할 수 있지만 값은 아직 `undefined`일 수 있습니다.

```js
console.log(value)
var value = 10
```

개념적 결과:

```text
undefined
```

이를 이용해 선언 전 사용을 권장하는 것은 아닙니다.

가독성과 오류 예방을 위해 변수는 사용 전에 선언합니다.

```js
let value = 10
console.log(value)
```

---

# 17. `var`

원본:

```js
var a = 10
var b = 20
```

`var`의 주요 특징:

- 같은 스코프에서 재선언 가능
- 재할당 가능
- 함수 스코프
- 선언이 hoisting됨
- 전역 script에서 선언할 경우 전역 객체와 연결되는 동작이 있을 수 있음

현대 JavaScript에서는 일반적으로 `let`과 `const`를 우선 사용합니다.

---

# 18. `var` 재할당

원본:

```js
a = 30
console.log("a : " + a)
```

이미 선언된 변수의 값을 바꾸는 것은 재할당입니다.

```text
기존 값 10
→ 새 값 30
```

`var`와 `let`은 재할당할 수 있습니다.

---

# 19. `var` 재선언

원본:

```js
var a = 40
```

앞에서 이미 `var a`를 선언했지만 같은 스코프에서 다시 선언해도 문법 오류가 나지 않습니다.

원본 주석:

```js
// 같은 변수명으로 다시 선언해도 오류가 없다
```

이 설명은 같은 스코프의 `var` 재선언 실험에 해당합니다.

다만 재선언을 허용한다는 점은 실수 탐지를 어렵게 만들 수 있습니다.

---

# 20. 선언 없는 `c = 50`

원본:

```js
// 선언 방법 2
// 타입 없음
c = 50
console.log("c : " + c)
```

이 부분의 “타입 없음” 주석은 정확하지 않습니다.

`c`에 저장된 값 `50`은 Number 타입입니다.

문제는 타입이 없는 것이 아니라 **선언 키워드 없이 식별자에 값을 할당했다는 것**입니다.

일반 script의 느슨한 모드에서는 전역 객체의 속성처럼 생성될 수 있습니다.

---

# 21. 선언 없는 할당의 위험

```js
c = 50
```

위험:

- 오타가 새로운 전역 변수를 만들 수 있다.
- 다른 코드와 이름이 충돌할 수 있다.
- 코드 출처를 찾기 어렵다.
- strict mode에서는 오류가 된다.
- ES module에서도 허용되지 않는다.

권장:

```js
let c = 50
```

또는 값이 바뀌지 않는다면:

```js
const c = 50
```

---

# 22. Strict mode

```js
"use strict"

c = 50
```

strict mode에서는 선언되지 않은 식별자에 할당할 때 `ReferenceError`가 발생합니다.

현대 ES module은 기본적으로 strict mode로 동작합니다.

원본은 일반 `<script>`이며 `"use strict"`를 사용하지 않았습니다.

---

# 23. `let`

원본:

```js
let d = 60
console.log("d : " + d)
```

`let`의 특징:

- 같은 스코프에서 재선언 불가
- 재할당 가능
- 블록 스코프
- 선언 전 접근 불가

현대 JavaScript에서 값이 바뀌는 변수에 사용합니다.

---

# 24. `let` 재선언

원본:

```js
// let d = 70
```

주석을 해제하면 같은 스코프에 이미 `let d`가 있으므로 문법 오류가 발생합니다.

원본 주석:

```js
// 같은 변수 명으로 다시 선언하는 것을 막아준다
```

이 설명은 핵심적으로 맞습니다.

---

# 25. `let` 재할당

원본:

```js
d = 65
console.log("d : " + d)
```

`let`은 재선언은 막지만 재할당은 허용합니다.

```text
선언: let d = 60
재할당: d = 65
```

---

# 26. `const`

원본:

```js
const e = 70
console.log("e : " + e)
```

`const`의 특징:

- 같은 스코프에서 재선언 불가
- 변수 바인딩 재할당 불가
- 블록 스코프
- 선언할 때 반드시 초기화

값을 다시 대입할 필요가 없는 변수에 우선 사용합니다.

---

# 27. `const` 재선언과 재할당

원본:

```js
// const e = 80
// e = 75
```

첫 번째는 같은 스코프 재선언 오류입니다.

두 번째는 const 바인딩 재할당 오류입니다.

```text
const e = 70
e = 75
→ TypeError
```

---

# 28. `const`는 선언과 동시에 초기화

원본:

```js
// const f
// f = 80
```

`const`는 다음처럼 나누어 작성할 수 없습니다.

```js
const f
```

문법 오류가 발생합니다.

올바른 작성:

```js
const f = 80
```

---

# 29. `const` 객체의 내부 변경

원본에는 객체가 없지만 `const`를 정확히 이해하기 위한 확장 학습입니다.

```js
const user = {
  name: "Kim"
}

user.name = "Lee"
```

객체 내부 속성은 변경할 수 있습니다.

불가능한 것은 변수 바인딩 자체를 다른 값으로 재할당하는 것입니다.

```js
user = {}
```

즉:

```text
const
→ 값 전체가 절대 불변이라는 뜻이 아님
→ 변수 바인딩 재할당을 막음
```

---

# 30. Var, Let, Const 비교

| 항목 | `var` | `let` | `const` |
| --- | --- | --- | --- |
| 재선언 | 가능 | 불가 | 불가 |
| 재할당 | 가능 | 가능 | 불가 |
| 스코프 | 함수 | 블록 | 블록 |
| 선언 시 초기값 | 선택 | 선택 | 필수 |
| 현대 권장 | 제한적 | 값 변경 시 | 기본 우선 |

실무 권장 흐름:

```text
기본은 const
값을 다시 대입해야 하면 let
기존 코드 유지보수 외에는 var 사용 최소화
```

---

# 31. JavaScript의 동적 타입

원본:

```js
let d = 60
d = "문자"
```

같은 변수에 Number를 저장했다가 String을 다시 저장할 수 있습니다.

```text
처음 d → Number
나중 d → String
```

JavaScript 변수 자체에 고정 타입이 붙는 것이 아니라 현재 저장된 값이 타입을 가집니다.

---

# 32. “타입 없음”과 동적 타입의 차이

JavaScript는 타입이 없는 언어가 아닙니다.

다음 값은 각각 타입이 있습니다.

```js
10       // number
"문자"   // string
true     // boolean
undefined
null
```

정확한 표현:

```text
JavaScript는 동적 타입 언어이다.
변수에 저장되는 값의 타입이 실행 중 바뀔 수 있다.
```

---

# 33. 변수 이름 규칙

JavaScript 식별자에는 일반적으로 다음을 사용할 수 있습니다.

- 영문자
- 숫자
- `_`
- `$`
- 유니코드 문자

숫자로 시작할 수 없습니다.

```js
let count1 = 1
let _count = 1
let $count = 1
let 잔고 = 15000
```

다음은 불가능합니다.

```js
let 1count = 1
```

---

# 34. Camel case

원본:

```js
let salesCount = 1
```

camelCase는 첫 단어를 소문자로 시작하고 이후 단어의 첫 글자를 대문자로 작성합니다.

```text
salesCount
userName
totalPrice
```

JavaScript 변수와 함수 이름에 널리 사용합니다.

---

# 35. Snake case

원본:

```js
let sales_count = 1
```

단어 사이를 밑줄로 구분합니다.

```text
sales_count
user_name
```

JavaScript에서도 사용할 수 있지만 프로젝트 스타일 규칙을 일관되게 따릅니다.

---

# 36. Kebab case

원본:

```js
// let font-size = 2
```

kebab-case는 CSS 클래스명이나 파일명에서 자주 사용합니다.

```text
font-size
main-menu
```

JavaScript 변수명에서는 `-`가 빼기 연산자로 해석되기 때문에 사용할 수 없습니다.

```js
let font - size = 2
```

처럼 해석되어 문법 오류가 납니다.

---

# 37. 한글 변수명

원본:

```js
let 밭 = 10
let 잔고 = 15000
let 번돈 = 100000
```

JavaScript는 한글 식별자를 허용합니다.

학습 예제에서는 의미를 쉽게 이해하는 장점이 있습니다.

실무에서는 다음을 고려합니다.

- 팀 구성원의 언어
- 외부 라이브러리와의 일관성
- 검색과 입력 편의
- 코드 스타일 규칙

문법 오류는 아니지만 일반적으로 영어 camelCase를 많이 사용합니다.

---

# 38. `undefined`

원본:

```js
let y
console.log(y)
```

변수는 선언했지만 값을 명시적으로 넣지 않았습니다.

결과:

```text
undefined
```

`undefined`는 값이 아직 지정되지 않았음을 나타내는 원시값입니다.

---

# 39. `not defined`와 `undefined`

원본:

```js
// not defined
// console.log(z)
let y
console.log(y)
```

차이:

```text
y
→ 선언됨
→ 값이 없어 undefined

z
→ 선언 자체가 없음
→ 접근하면 ReferenceError: z is not defined
```

`undefined`와 “not defined 오류”는 같은 것이 아닙니다.

---

# 40. `Infinity`

원본:

```js
console.log(7 / 0)
```

결과:

```text
Infinity
```

JavaScript의 Number 연산에서 양수를 0으로 나누면 `Infinity`가 나올 수 있습니다.

`Infinity`도 Number 타입입니다.

```js
typeof Infinity // "number"
```

---

# 41. 음의 Infinity

```js
console.log(-7 / 0)
```

결과:

```text
-Infinity
```

무한대 값인지 확인할 때는 상황에 따라 `Number.isFinite()`를 사용할 수 있습니다.

```js
Number.isFinite(7 / 0) // false
```

---

# 42. `NaN`

원본:

```js
console.log(7 * "문자")
```

결과:

```text
NaN
```

`NaN`은 Not a Number의 약자이며 숫자로 계산할 수 없는 결과를 나타냅니다.

이름과 달리 타입은 Number입니다.

```js
typeof NaN // "number"
```

---

# 43. NaN 비교 주의

```js
NaN === NaN
```

결과는 `false`입니다.

NaN 여부를 확인할 때는 다음을 권장합니다.

```js
Number.isNaN(value)
```

예:

```js
const value = Number("10개")
console.log(Number.isNaN(value))
```

---

# 44. Boolean

원본:

```js
let f = true
let g = false
```

Boolean은 참과 거짓을 표현하는 타입입니다.

```text
true
false
```

주로 다음에 사용합니다.

- 조건 판단
- 메뉴 열림 상태
- 로그인 여부
- 체크 여부
- 서버 요청 성공 여부

---

# 45. 문자열

원본:

```js
let strA = "10.1"
let strB = "10개"
```

따옴표로 감싼 값은 문자열입니다.

```js
"10.1"
```

숫자처럼 보여도 문자열입니다.

```js
typeof "10.1" // "string"
```

---

# 46. 템플릿 리터럴

원본:

```js
console.log(`백틱
엔터 가능
${a}
`)
```

백틱으로 감싸는 문자열을 템플릿 리터럴이라고 합니다.

기능:

- 여러 줄 문자열
- `${}`를 이용한 표현식 삽입
- 문자열 연결을 줄일 수 있음

---

# 47. 문자열 보간

원본 비교:

```js
console.log("a :" + a)
console.log(`a : ${a}`)
```

템플릿 리터럴은 변수와 문자열의 경계를 보기 쉽습니다.

```js
const name = "홍길동"
console.log(`이름: ${name}`)
```

`${}` 안에는 표현식을 작성할 수 있습니다.

```js
console.log(`합계: ${10 + 20}`)
```

---

# 48. 문자열과 숫자의 `+`

원본:

```js
console.log(strA + 2)
```

`strA`는 `"10.1"` 문자열이므로 결과는 숫자 덧셈이 아니라 문자열 연결입니다.

```text
"10.1" + 2
→ "10.12"
```

원본 주석도 다음 결과를 기록합니다.

```js
// "10.12"
```

---

# 49. `Number()`

원본:

```js
let numA = Number(strA) + 2
console.log(numA)
```

`Number("10.1")`은 전체 문자열을 숫자로 변환합니다.

```text
10.1 + 2
→ 12.1
```

---

# 50. `Number("10개")`

원본:

```js
console.log(Number(strB))
```

`strB`는 `"10개"`입니다.

전체 문자열이 유효한 숫자 형식이 아니므로 결과는:

```text
NaN
```

`Number()`는 문자열 전체가 숫자로 해석 가능해야 합니다.

---

# 51. `parseInt()`

원본:

```js
numA = parseInt(strA)
console.log("numA :", numA)
console.log(parseInt(strB))
```

결과:

```text
parseInt("10.1") → 10
parseInt("10개") → 10
```

`parseInt()`는 문자열 앞부분에서 정수로 해석 가능한 부분을 읽습니다.

숫자로 시작하지 않으면 NaN이 될 수 있습니다.

```js
parseInt("개10") // NaN
```

---

# 52. Number와 ParseInt 비교

| 입력 | `Number()` | `parseInt()` |
| --- | ---: | ---: |
| `"10.1"` | `10.1` | `10` |
| `"10개"` | `NaN` | `10` |
| `"개10"` | `NaN` | `NaN` |
| `""` | `0` | `NaN` |

목적에 맞게 선택합니다.

사용자 입력을 변환한 뒤에는 NaN 검사를 함께 고려합니다.

---

# 53. ParseInt의 진법

명시적으로 10진수를 전달할 수 있습니다.

```js
parseInt("10", 10)
```

두 번째 인수는 radix입니다.

현대 환경에서는 일반적인 십진 문자열이 예상대로 처리되지만 명확성을 위해 진법을 작성하는 스타일도 있습니다.

---

# 54. `String()`

원본:

```js
console.log(String(numA))
```

숫자를 문자열로 명시적으로 변환합니다.

```js
String(10) // "10"
```

의도가 명확하므로 권장되는 변환 방식입니다.

---

# 55. 빈 문자열을 이용한 변환

원본:

```js
console.log("" + numA)
```

문자열과 `+` 연산을 하면 숫자가 문자열로 변환됩니다.

결과는 가능하지만 의도가 덜 명확합니다.

```js
String(numA)
```

가 읽기 쉽습니다.

---

# 56. 단위 계산 원본

원본:

```js
let py = 3.3
let acre = 4046.8
let 밭 = 10

console.log("단위가 평일 때 : " + 밭 * py)
console.log("단위가 에이커일 때 : " + 밭 * acre)
console.log(82 / py)
```

수업 예제에서는:

```text
1평 → 3.3㎡
1에이커 → 4046.8㎡
```

라는 근삿값을 변수에 저장해 계산합니다.

---

# 57. 연산자 우선순위

다음 코드:

```js
"단위가 평일 때 : " + 밭 * py
```

곱셈이 문자열 연결보다 먼저 계산됩니다.

개념적으로:

```js
"단위가 평일 때 : " + (밭 * py)
```

결과:

```text
단위가 평일 때 : 33
```

가독성을 위해 괄호나 템플릿 리터럴을 사용할 수 있습니다.

```js
console.log(`단위가 평일 때: ${밭 * py}`)
```

---

# 58. 근삿값 주의

원본의 `3.3`과 `4046.8`은 학습용 근삿값입니다.

정밀한 토지 면적 계산이 필요한 서비스라면:

- 공식 환산 기준 확인
- 소수점 정밀도 결정
- 반올림 방식 결정
- 단위 표기
- 법적·업무 기준 확인

이 필요합니다.

이 문서에서는 원본의 학습값을 그대로 보존합니다.

---

# 59. 82㎡를 평으로 변환

원본:

```js
console.log(82 / py)
```

`py`가 3.3이므로 약 24.848...이 출력됩니다.

표시용 결과라면 반올림할 수 있습니다.

```js
const pyeong = 82 / py
console.log(pyeong.toFixed(1))
```

`toFixed()`의 결과는 문자열이라는 점도 기억합니다.

---

# 60. 증가 계산

원본:

```js
a = 10
a = a + 1
```

오른쪽의 기존 `a` 값에 1을 더한 뒤 결과를 다시 `a`에 저장합니다.

```text
a = 10
a = 11
```

다음 표현도 가능합니다.

```js
a += 1
a++
```

증감 연산자는 다음 연산자 단원에서 더 자세히 다룹니다.

---

# 61. 복합 할당 연산자

원본:

```js
let 잔고 = 15000
let 번돈 = 100000

잔고 = 잔고 + 번돈
잔고 += 번돈
```

두 줄은 순서대로 실행됩니다.

계산:

```text
초기 잔고 15,000
첫 번째 덧셈 후 115,000
두 번째 덧셈 후 215,000
```

두 표현은 같은 의미의 대체 예제가 아니라 실제로 둘 다 실행되므로 번돈이 두 번 더해집니다.

---

# 62. 원본 복합 할당 주의

만약 두 작성법을 비교하려는 목적이었다면 다음처럼 별도 변수나 주석 처리가 더 명확합니다.

```js
let balanceA = 15000
balanceA = balanceA + 100000

let balanceB = 15000
balanceB += 100000
```

원본은 두 문장이 연속 실행된다는 사실을 보존해야 합니다.

---

# 63. 나눗셈

원본:

```js
console.log(7 / 3)
```

JavaScript의 `/`는 실수 결과를 반환할 수 있습니다.

```text
7 / 3
→ 2.3333333333333335
```

정수 몫만 필요하다면 목적에 맞는 절삭 방법을 선택합니다.

---

# 64. 나머지 연산자

원본:

```js
console.log("나머지 :", 7 % 3)
```

결과:

```text
1
```

내 코드에는 다음 주석이 추가되어 있습니다.

```js
// %는 나머지의 값을 출력하게 하는 것
```

더 정확하게는 `%`가 나머지 연산의 결과를 반환합니다.

---

# 65. 몫 계산 원본

원본:

```js
console.log("몫 :", parseInt(7 / 3))
```

결과는 2입니다.

다만 숫자의 정수 부분을 얻기 위해 문자열 분석 함수인 `parseInt()`를 사용하는 방식은 의도가 덜 명확합니다.

권장:

```js
Math.trunc(7 / 3)
```

양수에서 내림이 목적이면:

```js
Math.floor(7 / 3)
```

음수에서는 `Math.trunc()`와 `Math.floor()` 결과가 다를 수 있습니다.

---

# 66. 강사님 회식비 문제

강사님 원본:

```js
/*
  9명이 회식을 했고 비용이 100000만원이 나왔다
  인당?
*/
console.log("인당 : ")
console.log("주최자가 조금 더 낼 때 얼마?")
```

문제만 제시되어 있고 계산식은 비어 있습니다.

중요한 원본 표현:

```text
100000만원
```

이는 문자 그대로 해석하면 매우 큰 금액입니다.

수업 문맥상 `100000원`을 의도했을 가능성이 있지만 원본을 조용히 수정하지 않습니다.

---

# 67. 내 코드 회식비 문제

내 코드:

```js
// 9명이 회식을 했고 비용이 100,000원이 나왔다

console.log("나머지 :", 100000 % 9)
console.log("인당 :", parseInt(100000 / 9))

console.log(
  "주최자 :",
  parseInt(100000 / 9) + (100000 % 9)
)
```

내 코드는 강사님 문제를 `100,000원`으로 해석하고 풀이를 추가했습니다.

---

# 68. 회식비 계산 결과

```text
100000 / 9
→ 11111.111...

정수 몫
→ 11111

나머지
→ 1
```

8명은 11,111원씩 내고, 주최자가 나머지 1원을 더 내면:

```text
주최자 → 11,112원
```

합계:

```text
11,111 × 8 + 11,112
= 100,000
```

---

# 69. 회식비 코드 개선

```js
const total = 100000
const people = 9

const perPerson = Math.floor(total / people)
const remainder = total % people
const organizer = perPerson + remainder

console.log(`인당: ${perPerson}원`)
console.log(`주최자: ${organizer}원`)
```

변수 이름을 사용하면 계산 의도를 파악하기 쉽습니다.

---

# 70. 확인 대화상자 값을 변수에 저장

내 코드 추가 주석:

```js
// confirm, prompt 등 값을 받아 변수에 넣을 수 있다
```

정확합니다.

함수 호출의 반환값을 변수에 저장합니다.

```js
const agreed = confirm("동의하시겠습니까?")
const password = prompt("비밀번호를 입력하세요")
```

이후 조건문에서 사용할 수 있습니다.

---

# 71. 여러 변수 개별 선언

원본:

```js
let a1 = 10
let a2 = 20
let a3 = 30
```

각 변수를 별도 문장으로 선언합니다.

장점:

- 한 줄씩 수정하기 쉽다.
- diff가 명확하다.
- 각 변수에 주석을 붙이기 쉽다.

---

# 72. 쉼표를 이용한 다중 선언

원본:

```js
let b1 = 10,
    b2 = 20,
    b3 = 30
```

하나의 `let` 선언문에서 여러 변수를 선언합니다.

내 코드에는 다음 설명이 추가되어 있습니다.

```js
// let을 3개 쓰거나 ,로 이어서 쓸 수 있다
```

둘 다 문법적으로 가능합니다.

프로젝트 코드 스타일에 따라 별도 선언을 선호하기도 합니다.

---

# 73. 세미콜론

원본은 일부 줄에 세미콜론이 있고 많은 줄에는 없습니다.

JavaScript에는 자동 세미콜론 삽입이 있어 많은 경우 실행됩니다.

하지만 특정 줄바꿈에서는 예상치 못한 문제가 생길 수 있으므로 프로젝트 스타일을 일관되게 유지합니다.

```js
const count = 10;
console.log(count);
```

또는 세미콜론을 생략하는 규칙을 사용하더라도 formatter와 lint 규칙을 함께 사용합니다.

---

# 74. My Code 분석

## 74.1 장점

- `%`가 나머지 계산에 사용된다는 설명을 추가했다.
- 강사님의 미완성 회식비 문제를 실제 계산식으로 완성했다.
- `100000만원` 대신 `100,000원`이라는 현실적인 학습 문제로 해석했다.
- 인당 금액, 나머지, 주최자 부담액을 각각 출력했다.
- `confirm()`과 `prompt()`의 반환값을 변수에 저장할 수 있음을 설명했다.
- prompt 취소 시 `null`이 반환된다는 설명을 추가했다.
- 템플릿 리터럴로 prompt 결과를 출력하는 방식을 설명했다.
- 다중 변수 선언 문법을 주석으로 설명했다.
- `console.error()`의 목적을 설명했다.

## 74.2 개선점

- 강사님 문제의 금액을 변경했다는 사실을 별도로 기록하지 않았다.
- 회식비 몫 계산에 `parseInt()`보다 `Math.floor()` 또는 `Math.trunc()`가 의도에 적합하다.
- 선언 없는 `c = 50`을 “타입 없음”으로 설명한 원본 주석을 보완해야 한다.
- `a = 15`가 선언보다 앞에 있는 이유를 hoisting과 연결해 설명해야 한다.
- 잔고 계산은 같은 돈을 두 번 더하고 있으므로 비교 예제라면 변수를 분리해야 한다.
- 변수 이름에 한글을 사용하는 것은 문법적으로 가능하지만 팀 스타일을 고려해야 한다.
- `var`보다 `const`와 `let`을 우선하는 현대 작성법을 추가할 수 있다.
- 문서 언어와 제목을 개선해야 한다.

---

# 75. Teacher Code 분석

## 75.1 장점

- 주석, 콘솔, 대화상자, 변수 선언을 하나의 파일에서 순차적으로 실습한다.
- `var`의 재선언과 재할당을 직접 확인한다.
- `let`의 재선언 제한과 재할당 가능성을 비교한다.
- `const`의 선언·초기화와 재할당 제한을 확인한다.
- 동적 타입 변경을 보여 준다.
- `undefined`, `Infinity`, `NaN`, Boolean, 문자열을 폭넓게 다룬다.
- `Number()`, `parseInt()`, `String()`을 비교한다.
- 단위 계산과 금액 계산으로 변수 사용을 연결한다.
- 다중 변수 선언과 `console.error()`까지 포함한다.

## 75.2 개선점

- `c = 50`을 “타입 없음”이라고 적은 것은 부정확하다.
- 선언 없는 할당이 전역 오염을 만들 수 있다는 설명이 없다.
- `var` hoisting과 선언 전 `a = 15`의 관계가 설명되지 않는다.
- `100000만원`은 문제 문맥상 오타 가능성이 크다.
- 회식비 문제의 계산식이 완성되지 않았다.
- `parseInt(7 / 3)`는 정수 몫 계산 의도가 명확하지 않다.
- `잔고 = 잔고 + 번돈`과 `잔고 += 번돈`이 둘 다 실행되어 금액이 두 번 더해진다.
- prompt 취소 시 `null` 설명이 없다.
- `order`와 같은 다음 단계 개념은 아니지만 변수 이름 규칙과 strict mode를 보완할 수 있다.
- 문서 언어와 제목이 콘텐츠에 맞지 않는다.

---

# 76. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기본 변수 실습 | 동일 | 동일 |
| `%` 설명 | 추가됨 | 없음 |
| 회식비 금액 표현 | `100,000원` | `100000만원` |
| 회식비 풀이 | 완료 | 문제 문구만 있음 |
| 나머지 출력 | 있음 | 없음 |
| 인당 계산 | 있음 | 출력 문구만 있음 |
| 주최자 계산 | 있음 | 질문 문구만 있음 |
| confirm 설명 | 반환값 저장 설명 | 코드만 있음 |
| prompt 취소 설명 | `null` 설명 있음 | 없음 |
| 템플릿 리터럴 설명 | 주석 있음 | 예제만 있음 |
| 다중 변수 선언 설명 | 있음 | 없음 |
| console.error 설명 | 있음 | 없음 |
| 나머지 코드 | 대부분 동일 | 대부분 동일 |

---

# 77. 원본 공통 핵심 코드

```js
console.log("hello world")

a = 15
console.log(a)

var a = 10
var b = 20

a = 30
var a = 40

c = 50

let d = 60
d = 65

const e = 70

d = "문자"

let y
console.log(y)

console.log(7 / 0)
console.log(7 * "문자")

let f = true
let g = false

let strA = "10.1"
let strB = "10개"

console.log(strA + 2)
let numA = Number(strA) + 2

numA = parseInt(strA)
console.log(parseInt(strB))

console.log(String(numA))
console.log("" + numA)
```

---

# 78. 원본 통합 개선 예제

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>JavaScript 변수와 자료형</title>
  <script src="asset/js/01_var.js" defer></script>
</head>
<body>
  <h1>JavaScript 변수와 자료형</h1>
  <p>개발자 도구의 Console을 확인하세요.</p>
</body>
</html>
```

## JavaScript

```js
"use strict";

console.log("hello world");

const initialValue = 15;
console.log("initialValue:", initialValue);

let count = 10;
console.log("count:", count);

count = 30;
console.log("변경된 count:", count);

const limit = 70;
console.log("limit:", limit);

let dynamicValue = 60;
dynamicValue = "문자";
console.log("dynamicValue:", dynamicValue);

let emptyValue;
console.log("emptyValue:", emptyValue);

console.log("Infinity:", 7 / 0);
console.log("NaN:", 7 * "문자");

const numericText = "10.1";
const mixedText = "10개";

const numberValue = Number(numericText);
const integerValue = parseInt(mixedText, 10);

console.log("Number:", numberValue);
console.log("parseInt:", integerValue);
console.log("String:", String(integerValue));
```

---

# 79. 회식비 개선 예제

```js
const totalPrice = 100000;
const peopleCount = 9;

const basePrice =
  Math.floor(totalPrice / peopleCount);

const remainder =
  totalPrice % peopleCount;

const organizerPrice =
  basePrice + remainder;

console.log(`기본 인당 금액: ${basePrice}원`);
console.log(`남은 금액: ${remainder}원`);
console.log(`주최자 금액: ${organizerPrice}원`);
```

---

# 80. 입력값 숫자 변환 예제

```js
const input = prompt("수량을 입력하세요");

if (input === null) {
  console.log("입력을 취소했습니다.");
} else {
  const quantity = Number(input);

  if (Number.isNaN(quantity)) {
    console.error("숫자를 입력해야 합니다.");
  } else {
    console.log(`입력한 수량: ${quantity}`);
  }
}
```

조건문은 이후 단원에서 자세히 학습합니다.

---

# 81. 변수 선언 권장 패턴

```js
const taxRate = 0.1;
const productName = "노트북";

let quantity = 1;
let totalPrice = 0;

totalPrice = 1200000 * quantity;
```

기준:

```text
재할당하지 않음 → const
재할당함 → let
var → 기존 코드 이해 목적 외에는 최소화
```

---

# 82. 개발자 도구 확인 방법

Chrome 기준:

```text
F12
또는
Ctrl + Shift + I
```

Console 탭에서 확인:

- `console.log()` 출력
- `console.error()` 출력
- ReferenceError
- SyntaxError
- TypeError
- 현재 변수 값

브라우저 새로고침 때 script가 다시 실행됩니다.

---

# 83. 자주 하는 실수

## 83.1 선언 없이 값 할당

```js
c = 50
```

전역 오염과 오타 문제를 만들 수 있습니다.

## 83.2 `let` 재선언

```js
let count = 1
let count = 2
```

같은 스코프에서 SyntaxError입니다.

## 83.3 `const` 재할당

```js
const count = 1
count = 2
```

TypeError입니다.

## 83.4 `const` 초기값 생략

```js
const count
```

SyntaxError입니다.

## 83.5 `"10" + 2`를 숫자 12로 예상

결과는 `"102"`입니다.

## 83.6 `Number("10개")`를 10으로 예상

결과는 NaN입니다.

## 83.7 `NaN === NaN`으로 검사

결과는 false입니다. `Number.isNaN()`을 사용합니다.

## 83.8 `undefined`와 not defined 혼동

선언된 변수의 빈 값과 선언되지 않은 식별자 오류는 다릅니다.

## 83.9 `parseInt()`를 모든 소수 제거에 사용

문자열 분석 함수이므로 숫자 절삭에는 `Math.trunc()` 등이 의도에 더 적합할 수 있습니다.

## 83.10 비교용 두 할당문을 연속 실행

원본 잔고 예제처럼 같은 금액이 두 번 더해질 수 있습니다.

---

# 84. 면접·복습 포인트

## Q1. `var`, `let`, `const`의 차이는 무엇인가요?

`var`는 같은 스코프 재선언이 가능하고 함수 스코프입니다. `let`은 블록 스코프이며 재할당은 가능하지만 재선언은 불가능합니다. `const`는 블록 스코프이며 재선언과 재할당이 불가능하고 선언 시 초기값이 필요합니다.

## Q2. JavaScript는 타입이 없는 언어인가요?

아닙니다. 값마다 타입이 있으며 변수에 저장되는 값의 타입이 실행 중 바뀔 수 있는 동적 타입 언어입니다.

## Q3. `undefined`와 not defined의 차이는 무엇인가요?

`undefined`는 선언된 변수에 값이 없는 상태입니다. not defined는 식별자 자체가 선언되지 않아 ReferenceError가 발생하는 상태입니다.

## Q4. `NaN`의 타입은 무엇인가요?

Number입니다.

## Q5. `Number("10개")`와 `parseInt("10개")` 결과는 무엇인가요?

`Number()`는 NaN, `parseInt()`는 10입니다.

## Q6. 템플릿 리터럴의 장점은 무엇인가요?

여러 줄 문자열과 `${}` 표현식 삽입을 지원해 문자열 연결을 읽기 쉽게 작성할 수 있습니다.

## Q7. 선언 없는 할당이 위험한 이유는 무엇인가요?

느슨한 모드에서 의도치 않은 전역 변수를 만들고 이름 충돌이나 오타를 숨길 수 있기 때문입니다.

## Q8. `const` 객체의 속성은 변경할 수 있나요?

가능합니다. const는 변수 바인딩의 재할당을 막으며 객체 자체의 내부 변경까지 자동으로 막지는 않습니다.

## Q9. 정수 몫을 얻을 때 `parseInt(7 / 3)`보다 명확한 방법은 무엇인가요?

목적에 따라 `Math.trunc(7 / 3)` 또는 양수에서 `Math.floor(7 / 3)`를 사용할 수 있습니다.

## Q10. `console.error()`는 실제 예외를 발생시키나요?

아닙니다. 오류 스타일로 메시지를 출력할 뿐 기본적으로 실행을 중단시키지 않습니다.

---

# Problems

## 문제 1. 콘솔 출력

콘솔에 `Hello JavaScript`를 출력하세요.

## 문제 2. 한 줄 주석

`사용자 수`라는 한 줄 주석을 작성하세요.

## 문제 3. 여러 줄 주석

두 줄로 된 여러 줄 주석을 작성하세요.

## 문제 4. Let 선언

`count`를 10으로 선언하세요.

## 문제 5. Let 재할당

문제 4의 `count`를 20으로 변경하세요.

## 문제 6. Const 선언

`MAX_COUNT`를 100으로 선언하세요.

## 문제 7. Var 재선언

같은 스코프에서 `var value`를 두 번 선언하는 예제를 작성하세요.

## 문제 8. 선언 없는 할당

다음 코드의 문제를 설명하세요.

```js
price = 1000
```

## 문제 9. 동적 타입

하나의 let 변수에 숫자를 저장한 뒤 문자열로 변경하세요.

## 문제 10. Undefined

선언만 하고 값을 넣지 않은 변수를 출력하세요.

## 문제 11. Not Defined

선언하지 않은 `unknownValue`를 출력하면 어떤 오류가 발생하는지 작성하세요.

## 문제 12. Infinity

7을 0으로 나눈 결과를 출력하세요.

## 문제 13. NaN

문자열 `"문자"`에 7을 곱하고 NaN인지 검사하세요.

## 문제 14. 템플릿 리터럴

`name`이 `"Kim"`일 때 `이름: Kim`을 템플릿 리터럴로 출력하세요.

## 문제 15. Number 변환

문자열 `"10.5"`를 숫자로 변환해 2를 더하세요.

## 문제 16. ParseInt 변환

문자열 `"20개"`에서 정수 20을 얻으세요.

## 문제 17. String 변환

숫자 100을 명시적으로 문자열로 변환하세요.

## 문제 18. 몫과 나머지

100을 9로 나눈 정수 몫과 나머지를 구하세요.

## 문제 19. 복합 할당

`balance`에 10,000을 저장하고 5,000을 더하세요.

## 문제 20. 원본 차이

회식비 문제에서 내 코드와 강사님 코드의 차이를 설명하세요.

## 문제 21. Prompt 처리

prompt 취소와 숫자가 아닌 입력을 구분하는 코드를 작성하세요.

## 문제 22. 종합 결제 계산

다음 요구사항을 만족하는 코드를 작성하세요.

- 상품 가격 12,000원
- 수량 문자열 `"3"`
- Number로 수량 변환
- 총액 계산
- 4명이 나눠 낼 기본 금액과 나머지 계산
- 템플릿 리터럴 출력
- 모든 고정값은 const
- NaN 검사 포함

---

# Answers & Explanations

## 정답 1

```js
console.log("Hello JavaScript")
```

## 정답 2

```js
// 사용자 수
```

## 정답 3

```js
/*
  첫 번째 줄
  두 번째 줄
*/
```

## 정답 4

```js
let count = 10
```

## 정답 5

```js
count = 20
```

재선언이 아니라 재할당입니다.

## 정답 6

```js
const MAX_COUNT = 100
```

상수처럼 사용하는 값에 대문자 snake case를 사용하는 규칙도 있지만 프로젝트 스타일에 따릅니다.

## 정답 7

```js
var value = 10
var value = 20
```

같은 스코프의 var 재선언은 허용됩니다.

## 정답 8

선언 키워드가 없습니다. 느슨한 일반 script에서는 의도치 않은 전역 속성을 만들 수 있고 strict mode나 module에서는 ReferenceError가 발생합니다.

개선:

```js
const price = 1000
```

## 정답 9

```js
let value = 10
value = "문자"
```

## 정답 10

```js
let emptyValue
console.log(emptyValue)
```

결과는 `undefined`입니다.

## 정답 11

```text
ReferenceError: unknownValue is not defined
```

## 정답 12

```js
console.log(7 / 0)
```

결과는 `Infinity`입니다.

## 정답 13

```js
const result = 7 * "문자"

console.log(result)
console.log(Number.isNaN(result))
```

## 정답 14

```js
const name = "Kim"

console.log(`이름: ${name}`)
```

## 정답 15

```js
const value = Number("10.5") + 2

console.log(value)
```

결과는 `12.5`입니다.

## 정답 16

```js
const count = parseInt("20개", 10)

console.log(count)
```

## 정답 17

```js
const text = String(100)

console.log(text)
```

## 정답 18

```js
const quotient = Math.floor(100 / 9)
const remainder = 100 % 9

console.log("몫:", quotient)
console.log("나머지:", remainder)
```

## 정답 19

```js
let balance = 10000

balance += 5000

console.log(balance)
```

## 정답 20

강사님 코드는 `100000만원`이라는 문제 문구와 미완성 출력문만 있습니다. 내 코드는 이를 `100,000원`으로 해석하고 나머지, 인당 금액, 주최자 금액 계산을 완성했습니다.

## 정답 21

```js
const input = prompt("숫자를 입력하세요")

if (input === null) {
  console.log("입력을 취소했습니다.")
} else {
  const value = Number(input)

  if (Number.isNaN(value)) {
    console.error("숫자가 아닙니다.")
  } else {
    console.log(`입력값: ${value}`)
  }
}
```

## 정답 22

```js
const productPrice = 12000
const quantityText = "3"
const peopleCount = 4

const quantity = Number(quantityText)

if (Number.isNaN(quantity)) {
  console.error("수량을 숫자로 변환할 수 없습니다.")
} else {
  const totalPrice =
    productPrice * quantity

  const basePayment =
    Math.floor(totalPrice / peopleCount)

  const remainder =
    totalPrice % peopleCount

  console.log(`총액: ${totalPrice}원`)
  console.log(`기본 인당 금액: ${basePayment}원`)
  console.log(`남는 금액: ${remainder}원`)
}
```

계산 결과:

```text
총액: 36,000원
기본 인당 금액: 9,000원
남는 금액: 0원
```

---

# Final Checklist

## JavaScript 실행

- [ ] script가 HTML에서 정상 실행된다.
- [ ] Console 탭에서 출력 결과를 확인했다.
- [ ] `console.log()`와 `console.error()`를 구분했다.
- [ ] alert, confirm, prompt의 반환값을 이해했다.
- [ ] script 위치와 defer 필요성을 확인했다.

## 변수 선언

- [ ] 선언과 할당을 구분했다.
- [ ] 기본적으로 const를 우선 검토했다.
- [ ] 재할당이 필요할 때 let을 사용했다.
- [ ] var의 재선언과 함수 스코프 특성을 이해했다.
- [ ] 선언 없는 할당을 사용하지 않았다.
- [ ] 변수를 사용하기 전에 선언했다.
- [ ] 같은 스코프에서 let과 const를 재선언하지 않았다.

## 자료형

- [ ] JavaScript가 동적 타입 언어임을 이해했다.
- [ ] 문자열과 숫자를 구분했다.
- [ ] Boolean의 true와 false를 사용했다.
- [ ] undefined와 not defined를 구분했다.
- [ ] Infinity가 Number 타입임을 이해했다.
- [ ] NaN 검사에 `Number.isNaN()`을 사용했다.
- [ ] const 객체의 내부 변경과 재할당을 구분했다.

## 문자열과 변환

- [ ] 템플릿 리터럴을 사용할 수 있다.
- [ ] `${}`로 표현식을 삽입했다.
- [ ] 문자열과 숫자의 `+` 결과를 예측했다.
- [ ] `Number()`와 `parseInt()`의 차이를 이해했다.
- [ ] 숫자 변환 뒤 NaN을 검사했다.
- [ ] 명시적 문자열 변환에는 `String()`을 검토했다.
- [ ] `parseInt()`에 진법을 명시할지 팀 규칙을 확인했다.

## 계산

- [ ] `/`와 `%`를 구분했다.
- [ ] 정수 몫에 적절한 Math 함수를 검토했다.
- [ ] 복합 할당이 실제로 한 번만 실행되는지 확인했다.
- [ ] 금액 계산에서 단위를 표시했다.
- [ ] 소수점과 반올림 기준을 정했다.
- [ ] 사용자 입력이 문자열이라는 점을 고려했다.

## 원본 코드 검수

- [ ] 내 코드와 강사님 코드의 공통 부분을 보존했다.
- [ ] 내 코드의 `%` 설명 추가를 기록했다.
- [ ] `100000만원`과 `100,000원` 차이를 기록했다.
- [ ] 강사님 회식비 문제의 미완성 상태를 보존했다.
- [ ] 내 코드의 회식비 풀이를 기록했다.
- [ ] 선언 없는 `c = 50`의 “타입 없음” 설명을 보완했다.
- [ ] `a = 15`와 var hoisting 관계를 설명했다.
- [ ] 잔고에 번돈이 두 번 더해지는 원본 실행 결과를 설명했다.
- [ ] prompt 취소 시 null 설명 차이를 기록했다.
- [ ] 문서 언어와 제목을 개선했다.

---

# Key Summary

- JavaScript는 웹 페이지에 동작과 계산 로직을 추가한다.
- 원본은 HTML head의 내부 script에서 실행된다.
- `//`는 한 줄 주석, `/* */`는 여러 줄 주석이다.
- `console.log()`는 일반 출력, `console.error()`는 오류 스타일 출력이다.
- `alert()`는 알림, `confirm()`은 Boolean, `prompt()`는 문자열 또는 null을 반환한다.
- 변수 선언과 값 할당은 서로 다른 개념이다.
- `var`는 같은 스코프에서 재선언과 재할당이 가능하다.
- `let`은 재선언은 불가능하지만 재할당은 가능하다.
- `const`는 재선언과 재할당이 불가능하며 선언할 때 초기값이 필요하다.
- 현대 JavaScript에서는 기본적으로 const를 우선하고 필요할 때 let을 사용한다.
- 원본의 `a = 15`는 뒤의 `var a` 선언 hoisting과 관련해 실행될 수 있다.
- 선언 없는 `c = 50`은 타입이 없는 것이 아니라 선언 키워드가 빠진 위험한 코드다.
- JavaScript는 타입이 없는 언어가 아니라 동적 타입 언어다.
- 같은 let 변수에 Number를 저장한 뒤 String을 저장할 수 있다.
- camelCase는 JavaScript 변수 이름에서 널리 사용한다.
- kebab-case는 `-`가 연산자로 해석되어 변수명으로 사용할 수 없다.
- 한글 식별자는 문법적으로 가능하지만 팀 규칙과 유지보수를 고려한다.
- 선언만 한 변수의 값은 undefined다.
- 선언되지 않은 식별자 접근은 ReferenceError를 만든다.
- `7 / 0`은 Infinity이고 `7 * "문자"`는 NaN이다.
- NaN 여부는 `Number.isNaN()`으로 확인한다.
- 백틱 템플릿 리터럴은 여러 줄 문자열과 `${}` 보간을 지원한다.
- `"10.1" + 2`는 문자열 연결로 `"10.12"`가 된다.
- `Number("10.1")`은 10.1이고 `Number("10개")`는 NaN이다.
- `parseInt("10.1")`과 `parseInt("10개")`는 모두 10이 될 수 있다.
- 문자열 변환 의도를 명확히 할 때 `String()`을 사용한다.
- 원본의 잔고 계산은 두 할당문이 모두 실행되어 번돈이 두 번 더해진다.
- `%`는 나머지를 구한다.
- 강사님 회식비 문제에는 `100000만원` 표현과 미완성 출력문이 있다.
- 내 코드는 이를 `100,000원`으로 해석하고 인당 금액과 주최자 부담액을 계산했다.
- 내 코드와 강사님 코드는 대부분 동일하며 후반부 설명과 문제 풀이에서 차이가 있다.
