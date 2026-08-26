---
title: JavaScript Gemini API와 멀티턴 대화
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# JavaScript Gemini API와 멀티턴 대화

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `21_JavaScript_Gemini_API와_멀티턴대화.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/21_gemini.html`, `workspace_teacher/workspace_html/javascript/21_gemini.html` |
| 핵심 범위 | Gemini API, POST 요청, Header, JSON Body, 응답 구조, 멀티턴 History, 오류·보안·UI 상태 |
| 실습 범위 | 단일 질문, 대화 누적, 응답 렌더링, 중복 요청 방지, Backend Proxy 구조 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 21번은 생성형 AI API에 질문을 전송하고 응답을 화면에 표시하는 흐름을 다룬다.  
> 원본의 API Key는 빈 문자열이며 실제 Key를 문서나 Client JavaScript에 추가하지 않는다.

---

# 개요

생성형 AI API 요청도 일반적인 JSON API 요청 흐름을 따른다.

```text
사용자 질문 입력
    ↓
요청 객체 생성
    ↓
JSON 문자열 변환
    ↓
POST 요청
    ↓
응답 JSON 변환
    ↓
생성된 Text 추출
    ↓
화면 출력
```

멀티턴 대화에서는 이전 사용자 질문과 Model 답변을 History에 누적한다.

```text
User 질문 저장
    ↓
전체 History 전송
    ↓
Model 응답 저장
    ↓
다음 질문에서 다시 전체 History 전송
```

> [!IMPORTANT]
> 멀티턴 대화의 핵심은 Model이 Browser 변수를 직접 기억하는 것이 아니다.  
> Client가 이전 대화를 다시 요청에 포함해 Context를 제공하는 것이다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| API Endpoint | 요청을 전송할 서버 주소 |
| API Key | 요청 인증 정보 |
| POST | 데이터를 Body에 담아 전송 |
| Header | 인증 방식과 Body 형식 전달 |
| `Content-Type` | 전송 데이터 형식 지정 |
| `contents` | 대화 Turn 목록 |
| `parts` | 한 Turn 안의 Text·Image 등 입력 단위 |
| `role` | `user` 또는 `model` 발화자 |
| Candidate | Model이 생성한 응답 후보 |
| Conversation History | 이전 질문과 답변의 누적 목록 |
| Loading State | 요청 중 화면 상태 |
| Backend Proxy | Client 대신 외부 API에 안전하게 요청하는 서버 |

---

# 학습 목표

- 생성형 AI API 요청 구조를 설명할 수 있다.
- `fetch()`로 JSON POST 요청을 보낼 수 있다.
- API Key Header와 Content Type Header의 역할을 이해한다.
- JavaScript 객체와 JSON 문자열을 구분할 수 있다.
- 단일 질문용 `contents` 구조를 만들 수 있다.
- 응답의 중첩 구조에서 Text를 안전하게 추출할 수 있다.
- HTTP 오류와 응답 구조 오류를 구분할 수 있다.
- 사용자 질문과 Model 답변을 History에 올바르게 저장할 수 있다.
- `user`와 `model` 역할을 번갈아 유지할 수 있다.
- 전체 응답 JSON이 아니라 실제 답변 Text를 저장해야 함을 이해한다.
- 빈 질문과 중복 요청을 방지할 수 있다.
- 생성형 AI 결과를 `textContent`로 안전하게 출력할 수 있다.
- API Key를 Client에 노출하면 안 되는 이유를 설명할 수 있다.
- Backend Proxy 기반 실무 구조를 이해한다.

---

# 1. 원본 HTML 구조

```html
<textarea id="prompt"></textarea>

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

<div id="ask-result"></div>
```

---

# 2. 내 코드의 Button Type 오류

내 원본:

```html
<button type="buttn">
```

`buttn`은 유효한 Button Type이 아니다.

개선:

```html
<button type="button">
```

---

# 3. 문서 기본 정보 개선

원본:

```html
<html lang="en">
<title>Document</title>
```

개선:

```html
<html lang="ko">
<title>Gemini API와 멀티턴 대화</title>
```

---

# 4. 원본 초기화

