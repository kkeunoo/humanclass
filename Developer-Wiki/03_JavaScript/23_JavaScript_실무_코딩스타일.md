---
title: JavaScript 실무 코딩 스타일
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# JavaScript 실무 코딩 스타일

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `23_JavaScript_실무_코딩스타일.md` |
| 분류 | `03_JavaScript` |
| 문서 성격 | JavaScript 실무 예제 및 리팩토링 기준 문서 |
| 핵심 범위 | 네이밍, `const`·`let`, 조건문, 함수 분리, 배열·객체, DOM, 이벤트, 비동기, API, 저장소, 보안, 모듈화 |
| 예제 형식 | Before → After → 실행 결과 → 개선 이유 → 실무 선택 기준 |
| 종합실습 | 별도 문서 `24_JavaScript_종합실습.md`에서 관리 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 이 문서는 새로운 문법을 배우는 문서가 아니다.  
> JavaScript 01~22번에서 학습한 문법과 Browser API를 **실무에서는 왜, 어떻게 선택하고 조합하는지** 설명하는 기준 문서다.

---

# 개요

실행되는 코드가 반드시 유지보수하기 좋은 코드는 아니다.

다음 두 코드는 같은 결과를 출력한다.

```javascript
for (
    let index = 0;
    index < users.length;
    index += 1
) {
    console.log(
        users[index].name,
    )
}
```

```javascript
for (const user of users) {
    console.log(user.name)
}
```

첫 번째 코드는 Index가 필요하지 않은데도 Index를 만들고 다시 배열을 조회한다.

```text
첫 번째 코드
→ Index 생성
→ 배열 재조회
→ 실제 목적은 사용자 이름 출력

두 번째 코드
→ 사용자 객체 직접 순회
→ 목적이 바로 보임
```

실무 코드는 다음 질문을 계속 확인한다.

```text
이름만 보고 역할을 알 수 있는가?
    ↓
상태와 화면이 분리되어 있는가?
    ↓
함수 하나의 책임이 분명한가?
    ↓
잘못된 입력과 실패 상태를 처리하는가?
    ↓
동적으로 추가된 요소도 안전하게 동작하는가?
    ↓
민감정보와 외부 데이터를 안전하게 다루는가?
```

> [!IMPORTANT]
> 실무 코딩 스타일의 목적은 코드를 무조건 짧게 만드는 것이 아니다.
>
> **읽기 쉽고, 변경하기 쉽고, 잘못 사용하기 어렵고, 실패를 예측할 수 있는 코드**를 만드는 것이 목적이다.

---

# 공통 실무 데이터

이 문서에서는 다음 사용자와 상품 데이터를 여러 예제에서 사용한다.

```javascript
const users = [
    {
        id: 1,
        name: "Kim",
        age: 21,
        active: true,
        email: "kim@example.com",
        score: 85,
    },
    {
        id: 2,
        name: "Lee",
        age: 17,
        active: false,
        email: "lee@example.com",
        score: 58,
    },
    {
        id: 3,
        name: "Park",
        age: 28,
        active: true,
        email: "park@example.com",
        score: 92,
    },
]

const products = [
    {
        id: 101,
        name: "Keyboard",
        price: 50000,
        stock: 3,
    },
    {
        id: 102,
        name: "Mouse",
        price: 30000,
        stock: 0,
    },
]
```

이 데이터로 다음 개념을 연결한다.

- 네이밍
- 조건문
- 배열 순회
- `map()`, `filter()`, `reduce()`
- 함수 분리
- DOM 렌더링
- 이벤트 위임
- 저장소
- API 요청
- 오류 처리
- 상태 관리
- 보안

---

# 핵심 기준

| 기준 | 의미 |
| --- | --- |
| 가독성 | 코드의 의도를 빠르게 이해할 수 있음 |
| 명확한 이름 | 변수·함수·상태의 역할이 이름에 드러남 |
| 단일 책임 | 함수가 하나의 주요 역할을 담당 |
| 상태 분리 | 데이터 상태와 DOM 표현을 구분 |
| 중복 최소화 | 같은 로직과 Listener를 반복 등록하지 않음 |
| 예측 가능성 | 입력·출력·오류 흐름이 분명함 |
| 안전한 출력 | 외부 문자열을 실행 가능한 HTML로 만들지 않음 |
| 실패 처리 | Loading·Empty·Error 상태를 구분 |
| 확장성 | 기능 추가 시 기존 코드를 크게 깨지 않음 |
| 테스트 가능성 | DOM과 무관한 계산 로직을 작은 함수로 검증 가능 |

---

# 학습 목표

- 실행되는 코드와 실무에서 유지보수하기 좋은 코드를 구분할 수 있다.
- 역할이 명확한 변수명·함수명·상태명을 작성할 수 있다.
- `const`를 기본으로 사용하고 재할당이 필요한 경우에만 `let`을 선택할 수 있다.
- 엄격한 비교와 명시적인 자료형 변환을 사용할 수 있다.
- Guard Clause로 중첩 조건문을 줄일 수 있다.
- 반복문의 목적에 맞게 `for...of`, `map()`, `filter()`, `reduce()`를 선택할 수 있다.
- 함수의 검증·계산·렌더링·요청 책임을 분리할 수 있다.
- DOM 선택 결과가 `null`일 수 있음을 처리할 수 있다.
- 상태를 DOM 문자열에만 저장하지 않고 JavaScript 값으로 관리할 수 있다.
- `innerHTML`과 `textContent`를 안전하게 선택할 수 있다.
- 동적 요소에 Event Delegation을 적용할 수 있다.
- Listener 중복 등록과 익명 함수 해제 문제를 방지할 수 있다.
- `async/await`, `response.ok`, `try...catch`, `finally`를 사용할 수 있다.
- Loading·Empty·Error·Success 상태를 화면에 표현할 수 있다.
- `AbortController`로 이전 요청을 취소할 수 있다.
- Local Storage 데이터를 안전하게 저장·복원할 수 있다.
- API Key·Webhook URL을 Client 코드에 노출하지 않는 구조를 설명할 수 있다.
- 큰 Script를 기능별 Module과 Component로 분리할 수 있다.

