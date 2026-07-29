# JavaScript Discord Webhook과 XMLHttpRequest

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `22_JavaScript_Discord_Webhook과_XMLHttpRequest.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `21_JavaScript_Gemini_API와_멀티턴대화.md` |
| 다음 학습 | 이후 JavaScript 원본 순서에 따라 진행 |
| 원본 기준 | `workspace/workspace_html/javascript/22_discord.html`, `workspace_teacher/workspace_html/javascript/22_discord.html` |
| 핵심 범위 | Discord webhook, `XMLHttpRequest`, POST 요청, JSON body, request header, textarea 입력값, `JSON.stringify()`, webhook URL 보안, 응답 처리 |
| 프로젝트 연결 | 알림 전송, 운영 메시지, 간단한 chatbot 연동, 외부 서비스 webhook 호출, 관리자 notification |

> 이 문서는 내 코드와 강사님 코드의 `22_discord.html`만 직접 비교했습니다. 두 파일 모두 textarea 입력값을 Discord webhook으로 POST 전송하는 구조입니다. 강사님 원본에는 실제 webhook URL이 포함되어 있었지만, 이는 외부에서 메시지를 보낼 수 있는 민감한 credential이므로 문서에는 재노출하지 않았습니다. 내 코드는 URL을 빈 문자열로 두었고 username과 주석, HTML 일부가 다릅니다. 원본의 오타와 동작상 문제는 그대로 보존한 뒤 개선 방향을 별도로 설명합니다.

---

# 학습 목표

- Discord webhook의 목적을 설명한다.
- textarea의 값을 읽어 JSON body로 구성한다.
- `XMLHttpRequest`로 POST 요청을 보낸다.
- `Content-Type: application/json` header를 설정한다.
- JavaScript 객체를 `JSON.stringify()`로 직렬화한다.
- webhook URL을 source code에 직접 넣는 위험을 이해한다.
- HTTP status와 network error를 처리한다.
- 빈 입력값과 중복 요청을 방지한다.
- 내 코드와 강사님 코드의 실제 차이를 정확히 기록한다.

---

# Core Concepts

## 1. Webhook이란?

Webhook은 특정 서비스가 제공하는 URL로 HTTP 요청을 보내 외부 동작을 실행하는 방식입니다.

Discord webhook은 JSON 형식의 message payload를 POST로 보내 channel에 message를 전송할 수 있습니다.

원본 흐름:

```text
textarea 입력
→ button click
→ webhook URL로 POST
→ Discord channel에 message 전송
```

---

## 2. Window.onload

양쪽 원본:

```js
window.onload =
  function() {
    discord()
  }
```

page load 후 `discord()`를 호출합니다.

`discord()` 함수는 즉시 message를 보내는 것이 아니라 button click listener를 등록합니다.

---

## 3. Button 선택

```js
const ask =
  document.querySelector(
    "#ask"
  )
```

`id="ask"` button을 선택합니다.

---

## 4. Click Event

```js
ask.addEventListener(
  "click",
  function() {
    // message 전송
  }
)
```

사용자가 button을 누를 때마다 새 request를 보냅니다.

원본에는 요청 중 button 비활성화 처리가 없어 빠르게 여러 번 누르면 message가 중복 전송될 수 있습니다.

---

# Input 처리

## 5. Textarea 값 읽기

```js
const prompt =
  document
    .querySelector(
      "#prompt"
    )
    .value
```

textarea의 현재 문자열을 가져옵니다.

원본에는 다음 처리가 없습니다.

- `trim()`
- 빈 값 검증
- 최대 길이 검증
- 성공 후 textarea 초기화

---

## 6. 빈 문자열 문제

사용자가 아무 내용도 입력하지 않아도 request를 보냅니다.

개선:

```js
const prompt =
  promptElement
    .value
    .trim()

if (prompt === "") {
  alert(
    "메시지를 입력하세요."
  )

  return
}
```

---

# XMLHttpRequest POST

## 7. 객체 생성

```js
const xhr =
  new XMLHttpRequest()
