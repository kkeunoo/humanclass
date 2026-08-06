---
title: JavaScript DOM 폼 요소와 입력값 처리
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript DOM 폼 요소와 입력값 처리

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `13_JavaScript_DOM_폼요소와_입력값처리.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/13_dom_form.html`, `workspace_teacher/workspace_html/javascript/13_dom_form.html` |
| 핵심 범위 | `input.value`, 비밀번호 입력, 날짜 입력, `checked`, 라디오 버튼, 체크박스, `select.value`, `textarea.value`, 줄바꿈 처리 |
| 실습 범위 | 입력값 읽기·변경, 오늘 날짜 설정, 선택값 조회, 체크 상태 변경, Textarea 미리보기 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 폼 요소의 현재값과 선택 상태를 읽고 변경하는 데 필요한 핵심 코드만 발췌하고, 잘못된 입력·보안·접근성·렌더링 안전성까지 함께 설명한다.

---

# 개요

폼 요소는 사용자가 값을 입력하거나 선택할 수 있는 DOM 요소다.

```html
<input type="text">
<input type="password">
<input type="date">
<input type="radio">
<input type="checkbox">
<select></select>
<textarea></textarea>
```

JavaScript에서는 요소 종류에 따라 주로 다음 property를 사용한다.

| 요소 | 주요 property |
| --- | --- |
| Text·Password·Date | `value` |
| Radio·Checkbox | `checked`, `value` |
| Select | `value`, `selectedIndex` |
| Option | `selected`, `value` |
| Textarea | `value` |
| Form | `elements`, `reset()`, `submit()` |

> [!IMPORTANT]
> HTML에 작성된 초기값과 사용자가 현재 입력한 값은 서로 다를 수 있다.
>
> 폼의 현재 상태를 읽을 때는 일반적으로 DOM property를 사용한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `value` | 현재 입력값·선택값 읽기와 변경 |
| `checked` | Radio·Checkbox 선택 여부 |
| `selected` | Option 선택 여부 |
| `selectedIndex` | 선택된 Option 인덱스 |
| `:checked` | 현재 선택된 Radio·Checkbox CSS 선택자 |
| `:not()` | 조건에 맞지 않는 요소 선택 |
| `input` 이벤트 | 사용자가 값을 변경할 때마다 발생 |
| `change` 이벤트 | 값 변경이 확정될 때 발생 |
| 초기 Attribute | HTML 작성 시점의 값 |
| 현재 Property | 사용자 조작 후 현재 상태 |
| FormData | 폼의 이름·값을 구조화해 수집 |

---

# 학습 목표

- Text·Password·Date 입력 요소의 현재값을 읽고 변경할 수 있다.
- HTML `value` attribute와 DOM `value` property 차이를 설명할 수 있다.
- 비밀번호 값을 Console에 출력하면 위험한 이유를 이해한다.
- `input[type="date"]`의 값 형식을 설명할 수 있다.
- 로컬 날짜 기준 `YYYY-MM-DD` 문자열을 만들 수 있다.
- ISO 날짜와 로컬 날짜가 달라질 수 있음을 이해한다.
- 선택된 Radio 요소 하나를 찾을 수 있다.
- Radio 전체 목록에서 특정 항목을 선택할 수 있다.
- Checkbox의 중복 선택 상태를 순회할 수 있다.
- `NodeList` 전체가 아니라 개별 요소의 `checked`를 확인할 수 있다.
- `:checked`와 `:not(:checked)`를 사용할 수 있다.
- Select의 현재값을 읽고 변경할 수 있다.
- Option의 `selected` 상태를 확인할 수 있다.
- Textarea의 현재값과 줄바꿈을 처리할 수 있다.
- 사용자 문자열을 안전하게 화면에 표시할 수 있다.
- `innerHTML` 대신 `textContent`와 CSS를 활용할 수 있다.
- 폼 요소와 `label`을 연결할 수 있다.
- `FormData`로 선택된 폼 값을 수집할 수 있다.

---

# 1. 원본 폼 구조

