---
title: JavaScript 배열과 배열 메서드
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript 배열과 배열 메서드

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `06_JavaScript_배열과_배열메서드.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/06_array.html`, `workspace_teacher/workspace_html/javascript/06_array.html` |
| 핵심 범위 | 배열 생성, 인덱스, 길이, 다차원 배열, 값 추가·삭제, 정렬, 복사, 검색, 문자열 변환 |
| 실습 범위 | 음식 목록 순회, 쿼리스트링 분석, 이메일 도메인 추출, 미완주자 찾기, 좌석 예약, 로또 번호 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 배열의 생성·접근·변경·검색·정렬에 필요한 핵심 코드만 발췌하고, 원본 변경 여부와 잘못된 풀이의 개선 방향을 함께 설명한다.

---

# 개요

배열은 여러 값을 하나의 변수에 순서대로 저장하는 자료구조다.

```javascript
const fruits = [
    "사과",
    "바나나",
    "포도",
]
```

각 값은 0부터 시작하는 인덱스로 구분한다.

```text
인덱스 0 → 사과
인덱스 1 → 바나나
인덱스 2 → 포도
```

배열을 사용하면 다음 작업을 할 수 있다.

| 작업 | 대표 기능 |
| --- | --- |
| 값 조회 | `array[index]` |
| 값 추가 | `push()`, `unshift()` |
| 값 삭제 | `pop()`, `shift()`, `splice()` |
| 일부 복사 | `slice()` |
| 값 검색 | `indexOf()`, `includes()` |
| 순서 변경 | `reverse()`, `sort()` |
| 문자열 변환 | `join()` |
| 반복 처리 | `for`, `for...of`, 배열 메서드 |

> [!IMPORTANT]
> 배열 변수 하나에 여러 값을 저장하지만, 각 값은 서로 다른 인덱스로 관리된다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 배열 | 여러 값을 순서대로 저장 |
| 인덱스 | 각 요소의 위치 번호 |
| 요소 | 배열에 저장된 각각의 값 |
| `length` | 배열의 길이 |
| 희소 배열 | 인덱스 사이가 비어 있는 배열 |
| 다차원 배열 | 배열 안에 다른 배열 저장 |
| 원본 변경 메서드 | 배열 자체의 내용을 변경 |
| 비변경 메서드 | 원본을 유지하고 새 값을 반환 |
| 얕은 복사 | 중첩 객체는 참조를 공유하는 복사 |
| 비교 함수 | 숫자 정렬 기준을 `sort()`에 전달 |

---

# 학습 목표

- 배열을 리터럴과 생성자로 만들 수 있다.
- 배열 인덱스가 0부터 시작함을 이해한다.
- 존재하지 않는 인덱스가 `undefined`를 반환함을 설명할 수 있다.
- `const` 배열의 요소를 변경할 수 있는 이유를 설명할 수 있다.
- `length`를 이용해 배열 전체를 순회할 수 있다.
- 다차원 배열의 요소에 접근할 수 있다.
- `push()`, `unshift()`, `pop()`, `shift()`를 사용할 수 있다.
- `reverse()`와 `sort()`가 원본을 변경함을 이해한다.
- 숫자 배열을 비교 함수로 정렬할 수 있다.
- `slice()`와 `splice()`를 구분할 수 있다.
- `indexOf()`와 `includes()`를 사용할 수 있다.
- `join()`과 `split()`의 방향을 구분할 수 있다.
- 쿼리스트링과 이메일 문자열을 안전하게 처리할 수 있다.
- 배열 문제에서 `Set`, `filter()`, `includes()`를 활용할 수 있다.

---

# 1. 배열 리터럴

## 1-1. 원본 코드

```javascript
const array = []
```

대괄호 `[]`를 이용한 배열 리터럴이 가장 일반적이다.

```javascript
const numbers = [
    1,
    2,
    3,
]
```

---

# 2. `new Array()`

```javascript
const array = new Array()
```

배열 생성자로도 만들 수 있다.

