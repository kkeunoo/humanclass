# JavaScript 폼 이벤트와 이벤트 전파·실전 문제

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `17_JavaScript_폼이벤트와_이벤트전파_실전문제.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `16_JavaScript_마우스이벤트와_드래그복사제어.md` |
| 다음 학습 | 이후 JavaScript 원본 순서에 따라 진행 |
| 원본 기준 | `workspace/workspace_html/javascript/17_event_form.html`, `workspace/workspace_html/javascript/asset/js/17_event_form.js`, `workspace_teacher/workspace_html/javascript/17_event_form.html`, `workspace_teacher/workspace_html/javascript/asset/js/17_event_form.js` |
| 핵심 범위 | `focus`, `blur`, `input`, `submit`, `preventDefault()`, `form.submit()`, event bubbling, `target`, `currentTarget`, `this`, `stopPropagation()`, event delegation, `parentNode`, 주문·배송 복사, 로그인 검증, 피자 주문 계산, 메뉴 선택, Todo List |
| 프로젝트 연결 | 검색 폼 검증, table event delegation, 배송지 자동 입력, 주문 금액 계산, 정렬 메뉴 UI, 동적 Todo 관리 |

> 이 문서는 HTML과 실제 연결된 JavaScript 파일을 함께 비교했습니다. 강사님 원본은 검색 폼과 event 전파·위임 예제를 구현하고 문제 1~5는 요구사항만 제시합니다. 내 원본은 문제 1~5의 HTML과 JavaScript를 추가로 구현했습니다. 다만 메뉴 선택은 기존 선택 해제와 중복 표시 처리가 없고, Todo List는 빈 값일 때 빈 div를 먼저 추가한 뒤 `null.addEventListener()` 오류가 발생할 수 있으며, listener를 항목 추가 때마다 반복 등록합니다. 원본을 임의로 고치지 않고 실제 동작과 개선 방향을 분리해 설명합니다.

---

# 학습 목표

- `focus`, `blur`, `input` event의 발생 시점을 구분한다.
- submit event에서 기본 제출을 막고 입력값을 검증한다.
- `form.submit()`이 submit event를 다시 발생시키지 않는다는 점을 이해한다.
- bubbling과 capturing을 정확히 구분한다.
- `event.target`, `event.currentTarget`, 일반 함수의 `this`를 비교한다.
- `stopPropagation()`이 상위 요소로의 event 전파를 막는다는 점을 이해한다.
- table과 tr에 event delegation을 적용한다.
- checkbox에서 부모 행의 title을 탐색한다.
- 주문 정보와 배송 정보를 checkbox 상태에 따라 복사하거나 지운다.
- 로그인 입력값을 검증하고 오류 문구를 초기화한다.
- radio와 checkbox value를 분리해 주문 내역과 총액을 계산한다.
- 하나의 메뉴만 선택 상태로 유지하는 방식을 이해한다.
- Todo 항목을 안전하게 생성·삭제하고 전체 선택 상태를 동기화한다.
- 내 코드와 강사님 코드의 실제 구현 범위와 오류를 정확히 기록한다.

---

# Core Concepts

## 1. Load 이후 Event Binding

양쪽 JavaScript는 다음 구조를 사용합니다.

```js
window.addEventListener(
  "load",
  function() {
    // DOM 선택과 event 등록
  }
)
```

외부 script는 `<head>`에서 불러오지만 load 이후에 DOM을 선택하므로 body 요소를 찾을 수 있습니다.

내 코드는 load listener를 두 개 등록합니다.

```text
첫 번째 load listener
→ 검색 폼, 전파, 게시판

두 번째 load listener
→ 문제 1~5
```

`addEventListener()` 방식이므로 두 callback은 모두 실행됩니다.

---

## 2. Focus와 Blur

공통 원본:

```js
query.addEventListener(
  "focus",
  function() {
    query.style.backgroundColor =
      "yellow"
  }
)

query.addEventListener(
  "blur",
  function() {
    query.style.backgroundColor =
      ""
  }
)
```

- `focus`: input이 입력 초점을 얻을 때
- `blur`: input이 입력 초점을 잃을 때

내 주석에는 `"blue"`라고 적힌 부분이 있지만 실제 event는 `blur`입니다.

---

## 3. Input Event

공통 원본:

```js
query.addEventListener(
  "input",
  function() {
    log(query.value)
  }
)
```

keyboard 입력뿐 아니라 붙여넣기, 삭제 등으로 값이 바뀔 때도 발생합니다.

`keyup`보다 값 변경 자체를 감지하는 데 적합합니다.

---

## 4. 무작위 배경색

공통 코드:

```js
const r =
  parseInt(
    Math.random() * 256
  )

const g =
  parseInt(
    Math.random() * 256
  )

const b =
  parseInt(
    Math.random() * 256
  )

const a =
  Math.random()
```

최종 적용:

```js
query.style.backgroundColor =
  `rgba(${r}, ${g}, ${b}, ${a})`
```

`r`, `g`, `b`는 0~255 범위의 정수이고 `a`는 0 이상 1 미만입니다.

양수 난수 정수화에는 다음이 의도가 더 명확합니다.

```js
Math.floor(
  Math.random() * 256
)
```

---

## 5. Submit Event

공통 원본:

```js
form.addEventListener(
  "submit",
  function(event) {
    event.preventDefault()

    if (
      query.value
        .trim()
        .length < 2
    ) {
      alert(
        "검색어는 두 글자 이상입니다"
      )
    } else {
      form.submit()
    }
  }
)
```

`preventDefault()`가 form의 기본 제출을 먼저 막습니다.

검색어가 두 글자 이상이면 JavaScript로 다시 제출합니다.

---

## 6. Form.submit()의 특징

```js
form.submit()
```

은 form을 직접 제출하지만 일반적으로 submit event와 HTML constraint validation을 다시 실행하지 않습니다.

따라서 현재 코드가 무한 재귀에 빠지지 않습니다.

event와 검증 흐름을 유지하고 싶다면 현대 코드에서는:

```js
form.requestSubmit()
```

을 사용할 수 있지만, 동일 submit handler에서 조건 없이 호출하면 다시 event가 발생하므로 구조를 조심해야 합니다.

---

## 7. 실제 검색 요청

HTML:

```html
<form
  method="get"
  action="https://search.naver.com/search.naver"
  target="_blank"
