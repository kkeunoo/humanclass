---
title: JavaScript While과 Do While
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript While과 Do While

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `05_JavaScript_While과_DoWhile.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/05_while.html`, `workspace_teacher/workspace_html/javascript/05_while.html` |
| 핵심 범위 | `while`, `do...while`, 반복 조건, 반복 변수 갱신, 무한 반복, `break`, 메뉴 반복, 입력값 검증 |
| 실습 범위 | 메뉴 프로그램, 입출금 프로그램, 주사위 반복, 업다운 게임, 정사각형 테두리 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> `while`과 `do...while`의 실행 구조, 사용자 입력 반복, 상태 유지, 종료 조건을 이해하는 데 필요한 코드만 발췌하고 실무 개선 방향을 함께 설명한다.

---

# 개요

`while`은 조건이 참인 동안 같은 코드를 반복한다.

```text
조건 확인
    ↓
참이면 코드 실행
    ↓
조건에 사용되는 값 변경
    ↓
다시 조건 확인
```

`for`가 반복 횟수와 증감 규칙을 한곳에 작성하는 문법이라면, `while`은 종료 시점이 사용자 입력이나 상태 변화에 따라 달라질 때 자연스럽다.

```javascript
let number = 1

while (number <= 5) {
    console.log(number)
    number += 1
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

> [!IMPORTANT]
> `while`에서는 조건에 사용되는 값이 반복 중 실제로 변경되는지 반드시 확인해야 한다.
>
> 값이 변경되지 않으면 브라우저 탭이 멈출 정도의 무한 반복이 발생할 수 있다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `while` | 조건이 Truthy인 동안 반복 |
| `do...while` | 실행 후 조건을 검사해 최소 한 번 실행 |
| 반복 조건 | 반복을 계속할지 결정 |
| 반복 변수 갱신 | 종료 조건에 가까워지도록 값 변경 |
| `while (true)` | 내부 종료 조건을 사용하는 무한 반복 구조 |
| `break` | 반복문 즉시 종료 |
| `continue` | 현재 반복의 남은 코드를 건너뜀 |
| 상태 변수 | 반복 사이에 유지해야 하는 값 |
| `prompt()` | 문자열 또는 `null` 반환 |
| `Number.isInteger()` | 정수 여부 검사 |
| `Number.isFinite()` | 유한한 숫자인지 검사 |
| `Number.isNaN()` | 값이 실제 `NaN`인지 검사 |
| 시도 횟수 | 유효한 입력 또는 실제 실행 횟수 기록 |

---

# 학습 목표

- `while`문의 실행 순서를 설명할 수 있다.
- 반복 변수의 초기값·조건·갱신을 구분할 수 있다.
- 무한 반복이 발생하는 원인을 설명할 수 있다.
- `for`와 `while`의 선택 기준을 구분할 수 있다.
- `while (true)`와 `break`를 안전하게 사용할 수 있다.
- `do...while`이 최소 한 번 실행되는 이유를 설명할 수 있다.
- 메뉴 입력을 반복해서 받을 수 있다.
- `prompt()`의 문자열·빈 문자열·`null`을 구분할 수 있다.
- 숫자 변환 전에 취소와 빈 입력을 검사할 수 있다.
- 입금·출금·잔액 조회 프로그램의 상태를 유지할 수 있다.
- 유효하지 않은 입력을 `continue`로 건너뛸 수 있다.
- 주사위가 특정 값이 나올 때까지 반복할 수 있다.
- 업다운 게임의 정답과 시도 횟수를 관리할 수 있다.
- 정사각형 테두리 패턴을 반복문으로 출력할 수 있다.

---

# 1. `while` 기본 구조

```text
while (조건식) {
    반복할 코드
}
```

조건식이 Truthy이면 블록을 실행하고, 블록이 끝나면 다시 조건을 검사한다.

---

# 2. 기본 `while`

## 2-1. 강사님 코드

```javascript
let number = 1

