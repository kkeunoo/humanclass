# JavaScript AJAX와 Fetch API

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `20_JavaScript_AJAX와_Fetch_API.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `19_JavaScript_JSON과_객체직렬화.md` |
| 다음 학습 | 이후 JavaScript 원본 순서에 따라 진행 |
| 원본 기준 | `workspace/workspace_html/javascript/20_ajax.html`, `workspace/workspace_html/javascript/asset/js/20_ajax.js`, `workspace_teacher/workspace_html/javascript/20_ajax.html`, `workspace_teacher/workspace_html/javascript/asset/js/20_ajax.js` |
| 핵심 범위 | AJAX, `XMLHttpRequest`, GET 요청, 비동기 응답, `responseText`, `JSON.parse()`, 공공데이터 API, `filter()`, 시간별 데이터 그룹화, 동적 table, `fetch()`, Promise chain, `try...catch`, `debugger` |
| 프로젝트 연결 | 회원 목록 조회, 외부 API 호출, 날씨 데이터 가공, JSON 응답 렌더링, 오류 처리, 개발자 도구 디버깅 |

> 이 문서는 HTML과 실제 연결된 JavaScript 파일을 함께 비교했습니다. 강사님 코드는 `XMLHttpRequest`의 기본 흐름, JSONPlaceholder 회원 정보, 기상청 초단기예보, 시간별 데이터 그룹화, `fetch()`, `try...catch`, `debugger`를 간결하게 구현합니다. 내 코드는 주석과 직접 풀이가 훨씬 많고 회원정보 table까지 구현했지만, 날씨 시간별 출력 조건이 잘못되어 온도·습도·강수량 열이 정확히 대응하지 않으며, 회원정보 출력에서 빈 `tr`을 만든 뒤 `tbody.innerHTML +=`로 `td`를 직접 추가하는 구조적 문제가 있습니다. 원본 오류와 차이는 수정하지 않고 보존한 뒤 개선 방향을 별도로 설명합니다.

---

# 학습 목표

- AJAX의 의미와 사용 목적을 설명한다.
- `XMLHttpRequest`의 생성·설정·전송·응답 처리 단계를 이해한다.
- 비동기 요청 직후 `responseText`가 비어 있을 수 있는 이유를 설명한다.
- JSON 문자열을 JavaScript 값으로 변환한다.
- 중첩 객체와 배열에서 필요한 값을 찾는다.
- 공공데이터 API URL과 query parameter를 구성한다.
- 날씨 category를 `filter()`로 추린다.
- 시간별 category 값을 객체로 그룹화한다.
- 동적으로 table row를 생성한다.
- `fetch()`와 Promise chain의 흐름을 이해한다.
- `try...catch`로 동기 오류를 처리한다.
- `debugger`를 이용해 실행을 중단하고 상태를 확인한다.
- HTTP 상태 오류와 network 오류의 차이를 이해한다.
- 내 코드와 강사님 코드의 실제 차이와 오류를 정확히 기록한다.

---

# Core Concepts

## 1. AJAX란?

AJAX는 다음 표현의 약자입니다.

```text
Asynchronous JavaScript And XML
```

원본 HTML 주석:

```html
<!--
AJAX =
Asynchronous JavaScript and XML
비동기 통신
-->
```

이름에 XML이 포함되어 있지만 현대 웹에서는 JSON을 더 자주 사용합니다.

핵심은 페이지 전체를 이동하거나 새로고침하지 않고 JavaScript에서 server와 비동기 통신하는 것입니다.

---

## 2. Browser 이동과 AJAX

내 원본 주석:

```text
browser는 서버에 가서 Text를 받아와 해석
AJAX는 Text를 받아오는 것까지만

browser는 직접 사이트를 이동해야 하지만
AJAX는 값을 가져올 수 있음
```

보완하면 다음과 같습니다.

```text
일반 navigation
→ browser가 새 document를 요청하고 화면 전체를 전환

AJAX
→ 현재 document를 유지한 채 JavaScript가 data를 요청
→ 받은 data로 필요한 DOM만 갱신
```

AJAX 응답은 text뿐 아니라 Blob, ArrayBuffer 등으로도 받을 수 있습니다.

---

## 3. Load 이후 Bind

양쪽 원본:

```js
window.addEventListener(
  "load",
  bind
)
```

page의 주요 resource가 load된 뒤 `bind()`를 실행합니다.

`bind()` 안에서 button selector를 찾고 click listener를 등록합니다.

---

# XMLHttpRequest

## 4. AJAX 4단계

원본에서 설명하는 네 단계:

```text
1. XMLHttpRequest 객체 생성
2. 요청 method와 URL 설정
3. 요청 전송
4. 응답을 받아 활용
```

코드:

```js
const xhr =
  new XMLHttpRequest()

xhr.open(
  "GET",
  url
)

xhr.send()

xhr.onload =
  function() {
    // 응답 처리
  }
```

---

## 5. XMLHttpRequest 생성

```js
const xhr =
  new XMLHttpRequest()
```

HTTP 요청 상태와 응답을 관리하는 객체를 만듭니다.

---

## 6. Open

```js
xhr.open(
  "GET",
  "https://jsonplaceholder.typicode.com/users"
)
```

`open()`은 즉시 network 요청을 보내는 것이 아니라 요청 정보를 설정합니다.

주요 인수:

```text
method
→ GET, POST 등

URL
→ 요청 대상

async
→ 생략하면 기본적으로 true
```

---

## 7. Send

```js
xhr.send()
```

설정한 요청을 실제로 전송합니다.

GET 요청은 보통 body 없이 호출합니다.

---

## 8. Onload

```js
xhr.onload =
  function() {
    console.log(
      xhr.responseText
    )
  }