```javascript
const values = new Array(
    1,
    2,
    3,
)
```

일반적인 배열 작성에는 리터럴이 더 짧고 명확하다.

---

# 3. 생성자 숫자 하나 주의

```javascript
const values = new Array(3)

console.log(values)
console.log(values.length)
```

출력 개념:

```text
비어 있는 칸 3개
length = 3
```

`[3]`과 의미가 다르다.

```javascript
const values = [3]
```

이 배열에는 숫자 3 하나가 들어 있다.

---

# 4. 배열의 자료형

```javascript
const array = []

console.log(typeof array)
```

출력:

```text
object
```

배열은 객체의 한 종류이므로 `typeof` 결과가 `"object"`다.

정확한 배열 검사는 다음을 사용한다.

```javascript
console.log(
    Array.isArray(array),
)
```

출력:

```text
true
```

---

# 5. 여러 자료형 저장

```javascript
const values = [
    1,
    2,
    "글씨",
    false,
    3.14,
    [],
]
```

JavaScript 배열에는 서로 다른 자료형을 함께 저장할 수 있다.

다만 실제 데이터 목록에서는 동일한 형태를 유지하는 편이 처리하기 쉽다.

---

# 6. 배열 출력 방식

원본:

```javascript
console.log(
    "values: " + values,
)

console.log(
    "values:",
    values,
)
```

문자열과 `+`로 연결하면 배열이 문자열로 변환된다.

```text
1,2,글씨,false,3.14,
```

배열 구조를 확인하려면 별도 인자로 전달하는 편이 좋다.

```javascript
console.log("values:", values)
```

---

# 7. 인덱스 접근

```javascript
const values = [
    10,
    20,
    30,
]

console.log(values[0])
console.log(values[1])
```

출력:

```text
10
20
```

인덱스는 0부터 시작한다.

---

# 8. 요소 변경

```javascript
const values = [
    1,
    2,
    3,
]

values[0] = 10

console.log(values)
```

출력:

```text
[10, 2, 3]
```

---

# 9. `const` 배열

다음 코드는 가능하다.

```javascript
const values = [
    1,
    2,
    3,
]

values[0] = 10
values.push(4)
```

다음 재할당은 불가능하다.

```text
values = [4, 5, 6]
```

> [!IMPORTANT]
> `const`는 배열 내부를 완전히 불변으로 만드는 문법이 아니다.
>
> 변수에 저장된 배열 참조를 다른 배열로 재할당하지 못하게 한다.

---

# 10. 문자열 인덱스

```javascript
const text = "abc"

console.log(text[1])
```

출력:

```text
b
```

문자열도 인덱스로 문자를 읽을 수 있지만 문자열 자체는 불변이다.

---

# 11. 존재하지 않는 인덱스

```javascript
const values = [
    1,
    2,
    3,
]

console.log(values[60])
```

출력:

```text
undefined
```

변수 자체가 선언되지 않은 경우의 `ReferenceError`와 다르다.

---

# 12. 먼 인덱스에 값 대입

```javascript
const values = [
    1,
    2,
    3,
]

values[60] = 60

console.log(values.length)
```

출력:

```text
61
```

인덱스 3부터 59까지 빈 칸이 생기는 희소 배열이 된다.

> [!WARNING]
> 희소 배열은 반복·메서드 동작을 예측하기 어렵게 만들 수 있다.
>
> 값은 `push()` 등으로 연속해서 추가하는 것이 일반적이다.

---

# 13. 배열에 문자열 키 추가

원본:

```javascript
const values = [
    1,
    2,
    3,
]

values["문자"] = "문자"
```

배열도 객체이므로 속성은 추가할 수 있다.

하지만 이 속성은 일반적인 배열 요소가 아니다.

```javascript
console.log(values.length)
```

문자열 키를 추가해도 `length`는 증가하지 않는다.

배열 요소가 아닌 이름 기반 데이터는 객체를 사용하는 편이 적합하다.

---