```javascript
window.onload = function () {
    gemini()
}
```

`gemini()`는 API를 즉시 호출하는 함수가 아니라 Event Listener를 등록하는 초기화 함수다.

---

# 5. 함수 이름 개선

기존:

```javascript
function gemini() {
    // Event 등록
}
```

개선:

```javascript
function initGeminiChat() {
    // Event 등록
}
```

역할이 드러나는 이름을 사용한다.

---

# 6. `defer` 초기화

```html
<script
    src="./js/21_gemini.js"
    defer
></script>
```

```javascript
initGeminiChat()
```

Inline Script보다 HTML과 JavaScript를 분리하기 쉽다.

---

# 7. 전역 History

원본:

```javascript
const list = {
    contents: [],
}
```

`contents` 배열에 대화 Turn을 저장하려는 구조다.

---

# 8. 변수 이름 개선

```javascript
const conversation = {
    contents: [],
}
```

`list`보다 저장 목적이 명확하다.

---

# 9. 단일 질문 입력

```javascript
const promptInput = (
    document.querySelector(
        "#prompt",
    )
)

const prompt = (
    promptInput.value
)
```

Textarea의 현재 입력값을 문자열로 읽는다.

---

# 10. 빈 질문 검증

```javascript
const prompt = (
    promptInput.value.trim()
)

if (prompt === "") {
    message.textContent = (
        "질문을 입력해주세요."
    )

    promptInput.focus()
    return
}
```

공백만 입력한 경우도 차단한다.

---

# 11. API Key

원본:

```javascript
const key = ""
```

빈 문자열이므로 인증 요청이 실패할 수 있다.

---

# 12. API Key를 Client에 넣으면 안 되는 이유

Browser JavaScript에 Key를 넣으면 다음 위치에서 확인할 수 있다.

- Page Source
- DevTools Sources
- Network Request Header
- Build File
- Git Repository
- Browser Extension

---

# 13. 안전한 Key 관리

```text
Frontend
→ 자신의 Backend 호출

Backend
→ Environment Variable에서 Key 읽기
→ Gemini API 호출

Frontend
← 필요한 응답만 전달
```

---

# 14. API Endpoint

원본:

```javascript
const url = (
    "https://generativelanguage.googleapis.com/"
    + "v1beta/models/"
    + "gemini-3.6-flash:"
    + "generateContent"
)
```

Model 이름과 Endpoint 지원 여부는 API 업데이트에 따라 달라질 수 있으므로 공식 문서를 기준으로 관리한다.

---

# 15. Endpoint 분리

```javascript
const model = "gemini-3.6-flash"

const url = (
    "https://generativelanguage.googleapis.com/"
    + `v1beta/models/${model}:generateContent`
)
```

---

# 16. Single-turn 요청 객체

```javascript
const requestData = {
    contents: [
        {
            role: "user",

            parts: [
                {
                    text: prompt,
                },
            ],
        },
    ],
}
```

---

# 17. `contents`

```text
contents
→ 대화 Turn 배열
```

단일 질문도 Turn 하나를 가진 배열로 표현한다.

---

# 18. `role`

```text
user
→ 사용자가 보낸 Turn

model
→ Model이 생성한 Turn
```

멀티턴에서는 일반적으로 두 역할이 번갈아 배치된다.

---

# 19. `parts`

```javascript
parts: [
    {
        text: prompt,
    },
]
```

한 Turn 안에 Text 또는 다른 입력 Part를 담는다.

---

# 20. Body 직렬화

```javascript
body: JSON.stringify(
    requestData,
)
```

`fetch()`의 Body에 JavaScript 객체를 직접 넣는 것이 아니라 JSON 문자열로 변환한다.

---

# 21. 원본 주석 수정

원본 취지:

```text
JSON으로 날아가면 안 되기 때문에
문자열로 변경
```

더 정확한 설명:

```text
HTTP Body에 JSON Text 형식으로 전송하기 위해
JavaScript 객체를 JSON 문자열로 직렬화
```

---

# 22. Request Header

```text
headers: {
    "x-goog-api-key": apiKey,
    "Content-Type": "application/json"
}
```

