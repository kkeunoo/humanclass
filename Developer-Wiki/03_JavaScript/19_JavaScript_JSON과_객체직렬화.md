# JavaScript JSON과 객체 직렬화

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `19_JavaScript_JSON과_객체직렬화.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `18_JavaScript_BOM과_지도우편번호API.md` |
| 다음 학습 | 이후 JavaScript 원본 순서에 따라 진행 |
| 원본 기준 | `workspace/workspace_html/javascript/19_json.html`, `workspace_teacher/workspace_html/javascript/19_json.html` |
| 핵심 범위 | JavaScript 객체, JSON 문법, bracket·dot notation, 중첩 객체, 함수 property, property 추가·수정·삭제, `JSON.stringify()`, `JSON.parse()`, 객체 배열, `for...of`, `for...in`, `Object.keys()` |
| 프로젝트 연결 | API 요청·응답, localStorage 저장, 서버 데이터 변환, 설정 파일, 객체 목록 순회, 데이터 직렬화 |

> 이 문서는 내 코드와 강사님 코드의 `19_json.html`만 직접 비교했습니다. 두 원본 모두 JavaScript 객체를 반복해서 “JSON”이라고 부르지만, 함수 property·따옴표 없는 key·single quote·trailing comma를 사용하는 현재 값은 엄밀히 JSON이 아니라 JavaScript 객체 literal입니다. 강사님 코드에는 중첩 객체의 `k: 3`이 존재해 `json.k1.k`가 `3`을 출력하지만, 내 코드에서는 해당 property가 빠져 있어 `undefined`가 출력됩니다. 원본 표현과 오류는 보존하고 JavaScript 객체와 JSON text의 차이를 분리해 설명합니다.

---

# 학습 목표

- JavaScript 객체와 JSON 문자열의 차이를 설명한다.
- 객체 literal의 key와 value 구조를 이해한다.
- bracket notation과 dot notation을 구분한다.
- hyphen이 포함된 property key에 접근하는 방법을 이해한다.
- 존재하지 않는 property가 `undefined`를 반환하는 이유를 설명한다.
- 객체 property를 추가·수정·삭제한다.
- 함수가 들어 있는 객체와 JSON 형식의 차이를 이해한다.
- `JSON.stringify()`의 변환 규칙을 이해한다.
- `JSON.parse()`가 유효한 JSON text만 처리한다는 점을 이해한다.
- 객체 배열을 `for...of`와 `for...in`으로 순회한다.
- `Object.keys()`로 own enumerable string key를 배열로 얻는다.
- 내 코드와 강사님 코드의 실제 출력 차이를 정확히 기록한다.

---

# Core Concepts

## 1. 원본에서 말하는 JSON

원본 주석:

```js
// json
// 값을 key와 value로 관리
// 순서는 보장하지 않는다
```

두 파일은 다음 변수를 사용합니다.

```js
let json = {}

json = {
  "key": "value",
  "num": 1234,
  "fn": function() {
    console.log(1)
  },
  "k1": {
    "k1-1": 1,
    "k1-2": 2
  },
  k2: "k3"
}
```

변수 이름은 `json`이지만 실제 값은 JavaScript 객체입니다.

---

## 2. JavaScript 객체와 JSON의 차이

JavaScript 객체 literal은 JavaScript 코드 안에서 사용하는 값입니다.

```js
const user = {
  name: "홍길동",
  age: 20,
  greet() {
    console.log("안녕하세요")
  }
}
```

JSON은 데이터를 문자열로 표현하는 형식입니다.

```json
{
  "name": "홍길동",
  "age": 20
}
```

JSON에서는 다음을 사용할 수 없습니다.

```text
함수
undefined
Symbol
따옴표 없는 property name
single quote 문자열
주석
trailing comma
```

따라서 원본 객체는 그대로는 JSON text가 아닙니다.

---

## 3. “닫는 태그를 줄이기 위해 JSON 사용” 설명

내 원본 주석:

```js
// json (닫는태그 등 줄여서 간결하게 하기 위해서 사용)
```

JSON의 주된 목적은 HTML 닫는 tag를 줄이는 것이 아닙니다.

JSON은 구조화된 데이터를 text로 교환하거나 저장하기 위한 형식입니다.

대표 사용처:

- API 요청과 응답
- 설정 파일
- localStorage 저장
- 서버와 client 간 데이터 교환
- 다른 언어와 데이터 공유

---

## 4. 객체 선언

원본:

```js
let json = {}
```

빈 객체를 만든 뒤 새 객체를 다시 대입합니다.

```js
json = {
  "key": "value"
}
```

처음부터 작성할 수도 있습니다.

```js
const json = {
  key: "value"
}
```

재할당이 필요 없다면 `const`가 적절합니다.

---

## 5. Key와 Value

객체는 property의 집합입니다.

```js
{
  "key": "value",
  "num": 1234
}
```

각 property:

```text
key → "key"
value → "value"