---

# 1. 좋은 코드는 의도가 보인다

## 1-1. Before

```javascript
const a = 21
const b = true

if (a >= 19 && b) {
    console.log("가능")
}
```

## 1-2. After

```javascript
const userAge = 21
const isActive = true

if (
    userAge >= 19
    && isActive
) {
    console.log(
        "이용 가능",
    )
}
```

## 1-3. 실행 결과

```text
이용 가능
```

## 1-4. 왜 개선됐을까?

| Before | After |
| --- | --- |
| `a`, `b`의 의미를 알 수 없음 | 업무 의미가 이름에 드러남 |
| `"가능"`의 대상이 불분명 | `"이용 가능"`으로 상황 표현 |
| 코드를 끝까지 읽어야 의미 파악 | 조건만 보고 의도 파악 가능 |

---

# 2. 변수는 명사, Boolean은 질문처럼 작성

일반 값은 명사 형태로 작성한다.

```javascript
const userName = "Kim"
const totalPrice = 30000
const loginCount = 3
```

Boolean은 조건문에서 질문처럼 읽히게 작성한다.

```javascript
const isActive = true
const hasPermission = false
const canEdit = true
const isLoading = false
```

## 2-1. Before

```javascript
const active = true

if (active) {
    console.log(
        "활성 사용자",
    )
}
```

## 2-2. After

```javascript
const isActive = true

if (isActive) {
    console.log(
        "활성 사용자",
    )
}
```

> 💼 **실무에서는 이렇게 생각합니다.**
>
> - `if (isActive)` → 활성 상태인가?
> - `if (hasPermission)` → 권한이 있는가?
> - `if (canEdit)` → 수정할 수 있는가?
> - `if (isLoading)` → 요청 중인가?

---

# 3. 함수 이름은 동작을 표현

```javascript
function validateUser() {}
function calculateTotal() {}
function renderUserList() {}
function fetchUsers() {}
function handleSubmit() {}
```

좋지 않은 이름:

```javascript
function run() {}
function test() {}
function data() {}
function click() {}
```

이벤트 함수에는 `handle`, 초기화 함수에는 `init`, 조회 함수에는 `get`·`find`·`fetch`를 사용할 수 있다.

---

# 4. `const`를 기본으로 사용

## 4-1. Before

```javascript
let userName = "Kim"
let users = []
let button = (
    document.querySelector(
        "#save",
    )
)
```

값을 다시 대입하지 않는데 모두 `let`을 사용한다.

## 4-2. After

```javascript
const userName = "Kim"
const users = []
const button = (
    document.querySelector(
        "#save",
    )
)
```

## 4-3. `let`이 필요한 경우

```javascript
let count = 0
let currentPage = 1
let isDragging = false
let controller = null
```

> [!IMPORTANT]
> `const`는 객체 내부를 변경할 수 없다는 뜻이 아니다.  
> 변수 자체에 다른 값을 다시 대입할 수 없다는 뜻이다.

---

# 5. `var` 대신 Block Scope 사용

## 5-1. Before

```javascript
for (
    var index = 0;
    index < 3;
    index += 1
) {
    setTimeout(
        () => {
            console.log(index)
        },
        0,
    )
}
```

대표 결과:

```text
3
3
3
```

## 5-2. After

```javascript
for (
    let index = 0;
    index < 3;
    index += 1
) {
    setTimeout(
        () => {
            console.log(index)
        },
        0,
    )
}
```

결과:

```text
0
1
2
```

`let`은 반복마다 새로운 Block Scope Binding을 만든다.

---

# 6. 엄격한 비교를 기본으로 사용

## 6-1. Before

```javascript
if (userId == 1) {
    console.log("일치")
}
```

문자열 `"1"`도 Number `1`과 같다고 판정될 수 있다.

## 6-2. After

```javascript
if (userId === 1) {
    console.log("일치")
}
```

자료형 변환이 필요하면 비교 전에 명시적으로 수행한다.

```javascript
const numericUserId = Number(
    userId,
)
```

---

# 7. 자료형 변환은 명시적으로 작성

```javascript
const quantity = Number(
    quantityInput.value,
)

if (
    !Number.isInteger(
        quantity,
    )
    || quantity < 1
) {
    throw new Error(
        "수량은 1 이상의 정수여야 합니다.",
    )
}
```

`parseInt()`는 문자열 앞부분만 읽을 수 있다.

```javascript
Number.parseInt(
    "10px",
    10,
)
```

CSS 단위 처리에는 적합할 수 있지만 Form 숫자 검증에는 `Number()`와 검증을 함께 사용하는 편이 명확하다.

---

# 8. Truthy·Falsy보다 업무 조건을 명확히 표현

## 8-1. Before

```javascript
if (users) {
    console.log(
        "사용자 있음",
    )
}
```

빈 배열도 Truthy다.

## 8-2. After

```javascript
if (
    users.length > 0
) {
    console.log(
        "사용자 있음",
    )
}
```

DOM Collection도 마찬가지다.

```javascript
if (
    menuItems.length === 0
) {
    emptyView.hidden = false
}
```

---

# 9. `null`과 `undefined`를 구분

```text
null
→ 값이 없음을 의도적으로 표현

undefined
→ 값이 아직 없거나 Property가 존재하지 않음
```

선택 결과:

```javascript
const button = (
    document.querySelector(
        "#save",
    )
)

if (button === null) {
    throw new Error(
        "#save 버튼이 없습니다.",
    )
}
```

