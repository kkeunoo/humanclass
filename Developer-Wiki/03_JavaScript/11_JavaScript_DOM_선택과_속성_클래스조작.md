---
title: JavaScript DOM 선택과 속성·클래스 조작
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript DOM 선택과 속성·클래스 조작

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `11_JavaScript_DOM_선택과_속성_클래스조작.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/11_dom.html`, `workspace_teacher/workspace_html/javascript/11_dom.html` |
| 핵심 범위 | DOM, 요소 선택, `getElementById()`, `getElementsByTagName()`, `getElementsByClassName()`, `querySelector()`, `querySelectorAll()`, 속성, `classList`, 요소 제거 |
| 실습 범위 | 제목·메뉴·이미지 요소 선택, 속성 확인·변경·삭제, 클래스 추가·제거·토글, 요소 숨김·삭제 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> DOM 요소를 선택하고 속성·클래스·노드를 조작하는 데 필요한 핵심 코드만 발췌하고, 반환 자료형과 실행 시점까지 함께 설명한다.

---

# 개요

DOM은 HTML 문서를 JavaScript에서 객체처럼 다룰 수 있도록 표현한 구조다.

```text
HTML 문서
→ 브라우저가 파싱
→ DOM 트리 생성
→ JavaScript에서 조회·변경
```

예를 들어 HTML의 제목 요소를 JavaScript에서 가져올 수 있다.

```html
<h1 id="title">DOM 연습</h1>
```

```javascript
const title = document.getElementById(
    "title",
)

console.log(title)
```

DOM을 이용하면 다음 작업이 가능하다.

| 작업 | 예시 |
| --- | --- |
| 요소 조회 | 제목·버튼·메뉴 찾기 |
| 텍스트 변경 | 제목 내용 수정 |
| 속성 변경 | 이미지 `src`, 입력창 `disabled` |
| 클래스 변경 | 활성·비활성 스타일 전환 |
| 요소 생성·삭제 | 목록 추가, 알림 제거 |
| 이벤트 연결 | 클릭·입력·제출 처리 |

> [!IMPORTANT]
> DOM은 HTML 문자열 자체가 아니라 브라우저가 문서를 해석해 만든 객체 구조다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `document` | 현재 HTML 문서를 나타내는 최상위 DOM 객체 |
| Element | HTML 태그 하나를 표현하는 객체 |
| `null` | 단일 요소를 찾지 못한 경우 |
| `HTMLCollection` | 일부 `getElementsBy...()` 메서드가 반환하는 live 컬렉션 |
| `NodeList` | `querySelectorAll()` 등이 반환하는 노드 목록 |
| Live collection | DOM 변경이 목록에 자동 반영되는 컬렉션 |
| Static collection | 선택 당시 결과를 유지하는 목록 |
| 속성 | `id`, `src`, `alt`, `disabled` 등 태그 정보 |
| `classList` | 클래스 목록을 관리하는 `DOMTokenList` |
| `remove()` | DOM 트리에서 요소 제거 |
| DOMContentLoaded | HTML 파싱이 끝난 시점 |

---

# 학습 목표

- DOM과 `document`의 역할을 설명할 수 있다.
- 단일 요소 선택과 여러 요소 선택을 구분할 수 있다.
- 찾지 못한 단일 요소가 `null`임을 이해한다.
- 빈 `HTMLCollection`과 `NodeList`가 Truthy임을 설명할 수 있다.
- `getElementById()`와 `querySelector()`를 구분할 수 있다.
- `getElementsByTagName()`과 `getElementsByClassName()`을 사용할 수 있다.
- 특정 요소 내부에서 다시 요소를 검색할 수 있다.
- `querySelectorAll()`의 반환값을 순회할 수 있다.
- 중복 `id`가 잘못된 HTML 구조임을 설명할 수 있다.
- `hasAttribute()`, `getAttribute()`, `setAttribute()`, `removeAttribute()`를 사용할 수 있다.
- 속성 property와 attribute 차이를 기초 수준에서 설명할 수 있다.
- `classList.add()`, `remove()`, `toggle()`, `contains()`를 사용할 수 있다.
- 요소를 숨기는 것과 DOM에서 삭제하는 것을 구분할 수 있다.
- 스크립트 위치와 `defer`의 관계를 설명할 수 있다.
- 선택 결과가 `null`일 때 안전하게 처리할 수 있다.

