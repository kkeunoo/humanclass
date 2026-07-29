# JavaScript BOM과 지도·우편번호 API

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `18_JavaScript_BOM과_지도우편번호API.md` |
| 분류 | `03_JavaScript` |
| 권장 선수 학습 | `17_JavaScript_폼이벤트와_이벤트전파_실전문제.md` |
| 다음 학습 | 이후 JavaScript 원본 순서에 따라 진행 |
| 원본 기준 | `workspace/workspace_html/javascript/18_map.html`, `workspace_teacher/workspace_html/javascript/18_map.html` |
| 핵심 범위 | `location`, `location.href`, `location.reload()`, `history`, `history.back()`, `history.go()`, `window.open()`, popup option, Kakao postcode API, Kakao rough map embed |
| 프로젝트 연결 | 페이지 이동, 새로고침, 브라우저 기록 이동, 팝업 창, 주소 검색, 매장 지도 표시 |

> 이 문서는 내 코드와 강사님 코드의 `18_map.html`을 직접 비교해 작성했습니다. 두 파일은 Browser Object Model의 `location`, `history`, `window.open()`과 Kakao 우편번호·지도 삽입 기능을 동일한 흐름으로 실습합니다. 내 코드는 설명 주석이 더 많고 버튼 문구와 지도 embed 값 일부가 다릅니다. 두 원본 모두 `http://naver.com` 이동, `history.go(-2)`, popup 차단 가능성, 외부 API·외부 script 의존성, mixed content 가능성이 있는 지도 이미지 URL, 새 창 보안 속성 누락, 문서 언어와 title 부정확성 등을 그대로 보존하고 개선 방향을 별도로 설명합니다.

---

# 학습 목표

- BOM과 DOM의 차이를 설명한다.
- `window`, `location`, `history` 객체의 역할을 이해한다.
- `location.href`를 읽고 변경하는 방법을 이해한다.
- `location.reload()`로 현재 페이지를 새로고침한다.
- `history.back()`과 `history.go()`의 차이를 이해한다.
- `window.open()`의 URL, name, option 인수를 설명한다.
- popup이 browser 정책에 의해 차단될 수 있음을 이해한다.
- Kakao 우편번호 API의 callback 구조를 이해한다.
- 우편번호 검색 결과에서 주소와 우편번호를 읽는다.
- Kakao rough map의 이미지형 지도와 script형 지도를 구분한다.
- 외부 script·외부 이미지 의존성과 보안 문제를 설명한다.
- 내 코드와 강사님 코드의 실제 차이를 정확히 기록한다.

---

# Core Concepts

## 1. BOM이란?

BOM은 Browser Object Model의 약자입니다.

브라우저 환경에서 다음과 같은 기능을 다룹니다.

```text
window
location
history
navigator
screen
```

DOM이 HTML 문서의 요소를 다룬다면 BOM은 browser window와 browser가 제공하는 기능을 다룹니다.

---

## 2. Window Object

browser JavaScript의 전역 객체는 일반적으로 `window`입니다.

다음 두 표현은 browser 환경에서 같은 객체를 가리킵니다.

```js
window.location
location
```

```js
window.history
history
```

원본은 `window.`를 생략한 `location`과 `history`를 사용합니다.

---

## 3. Load 이후 Event 등록

양쪽 원본:

```js
window.onload =
  () => {
    // button event 등록
  }
```

body의 button이 모두 load된 뒤 selector와 event listener를 실행합니다.

내 코드:

```js
window.onload = ()=> {
```

강사님 코드:

```js
window.onload = ()=>{
```

spacing 차이만 있습니다.

---

## 4. Button 1: Location 객체 출력

양쪽 원본:

```js
document
  .querySelector(
    "#btn1"
  )
  .addEventListener(
    "click",
    () => {
      console.log(
        location
      )

      console.log(
        location.href
      )
    }
  )
```

`location`은 현재 문서 URL 정보를 담고 있는 객체입니다.

`location.href`는 현재 전체 URL 문자열입니다.

---

## 5. Location.href 읽기

```js
console.log(
  location.href
)
```

현재 페이지의 전체 주소를 확인합니다.

예:

```text
http://127.0.0.1:5500/javascript/18_map.html
```

실제 출력값은 실행 환경에 따라 달라집니다.

---

## 6. Location.href 변경

양쪽 원본:

```js
location.href =
  "http://naver.com"
```

이 값을 바꾸면 browser가 해당 URL로 이동합니다.

내 주석:

```text
읽어 온 주소의 값을 바꿀 수도 있음
```

정확한 설명:

```text
location.href property에 새 URL을 대입하면 현재 문서가 그 URL로 이동한다.
```

---

## 7. HTTP URL 문제

원본은:

```js
"http://naver.com"
```

을 사용합니다.

현대 웹에서는 HTTPS를 사용하는 것이 적절합니다.

개선:

```js
location.href =
  "https://www.naver.com"
```