Optional Chaining은 선택 요소에만 사용한다.

```javascript
optionalBanner?.remove()
```

필수 요소까지 조용히 무시하면 HTML 오류를 발견하기 어렵다.

---

# 10. Guard Clause로 중첩을 줄인다

## 10-1. Before

```javascript
function submitOrder(
    order,
) {
    if (order) {
        if (
            order.items.length > 0
        ) {
            if (
                order.userId
            ) {
                console.log(
                    "주문 처리",
                )
            }
        }
    }
}
```

## 10-2. After

```javascript
function submitOrder(
    order,
) {
    if (order === null) {
        return
    }

    if (
        order.items.length === 0
    ) {
        return
    }

    if (!order.userId) {
        return
    }

    console.log(
        "주문 처리",
    )
}
```

정상 흐름이 가장 아래에 한 번만 나타난다.

---

# 11. 조건식은 의미 있는 함수로 분리

## 11-1. Before

```javascript
if (
    user.age >= 19
    && user.active
    && user.score >= 80
    && user.email.includes("@")
) {
    console.log(
        "대상 사용자",
    )
}
```

## 11-2. After

```javascript
function isEligibleUser(
    user,
) {
    return (
        user.age >= 19
        && user.active
        && user.score >= 80
        && user.email.includes("@")
    )
}

if (
    isEligibleUser(user)
) {
    console.log(
        "대상 사용자",
    )
}
```

복잡한 업무 규칙에 이름이 생긴다.

---

# 12. Magic Number와 Magic String을 상수로 분리

## 12-1. Before

```javascript
if (
    message.length > 2000
) {
    console.log(
        "너무 긴 메시지",
    )
}
```

## 12-2. After

```javascript
const MAX_MESSAGE_LENGTH = 2000

if (
    message.length
    > MAX_MESSAGE_LENGTH
) {
    console.log(
        "너무 긴 메시지",
    )
}
```

상수는 의미와 수정 위치를 제공한다.

---

# 13. 반복 목적에 맞는 문법 선택

| 목적 | 선택 |
| --- | --- |
| 단순 값 순회 | `for...of` |
| Index도 필요 | `entries()` 또는 일반 `for` |
| 새 배열 변환 | `map()` |
| 조건에 맞는 값 | `filter()` |
| 하나의 값으로 누적 | `reduce()` |
| 존재 여부 | `some()` |
| 전체 조건 | `every()` |
| 첫 항목 검색 | `find()` |

---

# 14. 배열을 단순 순회할 때 `for...of`

## 14-1. Before

```javascript
for (
    let index = 0;
    index < users.length;
    index += 1
) {
    console.log(
        users[index].name,
    )
}
```

## 14-2. After

```javascript
for (const user of users) {
    console.log(user.name)
}
```

Index가 필요하지 않다면 직접 값을 순회한다.

---

# 15. Index가 필요하면 `entries()`

```javascript
for (
    const [
        index,
        user,
    ]
    of users.entries()
) {
    console.log(
        index + 1,
        user.name,
    )
}
```

---

# 16. `map()`은 새 배열을 만들 때 사용

## 16-1. Before

```javascript
const names = []

users.forEach(
    user => {
        names.push(
            user.name,
        )
    },
)
```

## 16-2. After

```javascript
const names = users.map(
    user => user.name,
)
```

실행 결과:

```text
["Kim", "Lee", "Park"]
```

Side Effect가 목적이면 `forEach()`, 새 배열이 목적이면 `map()`을 사용한다.

---

# 17. `filter()`는 조건에 맞는 값만 남긴다

```javascript
const activeUsers = (
    users.filter(
        user => user.active,
    )
)
```

결과:

```text
Kim
Park
```

조건 함수를 분리하면 재사용하기 쉽다.

```javascript
function isActiveUser(
    user,
) {
    return user.active
}
```

---

# 18. `reduce()`는 누적 목적이 분명할 때 사용

```javascript
const totalPrice = (
    products.reduce(
        (
            total,
            product,
        ) => (
            total
            + product.price
        ),
        0,
    )
)
```

실행 결과:

```text
80000
```

복잡한 `reduce()` 하나보다 여러 단계의 명확한 코드가 더 읽기 쉬울 수 있다.

---

# 19. 객체 구조 분해로 필요한 값 표현

## 19-1. Before

```javascript
function printUser(
    user,
) {
    console.log(
        user.name,
        user.email,
    )
}
```

## 19-2. After

```javascript
function printUser({
    name,
    email,
}) {
    console.log(
        name,
        email,
    )
}
```

함수가 어떤 Property를 사용하는지 Signature에서 알 수 있다.

---

# 20. 기본값과 Nullish Coalescing

```javascript
const displayName = (
    user.nickname
    ?? user.name
    ?? "이름 없음"
)
```

`||`는 빈 문자열과 `0`도 Falsy로 처리한다.

```javascript
const pageSize = (
    settings.pageSize
    ?? 20
)
```

값 `0`도 유효한 설정이라면 `??`가 적합하다.

---

# 21. Optional Chaining은 안전한 탐색에 사용

```javascript
const city = (
    user
        .address
        ?.city
    ?? "주소 없음"
)
```

필수 데이터 검증을 Optional Chaining만으로 대체하지 않는다.

```javascript
if (
    typeof user.name
    !== "string"
) {
    throw new TypeError(
        "사용자 이름이 없습니다.",
    )
}
```

---

# 22. 함수 하나는 하나의 주요 역할을 가진다

## 22-1. Before

