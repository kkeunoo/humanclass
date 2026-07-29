# JavaScript DOM 콘텐츠 생성과 스타일 조작

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `12_JavaScript_DOM콘텐츠생성과_스타일조작.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `11_JavaScript_DOM선택과_속성클래스조작.md` |
| 다음 학습 | `13_JavaScript_DOM이벤트.md` |
| 원본 기준 | `workspace/workspace_html/javascript/12_dom_content.html`, `workspace_teacher/workspace_html/javascript/12_dom_content.html` |
| 핵심 범위 | `textContent`, `innerText`, `innerHTML`, XSS 주의, `createElement()`, `append()`, `appendChild()`, `prepend()`, `before()`, `after()`, 동적 표 생성, 역순 누적, 동적 `<style>` 생성, 인라인 스타일, `getComputedStyle()`, 픽셀값 계산, DOM 퀴즈 |
| 프로젝트 연결 | 게시판 렌더링, 실시간 카운터와 시계, 동적 목록·표 생성, 상태 메시지 변경, 콘텐츠 마스킹, 스타일 계산 및 변경 |

> 이 문서는 내 코드와 강사님 코드의 `12_dom_content.html`을 직접 비교해 작성했습니다. 강사님 코드는 DOM 콘텐츠 읽기·변경, DOM 생성, 게시판 출력, style 조작까지 구현하고 마지막 문제 1~4는 요구사항만 제시합니다. 내 코드는 문제 1~4를 모두 구현하고 시계에 시·밀리초를 추가하며 주석을 크게 확장했습니다. 원본의 `javascript:` URL 삽입, 반복적인 `innerHTML` 재할당, `parseInt(Math.random() * 100)`, teacher 문서의 퀴즈 요소 위치 문제, 문제 3 예시 불일치, 내 코드의 느슨한 비교와 공백 판정은 원본을 보존한 뒤 정확한 동작과 개선점을 별도로 설명합니다.

---

# 학습 목표

- `textContent`, `innerText`, `innerHTML`의 읽기 차이를 설명한다.
- 세 속성으로 콘텐츠를 변경했을 때 태그 해석 여부를 구분한다.
- `innerHTML`에 신뢰할 수 없는 문자열을 넣을 때의 보안 위험을 이해한다.
- 실시간 카운터와 시계를 `setInterval()`로 갱신한다.
- `document.createElement()`로 메모리상의 DOM 요소를 만든다.
- 생성한 요소가 문서에 삽입되기 전까지 화면에 나타나지 않는다는 점을 이해한다.
- `append()`, `appendChild()`, `prepend()`, `before()`, `after()`를 비교한다.
- 같은 DOM 객체를 여러 번 삽입하면 복제되지 않고 이동한다는 점을 이해한다.
- 2차원 배열을 이용해 표 행과 셀을 동적으로 만든다.
- DOM API 방식과 `innerHTML` 문자열 방식의 장단점을 비교한다.
- `element.style`과 `getComputedStyle()`의 차이를 설명한다.
- CSS의 kebab-case 속성을 JavaScript camelCase로 작성한다.
- CSS 길이 문자열에서 숫자를 추출해 계산한다.
- NodeList의 각 요소에서 `classList.contains()`를 사용한다.
- 공백만 있는 콘텐츠를 안전하게 판정한다.
- 내 코드와 강사님 코드의 실행 시점·HTML 위치 차이를 정확히 기록한다.

---

# 1. 콘텐츠를 읽는 세 가지 방법

원본 HTML:

```html
<div id="msg">
  <span>원래</span> 있던   글씨
</div>
```

선택:

```js
const msg =
  document.querySelector(
    "#msg"
  )
```

세 가지 대표 접근:

```js
msg.textContent
msg.innerText
msg.innerHTML
```

모두 요소 내부 콘텐츠를 다루지만 반환 기준이 다릅니다.

---

# 2. TextContent

공통 원본:

```js
console.log(
  "msg.textContent",
  msg.textContent
)
```

`textContent`는 하위 요소의 tag 자체는 제외하고 text node 내용을 가져옵니다.

소스에 존재하는 줄바꿈과 들여쓰기 공백도 포함될 수 있습니다.

```text
<span>원래</span>
→ tag는 제외
→ "원래" text는 포함
```

---

# 3. InnerText

공통 원본:

```js
console.log(
  "msg.innerText",
  msg.innerText
)
```

`innerText`는 사용자에게 렌더링되는 text를 기준으로 동작합니다.

CSS에 따라 숨겨진 요소나 줄바꿈 처리에서 `textContent`와 결과가 달라질 수 있습니다.

브라우저가 layout을 고려해야 하므로 단순 text node 접근인 `textContent`보다 비용이 커질 수 있습니다.

---

# 4. InnerHTML

공통 원본:

```js
console.log(
  "msg.innerHTML",
  msg.innerHTML
)
```

`innerHTML`은 요소 내부의 HTML markup을 문자열로 반환합니다.

따라서 `<span>` tag도 결과에 포함됩니다.

```html
<span>원래</span> 있던   글씨
```

---

# 5. 읽기 비교

| 속성 | 반환 기준 | 하위 Tag 문자열 포함 | 렌더링 상태 고려 |
| --- | --- | --- | --- |
| `textContent` | text node | 아니오 | 거의 고려하지 않음 |
| `innerText` | 화면에 보이는 text | 아니오 | 예 |
| `innerHTML` | HTML markup | 예 | HTML 문자열 기준 |

원본의 설명처럼 `textContent`와 `innerText`는 읽을 때 차이가 특히 중요합니다.

---

# 6. TextContent로 변경

공통 원본:

```js
msg.textContent =
  "<h1>h1제목</h1>   a   b      c"
```

`<h1>`을 실제 tag로 해석하지 않습니다.

화면에는 다음 문자열이 글자 그대로 표시됩니다.

```text
<h1>h1제목</h1> a b c
```

HTML의 일반 공백 축약 규칙 때문에 여러 space는 화면에서 하나처럼 보일 수 있습니다.

---

# 7. InnerText로 변경

공통 원본:

```js
msg.innerText =
  "<h1>h1제목</h1>   a   b      c"
```

이 경우에도 `<h1>`은 HTML tag가 아니라 text로 표시됩니다.

원본은 변경할 때 `innerText`와 `textContent`가 같은 결과처럼 보인다고 설명합니다.

현재 단순 문자열에서는 비슷하지만 줄바꿈과 렌더링 규칙에 따라 항상 완전히 동일하다고 단정할 수는 없습니다.

---

# 8. InnerHTML로 변경

공통 원본:

```js
msg.innerHTML =
  "<h1>h1제목</h1>   a   b      c"

