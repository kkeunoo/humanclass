# JavaScript Gemini API와 멀티턴 대화

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `21_JavaScript_Gemini_API와_멀티턴대화.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `20_JavaScript_AJAX와_Fetch_API.md` |
| 다음 학습 | 이후 JavaScript 원본 순서에 따라 진행 |
| 원본 기준 | `workspace/workspace_html/javascript/21_gemini.html`, `workspace_teacher/workspace_html/javascript/21_gemini.html` |
| 핵심 범위 | 생성형 AI API 요청, `fetch()` POST, request body, header, `JSON.stringify()`, response parsing, 중첩 응답 접근, 대화 history 배열, `role: "user"`, `role: "model"`, 멀티턴 구현, DOM 출력 |
| 프로젝트 연결 | AI 챗봇, 질문·응답 UI, conversation history, 외부 API 연동, 결과 렌더링, 오류 처리 |

> 이 문서는 내 코드와 강사님 코드의 `21_gemini.html`만 직접 비교했습니다. 두 원본 모두 Gemini 계열 API 호출을 학습하기 위한 예제로 작성되어 있으며, API key는 빈 문자열입니다. 내 코드는 응답 text를 화면에 출력하고 멀티턴 설명 주석을 추가했지만, 응답 DOM 생성 방식과 대화 history 저장 방식에 실제 문제가 있습니다. 또한 원본의 model URL과 API 형식이 현재도 유효한지는 이 문서의 비교 범위에서 별도로 검증하지 않았습니다. 원본에 적힌 문자열과 구조를 그대로 보존하고, 코드 자체의 동작과 개선점을 분리해 설명합니다.

---

# 학습 목표

- 생성형 AI API 요청의 기본 구조를 이해한다.
- `fetch()`로 POST 요청을 보낸다.
- request header에 API key와 content type을 설정한다.
- JavaScript 객체를 JSON 문자열로 변환해 body에 넣는다.
- single-turn 요청 body 구조를 이해한다.
- response JSON에서 text를 찾는다.
- 대화 history를 배열에 누적해 multi-turn 요청을 구성한다.
- `role: "user"`와 `role: "model"`의 의미를 이해한다.
- 내 코드와 강사님 코드의 실제 출력 차이를 설명한다.
- 내 코드의 DOM append 후 `innerText` 재할당 문제를 이해한다.
- model history에 전체 response JSON을 문자열로 저장하는 문제를 설명한다.
- API key를 client-side code에 직접 넣는 위험을 이해한다.
- HTTP 오류와 response shape 오류를 안전하게 처리한다.

---

# Core Concepts

## 1. 생성형 AI API 요청 흐름

원본의 전체 흐름:

```text
textarea에서 질문 읽기
→ request body 객체 생성
→ JSON.stringify()
→ fetch POST 요청
→ response.json()
→ 응답 객체 확인
→ text 출력
```

멀티턴에서는 여기에 다음이 추가됩니다.

```text
user 질문을 history에 push
→ history 전체를 body로 전송
→ model 응답을 history에 push
→ 다음 질문 때 누적 history 재전송
```

---

## 2. 전역 대화 History

양쪽 원본:

```js
const list = {
  contents: []
}
```

`contents` 배열에 user와 model message를 순서대로 저장하려는 구조입니다.

초기 상태:

```js
{
  contents: []
}
```

질문 후:

```js
{
  contents: [
    {
      role: "user",
      parts: [
        {
          text: "질문"
        }
      ]
    }
  ]
}
```

응답까지 저장하면 user와 model message가 번갈아 들어갑니다.

---

## 3. Window.onload

양쪽 원본:

```js
window.onload =
  function() {
    gemini()
  }
```

page와 resource가 load된 뒤 `gemini()`를 호출합니다.

`gemini()`는 실제 API를 즉시 호출하는 함수가 아니라 button event를 등록하는 초기화 함수입니다.

함수 이름은 다음처럼 더 구체적으로 지을 수 있습니다.

```js
initGeminiEvents()
```

---

## 4. 두 Button

HTML:

```html
<button
  type="button"
  id="ask"
>
  질문하기
</button>

<button
  type="button"
  id="ask2"
>
  멀티턴
</button>
```

역할:

```text
ask
→ 현재 prompt만 전송

ask2
→ 이전 대화 history와 현재 prompt를 함께 전송
```

내 HTML에서는 두 button의 type이 잘못 작성되어 있습니다.

```html
type="buttn"
```

강사님 HTML은 올바릅니다.

```html
type="button"
```

---

# Single-turn 요청

## 5. Prompt 읽기

양쪽 원본:

```js
const prompt =
  document
    .querySelector(
      "#prompt"
    )
    .value
```

textarea의 현재 문자열을 가져옵니다.

원본에는 빈 문자열 검증과 trim 처리가 없습니다.

개선:

```js
const prompt =
  promptInput
    .value
    .trim()

