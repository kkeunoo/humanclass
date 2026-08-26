---
title: JavaScript BOM과 지도·우편번호 API
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# JavaScript BOM과 지도·우편번호 API

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `18_JavaScript_BOM과_지도우편번호API.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/18_map.html`, `workspace_teacher/workspace_html/javascript/18_map.html` |
| 핵심 범위 | BOM, `window`, `location`, `history`, `window.open()`, Popup, Kakao Postcode, Kakao Rough Map |
| 실습 범위 | URL 확인·이동·새로고침, 뒤로·앞으로 이동, Popup 열기, 주소·우편번호 검색, 지도 삽입 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 18번은 브라우저 창과 주소·방문 기록을 제어하는 BOM 기능을 학습한 뒤, 외부 주소 검색·지도 Embed 기능으로 연결한다.  
> 외부 서비스는 네트워크·서비스 정책·Script 로드 상태에 영향을 받으므로 성공뿐 아니라 실패 처리도 함께 설계해야 한다.

---

# 개요

BOM은 Browser Object Model의 약자다.

DOM이 HTML 문서 구조를 다룬다면 BOM은 브라우저 창과 브라우저가 제공하는 기능을 다룬다.

```text
Window
├── Document
├── Location
├── History
├── Navigator
├── Screen
└── Timer
```

대표 코드:

```javascript
console.log(
    window.location.href,
)

window.history.back()

window.open(
    "./popup.html",
)
```

> [!IMPORTANT]
> `window`, `location`, `history`는 브라우저 환경에서 제공된다. Node.js처럼 브라우저가 아닌 환경에서는 동일하게 사용할 수 없다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| BOM | 브라우저 창과 기능을 객체로 제공 |
| `window` | 브라우저 JavaScript의 전역 객체 |
| `location` | 현재 문서 URL 정보와 이동 기능 |
| `history` | 현재 Tab의 Session History 이동 |
| `window.open()` | 새 Tab·Popup 열기 |
| Popup Blocker | 사용자 동작 없이 열린 창 차단 |
| Same-Origin Policy | 서로 다른 Origin 간 접근 제한 |
| `noopener` | 새 창의 `opener` 접근 차단 |
| Callback | 특정 작업 완료 후 실행되는 함수 |
| External API | 외부 서비스가 제공하는 기능 |
| Mixed Content | HTTPS 페이지에서 HTTP 자원 로드 |
| Embed | 외부 콘텐츠를 현재 페이지에 삽입 |

---

# 학습 목표

- BOM과 DOM의 차이를 설명할 수 있다.
- `window` 객체의 역할을 이해한다.
- `location` 객체와 `location.href` 문자열을 구분할 수 있다.
- URL을 안전하게 변경할 수 있다.
- `assign()`과 `replace()`의 차이를 이해한다.
- 현재 페이지를 새로고침할 수 있다.
- `history.back()`, `forward()`, `go()`를 사용할 수 있다.
- 버튼 문구와 실제 History 이동 단계를 일치시킬 수 있다.
- `window.open()`의 세 인수를 설명할 수 있다.
- Popup 차단 여부를 확인할 수 있다.
- 새 창 이름에 따른 재사용 동작을 이해한다.
- Same-Origin과 `window.opener` 보안을 이해한다.
- Kakao Postcode의 완료 Callback을 이해한다.
- 주소와 우편번호를 실제 Form Input에 연결할 수 있다.
- 외부 Script가 준비되지 않은 상태를 처리할 수 있다.
- 이미지형 지도와 Script형 Rough Map을 구분할 수 있다.
- HTTP 자원을 HTTPS 페이지에서 사용하면 생기는 문제를 설명할 수 있다.
- 외부 Embed의 ID·Timestamp·Key를 일관되게 관리할 수 있다.

---

# 1. BOM과 DOM

```text
DOM
→ 현재 HTML 문서와 Element

BOM
→ Browser Window와 Browser 기능
```

DOM도 `window.document`를 통해 Window 객체 아래에서 접근할 수 있다.

