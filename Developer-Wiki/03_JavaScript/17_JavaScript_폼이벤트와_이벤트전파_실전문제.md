---
title: JavaScript 폼 이벤트와 이벤트 전파·실전 문제
version: v4.0-detailed-source
last_updated: 2026-09-17
status: Completed
---

# JavaScript 폼 이벤트와 이벤트 전파·실전 문제

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `17_JavaScript_폼이벤트와_이벤트전파_실전문제.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/17_event_form.html`, `workspace_html/javascript/asset/js/17_event_form.js`, 강사님 동일 파일 |
| 핵심 범위 | `focus`, `blur`, `input`, `submit`, Event Propagation, `target`, `currentTarget`, `this`, `stopPropagation()`, Event Delegation |
| 실습 범위 | 검색 Form 검증, 주문·배송 복사, 로그인, 피자 주문 계산, 메뉴 선택, Todo List |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 17번은 폼 이벤트와 이벤트 전파를 학습한 뒤 다섯 개의 실전 문제로 연결한다.  
> 강사님 원본은 기본 이벤트 예제와 문제 요구사항을 제공하고, 내 원본은 문제 1~5를 직접 구현했다. 이 문서에서는 실제 구현 오류와 개선 방향을 함께 정리한다.

---

## 이 문서에서 바로 찾기

