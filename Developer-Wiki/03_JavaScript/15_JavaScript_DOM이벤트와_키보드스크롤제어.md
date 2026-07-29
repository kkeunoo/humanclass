# JavaScript DOM 이벤트와 키보드·스크롤 제어

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `15_JavaScript_DOM이벤트와_키보드스크롤제어.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `14_JavaScript_동기비동기와_이벤트루프.md` |
| 다음 학습 | 이후 JavaScript 원본 순서에 따라 진행 |
| 원본 기준 | `workspace/workspace_html/javascript/15_event.html`, `workspace/workspace_html/javascript/asset/js/15_event.js`, `workspace_teacher/workspace_html/javascript/15_event.html`, `workspace_teacher/workspace_html/javascript/asset/js/15_event.js` |
| 핵심 범위 | 페이지 로드 이벤트, `window.onload`, inline event, DOM property event, `addEventListener()`, `removeEventListener()`, click, keydown, keyup, `event.keyCode`, `event.key`, modifier key, `focus()`, `.click()`, scroll, `scrollTo()`, 키보드 이동 |
| 프로젝트 연결 | 로그인 검증, 키보드 단축키, Enter 제출, 맨 위 이동, 스크롤 감지, 키보드 게임 조작 |

> 이 문서는 HTML만이 아니라 실제로 연결된 `asset/js/15_event.js`까지 포함해 내 코드와 강사님 코드를 비교합니다. 내 코드는 강사님 코드에서 방향키 이동을 네 방향으로 확장하고 설명을 크게 추가했지만, 로그인 비밀번호 분기에서 아이디 오류 문구를 출력하는 실제 오류가 있습니다. 두 코드 모두 `window.onload`와 `<body onload="init()">`를 동시에 사용하고, `keyCode`, inline event, `innerHTML` 기반 로그, 외부 이미지 URL을 사용합니다. 원본은 그대로 보존하고 정확한 동작과 개선 방향을 분리해 설명합니다.

---

# 학습 목표

- `<head>`에서 script가 실행될 때 body 요소를 찾지 못할 수 있는 이유를 설명한다.
- `window.onload`와 `<body onload>`의 역할을 이해한다.
- `onclick` property 방식과 `addEventListener()` 방식의 차이를 설명한다.
- 같은 event property를 두 번 대입했을 때 덮어쓰기를 이해한다.
- 같은 event에 listener를 여러 개 등록하는 방법을 이해한다.
- `removeEventListener()`가 동일한 함수 참조를 요구한다는 점을 이해한다.
- inline `onclick`과 외부 JavaScript event binding을 비교한다.
- click event를 이용해 로그인 입력값을 검사한다.
- `trim()`으로 공백 입력을 검사한다.
- `keydown`과 `keyup`의 차이를 이해한다.
- event object에서 key와 modifier 정보를 읽는다.
- Enter를 이용해 focus 이동과 button click을 실행한다.
- scroll 위치를 읽고 smooth scroll을 실행한다.
- 방향키를 이용해 이미지의 위치를 변경한다.
- inline style과 computed style의 차이를 이벤트 이동 코드와 연결한다.
- 내 코드와 강사님 코드의 실제 차이와 오류를 정확히 기록한다.

---

# 1. HTML과 외부 JavaScript 연결

공통 HTML:

```html
<script src="asset/js/15_event.js"></script>
```

script가 `<head>` 안에 있습니다.

브라우저가 이 줄을 만났을 때 외부 JavaScript 파일을 불러와 실행합니다.

그 시점에는 `<body>` 내부의 button들이 아직 파싱되지 않았을 수 있습니다.

---

# 2. Head에서 Btn1 선택

공통 JavaScript:

```js
const btn1 =
  document.querySelector(
    "#btn1"
  )

console.log(
  1,
  "btn1",
  btn1
)
```

script가 head에서 즉시 실행되므로 일반적으로 `btn1`은 아직 존재하지 않습니다.

결과:

```text
null
```

내 코드 주석도 body가 아직 로딩되지 않아 읽지 못한다고 설명합니다.

---

# 3. Load 이후 선택

공통 구조:

```js
function init() {
  const btn1 =
    document.querySelector(
      "#btn1"
    )

  console.log(
    2,
    "btn1",
    btn1
  )

  bind()
}
```

페이지 load 이후 실행되므로 `btn1` Element를 정상적으로 찾을 수 있습니다.

---

# 4. Body Onload

공통 HTML:

```html
<body onload="init();">
```

body의 load event가 발생하면 전역 함수 `init()`을 호출합니다.

inline event handler 방식입니다.

주석 처리된 원본:

```html
<!--
<body onload="javascript:init()">
-->
```

`javascript:` 접두어 없이 `init()`만 작성해도 동작합니다.

---

# 5. Window Onload

공통 JavaScript:

```js
window.onload =
  init
```

window의 load event property에 함수 참조를 할당합니다.

중요:

```js
window.onload = init
```

은 함수 참조를 등록합니다.

```js
window.onload = init()
```

처럼 괄호를 붙이면 즉시 실행한 반환값을 대입하게 됩니다.

---

# 6. Onload 중복 등록 문제

원본은 다음 두 방식을 동시에 사용합니다.

```html
<body onload="init();">
```

```js
window.onload =
  init
