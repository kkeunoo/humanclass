---
title: JavaScript 조건문과 Switch
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# JavaScript 조건문과 Switch

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `03_JavaScript_조건문과_Switch.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/03_if.html`, `workspace_teacher/workspace_html/javascript/03_if.html` |
| 핵심 범위 | 조건식, Truthy/Falsy, `if`, `else if`, `else`, 중첩 조건문, `switch`, 다중 `case`, 난수 범위, 입력값 검증 |
| 실습 범위 | 양수·음수, 홀수·짝수, 큰 수, 교통수단, 가위바위보, 범위 판정, 계절, 온도, 시간 계산, 369게임, 좌표 판정 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 조건문을 이해하는 데 필요한 핵심 코드와 문제 풀이만 발췌하고, 실행 순서·오류 원인·입력값 검증·실무 개선 방향을 함께 설명한다.

---

# 개요

조건문은 프로그램이 상황에 따라 다른 코드를 실행하도록 만든다.

```text
조건 확인
    ↓
참이면 한 경로 실행
    ↓
거짓이면 다른 경로 실행
```

예를 들어 다음 판단에 사용한다.

- 점수가 합격 기준 이상인지
- 입력한 값이 올바른지
- 선택한 상품이 존재하는지
- 사용자가 이겼는지 졌는지
- 특정 범위 안에 좌표가 들어오는지

```javascript
const score = 85

if (score >= 60) {
    console.log("합격")
} else {
    console.log("불합격")
}
```

출력:

```text
합격
```

> [!IMPORTANT]
> 조건문은 단순히 `true`와 `false`를 확인하는 문법이 아니다.
>
> 입력값을 검증하고, 실행 경로를 결정하며, 잘못된 상태를 차단하는 핵심 제어문이다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 조건식 | 참·거짓으로 평가되는 표현식 |
| `if` | 조건이 참일 때 실행 |
| `else if` | 앞 조건이 거짓일 때 추가 조건 검사 |
| `else` | 모든 앞 조건이 거짓일 때 실행 |
| 실행 블록 | 중괄호 `{}`로 묶은 코드 영역 |
| Truthy/Falsy | 값을 참 또는 거짓처럼 평가하는 규칙 |
| 중첩 조건문 | 조건문 안에 다른 조건문 작성 |
| `switch` | 하나의 값을 여러 고정값과 비교 |
| `case` | `switch`에서 비교할 값 |
| `break` | 현재 `switch` 또는 반복문 종료 |
| `default` | 어떤 `case`에도 맞지 않을 때 실행 |
| 단락 평가 | 결과가 정해지면 뒤 조건을 평가하지 않음 |
| 입력값 검증 | 변환 가능 여부와 범위를 먼저 확인 |
| 난수 | `Math.random()`으로 생성한 임의의 값 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 조건식의 결과가 Boolean으로 평가됨을 이해한다.
- `if`, `else if`, `else`의 실행 순서를 설명할 수 있다.
- `!`를 이용해 조건을 반전할 수 있다.
- Truthy/Falsy 값을 구분할 수 있다.
- 빈 문자열이 Falsy라는 점을 이해한다.
- 실행 블록의 중괄호를 일관되게 작성할 수 있다.
- 중첩 조건문을 `else if`로 단순화할 수 있다.
- 조건 순서가 결과에 미치는 영향을 설명할 수 있다.
- `switch`, `case`, `break`, `default`를 사용할 수 있다.
- 여러 `case`를 하나의 실행 블록으로 묶을 수 있다.
- `==`보다 `===`를 우선 사용할 수 있다.
- `prompt()` 결과를 숫자로 변환하고 검증할 수 있다.
- `Number.isNaN()`으로 숫자 변환 실패를 확인할 수 있다.
- `Math.random()`의 범위를 설명할 수 있다.
- 임의의 정수 범위를 생성할 수 있다.
- 범위 조건에서 `x < z && z < y` 형태를 사용할 수 있다.
- 여러 조건문 문제를 입력·검증·판정·출력 단계로 나누어 해결할 수 있다.

---

# 1. 기본 `if`

## 1-1. 내 코드와 강사님 코드

```javascript
let value = false

if (!value) {
    console.log("이거 true임")
}
```

## 1-2. 출력 결과

```text
이거 true임
```

`value`는 `false`지만 `!value`는 `true`가 된다.

## 1-3. 구성

| 요소 | 의미 |
| --- | --- |
| `if` | 조건문 시작 |
| `!value` | `value`의 참·거짓 반전 |
| `{}` | 조건이 참일 때 실행할 블록 |
| `console.log()` | 결과 확인 |

---

# 2. 조건이 참일 때만 실행

```javascript
const value = true

if (value) {
    console.log("참")
}
```

출력:

```text
참
```

조건이 `false`면 블록을 건너뛴다.

---

# 3. 서로 반대인 두 개의 `if`

## 3-1. 원본 코드

```javascript
let value2 = true

if (value2) {
    console.log("참")
}

if (!value2) {
    console.log("거짓")
}
```

## 3-2. 출력 결과

```text
참
```

두 조건은 서로 반대지만 각각 독립적으로 검사된다.

```text
첫 번째 if 검사
    ↓
두 번째 if도 별도로 검사
```

---

# 4. `if·else`

## 4-1. 원본 코드

```javascript
let value3 = true

if (value3) {
    console.log("참")
} else {
    console.log("거짓")
}
```

## 4-2. 출력 결과

```text
참
```

`if`가 참이면 `else`는 검사하지 않는다.

> [!TIP]
> 두 조건이 정확히 서로 반대라면 독립된 `if` 두 개보다 `if·else`가 의도를 더 명확하게 표현한다.

---

# 5. 합격 판정

## 5-1. 원본 코드

```javascript
const score = 85

if (score >= 60) {
    console.log("합격")
} else {
    console.log("불합격")
}
```

## 5-2. 출력 결과

```text
합격
```

## 5-3. 반대 조건

다음 두 조건은 같은 의미다.

```javascript
score < 60
```

```javascript
!(score >= 60)
```

첫 번째 표현이 더 직접적으로 읽힌다.

---

# 6. 조건식은 Boolean으로 평가된다

```javascript
const score = 85
const isPassed = score >= 60

console.log(isPassed)
```

출력:

```text
true
```

비교 연산식의 결과를 변수에 저장할 수 있다.

```javascript
if (isPassed) {
    console.log("합격")
}
```

---

# 7. 실행 블록

원본 주석에는 `{}`로 감싼 곳을 실행 블록이라고 설명한다.

```javascript
if (score >= 60) {
    console.log("합격")
    console.log("다음 단계로 이동합니다.")
}
```

같은 중괄호 안의 문장은 하나의 블록으로 처리된다.

---

# 8. 중괄호 생략

## 8-1. 원본 코드

```javascript
if (true)
    console.log(1)
```

한 문장만 있을 때 중괄호를 생략할 수 있다.

## 8-2. 위험한 예

```javascript
if (isLoggedIn)
    console.log("로그인됨")
    showDashboard()
```

들여쓰기만 보면 두 문장 모두 조건문 안처럼 보이지만 실제로는 `console.log()`만 조건부 실행이다.

## 8-3. 권장

```javascript
if (isLoggedIn) {
    console.log("로그인됨")
    showDashboard()
}
```

> [!IMPORTANT]
> 실무에서는 한 줄이어도 중괄호를 사용하는 편이 수정과 코드 리뷰에 안전하다.

---

# 9. 최소값 보정

## 9-1. 원본 코드

```javascript
let age = 17

if (age < 18) {
    age = 18
}

console.log(age)
```

## 9-2. 출력 결과

```text
18
```

한 줄로 작성할 수 있지만 블록을 사용하는 편이 명확하다.

```javascript
if (age < 18) {
    age = 18
}
```

같은 목적에는 다음도 사용할 수 있다.

```javascript
age = Math.max(age, 18)
```

---

# 10. 중첩 조건문

## 10-1. 원본 코드

```javascript
const score = 85

if (score >= 90) {
    console.log("A")
} else {
    if (score >= 80) {
        console.log("B")
    } else {
        console.log("C")
    }
}
```

## 10-2. 출력 결과

```text
B
```

## 10-3. 실행 순서

```text
90 이상?
    ↓ 아니오
80 이상?
    ↓ 예
B 출력
```

---

# 11. `else if`로 단순화

```javascript
const score = 85

if (score >= 90) {
    console.log("A")
} else if (score >= 80) {
    console.log("B")
} else if (score >= 70) {
    console.log("C")
} else {
    console.log("D")
}
```

출력:

```text
B
```

중첩 `if`보다 실행 흐름이 평평하게 보인다.

---

# 12. 조건 순서의 중요성

잘못된 순서:

```javascript
const score = 95

if (score >= 70) {
    console.log("C 이상")
} else if (score >= 90) {
    console.log("A")
}
```

출력:

```text
C 이상
```

첫 조건이 이미 참이므로 뒤 조건을 검사하지 않는다.

개선:

```javascript
if (score >= 90) {
    console.log("A")
} else if (score >= 70) {
    console.log("C 이상")
}
```

> [!IMPORTANT]
> 범위가 겹치는 조건은 더 구체적이고 높은 기준부터 작성한다.

---

# 13. Truthy와 Falsy

원본에는 다음 값이 Falsy라고 정리되어 있다.