HTTP URL은 HTTPS 페이지에서 mixed content나 redirect 문제를 일으킬 수 있습니다.

---

## 8. Assign과 Replace

`location.href` 대입과 비슷한 API:

```js
location.assign(
  "https://example.com"
)
```

현재 history에 이동 전 페이지를 남깁니다.

```js
location.replace(
  "https://example.com"
)
```

현재 history entry를 교체하므로 뒤로 가기로 이전 페이지에 돌아가기 어려워집니다.

원본에는 없는 확장 개념입니다.

---

## 9. Button 2: Reload

양쪽 원본:

```js
document
  .querySelector(
    "#btn2"
  )
  .addEventListener(
    "click",
    () => {
      location.reload()
    }
  )
```

현재 페이지를 다시 불러옵니다.

---

## 10. Reload 주의점

새로고침하면:

- 현재 JavaScript 변수 상태 초기화
- DOM 상태 재생성
- 저장하지 않은 입력값 유실 가능
- 외부 resource 다시 요청 가능

browser cache 동작은 환경과 요청 정책에 따라 다를 수 있습니다.

---

## 11. Button 3: History 객체

양쪽 원본:

```js
console.log(
  history
)
```

`history`는 현재 tab의 session history를 다루는 객체입니다.

보안상 방문한 URL 목록 전체를 JavaScript가 직접 읽을 수는 없습니다.

주로 앞뒤 이동과 state 관리 API를 제공합니다.

---

## 12. History.back()

양쪽 원본에 주석 처리:

```js
// history.back()
```

현재 history에서 한 단계 뒤로 이동합니다.

개념적으로 다음과 같습니다.

```js
history.go(-1)
```

---

## 13. History.go(-2)

실제 실행 코드:

```js
history.go(-2)
```

현재 위치에서 history 두 단계 이전으로 이동하려고 시도합니다.

주의:

- 이전 entry가 두 개보다 적으면 이동하지 않을 수 있음
- 새 tab에서 직접 페이지를 연 경우 눈에 띄는 동작이 없을 수 있음
- 같은 origin이 아니어도 browser history 이동은 가능하지만 URL 목록을 읽을 수는 없음

---

## 14. 버튼 문구와 실제 동작 불일치

button text:

```html
<button
  type="button"
  id="btn3"
>
  뒤로가기
</button>
```

하지만 실제 코드는:

```js
history.go(-2)
```

한 단계가 아니라 두 단계 뒤로 갑니다.

button 문구를 그대로 유지하려면:

```js
history.back()
```

또는:

```js
history.go(-1)
```

이 더 자연스럽습니다.

---

## 15. Forward

앞으로 이동:

```js
history.forward()
```

또는:

```js
history.go(1)
```

원본에는 없는 확장 내용입니다.

---

## 16. Button 4: Window.open()

양쪽 원본:

```js
const url =
  "17_event_form.html"

const name =
  "open 연습"

let option =
  "width=800,height=600"

window.open(
  url,
  name,
  option
)
```

새 browsing context를 엽니다.

---

## 17. Window.open 인수

```js
window.open(
  url,
  name,
  option
)
```

각 인수:

```text
url
→ 열 문서 주소

name
→ 새 창 또는 tab의 이름

option
→ 창 크기와 기능 옵션 문자열
```

---

## 18. Popup Name

원본:

```js
const name =
  "open 연습"
```

name이 동일하면 browser가 기존 popup을 재사용할 수 있습니다.

공백이 포함된 이름은 환경에 따라 창 이름 처리 방식이 다를 수 있으므로 실무에서는 간단한 식별자를 권장합니다.

```js
const name =
  "eventFormPopup"
```

---

## 19. Popup Option

원본:

```js
let option =
  "width=800,height=600"
```

창의 폭과 높이를 요청합니다.

`option`은 변경하지 않으므로:

```js
const option =
  "width=800,height=600"
```

이 더 적절합니다.

---

## 20. Popup 차단

`window.open()`은 사용자 click event 안에서 실행되고 있어 popup 허용 가능성이 높습니다.

하지만 browser 설정이나 정책에 따라 차단될 수 있습니다.

반환값 검사:

```js
const popup =
  window.open(
    url,
    name,
    option
  )

if (popup === null) {
  alert(
    "팝업이 차단되었습니다."
  )
}
```

---

## 21. Popup과 보안

내 주석:

```text
iframe처럼 보안에 좋지 않음
부모가 뭐 하는지 다 알 수 있음
```

이 설명은 지나치게 단순화되어 있습니다.

보다 정확한 설명:

- 같은 origin의 popup과 opener는 서로 접근할 수 있음
- 다른 origin이면 Same-Origin Policy가 접근을 제한함
- 새 창에서 `window.opener`를 악용하는 reverse tabnabbing 위험을 고려할 수 있음
- 외부 링크는 `noopener` 사용을 검토해야 함

`window.open()` 자체가 무조건 보안에 나쁜 것은 아닙니다.