>
```

input:

```html
<input
  id="query"
  name="query"
>
```

제출하면 `query` parameter가 GET query string에 포함되고 새 tab에서 검색 URL이 열립니다.

---

## 8. Event Bubbling과 Capturing

내 원본 주석은 body부터 자식으로 내려가는 단계를 bubbling, 자식부터 부모로 올라가는 단계를 capturing이라고 설명합니다.

정확한 방향은 반대입니다.

```text
Capturing
→ window/document에서 target 방향으로 내려감

Target
→ 실제 target에서 처리

Bubbling
→ target에서 상위 요소 방향으로 올라감
```

기본 `addEventListener("click", handler)`는 capture option을 주지 않으면 bubbling 단계에서 listener가 실행됩니다.

---

## 9. Target과 CurrentTarget

부모에 listener를 등록하고 자식을 클릭한 경우:

```js
parent.addEventListener(
  "click",
  function(event) {
    console.log(
      event.target
    )

    console.log(
      event.currentTarget
    )
  }
)
```

- `target`: 실제로 클릭된 자식 또는 부모
- `currentTarget`: listener가 등록된 `#parent`

내 Console label은:

```js
"event.currenttarget"
```

으로 소문자 `t`를 사용하지만 property 접근은 `event.currentTarget`으로 올바릅니다.

---

## 10. 일반 함수의 This

`addEventListener()`에 일반 함수를 전달한 경우 handler 내부 `this`는 일반적으로 `event.currentTarget`과 같습니다.

```js
console.log(
  this ===
  event.currentTarget
)
// true
```

내 주석의 “기본적으로 this에는 window가 들어 있다”는 이 handler 문맥에는 맞지 않습니다.

arrow function은 자체 `this`를 만들지 않으므로 위와 같은 의미로 사용할 수 없습니다.

---

## 11. StopPropagation

공통 원본:

```js
child1.addEventListener(
  "click",
  function(event) {
    event.stopPropagation()

    log(
      "자식1 클릭"
    )
  }
)
```

`stopPropagation()`은 현재 event가 상위 요소로 계속 전파되는 것을 막습니다.

내 주석은 이를 “capturing 방지”라고 부르지만 현재 listener는 기본 bubbling 단계에서 실행되므로 부모로 올라가는 bubbling을 막는 상황입니다.

`preventDefault()`와 역할이 다릅니다.

```text
preventDefault()
→ 기본 동작 차단

stopPropagation()
→ event 전파 차단
```

---

## 12. 게시판 Event Delegation

내 코드는 `#board`에도 click listener를 등록합니다.

```js
board.addEventListener(
  "click",
  function(event) {
    if (
      event.target
        .classList
        .contains("chk")
    ) {
      log(
        event.target.value
      )
    }
  }
)
```

부모 table 하나에서 실제 target을 검사하는 event delegation입니다.

강사님 코드에는 이 board listener가 주석 처리되어 있습니다.

---

## 13. Tr Listener

양쪽 모두 각 `tr`에 listener를 등록합니다.

```js
const trs =
  document.querySelectorAll(
    "#board tr"
  )

for (
  const tr of trs
) {
  tr.addEventListener(
    "click",
    function(event) {
      // target 판정
    }
  )
}
```

엄밀히 말하면 각 행에 listener를 따로 등록한 것이므로 table 하나에 위임하는 방식보다 listener 수가 많습니다.

---

## 14. 내 코드의 중복 Log

내 코드에는:

```text
#board listener
+
각 tr listener
```

가 모두 활성화되어 있습니다.

title이나 writer cell을 클릭하면 tr listener와 board listener가 모두 처리하므로 같은 값이 두 번 log될 수 있습니다.

강사님 코드는 board listener가 주석 처리되어 있어 각 tr listener만 실행됩니다.

---

## 15. Checkbox에서 StopPropagation

각 checkbox에도 listener가 있습니다.

```js
tr
  .querySelector(
    "input.chk"
  )
  .addEventListener(
    "click",
    function(event) {
      event.stopPropagation()

      console.log(
        this
          .parentNode
          .parentNode
          .querySelector(
            ".title"
          )
          .innerText
      )
    }
  )
```

checkbox click event가 tr과 board로 올라가는 것을 막습니다.

따라서 checkbox value를 log하는 tr/board 분기는 checkbox click 때 실행되지 않고, 현재 checkbox listener의 title Console만 실행됩니다.

원본의 “체크하면 제목 출력” 요구에는 맞지만 위쪽 value 출력 분기와는 동시에 동작하지 않습니다.

---

## 16. ParentNode Traversal

현재 구조:

```text
input.chk
→ td
→ tr
```

따라서:

```js
this.parentNode.parentNode
```

가 tr입니다.

더 명확한 방법:

```js
const row =
  this.closest("tr")

const title =
  row.querySelector(
    ".title"
  )
```

HTML 구조가 조금 바뀌어도 의도가 더 잘 드러납니다.

---

# Syntax / Comparison

## 17. Form Event 비교

| Event | 발생 시점 | 대표 활용 |
| --- | --- | --- |
| `focus` | 초점을 얻을 때 | 강조 |
| `blur` | 초점을 잃을 때 | 입력 검증 |
| `input` | 값이 바뀔 때 | 실시간 검색·미리보기 |
| `submit` | form 제출 시도 | 최종 검증 |
| `change` | 값이 확정·변경될 때 | select, checkbox 상태 처리 |

---

## 18. Event 제어 비교

| API | 역할 |
| --- | --- |
| `preventDefault()` | 기본 browser 동작 차단 |
| `stopPropagation()` | capturing/bubbling 전파 중단 |
| `stopImmediatePropagation()` | 같은 요소의 다음 listener까지 중단 |
| `form.submit()` | submit event 없이 직접 제출 |
| `form.requestSubmit()` | submit button을 통한 것처럼 제출 요청 |

---

# Representative Examples

## 19. 문제 1: 주문과 배송

내 HTML과 JavaScript에만 구현되어 있습니다.

