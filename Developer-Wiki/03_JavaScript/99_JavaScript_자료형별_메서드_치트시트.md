# JavaScript 자료형별 메서드 치트시트

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `99_JavaScript_자료형별_메서드_치트시트.md` |
| 분류 | `03_JavaScript` |
| 문서 성격 | 수업 진도와 분리된 참고용 부록 |
| 핵심 범위 | String, Array, Object, Number, Math, JSON, Set, Map, DOM |
| 학습 기준 | 사용 가능한 자료형, 반환 타입, 원본 변경 여부 |
| 보충 범위 | 자료형 변환 후 다른 자료형의 메서드를 연결해서 사용하는 방법 |

> 이 문서는 JavaScript 메서드를 단순히 외우는 것이 아니라,  
> **어떤 자료형에 속한 기능인지**, **실행 결과로 무엇을 반환하는지**,  
> **원본 데이터를 직접 변경하는지**를 구분하기 위한 참고 문서입니다.

---

# 학습 목표

- 메서드가 어느 자료형에서 사용되는지 구분한다.
- 메서드 실행 후 반환되는 자료형을 예상한다.
- 원본 데이터 변경 여부를 확인한다.
- 사용할 수 없는 메서드는 자료형 변환 후 연결한다.
- 비슷한 메서드의 차이를 비교한다.
- 수업에서 자주 사용한 메서드와 알아두면 좋은 메서드를 함께 익힌다.

---

# 1. 가장 먼저 기억할 원칙

JavaScript의 메서드는 모든 값에 공통으로 존재하지 않습니다.

```javascript
"HTML,CSS,JavaScript".split(",")   // String 메서드
["HTML", "CSS"].join(" / ")        // Array 메서드
Object.keys({ name: "Kim" })       // Object 정적 메서드
```
# V3 실행 추적 카드 — 객체.메서드(인수) → 반환값/원본 변경

메서드는 이름만 외우지 않고 호출 객체 자료형, 반환값, 원본 변경, 콜백 인수 순서를 확인한다. 배열의 push/sort/splice는 원본을 바꾸고 map/filter/slice는 새 배열을 만든다.

`const a=[3,1]; const b=a.sort(); console.log(a,b,a===b);`는 정렬된 두 배열과 `true`를 보여 같은 객체임을 확인한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/01_var, 06_array, 10_string, 19_json 등 관련 원본`에서 실제 사용 위치와 차이를 확인한다.


다음 코드는 실행할 수 없습니다.

```javascript
const user = {
    name: "Kim",
    age: 20
};

user.join(","); // TypeError
```

`join()`은 Object의 메서드가 아니라 Array의 메서드이기 때문입니다.

Object를 배열로 바꾼 뒤 사용해야 합니다.

```javascript
const user = {
    name: "Kim",
    age: 20
};

const keys = Object.keys(user);
const result = keys.join(", ");

console.log(result);
```

출력:

```text
name, age
```

핵심 흐름:

```text
Object
  ↓ Object.keys()
Array
  ↓ join()
