---
title: JavaScript 화살표 함수와 TV 상태 관리
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript 화살표 함수와 TV 상태 관리

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `09_JavaScript_화살표함수와_TV상태관리.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/09_arrow.html`, `09_1_tv.html`, 강사님 동일 파일 |
| 핵심 범위 | 함수 표현식, 즉시 실행 함수, 화살표 함수, 반환 축약, 쉼표 연산자, `this`, 상태 변수, 범위 제한, 순환, 토글 |
| 실습 범위 | TV 전원, 채널 직접 변경·증감, 볼륨 조절, 음소거, 상태 검증과 리팩토링 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 09번은 `09_arrow.html`과 `09_1_tv.html` 두 파일을 하나로 통합한다.  
> 첫 파일은 화살표 함수 문법을, 두 번째 파일은 여러 함수가 하나의 TV 상태를 공유하고 변경하는 구조를 다룬다.

---

# 개요

화살표 함수는 함수를 더 짧게 작성할 수 있는 문법이다.

```javascript
const add = (
    a,
    b,
) => {
    return a + b
}
```

본문이 하나의 반환 표현식이라면 더 줄일 수 있다.

```javascript
const add = (
    a,
    b,
) => a + b
```

TV 실습에서는 여러 함수가 다음 상태를 함께 사용한다.

```text
전원
채널
볼륨
음소거
```

```javascript
const tv = {
    power: false,
    channel: 0,
    volume: 0,
    muted: false,
}
```

> [!IMPORTANT]
> 화살표 함수는 일반 함수를 무조건 대체하는 문법이 아니다.
>
> 특히 `this`, `arguments`, 생성자 사용 여부가 중요할 때는 일반 함수와 차이를 확인해야 한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 함수 표현식 | 함수를 값으로 변수에 저장 |
| 즉시 실행 함수 | 정의와 동시에 한 번 실행 |
| 화살표 함수 | 짧은 함수 표현식 문법 |
| 암시적 반환 | 표현식 결과를 자동 반환 |
| 쉼표 연산자 | 여러 표현식을 평가하고 마지막 값 반환 |
| Lexical `this` | 바깥 스코프의 `this`를 사용 |
| 상태 변수 | 프로그램의 현재 상태 저장 |
| 상수 범위값 | 허용되는 최소·최대값 관리 |
| Toggle | Boolean 상태 반전 |
| Clamp | 값을 최소·최대 범위 안에 고정 |
| Wrap-around | 범위를 넘으면 반대쪽 끝으로 이동 |
| Early Return | 잘못된 상태를 먼저 종료 |

---

# 학습 목표

- 일반 함수 표현식과 화살표 함수를 비교할 수 있다.
- 즉시 실행 함수의 구조를 이해한다.
- 매개변수 개수에 따른 괄호 생략 규칙을 설명할 수 있다.
- 중괄호와 `return` 생략 규칙을 설명할 수 있다.
- `return a, b`가 두 값을 반환하지 않는 이유를 이해한다.
- 배열·객체를 이용해 여러 값을 반환할 수 있다.
- 화살표 함수와 일반 함수의 `this` 차이를 설명할 수 있다.
- 여러 함수가 하나의 상태를 공유하는 구조를 이해한다.
- 전원이 꺼졌을 때 기능 실행을 차단할 수 있다.
- 채널 입력을 정수·범위로 검증할 수 있다.
- 채널을 최소·최대 범위에서 순환시킬 수 있다.
- 볼륨을 허용 범위 안에 고정할 수 있다.
- 음소거를 Boolean으로 토글할 수 있다.
- 볼륨 조절 시 음소거를 해제할 수 있다.
- 상태와 동작을 객체로 묶어 관리할 수 있다.

---

# 1. 09번 파일 구성

```text
09_arrow.html
→ 화살표 함수 문법

09_1_tv.html
→ 함수와 상태 변수를 이용한 TV 기능
```

두 파일은 함수 단원이지만 목적이 다르다.

---

# 2. 일반 함수 표현식

