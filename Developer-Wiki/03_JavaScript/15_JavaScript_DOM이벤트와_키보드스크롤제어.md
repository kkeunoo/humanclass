---
title: JavaScript DOM 이벤트와 키보드·스크롤 제어
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript DOM 이벤트와 키보드·스크롤 제어

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `15_JavaScript_DOM이벤트와_키보드스크롤제어.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/15_event.html`, `workspace_html/javascript/asset/js/15_event.js`, 강사님 동일 파일 |
| 핵심 범위 | 페이지 로드, 이벤트 등록·해제, 클릭, 키보드, 포커스, 스크롤, 방향키 이동 |
| 실습 범위 | 버튼 이벤트 비교, 로그인 검증, Enter 처리, 맨 위 이동, 스크롤 감지, 이미지 이동 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 15번은 HTML 파일만이 아니라 연결된 외부 JavaScript 파일까지 함께 확인해야 한다.  
> 원본의 실제 실행 흐름과 내 코드·강사님 코드 차이를 비교하고, 중복 초기화·오류 문구·구식 Keyboard API·안전하지 않은 로그 출력을 개선한다.

---

# 개요

이벤트는 사용자의 동작이나 브라우저 상태 변화가 발생했을 때 실행되는 신호다.

```text
사용자가 버튼 클릭
    ↓
click 이벤트 발생
    ↓
등록된 함수 실행
    ↓
화면 또는 상태 변경
```

대표 이벤트:

| 분류 | 이벤트 |
| --- | --- |
| 문서 로드 | `DOMContentLoaded`, `load` |
| 마우스 | `click`, `dblclick` |
| 키보드 | `keydown`, `keyup` |
| 폼 | `input`, `change`, `submit` |
| 포커스 | `focus`, `blur` |
| 화면 | `scroll`, `resize` |

```javascript
button.addEventListener(
    "click",
    () => {
        console.log("클릭")
    },
)
```

> [!IMPORTANT]
> 이벤트 처리에서는 **언제 요소를 선택하는가**, **어떤 함수 참조를 등록하는가**, **이벤트가 몇 번 등록되는가**를 함께 확인해야 한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| Event target | 이벤트가 실제 시작된 요소 |
| Event listener | 이벤트 발생 시 실행할 함수 |
| Event handler property | `onclick`, `onload` 같은 단일 함수 property |
| `addEventListener()` | 이벤트에 Listener 등록 |
| `removeEventListener()` | 등록된 Listener 제거 |
| 함수 참조 | 실행하지 않은 함수 객체 자체 |
| `event` 객체 | 발생한 이벤트의 상세 정보 |
| `event.key` | 사용자가 입력한 키 값 |
| `event.code` | 키보드 물리 위치 기준 코드 |
| `preventDefault()` | 브라우저 기본 동작 취소 |
| `focus()` | 요소에 키보드 포커스 이동 |
| `.click()` | JavaScript로 클릭 동작 발생 |
| `scrollY` | 현재 세로 스크롤 위치 |
| `scrollTo()` | 지정한 위치로 스크롤 |
| Event bubbling | 이벤트가 상위 요소 방향으로 전파되는 단계 |

---

# 학습 목표

- `<head>`의 Script가 Body 요소를 찾지 못할 수 있는 이유를 설명할 수 있다.
- `defer`, `DOMContentLoaded`, `load`의 차이를 이해한다.
- Inline 이벤트·DOM property·`addEventListener()` 방식을 비교할 수 있다.
- `onclick`을 여러 번 대입하면 마지막 함수만 남는 이유를 설명할 수 있다.
- 함수 참조와 함수 호출 결과를 구분할 수 있다.
- 같은 함수 참조로 Listener를 제거할 수 있다.
- 로그인 입력값을 공백까지 검증할 수 있다.
- 성공 시 기존 오류 메시지를 초기화할 수 있다.
- `keydown`, `keyup`, `input` 이벤트를 구분할 수 있다.
- `keyCode` 대신 `event.key`와 `event.code`를 사용할 수 있다.
- Enter로 포커스 이동과 제출을 구현할 수 있다.
- Modifier key를 검사할 수 있다.
- Scroll 위치를 읽고 부드럽게 맨 위로 이동할 수 있다.
- 방향키로 요소 위치를 변경할 수 있다.
- 입력 중에는 게임 이동을 차단할 수 있다.
- 이벤트 로그에 사용자 입력을 안전하게 출력할 수 있다.

---

# 1. 외부 JavaScript 연결