if (prompt === "") {
  alert(
    "질문을 입력하세요."
  )

  return
}
```

---

## 6. API Key

양쪽 원본:

```js
const key = ""
```

실제 key가 비어 있으므로 요청은 정상 인증되지 않을 가능성이 큽니다.

이 문서에는 key를 넣지 않습니다.

client-side JavaScript에 실제 API key를 직접 작성하면 browser source와 network panel에서 노출될 수 있습니다.

실무에서는 server가 key를 보관하고 frontend는 자신의 backend endpoint를 호출하는 구조를 검토합니다.

---

## 7. API URL

양쪽 원본:

```js
const url =
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent"
```

이 문서는 원본에 적힌 URL을 그대로 기록합니다.

다만 현재 실제 model 이름과 endpoint 지원 여부는 이 비교 작업에서 검증하지 않았습니다.

외부 AI API는 model 이름, version, 인증 방식이 변경될 수 있으므로 실제 사용 전 공식 문서를 확인해야 합니다.

---

## 8. Single-turn Data 구조

양쪽 원본:

```js
const data = {
  contents: [
    {
      parts: [
        {
          text: prompt
        }
      ]
    }
  ]
}
```

구조:

```text
data
└─ contents
   └─ 첫 번째 message
      └─ parts
         └─ 첫 번째 part
            └─ text
```

single-turn 요청에서는 role을 생략하고 text만 전달합니다.

---

## 9. Fetch POST

양쪽 원본:

```js
fetch(
  url,
  {
    method: "POST",
    headers: {
      "x-goog-api-key":
        key,
      "Content-Type":
        "application/json"
    },
    body:
      JSON.stringify(
        data
      )
  }
)
```

핵심:

```text
method
→ POST

x-goog-api-key
→ API 인증

Content-Type
→ JSON request body임을 알림

body
→ JavaScript 객체를 JSON text로 변환
```

---

## 10. 내 JSON 주석

내 코드:

```js
// JSON으로 날아가면 안되기 때문에,
// 문자열로 변경해서 전달
```

의도는 request body에 JavaScript 객체를 직접 넣지 않고 JSON 문자열로 직렬화해야 한다는 뜻입니다.

더 정확한 표현:

```text
JavaScript 객체를 HTTP request body에 JSON text로 전달하기 위해
JSON.stringify()를 사용한다.
```

“JSON으로 날아가면 안 된다”는 표현은 부정확합니다.

실제로 content type은 `application/json`이고 body는 JSON text입니다.

---

# Response 처리

## 11. Response.json()

양쪽 원본:

```js
.then(
  function(response) {
    return response.json()
  }
)
```

`response.json()`은 response body를 parsing하는 Promise를 반환합니다.

다음 `.then()`에서 parsing된 JavaScript object를 받습니다.

---

## 12. 강사님 Single-turn 출력

강사님:

```js
.then(
  function(result) {
    console.log(result)
  }
)
```

전체 response object를 Console에 출력합니다.

장점:

- 실제 response 구조 확인 가능
- candidates 유무 확인 가능
- error response 분석 가능

---

## 13. 내 Single-turn 출력

내 코드:

```js
console.log(
  result[
    "candidates"
  ][
    "0"
  ][
    "content"
  ][
    "parts"
  ][
    "0"
  ][
    "text"
  ]
)
```

응답의 text만 직접 찾습니다.

dot notation으로 표현하면:

```js
result
  .candidates[0]
  .content
  .parts[0]
  .text
```

---

## 14. 문자열 `"0"` Index

내 코드는 array index를 string `"0"`으로 작성합니다.

```js
result["candidates"]["0"]
```

JavaScript array의 property key는 내부적으로 string key로 접근할 수 있어 동작할 수 있습니다.

하지만 일반적인 array 표기는 다음이 더 명확합니다.

```js
result.candidates[0]
```

---

## 15. Response Shape 오류 가능성

다음 구조가 항상 있다고 가정합니다.

```text
candidates[0].content.parts[0].text
```

인증 실패, quota 오류, safety block, server error 등에서는 구조가 다를 수 있습니다.

그 경우 다음과 같은 TypeError가 발생할 수 있습니다.

```text
Cannot read properties of undefined
```

안전한 접근:

```js
const text =
  result
    ?.candidates
    ?.[0]
    ?.content
    ?.parts
    ?.[0]
    ?.text
```

---

## 16. Response.ok 검사 누락

양쪽 원본은:

```js
return response.json()
```

만 실행하고 `response.ok`를 검사하지 않습니다.

HTTP 오류도 JSON body를 반환할 수 있으므로 다음처럼 처리할 수 있습니다.

```js
if (!response.ok) {
  throw new Error(
    `HTTP ${response.status}`
  )
}
```

---

# 내 DOM 출력

## 17. AskResult 추가

내 HTML에만 존재:

```html
<div id="askResult"></div>
```

강사님 HTML에는 없습니다.

내 코드는 API response text를 화면에 표시하려고 합니다.

---

## 18. Div 생성

내 코드:

```js
const divAdd =
  document.createElement(
    "div"
  )