String
```

---

# 2. 표 읽는 방법

| 표시 | 의미 |
| --- | --- |
| ✅ | 해당 자료형에서 사용할 수 있음 |
| ❌ | 해당 자료형에서 직접 사용할 수 없음 |
| 🔴 변경 | 원본 값을 직접 변경함 |
| 🟢 유지 | 원본 값을 변경하지 않음 |
| ⭐ | 수업 또는 기초 학습에서 자주 사용 |
| 💡 | 아직 사용하지 않았더라도 알아두면 좋은 기능 |

> 문자열과 숫자 같은 원시값은 일반적으로 직접 수정되지 않습니다.  
> 문자열 메서드는 대부분 새로운 문자열이나 다른 값을 반환합니다.

---

# 3. 한눈에 보는 소속별 핵심 표

| 메서드 | String | Array | Object | 반환 타입 | 원본 변경 | 분류 |
| --- | :---: | :---: | :---: | --- | :---: | :---: |
| `split()` | ✅ | ❌ | ❌ | Array | 🟢 유지 | ⭐ |
| `join()` | ❌ | ✅ | ❌ | String | 🟢 유지 | ⭐ |
| `slice()` | ✅ | ✅ | ❌ | String 또는 Array | 🟢 유지 | ⭐ |
| `includes()` | ✅ | ✅ | ❌ | Boolean | 🟢 유지 | ⭐ |
| `indexOf()` | ✅ | ✅ | ❌ | Number | 🟢 유지 | ⭐ |
| `replace()` | ✅ | ❌ | ❌ | String | 🟢 유지 | ⭐ |
| `trim()` | ✅ | ❌ | ❌ | String | 🟢 유지 | ⭐ |
| `push()` | ❌ | ✅ | ❌ | Number | 🔴 변경 | ⭐ |
| `pop()` | ❌ | ✅ | ❌ | 제거한 요소 또는 `undefined` | 🔴 변경 | ⭐ |
| `shift()` | ❌ | ✅ | ❌ | 제거한 요소 또는 `undefined` | 🔴 변경 | ⭐ |
| `unshift()` | ❌ | ✅ | ❌ | Number | 🔴 변경 | ⭐ |
| `splice()` | ❌ | ✅ | ❌ | Array | 🔴 변경 | ⭐ |
| `map()` | ❌ | ✅ | ❌ | Array | 🟢 유지 | ⭐ |
| `filter()` | ❌ | ✅ | ❌ | Array | 🟢 유지 | ⭐ |
| `find()` | ❌ | ✅ | ❌ | 요소 또는 `undefined` | 🟢 유지 | ⭐ |
| `findIndex()` | ❌ | ✅ | ❌ | Number | 🟢 유지 | ⭐ |
| `forEach()` | ❌ | ✅ | ❌ | `undefined` | 🟢 유지* | ⭐ |
| `reduce()` | ❌ | ✅ | ❌ | 누적 결과 | 🟢 유지* | 💡 |
| `sort()` | ❌ | ✅ | ❌ | Array | 🔴 변경 | ⭐ |
| `reverse()` | ❌ | ✅ | ❌ | Array | 🔴 변경 | ⭐ |
| `Object.keys()` | ❌ | ❌ | ✅ | Array | 🟢 유지 | ⭐ |
| `Object.values()` | ❌ | ❌ | ✅ | Array | 🟢 유지 | ⭐ |
| `Object.entries()` | ❌ | ❌ | ✅ | Array | 🟢 유지 | ⭐ |
| `Object.assign()` | ❌ | ❌ | ✅ | Object | 조건부 | 💡 |

\* 콜백 함수 내부에서 요소나 외부 객체를 직접 수정하면 데이터가 변경될 수 있습니다.

---

# 4. String 메서드

문자열은 문자의 순서가 있는 데이터입니다.

```javascript
const language = "JavaScript";
```

문자열 메서드는 원본 문자열을 바꾸지 않고 새로운 문자열, 배열, 숫자 또는 논리값을 반환하는 경우가 대부분입니다.

## 4.1 String 메서드 표

| 메서드 | 반환 타입 | 원본 변경 | 설명 | 분류 |
| --- | --- | :---: | --- | :---: |
| `split()` | Array | 🟢 유지 | 구분자를 기준으로 문자열을 배열로 분리 | ⭐ |
| `slice()` | String | 🟢 유지 | 지정한 범위의 문자열 추출 | ⭐ |
| `substring()` | String | 🟢 유지 | 시작·종료 인덱스로 문자열 추출 | ⭐ |
| `replace()` | String | 🟢 유지 | 일치하는 일부 문자열 치환 | ⭐ |
| `replaceAll()` | String | 🟢 유지 | 일치하는 모든 문자열 치환 | 💡 |
| `trim()` | String | 🟢 유지 | 양쪽 공백 제거 | ⭐ |
| `trimStart()` | String | 🟢 유지 | 앞쪽 공백 제거 | 💡 |
| `trimEnd()` | String | 🟢 유지 | 뒤쪽 공백 제거 | 💡 |
| `includes()` | Boolean | 🟢 유지 | 포함 여부 확인 | ⭐ |
| `startsWith()` | Boolean | 🟢 유지 | 특정 문자열로 시작하는지 확인 | 💡 |
| `endsWith()` | Boolean | 🟢 유지 | 특정 문자열로 끝나는지 확인 | 💡 |
| `indexOf()` | Number | 🟢 유지 | 처음 등장한 위치 반환 | ⭐ |
| `lastIndexOf()` | Number | 🟢 유지 | 마지막 등장 위치 반환 | 💡 |
| `toUpperCase()` | String | 🟢 유지 | 대문자로 변환 | ⭐ |
| `toLowerCase()` | String | 🟢 유지 | 소문자로 변환 | ⭐ |
| `charAt()` | String | 🟢 유지 | 지정 인덱스의 문자 반환 | 💡 |
| `repeat()` | String | 🟢 유지 | 문자열 반복 | 💡 |
| `padStart()` | String | 🟢 유지 | 앞쪽을 지정 문자로 채움 | 💡 |
| `padEnd()` | String | 🟢 유지 | 뒤쪽을 지정 문자로 채움 | 💡 |

## 4.2 `split()` — String에서 Array로

```javascript
const text = "HTML,CSS,JavaScript";
const languages = text.split(",");