원본 HTML:

```html
<script src="asset/js/15_event.js"></script>
```

이 Script는 `<head>`에 있다.

브라우저가 Script를 만나면 HTML 파싱을 잠시 멈추고 파일을 내려받아 실행할 수 있다.

---

# 2. Head에서 요소 선택

```javascript
const button = (
    document.querySelector(
        "#btn1",
    )
)

console.log(button)
```

Body가 아직 파싱되지 않았다면 결과는 다음과 같다.

```text
null
```

---

# 3. 요소가 아직 없는 이유

```text
HTML 파싱 시작
    ↓
head의 script 실행
    ↓
#btn1 검색
    ↓
body는 아직 파싱 전
    ↓
null
```

선택자가 잘못된 것이 아니라 실행 시점 문제일 수 있다.

---

# 4. `defer`

```html
<script
    src="./asset/js/15_event.js"
    defer
></script>
```

`defer`를 사용하면 HTML 파싱을 막지 않고, 문서 파싱이 끝난 뒤 Script를 실행한다.

외부 Script에서 DOM 요소를 다룰 때 자주 사용하는 방식이다.

---

# 5. `DOMContentLoaded`

```javascript
document.addEventListener(
    "DOMContentLoaded",
    init,
)
```

DOM 트리 구성이 완료되면 실행된다.

이미지·스타일시트 같은 모든 외부 자원의 로드 완료까지 기다리지는 않는다.

---

# 6. `load`

```javascript
window.addEventListener(
    "load",
    init,
)
```

문서와 이미지 등 주요 외부 자원의 로드가 끝난 뒤 실행된다.

단순 DOM 선택만 필요하다면 `DOMContentLoaded` 또는 `defer`로 충분한 경우가 많다.

---

# 7. Body `onload`

원본 HTML:

```html
<body onload="init();">
```

HTML Attribute 안에서 전역 함수 `init()`을 호출한다.

Inline 이벤트 방식이다.

---

# 8. `window.onload`

원본 JavaScript:

```javascript
window.onload = init
```

`onload` property에 함수 참조를 저장한다.

다음처럼 괄호를 붙이면 잘못된 의미가 된다.

```text
window.onload = init()
```

`init()`이 즉시 실행되고 반환값이 `onload`에 저장된다.

---

# 9. 중복 초기화 문제

원본은 다음 두 방식을 동시에 사용한다.

```html
<body onload="init();">
```

```javascript
window.onload = init
```

`init()`이 두 경로로 호출될 수 있다.

---

# 10. 중복 초기화의 영향

```text
init() 첫 실행
→ bind()
→ Listener 등록

init() 두 번째 실행
→ bind()
→ Listener 재등록 가능
```

같은 기능이 여러 번 실행되거나 상태 초기값이 다시 설정될 수 있다.

초기화 방식은 하나만 선택한다.

---

# 11. 권장 초기화 구조

`defer`를 사용한 경우:

```javascript
function init() {
    // 요소 선택
    // 이벤트 등록
}

init()
```

또는:

```javascript
document.addEventListener(
    "DOMContentLoaded",
    init,
    {
        once: true,
    },
)
```

---

# 12. `once` 옵션

```javascript
element.addEventListener(
    "click",
    handler,
    {
        once: true,
    },
)
```

Listener가 한 번 실행된 뒤 자동 제거된다.

초기화 중복을 근본적으로 해결하는 대체재는 아니지만, 한 번만 처리해야 하는 이벤트에 사용할 수 있다.

---

# 13. `bind()` 함수

원본:

```javascript
function bind() {
    // 이벤트 등록
}
```

관련 이벤트 등록 코드를 한곳에 모은다.

다만 이름이 내장 `Function.prototype.bind()`와 같아 다음처럼 더 구체적으로 작성할 수 있다.

```javascript
function bindEvents() {
    // 이벤트 등록
}
```

---

# 14. DOM Property 이벤트

```javascript
button.onclick = (
    function () {
        console.log(
            "첫 번째",
        )
    }
)
```

`onclick`에는 함수 하나를 저장한다.

---

# 15. Property 덮어쓰기

```javascript
button.onclick = (
    function () {
        console.log(
            "첫 번째",
        )
    }
)

button.onclick = (
    function () {
        console.log(
            "두 번째",
        )
    }
)
```

버튼 클릭 결과:

```text
두 번째
```

두 번째 대입이 첫 번째 함수를 덮어쓴다.

---

# 16. `addEventListener()`

