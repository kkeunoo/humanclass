# JavaScript While과 Do While

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `05_JavaScript_While과_DoWhile.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `04_JavaScript_반복문과_배열순회.md` |
| 다음 학습 | `06_JavaScript_함수.md` |
| 원본 기준 | `workspace_me/workspace/workspace_html/javascript/05_while.html`, `workspace_teacher/workspace_teacher/workspace_html/javascript/05_while.html` |
| 핵심 범위 | `while`, `do...while`, 반복 조건, 반복 변수 갱신, 무한 반복, `break`, 메뉴 반복, 사용자 입력 검증, 입출금 프로그램, 랜덤 주사위, 업다운 게임, `typeof`, `isNaN()` |
| 프로젝트 연결 | 키오스크 메뉴, 콘솔형 프로그램, 재입력 처리, 게임 루프, 반복 입력, 상태 유지, 잔액 관리 |

> 이 문서는 내 코드와 강사님 코드의 `05_while.html`을 직접 비교해 작성했습니다. 강사님 코드는 기본 while과 메뉴 반복, do...while, `typeof`, `isNaN()`을 실제 실행 코드로 작성하고 정사각형·업다운 게임 문제를 제시합니다. 내 코드는 대부분을 주석 처리한 대신 while과 do...while 설명, 입출금 프로그램, 주사위 반복, 업다운 게임 풀이를 상세히 추가했습니다. 원본의 오타, 입력 검증 누락, 잘못된 null 판정, 카운트 중복 증가 등은 수정하지 않고 보존한 뒤 설명합니다.

---

# 학습 목표

- `while`문의 구조와 실행 순서를 설명한다.
- 반복 조건과 반복 변수 갱신의 중요성을 이해한다.
- `for`와 `while`의 사용 목적을 비교한다.
- `while(true)`와 `break`를 이용한 반복 구조를 이해한다.
- `do...while`이 최소 한 번 실행된다는 점을 설명한다.
- 메뉴 입력을 반복해서 받는 프로그램을 작성한다.
- prompt의 문자열과 null 반환값을 구분한다.
- 입금·출금·잔액 조회 프로그램의 상태 변수를 관리한다.
- 음수, 빈 문자열, NaN, 잔액 초과 출금을 검증한다.
- 랜덤 주사위가 특정 값이 나올 때까지 반복한다.
- 업다운 게임의 정답, 입력값, 시도 횟수를 관리한다.
- `typeof`와 `isNaN()`의 기본 동작을 설명한다.
- 원본 코드에서 실행되는 코드와 주석 처리된 코드를 구분한다.
- 내 코드와 강사님 코드의 실제 차이를 분석한다.

---

# 1. While문이란?

`while`은 조건이 truthy인 동안 실행 블록을 반복합니다.

```js
while (조건식) {
  반복할 코드
}
```

기본 흐름:

```text
조건 검사
→ true이면 실행
→ 다시 조건 검사
→ false이면 종료
```

`for`와 달리 초기화식과 증감식이 괄호 안에 정해진 위치로 들어가지 않습니다.

---

# 2. 원본 문서 구조

두 원본 모두 HTML의 `<head>` 안에서 내부 `<script>`를 실행합니다.

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
    // while 실습
  </script>
</head>
<body>
</body>
</html>
```

강사님 코드는 일부 예제가 실제 실행 상태입니다.

내 코드는 거의 모든 JavaScript 예제가 주석 처리되어 있어 파일을 열어도 별도 주석 해제 없이는 동작하지 않습니다.

---

# 3. 문서 언어와 제목

공통 원본:

```html
<html lang="en">
<title>Document</title>
```

콘텐츠가 한국어이므로 다음처럼 개선할 수 있습니다.

```html
<html lang="ko">
<title>JavaScript While과 Do While</title>
```

---

# 4. 강사님 기본 While 실행 코드

강사님 원본:

```js
let i = 1

while (i <= 10) {
  console.log(i)
  i++
}
```

출력:

```text
1
2
3
...
10
```

핵심 요소:

```text
초기값 → let i = 1
조건 → i <= 10
실행 → console.log(i)
갱신 → i++
```

---

# 5. 내 코드의 기본 While

내 코드에도 같은 내용이 있지만 전체가 주석 처리되어 있습니다.

```js
// let i=1;
// while(i <= 10) {
//     console.log(i)
//     i++
// }
```

내 코드에는 다음 설명이 추가됩니다.

```text
while은 조건문만 들어가며, 조건이 맞을 경우 계속 동작
```

의미는 대체로 맞지만 정확하게는 `while` 괄호 안에는 **조건식**이 들어갑니다.

---

# 6. 반복 변수 갱신 누락

다음 코드에서 `i++`가 없으면 조건이 계속 true입니다.

```js
let i = 1

while (i <= 10) {
  console.log(i)
}
```

`i`가 계속 1이므로 무한 반복이 됩니다.

while에서는 초기화와 갱신이 문법 구조 밖에 있어 빠뜨리기 쉽습니다.

---

# 7. For와 While 비교

내 코드 주석:

```text
실무는 횟수가 정해져있을 때 for를 주로 쓰고,
정해지지 않았을 때 while을 씀
```

학습 기준으로 유용한 설명입니다.

| 상황 | 자주 검토하는 반복문 |
| --- | --- |
| 1~10처럼 횟수 명확 | `for` |
| 사용자가 종료할 때까지 | `while` |
| 최소 한 번 메뉴 표시 | `do...while` |
| 배열 값 순회 | `for...of`, 배열 메서드 |

문법적으로는 서로 대체할 수 있는 경우도 많습니다.

---

# 8. 첫 번째 메뉴 입력

강사님 원본:

```js
let menu = -1
```

이후 단일 입력 처리 예제는 주석 처리되어 있습니다.

```js
// menu = prompt('1:커피, 2:홍차, 0:종료')
```

내 코드도 같은 구조를 주석으로 보존합니다.

초기값 `-1`은 메뉴 0, 1, 2와 겹치지 않는 임시값입니다.

---

# 9. 단일 메뉴 분기

공통 흐름:

```js
if (menu == 1) {
  console.log("커피")
} else if (menu == 2) {
  console.log("홍차")
} else if (menu == 0) {
  console.log("종료")
} else {
  console.log("정확히 입력")
}
```

prompt는 문자열을 반환하지만 원본은 `==`를 사용해 숫자와 느슨하게 비교합니다.

```text
"1" == 1
→ true
```

---

# 10. 메뉴 입력을 한 번만 받는 문제

단일 `if` 구조에서는 주문 후 프로그램이 끝납니다.

