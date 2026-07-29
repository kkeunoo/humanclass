# JavaScript 배열과 배열 메서드

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `06_JavaScript_배열과_배열메서드.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `05_JavaScript_While과_DoWhile.md` |
| 다음 학습 | `07_JavaScript_Date와_날짜처리.md` |
| 원본 기준 | `workspace_me/workspace/workspace_html/javascript/06_array.html`, `workspace_teacher/workspace_teacher/workspace_html/javascript/06_array.html` |
| 핵심 범위 | 배열 선언, index, length, 중첩 배열, 배열 요소 변경, 희소 배열, 문자열 index 접근, `push()`, `unshift()`, `pop()`, `shift()`, `reverse()`, `sort()`, `slice()`, `indexOf()`, `join()`, `split()`, `splice()`, URL 쿼리스트링 분석, 이메일 도메인 추출, 배열 문제 풀이 |
| 프로젝트 연결 | 목록 데이터 관리, 좌석 예약, 검색 쿼리 분석, 이메일 검증, 참가자 비교, 로또 번호 생성, 장바구니, 테이블 데이터, API 응답 처리 |

> 이 문서는 내 코드와 강사님 코드의 `06_array.html`을 직접 비교해 작성했습니다. 강사님 코드는 배열의 기본 구조와 주요 메서드, URL 쿼리스트링 분석, 문제 목록, `splice()` 기본 예제를 제공합니다. 내 코드는 배열·메모리 설명, URL·이메일 추가 실습, 문제 1~5 풀이와 숫자야구 계획까지 크게 확장했습니다. 다만 일부 설명은 부정확하고, 문제 풀이에는 논리 오류나 미완성 부분이 있으므로 원본을 보존한 뒤 실행 결과에 근거해 설명합니다.

---

# 학습 목표

- 배열이 여러 값을 순서대로 관리하는 자료구조임을 설명한다.
- 배열 index가 0부터 시작한다는 점을 이해한다.
- 배열 리터럴과 `new Array()` 선언 방식을 비교한다.
- `typeof array`가 `"object"`인 이유와 배열 판별 방법을 이해한다.
- `const` 배열의 요소 변경과 배열 자체 재할당을 구분한다.
- 문자열과 배열의 index 접근 차이를 이해한다.
- 존재하지 않는 index 접근 결과가 `undefined`임을 설명한다.
- 희소 배열과 사용자 정의 속성 추가의 문제점을 이해한다.
- `length`를 이용해 전체 요소를 순회한다.
- 중첩 배열의 요소에 이중 index로 접근한다.
- `push()`, `unshift()`, `pop()`, `shift()`의 역할과 반환값을 구분한다.
- `reverse()`와 `sort()`가 원본 배열을 변경한다는 점을 이해한다.
- 숫자 정렬에 비교 함수가 필요한 이유를 설명한다.
- `slice()`와 `splice()`의 차이를 구분한다.
- `indexOf()`의 결과와 미발견 시 `-1`을 이해한다.
- `join()`과 `split()`으로 배열과 문자열을 변환한다.
- URL 쿼리스트링과 이메일 주소를 분해한다.
- 참가자·완주자 비교, 좌석 예약, 중복 없는 로또 문제를 배열로 해결한다.
- 내 코드와 강사님 코드의 실제 차이와 원본 오류를 분석한다.

---

# 1. 배열이란?

배열은 여러 값을 하나의 변수 아래 순서대로 저장하는 자료구조입니다.

```js
const fruits = ["apple", "banana", "orange"]
```

각 값은 index로 구분합니다.

```text
index 0 → "apple"
index 1 → "banana"
index 2 → "orange"
```

JavaScript 배열의 index는 0부터 시작합니다.

---

# 2. 원본의 배열 설명

강사님 원본:

```text
한번에 여러 변수를 만드는 기술
각 변수는 index로 구분한다
index는 0번부터 시작
```

내 코드:

```text
한 번에 여러 변수를 만드는 기술
각 변수는 index로 구분(관리)한다
index는 '0번'부터 시작한다
```

학습용으로 이해하기 쉬운 설명이지만, 배열 요소를 각각 독립된 변수라고만 보는 것보다 다음 표현이 더 정확합니다.

```text
배열은 여러 값을 하나의 순서 있는 자료구조로 관리한다.
각 요소는 0부터 시작하는 index로 접근한다.
```

---

# 3. 배열 선언 방법 1

공통 원본:

```js
const arr1 = []
```

배열 리터럴 방식입니다.

실무에서 가장 흔히 사용합니다.

```js
const numbers = [1, 2, 3]
```

빈 배열을 만든 뒤 값을 추가할 수도 있습니다.

```js
const values = []
values.push(10)
```

---

# 4. 배열 선언 방법 2

공통 원본:

```js
const arr2 = new Array()
```

생성자 방식입니다.

여러 값을 전달하면 배열 요소가 됩니다.

```js
const values =
  new Array(1, 2, 3)
```

주의:

```js
new Array(3)
```

은 `[3]`이 아니라 길이 3의 빈 슬롯 배열을 만듭니다.

이 차이 때문에 일반적으로 배열 리터럴을 더 자주 사용합니다.

---

# 5. Typeof 배열

공통 원본:

```js
console.log(typeof arr1)
```

결과:

```text
object
```

배열은 JavaScript 객체의 한 종류입니다.

배열인지 정확히 확인하려면:

```js
Array.isArray(arr1)
```

결과:

```text
true
```

---

# 6. 혼합 자료형 배열

공통 원본:

```js
const arr3 = [
  1,
  2,
  "글씨",
  false,
  3.14,
  arr1
]
```

JavaScript 배열에는 서로 다른 자료형을 함께 저장할 수 있습니다.

```text
number
string
boolean
array
```

문법적으로 가능하지만 실무에서는 한 배열에 비슷한 의미와 구조의 값을 넣는 편이 관리하기 쉽습니다.

---

# 7. 내 코드와 강사님 코드의 Arr3 선언 차이

강사님 코드:

```js
let arr3 = [
  1, 2, "글씨", false, 3.14, arr1
]
```

내 코드:

```js
const arr3 = [
  1, 2, "글씨", false, 3.14, arr1
]
```

이 차이는 뒤의 재할당 코드에 직접 영향을 줍니다.

강사님 코드:

```js
arr3 = [1, 2, 3]
```

정상 실행됩니다.

내 코드에서는 같은 코드가 주석 처리되어 있습니다.

```js
// arr3 = [1, 2, 3]
```

주석을 해제하면 `const` 재할당 오류가 발생합니다.

---

# 8. Const 배열의 요소 변경

내 코드:

```js
const arr3 = [1, 2, 3]

arr3[0] = 10
```

이 코드는 가능합니다.

결과:

```js
[10, 2, 3]
```

`const`는 변수 바인딩의 재할당을 막습니다.

배열 내부 요소의 변경까지 자동으로 막지는 않습니다.

---

# 9. Const 배열의 재할당

불가능:

```js
const arr3 = [1, 2, 3]

arr3 = [4, 5, 6]
```

결과:

```text
TypeError
```

가능:

```js
arr3[0] = 4
arr3.push(5)
```

---

# 10. 내 코드 배열 정리 설명 검토

내 코드:

```text
const로 선언했다면 중복 선언이 불가하기 때문에 값을 바꿀 수 없음
```

여기에는 재선언과 재할당이 섞여 있습니다.

정확한 구분:

```text
const 배열 변수는 같은 스코프에서 재선언할 수 없다.
const 배열 변수에 새 배열을 재할당할 수 없다.
기존 배열의 요소는 변경할 수 있다.
```

---

# 11. 배열 출력 방식

내 코드:

```js
console.log("arr3[0]:" + arr3)
console.log("arr3[0]:", arr3)
console.log("arr3[0]:", arr3[0])
```

첫 번째:

```js
"arr3[0]:" + arr3
```

배열이 문자열로 변환됩니다.

두 번째:

```js
console.log("arr3[0]:", arr3)
```

배열 객체 자체를 별도 인수로 전달합니다.

세 번째:

```js
console.log("arr3[0]:", arr3[0])
```

첫 번째 요소만 출력합니다.

---

# 12. 잘못된 출력 Label

내 코드의 첫 두 출력은 실제로 배열 전체를 출력하면서 label은 `arr3[0]`이라고 적습니다.

```js
console.log("arr3[0]:" + arr3)
console.log("arr3[0]:", arr3)
```

정확한 label:

```js
console.log("arr3:", arr3)
```

강사님 코드는 올바르게 작성합니다.

```js
console.log("arr3:", arr3)
```

---

# 13. 배열 요소와 식별자 설명

내 코드:

```text
arr3[] 자체가 변수가 되었으며 본래 식별자(id)라고도 부름
```

이 설명은 부정확합니다.

- `arr3`는 식별자입니다.
- `arr3[0]`은 배열 요소에 접근하는 표현식입니다.
- `arr3[]`만 단독으로 작성하는 문법은 유효하지 않습니다.

정확한 표현:

```text
arr3는 배열을 가리키는 변수 식별자이다.
arr3[0]은 0번 index 요소에 접근하는 표현식이다.
```

---

# 14. 문자열 Index 접근

공통 원본:

```js
let s = "abc"