---

# 23. `Content-Type`

```text
application/json
→ Request Body가 JSON Text임을 서버에 전달
```

---

# 24. 단일 요청

```javascript
async function requestContent() {
    return fetch(
        url,
        {
            method: "POST",

            headers: {
                "x-goog-api-key":
                    apiKey,

                "Content-Type":
                    "application/json",
            },

            body: JSON.stringify(
                requestData,
            ),
        },
    )
}
```

---

# 25. HTTP 상태 검사

원본은 바로 `response.json()`을 호출한다.

개선:

```javascript
if (!response.ok) {
    throw new Error(
        `HTTP ${response.status}`,
    )
}
```

---

# 26. Error Response Body

API는 실패 시에도 JSON Error Body를 반환할 수 있다.

```javascript
async function readErrorMessage(
    response,
) {
    try {
        const errorData = (
            await response.json()
        )

        return (
            errorData.error?.message
            ?? `HTTP ${response.status}`
        )
    } catch {
        return (
            `HTTP ${response.status}`
        )
    }
}
```

---

# 27. 응답 JSON 변환

```javascript
async function parseResponse(
    response,
) {
    return response.json()
}
```

`response.json()`도 비동기 작업이다.

---

# 28. 원본 응답 접근

```javascript
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
```

배열 Index에 문자열 `"0"`을 사용할 수 있지만 일반적으로 숫자 Index를 사용한다.

---

# 29. Dot·Index 접근

```javascript
const text = (
    result
        .candidates[0]
        .content
        .parts[0]
        .text
)
```

---

# 30. 안전한 응답 Text 추출

```javascript
function getResponseText(
    result,
) {
    const parts = (
        result
            ?.candidates
            ?.[0]
            ?.content
            ?.parts
    )

    if (!Array.isArray(parts)) {
        return null
    }

    const text = parts
        .map(
            part => (
                typeof part.text
                    === "string"
                    ? part.text
                    : ""
            ),
        )
        .join("")

    return (
        text.trim() === ""
            ? null
            : text
    )
}
```

---

# 31. Candidate가 없을 수 있는 경우

다음 상황에서는 예상한 Text가 없을 수 있다.

- 안전 정책에 의한 차단
- 빈 Candidate
- API 오류 응답
- 응답 형식 변경
- Tool Call·다른 Part 유형
- Model 출력 중단

중첩 Property가 항상 존재한다고 가정하지 않는다.

---

# 32. Finish Reason 확인

```javascript
const finishReason = (
    result
        ?.candidates
        ?.[0]
        ?.finishReason
    ?? "UNKNOWN"
)
```

Text가 없을 때 종료 이유를 확인할 수 있다.

---

# 33. 원본 단일 응답 화면 출력

내 코드:

```javascript
const divAdd = (
    document.createElement(
        "div",
    )
)

askResult.append(divAdd)

askResult.innerText = text
```

---

# 34. 생성한 Div가 사라지는 이유

```text
빈 Div Append
    ↓
부모의 innerText 전체 재할당
    ↓
기존 자식 Node 제거
    ↓
Text Node로 교체
```

생성한 `divAdd`는 실제로 활용되지 않는다.

---

# 35. 단일 결과 교체

최신 답변 하나만 표시할 경우:

```javascript
askResult.textContent = text
```

---

# 36. 대화 Message 추가

대화를 누적할 경우:

```javascript
function appendMessage(
    container,
    role,
    text,
) {
    const message = (
        document.createElement(
            "article",
        )
    )

    message.classList.add(
        "chat-message",
        `chat-message--${role}`,
    )

    const label = (
        document.createElement(
            "strong",
        )
    )

    label.textContent = (
        role === "user"
            ? "사용자"
            : "Gemini"
    )

    const body = (
        document.createElement(
            "p",
        )
    )

    body.textContent = text

    message.append(
        label,
        body,
    )

    container.append(message)
}
```

---

# 37. `textContent` 사용

AI 응답도 외부 데이터다.

```javascript
body.textContent = text
```

응답을 `innerHTML`에 직접 넣지 않는다.

---

# 38. Markdown 응답