# 14. 배열 길이

```javascript
const values = [
    0,
    1,
    2,
    3,
    4,
    5,
]

console.log(values.length)
```

출력:

```text
6
```

마지막 인덱스는 다음과 같다.

```javascript
values.length - 1
```

---

# 15. `length`를 이용한 순회

```javascript
for (
    let index = 0;
    index < values.length;
    index += 1
) {
    console.log(values[index])
}
```

배열 길이가 바뀌어도 반복 범위를 자동으로 맞출 수 있다.

---

# 16. 마지막 요소

```javascript
const lastValue = (
    values[values.length - 1]
)
```

현대 JavaScript에서는 다음도 사용할 수 있다.

```javascript
const lastValue = values.at(-1)
```

---

# 17. 다차원 배열

## 17-1. 원본 구조

```javascript
const westernFood = [
    "파스타",
    "피자",
    "스테이크",
]

const chineseFood = [
    "짜장",
    "짬뽕",
    "탕수육",
]

const japaneseFood = [
    "라멘",
    "오차즈케",
    "스키야키",
]

const foods = [
    westernFood,
    chineseFood,
    japaneseFood,
]
```

배열 안에 배열을 저장한 2차원 배열이다.

---

# 18. 다차원 배열 접근

```javascript
console.log(foods[0])
console.log(foods[0][2])
```

출력:

```text
['파스타', '피자', '스테이크']
스테이크
```

```text
foods[0]
→ 첫 번째 음식 분류

foods[0][2]
→ 첫 분류의 세 번째 음식
```

---

# 19. 모든 음식 출력

```javascript
for (
    let categoryIndex = 0;
    categoryIndex < foods.length;
    categoryIndex += 1
) {
    for (
        let foodIndex = 0;
        foodIndex < foods[categoryIndex].length;
        foodIndex += 1
    ) {
        console.log(
            foods[categoryIndex][foodIndex],
        )
    }
}
```

---

# 20. `for...of`로 개선

```javascript
for (const category of foods) {
    for (const food of category) {
        console.log(food)
    }
}
```

인덱스가 필요하지 않다면 값 자체를 순회하는 방식이 더 읽기 쉽다.

---

# 21. `push()`

```javascript
const values = [
    1,
    2,
    3,
    4,
]

const newLength = values.push(5)

console.log(values)
console.log(newLength)
```

출력:

```text
[1, 2, 3, 4, 5]
5
```

`push()`는 배열 끝에 값을 추가하고 새 길이를 반환한다.

---

# 22. `unshift()`

```javascript
values.unshift(0)
```

배열 앞에 값을 추가한다.

앞쪽 인덱스를 모두 이동해야 하므로 큰 배열에서는 `push()`보다 비용이 클 수 있다.

---

# 23. `pop()`

```javascript
const removedValue = values.pop()
```

배열 마지막 값을 제거하고 그 값을 반환한다.

배열이 비어 있으면 `undefined`를 반환한다.

---

# 24. `shift()`

```javascript
const removedValue = values.shift()
```

배열 첫 값을 제거하고 반환한다.

앞쪽 요소들의 인덱스가 다시 정리된다.

---

# 25. 스택과 큐

| 구조 | 입력 | 출력 |
| --- | --- | --- |
| 스택 | `push()` | `pop()` |
| 큐처럼 사용 | `push()` | `shift()` |

원본의 “선입선출에서 `unshift()`와 `shift()`”도 가능하지만, 일반적인 큐 표현은 뒤에 넣고 앞에서 꺼내는 `push()`·`shift()` 조합이 이해하기 쉽다.

---

# 26. `reverse()`

```javascript
const values = [
    1,
    2,
    3,
]

const reversed = values.reverse()

console.log(values)
console.log(reversed)
```

둘 다 뒤집힌 같은 배열을 가리킨다.

> [!WARNING]
> `reverse()`는 원본 배열을 변경한다.

원본 유지:

```javascript
const reversed = [
    ...values,
].reverse()
```