---

# 2. Window 객체

```javascript
console.log(window)
```

브라우저 JavaScript의 전역 객체다.

다음 표현은 브라우저에서 같은 객체를 가리킨다.

```javascript
console.log(
    window.location
    === location,
)

console.log(
    window.history
    === history,
)
```

---

# 3. 전역 함수와 Window

브라우저의 일반 Script에서 전역에 선언된 함수·`var`는 `window` property와 연결될 수 있다.

```javascript
function greet() {
    console.log("hello")
}

window.greet()
```

Module Script에서는 전역 노출 방식이 다르다.

---

# 4. 원본 초기화

양쪽 원본은 `window.onload`에서 Button Listener를 등록한다.

```javascript
window.onload = () => {
    // Button 선택
    // Click Listener 등록
}
```

Body와 외부 자원이 모두 Load된 뒤 실행된다.

---

# 5. `defer` 방식

DOM 요소 선택만 필요하다면 다음 구조를 사용할 수 있다.

```html
<script
    src="./js/18_map.js"
    defer
></script>
```

```javascript
init()
```

---

# 6. Location 객체

```javascript
console.log(location)
```

현재 문서 URL과 관련된 정보를 가진 객체다.

---

# 7. `location.href`

```javascript
console.log(
    location.href,
)
```

현재 페이지의 전체 URL 문자열이다.

출력 예:

```text
http://127.0.0.1:5500/javascript/18_map.html
```

실제 값은 실행 환경에 따라 달라진다.

---

# 8. Location 주요 Property

| Property | 의미 |
| --- | --- |
| `href` | 전체 URL |
| `protocol` | `http:`, `https:` |
| `host` | Hostname과 Port |
| `hostname` | Domain·IP |
| `port` | Port 번호 |
| `pathname` | 경로 |
| `search` | Query String |
| `hash` | Fragment |

---

# 9. URL 객체로 분석

```javascript
const currentUrl = new URL(
    location.href,
)

console.log(
    currentUrl.pathname,
)

console.log(
    currentUrl.searchParams,
)
```

문자열을 직접 `split()`하는 것보다 URL 구조를 안전하게 다룰 수 있다.

---

# 10. `location.href` 변경

원본:

```javascript
location.href = (
    "http://naver.com"
)
```

새 페이지로 이동한다.

개선:

```javascript
location.href = (
    "https://www.naver.com"
)
```

HTTPS를 명시한다.

---

# 11. HTTP 사용 문제

HTTP URL은 다음 문제가 있을 수 있다.

- 통신 암호화 없음
- HTTPS로 Redirect될 수 있음
- 중간자 공격 위험
- Mixed Content와 보안 정책 문제
- 동작 예측 어려움

---

# 12. `location.assign()`

```javascript
location.assign(
    "https://www.naver.com",
)
```

새 URL로 이동하며 일반적으로 현재 페이지가 History에 남는다.

---

# 13. `location.replace()`

```javascript
location.replace(
    "https://www.naver.com",
)
```

현재 History Entry를 새 URL로 교체한다.

로그인 완료 후 로그인 페이지로 되돌아가면 안 되는 흐름 등에 사용할 수 있다.

---

# 14. 이동 방식 비교

| 방식 | 현재 Entry 유지 | 뒤로가기 |
| --- | --- | --- |
| `href = URL` | 일반적으로 유지 | 가능 |
| `assign(URL)` | 일반적으로 유지 | 가능 |
| `replace(URL)` | 현재 Entry 교체 | 이전 페이지로 직접 복귀 어려움 |

---

# 15. `location.reload()`

```javascript
location.reload()
```

현재 페이지를 다시 Load한다.

---

# 16. 새로고침 후 상태

새로고침하면 일반 JavaScript 변수와 현재 DOM 변경은 초기화된다.

유지해야 하는 상태는 다음 저장소를 검토한다.

- URL Query String
- `sessionStorage`
- `localStorage`
- Cookie
- Server Session
- Database

---