key → "num"
value → 1234
```

JavaScript 객체의 property key는 string 또는 Symbol입니다.

숫자처럼 작성한 key도 일반적으로 string key로 처리됩니다.

---

## 6. Value에 들어갈 수 있는 값

내 원본 주석:

```js
// value에는 변수에 담을 수 있는 모든것이 들어감
// 함수, 변수 등
```

JavaScript 객체 value에는 대부분의 JavaScript 값을 넣을 수 있습니다.

```js
const object = {
  number: 1,
  string: "text",
  boolean: true,
  nothing: null,
  missing: undefined,
  array: [1, 2],
  nested: {},
  fn: function() {}
}
```

하지만 JSON value는 다음 여섯 유형만 표현할 수 있습니다.

```text
string
number
boolean
null
object
array
```

---

## 7. Property 순서

원본은 순서를 보장하지 않는다고 설명합니다.

실무적으로 객체를 array처럼 순서 중심 자료구조로 사용하면 안 된다는 취지는 타당합니다.

다만 현대 JavaScript에는 own property key 열거 순서에 대한 규칙이 있습니다.

대략:

1. 정수 index 형태 key
2. 나머지 string key의 생성 순서
3. Symbol key의 생성 순서

그래도 의미 있는 순서가 중요하다면 array를 사용하는 편이 명확합니다.

---

# Syntax / Comparison

## 8. Bracket Notation

원본:

```js
console.log(
  json["key"]
)

console.log(
  json["num"]
)

console.log(
  json["k1"]["k1-1"]
)
```

bracket notation은 key를 문자열로 전달합니다.

장점:

- hyphen 포함 key 접근 가능
- space 포함 key 접근 가능
- 변수에 저장된 동적 key 접근 가능

```js
const keyName = "num"

console.log(
  json[keyName]
)
```

---

## 9. Dot Notation

원본:

```js
console.log(
  json.key
)
```

identifier 문법에 맞는 property name은 dot notation으로 접근할 수 있습니다.

```js
json.num
json.k1
json.fn
```

---

## 10. Hyphen Property

원본 key:

```js
"k1-2": 2
```

다음 코드는 원하는 property 접근이 아닙니다.

```js
json.k1.k1 - 2
```

JavaScript는 `-`를 subtraction operator로 해석합니다.

원본에 주석 처리된 표현:

```js
// json.k1.k1-2
```

실행하면 단순히 “hyphen key라서 NaN”이라고만 설명하기 어렵습니다.

실제 해석은 대략 다음과 같습니다.

```js
(json.k1.k1) - 2
```

`json.k1.k1`이 `undefined`라면:

```text
undefined - 2
→ NaN
```

올바른 접근:

```js
json.k1["k1-2"]
```

---

## 11. 중첩 객체

강사님 코드:

```js
"k1": {
  "k1-1": 1,
  "k1-2": 2,
  k: 3
}
```

따라서:

```js
json.k1.k
```

결과:

```text
3
```

---

## 12. 내 코드의 누락된 K Property

내 코드:

```js
"k1": {
  "k1-1": 1,
  "k1-2": 2
}
```

`k` property가 없습니다.

그런데 다음 코드는 그대로 실행합니다.

```js
console.log(
  "json.k1.k : ",
  json.k1.k
)
```

결과:

```text
undefined
```

강사님은 `3`, 나는 `undefined`가 출력되는 중요한 실제 차이입니다.

---

## 13. 함수 Property

원본:

```js
"fn": function() {
  console.log(1)
}
```

호출 방법:

```js
json["fn"]()
json.fn()
```

두 호출 모두 같은 함수를 실행해 `1`을 출력합니다.

함수가 객체 property에 저장되어 있을 때 method라고 부를 수 있습니다.

---

## 14. Object를 String과 결합

원본:

```js
console.log(
  "" + json
)
```

일반 객체는 문자열 변환 시 기본적으로 다음과 비슷한 결과가 나옵니다.

```text
[object Object]
```

객체 내용을 JSON 문자열로 확인하려면:

```js
JSON.stringify(json)
```

을 사용할 수 있습니다.

Console에서는 객체 자체를 전달하는 편이 디버깅에 더 좋습니다.

```js
console.log(json)
```

---

## 15. Property 수정

원본:

```js
json.num = 456
```

기존 `num` property가 있으므로 값이 `1234`에서 `456`으로 바뀝니다.

```text
기존 key
→ value 수정
```

---

## 16. 존재하지 않는 Property

원본:

```js
console.log(
  json.num2
)
```

`num2`가 아직 없으므로:

```text
undefined
```

가 출력됩니다.

이는 undeclared identifier를 읽는 것과 다릅니다.

```js
console.log(num2)
```

변수 자체가 선언되지 않았다면 `ReferenceError`가 발생할 수 있습니다.

---

## 17. Property 추가

원본:

```js
json.num2 = 222
```

`num2`가 없으므로 새 property가 추가됩니다.

내 코드는:

```js
console.log(
  json.num2
)
```

를 한 번 더 실행해 `222`를 직접 출력합니다.

강사님 코드는 추가 후 객체 전체만 출력합니다.

---

## 18. Array Push와 객체 Property 추가

내 주석:

```js
// 배열의 push처럼 넣지 않아도,
// 값을 넣으면 자동적으로 들어감
```

객체에는 array의 `push()`처럼 순서 끝에 넣는 개념이 핵심이 아닙니다.

property key를 지정해 추가합니다.

```js
object.newKey =
  newValue
