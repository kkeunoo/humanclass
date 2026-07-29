# JavaScript DOM 선택과 속성·클래스 조작

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `11_JavaScript_DOM선택과_속성클래스조작.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `10_JavaScript_문자열과_문자열메서드.md` |
| 다음 학습 | `12_JavaScript_DOM이벤트.md` |
| 원본 기준 | `workspace/workspace_html/javascript/11_dom.html`, `workspace_teacher/workspace_html/javascript/11_dom.html` |
| 핵심 범위 | DOM, `document`, `getElementById()`, `getElementsByTagName()`, `getElementsByClassName()`, `querySelector()`, `querySelectorAll()`, `HTMLCollection`, `NodeList`, 속성 조회·추가·변경·삭제, `classList`, `add()`, `remove()`, `toggle()`, `contains()`, DOM 제거 |
| 프로젝트 연결 | 화면 요소 선택, 메뉴 조작, 이미지 교체, 클래스 기반 스타일 변경, 폼 속성 검사, 동적 UI 구성 |

> 이 문서는 내 코드와 강사님 코드의 `11_dom.html`을 직접 비교해 작성했습니다. 두 파일은 DOM 선택, 속성 조작, 클래스 조작, 요소 제거까지 거의 같은 흐름으로 진행합니다. 내 코드는 설명이 더 많고 일부 선택 방법과 출력 문구가 다르며, 강사님 코드는 더 간결합니다. 중복된 `id`, `HTMLCollection`을 배열이라고 표현한 부분, 빈 collection의 truthy 판정, `remove()` 설명, 외부 이미지 사용, `querySelectorAll('#view')` 사용은 원본을 보존한 뒤 정확한 동작을 별도로 설명합니다.

---

# 학습 목표

- DOM과 `document` 객체의 역할을 설명한다.
- script 실행 위치에 따라 DOM 선택 결과가 달라질 수 있음을 이해한다.
- `getElementById()`의 반환값과 미발견 시 `null`을 이해한다.
- 중복된 `id`가 HTML 문법상 잘못된 구조임을 이해한다.
- `getElementsByTagName()`과 `getElementsByClassName()`의 반환 형식을 이해한다.
- `HTMLCollection`과 일반 배열을 구분한다.
- 빈 collection도 truthy라는 점을 이해한다.
- 특정 DOM 내부에서 다시 요소를 검색한다.
- `querySelector()`와 `querySelectorAll()`의 차이를 설명한다.
- `HTMLCollection`과 `NodeList`를 구분한다.
- `hasAttribute()`, `getAttribute()`, `setAttribute()`, `removeAttribute()`를 사용한다.
- `classList.add()`, `remove()`, `toggle()`, `contains()`를 사용한다.
- `contains()`가 true 또는 false를 반환하는 조건을 설명한다.
- `Element.remove()`가 DOM에서 요소를 제거한다는 점을 이해한다.
- 내 코드와 강사님 코드의 실제 차이를 원본에 근거해 비교한다.

---

# 1. DOM이란?

DOM은 Document Object Model의 약자입니다.

HTML 문서를 JavaScript가 읽고 조작할 수 있는 객체 구조로 표현한 것입니다.

```js
console.log(document)
```

`document`는 현재 HTML 문서 전체를 나타내는 최상위 DOM 객체입니다.

내 코드 주석:

```text
DOM : Document Object Model
JavaScript로 수정이 가능
```

강사님 코드 주석:

```text
DOM : Document Object Model
javascript로 수정이 가능한 대상
```

두 설명의 핵심은 같습니다.

---

# 2. HTML 요소와 DOM 객체

HTML:

```html
<h1 id="title">DOM 연습</h1>
```

JavaScript:

```js
const title =
  document.getElementById("title")
```

`title` 변수에는 문자열 HTML이 아니라 실제 `HTMLHeadingElement` 객체가 들어갑니다.

이 객체를 통해 다음과 같은 작업을 할 수 있습니다.

```js
title.textContent =
  "새 제목"

title.classList.add(
  "active"
)
```

원본은 선택과 클래스 조작 중심으로 실습합니다.

---

# 3. Script 위치

내 코드에는 다음 설명이 있습니다.

```text
script가 head 영역으로 그대로 올라간다면
로딩이 다 되기 전에 실행되어 null이 반환될 수 있음
```

현재 원본의 `<script>`는 `<body>` 마지막 부분에 있습니다.

따라서 앞에서 작성된 HTML 요소들이 먼저 파싱된 뒤 script가 실행됩니다.

`<head>`에서 바로 실행해야 한다면 다음 중 하나를 사용할 수 있습니다.

```html
<script defer src="main.js"></script>
```

또는:

```js
document.addEventListener(
  "DOMContentLoaded",
  function() {
    // DOM 선택
  }
)
```

---

# 4. GetElementById

공통 원본:

```js
const title =
  document.getElementById(
    "title"
  )

console.log(title)
```

`id="title"`인 요소 하나를 반환합니다.

반환 형식:

```text
Element 객체 또는 null
```

---

# 5. 문자열 결합한 DOM 출력

공통 원본:

```js
console.log("" + title)
```

브라우저 환경에서는 다음과 비슷한 문자열이 나올 수 있습니다.

```text
[object HTMLHeadingElement]
```

내 코드에서는 이를 heap 영역의 주소값과 연결해 설명합니다.

정확히는 실제 메모리 주소가 노출된 것이 아닙니다.

객체가 문자열로 변환될 때 기본 문자열 표현이 출력된 것입니다.

```text
[object HTMLHeadingElement]
```

은 객체의 종류를 나타내는 문자열 표현입니다.

---

# 6. 없는 ID

공통 원본:

```js
const title2 =
  document.getElementById(
    "title2"
  )

console.log(title2)
```

결과:

```text
null
```

`null`은 해당 id를 가진 DOM 요소를 찾지 못했다는 뜻입니다.

내 코드에서는 `undefined`와 다른 값 없음의 표현이라고 설명합니다.

핵심적으로 다음처럼 구분할 수 있습니다.

```text
getElementById() 미발견
→ null

선언된 변수에 값이 할당되지 않음
→ undefined일 수 있음
```

---

# 7. 중복된 ID

양쪽 원본 HTML:

```html
<div id="view">
  첫번째 view