# 17. History 객체

```javascript
console.log(history)
```

현재 Tab의 Session History 이동 기능을 제공한다.

보안상 방문한 URL 목록 전체를 JavaScript에서 직접 읽을 수는 없다.

---

# 18. `history.length`

```javascript
console.log(
    history.length,
)
```

현재 Tab Session History의 Entry 개수를 나타내지만 실제 URL 목록은 제공하지 않는다.

---

# 19. 한 단계 뒤로

```javascript
history.back()
```

다음과 비슷한 의미다.

```javascript
history.go(-1)
```

---

# 20. 한 단계 앞으로

```javascript
history.forward()
```

다음과 비슷하다.

```javascript
history.go(1)
```

앞으로 갈 Entry가 없으면 이동하지 않는다.

---

# 21. `history.go()`

```javascript
history.go(-2)
```

두 단계 이전 History Entry로 이동한다.

---

# 22. 원본 버튼 문구 불일치

원본 Button은 “뒤로가기”처럼 표시되지만 실제 코드는 다음을 실행한다.

```javascript
history.go(-2)
```

사용자는 한 단계 뒤로 이동한다고 예상할 수 있으므로 문구와 동작을 맞춰야 한다.

---

# 23. Button 문구 개선

```html
<button
    type="button"
    id="go-back-two"
>
    두 단계 뒤로
</button>
```

```javascript
goBackTwo.addEventListener(
    "click",
    () => {
        history.go(-2)
    },
)
```

---

# 24. History 이동 제한

다음 상황에서는 기대한 페이지로 이동하지 않을 수 있다.

- 이전 Entry가 없음
- 새 Tab에서 직접 접속
- Browser 정책
- 외부 사이트와의 이동 이력
- SPA Router가 History를 변경함

---

# 25. `window.open()`

```javascript
const popup = window.open(
    "./17_event_form.html",
    "eventFormPopup",
    "width=800,height=600",
)
```

---

# 26. 세 인수

```text
첫 번째
→ 열 URL

두 번째
→ 창 이름·Target 이름

세 번째
→ Popup Option 문자열
```

---

# 27. Popup Option

```javascript
const popupOptions = [
    "width=800",
    "height=600",
    "left=100",
    "top=100",
].join(",")

window.open(
    "./17_event_form.html",
    "eventFormPopup",
    popupOptions,
)
```

변경하지 않는 값은 `const`로 선언한다.

---

# 28. Popup 반환값

```javascript
const popup = window.open(
    "./popup.html",
    "popupName",
    popupOptions,
)

console.log(popup)
```

성공하면 새 창의 Window 참조를 반환할 수 있다.

차단되면 `null`일 수 있다.

---

# 29. Popup 차단 처리

```javascript
if (popup === null) {
    alert(
        "Popup이 차단되었습니다. "
        + "Browser 설정을 확인해주세요.",
    )
}
```

---

# 30. 사용자 동작과 Popup

Popup은 Button Click 같은 직접적인 사용자 동작 안에서 열어야 차단 가능성을 줄일 수 있다.

```javascript
openButton.addEventListener(
    "click",
    () => {
        window.open(
            "./popup.html",
        )
    },
)
```

Timer·비동기 Callback 뒤에서 열면 차단될 수 있다.

---

# 31. 같은 Window Name

```javascript
window.open(
    "./page-a.html",
    "myPopup",
)

window.open(
    "./page-b.html",
    "myPopup",
)
```

같은 이름의 Window가 존재하면 새 Window 대신 기존 Window를 재사용할 수 있다.

---

# 32. `_blank`

```javascript
window.open(
    "https://example.com",
    "_blank",
)
```

새 Tab 또는 Window를 열도록 요청한다.

실제 표시 형태는 Browser 설정에 따라 달라진다.

---

# 33. Same-Origin Policy

새 창과 현재 창이 다음 Origin 구성요소를 모두 공유해야 DOM 접근이 허용되는 범위가 넓다.

```text
Protocol
Host
Port
```