console.log(languages);
console.log(Array.isArray(languages));
```

출력:

```text
["HTML", "CSS", "JavaScript"]
true
```

자료형 흐름:

```text
String → split() → Array
```

배열로 변환되었기 때문에 이후에는 Array 메서드를 사용할 수 있습니다.

```javascript
const result = "HTML,CSS,JavaScript"
    .split(",")
    .map(item => item.toUpperCase())
    .join(" / ");

console.log(result);
```

출력:

```text
HTML / CSS / JAVASCRIPT
```

## 4.3 `trim()`과 입력값 정리

```javascript
const input = "   JavaScript   ";
const result = input.trim();

console.log(result);
console.log(input);
```

출력:

```text
JavaScript
   JavaScript
```

원본 `input`은 유지되고 새로운 문자열이 반환됩니다.

## 4.4 문자열 메서드 연결

```javascript
const input = "  html, css, javascript  ";

const result = input
    .trim()
    .toUpperCase()
    .split(", ")
    .join(" → ");

console.log(result);
```

자료형 흐름:

```text
String
  ↓ trim()
String
  ↓ toUpperCase()
String
  ↓ split()
Array
  ↓ join()
String
```

---

# 5. Array 메서드

Array는 여러 값을 순서대로 저장하는 자료형입니다.

```javascript
const fruits = ["apple", "banana", "peach"];
```

Array 메서드는 원본을 직접 변경하는 메서드와 새로운 값을 반환하는 메서드가 섞여 있습니다.

## 5.1 Array 메서드 표

| 메서드 | 반환 타입 | 원본 변경 | 설명 | 분류 |
| --- | --- | :---: | --- | :---: |
| `push()` | Number | 🔴 변경 | 뒤에 요소 추가, 새 길이 반환 | ⭐ |
| `pop()` | 요소 | 🔴 변경 | 마지막 요소 제거 및 반환 | ⭐ |
| `unshift()` | Number | 🔴 변경 | 앞에 요소 추가, 새 길이 반환 | ⭐ |
| `shift()` | 요소 | 🔴 변경 | 첫 번째 요소 제거 및 반환 | ⭐ |
| `splice()` | Array | 🔴 변경 | 원하는 위치에서 삭제·추가 | ⭐ |
| `sort()` | Array | 🔴 변경 | 배열 정렬 | ⭐ |
| `reverse()` | Array | 🔴 변경 | 배열 순서 반전 | ⭐ |
| `fill()` | Array | 🔴 변경 | 일정 범위를 지정 값으로 채움 | 💡 |
| `copyWithin()` | Array | 🔴 변경 | 배열 내부 요소 복사 | 💡 |
| `slice()` | Array | 🟢 유지 | 일부 범위를 복사 | ⭐ |
| `concat()` | Array | 🟢 유지 | 배열을 합친 새 배열 반환 | ⭐ |
| `join()` | String | 🟢 유지 | 배열 요소를 문자열로 연결 | ⭐ |
| `includes()` | Boolean | 🟢 유지 | 값 포함 여부 | ⭐ |
| `indexOf()` | Number | 🟢 유지 | 값의 위치 | ⭐ |
| `map()` | Array | 🟢 유지 | 각 요소를 변환한 새 배열 | ⭐ |
| `filter()` | Array | 🟢 유지 | 조건을 통과한 새 배열 | ⭐ |
| `find()` | 요소 | 🟢 유지 | 조건을 통과한 첫 요소 | ⭐ |
| `findIndex()` | Number | 🟢 유지 | 조건을 통과한 첫 인덱스 | ⭐ |
| `forEach()` | `undefined` | 🟢 유지* | 각 요소에 작업 수행 | ⭐ |
| `reduce()` | 누적 결과 | 🟢 유지* | 여러 값을 하나로 누적 | 💡 |
| `some()` | Boolean | 🟢 유지 | 하나라도 조건을 만족하는지 | 💡 |
| `every()` | Boolean | 🟢 유지 | 모두 조건을 만족하는지 | 💡 |
| `flat()` | Array | 🟢 유지 | 중첩 배열을 평탄화 | 💡 |
| `flatMap()` | Array | 🟢 유지 | `map()` 후 한 단계 평탄화 | 💡 |
| `at()` | 요소 | 🟢 유지 | 양수·음수 인덱스로 요소 조회 | 💡 |

## 5.2 `join()` — Array에서 String으로

```javascript
const languages = ["HTML", "CSS", "JavaScript"];
const result = languages.join(" → ");