```javascript
async function loadUsers() {
    const response = await fetch(
        "/api/users",
    )

    const users = await response.json()

    const tbody = (
        document.querySelector(
            "#users",
        )
    )

    tbody.innerHTML = ""

    for (const user of users) {
        tbody.innerHTML += (
            `<tr>`
            + `<td>${user.name}</td>`
            + `</tr>`
        )
    }

    localStorage.setItem(
        "users",
        JSON.stringify(
            users,
        ),
    )
}
```

요청·변환·DOM·저장을 한 함수에서 모두 처리한다.

## 22-2. After

```javascript
async function fetchUsers() {
    const response = await fetch(
        "/api/users",
    )

    if (!response.ok) {
        throw new Error(
            `HTTP ${response.status}`,
        )
    }

    return response.json()
}

function saveUsers(
    users,
) {
    localStorage.setItem(
        "users",
        JSON.stringify(
            users,
        ),
    )
}

function renderUsers(
    tbody,
    users,
) {
    // DOM 렌더링
}
```

---

# 23. 함수의 입력과 결과를 분명히 한다

```javascript
function calculateTotal(
    items,
) {
    return items.reduce(
        (
            total,
            item,
        ) => (
            total
            + item.price
            * item.quantity
        ),
        0,
    )
}
```

DOM에 직접 출력하지 않는 계산 함수는 독립적으로 테스트하기 쉽다.

---

# 24. Side Effect를 경계에 모은다

```text
순수 계산
→ 값 입력
→ 값 반환

Side Effect
→ DOM 변경
→ Network 요청
→ Storage 저장
→ Console·Alert
```

계산 함수와 Side Effect 함수를 분리한다.

```javascript
const total = calculateTotal(
    cartItems,
)

renderTotal(
    totalView,
    total,
)
```

---

# 25. 필수 DOM 요소는 명확하게 검사

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

## 25-1. 사용

```javascript
const form = getRequiredElement(
    "#login-form",
)

const statusView = (
    getRequiredElement(
        "#status",
    )
)
```

HTML 누락을 조용히 무시하지 않는다.

---

# 26. DOM 선택 범위를 Component 내부로 제한

## 26-1. Before

```javascript
const button = (
    document.querySelector(
        ".button",
    )
)
```

같은 클래스가 여러 기능에 있으면 잘못된 요소를 선택할 수 있다.

## 26-2. After

```javascript
function initTodo(
    root,
) {
    const button = (
        root.querySelector(
            ".todo-add",
        )
    )
}
```

Component Root를 전달해 선택 범위를 제한한다.

---

# 27. 상태를 DOM Text에만 저장하지 않는다

## 27-1. Before

```javascript
countButton.addEventListener(
    "click",
    () => {
        countView.textContent = (
            Number(
                countView.textContent,
            ) + 1
        )
    },
)
```

## 27-2. After

```javascript
let count = 0

function renderCount() {
    countView.textContent = (
        String(count)
    )
}

countButton.addEventListener(
    "click",
    () => {
        count += 1
        renderCount()
    },
)
```

상태는 JavaScript 값에, DOM은 표시 결과에 둔다.

---

# 28. 외부 문자열은 `textContent`로 출력

## 28-1. Before

```javascript
messageView.innerHTML = (
    userInput
)
```

## 28-2. After

```javascript
messageView.textContent = (
    userInput
)
```

사용자 입력·API 응답·AI 응답·Webhook 메시지는 신뢰하지 못한 문자열로 취급한다.

---

# 29. HTML 구조가 필요하면 Node를 생성

```javascript
function createUserItem(
    user,
) {
    const item = (
        document.createElement(
            "li",
        )
    )

    const name = (
        document.createElement(
            "strong",
        )
    )

    name.textContent = user.name

    const email = (
        document.createElement(
            "span",
        )
    )

    email.textContent = user.email

    item.append(
        name,
        email,
    )

    return item
}
```

---

# 30. 반복 렌더링에서 `innerHTML +=`를 피한다

## 30-1. Before

```javascript
for (const user of users) {
    list.innerHTML += (
        `<li>${user.name}</li>`
    )
}
```

반복마다 기존 HTML 전체를 다시 읽고 Parse할 수 있다.

## 30-2. After

```javascript
const fragment = (
    document.createDocumentFragment()
)

for (const user of users) {
    fragment.append(
        createUserItem(user),
    )
}

list.replaceChildren(
    fragment,
)
```

---

# 31. Append 후 부모 Text를 덮어쓰지 않는다

## 31-1. Before

```javascript
const message = (
    document.createElement(
        "div",
    )
)

resultView.append(message)

resultView.innerText = (
    responseText
)
```

`innerText` 재할당으로 방금 추가한 `message`가 제거된다.

## 31-2. After

```javascript
message.textContent = (
    responseText
)

resultView.append(message)
```

---

# 32. 상태 Style은 Class로 관리

## 32-1. Before

```javascript
button.style.backgroundColor = (
    "red"
)

button.style.fontWeight = (
    "bold"
)
```

## 32-2. After

```javascript
button.classList.add(
    "is-error",
)
```

```css
.button.is-error {
    background: red;
    font-weight: bold;
}
```

JavaScript는 상태를, CSS는 시각 표현을 담당한다.

---

# 33. 이벤트 함수는 이름 있는 참조를 사용

```javascript
function handleSaveClick() {
    console.log("저장")
}

saveButton.addEventListener(
    "click",
    handleSaveClick,
)
```

해제:

```javascript
saveButton.removeEventListener(
    "click",
    handleSaveClick,
)
```

익명 함수는 같은 참조로 제거하기 어렵다.

---

# 34. 이벤트 등록을 한 번만 수행

## 34-1. Before

```javascript
function addTodo() {
    // Todo 생성

    document
        .querySelectorAll(
            ".todo-remove",
        )
        .forEach(
            button => {
                button.addEventListener(
                    "click",
                    removeTodo,
                )
            },
        )
}
```