```

HTTP request를 관리하는 객체를 만듭니다.

---

## 8. Open

```js
xhr.open(
  "post",
  url
)
```

method와 URL을 설정합니다.

HTTP method는 대소문자를 구분하지 않지만 관례적으로 uppercase를 사용합니다.

```js
xhr.open(
  "POST",
  url
)
```

---

## 9. 내 URL

내 코드:

```js
const url = ""
```

빈 문자열입니다.

현재 document URL을 대상으로 요청하려 할 수 있으므로 Discord webhook 전송은 정상 동작하지 않습니다.

내 코드가 credential을 직접 노출하지 않는 점은 안전하지만, 실제 호출을 위해서는 server-side proxy 등 안전한 endpoint가 필요합니다.

---

## 10. 강사님 URL

강사님 원본에는 실제 Discord webhook URL이 들어 있습니다.

이 URL은 message 전송 권한을 가진 secret credential과 비슷하게 취급해야 합니다.

문서에서는 URL 원문을 재출력하지 않습니다.

노출된 webhook은 다음 조치가 필요할 수 있습니다.

```text
Discord에서 기존 webhook 삭제 또는 재생성
새 URL을 source code에 commit하지 않기
server 환경 변수에 저장
frontend는 자신의 backend endpoint만 호출
```

---

## 11. Request Header

양쪽 원본:

```js
xhr.setRequestHeader(
  "Content-Type",
  "application/json"
)
```

request body가 JSON text임을 server에 알립니다.

---

# Payload

## 12. Param 객체

내 코드:

```js
const param = {
  username:
    "zl존법사v",
  content:
    prompt
}
```

강사님 코드:

```js
const param = {
  username:
    "쵬니수",
  content:
    prompt
}
```

실제 차이:

```text
username 값이 다름
강사님 코드에는 username 80자 제한 주석이 있음
내 코드에는 payload 형식을 설명하는 주석이 있음
```

---

## 13. Username

`username`은 webhook message에 표시되는 이름을 지정합니다.

강사님 주석:

```js
// 80자 제한
```

실제 제한은 service 정책에 따라 달라질 수 있으므로 현재 사용 전 공식 Discord 문서를 확인해야 합니다.

---

## 14. Content

```js
content:
  prompt
```

textarea에서 읽은 message 문자열을 Discord에 보냅니다.

원본에는 length validation이 없습니다.

---

## 15. JSON.stringify

```js
xhr.send(
  JSON.stringify(
    param
  )
)
```

JavaScript 객체를 JSON 문자열로 직렬화해 request body에 넣습니다.

전송 형태:

```json
{
  "username": "표시 이름",
  "content": "사용자 입력"
}
```

---

# Response 처리

## 16. Onload

양쪽 원본:

```js
xhr.onload =
  function() {
    console.log(
      xhr.responseText
    )
  }
```

요청이 완료되면 response body를 출력합니다.

하지만 HTTP status 검사가 없습니다.

---

## 17. 성공 Status

Discord webhook은 성공 시 response body가 비어 있을 수 있습니다.

따라서 `responseText`만 보는 것보다 status를 확인하는 편이 중요합니다.

```js
if (
  xhr.status >= 200 &&
  xhr.status < 300
) {
  console.log(
    "전송 성공"
  )
}
```

---

## 18. HTTP 오류

예:

```text
400
→ 잘못된 body

401 또는 403
→ 인증·권한 문제

404
→ webhook 없음

429
→ rate limit
```

정확한 status와 정책은 Discord 공식 문서를 기준으로 확인해야 합니다.

---

## 19. Network Error

원본에는 `xhr.onerror`가 없습니다.

개선:

```js
xhr.onerror =
  function() {
    console.error(
      "네트워크 오류"
    )
  }
```

---

# HTML 비교

## 20. Textarea

양쪽:

```html
<textarea id="prompt"></textarea>
```

label이 없습니다.

접근성을 위해:

```html
<label for="prompt">
  Discord 메시지
