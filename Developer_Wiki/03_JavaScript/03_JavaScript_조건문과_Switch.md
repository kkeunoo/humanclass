# JavaScript 조건문과 Switch

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `03_JavaScript_조건문과_Switch.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `02_JavaScript_연산자.md` |
| 다음 학습 | `04_JavaScript_반복문.md` |
| 원본 기준 | `workspace_me/workspace/workspace_html/javascript/03_if.html`, `workspace_teacher/workspace_teacher/workspace_html/javascript/03_if.html` |
| 핵심 범위 | `if`, `else`, `else if`, 중첩 조건문, 실행 블록, truthy·falsy, 단일 문장 조건문, `switch`, `case`, `break`, `default`, 범위 조건, 난수, 입력 검증, 조건문 문제 풀이 |
| 프로젝트 연결 | 로그인·권한 분기, 성적 판정, 입력 검증, 메뉴 선택, 상태 메시지, 랜덤 게임, 시간 계산, 좌표 판정 |

> 이 문서는 내 코드와 강사님 코드의 `03_if.html`을 직접 비교해 작성했습니다. 강사님 코드는 조건문의 핵심 개념과 문제 목록을 제시하고, 내 코드는 문제 1~11의 풀이와 상세 설명을 추가했습니다. 원본의 오타, 부정확한 조건, 누락된 검증, 잘못된 출력은 조용히 수정하지 않고 그대로 기록한 뒤 개선 방향을 설명합니다.

---

# 학습 목표

- 조건식이 Boolean으로 평가되는 과정을 이해한다.
- `if`, `else`, `else if`의 실행 흐름을 설명한다.
- 독립된 `if` 여러 개와 하나의 `if...else` 체인의 차이를 구분한다.
- 중첩 조건문과 연속된 `else if`를 비교한다.
- 실행 블록과 중괄호의 역할을 이해한다.
- truthy와 falsy의 기본 규칙을 설명한다.
- `switch`, `case`, `break`, `default`의 역할을 이해한다.
- 여러 case를 묶는 fall-through 패턴을 작성한다.
- 범위 비교는 논리 연산자로 나누어 작성해야 함을 이해한다.
- `prompt()` 입력을 숫자로 변환하고 유효성을 검증한다.
- 양수·음수, 홀수·짝수, 큰 수, 교통수단, 가위바위보, 범위, 계절, 온도, 시간, 자리 비교, 369 게임 문제를 해결한다.
- `Math.random()`의 범위와 정수 난수 공식을 이해한다.
- 내 코드와 강사님 코드의 차이를 실제 원본에 근거해 설명한다.

---

# 1. 조건문이란?

조건문은 주어진 조건에 따라 실행할 코드를 선택합니다.

```js
if (조건식) {
  조건이 참일 때 실행
}
```

조건식은 최종적으로 truthy 또는 falsy로 평가됩니다.

```js
const score = 85

if (score >= 60) {
  console.log("합격")
}
```

`score >= 60`의 결과는 `true`이므로 블록이 실행됩니다.

---

# 2. 원본 문서 구조

두 원본 모두 HTML의 `<head>` 안에 내부 `<script>`를 작성합니다.

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
    // 조건문 실습
  </script>
</head>
<body>
</body>
</html>
```

본문은 비어 있으며 결과는 Console에서 확인합니다.

내 코드에는 파일 끝에 주석 처리된 CSS와 HTML 실험 코드도 포함되어 있습니다.

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
<title>JavaScript 조건문과 Switch</title>
```

---

# 4. 부정 연산자와 If

공통 원본:

```js
let value = false

if (!value) {
  console.log("이거 true임")
}
```

`value`는 false입니다.

```text
!false
→ true
```

따라서 블록이 실행됩니다.

출력:

```text
이거 true임
```

---

# 5. 독립된 If 두 개

공통 원본:

```js
let value2 = true

if (value2) {
  console.log("참")
}

if (!value2) {
  console.log("거짓")
}
```

두 조건문은 서로 독립적입니다.

현재 값에서는 첫 번째만 실행되지만, 일반적으로 독립된 `if`는 각각 조건을 검사합니다.

```text
첫 번째 if 검사
두 번째 if 검사
```

---

# 6. If Else

공통 원본:

```js
let value3 = true

if (value3) {
  console.log("참")
} else {
  console.log("거짓")
}
```

`if...else`는 둘 중 하나만 실행됩니다.

```text
조건이 truthy → if 블록
조건이 falsy  → else 블록
```

내 코드 주석:

```js
//위처럼 not(!)으로도 쓸 수 있지만 if, else로 보편적 사용
```

핵심은 두 반대 조건을 별도 `if`로 작성하기보다 하나의 `if...else` 체인으로 표현할 수 있다는 의미입니다.

---

# 7. 독립 If와 Else 체인의 차이

내 코드 주석:

```js
//if 2개로 표현도 가능하지만, else를 쓰면 컴퓨터가 1번만 일 하기 때문에 차이가 있음
```

이 설명은 단순화되어 있습니다.

정확한 차이:

```text
독립된 if 두 개
→ 각 조건을 각각 검사
→ 둘 다 실행될 수도 있고 둘 다 실행되지 않을 수도 있음

if...else
→ 첫 조건을 검사
→ 두 블록 중 정확히 하나만 실행
```

`else`가 반드시 “컴퓨터가 한 번만 일한다”는 의미는 아닙니다. 핵심은 하나의 배타적인 분기 구조라는 점입니다.

---

# 8. 합격과 불합격

공통 원본:

```js
let score = 85

if (score >= 60) {
  console.log("합격")
} else {
  console.log("불합격")
}
```

결과:

```text
합격
```

60 이상이면 합격, 그 외에는 불합격입니다.

---

# 9. 반대 조건 표현

공통 원본:

```js
if (score < 60) { }
if (!(score >= 60)) { }
```

두 조건은 같은 의미입니다.

```text
score < 60
!(score >= 60)
```

내 코드 주석:

```js
//크거나 같다의 반대는 작다
```

논리적으로 맞습니다.

가독성을 위해 가능한 경우 직접 비교를 권장합니다.

```js
score < 60
```

이중 부정이나 복잡한 괄호보다 읽기 쉽습니다.

---

# 10. 중첩 조건문

공통 원본:

```js
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

현재 점수는 85이므로:

```text
score >= 90 → false
score >= 80 → true
```

결과는 B입니다.

---

# 11. 범위 조건 생략 가능성

내 코드 주석:

```js
//if(score < 90 && score >= 80) 으로도 작성 가능하지만,
//이미 if첫문단에서 90이상은 걸림
```

`else` 블록에 도달했다는 것은 이미 `score >= 90`이 false라는 뜻입니다.

따라서 다음 조건만 검사해도 됩니다.

```js
score >= 80
```

범위로 풀어 쓰면:

```js
score < 90 && score >= 80
```

둘 다 동작하지만 앞선 분기의 보장을 활용하면 조건을 간결하게 작성할 수 있습니다.

---

# 12. Else If 체인

공통 원본:

```js
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

85점의 결과는 B입니다.

위에서부터 조건을 검사하고 처음 true가 된 블록만 실행한 뒤 전체 체인을 종료합니다.

---

# 13. 조건 순서의 중요성

다음처럼 넓은 조건을 먼저 쓰면 문제가 생깁니다.

```js
if (score >= 60) {
  console.log("D 이상")
} else if (score >= 90) {
  console.log("A")
}
```

95도 첫 번째 조건에서 걸리므로 A에 도달하지 않습니다.

범위 조건은 일반적으로 더 엄격한 조건부터 배치합니다.

```text
90 이상
80 이상
70 이상
그 외
```

---

# 14. Else If와 Else 개수

내 코드 주석:

```js
//else if는 여러개로 쓸 수 있지만, else는 단 1개만 존재해야 함
```

하나의 `if` 체인에서:

- `if`는 시작에 하나
- `else if`는 0개 이상
- `else`는 마지막에 0개 또는 1개

사용할 수 있습니다.

`else` 뒤에는 조건을 작성하지 않습니다.

---

# 15. 실행 블록

내 코드 주석:

```js
//{}로 감싼곳이 실행블럭이라고 불림
```

중괄호로 묶인 부분을 블록이라고 합니다.

```js
{
  console.log("첫 번째 문장")
  console.log("두 번째 문장")
}
```

조건이 참이면 블록 내부 문장들이 함께 실행됩니다.

---

# 16. Truthy와 Falsy

원본 주석:

```js
/*
  js에서
  참(true)의 정의 : 거짓이 아닌 것
  거짓 : false, 0, undefined, null, NaN
*/
```

내 코드에서는 다음처럼 확장되어 있습니다.

```text
false, 0, undefined, null, NaN
```

하지만 JavaScript의 대표 falsy 값에는 빈 문자열도 포함됩니다.

```js
false
0
-0
0n
""
null
undefined
NaN
```

원본의 “아래 5가지가 아닌 모든 것”은 정확하지 않습니다. 빈 문자열 `""`도 falsy입니다.

---

# 17. 문자열 `"0"`과 빈 배열 주의

다음 값들은 truthy입니다.

```js
"0"
"false"
[]
{}
```

예:

```js
if ("false") {
  console.log("실행됨")
}
```

문자열 내용이 “false”여도 빈 문자열이 아니므로 truthy입니다.

---

# 18. 중괄호 생략

내 코드:

```js
if (true)
  console.log(1)
```

실행 문장이 하나라면 중괄호를 생략할 수 있습니다.

하지만 다음처럼 코드가 추가되면 의도와 다르게 동작할 수 있습니다.

```js
if (condition)
  console.log("조건부")
  console.log("항상 실행")
```

두 번째 `console.log()`는 조건문 밖입니다.

실무에서는 한 줄이어도 중괄호 사용을 권장하는 경우가 많습니다.

---

# 19. 한 줄 조건문

공통 원본:

```js
let ac = 17

if (ac < 18) ac = 18
```

최솟값을 보정하는 예제입니다.

```text
ac가 18보다 작음
→ ac를 18로 변경
```

내 코드 주석의 `minumum`은 `minimum`의 오타입니다.

더 명확한 방법:

```js
const adjustedAge = Math.max(ac, 18)
```

다만 현재 단원에서는 조건문 자체를 학습하는 예제로 봅니다.

---

# 20. Fruit If Else

공통 원본:

```js
let fruit = "apple"

if (fruit == "apple") {
  console.log("사과")
} else if (fruit == "banana") {
  console.log("바나나")
} else {
  console.log("알 수 없음")
}
```

강사님 코드는 기본 출력이 `"모름"`, 내 코드는 `"알 수 없음"`입니다.

비교에는 엄격 비교를 사용할 수 있습니다.

```js
fruit === "apple"
```

---

# 21. Switch 기본 구조

공통 원본:

```js
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

구성:

```text
switch 값
→ 비교 대상

case
→ 일치할 후보

break
→ switch 종료

default
→ 일치하는 case가 없을 때
```

---

# 22. Switch 비교 방식

`switch`는 case 값과 엄격한 비교에 가까운 방식으로 일치 여부를 확인합니다.

```js
switch (3) {
  case "3":
    console.log("문자열")
    break
  case 3:
    console.log("숫자")
}
```

숫자 case가 선택됩니다.

따라서 prompt의 문자열을 그대로 switch에 사용할 때 case도 문자열로 작성해야 합니다.

---

# 23. Break의 역할

`break`가 없으면 다음 case의 코드까지 이어서 실행될 수 있습니다.

```js
switch (fruit) {
  case "apple":
    console.log("사과")
  case "banana":
    console.log("바나나")
}
```

fruit가 apple이면 두 출력이 모두 실행될 수 있습니다.

이를 fall-through라고 합니다.

의도한 case 묶음이 아니라면 `break`를 작성합니다.

---

# 24. Default의 Break

마지막 `default` 뒤에는 더 실행할 case가 없으므로 `break`가 없어도 결과는 같습니다.

강사님 fruit switch에는 default 뒤 `break`가 있고, 내 코드에는 없습니다.

둘 다 현재 구조에서는 동작합니다.

일관성을 위해 작성할 수도 있지만 필수는 아닙니다.

---

# 25. Switch 사용 설명 검토

내 코드 주석:

```js
//if에서 ==같다만 스위치로 옮길 수 있기 때문에 주로 사용하지는 않음
```

이 설명은 지나치게 제한적입니다.

정확한 의미:

- switch는 하나의 표현식 결과를 여러 case 값과 일치 비교할 때 적합합니다.
- 범위 비교나 복잡한 논리식에는 `if`가 더 적합합니다.
- switch가 “주로 사용되지 않는다”고 일반화하기는 어렵습니다.
- 메뉴, 상태 코드, 명령, 열거형 값 분기에 유용합니다.

---

# 26. Phone If

공통 원본:

```js
let phone = "s23"

if (phone == "s23") {
  console.log("삼성")
} else if (phone == "s24") {
  console.log("삼성")
}
```

서로 다른 값에서 같은 결과를 출력합니다.

이 경우 OR 조건이나 switch case 묶음을 사용할 수 있습니다.

강사님 코드에는 다음 입력 예제가 주석으로 있습니다.

```js
// let phone = prompt('기종을 입력하세요')
```

내 코드에는 없습니다.

---

# 27. OR 조건으로 모델 묶기

공통 원본:

```js
if (
  phone == "s23" ||
  phone == "s24" ||
  phone == "s25" ||
  phone == "s26"
) {
  console.log("삼성")
}
```

여러 모델 중 하나와 일치하면 삼성으로 출력합니다.

엄격 비교 개선:

```js
phone === "s23"
```

더 확장하면 배열의 `includes()`를 사용할 수 있습니다.

```js
const samsungModels = ["s23", "s24", "s25", "s26"]

if (samsungModels.includes(phone)) {
  console.log("삼성")
}
```

---

# 28. Switch Case 묶기

공통 원본:

```js
switch (phone) {
  case "s23":
  case "s24":
  case "s25":
  case "s26":
    console.log("삼성")
    break
}
```

중간 case에 실행문과 break가 없으므로 마지막 case의 코드까지 이어집니다.

의도적인 fall-through 패턴입니다.

---

# 29. 내 코드의 Apple 출력 오류

내 코드:

```js
case "i15":
case "i16":
case "i17":
  console.log("삼성")
  break
```

강사님 코드:

```js
case "i15":
case "i16":
case "i17":
  console.log("애플")
  break
```

내 코드의 iPhone case에서 `"삼성"`을 출력하는 것은 명백한 잘못입니다.

원본은 보존하되 개선안에서는 `"애플"`로 작성합니다.

---

# 30. 문제 목록 비교

강사님 코드는 문제 1~12의 요구사항만 제시합니다.

내 코드는:

- 문제 1~11 풀이를 주석 처리 상태로 작성
- 문제별 설명 주석 추가
- 문제 9 참고 풀이 추가
- 문제 12는 요구사항만 남김
- 난수와 범위 비교 실습 코드를 확장

했습니다.

---

# 31. Prompt 입력의 기본 특성

`prompt()`는 문자열 또는 null을 반환합니다.

```js
const input = prompt("숫자를 입력하세요")
```

숫자 비교 연산에서는 암묵적 변환이 일어날 수 있지만 명시적으로 변환하는 것이 안전합니다.

```js
const value = Number(input)
```

취소 검증:

```js
if (input === null) {
  console.log("입력을 취소했습니다.")
}
```

---

# 32. 숫자 입력 검증

권장 기본 흐름:

```js
const input = prompt("숫자를 입력하세요")

if (input === null || input.trim() === "") {
  console.log("값을 입력하세요.")
} else {
  const number = Number(input)

  if (Number.isNaN(number)) {
    console.log("숫자만 입력하세요.")
  } else {
    console.log(number)
  }
}
```

`Number("")`는 0이 되므로 빈 문자열을 먼저 구분해야 합니다.