```

응답 load가 완료되었을 때 실행됩니다.

다만 network 요청이 완료됐다는 뜻이지 HTTP status가 반드시 성공이라는 뜻은 아닙니다.

따라서 다음과 같은 status 검사가 필요할 수 있습니다.

```js
if (
  xhr.status >= 200 &&
  xhr.status < 300
) {
  // 성공
}
```

---

## 9. ResponseText

```js
xhr.responseText
```

응답 body를 string으로 제공합니다.

JSONPlaceholder의 users endpoint는 JSON text를 반환합니다.

---

## 10. 비동기 직후 ResponseText

두 원본:

```js
xhr.send()

xhr.onload =
  function() {
    console.log(
      xhr.responseText
    )
  }

console.log(
  "[" +
  xhr.responseText +
  "]"
)
```

마지막 log는 요청 완료 전에 실행됩니다.

대표 출력:

```text
[]
```

그 후 응답이 오면 onload callback에서 HTML text가 출력됩니다.

이는 code 위치가 아래라고 해서 나중에 실행되는 것이 아니라, asynchronous callback이 응답 완료 후 실행되기 때문입니다.

---

## 11. 상대 URL 기준

두 번째 요청:

```js
xhr.open(
  "GET",
  "19_json.html"
)
```

내 주석은 JavaScript가 head에 연결되어 20번 HTML과 같은 folder path를 참고한다고 설명합니다.

더 정확히 말하면 상대 URL은 현재 document URL을 기준으로 해석됩니다.

외부 JavaScript 파일 자신의 filesystem 위치가 기준이 아닙니다.

---

# JSONPlaceholder 회원 데이터

## 12. JSON Parse

```js
const users =
  JSON.parse(
    xhr.responseText
  )
```

JSON string을 JavaScript array로 변환합니다.

---

## 13. 두 번째 사용자 이름

강사님:

```js
console.log(
  member[1].name
)

console.log(
  member[1]["name"]
)
```

내 코드:

```js
console.log(
  xhrData[1]["name"]
)

console.log(
  xhrData[1].name
)
```

둘 다 두 번째 배열 요소의 name을 가져옵니다.

원본 주석의 예상값:

```text
Ervin Howell
```

외부 서비스 데이터가 변경되면 실제 값도 달라질 수 있습니다.

---

## 14. 세 번째 사용자의 Latitude

```js
users[2]
  .address
  .geo
  .lat
```

bracket notation:

```js
users[2]
  ["address"]
  ["geo"]
  ["lat"]
```

중첩 객체 property를 순서대로 접근합니다.

---

## 15. 내 코드와 강사님 출력 차이

강사님은:

```js
console.log(
  member[1]
)
```

로 두 번째 user 객체 전체도 출력합니다.

내 코드는 parsed array 전체를 출력합니다.

```js
console.log(
  xhrData
)
```

학습 목적은 동일하지만 Console 범위가 다릅니다.

---

# 기상청 API

## 16. 날짜 생성

양쪽 원본:

```js
const now =
  new Date()

const today =
  now
    .toISOString()
    .split("T")[0]
    .replace(/-/g, "")
```

결과 형식:

```text
YYYYMMDD
```

---

## 17. UTC 주의

`toISOString()`은 UTC 기준입니다.

한국 local date와 UTC date가 다른 시간대에는 API에 잘못된 날짜를 보낼 수 있습니다.

local date가 필요하면 `getFullYear()`, `getMonth() + 1`, `getDate()`를 직접 조합하는 편이 안전합니다.

---

## 18. Base Time

원본:

```js
let hour =
  now.getHours() - 1
```

이후:

```js
if (hour < 10) {
  hour =
    "0" +
    hour +
    "00"
} else {
  hour =
    hour +
    "00"
}
```

현재 시각보다 한 시간 전의 `HH00` 형태를 만들려는 코드입니다.

---

## 19. 자정 오류

현재 시각이 0시이면:

```js
hour =
  -1
```

조건 결과:

```text
0-100
```

과 같은 잘못된 base_time이 만들어질 수 있습니다.

날짜도 전날로 바꿔야 합니다.

현재 원본에는 자정 처리 로직이 없습니다.

---

## 20. Service Key 차이

강사님 원본에는 공공데이터 service key가 직접 포함되어 있습니다.

내 원본:

```js
const key = ""
```

보안과 공유를 위해 이 문서에는 강사님 key 원문을 재출력하지 않습니다.

중요한 차이:

```text
강사님
→ key 값 존재

내 코드
→ 빈 문자열
```

따라서 내 날씨 요청은 유효한 key가 없으면 정상 응답을 받지 못합니다.

실무에서는 API key를 public repository의 client-side JavaScript에 직접 노출하지 않는 편이 좋습니다.

---

## 21. API URL

원본:

```js
let url =
  "http://apis.data.go.kr/" +
  "1360000/" +
  "VilageFcstInfoService_2.0/" +
  "getUltraSrtFcst"
```

query parameter:

```text
serviceKey
numOfRows
pageNo
dataType
base_date
base_time
nx
ny
```

---

## 22. HTTP와 Mixed Content

API URL은 HTTP입니다.

```text
http://apis.data.go.kr/...
```

페이지가 HTTPS라면 mixed content로 요청이 차단될 수 있습니다.

API가 HTTPS endpoint를 지원한다면 HTTPS를 사용해야 합니다.

---

## 23. URLSearchParams 개선

문자열을 계속 이어 붙이는 대신:

```js
const params =
  new URLSearchParams({
    serviceKey: key,
    numOfRows: "1000",
    pageNo: "1",
    dataType: "JSON",
    base_date: today,
    base_time: hour,
    nx: "63",
    ny: "110"
  })

const url =
  `${endpoint}?${params}`
```

처럼 구성할 수 있습니다.

service key가 이미 percent-encoded되어 있다면 `URLSearchParams`가 다시 encoding할 가능성도 검토해야 합니다.

---

## 24. 응답 구조

원본 접근:

```js
data
  .response
  .body
  .items
  .item
```

`item`은 예보 항목 array입니다.

대표 property:

```text
category
fcstValue
fcstTime
```

---

## 25. Category

원본에서 사용하는 category:

```text
T1H
→ 기온

REH
→ 습도

