# JavaScript 마우스 이벤트와 드래그·복사 제어

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `16_JavaScript_마우스이벤트와_드래그복사제어.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `15_JavaScript_DOM이벤트와_키보드스크롤제어.md` |
| 다음 학습 | 이후 JavaScript 원본 순서에 따라 진행 |
| 원본 기준 | `workspace/workspace_html/javascript/16_event_mouse.html`, `workspace/workspace_html/javascript/asset/js/16_event_mouse.js`, `workspace_teacher/workspace_html/javascript/16_event_mouse.html`, `workspace_teacher/workspace_html/javascript/asset/js/16_event_mouse.js` |
| 핵심 범위 | `contextmenu`, `selectstart`, `copy`, Clipboard API, `dblclick`, `mousedown`, `mouseup`, `click`, mouse 좌표, `mouseover`, `mouseout`, `mousemove`, 마우스 추적 이미지, drag and drop, `resize`, `innerWidth`, `innerHeight` |
| 프로젝트 연결 | 복사 방지·출처 추가, 마우스 좌표 표시, 커서 추적 UI, 직접 구현한 drag and drop, 반응형 resize 처리 |

> 이 문서는 HTML과 실제 연결된 JavaScript 파일을 함께 비교했습니다. 내 코드는 강사님 코드와 기능적으로 거의 같지만 설명이 훨씬 많고, 일부 문구·공백·로그 형식이 다릅니다. 내 코드에는 `"moseover"` 오타가 있으며, 양쪽 모두 `innerHTML` 로그, `return false` 기반 기본 동작 차단, 오래된 clipboard 접근 방식, `mouseover`/`mouseout`의 자식 요소 진입 문제 가능성, body 전체 `mousemove` listener 중복, 외부 이미지와 `alt` 누락이 있습니다. 원본은 그대로 보존하고 정확한 동작과 개선 방법을 별도로 설명합니다.

---

# 학습 목표

- 우클릭 시 발생하는 `contextmenu` event를 이해한다.
- `selectstart` event로 text 선택 시작을 감지한다.
- `copy` event와 `preventDefault()`를 이용해 기본 복사를 제어한다.
- 현재 선택 text를 `window.getSelection()`으로 읽는다.
- clipboard에 새로운 text를 넣는 원리를 이해한다.
- `dblclick`, `mousedown`, `mouseup`, `click`의 발생 시점을 구분한다.
- `offset`, `page`, `client`, `screen` 좌표계를 비교한다.
- `mouseover`·`mouseout`과 `mouseenter`·`mouseleave` 차이를 이해한다.
- `mousemove`가 매우 자주 발생하는 event임을 이해한다.
- 마우스 위치를 따라 image를 이동시킨다.
- drag 시작점에서 pointer와 요소 좌상단의 offset을 저장한다.
- drag 중 page 좌표에서 offset을 빼 요소 위치를 계산한다.
- resize event로 viewport 크기를 읽는다.
- 내 코드와 강사님 코드의 실제 차이를 원본 기준으로 기록한다.

---

# 1. HTML 구조

공통 주요 요소:

```html
<div id="area" class="area">
  굉장히 중요해서 막 ctrl+c로 퍼가고 싶은 글씨인데 막음
</div>

<div id="area2" class="area">
  뭔가 복사할 때 덧붙이기
</div>

<img
  id="game"
  src="외부 이미지 URL"
>

<div id="img" class="area"></div>

<div id="view"></div>
```

각 요소 역할:

```text
#area
→ 우클릭과 text 선택 차단

#area2
→ 복사·mouse event 실습

#game
→ mouse pointer를 따라 이동하는 이미지

#img
→ 직접 drag하는 사각형

#view
→ event log 출력 영역
```

---

# 2. Script 실행 시점

공통 HTML:

```html
<script src="./asset/js/16_event_mouse.js"></script>
```

script는 `<head>` 안에 있습니다.

JavaScript 파일이 먼저 실행되지만 실제 DOM binding은 load 이후 실행합니다.

```js
window.onload =
  function() {
    bind()
  }
```

따라서 body 요소가 모두 load된 뒤 selector를 실행합니다.

---

# 3. Window Onload

공통 원본:

```js
window.onload =
  function() {
    bind()
  }
```

window load event는 HTML뿐 아니라 image 등 주요 resource의 load까지 기다립니다.

이 문서에는 외부 image가 있으므로 네트워크 상태에 따라 `bind()` 실행 시점이 늦어질 수 있습니다.

DOM 요소만 필요하다면 `DOMContentLoaded`나 `defer`를 고려할 수 있습니다.

---

# 4. 전역 Drag 상태

공통 원본:

```js
let _isDrag = false
let _offsetX = 0
let _offsetY = 0
```

역할:

```text
_isDrag
→ 현재 drag 중인지 저장

_offsetX
→ 요소 내부에서 pointer를 누른 X 위치

_offsetY
→ 요소 내부에서 pointer를 누른 Y 위치
```

내 코드 주석은 전역변수를 underscore로 구분할 수 있다고 설명합니다.

underscore는 naming convention일 뿐 JavaScript의 특별한 접근 제한 기능은 아닙니다.

---

# 5. Log 함수

공통 구조:

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

최신 log를 위에 표시하기 위해 `prepend()`를 사용합니다.

---

# 6. Log의 InnerHTML

양쪽 원본은:

```js
div.innerHTML =
  message
```

를 사용합니다.

현재 전달값은 코드 내부에서 만든 고정 문자열과 좌표 숫자이므로 즉시 문제가 드러나지는 않습니다.

하지만 사용자 입력을 전달하면 HTML injection 또는 XSS 위험이 생길 수 있습니다.

안전한 기본값:

```js
div.textContent =
  message
```

---

# 7. Contextmenu Event

공통 원본:

```js
const area =
  document.querySelector(
    "#area"
  )

area.oncontextmenu =
  function() {
    alert(
      "오른쪽 버튼 금지입니다"
    )

    return false
  }