## 2-1. 원본 코드

```javascript
const fn1 = function (
    a,
    b,
) {
    console.log(a, b)

    return a, b
}
```

`function` 뒤에 이름이 없으므로 익명 함수 표현식이다.

변수 `fn1`이 함수 객체를 참조한다.

---

# 3. 함수 표현식 호출

```javascript
const result = fn1(
    1,
    2,
)

console.log(result)
```

출력:

```text
1 2
2
```

왜 반환값이 2인지 다음 절에서 확인한다.

---

# 4. 쉼표 연산자

```javascript
return a, b
```

두 값을 반환하는 문법이 아니다.

실행 순서:

```text
a 평가
→ b 평가
→ 마지막 값 b 반환
```

---

# 5. 여러 값 반환

배열:

```javascript
function getValues(
    a,
    b,
) {
    return [
        a,
        b,
    ]
}
```

객체:

```javascript
function getValues(
    a,
    b,
) {
    return {
        a,
        b,
    }
}
```

---

# 6. 구조 분해 할당

```javascript
const [
    first,
    second,
] = getValues(
    1,
    2,
)

console.log(
    first,
    second,
)
```

출력:

```text
1 2
```

---

# 7. 함수 안의 여러 `return`

내 코드의 “`return`은 한 번만 써야 한다”는 설명은 정확히 구분해야 한다.

함수 안에 여러 `return` 문을 작성할 수 있다.

```javascript
function checkNumber(
    value,
) {
    if (value > 0) {
        return "양수"
    }

    if (value < 0) {
        return "음수"
    }

    return "0"
}
```

하나의 실행 경로에서는 첫 번째로 만난 `return`에서 함수가 종료된다.

---

# 8. 즉시 실행 함수

```javascript
(
    function () {
        console.log(
            "즉시 실행",
        )
    }
)()
```

함수를 선언한 뒤 마지막 괄호로 즉시 호출한다.

이를 IIFE라고 부른다.

---

# 9. IIFE의 역할

과거에는 전역 변수 오염을 줄이기 위한 스코프 생성에 자주 사용했다.

```javascript
(
    function () {
        const message = "내부 변수"

        console.log(message)
    }
)()
```

현재는 ES module과 블록 스코프를 더 자주 사용한다.

---

# 10. 기본 화살표 함수

```javascript
const fn2 = (
    a,
    b,
) => {
    console.log(a, b)

    return b
}
```

일반 함수 표현식에서 `function` 키워드를 제거하고 `=>`를 사용한다.

---

# 11. 매개변수가 없는 경우

```javascript
const hello = () => {
    console.log("hello")
}
```

매개변수가 없어도 빈 괄호 `()`가 필요하다.

---

# 12. 매개변수가 하나인 경우

```javascript
const double = value => {
    return value * 2
}
```

매개변수가 정확히 하나일 때만 괄호를 생략할 수 있다.

괄호를 작성해도 정상이다.

```javascript
const double = (
    value,
) => {
    return value * 2
}
```

---

# 13. 매개변수가 두 개 이상인 경우

```javascript
const add = (
    a,
    b,
) => {
    return a + b
}
```

괄호를 생략할 수 없다.

---

# 14. 암시적 반환

```javascript
const add = (
    a,
    b,
) => a + b
```

본문이 하나의 표현식이면 중괄호와 `return`을 함께 생략할 수 있다.

---

# 15. 중괄호와 `return`

다음 함수는 값을 반환하지 않는다.

```javascript
const add = (
    a,
    b,
) => {
    a + b
}
```

중괄호를 사용했다면 `return`을 직접 작성해야 한다.

---

# 16. 객체 암시적 반환

잘못 이해하기 쉬운 코드:

```text
const createUser = (
    name,
) => {
    name,
}
```

중괄호가 함수 블록으로 해석된다.

객체를 바로 반환하려면 괄호로 감싼다.

```javascript
const createUser = (
    name,
) => ({
    name,
})
```

---

# 17. 원본의 미선언 변수 문제