RN1
→ 1시간 강수량
```

원본 주석에는 LGT도 번개 category 예로 언급됩니다.

---

## 26. Filter

양쪽 코드의 핵심:

```js
const filtered =
  item.filter(
    function(data) {
      if (
        data.category ===
          "T1H" ||
        data.category ===
          "RN1" ||
        data.category ===
          "REH"
      ) {
        return true
      }
    }
  )
```

간단히:

```js
const categories =
  ["T1H", "RN1", "REH"]

const filtered =
  item.filter(
    data =>
      categories.includes(
        data.category
      )
  )
```

로 작성할 수 있습니다.

---

# 문제 1: 예측 Category Table

## 27. 강사님 구현

강사님 HTML에는:

```html
<tbody id="q1"></tbody>
```

가 있습니다.

JavaScript:

```js
for (
  let i = 0;
  i < filtered.length;
  i++
) {
  const tr =
    document.createElement(
      "tr"
    )

  tr.innerHTML = `
    <td>
      ${filtered[i].category}
    </td>
    <td>
      ${filtered[i].fcstTime}
    </td>
    <td>
      ${filtered[i].fcstValue}
    </td>
  `

  q1.append(tr)
}
```

table 구조에 맞게 `tr`과 `td`를 생성합니다.

---

## 28. 내 구현

내 HTML에는 `q1` table이 없습니다.

대신:

```html
<div id="output"></div>
```

을 사용합니다.

각 값에 `.column` class를 넣은 div를 생성합니다.

```text
예측카테고리
예측시간
값
```

기능상 목록을 보여 주지만 semantic table이 아니라 div layout입니다.

---

## 29. 내 CSS

```css
.column {
  display: inline-block;
  border: 1px solid red;
  width: 100px;
  text-align: center;
}
```

두 번째 layout:

```css
.column2 {
  display: inline-block;
  border: 1px solid red;
  width: 100px;
  height: 50px;
  text-align: center;
  vertical-align: top;
}
```

강사님 HTML에는 별도 CSS가 없습니다.

---

# 문제 2: 시간별 Grouping

## 30. 강사님의 객체 Grouping

강사님은 빈 객체를 만듭니다.

```js
const grouped = {}
```

각 item의 `fcstTime`을 key로 사용합니다.

```js
if (
  !grouped[
    filtered[i].fcstTime
  ]
) {
  grouped[
    filtered[i].fcstTime
  ] = {}
}
```

category를 중첩 key로 저장합니다.

```js
grouped[
  filtered[i].fcstTime
][
  filtered[i].category
] =
  filtered[i].fcstValue
```

결과 구조:

```js
{
  "1000": {
    T1H: "20",
    REH: "80",
    RN1: "0"
  }
}
```

---

## 31. Object.keys로 시간 순회

```js
const keys =
  Object.keys(grouped)
```

각 시간 key에 접근:

```js
grouped[keys[i]].T1H
grouped[keys[i]].REH
grouped[keys[i]].RN1
```

강사님 구현은 같은 예보 시간의 세 category를 한 row에 배치합니다.

---

## 32. 강사님 Q2 초기화 누락

강사님 코드:

```js
const q2 =
  document.querySelector(
    "#q2"
  )
```

그 뒤 기존 내용을 지우지 않고 row를 append합니다.

따라서 날씨 button을 여러 번 클릭하면 table row가 누적될 수 있습니다.

개선:

```js
q2.innerHTML = ""
```

---

## 33. 내 시간별 출력 구조

내 코드는 filtered item을 다시 순회하면서 item 하나마다 row 역할의 div를 만듭니다.

```js
for (
  let j = 0;
  j < timeFilter.length;
  j++
) {
  const addDiv =
    document.createElement(
      "div"
    )
}
```

같은 시간의 category를 하나의 객체로 먼저 묶지 않습니다.

따라서 시간별 한 줄 구조를 만들기 어렵습니다.

---

## 34. 내 Category 조건 오류

내 코드의 온도 열:

```js
if (
  category === "T1H" ||
  category === "REH"
) {
  t1hDiv.innerText =
    fcstValue
}
```

온도 column에 습도 값도 들어갑니다.

습도 열:

```js
if (
  category === "T1H"
) {
  rehDiv.innerText =
    fcstValue
}
```

습도 열에도 온도 값이 들어갑니다.

강수량 열:

```js
if (
  category === "T1H"
) {
  rn1Div.innerText =
    fcstValue
}
```

강수량 열에도 온도 값이 들어갑니다.

정확해야 할 조건:

```text
온도 열 → T1H
습도 열 → REH
강수량 열 → RN1
```

---

## 35. 내 시간 열 빈칸

내 코드:

```js
if (
  category === "T1H"
) {
  fcstDiv.innerText =
    fcstTime
}
```

T1H item에서만 시간을 표시하고 REH와 RN1 item row에서는 시간 칸이 비어 있습니다.

결과적으로 하나의 시간에 대해 여러 줄이 생기고 값이 잘못된 column에 배치됩니다.

---

# 문제 3: 회원정보 Table

## 36. 강사님 상태

강사님은 요구사항만 주석으로 남깁니다.

```text
btn4를 클릭하면
10명의 정보 중
id, name, zipcode, 회사 이름을 HTML로 표시
```

실제 `btn4` listener 구현은 없습니다.

---

## 37. 내 HTML

내 HTML에는 회원정보용 table이 있습니다.

```html
<tbody id="q3"></tbody>
```

column:

```text
ID
NAME
ZIPCODE
COMPANY
```

---

## 38. 내 회원정보 요청

```js
const xhr =
  new XMLHttpRequest()

xhr.open(
  "GET",
  "https://jsonplaceholder.typicode.com/users"
)

xhr.send()
```

응답을 parse해 users를 얻습니다.

---

## 39. 내 Row 생성 오류

내 코드:

```js
const tr =
  document.createElement(
    "tr"
  )

q3.append(tr)