```js
valueChk.addEventListener(
  "click",
  function() {
    if (
      valueChk.checked ==
      true
    ) {
      name2.value =
        name1.value

      address2.value =
        address1.value
    } else {
      name2.value =
        ""

      address2.value =
        ""
    }
  }
)
```

checkbox를 선택하면 주문자의 이름과 주소를 배송 정보에 복사합니다.

해제하면 배송 정보를 지웁니다.

강사님 원본은 요구사항만 있고 실제 HTML과 정답 코드는 없습니다.

### 개선점

checkbox의 상태 변화이므로 `click`보다 `change`가 의미상 적합합니다.

```js
valueChk.addEventListener(
  "change",
  function() {
  }
)
```

체크 후 주문 정보를 수정해도 배송 정보가 자동으로 다시 동기화되지는 않습니다.

---

## 20. 문제 2: 로그인 검증

내 코드:

```js
if (
  id1.value.trim() ==
  ""
) {
  errChk.innerText =
    "아이디를 입력하세요"

  errChk.style.color =
    "red"
} else if (
  pw1.value.trim() ==
  ""
) {
  errChk.innerText =
    "패스워드를 입력하세요"

  errChk.style.color =
    "red"
} else {
  errChk.innerText =
    ""
}
```

이전 15번의 password 문구 오류와 달리 17번에서는 올바른 분기 문구를 사용합니다.

성공하면 기존 오류 문구도 지웁니다.

### 개선점

- `===` 사용
- inline style 대신 CSS class 사용
- button click보다 form submit 사용
- `textContent` 사용

---

## 21. 문제 3: 피자 주문 HTML

내 원본 선택 항목:

```text
피자
→ 불고기, 페퍼로니, 포테이토, 치즈, 파인애플, 고르곤졸라

크기
→ small 18000
→ medium 20000
→ large 22000

도우
→ 씬, 고구마, 치즈, 소보로

토핑
→ 감자 2000
→ 고구마 2000
→ 치즈 2500
→ 베이컨 3000
→ 옥수수 500
→ 페퍼론치노 2500
```

화면 표기는 원본 금액을 그대로 사용합니다.

```text
small(18,000)
medium(20,000)
large(22,000)
```

---

## 22. Radio 선택값

```js
const size =
  document.querySelector(
    "[name=size]:checked"
  )

const dough =
  document.querySelector(
    "[name=dough]:checked"
  )
```

기본 checked 항목이 있으므로 현재 원본에서는 null이 아닙니다.

value 문자열을 space로 나눕니다.

```js
size.value
  .split(" ")[0]
// small

size.value
  .split(" ")[1]
// 18000
```

원본 주석도 space보다 데이터에 등장하지 않을 구분자를 쓰는 편이 좋다고 설명합니다.

더 좋은 구조는 가격을 별도 data attribute로 두는 것입니다.

```html
<input
  value="small"
  data-price="18000"
>
```

---

## 23. Topping 계산

내 코드:

```js
for (
  let i = 0;
  i < topping.length;
  i++
) {
  if (
    topping[i].checked ==
    true
  ) {
    topResult +=
      topping[i]
        .value
        .split(" ")[0]

    topPrice +=
      Number(
        topping[i]
          .value
          .split(" ")[1]
      )
  }
}
```

선택된 topping 이름과 가격을 누적합니다.

### 실제 문제

`topResult`에 구분자가 없습니다.

```text
감자치즈베이컨
```

처럼 붙어서 출력됩니다.

배열을 사용한 뒤 join하는 편이 좋습니다.

```js
const names = []

names.push(name)

names.join(", ")
```

---

## 24. 주문 총액

내 코드:

```js
priceResult +=
  topPrice +
  Number(
    size.value
      .split(" ")[1]
  )
```

총액은:

```text
size 가격
+
선택 topping 가격
```

입니다.

피자 종류와 dough에는 원본상 별도 가격이 없으므로 계산에 포함되지 않습니다.

출력:

```js
orderPrice.innerText =
  `총액: ${priceResult}원`
```

예를 들어 기본 small과 감자 topping이면 원본 데이터 기준 총액은 `20000원`입니다.

---

## 25. 문제 4: 메뉴 선택

요구사항:

```text
클릭한 메뉴만 굵게 유지
```

내 실제 구현:

```js
event.target
  .classList
  .add("true")

event.target
  .style
  .fontWeight =
  "bold"

event.target
  .innerText =
  "✔" +
  event.target.innerText
```

### 실제 동작 문제

- 이전에 선택한 메뉴의 class와 굵기를 제거하지 않음
- 여러 메뉴가 동시에 선택 상태가 됨
- 같은 메뉴를 다시 클릭할 때 `✔`가 계속 추가됨
- `textKeep`에 값을 저장하지만 복원에 사용하지 않음
- class 이름 `"true"`는 상태 의미가 불분명함
- `items.classList.contains("true")`는 container를 검사하므로 초기 false일 뿐 실질적 의미가 없음

따라서 원본 요구사항인 “클릭한 것만 유지”를 완성하지 못했습니다.

---

## 26. 메뉴 선택 개선

```js
items.addEventListener(
  "click",
  function(event) {
    const item =
      event.target.closest(
        "[data-sort]"
      )

    if (item === null) {
      return
    }

    const allItems =
      items.querySelectorAll(
        "[data-sort]"
      )

    allItems.forEach(
      function(menu) {
        menu.classList.remove(
          "active"
        )
      }
    )

    item.classList.add(
      "active"
    )
  }
)
```

표시 문자 `✔`는 text를 직접 덧붙이기보다 CSS pseudo-element로 처리하면 중복되지 않습니다.

---

## 27. 문제 5: Todo 생성 흐름

내 코드:

```js
const divAdd =
  document.createElement(
    "div"
  )

divCnt++

divAdd.classList.add(
  `col${divCnt}`
)

column.prepend(
  divAdd
)

if (
  inputText.value
    .trim() == ""
) {
  alert(
    "할일은 한 글자 이상 입력하세요."
  )
} else {
  divAdd.innerHTML = `
    <input
      type="checkbox"
      class=deleteChk
    >
    ${inputText.value}
    <button
      type="button"
      class="deleteCol"
    >
      삭제
    </button>
  `
}
```

---

## 28. 빈 Todo 입력의 실제 오류

빈 입력이어도 `divAdd`를 먼저 column에 삽입합니다.

