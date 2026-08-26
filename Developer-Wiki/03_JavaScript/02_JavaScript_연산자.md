---
title: JavaScript 연산자
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# JavaScript 연산자

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `02_JavaScript_연산자.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/02_op.html`, `workspace_teacher/workspace_html/javascript/02_op.html` |
| 핵심 범위 | 산술 연산자, 증감 연산자, 전위·후위 연산, 논리 연산자, 비교 연산자, 엄격한 동등 비교, 삼항 조건 연산자 |
| 실습 범위 | 구매 가능 수량, 할인 가격, 자리수 버림, 소수점 처리, 화폐 분배 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 각 연산자의 동작을 이해하는 데 필요한 코드만 발췌하고, 실행 순서·반환값·형 변환·실무 개선 방향을 함께 설명한다.

---

# 개요

연산자는 값을 계산하고, 비교하고, 조건을 결합하는 기호다.

```text
숫자 계산
→ 산술 연산자

값 변경
→ 대입·증감 연산자

값 비교
→ 비교 연산자

여러 조건 결합
→ 논리 연산자

조건에 따라 값 선택
→ 삼항 조건 연산자
```

JavaScript에서는 같은 기호라도 값의 자료형과 위치에 따라 결과가 달라질 수 있다.

```javascript
console.log(1 + 2)
console.log("1" + 2)
```

출력:

```text
3
12
```

> [!IMPORTANT]
> 연산자는 단순히 계산 결과만 보는 것이 아니라 **평가 순서**, **반환값**, **암시적 형 변환**까지 함께 이해해야 한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 산술 연산자 | 숫자 계산 |
| 대입 연산자 | 계산 결과를 변수에 저장 |
| 복합 대입 연산자 | 기존 값과 계산 후 같은 변수에 저장 |
| 증감 연산자 | 값을 1 증가·감소 |
| 전위 연산 | 먼저 값을 변경한 뒤 사용 |
| 후위 연산 | 현재 값을 사용한 뒤 변경 |
| 비교 연산자 | 두 값을 비교해 Boolean 반환 |
| 느슨한 동등 비교 | 형 변환 후 값 비교 |
| 엄격한 동등 비교 | 형 변환 없이 값과 타입 비교 |
| 논리 연산자 | 여러 조건을 결합하거나 반전 |
| 삼항 조건 연산자 | 조건에 따라 두 값 중 하나 선택 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 기본 산술 연산자를 사용할 수 있다.
- 대입 연산자와 복합 대입 연산자를 구분할 수 있다.
- `++`, `--`의 전위·후위 차이를 설명할 수 있다.
- 복잡한 증감 표현식의 평가 순서를 추적할 수 있다.
- `&&`, `||`, `!`의 기본 동작을 설명할 수 있다.
- `==`와 `===`의 차이를 설명할 수 있다.
- 실무에서 엄격한 동등 비교를 우선 사용하는 이유를 이해한다.
- `typeof` 결과를 비교할 수 있다.
- 삼항 조건 연산자를 작성할 수 있다.
- 구매 수량과 남은 금액을 계산할 수 있다.
- 할인 가격을 계산할 수 있다.
- 자리수 버림을 계산할 수 있다.
- 소수점 이하 값을 자르거나 반올림할 수 있다.
- 큰 단위 화폐부터 나누어 지급하는 계산을 작성할 수 있다.

---

# 1. 산술 연산자

JavaScript의 대표적인 산술 연산자는 다음과 같다.

| 연산자 | 의미 | 예시 | 결과 |
| --- | --- | --- | --- |
| `+` | 덧셈 | `7 + 3` | `10` |
| `-` | 뺄셈 | `7 - 3` | `4` |
| `*` | 곱셈 | `7 * 3` | `21` |
| `/` | 나눗셈 | `7 / 3` | `2.333...` |
| `%` | 나머지 | `7 % 3` | `1` |
| `**` | 거듭제곱 | `2 ** 3` | `8` |

```javascript
console.log(7 + 3)
console.log(7 - 3)
console.log(7 * 3)
console.log(7 / 3)
console.log(7 % 3)
console.log(2 ** 3)
```

---

# 2. 기본 대입 연산자