Todo를 추가할 때마다 기존 Button에도 Listener가 다시 등록될 수 있다.

## 34-2. After

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
    },
)
```

---

# 35. 동적 요소에는 Event Delegation

상위 요소 Listener 하나로 동적 자식을 처리한다.

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

        selectMenu(item)
    },
)
```

---

# 36. `target`과 `currentTarget`을 구분

```javascript
menuList.addEventListener(
    "click",
    event => {
        console.log(
            event.target,
        )

        console.log(
            event.currentTarget,
        )
    },
)
```

```text
target
→ 실제 클릭된 자식

currentTarget
→ Listener가 등록된 menuList
```

---

# 37. 기본 동작과 이벤트 전파를 구분

```javascript
event.preventDefault()
```

기본 Form 제출·Link 이동·방향키 Scroll 등을 막는다.

```javascript
event.stopPropagation()
```

이벤트가 다음 상위 요소로 전달되는 것을 막는다.

두 기능을 같은 것으로 이해하면 안 된다.

---

# 38. Form은 Button Click보다 Submit을 처리

## 38-1. Before

```javascript
loginButton.addEventListener(
    "click",
    handleLogin,
)
```

Keyboard Enter 제출을 놓칠 수 있다.

## 38-2. After

```javascript
loginForm.addEventListener(
    "submit",
    event => {
        event.preventDefault()
        handleLogin()
    },
)
```

Button과 Enter 제출을 하나의 흐름으로 통합한다.

---

# 39. 입력값은 `trim()` 후 검증

```javascript
const userId = (
    idInput.value.trim()
)

if (userId === "") {
    statusView.textContent = (
        "아이디를 입력해주세요."
    )

    idInput.focus()
    return
}
```

Password는 정책에 따라 공백이 유효할 수도 있으므로 무조건 `trim()`할지 요구사항을 확인한다.

---

# 40. Loading·Empty·Error·Success 상태를 구분

```text
Idle
→ 요청 전

Loading
→ 요청 진행 중

Success
→ 데이터 표시

Empty
→ 정상 응답이지만 결과 없음

Error
→ 요청·Parse·검증 실패
```

화면에 같은 문구 하나만 사용하지 않는다.

---

# 41. Fetch에서는 `response.ok`를 검사

## 41-1. Before

```javascript
const response = await fetch(
    "/api/users",
)

const users = await response.json()
```

HTTP 404·500도 Parse를 시도할 수 있다.

## 41-2. After

```javascript
const response = await fetch(
    "/api/users",
)

if (!response.ok) {
    throw new Error(
        `HTTP ${response.status}`,
    )
}

const users = await response.json()
```

---

# 42. `async/await`와 `try...catch`

```javascript
async function loadUsers() {
    try {
        const users = (
            await fetchUsers()
        )

        renderUsers(
            userList,
            users,
        )
    } catch (
        error
    ) {
        errorView.textContent = (
            "사용자 정보를 "
            + "불러오지 못했습니다."
        )

        console.error(error)
    }
}
```

사용자용 메시지와 개발자용 오류 정보를 구분한다.

---

# 43. `finally`에서 UI를 복구

```javascript
async function handleLoad() {
    loadButton.disabled = true

    try {
        await loadUsers()
    } finally {
        loadButton.disabled = false
    }
}
```

성공·실패 모두에서 실행해야 하는 정리를 한곳에 둔다.

---

# 44. 중복 요청을 막는다

```javascript
let isLoading = false

async function handleSearch() {
    if (isLoading) {
        return
    }

    isLoading = true

    try {
        await search()
    } finally {
        isLoading = false
    }
}
```

Button `disabled`와 상태 Flag를 함께 사용할 수 있다.

---

# 45. 이전 요청을 취소한다

검색어가 바뀔 때 이전 요청 결과가 최신 결과를 덮어쓰지 않도록 한다.

```javascript
let currentController = null

async function fetchLatest(
    url,
) {
    currentController?.abort()

    const controller = (
        new AbortController()
    )

    currentController = controller

    try {
        const response = await fetch(
            url,
            {
                signal:
                    controller.signal,
            },
        )

        if (!response.ok) {
            throw new Error(
                `HTTP ${response.status}`,
            )
        }

        return response.json()
    } finally {
        if (
            currentController
            === controller
        ) {
            currentController = null
        }
    }
}
```

---

# 46. Abort는 일반 오류와 구분

```javascript
async function handleLatestRequest(
    url,
) {
    try {
        return await fetchLatest(
            url,
        )
    } catch (
        error
    ) {
        if (
            error.name
            === "AbortError"
        ) {
            return null
        }

        throw error
    }
}
```

사용자 취소와 실제 실패를 같은 오류 문구로 표시하지 않는다.

---

# 47. API 응답의 구조를 검증

```javascript
function isUserArray(
    value,
) {
    return (
        Array.isArray(value)
        && value.every(
            user => (
                user !== null
                && typeof user
                    === "object"
                && typeof user.name
                    === "string"
            ),
        )
    )
}
```

JSON Parse 성공은 데이터 구조가 올바르다는 뜻이 아니다.

---

# 48. 외부 API 날짜는 Timezone을 확인