Model 답변에 Markdown 문법이 포함될 수 있다.

```text
**강조**
- 목록
인라인 코드 또는 코드 블록
```

그대로 `textContent`로 표시하면 안전하지만 Markdown 스타일은 적용되지 않는다.

Markdown Renderer를 사용할 경우 Sanitizing이 필요하다.

---

# 39. 멀티턴 User Turn 추가

```javascript
conversation.contents.push({
    role: "user",

    parts: [
        {
            text: prompt,
        },
    ],
})
```

---

# 40. History 전체 전송

```javascript
body: JSON.stringify(
    conversation,
)
```

이전 Turn과 현재 질문을 모두 Context로 전달한다.

---

# 41. 원본 Model Turn 저장

원본:

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

---

# 42. 원본 History 저장 오류

Model의 실제 답변 Text가 아니라 전체 API Response JSON 문자열을 저장한다.

문제:

- 불필요한 Metadata 포함
- 다음 Prompt 크기 증가
- Model이 자신의 답변 대신 JSON 구조를 Context로 받음
- Token 사용량 증가
- 대화 품질 저하
- 응답 크기 급증

---

# 43. 올바른 Model Turn 저장

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

---

# 44. Role 순서

정상적인 History 예:

```javascript
[
    {
        role: "user",
        parts: [
            {
                text: "내 이름은 근욱이야.",
            },
        ],
    },
    {
        role: "model",
        parts: [
            {
                text: "반가워요, 근욱님.",
            },
        ],
    },
    {
        role: "user",
        parts: [
            {
                text: "내 이름이 뭐야?",
            },
        ],
    },
]
```

---

# 45. 실패한 User Turn 처리

User Turn을 먼저 History에 추가한 뒤 요청이 실패하면 실패한 질문이 History에 남는다.

정책을 정해야 한다.

```text
1. 실패해도 질문 유지
2. 실패 시 마지막 User Turn 제거
3. Retry용 상태로 보관
```

---

# 46. 실패 시 Rollback

```javascript
conversation.contents.push(
    userTurn,
)

try {
    // Request
} catch (
    error
) {
    conversation.contents.pop()
    throw error
}
```

---

# 47. 중복 클릭 문제

요청 중 Button을 다시 클릭하면 여러 요청이 동시에 실행될 수 있다.

- 답변 순서 역전
- History 순서 오류
- 요청 비용 증가
- 중복 화면 출력

---

# 48. Loading 상태

```javascript
askButton.disabled = true

statusView.textContent = (
    "답변을 생성하는 중입니다."
)
```

---

# 49. 상태 복구

```javascript
try {
    // Request
} finally {
    askButton.disabled = false
}
```

---

# 50. 입력 초기화

성공 후:

```javascript
promptInput.value = ""
promptInput.focus()
```

실패한 경우 질문을 유지하면 사용자가 수정·재시도하기 쉽다.

---

# 51. Enter 전송

```javascript
promptInput.addEventListener(
    "keydown",
    event => {
        if (
            event.key === "Enter"
            && !event.shiftKey
        ) {
            event.preventDefault()
            askButton.click()
        }
    },
)
```

`Shift + Enter`는 줄바꿈으로 유지할 수 있다.

---

# 52. 요청 함수 분리

```javascript
async function generateContent({
    endpoint,
    apiKey,
    contents,
}) {
    const response = await fetch(
        endpoint,
        {
            method: "POST",

            headers: {
                "x-goog-api-key":
                    apiKey,

                "Content-Type":
                    "application/json",
            },

            body: JSON.stringify({
                contents,
            }),
        },
    )

    if (!response.ok) {
        const message = (
            await readErrorMessage(
                response,
            )
        )

        throw new Error(message)
    }

    return response.json()
}
```

---

# 53. 단일 질문 함수

```javascript
async function askOnce(
    prompt,
) {
    const result = await generateContent({
        endpoint,
        apiKey,

        contents: [
            {
                role: "user",

                parts: [
                    {
                        text: prompt,
                    },
                ],
            },
        ],
    })

    const text = getResponseText(
        result,
    )

    if (text === null) {
        throw new Error(
            "답변 Text가 없습니다.",
        )
    }

    return text
}
```