```javascript
button.addEventListener(
    "click",
    () => {
        console.log(
            "첫 번째",
        )
    },
)

button.addEventListener(
    "click",
    () => {
        console.log(
            "두 번째",
        )
    },
)
```

두 Listener가 모두 실행된다.

---

# 17. 이벤트 등록 방식 비교

| 방식 | 예 | 동일 이벤트의 여러 함수 |
| --- | --- | --- |
| Inline | `onclick="run()"` | Attribute 한 곳에 작성 |
| Property | `button.onclick = run` | 새 대입이 기존 함수 덮어씀 |
| Listener | `addEventListener("click", run)` | 여러 함수 등록 가능 |

실무에서는 HTML·JavaScript 분리와 해제 가능성 때문에 Listener 방식을 자주 사용한다.

---

# 18. Inline `onclick`

```html
<button
    type="button"
    id="btn3"
    onclick="handleButton3()"
>
    버튼3
</button>
```

```javascript
function handleButton3() {
    console.log(
        "버튼3 클릭",
    )
}
```

HTML 문자열에서 전역 함수 이름을 찾아 호출한다.

Module Script에서는 전역에서 함수를 찾지 못할 수 있다.

---

# 19. Inline 이벤트 개선

HTML:

```html
<button
    type="button"
    id="btn3"
>
    버튼3
</button>
```

JavaScript:

```javascript
const button3 = (
    document.querySelector(
        "#btn3",
    )
)

button3.addEventListener(
    "click",
    handleButton3,
)
```

---

# 20. 함수 참조

올바른 Listener 등록:

```javascript
button.addEventListener(
    "click",
    handleClick,
)
```

`handleClick` 함수 자체를 전달한다.

---

# 21. 함수 호출 결과 전달

잘못된 코드:

```text
button.addEventListener(
    "click",
    handleClick()
)
```

등록 시점에 함수가 즉시 실행된다.

반환값이 함수가 아니라면 Listener로 사용할 수 없다.

---

# 22. `removeEventListener()`

```javascript
function handleClick() {
    console.log("click")
}

button.addEventListener(
    "click",
    handleClick,
)

button.removeEventListener(
    "click",
    handleClick,
)
```

등록할 때와 같은 함수 참조를 사용해야 한다.

---

# 23. 익명 함수 제거 실패

```javascript
button.addEventListener(
    "click",
    function () {
        console.log("click")
    },
)

button.removeEventListener(
    "click",
    function () {
        console.log("click")
    },
)
```

코드가 같아 보여도 서로 다른 함수 객체다.

제거되지 않는다.

---

# 24. Listener 옵션 일치

`removeEventListener()`에는 다음 항목이 중요하다.

```text
같은 대상
같은 이벤트 타입
같은 함수 참조
같은 capture 설정
```

---

# 25. 로그인 버튼 이벤트

원본 구조:

```javascript
loginButton.addEventListener(
    "click",
    () => {
        const idInput = (
            document.querySelector(
                "#id",
            )
        )

        const passwordInput = (
            document.querySelector(
                "#pw",
            )
        )
    },
)
```

클릭 시점의 최신 입력값을 읽는다.

---

# 26. 요소 반복 선택 개선

고정된 요소는 초기화할 때 한 번 선택할 수 있다.

```javascript
const idInput = (
    document.querySelector(
        "#id",
    )
)

const passwordInput = (
    document.querySelector(
        "#pw",
    )
)
```

Listener 내부에서는 선택 결과를 재사용한다.

---

# 27. ID 공백 검사

```javascript
if (
    idInput.value.trim()
    === ""
) {
    warning.textContent = (
        "아이디는 필수입니다."
    )
}
```

공백만 입력해도 빈 값으로 판정한다.

---

# 28. 내 코드의 Password 문구 오류

내 원본은 비밀번호가 비었을 때 일부 위치에 다음 문구를 출력한다.

```text
아이디는 필수입니다.
```

실제 조건과 메시지가 일치하지 않는다.

---

# 29. Password 검사 수정

```javascript
if (
    passwordInput.value.trim()
    === ""
) {
    warning.textContent = (
        "비밀번호는 필수입니다."
    )
}
```

오류 메시지는 실제 실패 조건과 일치해야 한다.

---

# 30. 성공 시 오류 초기화

```javascript
warning.textContent = ""
```

한 번 오류가 표시된 뒤 입력을 수정하면 기존 메시지를 지워야 한다.

---

# 31. Early Return 검증

