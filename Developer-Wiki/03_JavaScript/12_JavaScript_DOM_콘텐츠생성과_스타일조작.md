---
title: JavaScript DOM 콘텐츠 생성과 스타일 조작
version: v4.0-detailed-source
last_updated: 2026-09-17
status: Completed
---

# JavaScript DOM 콘텐츠 생성과 스타일 조작

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `12_JavaScript_DOM_콘텐츠생성과_스타일조작.md` |
| 분류 | `03_JavaScript` |
| 원본 기준 | `workspace_html/javascript/12_dom_content.html`, `workspace_teacher/workspace_html/javascript/12_dom_content.html` |
| 핵심 범위 | `textContent`, `innerText`, `innerHTML`, `createElement()`, `append()`, `appendChild()`, `prepend()`, `before()`, `after()`, 인라인 스타일, `getComputedStyle()` |
| 실습 범위 | 카운터, 실시간 시계, 동적 표 생성, 게시판 행 생성, 클래스 개수 세기, 빈 요소 채우기 |
| 문서 형식 | JavaScript Developer-Wiki V3 개인 강의 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> DOM 콘텐츠를 읽고 변경하며, 요소를 생성·삽입하고, 스타일을 조작하는 데 필요한 핵심 코드만 발췌해 설명한다.

---

## 이 문서에서 바로 찾기