msg.innerHTML += "d"
```

`<h1>`을 실제 HTML 요소로 파싱합니다.

최종적으로 heading과 뒤 text가 생성됩니다.

`+=`는 기존 `innerHTML` 문자열을 읽어 새 문자열을 만든 뒤 내부 DOM을 다시 파싱하는 방식입니다.

---

# 9. InnerHTML과 XSS

양쪽 원본:

```js
msg.innerHTML =
  '<a href="javascript:alert(1);alert(2);">눌러봐</a>'
```

링크를 클릭하면 `javascript:` URL이 실행될 수 있습니다.

학습용으로 HTML과 JavaScript 삽입 가능성을 보여 주지만 실제 서비스에서는 심각한 보안 위험이 될 수 있습니다.

사용자 입력을 그대로 `innerHTML`에 넣으면 XSS가 발생할 수 있습니다.

안전한 text 출력:

```js
msg.textContent =
  userInput
```

HTML이 꼭 필요하다면 신뢰할 수 있는 sanitizer와 허용 목록 정책이 필요합니다.

---

# 10. 실시간 Count

공통 구조:

```js
setInterval(
  function() {
    const count =
      document.querySelector(
        "#count"
      )

    let cnt =
      count.textContent

    cnt =
      Number(cnt) + 1

    count.innerText =
      cnt
  },
  1000
)
```

`textContent`는 문자열이므로 숫자 증가 전에 `Number()`로 변환합니다.

---

# 11. Count의 첫 실행 시점

`setInterval(callback, 1000)`은 callback을 즉시 실행하지 않습니다.

약 1초가 지난 후 첫 실행이 예약됩니다.

또한 정확히 매 1000ms마다 실행된다고 보장하지 않습니다.

main thread가 바쁘면 실행이 늦어질 수 있습니다.

---

# 12. Clock 비교

내 코드:

```js
const hour =
  now.getHours()

const min =
  now.getMinutes()

const sec =
  now.getSeconds()

const ms =
  now.getMilliseconds()

const clockNew =
  `${hour}시 ${min}분 ${sec}초.${ms}(ms)`
```

강사님 코드:

```js
const m =
  now.getMinutes()

const s =
  now.getSeconds()

const ms =
  now.getMilliseconds()

const time =
  m + "분 " +
  s + "초." +
  ms
```

내 코드는 시까지 표시하며 template literal을 사용합니다.

---

# 13. Clock 갱신 주기 차이

내 코드:

```js
}, 250)
```

강사님 코드:

```js
}, 3000)
```

내 코드는 0.25초 간격으로 예약해 밀리초 표시를 자주 갱신합니다.

강사님 코드는 3초 간격이므로 초·밀리초가 3초마다 갱신됩니다.

내 주석의 “1000ms를 3으로 나누어 delay를 해결”은 정확한 해결책은 아닙니다.

주기를 짧게 하면 표시 지연이 덜 눈에 띌 수 있지만 event loop 지연 자체를 제거하지는 못합니다.

---

# 14. Date 생성 위치

양쪽 모두 `new Date()`를 interval callback 내부에서 생성합니다.

```js
setInterval(
  function() {
    const now =
      new Date()
  },
  delay
)
```

밖에서 한 번만 생성하면 같은 Date 객체의 시간이 자동으로 현재 시각으로 갱신되지 않으므로 매 실행마다 새 시각을 읽는 현재 구조가 적절합니다.

---

# 15. CreateElement

공통 원본:

```js
const div =
  document.createElement(
    "div"
  )
```

메모리상에 `<div></div>` 요소 객체를 만듭니다.

아직 document에 연결되지 않았으므로 화면에는 나타나지 않습니다.

원본 주석의 “가상 DOM”은 React 등의 Virtual DOM 개념과 혼동될 수 있습니다.

더 정확한 표현은 **문서에 아직 연결되지 않은 DOM Element**입니다.

---

# 16. 생성 요소 설정

공통 원본:

```js
div.setAttribute(
  "id",
  "lol"
)

div.innerText =
  "정글차이"

div.setAttribute(
  "style",
  "color: red;"
)
```

완성되는 형태:

```html
<div
  id="lol"
  style="color: red;"
>
  정글차이
</div>
```

style attribute 전체 문자열보다 다음처럼 property를 직접 설정할 수도 있습니다.

```js
div.style.color =
  "red"
```

---

# 17. Append

공통 원본:

```js
const log =
  document.querySelector(
    "#log"
  )

log.append(div)
```

`div`를 `log`의 마지막 자식으로 삽입합니다.

`append()`는 Node뿐 아니라 문자열도 받을 수 있습니다.

---

# 18. Append의 문자열 처리

공통 원본:

```js
log.append(
  "<h1>abcd</h1>"
)
```

문자열은 HTML로 파싱되지 않습니다.

화면에는 `<h1>abcd</h1>`이 text로 들어갑니다.

HTML 요소를 넣으려면 `createElement()`를 사용하거나 신뢰할 수 있는 HTML에 한해 별도 파싱 방식을 사용해야 합니다.

---

# 19. 같은 Element를 두 번 Append

공통 원본:

```js
log.append(div)
log.append(div)
```

두 번째 호출에서 같은 객체가 복제되지 않습니다.

이미 삽입된 `div`가 마지막 위치로 이동합니다.

복제하려면:

```js
const copy =
  div.cloneNode(true)
```

를 사용할 수 있습니다.

---

# 20. AppendChild

공통 원본:

```js
const p =
  document.createElement(
    "p"
  )

p.textContent =
  "p태그"

log.appendChild(p)
```

`appendChild()`는 Node 하나를 마지막 자식으로 추가합니다.

문자열은 허용되지 않습니다.

```js
log.appendChild(
  "<h1>글씨</h1>"
)
```

는 TypeError를 발생시킵니다.

---

# 21. Append와 AppendChild 비교

| 구분 | `append()` | `appendChild()` |
| --- | --- | --- |
| Node 추가 | 가능 | 가능 |
| 문자열 추가 | 가능 | 불가능 |
| 여러 인수 | 가능 | 한 번에 하나 |
| 반환값 | `undefined` | 추가한 Node |

원본은 문자열 허용 여부를 중심으로 비교합니다.

---

# 22. Prepend

공통 원본:

```js
const p2 =
  document.createElement(
    "p"
  )

log.prepend(p2)
```

`log` 내부의 첫 번째 자식으로 삽입합니다.

내 text:

```text
p2 log 앞에붙이기
```

강사님 text:

```text
p2
```

동작은 같습니다.

---

# 23. Before와 After

공통 구조:

```js
log.before(p3)
log.after(p4)
```

`before()`와 `after()`는 `log`의 자식이 아니라 형제 위치에 요소를 삽입합니다.

```text
before
→ log 이전 형제

after
→ log 다음 형제
```

내 text는 `"p3 형제로 넣기"`, `"p4 형제로 넣기"`이고 강사님은 `"p3"`, `"p4"`입니다.

---

# 24. 첫 Table Row 생성

내 코드:

```js
const tbody =
  document.querySelector(
    "#tbody"
  )

const tr =
  document.createElement(
    "tr"
  )