```

따라서 환경과 event 처리 흐름에 따라 `init()`이 두 경로에서 실행될 수 있습니다.

`init()`이 반복 실행되면 `bind()`도 반복 호출되고 `addEventListener()` listener가 중복 등록될 수 있습니다.

원본 설명은 `window.onload`와 body onload를 별도 방식으로 소개하지만 실제 파일에서는 둘 다 활성화되어 있습니다.

실무에서는 한 가지 방식만 선택하는 편이 안전합니다.

---

# 7. AddEventListener Load

내 코드에 주석 처리된 예:

```js
// window.addEventListener(
//   "load",
//   init
// )
```

`addEventListener()`는 같은 event에 여러 listener를 등록할 수 있습니다.

그러나 같은 target, 같은 event type, 같은 function reference, 같은 주요 option으로 동일 listener를 반복 등록하면 일반적으로 중복 등록되지 않습니다.

내 주석의 “여러 번 적용할 수 있으나 현재 예시는 함수가 같아 중복 실행 안 됨”은 이 특성을 가리킵니다.

---

# 8. Init에서 Game 위치 설정

내 코드:

```js
game.style.left =
  "10px"

game.style.top =
  "20px"
```

강사님 코드:

```js
game.style.top =
  "10px"

game.style.left =
  "20px"
```

HTML CSS 초기값:

```css
#game {
  top: 10px;
  left: 20px;
}
```

강사님은 CSS와 같은 값을 inline style로 넣습니다.

내 코드는 값이 서로 바뀌어 최종 위치가:

```text
left: 10px
top: 20px
```

가 됩니다.

---

# 9. Bind 함수

공통 구조:

```js
function bind() {
  // event listener 등록
}
```

관련 event binding 코드를 한 함수에 모았습니다.

원본은 실무에서 event들을 묶기 위해 이런 함수를 사용한다고 설명합니다.

`bind()`는 JavaScript 내장 `Function.prototype.bind()`와 이름이 같지만 여기서는 사용자가 만든 일반 함수입니다.

---

# 10. Onclick Property

공통 원본:

```js
btn1.onclick =
  function() {
    console.log(
      "btn1 클릭"
    )
  }

btn1.onclick =
  function() {
    console.log(
      "btn1 click"
    )
  }
```

`onclick` property에는 최종적으로 함수 하나만 저장됩니다.

두 번째 대입이 첫 번째 함수를 덮어씁니다.

버튼1 클릭 시 일반적으로:

```text
btn1 click
```

만 출력됩니다.

---

# 11. AddEventListener

공통 원본:

```js
btn2.addEventListener(
  "click",
  function() {
    console.log(
      "btn2 클릭"
    )
  }
)

btn2.addEventListener(
  "click",
  function() {
    console.log(
      "btn2 click"
    )
  }
)
```

두 listener가 모두 등록됩니다.

버튼2 클릭 시 등록 순서대로 두 문자열이 출력됩니다.

```text
btn2 클릭
btn2 click
```

---

# 12. Property 방식과 Listener 방식 비교

| 방식 | 예 | 같은 Event 여러 함수 |
| --- | --- | --- |
| inline HTML | `onclick="fn()"` | HTML attribute 하나 기준 |
| DOM property | `element.onclick = fn` | 새 대입이 기존 값 덮어씀 |
| Event listener | `addEventListener("click", fn)` | 여러 listener 등록 가능 |

실무에서는 관심사 분리와 제거 가능성 때문에 `addEventListener()`가 자주 사용됩니다.

---

# 13. Inline Onclick

HTML:

```html
<button
  type="button"
  id="btn3"
  onclick="btn3click()"
>
  버튼3
</button>
```

JavaScript:

```js
function btn3click() {
  console.log(
    "btn3 click"
  )
}
```

button 클릭 시 전역 함수 이름을 HTML 문자열에서 찾습니다.

module script나 scope 구조에 따라 inline handler에서 함수를 찾지 못할 수도 있습니다.

---

# 14. 함수 참조와 함수 호출

공통 원본:

```js
btn4.addEventListener(
  "click",
  btn4click
)
```

올바른 함수 참조 전달입니다.

잘못된 형태:

```js
btn4.addEventListener(
  "click",
  btn4click()
)
```

괄호를 붙이면 등록 시점에 함수가 실행되고, 현재 함수에 return이 없으므로 `undefined`가 listener 위치에 전달됩니다.

---

# 15. RemoveEventListener

공통 원본:

```js
btn4.addEventListener(
  "click",
  btn4click
)

btn4.removeEventListener(
  "click",
  btn4click
)
```

동일한 함수 참조를 사용했기 때문에 listener가 제거됩니다.

따라서 버튼4를 클릭해도 `"btn4 click"`이 출력되지 않습니다.

---

# 16. 익명 함수 제거

다음은 제거되지 않습니다.

```js
button.addEventListener(
  "click",
  function() {
    console.log("click")
  }
)

button.removeEventListener(
  "click",
  function() {
    console.log("click")
  }
)
```

두 익명 함수는 코드 내용이 같아도 서로 다른 함수 객체입니다.

제거하려면 참조를 저장해야 합니다.

```js
function handleClick() {
  console.log("click")
}

button.addEventListener(
  "click",
  handleClick
)

button.removeEventListener(
  "click",
  handleClick
)
```

---

# 17. Login Click Event

공통 구조:

```js
login.addEventListener(
  "click",
  function() {
    const id =
      document.querySelector(
        "#id"
      )

    const pw =
      document.querySelector(
        "#pw"
      )

    const warning =
      document.querySelector(
        ".warning"
      )
  }
)
```

click 시점의 최신 id와 password value를 읽습니다.

---

# 18. Trim 검사

공통 원본:

```js
if (
  id.value.trim() == ""
) {
}
```

`trim()`은 앞뒤 공백을 제거합니다.

입력값이 space만 있는 경우에도 빈 문자열로 판정할 수 있습니다.

엄격 비교 권장:

```js
id.value.trim() === ""
```

---

# 19. 내 Login 오류

내 코드 password 분기:

```js
else if (
  pw.value.trim() == ""
) {
  console.log(
    "아이디는 필수입니다."
  )

  warning.innerText =
    "아이디는 필수입니다."

  log(
    "비밀번호는 필수입니다."
  )
}
```

비밀번호가 비어 있는데 Console과 warning에는 아이디 오류 문구를 표시합니다.

log 영역에만 비밀번호 오류 문구가 표시됩니다.

이는 실제 코드 오류입니다.

올바른 문구:

```js
console.log(
  "비밀번호는 필수입니다."
)