원본의 일부 화살표 함수는 선언되지 않은 `a`를 사용한다.

```text
const fn4 = () => a
```

`a`가 현재 스코프에 없다면 호출 시 다음 오류가 발생한다.

```text
ReferenceError: a is not defined
```

개선:

```javascript
const fn4 = (
    a,
) => a
```

---

# 18. 화살표 함수와 `this`

화살표 함수는 자신만의 `this`를 만들지 않는다.

```javascript
const user = {
    name: "Kim",

    regularMethod() {
        console.log(this.name)
    },

    arrowMethod: () => {
        console.log(this.name)
    },
}
```

`regularMethod()`의 `this`는 호출한 객체가 될 수 있다.

`arrowMethod`의 `this`는 바깥 스코프의 `this`를 사용한다.

> [!WARNING]
> 객체 메서드에서 객체 자신을 `this`로 사용하려면 화살표 함수가 적합하지 않을 수 있다.

---

# 19. 화살표 함수와 `arguments`

화살표 함수에는 자체 `arguments` 객체가 없다.

여러 인수를 받으려면 rest parameter를 사용한다.

```javascript
const sum = (
    ...numbers
) => {
    return numbers.reduce(
        (
            total,
            number,
        ) => total + number,
        0,
    )
}
```

---

# 20. 생성자로 사용할 수 없음

```text
const User = name => {
    this.name = name
}

new User("Kim")
```

화살표 함수는 생성자로 사용할 수 없으며 `TypeError`가 발생한다.

생성자나 클래스는 일반 함수 또는 `class`를 사용한다.

---

# 21. 일반 함수와 화살표 함수 선택

| 상황 | 권장 |
| --- | --- |
| 짧은 배열 콜백 | 화살표 함수 |
| 바깥 `this` 유지 | 화살표 함수 |
| 객체 메서드의 동적 `this` | 일반 메서드 |
| 생성자 | 일반 함수·클래스 |
| `arguments` 필요 | 일반 함수 또는 rest parameter |
| 간단한 계산 함수 | 둘 다 가능 |

---

# 22. TV 상태 변수

원본 TV 예제는 여러 전역 변수를 사용한다.

```javascript
let power = false
let lastChannel = 0
let lastVolume = 0
let muted = false
```

여러 함수가 같은 상태를 읽고 변경한다.

---

# 23. 범위 상수

```javascript
const CHANNEL_MIN = 0
const CHANNEL_MAX = 10

const VOLUME_MIN = 0
const VOLUME_MAX = 5
```

상수로 분리하면 숫자의 의미와 변경 위치가 명확하다.

> [!NOTE]
> 강사님 주석에는 채널이 0~100이라고 적혀 있지만 실제 코드는 최대 10을 사용한다.

---

# 24. 전원 켜기

```javascript
function powerOn() {
    if (power) {
        console.log(
            "이미 전원이 켜져 있습니다.",
        )

        return
    }

    power = true

    console.log("TV 켜짐")
}
```

---

# 25. 전원 끄기

```javascript
function powerOff() {
    if (!power) {
        console.log(
            "이미 전원이 꺼져 있습니다.",
        )

        return
    }

    power = false

    console.log("TV 꺼짐")
}
```

---

# 26. 전원 토글

```javascript
function togglePower() {
    power = !power

    console.log(
        power
            ? "TV 켜짐"
            : "TV 꺼짐",
    )
}
```

Boolean 값을 반전해 하나의 함수로 켜기·끄기를 처리한다.

---

# 27. 내 코드의 `powerOne()`

내 코드에는 전원 토글 함수가 있지만 테스트에서 실제로 호출하지 않는다.

함수는 정의만 하면 실행되지 않으므로 테스트 코드에서 호출해야 동작을 확인할 수 있다.

---

# 28. 공통 전원 검사

각 기능마다 다음 조건이 반복된다.

```javascript
if (!power) {
    console.log(
        "전원이 꺼져 있습니다.",
    )

    return
}
```

함수로 분리:

```javascript
function ensurePower() {
    if (!power) {
        console.log(
            "전원이 꺼져 있습니다.",
        )

        return false
    }

    return true
}
```

---

# 29. Early Return

```javascript
function channelUp() {
    if (!ensurePower()) {
        return
    }

    // 채널 변경
}
```

잘못된 상태를 먼저 종료하면 중첩 조건을 줄일 수 있다.

---

# 30. 직접 채널 변경

```javascript
function setChannel(
    channel,
) {
    if (!ensurePower()) {
        return
    }

    if (
        !Number.isInteger(channel)
        || channel < CHANNEL_MIN
        || channel > CHANNEL_MAX
    ) {
        console.log(
            "채널이 없습니다.",
        )

        return
    }

    lastChannel = channel

    console.log(
        `${lastChannel}번으로 채널 변경`,
    )
}
```

---

# 31. 원본 채널 주석 불일치

강사님 테스트 주석에는 다음 형태가 있다.

```text
channel(-50) // 0
```

하지만 실제 범위 검증에서는 `-50`이 허용되지 않아 채널이 변경되지 않는다.

주석과 코드의 실제 동작을 구분해야 한다.

---

# 32. 채널 증가

```javascript
function channelUp() {
    if (!ensurePower()) {
        return
    }

    lastChannel += 1

    if (
        lastChannel
        > CHANNEL_MAX
    ) {
        lastChannel = CHANNEL_MIN
    }

    console.log(
        `${lastChannel}번으로 채널 변경`,
    )
}
```

---

# 33. 채널 감소

```javascript
function channelDown() {
    if (!ensurePower()) {
        return
    }

    lastChannel -= 1

    if (
        lastChannel
        < CHANNEL_MIN
    ) {
        lastChannel = CHANNEL_MAX
    }

    console.log(
        `${lastChannel}번으로 채널 변경`,
    )
}
```

---

# 34. 채널 순환

```text
채널 10에서 UP
→ 0

채널 0에서 DOWN
→ 10
```

이를 wrap-around라고 볼 수 있다.

---

# 35. 나머지 연산을 이용한 채널 순환

0부터 10까지 총 11개 채널이다.

```javascript
function channelUp() {
    lastChannel = (
        lastChannel + 1
    ) % (
        CHANNEL_MAX + 1
    )
}
```

최소값이 0이 아닌 일반적인 범위에서는 별도 공식을 사용하거나 조건문이 더 읽기 쉬울 수 있다.

---

# 36. 볼륨 증가

강사님 구조:

```javascript
function volumeUp() {
    if (!ensurePower()) {
        return
    }

    muted = false
    lastVolume += 1

    if (
        lastVolume
        > VOLUME_MAX
    ) {
        lastVolume = VOLUME_MAX
    }

    console.log(
        `볼륨: ${lastVolume}`,
    )
}
```

볼륨을 조절하면 음소거를 먼저 해제한다.

---

# 37. 볼륨 감소

```javascript
function volumeDown() {
    if (!ensurePower()) {
        return
    }

    muted = false
    lastVolume -= 1

    if (
        lastVolume
        < VOLUME_MIN
    ) {
        lastVolume = VOLUME_MIN
    }

    console.log(
        `볼륨: ${lastVolume}`,
    )
}
```

---

# 38. 내 코드의 볼륨 경계 문제

내 코드에서는 볼륨이 최대·최소 범위를 넘는 분기가 먼저 실행될 때 다음 작업이 누락될 수 있다.

- 현재 볼륨 출력
- 음소거 해제

예:

```text
음소거 true
볼륨 5
volUp()
→ 6으로 증가
→ 최대값 5로 복구
→ 뒤 음소거 해제 분기 실행 안 됨
```

---

# 39. Clamp

값을 범위 안에 고정하는 방식:

```javascript
function clamp(
    value,
    min,
    max,
) {
    return Math.min(
        max,
        Math.max(
            min,
            value,
        ),
    )
}
```

---

# 40. 공통 볼륨 변경 함수