while (number <= 10) {
    console.log(number)
    number += 1
}
```

## 2-2. 출력 결과

```text
1
2
3
...
10
```

## 2-3. 구성

| 코드 | 역할 |
| --- | --- |
| `let number = 1` | 초기값 |
| `number <= 10` | 반복 조건 |
| `console.log(number)` | 반복 작업 |
| `number += 1` | 반복 변수 갱신 |

---

# 3. 내 코드의 기본 `while`

내 코드에는 같은 예제가 주석 처리된 상태로 들어 있다.

```javascript
let number = 1

while (number <= 10) {
    console.log(number)
    number += 1
}
```

내 코드의 설명처럼 `while` 괄호 안에는 반복 여부를 결정하는 조건식이 들어간다.

---

# 4. 반복 변수 갱신 누락

잘못된 코드:

```javascript
let number = 1

while (number <= 10) {
    console.log(number)
}
```

`number`가 계속 1이므로 조건은 영원히 참이다.

> [!WARNING]
> 브라우저에서 무한 반복이 실행되면 화면이 멈추고 개발자 도구도 응답하지 않을 수 있다.

---

# 5. 종료 조건 방향

잘못된 코드:

```javascript
let number = 1

while (number <= 5) {
    console.log(number)
    number -= 1
}
```

`number`는 종료값 5에서 더 멀어지므로 반복이 끝나지 않는다.

올바른 코드:

```javascript
number += 1
```

---

# 6. 감소하는 `while`

```javascript
let number = 5

while (number >= 1) {
    console.log(number)
    number -= 1
}
```

출력:

```text
5
4
3
2
1
```

---

# 7. 합계 누적

```javascript
let number = 1
let total = 0

while (number <= 100) {
    total += number
    number += 1
}

console.log(total)
```

출력:

```text
5050
```

`total`은 반복 사이에 유지되어야 하므로 반복문 밖에 선언한다.

---

# 8. `for`와 `while` 비교

| 상황 | 적합한 방식 |
| --- | --- |
| 1부터 10까지 반복 | `for` |
| 배열 인덱스 순회 | `for`, 배열 메서드 |
| 사용자가 종료할 때까지 | `while` |
| 게임 정답을 맞힐 때까지 | `while` |
| 최소 한 번 메뉴 표시 | `do...while` |
| 특정 상태가 될 때까지 | `while` |

문법적으로 서로 바꿀 수 있는 경우도 있지만, 코드의 목적이 잘 드러나는 방식을 선택한다.

---

# 9. 메뉴 프로그램의 초기값

원본:

```javascript
let menu = -1
```

`-1`은 실제 메뉴 번호 0·1·2와 겹치지 않는 임시값이다.

하지만 입력을 반복 블록 안에서 바로 받는 구조라면 별도 초기값 없이 작성할 수도 있다.

---

# 10. 단일 메뉴 처리

```javascript
const menu = "1"

if (menu === "1") {
    console.log("커피")
} else if (menu === "2") {
    console.log("홍차")
} else if (menu === "0") {
    console.log("종료")
} else {
    console.log("정확히 입력해주세요.")
}
```

한 번만 실행되므로 주문 뒤 프로그램은 종료된다.

---

# 11. 메뉴 입력 반복

```javascript
let menu = prompt(
    "1:커피, 2:홍차, 0:종료",
)

while (menu !== "0") {
    if (menu === "1") {
        console.log("커피를 준비합니다.")
    } else if (menu === "2") {
        console.log("홍차를 준비합니다.")
    } else {
        console.log("메뉴를 정확히 입력해주세요.")
    }

    menu = prompt(
        "1:커피, 2:홍차, 0:종료",
    )
}