tbody.append(tr)

const td =
  document.createElement(
    "td"
  )

tr.append(td)

td.innerText =
  "첫째칸"
```

강사님 코드:

```js
let tr =
  document.createElement(
    "tr"
  )

let td =
  document.createElement(
    "td"
  )

td.innerText =
  "첫째칸"

tr.append(td)

let tbody =
  document.querySelector(
    "#tbody"
  )

tbody.prepend(tr)
```

최종 표 내용은 같지만 삽입 순서와 `append`·`prepend`가 다릅니다.

---

# 25. Const와 Let 차이

내 코드는 `tbody`, `tr`, `td`를 `const`로 선언합니다.

강사님 코드는 `let`을 사용합니다.

변수 자체를 다른 값으로 재할당하지 않으므로 `const`가 의도를 더 명확하게 표현합니다.

DOM 요소의 내부 속성을 바꾸는 것은 const 재할당과 다른 개념입니다.

---

# 26. Rows 배열

공통 원본:

```js
const rows = [
  ["제목1", "작성자1"],
  ["제목2", "작성자2"],
  ["제목3", "작성자3"],
  ["제목4", "작성자4"],
  ["제목5", "작성자5"]
]
```

각 내부 배열은 한 게시글 행을 나타냅니다.

```text
rows[i][0]
→ 제목

rows[i][1]
→ 작성자
```

---

# 27. DOM API로 Board 생성

공통 핵심:

```js
for (
  let i = 0;
  i < rows.length;
  i++
) {
  const tr =
    document.createElement(
      "tr"
    )

  const titleCell =
    document.createElement(
      "td"
    )

  const authorCell =
    document.createElement(
      "td"
    )

  titleCell.innerText =
    rows[i][0]

  authorCell.innerText =
    rows[i][1]

  tr.append(
    titleCell,
    authorCell
  )

  board.append(tr)
}
```

각 값을 text로 넣기 때문에 사용자 문자열이 HTML tag로 실행되지 않습니다.

---

# 28. 내 Board 생성 순서

내 코드는 먼저 구조를 삽입합니다.

```js
board.append(
  tr_board
)

tr_board.append(
  td1_board
)

tr_board.append(
  td2_board
)
```

그 뒤 cell text를 설정합니다.

강사님 코드는 cell text와 tr 구조를 먼저 완성한 뒤 마지막에 board에 삽입합니다.

두 방식 모두 동작하지만 완성된 row를 한 번에 삽입하는 강사님 방식이 중간 상태 노출을 줄일 수 있습니다.

---

# 29. DocumentFragment 확장

많은 행을 만들 때 fragment에 모아 한 번에 넣을 수 있습니다.

```js
const fragment =
  document.createDocumentFragment()

for (
  const [title, author]
  of rows
) {
  const tr =
    document.createElement(
      "tr"
    )

  const td1 =
    document.createElement(
      "td"
    )

  const td2 =
    document.createElement(
      "td"
    )

  td1.textContent =
    title

  td2.textContent =
    author

  tr.append(td1, td2)
  fragment.append(tr)
}

board.append(fragment)
```

원본에는 없는 성능·구조 개선입니다.

---

# 30. InnerHTML 누적 방식

공통 원본:

```js
for (
  let i = 0;
  i < rows.length;
  i++
) {
  const html = `
    <tr>
      <td>${rows[i][0]}</td>
      <td>${rows[i][1]}</td>
    </tr>
  `

  board2.innerHTML =
    html +
    board2.innerHTML
}
```

새 문자열을 앞에 붙이므로 결과 행 순서는 역순입니다.

```text
제목5
제목4
제목3
제목2
제목1
```

---

# 31. InnerHTML 반복 재할당 문제

매 반복마다:

```js
board2.innerHTML
```

을 읽고 전체 내부 HTML을 다시 파싱합니다.

문제점:

- 기존 child node가 새 node로 교체될 수 있음
- 기존 node에 연결된 event listener가 사라질 수 있음
- 행이 많으면 비효율적
- 데이터가 신뢰되지 않으면 XSS 위험

작은 학습 예제에서는 결과를 확인할 수 있지만 실무에서는 문자열을 한 번 누적한 뒤 한 번만 대입하거나 DOM API를 사용하는 편이 안전합니다.

---

# 32. “중간까지 남아서 안전” 설명 검토

내 코드 주석:

```text
한 번에 만든 html은 error가 나면 전체 추가가 안 되지만,
반복마다 넣으면 앞 행은 남아서 안전
```

반복마다 성공한 행이 이미 DOM에 들어가 있으므로 뒤 반복에서 오류가 발생할 때 앞 결과가 남을 수 있다는 뜻에서는 맞습니다.

하지만 이를 일반적으로 “더 안전하다”고 말하기는 어렵습니다.

반복적인 `innerHTML` 재파싱과 부분 완료 상태가 오히려 문제일 수 있습니다.

오류 처리와 원자적 갱신 요구에 따라 방식을 선택해야 합니다.

---

# 33. 문자열 역순 누적

공통 원본:

```js
let str = ""

for (
  let i = 0;
  i < 5;
  i++
) {
  str =
    i + str
}
```

실행:

```text
i=0 → "0"
i=1 → "10"
i=2 → "210"
i=3 → "3210"
i=4 → "43210"
```

결과:

```text
43210
```

앞에 붙이는 방식이 board2 역순 행 생성과 같은 원리입니다.

---

# 34. 동적 Style 생성

공통 원본:

```js
const body =
  document.querySelector(
    "body"
  )

const style =
  document.createElement(
    "style"
  )

style.innerText = `
  #board {
    border: 1px solid red;
  }
`

body.append(style)
```

JavaScript로 `<style>` 요소를 만들고 document에 삽입합니다.

일반적으로 style은 `<head>`에 추가하는 편이 문서 구조상 자연스럽습니다.

```js
document.head.append(
  style
)
```

---

# 35. 동적 Script 생성

양쪽 원본에 주석 처리된 코드:

```js
const script =
  document.createElement(
    "script"
  )

script.innerText = `
  alert(1)
`

body.append(script)
```

실제로 실행하면 동적으로 삽입된 script가 실행될 수 있습니다.

외부 입력을 script 내용으로 넣어서는 안 됩니다.

보안 정책과 CSP에 의해 실행이 제한될 수도 있습니다.

---

# 36. Element.style

공통 원본:

```js
const clock =
  document.getElementById(
    "clock"
  )

clock.style.color =
  "red"

clock.style.fontSize =
  "1.5em"
```

`element.style`은 해당 요소의 inline style을 읽고 변경합니다.

결과:

```html
<div
  id="clock"
  style="color: red; font-size: 1.5em;"
