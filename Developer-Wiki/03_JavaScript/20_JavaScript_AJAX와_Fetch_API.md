---
title: JavaScript AJAX와 Fetch API
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# JavaScript AJAX와 Fetch API

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `20_JavaScript_AJAX와_Fetch_API.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/20_ajax.html`, `workspace_html/javascript/asset/js/20_ajax.js`, 강사님 동일 파일 |
| 핵심 범위 | AJAX, `XMLHttpRequest`, JSON 응답, 공공데이터 API, 데이터 필터·그룹화, Fetch, Promise, `async/await`, 오류 처리, Debugger |
| 실습 범위 | 회원 조회, 상대 HTML 요청, 날씨 데이터 가공, Table 렌더링, Fetch 요청, 로딩·오류·중복 요청 처리 |
| 문서 형식 | JavaScript Developer-Wiki V2 확정 형식 |

> 20번은 HTML과 연결된 외부 JavaScript 파일을 함께 확인한다.  
> 강사님 코드는 `XMLHttpRequest`, 기상청 초단기예보, 시간별 그룹화, Fetch 흐름을 구현하고, 내 코드는 회원 Table과 날씨 출력 문제를 추가로 시도했다. 이 문서에서는 실제 오류를 보존해 비교한 뒤 안전한 구현으로 개선한다.

---

# 개요

AJAX는 현재 페이지를 유지하면서 JavaScript로 서버에 데이터를 요청하고 응답 결과만 화면에 반영하는 방식이다.

```text
사용자 버튼 클릭
    ↓
JavaScript가 서버에 요청
    ↓
현재 화면은 유지
    ↓
응답 도착
    ↓
JSON 변환
    ↓
필요한 DOM만 갱신
```

대표 요청 방식:

```javascript
const xhr = new XMLHttpRequest()

xhr.open(
    "GET",
    "/api/users",
)

xhr.send()
```

```javascript
const response = await fetch(
    "/api/users",
)

const users = await response.json()
```

> [!IMPORTANT]
> 비동기 요청은 코드가 작성된 순서와 실제 완료 순서가 다를 수 있다. 응답 데이터는 요청 직후가 아니라 응답 완료 Callback 또는 `await` 이후에 사용해야 한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| AJAX | 현재 문서를 유지한 비동기 데이터 통신 |
| `XMLHttpRequest` | 전통적인 HTTP 요청 객체 |
| `open()` | HTTP Method와 URL 설정 |
| `send()` | 요청 전송 |
| `responseText` | 응답 Body 문자열 |
| HTTP Status | 요청 처리 결과 코드 |
| JSON Parse | JSON 문자열을 JavaScript 값으로 변환 |
| Fetch | Promise 기반 HTTP 요청 API |
| Promise | 미래에 완료될 작업의 상태·결과 표현 |
| `response.ok` | HTTP 성공 범위 확인 |
| `async/await` | Promise 흐름을 동기 코드처럼 작성 |
| AbortController | 진행 중인 Fetch 요청 취소 |
| Loading State | 요청 진행 중 UI 상태 |
| Data Grouping | 분리된 항목을 공통 Key 기준으로 묶는 작업 |

---

# 학습 목표

- AJAX의 목적을 설명할 수 있다.
- 일반 페이지 이동과 AJAX 요청을 구분할 수 있다.
- `XMLHttpRequest`의 생성·설정·전송·응답 처리 순서를 이해한다.
- `open()`과 `send()`의 역할을 구분할 수 있다.
- 요청 직후 `responseText`가 비어 있을 수 있는 이유를 설명할 수 있다.
- HTTP Status와 Network Error를 구분할 수 있다.
- JSON 응답을 안전하게 Parse할 수 있다.
- 상대 URL의 기준이 현재 문서 URL임을 이해한다.
- 공공데이터 API Query Parameter를 구성할 수 있다.
- UTC 날짜와 Local 날짜의 차이를 이해한다.
- 자정 이전 발표 시각을 안전하게 계산할 수 있다.
- Weather Category를 필터링하고 시간별로 그룹화할 수 있다.
- Table의 `tbody → tr → td` 구조를 올바르게 생성할 수 있다.
- `fetch()`와 `response.json()`이 Promise를 반환함을 이해한다.
- `response.ok`를 검사할 수 있다.
- Promise Chain과 `async/await`를 사용할 수 있다.
- 요청 진행·성공·실패 상태를 화면에 표시할 수 있다.
- 중복 요청을 방지하고 필요하면 요청을 취소할 수 있다.
- `debugger`와 개발자 도구로 실행 흐름을 추적할 수 있다.

---

# 1. AJAX란?

```text
Asynchronous JavaScript And XML
```