```

`contextmenu`는 일반적으로 mouse 오른쪽 button을 눌러 context menu를 열 때 발생합니다.

---

# 8. Return False 의미

DOM event property handler에서:

```js
return false
```

를 반환하면 기본 context menu 표시를 막을 수 있습니다.

보다 명시적인 방식:

```js
area.addEventListener(
  "contextmenu",
  function(event) {
    event.preventDefault()
  }
)
```

`preventDefault()`가 무엇을 막는지 코드상 더 분명합니다.

---

# 9. 우클릭 차단의 한계

우클릭 menu를 막더라도 사용자는 다음 방법으로 콘텐츠에 접근할 수 있습니다.

- 개발자 도구
- keyboard shortcut
- 페이지 source
- JavaScript 비활성화
- network request
- screenshot

따라서 context menu 차단은 보안 기능으로 볼 수 없습니다.

사용자 경험을 해칠 수도 있으므로 사용 목적을 신중히 검토해야 합니다.

---

# 10. Selectstart Event

공통 원본:

```js
area.onselectstart =
  function() {
    return false
  }
```

text 선택이 시작될 때 발생하는 event입니다.

false를 반환해 기본 text 선택을 막습니다.

CSS 대안:

```css
#area {
  user-select: none;
}
```

---

# 11. Copy Event

공통 원본:

```js
const area2 =
  document.querySelector(
    "#area2"
  )

area2.addEventListener(
  "copy",
  function(event) {
  }
)
```

사용자가 area2의 text를 복사할 때 callback이 실행됩니다.

Ctrl+C뿐 아니라 context menu 복사 등에서도 발생할 수 있습니다.

---

# 12. Copy 기본 동작 차단

공통 원본:

```js
event.preventDefault()
```

브라우저의 기본 복사 동작을 막습니다.

이후 직접 clipboard data를 설정합니다.

---

# 13. 현재 선택 Text

공통 원본:

```js
const selection =
  window
    .getSelection()
    .toString()
```

현재 document에서 선택된 text를 문자열로 가져옵니다.

선택이 없다면 빈 문자열일 수 있습니다.

---

# 14. 빈 Selection 검사

공통 원본:

```js
if (
  selection.length == 0
) {
  return
}
```

선택 text가 없으면 clipboard에 별도 값을 넣지 않고 종료합니다.

엄격 비교:

```js
selection.length === 0
```

을 권장할 수 있습니다.

---

# 15. 출처 문자열 추가

공통 원본:

```js
const str =
  "[출처] www.naver.com"

const result =
  selection + str
```

선택 text 바로 뒤에 출처가 붙습니다.

결과 예:

```text
선택한 글씨[출처] www.naver.com
```

가독성을 위해 줄바꿈이나 space를 넣을 수 있습니다.

```js
const result =
  `${selection}\n\n[출처] www.naver.com`
```

---

# 16. ClipboardData SetData

공통 원본:

```js
event.clipboardData.setData(
  "text/plain",
  result
)
```

현재 copy event의 clipboard data에 plain text를 설정합니다.

원본 내 설명의 “plain은 순수한 글씨”는 `text/plain` MIME type을 뜻합니다.

---

# 17. Clipboard 접근 주의

`event.clipboardData`는 copy event 내부에서 사용하는 전통적인 방식입니다.

현대 Clipboard API:

```js
navigator.clipboard
  .writeText(result)