</label>
```

을 추가할 수 있습니다.

---

## 21. Button Type

내 코드:

```html
<button
  type="buttn"
  id="ask"
>
  디코에 말하기
</button>
```

`buttn`은 오타입니다.

강사님 코드:

```html
<button
  type="button"
  id="ask"
>
  디코에 말하기
</button>
```

올바른 값은 `button`입니다.

---

## 22. 내 Body의 Test 문자열

내 코드에는 button 아래에 다음 text가 있습니다.

```text
test
```

강사님 코드에는 없습니다.

실행 기능과 직접 관련 없는 임시 text로 보입니다.

---

## 23. Line Break 차이

강사님:

```html
</button><br>
```

내 코드:

```html
</button>
test
```

강사님은 button 뒤에 line break를 넣고, 내 코드는 test text를 바로 배치합니다.

---

## 24. Lang와 Title

양쪽:

```html
<html lang="en">
<title>Document</title>
```

한국어 UI이므로 다음이 더 적절합니다.

```html
<html lang="ko">
<title>Discord Webhook 실습</title>
```

---

# My Code vs Teacher Code

## 25. 비교표

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 원본 파일 | `22_discord.html` | `22_discord.html` |
| 핵심 흐름 | 동일 | 동일 |
| Webhook URL | 빈 문자열 | 실제 URL 포함 |
| URL 보안 | credential 미포함 | credential 노출 위험 |
| Username | `zl존법사v` | `쵬니수` |
| Username 주석 | 없음 | 80자 제한 |
| Payload 주석 | 있음 | 없음 |
| Button type | `buttn` 오타 | `button` 정상 |
| Body 추가 text | `test` 있음 | 없음 |
| Button 뒤 `<br>` | 없음 | 있음 |
| Response 처리 | responseText 출력 | responseText 출력 |
| Status 검사 | 없음 | 없음 |
| Onerror | 없음 | 없음 |
| 빈 값 검증 | 없음 | 없음 |
| 중복 요청 방지 | 없음 | 없음 |

---

# My Code Analysis

## 26. 내 코드 장점

- webhook URL을 빈 문자열로 두어 credential을 직접 노출하지 않았다.
- payload가 Discord 전송 형식이라는 주석을 추가했다.
- textarea 값을 content에 넣는 기본 흐름이 명확하다.
- `Content-Type: application/json`을 설정했다.
- `JSON.stringify()`를 사용했다.
- 강사님 코드와 동일한 핵심 request 흐름을 구현했다.

---

## 27. 내 코드 개선점

- URL이 빈 문자열이라 실제 Discord 전송이 되지 않는다.
- `type="buttn"` 오타가 있다.
- body에 임시 `test` text가 남아 있다.
- prompt trim과 빈 값 검증이 없다.
- username과 content 길이를 검증하지 않는다.
- HTTP status를 검사하지 않는다.
- `xhr.onerror`가 없다.
- rate limit을 처리하지 않는다.
- 전송 중 button을 비활성화하지 않는다.
- 성공 후 textarea를 비우지 않는다.
- 사용자에게 성공·실패 message를 표시하지 않는다.
- `lang="en"`과 title이 내용에 맞지 않는다.

---

# Teacher Code Analysis

## 28. 강사님 코드 장점

- 실제 webhook request 전체 흐름을 보여 준다.
- `POST`, JSON header, stringify, onload가 간결하다.
- button type이 올바르다.
- username 제한 관련 주석이 있다.
- 실습 목적에 필요한 최소 코드가 명확하다.

---

## 29. 강사님 코드 개선점

- 실제 webhook URL을 client source에 직접 포함한다.
- source가 공유되면 누구나 webhook을 악용할 수 있다.
- prompt trim과 빈 값 검증이 없다.
- HTTP status를 검사하지 않는다.
- `xhr.onerror`가 없다.
- 429 rate limit 처리가 없다.
- 전송 중 button을 막지 않는다.
- 성공 후 UI 상태를 갱신하지 않는다.
- label이 없다.
- `lang="en"`과 title이 내용에 맞지 않는다.

---

# Improvements

## 30. 안전한 Frontend 구조

Frontend는 vendor webhook URL을 직접 호출하지 않습니다.

```js
fetch(
  "/api/discord-message",
  {
    method: "POST",
    headers: {
      "Content-Type":
        "application/json"
    },
    body:
      JSON.stringify({
        content: prompt
      })
  }
)
```

backend가 환경 변수에 저장한 webhook URL을 사용해 Discord로 전달합니다.

---

## 31. 안전한 XHR 함수

```js
function sendDiscordMessage(
  content
) {
  return new Promise(
    function(
      resolve,
      reject
    ) {
      const xhr =
        new XMLHttpRequest()

      xhr.open(
        "POST",
        "/api/discord-message"
      )

      xhr.setRequestHeader(
        "Content-Type",
        "application/json"
      )

      xhr.onload =
        function() {
          if (
            xhr.status >= 200 &&
            xhr.status < 300
          ) {
            resolve()
          } else {
            reject(
              new Error(
                `HTTP ${xhr.status}`
              )
            )
          }
        }

      xhr.onerror =
        function() {
          reject(
            new Error(
              "네트워크 오류"
            )
          )
        }

      xhr.send(
        JSON.stringify({
          content
        })
      )
    }
  )
}
```

---

# Representative Examples

## 32. 상태 Message

HTML:

```html
<p
  id="status"
  role="status"