</div>

<div
  id="view"
  class="pizza"
>
  두번째 view
</div>
```

같은 문서에서 `id="view"`가 두 번 사용되었습니다.

HTML에서 id는 문서 내에서 고유해야 합니다.

따라서 이 구조는 올바른 HTML이 아닙니다.

---

# 8. 중복 ID와 GetElementById

공통 원본:

```js
const view =
  document.getElementById(
    "view"
  )
```

일반적으로 문서 순서상 첫 번째 `id="view"` 요소가 반환됩니다.

하지만 중복 id 자체가 잘못된 문서 구조이므로 이 동작에 의존하면 안 됩니다.

개선:

```html
<div id="view1">
  첫번째 view
</div>

<div
  id="view2"
  class="pizza"
>
  두번째 view
</div>
```

또는 여러 요소를 묶으려면 class를 사용합니다.

```html
<div class="view">
```

---

# 9. CSS와 중복 ID

내 CSS 주석:

```text
CSS는 ID가 중복이 되어도 동작시킴
```

CSS selector:

```css
#view {
  color: red;
}
```

브라우저는 selector에 맞는 모든 요소에 스타일을 적용할 수 있습니다.

하지만 스타일이 적용된다고 해서 중복 id가 올바른 HTML이 되는 것은 아닙니다.

```text
CSS 적용 가능
≠
HTML 구조가 유효함
```

---

# 10. GetElementsByTagName

공통 원본:

```js
let divs =
  document.getElementsByTagName(
    "div"
  )

console.log(divs)
```

반환값은 `HTMLCollection`입니다.

문서 안의 모든 `<div>` 요소가 포함됩니다.

---

# 11. HTMLCollection은 배열이 아님

내 코드와 강사님 코드 모두 collection을 배열에 가깝게 설명합니다.

```text
유사 배열
class를 배열로 돌려줌
length가 0인 빈 배열
```

정확히는 `HTMLCollection`은 일반 배열이 아닙니다.

가능:

```js
divs.length
divs[0]
```

일반 배열처럼 바로 사용할 수 없는 메서드도 있습니다.

```js
divs.map
// undefined
```

배열로 변환:

```js
const divArray =
  Array.from(divs)
```

또는:

```js
const divArray =
  [...divs]
```

---

# 12. Live Collection

`getElementsByTagName()`과 `getElementsByClassName()`이 반환하는 `HTMLCollection`은 일반적으로 live collection입니다.

DOM이 변경되면 collection 내용도 자동으로 반영될 수 있습니다.

```js
const divs =
  document.getElementsByTagName(
    "div"
  )

const newDiv =
  document.createElement(
    "div"
  )

document.body.appendChild(
  newDiv
)

console.log(divs.length)
```

새 div가 collection에 반영될 수 있습니다.

원본에는 없는 확장 개념입니다.

---

# 13. 없는 Tag 검색

공통 원본:

```js
let divs2 =
  document.getElementsByTagName(
    "div2"
  )

console.log(divs2)
```

`<div2>`라는 tag가 문서에 없으므로 length가 0인 `HTMLCollection`이 반환됩니다.

결과는 `null`이 아닙니다.

---

# 14. 빈 Collection의 Truthy

공통 원본:

```js
if (divs2) {
  console.log("참")
}
```

빈 collection 객체도 객체이므로 truthy입니다.

따라서 `"참"`이 출력됩니다.

요소 존재 여부를 검사하려면 length를 확인해야 합니다.

```js
if (divs2.length > 0) {
  console.log("존재")
}
```

---

# 15. GetElementsByClassName

공통 원본:

```js
let menus =
  document
    .getElementsByClassName(
      "menu"
    )

console.log(menus)
```

`class` 목록에 `"menu"`가 포함된 모든 요소를 반환합니다.

HTML:

```html
<li class="menu li1">
<li class="menu pizza">
<li class="menu">
```

세 요소가 collection에 포함됩니다.

---

# 16. Class 순서와 포함 관계

다음 요소:

```html
<li class="menu li1">
```

는 class 두 개를 가집니다.

```text
menu
li1
```

`getElementsByClassName("menu")`은 class 속성 전체가 정확히 `"menu"`인 요소만 찾는 것이 아닙니다.

class 목록에 `menu`가 포함된 요소를 찾습니다.

---

# 17. 특정 DOM 내부 검색

공통 원본:

```js
let 메뉴 =
  document.getElementById(
    "메뉴"
  )

let pizza =
  메뉴.getElementsByClassName(
    "pizza"
  )

console.log(pizza)
```

문서 전체가 아니라 `ul#메뉴` 안에서만 class `"pizza"`를 검색합니다.

결과:

```html
<li class="menu pizza">
  피자
</li>
```

---

# 18. 한글 ID와 변수명

원본:

```html
<ul id="메뉴">
```

```js
let 메뉴 =
  document.getElementById(
    "메뉴"
  )
```

JavaScript 식별자와 HTML id에 한글을 사용할 수 있습니다.

다만 협업 프로젝트에서는 영어 naming convention을 일관되게 사용하는 경우가 많습니다.

예:

```html
<ul id="menu">
```

```js
const menu =
  document.getElementById(
    "menu"
  )
```

---

# 19. 음식 이름 차이

내 코드:

```html
<li class="menu">
  똠얌꿍
</li>
```

강사님 코드:

```html
<li class="menu">
  똠양꿍
</li>
```

문자열 내용 차이만 있으며 DOM 선택 동작에는 영향이 없습니다.

원본 차이를 추측해 수정하지 않습니다.

---

# 20. QuerySelector

공통 원본:

```js
let view2 =
  document.querySelector(
    "#view.pizza"
  )
```

`querySelector()`는 CSS selector 문법을 사용합니다.

```text
#view.pizza
→ id가 view이면서 class가 pizza인 요소
```

현재 원본에서는 두 번째 div가 선택됩니다.

---

# 21. QuerySelector 반환값

`querySelector()`:

```text
첫 번째 일치 요소
또는
일치 요소가 없으면 null
```

여러 요소가 일치해도 하나만 반환합니다.

---

# 22. Div Hash View Selector

공통 원본:

```js
let view3 =
  document.querySelector(
    "div#view"
  )
```

뜻:

```text
div 요소이면서 id가 view
```

중복 id가 두 개 있으므로 첫 번째 일치 요소가 반환됩니다.

다시 강조하면 중복 id에 의존해서는 안 됩니다.

---

# 23. 없는 QuerySelector

공통 원본:

```js
let view4 =
  document.querySelector(
    "div#view4"
  )

console.log(view4)
```

일치하는 요소가 없으므로:

```text
null
```

을 반환합니다.

---

# 24. QuerySelectorAll

공통 원본:

```js
let qsa =
  document.querySelectorAll(
    "#view"
  )

console.log(qsa)
```

중복 id 두 요소가 모두 selector와 일치하므로 둘 다 포함된 `NodeList`를 반환할 수 있습니다.

그러나 `id` 중복이 잘못된 구조라는 사실은 변하지 않습니다.

---

# 25. NodeList와 HTMLCollection 차이

| 구분 | 대표 메서드 | 반환 형식 |
| --- | --- | --- |
| `getElementsByTagName()` | tag 검색 | `HTMLCollection` |
| `getElementsByClassName()` | class 검색 | `HTMLCollection` |
| `querySelectorAll()` | CSS selector 검색 | `NodeList` |

`querySelectorAll()`이 반환하는 NodeList는 일반적으로 static collection입니다.

DOM이 바뀌어도 기존 NodeList가 자동 갱신되지 않는 경우가 일반적입니다.

또한 NodeList는 `forEach()`를 사용할 수 있는 환경이 많습니다.

```js
qsa.forEach(
  function(element) {
    console.log(element)
  }
)
```

---

# 26. GetElementById를 제외하면 모두 배열인가?

내 코드 주석:

```text
getElementById를 제외하고는
모두 배열을 돌려줌
```

이 설명은 너무 넓습니다.

정확한 구분:

```text
getElementById()
→ Element 또는 null

getElementsByTagName()
→ HTMLCollection

getElementsByClassName()
→ HTMLCollection

querySelector()
→ Element 또는 null

querySelectorAll()
→ NodeList
```

`querySelector()`도 하나의 Element 또는 null을 반환하므로 배열이나 collection이 아닙니다.

---

# 27. 속성 선택 대상

공통 원본:

```js
let aha =
  document.querySelector(
    "#aha"
  )

console.log(aha)
```

HTML:

```html
<img
  id="aha"
  alt="아하모먼트"
  style="width:100px;"
  src="..."
>
```

이미지 요소를 선택한 뒤 속성 API를 실습합니다.

---

# 28. 외부 이미지 URL

양쪽 원본은 외부 사이트의 긴 이미지 URL을 사용합니다.

주의점:

- 외부 서버 정책에 따라 이미지가 표시되지 않을 수 있음
- URL이 변경되거나 만료될 수 있음
- CORS와 별개로 hotlink 차단이 있을 수 있음
- 학습 파일 재현성이 낮아질 수 있음

실습 프로젝트에서는 로컬 이미지 파일을 사용하는 편이 안정적입니다.

```html
<img
  src="./images/aha.jpg"
  alt="아하모먼트"
>
```

---

# 29. HasAttribute

공통 원본:

```js
let isSrc =
  aha.hasAttribute(
    "src"
  )

console.log(
  "isSrc",
  isSrc
)
```

`src` 속성이 존재하므로:

```text
true
```

를 반환합니다.

Boolean 속성 검사에도 유용합니다.

```js
input.hasAttribute(
  "disabled"
)
```

---

# 30. 속성 존재와 값 구분

다음 요소:

```html
<input disabled>
```

`hasAttribute("disabled")`는 true입니다.

다음도 true입니다.

```html
<input disabled="false">
```

HTML Boolean 속성은 속성이 존재하는지가 중요할 수 있습니다.

문자열 `"false"`가 있다고 자동으로 비활성 해제가 되는 것은 아닙니다.

원본은 속성명 존재 검사만 다룹니다.

---

# 31. GetAttribute

공통 원본:

```js
let src =
  aha.getAttribute(
    "src"
  )

console.log("src", src)
```

HTML에 작성된 `src` 속성값을 문자열로 반환합니다.

---

# 32. 없는 속성 GetAttribute

공통 원본:

```js
let src2 =
  aha.getAttribute(
    "src2"
  )

console.log("src2", src2)
```

없는 속성이므로:

```text
null
```

을 반환합니다.

내 코드의 출력 label:

```js
console.log(
  "src : ",
  src2
)
```

강사님 코드:

```js
console.log(
  "src2",
  src2
)
```

내 코드는 변수는 `src2`인데 출력 label은 `"src"`라서 Console 확인 시 혼동될 수 있습니다.

---

# 33. 속성 Property와 Attribute

HTML attribute:

```js
aha.getAttribute("src")
```

DOM property:

```js
aha.src
```

둘은 관련되어 있지만 항상 같은 문자열 표현을 반환하는 것은 아닙니다.

`aha.src`는 브라우저가 절대 URL로 정규화해 반환할 수 있습니다.

원본은 attribute API만 사용합니다.

---

# 34. SetAttribute

공통 원본:

```js
setTimeout(
  function() {
    aha.setAttribute(
      "src",
      "새 이미지 URL"
    )
  },
  1000 * 2
)
```

약 2초 뒤 이미지의 `src` 속성을 변경합니다.

원래 속성이 있으면 값을 바꾸고, 없으면 새 속성을 추가합니다.

---

# 35. 타이머 실행 순서

script 실행 중:

```text
setTimeout 등록
→ 다음 코드 계속 실행
→ 약 2초 뒤 callback 실행
```

타이머가 2초 동안 전체 script를 멈추는 것은 아닙니다.

이 개념은 JavaScript 08번 타이머 학습과 연결됩니다.

---

# 36. Custom Attribute 추가

공통 원본:

```js
aha.setAttribute(
  "human",
  "교육센터"
)
```

`human`이라는 사용자 정의 attribute를 추가합니다.

브라우저는 임의 attribute를 DOM에 유지할 수 있지만 사용자 정의 데이터는 일반적으로 `data-*`를 사용하는 것이 권장됩니다.

```js
aha.setAttribute(
  "data-human",
  "교육센터"
)
```

접근:

```js
aha.dataset.human
```

---