```text
false
0
undefined
null
NaN
```

JavaScript에서는 다음 값도 Falsy다.

```text
""
0n
-0
```

대표 Falsy 값:

```javascript
const values = [
    false,
    0,
    -0,
    0n,
    "",
    null,
    undefined,
    NaN,
]

for (const value of values) {
    console.log(Boolean(value))
}
```

모두 `false`가 출력된다.

---

# 14. Truthy 값

Falsy가 아닌 대부분의 값은 Truthy다.

```javascript
const values = [
    true,
    1,
    -1,
    "0",
    "false",
    [],
    {},
]

for (const value of values) {
    console.log(Boolean(value))
}
```

모두 `true`다.

> [!WARNING]
> 빈 배열 `[]`과 빈 객체 `{}`도 Truthy다.
>
> Python의 빈 리스트·딕셔너리와 동작이 다르다.

---

# 15. Boolean 변환

```javascript
console.log(Boolean(""))
console.log(Boolean("JavaScript"))
console.log(Boolean(0))
console.log(Boolean(1))
```

출력:

```text
false
true
false
true
```

조건식 내부에서는 JavaScript가 같은 방식으로 값을 Boolean처럼 평가한다.

---

# 16. 과일 분기

## 16-1. 원본 코드

```javascript
const fruit = "apple"

if (fruit === "apple") {
    console.log("사과")
} else if (fruit === "banana") {
    console.log("바나나")
} else {
    console.log("알 수 없음")
}
```

## 16-2. 출력 결과

```text
사과
```

원본은 `==`를 사용하지만 실무 기준으로 `===`를 우선 사용한다.

---

# 17. `switch` 기본 구조

```javascript
switch (fruit) {
    case "apple":
        console.log("사과")
        break
    case "banana":
        console.log("바나나")
        break
    default:
        console.log("알 수 없음")
}
```

## 17-1. 구성

| 요소 | 의미 |
| --- | --- |
| `switch (fruit)` | 비교 대상 |
| `case "apple"` | 일치 여부 확인 |
| `break` | `switch` 종료 |
| `default` | 어떤 경우에도 일치하지 않을 때 |

---

# 18. `switch`는 엄격하게 비교한다

`switch`의 `case` 비교는 엄격한 동등 비교와 유사하게 동작한다.

```javascript
const value = 1

switch (value) {
    case "1":
        console.log("문자열")
        break
    case 1:
        console.log("숫자")
        break
}
```

출력:

```text
숫자
```

---

# 19. `break`가 필요한 이유

```javascript
const fruit = "apple"

switch (fruit) {
    case "apple":
        console.log("사과")
    case "banana":
        console.log("바나나")
    default:
        console.log("알 수 없음")
}
```

출력:

```text
사과
바나나
알 수 없음
```

`break`가 없으면 일치한 `case` 이후의 코드가 계속 실행된다.

이를 fall-through라고 한다.

---

# 20. 여러 `case` 묶기

## 20-1. 원본 코드

```javascript
const phone = "s23"

switch (phone) {
    case "s23":
    case "s24":
    case "s25":
    case "s26":
        console.log("삼성")
        break
    case "i15":
    case "i16":
    case "i17":
        console.log("애플")
        break
    default:
        console.log("삼성, 애플 아님")
}
```

## 20-2. 출력 결과

```text
삼성
```

여러 `case`가 같은 코드를 실행하도록 묶을 수 있다.

> [!NOTE]
> 내 코드 원본의 iPhone 분기에서 `"삼성"`을 출력하는 부분은 오타이므로 `"애플"`로 수정해야 한다.

---

# 21. `if`와 `switch` 선택 기준

| 상황 | 적합한 방식 |
| --- | --- |
| 범위 비교 | `if·else if` |
| 복잡한 논리 조건 | `if·else if` |
| 하나의 값을 여러 고정값과 비교 | `switch` |
| 단순 키와 결과 매핑 | 객체·`Map` 검토 |
| 분기마다 복잡한 동작 | 함수 분리 검토 |

`switch`가 항상 더 좋은 것은 아니다.

---

# 22. 객체를 이용한 단순 매핑

```javascript
const fruitNames = {
    apple: "사과",
    banana: "바나나",
}

const fruit = "apple"

console.log(
    fruitNames[fruit] ?? "알 수 없음",
)
```

출력:

```text
사과
```

값과 결과만 단순하게 연결할 때 객체가 더 간결할 수 있다.

---

# 23. 문제 해결 기본 흐름

조건문 문제는 다음 순서로 나누면 이해하기 쉽다.

| 단계 | 작업 |
| --- | --- |
| 1 | 입력값 받기 |
| 2 | 필요한 자료형으로 변환 |
| 3 | 변환 성공 여부 검사 |
| 4 | 허용 범위 검사 |
| 5 | 조건에 따라 결과 계산 |
| 6 | 사용자에게 결과 출력 |