console.log(s[1])
```

결과:

```text
b
```

문자열도 index로 문자에 접근할 수 있습니다.

```text
s[0] → a
s[1] → b
s[2] → c
```

문자열은 배열과 달리 개별 문자를 직접 대입해 바꿀 수 없는 immutable 값입니다.

---

# 15. 존재하지 않는 배열 Index

공통 원본:

```js
let arr = [1, 2, 3, 4, 5]

console.log(arr[60])
```

결과:

```text
undefined
```

배열 자체가 선언되지 않은 경우와 다릅니다.

```js
console.log(arr60)
```

은 `ReferenceError`가 발생할 수 있습니다.

---

# 16. Undefined 비교

공통 원본:

```js
let i
console.log(i)
```

결과:

```text
undefined
```

두 경우:

```text
arr[60]
→ 배열은 존재하지만 해당 index 요소가 없음

i
→ 변수는 선언했지만 값이 없음
```

둘 다 결과는 undefined이지만 원인은 다릅니다.

---

# 17. 먼 Index에 값 추가

공통 원본:

```js
arr[60] = 60
```

배열의 length는 최소 61이 됩니다.

0~59 사이의 대부분 index는 빈 슬롯이 됩니다.

이를 희소 배열이라고 부를 수 있습니다.

```js
console.log(arr.length)
```

결과:

```text
61
```

---

# 18. 희소 배열 주의

희소 배열은 다음 문제를 만들 수 있습니다.

- 실제 요소 수와 length가 다름
- 배열 메서드마다 빈 슬롯 처리 차이
- 디버깅 어려움
- 불필요한 복잡성

일반적인 목록이라면 연속된 index를 유지하는 편이 좋습니다.

---

# 19. 문자열 Key 추가

공통 원본:

```js
arr["문자"] = "문자"
```

배열도 객체이므로 문자열 속성을 추가할 수 있습니다.

하지만 이 속성은 일반적인 배열 요소로 취급되지 않습니다.

```js
arr.length
```

에는 영향을 주지 않습니다.

배열에는 숫자 index 기반 요소를 사용하고, 이름 기반 속성은 일반 객체로 관리하는 편이 명확합니다.

---

# 20. 배열과 객체 혼용 주의

다음 구조보다:

```js
const arr = []
arr["name"] = "Kim"
```

일반 객체가 자연스럽습니다.

```js
const user = {
  name: "Kim"
}
```

배열은 순서 있는 목록, 객체는 이름 있는 속성 묶음에 적합합니다.

---

# 21. 내 코드의 Stack과 Heap 설명

내 코드에는 stack, heap, GC 설명이 추가되어 있습니다.

```text
stack은 늦게 들어온 것이 먼저 나감
heap에는 배열 값이 들어감
주소값을 stack에 저장
문자 1Byte, 숫자 4byte
```

일부 내용은 지나치게 단순하거나 JavaScript에 정확히 적용하기 어렵습니다.

특히:

- JavaScript 문자열의 문자당 크기를 항상 1Byte로 볼 수 없습니다.
- JavaScript Number는 일반적으로 IEEE 754 배정밀도 숫자로 다뤄집니다.
- 실제 메모리 배치는 엔진 구현에 따라 달라질 수 있습니다.
- 배열과 객체가 항상 한 가지 방식으로 stack·heap에 배치된다고 단정하기 어렵습니다.

이 단원에서는 참조형 값의 개념 정도로만 이해하는 것이 안전합니다.

---

# 22. Garbage Collector 설명

내 코드:

```text
배열변수 선언을 하고 주소값이 사라진다면
GC로 자료가 사라짐
```

핵심 개념:

```text
더 이상 접근 가능한 참조가 없는 객체는
가비지 컬렉션 대상이 될 수 있다.
```

언제 실제로 메모리가 회수되는지는 JavaScript 엔진이 결정합니다.

즉시 삭제된다고 단정하지 않습니다.

---

# 23. 배열 전체 순회

공통 원본:

```js
arr = [0, 1, 2, 3, 4, 5]

for (let i = 0; i < 6; i++) {
  console.log(arr[i])
}
```

0~5 index를 순회합니다.

배열 길이가 바뀌면 숫자 6을 수정해야 합니다.

---

# 24. Length 사용

공통 원본:

```js
for (
  let i = 0;
  i < arr.length;
  i++
) {
  console.log(arr[i])
}
```

배열 길이에 맞춰 자동으로 반복 범위가 바뀝니다.

일반적인 배열 전체 순회에 더 안전합니다.

---

# 25. 강사님 Index 증가 실험

강사님 코드에만 있습니다.

```js
i = 0
arr[i]

i = 1
arr[i]

arr[i++]
arr[i++]
arr[i++]
```

후위 증가 연산자를 index에 사용합니다.

```text
현재 i로 요소 접근
→ 접근 후 i 증가
```

이 코드는 표현 결과를 출력하거나 저장하지 않아 Console에서 직접 확인되지는 않습니다.

연산 흐름 실험용 코드입니다.

---

# 26. 중첩 배열

공통 원본:

```js
const 음식 = [
  양식,
  중식,
  일식
]
```

`음식`은 배열 안에 배열이 들어 있는 중첩 배열입니다.

```text
음식[0] → 양식 배열
음식[1] → 중식 배열
음식[2] → 일식 배열
```

---

# 27. 중첩 배열 요소 접근

공통 원본:

```js
let y = 음식[0]
let p = y[0]
let 스테이크 = 음식[0][2]
```

결과:

```text
y → 양식 전체
p → "파스타"
스테이크 → "스테이크"
```

이중 index:

```js
음식[0][2]
```

첫 index는 바깥 배열, 두 번째 index는 안쪽 배열입니다.

---

# 28. 1차원 배열 설명 오류

내 코드:

```text
1차원 배열은 아래와 같이 [][]두개로 안에있는 값에 접근
```

`음식`은 중첩 배열이므로 2차원 형태로 볼 수 있습니다.

정확한 표현:

```text
중첩 배열의 내부 요소에는 두 번의 index 접근으로 접근한다.
```

---

# 29. 음식 데이터 차이

강사님 중식:

```js
"탕슉"
```

내 코드:

```js
"탕수육"
```

강사님 일식:

```js
"오차즈께"
"스키야끼"
```

내 코드:

```js
"오차즈케"
"스키야키"
```

내 코드에서 일부 명칭 표기를 수정한 차이가 있습니다.

원본 차이로 기록하되 어느 표기가 수업 의도였는지 임의로 단정하지 않습니다.

---

# 30. 모든 음식 출력

공통 원본:

```js
for (let j = 0; j < 음식.length; j++) {
  for (
    let i = 0;
    i < 음식[j].length;
    i++
  ) {
    console.log(음식[j][i])
  }
}
```

바깥 반복:

```text
음식 분류 선택
```

안쪽 반복:

```text
선택한 분류의 각 메뉴 출력
```

---

# 31. 강사님의 단계별 주석 코드

강사님은 먼저 각 분류를 별도 반복하는 코드를 주석으로 남깁니다.

```js
for (let i = 0; i < 음식[0].length; i++) {
}
```

```js
for (let i = 0; i < 음식[1].length; i++) {
}
```

이 중복을 중첩 반복문으로 일반화합니다.

내 코드에는 이 단계별 주석이 없습니다.

---

# 32. 배열 메서드와 원본 변경

공통 원본은 다음 메서드를 다룹니다.

```text
push
unshift
pop
shift
reverse
sort
slice
indexOf
join
split
splice
```

이 중 일부는 원본 배열을 변경하고 일부는 변경하지 않습니다.

| 메서드 | 원본 변경 |
| --- | --- |
| `push()` | 변경 |
| `unshift()` | 변경 |
| `pop()` | 변경 |
| `shift()` | 변경 |
| `reverse()` | 변경 |
| `sort()` | 변경 |
| `splice()` | 변경 |
| `slice()` | 변경하지 않음 |
| `indexOf()` | 변경하지 않음 |
| `join()` | 변경하지 않음 |

---

# 33. Push

공통 원본:

```js
arr.push(5)
```

배열 마지막에 값을 추가합니다.

```js
const length = arr.push(5)
```

반환값은 추가된 요소가 아니라 변경 후 배열 길이입니다.

---

# 34. Unshift

공통 원본:

```js
arr.unshift(0)
```

배열 처음에 값을 추가합니다.

반환값은 변경 후 배열 길이입니다.

앞쪽 요소들의 index가 모두 이동하므로 큰 배열에서 비용이 커질 수 있습니다.

---

# 35. Pop

공통 원본:

```js
let pop = arr.pop()
```

배열 마지막 요소를 제거하고 제거한 값을 반환합니다.

```text
원본 배열 변경
반환값 → 제거된 마지막 요소
```

빈 배열에서 호출하면 undefined를 반환합니다.

---

# 36. Shift

공통 원본:

```js
let shift = arr.shift()
```

배열 첫 요소를 제거하고 제거한 값을 반환합니다.

앞쪽 제거로 나머지 요소의 index가 이동합니다.

---

# 37. Queue와 Stack 설명 검토

내 코드:

```text
큐: 선입선출
스택: 후입선출
선입: unshift, 선출: shift
후압: push, 선출: pop
```

큐를 배열로 구현할 때 일반적으로 다음 조합이 자연스럽습니다.

```text
enqueue → push()
dequeue → shift()
```

`unshift()`와 `shift()`를 함께 쓰면 둘 다 앞쪽에서 추가·제거하므로 FIFO 큐 설명으로 적절하지 않습니다.

스택:

```text
push()
pop()
```

은 LIFO 동작입니다.

`후압`은 일반적으로 사용하는 표준 용어가 아닙니다.

---

# 38. Reverse

공통 원본:

```js
const reverse = arr.reverse()
```

배열 순서를 뒤집습니다.

중요:

```text
arr 자체가 변경됨
reverse도 같은 배열 객체를 참조
```

```js
console.log(arr === reverse)
```

결과는 true입니다.

원본을 유지하려면:

```js
const reversed =
  [...arr].reverse()