# 37. RemoveAttribute

공통 원본:

```js
aha.removeAttribute(
  "human"
)
```

앞서 추가한 `human` 속성을 제거합니다.

없는 속성을 제거해도 일반적으로 오류가 발생하지 않습니다.

---

# 38. ClassList

공통 원본:

```js
let div1 =
  document
    .getElementById("div1")

let div2 =
  document
    .getElementById("div2")
```

내 코드는:

```js
document.querySelector(
  "#div1"
)
```

강사님 코드는:

```js
document.getElementById(
  "div1"
)
```

둘 다 같은 요소를 선택합니다.

---

# 39. ClassList 반환값

공통 원본:

```js
console.log(
  div2.classList
)
```

반환값은 `DOMTokenList`입니다.

원본 주석은 class를 배열로 돌려준다고 표현합니다.

정확히는 일반 배열이 아니라 class token 목록을 다루는 전용 객체입니다.

가능한 작업:

```js
div2.classList.length
div2.classList[0]
div2.classList.add("blue")
```

---

# 40. ClassList Add

공통 원본:

```js
div1.classList.add(
  "blue"
)

div1.classList.add(
  "blue"
)
```

같은 class를 두 번 추가해도 중복 token이 만들어지지 않습니다.

최종 class:

```html
class="blue"
```

---

# 41. ClassList Remove

공통 원본:

```js
div1.classList.remove(
  "blue"
)

div1.classList.remove(
  "blue"
)
```

첫 호출에서 class를 제거합니다.

두 번째 호출 시 class가 없어도 오류가 발생하지 않습니다.

---

# 42. ClassList Toggle

공통 원본:

```js
div1.classList.toggle(
  "blue"
)

div1.classList.toggle(
  "blue"
)
```

첫 호출:

```text
blue 없음
→ blue 추가
```

두 번째 호출:

```text
blue 있음
→ blue 제거
```

최종적으로 `blue`가 없는 상태입니다.

---

# 43. Toggle 반환값

`classList.toggle()`은 동작 후 class가 존재하면 true, 없으면 false를 반환합니다.

```js
const result =
  div1.classList.toggle(
    "blue"
  )

console.log(result)
```

원본은 반환값을 저장하지 않지만 UI 상태 확인에 사용할 수 있습니다.

---

# 44. ClassList Contains

공통 원본:

```js
let isBlue =
  div1.classList.contains(
    "blue"
  )

console.log(isBlue)
```

앞서 toggle을 두 번 호출했기 때문에 최종 상태에서 `blue`가 없습니다.

따라서:

```text
false
```

가 반환됩니다.

---

# 45. Contains 오류가 발생하는 경우

`classList.contains()`는 Element 하나의 `classList`에서 사용해야 합니다.

올바른 코드:

```js
const div =
  document.querySelector(
    "#div1"
  )

div.classList.contains(
  "blue"
)
```

잘못된 형태:

```js
const divs =
  document.querySelectorAll(
    "div"
  )

divs.classList.contains(
  "blue"
)
```

`querySelectorAll()`은 NodeList를 반환하므로 NodeList 자체에는 `classList`가 없습니다.

각 요소에 접근해야 합니다.

```js
divs[0]
  .classList
  .contains("blue")
```

---

# 46. Div2에 Blue 추가

공통 원본:

```js
div2.classList.add(
  "blue"
)
```

기존 HTML:

```html
<div
  id="div2"
  class="bg-yellow"
>
  div2
</div>
```

추가 후:

```html
<div
  id="div2"
  class="bg-yellow blue"
>
  div2
</div>
```

배경은 노란색, 글자색은 파란색이 됩니다.

---

# 47. CSS 차이

내 코드:

```css
.blue {
  color: blue;
}

.bg-yellow {
  background-color: yellow;
}
```

강사님 코드:

```css
.blue {
  color: blue
}

.bg-yellow {
  background: yellow;
}
```

차이:

- 강사님 `.blue`의 세미콜론 생략
- 내 코드는 `background-color`
- 강사님 코드는 `background` shorthand

현재 단일 색상에서는 시각적 결과가 같습니다.

---

# 48. Selector 순서 차이

내 코드:

```css
div.pizza,
div#view.pizza,
#view.pizza
```

강사님 코드:

```css
div.pizza,
#view.pizza,
div#view.pizza
```

selector 순서만 다릅니다.

모두 동일한 선언 block을 사용하므로 결과에는 영향이 없습니다.

---

# 49. ID Selector CSS 주석 차이

내 코드:

```text
CSS는 ID가 중복이 되어도 동작시킴
```

강사님 코드:

```css
/* [id=view] */
```

강사님 주석의 `[id=view]`는 attribute selector 예시처럼 보이지만 실제 selector는 `#view`입니다.

다음 둘은 유사한 요소를 선택할 수 있습니다.

```css
#view
```

```css
[id="view"]
```

하지만 의미와 specificity가 다릅니다.

---

# 50. DOM Remove

공통 원본:

```js
div2.remove()
```

해당 요소를 현재 DOM tree에서 제거합니다.

화면에서도 사라집니다.

---

# 51. Remove 설명 검토

내 코드 주석:

```text
remove()로 DOM을 지우면
되돌릴 수 없음
```

정확히는 DOM에서 제거된 뒤에도 JavaScript 변수 `div2`가 요소 객체를 참조하고 있다면 다시 삽입할 수 있습니다.

```js
div2.remove()

document.body.appendChild(
  div2
)
```

따라서 완전히 되돌릴 수 없다고 단정하면 부정확합니다.

다만 원래 위치 정보는 별도로 저장하지 않으면 자동 복원되지 않습니다.

---

# 52. 숨김과 제거 차이

제거:

```js
div2.remove()
```

- DOM tree에서 빠짐
- layout에도 참여하지 않음

숨김:

```js
div2.style.display =
  "none"
```

- DOM tree에는 남아 있음
- 다시 표시하기 쉬움

class 방식:

```css
.hidden {
  display: none;
}
```

```js
div2.classList.add(
  "hidden"
)
```

실무에서는 class 기반 상태 변경을 자주 사용합니다.

---

# 53. Script 실행 후 최종 상태

원본 script가 실행된 직후:

```text
div1
→ blue 추가
→ blue 제거
→ toggle로 추가
→ toggle로 제거
→ 최종 blue 없음

div2
→ blue 추가
→ DOM에서 remove
```

약 2초 후:

```text
aha 이미지의 src 변경
```

`div2`는 이미 DOM에서 제거되어 화면에 보이지 않습니다.

---

# 54. 선택 메서드 비교

| 메서드 | 선택 기준 | 반환값 | 미발견 |
| --- | --- | --- | --- |
| `getElementById()` | id | Element 하나 | `null` |
| `getElementsByTagName()` | tag | HTMLCollection | length 0 |
| `getElementsByClassName()` | class | HTMLCollection | length 0 |
| `querySelector()` | CSS selector | Element 하나 | `null` |
| `querySelectorAll()` | CSS selector | NodeList | length 0 |

---

# 55. 어떤 선택 메서드를 쓸까?

id 하나:

```js
document.getElementById(
  "title"
)
```

복잡한 CSS selector 하나:

```js
document.querySelector(
  "#menu .pizza"
)
```

복수 selector:

```js
document.querySelectorAll(
  ".menu"
)
```

tag 또는 class live collection이 필요한 경우:

```js
document
  .getElementsByClassName(
    "menu"
  )
```

대부분의 현대 코드에서는 `querySelector()`와 `querySelectorAll()`이 일관된 CSS selector 문법 때문에 자주 사용됩니다.

---

# 56. My Code 분석

## 56.1 장점

- DOM과 document의 관계를 강사님보다 상세히 설명했다.
- script가 head에서 너무 일찍 실행되면 null이 될 수 있음을 설명했다.
- 없는 id의 null과 일반 undefined를 구분하려 했다.
- 중복 id에서 첫 요소가 선택되는 현상을 기록했다.
- HTMLCollection을 유사 배열로 설명했다.
- 빈 collection도 truthy라는 점을 실제 조건문으로 확인했다.
- 특정 DOM 내부에서 class 검색이 가능함을 설명했다.
- querySelector가 CSS selector를 사용한다는 점을 상세히 기록했다.
- querySelector와 querySelectorAll 차이를 설명했다.
- 속성 존재·조회·추가·변경·삭제 흐름을 상세히 기록했다.
- `classList`의 add, remove, toggle, contains를 각각 설명했다.
- add 중복 방지와 remove 미존재 안전성을 설명했다.
- DOM 제거와 숨김의 차이를 학습하려는 주석을 추가했다.

## 56.2 개선점

- `getElementById()` 외에는 모두 배열을 반환한다는 설명은 잘못되었다.
- `querySelector()`도 Element 하나 또는 null을 반환한다.
- HTMLCollection, NodeList, DOMTokenList를 일반 배열이라고 표현했다.
- `[object HTMLHeadingElement]`를 heap 주소값이라고 설명한 부분은 부정확하다.
- 중복 id가 HTML 문법상 잘못이라는 설명이 부족하다.
- 빈 collection 존재 여부를 객체 truthy로 검사해 항상 참이 된다.
- `src2`를 출력하면서 label을 `"src"`라고 작성했다.
- custom attribute `human`보다 `data-human`이 적절하다.
- 외부 이미지 URL에 의존한다.
- `contains()` 최종 결과가 false라는 직접 설명이 없다.
- `remove()` 후 되돌릴 수 없다고 단정한 설명은 부정확하다.
- `div2` 선택에 querySelector를 사용하지만 강사님과 기능상 차이는 없다.
- 문서 title과 lang이 학습 내용에 맞지 않는다.

---

# 57. Teacher Code 분석

## 57.1 장점

- DOM과 document를 간결하게 소개한다.
- id, tag, class 선택을 순서대로 실습한다.
- 없는 id는 null, 없는 tag는 length 0 collection임을 구분한다.
- 특정 DOM 내부에서 다시 class를 찾는다.
- querySelector와 querySelectorAll을 비교한다.
- 속성 API 네 가지를 순서대로 실습한다.
- setTimeout으로 이미지 src가 나중에 변경되는 모습을 보여 준다.
- classList add, remove, toggle, contains를 순서대로 실습한다.
- id 선택에는 getElementById를 일관되게 사용한다.
- 마지막에 Element.remove()를 실습한다.

## 57.2 개선점

- 중복 id가 잘못된 HTML이라는 설명이 없다.
- HTMLCollection을 배열이라고 표현한다.
- 빈 collection을 if 조건으로 검사해 항상 참이 된다.
- NodeList와 HTMLCollection의 차이를 설명하지 않는다.
- classList가 DOMTokenList라는 설명이 없다.
- 외부 이미지 URL에 의존한다.
- custom attribute를 `data-*`가 아닌 `human`으로 만든다.
- setTimeout이 정확히 2초 실행을 보장하지 않는다는 설명이 없다.
- DOM remove 후 참조를 이용해 재삽입할 수 있다는 설명이 없다.
- 문서 title과 lang이 학습 내용에 맞지 않는다.

---

# 58. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| DOM 설명 | 상세 | 간결 |
| Script 위치 설명 | 있음 | 없음 |
| `<h1>` 텍스트 | `DOM연습` | `DOM 연습` |
| 음식 이름 | `똠얌꿍` | `똠양꿍` |
| `divs` 출력 | label `"divs"` 포함 | collection만 출력 |
| 특정 DOM 설명 | 상세 | 간결 |
| `div1`, `div2` 선택 | `querySelector()` | `getElementById()` |
| `isSrc` 출력 | `"isSrc : "` | `"isSrc"` |
| 없는 속성 label | `"src"`로 잘못 표기 | `"src2"` |
| CSS 배경 | `background-color` | `background` |
| `.blue` 세미콜론 | 있음 | 생략 |
| Selector 순서 | `div.pizza`, `div#view.pizza`, `#view.pizza` | `div.pizza`, `#view.pizza`, `div#view.pizza` |
| Remove 설명 | 되돌릴 수 없다고 설명 | 설명 없음 |
| 전체 코드 | 주석이 매우 상세 | 핵심 위주 |

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
  <title>DOM 선택과 조작</title>

  <style>
    .blue {
      color: blue;
    }

    .hidden {
      display: none;
    }
  </style>
