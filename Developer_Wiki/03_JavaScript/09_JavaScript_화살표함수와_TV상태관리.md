# JavaScript 화살표 함수와 TV 상태 관리

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `09_JavaScript_화살표함수와_TV상태관리.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `08_JavaScript_함수와_콜백_타이머.md` |
| 다음 학습 | `10_JavaScript_객체와_메서드.md` |
| 원본 기준 | `workspace_me/workspace/workspace_html/javascript/09_arrow.html`, `workspace_teacher/workspace_teacher/workspace_html/javascript/09_arrow.html`, 양쪽의 `09_1_tv.html` |
| 핵심 범위 | 일반 함수 표현식, 즉시 실행 함수, 화살표 함수, 매개변수 괄호 생략, 중괄호·return 생략, 쉼표 연산자, 전역 상태, 상수 범위값, 전원·채널·볼륨·음소거 함수, wrap-around, clamp, toggle, early return, 상태 테스트 |
| 프로젝트 연결 | UI 상태 관리, 리모컨 기능, 설정값 범위 제한, 토글 버튼, 입력 검증, 함수 분리, 상태 기반 동작 |

> 이 문서는 `09_arrow.html`과 `09_1_tv.html`을 함께 분석해 작성했습니다. 첫 파일은 일반 익명 함수와 화살표 함수 문법을 비교하고, 두 번째 파일은 여러 함수가 하나의 TV 상태를 공유하는 구조를 실습합니다. 내 코드와 강사님 코드의 실제 차이, 주석과 구현의 불일치, 함수명 차이, 테스트 시나리오 차이, 논리상 보완이 필요한 부분을 원본 그대로 보존한 뒤 설명합니다.

---

# 학습 목표

- 일반 함수 표현식과 화살표 함수를 비교한다.
- 즉시 실행 함수 표현식의 호출 구조를 이해한다.
- 매개변수 개수에 따른 괄호 생략 규칙을 설명한다.
- 실행문이 하나일 때 중괄호와 `return`을 생략하는 규칙을 이해한다.
- `return a, b`가 두 값을 반환하는 문법이 아니라는 점을 설명한다.
- 전역 상태 변수와 상수 범위값을 구분한다.
- 여러 함수가 같은 상태를 읽고 변경하는 구조를 이해한다.
- 전원이 꺼진 상태에서 동작을 차단한다.
- 채널 범위를 벗어나면 처음 또는 끝으로 순환시킨다.
- 볼륨을 최소·최대 범위 안에 고정한다.
- 음소거 상태를 Boolean으로 토글한다.
- 볼륨 조절 시 음소거가 해제되는 규칙을 구현한다.
- 별도 `muteOn()`, `muteOff()`와 하나의 toggle 함수 차이를 비교한다.
- 원본 테스트 코드의 실제 상태 변화를 순서대로 추적한다.
- 내 코드와 강사님 코드의 주석·코드 불일치를 정확히 기록한다.

---

# 1. JavaScript 09번 파일 구성

이번 번호는 두 개의 학습 파일로 구성됩니다.

```text
09_arrow.html
09_1_tv.html
```

역할:

```text
09_arrow.html
→ 화살표 함수 문법

09_1_tv.html
→ 함수와 상태 변수를 이용한 TV 기능 구현
```

두 파일은 모두 함수 단원이지만 학습 목적이 다릅니다.

---

# 2. 원본 HTML 구조

두 원본 모두 `<head>` 내부 `<script>`에서 코드를 실행합니다.

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
    // JavaScript 실습
  </script>
</head>
<body>
</body>
</html>
```

결과는 브라우저 개발자 도구 Console에서 확인합니다.

---

# 3. 문서 언어와 제목

공통 원본:

```html
<html lang="en">
<title>Document</title>
```

한국어 학습 콘텐츠이므로 다음처럼 개선할 수 있습니다.

```html
<html lang="ko">
<title>JavaScript 화살표 함수와 TV 상태 관리</title>
```

---

# 4. 일반 익명 함수

공통 원본:

```js
const fn1 = function(a, b) {
  console.log(a, b)
  return a, b
}
```

`function` 뒤에 별도 함수 이름이 없으므로 익명 함수 표현식입니다.

변수 `fn1`이 함수 객체를 참조합니다.

호출:

```js
fn1(1, 2)
```

---

# 5. Return A Comma B

양쪽 원본:

```js
return a, b
```

이 코드는 두 값을 한 번에 반환하지 않습니다.

쉼표 연산자는 왼쪽 표현식을 평가한 뒤 오른쪽 표현식의 값을 결과로 사용합니다.

```js
function example(a, b) {
  return a, b
}

console.log(
  example(1, 2)
)
```

결과:

```text
2
```

두 값을 반환하려면 배열이나 객체를 사용합니다.

```js
return [a, b]
```

또는:

```js
return { a, b }
```

---

# 6. 내 코드의 Return 주석 검토

내 코드:

```text
return은 1번만 써야 한다
```

한 함수 실행 경로에서 하나의 `return`이 실행되면 함수가 종료되는 것은 맞습니다.

그러나 함수 안에 `return` 문을 문법적으로 하나만 작성해야 하는 것은 아닙니다.

```js
function check(value) {
  if (value > 0) {
    return "양수"
  }

  return "0 또는 음수"
}
```

조건에 따라 여러 return 문을 작성할 수 있습니다.

---

# 7. 즉시 실행 함수 표현식

공통 원본:

```js
(function(a, b) {
  console.log(a, b)
  return a, b
})(1, 2)
```

구조:

```text
(function(...) { ... })
→ 함수 표현식

(1, 2)
→ 바로 호출
```

별도 변수에 저장하지 않고 선언 직후 실행합니다.

이를 IIFE라고 부를 수 있습니다.

---

# 8. 내 코드의 즉시 실행 설명

내 코드:

```text
()는 실행의 괄호이기 때문에 앞에 있는 것 실행
```

핵심은 맞습니다.

더 정확한 표현:

```text
첫 괄호는 함수 표현식을 감싸고,
뒤 괄호는 그 함수에 인수를 전달해 즉시 호출한다.
```

---

# 9. 화살표 함수 기본

공통 원본:

```js
const fn2 = (a, b) => {
  console.log(a, b)
  return a, b
}
```

일반 함수 표현식:

```js
const fn2 = function(a, b) {
  console.log(a, b)
  return a, b
}
```

화살표 함수는 익명 함수 표현식을 간결하게 작성하는 문법입니다.

다만 일반 함수와 모든 동작이 완전히 같은 것은 아닙니다.

---

# 10. 내 코드의 Fn2 호출

내 코드:

```js
fn2(1, 2)
```

강사님 코드에는 `fn2` 선언만 있고 실제 호출은 없습니다.