---

## 22. Popup URL 상대 경로

원본:

```js
const url =
  "17_event_form.html"
```

현재 `18_map.html`과 같은 directory에 `17_event_form.html`이 있다는 전제입니다.

파일 구조가 달라지면 열리지 않습니다.

---

## 23. Button 5: Kakao Postcode

양쪽 원본:

```js
new kakao.Postcode({
  oncomplete:
    function(data) {
      console.log(data)
      console.log(
        data.address
      )
      console.log(
        data.zonecode
      )
    }
}).open()
```

`kakao.Postcode` instance를 생성하고 `.open()`으로 주소 검색 UI를 엽니다.

---

## 24. Oncomplete Callback

```js
oncomplete:
  function(data) {
  }
```

사용자가 주소를 선택하면 실행됩니다.

`data` 객체에는 선택한 주소와 우편번호 등 여러 정보가 들어 있습니다.

원본이 사용하는 값:

```js
data.address
data.zonecode
```

---

## 25. Address와 Zonecode

```js
data.address
```

선택된 기본 주소 문자열입니다.

```js
data.zonecode
```

우편번호입니다.

실무에서는 input에 넣을 수 있습니다.

```js
postcode.value =
  data.zonecode

address.value =
  data.address
```

---

## 26. External Script 순서

우편번호 script:

```html
<script
  src="//t1.kakaocdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"
></script>
```

body 마지막에 있습니다.

button click은 page load 이후 발생하므로 일반적인 상황에서는 script가 먼저 실행되어 `kakao.Postcode`가 준비됩니다.

그러나 network 실패 시:

```text
kakao is not defined
```

오류가 발생할 수 있습니다.

---

## 27. Protocol-relative URL

원본:

```html
src="//t1.kakaocdn.net/..."
```

현재 페이지 protocol을 따라갑니다.

현대 문서에서는 명시적인 HTTPS가 더 명확합니다.

```html
src="https://t1.kakaocdn.net/..."
```

---

## 28. Kakao Rough Map 두 종류

양쪽 원본에는 지도 표시가 두 번 등장합니다.

첫 번째:

```text
이미지형 rough map
```

두 번째:

```text
loader script와 Lander를 이용한 일반 rough map
```

내 주석:

```text
카카오맵 이미지로 따오기
```

강사님 주석:

```text
이미지 지도
```

두 표현은 같은 첫 번째 지도 block을 가리킵니다.

---

## 29. 이미지형 지도

첫 지도는 `<img>`를 link 안에 넣은 형태입니다.

```html
<a
  href="Kakao Map URL"
  target="_blank"
>
  <img
    class="map"
    src="http://t1.daumcdn.net/roughmap/imgmap/..."
  >
</a>
```

클릭하면 Kakao Map 상세 페이지로 이동합니다.

---

## 30. 이미지 Src 차이

내 코드 image hash:

```text
eeddbb219e74a4dfec39648ae01a6274324e280c572c8cfc096e75fd5a80d119
```

강사님 코드 image hash:

```text
6926607f9a770263599ba57565d83db12ce90ef77393bb767376c35f9e2f5724
```

둘 다 같은 장소 관련 rough map이지만 생성 시점이나 embed 결과가 달라 image URL이 다릅니다.

---

## 31. Mixed Content 가능성

첫 지도 image URL:

```html
src="http://t1.daumcdn.net/..."
```

페이지가 HTTPS로 제공되면 HTTP image가 차단될 수 있습니다.

HTTPS URL을 사용하는 것이 안전합니다.

---

## 32. Target Blank 보안 속성

원본 link:

```html
target="_blank"
```

외부 페이지를 새 tab에서 엽니다.

개선:

```html
target="_blank"
rel="noopener noreferrer"
```

`noopener`는 새 페이지가 `window.opener`를 통해 원본 window에 접근하는 위험을 줄입니다.

---

## 33. 일반 Rough Map Node

내 코드:

```html
<div
  id="daumRoughmapContainer1784611174105"
  class="root_daum_roughmap root_daum_roughmap_landing"
></div>
```

강사님 코드:

```html
<div
  id="daumRoughmapContainer1784611170515"
  class="root_daum_roughmap root_daum_roughmap_landing"
></div>
```

ID의 timestamp 숫자가 다릅니다.

실행 script의 timestamp와 container id는 서로 맞아야 합니다.

---

## 34. Roughmap Loader

공통 script:

```html
<script
  charset="UTF-8"
  class="daum_roughmap_loader_script"
  src="https://ssl.daumcdn.net/dmaps/map_js_init/roughmapLoader.js"
></script>
```

Kakao rough map renderer를 불러옵니다.

주석에도 지도 embed가 여러 개일 때 loader script는 한 번만 삽입한다고 적혀 있습니다.

---

## 35. Lander 실행

내 코드:

```js
new daum
  .roughmap
  .Lander({
    timestamp:
      "1784611174105",
    key:
      "r85qmeux7up",
    mapWidth:
      "640",
    mapHeight:
      "360"
  })
  .render()
```

강사님 코드:

```js
new daum
  .roughmap
  .Lander({
    timestamp:
      "1784611170515",
    key:
      "rkqpeyht8az",
    mapWidth:
      "640",
    mapHeight:
      "360"
  })
  .render()
```

timestamp와 key가 다릅니다.

이 값은 각 embed 코드에 맞게 함께 사용해야 합니다.

---

## 36. 지도 위치

두 rough map URL의 장소 이름:

```text
달식당
```

좌표 관련 parameter:

```text
urlX = 532829.9999999995
urlY = 919102.9999999993
```

두 원본 모두 같은 장소와 좌표를 사용합니다.

---

# Syntax / Comparison

## 37. BOM API 비교

| 기능 | API | 설명 |
| --- | --- | --- |
| 현재 URL 읽기 | `location.href` | 현재 전체 주소 |
| 페이지 이동 | `location.href = url` | 새 URL로 이동 |
| 새로고침 | `location.reload()` | 현재 페이지 다시 load |
| 한 단계 뒤로 | `history.back()` | 이전 history entry |
| 여러 단계 이동 | `history.go(n)` | 음수는 뒤, 양수는 앞 |
| 새 창 | `window.open()` | 새 tab 또는 popup 열기 |
| 새 창 닫기 | `popup.close()` | 열린 창 참조로 닫기 |

---

## 38. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기능 흐름 | 동일 | 동일 |
| 설명 주석 | 많음 | 간결 |
| 우편번호 button 문구 | `우편번호찾기` | `우편번호 찾기` |
| 첫 지도 주석 | `카카오맵 이미지로 따오기` | `이미지 지도` |
| 두 번째 지도 주석 | Kakao 공식 주석 | `일반 지도` 추가 |
| 첫 지도 image hash | 내 embed 값 | 강사님 embed 값 |
| Rough map container ID | `...1174105` | `...1170515` |
| Rough map timestamp | `1784611174105` | `1784611170515` |
| Rough map key | `r85qmeux7up` | `rkqpeyht8az` |
| Window.open 설명 | 보안 관련 주석 추가 | 설명 없음 |
| 코드 spacing | 비교적 넓음 | 더 조밀함 |
| 실제 API 기능 | 동일 | 동일 |

---

# Representative Examples

## 39. 안전한 페이지 이동

```js
const moveButton =
  document.querySelector(
    "#moveButton"
  )

moveButton.addEventListener(
  "click",
  function() {
    const confirmed =
      confirm(
        "네이버로 이동할까요?"
      )

    if (!confirmed) {
      return
    }

    location.assign(
      "https://www.naver.com"
    )
  }
)
```

---

## 40. History 이동

```js
const backButton =
  document.querySelector(
    "#backButton"
  )

backButton.addEventListener(
  "click",
  function() {
    if (
      history.length > 1
    ) {
      history.back()
    } else {
      location.href =
        "./index.html"
    }
  }
)
```

`history.length`는 현재 session history의 대략적인 entry 수를 나타내지만 어떤 URL인지 확인할 수는 없습니다.

---

## 41. Popup 차단 검사

```js
const popupButton =
  document.querySelector(
    "#popupButton"
  )

popupButton.addEventListener(
  "click",
  function() {
    const popup =
      window.open(
        "./17_event_form.html",
        "eventFormPopup",
        "width=800,height=600"
      )

    if (popup === null) {
      alert(
        "팝업 차단을 해제해 주세요."
      )

      return
    }

    popup.focus()
  }
)
```

---

# Practical Usage

## 42. 우편번호 Form 연결

HTML:

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
  id="findPostcode"
>
  우편번호 찾기
</button>

<label for="address">
  주소
</label>

<input
  type="text"
  id="address"
  readonly
>

<label for="detailAddress">
  상세 주소
</label>

<input
  type="text"
  id="detailAddress"
>
```

JavaScript:

```js
const findButton =
  document.querySelector(
    "#findPostcode"
  )

findButton.addEventListener(
  "click",
  function() {
    if (
      typeof kakao ===
      "undefined"
    ) {
      alert(
        "주소 검색 기능을 불러오지 못했습니다."
      )

      return
    }

    new kakao.Postcode({
      oncomplete:
        function(data) {
          postcode.value =
            data.zonecode

          address.value =
            data.address

          detailAddress.focus()
        }
    }).open()
  }
)
```

---

## 43. External API 오류 처리

```js
const postcodeReady =
  typeof window.kakao !==
    "undefined" &&
  typeof window
    .kakao
    .Postcode ===
    "function"
```

API script가 load되지 않았을 때 user에게 안내할 수 있습니다.

---

## 44. Script Load Event

```js
const script =
  document.createElement(
    "script"
  )

script.src =
  "https://example.com/api.js"

