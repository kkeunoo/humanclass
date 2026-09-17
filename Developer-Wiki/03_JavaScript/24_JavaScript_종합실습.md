---
title: JavaScript 종합실습
version: v4.0-detailed-source
last_updated: 2026-09-17
status: Completed
---

# JavaScript 종합실습

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `24_JavaScript_종합실습.md` |
| 분류 | `03_JavaScript` |
| 실습 주제 | 회원·할 일 관리 대시보드 |
| 핵심 범위 | 변수, 조건문, 반복문, 배열, 객체, 함수, DOM, 이벤트, 폼, JSON, Local Storage, Fetch, 비동기, 오류 처리 |
| 구현 방식 | 상태 중심 설계, 함수 분리, Event Delegation, 안전한 DOM 렌더링 |
| 문서 형식 | 요구사항 → 설계 → 단계별 구현 → 완성 코드 → 실행 결과 → 해설 → 개선 포인트 |

> 이 문서는 JavaScript 01~23번에서 학습한 내용을 하나의 프로젝트 흐름으로 연결한다.  
> 단순 문제 모음이 아니라, 실무에서 자주 사용하는 **입력 → 검증 → 상태 저장 → 렌더링 → 이벤트 → 저장소 → 비동기 요청** 구조를 직접 구현한다.

---

## 이 문서에서 바로 찾기