```javascript
function validateLogin() {
    if (
        idInput.value.trim()
        === ""
    ) {
        warning.textContent = (
            "아이디는 필수입니다."
        )

        idInput.focus()
        return false
    }

    if (
        passwordInput.value.trim()
        === ""
    ) {
        warning.textContent = (
            "비밀번호는 필수입니다."
        )

        passwordInput.focus()
        return false
    }

    warning.textContent = ""

    return true
}
```

---

# 32. 비밀번호 로그 출력 주의

원본은 비밀번호 값을 Console에 출력한다.

> [!WARNING]
> 비밀번호·토큰·인증번호는 Console과 운영 로그에 출력하지 않는다.

검증 여부만 기록한다.

```javascript
console.log(
    "로그인 입력 검증 완료",
)
```

---

# 33. 안전한 Log 함수

원본:

```javascript
div.innerHTML = message
```

개선:

```javascript
div.textContent = message
```

외부 문자열이 들어와도 HTML로 실행되지 않는다.

---

# 34. Log 최신 항목 위에 추가

```javascript
function log(
    message,
) {
    const item = (
        document.createElement(
            "div",
        )
    )

    item.classList.add(
        "log",
    )

    item.textContent = message

    logView.prepend(item)
}
```

`prepend()`를 사용하므로 최신 로그가 위에 표시된다.

---

# 35. `keydown`

```javascript
idInput.addEventListener(
    "keydown",
    event => {
        console.log(event.key)
    },
)
```

키를 누르는 순간 발생한다.

키를 계속 누르면 반복 발생할 수 있다.

---

# 36. `keyup`

```javascript
idInput.addEventListener(
    "keyup",
    event => {
        console.log(event.key)
    },
)
```

키를 놓을 때 발생한다.

---

# 37. `input`

```javascript
idInput.addEventListener(
    "input",
    () => {
        console.log(
            idInput.value,
        )
    },
)
```

키보드뿐 아니라 붙여넣기·삭제·음성 입력 등 값 변경 자체를 감지한다.

실시간 입력값 처리에는 `input`이 더 직접적이다.

---

# 38. Key 이벤트 비교

| 이벤트 | 발생 시점 | 대표 사용 |
| --- | --- | --- |
| `keydown` | 키를 누를 때 | 단축키, 방향키 |
| `keyup` | 키를 놓을 때 | 키 입력 완료 후 처리 |
| `input` | 값이 바뀔 때 | Text 입력 실시간 검증 |

---

# 39. Event 객체

```javascript
function handleKey(
    event,
) {
    console.log(
        event.target,
    )

    console.log(
        event.currentTarget,
    )

    console.log(
        event.key,
    )
}
```

Listener의 첫 번째 인수로 전달된다.

---

# 40. `target`과 `currentTarget`

| Property | 의미 |
| --- | --- |
| `target` | 이벤트가 실제 시작된 요소 |
| `currentTarget` | 현재 Listener가 실행 중인 요소 |

이벤트 위임과 Bubbling을 이해할 때 중요하다.

---

# 41. `keyCode`

원본:

```javascript
if (
    event.keyCode == 13
) {
    // Enter
}
```

`keyCode`는 Deprecated API다.

---

# 42. `event.key`

```javascript
if (
    event.key === "Enter"
) {
    // Enter 처리
}
```

사용자가 입력한 의미 있는 키 값을 확인한다.

---

# 43. `event.code`

```javascript
if (
    event.code === "KeyC"
) {
    // 물리적 C 키
}
```

키보드 배열의 물리적 위치가 중요할 때 사용할 수 있다.

---

# 44. Enter로 Password Focus

```javascript
idInput.addEventListener(
    "keydown",
    event => {
        if (
            event.key
            === "Enter"
        ) {
            event.preventDefault()
            passwordInput.focus()
        }
    },
)
```

---

# 45. Enter로 로그인 실행

원본 방식:

```javascript
if (
    event.key === "Enter"
) {
    loginButton.click()
}
```

버튼 Click Listener를 실행할 수 있다.

---

# 46. Form Submit 사용

HTML:

```html
<form id="login-form">
    <input
        id="id"
        name="id"
    >

    <input
        id="pw"
        name="password"
        type="password"
    >

    <button type="submit">
        로그인
    </button>
</form>
```

JavaScript:

```javascript
loginForm.addEventListener(
    "submit",
    event => {
        event.preventDefault()

        if (!validateLogin()) {
            return
        }

        console.log(
            "로그인 처리",
        )
    },
)
```