이름에는 XML이 포함되지만 현대 웹에서는 JSON 응답을 더 자주 사용한다.

핵심은 데이터 형식보다 현재 페이지를 유지한 비동기 통신이다.

---

# 2. 일반 이동과 AJAX

```text
일반 Navigation
→ 새 문서 요청
→ 화면 전체 전환

AJAX
→ 현재 문서 유지
→ 데이터 요청
→ 일부 DOM만 갱신
```

---

# 3. AJAX 응답 형식

응답은 문자열만 가능한 것이 아니다.

- JSON
- Text
- HTML
- Blob
- ArrayBuffer
- Form Data
- Image·File Binary

---

# 4. 원본 초기화

```javascript
window.addEventListener(
    "load",
    bind,
)
```

Load가 끝난 뒤 Button을 선택하고 Click Listener를 등록한다.

DOM만 필요하면 `defer`와 초기화 함수를 사용할 수 있다.

---

# 5. `XMLHttpRequest` 기본 순서

```text
1. 객체 생성
2. Method·URL 설정
3. 요청 전송
4. 응답 완료 후 처리
```

---

# 6. 객체 생성

```javascript
const xhr = (
    new XMLHttpRequest()
)
```

요청 상태와 응답 정보를 관리하는 객체를 만든다.

---

# 7. `open()`

```javascript
xhr.open(
    "GET",
    "https://jsonplaceholder.typicode.com/users",
)
```

요청 정보를 설정한다.

이 단계에서는 실제 Network 요청을 보내지 않는다.

---

# 8. `open()`의 인수

```text
Method
→ GET, POST, PUT, DELETE 등

URL
→ 요청 대상

Async
→ 기본값 true
```

동기 XHR은 UI를 멈출 수 있으므로 사용하지 않는 편이 좋다.

---

# 9. `send()`

```javascript
xhr.send()
```

설정한 요청을 실제 전송한다.

GET 요청은 일반적으로 Body 없이 호출한다.

---

# 10. `onload`

```javascript
xhr.onload = function () {
    console.log(
        xhr.responseText,
    )
}
```

응답 Body를 읽을 수 있는 상태가 되면 실행된다.

---

# 11. `onload`와 HTTP 성공

`onload`는 요청·응답 교환이 완료되었다는 의미다.

HTTP 404·500 응답이어도 `onload`가 실행될 수 있으므로 Status를 확인한다.

```javascript
if (
    xhr.status >= 200
    && xhr.status < 300
) {
    // 성공
}
```

---

# 12. `responseText`

```javascript
console.log(
    xhr.responseText,
)
```

응답 Body를 문자열로 제공한다.

JSON 응답도 처음에는 문자열이다.

---

# 13. 비동기 직후 응답

원본:

```javascript
xhr.send()

console.log(
    `[${xhr.responseText}]`,
)
```

대표 출력:

```text
[]
```

응답이 도착하기 전에 동기 코드가 먼저 실행되기 때문이다.

---

# 14. 실제 실행 흐름

```text
send()
→ Network 요청 시작
→ 다음 동기 코드 실행
→ ResponseText 아직 빈 값
→ 응답 도착
→ onload Callback 실행
```

---

# 15. `readystatechange`

```javascript
xhr.addEventListener(
    "readystatechange",
    () => {
        console.log(
            xhr.readyState,
        )
    },
)
```

XHR 상태 변화를 확인할 수 있다.

---

# 16. ReadyState

| 값 | 상태 |
| ---: | --- |
| `0` | UNSENT |
| `1` | OPENED |
| `2` | HEADERS_RECEIVED |
| `3` | LOADING |
| `4` | DONE |

현대 코드에서는 `load`, `error`, `timeout` Event를 나누어 처리하는 편이 읽기 쉽다.

---

# 17. Network Error

```javascript
xhr.onerror = function () {
    console.error(
        "Network 요청 실패",
    )
}
```

연결 실패·DNS·CORS 같은 Network 문제를 처리한다.

---

# 18. Timeout

```javascript
xhr.timeout = 5000

xhr.ontimeout = function () {
    console.error(
        "요청 시간이 초과되었습니다.",
    )
}
```

---

# 19. 안전한 XHR 함수