---

# 33. 문제 1: 양수·0·음수

강사님 요구:

```text
아무 숫자나 받아
양수, 0, 음수 중 하나 출력
```

내 코드 주석은 다음과 같습니다.

```text
0도 양수로 침
```

그리고 실제 코드는:

```js
if (q1_num >= 0) {
  console.log("양수")
} else if (q1_num < 0) {
  console.log("음수")
}
```

즉, 0을 별도 출력하지 않고 양수에 포함합니다.

강사님 문제 문구는 `"양수" 또는 0 또는 "음수"`로 0을 별도로 분류하는 의미에 더 가깝습니다.

---

# 34. 문제 1의 입력 검증 문제

내 코드는 prompt 문자열을 그대로 비교합니다.

```js
if (q1_num >= 0)
```

문자 입력은 비교 과정에서 NaN으로 변환되어 else에 도달할 수 있습니다.

하지만 빈 문자열은 0으로 변환되어 양수로 처리됩니다.

개선:

```js
const input = prompt("숫자를 입력하세요")

if (input === null || input.trim() === "") {
  console.log("값을 입력하세요.")
} else {
  const number = Number(input)

  if (Number.isNaN(number)) {
    console.log("숫자만 입력하세요.")
  } else if (number > 0) {
    console.log("양수")
  } else if (number === 0) {
    console.log("0")
  } else {
    console.log("음수")
  }
}
```

---

# 35. 문제 2: 홀수·짝수

내 코드:

```js
let q2_result = Number(q2_num)

if (q2_result % 2 == 0) {
  console.log("짝수")
} else if (!q2_result % 2 == 0) {
  console.log("홀수")
} else {
  console.log("오류")
}
```

첫 조건은 짝수를 판별합니다.

두 번째 조건은 의도와 다르게 해석될 수 있습니다.

---

# 36. 문제 2의 연산자 우선순위 오류

```js
!q2_result % 2 == 0
```

`!`가 먼저 적용됩니다.

개념적으로:

```js
(!q2_result) % 2 == 0
```

예를 들어 q2_result가 3이면:

```text
!3 → false
false % 2 → 0
0 == 0 → true
```

우연히 홀수에서 true가 될 수 있지만 의도가 매우 불명확하며 일부 값에서 검증 로직이 제대로 동작하지 않습니다.

정확한 홀수 판별:

```js
q2_result % 2 !== 0
```

---

# 37. 문제 2의 NaN 처리 문제

NaN의 경우:

```js
NaN % 2
→ NaN
```

첫 조건은 false입니다.

하지만 두 번째 식은:

```js
!NaN
→ true
true % 2
→ 1
1 == 0
→ false
```

따라서 else로 갈 수 있습니다.

그러나 빈 문자열은 Number("")가 0이므로 짝수로 처리됩니다.

검증을 조건 앞에 배치해야 합니다.

---

# 38. 문제 3: 두 수 중 큰 값

내 코드는 두 prompt 값을 Number로 변환합니다.

```js
let q3_val1 = Number(q3_num1)
let q3_val2 = Number(q3_num2)
```

분기:

```text
첫 번째가 큼
두 번째가 큼
둘이 같음
그 외 오류
```

구조는 학습 목적에 적합합니다.

---

# 39. 문제 3의 NaN 검증

NaN은 모든 크기 비교와 동등 비교가 false입니다.

따라서 문자 입력 시 마지막 else에 도달합니다.

다만 빈 문자열은 0이 되므로 정상 숫자로 처리됩니다.

명시적 검증:

```js
if (
  Number.isNaN(value1) ||
  Number.isNaN(value2)
) {
  console.log("숫자만 입력하세요.")
}
```

---

# 40. 문제 3 개선

```js
if (value1 > value2) {
  console.log(`큰 수: ${value1}`)
} else if (value1 < value2) {
  console.log(`큰 수: ${value2}`)
} else {
  console.log("두 수가 같습니다.")
}
```

유효성 검증을 먼저 끝냈다면 마지막 else는 동일한 값만 의미하게 됩니다.

---

# 41. 문제 4: 교통수단 선택

강사님 요구:

```text
7,000원 이상 → 택시
3,000원 이상 7,000원 미만 → 버스
3,000원 미만 → 도보
```

내 코드:

```js
if (q4_money >= 7000) {
  console.log("택시타자")
} else if (q4_money >= 3000) {
  console.log("버스타자")
} else if (q4_money < 3000) {
  console.log("걸어가자")
} else {
  console.log("정확한 금액을 입력해주세요.")
}
```

범위 순서는 올바릅니다.

---

# 42. 문제 4의 설명 오류

내 코드 주석:

```js
// 정수는 포함이기에 별도 Number치환 없음
```

prompt는 정수를 입력해도 문자열을 반환합니다.

비교 연산에서 자동 숫자 변환이 일어나는 것일 뿐, 입력이 Number가 된 것은 아닙니다.

정확한 설명:

```text
prompt 결과는 문자열이지만 숫자 비교 과정에서 암묵적 변환이 일어날 수 있다.
명시적으로 Number로 변환하는 편이 안전하다.
```

---

# 43. 문제 4의 음수 처리

현재 코드는 음수 금액도 3,000원 미만이므로 `"걸어가자"`를 출력합니다.

업무 규칙상 음수 금액을 허용하지 않는다면 먼저 검증해야 합니다.

```js
if (money < 0) {
  console.log("0원 이상을 입력하세요.")
}
```

---

# 44. 문제 5-1: 컴퓨터가 항상 바위

내 코드는 엄격 비교를 사용합니다.

```js
if (q5_rps === "가위") {
  console.log("졌습니다.")
} else if (q5_rps === "바위") {
  console.log("비겼습니다.")
} else if (q5_rps === "보") {
  console.log("이겼습니다.")
}
```

문자열 후보를 정확히 구분하는 적절한 구조입니다.

---

# 45. 문제 5-2: 랜덤 가위바위보

내 코드:

```js
let rand = parseInt(Math.random() * 10) % 3
```

0, 1, 2 중 하나를 만들려는 코드입니다.

하지만 분포가 균등하지 않습니다.

---

# 46. 랜덤 분포 문제

`parseInt(Math.random() * 10)`은 0~9를 거의 균등하게 생성합니다.

그 후 `% 3`을 적용하면:

```text
0 → 0
1 → 1
2 → 2
3 → 0
4 → 1
5 → 2
6 → 0
7 → 1
8 → 2
9 → 0
```

결과 0은 네 번, 1과 2는 세 번씩 나타납니다.

따라서 가위 확률이 더 높습니다.

균등한 0~2:

```js
Math.floor(Math.random() * 3)
```

---

# 47. ParseInt와 Math Floor

원본은 난수 정수화에 `parseInt()`를 사용합니다.

```js
parseInt(Math.random() * 3)
```

양수에서는 기대한 결과가 나오지만 문자열 파싱 함수보다 숫자 내림 함수가 의도를 잘 표현합니다.

```js
Math.floor(Math.random() * 3)
```

---

# 48. 가위바위보 승패 조건

내 코드는 비김, 패배, 승리 순으로 분기합니다.

```js
if (user === computer) {
  // 비김
} else if (
  user === "가위" && computer === "바위" ||
  user === "바위" && computer === "보" ||
  user === "보" && computer === "가위"
) {
  // 패배
} else {
  // 승리 또는 오류
}
```

`&&`가 `||`보다 우선순위가 높지만 각 쌍에 괄호를 쓰면 읽기 쉽습니다.

---

# 49. 문제 5-2의 느슨한 비교

컴퓨터 값과 사용자 값은 모두 문자열이므로 `==` 대신 `===`를 사용할 수 있습니다.

```js
q5_rps === com_rps
```

원본 문제 5-1에서는 엄격 비교를 사용하지만 5-2에서는 느슨한 비교로 바뀝니다.

일관성을 유지하는 것이 좋습니다.

---

# 50. 문제 6: 세 번째 수가 두 수 사이인지

내 코드:

```js
if (num1 > num3 && num2 < num3) {
  console.log("사이에 있음")
} else if (num1 < num3 && num2 > num3) {
  console.log("사이에 있음")
}
```

x와 y의 대소 순서가 어느 쪽이든 처리합니다.

---

# 51. 문제 6의 간결한 범위 판정

다음처럼 최솟값과 최댓값을 구할 수 있습니다.

```js
const min = Math.min(x, y)
const max = Math.max(x, y)

const isBetween =
  z > min && z < max
```

경계 포함이면:

```js
z >= min && z <= max
```

원본은 중복값을 별도 메시지로 처리하므로 경계를 제외한 “사이”를 의미합니다.

---

# 52. 문제 6의 중복값 처리

내 코드:

```js
else if (
  num1 === num2 ||
  num1 === num3 ||
  num2 === num3
) {
  console.log("중복된 값을 입력하셨습니다.")
}
```

세 값 중 어느 두 값이라도 같으면 중복으로 처리합니다.

문제 요구가 경계를 포함하는지 여부에 따라 이 정책은 달라질 수 있습니다.

---

# 53. 문제 7: 월과 계절

내 코드는 switch를 사용합니다.

```js
case "12":
case "1":
case "2":
  console.log("겨울")
  break
```

prompt 결과가 문자열이므로 case도 문자열입니다.

1~12 외 값은 default에서 재입력을 요구합니다.

---

# 54. 계절 기준은 정책

내 코드 주석:

```text
계절의 경우 명확하지 않으나 3개월씩 잘라 4개의 계절로 표현
```

맞는 설명입니다.

계절 구분은 문제에서 정한 기준입니다.

이 예제에서는:

```text
12~2 겨울
3~5 봄
6~8 여름
9~11 가을
```

을 사용합니다.

---

# 55. 문제 8: 영상과 영하

내 코드:

```js
if (temp >= 0 && temp <= 50) {
  console.log(`영상 ${temp}도`)
} else if (temp < 0 && temp >= -50) {
  console.log(`영하 ${temp}도`)
}
```

음수 온도를 그대로 출력하므로 `-3` 입력 시:

```text
영하 -3도
```

가 됩니다.

문제 기대 출력은 `"영하 3도"`입니다.

---

# 56. 문제 8 개선

절댓값을 사용합니다.

```js
if (temp >= 0) {
  console.log(`영상 ${temp}도`)
} else {
  console.log(`영하 ${Math.abs(temp)}도`)
}
```

내 코드 주석에는 `-1을 곱한다`는 아이디어가 있지만 실제 출력 코드에는 적용되지 않았습니다.

---

# 57. 문제 8의 위험 문구

내 코드:

```js
console.log("현재 온도에서 당신은 죽을수도 있습니다.")
```

원본 학습 코드의 추가 메시지입니다.

문법 문제는 아니지만 실제 서비스에서는 단정적이고 자극적인 문구보다 중립적인 안내가 적합합니다.

```text
입력 가능한 범위는 -50도에서 50도입니다.
```

`죽을수도`는 띄어쓰기상 `죽을 수도`가 자연스럽습니다.

---

# 58. 문제 9: 35분 후 시간

내 코드 분기:

```js
if (min <= 60 && min >= 25) {
  time++
  console.log(`${time}시 ${min - 25}분`)
} else if (min >= 0 && min < 25) {
  console.log(`${time}시 ${min + 35}분`)
}
```

35분을 더했을 때 60분 이상이면:

```text
min + 35 - 60
= min - 25
```

가 되므로 기본 계산은 맞습니다.

---

# 59. 문제 9의 분 입력 범위 오류

유효한 분 범위는 일반적으로 0~59입니다.

원본 prompt:

```text
분(1~60)
```

조건도 `min <= 60`을 허용합니다.

60분 입력은 이미 다음 시간의 0분과 같은 값이므로 일반적인 시각 입력으로는 부적절합니다.

권장:

```js
min >= 0 && min <= 59
```

---

# 60. 문제 9의 24시 처리 누락

23시 30분에 35분을 더하면 24시 5분이 아니라 0시 5분으로 순환해야 합니다.

내 첫 풀이에는 이 처리가 없습니다.

내 코드의 참고형에는 다음이 있습니다.

```js
if (hour >= 24) {
  hour -= 24
}
```

참고형이 자정 순환까지 더 완전합니다.

---

# 61. 문제 9의 일반화된 계산

```js
let totalMinutes =
  hour * 60 + minute + 35

totalMinutes %= 24 * 60

const resultHour =
  Math.floor(totalMinutes / 60)

const resultMinute =
  totalMinutes % 60
```

분 단위로 합산하면 조건문을 줄이고 여러 시간 증가도 처리할 수 있습니다.

---

# 62. 중복된 오전·오후 조건

내 코드의 재검토 주석:

```js
else if(min >= 0 && min < 25 && time >= 12 && time < 24) {
  ...
} else if(min >= 0 && min < 25 && time >= 12 && time < 24) {
  ...
}
```

두 조건이 완전히 동일합니다.

두 번째 분기는 절대 실행될 수 없습니다.

오전·오후를 나누려면 시간 범위를 다르게 작성해야 합니다.

---

# 63. 문제 10: 두 자리 숫자의 자리 비교

내 코드 방법 1:

```js
if (num1 % 11 == 0) {
  console.log("같음")
}
```

두 자리 양수에서 11의 배수는 십의 자리와 일의 자리가 같습니다.

```text
11, 22, 33, ..., 99
```

학습용으로 동작합니다.

---

# 64. 문제 10의 검증 순서 오류

현재 방법 1은 11 배수 조건을 범위 검증보다 먼저 검사합니다.

```js
if (num1 % 11 == 0) {
  ...
} else if (num1 < 10 || num1 >= 100) {
  ...
}
```

예를 들어 0도 `0 % 11 === 0`이므로 “자리가 같다”고 출력됩니다.

먼저 두 자리 범위를 검사해야 합니다.

```js
if (num < 10 || num > 99) {
  console.log("두 자리 숫자를 입력하세요.")
} else if (num % 11 === 0) {
  console.log("같습니다.")
}
```

---

# 65. 문제 10의 직접 자리 분리

더 일반적인 방법:

```js
const tens = Math.floor(num / 10)
const ones = num % 10

if (tens === ones) {
  console.log("같음")
}
```

자리 의미가 코드에 직접 드러납니다.

---

# 66. 문제 10 방법 2 검토

내 코드:

```js
let num1 = parseInt(Number(q10_num1) / 10)

if (q10_num1 / num1 == 11) {
  console.log("같음")
}
```

십의 자리를 구한 뒤 원래 수를 나누어 11인지 확인합니다.

특정 두 자리 양수에서는 동작할 수 있지만 의도가 복잡하고 0 나눗셈, 범위 외 값, 타입 강제 변환 문제가 있습니다.

직접 자리 분리가 더 명확합니다.

---

# 67. 문제 11: 369 게임

내 코드:

```js
let num1 = parseInt(q11_num / 10)
let num2 = q11_num % 10

if (
  num1 == 3 || num1 == 6 || num1 == 9 ||
  num2 == 3 || num2 == 6 || num2 == 9
) {
  console.log("박수")
}
```

두 자리 숫자의 십의 자리와 일의 자리를 검사합니다.

---

# 68. 문제 11의 범위 한계

현재 방식은 사실상 두 자리 숫자에 맞춰져 있습니다.

예:

```text
3
13
31
69
99
```

에는 적용할 수 있지만 세 자리 이상에서는 모든 자리를 검사하지 못합니다.

문자열 방식 확장:

```js
const text = String(number)

const has369 =
  text.includes("3") ||
  text.includes("6") ||
  text.includes("9")
```

---

# 69. 문제 11 출력 문자열 오류

내 코드:

```js
console.log(`계속 이어가세요. (입력하신 숫자 :  ${q11_num}`)
```

닫는 괄호 `)`가 출력 문자열에 없습니다.

JavaScript 문법상 템플릿 리터럴은 닫혀 있으므로 실행은 되지만 표시 문구가 불완전합니다.

개선:

```js
console.log(
  `계속 이어가세요. (입력하신 숫자: ${q11_num})`
)
```

---

# 70. 문제 12: 사각형 좌표 판정

강사님 요구:

```text
좌상단: x1=10, y1=20
우하단: x2=90, y2=100
입력 좌표가 사각형 내부 또는 경계에 있는지 판정
```

내 코드에는 문제 설명만 있고 실제 판정 코드는 없습니다.

조건 예:

```js
const isInside =
  x >= x1 &&
  x <= x2 &&
  y >= y1 &&
  y <= y2
```

경계도 포함하므로 `>=`, `<=`를 사용합니다.

---

# 71. Math Random 기본 범위

공통 원본:

```js
let rand = Math.random()
console.log(rand)
```

`Math.random()`은 다음 범위의 난수를 반환합니다.

```text
0 이상
1 미만
```

즉:

```text
0 <= rand < 1
```

1은 나오지 않습니다.

---

# 72. 강사님 랜덤 코드와 내 코드 차이

강사님:

```js
rand = parseInt(Math.random() * 1000) % 3
console.log(rand)
```

내 코드:

```js
console.log(parseInt(Math.random() * 10) % 3)
```

둘 다 0~2를 만들 수 있지만 `% 3` 앞의 정수 범위가 3의 배수가 아니면 결과 분포가 완전히 균등하지 않을 수 있습니다.

권장:

```js
Math.floor(Math.random() * 3)
```

---

# 73. 연속 비교 오류

공통 원본 주석:

```js
// if(3 < a < 20){
```

JavaScript에서는 수학식처럼 연속 비교할 수 없습니다.

평가 과정:

```text
3 < a
→ true 또는 false

true < 20
→ true가 1로 변환되어 1 < 20
```

따라서 의도한 범위 판정이 아닙니다.

---

# 74. 올바른 범위 비교

공통 원본:

```js
if (3 < a && a < 20) {
}
```

JavaScript에서는 각각의 비교를 논리 AND로 연결합니다.

```text
3보다 큼
그리고
20보다 작음
```

경계 포함:

```js
3 <= a && a <= 20
```

---

# 75. 정수 난수 공식

내 코드:

```js
let test =
  parseInt(
    Math.random() * (max - min + 1)
  ) + min
```

min 이상 max 이하의 정수를 생성하려는 공식입니다.

권장 표현:

```js
const randomInteger =
  Math.floor(
    Math.random() * (max - min + 1)
  ) + min
```

범위:

```text
min <= 결과 <= max
```

---

# 76. Min과 Max 순서 검증

사용자가 min과 max를 반대로 넣을 수 있다면 정렬이 필요합니다.

```js
const low = Math.min(inputA, inputB)
const high = Math.max(inputA, inputB)
```

그 후 공식에 low와 high를 사용합니다.

---

# 77. 내 코드의 주석 처리된 CSS·HTML

내 파일 끝에는 다음 실험 코드가 주석 처리되어 있습니다.

```html
<style>
  .main .test {
    position: absolute;
    top: 20px;
    left: 10px;
    right: 90px;
    bottom: 100px;
  }
</style>
```

그리고 body 안의 테스트 박스도 주석 처리되어 있습니다.

조건문 단원과 직접 관련되지 않는 이전 또는 별도 실험 코드로 보입니다.

문서화에서는 원본에 존재한다는 점을 기록하되 핵심 조건문 학습과 분리합니다.

---

# 78. My Code 분석

## 78.1 장점

- `if...else`와 독립 if의 차이를 설명하려는 주석이 있다.
- 반대 조건을 `!`와 직접 비교로 표현하는 예를 설명했다.
- 중첩 조건에서 앞선 분기로 이미 범위가 걸러진다는 점을 기록했다.
- 실행 블록과 else if 구조를 주석으로 설명했다.
- 단일 문장 if와 중괄호 생략을 보여 준다.
- fruit와 phone 예제로 if와 switch를 비교한다.
- 문제 1~11의 풀이를 직접 작성했다.
- prompt 입력값을 Number로 변환하는 시도를 했다.
- 가위바위보의 승패 경우를 AND와 OR로 구성했다.
- x와 y의 순서가 달라도 z의 사이 여부를 판정했다.
- switch case 묶음으로 계절을 구현했다.
- 35분 후 시간 계산과 자정 처리 참고 풀이를 포함했다.
- 369 게임을 자리 분리 방식으로 구현했다.
- 연속 범위 비교가 불가능한 이유를 주석으로 설명했다.
- min~max 정수 난수 공식을 작성하고 출력했다.

## 78.2 개선점

- falsy 목록에서 빈 문자열이 누락되었다.
- “else를 쓰면 컴퓨터가 한 번만 일한다”는 설명은 지나치게 단순하다.
- `minumum` 오타가 있다.
- switch를 “주로 사용하지 않는다”고 일반화한 설명은 부정확하다.
- i15~i17 case에서 `"삼성"`을 출력하는 오류가 있다.
- 문제 1은 강사님 요구와 달리 0을 양수에 포함한다.
- prompt 취소와 빈 문자열 검증이 대부분 빠져 있다.
- 문제 2의 `!q2_result % 2 == 0`은 우선순위상 부정확하다.
- 문제 4에서 prompt가 문자열이라는 사실을 잘못 설명한다.
- 랜덤 가위바위보의 `% 3` 방식은 분포가 균등하지 않다.
- 문제 5-2에서 느슨한 비교를 사용한다.
- 문제 8에서 음수를 그대로 출력해 `"영하 -3도"`가 된다.
- 문제 9는 60분을 허용하고 첫 풀이에 24시 순환이 없다.
- 오전·오후 추가 조건 두 개가 완전히 중복된다.
- 문제 10은 범위 검사보다 11의 배수 검사를 먼저 한다.
- 문제 11의 일반 출력 문자열에 닫는 괄호가 없다.
- 문제 12 풀이가 없다.
- 조건문과 무관한 CSS·HTML 실험 코드가 함께 남아 있다.

---

# 79. Teacher Code 분석

## 79.1 장점

- 부정 연산자와 조건문을 간단한 Boolean 값으로 시작한다.
- 독립 if와 if...else를 모두 보여 준다.
- 합격·불합격과 학점 분기로 범위 조건을 설명한다.
- 중첩 if와 else if 체인을 비교한다.
- truthy와 falsy 개념을 소개한다.
- 한 줄 조건문을 보여 준다.
- fruit 예제로 if와 switch를 비교한다.
- phone 예제로 OR 조건과 case 묶음을 비교한다.
- iPhone 모델은 올바르게 `"애플"`로 출력한다.
- 문제 1~12를 난이도 순으로 제시한다.
- Math.random 기본 범위와 정수 난수 아이디어를 다룬다.
- JavaScript에서 연속 비교를 직접 사용할 수 없음을 보여 준다.
- min~max 정수 난수 공식을 제시한다.

## 79.2 개선점

- truthy·falsy 목록에서 빈 문자열이 누락되었다.
- 중괄호 생략 위험에 대한 설명이 없다.
- 비교에 느슨한 동등 연산자를 사용한다.
- switch의 엄격 비교, break, fall-through 설명이 부족하다.
- 문제에 풀이와 정답이 없다.
- prompt 입력 검증 지침이 없다.
- 난수 생성에 `parseInt()`와 `%`를 사용한다.
- `parseInt(Math.random() * 1000) % 3`은 균등성 설명이 없다.
- 문제 12 이후 실제 좌표 판정 코드는 없다.
- min=1, max=45는 지정만 하고 사용하지 않는다.
- 마지막 정수 난수 표현은 계산만 하고 출력하거나 저장하지 않는다.
- 문서 언어와 제목이 콘텐츠에 맞지 않는다.

---

# 80. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기본 if 흐름 | 동일 | 동일 |
| if·else 설명 주석 | 상세 추가 | 거의 없음 |
| falsy 설명 | 5개를 한 줄로 정리 | 5개 제시 |
| 한 줄 `if(true)` 출력 | 있음 | 없음 |
| `minimum` 주석 | `minumum` 오타 포함 | 없음 |
| fruit 기본 메시지 | `알 수 없음` | `모름` |
| switch 설명 | 있음, 일부 부정확 | 없음 |
| default break | fruit에서 없음 | 있음 |
| phone prompt 예제 | 없음 | 주석으로 있음 |
| iPhone 출력 | 잘못 `"삼성"` | 올바른 `"애플"` |
| 문제 1~11 풀이 | 있음 | 없음 |
| 문제 12 풀이 | 없음 | 없음 |
| 문제 1의 0 처리 | 양수 포함 | 0 별도 요구 |
| 문제 2 홀수 조건 | 우선순위 오류 가능 | 풀이 없음 |
| 가위바위보 랜덤 | 0~9 후 `% 3` | 문제만 제시 |
| 문제 9 참고 풀이 | 있음 | 없음 |
| 문제 10 두 방법 | 있음 | 없음 |
| 문제 11 자리 분리 | 있음 | 없음 |
| 랜덤 `% 3` 범위 | `*10` | `*1000` |
| 최종 난수 저장·출력 | `test` 저장 후 출력 | 계산만 함 |
| CSS·HTML 주석 코드 | 있음 | 없음 |

---

# 81. 공통 핵심 코드

```js
let value = false

if (!value) {
  console.log("이거 true임")
}

let value3 = true

if (value3) {
  console.log("참")
} else {
  console.log("거짓")
}

let score = 85

if (score >= 90) {
  console.log("A")
} else if (score >= 80) {
  console.log("B")
} else if (score >= 70) {
  console.log("C")
} else {
  console.log("D")
}

let fruit = "apple"

switch (fruit) {
  case "apple":
    console.log("사과")
    break
  case "banana":
    console.log("바나나")
    break
  default:
    console.log("모름")
}

let phone = "s23"

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

---

# 82. 원본 통합 개선 예제

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>JavaScript 조건문과 Switch</title>
  <script src="asset/js/03_if.js" defer></script>
</head>
<body>
  <h1>JavaScript 조건문과 Switch</h1>
  <p>개발자 도구의 Console을 확인하세요.</p>
</body>
</html>
```

## JavaScript

```js
"use strict";

const score = 85;

if (score >= 90) {
  console.log("A");
} else if (score >= 80) {
  console.log("B");
} else if (score >= 70) {
  console.log("C");
} else {
  console.log("D");
}

const fruit = "apple";

switch (fruit) {
  case "apple":
    console.log("사과");
    break;
  case "banana":
    console.log("바나나");
    break;
  default:
    console.log("알 수 없음");
}

const phone = "i16";

switch (phone) {
  case "s23":
  case "s24":
  case "s25":
  case "s26":
    console.log("삼성");
    break;
  case "i15":
  case "i16":
  case "i17":
    console.log("애플");
    break;
  default:
    console.log("지원하지 않는 모델");
}
```

---

# 83. 입력 검증 통합 예제

```js
const input = prompt("정수를 입력하세요.");

if (input === null) {
  console.log("입력을 취소했습니다.");
} else if (input.trim() === "") {
  console.log("값을 입력하세요.");
} else {
  const number = Number(input);

  if (!Number.isInteger(number)) {
    console.log("정수만 입력하세요.");
  } else if (number > 0) {
    console.log("양수");
  } else if (number === 0) {
    console.log("0");
  } else {
    console.log("음수");
  }
}
```

---

# 84. 조건문 실무 작성 기준

- 입력 검증을 먼저 끝낸다.
- 정상 로직에서는 유효한 값만 다룬다.
- 넓은 조건보다 구체적인 조건을 먼저 검사한다.
- 범위는 `&&`로 각각 비교한다.
- 값 일치 분기가 많으면 switch나 매핑 객체를 검토한다.
- 단순한 두 값 선택은 삼항 연산자를 검토한다.
- 중괄호는 한 줄이어도 유지해 실수를 줄인다.
- 비교는 특별한 이유가 없다면 `===`, `!==`를 우선한다.
- 중첩이 깊어지면 조기 반환이나 함수 분리를 검토한다.
- 사용자 메시지는 중립적이고 명확하게 작성한다.

---

# 85. 자주 하는 실수

## 85.1 `if (3 < a < 20)` 작성

JavaScript에서는 수학식과 다르게 동작합니다.

```js
3 < a && a < 20
```

로 작성합니다.

## 85.2 Falsy에서 빈 문자열 누락

`""`도 falsy입니다.

## 85.3 Prompt가 숫자를 반환한다고 생각

prompt는 문자열 또는 null을 반환합니다.

## 85.4 빈 문자열을 Number로 바로 변환

`Number("")`는 0입니다. 빈 입력을 먼저 검사합니다.

## 85.5 `!value % 2 === 0`으로 홀수 판별

부정 연산자가 먼저 적용됩니다.

```js
value % 2 !== 0
```

을 사용합니다.

## 85.6 Switch case의 break 누락

의도하지 않은 다음 case 실행이 생길 수 있습니다.

## 85.7 Case 묶음의 출력값 복사 오류

내 코드처럼 iPhone case에서 삼성이라고 출력할 수 있습니다.

## 85.8 범위 검증보다 계산 조건을 먼저 검사

문제 10의 0처럼 범위 밖 값이 정상 결과로 처리될 수 있습니다.

## 85.9 영하 값에 음수 기호를 그대로 붙임

`영하 -3도`가 됩니다. `Math.abs()`를 사용합니다.

## 85.10 60분을 유효한 분으로 허용

일반 시각 입력은 0~59분입니다.

## 85.11 23시 이후 순환 누락

24시 이상이면 0시부터 다시 계산해야 합니다.

## 85.12 `% 3`이면 항상 균등 난수라고 생각

원본 정수 범위가 3의 배수가 아니면 분포가 치우칠 수 있습니다.

---

# 86. 면접·복습 포인트

## Q1. 독립된 if 두 개와 if...else의 차이는 무엇인가요?

독립된 if는 각 조건을 모두 검사하며 여러 블록이 실행될 수 있습니다. if...else는 하나의 배타적인 분기 체인이며 둘 중 하나만 실행됩니다.

## Q2. Else if 체인에서 조건 순서가 중요한 이유는 무엇인가요?

위에서 처음 true가 된 블록만 실행되므로 넓은 조건을 먼저 두면 뒤의 구체적인 조건에 도달하지 못할 수 있습니다.

## Q3. JavaScript의 대표 falsy 값은 무엇인가요?

`false`, `0`, `-0`, `0n`, 빈 문자열, `null`, `undefined`, `NaN`입니다.

## Q4. Switch는 어떤 경우에 적합한가요?

하나의 표현식 결과를 여러 고정된 값과 비교해 분기할 때 적합합니다.

## Q5. Break를 생략하면 어떻게 되나요?

일치한 case 이후 다음 case 코드까지 이어서 실행되는 fall-through가 발생할 수 있습니다.

## Q6. Prompt의 반환 타입은 무엇인가요?

입력 후 확인하면 문자열, 취소하면 null입니다.

## Q7. 왜 `3 < a < 20`을 사용할 수 없나요?

첫 비교 결과가 Boolean이 되고 그 Boolean이 다시 20과 비교되기 때문입니다.

## Q8. 0~2 균등 정수 난수는 어떻게 만드나요?

`Math.floor(Math.random() * 3)`을 사용합니다.

## Q9. Min~max 포함 정수 난수 공식은 무엇인가요?

`Math.floor(Math.random() * (max - min + 1)) + min`입니다.

## Q10. 문제 2의 `!q2_result % 2 == 0`이 잘못된 이유는 무엇인가요?

`!`가 나머지 연산보다 먼저 적용되어 숫자의 홀수 여부가 아니라 Boolean 변환 결과에 나머지 연산을 수행하기 때문입니다.

## Q11. 문제 8에서 영하 -3도를 어떻게 표시해야 하나요?

`Math.abs(-3)`을 사용해 `"영하 3도"`로 출력합니다.

## Q12. 문제 9에서 자정 순환은 어떻게 처리하나요?

시간이 24 이상이면 24를 빼거나 전체 분을 `24 * 60`으로 나눈 나머지를 사용합니다.

---

# Problems

## 문제 1. Boolean 조건

`isReady`가 true일 때 `"준비 완료"`를 출력하세요.

## 문제 2. If Else

숫자 7이 짝수이면 `"짝수"`, 아니면 `"홀수"`를 출력하세요.

## 문제 3. 성적 판정

점수 92를 A, B, C, D로 분류하세요.

- 90 이상 A
- 80 이상 B
- 70 이상 C
- 그 외 D

## 문제 4. Truthy Falsy

빈 문자열을 if 조건에 넣었을 때 어느 블록이 실행되는지 작성하세요.

## 문제 5. 입력 검증

prompt 취소, 빈 문자열, 숫자가 아닌 입력을 각각 구분하는 코드를 작성하세요.

## 문제 6. Switch 과일

`fruit`가 `"banana"`일 때 `"바나나"`를 출력하고 그 외에는 `"알 수 없음"`을 출력하세요.

## 문제 7. Case 묶음

`s23`, `s24`, `s25`는 삼성, `i15`, `i16`, `i17`은 애플로 출력하세요.

## 문제 8. 양수·0·음수

숫자 -5를 양수, 0, 음수 중 하나로 판정하세요.

## 문제 9. 두 수 중 큰 수

12와 27 중 큰 값을 출력하세요. 같은 경우도 처리하세요.

## 문제 10. 교통수단

보유 금액 5,000원일 때 택시, 버스, 도보 중 하나를 출력하세요.

## 문제 11. 고정 바위 가위바위보

사용자가 `"보"`를 입력했고 컴퓨터가 항상 `"바위"`일 때 승패를 출력하세요.

## 문제 12. 랜덤 가위바위보

균등한 0~2 난수를 만들고 가위, 바위, 보 중 하나로 변환하세요.

## 문제 13. 사이 값

x=20, y=5, z=12일 때 z가 두 수 사이에 있는지 판정하세요.

## 문제 14. 계절

월 10을 입력받았다고 가정하고 switch로 계절을 출력하세요.

## 문제 15. 온도

-7도를 `"영하 7도"`로 출력하세요.

## 문제 16. 35분 후

23시 50분에서 35분 후의 시간을 출력하세요.

## 문제 17. 두 자리 비교

88의 십의 자리와 일의 자리가 같은지 직접 자리 분리로 확인하세요.

## 문제 18. 369 게임

숫자 63에 3, 6, 9가 포함되어 있는지 확인하고 `"박수"`를 출력하세요.

## 문제 19. 좌표 판정

사각형 범위 x=10~90, y=20~100에서 점 (90, 100)이 겹치는지 판정하세요.

## 문제 20. 범위 비교

a=10이 3보다 크고 20보다 작은지 올바른 JavaScript 조건으로 작성하세요.

## 문제 21. 정수 난수

5 이상 8 이하의 균등한 정수 난수를 생성하세요.

## 문제 22. 종합 회원 등급

다음 요구사항을 만족하세요.

- prompt로 구매 금액 입력
- 취소, 빈 값, 숫자가 아닌 값, 음수 검증
- 100,000원 이상 VIP
- 50,000원 이상 GOLD
- 10,000원 이상 SILVER
- 그 외 BASIC
- 엄격 비교 사용
- 결과에 입력 금액과 등급 출력

---

# Answers & Explanations

## 정답 1

```js
const isReady = true

if (isReady) {
  console.log("준비 완료")
}
```

## 정답 2

```js
const number = 7

if (number % 2 === 0) {
  console.log("짝수")
} else {
  console.log("홀수")
}
```

## 정답 3

```js
const score = 92

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

## 정답 4

```js
if ("") {
  console.log("참")
} else {
  console.log("거짓")
}
```

빈 문자열은 falsy이므로 `"거짓"`이 출력됩니다.

## 정답 5

```js
const input = prompt("숫자를 입력하세요")

if (input === null) {
  console.log("취소")
} else if (input.trim() === "") {
  console.log("빈 값")
} else {
  const number = Number(input)

  if (Number.isNaN(number)) {
    console.log("숫자가 아님")
  } else {
    console.log(`숫자: ${number}`)
  }
}
```

## 정답 6

```js
const fruit = "banana"

switch (fruit) {
  case "banana":
    console.log("바나나")
    break
  default:
    console.log("알 수 없음")
}
```

## 정답 7

```js
const phone = "i16"

switch (phone) {
  case "s23":
  case "s24":
  case "s25":
    console.log("삼성")
    break
  case "i15":
  case "i16":
  case "i17":
    console.log("애플")
    break
  default:
    console.log("알 수 없음")
}
```

## 정답 8

```js
const number = -5

if (number > 0) {
  console.log("양수")
} else if (number === 0) {
  console.log("0")
} else {
  console.log("음수")
}
```

## 정답 9

```js
const a = 12
const b = 27

if (a > b) {
  console.log(a)
} else if (a < b) {
  console.log(b)
} else {
  console.log("같음")
}
```

## 정답 10

```js
const money = 5000

if (money >= 7000) {
  console.log("택시타자")
} else if (money >= 3000) {
  console.log("버스타자")
} else {
  console.log("걸어가자")
}
```

## 정답 11

```js
const user = "보"
const computer = "바위"

if (user === computer) {
  console.log("비김")
} else if (user === "보") {
  console.log("승리")
} else {
  console.log("패배")
}
```

## 정답 12

```js
const randomIndex =
  Math.floor(Math.random() * 3)

let computer

if (randomIndex === 0) {
  computer = "가위"
} else if (randomIndex === 1) {
  computer = "바위"
} else {
  computer = "보"
}

console.log(computer)
```

## 정답 13

```js
const x = 20
const y = 5
const z = 12

const min = Math.min(x, y)
const max = Math.max(x, y)

if (z > min && z < max) {
  console.log("사이에 있음")
} else {
  console.log("사이에 없음")
}
```

## 정답 14

```js
const month = 10

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
    console.log("다시 입력하세요")
}
```

## 정답 15

```js
const temperature = -7