```html
<form>
    <input
        type="text"
        id="user-id"
        value="abcd"
    >

    <input
        type="password"
        id="password"
    >

    <input
        type="date"
        id="date"
    >
</form>
```

원본에서는 Text·Password·Date를 순서대로 배치한다.

---

# 2. `value` property

```javascript
const textInput = (
    document.querySelector(
        "#user-id",
    )
)

console.log(
    textInput.value,
)
```

`value`는 요소의 현재 입력값을 문자열로 반환한다.

---

# 3. 초기값과 현재값

```html
<input
    id="user-id"
    value="abcd"
>
```

초기 attribute:

```javascript
textInput.getAttribute(
    "value",
)
```

현재 property:

```javascript
textInput.value
```

사용자가 값을 바꾸면 두 결과가 달라질 수 있다.

---

# 4. 입력값 변경

```javascript
textInput.value = "12345"
```

화면에 표시되는 현재값도 변경된다.

---

# 5. Text input 값의 자료형

```javascript
textInput.value = "123"

console.log(
    typeof textInput.value,
)
```

출력:

```text
string
```

숫자처럼 보여도 Text input의 `value`는 문자열이다.

---

# 6. 숫자 입력 변환

```javascript
const number = Number(
    textInput.value,
)

if (Number.isNaN(number)) {
    console.log(
        "숫자를 입력해주세요.",
    )
}
```

계산 전 명시적으로 변환하고 검증한다.

---

# 7. Password 입력값

```javascript
const passwordInput = (
    document.querySelector(
        "#password",
    )
)

console.log(
    passwordInput.value,
)
```

기술적으로 현재 비밀번호 값을 읽을 수 있다.

---

# 8. 비밀번호 Console 출력 주의

> [!WARNING]
> 실제 서비스에서는 비밀번호를 Console·로그·서버 오류 메시지에 출력하지 않는다.

위험:

- 개발자 도구 노출
- 원격 로그 수집
- 화면 공유·스크린샷 노출
- 운영 로그 장기 보관
- 디버깅 도구를 통한 유출

---

# 9. 비밀번호 설정

강사님 코드:

```javascript
passwordInput.value = "abcd"
```

학습 예제로는 property 변경을 보여 주지만 실제 로그인 화면에서 비밀번호를 임의로 채우는 기능은 보안·UX 요구사항을 먼저 확인해야 한다.

---

# 10. Date input

```javascript
const dateInput = (
    document.querySelector(
        "#date",
    )
)

console.log(
    `[${dateInput.value}]`,
)
```

날짜가 선택되지 않았다면 빈 문자열이다.

```text
[]
```

---

# 11. Date input 값 형식

```text
YYYY-MM-DD
```

올바른 예:

```javascript
dateInput.value = (
    "2026-07-16"
)
```

잘못된 예:

```text
2026-7-16
```

브라우저가 값을 적용하지 않을 수 있다.

---

# 12. 현재 연도

```javascript
const today = new Date()

const year = (
    today.getFullYear()
)
```

로컬 시간대 기준 연도를 읽는다.

---

# 13. 현재 월

```javascript
let month = (
    today.getMonth() + 1
)
```

`getMonth()`는 0부터 11까지 반환하므로 1을 더한다.

---

# 14. 월 두 자리 처리

원본:

```javascript
if (month < 10) {
    month = "0" + month
}
```

개선:

```javascript
const month = String(
    today.getMonth() + 1,
).padStart(
    2,
    "0",
)
```

---

# 15. 날짜 두 자리 처리

원본:

```javascript
let day = today.getDate()

day = (
    "0" + day
).slice(-2)
```

개선:

```javascript
const day = String(
    today.getDate(),
).padStart(
    2,
    "0",
)
```

---

# 16. 로컬 오늘 날짜 생성

```javascript
function getLocalDateValue(
    date = new Date(),
) {
    const year = (
        date.getFullYear()
    )

    const month = String(
        date.getMonth() + 1,
    ).padStart(
        2,
        "0",
    )

    const day = String(
        date.getDate(),
    ).padStart(
        2,
        "0",
    )

    return (
        `${year}-${month}-${day}`
    )
}
```