```

computed key:

```js
const key =
  "newKey"

object[key] =
  newValue
```

---

# JSON 직렬화와 역직렬화

## 19. 직렬화

객체를 전송·저장 가능한 문자열 표현으로 바꾸는 작업을 직렬화라고 합니다.

원본:

```js
const str =
  JSON.stringify(json)
```

`JSON.stringify()`는 JavaScript 값을 JSON 문자열로 변환합니다.

---

## 20. 함수 Property 제외

원본 객체에는 함수가 있습니다.

```js
fn: function() {
  console.log(1)
}
```

`JSON.stringify()` 결과에서 객체 property value가 함수라면 해당 property는 제외됩니다.

예상 구조:

```json
{
  "key": "value",
  "num": 456,
  "k1": {
    "k1-1": 1,
    "k1-2": 2
  },
  "k2": "k3",
  "num2": 222
}
```

강사님 결과에는 중첩 `k: 3`도 포함됩니다.

---

## 21. Stringify의 추가 규칙

객체 property에서 다음 value도 일반적으로 제외됩니다.

```text
undefined
function
Symbol
```

array 안에서는 해당 값들이 `null`로 바뀔 수 있습니다.

```js
JSON.stringify([
  undefined,
  function() {},
  Symbol()
])
```

결과:

```json
[null,null,null]
```

`NaN`과 `Infinity`도 JSON에서는 숫자로 표현할 수 없어 `null`이 됩니다.

`BigInt`는 기본적으로 stringify 시 `TypeError`를 발생시킵니다.

---

## 22. Network는 “무조건 문자”인가?

원본 주석:

```js
// 네트워크 통신할 때 무조건 문자로 전송한다
```

학습 단계에서는 JSON payload가 text 형태라는 뜻으로 이해할 수 있습니다.

하지만 네트워크는 byte를 전송하며 다음과 같은 다양한 형식을 사용할 수 있습니다.

- JSON text
- form data
- binary image
- ArrayBuffer
- Blob
- Protocol Buffers

따라서 모든 네트워크 데이터가 반드시 JavaScript string이라는 의미는 아닙니다.

---

## 23. 역직렬화

원본:

```js
const json2 =
  JSON.parse(str)
```

JSON text를 JavaScript 값으로 변환합니다.

결과는 문자열이 아니라 JavaScript object입니다.

함수 property는 stringify 단계에서 빠졌으므로 `json2.fn`은 존재하지 않습니다.

---

## 24. Parse 오류

원본에 주석 처리:

```js
// JSON.parse("<h1>")
```

`"<h1>"`은 유효한 JSON text가 아니므로 `SyntaxError`가 발생합니다.

유효한 JSON string value로 parsing하려면 문자열 자체를 JSON의 double quote로 감싸야 합니다.

```js
JSON.parse(
  '"<h1>"'
)
```

결과:

```text
<h1>
```

---

## 25. JSON.parse("{}")

원본:

```js
let j =
  JSON.parse("{}")
```

결과:

```js
{}
```

빈 JavaScript object가 만들어집니다.

내 코드는 이를 Console에 출력합니다.

강사님 코드는 변수에 대입만 합니다.

---

## 26. JSON.parse("[{}]")

원본:

```js
j =
  JSON.parse("[{}]")
```

결과:

```js
[
  {}
]
```

빈 객체 하나를 가진 array가 만들어집니다.

내 코드는 이를 Console에 출력하고 강사님은 출력하지 않습니다.

---

## 27. JSON 문법 규칙

올바른 JSON:

```json
{
  "name": "홍길동",
  "age": 20,
  "active": true,
  "address": null,
  "skills": ["HTML", "CSS"]
}
```

핵심 규칙:

- property name은 double quote
- string도 double quote
- comment 불가
- trailing comma 불가
- function 불가
- `undefined`, `NaN`, `Infinity` 불가

---

# 객체 배열과 순회

## 28. Temple 배열

양쪽 원본:

```js
const temple = [
  {
    이름: "그랜절",
    주소: "광장",
    가격: 300000
  },
  {
    이름: "만우절",
    주소: "없음",
    가격: 2147483647
  }
]
```

이는 JSON text가 아니라 JavaScript object 두 개를 담은 array입니다.

property name으로 한글도 사용할 수 있습니다.

---

## 29. For...of

원본:

```js
for (
  let t of temple
) {
  console.log(
    t.이름
  )
}
```

`for...of`는 array의 value를 순회합니다.

출력:

```text
그랜절
만우절
```

---

## 30. For...in

원본:

```js
for (
  let i in temple
) {
  console.log(
    temple[i].가격
  )
}
```

`for...in`은 enumerable key를 순회합니다.

array에서는 key가 `"0"`, `"1"`처럼 전달됩니다.

출력:

```text
300000
2147483647
```

array value 순회에는 일반적으로 `for...of`, `forEach()`, `map()`이 더 의도에 맞습니다.

---

## 31. Object.keys()

원본:

```js
const keys =
  Object.keys(json)