warning.innerText =
  "비밀번호는 필수입니다."
```

---

# 20. 강사님 Login 분기

강사님 코드:

```js
else if (
  pw.value.trim() == ""
) {
  warning.innerText =
    "비밀번호는 필수입니다"

  log(
    "비밀번호는 필수입니다"
  )
}
```

비밀번호 오류 문구를 올바르게 표시합니다.

다만 성공했을 때 기존 warning을 지우는 `else`가 없습니다.

---

# 21. 성공 시 Warning 초기화

내 코드에는 주석 처리된 이전 연습에 성공 분기가 있습니다.

```js
// else {
//   warning.innerText = ""
// }
```

현재 실제 실행 코드에는 성공 시 warning을 지우는 부분이 없습니다.

한 번 오류가 표시된 후 값을 정상 입력하고 다시 클릭해도 기존 warning이 남을 수 있습니다.

개선:

```js
else {
  warning.textContent =
    ""
}
```

---

# 22. Log 함수

공통 원본:

```js
function log(message) {
  const div =
    document.createElement(
      "div"
    )

  div.classList.add(
    "log"
  )

  div.innerHTML =
    message

  const view =
    document.querySelector(
      "#view"
    )

  view.prepend(div)
}
```

새 로그를 view의 첫 번째 자식으로 넣으므로 최신 로그가 위에 표시됩니다.

---

# 23. InnerHTML 위험

현재 원본은 내부에서 만든 문자열만 `log()`에 전달합니다.

하지만 외부 입력을 `message`로 전달하면 `innerHTML` 때문에 HTML이 실행될 수 있습니다.

안전한 text 로그:

```js
div.textContent =
  message
```

현재 예제 메시지는 고정 문자열과 숫자 중심이지만 함수 자체는 범용이므로 `textContent`가 더 안전합니다.

---

# 24. Keydown

공통 원본:

```js
document
  .querySelector("#id")
  .addEventListener(
    "keydown",
    function() {
      // key를 누르는 시점
    }
  )
```

키가 눌리는 순간 발생합니다.

키를 계속 누르면 반복 발생할 수 있습니다.

---

# 25. Keyup

공통 원본:

```js
document
  .querySelector("#id")
  .addEventListener(
    "keyup",
    function(event) {
    }
  )
```

눌렀던 키를 놓을 때 발생합니다.

입력값이 반영된 뒤 검사하기 쉬워 원본은 중복 검사 같은 예를 설명합니다.

현대 입력 처리에서는 `input` event가 더 직접적인 경우도 많습니다.

---

# 26. Event Object

listener callback의 첫 번째 인수로 event object를 받을 수 있습니다.

```js
function(event) {
  console.log(event)
}
```

원본에서 사용하는 property:

```js
event.keyCode
event.ctrlKey
event.shiftKey
event.altKey
```

---

# 27. KeyCode

공통 원본:

```js
log(
  "keyCode:" +
  event.keyCode
)
```

`keyCode`는 오래된 API이며 현재는 deprecated입니다.

권장:

```js
event.key
event.code
```

예:

```js
if (
  event.key === "Enter"
) {
}
```

---

# 28. Enter로 Password Focus

공통 원본:

```js
if (
  event.keyCode == 13
) {
  log("엔터 빵")

  const pw =
    document.querySelector(
      "#pw"
    )

  pw.focus()
}
```

id input에서 Enter를 놓으면 password input으로 focus가 이동합니다.

개선:

```js
if (
  event.key === "Enter"
) {
  pw.focus()
}
```

---

# 29. Ctrl+C 감지

공통 원본:

```js
if (
  event.ctrlKey &&
  event.keyCode == 67
) {
  alert("ctrl + c")
}
```

내 alert text:

```text
ctrl+c
```

강사님 alert text:

```text
ctrl + c
```

이 코드는 조합을 감지할 뿐 복사를 실제로 막지는 않습니다.

복사를 막으려면 `copy` event와 `preventDefault()`를 고려해야 합니다.

또한 사용자 경험과 접근성 때문에 복사 차단은 일반적으로 신중해야 합니다.

---

# 30. Password에서 Enter로 Login Click

공통 원본:

```js
if (
  event.keyCode == 13
) {
  const login =
    document.querySelector(
      "#login"
    )

  login.click()
}
```

사용자가 password input에서 Enter를 놓으면 로그인 button의 click event를 프로그래밍 방식으로 발생시킵니다.

실제 form에서는 submit event를 사용하는 편이 더 자연스럽습니다.

---

# 31. Top Button

공통 HTML:

```html
<button
  type="button"
  id="top"
>
  맨 위로
</button>
```

CSS:

```css
#top {
  position: fixed;
  right: 10px;
  bottom: 10px;
}
```

화면 오른쪽 아래에 고정됩니다.

---

# 32. ScrollTop 출력

공통 원본:

```js
console.log(
  document
    .documentElement
    .scrollTop
)
```

문서의 현재 세로 scroll 위치를 읽습니다.

주석 처리된 직접 이동:

```js
document
  .documentElement
  .scrollTop =
  0