> [!IMPORTANT]
> 원본 문제 중 일부는 문자열과 숫자의 암시적 형 변환에 의존한다.
>
> 실제 코드에서는 먼저 `Number()`로 변환하고 `Number.isNaN()`으로 검증하는 것이 안전하다.

---

# 24. 문제 1: 양수·0·음수 판정

## 24-1. 요구사항

```text
숫자 입력
→ 양수
→ 0
→ 음수
```

## 24-2. 개선 코드

```javascript
const input = "10"
const number = Number(input)

if (Number.isNaN(number)) {
    console.log("숫자만 입력해주세요.")
} else if (number > 0) {
    console.log("양수입니다.")
} else if (number === 0) {
    console.log("0입니다.")
} else {
    console.log("음수입니다.")
}
```

## 24-3. 출력 결과

```text
양수입니다.
```

원본 요구사항에는 0을 양수로 처리한다는 메모도 있으므로, 요구사항에 따라 다음처럼 작성할 수도 있다.

```javascript
if (number >= 0) {
    console.log("0 또는 양수입니다.")
}
```

---

# 25. 문제 2: 홀수·짝수

## 25-1. 원본 코드의 문제

```javascript
if (result % 2 == 0) {
    console.log("짝수")
} else if (!result % 2 == 0) {
    console.log("홀수")
}
```

`!result % 2 == 0`은 연산자 우선순위 때문에 의도대로 읽히지 않는다.

## 25-2. 개선 코드

```javascript
const input = "7"
const number = Number(input)

if (
    Number.isNaN(number)
    || !Number.isInteger(number)
) {
    console.log("정수를 입력해주세요.")
} else if (number % 2 === 0) {
    console.log("짝수입니다.")
} else {
    console.log("홀수입니다.")
}
```

## 25-3. 출력 결과

```text
홀수입니다.
```

---

# 26. 문제 3: 두 수 중 큰 값

```javascript
const first = 3
const second = 5

if (first > second) {
    console.log(`큰 수: ${first}`)
} else if (first < second) {
    console.log(`큰 수: ${second}`)
} else {
    console.log("두 수가 같습니다.")
}
```

출력:

```text
큰 수: 5
```

단순한 최대값은 다음처럼 계산할 수도 있다.

```javascript
console.log(
    Math.max(first, second),
)
```

---

# 27. 문제 4: 교통수단 선택

## 27-1. 요구사항

```text
7,000원 이상
→ 택시

3,000원 이상 7,000원 미만
→ 버스

3,000원 미만
→ 도보
```

## 27-2. 코드

```javascript
const money = 6500

if (money >= 7000) {
    console.log("택시타자")
} else if (money >= 3000) {
    console.log("버스타자")
} else {
    console.log("걸어가자")
}
```

## 27-3. 출력 결과

```text
버스타자
```

앞 조건에서 7,000원 이상이 걸러졌으므로 두 번째 조건에는 `money < 7000`을 다시 작성할 필요가 없다.

---

# 28. 문제 5-1: 컴퓨터가 항상 바위

```javascript
const userChoice = "보"
const computerChoice = "바위"

if (userChoice === computerChoice) {
    console.log("비겼습니다.")
} else if (userChoice === "보") {
    console.log("이겼습니다.")
} else if (userChoice === "가위") {
    console.log("졌습니다.")
} else {
    console.log("가위·바위·보만 입력해주세요.")
}
```

출력:

```text
이겼습니다.
```

---

# 29. 문제 5-2: 무작위 가위바위보

## 29-1. 컴퓨터 선택

```javascript
const choices = [
    "가위",
    "바위",
    "보",
]

const randomIndex = Math.floor(
    Math.random() * choices.length,
)

const computerChoice = (
    choices[randomIndex]
)
```

`parseInt(Math.random() * 10) % 3`보다 배열 길이를 직접 사용하는 방식이 분포와 의도를 이해하기 쉽다.

---

# 30. 가위바위보 승패 판정

```javascript
const userChoice = "가위"

const isValidChoice = (
    choices.includes(userChoice)
)

if (!isValidChoice) {
    console.log(
        "가위·바위·보만 입력해주세요.",
    )
} else if (
    userChoice === computerChoice
) {
    console.log("비겼습니다.")
} else if (
    (
        userChoice === "가위"
        && computerChoice === "보"
    )
    || (
        userChoice === "바위"
        && computerChoice === "가위"
    )
    || (
        userChoice === "보"
        && computerChoice === "바위"
    )
) {
    console.log("이겼습니다.")
} else {
    console.log("졌습니다.")
}
```

