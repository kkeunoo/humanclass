---
title: JavaScript 반복문과 배열 순회
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript 반복문과 배열 순회

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `04_JavaScript_반복문과_배열순회.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/04_for.html`, `04_1_pyramid.html`, 강사님 동일 파일 |
| 핵심 범위 | `for`, 누적 계산, 중첩 반복문, `break`, `continue`, `for...in`, `for...of`, `forEach()`, `map()`, `filter()`, `sort()` |
| 실습 범위 | 역순 출력, 홀짝 표시, 홀수 개수, 구구단, 주사위 조합, 로또 난수, 주차장 탐색, 문자열 패턴, 피라미드 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 반복문의 실행 구조와 배열 순회 방식에 필요한 코드만 발췌하고, 결과·선택 기준·오류 원인·실무 개선 방향을 함께 설명한다.

---

# 개요

반복문은 같은 작업을 여러 번 실행할 때 사용한다.

```text
반복되는 코드 찾기
    ↓
변하는 값의 규칙 찾기
    ↓
규칙을 변수로 바꾸기
    ↓
시작값과 종료 조건 정하기
```

예를 들어 1부터 5까지 출력하는 코드를 직접 다섯 번 작성할 수도 있다.

```javascript
console.log(1)
console.log(2)
console.log(3)
console.log(4)
console.log(5)
```

반복문으로 바꾸면 다음과 같다.

```javascript
for (let number = 1; number <= 5; number += 1) {
    console.log(number)
}
```

> [!IMPORTANT]
> 반복문의 핵심은 코드를 짧게 만드는 것이 아니라, 반복되는 규칙을 코드로 표현하는 것이다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `for` | 반복 횟수와 변화 규칙이 명확할 때 사용 |
| 초기화식 | 반복 시작 전에 한 번 실행 |
| 조건식 | 반복을 계속할지 판단 |
| 증감식 | 한 번 실행한 뒤 반복 변수 변경 |
| 중첩 반복문 | 반복문 안에 다른 반복문 작성 |
| `break` | 가장 가까운 반복문 즉시 종료 |
| `continue` | 현재 반복만 건너뛰고 다음 반복 진행 |
| `for...in` | 객체의 열거 가능한 키 순회 |
| `for...of` | 반복 가능한 객체의 값 순회 |
| `forEach()` | 배열의 각 요소마다 함수 실행 |
| `map()` | 각 요소를 변환해 새 배열 반환 |
| `filter()` | 조건을 만족한 요소만 새 배열로 반환 |
| `sort()` | 배열 원본 정렬 |
| 누적 변수 | 반복 중 계산 결과를 계속 저장 |
| 플래그 변수 | 특정 상태가 발생했는지 기록 |

---

# 학습 목표

- `for`문의 실행 순서를 설명할 수 있다.
- 증가·감소 반복문을 작성할 수 있다.
- 합계와 개수를 누적할 수 있다.
- 중첩 반복문으로 구구단과 조합을 만들 수 있다.
- 반복 횟수를 계산할 수 있다.
- `break`와 `continue`를 구분할 수 있다.
- 중첩 반복문을 플래그로 종료할 수 있다.
- `for...in`과 `for...of`의 차이를 설명할 수 있다.
- `forEach()`가 `undefined`를 반환함을 이해한다.
- `map()`과 `filter()`로 새 배열을 만들 수 있다.
- `sort()`의 비교 함수 동작을 설명할 수 있다.
- 문자열 누적으로 패턴을 만들 수 있다.
- 입력받은 줄 수로 피라미드를 출력할 수 있다.
- 난수 중복 가능성을 이해한다.
- 실무 상황에 맞는 반복 방식을 선택할 수 있다.

---

# 1. `for` 기본 구조

## 1-1. 원본 코드

```javascript
for (let i = 1; i <= 10; i++) {
    console.log(i)
}
```

## 1-2. 구성

```javascript
for (초기화식; 조건식; 증감식) {
    실행문
}
```

| 영역 | 실행 시점 |
| --- | --- |
| 초기화식 | 반복 시작 전 한 번 |
| 조건식 | 매 반복 시작 전 |
| 실행 블록 | 조건식이 Truthy일 때 |
| 증감식 | 실행 블록이 끝난 뒤 |