></p>
```

JavaScript:

```js
statusElement.textContent =
  "전송 중입니다."
```

성공:

```js
statusElement.textContent =
  "메시지를 전송했습니다."
```

실패:

```js
statusElement.textContent =
  "메시지 전송에 실패했습니다."
```

---

# Practical Usage

## 33. 완성된 Frontend 예제

```js
window.addEventListener(
  "DOMContentLoaded",
  function() {
    const prompt =
      document.querySelector(
        "#prompt"
      )

    const ask =
      document.querySelector(
        "#ask"
      )

    const status =
      document.querySelector(
        "#status"
      )

    ask.addEventListener(
      "click",
      async function() {
        const content =
          prompt
            .value
            .trim()

        if (content === "") {
          status.textContent =
            "메시지를 입력하세요."

          prompt.focus()

          return
        }

        if (ask.disabled) {
          return
        }

        ask.disabled = true
        status.textContent =
          "전송 중입니다."

        try {
          const response =
            await fetch(
              "/api/discord-message",
              {
                method: "POST",
                headers: {
                  "Content-Type":
                    "application/json"
                },
                body:
                  JSON.stringify({
                    content
                  })
              }
            )

          if (!response.ok) {
            throw new Error(
              `HTTP ${response.status}`
            )
          }

          status.textContent =
            "전송했습니다."

          prompt.value = ""
        } catch (error) {
          status.textContent =
            "전송에 실패했습니다."

          console.error(error)
        } finally {
          ask.disabled = false
          prompt.focus()
        }
      }
    )
  }
)
```

---

# Common Mistakes

## 34. 자주 하는 실수

### 34.1 Webhook URL을 Public Repository에 Commit

누구나 해당 URL로 message를 전송할 수 있습니다.

### 34.2 빈 URL로 XHR 전송

현재 document를 대상으로 요청할 수 있어 의도한 Discord 전송이 되지 않습니다.

### 34.3 Button Type 오타

`buttn`이 아니라 `button`입니다.

### 34.4 빈 Content 전송

trim과 validation이 필요합니다.

### 34.5 Onload만 확인

HTTP status가 실패일 수 있습니다.

### 34.6 Onerror 누락

network failure를 사용자에게 알릴 수 없습니다.

### 34.7 빠른 중복 Click

같은 message가 여러 번 전송될 수 있습니다.

### 34.8 ResponseText가 비어 있으면 실패라고 판단

성공 응답 body가 비어 있을 수 있으므로 status를 확인해야 합니다.

### 34.9 Frontend에 Secret 저장

browser code는 secret 저장소가 아닙니다.

### 34.10 Rate Limit 무시

과도한 요청은 제한될 수 있습니다.

---

# Interview / Review

## 35. 면접·복습 포인트

### Q1. Webhook은 무엇인가요?

외부 서비스가 제공한 URL에 HTTP 요청을 보내 특정 동작을 실행하는 방식입니다.

### Q2. Discord Webhook에 POST Body는 어떤 형식인가요?

JSON text 형식으로 username, content 등을 전달할 수 있습니다.

### Q3. JSON.stringify를 사용하는 이유는 무엇인가요?

JavaScript 객체를 JSON 문자열로 직렬화해 request body에 넣기 위해서입니다.

### Q4. Webhook URL을 Frontend에 넣으면 왜 위험한가요?

source와 network panel에서 URL이 노출되어 제3자가 악용할 수 있기 때문입니다.

### Q5. Onload만으로 성공을 판단할 수 있나요?

아닙니다. HTTP status를 확인해야 합니다.

### Q6. 내 코드가 실제 Discord로 전송되지 않는 이유는 무엇인가요?

URL이 빈 문자열이기 때문입니다.

### Q7. 내 HTML의 실제 오타는 무엇인가요?

button의 `type="buttn"`입니다.

### Q8. 성공 ResponseText가 비어 있을 수 있나요?

가능합니다. body보다 status를 기준으로 성공 여부를 판단해야 합니다.

### Q9. 중복 요청을 막는 방법은 무엇인가요?

요청 중 button을 disabled로 만들고 완료 후 다시 활성화합니다.

### Q10. Webhook URL은 어디에 저장하는 것이 적절한가요?

backend 환경 변수나 secret manager에 저장하는 구조가 적절합니다.

---

# Problems

## 문제 1. Textarea 값

`#prompt`의 값을 읽으세요.