```javascript
let value = 10
```

`=`는 오른쪽 값을 왼쪽 변수에 저장한다.

```text
10
→ value에 저장
```

> [!IMPORTANT]
> `=`는 같은지 비교하는 기호가 아니다.
>
> 값 비교에는 `==`, `===` 등을 사용한다.

---

# 3. 복합 대입 연산자

## 3-1. 원본 코드

```javascript
let j = 10

j = j + 1
j += 1
```

두 코드는 모두 기존 `j`에 1을 더한 뒤 다시 저장한다.

## 3-2. 실행

```javascript
let count = 10

count += 2
count *= 3

console.log(count)
```

## 3-3. 출력 결과

```text
36
```

계산 순서:

```text
10 + 2
→ 12

12 × 3
→ 36
```

---

# 4. 증감 연산자

증감 연산자는 숫자 값을 1 증가하거나 감소시킨다.

```javascript
let count = 10

count++
count--

console.log(count)
```

출력:

```text
10
```

| 연산자 | 의미 |
| --- | --- |
| `++` | 1 증가 |
| `--` | 1 감소 |

---

# 5. 후위 증가 `value++`

## 5-1. 원본 코드

```javascript
let k = 10

console.log("k++", k++)
console.log("k", k)
```

## 5-2. 출력 결과

```text
k++ 10
k 11
```

후위 증가는 현재 값을 먼저 사용하고 그 다음 값을 증가시킨다.

```text
k++ 평가
    ↓
현재 값 10 반환
    ↓
k를 11로 변경
```

---

# 6. 전위 증가 `++value`

## 6-1. 원본 코드

```javascript
let k = 10

console.log("++k", ++k)
console.log("k", k)
```

## 6-2. 출력 결과

```text
++k 11
k 11
```

전위 증가는 먼저 값을 증가시키고 변경된 값을 사용한다.

```text
++k 평가
    ↓
k를 11로 변경
    ↓
변경된 값 11 반환
```

---

# 7. 전위·후위 증가 비교

| 표현 | 반환값 | 연산 후 변수 |
| --- | ---: | ---: |
| `k++` (`k = 10`) | `10` | `11` |
| `++k` (`k = 10`) | `11` | `11` |

```javascript
let first = 10
let second = 10

const postResult = first++
const preResult = ++second

console.log(postResult, first)
console.log(preResult, second)
```

출력:

```text
10 11
11 11
```

---

# 8. 후위 증가가 포함된 계산

## 8-1. 원본 코드

```javascript
let k = 10
let m = k++ + 1

console.log(m)
console.log(k)
```

## 8-2. 출력 결과

```text
11
11
```

실행 순서:

```text
k++가 현재 값 10 반환
    ↓
10 + 1
    ↓
m = 11
    ↓
k는 11
```

---

# 9. 전위·후위 증가 혼합

## 9-1. 원본 코드

```javascript
let k = 10
let m = ++k + k++

console.log(`m: ${m}, k: ${k}`)
```

## 9-2. 출력 결과

```text
m: 22, k: 12
```

## 9-3. 평가 과정

```text
++k
→ k를 11로 변경
→ 11 반환

k++
→ 현재 값 11 반환
→ k를 12로 변경

m
→ 11 + 11
→ 22
```

---

# 10. 감소 연산 혼합

## 10-1. 원본 코드

```javascript
let k = 10
let m = k-- + ++k - --k

console.log(`m: ${m}, k: ${k}`)
```

## 10-2. 출력 결과

```text
m: 11, k: 9
```

## 10-3. 평가 과정

```text
k--
→ 10 반환
→ k = 9

++k
→ k = 10
→ 10 반환

--k
→ k = 9
→ 9 반환

m
→ 10 + 10 - 9
→ 11
```

> [!WARNING]
> 전위·후위 증감을 한 표현식에 여러 번 섞으면 읽기 어렵고 실수가 많아진다.
>
> 실무에서는 값을 단계별로 변경하고 의미 있는 변수에 저장하는 편이 좋다.

---

# 11. 복잡한 증감식 개선

기존:

```javascript
let k = 10
const m = k-- + ++k - --k
```

개선:

```javascript
let k = 10

const firstValue = k
k -= 1

k += 1
const secondValue = k

k -= 1
const thirdValue = k

const result = (
    firstValue
    + secondValue
    - thirdValue
)
```

코드가 길어지더라도 각 단계의 의도를 확인하기 쉽다.

---

# 12. 증감 연산자와 복합 대입

다음 세 코드는 값 자체를 1 증가시키는 목적에서는 비슷하다.

```javascript
count = count + 1
count += 1
count++
```

그러나 `count++`는 표현식의 반환값이 현재값 또는 변경값인지 구분해야 한다.

단순히 값을 증가시키는 목적이라면 다음 표현이 명확한 경우가 많다.

```javascript
count += 1
```

---

# 13. 논리 AND `&&`

## 13-1. 원본 코드

```javascript
const boolA = true
const boolB = false

const result = boolA && boolB

console.log("and:", result)
```

## 13-2. 출력 결과

```text
and: false
```

두 조건이 모두 참일 때만 `true`다.

| A | B | `A && B` |
| --- | --- | --- |
| `true` | `true` | `true` |
| `true` | `false` | `false` |
| `false` | `true` | `false` |
| `false` | `false` | `false` |

---

# 14. 논리 OR `||`

## 14-1. 원본 코드

```javascript
const result = boolA || boolB

console.log("or:", result)
```

## 14-2. 출력 결과

```text
or: true
```

한쪽이라도 참이면 `true`다.

| A | B | `A || B` |
| --- | --- | --- |
| `true` | `true` | `true` |
| `true` | `false` | `true` |
| `false` | `true` | `true` |
| `false` | `false` | `false` |

---

# 15. 논리 NOT `!`

## 15-1. 원본 코드

```javascript
console.log(!boolA)
console.log(!boolB)
```

## 15-2. 출력 결과

```text
false
true
```

`!`는 참·거짓을 반대로 바꾼다.

---

# 16. 논리 연산자는 Boolean만 반환할까?

JavaScript의 `&&`와 `||`는 항상 Boolean만 반환하는 것이 아니다.

```javascript
console.log("사용자" && "관리자")
console.log("" || "기본값")
```

출력:

```text
관리자
기본값
```

동작:

```text
A && B
→ A가 Falsy면 A
→ A가 Truthy면 B

A || B
→ A가 Truthy면 A
→ A가 Falsy면 B
```

이러한 동작은 단락 평가와 기본값 선택에 활용된다.

---

# 17. 단락 평가

```javascript
const user = null

const userName = (
    user
    && user.name
)

console.log(userName)
```

출력:

```text
null
```

첫 번째 값이 Falsy이므로 뒤의 `user.name`을 평가하지 않는다.

현대 JavaScript에서는 안전한 속성 접근에 선택적 체이닝도 사용할 수 있다.

```javascript
const userName = user?.name
```

---

# 18. 기본값과 `||`

```javascript
const inputName = ""
const displayName = (
    inputName || "익명"
)

console.log(displayName)
```

출력:

```text
익명
```

> [!WARNING]
> `0`, `false`, `""`도 Falsy이므로 정상 데이터까지 기본값으로 바뀔 수 있다.
>
> `null`과 `undefined`만 기본값 처리하려면 `??`를 검토한다.

---

# 19. Null 병합 연산자 `??`

```javascript
const count = 0

console.log(count || 10)
console.log(count ?? 10)
```

출력:

```text
10
0
```

| 연산자 | 기본값을 사용하는 조건 |
| --- | --- |
| `||` | 값이 Falsy |
| `??` | 값이 `null` 또는 `undefined` |

---

# 20. 느슨한 동등 비교 `==`

## 20-1. 원본 코드

```javascript
const n = 3
const o = "3"

console.log(n == o)
```

## 20-2. 출력 결과

```text
true
```

`==`는 필요하면 자료형을 변환한 뒤 값을 비교한다.

```text
3 == "3"
    ↓
문자열 "3"을 숫자처럼 변환
    ↓
3 == 3
    ↓
true
```

---

# 21. 느슨한 부등 비교 `!=`

```javascript
console.log(3 != "3")
```

출력:

```text
false
```

형 변환 후 값이 같다고 판단하기 때문이다.