## 1-3. 실행 순서

```text
i = 1
→ i <= 10 확인
→ console.log(i)
→ i 증가
→ 다시 조건 확인
```

---

# 2. 반복 변수 이름

원본에서는 학습을 위해 `i`, `j`, `p`, `q`를 사용한다.

실무에서는 역할이 명확하면 의미 있는 이름을 사용한다.

```javascript
for (
    let productIndex = 0;
    productIndex < products.length;
    productIndex += 1
) {
    console.log(products[productIndex])
}
```

짧고 단순한 중첩 반복에서는 `i`, `j`도 사용할 수 있지만, 여러 단계가 섞이면 이름을 구체화하는 편이 좋다.

---

# 3. 증가 반복

```javascript
for (let number = 1; number <= 5; number += 1) {
    console.log(number)
}
```

출력:

```text
1
2
3
4
5
```

종료값을 포함하려면 `<=`, 제외하려면 `<`를 사용한다.

---

# 4. 감소 반복

## 4-1. 원본 문제

```javascript
for (let number = 5; number >= 1; number -= 1) {
    console.log(number)
}
```

## 4-2. 출력 결과

```text
5
4
3
2
1
```

감소 반복에서는 조건 방향과 증감 방향이 일치해야 한다.

---

# 5. 반복문 무한 실행 주의

잘못된 코드:

```javascript
for (let number = 1; number <= 5; number -= 1) {
    console.log(number)
}
```

`number`가 계속 작아지므로 `number <= 5`가 계속 참이 된다.

> [!WARNING]
> 반복 변수가 종료 조건에 가까워지는 방향으로 변경되는지 반드시 확인한다.

---

# 6. 1부터 5까지 합계

## 6-1. 반복 전 코드

```javascript
let sum = 0

sum += 1
sum += 2
sum += 3
sum += 4
sum += 5
```

## 6-2. 반복문으로 개선

```javascript
let sum = 0

for (let number = 1; number <= 5; number += 1) {
    sum += number
}

console.log(sum)
```

## 6-3. 출력 결과

```text
15
```

`sum`은 반복할 때마다 계산 결과를 저장하는 누적 변수다.

---

# 7. 홀수·짝수 표시

## 7-1. 내 코드

```javascript
for (let number = 1; number <= 5; number += 1) {
    if (number % 2 === 0) {
        console.log(`${number}(짝)`)
    } else {
        console.log(`${number}(홀)`)
    }
}
```

## 7-2. 출력 결과

```text
1(홀)
2(짝)
3(홀)
4(짝)
5(홀)
```

강사님 코드는 홀수 조건을 먼저 검사하지만 결과는 같다.

---

# 8. 삼항 연산자로 단순화

```javascript
for (let number = 1; number <= 5; number += 1) {
    const type = (
        number % 2 === 0
            ? "짝"
            : "홀"
    )

    console.log(`${number}(${type})`)
}
```

단순한 값 선택에는 삼항 연산자를 사용할 수 있다.

---

# 9. 홀수 개수 세기

```javascript
let oddCount = 0

for (let number = 1; number <= 10; number += 1) {
    if (number % 2 !== 0) {
        oddCount += 1
    }
}

console.log(`count: ${oddCount}`)
```

출력:

```text
count: 5
```

```text
홀수 발견
→ oddCount를 1 증가
```

---

# 10. 반복문 만드는 원리

원본에서 정리한 반복문 설계 순서:

| 단계 | 질문 |
| --- | --- |
| 1 | 어떤 코드가 반복되는가? |
| 2 | 반복할 때 바뀌는 값은 무엇인가? |
| 3 | 바뀌는 값의 규칙은 무엇인가? |
| 4 | 시작값은 무엇인가? |
| 5 | 언제 종료해야 하는가? |

이 원리는 구구단·패턴 출력·목록 처리에 공통으로 적용된다.

---

# 11. 구구단 한 단

```javascript
const dan = 2

for (let number = 1; number <= 9; number += 1) {
    console.log(
        `${dan} x ${number} = ${dan * number}`,
    )
}
```

출력 일부:

```text
2 x 1 = 2
2 x 2 = 4
...
2 x 9 = 18
```

---

# 12. 중첩 반복문

```javascript
for (let dan = 2; dan <= 9; dan += 1) {
    for (let number = 1; number <= 9; number += 1) {
        console.log(
            `${dan} x ${number} = ${dan * number}`,
        )
    }
}
```

바깥 반복문이 한 번 실행될 때 안쪽 반복문은 9번 실행된다.

총 실행 횟수:

```text
8단 × 9회
→ 72회
```

---

# 13. 중첩 반복문의 역할

```text
바깥 반복문
→ 큰 단위 변경

안쪽 반복문
→ 각 큰 단위 안의 세부 반복
```

예:

- 층과 주차 자리
- 행과 열
- 구구단의 단과 곱하는 수
- 주사위 첫 번째 값과 두 번째 값

---

# 14. 주사위 하나의 모든 경우

```javascript
for (let dice = 1; dice <= 6; dice += 1) {
    console.log(dice)
}
```

출력:

```text
1
2
3
4
5
6
```

---

# 15. 주사위 두 개의 모든 경우

```javascript
for (let firstDice = 1; firstDice <= 6; firstDice += 1) {
    for (
        let secondDice = 1;
        secondDice <= 6;
        secondDice += 1
    ) {
        console.log(
            `[${firstDice}, ${secondDice}]`,
        )
    }
}
```

총 조합:

```text
6 × 6
→ 36개
```

---

# 16. 주사위 합별 조합

```javascript
for (let targetSum = 2; targetSum <= 12; targetSum += 1) {
    let combinations = `합계 ${targetSum}: `

    for (let firstDice = 1; firstDice <= 6; firstDice += 1) {
        for (
            let secondDice = 1;
            secondDice <= 6;
            secondDice += 1
        ) {
            if (
                firstDice + secondDice
                === targetSum
            ) {
                combinations += (
                    `[${firstDice}, ${secondDice}] `
                )
            }
        }
    }

    console.log(combinations)
}
```

합계별 문자열을 누적한 뒤 한 번에 출력한다.

---

# 17. 중복 조합 제거

`[1, 2]`와 `[2, 1]`을 같은 조합으로 본다면 두 번째 주사위의 시작값을 첫 번째 주사위 값으로 설정할 수 있다.

```javascript
for (let firstDice = 1; firstDice <= 6; firstDice += 1) {
    for (
        let secondDice = firstDice;
        secondDice <= 6;
        secondDice += 1
    ) {
        console.log(
            `[${firstDice}, ${secondDice}]`,
        )
    }
}
```

단, 순서가 다른 경우를 별개로 봐야 한다면 제거하면 안 된다.

---

# 18. 로또 난수

## 18-1. 원본 코드

```javascript
for (let count = 1; count <= 6; count += 1) {
    const lottoNumber = (
        parseInt(Math.random() * 45)
        + 1
    )

    console.log(lottoNumber)
}
```

## 18-2. 개선

```javascript
const lottoNumber = (
    Math.floor(Math.random() * 45)
    + 1
)
```

가능한 값:

```text
1~45
```

---

# 19. 난수 중복 문제

원본 코드에서는 같은 숫자가 여러 번 나올 수 있다.

중복을 제거하려면 `Set`을 사용할 수 있다.

```javascript
const lottoNumbers = new Set()

while (lottoNumbers.size < 6) {
    const number = (
        Math.floor(Math.random() * 45)
        + 1
    )

    lottoNumbers.add(number)
}

console.log(
    [...lottoNumbers].sort(
        (a, b) => a - b,
    ),
)
```

---

# 20. `break`

## 20-1. 원본 코드

```javascript
for (let number = 1; number <= 100; number += 1) {
    if (number === 11) {
        console.log(number, "종료합니다.")
        break
    }

    console.log(number)
}
```

`break`를 만나면 가장 가까운 반복문이 즉시 종료된다.

---

# 21. `>` 조건이 안전한 경우

원본 메모에서는 `number === 11`보다 `number > 10`이 더 안전할 수 있다고 설명한다.

```text
if (number > 10) {
    break
}
```

증감값이 2이거나 중간값을 건너뛰는 경우에도 종료 조건을 놓치지 않는다.