그 후 HTML을 만들지 않으므로:

```js
const deleteCol =
  document.querySelector(
    ".deleteCol"
  )
```

가 기존 항목도 없다면 null을 반환합니다.

이어서:

```js
deleteCol.addEventListener(
  "click",
  ...
)
```

에서 TypeError가 발생합니다.

결과:

- 빈 div가 화면에 남음
- callback 실행이 중단됨
- 이후 코드가 실행되지 않음

입력 검사를 요소 생성보다 먼저 해야 합니다.

---

## 29. Todo InnerHTML과 XSS

사용자 입력:

```js
${inputText.value}
```

를 `innerHTML` 안에 직접 삽입합니다.

HTML tag나 event attribute가 실행될 수 있으므로 XSS 위험이 있습니다.

안전한 방식:

```js
const text =
  document.createElement(
    "span"
  )

text.textContent =
  inputText.value
```

---

## 30. QuerySelector 범위

항목을 만든 뒤:

```js
document.querySelector(
  ".deleteCol"
)
```

을 사용합니다.

새 항목을 `prepend()`했으므로 현재는 새 항목이 document 순서상 첫 번째라서 대체로 새 button을 가져옵니다.

하지만 전역 selector에 의존하지 말고 생성한 `divAdd` 내부에서 찾는 편이 안전합니다.

```js
divAdd.querySelector(
  ".deleteCol"
)
```

---

## 31. Listener 반복 등록

Todo 하나를 추가할 때마다 다음 listener를 새로 등록합니다.

```text
#allChk click
#checkDel click
기존 모든 .deleteChk click
```

항목이 늘어날수록 같은 control에 listener가 계속 추가됩니다.

예를 들어 Todo 10개를 추가하면 `#allChk`에 10개의 callback이 등록됩니다.

각 callback이 특정 항목을 capture하므로 결과 일부는 동작해 보일 수 있지만 관리가 어렵고 삭제된 DOM을 참조하는 listener도 남습니다.

전역 control listener는 초기화 시 한 번만 등록해야 합니다.

---

## 32. 전체 선택의 실제 범위

각 추가 시점에 등록한 allChk listener는 해당 시점의 `deleteChk` 하나만 변경합니다.

여러 listener가 누적되어 있어 결과적으로 여러 항목이 바뀔 수 있지만, 이는 의도적인 전체 순회가 아니라 callback 누적의 부수 효과입니다.

올바른 방식:

```js
const checkboxes =
  column.querySelectorAll(
    ".deleteChk"
  )

checkboxes.forEach(
  function(checkbox) {
    checkbox.checked =
      allChk.checked
  }
)
```

---

## 33. 개별 선택과 전체 선택 동기화

내 코드가 구현한 부분:

```js
if (
  chkBox[j].checked ==
  false
) {
  allChk.checked =
    false
}
```

한 항목이라도 해제하면 전체 선택을 해제합니다.

하지만 모든 개별 checkbox를 다시 선택했을 때 전체 선택을 true로 만드는 로직은 주석 설명만 있고 구현되지 않았습니다.

완성 조건:

```js
allChk.checked =
  [...checkboxes]
    .every(
      checkbox =>
        checkbox.checked
    )
```

---

## 34. 선택 삭제

내 각 listener는 자신이 참조하는 checkbox가 checked이면 해당 `divAdd`를 제거합니다.

listener가 항목마다 누적되어 있으므로 button 한 번에 여러 callback이 실행되어 checked 항목들이 삭제될 수 있습니다.

기능은 일부 충족하지만 새 항목마다 button listener를 추가하는 구조입니다.

더 명확한 방식은 `#checkDel` listener 하나에서 현재 checked 항목 전체를 조회하는 것입니다.

---

## 35. 초기 Placeholder Text

HTML:

```html
<div id="column">
  한 줄이 추가 될 곳
</div>
```

Todo를 추가해도 이 text를 지우지 않습니다.

따라서 실제 Todo와 placeholder 문구가 함께 남습니다.

빈 container로 시작하거나 첫 추가 때 placeholder를 제거하는 편이 자연스럽습니다.

---

# Practical Usage

## 36. 안전한 검색 Form

```js
const form =
  document.querySelector(
    "#form"
  )

const query =
  document.querySelector(
    "#query"
  )

form.addEventListener(
  "submit",
  function(event) {
    const keyword =
      query.value.trim()

    if (
      keyword.length < 2
    ) {
      event.preventDefault()

      alert(
        "검색어는 두 글자 이상입니다."
      )

      query.focus()
    }
  }
)
```

검증 실패 때만 기본 제출을 막으면 `form.submit()`을 직접 호출할 필요가 없습니다.

---

## 37. Table Delegation 개선

```js
const board =
  document.querySelector(
    "#board"
  )

board.addEventListener(
  "click",
  function(event) {
    const target =
      event.target

    if (
      target.matches(
        "input.chk"
      )
    ) {
      const row =
        target.closest("tr")

      console.log(
        row
          .querySelector(
            ".title"
          )
          .textContent
      )

      return
    }

    if (
      target.matches(
        ".title"
      )
    ) {
      log(
        target.textContent
      )

      return
    }

    if (
      target.hasAttribute(
        "writer"
      )
    ) {
      log(
        target.getAttribute(
          "writer"
        )
      )
    }
  }
)
```

table listener 하나로 처리해 중복 log와 여러 tr listener를 피합니다.

---

## 38. 안전한 Todo 구현 예제