```

---

# 39. Sort 기본

공통 원본:

```js
arr = [7, 4, 2, 3, 6, 5]

const sort = arr.sort()
```

한 자리 숫자에서는 오름차순처럼 보입니다.

하지만 기본 `sort()`는 값을 문자열로 변환한 뒤 정렬합니다.

---

# 40. 숫자 Sort 문제

공통 원본:

```js
arr = [10, 5, 3]

console.log(arr.sort())
```

결과:

```js
[10, 3, 5]
```

문자열 비교:

```text
"10"
"3"
"5"
```

첫 문자 기준으로 `"10"`이 `"3"`보다 앞에 옵니다.

---

# 41. 숫자 정렬 비교 함수

오름차순:

```js
arr.sort((a, b) => a - b)
```

내림차순:

```js
arr.sort((a, b) => b - a)
```

원본의 `sort().reverse()`도 일부 숫자에서 내림차순처럼 보이지만 기본 sort가 문자열 정렬이라는 문제를 그대로 가집니다.

---

# 42. 내림차순 설명 오류

내 코드:

```text
내림차순은 함수로는 없어
정렬한 것을 reverse로
```

JavaScript에는 별도의 `descendingSort()` 메서드는 없지만 비교 함수를 사용해 직접 내림차순 정렬할 수 있습니다.

```js
arr.sort((a, b) => b - a)
```

따라서 reverse만이 유일한 방법은 아닙니다.

---

# 43. Chaining

공통 원본:

```js
arr.sort().reverse()
```

한 메서드의 반환값에 이어서 다른 메서드를 호출합니다.

이를 method chaining이라고 합니다.

주의:

`sort()`와 `reverse()` 모두 같은 원본 배열을 변경합니다.

---

# 44. Sort 변수 참조

공통 코드:

```js
const sort = arr.sort()

arr.sort().reverse()

console.log(sort)
```

`sort`와 `arr`는 같은 배열을 참조합니다.

따라서 이후 `arr.reverse()`가 실행되면 `sort`로 출력한 결과도 뒤집힌 상태입니다.

새로운 독립 배열이 아닙니다.

---

# 45. Slice 기본

공통 원본:

```js
let a = arr.slice(2, 5)
```

범위:

```text
시작 index 포함
끝 index 제외
```

즉 index 2, 3, 4를 복사합니다.

원본 배열은 변경하지 않습니다.

---

# 46. Slice 범위 초과

공통 원본:

```js
a = arr.slice(2, 50)
```

끝 index가 배열 길이를 넘어가도 오류가 발생하지 않습니다.

index 2부터 배열 끝까지 복사합니다.

---

# 47. Slice 인수 하나

공통 원본:

```js
a = arr.slice(2)
```

index 2부터 끝까지 복사합니다.

얕은 복사 용도로도 사용할 수 있습니다.

```js
const copy = arr.slice()
```

---

# 48. 음수 Slice

공통 원본:

```js
hour = hour.slice(-2)
```

음수 index는 뒤에서부터 계산합니다.

```js
"012".slice(-2)
// "12"
```

시간과 분을 두 자리 문자열로 만들 때 활용할 수 있습니다.

---

# 49. Hour 값 차이

강사님:

```js
let hour = 2
hour = "0" + 2
```

결과:

```text
02
```

내 코드:

```js
let hour = 12
hour = "0" + 12
hour = hour.slice(-2)
```

결과:

```text
12
```

내 코드는 이미 두 자리인 값에서도 마지막 두 자리만 남는 것을 확인합니다.

---

# 50. PadStart 개선

현대적인 문자열 채우기:

```js
String(hour).padStart(2, "0")
```

예:

```text
2 → "02"
12 → "12"
```

원본은 `slice(-2)` 방식을 학습합니다.

---

# 51. IndexOf

공통 원본:

```js
let b = arr.indexOf(4)
```

값 4가 처음 등장하는 index를 반환합니다.

없으면:

```text
-1
```

---

# 52. IndexOf 두 번째 인수

내 코드:

```js
arr.indexOf(4, 0)
```

두 번째 인수는 검색 시작 index입니다.

```js
arr.indexOf(value, fromIndex)
```

강사님은 두 번째 인수를 생략합니다.

현재 배열에서는 결과가 같습니다.

---

# 53. 이메일 At 위치 찾기

공통 원본:

```js
let c = "todair@naver.com"

b = c.indexOf("@")
console.log(c.slice(0, b))
```

`@` 앞부분을 추출합니다.

결과:

```text
todair
```

`indexOf()`가 -1이면 `slice(0, -1)`이 되어 마지막 문자를 제외한 문자열이 나올 수 있으므로 유효성 검사가 필요합니다.

---

# 54. 여러 문자 IndexOf

내 코드 설명:

```text
여러 글자를 쓰면 그 값의 첫 번째 index가 나옴
```

맞습니다.

```js
"abcabc".indexOf("bc")
// 1
```

찾지 못하면:

```text
-1
```

---

# 55. Join

공통 원본:

```js
arr = ["a", "b", "c"]

b = arr.join()
```

기본 구분자는 쉼표입니다.

결과:

```text
a,b,c
```

원본 배열은 변경되지 않습니다.

---

# 56. 빈 문자열 연결과 Join

공통 원본:

```js
console.log("" + arr)
```

배열이 문자열로 변환되면서 기본적으로 `join(",")`과 비슷한 결과가 나옵니다.

의도를 명확히 하려면 직접 `join()`을 사용합니다.

---

# 57. 사용자 지정 구분자

공통 원본:

```js
b = arr.join(";")
```

결과:

```text
a;b;c
```

구분자는 데이터 안에 등장할 가능성을 고려해야 합니다.

단순한 `join()` 문자열은 복잡한 데이터 전송 포맷으로는 한계가 있습니다.

실무 데이터 교환에는 JSON이 흔히 사용됩니다.

---

# 58. 내 코드 네트워크 설명 검토

내 코드:

```text
네트워크 등 전송할 때 join으로 전환
보통 ; 많이 사용
네이버 등 &로 검색해도 %로 바뀜
```

이 설명은 일반화하기 어렵습니다.

- 네트워크 데이터 전송 형식은 JSON, form encoding 등 다양합니다.
- 세미콜론이 일반적인 표준 구분자라고 단정하기 어렵습니다.
- URL에서 특수 문자가 percent encoding되는 규칙은 문자와 위치에 따라 다릅니다.

이 단원에서는 배열을 문자열로 결합하는 기능에 집중합니다.

---

# 59. Split

공통 원본:

```js
let d = b.split(";")
```

문자열을 구분자를 기준으로 나눠 배열로 만듭니다.

```text
"a;b;c"
→ ["a", "b", "c"]
```

구분자 자체는 결과 배열에 포함되지 않습니다.

---

# 60. Join과 Split 비교

| 메서드 | 입력 | 결과 |
| --- | --- | --- |
| `join()` | 배열 | 문자열 |
| `split()` | 문자열 | 배열 |

예:

```js
const text =
  ["a", "b", "c"].join(";")

const values =
  text.split(";")
```

---

# 61. URL Query String 분석

공통 원본은 검색 URL에서 `query`의 값 `1234`를 추출합니다.

```js
const url =
  "https://search.naver.com/..." +
  "?where=nexearch&..." +
  "&query=1234&ackey=..."