</head>
<body>
  <h1 id="title">
    DOM 연습
  </h1>

  <ul id="menu">
    <li class="menu-item">
      치킨
    </li>
    <li class="menu-item pizza">
      피자
    </li>
  </ul>

  <div id="box">
    Box
  </div>

  <script>
    "use strict";

    const title =
      document.getElementById(
        "title"
      );

    const pizza =
      document.querySelector(
        "#menu .pizza"
      );

    const menuItems =
      document.querySelectorAll(
        ".menu-item"
      );

    const box =
      document.getElementById(
        "box"
      );

    console.log(title);
    console.log(pizza);

    menuItems.forEach(
      function(item) {
        console.log(item.textContent);
      }
    );

    box.classList.add("blue");

    const isBlue =
      box.classList.contains(
        "blue"
      );

    console.log(isBlue);
  </script>
</body>
</html>
```

---

# 60. 속성 조작 개선 예제

```js
const image =
  document.querySelector(
    "#aha"
  )

if (image !== null) {
  const hasSrc =
    image.hasAttribute(
      "src"
    )

  console.log(hasSrc)

  image.setAttribute(
    "data-human",
    "교육센터"
  )

  console.log(
    image.getAttribute(
      "data-human"
    )
  )

  image.removeAttribute(
    "data-human"
  )
}
```

요소가 null일 가능성을 먼저 확인합니다.

---

# 61. Class 조작 개선 예제

```js
const box =
  document.querySelector(
    "#div1"
  )

if (box !== null) {
  box.classList.add(
    "blue"
  )

  const isBlue =
    box.classList.contains(
      "blue"
    )

  console.log(
    "blue 존재:",
    isBlue
  )

  box.classList.toggle(
    "blue"
  )
}
```

---

# 62. 여러 요소 Class 조작

```js
const menuItems =
  document.querySelectorAll(
    ".menu"
  )

menuItems.forEach(
  function(item) {
    item.classList.add(
      "active"
    )
  }
)
```

NodeList 자체가 아니라 각 Element의 classList를 조작합니다.

---

# 63. 요소 제거와 복원

```js
const div2 =
  document.getElementById(
    "div2"
  )

const parent =
  div2.parentElement

const next =
  div2.nextSibling

div2.remove()

if (next !== null) {
  parent.insertBefore(
    div2,
    next
  )
} else {
  parent.appendChild(
    div2
  )
}
```

원래 위치를 저장하면 제거 후 다시 삽입할 수 있습니다.

---

# 64. 자주 하는 실수

## 64.1 중복 ID 사용

선택 결과가 예측하기 어려워지고 HTML 유효성이 깨집니다.

## 64.2 HTMLCollection을 배열로 생각

`map()` 같은 배열 메서드를 바로 사용할 수 없습니다.

## 64.3 빈 Collection을 If로 검사

객체이므로 length가 0이어도 truthy입니다.

## 64.4 QuerySelectorAll 결과에 ClassList 사용

NodeList에는 classList가 없으며 각 요소에 접근해야 합니다.

## 64.5 GetElementById 미발견 후 바로 조작

null에서 classList를 읽으면 TypeError가 발생합니다.

## 64.6 GetAttribute 미발견값을 문자열로 생각

없는 attribute는 null을 반환합니다.

## 64.7 SetAttribute로 임의 속성 생성

사용자 정의 데이터는 `data-*`가 더 적절합니다.

## 64.8 Remove를 완전 삭제로만 이해

변수 참조가 남아 있다면 다시 삽입할 수 있습니다.

## 64.9 외부 이미지 URL에 의존

URL 변경이나 hotlink 차단으로 실습 결과가 달라질 수 있습니다.

## 64.10 CSS 적용을 HTML 유효성으로 착각

중복 id에 CSS가 적용되어도 중복 id는 잘못된 구조입니다.

---

# 65. 면접·복습 포인트

## Q1. DOM이란 무엇인가요?

HTML 문서를 JavaScript가 접근하고 조작할 수 있는 객체 구조로 표현한 것입니다.

## Q2. `getElementById()`가 요소를 찾지 못하면 무엇을 반환하나요?

null을 반환합니다.

## Q3. `getElementsByClassName()`은 무엇을 반환하나요?

HTMLCollection을 반환합니다.

## Q4. 빈 HTMLCollection이 if 조건에서 참인 이유는 무엇인가요?

length와 관계없이 collection 자체가 객체이기 때문에 truthy입니다.

## Q5. `querySelector()`와 `querySelectorAll()`의 차이는 무엇인가요?

querySelector는 첫 Element 하나 또는 null을 반환하고, querySelectorAll은 모든 일치 요소의 NodeList를 반환합니다.

## Q6. `classList.contains()`는 무엇을 반환하나요?

해당 class가 있으면 true, 없으면 false를 반환합니다.

## Q7. 원본의 `contains("blue")` 결과는 무엇인가요?

toggle을 두 번 호출해 blue가 제거된 상태이므로 false입니다.

## Q8. 중복 id가 있는데 querySelectorAll로 모두 선택되면 문제가 없는 것인가요?

아닙니다. 선택 가능 여부와 무관하게 id는 문서 내에서 고유해야 합니다.

## Q9. `remove()`한 요소는 다시 사용할 수 없나요?

변수가 요소를 참조하고 있으면 다시 DOM에 삽입할 수 있습니다.

## Q10. HTMLCollection과 NodeList는 일반 배열인가요?

아닙니다. 배열과 비슷하게 index와 length를 가질 수 있지만 별도의 collection 객체입니다.

---

# Problems

## 문제 1. ID 선택

`id="title"`인 요소를 선택하고 Console에 출력하세요.

## 문제 2. 없는 ID

없는 id를 선택했을 때 어떤 값이 나오는지 확인하세요.

## 문제 3. Tag 선택

문서의 모든 `<div>`를 선택하고 개수를 출력하세요.

## 문제 4. Class 선택

class `"menu"`를 가진 모든 요소를 선택하세요.

## 문제 5. 빈 Collection 검사

`getElementsByTagName("unknown")` 결과에 실제 요소가 있는지 올바르게 검사하세요.

## 문제 6. 특정 DOM 내부 검색

`#menu` 안에서 class `"pizza"`인 요소를 선택하세요.

## 문제 7. QuerySelector