```javascript
function formatLocalDate(
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

사용자의 “오늘”에 `toISOString()`을 그대로 사용하면 UTC 날짜와 달라질 수 있다.

---

# 49. JSON 객체와 JSON 문자열을 구분

```javascript
const requestData = {
    name: "Kim",
}
```

JavaScript 객체다.

```javascript
const jsonText = (
    JSON.stringify(
        requestData,
    )
)
```

JSON 문자열이다.

변수 이름도 구분한다.

---

# 50. Local Storage는 안전하게 Parse

```javascript
function loadJson(
    key,
    fallback,
) {
    const stored = (
        localStorage.getItem(
            key,
        )
    )

    if (stored === null) {
        return fallback
    }

    try {
        return JSON.parse(
            stored,
        )
    } catch (
        error
    ) {
        console.error(
            `${key} 복원 실패`,
            error,
        )

        return fallback
    }
}
```

손상된 값 하나로 Application 전체가 중단되지 않게 한다.

---

# 51. 저장할 데이터와 실행 객체를 구분

Storage에는 상태 데이터만 저장한다.

```javascript
const settings = {
    theme: "dark",
    pageSize: 20,
}
```

함수·DOM Element·Event 객체를 저장하려 하지 않는다.

---

# 52. API Key와 Webhook URL은 Client에 넣지 않는다

```text
잘못된 구조
Browser JavaScript
→ 실제 API Key·Webhook URL 포함

권장 구조
Browser
→ 자신의 Backend
→ Environment Variable
→ 외부 API
```

`.gitignore`는 이미 Browser Bundle에 포함된 Key를 보호하지 못한다.

---

# 53. 민감정보는 Console에 출력하지 않는다

출력하지 않는 값:

- Password
- Token
- API Key
- Webhook URL
- 인증번호
- 개인식별정보

```javascript
console.log(
    "로그인 검증 완료",
)
```

결과 상태만 기록한다.

---

# 54. 외부 HTML과 AI 응답을 바로 실행하지 않는다

```text
API 응답
AI 응답
사용자 입력
URL Parameter
→ 외부 문자열
```

기본 출력:

```javascript
view.textContent = text
```

Markdown·HTML Renderer를 사용할 경우 Sanitizer와 허용 정책이 필요하다.

---

# 55. Module로 역할을 분리

```text
api/
→ HTTP 요청

domain/
→ 검증·계산

ui/
→ DOM 생성·렌더링

storage/
→ 저장·복원

main.js
→ 초기화·연결
```

---

# 56. Module Export 예제

```javascript
export function calculateTotal(
    items,
) {
    return items.reduce(
        (
            total,
            item,
        ) => (
            total
            + item.price
            * item.quantity
        ),
        0,
    )
}
```

```javascript
import {
    calculateTotal,
} from "./domain/cart.js"
```

---

# 57. 초기화 함수는 기능을 연결

```javascript
function init() {
    const form = getRequiredElement(
        "#search-form",
    )

    const resultView = (
        getRequiredElement(
            "#result",
        )
    )

    initSearch({
        form,
        resultView,
    })
}

init()
```

`main.js`에 모든 세부 로직을 작성하지 않는다.

---

# 58. 작은 Component는 Closure로 상태를 숨긴다

```javascript
function createCounter(
    view,
) {
    let count = 0

    function render() {
        view.textContent = (
            String(count)
        )
    }

    return {
        increment() {
            count += 1
            render()
        },

        reset() {
            count = 0
            render()
        },
    }
}
```

전역 변수 충돌을 줄인다.

---

# 59. 주석은 코드가 아닌 이유를 설명

좋지 않은 주석:

```javascript
// count에 1을 더한다.
count += 1
```

좋은 주석:

```javascript
// API가 이전 시각 발표값만 제공하므로
// 조회 기준을 한 시간 전으로 조정한다.
baseDate.setHours(
    baseDate.getHours() - 1,
)
```

코드 자체로 알 수 없는 정책과 제약을 기록한다.

---

# 60. Format과 Lint를 자동화

대표 도구:

```text
Formatter
→ Prettier

Lint
→ ESLint

Type 검사
→ TypeScript 또는 JSDoc

Test
→ Vitest, Jest 등
```

팀 설정을 Repository에 함께 저장해 개인별 Format 차이를 줄인다.

---

# 61. JSDoc으로 입력과 반환값 표현

```javascript
/**
 * 장바구니 합계를 계산한다.
 *
 * @param {{
 *   price: number,
 *   quantity: number
 * }[]} items
 * @returns {number}
 */
function calculateTotal(
    items,
) {
    return items.reduce(
        (
            total,
            item,
        ) => (
            total
            + item.price
            * item.quantity
        ),
        0,
    )
}
```

---

# 62. 실제 개선 사례 1: NodeList에 `classList`

## 62-1. Before

```javascript
const quizItems = (
    document.querySelectorAll(
        "div.quiz",
    )
)

quizItems.classList.contains(
    "q2",
)
```

`querySelectorAll()` 결과는 NodeList다.

## 62-2. After

```javascript
const quizItems = (
    document.querySelectorAll(
        "div.quiz.q2",
    )
)

console.log(
    quizItems.length,
)
```

또는 개별 요소를 순회한다.

---

# 63. 실제 개선 사례 2: Event Listener 중복

## 63-1. Before

```text
Todo 추가
→ 모든 삭제 버튼 다시 선택
→ 기존 버튼에도 Listener 재등록
```

## 63-2. After

```javascript
todoList.addEventListener(
    "click",
    handleTodoClick,
)
```

부모에 한 번 등록한다.

---

# 64. 실제 개선 사례 3: `innerHTML +=`

## 64-1. Before

```javascript
for (const user of users) {
    tbody.innerHTML += (
        `<td>${user.name}</td>`
    )
}
```

Table 구조도 잘못되고 반복 재파싱도 발생한다.

## 64-2. After

```javascript
const row = document.createElement(
    "tr",
)

const cell = document.createElement(
    "td",
)

cell.textContent = user.name
row.append(cell)
tbody.append(row)
```

---

# 65. 실제 개선 사례 4: Fetch 성공 검사 누락

## 65-1. Before

```javascript
const response = await fetch(url)
const data = await response.json()
```

## 65-2. After

```javascript
const response = await fetch(url)

if (!response.ok) {
    throw new Error(
        `HTTP ${response.status}`,
    )
}