---

# 54. 멀티턴 질문 함수

```javascript
async function askWithHistory(
    prompt,
) {
    const userTurn = {
        role: "user",

        parts: [
            {
                text: prompt,
            },
        ],
    }

    conversation.contents.push(
        userTurn,
    )

    try {
        const result = (
            await generateContent({
                endpoint,
                apiKey,

                contents: (
                    conversation.contents
                ),
            })
        )

        const text = getResponseText(
            result,
        )

        if (text === null) {
            throw new Error(
                "답변 Text가 없습니다.",
            )
        }

        conversation.contents.push({
            role: "model",

            parts: [
                {
                    text,
                },
            ],
        })

        return text
    } catch (
        error
    ) {
        conversation.contents.pop()
        throw error
    }
}
```

---

# 55. `contents` 복사

Request 중 원본 배열이 변경될 가능성을 줄이려면 Snapshot을 전달할 수 있다.

```javascript
contents: (
    structuredClone(
        conversation.contents,
    )
)
```

---

# 56. History 초기화

```javascript
function resetConversation() {
    conversation.contents.length = 0
    chatView.replaceChildren()
}
```

---

# 57. 대화가 계속 길어지는 문제

History를 무제한 누적하면:

- Request Body 증가
- Token 사용량 증가
- 응답 지연
- 비용 증가
- Context 한도 초과 가능
- 오래된 정보의 영향 증가

---

# 58. 최근 Turn만 유지

```javascript
const MAX_TURNS = 10

function trimConversation() {
    const maxContents = (
        MAX_TURNS * 2
    )

    if (
        conversation.contents.length
        > maxContents
    ) {
        conversation.contents.splice(
            0,
            conversation.contents.length
                - maxContents,
        )
    }
}
```

---

# 59. 대화 요약 방식

오래된 대화를 단순 삭제하는 대신 요약 Turn으로 압축할 수 있다.

```text
오래된 대화
→ 핵심 정보 요약
→ System Instruction 또는 Context에 저장
→ 최근 실제 Turn 유지
```

요약 과정에서도 정보 손실 가능성을 고려한다.

---

# 60. AbortController

```javascript
const controller = (
    new AbortController()
)

fetch(
    endpoint,
    {
        signal: controller.signal,
    },
)

controller.abort()
```

사용자가 요청을 취소하거나 새 요청을 시작할 때 활용할 수 있다.

---

# 61. Timeout 구현

```javascript
const controller = (
    new AbortController()
)

const timeoutId = setTimeout(
    () => {
        controller.abort()
    },
    30000,
)

try {
    const response = await fetch(
        endpoint,
        {
            signal: controller.signal,
        },
    )
} finally {
    clearTimeout(timeoutId)
}
```

---

# 62. Retry 주의

일시적인 서버 오류에는 Retry가 도움이 될 수 있다.

하지만 다음 요청을 무조건 반복하면 안 된다.

- 인증 오류
- 잘못된 Request
- 안전 정책 차단
- 사용량 한도 초과
- 사용자 취소

---

# 63. 재시도 대상 예

```text
일시적 Network 오류
HTTP 429
HTTP 500
HTTP 502
HTTP 503
HTTP 504
```

지수 Backoff와 최대 횟수를 둔다.

---

# 64. 응답 순서 보호

동시에 요청할 수 있는 UI라면 요청 ID를 사용할 수 있다.

```javascript
let latestRequestId = 0

async function askLatest(
    prompt,
) {
    const requestId = (
        ++latestRequestId
    )

    const text = await askOnce(
        prompt,
    )

    if (
        requestId
        !== latestRequestId
    ) {
        return null
    }

    return text
}
```

---

# 65. UI 상태 구분

```text
Idle
→ 질문 입력 가능

Loading
→ 답변 생성 중

Success
→ 답변 표시

Empty
→ 답변 Text 없음

Error
→ 요청 실패

Blocked
→ 안전 정책 등으로 결과 없음
```

---

# 66. 접근성 상태

