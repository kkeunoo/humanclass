---
title: JavaScript 마우스 이벤트와 드래그·복사 제어
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript 마우스 이벤트와 드래그·복사 제어

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `16_JavaScript_마우스이벤트와_드래그복사제어.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/16_event_mouse.html`, `workspace_html/javascript/asset/js/16_event_mouse.js`, 강사님 동일 파일 |
| 핵심 범위 | `contextmenu`, `selectstart`, `copy`, Mouse Event, 좌표계, Hover, `mousemove`, Drag, `resize`, Pointer Event |
| 실습 범위 | 우클릭·선택 제어, 복사 출처 추가, 좌표 출력, 커서 추적 이미지, Drag Box, Viewport 크기 표시 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 16번은 HTML과 실제 연결된 외부 JavaScript 파일을 함께 확인한다.  
> 마우스 이벤트의 발생 순서와 좌표계를 이해하고, 복사 제어·커서 추적·직접 Drag 기능을 안전하고 현대적인 방식으로 개선한다.

---

# 개요

마우스 이벤트는 Pointer가 요소 위로 이동하거나 버튼을 누르고 놓을 때 발생한다.

```text
Pointer가 요소 위로 이동
    ↓
Mouse Event 발생
    ↓
Event 객체에 좌표와 버튼 정보 저장
    ↓
등록된 Listener 실행
    ↓
화면 상태 변경
```

대표 이벤트:

| 분류 | 이벤트 |
| --- | --- |
| 메뉴·선택 | `contextmenu`, `selectstart`, `copy` |
| 버튼 | `mousedown`, `mouseup`, `click`, `dblclick` |
| 진입·이탈 | `mouseover`, `mouseout`, `mouseenter`, `mouseleave` |
| 이동 | `mousemove` |
| 화면 | `resize` |
| 통합 입력 | `pointerdown`, `pointermove`, `pointerup` |

> [!IMPORTANT]
> 마우스 이벤트를 사용할 때는 **이벤트 발생 빈도**, **좌표 기준**, **기본 브라우저 동작**, **요소 밖으로 Pointer가 이동했을 때의 종료 처리**를 함께 확인해야 한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `preventDefault()` | 우클릭 메뉴·복사·선택 등 기본 동작 취소 |
| `window.getSelection()` | 현재 선택된 텍스트 조회 |
| `clipboardData` | Copy Event의 Clipboard 데이터 변경 |
| `offsetX`, `offsetY` | Event Target 내부 좌표 |
| `pageX`, `pageY` | 전체 문서 좌표 |
| `clientX`, `clientY` | 현재 Viewport 좌표 |
| `screenX`, `screenY` | 실제 화면 좌표 |
| Drag Offset | 요소를 누른 내부 위치 |
| `pointer-events` | 요소가 Pointer Target이 되는 방식 제어 |
| Pointer Capture | 요소 밖으로 이동해도 Pointer 흐름 유지 |
| `innerWidth`, `innerHeight` | 현재 Viewport 내부 크기 |
| `requestAnimationFrame()` | 화면 갱신 주기에 맞춘 이벤트 처리 |

---

# 학습 목표

- `contextmenu` 이벤트를 이해하고 기본 동작을 취소할 수 있다.
- 우클릭 차단이 보안 기능이 아님을 설명할 수 있다.
- `selectstart`와 CSS `user-select`를 사용할 수 있다.
- Copy Event에서 선택 텍스트를 읽을 수 있다.
- 복사 텍스트에 출처를 추가할 수 있다.
- `mousedown`, `mouseup`, `click`, `dblclick`을 구분할 수 있다.
- 네 가지 마우스 좌표계를 설명할 수 있다.
- `mouseover`와 `mouseenter`의 차이를 이해한다.
- 빈번한 `mousemove`에서 DOM 생성을 최소화할 수 있다.
- 커서 추적 요소가 Event Target을 가리지 않도록 설정할 수 있다.
- Drag 시작 시 Pointer Offset을 저장할 수 있다.
- Drag 중 요소의 새 위치를 계산할 수 있다.
- 요소 밖에서 버튼을 놓아도 Drag를 종료할 수 있다.
- Pointer Event와 Pointer Capture를 사용할 수 있다.
- `resize`에서 Viewport 크기를 읽을 수 있다.
- `innerHTML` 대신 안전한 텍스트 출력을 사용할 수 있다.