따라서 내 파일에서는 `fn1`, IIFE, `fn2`까지 각각 Console 출력이 발생합니다.

강사님 파일에서는 `fn1`과 IIFE만 실제 출력합니다.

---

# 11. 매개변수 하나일 때 괄호 생략

공통 원본:

```js
const fn3 = a => {
  console.log(a)
  return a
}
```

매개변수가 정확히 하나일 때 괄호를 생략할 수 있습니다.

다음도 동일합니다.

```js
const fn3 = (a) => {
  return a
}
```

---

# 12. 매개변수 괄호 생략 규칙

| 매개변수 수 | 예 |
| --- | --- |
| 0개 | `() => {}` |
| 1개 | `a => {}` 또는 `(a) => {}` |
| 2개 이상 | `(a, b) => {}` |
| 기본값·구조분해 | 괄호 필요 |

예:

```js
(a = 0) => a
```

```js
({ name }) => name
```

---

# 13. 매개변수 없음

공통 원본:

```js
const fn4 = () => {
  console.log(a)
  return a
}
```

매개변수가 없으므로 빈 괄호를 생략할 수 없습니다.

중요한 문제:

`fn4` 내부의 `a`는 함수 매개변수도 아니고 이 파일에서 선언된 전역 변수도 아닙니다.

실제로 `fn4()`를 호출하면 ReferenceError가 발생할 가능성이 큽니다.

양쪽 원본은 `fn4`를 선언만 하고 호출하지 않으므로 오류가 발생하지 않습니다.

---

# 14. Fn4 개선

외부 값을 사용할 목적이라면 먼저 선언해야 합니다.

```js
const a = 10

const fn4 = () => {
  console.log(a)
  return a
}
```

매개변수로 받을 목적이라면:

```js
const fn4 = a => {
  console.log(a)
  return a
}
```

---

# 15. 실행 블록과 Return 생략

공통 원본:

```js
const fn5 = (a, b) => {
  return a + b
}
```

축약:

```js
const fn6 =
  (a, b) => a + b
```

실행문이 하나의 표현식이고 그 결과를 반환할 때 중괄호와 `return`을 함께 생략할 수 있습니다.

---

# 16. 중괄호와 Return 규칙

올바른 코드:

```js
const add =
  (a, b) => a + b
```

올바른 코드:

```js
const add = (a, b) => {
  return a + b
}
```

잘못된 의도:

```js
const add = (a, b) => {
  a + b
}
```

중괄호가 있으면 자동 반환되지 않으므로 결과는 undefined입니다.

---

# 17. Fn7

공통 원본:

```js
const fn7 =
  a => a + 100
```

매개변수 하나이므로 괄호 생략, 반환 표현식 하나이므로 중괄호와 return을 생략했습니다.

호출 예:

```js
console.log(
  fn7(20)
)
```

결과:

```text
120
```

원본에서는 선언만 하고 호출하지 않습니다.

---

# 18. 객체 리터럴 반환 확장

화살표 함수에서 객체를 바로 반환하려면 괄호로 감쌉니다.

```js
const createUser =
  name => ({ name })
```

괄호 없이:

```js
name => { name }
```

로 작성하면 중괄호를 함수 블록으로 해석하고 객체가 반환되지 않습니다.

원본에는 없는 확장 학습입니다.

---

# 19. 화살표 함수의 This 차이

화살표 함수는 자신만의 `this`를 만들지 않습니다.

일반 함수 메서드와 다를 수 있습니다.

```js
const user = {
  name: "Kim",

  normal() {
    console.log(this.name)
  },

  arrow: () => {
    console.log(this.name)
  }
}
```

객체 메서드의 `this`가 필요할 때 화살표 함수를 무조건 사용하면 안 됩니다.

원본은 `this`를 다루지 않으므로 확장 개념으로 분리합니다.

---

# 20. TV 만들기 요구사항

내 코드 주석:

```text
채널 0~10
볼륨 0~5
채널 10에서 up → 0
채널 0에서 down → 10
```

강사님 주석 첫 부분:

```text
채널 0~100
100에서 up → 0
0에서 down → 100
```

하지만 실제 상수는 양쪽 모두:

```js
const CH_MAX = 10
const CH_MIN = 0
```

따라서 강사님 주석의 `0~100`은 실제 구현과 일치하지 않습니다.

---

# 21. TV 기능 목록

공통 요구:

```text
전원 on
전원 off
채널 직접 입력
채널 up
채널 down
볼륨 up
볼륨 down
음소거 on/off
```

내 코드는 기능에 번호 1~8을 붙였습니다.

강사님 코드는 번호 없이 나열합니다.

---

# 22. 전역 상태 변수

공통 구조:

```js
let power = false
let lastCh = 0
let lastVol = 0
```

각 함수가 같은 변수를 읽고 변경합니다.

```text
power
→ 전원 상태

lastCh
→ 현재 또는 마지막 채널

lastVol
→ 현재 또는 마지막 볼륨
```

전역 상태를 사용하면 실습은 단순하지만 규모가 커지면 상태 변경 위치를 추적하기 어려울 수 있습니다.

---

# 23. 상수 범위값

공통 원본:

```js
const CH_MAX = 10
const CH_MIN = 0

const VOL_MAX = 5
const VOL_MIN = 0
```

변하지 않는 설정값이므로 `const`를 사용합니다.

대문자와 underscore를 사용하는 이름은 상수 설정값을 강조하는 관례입니다.

내 코드 주석도 이를 설명합니다.

---

# 24. 음소거 상태 변수 이름 차이

내 코드:

```js
let VOL_MUTE = false
```

강사님 코드:

```js
let status_mute = false
```

둘 다 Boolean 상태를 저장합니다.

스타일 측면에서 다음처럼 통일할 수 있습니다.

```js
let isMuted = false
```

`VOL_MUTE`는 값이 바뀌는 `let` 변수인데 대문자 상수처럼 보여 혼동될 수 있습니다.

---

# 25. Power On

공통 원본:

```js
function powerOn() {
  power = true
  console.log("TV 켜짐")
}
```

전원 상태를 true로 바꿉니다.

현재 상태가 이미 true여도 다시 true를 대입하고 같은 메시지를 출력합니다.

---

# 26. Power Off

공통 원본:

```js
function powerOff() {
  power = false
  console.log("TV 꺼짐")
}
```

전원 상태를 false로 바꿉니다.

전원을 꺼도 채널과 볼륨 값은 초기화하지 않습니다.

따라서 다시 켜면 마지막 값이 유지됩니다.

---

# 27. 내 코드의 Power One

내 코드에만 있습니다.