```html
<div
    id="chat-status"
    role="status"
    aria-live="polite"
></div>
```

답변 생성 상태를 보조기기에 전달한다.

---

# 67. 민감정보 전송 주의

사용자 Prompt에 다음 정보가 포함되지 않도록 안내할 수 있다.

- 비밀번호
- 주민등록번호
- 카드번호
- API Key
- 회사 기밀
- 비공개 Source Code
- 의료·법률 민감정보

---

# 68. Prompt Injection 기초

Model 출력이나 외부 문서의 지시를 무조건 신뢰하지 않는다.

특히 AI가 다음 작업을 직접 수행하게 할 경우 별도 검증이 필요하다.

- 파일 삭제
- 결제
- Email 전송
- Database 변경
- 관리자 기능
- 외부 URL 실행

---

# 69. Model 출력 검증

생성된 Text를 화면에 표시하는 것과 실행 가능한 코드·명령으로 사용하는 것은 다르다.

```text
표시
→ textContent

HTML 렌더링
→ Sanitizing 필요

Command 실행
→ Allowlist와 사용자 확인 필요
```

---

# 70. Backend Proxy 요청

Frontend:

```javascript
const response = await fetch(
    "/api/chat",
    {
        method: "POST",

        headers: {
            "Content-Type":
                "application/json",
        },

        body: JSON.stringify({
            contents:
                conversation.contents,
        }),
    },
)
```

Frontend에는 Gemini API Key가 없다.

---

# 71. Backend 역할

```text
입력 검증
API Key 보관
사용자 인증
Rate Limit
Gemini API 요청
오류 형식 통일
응답 필터링
사용량 기록
```

---

# 72. 원본 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| Single-turn Console | 생성 Text 직접 출력 | 전체 Result 출력 |
| Single-turn 화면 출력 | 구현 | 없음 |
| Multiturn 주석 | 상세 | 간결 |
| Model History | 전체 Result JSON 문자열 | 전체 Result JSON 문자열 |
| 결과 Container | `#askResult` 존재 | 없음 |
| Button Type | `buttn` 오타 | `button` |
| 빈 Prompt 검사 | 없음 | 없음 |
| HTTP Status 검사 | 없음 | 없음 |
| API Key | 빈 문자열 | 빈 문자열 |

## 72-1. 내 코드의 장점

- 단일 응답 Text를 직접 찾아 출력했다.
- 화면 출력 Container를 추가했다.
- History 누적의 목적을 주석으로 설명했다.
- Single-turn과 Multiturn Button을 분리했다.

## 72-2. 내 코드의 개선점

- Button Type 오타가 있다.
- 빈 Prompt를 전송한다.
- HTTP Status를 확인하지 않는다.
- 응답 구조를 항상 존재한다고 가정한다.
- 빈 Div를 Append한 뒤 부모 `innerText`로 제거한다.
- Model History에 전체 Result JSON을 저장한다.
- 요청 중 Button 상태를 관리하지 않는다.
- API Key를 Client Header에 넣는 구조다.

## 72-3. 강사님 코드의 장점

- Request Header·Body·Fetch 흐름이 간결하다.
- Single-turn과 Multiturn 구조를 비교할 수 있다.
- `user`와 `model` Turn을 배열에 누적하는 기본 형태를 보여 준다.

## 72-4. 강사님 코드의 보충점

- 응답을 화면에 출력하지 않는다.
- 실제 Model Text 대신 전체 Response JSON을 History에 저장한다.
- 오류 Body와 HTTP Status를 처리하지 않는다.
- 빈 Prompt·중복 요청·History 크기를 관리하지 않는다.
- API Key 보안 설명이 필요하다.

---

# 73. 기존 코드에서 개선한 이유

## 73-1. Button Type

기존:

```html
type="buttn"
```

개선:

```html
type="button"
```

## 73-2. 응답 출력

기존:

```javascript
container.append(
    document.createElement(
        "div",
    ),
)

container.innerText = text
```

개선:

```javascript
appendMessage(
    container,
    "model",
    text,
)
```

## 73-3. Model History

기존:

```javascript
text: JSON.stringify(result)
```

개선:

```javascript
text: responseText
```