```

---

# 33. Smooth Scroll

공통 원본:

```js
window.scrollTo({
  top: 0,
  behavior: "smooth"
})
```

객체 literal을 전달합니다.

내 코드 주석의 “나중에 배울 제이슨?”은 정확히는 JSON이 아니라 JavaScript 객체입니다.

JSON과 객체 literal은 비슷하게 보이지만 동일한 개념은 아닙니다.

---

# 34. Body Height 차이

강사님 CSS:

```css
body {
  height: 300vh;
}
```

내 CSS:

```css
/* body {
  height: 300vh;
} */
```

내 코드는 body height가 주석 처리되어 있어 콘텐츠가 viewport보다 짧으면 scroll bar가 생기지 않을 수 있습니다.

따라서:

- 맨 위로 button 기능 확인
- window scroll event 확인

이 어려울 수 있습니다.

강사님 문서는 300vh로 scroll 실습이 가능합니다.

---

# 35. Scroll Event

공통 원본:

```js
window.addEventListener(
  "scroll",
  function() {
    console.log(
      "window.scrollY",
      window.scrollY
    )
  }
)
```

scroll할 때마다 현재 Y 위치를 출력합니다.

scroll event는 매우 자주 발생할 수 있으므로 무거운 작업은 throttle이나 requestAnimationFrame을 고려해야 합니다.

---

# 36. Teacher Game 이동

강사님 코드는 오른쪽 방향키만 구현합니다.

```js
if (
  event.keyCode == 39
) {
  game.style.left =
    (
      parseInt(
        game.style.left
      ) +
      10
    ) +
    "px"
}
```

초기 inline left가 `"20px"`이므로 누를 때마다 10px 증가합니다.

---

# 37. My Game 이동 확장

내 코드는 네 방향을 모두 구현합니다.

```text
39 → 오른쪽
37 → 왼쪽
40 → 아래
38 → 위
```

각 방향마다 left 또는 top을 10px씩 변경합니다.

강사님 코드보다 기능이 확장되었습니다.

---

# 38. 내 초기값과 방향 이동

내 init:

```js
left = "10px"
top = "20px"
```

따라서 첫 오른쪽 이동:

```text
10px → 20px
```

첫 위 이동:

```text
20px → 10px
```

강사님은:

```text
left 20px → 30px
```

입니다.

---

# 39. Inline Style가 필요한 이유

원본은 다음 값을 읽습니다.

```js
game.style.left
game.style.top
```

`element.style`은 inline style만 읽습니다.

CSS stylesheet에만 값이 있다면:

```js
game.style.left
```

는 빈 문자열일 수 있습니다.

따라서 `init()`에서 inline style을 한 번 설정합니다.

원본 내 설명도 이 점을 기록합니다.

---

# 40. Computed Style 대안

stylesheet에 적용된 실제 값을 읽으려면:

```js
const style =
  getComputedStyle(
    game
  )

const left =
  parseFloat(
    style.left
  )
```

를 사용할 수 있습니다.

다만 매 key event마다 계산 style을 읽는 것보다 위치 상태를 숫자 변수로 관리하는 편이 구조적으로 더 좋을 수 있습니다.

---

# 41. 숫자 상태 기반 이동 개선

```js
let x = 20
let y = 10

function renderGame() {
  game.style.left =
    `${x}px`

  game.style.top =
    `${y}px`
}

document.addEventListener(
  "keydown",
  function(event) {
    if (
      event.key === "ArrowRight"
    ) {
      x += 10
    } else if (
      event.key === "ArrowLeft"
    ) {
      x -= 10
    } else if (
      event.key === "ArrowDown"
    ) {
      y += 10
    } else if (
      event.key === "ArrowUp"
    ) {
      y -= 10
    } else {
      return
    }

    event.preventDefault()
    renderGame()
  }
)
```

style 문자열을 매번 parse하지 않습니다.

---

# 42. Arrow Key 기본 동작

방향키는 페이지 scroll 같은 기본 동작을 일으킬 수 있습니다.

게임 이동에 사용할 때:

```js
event.preventDefault()
```

를 고려할 수 있습니다.

원본에는 없으므로 방향키로 이미지와 페이지가 함께 움직일 가능성이 있습니다.

---

# 43. Body Keydown Target

공통 원본:

```js
document
  .querySelector("body")
  .addEventListener(
    "keydown",
    function(event) {
    }
  )
```

keydown event는 focus된 input 등에서 시작해 body까지 bubble할 수 있습니다.

따라서 id나 password 입력 중 방향키를 눌러도 game이 이동할 수 있습니다.

게임 조작을 별도 상태나 특정 영역 focus에 제한하는 것이 좋습니다.

---

# 44. Event Bubbling 확장

원본은 bubbling을 직접 설명하지 않지만 body listener가 input key event도 받을 수 있는 이유와 연결됩니다.

event는 일반적으로 target에서 시작해 상위 요소 방향으로 전파됩니다.

```js
console.log(
  event.target
)

console.log(
  event.currentTarget
)
```

- `target`: 실제 event가 시작된 요소
- `currentTarget`: 현재 listener가 등록된 요소

---

# 45. Login Form 접근성

HTML은 label 없이 text만 작성합니다.

```html
아이디 :
<input id="id">
```

개선:

```html
<label for="id">
  아이디
</label>

<input
  type="text"
  id="id"
>
```

password도 같은 방식으로 연결할 수 있습니다.

---

# 46. External Image

양쪽 원본은 Google image search 계열 외부 URL을 사용합니다.

문제:

- URL 변경 가능
- hotlink 차단 가능
- 네트워크 없으면 표시되지 않음
- 대체 text 없음

개선:

```html
<img
  id="game"
  src="./images/game.png"
  alt="키보드로 이동하는 게임 캐릭터"
