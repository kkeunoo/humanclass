---
title: JavaScript AJAX와 Fetch API
version: v4.0-detailed-source
last_updated: 2026-09-17
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
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 20번은 HTML과 연결된 외부 JavaScript 파일을 함께 확인한다.  
> 강사님 코드는 `XMLHttpRequest`, 기상청 초단기예보, 시간별 그룹화, Fetch 흐름을 구현하고, 내 코드는 회원 Table과 날씨 출력 문제를 추가로 시도했다. 이 문서에서는 실제 오류를 보존해 비교한 뒤 안전한 구현으로 개선한다.

---

## 이 문서에서 바로 찾기

- [개념에서 실제 실행까지: AJAX는 문서 전체 이동 없이 요청·응답으로 일부 화면을 갱신한다](#js-20-section-4)
- [81. 내 코드와 강사님 코드 비교](#js-20-section-85)
- [83. 실무형 예제: 회원 API Viewer](#js-20-section-87)
- [84. 대표 오류로 이해하기](#js-20-section-88)
- [85. 자주 하는 실수](#js-20-section-89)
- [86. 핵심 요약](#js-20-section-90)
- [87. 최종 체크리스트](#js-20-section-91)

<details>
<summary>세부 목차 펼치기 — 번호형 본문 전체</summary>

- [개요](#js-20-section-1)
- [핵심 개념](#js-20-section-2)
- [학습 목표](#js-20-section-3)
- [개념에서 실제 실행까지: AJAX는 문서 전체 이동 없이 요청·응답으로 일부 화면을 갱신한다](#js-20-section-4)
- [1. AJAX란?](#js-20-section-5)
- [2. 일반 이동과 AJAX](#js-20-section-6)
- [3. AJAX 응답 형식](#js-20-section-7)
- [4. 원본 초기화](#js-20-section-8)
- [5. `XMLHttpRequest` 기본 순서](#js-20-section-9)
- [6. 객체 생성](#js-20-section-10)
- [7. `open()`](#js-20-section-11)
- [8. `open()`의 인수](#js-20-section-12)
- [9. `send()`](#js-20-section-13)
- [10. `onload`](#js-20-section-14)
- [11. `onload`와 HTTP 성공](#js-20-section-15)
- [12. `responseText`](#js-20-section-16)
- [13. 비동기 직후 응답](#js-20-section-17)
- [14. 실제 실행 흐름](#js-20-section-18)
- [15. `readystatechange`](#js-20-section-19)
- [16. ReadyState](#js-20-section-20)
- [17. Network Error](#js-20-section-21)
- [18. Timeout](#js-20-section-22)
- [19. 안전한 XHR 함수](#js-20-section-23)
- [20. 상대 URL 기준](#js-20-section-24)
- [21. JSON Parse](#js-20-section-25)
- [22. 두 번째 사용자 이름](#js-20-section-26)
- [23. 중첩 Property](#js-20-section-27)
- [24. 외부 데이터 변경 가능성](#js-20-section-28)
- [25. Optional Chaining](#js-20-section-29)
- [26. 회원 데이터 검증](#js-20-section-30)
- [27. 기상청 요청 날짜](#js-20-section-31)
- [28. UTC 날짜 문제](#js-20-section-32)
- [29. Local 날짜 함수](#js-20-section-33)
- [30. 원본 Base Time](#js-20-section-34)
- [31. 자정 오류](#js-20-section-35)
- [32. 발표 시각 계산](#js-20-section-36)
- [33. API Key 차이](#js-20-section-37)
- [34. Frontend API Key 노출](#js-20-section-38)
- [35. API Endpoint](#js-20-section-39)
- [36. Query Parameter](#js-20-section-40)
- [37. `URLSearchParams`](#js-20-section-41)
- [38. 응답 구조](#js-20-section-42)
- [39. Weather Category](#js-20-section-43)
- [40. Category Filter](#js-20-section-44)
- [41. 원본 문제 1](#js-20-section-45)
- [42. 안전한 Category Row](#js-20-section-46)
- [43. Category Table 렌더링](#js-20-section-47)
- [44. 시간별 그룹화](#js-20-section-48)
- [45. 그룹화 결과](#js-20-section-49)
- [46. 내 코드의 Category 오류](#js-20-section-50)
- [47. 내 코드의 시간 열 오류](#js-20-section-51)
- [48. 시간별 Table 렌더링](#js-20-section-52)
- [49. 재조회 누적 문제](#js-20-section-53)
- [50. 회원정보 문제](#js-20-section-54)
- [51. 내 회원 Row 구조 오류](#js-20-section-55)
- [52. 올바른 Table 구조](#js-20-section-56)
- [53. 회원 Row 생성](#js-20-section-57)
- [54. 회원 Table 렌더링](#js-20-section-58)
- [55. `try...catch`](#js-20-section-59)
- [56. 동기 오류와 비동기 오류](#js-20-section-60)
- [57. Fetch 기본 구조](#js-20-section-61)
- [58. Fetch 반환값](#js-20-section-62)
- [59. `response.json()`](#js-20-section-63)
- [60. Fetch Option 객체](#js-20-section-64)
- [61. HTTP 오류 처리](#js-20-section-65)
- [62. Promise Chain 개선](#js-20-section-66)
- [63. `async/await`](#js-20-section-67)
- [64. `try...catch`와 Await](#js-20-section-68)
- [65. Loading State](#js-20-section-69)
- [66. `finally`](#js-20-section-70)
- [67. 빈 상태와 오류 상태](#js-20-section-71)
- [68. 중복 요청 방지](#js-20-section-72)
- [69. AbortController](#js-20-section-73)
- [70. 최신 요청만 유지](#js-20-section-74)
- [71. Abort 오류 처리](#js-20-section-75)
- [72. 응답 Content Type 확인](#js-20-section-76)
- [73. POST JSON 요청](#js-20-section-77)
- [74. CORS](#js-20-section-78)
- [75. Debugger](#js-20-section-79)
- [76. Debugger 확인 항목](#js-20-section-80)
- [77. 중복 객체 Key](#js-20-section-81)
- [78. Counting Pattern](#js-20-section-82)
- [79. HTML 문구 차이](#js-20-section-83)
- [80. 문서 기본 정보](#js-20-section-84)
- [81. 내 코드와 강사님 코드 비교](#js-20-section-85)
- [82. 기존 코드에서 개선한 이유](#js-20-section-86)
- [83. 실무형 예제: 회원 API Viewer](#js-20-section-87)
- [84. 대표 오류로 이해하기](#js-20-section-88)
- [85. 자주 하는 실수](#js-20-section-89)
- [86. 핵심 요약](#js-20-section-90)
- [87. 최종 체크리스트](#js-20-section-91)
- [마무리](#js-20-section-92)
- [V3 실행 추적 카드 — 요청 생성 → 서버 처리 → Response → 본문 변환 → DOM](#js-20-section-93)

</details>

---

<a id="js-20-section-1"></a>

## 개요

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

<a id="js-20-section-2"></a>

## 핵심 개념

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

<a id="js-20-section-3"></a>

## 학습 목표

- 요청 전송·HTTP 상태·본문 파싱·출력을 분리한다.
- 원본의 해당 부분을 찾아 실행 순서와 결과를 다시 확인한다.

---

<a id="js-20-section-4"></a>

## 개념에서 실제 실행까지: AJAX는 문서 전체 이동 없이 요청·응답으로 일부 화면을 갱신한다

XHR open은 요청 설정, send는 전송 시작, onload는 응답 전송이 완료되어 결과를 사용할 시점이다. send 직후 responseText는 아직 빈 문자열일 수 있다. fetch도 Promise를 주고, Response를 얻은 뒤 response.json으로 본문을 비동기 파싱한다.

두 원본의 상대 주소 19_json.html은 외부 JS가 있는 asset/js 폴더가 아니라 문서의 base URL 기준으로 해석된다. 내 사용자 표는 tr을 만든 뒤 tbody에 td 문자열을 직접 더해 행 구조가 틀어질 수 있다. 강사님 날씨 묶음은 fcstTime을 키로 카테고리 값을 모으고, 내 코드는 개별 행의 같은 값을 온도·습도에 넣어 잘못된 표를 만들 수 있다. 💡 여러 날짜이면 fcstDate+fcstTime을 키로 사용한다.

응답이 HTTP400/500이어도 XHR load나 fetch fulfilled가 발생할 수 있다. 상태 검사→파싱→스키마 검사→화면 출력으로 나눠야 한다. JSON 파싱 오류, HTTP 오류, 네트워크/CORS 실패는 원인과 확인 위치가 다르다. 기상청 기준시각은 UTC ISO 날짜와 로컬 시각을 섞지 말고, 자정 이전 날짜 보정·발표시각 규칙까지 확인해야 한다.

### 수업 원본에서 사용한 부분

아래는 전체 실행 파일이 아니라 **개념에 대응하는 문맥 발췌**다. 나머지 HTML·선언·등록 코드는 원본과 기존 번호형 본문에서 이어 확인한다. 

내 코드: `workspace_html/javascript/asset/js/20_ajax.js`

```javascript
// 2_보낼 준비 방식(method), 주소(url)
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')

        // 3_보내기
        xhr.send()

        // 4_결과 받기 및 활용, 갔다 오면~이기 때문에 콜백함수 이용
        xhr.onload = function() {
```

강사님 코드: `workspace_teacher/workspace_html/javascript/asset/js/20_ajax.js`

```javascript
// 방식method, 주소
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')

        // 3. 보내기
        xhr.send()

        // 4. 결과 활용
        xhr.onload = function(){
```

### 직접 재현하는 최소 예제와 결과

이 예제는 **이번 리팩토링의 설명용 재구성**이다. 원본 그대로의 발췌와 구별한다. 외부 통신 없이 Console에서 실행한다. 다른 예제의 변수와 섞이지 않게 새 실행 문맥에서 실행한다.

```javascript
const items = [
  {fcstDate:"20260716", fcstTime:"0900", category:"T1H", fcstValue:"28"},
  {fcstDate:"20260716", fcstTime:"0900", category:"REH", fcstValue:"80"}
];
const grouped = {};
for (const item of items) {
  const key = item.fcstDate + item.fcstTime;
  grouped[key] ??= {};
  grouped[key][item.category] = item.fcstValue;
}
console.log(JSON.stringify(grouped));
```

예상 출력:

```text
{"202607160900":{"T1H":"28","REH":"80"}}
```

### 결과를 역추적하는 방법

고정 데이터 계산이라 실제 날씨 조회가 아니다. CORS는 scheme·host·port로 결정되는 origin에 대한 브라우저 응답 접근 정책이며 서버가 허용해야 한다. no-cors는 JSON을 읽는 해결책이 아니다. [Fetch 표준](https://fetch.spec.whatwg.org/)에 따라 HTTP 상태와 응답 접근을 분리한다.

출력은 아래의 확인 경로로 추적한다. return 값은 호출자에게 전달되고 자동으로 화면에 표시되지 않는다. Console 로그, DOM 변경, 저장소 변경, 서버 응답은 별개 단계다.

| 확인할 단계 | 이 예제에서 볼 것 |
| --- | --- |
| 입력 | 리터럴·현재 폼 값·이벤트 인수·응답 중 출처를 위 설명과 대조 |
| 실행 | 각 줄 또는 콜백이 지금 실행되는지, 나중에 실행되는지 구분 |
| 결과 | 위 예상 출력과 현재 값·자료형을 함께 대조 |
| 오류 | 첫 오류 줄의 입력과 직전 상태를 확인하고 뒤 로그 누락 원인 추적 |

### 단계별 복습 실습과 정답

**기본 실습:** HTTP500 HTML을받은fetch에서 상태검사없이response.json을한상황을 진단한다.

**응용·디버깅 실습:** 두날짜의같은0900 날씨를묶는키를정한다.

**통합 확인:** 위 최소 예제를 새 문맥에서 작성하고 정상값·빈 값·경계값으로 실행한다. 원본에서 대응하는 선언·호출·콜백을 찾아 위에 나타난 차이가 무엇을 바꾸는지 설명한다. 아래 정답은 먼저 예측한 뒤 펼친다. 이 실습은 💡 설명용 보강이며 원본에 모두 완성되어 있다는 뜻은 아니다.

<details>
<summary>정답과 처리 순서 해설</summary>

1. fetch는HTTP500만으로reject하지않는다. 먼저response.ok/status검사,본문형식검사를한다. parse오류와HTTP실패를구분한다.
2. fcstDate+fcstTime을쓴다. 시간만쓰면서로다른날짜가덮어쓸수있다.
3. 최소 예제의 예상 출력과 한 줄씩 대조한다. 값이 다른 경우 입력 → 형 변환 → 분기/상태 변경 → 출력 순서로 첫 차이를 찾는다. DOM·API 예제는 Console 값만 아니라 화면·Elements·Network가 서로 같은 상태를 말하는지도 점검한다.

</details>

### 복습 질문과 해설

**질문:** JSON.parse에서 Unexpected token '<'가 나오면?

**해설:** 응답이 JSON 대신 HTML 오류·로그인 페이지일 수 있다. Network에서 상태와 Content-Type 및 실제 응답 본문부터 확인한다.

**한 번 더 확인:** 예제의 입력을 하나 바꾸고 결과를 먼저 예상한 뒤 실행한다. 정상 입력만 아니라 비어 있는 값, 경계값, 두 번 실행했을 때의 상태를 기존 실습·오류 절에서 반복 확인한다.

---

<a id="js-20-section-5"></a>

## 1. AJAX란?

```text
Asynchronous JavaScript And XML
```

이름에는 XML이 포함되지만 현대 웹에서는 JSON 응답을 더 자주 사용한다.

핵심은 데이터 형식보다 현재 페이지를 유지한 비동기 통신이다.

---

<a id="js-20-section-6"></a>

## 2. 일반 이동과 AJAX

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

<a id="js-20-section-7"></a>

## 3. AJAX 응답 형식

응답은 문자열만 가능한 것이 아니다.

- JSON
- Text
- HTML
- Blob
- ArrayBuffer
- Form Data
- Image·File Binary

---

<a id="js-20-section-8"></a>

## 4. 원본 초기화

```javascript
window.addEventListener(
    "load",
    bind,
)
```

Load가 끝난 뒤 Button을 선택하고 Click Listener를 등록한다.

DOM만 필요하면 `defer`와 초기화 함수를 사용할 수 있다.

---

<a id="js-20-section-9"></a>

## 5. `XMLHttpRequest` 기본 순서

```text
1. 객체 생성
2. Method·URL 설정
3. 요청 전송
4. 응답 완료 후 처리
```

---

<a id="js-20-section-10"></a>

## 6. 객체 생성

```javascript
const xhr = (
    new XMLHttpRequest()
)
```

요청 상태와 응답 정보를 관리하는 객체를 만든다.

---

<a id="js-20-section-11"></a>

## 7. `open()`

```javascript
xhr.open(
    "GET",
    "https://jsonplaceholder.typicode.com/users",
)
```

요청 정보를 설정한다.

이 단계에서는 실제 Network 요청을 보내지 않는다.

---

<a id="js-20-section-12"></a>

## 8. `open()`의 인수

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

<a id="js-20-section-13"></a>

## 9. `send()`

```javascript
xhr.send()
```

설정한 요청을 실제 전송한다.

GET 요청은 일반적으로 Body 없이 호출한다.

---

<a id="js-20-section-14"></a>

## 10. `onload`

```javascript
xhr.onload = function () {
    console.log(
        xhr.responseText,
    )
}
```

응답 Body를 읽을 수 있는 상태가 되면 실행된다.

---

<a id="js-20-section-15"></a>

## 11. `onload`와 HTTP 성공

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

<a id="js-20-section-16"></a>

## 12. `responseText`

```javascript
console.log(
    xhr.responseText,
)
```

응답 Body를 문자열로 제공한다.

JSON 응답도 처음에는 문자열이다.

---

<a id="js-20-section-17"></a>

## 13. 비동기 직후 응답

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

<a id="js-20-section-18"></a>

## 14. 실제 실행 흐름

```text
send()
→ Network 요청 시작
→ 다음 동기 코드 실행
→ ResponseText 아직 빈 값
→ 응답 도착
→ onload Callback 실행
```

---

<a id="js-20-section-19"></a>

## 15. `readystatechange`

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

<a id="js-20-section-20"></a>

## 16. ReadyState

| 값 | 상태 |
| ---: | --- |
| `0` | UNSENT |
| `1` | OPENED |
| `2` | HEADERS_RECEIVED |
| `3` | LOADING |
| `4` | DONE |

현대 코드에서는 `load`, `error`, `timeout` Event를 나누어 처리하는 편이 읽기 쉽다.

---

<a id="js-20-section-21"></a>

## 17. Network Error

```javascript
xhr.onerror = function () {
    console.error(
        "Network 요청 실패",
    )
}
```

연결 실패·DNS·CORS 같은 Network 문제를 처리한다.

---

<a id="js-20-section-22"></a>

## 18. Timeout

```javascript
xhr.timeout = 5000

xhr.ontimeout = function () {
    console.error(
        "요청 시간이 초과되었습니다.",
    )
}
```

---

<a id="js-20-section-23"></a>

## 19. 안전한 XHR 함수

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

<a id="js-20-section-24"></a>

## 20. 상대 URL 기준

원본:

```javascript
xhr.open(
    "GET",
    "19_json.html",
)
```

상대 URL은 외부 JavaScript 파일의 위치가 아니라 현재 Document URL을 기준으로 해석된다.

---

<a id="js-20-section-25"></a>

## 21. JSON Parse

```javascript
const users = JSON.parse(
    xhr.responseText,
)
```

JSON 문자열을 JavaScript 배열로 변환한다.

---

<a id="js-20-section-26"></a>

## 22. 두 번째 사용자 이름

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

<a id="js-20-section-27"></a>

## 23. 중첩 Property

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

<a id="js-20-section-28"></a>

## 24. 외부 데이터 변경 가능성

JSONPlaceholder처럼 학습용 서비스도 응답·가용성이 변경될 수 있다.

실무 코드에서는 다음을 검증한다.

- 배열인지
- 필요한 Index가 있는지
- 중첩 객체가 있는지
- 필요한 Property의 자료형
- 빈 배열·빈 문자열 여부

---

<a id="js-20-section-29"></a>

## 25. Optional Chaining

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

<a id="js-20-section-30"></a>

## 26. 회원 데이터 검증

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

<a id="js-20-section-31"></a>

## 27. 기상청 요청 날짜

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

<a id="js-20-section-32"></a>

## 28. UTC 날짜 문제

`toISOString()`은 UTC 기준이다.

한국 Local 날짜가 필요한 API에서는 새벽 시간대에 날짜가 다르게 계산될 수 있다.

---

<a id="js-20-section-33"></a>

## 29. Local 날짜 함수

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

<a id="js-20-section-34"></a>

## 30. 원본 Base Time

```javascript
let hour = (
    new Date().getHours() - 1
)
```

한 시간 전의 `HH00`을 만들려는 코드다.

---

<a id="js-20-section-35"></a>

## 31. 자정 오류

현재 시각이 0시라면:

```text
hour
→ -1
```

잘못된 Base Time이 만들어지고 날짜도 전날로 조정되지 않는다.

---

<a id="js-20-section-36"></a>

## 32. 발표 시각 계산

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

<a id="js-20-section-37"></a>

## 33. API Key 차이

```text
강사님 코드
→ Service Key 값 포함

내 코드
→ 빈 문자열
```

강사님 Key 원문은 문서에 다시 노출하지 않는다.

---

<a id="js-20-section-38"></a>

## 34. Frontend API Key 노출

Browser JavaScript에 Key를 넣으면 Source·Network에서 확인할 수 있다.

보호가 필요한 Key는 Backend·Proxy·Serverless Function에서 관리한다.

---

<a id="js-20-section-39"></a>

## 35. API Endpoint

원본은 HTTP Endpoint를 사용한다.

```text
http://apis.data.go.kr/...
```

HTTPS 페이지에서는 Mixed Content로 차단될 수 있다.

서비스가 지원한다면 HTTPS를 사용한다.

---

<a id="js-20-section-40"></a>

## 36. Query Parameter

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

<a id="js-20-section-41"></a>

## 37. `URLSearchParams`

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

<a id="js-20-section-42"></a>

## 38. 응답 구조

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

<a id="js-20-section-43"></a>

## 39. Weather Category

```text
T1H
→ 기온

REH
→ 습도

RN1
→ 1시간 강수량
```

---

<a id="js-20-section-44"></a>

## 40. Category Filter

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

<a id="js-20-section-45"></a>

## 41. 원본 문제 1

강사님은 Category·예측 시간·값을 Table에 출력한다.

```text
Category
Forecast Time
Forecast Value
```

내 코드는 같은 데이터를 `div`와 `inline-block`으로 표시한다.

표 형태 데이터라면 의미 구조가 있는 `<table>`이 적합하다.

---

<a id="js-20-section-46"></a>

## 42. 안전한 Category Row

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

<a id="js-20-section-47"></a>

## 43. Category Table 렌더링

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

<a id="js-20-section-48"></a>

## 44. 시간별 그룹화

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

<a id="js-20-section-49"></a>

## 45. 그룹화 결과

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

<a id="js-20-section-50"></a>

## 46. 내 코드의 Category 오류

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

<a id="js-20-section-51"></a>

## 47. 내 코드의 시간 열 오류

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

<a id="js-20-section-52"></a>

## 48. 시간별 Table 렌더링

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

<a id="js-20-section-53"></a>

## 49. 재조회 누적 문제

강사님 원본은 기존 `q2` Row를 지우지 않고 Append한다.

Button을 여러 번 누르면 결과가 누적될 수 있다.

```javascript
tbody.replaceChildren()
```

로 먼저 초기화한다.

---

<a id="js-20-section-54"></a>

## 50. 회원정보 문제

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

<a id="js-20-section-55"></a>

## 51. 내 회원 Row 구조 오류

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

<a id="js-20-section-56"></a>

## 52. 올바른 Table 구조

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

<a id="js-20-section-57"></a>

## 53. 회원 Row 생성

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

<a id="js-20-section-58"></a>

## 54. 회원 Table 렌더링

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

<a id="js-20-section-59"></a>

## 55. `try...catch`

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

<a id="js-20-section-60"></a>

## 56. 동기 오류와 비동기 오류

```text
동기 오류
→ 같은 try Block의 catch 가능

Promise Rejection
→ await를 try로 감싸거나 .catch() 사용
```

---

<a id="js-20-section-61"></a>

## 57. Fetch 기본 구조

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

<a id="js-20-section-62"></a>

## 58. Fetch 반환값

`fetch()`는 Promise를 반환한다.

첫 번째 `.then()`에는 `Response` 객체가 전달된다.

---

<a id="js-20-section-63"></a>

## 59. `response.json()`

```javascript
const promise = (
    response.json()
)
```

응답 Body를 읽고 JSON Parse하는 Promise를 반환한다.

---

<a id="js-20-section-64"></a>

## 60. Fetch Option 객체

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

<a id="js-20-section-65"></a>

## 61. HTTP 오류 처리

Fetch는 404·500 같은 HTTP 응답을 자동으로 Reject하지 않을 수 있다.

```javascript
if (!response.ok) {
    throw new Error(
        `HTTP ${response.status}`,
    )
}
```

---

<a id="js-20-section-66"></a>

## 62. Promise Chain 개선

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

<a id="js-20-section-67"></a>

## 63. `async/await`

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

<a id="js-20-section-68"></a>

## 64. `try...catch`와 Await

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

<a id="js-20-section-69"></a>

## 65. Loading State

```javascript
button.disabled = true
message.textContent = (
    "불러오는 중입니다."
)
```

요청 완료 후 상태를 복구한다.

---

<a id="js-20-section-70"></a>

## 66. `finally`

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

<a id="js-20-section-71"></a>

## 67. 빈 상태와 오류 상태

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

<a id="js-20-section-72"></a>

## 68. 중복 요청 방지

```javascript
if (button.disabled) {
    return
}

button.disabled = true
```

같은 Button을 연속 클릭해 중복 요청이 발생하는 것을 줄인다.

---

<a id="js-20-section-73"></a>

## 69. AbortController

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

<a id="js-20-section-74"></a>

## 70. 최신 요청만 유지

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

<a id="js-20-section-75"></a>

## 71. Abort 오류 처리

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

<a id="js-20-section-76"></a>

## 72. 응답 Content Type 확인

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

<a id="js-20-section-77"></a>

## 73. POST JSON 요청

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

<a id="js-20-section-78"></a>

## 74. CORS

다른 Origin으로 요청할 때 Server의 CORS 정책 영향을 받는다.

```text
Protocol
Host
Port
```

Browser에서 CORS 오류가 발생하면 Client JavaScript만으로 해결할 수 없는 경우가 많다.

---

<a id="js-20-section-79"></a>

## 75. Debugger

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

<a id="js-20-section-80"></a>

## 76. Debugger 확인 항목

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

<a id="js-20-section-81"></a>

## 77. 중복 객체 Key

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

<a id="js-20-section-82"></a>

## 78. Counting Pattern

```javascript
counts[key] = (
    counts[key] ?? 0
) + 1
```

Key가 없으면 0에서 시작하고 있으면 기존 값에 1을 더한다.

---

<a id="js-20-section-83"></a>

## 79. HTML 문구 차이

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

<a id="js-20-section-84"></a>

## 80. 문서 기본 정보

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

<a id="js-20-section-85"></a>

## 81. 내 코드와 강사님 코드 비교

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

### 81-1. 내 코드의 장점

- AJAX와 Navigation 차이를 자세히 기록했다.
- XHR의 네 단계를 직접 확인했다.
- 요청 직후 응답이 비어 있는 현상을 확인했다.
- Weather Category를 직접 필터링했다.
- 회원정보 조회와 Table 출력까지 시도했다.
- Fetch·Promise·`try...catch` 흐름을 설명했다.
- Debugger 실습을 포함했다.

### 81-2. 내 코드의 개선점

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

### 81-3. 강사님 코드의 장점

- XHR 기본 순서가 명확하다.
- User JSON Parse와 중첩 Property 접근이 간결하다.
- Weather Category Filter와 시간별 Grouping을 구현한다.
- Table Row 구조가 비교적 올바르다.
- Promise Chain과 Debugger를 연결한다.
- 중복 Key 동작을 확인한다.

### 81-4. 강사님 코드의 보충점

- API Key를 Client 코드에 포함한다.
- HTTP Endpoint와 UTC·자정 문제가 있다.
- XHR Status·Error 처리가 없다.
- Weather Table 재조회 시 Row가 누적된다.
- 회원정보 문제를 구현하지 않는다.
- Fetch에서 `response.ok` 검사가 없다.
- Counting 주석이 구현되지 않았다.

---

<a id="js-20-section-86"></a>

## 82. 기존 코드에서 개선한 이유

### 82-1. XHR 응답 검사

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

### 82-2. Weather Grouping

기존:

```text
Item 하나마다 Row 생성
```

개선:

```text
fcstTime 기준 Grouping
→ 한 시간당 한 Row
```

### 82-3. 회원 Table

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

### 82-4. Fetch HTTP 오류

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

<a id="js-20-section-87"></a>

## 83. 실무형 예제: 회원 API Viewer

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

### 83-1. 코드에서 무엇을 사용하는 걸까?

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

<a id="js-20-section-88"></a>

## 84. 대표 오류로 이해하기

### 84-1. `send()` 직후 응답 사용

응답이 아직 도착하지 않아 빈 문자열일 수 있다.

### 84-2. `onload`를 무조건 성공으로 처리

HTTP 404·500도 들어올 수 있다.

### 84-3. JSON이 아닌 응답 Parse

`SyntaxError`가 발생한다.

### 84-4. 자정에 Hour만 1 감소

Date와 Time이 서로 맞지 않는다.

### 84-5. Weather Category를 잘못된 열에 배치

의미가 다른 측정값이 섞인다.

<a id="index-section-110"></a>

### 84-6. `tbody`에 `td` 직접 추가

올바른 Table 구조가 아니다.

---

<a id="js-20-section-89"></a>

## 85. 자주 하는 실수

### 85-1. `open()`이 요청을 전송한다고 생각

실제 전송은 `send()`다.

### 85-2. 상대 URL 기준을 JS 파일 위치로 생각

현재 Document URL 기준이다.

<a id="index-section-114"></a>

### 85-3. `toISOString()`을 Local 날짜로 생각

UTC 기준이다.

### 85-4. API Key를 Public Frontend에 직접 작성

사용자에게 노출된다.

### 85-5. HTTP API를 HTTPS 페이지에서 호출

Mixed Content로 차단될 수 있다.

### 85-6. 시간별 데이터를 Grouping하지 않음

같은 시간의 값을 한 Row에 맞추기 어렵다.

<a id="index-section-118"></a>

### 85-7. 반복문에서 `innerHTML +=` 사용

하위 DOM 전체가 반복해서 재파싱될 수 있다.

### 85-8. Fetch Catch가 404도 처리한다고 생각

`response.ok`를 직접 검사한다.

### 85-9. JSON Parse 성공만 확인

응답의 실제 자료형·Property도 검증한다.

### 85-10. 요청 상태 UI를 만들지 않음

Loading·Empty·Error·Success를 구분한다.

---

<a id="js-20-section-90"></a>

## 86. 핵심 요약

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

<a id="js-20-section-91"></a>

## 87. 최종 체크리스트

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

<a id="js-20-section-92"></a>

## 마무리

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
<a id="js-20-section-93"></a>

## V3 실행 추적 카드 — 요청 생성 → 서버 처리 → Response → 본문 변환 → DOM

`fetch`는 Promise를 즉시 반환한다. 응답이 오면 Response를 받고 `json()` 같은 비동기 본문 변환을 거친다. HTTP 404/500은 자동으로 reject되지 않을 수 있어 `response.ok`를 검사한다.

Console에는 단계별 값, Network에는 URL·메서드·상태·응답을 확인한다. CORS, 네트워크 실패, JSON 형식 오류를 서로 구분한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/20_ajax.html, asset/js/20_ajax.js`에서 실제 사용 위치와 차이를 확인한다.