버튼 클릭과 Password Enter를 하나의 Submit 이벤트로 통합한다.

---

# 47. Modifier Key

```javascript
console.log(
    event.ctrlKey,
    event.shiftKey,
    event.altKey,
    event.metaKey,
)
```

특수 키의 동시 입력 상태를 Boolean으로 확인한다.

---

# 48. Ctrl+C 감지

```javascript
if (
    event.ctrlKey
    && event.key.toLowerCase()
        === "c"
) {
    console.log(
        "Ctrl+C 입력",
    )
}
```

감지하는 것과 복사를 차단하는 것은 다르다.

---

# 49. 복사 차단 주의

```javascript
element.addEventListener(
    "copy",
    event => {
        event.preventDefault()
    },
)
```

기술적으로 복사 기본 동작을 막을 수 있다.

하지만 접근성과 사용자 경험을 해칠 수 있으므로 실제 서비스에서는 신중하게 사용한다.

---

# 50. `focus()`

```javascript
passwordInput.focus()
```

키보드 입력 포커스를 Password 요소로 이동한다.

오류가 있는 입력 요소로 사용자를 안내할 때 유용하다.

---

# 51. `.click()`

```javascript
loginButton.click()
```

JavaScript로 Click 이벤트를 발생시킨다.

폼 제출이 목적이라면 Submit 이벤트 구조가 더 자연스럽다.

---

# 52. 맨 위 버튼

HTML:

```html
<button
    type="button"
    id="top-button"
>
    맨 위로
</button>
```

CSS:

```css
#top-button {
    position: fixed;
    right: 1rem;
    bottom: 1rem;
}
```

---

# 53. 현재 Scroll 위치

```javascript
console.log(
    window.scrollY,
)
```

현재 문서의 세로 Scroll 위치를 픽셀 단위로 반환한다.

---

# 54. `documentElement.scrollTop`

```javascript
console.log(
    document
        .documentElement
        .scrollTop,
)
```

문서 루트의 세로 Scroll 위치를 읽는 방식이다.

일반적으로 `window.scrollY`가 간결하다.

---

# 55. Smooth Scroll

```javascript
window.scrollTo({
    top: 0,
    behavior: "smooth",
})
```

전달하는 값은 JSON 문자열이 아니라 JavaScript 객체 리터럴이다.

---

# 56. Scroll Event

```javascript
window.addEventListener(
    "scroll",
    () => {
        console.log(
            window.scrollY,
        )
    },
)
```

Scroll 이벤트는 매우 자주 발생할 수 있다.

---

# 57. Scroll 성능 주의

Scroll Listener 안에서 다음 작업을 반복하면 성능이 저하될 수 있다.

- 복잡한 DOM 검색
- 큰 배열 계산
- 반복적인 Layout 측정
- 다수의 Style 변경
- 과도한 Console 출력

---

# 58. `requestAnimationFrame()` 활용

```javascript
let isScheduled = false

window.addEventListener(
    "scroll",
    () => {
        if (isScheduled) {
            return
        }

        isScheduled = true

        requestAnimationFrame(
            () => {
                console.log(
                    window.scrollY,
                )

                isScheduled = false
            },
        )
    },
)
```

화면 갱신 주기에 맞춰 처리 빈도를 제한할 수 있다.

---

# 59. Scroll 실습용 문서 높이

강사님 CSS:

```css
body {
    min-height: 300vh;
}
```

내 원본은 이 높이가 주석 처리되어 있어 콘텐츠가 짧으면 Scroll 이벤트와 맨 위 버튼을 확인하기 어렵다.

---

# 60. 게임 요소 기본 구조

```html
<img
    id="game"
    src="./images/game.png"
    alt="방향키로 이동하는 캐릭터"
>
```

```css
#game {
    position: absolute;
}
```

`left`, `top`을 변경하려면 위치 지정 기준이 필요하다.

---

# 61. 원본 초기 위치 차이

내 코드:

```text
left: 10px
top: 20px
```

강사님 코드:

```text
left: 20px
top: 10px
```

강사님 값은 원본 CSS 초기값과 일치한다.

---

# 62. `element.style`의 범위

```javascript
console.log(
    game.style.left,
)
```

Inline Style만 직접 읽는다.

Stylesheet에만 `left`가 있다면 빈 문자열일 수 있다.

---

# 63. Computed Style

```javascript
const style = getComputedStyle(
    game,
)

const left = Number.parseFloat(
    style.left,
)
```

최종 계산된 CSS 값을 읽을 수 있다.