console.log("종료합니다.")
```

입력 갱신이 없으면 같은 메뉴를 계속 처리한다.

---

# 12. 도달할 수 없는 종료 분기

다음 구조에서는 내부의 `menu === "0"` 분기가 실행되지 않는다.

```javascript
while (menu !== "0") {
    if (menu === "0") {
        break
    }
}
```

`menu`가 `"0"`이면 반복문에 진입하기 전에 종료되기 때문이다.

종료 조건을 `while` 조건식에서 처리할지, 내부 `break`로 처리할지 하나의 방식으로 통일한다.

---

# 13. `while (true)`

```javascript
while (true) {
    const menu = prompt(
        "1:커피, 2:홍차, 0:종료",
    )

    if (menu === null || menu === "0") {
        break
    }

    if (menu === "1") {
        console.log("커피를 준비합니다.")
    } else if (menu === "2") {
        console.log("홍차를 준비합니다.")
    } else {
        console.log("메뉴를 정확히 입력해주세요.")
    }
}
```

종료 지점이 블록 안에 명확하게 보일 때 사용할 수 있다.

---

# 14. 안전한 무한 반복 조건

`while (true)`를 사용할 때 확인할 항목:

- `break`에 도달 가능한 조건이 있는가?
- 취소 입력을 처리하는가?
- 잘못된 입력에서도 다음 반복으로 이동하는가?
- 종료 조건이 코드 여러 곳에 흩어져 있지 않은가?
- 반복 중 브라우저를 막는 무거운 작업이 없는가?

---

# 15. 웹 서버와 `while (true)`

내 코드에는 지속적으로 사용자가 접근하는 웹 서비스와 `while (true)`를 연결한 설명이 있다.

브라우저 JavaScript의 무한 반복은 서버 요청을 처리하는 방식이 아니다.

이 단원에서 적절한 예:

- 사용자가 종료 메뉴를 고를 때까지 반복
- 게임을 끝낼 때까지 입력 반복
- 특정 난수가 나올 때까지 반복
- 유효한 입력을 받을 때까지 재입력

---

# 16. `for`로 입력 반복

```javascript
for (
    let menu = prompt("메뉴");
    menu !== "0";
    menu = prompt("메뉴")
) {
    console.log(menu)
}
```

문법적으로 가능하지만 입력 로직이 `for` 괄호에 들어가 읽기 어렵다.

사용자 입력 기반 반복은 `while`이 더 자연스러운 경우가 많다.

---

# 17. `do...while`

```text
do {
    실행할 코드
} while (조건식)
```

`do` 블록을 먼저 실행한 뒤 조건을 검사한다.

```text
while
→ 조건 검사 후 실행

do...while
→ 먼저 실행 후 조건 검사
```

---

# 18. 최소 한 번 실행

```javascript
let value = 10

do {
    console.log(value)
} while (value < 0)
```

조건은 처음부터 거짓이지만 `10`이 한 번 출력된다.

---

# 19. `do...while` 메뉴

```javascript
let menu

do {
    menu = prompt(
        "1:커피, 2:홍차, 0:종료",
    )

    if (menu === null || menu === "0") {
        console.log("종료합니다.")
        break
    }

    if (menu === "1") {
        console.log("커피를 준비합니다.")
    } else if (menu === "2") {
        console.log("홍차를 준비합니다.")
    } else {
        console.log("메뉴를 정확히 입력해주세요.")
    }
} while (menu !== "0")
```

메뉴가 반드시 한 번 표시되어야 하는 구조에 적합하다.

---

# 20. `do...while`의 세미콜론

표준적인 형태:

```javascript
do {
    console.log("실행")
} while (false);
```

마지막 `while (조건식)` 뒤에는 세미콜론을 작성한다.

---

# 21. `typeof`

```javascript
const value = 1

console.log(
    typeof value === "string",
)
```

출력:

```text
false
```

`typeof value`의 결과는 `"number"`다.

엄격 비교 `===`를 사용한다.

---

# 22. 전역 `isNaN()`

```javascript
console.log(isNaN(231))
console.log(isNaN("문자"))
console.log(isNaN(""))
```

출력:

```text
false
true
false
```

전역 `isNaN()`은 먼저 숫자로 변환한 뒤 검사한다.

```javascript
Number("")
// 0
```

이 때문에 빈 문자열도 숫자로 해석될 수 있다.

---

# 23. `Number.isNaN()`

```javascript
const value = Number("문자")