> [!TIP]
> 정확히 한 값에 도달해야 하는지, 기준을 넘으면 종료해야 하는지 요구사항에 따라 조건을 선택한다.

---

# 22. 중첩 반복문 종료

주차장 예제:

```javascript
let position = 0
let isFound = false

for (let floor = 1; floor <= 4; floor += 1) {
    for (let space = 1; space <= 10; space += 1) {
        position += 1

        if (position >= 17) {
            isFound = true
            break
        }
    }

    if (isFound) {
        break
    }
}
```

안쪽 `break`만으로는 바깥 반복문이 종료되지 않으므로 플래그 변수를 사용한다.

---

# 23. 레이블을 이용한 중첩 종료

JavaScript는 레이블로 바깥 반복문을 직접 종료할 수 있다.

```javascript
parkingLoop:
for (let floor = 1; floor <= 4; floor += 1) {
    for (let space = 1; space <= 10; space += 1) {
        position += 1

        if (position >= 17) {
            break parkingLoop
        }
    }
}
```

> [!WARNING]
> 레이블은 익숙하지 않은 개발자에게 읽기 어려울 수 있다.
>
> 복잡한 탐색은 함수로 분리하고 `return`으로 종료하는 방법도 검토한다.

---

# 24. `continue`

```javascript
for (let number = 1; number <= 10; number += 1) {
    if (number % 2 === 0) {
        continue
    }

    console.log(number)
}
```

출력:

```text
1
3
5
7
9
```

`continue`는 현재 반복의 남은 코드를 건너뛰고 다음 반복으로 이동한다.

---

# 25. `break`와 `continue` 비교

| 키워드 | 동작 |
| --- | --- |
| `break` | 반복문 전체 종료 |
| `continue` | 현재 반복만 건너뜀 |

---

# 26. 배열 준비

```javascript
const numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
]
```

배열은 여러 방식으로 순회할 수 있으며 목적에 따라 선택해야 한다.

---

# 27. `for...in`

## 27-1. 원본 코드

```javascript
for (const index in numbers) {
    console.log("index:", index)
    console.log("value:", numbers[index])
}
```

`for...in`은 배열에서 인덱스처럼 보이는 **키**를 순회한다.

## 27-2. 주의점

- 키는 문자열이다.
- 배열 순회 전용 문법이 아니다.
- 상속된 열거 가능 속성까지 포함될 수 있다.

> [!WARNING]
> 배열 값 순회에는 `for...of`, 인덱스가 필요하면 일반 `for`나 `entries()`를 우선 고려한다.

---

# 28. `for...of`

```javascript
for (const value of numbers) {
    console.log(value)
}
```

배열의 값을 직접 순회한다.

인덱스가 필요하지 않다면 가장 읽기 쉽다.

---

# 29. 인덱스와 값 함께 순회

```javascript
for (const [index, value] of numbers.entries()) {
    console.log(index, value)
}
```

`entries()`는 `[인덱스, 값]` 형태를 반환한다.

---

# 30. `forEach()`

## 30-1. 원본 코드

```javascript
numbers.forEach(
    function (element, index, array) {
        console.log(element)
        console.log(index)
        console.log(array)
    },
)
```

콜백 전달인자:

| 순서 | 값 |
| --- | --- |
| 1 | 현재 요소 |
| 2 | 현재 인덱스 |
| 3 | 원본 배열 |

네 번째 전달인자는 기본적으로 제공되지 않아 `undefined`다.

---

# 31. `forEach()` 반환값

```javascript
const result = numbers.forEach(
    element => {
        console.log(element)
    },
)

console.log(result)
```

출력:

```text
undefined
```

`forEach()`는 새 배열을 반환하지 않는다.

---

# 32. `forEach()`의 `break`

`forEach()` 안에서는 일반 반복문처럼 `break`를 사용할 수 없다.

중간 종료가 필요하면 다음을 검토한다.

- `for`
- `for...of`
- `some()`
- `every()`
- `find()`

---

# 33. `map()`

## 33-1. 원본 코드

```javascript
const parity = numbers.map(
    element => {
        if (element % 2 === 0) {
            return "짝"
        }

        return "홀"
    },
)

console.log(parity)
```