script.addEventListener(
  "load",
  function() {
    console.log(
      "API 준비 완료"
    )
  }
)

script.addEventListener(
  "error",
  function() {
    console.error(
      "API를 불러오지 못했습니다."
    )
  }
)

document.head.append(
  script
)
```

외부 API는 성공과 실패를 모두 고려해야 합니다.

---

# My Code Analysis

## 45. 내 코드 장점

- `location`이 현재 주소 관련 객체라는 설명을 추가했다.
- `location.href`를 읽고 변경할 수 있다는 점을 주석으로 기록했다.
- `location.reload()`의 역할을 설명했다.
- `history.back()`과 `history.go(-2)`의 차이를 확인할 수 있다.
- `window.open()`의 URL, name, option을 변수로 분리했다.
- popup 창과 option에 관한 설명을 추가했다.
- Kakao postcode callback에서 전체 data, address, zonecode를 각각 출력한다.
- 이미지형 지도와 일반 rough map을 모두 삽입했다.
- 강사님 코드보다 학습용 주석이 풍부하다.

---

## 46. 내 코드 개선점

- `location.href`에 HTTP URL을 사용한다.
- button은 “뒤로가기”인데 두 단계 이전으로 이동한다.
- `window.open()` 보안 설명이 지나치게 단순화되어 있다.
- popup option은 변경하지 않으므로 `let`보다 `const`가 적절하다.
- popup 차단 여부를 확인하지 않는다.
- 외부 API load 실패를 처리하지 않는다.
- postcode 결과를 form input에 연결하지 않고 Console에만 출력한다.
- protocol-relative script URL을 사용한다.
- 첫 지도 image가 HTTP라 mixed content 문제가 생길 수 있다.
- `target="_blank"` link에 `rel="noopener noreferrer"`가 없다.
- 첫 지도 image에 장소를 설명하는 `alt`가 없다.
- inline style이 매우 길어 유지보수가 어렵다.
- 외부 embed key와 timestamp에 의존한다.
- `lang="en"`과 `<title>Document</title>`이 내용에 맞지 않는다.

---

# Teacher Code Analysis

## 47. 강사님 코드 장점

- BOM의 핵심 기능을 짧은 button 예제로 보여 준다.
- URL 읽기, 이동, 새로고침을 쉽게 확인할 수 있다.
- history 객체와 다단계 뒤로가기를 보여 준다.
- popup 창 크기 option을 사용한다.
- Kakao postcode callback 구조를 보여 준다.
- image map과 script map 두 방식을 모두 포함한다.
- 코드가 간결해 전체 실행 흐름을 빠르게 파악할 수 있다.

---

## 48. 강사님 코드 개선점

- 각 BOM 객체에 대한 설명이 거의 없다.
- HTTP 이동 URL을 사용한다.
- button 문구와 history.go(-2) 동작이 다르다.
- popup 차단·보안 설명이 없다.
- `option`에 `let`을 사용한다.
- 외부 API 실패 처리가 없다.
- postcode 결과를 화면에 연결하지 않는다.
- protocol-relative postcode script를 사용한다.
- HTTP map image를 사용한다.
- 새 tab link에 noopener가 없다.
- image에 의미 있는 alt가 부족하다.
- inline style과 embed code가 길다.
- `lang="en"`과 title이 내용에 맞지 않는다.

---

# Improvements

## 49. 개선된 전체 초기화

```js
window.addEventListener(
  "DOMContentLoaded",
  function() {
    const moveButton =
      document.querySelector(
        "#btn1"
      )

    const reloadButton =
      document.querySelector(
        "#btn2"
      )

    const backButton =
      document.querySelector(
        "#btn3"
      )

    const openButton =
      document.querySelector(
        "#btn4"
      )

    const postcodeButton =
      document.querySelector(
        "#btn5"
      )

    moveButton.addEventListener(
      "click",
      function() {
        location.assign(
          "https://www.naver.com"
        )
      }
    )

    reloadButton.addEventListener(
      "click",
      function() {
        location.reload()
      }
    )

    backButton.addEventListener(
      "click",
      function() {
        history.back()
      }
    )

    openButton.addEventListener(
      "click",
      function() {
        const popup =
          window.open(
            "./17_event_form.html",
            "eventFormPopup",
            "width=800,height=600"
          )

        if (popup === null) {
          alert(
            "팝업이 차단되었습니다."
          )
        }
      }
    )

    postcodeButton
      .addEventListener(
        "click",
        openPostcode
      )
  }
)
```

---

# Common Mistakes

## 50. 자주 하는 실수

### 50.1 Location 객체와 URL 문자열을 같다고 생각

`location`은 객체이고 `location.href`가 전체 URL 문자열입니다.

### 50.2 Reload 후 변수 상태가 유지된다고 생각

페이지가 다시 load되므로 JavaScript 실행 상태가 초기화됩니다.

### 50.3 뒤로가기 Button에 Go(-2) 사용

사용자 기대와 실제 이동 단계가 다릅니다.

### 50.4 History URL 목록을 읽을 수 있다고 생각

보안상 전체 방문 URL을 직접 열람할 수 없습니다.

### 50.5 Window.open은 항상 성공한다고 생각

browser popup 정책에 의해 null을 반환할 수 있습니다.

### 50.6 Popup은 무조건 위험하다고 설명

origin과 opener 관계에 따라 접근 가능 범위가 달라집니다.

### 50.7 External API가 항상 준비되어 있다고 생각

network 오류나 script 차단으로 전역 객체가 없을 수 있습니다.

### 50.8 HTTP Resource를 HTTPS 문서에서 사용

mixed content로 차단될 수 있습니다.

### 50.9 Target Blank에 Noopener 누락

새 페이지가 opener에 접근할 위험을 줄여야 합니다.

### 50.10 Rough Map Timestamp와 Container ID를 다르게 사용

embed renderer가 target container를 찾지 못할 수 있습니다.

---

# Interview / Review

## 51. 면접·복습 포인트

### Q1. BOM과 DOM의 차이는 무엇인가요?

DOM은 HTML 문서 구조를 다루고 BOM은 browser window와 URL, history 같은 browser 기능을 다룹니다.

### Q2. Location.href를 변경하면 어떻게 되나요?

현재 문서가 지정한 URL로 이동합니다.

### Q3. History.back과 History.go(-1)은 같은가요?

개념적으로 한 단계 이전 history로 이동한다는 점에서 같습니다.

### Q4. History.go(-2)는 무엇을 의미하나요?

현재 위치에서 두 단계 이전 session history entry로 이동을 시도합니다.

### Q5. Window.open의 반환값은 무엇인가요?

열린 window 참조를 반환하며 popup이 차단되면 null일 수 있습니다.

### Q6. Window.open의 Name을 재사용하면 어떻게 되나요?

같은 이름의 browsing context가 있으면 새 창 대신 기존 창을 재사용할 수 있습니다.

### Q7. Kakao Postcode의 Oncomplete는 언제 실행되나요?

사용자가 검색 결과에서 주소를 선택해 검색이 완료될 때 실행됩니다.

### Q8. Data.address와 Data.zonecode는 무엇인가요?

각각 선택된 기본 주소와 우편번호입니다.

### Q9. Protocol-relative URL보다 HTTPS를 권장하는 이유는 무엇인가요?

protocol을 명시해 보안과 동작을 예측하기 쉽고 HTTPS 환경의 mixed content 문제를 줄일 수 있습니다.

### Q10. Rough Map의 Container ID와 Timestamp가 맞아야 하는 이유는 무엇인가요?

renderer가 지정된 embed instance와 대상 container를 연결해야 하기 때문입니다.

---

# Problems

## 문제 1. 현재 URL

현재 페이지 전체 URL을 Console에 출력하세요.

## 문제 2. HTTPS 이동

button click 시 `https://www.naver.com`으로 이동하세요.