>
```

---

# 47. Html 구조 차이

내 HTML은 button 영역 뒤에:

```html
<br><hr>
```

를 추가하고 view 앞에도 `<hr>`를 넣습니다.

강사님 HTML은 이 구분선이 없습니다.

기능 차이는 없고 시각적 구분만 다릅니다.

---

# 48. My Code 분석

## 48.1 장점

- head script 실행 시 DOM이 null일 수 있는 이유를 상세히 설명했다.
- load event와 callback 개념을 설명했다.
- onclick property가 덮어쓰기 된다는 점을 설명했다.
- addEventListener가 같은 event에 여러 함수를 등록할 수 있음을 설명했다.
- 함수 참조와 함수 호출의 차이를 설명했다.
- 익명 함수는 removeEventListener로 제거하기 어렵다는 점을 설명했다.
- 로그인 값 검사에 trim을 사용했다.
- keydown과 keyup 차이를 설명했다.
- event object에서 keyCode와 modifier key를 확인했다.
- Enter로 focus 이동과 login click을 구현했다.
- smooth scroll과 scrollY 출력을 구현했다.
- 방향키 이동을 네 방향으로 확장했다.
- inline style을 초기화해야 `game.style.left`를 읽을 수 있다는 점을 설명했다.
- 강사님보다 기능과 주석이 풍부하다.

## 48.2 개선점

- body onload와 window.onload를 동시에 활성화해 init이 중복 실행될 수 있다.
- init 중복 실행 시 addEventListener listener가 반복 등록될 수 있다.
- password 공백 분기에서 Console과 warning 문구가 아이디 오류로 잘못 작성되었다.
- 성공 시 warning을 지우지 않는다.
- `==` 대신 `===`가 권장된다.
- `keyCode`는 deprecated다.
- Ctrl+C 감지만 하고 실제 복사는 막지 않는다.
- JSON이라고 추측한 객체는 JavaScript object literal이다.
- body height가 주석이라 scroll 기능을 확인하기 어려울 수 있다.
- 방향키에서 preventDefault가 없어 페이지도 scroll될 수 있다.
- body keydown listener가 input 사용 중에도 game을 움직일 수 있다.
- log 함수가 innerHTML을 사용한다.
- password를 Console에 출력한다.
- 외부 이미지에 alt가 없다.
- inline event와 외부 binding을 혼용한다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.

---

# 49. Teacher Code 분석

## 49.1 장점

- head script와 load 이후 DOM 선택 차이를 보여 준다.
- onclick property와 addEventListener 차이를 직접 비교한다.
- removeEventListener를 동일 함수 참조로 실행한다.
- 로그인 id와 password 검사를 구현한다.
- password 오류 문구가 올바르다.
- keyup에서 keyCode와 modifier key를 확인한다.
- Enter로 focus 이동과 button click을 구현한다.
- 맨 위로 smooth scroll을 구현한다.
- window scrollY를 확인한다.
- 오른쪽 방향키로 image 이동을 구현한다.
- body height 300vh로 scroll 실습이 가능하다.

## 49.2 개선점

- body onload와 window.onload를 동시에 활성화한다.
- 중복 init 가능성을 설명하지 않는다.
- keyCode를 사용한다.
- 로그인 성공 시 warning을 지우지 않는다.
- password 값을 Console에 출력한다.
- `==` 비교를 사용한다.
- log 함수가 innerHTML을 사용한다.
- 방향키 이동이 오른쪽만 구현되어 있다.
- 방향키 기본 scroll을 막지 않는다.
- body listener가 form 입력 중에도 동작할 수 있다.
- inline onclick과 외부 event binding을 혼용한다.
- 외부 이미지에 alt가 없다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.

---

# 50. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| HTML 구분선 | `<hr>` 추가 | 없음 |
| Body height | 300vh 주석 처리 | 300vh 활성 |
| Init game left | 10px | 20px |
| Init game top | 20px | 10px |
| 이벤트 설명 | 매우 상세 | 핵심 중심 |
| Login Console label | `ID:`, `PW:` | `id.value :`, `pw.value :` |
| Password 오류 warning | 아이디 문구로 잘못 작성 | 비밀번호 문구 정상 |
| Ctrl+C alert | `ctrl+c` | `ctrl + c` |
| 방향키 이동 | 상·하·좌·우 | 오른쪽만 |
| Game debug log | 대부분 주석 | keyCode와 left를 log |
| Scroll 실습 가능성 | body height 주석이라 낮음 | 300vh로 가능 |
| 전체 기능 | 강사님 코드 확장 | 기본 예제 |

---

# 51. 대표 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>DOM 이벤트</title>

  <script
    src="./main.js"
    defer
  ></script>
</head>
<body>
  <button
    type="button"
    id="button"
  >
    클릭
  </button>

  <label for="userId">
    아이디
  </label>

  <input
    type="text"
    id="userId"
  >

  <div
    id="warning"
    aria-live="polite"
  ></div>
</body>
</html>
```

```js
"use strict"

function init() {
  const button =
    document.querySelector(
      "#button"
    )

  const userId =
    document.querySelector(
      "#userId"
    )

  const warning =
    document.querySelector(
      "#warning"
    )

  button.addEventListener(
    "click",
    function() {
      if (
        userId.value.trim() === ""
      ) {
        warning.textContent =
          "아이디는 필수입니다."
      } else {
        warning.textContent =
          ""
      }
    }
  )
}

init()
```

`defer`를 사용했기 때문에 body onload와 window.onload를 중복 사용할 필요가 없습니다.

---

# 52. 실무 활용: 로그인 Submit

```js
const form =
  document.querySelector(
    "#loginForm"
  )

form.addEventListener(
  "submit",
  function(event) {
    event.preventDefault()

    const id =
      form.elements.id.value.trim()

    const password =
      form.elements.password.value

    if (id === "") {
      showWarning(
        "아이디는 필수입니다."
      )

      return
    }

    if (
      password.trim() === ""
    ) {
      showWarning(
        "비밀번호는 필수입니다."
      )

      return
    }

    showWarning("")
  }
)
```