```js
function powerOne() {
  if (power) {
    console.log("원버튼 TV 꺼짐")
    power = false
  } else {
    console.log("원버튼 TV 켜짐")
    power = true
  }
}
```

하나의 버튼으로 전원을 토글합니다.

더 간단한 상태 반전:

```js
power = !power
```

다만 메시지를 상태별로 출력하려면 반전 후 조건을 확인할 수 있습니다.

---

# 28. Power One 미사용

내 코드는 `powerOne()`을 선언하지만 테스트 코드에서는 호출하지 않습니다.

따라서 실제 실행 결과에는 영향을 주지 않습니다.

강사님 코드에는 이 함수가 없습니다.

---

# 29. 채널 직접 입력

공통 구조:

```js
function channel(ch) {
  if (power) {
    if (
      ch < CH_MIN ||
      ch > CH_MAX
    ) {
      console.log("채널이 없습니다")
      return
    }

    lastCh = ch
    console.log(
      ch + "번으로 채널 변경"
    )
  } else {
    console.log("전원 꺼져있음")
  }
}
```

전원이 켜져 있을 때만 채널을 변경합니다.

---

# 30. Early Return

채널 범위가 잘못되면:

```js
return
```

으로 함수를 즉시 종료합니다.

내 코드 주석:

```text
return만 쓰면 해당 함수가 종료되기 때문에 else 대신 사용
```

적절한 설명입니다.

중첩을 줄이고 정상 흐름을 아래쪽에 유지할 수 있습니다.

---

# 31. 채널 입력 검증의 한계

원본 조건:

```js
ch < CH_MIN ||
ch > CH_MAX
```

다음 입력은 충분히 검증하지 않습니다.

```text
문자열 "5"
소수 3.5
NaN
undefined
```

예를 들어 `"5"`는 비교에서 숫자로 변환되어 통과하고 `lastCh`에는 문자열이 저장될 수 있습니다.

개선:

```js
if (
  !Number.isInteger(ch) ||
  ch < CH_MIN ||
  ch > CH_MAX
) {
  return
}
```

---

# 32. Channel Up

공통 원본:

```js
lastCh++

if (lastCh > CH_MAX) {
  lastCh = CH_MIN
}
```

10에서 증가하면 11이 된 뒤 0으로 돌아갑니다.

이를 순환 또는 wrap-around 동작으로 볼 수 있습니다.

---

# 33. Channel Down

공통 원본:

```js
lastCh--

if (lastCh < CH_MIN) {
  lastCh = CH_MAX
}
```

0에서 감소하면 -1이 된 뒤 10으로 돌아갑니다.

---

# 34. Modulo 확장

채널 증가를 나머지 연산으로 표현할 수 있습니다.

```js
lastCh =
  (lastCh + 1) %
  (CH_MAX + 1)
```

감소:

```js
lastCh =
  (
    lastCh - 1 +
    CH_MAX + 1
  ) %
  (CH_MAX + 1)
```

현재 범위가 0부터 시작하므로 가능한 표현입니다.

원본은 조건문 학습을 위해 if를 사용합니다.

---

# 35. 강사님 테스트 주석 오류

강사님 테스트:

```js
channel(-50) // 0
```

실제 `channel()`은 -50을 범위 밖으로 판단합니다.

출력:

```text
채널이 없습니다
```

`lastCh`를 0으로 변경하지 않습니다.

주석 `// 0`은 실제 코드와 일치하지 않습니다.

---

# 36. 내 채널 테스트 순서

내 코드:

```js
channelUp()
channel(5)
channelDown()
channel(50)
channelUp()
channel(-50)
channelDown()
```

상태 추적:

```text
초기 0
up → 1
직접 5
down → 4
50 → 거부, 4 유지
up → 5
-50 → 거부, 5 유지
down → 4
```

최종 채널은 4입니다.

---

# 37. 강사님 채널 테스트 순서

강사님 코드:

```js
channelUp()
channel(5)
channelDown()
channel(50)
channel(-50)
channel(10)
channelUp()
channel(0)
channelDown()
```

상태 추적:

```text
초기 0
up → 1
직접 5
down → 4
50 → 거부, 4 유지
-50 → 거부, 4 유지
직접 10
up → 0
직접 0
down → 10
```

최종 채널은 10입니다.

---

# 38. 볼륨 기본 요구

공통 요구:

```text
초기 볼륨 0
최대 5
최소 0
5에서 up → 5 유지
0에서 down → 0 유지
볼륨 조절 시 음소거 해제
```

강사님 코드는 이 요구를 비교적 직접 구현합니다.

내 코드는 음소거 상태에 따라 출력 문구를 분기합니다.

---

# 39. 강사님 Volume Up

```js
function volumeUp() {
  if (power) {
    status_mute = false

    lastVol++

    if (lastVol > VOL_MAX) {
      lastVol = VOL_MAX
    }

    console.log(
      "볼륨 : " + lastVol
    )
  }
}
```

볼륨 조절 시작 시 음소거를 무조건 해제합니다.

최대값을 넘으면 5로 고정합니다.

항상 현재 볼륨을 출력합니다.

---

# 40. 내 Vol Up

내 코드:

```js
function volUp() {
  if (power) {
    lastVol++

    if (lastVol > VOL_MAX) {
      lastVol = VOL_MAX
    } else if (VOL_MUTE == true) {
      console.log(
        "[음소거 해제 및 볼륨UP] 현재볼륨 : ",
        lastVol
      )
      VOL_MUTE = false
    } else {
      console.log(
        "[볼륨UP] 현재볼륨 : ",
        lastVol
      )
    }
  }
}
```

강사님과 다른 점:

- 음소거 해제를 증가 처리 뒤의 `else if`에서 수행
- 상태별 메시지 구분
- 최대값 초과 분기에서는 Console 출력이 없음

---

# 41. 내 Vol Up 최대값 출력 누락

볼륨이 이미 5일 때 `volUp()`:

```text
lastVol++ → 6
6 > 5 → 5로 복구
```

첫 번째 if가 실행되므로 뒤 `else if`, `else`는 실행되지 않습니다.

따라서 현재 볼륨 메시지를 출력하지 않습니다.

기능상 값은 5로 유지되지만 사용자 피드백이 없습니다.

강사님 코드는 항상 `"볼륨 : 5"`를 출력합니다.

---

# 42. 내 Vol Up 음소거 해제 누락 가능성

음소거 상태이고 볼륨이 이미 최대 5일 때:

```js
lastVol++
```

후 최대값 분기가 먼저 실행됩니다.

`VOL_MUTE = false`가 실행되지 않습니다.

즉, 볼륨 up을 눌러도 음소거가 계속 true로 남을 수 있습니다.

요구사항인 “볼륨 조절 시 음소거 해제”와 어긋납니다.

---