출력:

```text
['홀', '짝', '홀', '짝', '홀', '짝', '홀']
```

`map()`은 각 요소의 반환값으로 원본과 같은 길이의 새 배열을 만든다.

---

# 34. 반환값 없는 `map()`

```javascript
const result = numbers.map(
    element => {
        console.log(element)
    },
)

console.log(result)
```

출력 형태:

```text
[undefined, undefined, ...]
```

`map()`은 변환 결과가 필요할 때 사용한다.

---

# 35. 영화 제목 길이 배열

```javascript
const movies = [
    "호프",
    "스파이더맨-브랜드 뉴 데이",
    "오디세이",
    "모아나",
]

const titleLengths = movies.map(
    movie => movie.length,
)

console.log(titleLengths)
```

각 제목을 길이 값으로 변환한다.

---

# 36. 화살표 함수 축약

일반 함수:

```javascript
const lengths = movies.map(
    function (movie) {
        return movie.length
    },
)
```

화살표 함수:

```javascript
const lengths = movies.map(
    movie => movie.length,
)
```

매개변수가 하나이고 반환 표현식이 하나라면 괄호·중괄호·`return`을 생략할 수 있다.

---

# 37. `filter()`

```javascript
const longTitles = movies.filter(
    movie => movie.length >= 4,
)

console.log(longTitles)
```

`filter()`는 콜백 결과가 Truthy인 요소만 새 배열에 포함한다.

---

# 38. `map()`과 `filter()` 비교

| 메서드 | 목적 | 결과 길이 |
| --- | --- | --- |
| `map()` | 각 요소 변환 | 원본과 같음 |
| `filter()` | 조건에 맞는 요소 선택 | 원본 이하 |
| `forEach()` | 부수 효과 실행 | 반환 배열 없음 |

---

# 39. `sort()`

## 39-1. 원본 코드

```javascript
titleLengths.sort(
    (a, b) => a - b,
)
```

오름차순 정렬이다.

내림차순:

```javascript
titleLengths.sort(
    (a, b) => b - a,
)
```

---

# 40. 비교 함수 반환값

```text
음수
→ a가 b보다 앞

양수
→ b가 a보다 앞

0
→ 순서 유지
```

숫자 정렬에는 `a - b`, `b - a` 패턴을 자주 사용한다.

---

# 41. `sort()`는 원본 변경

```javascript
const values = [3, 1, 2]
const sortedValues = values.sort(
    (a, b) => a - b,
)

console.log(values)
console.log(sortedValues)
```

둘 다 같은 정렬된 배열 객체를 가리킨다.

원본을 유지하려면:

```javascript
const sortedValues = [
    ...values,
].sort(
    (a, b) => a - b,
)
```

---

# 42. 마지막 요소 조회

원본:

```javascript
const lastValue = (
    titleLengths[
        titleLengths.length - 1
    ]
)
```

현대 JavaScript에서는 다음도 사용할 수 있다.

```javascript
const lastValue = titleLengths.at(-1)
```

`array[-1]`은 일반적인 마지막 인덱스 접근으로 동작하지 않는다.

---

# 43. 문자열 누적 패턴

```javascript
let line = ""

for (let count = 1; count <= 5; count += 1) {
    line += "+"
}

console.log(line)
```

출력:

```text
+++++
```

문자열을 반복해서 이어 붙여 한 줄의 패턴을 만든다.

---

# 44. `repeat()`로 단순화

같은 문자열을 정해진 횟수만큼 반복할 때는 `repeat()`를 사용할 수 있다.

```javascript
console.log("+".repeat(5))
```

출력:

```text
+++++
```

> [!TIP]
> 단순 반복 문자열은 `repeat()`가 더 직접적이다.  
> 각 위치마다 조건이 달라지면 반복문을 사용한다.

---

# 45. 직사각형 패턴

```javascript
for (let row = 1; row <= 3; row += 1) {
    console.log("+".repeat(5))
}
```

출력:

```text
+++++
+++++
+++++
```

바깥 반복문은 행, 문자열 반복은 열 역할을 한다.

---

# 46. 숫자 삼각형