---

# 1. DOM

원본 주석:

```text
DOM
→ Document Object Model
→ JavaScript로 수정 가능한 대상
```

DOM은 HTML 요소를 객체와 노드의 트리 구조로 표현한다.

```text
document
└── html
    ├── head
    └── body
        ├── h1
        ├── div
        └── ul
            └── li
```

---

# 2. `document`

```javascript
console.log(document)
```

현재 브라우저 문서 전체를 나타내는 객체다.

`document`를 시작점으로 요소 검색·생성·변경을 수행한다.

---

# 3. Element와 Node

HTML 태그 하나는 일반적으로 Element 객체로 다룬다.

```html
<h1 id="title">DOM 연습</h1>
```

JavaScript에서 선택하면 `HTMLHeadingElement` 같은 구체적인 객체가 된다.

```javascript
const title = document.getElementById(
    "title",
)
```

---

# 4. 객체를 문자열로 연결

원본:

```javascript
console.log(
    "" + title,
)
```

대표 출력:

```text
[object HTMLHeadingElement]
```

객체 내부를 확인하려면 문자열로 연결하기보다 객체 자체를 전달하는 편이 좋다.

```javascript
console.log(title)
```

---

# 5. `getElementById()`

```javascript
const title = document.getElementById(
    "title",
)
```

지정한 `id`와 일치하는 요소 하나를 반환한다.

---

# 6. 요소를 찾지 못한 경우

```javascript
const title2 = document.getElementById(
    "title2",
)

console.log(title2)
```

출력:

```text
null
```

`undefined`가 아니라 `null`이다.

---

# 7. `null` 안전 처리

```javascript
const title = document.getElementById(
    "title",
)

if (title !== null) {
    console.log(title)
}
```

선택적 체이닝:

```javascript
title?.classList.add(
    "active",
)
```

---

# 8. 중복 `id`

원본 HTML에는 다음 구조가 있다.

```html
<div id="view">첫 번째 view</div>
<div id="view" class="pizza">두 번째 view</div>
```

`id`는 문서 안에서 고유해야 한다.

> [!WARNING]
> CSS와 JavaScript가 중복 `id`에서도 일부 동작할 수 있지만 유효한 HTML 구조가 아니다.

---

# 9. 중복 `id`에서 선택 결과

```javascript
const view = document.getElementById(
    "view",
)
```

브라우저는 일반적으로 첫 번째 일치 요소를 반환하지만 중복 `id`에 의존하면 안 된다.

개선:

```html
<div id="first-view">첫 번째 view</div>
<div id="second-view" class="pizza">
    두 번째 view
</div>
```

---

# 10. `getElementsByTagName()`

```javascript
const divs = document.getElementsByTagName(
    "div",
)

console.log(divs)
```

일치하는 모든 태그를 `HTMLCollection`으로 반환한다.

---

# 11. 빈 `HTMLCollection`

```javascript
const unknownElements = (
    document.getElementsByTagName(
        "div2",
    )
)

console.log(
    unknownElements.length,
)
```

출력:

```text
0
```

단일 선택처럼 `null`을 반환하지 않는다.

---

# 12. 빈 컬렉션도 Truthy

```javascript
if (unknownElements) {
    console.log("참")
}
```

빈 컬렉션 객체 자체는 Truthy이므로 `"참"`이 출력된다.

실제 결과 존재 여부는 길이로 확인한다.

```javascript
if (
    unknownElements.length > 0
) {
    console.log("요소 있음")
}
```

---

# 13. `getElementsByClassName()`

```javascript
const menus = (
    document.getElementsByClassName(
        "menu",
    )
)

console.log(menus)
```

지정한 클래스가 포함된 모든 요소를 `HTMLCollection`으로 반환한다.

---

# 14. 여러 클래스가 있는 요소

```html
<li class="menu li1">치킨</li>
```

다음 선택에 포함된다.