---

# 17. Date input에 오늘 설정

```javascript
dateInput.value = (
    getLocalDateValue()
)
```

사용자 지역의 오늘 날짜를 설정한다.

---

# 18. ISO 날짜 방식

원본:

```javascript
today
    .toISOString()
    .split("T")[0]
```

이 값은 UTC 기준 날짜다.

---

# 19. ISO와 로컬 날짜 차이

한국처럼 UTC보다 앞선 시간대에서는 오전 시간대에도 날짜 차이가 생길 수 있고, UTC보다 늦은 시간대에서는 로컬 자정 부근에 이전·다음 날짜가 될 수 있다.

> [!WARNING]
> 사용자 화면의 “오늘”에는 로컬 getter를 조합하는 방식을 사용하는 편이 안전하다.

---

# 20. Radio 기본 구조

```html
<input
    type="radio"
    name="ai"
    value="1"
    checked
>
ChatGPT

<input
    type="radio"
    name="ai"
    value="2"
>
Gemini
```

같은 `name`을 가진 Radio는 일반적으로 하나만 선택된다.

---

# 21. 선택된 Radio 찾기

```javascript
const selectedRadio = (
    document.querySelector(
        '[name="ai"]:checked',
    )
)
```

선택된 요소 하나 또는 `null`을 반환한다.

---

# 22. Radio Null 처리

```javascript
const selectedValue = (
    selectedRadio?.value
    ?? null
)

console.log(
    selectedValue,
)
```

선택값이 없을 수 있는 구조에서는 `null`을 처리한다.

---

# 23. Radio Value 읽기

```javascript
if (
    selectedRadio
    !== null
) {
    console.log(
        selectedRadio.value,
    )
}
```

원본 기본 선택값은 `"1"`이다.

---

# 24. Radio 전체 선택

```javascript
const radios = (
    document.querySelectorAll(
        '[name="ai"]',
    )
)
```

반환값은 `NodeList`다.

---

# 25. 특정 Radio 선택

원본:

```javascript
radios[1].checked = true
```

두 번째 Radio가 선택되고 같은 그룹의 기존 선택은 해제된다.

---

# 26. 인덱스 선택의 위험

```javascript
radios[1]
```

HTML 순서가 바뀌면 다른 항목을 선택하게 된다.

값을 기준으로 선택하는 방식이 더 명확하다.

```javascript
const geminiRadio = (
    document.querySelector(
        '[name="ai"][value="2"]',
    )
)

if (
    geminiRadio
    !== null
) {
    geminiRadio.checked = true
}
```

---

# 27. Label 연결

원본은 입력 요소 뒤에 텍스트만 작성한다.

개선:

```html
<input
    type="radio"
    id="ai-chatgpt"
    name="ai"
    value="1"
>

<label for="ai-chatgpt">
    ChatGPT
</label>
```

Label 텍스트를 클릭해도 입력 요소가 선택된다.

---

# 28. Checkbox 구조

```html
<input
    type="checkbox"
    class="game"
    value="a"
>
마비노기 모바일
```

Checkbox는 같은 그룹에서도 여러 개를 동시에 선택할 수 있다.

---

# 29. 선택되지 않은 Checkbox

원본:

```javascript
const uncheckedGames = (
    document.querySelectorAll(
        ".game:not(:checked)",
    )
)
```

현재 선택되지 않은 게임 Checkbox만 반환한다.

---

# 30. 선택된 Checkbox

```javascript
const checkedGames = (
    document.querySelectorAll(
        ".game:checked",
    )
)
```

---

# 31. Checkbox 순회

```javascript
for (
    const checkbox
    of checkedGames
) {
    console.log(
        checkbox.value,
    )
}
```

---

# 32. 모든 Checkbox 상태

```javascript
const gameCheckboxes = (
    document.querySelectorAll(
        ".game",
    )
)

for (
    const checkbox
    of gameCheckboxes
) {
    console.log(
        checkbox.value,
        checkbox.checked,
    )
}
```