const data = await response.json()
```

---

# 66. 실제 개선 사례 5: AI History 오염

## 66-1. Before

```javascript
conversation.contents.push({
    role: "model",

    parts: [
        {
            text: JSON.stringify(
                result,
            ),
        },
    ],
})
```

전체 API Response Metadata를 대화에 저장한다.

## 66-2. After

```javascript
conversation.contents.push({
    role: "model",

    parts: [
        {
            text: responseText,
        },
    ],
})
```

실제 답변 Text만 저장한다.

---

# 67. 실제 개선 사례 6: Webhook Credential 노출

## 67-1. Before

```text
Client JavaScript
→ 실제 Discord Webhook URL
```

## 67-2. After

```text
Client
→ /api/discord-message
→ Backend 환경 변수
→ Discord Webhook
```

노출된 Credential은 Source에서 지우는 것만으로 끝나지 않고 폐기·재생성이 필요하다.

---

# 68. 실제 개선 사례 7: 잘못된 Button Type

## 68-1. Before

```html
<button type="buttn">
```

## 68-2. After

```html
<button type="button">
```

작은 오타도 Form 기본 동작에 영향을 줄 수 있으므로 HTML Validator와 Browser DevTools로 검수한다.

---

# 69. 실제 개선 사례 8: 빈 입력 전송

## 69-1. Before

```javascript
const prompt = (
    promptInput.value
)

sendPrompt(prompt)
```

## 69-2. After

```javascript
const prompt = (
    promptInput.value.trim()
)

if (prompt === "") {
    statusView.textContent = (
        "내용을 입력해주세요."
    )

    return
}

sendPrompt(prompt)
```

---

# 70. 실제 개선 사례 9: 동일 Node를 여러 번 Append

```javascript
list.append(item)
list.append(item)
```

복제되지 않고 같은 Node가 이동한다.

복제본이 필요하면:

```javascript
const clonedItem = item.cloneNode(
    true,
)
```

---

# 71. 실제 개선 사례 10: 삭제와 숨김 혼동

```javascript
element.remove()
```

DOM에서 제거한다.

잠시 숨기는 목적이면:

```javascript
element.hidden = true
```

또는 상태 Class를 사용한다.

---

# 72. Before와 After를 비교할 때 확인할 기준

```text
코드 줄 수가 줄었는가?
→ 참고 기준일 뿐

의도가 더 명확한가?
→ 중요

잘못된 상태를 더 일찍 막는가?
→ 중요

변경 범위가 작아졌는가?
→ 중요

테스트 가능한 함수가 늘었는가?
→ 중요

보안·실패 상태를 처리하는가?
→ 중요
```

---

# 73. 실무형 예제: 사용자 목록 Component

```javascript
function createUserList({
    root,
    fetchUsers,
}) {
    const loadButton = (
        getRequiredElement(
            ".user-load",
            root,
        )
    )

    const list = (
        getRequiredElement(
            ".user-list",
            root,
        )
    )

    const statusView = (
        getRequiredElement(
            ".user-status",
            root,
        )
    )

    let isLoading = false

    function createUserItem(
        user,
    ) {
        const item = (
            document.createElement(
                "li",
            )
        )

        item.dataset.userId = (
            String(user.id)
        )

        const name = (
            document.createElement(
                "strong",
            )
        )

        name.textContent = user.name

        const email = (
            document.createElement(
                "span",
            )
        )

        email.textContent = user.email

        item.append(
            name,
            email,
        )

        return item
    }

    function render(
        users,
    ) {
        const fragment = (
            document
                .createDocumentFragment()
        )

        for (const user of users) {
            fragment.append(
                createUserItem(user),
            )
        }

        list.replaceChildren(
            fragment,
        )
    }

    async function load() {
        if (isLoading) {
            return
        }

        isLoading = true
        loadButton.disabled = true
        statusView.textContent = (
            "불러오는 중입니다."
        )

        try {
            const users = (
                await fetchUsers()
            )

            if (!Array.isArray(users)) {
                throw new TypeError(
                    "사용자 목록이 아닙니다.",
                )
            }

            render(users)

            statusView.textContent = (
                users.length === 0
                    ? "사용자가 없습니다."
                    : `${users.length}명을 `
                        + "불러왔습니다."
            )
        } catch (
            error
        ) {
            statusView.textContent = (
                "사용자 정보를 "
                + "불러오지 못했습니다."
            )

            console.error(error)
        } finally {
            isLoading = false
            loadButton.disabled = false
        }
    }

    loadButton.addEventListener(
        "click",
        load,
    )

    return {
        load,
    }
}
```

## 73-1. 실행 흐름

```text
Button Click
→ 중복 요청 검사
→ Loading 상태
→ API 함수 호출
→ 응답 자료형 검증
→ 안전한 Node 렌더링
→ Empty·Success 상태 표시
→ Button 복구
```

## 73-2. 실무에서 이렇게 작성하는 이유

| 코드 | 이유 |
| --- | --- |
| Root 기반 선택 | Component 범위 제한 |
| API 함수 주입 | Network와 UI 분리 |
| Loading Flag | 중복 요청 방지 |
| `textContent` | 외부 데이터 안전 출력 |
| Fragment | 여러 Node 조립 |
| `replaceChildren()` | 재조회 중복 제거 |
| `finally` | UI 상태 복구 |
| 반환 객체 | 외부에서 필요한 기능만 공개 |

---

# 74. 파일 구조 예시

```text
src/
├── api/
│   └── users-api.js
├── components/
│   └── user-list.js
├── domain/
│   └── user-validator.js
├── storage/
│   └── json-storage.js
├── utils/
│   └── dom.js
└── main.js
```

기능 규모가 작다면 과도하게 파일을 나누지 않는다.

---

# 75. 자주 하는 실수

## 75-1. 모든 변수를 `let`으로 선언

재할당 여부가 드러나지 않는다.

## 75-2. 짧은 이름을 좋은 코드라고 생각

의미 없는 축약은 해석 비용을 높인다.

## 75-3. `map()`을 Side Effect 목적으로 사용

새 배열을 사용하지 않는다면 다른 반복 방식을 검토한다.

## 75-4. 빈 배열·NodeList를 Falsy로 생각

객체이므로 Truthy다.

## 75-5. 필수 DOM 요소에 Optional Chaining만 사용

HTML 오류가 조용히 무시된다.

## 75-6. `innerHTML`을 문자열 출력 기본값으로 사용

XSS와 재파싱 문제가 생길 수 있다.

## 75-7. 동적 요소마다 Listener 등록

Event Delegation을 검토한다.

## 75-8. Fetch Catch가 HTTP 404를 자동 처리한다고 생각

`response.ok`를 직접 확인한다.

## 75-9. 실패 상태에서도 입력과 상태를 모두 초기화

사용자의 재시도 흐름을 고려한다.

## 75-10. Secret을 Client Bundle에 넣고 `.gitignore`로 보호

Browser에 전달된 값은 사용자에게 노출된다.

---

# 76. 핵심 요약

```text
좋은 이름
→ 업무 의미 표현