---

# 1. 원본 HTML 구조

```html
<div id="area" class="area">
    선택을 막을 글씨
</div>

<div id="area2" class="area">
    복사할 때 출처를 덧붙일 글씨
</div>

<img
    id="game"
    src="./asset/game.png"
    alt="마우스를 따라 이동하는 이미지"
>

<div
    id="drag-box"
    class="area"
></div>

<div id="view"></div>
```

---

# 2. 요소별 역할

```text
#area
→ 우클릭·텍스트 선택 제어

#area2
→ 복사·마우스 이벤트 실습

#game
→ Pointer 위치 추적

#drag-box
→ 직접 Drag하는 요소

#view
→ 이벤트 로그 출력
```

---

# 3. Script 실행 시점

원본은 `<head>`에서 외부 JavaScript를 연결하고 `window.onload` 후 이벤트를 등록한다.

```javascript
window.onload = () => {
    bindEvents()
}
```

이미지 등 외부 자원의 로드까지 기다린다.

---

# 4. `defer` 개선

```html
<script
    src="./asset/js/16_event_mouse.js"
    defer
></script>
```

```javascript
bindEvents()
```

DOM 요소만 필요하다면 `defer`로 충분한 경우가 많다.

외부 이미지 로드 지연 때문에 초기화가 늦어지는 문제도 줄일 수 있다.

---

# 5. Drag 상태 변수

원본:

```javascript
let _isDrag = false
let _offsetX = 0
let _offsetY = 0
```

개선된 이름:

```javascript
let isDragging = false
let dragOffsetX = 0
let dragOffsetY = 0
```

Underscore는 Naming Convention일 뿐 접근 제한 기능이 아니다.

---

# 6. 안전한 Log 함수

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

---

# 7. 원본 Log의 문제

원본:

```javascript
item.innerHTML = message
```

사용자 입력이나 외부 문자열이 전달되면 HTML Injection 또는 XSS 위험이 생길 수 있다.

일반 로그에는 `textContent`를 사용한다.

---

# 8. `contextmenu`

```javascript
area.addEventListener(
    "contextmenu",
    event => {
        event.preventDefault()

        console.log(
            "Context Menu 차단",
        )
    },
)
```

오른쪽 버튼 등으로 Context Menu를 열 때 발생한다.

---

# 9. `return false`와 `preventDefault()`

원본 Property 방식:

```javascript
area.oncontextmenu = () => {
    return false
}
```

개선:

```javascript
area.addEventListener(
    "contextmenu",
    event => {
        event.preventDefault()
    },
)
```

`preventDefault()`는 어떤 기본 동작을 막는지 의도가 명확하다.

---

# 10. 우클릭 차단의 한계

우클릭 메뉴를 막아도 다음 접근을 막을 수 없다.

- 개발자 도구
- Page Source
- Network 요청
- JavaScript 비활성화
- 키보드 단축키
- Screenshot

> [!WARNING]
> 우클릭 차단을 콘텐츠 보안 기능으로 사용하지 않는다.

---

# 11. `selectstart`

```javascript
area.addEventListener(
    "selectstart",
    event => {
        event.preventDefault()
    },
)
```

텍스트 선택이 시작될 때 발생한다.

---

# 12. CSS `user-select`

```css
#area {
    user-select: none;
}
```

단순 텍스트 선택 제한은 CSS가 더 간결할 수 있다.

접근성과 사용자 경험을 고려해 꼭 필요한 영역에만 사용한다.

---

# 13. Copy Event

```javascript
copyArea.addEventListener(
    "copy",
    event => {
        console.log(
            "복사 이벤트",
        )
    },
)
```

키보드 단축키뿐 아니라 Context Menu 복사 등에서도 발생할 수 있다.

---

# 14. 현재 선택 텍스트

```javascript
const selection = (
    window
        .getSelection()
        ?.toString()
    ?? ""
)
```

선택된 텍스트가 없다면 빈 문자열이다.

---

# 15. 빈 선택 검사

```javascript
if (
    selection.length
    === 0
) {
    return
}
```

느슨한 비교 대신 엄격 비교를 사용한다.

---

# 16. 복사 텍스트에 출처 추가

```javascript
const copiedText = (
    `${selection}\n\n`
    + "[출처] example.com"
)
```