키오스크처럼 계속 메뉴로 돌아가려면 입력과 분기를 반복해야 합니다.

내 코드 주석:

```text
주문을 하고나서도 메인 화면으로 돌아가고 싶을 때 while 사용
```

while 사용 목적을 잘 설명합니다.

---

# 11. 강사님 While 메뉴 코드

강사님 원본은 실제 실행 상태입니다.

```js
menu = prompt("1:커피, 2:홍차, 0:종료")

while (menu != 0) {
  if (menu == 1) {
    console.log("커피 드릴께요")
  } else if (menu == 2) {
    console.log("홍차 드릴께요")
  } else if (menu == 0) {
    console.log("종료합니다")
    break
  } else {
    console.log("정확히 입력해 주세요")
  }

  menu = prompt(
    "1:커피, 2:홍차, 0:종료"
  )
}
```

조건에서 이미 `menu != 0`을 검사하므로 `menu == 0` 분기는 일반적으로 실행되지 않습니다.

---

# 12. 종료 분기가 도달하지 않는 이유

```js
while (menu != 0) {
  if (menu == 0) {
    console.log("종료합니다")
  }
}
```

`menu`가 0이면 while 진입 전에 반복이 종료됩니다.

따라서 내부의 `menu == 0` 분기는 도달할 수 없습니다.

종료 메시지가 필요하다면 반복이 끝난 뒤 출력할 수 있습니다.

```js
while (menu !== "0") {
  // 메뉴 처리
}

console.log("종료합니다.")
```

---

# 13. Break의 중복성

강사님 while 조건:

```js
while (menu != 0)
```

내부 종료 분기:

```js
else if (menu == 0) {
  break
}
```

조건식으로 종료하는 방식과 내부 `break` 방식이 함께 존재합니다.

둘 중 하나의 구조를 일관되게 선택하면 흐름이 명확합니다.

---

# 14. 내 코드의 While 메뉴

내 코드도 동일한 구조를 주석 처리해 보존합니다.

추가 설명:

```text
while에 true값을 주고 break을 따로 줄 수도 있지만,
안에있는 break을 찾기 어려움
```

`while(true)`는 종료 지점이 내부에 흩어질 수 있어 주의가 필요하다는 의미입니다.

다만 종료 조건이 여러 개인 프로그램에서는 오히려 `while(true)`와 명확한 `break`가 읽기 쉬울 수도 있습니다.

---

# 15. Whilte 오타

내 코드 주석:

```text
whilte(true)
```

`while(true)`의 오타입니다.

원본 오타는 보존하되 문서에서는 올바른 철자를 구분합니다.

---

# 16. 네이버 접근 설명 검토

내 코드:

```text
while(true) 같은 경우 네이버와 같이 계속 누군가 접근할 때
```

웹 서버는 단순히 브라우저 JavaScript의 `while(true)`로 사용자 접근을 처리하지 않습니다.

이 설명은 서버의 지속 실행과 반복문을 지나치게 단순화한 표현입니다.

현재 단원에서는 다음 예가 적절합니다.

```text
사용자가 종료 메뉴를 선택할 때까지 메뉴를 반복 표시
게임이 끝날 때까지 입력 반복
특정 랜덤 값이 나올 때까지 반복
```

---

# 17. For문으로 메뉴 반복

내 코드:

```js
for (
  menu = prompt("메뉴");
  menu != 0;
  menu = prompt("메뉴")
) {
}
```

문법적으로 가능하지만 입력식이 for 괄호에 들어가 의도를 읽기 어렵습니다.

while이 더 자연스럽습니다.

```js
let menu = prompt("메뉴")

while (menu !== "0") {
  // 처리
  menu = prompt("메뉴")
}
```

---

# 18. Do While 기본

구조:

```js
do {
  실행할 코드
} while (조건식)
```

`while`과의 가장 큰 차이:

```text
while
→ 조건을 먼저 검사

do...while
→ 코드를 먼저 한 번 실행한 뒤 조건 검사
```

따라서 do 블록은 최소 한 번 실행됩니다.

---

# 19. 강사님 Do While 메뉴

강사님 코드는 실제 실행 상태입니다.

```js
do {
  menu = prompt("1:커피, 2:홍차, 0:종료")

  if (menu == 1) {
    console.log("커피 드릴께요")
  } else if (menu == 2) {
    console.log("홍차 드릴께요")
  } else if (menu == 0) {
    console.log("종료합니다")
    break
  } else {
    console.log("정확히 입력해 주세요")
  }
} while (menu != 0)
```

입력을 do 블록 내부에서 받기 때문에 메뉴가 적어도 한 번 표시됩니다.

---

# 20. 내 코드 Do While 설명

내 코드:

```text
do-while은 while과 다르게 우선 1회 진행하고나서
조건에 맞았을 때 추가 진행여부 확인
```

핵심적으로 맞습니다.

더 정확한 표현:

```text
do 블록을 먼저 한 번 실행한 뒤,
while 조건이 truthy이면 다음 반복을 실행한다.
```

---

# 21. 드릴께요와 드릴게요

강사님 코드:

```text
커피 드릴께요
홍차 드릴께요
```

내 코드:

```text
커피 드릴게요
홍차 드릴게요
```

표준적인 표기는 `드릴게요`입니다.

내 코드가 문구를 수정한 차이가 있습니다.

---

# 22. 강사님 Typeof 예제

강사님 코드:

```js
let a = 1

console.log(typeof a == "string")
```

`typeof a`는 `"number"`입니다.

결과:

```text
"number" == "string"
→ false
```

엄격 비교 개선:

```js
typeof a === "string"
```

---

# 23. IsNaN 예제

강사님 코드:

```js
console.log(isNaN(231))
```

231은 숫자이므로 결과는 false입니다.

```text
isNaN(231)
→ false
```

전역 `isNaN()`은 입력을 숫자로 변환한 뒤 검사할 수 있습니다.

---

# 24. IsNaN과 Number IsNaN

```js
isNaN("문자")
// true

isNaN("")
// false
```

빈 문자열은 숫자 0으로 변환되기 때문입니다.

보다 엄격한 검사:

```js
Number.isNaN(value)
```

`Number.isNaN()`은 값이 실제 NaN일 때만 true입니다.

---

# 25. 강사님 정사각형 Border 문제

강사님 원본에는 문제 설명만 있습니다.

```text
입력 4

++++
+__+
+__+
++++
```

```text
입력 5

+++++
+___+
+___+
+___+
+++++
```

실제 구현 코드는 없습니다.

이 문제는 반복문과 조건문을 조합하는 확장 문제입니다.

---