# 43. 강사님 Volume Down

```js
function volumeDown() {
  if (power) {
    status_mute = false

    lastVol--

    if (lastVol < VOL_MIN) {
      lastVol = VOL_MIN
    }

    console.log(
      "볼륨 : " + lastVol
    )
  }
}
```

최소값에서 더 내려도 0을 유지하고 항상 출력합니다.

음소거도 항상 해제합니다.

---

# 44. 내 Vol Down

내 코드:

```js
lastVol--

if (lastVol < VOL_MIN) {
  lastVol = VOL_MIN
} else if (VOL_MUTE == true) {
  VOL_MUTE = false
} else {
  console.log(...)
}
```

Vol Up과 같은 구조적 문제가 있습니다.

- 최소값 고정 분기에서 출력 없음
- 음소거 상태에서 최소값 아래로 내려간 경우 음소거 해제 안 됨
- 음소거 해제 분기에서는 전용 메시지를 출력함

---

# 45. Clamp 확장

볼륨을 범위 안에 고정하는 표현:

```js
lastVol =
  Math.min(
    VOL_MAX,
    Math.max(
      VOL_MIN,
      lastVol + 1
    )
  )
```

내려가기:

```js
lastVol =
  Math.min(
    VOL_MAX,
    Math.max(
      VOL_MIN,
      lastVol - 1
    )
  )
```

원본은 if문 연습에 적합합니다.

---

# 46. 내 Mute On과 Mute Off

내 코드에만 있습니다.

```js
function muteOn() {
  if (power) {
    console.log(
      "[음소거 설정] 현재볼륨 : 0"
    )
  }
}
```

```js
function muteOff() {
  if (power) {
    console.log(
      "[음소거 해제] 현재볼륨 :",
      lastVol
    )
  }
}
```

중요:

두 함수 모두 `VOL_MUTE` 값을 변경하지 않습니다.

따라서 이름과 출력은 상태 변경 함수처럼 보이지만 실제 상태는 바뀌지 않습니다.

또한 테스트 코드에서 호출하지 않습니다.

---

# 47. 내 Mute One

```js
function muteOne() {
  if (power) {
    if (VOL_MUTE == false) {
      console.log(
        "[음소거 설정] 현재볼륨 : 0"
      )
      VOL_MUTE = true
    } else {
      console.log(
        "[음소거 해제] 현재볼륨 :",
        lastVol
      )
      VOL_MUTE = false
    }
  }
}
```

하나의 함수가 음소거 상태를 반전합니다.

실제 상태 변경은 이 함수에서 올바르게 수행됩니다.

---

# 48. 강사님 Mute

```js
function mute() {
  if (power) {
    if (status_mute) {
      status_mute = false
      console.log(
        "볼륨 : " + lastVol
      )
    } else {
      status_mute = true
      console.log("볼륨 : 0")
    }
  }
}
```

내 `muteOne()`과 같은 toggle 구조입니다.

차이는 변수 이름과 출력 문구입니다.

---

# 49. Boolean Toggle 단순화

양쪽 원본 주석에 다음 아이디어가 있습니다.

```js
status_mute =
  !status_mute
```

내 코드:

```text
VOL_MUTE = !VOL_MUTE도 가능
```

상태 반전 후 출력:

```js
isMuted = !isMuted

console.log(
  isMuted
    ? "볼륨 : 0"
    : `볼륨 : ${lastVol}`
)
```

---

# 50. 음소거와 LastVol

원본은 음소거 시 `lastVol` 값을 0으로 바꾸지 않습니다.

```text
lastVol
→ 실제 기억된 볼륨

음소거 출력
→ 0으로 보이게 함
```

음소거 해제 시 이전 볼륨을 복구할 수 있습니다.

이 설계는 요구사항과 잘 맞습니다.

---

# 51. 전원 Off 테스트

양쪽 원본은 먼저 전원이 꺼진 상태에서 기능을 호출합니다.

공통 흐름:

```js
powerOff()
channel(...)
channelUp()
channelDown()
volumeUp 또는 volUp
volumeDown 또는 volDown
mute 또는 muteOne
```

`powerOff()`는 `"TV 꺼짐"`을 출력합니다.

이후 각 기능은:

```text
전원 꺼져있음
```

을 출력하고 상태 변경을 차단합니다.

---

# 52. 내 전원 On 볼륨 테스트

내 코드:

```js
volUp()
volDown()
volDown()
volUp()
muteOne()
volUp()
muteOne()
volDown()
muteOne()
muteOne()
```

상태 개념:

```text
초기 볼륨 0, 음소거 false
up → 1
down → 0
down → 0, 출력 누락
up → 1
mute → true
up → 2, mute false
mute → true
down → 1, mute false
mute → true
mute → false
```

최종 볼륨은 1, 음소거는 false입니다.

---

# 53. 강사님 전원 On 볼륨 테스트

강사님은 최대·최소·음소거 해제까지 더 긴 테스트를 수행합니다.

```text
0 → 1 → 0 → 0
→ 1 → 2 → 3 → 4 → 5 → 5
→ mute on → off → on
→ volumeDown으로 mute 해제 및 4
→ mute on
→ volumeUp으로 mute 해제 및 5
→ mute on
```

최종 볼륨은 5, 음소거는 true입니다.

---

# 54. 함수명 차이

| 기능 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 볼륨 증가 | `volUp()` | `volumeUp()` |
| 볼륨 감소 | `volDown()` | `volumeDown()` |
| 음소거 toggle | `muteOne()` | `mute()` |
| 전원 toggle | `powerOne()` | 없음 |
| 음소거 켜기 | `muteOn()` | 없음 |
| 음소거 끄기 | `muteOff()` | 없음 |

`volumeUp`, `toggleMute`, `togglePower`처럼 의미가 직접 드러나는 이름이 읽기 쉽습니다.

---

# 55. 출력 띄어쓰기 차이

내 코드:

```text
5번으로 채널변경
```

강사님 코드:

```text
5번으로 채널 변경
```

강사님 문구가 띄어쓰기상 자연스럽습니다.

기능에는 영향이 없습니다.

---

# 56. 느슨한 Boolean 비교

내 코드:

```js
VOL_MUTE == true
VOL_MUTE == false
```

Boolean 변수는 직접 조건으로 사용할 수 있습니다.

```js
if (VOL_MUTE)
```

```js
if (!VOL_MUTE)
```

또는 엄격 비교:

```js
VOL_MUTE === true
```

가 가능하지만 직접 조건이 가장 간결합니다.

---

# 57. 전원 검사 중복

모든 기능에서 다음 구조가 반복됩니다.

```js
if (power) {
  // 기능
} else {
  console.log("전원 꺼져있음")
}
```