> [!TIP]
> 가능한 입력값 검증을 승패 판정보다 먼저 수행하면 이후 조건이 단순해진다.

---

# 31. 문제 6: 세 번째 수가 두 수 사이인지

## 31-1. 원본 문제

```text
x, y, z 입력
→ z가 x와 y 사이인지 판단
```

## 31-2. 순서를 모를 때

```javascript
const x = 10
const y = 30
const z = 20

const minValue = Math.min(x, y)
const maxValue = Math.max(x, y)

const isBetween = (
    z > minValue
    && z < maxValue
)

console.log(isBetween)
```

출력:

```text
true
```

---

# 32. 경계값 포함 여부

경계값까지 “사이”로 인정한다면:

```javascript
const isInside = (
    z >= minValue
    && z <= maxValue
)
```

경계값을 제외한다면:

```javascript
const isInside = (
    z > minValue
    && z < maxValue
)
```

요구사항에서 경계 포함 여부를 먼저 확인해야 한다.

---

# 33. 문제 7: 월별 계절

## 33-1. `switch` 풀이

```javascript
const month = 8

switch (month) {
    case 12:
    case 1:
    case 2:
        console.log("겨울")
        break
    case 3:
    case 4:
    case 5:
        console.log("봄")
        break
    case 6:
    case 7:
    case 8:
        console.log("여름")
        break
    case 9:
    case 10:
    case 11:
        console.log("가을")
        break
    default:
        console.log(
            "1부터 12까지 입력해주세요.",
        )
}
```

출력:

```text
여름
```

---

# 34. 문자열과 숫자 `case`

`prompt()` 결과는 문자열이다.

```javascript
const monthText = "8"
```

다음 두 방식 중 하나로 통일해야 한다.

숫자로 변환:

```javascript
const month = Number(monthText)
```

문자열 `case` 사용:

```text
case "8":
```

실무에서는 숫자 범위 검증을 위해 `Number()`로 변환하는 편이 자연스럽다.

---

# 35. 문제 8: 영상·영하 온도

## 35-1. 원본 코드의 문제

원본은 음수값을 그대로 출력해 다음처럼 보일 수 있다.

```text
영하 -3도
```

일반적으로는 부호를 제거해 출력한다.

## 35-2. 개선 코드

```javascript
const temperature = -3

if (temperature >= 0) {
    console.log(
        `영상 ${temperature}도입니다.`,
    )
} else {
    console.log(
        `영하 ${Math.abs(temperature)}도입니다.`,
    )
}
```

## 35-3. 출력 결과

```text
영하 3도입니다.
```

---

# 36. 온도 입력 검증

```javascript
const input = "-3"
const temperature = Number(input)

if (Number.isNaN(temperature)) {
    console.log("숫자를 입력해주세요.")
} else if (
    temperature < -50
    || temperature > 50
) {
    console.log("온도 범위를 확인해주세요.")
} else if (temperature >= 0) {
    console.log(
        `영상 ${temperature}도입니다.`,
    )
} else {
    console.log(
        `영하 ${Math.abs(temperature)}도입니다.`,
    )
}
```

---

# 37. 문제 9: 35분 후 시간

## 37-1. 입력값

```text
3시 51분
```

## 37-2. 코드

```javascript
let hour = 3
let minute = 51

minute += 35

if (minute >= 60) {
    hour += Math.floor(
        minute / 60,
    )

    minute %= 60
}

if (hour >= 24) {
    hour %= 24
}

console.log(
    `${hour}시 ${minute}분`,
)
```

## 37-3. 출력 결과

```text
4시 26분
```

---

# 38. 시간 계산 일반화

원본의 `minute >= 25` 분기는 35분 추가에만 맞춘 방식이다.

다음 방식은 추가 시간이 달라져도 사용할 수 있다.

```javascript
const addedMinutes = 95

minute += addedMinutes

hour += Math.floor(
    minute / 60,
)

minute %= 60
hour %= 24
```

---

# 39. 문제 10: 두 자리 숫자의 각 자리 비교

```javascript
const number = 88

if (
    !Number.isInteger(number)
    || number < 10
    || number > 99
) {
    console.log(
        "10부터 99까지 입력해주세요.",
    )
} else {
    const tens = Math.floor(
        number / 10,
    )

    const ones = number % 10

    if (tens === ones) {
        console.log("같음")
    } else {
        console.log("다름")
    }
}
```

출력:

```text
같음
```

`11`로 나누어떨어지는지 검사하는 방식도 가능하지만, 자리값을 직접 구하면 문제 의도가 더 명확하다.

---

# 40. 문제 11: 369게임

## 40-1. 두 자리 숫자 방식