## 문제 3. Reload

button click 시 현재 페이지를 새로고침하세요.

## 문제 4. 한 단계 뒤로

button click 시 한 단계 이전 페이지로 이동하세요.

## 문제 5. 두 단계 뒤로

`history.go()`로 두 단계 이전으로 이동하세요.

## 문제 6. 앞으로 이동

button click 시 한 단계 앞으로 이동하세요.

## 문제 7. Popup 열기

폭 800px, 높이 600px의 popup으로 `17_event_form.html`을 여세요.

## 문제 8. Popup 차단 검사

window.open 반환값이 null이면 안내 문구를 표시하세요.

## 문제 9. Popup Option 상수

변경하지 않는 option 변수를 적절한 선언 방식으로 작성하세요.

## 문제 10. Replace 이동

현재 history entry를 교체하며 다른 URL로 이동하세요.

## 문제 11. Postcode 생성

Kakao Postcode instance를 만들고 `.open()`을 호출하세요.

## 문제 12. 주소 출력

oncomplete에서 address를 Console에 출력하세요.

## 문제 13. 우편번호 출력

oncomplete에서 zonecode를 Console에 출력하세요.

## 문제 14. Form 연결

address와 zonecode를 각각 input value에 넣으세요.

## 문제 15. API 존재 검사

`kakao.Postcode`를 사용할 수 있는지 검사하세요.

## 문제 16. Script 오류 처리

외부 script load 실패 시 오류 문구를 출력하세요.

## 문제 17. Noopener

새 tab link에 필요한 보안 속성을 추가하세요.

## 문제 18. Mixed Content 수정

HTTP image URL을 HTTPS로 수정하세요.

## 문제 19. Button 동작 일치

“뒤로가기” button이 실제로 한 단계만 이동하게 수정하세요.

## 문제 20. DOMContentLoaded

window.onload 대신 DOMContentLoaded로 초기화하세요.

## 문제 21. 원본 차이