학습 단계에서는 명확하지만 중복이 많습니다.

early return 형태:

```js
if (!power) {
  console.log("전원 꺼져있음")
  return
}
```

이후 정상 로직을 작성하면 중첩을 줄일 수 있습니다.

---

# 58. 전원 검사 함수 확장

```js
function ensurePower() {
  if (!power) {
    console.log("전원 꺼져있음")
    return false
  }

  return true
}
```

사용:

```js
function channelUp() {
  if (!ensurePower()) {
    return
  }

  // 채널 변경
}
```

원본에는 없는 리팩터링 예제입니다.

---

# 59. 상태 객체 확장

여러 전역 변수를 하나의 객체로 묶을 수 있습니다.

```js
const tv = {
  power: false,
  channel: 0,
  volume: 0,
  muted: false
}
```

상태가 한 곳에 모여 의미가 명확해집니다.

이후 객체 단원과 연결할 수 있습니다.

---

# 60. 원본 통합 개선 예제

```js
const tv = {
  power: false,
  channel: 0,
  volume: 0,
  muted: false
}

const CHANNEL_MIN = 0
const CHANNEL_MAX = 10
const VOLUME_MIN = 0
const VOLUME_MAX = 5

function ensurePower() {
  if (!tv.power) {
    console.log("전원이 꺼져 있습니다.")
    return false
  }

  return true
}

function togglePower() {
  tv.power = !tv.power

  console.log(
    tv.power
      ? "TV 켜짐"
      : "TV 꺼짐"
  )
}

function setChannel(channel) {
  if (!ensurePower()) {
    return
  }

  if (
    !Number.isInteger(channel) ||
    channel < CHANNEL_MIN ||
    channel > CHANNEL_MAX
  ) {
    console.log("채널이 없습니다.")
    return
  }

  tv.channel = channel

  console.log(
    `${tv.channel}번으로 채널 변경`
  )
}

function channelUp() {
  if (!ensurePower()) {
    return
  }

  tv.channel++

  if (tv.channel > CHANNEL_MAX) {
    tv.channel = CHANNEL_MIN
  }

  console.log(
    `${tv.channel}번으로 채널 변경`
  )
}

function channelDown() {
  if (!ensurePower()) {
    return
  }

  tv.channel--

  if (tv.channel < CHANNEL_MIN) {
    tv.channel = CHANNEL_MAX
  }

  console.log(
    `${tv.channel}번으로 채널 변경`
  )
}

function changeVolume(amount) {
  if (!ensurePower()) {
    return
  }

  tv.muted = false

  tv.volume =
    Math.min(
      VOLUME_MAX,
      Math.max(
        VOLUME_MIN,
        tv.volume + amount
      )
    )

  console.log(
    `볼륨 : ${tv.volume}`
  )
}

const volumeUp =
  () => changeVolume(1)

const volumeDown =
  () => changeVolume(-1)

function toggleMute() {
  if (!ensurePower()) {
    return
  }

  tv.muted = !tv.muted

  console.log(
    tv.muted
      ? "볼륨 : 0"
      : `볼륨 : ${tv.volume}`
  )
}
```

---

# 61. My Code 분석

## 61.1 장점

- 화살표 함수 규칙을 강사님보다 상세히 설명했다.
- `fn2(1, 2)`를 실제로 호출해 화살표 함수 실행을 확인했다.
- 즉시 실행 함수의 뒤 괄호 의미를 설명했다.
- 매개변수 하나와 없음의 괄호 규칙을 상세히 기록했다.
- 중괄호를 생략하면 return도 생략해야 한다는 점을 설명했다.
- TV 요구사항을 기능 번호와 함께 명확히 정리했다.
- 범위 상수를 대문자로 사용하는 이유를 설명했다.
- `powerOne()`으로 전원 toggle 기능을 추가했다.
- 채널 입력 검증에 early return을 사용했다.
- 채널 up·down 순환 동작을 구현했다.
- 음소거 상태별 볼륨 메시지를 구분했다.
- `muteOn()`, `muteOff()`, `muteOne()`을 별도로 작성해 여러 설계를 실험했다.
- 전원 off와 on 상태 테스트를 구분했다.
- 잘못된 채널 50과 -50을 모두 테스트했다.

## 61.2 개선점

- `return a, b`가 두 값을 반환하는 것처럼 오해할 수 있다.
- `return은 1번만 써야 한다`는 설명은 부정확하다.
- `fn4()`는 선언되지 않은 `a`를 사용하므로 호출 시 오류가 발생한다.
- 화살표 함수와 일반 함수의 `this` 차이를 설명하지 않는다.
- `VOL_MUTE`는 변경되는 let 변수인데 상수처럼 대문자로 작성했다.
- `powerOne()`, `muteOn()`, `muteOff()`는 테스트에서 사용하지 않는다.
- `muteOn()`과 `muteOff()`는 실제 음소거 상태를 변경하지 않는다.
- 채널 입력에서 정수와 NaN 검증이 없다.
- 볼륨 최대·최소 고정 분기에서 현재 볼륨 메시지가 출력되지 않는다.
- 볼륨이 경계값이고 음소거 상태일 때 음소거가 해제되지 않을 수 있다.
- Boolean 비교에 `== true`, `== false`를 사용한다.
- 같은 전원 검사 로직이 모든 함수에 반복된다.
- 함수명이 `volUp`, `muteOne`, `powerOne`처럼 일관성이 부족하다.
- 많은 세미콜론과 생략된 세미콜론이 섞여 있다.

---

# 62. Teacher Code 분석

## 62.1 장점

- 일반 익명 함수와 화살표 함수를 같은 구조로 비교한다.
- IIFE 형태를 보여 준다.
- 매개변수 하나일 때 괄호 생략 규칙을 명확히 강조한다.
- 실행문이 return 하나일 때 축약하는 방법을 보여 준다.
- TV 상태 변수와 상수 범위값을 명확히 구분한다.
- 채널 직접 입력에서 early return을 사용한다.
- 채널 10→0, 0→10 순환을 테스트한다.
- 볼륨 조절 시 음소거를 항상 해제한다.
- 최대·최소 볼륨에서도 항상 현재값을 출력한다.
- 음소거 toggle을 하나의 함수로 구현한다.
- 최대 볼륨, 최소 볼륨, 음소거, 볼륨 조절 후 해제를 긴 테스트로 검증한다.

## 62.2 개선점