console.log(result);
```

출력:

```text
HTML → CSS → JavaScript
```

자료형 흐름:

```text
Array → join() → String
```

`join()`의 반환값은 문자열이므로 이후에는 String 메서드를 사용할 수 있습니다.

```javascript
const result = ["html", "css", "javascript"]
    .join(", ")
    .toUpperCase();

console.log(result);
```

## 5.3 `map()`과 `filter()` 연결

```javascript
const numbers = [1, 2, 3, 4, 5];

const result = numbers
    .filter(number => number % 2 === 1)
    .map(number => number * 10);

console.log(result);
```

출력:

```text
[10, 30, 50]
```

## 5.4 원본 변경 확인

```javascript
const numbers = [3, 1, 2];
const sorted = numbers.sort();

console.log(numbers);
console.log(sorted);
```

출력:

```text
[1, 2, 3]
[1, 2, 3]
```

`sort()`는 원본 배열을 변경합니다.

원본을 유지하려면 먼저 복사합니다.

```javascript
const numbers = [3, 1, 2];
const sorted = [...numbers].sort((a, b) => a - b);

console.log(numbers);
console.log(sorted);
```

출력:

```text
[3, 1, 2]
[1, 2, 3]
```

---

# 6. Object 관련 메서드

일반 객체는 키와 값의 쌍으로 데이터를 저장합니다.

```javascript
const user = {
    name: "Kim",
    age: 20,
    job: "developer"
};
```

Object에는 Array의 `join()`, `map()`, `filter()`가 없습니다.

따라서 객체를 먼저 배열로 변환해야 합니다.

## 6.1 Object 메서드 표

| 메서드 | 반환 타입 | 원본 변경 | 설명 | 분류 |
| --- | --- | :---: | --- | :---: |
| `Object.keys()` | Array | 🟢 유지 | 키를 배열로 반환 | ⭐ |
| `Object.values()` | Array | 🟢 유지 | 값을 배열로 반환 | ⭐ |
| `Object.entries()` | Array | 🟢 유지 | `[키, 값]` 배열로 반환 | ⭐ |
| `Object.fromEntries()` | Object | 🟢 유지 | 엔트리 배열을 객체로 변환 | 💡 |
| `Object.assign()` | Object | 조건부 | 첫 번째 인수에 속성 복사 | 💡 |
| `Object.hasOwn()` | Boolean | 🟢 유지 | 직접 소유한 속성인지 확인 | 💡 |
| `Object.freeze()` | Object | 상태 변경 | 객체의 변경을 제한 | 💡 |

## 6.2 Object의 키를 `join()`으로 연결

```javascript
const user = {
    name: "Kim",
    age: 20,
    job: "developer"
};

const result = Object.keys(user).join(", ");

console.log(result);
```

출력:

```text
name, age, job
```

## 6.3 Object의 값을 `join()`으로 연결

```javascript
const user = {
    name: "Kim",
    age: 20,
    job: "developer"
};

const result = Object.values(user).join(" / ");

console.log(result);
```

출력:

```text
Kim / 20 / developer
```

## 6.4 Object를 문장 배열로 바꾼 뒤 `join()`

```javascript
const user = {
    name: "Kim",
    age: 20,
    job: "developer"
};

const result = Object.entries(user)
    .map(([key, value]) => `${key}: ${value}`)
    .join(", ");

console.log(result);
```

출력:

```text
name: Kim, age: 20, job: developer
```

자료형 흐름:

```text
Object
  ↓ Object.entries()
Array<Array>
  ↓ map()
Array<String>
  ↓ join()
String
```

## 6.5 Object 필터링 후 다시 Object로 변환

```javascript
const scores = {
    html: 90,
    css: 70,
    javascript: 95,
    python: 80
};