const askResult =
  document.querySelector(
    "#askResult"
  )

askResult.append(
  divAdd
)
```

빈 div를 `#askResult` 안에 추가합니다.

---

## 19. InnerText 재할당 문제

곧바로:

```js
askResult.innerText =
  responseText
```

를 실행합니다.

`innerText`를 parent에 재할당하면 기존 child content가 대체됩니다.

따라서 직전에 append한 `divAdd`는 실제로 유지되지 않습니다.

결과적으로 화면에는 response text만 남습니다.

의도대로 새 div에 넣으려면:

```js
divAdd.innerText =
  responseText

askResult.append(
  divAdd
)
```

순서로 작성해야 합니다.

---

## 20. 대화 누적 출력 문제

현재는 매 응답마다:

```js
askResult.innerText =
  responseText
```

를 실행하므로 이전 출력이 모두 사라집니다.

multi-turn history는 request body에는 누적되지만 화면에는 마지막 응답만 표시됩니다.

chat UI라면 user message와 model message를 각각 새 element로 append해야 합니다.

---

# Multi-turn 요청

## 21. User Message Push

양쪽 원본:

```js
list.contents.push({
  role: "user",
  parts: [
    {
      text: prompt
    }
  ]
})
```

현재 질문을 대화 history 끝에 추가합니다.

---

## 22. History 전체 전송

```js
body:
  JSON.stringify(
    list
  )
```

single-turn의 `data` 대신 누적된 `list` 전체를 전송합니다.

이 방식으로 이전 대화 문맥을 model에게 다시 전달하려는 구조입니다.

---

## 23. Model Message Push

양쪽 원본:

```js
list.contents.push({
  role: "model",
  parts: [
    {
      text:
        JSON.stringify(
          result
        )
    }
  ]
})
```

응답을 model message로 추가합니다.

---

## 24. 전체 Result 저장 문제

현재 저장하는 값:

```js
JSON.stringify(result)
```

은 model이 생성한 실제 답변 text가 아니라 전체 API response object의 JSON 문자열입니다.

다음 요청 때 history에는 이런 형태가 들어갑니다.

```text
{
  "candidates": [...],
  "usageMetadata": ...,
  ...
}
```

대화 문맥으로 저장해야 할 값은 보통 model의 실제 응답 text입니다.

```js
const answer =
  result
    .candidates[0]
    .content
    .parts[0]
    .text

list.contents.push({
  role: "model",
  parts: [
    {
      text: answer
    }
  ]
})
```

---

## 25. 실패한 User Message가 History에 남는 문제

user message는 fetch 전에 push됩니다.

```js
list.contents.push(
  userMessage
)

fetch(...)
```

요청이 실패해도 user message는 list에 남습니다.

다음 재시도에서는 실패했던 질문이 history에 중복되거나 model response 없이 남을 수 있습니다.

개선 방법:

- 요청 성공 후 history 확정
- 실패 시 마지막 user message 제거
- pending state를 별도로 관리

예:

```js
const message = {
  role: "user",
  parts: [
    {
      text: prompt
    }
  ]
}

list.contents.push(message)

try {
  // 요청
} catch (error) {
  list.contents.pop()
}
```

---

## 26. 연속 클릭 문제

원본에는 loading state나 button disabled가 없습니다.

사용자가 빠르게 여러 번 클릭하면:

- 요청 순서와 응답 순서가 달라질 수 있음
- history 순서가 꼬일 수 있음
- 같은 prompt가 여러 번 들어갈 수 있음
- UI 응답이 뒤섞일 수 있음

요청 중 button을 disable하는 방식이 필요할 수 있습니다.

---

# Error 처리

## 27. Catch

양쪽 원본:

```js
.catch(
  function(error) {
    console.error(
      "요청 중 에러",
      error
    )
  }
)
```

network failure, parsing rejection, then callback 내부 오류 등을 처리할 수 있습니다.

하지만 HTTP 400·401·500이 자동으로 catch되는 것은 아닙니다.

---

## 28. Error Response Body

AI API는 HTTP 오류일 때도 JSON error body를 반환할 수 있습니다.

안전한 예:

```js
const result =
  await response.json()

if (!response.ok) {
  const message =
    result
      ?.error
      ?.message ??
    `HTTP ${response.status}`

  throw new Error(message)
}
```

---

# HTML 비교

## 29. 강사님 HTML

강사님 body:

```html
<textarea id="prompt"></textarea>
<br>
<button
  type="button"
  id="ask"
>
  질문하기
</button>
<br>
<button
  type="button"
  id="ask2"
>
  멀티턴
</button>
```