- [개념에서 실제 실행까지: 콘텐츠 변경은 문자열을 표시하거나 새로운 노드를 연결하는 일이다](#js-12-section-4)
- [5. 세 속성 비교](#js-12-section-9)
- [34. 삽입 위치 비교](#js-12-section-38)
- [61. 내 코드와 강사님 코드 비교](#js-12-section-65)
- [63. 실무형 예제: 안전한 게시판 렌더링](#js-12-section-67)
- [64. 대표 오류로 이해하기](#js-12-section-68)
- [65. 자주 하는 실수](#js-12-section-69)
- [66. 핵심 요약](#js-12-section-70)
- [67. 최종 체크리스트](#js-12-section-71)

<details>
<summary>세부 목차 펼치기 — 번호형 본문 전체</summary>

- [개요](#js-12-section-1)
- [핵심 개념](#js-12-section-2)
- [학습 목표](#js-12-section-3)
- [개념에서 실제 실행까지: 콘텐츠 변경은 문자열을 표시하거나 새로운 노드를 연결하는 일이다](#js-12-section-4)
- [1. 원본 HTML 구조](#js-12-section-5)
- [2. `textContent`](#js-12-section-6)
- [3. `innerText`](#js-12-section-7)
- [4. `innerHTML`](#js-12-section-8)
- [5. 세 속성 비교](#js-12-section-9)
- [6. 텍스트 변경](#js-12-section-10)
- [7. `innerText` 변경](#js-12-section-11)
- [8. `innerHTML` 변경](#js-12-section-12)
- [9. `innerHTML +=`](#js-12-section-13)
- [10. `innerHTML`과 XSS](#js-12-section-14)
- [11. 안전한 링크 생성](#js-12-section-15)
- [12. `replaceChildren()`](#js-12-section-16)
- [13. 카운터 기본 구조](#js-12-section-17)
- [14. 카운터 갱신](#js-12-section-18)
- [15. 숫자 변환 검증](#js-12-section-19)
- [16. 상태를 DOM에만 저장하지 않기](#js-12-section-20)
- [17. 타이머 해제](#js-12-section-21)
- [18. 실시간 시계](#js-12-section-22)
- [19. Date를 반복문 밖에 두면?](#js-12-section-23)
- [20. 시계 두 자리 형식](#js-12-section-24)
- [21. 갱신 간격과 정확도](#js-12-section-25)
- [22. DOM 요소 생성](#js-12-section-26)
- [23. 생성한 요소 설정](#js-12-section-27)
- [24. DOM 삽입 전과 후](#js-12-section-28)
- [25. `append()`](#js-12-section-29)
- [26. 문자열 `append()`](#js-12-section-30)
- [27. 같은 Node를 두 번 Append](#js-12-section-31)
- [28. Node 복제](#js-12-section-32)
- [29. `appendChild()`](#js-12-section-33)
- [30. `append()`와 `appendChild()`](#js-12-section-34)
- [31. `prepend()`](#js-12-section-35)
- [32. `before()`](#js-12-section-36)
- [33. `after()`](#js-12-section-37)
- [34. 삽입 위치 비교](#js-12-section-38)
- [35. Table 행 생성](#js-12-section-39)
- [36. 데이터 배열](#js-12-section-40)
- [37. 반복문으로 게시판 생성](#js-12-section-41)
- [38. 단계별 조립 원리](#js-12-section-42)
- [39. `innerHTML`로 표 생성](#js-12-section-43)
- [40. `innerHTML` 표 생성의 위험](#js-12-section-44)
- [41. 반복마다 `innerHTML` 갱신](#js-12-section-45)
- [42. 역순 데이터 출력](#js-12-section-46)
- [43. `DocumentFragment`](#js-12-section-47)
- [44. 문자열 역순 누적](#js-12-section-48)
- [45. Style 요소 생성](#js-12-section-49)
- [46. Script 동적 삽입 주의](#js-12-section-50)
- [47. 인라인 스타일](#js-12-section-51)
- [48. CSS 속성 이름 변환](#js-12-section-52)
- [49. `element.style`](#js-12-section-53)
- [50. 계산된 스타일](#js-12-section-54)
- [51. `getPropertyValue()`](#js-12-section-55)
- [52. 높이 숫자 계산](#js-12-section-56)
- [53. Style 직접 조작과 클래스](#js-12-section-57)
- [54. 문제 1: 텍스트 뒤에 문자열 추가](#js-12-section-58)
- [55. 문제 2: `q2` 클래스 개수](#js-12-section-59)
- [56. NodeList와 `classList`](#js-12-section-60)
- [57. 문제 3: `q2` 텍스트 출력](#js-12-section-61)
- [58. 문제 4: 빈 요소 채우기](#js-12-section-62)
- [59. `innerText === ""`의 한계](#js-12-section-63)
- [60. 스타일 직접 변경 개선](#js-12-section-64)
- [61. 내 코드와 강사님 코드 비교](#js-12-section-65)
- [62. 기존 코드에서 개선 코드로 바꾼 이유](#js-12-section-66)
- [63. 실무형 예제: 안전한 게시판 렌더링](#js-12-section-67)
- [64. 대표 오류로 이해하기](#js-12-section-68)
- [65. 자주 하는 실수](#js-12-section-69)
- [66. 핵심 요약](#js-12-section-70)
- [67. 최종 체크리스트](#js-12-section-71)
- [마무리](#js-12-section-72)
- [V3 실행 추적 카드 — 데이터 → 노드 생성 → DOM 연결 → 렌더링](#js-12-section-73)

</details>

---

<a id="js-12-section-1"></a>

## 개요

11번에서는 이미 존재하는 DOM 요소를 선택하고 속성·클래스를 조작했다.

12번에서는 선택한 요소의 **내용을 읽고 바꾸고**, 새로운 요소를 **직접 생성해 문서에 삽입**한다.

```text
요소 선택
    ↓
내용 읽기·변경
    ↓
새 요소 생성
    ↓
부모·형제 위치에 삽입
    ↓
스타일과 상태 변경
```

```javascript
const message = document.querySelector(
    "#message",
)

message.textContent = "변경된 내용"
```

> [!IMPORTANT]
> DOM 조작에서 가장 먼저 결정해야 할 것은 **일반 텍스트를 넣을지**, **HTML 구조를 넣을지**다.

---

<a id="js-12-section-2"></a>

## 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `textContent` | 노드 내부의 텍스트를 원문에 가깝게 읽고 변경 |
| `innerText` | 화면에 실제 표시되는 텍스트를 읽고 변경 |
| `innerHTML` | 내부 HTML 구조를 문자열로 읽고 변경 |
| `createElement()` | 메모리에 새 Element 생성 |
| `append()` | 마지막 자식으로 Node 또는 문자열 추가 |
| `appendChild()` | 마지막 자식으로 Node 하나 추가 |
| `prepend()` | 첫 번째 자식으로 추가 |
| `before()` | 이전 형제로 추가 |
| `after()` | 다음 형제로 추가 |
| `DocumentFragment` | 여러 노드를 한 번에 삽입하기 위한 임시 컨테이너 |
| `style` | 요소의 인라인 스타일 조작 |
| `getComputedStyle()` | 최종 계산된 CSS 값 조회 |
| XSS | 신뢰하지 못한 문자열이 HTML·Script로 실행되는 보안 문제 |

---

<a id="js-12-section-3"></a>

## 학습 목표

- textContent·innerHTML·노드 이동을 구분한다.
- 원본의 해당 부분을 찾아 실행 순서와 결과를 다시 확인한다.

---

<a id="js-12-section-4"></a>

## 개념에서 실제 실행까지: 콘텐츠 변경은 문자열을 표시하거나 새로운 노드를 연결하는 일이다

textContent는 텍스트를 다루고 innerHTML은 문자열을 HTML로 파싱하여 자식 노드를 바꾼다. 같은 "<b>안녕</b>"도 textContent는 태그 문자까지 보이고 innerHTML은 b 요소를 만든다. innerText는 렌더링 상태와 연결되어 숨김·공백·줄바꿈 처리에서 차이가 있다. 쓰기에서도 줄바꿈이 br로 변환될 수 있어 완전히 동일하지 않다.

두 원본은 createElement로 div를 만든 뒤 log.append(div)를 두 번 호출한다. 같은 노드를 복제한 것이 아니라 위치를 이동한 것이다. 다른 위치에도 같은 모양이 필요하면 새 노드를 만들거나 cloneNode를 사용한다. cloneNode는 addEventListener로 붙인 이벤트를 자동 복사하지 않는다.

내 시계는 시·분·초·밀리초를, 강사님 시계는 분·초·밀리초를 표시하며 갱신 간격도 다르다. 타이머가 1초라고 실제 화면이 정확히 매1초 갱신되는 것은 아니다. createElement 시점에는 아직 화면에 붙지 않으며 append한 뒤 연결 상태가 바뀐다.

### 수업 원본에서 사용한 부분

아래는 전체 실행 파일이 아니라 **개념에 대응하는 문맥 발췌**다. 나머지 HTML·선언·등록 코드는 원본과 기존 번호형 본문에서 이어 확인한다. 

내 코드: `workspace_html/javascript/12_dom_content.html`

```javascript
<script>
            const msg = document.querySelector('#msg')
            console.log(msg)

            // 태그 안쪽의 글씨들(content)을 가져오는 3가지 방법들

            // textContent , div안에 있는 공백 및 엔터까지 같이 출력됨
            // content영역의 소스 중에서 'text(글씨)'만 '그대로' 가져옴,
```

강사님 코드: `workspace_teacher/workspace_html/javascript/12_dom_content.html`

```javascript
<script>
        const msg = document.querySelector('#msg')
        console.log(msg)

        // 태그 안쪽의 글씨들(컨텐츠) 가져오는 방법들

        // textContent
        // 컨텐츠 영역의 소스 중에서 text(글씨)만 "그대로" 가져온다
```

### 직접 재현하는 최소 예제와 결과

이 예제는 **이번 리팩토링의 설명용 재구성**이다. 원본 그대로의 발췌와 구별한다. 브라우저 Console에서 실행한다. 다른 예제의 변수와 섞이지 않게 새 실행 문맥에서 실행한다.

```javascript
const box = document.createElement("div");
const p = document.createElement("p");
p.textContent = "<b>안녕</b>";
box.append(p);
box.append(p);
console.log(box.children.length, p.textContent);
const copy = p.cloneNode(true);
box.append(copy);
console.log(box.children.length, p === copy);
```

예상 출력:

```text
1 <b>안녕</b>
2 false
```

### 결과를 역추적하는 방법

이 예제는 메모리에서만 노드를 만들므로 화면에는 나타나지 않는다. document.body.append(box)를 추가하면 문자 그대로의 두 줄을 확인할 수 있다. 사용자 입력은 textContent로 넣고 innerHTML +=가 기존 자식과 이벤트 참조를 교체할 수 있음을 주의한다.

출력은 아래의 확인 경로로 추적한다. return 값은 호출자에게 전달되고 자동으로 화면에 표시되지 않는다. Console 로그, DOM 변경, 저장소 변경, 서버 응답은 별개 단계다.

| 확인할 단계 | 이 예제에서 볼 것 |
| --- | --- |
| 입력 | 리터럴·현재 폼 값·이벤트 인수·응답 중 출처를 위 설명과 대조 |
| 실행 | 각 줄 또는 콜백이 지금 실행되는지, 나중에 실행되는지 구분 |
| 결과 | 위 예상 출력과 현재 값·자료형을 함께 대조 |
| 오류 | 첫 오류 줄의 입력과 직전 상태를 확인하고 뒤 로그 누락 원인 추적 |

### 단계별 복습 실습과 정답

**기본 실습:** 한 p노드를 A부모와B부모에 차례로append한 뒤 개수를 확인한다.

**응용·디버깅 실습:** 사용자가 <b>복습</b>을 입력했을 때 HTML 해석 없이 표시한다.

**통합 확인:** 위 최소 예제를 새 문맥에서 작성하고 정상값·빈 값·경계값으로 실행한다. 원본에서 대응하는 선언·호출·콜백을 찾아 위에 나타난 차이가 무엇을 바꾸는지 설명한다. 아래 정답은 먼저 예측한 뒤 펼친다. 이 실습은 💡 설명용 보강이며 원본에 모두 완성되어 있다는 뜻은 아니다.

<details>
<summary>정답과 처리 순서 해설</summary>

1. A에는0개, B에는1개다. 동일 노드를 옮겼다.
2. textContent에 넣는다. 실제화면에 태그 문자열이 보이고 자식b요소는 생성되지 않는다.
3. 최소 예제의 예상 출력과 한 줄씩 대조한다. 값이 다른 경우 입력 → 형 변환 → 분기/상태 변경 → 출력 순서로 첫 차이를 찾는다. DOM·API 예제는 Console 값만 아니라 화면·Elements·Network가 서로 같은 상태를 말하는지도 점검한다.

</details>

### 복습 질문과 해설

**질문:** innerHTML로 삽입한 script가 항상 실행되는가?

**해설:** 아니다. 그 사실이 안전함을 뜻하지도 않는다. 이벤트 핸들러 속성이나 위험한 URL 등으로 XSS가 가능하므로 사용자 입력의 HTML 삽입을 피한다.

**한 번 더 확인:** 예제의 입력을 하나 바꾸고 결과를 먼저 예상한 뒤 실행한다. 정상 입력만 아니라 비어 있는 값, 경계값, 두 번 실행했을 때의 상태를 기존 실습·오류 절에서 반복 확인한다.

---

<a id="js-12-section-5"></a>

## 1. 원본 HTML 구조

```html
<div id="msg">
    <span>원래</span> 있던 글씨
</div>
```

이 요소에는 다음 내용이 함께 있다.

- `span` 요소
- 텍스트 노드
- 들여쓰기와 공백

이 차이 때문에 콘텐츠 조회 방식마다 결과가 달라진다.

---

<a id="js-12-section-6"></a>

## 2. `textContent`

```javascript
const message = document.querySelector(
    "#msg",
)

console.log(
    message.textContent,
)
```

`textContent`는 하위 태그를 제외하고 텍스트 노드 내용을 읽는다.

소스에 포함된 줄바꿈·들여쓰기·공백도 포함될 수 있다.

---

<a id="js-12-section-7"></a>

## 3. `innerText`

```javascript
console.log(
    message.innerText,
)
```

`innerText`는 브라우저 화면에 실제로 보이는 텍스트를 기준으로 계산한다.

숨겨진 요소나 CSS 레이아웃의 영향을 받을 수 있으며, 값을 읽는 과정에서 레이아웃 계산이 필요할 수 있다.

---

<a id="js-12-section-8"></a>

## 4. `innerHTML`

```javascript
console.log(
    message.innerHTML,
)
```

하위 HTML 태그까지 포함한 문자열을 반환한다.

대표 형태:

```html
<span>원래</span> 있던 글씨
```

---

<a id="js-12-section-9"></a>

## 5. 세 속성 비교

| 속성 | 태그 포함 | 숨겨진 텍스트 | 공백·줄바꿈 | 주요 목적 |
| --- | --- | --- | --- | --- |
| `textContent` | 아니오 | 포함 가능 | 소스에 가까움 | 일반 텍스트 읽기·쓰기 |
| `innerText` | 아니오 | 화면 표시 기준 | 화면 표시 기준 | 사용자에게 보이는 텍스트 |
| `innerHTML` | 예 | HTML 구조 포함 | HTML 문자열 | 내부 마크업 읽기·쓰기 |

---

<a id="js-12-section-10"></a>

## 6. 텍스트 변경

```javascript
message.textContent = (
    "<h1>제목</h1> a b c"
)
```

화면에는 태그가 실행되지 않고 글자로 표시된다.

```text
<h1>제목</h1> a b c
```

일반 사용자 문자열 출력에는 이 방식이 안전하다.

---

<a id="js-12-section-11"></a>

## 7. `innerText` 변경

```javascript
message.innerText = (
    "<h1>제목</h1> a b c"
)
```

이 경우에도 `<h1>`은 태그가 아니라 텍스트로 처리된다.

---

<a id="js-12-section-12"></a>

## 8. `innerHTML` 변경

```javascript
message.innerHTML = (
    "<h1>제목</h1> a b c"
)
```

`<h1>`이 실제 HTML 요소로 생성된다.

---

<a id="js-12-section-13"></a>

## 9. `innerHTML +=`

```javascript
message.innerHTML += "d"
```

기존 HTML을 읽고 새 문자열을 합친 뒤 내부 전체를 다시 파싱할 수 있다.

다음 문제가 생길 수 있다.

- 기존 하위 Node가 새로 만들어짐
- 연결된 이벤트가 사라질 수 있음
- 입력 상태가 초기화될 수 있음
- 반복할수록 불필요한 재파싱 증가

단순 텍스트 추가에는 다음이 더 적합하다.

```javascript
message.append("d")
```

---

<a id="js-12-section-14"></a>

## 10. `innerHTML`과 XSS

원본:

```javascript
message.innerHTML = (
    '<a href="javascript:alert(1)">눌러봐</a>'
)
```

`javascript:` URL이나 사용자 입력을 `innerHTML`에 넣으면 Script 실행 경로가 생길 수 있다.

> [!WARNING]
> 서버 응답·입력창·URL 파라미터 같은 신뢰하지 못한 문자열을 `innerHTML`에 직접 넣지 않는다.

---

<a id="js-12-section-15"></a>

## 11. 안전한 링크 생성

```javascript
const link = document.createElement(
    "a",
)

link.textContent = "안전한 링크"
link.href = "https://example.com"
link.rel = "noopener noreferrer"

message.replaceChildren(link)
```

HTML 문자열 조립 대신 DOM API로 요소와 속성을 분리한다.

---

<a id="js-12-section-16"></a>

## 12. `replaceChildren()`

```javascript
message.replaceChildren(
    link,
)
```

기존 모든 자식을 제거하고 전달한 Node·문자열로 교체한다.

`innerHTML = ""`보다 Node 기반 코드와 잘 어울린다.

---

<a id="js-12-section-17"></a>

## 13. 카운터 기본 구조

```html
<div id="count">0</div>
```

```javascript
const countElement = (
    document.querySelector(
        "#count",
    )
)
```

---

<a id="js-12-section-18"></a>

## 14. 카운터 갱신

```javascript
const countIntervalId = setInterval(
    () => {
        const current = Number(
            countElement.textContent,
        )

        countElement.textContent = (
            current + 1
        )
    },
    1000,
)
```

문자열 `"0"`을 숫자로 변환한 뒤 1을 더한다.

---

<a id="js-12-section-19"></a>

## 15. 숫자 변환 검증

```javascript
const current = Number(
    countElement.textContent,
)

if (Number.isNaN(current)) {
    countElement.textContent = "0"
}
```

DOM 텍스트가 항상 숫자라는 가정이 깨질 수 있으므로 검증할 수 있다.

---

<a id="js-12-section-20"></a>

## 16. 상태를 DOM에만 저장하지 않기

개선:

```javascript
let count = 0

const countIntervalId = setInterval(
    () => {
        count += 1

        countElement.textContent = (
            String(count)
        )
    },
    1000,
)
```

애플리케이션 상태는 JavaScript 변수에 두고 DOM은 표시 결과로 사용하는 편이 관리하기 쉽다.

---

<a id="js-12-section-21"></a>

## 17. 타이머 해제

```javascript
clearInterval(
    countIntervalId,
)
```

페이지 기능이 종료되거나 요소가 사라질 때 타이머를 정리해야 한다.

---

<a id="js-12-section-22"></a>

## 18. 실시간 시계

```javascript
const clockElement = (
    document.querySelector(
        "#clock",
    )
)

const clockIntervalId = setInterval(
    () => {
        const now = new Date()

        clockElement.textContent = (
            `${now.getHours()}시 `
            + `${now.getMinutes()}분 `
            + `${now.getSeconds()}초`
        )
    },
    250,
)
```

현재 시간은 반복 콜백 내부에서 새로 생성해야 한다.

---

<a id="js-12-section-23"></a>

## 19. Date를 반복문 밖에 두면?

```javascript
const now = new Date()

setInterval(
    () => {
        console.log(now)
    },
    1000,
)
```

같은 `Date` 객체가 계속 출력되어 시각이 갱신되지 않는다.

---

<a id="js-12-section-24"></a>

## 20. 시계 두 자리 형식

```javascript
function padTwo(
    value,
) {
    return String(value).padStart(
        2,
        "0",
    )
}
```

```javascript
const time = (
    `${padTwo(now.getHours())}:`
    + `${padTwo(now.getMinutes())}:`
    + `${padTwo(now.getSeconds())}`
)
```

---

<a id="js-12-section-25"></a>

## 21. 갱신 간격과 정확도

`setInterval(callback, 1000)`은 정확히 매 1000ms 실행을 보장하지 않는다.

브라우저 상태와 이벤트 루프에 따라 지연될 수 있다.

따라서 시계 값은 이전 값에 1을 더하기보다 매번 새로운 `Date`에서 읽는다.

---

<a id="js-12-section-26"></a>

## 22. DOM 요소 생성

```javascript
const div = document.createElement(
    "div",
)
```

이 시점에는 메모리에 Element 객체만 존재하고 화면에는 나타나지 않는다.

---

<a id="js-12-section-27"></a>

## 23. 생성한 요소 설정

```javascript
div.id = "lol"
div.textContent = "정글차이"
div.style.color = "red"
```

---

<a id="js-12-section-28"></a>

## 24. DOM 삽입 전과 후

```text
createElement()
→ 메모리에 생성

append()
→ DOM 트리에 삽입

브라우저
→ 화면에 렌더링
```

“가상 DOM”이라는 표현보다는 아직 문서 트리에 연결되지 않은 Element라고 설명하는 것이 정확하다.

---

<a id="js-12-section-29"></a>

## 25. `append()`

```javascript
const log = document.querySelector(
    "#log",
)

log.append(div)
```

마지막 자식으로 추가한다.

---

<a id="js-12-section-30"></a>

## 26. 문자열 `append()`

```javascript
log.append(
    "<h1>문자열</h1>",
)
```

태그로 해석되지 않고 텍스트 노드로 삽입된다.

---

<a id="js-12-section-31"></a>

## 27. 같은 Node를 두 번 Append

```javascript
log.append(div)
log.append(div)
```

복제본 두 개가 생기지 않는다.

같은 Node 객체가 마지막 위치로 이동한다.

---

<a id="js-12-section-32"></a>

## 28. Node 복제

```javascript
const clonedDiv = div.cloneNode(
    true,
)

log.append(
    div,
    clonedDiv,
)
```

복제본이 필요하면 `cloneNode()`를 사용한다.

`true`는 하위 노드까지 복사한다.

---

<a id="js-12-section-33"></a>

## 29. `appendChild()`

```javascript
const paragraph = (
    document.createElement(
        "p",
    )
)

paragraph.textContent = "p태그"

log.appendChild(
    paragraph,
)
```

Node 하나만 마지막 자식으로 추가한다.

---

<a id="js-12-section-34"></a>

## 30. `append()`와 `appendChild()`

| 항목 | `append()` | `appendChild()` |
| --- | --- | --- |
| 문자열 추가 | 가능 | 불가 |
| 여러 인수 | 가능 | 불가 |
| 반환값 | `undefined` | 추가한 Node |
| 위치 | 마지막 자식 | 마지막 자식 |

---

<a id="js-12-section-35"></a>

## 31. `prepend()`

```javascript
const firstParagraph = (
    document.createElement(
        "p",
    )
)

firstParagraph.textContent = (
    "첫 번째 자식"
)

log.prepend(
    firstParagraph,
)
```

부모의 첫 번째 자식으로 삽입한다.

---

<a id="js-12-section-36"></a>

## 32. `before()`

```javascript
const previous = (
    document.createElement(
        "p",
    )
)

previous.textContent = (
    "이전 형제"
)

log.before(previous)
```

---

<a id="js-12-section-37"></a>

## 33. `after()`

```javascript
const next = document.createElement(
    "p",
)

next.textContent = "다음 형제"

log.after(next)
```

---

<a id="js-12-section-38"></a>

## 34. 삽입 위치 비교

```text
before()
[대상 요소]
after()

[대상 요소 내부]
prepend()
기존 자식
append()
```

---

<a id="js-12-section-39"></a>

## 35. Table 행 생성

```javascript
const tableBody = (
    document.querySelector(
        "#tbody",
    )
)

const row = document.createElement(
    "tr",
)

const cell = document.createElement(
    "td",
)

cell.textContent = "첫째칸"
row.append(cell)
tableBody.append(row)
```

---

<a id="js-12-section-40"></a>

## 36. 데이터 배열

```javascript
const rows = [
    ["제목1", "작성자1"],
    ["제목2", "작성자2"],
    ["제목3", "작성자3"],
]
```

한 행에 필요한 값을 배열 하나로 표현한다.

---

<a id="js-12-section-41"></a>

## 37. 반복문으로 게시판 생성

```javascript
const board = document.querySelector(
    "#board",
)

for (const [
    title,
    author,
] of rows) {
    const row = document.createElement(
        "tr",
    )

    const titleCell = (
        document.createElement(
            "td",
        )
    )

    const authorCell = (
        document.createElement(
            "td",
        )
    )

    titleCell.textContent = title
    authorCell.textContent = author

    row.append(
        titleCell,
        authorCell,
    )

    board.append(row)
}
```

---

<a id="js-12-section-42"></a>

## 38. 단계별 조립 원리

```text
데이터 확인
→ tr 생성
→ td 생성
→ td에 안전한 텍스트 입력
→ td를 tr에 삽입
→ tr을 tbody에 삽입
```

복잡한 DOM 작업은 작은 단계로 나누면 오류를 찾기 쉽다.

---

<a id="js-12-section-43"></a>

## 39. `innerHTML`로 표 생성

```javascript
let html = ""

for (const [
    title,
    author,
] of rows) {
    html += `
        <tr>
            <td>${title}</td>
            <td>${author}</td>
        </tr>
    `
}

board.innerHTML = html
```

데이터가 완전히 신뢰 가능한 경우 간단히 사용할 수 있다.

---

<a id="js-12-section-44"></a>

## 40. `innerHTML` 표 생성의 위험

`title`이나 `author`가 사용자 입력이면 HTML이나 Script가 삽입될 수 있다.

```text
사용자 입력
→ 템플릿 리터럴
→ innerHTML
→ XSS 가능
```

신뢰하지 못한 값에는 `textContent` 기반 Node 생성 방식을 사용한다.

---

<a id="js-12-section-45"></a>

## 41. 반복마다 `innerHTML` 갱신

원본:

```text
for (...) {
    board.innerHTML = (
        html + board.innerHTML
    )
}
```

매 반복마다 기존 전체 HTML을 다시 읽고 파싱하므로 비효율적이다.

또한 앞에 붙여 역순이 된다.

---

<a id="js-12-section-46"></a>

## 42. 역순 데이터 출력

데이터 자체를 역순으로 순회한다.

```javascript
for (
    const [
        title,
        author,
    ]
    of [...rows].reverse()
) {
    // Node 생성
}
```

표시 순서를 DOM 문자열 재조립에 의존하지 않는다.

---

<a id="js-12-section-47"></a>

## 43. `DocumentFragment`

```javascript
const fragment = (
    document.createDocumentFragment()
)

for (const [
    title,
    author,
] of rows) {
    const row = document.createElement(
        "tr",
    )

    const titleCell = (
        document.createElement(
            "td",
        )
    )

    const authorCell = (
        document.createElement(
            "td",
        )
    )

    titleCell.textContent = title
    authorCell.textContent = author

    row.append(
        titleCell,
        authorCell,
    )

    fragment.append(row)
}

board.append(fragment)
```

여러 Node를 임시 Fragment에 모은 뒤 한 번에 삽입한다.

---

<a id="js-12-section-48"></a>

## 44. 문자열 역순 누적

원본:

```javascript
let result = ""

for (
    let index = 0;
    index < 5;
    index += 1
) {
    result = index + result
}
```

출력:

```text
43210
```

새 값을 기존 문자열 앞에 붙이기 때문이다.

---

<a id="js-12-section-49"></a>

## 45. Style 요소 생성

```javascript
const style = document.createElement(
    "style",
)

style.textContent = `
    #board {
        border: 1px solid red;
    }
`

document.head.append(style)
```

스타일 요소는 의미상 `<head>`에 넣는 편이 자연스럽다.

---

<a id="js-12-section-50"></a>

## 46. Script 동적 삽입 주의

```javascript
const script = document.createElement(
    "script",
)

script.textContent = (
    "alert('실행')"
)
```

동적 Script 삽입은 즉시 실행 경로가 될 수 있다.

일반 UI 개발에서는 고정된 JavaScript 모듈과 함수를 호출하는 방식을 사용한다.

---

<a id="js-12-section-51"></a>

## 47. 인라인 스타일

```javascript
const clock = document.getElementById(
    "clock",
)

clock.style.color = "red"
clock.style.fontSize = "1.5em"
```

CSS의 `font-size`는 JavaScript에서 `fontSize`로 작성한다.

---

<a id="js-12-section-52"></a>

## 48. CSS 속성 이름 변환

| CSS | JavaScript style |
| --- | --- |
| `font-size` | `fontSize` |
| `background-color` | `backgroundColor` |
| `border-top-width` | `borderTopWidth` |

---

<a id="js-12-section-53"></a>

## 49. `element.style`

```javascript
console.log(
    clock.style.height,
)
```

인라인 스타일만 직접 확인한다.

외부 CSS나 `<style>`에서 적용된 값은 빈 문자열일 수 있다.

---

<a id="js-12-section-54"></a>

## 50. 계산된 스타일

```javascript
const computedStyle = (
    window.getComputedStyle(
        clock,
    )
)

console.log(
    computedStyle.width,
)
```

브라우저가 최종 계산한 CSS 값을 읽는다.

---

<a id="js-12-section-55"></a>

## 51. `getPropertyValue()`

```javascript
const width = (
    window
        .getComputedStyle(
            clock,
        )
        .getPropertyValue(
            "width",
        )
)
```

CSS 속성 이름 그대로 kebab-case를 사용할 수 있다.

---

<a id="js-12-section-56"></a>

## 52. 높이 숫자 계산

```javascript
clock.style.height = "66px"

const height = Number.parseFloat(
    clock.style.height,
)

clock.style.height = (
    `${height + 5}px`
)
```

`Number("66px")`는 `NaN`이지만 `parseFloat("66px")`는 `66`을 반환한다.

---

<a id="js-12-section-57"></a>

## 53. Style 직접 조작과 클래스

직접 조작:

```javascript
clock.style.color = "red"
```

클래스 방식:

```css
.clock--alert {
    color: red;
    border: 1px solid red;
}
```

```javascript
clock.classList.add(
    "clock--alert",
)
```

여러 스타일을 하나의 상태로 관리할 때는 클래스가 유지보수에 유리하다.

---

<a id="js-12-section-58"></a>

## 54. 문제 1: 텍스트 뒤에 문자열 추가

```javascript
const quiz1 = document.querySelector(
    ".quiz.q1",
)

quiz1.textContent += (
    " 쮸인님~♥"
)
```

기존 내용이 일반 텍스트이므로 `textContent`가 적합하다.

---

<a id="js-12-section-59"></a>

## 55. 문제 2: `q2` 클래스 개수

```javascript
const quiz2Items = (
    document.querySelectorAll(
        "div.quiz.q2",
    )
)

console.log(
    quiz2Items.length,
)
```

출력:

```text
2
```

전체 `.quiz`를 선택한 뒤 `contains()`로 검사할 수도 있지만 CSS 선택자로 직접 좁히는 편이 간결하다.

---

<a id="js-12-section-60"></a>

## 56. NodeList와 `classList`

잘못된 코드:

```text
const quizItems = document.querySelectorAll(
    "div.quiz"
)

quizItems.classList.contains(
    "q2"
)
```

`querySelectorAll()` 결과는 `NodeList`이며 `classList`가 없다.

각 요소에 접근해야 한다.

```javascript
for (const item of quizItems) {
    item.classList.contains(
        "q2",
    )
}
```

---

<a id="js-12-section-61"></a>

## 57. 문제 3: `q2` 텍스트 출력

```javascript
const quiz2Items = (
    document.querySelectorAll(
        "div.quiz.q2",
    )
)

for (const item of quiz2Items) {
    console.log(
        item.textContent,
    )
}
```

공백만 있는 요소는 공백 문자열이 출력될 수 있다.

---

<a id="js-12-section-62"></a>

## 58. 문제 4: 빈 요소 채우기

```javascript
const quizItems = (
    document.querySelectorAll(
        "div.quiz",
    )
)

for (const item of quizItems) {
    if (
        item.textContent.trim()
        === ""
    ) {
        item.textContent = "비어있음"

        item.classList.add(
            "is-empty",
        )
    }
}
```

---

<a id="js-12-section-63"></a>

## 59. `innerText === ""`의 한계

원본은 `innerText == ""`로 검사한다.

공백·줄바꿈이 있거나 CSS 표시 상태가 영향을 주면 판정이 달라질 수 있다.

텍스트 값의 실질적 공백 여부는 다음처럼 확인한다.

```javascript
item.textContent.trim()
=== ""
```

---

<a id="js-12-section-64"></a>

## 60. 스타일 직접 변경 개선

원본:

```javascript
item.style.background = "red"
item.style.fontWeight = "bold"
```

개선 CSS:

```css
.is-empty {
    background: red;
}

.is-q2 {
    background: yellow;
    font-weight: bold;
}
```

JavaScript:

```javascript
item.classList.add(
    "is-empty",
)
```

---

<a id="js-12-section-65"></a>

## 61. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 콘텐츠 설명 | 세 속성 차이를 상세히 기록 | 핵심 설명 중심 |
| 시계 | 시·분·초·밀리초, 250ms | 분·초·밀리초, 3000ms |
| 표 생성 | Node 방식과 `innerHTML` 방식 모두 시도 | 동일한 두 방식 제시 |
| 문제 풀이 | 1~4번 직접 구현 | 문제만 제시 |
| Style 설명 | 직접 계산 과정 상세 | 핵심 코드 중심 |
| 보안 | `javascript:` 링크를 기능 예제로 설명 | 동일 코드 사용 |
| Quiz 위치 | Script보다 앞 | Script 뒤에 일부 요소 배치 |

### 61-1. 내 코드의 장점

- `textContent`, `innerText`, `innerHTML`의 차이를 상세히 설명했다.
- 카운터·시계·표 생성 문제를 직접 구현했다.
- 클래스 개수·빈 텍스트 문제를 실제 코드로 완성했다.
- 인라인 스타일과 `getComputedStyle()` 차이를 기록했다.
- DOM 조립 과정을 단계적으로 설명했다.

### 61-2. 내 코드의 개선점

- `innerHTML`에 `javascript:` URL을 넣는 코드는 보안상 위험하다.
- 같은 요소를 타이머마다 다시 선택할 필요가 없다.
- 타이머 ID를 저장하고 해제하지 않는다.
- `innerHTML`을 반복마다 다시 쓰면 재파싱 비용이 커진다.
- 동적 `<style>`은 `<body>`보다 `<head>`에 넣는 편이 자연스럽다.
- 스타일 상태는 직접 property보다 클래스로 관리하는 편이 좋다.
- `==`보다 `===`를 사용해야 한다.

### 61-3. 강사님 코드의 장점

- 콘텐츠 조회·변경부터 DOM 생성까지 흐름이 단계적이다.
- `append()`와 `appendChild()` 차이를 직접 확인할 수 있다.
- 게시판 데이터를 표 행으로 만드는 과정을 자세히 보여 준다.
- 인라인 스타일과 계산된 스타일을 함께 다룬다.

### 61-4. 강사님 코드의 보충점

- Quiz 요소가 Script 뒤에 있어 Script 실행 시 선택할 수 없는 구조다.
- `innerHTML`과 `javascript:` URL의 XSS 위험 설명이 필요하다.
- 반복적 `innerHTML` 재할당의 단점이 필요하다.
- 타이머 정리와 상태 분리가 필요하다.
- `DocumentFragment`, `replaceChildren()` 같은 안전한 DOM API를 보충할 수 있다.

---

<a id="js-12-section-66"></a>

## 62. 기존 코드에서 개선 코드로 바꾼 이유

### 62-1. 안전한 텍스트 출력

기존:

```javascript
element.innerHTML = userInput
```

개선:

```javascript
element.textContent = userInput
```

### 62-2. 반복 선택 제거

기존:

```javascript
setInterval(
    () => {
        const count = (
            document.querySelector(
                "#count",
            )
        )
    },
    1000,
)
```

개선:

```javascript
const count = document.querySelector(
    "#count",
)

setInterval(
    () => {
        // count 재사용
    },
    1000,
)
```

### 62-3. 반복 `innerHTML` 제거

기존:

```javascript
board.innerHTML = (
    html + board.innerHTML
)
```

개선:

```javascript
fragment.append(row)
board.append(fragment)
```

### 62-4. Style 상태 클래스화

기존:

```javascript
item.style.background = "red"
```

개선:

```javascript
item.classList.add(
    "is-empty",
)
```

---

<a id="js-12-section-67"></a>

## 63. 실무형 예제: 안전한 게시판 렌더링

```javascript
function createBoardRow(
    post,
) {
    const row = document.createElement(
        "tr",
    )

    const titleCell = (
        document.createElement(
            "td",
        )
    )

    const authorCell = (
        document.createElement(
            "td",
        )
    )

    titleCell.textContent = post.title
    authorCell.textContent = post.author

    row.append(
        titleCell,
        authorCell,
    )

    return row
}

function renderBoard(
    board,
    posts,
) {
    const fragment = (
        document.createDocumentFragment()
    )

    for (const post of posts) {
        fragment.append(
            createBoardRow(post),
        )
    }

    board.replaceChildren(
        fragment,
    )
}

const posts = [
    {
        title: "<script>alert(1)</script>",
        author: "사용자1",
    },
    {
        title: "안전한 게시글",
        author: "사용자2",
    },
]

const board = document.querySelector(
    "#board",
)

if (board !== null) {
    renderBoard(
        board,
        posts,
    )
}
```

### 63-1. 실행 결과

첫 번째 제목의 Script는 실행되지 않고 일반 텍스트로 표시된다.

```text
<script>alert(1)</script>
```

### 63-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `createElement()` | 안전한 Element 생성 |
| `textContent` | 사용자 데이터를 텍스트로 출력 |
| `DocumentFragment` | 여러 행을 임시로 모음 |
| `replaceChildren()` | 기존 목록을 새 목록으로 교체 |
| 함수 분리 | 한 행 생성과 전체 렌더링 역할 구분 |
| `null` 검사 | 선택 실패 안전 처리 |

---

<a id="js-12-section-68"></a>

## 64. 대표 오류로 이해하기

<a id="index-section-86"></a>

### 64-1. `null` 요소에 콘텐츠 설정

```text
TypeError: Cannot set properties of null
```

선택 결과와 Script 실행 시점을 확인한다.

### 64-2. 문자열을 `appendChild()`에 전달

```text
TypeError: parameter 1 is not of type Node
```

문자열은 `append()`를 사용한다.

### 64-3. NodeList에 `classList` 사용

`classList`는 각 Element에 존재한다.

### 64-4. `Number("66px")`

결과는 `NaN`이다.

### 64-5. 타이머 중복 생성

같은 기능이 여러 번 실행되고 해제하기 어려워진다.

### 64-6. 신뢰하지 못한 `innerHTML`

XSS가 발생할 수 있다.

---

<a id="js-12-section-69"></a>

## 65. 자주 하는 실수

### 65-1. `textContent`와 `innerHTML`을 같은 기능으로 이해

텍스트 처리와 HTML 파싱은 다르다.

### 65-2. `innerText`가 항상 `textContent`와 같다고 생각

CSS 표시 상태와 레이아웃 계산의 영향을 받는다.

### 65-3. 생성한 요소가 자동으로 화면에 나온다고 생각

DOM 트리에 삽입해야 한다.

### 65-4. 같은 Node를 두 번 Append하면 복제된다고 생각

기존 Node가 이동한다.

### 65-5. `appendChild()`에 문자열 전달

Node만 받을 수 있다.

### 65-6. 반복마다 `innerHTML +=` 사용

전체 하위 DOM이 재파싱될 수 있다.

### 65-7. `element.style`로 외부 CSS 값을 읽으려 함

`getComputedStyle()`을 사용한다.

<a id="index-section-100"></a>

### 65-8. `"66px"`를 `Number()`로 변환

`parseFloat()` 또는 CSS Typed OM을 검토한다.

### 65-9. 공백만 있는 요소를 비어 있지 않다고 판단

`trim()` 후 비교한다.

### 65-10. 타이머를 생성하고 해제하지 않음

기능 종료 시 `clearInterval()`을 사용한다.

---

<a id="js-12-section-70"></a>

## 66. 핵심 요약

```text
textContent
→ 일반 텍스트

innerText
→ 화면에 보이는 텍스트

innerHTML
→ HTML 문자열
```

```text
createElement()
→ Element 생성

append()
prepend()
before()
after()
→ DOM 위치에 삽입
```

```text
append()
→ Node·문자열·여러 개 가능

appendChild()
→ Node 하나
```

```text
element.style
→ 인라인 스타일

getComputedStyle()
→ 최종 계산된 스타일

classList
→ 상태 기반 스타일 관리
```

---

<a id="js-12-section-71"></a>

## 67. 최종 체크리스트

- [ ] `textContent`, `innerText`, `innerHTML`을 구분할 수 있는가?
- [ ] 사용자 입력에는 `textContent`를 사용할 수 있는가?
- [ ] `innerHTML`의 XSS 위험을 설명할 수 있는가?
- [ ] 타이머로 DOM 텍스트를 갱신할 수 있는가?
- [ ] 타이머 ID를 저장하고 해제할 수 있는가?
- [ ] `createElement()`로 요소를 만들 수 있는가?
- [ ] 생성한 요소를 DOM에 삽입할 수 있는가?
- [ ] 같은 Node를 다시 삽입하면 이동함을 이해했는가?
- [ ] `cloneNode()`로 복제할 수 있는가?
- [ ] `append()`와 `appendChild()`를 구분할 수 있는가?
- [ ] `prepend()`, `before()`, `after()`를 사용할 수 있는가?
- [ ] 배열 데이터로 표 행을 생성할 수 있는가?
- [ ] 반복적인 `innerHTML` 재할당을 피할 수 있는가?
- [ ] `DocumentFragment`를 사용할 수 있는가?
- [ ] CSS 속성을 camelCase로 작성할 수 있는가?
- [ ] 인라인 스타일과 계산된 스타일을 구분할 수 있는가?
- [ ] 문자열 CSS 값을 숫자로 변환할 수 있는가?
- [ ] NodeList의 각 Element에 접근해 `classList`를 사용할 수 있는가?
- [ ] 공백만 있는 콘텐츠를 `trim()`으로 확인할 수 있는가?
- [ ] 스타일 상태를 클래스로 관리할 수 있는가?

---

<a id="js-12-section-72"></a>

## 마무리

DOM 콘텐츠 조작의 핵심은 화면에 문자열을 넣는 것에서 끝나지 않는다.

```text
텍스트와 HTML을 구분하고
    ↓
신뢰하지 못한 값은 안전하게 출력하고
    ↓
Node를 작은 단위로 생성해 조립하고
    ↓
반복 렌더링의 비용을 줄이고
    ↓
스타일과 상태를 클래스 중심으로 관리하는 것
```

이 흐름을 이해하면 이후 이벤트 문서에서 사용자 동작에 따라 안전하게 화면을 갱신할 수 있다.
<a id="js-12-section-73"></a>

## V3 실행 추적 카드 — 데이터 → 노드 생성 → DOM 연결 → 렌더링

`createElement`만으로는 화면에 나타나지 않으며 `append` 등으로 문서 트리에 연결해야 한다. `textContent`는 텍스트, `innerHTML`은 HTML을 파싱한다.

새 `li`를 만들고 textContent 설정 후 append하면 Elements에 노드가 생기고 화면 목록에 표시된다. 외부 입력을 innerHTML에 넣으면 XSS 위험이 있다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/javascript/12_dom_content.html`에서 실제 사용 위치와 차이를 확인한다.