## 문제 2. Trim

입력값의 앞뒤 공백을 제거하세요.

## 문제 3. 빈 값 검증

빈 message면 요청하지 않도록 작성하세요.

## 문제 4. XHR 생성

XMLHttpRequest 객체를 생성하세요.

## 문제 5. POST 설정

POST method와 backend endpoint를 설정하세요.

## 문제 6. JSON Header

Content-Type을 application/json으로 지정하세요.

## 문제 7. Payload

username과 content가 있는 객체를 만드세요.

## 문제 8. Stringify

payload를 JSON 문자열로 변환해 전송하세요.

## 문제 9. Status 검사

2xx status일 때 성공 처리하세요.

## 문제 10. Network Error

xhr.onerror를 작성하세요.

## 문제 11. Button Type

내 HTML의 `buttn` 오타를 수정하세요.

## 문제 12. 중복 요청 방지

요청 중 button을 disabled로 만드세요.

## 문제 13. 성공 후 초기화

성공 후 textarea를 비우세요.

## 문제 14. 사용자 상태 표시

전송 중·성공·실패 message를 화면에 출력하세요.

## 문제 15. Webhook 보안

실제 webhook URL을 frontend에 넣으면 안 되는 이유를 설명하세요.

## 문제 16. Backend Proxy

frontend가 `/api/discord-message`를 호출하는 구조를 작성하세요.

## 문제 17. Fetch 변환

원본 XHR 요청을 fetch로 다시 작성하세요.

## 문제 18. Response.ok

fetch에서 HTTP 실패를 처리하세요.

## 문제 19. Rate Limit

429 status를 별도로 안내하세요.

## 문제 20. Label

textarea와 연결된 label을 작성하세요.

## 문제 21. 원본 차이

내 코드와 강사님 코드의 URL, username, button, body 차이를 설명하세요.

## 문제 22. 종합 Discord 알림 Form

다음 요구사항을 만족하세요.

- textarea와 label
- 올바른 button type
- trim과 빈 값 검증
- backend endpoint로 POST
- JSON body
- 실제 webhook URL은 frontend에 없음
- 요청 중 button disabled
- HTTP status 검사
- 429 별도 안내
- network error 처리
- 성공 시 textarea 초기화
- 성공·실패 상태 message
- 재전송 가능하도록 finally에서 button 복구