---

# 33. 원본의 Checkbox 오류

내 코드:

```text
if (
    checks2.checked == true
) {
```

`checks2`는 `NodeList`이므로 `checked` property가 없다.

올바른 코드:

```text
if (
    gameCheckboxes[index]
        .checked
    === true
) {
```

또는:

```javascript
for (
    const checkbox
    of gameCheckboxes
) {
    if (checkbox.checked) {
        console.log(
            checkbox.value,
        )
    }
}
```

---

# 34. Checkbox 선택 변경

```javascript
gameCheckboxes[0]
    .checked = true
```

첫 번째 Checkbox를 선택 상태로 변경한다.

---

# 35. 값 기준 Checkbox 선택

```javascript
const game = (
    document.querySelector(
        '.game[value="a"]',
    )
)

if (game !== null) {
    game.checked = true
}
```

인덱스보다 의미가 명확하다.

---

# 36. 선택값 배열 만들기

```javascript
const selectedGames = [
    ...document.querySelectorAll(
        ".game:checked",
    ),
].map(
    checkbox => (
        checkbox.value
    ),
)

console.log(
    selectedGames,
)
```

---

# 37. Checkbox 전체 선택

```javascript
for (
    const checkbox
    of gameCheckboxes
) {
    checkbox.checked = true
}
```

---

# 38. Checkbox 전체 해제

```javascript
for (
    const checkbox
    of gameCheckboxes
) {
    checkbox.checked = false
}
```

---

# 39. Select 기본 구조

```html
<select id="language">
    <option value="1">
        JavaScript
    </option>

    <option
        value="2"
        selected
    >
        Python
    </option>
</select>
```

---

# 40. Select Value

```javascript
const languageSelect = (
    document.getElementById(
        "language",
    )
)

console.log(
    languageSelect.value,
)
```

선택된 Option의 `value`를 반환한다.

원본 기본값은 `"2"`다.

---

# 41. Select 값 변경

```javascript
languageSelect.value = "4"
```

`value="4"`인 Option이 선택된다.

일치하는 Option이 없으면 브라우저 상태에 따라 선택값이 비어 보일 수 있다.

---

# 42. Option Selected

```javascript
const selectedOption = (
    languageSelect
        .selectedOptions[0]
)

console.log(
    selectedOption?.textContent,
)
```

현재 선택된 Option의 표시 텍스트를 읽을 수 있다.

---

# 43. `selectedIndex`

```javascript
console.log(
    languageSelect
        .selectedIndex,
)
```

선택된 Option의 인덱스를 반환한다.

선택된 항목이 없으면 `-1`일 수 있다.

---

# 44. Option 직접 선택

```javascript
const javaOption = (
    languageSelect.querySelector(
        'option[value="4"]',
    )
)

if (
    javaOption
    !== null
) {
    javaOption.selected = true
}
```

---

# 45. Select와 `checked`

원본 설명 중 Select도 `checked = true`를 사용한다는 표현은 수정이 필요하다.

```text
Radio·Checkbox
→ checked

Option
→ selected

Select
→ value, selectedIndex
```

---

# 46. Textarea 기본 구조

```html
<textarea id="message">
초기값
</textarea>
```

Textarea의 현재 입력값은 `value`로 읽는다.

---

# 47. Textarea Value

```javascript
const textarea = (
    document.querySelector(
        "#message",
    )
)

console.log(
    textarea.value,
)
```

---

# 48. Textarea와 `innerText`

Textarea의 사용자 현재 입력값을 읽을 때는 `value`를 사용한다.

```text
textarea.value
→ 현재 입력값

textarea.textContent
→ 초기 HTML 텍스트에 가까운 값
```

---

# 49. 줄바꿈 검색

```javascript
console.log(
    textarea.value.indexOf(
        "\n",
    ),
)
```

첫 번째 줄바꿈의 인덱스를 반환한다.

없으면 `-1`이다.

---

# 50. 원본 Textarea 미리보기