>
```

---

# 37. CamelCase CSS Property

CSS:

```css
font-size
background-color
```

JavaScript style property:

```js
clock.style.fontSize
clock.style.backgroundColor
```

hyphen을 제거하고 뒤 단어 첫 글자를 대문자로 연결합니다.

CSS custom property는 `setProperty()`를 사용할 수 있습니다.

```js
clock.style.setProperty(
  "--accent-color",
  "red"
)
```

---

# 38. Inline Style 조회

공통 원본:

```js
console.log(
  clock.style
)

console.log(
  clock.style.color
)

console.log(
  clock.style.height
)
```

`clock.style`은 inline style만 직접 나타냅니다.

stylesheet에서 적용된 값이 있어도 inline으로 지정되지 않았다면 `clock.style.height`는 빈 문자열일 수 있습니다.

---

# 39. GetComputedStyle

공통 원본:

```js
let w =
  window
    .getComputedStyle(
      clock,
      null
    )
    .getPropertyValue(
      "width"
    )

console.log("w", w)
```

`getComputedStyle()`은 cascade와 layout 계산 후 실제 적용된 style 값을 읽습니다.

반환값은 읽기 전용 style 정보입니다.

현대 사용에서는 두 번째 인수 `null`을 생략할 수 있습니다.

```js
getComputedStyle(
  clock
).width
```

---

# 40. Border 차이

내 코드:

```js
clock.style.border =
  "1px solid red"
```

강사님 코드:

```js
clock.style.border =
  "1px solid salmon"
```

색상만 다르며 동작은 같습니다.

---

# 41. Random Height

양쪽 핵심:

```js
clock.style.height =
  parseInt(
    Math.random() * 100
  ) + "px"
```

`Math.random() * 100`은 0 이상 100 미만의 숫자입니다.

양수에서 `parseInt()`가 정수 부분을 남기므로 현재 결과는 0~99px입니다.

더 명확한 표현:

```js
Math.floor(
  Math.random() * 100
)
```

---

# 42. 기존 높이보다 5px 증가

강사님 코드:

```js
clock.style.height =
  parseInt(
    clock.style.height
  ) +
  5 +
  "px"
```

내 코드:

```js
let n =
  Number(
    clock.style.height
      .split("px")[0]
  )

let t =
  n + 5

clock.style.height =
  t + "px"
```

두 방식 모두 현재 `"66px"` 같은 단순 문자열에서는 동작합니다.

---

# 43. CSS 단위 문자열 처리 주의

```js
parseInt("1.5em")
// 1

parseInt("auto")
// NaN
```

항상 px라고 가정할 수는 없습니다.

정확한 계산에는 computed style, 단위 확인, `parseFloat()` 등을 고려해야 합니다.

현재 원본은 직접 px를 넣은 직후 읽으므로 전제가 유지됩니다.

---

# 44. 문제 1: 문자열 추가

내 코드 구현:

```js
let Q1_query =
  document.querySelector(
    ".quiz.q1"
  )

Q1_query.innerText +=
  " 쮸인님~♥"
```

결과:

```text
힌트만 달라 쮸인님~♥
```

강사님 코드는 문제 요구만 있고 구현하지 않습니다.

---

# 45. 문제 2: Q2 Class 개수

내 HTML에는 script보다 앞에 quiz 요소들이 있습니다.

```html
<div class="quiz q2">
  퀴즈2
</div>

<div class="quiz q2">
</div>
```

내 구현:

```js
const quizzes =
  document.querySelectorAll(
    "div.quiz"
  )

let q2Count = 0

for (
  let i = 0;
  i < quizzes.length;
  i++
) {
  const isQ2 =
    quizzes[i]
      .classList
      .contains("q2")

  if (isQ2 == true) {
    q2Count++
  }
}
```

결과는 2입니다.

---

# 46. NodeList Contains 오류 방지

잘못된 코드:

```js
const quizzes =
  document.querySelectorAll(
    "div.quiz"
  )

quizzes.classList.contains(
  "q2"
)
```

`quizzes`는 NodeList이므로 `classList`가 없습니다.

내 코드는 index로 각 Element에 접근합니다.

```js
quizzes[i]
  .classList
  .contains("q2")
```

이전 대화에서 발생했던 `property를 읽을 수 없음` 문제와 직접 연결되는 핵심입니다.

---

# 47. 문제 2 개선

내 코드:

```js
if (isQ2 == true)
```

Boolean은 직접 검사할 수 있습니다.

```js
if (isQ2)
```

더 간단한 selector:

```js
const q2Elements =
  document.querySelectorAll(
    "div.quiz.q2"
  )

console.log(
  q2Elements.length
)
```

---

# 48. 문제 3: Q2 Text 출력

내 코드:

```js
let Q3_query =
  document.querySelectorAll(
    "div.quiz.q2"
  )

let Q3_str = ""

for (
  let i = 0;
  i < Q3_query.length;
  i++
) {
  Q3_str +=
    `${i + 1}번째 값 : ` +
    `${Q3_query[i].textContent}\n`
}

console.log(Q3_str)
```

현재 내 HTML의 exact `q2` 요소 text:

```text
퀴즈2
공백만 있는 문자열
```

두 번째 요소는 source에 space가 있으므로 `textContent`에는 공백이 포함될 수 있습니다.

---

# 49. 강사님 문제 3 예시 불일치

강사님 주석:

```text
q2를 가지는 태그의 글씨를 출력

퀴즈2-1
```

하지만 `class="q2-1"`은 정확한 class token `"q2"`를 가진 것이 아닙니다.

`classList.contains("q2")`는 `q2-1`을 q2로 판정하지 않습니다.

정확한 q2 요소의 text는:

```text
퀴즈2
빈 내용
```

강사님 문제 3의 예시 `"퀴즈2-1"`은 요구와 일치하지 않습니다.

---

# 50. 문제 4: 빈 콘텐츠 채우기

내 코드:

```js
let Q4_query =
  document.querySelectorAll(
    "div.quiz"
  )

for (
  let i = 0;
  i < Q4_query.length;
  i++
) {
  if (
    Q4_query[i].innerText == ""
  ) {
    Q4_query[i].innerText =
      "비어있음"

    Q4_query[i].style.background =
      "red"
  }
}
```

공백만 있는 q2 요소를 찾아 text를 바꾸려는 구현입니다.

---

# 51. 공백 판정 개선

공백 종류와 브라우저 렌더링에 의존하지 않으려면 `textContent.trim()`이 명확합니다.

```js
if (
  element
    .textContent
    .trim() === ""
) {
  element.textContent =
    "비어있음"
}
```

원본 주석에도 `textContent` 사용 시 `trim()`을 사용할 수 있다고 기록되어 있습니다.

---

# 52. 강사님 문서의 Quiz 위치 문제

강사님 문서의 문제 설명은 `<script>` 내부 마지막에 있습니다.

실제 quiz 2 요소들은 닫는 `</script>` 뒤, 즉 script 실행 이후에 작성되어 있습니다.

```html
</script>

<div class="quiz q2">
  퀴즈2