다른 Origin의 페이지 내부 DOM을 마음대로 읽을 수 없다.

---

# 34. `window.opener`

새 창은 열어 준 창을 `window.opener`로 참조할 수 있는 경우가 있다.

외부 페이지가 Opener를 조작하는 위험을 줄이려면 Link에서 다음을 사용한다.

```html
<a
    href="https://example.com"
    target="_blank"
    rel="noopener noreferrer"
>
    새 창
</a>
```

---

# 35. `window.open()` 보안 설명

`window.open()` 자체가 무조건 위험한 것은 아니다.

다음 항목을 함께 관리해야 한다.

- 사용자 동작 안에서 실행
- 신뢰 가능한 URL
- Same-Origin 이해
- Popup 차단 처리
- `opener` 접근 제한
- 반환 Window 참조 검증

---

# 36. Kakao Postcode Script

원본은 외부 Script를 불러온다.

```html
<script
    src="//t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"
></script>
```

Protocol-relative URL이다.

---

# 37. 명시적 HTTPS

```html
<script
    src="https://t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"
></script>
```

Protocol을 명시하면 HTTPS 페이지에서 동작을 예측하기 쉽다.

---

# 38. Postcode 객체 생성

```javascript
const postcode = (
    new kakao.Postcode({
        oncomplete(
            data,
        ) {
            console.log(data)
        },
    })
)
```

---

# 39. `.open()`

```javascript
postcode.open()
```

주소 검색 UI를 연다.

한 번에 작성할 수도 있다.

```javascript
new kakao.Postcode({
    oncomplete(
        data,
    ) {
        console.log(data)
    },
}).open()
```

---

# 40. `oncomplete`

사용자가 검색 결과에서 주소를 선택해 검색이 완료되면 실행되는 Callback이다.

```text
oncomplete(
    data,
) {
    console.log(
        data.address,
    )

    console.log(
        data.zonecode,
    )
}
```

---

# 41. Address와 Zonecode

| Property | 의미 |
| --- | --- |
| `data.address` | 선택된 기본 주소 |
| `data.zonecode` | 우편번호 |
| `data.roadAddress` | 도로명 주소 |
| `data.jibunAddress` | 지번 주소 |

실제 응답 Property는 서비스 문서를 기준으로 확인한다.

---

# 42. 원본 결과 처리

원본은 결과를 Console에 출력한다.

```javascript
console.log(data)
console.log(data.address)
console.log(data.zonecode)
```

학습에는 도움이 되지만 실제 Form에서는 Input에 연결해야 한다.

---

# 43. 주소 Form

```html
<label for="postcode">
    우편번호
</label>

<input
    type="text"
    id="postcode"
    readonly
>

<button
    type="button"
    id="find-postcode"
>
    주소 검색
</button>

<label for="address">
    기본 주소
</label>

<input
    type="text"
    id="address"
    readonly
>

<label for="detail-address">
    상세 주소
</label>

<input
    type="text"
    id="detail-address"
>
```

---

# 44. 주소 결과 연결

```javascript
findPostcodeButton.addEventListener(
    "click",
    () => {
        new kakao.Postcode({
            oncomplete(
                data,
            ) {
                postcodeInput.value = (
                    data.zonecode
                )

                addressInput.value = (
                    data.address
                )

                detailAddressInput.focus()
            },
        }).open()
    },
)
```

---

# 45. Readonly 사용

사용자가 검색 결과 필드를 임의로 바꾸지 않도록 다음 Input에 `readonly`를 사용할 수 있다.

```text
우편번호
기본 주소
```

상세 주소는 사용자가 직접 입력할 수 있게 둔다.

---

# 46. API 존재 검사

외부 Script가 Load되지 않았다면 `kakao` 접근에서 오류가 발생할 수 있다.

```javascript
const postcodeAvailable = (
    typeof window.kakao
    !== "undefined"
    && typeof window
        .kakao
        .Postcode
    === "function"
)
```

---

# 47. 실패 안내