줄바꿈을 넣어 원문과 출처를 구분한다.

---

# 17. Clipboard 데이터 변경

```javascript
copyArea.addEventListener(
    "copy",
    event => {
        const selection = (
            window
                .getSelection()
                ?.toString()
            ?? ""
        )

        if (
            selection.length
            === 0
        ) {
            return
        }

        event.preventDefault()

        event.clipboardData?.setData(
            "text/plain",
            `${selection}\n\n`
            + "[출처] example.com",
        )
    },
)
```

---

# 18. `text/plain`

```text
text/plain
→ HTML 태그를 실행하지 않는 일반 텍스트 MIME Type
```

복사 결과를 HTML이 아닌 일반 문자열로 설정한다.

---

# 19. Clipboard API

```javascript
await navigator.clipboard.writeText(
    "복사할 문자열",
)
```

현대 API이지만 다음 조건의 영향을 받을 수 있다.

- HTTPS 등 Secure Context
- 사용자 Gesture
- Browser Permission
- Browser 지원 범위

Copy Event 자체를 변경할 때는 `event.clipboardData` 방식이 적합하다.

---

# 20. `mousedown`

```javascript
area2.addEventListener(
    "mousedown",
    () => {
        log("mousedown")
    },
)
```

마우스 버튼을 누르는 순간 발생한다.

---

# 21. `mouseup`

```javascript
area2.addEventListener(
    "mouseup",
    () => {
        log("mouseup")
    },
)
```

눌렀던 마우스 버튼을 놓는 순간 발생한다.

---

# 22. `click`

```javascript
area2.addEventListener(
    "click",
    () => {
        log("click")
    },
)
```

일반적으로 같은 요소에서 `mousedown`과 `mouseup`이 완료된 뒤 발생한다.

---

# 23. 기본 클릭 순서

```text
mousedown
→ mouseup
→ click
```

Pointer 이동과 Target 변경에 따라 실제 세부 순서는 달라질 수 있다.

---

# 24. `dblclick`

```javascript
area2.addEventListener(
    "dblclick",
    () => {
        log(
            "더블클릭 발생",
        )
    },
)
```

두 번의 클릭이 Double Click으로 판정되면 발생한다.

---

# 25. Double Click 시간

원본의 “0.3초 이내”라는 설명은 고정 기준이 아니다.

Double Click 판정 간격은 다음 영향을 받을 수 있다.

- 운영체제 설정
- 접근성 설정
- Browser
- 사용자 입력 속도

---

# 26. Mouse Event 객체

```javascript
area2.addEventListener(
    "click",
    event => {
        console.log(event)
    },
)
```

좌표·버튼·Target·Modifier Key 등의 정보가 포함된다.

---

# 27. `offsetX`, `offsetY`

```javascript
console.log(
    event.offsetX,
    event.offsetY,
)
```

Event Target 내부를 기준으로 한 좌표다.

자식 요소가 Target이 되면 기준 요소가 달라질 수 있다.

---

# 28. `pageX`, `pageY`

```javascript
console.log(
    event.pageX,
    event.pageY,
)
```

문서 전체 좌상단 기준 좌표다.

Scroll된 거리도 포함한다.

---

# 29. `clientX`, `clientY`

```javascript
console.log(
    event.clientX,
    event.clientY,
)
```

현재 Browser Viewport 좌상단 기준 좌표다.

여기서 Client는 서버 접속 도구가 아니라 Viewport Coordinate를 의미한다.

---

# 30. `screenX`, `screenY`

```javascript
console.log(
    event.screenX,
    event.screenY,
)
```

사용자의 실제 Screen 좌상단 기준 좌표다.

Browser Window의 위치에 따라 달라진다.

---

# 31. 좌표계 비교

| Property | 기준 |
| --- | --- |
| `offsetX`, `offsetY` | Event Target 내부 |
| `pageX`, `pageY` | 전체 Document |
| `clientX`, `clientY` | 현재 Viewport |
| `screenX`, `screenY` | 실제 Screen |

---

# 32. 좌표 출력 함수

```javascript
function getMousePosition(
    event,
) {
    return {
        offset: {
            x: event.offsetX,
            y: event.offsetY,
        },
        page: {
            x: event.pageX,
            y: event.pageY,
        },
        client: {
            x: event.clientX,
            y: event.clientY,
        },
        screen: {
            x: event.screenX,
            y: event.screenY,
        },
    }
}
```