</div>
```

따라서 강사님이 script 안에서 문제 2~4 코드를 그대로 구현하면 실행 시점에는 뒤의 quiz 요소가 아직 DOM에 존재하지 않습니다.

결과:

```js
document.querySelectorAll(
  "div.quiz"
).length
// 0
```

해결:

- quiz HTML을 script보다 앞으로 이동
- script에 `defer` 사용
- `DOMContentLoaded` 이후 실행

내 문서는 quiz 요소가 script보다 앞에 있어 구현이 정상 실행됩니다.

---

# 53. 강사님 문서의 Q1 요소 부재

강사님 문제 1 주석은 다음 HTML을 전제로 합니다.

```html
<div class="quiz q1">
  힌트만 달라
</div>
```

그러나 강사님 원본 실제 HTML에는 `quiz q1` 요소가 없습니다.

따라서 문제 1을 그대로 구현하면:

```js
document.querySelector(
  ".quiz.q1"
)
// null
```

이후 `innerText` 접근 시 TypeError가 발생합니다.

내 원본에는 `quiz q1` 요소가 script 앞에 존재합니다.

---

# 54. My Code 분석

## 54.1 장점

- textContent, innerText, innerHTML 차이를 상세히 설명했다.
- 콘텐츠 읽기와 변경을 구분해 기록했다.
- innerHTML이 tag를 실제 HTML로 처리한다는 점을 보여 줬다.
- count의 문자열 값을 Number로 변환해 증가시켰다.
- 시·분·초·밀리초를 250ms 간격으로 갱신했다.
- createElement부터 attribute, text, style 설정 과정을 단계적으로 설명했다.
- append와 appendChild의 문자열 처리 차이를 설명했다.
- 같은 객체를 다시 append하면 이동한다는 점을 기록했다.
- prepend, before, after의 위치 차이를 설명했다.
- DOM API로 표를 동적으로 완성했다.
- innerHTML을 이용한 역순 표 생성도 비교했다.
- inline style과 computed style 차이를 상세히 주석으로 남겼다.
- CSS px 문자열을 숫자로 바꿔 5를 더하는 과정을 풀어 작성했다.
- 강사님이 문제만 제시한 1~4를 모두 구현했다.
- 문제 2에서 NodeList의 각 요소에 접근한 뒤 contains를 사용했다.
- 문제 4에서 공백 판정을 위한 trim 대안도 주석으로 기록했다.

## 54.2 개선점

- 문서에 연결되지 않은 Element를 “가상 DOM”이라 부르면 Virtual DOM과 혼동될 수 있다.
- innerText와 textContent가 변경할 때 항상 같다고 단정하면 부정확하다.
- `javascript:` URL을 innerHTML로 삽입해 보안상 위험한 예제를 실행 가능 상태로 둔다.
- 갱신 주기를 250ms로 줄이는 것이 timer delay의 근본 해결책은 아니다.
- `innerHTML +=`와 반복 재할당은 내부 DOM을 계속 재파싱한다.
- “반복 대입이 더 안전하다”는 설명은 상황에 따라 다르다.
- style 요소는 body보다 head에 넣는 편이 자연스럽다.
- 랜덤 정수에 `parseInt()`보다 `Math.floor()`가 명확하다.
- CSS 길이 계산이 px 문자열이라는 전제에 의존한다.
- 문제 2에서 별도 전체 div count 변수가 꼭 필요하지 않다.
- Boolean 비교에 `== true`를 사용한다.
- 문제 3의 공백 text를 trim하지 않고 그대로 출력한다.
- 문제 4에서 `innerText == ""` 대신 `textContent.trim() === ""`이 더 명확하다.
- 변수명이 `Q1_query`, `Q2_divCnt` 등 대문자와 underscore를 혼합한다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.

---

# 55. Teacher Code 분석

## 55.1 장점

- textContent, innerText, innerHTML을 순서대로 비교한다.
- 세 속성을 이용해 콘텐츠를 직접 변경한다.
- count와 clock을 interval로 갱신한다.
- createElement와 DOM 삽입 API를 단계적으로 실습한다.
- append가 문자열도 받을 수 있고 appendChild는 Node만 받는다는 점을 보여 준다.
- 표 한 행 생성 후 2차원 배열 전체를 표로 렌더링한다.
- DOM API 방식과 innerHTML 방식 모두 제시한다.
- 문자열 앞쪽 누적으로 역순을 만드는 원리를 보여 준다.
- JavaScript로 style 요소를 생성한다.
- inline style과 getComputedStyle을 비교한다.
- px 문자열에 숫자 5를 더하는 방법을 보여 준다.
- 문제 1~4를 복습 과제로 제시한다.

## 55.2 개선점

- `javascript:` URL 삽입의 XSS 위험을 설명하지 않는다.
- clock이 3초마다 갱신되어 “계속 표시” 체감이 떨어질 수 있다.
- `parseInt(Math.random() * 100)`보다 Math.floor가 의도가 명확하다.
- innerHTML 반복 재할당의 node 교체와 성능 문제를 설명하지 않는다.
- `style`을 body에 추가한다.
- 문제 1의 전제인 `.quiz.q1` 요소가 실제 문서에 없다.
- 문제 2~4 대상 quiz 요소가 script 뒤에 있어 script 실행 중 선택할 수 없다.
- 문제 3 예시 `"퀴즈2-1"`은 exact class q2 요구와 일치하지 않는다.
- 문제 1~4 정답 코드가 없다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.

---

# 56. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 콘텐츠 설명 | 매우 상세 | 핵심 위주 |
| Clock 표시 | 시·분·초·ms | 분·초·ms |
| Clock 주기 | 250ms | 3000ms |
| Clock 초기 text | `시계 로딩 중 . . .` | `시계 로딩 중...` |
| 첫 Table 삽입 | `tbody.append(tr)` | `tbody.prepend(tr)` |
| Table 변수 선언 | `const` | `let` |
| Board 구성 | 구조 삽입 후 text 설정 | row 완성 후 board 삽입 |
| Board Console | 적음 | 각 tr·td 다수 출력 |
| Board2 설명 | 상세 | 간결 |
| Border color | red | salmon |
| Height +5 | split 후 Number | parseInt |
| Quiz q1 HTML | 존재 | 없음 |
| Quiz q2 HTML 위치 | script 앞 | script 뒤 |
| 문제 1~4 구현 | 모두 구현 | 요구만 제시 |
| 문제 3 예시 | 실제 q2 text 출력 | `퀴즈2-1`로 불일치 |
| 공백 처리 | innerText 비교, trim 대안 주석 | 문제만 제시 |

---

# 57. 대표 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>DOM 콘텐츠 생성</title>
</head>
<body>
  <div id="message">
    원래 내용
  </div>

  <table>
    <tbody id="board"></tbody>
  </table>

  <script>
    "use strict";

    const message =
      document.querySelector(
        "#message"
      );

    message.textContent =
      "안전한 text";

    const rows = [
      ["제목1", "작성자1"],
      ["제목2", "작성자2"]
    ];

    const board =
      document.querySelector(
        "#board"
      );

    const fragment =
      document
        .createDocumentFragment();

    rows.forEach(
      function(row) {
        const tr =
          document.createElement(
            "tr"
          );

        const title =
          document.createElement(
            "td"
          );

        const author =
          document.createElement(
            "td"
          );

        title.textContent =
          row[0];

        author.textContent =
          row[1];

        tr.append(
          title,
          author
        );

        fragment.append(tr);
      }
    );

    board.append(fragment);
  </script>
</body>
</html>
```