```javascript
const view = document.querySelector(
    "#view",
)

view.innerHTML = (
    textarea.value
)
```

사용자가 입력한 문자열이 HTML로 파싱될 수 있다.

---

# 51. `innerHTML` 위험

사용자가 다음 값을 입력하면:

```html
<img
    src="invalid"
    onerror="alert(1)"
>
```

`innerHTML`을 통해 이벤트 코드가 실행될 수 있다.

> [!WARNING]
> 사용자 입력을 `innerHTML`에 직접 넣지 않는다.

---

# 52. 줄바꿈을 `<br>`로 바꾸는 원본

```javascript
const html = textarea.value.replace(
    /\n/g,
    "<br>",
)

view.innerHTML = html
```

줄바꿈은 표현되지만 사용자 HTML도 함께 실행될 수 있다.

---

# 53. 안전한 줄바꿈 표시

CSS:

```css
#view {
    white-space: pre-wrap;
}
```

JavaScript:

```javascript
view.textContent = (
    textarea.value
)
```

사용자 문자열을 텍스트로 유지하면서 줄바꿈과 공백을 표시한다.

---

# 54. `white-space: pre-wrap`

```text
줄바꿈 유지
연속 공백 유지
필요하면 자동 줄바꿈
```

Textarea 미리보기에 적합하다.

---

# 55. Textarea 실시간 미리보기

```javascript
textarea.addEventListener(
    "input",
    () => {
        view.textContent = (
            textarea.value
        )
    },
)
```

사용자가 입력할 때마다 안전하게 미리보기를 갱신한다.

---

# 56. `input`과 `change`

| 이벤트 | 발생 시점 |
| --- | --- |
| `input` | 값이 바뀔 때마다 |
| `change` | 변경이 확정되거나 포커스를 잃을 때 |
| `click` | 클릭 동작 |
| `submit` | Form 제출 |

Text·Textarea 실시간 반응에는 `input`을 자주 사용한다.

---

# 57. 원본의 `setTimeout()`

원본은 페이지 로드 3초 후 폼 값을 읽고 변경한다.

```javascript
setTimeout(
    () => {
        // 폼 조작
    },
    3000,
)
```

폼 요소 사용법을 확인하는 학습 예제로는 가능하다.

실제 UI에서는 사용자 이벤트에 연결하는 경우가 많다.

---

# 58. Form 요소

```javascript
const form = document.querySelector(
    "form",
)

console.log(
    form.elements,
)
```

폼 내부의 입력 요소 목록에 접근할 수 있다.

---

# 59. Name 속성의 중요성

Form 제출과 `FormData`에서는 `name` 속성이 키가 된다.

```html
<input
    type="text"
    name="userId"
>
```

`id`는 DOM 선택·Label 연결에, `name`은 폼 데이터 그룹과 제출에 주로 사용한다.

---

# 60. `FormData`

```javascript
const formData = new FormData(
    form,
)

for (
    const [
        name,
        value,
    ]
    of formData.entries()
) {
    console.log(
        name,
        value,
    )
}
```

선택된 Radio·Checkbox와 입력값을 수집할 수 있다.

---

# 61. Checkbox와 FormData

선택된 Checkbox만 포함된다.

같은 `name`을 가진 여러 Checkbox를 모두 읽으려면:

```javascript
const games = (
    formData.getAll(
        "games",
    )
)
```

HTML:

```html
<input
    type="checkbox"
    name="games"
    value="minecraft"
>
```

---

# 62. `form.reset()`

```javascript
form.reset()
```

폼 요소를 초기 HTML 기본 상태로 되돌린다.

현재값을 빈 값으로 만드는 것과 항상 같지는 않다.

---

# 63. `defaultValue`와 `defaultChecked`

```javascript
console.log(
    textInput.defaultValue,
)

console.log(
    gameCheckboxes[0]
        .defaultChecked,
)
```

초기 기본 상태를 나타낸다.

---

# 64. 접근성 개선 HTML