console.log(
    Number.isNaN(value),
)
```

출력:

```text
true
```

`Number.isNaN()`은 값이 실제 `NaN`일 때만 `true`다.

---

# 24. 숫자 입력 검증 순서

`prompt()` 결과를 다음 순서로 처리한다.

```text
취소 확인
→ null 검사

빈 입력 확인
→ trim() 검사

숫자로 변환
→ Number()

정수·범위 확인
→ Number.isInteger()
```

---

# 25. 취소를 변환 전에 검사

잘못된 코드:

```javascript
const input = prompt("숫자")
const number = Number(input)

if (number === null) {
    console.log("취소")
}
```

`Number(null)`은 `0`이므로 `number`는 `null`이 아니다.

개선:

```javascript
const input = prompt("숫자")

if (input === null) {
    console.log("취소")
}
```

---

# 26. 빈 문자열 검사

```javascript
const input = prompt("숫자")

if (
    input !== null
    && input.trim() === ""
) {
    console.log("값을 입력해주세요.")
}
```

`Number("")`와 `Number(" ")`는 모두 `0`이 될 수 있으므로 변환 전에 검사한다.

---

# 27. 정수 검사

```javascript
const input = "10"
const number = Number(input)

console.log(
    Number.isInteger(number),
)
```

출력:

```text
true
```

`number >= 0`은 정수 검사가 아니다.

다음 값도 통과할 수 있다.

```text
10.5
Infinity
```

---

# 28. 입출금 프로그램 요구사항

```text
초기 잔액
→ 0원

메뉴
→ 입금
→ 출금
→ 잔액 조회
→ 종료

검증
→ 1원 이상의 정수
→ 잔액 초과 출금 금지
→ 취소·빈 입력 처리
```

---

# 29. 상태 변수

```javascript
let balance = 0

while (true) {
    // balance 변경
}
```

`balance`는 반복문 밖에 선언해야 다음 메뉴에서도 값이 유지된다.

반복문 안에서 `0`으로 다시 선언하면 매 회차 잔액이 초기화된다.

---

# 30. 금액 입력 함수

```javascript
function readPositiveAmount(
    message,
) {
    const input = prompt(message)

    if (input === null) {
        return null
    }

    if (input.trim() === "") {
        console.log("금액을 입력해주세요.")
        return undefined
    }

    const amount = Number(input)

    if (
        !Number.isInteger(amount)
        || amount <= 0
    ) {
        console.log(
            "1원 이상의 정수를 입력해주세요.",
        )

        return undefined
    }

    return amount
}
```

반복되는 입력 검증을 함수로 분리하면 입금과 출금에서 재사용할 수 있다.

---

# 31. 입금 처리

```javascript
const amount = readPositiveAmount(
    "입금액을 입력해주세요.",
)

if (amount !== null && amount !== undefined) {
    balance += amount

    console.log(
        `${amount.toLocaleString()}원을 입금했습니다.`,
    )

    console.log(
        `현재 잔액: ${balance.toLocaleString()}원`,
    )
}
```

---

# 32. 출금 처리

```javascript
const amount = readPositiveAmount(
    "출금액을 입력해주세요.",
)

if (amount !== null && amount !== undefined) {
    if (amount > balance) {
        console.log("잔액이 부족합니다.")
    } else {
        balance -= amount

        console.log(
            `${amount.toLocaleString()}원을 출금했습니다.`,
        )

        console.log(
            `현재 잔액: ${balance.toLocaleString()}원`,
        )
    }
}
```

---

# 33. 입출금 프로그램 완성본

```javascript
let balance = 0