---

# Answers

## 정답 1

```js
const value =
  document
    .querySelector(
      "#prompt"
    )
    .value
```

## 정답 2

```js
const content =
  value.trim()
```

## 정답 3

```js
if (content === "") {
  return
}
```

## 정답 4

```js
const xhr =
  new XMLHttpRequest()
```

## 정답 5

```js
xhr.open(
  "POST",
  "/api/discord-message"
)
```

## 정답 6

```js
xhr.setRequestHeader(
  "Content-Type",
  "application/json"
)
```

## 정답 7

```js
const param = {
  username:
    "알림봇",
  content
}
```

## 정답 8

```js
xhr.send(
  JSON.stringify(
    param
  )
)
```

## 정답 9

```js
xhr.onload =
  function() {
    if (
      xhr.status >= 200 &&
      xhr.status < 300
    ) {
      console.log(
        "전송 성공"
      )
    }
  }
```

## 정답 10

```js
xhr.onerror =
  function() {
    console.error(
      "네트워크 오류"
    )
  }
```

## 정답 11

```html
<button
  type="button"
  id="ask"
>
  디코에 말하기
</button>
```

## 정답 12

```js
ask.disabled =
  true

xhr.onloadend =
  function() {
    ask.disabled =
      false
  }
```

## 정답 13

```js
prompt.value = ""
```

## 정답 14

```js
status.textContent =
  "전송 중입니다."
```

## 정답 15

browser source에서 URL을 확인할 수 있어 제3자가 webhook을 이용해 임의 message를 전송할 수 있기 때문입니다.

## 정답 16

```js
fetch(
  "/api/discord-message",
  {
    method: "POST",
    headers: {
      "Content-Type":
        "application/json"
    },
    body:
      JSON.stringify({
        content
      })
  }
)
```

## 정답 17

```js
fetch(
  "/api/discord-message",
  {
    method: "POST",
    headers: {
      "Content-Type":
        "application/json"
    },
    body:
      JSON.stringify(
        param
      )
  }
)
```

## 정답 18

```js
if (!response.ok) {
  throw new Error(
    `HTTP ${response.status}`
  )
}
```

## 정답 19

```js
if (
  response.status === 429
) {
  throw new Error(
    "요청이 너무 많습니다."
  )
}
```

## 정답 20

```html
<label for="prompt">
  Discord 메시지
</label>

<textarea
  id="prompt"
></textarea>
```

## 정답 21

내 코드는 URL이 빈 문자열이고 username이 `zl존법사v`이며 button type이 `buttn`으로 잘못 작성되어 있고 body에 `test` text가 있습니다. 강사님 코드는 실제 webhook URL이 포함되어 있고 username은 `쵬니수`, button type은 올바른 `button`, button 뒤에는 `<br>`가 있습니다.

## 정답 22

```html
<label for="prompt">
  Discord 메시지
</label>

<textarea
  id="prompt"
></textarea>

<button
  type="button"
  id="ask"
>
  전송
</button>

<p
  id="status"
  role="status"
></p>
```

```js
const prompt =
  document.querySelector(
    "#prompt"
  )

const ask =
  document.querySelector(
    "#ask"
  )

const status =
  document.querySelector(
    "#status"
  )

ask.addEventListener(
  "click",
  async function() {
    const content =
      prompt
        .value
        .trim()

    if (content === "") {
      status.textContent =
        "메시지를 입력하세요."

      return
    }

    ask.disabled = true
    status.textContent =
      "전송 중입니다."

    try {
      const response =
        await fetch(
          "/api/discord-message",
          {
            method: "POST",
            headers: {
              "Content-Type":
                "application/json"
            },
            body:
              JSON.stringify({
                content
              })
          }
        )

      if (
        response.status ===
        429
      ) {
        throw new Error(
          "요청이 너무 많습니다."
        )
      }

      if (!response.ok) {
        throw new Error(
          `HTTP ${response.status}`
        )
      }

      status.textContent =
        "전송했습니다."

      prompt.value = ""
    } catch (error) {
      status.textContent =
        error.message

      console.error(error)
    } finally {
      ask.disabled = false
      prompt.focus()
    }
  }
)
```