- `return a, b`의 쉼표 연산자 의미를 설명하지 않는다.
- `fn4()`는 선언되지 않은 `a`를 사용한다.
- `fn2`, `fn3`, `fn4`, `fn5`, `fn6`, `fn7`을 대부분 호출하지 않는다.
- TV 주석은 채널 0~100이라고 하지만 실제 상수는 최대 10이다.
- `channel(-50) // 0` 주석은 실제 동작과 다르다.
- 입력 채널의 정수·NaN 검증이 없다.
- 음소거 변수명 `status_mute`가 일반적인 camelCase 스타일과 다르다.
- 모든 기능에 전원 확인 코드가 반복된다.
- 전역 상태가 여러 함수에 분산되어 있다.
- 문서 언어와 제목이 콘텐츠에 맞지 않는다.

---

# 63. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| Arrow 파일 설명 | 더 상세 | 간결 |
| `fn2` 호출 | 있음 | 없음 |
| IIFE 설명 | 추가 | 코드만 |
| `return a, b` | 같은 코드, 추가 주석도 부정확 | 같은 코드 |
| `fn4` 미선언 a | 있음 | 있음 |
| TV 채널 주석 | 0~10 | 0~100이라고 잘못 표기 |
| 실제 CH_MAX | 10 | 10 |
| 음소거 변수 | `VOL_MUTE` | `status_mute` |
| 전원 toggle | `powerOne()` 있음 | 없음 |
| 음소거 개별 함수 | `muteOn`, `muteOff` 있음 | 없음 |
| 실제 음소거 toggle | `muteOne()` | `mute()` |
| 볼륨 함수명 | `volUp`, `volDown` | `volumeUp`, `volumeDown` |
| 볼륨 경계 출력 | 누락 가능 | 항상 출력 |
| 경계에서 mute 해제 | 실패 가능 | 항상 해제 |
| 채널 테스트 최종값 | 4 | 10 |
| 볼륨 테스트 최종값 | 1, mute false | 5, mute true |
| 잘못된 채널 주석 | 없음 | `channel(-50) // 0` |
| 테스트 범위 | 비교적 짧음 | 최대·최소까지 상세 |

---

# 64. 공통 핵심 코드

```js
const add =
  (a, b) => a + b

let power = false
let channelValue = 0
let volumeValue = 0
let muted = false

const CH_MIN = 0
const CH_MAX = 10

const VOL_MIN = 0
const VOL_MAX = 5

function powerOn() {
  power = true
}

function powerOff() {
  power = false
}

function channelUp() {
  if (!power) {
    return
  }

  channelValue++

  if (channelValue > CH_MAX) {
    channelValue = CH_MIN
  }
}

function channelDown() {
  if (!power) {
    return
  }

  channelValue--

  if (channelValue < CH_MIN) {
    channelValue = CH_MAX
  }
}

function toggleMute() {
  if (!power) {
    return
  }

  muted = !muted
}
```

---

# 65. 자주 하는 실수

## 65.1 Return A Comma B로 두 값 반환

실제로는 마지막 표현식 `b`만 반환됩니다.

## 65.2 화살표 함수 중괄호 안에서 Return 생략

중괄호가 있으면 명시적 return이 필요합니다.

## 65.3 매개변수 없는 함수에서 괄호 생략

`() => {}`처럼 빈 괄호가 필요합니다.

## 65.4 선언되지 않은 외부 변수 사용

`fn4()`처럼 `a`가 없으면 호출 시 ReferenceError가 발생합니다.

## 65.5 주석 범위와 실제 상수 불일치

강사님 주석은 0~100이지만 구현은 0~10입니다.

## 65.6 Boolean 상태를 대문자 상수처럼 명명

변경되는 상태는 `isMuted` 같은 이름이 명확합니다.

## 65.7 상태를 출력만 하고 실제 변수는 변경하지 않기

내 `muteOn()`과 `muteOff()`가 해당합니다.

## 65.8 경계값 분기에서 출력과 부가 상태 처리 누락

내 volUp·volDown은 최대·최소 분기에서 mute 해제가 누락될 수 있습니다.

## 65.9 문자열 숫자를 채널로 그대로 저장

정수 변환과 유효성 검증이 필요합니다.

## 65.10 전역 상태 변경 위치가 너무 많음

객체나 클래스로 상태와 기능을 묶는 방법을 검토할 수 있습니다.

---

# 66. 면접·복습 포인트

## Q1. 화살표 함수에서 매개변수 괄호는 언제 생략할 수 있나요?

매개변수가 정확히 하나이고 기본값·구조분해 같은 복잡한 문법이 없을 때 생략할 수 있습니다.

## Q2. 중괄호와 return은 언제 생략할 수 있나요?

본문이 하나의 표현식이고 그 결과를 바로 반환할 때 함께 생략할 수 있습니다.

## Q3. `return a, b`의 반환값은 무엇인가요?

쉼표 연산자 때문에 `b`의 값이 반환됩니다.

## Q4. 원본 `fn4()`를 호출하면 왜 문제가 되나요?

함수 안에서 선언되지 않은 `a`를 참조하기 때문입니다.

## Q5. 채널 up에서 10 다음 0으로 가는 동작을 무엇이라 하나요?

범위 끝에서 처음으로 돌아가는 순환 또는 wrap-around 동작입니다.

## Q6. 볼륨 최대값 고정을 어떻게 구현하나요?

증가 후 최대값을 초과하면 최대값으로 다시 설정하거나 `Math.min()`으로 제한할 수 있습니다.

## Q7. 음소거할 때 lastVol을 0으로 바꾸지 않는 이유는 무엇인가요?

해제 시 이전 볼륨을 복구하기 위해 기억된 볼륨을 유지하기 때문입니다.

## Q8. 내 volUp의 경계값 문제는 무엇인가요?

최대값 분기가 먼저 실행되면 현재 볼륨 출력과 음소거 해제가 실행되지 않을 수 있습니다.

## Q9. 강사님 주석과 구현의 채널 범위 차이는 무엇인가요?

주석은 0~100이라고 하지만 실제 `CH_MAX`는 10입니다.

## Q10. 상태 변수를 객체로 묶는 장점은 무엇인가요?

관련 상태를 한 구조에 모아 의미와 변경 위치를 추적하기 쉬워집니다.

---

# Problems

## 문제 1. 일반 함수 표현식

두 수를 더하는 익명 함수를 변수에 저장하고 호출하세요.

## 문제 2. 화살표 함수 변환

문제 1을 화살표 함수로 바꾸세요.

## 문제 3. 매개변수 하나

숫자 하나를 받아 100을 더해 반환하는 화살표 함수를 괄호 없이 작성하세요.

## 문제 4. 매개변수 없음

`"hello"`를 출력하는 매개변수 없는 화살표 함수를 작성하세요.

## 문제 5. Return 축약

두 수를 곱해 반환하는 함수를 한 줄 화살표 함수로 작성하세요.

## 문제 6. 쉼표 연산자

`return 10, 20`의 실제 반환값을 설명하세요.

## 문제 7. 두 값 반환