while (true) {
    const menu = prompt(
        "1.입금 / 2.출금 / 3.잔액 / 4.종료",
    )

    if (menu === null || menu === "4") {
        console.log("프로그램을 종료합니다.")
        break
    }

    if (menu === "1") {
        const amount = readPositiveAmount(
            "입금액을 입력해주세요.",
        )

        if (
            amount !== null
            && amount !== undefined
        ) {
            balance += amount

            console.log(
                `현재 잔액: ${balance.toLocaleString()}원`,
            )
        }
    } else if (menu === "2") {
        const amount = readPositiveAmount(
            "출금액을 입력해주세요.",
        )

        if (
            amount !== null
            && amount !== undefined
        ) {
            if (amount > balance) {
                console.log("잔액이 부족합니다.")
            } else {
                balance -= amount

                console.log(
                    `현재 잔액: ${balance.toLocaleString()}원`,
                )
            }
        }
    } else if (menu === "3") {
        console.log(
            `현재 잔액: ${balance.toLocaleString()}원`,
        )
    } else {
        console.log("메뉴를 정확히 입력해주세요.")
    }
}
```

---

# 34. 주사위가 3이 나올 때까지

```javascript
let attempts = 0
let dice

while (dice !== 3) {
    dice = (
        Math.floor(Math.random() * 6)
        + 1
    )

    attempts += 1

    console.log(
        `${attempts}회: ${dice}`,
    )
}
```

`dice`가 3이 되면 다음 조건 검사에서 반복이 종료된다.

---

# 35. `while (true)` 주사위 방식

```javascript
let attempts = 0

while (true) {
    const dice = (
        Math.floor(Math.random() * 6)
        + 1
    )

    attempts += 1

    if (dice === 3) {
        console.log(
            `${attempts}번째 시도에서 3이 나왔습니다.`,
        )

        break
    }
}
```

종료 조건이 블록 안에 더 직접적으로 보인다.

---

# 36. 난수 정수화

원본:

```javascript
parseInt(
    Math.random() * 6,
) + 1
```

개선:

```javascript
Math.floor(
    Math.random() * 6,
) + 1
```

숫자의 소수 부분을 내리는 목적에는 `Math.floor()`가 명확하다.

---

# 37. 업다운 게임 정답

```javascript
const answer = (
    Math.floor(Math.random() * 100)
    + 1
)
```

정답은 게임이 끝날 때까지 유지되어야 하므로 반복문 밖에 선언한다.

반복문 안에 선언하면 매 입력마다 정답이 바뀐다.

---

# 38. 업다운 입력 검증

```javascript
function readGuess() {
    const input = prompt(
        "1~100 사이 정수를 입력해주세요.\n"
        + "0 또는 취소: 종료",
    )

    if (input === null || input === "0") {
        return null
    }

    if (input.trim() === "") {
        console.log("숫자를 입력해주세요.")
        return undefined
    }

    const guess = Number(input)

    if (
        !Number.isInteger(guess)
        || guess < 1
        || guess > 100
    ) {
        console.log(
            "1~100 사이 정수를 입력해주세요.",
        )

        return undefined
    }

    return guess
}
```

---

# 39. 업다운 게임 완성본

```javascript
const answer = (
    Math.floor(Math.random() * 100)
    + 1
)

let attempts = 0

while (true) {
    const guess = readGuess()

    if (guess === null) {
        console.log("게임을 종료합니다.")
        break
    }

    if (guess === undefined) {
        continue
    }

    attempts += 1

    if (guess === answer) {
        console.log(
            `정답 ${answer}!`,
        )

        console.log(
            `${attempts}번 만에 맞혔습니다.`,
        )

        break
    }

    if (guess < answer) {
        console.log("UP")
    } else {
        console.log("DOWN")
    }
}
```

---

# 40. 시도 횟수 증가 위치

잘못된 구조:

```javascript
attempts += 1

// 그 뒤 입력값 검증
```

취소·빈 값·문자·범위 밖 값까지 시도 횟수에 포함된다.

권장:

```text
입력 검증 완료
    ↓
유효한 추측
    ↓
attempts 증가
```

---

# 41. 출력문에서 카운트 증가 금지

잘못된 코드:

```javascript
console.log(
    `${attempts++}번 만에 맞혔습니다.`,
)
```

출력 뒤 `attempts`가 다시 증가한다.

개선:

```javascript
console.log(
    `${attempts}번 만에 맞혔습니다.`,
)
```

---

# 42. UP과 DOWN

```javascript
if (guess < answer) {
    console.log("UP")
} else {
    console.log("DOWN")
}
```

사용자 입력이 정답보다 작으면 더 큰 숫자를 입력해야 하므로 `UP`이다.

---

# 43. 거리 안내

“거의 다 왔어요”를 출력하려면 실제 차이를 계산해야 한다.

```javascript
const distance = Math.abs(
    answer - guess,
)