---

# 64. 숫자 상태로 위치 관리

```javascript
let x = 20
let y = 10

function renderGame() {
    game.style.left = `${x}px`
    game.style.top = `${y}px`
}
```

Style 문자열을 매번 읽고 Parse하는 것보다 상태를 숫자로 관리하기 쉽다.

---

# 65. 오른쪽 이동

```javascript
if (
    event.key
    === "ArrowRight"
) {
    x += 10
}
```

강사님 원본은 오른쪽 이동만 구현한다.

---

# 66. 네 방향 이동

```javascript
function moveGame(
    event,
) {
    if (
        event.key
        === "ArrowRight"
    ) {
        x += 10
    } else if (
        event.key
        === "ArrowLeft"
    ) {
        x -= 10
    } else if (
        event.key
        === "ArrowDown"
    ) {
        y += 10
    } else if (
        event.key
        === "ArrowUp"
    ) {
        y -= 10
    } else {
        return
    }

    event.preventDefault()
    renderGame()
}
```

내 원본은 네 방향으로 기능을 확장했다.

---

# 67. 방향키 기본 동작

방향키는 페이지 Scroll을 발생시킬 수 있다.

게임 이동에 사용했다면:

```javascript
event.preventDefault()
```

로 기본 동작을 취소할 수 있다.

---

# 68. 입력 중 게임 이동 문제

Body 또는 Document에 Keydown Listener를 등록하면 Input에서 발생한 이벤트도 Bubbling되어 도달할 수 있다.

아이디 입력 중 방향키를 눌러도 캐릭터가 이동할 수 있다.

---

# 69. 입력 요소 제외

```javascript
function isTypingTarget(
    target,
) {
    return (
        target instanceof
            HTMLInputElement
        || target instanceof
            HTMLTextAreaElement
        || target instanceof
            HTMLSelectElement
        || target.isContentEditable
    )
}
```

```javascript
if (
    isTypingTarget(
        event.target,
    )
) {
    return
}
```

---

# 70. Event Bubbling

```text
실제 Target
    ↓
부모
    ↓
Body
    ↓
Document
    ↓
Window
```

일반적인 Click·Key 이벤트는 Target에서 상위 요소 방향으로 전파될 수 있다.

---

# 71. 외부 이미지 주의

원본은 외부 검색 URL 이미지를 사용한다.

문제:

- URL 변경·만료
- Hotlink 차단
- 네트워크 의존
- 대체 텍스트 누락
- 저장소 재현성 저하

프로젝트 내부 Asset 경로와 의미 있는 `alt`를 사용한다.

---

# 72. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 설명 | 상세 주석 다수 | 핵심 코드 중심 |
| Body 높이 | 300vh 주석 | 300vh 활성 |
| 게임 초기 Left | 10px | 20px |
| 게임 초기 Top | 20px | 10px |
| Password 오류 문구 | 일부 ID 문구로 잘못 작성 | 올바른 Password 문구 |
| 성공 Warning 초기화 | 없음 | 없음 |
| Ctrl+C 문구 | `ctrl+c` | `ctrl + c` |
| 게임 이동 | 상·하·좌·우 | 오른쪽 |
| 방향키 기본 Scroll 방지 | 없음 | 없음 |
| Key API | `keyCode` | `keyCode` |
| Log 출력 | `innerHTML` | `innerHTML` |

## 72-1. 내 코드의 장점

- Head Script와 DOM 로드 시점을 상세히 설명했다.
- Property 이벤트와 Listener 차이를 비교했다.
- 함수 참조와 호출 결과 차이를 기록했다.
- 네 방향 게임 이동을 구현했다.
- Inline Style을 읽는 이유를 설명했다.
- 키보드·스크롤 기능을 강사님 코드보다 확장했다.

## 72-2. 내 코드의 개선점

- Body `onload`와 `window.onload`를 함께 사용한다.
- Password 공백 조건에서 ID 오류 문구를 출력한다.
- 성공 후 Warning을 지우지 않는다.
- `keyCode`와 느슨한 비교를 사용한다.
- Input 입력 중에도 게임이 이동할 수 있다.
- Log에 `innerHTML`을 사용한다.
- Password 값을 Console에 출력한다.
- Scroll 실습용 높이가 비활성 상태다.

## 72-3. 강사님 코드의 장점

- DOM 로드 전후 선택 결과를 직접 보여 준다.
- 이벤트 Property·Listener·제거 방식을 순서대로 다룬다.
- Password 오류 메시지가 조건과 일치한다.
- Scroll 실습이 가능한 문서 높이를 제공한다.
- 기본 키보드 이동을 간결하게 구현한다.