```

단계:

```text
? 기준 분리
& 기준 분리
= 기준 분리
name이 query인지 확인
value 출력
```

---

# 62. URL 분리 1단계

```js
let temp = url.split("?")
```

결과 개념:

```js
[
  "https://search.naver.com/search.naver",
  "where=nexearch&...&query=1234&..."
]
```

두 번째 요소가 query string입니다.

---

# 63. URL 분리 2단계

```js
let qs = temp[1]

qs = qs.split("&")
```

각 항목:

```text
where=nexearch
sm=top_hty
fbm=0
ie=utf8
query=1234
ackey=...
```

---

# 64. URL 분리 3단계

```js
for (let i = 0; i < qs.length; i++) {
  let q = qs[i].split("=")
  let name = q[0]
  let value = q[1]

  if (name == "query") {
    console.log(value)
  }
}
```

결과:

```text
1234
```

---

# 65. 강사님과 내 URL 차이

두 URL의 `ackey` 값이 다릅니다.

강사님:

```text
lm2glmr8
```

내 코드 첫 URL:

```text
4lm5o7gi
```

`query=1234` 추출 결과에는 영향이 없습니다.

내 코드에는 같은 문제를 다시 푼 `url_try` 풀이가 추가되어 있습니다.

---

# 66. URL API 개선

브라우저에서는 다음 API를 사용할 수 있습니다.

```js
const parsed = new URL(url)

console.log(
  parsed.searchParams.get("query")
)
```

결과:

```text
1234
```

원본은 `split()`과 반복문 학습이 목적이므로 직접 분해합니다.

---

# 67. URL Encoding 주의

실제 query 값은 percent encoding될 수 있습니다.

```text
query=%EC%9E%90%EB%B0%94
```

직접 split만 하면 인코딩된 문자열이 남습니다.

`URLSearchParams`는 쿼리 파싱과 디코딩을 더 안전하게 처리합니다.

---

# 68. 내 코드 이메일 분석

내 코드에만 있습니다.

```js
const email = "test@naver.com"

let temp1 = email.split("@")
let temp2 = temp1[1]
let temp3 = temp2.split(".")

console.log(temp3[0])
```

결과:

```text
naver
```

이메일의 도메인 부분에서 첫 label을 추출합니다.

---

# 69. 이메일 분해 주의

단순한 이메일:

```text
test@naver.com
```

에서는 동작합니다.

그러나 다음처럼 복잡할 수 있습니다.

```text
user@mail.example.co.kr
```

`temp3[0]`은 `mail`만 반환합니다.

이메일 유효성 검증 전체를 단순 split만으로 해결할 수는 없습니다.

---

# 70. 문제 1: 1~10 배열 생성

강사님 원본은 문제만 제시합니다.

내 코드:

```js
let q1_array = []

for (let i = 1; i < 11; i++) {
  q1_array.push(i)
}
```

결과:

```js
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

# 71. 문제 1 개선

조건을 더 직접 표현할 수 있습니다.

```js
for (let i = 1; i <= 10; i++) {
  q1Array.push(i)
}
```

또는 확장 학습:

```js
const values =
  Array.from(
    { length: 10 },
    (_, index) => index + 1
  )
```

---

# 72. 문제 2-1: 홀수 개수

내 코드:

```js
let q2_array = [3, 4, 7, 5, 1, 6]
let q2_num = ""
let count = 0

for (
  let i = 0;
  i < q2_array.length;
  i++
) {
  if (q2_array[i] % 2 !== 0) {
    q2_num += q2_array[i] + " "
    count++
  }
}
```

결과:

```text
홀수: 3, 7, 5, 1
개수: 4
```

---

# 73. 문제 2-2: 4보다 큰 수

내 코드:

```js
if (q2_array[i] > 4) {
  q2_num += String(q2_array[i]) + " "
  count++
}
```

결과:

```text
7, 5, 6
개수 3
```

---

# 74. 문제 2-2 출력 Label 오류

내 코드 출력:

```text
홀수의 개수 : 3개, 4보다 큰 수 : 7 5 6
```

첫 label은 잘못되었습니다.

정확한 문구:

```text
4보다 큰 수의 개수 : 3개
```

문제 2-1의 출력 문구를 복사한 오류입니다.

---

# 75. Filter 확장 풀이

```js
const values = [3, 4, 7, 5, 1, 6]

const odds =
  values.filter(value => value % 2 !== 0)

const overFour =
  values.filter(value => value > 4)
```

현재 원본은 기본 반복문을 연습하는 단계이므로 for문 풀이가 적절합니다.

---

# 76. 문제 3: 미완주자 등번호

강사님 문제:

```text
참가자 1~5
완주 목록 [2,4,5,1]
미완주자는?
```

정답:

```text
3
```

내 코드에는 여러 시도와 최종 중첩 반복 풀이가 있습니다.

---

# 77. 첫 번째 문제 3 시도 오류

내 코드:

```js
let check_num = q3_human.join("")
let check_num2 =
  check_num.split("3").join("")
```

`3`을 직접 알고 제거합니다.

이는 정답을 미리 알고 사용하는 방식이므로 일반적인 문제 풀이가 아닙니다.

또한 `check_num2`는 이후 실제 결과 판정에 사용되지 않습니다.

---

# 78. 첫 번째 중첩 반복 오류

내 코드:

```js
for (let i = 0; i < q3_result.length; i++) {
  for (let j = 0; j < check_num.length; j++) {
    if (q3_result[i] == check_num[j]) {
      console.log("완주자")
    }

    break
  }
}
```

안쪽 반복의 `break`가 첫 비교 후 항상 실행됩니다.

따라서 각 완주자를 `check_num[0]`과만 비교합니다.

전체 참가자 비교가 되지 않습니다.

---

# 79. 최종 문제 3 풀이

내 코드:

```js
for (let j = 0; j < entry.length; j++) {
  let result_check = false

  for (
    let i = 0;
    i < finisher.length;
    i++
  ) {
    if (entry[j] == finisher[i]) {
      result_check = true
      break
    }
  }

  if (result_check == true) {
    result_success += entry[j] + " "
  } else {
    result_fail += entry[j] + " "
  }
}
```

이 구조는 각 참가자가 완주 목록에 존재하는지 검사합니다.

결과:

```text
완주자: 1 2 4 5
미완주자: 3
```

---

# 80. Result 배열 선언과 문자열 누적

내 코드:

```js
let result_success = []
let result_fail = []
```

이후:

```js
result_success += entry[j] + " "
```

`+=`를 사용하면 배열이 문자열로 변환됩니다.

최종 자료형은 문자열이 됩니다.

배열을 유지하려면:

```js
result_success.push(entry[j])
result_fail.push(entry[j])
```

를 사용해야 합니다.

---

# 81. 불필요한 Else If

내 코드:

```js
if (entry[j] == finisher[i]) {
  result_check = true
  break
} else if (entry[j] !== finisher[i]) {
  result_check = false
}
```

`result_check`는 반복 시작 시 false입니다.

불일치할 때마다 다시 false를 대입할 필요가 없습니다.

```js
if (entry[j] === finisher[i]) {
  resultCheck = true
  break
}
```

로 충분합니다.

---

# 82. Includes 개선

```js
const unfinished =
  entry.filter(
    number => !finisher.includes(number)
  )
```

결과:

```js
[3]
```

원본은 중첩 반복과 flag를 연습하는 풀이입니다.

---

# 83. 문제 3-1: 이름 참가자

강사님 문제:

```js
참가 목록:
["나미", "우솝", "조로", "루피", "상디"]

완주 목록:
["우솝", "나미", "상디", "조로"]
```

미완주자:

```text
루피
```

내 코드의 완주 목록은 같은 네 이름을 사용하지만 순서가 원본 예시와 다릅니다.

---

# 84. 내 문제 3-1 풀이 오류

내 코드:

```js
let rand =
  parseInt(Math.random() * 4)

for (
  let i = 0;
  i < q4_human.length;
  i++
) {
  for (
    let j = 0;
    j < q4_result.length;
    j++
  ) {
    if (q4_human[i] == q4_result[j]) {
      sum += q4_result[rand]
    }
  }
}
```

일치한 참가자를 누적하는 대신 랜덤한 완주자 이름을 더합니다.

미완주자 `"루피"`를 찾지 못합니다.

이 풀이는 잘못되었습니다.

---

# 85. 이름 미완주자 개선

```js
const participants = [
  "나미", "우솝", "조로", "루피", "상디"
]

const finishers = [
  "우솝", "나미", "상디", "조로"
]

for (const person of participants) {
  if (!finishers.includes(person)) {
    console.log(person)
  }
}
```

결과:

```text
루피
```

---

# 86. 문제 4: 소극장 예약 시스템

강사님은 요구사항만 제시합니다.

내 코드는 while 기반 풀이를 시작했지만 전체가 주석 처리되어 있고 미완성입니다.

```text
1. 예약
2. 모든 좌석 현황
3. 잔여 좌석
x. 종료
```

---

# 87. 내 좌석 예약 코드의 현재 상태

작성된 기능:

- 메뉴 prompt
- 종료 조건 일부
- 좌석 번호 prompt
- 1~10 범위 검사
- 배열에 예약값 push

미완성 기능:

- 이미 예약된 좌석 확인
- 모든 좌석 현황 출력
- 잔여 좌석 출력
- 메뉴 2·3 분기
- 중괄호 구조 완성
- 숫자 입력 검증
- 취소 처리 세분화

---

# 88. 좌석 중복 문제

현재 코드:

```js
q4_seat.push(value)
```

기존 예약 여부를 확인하지 않습니다.

개선:

```js
if (reservedSeats.includes(seat)) {
  console.log("이미 예약된 자리입니다.")
} else {
  reservedSeats.push(seat)
}
```

prompt 값이 문자열이므로 숫자로 변환하거나 문자열 기준을 일관되게 유지해야 합니다.

---

# 89. 좌석 상태 배열 설계

10개 자리를 Boolean 배열로 관리할 수 있습니다.

```js
const seats =
  Array(10).fill(false)
```

예약:

```js
seats[seatNumber - 1] = true
```

조회:

```text
false → 예약 가능
true → 예약 완료
```

---

# 90. 문제 5: 로또 중복 제거 첫 풀이

내 코드:

```js
for (let i = 0; i < 6; i++) {
  q5_lotto.push(random)

  for (let k = 1; k < 6; k++) {
    for (
      let j = 0;
      j < q5_lotto.length;
      j++
    ) {
      if (
        q5_lotto[j] ==
        q5_lotto[j + k]
      ) {
        q5_lotto.pop()
        q5_lotto.push(random)
      }
    }
  }
}
```

중복을 찾으면 마지막 값을 제거하고 새 값을 추가합니다.

하지만 새로 추가한 값도 다시 중복일 수 있으며, 교체 후 전체 검사를 확실하게 반복하지 않습니다.

중복 없는 6개를 보장하기 어렵습니다.

---

# 91. 문제 5-1 풀이 오류

내 코드:

```js
q6_number = random

if (q6_lotto[i] !== q6_number) {
  q6_lotto.push(q6_number)
} else {
  i--
}
```

새 번호를 기존 전체 배열과 비교하지 않습니다.

`q6_lotto[i]`는 현재 추가 전 index라 대부분 undefined입니다.

```text
undefined !== 생성된 숫자
→ true
```

따라서 거의 항상 push되어 중복을 막지 못합니다.

---

# 92. 문제 7 로또 풀이

내 코드의 세 번째 로또 풀이:

```js
let q7_check = false

for (
  let j = 0;
  j < q7_lotto.length;
  j++
) {
  if (q7_lotto[j] === q7_number) {
    q7_check = true
    break
  }
}

if (!q7_check) {
  q7_lotto.push(q7_number)
} else {
  i--
}
```

기존 모든 번호를 검사하므로 앞의 두 풀이보다 올바른 구조입니다.

중복이면 반복 index를 되돌려 다시 생성합니다.

---

# 93. 로또 Sort 오류

내 코드:

```js
q7_lotto.sort()
```

숫자 비교 함수를 전달하지 않아 문자열 순서로 정렬됩니다.

예:

```js
[3, 11, 20]
```

기본 sort 결과가 숫자 오름차순과 다를 수 있습니다.

개선:

```js
q7_lotto.sort((a, b) => a - b)
```

---

# 94. While 기반 로또 개선

```js
const lotto = []

while (lotto.length < 6) {
  const number =
    Math.floor(Math.random() * 45) + 1

  if (!lotto.includes(number)) {
    lotto.push(number)
  }
}

lotto.sort((a, b) => a - b)
```

배열 길이가 6이 될 때까지 반복합니다.

---

# 95. Set 확장 풀이

```js
const lotto = new Set()

while (lotto.size < 6) {
  lotto.add(
    Math.floor(Math.random() * 45) + 1
  )
}

const result =
  [...lotto].sort((a, b) => a - b)
```

`Set`은 중복 값을 저장하지 않습니다.

원본 범위를 넘어서는 확장 학습입니다.

---

# 96. 숫자 야구 게임

강사님과 내 코드 모두 숫자 야구 문제 설명을 포함합니다.

```text
스트라이크:
숫자와 위치가 모두 일치

볼:
숫자는 존재하지만 위치가 다름

아웃:
일치하는 숫자가 없음
```

강사님은 문제 설명 뒤 `splice()` 예제를 작성합니다.

내 코드는 구현 계획 주석까지만 있고 실제 게임 코드는 없습니다.

---

# 97. Splice

강사님 원본:

```js
arr = [1, 2, 3, 4, 5]

arr.splice(2, 1)
```

index 2부터 1개 요소를 제거합니다.

결과:

```js
arr
// [1, 2, 4, 5]
```

반환값:

```js
[3]
```

---

# 98. Slice와 Splice 비교

| 구분 | `slice()` | `splice()` |
| --- | --- | --- |
| 목적 | 범위 복사 | 삭제·추가·교체 |
| 원본 변경 | 안 함 | 변경함 |
| 두 번째 인수 | 끝 index | 삭제 개수 |
| 반환값 | 복사된 새 배열 | 삭제된 요소 배열 |

---

# 99. Splice 요소 추가

```js
const values = [1, 2, 5]

values.splice(2, 0, 3, 4)
```

결과:

```js
[1, 2, 3, 4, 5]
```

두 번째 인수 0은 삭제하지 않는다는 뜻입니다.

---

# 100. Splice 교체

```js
const values = [1, 2, 9, 4]

values.splice(2, 1, 3)
```

결과:

```js
[1, 2, 3, 4]
```

index 2에서 1개를 삭제하고 3을 삽입합니다.

---

# 101. 원본의 전체 실행 흐름

두 파일 모두 많은 코드가 실제 실행 상태입니다.

브라우저에서 열면 다음이 연속으로 출력됩니다.

- 배열 자료형
- 배열 요소 변경
- 희소 배열
- 전체 배열 순회
- 음식 목록 전체
- 배열 메서드 실행 결과
- URL 쿼리 추출
- 내 코드의 이메일과 추가 URL 풀이
- 내 코드의 문제 풀이 결과
- 로또 번호

특히 내 파일은 실행 코드가 매우 길어 Console 출력량이 많습니다.

---

# 102. My Code 분석

## 102.1 장점

- 배열과 index 개념을 상세히 주석으로 정리했다.
- const 배열 요소 변경과 배열 재할당 차이를 설명했다.
- 배열 출력에서 문자열 연결과 쉼표 전달 차이를 설명했다.
- 존재하지 않는 index와 선언되지 않은 변수 차이를 기록했다.
- 배열 length를 반복문과 연결해 설명했다.
- 중첩 배열의 모든 음식을 실제로 출력했다.
- `push()`, `unshift()`, `pop()`, `shift()`의 역할과 반환값을 상세히 설명했다.
- `reverse()`, `sort()`, `slice()`, `indexOf()`, `join()`, `split()` 설명을 확장했다.
- 음수 slice로 두 자리 문자열을 만드는 예제를 작성했다.
- URL 쿼리스트링 풀이를 한 번 더 직접 작성했다.
- 이메일에서 도메인 이름을 추출하는 실습을 추가했다.
- 문제 1과 문제 2를 완성했다.
- 등번호 미완주자 문제에서 중첩 반복과 flag 풀이를 완성했다.
- 소극장 예약 시스템 구현을 시작했다.
- 로또 중복 제거를 세 가지 방식으로 시도했다.
- 마지막 로또 풀이에서는 전체 배열을 검사해 중복을 방지한다.
- 숫자 야구 구현 단계를 주석으로 계획했다.

## 102.2 개선점

- `arr3[0]` label로 배열 전체를 출력하는 문구 오류가 있다.
- `arr3[] 자체가 식별자`라는 설명은 잘못이다.
- stack·heap과 자료 크기 설명이 지나치게 단순하거나 부정확하다.
- 1차원 배열이라고 하면서 이중 index 접근을 설명한다.
- Queue 설명에서 `unshift()`와 `shift()`를 함께 제시해 FIFO 설명이 맞지 않는다.
- `내림차순 함수는 없다`는 설명은 비교 함수 정렬을 누락한다.
- 기본 `sort()`가 문자열 정렬이라는 설명은 있지만 이후 로또에도 비교 함수를 사용하지 않는다.
- 네트워크 전송과 세미콜론 구분자 설명을 일반화하기 어렵다.
- 문제 2-2 출력에 `홀수의 개수`라는 잘못된 label이 있다.
- 문제 3의 첫 풀이에서 정답 3을 미리 제거한다.
- 첫 중첩 반복에서 break가 항상 실행되어 첫 요소만 비교한다.
- 완주자·미완주자 결과 변수를 배열로 선언한 뒤 문자열로 변경한다.
- 문제 3-1 이름 풀이가 랜덤 완주자를 누적해 정답을 찾지 못한다.
- 소극장 예약 프로그램이 미완성이다.
- 첫 번째와 두 번째 로또 풀이가 중복을 확실히 방지하지 못한다.
- 마지막 로또 정렬도 기본 sort라 숫자 순서가 잘못될 수 있다.
- 숫자 난수에 `parseInt()`를 사용한다.
- 숫자 야구는 계획만 있고 구현이 없다.
- 많은 실험과 문제 풀이가 한 파일에서 모두 실행되어 학습 흐름과 Console 확인이 복잡하다.