```javascript
function changeVolume(
    amount,
) {
    if (!ensurePower()) {
        return
    }

    muted = false

    lastVolume = clamp(
        lastVolume + amount,
        VOLUME_MIN,
        VOLUME_MAX,
    )

    console.log(
        `볼륨: ${lastVolume}`,
    )
}
```

---

# 41. 화살표 함수로 기능 연결

```javascript
const volumeUp = (
    () => changeVolume(1)
)

const volumeDown = (
    () => changeVolume(-1)
)
```

짧은 위임 함수에는 화살표 함수가 잘 어울린다.

---

# 42. 음소거 켜기

```javascript
function muteOn() {
    if (!ensurePower()) {
        return
    }

    muted = true

    console.log("음소거")
}
```

---

# 43. 음소거 끄기

```javascript
function muteOff() {
    if (!ensurePower()) {
        return
    }

    muted = false

    console.log(
        `볼륨: ${lastVolume}`,
    )
}
```

---

# 44. 원본의 `muteOn()`·`muteOff()`

내 코드 원본의 일부 함수는 메시지만 출력하고 실제 음소거 Boolean 상태를 변경하지 않는다.

```text
메시지 출력
≠ 상태 변경
```

기능 함수는 반드시 상태값도 실제로 변경해야 한다.

---

# 45. 음소거 토글

```javascript
function toggleMute() {
    if (!ensurePower()) {
        return
    }

    muted = !muted

    console.log(
        muted
            ? "볼륨: 0"
            : `볼륨: ${lastVolume}`,
    )
}
```

하나의 함수로 음소거 켜기·끄기를 처리한다.

---

# 46. 음소거와 실제 볼륨

음소거할 때 `lastVolume`을 0으로 바꾸지 않는다.

```text
음소거 전 볼륨
→ 4

음소거
→ 출력 볼륨 0
→ lastVolume은 4 유지

음소거 해제
→ 볼륨 4 복구
```

기억된 볼륨과 실제 출력 상태를 구분한다.

---

# 47. TV 상태를 객체로 묶기

전역 변수가 흩어진 구조:

```javascript
let power = false
let lastChannel = 0
let lastVolume = 0
let muted = false
```

개선:

```javascript
const tv = {
    power: false,
    channel: 0,
    volume: 0,
    muted: false,
}
```

관련 상태가 한곳에 모인다.

---

# 48. 객체 기반 전원 검사

```javascript
function ensurePower() {
    if (!tv.power) {
        console.log(
            "전원이 꺼져 있습니다.",
        )

        return false
    }

    return true
}
```

---

# 49. 객체 기반 전원 토글

```javascript
const togglePower = () => {
    tv.power = !tv.power

    console.log(
        tv.power
            ? "TV 켜짐"
            : "TV 꺼짐",
    )
}
```

---

# 50. 객체 기반 채널 변경

```javascript
function setChannel(
    channel,
) {
    if (!ensurePower()) {
        return
    }

    if (
        !Number.isInteger(channel)
        || channel < CHANNEL_MIN
        || channel > CHANNEL_MAX
    ) {
        console.log(
            "채널이 없습니다.",
        )

        return
    }

    tv.channel = channel

    console.log(
        `${tv.channel}번으로 채널 변경`,
    )
}
```

---

# 51. 객체 기반 볼륨 변경

```javascript
function changeVolume(
    amount,
) {
    if (!ensurePower()) {
        return
    }

    tv.muted = false

    tv.volume = clamp(
        tv.volume + amount,
        VOLUME_MIN,
        VOLUME_MAX,
    )

    console.log(
        `볼륨: ${tv.volume}`,
    )
}
```

---

# 52. 객체 기반 음소거

```javascript
function toggleMute() {
    if (!ensurePower()) {
        return
    }

    tv.muted = !tv.muted

    console.log(
        tv.muted
            ? "볼륨: 0"
            : `볼륨: ${tv.volume}`,
    )
}
```

---

# 53. 상태 출력 함수

```javascript
function printStatus() {
    console.log({
        power: tv.power,
        channel: tv.channel,
        volume: (
            tv.muted
                ? 0
                : tv.volume
        ),
        muted: tv.muted,
    })
}
```