```js
const column =
  document.querySelector(
    "#column"
  )

const inputText =
  document.querySelector(
    "#inputText"
  )

const addButton =
  document.querySelector(
    "#inputDiv"
  )

const allCheckbox =
  document.querySelector(
    "#allChk"
  )

const deleteSelected =
  document.querySelector(
    "#checkDel"
  )

function updateAllCheckbox() {
  const checkboxes =
    [
      ...column
        .querySelectorAll(
          ".todo-check"
        )
    ]

  allCheckbox.checked =
    checkboxes.length > 0 &&
    checkboxes.every(
      function(checkbox) {
        return checkbox.checked
      }
    )
}

function createTodo(value) {
  const row =
    document.createElement(
      "div"
    )

  row.classList.add(
    "todo-row"
  )

  const checkbox =
    document.createElement(
      "input"
    )

  checkbox.type =
    "checkbox"

  checkbox.classList.add(
    "todo-check"
  )

  const text =
    document.createElement(
      "span"
    )

  text.textContent =
    value

  const deleteButton =
    document.createElement(
      "button"
    )

  deleteButton.type =
    "button"

  deleteButton.textContent =
    "삭제"

  checkbox.addEventListener(
    "change",
    function() {
      row.classList.toggle(
        "done",
        checkbox.checked
      )

      updateAllCheckbox()
    }
  )

  deleteButton.addEventListener(
    "click",
    function() {
      row.remove()
      updateAllCheckbox()
    }
  )

  row.append(
    checkbox,
    text,
    deleteButton
  )

  return row
}

addButton.addEventListener(
  "click",
  function() {
    const value =
      inputText.value.trim()

    if (value === "") {
      alert(
        "할 일은 한 글자 이상 입력하세요."
      )

      return
    }

    column.prepend(
      createTodo(value)
    )

    inputText.value =
      ""

    updateAllCheckbox()
  }
)

allCheckbox.addEventListener(
  "change",
  function() {
    const checkboxes =
      column.querySelectorAll(
        ".todo-check"
      )

    checkboxes.forEach(
      function(checkbox) {
        checkbox.checked =
          allCheckbox.checked

        checkbox.dispatchEvent(
          new Event("change")
        )
      }
    )
  }
)

deleteSelected.addEventListener(
  "click",
  function() {
    const selected =
      column.querySelectorAll(
        ".todo-check:checked"
      )

    selected.forEach(
      function(checkbox) {
        checkbox
          .closest(".todo-row")
          .remove()
      }
    )

    updateAllCheckbox()
  }
)
```

---

# My Code vs Teacher Code

## 39. 비교표

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| HTML 범위 | 기본 예제 + 문제 1~5 UI | 기본 예제만 |
| JavaScript 범위 | 기본 예제 + 문제 1~5 풀이 | 기본 예제 + 문제 요구사항 주석 |
| Focus 설명 | 상세 | 간결 |
| Alert 문구 | 마침표 있음 | 마침표 없음 |
| Parent Console label | `event.currenttarget` | `event.currentTarget` |
| Board listener | 활성 | 주석 처리 |
| Tr listener | 활성 | 활성 |
| Title·writer click | 중복 log 가능 | 한 번 log |
| 문제 1 | 구현 | 요구만 제시 |
| 문제 2 | 구현 | 요구만 제시 |
| 문제 3 | 구현 | 요구만 제시 |
| 문제 4 | 미완성 구현 | 요구만 제시 |
| 문제 5 | 부분 구현·오류 존재 | 요구만 제시 |
| 전체 코드량 | 매우 큼 | 간결 |

---

## 40. 내 코드 장점

- focus, blur, input event를 상세히 설명했다.
- 붙여넣기도 input event가 감지한다는 점을 기록했다.
- submit 기본 동작과 preventDefault를 설명했다.
- target, currentTarget, this를 실제로 출력했다.
- event delegation과 custom attribute 조회를 구현했다.
- 주문·배송 정보 복사를 완성했다.
- 로그인 오류와 성공 초기화를 구현했다.
- 피자 size와 topping 가격을 합산했다.
- 문제 1~5를 직접 시도해 실습 범위를 확장했다.
- Todo의 개별 삭제, 취소선, 전체 선택, 선택 삭제를 각각 구현하려 했다.

---

## 41. 내 코드 개선점

- bubbling과 capturing 방향 설명이 반대다.
- stopPropagation을 capturing 방지라고 설명했다.
- event handler의 this에 기본적으로 window가 있다고 설명한 부분이 부정확하다.
- board와 tr listener를 동시에 활성화해 일부 log가 중복된다.
- checkbox stopPropagation 때문에 상위 value 분기는 실행되지 않는다.
- `==`를 반복 사용한다.
- `log()`가 `innerHTML`을 사용한다.
- 피자 topping 이름 사이에 구분자가 없다.
- 메뉴 선택 시 기존 항목을 해제하지 않는다.
- 메뉴를 반복 클릭하면 `✔`가 누적된다.
- Todo 빈 입력에서도 빈 div를 먼저 추가한다.
- 빈 입력 후 `deleteCol`이 null이면 TypeError가 발생한다.
- Todo text를 `innerHTML`에 넣어 XSS 위험이 있다.
- Todo 전역 listener를 항목 추가 때마다 반복 등록한다.
- 모든 개별 항목을 체크해도 전체 선택이 자동으로 켜지지 않는다.
- placeholder text를 제거하지 않는다.
- 문서 `lang="en"`과 `<title>Document</title>`이 내용에 맞지 않는다.

---

## 42. 강사님 코드 장점

- 검색 form event 흐름이 간결하다.
- focus·blur·input·submit을 순서대로 학습할 수 있다.
- target, currentTarget, this를 비교한다.
- child1에서 stopPropagation을 확인한다.
- tr별 target 판정으로 checkbox, title, writer를 구분한다.
- checkbox에서 부모 tr의 title을 찾는다.
- 문제 1~5 요구사항을 구체적으로 제시한다.

---

## 43. 강사님 코드 개선점

- board 하나에 위임하는 예제는 주석 처리되어 있다.
- tr마다 listener를 등록한다.
- checkbox stopPropagation으로 tr의 checkbox value 분기가 실행되지 않는다.
- `log()`가 innerHTML을 사용한다.
- `parseInt(Math.random() * 256)`보다 Math.floor가 명확하다.
- `==`를 사용한다.
- this와 arrow function 주석이 지나치게 일반화되어 있다.
- 문제 1~5 정답 구현이 없다.
- 문서 lang과 title이 내용에 맞지 않는다.

---

# Improvements

## 44. 핵심 개선 원칙