---

# 33. `mouseover`

```javascript
area2.addEventListener(
    "mouseover",
    () => {
        area2.style.backgroundColor = (
            "yellow"
        )
    },
)
```

Pointer가 요소 또는 자식 요소 경계로 들어올 때 발생할 수 있다.

---

# 34. 원본 오타

내 원본의 Event Type은 올바르다.

```javascript
"mouseover"
```

하지만 Log 문자열은 다음처럼 잘못 작성되어 있다.

```text
moseover
```

출력 오타만 있으며 이벤트 자체는 정상 등록된다.

---

# 35. `mouseout`

```javascript
area2.addEventListener(
    "mouseout",
    () => {
        area2.style.backgroundColor = (
            "white"
        )
    },
)
```

Pointer가 요소 또는 자식 요소 경계를 벗어날 때 발생할 수 있다.

---

# 36. `mouseenter`, `mouseleave`

```javascript
area2.addEventListener(
    "mouseenter",
    () => {
        area2.classList.add(
            "is-hovered",
        )
    },
)

area2.addEventListener(
    "mouseleave",
    () => {
        area2.classList.remove(
            "is-hovered",
        )
    },
)
```

---

# 37. Hover 이벤트 차이

```text
mouseover / mouseout
→ Bubbling
→ 자식 요소 경계를 오갈 때도 반복 가능

mouseenter / mouseleave
→ 일반적으로 Bubbling하지 않음
→ 요소 전체 경계 진입·이탈 중심
```

완전히 동일한 이벤트가 아니다.

---

# 38. CSS Hover 대안

```css
.area:hover {
    background: yellow;
}
```

단순 시각 효과라면 JavaScript 이벤트보다 CSS `:hover`가 더 적합하다.

---

# 39. `mousemove`

```javascript
area2.addEventListener(
    "mousemove",
    event => {
        coordinates.textContent = (
            `x: ${event.offsetX}, `
            + `y: ${event.offsetY}`
        )
    },
)
```

Pointer가 움직일 때 매우 자주 발생한다.

---

# 40. 원본 Mousemove Log 문제

원본은 Mousemove 한 번마다 Log Node를 여러 개 생성한다.

문제:

- DOM Node 빠른 증가
- Memory 사용 증가
- 화면 렌더링 부담
- 로그 탐색 어려움
- UI 반응 저하

기존 표시 요소 하나만 갱신한다.

---

# 41. `requestAnimationFrame()`

```javascript
let pendingEvent = null
let isScheduled = false

area2.addEventListener(
    "mousemove",
    event => {
        pendingEvent = event

        if (isScheduled) {
            return
        }

        isScheduled = true

        requestAnimationFrame(
            () => {
                coordinates.textContent = (
                    `x: ${pendingEvent.offsetX}, `
                    + `y: ${pendingEvent.offsetY}`
                )

                isScheduled = false
            },
        )
    },
)
```

화면 갱신 주기에 맞춰 처리 횟수를 제한한다.

---

# 42. 커서 추적 이미지

```javascript
document.addEventListener(
    "mousemove",
    event => {
        game.style.left = (
            `${event.pageX + 10}px`
        )

        game.style.top = (
            `${event.pageY + 10}px`
        )
    },
)
```

이미지를 Pointer보다 오른쪽 아래로 10px 떨어뜨린다.

---

# 43. 10px Offset 이유

Pointer 바로 아래에 이미지가 있으면 이미지가 새로운 Event Target이 되어 움직임을 방해할 수 있다.

Offset을 추가해 Pointer와 요소를 분리한다.

---

# 44. `pointer-events: none`

```css
#game {
    pointer-events: none;
}
```

추적 이미지가 마우스 이벤트를 가로채지 않는다.

이 설정을 사용하면 반드시 10px 떨어뜨리지 않아도 Event Target 방해를 줄일 수 있다.

---

# 45. `position: absolute`

```css
#game {
    position: absolute;
}
```

문서 좌표 기반 `pageX`, `pageY`와 연결하기 쉽다.

Fixed 요소라면 `clientX`, `clientY`가 더 자연스러울 수 있다.

---

# 46. Mousemove Listener 통합