---

# 103. Teacher Code 분석

## 103.1 장점

- 배열 리터럴과 `new Array()` 선언을 비교한다.
- 배열에 여러 자료형을 저장하는 예제를 보여 준다.
- let 배열의 요소 변경과 전체 재할당을 모두 실행한다.
- 문자열 index 접근을 보여 준다.
- 없는 배열 index가 undefined임을 확인한다.
- 먼 index와 문자열 속성을 배열에 추가하는 실험을 한다.
- 고정 길이 반복과 length 기반 반복을 비교한다.
- 후위 증가를 index에 사용하는 실험이 있다.
- 중첩 배열과 중첩 반복문으로 음식 전체를 출력한다.
- 주요 배열 변경 메서드를 순서대로 실습한다.
- slice, indexOf, join, split을 문자열 처리와 연결한다.
- URL 쿼리스트링에서 query 값을 추출한다.
- 문제 1~5와 숫자 야구 문제를 제시한다.
- `splice()` 기본 삭제 예제를 제공한다.

## 103.2 개선점

- `typeof`가 object라는 사실만 보여 주고 `Array.isArray()`는 설명하지 않는다.
- 희소 배열과 문자열 속성 추가의 위험을 설명하지 않는다.
- `sort()`의 문자열 정렬 문제 해결법을 제공하지 않는다.
- `reverse()`와 `sort()`가 원본을 변경한다는 설명이 부족하다.
- `sort` 변수와 arr가 같은 배열을 참조한다는 설명이 없다.
- Queue와 Stack 개념을 직접 연결하지 않는다.
- URL 파싱에서 name 비교에 느슨한 동등 연산자를 사용한다.
- URL 구조가 잘못된 경우의 검증이 없다.
- 문제 1~5의 정답이 없다.
- 좌석 예약, 로또, 숫자 야구의 구현이 없다.
- `splice()`의 반환값과 추가·교체 기능 설명이 없다.
- 음식 이름에 `탕슉`, `오차즈께`, `스키야끼` 표기가 사용된다.
- 문서 언어와 제목이 콘텐츠에 맞지 않는다.

---

# 104. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| `arr3` 선언 | `const` | `let` |
| `arr3` 전체 재할당 | 주석 처리 | 실제 실행 |
| 배열 출력 label | 일부 잘못 `arr3[0]` | 올바른 `arr3` |
| 배열 개념 주석 | 매우 상세, 일부 부정확 | 핵심만 |
| stack·heap·GC 설명 | 있음 | 없음 |
| 후위 index 증가 실험 | 없음 | 있음 |
| 음식 이름 | 일부 표기 수정 | 수업 원본 표기 |
| 단계별 음식 반복 주석 | 없음 | 있음 |
| Queue·Stack 설명 | 있음, 일부 오류 | 없음 |
| Hour 예제 | 12 | 2 |
| IndexOf 두 번째 인수 | 0 명시 | 생략 |
| URL 풀이 | 두 번 | 한 번 |
| 이메일 분석 | 있음 | 없음 |
| 문제 1·2 풀이 | 있음 | 없음 |
| 등번호 미완주자 풀이 | 여러 시도와 최종 풀이 | 문제만 |
| 이름 미완주자 풀이 | 있음, 잘못됨 | 문제만 |
| 좌석 예약 | 미완성 구현 | 문제만 |
| 로또 | 세 가지 풀이 | 문제만 |
| 숫자 야구 | 계획 주석 | 문제 설명 + splice |
| `splice()` 실행 | 없음 | 있음 |
| 파일 크기·실행량 | 매우 큼 | 상대적으로 간결 |

---

# 105. 공통 핵심 코드

```js
const arr1 = []
const arr2 = new Array()

let arr3 = [
  1, 2, "글씨", false, 3.14, arr1
]

console.log(typeof arr1)
console.log(arr3[0])

arr3[0] = 10

let arr = [0, 1, 2, 3, 4, 5]

for (
  let i = 0;
  i < arr.length;
  i++
) {
  console.log(arr[i])
}

arr.push(6)
arr.unshift(-1)

const last = arr.pop()
const first = arr.shift()

arr.reverse()
arr.sort()

const copied = arr.slice(2, 5)
const index = arr.indexOf(4)

const text = ["a", "b", "c"].join(";")
const values = text.split(";")
```

---

# 106. 배열 메서드 통합 개선 예제

```js
"use strict";

const numbers = [7, 4, 2, 3, 6, 5];

numbers.push(8);
numbers.unshift(1);

const last = numbers.pop();
const first = numbers.shift();

console.log("제거한 첫 값:", first);
console.log("제거한 마지막 값:", last);

const reversed = [...numbers].reverse();

const ascending =
  [...numbers].sort((a, b) => a - b);

const descending =
  [...numbers].sort((a, b) => b - a);

const section =
  numbers.slice(1, 4);

console.log("원본:", numbers);
console.log("뒤집기 복사:", reversed);
console.log("오름차순:", ascending);
console.log("내림차순:", descending);
console.log("일부 복사:", section);
```

---

# 107. URL Query 개선 예제

```js
const url =
  "https://search.naver.com/search.naver" +
  "?where=nexearch&query=1234";

const parsedUrl = new URL(url);

const query =
  parsedUrl.searchParams.get("query");

console.log(query);
```

원본의 split 기반 풀이:

```js
const queryString =
  url.split("?")[1];

const pairs =
  queryString.split("&");

for (const pair of pairs) {
  const [name, value] =
    pair.split("=");

  if (name === "query") {
    console.log(value);
  }
}
```

---

# 108. 미완주자 통합 개선 예제

```js
const participants =
  ["나미", "우솝", "조로", "루피", "상디"];

const finishers =
  ["우솝", "나미", "상디", "조로"];

const unfinished = [];

for (const participant of participants) {
  let completed = false;

  for (const finisher of finishers) {
    if (participant === finisher) {
      completed = true;
      break;
    }
  }

  if (!completed) {
    unfinished.push(participant);
  }
}

console.log(unfinished);
```

---

# 109. 좌석 예약 개선 예제

```js
const seats =
  Array(10).fill(false);

while (true) {
  const menu = prompt(
    "1.예약 / 2.전체 현황 / " +
    "3.잔여 좌석 / x.종료"
  );

  if (menu === null || menu === "x") {
    break;
  }

  if (menu === "1") {
    const input =
      prompt("좌석 번호 1~10");

    if (
      input === null ||
      input.trim() === ""
    ) {
      continue;
    }

    const seat = Number(input);

    if (
      !Number.isInteger(seat) ||
      seat < 1 ||
      seat > 10
    ) {
      console.log("1~10 정수를 입력하세요.");
      continue;
    }

    const index = seat - 1;

    if (seats[index]) {
      console.log("이미 예약된 자리입니다.");
    } else {
      seats[index] = true;
      console.log(`${seat}번 자리 예약 완료`);
    }
  } else if (menu === "2") {
    console.log(
      seats.map(
        (reserved, index) =>
          `${index + 1}:${reserved ? "예약" : "가능"}`
      )
    );
  } else if (menu === "3") {
    const remaining =
      seats.filter(reserved => !reserved).length;

    console.log(`잔여 좌석: ${remaining}개`);
  } else {
    console.log("메뉴를 정확히 입력하세요.");
  }
}
```

---

# 110. 자주 하는 실수

## 110.1 배열 Index를 1부터 시작

첫 요소는 index 0입니다.

## 110.2 Const 배열은 요소도 변경 불가라고 생각

배열 자체 재할당은 불가하지만 요소 변경은 가능합니다.

## 110.3 Typeof 배열 결과를 `"array"`로 예상

결과는 `"object"`입니다. `Array.isArray()`를 사용합니다.

## 110.4 존재하지 않는 Index를 오류로 예상

대부분 undefined가 반환됩니다.

## 110.5 먼 Index에 값을 넣어도 중간이 자동 채워진다고 생각

빈 슬롯이 생깁니다.

## 110.6 문자열 Key를 일반 배열 요소처럼 사용

length와 일반 index 순회에 포함되지 않습니다.

## 110.7 Reverse와 Sort가 원본을 유지한다고 생각

둘 다 원본 배열을 변경합니다.

## 110.8 숫자 배열에 기본 Sort 사용

문자열 순서로 정렬됩니다.

## 110.9 Slice와 Splice 혼동

slice는 복사, splice는 원본 삭제·추가·교체입니다.

## 110.10 IndexOf 미발견 결과를 False로만 검사