if (temperature >= 0) {
  console.log(`영상 ${temperature}도`)
} else {
  console.log(`영하 ${Math.abs(temperature)}도`)
}
```

## 정답 16

```js
let hour = 23
let minute = 50

let totalMinutes =
  hour * 60 + minute + 35

totalMinutes %= 24 * 60

hour = Math.floor(totalMinutes / 60)
minute = totalMinutes % 60

console.log(`${hour}시 ${minute}분`)
```

결과는 `0시 25분`입니다.

## 정답 17

```js
const number = 88

const tens =
  Math.floor(number / 10)

const ones =
  number % 10

console.log(tens === ones)
```

## 정답 18

```js
const number = 63
const text = String(number)

const has369 =
  text.includes("3") ||
  text.includes("6") ||
  text.includes("9")

if (has369) {
  console.log("박수")
} else {
  console.log(number)
}
```

## 정답 19

```js
const x1 = 10
const x2 = 90
const y1 = 20
const y2 = 100

const x = 90
const y = 100

const isInside =
  x >= x1 &&
  x <= x2 &&
  y >= y1 &&
  y <= y2

console.log(isInside)
```

경계를 포함하므로 true입니다.

## 정답 20

```js
const a = 10

if (3 < a && a < 20) {
  console.log("범위 안")
}
```

## 정답 21

```js
const min = 5
const max = 8