# 26. 정사각형 Border 규칙

줄과 칸이 다음 중 하나이면 `+`입니다.

```text
첫 번째 줄
마지막 줄
첫 번째 칸
마지막 칸
```

그 외 내부는 `_`입니다.

```js
if (
  row === 1 ||
  row === size ||
  col === 1 ||
  col === size
) {
  line += "+"
} else {
  line += "_"
}
```

---

# 27. 내 코드 문제 1: 입출금 프로그램

내 코드에만 상세 풀이가 있습니다.

요구사항:

```text
초기 잔액 0원
입금
출금
잔액 보기
종료
음수 불가
출금은 잔액 초과 불가
```

전체 코드는 주석 처리되어 있습니다.

---

# 28. 입출금 상태 변수

내 코드:

```js
let money = prompt(
  "1.입금 / 2.출금 / 3.잔액보기 / 4.종료"
)

let bank_input
let bank_output
let bank_money = 0
```

역할:

```text
money
→ 현재 메뉴 선택

bank_input
→ 최근 입금액

bank_output
→ 최근 출금액

bank_money
→ 누적 잔액
```

---

# 29. 상태 유지

`bank_money`는 while 밖에서 선언됩니다.

```js
let bank_money = 0

while (true) {
  // bank_money 변경
}
```

반복마다 다시 0으로 초기화하지 않기 때문에 입금과 출금 결과가 다음 메뉴에서도 유지됩니다.

반복문 내부에 선언하면 매 회차 초기화되어 잔액이 사라질 수 있습니다.

---

# 30. 입금 처리

내 코드:

```js
let input =
  prompt("얼마를 입금하시겠습니까?")

bank_input = Number(input)

if (bank_input >= 0) {
  bank_money += bank_input
}
```

0원 입금도 허용합니다.

요구사항에서 음수만 금지하므로 문법적으로는 가능하지만, 실제 서비스에서는 0보다 큰 금액만 허용할 수 있습니다.

---

# 31. 입금 검증의 문제

다음 입력은 문제가 될 수 있습니다.

```text
취소
빈 문자열
공백
문자
```

변환:

```js
Number(null) // 0
Number("")   // 0
Number(" ")  // 0
Number("abc") // NaN
```

취소와 빈 입력이 0원 입금으로 처리될 수 있습니다.

---

# 32. 정수 설명 오류

내 코드 주석:

```text
bank_input에 값이 들어왔을 때 정수이면
```

실제 조건:

```js
bank_input >= 0
```

이 조건은 정수 여부를 검사하지 않습니다.

```text
10.5
→ 조건 통과

Infinity
→ 조건 통과
```

정수만 허용하려면:

```js
Number.isInteger(bank_input)
```

를 함께 검사합니다.

---

# 33. 입금 성공 메시지 누락

문제 설명:

```text
입금하면 얼마 입금
입금
잔액 얼마
```

그러나 실제 코드에서 정상 입금 후 잔액을 출력하지 않습니다.

```js
bank_money += bank_input
```

만 실행됩니다.

개선:

```js
console.log(
  `${bank_input}원을 입금했습니다.`
)

console.log(
  `현재 잔액: ${bank_money}원`
)
```

---

# 34. 출금 처리

내 코드:

```js
if (
  bank_output <= bank_money &&
  bank_output >= 0
) {
  bank_money -= bank_output
}
```

두 조건:

```text
잔액 이하
0 이상
```

을 모두 만족해야 출금합니다.

---

# 35. 출금 검증의 문제

입금과 같은 이유로 다음을 별도 검증해야 합니다.

```text
취소
빈 문자열
NaN
소수
Infinity
0원 출금
```

현재 오류 메시지는 모든 실패를 잔액 초과로 설명합니다.

```text
출금 가능한 금액을 초과하셨습니다.
```

문자 입력과 음수도 같은 메시지를 받습니다.

오류 원인별 분리가 더 정확합니다.

---

# 36. 메뉴 Prompt 갱신

while 마지막:

```js
money = prompt(
  "1.입금 / 2.출금 / 3.잔액보기 / 4.종료"
)
```

이 갱신이 없으면 최초 메뉴 값으로 같은 작업만 계속 반복됩니다.

while 반복에서 조건과 관련된 값을 갱신하는 핵심 부분입니다.

---

# 37. 메뉴 취소 처리

메뉴 prompt에서 취소를 누르면 null이 반환됩니다.

현재 내 코드에서는 어느 메뉴와도 일치하지 않아:

```text
정확히 입력해 주세요.
```

를 출력하고 다시 메뉴를 표시합니다.

취소를 종료로 처리하려면 먼저 검사해야 합니다.

```js
if (money === null) {
  break
}
```

---

# 38. 문제 2: 주사위 3 찾기

내 코드 요구:

```text
주사위를 던져서 3이 나올 때까지 반복
몇 번 만에 나왔는지 출력
```

강사님 원본에는 이 문제와 풀이가 없습니다.

내 코드에만 상세 구현이 있습니다.

---

# 39. 주사위 난수

내 코드:

```js
let box =
  parseInt(Math.random() * 6) + 1
```

범위:

```text
1~6
```

숫자 내림 목적에는 다음이 명확합니다.

```js
Math.floor(Math.random() * 6) + 1
```

---

# 40. 시도 횟수

```js
let cnt = 0

while (true) {
  const box =
    Math.floor(Math.random() * 6) + 1

  cnt++

  if (box === 3) {
    break
  }
}
```

주사위를 한 번 생성할 때마다 시도 횟수를 1 증가시킵니다.

첫 시도에 3이 나오면 cnt는 1입니다.

---

# 41. 주사위 출력 문구

내 코드:

```js
console.log(
  `찾았다 내 사랑 [${box}] ${cnt}번째 시도만에`
)
```

학습용 개성 있는 문구입니다.

일반적인 설명형 출력:

```js
console.log(
  `${cnt}번째 시도에서 3이 나왔습니다.`
)
```

---

# 42. 문제 3: 업다운 게임

공통 문제 요구:

```text
1~100 사이 랜덤 정답
입력값이 낮으면 UP
입력값이 높으면 DOWN
정답까지 시도 횟수 출력
```

강사님 코드는 요구사항만 제시합니다.

내 코드는 전체 풀이를 주석 처리 상태로 추가합니다.

---

# 43. 정답은 While 밖에 선언

내 코드 설명:

```text
업다운 중 숫자가 바뀌면 안되기 때문에 while문 밖에 선언
```

정확합니다.

```js
const answer =
  Math.floor(Math.random() * 100) + 1

while (true) {
  // 사용자 입력
}
```