```javascript
document.getElementsByClassName(
    "menu",
)
```

클래스 문자열 전체가 정확히 같은지 검사하는 것이 아니라 `menu` 클래스 포함 여부를 본다.

---

# 15. 특정 요소 내부 검색

```javascript
const menuList = document.getElementById(
    "menu",
)

const pizzas = (
    menuList.getElementsByClassName(
        "pizza",
    )
)
```

문서 전체가 아니라 `menuList` 내부에서만 찾는다.

---

# 16. 원본의 한글 `id`

원본:

```html
<ul id="메뉴">
```

문법적으로 가능하지만 실무에서는 도구·협업·일관성을 위해 영문 이름을 자주 사용한다.

```html
<ul id="menu">
```

---

# 17. `querySelector()`

```javascript
const pizzaView = document.querySelector(
    "#view.pizza",
)
```

CSS 선택자를 사용해 첫 번째 일치 요소 하나를 반환한다.

---

# 18. `querySelector()` 결과 없음

```javascript
const view4 = document.querySelector(
    "div#view4",
)

console.log(view4)
```

출력:

```text
null
```

---

# 19. CSS 선택자 활용

```javascript
document.querySelector(
    "ul#menu > li.pizza",
)

document.querySelector(
    '[data-role="menu"]',
)

document.querySelector(
    "input:checked",
)
```

복잡한 조건을 CSS 선택자로 표현할 수 있다.

---

# 20. `querySelectorAll()`

```javascript
const views = document.querySelectorAll(
    "#view",
)

console.log(views)
```

일치하는 모든 요소를 `NodeList`로 반환한다.

중복 `id` 검색도 기술적으로 결과가 여러 개 나올 수 있지만 HTML 구조는 먼저 수정해야 한다.

---

# 21. 빈 `NodeList`

```javascript
const items = document.querySelectorAll(
    ".not-found",
)

console.log(items.length)
```

출력:

```text
0
```

빈 `NodeList`도 객체이므로 Truthy다.

---

# 22. `NodeList` 순회

```javascript
const menuItems = (
    document.querySelectorAll(
        ".menu",
    )
)

menuItems.forEach(
    item => {
        console.log(item)
    },
)
```

---

# 23. `HTMLCollection` 순회

`HTMLCollection`은 환경과 사용 방식에 따라 직접 `forEach()`를 사용할 수 없다.

```javascript
const menus = (
    document.getElementsByClassName(
        "menu",
    )
)

for (const menu of menus) {
    console.log(menu)
}
```

배열 변환:

```javascript
const menuArray = Array.from(
    menus,
)
```

---

# 24. HTMLCollection과 NodeList

| 항목 | `HTMLCollection` | `NodeList` |
| --- | --- | --- |
| 대표 반환 | `getElementsBy...()` | `querySelectorAll()` |
| 내용 | Element 중심 | Node 또는 Element |
| Live 여부 | 대표적으로 live | `querySelectorAll()`은 static |
| `forEach()` | 일반적으로 없음 | 보통 사용 가능 |
| 인덱스 접근 | 가능 | 가능 |

---

# 25. Live collection

```javascript
const divs = (
    document.getElementsByTagName(
        "div",
    )
)

const newDiv = document.createElement(
    "div",
)

document.body.append(
    newDiv,
)

console.log(divs.length)
```

DOM 변경이 기존 컬렉션에 자동 반영될 수 있다.

---

# 26. Static NodeList

```javascript
const divs = document.querySelectorAll(
    "div",
)

const newDiv = document.createElement(
    "div",
)

document.body.append(
    newDiv,
)

console.log(divs.length)
```

기존 `NodeList`에는 새 요소가 자동 추가되지 않는다.

다시 선택해야 최신 목록을 얻는다.

---

# 27. 선택 메서드 기준

| 목적 | 권장 |
| --- | --- |
| 고유 `id` 하나 | `getElementById()` |
| CSS 선택자 하나 | `querySelector()` |
| CSS 선택자 여러 개 | `querySelectorAll()` |
| live 태그 목록 필요 | `getElementsByTagName()` |
| live 클래스 목록 필요 | `getElementsByClassName()` |