미발견 결과는 -1입니다.

## 110.11 Join과 Split 방향 혼동

join은 배열에서 문자열, split은 문자열에서 배열입니다.

## 110.12 배열로 선언한 결과에 `+=` 사용

배열이 문자열로 변환될 수 있습니다.

## 110.13 로또에서 새 숫자를 한 Index와만 비교

기존 모든 번호와 비교해야 합니다.

## 110.14 기본 Sort로 로또 정렬

10, 2, 3처럼 잘못된 숫자 순서가 될 수 있습니다.

---

# 111. 면접·복습 포인트

## Q1. 배열 Index는 몇부터 시작하나요?

0부터 시작합니다.

## Q2. `typeof []`의 결과는 무엇인가요?

`"object"`입니다. 배열 여부는 `Array.isArray()`로 확인할 수 있습니다.

## Q3. Const 배열의 요소를 변경할 수 있나요?

가능합니다. const는 배열 변수에 다른 배열을 재할당하는 것을 막습니다.

## Q4. 존재하지 않는 배열 Index에 접근하면 어떻게 되나요?

일반적으로 undefined가 반환됩니다.

## Q5. Push와 Pop의 반환값은 무엇인가요?

push는 변경 후 배열 길이, pop은 제거한 마지막 요소를 반환합니다.

## Q6. Reverse와 Sort의 공통 주의점은 무엇인가요?

원본 배열을 직접 변경합니다.

## Q7. 숫자 오름차순 정렬은 어떻게 하나요?

`array.sort((a, b) => a - b)`를 사용합니다.

## Q8. Slice와 Splice의 차이는 무엇인가요?

slice는 원본을 변경하지 않고 일부를 복사하며, splice는 원본에서 요소를 삭제·추가·교체합니다.

## Q9. IndexOf가 값을 찾지 못하면 무엇을 반환하나요?

-1을 반환합니다.

## Q10. Join과 Split은 각각 무엇을 반환하나요?

join은 문자열, split은 배열을 반환합니다.

## Q11. 내 이름 미완주자 풀이가 틀린 이유는 무엇인가요?

일치한 참가자를 결과에 넣지 않고 랜덤한 완주자 이름을 반복 누적하기 때문에 미완주자를 찾지 못합니다.

## Q12. 내 두 번째 로또 풀이가 중복을 막지 못하는 이유는 무엇인가요?

새 번호를 기존 전체 배열이 아니라 아직 값이 없는 현재 index와만 비교하기 때문입니다.

---

# Problems

## 문제 1. 배열 선언

숫자 10, 20, 30을 가진 배열을 리터럴 방식으로 선언하세요.

## 문제 2. Index 접근

문제 1 배열의 두 번째 값을 출력하세요.

## 문제 3. 요소 변경

문제 1 배열의 첫 번째 값을 100으로 변경하세요.

## 문제 4. Const 배열

const 배열의 요소 변경과 배열 전체 재할당 가능 여부를 설명하세요.

## 문제 5. 배열 판별

빈 배열이 배열인지 `Array.isArray()`로 확인하세요.

## 문제 6. 없는 Index

배열 `[1, 2, 3]`의 index 10을 출력하고 결과를 설명하세요.

## 문제 7. Length 순회

배열 `["a", "b", "c"]`의 모든 값을 length 기반 for문으로 출력하세요.

## 문제 8. 중첩 배열

배열 `[[1, 2], [3, 4]]`에서 숫자 4를 출력하세요.

## 문제 9. Push와 Unshift

배열 `[2, 3]`의 앞에 1, 뒤에 4를 추가하세요.

## 문제 10. Pop과 Shift

배열 `[1, 2, 3, 4]`의 첫 값과 마지막 값을 제거하고 반환값을 출력하세요.

## 문제 11. Reverse 복사

원본 `[1, 2, 3]`을 유지하면서 뒤집힌 새 배열을 만드세요.

## 문제 12. 숫자 정렬

배열 `[10, 5, 3]`을 숫자 오름차순으로 정렬하세요.

## 문제 13. Slice

배열 `[0, 1, 2, 3, 4, 5]`에서 index 2부터 4까지 복사하세요.

## 문제 14. Splice

배열 `[1, 2, 3, 4, 5]`에서 숫자 3을 제거하세요.

## 문제 15. IndexOf

문자열 `"test@naver.com"`에서 `@`의 index를 찾으세요.

## 문제 16. Join과 Split

배열 `["html", "css", "js"]`를 `;`로 연결한 뒤 다시 배열로 만드세요.

## 문제 17. Query String

문자열 `"page=2&query=javascript&sort=recent"`에서 query 값을 출력하세요.

## 문제 18. 홀수 개수

배열 `[3, 4, 7, 5, 1, 6]`의 홀수 목록과 개수를 구하세요.

## 문제 19. 미완주자

참가자 `[1, 2, 3, 4, 5]`, 완주자 `[2, 4, 5, 1]`에서 미완주자를 구하세요.

## 문제 20. 좌석 예약

10개 좌석 Boolean 배열에서 3번 좌석을 예약하고 중복 예약 여부를 검사하세요.

## 문제 21. 중복 없는 로또

1~45에서 중복 없는 숫자 6개를 배열에 저장하고 숫자 오름차순으로 정렬하세요.

## 문제 22. 종합 데이터 처리

다음 요구사항을 만족하세요.

- 문자열 `"10,3,5,20,3"`
- 쉼표 기준 배열 변환
- 모든 값을 Number로 변환
- 중복 제거
- 숫자 오름차순 정렬
- 첫 값과 마지막 값 출력
- 원본 문자열도 함께 출력

---

# Answers & Explanations

## 정답 1

```js
const numbers = [10, 20, 30]
```

## 정답 2

```js
console.log(numbers[1])
```

결과는 20입니다.

## 정답 3

```js
numbers[0] = 100

console.log(numbers)
```

## 정답 4

```js
const values = [1, 2, 3]

values[0] = 10
```

요소 변경은 가능합니다.

```js
values = [4, 5, 6]
```

배열 전체 재할당은 TypeError가 발생합니다.

## 정답 5

```js
const values = []

console.log(Array.isArray(values))
```

## 정답 6

```js
const values = [1, 2, 3]

console.log(values[10])
```

결과는 undefined입니다.

## 정답 7

```js
const values = ["a", "b", "c"]

for (
  let i = 0;
  i < values.length;
  i++
) {
  console.log(values[i])
}
```

## 정답 8

```js
const values = [
  [1, 2],
  [3, 4]
]

console.log(values[1][1])
```

## 정답 9

```js
const values = [2, 3]

values.unshift(1)
values.push(4)

console.log(values)
```

## 정답 10

```js
const values = [1, 2, 3, 4]

const first = values.shift()
const last = values.pop()

console.log(first)
console.log(last)
console.log(values)
```

## 정답 11

```js
const values = [1, 2, 3]

const reversed =
  [...values].reverse()

console.log(values)
console.log(reversed)
```

## 정답 12

```js
const values = [10, 5, 3]

values.sort((a, b) => a - b)

console.log(values)
```

## 정답 13

```js
const values = [0, 1, 2, 3, 4, 5]

const copied =
  values.slice(2, 5)

console.log(copied)
```

결과는 `[2, 3, 4]`입니다.

## 정답 14

```js
const values = [1, 2, 3, 4, 5]

const removed =
  values.splice(2, 1)

console.log(values)
console.log(removed)
```

## 정답 15

```js
const email = "test@naver.com"

console.log(email.indexOf("@"))
```

결과는 4입니다.

## 정답 16

```js
const values = ["html", "css", "js"]

const text =
  values.join(";")

const restored =
  text.split(";")

console.log(text)
console.log(restored)
```

## 정답 17

```js
const queryString =
  "page=2&query=javascript&sort=recent"

const pairs =
  queryString.split("&")

for (const pair of pairs) {
  const [name, value] =
    pair.split("=")

  if (name === "query") {
    console.log(value)
  }
}
```

## 정답 18

```js
const values = [3, 4, 7, 5, 1, 6]
const odds = []

for (const value of values) {
  if (value % 2 !== 0) {
    odds.push(value)
  }
}

console.log(odds)
console.log(odds.length)
```

## 정답 19

```js
const participants = [1, 2, 3, 4, 5]
const finishers = [2, 4, 5, 1]
const unfinished = []

for (const participant of participants) {
  if (!finishers.includes(participant)) {
    unfinished.push(participant)
  }
}

console.log(unfinished)
```

## 정답 20

```js
const seats =
  Array(10).fill(false)

const seatNumber = 3
const index = seatNumber - 1

if (seats[index]) {
  console.log("이미 예약된 자리입니다.")
} else {
  seats[index] = true
  console.log(`${seatNumber}번 예약 완료`)
}

if (seats[index]) {
  console.log("이미 예약된 자리입니다.")
}
```

## 정답 21

