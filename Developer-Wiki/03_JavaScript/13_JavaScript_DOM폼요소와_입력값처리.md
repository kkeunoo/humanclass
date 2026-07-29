# JavaScript DOM 폼 요소와 입력값 처리

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `13_JavaScript_DOM폼요소와_입력값처리.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `12_JavaScript_DOM콘텐츠생성과_스타일조작.md` |
| 다음 학습 | `14_JavaScript_DOM이벤트.md` |
| 원본 기준 | `workspace/workspace_html/javascript/13_dom_form.html`, `workspace_teacher/workspace_html/javascript/13_dom_form.html` |
| 핵심 범위 | `input.value`, password, date input, 날짜 형식, radio, checkbox, `:checked`, `:not(:checked)`, `checked`, select value, option 선택, textarea value, 줄바꿈 치환, DOM 출력 |
| 프로젝트 연결 | 회원가입 폼, 설문조사, 날짜 입력, 관심사 선택, select 제어, textarea 미리보기, 입력 검증 |

> 이 문서는 내 코드와 강사님 코드의 `13_dom_form.html`을 직접 비교해 작성했습니다. 두 파일은 text, password, date, radio, checkbox, select, textarea의 값을 읽고 변경하는 흐름을 다룹니다. 내 코드는 설명과 구분선을 추가했지만 checkbox 판정에서 `checks2.checked`를 사용한 실제 오류가 있습니다. 강사님 코드는 같은 부분을 `checks2[i].checked`로 올바르게 작성했습니다. 또한 두 코드 모두 textarea 값을 `innerHTML`로 출력하므로 사용자 입력을 그대로 넣을 경우 XSS 위험이 있습니다. 원본은 그대로 보존하고 정확한 동작과 개선점을 분리해 설명합니다.

---

# 학습 목표

- 폼 요소의 현재 입력값을 `.value`로 읽는다.
- HTML의 초기 `value`와 사용자가 입력한 최신 값을 구분한다.
- JavaScript로 text, password, date 값을 변경한다.
- date input이 `YYYY-MM-DD` 형식을 요구한다는 점을 이해한다.
- 현재 날짜를 date input 형식으로 만든다.
- `getMonth()`가 0부터 시작한다는 점을 이해한다.
- radio에서 `:checked`를 사용해 선택된 항목 하나를 찾는다.
- 여러 radio의 checked 상태를 JavaScript로 변경한다.
- checkbox는 복수 선택이 가능하므로 여러 요소를 순회한다.
- `:checked`와 `:not(:checked)` selector를 구분한다.
- NodeList 자체와 각 Element의 `checked` 속성을 구분한다.
- select의 현재 선택값을 읽고 변경한다.
- option의 `selected`와 input의 `checked` 차이를 이해한다.
- textarea의 줄바꿈 문자를 확인한다.
- 줄바꿈을 `<br>`로 바꾸는 방식과 안전한 출력 방식을 구분한다.
- 내 코드와 강사님 코드의 실제 차이와 오류를 정확히 기록한다.

---

# 1. 폼 요소와 Value

폼 요소의 현재 값은 일반적으로 `.value`로 읽습니다.

```js
const text =
  document.querySelector(
    "#id"
  )

console.log(
  text.value
)
```

HTML:

```html
<input
  type="text"
  id="id"
  value="abcd"
>
```

초기 value는 `"abcd"`입니다.

---

# 2. 초기 Value와 현재 Value

HTML attribute:

```html
value="abcd"
```

JavaScript property:

```js
text.value
```

사용자가 입력값을 바꾸면 `.value`는 현재 최신 입력값을 나타냅니다.

원본 내 주석:

```text
input type에 value값이 있지만,
가져오는 것은 입력된 최신 데이터
```

핵심적으로 올바른 설명입니다.

---

# 3. 내 코드의 Text 순서

내 코드:

```js
const text =
  document.querySelector(
    "#id"
  )

text.value =
  "12345"

console.log(
  "text",
  text.value
)
```

먼저 값을 `"12345"`로 바꾼 후 출력합니다.

따라서 Console 결과:

```text
text 12345
```

---

# 4. 강사님 코드의 Text 순서

강사님 코드:

```js
const text =
  document.querySelector(
    "#id"
  )

console.log(
  "text",
  text.value
)

text.value =
  "12345"
```

먼저 초기값 `"abcd"`를 출력한 후 `"12345"`로 변경합니다.

따라서 두 코드의 Console 결과가 다릅니다.

```text
내 코드
→ 12345 출력

강사님 코드
→ abcd 출력 후 값 변경
```

---

# 5. Password Value

공통 원본:

```js
const password =
  document.querySelector(
    "#pw"
  )

console.log(
  "password",
  password.value
)
```

초기 입력값이 없으므로 빈 문자열을 출력합니다.

```text
""
```

---

# 6. Password 변경 차이

강사님 코드에만 있습니다.

```js
password.value =
  "abcd"
```

내 코드는 password를 읽기만 하고 변경하지 않습니다.

브라우저 화면에는 password input 특성상 문자가 점이나 별표처럼 가려져 보입니다.

하지만 JavaScript의 `.value`에는 실제 문자열이 들어 있습니다.

실제 서비스에서는 password 값을 Console에 출력하지 않는 것이 안전합니다.

---

# 7. Date Input Value

공통 원본:

```js
const date =
  document.querySelector(
    "#date"
  )