원본은 Body에 Mousemove Listener를 두 개 등록한다.

```text
첫 번째
→ 추적 이미지 이동

두 번째
→ Drag Box 이동
```

두 Listener 모두 실행된다.

역할 분리는 가능하지만 공통 계산이나 성능이 중요하면 하나로 통합할 수 있다.

---

# 47. Drag 시작

```javascript
dragBox.addEventListener(
    "mousedown",
    event => {
        event.preventDefault()

        isDragging = true
        dragOffsetX = event.offsetX
        dragOffsetY = event.offsetY
    },
)
```

---

# 48. Drag Offset 저장 이유

요소 중앙을 눌렀는데 Pointer 좌표를 그대로 `left`, `top`으로 사용하면 요소의 좌상단이 Pointer 위치로 순간 이동한다.

```text
새 Left
= Pointer PageX - 누른 내부 OffsetX

새 Top
= Pointer PageY - 누른 내부 OffsetY
```

---

# 49. Drag 중 이동

```javascript
document.addEventListener(
    "mousemove",
    event => {
        if (!isDragging) {
            return
        }

        dragBox.style.left = (
            `${event.pageX - dragOffsetX}px`
        )

        dragBox.style.top = (
            `${event.pageY - dragOffsetY}px`
        )
    },
)
```

---

# 50. 원본 Drag 종료

원본은 Drag 요소 자체에 `mouseup`을 등록한다.

```javascript
dragBox.addEventListener(
    "mouseup",
    () => {
        isDragging = false
    },
)
```

---

# 51. 요소 밖 Mouseup 문제

Drag 중 Pointer가 요소 밖으로 나간 뒤 버튼을 놓으면 요소의 `mouseup`이 발생하지 않을 수 있다.

`isDragging`이 계속 `true`로 남을 가능성이 있다.

---

# 52. Document에서 Drag 종료

```javascript
document.addEventListener(
    "mouseup",
    () => {
        isDragging = false
    },
)
```

요소 밖에서 버튼을 놓아도 Drag 상태를 종료한다.

---

# 53. Window Blur 처리

```javascript
window.addEventListener(
    "blur",
    () => {
        isDragging = false
    },
)
```

Drag 중 Browser Window가 Focus를 잃는 경우도 상태를 정리할 수 있다.

---

# 54. Drag 상태 클래스

```javascript
dragBox.classList.add(
    "is-dragging",
)
```

```javascript
dragBox.classList.remove(
    "is-dragging",
)
```

CSS:

```css
#drag-box {
    cursor: grab;
    user-select: none;
}

#drag-box.is-dragging {
    cursor: grabbing;
}
```

---

# 55. 이름 개선

원본에는 실제 `<img>`가 아닌 `<div id="img">`가 있다.

역할이 명확한 이름으로 변경한다.

```html
<div id="drag-box"></div>
```

```javascript
const dragBox = (
    document.querySelector(
        "#drag-box",
    )
)
```

---

# 56. 중복 ID 가능성

내 원본의 주석 처리된 내부 이미지까지 활성화하면 부모와 자식에 같은 `id="img"`가 생길 수 있다.

`id`는 문서에서 고유해야 한다.

---

# 57. Pointer Event

Mouse·Touch·Pen을 함께 지원하려면 Pointer Event를 사용할 수 있다.

```javascript
dragBox.addEventListener(
    "pointerdown",
    event => {
        // Drag 시작
    },
)
```

---

# 58. Pointer Capture

```javascript
dragBox.setPointerCapture(
    event.pointerId,
)
```

Pointer가 요소 밖으로 이동해도 해당 요소가 Pointer Event를 계속 받을 수 있다.

---

# 59. Pointer Drag 시작

```javascript
dragBox.addEventListener(
    "pointerdown",
    event => {
        event.preventDefault()

        const rect = (
            dragBox
                .getBoundingClientRect()
        )

        dragOffsetX = (
            event.clientX
            - rect.left
        )

        dragOffsetY = (
            event.clientY
            - rect.top
        )

        isDragging = true

        dragBox.setPointerCapture(
            event.pointerId,
        )
    },
)
```

---

# 60. Pointer Drag 이동