---

# 58. 실무 활용: 안전한 게시판 렌더링

```js
function renderBoard(
  board,
  rows
) {
  board.replaceChildren()

  const fragment =
    document
      .createDocumentFragment()

  rows.forEach(
    function({
      title,
      author
    }) {
      const row =
        document.createElement(
          "tr"
        )

      const titleCell =
        document.createElement(
          "td"
        )

      const authorCell =
        document.createElement(
          "td"
        )

      titleCell.textContent =
        title

      authorCell.textContent =
        author

      row.append(
        titleCell,
        authorCell
      )

      fragment.append(row)
    }
  )

  board.append(fragment)
}
```

사용자 데이터를 `innerHTML`로 결합하지 않고 textContent로 넣습니다.

---

# 59. 실무 활용: 시계

```js
const clock =
  document.querySelector(
    "#clock"
  )

function updateClock() {
  const now =
    new Date()

  const time =
    new Intl.DateTimeFormat(
      "ko-KR",
      {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
      }
    ).format(now)

  clock.textContent =
    time
}

updateClock()

const clockId =
  setInterval(
    updateClock,
    1000
  )
```

필요하지 않을 때:

```js
clearInterval(
  clockId
)
```

로 정리할 수 있습니다.

---

# 60. 자주 하는 실수

## 60.1 TextContent에 HTML을 넣고 Tag가 생성될 것으로 기대

textContent는 tag를 text로 처리합니다.

## 60.2 사용자 입력을 InnerHTML에 바로 넣기

XSS가 발생할 수 있습니다.

## 60.3 CreateElement만 하고 화면에 나타날 것으로 기대

append 등의 삽입 작업이 필요합니다.

## 60.4 같은 Element를 여러 곳에 Append하면 복제된다고 생각

같은 node는 마지막 위치로 이동합니다.

## 60.5 AppendChild에 문자열 전달

Node가 아니므로 TypeError가 발생합니다.

## 60.6 Before와 Prepend 혼동

before는 형제, prepend는 첫 번째 자식입니다.

## 60.7 InnerHTML을 반복해서 재할당

기존 child node와 event listener가 교체될 수 있습니다.

## 60.8 Element.style로 Stylesheet 값까지 읽을 수 있다고 생각

inline style만 직접 나타냅니다. 계산값은 getComputedStyle을 사용합니다.

## 60.9 NodeList에서 직접 ClassList 접근

각 Element에 접근해야 합니다.

## 60.10 공백만 있는 Text를 빈 문자열과 단순 비교

`textContent.trim() === ""`처럼 공백을 제거한 뒤 검사합니다.

---

# 61. 면접·복습 포인트

## Q1. TextContent와 InnerHTML의 가장 큰 차이는 무엇인가요?

textContent는 문자열을 text로 처리하고 innerHTML은 HTML markup으로 파싱합니다.

## Q2. InnerText와 TextContent가 다른 이유는 무엇인가요?

innerText는 화면 렌더링과 CSS 상태를 고려하지만 textContent는 text node 자체를 중심으로 읽기 때문입니다.

## Q3. Append와 AppendChild의 차이는 무엇인가요?

append는 문자열과 여러 Node를 받을 수 있고 appendChild는 Node 하나만 받으며 추가한 Node를 반환합니다.

## Q4. 같은 DOM 객체를 두 번 Append하면 어떻게 되나요?

복제되지 않고 기존 위치에서 새 위치로 이동합니다.

## Q5. InnerHTML 반복 재할당의 문제는 무엇인가요?

내부 HTML 전체를 반복 파싱하고 기존 node와 event listener를 교체할 수 있습니다.

## Q6. Element.style과 GetComputedStyle의 차이는 무엇인가요?

element.style은 inline style 중심이고 getComputedStyle은 최종 계산된 style을 읽습니다.

## Q7. 원본 문제 2에서 NodeList에 바로 Contains를 사용할 수 있나요?

아닙니다. NodeList의 각 Element에 접근한 뒤 classList.contains를 사용해야 합니다.

## Q8. 원본 문제 3에서 q2-1이 q2로 판정되나요?

아닙니다. classList.contains는 정확한 class token을 비교합니다.

## Q9. 강사님 문서에서 문제 2~4 코드가 즉시 동작하지 않는 이유는 무엇인가요?

대상 quiz 요소가 script 뒤에 있어 script 실행 시 아직 파싱되지 않았기 때문입니다.

## Q10. 공백만 있는 요소를 어떻게 검사하나요?

`element.textContent.trim() === ""`처럼 공백을 제거한 뒤 검사합니다.

---

# Problems

## 문제 1. 콘텐츠 읽기

`#message`의 `textContent`, `innerText`, `innerHTML`을 각각 출력하세요.

## 문제 2. 안전한 Text 변경

문자열 `"<strong>안녕</strong>"`을 HTML tag로 실행하지 않고 화면에 그대로 출력하세요.

## 문제 3. HTML 변경

신뢰할 수 있는 고정 문자열로 `#message` 안에 `<strong>안녕</strong>`을 생성하세요.

## 문제 4. 카운터

`#count`의 숫자를 1초마다 1씩 증가시키세요.

## 문제 5. 시계

현재 시·분·초를 1초마다 `#clock`에 출력하세요.

## 문제 6. Element 생성

`<p>새 문단</p>`을 JavaScript로 생성하세요.

## 문제 7. Append

문제 6의 p를 `#container` 마지막 자식으로 넣으세요.

## 문제 8. Append 문자열

`append("<b>text</b>")`가 HTML tag를 생성하는지 설명하세요.

## 문제 9. AppendChild 오류

appendChild에 문자열을 전달하면 왜 오류가 발생하는지 설명하세요.

## 문제 10. Prepend

새 p를 `#container` 첫 번째 자식으로 넣으세요.

## 문제 11. Before와 After

`#container`의 이전과 다음 형제로 각각 hr 요소를 넣으세요.

## 문제 12. 같은 Node 이동

같은 Element를 두 container에 순서대로 append했을 때 최종 위치를 설명하세요.

## 문제 13. Table 한 행 생성

tbody 안에 제목과 작성자 cell을 가진 한 행을 생성하세요.

## 문제 14. 배열 Table

2차원 배열 전체를 DOM API로 표에 출력하세요.

## 문제 15. 역순 출력

배열의 행을 마지막 데이터부터 첫 데이터 순서로 렌더링하세요.