```html
<form id="profile-form">
    <div>
        <label for="user-id">
            아이디
        </label>

        <input
            type="text"
            id="user-id"
            name="userId"
            autocomplete="username"
        >
    </div>

    <fieldset>
        <legend>
            AI 서비스
        </legend>

        <input
            type="radio"
            id="ai-chatgpt"
            name="ai"
            value="chatgpt"
        >

        <label for="ai-chatgpt">
            ChatGPT
        </label>
    </fieldset>
</form>
```

---

# 65. `fieldset`과 `legend`

Radio·Checkbox 그룹의 목적을 사용자와 스크린 리더에 전달한다.

```text
fieldset
→ 관련 입력 그룹

legend
→ 그룹 제목
```

---

# 66. 필수 요소 선택 함수

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
            `${selector} 요소가 없습니다.`,
        )
    }

    return element
}
```

폼 기능이 필수 요소 누락으로 조용히 실패하는 것을 막는다.

---

# 67. 폼 상태 읽기 함수

```javascript
function getFormState() {
    const selectedAi = (
        document.querySelector(
            '[name="ai"]:checked',
        )
    )

    const selectedGames = [
        ...document.querySelectorAll(
            '[name="games"]:checked',
        ),
    ].map(
        input => input.value,
    )

    return {
        userId: (
            textInput.value.trim()
        ),
        date: dateInput.value,
        ai: (
            selectedAi?.value
            ?? null
        ),
        games: selectedGames,
        language: (
            languageSelect.value
        ),
        message: (
            textarea.value
        ),
    }
}
```

---

# 68. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| Text | 변경 후 출력 | 출력 후 변경 |
| Password | 값 출력만 함 | 값 출력 후 `"abcd"` 설정 |
| Date 초기값 | `2026-07-16` | `2026-07-15` |
| 오늘 날짜 | 상세 주석과 두 방식 비교 | 핵심 계산 중심 |
| Radio | 선택값 조회·두 번째 선택 | 동일 |
| Checkbox | `:not(:checked)` 설명 상세 | 기본 순회 |
| Checkbox 두 번째 순회 | `checks2.checked` 오타 | 올바른 `checks2[i].checked` |
| Select | `value` 변경 설명 상세 | 기본 값 조회·변경 |
| Textarea | 줄바꿈 정규표현식 설명 | 기본 코드 |
| 보안 | 별도 설명 없음 | 별도 설명 없음 |

## 68-1. 내 코드의 장점

- `input.value`가 현재 최신값이라는 점을 상세히 기록했다.
- 로컬 날짜 형식을 직접 조립하는 과정을 설명했다.
- `:checked`와 `:not(:checked)` 선택자를 비교했다.
- Select와 Textarea의 값 처리 방법을 주석으로 정리했다.
- 줄바꿈을 `<br>`로 변경하는 정규표현식을 설명했다.

## 68-2. 내 코드의 개선점

- `checks2.checked`는 NodeList에 존재하지 않는 property다.
- 비밀번호를 Console에 출력하지 않아야 한다.
- Radio·Checkbox의 Label 연결이 없다.
- Select Option은 `checked`가 아니라 `selected`를 사용한다.
- ISO 날짜를 로컬 오늘 날짜와 동일하게 사용하면 날짜 차이가 날 수 있다.
- Textarea 값을 `innerHTML`에 넣어 XSS가 발생할 수 있다.
- 여러 입력 요소의 `id`와 변수 이름을 더 의미 있게 작성할 수 있다.

## 68-3. 강사님 코드의 장점

- Text·Password·Date·Radio·Checkbox·Select·Textarea를 한 번에 다룬다.
- 오늘 날짜를 Date input 형식으로 변경하는 과정을 보여 준다.
- Checkbox의 개별 `checked` 상태를 올바르게 확인한다.
- Select 값을 직접 변경하는 간단한 예제를 제공한다.

## 68-4. 강사님 코드의 보충점

- 비밀번호 값 출력의 위험을 설명할 필요가 있다.
- `selected`와 `checked` 차이를 설명할 필요가 있다.
- `input`·`change` 이벤트와 실제 폼 사용 흐름을 보충할 수 있다.
- Textarea 미리보기에서 `innerHTML`의 보안 위험을 설명해야 한다.
- `FormData`, `label`, `fieldset`을 추가하면 실무 연결성이 높아진다.

---

# 69. 기존 코드에서 개선 코드로 바꾼 이유

## 69-1. Checkbox 개별 상태 검사

기존:

```text
checks2.checked
```

개선:

```javascript
for (
    const checkbox
    of gameCheckboxes
) {
    if (checkbox.checked) {
        console.log(
            checkbox.value,
        )
    }
}
```

## 69-2. 오늘 날짜 처리

기존:

```javascript
new Date()
    .toISOString()
    .split("T")[0]