---

# Final Checklist

## Request

- [ ] textarea 값을 읽었다.
- [ ] trim과 빈 값 검증을 했다.
- [ ] POST method를 사용했다.
- [ ] JSON header를 설정했다.
- [ ] payload를 stringify했다.
- [ ] 2xx status를 확인했다.
- [ ] network error를 처리했다.
- [ ] 429 rate limit을 고려했다.

## Security

- [ ] 실제 webhook URL을 frontend source에 넣지 않았다.
- [ ] webhook URL을 repository에 commit하지 않았다.
- [ ] 노출된 webhook은 재생성 또는 폐기했다.
- [ ] backend 환경 변수에 URL을 저장했다.
- [ ] frontend는 자신의 backend endpoint만 호출했다.
- [ ] 입력값 길이와 abuse 방지를 고려했다.

## UI

- [ ] button type을 올바르게 작성했다.
- [ ] textarea에 label을 연결했다.
- [ ] 요청 중 button을 비활성화했다.
- [ ] 성공·실패 상태를 표시했다.
- [ ] 성공 후 textarea를 초기화했다.
- [ ] finally에서 button과 focus를 복구했다.
- [ ] 임시 `test` text를 제거했다.

## 원본 검수

- [ ] 두 실제 `22_discord.html`만 비교했다.
- [ ] 내 URL이 빈 문자열임을 기록했다.
- [ ] 강사님 URL이 실제 credential임을 기록했다.
- [ ] 강사님 webhook URL 원문을 재노출하지 않았다.
- [ ] username 차이를 기록했다.
- [ ] 내 `type="buttn"` 오타를 기록했다.
- [ ] 내 body의 `test` text를 기록했다.
- [ ] 공통 status 검사 누락을 기록했다.
- [ ] 공통 onerror 누락을 기록했다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 22번은 Discord webhook에 message를 보내는 POST 요청을 다룬다.
- 두 원본 모두 HTML 안에 JavaScript가 포함된 단일 파일이다.
- textarea의 값을 읽어 `content` property에 넣는다.
- `XMLHttpRequest`를 생성하고 POST method로 webhook URL을 설정한다.
- `Content-Type: application/json` header를 사용한다.
- payload 객체는 `JSON.stringify()`로 JSON text로 변환한다.
- 내 코드는 webhook URL이 빈 문자열이라 실제 Discord 전송이 되지 않는다.
- 강사님 원본에는 실제 webhook URL이 포함되어 있어 credential 노출 위험이 있다.
- 문서에는 해당 webhook URL을 재출력하지 않았다.
- 노출된 webhook은 삭제 또는 재생성을 검토해야 한다.
- 실무에서는 webhook URL을 backend 환경 변수에 저장하는 구조가 적절하다.
- 내 username은 `zl존법사v`, 강사님 username은 `쵬니수`다.
- 강사님 코드에는 username 80자 제한 주석이 있다.
- 내 button에는 `type="buttn"` 오타가 있다.
- 강사님 button은 올바른 `type="button"`이다.
- 내 body에는 기능과 관계없는 `test` text가 남아 있다.
- 두 원본 모두 prompt trim과 빈 값 검증이 없다.
- 두 원본 모두 HTTP status를 검사하지 않는다.
- 두 원본 모두 `xhr.onerror`가 없다.
- 성공 response body가 비어 있을 수 있으므로 responseText만으로 성공 여부를 판단하면 안 된다.
- status code를 기준으로 성공 여부를 확인해야 한다.
- 빠른 연속 click은 같은 message를 중복 전송할 수 있다.
- 요청 중 button을 disabled로 만들고 완료 후 복구하는 방식이 필요하다.
- 성공·실패 상태를 사용자에게 화면으로 안내하는 것이 좋다.