---

# 27. `sort()` 기본 동작

```javascript
const values = [
    7,
    4,
    2,
    3,
    6,
    5,
]

values.sort()
```

한 자리 숫자에서는 오름차순처럼 보일 수 있다.

하지만 기본 `sort()`는 값을 문자열로 변환해 비교한다.

---

# 28. 숫자 정렬 오류

```javascript
const values = [
    10,
    5,
    3,
]

console.log(values.sort())
```

출력:

```text
[10, 3, 5]
```

문자열 순서로 비교하기 때문이다.

---

# 29. 숫자 오름차순·내림차순

```javascript
values.sort(
    (a, b) => a - b,
)
```

오름차순:

```text
[3, 5, 10]
```

내림차순:

```javascript
values.sort(
    (a, b) => b - a,
)
```

> [!IMPORTANT]
> 숫자 정렬에는 비교 함수를 전달한다.

---

# 30. 메서드 체이닝

원본:

```javascript
values.sort().reverse()
```

메서드의 반환값에 다음 메서드를 이어 호출하는 방식을 체이닝이라고 한다.

다만 숫자 내림차순에는 다음이 더 직접적이다.

```javascript
values.sort(
    (a, b) => b - a,
)
```

---

# 31. `slice()`

```javascript
const values = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
]

const copied = values.slice(
    2,
    5,
)
```

결과:

```text
[2, 3, 4]
```

시작 인덱스는 포함하고 종료 인덱스는 포함하지 않는다.

원본 배열은 변경되지 않는다.

---

# 32. `slice()` 사용 형태

```javascript
values.slice(2)
// 인덱스 2부터 끝까지

values.slice(-2)
// 뒤에서 두 번째부터 끝까지

values.slice()
// 얕은 복사
```

---

# 33. `splice()`

원본 마지막 코드:

```javascript
const values = [
    1,
    2,
    3,
    4,
    5,
]

values.splice(
    2,
    1,
)
```

결과:

```text
values
→ [1, 2, 4, 5]

반환값
→ [3]
```

`splice()`는 원본을 변경한다.

---

# 34. `slice()`와 `splice()` 비교

| 메서드 | 목적 | 원본 변경 |
| --- | --- | --- |
| `slice()` | 일부 복사 | 아니오 |
| `splice()` | 삭제·삽입·교체 | 예 |

```javascript
values.splice(
    시작인덱스,
    삭제개수,
    추가값,
)
```

---

# 35. `indexOf()`

```javascript
const values = [
    0,
    1,
    2,
    3,
    4,
]

console.log(
    values.indexOf(4),
)
```

출력:

```text
4
```

찾지 못하면 `-1`을 반환한다.

---

# 36. `includes()`

값 존재 여부만 필요하다면 다음이 더 직접적이다.

```javascript
console.log(
    values.includes(4),
)
```

출력:

```text
true
```

---

# 37. 이메일 ID 추출

```javascript
const email = "todair@naver.com"
const atIndex = email.indexOf("@")

if (atIndex === -1) {
    console.log("올바른 이메일이 아닙니다.")
} else {
    const id = email.slice(
        0,
        atIndex,
    )

    console.log(id)
}
```

출력:

```text
todair
```

---

# 38. `join()`

```javascript
const values = [
    "a",
    "b",
    "c",
]

console.log(values.join())
console.log(values.join(";"))
```

출력:

```text
a,b,c
a;b;c
```

배열 요소를 하나의 문자열로 결합한다.

---

# 39. `split()`

```javascript
const text = "a;b;c"
const values = text.split(";")

console.log(values)
```

출력:

```text
['a', 'b', 'c']
```

`split()`은 문자열 메서드이며 문자열을 배열로 나눈다.

---

# 40. `join()`과 `split()` 비교

```text
배열
→ join()
→ 문자열

문자열
→ split()
→ 배열
```

구분자가 실제 데이터에 포함될 수 있다면 단순 결합보다 JSON 같은 구조화 형식을 검토한다.