1. form 검증 실패 때만 `preventDefault()`를 호출한다.
2. table event는 상위 요소 하나에 위임한다.
3. `target.closest()`로 의도한 요소를 찾는다.
4. 상태 class는 `"true"` 대신 `"active"`, `"done"`처럼 의미 있게 정한다.
5. 사용자 입력은 `innerHTML`에 직접 삽입하지 않는다.
6. 전역 button listener는 초기화 시 한 번만 등록한다.
7. 생성 요소는 생성한 node 참조로 직접 다룬다.
8. 전체 선택은 현재 DOM을 다시 조회해 계산한다.
9. 가격과 이름은 space split보다 `data-*` 또는 객체로 분리한다.
10. 화면 금액은 `toLocaleString("ko-KR")`로 표시할 수 있다.

예:

```js
orderPrice.textContent =
  `총액: ${priceResult
    .toLocaleString(
      "ko-KR"
    )}원`
```

---

# Common Mistakes

## 45. 자주 하는 실수

### 45.1 Capturing과 Bubbling 방향을 반대로 설명

capturing은 상위에서 target 방향, bubbling은 target에서 상위 방향입니다.

### 45.2 PreventDefault와 StopPropagation 혼동

기본 동작과 event 전파는 서로 다른 개념입니다.

### 45.3 Target과 CurrentTarget 혼동

target은 실제 발생 요소, currentTarget은 현재 listener 요소입니다.

### 45.4 Form.submit()이 Submit Event를 다시 호출한다고 생각

직접 `submit()`은 일반적으로 submit event를 다시 발생시키지 않습니다.

### 45.5 Parent와 Child에 중복 Listener 등록

같은 click이 여러 handler에서 처리되어 log가 중복될 수 있습니다.

### 45.6 사용자 입력을 InnerHTML에 결합

Todo 입력을 통해 HTML injection이 가능해집니다.

### 45.7 검증 전에 빈 Element 추가

빈 Todo div가 남고 null property 오류가 발생할 수 있습니다.

### 45.8 항목 추가 때마다 전역 Listener 등록

listener 수가 항목 수만큼 증가합니다.

### 45.9 메뉴 기존 상태를 제거하지 않음

여러 메뉴가 동시에 선택되고 check mark가 누적됩니다.

### 45.10 Checkbox 전체 상태를 일부 항목만 보고 판단

모든 checkbox를 `every()`로 확인해야 합니다.

---

# Interview / Review

## 46. 면접·복습 포인트

### Q1. Input Event는 언제 발생하나요?

input의 값이 keyboard, 붙여넣기, 삭제 등으로 변경될 때 발생합니다.

### Q2. Submit에서 PreventDefault를 사용하는 이유는 무엇인가요?

기본 form 제출을 잠시 막고 JavaScript 검증을 수행하기 위해서입니다.

### Q3. Target과 CurrentTarget의 차이는 무엇인가요?

target은 실제 event 발생 요소이고 currentTarget은 현재 listener가 실행 중인 요소입니다.

### Q4. Capturing과 Bubbling 방향은 어떻게 되나요?

capturing은 상위에서 target으로, bubbling은 target에서 상위로 진행됩니다.

### Q5. StopPropagation은 무엇을 막나요?

현재 event가 다음 상위 또는 하위 전파 경로로 계속 이동하는 것을 막습니다.

### Q6. Event Delegation의 장점은 무엇인가요?

부모 listener 하나로 여러 자식과 동적 자식을 처리할 수 있습니다.

### Q7. 내 게시판에서 title log가 두 번 나올 수 있는 이유는 무엇인가요?

board listener와 tr listener가 모두 활성화되어 같은 bubbling click을 처리하기 때문입니다.

### Q8. 피자 topping 출력의 문제는 무엇인가요?

문자열에 구분자를 넣지 않아 topping 이름들이 붙어서 출력됩니다.

### Q9. Todo 빈 입력 때 발생할 수 있는 오류는 무엇인가요?

빈 div를 먼저 넣고 delete button이 없는 상태에서 null에 addEventListener를 호출할 수 있습니다.

### Q10. 전체 선택 상태는 어떻게 계산하나요?

현재 checkbox가 하나 이상 있고 모든 checkbox가 checked인지 `every()`로 확인합니다.

---

# Problems

## 문제 1. Focus와 Blur

input이 focus되면 yellow, blur되면 원래 배경으로 돌아오게 작성하세요.

## 문제 2. Input Log

input 값이 변경될 때 현재 value를 출력하세요.

## 문제 3. 검색어 검증

검색어가 두 글자 미만일 때 제출을 막고 경고를 표시하세요.

## 문제 4. Event 단계

capturing과 bubbling의 진행 방향을 작성하세요.

## 문제 5. Target 비교

자식 click 시 target과 currentTarget을 출력하세요.

## 문제 6. StopPropagation

`#child1` click이 부모 listener까지 올라가지 않게 하세요.

## 문제 7. Table Delegation

`#board` listener 하나로 title과 writer click을 처리하세요.

## 문제 8. Checkbox Title

checkbox click 시 같은 tr의 제목을 출력하세요.

## 문제 9. 주문·배송 복사

checkbox를 선택하면 주문 이름·주소를 배송 정보에 복사하세요.

## 문제 10. 주문·배송 초기화

checkbox를 해제하면 배송 이름·주소를 지우세요.

## 문제 11. 로그인 검증

id와 password가 비어 있으면 각각 오류 문구를 표시하세요.

## 문제 12. 로그인 성공

두 값이 있으면 기존 오류 문구를 지우세요.

## 문제 13. 피자 Size 분석

`"medium 20000"`에서 이름과 가격을 분리하세요.

## 문제 14. Topping 총액

선택된 topping 가격을 모두 합산하세요.

## 문제 15. 주문 총액

size와 topping 총액을 합산하고 원 단위로 표시하세요.

## 문제 16. Topping 이름

선택 topping 이름을 쉼표로 연결하세요.

## 문제 17. 메뉴 단일 선택

클릭한 메뉴 하나만 active class를 가지게 하세요.

## 문제 18. Todo 안전 생성

사용자 입력을 innerHTML 없이 checkbox, text, button으로 생성하세요.

## 문제 19. Todo 빈 값

빈 입력일 때 아무 DOM도 추가하지 않도록 작성하세요.

## 문제 20. Todo 전체 선택

전체 선택 checkbox로 현재 모든 Todo를 선택·해제하세요.

## 문제 21. Todo 상태 동기화

개별 checkbox 상태에 따라 전체 선택을 자동 갱신하세요.

## 문제 22. 종합 Todo