일반적인 화면 코드에서는 `querySelector()`와 `querySelectorAll()`이 일관된 선택자 문법 때문에 자주 사용된다.

---

# 28. 속성 선택 대상

```javascript
const image = document.querySelector(
    "#aha",
)

console.log(image)
```

속성을 읽기 전에 요소가 실제로 존재하는지 확인한다.

---

# 29. `hasAttribute()`

```javascript
const hasSrc = image.hasAttribute(
    "src",
)

console.log(hasSrc)
```

속성 이름이 존재하면 `true`다.

다음 속성 검사에 활용할 수 있다.

- `disabled`
- `required`
- `readonly`
- `aria-expanded`
- `data-*`

---

# 30. `getAttribute()`

```javascript
const src = image.getAttribute(
    "src",
)

console.log(src)
```

HTML에 작성된 속성값을 문자열로 반환한다.

---

# 31. 없는 속성 조회

```javascript
const value = image.getAttribute(
    "src2",
)

console.log(value)
```

출력:

```text
null
```

---

# 32. `setAttribute()`

```javascript
image.setAttribute(
    "data-center",
    "교육센터",
)
```

기존 속성이 있으면 값을 바꾸고, 없으면 새 속성을 만든다.

---

# 33. 사용자 정의 속성

원본:

```javascript
image.setAttribute(
    "human",
    "교육센터",
)
```

임의 속성도 브라우저가 보존할 수 있지만 사용자 정의 데이터는 `data-*` 형식을 권장한다.

```javascript
image.setAttribute(
    "data-center",
    "교육센터",
)
```

---

# 34. `dataset`

```html
<img
    id="aha"
    data-center="교육센터"
    alt="아하 모먼트"
>
```

```javascript
console.log(
    image.dataset.center,
)
```

출력:

```text
교육센터
```

---

# 35. `removeAttribute()`

```javascript
image.removeAttribute(
    "data-center",
)
```

지정한 속성을 제거한다.

속성이 없어도 일반적으로 오류가 발생하지 않는다.

---

# 36. 속성 property 접근

일부 표준 속성은 객체 property로도 접근할 수 있다.

```javascript
console.log(image.src)
console.log(image.alt)

image.alt = "변경된 설명"
```

---

# 37. Attribute와 Property

| 구분 | 예 |
| --- | --- |
| Attribute | HTML에 작성된 문자열 정보 |
| Property | 현재 DOM 객체의 상태값 |

입력 요소에서 차이가 잘 보인다.

```html
<input value="초기값">
```

사용자가 값을 변경하면 `input.value`는 바뀌지만 `getAttribute("value")`는 초기 HTML 값을 유지할 수 있다.

---

# 38. Boolean 속성

```html
<button disabled>저장</button>
```

```javascript
const button = document.querySelector(
    "button",
)

console.log(button.disabled)
```

Boolean 상태는 property 사용이 더 자연스러운 경우가 많다.

```javascript
button.disabled = false
```

---

# 39. 이미지 `src` 변경

원본:

```javascript
setTimeout(
    function () {
        image.setAttribute(
            "src",
            "새 이미지 URL",
        )
    },
    2000,
)
```

2초 후 이미지 주소를 바꾼다.

---

# 40. 외부 이미지 URL 주의

원본 이미지는 외부 사이트의 긴 URL에 의존한다.

문제점:

- URL 만료 가능
- 외부 서버 차단 가능
- CORS·핫링크 제한
- 문서 재현성 저하
- 개인정보·추적 위험

학습 프로젝트에서는 로컬 이미지나 안정적인 자체 경로를 사용하는 편이 좋다.

```html
<img
    id="aha"
    src="./images/aha.webp"
    alt="아하 모먼트"
>
```

---

# 41. 이미지 변경 예제

```javascript
const image = document.querySelector(
    "#aha",
)

if (image !== null) {
    setTimeout(
        () => {
            image.src = (
                "./images/changed.webp"
            )

            image.alt = (
                "변경된 이미지"
            )
        },
        2000,
    )
}
```

이미지를 바꿀 때 대체 텍스트도 실제 내용과 맞추는 것이 좋다.