console.log(keys)
```

`Object.keys()`는 객체 자신의 enumerable string key를 array로 반환합니다.

삭제 전 key는 파일별로 다릅니다.

강사님:

```text
key
num
fn
k1
k2
num2
```

내 코드도 최상위 key 목록은 같습니다.

중첩 `k`의 존재 여부는 최상위 `Object.keys(json)`에는 영향을 주지 않습니다.

---

## 32. Property 삭제

원본:

```js
delete json.num
```

`num` property를 객체에서 제거합니다.

그 후:

```js
console.log(json)
```

객체에서 `num`이 사라진 상태를 확인합니다.

---

## 33. “실무에서는 실제 삭제하지 않는다” 설명

내 주석:

```js
// key 삭제
// 실무해서는 실제 삭제하지는 않음
```

실무에서도 `delete`를 사용할 수 있습니다.

다만 immutable update나 새 객체 생성 방식을 사용하는 경우도 많습니다.

```js
const {
  num,
  ...rest
} = json
```

`rest`에는 `num`을 제외한 property가 들어갑니다.

“실무에서 delete를 사용하지 않는다”라고 단정하기보다 상태 관리 방식과 성능·설계에 따라 선택한다고 설명하는 편이 정확합니다.

---

# HTML과 데이터 표현

## 34. Custom Element 형태

양쪽 body:

```html
<year cen="20">
  1999
</year>

<month>
  03
</month>

<day>
  02
</day>
```

HTML parser는 알 수 없는 tag도 element로 만들 수 있습니다.

그러나 의미 있는 표준 HTML 요소나 Web Components의 custom element naming 규칙을 사용하는 편이 좋습니다.

custom element 이름은 일반적으로 hyphen을 포함해야 합니다.

```html
<birth-year></birth-year>
```

---

## 35. Teacher Body 설명

강사님 body:

```text
[1~4] : 년도
[5~6] : 월
[7~8] : 일