```javascript
function requestJson(
    url,
) {
    return new Promise(
        (
            resolve,
            reject,
        ) => {
            const xhr = (
                new XMLHttpRequest()
            )

            xhr.open(
                "GET",
                url,
            )

            xhr.onload = () => {
                if (
                    xhr.status < 200
                    || xhr.status >= 300
                ) {
                    reject(
                        new Error(
                            `HTTP ${xhr.status}`,
                        ),
                    )

                    return
                }

                try {
                    resolve(
                        JSON.parse(
                            xhr.responseText,
                        ),
                    )
                } catch (
                    error
                ) {
                    reject(error)
                }
            }

            xhr.onerror = () => {
                reject(
                    new Error(
                        "Network 요청 실패",
                    ),
                )
            }

            xhr.ontimeout = () => {
                reject(
                    new Error(
                        "요청 시간 초과",
                    ),
                )
            }

            xhr.timeout = 5000
            xhr.send()
        },
    )
}
```

---

# 20. 상대 URL 기준

원본:

```javascript
xhr.open(
    "GET",
    "19_json.html",
)
```

상대 URL은 외부 JavaScript 파일의 위치가 아니라 현재 Document URL을 기준으로 해석된다.

---

# 21. JSON Parse

```javascript
const users = JSON.parse(
    xhr.responseText,
)
```

JSON 문자열을 JavaScript 배열로 변환한다.

---

# 22. 두 번째 사용자 이름

```javascript
console.log(
    users[1].name,
)
```

Bracket Notation:

```javascript
console.log(
    users[1]["name"],
)
```

---

# 23. 중첩 Property

```javascript
const latitude = (
    users[2]
        .address
        .geo
        .lat
)
```

응답 구조를 먼저 확인한 뒤 순서대로 접근한다.

---

# 24. 외부 데이터 변경 가능성

JSONPlaceholder처럼 학습용 서비스도 응답·가용성이 변경될 수 있다.

실무 코드에서는 다음을 검증한다.

- 배열인지
- 필요한 Index가 있는지
- 중첩 객체가 있는지
- 필요한 Property의 자료형
- 빈 배열·빈 문자열 여부

---

# 25. Optional Chaining

```javascript
const latitude = (
    users[2]
        ?.address
        ?.geo
        ?.lat
    ?? null
)
```

중간 Property가 없을 때 `TypeError`를 방지한다.

---

# 26. 회원 데이터 검증

```javascript
function isUser(
    value,
) {
    return (
        value !== null
        && typeof value === "object"
        && Number.isInteger(
            value.id,
        )
        && typeof value.name
            === "string"
    )
}
```

JSON Parse 성공과 데이터 구조가 올바른 것은 별개다.

---

# 27. 기상청 요청 날짜

원본:

```javascript
const today = (
    new Date()
        .toISOString()
        .split("T")[0]
        .replace(
            /-/g,
            "",
        )
)
```

결과:

```text
YYYYMMDD
```

---

# 28. UTC 날짜 문제

`toISOString()`은 UTC 기준이다.

한국 Local 날짜가 필요한 API에서는 새벽 시간대에 날짜가 다르게 계산될 수 있다.

---

# 29. Local 날짜 함수

```javascript
function formatLocalDate(
    date,
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
        `${year}${month}${day}`
    )
}
```

---

# 30. 원본 Base Time

```javascript
let hour = (
    new Date().getHours() - 1
)
```

한 시간 전의 `HH00`을 만들려는 코드다.

---

# 31. 자정 오류

현재 시각이 0시라면:

```text
hour
→ -1
```

잘못된 Base Time이 만들어지고 날짜도 전날로 조정되지 않는다.

---

# 32. 발표 시각 계산

```javascript
function getBaseDateTime(
    now = new Date(),
) {
    const base = new Date(
        now,
    )

    base.setHours(
        base.getHours() - 1,
        0,
        0,
        0,
    )

    return {
        baseDate: (
            formatLocalDate(base)
        ),

        baseTime: (
            String(
                base.getHours(),
            ).padStart(
                2,
                "0",
            )
            + "00"
        ),
    }
}
```

Date가 날짜 경계를 자동 조정한다.

---

# 33. API Key 차이

```text
강사님 코드
→ Service Key 값 포함

내 코드
→ 빈 문자열
```

강사님 Key 원문은 문서에 다시 노출하지 않는다.

---

# 34. Frontend API Key 노출

Browser JavaScript에 Key를 넣으면 Source·Network에서 확인할 수 있다.

보호가 필요한 Key는 Backend·Proxy·Serverless Function에서 관리한다.

---

# 35. API Endpoint

원본은 HTTP Endpoint를 사용한다.

```text
http://apis.data.go.kr/...
```

HTTPS 페이지에서는 Mixed Content로 차단될 수 있다.

서비스가 지원한다면 HTTPS를 사용한다.

---

# 36. Query Parameter

대표 Parameter:

- `serviceKey`
- `numOfRows`
- `pageNo`
- `dataType`
- `base_date`
- `base_time`
- `nx`
- `ny`

---

# 37. `URLSearchParams`