q3.innerHTML += `
  <td>...</td>
  <td>...</td>
  <td>...</td>
  <td>...</td>
`
```

문제:

1. 만든 `tr`에 `td`를 append하지 않음
2. 빈 `tr`이 먼저 남음
3. `td`를 `tbody`의 direct child처럼 문자열로 추가함
4. `innerHTML +=`가 매 반복마다 전체 `tbody`를 다시 parsing함
5. 기존 DOM reference와 listener가 있다면 손실될 수 있음
6. button을 다시 누르면 기존 결과가 누적됨

browser가 HTML table parsing 규칙에 따라 보정할 수 있지만 의도한 구조가 명확하지 않습니다.

---

## 40. 올바른 회원 Row

```js
const tr =
  document.createElement(
    "tr"
  )

tr.innerHTML = `
  <td>${user.id}</td>
  <td>${user.name}</td>
  <td>${user.address.zipcode}</td>
  <td>${user.company.name}</td>
`

q3.append(tr)
```

또는 모든 `td`를 `createElement()`로 생성할 수 있습니다.

---

# Fetch API

## 41. Try...catch 예제

양쪽 원본:

```js
let a =
  undefined

try {
  a.push(1)
} catch (error) {
  console.log(error)
}
```

`undefined`에는 `push()` method가 없으므로 TypeError가 발생합니다.

catch가 오류를 잡아 이후 fetch 코드가 계속 실행됩니다.

---

## 42. Try...catch 범위

`try...catch`는 해당 block 안에서 synchronous하게 발생한 오류를 잡습니다.

Promise rejection은 `.catch()` 또는 `await`를 감싼 try...catch로 처리해야 합니다.

---

## 43. Fetch 기본 구조

양쪽 원본:

```js
fetch(
  url,
  {
    method: "GET"
  }
)
  .then(
    function(response) {
      console.log(response)

      return response.json()
    }
  )
  .then(
    function(data) {
      console.log(data)
    }
  )
  .catch(
    function(error) {
      console.error(error)
    }
  )
```

---

## 44. Fetch 반환값

`fetch()`는 Promise를 반환합니다.

첫 번째 `.then()`은 `Response` 객체를 받습니다.

```js
response.json()
```

도 Promise를 반환합니다.

두 번째 `.then()`은 parsing된 JavaScript data를 받습니다.

---

## 45. “Fetch가 3단계를 한 번에” 설명

내 주석:

```text
fetch(주소, 옵션 JSON)
3번까지가 한 번에 끝남
```

개념적으로 `XMLHttpRequest`보다 선언적이고 간결하다는 뜻으로 이해할 수 있습니다.

하지만 fetch도 내부적으로 요청 생성·전송·응답 대기·body parsing 단계가 존재합니다.

`response.json()`은 별도 asynchronous 작업입니다.

또한 fetch option은 JSON text가 아니라 JavaScript object입니다.

---

## 46. HTTP 오류와 Catch

중요:

```js
fetch("/not-found")
```

가 HTTP 404를 받아도 fetch Promise가 자동으로 reject되지 않을 수 있습니다.

`.catch()`는 주로 network failure, CORS failure, abort 등을 처리합니다.

HTTP status 검사:

```js
if (!response.ok) {
  throw new Error(
    `HTTP ${response.status}`
  )
}
```

가 필요합니다.

---

## 47. Fetch 개선

```js
fetch(url)
  .then(
    function(response) {
      if (!response.ok) {
        throw new Error(
          `HTTP ${response.status}`
        )
      }

      return response.json()
    }
  )
  .then(
    function(data) {
      console.log(data)
    }
  )
  .catch(
    function(error) {
      console.error(
        "요청 실패:",
        error
      )
    }
  )
```

---

# Debugger

## 48. Debug Button

원본:

```js
btn6.addEventListener(
  "click",
  function() {
    debugger

    console.log(
      "btn6 클릭"
    )

    debug()

    console.log(
      "끝"
    )
  }
)
```

개발자 도구가 열려 있으면 `debugger` statement에서 실행이 일시 정지됩니다.

---

## 49. Debug 함수

양쪽 원본:

```js
function debug() {
  let a = 1

  console.log(a)
}
```

step into, step over, scope 확인 등을 연습할 수 있습니다.

---

## 50. Teacher의 중복 Key 객체

강사님 JavaScript 마지막:

```js
let a = {
  a: 1,
  b: 2,
  a: 3
}

console.log(a)
```

같은 object literal에서 `a` key가 두 번 나오면 뒤의 값이 앞의 값을 덮어씁니다.

결과:

```js
{
  a: 3,
  b: 2
}
```

내 JavaScript에는 이 코드가 없습니다.

---

## 51. Teacher의 미완성 주석

강사님 마지막 주석:

```text
key가 없으면 만들고
key가 있으면 그 값에 +1
```

관련 구현은 없습니다.

예시:

```js
counts[key] =
  (counts[key] ?? 0) + 1
```

---

# HTML 비교

## 52. Button 문구

| Button | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| btn1 | `AJAX 실행` | `ajax 실행` |
| btn2 | `19_jason.html` | `19_json.html` |
| btn3 | `날씨예보` | `날씨 예보` |
| btn4 | `회원정보` | `회원 정보` |
| btn5 | `fetch` | `fetch` |
| btn6 | `debug` | `debug` |

내 btn2에는 `jason` 오타가 있지만 실제 요청 URL은 올바른 `19_json.html`입니다.

---

## 53. Table 구성 차이

강사님 HTML:

```text
q1
→ category, time, value table

q2
→ time, temperature, humidity, rainfall table
```

내 HTML:

```text
q2
→ time, temperature, humidity, rainfall table

q3
→ user information table

output
→ category listing div

output_time
→ time-based weather div
```

내 코드는 강사님 q1 문제를 div layout으로 별도 구현합니다.

---

## 54. 내 미사용 Q2 Table

내 HTML에는 `#q2` table이 있지만 내 JavaScript는 날씨 결과를 `#output_time`에 표시합니다.

따라서 `#q2` tbody는 현재 코드에서 사용되지 않습니다.

---

## 55. 내 HTML 주석

내 HTML에는 AJAX 정의 주석이 있습니다.

강사님 HTML에는 해당 주석이 없습니다.