19990302
```

날짜 문자열의 위치별 의미를 먼저 보여 줍니다.

내 body에는 이 세 줄이 없습니다.

---

## 36. Teacher의 객체형 표현

강사님 body:

```text
{year: {cen:20, value:1999},month:03,day:02}
```

이것은 JavaScript object처럼 보이는 설명용 text입니다.

JSON이라면 key와 string value에 double quote가 필요하고 `03`, `02` 같은 leading zero number는 허용되지 않습니다.

올바른 JSON 예:

```json
{
  "year": {
    "cen": 20,
    "value": 1999
  },
  "month": "03",
  "day": "02"
}
```

---

## 37. 내 Body 표현

내 body:

```text
JSON : {year: {cen="20"} 1999,month:03,day:02}
```

이 문자열은 유효한 JSON도 JavaScript object literal도 아닙니다.

문제:

- key에 double quote 없음
- `cen="20"`은 object property 문법이 아님
- `}` 뒤에 comma나 property key 없이 `1999` 등장
- `03`, `02`는 JSON number로 부적절
- 구조 구분이 불명확

원본의 의도는 year tag의 attribute와 text를 object 구조로 표현하려는 것으로 보입니다.

---

# My Code vs Teacher Code

## 38. 비교표

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 핵심 흐름 | 동일 | 동일 |
| 설명 주석 | 매우 상세 | 간결 |
| 중첩 `k` property | 없음 | `k: 3` 있음 |
| `json.k1.k` 결과 | `undefined` | `3` |
| `num2` 추가 후 출력 | `json.num2`와 객체 모두 출력 | 객체만 출력 |
| `JSON.parse("{}")` 출력 | 출력함 | 출력하지 않음 |
| `JSON.parse("[{}]")` 출력 | 출력함 | 출력하지 않음 |
| Parse 오류 설명 | 상세 error 주석 | 호출 예만 주석 |
| Temple 주석 | 객체 배열 사용 설명 추가 | 없음 |
| Delete 주석 | 실무에서는 실제 삭제하지 않는다고 설명 | 단순 삭제 설명 |
| 날짜 위치 설명 | 없음 | 년·월·일 위치 표시 |
| 마지막 객체 표현 | 문법상 잘못된 `JSON : ...` | 설명용 객체형 text |
| 전체 formatting | 들여쓰기 깊음 | 일반적인 들여쓰기 |

---

# My Code Analysis

## 39. 내 코드 장점

- 객체와 key·value 구조에 대한 설명을 많이 추가했다.
- bracket notation과 dot notation을 구분했다.
- hyphen key가 dot notation에서 문제가 된다는 점을 설명하려 했다.
- 존재하지 않는 property가 `undefined`라는 점을 기록했다.
- property 추가와 수정의 차이를 설명했다.
- stringify가 함수 property를 제외한다는 점을 기록했다.
- parse error message를 구체적으로 남겼다.
- 빈 객체 JSON과 객체 배열 JSON을 직접 출력했다.
- 객체 배열을 `for...of`와 `for...in`으로 순회했다.
- `Object.keys()`와 `delete`를 실습했다.

---

## 40. 내 코드 개선점

- JavaScript 객체를 계속 JSON이라고 부른다.
- JSON의 목적을 HTML 닫는 tag 축소와 연결한 설명이 부정확하다.
- JSON value에 함수도 들어갈 수 있는 것처럼 설명한다.
- `json.k1.k`를 출력하지만 실제 `k` property가 없어 `undefined`가 나온다.
- hyphen key 설명에서 “value값에 -가 있다”고 했지만 문제는 property key이다.
- `json.k1.k1-2`가 단순히 key를 찾는 표현처럼 설명되어 있다.
- 네트워크 통신은 무조건 문자라고 단정한다.
- parse가 문자열을 “다시 JSON으로” 만든다고 설명하지만 결과는 JavaScript 값이다.
- 객체 배열을 “JSON 배열”이라고 부른다.
- 실무에서는 delete를 사용하지 않는다고 단정한다.
- 마지막 `JSON : ...` text가 유효한 JSON이 아니다.
- `lang="en"`과 `<title>Document</title>`이 내용에 맞지 않는다.

---

# Teacher Code Analysis

## 41. 강사님 코드 장점

- 객체 생성부터 접근·수정·추가·삭제까지 순서가 간결하다.
- 중첩 객체에 `k: 3`을 실제로 선언해 `json.k1.k` 접근이 정상 동작한다.
- bracket notation과 dot notation을 직접 비교한다.
- 함수 property를 두 방식으로 호출한다.
- stringify와 parse의 기본 왕복 흐름을 보여 준다.
- 객체 배열을 두 반복문으로 순회한다.
- Object.keys와 delete를 포함한다.
- body에서 날짜 문자열을 구조화된 데이터로 바꾸려는 개념을 보여 준다.

---

## 42. 강사님 코드 개선점

- JavaScript 객체와 JSON을 구분하지 않는다.
- 객체에 함수·single quote·trailing comma가 있어도 JSON이라고 부른다.
- property 순서 설명이 지나치게 단순하다.
- stringify의 제외·변환 규칙을 함수 외에는 설명하지 않는다.
- parse 실패를 자세히 설명하지 않는다.
- `for...in`을 array에 사용할 때 주의점을 설명하지 않는다.
- 마지막 body 표현은 JSON이 아니다.
- `03`, `02`를 number처럼 작성한 설명은 JSON 문법에 맞지 않는다.
- custom tag의 의미와 제약을 설명하지 않는다.
- `lang="en"`과 title이 내용에 맞지 않는다.

---

# Improvements

## 43. 올바른 객체와 JSON 구분

JavaScript 객체:

```js
const user = {
  name: "홍길동",
  age: 20,
  greet() {
    console.log("안녕하세요")
  }
}
```

직렬화:

```js
const jsonText =
  JSON.stringify(user)
```

결과:

```json
{"name":"홍길동","age":20}
```

함수 `greet`는 빠집니다.

역직렬화:

```js
const parsedUser =
  JSON.parse(jsonText)
```

`parsedUser`는 JavaScript object이며 method는 복구되지 않습니다.

---

## 44. 안전한 Parse

```js
function parseJSON(text) {
  try {
    return JSON.parse(text)
  } catch (error) {
    console.error(
      "JSON 형식이 올바르지 않습니다.",
      error
    )

    return null
  }
}
```

외부에서 받은 JSON text는 형식 오류 가능성을 고려해야 합니다.

---

## 45. Replacer

특정 property만 stringify할 수 있습니다.

```js
const text =
  JSON.stringify(
    json,
    [
      "key",
      "num",
      "k1"
    ]
  )
```

또는 function replacer:

```js
const text =
  JSON.stringify(
    json,
    function(key, value) {
      if (
        typeof value ===
        "function"
      ) {
        return undefined
      }

      return value
    }
  )
```

---

## 46. Pretty Print

```js
const pretty =
  JSON.stringify(
    json,
    null,
    2
  )