`id="view"`이면서 class `"pizza"`인 요소를 CSS selector로 선택하세요.

## 문제 8. QuerySelectorAll

class `"menu"`인 모든 요소를 NodeList로 선택하세요.

## 문제 9. NodeList 순회

문제 8의 모든 요소 textContent를 출력하세요.

## 문제 10. 속성 존재 검사

이미지에 `src` 속성이 있는지 검사하세요.

## 문제 11. 속성값 가져오기

이미지의 `alt` 속성값을 가져오세요.

## 문제 12. 속성 추가

이미지에 `data-owner="교육센터"` 속성을 추가하세요.

## 문제 13. 속성 제거

문제 12에서 추가한 속성을 제거하세요.

## 문제 14. Class 추가

`#div1`에 class `"blue"`를 추가하세요.

## 문제 15. Class 중복

같은 class를 두 번 add했을 때 결과를 설명하세요.

## 문제 16. Class 제거

존재하지 않는 class를 remove했을 때의 동작을 설명하세요.

## 문제 17. Toggle

버튼을 누를 때 `"active"` class가 켜지고 꺼지도록 작성하세요.

## 문제 18. Contains

요소에 `"blue"` class가 있는지 Boolean으로 확인하세요.

## 문제 19. Collection 오류

`document.querySelectorAll("div").classList`가 잘못된 이유를 설명하세요.

## 문제 20. DOM 제거

`#div2`를 DOM에서 제거하세요.

## 문제 21. 중복 ID 개선

원본의 두 `id="view"` 요소를 올바른 구조로 수정하세요.

## 문제 22. 종합 카드 제어

다음 요구사항을 만족하세요.

- `.card` 요소 모두 선택
- 각 카드에 `"ready"` class 추가
- `data-index` 속성에 1부터 번호 부여
- `"hidden"` class가 있는 카드는 DOM에서 제거하지 말고 표시만 건너뜀
- 각 카드의 `data-index`와 textContent 출력
- NodeList 자체에 classList를 사용하지 않음
- 요소가 하나도 없으면 별도 메시지 출력

---

# Answers & Explanations

## 정답 1

```js
const title =
  document.getElementById(
    "title"
  )

console.log(title)
```

## 정답 2

```js
const unknown =
  document.getElementById(
    "unknown"
  )

console.log(unknown)
```

결과는 null입니다.

## 정답 3

```js
const divs =
  document.getElementsByTagName(
    "div"
  )

console.log(
  divs.length
)
```

## 정답 4

```js
const menus =
  document
    .getElementsByClassName(
      "menu"
    )

console.log(menus)
```

## 정답 5

```js
const unknowns =
  document.getElementsByTagName(
    "unknown"
  )

if (unknowns.length > 0) {
  console.log("존재")
} else {
  console.log("없음")
}
```

## 정답 6

```js
const menu =
  document.querySelector(
    "#menu"
  )

const pizza =
  menu.querySelector(
    ".pizza"
  )

console.log(pizza)
```

## 정답 7

```js
const view =
  document.querySelector(
    "#view.pizza"
  )

console.log(view)
```

원본 구조에서는 선택되지만 중복 id는 반드시 개선해야 합니다.

## 정답 8

```js
const menus =
  document.querySelectorAll(
    ".menu"
  )
```

## 정답 9

```js
menus.forEach(
  function(menu) {
    console.log(
      menu.textContent
    )
  }
)
```

## 정답 10

```js
const image =
  document.querySelector(
    "img"
  )

const hasSrc =
  image !== null &&
  image.hasAttribute(
    "src"
  )

console.log(hasSrc)
```

## 정답 11

```js
const alt =
  image.getAttribute(
    "alt"
  )

console.log(alt)
```

## 정답 12

```js
image.setAttribute(
  "data-owner",
  "교육센터"
)
```

## 정답 13

```js
image.removeAttribute(
  "data-owner"
)
```

## 정답 14

```js
const div1 =
  document.getElementById(
    "div1"
  )

div1.classList.add(
  "blue"
)
```

## 정답 15

`classList.add()`는 동일한 class token을 중복 저장하지 않습니다. 두 번 호출해도 `"blue"`는 한 번만 존재합니다.

## 정답 16

존재하지 않는 class를 `classList.remove()`로 제거해도 오류가 발생하지 않으며 상태는 그대로입니다.

## 정답 17

```js
const button =
  document.querySelector(
    "button"
  )

button.addEventListener(
  "click",
  function() {
    button.classList.toggle(
      "active"
    )
  }
)
```

## 정답 18

```js
const isBlue =
  div1.classList.contains(
    "blue"
  )

console.log(isBlue)
```

## 정답 19

`querySelectorAll("div")`은 NodeList를 반환합니다. NodeList 자체는 Element가 아니므로 classList가 없습니다. index 또는 반복문으로 각 요소에 접근해야 합니다.

```js
const divs =
  document.querySelectorAll(
    "div"
  )

divs.forEach(
  function(div) {
    div.classList.add(
      "active"
    )
  }
)
```

## 정답 20

```js
const div2 =
  document.getElementById(
    "div2"
  )

if (div2 !== null) {
  div2.remove()
}
```

## 정답 21

```html
<div id="view1">
  첫번째 view
</div>

<div
  id="view2"
  class="pizza"
>
  두번째 view
</div>
```

여러 요소를 같은 종류로 묶으려면 class를 사용할 수도 있습니다.

```html
<div class="view">
<div class="view pizza">
```

## 정답 22

```js
const cards =
  document.querySelectorAll(
    ".card"
  )

if (cards.length === 0) {
  console.log(
    "카드가 없습니다."
  )
} else {
  cards.forEach(
    function(card, index) {
      card.classList.add(
        "ready"
      )

      card.setAttribute(
        "data-index",
        String(index + 1)
      )

      if (
        card.classList.contains(
          "hidden"
        )
      ) {
        return
      }

      console.log(
        "index:",
        card.getAttribute(
          "data-index"
        )
      )

      console.log(
        "text:",
        card.textContent.trim()
      )
    }
  )
}
```

---

# Final Checklist

## DOM 기본