---

# 42. `classList`

```javascript
const div2 = document.querySelector(
    "#div2",
)

console.log(
    div2.classList,
)
```

`classList`는 배열이 아니라 `DOMTokenList`다.

---

# 43. `classList.add()`

```javascript
div1.classList.add(
    "blue",
)
```

클래스를 추가한다.

같은 클래스를 다시 추가해도 중복 저장되지 않는다.

---

# 44. 여러 클래스 추가

```javascript
div1.classList.add(
    "blue",
    "bg-yellow",
)
```

여러 클래스를 한 번에 추가할 수 있다.

---

# 45. `classList.remove()`

```javascript
div1.classList.remove(
    "blue",
)
```

클래스를 제거한다.

없는 클래스를 제거해도 일반적으로 오류가 발생하지 않는다.

---

# 46. `classList.toggle()`

```javascript
div1.classList.toggle(
    "blue",
)
```

클래스가 있으면 제거하고 없으면 추가한다.

---

# 47. `toggle()` 반환값

```javascript
const isActive = (
    div1.classList.toggle(
        "blue",
    )
)

console.log(isActive)
```

토글 이후 클래스가 존재하면 `true`, 없으면 `false`를 반환한다.

---

# 48. 강제 토글

```javascript
div1.classList.toggle(
    "blue",
    true,
)
```

반드시 추가한다.

```javascript
div1.classList.toggle(
    "blue",
    false,
)
```

반드시 제거한다.

---

# 49. `classList.contains()`

```javascript
const isBlue = (
    div1.classList.contains(
        "blue",
    )
)

console.log(isBlue)
```

클래스 존재 여부를 Boolean으로 반환한다.

---

# 50. Contains 후 직접 Add·Remove

```javascript
if (
    div1.classList.contains(
        "blue",
    )
) {
    div1.classList.remove(
        "blue",
    )
} else {
    div1.classList.add(
        "blue",
    )
}
```

이 동작은 `toggle()`로 더 간단하게 작성할 수 있다.

---

# 51. `className`과 `classList`

```javascript
element.className = "blue"
```

기존 모든 클래스를 한 번에 교체할 수 있다.

```javascript
element.classList.add(
    "blue",
)
```

기존 클래스를 유지하면서 개별 클래스를 관리한다.

실무에서는 상태 클래스 조작에 `classList`가 안전하다.

---

# 52. 요소 제거 `remove()`

```javascript
div2.remove()
```

현재 DOM 트리에서 요소를 제거한다.

---

# 53. `remove()` 후 객체 참조

원본 주석은 “지우면 되돌릴 수 없다”고 설명한다.

변수에 참조가 남아 있다면 다시 삽입할 수 있다.

```javascript
const parent = div2.parentElement

div2.remove()

parent?.append(
    div2,
)
```

> [!IMPORTANT]
> DOM 트리에서 제거되는 것과 JavaScript 객체 참조가 완전히 사라지는 것은 다르다.

---

# 54. 삭제와 숨김

| 목적 | 방법 |
| --- | --- |
| 화면에서만 잠시 숨김 | `hidden`, CSS 클래스 |
| 접근성 트리까지 숨김 | 상황에 맞는 `hidden`, `aria-*` |
| DOM 구조에서 제거 | `remove()` |
| 나중에 재삽입 | 참조 저장 후 `append()` |

---

# 55. `hidden` property

```javascript
div2.hidden = true
```

다시 표시:

```javascript
div2.hidden = false
```

단순 표시·숨김에는 요소 제거보다 의도가 명확할 수 있다.

---

# 56. CSS 클래스 기반 숨김

```css
.is-hidden {
    display: none;
}
```

```javascript
div2.classList.add(
    "is-hidden",
)
```

상태에 따라 다시 제거할 수 있다.

---

# 57. 스크립트 실행 시점

원본 주석:

```text
script가 head에 있으면
HTML 로딩 전에 실행되어
선택 결과가 null일 수 있음
```

HTML 파싱 전에 요소를 선택하면 아직 DOM에 존재하지 않는다.

---

# 58. Body 끝에 Script 배치