반복문 안에서 정답을 생성하면 매 시도마다 정답이 바뀝니다.

---

# 44. 불필요한 Number 변환

내 코드:

```js
let updown =
  parseInt(Math.random() * 100) + 1

let updown_result =
  Number(updown)
```

`updown`은 이미 숫자입니다.

다시 `Number()`로 변환할 필요가 없습니다.

```js
const answer =
  Math.floor(Math.random() * 100) + 1
```

로 충분합니다.

---

# 45. Prompt 취소의 잘못된 판정

내 코드:

```js
let value = prompt("숫자를 입력하세요")
result = Number(value)

if (result == null || result == 0) {
  break
}
```

문제:

```js
Number(null)
→ 0
```

변환 후에는 취소와 숫자 0을 구분할 수 없습니다.

또한 숫자 변수 `result`는 일반적으로 null이 되지 않습니다.

취소 여부는 변환 전에 검사해야 합니다.

```js
if (value === null) {
  break
}
```

---

# 46. 입력 범위 조건

내 코드:

```js
if (result >= 0 && result <= 100)
```

0도 허용한 뒤 내부에서 종료값으로 처리합니다.

게임 숫자는 1~100이고, 0은 종료 명령이라는 설계입니다.

이 구조 자체는 가능하지만 입력 검증과 종료 명령을 분리하면 읽기 쉽습니다.

---

# 47. 빈 문자열 문제

```js
Number("")
→ 0
```

사용자가 아무것도 입력하지 않고 확인하면 게임 취소로 처리됩니다.

빈 입력과 명시적 0 종료를 구분하려면:

```js
if (value.trim() === "") {
  console.log("숫자를 입력하세요.")
  continue
}
```

가 필요합니다.

---

# 48. 시도 횟수 증가 위치

내 코드:

```js
updown_cnt++
```

입력 직후 무조건 증가합니다.

따라서 다음 입력도 시도 횟수에 포함됩니다.

```text
취소
0
문자
범위 밖 숫자
```

유효한 게임 입력만 시도로 계산하려면 검증 후 증가해야 합니다.

---

# 49. 정답 출력의 중복 증가 오류

내 코드:

```js
console.log(
  `${updown_cnt++}번만에 맞추셨습니다!`
)
```

반복 시작에서 이미 `updown_cnt++`를 실행했습니다.

출력에서도 후위 증가를 사용해 카운트를 한 번 더 증가시킵니다.

화면에는 증가 전 값이 보이지만 변수는 추가로 1 증가합니다.

정확한 출력:

```js
console.log(
  `${updown_cnt}번 만에 맞추셨습니다.`
)
```

---

# 50. UP과 DOWN 조건

내 코드:

```js
if (answer > result) {
  console.log("UP")
} else if (answer < result) {
  console.log("DOWN")
}
```

사용자 입력이 정답보다 작으면 더 큰 수를 입력해야 하므로 UP입니다.

사용자 입력이 정답보다 크면 DOWN입니다.

조건은 올바릅니다.

---

# 51. 거의 다 왔어요 문구

내 코드:

```text
거의 다 왔어요! UP!
거의 다 왔어요! DOWN!
```

현재 코드는 입력값과 정답의 차이를 계산하지 않습니다.

따라서 실제로 가까운지 여부와 관계없이 항상 “거의 다 왔어요”를 출력합니다.

단순히 다음 방향만 안내하려면 “UP”, “DOWN”으로 표현하는 것이 정확합니다.

---

# 52. 느슨한 비교

내 코드와 강사님 코드는 메뉴 및 값 비교에 `==`, `!=`를 사용합니다.

prompt 문자열과 숫자 비교를 간단히 하기 위한 학습 코드입니다.

실무 개선 흐름:

```js
const menu = Number(input)

if (menu === 1) {
}
```

입력값을 명시적으로 변환한 뒤 엄격 비교를 사용합니다.

---

# 53. 모든 예제가 주석 처리된 내 파일

내 코드의 JavaScript는 설명 주석을 포함해 거의 전부 `//`로 막혀 있습니다.

따라서 다음은 실제 실행되지 않습니다.

```text
기본 while
메뉴 프로그램
do...while
입출금 프로그램
주사위 문제
업다운 게임
```

학습 문서에서는 코드 내용을 분석하지만, 브라우저에서 확인하려면 원하는 예제의 주석을 해제해야 합니다.

---

# 54. 강사님 파일의 연속 Prompt

강사님 파일을 그대로 실행하면 다음 흐름이 이어집니다.

```text
1~10 출력
while 메뉴 prompt 반복
종료 후 do...while 메뉴 prompt 다시 실행
typeof 출력
isNaN 출력
```

즉, 메뉴 프로그램이 한 번 끝난 뒤 또 다른 메뉴 prompt가 다시 표시됩니다.

각 실습을 개별 주석 처리하지 않고 연속 실행한 구조입니다.

---

# 55. While 무한 반복 사용 기준

```js
while (true) {
  const input = prompt("메뉴")

  if (input === null || input === "0") {
    break
  }
}
```

이 구조는 다음 조건을 갖춰야 안전합니다.

- 종료 지점이 명확함
- break에 도달 가능한 조건이 있음
- 취소와 예외 입력 처리
- 반복 중 상태 갱신
- 브라우저가 멈출 가능성 검토

---

# 56. Do While의 세미콜론

문법:

```js
do {
  // 코드
} while (condition);
```

마지막 `while(condition)` 뒤에는 세미콜론을 작성하는 형태가 표준입니다.

원본은 세미콜론을 생략하지만 자동 세미콜론 삽입으로 실행될 수 있습니다.

프로젝트 스타일을 일관되게 유지합니다.

---

# 57. 입출금 프로그램 개선 예제

```js
let balance = 0

while (true) {
  const menuInput = prompt(
    "1.입금 / 2.출금 / 3.잔액 / 4.종료"
  )

  if (menuInput === null || menuInput === "4") {
    console.log("프로그램을 종료합니다.")
    break
  }

  if (menuInput === "1") {
    const amountInput =
      prompt("입금액을 입력하세요.")

    if (
      amountInput === null ||
      amountInput.trim() === ""
    ) {
      console.log("입금이 취소되었습니다.")
      continue
    }

    const amount = Number(amountInput)

    if (
      !Number.isInteger(amount) ||
      amount <= 0
    ) {
      console.log("1원 이상의 정수를 입력하세요.")
      continue
    }

    balance += amount
    console.log(`현재 잔액: ${balance}원`)
  } else if (menuInput === "2") {
    const amountInput =
      prompt("출금액을 입력하세요.")

    if (
      amountInput === null ||
      amountInput.trim() === ""
    ) {
      console.log("출금이 취소되었습니다.")
      continue
    }

    const amount = Number(amountInput)

    if (
      !Number.isInteger(amount) ||
      amount <= 0
    ) {
      console.log("1원 이상의 정수를 입력하세요.")
    } else if (amount > balance) {
      console.log("잔액이 부족합니다.")
    } else {
      balance -= amount
      console.log(`현재 잔액: ${balance}원`)
    }
  } else if (menuInput === "3") {
    console.log(`현재 잔액: ${balance}원`)
  } else {
    console.log("메뉴를 정확히 입력하세요.")
  }
}
```