---

# 22. 엄격한 동등 비교 `===`

## 22-1. 원본 코드

```javascript
console.log(n === o)
```

## 22-2. 출력 결과

```text
false
```

`===`는 암시적 형 변환 없이 값과 자료형을 비교한다.

```text
number 3
string "3"
→ 타입이 다름
→ false
```

---

# 23. 엄격한 부등 비교 `!==`

```javascript
console.log(3 !== "3")
```

출력:

```text
true
```

값 또는 자료형 중 하나라도 다르면 `true`다.

---

# 24. `==`와 `===` 비교

| 표현 | 결과 |
| --- | --- |
| `3 == "3"` | `true` |
| `3 === "3"` | `false` |
| `0 == false` | `true` |
| `0 === false` | `false` |
| `"" == false` | `true` |
| `"" === false` | `false` |
| `null == undefined` | `true` |
| `null === undefined` | `false` |

> [!IMPORTANT]
> 실무에서는 예상하지 못한 형 변환을 줄이기 위해 `===`, `!==`를 기본으로 사용한다.

---

# 25. `typeof` 비교

## 25-1. 원본 코드

```javascript
console.log(
    typeof o == "string",
)
```

출력:

```text
true
```

`typeof` 결과는 문자열이므로 다음처럼 비교한다.

```javascript
typeof o === "string"
```

엄격한 동등 비교를 사용하는 편이 일관적이다.

---

# 26. 크기 비교 연산자

| 연산자 | 의미 |
| --- | --- |
| `>` | 크다 |
| `<` | 작다 |
| `>=` | 크거나 같다 |
| `<=` | 작거나 같다 |

```javascript
const score = 85

console.log(score >= 80)
console.log(score < 60)
```

출력:

```text
true
false
```

---

# 27. 문자열 크기 비교

JavaScript 문자열은 유니코드 코드 단위 순서를 기준으로 비교한다.

```javascript
console.log("apple" < "banana")
```

출력:

```text
true
```

사용자 언어 기준 정렬에는 `localeCompare()`나 `Intl.Collator`를 검토한다.

---

# 28. 삼항 조건 연산자

## 28-1. 원본 코드

```javascript
let num = 2

const result = (
    num % 2 === 0
        ? "짝수"
        : "홀수"
)

console.log(result)
```

## 28-2. 출력 결과

```text
짝수
```

## 28-3. 기본 구조

```javascript
조건식 ? 참일_때_값 : 거짓일_때_값
```

---

# 29. 홀수 판별

```javascript
const num = 1

const result = (
    num % 2 === 0
        ? "짝수"
        : "홀수"
)

console.log(result)
```

출력:

```text
홀수
```

---

# 30. 삼항 연산자 사용 기준

적절한 예:

```javascript
const statusText = (
    isActive
        ? "활성"
        : "비활성"
)
```

복잡한 예:

```javascript
const grade = (
    score >= 90
        ? "A"
        : score >= 80
            ? "B"
            : score >= 70
                ? "C"
                : "F"
)
```

여러 조건이 중첩되면 `if·else`나 별도 함수가 더 읽기 쉽다.

---

# 31. 문제 1: 구매 가능 수량

## 31-1. 요구사항

```text
보유 금액
→ 10,000원

상품 가격
→ 4,800원

구할 값
→ 최대 구매 수량
→ 남는 금액
```

## 31-2. 내 코드

```javascript
const money = 10000
const price = 4800

console.log(
    `구매 가능: ${
        parseInt(money / price)
    }잔, 남는 돈: ${
        money % price
    }원`,
)
```

## 31-3. 강사님 코드

```javascript
const money = 10000
const price = 4800

console.log(
    parseInt(money / price),
)

console.log(
    money % price,
)
```

## 31-4. 출력 결과

```text
구매 가능: 2잔, 남는 돈: 400원
```

---

# 32. 구매 가능 수량 개선

숫자 계산 결과의 소수 부분을 제거하는 목적에는 `Math.trunc()` 또는 `Math.floor()`를 사용할 수 있다.

```javascript
const quantity = Math.floor(
    money / price,
)

const remainingMoney = (
    money % price
)

console.log(quantity)
console.log(remainingMoney)
```