console.log(
  "date",
  "[" + date.value + "]"
)
```

초기 날짜가 선택되지 않았으므로:

```text
[]
```

처럼 보입니다.

실제 `date.value`는 빈 문자열입니다.

---

# 8. Date 형식

내 코드 주석:

```js
// date.value = '2026-7-16'
// yyyy-mm-dd 양식을 지켜야 함
```

date input에 문자열을 직접 넣을 때 일반적으로 다음 형식을 사용합니다.

```text
YYYY-MM-DD
```

올바른 예:

```js
date.value =
  "2026-07-16"
```

강사님 코드:

```js
date.value =
  "2026-07-15"
```

날짜 값만 다릅니다.

---

# 9. 현재 날짜 만들기

공통 흐름:

```js
const today =
  new Date()

const y =
  today.getFullYear()

let m =
  today.getMonth() + 1

let d =
  today.getDate()
```

`getMonth()`는 0부터 11까지 반환하므로 실제 월을 표시하려면 1을 더합니다.

```text
0 → 1월
6 → 7월
11 → 12월
```

---

# 10. 월 두 자리 만들기

공통 원본:

```js
if (m < 10) {
  m =
    "0" + m
}
```

7월이면:

```text
7
→ "07"
```

내 코드에는 대안이 주석으로 있습니다.

```js
m =
  ("0" + m)
    .slice(-2)
```

---

# 11. 일 두 자리 만들기

공통 원본:

```js
let d =
  today.getDate()

d =
  ("0" + d)
    .slice(-2)
```

예:

```text
3
→ "03"

15
→ "15"
```

문자열 앞에 0을 붙인 후 마지막 두 글자만 가져옵니다.

---

# 12. 날짜 문자열 결합

공통 원본:

```js
const result =
  `${y}-${m}-${d}`

date.value =
  result
```

결과 예:

```text
2026-07-29
```

date input에 현재 날짜가 표시됩니다.

---

# 13. ToISOString 대안

공통 원본:

```js
console.log(
  today
    .toISOString()
    .split("T")[0]
)
```

ISO 문자열의 날짜 부분만 추출합니다.

주의:

`toISOString()`은 UTC 기준입니다.

사용자의 로컬 시간대가 UTC와 다르면 자정 부근에 로컬 날짜와 ISO 날짜가 달라질 수 있습니다.

따라서 로컬 date input 값에는 직접 연·월·일을 조합하는 방식이 더 안전할 수 있습니다.

---

# 14. SetTimeout 실행

양쪽 원본은 모든 폼 처리를 다음 안에서 실행합니다.

```js
setTimeout(
  function() {
    // form 처리
  },
  1000 * 3
)
```

약 3초 후 실행됩니다.

그 사이 사용자가 text, password, date, checkbox 등을 조작하면 callback 실행 시점의 최신 값이 읽힐 수 있습니다.

단, 코드에서 이후 값을 다시 덮어쓰는 부분도 있습니다.

---

# 15. Radio 기본 선택

HTML:

```html
<input
  type="radio"
  name="ai"
  value="1"
  checked
>
chatGPT
```

같은 `name="ai"`를 가진 radio들은 한 그룹입니다.

한 항목만 선택할 수 있습니다.

초기 선택값은 `"1"`입니다.

---

# 16. 선택된 Radio 가져오기

공통 원본:

```js
const radio =
  document.querySelector(
    "[name=ai]:checked"
  )

console.log(
  radio.value
)
```

selector 의미:

```text
[name=ai]
→ name 속성이 ai

:checked
→ 현재 선택된 요소
```

결과:

```text
1
```

사용자가 3초 안에 다른 radio를 선택하면 그 시점의 선택값이 출력될 수 있습니다.

---

# 17. Radio Null 가능성

radio group에 아무 항목도 선택되지 않았다면:

```js
document.querySelector(
  "[name=ai]:checked"
)
```

결과는 null입니다.

이후:

```js
radio.value
```

를 실행하면 TypeError가 발생합니다.

안전한 처리:

```js
if (radio !== null) {
  console.log(radio.value)
}
```

현재 원본은 chatGPT가 기본 checked이므로 null이 아닙니다.

---

# 18. Radio Checked 변경

공통 원본:

```js
const radios =
  document.querySelectorAll(
    "[name=ai]"
  )

radios[1].checked =
  true
```

두 번째 radio인 gemini가 선택됩니다.

같은 name group에서 다른 radio의 checked 상태는 자동으로 해제됩니다.

---

# 19. Checkbox와 Radio 차이

radio:

```text
같은 name 그룹에서 하나만 선택
```

checkbox:

```text
여러 개 동시 선택 가능
```

따라서 checkbox 선택값을 읽을 때는 여러 요소를 선택하고 반복하는 경우가 많습니다.

---

# 20. 선택되지 않은 Checkbox

공통 원본:

```js
const checks =
  document.querySelectorAll(
    ".game:not(:checked)"
  )
```

뜻:

```text
class가 game이면서
현재 checked가 아닌 checkbox
```

초기에는 모든 game checkbox가 선택되지 않았으므로 6개가 모두 포함됩니다.

---

# 21. 선택된 Checkbox Selector

원본 주석:

```js
// const checks =
//   document.querySelectorAll(
//     ".game:checked"
//   )
```

선택된 항목만 가져오려면:

```js
.game:checked
```

를 사용합니다.

선택되지 않은 항목:

```js
.game:not(:checked)
```

---

# 22. Checkbox Value 출력

공통 원본:

```js
for (
  let i = 0;
  i < checks.length;
  i++
) {
  console.log(
    checks[i].value
  )
}
```

초기 상태에서 출력:

```text
a
b
c
d
e
f
```

각 checkbox의 value입니다.

---

# 23. Checkbox 전체 상태 출력

공통 흐름:

```js
const checks2 =
  document.querySelectorAll(
    ".game"
  )