특징:

- button type 정상
- 두 button 사이 line break
- 결과 출력 element 없음

---

## 30. 내 HTML

내 body:

```html
<textarea id="prompt"></textarea>
<br>
<button
  type="buttn"
  id="ask"
>
  질문하기
</button>
<button
  type="buttn"
  id="ask2"
>
  멀티턴
</button>
<div id="askResult"></div>
```

특징:

- `type="buttn"` 오타
- 두 button이 같은 줄
- 결과 표시 div 추가
- closing body 뒤에 trailing space
- 파일 마지막 newline 없음

---

## 31. Unknown Button Type

HTML button의 기본 type은 form 내부에서는 `submit`입니다.

원본 button은 form 밖에 있어 현재 예제에서는 submit 문제가 드러나지 않습니다.

하지만 `type="buttn"`은 유효한 button type이 아닙니다.

정확히:

```html
type="button"
```

으로 작성해야 합니다.

---

## 32. 문서 언어와 Title

양쪽 원본:

```html
<html lang="en">
<title>Document</title>
```

한국어 UI이므로 다음이 더 적절합니다.

```html
<html lang="ko">
<title>Gemini API 실습</title>
```

---

# My Code vs Teacher Code

## 33. 비교표

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 원본 파일 | `21_gemini.html` | `21_gemini.html` |
| API key | 빈 문자열 | 빈 문자열 |
| API URL | 동일 | 동일 |
| Single-turn request body | 동일 | 동일 |
| Multi-turn history | 동일한 기본 구조 | 동일한 기본 구조 |
| Single-turn Console | answer text만 출력 | result 전체 출력 |
| Multi-turn Console | answer text만 출력 | result 전체 출력 |
| 결과 DOM | `#askResult` 추가 | 없음 |
| DOM 출력 | 마지막 text로 교체 | 미구현 |
| 빈 div 생성 | 생성 후 parent innerText로 제거됨 | 없음 |
| Multi-turn 설명 | 상세 주석 추가 | 없음 |
| Button type | `buttn` 오타 | `button` 정상 |
| Button 배치 | 같은 줄 | `<br>`로 분리 |
| 응답 history 저장 | 전체 result JSON 문자열 | 전체 result JSON 문자열 |
| Response.ok | 검사하지 않음 | 검사하지 않음 |
| Prompt 검증 | 없음 | 없음 |

---

# My Code Analysis

## 34. 내 코드 장점

- request body를 문자열로 바꾸는 이유를 주석으로 설명했다.
- response의 실제 answer text 경로를 직접 찾아 출력했다.
- API 결과를 Console뿐 아니라 화면에 표시하려고 시도했다.
- multi-turn이 user와 model message를 history에 저장하는 구조임을 설명했다.
- single-turn과 multi-turn button을 분리했다.
- request 실패를 catch로 처리했다.
- 강사님 코드보다 학습용 설명이 풍부하다.

---

## 35. 내 코드 개선점

- `type="buttn"` 오타가 두 곳에 있다.
- prompt trim과 빈 값 검증이 없다.
- API key가 빈 문자열이다.
- API key를 browser code에 직접 넣는 구조다.
- 현재 model URL이 유효한지 확인하지 않는다.
- `response.ok`를 검사하지 않는다.
- response shape를 고정으로 가정한다.
- optional chaining이나 fallback이 없다.
- `divAdd`를 append한 뒤 parent `innerText`로 제거한다.
- 화면에는 마지막 응답만 남는다.
- user message는 화면에 표시하지 않는다.
- model history에 answer text가 아니라 전체 result JSON을 넣는다.
- 요청 실패 시 user history가 그대로 남는다.
- 연속 클릭 방지가 없다.
- 입력 textarea를 응답 후 비우지 않는다.
- `lang="en"`과 title이 내용에 맞지 않는다.

---

# Teacher Code Analysis

## 36. 강사님 코드 장점

- single-turn request 구조가 간결하다.
- full response object를 Console에 출력해 API 구조를 확인하기 좋다.
- multi-turn history의 user/model role 구조를 보여 준다.
- fetch POST와 JSON.stringify를 연결한다.
- catch를 통해 request 오류를 확인한다.
- button type이 올바르다.
- 내 코드보다 불필요한 DOM 조작이 적다.

---

## 37. 강사님 코드 개선점

- prompt 검증이 없다.
- API key가 빈 문자열이다.
- 실제 key를 frontend에 넣으면 노출된다.
- 현재 model endpoint 유효성을 확인하지 않는다.
- `response.ok`를 검사하지 않는다.
- response JSON의 error shape를 처리하지 않는다.
- model history에 전체 response JSON 문자열을 저장한다.
- 요청 실패 시 user message가 history에 남는다.
- 결과를 화면에 표시하지 않는다.
- loading state와 중복 요청 방지가 없다.
- 대화 history 크기 제한이 없다.
- `lang="en"`과 title이 내용에 맞지 않는다.