원본은 `<body>` 마지막에 `<script>`를 배치한다.

```html
<body>
    <h1 id="title">DOM 연습</h1>

    <script>
        const title = (
            document.getElementById(
                "title"
            )
        )
    </script>
</body>
```

선택 대상이 먼저 파싱되므로 정상적으로 찾을 수 있다.

---

# 59. `defer`

외부 JavaScript는 다음처럼 작성할 수 있다.

```html
<head>
    <script
        src="./js/main.js"
        defer
    ></script>
</head>
```

`defer`는 HTML 파싱을 막지 않고 문서 파싱이 끝난 뒤 스크립트를 실행한다.

---

# 60. `DOMContentLoaded`

```javascript
document.addEventListener(
    "DOMContentLoaded",
    () => {
        const title = (
            document.getElementById(
                "title",
            )
        )

        console.log(title)
    },
)
```

DOM 구성이 끝난 뒤 실행한다.

`defer` 스크립트에서는 일반적으로 별도 이벤트 대기가 필요하지 않은 경우가 많다.

---

# 61. 안전한 선택 함수

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
            `${selector} 요소를 찾을 수 없습니다.`,
        )
    }

    return element
}
```

필수 요소가 없을 때 조용히 실패하지 않고 원인을 알려 준다.

---

# 62. 선택 결과 변수명

좋지 않은 예:

```text
const view2 = ...
const view3 = ...
const view4 = ...
```

개선:

```text
const pizzaView = ...
const firstView = ...
const missingView = ...
```

선택 기준이나 역할이 드러나는 이름을 사용한다.

---

# 63. 원본 HTML 개선

중복 `id`와 한글 `id`를 정리한 예:

```html
<h1 id="title">
    DOM 연습
</h1>

<div id="first-view">
    첫 번째 view
</div>

<div
    id="pizza-view"
    class="pizza"
>
    두 번째 view
</div>

<ul id="menu">
    <li class="menu-item">
        치킨
    </li>

    <li
        class="menu-item pizza"
    >
        피자
    </li>
</ul>
```

---

# 64. 원본 선택 코드 개선

```javascript
const title = getRequiredElement(
    "#title",
)

const menu = getRequiredElement(
    "#menu",
)

const pizzaItems = (
    menu.querySelectorAll(
        ".pizza",
    )
)

pizzaItems.forEach(
    item => {
        item.classList.add(
            "is-selected",
        )
    },
)
```

---

# 65. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| DOM 설명 | 상세 주석과 활용 예시 추가 | 핵심 설명 중심 |
| 메뉴 목록 | `#메뉴` 한 개 | `#메뉴`, `#메뉴2` 두 개 |
| 중복 `id` | 그대로 사용하며 동작 설명 | 동일 |
| 빈 컬렉션 | Truthy 설명 추가 | 기본 결과 확인 |
| 선택자 | 주석이 더 상세 | 핵심 사용 중심 |
| 속성 | 활용 상황 설명 추가 | 핵심 메서드 중심 |
| 클래스 | `contains()` 활용 설명 추가 | 기본 조작 중심 |
| 요소 제거 | 복구 불가로 설명 | 단순 제거 |
| 선택 방식 | 일부 `querySelector()` | `div1`, `div2`는 `getElementById()` |

## 65-1. 내 코드의 장점

- DOM과 `document`의 관계를 상세히 기록했다.
- 단일 선택 실패와 컬렉션 실패의 차이를 설명했다.
- 특정 DOM 내부에서 다시 검색하는 방식을 확인했다.
- 속성·클래스 메서드의 동작을 자세히 기록했다.
- 스크립트 위치에 따라 `null`이 발생할 수 있음을 설명했다.

## 65-2. 내 코드의 개선점

- 중복 `id`가 잘못된 HTML 구조임을 더 명확히 해야 한다.
- `HTMLCollection`을 배열이라고 설명한 부분을 수정해야 한다.
- 빈 컬렉션은 Truthy이므로 객체 존재 검사만으로 결과 유무를 판단할 수 없다.
- 사용자 정의 속성은 `data-*` 형식을 사용하는 편이 좋다.
- 외부 이미지 URL 의존을 줄여야 한다.
- `remove()` 후 변수 참조가 있으면 재삽입할 수 있다.
- 전역 변수 선언에 `let`보다 `const`를 사용할 수 있는 곳이 많다.