---

# 41. 쿼리스트링 원본 풀이

원본은 URL을 `?`, `&`, `=` 순서로 나눈다.

```javascript
const url = (
    "https://search.naver.com/search.naver"
    + "?where=nexearch"
    + "&query=1234"
    + "&ackey=test"
)

const queryString = url.split("?")[1]
const parameters = queryString.split("&")

for (const parameter of parameters) {
    const [name, value] = parameter.split("=")

    if (name === "query") {
        console.log(value)
    }
}
```

출력:

```text
1234
```

---

# 42. `URLSearchParams`로 개선

브라우저에는 쿼리스트링 전용 API가 있다.

```javascript
const url = new URL(
    "https://search.naver.com/search.naver"
    + "?where=nexearch"
    + "&query=1234",
)

const query = (
    url.searchParams.get("query")
)

console.log(query)
```

직접 `split()`을 여러 번 작성하는 것보다 인코딩된 값과 누락된 키를 안전하게 처리할 수 있다.

---

# 43. 이메일 도메인 추출

```javascript
const email = "test@naver.com"
const parts = email.split("@")

if (parts.length !== 2) {
    console.log("올바른 이메일이 아닙니다.")
} else {
    const domainParts = (
        parts[1].split(".")
    )

    console.log(domainParts[0])
}
```

출력:

```text
naver
```

---

# 44. 문제 1: 1부터 10까지 배열 만들기

## 44-1. 내 코드

```javascript
const numbers = []

for (let number = 1; number <= 10; number += 1) {
    numbers.push(number)
}

console.log(numbers)
```

출력:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

# 45. `Array.from()`으로 만들기

```javascript
const numbers = Array.from(
    {
        length: 10,
    },
    (_, index) => index + 1,
)
```

반복 규칙이 명확한 배열을 선언적으로 생성할 수 있다.

---

# 46. 문제 2: 조건별 개수

```javascript
const numbers = [
    3,
    4,
    7,
    5,
    1,
    6,
]

const oddNumbers = numbers.filter(
    number => number % 2 !== 0,
)

const greaterThanFour = numbers.filter(
    number => number > 4,
)

console.log(oddNumbers.length)
console.log(greaterThanFour.length)
```

출력:

```text
4
3
```

원본의 문자열 누적보다 실제 값 목록과 개수를 함께 재사용하기 쉽다.

---

# 47. 문제 3: 미완주자 찾기

```javascript
const participants = [
    1,
    2,
    3,
    4,
    5,
]

const finishers = [
    2,
    4,
    5,
    1,
]

const unfinished = participants.filter(
    participant => (
        !finishers.includes(
            participant,
        )
    ),
)

console.log(unfinished)
```

출력:

```text
[3]
```

원본의 `join()`·`split()` 방식은 특정 값 3을 미리 알고 있어 일반적인 풀이가 아니다.

---

# 48. 이름으로 미완주자 찾기

```javascript
const participants = [
    "나미",
    "우솝",
    "조로",
    "루피",
    "상디",
]

const finishers = [
    "우솝",
    "나미",
    "상디",
    "조로",
]

const unfinished = participants.filter(
    name => !finishers.includes(name),
)

console.log(unfinished)
```

출력:

```text
['루피']
```

---

# 49. 중복 이름이 있을 때

`includes()` 방식은 동명이인이 있는 경우 정확하지 않을 수 있다.

빈도표를 사용한다.

```javascript
const counts = new Map()

for (const name of finishers) {
    counts.set(
        name,
        (counts.get(name) ?? 0) + 1,
    )
}

const unfinished = participants.filter(
    name => {
        const count = counts.get(name) ?? 0

        if (count === 0) {
            return true
        }

        counts.set(name, count - 1)
        return false
    },
)
```

---

# 50. 문제 4: 좌석 예약 상태