```javascript
if (!postcodeAvailable) {
    alert(
        "주소 검색 기능을 "
        + "불러오지 못했습니다.",
    )

    return
}
```

---

# 48. 안전한 주소 검색 함수

```javascript
function openPostcodeSearch() {
    const available = (
        typeof window.kakao
        !== "undefined"
        && typeof window
            .kakao
            .Postcode
        === "function"
    )

    if (!available) {
        addressError.textContent = (
            "주소 검색 서비스를 "
            + "사용할 수 없습니다."
        )

        return
    }

    addressError.textContent = ""

    new window.kakao.Postcode({
        oncomplete(
            data,
        ) {
            postcodeInput.value = (
                data.zonecode
            )

            addressInput.value = (
                data.address
            )

            detailAddressInput.focus()
        },
    }).open()
}
```

---

# 49. 외부 Script Load Event

```javascript
const script = (
    document.createElement(
        "script",
    )
)

script.src = (
    "https://example.com/api.js"
)

script.addEventListener(
    "load",
    () => {
        console.log(
            "API 준비 완료",
        )
    },
)

script.addEventListener(
    "error",
    () => {
        console.error(
            "API Load 실패",
        )
    },
)

document.head.append(script)
```

---

# 50. 동적 Script 중복 방지

```javascript
if (
    document.querySelector(
        '[data-api="postcode"]',
    )
    !== null
) {
    return
}
```

같은 API Script를 여러 번 삽입하지 않도록 식별 Attribute를 사용할 수 있다.

---

# 51. 외부 API 의존성

외부 API는 다음 상황에 영향을 받는다.

- Network 단절
- Script 차단 Extension
- 서비스 장애
- API URL 변경
- 정책·약관 변경
- Browser 보안 설정
- 서비스 종료

Fallback 안내가 필요하다.

---

# 52. 이미지형 지도

원본 첫 지도는 이미지와 Link로 구성된 정적 지도 형태다.

```text
지도 이미지
+ 장소 상세 페이지 Link
```

사용자가 지도를 직접 확대·축소하는 인터랙티브 지도와는 다르다.

---

# 53. 이미지형 지도 장점

- 구현이 간단함
- JavaScript 의존이 적음
- 초기 표시가 빠를 수 있음
- 정적 위치 안내에 적합

---

# 54. 이미지형 지도 한계

- 확대·축소 제한
- 외부 이미지 URL 의존
- URL 만료 가능성
- HTTP 이미지의 Mixed Content
- 접근성 설명 필요
- 장소 정보 변경 반영 문제

---

# 55. Mixed Content

HTTPS 페이지에서 HTTP 이미지·Script를 Load하면 Browser가 차단하거나 경고할 수 있다.

원본 첫 지도 이미지 URL이 HTTP라면 다음처럼 개선한다.

```text
http://...
→ https://...
```

서비스가 HTTPS를 지원하는지 먼저 확인한다.

---

# 56. 지도 Link 보안

```html
<a
    href="https://map.kakao.com/..."
    target="_blank"
    rel="noopener noreferrer"
>
    지도 크게 보기
</a>
```

---

# 57. 지도 이미지 `alt`

```html
<img
    src="https://..."
    alt="교육센터 위치 지도"
>
```

단순히 `alt=""`로 두기보다 이미지가 전달하는 장소 정보를 설명한다.

장식용 이미지라면 빈 `alt`를 사용할 수 있다.

---

# 58. Rough Map

두 번째 지도는 Loader Script와 `daum.roughmap.Lander`를 사용해 렌더링한다.

```javascript
new daum.roughmap.Lander({
    timestamp: "값",
    key: "값",
    mapWidth: "640",
    mapHeight: "360",
}).render()
```

---

# 59. Container ID

```html
<div
    id="daumRoughmapContainer123"
    class="root_daum_roughmap root_daum_roughmap_landing"
></div>
```

Renderer가 지정한 Embed Instance와 Container를 연결한다.

---

# 60. Timestamp·Key 일치