```javascript
const params = (
    new URLSearchParams({
        serviceKey: apiKey,
        numOfRows: "1000",
        pageNo: "1",
        dataType: "JSON",
        base_date: baseDate,
        base_time: baseTime,
        nx: "63",
        ny: "110",
    })
)

const url = (
    `${endpoint}?${params}`
)
```

이미 Encoding된 Key를 다시 Encoding하지 않는지 API 문서를 확인한다.

---

# 38. 응답 구조

```javascript
const items = (
    data
        .response
        .body
        .items
        .item
)
```

실제 응답에는 오류 Message나 빈 Body가 올 수 있으므로 구조를 검증한다.

---

# 39. Weather Category

```text
T1H
→ 기온

REH
→ 습도

RN1
→ 1시간 강수량
```

---

# 40. Category Filter

```javascript
const targetCategories = [
    "T1H",
    "REH",
    "RN1",
]

const filtered = items.filter(
    item => (
        targetCategories.includes(
            item.category,
        )
    ),
)
```

---

# 41. 원본 문제 1

강사님은 Category·예측 시간·값을 Table에 출력한다.

```text
Category
Forecast Time
Forecast Value
```

내 코드는 같은 데이터를 `div`와 `inline-block`으로 표시한다.

표 형태 데이터라면 의미 구조가 있는 `<table>`이 적합하다.

---

# 42. 안전한 Category Row

```javascript
function createRow(
    values,
) {
    const row = document.createElement(
        "tr",
    )

    for (const value of values) {
        const cell = (
            document.createElement(
                "td",
            )
        )

        cell.textContent = (
            String(value)
        )

        row.append(cell)
    }

    return row
}
```

---

# 43. Category Table 렌더링

```javascript
function renderForecastItems(
    tbody,
    items,
) {
    tbody.replaceChildren()

    const fragment = (
        document.createDocumentFragment()
    )

    for (const item of items) {
        fragment.append(
            createRow([
                item.category,
                item.fcstTime,
                item.fcstValue,
            ]),
        )
    }

    tbody.append(fragment)
}
```

---

# 44. 시간별 그룹화

같은 `fcstTime`의 Category를 하나의 객체로 묶는다.

```javascript
function groupForecast(
    items,
) {
    return items.reduce(
        (
            grouped,
            item,
        ) => {
            const time = (
                item.fcstTime
            )

            grouped[time] ??= {}

            grouped[time][
                item.category
            ] = item.fcstValue

            return grouped
        },
        {},
    )
}
```

---

# 45. 그룹화 결과

```text
{
    "1000": {
        T1H: "20",
        REH: "80",
        RN1: "0",
    },
}
```

한 시간의 값을 한 Row로 출력할 수 있다.

---

# 46. 내 코드의 Category 오류

원본의 온도 열 조건:

```text
T1H 또는 REH
```

온도 열에 습도 값도 들어간다.

정확한 연결:

```text
온도
→ T1H

습도
→ REH

강수량
→ RN1
```

---

# 47. 내 코드의 시간 열 오류

T1H 항목에서만 시간을 출력하고 REH·RN1 항목은 별도 Row를 만든다.

결과:

```text
같은 시간
→ 세 개 Row로 분리
→ 일부 시간 칸 비어 있음
→ 값이 잘못된 Column에 배치
```

먼저 시간별로 그룹화해야 한다.

---

# 48. 시간별 Table 렌더링

```javascript
function renderGroupedForecast(
    tbody,
    grouped,
) {
    tbody.replaceChildren()

    const fragment = (
        document.createDocumentFragment()
    )

    for (
        const [
            time,
            values,
        ]
        of Object.entries(grouped)
    ) {
        fragment.append(
            createRow([
                time,
                values.T1H ?? "-",
                values.REH ?? "-",
                values.RN1 ?? "-",
            ]),
        )
    }

    tbody.append(fragment)
}
```

---

# 49. 재조회 누적 문제

강사님 원본은 기존 `q2` Row를 지우지 않고 Append한다.

Button을 여러 번 누르면 결과가 누적될 수 있다.

```javascript
tbody.replaceChildren()
```

로 먼저 초기화한다.

---

# 50. 회원정보 문제

요구사항:

```text
ID
Name
Zipcode
Company Name
```

강사님 코드는 요구사항만 있고 Listener 구현은 없다.

내 코드는 요청과 렌더링을 직접 구현했다.

---

# 51. 내 회원 Row 구조 오류

원본 흐름:

```text
빈 tr 생성
→ tbody에 append

td 문자열
→ tbody.innerHTML += 로 추가
```

문제:

- 빈 `tr`이 남음
- `td`가 `tr` 안에 명확히 들어가지 않음
- 매 반복마다 전체 `tbody` 재파싱
- 기존 Node 참조가 바뀔 수 있음
- 재조회하면 결과 누적

---

# 52. 올바른 Table 구조

```text
table
└── tbody
    └── tr
        ├── td
        ├── td
        ├── td
        └── td
```

---

# 53. 회원 Row 생성

```javascript
function createUserRow(
    user,
) {
    return createRow([
        user.id,
        user.name,
        user.address?.zipcode
            ?? "-",
        user.company?.name
            ?? "-",
    ])
}
```

---

# 54. 회원 Table 렌더링

```javascript
function renderUsers(
    tbody,
    users,
) {
    tbody.replaceChildren()

    const fragment = (
        document.createDocumentFragment()
    )

    for (const user of users) {
        fragment.append(
            createUserRow(user),
        )
    }

    tbody.append(fragment)
}
```

---

# 55. `try...catch`

원본:

```javascript
try {
    const value = undefined

    value.push(1)
} catch (
    error
) {
    console.error(error)
}
```

`undefined`에는 `push()`가 없어 `TypeError`가 발생한다.

---

# 56. 동기 오류와 비동기 오류

```text
동기 오류
→ 같은 try Block의 catch 가능

Promise Rejection
→ await를 try로 감싸거나 .catch() 사용
```

---

# 57. Fetch 기본 구조

```javascript
fetch(
    "https://jsonplaceholder.typicode.com/users",
)
    .then(
        response => (
            response.json()
        ),
    )
    .then(
        users => {
            console.log(users)
        },
    )
    .catch(
        error => {
            console.error(error)
        },
    )
```

---

# 58. Fetch 반환값

`fetch()`는 Promise를 반환한다.

첫 번째 `.then()`에는 `Response` 객체가 전달된다.

---

# 59. `response.json()`

```javascript
const promise = (
    response.json()
)
```

응답 Body를 읽고 JSON Parse하는 Promise를 반환한다.

---

# 60. Fetch Option 객체

```javascript
fetch(
    url,
    {
        method: "GET",
    },
)
```

두 번째 인수는 JSON 문자열이 아니라 JavaScript 객체다.

---

# 61. HTTP 오류 처리

Fetch는 404·500 같은 HTTP 응답을 자동으로 Reject하지 않을 수 있다.

```javascript
if (!response.ok) {
    throw new Error(
        `HTTP ${response.status}`,
    )
}
```

---

# 62. Promise Chain 개선

```javascript
fetch(url)
    .then(
        response => {
            if (!response.ok) {
                throw new Error(
                    `HTTP ${response.status}`,
                )
            }

            return response.json()
        },
    )
    .then(
        data => {
            console.log(data)
        },
    )
    .catch(
        error => {
            console.error(
                "요청 실패",
                error,
            )
        },
    )
```

---

# 63. `async/await`

```javascript
async function loadUsers() {
    const response = await fetch(
        "https://jsonplaceholder.typicode.com/users",
    )

    if (!response.ok) {
        throw new Error(
            `HTTP ${response.status}`,
        )
    }

    return response.json()
}
```

---

# 64. `try...catch`와 Await

```javascript
async function handleLoadUsers() {
    try {
        const users = (
            await loadUsers()
        )

        console.log(users)
    } catch (
        error
    ) {
        console.error(
            "회원정보 조회 실패",
            error,
        )
    }
}
```

---

# 65. Loading State

```javascript
button.disabled = true
message.textContent = (
    "불러오는 중입니다."
)
```

요청 완료 후 상태를 복구한다.

---

# 66. `finally`

```javascript
try {
    // 요청
} catch (
    error
) {
    // 오류
} finally {
    button.disabled = false
}
```

성공·실패와 관계없이 실행한다.

---

# 67. 빈 상태와 오류 상태

```text
Loading
→ 데이터를 불러오는 중

Success
→ N개의 결과

Empty
→ 결과 없음

Error
→ 불러오지 못함
```

Console만이 아니라 사용자 화면에도 상태를 표시한다.

---

# 68. 중복 요청 방지

```javascript
if (button.disabled) {
    return
}

button.disabled = true
```

같은 Button을 연속 클릭해 중복 요청이 발생하는 것을 줄인다.

---

# 69. AbortController

```javascript
const controller = (
    new AbortController()
)

fetch(
    url,
    {
        signal: controller.signal,
    },
)

controller.abort()
```

진행 중인 Fetch 요청을 취소할 수 있다.

---

# 70. 최신 요청만 유지