const 기본
→ 재할당 의도 제한

Guard Clause
→ 중첩 감소
```

```text
상태
→ JavaScript 값

화면
→ render 함수

Style 상태
→ classList
```

```text
외부 문자열
→ textContent

동적 요소
→ Event Delegation

필수 요소
→ 명확한 null 검사
```

```text
fetch
→ response.ok 검사

async/await
→ try·catch·finally

중복 요청
→ Flag·disabled·AbortController
```

```text
API Key·Webhook URL
→ Backend 환경 변수

Local Storage
→ stringify·안전한 parse
```

---

# 77. 최종 체크리스트

- [ ] 변수 이름이 업무 의미를 표현하는가?
- [ ] Boolean 이름이 질문처럼 읽히는가?
- [ ] 함수 이름이 동작을 표현하는가?
- [ ] 재할당하지 않는 값에 `const`를 사용하는가?
- [ ] `var` 대신 Block Scope를 사용하는가?
- [ ] 엄격한 비교를 사용하는가?
- [ ] 자료형을 비교 전에 명시적으로 변환하는가?
- [ ] 빈 배열·Collection을 `length`로 검사하는가?
- [ ] Guard Clause로 중첩을 줄였는가?
- [ ] Magic Number·String을 상수로 분리했는가?
- [ ] 반복 목적에 맞는 문법을 선택했는가?
- [ ] 함수 하나가 하나의 주요 역할을 담당하는가?
- [ ] 계산과 DOM·Network Side Effect를 분리했는가?
- [ ] 필수 DOM 요소 누락을 명확하게 처리하는가?
- [ ] Component 선택 범위를 Root 내부로 제한하는가?
- [ ] 상태를 DOM Text에만 저장하지 않는가?
- [ ] 외부 문자열에 `textContent`를 사용하는가?
- [ ] 반복 렌더링에서 `innerHTML +=`를 피하는가?
- [ ] Style 상태를 Class로 관리하는가?
- [ ] Listener 등록과 제거에 같은 함수 참조를 사용하는가?
- [ ] 동적 요소에 Event Delegation을 적용하는가?
- [ ] Form Submit Event를 사용하는가?
- [ ] 입력값을 요구사항에 맞게 검증하는가?
- [ ] Loading·Empty·Error·Success 상태를 구분하는가?
- [ ] Fetch에서 `response.ok`를 검사하는가?
- [ ] `try...catch...finally`로 오류와 UI 복구를 처리하는가?
- [ ] 중복 요청을 방지하거나 이전 요청을 취소하는가?
- [ ] 외부 응답 자료형과 Property를 검증하는가?
- [ ] JSON 객체와 JSON 문자열을 구분하는가?
- [ ] Storage Parse 실패에 Fallback을 제공하는가?
- [ ] Password·Token·API Key를 로그에 출력하지 않는가?
- [ ] Secret을 Backend 환경 변수에서 관리하는가?
- [ ] 큰 Script를 역할별 Module로 분리했는가?
- [ ] 주석이 동작보다 이유와 제약을 설명하는가?
- [ ] Formatter·Lint·Test 도구를 팀 설정으로 관리하는가?

---

# 마무리

JavaScript 실무 코딩 스타일의 핵심은 최신 문법을 많이 사용하는 것에서 끝나지 않는다.

```text
이름과 함수에서 의도가 보이고
    ↓
상태·계산·화면·요청의 책임이 분리되고
    ↓
동적 DOM과 이벤트가 중복 없이 관리되고
    ↓
성공뿐 아니라 빈 결과와 실패도 처리되고
    ↓
외부 데이터와 Credential이 안전하게 관리되는 것
```

좋은 JavaScript 코드는 단순히 실행되는 코드가 아니다.

**다른 개발자가 빠르게 이해하고, 기능을 안전하게 변경하고, 잘못된 상태를 쉽게 발견할 수 있는 코드**다.
# V3 실행 추적 카드 — 입력 경계 → 작은 책임 → 명시적 오류·결과

읽기 좋은 코드는 이름, 실행 시점, 상태 소유자, 부수 효과를 드러낸다. DOM 선택·검증·상태 변경·렌더링·네트워크를 함수 책임별로 나누면 디버깅이 쉬워진다.

01~22번 내 코드와 강사님 코드를 Console·Elements·Network 근거로 비교한다. `var`의 무조건적 교체보다 스코프와 재할당 의도를 보고 `const`/`let`을 선택한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/01~22 전체 원본`에서 실제 사용 위치와 차이를 확인한다.