다음 값은 한 Embed 세트 안에서 서로 맞아야 한다.

```text
Container ID
Timestamp
Key
```

내 코드와 강사님 코드의 값을 섞으면 지도가 표시되지 않을 수 있다.

---

# 61. Loader 중복 삽입

같은 Rough Map Loader를 페이지에 여러 번 삽입하지 않는다.

```javascript
if (
    typeof window.daum
    !== "undefined"
    && window.daum.roughmap
) {
    renderMap()
}
```

---

# 62. Inline Style 개선

외부 Embed가 긴 Inline Style을 제공하더라도 직접 작성하는 프로젝트 UI는 CSS File로 분리한다.

```css
.map-section {
    max-width: 640px;
    margin: 0 auto;
}
```

---

# 63. 외부 지도 Fallback

```html
<div id="map-status">
    지도를 불러오는 중입니다.
</div>
```

Load 실패 시:

```javascript
mapStatus.textContent = (
    "지도를 불러오지 못했습니다. "
    + "주소를 직접 확인해주세요."
)
```

---

# 64. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| BOM 흐름 | 동일 | 동일 |
| 설명 주석 | 더 상세 | 핵심 중심 |
| Location | 동일 | 동일 |
| History | 동일 | 동일 |
| Popup | 동일 | 동일 |
| Postcode | 결과 Console 출력 | 결과 Console 출력 |
| 첫 지도 이미지 Hash | 서로 다름 | 서로 다름 |
| Rough Map ID·Timestamp·Key | 자체 세트 | 자체 세트 |
| Button 문구 | 일부 동작과 불일치 | 일부 동작과 불일치 |
| 외부 API 오류 처리 | 없음 | 없음 |

## 64-1. 내 코드의 장점

- `location`과 `location.href`의 역할을 상세히 기록했다.
- 새로고침과 History 이동 차이를 설명했다.
- `window.open()` 인수를 변수로 분리했다.
- Postcode Callback 전체 Data를 확인했다.
- 이미지형 지도와 Rough Map을 모두 삽입했다.
- 강사님 코드보다 학습 주석이 풍부하다.

## 64-2. 내 코드의 개선점

- HTTP URL로 이동한다.
- “뒤로가기” Button이 실제로 두 단계 이동한다.
- Popup Option이 변경되지 않는데 `let`을 사용할 수 있다.
- Popup 차단 여부를 검사하지 않는다.
- Postcode 결과를 Input에 연결하지 않는다.
- Protocol-relative Script URL을 사용한다.
- 지도 이미지가 HTTP라 Mixed Content 가능성이 있다.
- `_blank` Link에 `noopener`가 없다.
- 지도 Image의 `alt`가 부족하다.
- 외부 API Load 실패를 처리하지 않는다.

## 64-3. 강사님 코드의 장점

- Location·History·Popup을 간결하게 실습한다.
- Postcode Callback 구조를 확인할 수 있다.
- 정적 지도와 Script형 지도를 비교할 수 있다.
- 실제 외부 서비스 Embed 흐름을 경험할 수 있다.

## 64-4. 강사님 코드의 보충점

- HTTP·HTTPS 차이를 설명해야 한다.
- Popup 차단과 Same-Origin 처리가 필요하다.
- Postcode 결과를 Form에 연결해야 한다.
- External API 오류 처리와 Fallback이 없다.
- Mixed Content와 새 창 보안을 설명해야 한다.
- Embed Value를 서로 섞지 않아야 한다는 안내가 필요하다.

---

# 65. 기존 코드에서 개선한 이유

## 65-1. HTTPS 이동

기존:

```javascript
location.href = (
    "http://naver.com"
)
```

개선:

```javascript
location.href = (
    "https://www.naver.com"
)
```

## 65-2. History 문구 일치

기존:

```text
Button: 뒤로가기
Code: history.go(-2)
```

개선:

```text
Button: 두 단계 뒤로
Code: history.go(-2)
```

## 65-3. Popup 반환값

기존:

```javascript
window.open(
    url,
    name,
    options,
)
```