양수 금액에서는 `Math.floor()`가 “최대 구매 수량”이라는 의미를 잘 표현한다.

---

# 33. 문제 2: 할인 가격

## 33-1. 요구사항

```text
정가
→ 8,000원

할인율
→ 15%

구할 값
→ 할인 후 가격
```

## 33-2. 원본 코드

```javascript
const price = 8000
const discountPercent = 15

const salePrice = (
    price
    - (
        price
        * discountPercent
        / 100
    )
)

console.log(salePrice)
```

## 33-3. 출력 결과

```text
6800
```

---

# 34. 할인 계산 과정

```text
할인 금액
→ 8,000 × 15 ÷ 100
→ 1,200

할인 후 가격
→ 8,000 - 1,200
→ 6,800
```

분리해서 작성하면 의미가 더 명확하다.

```javascript
const discountAmount = (
    price
    * discountPercent
    / 100
)

const salePrice = (
    price
    - discountAmount
)
```

---

# 35. 할인율 소수 표현

할인율을 소수로 저장할 수도 있다.

```javascript
const discountRate = 0.15

const salePrice = (
    price
    * (1 - discountRate)
)

console.log(salePrice)
```

출력:

```text
6800
```

프로젝트에서 할인율을 퍼센트 정수와 소수 중 어떤 방식으로 저장하는지 일관되게 정한다.

---

# 36. 문제 3: 10의 자리 이하 버림

## 36-1. 요구사항

```text
입력
→ 1234

10의 자리 이하 버림
→ 1200
```

원본 설명에서 “10의 자리 이하”라고 했지만 계산식은 100 단위 아래를 버려 1200을 만든다.

## 36-2. 원본 코드

```javascript
const value = 1234

const result = (
    parseInt(value / 100)
    * 100
)

console.log(result)
```

## 36-3. 출력 결과

```text
1200
```

---

# 37. 자리수 버림 개선

```javascript
const result = (
    Math.floor(value / 100)
    * 100
)
```

또는:

```javascript
const result = (
    value
    - (value % 100)
)
```

양수에서 둘 다 `1200`을 반환한다.

---

# 38. 음수 자리수 처리 주의

```javascript
console.log(
    Math.trunc(-1234 / 100)
    * 100,
)

console.log(
    Math.floor(-1234 / 100)
    * 100,
)
```

출력:

```text
-1200
-1300
```

| 함수 | 동작 |
| --- | --- |
| `Math.trunc()` | 0 방향으로 소수 부분 제거 |
| `Math.floor()` | 더 작은 정수 방향으로 내림 |

업무 규칙에서 말하는 “버림”이 어떤 방향인지 확인해야 한다.

---

# 39. 문제 4: 소수점 둘째 자리까지 자르기

## 39-1. 요구사항

```text
1000 ÷ 794
→ 1.259445...

소수점 둘째 자리까지 자르기
→ 1.25
```

## 39-2. 원본 코드

```javascript
const firstValue = 1000
const secondValue = 794

const result = (
    parseInt(
        firstValue
        / secondValue
        * 100,
    )
    / 100
)

console.log(result)
```

## 39-3. 출력 결과

```text
1.25
```

---

# 40. 소수점 자르기 개선

```javascript
const result = (
    Math.trunc(
        firstValue
        / secondValue
        * 100,
    )
    / 100
)
```

계산 과정:

```text
1000 / 794
→ 1.259445...

× 100
→ 125.9445...

Math.trunc()
→ 125

÷ 100
→ 1.25
```

---

# 41. 자르기와 반올림 구분

```javascript
const value = (
    1000 / 794
)

console.log(
    Math.trunc(value * 100) / 100,
)

console.log(
    Math.round(value * 100) / 100,
)

console.log(
    value.toFixed(2),
)
```

출력:

```text
1.25
1.26
1.26
```

| 방식 | 결과 | 자료형 |
| --- | --- | --- |
| `Math.trunc()` | 자르기 | Number |
| `Math.round()` | 반올림 | Number |
| `toFixed(2)` | 반올림 후 두 자리 표시 | String |

---

# 42. `toFixed()` 주의