---

## 56. 문서 기본 정보

양쪽 HTML:

```html
<html lang="en">
<title>Document</title>
```

한국어 학습 문서이므로:

```html
<html lang="ko">
<title>AJAX와 Fetch API</title>
```

가 더 적절합니다.

---

# My Code vs Teacher Code

## 57. 비교표

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| AJAX 설명 | 매우 상세 | 간결 |
| btn2 표시 | `19_jason.html` 오타 | `19_json.html` |
| 첫 users 출력 | array 전체 | 두 번째 user 객체 |
| 날씨 API key | 빈 문자열 | 값 포함 |
| 문제 1 출력 | div layout | semantic table |
| 문제 2 grouping | grouping 미완성 | 시간별 객체 grouping |
| 온도 조건 | T1H 또는 REH | grouped T1H |
| 습도 조건 | T1H | grouped REH |
| 강수량 조건 | T1H | grouped RN1 |
| 회원정보 문제 | 직접 구현 | 요구사항만 |
| 회원 row 구조 | 빈 tr + tbody innerHTML | 미구현 |
| q2 초기화 | output_time 초기화 | q2 초기화 누락 |
| fetch 흐름 | 동일, 설명 많음 | 동일 |
| debugger | 동일 | 동일 |
| 중복 object key 예제 | 없음 | 있음 |
| 마지막 counting 주석 | 없음 | 있음 |

---

# My Code Analysis

## 58. 내 코드 장점

- AJAX와 일반 browser navigation의 차이를 주석으로 설명했다.
- XMLHttpRequest 네 단계를 상세히 표시했다.
- bracket notation과 dot notation을 모두 사용했다.
- 상대 URL 기준을 스스로 보완 설명했다.
- 비동기 요청 직후 responseText가 비어 있음을 확인했다.
- 날씨 category를 filter로 추렸다.
- 문제 1을 직접 DOM element 생성 방식으로 구현했다.
- 회원정보 문제를 실제 요청과 table 출력까지 시도했다.
- try...catch 동작을 자세히 설명했다.
- XMLHttpRequest와 fetch를 비교했다.
- Promise chain과 response.json 역할을 설명했다.
- debugger 실습을 포함했다.

---

## 59. 내 코드 개선점

- btn2 표시 문구에 `jason` 오타가 있다.
- 날씨 API key가 비어 있어 요청이 실패할 수 있다.
- `toISOString()`의 UTC 날짜 문제를 처리하지 않는다.
- 자정에 base_time이 음수가 되는 문제를 처리하지 않는다.
- API endpoint가 HTTP다.
- XMLHttpRequest에서 status와 onerror를 검사하지 않는다.
- JSON parse 실패를 처리하지 않는다.
- 문제 2에서 시간별 grouping을 하지 않는다.
- 온도 열에 REH도 넣는다.
- 습도와 강수량 열에 T1H를 넣는다.
- 같은 시간 데이터를 여러 row로 분리한다.
- 회원 table에서 빈 tr을 만들고 td는 tbody.innerHTML에 직접 추가한다.
- `innerHTML +=`로 반복해서 tbody 전체를 재parse한다.
- 회원 table을 다시 누르면 이전 결과가 누적된다.
- fetch에서 `response.ok`를 검사하지 않는다.
- fetch option을 JSON이라고 부른다.
- `==`를 많이 사용한다.
- 문서 lang과 title이 내용에 맞지 않는다.

---

# Teacher Code Analysis

## 60. 강사님 코드 장점

- XMLHttpRequest 네 단계가 명확하다.
- users JSON parsing과 중첩 property 접근을 간결하게 보여 준다.
- 상대 HTML 요청의 asynchronous 결과를 확인한다.
- 날씨 API response 구조를 단계적으로 접근한다.
- category filter를 실제 실행한다.
- 문제 1을 올바른 table row 구조로 구현한다.
- 시간별 객체 grouping을 구현한다.
- Object.keys로 시간별 row를 출력한다.
- try...catch와 fetch Promise chain을 연결한다.
- debugger와 duplicate key 예제를 포함한다.

---

## 61. 강사님 코드 개선점

- API key를 client JavaScript에 직접 포함한다.
- HTTP 날씨 endpoint를 사용한다.
- UTC 날짜와 자정 처리가 없다.
- XMLHttpRequest status·error 처리가 없다.
- q2를 다시 실행하기 전 비우지 않아 row가 누적된다.
- btn4 문제는 구현하지 않는다.
- fetch에서 response.ok를 검사하지 않는다.
- `let option`을 만들고 실제 fetch에서는 literal object를 다시 작성해 option 변수가 사용되지 않는다.
- `==`를 사용한다.
- duplicate key는 동작하지만 lint error나 실수 가능성이 있다.
- 마지막 counting 요구는 구현되지 않았다.
- 문서 lang과 title이 내용에 맞지 않는다.

---

# Improvements

## 62. 안전한 XMLHttpRequest

```js
function requestJSON(
  url,
  onSuccess
) {
  const xhr =
    new XMLHttpRequest()

  xhr.open(
    "GET",
    url
  )

  xhr.onload =
    function() {
      if (
        xhr.status < 200 ||
        xhr.status >= 300
      ) {
        console.error(
          `HTTP ${xhr.status}`
        )

        return
      }

      try {
        const data =
          JSON.parse(
            xhr.responseText
          )

        onSuccess(data)
      } catch (error) {
        console.error(
          "JSON 처리 실패",
          error
        )
      }
    }

  xhr.onerror =
    function() {
      console.error(
        "Network 요청 실패"
      )
    }

  xhr.send()
}
```

---

## 63. 시간별 날씨 Grouping

```js
function groupForecast(items) {
  const targetCategories =
    ["T1H", "REH", "RN1"]

  return items
    .filter(
      item =>
        targetCategories
          .includes(
            item.category
          )
    )
    .reduce(
      function(grouped, item) {
        const time =
          item.fcstTime

        if (!grouped[time]) {
          grouped[time] = {}
        }

        grouped[time][
          item.category
        ] =
          item.fcstValue

        return grouped
      },
      {}
    )
}
```