---

# Improvements

## 38. Response Text 추출 함수

```js
function getAnswerText(
  result
) {
  const text =
    result
      ?.candidates
      ?.[0]
      ?.content
      ?.parts
      ?.[0]
      ?.text

  if (
    typeof text !==
    "string"
  ) {
    throw new Error(
      "응답 text를 찾지 못했습니다."
    )
  }

  return text
}
```

---

## 39. Message 생성 함수

```js
function createMessage(
  role,
  text
) {
  return {
    role,
    parts: [
      {
        text
      }
    ]
  }
}
```

사용:

```js
const userMessage =
  createMessage(
    "user",
    prompt
  )

const modelMessage =
  createMessage(
    "model",
    answer
  )
```

---

## 40. 안전한 Request 함수

```js
async function requestGemini(
  contents
) {
  const response =
    await fetch(
      "/api/gemini",
      {
        method: "POST",
        headers: {
          "Content-Type":
            "application/json"
        },
        body:
          JSON.stringify({
            contents
          })
      }
    )

  const result =
    await response.json()

  if (!response.ok) {
    throw new Error(
      result
        ?.error
        ?.message ??
      `HTTP ${response.status}`
    )
  }

  return getAnswerText(
    result
  )
}
```

이 예제는 frontend에 vendor API key를 두지 않고 자신의 backend endpoint를 호출하는 구조입니다.

---

# Representative Examples

## 41. Chat Message 렌더링

```js
function appendMessage(
  container,
  role,
  text
) {
  const message =
    document.createElement(
      "div"
    )

  message.classList.add(
    "message",
    `message--${role}`
  )

  const label =
    document.createElement(
      "strong"
    )

  label.textContent =
    role === "user"
      ? "나"
      : "AI"

  const content =
    document.createElement(
      "p"
    )

  content.textContent =
    text

  message.append(
    label,
    content
  )

  container.append(
    message
  )
}
```

`textContent`를 사용하므로 model response에 HTML처럼 보이는 문자열이 있어도 code로 실행하지 않습니다.

---

# Practical Usage

## 42. 안전한 Multi-turn Chat

```js
const history = []

const promptInput =
  document.querySelector(
    "#prompt"
  )

const askButton =
  document.querySelector(
    "#ask2"
  )

const resultArea =
  document.querySelector(
    "#askResult"
  )

askButton.addEventListener(
  "click",
  async function() {
    const prompt =
      promptInput
        .value
        .trim()

    if (prompt === "") {
      alert(
        "질문을 입력하세요."
      )

      return
    }

    if (askButton.disabled) {
      return
    }

    const userMessage =
      createMessage(
        "user",
        prompt
      )

    askButton.disabled =
      true

    history.push(
      userMessage
    )

    appendMessage(
      resultArea,
      "user",
      prompt
    )

    try {
      const answer =
        await requestGemini(
          history
        )

      const modelMessage =
        createMessage(
          "model",
          answer
        )

      history.push(
        modelMessage
      )

      appendMessage(
        resultArea,
        "model",
        answer
      )

      promptInput.value =
        ""
    } catch (error) {
      history.pop()

      appendMessage(
        resultArea,
        "error",
        error.message
      )

      console.error(error)
    } finally {
      askButton.disabled =
        false

      promptInput.focus()
    }
  }
)
```

---

## 43. History 크기 제한

대화가 길어질수록 request body가 커집니다.

간단한 제한 예:

```js
const MAX_MESSAGES = 20

if (
  history.length >
  MAX_MESSAGES
) {
  history.splice(
    0,
    history.length -
      MAX_MESSAGES
  )
}
```

실제 AI API에서는 token limit과 system instruction 구조를 함께 고려해야 합니다.

---

# Common Mistakes

## 44. 자주 하는 실수

### 44.1 API Key를 HTML에 직접 작성

browser에서 누구나 확인할 수 있습니다.

### 44.2 JavaScript 객체를 Body에 그대로 전달

JSON API라면 `JSON.stringify()`가 필요합니다.

### 44.3 Content-Type만 JSON이면 객체를 자동 변환한다고 생각

header는 형식을 알릴 뿐 body 직렬화는 별도입니다.

### 44.4 Response.ok를 검사하지 않음

HTTP 오류를 정상 response처럼 parsing할 수 있습니다.

### 44.5 Candidates가 항상 존재한다고 가정

error나 blocked response에서는 없을 수 있습니다.

### 44.6 Parent InnerText로 Child 제거

append한 message element가 사라집니다.

### 44.7 Model History에 전체 API Result 저장

다음 대화에는 실제 answer text를 저장해야 합니다.

### 44.8 실패한 User Message를 History에 유지