```javascript
const result = (
    (1000 / 794).toFixed(2)
)

console.log(result)
console.log(typeof result)
```

출력:

```text
1.26
string
```

추가 계산이 필요하면 숫자로 다시 변환해야 한다.

```javascript
const numberResult = Number(result)
```

---

# 43. 문제 5: 화폐 분배

## 43-1. 요구사항

```text
지급 금액
→ 17,000원

사용 가능한 지폐
→ 5,000원
→ 1,000원

조건
→ 5,000원부터 최대한 많이 지급
```

## 43-2. 원본 코드

```javascript
const money = 17000

const fiveThousandCount = (
    parseInt(money / 5000)
)

const remainingMoney = (
    money % 5000
)

const oneThousandCount = (
    remainingMoney / 1000
)

console.log(
    `5천원: ${fiveThousandCount}장`,
)

console.log(
    `1천원: ${oneThousandCount}장`,
)
```

## 43-3. 출력 결과

```text
5천원: 3장
1천원: 2장
```

---

# 44. 화폐 분배 계산 과정

```text
17,000 ÷ 5,000
→ 3장

17,000 % 5,000
→ 2,000원

2,000 ÷ 1,000
→ 2장
```

큰 단위부터 나눈 뒤 나머지를 다음 단위로 넘긴다.

---

# 45. 화폐 분배 개선

```javascript
const totalMoney = 17000
const largeBill = 5000
const smallBill = 1000

const largeBillCount = Math.floor(
    totalMoney / largeBill,
)

const remainingMoney = (
    totalMoney % largeBill
)

const smallBillCount = Math.floor(
    remainingMoney / smallBill,
)
```

의미 있는 변수명과 `Math.floor()`를 사용하면 계산 목적이 분명해진다.

---

# 46. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 증감 연산 | 평가 과정을 상세 주석으로 기록 | 결과 예측 중심 |
| 전위·후위 혼합 | 직접 계산식과 설명 추가 | 빈칸으로 결과 추론 유도 |
| 논리 연산 | AND·OR·NOT 설명 추가 | 기본 실행 예제 |
| 동등 비교 | `==`, `!=`, `===`, `!==` 모두 확인 | 핵심 비교 중심 |
| 삼항 연산 | 짝수·홀수 두 경우 실행 | 짝수 예제 중심 |
| 문제 1 | 템플릿 리터럴로 결과 한 줄 출력 | 수량·나머지를 각각 출력 |
| 문제 3 | 한 줄 계산 | 중간 계산값을 단계별 변수로 분리 |
| 문제 5 | 최종 지폐 수량까지 출력 | 계산값만 변수에 저장 |

## 46-1. 내 코드의 장점

- 전위·후위 증감의 평가 순서를 상세히 기록했다.
- 문제 결과를 템플릿 리터럴로 읽기 좋게 출력했다.
- 짝수와 홀수 두 경우를 모두 직접 확인했다.
- 화폐 분배 문제를 최종 출력까지 완성했다.

## 46-2. 내 코드의 개선점

- 복잡한 증감식을 한 줄에 작성하면 가독성이 떨어진다.
- 숫자 계산의 소수 제거에 `parseInt()`를 사용하는 것은 목적이 불명확하다.
- 느슨한 동등 비교보다 엄격한 동등 비교를 우선 사용해야 한다.
- 문제 변수명에 `q1_`보다 역할이 드러나는 camelCase를 사용할 수 있다.
- 소수점 자르기와 반올림을 명확히 구분해야 한다.

## 46-3. 강사님 코드의 장점

- 증감 연산 결과를 직접 예측하도록 구성되어 있다.
- 자리수 버림 문제를 중간 단계별로 분리해 계산 흐름을 확인할 수 있다.
- 논리·비교·삼항 연산자를 하나의 흐름에서 학습할 수 있다.

## 46-4. 강사님 코드의 보충점

- `parseInt()`와 `Math.trunc()`의 역할 차이를 설명할 필요가 있다.
- `==`의 암시적 형 변환 위험을 보충할 필요가 있다.
- `&&`, `||`가 Boolean 외의 값을 반환할 수 있다는 설명이 필요하다.
- 화폐 분배 문제의 최종 출력 결과가 있으면 이해하기 쉽다.