```

도 있지만 secure context, permission, 사용자 gesture 등의 조건이 있습니다.

현재 원본 방식은 copy event를 직접 가로채는 목적에 적합합니다.

---

# 18. HTML 문구 차이

내 HTML:

```text
뭔가 복사할 때 덧붙이기
```

강사님 HTML:

```text
뭔가 복사할 때 덛 붙이기
```

강사님 원본에는 `"덛 붙이기"` 표기가 있습니다.

동작에는 영향이 없는 text 차이이며 원본을 임의로 수정하지 않습니다.

---

# 19. Dblclick

공통 구조:

```js
area2.addEventListener(
  "dblclick",
  function() {
    log(
      "더블클릭 발생"
    )
  }
)
```

double click이 완료되었을 때 발생합니다.

내 코드 log:

```text
더블클릭발생
```

강사님 코드:

```text
더블클릭 발생
```

space 차이만 있습니다.

---

# 20. “0.3초” 설명 검토

내 코드 주석:

```text
0.3초 이내에 클릭이 두 번 발생했을 때 dblclick
```

double-click 판정 시간은 운영체제와 사용자 설정, browser 환경에 영향을 받을 수 있습니다.

항상 정확히 0.3초라고 단정하면 부정확합니다.

---

# 21. Mousedown

공통 원본:

```js
area2.addEventListener(
  "mousedown",
  function() {
    log("mousedown")
  }
)
```

mouse button을 누르는 순간 발생합니다.

button을 아직 놓지 않아도 실행됩니다.

---

# 22. Mouseup

공통 원본:

```js
area2.addEventListener(
  "mouseup",
  function() {
    log("mouseup")
  }
)
```

눌렀던 mouse button을 놓는 순간 발생합니다.

---

# 23. Click

공통 원본:

```js
area2.addEventListener(
  "click",
  function(event) {
    log("click")
  }
)
```

일반적으로 같은 요소에서 mousedown과 mouseup이 정상적으로 완료된 뒤 click이 발생합니다.

대표 순서:

```text
mousedown
mouseup
click
```

double click 시 click도 함께 여러 번 발생할 수 있습니다.

---

# 24. Mouse Event 순서

area2를 한 번 클릭할 때 대체로:

```text
mouseover 또는 mouseenter
mousemove 여러 번
mousedown
mouseup
click
```

이 발생할 수 있습니다.

정확한 발생 sequence는 pointer 이동과 child target에 따라 달라질 수 있습니다.

---

# 25. OffsetY

공통 원본:

```js
event.offsetY
```

event target의 padding edge를 기준으로 한 pointer Y 좌표입니다.

내 설명은 DOM 좌상단 기준 상대값이라고 정리합니다.

실제로 event target과 nested element에 따라 기준이 바뀔 수 있으므로 target을 함께 확인하는 것이 좋습니다.

---

# 26. PageY

공통 원본:

```js
event.pageY
```

document 전체 좌표 기준입니다.

scroll된 거리까지 포함합니다.

페이지 위쪽에서 얼마나 떨어졌는지를 나타냅니다.

---

# 27. ClientY

공통 원본:

```js
event.clientY
```

현재 viewport 좌상단 기준입니다.

scroll을 내려도 viewport의 같은 화면 위치라면 clientY는 비슷하게 유지될 수 있습니다.

내 주석의 “서버에 접속할 수 있는 도구(client)”라는 표현은 부정확합니다.

여기서 client는 viewport coordinate를 의미합니다.

---

# 28. ScreenY

공통 원본:

```js
event.screenY
```

사용자 physical screen 좌상단 기준 좌표입니다.

browser window의 위치에 따라 값이 달라집니다.

---

# 29. 좌표계 비교

| Property | 기준 |
| --- | --- |
| `offsetX`, `offsetY` | event target 내부 |
| `pageX`, `pageY` | 전체 document |
| `clientX`, `clientY` | 현재 viewport |
| `screenX`, `screenY` | physical screen |

원본은 Y 값만 log하지만 X도 같은 기준 체계를 가집니다.

---

# 30. Mouseover

강사님 코드:

```js
area2.addEventListener(
  "mouseover",
  function() {
    log("mouseover")

    area2.style.backgroundColor =
      "yellow"
  }
)
```

내 코드 실제 log:

```js
log("moseover")
```

`mouseover`가 아니라 `"moseover"`로 오타가 있습니다.

event type은 올바르게 `"mouseover"`라서 event 동작에는 문제가 없고 출력 text만 잘못됩니다.

---

# 31. Mouseout

공통 원본:

```js
area2.addEventListener(
  "mouseout",
  function() {
    log("mouseout")

    area2.style.backgroundColor =
      "white"
  }
)
```

pointer가 요소에서 벗어날 때 실행됩니다.

---

# 32. Mouseover와 Mouseenter 차이

원본에는 대안으로 주석 처리되어 있습니다.

```js
// mouseenter
// mouseleave
```

차이:

```text
mouseover / mouseout
→ bubble함
→ child element 경계를 오갈 때도 추가 발생 가능

mouseenter / mouseleave
→ 일반적으로 bubble하지 않음
→ 해당 요소 경계 진입·이탈 중심
```

원본 주석의 “동일한 기능”은 단순 예제에서는 비슷해 보이지만 완전히 동일하지 않습니다.

---

# 33. Mousemove

공통 원본:

```js
area2.addEventListener(
  "mousemove",
  function(event) {
    log("mousemove")

    log(
      `offsetX:${event.offsetX}, ` +
      `offsetY:${event.offsetY}`
    )
  }
)
```

pointer가 area2 안에서 움직일 때 매우 자주 발생합니다.

---

# 34. Mousemove Log 과다

mousemove 한 번마다 DOM 요소를 두 개씩 생성해 `#view` 앞에 추가합니다.

문제:

- DOM node가 빠르게 증가
- 화면과 memory 부담
- log가 매우 길어짐
- UI 반응 저하 가능

개선:

- 기존 한 요소의 text만 갱신
- throttle 적용
- requestAnimationFrame 사용
- 개발 완료 후 log 제거

---

# 35. 내 Log 형식 차이

내 코드:

```text
offsetX : 10, offsetY : 20
```

강사님 코드:

```text
offsetX:10, offsetY:20
```

space formatting 차이만 있습니다.

---

# 36. Game Mouse 추적

공통 원본:

```js
document
  .querySelector("body")
  .addEventListener(
    "mousemove",
    function(event) {
      const game =
        document.querySelector(
          "#game"
        )

      game.style.top =
        event.pageY +
        10 +
        "px"

      game.style.left =
        event.pageX +
        10 +
        "px"
    }
  )
```

mouse가 body 위에서 움직이면 image가 pointer를 따라갑니다.

---

# 37. 왜 10px 떨어뜨리는가?

내 코드 주석은 image가 pointer 바로 아래 있으면 image가 pointer target을 가릴 수 있다고 설명합니다.

10px offset:

```js
pageX + 10
pageY + 10
```

으로 pointer와 image를 조금 떨어뜨립니다.

더 안정적인 CSS 대안:

```css
#game {
  pointer-events: none;
}
```

그러면 image가 mouse event target을 가로채지 않습니다.

---

# 38. Page 좌표를 사용하는 이유

`#game`은:

```css
position: absolute;
```

입니다.

document 좌표에 배치하므로 `pageX`, `pageY`와 자연스럽게 연결됩니다.

`clientX`, `clientY`를 사용할 경우 scroll offset을 별도로 고려해야 할 수 있습니다.

---

# 39. Body Mousemove Listener가 두 개

양쪽 원본은 body에 `mousemove` listener를 두 번 등록합니다.

첫 번째:

```text
game 이미지를 pointer에 따라 이동
```

두 번째:

```text
_isDrag가 true면 #img 이동
```

`addEventListener()`이므로 두 listener가 모두 실행됩니다.

하나의 listener로 합칠 수도 있지만 학습 목적상 역할을 분리한 구조입니다.

---

# 40. Drag 시작

공통 원본:

```js
document
  .querySelector("#img")
  .addEventListener(
    "mousedown",
    function(event) {
      _isDrag =
        true

      _offsetX =
        event.offsetX

      _offsetY =
        event.offsetY
    }
  )
```

mouse button을 누르면 drag 상태를 시작합니다.

---

# 41. Offset을 저장하는 이유

pointer로 요소의 중앙을 눌렀다고 가정합니다.