```

결과를 2-space indentation으로 읽기 좋게 만듭니다.

---

## 47. Reviver

parse할 때 값을 변환할 수 있습니다.

```js
const data =
  JSON.parse(
    '{"price":"300000"}',
    function(key, value) {
      if (key === "price") {
        return Number(value)
      }

      return value
    }
  )
```

---

# Representative Examples

## 48. API Data 예제

```js
const products = [
  {
    id: 1,
    name: "키보드",
    price: 50000
  },
  {
    id: 2,
    name: "마우스",
    price: 30000
  }
]

const requestBody =
  JSON.stringify(products)

console.log(
  requestBody
)
```

server에서 받은 JSON text:

```js
const responseText = `
[
  {
    "id": 1,
    "name": "키보드",
    "price": 50000
  }
]
`

const responseData =
  JSON.parse(
    responseText
  )
```

---

# Practical Usage

## 49. LocalStorage 저장

`localStorage`는 string을 저장합니다.

```js
const settings = {
  theme: "dark",
  fontSize: 16
}

localStorage.setItem(
  "settings",
  JSON.stringify(settings)
)
```

읽기:

```js
const saved =
  localStorage.getItem(
    "settings"
  )

const settings =
  saved === null
    ? null
    : JSON.parse(saved)
```

---

## 50. Fetch 요청 Body

```js
fetch(
  "/api/users",
  {
    method: "POST",
    headers: {
      "Content-Type":
        "application/json"
    },
    body:
      JSON.stringify({
        name: "홍길동",
        age: 20
      })
  }
)
```

`body`에는 JSON text가 들어갑니다.

원본에는 없는 실무 확장 예제입니다.

---

# Common Mistakes

## 51. 자주 하는 실수

### 51.1 객체를 모두 JSON이라고 부름

JavaScript object와 JSON text는 서로 다른 개념입니다.

### 51.2 JSON에 함수가 들어갈 수 있다고 생각

JSON 문법에는 함수가 없습니다.

### 51.3 Single Quote를 JSON에서 사용

JSON string은 double quote만 허용합니다.

### 51.4 Hyphen Key를 Dot Notation으로 접근

bracket notation을 사용해야 합니다.

### 51.5 존재하지 않는 Property와 미선언 변수를 혼동

전자는 `undefined`, 후자는 `ReferenceError`가 될 수 있습니다.

### 51.6 Stringify 후 함수가 유지된다고 생각

객체 property의 함수는 제외됩니다.

### 51.7 Parse가 어떤 문자열이든 처리한다고 생각

유효한 JSON text만 parsing할 수 있습니다.

### 51.8 Array에 For...in을 기본으로 사용

value 순회에는 `for...of`가 더 적합합니다.

### 51.9 Object.keys가 중첩 Key까지 모두 반환한다고 생각

현재 객체의 own enumerable string key만 반환합니다.

### 51.10 Leading Zero Number를 JSON에 작성

`03`, `02`는 유효한 JSON number가 아닙니다. 문자열 `"03"`, `"02"`로 표현해야 합니다.

---

# Interview / Review

## 52. 면접·복습 포인트

### Q1. JavaScript 객체와 JSON의 차이는 무엇인가요?

JavaScript 객체는 실행 중 사용하는 값이고 JSON은 구조화된 데이터를 표현하는 문자열 형식입니다.

### Q2. JSON에서 함수가 허용되나요?

허용되지 않습니다.

### Q3. Hyphen이 포함된 Key에는 어떻게 접근하나요?

bracket notation을 사용합니다.

```js
object["user-name"]
```

### Q4. 존재하지 않는 Property를 읽으면 무엇이 나오나요?

일반적으로 `undefined`가 나옵니다.

### Q5. JSON.stringify는 무엇을 하나요?

JavaScript 값을 JSON 문자열로 직렬화합니다.

### Q6. 함수 Property는 Stringify 결과에 어떻게 되나요?

객체 property라면 제외됩니다.

### Q7. JSON.parse는 무엇을 반환하나요?

JSON text에 따라 JavaScript object, array, string, number, boolean 또는 null을 반환합니다.

### Q8. For...of와 For...in 차이는 무엇인가요?

for...of는 iterable value를 순회하고 for...in은 enumerable property key를 순회합니다.

### Q9. Object.keys는 무엇을 반환하나요?

own enumerable string key의 array를 반환합니다.

### Q10. 내 코드와 강사님 코드의 핵심 실행 차이는 무엇인가요?

강사님 중첩 객체에는 `k: 3`이 있어 `json.k1.k`가 3이고, 내 코드에는 없어 undefined입니다.

---

# Problems

## 문제 1. 객체 선언

이름과 나이를 가진 JavaScript 객체를 선언하세요.

## 문제 2. JSON Text

문제 1의 객체와 같은 데이터를 유효한 JSON text로 작성하세요.

## 문제 3. Bracket Notation

`"user-name"` property 값을 출력하세요.

## 문제 4. Dot Notation

`user.age`를 출력하세요.

## 문제 5. 중첩 Property

중첩 객체의 `address.city`를 출력하세요.

## 문제 6. 존재하지 않는 Property

없는 property를 읽을 때 결과를 설명하세요.

## 문제 7. Property 수정

age를 20에서 21로 바꾸세요.

## 문제 8. Property 추가

active property에 true를 추가하세요.

## 문제 9. Property 삭제

active property를 삭제하세요.

## 문제 10. 함수 Property

객체에 `greet()` 함수를 넣고 두 접근 방식으로 호출하세요.

## 문제 11. String 변환

일반 객체에 `"" + object`를 실행했을 때 대표 결과를 설명하세요.

## 문제 12. Stringify

JavaScript 객체를 JSON 문자열로 변환하세요.

## 문제 13. 함수 제외

함수 property가 stringify 결과에서 어떻게 되는지 설명하세요.

## 문제 14. Parse

JSON 문자열을 JavaScript 객체로 변환하세요.

## 문제 15. Parse 오류

`JSON.parse("<h1>")`가 실패하는 이유를 설명하세요.

## 문제 16. 빈 객체 Parse

`"{}"`를 parsing하세요.

## 문제 17. 객체 배열 Parse

`"[{}]"`를 parsing하세요.

## 문제 18. For...of

객체 배열의 모든 이름을 출력하세요.

## 문제 19. For...in

객체의 모든 key를 순회하세요.

## 문제 20. Object.keys

객체 key 배열을 만드세요.

## 문제 21. 원본 차이

내 코드에서 `json.k1.k`가 undefined인 이유를 설명하세요.

## 문제 22. 종합 설정 저장

다음 요구사항을 만족하세요.

- 설정 객체에 theme, fontSize, notifications 저장
- JSON.stringify로 문자열 변환
- localStorage에 저장
- 다시 읽기
- 값이 없으면 기본 객체 사용
- JSON.parse 실패를 try...catch로 처리
- 복원된 객체의 theme 출력
- 함수는 저장하지 않음

---

# Answers

## 정답 1

```js
const user = {
  name: "홍길동",
  age: 20
}
```

## 정답 2

```json
{
  "name": "홍길동",
  "age": 20
}
```

## 정답 3

```js
const user = {
  "user-name":
    "홍길동"
}