```javascript
dragBox.addEventListener(
    "pointermove",
    event => {
        if (!isDragging) {
            return
        }

        const left = (
            event.clientX
            - dragOffsetX
            + window.scrollX
        )

        const top = (
            event.clientY
            - dragOffsetY
            + window.scrollY
        )

        dragBox.style.left = (
            `${left}px`
        )

        dragBox.style.top = (
            `${top}px`
        )
    },
)
```

---

# 61. Pointer Drag 종료

```javascript
function stopDragging(
    event,
) {
    isDragging = false

    if (
        dragBox.hasPointerCapture(
            event.pointerId,
        )
    ) {
        dragBox.releasePointerCapture(
            event.pointerId,
        )
    }
}

dragBox.addEventListener(
    "pointerup",
    stopDragging,
)

dragBox.addEventListener(
    "pointercancel",
    stopDragging,
)
```

---

# 62. `resize`

```javascript
window.addEventListener(
    "resize",
    () => {
        console.log(
            window.innerWidth,
            window.innerHeight,
        )
    },
)
```

Browser Viewport 크기가 변경될 때 발생한다.

---

# 63. `innerWidth`, `innerHeight`

```text
window.innerWidth
→ Viewport 내부 너비

window.innerHeight
→ Viewport 내부 높이
```

CSS Pixel 단위다.

---

# 64. `outerWidth`, `outerHeight`

```javascript
window.outerWidth
window.outerHeight
```

Browser Chrome 영역 등을 포함한 Window 전체 외곽 크기다.

---

# 65. Resize 성능

Resize 이벤트도 연속으로 매우 자주 발생할 수 있다.

새 Log Node를 계속 만들기보다 하나의 상태 표시 요소를 갱신한다.

```javascript
viewportSize.textContent = (
    `${window.innerWidth}`
    + ` × ${window.innerHeight}`
)
```

---

# 66. Resize 최적화

```javascript
let resizeFrameId = null

window.addEventListener(
    "resize",
    () => {
        if (
            resizeFrameId
            !== null
        ) {
            cancelAnimationFrame(
                resizeFrameId,
            )
        }

        resizeFrameId = (
            requestAnimationFrame(
                () => {
                    viewportSize.textContent = (
                        `${window.innerWidth}`
                        + ` × `
                        + `${window.innerHeight}`
                    )

                    resizeFrameId = null
                },
            )
        )
    },
)
```

---

# 67. 외부 이미지와 `alt`

원본은 외부 검색 이미지 URL을 사용하고 `alt`가 없다.

개선:

```html
<img
    id="game"
    src="./asset/game.png"
    alt="마우스를 따라 이동하는 캐릭터"
>
```

로컬 Asset은 재현성이 높고, `alt`는 접근성을 개선한다.

---

# 68. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 전체 기능 | 거의 동일 | 거의 동일 |
| 주석 | 매우 상세 | 핵심 중심 |
| 복사 영역 문구 | `덧붙이기` | `덛 붙이기` |
| Double Click Log | 공백 없음 | 공백 있음 |
| Mouseover Log | `moseover` 오타 | 정상 |
| 좌표 Log | 공백 포함 | 간결 |
| 추적 이미지 Offset 설명 | 상세 | 없음 |
| 내부 주석 이미지 | 중복 ID 가능 | 없음 |
| Resize 문구 | 설명형 | 축약형 |

## 68-1. 내 코드의 장점

- Mouse Event와 좌표계 설명이 자세하다.
- 추적 이미지에 10px Offset을 주는 이유를 기록했다.
- Drag Offset 저장 원리를 설명했다.
- Clipboard와 Resize 개념을 강사님보다 자세히 정리했다.
- 실습 코드의 실행 이유를 주석으로 남겼다.

## 68-2. 내 코드의 개선점

- `"moseover"` Log 오타가 있다.
- `mouseover`와 `mouseenter`를 동일하게 설명했다.
- Double Click 시간을 0.3초로 단정했다.
- Client 좌표 설명이 부정확하다.
- `return false`와 느슨한 비교를 사용한다.
- Mousemove마다 Log Node를 생성한다.
- Drag 종료가 요소 내부 Mouseup에만 의존한다.
- `#img` 이름과 중복 ID 가능성이 있다.
- 외부 이미지와 `alt` 누락 문제가 있다.

## 68-3. 강사님 코드의 장점