pointer의 page 좌표를 그대로 element left/top으로 넣으면 element 좌상단이 pointer 위치로 순간 이동합니다.

그래서 누른 지점의 내부 offset을 저장합니다.

```text
새 left
= pointer pageX - 누른 내부 offsetX

새 top
= pointer pageY - 누른 내부 offsetY
```

---

# 42. Drag 중 이동

공통 원본:

```js
if (_isDrag) {
  img.style.top =
    (
      event.pageY -
      _offsetY
    ) +
    "px"

  img.style.left =
    (
      event.pageX -
      _offsetX
    ) +
    "px"
}
```

pointer가 요소의 같은 내부 지점을 잡은 것처럼 이동합니다.

---

# 43. Drag 종료

공통 원본:

```js
document
  .querySelector("#img")
  .addEventListener(
    "mouseup",
    function() {
      _isDrag =
        false
    }
  )
```

`#img` 위에서 mouse button을 놓으면 drag가 종료됩니다.

---

# 44. Drag 종료 누락 가능성

현재 `mouseup` listener는 `#img`에만 등록되어 있습니다.

drag 중 pointer가 요소 밖으로 빠져나간 상태에서 mouse button을 놓으면 `#img`의 mouseup이 발생하지 않을 수 있습니다.

그러면 `_isDrag`가 true로 남을 가능성이 있습니다.

개선:

```js
document.addEventListener(
  "mouseup",
  function() {
    _isDrag = false
  }
)
```

또는 Pointer Events와 pointer capture를 사용할 수 있습니다.

---

# 45. Pointer Events 개선

mouse와 touch를 함께 다루려면:

```js
pointerdown
pointermove
pointerup
```

을 사용할 수 있습니다.

`setPointerCapture()`를 사용하면 pointer가 요소 밖으로 이동해도 drag 흐름을 더 안정적으로 유지할 수 있습니다.

원본은 mouse event 학습 범위이므로 mouse event를 그대로 사용합니다.

---

# 46. Drag Text 선택 문제

drag 중 document text가 선택될 수 있습니다.

개선:

```js
event.preventDefault()
```

를 `mousedown`에 적용하거나 CSS:

```css
#img {
  user-select: none;
}
```

을 사용할 수 있습니다.

현재 `#img`는 빈 div이므로 text 선택 문제는 작지만 원리가 중요합니다.

---

# 47. Img 요소 이름 혼동

HTML에는:

```html
<img id="game">
```

과:

```html
<div id="img">
```

가 함께 있습니다.

`#img`라는 id가 실제 `<img>` tag가 아니라 `<div>`입니다.

변수 이름도 `img`라서 혼동될 수 있습니다.

개선 이름:

```html
<div id="dragBox">
```

```js
const dragBox =
  document.querySelector(
    "#dragBox"
  )
```

---

# 48. 주석 처리된 내부 Img

내 HTML:

```html
<div id="img" class="area">
  <!--
  <img
    id="img"
    src="./asset/pngegg.png"
  >
  -->
</div>
```

주석 속 `<img id="img">`를 활성화하면 부모 div와 자식 img가 같은 id를 가지게 될 수 있습니다.

동일 id 중복은 잘못된 HTML 구조입니다.

강사님 원본에는 이 주석이 없습니다.

---

# 49. Resize Event

공통 원본:

```js
window.addEventListener(
  "resize",
  function() {
    const w =
      window.innerWidth

    const h =
      window.innerHeight
  }
)
```

browser viewport 크기가 바뀔 때 실행됩니다.

---

# 50. InnerWidth와 InnerHeight

```js
window.innerWidth
window.innerHeight
```

viewport 내부 크기를 CSS pixel 단위로 나타냅니다.

scrollbar 포함 여부는 browser 환경과 측정 방식에 따라 세부 차이가 있을 수 있습니다.

내 주석은 scrollbar 영역을 제외한 내부 크기라고 설명합니다.

일반적으로 viewport 내부 크기로 이해하는 것이 적절합니다.

---

# 51. OuterWidth와 OuterHeight

browser window 전체 외곽 크기:

```js
window.outerWidth
window.outerHeight
```

browser chrome 영역까지 포함할 수 있습니다.

원본은 “아우터”를 대안으로만 언급하고 실제 사용하지 않습니다.

---

# 52. Resize Log 차이

내 코드:

```text
화면w:1234, 높이h:800
```

강사님 코드:

```text
w:1234, h:800
```

출력 문구만 다릅니다.

---

# 53. Resize 성능 주의

resize event도 연속적으로 매우 자주 발생할 수 있습니다.

매 resize마다 새 log div를 만들면 DOM이 빠르게 증가할 수 있습니다.

mousemove와 마찬가지로 throttle 또는 기존 text 갱신 방식을 고려할 수 있습니다.

---

# 54. CSS 비교

양쪽 CSS 기능은 동일합니다.

내 코드:

```css
.area {
  width: 200px;
  height: 100px;
  border: 1px solid red;
}
```

강사님 코드:

```css
.area{
  width: 200px;
  height: 100px;
  border: 1px solid red;
}
```

spacing 차이만 있습니다.

---

# 55. External Image와 Alt

양쪽 원본:

```html
<img
  id="game"
  src="https://encrypted-tbn0..."
>
```

문제:

- 외부 URL 변경 가능
- network에 따라 load 실패
- hotlink 제한 가능
- `alt` 누락
- window load가 image 완료를 기다려 초기화 지연 가능

개선:

```html
<img
  id="game"
  src="./asset/game.png"
  alt="마우스를 따라 이동하는 게임 이미지"
>
```

---

# 56. My Code 분석

## 56.1 장점