```javascript
const seats = Array(
    10,
).fill(false)

const seatNumber = 3
const seatIndex = seatNumber - 1

if (
    !Number.isInteger(seatNumber)
    || seatNumber < 1
    || seatNumber > seats.length
) {
    console.log("좌석 번호를 확인해주세요.")
} else if (seats[seatIndex]) {
    console.log("이미 예약된 자리입니다.")
} else {
    seats[seatIndex] = true

    console.log(
        `${seatNumber}번 자리 예약 완료`,
    )
}
```

Boolean 배열로 예약 상태를 표현할 수 있다.

---

# 51. 잔여 좌석

```javascript
const remainingCount = seats.filter(
    isReserved => !isReserved,
).length

console.log(
    `잔여 좌석: ${remainingCount}개`,
)
```

---

# 52. 문제 5: 로또 번호

원본의 첫 번째·두 번째 풀이는 모든 기존 번호와 비교하지 않아 중복을 완전히 막지 못할 수 있다.

가장 단순한 방식:

```javascript
const lottoNumbers = new Set()

while (lottoNumbers.size < 6) {
    const number = (
        Math.floor(Math.random() * 45)
        + 1
    )

    lottoNumbers.add(number)
}

const result = [
    ...lottoNumbers,
].sort(
    (a, b) => a - b,
)

console.log(result)
```

---

# 53. `Set`을 사용하는 이유

`Set`은 같은 값을 다시 추가해도 하나만 저장한다.

```javascript
const values = new Set()

values.add(3)
values.add(3)

console.log(values.size)
```

출력:

```text
1
```

중복 없는 로또 번호 생성에 적합하다.

---

# 54. 숫자 야구 배열 설계

```javascript
const answer = [
    1,
    2,
    3,
]

const guess = [
    1,
    3,
    5,
]

let strikes = 0
let balls = 0

for (
    let index = 0;
    index < answer.length;
    index += 1
) {
    if (guess[index] === answer[index]) {
        strikes += 1
    } else if (
        answer.includes(
            guess[index],
        )
    ) {
        balls += 1
    }
}

console.log(
    `${strikes}스트라이크 ${balls}볼`,
)
```

출력:

```text
1스트라이크 1볼
```

---

# 55. 원본 변경 여부 정리

| 메서드 | 원본 변경 | 반환값 |
| --- | --- | --- |
| `push()` | 예 | 새 길이 |
| `unshift()` | 예 | 새 길이 |
| `pop()` | 예 | 제거한 값 |
| `shift()` | 예 | 제거한 값 |
| `reverse()` | 예 | 원본 배열 |
| `sort()` | 예 | 원본 배열 |
| `splice()` | 예 | 제거한 요소 배열 |
| `slice()` | 아니오 | 새 배열 |
| `join()` | 아니오 | 문자열 |
| `indexOf()` | 아니오 | 인덱스 |
| `includes()` | 아니오 | Boolean |

---

# 56. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 배열 설명 | 참조·메모리 설명까지 상세 | 기본 개념 중심 |
| 선언 | `arr3`가 `const` | `arr3`가 `let` |
| 희소 배열 | 문자열 키와 먼 인덱스 설명 추가 | 동일 실습 |
| 음식 배열 | 완성된 중첩 반복 | 단계별 주석 포함 |
| 배열 메서드 | 설명과 반환값 기록 | 핵심 실행 중심 |
| URL 분석 | 풀이를 여러 번 재작성 | 기본 풀이 한 번 |
| 배열 문제 | 대부분 직접 시도 | 문제 요구사항 중심 |
| 로또 | 세 가지 풀이 시도 | 문제만 제시 |

## 56-1. 내 코드의 장점

- 배열 요소 변경과 배열 재할당 차이를 상세히 기록했다.
- 메서드의 반환값과 원본 변경 여부를 확인했다.
- URL·이메일 문자열 문제를 직접 풀었다.
- 미완주자·예약·로또 문제를 여러 방식으로 시도했다.

## 56-2. 내 코드의 개선점