---

# 58. 업다운 게임 개선 예제

```js
const answer =
  Math.floor(Math.random() * 100) + 1

let attempts = 0

while (true) {
  const input = prompt(
    "1~100 숫자를 입력하세요.\n" +
    "0 또는 취소: 종료"
  )

  if (input === null || input === "0") {
    console.log("게임을 종료합니다.")
    break
  }

  if (input.trim() === "") {
    console.log("숫자를 입력하세요.")
    continue
  }

  const guess = Number(input)

  if (
    !Number.isInteger(guess) ||
    guess < 1 ||
    guess > 100
  ) {
    console.log("1~100 사이 정수를 입력하세요.")
    continue
  }

  attempts++

  if (guess === answer) {
    console.log(
      `정답 ${answer}, ${attempts}번 만에 성공`
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

# 59. 정사각형 Border 개선 예제

```js
const size = 5

for (let row = 1; row <= size; row++) {
  let line = ""

  for (let col = 1; col <= size; col++) {
    const isBorder =
      row === 1 ||
      row === size ||
      col === 1 ||
      col === size

    line += isBorder ? "+" : "_"
  }

  console.log(line)
}
```

결과:

```text
+++++
+___+
+___+
+___+
+++++
```

---

# 60. My Code 분석

## 60.1 장점

- while의 사용 상황을 for와 비교해 설명했다.
- 반복 메뉴가 필요한 키오스크 사례를 제시했다.
- `while(true)`와 조건식 기반 while을 비교했다.
- do...while이 최소 한 번 실행됨을 설명했다.
- 강사님 코드의 메뉴 예제를 더 상세한 주석으로 풀었다.
- 입출금 프로그램의 전체 흐름을 직접 구현했다.
- 입금액과 출금액을 Number로 변환했다.
- 출금액이 잔액보다 클 수 없다는 조건을 구현했다.
- 잔액을 while 밖에서 관리해 상태를 유지했다.
- 주사위가 3이 나올 때까지 반복하는 문제를 완성했다.
- 시도 횟수 변수를 사용했다.
- 업다운 게임의 랜덤 정답을 while 밖에서 생성했다.
- UP, DOWN, 정답, 종료 분기를 구현했다.
- 각 코드에 초보자 관점의 상세 설명을 추가했다.
- 강사님 표현 `드릴께요`를 `드릴게요`로 수정했다.

## 60.2 개선점

- 전체 예제가 주석 처리되어 실제로 실행되지 않는다.
- `whilte` 오타가 있다.
- 서버의 지속 접근을 `while(true)`로 단순화한 설명은 부정확하다.
- 메뉴 비교에 느슨한 동등 연산자를 사용한다.
- while 조건이 `menu != 0`인데 내부에 `menu == 0` 분기와 break가 중복된다.
- 입금·출금 prompt의 취소와 빈 문자열을 처리하지 않는다.
- `bank_input >= 0`을 정수 검사라고 설명한 주석은 틀리다.
- NaN과 Infinity를 명시적으로 검증하지 않는다.
- 정상 입금·출금 후 잔액 출력이 없다.
- 출금 오류 원인을 모두 잔액 초과 메시지로 처리한다.
- 0원 입금과 0원 출금을 허용한다.
- 난수 정수화에 `parseInt()`를 사용한다.
- 업다운 정답 숫자에 불필요한 `Number()` 변환을 한다.
- prompt 취소를 Number로 변환한 뒤 null과 비교한다.
- 빈 문자열이 0으로 변환되어 취소처럼 처리된다.
- 유효하지 않은 입력도 시도 횟수에 포함된다.
- 정답 출력에서 `updown_cnt++`를 다시 사용해 카운트가 중복 증가한다.
- 실제 거리와 관계없이 항상 “거의 다 왔어요”를 출력한다.

---

# 61. Teacher Code 분석

## 61.1 장점

- 1~10 기본 while을 실제 실행 코드로 보여 준다.
- 반복 변수 초기화, 조건, 증가를 한 예제에서 확인한다.
- 메뉴 입력을 while로 반복한다.
- 메뉴 입력값을 반복 마지막에 갱신한다.
- do...while 메뉴 예제를 실제 실행한다.
- 최소 한 번 입력받는 do...while의 구조를 보여 준다.
- `typeof` 비교를 추가한다.
- `isNaN()` 기본 결과를 확인한다.
- 정사각형 테두리 패턴 문제를 제시한다.
- 업다운 게임의 요구사항을 제시한다.

## 61.2 개선점

- while 메뉴의 `menu == 0` 분기는 조건상 도달하기 어렵다.
- 조건식 종료와 break 종료가 중복된다.
- prompt 취소를 처리하지 않는다.
- 비교에 `==`, `!=`를 사용한다.
- `드릴께요`는 `드릴게요`가 자연스럽다.
- while 메뉴 종료 후 do...while 메뉴가 다시 시작된다.
- `typeof a == "string"`에 엄격 비교를 사용하지 않는다.
- 전역 `isNaN()`의 암묵적 변환 주의점이 없다.
- 정사각형 테두리 문제의 정답 코드가 없다.
- 업다운 게임의 풀이가 없다.
- while과 for의 사용 기준 설명이 없다.
- 무한 반복 방지와 break 사용 기준 설명이 부족하다.
- 문서 언어와 제목이 콘텐츠에 맞지 않는다.

---

# 62. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기본 while | 주석 처리 | 실제 실행 |
| while 설명 | 상세 추가 | 없음 |
| for·while 기준 | 설명 있음 | 없음 |
| 메뉴 단일 분기 | 주석 처리 | 주석 처리 |
| 메뉴 반복 while | 주석 처리 | 실제 실행 |
| 메뉴 문구 | `드릴게요` | `드릴께요` |
| while(true) 설명 | 있음, 일부 부정확 | 주석 형태만 |
| for 대체 예제 | 완성 형태 주석 | 헤더만 주석 |
| do...while | 주석 처리 | 실제 실행 |
| typeof 예제 | 없음 | 있음 |
| isNaN 예제 | 없음 | 있음 |
| 정사각형 문제 | 없음 | 요구사항 있음 |
| 입출금 프로그램 | 상세 풀이 있음 | 없음 |
| 주사위 3 찾기 | 상세 풀이 있음 | 없음 |
| 업다운 게임 | 상세 풀이 있음 | 요구사항만 |
| 입력 검증 | 일부 구현 | 없음 |
| null 처리 | 잘못된 변환 후 비교 | 없음 |
| 시도 횟수 | 구현, 중복 증가 오류 | 요구만 |
| 실제 실행 결과 | 거의 없음 | prompt 포함 연속 실행 |

---

# 63. 원본 공통 핵심 구조

```js
let i = 1