- 전역 drag 상태 변수의 역할을 주석으로 설명했다.
- context menu의 용어와 차단 동작을 설명했다.
- selectstart로 text drag 선택을 막는다고 설명했다.
- copy event와 clipboard 저장 개념을 상세히 설명했다.
- `window.getSelection()`의 역할을 설명했다.
- mousedown, mouseup, click의 의미를 각각 기록했다.
- offset, page, client, screen 좌표를 자세히 설명했다.
- mousemove에서 X·Y 좌표를 template literal로 출력했다.
- game image를 pointer에서 10px 떨어뜨린 이유를 설명했다.
- drag offset을 전역 변수에 저장하는 이유를 설명했다.
- resize와 innerWidth·innerHeight를 설명했다.
- 강사님 코드보다 학습용 주석이 훨씬 풍부하다.

## 56.2 개선점

- `"moseover"` 출력 오타가 있다.
- mouseenter와 mouseover를 동일한 기능이라고 설명한 것은 부정확하다.
- double click을 항상 0.3초 이내라고 단정한다.
- client 좌표 설명에서 “서버에 접속할 수 있는 도구”라는 표현은 부정확하다.
- contextmenu와 selectstart를 `return false` 방식으로 막는다.
- 우클릭·선택 차단을 보안처럼 오해할 수 있다.
- copy 출처 앞에 공백이나 줄바꿈이 없다.
- 비교 연산에 `==`를 사용한다.
- log 함수가 `innerHTML`을 사용한다.
- mousemove마다 log DOM을 계속 생성한다.
- body에 mousemove listener가 두 개여서 매 이동마다 두 callback이 실행된다.
- drag 종료가 `#img` mouseup에만 의존한다.
- 방향을 잃고 mouseup하면 drag 상태가 남을 수 있다.
- `#img`가 div인데 이름이 image처럼 보여 혼동된다.
- 주석 속 img를 활성화하면 id가 중복될 수 있다.
- 외부 image에 alt가 없다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.

---

# 57. Teacher Code 분석

## 57.1 장점

- mouse event 종류를 짧고 순서 있게 실습한다.
- context menu와 text selection 차단을 구현한다.
- copy event에서 선택 text에 출처를 추가한다.
- mouse coordinate 네 종류를 비교한다.
- mouseover와 mouseout으로 배경색을 바꾼다.
- mousemove로 현재 offset을 출력한다.
- game image를 pointer에 따라 이동시킨다.
- offset을 이용한 drag and drop을 구현한다.
- resize에서 viewport 크기를 읽는다.
- 코드가 간결해 실행 흐름을 빠르게 볼 수 있다.

## 57.2 개선점

- `return false`와 `preventDefault()` 차이를 설명하지 않는다.
- 우클릭·선택 차단의 한계를 설명하지 않는다.
- mouseover와 mouseenter 차이를 설명하지 않는다.
- mousemove log 과다 문제를 설명하지 않는다.
- drag 종료가 요소 내부 mouseup에만 의존한다.
- pointer event나 touch 대응이 없다.
- log 함수가 innerHTML을 사용한다.
- `==`를 사용한다.
- 출처 text 앞 구분이 없다.
- 외부 image와 alt 누락 문제가 있다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.

---

# 58. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 전체 기능 | 동일 | 동일 |
| 주석 | 매우 상세 | 간결 |
| Area2 문구 | `덧붙이기` | `덛 붙이기` |
| Double Click log | `더블클릭발생` | `더블클릭 발생` |
| Mouseover log | `moseover` 오타 | `mouseover` 정상 |
| Offset log spacing | 공백 포함 | 공백 적음 |
| Mouse 좌표 설명 | line 주석으로 상세 | block 주석으로 요약 |
| Game 10px 이유 | 상세 설명 | 설명 없음 |
| Img 내부 주석 | 중복 id 가능 `<img>` 주석 있음 | 없음 |
| Resize log | `화면w`, `높이h` | `w`, `h` |
| 기능적 결과 | 거의 동일 | 거의 동일 |

---

# 59. 대표 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>마우스 이벤트</title>

  <script
    src="./main.js"
    defer
  ></script>

  <style>
    #dragBox {
      width: 100px;
      height: 100px;
      border: 1px solid;
      position: absolute;
      user-select: none;
      cursor: grab;
    }

    #dragBox.dragging {
      cursor: grabbing;
    }
  </style>
</head>
<body>
  <div id="copyArea">
    복사할 콘텐츠
  </div>

  <div id="dragBox"></div>

  <div id="view"></div>
</body>
</html>
```

```js
"use strict"

const copyArea =
  document.querySelector(
    "#copyArea"
  )

copyArea.addEventListener(
  "copy",
  function(event) {
    const selection =
      window
        .getSelection()
        .toString()

    if (
      selection.length === 0
    ) {
      return
    }

    event.preventDefault()

    const result =
      `${selection}\n\n` +
      "[출처] example.com"

    event.clipboardData.setData(
      "text/plain",
      result
    )
  }
)
```

---

# 60. 개선된 Drag 예제

```js
const dragBox =
  document.querySelector(
    "#dragBox"
  )

let isDragging = false
let offsetX = 0
let offsetY = 0

dragBox.addEventListener(
  "mousedown",
  function(event) {
    event.preventDefault()

    isDragging = true

    offsetX =
      event.offsetX

    offsetY =
      event.offsetY

    dragBox.classList.add(
      "dragging"
    )
  }
)

document.addEventListener(
  "mousemove",
  function(event) {
    if (!isDragging) {
      return
    }

    dragBox.style.left =
      `${event.pageX - offsetX}px`

    dragBox.style.top =
      `${event.pageY - offsetY}px`
  }
)

document.addEventListener(
  "mouseup",
  function() {
    isDragging = false

    dragBox.classList.remove(
      "dragging"
    )
  }
)
```

mouseup을 document에 등록해 요소 밖에서 button을 놓아도 drag를 종료합니다.

---

# 61. Pointer Event 확장 예제

```js
dragBox.addEventListener(
  "pointerdown",
  function(event) {
    dragBox.setPointerCapture(
      event.pointerId
    )
  }
)