for (
  let i = 0;
  i < checks2.length;
  i++
) {
  console.log(
    checks2[i].value,
    checks2[i].checked
  )
}
```

각 checkbox의 value와 Boolean checked 상태를 출력합니다.

초기에는 모두 false입니다.

---

# 24. 내 코드의 Checkbox 오류

내 코드:

```js
if (
  checks2.checked == true
) {
  console.log(
    checks2[i].value
  )
}
```

`checks2`는 NodeList입니다.

NodeList 자체에는 checkbox의 `checked` 속성이 없습니다.

```js
checks2.checked
// undefined
```

따라서 조건:

```js
undefined == true
```

는 false이고 내부 Console은 실행되지 않습니다.

---

# 25. 강사님 코드의 올바른 Checkbox 판정

강사님 코드:

```js
if (
  checks2[i].checked == true
) {
  console.log(
    checks2[i].value
  )
}
```

각 checkbox Element에 접근한 뒤 checked를 확인합니다.

올바른 구조입니다.

더 간단히:

```js
if (
  checks2[i].checked
) {
}
```

처럼 작성할 수 있습니다.

---

# 26. Checks2[0] Checked 변경

공통 원본:

```js
checks2[0].checked =
  true
```

첫 번째 checkbox인 `"마비노기 모바일"`을 선택 상태로 만듭니다.

주의:

이 코드는 전체 상태를 출력한 반복문 뒤에 있습니다.

따라서 그 앞 Console에는 첫 checkbox가 false로 출력되고, 이후 화면에서만 checked가 true가 됩니다.

---

# 27. 게임 이름 차이

내 코드:

```text
스타듀밸리
워크래프트3
```

강사님 코드:

```text
스타듀벨리
워크레프트3
```

문자열 표기 차이이며 checkbox 동작에는 영향이 없습니다.

원본 차이를 임의로 수정하지 않습니다.

---

# 28. Select 기본값

HTML:

```html
<select id="lang">
  <option value="1">
    javascript
  </option>

  <option
    value="2"
    selected
  >
    python
  </option>

  <option value="3">
    db
  </option>

  <option value="4">
    java
  </option>
</select>
```

초기 선택값:

```text
2
```

---

# 29. Select Value 읽기

공통 원본:

```js
const lang =
  document.getElementById(
    "lang"
  )

console.log(
  lang.value
)
```

현재 선택된 option의 value를 반환합니다.

초기값은 `"2"`입니다.

---

# 30. Select Value 변경

공통 원본:

```js
lang.value =
  "4"
```

value가 `"4"`인 option이 선택됩니다.

화면에서는 `java`가 선택됩니다.

---

# 31. Select와 Checked 설명 보완

내 코드 주석:

```text
select도 checked = true로 하되,
option에 주어야 함
```

정확히는 option에는 `checked`가 아니라 `selected`를 사용합니다.

```js
option.selected =
  true
```

또는 select 자체의 value를 설정합니다.

```js
lang.value =
  "4"
```

따라서 원본 주석의 `checked = true`는 잘못된 표현입니다.

---

# 32. SelectedIndex 확장

현재 선택된 option index:

```js
lang.selectedIndex
```

선택된 option 객체:

```js
lang.options[
  lang.selectedIndex
]
```

화면 text:

```js
lang.options[
  lang.selectedIndex
].text
```

원본에는 value 변경만 있습니다.

---

# 33. Textarea Value

공통 원본:

```js
const textarea =
  document.querySelector(
    "#textarea"
  )

console.log(
  textarea.value
)
```

HTML:

```html
<textarea id="textarea">
초기값
</textarea>
```

textarea의 현재 입력값은 `.value`로 읽습니다.

---

# 34. Textarea와 InnerText

내 코드 마지막 주석에는 `innerText`를 확인하려는 시도가 있습니다.

```js
// const input_text =
//   document.querySelector(
//     "#textarea"
//   )

// console.log(
//   input_text.innerText
// )
```

textarea의 사용자 입력 최신값은 `.value`를 사용해야 합니다.

`textContent`나 `innerText`는 초기 markup text와 관련된 결과를 줄 수 있지만 현재 편집값을 읽는 표준 방식은 `.value`입니다.

---

# 35. 줄바꿈 위치 확인

공통 원본:

```js
console.log(
  textarea.value
    .indexOf("\n")
)
```

줄바꿈이 있으면 첫 줄바꿈 index를 반환합니다.

없으면:

```text
-1
```

초기값 `"초기값"`에는 줄바꿈이 없으므로 -1입니다.

사용자가 3초 안에 여러 줄을 입력하면 다른 값이 나올 수 있습니다.

---

# 36. Textarea 내용 View 출력

공통 원본:

```js
const view =
  document.querySelector(
    "#view"
  )

view.innerHTML =
  textarea.value