while (i <= 10) {
  console.log(i)
  i++
}

let menu = prompt(
  "1:커피, 2:홍차, 0:종료"
)

while (menu != 0) {
  if (menu == 1) {
    console.log("커피")
  } else if (menu == 2) {
    console.log("홍차")
  } else {
    console.log("정확히 입력")
  }

  menu = prompt(
    "1:커피, 2:홍차, 0:종료"
  )
}

do {
  menu = prompt(
    "1:커피, 2:홍차, 0:종료"
  )
} while (menu != 0)
```

---

# 64. 자주 하는 실수

## 64.1 반복 변수 증가 누락

조건이 계속 true여서 무한 반복됩니다.

## 64.2 Prompt 갱신 누락

같은 메뉴 값으로 같은 작업을 계속 반복합니다.

## 64.3 While 조건과 내부 Break 중복

종료 흐름이 불필요하게 복잡해집니다.

## 64.4 Prompt 취소를 Number 변환 후 검사

`Number(null)`이 0이 되어 취소와 숫자 0을 구분할 수 없습니다.

## 64.5 빈 문자열을 숫자로 바로 변환

`Number("")`는 0입니다.

## 64.6 NaN에 단순 범위 비교만 사용

NaN은 모든 일반 비교에서 false가 되므로 오류 원인을 명시적으로 검사해야 합니다.

## 64.7 정수 검사를 `value >= 0`으로 작성

소수와 Infinity도 통과할 수 있습니다.

## 64.8 유효하지 않은 입력도 시도 횟수 증가

검증 후에 count를 증가시켜야 합니다.

## 64.9 출력문에서 Count를 다시 증가

`count++`는 출력 후 변수까지 증가시킵니다.

## 64.10 While True에 종료 조건 없음

브라우저 탭이 멈출 수 있습니다.

---

# 65. 면접·복습 포인트

## Q1. While과 For의 차이는 무엇인가요?

for는 초기화·조건·증감을 한 곳에 표현하기 좋아 반복 횟수가 명확한 경우에 자주 사용합니다. while은 종료 시점이 사용자 입력이나 상태 변화에 따라 달라지는 경우에 자연스럽습니다.

## Q2. Do While의 가장 큰 특징은 무엇인가요?

조건을 검사하기 전에 do 블록을 먼저 실행하므로 최소 한 번 실행됩니다.

## Q3. While에서 무한 반복이 생기는 대표 원인은 무엇인가요?

조건에 사용되는 값이 반복 중 갱신되지 않거나 종료 조건에 절대 도달하지 못하는 경우입니다.

## Q4. While True는 항상 나쁜가요?

아닙니다. 종료 조건과 break가 명확하면 메뉴 루프나 게임 루프에 사용할 수 있습니다.

## Q5. Prompt 취소를 어떻게 검사해야 하나요?

Number 변환 전에 원본 문자열 변수가 `null`인지 검사해야 합니다.

## Q6. `Number("")`의 결과는 무엇인가요?

0입니다. 빈 문자열은 숫자 변환 전에 따로 검증해야 합니다.

## Q7. `isNaN()`과 `Number.isNaN()`의 차이는 무엇인가요?

전역 isNaN은 값을 숫자로 변환한 뒤 검사하지만 Number.isNaN은 실제 값이 NaN일 때만 true입니다.

## Q8. 업다운 게임 정답은 왜 while 밖에 선언하나요?

반복마다 정답이 바뀌지 않고 게임 전체에서 같은 값이 유지되어야 하기 때문입니다.

## Q9. 시도 횟수는 언제 증가시키는 것이 적합한가요?

취소, 빈 값, 오류 입력 검증을 통과한 유효한 추측을 처리할 때 증가시키는 것이 자연스럽습니다.

## Q10. 원본 업다운 코드의 null 판정이 잘못된 이유는 무엇인가요?

prompt 결과를 Number로 변환하면 null이 0이 되므로 변환된 결과를 null과 비교할 수 없기 때문입니다.

---

# Problems

## 문제 1. 기본 While

while문으로 1부터 5까지 출력하세요.

## 문제 2. 역순 While

while문으로 5부터 1까지 출력하세요.

## 문제 3. 합계

while문으로 1부터 100까지 합계를 구하세요.

## 문제 4. 짝수 출력

while문으로 1부터 20까지 짝수만 출력하세요.

## 문제 5. 무한 반복 수정

다음 코드의 문제를 설명하고 수정하세요.

```js
let i = 1

while (i <= 5) {
  console.log(i)
}
```

## 문제 6. Do While 최소 실행

조건이 처음부터 false여도 한 번 출력되는 do...while 예제를 작성하세요.

## 문제 7. 메뉴 반복

사용자가 `"0"`을 입력할 때까지 prompt로 메뉴를 반복해서 받으세요.

## 문제 8. 취소 종료

문제 7에서 prompt 취소도 종료로 처리하세요.

## 문제 9. 엄격한 메뉴 비교

문자열 메뉴 `"1"`, `"2"`, `"0"`을 엄격 비교로 처리하세요.

## 문제 10. 입금 검증

입금액 prompt에서 취소, 빈 값, 숫자가 아닌 값, 0 이하 값을 검증하세요.

## 문제 11. 출금 검증

잔액 10,000원에서 12,000원을 출금하려 할 때 잔액 부족을 출력하세요.

## 문제 12. 잔액 상태 유지

while 반복 중 입금과 출금 후 잔액이 유지되도록 변수 위치를 작성하세요.

## 문제 13. 주사위 3 찾기

주사위를 반복해서 던져 3이 나오면 종료하고 시도 횟수를 출력하세요.

## 문제 14. 주사위 Math Floor

1~6 난수를 `Math.floor()`로 생성하세요.

## 문제 15. Typeof

숫자 1의 typeof 결과가 `"number"`인지 엄격 비교하세요.

## 문제 16. Number IsNaN

문자열 `"abc"`를 Number로 변환한 뒤 NaN인지 검사하세요.

## 문제 17. 정사각형 테두리

크기 4의 테두리 패턴을 출력하세요.

## 문제 18. 업다운 정답 유지

1~100 랜덤 정답을 while 밖에 선언하세요.

## 문제 19. 업다운 입력 검증

취소, 빈 문자열, 정수가 아닌 값, 1~100 범위 밖 값을 구분하세요.

## 문제 20. 업다운 Count

유효한 입력만 시도 횟수에 포함하도록 코드를 작성하세요.

## 문제 21. 원본 오류 설명

내 업다운 코드의 `result == null`과 `${updown_cnt++}`가 왜 문제인지 설명하세요.

## 문제 22. 종합 ATM

다음 요구사항을 만족하는 while 프로그램을 작성하세요.

- 초기 잔액 0원
- 메뉴: 입금, 출금, 잔액 조회, 종료
- prompt 취소 시 종료
- 입출금액은 1원 이상의 정수
- 출금액은 잔액 이하여야 함
- 성공 후 현재 잔액 출력
- 잘못된 메뉴 재입력
- 엄격 비교 사용

---

# Answers & Explanations

## 정답 1

```js
let i = 1