```javascript
for (let row = 1; row <= 5; row += 1) {
    console.log(
        String(row).repeat(row),
    )
}
```

출력:

```text
1
22
333
4444
55555
```

원본의 3중 반복문을 한 줄의 `repeat()`로 단순화할 수 있다.

---

# 47. 감소 숫자 패턴

```javascript
for (let row = 1; row <= 5; row += 1) {
    console.log(
        String(row).repeat(
            6 - row,
        ),
    )
}
```

출력:

```text
11111
2222
333
44
5
```

---

# 48. 오른쪽 정렬 삼각형

```javascript
const height = 5

for (let row = 1; row <= height; row += 1) {
    const spaces = "_".repeat(
        height - row,
    )

    const symbols = "+".repeat(row)

    console.log(
        spaces + symbols,
    )
}
```

출력:

```text
____+
___++
__+++
_++++
+++++
```

---

# 49. 가운데 정렬 피라미드

```javascript
const height = 5

for (let row = 1; row <= height; row += 1) {
    const spaces = "_".repeat(
        height - row,
    )

    const symbols = "+".repeat(
        row * 2 - 1,
    )

    console.log(
        spaces + symbols + spaces,
    )
}
```

출력:

```text
____+____
___+++___
__+++++__
_+++++++_
+++++++++
```

---

# 50. 피라미드 공식

| 영역 | 개수 |
| --- | --- |
| 왼쪽 공백 | `height - row` |
| 기호 | `row * 2 - 1` |
| 오른쪽 공백 | `height - row` |

```text
1행
→ 공백 4, 기호 1

2행
→ 공백 3, 기호 3

3행
→ 공백 2, 기호 5
```

---

# 51. 입력 줄 수 검증

원본은 `prompt()` 값을 바로 반복 조건에 사용한다.

개선:

```javascript
const input = prompt(
    "줄 수를 입력해주세요.",
)

const height = Number(input)

if (
    !Number.isInteger(height)
    || height <= 0
    || height > 20
) {
    console.log(
        "1부터 20까지의 정수를 입력해주세요.",
    )
} else {
    for (let row = 1; row <= height; row += 1) {
        const spaces = " ".repeat(
            height - row,
        )

        const symbols = "*".repeat(
            row * 2 - 1,
        )

        console.log(
            spaces + symbols,
        )
    }
}
```

---

# 52. 반복 방식 선택 기준

| 목적 | 권장 방식 |
| --- | --- |
| 횟수·인덱스 제어 | `for` |
| 값 직접 순회 | `for...of` |
| 객체 키 순회 | `for...in`, `Object.keys()` |
| 배열 요소마다 작업 실행 | `forEach()` |
| 각 요소를 변환 | `map()` |
| 조건에 맞는 요소 선택 | `filter()` |
| 중간에 종료 | `for`, `for...of` |
| 단순 문자열 반복 | `repeat()` |

---

# 53. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 반복 구조 | 주석으로 실행 순서 상세 설명 | 핵심 순서 정리 |
| 홀짝 문제 | 짝수 조건 우선 | 홀수 조건 우선 |
| 주사위 합 | 문자열 누적으로 한 줄 출력 | 합별 조합과 합 9 별도 저장 |
| 중첩 종료 | 플래그 사용 | 플래그와 추가 증감 코드 |
| 배열 순회 | 각 방식의 용도 메모 상세 | 핵심 동작 중심 |
| `map()`·`filter()` | 화살표 함수까지 확장 | 일반 함수와 화살표 함수 비교 |
| 피라미드 | 12단계 대부분 직접 구현 | 일부 단계와 추가 패턴 제공 |

## 53-1. 내 코드의 장점

- 반복문을 만드는 사고 과정을 구체적으로 기록했다.
- 주사위·주차장·배열 순회를 직접 확장했다.
- `forEach()`, `map()`, `filter()` 차이를 직접 확인했다.
- 피라미드 패턴을 여러 단계로 구현했다.

## 53-2. 내 코드의 개선점