```

textarea 입력을 HTML로 파싱하여 출력합니다.

사용자가 HTML tag를 입력하면 실제 tag로 만들어질 수 있습니다.

예:

```html
<h1>제목</h1>
```

---

# 37. 줄바꿈을 Br로 치환

공통 원본:

```js
let str =
  textarea.value
    .replace(
      /\n/g,
      "<br>"
    )

view.innerHTML =
  str
```

모든 줄바꿈 문자를 `<br>` 문자열로 바꾼 뒤 HTML로 렌더링합니다.

`g` 플래그 때문에 모든 줄바꿈이 바뀝니다.

---

# 38. Textarea InnerHTML XSS 위험

사용자가 다음을 입력할 수 있습니다.

```html
<img
  src="x"
  onerror="alert(1)"
>
```

이를 `innerHTML`에 넣으면 event handler가 실행될 수 있습니다.

따라서 사용자 입력을 직접 innerHTML에 넣는 것은 위험합니다.

---

# 39. 안전한 줄바꿈 표시

방법 1: textContent와 CSS 사용

```css
#view {
  white-space: pre-wrap;
}
```

```js
view.textContent =
  textarea.value
```

방법 2: 줄 단위로 text node와 br 생성

```js
const lines =
  textarea.value
    .split("\n")

view.replaceChildren()

lines.forEach(
  function(line, index) {
    if (index > 0) {
      view.append(
        document.createElement(
          "br"
        )
      )
    }

    view.append(
      document.createTextNode(
        line
      )
    )
  }
)
```

사용자 문자열을 HTML로 파싱하지 않습니다.

---

# 40. Hr 추가 차이

내 HTML에는 각 폼 그룹 사이에 `<hr>`가 추가되어 있습니다.

강사님 코드는 대부분 `<br>`만 사용합니다.

내 코드:

```html
<br><hr>
```

강사님 코드:

```html
<br>
```

시각적 구분 차이이며 JavaScript 동작에는 영향이 없습니다.

---

# 41. 들여쓰기 차이

내 코드는 form과 script를 body 안에서 한 단계 들여썼습니다.

강사님 코드는 body 바로 아래에서 들여쓰기가 상대적으로 적습니다.

기능 차이는 없지만 일관된 indentation은 구조 파악에 도움을 줍니다.

---

# 42. 출력 구분선 차이

내 코드:

```js
console.log(
  "---------------------------"
)
```

강사님 코드:

```js
console.log(
  "---------------------"
)
```

내 코드는 select와 textarea 앞에도 구분선을 추가합니다.

Console 가독성을 위한 차이입니다.

---

# 43. Form Submit 기본 동작

원본 `<form>`에는 submit button이 없습니다.

따라서 현재 예제에서는 자동 제출이 일어나지 않습니다.

실무에서 submit button을 추가하면 form submit 시 페이지가 새로고침될 수 있습니다.

이벤트 처리에서는:

```js
form.addEventListener(
  "submit",
  function(event) {
    event.preventDefault()
  }
)
```

를 사용할 수 있습니다.

다음 이벤트 단원과 연결되는 확장 내용입니다.

---

# 44. Input Value와 Attribute 차이 확장

현재 값:

```js
text.value
```

HTML attribute 값:

```js
text.getAttribute(
  "value"
)
```

사용자가 입력을 변경한 뒤 두 값은 달라질 수 있습니다.

```text
text.value
→ 현재 UI 값

getAttribute("value")
→ HTML에 기록된 초기 attribute 값
```

원본은 `.value` 중심입니다.

---

# 45. Radio와 Checkbox Value 타입

HTML value는 문자열입니다.

```html
<input value="1">
```

JavaScript:

```js
radio.value
// "1"
```

숫자 계산이 필요하면 명시적으로 변환해야 합니다.

```js
Number(
  radio.value
)
```

---

# 46. FormData 확장

여러 form 값을 한 번에 다룰 때:

```js
const form =
  document.querySelector(
    "form"
  )

const data =
  new FormData(form)
```

단, checkbox가 선택되지 않으면 FormData에 포함되지 않을 수 있고, 여러 같은 name 값은 `getAll()`로 가져옵니다.

원본 checkbox에는 class만 있고 name이 없으므로 FormData에 포함하려면 name을 추가해야 합니다.

```html
<input
  type="checkbox"
  name="game"
  value="a"