## 73-4. API Key

기존:

```text
Browser
→ Gemini API 직접 호출
→ Key 노출
```

개선:

```text
Browser
→ Backend Proxy
→ Gemini API
```

---

# 74. 실무형 예제: 안전한 Chat UI

```javascript
function createChatApp({
    form,
    input,
    chatView,
    statusView,
}) {
    const conversation = {
        contents: [],
    }

    let isLoading = false

    async function submitPrompt(
        prompt,
    ) {
        if (isLoading) {
            return
        }

        isLoading = true

        statusView.textContent = (
            "답변을 생성하는 중입니다."
        )

        appendMessage(
            chatView,
            "user",
            prompt,
        )

        const userTurn = {
            role: "user",

            parts: [
                {
                    text: prompt,
                },
            ],
        }

        conversation.contents.push(
            userTurn,
        )

        try {
            const response = await fetch(
                "/api/chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json",
                    },

                    body: JSON.stringify({
                        contents:
                            conversation
                                .contents,
                    }),
                },
            )

            if (!response.ok) {
                throw new Error(
                    `HTTP ${response.status}`,
                )
            }

            const data = (
                await response.json()
            )

            if (
                typeof data.text
                !== "string"
                || data.text.trim()
                    === ""
            ) {
                throw new Error(
                    "답변 Text가 없습니다.",
                )
            }

            conversation.contents.push({
                role: "model",

                parts: [
                    {
                        text: data.text,
                    },
                ],
            })

            appendMessage(
                chatView,
                "model",
                data.text,
            )

            statusView.textContent = ""
        } catch (
            error
        ) {
            conversation.contents.pop()

            statusView.textContent = (
                "답변을 불러오지 "
                + "못했습니다."
            )

            console.error(error)
        } finally {
            isLoading = false
            input.focus()
        }
    }

    form.addEventListener(
        "submit",
        event => {
            event.preventDefault()

            const prompt = (
                input.value.trim()
            )

            if (prompt === "") {
                statusView.textContent = (
                    "질문을 입력해주세요."
                )

                input.focus()
                return
            }

            input.value = ""

            submitPrompt(prompt)
        },
    )
}
```

## 74-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| Backend Endpoint | Client API Key 노출 방지 |
| Form Submit | Button·Enter 전송 통합 |
| `trim()` | 빈 질문 차단 |
| Loading Flag | 중복 요청 방지 |
| User Turn 선출력 | 즉각적인 UI 반응 |
| 실패 시 `pop()` | History Rollback |
| 응답 자료형 검사 | 예상 구조 누락 처리 |
| `textContent` | 외부 Text 안전 출력 |
| Status View | Loading·Error 안내 |
| `finally` | UI 상태 복구 |

---

# 75. 대표 오류로 이해하기

## 75-1. HTTP 400·401 후 응답 접근

Error JSON에는 `candidates`가 없어 `TypeError`가 발생할 수 있다.

## 75-2. API Key가 빈 문자열

인증 오류가 발생한다.

## 75-3. Model 응답 전체를 History Text로 저장

다음 요청 Context가 불필요한 JSON Metadata로 오염된다.

## 75-4. Append 후 `innerText` 재할당

생성한 자식 Node가 모두 제거된다.

## 75-5. 중복 요청

응답 순서와 History 순서가 엉킬 수 있다.

## 75-6. Client에 Key 하드코딩

사용자가 Key를 확인하고 악용할 수 있다.

---

# 76. 자주 하는 실수

## 76-1. Model이 Browser 상태를 자동 기억한다고 생각

Client가 History를 다시 전송해야 한다.

## 76-2. 객체가 자동으로 JSON 전송된다고 생각

`JSON.stringify()`가 필요하다.

## 76-3. `response.json()`이 동기 함수라고 생각

Promise를 반환한다.

## 76-4. HTTP 오류도 Catch가 자동 처리한다고 생각

`response.ok`를 확인한다.

## 76-5. Candidate Text가 항상 존재한다고 생각

안전 차단·빈 응답·형식 변경을 처리한다.

## 76-6. 전체 Result를 Model 답변으로 저장