dragBox.addEventListener(
  "pointerup",
  function(event) {
    dragBox.releasePointerCapture(
      event.pointerId
    )
  }
)
```

mouse뿐 아니라 touch, pen 입력까지 통합할 수 있습니다.

원본 학습 범위를 넘어서는 확장 내용입니다.

---

# 62. 자주 하는 실수

## 62.1 Contextmenu 차단을 보안 기능으로 생각

사용자가 source나 개발자 도구로 접근하는 것은 막지 못합니다.

## 62.2 Selection 뒤에 출처를 바로 연결

space나 줄바꿈이 없어 읽기 어렵습니다.

## 62.3 Mouseover와 Mouseenter를 완전히 같다고 생각

bubbling과 child 경계 처리 차이가 있습니다.

## 62.4 Mousemove마다 DOM Log 추가

성능과 memory 문제가 생길 수 있습니다.

## 62.5 ClientY를 Document 좌표로 생각

client는 viewport 기준입니다.

## 62.6 Pointer 바로 아래에 추적 Image 배치

image가 mouse event target을 가릴 수 있습니다.

## 62.7 Drag Offset을 저장하지 않음

요소 좌상단이 pointer로 순간 이동합니다.

## 62.8 Mouseup을 Drag 요소에만 등록

요소 밖에서 button을 놓으면 drag가 종료되지 않을 수 있습니다.

## 62.9 Div에 Img라는 ID 사용

tag와 역할이 혼동됩니다.

## 62.10 External Image에 Alt 누락

접근성과 재현성이 떨어집니다.

---

# 63. 면접·복습 포인트

## Q1. Contextmenu Event는 언제 발생하나요?

일반적으로 오른쪽 mouse button으로 context menu를 열 때 발생합니다.

## Q2. Copy Event에서 PreventDefault를 사용하는 이유는 무엇인가요?

기본 clipboard 복사를 막고 직접 구성한 text를 clipboard에 넣기 위해서입니다.

## Q3. OffsetY와 PageY의 차이는 무엇인가요?

offsetY는 event target 내부 기준이고 pageY는 전체 document 기준입니다.

## Q4. ClientY와 ScreenY의 차이는 무엇인가요?

clientY는 viewport 기준이고 screenY는 physical screen 기준입니다.

## Q5. Mouseover와 Mouseenter의 차이는 무엇인가요?

mouseover는 bubble하고 child 경계를 오갈 때 반복 발생할 수 있지만 mouseenter는 요소 경계 진입 중심이며 일반적으로 bubble하지 않습니다.

## Q6. Mousemove 사용 시 주의점은 무엇인가요?

매우 자주 발생하므로 무거운 DOM 작업이나 계속되는 node 생성을 피해야 합니다.

## Q7. Drag 시작 시 Offset을 저장하는 이유는 무엇인가요?

pointer가 잡은 내부 위치를 유지해 요소가 갑자기 좌상단 기준으로 이동하지 않도록 하기 위해서입니다.

## Q8. 내 코드의 Mouseover 관련 오타는 무엇인가요?

event type은 맞지만 log text가 `"moseover"`로 작성되어 있습니다.

## Q9. 현재 Drag 종료 구현의 문제는 무엇인가요?

mouseup이 `#img`에만 있어 요소 밖에서 button을 놓으면 drag 상태가 남을 수 있습니다.

## Q10. Resize에서 InnerWidth와 InnerHeight는 무엇을 나타내나요?

browser viewport의 내부 폭과 높이를 나타냅니다.

---

# Problems

## 문제 1. Contextmenu 차단

`#area`에서 context menu의 기본 동작을 막으세요.

## 문제 2. Text 선택 차단

JavaScript 또는 CSS로 `#area`의 text 선택을 막으세요.

## 문제 3. Selection 읽기

현재 선택된 text를 문자열로 출력하세요.

## 문제 4. Copy 출처 추가

복사한 text 뒤에 줄바꿈과 `[출처] example.com`을 붙이세요.

## 문제 5. Dblclick

`#area2`를 double click하면 log를 출력하세요.

## 문제 6. Mouse Event 순서

한 번 클릭할 때 mousedown, mouseup, click의 일반적인 순서를 작성하세요.

## 문제 7. Offset 좌표

click 위치의 offsetX와 offsetY를 출력하세요.

## 문제 8. Page 좌표

click 위치의 pageX와 pageY를 출력하세요.

## 문제 9. Client 좌표

click 위치의 clientX와 clientY를 출력하세요.

## 문제 10. Screen 좌표

click 위치의 screenX와 screenY를 출력하세요.

## 문제 11. Hover 색상

pointer가 들어오면 yellow, 나가면 white로 바꾸세요.

## 문제 12. Mouseenter 사용

mouseover 대신 mouseenter를 사용하고 차이를 설명하세요.

## 문제 13. Mouse 추적

image를 pointer보다 10px 오른쪽 아래에 이동시키세요.

## 문제 14. Pointer Events 방해 방지

추적 image가 mouse event target을 가리지 않도록 CSS를 작성하세요.

## 문제 15. Drag 시작

mousedown에서 drag 상태와 pointer 내부 offset을 저장하세요.

## 문제 16. Drag 이동

mousemove에서 page 좌표와 offset을 이용해 요소를 이동하세요.

## 문제 17. Drag 종료

요소 밖에서 mouseup해도 drag가 종료되도록 작성하세요.

## 문제 18. Resize

window resize 때 innerWidth와 innerHeight를 출력하세요.

## 문제 19. 안전한 Log

innerHTML 대신 textContent를 사용하세요.

## 문제 20. Mousemove 최적화

새 log node를 계속 만들지 않고 기존 좌표 표시 요소 하나만 갱신하세요.

## 문제 21. 원본 오류 찾기

내 코드의 mouseover log 오타와 drag 종료 문제를 설명하세요.

## 문제 22. 종합 Drag Component

다음 요구사항을 만족하세요.