```javascript
let currentController = null

async function requestLatest(
    url,
) {
    currentController?.abort()

    currentController = (
        new AbortController()
    )

    try {
        const response = await fetch(
            url,
            {
                signal: (
                    currentController
                        .signal
                ),
            },
        )

        if (!response.ok) {
            throw new Error(
                `HTTP ${response.status}`,
            )
        }

        return await response.json()
    } finally {
        currentController = null
    }
}
```

검색 자동 완성처럼 이전 요청 결과가 최신 결과를 덮어쓰는 문제를 줄일 수 있다.

---

# 71. Abort 오류 처리

```javascript
async function handleLatestRequest(
    url,
) {
    try {
        return await requestLatest(
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

취소는 일반 실패와 구분한다.

---

# 72. 응답 Content Type 확인

```javascript
const contentType = (
    response.headers.get(
        "content-type",
    )
    ?? ""
)

if (
    !contentType.includes(
        "application/json",
    )
) {
    throw new Error(
        "JSON 응답이 아닙니다.",
    )
}
```

서버가 HTML 오류 페이지를 반환하는 상황을 감지할 수 있다.

---

# 73. POST JSON 요청

```javascript
const response = await fetch(
    "/api/users",
    {
        method: "POST",

        headers: {
            "Content-Type":
                "application/json",
        },

        body: JSON.stringify({
            name: "Kim",
        }),
    },
)
```

---

# 74. CORS

다른 Origin으로 요청할 때 Server의 CORS 정책 영향을 받는다.

```text
Protocol
Host
Port
```

Browser에서 CORS 오류가 발생하면 Client JavaScript만으로 해결할 수 없는 경우가 많다.

---

# 75. Debugger

```javascript
button.addEventListener(
    "click",
    () => {
        debugger

        console.log(
            "중단점 이후",
        )
    },
)
```

개발자 도구가 열려 있으면 해당 줄에서 실행을 일시 정지한다.

---

# 76. Debugger 확인 항목

- Scope 변수
- Call Stack
- Network 요청
- Breakpoint
- Step Over
- Step Into
- Step Out
- Watch Expression
- XHR·Fetch Breakpoint

---

# 77. 중복 객체 Key

강사님 코드:

```javascript
const data = {
    a: 1,
    b: 2,
    a: 3,
}
```

결과:

```text
{
    a: 3,
    b: 2,
}
```

뒤의 `a: 3`이 앞의 값을 덮어쓴다.

---

# 78. Counting Pattern

```javascript
counts[key] = (
    counts[key] ?? 0
) + 1
```

Key가 없으면 0에서 시작하고 있으면 기존 값에 1을 더한다.

---

# 79. HTML 문구 차이

내 Button:

```text
19_jason.html
```

실제 요청 URL:

```text
19_json.html
```

표시 문구의 `jason`은 오타다.

---

# 80. 문서 기본 정보

원본:

```html
<html lang="en">
<title>Document</title>
```

개선:

```html
<html lang="ko">
<title>AJAX와 Fetch API</title>
```

---

# 81. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| AJAX 설명 | 상세 주석 | 핵심 중심 |
| `btn2` 문구 | `jason` 오타 | `json` |
| User 출력 | 배열 전체 중심 | 특정 User 중심 |
| Weather Key | 빈 값 | 값 포함 |
| 문제 1 | Div Layout | Semantic Table |
| 문제 2 | 시간별 Grouping 미완성 | 객체 Grouping |
| 온도 조건 | T1H·REH | T1H |
| 습도 조건 | T1H | REH |
| 강수량 조건 | T1H | RN1 |
| 회원 Table | 직접 구현·구조 오류 | 미구현 |
| Fetch | 동일 흐름 | 동일 흐름 |
| Duplicate Key | 없음 | 예제 존재 |

## 81-1. 내 코드의 장점

- AJAX와 Navigation 차이를 자세히 기록했다.
- XHR의 네 단계를 직접 확인했다.
- 요청 직후 응답이 비어 있는 현상을 확인했다.
- Weather Category를 직접 필터링했다.
- 회원정보 조회와 Table 출력까지 시도했다.
- Fetch·Promise·`try...catch` 흐름을 설명했다.
- Debugger 실습을 포함했다.

## 81-2. 내 코드의 개선점

- Button 문구에 `jason` 오타가 있다.
- Weather API Key가 빈 값이다.
- UTC 날짜와 자정 문제를 처리하지 않는다.
- HTTP Endpoint를 사용한다.
- XHR Status·Network Error를 처리하지 않는다.
- Weather Grouping 없이 Category를 잘못된 Column에 넣는다.
- 회원 Table에서 빈 Row와 `tbody.innerHTML +=`를 사용한다.
- 재조회 시 기존 결과가 누적된다.
- Fetch에서 `response.ok`를 검사하지 않는다.
- Fetch Option 객체를 JSON이라고 부른다.

## 81-3. 강사님 코드의 장점

- XHR 기본 순서가 명확하다.
- User JSON Parse와 중첩 Property 접근이 간결하다.
- Weather Category Filter와 시간별 Grouping을 구현한다.
- Table Row 구조가 비교적 올바르다.
- Promise Chain과 Debugger를 연결한다.
- 중복 Key 동작을 확인한다.

## 81-4. 강사님 코드의 보충점

- API Key를 Client 코드에 포함한다.
- HTTP Endpoint와 UTC·자정 문제가 있다.
- XHR Status·Error 처리가 없다.
- Weather Table 재조회 시 Row가 누적된다.
- 회원정보 문제를 구현하지 않는다.
- Fetch에서 `response.ok` 검사가 없다.
- Counting 주석이 구현되지 않았다.

---

# 82. 기존 코드에서 개선한 이유

## 82-1. XHR 응답 검사

기존:

```javascript
xhr.onload = () => {
    const data = JSON.parse(
        xhr.responseText,
    )
}
```

개선:

```javascript
xhr.onload = () => {
    if (
        xhr.status < 200
        || xhr.status >= 300
    ) {
        return
    }

    // Parse
}
```

## 82-2. Weather Grouping

기존:

```text
Item 하나마다 Row 생성
```

개선:

```text
fcstTime 기준 Grouping
→ 한 시간당 한 Row
```

## 82-3. 회원 Table

기존:

```javascript
tbody.innerHTML += (
    "<td>...</td>"
)
```

개선:

```javascript
row.append(cell)
tbody.append(row)
```

## 82-4. Fetch HTTP 오류

기존:

```javascript
return response.json()
```

개선:

```javascript
if (!response.ok) {
    throw new Error(
        `HTTP ${response.status}`,
    )
}