```javascript
const number = 31

const tens = Math.floor(
    number / 10,
)

const ones = number % 10

const hasClapNumber = (
    [3, 6, 9].includes(tens)
    || [3, 6, 9].includes(ones)
)

console.log(
    hasClapNumber
        ? "박수"
        : number,
)
```

출력:

```text
박수
```

---

# 41. 문자열 방식의 369게임

자리수가 늘어나도 처리하려면 문자열로 검사할 수 있다.

```javascript
const number = 3693
const text = String(number)

const clapCount = [
    ...text,
].filter(
    digit => (
        digit === "3"
        || digit === "6"
        || digit === "9"
    ),
).length

console.log(
    clapCount > 0
        ? "박수 ".repeat(clapCount).trim()
        : number,
)
```

출력:

```text
박수 박수 박수 박수
```

---

# 42. 문제 12: 좌표가 사각형 안에 있는지

## 42-1. 조건

```text
좌상단
→ x1 = 10, y1 = 20

우하단
→ x2 = 90, y2 = 100

경계선 포함
```

## 42-2. 코드

```javascript
const x1 = 10
const y1 = 20
const x2 = 90
const y2 = 100

const pointX = 50
const pointY = 80

const isInside = (
    pointX >= x1
    && pointX <= x2
    && pointY >= y1
    && pointY <= y2
)

console.log(isInside)
```

출력:

```text
true
```

---

# 43. JavaScript의 연속 비교 주의

## 43-1. 원본 메모

```javascript
const a = 10

// 잘못된 방식
// if (3 < a < 20) {
```

JavaScript에서는 다음 식을 수학식처럼 해석하지 않는다.

```javascript
3 < a < 20
```

평가 과정:

```text
3 < 10
→ true

true < 20
→ 1 < 20
→ true
```

## 43-2. 올바른 코드

```javascript
if (
    3 < a
    && a < 20
) {
    console.log("범위 안")
}
```

---

# 44. `Math.random()`

## 44-1. 원본 코드

```javascript
const randomValue = Math.random()

console.log(randomValue)
```

`Math.random()`은 다음 범위의 난수를 반환한다.

```text
0 이상
1 미만
```

```text
0 <= value < 1
```

---

# 45. 0부터 2까지 난수

원본:

```javascript
parseInt(
    Math.random() * 10,
) % 3
```

더 직접적인 방식:

```javascript
const randomNumber = Math.floor(
    Math.random() * 3,
)
```

가능한 결과:

```text
0
1
2
```

---

# 46. 최소값·최대값 범위 난수

## 46-1. 원본 공식

```javascript
const min = 5
const max = 8

const randomNumber = Math.floor(
    Math.random()
    * (max - min + 1),
) + min
```

## 46-2. 가능한 결과

```text
5
6
7
8
```

## 46-3. 공식

```text
Math.floor(
    Math.random()
    × (최대값 - 최소값 + 1)
)
+ 최소값
```

---

# 47. 난수 함수로 분리

```javascript
function getRandomInteger(
    min,
    max,
) {
    return Math.floor(
        Math.random()
        * (max - min + 1),
    ) + min
}

console.log(
    getRandomInteger(5, 8),
)
```

반복되는 난수 공식을 함수로 분리하면 재사용과 테스트가 쉬워진다.

---

# 48. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기본 조건문 | 설명 주석을 상세히 추가 | 핵심 실행 코드 중심 |
| Falsy | 5개 값으로 정리 | 동일 |
| 중괄호 생략 | 사용 가능하나 가독성 주의 설명 | 한 줄 예제 |
| `switch` | 휴대폰·계절 문제까지 확장 | 기본 과일·휴대폰 예제 |
| 문제 풀이 | 1~12번 대부분 직접 구현 | 문제 요구사항 중심 |
| 가위바위보 | 난수와 승패 조건 직접 작성 | 도전 문제로 제시 |
| 시간 계산 | 35분 전용 조건식 작성 | 일반화된 참고 코드 제공 |
| 난수 | 범위 공식과 테스트값 추가 | 기본 공식 중심 |

## 48-1. 내 코드의 장점

- 문제 풀이 과정을 상세한 주석과 함께 직접 작성했다.
- 가위바위보·계절·시간 계산·369게임까지 확장했다.
- 입력값을 `Number()`로 변환해야 하는 이유를 기록했다.
- 범위 난수 공식과 연속 비교의 문제를 직접 확인했다.

## 48-2. 내 코드의 개선점

- 숫자 입력 검증에 `Number.isNaN()`을 먼저 사용해야 한다.
- `!result % 2 == 0`은 우선순위 때문에 의도대로 동작하지 않는다.
- `prompt()` 문자열과 숫자의 암시적 비교에 의존하지 않는 것이 좋다.
- iPhone `case`에서 `"삼성"`을 출력하는 오타를 수정해야 한다.
- 시간 계산은 특정 35분에만 맞춘 분기보다 나눗셈과 나머지로 일반화할 수 있다.
- 영하 온도 출력에는 `Math.abs()`를 사용해 부호를 제거하는 것이 자연스럽다.

