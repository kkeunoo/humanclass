---
title: JavaScript DOM 선택과 속성·클래스 조작
version: v4.0-detailed-source
last_updated: 2026-09-17
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
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> DOM 요소를 선택하고 속성·클래스·노드를 조작하는 데 필요한 핵심 코드만 발췌하고, 반환 자료형과 실행 시점까지 함께 설명한다.

---

## 이 문서에서 바로 찾기

- [개념에서 실제 실행까지: DOM은 브라우저가 만든 문서 객체이며 선택자는 그 객체를 찾는다](#js-11-section-4)
- [65. 내 코드와 강사님 코드 비교](#js-11-section-69)
- [67. 실무형 예제: 메뉴 선택 상태 관리](#js-11-section-71)
- [68. 대표 오류로 이해하기](#js-11-section-72)
- [69. 자주 하는 실수](#js-11-section-73)
- [70. 핵심 요약](#js-11-section-74)
- [71. 최종 체크리스트](#js-11-section-75)

<details>
<summary>세부 목차 펼치기 — 번호형 본문 전체</summary>

- [개요](#js-11-section-1)
- [핵심 개념](#js-11-section-2)
- [학습 목표](#js-11-section-3)
- [개념에서 실제 실행까지: DOM은 브라우저가 만든 문서 객체이며 선택자는 그 객체를 찾는다](#js-11-section-4)
- [1. DOM](#js-11-section-5)
- [2. `document`](#js-11-section-6)
- [3. Element와 Node](#js-11-section-7)
- [4. 객체를 문자열로 연결](#js-11-section-8)
- [5. `getElementById()`](#js-11-section-9)
- [6. 요소를 찾지 못한 경우](#js-11-section-10)
- [7. `null` 안전 처리](#js-11-section-11)
- [8. 중복 `id`](#js-11-section-12)
- [9. 중복 `id`에서 선택 결과](#js-11-section-13)
- [10. `getElementsByTagName()`](#js-11-section-14)
- [11. 빈 `HTMLCollection`](#js-11-section-15)
- [12. 빈 컬렉션도 Truthy](#js-11-section-16)
- [13. `getElementsByClassName()`](#js-11-section-17)
- [14. 여러 클래스가 있는 요소](#js-11-section-18)
- [15. 특정 요소 내부 검색](#js-11-section-19)
- [16. 원본의 한글 `id`](#js-11-section-20)
- [17. `querySelector()`](#js-11-section-21)
- [18. `querySelector()` 결과 없음](#js-11-section-22)
- [19. CSS 선택자 활용](#js-11-section-23)
- [20. `querySelectorAll()`](#js-11-section-24)
- [21. 빈 `NodeList`](#js-11-section-25)
- [22. `NodeList` 순회](#js-11-section-26)
- [23. `HTMLCollection` 순회](#js-11-section-27)
- [24. HTMLCollection과 NodeList](#js-11-section-28)
- [25. Live collection](#js-11-section-29)
- [26. Static NodeList](#js-11-section-30)
- [27. 선택 메서드 기준](#js-11-section-31)
- [28. 속성 선택 대상](#js-11-section-32)
- [29. `hasAttribute()`](#js-11-section-33)
- [30. `getAttribute()`](#js-11-section-34)
- [31. 없는 속성 조회](#js-11-section-35)
- [32. `setAttribute()`](#js-11-section-36)
- [33. 사용자 정의 속성](#js-11-section-37)
- [34. `dataset`](#js-11-section-38)
- [35. `removeAttribute()`](#js-11-section-39)
- [36. 속성 property 접근](#js-11-section-40)
- [37. Attribute와 Property](#js-11-section-41)
- [38. Boolean 속성](#js-11-section-42)
- [39. 이미지 `src` 변경](#js-11-section-43)
- [40. 외부 이미지 URL 주의](#js-11-section-44)
- [41. 이미지 변경 예제](#js-11-section-45)
- [42. `classList`](#js-11-section-46)
- [43. `classList.add()`](#js-11-section-47)
- [44. 여러 클래스 추가](#js-11-section-48)
- [45. `classList.remove()`](#js-11-section-49)
- [46. `classList.toggle()`](#js-11-section-50)
- [47. `toggle()` 반환값](#js-11-section-51)
- [48. 강제 토글](#js-11-section-52)
- [49. `classList.contains()`](#js-11-section-53)
- [50. Contains 후 직접 Add·Remove](#js-11-section-54)
- [51. `className`과 `classList`](#js-11-section-55)
- [52. 요소 제거 `remove()`](#js-11-section-56)
- [53. `remove()` 후 객체 참조](#js-11-section-57)
- [54. 삭제와 숨김](#js-11-section-58)
- [55. `hidden` property](#js-11-section-59)
- [56. CSS 클래스 기반 숨김](#js-11-section-60)
- [57. 스크립트 실행 시점](#js-11-section-61)
- [58. Body 끝에 Script 배치](#js-11-section-62)
- [59. `defer`](#js-11-section-63)
- [60. `DOMContentLoaded`](#js-11-section-64)
- [61. 안전한 선택 함수](#js-11-section-65)
- [62. 선택 결과 변수명](#js-11-section-66)
- [63. 원본 HTML 개선](#js-11-section-67)
- [64. 원본 선택 코드 개선](#js-11-section-68)
- [65. 내 코드와 강사님 코드 비교](#js-11-section-69)
- [66. 기존 코드에서 개선 코드로 바꾼 이유](#js-11-section-70)
- [67. 실무형 예제: 메뉴 선택 상태 관리](#js-11-section-71)
- [68. 대표 오류로 이해하기](#js-11-section-72)
- [69. 자주 하는 실수](#js-11-section-73)
- [70. 핵심 요약](#js-11-section-74)
- [71. 최종 체크리스트](#js-11-section-75)
- [마무리](#js-11-section-76)
- [V3 실행 추적 카드 — CSS 선택자 → Element/null → 속성·클래스 변경](#js-11-section-77)

</details>

---

<a id="js-11-section-1"></a>

## 개요

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

<a id="js-11-section-2"></a>

## 핵심 개념

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

<a id="js-11-section-3"></a>

## 학습 목표

- 선택 결과의 자료형과 null 원인을 추적한다.
- 원본의 해당 부분을 찾아 실행 순서와 결과를 다시 확인한다.

---

<a id="js-11-section-4"></a>

## 개념에서 실제 실행까지: DOM은 브라우저가 만든 문서 객체이며 선택자는 그 객체를 찾는다

HTML 문자열은 파싱 과정에서 요소·텍스트 노드로 만들어진다. document는 문서 객체이고 선택 함수는 이미 만들어진 노드에 접근한다. script가 해당 HTML보다 먼저 실행되면 아직 노드가 없어서 null을 받는다. 선택자 오타와 로딩 시점 오류는 결과는 같아도 원인은 다르다.

두 원본 모두 id=view를 두 번 써 선택 방식 차이를 실험한다. getElementById와 querySelector는 첫 일치 요소, querySelectorAll은 일치 목록을 준다. 이는 ID 중복을 정상 설계로 허용한다는 뜻이 아니다. 실제 문서에서는 고유 ID를 사용한다. getElementsByClassName/TagName의 HTMLCollection, querySelectorAll의 정적 NodeList는 Array와 다르다.

내 원본의 ''+title 결과 [object HTMLHeadingElement]는 객체 문자열 표현이지 실제 Heap 주소가 아니다. classList도 배열이 아니라 DOMTokenList다. remove한 요소는 DOM에서 분리되지만 참조가 남으면 다시 append할 수 있다. '절대 되돌릴 수 없음'과는 다르다.

### 수업 원본에서 사용한 부분

아래는 전체 실행 파일이 아니라 **개념에 대응하는 문맥 발췌**다. 나머지 HTML·선언·등록 코드는 원본과 기존 번호형 본문에서 이어 확인한다. 

내 코드: `workspace_html/javascript/11_dom.html`

```javascript
// html body에 있는 h1이 가져와진 것
            const title = document.getElementById('title')
            console.log(title)
            // [object HTMLHeadingElement] 가 나오는데, heap영역의 주소값이 나옴
            // javascript는 주소값을 가려서 보여주기 때문에 위 멘트로 나옴
            console.log(''+title)

            // 아래처럼 없는 id 등 선언되지 않은 것을 불러오면 'null = 주소값이 없다'
```

강사님 코드: `workspace_teacher/workspace_html/javascript/11_dom.html`

```javascript
// id 속성으로 DOM을 가져오기
        const title = document.getElementById('title')
        console.log(title)
        console.log(''+title)

        // 없으면 null
        const title2 = document.getElementById('title2')
        console.log(title2)
```

### 직접 재현하는 최소 예제와 결과

이 예제는 **이번 리팩토링의 설명용 재구성**이다. 원본 그대로의 발췌와 구별한다. 브라우저 Console에서 실행한다. 다른 예제의 변수와 섞이지 않게 새 실행 문맥에서 실행한다.

```javascript
const title = document.getElementById("title");
console.log(title?.tagName);
console.log(document.getElementById("missing"));
console.log(document.querySelectorAll(".menu").length);
console.log(Array.isArray(document.querySelectorAll(".menu")));
console.log(Boolean(document.querySelectorAll(".missing")));
```

예상 출력:

```text
H1
null
3
false
true
```

### 결과를 역추적하는 방법

원본 11_dom.html의 body가 만들어진 후 실행하는 Console 예제다. 강사님 파일은 메뉴 목록이 하나 더 있어 .menu가6개다. 빈 목록도 객체이므로 Truthy다. 존재 여부는 단일 요소의 null, 목록의 length를 각각 검사한다.

출력은 아래의 확인 경로로 추적한다. return 값은 호출자에게 전달되고 자동으로 화면에 표시되지 않는다. Console 로그, DOM 변경, 저장소 변경, 서버 응답은 별개 단계다.

| 확인할 단계 | 이 예제에서 볼 것 |
| --- | --- |
| 입력 | 리터럴·현재 폼 값·이벤트 인수·응답 중 출처를 위 설명과 대조 |
| 실행 | 각 줄 또는 콜백이 지금 실행되는지, 나중에 실행되는지 구분 |
| 결과 | 위 예상 출력과 현재 값·자료형을 함께 대조 |
| 오류 | 첫 오류 줄의 입력과 직전 상태를 확인하고 뒤 로그 누락 원인 추적 |

### 단계별 복습 실습과 정답

**기본 실습:** 메뉴 요소를 나중에 하나 추가했을 때 live HTMLCollection과 querySelectorAll 목록을 비교한다.

**응용·디버깅 실습:** querySelector가null일 때 우선 점검할3가지를 적는다.

**통합 확인:** 위 최소 예제를 새 문맥에서 작성하고 정상값·빈 값·경계값으로 실행한다. 원본에서 대응하는 선언·호출·콜백을 찾아 위에 나타난 차이가 무엇을 바꾸는지 설명한다. 아래 정답은 먼저 예측한 뒤 펼친다. 이 실습은 💡 설명용 보강이며 원본에 모두 완성되어 있다는 뜻은 아니다.

<details>
<summary>정답과 처리 순서 해설</summary>

1. 기존 HTMLCollection은 추가를 반영하고 querySelectorAll의 정적 NodeList는 다시 조회해야 한다.
2. 선택자 철자, 해당 HTML 존재, script 실행 시점이다. 선택자문법 자체가 잘못되면 null이 아니라SyntaxError일 수도 있다.
3. 최소 예제의 예상 출력과 한 줄씩 대조한다. 값이 다른 경우 입력 → 형 변환 → 분기/상태 변경 → 출력 순서로 첫 차이를 찾는다. DOM·API 예제는 Console 값만 아니라 화면·Elements·Network가 서로 같은 상태를 말하는지도 점검한다.

</details>

### 복습 질문과 해설

**질문:** classList.add("blue")를 두 번 하면 class에 blue가 두 개 생길까?

**해설:** 아니다. 토큰은 중복되지 않는다. toggle의 반환값은 실행 뒤 해당 클래스 존재 여부다.

**한 번 더 확인:** 예제의 입력을 하나 바꾸고 결과를 먼저 예상한 뒤 실행한다. 정상 입력만 아니라 비어 있는 값, 경계값, 두 번 실행했을 때의 상태를 기존 실습·오류 절에서 반복 확인한다.

---

<a id="js-11-section-5"></a>

## 1. DOM

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

<a id="js-11-section-6"></a>

## 2. `document`

```javascript
console.log(document)
```

현재 브라우저 문서 전체를 나타내는 객체다.

`document`를 시작점으로 요소 검색·생성·변경을 수행한다.

---

<a id="js-11-section-7"></a>

## 3. Element와 Node

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

<a id="js-11-section-8"></a>

## 4. 객체를 문자열로 연결

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

<a id="js-11-section-9"></a>

## 5. `getElementById()`

```javascript
const title = document.getElementById(
    "title",
)
```

지정한 `id`와 일치하는 요소 하나를 반환한다.

---

<a id="js-11-section-10"></a>

## 6. 요소를 찾지 못한 경우

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

<a id="js-11-section-11"></a>

## 7. `null` 안전 처리

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

<a id="js-11-section-12"></a>

## 8. 중복 `id`

원본 HTML에는 다음 구조가 있다.

```html
<div id="view">첫 번째 view</div>
<div id="view" class="pizza">두 번째 view</div>
```

`id`는 문서 안에서 고유해야 한다.

> [!WARNING]
> CSS와 JavaScript가 중복 `id`에서도 일부 동작할 수 있지만 유효한 HTML 구조가 아니다.

---

<a id="js-11-section-13"></a>

## 9. 중복 `id`에서 선택 결과

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

<a id="js-11-section-14"></a>

## 10. `getElementsByTagName()`

```javascript
const divs = document.getElementsByTagName(
    "div",
)

console.log(divs)
```

일치하는 모든 태그를 `HTMLCollection`으로 반환한다.

---

<a id="js-11-section-15"></a>

## 11. 빈 `HTMLCollection`

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

<a id="js-11-section-16"></a>

## 12. 빈 컬렉션도 Truthy

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

<a id="js-11-section-17"></a>

## 13. `getElementsByClassName()`

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

<a id="js-11-section-18"></a>

## 14. 여러 클래스가 있는 요소

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

<a id="js-11-section-19"></a>

## 15. 특정 요소 내부 검색

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

<a id="js-11-section-20"></a>

## 16. 원본의 한글 `id`

원본:

```html
<ul id="메뉴">
```

문법적으로 가능하지만 실무에서는 도구·협업·일관성을 위해 영문 이름을 자주 사용한다.

```html
<ul id="menu">
```

---

<a id="js-11-section-21"></a>

## 17. `querySelector()`

```javascript
const pizzaView = document.querySelector(
    "#view.pizza",
)
```

CSS 선택자를 사용해 첫 번째 일치 요소 하나를 반환한다.

---

<a id="js-11-section-22"></a>

## 18. `querySelector()` 결과 없음

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

<a id="js-11-section-23"></a>

## 19. CSS 선택자 활용

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

<a id="js-11-section-24"></a>

## 20. `querySelectorAll()`

```javascript
const views = document.querySelectorAll(
    "#view",
)

console.log(views)
```

일치하는 모든 요소를 `NodeList`로 반환한다.

중복 `id` 검색도 기술적으로 결과가 여러 개 나올 수 있지만 HTML 구조는 먼저 수정해야 한다.

---

<a id="js-11-section-25"></a>

## 21. 빈 `NodeList`

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

<a id="js-11-section-26"></a>

## 22. `NodeList` 순회

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

<a id="js-11-section-27"></a>

## 23. `HTMLCollection` 순회

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

<a id="js-11-section-28"></a>

## 24. HTMLCollection과 NodeList

| 항목 | `HTMLCollection` | `NodeList` |
| --- | --- | --- |
| 대표 반환 | `getElementsBy...()` | `querySelectorAll()` |
| 내용 | Element 중심 | Node 또는 Element |
| Live 여부 | 대표적으로 live | `querySelectorAll()`은 static |
| `forEach()` | 일반적으로 없음 | 보통 사용 가능 |
| 인덱스 접근 | 가능 | 가능 |

---

<a id="js-11-section-29"></a>

## 25. Live collection

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

<a id="js-11-section-30"></a>

## 26. Static NodeList

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

<a id="js-11-section-31"></a>

## 27. 선택 메서드 기준

| 목적 | 권장 |
| --- | --- |
| 고유 `id` 하나 | `getElementById()` |
| CSS 선택자 하나 | `querySelector()` |
| CSS 선택자 여러 개 | `querySelectorAll()` |
| live 태그 목록 필요 | `getElementsByTagName()` |
| live 클래스 목록 필요 | `getElementsByClassName()` |

일반적인 화면 코드에서는 `querySelector()`와 `querySelectorAll()`이 일관된 선택자 문법 때문에 자주 사용된다.

---

<a id="js-11-section-32"></a>

## 28. 속성 선택 대상

```javascript
const image = document.querySelector(
    "#aha",
)

console.log(image)
```

속성을 읽기 전에 요소가 실제로 존재하는지 확인한다.

---

<a id="js-11-section-33"></a>

## 29. `hasAttribute()`

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

<a id="js-11-section-34"></a>

## 30. `getAttribute()`

```javascript
const src = image.getAttribute(
    "src",
)

console.log(src)
```

HTML에 작성된 속성값을 문자열로 반환한다.

---

<a id="js-11-section-35"></a>

## 31. 없는 속성 조회

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

<a id="js-11-section-36"></a>

## 32. `setAttribute()`

```javascript
image.setAttribute(
    "data-center",
    "교육센터",
)
```

기존 속성이 있으면 값을 바꾸고, 없으면 새 속성을 만든다.

---

<a id="js-11-section-37"></a>

## 33. 사용자 정의 속성

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

<a id="js-11-section-38"></a>

## 34. `dataset`

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

<a id="js-11-section-39"></a>

## 35. `removeAttribute()`

```javascript
image.removeAttribute(
    "data-center",
)
```

지정한 속성을 제거한다.

속성이 없어도 일반적으로 오류가 발생하지 않는다.

---

<a id="js-11-section-40"></a>

## 36. 속성 property 접근

일부 표준 속성은 객체 property로도 접근할 수 있다.

```javascript
console.log(image.src)
console.log(image.alt)

image.alt = "변경된 설명"
```

---

<a id="js-11-section-41"></a>

## 37. Attribute와 Property

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

<a id="js-11-section-42"></a>

## 38. Boolean 속성

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

<a id="js-11-section-43"></a>

## 39. 이미지 `src` 변경

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

<a id="js-11-section-44"></a>

## 40. 외부 이미지 URL 주의

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

<a id="js-11-section-45"></a>

## 41. 이미지 변경 예제

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

<a id="js-11-section-46"></a>

## 42. `classList`

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

<a id="js-11-section-47"></a>

## 43. `classList.add()`

```javascript
div1.classList.add(
    "blue",
)
```

클래스를 추가한다.

같은 클래스를 다시 추가해도 중복 저장되지 않는다.

---

<a id="js-11-section-48"></a>

## 44. 여러 클래스 추가

```javascript
div1.classList.add(
    "blue",
    "bg-yellow",
)
```

여러 클래스를 한 번에 추가할 수 있다.

---

<a id="js-11-section-49"></a>

## 45. `classList.remove()`

```javascript
div1.classList.remove(
    "blue",
)
```

클래스를 제거한다.

없는 클래스를 제거해도 일반적으로 오류가 발생하지 않는다.

---

<a id="js-11-section-50"></a>

## 46. `classList.toggle()`

```javascript
div1.classList.toggle(
    "blue",
)
```

클래스가 있으면 제거하고 없으면 추가한다.

---

<a id="js-11-section-51"></a>

## 47. `toggle()` 반환값

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

<a id="js-11-section-52"></a>

## 48. 강제 토글

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

<a id="js-11-section-53"></a>

## 49. `classList.contains()`

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

<a id="js-11-section-54"></a>

## 50. Contains 후 직접 Add·Remove

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

<a id="js-11-section-55"></a>

## 51. `className`과 `classList`

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

<a id="js-11-section-56"></a>

## 52. 요소 제거 `remove()`

```javascript
div2.remove()
```

현재 DOM 트리에서 요소를 제거한다.

---

<a id="js-11-section-57"></a>

## 53. `remove()` 후 객체 참조

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

<a id="js-11-section-58"></a>

## 54. 삭제와 숨김

| 목적 | 방법 |
| --- | --- |
| 화면에서만 잠시 숨김 | `hidden`, CSS 클래스 |
| 접근성 트리까지 숨김 | 상황에 맞는 `hidden`, `aria-*` |
| DOM 구조에서 제거 | `remove()` |
| 나중에 재삽입 | 참조 저장 후 `append()` |

---

<a id="js-11-section-59"></a>

## 55. `hidden` property

```javascript
div2.hidden = true
```

다시 표시:

```javascript
div2.hidden = false
```

단순 표시·숨김에는 요소 제거보다 의도가 명확할 수 있다.

---

<a id="js-11-section-60"></a>

## 56. CSS 클래스 기반 숨김

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

<a id="js-11-section-61"></a>

## 57. 스크립트 실행 시점

원본 주석:

```text
script가 head에 있으면
HTML 로딩 전에 실행되어
선택 결과가 null일 수 있음
```

HTML 파싱 전에 요소를 선택하면 아직 DOM에 존재하지 않는다.

---

<a id="js-11-section-62"></a>

## 58. Body 끝에 Script 배치

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

<a id="js-11-section-63"></a>

## 59. `defer`

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

<a id="js-11-section-64"></a>

## 60. `DOMContentLoaded`

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

<a id="js-11-section-65"></a>

## 61. 안전한 선택 함수

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

<a id="js-11-section-66"></a>

## 62. 선택 결과 변수명

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

<a id="js-11-section-67"></a>

## 63. 원본 HTML 개선

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

<a id="js-11-section-68"></a>

## 64. 원본 선택 코드 개선

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

<a id="js-11-section-69"></a>

## 65. 내 코드와 강사님 코드 비교

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

### 65-1. 내 코드의 장점

- DOM과 `document`의 관계를 상세히 기록했다.
- 단일 선택 실패와 컬렉션 실패의 차이를 설명했다.
- 특정 DOM 내부에서 다시 검색하는 방식을 확인했다.
- 속성·클래스 메서드의 동작을 자세히 기록했다.
- 스크립트 위치에 따라 `null`이 발생할 수 있음을 설명했다.

### 65-2. 내 코드의 개선점

- 중복 `id`가 잘못된 HTML 구조임을 더 명확히 해야 한다.
- `HTMLCollection`을 배열이라고 설명한 부분을 수정해야 한다.
- 빈 컬렉션은 Truthy이므로 객체 존재 검사만으로 결과 유무를 판단할 수 없다.
- 사용자 정의 속성은 `data-*` 형식을 사용하는 편이 좋다.
- 외부 이미지 URL 의존을 줄여야 한다.
- `remove()` 후 변수 참조가 있으면 재삽입할 수 있다.
- 전역 변수 선언에 `let`보다 `const`를 사용할 수 있는 곳이 많다.

### 65-3. 강사님 코드의 장점

- DOM 선택부터 속성·클래스 조작까지 한 흐름으로 구성되어 있다.
- 두 메뉴 목록을 사용해 문서 전체 선택과 내부 선택을 비교할 수 있다.
- 선택 메서드별 반환 형태를 직접 확인할 수 있다.
- `classList` 핵심 기능을 간결하게 실습한다.

### 65-4. 강사님 코드의 보충점

- 중복 `id`의 HTML 유효성 문제를 설명할 필요가 있다.
- `HTMLCollection`과 `NodeList`의 차이를 보충할 수 있다.
- live collection과 static collection 차이를 설명할 필요가 있다.
- 속성 property와 attribute의 차이를 보충할 수 있다.
- 요소 제거와 숨김의 선택 기준을 설명할 수 있다.
- `defer`를 이용한 외부 스크립트 실행 방식을 추가할 수 있다.

---

<a id="js-11-section-70"></a>

## 66. 기존 코드에서 개선 코드로 바꾼 이유

### 66-1. 중복 ID 제거

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

### 66-2. 컬렉션 존재 검사

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

### 66-3. 사용자 정의 속성

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

### 66-4. 요소 숨김

기존:

```javascript
element.remove()
```

잠시 숨기는 목적:

```javascript
element.hidden = true
```

---

<a id="js-11-section-71"></a>

## 67. 실무형 예제: 메뉴 선택 상태 관리

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

### 67-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `querySelectorAll()` | 여러 메뉴 요소 선택 |
| `forEach()` | 각 요소에 동일 작업 수행 |
| `classList.toggle(force)` | 선택된 요소만 클래스 유지 |
| `setAttribute()` | 접근성 상태 동기화 |
| 요소 비교 | 클릭한 요소인지 확인 |
| 이벤트 콜백 | 사용자 클릭 후 상태 변경 |

---

<a id="js-11-section-72"></a>

## 68. 대표 오류로 이해하기

### 68-1. 선택 결과가 `null`

존재하지 않는 요소에 `classList`를 사용하면 `TypeError`가 발생한다.

<a id="index-section-90"></a>

### 68-2. 빈 컬렉션을 `false`로 예상

빈 객체이므로 Truthy다.

<a id="index-section-91"></a>

### 68-3. HTMLCollection에서 `forEach()` 호출

환경에 따라 메서드가 없어 `TypeError`가 발생할 수 있다.

### 68-4. 중복 ID 선택

첫 번째 요소만 선택되어 다른 요소가 무시될 수 있다.

### 68-5. Head Script에서 즉시 선택

HTML 파싱 전이면 `null`이다.

### 68-6. 요소 제거 후 다시 선택

DOM에서 삭제되었으므로 같은 선택자로 찾을 수 없다.

---

<a id="js-11-section-73"></a>

## 69. 자주 하는 실수

### 69-1. 모든 선택 메서드가 배열을 반환한다고 생각

단일 Element·`null`·`HTMLCollection`·`NodeList`가 서로 다르다.

### 69-2. 빈 컬렉션을 Falsy라고 생각

객체 자체는 Truthy다.

### 69-3. `id`를 여러 요소에 사용

문서 내 고유해야 한다.

### 69-4. `querySelector()`가 모든 요소를 반환한다고 생각

첫 번째 요소 하나만 반환한다.

### 69-5. `querySelectorAll()`이 live라고 생각

일반적으로 static `NodeList`다.

### 69-6. `classList`를 실제 배열이라고 생각

`DOMTokenList`다.

### 69-7. `setAttribute()`만 모든 상태에 사용

표준 DOM property가 더 적합한 경우가 있다.

### 69-8. `remove()`와 숨김을 같은 기능으로 이해

DOM 삭제와 표시 상태 변경은 다르다.

### 69-9. 외부 이미지 URL을 영구 경로로 생각

언제든 바뀌거나 차단될 수 있다.

### 69-10. Script 실행 시점을 고려하지 않음

선택 대상이 아직 파싱되지 않았을 수 있다.

---

<a id="js-11-section-74"></a>

## 70. 핵심 요약

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

<a id="js-11-section-75"></a>

## 71. 최종 체크리스트

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

<a id="js-11-section-76"></a>

## 마무리

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
<a id="js-11-section-77"></a>

## V3 실행 추적 카드 — CSS 선택자 → Element/null → 속성·클래스 변경

`querySelector`는 첫 Element 또는 `null`을 반환한다. script가 요소보다 먼저 실행되거나 선택자가 틀리면 `null`이고 속성 접근 시 TypeError가 난다.

`const box=document.querySelector("#box"); box.classList.add("active");` 실행 뒤 Elements 패널에서 class가 추가되고 CSS가 있으면 화면도 변한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/11_dom.html`에서 실제 사용 위치와 차이를 확인한다.