```

개선:

```javascript
getLocalDateValue()
```

## 69-3. Textarea 미리보기

기존:

```javascript
view.innerHTML = (
    textarea.value.replace(
        /\n/g,
        "<br>",
    )
)
```

개선:

```javascript
view.textContent = (
    textarea.value
)
```

CSS:

```css
#view {
    white-space: pre-wrap;
}
```

## 69-4. 인덱스 기반 선택

기존:

```javascript
radios[1].checked = true
```

개선:

```javascript
const targetRadio = (
    document.querySelector(
        '[name="ai"][value="2"]',
    )
)

if (
    targetRadio
    !== null
) {
    targetRadio.checked = true
}
```

---

# 70. 실무형 예제: 프로필 폼 미리보기

```javascript
const form = getRequiredElement(
    "#profile-form",
)

const preview = getRequiredElement(
    "#profile-preview",
)

function renderPreview() {
    const formData = new FormData(
        form,
    )

    const userId = String(
        formData.get(
            "userId",
        ) ?? "",
    ).trim()

    const ai = formData.get(
        "ai",
    )

    const games = formData.getAll(
        "games",
    )

    const language = formData.get(
        "language",
    )

    const message = String(
        formData.get(
            "message",
        ) ?? "",
    )

    preview.replaceChildren()

    const summary = (
        document.createElement(
            "dl",
        )
    )

    const values = [
        [
            "아이디",
            userId || "미입력",
        ],
        [
            "AI",
            ai || "미선택",
        ],
        [
            "게임",
            games.join(", ")
            || "미선택",
        ],
        [
            "언어",
            language || "미선택",
        ],
        [
            "메시지",
            message || "미입력",
        ],
    ]

    for (
        const [
            label,
            value,
        ]
        of values
    ) {
        const term = (
            document.createElement(
                "dt",
            )
        )

        const description = (
            document.createElement(
                "dd",
            )
        )

        term.textContent = label
        description.textContent = value

        summary.append(
            term,
            description,
        )
    }

    preview.append(summary)
}

form.addEventListener(
    "input",
    renderPreview,
)

form.addEventListener(
    "change",
    renderPreview,
)