- `#dragBox`를 drag
- pointer event 사용
- mouse, touch, pen 지원
- pointerdown에서 offset 계산
- pointer capture 사용
- pointermove에서 위치 이동
- pointerup 또는 pointercancel에서 종료
- text 선택 방지
- 위치는 page 기준
- XSS 없는 상태 log 출력

---

# Answers & Explanations

## 정답 1

```js
area.addEventListener(
  "contextmenu",
  function(event) {
    event.preventDefault()
  }
)
```

## 정답 2

JavaScript:

```js
area.addEventListener(
  "selectstart",
  function(event) {
    event.preventDefault()
  }
)
```

CSS:

```css
#area {
  user-select: none;
}
```

## 정답 3

```js
const selection =
  window
    .getSelection()
    .toString()

console.log(selection)
```

## 정답 4

```js
area2.addEventListener(
  "copy",
  function(event) {
    const selection =
      window
        .getSelection()
        .toString()

    if (
      selection.length === 0
    ) {
      return
    }

    event.preventDefault()

    const result =
      `${selection}\n\n` +
      "[출처] example.com"

    event.clipboardData.setData(
      "text/plain",
      result
    )
  }
)
```

## 정답 5

```js
area2.addEventListener(
  "dblclick",
  function() {
    log(
      "더블클릭 발생"
    )
  }
)
```

## 정답 6

```text
mousedown
mouseup
click
```

## 정답 7

```js
area2.addEventListener(
  "click",
  function(event) {
    console.log(
      event.offsetX,
      event.offsetY
    )
  }
)
```

## 정답 8

```js
console.log(
  event.pageX,
  event.pageY
)
```

## 정답 9

```js
console.log(
  event.clientX,
  event.clientY
)
```

## 정답 10

```js
console.log(
  event.screenX,
  event.screenY
)
```

## 정답 11

```js
area2.addEventListener(
  "mouseenter",
  function() {
    area2.style
      .backgroundColor =
      "yellow"
  }
)

area2.addEventListener(
  "mouseleave",
  function() {
    area2.style
      .backgroundColor =
      "white"
  }
)
```

## 정답 12

```js
area2.addEventListener(
  "mouseenter",
  function() {
    console.log(
      "진입"
    )
  }
)
```

mouseenter는 child 경계 이동에 의한 반복 발생이 적고 일반적으로 bubble하지 않습니다.

## 정답 13

```js
document.addEventListener(
  "mousemove",
  function(event) {
    game.style.left =
      `${event.pageX + 10}px`

    game.style.top =
      `${event.pageY + 10}px`
  }
)
```

## 정답 14

```css
#game {
  pointer-events: none;
}
```

## 정답 15

```js
dragBox.addEventListener(
  "mousedown",
  function(event) {
    isDragging = true

    offsetX =
      event.offsetX

    offsetY =
      event.offsetY
  }
)
```

## 정답 16

```js
document.addEventListener(
  "mousemove",
  function(event) {
    if (!isDragging) {
      return
    }

    dragBox.style.left =
      `${event.pageX - offsetX}px`

    dragBox.style.top =
      `${event.pageY - offsetY}px`
  }
)
```

## 정답 17

```js
document.addEventListener(
  "mouseup",
  function() {
    isDragging = false
  }
)
```

## 정답 18

```js
window.addEventListener(
  "resize",
  function() {
    console.log(
      window.innerWidth,
      window.innerHeight
    )
  }
)
```

## 정답 19

```js
div.textContent =
  message
```

## 정답 20

HTML:

```html
<div id="coordinates"></div>
```

JavaScript:

```js
const coordinates =
  document.querySelector(
    "#coordinates"
  )

area2.addEventListener(
  "mousemove",
  function(event) {
    coordinates.textContent =
      `x:${event.offsetX}, ` +
      `y:${event.offsetY}`
  }
)
```

## 정답 21

내 event type은 `"mouseover"`로 올바르지만 log 문자열이 `"moseover"`로 오타입니다. 또한 mouseup listener가 drag 요소에만 있어 요소 밖에서 button을 놓으면 `_isDrag`가 true로 남을 수 있습니다.

## 정답 22

```js
const dragBox =
  document.querySelector(
    "#dragBox"
  )

const status =
  document.querySelector(
    "#status"
  )

let dragging = false
let offsetX = 0
let offsetY = 0

function setStatus(message) {
  status.textContent =
    message
}

dragBox.addEventListener(
  "pointerdown",
  function(event) {
    event.preventDefault()

    dragging = true

    const rect =
      dragBox
        .getBoundingClientRect()

    offsetX =
      event.clientX -
      rect.left

    offsetY =
      event.clientY -
      rect.top

    dragBox.setPointerCapture(
      event.pointerId
    )

    setStatus(
      "drag 시작"
    )
  }
)

dragBox.addEventListener(
  "pointermove",
  function(event) {
    if (!dragging) {
      return
    }

    const pageX =
      event.clientX +
      window.scrollX

    const pageY =
      event.clientY +
      window.scrollY

    dragBox.style.left =
      `${pageX - offsetX}px`

    dragBox.style.top =
      `${pageY - offsetY}px`
  }
)

function stopDrag(event) {
  if (!dragging) {
    return
  }

  dragging = false

  if (
    dragBox.hasPointerCapture(
      event.pointerId
    )
  ) {
    dragBox.releasePointerCapture(
      event.pointerId
    )
  }

  setStatus(
    "drag 종료"
  )
}

dragBox.addEventListener(
  "pointerup",
  stopDrag
)

dragBox.addEventListener(
  "pointercancel",
  stopDrag
)
```

CSS:

```css
#dragBox {
  position: absolute;
  user-select: none;
  touch-action: none;
}
```

---

# Final Checklist

## 초기화와 구조

- [ ] head script와 window load 실행 관계를 이해했다.
- [ ] 외부 image가 load 시점을 늦출 수 있음을 이해했다.
- [ ] 전역 drag 상태 변수의 역할을 이해했다.
- [ ] underscore가 convention임을 이해했다.
- [ ] `#game`과 `#img`의 역할을 구분했다.