if (distance <= 5) {
    console.log("거의 다 왔어요!")
}
```

단순히 모든 오답에 같은 문구를 출력하면 실제 상태와 맞지 않는다.

---

# 44. 정사각형 테두리 문제

요구사항:

```text
입력 5

+++++
+___+
+___+
+___+
+++++
```

테두리 조건:

```text
첫 행
마지막 행
첫 열
마지막 열
```

---

# 45. 정사각형 테두리 구현

```javascript
const size = 5

for (let row = 1; row <= size; row += 1) {
    let line = ""

    for (
        let column = 1;
        column <= size;
        column += 1
    ) {
        const isBorder = (
            row === 1
            || row === size
            || column === 1
            || column === size
        )

        line += (
            isBorder
                ? "+"
                : "_"
        )
    }

    console.log(line)
}
```

출력:

```text
+++++
+___+
+___+
+___+
+++++
```

---

# 46. 입력 크기 검증

```javascript
const input = "5"
const size = Number(input)

if (
    !Number.isInteger(size)
    || size < 2
    || size > 30
) {
    console.log(
        "2부터 30까지의 정수를 입력해주세요.",
    )
}
```

과도한 크기를 제한하면 콘솔 출력과 브라우저 성능을 보호할 수 있다.

---

# 47. `break`와 `continue`

| 키워드 | 동작 |
| --- | --- |
| `break` | 반복문 전체 종료 |
| `continue` | 현재 반복의 남은 코드 건너뜀 |

업다운 게임에서 잘못된 입력은 `continue`, 종료 입력은 `break`에 해당한다.

---

# 48. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기본 `while` | 주석 처리 | 실제 실행 |
| 설명 | `for`와 비교한 상세 메모 | 기본 흐름 중심 |
| 메뉴 반복 | 주석 처리 | 실제 실행 |
| `do...while` | 설명 중심 | 실제 실행 |
| `typeof`, `isNaN()` | 별도 예제 없음 | 기본 예제 포함 |
| 입출금 프로그램 | 상세 풀이 | 없음 |
| 주사위 문제 | 상세 풀이 | 없음 |
| 업다운 게임 | 직접 구현 | 요구사항만 제시 |
| 정사각형 테두리 | 없음 | 문제만 제시 |

## 48-1. 내 코드의 장점

- `for`와 `while`의 사용 상황을 비교했다.
- 입출금·주사위·업다운 게임을 직접 구현했다.
- 상태 변수를 반복문 밖에 두는 이유를 설명했다.
- 초보자가 이해할 수 있도록 상세 주석을 작성했다.

## 48-2. 내 코드의 개선점

- 전체 코드가 주석 처리되어 바로 실행되지 않는다.
- `whilte` 오타가 있다.
- 메뉴 비교에 `==`, `!=`를 사용한다.
- 취소와 빈 입력을 숫자 변환 전에 검사하지 않는다.
- `value >= 0`을 정수 검사로 설명한 부분은 정확하지 않다.
- 업다운 시도 횟수가 잘못된 입력까지 포함된다.
- 정답 출력에서 카운트를 다시 증가시킨다.

## 48-3. 강사님 코드의 장점

- 기본 `while`과 `do...while`을 실제 실행 상태로 보여 준다.
- 메뉴 입력 갱신 위치를 확인할 수 있다.
- `typeof`와 `isNaN()` 기본 동작을 다룬다.
- 정사각형과 업다운 게임 문제를 제시한다.

## 48-4. 강사님 코드의 보충점

- 종료 조건과 내부 `break`가 중복된다.
- `prompt()` 취소와 빈 입력 검증이 없다.
- 느슨한 비교를 사용한다.
- 정사각형과 업다운 게임의 완성 코드가 없다.
- 전역 `isNaN()`의 암시적 형 변환 주의가 필요하다.

---

# 49. 기존 코드에서 개선 코드로 바꾼 이유

## 49-1. 느슨한 비교 제거

기존:

```text
if (menu == 1) {
```

개선:

```text
if (menu === "1") {
```

`prompt()` 결과가 문자열임을 그대로 반영한다.

## 49-2. 취소 먼저 검사

기존:

```javascript
const value = Number(
    prompt("숫자"),
)
```

개선:

```javascript
const input = prompt("숫자")

if (input === null) {
    // 취소 처리
}
```

## 49-3. 시도 횟수 위치 개선

기존:

```javascript
attempts += 1
// 입력 검증
```

개선:

```javascript
// 입력 검증
attempts += 1
```

## 49-4. 난수 생성 개선

기존:

```javascript
parseInt(
    Math.random() * 6,
) + 1
```

개선:

```javascript
Math.floor(
    Math.random() * 6,
) + 1
```

---

# 50. 실무형 예제: 콘솔형 재고 관리

```javascript
const products = {
    keyboard: 5,
    mouse: 3,
}

while (true) {
    const menu = prompt(
        "1.재고 조회 / 2.입고 / 3.출고 / 4.종료",
    )

    if (menu === null || menu === "4") {
        console.log("재고 관리를 종료합니다.")
        break
    }

    if (menu === "1") {
        console.log(products)
        continue
    }

    const productName = prompt(
        "상품명을 입력해주세요.",
    )

    if (
        productName === null
        || productName.trim() === ""
        || !(productName in products)
    ) {
        console.log("등록된 상품이 아닙니다.")
        continue
    }

    const amountInput = prompt(
        "수량을 입력해주세요.",
    )

    if (
        amountInput === null
        || amountInput.trim() === ""
    ) {
        console.log("작업을 취소했습니다.")
        continue
    }

    const amount = Number(amountInput)

    if (
        !Number.isInteger(amount)
        || amount <= 0
    ) {
        console.log(
            "1 이상의 정수를 입력해주세요.",
        )

        continue
    }

    if (menu === "2") {
        products[productName] += amount
    } else if (menu === "3") {
        if (
            amount
            > products[productName]
        ) {
            console.log("재고가 부족합니다.")
            continue
        }

        products[productName] -= amount
    } else {
        console.log("메뉴를 확인해주세요.")
        continue
    }

    console.log(
        `${productName} 재고: ${products[productName]}개`,
    )
}
```

## 50-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `while (true)` | 사용자가 종료할 때까지 메뉴 반복 |
| `break` | 종료 메뉴·취소 시 전체 반복 종료 |
| `continue` | 잘못된 입력만 건너뛰고 메뉴로 복귀 |
| 객체 | 상품별 재고 상태 저장 |
| `Number.isInteger()` | 수량 정수 검증 |
| 상태 변수 | 입고·출고 후 재고 유지 |

---

# 51. 대표 오류로 이해하기

## 51-1. 무한 반복

```javascript
let number = 1

while (number <= 5) {
    console.log(number)
}
```

반복 변수 갱신이 없다.

## 51-2. 메뉴 갱신 누락

같은 메뉴로 같은 작업을 계속 반복한다.

## 51-3. 취소를 숫자 변환 후 확인

`Number(null)`은 `0`이므로 취소와 숫자 0을 구분할 수 없다.

## 51-4. 빈 문자열 직접 숫자 변환

`Number("")`는 `0`이다.

## 51-5. `NaN`을 범위 비교로만 검사

`NaN`은 대부분의 크기 비교에서 `false`다.

## 51-6. 출력 중 카운트 증가

```javascript
console.log(attempts++)
```

출력 뒤 값이 추가로 증가한다.

---

# 52. 자주 하는 실수

## 52-1. 반복 변수 갱신 누락

조건이 계속 참이 된다.

## 52-2. 종료 조건과 반대 방향으로 값 변경

종료 지점에서 더 멀어진다.

## 52-3. 상태 변수를 반복문 안에서 초기화

잔액·횟수·정답 등이 매 반복마다 초기화된다.

## 52-4. `while` 조건과 내부 `break`를 중복 사용

종료 흐름이 복잡해진다.

## 52-5. `prompt()` 결과를 바로 숫자로 변환

취소와 빈 문자열을 구분하기 어렵다.

## 52-6. `==`, `!=` 사용

명시적으로 변환한 뒤 `===`, `!==`를 사용한다.

## 52-7. 정수 검사를 범위 조건만으로 처리

`Number.isInteger()`가 필요하다.

## 52-8. 잘못된 입력도 시도 횟수에 포함

검증을 통과한 뒤 횟수를 증가한다.

## 52-9. `while (true)`에 종료 조건 누락

브라우저가 멈출 수 있다.

## 52-10. `do...while`이 조건을 먼저 검사한다고 생각

블록을 먼저 한 번 실행한다.

---

# 53. 핵심 요약

```text
while
→ 조건 먼저 검사
→ 참인 동안 반복

do...while
→ 먼저 한 번 실행
→ 그 뒤 조건 검사
```

```text
break
→ 반복 전체 종료

continue
→ 현재 반복 건너뜀

while (true)
→ 내부 종료 조건 필요
```

```text
prompt()
→ 문자열 또는 null

Number()
→ 숫자 변환

Number.isInteger()
→ 정수 검사

Number.isNaN()
→ NaN 검사
```

```text
상태 변수
→ 반복문 밖에 선언

정답
→ 게임 시작 전에 한 번 생성

시도 횟수
→ 유효한 입력 뒤 증가
```

---

# 54. 최종 체크리스트

- [ ] `while`문의 실행 순서를 설명할 수 있는가?
- [ ] 초기값·조건·갱신을 구분할 수 있는가?
- [ ] 무한 반복의 원인을 찾을 수 있는가?
- [ ] 증가·감소 `while`을 작성할 수 있는가?
- [ ] 합계를 누적할 수 있는가?
- [ ] `for`와 `while`의 선택 기준을 설명할 수 있는가?
- [ ] `while (true)`와 `break`를 안전하게 사용할 수 있는가?
- [ ] `do...while`이 최소 한 번 실행됨을 이해했는가?
- [ ] 메뉴 입력을 반복해서 받을 수 있는가?
- [ ] 종료 분기가 도달 가능한지 확인할 수 있는가?
- [ ] `prompt()`의 `null`을 변환 전에 검사할 수 있는가?
- [ ] 빈 문자열을 `trim()`으로 확인할 수 있는가?
- [ ] `Number.isInteger()`로 정수를 검사할 수 있는가?
- [ ] 잔액과 같은 상태를 반복문 밖에서 유지할 수 있는가?
- [ ] 입금·출금의 오류 원인을 구분해 안내할 수 있는가?
- [ ] 주사위가 특정 값이 나올 때까지 반복할 수 있는가?
- [ ] 업다운 게임 정답을 반복문 밖에 선언할 수 있는가?
- [ ] 유효한 추측만 시도 횟수에 포함할 수 있는가?
- [ ] 출력문에서 카운트를 다시 증가시키지 않는가?
- [ ] 중첩 반복문으로 테두리 패턴을 만들 수 있는가?
- [ ] `break`와 `continue`를 목적에 맞게 사용할 수 있는가?

---

# 마무리

`while`문의 핵심은 단순히 조건이 참인 동안 반복하는 것에서 끝나지 않는다.

```text
종료 조건을 명확하게 만들고
    ↓
조건에 사용되는 값을 갱신하고
    ↓
입력값을 변환 전에 검증하고
    ↓
반복 사이에 필요한 상태를 유지하고
    ↓
break와 continue로 흐름을 안전하게 제어하는 것
```

이 흐름을 이해하면 이후 함수 문서에서 반복되는 입력 검증과 작업을 별도 함수로 분리할 수 있다.