const passed = Object.fromEntries(
    Object.entries(scores)
        .filter(([, score]) => score >= 80)
);

console.log(passed);
```

출력:

```text
{
    html: 90,
    javascript: 95,
    python: 80
}
```

자료형 흐름:

```text
Object
  ↓ Object.entries()
Array
  ↓ filter()
Array
  ↓ Object.fromEntries()
Object
```

## 6.6 Object에는 왜 `map()`이 없을까?

```javascript
const user = {
    name: "Kim",
    age: 20
};

user.map(item => item); // TypeError
```

객체를 엔트리 배열로 변환하면 사용할 수 있습니다.

```javascript
const result = Object.entries(user)
    .map(([key, value]) => [key.toUpperCase(), value]);

console.log(result);
```

다시 객체가 필요하면:

```javascript
const converted = Object.fromEntries(result);
console.log(converted);
```

---

# 7. Number와 Math

## 7.1 Number 메서드

| 메서드 | 사용 방식 | 반환 타입 | 원본 변경 | 설명 |
| --- | --- | --- | :---: | --- |
| `toFixed()` | 숫자 값 | String | 🟢 유지 | 소수점 자릿수 지정 |
| `toString()` | 숫자 값 | String | 🟢 유지 | 문자열 변환 |
| `Number.isInteger()` | Number 정적 메서드 | Boolean | 🟢 유지 | 정수 여부 |
| `Number.isNaN()` | Number 정적 메서드 | Boolean | 🟢 유지 | `NaN` 여부 |
| `Number()` | 변환 함수 | Number | 🟢 유지 | 숫자로 변환 |
| `parseInt()` | 전역 함수 | Number | 🟢 유지 | 정수 부분 변환 |
| `parseFloat()` | 전역 함수 | Number | 🟢 유지 | 실수 변환 |

```javascript
const price = 1234.567;
const result = price.toFixed(2);

console.log(result);
console.log(typeof result);
```

출력:

```text
1234.57
string
```

`toFixed()`는 Number가 아니라 String을 반환한다는 점에 주의합니다.

## 7.2 Math 메서드

| 메서드 | 반환 타입 | 설명 |
| --- | --- | --- |
| `Math.floor()` | Number | 내림 |
| `Math.ceil()` | Number | 올림 |
| `Math.round()` | Number | 반올림 |
| `Math.trunc()` | Number | 소수 부분 제거 |
| `Math.random()` | Number | 0 이상 1 미만 난수 |
| `Math.max()` | Number | 가장 큰 값 |
| `Math.min()` | Number | 가장 작은 값 |
| `Math.abs()` | Number | 절댓값 |
| `Math.pow()` | Number | 거듭제곱 |
| `Math.sqrt()` | Number | 제곱근 |

```javascript
const numbers = [10, 30, 20];
const max = Math.max(...numbers);

console.log(max);
```

Array를 `Math.max()`에 전달할 때는 펼침 연산자가 필요합니다.

---

# 8. JSON

| 메서드 | 입력 | 반환 타입 | 설명 |
| --- | --- | --- | --- |
| `JSON.stringify()` | Object, Array 등 | String | JavaScript 값을 JSON 문자열로 변환 |
| `JSON.parse()` | JSON String | Object, Array 등 | JSON 문자열을 JavaScript 값으로 변환 |

```javascript
const user = {
    name: "Kim",
    age: 20
};

const json = JSON.stringify(user);
const restored = JSON.parse(json);

console.log(typeof json);
console.log(typeof restored);
```

출력:

```text
string
object
```

자료형 흐름:

```text
Object → JSON.stringify() → String
String → JSON.parse() → Object
```

---

# 9. Set

Set은 중복을 허용하지 않는 값의 집합입니다.

| 메서드 | 반환 타입 | 원본 변경 | 설명 |
| --- | --- | :---: | --- |
| `add()` | Set | 🔴 변경 | 값 추가 |
| `delete()` | Boolean | 🔴 변경 | 값 삭제 |
| `has()` | Boolean | 🟢 유지 | 값 존재 여부 |
| `clear()` | `undefined` | 🔴 변경 | 전체 삭제 |
| `values()` | Iterator | 🟢 유지 | 값 반복자 반환 |

Set에는 `map()`과 `join()`이 없습니다.

배열로 변환한 뒤 사용합니다.

```javascript
const skills = new Set(["HTML", "CSS", "HTML", "JavaScript"]);