## 48-3. 강사님 코드의 장점

- `if`, 중첩 조건문, `else if`, `switch` 흐름이 단계적으로 이어진다.
- 문제를 직접 풀 수 있도록 요구사항을 명확하게 제시한다.
- 난수 생성과 JavaScript 연속 비교의 차이를 함께 설명한다.
- 시간 계산 참고 코드가 일반적인 분·시간 보정 구조를 보여 준다.

## 48-4. 강사님 코드의 보충점

- Truthy/Falsy에서 빈 문자열과 BigInt 0도 추가 설명할 수 있다.
- 입력값 검증 예제가 있으면 문제 풀이 안정성이 높아진다.
- `switch`가 엄격 비교를 사용한다는 설명이 필요하다.
- 난수에 `%`를 사용하는 방식보다 `Math.floor()` 범위 공식을 권장할 수 있다.

---

# 49. 기존 코드에서 개선 코드로 바꾼 이유

## 49-1. `==`에서 `===`로

기존:

```text
if (fruit == "apple") {
```

개선:

```text
if (fruit === "apple") {
```

이유:

- 암시적 형 변환을 막는다.
- 값과 타입이 모두 같은지 확인한다.

## 49-2. 문자열 입력 먼저 변환

기존:

```text
const money = prompt(
    "금액을 입력하세요.",
)

if (money >= 7000) {
```

개선:

```text
const money = Number(
    prompt("금액을 입력하세요."),
)

if (Number.isNaN(money)) {
    console.log("숫자를 입력해주세요.")
} else if (money >= 7000) {
```

## 49-3. 연속 비교 개선

기존:

```javascript
3 < value < 20
```

개선:

```javascript
3 < value
&& value < 20
```

## 49-4. 난수 계산 개선

기존:

```javascript
parseInt(
    Math.random() * 10,
) % 3
```

개선:

```javascript
Math.floor(
    Math.random() * 3,
)
```

---

# 50. 실무형 예제: 회원 등급 판정

```javascript
function getMemberGrade(
    purchaseAmount,
) {
    if (
        !Number.isFinite(
            purchaseAmount,
        )
        || purchaseAmount < 0
    ) {
        return "잘못된 금액"
    }

    if (purchaseAmount >= 1000000) {
        return "VIP"
    }

    if (purchaseAmount >= 500000) {
        return "GOLD"
    }

    if (purchaseAmount >= 100000) {
        return "SILVER"
    }

    return "BASIC"
}

const purchaseAmount = 650000
const grade = getMemberGrade(
    purchaseAmount,
)

console.log(grade)
```

## 50-1. 입력값

```text
650,000원
```

## 50-2. 출력 결과

```text
GOLD
```

## 50-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `Number.isFinite()` | 유효한 유한 숫자인지 검사 |
| 조기 반환 | 잘못된 입력을 먼저 종료 |
| 높은 기준부터 검사 | 겹치는 범위의 잘못된 판정 방지 |
| `return` | 판정 결과 재사용 |
| 함수 분리 | 등급 규칙을 한곳에서 관리 |

---

# 51. 대표 오류로 이해하기

## 51-1. 대입과 비교 혼동

```javascript
let score = 85

if (score = 100) {
    console.log("만점")
}
```

`score`에 100이 대입되고 100은 Truthy이므로 블록이 실행된다.

개선:

```text
if (score === 100) {
```

---

## 51-2. `else` 조건 작성

```text
if (score >= 60) {
    ...
} else (score < 60) {
    ...
}
```

발생 결과:

```text
SyntaxError
```

추가 조건은 `else if`를 사용한다.

---

## 51-3. `switch`의 `break` 누락

일치한 `case` 아래의 코드가 계속 실행될 수 있다.

---

## 51-4. 숫자 변환 실패를 검사하지 않음

```text
const number = Number("문자")

if (number >= 0) {
    ...
}
```

`number`는 `NaN`이며 모든 크기 비교가 `false`다.

`Number.isNaN(number)`를 먼저 검사해야 한다.

---

## 51-5. 잘못된 범위 비교

```text
if (3 < value < 20) {
```

JavaScript에서는 원하는 범위 비교가 아니다.

---

# 52. 자주 하는 실수

## 52-1. 서로 반대인 조건을 독립된 `if` 두 개로 작성

둘 중 하나만 실행되어야 한다면 `if·else`가 적합하다.

## 52-2. 한 줄 조건문에서 중괄호 생략

나중에 문장을 추가할 때 오류가 생기기 쉽다.