- 배열을 단순히 “여러 변수를 만드는 기술”로만 설명하면 부족하다.
- `typeof array`가 `"object"`인 것과 배열 검사를 구분해야 한다.
- 먼 인덱스와 문자열 키 추가는 일반적인 배열 사용 방식이 아니다.
- 숫자 정렬에 기본 `sort()`를 사용하면 잘못된 순서가 나올 수 있다.
- 미완주자 풀이 일부는 특정 값과 무작위 값에 의존해 정답을 찾지 못한다.
- 로또 풀이 일부는 모든 기존 번호와 비교하지 않아 중복될 수 있다.
- `==`보다 `===`를 사용해야 한다.

## 56-3. 강사님 코드의 장점

- 배열 생성부터 메서드까지 한 흐름으로 학습할 수 있다.
- 다차원 배열과 중첩 반복문을 연결한다.
- `slice()`, `indexOf()`, `join()`, `split()`을 실제 문자열 문제에 적용한다.
- 배열 기반 종합 문제를 다양하게 제시한다.

## 56-4. 강사님 코드의 보충점

- `Array.isArray()` 설명이 필요하다.
- 숫자 정렬 비교 함수가 필요하다.
- `slice()`와 `splice()`의 차이를 보강할 수 있다.
- 배열의 문자열 속성과 희소 배열 사용 위험을 설명할 필요가 있다.
- 문제별 완성 풀이와 검증이 필요하다.

---

# 57. 기존 코드에서 개선 코드로 바꾼 이유

## 57-1. 숫자 정렬

기존:

```javascript
numbers.sort()
```

개선:

```javascript
numbers.sort(
    (a, b) => a - b,
)
```

## 57-2. URL 분석

기존:

```javascript
url
    .split("?")[1]
    .split("&")
```

개선:

```javascript
new URL(url)
    .searchParams
    .get("query")
```

## 57-3. 미완주자 탐색

기존:

```javascript
participants.join("")
```

개선:

```javascript
participants.filter(
    value => !finishers.includes(value),
)
```

## 57-4. 로또 중복 제거

기존:

```text
for문으로 이전 값 일부 비교
```

개선:

```javascript
const numbers = new Set()
```

---

# 58. 실무형 예제: 장바구니 요약

```javascript
const cart = [
    {
        name: "키보드",
        price: 45000,
        quantity: 2,
    },
    {
        name: "마우스",
        price: 25000,
        quantity: 1,
    },
]

const itemNames = cart.map(
    item => item.name,
)

const totalPrice = cart.reduce(
    (
        total,
        item,
    ) => (
        total
        + item.price * item.quantity
    ),
    0,
)

console.log(
    `상품: ${itemNames.join(", ")}`,
)

console.log(
    `총액: ${totalPrice.toLocaleString()}원`,
)
```

## 58-1. 출력 결과

```text
상품: 키보드, 마우스
총액: 115,000원
```

## 58-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| 객체 배열 | 상품별 여러 속성 관리 |
| `map()` | 상품명만 새 배열로 변환 |
| `reduce()` | 상품 금액 누적 |
| `join()` | 상품명 문자열 생성 |
| `toLocaleString()` | 금액 형식 표시 |

---

# 59. 대표 오류로 이해하기

## 59-1. 존재하지 않는 인덱스

오류가 아니라 `undefined`가 반환된다.

## 59-2. `const` 배열 재할당

```text
const values = []
values = [1, 2]
```

`TypeError`가 발생한다.

## 59-3. 숫자 기본 정렬

`[10, 5, 3]`이 `[10, 3, 5]`로 정렬될 수 있다.

## 59-4. `slice()`와 `splice()` 혼동

원본 배열이 예상하지 못하게 변경될 수 있다.

## 59-5. 찾지 못한 `indexOf()` 결과 사용

`-1`을 실제 인덱스처럼 사용하면 마지막 쪽을 잘못 자를 수 있다.

## 59-6. 로또 중복 검사 누락

새 숫자를 모든 기존 숫자와 비교하지 않으면 중복이 남는다.