## Context와 Copy

- [ ] contextmenu event를 이해했다.
- [ ] preventDefault로 기본 menu를 차단했다.
- [ ] 우클릭 차단이 보안 기능이 아님을 이해했다.
- [ ] selectstart와 user-select를 비교했다.
- [ ] copy event에서 selection을 읽었다.
- [ ] 빈 selection을 처리했다.
- [ ] clipboardData에 text/plain을 설정했다.
- [ ] 출처 text에 적절한 구분을 넣었다.

## Mouse Event

- [ ] dblclick, mousedown, mouseup, click을 구분했다.
- [ ] double-click 시간을 고정값으로 단정하지 않았다.
- [ ] offset, page, client, screen 좌표를 구분했다.
- [ ] mouseover와 mouseenter 차이를 이해했다.
- [ ] 내 `"moseover"` 오타를 확인했다.
- [ ] mousemove의 높은 발생 빈도를 이해했다.
- [ ] 반복적인 DOM log 생성을 피했다.

## Mouse 추적과 Drag

- [ ] pointer에서 image를 약간 떨어뜨린 이유를 이해했다.
- [ ] `pointer-events: none` 대안을 이해했다.
- [ ] drag 시작 때 내부 offset을 저장했다.
- [ ] page 좌표에서 offset을 빼 위치를 계산했다.
- [ ] document mouseup으로 drag 종료를 보장했다.
- [ ] Pointer Events 확장을 이해했다.
- [ ] text selection 방지를 검토했다.
- [ ] 요소 id와 역할이 혼동되지 않도록 이름을 정했다.

## Resize와 안전성

- [ ] innerWidth와 innerHeight를 이해했다.
- [ ] outerWidth와 outerHeight 차이를 이해했다.
- [ ] resize event의 높은 발생 빈도를 고려했다.
- [ ] log에 innerHTML 대신 textContent를 사용했다.
- [ ] 외부 image 의존성을 검토했다.
- [ ] image에 alt를 제공했다.

## 원본 코드 검수

- [ ] 두 실제 16_event_mouse.html을 비교했다.
- [ ] 연결된 두 실제 16_event_mouse.js를 비교했다.
- [ ] area2 문구 차이를 기록했다.
- [ ] double click log 공백 차이를 기록했다.
- [ ] 내 mouseover log 오타를 기록했다.
- [ ] 좌표 log formatting 차이를 기록했다.
- [ ] resize log 문구 차이를 기록했다.
- [ ] 내 HTML의 주석 처리된 img와 id 중복 가능성을 기록했다.
- [ ] drag mouseup 범위 문제를 기록했다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 16번은 mouse, copy, drag, resize event를 다룬다.
- script는 head에 있지만 `window.onload` 이후 `bind()`를 실행해 body DOM을 선택한다.
- window load는 외부 image 같은 resource load까지 기다릴 수 있다.
- `_isDrag`, `_offsetX`, `_offsetY`는 drag 상태와 pointer 내부 위치를 저장한다.
- underscore는 private 기능이 아니라 naming convention이다.
- `contextmenu`는 우클릭 menu가 열릴 때 발생한다.
- `return false`로 context menu를 막을 수 있지만 `preventDefault()`가 더 명시적이다.
- 우클릭과 text 선택 차단은 실제 콘텐츠 보안 수단이 아니다.
- `selectstart` 또는 CSS `user-select: none`으로 text 선택을 막을 수 있다.
- copy event에서 `window.getSelection().toString()`으로 선택 text를 읽는다.
- `event.clipboardData.setData("text/plain", result)`로 복사 text를 바꾼다.
- 원본은 선택 text와 출처 사이에 space나 줄바꿈이 없다.
- 내 HTML의 `"덧붙이기"`와 강사님 `"덛 붙이기"`는 text 차이다.
- dblclick 판정 시간은 항상 정확히 0.3초라고 단정할 수 없다.
- 일반적인 한 번 click 순서는 mousedown, mouseup, click이다.
- offset 좌표는 target 내부, page는 document, client는 viewport, screen은 physical screen 기준이다.
- 내 client 설명의 서버 관련 표현은 부정확하다.
- mouseover와 mouseenter는 비슷해 보여도 bubbling과 child 경계 처리에서 다르다.
- 내 실제 event type은 맞지만 log 문자열 `"moseover"`는 오타다.
- mousemove는 매우 자주 발생하므로 매번 log node를 생성하면 성능 문제가 생길 수 있다.
- game image는 body mousemove에서 pageX·pageY보다 10px 떨어진 위치로 이동한다.
- `pointer-events: none`으로 추적 image가 mouse target을 가리는 것을 막을 수 있다.
- body에는 game 추적과 drag 이동을 위한 mousemove listener가 각각 하나씩 등록되어 있다.
- drag 시작 때 offsetX·offsetY를 저장해야 pointer가 잡은 위치를 유지할 수 있다.
- drag 위치는 `pageX - offsetX`, `pageY - offsetY`로 계산한다.
- 현재 mouseup은 `#img`에만 있어 요소 밖에서 놓으면 drag가 종료되지 않을 수 있다.
- document mouseup 또는 pointer capture가 더 안정적이다.
- `#img`는 실제 img tag가 아니라 div이므로 이름이 혼동될 수 있다.
- 내 HTML의 주석 속 img를 활성화하면 id 중복 가능성이 있다.
- resize event에서 innerWidth와 innerHeight로 viewport 크기를 읽는다.
- 내 resize log는 `"화면w"`, `"높이h"`이고 강사님은 `"w"`, `"h"`다.
- 양쪽 log 함수는 innerHTML을 사용하므로 기본적으로 textContent가 더 안전하다.
- 외부 image URL과 alt 누락은 재현성과 접근성 문제를 만든다.