---

# 47. 기존 코드에서 개선 코드로 바꾼 이유

## 47-1. 느슨한 비교에서 엄격한 비교로

기존:

```javascript
num % 2 == 0
```

개선:

```javascript
num % 2 === 0
```

이유:

- 암시적 형 변환을 방지한다.
- 값과 자료형이 모두 같은지 확인한다.
- 비교 의도가 더 명확하다.

## 47-2. `parseInt()`에서 `Math.floor()`로

기존:

```javascript
parseInt(
    money / price,
)
```

개선:

```javascript
Math.floor(
    money / price,
)
```

이유:

- 문자열 파싱 함수가 아니라 숫자 내림 함수다.
- 최대 구매 수량 계산 의도가 명확하다.

## 47-3. 문제 변수명 개선

기존:

```javascript
let q1_money = 10000
let q1_pay = 4800
```

개선:

```javascript
const availableMoney = 10000
const drinkPrice = 4800
```

---

# 48. 실무형 예제: 쿠폰 할인 계산

```javascript
const orderPrice = 85000
const couponPercent = 15
const maximumDiscount = 10000

const calculatedDiscount = (
    orderPrice
    * couponPercent
    / 100
)

const discountAmount = Math.min(
    calculatedDiscount,
    maximumDiscount,
)

const finalPrice = (
    orderPrice
    - discountAmount
)

const message = (
    finalPrice >= 50000
        ? "무료 배송"
        : "배송비 3,000원"
)

console.log(
    `할인 금액: ${
        discountAmount.toLocaleString()
    }원`,
)

console.log(
    `결제 금액: ${
        finalPrice.toLocaleString()
    }원`,
)

console.log(message)
```

## 48-1. 입력값

```text
주문 금액: 85,000원
쿠폰 할인율: 15%
최대 할인: 10,000원
```

## 48-2. 출력 결과

```text
할인 금액: 10,000원
결제 금액: 75,000원
무료 배송
```

## 48-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| 산술 연산 | 할인 금액과 결제 금액 계산 |
| `Math.min()` | 계산 할인액과 최대 할인액 중 작은 값 선택 |
| 엄격한 비교 | 무료 배송 기준 확인 |
| 삼항 연산자 | 간단한 배송 메시지 선택 |
| `toLocaleString()` | 천 단위 구분 기호 표시 |

---

# 49. 대표 오류로 이해하기

## 49-1. 대입과 비교 혼동

```javascript
let value = 10

if (value = 5) {
    console.log("실행")
}
```

`value`에 5가 대입되고 5가 Truthy이므로 블록이 실행된다.

개선:

```javascript
if (value === 5) {
    console.log("실행")
}
```

---

## 49-2. 느슨한 비교의 예상 밖 결과

```javascript
console.log(0 == false)
console.log("" == false)
```

출력:

```text
true
true
```

엄격한 비교를 사용하면 의도하지 않은 변환을 줄일 수 있다.

---

## 49-3. 삼항 연산자 콜론 누락

```text
const result = condition ? "참" "거짓"
```

발생 결과:

```text
SyntaxError
```

---

## 49-4. `toFixed()` 결과를 숫자로 생각

```javascript
const result = (
    1.234.toFixed(2)
)

console.log(result + 1)
```

출력:

```text
1.231
```

문자열 연결이 발생한다.

개선:

```javascript
Number(result) + 1
```

---

# 50. 자주 하는 실수

## 50-1. `=`를 비교 연산자로 사용

`=`는 대입이다.

## 50-2. 전위·후위 증감을 같은 반환값으로 이해

값 변경 시점과 반환값이 다르다.

## 50-3. 한 표현식에서 같은 변수를 여러 번 증감

평가 순서를 이해하기 어렵다.

## 50-4. `&&`, `||`가 항상 Boolean을 반환한다고 생각

피연산자 값을 반환할 수 있다.

## 50-5. `==`와 `===`를 같은 비교로 이해

`==`는 암시적 형 변환을 수행할 수 있다.

## 50-6. `typeof` 비교에도 `==` 사용

일관되게 `===`를 사용한다.

## 50-7. 삼항 연산자를 여러 단계 중첩