console.log(
  user["user-name"]
)
```

## 정답 4

```js
console.log(
  user.age
)
```

## 정답 5

```js
const user = {
  address: {
    city: "서울"
  }
}

console.log(
  user.address.city
)
```

## 정답 6

```js
console.log(
  user.missing
)
```

결과는 일반적으로 `undefined`입니다.

## 정답 7

```js
user.age = 21
```

## 정답 8

```js
user.active = true
```

## 정답 9

```js
delete user.active
```

## 정답 10

```js
const user = {
  greet:
    function() {
      console.log(
        "안녕하세요"
      )
    }
}

user.greet()
user["greet"]()
```

## 정답 11

일반 객체의 기본 문자열 변환 결과는 대체로 다음과 같습니다.

```text
[object Object]
```

## 정답 12

```js
const text =
  JSON.stringify(user)
```

## 정답 13

객체 property value가 함수이면 해당 property는 stringify 결과에서 제외됩니다.

## 정답 14

```js
const user =
  JSON.parse(
    '{"name":"홍길동"}'
  )
```

## 정답 15

`<h1>`은 JSON 문법에 맞는 object, array, string, number, boolean, null 표현이 아니기 때문입니다.

## 정답 16

```js
const emptyObject =
  JSON.parse("{}")
```

## 정답 17

```js
const objectArray =
  JSON.parse("[{}]")
```

## 정답 18

```js
for (
  const item of users
) {
  console.log(
    item.name
  )
}
```

## 정답 19

```js
for (
  const key in user
) {
  if (
    Object.hasOwn(
      user,
      key
    )
  ) {
    console.log(
      key,
      user[key]
    )
  }
}
```

## 정답 20

```js
const keys =
  Object.keys(user)
```

## 정답 21

내 `json.k1` 객체에는 `"k1-1"`과 `"k1-2"`만 있고 `k` property가 선언되지 않았기 때문에 `json.k1.k`는 `undefined`입니다.

## 정답 22

```js
const defaultSettings = {
  theme: "light",
  fontSize: 16,
  notifications: true
}

function saveSettings(
  settings
) {
  const text =
    JSON.stringify(
      settings
    )

  localStorage.setItem(
    "settings",
    text
  )
}

function loadSettings() {
  const text =
    localStorage.getItem(
      "settings"
    )

  if (text === null) {
    return {
      ...defaultSettings
    }
  }

  try {
    return JSON.parse(text)
  } catch (error) {
    console.error(
      "설정 JSON을 읽지 못했습니다.",
      error
    )

    return {
      ...defaultSettings
    }
  }
}

saveSettings({
  theme: "dark",
  fontSize: 18,
  notifications: false
})