---

## 64. 안전한 Table Rendering

```js
function renderForecast(
  tbody,
  grouped
) {
  tbody.replaceChildren()

  const fragment =
    document
      .createDocumentFragment()

  Object.entries(
    grouped
  ).forEach(
    function([
      time,
      values
    ]) {
      const tr =
        document.createElement(
          "tr"
        )

      const cells = [
        time,
        values.T1H ?? "-",
        values.REH ?? "-",
        values.RN1 ?? "-"
      ]

      cells.forEach(
        function(value) {
          const td =
            document
              .createElement(
                "td"
              )

          td.textContent =
            value

          tr.append(td)
        }
      )

      fragment.append(tr)
    }
  )

  tbody.append(fragment)
}
```

---

# Representative Examples

## 65. Async/Await Fetch

```js
async function loadUsers() {
  const response =
    await fetch(
      "https://jsonplaceholder.typicode.com/users"
    )

  if (!response.ok) {
    throw new Error(
      `HTTP ${response.status}`
    )
  }

  return response.json()
}

async function handleClick() {
  try {
    const users =
      await loadUsers()

    console.log(users)
  } catch (error) {
    console.error(
      "회원 정보를 불러오지 못했습니다.",
      error
    )
  }
}
```

---

# Practical Usage

## 66. 회원정보 Table 완성

```js
async function renderUsers() {
  const q3 =
    document.querySelector(
      "#q3"
    )

  q3.replaceChildren()

  try {
    const response =
      await fetch(
        "https://jsonplaceholder.typicode.com/users"
      )

    if (!response.ok) {
      throw new Error(
        `HTTP ${response.status}`
      )
    }

    const users =
      await response.json()

    const fragment =
      document
        .createDocumentFragment()

    users.forEach(
      function(user) {
        const tr =
          document.createElement(
            "tr"
          )

        const values = [
          user.id,
          user.name,
          user.address.zipcode,
          user.company.name
        ]

        values.forEach(
          function(value) {
            const td =
              document
                .createElement(
                  "td"
                )

            td.textContent =
              value

            tr.append(td)
          }
        )

        fragment.append(tr)
      }
    )

    q3.append(fragment)
  } catch (error) {
    console.error(
      "회원정보 조회 실패",
      error
    )
  }
}
```

---

# Common Mistakes

## 67. 자주 하는 실수

### 67.1 Open이 요청을 바로 보낸다고 생각

실제 전송은 `send()`에서 시작합니다.

### 67.2 Send 바로 다음 줄에서 응답을 읽음

비동기 요청이 아직 끝나지 않아 빈 문자열일 수 있습니다.

### 67.3 Onload면 무조건 HTTP 성공이라고 생각

status를 별도로 확인해야 합니다.

### 67.4 상대 URL 기준을 JS 파일 위치라고 생각

현재 document URL 기준입니다.

### 67.5 ToISOString을 Local Date로 생각

UTC 기준입니다.

### 67.6 자정에 Hour - 1만 수행

날짜도 전날로 조정해야 합니다.

### 67.7 API Key를 Frontend에 직접 공개

source에서 쉽게 노출됩니다.

### 67.8 시간별 데이터를 Grouping하지 않음

category별 item을 한 row에 정확히 배치하기 어렵습니다.

### 67.9 Tbody에 Td를 직접 추가

table 구조상 tr 안에 td가 있어야 합니다.

### 67.10 Fetch Catch가 404도 자동 처리한다고 생각

`response.ok`를 확인해야 합니다.

---

# Interview / Review

## 68. 면접·복습 포인트

### Q1. AJAX란 무엇인가요?

현재 페이지를 유지하면서 JavaScript로 server와 비동기 통신하고 일부 UI만 갱신하는 방식입니다.

### Q2. XMLHttpRequest의 기본 순서는 무엇인가요?

객체 생성, open, send, 응답 callback 처리입니다.

### Q3. Send 직후 ResponseText가 비어 있는 이유는 무엇인가요?

network 요청이 비동기로 진행되어 응답이 아직 도착하지 않았기 때문입니다.

### Q4. Onload와 HTTP 성공은 같은 의미인가요?

아닙니다. onload 후에도 status를 확인해야 합니다.

### Q5. Fetch는 무엇을 반환하나요?

Promise를 반환합니다.

### Q6. Response.json은 무엇을 반환하나요?

JSON body parsing 결과를 제공하는 Promise를 반환합니다.

### Q7. Fetch에서 404를 어떻게 처리하나요?

`response.ok` 또는 status를 검사하고 직접 error를 throw합니다.

### Q8. 날씨 데이터를 시간별로 묶는 이유는 무엇인가요?

같은 시간의 온도·습도·강수량을 한 row에 배치하기 위해서입니다.

### Q9. 내 시간별 날씨 출력의 핵심 오류는 무엇인가요?

category 조건이 잘못되어 온도 값이 습도·강수량 열에도 들어가고 시간별 grouping이 없습니다.

### Q10. 내 회원 table 생성의 구조적 문제는 무엇인가요?

빈 tr을 append한 뒤 td 문자열을 tbody.innerHTML에 직접 누적합니다.

---

# Problems

## 문제 1. XMLHttpRequest 생성

새 XMLHttpRequest 객체를 생성하세요.

## 문제 2. GET 요청 준비

JSONPlaceholder users URL로 GET 요청을 설정하세요.

## 문제 3. 요청 전송

설정된 XMLHttpRequest를 전송하세요.

## 문제 4. 응답 출력

onload에서 responseText를 출력하세요.

## 문제 5. Status 검사

2xx status일 때만 성공 처리하세요.

## 문제 6. JSON Parse

users responseText를 JavaScript array로 변환하세요.

## 문제 7. 중첩 Property

세 번째 user의 latitude를 출력하세요.

## 문제 8. 비동기 순서

send 직후 responseText가 빈 값일 수 있는 이유를 설명하세요.

## 문제 9. 상대 URL