숫자 10과 20을 배열로 반환하는 함수를 작성하세요.

## 문제 8. IIFE

두 수를 전달받아 합계를 즉시 출력하는 즉시 실행 함수를 작성하세요.

## 문제 9. 전원 Toggle

Boolean 전원 상태를 하나의 함수로 반전하세요.

## 문제 10. 채널 직접 입력

0~10 정수만 허용하는 채널 변경 함수를 작성하세요.

## 문제 11. 채널 Up

현재 채널이 10이면 다음 up에서 0으로 돌아가게 하세요.

## 문제 12. 채널 Down

현재 채널이 0이면 다음 down에서 10으로 돌아가게 하세요.

## 문제 13. 볼륨 Up

볼륨을 1 증가시키되 최대 5를 넘지 않게 하세요.

## 문제 14. 볼륨 Down

볼륨을 1 감소시키되 최소 0보다 작아지지 않게 하세요.

## 문제 15. 음소거 Toggle

음소거 Boolean을 `!` 연산자로 반전하세요.

## 문제 16. 볼륨 조절과 음소거

볼륨을 조절하면 음소거 상태가 자동으로 false가 되게 하세요.

## 문제 17. Early Return

전원이 꺼져 있으면 채널 함수가 즉시 종료되게 하세요.

## 문제 18. 상태 객체

전원·채널·볼륨·음소거를 하나의 객체에 저장하세요.

## 문제 19. 원본 오류 찾기

내 `muteOn()`과 `muteOff()`의 상태 관리 문제를 설명하세요.

## 문제 20. 경계값 오류 찾기

내 `volUp()`에서 최대 볼륨 상태일 때 출력과 음소거 해제가 누락될 수 있는 이유를 설명하세요.

## 문제 21. 원본 비교

강사님 TV 주석의 채널 범위와 실제 상수값 차이를 설명하세요.

## 문제 22. 종합 리모컨

다음 요구사항을 만족하는 TV 리모컨 코드를 작성하세요.

- 상태 객체 사용
- 채널 0~10
- 볼륨 0~5
- 전원 toggle
- 직접 채널 입력 정수 검증
- 채널 순환
- 볼륨 범위 고정
- 볼륨 조절 시 음소거 해제
- 음소거 toggle
- 전원이 꺼졌으면 기능 차단
- 화살표 함수 최소 2개 사용

---

# Answers & Explanations

## 정답 1

```js
const add =
  function(a, b) {
    return a + b
  }

console.log(
  add(10, 20)
)
```

## 정답 2

```js
const add =
  (a, b) => {
    return a + b
  }
```

## 정답 3

```js
const addHundred =
  value => value + 100
```

## 정답 4

```js
const hello = () => {
  console.log("hello")
}
```

## 정답 5

```js
const multiply =
  (a, b) => a * b
```

## 정답 6

```js
function example() {
  return 10, 20
}

console.log(
  example()
)
```

결과는 20입니다.

## 정답 7

```js
const getValues =
  () => [10, 20]
```

## 정답 8

```js
(function(a, b) {
  console.log(a + b)
})(10, 20)
```

## 정답 9

```js
let power = false

function togglePower() {
  power = !power
}
```

## 정답 10

```js
let channel = 0

function setChannel(value) {
  if (
    !Number.isInteger(value) ||
    value < 0 ||
    value > 10
  ) {
    console.log("채널이 없습니다.")
    return
  }

  channel = value
}
```

## 정답 11

```js
let channel = 10

function channelUp() {
  channel++

  if (channel > 10) {
    channel = 0
  }
}
```

## 정답 12

```js
let channel = 0

function channelDown() {
  channel--

  if (channel < 0) {
    channel = 10
  }
}
```

## 정답 13

```js
let volume = 5

function volumeUp() {
  volume =
    Math.min(5, volume + 1)
}
```

## 정답 14

```js
let volume = 0

function volumeDown() {
  volume =
    Math.max(0, volume - 1)
}
```

## 정답 15

```js
let muted = false

function toggleMute() {
  muted = !muted
}
```

## 정답 16

```js
let volume = 2
let muted = true

function changeVolume(amount) {
  muted = false

  volume =
    Math.min(
      5,
      Math.max(
        0,
        volume + amount
      )
    )
}
```

## 정답 17

```js
let power = false

function channelUp() {
  if (!power) {
    console.log("전원 꺼져있음")
    return
  }

  console.log("채널 변경")
}
```

## 정답 18

```js
const tv = {
  power: false,
  channel: 0,
  volume: 0,
  muted: false
}
```

## 정답 19

두 함수는 음소거 설정·해제 메시지만 출력하고 `VOL_MUTE` 값을 true 또는 false로 변경하지 않습니다. 따라서 함수 이름과 실제 상태가 일치하지 않습니다.

## 정답 20

`lastVol > VOL_MAX` 분기가 실행되면 뒤의 `else if (VOL_MUTE == true)`와 `else`가 실행되지 않습니다. 따라서 최대값에서는 현재 볼륨 출력과 음소거 해제가 누락될 수 있습니다.

## 정답 21

강사님 주석에는 채널이 0~100이라고 적혀 있지만 실제 코드는 `CH_MAX = 10`, `CH_MIN = 0`이므로 구현 범위는 0~10입니다.

## 정답 22

```js
const tv = {
  power: false,
  channel: 0,
  volume: 0,
  muted: false
}

const CHANNEL_MIN = 0
const CHANNEL_MAX = 10

const VOLUME_MIN = 0
const VOLUME_MAX = 5

const ensurePower = () => {
  if (!tv.power) {
    console.log("전원이 꺼져 있습니다.")
    return false
  }

  return true
}

const togglePower = () => {
  tv.power = !tv.power

  console.log(
    tv.power
      ? "TV 켜짐"
      : "TV 꺼짐"
  )
}

function setChannel(value) {
  if (!ensurePower()) {
    return
  }

  if (
    !Number.isInteger(value) ||
    value < CHANNEL_MIN ||
    value > CHANNEL_MAX
  ) {
    console.log("채널이 없습니다.")
    return
  }

  tv.channel = value

  console.log(
    `${tv.channel}번으로 채널 변경`
  )
}

function channelUp() {
  if (!ensurePower()) {
    return
  }

  tv.channel++

  if (tv.channel > CHANNEL_MAX) {
    tv.channel = CHANNEL_MIN
  }

  console.log(
    `${tv.channel}번으로 채널 변경`
  )
}

function channelDown() {
  if (!ensurePower()) {
    return
  }

  tv.channel--

  if (tv.channel < CHANNEL_MIN) {
    tv.channel = CHANNEL_MAX
  }

  console.log(
    `${tv.channel}번으로 채널 변경`
  )
}

function changeVolume(amount) {
  if (!ensurePower()) {
    return
  }

  tv.muted = false

  tv.volume =
    Math.min(
      VOLUME_MAX,
      Math.max(
        VOLUME_MIN,
        tv.volume + amount
      )
    )

  console.log(
    `볼륨 : ${tv.volume}`
  )
}

const volumeUp =
  () => changeVolume(1)

const volumeDown =
  () => changeVolume(-1)

function toggleMute() {
  if (!ensurePower()) {
    return
  }

  tv.muted = !tv.muted

  console.log(
    tv.muted
      ? "볼륨 : 0"
      : `볼륨 : ${tv.volume}`
  )
}
```