renderPreview()
```

## 70-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `FormData` | 폼 전체 현재값 수집 |
| `getAll()` | 여러 Checkbox 값 수집 |
| `trim()` | 공백 입력 정리 |
| `textContent` | 사용자 입력 안전 출력 |
| `replaceChildren()` | 기존 미리보기 교체 |
| `input` 이벤트 | Text·Textarea 실시간 반영 |
| `change` 이벤트 | Radio·Checkbox·Select 반영 |
| Node 생성 | HTML 문자열 삽입 없이 안전한 렌더링 |

---

# 71. 대표 오류로 이해하기

## 71-1. `null.value`

선택한 요소가 없으면 `TypeError`가 발생한다.

## 71-2. NodeList에 `checked` 사용

`checked`는 개별 input 요소의 property다.

## 71-3. Date 형식 오류

`YYYY-MM-DD`가 아니면 값이 적용되지 않을 수 있다.

## 71-4. Select에 존재하지 않는 Value 설정

일치하는 Option을 선택할 수 없다.

## 71-5. `innerHTML`에 사용자 입력 삽입

XSS가 발생할 수 있다.

## 71-6. 비밀번호 로그 출력

개인정보와 인증정보가 노출될 수 있다.

---

# 72. 자주 하는 실수

## 72-1. HTML `value`가 항상 현재값이라고 생각

사용자가 변경한 현재값은 property에 있다.

## 72-2. Input Value를 숫자로 생각

기본적으로 문자열이다.

## 72-3. 비밀번호를 일반 Text처럼 로그에 출력

민감정보는 기록하지 않는다.

## 72-4. Date Month를 두 자리로 만들지 않음

`YYYY-MM-DD` 형식을 맞춰야 한다.

## 72-5. UTC ISO 날짜를 로컬 오늘 날짜로 사용

시간대에 따라 날짜가 다를 수 있다.

## 72-6. 선택된 Radio가 항상 있다고 생각

선택이 없으면 `null`이다.

## 72-7. Checkbox도 하나만 선택된다고 생각

여러 개를 동시에 선택할 수 있다.

## 72-8. NodeList에 `checked` 사용

각 요소를 순회해야 한다.

## 72-9. Option에 `checked` 사용

`selected`를 사용한다.

## 72-10. Textarea 줄바꿈을 위해 사용자 입력을 `innerHTML`에 삽입

`textContent`와 `white-space: pre-wrap`을 사용한다.

---

# 73. 핵심 요약

```text
input.value
textarea.value
select.value
→ 현재값
```

```text
radio.checked
checkbox.checked
→ 선택 여부

option.selected
→ Option 선택 여부
```

```text
[name="ai"]:checked
→ 선택된 Radio

.game:checked
→ 선택된 Checkbox

.game:not(:checked)
→ 선택되지 않은 Checkbox
```

```text
FormData
→ 폼 데이터 수집

input 이벤트
→ 값 변경마다

change 이벤트
→ 선택·변경 확정
```

---

# 74. 최종 체크리스트

- [ ] Input의 현재값을 `value`로 읽을 수 있는가?
- [ ] 초기 Attribute와 현재 Property를 구분할 수 있는가?
- [ ] Text input 값이 문자열임을 이해했는가?
- [ ] 비밀번호를 로그에 출력하지 않는가?
- [ ] Date input의 형식을 설명할 수 있는가?
- [ ] 로컬 오늘 날짜를 `YYYY-MM-DD`로 만들 수 있는가?
- [ ] ISO UTC 날짜와 로컬 날짜 차이를 이해했는가?
- [ ] 선택된 Radio 요소를 찾을 수 있는가?
- [ ] Radio 선택 없음 상태를 처리할 수 있는가?
- [ ] 값을 기준으로 Radio를 선택할 수 있는가?
- [ ] Checkbox의 여러 선택값을 순회할 수 있는가?
- [ ] NodeList 전체가 아닌 개별 `checked`를 확인할 수 있는가?
- [ ] `:checked`와 `:not(:checked)`를 사용할 수 있는가?
- [ ] Select 값을 읽고 변경할 수 있는가?
- [ ] `checked`와 `selected`를 구분할 수 있는가?
- [ ] Textarea의 현재값을 `value`로 읽을 수 있는가?
- [ ] 줄바꿈을 안전하게 화면에 표시할 수 있는가?
- [ ] `input`과 `change` 이벤트를 구분할 수 있는가?
- [ ] `FormData`로 폼 값을 수집할 수 있는가?
- [ ] Label·Fieldset·Legend로 접근성을 개선할 수 있는가?
- [ ] 사용자 입력을 `innerHTML`에 직접 넣지 않는가?

---

# 마무리

폼 처리의 핵심은 입력값을 가져오는 것에서 끝나지 않는다.

```text
현재 property 값을 정확히 읽고
    ↓
입력 형식과 선택 상태를 검증하고
    ↓
민감정보를 노출하지 않고
    ↓
사용자 문자열을 안전하게 렌더링하고
    ↓
접근 가능한 폼 구조와 이벤트 흐름을 만드는 것
```

이 흐름을 이해하면 이후 이벤트 문서에서 입력·선택·제출 동작을 더 안전하게 연결할 수 있다.