## 72-4. 강사님 코드의 보충점

- 중복 `onload` 실행 가능성을 설명하지 않는다.
- 성공 후 Warning이 남는다.
- `keyCode`를 사용한다.
- 오른쪽 이동만 구현되어 있다.
- 방향키 기본 Scroll을 막지 않는다.
- 입력 중 게임 이동을 차단하지 않는다.
- Log XSS와 비밀번호 로그 위험 설명이 필요하다.

---

# 73. 기존 코드에서 개선한 이유

## 73-1. 로드 방식 통일

기존:

```html
<body onload="init()">
```

```javascript
window.onload = init
```

개선:

```html
<script
    src="./main.js"
    defer
></script>
```

```javascript
init()
```

## 73-2. Key API 교체

기존:

```javascript
event.keyCode == 13
```

개선:

```javascript
event.key === "Enter"
```

## 73-3. 안전한 로그

기존:

```javascript
item.innerHTML = message
```

개선:

```javascript
item.textContent = message
```

## 73-4. 위치 상태 분리

기존:

```javascript
game.style.left = (
    parseInt(
        game.style.left,
    ) + 10
) + "px"
```

개선:

```javascript
x += 10
renderGame()
```

---

# 74. 실무형 예제: 이벤트 초기화 완성본

```javascript
function getRequiredElement(
    selector,
) {
    const element = (
        document.querySelector(
            selector,
        )
    )

    if (element === null) {
        throw new Error(
            `${selector} 요소가 없습니다.`,
        )
    }

    return element
}

function init() {
    const form = getRequiredElement(
        "#login-form",
    )

    const idInput = getRequiredElement(
        "#id",
    )

    const passwordInput = (
        getRequiredElement(
            "#pw",
        )
    )

    const warning = getRequiredElement(
        "#warning",
    )

    const topButton = (
        getRequiredElement(
            "#top-button",
        )
    )

    const game = getRequiredElement(
        "#game",
    )

    let x = 20
    let y = 10

    function renderGame() {
        game.style.transform = (
            `translate(${x}px, ${y}px)`
        )
    }

    form.addEventListener(
        "submit",
        event => {
            event.preventDefault()

            if (
                idInput.value.trim()
                === ""
            ) {
                warning.textContent = (
                    "아이디는 필수입니다."
                )

                idInput.focus()
                return
            }

            if (
                passwordInput.value.trim()
                === ""
            ) {
                warning.textContent = (
                    "비밀번호는 필수입니다."
                )

                passwordInput.focus()
                return
            }

            warning.textContent = ""
        },
    )

    topButton.addEventListener(
        "click",
        () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth",
            })
        },
    )

    document.addEventListener(
        "keydown",
        event => {
            if (
                isTypingTarget(
                    event.target,
                )
            ) {
                return
            }

            if (
                event.key
                === "ArrowRight"
            ) {
                x += 10
            } else if (
                event.key
                === "ArrowLeft"
            ) {
                x -= 10
            } else if (
                event.key
                === "ArrowDown"
            ) {
                y += 10
            } else if (
                event.key
                === "ArrowUp"
            ) {
                y -= 10
            } else {
                return
            }

            event.preventDefault()
            renderGame()
        },
    )

    renderGame()
}

init()
```

## 74-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `defer` | DOM 파싱 후 Script 실행 |
| 필수 선택 함수 | 누락된 요소를 즉시 확인 |
| Submit 이벤트 | 버튼 클릭·Enter 제출 통합 |
| Early Return | 입력 오류별 처리 |
| `textContent` | 안전한 오류 출력 |
| `focus()` | 오류 입력으로 이동 |
| 숫자 상태 | 위치 계산 단순화 |
| `event.key` | 현대적인 키 판정 |
| 입력 Target 제외 | 폼 입력과 게임 조작 충돌 방지 |
| `preventDefault()` | 방향키 기본 Scroll 방지 |

---

# 75. 대표 오류로 이해하기

## 75-1. Head Script에서 요소가 `null`

DOM 파싱 전 선택했을 수 있다.

## 75-2. `onclick` 두 번 대입

마지막 함수만 남는다.

## 75-3. `addEventListener("click", fn())`

함수가 등록 전에 즉시 실행된다.

## 75-4. 다른 익명 함수로 Listener 제거

함수 참조가 달라 제거되지 않는다.