개선:

```javascript
const popup = window.open(
    url,
    name,
    options,
)

if (popup === null) {
    // 차단 안내
}
```

## 65-4. Postcode Form 연결

기존:

```javascript
console.log(
    data.address,
)
```

개선:

```javascript
addressInput.value = (
    data.address
)
```

---

# 66. 실무형 예제: 주소 검색 초기화

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

function initPostcode() {
    const button = getRequiredElement(
        "#find-postcode",
    )

    const postcodeInput = (
        getRequiredElement(
            "#postcode",
        )
    )

    const addressInput = (
        getRequiredElement(
            "#address",
        )
    )

    const detailInput = (
        getRequiredElement(
            "#detail-address",
        )
    )

    const errorView = (
        getRequiredElement(
            "#address-error",
        )
    )

    button.addEventListener(
        "click",
        () => {
            const available = (
                typeof window.kakao
                !== "undefined"
                && typeof window
                    .kakao
                    .Postcode
                === "function"
            )

            if (!available) {
                errorView.textContent = (
                    "주소 검색 기능을 "
                    + "불러오지 못했습니다."
                )

                return
            }

            errorView.textContent = ""

            new window.kakao.Postcode({
                oncomplete(
                    data,
                ) {
                    postcodeInput.value = (
                        data.zonecode
                    )

                    addressInput.value = (
                        data.address
                    )

                    detailInput.focus()
                },
            }).open()
        },
    )
}

document.addEventListener(
    "DOMContentLoaded",
    initPostcode,
    {
        once: true,
    },
)
```

## 66-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| 필수 요소 검사 | HTML 누락을 즉시 확인 |
| 외부 API 존재 검사 | Script 실패 시 ReferenceError 방지 |
| Click Event | 사용자 동작 안에서 Popup 실행 |
| `oncomplete` | 주소 선택 완료 후 결과 처리 |
| Input Value | 주소·우편번호 Form 연결 |
| `focus()` | 상세 주소 입력 흐름 연결 |
| 오류 View | Alert에만 의존하지 않는 안내 |
| `once` | 초기화 중복 방지 |

---

# 67. 대표 오류로 이해하기

## 67-1. `kakao is not defined`

외부 Script가 Load되지 않았거나 차단되었을 수 있다.

## 67-2. Popup 반환값이 `null`

Browser가 Popup을 차단했을 수 있다.

## 67-3. Rough Map이 표시되지 않음

Container ID·Timestamp·Key가 서로 일치하는지 확인한다.

## 67-4. HTTPS에서 HTTP 지도 차단

Mixed Content 문제다.

## 67-5. History가 기대한 만큼 이동하지 않음

해당 단계의 Entry가 없을 수 있다.

## 67-6. 주소는 검색되지만 Form에 보이지 않음

Callback에서 Input Value에 연결하지 않았을 수 있다.

---

# 68. 자주 하는 실수

## 68-1. BOM과 DOM을 같은 개념으로 생각

문서 구조와 브라우저 기능의 역할이 다르다.

## 68-2. `location` 객체와 `location.href` 문자열 혼동

전체 객체와 특정 Property다.

## 68-3. `replace()`도 History에 현재 페이지를 남긴다고 생각

현재 Entry를 교체한다.

## 68-4. `history.go(-2)`를 한 단계 뒤로 이해

두 단계 이전이다.

## 68-5. Popup이 항상 열린다고 생각

Browser 정책에 따라 차단될 수 있다.

## 68-6. 새 창 내부를 항상 조작할 수 있다고 생각

Same-Origin Policy의 영향을 받는다.

## 68-7. 외부 Script가 항상 준비되었다고 가정

존재와 Load 실패를 검사한다.

## 68-8. Protocol-relative URL을 무조건 안전하다고 생각

HTTPS를 명시하는 편이 예측 가능하다.

## 68-9. Embed ID·Key를 다른 코드와 섞음

한 Embed에서 제공된 세트를 그대로 사용한다.

## 68-10. 외부 API 실패 UI를 준비하지 않음

주소·지도 기능이 없어도 사용자가 다음 행동을 알 수 있어야 한다.

---

# 69. 핵심 요약

```text
DOM
→ HTML 문서