각 기능 호출 후 현재 상태를 확인할 수 있다.

---

# 54. 테스트 시나리오

```javascript
togglePower()
setChannel(10)
channelUp()
channelDown()

changeVolume(3)
toggleMute()
changeVolume(1)

printStatus()
```

예상 최종 상태:

```text
power: true
channel: 10
volume: 4
muted: false
```

---

# 55. 내 코드와 강사님 코드의 테스트 차이

두 원본은 호출 순서가 다르므로 최종 상태도 다르다.

- 내 채널 테스트 최종값: 4
- 강사님 채널 테스트 최종값: 10
- 내 볼륨 테스트 최종값: 볼륨 1, 음소거 false
- 강사님 볼륨 테스트 최종값: 볼륨 5, 음소거 true

코드 비교에서는 함수 정의뿐 아니라 실제 호출 순서도 함께 확인해야 한다.

---

# 56. 상태 관리 함수의 공통 원칙

| 원칙 | 설명 |
| --- | --- |
| 상태 한곳에 모으기 | 관련 값을 객체로 관리 |
| 입력 검증 | 타입·정수·범위 확인 |
| Early Return | 잘못된 상태 먼저 종료 |
| 중복 제거 | 전원 검사·범위 처리 함수화 |
| 상태와 출력 일치 | 메시지만 출력하지 말고 실제 상태 변경 |
| 경계 테스트 | 최소·최대·순환 지점 확인 |
| 토글 | Boolean 반전으로 구현 |

---

# 57. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 화살표 함수 | 설명과 일부 추가 호출 | 기본 선언 중심 |
| `return a, b` | 주석은 있으나 의미 불명확 | 같은 코드 사용 |
| 미선언 `a` | 동일 문제 | 동일 문제 |
| 전원 기능 | 별도 On·Off·Toggle | On·Off 중심 |
| 채널 범위 | 직접 입력·증감 구현 | 동일 |
| 음소거 | On·Off와 Toggle 혼합 | Toggle 중심 |
| 볼륨 경계 | 일부 출력·해제 누락 | 항상 상태 출력 |
| 상태 변수 | 전역에 분산 | 전역에 분산 |
| 테스트 | 짧은 시나리오 | 경계값까지 긴 시나리오 |

## 57-1. 내 코드의 장점

- 화살표 함수 문법을 주석으로 상세히 정리했다.
- 전원 토글 함수를 추가했다.
- 음소거 On·Off·Toggle을 다양한 형태로 시도했다.
- TV 상태 변화 과정을 직접 테스트했다.

## 57-2. 내 코드의 개선점

- `return a, b`가 두 값을 반환한다고 오해할 수 있다.
- 선언되지 않은 `a`를 사용하는 함수가 있다.
- `powerOne()`이 실제 테스트에서 호출되지 않는다.
- `muteOn()`·`muteOff()`가 실제 상태를 변경하지 않는 경우가 있다.
- 볼륨 경계 분기에서 출력과 음소거 해제가 누락될 수 있다.
- `==`보다 `===`를 사용해야 한다.

## 57-3. 강사님 코드의 장점

- 일반 함수 표현식과 화살표 함수를 직접 비교한다.
- 매개변수와 반환 축약 규칙을 단계적으로 보여 준다.
- TV 채널 순환과 볼륨 경계를 충분히 테스트한다.
- 볼륨 조절 시 음소거를 항상 해제한다.
- Early Return을 사용해 채널 오류를 처리한다.

## 57-4. 강사님 코드의 보충점

- 채널 0~100 주석과 실제 최대 10의 불일치를 수정해야 한다.
- `channel(-50) // 0` 주석이 실제 동작과 다르다.
- 입력값의 정수·NaN 검사가 필요하다.
- 전원 검사 코드가 반복된다.
- 상태가 여러 전역 변수에 분산되어 있다.
- `return a, b`와 화살표 함수 `this` 차이를 설명할 필요가 있다.