- [ ] DOM과 document의 의미를 이해했다.
- [ ] script 실행 시점과 DOM 파싱 순서를 이해했다.
- [ ] getElementById가 Element 또는 null을 반환함을 확인했다.
- [ ] 객체 문자열 표현이 실제 메모리 주소가 아님을 이해했다.
- [ ] 중복 id를 사용하지 않았다.
- [ ] CSS 적용 여부와 HTML 유효성을 구분했다.

## 선택 메서드

- [ ] getElementsByTagName 결과가 HTMLCollection임을 이해했다.
- [ ] getElementsByClassName 결과가 HTMLCollection임을 이해했다.
- [ ] querySelector 결과가 Element 또는 null임을 이해했다.
- [ ] querySelectorAll 결과가 NodeList임을 이해했다.
- [ ] 빈 collection 존재 여부를 length로 검사했다.
- [ ] 특정 DOM 내부에서 다시 검색했다.
- [ ] HTMLCollection과 NodeList를 일반 배열과 구분했다.
- [ ] 여러 요소 선택 결과에 직접 classList를 사용하지 않았다.

## 속성 조작

- [ ] hasAttribute로 속성 존재 여부를 검사했다.
- [ ] getAttribute 미발견값이 null임을 이해했다.
- [ ] setAttribute로 기존 속성을 변경했다.
- [ ] setAttribute로 새 속성을 추가했다.
- [ ] 사용자 정의 데이터에 data-*를 검토했다.
- [ ] removeAttribute로 속성을 제거했다.
- [ ] 외부 이미지 URL 의존성을 검토했다.

## Class 조작

- [ ] classList가 DOMTokenList임을 이해했다.
- [ ] add가 중복 class를 만들지 않음을 확인했다.
- [ ] remove가 없는 class에도 오류를 내지 않음을 확인했다.
- [ ] toggle로 상태를 반전했다.
- [ ] contains가 Boolean을 반환함을 확인했다.
- [ ] 원본 최종 contains 결과가 false임을 이해했다.

## DOM 제거

- [ ] Element.remove로 DOM tree에서 제거했다.
- [ ] 제거와 display none 숨김을 구분했다.
- [ ] 변수 참조가 남으면 다시 삽입할 수 있음을 이해했다.
- [ ] 원래 위치 복원에는 위치 정보가 필요함을 이해했다.

## 원본 코드 검수

- [ ] 두 실제 11_dom.html 원본만 비교했다.
- [ ] 내 코드의 script 위치 설명을 기록했다.
- [ ] `DOM연습`과 `DOM 연습` 텍스트 차이를 기록했다.
- [ ] `똠얌꿍`과 `똠양꿍` 문자열 차이를 기록했다.
- [ ] 중복 id 문제를 기록했다.
- [ ] 빈 HTMLCollection이 truthy임을 기록했다.
- [ ] 내 `getElementById 외 모두 배열` 설명 오류를 기록했다.
- [ ] 내 `[object HTMLHeadingElement]` 주소 설명 오류를 기록했다.
- [ ] 내 src2 Console label 오류를 기록했다.
- [ ] div1·div2 선택 메서드 차이를 기록했다.
- [ ] classList를 배열이라 부른 표현을 보완했다.
- [ ] remove 후 재삽입 가능성을 기록했다.
- [ ] CSS shorthand와 세미콜론 차이를 기록했다.
- [ ] 외부 이미지 URL 사용을 기록했다.

---

# Key Summary

- DOM은 HTML 문서를 JavaScript가 접근하고 조작할 수 있는 객체 구조로 표현한 것이다.
- `document`는 현재 문서 전체를 나타내는 최상위 DOM 객체다.
- script가 DOM보다 먼저 실행되면 요소 선택 결과가 null일 수 있다.
- 현재 원본 script는 body 마지막에 있어 앞 요소가 파싱된 뒤 실행된다.
- `getElementById()`는 Element 하나 또는 null을 반환한다.
- `"" + element`의 `[object HTMLHeadingElement]`는 실제 메모리 주소가 아니다.
- 같은 id를 여러 요소에 사용하는 것은 잘못된 HTML 구조다.
- CSS가 중복 id 모두에 적용될 수 있어도 중복 id가 유효해지는 것은 아니다.
- `getElementsByTagName()`과 `getElementsByClassName()`은 HTMLCollection을 반환한다.
- HTMLCollection은 index와 length가 있지만 일반 배열은 아니다.
- 요소가 하나도 없어도 빈 HTMLCollection 객체는 truthy다.
- 존재 여부는 `collection.length > 0`으로 검사해야 한다.
- 특정 Element에서도 tag, class, query selector 검색을 다시 수행할 수 있다.
- `querySelector()`는 첫 일치 Element 또는 null을 반환한다.
- `querySelectorAll()`은 모든 일치 요소의 NodeList를 반환한다.
- `getElementById()` 외 모두 배열을 반환한다는 내 설명은 잘못되었다.
- HTMLCollection, NodeList, DOMTokenList는 각각 일반 배열과 다른 전용 collection 객체다.
- `hasAttribute()`는 속성 존재 여부를 Boolean으로 반환한다.
- `getAttribute()`는 속성값 문자열 또는 null을 반환한다.
- 내 코드는 `src2` 값을 출력하면서 label을 `"src"`라고 잘못 작성했다.
- `setAttribute()`는 기존 속성을 바꾸거나 새 속성을 만든다.
- 사용자 정의 데이터는 일반 임의 속성보다 `data-*` 사용이 적절하다.
- `removeAttribute()`는 해당 속성을 제거한다.
- `classList.add()`는 같은 class를 중복으로 추가하지 않는다.
- `classList.remove()`는 class가 없어도 오류를 내지 않는다.
- `classList.toggle()`은 class 존재 상태를 반전한다.
- 원본에서 toggle을 두 번 실행한 뒤 `contains("blue")` 결과는 false다.
- `querySelectorAll()` 결과 NodeList 자체에는 classList가 없다.
- 각 NodeList 요소에 접근한 뒤 classList를 사용해야 한다.
- `div2.remove()`는 요소를 DOM tree에서 제거한다.
- 내 코드의 “remove 후 되돌릴 수 없음” 설명은 부정확하다.
- JavaScript 변수가 요소를 참조하고 있으면 제거 후 다시 삽입할 수 있다.
- 양쪽 원본은 외부 이미지 URL을 사용해 재현성이 떨어질 수 있다.