## 65-3. 강사님 코드의 장점

- DOM 선택부터 속성·클래스 조작까지 한 흐름으로 구성되어 있다.
- 두 메뉴 목록을 사용해 문서 전체 선택과 내부 선택을 비교할 수 있다.
- 선택 메서드별 반환 형태를 직접 확인할 수 있다.
- `classList` 핵심 기능을 간결하게 실습한다.

## 65-4. 강사님 코드의 보충점

- 중복 `id`의 HTML 유효성 문제를 설명할 필요가 있다.
- `HTMLCollection`과 `NodeList`의 차이를 보충할 수 있다.
- live collection과 static collection 차이를 설명할 필요가 있다.
- 속성 property와 attribute의 차이를 보충할 수 있다.
- 요소 제거와 숨김의 선택 기준을 설명할 수 있다.
- `defer`를 이용한 외부 스크립트 실행 방식을 추가할 수 있다.

---

# 66. 기존 코드에서 개선 코드로 바꾼 이유

## 66-1. 중복 ID 제거

기존:

```html
<div id="view"></div>
<div id="view"></div>
```

개선:

```html
<div id="first-view"></div>
<div id="second-view"></div>
```

## 66-2. 컬렉션 존재 검사

기존:

```javascript
if (elements) {
    console.log("참")
}
```

개선:

```javascript
if (
    elements.length > 0
) {
    console.log("요소 있음")
}
```

## 66-3. 사용자 정의 속성

기존:

```javascript
element.setAttribute(
    "human",
    "교육센터",
)
```

개선:

```javascript
element.dataset.center = (
    "교육센터"
)
```

## 66-4. 요소 숨김

기존:

```javascript
element.remove()
```

잠시 숨기는 목적:

```javascript
element.hidden = true
```

---

# 67. 실무형 예제: 메뉴 선택 상태 관리

```javascript
const menuList = getRequiredElement(
    "#menu",
)

const menuItems = (
    menuList.querySelectorAll(
        ".menu-item",
    )
)

function selectMenu(
    selectedItem,
) {
    menuItems.forEach(
        item => {
            const isSelected = (
                item === selectedItem
            )

            item.classList.toggle(
                "is-selected",
                isSelected,
            )

            item.setAttribute(
                "aria-selected",
                String(isSelected),
            )
        },
    )
}

menuItems.forEach(
    item => {
        item.addEventListener(
            "click",
            () => {
                selectMenu(item)
            },
        )
    },
)
```

## 67-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `querySelectorAll()` | 여러 메뉴 요소 선택 |
| `forEach()` | 각 요소에 동일 작업 수행 |
| `classList.toggle(force)` | 선택된 요소만 클래스 유지 |
| `setAttribute()` | 접근성 상태 동기화 |
| 요소 비교 | 클릭한 요소인지 확인 |
| 이벤트 콜백 | 사용자 클릭 후 상태 변경 |

---

# 68. 대표 오류로 이해하기

## 68-1. 선택 결과가 `null`

존재하지 않는 요소에 `classList`를 사용하면 `TypeError`가 발생한다.

## 68-2. 빈 컬렉션을 `false`로 예상

빈 객체이므로 Truthy다.

## 68-3. HTMLCollection에서 `forEach()` 호출

환경에 따라 메서드가 없어 `TypeError`가 발생할 수 있다.

## 68-4. 중복 ID 선택

첫 번째 요소만 선택되어 다른 요소가 무시될 수 있다.

## 68-5. Head Script에서 즉시 선택

HTML 파싱 전이면 `null`이다.

## 68-6. 요소 제거 후 다시 선택

DOM에서 삭제되었으므로 같은 선택자로 찾을 수 없다.

---

# 69. 자주 하는 실수

## 69-1. 모든 선택 메서드가 배열을 반환한다고 생각

단일 Element·`null`·`HTMLCollection`·`NodeList`가 서로 다르다.