>
```

---

# 47. My Code 분석

## 47.1 장점

- input의 HTML 초기값과 최신 `.value` 차이를 설명했다.
- text 값을 JavaScript로 직접 변경했다.
- date input에 필요한 형식을 주석으로 기록했다.
- `getMonth() + 1` 이유를 설명했다.
- 월과 일을 두 자리 문자열로 만드는 과정을 상세히 기록했다.
- radio에서 `:checked` selector 의미를 설명했다.
- NodeList index로 특정 radio의 checked 상태를 변경했다.
- checkbox의 복수 선택 특성을 설명했다.
- `:not(:checked)`와 `:checked` 대안을 함께 기록했다.
- select와 textarea 처리 앞에 Console 구분선을 추가했다.
- textarea 줄바꿈을 정규 표현식으로 `<br>`로 바꾸는 이유를 설명했다.
- form 그룹 사이에 `<hr>`를 추가해 화면 구분을 개선했다.

## 47.2 개선점

- text 값을 출력하기 전에 `"12345"`로 변경하여 초기값 확인이 불가능하다.
- 강사님과 달리 password 값을 JavaScript로 설정하지 않는다.
- `toISOString()` 날짜가 UTC 기준이라는 설명이 없다.
- `checks2.checked`는 NodeList 속성을 읽는 오류다.
- 올바른 코드는 `checks2[i].checked`다.
- Boolean 비교에 `== true`를 사용한다.
- `checks2[0].checked = true`가 반복문 뒤여서 이전 Console 출력에는 반영되지 않는다.
- select option에 `checked`를 사용한다고 설명했지만 실제 속성은 `selected`다.
- textarea 현재값은 `.value`를 사용해야 하며 `innerText` 실험은 혼동을 줄 수 있다.
- textarea 사용자 입력을 `innerHTML`에 직접 넣어 XSS 위험이 있다.
- 줄바꿈 치환 후에도 innerHTML을 사용하므로 보안 문제가 해결되지 않는다.
- form 요소에 label이 없어 접근성이 부족하다.
- id가 `"id"`라서 변수 의미가 모호하다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.

---

# 48. Teacher Code 분석

## 48.1 장점

- text의 초기값을 먼저 출력한 뒤 값을 변경한다.
- password의 빈 값을 확인하고 `"abcd"`로 변경한다.
- date input의 빈 값, 지정 날짜, 현재 날짜 설정 흐름을 보여 준다.
- radio 선택값과 radio 상태 변경을 구현한다.
- checkbox 미선택 selector와 전체 상태 순회를 구현한다.
- checkbox 판정에서 `checks2[i].checked`를 올바르게 사용한다.
- select value 읽기와 변경을 구현한다.
- textarea value와 줄바꿈 위치를 확인한다.
- textarea 줄바꿈을 정규 표현식으로 바꿔 출력한다.

## 48.2 개선점

- password 값을 Console에 출력하는 구조는 실무 보안상 피해야 한다.
- `toISOString()`의 UTC 날짜 차이를 설명하지 않는다.
- 느슨한 Boolean 비교를 사용한다.
- checkbox를 checked로 바꾸는 코드가 상태 출력 뒤에 있다.
- textarea 입력을 innerHTML에 넣어 XSS 위험이 있다.
- `parse`나 validation 없이 form 값을 신뢰한다.
- form 요소에 label이 없다.
- 게임 이름에 `스타듀벨리`, `워크레프트3` 표기가 있다.
- 문서 lang과 title이 학습 내용에 맞지 않는다.

---

# 49. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| Text 출력 순서 | 값 변경 후 `12345` 출력 | 초기 `abcd` 출력 후 변경 |
| Password 설정 | 없음 | `"abcd"` 설정 |
| Date 직접 설정 | `2026-07-16` | `2026-07-15` |
| 설명 주석 | 매우 상세 | 핵심 위주 |
| Form 구분 | `<hr>` 다수 | `<br>` 중심 |
| 게임 표기 | 스타듀밸리, 워크래프트3 | 스타듀벨리, 워크레프트3 |
| Checkbox 조건 | `checks2.checked` 오류 | `checks2[i].checked` 정상 |
| Select 설명 | option에 checked라고 잘못 설명 | 별도 설명 없음 |
| Console 구분선 | 여러 위치 | 일부 위치 |
| Textarea 추가 주석 | innerText 실험 주석 있음 | 없음 |
| XSS 위험 | 설명 없음 | 설명 없음 |

---

# 50. 대표 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>DOM 폼 처리</title>
</head>
<body>
  <form id="profileForm">
    <label for="userId">
      아이디
    </label>

    <input
      type="text"
      id="userId"
      name="userId"
      value="abcd"
    >

    <fieldset>
      <legend>
        AI 선택
      </legend>

      <label>
        <input
          type="radio"
          name="ai"
          value="1"
          checked
        >
        ChatGPT
      </label>

      <label>
        <input
          type="radio"
          name="ai"
          value="2"
        >
        Gemini
      </label>
    </fieldset>

    <label for="language">
      언어
    </label>

    <select
      id="language"
      name="language"
    >
      <option value="js">
        JavaScript
      </option>

      <option value="python">
        Python
      </option>
    </select>

    <label for="memo">
      메모
    </label>

    <textarea
      id="memo"
      name="memo"
    ></textarea>
  </form>

  <div id="preview"></div>

  <script>
    "use strict";

    const selectedAi =
      document.querySelector(
        '[name="ai"]:checked'
      );

    if (selectedAi !== null) {
      console.log(
        selectedAi.value
      );
    }

    const memo =
      document.querySelector(
        "#memo"
      );

    const preview =
      document.querySelector(
        "#preview"
      );

    preview.textContent =
      memo.value;
  </script>
</body>
</html>
```

---

# 51. 안전한 Checkbox 수집

```js
const checkedGames =
  document.querySelectorAll(
    ".game:checked"
  )

const values = []

checkedGames.forEach(
  function(game) {
    values.push(
      game.value
    )
  }
)

console.log(values)
```

또는:

```js
const values =
  [...document.querySelectorAll(
    ".game:checked"
  )].map(
    function(game) {
      return game.value
    }
  )
```

---

# 52. 실무 활용: 폼 상태 읽기

```js
function readFormState() {
  const userId =
    document.querySelector(
      "#userId"
    )

  const selectedAi =
    document.querySelector(
      '[name="ai"]:checked'
    )

  const games =
    document.querySelectorAll(
      ".game:checked"
    )

  const language =
    document.querySelector(
      "#lang"
    )

  const textarea =
    document.querySelector(
      "#textarea"
    )

  return {
    userId:
      userId.value.trim(),

    ai:
      selectedAi === null
        ? null
        : selectedAi.value,

    games:
      [...games].map(
        function(game) {
          return game.value
        }
      ),

    language:
      language.value,

    memo:
      textarea.value
  }
}
```

