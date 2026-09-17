---
title: JavaScript Discord Webhook과 XMLHttpRequest
version: v4.0-detailed-source
last_updated: 2026-09-17
status: Completed
---

# JavaScript Discord Webhook과 XMLHttpRequest

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `22_JavaScript_Discord_Webhook과_XMLHttpRequest.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/22_discord.html`, `workspace_teacher/workspace_html/javascript/22_discord.html` |
| 핵심 범위 | Discord Webhook, `XMLHttpRequest`, POST 요청, JSON Header, Payload, 상태 코드, Network Error, Credential 보안 |
| 실습 범위 | Textarea 메시지 전송, 입력 검증, 중복 요청 방지, 상태 표시, Backend Proxy, Fetch 전환 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 22번은 Textarea에 입력한 메시지를 Discord Webhook으로 전송하는 과정을 다룬다.  
> 강사님 원본에는 실제 Webhook URL이 포함되어 있었지만, Webhook URL은 메시지 전송 권한을 가진 Credential이므로 이 문서에는 원문을 재노출하지 않는다.

---

## 이 문서에서 바로 찾기

- [개념에서 실제 실행까지: Webhook URL은 메시지 전송 권한을 가진 비밀 주소일 수 있다](#js-22-section-4)
- [57. 원본 코드와 강사님 코드 비교](#js-22-section-61)
- [63. 실무형 예제: 안전한 Discord 알림 Form](#js-22-section-67)
- [64. 대표 오류로 이해하기](#js-22-section-68)
- [65. 자주 하는 실수](#js-22-section-69)
- [66. 핵심 요약](#js-22-section-70)
- [67. 최종 체크리스트](#js-22-section-71)

<details>
<summary>세부 목차 펼치기 — 번호형 본문 전체</summary>

- [개요](#js-22-section-1)
- [핵심 개념](#js-22-section-2)
- [학습 목표](#js-22-section-3)
- [개념에서 실제 실행까지: Webhook URL은 메시지 전송 권한을 가진 비밀 주소일 수 있다](#js-22-section-4)
- [1. 원본 HTML 구조](#js-22-section-5)
- [2. 내 코드의 Button Type 오류](#js-22-section-6)
- [3. 임시 Text 제거](#js-22-section-7)
- [4. 문서 언어와 제목](#js-22-section-8)
- [5. 접근 가능한 Label](#js-22-section-9)
- [6. 상태 표시 영역](#js-22-section-10)
- [7. 원본 초기화](#js-22-section-11)
- [8. 함수 이름 개선](#js-22-section-12)
- [9. `defer` 사용](#js-22-section-13)
- [10. 요소 선택](#js-22-section-14)
- [11. 필수 요소 검사](#js-22-section-15)
- [12. Textarea 값 읽기](#js-22-section-16)
- [13. 반복 선택 제거](#js-22-section-17)
- [14. 공백 제거](#js-22-section-18)
- [15. 빈 메시지 검증](#js-22-section-19)
- [16. 길이 검증](#js-22-section-20)
- [17. Webhook URL](#js-22-section-21)
- [18. 빈 URL의 동작](#js-22-section-22)
- [19. 강사님 원본의 URL](#js-22-section-23)
- [20. 노출된 Webhook 대응](#js-22-section-24)
- [21. `XMLHttpRequest` 생성](#js-22-section-25)
- [22. `open()`](#js-22-section-26)
- [23. `open()`은 전송이 아님](#js-22-section-27)
- [24. Request Header](#js-22-section-28)
- [25. Payload 객체](#js-22-section-29)
- [26. `username`](#js-22-section-30)
- [27. `content`](#js-22-section-31)
- [28. JSON 직렬화](#js-22-section-32)
- [29. `send()`](#js-22-section-33)
- [30. 전체 원본 흐름](#js-22-section-34)
- [31. 원본 `onload`](#js-22-section-35)
- [32. `onload`와 성공 구분](#js-22-section-36)
- [33. HTTP Status 검사](#js-22-section-37)
- [34. 빈 Response Body](#js-22-section-38)
- [35. Response Body보다 Status](#js-22-section-39)
- [36. 오류 Status 분기](#js-22-section-40)
- [37. Network Error](#js-22-section-41)
- [38. Timeout](#js-22-section-42)
- [39. 요청 종료](#js-22-section-43)
- [40. 중복 요청 방지](#js-22-section-44)
- [41. Loading 상태](#js-22-section-45)
- [42. 성공 후 초기화](#js-22-section-46)
- [43. 실패 시 입력 유지](#js-22-section-47)
- [44. 안전한 XHR 완성본](#js-22-section-48)
- [45. Frontend 직접 호출의 문제](#js-22-section-49)
- [46. Backend Proxy 구조](#js-22-section-50)
- [47. Frontend 요청 데이터 최소화](#js-22-section-51)
- [48. Backend 환경 변수](#js-22-section-52)
- [49. Backend 검증 항목](#js-22-section-53)
- [50. Public Endpoint 위험](#js-22-section-54)
- [51. Fetch로 전환](#js-22-section-55)
- [52. Fetch HTTP 오류](#js-22-section-56)
- [53. 429 별도 처리](#js-22-section-57)
- [54. Fetch Network Error](#js-22-section-58)
- [55. AbortController](#js-22-section-59)
- [56. Fetch Timeout](#js-22-section-60)
- [57. 원본 코드와 강사님 코드 비교](#js-22-section-61)
- [58. 내 코드의 장점](#js-22-section-62)
- [59. 내 코드의 개선점](#js-22-section-63)
- [60. 강사님 코드의 장점](#js-22-section-64)
- [61. 강사님 코드의 개선점](#js-22-section-65)
- [62. 기존 코드에서 개선한 이유](#js-22-section-66)
- [63. 실무형 예제: 안전한 Discord 알림 Form](#js-22-section-67)
- [64. 대표 오류로 이해하기](#js-22-section-68)
- [65. 자주 하는 실수](#js-22-section-69)
- [66. 핵심 요약](#js-22-section-70)
- [67. 최종 체크리스트](#js-22-section-71)
- [마무리](#js-22-section-72)
- [V3 실행 추적 카드 — 폼/데이터 → HTTP 요청 → 상태 변화 → 성공·실패 처리](#js-22-section-73)

</details>

---

<a id="js-22-section-1"></a>

## 개요

Webhook은 외부 서비스가 제공하는 URL로 HTTP 요청을 보내 특정 동작을 실행하는 방식이다.

Discord Webhook을 사용하면 JSON 형식의 메시지를 특정 Channel로 전송할 수 있다.

```text
사용자 메시지 입력
    ↓
Button Click
    ↓
Payload 객체 생성
    ↓
JSON 문자열 직렬화
    ↓
Webhook URL로 POST
    ↓
Discord Channel에 메시지 표시
```

원본의 핵심 코드:

```javascript
const xhr = new XMLHttpRequest()

xhr.open(
    "POST",
    url,
)

xhr.setRequestHeader(
    "Content-Type",
    "application/json",
)

xhr.send(
    JSON.stringify(
        payload,
    ),
)
```

> [!IMPORTANT]
> Webhook URL은 일반 URL처럼 보여도 메시지 전송 권한을 포함할 수 있다.  
> Public Repository와 Browser JavaScript에 직접 넣지 않는다.

---

<a id="js-22-section-2"></a>

## 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| Webhook | 지정된 URL로 요청을 보내 외부 서비스 기능 실행 |
| Webhook URL | 메시지 전송 권한을 포함할 수 있는 Endpoint |
| `XMLHttpRequest` | HTTP 요청과 응답을 관리하는 객체 |
| POST | 요청 Body에 데이터를 담아 전송하는 Method |
| Request Header | Body 형식과 인증 관련 정보 전달 |
| JSON Payload | 서버가 요구하는 구조에 맞춘 메시지 데이터 |
| `JSON.stringify()` | JavaScript 객체를 JSON 문자열로 변환 |
| HTTP Status | 요청 처리 결과 코드 |
| Network Error | DNS·연결·CORS 등 응답 이전 단계 오류 |
| Rate Limit | 짧은 시간에 과도한 요청을 제한하는 정책 |
| Backend Proxy | Frontend 대신 외부 Webhook을 호출하는 서버 |

---

<a id="js-22-section-3"></a>

## 학습 목표

- JSON POST와 본문 없는 응답을 구분한다.
- 원본의 해당 부분을 찾아 실행 순서와 결과를 다시 확인한다.

---

<a id="js-22-section-4"></a>

## 개념에서 실제 실행까지: Webhook URL은 메시지 전송 권한을 가진 비밀 주소일 수 있다

사용자가 textarea에 입력한 문자열을 click 콜백에서 읽고, username/content 객체로 구성해 JSON.stringify한 다음 POST Body로 보낸다. Content-Type 헤더는 서버에 이 본문을 JSON으로 해석해 달라는 형식 정보다.

내 원본 url은 빈 문자열이며 강사님 원본에는 실제 Webhook 주소가 있었다. 빈 문자열 URL은 구성 오류일 뿐 아니라 현재 문서 주소로 해석될 수 있어 '아무 요청도 안 함'으로 생각하면 안 된다. 사용자명만 다른 완전 동일 코드라고 요약하면 주소와 button type 오타 차이를 놓친다.

Discord 성공 응답은 wait 설정에 따라 메시지 JSON 또는204가 될 수 있다. 204는 빈 본문이라 console.log(responseText)가 아무 내용 없는 로그처럼 보일 수 있고 JSON.parse("")는 실패한다. 실패·제한 응답을 무조건 재전송하면 메시지가 중복될 수 있다. 💡 서버 프록시, 인증·권한·입력 제한·allowed_mentions 설정을 더해 악용과 원치 않는 멘션을 줄인다.

### 수업 원본에서 사용한 부분

아래는 전체 실행 파일이 아니라 **개념에 대응하는 문맥 발췌**다. 나머지 HTML·선언·등록 코드는 원본과 기존 번호형 본문에서 이어 확인한다. 

내 코드: `workspace_html/javascript/22_discord.html`

```javascript
xhr.setRequestHeader('Content-Type','application/json')
                // discord에 보내기 위한 파라미터 양식
                const param = {
                    username: 'zl존법사v',
                    content: prompt
                }
```

강사님 코드: `workspace_teacher/workspace_html/javascript/22_discord.html`

```javascript
xhr.setRequestHeader('Content-Type', 'application/json')
                const param = {
                    username: '쵬니수', // 80자 제한
                    content: prompt
                }

                xhr.send( JSON.stringify(param) )
```

### 직접 재현하는 최소 예제와 결과

이 예제는 **이번 리팩토링의 설명용 재구성**이다. 원본 그대로의 발췌와 구별한다. 외부 통신 없이 Console에서 실행한다. 다른 예제의 변수와 섞이지 않게 새 실행 문맥에서 실행한다.

```javascript
const payload = {username:"학습용", content:"안녕하세요", allowed_mentions:{parse:[]}};
console.log(JSON.stringify(payload));
function readBody(status, body) {
  if (status === 204) return "본문 없음";
  return JSON.parse(body);
}
console.log(readBody(204, ""));
```

예상 출력:

```text
{"username":"학습용","content":"안녕하세요","allowed_mentions":{"parse":[]}}
본문 없음
```

### 결과를 역추적하는 방법

외부 메시지는 보내지 않은 mock이다. [Discord Execute Webhook 공식 문서](https://docs.discord.com/developers/resources/webhook#execute-webhook)를 기준으로204와 wait의 차이를 확인했다. ZIP에는 실제 인증 키나 메시지 전송용 Webhook을 넣지 않는다.

출력은 아래의 확인 경로로 추적한다. return 값은 호출자에게 전달되고 자동으로 화면에 표시되지 않는다. Console 로그, DOM 변경, 저장소 변경, 서버 응답은 별개 단계다.

| 확인할 단계 | 이 예제에서 볼 것 |
| --- | --- |
| 입력 | 리터럴·현재 폼 값·이벤트 인수·응답 중 출처를 위 설명과 대조 |
| 실행 | 각 줄 또는 콜백이 지금 실행되는지, 나중에 실행되는지 구분 |
| 결과 | 위 예상 출력과 현재 값·자료형을 함께 대조 |
| 오류 | 첫 오류 줄의 입력과 직전 상태를 확인하고 뒤 로그 누락 원인 추적 |

### 단계별 복습 실습과 정답

**기본 실습:** HTTP204와빈responseText를읽었을때화면상태와파싱을결정한다.

**응용·디버깅 실습:** 빈URL·Webhook노출·중복재시도중어느것이문제인지설명한다.

**통합 확인:** 위 최소 예제를 새 문맥에서 작성하고 정상값·빈 값·경계값으로 실행한다. 원본에서 대응하는 선언·호출·콜백을 찾아 위에 나타난 차이가 무엇을 바꾸는지 설명한다. 아래 정답은 먼저 예측한 뒤 펼친다. 이 실습은 💡 설명용 보강이며 원본에 모두 완성되어 있다는 뜻은 아니다.

<details>
<summary>정답과 처리 순서 해설</summary>

1. 본문없음으로처리한다. JSON.parse하지않는다. wait설정과정상상태조건은서버계약에맞춘다.
2. 모두문제다. URL검증후서버에서비밀주소관리,인증과rate limit적용,중복방지정책을둔다.
3. 최소 예제의 예상 출력과 한 줄씩 대조한다. 값이 다른 경우 입력 → 형 변환 → 분기/상태 변경 → 출력 순서로 첫 차이를 찾는다. DOM·API 예제는 Console 값만 아니라 화면·Elements·Network가 서로 같은 상태를 말하는지도 점검한다.

</details>

### 복습 질문과 해설

**질문:** Webhook URL을 .gitignore에 적으면 이미 commit된 키도 안전해질까?

**해설:** 아니다. 이미 공개된 권한은 재발급·폐기하고 기록 노출도 점검해야 한다. 브라우저 코드에 키를 전달하면 Network와 소스에서 볼 수 있다.

**한 번 더 확인:** 예제의 입력을 하나 바꾸고 결과를 먼저 예상한 뒤 실행한다. 정상 입력만 아니라 비어 있는 값, 경계값, 두 번 실행했을 때의 상태를 기존 실습·오류 절에서 반복 확인한다.

---

<a id="js-22-section-5"></a>

## 1. 원본 HTML 구조

```html
<textarea id="prompt"></textarea>

<br>

<button
    type="button"
    id="ask"
>
    디코에 말하기
</button>
```

Textarea에 메시지를 입력하고 Button을 눌러 요청한다.

---

<a id="js-22-section-6"></a>

## 2. 내 코드의 Button Type 오류

내 원본:

```html
<button type="buttn">
```

`buttn`은 올바른 Button Type이 아니다.

개선:

```html
<button type="button">
```

---

<a id="js-22-section-7"></a>

## 3. 임시 Text 제거

내 원본 Body에는 다음 문자열이 남아 있다.

```text
test
```

기능과 관련 없는 임시 문자열이므로 제거한다.

---

<a id="js-22-section-8"></a>

## 4. 문서 언어와 제목

원본:

```html
<html lang="en">
<title>Document</title>
```

개선:

```html
<html lang="ko">
<title>Discord Webhook 메시지 전송</title>
```

---

<a id="js-22-section-9"></a>

## 5. 접근 가능한 Label

```html
<label for="prompt">
    Discord 메시지
</label>

<textarea
    id="prompt"
    rows="6"
></textarea>
```

Label과 Textarea를 연결하면 클릭 범위와 접근성이 개선된다.

---

<a id="js-22-section-10"></a>

## 6. 상태 표시 영역

```html
<p
    id="status"
    role="status"
    aria-live="polite"
></p>
```

전송 중·성공·실패 상태를 사용자와 보조기기에 전달한다.

---

<a id="js-22-section-11"></a>

## 7. 원본 초기화

```javascript
window.onload = function () {
    discord()
}
```

`discord()`는 메시지를 바로 보내는 함수가 아니라 Click Listener를 등록한다.

---

<a id="js-22-section-12"></a>

## 8. 함수 이름 개선

기존:

```javascript
function discord() {
    // Listener 등록
}
```

개선:

```javascript
function initDiscordWebhookForm() {
    // Listener 등록
}
```

초기화 역할이 드러난다.

---

<a id="js-22-section-13"></a>

## 9. `defer` 사용

```html
<script
    src="./js/22_discord.js"
    defer
></script>
```

```javascript
initDiscordWebhookForm()
```

HTML과 JavaScript를 분리하고 DOM 파싱 후 실행한다.

---

<a id="js-22-section-14"></a>

## 10. 요소 선택

```javascript
const promptInput = (
    document.querySelector(
        "#prompt",
    )
)

const sendButton = (
    document.querySelector(
        "#ask",
    )
)

const statusView = (
    document.querySelector(
        "#status",
    )
)
```

---

<a id="js-22-section-15"></a>

## 11. 필수 요소 검사

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

---

<a id="js-22-section-16"></a>

## 12. Textarea 값 읽기

원본:

```javascript
const prompt = (
    document.querySelector(
        "#prompt",
    ).value
)
```

현재 입력값을 문자열로 가져온다.

---

<a id="js-22-section-17"></a>

## 13. 반복 선택 제거

고정된 요소는 Click마다 다시 선택하지 않고 초기화 시 한 번 선택할 수 있다.

```javascript
const promptInput = (
    getRequiredElement(
        "#prompt",
    )
)
```

---

<a id="js-22-section-18"></a>

## 14. 공백 제거

```javascript
const content = (
    promptInput.value.trim()
)
```

앞뒤 공백을 제거한다.

---

<a id="js-22-section-19"></a>

## 15. 빈 메시지 검증

```javascript
if (content === "") {
    statusView.textContent = (
        "메시지를 입력해주세요."
    )

    promptInput.focus()
    return
}
```

원본은 빈 문자열도 그대로 전송한다.

---

<a id="js-22-section-20"></a>

## 16. 길이 검증

외부 서비스에는 메시지와 표시 이름 길이 제한이 있을 수 있다.

```javascript
const MAX_CONTENT_LENGTH = 2000

if (
    content.length
    > MAX_CONTENT_LENGTH
) {
    statusView.textContent = (
        `메시지는 ${MAX_CONTENT_LENGTH}자 `
        + "이하로 입력해주세요."
    )

    return
}
```

정확한 제한은 실제 사용 시 해당 서비스의 최신 문서를 확인한다.

---

<a id="js-22-section-21"></a>

## 17. Webhook URL

내 원본:

```javascript
const url = ""
```

빈 문자열이므로 Discord Webhook으로 정상 전송되지 않는다.

---

<a id="js-22-section-22"></a>

## 18. 빈 URL의 동작

```javascript
xhr.open(
    "POST",
    "",
)
```

빈 URL은 현재 문서 URL을 기준으로 해석될 수 있다.

의도하지 않은 현재 페이지 요청이나 Server 오류가 발생할 수 있다.

---

<a id="js-22-section-23"></a>

## 19. 강사님 원본의 URL

강사님 원본에는 실제 Discord Webhook URL이 포함되어 있다.

이 URL은 다음 권한을 포함할 수 있다.

```text
해당 Webhook을 통한 메시지 전송
표시 이름 변경
허용된 Payload 전송
```

---

<a id="js-22-section-24"></a>

## 20. 노출된 Webhook 대응

```text
1. 기존 Webhook 삭제 또는 재생성
2. 새 URL을 Source에 작성하지 않기
3. Git History에서도 제거 검토
4. Backend 환경 변수에 저장
5. 전송 Endpoint에 인증·Rate Limit 적용
```

> [!WARNING]
> 문서에서 URL 문자열만 지워도 이미 공유된 Credential이 자동으로 안전해지는 것은 아니다.

---

<a id="js-22-section-25"></a>

## 21. `XMLHttpRequest` 생성

```javascript
const xhr = (
    new XMLHttpRequest()
)
```

하나의 요청 상태를 관리한다.

---

<a id="js-22-section-26"></a>

## 22. `open()`

원본:

```javascript
xhr.open(
    "post",
    url,
)
```

개선:

```javascript
xhr.open(
    "POST",
    url,
)
```

HTTP Method는 대소문자를 구분하지 않을 수 있지만 관례적으로 대문자를 사용한다.

---

<a id="js-22-section-27"></a>

## 23. `open()`은 전송이 아님

```text
open()
→ Method와 URL 설정

send()
→ 실제 요청 전송
```

---

<a id="js-22-section-28"></a>

## 24. Request Header

```javascript
xhr.setRequestHeader(
    "Content-Type",
    "application/json",
)
```

요청 Body가 JSON Text 형식임을 서버에 알린다.

---

<a id="js-22-section-29"></a>

## 25. Payload 객체

내 코드:

```javascript
const payload = {
    username: "zl존법사v",
    content,
}
```

강사님 코드:

```javascript
const payload = {
    username: "쵬니수",
    content,
}
```

핵심 HTTP 요청 구조는 동일하지만 `username` 외에도 URL 설정이 다르다. 내 URL은 빈 문자열이고 강사님 파일은 권한을 포함한 실제 Webhook 주소다. 내 버튼의 `type="buttn"` 오타도 함께 구분한다.

---

<a id="js-22-section-30"></a>

## 26. `username`

Webhook 메시지에 표시되는 이름을 지정한다.

서비스 정책에 따라 길이·문자 제한이 있을 수 있다.

고정 이름이면 사용자 입력으로 받지 않고 Server에서 관리할 수 있다.

---

<a id="js-22-section-31"></a>

## 27. `content`

```javascript
content: content
```

Property Shorthand:

```javascript
content
```

---

<a id="js-22-section-32"></a>

## 28. JSON 직렬화

```javascript
const body = JSON.stringify(
    payload,
)
```

JavaScript 객체를 JSON 문자열로 변환한다.

---

<a id="js-22-section-33"></a>

## 29. `send()`

```javascript
xhr.send(body)
```

설정한 요청을 실제로 전송한다.

---

<a id="js-22-section-34"></a>

## 30. 전체 원본 흐름

```javascript
const xhr = new XMLHttpRequest()

xhr.open(
    "POST",
    webhookUrl,
)

xhr.setRequestHeader(
    "Content-Type",
    "application/json",
)

const payload = {
    username: "알림봇",
    content,
}

xhr.send(
    JSON.stringify(
        payload,
    ),
)
```

---

<a id="js-22-section-35"></a>

## 31. 원본 `onload`

```javascript
xhr.onload = function () {
    console.log(
        xhr.responseText,
    )
}
```

응답 교환이 완료되면 실행된다.

---

<a id="js-22-section-36"></a>

## 32. `onload`와 성공 구분

`onload`가 실행되었다고 반드시 성공은 아니다.

HTTP 400·404·429·500 응답도 `onload`로 들어올 수 있다.

---

<a id="js-22-section-37"></a>

## 33. HTTP Status 검사

```javascript
const succeeded = (
    xhr.status >= 200
    && xhr.status < 300
)

if (succeeded) {
    statusView.textContent = (
        "메시지를 전송했습니다."
    )
}
```

---

<a id="js-22-section-38"></a>

## 34. 빈 Response Body

Webhook 전송 성공 시 응답 Body가 비어 있을 수 있다.

```text
responseText === ""
```

이어도 Status가 2xx라면 성공일 수 있다.

---

<a id="js-22-section-39"></a>

## 35. Response Body보다 Status

```text
잘못된 판단
→ responseText가 비었으므로 실패

올바른 판단
→ HTTP Status가 2xx인지 확인
```

---

<a id="js-22-section-40"></a>

## 36. 오류 Status 분기

```javascript
function getStatusMessage(
    status,
) {
    if (status === 400) {
        return "전송 데이터 형식이 올바르지 않습니다."
    }

    if (
        status === 401
        || status === 403
    ) {
        return "Webhook 인증 또는 권한을 확인해주세요."
    }

    if (status === 404) {
        return "Webhook을 찾을 수 없습니다."
    }

    if (status === 429) {
        return "요청이 너무 많습니다. 잠시 후 다시 시도해주세요."
    }

    return (
        `전송에 실패했습니다. HTTP ${status}`
    )
}
```

---

<a id="js-22-section-41"></a>

## 37. Network Error

```javascript
xhr.onerror = function () {
    statusView.textContent = (
        "네트워크 오류가 발생했습니다."
    )
}
```

HTTP 응답을 받은 실패와 Network 단계 실패를 구분한다.

---

<a id="js-22-section-42"></a>

## 38. Timeout

```javascript
xhr.timeout = 10000

xhr.ontimeout = function () {
    statusView.textContent = (
        "요청 시간이 초과되었습니다."
    )
}
```

---

<a id="js-22-section-43"></a>

## 39. 요청 종료

```javascript
xhr.onloadend = function () {
    sendButton.disabled = false
}
```

성공·HTTP 오류·Network Error 이후 공통 정리를 수행할 수 있다.

---

<a id="js-22-section-44"></a>

## 40. 중복 요청 방지

```javascript
if (sendButton.disabled) {
    return
}

sendButton.disabled = true
```

빠른 연속 Click으로 같은 메시지가 여러 번 전송되는 것을 줄인다.

---

<a id="js-22-section-45"></a>

## 41. Loading 상태

```javascript
statusView.textContent = (
    "메시지를 전송하는 중입니다."
)
```

요청이 시작되었음을 화면으로 알린다.

---

<a id="js-22-section-46"></a>

## 42. 성공 후 초기화

```javascript
promptInput.value = ""
promptInput.focus()
```

전송이 성공했을 때만 입력창을 비운다.

---

<a id="js-22-section-47"></a>

## 43. 실패 시 입력 유지

실패한 경우 메시지를 유지하면 사용자가 수정하거나 다시 시도할 수 있다.

```text
성공
→ Textarea 초기화

실패
→ 기존 입력 유지
```

---

<a id="js-22-section-48"></a>

## 44. 안전한 XHR 완성본

```javascript
function sendDiscordMessage({
    endpoint,
    content,
    onSuccess,
    onError,
    onFinally,
}) {
    const xhr = (
        new XMLHttpRequest()
    )

    xhr.open(
        "POST",
        endpoint,
    )

    xhr.setRequestHeader(
        "Content-Type",
        "application/json",
    )

    xhr.timeout = 10000

    xhr.onload = () => {
        if (
            xhr.status >= 200
            && xhr.status < 300
        ) {
            onSuccess()
            return
        }

        onError(
            getStatusMessage(
                xhr.status,
            ),
        )
    }

    xhr.onerror = () => {
        onError(
            "네트워크 오류가 발생했습니다.",
        )
    }

    xhr.ontimeout = () => {
        onError(
            "요청 시간이 초과되었습니다.",
        )
    }

    xhr.onloadend = onFinally

    xhr.send(
        JSON.stringify({
            content,
        }),
    )
}
```

---

<a id="js-22-section-49"></a>

## 45. Frontend 직접 호출의 문제

```text
Browser
→ Discord Webhook 직접 호출
```

문제:

- Webhook URL 노출
- 누구나 URL 재사용 가능
- 사용자 인증 없음
- Rate Limit 제어 어려움
- 입력 검증 우회 가능
- Spam·Abuse 위험
- CORS 정책 영향

---

<a id="js-22-section-50"></a>

## 46. Backend Proxy 구조

```text
Frontend
→ /api/discord-message

Backend
→ 사용자 인증
→ 입력 검증
→ Rate Limit
→ Environment Variable의 Webhook URL
→ Discord Webhook 호출
```

---

<a id="js-22-section-51"></a>

## 47. Frontend 요청 데이터 최소화

```javascript
const requestBody = {
    content,
}
```

Frontend에서 Webhook URL과 `username`을 제어하지 않게 만들 수 있다.

---

<a id="js-22-section-52"></a>

## 48. Backend 환경 변수

```text
DISCORD_WEBHOOK_URL
```

Source Code와 Git Repository에 URL을 직접 작성하지 않는다.

---

<a id="js-22-section-53"></a>

## 49. Backend 검증 항목

- 사용자 인증 여부
- 허용된 메시지 길이
- 공백 메시지
- 금지어·Spam
- 요청 횟수
- 허용된 출처
- Audit Log
- Timeout
- 외부 API 오류

---

<a id="js-22-section-54"></a>

## 50. Public Endpoint 위험

Backend Proxy도 인증과 Rate Limit 없이 Public으로 열려 있다면 Spam 전송 통로가 될 수 있다.

```text
Secret 숨김
≠ Endpoint가 자동으로 안전함
```

---

<a id="js-22-section-55"></a>

## 51. Fetch로 전환

```javascript
const response = await fetch(
    "/api/discord-message",
    {
        method: "POST",

        headers: {
            "Content-Type":
                "application/json",
        },

        body: JSON.stringify({
            content,
        }),
    },
)
```

---

<a id="js-22-section-56"></a>

## 52. Fetch HTTP 오류

```javascript
if (!response.ok) {
    throw new Error(
        `HTTP ${response.status}`,
    )
}
```

Fetch는 HTTP 400·500을 자동으로 Reject하지 않을 수 있다.

---

<a id="js-22-section-57"></a>

## 53. 429 별도 처리

```javascript
if (response.status === 429) {
    throw new Error(
        "요청이 너무 많습니다. "
        + "잠시 후 다시 시도해주세요.",
    )
}
```

---

<a id="js-22-section-58"></a>

## 54. Fetch Network Error

```javascript
try {
    const response = await fetch(
        endpoint,
        options,
    )
} catch (
    error
) {
    console.error(
        "Network 요청 실패",
        error,
    )
}
```

---

<a id="js-22-section-59"></a>

## 55. AbortController

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

사용자가 전송을 취소하거나 Timeout을 구현할 때 사용할 수 있다.

---

<a id="js-22-section-60"></a>

## 56. Fetch Timeout

```javascript
const controller = (
    new AbortController()
)

const timeoutId = setTimeout(
    () => {
        controller.abort()
    },
    10000,
)

try {
    const response = await fetch(
        endpoint,
        {
            method: "POST",
            signal: controller.signal,
        },
    )
} finally {
    clearTimeout(timeoutId)
}
```

---

<a id="js-22-section-61"></a>

## 57. 원본 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 핵심 흐름 | XHR POST | XHR POST |
| Webhook URL | 빈 문자열 | 실제 URL 포함 |
| Credential 안전성 | 직접 노출하지 않음 | 노출 위험 |
| Username | `zl존법사v` | `쵬니수` |
| Payload 주석 | 있음 | 없음 |
| Username 제한 주석 | 없음 | 있음 |
| Button Type | `buttn` 오타 | `button` |
| Body 임시 Text | `test` 있음 | 없음 |
| Status 검사 | 없음 | 없음 |
| Network Error | 없음 | 없음 |
| 빈 입력 검증 | 없음 | 없음 |
| 중복 요청 방지 | 없음 | 없음 |

---

<a id="js-22-section-62"></a>

## 58. 내 코드의 장점

- Webhook URL을 빈 문자열로 두어 실제 Credential을 직접 노출하지 않았다.
- Discord 전송 Payload라는 주석을 추가했다.
- `Content-Type: application/json`을 설정했다.
- 객체를 `JSON.stringify()`로 직렬화했다.
- 강사님 코드와 같은 핵심 XHR 흐름을 구현했다.

---

<a id="js-22-section-63"></a>

## 59. 내 코드의 개선점

- 빈 URL이라 실제 Discord 전송이 불가능하다.
- `type="buttn"` 오타가 있다.
- Body에 `test` 문자열이 남아 있다.
- 입력값을 `trim()`하지 않는다.
- 빈 메시지를 전송한다.
- Status·Network Error·Timeout을 처리하지 않는다.
- 중복 Click을 막지 않는다.
- 성공·실패 상태를 화면에 표시하지 않는다.
- 성공 후 입력값을 초기화하지 않는다.
- `lang`과 `title`이 문서 내용에 맞지 않는다.

---

<a id="js-22-section-64"></a>

## 60. 강사님 코드의 장점

- 실제 Webhook POST 요청 구조를 간결하게 보여 준다.
- Button Type이 올바르다.
- `username`, `content` Payload를 구성한다.
- Request Header와 직렬화 흐름이 명확하다.
- Webhook이 실제 Channel 메시지로 연결되는 과정을 확인할 수 있다.

---

<a id="js-22-section-65"></a>

## 61. 강사님 코드의 개선점

- 실제 Webhook URL을 Browser Source에 포함한다.
- 공유·Commit 시 제3자가 악용할 수 있다.
- Status를 검사하지 않는다.
- `responseText`만 출력한다.
- Network Error와 Timeout 처리가 없다.
- 빈 입력 검증이 없다.
- 중복 전송 방지가 없다.
- 사용자 상태 표시가 없다.
- Backend Proxy 구조가 없다.

---

<a id="js-22-section-66"></a>

## 62. 기존 코드에서 개선한 이유

### 62-1. Button Type

기존:

```html
type="buttn"
```

개선:

```html
type="button"
```

### 62-2. Method 표기

기존:

```javascript
xhr.open(
    "post",
    url,
)
```

개선:

```javascript
xhr.open(
    "POST",
    url,
)
```

### 62-3. 성공 판단

기존:

```javascript
console.log(
    xhr.responseText,
)
```

개선:

```javascript
if (
    xhr.status >= 200
    && xhr.status < 300
) {
    // 성공
}
```

### 62-4. Credential 관리

기존:

```text
Frontend Source
→ 실제 Webhook URL
```

개선:

```text
Frontend
→ Backend Proxy
→ Environment Variable의 Webhook URL
```

---

<a id="js-22-section-67"></a>

## 63. 실무형 예제: 안전한 Discord 알림 Form

```javascript
function initDiscordForm() {
    const form = getRequiredElement(
        "#discord-form",
    )

    const promptInput = (
        getRequiredElement(
            "#prompt",
        )
    )

    const sendButton = (
        getRequiredElement(
            "#ask",
        )
    )

    const statusView = (
        getRequiredElement(
            "#status",
        )
    )

    let isSubmitting = false

    form.addEventListener(
        "submit",
        async event => {
            event.preventDefault()

            if (isSubmitting) {
                return
            }

            const content = (
                promptInput
                    .value
                    .trim()
            )

            if (content === "") {
                statusView.textContent = (
                    "메시지를 입력해주세요."
                )

                promptInput.focus()
                return
            }

            isSubmitting = true
            sendButton.disabled = true

            statusView.textContent = (
                "메시지를 전송하는 중입니다."
            )

            try {
                const response = await fetch(
                    "/api/discord-message",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json",
                        },

                        body: JSON.stringify({
                            content,
                        }),
                    },
                )

                if (
                    response.status
                    === 429
                ) {
                    throw new Error(
                        "요청이 너무 많습니다. "
                        + "잠시 후 다시 시도해주세요.",
                    )
                }

                if (!response.ok) {
                    throw new Error(
                        `HTTP ${response.status}`,
                    )
                }

                statusView.textContent = (
                    "메시지를 전송했습니다."
                )

                promptInput.value = ""
            } catch (
                error
            ) {
                statusView.textContent = (
                    "메시지 전송에 실패했습니다."
                )

                console.error(error)
            } finally {
                isSubmitting = false
                sendButton.disabled = false
                promptInput.focus()
            }
        },
    )
}
```

### 63-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| Form Submit | Click·Enter 전송 통합 |
| `trim()` | 빈 메시지 차단 |
| Loading Flag | 중복 요청 방지 |
| Disabled Button | 사용자 중복 입력 방지 |
| Backend Endpoint | Webhook URL 비공개 |
| JSON Body | 메시지 데이터 전송 |
| `response.ok` | HTTP 오류 확인 |
| 429 분기 | Rate Limit 별도 안내 |
| Status View | 전송 상태 표시 |
| `finally` | Button과 Focus 복구 |

---

<a id="js-22-section-68"></a>

## 64. 대표 오류로 이해하기

### 64-1. 빈 URL 요청

현재 문서나 잘못된 Endpoint로 요청될 수 있다.

### 64-2. Webhook URL 노출

누구나 해당 URL로 메시지를 전송할 수 있다.

### 64-3. `onload`만 보고 성공 판단

HTTP 오류도 `onload`가 실행될 수 있다.

### 64-4. Response Body가 빈 값

성공 응답일 수 있으므로 Status를 확인한다.

### 64-5. 빠른 연속 Click

같은 메시지가 여러 번 전송될 수 있다.

### 64-6. Public Proxy에 인증 없음

Webhook URL은 숨겼지만 Spam Endpoint가 될 수 있다.

---

<a id="js-22-section-69"></a>

## 65. 자주 하는 실수

### 65-1. Webhook URL을 일반 공개 URL로 생각

메시지 전송 권한을 포함한 Credential로 취급한다.

### 65-2. `.gitignore`만으로 Browser Key 보호

Bundle에 들어가면 사용자에게 노출된다.

### 65-3. `open()`이 요청을 전송한다고 생각

실제 전송은 `send()`다.

### 65-4. 객체를 그대로 XHR Body에 전달

JSON API라면 `JSON.stringify()`가 필요하다.

### 65-5. 빈 입력과 공백 입력을 구분하지 않음

`trim()` 후 검사한다.

<a id="index-section-93"></a>

### 65-6. `responseText`가 비면 실패라고 생각

Status가 성공일 수 있다.

<a id="index-section-94"></a>

### 65-7. `xhr.onerror`가 HTTP 400도 처리한다고 생각

Network Error와 HTTP 오류는 다르다.

<a id="index-section-95"></a>

### 65-8. Rate Limit 무시

429 응답과 재시도 정책을 고려한다.

### 65-9. 실패 후 입력을 지움

재시도할 수 있도록 실패 시 입력을 유지한다.

### 65-10. Backend Proxy면 자동으로 안전하다고 생각

인증·Rate Limit·검증이 필요하다.

---

<a id="js-22-section-70"></a>

## 66. 핵심 요약

```text
Textarea
→ content

Payload 객체
→ JSON.stringify()

XHR POST
→ Webhook 호출
```

```text
open()
→ 요청 설정

setRequestHeader()
→ Body 형식 설정

send()
→ 실제 전송
```

```text
2xx
→ 성공

4xx·5xx
→ HTTP 오류

onerror
→ Network 오류
```

```text
Webhook URL
→ Secret Credential처럼 관리

Frontend
→ Backend Proxy

Backend
→ Discord Webhook
```

---

<a id="js-22-section-71"></a>

## 67. 최종 체크리스트

- [ ] Textarea에 Label을 연결했는가?
- [ ] Button Type을 올바르게 작성했는가?
- [ ] 임시 `test` 문자열을 제거했는가?
- [ ] 입력값을 `trim()`했는가?
- [ ] 빈 메시지를 차단하는가?
- [ ] 메시지 길이를 검증하는가?
- [ ] XHR Method를 `POST`로 설정했는가?
- [ ] `Content-Type: application/json`을 설정했는가?
- [ ] Payload 객체를 직렬화했는가?
- [ ] `open()`과 `send()`를 구분하는가?
- [ ] HTTP Status를 검사하는가?
- [ ] 빈 Response Body도 성공일 수 있음을 이해했는가?
- [ ] Network Error를 처리하는가?
- [ ] Timeout을 처리하는가?
- [ ] 429 Rate Limit을 별도로 처리하는가?
- [ ] 요청 중 Button을 비활성화하는가?
- [ ] 성공·실패 상태를 화면에 표시하는가?
- [ ] 성공 후에만 Textarea를 초기화하는가?
- [ ] 실패 시 입력값을 유지하는가?
- [ ] 실제 Webhook URL을 Frontend에 넣지 않는가?
- [ ] 노출된 기존 Webhook을 폐기·재생성했는가?
- [ ] Git History의 Credential 제거를 검토했는가?
- [ ] Backend 환경 변수에 URL을 저장하는가?
- [ ] Proxy Endpoint에 인증과 Rate Limit을 적용하는가?
- [ ] Fetch 전환 시 `response.ok`를 검사하는가?

---

<a id="js-22-section-72"></a>

## 마무리

Discord Webhook 연동의 핵심은 JSON 메시지를 POST로 전송하는 것에서 끝나지 않는다.

```text
사용자 입력을 먼저 검증하고
    ↓
요청·응답 상태를 정확히 구분하고
    ↓
중복 전송과 Rate Limit을 관리하고
    ↓
성공·실패 상태를 사용자에게 알리고
    ↓
Webhook Credential을 Backend에서 안전하게 보호하는 것
```

이 흐름을 이해하면 Discord 알림뿐 아니라 Slack·Teams·사내 알림 시스템 같은 Webhook 기반 연동도 더 안전하게 구현할 수 있다.
<a id="js-22-section-73"></a>

## V3 실행 추적 카드 — 폼/데이터 → HTTP 요청 → 상태 변화 → 성공·실패 처리

XMLHttpRequest는 readyState 변화와 status를 통해 진행을 관찰한다. Webhook URL은 쓰기 권한을 가진 비밀값이므로 공개 저장소나 브라우저 배포 코드에 그대로 두면 안 된다.

상태 4에서 HTTP 상태와 응답을 확인하고 Network에서도 요청을 검증한다. 실습 문서에는 실제 Webhook 토큰 대신 자리표시자를 사용한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/22_discord.html`에서 실제 사용 위치와 차이를 확인한다.