다음 요구사항을 만족하세요.

- 추가, 개별 삭제, 선택 삭제
- 전체 선택과 개별 상태 양방향 동기화
- 체크 항목 취소선
- 빈 값 검증
- 사용자 text는 `textContent`
- 전역 listener는 한 번만 등록
- 동적 항목은 event delegation 또는 생성 시 listener 연결
- 항목이 없으면 전체 선택 해제

---

# Answers

## 정답 1

```js
query.addEventListener(
  "focus",
  function() {
    query.style
      .backgroundColor =
      "yellow"
  }
)

query.addEventListener(
  "blur",
  function() {
    query.style
      .backgroundColor =
      ""
  }
)
```

## 정답 2

```js
query.addEventListener(
  "input",
  function() {
    console.log(
      query.value
    )
  }
)
```

## 정답 3

```js
form.addEventListener(
  "submit",
  function(event) {
    if (
      query.value
        .trim()
        .length < 2
    ) {
      event.preventDefault()

      alert(
        "검색어는 두 글자 이상입니다."
      )
    }
  }
)
```

## 정답 4

```text
capturing
→ 상위 요소에서 target 방향

bubbling
→ target에서 상위 요소 방향
```

## 정답 5

```js
parent.addEventListener(
  "click",
  function(event) {
    console.log(
      event.target
    )

    console.log(
      event.currentTarget
    )
  }
)
```

## 정답 6

```js
child1.addEventListener(
  "click",
  function(event) {
    event.stopPropagation()
  }
)
```

## 정답 7

```js
board.addEventListener(
  "click",
  function(event) {
    const target =
      event.target

    if (
      target.matches(
        ".title"
      )
    ) {
      console.log(
        target.textContent
      )
    }

    if (
      target.hasAttribute(
        "writer"
      )
    ) {
      console.log(
        target.getAttribute(
          "writer"
        )
      )
    }
  }
)
```

## 정답 8

```js
board.addEventListener(
  "click",
  function(event) {
    if (
      !event.target.matches(
        ".chk"
      )
    ) {
      return
    }

    const row =
      event.target.closest(
        "tr"
      )

    console.log(
      row
        .querySelector(
          ".title"
        )
        .textContent
    )
  }
)
```

## 정답 9

```js
valueChk.addEventListener(
  "change",
  function() {
    if (!valueChk.checked) {
      return
    }

    name2.value =
      name1.value

    address2.value =
      address1.value
  }
)
```

## 정답 10

```js
if (!valueChk.checked) {
  name2.value =
    ""

  address2.value =
    ""
}
```

## 정답 11

```js
if (
  id.value.trim() === ""
) {
  error.textContent =
    "아이디를 입력하세요."
} else if (
  password.value.trim() === ""
) {
  error.textContent =
    "패스워드를 입력하세요."
}
```

## 정답 12

```js
else {
  error.textContent =
    ""
}
```

## 정답 13

```js
const [
  sizeName,
  sizePrice
] =
  "medium 20000"
    .split(" ")

console.log(
  sizeName,
  Number(sizePrice)
)
```

## 정답 14

```js
const toppings =
  document.querySelectorAll(
    ".topping:checked"
  )

let total = 0

toppings.forEach(
  function(topping) {
    total +=
      Number(
        topping.value
          .split(" ")[1]
      )
  }
)
```

## 정답 15

```js
const total =
  sizePrice +
  toppingPrice

orderPrice.textContent =
  `총액: ${total
    .toLocaleString(
      "ko-KR"
    )}원`
```

## 정답 16

```js
const names =
  [
    ...document
      .querySelectorAll(
        ".topping:checked"
      )
  ].map(
    function(topping) {
      return topping.value
        .split(" ")[0]
    }
  )

console.log(
  names.join(", ")
)
```

## 정답 17

```js
items.addEventListener(
  "click",
  function(event) {
    const selected =
      event.target.closest(
        ".menu-item"
      )

    if (selected === null) {
      return
    }

    items
      .querySelectorAll(
        ".menu-item"
      )
      .forEach(
        function(item) {
          item.classList.remove(
            "active"
          )
        }
      )

    selected.classList.add(
      "active"
    )
  }
)
```

## 정답 18

```js
const row =
  document.createElement(
    "div"
  )

const checkbox =
  document.createElement(
    "input"
  )

checkbox.type =
  "checkbox"

const text =
  document.createElement(
    "span"
  )

text.textContent =
  inputText.value

const button =
  document.createElement(
    "button"
  )

button.type =
  "button"

button.textContent =
  "삭제"

row.append(
  checkbox,
  text,
  button
)
```

## 정답 19

```js
const value =
  inputText.value.trim()

if (value === "") {
  alert(
    "할 일은 한 글자 이상 입력하세요."
  )

  return
}
```

## 정답 20

```js
allCheckbox.addEventListener(
  "change",
  function() {
    column
      .querySelectorAll(
        ".todo-check"
      )
      .forEach(
        function(checkbox) {
          checkbox.checked =
            allCheckbox.checked
        }
      )
  }
)
```

## 정답 21

```js
function updateAll() {
  const checkboxes =
    [
      ...column
        .querySelectorAll(
          ".todo-check"
        )
    ]

  allCheckbox.checked =
    checkboxes.length > 0 &&
    checkboxes.every(
      function(checkbox) {
        return checkbox.checked
      }
    )
}
```

## 정답 22