button click과 password Enter를 따로 처리하지 않아도 submit event 하나로 통합할 수 있습니다.

---

# 53. 실무 활용: 제거 가능한 Listener

```js
function handleButtonClick() {
  console.log("click")
}

button.addEventListener(
  "click",
  handleButtonClick
)

button.removeEventListener(
  "click",
  handleButtonClick
)
```

동일 함수 참조를 유지합니다.

---

# 54. 자주 하는 실수

## 54.1 Head Script에서 Body Element 즉시 선택

defer나 load 이후 실행이 필요할 수 있습니다.

## 54.2 Body Onload와 Window Onload 동시 사용

init과 listener가 중복 실행될 수 있습니다.

## 54.3 Onclick Property에 여러 함수 대입

마지막 함수가 앞 함수를 덮어씁니다.

## 54.4 AddEventListener에 함수 호출 결과 전달

`fn()`이 아니라 `fn`을 전달해야 합니다.

## 54.5 다른 익명 함수로 RemoveEventListener 호출

같은 함수 참조가 아니므로 제거되지 않습니다.

## 54.6 Password 오류인데 ID 문구 출력

내 코드의 실제 오류입니다.

## 54.7 KeyCode 사용

deprecated API이므로 `event.key` 또는 `event.code`를 검토합니다.

## 54.8 Smooth Scroll Option을 JSON이라고 부름

JavaScript 객체 literal입니다.

## 54.9 Style Sheet 값이 Element.style에서 읽힌다고 생각

inline style만 직접 읽습니다.

## 54.10 사용자 입력을 InnerHTML 로그에 전달

XSS 위험이 있습니다.

---

# 55. 면접·복습 포인트

## Q1. Head에서 Btn1이 Null인 이유는 무엇인가요?

script 실행 시점에 body의 button이 아직 파싱되지 않았기 때문입니다.

## Q2. Onclick을 두 번 대입하면 어떻게 되나요?

두 번째 함수가 첫 번째 함수를 덮어씁니다.

## Q3. AddEventListener의 장점은 무엇인가요?

같은 event에 여러 listener를 등록할 수 있고 함수 참조를 유지하면 제거할 수 있습니다.

## Q4. RemoveEventListener가 동작하려면 무엇이 같아야 하나요?

target, event type, 함수 참조와 주요 capture option이 일치해야 합니다.

## Q5. 내 Login 코드의 실제 오류는 무엇인가요?

password가 비었을 때 Console과 warning에 아이디 오류 문구를 표시합니다.

## Q6. Keydown과 Keyup 차이는 무엇인가요?

keydown은 키를 누를 때, keyup은 키를 놓을 때 발생합니다.

## Q7. KeyCode 대신 무엇을 사용할 수 있나요?

`event.key` 또는 `event.code`를 사용할 수 있습니다.

## Q8. Login Button의 Click을 JavaScript로 발생시키는 방법은 무엇인가요?

`login.click()`을 호출합니다.

## Q9. Element.style.left가 빈 문자열일 수 있는 이유는 무엇인가요?

CSS stylesheet 값은 inline style property에 직접 들어 있지 않기 때문입니다.

## Q10. 내 코드와 강사님 코드의 Game 이동 차이는 무엇인가요?

내 코드는 네 방향을 구현하고 강사님은 오른쪽 이동만 구현합니다.

---

# Problems

## 문제 1. Load 이전 선택

head script에서 body button을 선택하면 null이 될 수 있는 이유를 설명하세요.

## 문제 2. Defer

외부 script가 DOM 파싱 이후 실행되도록 `defer`를 추가하세요.

## 문제 3. Onclick 덮어쓰기

같은 button.onclick에 두 함수를 순서대로 대입했을 때 최종 동작을 설명하세요.

## 문제 4. Listener 두 개

한 button click에 listener 두 개를 등록하세요.

## 문제 5. Listener 제거

등록한 named function listener를 제거하세요.

## 문제 6. 잘못된 함수 전달

`addEventListener("click", fn())`가 잘못된 이유를 설명하세요.

## 문제 7. Inline Event 개선

inline onclick을 addEventListener 방식으로 바꾸세요.

## 문제 8. ID 검사

아이디가 공백만 있으면 오류 문구를 표시하세요.

## 문제 9. Password 검사

비밀번호가 공백만 있으면 올바른 오류 문구를 표시하세요.

## 문제 10. Warning 초기화

입력값이 모두 정상일 때 기존 warning을 지우세요.

## 문제 11. Enter Focus

id input에서 Enter를 누르면 password input으로 focus를 이동하세요.

## 문제 12. Enter Submit

password input에서 Enter를 누르면 login button click을 실행하세요.

## 문제 13. KeyCode 개선

Enter 판정을 `event.key`로 작성하세요.

## 문제 14. Ctrl+C 감지

Ctrl+C 조합을 event.key 방식으로 감지하세요.

## 문제 15. Smooth Scroll

button 클릭 시 페이지 맨 위로 부드럽게 이동하세요.

## 문제 16. Scroll 위치

window scroll 시 현재 scrollY를 출력하세요.

## 문제 17. 오른쪽 이동

ArrowRight를 누르면 image를 10px 오른쪽으로 이동하세요.

## 문제 18. 네 방향 이동

상·하·좌·우 방향키 이동을 모두 구현하세요.

## 문제 19. 기본 Scroll 방지

게임 방향키 조작 시 페이지 scroll을 막으세요.

## 문제 20. 안전한 Log

log 함수에서 innerHTML 대신 안전한 property를 사용하세요.

## 문제 21. 원본 중복 초기화

body onload와 window.onload를 동시에 사용했을 때 문제를 설명하세요.

## 문제 22. 종합 이벤트 초기화

다음 요구사항을 만족하는 `init()`을 작성하세요.