## 69-2. 빈 컬렉션을 Falsy라고 생각

객체 자체는 Truthy다.

## 69-3. `id`를 여러 요소에 사용

문서 내 고유해야 한다.

## 69-4. `querySelector()`가 모든 요소를 반환한다고 생각

첫 번째 요소 하나만 반환한다.

## 69-5. `querySelectorAll()`이 live라고 생각

일반적으로 static `NodeList`다.

## 69-6. `classList`를 실제 배열이라고 생각

`DOMTokenList`다.

## 69-7. `setAttribute()`만 모든 상태에 사용

표준 DOM property가 더 적합한 경우가 있다.

## 69-8. `remove()`와 숨김을 같은 기능으로 이해

DOM 삭제와 표시 상태 변경은 다르다.

## 69-9. 외부 이미지 URL을 영구 경로로 생각

언제든 바뀌거나 차단될 수 있다.

## 69-10. Script 실행 시점을 고려하지 않음

선택 대상이 아직 파싱되지 않았을 수 있다.

---

# 70. 핵심 요약

```text
document
→ 현재 HTML 문서

getElementById()
querySelector()
→ 요소 하나 또는 null
```

```text
getElementsByTagName()
getElementsByClassName()
→ HTMLCollection

querySelectorAll()
→ static NodeList
```

```text
hasAttribute()
→ 속성 존재 여부

getAttribute()
→ 속성값 읽기

setAttribute()
→ 속성 추가·변경

removeAttribute()
→ 속성 제거
```

```text
classList.add()
classList.remove()
classList.toggle()
classList.contains()
→ 클래스 상태 관리
```

```text
remove()
→ DOM에서 제거

hidden
→ 표시·숨김

defer
→ HTML 파싱 후 실행
```

---

# 71. 최종 체크리스트

- [ ] DOM과 `document`의 역할을 설명할 수 있는가?
- [ ] 단일 선택과 다중 선택을 구분할 수 있는가?
- [ ] 단일 선택 실패 시 `null`을 처리할 수 있는가?
- [ ] 빈 컬렉션이 Truthy임을 이해했는가?
- [ ] `getElementById()`를 사용할 수 있는가?
- [ ] `getElementsByTagName()`과 `getElementsByClassName()`을 사용할 수 있는가?
- [ ] 특정 요소 내부에서 다시 검색할 수 있는가?
- [ ] `querySelector()`와 `querySelectorAll()`을 구분할 수 있는가?
- [ ] HTMLCollection과 NodeList의 차이를 설명할 수 있는가?
- [ ] live collection과 static collection을 구분할 수 있는가?
- [ ] 중복 `id`를 사용하지 않는가?
- [ ] `hasAttribute()`로 속성 존재 여부를 확인할 수 있는가?
- [ ] 속성을 읽고·변경하고·삭제할 수 있는가?
- [ ] 사용자 정의 데이터에 `data-*`를 사용할 수 있는가?
- [ ] `classList`가 DOMTokenList임을 이해했는가?
- [ ] 클래스를 추가·제거·토글·검사할 수 있는가?
- [ ] `toggle()`의 force 인수를 사용할 수 있는가?
- [ ] DOM 제거와 숨김을 구분할 수 있는가?
- [ ] `remove()` 후 참조가 남으면 재삽입할 수 있음을 이해했는가?
- [ ] `defer` 또는 적절한 스크립트 위치를 사용할 수 있는가?
- [ ] 필수 요소가 없을 때 오류를 명확하게 처리할 수 있는가?

---

# 마무리

DOM 조작의 핵심은 요소를 선택하는 것에서 끝나지 않는다.

```text
반환 자료형을 정확히 구분하고
    ↓
선택 실패와 빈 컬렉션을 안전하게 처리하고
    ↓
속성과 property를 목적에 맞게 사용하고
    ↓
클래스로 화면 상태를 관리하고
    ↓
실행 시점과 DOM 구조를 올바르게 설계하는 것
```

이 흐름을 이해하면 이후 DOM 생성·텍스트 변경·이벤트 처리 문서에서 화면을 더 안전하게 제어할 수 있다.