## 52-3. 낮은 기준을 먼저 검사

높은 등급 조건이 실행되지 않을 수 있다.

## 52-4. `==`를 기본 비교로 사용

암시적 형 변환이 발생할 수 있다.

## 52-5. `switch`에서 `break` 누락

원하지 않는 다음 `case`까지 실행될 수 있다.

## 52-6. `prompt()` 결과를 숫자로 생각

문자열 또는 `null`이므로 변환과 검증이 필요하다.

## 52-7. `NaN` 비교 결과를 일반 숫자처럼 처리

`Number.isNaN()`으로 검사한다.

## 52-8. 빈 배열과 빈 객체를 Falsy로 생각

JavaScript에서는 Truthy다.

## 52-9. `!number % 2 === 0`처럼 우선순위를 혼동

홀수는 `number % 2 !== 0`으로 직접 작성한다.

## 52-10. 연속 비교식을 수학식처럼 작성

논리 AND로 각 비교를 연결해야 한다.

## 52-11. `Math.random()`이 1을 포함한다고 생각

0 이상 1 미만이다.

## 52-12. 난수에 불필요한 `%` 사용

원하는 범위를 곱한 뒤 `Math.floor()`를 사용한다.

---

# 53. 핵심 요약

```text
if
→ 첫 조건 검사

else if
→ 추가 조건 검사

else
→ 모든 앞 조건이 거짓일 때
```

```text
Truthy
→ 조건에서 참처럼 평가

Falsy
→ false, 0, "", null,
   undefined, NaN 등
```

```text
switch
→ 하나의 값 비교

case
→ 비교할 값

break
→ switch 종료

default
→ 기본 분기
```

```text
Number()
→ 문자열을 숫자로 변환

Number.isNaN()
→ 변환 실패 검사

Math.floor()
→ 아래 정수로 내림

Math.random()
→ 0 이상 1 미만 난수
```

---

# 54. 최종 체크리스트

- [ ] `if`, `else if`, `else`를 작성할 수 있는가?
- [ ] `!`로 조건을 반전할 수 있는가?
- [ ] 서로 반대인 조건을 `if·else`로 구성할 수 있는가?
- [ ] 실행 블록에 중괄호를 일관되게 사용할 수 있는가?
- [ ] 범위 조건을 높은 기준부터 작성할 수 있는가?
- [ ] 대표적인 Falsy 값을 설명할 수 있는가?
- [ ] 빈 배열과 빈 객체가 Truthy임을 이해했는가?
- [ ] `switch`, `case`, `break`, `default`를 사용할 수 있는가?
- [ ] 여러 `case`를 하나의 결과로 묶을 수 있는가?
- [ ] `switch`가 엄격하게 값을 비교함을 이해했는가?
- [ ] 입력 문자열을 `Number()`로 변환할 수 있는가?
- [ ] `Number.isNaN()`으로 변환 실패를 확인할 수 있는가?
- [ ] 홀수·짝수 조건을 정확하게 작성할 수 있는가?
- [ ] 두 수 사이 범위를 `&&`로 표현할 수 있는가?
- [ ] 35분 후 시간을 나눗셈과 나머지로 계산할 수 있는가?
- [ ] 각 자리 숫자를 나눗셈과 나머지로 구할 수 있는가?
- [ ] 369게임을 숫자 또는 문자열 방식으로 작성할 수 있는가?
- [ ] 좌표가 사각형 범위 안에 있는지 판정할 수 있는가?
- [ ] `Math.random()`의 반환 범위를 설명할 수 있는가?
- [ ] 최소값·최대값 범위의 정수 난수를 만들 수 있는가?
- [ ] 연속 비교식을 JavaScript 방식으로 올바르게 바꿀 수 있는가?

---

# 마무리

조건문의 핵심은 분기 문법을 외우는 것에서 끝나지 않는다.

```text
입력값을 먼저 검증하고
    ↓
조건의 우선순위를 정하고
    ↓
서로 겹치는 범위를 올바른 순서로 검사하고
    ↓
조건에 맞는 실행 경로를 선택하고
    ↓
잘못된 입력을 안전하게 처리하는 것
```

이 흐름을 이해하면 이후 반복문과 함수에서 프로그램의 동작을 더 안정적으로 제어할 수 있다.
# V3 실행 추적 카드 — 조건 평가 → 한 실행 경로 선택

`if`는 truthy/falsy를 평가하고 첫 참 분기만 실행한다. `switch`는 표현식과 case를 엄격 비교하며 `break`가 없으면 다음 case까지 이어진다.

`const value="1"; switch(value){case 1: console.log("숫자"); break; default: console.log("불일치");}`는 `불일치`를 출력한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/03_if.html`에서 실제 사용 위치와 차이를 확인한다.