다음 요청의 문맥이 잘못될 수 있습니다.

### 44.9 연속 Click을 허용

응답 순서와 history 순서가 꼬일 수 있습니다.

### 44.10 유효하지 않은 Button Type 사용

`type="buttn"`이 아니라 `type="button"`입니다.

---

# Interview / Review

## 45. 면접·복습 포인트

### Q1. 생성형 AI API 요청에서 POST를 사용하는 이유는 무엇인가요?

질문과 대화 history 같은 request body를 server에 전달하기 위해서입니다.

### Q2. JSON.stringify를 사용하는 이유는 무엇인가요?

JavaScript 객체를 JSON text로 직렬화해 HTTP body에 넣기 위해서입니다.

### Q3. Single-turn과 Multi-turn 차이는 무엇인가요?

single-turn은 현재 질문만 보내고 multi-turn은 이전 user와 model message history를 함께 보냅니다.

### Q4. Role은 무엇을 나타내나요?

message가 user가 보낸 것인지 model이 생성한 것인지 구분합니다.

### Q5. 내 DOM 출력에서 빈 Div가 사라지는 이유는 무엇인가요?

child를 append한 뒤 parent의 innerText를 다시 지정해 기존 child를 교체하기 때문입니다.

### Q6. Model History에 JSON.stringify(result)를 넣는 문제는 무엇인가요?

실제 model 답변이 아니라 metadata를 포함한 전체 API response가 다음 대화 문맥으로 들어갑니다.

### Q7. Fetch Catch가 HTTP 401도 자동 처리하나요?

항상 그렇지 않습니다. response.ok를 검사하고 직접 error를 발생시켜야 합니다.

### Q8. API Key를 Frontend에 넣으면 왜 위험한가요?

source와 network request에서 key가 노출될 수 있기 때문입니다.

### Q9. Optional Chaining이 필요한 이유는 무엇인가요?

응답 구조 일부가 없을 때 TypeError 대신 안전하게 undefined를 얻기 위해서입니다.

### Q10. Multi-turn에서 요청 중 Button을 막는 이유는 무엇인가요?

중복 요청과 response 순서 역전으로 history가 꼬이는 것을 줄이기 위해서입니다.

---

# Problems

## 문제 1. Prompt 읽기

textarea `#prompt`의 값을 trim해서 가져오세요.

## 문제 2. 빈 질문 검증

질문이 비어 있으면 요청하지 않고 안내하세요.

## 문제 3. Single-turn Data

현재 prompt를 `contents[].parts[].text` 구조에 넣으세요.

## 문제 4. Fetch POST

JSON request body로 POST 요청을 작성하세요.

## 문제 5. Header

API key header와 JSON content type을 설정하세요.

## 문제 6. Stringify

request data를 JSON text로 변환하세요.

## 문제 7. Response JSON

response body를 JavaScript object로 parsing하세요.

## 문제 8. Response OK

HTTP 오류 상태면 error를 발생시키세요.

## 문제 9. Answer Text

`candidates[0].content.parts[0].text`를 읽으세요.

## 문제 10. Optional Chaining

응답 구조가 없을 때 안전하게 text를 확인하세요.

## 문제 11. User Message

role이 user인 message 객체를 만드세요.

## 문제 12. Model Message

role이 model인 message 객체를 만드세요.

## 문제 13. Multi-turn History

user와 model message를 순서대로 history에 추가하세요.

## 문제 14. History Body

history 전체를 `contents`로 전송하세요.

## 문제 15. 실패 Rollback

요청 실패 시 마지막 user message를 history에서 제거하세요.

## 문제 16. DOM Message

새 div에 response text를 넣고 결과 영역에 append하세요.

## 문제 17. 기존 대화 유지

parent innerText 재할당 없이 message를 누적하세요.

## 문제 18. Button Type

내 HTML의 `buttn` 오타를 수정하세요.

## 문제 19. 중복 요청 방지

요청 중 button을 disabled로 만드세요.

## 문제 20. API Key 보호

Frontend에 직접 key를 넣지 않는 구조를 설명하세요.

## 문제 21. 원본 차이

내 코드와 강사님 코드의 응답 출력과 HTML 차이를 설명하세요.

## 문제 22. 종합 AI Chat

다음 요구사항을 만족하세요.

- textarea 질문 입력
- 빈 값 검증
- multi-turn history
- user와 model role 구분
- POST JSON 요청
- response.ok 검사
- answer text 안전 추출
- user·model message 화면 누적
- textContent 사용
- 요청 중 button disabled
- 실패 시 user history rollback
- 오류 메시지 표시
- 요청 성공 후 textarea 초기화와 focus
- frontend에는 실제 vendor API key를 두지 않음

---

# Answers

## 정답 1

```js
const prompt =
  document
    .querySelector(
      "#prompt"
    )
    .value
    .trim()
```