가독성이 떨어질 수 있다.

## 50-8. 숫자 소수 제거에 `parseInt()` 사용

숫자 계산에는 `Math.trunc()`·`Math.floor()`가 목적에 맞다.

## 50-9. 자르기와 반올림을 혼동

`Math.trunc()`와 `Math.round()`는 결과가 다르다.

## 50-10. `toFixed()`가 Number를 반환한다고 생각

String을 반환한다.

## 50-11. 할인율 계산에서 100으로 나누는 과정 누락

퍼센트 정수를 소수 비율로 바꾸어야 한다.

## 50-12. 나머지를 다음 화폐 단위로 넘기지 않음

큰 단위 계산 후 `%` 결과를 사용한다.

---

# 51. 핵심 요약

```text
+
-
*
/
%
**
→ 산술 연산
```

```text
+=
-=
*=
/=
→ 복합 대입
```

```text
value++
→ 현재 값 사용 후 증가

++value
→ 증가 후 변경값 사용
```

```text
&&
→ 모두 참

||
→ 하나라도 참 또는 첫 Truthy 값

!
→ 참·거짓 반전

??
→ null·undefined일 때 기본값
```

```text
==
→ 형 변환 후 값 비교

===
→ 형 변환 없이 값·타입 비교

!=
→ 느슨한 부등 비교

!==
→ 엄격한 부등 비교
```

```text
조건 ? 참값 : 거짓값
→ 삼항 조건 연산자
```

---

# 52. 최종 체크리스트

- [ ] 산술 연산자를 사용할 수 있는가?
- [ ] 대입과 비교를 구분할 수 있는가?
- [ ] 복합 대입 연산자를 사용할 수 있는가?
- [ ] 전위·후위 증감의 반환값을 설명할 수 있는가?
- [ ] 복잡한 증감식을 단계별 코드로 바꿀 수 있는가?
- [ ] `&&`, `||`, `!`의 기본 동작을 설명할 수 있는가?
- [ ] 단락 평가를 이해했는가?
- [ ] `||`와 `??`의 기본값 처리 차이를 설명할 수 있는가?
- [ ] `==`와 `===`의 차이를 설명할 수 있는가?
- [ ] 기본적으로 `===`, `!==`를 사용할 수 있는가?
- [ ] `typeof` 결과를 엄격하게 비교할 수 있는가?
- [ ] 삼항 조건 연산자를 작성할 수 있는가?
- [ ] 삼항 연산자의 과도한 중첩을 피할 수 있는가?
- [ ] 구매 가능 수량과 남은 금액을 계산할 수 있는가?
- [ ] 할인 금액과 할인 후 가격을 계산할 수 있는가?
- [ ] 자리수 버림을 계산할 수 있는가?
- [ ] 소수점 자르기와 반올림을 구분할 수 있는가?
- [ ] `toFixed()`가 문자열을 반환함을 이해했는가?
- [ ] 큰 화폐 단위부터 수량을 계산할 수 있는가?
- [ ] 계산 목적에 맞는 `Math` 메서드를 선택할 수 있는가?

---

# 마무리

연산자의 핵심은 기호를 외우는 것에서 끝나지 않는다.

```text
값의 자료형을 확인하고
    ↓
평가 순서와 반환값을 이해하고
    ↓
암시적 형 변환을 줄이며
    ↓
계산 목적에 맞는 연산자와 Math 메서드를 선택하고
    ↓
읽기 쉬운 코드로 결과를 표현하는 것
```

이 흐름을 이해하면 이후 조건문에서 비교식과 논리식을 더 안전하게 작성할 수 있다.
# V3 실행 추적 카드 — 피연산자 → 강제 변환 → 결과

연산자는 좌우 값의 자료형을 보고 계산하며 일부는 암묵적 형 변환을 일으킨다. 비교는 예측 가능한 `===`, `!==`를 기본으로 삼는다.

`console.log("5" + 1, "5" - 1, 5 === "5")`의 결과는 `51 4 false`다. 괄호로 우선순위를 명확히 하고 `NaN`은 `Number.isNaN()`으로 검사한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/02_op.html`에서 실제 사용 위치와 차이를 확인한다.