---

# 53. 자주 하는 실수

## 53.1 NodeList에서 Checked 읽기

```js
checks2.checked
```

가 아니라:

```js
checks2[i].checked
```

를 사용해야 합니다.

## 53.2 Option에 Checked 사용

option은 `selected`를 사용합니다.

## 53.3 Date 형식을 한 자리 월·일로 설정

`2026-7-6`보다 `2026-07-06` 형식을 사용합니다.

## 53.4 ToISOString 날짜를 로컬 날짜로 단정

UTC 기준이라 자정 부근 날짜가 다를 수 있습니다.

## 53.5 Checkbox 하나만 선택된다고 생각

checkbox는 복수 선택이 가능합니다.

## 53.6 :Checked 미발견 Null 처리 누락

radio 선택이 없으면 querySelector 결과가 null일 수 있습니다.

## 53.7 Textarea 최신값을 InnerText로 읽기

현재 입력값은 `.value`를 사용합니다.

## 53.8 Textarea 입력을 InnerHTML에 넣기

XSS 위험이 있습니다.

## 53.9 Boolean을 `== true`로 비교

Boolean 값을 직접 조건으로 사용할 수 있습니다.

## 53.10 Checked 변경 후 이전 Console 결과가 바뀐다고 생각

이미 출력된 값은 자동으로 갱신되지 않습니다.

---

# 54. 면접·복습 포인트

## Q1. Input의 현재 입력값은 어떻게 읽나요?

`.value` property를 사용합니다.

## Q2. HTML value attribute와 DOM value property의 차이는 무엇인가요?

attribute는 초기 markup 값이고 property는 현재 UI 값을 나타낼 수 있습니다.

## Q3. Date input의 대표 문자열 형식은 무엇인가요?

`YYYY-MM-DD`입니다.

## Q4. GetMonth에 왜 1을 더하나요?

0부터 11까지 반환하기 때문입니다.

## Q5. 선택된 Radio 하나를 어떻게 찾나요?

`document.querySelector('[name="ai"]:checked')`를 사용할 수 있습니다.

## Q6. Checkbox 여러 개의 선택값을 어떻게 찾나요?

`querySelectorAll('.game:checked')`로 선택한 뒤 순회합니다.

## Q7. 내 Checkbox 조건문의 오류는 무엇인가요?

NodeList인 `checks2`에서 checked를 읽었습니다. 각 요소인 `checks2[i].checked`를 사용해야 합니다.

## Q8. Select의 Option 선택 상태 속성은 무엇인가요?

`selected`입니다.

## Q9. Textarea의 최신 입력값은 무엇으로 읽나요?

`.value`로 읽습니다.

## Q10. Textarea 줄바꿈을 안전하게 화면에 표시하는 방법은 무엇인가요?

`textContent`와 `white-space: pre-wrap`을 사용하면 HTML 파싱 없이 줄바꿈을 보존할 수 있습니다.

---

# Problems

## 문제 1. Text Value 읽기

`#userId`의 현재 값을 출력하세요.

## 문제 2. Text Value 변경

`#userId` 값을 `"hello"`로 변경하세요.

## 문제 3. Password 빈 값 검사

password input이 비어 있으면 `"비밀번호를 입력하세요"`를 출력하세요.

## 문제 4. Date 설정

date input에 `"2026-07-29"`를 설정하세요.

## 문제 5. 오늘 날짜 설정

현재 로컬 날짜를 `YYYY-MM-DD`로 만들어 date input에 넣으세요.

## 문제 6. Radio 선택값

name이 `"ai"`인 radio 중 선택된 value를 출력하세요.

## 문제 7. Radio 선택 변경

두 번째 radio를 JavaScript로 선택하세요.

## 문제 8. Checkbox 선택값

class `"game"`인 checkbox 중 선택된 모든 value를 출력하세요.

## 문제 9. Checkbox 미선택값

선택되지 않은 game checkbox의 value를 출력하세요.

## 문제 10. Checkbox 오류 설명

`checks.checked`가 잘못된 이유를 설명하세요.

## 문제 11. Checkbox 첫 항목 선택

첫 번째 game checkbox를 선택 상태로 만드세요.

## 문제 12. Select 현재값

`#lang`의 현재 value를 출력하세요.

## 문제 13. Select 값 변경

`#lang`의 value를 `"4"`로 변경하세요.

## 문제 14. Option Selected

두 번째 option을 직접 selected 상태로 만드세요.

## 문제 15. Textarea Value

`#textarea`의 현재 입력값을 출력하세요.

## 문제 16. 줄바꿈 위치

textarea에서 첫 줄바꿈 index를 출력하세요.

## 문제 17. 안전한 미리보기

textarea 내용을 HTML로 실행하지 않고 `#view`에 출력하세요.

## 문제 18. 줄바꿈 보존

CSS와 textContent를 이용해 textarea의 줄바꿈을 그대로 표시하세요.

## 문제 19. Radio Null 처리

선택된 radio가 없어도 오류가 나지 않도록 작성하세요.

## 문제 20. 폼 값 객체

id, ai, games, lang, textarea 값을 하나의 객체로 만드세요.