## 정답 2

```js
if (prompt === "") {
  alert(
    "질문을 입력하세요."
  )

  return
}
```

## 정답 3

```js
const data = {
  contents: [
    {
      parts: [
        {
          text: prompt
        }
      ]
    }
  ]
}
```

## 정답 4

```js
fetch(
  url,
  {
    method: "POST",
    headers,
    body:
      JSON.stringify(
        data
      )
  }
)
```

## 정답 5

```js
const headers = {
  "x-goog-api-key":
    key,
  "Content-Type":
    "application/json"
}
```

## 정답 6

```js
const body =
  JSON.stringify(data)
```

## 정답 7

```js
const result =
  await response.json()
```

## 정답 8

```js
if (!response.ok) {
  throw new Error(
    `HTTP ${response.status}`
  )
}
```

## 정답 9

```js
const text =
  result
    .candidates[0]
    .content
    .parts[0]
    .text
```

## 정답 10

```js
const text =
  result
    ?.candidates
    ?.[0]
    ?.content
    ?.parts
    ?.[0]
    ?.text
```

## 정답 11

```js
const userMessage = {
  role: "user",
  parts: [
    {
      text: prompt
    }
  ]
}
```

## 정답 12

```js
const modelMessage = {
  role: "model",
  parts: [
    {
      text: answer
    }
  ]
}
```

## 정답 13

```js
history.push(
  userMessage
)

history.push(
  modelMessage
)
```

## 정답 14

```js
body:
  JSON.stringify({
    contents:
      history
  })
```

## 정답 15

```js
try {
  // 요청
} catch (error) {
  history.pop()
}
```

## 정답 16

```js
const message =
  document.createElement(
    "div"
  )

message.textContent =
  answer

resultArea.append(
  message
)
```

## 정답 17

```js
resultArea.append(
  message
)
```

parent의 `innerText`나 `innerHTML`을 다시 지정하지 않습니다.

## 정답 18

```html
<button
  type="button"
  id="ask"
>
  질문하기
</button>
```

## 정답 19

```js
button.disabled =
  true

try {
  // 요청
} finally {
  button.disabled =
    false
}
```

## 정답 20

Frontend는 자신의 backend endpoint를 호출하고 backend가 환경 변수 등에 보관한 vendor API key로 외부 AI API를 호출합니다.

## 정답 21

강사님 코드는 single-turn과 multi-turn 모두 전체 result 객체를 Console에 출력하고 화면 출력 element가 없습니다. 내 코드는 answer text만 Console과 `#askResult`에 표시하려 하지만 빈 div를 append한 뒤 parent `innerText`를 지정해 그 div를 제거합니다. 또한 내 두 button은 `type="buttn"` 오타이고 강사님은 `type="button"`입니다.

## 정답 22

```js
const history = []

const promptInput =
  document.querySelector(
    "#prompt"
  )

const button =
  document.querySelector(
    "#ask2"
  )

const output =
  document.querySelector(
    "#askResult"
  )

function createMessage(
  role,
  text
) {
  return {
    role,
    parts: [
      {
        text
      }
    ]
  }
}

function appendMessage(
  role,
  text
) {
  const div =
    document.createElement(
      "div"
    )

  div.classList.add(
    "message",
    `message--${role}`
  )

  div.textContent =
    `${role}: ${text}`

  output.append(div)
}

function getAnswerText(
  result
) {
  const answer =
    result
      ?.candidates
      ?.[0]
      ?.content
      ?.parts
      ?.[0]
      ?.text

  if (
    typeof answer !==
    "string"
  ) {
    throw new Error(
      "답변을 찾지 못했습니다."
    )
  }

  return answer
}

button.addEventListener(
  "click",
  async function() {
    const prompt =
      promptInput
        .value
        .trim()

    if (
      prompt === "" ||
      button.disabled
    ) {
      return
    }

    const userMessage =
      createMessage(
        "user",
        prompt
      )

    history.push(
      userMessage
    )

    appendMessage(
      "user",
      prompt
    )

    button.disabled =
      true

    try {
      const response =
        await fetch(
          "/api/gemini",
          {
            method: "POST",
            headers: {
              "Content-Type":
                "application/json"
            },
            body:
              JSON.stringify({
                contents:
                  history
              })
          }
        )

      const result =
        await response.json()

      if (!response.ok) {
        throw new Error(
          result
            ?.error
            ?.message ??
          `HTTP ${response.status}`
        )
      }

      const answer =
        getAnswerText(
          result
        )

      history.push(
        createMessage(
          "model",
          answer
        )
      )

      appendMessage(
        "model",
        answer
      )

      promptInput.value =
        ""
    } catch (error) {
      history.pop()

      appendMessage(
        "error",
        error.message
      )

      console.error(error)
    } finally {
      button.disabled =
        false

      promptInput.focus()
    }
  }
)
```