실제 생성 Text만 History에 넣는다.

## 76-7. History를 무제한 저장

Token·비용·지연·Context 한도를 관리한다.

## 76-8. AI 응답을 `innerHTML`에 직접 삽입

`textContent` 또는 Sanitizer를 사용한다.

## 76-9. API Key를 `.gitignore`만으로 보호 가능하다고 생각

Browser Bundle에 들어가면 사용자에게 노출된다.

## 76-10. Model 이름을 영구적인 값으로 생각

설정값으로 분리하고 공식 문서를 확인한다.

---

# 77. 핵심 요약

```text
Prompt
→ contents
→ JSON.stringify()
→ Fetch POST
→ Response JSON
→ Candidate Text
```

```text
Single-turn
→ 현재 질문만 전송

Multiturn
→ 이전 User·Model Turn
→ 현재 User Turn
→ 전체 History 전송
```

```text
User Turn
→ role: "user"

Model Turn
→ role: "model"
```

```text
Client API Key
→ 노출 위험

Backend Proxy
→ Key와 정책 관리
```

---

# 78. 최종 체크리스트

- [ ] Button Type을 올바르게 작성했는가?
- [ ] HTML `lang`과 `title`이 문서 내용에 맞는가?
- [ ] 빈 Prompt를 `trim()`으로 검사하는가?
- [ ] Endpoint와 Model 이름을 설정값으로 분리했는가?
- [ ] Request Body를 `JSON.stringify()` 하는가?
- [ ] `Content-Type`을 설정하는가?
- [ ] HTTP Status를 검사하는가?
- [ ] Error Response Body를 안전하게 읽는가?
- [ ] Candidate와 Parts 존재 여부를 검사하는가?
- [ ] 여러 Text Part를 합칠 수 있는가?
- [ ] Finish Reason을 확인할 수 있는가?
- [ ] 응답을 `textContent`로 출력하는가?
- [ ] 생성한 Message Node를 실제로 사용하는가?
- [ ] User와 Model Turn을 교대로 저장하는가?
- [ ] Model Turn에는 실제 답변 Text를 저장하는가?
- [ ] 실패 시 History Rollback 정책이 있는가?
- [ ] 요청 중 Button·Loading 상태를 관리하는가?
- [ ] 중복 요청과 응답 순서 역전을 방지하는가?
- [ ] Enter와 Shift+Enter를 구분할 수 있는가?
- [ ] History 길이와 Token 사용량을 관리하는가?
- [ ] 요청 취소와 Timeout을 처리할 수 있는가?
- [ ] AI 응답을 실행 가능한 HTML·명령으로 바로 사용하지 않는가?
- [ ] Client JavaScript에 API Key를 넣지 않는가?
- [ ] Backend에서 인증·Rate Limit·오류 처리를 수행하는가?
- [ ] 민감정보가 Prompt에 포함되지 않도록 안내하는가?

---

# 마무리

생성형 AI API 연동의 핵심은 질문을 보내고 답변을 출력하는 것에서 끝나지 않는다.

```text
요청과 응답 구조를 정확히 이해하고
    ↓
User·Model History를 올바르게 관리하고
    ↓
빈 응답·차단·HTTP 오류를 안전하게 처리하고
    ↓
Loading·취소·중복 요청 상태를 제어하고
    ↓
API Key와 사용자 데이터를 Backend에서 보호하는 것
```

이 흐름을 이해하면 단순한 API 실습을 넘어 실제 AI Chat UI와 서비스 구조로 확장할 수 있다.
# V3 실행 추적 카드 — 사용자 메시지 → 요청 본문 → API 응답 → 대화 상태·화면

멀티턴은 이전 user/model 메시지를 배열 상태에 누적해 다음 요청에 포함한다. 전송 전 UI 상태, 요청 중 로딩, 성공·실패 후 복구를 구분한다.

API 키를 프런트 코드에 두면 사용자에게 노출된다. Network에서 요청·응답을 확인하되 키와 개인정보를 기록하거나 Wiki에 넣지 않는다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/21_gemini.html`에서 실제 사용 위치와 차이를 확인한다.