return response.json()
```

---

# 83. 실무형 예제: 회원 API Viewer

```javascript
function createUserRow(
    user,
) {
    const row = document.createElement(
        "tr",
    )

    const values = [
        user.id,
        user.name,
        user.address?.zipcode
            ?? "-",
        user.company?.name
            ?? "-",
    ]

    for (const value of values) {
        const cell = (
            document.createElement(
                "td",
            )
        )

        cell.textContent = (
            String(value)
        )

        row.append(cell)
    }

    return row
}

async function loadAndRenderUsers({
    button,
    tbody,
    message,
}) {
    if (button.disabled) {
        return
    }

    button.disabled = true
    message.textContent = (
        "회원정보를 불러오는 중입니다."
    )

    tbody.replaceChildren()

    try {
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/users",
        )

        if (!response.ok) {
            throw new Error(
                `HTTP ${response.status}`,
            )
        }

        const users = (
            await response.json()
        )

        if (!Array.isArray(users)) {
            throw new TypeError(
                "회원 목록 형식이 아닙니다.",
            )
        }

        const fragment = (
            document
                .createDocumentFragment()
        )

        for (const user of users) {
            fragment.append(
                createUserRow(user),
            )
        }

        tbody.append(fragment)

        message.textContent = (
            users.length === 0
                ? "회원정보가 없습니다."
                : `${users.length}명을 `
                    + "불러왔습니다."
        )
    } catch (
        error
    ) {
        message.textContent = (
            "회원정보를 불러오지 "
            + "못했습니다."
        )

        console.error(error)
    } finally {
        button.disabled = false
    }
}
```

## 83-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `async/await` | 요청 흐름을 순서대로 표현 |
| `response.ok` | HTTP Status 검증 |
| 배열 검사 | 응답 데이터 구조 검증 |
| `textContent` | 외부 데이터를 안전하게 출력 |
| `DocumentFragment` | 여러 Row를 한 번에 삽입 |
| `replaceChildren()` | 재조회 중복 방지 |
| Disabled 상태 | 중복 요청 방지 |
| `finally` | 성공·실패 후 Button 복구 |
| Empty 상태 | 결과 0건과 오류 구분 |

---

# 84. 대표 오류로 이해하기

## 84-1. `send()` 직후 응답 사용

응답이 아직 도착하지 않아 빈 문자열일 수 있다.

## 84-2. `onload`를 무조건 성공으로 처리

HTTP 404·500도 들어올 수 있다.

## 84-3. JSON이 아닌 응답 Parse

`SyntaxError`가 발생한다.

## 84-4. 자정에 Hour만 1 감소

Date와 Time이 서로 맞지 않는다.

## 84-5. Weather Category를 잘못된 열에 배치

의미가 다른 측정값이 섞인다.

## 84-6. `tbody`에 `td` 직접 추가

올바른 Table 구조가 아니다.

---

# 85. 자주 하는 실수

## 85-1. `open()`이 요청을 전송한다고 생각

실제 전송은 `send()`다.

## 85-2. 상대 URL 기준을 JS 파일 위치로 생각

현재 Document URL 기준이다.

## 85-3. `toISOString()`을 Local 날짜로 생각

UTC 기준이다.

## 85-4. API Key를 Public Frontend에 직접 작성

사용자에게 노출된다.

## 85-5. HTTP API를 HTTPS 페이지에서 호출

Mixed Content로 차단될 수 있다.

## 85-6. 시간별 데이터를 Grouping하지 않음

같은 시간의 값을 한 Row에 맞추기 어렵다.

## 85-7. 반복문에서 `innerHTML +=` 사용

하위 DOM 전체가 반복해서 재파싱될 수 있다.

## 85-8. Fetch Catch가 404도 처리한다고 생각

`response.ok`를 직접 검사한다.

## 85-9. JSON Parse 성공만 확인

응답의 실제 자료형·Property도 검증한다.

## 85-10. 요청 상태 UI를 만들지 않음

Loading·Empty·Error·Success를 구분한다.

---

# 86. 핵심 요약

```text
AJAX
→ 현재 페이지 유지
→ 비동기 데이터 요청
→ 일부 DOM 갱신
```

```text
XMLHttpRequest
→ 생성
→ open
→ send
→ load·error 처리
```

```text
responseText
→ 문자열