while (i <= 5) {
  console.log(i)
  i++
}
```

## 정답 2

```js
let i = 5

while (i >= 1) {
  console.log(i)
  i--
}
```

## 정답 3

```js
let i = 1
let sum = 0

while (i <= 100) {
  sum += i
  i++
}

console.log(sum)
```

결과는 5050입니다.

## 정답 4

```js
let i = 1

while (i <= 20) {
  if (i % 2 === 0) {
    console.log(i)
  }

  i++
}
```

## 정답 5

`i`가 증가하지 않아 조건이 계속 true입니다.

```js
let i = 1

while (i <= 5) {
  console.log(i)
  i++
}
```

## 정답 6

```js
let value = 10

do {
  console.log(value)
} while (value < 0)
```

조건은 false지만 10이 한 번 출력됩니다.

## 정답 7

```js
let menu

while (menu !== "0") {
  menu = prompt("1:커피, 2:홍차, 0:종료")
}
```

## 정답 8

```js
while (true) {
  const menu =
    prompt("1:커피, 2:홍차, 0:종료")

  if (menu === null || menu === "0") {
    break
  }
}
```

## 정답 9

```js
const menu = "1"

if (menu === "1") {
  console.log("커피")
} else if (menu === "2") {
  console.log("홍차")
} else if (menu === "0") {
  console.log("종료")
}
```

## 정답 10

```js
const input =
  prompt("입금액을 입력하세요.")

if (input === null) {
  console.log("취소")
} else if (input.trim() === "") {
  console.log("빈 값")
} else {
  const amount = Number(input)

  if (
    !Number.isInteger(amount) ||
    amount <= 0
  ) {
    console.log("1원 이상의 정수를 입력하세요.")
  } else {
    console.log(`입금액: ${amount}원`)
  }
}
```

## 정답 11

```js
const balance = 10000
const amount = 12000

if (amount > balance) {
  console.log("잔액이 부족합니다.")
}
```

## 정답 12

```js
let balance = 0

while (true) {
  // balance를 변경
}
```

잔액 변수는 반복문 밖에 선언해야 반복마다 초기화되지 않습니다.

## 정답 13

```js
let attempts = 0

while (true) {
  const dice =
    Math.floor(Math.random() * 6) + 1

  attempts++

  if (dice === 3) {
    console.log(
      `${attempts}번째 시도에서 3`
    )
    break
  }
}
```

## 정답 14

```js
const dice =
  Math.floor(Math.random() * 6) + 1
```

## 정답 15

```js
const value = 1

console.log(typeof value === "number")
```

## 정답 16

```js
const value = Number("abc")

console.log(Number.isNaN(value))
```

## 정답 17

```js
const size = 4

for (let row = 1; row <= size; row++) {
  let line = ""

  for (let col = 1; col <= size; col++) {
    const isBorder =
      row === 1 ||
      row === size ||
      col === 1 ||
      col === size

    line += isBorder ? "+" : "_"
  }

  console.log(line)
}
```

## 정답 18

```js
const answer =
  Math.floor(Math.random() * 100) + 1

while (true) {
  // 사용자 입력
}
```

## 정답 19

```js
const input = prompt("1~100 정수")

if (input === null) {
  console.log("취소")
} else if (input.trim() === "") {
  console.log("빈 값")
} else {
  const guess = Number(input)

  if (!Number.isInteger(guess)) {
    console.log("정수가 아님")
  } else if (guess < 1 || guess > 100) {
    console.log("범위 밖")
  } else {
    console.log("유효한 입력")
  }
}
```

## 정답 20

```js
let attempts = 0

while (true) {
  const input = prompt("1~100 정수")

  if (input === null) {
    break
  }

  const guess = Number(input)

  if (
    input.trim() === "" ||
    !Number.isInteger(guess) ||
    guess < 1 ||
    guess > 100
  ) {
    continue
  }

  attempts++
}
```

## 정답 21

`result`는 `Number(value)`의 결과이므로 취소 null은 이미 0으로 변환됩니다. 따라서 null 여부를 구분할 수 없습니다. 또한 시도 횟수는 앞에서 이미 증가했는데 출력에서 `updown_cnt++`를 다시 사용해 변수 값을 추가로 증가시킵니다.

## 정답 22

```js
let balance = 0