const result = [...skills]
    .map(skill => skill.toUpperCase())
    .join(" / ");

console.log(result);
```

출력:

```text
HTML / CSS / JAVASCRIPT
```

자료형 흐름:

```text
Set → 펼침 연산자 → Array → map() → Array → join() → String
```

---

# 10. Map

Map은 키와 값의 쌍을 저장하는 컬렉션입니다.

| 메서드 | 반환 타입 | 원본 변경 | 설명 |
| --- | --- | :---: | --- |
| `set()` | Map | 🔴 변경 | 키와 값 저장 |
| `get()` | 값 또는 `undefined` | 🟢 유지 | 키로 값 조회 |
| `has()` | Boolean | 🟢 유지 | 키 존재 여부 |
| `delete()` | Boolean | 🔴 변경 | 항목 삭제 |
| `clear()` | `undefined` | 🔴 변경 | 전체 삭제 |
| `keys()` | Iterator | 🟢 유지 | 키 반복자 |
| `values()` | Iterator | 🟢 유지 | 값 반복자 |
| `entries()` | Iterator | 🟢 유지 | 엔트리 반복자 |

```javascript
const scores = new Map([
    ["HTML", 90],
    ["CSS", 80],
    ["JavaScript", 95]
]);

const result = [...scores.entries()]
    .map(([subject, score]) => `${subject}: ${score}`)
    .join(", ");

console.log(result);
```

---

# 11. DOM에서 자주 사용하는 메서드

DOM 메서드는 일반 String·Array·Object 메서드와 소속이 다릅니다.

| 메서드 | 사용 대상 | 반환 타입 | 원본/문서 변경 | 설명 |
| --- | --- | --- | :---: | --- |
| `document.querySelector()` | Document | Element 또는 `null` | 🟢 유지 | 첫 요소 선택 |
| `document.querySelectorAll()` | Document | NodeList | 🟢 유지 | 여러 요소 선택 |
| `document.getElementById()` | Document | Element 또는 `null` | 🟢 유지 | id로 선택 |
| `document.createElement()` | Document | Element | 🟢 유지 | 요소 생성 |
| `element.append()` | Element | `undefined` | 🔴 DOM 변경 | 마지막에 추가 |
| `element.prepend()` | Element | `undefined` | 🔴 DOM 변경 | 처음에 추가 |
| `element.remove()` | Element | `undefined` | 🔴 DOM 변경 | 요소 제거 |
| `element.classList.add()` | DOMTokenList | `undefined` | 🔴 DOM 변경 | 클래스 추가 |
| `element.classList.remove()` | DOMTokenList | `undefined` | 🔴 DOM 변경 | 클래스 제거 |
| `element.classList.contains()` | DOMTokenList | Boolean | 🟢 유지 | 클래스 포함 여부 |
| `element.addEventListener()` | EventTarget | `undefined` | 이벤트 등록 | 이벤트 연결 |

`querySelectorAll()`은 NodeList를 반환합니다.

```javascript
const quizzes = document.querySelectorAll("div.quiz");
```

NodeList 자체에는 `classList`가 없습니다.

```javascript
quizzes.classList.contains("q2"); // 오류
```

각 요소를 선택해야 합니다.

```javascript
quizzes.forEach(quiz => {
    console.log(quiz.classList.contains("q2"));
});
```

또는 Array로 변환할 수 있습니다.

```javascript
const result = [...quizzes]
    .filter(quiz => quiz.classList.contains("q2"));

console.log(result);
```

---

# 12. 자주 헷갈리는 메서드 비교

## 12.1 `split()` vs `join()`

| 구분 | `split()` | `join()` |
| --- | --- | --- |
| 소속 | String | Array |
| 변환 | String → Array | Array → String |
| 원본 변경 | 없음 | 없음 |

```javascript
const array = "HTML,CSS".split(",");
const string = ["HTML", "CSS"].join(",");
```

## 12.2 `slice()` vs `splice()`

| 구분 | `slice()` | `splice()` |
| --- | --- | --- |
| 원본 변경 | 없음 | 있음 |
| 반환 | 복사한 배열 | 제거한 요소 배열 |
| 용도 | 일부 복사 | 삭제·삽입 |

## 12.3 `map()` vs `forEach()`

| 구분 | `map()` | `forEach()` |
| --- | --- | --- |
| 반환 | 새 Array | `undefined` |
| 주요 목적 | 요소 변환 | 반복 작업 |
| 체이닝 | 적합 | 반환값으로 체이닝 불가 |

```javascript
const result = [1, 2, 3].map(number => number * 2);
```

```javascript
const result = [1, 2, 3].forEach(number => number * 2);
console.log(result); // undefined
```

## 12.4 `find()` vs `filter()`

| 구분 | `find()` | `filter()` |
| --- | --- | --- |
| 반환 | 첫 번째 요소 하나 | 조건을 만족한 새 배열 |
| 없을 때 | `undefined` | 빈 배열 |

## 12.5 `includes()` vs `indexOf()`

| 구분 | `includes()` | `indexOf()` |
| --- | --- | --- |
| 반환 | Boolean | Number |
| 없을 때 | `false` | `-1` |
| 목적 | 존재 여부 | 위치 확인 |

---

# 13. 자료형 변환 연결 예제

## 13.1 Object → Array → String

```javascript
const product = {
    name: "keyboard",
    price: 50000,
    stock: 3
};