## 75-5. Password 오류인데 ID 문구 표시

조건과 메시지가 일치하지 않는다.

## 75-6. 방향키로 페이지와 게임이 함께 이동

`preventDefault()`가 필요할 수 있다.

---

# 76. 자주 하는 실수

## 76-1. Body `onload`와 Window `onload` 동시 사용

초기화가 중복될 수 있다.

## 76-2. `window.onload = init()` 작성

함수 참조가 아닌 실행 결과를 대입한다.

## 76-3. Property 방식으로 여러 Listener 기대

새 대입이 기존 함수를 덮어쓴다.

## 76-4. Listener 제거용 함수 참조 미보관

익명 함수는 나중에 같은 참조로 접근할 수 없다.

## 76-5. `keyCode` 사용

`event.key` 또는 `event.code`를 사용한다.

## 76-6. Password 값을 Console에 출력

민감정보를 노출하지 않는다.

## 76-7. 성공 시 기존 오류 문구 유지

정상 상태에서 메시지를 초기화한다.

## 76-8. Scroll Listener에서 무거운 작업

`requestAnimationFrame()` 또는 Throttle을 검토한다.

## 76-9. Input 입력 중 전역 방향키 처리

`event.target`을 검사한다.

## 76-10. 외부 이미지 URL에 의존

로컬 Asset과 `alt`를 사용한다.

---

# 77. 핵심 요약

```text
defer
DOMContentLoaded
load
→ Script 실행 시점 제어
```

```text
onclick property
→ 함수 하나

addEventListener()
→ 여러 Listener

removeEventListener()
→ 같은 함수 참조 필요
```

```text
keydown
→ 키를 누를 때

keyup
→ 키를 놓을 때

input
→ 값이 바뀔 때
```

```text
event.key
→ 입력된 키 의미

preventDefault()
→ 기본 동작 취소

focus()
→ 포커스 이동
```

```text
scrollY
→ 현재 세로 위치

scrollTo()
→ 지정 위치 이동

숫자 상태
→ 게임 위치 관리
```

---

# 78. 최종 체크리스트

- [ ] Head Script가 Body 요소를 찾지 못할 수 있음을 이해했는가?
- [ ] `defer`, `DOMContentLoaded`, `load`를 구분할 수 있는가?
- [ ] 초기화 방식을 하나로 통일했는가?
- [ ] `onclick` Property의 덮어쓰기를 이해했는가?
- [ ] `addEventListener()`로 여러 Listener를 등록할 수 있는가?
- [ ] 함수 호출이 아닌 함수 참조를 전달하는가?
- [ ] 같은 함수 참조로 Listener를 제거할 수 있는가?
- [ ] ID와 Password를 `trim()` 후 검사하는가?
- [ ] 오류 조건과 메시지가 일치하는가?
- [ ] 성공 시 Warning을 초기화하는가?
- [ ] Password를 Console에 출력하지 않는가?
- [ ] `innerHTML` 대신 `textContent`로 로그를 작성하는가?
- [ ] `keydown`, `keyup`, `input`을 구분할 수 있는가?
- [ ] `keyCode` 대신 `event.key`를 사용하는가?
- [ ] Enter로 Focus 또는 Submit을 처리할 수 있는가?
- [ ] Modifier key를 확인할 수 있는가?
- [ ] `scrollY`를 읽을 수 있는가?
- [ ] Smooth Scroll 객체를 작성할 수 있는가?
- [ ] Scroll 이벤트 성능을 고려하는가?
- [ ] 위치를 숫자 상태로 관리하는가?
- [ ] 네 방향키 이동을 구현할 수 있는가?
- [ ] 방향키 기본 Scroll을 막을 수 있는가?
- [ ] Input 입력 중 게임 이동을 차단하는가?
- [ ] 외부 이미지 대신 안정적인 Asset을 사용하는가?

---

# 마무리

DOM 이벤트의 핵심은 버튼에 함수를 연결하는 것에서 끝나지 않는다.

```text
DOM이 준비된 시점에 초기화하고
    ↓
이벤트 등록 방식을 일관되게 선택하고
    ↓
같은 함수 참조와 상태를 안전하게 관리하고
    ↓
키보드·폼·스크롤 동작의 충돌을 막고
    ↓
사용자 입력과 화면 출력을 안전하게 처리하는 것
```

이 흐름을 이해하면 이후 마우스 이벤트와 이벤트 전파 문서에서 더 복잡한 사용자 상호작용을 안정적으로 구현할 수 있다.