const settings =
  loadSettings()

console.log(
  settings.theme
)
```

---

# Final Checklist

## 객체

- [ ] JavaScript 객체와 JSON을 구분했다.
- [ ] key와 value를 이해했다.
- [ ] bracket notation과 dot notation을 구분했다.
- [ ] hyphen key에 bracket notation을 사용했다.
- [ ] 존재하지 않는 property와 미선언 변수를 구분했다.
- [ ] property를 추가·수정·삭제했다.
- [ ] 함수 property를 호출했다.
- [ ] 의미 있는 순서가 필요할 때 array를 사용했다.

## Stringify와 Parse

- [ ] JSON.stringify가 문자열을 반환함을 이해했다.
- [ ] 함수 property가 제외됨을 이해했다.
- [ ] undefined, Symbol, NaN, Infinity 처리도 확인했다.
- [ ] BigInt stringify 오류를 인지했다.
- [ ] JSON.parse가 JavaScript 값을 반환함을 이해했다.
- [ ] parse 실패를 try...catch로 처리했다.
- [ ] JSON property name과 string에 double quote를 사용했다.
- [ ] comment와 trailing comma를 JSON에 넣지 않았다.
- [ ] leading zero number를 문자열로 표현했다.

## 순회

- [ ] 객체 배열에 for...of를 사용했다.
- [ ] for...in이 key를 순회함을 이해했다.
- [ ] Object.keys가 key array를 반환함을 이해했다.
- [ ] Object.keys가 중첩 key를 자동으로 펼치지 않음을 이해했다.
- [ ] own property 확인이 필요한 상황을 이해했다.

## 원본 검수

- [ ] 두 실제 19_json.html만 비교했다.
- [ ] 강사님 `k: 3`과 내 누락 차이를 기록했다.
- [ ] 내 `json.k1.k` 결과가 undefined임을 기록했다.
- [ ] num2 출력 차이를 기록했다.
- [ ] parse 결과 Console 출력 차이를 기록했다.
- [ ] teacher의 날짜 위치 설명 차이를 기록했다.
- [ ] 두 body의 마지막 표현이 JSON이 아님을 기록했다.
- [ ] 내 잘못된 `cen="20"` 구조를 기록했다.
- [ ] JavaScript 객체를 JSON이라고 부르는 공통 문제를 기록했다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 19번은 객체 property와 JSON 직렬화·역직렬화를 다룬다.
- 원본 변수 이름은 `json`이지만 실제 값은 JavaScript object이다.
- JavaScript 객체와 JSON 문자열은 서로 다른 개념이다.
- JavaScript 객체는 함수, undefined, Symbol 등을 value로 가질 수 있다.
- JSON은 string, number, boolean, null, object, array만 표현한다.
- JSON property name과 string은 double quote를 사용해야 한다.
- JSON에는 함수, comment, trailing comma, single quote를 사용할 수 없다.
- bracket notation은 hyphen이나 동적 key 접근에 적합하다.
- `json.k1["k1-2"]`는 올바르지만 `json.k1.k1-2`는 subtraction으로 해석된다.
- 강사님 `json.k1`에는 `k: 3`이 있어 `json.k1.k`가 3이다.
- 내 `json.k1`에는 k가 없어 같은 표현이 undefined다.
- 객체의 존재하지 않는 property는 일반적으로 undefined다.
- 미선언 identifier를 직접 읽는 것은 ReferenceError가 될 수 있다.
- 기존 property에 값을 넣으면 수정되고 없는 key에 넣으면 추가된다.
- `"" + object`의 대표 결과는 `[object Object]`이다.
- `JSON.stringify()`는 JavaScript 값을 JSON 문자열로 직렬화한다.
- 객체 property의 함수, undefined, Symbol은 stringify 결과에서 제외될 수 있다.
- `NaN`과 `Infinity`는 JSON에서 null로 변환된다.
- `JSON.parse()`는 유효한 JSON text를 JavaScript 값으로 바꾼다.
- `JSON.parse("<h1>")`는 유효한 JSON이 아니므로 SyntaxError가 발생한다.
- `JSON.parse("{}")`는 빈 객체를 반환한다.
- `JSON.parse("[{}]")`는 빈 객체 하나를 가진 array를 반환한다.
- temple은 JSON 문자열이 아니라 JavaScript 객체 배열이다.
- `for...of`는 array value를 순회한다.
- `for...in`은 enumerable key를 순회한다.
- `Object.keys()`는 own enumerable string key의 array를 반환한다.
- `delete`는 객체 property를 제거한다.
- 실무에서 delete 사용 여부는 상태 관리 방식과 설계에 따라 달라진다.
- 강사님 body의 객체형 text도 엄밀히 JSON이 아니다.
- 내 body의 `JSON : {year: {cen="20"} 1999,...}`는 JSON과 JavaScript object 문법 모두에 맞지 않는다.