JSON.parse()
→ JavaScript 값
```

```text
fetch()
→ Promise<Response>

response.json()
→ Promise<JavaScript 값>
```

```text
response.ok
→ HTTP 성공 확인

try...catch
→ Await 오류 처리

finally
→ UI 상태 복구
```

---

# 87. 최종 체크리스트

- [ ] AJAX의 의미를 설명할 수 있는가?
- [ ] 일반 Navigation과 AJAX를 구분할 수 있는가?
- [ ] XHR의 생성·Open·Send·응답 순서를 이해했는가?
- [ ] `open()`이 요청 설정이라는 점을 이해했는가?
- [ ] `send()` 직후 응답이 비어 있을 수 있음을 이해했는가?
- [ ] XHR Status를 확인하는가?
- [ ] `error`와 `timeout`을 처리하는가?
- [ ] JSON Parse 오류를 처리할 수 있는가?
- [ ] 상대 URL 기준이 Document임을 이해했는가?
- [ ] 외부 응답 구조를 검증하는가?
- [ ] Local 날짜와 UTC 날짜를 구분하는가?
- [ ] 자정 이전 시각을 Date 연산으로 처리하는가?
- [ ] API Key를 Frontend에 노출하지 않는가?
- [ ] HTTPS Endpoint를 사용하는가?
- [ ] `URLSearchParams`로 Query를 구성할 수 있는가?
- [ ] Weather Category를 정확하게 필터링하는가?
- [ ] 시간별로 데이터를 그룹화할 수 있는가?
- [ ] 없는 Category에 기본값을 표시하는가?
- [ ] 재조회 전에 기존 Table을 비우는가?
- [ ] `tbody → tr → td` 구조를 지키는가?
- [ ] `innerHTML +=` 반복을 피하는가?
- [ ] Fetch가 Promise를 반환함을 이해했는가?
- [ ] `response.json()`도 Promise임을 이해했는가?
- [ ] `response.ok`를 검사하는가?
- [ ] Network 오류와 HTTP 오류를 구분하는가?
- [ ] `async/await`와 `try...catch`를 사용할 수 있는가?
- [ ] Loading·Success·Empty·Error 상태를 표시하는가?
- [ ] 중복 요청을 방지하거나 취소할 수 있는가?
- [ ] 외부 데이터 출력에 `textContent`를 사용하는가?
- [ ] `debugger`와 Network Panel로 요청을 추적할 수 있는가?

---

# 마무리

AJAX와 Fetch의 핵심은 서버에서 JSON을 가져오는 것에서 끝나지 않는다.

```text
요청 시작과 응답 완료 시점을 구분하고
    ↓
HTTP·Network·Parse 오류를 각각 처리하고
    ↓
외부 데이터 구조를 검증하고
    ↓
필요한 형태로 Filter·Grouping한 뒤
    ↓
안전한 DOM 구조와 명확한 UI 상태로 렌더링하는 것
```

이 흐름을 이해하면 실제 프로젝트에서 회원 목록·검색 결과·날씨·상품·게시글 같은 서버 데이터를 안정적으로 화면에 연결할 수 있다.