- 배열에 `for...in`을 기본 순회 방식으로 권장하면 안 된다.
- `map()`을 출력만 하는 목적으로 사용하지 않아야 한다.
- `parseInt(Math.random() * 45)`보다 `Math.floor()`가 명확하다.
- 같은 문자열 반복은 `repeat()`로 단순화할 수 있다.
- 선언 키워드가 누락된 `k` 변수는 전역 오염을 만들 수 있다.
- 느슨한 비교보다 `===`를 사용해야 한다.

## 53-3. 강사님 코드의 장점

- 반복문 설계 원리를 직접 설명한다.
- 중첩 반복문으로 조합 문제를 단계적으로 보여 준다.
- 배열 순회 메서드의 전달인자와 반환값을 비교한다.
- 피라미드 패턴을 통해 행·열 규칙을 연습할 수 있다.

## 53-4. 강사님 코드의 보충점

- `for...in`의 배열 사용 주의가 필요하다.
- `sort()`가 원본을 변경한다는 설명이 필요하다.
- `forEach()` 중간 종료가 어렵다는 설명이 필요하다.
- 피라미드 문제는 `repeat()`를 함께 소개하면 규칙이 더 명확하다.

---

# 54. 기존 코드에서 개선 코드로 바꾼 이유

## 54-1. `i++`에서 `i += 1`

둘 다 가능하지만 팀 규칙에 따라 `+= 1`을 사용하면 변경량이 명확하다.

```text
for (
    let number = 1;
    number <= 5;
    number += 1
) {
```

## 54-2. 느슨한 비교 개선

기존:

```text
if (number % 2 == 0) {
```

개선:

```text
if (number % 2 === 0) {
```

## 54-3. 배열 값 순회 개선

기존:

```javascript
for (const index in numbers) {
    console.log(numbers[index])
}
```

개선:

```javascript
for (const number of numbers) {
    console.log(number)
}
```

## 54-4. 문자열 패턴 개선

기존:

```javascript
let line = ""

for (let i = 1; i <= 5; i += 1) {
    line += "+"
}
```

개선:

```javascript
const line = "+".repeat(5)
```

---

# 55. 실무형 예제: 주문 목록 집계

```javascript
const orders = [
    {
        id: 1,
        status: "paid",
        price: 45000,
    },
    {
        id: 2,
        status: "cancelled",
        price: 25000,
    },
    {
        id: 3,
        status: "paid",
        price: 70000,
    },
]

const paidOrders = orders.filter(
    order => order.status === "paid",
)

const paidPrices = paidOrders.map(
    order => order.price,
)

let totalPrice = 0

for (const price of paidPrices) {
    totalPrice += price
}

console.log(
    `결제 완료 주문: ${paidOrders.length}건`,
)

console.log(
    `총 결제 금액: ${totalPrice.toLocaleString()}원`,
)
```

## 55-1. 출력 결과

```text
결제 완료 주문: 2건
총 결제 금액: 115,000원
```

## 55-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `filter()` | 결제 완료 주문만 선택 |
| `map()` | 주문 객체에서 가격만 추출 |
| `for...of` | 가격 값을 직접 순회 |
| 누적 변수 | 총 결제 금액 계산 |
| `toLocaleString()` | 금액을 읽기 좋게 표시 |

---

# 56. 대표 오류로 이해하기

## 56-1. 종료되지 않는 반복

```javascript
for (let number = 1; number <= 5; number -= 1) {
    console.log(number)
}
```

종료 조건과 증감 방향이 맞지 않는다.

## 56-2. 선언하지 않은 반복 변수

```text
for (k = 1; k <= 5; k += 1) {
```

Strict mode에서 `ReferenceError`가 발생한다.

## 56-3. 배열에 `for...in` 사용 후 숫자 계산

인덱스가 문자열이므로 예상하지 못한 연결이 발생할 수 있다.

## 56-4. `forEach()` 반환값 기대

```javascript
const result = numbers.forEach(
    number => number * 2,
)
```

`result`는 `undefined`다.

## 56-5. `map()`에서 `return` 누락

결과 배열에 `undefined`가 들어간다.

## 56-6. `sort()` 원본 변경

복사 없이 정렬하면 기존 배열 순서도 바뀐다.

---

# 57. 자주 하는 실수

## 57-1. 조건식의 종료값 포함 여부 혼동

`<`와 `<=` 결과가 다르다.