---

# 58. 기존 코드에서 개선 코드로 바꾼 이유

## 58-1. 두 값 반환

기존:

```javascript
return a, b
```

개선:

```javascript
return {
    a,
    b,
}
```

## 58-2. 공통 전원 검사

기존:

```javascript
if (power) {
    // 기능
}
```

개선:

```javascript
if (!ensurePower()) {
    return
}
```

## 58-3. 볼륨 범위 처리

기존:

```javascript
lastVolume += 1

if (
    lastVolume
    > VOLUME_MAX
) {
    lastVolume = VOLUME_MAX
}
```

개선:

```javascript
lastVolume = clamp(
    lastVolume + 1,
    VOLUME_MIN,
    VOLUME_MAX,
)
```

## 58-4. 전역 상태 통합

기존:

```javascript
let power
let lastChannel
let lastVolume
let muted
```

개선:

```javascript
const tv = {
    power: false,
    channel: 0,
    volume: 0,
    muted: false,
}
```

---

# 59. 실무형 예제: TV 컨트롤러 객체

```javascript
function createTvController() {
    const state = {
        power: false,
        channel: 0,
        volume: 0,
        muted: false,
    }

    const CHANNEL_MIN = 0
    const CHANNEL_MAX = 10
    const VOLUME_MIN = 0
    const VOLUME_MAX = 5

    const ensurePower = () => {
        if (!state.power) {
            console.log(
                "전원이 꺼져 있습니다.",
            )

            return false
        }

        return true
    }

    const clamp = (
        value,
        min,
        max,
    ) => (
        Math.min(
            max,
            Math.max(
                min,
                value,
            ),
        )
    )

    return {
        togglePower() {
            state.power = !state.power

            return state.power
        },

        setChannel(
            channel,
        ) {
            if (!ensurePower()) {
                return false
            }

            if (
                !Number.isInteger(channel)
                || channel < CHANNEL_MIN
                || channel > CHANNEL_MAX
            ) {
                return false
            }

            state.channel = channel

            return true
        },

        changeVolume(
            amount,
        ) {
            if (!ensurePower()) {
                return false
            }

            state.muted = false

            state.volume = clamp(
                state.volume + amount,
                VOLUME_MIN,
                VOLUME_MAX,
            )

            return true
        },

        toggleMute() {
            if (!ensurePower()) {
                return false
            }

            state.muted = !state.muted

            return true
        },

        getState() {
            return {
                ...state,
                outputVolume: (
                    state.muted
                        ? 0
                        : state.volume
                ),
            }
        },
    }
}
```

## 59-1. 실행

```javascript
const controller = (
    createTvController()
)

controller.togglePower()
controller.setChannel(7)
controller.changeVolume(3)
controller.toggleMute()

console.log(
    controller.getState(),
)
```

## 59-2. 출력 결과

```text
{
    power: true,
    channel: 7,
    volume: 3,
    muted: true,
    outputVolume: 0
}
```

## 59-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| 클로저 | 내부 상태를 외부에서 직접 변경하지 못하게 보호 |
| 화살표 함수 | 짧은 내부 보조 함수 작성 |
| 객체 메서드 | TV 기능을 하나의 API로 제공 |
| 복사 객체 | 내부 상태 원본 노출 방지 |
| Clamp | 볼륨 범위 제한 |
| Boolean Toggle | 전원·음소거 전환 |
| 반환값 | 기능 성공 여부와 상태 재사용 |

---

# 60. 대표 오류로 이해하기

## 60-1. 객체 반환 괄호 누락

```javascript
const create = () => {
    name: "Kim"
}
```

객체를 반환하지 않는다.

## 60-2. 미선언 변수 반환

```text
const fn = () => a
```

`a`가 없으면 `ReferenceError`다.

## 60-3. 화살표 함수를 생성자로 사용

`TypeError`가 발생한다.

## 60-4. 화살표 메서드의 `this`

객체 자신을 가리키지 않을 수 있다.

## 60-5. 메시지만 출력하고 상태 미변경