- Mouse Event 종류와 좌표계를 간결하게 실습한다.
- Copy Event에서 출처 추가를 구현한다.
- 추적 이미지와 직접 Drag 기능을 연결한다.
- Resize에서 Viewport 크기를 읽는다.
- 전체 실행 흐름이 짧고 명확하다.

## 68-4. 강사님 코드의 보충점

- 우클릭·선택 차단의 한계를 설명해야 한다.
- `mouseover`와 `mouseenter` 차이가 필요하다.
- Mousemove 성능 문제를 설명해야 한다.
- 요소 밖 Mouseup 처리가 필요하다.
- Pointer·Touch 대응이 없다.
- 안전한 Log와 접근성 개선이 필요하다.

---

# 69. 기존 코드에서 개선한 이유

## 69-1. 기본 동작 취소

기존:

```javascript
return false
```

개선:

```javascript
event.preventDefault()
```

## 69-2. 안전한 Log

기존:

```javascript
item.innerHTML = message
```

개선:

```javascript
item.textContent = message
```

## 69-3. Mousemove 표시

기존:

```text
이동할 때마다 Log Node 추가
```

개선:

```javascript
coordinates.textContent = (
    `x: ${event.offsetX}, `
    + `y: ${event.offsetY}`
)
```

## 69-4. Drag 종료

기존:

```javascript
dragBox.addEventListener(
    "mouseup",
    stop,
)
```

개선:

```javascript
document.addEventListener(
    "mouseup",
    stop,
)
```

---

# 70. 실무형 예제: Pointer 기반 Drag Component

```javascript
function createDraggable(
    element,
) {
    let isDragging = false
    let offsetX = 0
    let offsetY = 0

    function start(
        event,
    ) {
        event.preventDefault()

        const rect = (
            element
                .getBoundingClientRect()
        )

        offsetX = (
            event.clientX
            - rect.left
        )

        offsetY = (
            event.clientY
            - rect.top
        )

        isDragging = true

        element.classList.add(
            "is-dragging",
        )

        element.setPointerCapture(
            event.pointerId,
        )
    }

    function move(
        event,
    ) {
        if (!isDragging) {
            return
        }

        const left = (
            event.clientX
            - offsetX
            + window.scrollX
        )

        const top = (
            event.clientY
            - offsetY
            + window.scrollY
        )

        element.style.left = (
            `${left}px`
        )

        element.style.top = (
            `${top}px`
        )
    }

    function stop(
        event,
    ) {
        isDragging = false

        element.classList.remove(
            "is-dragging",
        )

        if (
            element.hasPointerCapture(
                event.pointerId,
            )
        ) {
            element.releasePointerCapture(
                event.pointerId,
            )
        }
    }

    element.addEventListener(
        "pointerdown",
        start,
    )

    element.addEventListener(
        "pointermove",
        move,
    )

    element.addEventListener(
        "pointerup",
        stop,
    )

    element.addEventListener(
        "pointercancel",
        stop,
    )

    return function destroy() {
        element.removeEventListener(
            "pointerdown",
            start,
        )

        element.removeEventListener(
            "pointermove",
            move,
        )

        element.removeEventListener(
            "pointerup",
            stop,
        )

        element.removeEventListener(
            "pointercancel",
            stop,
        )
    }
}
```

## 70-1. 실행

```javascript
const dragBox = (
    document.querySelector(
        "#drag-box",
    )
)

const destroyDrag = (
    createDraggable(
        dragBox,
    )
)

// 기능 제거:
// destroyDrag()
```

## 70-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| Closure | Drag 상태를 Component 내부에 보관 |
| Pointer Event | Mouse·Touch·Pen 통합 |
| Pointer Capture | 요소 밖 이동에도 Drag 유지 |
| `getBoundingClientRect()` | Pointer 내부 Offset 계산 |
| 숫자 계산 | 새 위치 산출 |
| 상태 클래스 | Cursor와 시각 상태 변경 |
| Destroy 함수 | Listener 정리와 메모리 관리 |

---

# 71. 대표 오류로 이해하기

## 71-1. `window.getSelection()`이 `null`

Optional Chaining으로 안전하게 처리한다.

## 71-2. Mousemove마다 DOM Node 생성

화면과 Memory 부담이 빠르게 증가한다.

## 71-3. `clientX`와 `pageX` 혼동

Scroll 상태에서 요소 위치가 어긋날 수 있다.

## 71-4. Drag Offset 미저장