## 57-2. 감소 반복에서 `++` 사용

종료 조건에서 멀어질 수 있다.

## 57-3. 누적 변수를 반복문 안에서 초기화

매 반복마다 0으로 돌아간다.

## 57-4. 중첩 반복 횟수를 예상하지 않음

바깥 횟수 × 안쪽 횟수만큼 실행된다.

## 57-5. 안쪽 `break`가 모든 반복문을 종료한다고 생각

가장 가까운 반복문만 종료한다.

## 57-6. `continue` 뒤 코드가 실행된다고 생각

현재 반복의 남은 코드는 건너뛴다.

## 57-7. 배열 값 순회에 `for...in` 사용

`for...of`를 우선 고려한다.

## 57-8. `forEach()`에서 `break` 사용

일반적인 중간 종료를 지원하지 않는다.

## 57-9. `map()`을 출력 전용으로 사용

변환 배열이 필요할 때 사용한다.

## 57-10. `filter()`에서 요소 자체를 반환해야 한다고 생각

Truthy/Falsy 조건을 반환하면 된다.

## 57-11. 숫자 배열을 비교 함수 없이 `sort()`

기본 정렬은 문자열 기준이다.

## 57-12. 피라미드 입력값 검증 누락

음수·문자·과도한 줄 수를 먼저 차단한다.

---

# 58. 핵심 요약

```text
for
→ 횟수와 인덱스 제어

break
→ 반복 종료

continue
→ 현재 반복 건너뜀
```

```text
for...in
→ 키 순회

for...of
→ 값 순회

forEach()
→ 각 요소에 작업 실행
→ 반환값 undefined
```

```text
map()
→ 변환한 새 배열

filter()
→ 조건을 만족한 새 배열

sort()
→ 원본 배열 정렬
```

```text
repeat()
→ 같은 문자열 반복

height - row
→ 공백 수

row * 2 - 1
→ 피라미드 기호 수
```

---

# 59. 최종 체크리스트

- [ ] `for`문의 초기화·조건·증감 순서를 설명할 수 있는가?
- [ ] 증가·감소 반복문을 작성할 수 있는가?
- [ ] 합계와 개수를 누적할 수 있는가?
- [ ] 중첩 반복문의 실행 횟수를 계산할 수 있는가?
- [ ] 구구단과 주사위 조합을 만들 수 있는가?
- [ ] 중복 조합 포함 여부를 결정할 수 있는가?
- [ ] `break`와 `continue`를 구분할 수 있는가?
- [ ] 중첩 반복문을 플래그나 함수 반환으로 종료할 수 있는가?
- [ ] 배열에서 `for...in`과 `for...of`를 구분할 수 있는가?
- [ ] 인덱스와 값을 `entries()`로 함께 순회할 수 있는가?
- [ ] `forEach()`의 전달인자를 설명할 수 있는가?
- [ ] `forEach()`가 `undefined`를 반환함을 이해했는가?
- [ ] `map()`으로 변환 배열을 만들 수 있는가?
- [ ] `filter()`로 조건에 맞는 배열을 만들 수 있는가?
- [ ] 숫자 배열을 비교 함수로 정렬할 수 있는가?
- [ ] `sort()`가 원본을 변경함을 이해했는가?
- [ ] `at(-1)`로 마지막 요소를 조회할 수 있는가?
- [ ] `repeat()`로 단순 문자열 패턴을 만들 수 있는가?
- [ ] 피라미드의 공백·기호 개수 공식을 설명할 수 있는가?
- [ ] 사용자 입력 줄 수를 검증할 수 있는가?
- [ ] 난수 중복을 `Set`으로 제거할 수 있는가?

---

# 마무리

반복문의 핵심은 같은 코드를 여러 번 실행하는 것에서 끝나지 않는다.

```text
반복되는 규칙을 찾고
    ↓
시작값과 종료 조건을 정확히 정하고
    ↓
필요한 값은 누적하거나 변환하고
    ↓
목적에 맞는 순회 방식을 선택하고
    ↓
읽기 쉬운 구조로 반복을 표현하는 것
```

이 흐름을 이해하면 이후 배열 메서드와 함수에서 데이터를 더 효율적으로 처리할 수 있다.