내 코드와 강사님 코드의 rough map timestamp, key, container id 차이를 설명하세요.

## 문제 22. 종합 주소 검색 UI

다음 요구사항을 만족하세요.

- 우편번호 찾기 button
- 우편번호 input
- 주소 input
- 상세 주소 input
- API load 여부 확인
- 주소 선택 시 우편번호와 주소 자동 입력
- 상세 주소로 focus 이동
- 외부 API가 없으면 사용자 안내
- 모든 input에 label 연결
- button은 form을 submit하지 않음

---

# Answers

## 정답 1

```js
console.log(
  location.href
)
```

## 정답 2

```js
button.addEventListener(
  "click",
  function() {
    location.href =
      "https://www.naver.com"
  }
)
```

## 정답 3

```js
button.addEventListener(
  "click",
  function() {
    location.reload()
  }
)
```

## 정답 4

```js
history.back()
```

또는:

```js
history.go(-1)
```

## 정답 5

```js
history.go(-2)
```

## 정답 6

```js
history.forward()
```

또는:

```js
history.go(1)
```

## 정답 7

```js
window.open(
  "17_event_form.html",
  "eventFormPopup",
  "width=800,height=600"
)
```

## 정답 8

```js
const popup =
  window.open(
    "17_event_form.html",
    "eventFormPopup",
    "width=800,height=600"
  )

if (popup === null) {
  alert(
    "팝업이 차단되었습니다."
  )
}
```

## 정답 9

```js
const option =
  "width=800,height=600"
```

## 정답 10

```js
location.replace(
  "https://example.com"
)
```

## 정답 11

```js
new kakao.Postcode({
  oncomplete:
    function(data) {
      console.log(data)
    }
}).open()
```

## 정답 12

```js
oncomplete:
  function(data) {
    console.log(
      data.address
    )
  }
```

## 정답 13

```js
oncomplete:
  function(data) {
    console.log(
      data.zonecode
    )
  }
```

## 정답 14

```js
oncomplete:
  function(data) {
    postcode.value =
      data.zonecode

    address.value =
      data.address
  }
```

## 정답 15

```js
const available =
  typeof window.kakao !==
    "undefined" &&
  typeof window
    .kakao
    .Postcode ===
    "function"
```

## 정답 16

```js
script.addEventListener(
  "error",
  function() {
    console.error(
      "외부 API를 불러오지 못했습니다."
    )
  }
)
```

## 정답 17

```html
<a
  href="https://map.kakao.com"
  target="_blank"
  rel="noopener noreferrer"
>
  카카오맵
</a>
```

## 정답 18

```html
<img
  src="https://t1.daumcdn.net/roughmap/imgmap/..."
  alt="달식당 위치 지도"
>
```

## 정답 19

```js
history.back()
```

## 정답 20

```js
document.addEventListener(
  "DOMContentLoaded",
  function() {
    // event 등록
  }
)
```

## 정답 21

내 코드와 강사님 코드는 rough map을 각각 별도로 embed해 container id, timestamp, key가 다릅니다. 각 파일 안에서는 세 값이 해당 embed 코드와 맞게 사용되므로 서로 섞으면 안 됩니다.

## 정답 22

HTML:

```html
<form>
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
    id="findPostcode"
  >
    우편번호 찾기
  </button>

  <label for="address">
    주소
  </label>

  <input
    type="text"
    id="address"
    readonly
  >

  <label for="detailAddress">
    상세 주소
  </label>

  <input
    type="text"
    id="detailAddress"
  >
</form>
```

JavaScript:

```js
document.addEventListener(
  "DOMContentLoaded",
  function() {
    const findButton =
      document.querySelector(
        "#findPostcode"
      )

    const postcode =
      document.querySelector(
        "#postcode"
      )

    const address =
      document.querySelector(
        "#address"
      )

    const detailAddress =
      document.querySelector(
        "#detailAddress"
      )

    findButton.addEventListener(
      "click",
      function() {
        const available =
          typeof window.kakao !==
            "undefined" &&
          typeof window
            .kakao
            .Postcode ===
            "function"

        if (!available) {
          alert(
            "주소 검색 기능을 불러오지 못했습니다."
          )

          return
        }

        new kakao.Postcode({
          oncomplete:
            function(data) {
              postcode.value =
                data.zonecode

              address.value =
                data.address

              detailAddress.focus()
            }
        }).open()
      }
    )
  }
)
```

---

# Final Checklist

## Location

- [ ] location 객체와 href 문자열을 구분했다.
- [ ] 현재 URL을 읽을 수 있다.
- [ ] href 변경으로 페이지를 이동했다.
- [ ] HTTP 대신 HTTPS 사용을 검토했다.
- [ ] assign과 replace 차이를 이해했다.
- [ ] reload 후 상태가 초기화됨을 이해했다.

## History