`19_json.html` 요청의 기준 URL을 설명하세요.

## 문제 10. Category Filter

T1H, REH, RN1만 filter하세요.

## 문제 11. 시간별 Grouping

fcstTime을 key로 category 값을 객체에 묶으세요.

## 문제 12. Forecast Table

시간, 온도, 습도, 강수량을 한 row로 출력하세요.

## 문제 13. Table 초기화

재조회 전에 tbody 기존 내용을 지우세요.

## 문제 14. 회원정보 조회

users에서 id, name, zipcode, company name을 출력하세요.

## 문제 15. 안전한 Row 생성

tbody 안에 올바른 tr과 td를 생성하세요.

## 문제 16. Try Catch

undefined에 push를 호출하는 오류를 catch하세요.

## 문제 17. Fetch 요청

fetch로 users를 GET 요청하세요.

## 문제 18. Response OK

HTTP 실패 status를 error로 처리하세요.

## 문제 19. Promise Chain

response.json 결과를 다음 then에서 출력하세요.

## 문제 20. Async Await

문제 17을 async/await로 다시 작성하세요.

## 문제 21. 원본 오류

내 날씨 category 조건과 회원 table 구조 오류를 설명하세요.

## 문제 22. 종합 API Viewer

다음 요구사항을 만족하세요.

- fetch로 users 조회
- response.ok 검사
- JSON parsing
- loading 문구 표시
- 기존 tbody 초기화
- id, name, zipcode, company 출력
- createElement와 textContent 사용
- 오류 발생 시 사용자 메시지 출력
- 재조회해도 row 중복 없음
- button 연속 클릭 중 중복 요청 방지

---

# Answers

## 정답 1

```js
const xhr =
  new XMLHttpRequest()
```

## 정답 2

```js
xhr.open(
  "GET",
  "https://jsonplaceholder.typicode.com/users"
)
```

## 정답 3

```js
xhr.send()
```

## 정답 4

```js
xhr.onload =
  function() {
    console.log(
      xhr.responseText
    )
  }
```

## 정답 5

```js
xhr.onload =
  function() {
    if (
      xhr.status >= 200 &&
      xhr.status < 300
    ) {
      console.log(
        xhr.responseText
      )
    }
  }
```

## 정답 6

```js
const users =
  JSON.parse(
    xhr.responseText
  )
```

## 정답 7

```js
console.log(
  users[2]
    .address
    .geo
    .lat
)
```

## 정답 8

요청과 응답이 비동기로 진행되므로 send 다음 synchronous code가 응답 callback보다 먼저 실행될 수 있기 때문입니다.

## 정답 9

상대 URL은 외부 JavaScript 파일 위치가 아니라 현재 document URL을 기준으로 해석됩니다.

## 정답 10

```js
const categories =
  ["T1H", "REH", "RN1"]

const filtered =
  items.filter(
    item =>
      categories.includes(
        item.category
      )
  )
```

## 정답 11

```js
const grouped = {}

filtered.forEach(
  function(item) {
    if (
      !grouped[
        item.fcstTime
      ]
    ) {
      grouped[
        item.fcstTime
      ] = {}
    }

    grouped[
      item.fcstTime
    ][
      item.category
    ] =
      item.fcstValue
  }
)
```

## 정답 12

```js
Object.entries(
  grouped
).forEach(
  function([
    time,
    values
  ]) {
    const tr =
      document.createElement(
        "tr"
      )

    tr.innerHTML = `
      <td>${time}</td>
      <td>${values.T1H ?? "-"}</td>
      <td>${values.REH ?? "-"}</td>
      <td>${values.RN1 ?? "-"}</td>
    `

    tbody.append(tr)
  }
)
```

## 정답 13

```js
tbody.replaceChildren()
```

또는:

```js
tbody.innerHTML = ""
```

## 정답 14

```js
users.forEach(
  function(user) {
    console.log(
      user.id,
      user.name,
      user.address.zipcode,
      user.company.name
    )
  }
)
```

## 정답 15

```js
const tr =
  document.createElement(
    "tr"
  )

const td =
  document.createElement(
    "td"
  )

td.textContent =
  user.name

tr.append(td)
tbody.append(tr)
```

## 정답 16

```js
try {
  const value =
    undefined

  value.push(1)
} catch (error) {
  console.error(error)
}
```

## 정답 17

```js
fetch(
  "https://jsonplaceholder.typicode.com/users"
)
```

## 정답 18

```js
fetch(url)
  .then(
    function(response) {
      if (!response.ok) {
        throw new Error(
          `HTTP ${response.status}`
        )
      }

      return response.json()
    }
  )
```

## 정답 19

```js
fetch(url)
  .then(
    response =>
      response.json()
  )
  .then(
    function(data) {
      console.log(data)
    }
  )
```

## 정답 20

```js
async function loadUsers() {
  try {
    const response =
      await fetch(url)

    if (!response.ok) {
      throw new Error(
        `HTTP ${response.status}`
      )
    }

    const users =
      await response.json()

    console.log(users)
  } catch (error) {
    console.error(error)
  }
}
```

## 정답 21

내 날씨 코드는 온도 열에 T1H와 REH를 넣고, 습도와 강수량 열에는 T1H를 넣습니다. 또한 같은 시간의 세 category를 grouping하지 않습니다. 회원정보 코드는 빈 tr을 append한 뒤 td 문자열을 tbody의 innerHTML에 직접 누적하므로 올바른 row 구조가 아닙니다.

## 정답 22