- [개념에서 실제 실행까지: 종합실습은 상태를 기준으로 입력과 화면을 연결하는 프로젝트다](#js-24-section-3)
- [25. 요약 정보 렌더링](#js-24-section-28)
- [43. 대표 오류와 해결](#js-24-section-46)
- [46. 종합실습 체크리스트](#js-24-section-49)
- [47. 핵심 요약](#js-24-section-50)

<details>
<summary>세부 목차 펼치기 — 번호형 본문 전체</summary>

- [프로젝트 개요](#js-24-section-1)
- [학습 목표](#js-24-section-2)
- [개념에서 실제 실행까지: 종합실습은 상태를 기준으로 입력과 화면을 연결하는 프로젝트다](#js-24-section-3)
- [1. 요구사항](#js-24-section-4)
- [2. 화면 구조](#js-24-section-5)
- [3. 상태 설계](#js-24-section-6)
- [4. DOM 요소 선택](#js-24-section-7)
- [5. Local Storage Key](#js-24-section-8)
- [6. 안전한 JSON 저장](#js-24-section-9)
- [7. 안전한 JSON 복원](#js-24-section-10)
- [8. 저장 데이터 검증](#js-24-section-11)
- [9. 회원 API 함수](#js-24-section-12)
- [10. 회원 불러오기](#js-24-section-13)
- [11. 회원 Select 렌더링](#js-24-section-14)
- [12. 할 일 ID 생성](#js-24-section-15)
- [13. 할 일 Form 검증](#js-24-section-16)
- [14. 할 일 객체 생성](#js-24-section-17)
- [15. 할 일 추가](#js-24-section-18)
- [16. 담당 회원 검색](#js-24-section-19)
- [17. 우선순위 Label](#js-24-section-20)
- [18. 할 일 Item 생성](#js-24-section-21)
- [19. 검색 결과 계산](#js-24-section-22)
- [20. 상태 필터](#js-24-section-23)
- [21. 우선순위 점수](#js-24-section-24)
- [22. 정렬 함수](#js-24-section-25)
- [23. 화면에 표시할 할 일 계산](#js-24-section-26)
- [24. 목록 렌더링](#js-24-section-27)
- [25. 요약 정보 렌더링](#js-24-section-28)
- [26. 전체 선택 상태 계산](#js-24-section-29)
- [27. 전체 렌더링](#js-24-section-30)
- [28. 할 일 찾기](#js-24-section-31)
- [29. 목록 Event Delegation](#js-24-section-32)
- [30. 개별 삭제 Event Delegation](#js-24-section-33)
- [31. 검색 입력](#js-24-section-34)
- [32. 필터 변경](#js-24-section-35)
- [33. 정렬 변경](#js-24-section-36)
- [34. 전체 선택 변경](#js-24-section-37)
- [35. 선택 삭제](#js-24-section-38)
- [36. 이벤트 등록](#js-24-section-39)
- [37. 초기화](#js-24-section-40)
- [38. 완성 JavaScript 코드](#js-24-section-41)
- [39. 실행 결과 예시](#js-24-section-42)
- [40. 핵심 실행 흐름](#js-24-section-43)
- [41. 실무에서는 왜 이렇게 작성하는가?](#js-24-section-44)
- [42. 이 실습에 사용된 JavaScript 개념](#js-24-section-45)
- [43. 대표 오류와 해결](#js-24-section-46)
- [44. 개선 과제](#js-24-section-47)
- [45. 리팩토링 과제](#js-24-section-48)
- [46. 종합실습 체크리스트](#js-24-section-49)
- [47. 핵심 요약](#js-24-section-50)
- [마무리](#js-24-section-51)
- [V3 실행 추적 카드 — 요구사항 → 상태 모델 → 이벤트 → 렌더링 → 저장/통신](#js-24-section-52)

</details>

---

<a id="js-24-section-1"></a>

## 프로젝트 개요

사용자가 회원과 할 일을 관리할 수 있는 작은 대시보드를 만든다.

```text
회원 불러오기
    ↓
회원 선택
    ↓
할 일 입력
    ↓
상태 배열에 저장
    ↓
목록 렌더링
    ↓
검색·필터·정렬
    ↓
완료·삭제·전체 선택
    ↓
Local Storage 저장
```

외부 사용자 API를 불러오는 기능도 함께 구현한다.

```text
Load Button
    ↓
Fetch 요청
    ↓
HTTP 상태 확인
    ↓
JSON 변환
    ↓
회원 목록 상태 저장
    ↓
Select 렌더링
```

---

<a id="js-24-section-2"></a>

## 학습 목표

- 한 작업이 검증·상태·렌더링·저장으로 이어지는지 확인한다.
- 원본의 해당 부분을 찾아 실행 순서와 결과를 다시 확인한다.

---

<a id="js-24-section-3"></a>

## 개념에서 실제 실행까지: 종합실습은 상태를 기준으로 입력과 화면을 연결하는 프로젝트다

이 프로젝트는 원본 파일 그대로의 수업 완성본이 아니라 Todo 요구사항·DOM·JSON·통신을 연결한 💡 확장 실습이다. 완성 JavaScript를 복사하기 전에 기존 단계별 설명과 화면 구조를 따라 만들고, 한 작업씩 결과를 확인한다.

사용자가 할일 입력→submit→빈 값 검증→현재 회원 확인→객체 생성→state.todos에 추가→render→localStorage 저장으로 이어진다. state는 JavaScript 객체, render는 DOM 갱신, localStorage는 같은 origin에 남는 문자열 저장이다. 셋은 서로 자동으로 동기화되지 않는다.

직접 DOM 한 줄만 지워도 state에 남아 있으면 다음 render에서 다시 보일 수 있다. 반대로 state만 지우고 render를 안 하면 화면은 남는다. 저장 실패를 성공으로 표시하거나 다른 origin의 저장을 같은 데이터로 생각해서도 안 된다. 완료와 선택 체크박스의 의미가 혼합되지 않는지, 필터 뒤 전체선택 범위가 보이는 항목인지 전체인지 명시한다.

### 수업 원본에서 사용한 부분

아래는 전체 실행 파일이 아니라 **개념에 대응하는 문맥 발췌**다. 나머지 HTML·선언·등록 코드는 원본과 기존 번호형 본문에서 이어 확인한다. 이 문서의 개선·통합 예제는 💡 확장 학습이며 강사님 완성 코드로 표시하지 않는다.

내 코드: `workspace_html/javascript/asset/js/17_event_form.js`

```javascript
/*
        문제5_Todo List
        [할 일] [추가버튼] 
        + 문제5-1 : 추가버튼을 눌렀을 때 리스트 안에 추가되도록
        단, 앞에 체크박스가 같이 생기면서 체크하면 취소선 가도록
        위에 쌓이도록 진행

        + 문제 5-2 : 개별 삭제 버튼을 추가로 넣어서 삭제 버튼 눌렀을 때
```

강사님 코드: `workspace_teacher/workspace_html/javascript/asset/js/17_event_form.js`

```javascript
문제 5 : Todo List
    할일을 적는 input, 추가 버튼

    + 5-1 : 추가버튼 누르면 체크박스와 할일이 하단에 추가된다
    + 5-2 : 개별 삭제 버튼이 있고, 클릭 시 그 줄이 지워진다 (dom.remove())
    + 5-3 : 전체 선택 checkbox가 있고
            전체 선택 체크 시 : 모든 checkbox 체크
```

### 직접 재현하는 최소 예제와 결과

이 예제는 **이번 리팩토링의 설명용 재구성**이다. 원본 그대로의 발췌와 구별한다. 외부 통신 없이 Console에서 실행한다. 다른 예제의 변수와 섞이지 않게 새 실행 문맥에서 실행한다.

```javascript
let todos = [];
function addTodo(raw) {
  const title = raw.trim();
  if (!title) return false;
  todos.push({id: todos.length + 1, title, done: false});
  return true;
}
console.log(addTodo("  복습  "), addTodo("   "));
const saved = JSON.stringify(todos);
todos = JSON.parse(saved);
todos[0].done = true;
console.log(JSON.stringify(todos));
```

예상 출력:

```text
true false
[{"id":1,"title":"복습","done":true}]
```

### 결과를 역추적하는 방법

이 축소 예제의 ID 생성은 설명용이다. 실제 삭제 후 길이가 줄면 충돌할 수 있어 프로젝트의 UUID 등 고유 ID 정책을 따른다. 저장값 parse 성공뿐 아니라 객체 필드 형태도 검증한다. 기존 완성 코드와 요구사항·테스트 표를 연결해 읽는다.

출력은 아래의 확인 경로로 추적한다. return 값은 호출자에게 전달되고 자동으로 화면에 표시되지 않는다. Console 로그, DOM 변경, 저장소 변경, 서버 응답은 별개 단계다.

| 확인할 단계 | 이 예제에서 볼 것 |
| --- | --- |
| 입력 | 리터럴·현재 폼 값·이벤트 인수·응답 중 출처를 위 설명과 대조 |
| 실행 | 각 줄 또는 콜백이 지금 실행되는지, 나중에 실행되는지 구분 |
| 결과 | 위 예상 출력과 현재 값·자료형을 함께 대조 |
| 오류 | 첫 오류 줄의 입력과 직전 상태를 확인하고 뒤 로그 누락 원인 추적 |

### 단계별 복습 실습과 정답

**기본 실습:** Todo추가→완료→필터→삭제→새로고침을확인한다.

**응용·디버깅 실습:** 필터중전체선택이보이는항목만대상인지전체항목인지설계한다.

**통합 확인:** 위 최소 예제를 새 문맥에서 작성하고 정상값·빈 값·경계값으로 실행한다. 원본에서 대응하는 선언·호출·콜백을 찾아 위에 나타난 차이가 무엇을 바꾸는지 설명한다. 아래 정답은 먼저 예측한 뒤 펼친다. 이 실습은 💡 설명용 보강이며 원본에 모두 완성되어 있다는 뜻은 아니다.

<details>
<summary>정답과 처리 순서 해설</summary>

1. 각단계의state·DOM·저장문자열을따로확인한다. 삭제후저장과render가반영되고새로고침복원에도삭제상태가유지되어야한다.
2. 둘다가능하지만요구사항을명시한다. 적용대상배열과checked/indeterminate계산범위를같게해야한다.
3. 최소 예제의 예상 출력과 한 줄씩 대조한다. 값이 다른 경우 입력 → 형 변환 → 분기/상태 변경 → 출력 순서로 첫 차이를 찾는다. DOM·API 예제는 Console 값만 아니라 화면·Elements·Network가 서로 같은 상태를 말하는지도 점검한다.

</details>

### 복습 질문과 해설

**질문:** 선택된 항목 삭제 후 전체선택 체크가 남아 있으면 어디를 검사할까?

**해설:** 삭제 상태 변경→렌더링→전체선택 계산 호출 순서를 본다. 빈 배열.every와 indeterminate 초기화도 검사한다.

**한 번 더 확인:** 예제의 입력을 하나 바꾸고 결과를 먼저 예상한 뒤 실행한다. 정상 입력만 아니라 비어 있는 값, 경계값, 두 번 실행했을 때의 상태를 기존 실습·오류 절에서 반복 확인한다.

---

<a id="js-24-section-4"></a>

## 1. 요구사항

### 1-1. 회원 기능

- 외부 API에서 회원 목록을 불러온다.
- 회원 이름과 Email을 Select에 표시한다.
- 회원이 없으면 할 일을 추가할 수 없다.
- 회원 API 요청 중에는 Button을 비활성화한다.
- API 실패 시 오류 메시지를 표시한다.

### 1-2. 할 일 기능

- 회원을 선택하고 할 일을 입력한다.
- 빈 입력은 추가하지 않는다.
- 우선순위를 선택할 수 있다.
- 완료 여부를 변경할 수 있다.
- 개별 삭제가 가능하다.
- 여러 항목을 선택해 한 번에 삭제할 수 있다.
- 전체 선택과 일부 선택 상태를 표현한다.

### 1-3. 검색·필터·정렬

- 할 일 Text로 검색한다.
- 전체·진행 중·완료 상태로 필터링한다.
- 최신순·오래된순·우선순위순으로 정렬한다.

### 1-4. 저장

- 할 일 목록을 Local Storage에 저장한다.
- 새로고침 후에도 복원한다.
- 잘못된 저장 데이터가 있어도 Application이 중단되지 않는다.

---

<a id="js-24-section-5"></a>

## 2. 화면 구조

```html
<main class="dashboard">
    <section class="dashboard__users">
        <h1>회원·할 일 관리</h1>

        <button
            type="button"
            id="load-users"
        >
            회원 불러오기
        </button>

        <p
            id="user-status"
            role="status"
            aria-live="polite"
        ></p>
    </section>

    <section class="dashboard__form">
        <form id="todo-form">
            <label for="user-select">
                담당 회원
            </label>

            <select id="user-select">
                <option value="">
                    회원을 선택하세요
                </option>
            </select>

            <label for="todo-input">
                할 일
            </label>

            <input
                type="text"
                id="todo-input"
                autocomplete="off"
            >

            <label for="priority-select">
                우선순위
            </label>

            <select id="priority-select">
                <option value="high">
                    높음
                </option>

                <option
                    value="medium"
                    selected
                >
                    보통
                </option>

                <option value="low">
                    낮음
                </option>
            </select>

            <button type="submit">
                추가
            </button>
        </form>

        <p
            id="form-status"
            role="status"
            aria-live="polite"
        ></p>
    </section>

    <section class="dashboard__controls">
        <input
            type="search"
            id="search-input"
            placeholder="할 일 검색"
        >

        <select id="filter-select">
            <option value="all">
                전체
            </option>

            <option value="active">
                진행 중
            </option>

            <option value="done">
                완료
            </option>
        </select>

        <select id="sort-select">
            <option value="newest">
                최신순
            </option>

            <option value="oldest">
                오래된순
            </option>

            <option value="priority">
                우선순위순
            </option>
        </select>
    </section>

    <section class="dashboard__list">
        <label>
            <input
                type="checkbox"
                id="select-all"
            >
            전체 선택
        </label>

        <button
            type="button"
            id="delete-selected"
        >
            선택 삭제
        </button>

        <p id="todo-summary"></p>

        <ul id="todo-list"></ul>
    </section>
</main>
```

---

<a id="js-24-section-6"></a>

## 3. 상태 설계

```javascript
const state = {
    users: [],
    todos: [],
    searchKeyword: "",
    filter: "all",
    sort: "newest",
    isLoadingUsers: false,
}
```

### 3-1. 회원 객체

```text
{
    id: 1,
    name: "Kim",
    email: "kim@example.com"
}
```

### 3-2. 할 일 객체

```text
{
    id: "todo-1722920000000",
    userId: 1,
    text: "JavaScript 복습",
    priority: "high",
    done: false,
    selected: false,
    createdAt: 1722920000000
}
```

> [!IMPORTANT]
> 상태는 DOM Text에 저장하지 않는다.  
> JavaScript 객체와 배열에 저장하고, DOM은 `render()` 결과로 사용한다.

---

<a id="js-24-section-7"></a>

## 4. DOM 요소 선택

```javascript
function getRequiredElement(
    selector,
    root = document,
) {
    const element = (
        root.querySelector(
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

```javascript
const elements = {
    loadUsersButton: (
        getRequiredElement(
            "#load-users",
        )
    ),

    userStatus: (
        getRequiredElement(
            "#user-status",
        )
    ),

    todoForm: (
        getRequiredElement(
            "#todo-form",
        )
    ),

    userSelect: (
        getRequiredElement(
            "#user-select",
        )
    ),

    todoInput: (
        getRequiredElement(
            "#todo-input",
        )
    ),

    prioritySelect: (
        getRequiredElement(
            "#priority-select",
        )
    ),

    formStatus: (
        getRequiredElement(
            "#form-status",
        )
    ),

    searchInput: (
        getRequiredElement(
            "#search-input",
        )
    ),

    filterSelect: (
        getRequiredElement(
            "#filter-select",
        )
    ),

    sortSelect: (
        getRequiredElement(
            "#sort-select",
        )
    ),

    selectAll: (
        getRequiredElement(
            "#select-all",
        )
    ),

    deleteSelectedButton: (
        getRequiredElement(
            "#delete-selected",
        )
    ),

    todoSummary: (
        getRequiredElement(
            "#todo-summary",
        )
    ),

    todoList: (
        getRequiredElement(
            "#todo-list",
        )
    ),
}
```

---

<a id="js-24-section-8"></a>

## 5. Local Storage Key

```javascript
const TODO_STORAGE_KEY = (
    "javascript-dashboard-todos"
)
```

Magic String을 한곳에서 관리한다.

---

<a id="js-24-section-9"></a>

## 6. 안전한 JSON 저장

```javascript
function saveTodos() {
    localStorage.setItem(
        TODO_STORAGE_KEY,
        JSON.stringify(
            state.todos,
        ),
    )
}
```

---

<a id="js-24-section-10"></a>

## 7. 안전한 JSON 복원

```javascript
function loadTodos() {
    const stored = (
        localStorage.getItem(
            TODO_STORAGE_KEY,
        )
    )

    if (stored === null) {
        return []
    }

    try {
        const parsed = (
            JSON.parse(stored)
        )

        if (!Array.isArray(parsed)) {
            return []
        }

        return parsed.filter(
            isValidTodo,
        )
    } catch (
        error
    ) {
        console.error(
            "할 일 복원 실패",
            error,
        )

        return []
    }
}
```

---

<a id="js-24-section-11"></a>

## 8. 저장 데이터 검증

```javascript
function isValidTodo(
    todo,
) {
    return (
        todo !== null
        && typeof todo === "object"
        && typeof todo.id
            === "string"
        && Number.isInteger(
            todo.userId,
        )
        && typeof todo.text
            === "string"
        && [
            "high",
            "medium",
            "low",
        ].includes(
            todo.priority,
        )
        && typeof todo.done
            === "boolean"
        && typeof todo.selected
            === "boolean"
        && Number.isFinite(
            todo.createdAt,
        )
    )
}
```

JSON Parse 성공과 데이터 구조가 올바른 것은 별개다.

---

<a id="js-24-section-12"></a>

## 9. 회원 API 함수

```javascript
async function fetchUsers() {
    const response = await fetch(
        "https://jsonplaceholder.typicode.com/users",
    )

    if (!response.ok) {
        throw new Error(
            `HTTP ${response.status}`,
        )
    }

    const data = (
        await response.json()
    )

    if (!Array.isArray(data)) {
        throw new TypeError(
            "회원 목록 형식이 아닙니다.",
        )
    }

    return data.map(
        user => ({
            id: user.id,
            name: user.name,
            email: user.email,
        }),
    )
}
```

---

<a id="js-24-section-13"></a>

## 10. 회원 불러오기

```javascript
async function handleLoadUsers() {
    if (
        state.isLoadingUsers
    ) {
        return
    }

    state.isLoadingUsers = true

    elements
        .loadUsersButton
        .disabled = true

    elements.userStatus.textContent = (
        "회원정보를 불러오는 중입니다."
    )

    try {
        state.users = (
            await fetchUsers()
        )

        renderUserOptions()

        elements.userStatus.textContent = (
            `${state.users.length}명의 `
            + "회원을 불러왔습니다."
        )
    } catch (
        error
    ) {
        elements.userStatus.textContent = (
            "회원정보를 불러오지 "
            + "못했습니다."
        )

        console.error(error)
    } finally {
        state.isLoadingUsers = false

        elements
            .loadUsersButton
            .disabled = false
    }
}
```

---

<a id="js-24-section-14"></a>

## 11. 회원 Select 렌더링

```javascript
function renderUserOptions() {
    const fragment = (
        document
            .createDocumentFragment()
    )

    const placeholder = (
        document.createElement(
            "option",
        )
    )

    placeholder.value = ""
    placeholder.textContent = (
        "회원을 선택하세요"
    )

    fragment.append(placeholder)

    for (const user of state.users) {
        const option = (
            document.createElement(
                "option",
            )
        )

        option.value = String(
            user.id,
        )

        option.textContent = (
            `${user.name} `
            + `(${user.email})`
        )

        fragment.append(option)
    }

    elements.userSelect
        .replaceChildren(
            fragment,
        )
}
```

---

<a id="js-24-section-15"></a>

## 12. 할 일 ID 생성

```javascript
function createTodoId() {
    const randomPart = (
        typeof crypto.randomUUID
        === "function"
            ? crypto.randomUUID()
            : String(
                Math.random(),
            )
    )

    return (
        `todo-${Date.now()}-`
        + randomPart
    )
}
```

더 단순한 학습용 구현:

```javascript
function createTodoId() {
    return (
        `todo-${Date.now()}-`
        + `${Math.random()}`
    )
}
```

---

<a id="js-24-section-16"></a>

## 13. 할 일 Form 검증

```javascript
function getTodoFormData() {
    const userId = Number(
        elements.userSelect.value,
    )

    const text = (
        elements.todoInput
            .value
            .trim()
    )

    const priority = (
        elements
            .prioritySelect
            .value
    )

    if (
        !Number.isInteger(
            userId,
        )
    ) {
        throw new Error(
            "담당 회원을 선택해주세요.",
        )
    }

    if (text === "") {
        throw new Error(
            "할 일을 입력해주세요.",
        )
    }

    if (
        ![
            "high",
            "medium",
            "low",
        ].includes(priority)
    ) {
        throw new Error(
            "우선순위가 올바르지 않습니다.",
        )
    }

    return {
        userId,
        text,
        priority,
    }
}
```

---

<a id="js-24-section-17"></a>

## 14. 할 일 객체 생성

```javascript
function createTodo({
    userId,
    text,
    priority,
}) {
    return {
        id: createTodoId(),
        userId,
        text,
        priority,
        done: false,
        selected: false,
        createdAt: Date.now(),
    }
}
```

---

<a id="js-24-section-18"></a>

## 15. 할 일 추가

```javascript
function handleTodoSubmit(
    event,
) {
    event.preventDefault()

    try {
        const formData = (
            getTodoFormData()
        )

        const todo = createTodo(
            formData,
        )

        state.todos.unshift(todo)

        saveTodos()
        render()

        elements.todoInput.value = ""
        elements.formStatus.textContent = (
            "할 일을 추가했습니다."
        )

        elements.todoInput.focus()
    } catch (
        error
    ) {
        elements.formStatus.textContent = (
            error.message
        )
    }
}
```

---

<a id="js-24-section-19"></a>

## 16. 담당 회원 검색

```javascript
function findUser(
    userId,
) {
    return (
        state.users.find(
            user => (
                user.id === userId
            ),
        )
        ?? null
    )
}
```

회원 API를 새로 불러오기 전 Local Storage의 할 일이 존재할 수 있으므로 `null`을 처리한다.

---

<a id="js-24-section-20"></a>

## 17. 우선순위 Label

```javascript
const PRIORITY_LABELS = {
    high: "높음",
    medium: "보통",
    low: "낮음",
}
```

---

<a id="js-24-section-21"></a>

## 18. 할 일 Item 생성

```javascript
function createTodoItem(
    todo,
) {
    const item = (
        document.createElement(
            "li",
        )
    )

    item.classList.add(
        "todo-item",
    )

    item.classList.toggle(
        "todo-item--done",
        todo.done,
    )

    item.dataset.todoId = todo.id

    const select = (
        document.createElement(
            "input",
        )
    )

    select.type = "checkbox"
    select.classList.add(
        "todo-item__select",
    )

    select.checked = todo.selected
    select.setAttribute(
        "aria-label",
        `${todo.text} 선택`,
    )

    const done = (
        document.createElement(
            "input",
        )
    )

    done.type = "checkbox"
    done.classList.add(
        "todo-item__done",
    )

    done.checked = todo.done
    done.setAttribute(
        "aria-label",
        `${todo.text} 완료`,
    )

    const text = (
        document.createElement(
            "span",
        )
    )

    text.classList.add(
        "todo-item__text",
    )

    text.textContent = todo.text

    const user = findUser(
        todo.userId,
    )

    const owner = (
        document.createElement(
            "span",
        )
    )

    owner.classList.add(
        "todo-item__owner",
    )

    owner.textContent = (
        user?.name
        ?? `회원 #${todo.userId}`
    )

    const priority = (
        document.createElement(
            "span",
        )
    )

    priority.classList.add(
        "todo-item__priority",
        `todo-item__priority--${todo.priority}`,
    )

    priority.textContent = (
        PRIORITY_LABELS[
            todo.priority
        ]
    )

    const remove = (
        document.createElement(
            "button",
        )
    )

    remove.type = "button"
    remove.classList.add(
        "todo-item__remove",
    )

    remove.textContent = "삭제"

    item.append(
        select,
        done,
        text,
        owner,
        priority,
        remove,
    )

    return item
}
```

---

<a id="js-24-section-22"></a>

## 19. 검색 결과 계산

```javascript
function matchesSearch(
    todo,
) {
    const keyword = (
        state.searchKeyword
            .toLowerCase()
    )

    return (
        todo.text
            .toLowerCase()
            .includes(keyword)
    )
}
```

---

<a id="js-24-section-23"></a>

## 20. 상태 필터

```javascript
function matchesFilter(
    todo,
) {
    if (
        state.filter === "active"
    ) {
        return !todo.done
    }

    if (
        state.filter === "done"
    ) {
        return todo.done
    }

    return true
}
```

---

<a id="js-24-section-24"></a>

## 21. 우선순위 점수

```javascript
const PRIORITY_SCORE = {
    high: 3,
    medium: 2,
    low: 1,
}
```

---

<a id="js-24-section-25"></a>

## 22. 정렬 함수

```javascript
function sortTodos(
    todos,
) {
    const copied = [
        ...todos,
    ]

    if (
        state.sort === "oldest"
    ) {
        return copied.sort(
            (
                first,
                second,
            ) => (
                first.createdAt
                - second.createdAt
            ),
        )
    }

    if (
        state.sort === "priority"
    ) {
        return copied.sort(
            (
                first,
                second,
            ) => (
                PRIORITY_SCORE[
                    second.priority
                ]
                - PRIORITY_SCORE[
                    first.priority
                ]
                || second.createdAt
                - first.createdAt
            ),
        )
    }

    return copied.sort(
        (
            first,
            second,
        ) => (
            second.createdAt
            - first.createdAt
        ),
    )
}
```

원본 배열을 직접 정렬하지 않고 복사본을 정렬한다.

---

<a id="js-24-section-26"></a>

## 23. 화면에 표시할 할 일 계산

```javascript
function getVisibleTodos() {
    const filtered = (
        state.todos.filter(
            todo => (
                matchesSearch(todo)
                && matchesFilter(todo)
            ),
        )
    )

    return sortTodos(filtered)
}
```

---

<a id="js-24-section-27"></a>

## 24. 목록 렌더링

```javascript
function renderTodoList() {
    const visibleTodos = (
        getVisibleTodos()
    )

    const fragment = (
        document
            .createDocumentFragment()
    )

    for (
        const todo
        of visibleTodos
    ) {
        fragment.append(
            createTodoItem(todo),
        )
    }

    elements.todoList
        .replaceChildren(
            fragment,
        )

    if (
        visibleTodos.length === 0
    ) {
        const emptyItem = (
            document.createElement(
                "li",
            )
        )

        emptyItem.classList.add(
            "todo-list__empty",
        )

        emptyItem.textContent = (
            "표시할 할 일이 없습니다."
        )

        elements.todoList.append(
            emptyItem,
        )
    }
}
```

---

<a id="js-24-section-28"></a>

## 25. 요약 정보 렌더링

```javascript
function renderSummary() {
    const totalCount = (
        state.todos.length
    )

    const doneCount = (
        state.todos.filter(
            todo => todo.done,
        ).length
    )

    const selectedCount = (
        state.todos.filter(
            todo => todo.selected,
        ).length
    )

    elements.todoSummary.textContent = (
        `전체 ${totalCount}개 · `
        + `완료 ${doneCount}개 · `
        + `선택 ${selectedCount}개`
    )
}
```

---

<a id="js-24-section-29"></a>

## 26. 전체 선택 상태 계산

```javascript
function renderSelectAll() {
    const todos = state.todos

    const selectedCount = (
        todos.filter(
            todo => todo.selected,
        ).length
    )

    elements.selectAll.checked = (
        todos.length > 0
        && selectedCount
        === todos.length
    )

    elements.selectAll.indeterminate = (
        selectedCount > 0
        && selectedCount
        < todos.length
    )

    elements
        .deleteSelectedButton
        .disabled = (
            selectedCount === 0
        )
}
```

---

<a id="js-24-section-30"></a>

## 27. 전체 렌더링

```javascript
function render() {
    renderTodoList()
    renderSummary()
    renderSelectAll()
}
```

상태 변경 후 필요한 화면 갱신을 한곳에서 실행한다.

---

<a id="js-24-section-31"></a>

## 28. 할 일 찾기

```javascript
function findTodoById(
    todoId,
) {
    return (
        state.todos.find(
            todo => (
                todo.id === todoId
            ),
        )
        ?? null
    )
}
```

---

<a id="js-24-section-32"></a>

## 29. 목록 Event Delegation

```javascript
function handleTodoListChange(
    event,
) {
    const item = (
        event.target.closest(
            ".todo-item",
        )
    )

    if (
        item === null
        || !elements.todoList
            .contains(item)
    ) {
        return
    }

    const todo = findTodoById(
        item.dataset.todoId,
    )

    if (todo === null) {
        return
    }

    if (
        event.target.matches(
            ".todo-item__select",
        )
    ) {
        todo.selected = (
            event.target.checked
        )
    }

    if (
        event.target.matches(
            ".todo-item__done",
        )
    ) {
        todo.done = (
            event.target.checked
        )
    }

    saveTodos()
    render()
}
```

---

<a id="js-24-section-33"></a>

## 30. 개별 삭제 Event Delegation

```javascript
function handleTodoListClick(
    event,
) {
    const removeButton = (
        event.target.closest(
            ".todo-item__remove",
        )
    )

    if (
        removeButton === null
    ) {
        return
    }

    const item = (
        removeButton.closest(
            ".todo-item",
        )
    )

    if (item === null) {
        return
    }

    state.todos = (
        state.todos.filter(
            todo => (
                todo.id
                !== item.dataset.todoId
            ),
        )
    )

    saveTodos()
    render()
}
```

---

<a id="js-24-section-34"></a>

## 31. 검색 입력

```javascript
function handleSearchInput() {
    state.searchKeyword = (
        elements.searchInput
            .value
            .trim()
    )

    renderTodoList()
}
```

Search는 저장할 상태가 아니므로 Local Storage에 저장하지 않는다.

---

<a id="js-24-section-35"></a>

## 32. 필터 변경

```javascript
function handleFilterChange() {
    state.filter = (
        elements
            .filterSelect
            .value
    )

    renderTodoList()
}
```

---

<a id="js-24-section-36"></a>

## 33. 정렬 변경

```javascript
function handleSortChange() {
    state.sort = (
        elements
            .sortSelect
            .value
    )

    renderTodoList()
}
```

---

<a id="js-24-section-37"></a>

## 34. 전체 선택 변경

```javascript
function handleSelectAllChange() {
    for (const todo of state.todos) {
        todo.selected = (
            elements
                .selectAll
                .checked
        )
    }

    saveTodos()
    render()
}
```

---

<a id="js-24-section-38"></a>

## 35. 선택 삭제

```javascript
function handleDeleteSelected() {
    const hasSelected = (
        state.todos.some(
            todo => todo.selected,
        )
    )

    if (!hasSelected) {
        return
    }

    state.todos = (
        state.todos.filter(
            todo => !todo.selected,
        )
    )

    saveTodos()
    render()
}
```

---

<a id="js-24-section-39"></a>

## 36. 이벤트 등록

```javascript
function bindEvents() {
    elements
        .loadUsersButton
        .addEventListener(
            "click",
            handleLoadUsers,
        )

    elements.todoForm
        .addEventListener(
            "submit",
            handleTodoSubmit,
        )

    elements.todoList
        .addEventListener(
            "change",
            handleTodoListChange,
        )

    elements.todoList
        .addEventListener(
            "click",
            handleTodoListClick,
        )

    elements.searchInput
        .addEventListener(
            "input",
            handleSearchInput,
        )

    elements.filterSelect
        .addEventListener(
            "change",
            handleFilterChange,
        )

    elements.sortSelect
        .addEventListener(
            "change",
            handleSortChange,
        )

    elements.selectAll
        .addEventListener(
            "change",
            handleSelectAllChange,
        )

    elements
        .deleteSelectedButton
        .addEventListener(
            "click",
            handleDeleteSelected,
        )
}
```

---

<a id="js-24-section-40"></a>

## 37. 초기화

```javascript
function init() {
    state.todos = loadTodos()

    bindEvents()
    render()
}

init()
```

---

<a id="js-24-section-41"></a>

## 38. 완성 JavaScript 코드

```javascript
const TODO_STORAGE_KEY = (
    "javascript-dashboard-todos"
)

const PRIORITY_LABELS = {
    high: "높음",
    medium: "보통",
    low: "낮음",
}

const PRIORITY_SCORE = {
    high: 3,
    medium: 2,
    low: 1,
}

const state = {
    users: [],
    todos: [],
    searchKeyword: "",
    filter: "all",
    sort: "newest",
    isLoadingUsers: false,
}

function getRequiredElement(
    selector,
    root = document,
) {
    const element = (
        root.querySelector(
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

const elements = {
    loadUsersButton: (
        getRequiredElement(
            "#load-users",
        )
    ),

    userStatus: (
        getRequiredElement(
            "#user-status",
        )
    ),

    todoForm: (
        getRequiredElement(
            "#todo-form",
        )
    ),

    userSelect: (
        getRequiredElement(
            "#user-select",
        )
    ),

    todoInput: (
        getRequiredElement(
            "#todo-input",
        )
    ),

    prioritySelect: (
        getRequiredElement(
            "#priority-select",
        )
    ),

    formStatus: (
        getRequiredElement(
            "#form-status",
        )
    ),

    searchInput: (
        getRequiredElement(
            "#search-input",
        )
    ),

    filterSelect: (
        getRequiredElement(
            "#filter-select",
        )
    ),

    sortSelect: (
        getRequiredElement(
            "#sort-select",
        )
    ),

    selectAll: (
        getRequiredElement(
            "#select-all",
        )
    ),

    deleteSelectedButton: (
        getRequiredElement(
            "#delete-selected",
        )
    ),

    todoSummary: (
        getRequiredElement(
            "#todo-summary",
        )
    ),

    todoList: (
        getRequiredElement(
            "#todo-list",
        )
    ),
}

function isValidTodo(
    todo,
) {
    return (
        todo !== null
        && typeof todo === "object"
        && typeof todo.id
            === "string"
        && Number.isInteger(
            todo.userId,
        )
        && typeof todo.text
            === "string"
        && [
            "high",
            "medium",
            "low",
        ].includes(
            todo.priority,
        )
        && typeof todo.done
            === "boolean"
        && typeof todo.selected
            === "boolean"
        && Number.isFinite(
            todo.createdAt,
        )
    )
}

function saveTodos() {
    localStorage.setItem(
        TODO_STORAGE_KEY,
        JSON.stringify(
            state.todos,
        ),
    )
}

function loadTodos() {
    const stored = (
        localStorage.getItem(
            TODO_STORAGE_KEY,
        )
    )

    if (stored === null) {
        return []
    }

    try {
        const parsed = (
            JSON.parse(stored)
        )

        if (!Array.isArray(parsed)) {
            return []
        }

        return parsed.filter(
            isValidTodo,
        )
    } catch (
        error
    ) {
        console.error(
            "할 일 복원 실패",
            error,
        )

        return []
    }
}

async function fetchUsers() {
    const response = await fetch(
        "https://jsonplaceholder.typicode.com/users",
    )

    if (!response.ok) {
        throw new Error(
            `HTTP ${response.status}`,
        )
    }

    const data = (
        await response.json()
    )

    if (!Array.isArray(data)) {
        throw new TypeError(
            "회원 목록 형식이 아닙니다.",
        )
    }

    return data.map(
        user => ({
            id: user.id,
            name: user.name,
            email: user.email,
        }),
    )
}

async function handleLoadUsers() {
    if (
        state.isLoadingUsers
    ) {
        return
    }

    state.isLoadingUsers = true
    elements.loadUsersButton.disabled = true
    elements.userStatus.textContent = (
        "회원정보를 불러오는 중입니다."
    )

    try {
        state.users = (
            await fetchUsers()
        )

        renderUserOptions()

        elements.userStatus.textContent = (
            `${state.users.length}명의 `
            + "회원을 불러왔습니다."
        )

        render()
    } catch (
        error
    ) {
        elements.userStatus.textContent = (
            "회원정보를 불러오지 "
            + "못했습니다."
        )

        console.error(error)
    } finally {
        state.isLoadingUsers = false
        elements.loadUsersButton.disabled = false
    }
}

function renderUserOptions() {
    const fragment = (
        document
            .createDocumentFragment()
    )

    const placeholder = (
        document.createElement(
            "option",
        )
    )

    placeholder.value = ""
    placeholder.textContent = (
        "회원을 선택하세요"
    )

    fragment.append(placeholder)

    for (const user of state.users) {
        const option = (
            document.createElement(
                "option",
            )
        )

        option.value = String(
            user.id,
        )

        option.textContent = (
            `${user.name} `
            + `(${user.email})`
        )

        fragment.append(option)
    }

    elements.userSelect
        .replaceChildren(
            fragment,
        )
}

function createTodoId() {
    return (
        `todo-${Date.now()}-`
        + `${Math.random()}`
    )
}

function getTodoFormData() {
    const userId = Number(
        elements.userSelect.value,
    )

    const text = (
        elements.todoInput
            .value
            .trim()
    )

    const priority = (
        elements
            .prioritySelect
            .value
    )

    if (
        !Number.isInteger(
            userId,
        )
    ) {
        throw new Error(
            "담당 회원을 선택해주세요.",
        )
    }

    if (text === "") {
        throw new Error(
            "할 일을 입력해주세요.",
        )
    }

    if (
        ![
            "high",
            "medium",
            "low",
        ].includes(priority)
    ) {
        throw new Error(
            "우선순위가 올바르지 않습니다.",
        )
    }

    return {
        userId,
        text,
        priority,
    }
}

function createTodo({
    userId,
    text,
    priority,
}) {
    return {
        id: createTodoId(),
        userId,
        text,
        priority,
        done: false,
        selected: false,
        createdAt: Date.now(),
    }
}

function handleTodoSubmit(
    event,
) {
    event.preventDefault()

    try {
        const formData = (
            getTodoFormData()
        )

        state.todos.unshift(
            createTodo(
                formData,
            ),
        )

        saveTodos()
        render()

        elements.todoInput.value = ""
        elements.formStatus.textContent = (
            "할 일을 추가했습니다."
        )

        elements.todoInput.focus()
    } catch (
        error
    ) {
        elements.formStatus.textContent = (
            error.message
        )
    }
}

function findUser(
    userId,
) {
    return (
        state.users.find(
            user => (
                user.id === userId
            ),
        )
        ?? null
    )
}

function createTodoItem(
    todo,
) {
    const item = (
        document.createElement(
            "li",
        )
    )

    item.classList.add(
        "todo-item",
    )

    item.classList.toggle(
        "todo-item--done",
        todo.done,
    )

    item.dataset.todoId = todo.id

    const select = (
        document.createElement(
            "input",
        )
    )

    select.type = "checkbox"
    select.classList.add(
        "todo-item__select",
    )

    select.checked = todo.selected

    const done = (
        document.createElement(
            "input",
        )
    )

    done.type = "checkbox"
    done.classList.add(
        "todo-item__done",
    )

    done.checked = todo.done

    const text = (
        document.createElement(
            "span",
        )
    )

    text.classList.add(
        "todo-item__text",
    )

    text.textContent = todo.text

    const owner = (
        document.createElement(
            "span",
        )
    )

    owner.classList.add(
        "todo-item__owner",
    )

    owner.textContent = (
        findUser(todo.userId)
            ?.name
        ?? `회원 #${todo.userId}`
    )

    const priority = (
        document.createElement(
            "span",
        )
    )

    priority.classList.add(
        "todo-item__priority",
        `todo-item__priority--${todo.priority}`,
    )

    priority.textContent = (
        PRIORITY_LABELS[
            todo.priority
        ]
    )

    const remove = (
        document.createElement(
            "button",
        )
    )

    remove.type = "button"
    remove.classList.add(
        "todo-item__remove",
    )

    remove.textContent = "삭제"

    item.append(
        select,
        done,
        text,
        owner,
        priority,
        remove,
    )

    return item
}

function matchesSearch(
    todo,
) {
    return (
        todo.text
            .toLowerCase()
            .includes(
                state.searchKeyword
                    .toLowerCase(),
            )
    )
}

function matchesFilter(
    todo,
) {
    if (
        state.filter === "active"
    ) {
        return !todo.done
    }

    if (
        state.filter === "done"
    ) {
        return todo.done
    }

    return true
}

function sortTodos(
    todos,
) {
    const copied = [
        ...todos,
    ]

    if (
        state.sort === "oldest"
    ) {
        return copied.sort(
            (
                first,
                second,
            ) => (
                first.createdAt
                - second.createdAt
            ),
        )
    }

    if (
        state.sort === "priority"
    ) {
        return copied.sort(
            (
                first,
                second,
            ) => (
                PRIORITY_SCORE[
                    second.priority
                ]
                - PRIORITY_SCORE[
                    first.priority
                ]
                || second.createdAt
                - first.createdAt
            ),
        )
    }

    return copied.sort(
        (
            first,
            second,
        ) => (
            second.createdAt
            - first.createdAt
        ),
    )
}

function getVisibleTodos() {
    return sortTodos(
        state.todos.filter(
            todo => (
                matchesSearch(todo)
                && matchesFilter(todo)
            ),
        ),
    )
}

function renderTodoList() {
    const visibleTodos = (
        getVisibleTodos()
    )

    const fragment = (
        document
            .createDocumentFragment()
    )

    for (
        const todo
        of visibleTodos
    ) {
        fragment.append(
            createTodoItem(todo),
        )
    }

    elements.todoList
        .replaceChildren(
            fragment,
        )

    if (
        visibleTodos.length === 0
    ) {
        const emptyItem = (
            document.createElement(
                "li",
            )
        )

        emptyItem.classList.add(
            "todo-list__empty",
        )

        emptyItem.textContent = (
            "표시할 할 일이 없습니다."
        )

        elements.todoList.append(
            emptyItem,
        )
    }
}

function renderSummary() {
    const totalCount = (
        state.todos.length
    )

    const doneCount = (
        state.todos.filter(
            todo => todo.done,
        ).length
    )

    const selectedCount = (
        state.todos.filter(
            todo => todo.selected,
        ).length
    )

    elements.todoSummary.textContent = (
        `전체 ${totalCount}개 · `
        + `완료 ${doneCount}개 · `
        + `선택 ${selectedCount}개`
    )
}

function renderSelectAll() {
    const selectedCount = (
        state.todos.filter(
            todo => todo.selected,
        ).length
    )

    elements.selectAll.checked = (
        state.todos.length > 0
        && selectedCount
        === state.todos.length
    )

    elements.selectAll.indeterminate = (
        selectedCount > 0
        && selectedCount
        < state.todos.length
    )

    elements
        .deleteSelectedButton
        .disabled = (
            selectedCount === 0
        )
}

function render() {
    renderTodoList()
    renderSummary()
    renderSelectAll()
}

function findTodoById(
    todoId,
) {
    return (
        state.todos.find(
            todo => (
                todo.id === todoId
            ),
        )
        ?? null
    )
}

function handleTodoListChange(
    event,
) {
    const item = (
        event.target.closest(
            ".todo-item",
        )
    )

    if (
        item === null
        || !elements.todoList
            .contains(item)
    ) {
        return
    }

    const todo = findTodoById(
        item.dataset.todoId,
    )

    if (todo === null) {
        return
    }

    if (
        event.target.matches(
            ".todo-item__select",
        )
    ) {
        todo.selected = (
            event.target.checked
        )
    }

    if (
        event.target.matches(
            ".todo-item__done",
        )
    ) {
        todo.done = (
            event.target.checked
        )
    }

    saveTodos()
    render()
}

function handleTodoListClick(
    event,
) {
    const removeButton = (
        event.target.closest(
            ".todo-item__remove",
        )
    )

    if (
        removeButton === null
    ) {
        return
    }

    const item = (
        removeButton.closest(
            ".todo-item",
        )
    )

    if (item === null) {
        return
    }

    state.todos = (
        state.todos.filter(
            todo => (
                todo.id
                !== item.dataset.todoId
            ),
        )
    )

    saveTodos()
    render()
}

function handleSearchInput() {
    state.searchKeyword = (
        elements.searchInput
            .value
            .trim()
    )

    renderTodoList()
}

function handleFilterChange() {
    state.filter = (
        elements
            .filterSelect
            .value
    )

    renderTodoList()
}

function handleSortChange() {
    state.sort = (
        elements
            .sortSelect
            .value
    )

    renderTodoList()
}

function handleSelectAllChange() {
    for (const todo of state.todos) {
        todo.selected = (
            elements
                .selectAll
                .checked
        )
    }

    saveTodos()
    render()
}

function handleDeleteSelected() {
    if (
        !state.todos.some(
            todo => todo.selected,
        )
    ) {
        return
    }

    state.todos = (
        state.todos.filter(
            todo => !todo.selected,
        )
    )

    saveTodos()
    render()
}

function bindEvents() {
    elements
        .loadUsersButton
        .addEventListener(
            "click",
            handleLoadUsers,
        )

    elements.todoForm
        .addEventListener(
            "submit",
            handleTodoSubmit,
        )

    elements.todoList
        .addEventListener(
            "change",
            handleTodoListChange,
        )

    elements.todoList
        .addEventListener(
            "click",
            handleTodoListClick,
        )

    elements.searchInput
        .addEventListener(
            "input",
            handleSearchInput,
        )

    elements.filterSelect
        .addEventListener(
            "change",
            handleFilterChange,
        )

    elements.sortSelect
        .addEventListener(
            "change",
            handleSortChange,
        )

    elements.selectAll
        .addEventListener(
            "change",
            handleSelectAllChange,
        )

    elements
        .deleteSelectedButton
        .addEventListener(
            "click",
            handleDeleteSelected,
        )
}

function init() {
    state.todos = loadTodos()

    bindEvents()
    render()
}

init()
```

---

<a id="js-24-section-42"></a>

## 39. 실행 결과 예시

회원 불러오기 성공:

```text
10명의 회원을 불러왔습니다.
```

할 일 추가:

```text
회원: Leanne Graham
할 일: JavaScript 종합실습 검수
우선순위: 높음
상태: 진행 중
```

요약:

```text
전체 3개 · 완료 1개 · 선택 2개
```

검색 결과가 없을 때:

```text
표시할 할 일이 없습니다.
```

회원 API 실패:

```text
회원정보를 불러오지 못했습니다.
```

---

<a id="js-24-section-43"></a>

## 40. 핵심 실행 흐름

```text
초기화
→ Local Storage 복원
→ Event Listener 등록
→ 최초 렌더링
```

```text
Form Submit
→ 입력 검증
→ Todo 객체 생성
→ 상태 배열 변경
→ Storage 저장
→ 전체 렌더링
```

```text
동적 Checkbox·삭제 Button
→ List 부모 Listener
→ closest()로 Todo Item 탐색
→ data-todo-id로 상태 찾기
→ 상태 변경
→ 다시 렌더링
```

---

<a id="js-24-section-44"></a>

## 41. 실무에서는 왜 이렇게 작성하는가?

### 41-1. 상태 중심 설계

DOM을 직접 여러 위치에서 수정하지 않고 `state.todos`를 기준으로 화면을 다시 만든다.

```text
상태
→ 진짜 데이터

DOM
→ 현재 상태의 표현
```

### 41-2. 계산과 렌더링 분리

- `getVisibleTodos()` → 검색·필터·정렬 계산
- `renderTodoList()` → DOM 출력
- `saveTodos()` → 저장
- `fetchUsers()` → Network 요청

각 함수의 역할이 분명하다.

<a id="index-section-60"></a>

### 41-3. Event Delegation

Todo가 나중에 추가되어도 부모 Listener가 이미 등록되어 있으므로 자동으로 동작한다.

### 41-4. 안전한 출력

사용자 입력과 API 응답을 `textContent`로 출력해 HTML 실행을 막는다.

### 41-5. 실패 상태 처리

정상 결과뿐 아니라 다음 상태를 모두 처리한다.

```text
Loading
Empty
Error
Success
```

---

<a id="js-24-section-45"></a>

## 42. 이 실습에 사용된 JavaScript 개념

| 학습 범위 | 적용 위치 |
| --- | --- |
| 변수·자료형 | 상태, 상수, Form 값 |
| 조건문 | 검증, 필터, 오류 처리 |
| 반복문 | Option·Todo 렌더링 |
| 배열 | 회원·할 일 상태 |
| 배열 메서드 | `map`, `filter`, `find`, `some` |
| 객체 | User·Todo·State |
| 함수 | 검증·계산·렌더링·이벤트 분리 |
| Date | `createdAt` |
| DOM | 요소 생성·삽입·교체 |
| Form | Submit·Input·Select |
| 이벤트 | Click·Change·Input·Submit |
| 이벤트 전파 | Event Delegation |
| JSON | Storage 직렬화·역직렬화 |
| Fetch | 사용자 API 요청 |
| Promise | 비동기 응답 |
| `async/await` | 회원 조회 |
| 오류 처리 | `try...catch...finally` |
| 코딩 스타일 | 네이밍·Guard Clause·단일 책임 |

---

<a id="js-24-section-46"></a>

## 43. 대표 오류와 해결

### 43-1. 회원을 불러오기 전에 기존 Todo의 이름이 안 보임

Local Storage에는 `userId`만 저장되어 있고 회원 목록은 아직 비어 있다.

처리:

```text
회원 #1
```

처럼 임시 표시하고 회원을 불러온 뒤 다시 렌더링한다.

### 43-2. 빈 문자열이 추가됨

`trim()` 후 빈 값 검사로 방지한다.

### 43-3. 정렬할 때 원본 배열 순서가 바뀜

복사본을 만든 뒤 `sort()`한다.

```javascript
const copied = [
    ...todos,
]
```

### 43-4. 동적 삭제 Button이 동작하지 않음

각 Button에 Listener를 붙이지 말고 부모 목록에 Event Delegation을 적용한다.

<a id="index-section-69"></a>

### 43-5. 저장 데이터가 깨져 Application 중단

`try...catch`와 자료형 검증 후 Fallback `[]`을 사용한다.

---

<a id="js-24-section-47"></a>

## 44. 개선 과제

기본 실습을 완료한 뒤 다음 기능을 추가해볼 수 있다.

- Todo 수정
- 마감일 설정
- 회원별 필터
- 페이지네이션
- Drag and Drop 정렬
- API 저장 연동
- Undo 삭제
- Toast 메시지
- Theme 저장
- AbortController 기반 회원 요청 취소
- TypeScript 적용
- Unit Test 작성

---

<a id="js-24-section-48"></a>

## 45. 리팩토링 과제

다음 파일 구조로 분리해본다.

```text
src/
├── api/
│   └── users-api.js
├── domain/
│   ├── todo.js
│   └── todo-filter.js
├── storage/
│   └── todo-storage.js
├── ui/
│   ├── todo-item.js
│   └── todo-dashboard.js
└── main.js
```

---

<a id="js-24-section-49"></a>

## 46. 종합실습 체크리스트

- [ ] 상태를 객체와 배열로 설계했는가?
- [ ] DOM을 상태 저장소로 사용하지 않는가?
- [ ] Form Submit으로 입력을 처리하는가?
- [ ] 회원 선택과 할 일 Text를 검증하는가?
- [ ] 우선순위를 허용값으로 검증하는가?
- [ ] Todo 객체 생성 함수를 분리했는가?
- [ ] 사용자 API에서 `response.ok`를 검사하는가?
- [ ] 응답이 배열인지 확인하는가?
- [ ] Loading 상태에서 Button을 비활성화하는가?
- [ ] 성공·실패 메시지를 화면에 표시하는가?
- [ ] 회원 Select를 Node 생성 방식으로 렌더링하는가?
- [ ] Todo Text에 `textContent`를 사용하는가?
- [ ] 반복 렌더링에서 `innerHTML +=`를 사용하지 않는가?
- [ ] 검색·필터·정렬 계산을 함수로 분리했는가?
- [ ] 원본 배열을 직접 `sort()`하지 않는가?
- [ ] Event Delegation을 적용했는가?
- [ ] `closest()`와 `dataset`으로 Todo를 찾는가?
- [ ] 개별 선택과 전체 선택을 동기화했는가?
- [ ] 일부 선택에 `indeterminate`를 사용하는가?
- [ ] 선택 항목이 없을 때 삭제 Button을 비활성화하는가?
- [ ] Local Storage에 JSON 문자열로 저장하는가?
- [ ] Parse 오류에 Fallback을 제공하는가?
- [ ] 저장 데이터 구조를 검증하는가?
- [ ] 상태 변경 후 저장과 렌더링 순서를 일관되게 유지하는가?
- [ ] 함수 이름만으로 역할을 알 수 있는가?
- [ ] Network·Storage·DOM 책임이 분리되어 있는가?

---

<a id="js-24-section-50"></a>

## 47. 핵심 요약

```text
입력
→ 검증
→ 객체 생성
→ 상태 배열 변경
→ 저장
→ 렌더링
```

```text
검색·필터·정렬
→ 원본 상태를 변경하지 않고
→ 표시할 배열 계산
```

```text
동적 DOM
→ 부모 Event Delegation

외부 문자열
→ textContent
```

```text
Fetch
→ response.ok
→ JSON 구조 검증
→ Loading·Error 처리
```

```text
Local Storage
→ stringify
→ safe parse
→ Fallback
```

---

<a id="js-24-section-51"></a>

## 마무리

JavaScript 종합실습의 핵심은 기능을 많이 넣는 것이 아니다.

```text
업무 요구사항을 상태와 함수로 나누고
    ↓
사용자 입력과 외부 데이터를 검증하고
    ↓
상태를 기준으로 화면을 일관되게 렌더링하고
    ↓
동적 요소와 비동기 요청을 안전하게 관리하고
    ↓
실패 후에도 다시 사용할 수 있는 흐름을 만드는 것
```

이 프로젝트를 이해하고 직접 수정할 수 있다면 JavaScript 기초 문법을 넘어, 작은 실무형 Frontend 기능을 구조적으로 구현할 수 있다.
<a id="js-24-section-52"></a>

## V3 실행 추적 카드 — 요구사항 → 상태 모델 → 이벤트 → 렌더링 → 저장/통신

실습은 정상 화면만 보지 않고 초기 상태, 사용자 행동, 상태 변화, DOM 반영, 네트워크, 실패 복구를 시간 순서로 기록한다.

정상값·빈 값·경계값·중복 동작을 테스트하고 Console 오류 없음, Elements 상태, Network 요청을 함께 캡처한다. 완성 예시는 암기보다 요구사항을 바꿔 재작성한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/01~22 전체 원본을 결합한 종합 확장`에서 실제 사용 위치와 차이를 확인한다.