- [ ] history 객체의 역할을 이해했다.
- [ ] back과 go(-1)을 비교했다.
- [ ] go(-2)가 두 단계 이동임을 이해했다.
- [ ] button 문구와 실제 동작이 일치하는지 확인했다.
- [ ] forward와 go(1)을 이해했다.
- [ ] history URL 목록을 직접 읽을 수 없음을 이해했다.

## Window.open

- [ ] URL, name, option 인수를 이해했다.
- [ ] 변경하지 않는 option에 const를 사용했다.
- [ ] popup 반환값을 확인했다.
- [ ] popup 차단을 처리했다.
- [ ] same-origin과 opener 보안을 이해했다.
- [ ] 상대 경로가 실제 파일 구조와 맞는지 확인했다.

## Kakao API

- [ ] postcode script가 준비됐는지 확인했다.
- [ ] oncomplete callback을 이해했다.
- [ ] address와 zonecode를 읽었다.
- [ ] 결과를 input에 연결했다.
- [ ] 상세 주소 input으로 focus를 이동했다.
- [ ] external API 실패를 처리했다.
- [ ] protocol-relative URL을 HTTPS로 바꾸는 것을 검토했다.

## Map Embed

- [ ] 이미지형 지도와 script형 지도를 구분했다.
- [ ] external image URL의 mixed content 가능성을 확인했다.
- [ ] target blank에 noopener를 검토했다.
- [ ] image alt를 제공했다.
- [ ] roughmap loader를 중복 삽입하지 않았다.
- [ ] container id와 timestamp를 일치시켰다.
- [ ] embed key를 다른 파일 값과 섞지 않았다.

## 원본 검수

- [ ] 두 실제 18_map.html만 비교했다.
- [ ] 내 설명 주석과 강사님 간결한 코드를 기록했다.
- [ ] 우편번호 button spacing 차이를 기록했다.
- [ ] 첫 지도 image hash 차이를 기록했다.
- [ ] rough map container id 차이를 기록했다.
- [ ] timestamp와 key 차이를 기록했다.
- [ ] history button 문구와 go(-2) 불일치를 기록했다.
- [ ] HTTP URL과 mixed content 가능성을 기록했다.
- [ ] popup 보안 설명의 과도한 단순화를 기록했다.
- [ ] 외부 API 실패 처리 누락을 기록했다.
- [ ] BACKUP을 분석하지 않았다.

---

# Key Summary

- JavaScript 18번은 Browser Object Model과 외부 지도·주소 API를 다룬다.
- `location`은 현재 문서 URL 정보를 담는 객체다.
- `location.href`를 읽으면 현재 전체 URL을 얻을 수 있다.
- `location.href`에 새 URL을 대입하면 그 페이지로 이동한다.
- 원본은 `http://naver.com`을 사용하지만 HTTPS URL이 더 적절하다.
- `location.reload()`는 현재 페이지를 다시 load한다.
- 새로고침 후 JavaScript 변수와 DOM 상태는 다시 초기화된다.
- `history.back()`은 한 단계 뒤로 이동한다.
- `history.go(-2)`는 두 단계 뒤로 이동한다.
- 원본 button은 “뒤로가기”라고 쓰여 있지만 실제 코드는 두 단계 이전으로 이동한다.
- `window.open()`은 URL, 창 이름, option 문자열을 받는다.
- popup은 browser 정책에 의해 차단될 수 있으므로 반환값을 확인해야 한다.
- 같은 name을 사용하면 기존 popup이 재사용될 수 있다.
- popup과 opener 접근 가능 범위는 Same-Origin Policy의 영향을 받는다.
- `window.open()` 자체를 무조건 보안에 나쁘다고 설명하는 것은 부정확하다.
- Kakao Postcode는 `new kakao.Postcode({...}).open()`으로 실행한다.
- 주소를 선택하면 oncomplete callback의 data 객체를 받는다.
- `data.address`는 기본 주소이고 `data.zonecode`는 우편번호다.
- 원본은 결과를 Console에만 출력하고 실제 input에는 연결하지 않는다.
- 외부 postcode script가 load되지 않으면 `kakao` 관련 오류가 발생할 수 있다.
- 원본의 protocol-relative URL은 명시적 HTTPS로 작성하는 편이 좋다.
- 첫 번째 Kakao map은 image와 link로 구성된 이미지형 지도다.
- 두 번째 지도는 roughmap loader와 `daum.roughmap.Lander`로 렌더링한다.
- 내 코드와 강사님 코드는 첫 지도 image hash가 다르다.
- 두 파일의 rough map container id, timestamp, key도 각각 다르다.
- embed 값은 각 파일 내부에서 서로 맞게 사용해야 하며 다른 파일 값과 섞으면 안 된다.
- 첫 지도 image가 HTTP이므로 HTTPS 페이지에서 mixed content가 발생할 수 있다.
- `target="_blank"` link에는 `rel="noopener noreferrer"`를 검토해야 한다.
- 외부 지도와 API는 network, script 차단, 서비스 변경에 영향을 받는다.
