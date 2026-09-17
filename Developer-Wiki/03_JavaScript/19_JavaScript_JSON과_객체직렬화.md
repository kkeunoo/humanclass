---
title: JavaScript JSON과 객체 직렬화
version: v4.0-detailed-source
last_updated: 2026-09-17
status: Completed
---

# JavaScript JSON과 객체 직렬화

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `19_JavaScript_JSON과_객체직렬화.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/19_json.html`, `workspace_teacher/workspace_html/javascript/19_json.html` |
| 핵심 범위 | 객체 Literal, Property 접근, 중첩 객체, Property 추가·수정·삭제, `JSON.stringify()`, `JSON.parse()`, 객체 배열, 객체 순회 |
| 실습 범위 | 객체 조회·변경, 직렬화·역직렬화, JSON 오류 처리, 객체 배열 출력, Local Storage 저장 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 원본은 JavaScript 객체를 반복해서 “JSON”이라고 표현한다.  
> 이 문서에서는 **JavaScript 객체 값**과 **JSON 형식의 문자열**을 정확히 분리하고, 저장·전송 과정에서 어떤 값이 사라지거나 변환되는지 함께 설명한다.

---

## 이 문서에서 바로 찾기

- [개념에서 실제 실행까지: 객체는 JavaScript 값이고 JSON은 데이터를 표현하는 문자열 형식이다](#js-19-section-4)
- [71. 내 코드와 강사님 코드 비교](#js-19-section-75)
- [73. 실무형 예제: 설정 저장소](#js-19-section-77)
- [74. 대표 오류로 이해하기](#js-19-section-78)
- [75. 자주 하는 실수](#js-19-section-79)
- [76. 핵심 요약](#js-19-section-80)
- [77. 최종 체크리스트](#js-19-section-81)

<details>
<summary>세부 목차 펼치기 — 번호형 본문 전체</summary>

- [개요](#js-19-section-1)
- [핵심 개념](#js-19-section-2)
- [학습 목표](#js-19-section-3)
- [개념에서 실제 실행까지: 객체는 JavaScript 값이고 JSON은 데이터를 표현하는 문자열 형식이다](#js-19-section-4)
- [1. 원본에서 말하는 JSON](#js-19-section-5)
- [2. 객체와 JSON 차이](#js-19-section-6)
- [3. JSON에서 사용할 수 없는 문법](#js-19-section-7)
- [4. JSON의 사용 목적](#js-19-section-8)
- [5. 객체 선언](#js-19-section-9)
- [6. Key와 Value](#js-19-section-10)
- [7. 객체 Value의 범위](#js-19-section-11)
- [8. Property 순서](#js-19-section-12)
- [9. Bracket Notation](#js-19-section-13)
- [10. Dot Notation](#js-19-section-14)
- [11. 동적 Key](#js-19-section-15)
- [12. Hyphen Key](#js-19-section-16)
- [13. 잘못된 Hyphen 접근](#js-19-section-17)
- [14. 중첩 객체](#js-19-section-18)
- [15. Optional Chaining](#js-19-section-19)
- [16. 내 코드와 강사님 코드의 `k`](#js-19-section-20)
- [17. 내 코드의 누락 Property](#js-19-section-21)
- [18. 존재하지 않는 Property](#js-19-section-22)
- [19. 선언되지 않은 변수](#js-19-section-23)
- [20. 함수 Property](#js-19-section-24)
- [21. 객체를 문자열과 결합](#js-19-section-25)
- [22. Property 수정](#js-19-section-26)
- [23. Property 추가](#js-19-section-27)
- [24. Computed Property 추가](#js-19-section-28)
- [25. Property 삭제](#js-19-section-29)
- [26. Immutable 제거](#js-19-section-30)
- [27. Property 존재 확인](#js-19-section-31)
- [28. 직렬화](#js-19-section-32)
- [29. 직렬화 결과 자료형](#js-19-section-33)
- [30. 보기 좋은 JSON 문자열](#js-19-section-34)
- [31. 함수 Property 제외](#js-19-section-35)
- [32. `undefined`와 Symbol](#js-19-section-36)
- [33. 배열 안의 변환](#js-19-section-37)
- [34. `NaN`과 Infinity](#js-19-section-38)
- [35. BigInt 오류](#js-19-section-39)
- [36. Date 직렬화](#js-19-section-40)
- [37. 순환 참조 오류](#js-19-section-41)
- [38. `toJSON()`](#js-19-section-42)
- [39. Replacer 배열](#js-19-section-43)
- [40. Replacer 함수](#js-19-section-44)
- [41. 네트워크는 무조건 문자열인가?](#js-19-section-45)
- [42. 역직렬화](#js-19-section-46)
- [43. Parse 결과 자료형](#js-19-section-47)
- [44. 함수는 복원되지 않음](#js-19-section-48)
- [45. 잘못된 JSON Parse](#js-19-section-49)
- [46. JSON 문자열 값 Parse](#js-19-section-50)
- [47. 빈 객체 Parse](#js-19-section-51)
- [48. 객체 배열 Parse](#js-19-section-52)
- [49. Parse 오류 처리](#js-19-section-53)
- [50. Parse 결과 사용](#js-19-section-54)
- [51. Reviver](#js-19-section-55)
- [52. JSON 문법 규칙](#js-19-section-56)
- [53. Trailing Comma 금지](#js-19-section-57)
- [54. Leading Zero 금지](#js-19-section-58)
- [55. 객체 배열](#js-19-section-59)
- [56. `for...of`](#js-19-section-60)
- [57. `for...in`](#js-19-section-61)
- [58. 배열 Method 순회](#js-19-section-62)
- [59. `map()`](#js-19-section-63)
- [60. `Object.keys()`](#js-19-section-64)
- [61. `Object.values()`](#js-19-section-65)
- [62. `Object.entries()`](#js-19-section-66)
- [63. 객체 복사](#js-19-section-67)
- [64. JSON 기반 깊은 복사의 한계](#js-19-section-68)
- [65. `structuredClone()`](#js-19-section-69)
- [66. Local Storage 저장](#js-19-section-70)
- [67. Local Storage 복원](#js-19-section-71)
- [68. 저장 데이터 오류 처리](#js-19-section-72)
- [69. API 전송 전 직렬화](#js-19-section-73)
- [70. API 응답 Parse](#js-19-section-74)
- [71. 내 코드와 강사님 코드 비교](#js-19-section-75)
- [72. 기존 코드에서 개선한 이유](#js-19-section-76)
- [73. 실무형 예제: 설정 저장소](#js-19-section-77)
- [74. 대표 오류로 이해하기](#js-19-section-78)
- [75. 자주 하는 실수](#js-19-section-79)
- [76. 핵심 요약](#js-19-section-80)
- [77. 최종 체크리스트](#js-19-section-81)
- [마무리](#js-19-section-82)
- [V3 실행 추적 카드 — JS 값 ↔ JSON 문자열](#js-19-section-83)

</details>

---

<a id="js-19-section-1"></a>

## 개요

JavaScript 객체는 Key와 Value로 데이터를 관리한다.

```javascript
const user = {
    name: "Kim",
    age: 20,
}
```

JSON은 객체 자체가 아니라 구조화된 데이터를 표현하는 문자열 형식이다.

```json
{
    "name": "Kim",
    "age": 20
}
```

객체와 JSON 문자열 사이의 변환:

```text
JavaScript 값
    ↓ JSON.stringify()
JSON 문자열
    ↓ JSON.parse()
JavaScript 값
```

> [!IMPORTANT]
> 변수 이름이 `json`이라고 해서 그 값이 자동으로 JSON이 되는 것은 아니다.  
> 함수·따옴표 없는 Key·Single Quote 등을 포함한 값은 JavaScript 객체 Literal이지 JSON 문자열이 아니다.

---

<a id="js-19-section-2"></a>

## 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| Object | Key와 Value를 저장하는 JavaScript 자료형 |
| Property | 객체 안의 Key·Value 한 쌍 |
| Dot Notation | `object.key` 형식의 접근 |
| Bracket Notation | `object["key"]` 형식의 접근 |
| JSON | 구조화된 데이터를 표현하는 문자열 형식 |
| 직렬화 | JavaScript 값을 저장·전송 가능한 문자열로 변환 |
| 역직렬화 | JSON 문자열을 JavaScript 값으로 변환 |
| `JSON.stringify()` | JavaScript 값을 JSON 문자열로 변환 |
| `JSON.parse()` | JSON 문자열을 JavaScript 값으로 변환 |
| Replacer | Stringify 대상 Property를 선택·변환 |
| Reviver | Parse 중 Value를 복원·변환 |
| `Object.keys()` | Own Enumerable String Key 배열 반환 |

---

<a id="js-19-section-3"></a>

## 학습 목표

- 직렬화 때 남는 값과 사라지는 값을 확인한다.
- 원본의 해당 부분을 찾아 실행 순서와 결과를 다시 확인한다.

---

<a id="js-19-section-4"></a>

## 개념에서 실제 실행까지: 객체는 JavaScript 값이고 JSON은 데이터를 표현하는 문자열 형식이다

수업에서 json이라는 변수에 함수를 포함한 객체를 넣었지만 이것은 JSON 문자열 자체가 아니다. JavaScript 객체는 함수·undefined 등도 담을 수 있고 JSON 문법은 그 값을 직접 표현하지 않는다. JSON.stringify로 문자열을 만들고 JSON.parse로 다시 값을 읽는다.

내 원본의 k1에는 k가 없어 json.k1.k가 undefined, 강사님은 k:3이 있어3이다. 같은 접근 문법인데 입력 객체가 다른 사례다. 하이픈 키는 ["k1-2"]로 접근한다. json.k1.k1-2는 키 이름 하나가 아니라 프로퍼티 조회 뒤 숫자2를 빼는 표현식이다.

stringify는 객체 속성의 함수·undefined를 생략하고, 배열 요소의 undefined는 null로 표현한다. Date는 보통 ISO 문자열이 되며 parse가 Date 객체를 자동 복원하지 않는다. NaN/Infinity는 null, BigInt와 순환참조는 기본 직렬화에서 오류가 날 수 있다. stringify/parse를 만능 깊은 복사로 설명하면 안 된다.

### 수업 원본에서 사용한 부분

아래는 전체 실행 파일이 아니라 **개념에 대응하는 문맥 발췌**다. 나머지 HTML·선언·등록 코드는 원본과 기존 번호형 본문에서 이어 확인한다. 

내 코드: `workspace_html/javascript/19_json.html`

```javascript
// 단, 값이 함수인 것은 제외함
            const str = JSON.stringify(json)
            console.log(str)

            // parse(분석)을 이용해서 문자열로 바꾼 값을 다시 json으로 바꿀 수 있음
            const json2 = JSON.parse(str)
            console.log(json2)
```

강사님 코드: `workspace_teacher/workspace_html/javascript/19_json.html`

```javascript
// 단, 값이 함수인 것은 제외
        const str = JSON.stringify(json)
        console.log(str)

        // 글씨를 json으로 
        const json2 = JSON.parse(str)
        console.log(json2)
```

### 직접 재현하는 최소 예제와 결과

이 예제는 **이번 리팩토링의 설명용 재구성**이다. 원본 그대로의 발췌와 구별한다. 외부 통신 없이 Console에서 실행한다. 다른 예제의 변수와 섞이지 않게 새 실행 문맥에서 실행한다.

```javascript
const source = {num: 456, fn() {}, empty: undefined, rows: [undefined, NaN]};
const text = JSON.stringify(source);
const restored = JSON.parse(text);
console.log(text);
console.log(typeof text, typeof restored, "fn" in restored);
console.log(String(source));
```

예상 출력:

```text
{"num":456,"rows":[null,null]}
string object false
[object Object]
```

### 결과를 역추적하는 방법

네트워크는 결국 바이트를 전송하며 텍스트·파일·바이너리도 가능하다. 여기서는 application/json 계약에 맞춰 문자열을 인코딩하는 경우를 배운다. Object.keys의 순서는 정해진 규칙이 있지만 업무 순서를 표현할 때 배열로 명시한다.

출력은 아래의 확인 경로로 추적한다. return 값은 호출자에게 전달되고 자동으로 화면에 표시되지 않는다. Console 로그, DOM 변경, 저장소 변경, 서버 응답은 별개 단계다.

| 확인할 단계 | 이 예제에서 볼 것 |
| --- | --- |
| 입력 | 리터럴·현재 폼 값·이벤트 인수·응답 중 출처를 위 설명과 대조 |
| 실행 | 각 줄 또는 콜백이 지금 실행되는지, 나중에 실행되는지 구분 |
| 결과 | 위 예상 출력과 현재 값·자료형을 함께 대조 |
| 오류 | 첫 오류 줄의 입력과 직전 상태를 확인하고 뒤 로그 누락 원인 추적 |

### 단계별 복습 실습과 정답

**기본 실습:** {a:undefined,b:1}과[undefined,1]을 직렬화한다.

**응용·디버깅 실습:** 내 json.k1.k와 강사님 같은 접근이 다른 이유를 설명한다.

**통합 확인:** 위 최소 예제를 새 문맥에서 작성하고 정상값·빈 값·경계값으로 실행한다. 원본에서 대응하는 선언·호출·콜백을 찾아 위에 나타난 차이가 무엇을 바꾸는지 설명한다. 아래 정답은 먼저 예측한 뒤 펼친다. 이 실습은 💡 설명용 보강이며 원본에 모두 완성되어 있다는 뜻은 아니다.

<details>
<summary>정답과 처리 순서 해설</summary>

1. 객체는{"b":1}, 배열은[null,1]이다.
2. 내k1에는k프로퍼티가없어undefined,강사님은k:3이있어3이다. 접근문법이아니라입력데이터차이다.
3. 최소 예제의 예상 출력과 한 줄씩 대조한다. 값이 다른 경우 입력 → 형 변환 → 분기/상태 변경 → 출력 순서로 첫 차이를 찾는다. DOM·API 예제는 Console 값만 아니라 화면·Elements·Network가 서로 같은 상태를 말하는지도 점검한다.

</details>

### 복습 질문과 해설

**질문:** JSON.parse("{name:'Kim'}")이 실패하는 이유는?

**해설:** JSON 키와 문자열은 큰따옴표가 필요하다. JavaScript 객체 리터럴 문법을 JSON 문자열 문법과 혼동한 것이다.

**한 번 더 확인:** 예제의 입력을 하나 바꾸고 결과를 먼저 예상한 뒤 실행한다. 정상 입력만 아니라 비어 있는 값, 경계값, 두 번 실행했을 때의 상태를 기존 실습·오류 절에서 반복 확인한다.

---

<a id="js-19-section-5"></a>

## 1. 원본에서 말하는 JSON

원본:

```javascript
let json = {}

json = {
    "key": "value",
    "num": 1234,

    "fn": function () {
        console.log(1)
    },

    "k1": {
        "k1-1": 1,
        "k1-2": 2,
    },

    k2: "k3",
}
```

이 값은 JSON 문자열이 아니라 JavaScript 객체다.

---

<a id="js-19-section-6"></a>

## 2. 객체와 JSON 차이

JavaScript 객체:

```javascript
const user = {
    name: "Kim",

    greet() {
        console.log("hello")
    },
}
```

JSON 문자열:

```json
{
    "name": "Kim"
}
```

---

<a id="js-19-section-7"></a>

## 3. JSON에서 사용할 수 없는 문법

```text
함수
undefined
Symbol
따옴표 없는 Property Name
Single Quote 문자열
주석
Trailing Comma
```

JSON의 Property Name과 문자열은 Double Quote를 사용한다.

---

<a id="js-19-section-8"></a>

## 4. JSON의 사용 목적

원본의 “닫는 태그를 줄이기 위해 JSON 사용”이라는 설명은 정확하지 않다.

대표 사용처:

- API 요청·응답
- 설정 파일
- Local Storage
- Server·Client 데이터 교환
- 다른 프로그래밍 언어와 데이터 공유
- 로그·캐시 데이터 저장

---

<a id="js-19-section-9"></a>

## 5. 객체 선언

```javascript
const data = {
    key: "value",
}
```

재할당이 필요하지 않다면 `const`를 사용한다.

`const` 객체의 Property는 변경할 수 있다.

```javascript
data.key = "changed"
```

---

<a id="js-19-section-10"></a>

## 6. Key와 Value

```javascript
const product = {
    name: "Keyboard",
    price: 50000,
}
```

```text
name
→ Key

"Keyboard"
→ Value
```

---

<a id="js-19-section-11"></a>

## 7. 객체 Value의 범위

JavaScript 객체에는 대부분의 JavaScript 값을 저장할 수 있다.

```javascript
const object = {
    number: 1,
    string: "text",
    boolean: true,
    nothing: null,
    missing: undefined,
    array: [1, 2],
    nested: {},
    fn() {},
}
```

JSON에서 표현 가능한 Value:

```text
String
Number
Boolean
Null
Object
Array
```

---

<a id="js-19-section-12"></a>

## 8. Property 순서

객체를 배열처럼 순서 중심 자료구조로 사용하면 안 된다.

현대 JavaScript에는 Key 열거 순서 규칙이 있지만, 의미 있는 순서가 중요하면 배열을 사용한다.

---

<a id="js-19-section-13"></a>

## 9. Bracket Notation

```javascript
console.log(
    data["key"],
)
```

문자열 형태의 Key를 전달한다.

---

<a id="js-19-section-14"></a>

## 10. Dot Notation

```javascript
console.log(
    data.key,
)
```

Identifier 문법에 맞는 Key는 Dot Notation으로 접근할 수 있다.

---

<a id="js-19-section-15"></a>

## 11. 동적 Key

```javascript
const keyName = "price"

console.log(
    product[keyName],
)
```

변수에 저장된 Key를 사용할 때는 Bracket Notation이 필요하다.

---

<a id="js-19-section-16"></a>

## 12. Hyphen Key

```javascript
const data = {
    "user-name": "Kim",
}
```

올바른 접근:

```javascript
console.log(
    data["user-name"],
)
```

---

<a id="js-19-section-17"></a>

## 13. 잘못된 Hyphen 접근

```text
data.user-name
```

JavaScript는 다음처럼 해석한다.

```text
data.user - name
```

Property 접근이 아니라 뺄셈 표현식이다.

---

<a id="js-19-section-18"></a>

## 14. 중첩 객체

```javascript
const data = {
    profile: {
        name: "Kim",
        address: {
            city: "Seoul",
        },
    },
}
```

접근:

```javascript
console.log(
    data.profile.address.city,
)
```

---

<a id="js-19-section-19"></a>

## 15. Optional Chaining

```javascript
console.log(
    data.profile?.address?.city,
)
```

중간 값이 `null` 또는 `undefined`이면 오류 대신 `undefined`를 반환한다.

---

<a id="js-19-section-20"></a>

## 16. 내 코드와 강사님 코드의 `k`

강사님 코드:

```text
k1: {
    "k1-1": 1,
    "k1-2": 2,
    k: 3,
}
```

```javascript
console.log(
    json.k1.k,
)
```

출력:

```text
3
```

---

<a id="js-19-section-21"></a>

## 17. 내 코드의 누락 Property

내 코드에는 `k`가 없다.

```text
k1: {
    "k1-1": 1,
    "k1-2": 2,
}
```

따라서:

```javascript
console.log(
    json.k1.k,
)
```

출력:

```text
undefined
```

---

<a id="js-19-section-22"></a>

## 18. 존재하지 않는 Property

```javascript
console.log(
    product.stock,
)
```

출력:

```text
undefined
```

객체는 존재하지만 해당 Key가 없는 상태다.

---

<a id="js-19-section-23"></a>

## 19. 선언되지 않은 변수

```text
console.log(stock)
```

변수 자체가 선언되지 않았다면 `ReferenceError`가 발생할 수 있다.

```text
object.missing
→ undefined

missing
→ ReferenceError 가능
```

---

<a id="js-19-section-24"></a>

## 20. 함수 Property

```javascript
const calculator = {
    add(
        a,
        b,
    ) {
        return a + b
    },
}
```

호출:

```javascript
console.log(
    calculator.add(
        2,
        3,
    ),
)
```

출력:

```text
5
```

---

<a id="js-19-section-25"></a>

## 21. 객체를 문자열과 결합

```javascript
console.log(
    "" + product,
)
```

대표 결과:

```text
[object Object]
```

객체 내부를 확인할 때는 객체 자체를 출력한다.

```javascript
console.log(product)
```

---

<a id="js-19-section-26"></a>

## 22. Property 수정

```javascript
product.price = 60000
```

기존 Key가 있으므로 Value가 변경된다.

---

<a id="js-19-section-27"></a>

## 23. Property 추가

```javascript
product.stock = 10
```

기존 Key가 없으므로 새 Property가 추가된다.

---

<a id="js-19-section-28"></a>

## 24. Computed Property 추가

```javascript
const key = "category"

product[key] = "device"
```

동적으로 Key를 정할 수 있다.

---

<a id="js-19-section-29"></a>

## 25. Property 삭제

```javascript
delete product.stock
```

객체에서 해당 Property를 제거한다.

---

<a id="js-19-section-30"></a>

## 26. Immutable 제거

```javascript
const {
    stock,
    ...restProduct
} = product
```

`restProduct`에는 `stock`을 제외한 Property가 저장된다.

상태 관리 방식에 따라 `delete` 또는 새 객체 생성을 선택한다.

---

<a id="js-19-section-31"></a>

## 27. Property 존재 확인

```javascript
console.log(
    "price" in product,
)
```

Prototype Chain까지 검사한다.

Own Property만 확인:

```javascript
console.log(
    Object.hasOwn(
        product,
        "price",
    ),
)
```

---

<a id="js-19-section-32"></a>

## 28. 직렬화

```javascript
const jsonText = (
    JSON.stringify(
        product,
    )
)
```

JavaScript 값을 JSON 문자열로 변환한다.

---

<a id="js-19-section-33"></a>

## 29. 직렬화 결과 자료형

```javascript
console.log(
    typeof jsonText,
)
```

출력:

```text
string
```

---

<a id="js-19-section-34"></a>

## 30. 보기 좋은 JSON 문자열

```javascript
const jsonText = (
    JSON.stringify(
        product,
        null,
        2,
    )
)
```

세 번째 인수는 들여쓰기 크기다.

---

<a id="js-19-section-35"></a>

## 31. 함수 Property 제외

```javascript
const data = {
    name: "Kim",

    greet() {
        console.log("hello")
    },
}

console.log(
    JSON.stringify(data),
)
```

결과:

```json
{"name":"Kim"}
```

객체 Property의 함수는 제외된다.

---

<a id="js-19-section-36"></a>

## 32. `undefined`와 Symbol

객체 Property에서는 일반적으로 제외된다.

```javascript
const data = {
    missing: undefined,
    symbol: Symbol("id"),
}
```

---

<a id="js-19-section-37"></a>

## 33. 배열 안의 변환

```javascript
const values = [
    undefined,
    function () {},
    Symbol("id"),
]

console.log(
    JSON.stringify(values),
)
```

결과:

```json
[null,null,null]
```

---

<a id="js-19-section-38"></a>

## 34. `NaN`과 Infinity

```javascript
console.log(
    JSON.stringify({
        first: NaN,
        second: Infinity,
    }),
)
```

결과:

```json
{"first":null,"second":null}
```

---

<a id="js-19-section-39"></a>

## 35. BigInt 오류

```text
JSON.stringify({
    value: 10n
})
```

기본적으로 `TypeError`가 발생한다.

문자열로 명시적으로 변환할 수 있다.

```javascript
const data = {
    value: String(10n),
}
```

---

<a id="js-19-section-40"></a>

## 36. Date 직렬화

```javascript
const data = {
    createdAt: new Date(
        "2026-08-06T06:00:00Z",
    ),
}

console.log(
    JSON.stringify(data),
)
```

Date는 일반적으로 ISO 문자열로 변환된다.

---

<a id="js-19-section-41"></a>

## 37. 순환 참조 오류

```javascript
const data = {}

data.self = data
```

```text
JSON.stringify(data)
→ TypeError
```

서로 다시 참조하는 구조는 기본 JSON으로 직렬화할 수 없다.

---

<a id="js-19-section-42"></a>

## 38. `toJSON()`

```javascript
const user = {
    name: "Kim",
    password: "secret",

    toJSON() {
        return {
            name: this.name,
        }
    },
}
```

```javascript
console.log(
    JSON.stringify(user),
)
```

민감한 Property를 제외한 결과를 반환하도록 정의할 수 있다.

---

<a id="js-19-section-43"></a>

## 39. Replacer 배열

```javascript
const jsonText = (
    JSON.stringify(
        product,
        [
            "name",
            "price",
        ],
    )
)
```

지정한 Property만 포함한다.

---

<a id="js-19-section-44"></a>

## 40. Replacer 함수

```javascript
const jsonText = (
    JSON.stringify(
        product,
        (
            key,
            value,
        ) => {
            if (
                key === "password"
            ) {
                return undefined
            }

            return value
        },
    )
)
```

민감한 값을 제외하거나 변환할 수 있다.

---

<a id="js-19-section-45"></a>

## 41. 네트워크는 무조건 문자열인가?

원본의 “네트워크 통신은 무조건 문자로 전송한다”는 설명은 지나치게 단순하다.

네트워크는 Byte를 전송하며 다양한 형식을 사용할 수 있다.

- JSON Text
- Form Data
- Image Binary
- Blob
- ArrayBuffer
- Protocol Buffers

---

<a id="js-19-section-46"></a>

## 42. 역직렬화

```javascript
const parsed = (
    JSON.parse(
        jsonText,
    )
)
```

JSON 문자열을 JavaScript 값으로 변환한다.

---

<a id="js-19-section-47"></a>

## 43. Parse 결과 자료형

```javascript
console.log(
    typeof parsed,
)
```

객체 JSON을 Parse했다면:

```text
object
```

---

<a id="js-19-section-48"></a>

## 44. 함수는 복원되지 않음

Stringify 과정에서 함수가 제외되었으므로 Parse 후에도 함수가 생기지 않는다.

```javascript
console.log(
    parsed.greet,
)
```

출력:

```text
undefined
```

---

<a id="js-19-section-49"></a>

## 45. 잘못된 JSON Parse

```text
JSON.parse("<h1>")
```

유효한 JSON이 아니므로 `SyntaxError`가 발생한다.

---

<a id="js-19-section-50"></a>

## 46. JSON 문자열 값 Parse

```javascript
const value = JSON.parse(
    '"<h1>"',
)

console.log(value)
```

출력:

```text
<h1>
```

외부 Double Quote가 JSON String Literal을 만든다.

---

<a id="js-19-section-51"></a>

## 47. 빈 객체 Parse

```javascript
const value = JSON.parse(
    "{}",
)

console.log(value)
```

출력:

```text
{}
```

---

<a id="js-19-section-52"></a>

## 48. 객체 배열 Parse

```javascript
const value = JSON.parse(
    "[{}]",
)

console.log(value)
```

빈 객체 하나를 가진 배열이 만들어진다.

---

<a id="js-19-section-53"></a>

## 49. Parse 오류 처리

```javascript
function safeParse(
    jsonText,
) {
    try {
        return {
            ok: true,
            value: JSON.parse(
                jsonText,
            ),
        }
    } catch (
        error
    ) {
        return {
            ok: false,
            error,
        }
    }
}
```

---

<a id="js-19-section-54"></a>

## 50. Parse 결과 사용

```javascript
const result = safeParse(
    '{"name":"Kim"}',
)

if (result.ok) {
    console.log(
        result.value.name,
    )
} else {
    console.error(
        "JSON 형식 오류",
    )
}
```

---

<a id="js-19-section-55"></a>

## 51. Reviver

```javascript
const parsed = JSON.parse(
    '{"createdAt":"2026-08-06T06:00:00.000Z"}',
    (
        key,
        value,
    ) => {
        if (
            key === "createdAt"
        ) {
            return new Date(
                value,
            )
        }

        return value
    },
)
```

---

<a id="js-19-section-56"></a>

## 52. JSON 문법 규칙

올바른 JSON:

```json
{
    "name": "Kim",
    "age": 20,
    "active": true,
    "address": null,
    "skills": [
        "HTML",
        "CSS"
    ]
}
```

---

<a id="js-19-section-57"></a>

## 53. Trailing Comma 금지

잘못된 JSON:

```text
{
    "name": "Kim",
}
```

JavaScript 객체 Literal에서는 허용될 수 있지만 JSON에서는 허용되지 않는다.

---

<a id="js-19-section-58"></a>

## 54. Leading Zero 금지

잘못된 JSON 숫자:

```text
03
```

날짜의 월·일처럼 앞자리 0을 유지해야 한다면 문자열로 저장한다.

```json
{
    "month": "03",
    "day": "02"
}
```

---

<a id="js-19-section-59"></a>

## 55. 객체 배열

```javascript
const temples = [
    {
        name: "그랜절",
        address: "광장",
        price: 300000,
    },
    {
        name: "만우절",
        address: "없음",
        price: 2147483647,
    },
]
```

객체 두 개를 가진 JavaScript 배열이다.

---

<a id="js-19-section-60"></a>

## 56. `for...of`

```javascript
for (
    const temple
    of temples
) {
    console.log(
        temple.name,
    )
}
```

배열의 Value를 순회한다.

---

<a id="js-19-section-61"></a>

## 57. `for...in`

```javascript
for (
    const index
    in temples
) {
    console.log(
        temples[index].price,
    )
}
```

배열의 Enumerable Key를 순회한다.

배열 Value 순회에는 일반적으로 `for...of`가 더 적합하다.

---

<a id="js-19-section-62"></a>

## 58. 배열 Method 순회

```javascript
temples.forEach(
    temple => {
        console.log(
            temple.name,
        )
    },
)
```

---

<a id="js-19-section-63"></a>

## 59. `map()`

```javascript
const names = temples.map(
    temple => (
        temple.name
    ),
)

console.log(names)
```

새 배열을 만든다.

---

<a id="js-19-section-64"></a>

## 60. `Object.keys()`

```javascript
const keys = Object.keys(
    product,
)

console.log(keys)
```

Own Enumerable String Key를 배열로 반환한다.

---

<a id="js-19-section-65"></a>

## 61. `Object.values()`

```javascript
const values = Object.values(
    product,
)
```

Value 배열을 반환한다.

---

<a id="js-19-section-66"></a>

## 62. `Object.entries()`

```javascript
const entries = Object.entries(
    product,
)

for (
    const [
        key,
        value,
    ]
    of entries
) {
    console.log(
        key,
        value,
    )
}
```

---

<a id="js-19-section-67"></a>

## 63. 객체 복사

```javascript
const copied = {
    ...product,
}
```

얕은 복사다.

중첩 객체는 같은 참조를 공유할 수 있다.

---

<a id="js-19-section-68"></a>

## 64. JSON 기반 깊은 복사의 한계

```javascript
const copied = JSON.parse(
    JSON.stringify(
        original,
    ),
)
```

다음 값이 손실·변형될 수 있다.

- Function
- `undefined`
- Symbol
- Date
- Map
- Set
- BigInt
- 순환 참조
- Class Instance

일반 데이터 복사는 `structuredClone()`을 검토한다.

---

<a id="js-19-section-69"></a>

## 65. `structuredClone()`

```javascript
const copied = (
    structuredClone(
        original,
    )
)
```

지원 가능한 다양한 내장 자료형과 순환 참조를 복제할 수 있다.

함수는 복제할 수 없다.

---

<a id="js-19-section-70"></a>

## 66. Local Storage 저장

Local Storage에는 문자열만 저장된다.

```javascript
const settings = {
    theme: "dark",
    fontSize: 16,
}

localStorage.setItem(
    "settings",
    JSON.stringify(
        settings,
    ),
)
```

---

<a id="js-19-section-71"></a>

## 67. Local Storage 복원

```javascript
const stored = localStorage.getItem(
    "settings",
)

const settings = (
    stored === null
        ? null
        : JSON.parse(stored)
)
```

---

<a id="js-19-section-72"></a>

## 68. 저장 데이터 오류 처리

```javascript
function loadJson(
    key,
    fallback,
) {
    const stored = (
        localStorage.getItem(
            key,
        )
    )

    if (stored === null) {
        return fallback
    }

    try {
        return JSON.parse(
            stored,
        )
    } catch (
        error
    ) {
        console.error(
            `${key} 복원 실패`,
            error,
        )

        return fallback
    }
}
```

---

<a id="js-19-section-73"></a>

## 69. API 전송 전 직렬화

```javascript
const requestBody = (
    JSON.stringify({
        name: "Kim",
        age: 20,
    })
)
```

Fetch에서 사용할 때:

```javascript
fetch(
    "/api/users",
    {
        method: "POST",

        headers: {
            "Content-Type":
                "application/json",
        },

        body: requestBody,
    },
)
```

---

<a id="js-19-section-74"></a>

## 70. API 응답 Parse

```javascript
const response = await fetch(
    "/api/users",
)

const data = await response.json()
```

`response.json()`은 응답 Body를 읽고 JSON Parse까지 수행한다.

---

<a id="js-19-section-75"></a>

## 71. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 객체 기본 구조 | 거의 동일 | 거의 동일 |
| 중첩 `k` Property | 없음 | `k: 3` 존재 |
| `json.k1.k` 결과 | `undefined` | `3` |
| `num2` 추가 후 출력 | 직접 출력 | 객체 전체 출력 |
| Parse 결과 출력 | 일부 직접 출력 | 일부 대입만 수행 |
| 객체 배열 | 동일 | 동일 |
| 설명 주석 | 더 상세 | 핵심 중심 |
| 객체와 JSON 용어 | 혼용 | 혼용 |

### 71-1. 내 코드의 장점

- 객체의 Key·Value 구조를 상세히 주석으로 기록했다.
- Bracket·Dot Notation 차이를 실습했다.
- 함수 Property 호출을 확인했다.
- Stringify·Parse 결과를 직접 출력했다.
- 객체 배열과 반복문을 직접 확인했다.

### 71-2. 내 코드의 개선점

- JavaScript 객체를 JSON이라고 부른다.
- JSON을 HTML 닫는 Tag 감소 목적으로 설명한다.
- `k` Property가 없는데 `json.k1.k`를 출력한다.
- 네트워크 데이터가 항상 문자열이라고 단정한다.
- 실무에서 `delete`를 사용하지 않는다고 단정한다.
- `for...in`을 배열 Value 순회처럼 사용할 수 있다.
- Parse 오류 처리와 저장 데이터 검증이 없다.

### 71-3. 강사님 코드의 장점

- 객체 선언·접근·수정·추가·삭제 흐름이 간결하다.
- 중첩 객체의 Dot·Bracket 접근을 보여 준다.
- Stringify·Parse 기본 사용을 확인할 수 있다.
- 객체 배열 순회와 `Object.keys()`를 연결한다.

### 71-4. 강사님 코드의 보충점

- 객체와 JSON 문자열의 용어를 구분해야 한다.
- Stringify에서 제외·변환되는 값 설명이 필요하다.
- Parse 오류 처리와 Reviver를 보충할 수 있다.
- `for...in` 배열 순회의 한계를 설명해야 한다.
- Local Storage·API 연결 예제가 필요하다.

---

<a id="js-19-section-76"></a>

## 72. 기존 코드에서 개선한 이유

### 72-1. 변수 이름

기존:

```javascript
const json = {
    key: "value",
}
```

개선:

```javascript
const data = {
    key: "value",
}
```

객체와 JSON 문자열을 이름으로 구분한다.

### 72-2. 직렬화 변수

```javascript
const jsonText = (
    JSON.stringify(
        data,
    )
)
```

문자열임이 드러나는 이름을 사용한다.

### 72-3. 배열 순회

기존:

```javascript
for (
    const index
    in temples
) {
    console.log(
        temples[index],
    )
}
```

개선:

```javascript
for (
    const temple
    of temples
) {
    console.log(temple)
}
```

### 72-4. Parse 오류 처리

기존:

```javascript
const data = JSON.parse(
    input,
)
```

개선:

```javascript
const result = safeParse(
    input,
)
```

---

<a id="js-19-section-77"></a>

## 73. 실무형 예제: 설정 저장소

```javascript
function createJsonStorage(
    storage,
) {
    return {
        save(
            key,
            value,
        ) {
            const jsonText = (
                JSON.stringify(
                    value,
                )
            )

            storage.setItem(
                key,
                jsonText,
            )
        },

        load(
            key,
            fallback = null,
        ) {
            const jsonText = (
                storage.getItem(
                    key,
                )
            )

            if (
                jsonText === null
            ) {
                return fallback
            }

            try {
                return JSON.parse(
                    jsonText,
                )
            } catch (
                error
            ) {
                console.error(
                    `${key} Parse 실패`,
                    error,
                )

                return fallback
            }
        },

        remove(
            key,
        ) {
            storage.removeItem(
                key,
            )
        },
    }
}

const settingsStorage = (
    createJsonStorage(
        localStorage,
    )
)

settingsStorage.save(
    "app-settings",
    {
        theme: "dark",
        fontSize: 16,
    },
)

const settings = (
    settingsStorage.load(
        "app-settings",
        {
            theme: "light",
            fontSize: 14,
        },
    )
)

console.log(settings)
```

### 73-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `JSON.stringify()` | 객체를 저장 가능한 문자열로 변환 |
| `JSON.parse()` | 문자열을 객체로 복원 |
| `try...catch` | 손상된 저장 데이터 처리 |
| Fallback | 데이터 없음·오류 시 기본값 제공 |
| Storage 주입 | Local·Session Storage 재사용 |
| Method 분리 | 저장·조회·삭제 역할 구분 |

---

<a id="js-19-section-78"></a>

## 74. 대표 오류로 이해하기

### 74-1. 객체를 JSON이라고 부름

자료형과 문자열 형식을 혼동하게 된다.

### 74-2. Hyphen Key에 Dot Notation 사용

뺄셈 표현식으로 해석된다.

### 74-3. 없는 Property와 없는 변수 혼동

`undefined`와 `ReferenceError`가 다르다.

### 74-4. 함수가 Parse 후 복원된다고 생각

Stringify 단계에서 제외된다.

### 74-5. 잘못된 JSON Parse

`SyntaxError`가 발생한다.

### 74-6. BigInt·순환 참조 Stringify

`TypeError`가 발생할 수 있다.

---

<a id="js-19-section-79"></a>

## 75. 자주 하는 실수

### 75-1. Single Quote JSON 작성

JSON 문자열은 Double Quote를 사용한다.

### 75-2. Trailing Comma 사용

JavaScript 객체와 달리 JSON에서는 허용되지 않는다.

### 75-3. `undefined`를 JSON Value로 기대

객체에서는 제외되거나 배열에서는 `null`로 변환된다.

### 75-4. Date가 Date 객체로 복원된다고 생각

기본 Parse 결과는 문자열이다.

### 75-5. JSON 복사로 모든 자료형 깊은 복사

여러 자료형이 손실되거나 변형된다.

### 75-6. 배열에 `for...in`을 우선 사용

Value 순회에는 `for...of`가 더 적합하다.

### 75-7. Local Storage 값을 바로 Parse

잘못된 데이터에 대비해 `try...catch`를 사용한다.

### 75-8. 민감정보를 그대로 Stringify

Replacer·`toJSON()` 또는 별도 DTO로 제외한다.

### 75-9. 객체 Property 순서를 업무 로직에 의존

순서가 중요하면 배열을 사용한다.

### 75-10. API 응답 구조를 검증하지 않음

JSON Parse 성공과 데이터 형태가 올바른 것은 별개다.

---

<a id="js-19-section-80"></a>

## 76. 핵심 요약

```text
JavaScript Object
→ 실행 중 사용하는 값

JSON
→ 구조화된 문자열 형식
```

```text
object.key
object["key"]
→ Property 접근
```

```text
JSON.stringify()
→ 직렬화

JSON.parse()
→ 역직렬화
```

```text
Object.keys()
Object.values()
Object.entries()
→ 객체 순회용 배열
```

```text
for...of
→ 배열 Value

for...in
→ Enumerable Key
```

---

<a id="js-19-section-81"></a>

## 77. 최종 체크리스트

- [ ] JavaScript 객체와 JSON 문자열을 구분할 수 있는가?
- [ ] JSON에서 허용되지 않는 문법을 설명할 수 있는가?
- [ ] Dot·Bracket Notation을 구분할 수 있는가?
- [ ] 동적 Key에 Bracket Notation을 사용할 수 있는가?
- [ ] Hyphen Key에 안전하게 접근할 수 있는가?
- [ ] 중첩 객체에 Optional Chaining을 사용할 수 있는가?
- [ ] 내 코드의 누락된 `k` Property 차이를 이해했는가?
- [ ] 존재하지 않는 Property와 변수를 구분할 수 있는가?
- [ ] Property를 추가·수정·삭제할 수 있는가?
- [ ] `Object.hasOwn()`으로 Own Property를 확인할 수 있는가?
- [ ] `JSON.stringify()` 결과가 문자열임을 이해했는가?
- [ ] 함수·`undefined`·Symbol의 직렬화 규칙을 이해했는가?
- [ ] `NaN`, Infinity, BigInt의 동작을 이해했는가?
- [ ] 순환 참조 오류를 설명할 수 있는가?
- [ ] Replacer로 Property를 제외할 수 있는가?
- [ ] `JSON.parse()` 오류를 처리할 수 있는가?
- [ ] Reviver로 Date를 복원할 수 있는가?
- [ ] `for...of`와 `for...in`을 구분할 수 있는가?
- [ ] `Object.keys()`, `values()`, `entries()`를 사용할 수 있는가?
- [ ] JSON 깊은 복사의 한계를 이해했는가?
- [ ] 객체를 Local Storage에 저장·복원할 수 있는가?
- [ ] 저장 데이터 오류 시 Fallback을 제공하는가?
- [ ] API 요청 Body를 JSON 문자열로 만들 수 있는가?
- [ ] JSON Parse 성공 후 데이터 형태도 검증해야 함을 이해했는가?

---

<a id="js-19-section-82"></a>

## 마무리

JSON 처리의 핵심은 객체에 `JSON.stringify()`를 적용하는 것에서 끝나지 않는다.

```text
객체와 JSON 문자열을 정확히 구분하고
    ↓
변환 과정에서 손실되는 값을 이해하고
    ↓
유효하지 않은 문자열과 저장 오류를 처리하고
    ↓
객체 배열과 Property를 목적에 맞게 순회하고
    ↓
저장·API 전송에 안전한 데이터 구조를 설계하는 것
```

이 흐름을 이해하면 다음 AJAX·Fetch 문서에서 서버와 주고받는 데이터를 더 정확하게 처리할 수 있다.
<a id="js-19-section-83"></a>

## V3 실행 추적 카드 — JS 값 ↔ JSON 문자열

`JSON.stringify`는 객체를 전송·저장 가능한 문자열로 만들고 `JSON.parse`는 문자열을 JS 값으로 복원한다. 함수와 undefined 등은 그대로 보존되지 않는다.

`const text=JSON.stringify({name:"Kim"}); console.log(typeof text, JSON.parse(text).name);`은 `string Kim`이다. 잘못된 JSON은 SyntaxError다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/19_json.html`에서 실제 사용 위치와 차이를 확인한다.