사용자에게 보이는 결과와 내부 상태가 달라진다.

## 60-6. 경계값에서 음소거 해제 누락

분기 순서 때문에 일부 코드가 실행되지 않을 수 있다.

---

# 61. 자주 하는 실수

## 61-1. 매개변수가 없는데 괄호 생략

빈 괄호가 필요하다.

## 61-2. 두 개 이상의 매개변수 괄호 생략

문법 오류가 발생한다.

## 61-3. 중괄호를 사용하고 `return` 생략

`undefined`를 반환한다.

## 61-4. `return a, b`를 다중 반환으로 이해

마지막 값 `b`만 반환한다.

## 61-5. 객체를 암시적으로 반환하면서 괄호 생략

함수 블록으로 해석된다.

## 61-6. 모든 함수를 화살표 함수로 변경

`this`, 생성자, `arguments` 차이를 확인해야 한다.

## 61-7. 상태를 여러 전역 변수에 분산

변경 흐름을 추적하기 어렵다.

## 61-8. 범위값을 코드 여러 곳에 직접 작성

상수로 관리해야 한다.

## 61-9. 상태 변경보다 출력만 구현

실제 기능이 동작하지 않는다.

## 61-10. 경계값 테스트 누락

최소·최대·순환 지점에서 오류가 발생할 수 있다.

---

# 62. 핵심 요약

```text
const fn = function () {}
→ 함수 표현식

const fn = () => {}
→ 화살표 함수
```

```text
value => value * 2
→ 매개변수 하나
→ 괄호 생략 가능
→ 암시적 반환
```

```text
return a, b
→ b 반환

return [a, b]
return { a, b }
→ 여러 값 구조화
```

```text
Toggle
→ !현재값

Clamp
→ 최소·최대 범위 제한

Wrap-around
→ 범위를 넘으면 반대쪽 끝
```

---

# 63. 최종 체크리스트

- [ ] 일반 함수 표현식과 화살표 함수를 구분할 수 있는가?
- [ ] 즉시 실행 함수 구조를 설명할 수 있는가?
- [ ] 매개변수 괄호 생략 규칙을 이해했는가?
- [ ] 중괄호·`return` 생략 규칙을 이해했는가?
- [ ] 객체 암시적 반환에 괄호를 사용할 수 있는가?
- [ ] `return a, b`의 결과를 설명할 수 있는가?
- [ ] 배열이나 객체로 여러 값을 반환할 수 있는가?
- [ ] 화살표 함수의 lexical `this`를 이해했는가?
- [ ] 화살표 함수를 생성자로 사용할 수 없음을 이해했는가?
- [ ] TV 상태값과 범위 상수를 구분할 수 있는가?
- [ ] 공통 전원 검사를 함수로 분리할 수 있는가?
- [ ] 채널 입력의 정수·범위를 검증할 수 있는가?
- [ ] 채널을 양 끝에서 순환시킬 수 있는가?
- [ ] Clamp로 볼륨을 제한할 수 있는가?
- [ ] 볼륨 조절 시 음소거를 해제할 수 있는가?
- [ ] 음소거 상태를 Boolean으로 토글할 수 있는가?
- [ ] 메시지와 실제 상태를 일치시킬 수 있는가?
- [ ] 관련 상태를 객체로 묶을 수 있는가?
- [ ] 경계값 테스트를 작성할 수 있는가?
- [ ] 클로저로 내부 상태를 보호할 수 있는가?

---

# 마무리

화살표 함수의 핵심은 단순히 코드를 짧게 쓰는 것에서 끝나지 않는다.

```text
함수의 실행 목적을 확인하고
    ↓
반환 축약 규칙을 정확히 사용하고
    ↓
this가 필요한지 판단하고
    ↓
관련 상태를 한곳에 모으고
    ↓
범위·토글·순환 규칙을 함수로 관리하는 것
```

이 흐름을 이해하면 이후 객체와 메서드 문서에서 상태와 동작을 더 자연스럽게 하나의 객체로 묶을 수 있다.