---

# Final Checklist

## API 요청

- [ ] prompt를 trim했다.
- [ ] 빈 질문을 차단했다.
- [ ] POST method를 사용했다.
- [ ] JSON content type을 지정했다.
- [ ] JavaScript 객체를 stringify했다.
- [ ] response body를 JSON으로 parsing했다.
- [ ] response.ok를 검사했다.
- [ ] error response body를 처리했다.
- [ ] 현재 model endpoint 지원 여부를 공식 문서에서 별도로 확인했다.

## Multi-turn

- [ ] user message에 role을 지정했다.
- [ ] model message에 role을 지정했다.
- [ ] history 순서를 유지했다.
- [ ] model answer text만 history에 저장했다.
- [ ] 전체 API result를 history에 넣지 않았다.
- [ ] 실패 시 user message를 rollback했다.
- [ ] history 크기와 token limit을 고려했다.
- [ ] 중복 요청을 막았다.

## DOM

- [ ] button type을 올바르게 작성했다.
- [ ] message element 자체에 text를 넣었다.
- [ ] parent innerText 재할당을 피했다.
- [ ] 이전 대화를 화면에 누적했다.
- [ ] user와 model message를 구분했다.
- [ ] textContent를 사용했다.
- [ ] loading과 error 상태를 표시했다.
- [ ] 성공 후 textarea를 초기화했다.

## Security

- [ ] 실제 API key를 client-side source에 넣지 않았다.
- [ ] backend proxy 구조를 검토했다.
- [ ] key를 repository에 commit하지 않았다.
- [ ] request quota와 abuse 방지를 고려했다.
- [ ] 사용자 입력과 model 출력을 HTML로 실행하지 않았다.

## 원본 검수

- [ ] 두 실제 `21_gemini.html`만 비교했다.
- [ ] 내 answer text 출력과 강사님 전체 result 출력을 기록했다.
- [ ] 내 `#askResult` 추가를 기록했다.
- [ ] 내 `type="buttn"` 오타 두 곳을 기록했다.
- [ ] 내 append 후 parent innerText 문제를 기록했다.
- [ ] 공통 model history 저장 문제를 기록했다.
- [ ] 공통 response.ok 누락을 기록했다.
- [ ] 공통 API key 빈 문자열을 기록했다.
- [ ] model URL의 현재 유효성을 임의로 단정하지 않았다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 21번은 생성형 AI API의 single-turn과 multi-turn 요청을 다룬다.
- 두 원본 모두 `21_gemini.html` 하나에 HTML과 JavaScript가 함께 있다.
- `list.contents`는 대화 message history를 저장하려는 배열이다.
- `ask` button은 현재 질문만 보내는 single-turn 요청이다.
- `ask2` button은 이전 history를 함께 보내는 multi-turn 요청이다.
- request body는 `contents[].parts[].text` 구조다.
- JavaScript 객체를 JSON text로 보내기 위해 `JSON.stringify()`를 사용한다.
- `Content-Type: application/json`은 body 형식을 알리는 header다.
- `response.json()`은 response body를 parsing하는 Promise를 반환한다.
- 강사님 코드는 전체 result 객체를 Console에 출력한다.
- 내 코드는 `candidates[0].content.parts[0].text`만 직접 출력한다.
- 내 array index `"0"` 표기는 동작할 수 있지만 `[0]`이 더 명확하다.
- response shape가 다르면 직접 property 접근에서 TypeError가 발생할 수 있다.
- optional chaining과 fallback 검사가 필요하다.
- 두 원본 모두 response.ok를 검사하지 않는다.
- HTTP 오류도 JSON body를 반환할 수 있으므로 status 처리가 필요하다.
- 내 HTML에는 `#askResult`가 있지만 강사님 HTML에는 없다.
- 내 코드는 빈 div를 append한 뒤 parent `innerText`를 지정해 방금 만든 div를 제거한다.
- 내 화면 출력은 이전 대화를 누적하지 않고 마지막 answer로 교체한다.
- multi-turn에서는 user message를 fetch 전에 history에 push한다.
- 요청이 실패해도 user message가 history에 남을 수 있다.
- 두 원본 모두 model history에 answer text 대신 전체 result JSON 문자열을 저장한다.
- 다음 대화 문맥에는 실제 model answer text를 넣는 편이 적절하다.
- 내 두 button에는 `type="buttn"` 오타가 있다.
- 강사님 button type은 올바른 `button`이다.
- 실제 API key를 frontend JavaScript에 넣으면 노출될 수 있다.
- 실무에서는 backend가 key를 보관하는 구조를 검토한다.
- 원본의 model URL이 현재 유효한지는 이 비교 작업에서 검증하지 않았다.
- 외부 AI API를 실제 사용할 때는 공식 문서에서 model 이름과 endpoint를 확인해야 한다.