- [개념에서 실제 실행까지: 폼 제출과 이벤트 전파는 서로 다른 처리 흐름이다](#js-17-section-4)
- [26. Event 제어 비교](#js-17-section-30)
- [66. 내 코드와 강사님 코드 비교](#js-17-section-70)
- [68. 실무형 예제: 위임 기반 Todo Component](#js-17-section-72)
- [69. 대표 오류로 이해하기](#js-17-section-73)
- [70. 자주 하는 실수](#js-17-section-74)
- [71. 핵심 요약](#js-17-section-75)
- [72. 최종 체크리스트](#js-17-section-76)

<details>
<summary>세부 목차 펼치기 — 번호형 본문 전체</summary>

- [개요](#js-17-section-1)
- [핵심 개념](#js-17-section-2)
- [학습 목표](#js-17-section-3)
- [개념에서 실제 실행까지: 폼 제출과 이벤트 전파는 서로 다른 처리 흐름이다](#js-17-section-4)
- [1. 원본 실행 구조](#js-17-section-5)
- [2. 여러 Load Listener](#js-17-section-6)
- [3. 초기화 통합](#js-17-section-7)
- [4. `focus`](#js-17-section-8)
- [5. `blur`](#js-17-section-9)
- [6. Style 직접 변경 개선](#js-17-section-10)
- [7. `input`](#js-17-section-11)
- [8. 무작위 배경색](#js-17-section-12)
- [9. RGBA 색상](#js-17-section-13)
- [10. Submit Event](#js-17-section-14)
- [11. `preventDefault()`](#js-17-section-15)
- [12. `form.submit()`](#js-17-section-16)
- [13. `requestSubmit()`](#js-17-section-17)
- [14. 더 단순한 Submit 구조](#js-17-section-18)
- [15. Capturing](#js-17-section-19)
- [16. Target 단계](#js-17-section-20)
- [17. Bubbling](#js-17-section-21)
- [18. 원본 전파 방향 오류](#js-17-section-22)
- [19. Capture Listener](#js-17-section-23)
- [20. `event.target`](#js-17-section-24)
- [21. `event.currentTarget`](#js-17-section-25)
- [22. 일반 함수의 `this`](#js-17-section-26)
- [23. 화살표 함수의 `this`](#js-17-section-27)
- [24. `stopPropagation()`](#js-17-section-28)
- [25. `stopImmediatePropagation()`](#js-17-section-29)
- [26. Event 제어 비교](#js-17-section-30)
- [27. Board Event 구조](#js-17-section-31)
- [28. 중복 Listener 문제](#js-17-section-32)
- [29. Event Delegation](#js-17-section-33)
- [30. `matches()`](#js-17-section-34)
- [31. `closest()`](#js-17-section-35)
- [32. Checkbox에서 Row 찾기](#js-17-section-36)
- [33. `parentNode`보다 `closest()`](#js-17-section-37)
- [34. Custom Attribute](#js-17-section-38)
- [35. 문제 1: 주문 정보와 배송 정보](#js-17-section-39)
- [36. `change` 이벤트 사용](#js-17-section-40)
- [37. 복사 후 주문 정보 변경](#js-17-section-41)
- [38. 실시간 배송 동기화](#js-17-section-42)
- [39. 문제 2: 로그인 검증](#js-17-section-43)
- [40. 오류 Style Class](#js-17-section-44)
- [41. 문제 3: 피자 주문 데이터](#js-17-section-45)
- [42. 가격과 이름 분리](#js-17-section-46)
- [43. 선택된 Size](#js-17-section-47)
- [44. 선택된 Topping](#js-17-section-48)
- [45. 가격 계산](#js-17-section-49)
- [46. 주문 내역 출력](#js-17-section-50)
- [47. 금액 표시](#js-17-section-51)
- [48. 문제 4: 메뉴 선택](#js-17-section-52)
- [49. 원본 메뉴 문제](#js-17-section-53)
- [50. 단일 선택 상태](#js-17-section-54)
- [51. Check 표시 CSS](#js-17-section-55)
- [52. 문제 5: Todo 원본 흐름](#js-17-section-56)
- [53. 빈 입력 오류](#js-17-section-57)
- [54. 검증을 먼저 수행](#js-17-section-58)
- [55. 안전한 Todo 생성](#js-17-section-59)
- [56. 사용자 입력과 `innerHTML`](#js-17-section-60)
- [57. Listener 반복 등록 문제](#js-17-section-61)
- [58. Todo Event Delegation](#js-17-section-62)
- [59. Todo 삭제 위임](#js-17-section-63)
- [60. Todo 추가](#js-17-section-64)
- [61. 전체 선택](#js-17-section-65)
- [62. 개별 선택과 전체 선택 동기화](#js-17-section-66)
- [63. `indeterminate`](#js-17-section-67)
- [64. 선택 Todo 삭제](#js-17-section-68)
- [65. Todo 완료 Style](#js-17-section-69)
- [66. 내 코드와 강사님 코드 비교](#js-17-section-70)
- [67. 기존 코드에서 개선한 이유](#js-17-section-71)
- [68. 실무형 예제: 위임 기반 Todo Component](#js-17-section-72)
- [69. 대표 오류로 이해하기](#js-17-section-73)
- [70. 자주 하는 실수](#js-17-section-74)
- [71. 핵심 요약](#js-17-section-75)
- [72. 최종 체크리스트](#js-17-section-76)
- [마무리](#js-17-section-77)
- [V3 실행 추적 카드 — submit 발생 → 캡처/타깃/버블 → 검증·전송](#js-17-section-78)

</details>

---

<a id="js-17-section-1"></a>

## 개요

폼 이벤트는 사용자가 입력창을 선택하고 값을 바꾸거나 Form을 제출할 때 발생한다.

```text
입력 요소 Focus
    ↓
사용자 입력
    ↓
Input Event
    ↓
Form Submit
    ↓
검증
    ↓
제출 또는 오류 표시
```

이벤트 전파는 자식 요소에서 발생한 이벤트가 상위 요소로 전달되는 흐름이다.

```text
Capturing
→ 상위에서 Target 방향

Target
→ 실제 이벤트 발생 요소

Bubbling
→ Target에서 상위 방향
```

> [!IMPORTANT]
> `preventDefault()`는 브라우저 기본 동작을 막고, `stopPropagation()`은 이벤트 전파를 막는다. 두 API의 목적은 다르다.

---

<a id="js-17-section-2"></a>

## 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `focus` | 요소가 입력 초점을 얻을 때 발생 |
| `blur` | 요소가 입력 초점을 잃을 때 발생 |
| `input` | 입력값이 실제로 바뀔 때 발생 |
| `change` | 선택값 변경이 확정될 때 발생 |
| `submit` | Form 제출을 시도할 때 발생 |
| `preventDefault()` | 기본 제출·이동 동작 취소 |
| `requestSubmit()` | Submit Event와 검증을 유지한 제출 요청 |
| `target` | 이벤트가 실제 발생한 요소 |
| `currentTarget` | 현재 Listener가 등록된 요소 |
| `stopPropagation()` | 현재 전파 경로의 다른 요소로 전달 중단; 같은 요소의 다른 리스너·기본 동작 취소와는 별개 |
| Event Delegation | 상위 요소 Listener 하나로 하위 요소 처리 |
| `closest()` | 현재 요소에서 가까운 조상 탐색 |
| `matches()` | 요소가 선택자와 일치하는지 확인 |

---

<a id="js-17-section-3"></a>

## 학습 목표

- target/currentTarget, 기본 동작과 전파 취소를 구분한다.
- 원본의 해당 부분을 찾아 실행 순서와 결과를 다시 확인한다.

---

<a id="js-17-section-4"></a>

## 개념에서 실제 실행까지: 폼 제출과 이벤트 전파는 서로 다른 처리 흐름이다

폼 제출은 버튼 클릭뿐 아니라 Enter로도 일어날 수 있으므로 form의 submit에서 검증한다. preventDefault는 제출 같은 기본 동작을 취소하고 stopPropagation은 다음 요소로 전달되는 경로를 막는다. 서로 대체할 수 없다.

전파는 조상 capture→target→조상 bubble 순서다. target은 실제 발생 요소, currentTarget은 지금 실행 중인 listener의 등록 요소다. 일반 함수 listener의 this는 currentTarget이지만 화살표는 주변 this를 유지한다. form.submit은 검증·submit 이벤트를 거치지 않고, requestSubmit은 일반 제출 절차를 거친다. submit listener 안에서 무조건 requestSubmit을 다시 호출하면 재진입 문제가 생길 수 있다.

강사님 원본은 배송·로그인·피자·메뉴·Todo의 요구사항을 남겼고, 내 원본은 추가 구현을 작성했다. 이를 강사님 완성 풀이와 비교했다고 표현하면 안 된다. 내 메뉴는 클릭마다 ✔를 누적할 수 있고 Todo는 재등록·빈 입력·innerHTML 입력 문제가 있다. 수업 요구사항을 기준으로 개선 예제를 분리한다.

### 수업 원본에서 사용한 부분

아래는 전체 실행 파일이 아니라 **개념에 대응하는 문맥 발췌**다. 나머지 HTML·선언·등록 코드는 원본과 기존 번호형 본문에서 이어 확인한다. 

내 코드: `workspace_html/javascript/asset/js/17_event_form.js`

```javascript
const form = document.querySelector('#form')
    form.addEventListener('submit', function(event){
        
        // prevent는 태그의 기본 고유 기능을 막는다는 함수 (submit 등)
        event.preventDefault()

        if(query.value.trim().length < 2) {
            alert('검색어는 두 글자 이상입니다.')
```

강사님 코드: `workspace_teacher/workspace_html/javascript/asset/js/17_event_form.js`

```javascript
const form = document.querySelector('#form')
    form.addEventListener('submit', function(event){

        // 태그의 기본(고유) 기능을 막아준다
        event.preventDefault()

        if(query.value.trim().length < 2){
            alert('검색어는 두 글자 이상입니다')
```

### 직접 재현하는 최소 예제와 결과

이 예제는 **이번 리팩토링의 설명용 재구성**이다. 원본 그대로의 발췌와 구별한다. 외부 통신 없이 Console에서 실행한다. 다른 예제의 변수와 섞이지 않게 새 실행 문맥에서 실행한다.

```javascript
const selected = [true, false, true];
const all = selected.length > 0 && selected.every(Boolean);
const some = selected.some(Boolean);
console.log(all, some && !all);
const size = "small 18000";
const topping = ["감자 2000", "치즈 2500"];
const total = Number(size.split(" ")[1]) +
  topping.reduce((sum, item) => sum + Number(item.split(" ")[1]), 0);
console.log(total);
```

예상 출력:

```text
false true
22500
```

### 결과를 역추적하는 방법

첫 줄은 전체선택 checked=false, indeterminate=true에 대응한다. 빈 배열.every는 true라 length>0 검사가 필요하다. 가격 문자열 분리는 수업 방식이고 💡 개선 설계는 데이터의 name/price 필드를 따로 둔다.

출력은 아래의 확인 경로로 추적한다. return 값은 호출자에게 전달되고 자동으로 화면에 표시되지 않는다. Console 로그, DOM 변경, 저장소 변경, 서버 응답은 별개 단계다.

| 확인할 단계 | 이 예제에서 볼 것 |
| --- | --- |
| 입력 | 리터럴·현재 폼 값·이벤트 인수·응답 중 출처를 위 설명과 대조 |
| 실행 | 각 줄 또는 콜백이 지금 실행되는지, 나중에 실행되는지 구분 |
| 결과 | 위 예상 출력과 현재 값·자료형을 함께 대조 |
| 오류 | 첫 오류 줄의 입력과 직전 상태를 확인하고 뒤 로그 누락 원인 추적 |

### 별도 강사님 완성 퀴즈와 대조: data 속성과 함수별 책임

주 수업 파일 `asset/js/17_event_form.js`에서는 문제1~5가 요구사항 상태지만, **별도 `workspace_teacher/workspace_html/javascript/퀴즈/이벤트.html`에는 q1~q5 구현이 있다.** '강사님 구현이 전혀 없음'으로 읽으면 안 된다. 아래 비교는 이 별도 파일까지 확인한 결과다.

| 기능 | 내 주 수업 파일 | 강사님 별도 퀴즈 | 실제 동작과 개선 |
| --- | --- | --- | --- |
| 초기화 | 여러 load listener에서 등록 | onload에서q1~q5 호출 | 실행 순서와 중복 등록을 점검 |
| 로그인 | 빈 값에 오류 문구 표시 | q2에서 정상입력 시 오류 삭제 | 이전 오류가 남지 않는지 다시 클릭 |
| 피자 가격 | value의 이름·가격을split | data-size/data-price 등을 읽음 | 문자열 숫자는Number변환 후합산 |
| 메뉴 선택 | ✔ 문자열이 누적될 수 있음 | 모든li의bold를지우고target에추가 | ul의 빈 곳 클릭은closest('li')로거름 |
| Todo | 입력·리스너 재등록 문제 | 새 노드별 등록과부모위임이혼재 | 빈입력·innerHTML·삭제후전체선택 재계산 보강 |

강사님q2의id는 `login.do`다. `#login.do`는IDlogin이며classdo인요소를 뜻하므로 `[id="login.do"]`로 찾았다. 같은 점 문자라도 실제ID문자와CSS선택자문법이 다르다.

q3은 `option.dataset.name`, `size.getAttribute('data-price')`를 읽는다. dataset도 문자열이다. 강사님 코드의 `for(topping of aTopping)`에는 선언이 없고, 문서전체 `[type="checkbox"]:checked` 조회는 다른 문제의체크박스까지 포함할 수 있으므로 `#q3` 범위에서 선택해야 한다.

💡 아래는 속성형 가격 방식의 최소 재구성이다. 단독브라우저Console에서 실행하며 화면에는노드를붙이지않는다.

```javascript
const size = document.createElement("input");
size.dataset.price = "18000";
const prices = ["2000", "2500"];
const total = Number(size.dataset.price) + prices.reduce((sum, p) => sum + Number(p), 0);
console.log(typeof size.dataset.price, total);
```

예상출력은 `string 22500`이다. 실제피자화면에서도size·topping원본값→숫자변환→합계→bill출력을차례로확인한다. q5의선택삭제뒤에는체크박스상태도다시계산한다. 기존개선Todo예제는강사님퀴즈를그대로복사한것이아니라안전성을보강한별도구현이다.


### 단계별 복습 실습과 정답

**기본 실습:** small18000+감자2000+치즈2500의 가격을 계산한다.

**응용·디버깅 실습:** 3개 체크중2개선택,전체선택뒤1개해제,선택삭제후빈목록의 상태를 설명한다.

**통합 확인:** 위 최소 예제를 새 문맥에서 작성하고 정상값·빈 값·경계값으로 실행한다. 원본에서 대응하는 선언·호출·콜백을 찾아 위에 나타난 차이가 무엇을 바꾸는지 설명한다. 아래 정답은 먼저 예측한 뒤 펼친다. 이 실습은 💡 설명용 보강이며 원본에 모두 완성되어 있다는 뜻은 아니다.

<details>
<summary>정답과 처리 순서 해설</summary>

1. 22500원이다. 문자열을Number로 변환해 합한다. 클릭할 때마다 합계변수를 초기화한다.
2. 일부선택checked=false/indeterminate=true,1개해제도일부선택,빈목록은둘다false다. 추가·삭제뒤에도 재계산한다.
3. 최소 예제의 예상 출력과 한 줄씩 대조한다. 값이 다른 경우 입력 → 형 변환 → 분기/상태 변경 → 출력 순서로 첫 차이를 찾는다. DOM·API 예제는 Console 값만 아니라 화면·Elements·Network가 서로 같은 상태를 말하는지도 점검한다.

</details>

### 복습 질문과 해설

**질문:** 할 일을 추가할 때 기존 모든 항목에 새 익명 listener를 다시 붙이면?

**해설:** 기존 항목에 이벤트가 누적된다. 고정 부모에 위임하거나 새 항목에만 한 번 등록한다. 클릭 후 콘솔 횟수와 항목 개수를 함께 확인한다.

**한 번 더 확인:** 예제의 입력을 하나 바꾸고 결과를 먼저 예상한 뒤 실행한다. 정상 입력만 아니라 비어 있는 값, 경계값, 두 번 실행했을 때의 상태를 기존 실습·오류 절에서 반복 확인한다.

---

<a id="js-17-section-5"></a>

## 1. 원본 실행 구조

원본 JavaScript는 `window.addEventListener("load", ...)` 안에서 DOM을 선택하고 이벤트를 등록한다.

```javascript
window.addEventListener(
    "load",
    () => {
        // DOM 선택
        // Event Listener 등록
    },
)
```

내 코드는 기본 예제와 문제 1~5를 각각 다른 Load Listener에서 초기화한다.

---

<a id="js-17-section-6"></a>

## 2. 여러 Load Listener

```javascript
window.addEventListener(
    "load",
    initCore,
)

window.addEventListener(
    "load",
    initExercises,
)
```

`addEventListener()` 방식이므로 두 Callback이 모두 실행된다.

기능별 초기화 함수를 분리하는 것은 가능하지만 전체 시작점을 하나로 모으면 흐름을 파악하기 쉽다.

---

<a id="js-17-section-7"></a>

## 3. 초기화 통합

```javascript
function init() {
    initSearchForm()
    initPropagationExamples()
    initExercises()
}

window.addEventListener(
    "DOMContentLoaded",
    init,
    {
        once: true,
    },
)
```

---

<a id="js-17-section-8"></a>

## 4. `focus`

```javascript
queryInput.addEventListener(
    "focus",
    () => {
        queryInput.classList.add(
            "is-focused",
        )
    },
)
```

요소가 입력 초점을 얻을 때 발생한다.

---

<a id="js-17-section-9"></a>

## 5. `blur`

```javascript
queryInput.addEventListener(
    "blur",
    () => {
        queryInput.classList.remove(
            "is-focused",
        )
    },
)
```

요소가 입력 초점을 잃을 때 발생한다.

---

<a id="js-17-section-10"></a>

## 6. Style 직접 변경 개선

원본:

```javascript
queryInput.style.backgroundColor = (
    "yellow"
)
```

개선 CSS:

```css
.search-input.is-focused {
    background: yellow;
}
```

JavaScript:

```javascript
queryInput.classList.add(
    "is-focused",
)
```

상태 스타일은 Class로 관리하는 편이 유지보수에 유리하다.

---

<a id="js-17-section-11"></a>

## 7. `input`

```javascript
queryInput.addEventListener(
    "input",
    () => {
        console.log(
            queryInput.value,
        )
    },
)
```

키보드 입력뿐 아니라 다음 값 변경도 감지한다.

- 붙여넣기
- 잘라내기
- 자동 완성
- 음성 입력
- 모바일 키보드 입력

---

<a id="js-17-section-12"></a>

## 8. 무작위 배경색

원본:

```javascript
const red = parseInt(
    Math.random() * 256,
)
```

개선:

```javascript
const red = Math.floor(
    Math.random() * 256,
)
```

양수 난수의 정수화 의도가 더 명확하다.

---

<a id="js-17-section-13"></a>

## 9. RGBA 색상

```javascript
function getRandomColor() {
    const red = Math.floor(
        Math.random() * 256,
    )

    const green = Math.floor(
        Math.random() * 256,
    )

    const blue = Math.floor(
        Math.random() * 256,
    )

    const alpha = Math.random()

    return (
        `rgba(${red}, ${green}, `
        + `${blue}, ${alpha})`
    )
}
```

---

<a id="js-17-section-14"></a>

## 10. Submit Event

```javascript
searchForm.addEventListener(
    "submit",
    event => {
        event.preventDefault()

        const query = (
            queryInput.value.trim()
        )

        if (
            query.length < 2
        ) {
            alert(
                "검색어는 두 글자 이상입니다.",
            )

            return
        }

        searchForm.submit()
    },
)
```

---

<a id="js-17-section-15"></a>

## 11. `preventDefault()`

Form의 기본 제출을 먼저 막고 JavaScript에서 검증한다.

```text
Submit 시도
→ preventDefault()
→ 입력 검증
→ 실패하면 종료
→ 성공하면 제출
```

---

<a id="js-17-section-16"></a>

## 12. `form.submit()`

```javascript
searchForm.submit()
```

Form을 직접 제출한다.

일반적으로 다음이 다시 실행되지 않는다.

- Submit Event
- HTML Constraint Validation
- Submit Button 정보

따라서 원본 구조는 무한 재귀에 빠지지 않는다.

---

<a id="js-17-section-17"></a>

## 13. `requestSubmit()`

```javascript
searchForm.requestSubmit()
```

실제 Submit Button을 누른 것처럼 Submit Event와 검증 흐름을 유지한다.

하지만 같은 Submit Handler에서 조건 없이 다시 호출하면 재귀적으로 Submit Event가 발생할 수 있다.

---

<a id="js-17-section-18"></a>

## 14. 더 단순한 Submit 구조

```javascript
searchForm.addEventListener(
    "submit",
    event => {
        const query = (
            queryInput.value.trim()
        )

        if (
            query.length >= 2
        ) {
            return
        }

        event.preventDefault()

        alert(
            "검색어는 두 글자 이상입니다.",
        )

        queryInput.focus()
    },
)
```

성공 시 기본 제출을 그대로 허용하고, 실패할 때만 막는다.

---

<a id="js-17-section-19"></a>

## 15. Capturing

```text
Window
→ Document
→ Body
→ Parent
→ Target
```

상위 요소에서 실제 Target 방향으로 내려가는 단계다.

---

<a id="js-17-section-20"></a>

## 16. Target 단계

실제 이벤트가 발생한 요소에서 처리되는 단계다.

```text
Capturing
→ Target
→ Bubbling
```

---

<a id="js-17-section-21"></a>

## 17. Bubbling

```text
Target
→ Parent
→ Body
→ Document
→ Window
```

Target에서 상위 요소 방향으로 올라가는 단계다.

---

<a id="js-17-section-22"></a>

## 18. 원본 전파 방향 오류

내 원본 주석은 Capturing과 Bubbling 방향을 반대로 설명한다.

정확한 방향:

```text
Capturing
→ 상위에서 Target으로

Bubbling
→ Target에서 상위로
```

---

<a id="js-17-section-23"></a>

## 19. Capture Listener

```javascript
parent.addEventListener(
    "click",
    handleParent,
    {
        capture: true,
    },
)
```

Capturing 단계에서 실행한다.

기본값은 `false`이며 Bubbling 단계에서 실행한다.

---

<a id="js-17-section-24"></a>

## 20. `event.target`

```javascript
parent.addEventListener(
    "click",
    event => {
        console.log(
            event.target,
        )
    },
)
```

실제로 클릭된 가장 안쪽 요소다.

---

<a id="js-17-section-25"></a>

## 21. `event.currentTarget`

```javascript
parent.addEventListener(
    "click",
    event => {
        console.log(
            event.currentTarget,
        )
    },
)
```

현재 Listener가 등록된 요소다.

---

<a id="js-17-section-26"></a>

## 22. 일반 함수의 `this`

```javascript
parent.addEventListener(
    "click",
    function (
        event,
    ) {
        console.log(
            this
            === event.currentTarget,
        )
    },
)
```

일반 함수 Listener에서 `this`는 일반적으로 `currentTarget`과 같다.

---

<a id="js-17-section-27"></a>

## 23. 화살표 함수의 `this`

```javascript
parent.addEventListener(
    "click",
    event => {
        console.log(this)
    },
)
```

화살표 함수는 자신만의 `this`를 만들지 않고 바깥 Scope의 `this`를 사용한다.

“화살표 함수에서는 `this`를 사용할 수 없다”는 설명은 부정확하다.

---

<a id="js-17-section-28"></a>

## 24. `stopPropagation()`

```javascript
child.addEventListener(
    "click",
    event => {
        event.stopPropagation()
    },
)
```

현재 이벤트가 다음 상위 요소로 전파되는 것을 막는다.

---

<a id="js-17-section-29"></a>

## 25. `stopImmediatePropagation()`

```javascript
child.addEventListener(
    "click",
    event => {
        event.stopImmediatePropagation()
    },
)
```

전파뿐 아니라 같은 요소에 등록된 이후 Listener 실행도 중단한다.

---

<a id="js-17-section-30"></a>

## 26. Event 제어 비교

| API | 역할 |
| --- | --- |
| `preventDefault()` | 기본 브라우저 동작 취소 |
| `stopPropagation()` | 상위·하위 방향 전파 중단 |
| `stopImmediatePropagation()` | 같은 요소의 다음 Listener까지 중단 |
| `submit()` | Submit Event 없이 직접 제출 |
| `requestSubmit()` | Submit Event 흐름을 유지한 제출 요청 |

---

<a id="js-17-section-31"></a>

## 27. Board Event 구조

원본은 Table과 각 `tr`에 Click Listener를 등록하는 실습이 포함된다.

```text
Board Listener
+ 각 Row Listener
→ 같은 Click이 여러 경로에서 처리될 수 있음
```

---

<a id="js-17-section-32"></a>

## 28. 중복 Listener 문제

Title이나 Writer를 클릭하면 다음 Listener가 모두 실행될 수 있다.

```text
tr Listener
→ Board Listener
```

Bubbling으로 중복 로그가 발생할 수 있다.

---

<a id="js-17-section-33"></a>

## 29. Event Delegation

상위 Table 하나에 Listener를 등록한다.

```javascript
board.addEventListener(
    "click",
    event => {
        const target = event.target

        // Target별 분기
    },
)
```

동적으로 추가된 Row에도 별도 Listener 없이 동작한다.

---

<a id="js-17-section-34"></a>

## 30. `matches()`

```javascript
if (
    target.matches(
        ".title",
    )
) {
    console.log(
        target.textContent,
    )
}
```

현재 요소가 CSS Selector와 일치하는지 검사한다.

---

<a id="js-17-section-35"></a>

## 31. `closest()`

```javascript
const row = target.closest(
    "tr",
)
```

현재 요소부터 시작해 가장 가까운 조상 중 Selector와 일치하는 요소를 찾는다.

---

<a id="js-17-section-36"></a>

## 32. Checkbox에서 Row 찾기

```javascript
if (
    target.matches(
        "input.chk",
    )
) {
    const row = target.closest(
        "tr",
    )

    const title = (
        row?.querySelector(
            ".title",
        )
    )

    console.log(
        title?.textContent,
    )
}
```

---

<a id="js-17-section-37"></a>

## 33. `parentNode`보다 `closest()`

원본은 구조에 따라 여러 번 `parentNode`를 사용할 수 있다.

```text
target.parentNode.parentNode
```

HTML 구조가 조금만 바뀌어도 잘못된 요소를 선택할 수 있다.

```javascript
target.closest("tr")
```

의도가 명확하고 구조 변화에 더 강하다.

---

<a id="js-17-section-38"></a>

## 34. Custom Attribute

원본:

```html
<td writer="작성자1">
    작성자1
</td>
```

```javascript
target.getAttribute(
    "writer",
)
```

사용자 정의 데이터는 `data-*`를 권장한다.

```html
<td data-writer="작성자1">
```

```javascript
target.dataset.writer
```

---

<a id="js-17-section-39"></a>

## 35. 문제 1: 주문 정보와 배송 정보

요구사항:

```text
Checkbox 선택
→ 주문 이름·주소를 배송 이름·주소에 복사

Checkbox 해제
→ 배송 정보 초기화
```

---

<a id="js-17-section-40"></a>

## 36. `change` 이벤트 사용

```javascript
sameAsOrder.addEventListener(
    "change",
    () => {
        if (
            sameAsOrder.checked
        ) {
            shippingName.value = (
                orderName.value
            )

            shippingAddress.value = (
                orderAddress.value
            )

            return
        }

        shippingName.value = ""
        shippingAddress.value = ""
    },
)
```

Checkbox 상태 변경에는 `click`보다 `change`가 의미상 적합하다.

---

<a id="js-17-section-41"></a>

## 37. 복사 후 주문 정보 변경

Checkbox를 선택한 뒤 주문 정보를 다시 수정하면 배송 정보가 자동 동기화되지 않을 수 있다.

필요하면 다음 정책 중 하나를 정한다.

```text
1. Checkbox 선택 순간에만 복사
2. 선택 중에는 실시간 동기화
3. 배송 필드를 Readonly 처리
```

---

<a id="js-17-section-42"></a>

## 38. 실시간 배송 동기화

```javascript
function syncShipping() {
    if (!sameAsOrder.checked) {
        return
    }

    shippingName.value = (
        orderName.value
    )

    shippingAddress.value = (
        orderAddress.value
    )
}

orderName.addEventListener(
    "input",
    syncShipping,
)

orderAddress.addEventListener(
    "input",
    syncShipping,
)
```

---

<a id="js-17-section-43"></a>

## 39. 문제 2: 로그인 검증

```javascript
loginForm.addEventListener(
    "submit",
    event => {
        event.preventDefault()

        const id = (
            loginId.value.trim()
        )

        const password = (
            loginPassword
                .value
                .trim()
        )

        if (id === "") {
            loginError.textContent = (
                "아이디를 입력하세요."
            )

            loginId.focus()
            return
        }

        if (password === "") {
            loginError.textContent = (
                "비밀번호를 입력하세요."
            )

            loginPassword.focus()
            return
        }

        loginError.textContent = ""
    },
)
```

---

<a id="js-17-section-44"></a>

## 40. 오류 Style Class

```css
.form-error {
    color: red;
}
```

```javascript
loginError.classList.add(
    "form-error",
)
```

Inline Style보다 CSS Class를 사용한다.

---

<a id="js-17-section-45"></a>

## 41. 문제 3: 피자 주문 데이터

원본 선택 범위:

```text
피자
→ 불고기, 페퍼로니, 포테이토, 치즈, 파인애플, 고르곤졸라

크기
→ Small 18,000원
→ Medium 20,000원
→ Large 22,000원

도우
→ 씬, 고구마, 치즈, 소보로

토핑
→ 감자 2,000원
→ 고구마 2,000원
→ 치즈 2,500원
→ 베이컨 3,000원
```

---

<a id="js-17-section-46"></a>

## 42. 가격과 이름 분리

좋지 않은 방식:

```text
감자 2000
```

문자열을 공백으로 나눠 이름과 가격을 얻으면 이름에 공백이 포함될 때 문제가 생긴다.

개선 HTML:

```html
<input
    type="checkbox"
    name="topping"
    value="potato"
    data-name="감자"
    data-price="2000"
>
```

---

<a id="js-17-section-47"></a>

## 43. 선택된 Size

```javascript
const selectedSize = (
    pizzaForm.querySelector(
        '[name="size"]:checked',
    )
)
```

---

<a id="js-17-section-48"></a>

## 44. 선택된 Topping

```javascript
const selectedToppings = [
    ...pizzaForm.querySelectorAll(
        '[name="topping"]:checked',
    ),
]
```

---

<a id="js-17-section-49"></a>

## 45. 가격 계산

```javascript
const sizePrice = Number(
    selectedSize?.dataset.price
    ?? 0,
)

const toppingPrice = (
    selectedToppings.reduce(
        (
            total,
            topping,
        ) => (
            total
            + Number(
                topping.dataset.price
                ?? 0,
            )
        ),
        0,
    )
)

const totalPrice = (
    sizePrice
    + toppingPrice
)
```

---

<a id="js-17-section-50"></a>

## 46. 주문 내역 출력

```javascript
const toppingNames = (
    selectedToppings.map(
        topping => (
            topping.dataset.name
        ),
    )
)

orderSummary.textContent = (
    `토핑: `
    + (
        toppingNames.join(", ")
        || "없음"
    )
)
```

---

<a id="js-17-section-51"></a>

## 47. 금액 표시

```javascript
orderPrice.textContent = (
    `총액: `
    + `${totalPrice.toLocaleString(
        "ko-KR",
    )}원`
)
```

---

<a id="js-17-section-52"></a>

## 48. 문제 4: 메뉴 선택

요구사항:

```text
클릭한 메뉴 하나만 굵게 유지
```

내 원본은 클릭한 요소에 Class와 Check 문자를 계속 추가하지만 기존 선택을 해제하지 않는다.

---

<a id="js-17-section-53"></a>

## 49. 원본 메뉴 문제

```text
첫 번째 메뉴 클릭
→ 선택 표시 추가

두 번째 메뉴 클릭
→ 첫 번째 표시 유지
→ 두 번째에도 표시 추가

같은 메뉴 재클릭
→ Check 문자 중복 가능
```

---

<a id="js-17-section-54"></a>

## 50. 단일 선택 상태

```javascript
menuList.addEventListener(
    "click",
    event => {
        const item = (
            event.target.closest(
                ".menu-item",
            )
        )

        if (
            item === null
            || !menuList.contains(item)
        ) {
            return
        }

        menuList
            .querySelectorAll(
                ".menu-item",
            )
            .forEach(
                menuItem => {
                    menuItem.classList.toggle(
                        "is-active",
                        menuItem === item,
                    )
                },
            )
    },
)
```

---

<a id="js-17-section-55"></a>

## 51. Check 표시 CSS

```css
.menu-item.is-active {
    font-weight: bold;
}

.menu-item.is-active::after {
    content: " ✔";
}
```

Text Node를 직접 계속 추가하지 않으므로 중복되지 않는다.

---

<a id="js-17-section-56"></a>

## 52. 문제 5: Todo 원본 흐름

내 원본은 Todo 추가 버튼을 누르면 먼저 빈 `div`를 생성하고 DOM에 삽입한 뒤 입력값을 검사한다.

```text
빈 Row 생성
→ DOM 삽입
→ 입력값 검사
→ 빈 값이면 중간 종료
```

---

<a id="js-17-section-57"></a>

## 53. 빈 입력 오류

입력값이 비어 있어도 빈 Row가 먼저 추가된다.

이후 존재하지 않는 Checkbox나 Button을 선택해 Listener를 등록하려 하면 다음 오류가 발생할 수 있다.

```text
TypeError:
Cannot read properties of null
```

---

<a id="js-17-section-58"></a>

## 54. 검증을 먼저 수행

```javascript
const value = (
    todoInput.value.trim()
)

if (value === "") {
    alert(
        "할 일을 입력하세요.",
    )

    todoInput.focus()
    return
}
```

DOM 생성 전에 검증한다.

---

<a id="js-17-section-59"></a>

## 55. 안전한 Todo 생성

```javascript
function createTodo(
    value,
) {
    const row = (
        document.createElement(
            "div",
        )
    )

    row.classList.add(
        "todo-row",
    )

    const checkbox = (
        document.createElement(
            "input",
        )
    )

    checkbox.type = "checkbox"
    checkbox.classList.add(
        "todo-check",
    )

    const text = (
        document.createElement(
            "span",
        )
    )

    text.classList.add(
        "todo-text",
    )

    text.textContent = value

    const removeButton = (
        document.createElement(
            "button",
        )
    )

    removeButton.type = "button"
    removeButton.classList.add(
        "todo-remove",
    )

    removeButton.textContent = "삭제"

    row.append(
        checkbox,
        text,
        removeButton,
    )

    return row
}
```

---

<a id="js-17-section-60"></a>

## 56. 사용자 입력과 `innerHTML`

Todo 사용자 문자열을 `innerHTML`에 넣으면 HTML Injection 또는 XSS가 발생할 수 있다.

```javascript
text.textContent = value
```

를 사용한다.

---

<a id="js-17-section-61"></a>

## 57. Listener 반복 등록 문제

원본은 Todo를 추가할 때마다 전체 Checkbox와 Button을 다시 조회하고 Listener를 등록할 수 있다.

기존 항목에 같은 Listener가 중복 등록된다.

---

<a id="js-17-section-62"></a>

## 58. Todo Event Delegation

```javascript
todoList.addEventListener(
    "change",
    event => {
        const checkbox = (
            event.target.closest(
                ".todo-check",
            )
        )

        if (
            checkbox === null
        ) {
            return
        }

        checkbox
            .closest(
                ".todo-row",
            )
            ?.classList
            .toggle(
                "is-done",
                checkbox.checked,
            )

        updateAllCheckbox()
    },
)
```

---

<a id="js-17-section-63"></a>

## 59. Todo 삭제 위임

```javascript
todoList.addEventListener(
    "click",
    event => {
        const removeButton = (
            event.target.closest(
                ".todo-remove",
            )
        )

        if (
            removeButton === null
        ) {
            return
        }

        removeButton
            .closest(
                ".todo-row",
            )
            ?.remove()

        updateAllCheckbox()
    },
)
```

---

<a id="js-17-section-64"></a>

## 60. Todo 추가

```javascript
todoAddButton.addEventListener(
    "click",
    () => {
        const value = (
            todoInput.value.trim()
        )

        if (value === "") {
            alert(
                "할 일을 입력하세요.",
            )

            todoInput.focus()
            return
        }

        todoList.prepend(
            createTodo(value),
        )

        todoInput.value = ""

        updateAllCheckbox()
    },
)
```

---

<a id="js-17-section-65"></a>

## 61. 전체 선택

```javascript
allCheckbox.addEventListener(
    "change",
    () => {
        todoList
            .querySelectorAll(
                ".todo-check",
            )
            .forEach(
                checkbox => {
                    checkbox.checked = (
                        allCheckbox.checked
                    )

                    checkbox
                        .closest(
                            ".todo-row",
                        )
                        ?.classList
                        .toggle(
                            "is-done",
                            checkbox.checked,
                        )
                },
            )
    },
)
```

---

<a id="js-17-section-66"></a>

## 62. 개별 선택과 전체 선택 동기화

```javascript
function updateAllCheckbox() {
    const checkboxes = [
        ...todoList.querySelectorAll(
            ".todo-check",
        ),
    ]

    allCheckbox.checked = (
        checkboxes.length > 0
        && checkboxes.every(
            checkbox => (
                checkbox.checked
            ),
        )
    )

    allCheckbox.indeterminate = (
        checkboxes.some(
            checkbox => (
                checkbox.checked
            ),
        )
        && !allCheckbox.checked
    )
}
```

---

<a id="js-17-section-67"></a>

## 63. `indeterminate`

```text
모두 미선택
→ checked false
→ indeterminate false

일부 선택
→ checked false
→ indeterminate true

모두 선택
→ checked true
→ indeterminate false
```

Checkbox의 중간 상태를 시각적으로 표현한다.

---

<a id="js-17-section-68"></a>

## 64. 선택 Todo 삭제

```javascript
deleteSelectedButton.addEventListener(
    "click",
    () => {
        todoList
            .querySelectorAll(
                ".todo-check:checked",
            )
            .forEach(
                checkbox => {
                    checkbox
                        .closest(
                            ".todo-row",
                        )
                        ?.remove()
                },
            )

        updateAllCheckbox()
    },
)
```

---

<a id="js-17-section-69"></a>

## 65. Todo 완료 Style

```css
.todo-row.is-done .todo-text {
    text-decoration: line-through;
    color: #777;
}
```

JavaScript에서 직접 Style을 여러 개 변경하지 않고 상태 Class를 사용한다.

---

<a id="js-17-section-70"></a>

## 66. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| Focus·Blur·Input | 구현·상세 설명 | 구현 |
| Submit 검증 | 구현 | 구현 |
| 전파 주석 | 방향 반대로 설명 | 비교적 정확 |
| Board Listener | 일부 활성 | 일부 주석 |
| Row Listener | 활성 | 활성 |
| 문제 1~5 | 직접 구현 | 요구사항만 제시 |
| 메뉴 선택 | 미완성 | 구현 없음 |
| Todo | 부분 구현·오류 존재 | 구현 없음 |
| 전체 코드량 | 매우 큼 | 간결 |

### 66-1. 내 코드의 장점

- 폼 이벤트 종류와 발생 시점을 상세히 기록했다.
- `target`, `currentTarget`, `this`를 직접 비교했다.
- 다섯 실전 문제를 모두 시도했다.
- 주문·배송 복사와 로그인 검증을 완성했다.
- 피자 Size·Topping 가격을 합산했다.
- Todo의 추가·선택·삭제·전체 선택을 구현하려 했다.

### 66-2. 내 코드의 개선점

- Capturing과 Bubbling 방향을 반대로 설명했다.
- `==`를 사용한다.
- `innerHTML` 기반 Log와 Todo 생성 위험이 있다.
- Parent와 Child Listener가 중복 실행될 수 있다.
- 메뉴 기존 선택 해제와 중복 Check 처리가 없다.
- Todo 입력 검증 전에 DOM을 생성한다.
- Todo Listener를 추가할 때마다 다시 등록한다.
- 일부 DOM 구조 탐색이 `parentNode`에 의존한다.

### 66-3. 강사님 코드의 장점

- Focus·Blur·Input·Submit 흐름이 간결하다.
- Event 전파와 `target`, `currentTarget`, `this`를 비교한다.
- `stopPropagation()`의 효과를 확인할 수 있다.
- Table Row별 클릭 분기를 보여 준다.
- 실전 문제 요구사항을 명확히 제공한다.

### 66-4. 강사님 코드의 보충점

- Board Event Delegation 예제가 주석 처리되어 있다.
- 각 Row에 별도 Listener를 등록한다.
- Checkbox 전파 차단으로 일부 Row 분기가 실행되지 않을 수 있다.
- `innerHTML`, `==`, `parseInt()` 개선이 필요하다.
- 주 수업 파일 `asset/js/17_event_form.js`에는 문제 1~5의 완성 구현이 없지만, 별도 `퀴즈/이벤트.html`에는 q1~q5 풀이가 있다. 위 추가 대조 절에서 두 파일을 구분한다.
- `form.submit()`과 `requestSubmit()` 차이 설명이 필요하다.

---

<a id="js-17-section-71"></a>

## 67. 기존 코드에서 개선한 이유

### 67-1. 전파 방향 수정

기존 설명:

```text
Bubbling
→ 위에서 아래

Capturing
→ 아래에서 위
```

개선:

```text
Capturing
→ 상위에서 Target

Bubbling
→ Target에서 상위
```

### 67-2. Board Listener 통합

기존:

```text
각 tr마다 Listener 등록
```

개선:

```javascript
board.addEventListener(
    "click",
    handleBoardClick,
)
```

### 67-3. 메뉴 선택

기존:

```javascript
item.classList.add(
    "true",
)
```

개선:

```javascript
item.classList.toggle(
    "is-active",
    item === selectedItem,
)
```

### 67-4. Todo Listener

기존:

```text
항목 추가 때마다
모든 Checkbox·Button에 Listener 재등록
```

개선:

```text
Todo List 부모에
Change·Click Listener 한 번 등록
```

---

<a id="js-17-section-72"></a>

## 68. 실무형 예제: 위임 기반 Todo Component

```javascript
function createTodoComponent(
    root,
) {
    const input = root.querySelector(
        ".todo-input",
    )

    const addButton = root.querySelector(
        ".todo-add",
    )

    const list = root.querySelector(
        ".todo-list",
    )

    const allCheckbox = root.querySelector(
        ".todo-all",
    )

    const deleteSelected = (
        root.querySelector(
            ".todo-delete-selected",
        )
    )

    function getCheckboxes() {
        return [
            ...list.querySelectorAll(
                ".todo-check",
            ),
        ]
    }

    function updateAll() {
        const checkboxes = (
            getCheckboxes()
        )

        const checkedCount = (
            checkboxes.filter(
                checkbox => (
                    checkbox.checked
                ),
            ).length
        )

        allCheckbox.checked = (
            checkboxes.length > 0
            && checkedCount
            === checkboxes.length
        )

        allCheckbox.indeterminate = (
            checkedCount > 0
            && checkedCount
            < checkboxes.length
        )
    }

    function addTodo() {
        const value = (
            input.value.trim()
        )

        if (value === "") {
            input.focus()
            return
        }

        list.prepend(
            createTodo(value),
        )

        input.value = ""
        updateAll()
    }

    addButton.addEventListener(
        "click",
        addTodo,
    )

    input.addEventListener(
        "keydown",
        event => {
            if (
                event.key
                === "Enter"
            ) {
                addTodo()
            }
        },
    )

    list.addEventListener(
        "change",
        event => {
            if (
                !event.target.matches(
                    ".todo-check",
                )
            ) {
                return
            }

            event.target
                .closest(
                    ".todo-row",
                )
                ?.classList
                .toggle(
                    "is-done",
                    event.target.checked,
                )

            updateAll()
        },
    )

    list.addEventListener(
        "click",
        event => {
            if (
                !event.target.matches(
                    ".todo-remove",
                )
            ) {
                return
            }

            event.target
                .closest(
                    ".todo-row",
                )
                ?.remove()

            updateAll()
        },
    )

    allCheckbox.addEventListener(
        "change",
        () => {
            getCheckboxes().forEach(
                checkbox => {
                    checkbox.checked = (
                        allCheckbox.checked
                    )

                    checkbox
                        .closest(
                            ".todo-row",
                        )
                        ?.classList
                        .toggle(
                            "is-done",
                            checkbox.checked,
                        )
                },
            )
        },
    )

    deleteSelected.addEventListener(
        "click",
        () => {
            list
                .querySelectorAll(
                    ".todo-check:checked",
                )
                .forEach(
                    checkbox => {
                        checkbox
                            .closest(
                                ".todo-row",
                            )
                            ?.remove()
                    },
                )

            updateAll()
        },
    )
}
```

### 68-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| Component Root | 선택 범위를 기능 내부로 제한 |
| Event Delegation | 동적 Todo에도 자동 적용 |
| `matches()` | Event Target 종류 판정 |
| `closest()` | Todo Row 탐색 |
| `textContent` | 사용자 입력 안전 출력 |
| `indeterminate` | 일부 선택 상태 표시 |
| 상태 Class | 완료 Style 관리 |
| 함수 분리 | 생성·추가·동기화 역할 분리 |

---

<a id="js-17-section-73"></a>

## 69. 대표 오류로 이해하기

### 69-1. Capturing과 Bubbling 반대 설명

이벤트 실행 순서를 잘못 추적하게 된다.

### 69-2. `preventDefault()`와 `stopPropagation()` 혼동

기본 동작과 전파는 서로 다른 기능이다.

### 69-3. `form.submit()`이 Submit Event를 다시 발생시킨다고 생각

일반적으로 다시 발생시키지 않는다.

### 69-4. Parent와 Child Listener 중복

한 Click에서 로그나 로직이 여러 번 실행될 수 있다.

### 69-5. Todo 입력 검증 전에 DOM 생성

빈 Row와 `null` 접근 오류가 발생할 수 있다.

### 69-6. 사용자 입력을 `innerHTML`에 삽입

XSS가 발생할 수 있다.

---

<a id="js-17-section-74"></a>

## 70. 자주 하는 실수

### 70-1. Focus와 Input을 같은 이벤트로 생각

초점 변화와 값 변화는 다르다.

### 70-2. Submit Button Click만 검증

Enter 제출을 놓칠 수 있으므로 Form Submit을 사용한다.

<a id="index-section-100"></a>

### 70-3. `target`과 `currentTarget` 혼동

실제 클릭 요소와 Listener 요소가 다를 수 있다.

### 70-4. 화살표 함수의 `this`를 CurrentTarget으로 생각

화살표 함수는 Lexical `this`를 사용한다.

### 70-5. 모든 Child에 Listener 등록

동적 요소 관리와 성능이 어려워진다.

<a id="index-section-103"></a>

### 70-6. `parentNode.parentNode`에 의존

HTML 구조 변경에 취약하다.

### 70-7. 메뉴 Check 문자를 계속 추가

CSS Pseudo-element로 상태를 표현한다.

### 70-8. 가격을 문자열 그대로 더함

숫자로 변환하지 않으면 문자열 결합이 될 수 있다.

### 70-9. 전체 선택 상태를 한 방향으로만 처리

개별 선택 변경 후 전체 Checkbox도 다시 계산해야 한다.

### 70-10. 삭제 후 전체 선택 상태를 갱신하지 않음

남은 항목 기준으로 다시 계산한다.

---

<a id="js-17-section-75"></a>

## 71. 핵심 요약

```text
focus
→ 초점 획득

blur
→ 초점 상실

input
→ 값 변경

submit
→ Form 제출 시도
```

```text
Capturing
→ 상위에서 Target

Bubbling
→ Target에서 상위
```

```text
target
→ 실제 발생 요소

currentTarget
→ Listener 등록 요소
```

```text
preventDefault()
→ 기본 동작 취소

stopPropagation()
→ Event 전파 중단
```

```text
Event Delegation
→ 상위 Listener 하나로
동적 하위 요소 처리
```

---

<a id="js-17-section-76"></a>

## 72. 최종 체크리스트

- [ ] `focus`, `blur`, `input`, `change`, `submit`을 구분할 수 있는가?
- [ ] 검색어를 `trim()` 후 검증할 수 있는가?
- [ ] 검증 실패할 때만 제출을 막을 수 있는가?
- [ ] `submit()`과 `requestSubmit()` 차이를 이해했는가?
- [ ] Capturing과 Bubbling 방향을 정확히 설명할 수 있는가?
- [ ] `target`과 `currentTarget`을 구분할 수 있는가?
- [ ] 일반 함수와 화살표 함수의 `this` 차이를 이해했는가?
- [ ] `preventDefault()`와 `stopPropagation()`을 구분할 수 있는가?
- [ ] Event Delegation을 적용할 수 있는가?
- [ ] `matches()`와 `closest()`를 사용할 수 있는가?
- [ ] 주문·배송 정보를 Checkbox 상태에 따라 복사할 수 있는가?
- [ ] 로그인 오류와 성공 상태를 초기화할 수 있는가?
- [ ] Size·Topping 가격을 숫자로 합산할 수 있는가?
- [ ] 주문 내역을 구분자로 연결할 수 있는가?
- [ ] 메뉴 하나만 활성 상태로 유지할 수 있는가?
- [ ] Todo 입력 검증을 DOM 생성보다 먼저 수행하는가?
- [ ] 사용자 입력에 `textContent`를 사용하는가?
- [ ] Todo Listener를 부모에 한 번만 등록하는가?
- [ ] 전체 선택과 개별 선택을 양방향 동기화하는가?
- [ ] 일부 선택 상태에 `indeterminate`를 사용할 수 있는가?
- [ ] 삭제 후 전체 선택 상태를 다시 계산하는가?

---

<a id="js-17-section-77"></a>

## 마무리

폼 이벤트와 이벤트 전파의 핵심은 입력값을 읽고 Click Listener를 추가하는 것에서 끝나지 않는다.

```text
사용자 입력 변화와 제출 시점을 구분하고
    ↓
기본 동작과 전파 제어를 정확히 선택하고
    ↓
Target과 상위 구조를 안전하게 탐색하고
    ↓
동적 요소는 Event Delegation으로 관리하고
    ↓
상태와 화면을 일관되게 동기화하는 것
```

이 흐름을 이해하면 이후 BOM과 외부 API 문서에서도 사용자 동작과 브라우저 기능을 안정적으로 연결할 수 있다.
<a id="js-17-section-78"></a>

## V3 실행 추적 카드 — submit 발생 → 캡처/타깃/버블 → 검증·전송

폼 제출은 버튼 click보다 form의 submit 이벤트를 중심으로 처리한다. `preventDefault()`는 제출·새로고침을 막고, `stopPropagation()`은 전파를 멈추는 별도 기능이다.

부모와 자식 리스너에서 event.currentTarget을 출력해 버블 순서를 확인한다. 검증 실패 시 화면 오류를 표시하고 실제 요청이 없는지 Network에서 확인한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/17_event_form.html, asset/js/17_event_form.js`에서 실제 사용 위치와 차이를 확인한다.