---

# Final Checklist

## 화살표 함수

- [ ] 일반 함수 표현식과 화살표 함수를 비교했다.
- [ ] 함수 선언과 즉시 실행 함수를 구분했다.
- [ ] 매개변수가 하나일 때만 괄호를 생략했다.
- [ ] 매개변수가 없으면 빈 괄호를 작성했다.
- [ ] 중괄호를 생략할 때 return도 함께 생략했다.
- [ ] 중괄호가 있으면 명시적 return을 작성했다.
- [ ] `return a, b`가 b만 반환함을 이해했다.
- [ ] 여러 값은 배열 또는 객체로 반환했다.
- [ ] `fn4()`의 선언되지 않은 a 문제를 확인했다.
- [ ] 객체 메서드에서 화살표 함수의 this 차이를 검토했다.

## TV 상태

- [ ] 전원 상태를 Boolean으로 관리했다.
- [ ] 채널과 볼륨의 최소·최대 상수를 선언했다.
- [ ] 변경 가능한 음소거 상태를 상수처럼 명명하지 않았다.
- [ ] 전원이 꺼진 경우 기능을 차단했다.
- [ ] 직접 채널 입력을 정수로 검증했다.
- [ ] 채널 10 다음 0으로 순환시켰다.
- [ ] 채널 0 이전 10으로 순환시켰다.
- [ ] 볼륨을 0~5 안에 고정했다.
- [ ] 볼륨 조절 시 음소거를 해제했다.
- [ ] 음소거 중에도 기억된 볼륨값을 유지했다.
- [ ] toggle 함수가 실제 상태를 변경하는지 확인했다.

## 코드 구조

- [ ] 반복되는 전원 확인을 early return으로 정리했다.
- [ ] 상태를 하나의 객체로 묶는 방법을 이해했다.
- [ ] 함수 이름을 일관되게 작성했다.
- [ ] 출력 문구와 실제 상태가 일치하는지 확인했다.
- [ ] 테스트 후 최종 채널·볼륨·음소거 상태를 추적했다.

## 원본 코드 검수

- [ ] 두 화살표 함수 원본과 두 TV 원본을 함께 분석했다.
- [ ] 강사님 TV 주석의 0~100과 실제 CH_MAX 10 차이를 기록했다.
- [ ] 강사님 `channel(-50) // 0` 주석 오류를 기록했다.
- [ ] 내 fn2만 추가 호출된 차이를 기록했다.
- [ ] 양쪽 `return a, b` 문제를 기록했다.
- [ ] 양쪽 fn4의 미선언 a 문제를 기록했다.
- [ ] 내 powerOne이 미사용임을 기록했다.
- [ ] 내 muteOn·muteOff가 상태를 변경하지 않음을 기록했다.
- [ ] 내 volUp·volDown의 경계 출력 누락을 기록했다.
- [ ] 내 경계값에서 음소거 해제 누락 가능성을 기록했다.
- [ ] 강사님 볼륨 함수는 항상 음소거를 해제함을 기록했다.
- [ ] 테스트 결과의 최종 상태 차이를 기록했다.

---

# Key Summary

- JavaScript 09번은 `09_arrow.html`과 `09_1_tv.html` 두 파일로 구성된다.
- 일반 익명 함수는 `const fn = function() {}` 형태로 변수에 저장할 수 있다.
- 화살표 함수는 `const fn = () => {}` 형태로 작성한다.
- 매개변수가 정확히 하나일 때 괄호를 생략할 수 있다.
- 매개변수가 없거나 두 개 이상이면 괄호가 필요하다.
- 본문이 하나의 반환 표현식이면 중괄호와 return을 함께 생략할 수 있다.
- `return a, b`는 두 값을 반환하지 않고 쉼표 연산자 결과인 b를 반환한다.
- 여러 값을 반환하려면 배열이나 객체를 사용한다.
- 내 `return은 1번만 써야 한다`는 주석은 함수에 return 문을 하나만 작성해야 한다는 뜻으로는 부정확하다.
- 양쪽 원본의 `fn4()`는 선언되지 않은 `a`를 참조하므로 호출 시 오류가 발생할 수 있다.
- 내 코드는 `fn2(1, 2)`를 호출하지만 강사님 코드는 fn2를 선언만 한다.
- 화살표 함수는 일반 함수와 `this` 동작이 다를 수 있다.
- TV 구현은 여러 함수가 `power`, `lastCh`, `lastVol`, mute 상태를 공유한다.
- 상수 `CH_MIN`, `CH_MAX`, `VOL_MIN`, `VOL_MAX`는 범위 제한에 사용된다.
- 강사님 주석은 채널 0~100이라고 하지만 실제 구현은 0~10이다.
- 강사님 `channel(-50) // 0` 주석은 실제 코드와 다르며 해당 입력은 거부된다.
- 채널 up은 10 다음 0, down은 0 이전 10으로 순환한다.
- 직접 채널 입력은 정수·NaN까지 검증하는 것이 안전하다.
- 내 `powerOne()`은 전원 toggle을 구현하지만 테스트에서 호출하지 않는다.
- 내 `muteOn()`과 `muteOff()`는 메시지만 출력하고 실제 mute 상태를 변경하지 않는다.
- 실제 음소거 toggle은 내 `muteOne()`과 강사님 `mute()`에서 수행된다.
- 음소거 시 기억된 `lastVol`을 0으로 바꾸지 않아 해제 시 이전 볼륨을 복구한다.
- 강사님 볼륨 함수는 조절 시작 시 음소거를 항상 false로 바꾼다.
- 내 volUp·volDown은 최대·최소 분기가 먼저 실행되면 출력과 음소거 해제가 누락될 수 있다.
- 내 채널 테스트의 최종 채널은 4이고 강사님 테스트의 최종 채널은 10이다.
- 내 볼륨 테스트의 최종 상태는 볼륨 1·음소거 false이며 강사님은 볼륨 5·음소거 true다.
- 관련 상태를 객체로 묶고 공통 전원 검사를 함수로 분리하면 구조가 명확해진다.