BOM
→ Browser Window와 기능
```

```text
location.href
→ 현재 URL 읽기·이동

location.reload()
→ 새로고침

location.replace()
→ 현재 History Entry 교체
```

```text
history.back()
→ 한 단계 뒤로

history.forward()
→ 한 단계 앞으로

history.go(number)
→ 지정 단계 이동
```

```text
window.open()
→ 새 Tab·Popup

반환값 null
→ Popup 차단 가능성
```

```text
Kakao Postcode
→ 주소 검색

oncomplete
→ 주소 선택 완료 Callback

Rough Map
→ Script형 지도 Embed
```

---

# 70. 최종 체크리스트

- [ ] BOM과 DOM의 차이를 설명할 수 있는가?
- [ ] `window`가 브라우저 전역 객체임을 이해했는가?
- [ ] `location`과 `location.href`를 구분할 수 있는가?
- [ ] 현재 URL을 읽을 수 있는가?
- [ ] HTTPS URL로 이동할 수 있는가?
- [ ] `assign()`과 `replace()` 차이를 이해했는가?
- [ ] 페이지를 새로고침할 수 있는가?
- [ ] 새로고침 후 상태 초기화를 이해했는가?
- [ ] `back()`, `forward()`, `go()`를 사용할 수 있는가?
- [ ] Button 문구와 실제 이동 단계가 일치하는가?
- [ ] `window.open()`의 세 인수를 설명할 수 있는가?
- [ ] 변경하지 않는 Popup Option에 `const`를 사용하는가?
- [ ] Popup 반환값과 차단 여부를 확인하는가?
- [ ] Same-Origin Policy를 이해했는가?
- [ ] `_blank` Link에 `noopener`를 검토했는가?
- [ ] Postcode API 준비 여부를 검사하는가?
- [ ] `oncomplete` Callback을 이해했는가?
- [ ] 주소와 우편번호를 Input에 연결할 수 있는가?
- [ ] 상세 주소 Input으로 Focus를 이동할 수 있는가?
- [ ] 외부 Script Load 실패를 처리하는가?
- [ ] 이미지형 지도와 Script형 지도를 구분할 수 있는가?
- [ ] Mixed Content 가능성을 확인했는가?
- [ ] 지도 Image에 적절한 `alt`를 제공하는가?
- [ ] Rough Map Container ID·Timestamp·Key를 일치시키는가?
- [ ] 외부 API 실패 시 Fallback을 제공하는가?

---

# 마무리

BOM과 외부 API 사용의 핵심은 페이지를 이동하거나 외부 Script를 붙이는 것에서 끝나지 않는다.

```text
Browser 객체의 역할을 정확히 구분하고
    ↓
History와 Popup의 사용자 경험을 예측하고
    ↓
HTTPS와 새 창 보안을 고려하고
    ↓
외부 API의 준비·성공·실패 상태를 처리하고
    ↓
검색 결과를 실제 Form과 화면에 연결하는 것
```

이 흐름을 이해하면 이후 JSON·AJAX·Fetch 문서에서 외부 데이터와 브라우저 화면을 더 안정적으로 연결할 수 있다.
# V3 실행 추적 카드 — window 기능/사용자 선택 → 외부 API → 콜백 결과

BOM은 `window`, `location`, `history`, `navigator` 등 브라우저 환경을 다룬다. 지도·우편번호 API는 외부 스크립트가 제공한 객체를 호출하고 사용자 선택 결과를 콜백으로 받는다.

팝업 호출 직후에는 주소가 없고 선택 콜백 안에서 값이 생긴다. 외부 스크립트 미로딩, 팝업 차단, 키·도메인 설정 오류를 Console과 Network에서 확인한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/18_map.html`에서 실제 사용 위치와 차이를 확인한다.