- DOMContentLoaded 이후 한 번만 실행
- login form submit 사용
- id와 password 공백 검사
- 오류는 textContent로 출력
- 성공 시 warning 제거
- Arrow key로 game 이동
- 입력 중에는 game 이동하지 않음
- keyCode 사용하지 않음
- 방향키 기본 scroll 방지
- 위치는 숫자 상태 변수로 관리

---

# Answers & Explanations

## 정답 1

script가 head에서 실행될 때 body가 아직 파싱되지 않았기 때문에 selector 결과가 null일 수 있습니다.

## 정답 2

```html
<script
  src="./main.js"
  defer
></script>
```

## 정답 3

두 번째 대입이 첫 번째 함수를 덮어쓰므로 마지막 함수만 실행됩니다.

## 정답 4

```js
button.addEventListener(
  "click",
  function() {
    console.log("first")
  }
)

button.addEventListener(
  "click",
  function() {
    console.log("second")
  }
)
```

## 정답 5

```js
function handleClick() {
  console.log("click")
}

button.addEventListener(
  "click",
  handleClick
)

button.removeEventListener(
  "click",
  handleClick
)
```

## 정답 6

`fn()`은 등록 시점에 즉시 실행되고 반환값을 listener로 전달합니다. 함수 자체를 전달하려면 `fn`을 사용합니다.

## 정답 7

```js
const btn3 =
  document.querySelector(
    "#btn3"
  )

btn3.addEventListener(
  "click",
  btn3click
)
```

HTML의 onclick attribute는 제거합니다.

## 정답 8

```js
if (
  id.value.trim() === ""
) {
  warning.textContent =
    "아이디는 필수입니다."
}
```

## 정답 9

```js
if (
  password.value.trim() === ""
) {
  warning.textContent =
    "비밀번호는 필수입니다."
}
```

## 정답 10

```js
else {
  warning.textContent =
    ""
}
```

## 정답 11

```js
id.addEventListener(
  "keyup",
  function(event) {
    if (
      event.key === "Enter"
    ) {
      password.focus()
    }
  }
)
```

## 정답 12

```js
password.addEventListener(
  "keyup",
  function(event) {
    if (
      event.key === "Enter"
    ) {
      login.click()
    }
  }
)
```

## 정답 13

```js
if (
  event.key === "Enter"
) {
}
```

## 정답 14

```js
if (
  event.ctrlKey &&
  event.key.toLowerCase() === "c"
) {
  console.log("Ctrl+C")
}
```

## 정답 15

```js
topButton.addEventListener(
  "click",
  function() {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    })
  }
)
```

## 정답 16

```js
window.addEventListener(
  "scroll",
  function() {
    console.log(
      window.scrollY
    )
  }
)
```

## 정답 17

```js
let x = 20

document.addEventListener(
  "keydown",
  function(event) {
    if (
      event.key ===
      "ArrowRight"
    ) {
      x += 10

      game.style.left =
        `${x}px`
    }
  }
)
```

## 정답 18

```js
let x = 20
let y = 10

document.addEventListener(
  "keydown",
  function(event) {
    if (
      event.key ===
      "ArrowRight"
    ) {
      x += 10
    } else if (
      event.key ===
      "ArrowLeft"
    ) {
      x -= 10
    } else if (
      event.key ===
      "ArrowDown"
    ) {
      y += 10
    } else if (
      event.key ===
      "ArrowUp"
    ) {
      y -= 10
    } else {
      return
    }

    game.style.left =
      `${x}px`

    game.style.top =
      `${y}px`
  }
)
```

## 정답 19

```js
if (
  event.key.startsWith(
    "Arrow"
  )
) {
  event.preventDefault()
}
```

## 정답 20

```js
function log(message) {
  const div =
    document.createElement(
      "div"
    )

  div.classList.add(
    "log"
  )

  div.textContent =
    message

  view.prepend(div)
}
```

## 정답 21

`init()`이 두 번 실행될 수 있고 `bind()`에서 listener가 중복 등록될 수 있습니다. load 초기화 방식은 하나만 선택해야 합니다.

## 정답 22

```js
document.addEventListener(
  "DOMContentLoaded",
  function init() {
    const form =
      document.querySelector(
        "#loginForm"
      )

    const id =
      document.querySelector(
        "#id"
      )

    const password =
      document.querySelector(
        "#pw"
      )

    const warning =
      document.querySelector(
        ".warning"
      )

    const game =
      document.querySelector(
        "#game"
      )

    let x = 20
    let y = 10

    function renderGame() {
      game.style.left =
        `${x}px`

      game.style.top =
        `${y}px`
    }

    form.addEventListener(
      "submit",
      function(event) {
        event.preventDefault()

        if (
          id.value.trim() === ""
        ) {
          warning.textContent =
            "아이디는 필수입니다."

          return
        }

        if (
          password.value.trim() === ""
        ) {
          warning.textContent =
            "비밀번호는 필수입니다."

          return
        }

        warning.textContent =
          ""
      }
    )

    document.addEventListener(
      "keydown",
      function(event) {
        const target =
          event.target

        if (
          target instanceof
            HTMLInputElement ||
          target instanceof
            HTMLTextAreaElement
        ) {
          return
        }

        if (
          event.key ===
          "ArrowRight"
        ) {
          x += 10
        } else if (
          event.key ===
          "ArrowLeft"
        ) {
          x -= 10
        } else if (
          event.key ===
          "ArrowDown"
        ) {
          y += 10
        } else if (
          event.key ===
          "ArrowUp"
        ) {
          y -= 10
        } else {
          return
        }

        event.preventDefault()
        renderGame()
      }
    )

    renderGame()
  },
  {
    once: true
  }
)
```

---

# Final Checklist

## Load와 초기화