```js
const button =
  document.querySelector(
    "#loadUsers"
  )

const tbody =
  document.querySelector(
    "#users"
  )

const message =
  document.querySelector(
    "#message"
  )

button.addEventListener(
  "click",
  async function() {
    if (button.disabled) {
      return
    }

    button.disabled = true
    message.textContent =
      "불러오는 중입니다."
    tbody.replaceChildren()

    try {
      const response =
        await fetch(
          "https://jsonplaceholder.typicode.com/users"
        )

      if (!response.ok) {
        throw new Error(
          `HTTP ${response.status}`
        )
      }

      const users =
        await response.json()

      const fragment =
        document
          .createDocumentFragment()

      users.forEach(
        function(user) {
          const tr =
            document.createElement(
              "tr"
            )

          const values = [
            user.id,
            user.name,
            user.address.zipcode,
            user.company.name
          ]

          values.forEach(
            function(value) {
              const td =
                document
                  .createElement(
                    "td"
                  )

              td.textContent =
                value

              tr.append(td)
            }
          )

          fragment.append(tr)
        }
      )

      tbody.append(fragment)
      message.textContent =
        `${users.length}명을 불러왔습니다.`
    } catch (error) {
      message.textContent =
        "회원정보를 불러오지 못했습니다."

      console.error(error)
    } finally {
      button.disabled = false
    }
  }
)
```

---

# Final Checklist

## AJAX와 XHR

- [ ] AJAX의 의미를 설명할 수 있다.
- [ ] XMLHttpRequest 네 단계를 이해했다.
- [ ] open과 send 역할을 구분했다.
- [ ] onload에서 응답을 처리했다.
- [ ] status를 검사했다.
- [ ] onerror를 처리했다.
- [ ] responseText가 string임을 이해했다.
- [ ] JSON.parse 실패 가능성을 처리했다.
- [ ] 상대 URL의 기준을 이해했다.

## 날씨 API

- [ ] UTC와 local date 차이를 확인했다.
- [ ] 자정 base_time 문제를 확인했다.
- [ ] API key 노출을 피했다.
- [ ] HTTPS endpoint를 검토했다.
- [ ] T1H, REH, RN1을 filter했다.
- [ ] fcstTime 기준으로 grouping했다.
- [ ] 시간별 값을 한 row로 출력했다.
- [ ] 재조회 전 tbody를 초기화했다.
- [ ] 없는 category는 기본값을 표시했다.

## Fetch

- [ ] fetch가 Promise를 반환함을 이해했다.
- [ ] response.json도 Promise임을 이해했다.
- [ ] response.ok를 검사했다.
- [ ] network error와 HTTP error를 구분했다.
- [ ] Promise chain과 async/await를 모두 이해했다.
- [ ] loading과 button disabled 상태를 처리했다.
- [ ] finally에서 상태를 복구했다.

## DOM과 Debug

- [ ] tbody 안에 tr, tr 안에 td를 넣었다.
- [ ] innerHTML 반복 재할당을 피했다.
- [ ] createDocumentFragment를 활용했다.
- [ ] textContent로 값을 넣었다.
- [ ] debugger 중단점을 이해했다.
- [ ] duplicate object key가 뒤 값으로 덮어써짐을 이해했다.

## 원본 검수

- [ ] 두 실제 20_ajax.html을 비교했다.
- [ ] 연결된 두 실제 20_ajax.js를 비교했다.
- [ ] 내 btn2의 `jason` 오타를 기록했다.
- [ ] API key 유무 차이를 기록했다.
- [ ] 강사님 key 원문을 문서에 재노출하지 않았다.
- [ ] 문제 1 div/table 구현 차이를 기록했다.
- [ ] 내 문제 2 category 조건 오류를 기록했다.
- [ ] 강사님 시간별 grouping 구현을 기록했다.
- [ ] 강사님 q2 누적 문제를 기록했다.
- [ ] 내 회원 row 구조 문제를 기록했다.
- [ ] 강사님의 btn4 미구현을 기록했다.
- [ ] 강사님의 duplicate key 예제를 기록했다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 20번은 XMLHttpRequest 기반 AJAX와 Fetch API를 다룬다.
- AJAX는 현재 페이지를 유지하면서 server data를 비동기로 요청하는 방식이다.
- XMLHttpRequest 기본 흐름은 생성, open, send, callback 처리다.
- open은 요청 정보를 설정하고 실제 전송은 send가 수행한다.
- responseText는 응답 body 문자열이다.
- send 직후 responseText는 응답 전이라 비어 있을 수 있다.
- 상대 URL은 현재 document URL을 기준으로 해석된다.
- onload가 실행되어도 HTTP status가 성공이라는 보장은 없다.
- JSON response는 JSON.parse로 JavaScript 값으로 바꾼다.
- JSONPlaceholder users에서 중첩 property를 dot 또는 bracket notation으로 접근한다.
- 날씨 날짜 생성에 toISOString을 쓰면 UTC와 local date 차이를 주의해야 한다.
- 현재 시각에서 한 시간을 빼는 원본은 자정 처리가 없다.
- 강사님 원본에는 service key가 포함되지만 내 원본 key는 빈 문자열이다.
- API key를 client JavaScript와 public repository에 직접 노출하지 않는 편이 좋다.
- 원본 날씨 endpoint는 HTTP라 HTTPS page에서 mixed content가 생길 수 있다.
- T1H는 기온, REH는 습도, RN1은 강수량이다.
- 강사님은 category를 filter한 뒤 fcstTime 기준 객체로 grouping한다.
- 내 코드는 같은 시간의 category를 grouping하지 않는다.
- 내 온도 열은 T1H와 REH를 넣고 습도·강수량 열은 T1H를 넣는 실제 오류가 있다.
- 강사님 q2는 재조회 전에 비우지 않아 row가 누적될 수 있다.
- 내 btn4는 회원정보를 직접 구현했지만 빈 tr과 tbody.innerHTML 누적 구조가 잘못됐다.
- tbody에는 tr을 넣고 각 td는 해당 tr 안에 넣어야 한다.
- try...catch는 synchronous 오류를 잡아 이후 code가 계속 실행되게 한다.
- fetch는 Promise를 반환하고 response.json도 Promise를 반환한다.
- fetch catch는 404 같은 HTTP status를 자동으로 오류 처리하지 않을 수 있다.
- response.ok를 검사하고 직접 error를 throw해야 한다.
- debugger statement는 개발자 도구에서 실행을 일시 정지한다.
- 강사님 마지막 duplicate key 객체는 뒤의 a:3이 앞의 a:1을 덮어쓴다.