```js
const column =
  document.querySelector(
    "#column"
  )

function updateAll() {
  const checkboxes =
    [
      ...column
        .querySelectorAll(
          ".todo-check"
        )
    ]

  allCheckbox.checked =
    checkboxes.length > 0 &&
    checkboxes.every(
      checkbox =>
        checkbox.checked
    )
}

addButton.addEventListener(
  "click",
  function() {
    const value =
      input.value.trim()

    if (value === "") {
      alert(
        "할 일을 입력하세요."
      )

      return
    }

    const row =
      document.createElement(
        "div"
      )

    row.className =
      "todo-row"

    const checkbox =
      document.createElement(
        "input"
      )

    checkbox.type =
      "checkbox"

    checkbox.className =
      "todo-check"

    const text =
      document.createElement(
        "span"
      )

    text.textContent =
      value

    const remove =
      document.createElement(
        "button"
      )

    remove.type =
      "button"

    remove.textContent =
      "삭제"

    row.append(
      checkbox,
      text,
      remove
    )

    column.prepend(row)
    input.value = ""
  }
)

column.addEventListener(
  "change",
  function(event) {
    if (
      !event.target.matches(
        ".todo-check"
      )
    ) {
      return
    }

    event.target
      .closest(".todo-row")
      .classList
      .toggle(
        "done",
        event.target.checked
      )

    updateAll()
  }
)

column.addEventListener(
  "click",
  function(event) {
    if (
      event.target
        .matches(
          ".todo-remove"
        )
    ) {
      event.target
        .closest(".todo-row")
        .remove()

      updateAll()
    }
  }
)

allCheckbox.addEventListener(
  "change",
  function() {
    column
      .querySelectorAll(
        ".todo-check"
      )
      .forEach(
        function(checkbox) {
          checkbox.checked =
            allCheckbox.checked

          checkbox
            .closest(".todo-row")
            .classList
            .toggle(
              "done",
              checkbox.checked
            )
        }
      )
  }
)

deleteSelected.addEventListener(
  "click",
  function() {
    column
      .querySelectorAll(
        ".todo-check:checked"
      )
      .forEach(
        function(checkbox) {
          checkbox
            .closest(".todo-row")
            .remove()
        }
      )

    updateAll()
  }
)
```

> 위 종합 예제에서는 삭제 button에 `todo-remove` class를 지정해야 합니다.

---

# Final Checklist

## Form

- [ ] focus와 blur를 구분했다.
- [ ] input event가 붙여넣기도 감지함을 이해했다.
- [ ] 검색어를 trim 후 검증했다.
- [ ] 검증 실패 때 기본 제출을 막았다.
- [ ] form.submit과 requestSubmit 차이를 이해했다.
- [ ] 난수 정수화에 Math.floor 사용을 검토했다.

## Event 전파

- [ ] capturing과 bubbling 방향을 정확히 이해했다.
- [ ] target과 currentTarget을 구분했다.
- [ ] 일반 함수 handler의 this를 확인했다.
- [ ] preventDefault와 stopPropagation을 구분했다.
- [ ] board와 tr listener 중복을 확인했다.
- [ ] checkbox의 stopPropagation 결과를 확인했다.
- [ ] parentNode 대신 closest 사용을 검토했다.

## 실전 문제

- [ ] 주문·배송 checkbox 상태를 처리했다.
- [ ] 로그인 오류와 성공 초기화를 구현했다.
- [ ] size와 topping 가격을 숫자로 변환했다.
- [ ] topping 이름을 구분자로 연결했다.
- [ ] 메뉴에서 기존 active 상태를 제거했다.
- [ ] 같은 메뉴 click 시 check mark가 중복되지 않게 했다.
- [ ] Todo 입력 검증을 DOM 생성보다 먼저 수행했다.
- [ ] 사용자 입력을 textContent로 넣었다.
- [ ] 전역 listener를 한 번만 등록했다.
- [ ] 전체 선택과 개별 선택을 양방향 동기화했다.
- [ ] 선택 삭제 후 전체 상태를 갱신했다.

## 원본 검수

- [ ] 두 실제 17_event_form.html을 비교했다.
- [ ] 연결된 두 실제 17_event_form.js를 비교했다.
- [ ] 강사님 문제 1~5가 요구사항만임을 기록했다.
- [ ] 내 문제 1~5 구현을 기록했다.
- [ ] board listener 활성 여부 차이를 기록했다.
- [ ] bubbling·capturing 주석 오류를 기록했다.
- [ ] 메뉴 선택 미완성 상태를 기록했다.
- [ ] Todo 빈 입력 TypeError 가능성을 기록했다.
- [ ] Todo listener 중복 등록을 기록했다.
- [ ] Todo innerHTML 위험을 기록했다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 17번은 form event, event 전파, delegation과 다섯 개의 실전 문제를 다룬다.
- focus는 초점을 얻을 때, blur는 잃을 때 발생한다.
- input event는 keyboard뿐 아니라 붙여넣기 등 실제 값 변경을 감지한다.
- submit event에서 `preventDefault()`로 기본 제출을 막고 검증할 수 있다.
- 현재 원본의 `form.submit()`은 submit event를 다시 발생시키지 않아 재귀되지 않는다.
- capturing은 상위에서 target 방향, bubbling은 target에서 상위 방향이다.
- 내 원본 주석은 두 방향을 반대로 설명했다.
- target은 실제 발생 요소, currentTarget은 listener가 등록된 요소다.
- 일반 함수 listener의 this는 일반적으로 currentTarget과 같다.
- stopPropagation은 기본 동작이 아니라 event 전파를 막는다.
- 내 코드는 board와 각 tr listener가 모두 활성화되어 title과 writer log가 중복될 수 있다.
- checkbox listener의 stopPropagation 때문에 상위 checkbox value 분기는 실행되지 않는다.
- 강사님 코드는 문제 1~5 요구만 제시하고 내 코드는 HTML과 JavaScript를 직접 구현했다.
- 주문·배송 문제는 checkbox 선택 시 값을 복사하고 해제 시 지운다.
- 로그인 문제는 id와 password 오류를 구분하고 성공하면 문구를 지운다.
- 피자 총액은 size 가격과 선택 topping 가격을 합산한다.
- topping 이름은 현재 구분자 없이 이어 붙여진다.
- 메뉴 선택은 기존 메뉴를 해제하지 않아 여러 메뉴가 동시에 굵게 남는다.
- 같은 메뉴를 반복 click하면 `✔`가 계속 누적된다.
- Todo는 빈 입력 검증 전에 빈 div를 삽입한다.
- 빈 입력일 때 delete button이 없어 null에 addEventListener를 호출할 수 있다.
- Todo 사용자 입력을 innerHTML로 넣어 XSS 위험이 있다.
- Todo 추가 때마다 all select, selected delete, 기존 checkbox listener를 반복 등록한다.
- 개별 checkbox를 모두 선택해도 전체 선택을 true로 만드는 로직은 구현되지 않았다.
- 안전한 Todo는 입력 검증 후 createElement와 textContent로 만들고 전역 listener를 한 번만 등록한다.