- [ ] head script 실행 시 body DOM이 없을 수 있음을 이해했다.
- [ ] `defer`, load, DOMContentLoaded 차이를 이해했다.
- [ ] body onload와 window.onload를 동시에 사용하지 않았다.
- [ ] init이 한 번만 실행되는지 확인했다.
- [ ] bind가 반복 호출되어 listener가 중복되지 않는지 확인했다.

## Event 등록

- [ ] onclick property가 덮어쓰기 됨을 이해했다.
- [ ] addEventListener로 여러 listener를 등록했다.
- [ ] 함수 호출이 아니라 함수 참조를 전달했다.
- [ ] removeEventListener에 같은 함수 참조를 사용했다.
- [ ] inline event 사용 필요성을 검토했다.

## Login

- [ ] id와 password를 trim 후 검사했다.
- [ ] password 오류에 올바른 문구를 표시했다.
- [ ] 성공 시 warning을 지웠다.
- [ ] password 값을 Console에 노출하지 않았다.
- [ ] innerHTML 대신 textContent를 사용했다.
- [ ] form submit event 사용을 검토했다.

## Keyboard

- [ ] keydown과 keyup을 구분했다.
- [ ] keyCode 대신 event.key 또는 event.code를 사용했다.
- [ ] Enter로 focus 이동을 구현했다.
- [ ] Enter로 로그인 동작을 실행했다.
- [ ] modifier key를 확인했다.
- [ ] input 입력 중 게임 이동을 막았다.
- [ ] 방향키 기본 scroll을 막았다.

## Scroll과 이동

- [ ] smooth scroll option이 JavaScript 객체임을 이해했다.
- [ ] scrollY를 확인했다.
- [ ] body 높이가 scroll 실습에 충분한지 확인했다.
- [ ] inline style과 computed style을 구분했다.
- [ ] 위치를 숫자 상태로 관리했다.
- [ ] 네 방향 이동을 검증했다.

## 원본 코드 검수

- [ ] 두 실제 15_event.html을 비교했다.
- [ ] 연결된 두 실제 15_event.js를 비교했다.
- [ ] 내 body height 주석과 강사님 300vh 차이를 기록했다.
- [ ] game 초기 left·top 차이를 기록했다.
- [ ] 내 password 오류 문구 버그를 기록했다.
- [ ] 강사님 오른쪽 이동과 내 네 방향 이동을 기록했다.
- [ ] Ctrl+C alert 문자열 차이를 기록했다.
- [ ] body onload와 window.onload 중복을 기록했다.
- [ ] keyCode deprecated를 기록했다.
- [ ] log innerHTML 위험을 기록했다.
- [ ] 외부 이미지와 alt 누락을 기록했다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 15번은 load, click, keyboard, scroll event와 DOM 조작을 다룬다.
- 외부 JavaScript가 head에서 즉시 실행되면 body의 `#btn1`은 아직 없어 null일 수 있다.
- load 이후 `init()`에서 다시 선택하면 Element를 찾을 수 있다.
- 원본은 `<body onload="init()">`와 `window.onload = init`을 동시에 사용한다.
- 이 구조는 init과 bind가 중복 실행될 가능성이 있으므로 한 방식만 선택하는 편이 안전하다.
- `onclick` property를 두 번 대입하면 마지막 함수가 앞 함수를 덮어쓴다.
- `addEventListener()`는 같은 event에 여러 listener를 등록할 수 있다.
- listener에는 `btn4click()`이 아니라 `btn4click` 함수 참조를 전달해야 한다.
- `removeEventListener()`는 등록 때와 같은 함수 참조가 필요하다.
- inline onclick은 HTML과 JavaScript를 섞으므로 외부 binding으로 통일할 수 있다.
- 로그인 검사는 `trim()`으로 공백 입력을 판정한다.
- 내 password 공백 분기에는 Console과 warning에 아이디 오류 문구를 표시하는 실제 버그가 있다.
- 강사님 코드는 password 오류 문구를 올바르게 표시한다.
- 두 코드 모두 로그인 성공 시 기존 warning을 지우지 않는다.
- `keydown`은 키를 누를 때, `keyup`은 키를 놓을 때 발생한다.
- `event.keyCode`는 deprecated이며 `event.key` 또는 `event.code`가 권장된다.
- id에서 Enter를 누르면 password로 focus가 이동한다.
- password에서 Enter를 누르면 `login.click()`으로 click event를 발생시킨다.
- Ctrl+C 조건을 감지하는 것만으로 복사가 실제 차단되는 것은 아니다.
- `window.scrollTo({ top: 0, behavior: "smooth" })`의 인수는 JSON이 아니라 JavaScript 객체다.
- 내 HTML은 body 300vh가 주석 처리되어 scroll 실습이 어려울 수 있다.
- 강사님 HTML은 body height 300vh로 scroll event와 top button을 확인할 수 있다.
- `window.scrollY`는 현재 세로 scroll 위치를 나타낸다.
- 강사님 game 이동은 오른쪽 방향키만 구현한다.
- 내 코드는 상·하·좌·우 네 방향을 모두 구현한다.
- 내 초기 game 위치는 left 10px, top 20px이고 강사님은 left 20px, top 10px이다.
- `element.style.left`는 inline style을 읽으므로 init에서 위치를 inline으로 설정한다.
- 방향키 이동은 숫자 상태를 별도 변수로 관리하는 방식이 더 명확할 수 있다.
- 방향키 기본 페이지 scroll을 막으려면 `preventDefault()`를 고려한다.
- body keydown listener는 input 사용 중에도 game 이동을 발생시킬 수 있다.
- `log()`는 `innerHTML`보다 `textContent`가 안전하다.
- 외부 이미지 URL과 alt 누락은 재현성과 접근성 문제를 만들 수 있다.