요소 좌상단이 Pointer 위치로 점프한다.

## 71-5. 요소 내부 Mouseup만 사용

요소 밖에서 놓으면 Drag가 끝나지 않을 수 있다.

## 71-6. 추적 이미지가 Pointer Event를 가로챔

`pointer-events: none`을 사용한다.

---

# 72. 자주 하는 실수

## 72-1. Context Menu 차단을 보안 기능으로 생각

콘텐츠 접근을 실제로 막지 못한다.

## 72-2. Copy 출처를 원문과 바로 연결

공백이나 줄바꿈을 추가한다.

## 72-3. Double Click 시간을 고정값으로 단정

사용자·운영체제 설정의 영향을 받는다.

## 72-4. Mouseover와 Mouseenter를 같은 이벤트로 생각

Bubbling과 자식 경계 동작이 다르다.

## 72-5. Client 좌표를 문서 전체 좌표로 생각

Viewport 기준이다.

## 72-6. Mousemove에 무거운 작업 수행

`requestAnimationFrame()`과 기존 요소 갱신을 사용한다.

## 72-7. Div에 `img`라는 ID 사용

역할이 명확한 이름을 사용한다.

## 72-8. 동일 ID 중복

각 ID는 문서에서 고유해야 한다.

## 72-9. Mouse Event만 사용해 Touch 미지원

Pointer Event를 검토한다.

## 72-10. Resize마다 새 Log 추가

하나의 상태 표시 요소만 갱신한다.

---

# 73. 핵심 요약

```text
contextmenu
selectstart
copy
→ 브라우저 기본 동작 제어
```

```text
mousedown
mouseup
click
dblclick
→ 마우스 버튼 흐름
```

```text
offset
→ Target 내부

page
→ Document

client
→ Viewport

screen
→ 실제 화면
```

```text
mousemove
→ 매우 자주 발생

requestAnimationFrame()
→ 화면 갱신 주기에 맞춰 처리
```

```text
pointerdown
pointermove
pointerup
pointercancel
→ 통합 Pointer 입력
```

---

# 74. 최종 체크리스트

- [ ] `contextmenu` 기본 동작을 취소할 수 있는가?
- [ ] 우클릭 차단이 보안 기능이 아님을 이해했는가?
- [ ] `selectstart`와 `user-select`를 구분할 수 있는가?
- [ ] 선택 텍스트를 안전하게 읽을 수 있는가?
- [ ] Copy Event에서 출처를 추가할 수 있는가?
- [ ] `text/plain`의 의미를 이해했는가?
- [ ] `mousedown`, `mouseup`, `click`, `dblclick`을 구분할 수 있는가?
- [ ] 네 가지 좌표계를 설명할 수 있는가?
- [ ] `mouseover`와 `mouseenter` 차이를 이해했는가?
- [ ] Mousemove에서 새 DOM Node 생성을 피하는가?
- [ ] `requestAnimationFrame()`으로 빈번한 이벤트를 제어할 수 있는가?
- [ ] 추적 요소에 `pointer-events: none`을 적용할 수 있는가?
- [ ] Drag Offset을 계산할 수 있는가?
- [ ] 요소 밖 Mouseup에서도 Drag를 종료하는가?
- [ ] Pointer Capture를 사용할 수 있는가?
- [ ] Pointer Cancel을 처리하는가?
- [ ] Resize에서 Viewport 크기를 읽을 수 있는가?
- [ ] 안전한 Log에 `textContent`를 사용하는가?
- [ ] 외부 이미지 대신 로컬 Asset을 사용하는가?
- [ ] Listener 제거 기능까지 고려할 수 있는가?

---

# 마무리

마우스 이벤트의 핵심은 좌표를 출력하는 것에서 끝나지 않는다.

```text
브라우저 기본 동작을 목적에 맞게 제어하고
    ↓
이벤트 종류와 좌표 기준을 정확히 선택하고
    ↓
빈번한 이벤트의 렌더링 비용을 줄이고
    ↓
요소 밖 이동과 종료 상황까지 처리하고
    ↓
Mouse·Touch·Pen을 함께 지원하는 구조로 확장하는 것
```

이 흐름을 이해하면 이후 폼 이벤트와 이벤트 전파 문서에서 더 복잡한 사용자 상호작용을 안정적으로 구현할 수 있다.