---

# 60. 자주 하는 실수

## 60-1. 배열 인덱스를 1부터 시작한다고 생각

첫 요소는 인덱스 0이다.

## 60-2. `typeof`만으로 배열 확인

`Array.isArray()`를 사용한다.

## 60-3. `const` 배열 요소도 변경 불가하다고 생각

요소 변경은 가능하고 재할당만 불가능하다.

## 60-4. 먼 인덱스에 직접 값 추가

희소 배열이 만들어진다.

## 60-5. 배열에 이름 기반 속성 저장

객체가 더 적합할 수 있다.

## 60-6. `reverse()`·`sort()`가 새 배열을 반환한다고 생각

원본을 직접 변경한다.

## 60-7. 숫자 배열에 기본 `sort()` 사용

비교 함수를 전달한다.

## 60-8. `slice()` 종료 인덱스도 포함한다고 생각

종료 인덱스 직전까지만 복사한다.

## 60-9. `indexOf()`가 값을 찾지 못하면 `undefined`라고 생각

`-1`을 반환한다.

## 60-10. `join()`이 배열을 변경한다고 생각

새 문자열을 반환한다.

---

# 61. 핵심 요약

```text
[]
→ 배열 리터럴

array[index]
→ 요소 접근

array.length
→ 배열 길이

Array.isArray()
→ 배열 여부 확인
```

```text
push()
→ 끝에 추가

pop()
→ 끝에서 제거

unshift()
→ 앞에 추가

shift()
→ 앞에서 제거
```

```text
slice()
→ 일부 복사
→ 원본 유지

splice()
→ 삭제·추가·교체
→ 원본 변경
```

```text
sort((a, b) => a - b)
→ 숫자 오름차순

join()
→ 배열을 문자열로

split()
→ 문자열을 배열로
```

---

# 62. 최종 체크리스트

- [ ] 배열 리터럴을 작성할 수 있는가?
- [ ] 인덱스가 0부터 시작함을 이해했는가?
- [ ] `Array.isArray()`로 배열을 확인할 수 있는가?
- [ ] `const` 배열의 요소 변경과 재할당을 구분할 수 있는가?
- [ ] 존재하지 않는 인덱스가 `undefined`임을 이해했는가?
- [ ] 희소 배열의 문제를 설명할 수 있는가?
- [ ] `length`로 배열 전체를 순회할 수 있는가?
- [ ] 다차원 배열 요소에 접근할 수 있는가?
- [ ] `push()`, `unshift()`, `pop()`, `shift()`를 사용할 수 있는가?
- [ ] `reverse()`와 `sort()`의 원본 변경을 이해했는가?
- [ ] 숫자 배열을 비교 함수로 정렬할 수 있는가?
- [ ] `slice()`와 `splice()`를 구분할 수 있는가?
- [ ] `indexOf()`와 `includes()`를 사용할 수 있는가?
- [ ] `join()`과 `split()`의 방향을 구분할 수 있는가?
- [ ] `URLSearchParams`로 쿼리 값을 찾을 수 있는가?
- [ ] 배열에서 조건에 맞는 값을 `filter()`로 찾을 수 있는가?
- [ ] `Set`으로 중복값을 제거할 수 있는가?
- [ ] 로또 번호를 중복 없이 생성할 수 있는가?
- [ ] 배열 메서드의 원본 변경 여부를 확인할 수 있는가?

---

# 마무리

배열의 핵심은 여러 값을 한 변수에 넣는 것에서 끝나지 않는다.

```text
값의 순서와 인덱스를 이해하고
    ↓
추가·삭제 메서드의 반환값을 확인하고
    ↓
원본 변경 여부를 구분하고
    ↓
목적에 맞는 검색·정렬·변환 방식을 선택하고
    ↓
반복되는 데이터 처리를 안전하게 구성하는 것
```

이 흐름을 이해하면 이후 날짜·함수·DOM 문서에서도 여러 데이터를 효과적으로 관리할 수 있다.