```js
const lotto = []

while (lotto.length < 6) {
  const number =
    Math.floor(Math.random() * 45) + 1

  if (!lotto.includes(number)) {
    lotto.push(number)
  }
}

lotto.sort((a, b) => a - b)

console.log(lotto)
```

## 정답 22

```js
const source = "10,3,5,20,3"

const numberTexts =
  source.split(",")

const numbers = []

for (const text of numberTexts) {
  const number = Number(text)

  if (!numbers.includes(number)) {
    numbers.push(number)
  }
}

numbers.sort((a, b) => a - b)

console.log("원본:", source)
console.log("결과:", numbers)
console.log("첫 값:", numbers[0])
console.log(
  "마지막 값:",
  numbers[numbers.length - 1]
)
```

결과:

```text
원본: 10,3,5,20,3
결과: [3, 5, 10, 20]
첫 값: 3
마지막 값: 20
```

---

# Final Checklist

## 배열 기본

- [ ] 배열 index가 0부터 시작함을 이해했다.
- [ ] 배열 리터럴과 new Array를 구분했다.
- [ ] 배열에 여러 값을 저장하고 index로 접근했다.
- [ ] typeof 배열이 object임을 확인했다.
- [ ] Array.isArray로 배열 여부를 검사했다.
- [ ] const 배열의 요소 변경과 재할당을 구분했다.
- [ ] 문자열 index 접근과 배열 index 접근을 구분했다.

## 배열 구조와 순회

- [ ] 없는 index 결과가 undefined임을 이해했다.
- [ ] 먼 index 할당으로 희소 배열이 생길 수 있음을 확인했다.
- [ ] 문자열 key 속성이 length에 포함되지 않음을 이해했다.
- [ ] 배열 전체 순회에 length를 사용했다.
- [ ] 중첩 배열에 이중 index로 접근했다.
- [ ] 중첩 반복문으로 모든 내부 요소를 출력했다.

## 배열 변경 메서드

- [ ] push가 뒤에 추가하고 길이를 반환함을 이해했다.
- [ ] unshift가 앞에 추가하고 길이를 반환함을 이해했다.
- [ ] pop이 마지막 요소를 제거하고 반환함을 이해했다.
- [ ] shift가 첫 요소를 제거하고 반환함을 이해했다.
- [ ] reverse가 원본 배열을 변경함을 확인했다.
- [ ] sort가 원본 배열을 변경함을 확인했다.
- [ ] 숫자 정렬에 비교 함수를 사용했다.
- [ ] splice로 삭제·추가·교체할 수 있다.

## 복사와 검색

- [ ] slice가 원본을 변경하지 않음을 이해했다.
- [ ] slice의 끝 index가 제외됨을 확인했다.
- [ ] 음수 slice가 뒤에서부터 계산됨을 이해했다.
- [ ] indexOf가 첫 일치 index를 반환함을 이해했다.
- [ ] 찾지 못할 때 -1을 반환함을 확인했다.

## 문자열 변환

- [ ] join으로 배열을 문자열로 만들었다.
- [ ] split으로 문자열을 배열로 만들었다.
- [ ] 구분자가 결과에서 제거됨을 이해했다.
- [ ] URL query string을 단계별로 분해했다.
- [ ] 이메일을 @와 점 기준으로 분리했다.
- [ ] 실제 URL 분석에는 URLSearchParams를 검토했다.

## 문제 해결

- [ ] 1~10 배열을 반복문으로 생성했다.
- [ ] 홀수와 4보다 큰 수를 필터링했다.
- [ ] 참가자와 완주자를 비교했다.
- [ ] 결과 배열에는 push를 사용했다.
- [ ] 좌석 예약 중복을 검사했다.
- [ ] 중복 없는 로또를 전체 배열과 비교했다.
- [ ] 로또 숫자 정렬에 숫자 비교 함수를 사용했다.

## 원본 코드 검수

- [ ] 두 실제 원본 경로를 기록했다.
- [ ] arr3의 let·const 차이를 기록했다.
- [ ] 내 코드의 잘못된 arr3[0] label을 기록했다.
- [ ] arr3[] 식별자 설명 오류를 기록했다.
- [ ] stack·heap·자료 크기 설명의 한계를 기록했다.
- [ ] 1차원 배열 설명 오류를 기록했다.
- [ ] Queue 설명의 push·shift 조합 문제를 기록했다.
- [ ] 내림차순 설명의 비교 함수 누락을 기록했다.
- [ ] 기본 sort의 문자열 정렬 문제를 설명했다.
- [ ] 문제 2-2의 잘못된 출력 label을 기록했다.
- [ ] 문제 3 첫 풀이의 break 오류를 기록했다.
- [ ] 결과 배열이 문자열로 변하는 문제를 기록했다.
- [ ] 이름 미완주자 풀이 오류를 기록했다.
- [ ] 좌석 예약 프로그램이 미완성임을 기록했다.
- [ ] 앞의 두 로또 풀이가 중복을 보장하지 못함을 기록했다.
- [ ] 마지막 로또 풀이 구조가 더 적절함을 기록했다.
- [ ] 강사님 splice 예제를 기록했다.
- [ ] 숫자 야구가 양쪽 모두 미완성임을 기록했다.

---

# Key Summary

- 배열은 여러 값을 순서대로 관리하며 index는 0부터 시작한다.
- 배열 리터럴 `[]`이 일반적으로 가장 많이 사용된다.
- `new Array(3)`은 숫자 3 하나를 가진 배열이 아니라 길이 3의 빈 슬롯 배열이다.
- `typeof []`의 결과는 `"object"`이며 배열 판별에는 `Array.isArray()`를 사용한다.
- 강사님 arr3는 let이라 전체 재할당이 가능하고, 내 arr3는 const라 전체 재할당이 불가능하다.
- const 배열도 내부 요소는 변경할 수 있다.
- 내 코드의 `arr3[] 자체가 식별자`라는 설명은 잘못이다.
- 존재하지 않는 배열 index에 접근하면 일반적으로 undefined가 반환된다.
- 먼 index에 값을 넣으면 빈 슬롯이 많은 희소 배열이 생길 수 있다.
- 배열에 문자열 key를 추가할 수 있지만 일반적인 배열 요소와 length에 포함되지 않는다.
- 내 stack·heap과 문자·숫자 크기 설명은 JavaScript 엔진에 정확히 일반화하기 어렵다.
- 배열 전체 순회에는 고정 숫자보다 `arr.length`를 사용하는 편이 안전하다.
- 중첩 배열 요소는 `array[row][column]`처럼 이중 index로 접근한다.
- 내 코드는 중첩 배열을 1차원 배열이라고 설명해 부정확하다.
- `push()`는 뒤에 추가하고 `unshift()`는 앞에 추가한다.
- `pop()`은 마지막 요소, `shift()`는 첫 요소를 제거하고 반환한다.
- Queue를 배열로 구현할 때 일반적으로 push와 shift를 조합한다.
- `reverse()`와 `sort()`는 원본 배열을 변경한다.
- 기본 `sort()`는 문자열 기준이라 `[10,5,3]`을 `[10,3,5]`로 정렬할 수 있다.
- 숫자 오름차순은 `(a, b) => a - b`, 내림차순은 `(a, b) => b - a`를 사용한다.
- `slice()`는 원본을 변경하지 않고 시작 index 포함, 끝 index 제외 범위를 복사한다.
- `splice()`는 원본에서 요소를 삭제·추가·교체한다.
- `indexOf()`는 첫 일치 index를 반환하고 없으면 -1을 반환한다.
- `join()`은 배열을 문자열로, `split()`은 문자열을 배열로 만든다.
- URL query string은 ?, &, = 기준으로 단계별 분해할 수 있다.
- 실무 URL 파싱에는 URL과 URLSearchParams가 더 안전하다.
- 내 코드는 이메일에서 `naver`를 추출하는 추가 실습을 포함한다.
- 문제 1은 push로 1~10 배열을 생성한다.
- 문제 2-2 출력에는 `홀수의 개수`라는 잘못된 label이 남아 있다.
- 문제 3의 첫 풀이에는 정답 3을 미리 제거하고, 안쪽 반복을 첫 비교 후 break하는 오류가 있다.
- 최종 등번호 풀이 구조는 작동하지만 결과 배열에 `+=`를 사용해 문자열로 변한다.
- 이름 미완주자 풀이에서는 랜덤 완주자를 누적해 루피를 찾지 못한다.
- 소극장 예약 시스템은 메뉴 2·3과 중복 예약 처리가 미완성이다.
- 첫 번째와 두 번째 로또 풀이는 중복을 확실히 막지 못한다.
- 세 번째 로또 풀이는 기존 전체 배열을 검사해 더 적절하지만 숫자 sort 비교 함수가 빠져 있다.
- 강사님 코드는 `splice(2,1)`로 index 2의 요소 하나를 제거한다.
- 숫자 야구 게임은 양쪽 모두 설명 또는 계획만 있고 실제 완성 코드는 없다.