## 문제 16. Style 변경

`#clock`의 글자색과 글자 크기를 JavaScript로 변경하세요.

## 문제 17. Computed Style

`#clock`에 실제 적용된 width를 읽으세요.

## 문제 18. 높이 증가

현재 inline height가 `"50px"`일 때 5px 증가시키세요.

## 문제 19. Q2 개수

`.quiz` 요소 중 exact class `"q2"`를 가진 요소 개수를 구하세요.

## 문제 20. 빈 Quiz

공백만 있는 `.quiz`의 text를 `"비어있음"`으로 변경하세요.

## 문제 21. 강사님 원본 오류

강사님 문서에서 quiz 요소를 script 뒤에 두었을 때 발생하는 문제를 설명하세요.

## 문제 22. 종합 동적 목록

다음 요구사항을 만족하세요.

- 문자열 배열을 인수로 받는 `renderList()` 함수
- 기존 목록을 비움
- `DocumentFragment` 사용
- 각 값을 li의 textContent로 설정
- 빈 문자열 또는 공백만 있는 값은 `"비어있음"`으로 표시
- 빈 항목에는 `"empty"` class 추가
- innerHTML로 사용자 값을 조합하지 않음
- 완성 후 ul에 한 번 삽입

---

# Answers & Explanations

## 정답 1

```js
const message =
  document.querySelector(
    "#message"
  )

console.log(
  message.textContent
)

console.log(
  message.innerText
)

console.log(
  message.innerHTML
)
```

## 정답 2

```js
message.textContent =
  "<strong>안녕</strong>"
```

tag가 아니라 text로 표시됩니다.

## 정답 3

```js
message.innerHTML =
  "<strong>안녕</strong>"
```

고정되고 신뢰할 수 있는 문자열이라는 전제입니다.

## 정답 4

```js
setInterval(
  function() {
    const count =
      document.querySelector(
        "#count"
      )

    const current =
      Number(
        count.textContent
      )

    count.textContent =
      String(current + 1)
  },
  1000
)
```

## 정답 5

```js
function updateClock() {
  const now =
    new Date()

  const clock =
    document.querySelector(
      "#clock"
    )

  clock.textContent =
    `${now.getHours()}시 ` +
    `${now.getMinutes()}분 ` +
    `${now.getSeconds()}초`
}

updateClock()

setInterval(
  updateClock,
  1000
)
```

## 정답 6

```js
const paragraph =
  document.createElement(
    "p"
  )

paragraph.textContent =
  "새 문단"
```

## 정답 7

```js
const container =
  document.querySelector(
    "#container"
  )

container.append(
  paragraph
)
```

## 정답 8

HTML tag를 생성하지 않습니다. 문자열 text node로 추가되어 `<b>text</b>`가 글자 그대로 표시됩니다.

## 정답 9

appendChild는 Node 객체만 인수로 받습니다. 문자열은 Node가 아니므로 TypeError가 발생합니다.

## 정답 10

```js
container.prepend(
  paragraph
)
```

같은 paragraph가 이미 다른 위치에 있다면 새 위치로 이동합니다.

## 정답 11

```js
const beforeHr =
  document.createElement(
    "hr"
  )

const afterHr =
  document.createElement(
    "hr"
  )

container.before(
  beforeHr
)

container.after(
  afterHr
)
```

## 정답 12

Element는 복제되지 않습니다. 두 번째 container로 이동하여 최종적으로 두 번째 container의 자식이 됩니다.

## 정답 13

```js
const tbody =
  document.querySelector(
    "tbody"
  )

const row =
  document.createElement(
    "tr"
  )

const titleCell =
  document.createElement(
    "td"
  )

const authorCell =
  document.createElement(
    "td"
  )

titleCell.textContent =
  "제목1"

authorCell.textContent =
  "작성자1"

row.append(
  titleCell,
  authorCell
)

tbody.append(row)
```

## 정답 14

```js
const rows = [
  ["제목1", "작성자1"],
  ["제목2", "작성자2"]
]

const fragment =
  document
    .createDocumentFragment()

rows.forEach(
  function(rowData) {
    const row =
      document.createElement(
        "tr"
      )

    rowData.forEach(
      function(value) {
        const cell =
          document.createElement(
            "td"
          )

        cell.textContent =
          value

        row.append(cell)
      }
    )

    fragment.append(row)
  }
)

tbody.append(fragment)
```

## 정답 15

```js
for (
  let i = rows.length - 1;
  i >= 0;
  i--
) {
  console.log(rows[i])
}
```

렌더링 코드를 이 반복문 안에 작성하면 역순 표를 만들 수 있습니다.

## 정답 16

```js
const clock =
  document.querySelector(
    "#clock"
  )

clock.style.color =
  "red"

clock.style.fontSize =
  "1.5em"
```

## 정답 17

```js
const width =
  getComputedStyle(
    clock
  ).getPropertyValue(
    "width"
  )

console.log(width)
```

## 정답 18

```js
clock.style.height =
  "50px"

const height =
  parseFloat(
    clock.style.height
  )

clock.style.height =
  `${height + 5}px`
```

## 정답 19

```js
const q2Elements =
  document.querySelectorAll(
    ".quiz.q2"
  )

console.log(
  q2Elements.length
)
```

## 정답 20

```js
const quizzes =
  document.querySelectorAll(
    ".quiz"
  )

quizzes.forEach(
  function(quiz) {
    if (
      quiz
        .textContent
        .trim() === ""
    ) {
      quiz.textContent =
        "비어있음"

      quiz.classList.add(
        "empty"
      )
    }
  }
)
```

## 정답 21

script가 실행될 때 뒤쪽 quiz HTML은 아직 파싱되지 않았습니다. 따라서 querySelectorAll 결과는 빈 NodeList이며 q1은 실제 HTML 자체가 없어 null입니다. HTML을 script 앞으로 옮기거나 DOMContentLoaded 이후 실행해야 합니다.

## 정답 22

```js
function renderList(
  list,
  values
) {
  list.replaceChildren()

  const fragment =
    document
      .createDocumentFragment()

  values.forEach(
    function(value) {
      const item =
        document.createElement(
          "li"
        )

      const normalized =
        String(value).trim()

      if (normalized === "") {
        item.textContent =
          "비어있음"

        item.classList.add(
          "empty"
        )
      } else {
        item.textContent =
          value
      }

      fragment.append(item)
    }
  )

  list.append(fragment)
}
```

---

# Final Checklist

## 콘텐츠 읽기와 변경

- [ ] textContent가 text node를 읽는다는 점을 이해했다.
- [ ] innerText가 렌더링된 text를 고려함을 이해했다.
- [ ] innerHTML이 HTML markup 문자열을 다룸을 이해했다.
- [ ] textContent와 innerText에 tag 문자열을 넣으면 text로 표시됨을 확인했다.
- [ ] innerHTML은 tag를 실제 Element로 파싱함을 확인했다.
- [ ] 신뢰할 수 없는 문자열을 innerHTML에 넣지 않았다.
- [ ] `javascript:` URL의 보안 위험을 이해했다.