const randomInteger =
  Math.floor(
    Math.random() * (max - min + 1)
  ) + min

console.log(randomInteger)
```

## 정답 22

```js
const input =
  prompt("구매 금액을 입력하세요.")

if (input === null) {
  console.log("입력을 취소했습니다.")
} else if (input.trim() === "") {
  console.log("금액을 입력하세요.")
} else {
  const money = Number(input)

  if (Number.isNaN(money)) {
    console.log("숫자만 입력하세요.")
  } else if (money < 0) {
    console.log("0원 이상을 입력하세요.")
  } else {
    let grade

    if (money >= 100000) {
      grade = "VIP"
    } else if (money >= 50000) {
      grade = "GOLD"
    } else if (money >= 10000) {
      grade = "SILVER"
    } else {
      grade = "BASIC"
    }

    console.log(
      `구매 금액: ${money}원, 등급: ${grade}`
    )
  }
}
```

---

# Final Checklist

## If 기본

- [ ] 조건식이 truthy 또는 falsy로 평가됨을 이해했다.
- [ ] `if`, `else`, `else if` 구조를 작성할 수 있다.
- [ ] 독립 if와 하나의 분기 체인을 구분했다.
- [ ] 조건 순서가 결과에 영향을 준다는 점을 확인했다.
- [ ] 중첩 조건문과 else if 체인을 비교했다.
- [ ] 실행 블록의 중괄호를 이해했다.
- [ ] 한 줄 조건문에서도 중괄호 사용을 검토했다.

## Truthy와 Falsy

- [ ] false, 0, 빈 문자열, null, undefined, NaN을 구분했다.
- [ ] 문자열 `"false"`는 truthy임을 이해했다.
- [ ] 빈 배열과 빈 객체도 truthy임을 이해했다.
- [ ] 부정 연산자의 결과를 예측할 수 있다.

## Switch

- [ ] switch의 비교 대상을 이해했다.
- [ ] case, break, default를 사용할 수 있다.
- [ ] break 누락 시 fall-through가 발생함을 이해했다.
- [ ] 여러 case를 같은 결과로 묶을 수 있다.
- [ ] prompt 문자열과 case 타입을 맞췄다.
- [ ] 범위 조건에는 if가 더 적합할 수 있음을 이해했다.

## 입력 검증

- [ ] prompt가 문자열 또는 null을 반환함을 이해했다.
- [ ] 취소를 먼저 검사했다.
- [ ] 빈 문자열을 먼저 검사했다.
- [ ] Number 변환 후 NaN을 검사했다.
- [ ] 정수가 필요한 경우 Number.isInteger를 검토했다.
- [ ] 음수나 범위 밖 값을 검증했다.
- [ ] 정상 로직 전에 오류 입력을 분리했다.

## 문제 해결

- [ ] 양수·0·음수를 분리했다.
- [ ] 홀수는 `% 2 !== 0`으로 판별했다.
- [ ] 두 수의 대소와 동일 여부를 처리했다.
- [ ] 금액 범위를 높은 조건부터 분기했다.
- [ ] 가위바위보 승패 조건을 작성했다.
- [ ] 두 수의 순서와 무관하게 사이 여부를 판정했다.
- [ ] 월을 계절로 변환했다.
- [ ] 영하 출력에 절댓값을 사용했다.
- [ ] 35분 후 시간에서 자정 순환을 처리했다.
- [ ] 두 자리 숫자의 자리를 직접 분리했다.
- [ ] 369 포함 여부를 검사했다.
- [ ] 사각형 경계 포함 판정을 작성했다.

## 난수와 범위

- [ ] Math.random의 범위가 0 이상 1 미만임을 이해했다.
- [ ] 0~2 정수에 `Math.floor(Math.random() * 3)`을 사용했다.
- [ ] `% 3` 방식의 분포 문제를 이해했다.
- [ ] min~max 포함 정수 난수 공식을 작성했다.
- [ ] JavaScript에서 연속 비교를 사용하지 않았다.
- [ ] 범위 비교를 `&&`로 연결했다.

## 원본 코드 검수

- [ ] 두 실제 원본 경로를 기록했다.
- [ ] falsy 목록의 빈 문자열 누락을 설명했다.
- [ ] `minumum` 오타를 기록했다.
- [ ] switch 설명의 과도한 일반화를 보완했다.
- [ ] 내 코드 iPhone case의 `"삼성"` 출력 오류를 기록했다.
- [ ] 문제 1의 0 처리 차이를 기록했다.
- [ ] 문제 2의 `!q2_result % 2 == 0` 오류를 설명했다.
- [ ] 문제 4의 prompt 타입 설명 오류를 기록했다.
- [ ] 랜덤 가위바위보의 불균등 가능성을 설명했다.
- [ ] 문제 8의 `"영하 -3도"` 문제를 기록했다.
- [ ] 문제 9의 60분 허용과 24시 순환 문제를 기록했다.
- [ ] 중복된 오전·오후 조건을 기록했다.
- [ ] 문제 10의 검증 순서 문제를 기록했다.
- [ ] 문제 11의 닫는 괄호 누락을 기록했다.
- [ ] 양쪽 모두 문제 12 풀이가 없음을 기록했다.
- [ ] 내 코드의 주석 처리된 CSS·HTML 실험 코드를 기록했다.

---

# Key Summary

- 조건문은 조건에 따라 실행할 코드 블록을 선택한다.
- 독립된 if는 각각 검사하지만 if...else는 하나의 배타적인 분기 체인이다.
- else if는 여러 개 사용할 수 있고 else는 마지막에 최대 하나 사용한다.
- 조건 순서는 구체적이고 높은 범위부터 작성해야 한다.
- 중괄호는 실행 블록을 만들며 한 줄이어도 유지하는 편이 안전하다.
- JavaScript의 falsy에는 false, 0, 빈 문자열, null, undefined, NaN 등이 있다.
- 원본 falsy 설명에는 빈 문자열이 누락되어 있다.
- `switch`는 하나의 값을 여러 고정 case와 비교할 때 적합하다.
- `break`가 없으면 다음 case까지 이어지는 fall-through가 발생할 수 있다.
- 여러 case를 묶어 같은 결과를 실행할 수 있다.
- 내 코드의 i15~i17 case는 잘못 `"삼성"`을 출력한다.
- prompt는 문자열 또는 null을 반환한다.
- 빈 문자열을 Number로 변환하면 0이므로 입력 검증을 먼저 해야 한다.
- 문제 1은 강사님 요구와 달리 0을 양수에 포함한다.
- 문제 2의 `!q2_result % 2 == 0`은 연산자 우선순위상 부정확하다.
- 홀수는 `value % 2 !== 0`으로 판별한다.
- 문제 4의 prompt 값은 정수가 아니라 문자열이다.
- 0~2 균등 난수는 `Math.floor(Math.random() * 3)`으로 만든다.
- `parseInt(Math.random() * 10) % 3`은 결과 분포가 균등하지 않다.
- 두 수 사이 판정에는 `Math.min()`과 `Math.max()`를 활용할 수 있다.
- 월의 계절 분류는 문제에서 정한 정책이다.
- 영하 출력에는 `Math.abs()`를 사용해 음수 기호를 제거한다.
- 내 문제 8 코드는 실제로 `"영하 -3도"`를 출력한다.
- 유효한 분 범위는 0~59이며 자정 이후는 0시로 순환해야 한다.
- 문제 9의 참고형은 24시 순환을 처리하지만 첫 풀이에는 없다.
- 두 자리 숫자는 십의 자리와 일의 자리를 직접 분리하는 방식이 명확하다.
- 문제 10은 범위 검사보다 11의 배수 검사를 먼저 해 0을 잘못 처리할 수 있다.
- 369 게임은 문자열 includes 방식으로 여러 자리까지 확장할 수 있다.
- 내 문제 11 출력 문구에는 닫는 괄호가 누락되어 있다.
- 문제 12 좌표 판정은 양쪽 원본 모두 실제 풀이가 없다.
- JavaScript에서는 `3 < a < 20` 대신 `3 < a && a < 20`을 사용한다.
- min~max 포함 정수 난수는 `Math.floor(Math.random() * (max - min + 1)) + min`이다.
- 내 코드는 강사님 문제 목록을 기반으로 많은 풀이와 설명을 추가했지만 검증과 일부 조건식에 개선점이 있다.