const summary = Object.entries(product)
    .map(([key, value]) => `${key}=${value}`)
    .join(" | ");

console.log(summary);
```

## 13.2 String → Array → 조건 처리 → String

```javascript
const input = "apple, banana, peach, kiwi";

const result = input
    .split(", ")
    .filter(fruit => fruit.length >= 5)
    .map(fruit => fruit.toUpperCase())
    .join(" / ");

console.log(result);
```

## 13.3 Set → Array → String

```javascript
const tags = new Set(["js", "html", "js", "css"]);

const result = Array.from(tags)
    .sort()
    .join(", ");

console.log(result);
```

## 13.4 JSON String → Object → Array → String

```javascript
const json = `{
    "name": "Kim",
    "skills": ["HTML", "CSS", "JavaScript"]
}`;

const result = JSON.parse(json)
    .skills
    .join(" → ");

console.log(result);
```

## 13.5 Array → Object

```javascript
const entries = [
    ["name", "Kim"],
    ["age", 20]
];

const user = Object.fromEntries(entries);

console.log(user);
```

---

# 14. 오류를 만났을 때 확인 순서

다음 오류가 나왔다고 가정합니다.

```text
TypeError: value.join is not a function
```

확인 순서:

1. `value`의 현재 자료형을 확인한다.
2. `join()`이 어느 자료형의 메서드인지 확인한다.
3. 현재 값이 Array가 아니라면 배열로 변환할 수 있는지 확인한다.
4. 메서드 실행 후 반환 타입을 확인한다.
5. 다음 메서드가 그 반환 타입에서 사용 가능한지 확인한다.

```javascript
console.log(value);
console.log(typeof value);
console.log(Array.isArray(value));
```

Object라면:

```javascript
Object.keys(value).join(", ");
Object.values(value).join(", ");
Object.entries(value).map(...).join(", ");
```

---

# 15. 최종 체크리스트

- [ ] `split()`은 String 메서드임을 설명할 수 있다.
- [ ] `join()`은 Array 메서드임을 설명할 수 있다.
- [ ] Object에 `join()`을 직접 사용할 수 없는 이유를 안다.
- [ ] `Object.keys()`, `Object.values()`, `Object.entries()`의 반환 타입이 Array임을 안다.
- [ ] `map()`과 `forEach()`의 반환값 차이를 안다.
- [ ] `slice()`와 `splice()`의 원본 변경 여부를 구분한다.
- [ ] `sort()`가 원본 배열을 변경한다는 것을 안다.
- [ ] 메서드 체이닝 중간의 반환 타입을 추적할 수 있다.
- [ ] Set, Map, NodeList를 Array로 변환해 Array 메서드를 사용할 수 있다.
- [ ] 오류 발생 시 현재 자료형부터 확인한다.

---

# 핵심 요약

```text
split()  : String → Array
join()   : Array → String

Object.keys()    : Object → Array
Object.values()  : Object → Array
Object.entries() : Object → Array
Object.fromEntries() : Array → Object

JSON.stringify() : Object/Array → String
JSON.parse()     : JSON String → Object/Array

map()    : Array → Array
filter() : Array → Array
find()   : Array → 요소 하나
forEach(): Array → undefined
reduce() : Array → 누적 결과
```

메서드 이름만 외우기보다 다음 세 가지를 함께 기억합니다.

```text
1. 어떤 자료형에서 사용하는가?
2. 무엇을 반환하는가?
3. 원본을 변경하는가?
```