## 실시간 UI

- [ ] count 값을 문자열에서 숫자로 변환했다.
- [ ] setInterval의 첫 실행이 지연 후임을 이해했다.
- [ ] interval 주기가 정확한 실행 시각을 보장하지 않음을 이해했다.
- [ ] Date를 callback 안에서 새로 생성했다.
- [ ] 필요할 때 interval ID를 정리할 수 있다.

## DOM 생성과 삽입

- [ ] createElement만으로 화면에 표시되지 않음을 이해했다.
- [ ] 문서 미연결 Element와 Virtual DOM을 구분했다.
- [ ] append가 문자열과 Node를 받을 수 있음을 확인했다.
- [ ] append 문자열은 HTML로 파싱되지 않음을 확인했다.
- [ ] appendChild는 Node만 받음을 확인했다.
- [ ] 같은 Element를 다시 삽입하면 이동함을 이해했다.
- [ ] prepend는 첫 자식, before·after는 형제임을 구분했다.

## Table 생성

- [ ] 2차원 배열의 제목과 작성자 위치를 확인했다.
- [ ] tr과 td의 부모·자식 관계를 올바르게 구성했다.
- [ ] 사용자 값을 textContent로 넣었다.
- [ ] innerHTML 반복 재할당 문제를 이해했다.
- [ ] 역순 누적 원리를 이해했다.
- [ ] 많은 node는 DocumentFragment로 묶을 수 있음을 이해했다.

## Style 조작

- [ ] CSS kebab-case를 JavaScript camelCase로 바꿨다.
- [ ] element.style이 inline style 중심임을 이해했다.
- [ ] getComputedStyle로 계산된 값을 읽었다.
- [ ] CSS 길이 문자열에서 숫자와 단위를 구분했다.
- [ ] 랜덤 정수에는 Math.floor 사용을 검토했다.
- [ ] 동적 style은 head에 삽입하는 방법을 이해했다.

## 문제 풀이

- [ ] NodeList 자체에 classList를 사용하지 않았다.
- [ ] 각 Element에서 contains를 호출했다.
- [ ] q2와 q2-1을 exact class token으로 구분했다.
- [ ] 공백만 있는 text는 trim 후 검사했다.
- [ ] Boolean에 느슨한 비교를 사용하지 않았다.
- [ ] 빈 요소에 text와 class를 함께 적용했다.

## 원본 코드 검수

- [ ] 두 실제 12_dom_content.html만 비교했다.
- [ ] 내 시계와 강사님 시계의 출력 범위를 기록했다.
- [ ] 250ms와 3000ms 주기 차이를 기록했다.
- [ ] append와 prepend 차이를 기록했다.
- [ ] const와 let 차이를 기록했다.
- [ ] board 구성 순서 차이를 기록했다.
- [ ] border red와 salmon 차이를 기록했다.
- [ ] 높이 계산 방식 차이를 기록했다.
- [ ] 강사님 quiz q1 요소 부재를 기록했다.
- [ ] 강사님 quiz q2 요소가 script 뒤에 있음을 기록했다.
- [ ] 강사님 문제 3 예시 불일치를 기록했다.
- [ ] 내 문제 1~4 구현을 기록했다.
- [ ] 내 공백 비교 개선점을 기록했다.
- [ ] innerHTML과 javascript URL 위험을 기록했다.

---

# Key Summary

- JavaScript 12번은 DOM 내부 콘텐츠 읽기·변경, Element 생성·삽입, 동적 표, style 조작을 다룬다.
- `textContent`는 text node 중심, `innerText`는 렌더링 text 중심, `innerHTML`은 HTML markup 중심이다.
- textContent와 innerText에 `<h1>` 문자열을 넣으면 tag가 아니라 글자로 표시된다.
- innerHTML은 문자열을 HTML로 파싱하므로 tag가 실제 Element가 된다.
- 사용자 입력을 innerHTML에 직접 넣으면 XSS가 발생할 수 있다.
- 원본의 `javascript:alert(...)` 링크는 실행 가능한 보안 위험 예제다.
- count의 textContent는 문자열이므로 Number 변환 후 증가한다.
- interval은 delay가 지난 뒤 처음 실행되며 정확한 주기를 보장하지 않는다.
- 내 시계는 시·분·초·ms를 250ms마다 갱신하고 강사님은 분·초·ms를 3000ms마다 갱신한다.
- 주기를 짧게 설정해도 event loop 지연 자체가 해결되는 것은 아니다.
- `createElement()`는 문서에 아직 연결되지 않은 실제 DOM Element를 만든다.
- 이를 Virtual DOM이라고 부르는 것은 다른 개념과 혼동될 수 있다.
- `append()`는 Node와 문자열을 받을 수 있지만 문자열을 HTML로 파싱하지 않는다.
- `appendChild()`는 Node 하나만 받을 수 있다.
- 같은 Element를 다시 append하면 복제되지 않고 마지막 위치로 이동한다.
- `prepend()`는 첫 자식, `before()`와 `after()`는 형제 위치에 삽입한다.
- 내 첫 table row는 tbody에 append하고 강사님은 prepend한다.
- 내 코드는 const를, 강사님은 let을 주로 사용한다.
- 2차원 rows 배열의 `[i][0]`은 제목, `[i][1]`은 작성자다.
- DOM API로 cell text를 넣으면 HTML 문자열 실행 위험을 줄일 수 있다.
- board2는 새 HTML을 앞에 붙여 제목5부터 제목1까지 역순으로 표시한다.
- 반복적인 innerHTML 재할당은 전체 내부 DOM을 계속 재파싱한다.
- “앞 반복 결과가 남는다”는 장점만으로 더 안전하다고 일반화할 수 없다.
- `element.style`은 inline style 중심이고 `getComputedStyle()`은 최종 계산값을 읽는다.
- CSS의 `font-size`는 JavaScript에서 `fontSize`로 작성한다.
- 현재 랜덤 높이는 0~99px이며 Math.floor가 parseInt보다 의도가 명확하다.
- 내 문제 2는 NodeList의 각 Element에서 classList.contains를 사용해 q2 두 개를 찾는다.
- `q2-1`은 exact class token `q2`가 아니다.
- 강사님 문제 3의 `"퀴즈2-1"` 예시는 q2 요구와 일치하지 않는다.
- 공백만 있는 요소는 `textContent.trim() === ""`으로 검사하는 것이 명확하다.
- 강사님 원본에는 q1 HTML이 없고 q2 요소들은 script 뒤에 있다.
- 따라서 강사님 문제 1~4를 script 위치 그대로 구현하면 선택 시점 문제가 발생한다.
- 내 원본은 quiz 요소들이 script 앞에 있어 문제 1~4 구현이 실행된다.