while (true) {
  const menu = prompt(
    "1.입금 / 2.출금 / 3.잔액 / 4.종료"
  )

  if (menu === null || menu === "4") {
    console.log("종료합니다.")
    break
  }

  if (menu === "3") {
    console.log(`현재 잔액: ${balance}원`)
    continue
  }

  if (menu !== "1" && menu !== "2") {
    console.log("메뉴를 정확히 입력하세요.")
    continue
  }

  const amountInput = prompt(
    menu === "1"
      ? "입금액을 입력하세요."
      : "출금액을 입력하세요."
  )

  if (
    amountInput === null ||
    amountInput.trim() === ""
  ) {
    console.log("작업이 취소되었습니다.")
    continue
  }

  const amount = Number(amountInput)

  if (
    !Number.isInteger(amount) ||
    amount <= 0
  ) {
    console.log("1원 이상의 정수를 입력하세요.")
    continue
  }

  if (menu === "1") {
    balance += amount
    console.log(`현재 잔액: ${balance}원`)
  } else if (amount > balance) {
    console.log("잔액이 부족합니다.")
  } else {
    balance -= amount
    console.log(`현재 잔액: ${balance}원`)
  }
}
```

---

# Final Checklist

## While 기본

- [ ] while 조건이 true인 동안 반복함을 이해했다.
- [ ] 반복 변수 초기값을 준비했다.
- [ ] 반복 중 조건 관련 값을 갱신했다.
- [ ] 종료 조건에 도달 가능한지 확인했다.
- [ ] 무한 반복이 발생하지 않는지 검토했다.
- [ ] for와 while의 사용 상황을 구분했다.

## Do While

- [ ] do 블록이 최소 한 번 실행됨을 이해했다.
- [ ] 조건 검사가 실행 후 이루어짐을 이해했다.
- [ ] 메뉴를 최소 한 번 표시해야 하는 상황에 적용했다.
- [ ] 마지막 while 조건 뒤 세미콜론 스타일을 확인했다.

## 메뉴 반복

- [ ] prompt 반환값이 문자열 또는 null임을 이해했다.
- [ ] 취소를 Number 변환 전에 검사했다.
- [ ] 문자열 메뉴를 엄격 비교했다.
- [ ] 한 사이클 후 메뉴를 다시 입력받았다.
- [ ] 조건식 종료와 break 종료를 불필요하게 중복하지 않았다.
- [ ] 잘못된 메뉴를 다시 입력받도록 처리했다.

## 입출금 프로그램

- [ ] 잔액 변수를 반복문 밖에 선언했다.
- [ ] 입금과 출금 성공 후 잔액을 갱신했다.
- [ ] 취소와 빈 문자열을 검사했다.
- [ ] Number 변환 후 정수 여부를 검사했다.
- [ ] 1원 이상의 금액만 허용했다.
- [ ] 출금액이 잔액 이하인지 확인했다.
- [ ] 오류 원인별 메시지를 구분했다.
- [ ] 종료 메뉴 또는 취소 시 반복을 끝냈다.

## 랜덤과 게임

- [ ] 주사위 난수에 Math.floor를 사용했다.
- [ ] 한 번 생성할 때마다 시도 횟수를 증가시켰다.
- [ ] 업다운 정답을 while 밖에 선언했다.
- [ ] 유효한 입력만 시도 횟수에 포함했다.
- [ ] 정답 출력에서 count를 다시 증가시키지 않았다.
- [ ] 작은 입력에는 UP, 큰 입력에는 DOWN을 출력했다.
- [ ] 0 종료와 취소를 명확히 구분했다.

## 원본 코드 검수

- [ ] 두 원본의 실제 경로를 기록했다.
- [ ] 강사님 기본 while과 메뉴 코드가 실제 실행됨을 기록했다.
- [ ] 내 코드가 대부분 주석 처리 상태임을 기록했다.
- [ ] `whilte` 오타를 기록했다.
- [ ] `드릴께요`와 `드릴게요` 차이를 기록했다.
- [ ] while 조건상 menu 0 내부 분기가 도달하기 어려움을 설명했다.
- [ ] 조건식 종료와 break 중복을 설명했다.
- [ ] 네이버 접근과 while true 설명의 부정확함을 기록했다.
- [ ] 강사님 typeof와 isNaN 예제를 기록했다.
- [ ] 강사님 정사각형 문제와 업다운 문제가 미완성임을 기록했다.
- [ ] 내 입출금 프로그램의 입력 검증 문제를 기록했다.
- [ ] `bank_input >= 0`이 정수 검사가 아님을 기록했다.
- [ ] 내 업다운 코드의 null 판정 오류를 기록했다.
- [ ] 내 업다운 코드의 count 중복 증가를 기록했다.
- [ ] 유효하지 않은 입력도 시도 횟수에 포함되는 문제를 기록했다.

---

# Key Summary

- while은 조건식이 truthy인 동안 반복한다.
- while에서는 초기화와 값 갱신이 괄호 밖에 있어 누락하기 쉽다.
- 반복 조건에 사용되는 값이 바뀌지 않으면 무한 반복이 발생할 수 있다.
- 반복 횟수가 명확하면 for, 종료 시점이 입력에 따라 달라지면 while이 자연스러운 경우가 많다.
- do...while은 실행 후 조건을 검사하므로 최소 한 번 실행된다.
- 강사님 코드는 기본 while, 메뉴 while, do...while을 실제 실행 상태로 작성한다.
- 내 코드는 대부분의 예제를 주석 처리해 설명과 문제 풀이 중심으로 확장했다.
- 강사님 메뉴 while은 `menu != 0` 조건 때문에 내부의 `menu == 0` 분기가 도달하기 어렵다.
- while 조건 종료와 내부 break 종료가 중복되어 있다.
- 내 코드의 `whilte`는 `while` 오타다.
- 웹 서버의 지속 접근을 브라우저의 `while(true)`로 설명하는 것은 부정확하다.
- prompt는 문자열 또는 null을 반환한다.
- prompt 취소는 Number 변환 전에 검사해야 한다.
- `Number(null)`과 `Number("")`는 모두 0이 될 수 있다.
- 메뉴 문자열은 `"1"`, `"2"`, `"0"`처럼 엄격 비교할 수 있다.
- 입출금 잔액은 반복문 밖에서 선언해야 상태가 유지된다.
- `bank_input >= 0`은 정수 검사 조건이 아니다.
- 입출금액은 취소, 빈 값, NaN, 소수, Infinity, 0 이하를 검증할 수 있다.
- 출금액은 현재 잔액을 초과할 수 없다.
- 내 입출금 코드는 정상 입출금 후 잔액 출력이 빠져 있다.
- 주사위 1~6 난수는 `Math.floor(Math.random() * 6) + 1`로 만들 수 있다.
- 특정 값이 나올 때까지 `while(true)`로 반복하고 break할 수 있다.
- 업다운 게임의 랜덤 정답은 반복문 밖에 선언해야 유지된다.
- 내 업다운 코드에서 prompt 취소는 Number 변환 후 null과 비교해 제대로 구분할 수 없다.
- 빈 문자열도 0으로 변환되어 게임 종료로 처리될 수 있다.
- 시도 횟수는 유효한 입력을 처리할 때만 증가시키는 것이 자연스럽다.
- 내 정답 출력의 `${updown_cnt++}`는 카운트를 불필요하게 한 번 더 증가시킨다.
- 강사님 코드는 `typeof`와 전역 `isNaN()` 예제를 추가하지만 암묵적 변환 주의점은 설명하지 않는다.
- 강사님 정사각형 테두리와 업다운 게임은 요구사항만 있고 풀이가 없다.