## 문제 21. 원본 오류 찾기

내 코드의 `checks2.checked == true`가 항상 의도대로 동작하지 않는 이유를 설명하세요.

## 문제 22. 종합 회원가입 검사

다음 요구사항을 만족하세요.

- 아이디 앞뒤 공백 제거
- 아이디가 비어 있으면 오류
- password가 4글자 미만이면 오류
- radio 선택이 없으면 오류
- checkbox 선택값을 배열로 저장
- select value 저장
- textarea는 원본 text 그대로 저장
- 사용자 입력을 innerHTML에 넣지 않음
- 오류가 없으면 객체 반환

---

# Answers & Explanations

## 정답 1

```js
const userId =
  document.querySelector(
    "#userId"
  )

console.log(
  userId.value
)
```

## 정답 2

```js
userId.value =
  "hello"
```

## 정답 3

```js
const password =
  document.querySelector(
    "#pw"
  )

if (
  password.value === ""
) {
  console.log(
    "비밀번호를 입력하세요"
  )
}
```

## 정답 4

```js
const date =
  document.querySelector(
    "#date"
  )

date.value =
  "2026-07-29"
```

## 정답 5

```js
const now =
  new Date()

const year =
  now.getFullYear()

const month =
  String(
    now.getMonth() + 1
  ).padStart(2, "0")

const day =
  String(
    now.getDate()
  ).padStart(2, "0")

date.value =
  `${year}-${month}-${day}`
```

## 정답 6

```js
const selectedAi =
  document.querySelector(
    '[name="ai"]:checked'
  )

if (selectedAi !== null) {
  console.log(
    selectedAi.value
  )
}
```

## 정답 7

```js
const radios =
  document.querySelectorAll(
    '[name="ai"]'
  )

radios[1].checked =
  true
```

## 정답 8

```js
const checkedGames =
  document.querySelectorAll(
    ".game:checked"
  )

checkedGames.forEach(
  function(game) {
    console.log(
      game.value
    )
  }
)
```

## 정답 9

```js
const uncheckedGames =
  document.querySelectorAll(
    ".game:not(:checked)"
  )

uncheckedGames.forEach(
  function(game) {
    console.log(
      game.value
    )
  }
)
```

## 정답 10

`checks`는 NodeList이므로 checkbox Element의 `checked` property가 없습니다. 각 요소에 접근해야 합니다.

```js
checks[i].checked
```

## 정답 11

```js
const games =
  document.querySelectorAll(
    ".game"
  )

games[0].checked =
  true
```

## 정답 12

```js
const lang =
  document.querySelector(
    "#lang"
  )

console.log(
  lang.value
)
```

## 정답 13

```js
lang.value =
  "4"
```

## 정답 14

```js
const options =
  lang.querySelectorAll(
    "option"
  )

options[1].selected =
  true
```

## 정답 15

```js
const textarea =
  document.querySelector(
    "#textarea"
  )

console.log(
  textarea.value
)
```

## 정답 16

```js
console.log(
  textarea.value
    .indexOf("\n")
)
```

## 정답 17

```js
const view =
  document.querySelector(
    "#view"
  )

view.textContent =
  textarea.value
```

## 정답 18

```css
#view {
  white-space: pre-wrap;
}
```

```js
view.textContent =
  textarea.value
```

## 정답 19

```js
const selected =
  document.querySelector(
    '[name="ai"]:checked'
  )

if (selected === null) {
  console.log(
    "선택된 항목이 없습니다."
  )
} else {
  console.log(
    selected.value
  )
}
```

## 정답 20

```js
const state = {
  id:
    document.querySelector(
      "#id"
    ).value,

  ai:
    document.querySelector(
      '[name="ai"]:checked'
    )?.value ?? null,

  games:
    [...document.querySelectorAll(
      ".game:checked"
    )].map(
      function(game) {
        return game.value
      }
    ),

  lang:
    document.querySelector(
      "#lang"
    ).value,

  textarea:
    document.querySelector(
      "#textarea"
    ).value
}

console.log(state)
```

## 정답 21

`checks2`는 여러 checkbox를 담은 NodeList입니다. `checked`는 checkbox Element의 property이므로 `checks2.checked`는 undefined입니다. `checks2[i].checked`를 사용해야 합니다.

## 정답 22

```js
function validateSignup() {
  const id =
    document.querySelector(
      "#id"
    ).value.trim()

  const password =
    document.querySelector(
      "#pw"
    ).value

  const selectedAi =
    document.querySelector(
      '[name="ai"]:checked'
    )

  const games =
    [...document.querySelectorAll(
      ".game:checked"
    )].map(
      function(game) {
        return game.value
      }
    )

  const lang =
    document.querySelector(
      "#lang"
    ).value

  const memo =
    document.querySelector(
      "#textarea"
    ).value

  if (id === "") {
    return {
      ok: false,
      message:
        "아이디를 입력하세요."
    }
  }

  if (
    password.length < 4
  ) {
    return {
      ok: false,
      message:
        "비밀번호는 4글자 이상이어야 합니다."
    }
  }

  if (
    selectedAi === null
  ) {
    return {
      ok: false,
      message:
        "AI를 선택하세요."
    }
  }

  return {
    ok: true,
    data: {
      id,
      password,
      ai:
        selectedAi.value,
      games,
      lang,
      memo
    }
  }
}
```

---

# Final Checklist

## Input Value

- [ ] input의 현재값을 `.value`로 읽었다.
- [ ] HTML 초기 value와 현재 property 값을 구분했다.
- [ ] text 값을 읽기 전·후 변경 순서를 확인했다.
- [ ] password 값을 Console에 노출하지 않았다.
- [ ] 빈 문자열을 엄격 비교했다.

## Date

- [ ] date input에 `YYYY-MM-DD` 형식을 사용했다.
- [ ] getMonth 결과에 1을 더했다.
- [ ] 월과 일을 두 자리로 만들었다.
- [ ] 로컬 날짜와 UTC ISO 날짜 차이를 이해했다.
- [ ] date value가 빈 문자열일 수 있음을 확인했다.

## Radio

- [ ] 같은 name이 radio group을 만든다는 점을 이해했다.
- [ ] `:checked`로 현재 선택 항목을 찾았다.
- [ ] 미선택 시 null을 처리했다.
- [ ] radio value가 문자열임을 이해했다.
- [ ] checked property로 선택을 변경했다.

## Checkbox

- [ ] checkbox가 복수 선택 가능함을 이해했다.
- [ ] `.game:checked`로 선택 항목을 찾았다.
- [ ] `.game:not(:checked)`로 미선택 항목을 찾았다.
- [ ] NodeList 자체에서 checked를 읽지 않았다.
- [ ] 각 Element의 checked를 확인했다.
- [ ] checked 변경 시점과 Console 출력 시점을 구분했다.
- [ ] 느슨한 Boolean 비교를 피했다.

## Select

- [ ] select.value로 현재값을 읽었다.
- [ ] select.value로 선택을 변경했다.
- [ ] option에는 checked가 아니라 selected를 사용했다.
- [ ] selectedIndex와 options 사용법을 이해했다.

## Textarea

- [ ] textarea 현재 입력값을 `.value`로 읽었다.
- [ ] 첫 줄바꿈 index를 확인했다.
- [ ] 사용자 입력을 innerHTML에 직접 넣지 않았다.
- [ ] textContent와 white-space로 줄바꿈을 보존했다.
- [ ] XSS 위험을 이해했다.

## 원본 코드 검수

- [ ] 두 실제 13_dom_form.html만 비교했다.
- [ ] text 출력 순서 차이를 기록했다.
- [ ] password 설정 차이를 기록했다.
- [ ] date 15일과 16일 차이를 기록했다.
- [ ] hr 구분 차이를 기록했다.
- [ ] 게임 이름 표기 차이를 기록했다.
- [ ] 내 `checks2.checked` 오류를 기록했다.
- [ ] 강사님 `checks2[i].checked` 정상 코드를 기록했다.
- [ ] select checked 설명 오류를 기록했다.
- [ ] textarea innerHTML 위험을 기록했다.
- [ ] toISOString UTC 주의를 기록했다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 13번은 text, password, date, radio, checkbox, select, textarea 값을 읽고 변경하는 폼 DOM 실습이다.
- input의 현재 입력값은 `.value`로 읽는다.
- HTML의 value attribute는 초기값이고 DOM value property는 현재값을 나타낼 수 있다.
- 내 코드는 text를 `"12345"`로 변경한 뒤 출력하므로 초기 `"abcd"`를 확인하지 못한다.
- 강사님 코드는 초기 `"abcd"`를 출력한 뒤 `"12345"`로 변경한다.
- 강사님은 password에 `"abcd"`를 설정하지만 내 코드는 읽기만 한다.
- password 값은 실제 서비스에서 Console에 출력하지 않는 것이 안전하다.
- date input의 초기 미선택값은 빈 문자열이다.
- date input에는 일반적으로 `YYYY-MM-DD` 형식을 사용한다.
- 내 직접 날짜는 `2026-07-16`, 강사님은 `2026-07-15`다.
- getMonth는 0~11이므로 실제 월에 1을 더한다.
- 월과 일은 두 자리 문자열로 만들어 date input에 넣는다.
- toISOString은 UTC 기준이므로 로컬 날짜와 달라질 수 있다.
- 같은 name의 radio는 하나의 그룹이며 한 항목만 선택된다.
- `[name=ai]:checked`는 현재 선택된 radio를 찾는다.
- 선택된 radio가 없으면 querySelector 결과가 null일 수 있다.
- NodeList의 특정 radio는 `radios[index].checked = true`로 선택할 수 있다.
- checkbox는 여러 항목을 동시에 선택할 수 있다.
- `.game:checked`는 선택 항목, `.game:not(:checked)`는 미선택 항목을 찾는다.
- 내 코드의 `checks2.checked`는 NodeList에서 checked를 읽으므로 잘못되었다.
- 강사님 코드의 `checks2[i].checked`가 올바른 접근이다.
- `checks2[0].checked = true`는 상태 출력 반복문 뒤에 있어 앞 Console 결과에는 반영되지 않는다.
- select의 현재값은 `select.value`로 읽고 같은 property로 선택을 변경할 수 있다.
- option 선택 속성은 checked가 아니라 selected다.
- textarea의 최신 편집값은 `.value`로 읽는다.
- 줄바꿈이 없으면 `indexOf("\n")`은 -1이다.
- textarea 줄바꿈을 `/\n/g`로 `<br>`에 바꿀 수 있지만 innerHTML에 넣으면 XSS 위험이 남는다.
- 안전한 미리보기는 `textContent`와 `white-space: pre-wrap`을 사용할 수 있다.
