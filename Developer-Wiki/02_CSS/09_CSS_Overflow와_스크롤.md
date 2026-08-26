---
title: CSS Overflow와 스크롤
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# CSS Overflow와 스크롤

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `09_CSS_Overflow와_스크롤.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_html/css/09_overflow.html`, `workspace_teacher/workspace_html/css/09_overflow.html` |
| 핵심 범위 | `overflow`, `hidden`, `scroll`, `auto`, `overflow-x`, `overflow-y`, `white-space: nowrap`, 가로 스크롤 |
| 프로젝트 연결 | 카드 본문, 고정 높이 패널, 코드 영역, 모바일 탭, 가로 목록, 모달 내부 스크롤 |

> 이 문서는 내 코드와 강사님 코드의 `09_overflow.html`을 비교해 콘텐츠가 박스를 넘을 때 `visible`, `hidden`, `clip`, `scroll`, `auto`가 레이아웃과 스크롤 영역에 미치는 차이를 정리한다. 축별 Overflow, 가로 목록, 코드·테이블·모달 Scroll Container, 말줄임표와 접근성까지 실무 기준으로 연결한다.

---

# 학습 목표

- 콘텐츠가 요소의 박스보다 커질 때 발생하는 overflow를 설명한다.
- `overflow`의 기본값이 `visible`이라는 점을 이해한다.
- `overflow: hidden`이 넘친 콘텐츠를 잘라 보이지 않게 하는 원리를 설명한다.
- `overflow: scroll`이 콘텐츠의 넘침 여부와 관계없이 스크롤 영역을 만드는 특성을 이해한다.
- `overflow: auto`가 필요한 축에만 스크롤을 제공하는 일반적인 동작을 설명한다.
- `overflow-x`, `overflow-y`로 축별 넘침을 제어한다.
- `overflow-y: scroll`이 세로 스크롤바 공간을 항상 확보할 수 있다는 점을 이해한다.
- 짧은 콘텐츠를 넣은 `.scroll` 원본 예제의 의도를 설명한다.
- `white-space: nowrap`이 인라인 콘텐츠의 줄바꿈을 막는다는 점을 이해한다.
- `inline-block` 목록과 `overflow: auto`로 가로 스크롤을 구현한다.
- 고정 `width`와 `height`가 overflow 발생 조건에 미치는 영향을 이해한다.
- overflow가 새로운 스크롤 컨테이너와 블록 서식 문맥에 미치는 영향을 이해한다.
- `overflow: hidden`을 레이아웃 문제의 만능 해결책으로 사용하지 않는다.
- 스크롤 영역의 키보드 접근성과 포커스 표시를 고려한다.
- 내 코드와 강사님 코드의 차이와 원본 개선점을 찾는다.

---

# 1. Overflow란?

요소 안의 콘텐츠가 요소의 콘텐츠 박스보다 커지면 콘텐츠가 경계를 넘칠 수 있습니다.

```css
.box {
  width: 130px;
  height: 130px;
}
```

```html
<div class="box">
  매우 긴 내용...
</div>
```

콘텐츠가 박스보다 크다고 해서 브라우저가 자동으로 내용을 삭제하지는 않습니다.

기본 상태에서는 콘텐츠가 박스 밖으로 보일 수 있습니다.

```css
overflow: visible;
```

`overflow`는 이 넘친 콘텐츠를 어떻게 처리할지 지정합니다.

---

# 2. 원본 공통 박스

내 코드:

```css
.box {
  border: 1px solid red;
  height: 130px;
  width: 130px;
  margin: 10px;
}
```

강사님 코드:

```css
.box {
  border: 1px solid red;
  height: 130px;
  width: 100px;
  /* width: 130px; */
  margin: 10px;
}
```

두 코드의 중요한 차이:

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 실제 너비 | `130px` | `100px` |
| 주석 실험값 | 없음 | `width: 130px` |
| 높이 | `130px` | `130px` |

강사님 코드가 더 좁기 때문에 같은 길이의 텍스트라도 더 많은 줄로 나뉘고 세로 overflow가 더 쉽게 발생합니다.

---

# 3. 고정 크기와 overflow 발생

```css
.box {
  width: 100px;
  height: 130px;
}
```

박스 높이가 고정되어 있기 때문에 내용이 많아도 박스가 자동으로 늘어나지 않습니다.

내용이 높이보다 커지면 overflow가 발생합니다.

반대로 다음처럼 높이를 지정하지 않으면 블록 요소는 일반적으로 콘텐츠 높이만큼 늘어납니다.

```css
.box {
  width: 100px;
}
```

따라서 overflow 실습에서는 고정 높이를 지정해 넘침 상황을 의도적으로 만듭니다.

---

# 4. `overflow` 기본값

기본값:

```css
overflow: visible;
```

특징:

- 넘친 콘텐츠가 박스 밖으로 보일 수 있다.
- 스크롤바를 자동으로 만들지 않는다.
- 콘텐츠가 다음 요소 위에 겹쳐 보일 수 있다.
- 박스의 레이아웃 크기는 그대로 유지된다.

원본에는 `.visible` 클래스가 없지만, 아무 overflow 속성도 없는 고정 크기 박스를 추가하면 기본값을 비교할 수 있습니다.

```css
.visible {
  overflow: visible;
}
```

---

# 5. `overflow: hidden`

원본:

```css
.hidden {
  overflow: hidden;
}
```

박스 영역 밖으로 넘친 콘텐츠를 잘라 보이지 않게 합니다.

```text
박스 내부에 들어온 부분 → 표시
박스 밖으로 넘친 부분 → 잘림
```

원본 첫 번째 박스는 긴 Lorem Ipsum을 넣어 잘리는 결과를 확인합니다.

---

# 6. hidden은 콘텐츠를 삭제하지 않는다

```css
.hidden {
  overflow: hidden;
}
```

화면에서 보이지 않을 뿐 DOM의 텍스트가 제거되는 것은 아닙니다.

JavaScript:

```js
const box = document.querySelector(".hidden");

console.log(box.textContent);
```

전체 문자열을 읽을 수 있습니다.

하지만 사용자는 화면에서 잘린 부분을 볼 수 없고 기본 스크롤로 접근할 수도 없습니다.

중요한 본문을 단순히 `hidden`으로 잘라서는 안 됩니다.

---

# 7. `overflow: hidden`의 다른 효과

`overflow: hidden`은 넘침을 자르는 것 외에도 다음 효과가 생길 수 있습니다.

- 새로운 블록 서식 문맥을 형성할 수 있다.
- 자식 float를 감싸는 것처럼 보일 수 있다.
- 마진 상쇄 조건에 영향을 줄 수 있다.
- 자식의 그림자나 포커스 outline이 잘릴 수 있다.
- 절대 위치 자식의 일부가 잘릴 수 있다.
- 스티키 위치의 스크롤 기준에 영향을 줄 수 있다.

따라서 단순 레이아웃 보정 목적으로 무조건 사용하는 것은 피합니다.

---

# 8. `overflow: clip` 확장 학습

현대 CSS에서는 스크롤 컨테이너를 만들지 않고 넘친 부분만 자르는 목적에 `clip`을 검토할 수 있습니다.

```css
.box {
  overflow: clip;
}
```

`hidden`과 유사하게 보이지만 스크롤 동작과 서식 문맥에서 차이가 있습니다.

원본에는 없는 확장 개념이므로 프로젝트 지원 브라우저를 확인한 뒤 사용합니다.

---

# 9. `overflow: scroll`

원본:

```css
.scroll {
  overflow: scroll;
}
```

스크롤 영역을 명시적으로 만듭니다.

일반적인 특징:

- 콘텐츠가 넘치면 스크롤로 접근할 수 있다.
- 콘텐츠가 짧아도 스크롤바 영역이 표시될 수 있다.
- 가로와 세로 양쪽 축에 스크롤 UI가 생길 수 있다.
- 운영체제의 overlay scrollbar 설정에 따라 항상 눈에 보이지 않을 수도 있다.

---

# 10. 긴 콘텐츠가 있는 scroll 박스

원본 두 번째 박스:

```html
<div class="box scroll">
  긴 Lorem ipsum...
</div>
```

고정 박스보다 내용이 길기 때문에 세로 스크롤이 필요합니다.

박스 폭과 텍스트의 줄바꿈 결과에 따라 가로 스크롤은 필요하지 않을 수 있지만 `overflow: scroll`은 양쪽 축의 스크롤 영역을 만들 수 있습니다.

---

# 11. 짧은 콘텐츠가 있는 scroll 박스

원본 세 번째 박스:

```html
<div class="box scroll">
  Lorem ipsum
</div>
```

콘텐츠가 박스 안에 충분히 들어가더라도 클래스는 다음과 같습니다.

```css
.scroll {
  overflow: scroll;
}
```

이 예제의 핵심 목적은 다음 차이를 확인하는 것입니다.

```text
scroll → 필요하지 않아도 스크롤 영역을 만들 수 있음
auto   → 넘칠 때만 필요한 스크롤을 제공
```

강사님과 내 코드 모두 짧은 콘텐츠의 `.scroll` 박스를 별도로 배치했습니다.

---

# 12. 스크롤바는 운영체제마다 다르다

스크롤바가 “항상 보인다”는 설명은 환경에 따라 화면 결과가 다를 수 있습니다.

예:

- Windows 전통 스크롤바: 공간을 차지하며 보이는 경우가 많음
- macOS overlay scrollbar: 스크롤할 때만 보일 수 있음
- 모바일 브라우저: 얇은 표시만 잠시 나타날 수 있음
- 사용자 설정: 스크롤바 항상 표시 여부가 달라질 수 있음

따라서 핵심은 시각적 막대가 항상 보인다는 점보다 해당 요소가 스크롤 컨테이너로 동작한다는 점입니다.

---

# 13. 축별 overflow

개별 축을 제어할 수 있습니다.

```css
.box {
  overflow-x: auto;
  overflow-y: hidden;
}
```

대표 속성:

- `overflow-x`: 가로축
- `overflow-y`: 세로축

원본은 `.overflow-y` 클래스에서 세로축을 직접 제어합니다.

---

# 14. `overflow-y: scroll`

내 코드:

```css
/* -y는 y영역 스크롤이 생기게끔 보장 (x는 없어질수도 있다) */
.overflow-y {
  overflow-y: scroll;
  /* overflow-x: scroll; */
}
```

강사님 코드:

```css
.overflow-y {
  /* y 스크롤을 보장하라 */
  overflow-y: scroll;
  /* overflow-x: scroll; */
}
```

두 코드의 실제 속성값은 같습니다.

```css
overflow-y: scroll;
```

세로축을 스크롤 가능 영역으로 만들고, 전통적인 스크롤바 환경에서는 세로 스크롤바 공간을 미리 확보할 수 있습니다.

---

# 15. “x는 없어질 수도 있다” 설명 보완

내 코드 주석:

```text
x는 없어질수도 있다
```

축별 속성을 하나만 지정했을 때 다른 축의 계산값은 CSS overflow 규칙의 영향을 받을 수 있습니다.

단순히 “x는 사라진다”라고 암기하기보다 필요한 축을 명시하는 것이 안전합니다.

세로 스크롤만 허용하고 가로 overflow를 숨기려면:

```css
.box {
  overflow-x: hidden;
  overflow-y: auto;
}
```

긴 단어가 잘리는 문제를 줄이려면:

```css
.box {
  overflow-wrap: anywhere;
}
```

---

# 16. `overflow: auto`

원본:

```css
.auto {
  overflow: auto;
}
```

필요한 경우에만 스크롤을 제공하는 값입니다.

원본 내 코드 주석:

```text
auto는 필요 시 생기고 필요 없을 때 생기지 않음
실무에서는 자주 사용하지 않고 -y로 맞춰놓는편이 많음
```

첫 문장은 핵심적으로 맞습니다.

두 번째 문장은 일반화하기 어렵습니다.

실무에서도 `overflow: auto`는 다음 상황에서 매우 자주 사용됩니다.

- 모달 내부 본문
- 코드 블록
- 가로 탭 목록
- 테이블 래퍼
- 제한 높이 패널
- 채팅 기록 영역
- 파일 목록

목적에 따라 `overflow-y: auto`처럼 축을 명확히 지정하기도 합니다.

---

# 17. `scroll`과 `auto` 비교

| 구분 | `overflow: scroll` | `overflow: auto` |
| --- | --- | --- |
| 스크롤 영역 | 명시적으로 생성 | 필요할 때 생성 |
| 짧은 콘텐츠 | 스크롤 영역이 남을 수 있음 | 일반적으로 스크롤 불필요 |
| 레이아웃 안정성 | 스크롤바 공간을 미리 확보 가능 | 스크롤바 등장 시 폭 변화 가능 |
| 일반 사용 | 항상 스크롤 UI가 필요한 특수 상황 | 일반적인 제한 영역 |
| 원본 비교 | 긴 박스 + 짧은 박스 | 긴 박스 |

---

# 18. 세로 스크롤 패널 실무 패턴

```css
.panel {
  max-height: 20rem;
  overflow-y: auto;
}
```

`height`보다 `max-height`를 사용하면 내용이 적을 때 불필요하게 큰 빈 공간을 만들지 않을 수 있습니다.

```css
.modal__body {
  max-height: min(70vh, 40rem);
  overflow-y: auto;
}
```

---

# 19. `overflow` 단축 속성의 두 값

```css
.box {
  overflow: auto hidden;
}
```

두 값을 사용하면:

```text
첫 번째 값 → overflow-x
두 번째 값 → overflow-y
```

예:

```css
.horizontal-list {
  overflow: auto hidden;
}
```

다만 가독성을 위해 개별 속성을 사용하는 편이 명확할 수 있습니다.

```css
.horizontal-list {
  overflow-x: auto;
  overflow-y: hidden;
}
```

---

# 20. 원본 가로 스크롤 부모

원본:

```css
.parent {
  border: 1px solid red;
  width: 300px;
  white-space: nowrap;
  overflow: auto;
}
```

HTML:

```html
<div class="parent">
  <div>항목1</div>
  <div>항목2</div>
  <div>항목3</div>
  <div>항목4</div>
  <div>항목5</div>
</div>
```

부모 너비는 `300px`인데 자식 다섯 개의 전체 너비는 그보다 큽니다.

`white-space: nowrap`이 줄바꿈을 막고 `overflow: auto`가 넘친 가로 영역을 스크롤할 수 있게 합니다.

---

# 21. 원본 가로 목록 자식

```css
.parent div {
  border: 1px solid brown;
  display: inline-block;
  width: 100px;
  margin: 5px;
}
```

자식 하나의 대략적인 외부 가로 크기:

```text
width 100px
+ 좌우 border 2px
+ 좌우 margin 10px
= 약 112px
```

기본 `content-box` 기준입니다.

다섯 개라면 약:

```text
112px × 5 = 560px
```

부모 너비 `300px`보다 훨씬 크므로 가로 overflow가 발생합니다.

---

# 22. `white-space: nowrap`

```css
.parent {
  white-space: nowrap;
}
```

인라인 수준 콘텐츠의 자동 줄바꿈을 막습니다.

원본 자식은 `display: inline-block`이므로 한 줄에 계속 배치됩니다.

`nowrap`이 없다면 남는 공간이 부족할 때 다음 줄로 내려갈 수 있습니다.

```text
nowrap 없음 → 여러 줄 배치 가능
nowrap 있음 → 한 줄 유지, 가로 넘침
```

---

# 23. inline-block 사이 공백

HTML 태그 사이의 줄바꿈과 들여쓰기는 인라인 공백으로 렌더링될 수 있습니다.

```html
<div>항목1</div>
<div>항목2</div>
```

`inline-block` 사이에 작은 간격이 추가됩니다.

원본은 자식에 `margin: 5px`도 있으므로 공백까지 더해집니다.

정확한 폭 계산은 글꼴과 공백 렌더링에 따라 달라질 수 있습니다.

현대적인 가로 목록에는 Flexbox가 더 명확할 수 있습니다.

---

# 24. Flexbox 가로 스크롤 개선

```css
.horizontal-list {
  display: flex;
  gap: 0.625rem;
  overflow-x: auto;
}

.horizontal-list__item {
  flex: 0 0 100px;
}
```

장점:

- HTML 공백 영향을 받지 않음
- `gap`으로 간격을 관리
- 줄바꿈 금지 의도가 명확함
- 각 자식의 축소를 `flex: 0 0`으로 제어

HTML:

```html
<div class="horizontal-list">
  <div class="horizontal-list__item">항목 1</div>
  <div class="horizontal-list__item">항목 2</div>
  <div class="horizontal-list__item">항목 3</div>
</div>
```

원본의 학습 목적은 `nowrap + inline-block + overflow`이므로 원본 방식도 보존합니다.

---

# 25. 모바일 탭 목록 패턴

```css
.tabs {
  display: flex;
  gap: 0.5rem;
  padding-bottom: 0.5rem;
  overflow-x: auto;
  overscroll-behavior-inline: contain;
  scrollbar-width: thin;
}

.tabs__item {
  flex: 0 0 auto;
  white-space: nowrap;
}
```

사용자는 작은 화면에서 가로로 스크롤하여 탭을 볼 수 있습니다.

스크롤바를 완전히 숨기면 스크롤 가능 여부를 알아차리기 어려울 수 있으므로 신중하게 결정합니다.

---

# 26. 원본 Emmet 문자열 노출

내 코드와 강사님 코드 모두 HTML에 다음 문자열이 그대로 있습니다.

```text
div>div*5
```

HTML 주석이 아니므로 브라우저 화면에 텍스트로 표시됩니다.

Emmet 메모라면 다음처럼 작성합니다.

```html
<!-- Emmet: div>div*5 -->
```

최종 프로젝트에서는 제거할 수 있습니다.

---

# 27. 반복 `<br>` 문제

내 코드:

```html
<br><br><br><br><br><br><br><br><br><br>
```

강사님 코드에는 약 30개의 `<br>`가 있습니다.

하단 공간 또는 스크롤 실습을 위한 것으로 보입니다.

CSS로 대체:

```css
body {
  padding-bottom: 20rem;
}
```

또는:

```css
.page {
  min-height: 150vh;
}
```

의미 없는 반복 줄바꿈은 최종 문서 구조에서 제거합니다.

---

# 28. 문서 언어와 제목

내 코드와 강사님 코드:

```html
<html lang="en">
<title>Document</title>
```

본문과 설명은 한국어이므로 다음처럼 개선합니다.

```html
<html lang="ko">
<title>CSS Overflow</title>
```

---

# 29. 내 코드의 설명 장점

내 코드에는 강사님 코드보다 다음 설명이 추가되어 있습니다.

```css
/* -y는 y영역 스크롤이 생기게끔 보장 (x는 없어질수도 있다) */
```

```css
/* auto는 필요 시 생기고 필요 없을 때 생기지 않음
실무에서는 자주 사용하지 않고 -y로 맞춰놓는편이 많음 */
```

장점:

- `overflow-y`가 축별 제어라는 점을 기억하기 쉽다.
- `auto`와 `scroll`의 표시 조건 차이를 기록했다.
- 수업 후 복습할 때 실험 의도를 파악하기 쉽다.

---

# 30. 내 코드 설명 개선점

## 30.1 `auto`를 실무에서 자주 쓰지 않는다는 설명

일반화하기 어렵습니다.

`overflow: auto`, `overflow-y: auto`, `overflow-x: auto`는 실무에서 매우 자주 사용됩니다.

정확한 설명:

```text
auto는 실제 overflow가 발생한 축에 스크롤을 제공한다.
항상 세로 스크롤 영역을 유지해야 한다면 overflow-y: scroll을,
필요할 때만 제공하려면 overflow-y: auto를 사용한다.
```

## 30.2 x축 설명

다른 축의 계산 규칙을 단순히 “없어질 수 있다”로 설명하기보다 필요한 축을 명시적으로 지정합니다.

## 30.3 고정 너비 차이

내 코드는 `130px`, 강사님은 `100px`이므로 결과 비교 시 동일한 박스처럼 설명하면 안 됩니다.

---

# 31. 강사님 코드의 장점

- 각 overflow 값을 최소 코드로 비교한다.
- 긴 `.scroll`과 짧은 `.scroll`을 연속 배치해 항상 스크롤 영역을 만드는 특성을 관찰할 수 있다.
- `overflow-y: scroll`로 축별 제어를 보여 준다.
- 마지막 예제에서 `nowrap`, `inline-block`, `auto`를 결합해 가로 스크롤을 만든다.
- `width: 100px`과 주석 처리한 `130px`으로 박스 너비에 따른 텍스트 줄바꿈 차이를 실험할 수 있다.

---

# 32. 강사님 코드 개선점

## 32.1 width 실험값 정리

```css
width: 100px;
/* width: 130px; */
```

실험에는 유효하지만 최종 코드에서는 현재 의도를 주석으로 명확히 합니다.

```css
/* 좁은 박스에서 overflow를 더 쉽게 확인하기 위한 너비 */
width: 100px;
```

## 32.2 `auto` 설명 부족

강사님 코드에는 `.auto`의 결과 설명이 없습니다.

독립 문서에서는 `scroll`과 비교해 설명해야 합니다.

## 32.3 가로 스크롤 원리 설명 부족

`white-space: nowrap`이 왜 필요한지, `inline-block` 총너비가 부모보다 커진다는 설명을 보완합니다.

## 32.4 Emmet 문자열

`div>div*5`가 화면에 표시됩니다.

## 32.5 반복 `<br>`

약 30개의 `<br>`를 CSS 공간으로 대체합니다.

---

# 33. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| `.box` 너비 | `130px` | `100px` |
| 강사님 너비 실험 | 없음 | `130px` 주석 |
| Lorem 내용 | `Ducimus debitis...` | `Perferendis consequatur...` |
| `overflow-y` 설명 | y축 보장, x축 메모 | “y 스크롤을 보장하라” |
| `auto` 설명 | 필요 시 생성 + 실무 의견 | 설명 없음 |
| hidden/scroll/auto 값 | 동일 | 동일 |
| 짧은 scroll 박스 | 있음 | 있음 |
| 가로 목록 구조 | 동일 | 동일 |
| Emmet 노출 | `div>div*5` | `div>div*5` |
| 하단 `<br>` | 10개 | 약 30개 |
| 학습 성격 | 설명 추가형 | 최소 실습형 |

---

# 34. 원본 통합 개선 예제

## HTML

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>CSS Overflow</title>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      font-family: sans-serif;
    }

    .page {
      width: min(100% - 2rem, 60rem);
      margin-inline: auto;
      padding-block: 2rem;
    }

    .demo-list {
      display: grid;
      gap: 1rem;
    }

    .box {
      width: 12rem;
      height: 8rem;
      padding: 0.75rem;
      border: 1px solid #dc2626;
    }

    .box--hidden {
      overflow: hidden;
    }

    .box--scroll {
      overflow: scroll;
    }

    .box--auto {
      overflow: auto;
    }

    .box--vertical {
      overflow-x: hidden;
      overflow-y: auto;
    }

    .horizontal-list {
      display: flex;
      gap: 0.625rem;
      padding: 0.625rem;
      border: 1px solid #dc2626;
      overflow-x: auto;
    }

    .horizontal-list__item {
      flex: 0 0 7rem;
      padding: 1rem;
      border: 1px solid #92400e;
    }
  </style>
</head>
<body>
  <main class="page">
    <h1>CSS Overflow</h1>

    <section class="demo-list">
      <div class="box box--hidden">
        넘치는 콘텐츠를 잘라 표시하지 않습니다.
        중요한 정보에는 주의해야 합니다.
      </div>

      <div class="box box--scroll">
        콘텐츠의 길이와 관계없이
        스크롤 영역을 만듭니다.
      </div>

      <div class="box box--auto">
        실제로 넘칠 때 필요한 축에
        스크롤을 제공합니다.
      </div>

      <div class="box box--vertical">
        세로축만 필요한 경우
        overflow-y를 직접 사용합니다.
      </div>
    </section>

    <section>
      <h2>가로 목록</h2>

      <div class="horizontal-list">
        <div class="horizontal-list__item">항목 1</div>
        <div class="horizontal-list__item">항목 2</div>
        <div class="horizontal-list__item">항목 3</div>
        <div class="horizontal-list__item">항목 4</div>
        <div class="horizontal-list__item">항목 5</div>
      </div>
    </section>
  </main>
</body>
</html>
```

---

# 35. 코드 블록 실무 패턴

```css
pre {
  max-width: 100%;
  overflow-x: auto;
}
```

코드의 줄바꿈을 보존하면서 가로 스크롤을 제공합니다.

```css
pre code {
  white-space: pre;
}
```

긴 코드 줄을 임의로 끊으면 읽기 어려울 수 있으므로 코드 블록에는 가로 스크롤이 적합한 경우가 많습니다.

---

# 36. 테이블 래퍼 패턴

```html
<div class="table-wrapper" tabindex="0">
  <table>
    ...
  </table>
</div>
```

```css
.table-wrapper {
  max-width: 100%;
  overflow-x: auto;
}
```

작은 화면에서 표 전체 페이지가 가로로 넘치는 것을 방지합니다.

`tabindex="0"`은 키보드 사용자가 스크롤 영역에 포커스할 수 있게 할 수 있지만, 불필요한 탭 정류장을 만들지 않는지 실제 환경에서 확인합니다.

---

# 37. 모달 내부 스크롤

```css
.modal {
  display: grid;
  position: fixed;
  inset: 0;
  padding: 1rem;
  background-color: rgb(0 0 0 / 50%);
  place-items: center;
}

.modal__panel {
  width: min(100%, 40rem);
  max-height: calc(100dvh - 2rem);
  overflow-y: auto;
  background-color: white;
}
```

모달 전체가 화면 밖으로 넘어가지 않고 패널 내부에서 스크롤됩니다.

포커스 관리와 키보드 닫기는 별도로 구현해야 합니다.

---

# 38. 채팅 기록 영역

```css
.chat-log {
  min-height: 0;
  overflow-y: auto;
}
```

Flex/Grid 안의 스크롤 자식은 `min-height: 0`이 필요할 수 있습니다.

```css
.chat {
  display: grid;
  grid-template-rows: auto 1fr auto;
  height: 100dvh;
}

.chat-log {
  min-height: 0;
  overflow-y: auto;
}
```

---

# 39. `overscroll-behavior`

스크롤 영역 끝에서 상위 페이지로 스크롤이 이어지는 동작을 제어할 수 있습니다.

```css
.modal__body {
  overscroll-behavior: contain;
  overflow-y: auto;
}
```

원본에는 없는 확장 개념입니다.

모달이나 가로 캐러셀에서 스크롤 연쇄를 줄일 때 유용할 수 있습니다.

---

# 40. 스크롤바 스타일 주의

브라우저별 스크롤바 스타일 속성이 존재하지만 과도한 커스터마이징은 피합니다.

```css
.scroll-area {
  scrollbar-width: thin;
}
```

고려할 점:

- 운영체제 접근성 설정
- 충분한 대비
- 클릭 가능한 두께
- 브라우저 지원 차이
- 스크롤 가능 여부 인지

스크롤바를 완전히 숨기면 사용자가 영역이 스크롤된다는 사실을 모를 수 있습니다.

---

# 41. 포커스 outline 잘림

```css
.wrapper {
  overflow: hidden;
}
```

내부 링크의 포커스 outline이 박스 밖으로 나가면 잘릴 수 있습니다.

```css
.link:focus-visible {
  outline: 3px solid blue;
  outline-offset: 4px;
}
```

해결 방향:

- 불필요한 `overflow: hidden` 제거
- 내부 패딩 확보
- outline offset 조정
- `box-shadow` 기반 포커스 보조 검토

접근성 검수에서 키보드 포커스가 완전히 보이는지 확인합니다.

---

# 42. 이미지 크롭과 overflow

```css
.avatar {
  width: 100px;
  aspect-ratio: 1;
  overflow: hidden;
  border-radius: 50%;
}
```

```css
.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

이 경우 `overflow: hidden`은 원형 경계 밖의 이미지 부분을 자르는 명확한 목적이 있습니다.

이처럼 목적이 분명할 때 사용하는 것은 적절합니다.

---

# 43. 말줄임표와 overflow 연결

한 줄 말줄임표:

```css
.title {
  width: 240px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

여기서 `overflow: hidden`은 넘친 텍스트를 자르는 역할을 합니다.

CSS 07의 텍스트 넘침과 CSS 09의 overflow 개념이 연결됩니다.

---

# 44. 개발자 도구 확인 항목

Elements와 Computed 패널에서 확인합니다.

- 실제 `width`, `height`
- `overflow-x`, `overflow-y` 계산값
- 스크롤 가능한 총 콘텐츠 크기
- `scrollWidth`, `clientWidth`
- `scrollHeight`, `clientHeight`
- 줄바꿈 여부
- 자식의 외부 너비
- 스크롤바가 차지하는 공간

JavaScript 확인:

```js
const box = document.querySelector(".box");

console.log(box.clientHeight);
console.log(box.scrollHeight);
```

```text
scrollHeight > clientHeight
→ 세로 overflow 발생
```

---

# 45. overflow가 발생했는지 검사

```js
function hasVerticalOverflow(element) {
  return element.scrollHeight > element.clientHeight;
}

function hasHorizontalOverflow(element) {
  return element.scrollWidth > element.clientWidth;
}
```

동적 UI에서 “더 보기” 버튼을 표시할지 판단할 때 사용할 수 있습니다.

레이아웃 측정은 브라우저 렌더링 비용을 만들 수 있으므로 반복 호출을 주의합니다.

---

# 46. 콘텐츠가 잘릴 때 점검

1. `overflow: hidden`이 적용됐는가?
2. 부모나 조상에 hidden이 있는가?
3. 고정 높이 또는 최대 높이가 있는가?
4. 텍스트 말줄임표 스타일이 있는가?
5. 절대 위치 자식이 부모 밖으로 나갔는가?
6. 그림자와 outline이 잘리는가?
7. border-radius 크롭이 의도된 것인가?
8. 미디어 쿼리에서 overflow가 변경되는가?
9. 전체 내용을 볼 수 있는 방법이 있는가?
10. 개발자 도구에서 `scrollHeight`를 확인했는가?

---

# 47. 스크롤이 생기지 않을 때 점검

1. 콘텐츠가 실제로 박스보다 큰가?
2. 높이나 최대 높이가 제한됐는가?
3. 자식 콘텐츠가 정상 흐름에 있는가?
4. `overflow: visible`로 덮였는가?
5. 잘못된 축에 overflow를 지정했는가?
6. `white-space: nowrap`이 필요한 가로 목록인가?
7. 자식이 줄어들어 부모 안에 들어가는가?
8. Flex 자식의 `flex-shrink`가 적용되는가?
9. 스크롤 컨테이너가 다른 조상인가?
10. 운영체제 overlay scrollbar로 막대만 안 보이는가?

---

# 48. 원치 않는 가로 스크롤 점검

1. 고정 너비가 화면보다 큰가?
2. `width: 100vw`와 body 스크롤바가 겹치는가?
3. 음수 마진이 있는가?
4. 절대 위치 요소가 밖으로 나갔는가?
5. 긴 URL이나 단어가 줄바꿈되지 않는가?
6. `white-space: nowrap`이 상속됐는가?
7. 이미지에 `max-width: 100%`가 없는가?
8. transform으로 요소가 화면 밖으로 이동했는가?
9. `box-sizing` 계산을 확인했는가?
10. 원인을 찾지 않고 body에 hidden을 적용하려는가?

다음 방식은 문제를 숨길 수 있습니다.

```css
body {
  overflow-x: hidden;
}
```

먼저 실제 넘치는 요소를 찾아 수정합니다.

---

# 49. 자주 하는 실수

## 49.1 중요한 내용을 hidden으로 잘라 버림

전체 내용에 접근할 방법이 없어집니다.

## 49.2 scroll과 auto를 동일하게 이해

`scroll`은 필요하지 않은 상황에도 스크롤 영역을 만들 수 있고 `auto`는 넘침에 따라 결정합니다.

## 49.3 스크롤바가 항상 화면에 보여야 scroll이라고 판단

운영체제의 overlay scrollbar 설정에 따라 보이는 방식이 다릅니다.

## 49.4 축을 반대로 지정

가로 목록에 `overflow-y`, 세로 패널에 `overflow-x`를 지정하는 실수가 발생합니다.

## 49.5 nowrap 없이 가로 목록 스크롤 기대

인라인 요소가 다음 줄로 내려가면 가로 overflow가 생기지 않을 수 있습니다.

## 49.6 flex 자식이 줄어드는 것을 고려하지 않음

`flex: 0 0 auto` 또는 고정 basis가 필요할 수 있습니다.

## 49.7 body hidden으로 모든 가로 overflow 숨김

근본 원인을 찾기 어렵고 콘텐츠가 잘릴 수 있습니다.

## 49.8 포커스 outline 잘림

키보드 사용자가 현재 위치를 알기 어려워집니다.

## 49.9 스크롤 영역임을 알 수 있는 단서 제거

스크롤바를 숨기고 다음 항목 일부도 보이지 않으면 탐색 가능성을 알아차리기 어렵습니다.

## 49.10 반복 `<br>`로 페이지 길이 생성

레이아웃 공간은 CSS로 관리합니다.

---


# 종합실습

## 문제 1. 기본값

`overflow`의 기본값을 작성하세요.

## 문제 2. 숨김

너비 `150px`, 높이 `100px` 박스에서 넘친 콘텐츠를 잘라 보이지 않게 하세요.

## 문제 3. 항상 스크롤

`.box`에 콘텐츠 길이와 관계없이 스크롤 영역을 만드세요.

## 문제 4. 필요할 때 스크롤

`.box`에서 콘텐츠가 넘칠 때만 스크롤을 제공하세요.

## 문제 5. 세로축

세로축만 필요할 때 스크롤하도록 작성하고 가로 overflow는 숨기세요.

## 문제 6. 가로축

가로축만 필요할 때 스크롤하도록 작성하세요.

## 문제 7. 원본 비교

짧은 콘텐츠가 있는 요소에 `overflow: scroll`과 `overflow: auto`를 각각 적용하면 어떤 차이가 있는지 설명하세요.

## 문제 8. 콘텐츠 보존

`overflow: hidden`을 적용하면 DOM의 텍스트가 삭제되는지 설명하세요.

## 문제 9. 가로 목록

부모 너비 `300px` 안에서 너비 `100px` 항목 다섯 개를 한 줄에 유지하고 가로 스크롤하도록 원본 방식으로 작성하세요.

조건:

- `white-space`
- `inline-block`
- `overflow`

사용

## 문제 10. Flex 개선

문제 9를 Flexbox와 `gap`으로 개선하세요.

## 문제 11. 코드 블록

긴 코드 줄이 페이지 전체를 넘지 않고 코드 블록 안에서 가로 스크롤되도록 작성하세요.

## 문제 12. 테이블 래퍼

작은 화면에서 테이블만 가로 스크롤되도록 래퍼 CSS를 작성하세요.

## 문제 13. 모달 본문

모달 패널의 최대 높이를 화면 높이보다 작게 제한하고 내부 세로 스크롤을 제공하세요.

## 문제 14. 채팅 영역

Grid의 가운데 채팅 기록 행이 남은 높이를 사용하고 내부 스크롤되도록 작성하세요.

## 문제 15. 말줄임표

너비 `200px`인 한 줄 텍스트를 말줄임표 처리하세요.

## 문제 16. 이미지 크롭

정사각형 이미지를 원형으로 자르기 위해 overflow를 사용하세요.

## 문제 17. Emmet 문자열

다음 원본을 화면에 보이지 않는 메모로 수정하세요.

```html
div>div*5
```

## 문제 18. 반복 줄바꿈

하단 여백을 만들기 위한 `<br>` 30개를 CSS로 대체하세요.

## 문제 19. 원본 설명 수정

다음 주석을 더 정확하게 수정하세요.

```text
실무에서는 auto를 자주 사용하지 않고 -y로 맞춰놓는 편
```

## 문제 20. overflow 검사

세로 overflow가 실제로 발생했는지 반환하는 JavaScript 함수를 작성하세요.

## 문제 21. 가로 스크롤 원인

`white-space: nowrap`이 없는 원본 가로 목록에서 스크롤이 예상보다 생기지 않을 수 있는 이유를 설명하세요.

## 문제 22. 종합 모바일 탭

다음 요구사항을 만족하는 가로 탭 목록을 작성하세요.

- 실제 링크 사용
- Flexbox 사용
- 한 줄 유지
- 화면이 좁을 때 가로 스크롤
- 항목 축소 금지
- `gap` 사용
- 현재 탭에 `aria-current="page"`
- 키보드 포커스 표시
- 스크롤 연쇄 완화
- 스크롤 가능 여부를 완전히 숨기지 않음

---

# 정답과 해설

## 정답 1

```css
overflow: visible;
```

## 정답 2

```css
.box {
  width: 150px;
  height: 100px;
  overflow: hidden;
}
```

중요한 내용에는 전체 콘텐츠 접근 방법을 고려합니다.

## 정답 3

```css
.box {
  overflow: scroll;
}
```

## 정답 4

```css
.box {
  overflow: auto;
}
```

## 정답 5

```css
.box {
  overflow-x: hidden;
  overflow-y: auto;
}
```

## 정답 6

```css
.box {
  overflow-x: auto;
  overflow-y: hidden;
}
```

## 정답 7

`scroll`은 콘텐츠가 짧아도 스크롤 영역을 만들 수 있습니다. `auto`는 일반적으로 실제 overflow가 있을 때 필요한 축에 스크롤을 제공합니다.

스크롤바의 시각적 표시 방식은 운영체제 설정에 따라 다를 수 있습니다.

## 정답 8

삭제되지 않습니다.

DOM 텍스트는 그대로 존재하고 화면에서 넘친 부분만 보이지 않습니다.

## 정답 9

```css
.parent {
  width: 300px;
  white-space: nowrap;
  overflow-x: auto;
}

.parent > div {
  display: inline-block;
  width: 100px;
  margin: 5px;
}
```

## 정답 10

```css
.horizontal-list {
  display: flex;
  gap: 0.625rem;
  overflow-x: auto;
}

.horizontal-list > div {
  flex: 0 0 100px;
}
```

## 정답 11

```css
pre {
  max-width: 100%;
  overflow-x: auto;
}

pre code {
  white-space: pre;
}
```

## 정답 12

```css
.table-wrapper {
  max-width: 100%;
  overflow-x: auto;
}
```

## 정답 13

```css
.modal__panel {
  max-height: calc(100dvh - 2rem);
  overflow-y: auto;
}
```

## 정답 14

```css
.chat {
  display: grid;
  grid-template-rows: auto 1fr auto;
  height: 100dvh;
}

.chat__log {
  min-height: 0;
  overflow-y: auto;
}
```

## 정답 15

```css
.title {
  width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

## 정답 16

```css
.avatar {
  width: 100px;
  aspect-ratio: 1;
  overflow: hidden;
  border-radius: 50%;
}

.avatar img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

## 정답 17

```html
<!-- Emmet: div>div*5 -->
```

## 정답 18

```css
body {
  padding-bottom: 20rem;
}
```

## 정답 19

```text
overflow: auto는 실제 overflow가 발생할 때 필요한 스크롤을 제공하며
모달, 코드 블록, 테이블, 가로 목록 등 실무에서도 자주 사용한다.
항상 특정 축의 스크롤 영역이 필요하면 overflow-y: scroll을,
필요할 때만 제공하려면 overflow-y: auto를 선택한다.
```

## 정답 20

```js
function hasVerticalOverflow(element) {
  return element.scrollHeight > element.clientHeight;
}
```

## 정답 21

인라인 블록 자식이 부모 너비를 넘으면 다음 줄로 내려갈 수 있기 때문입니다. `white-space: nowrap`이 줄바꿈을 막아 전체 항목을 한 줄로 유지해야 가로 overflow가 발생합니다.

## 정답 22

### HTML

```html
<nav class="tabs" aria-label="과정 분류">
  <a
    class="tabs__link"
    href="/all"
    aria-current="page"
  >
    전체
  </a>

  <a class="tabs__link" href="/html">
    HTML
  </a>

  <a class="tabs__link" href="/css">
    CSS
  </a>

  <a class="tabs__link" href="/javascript">
    JavaScript
  </a>

  <a class="tabs__link" href="/react">
    React
  </a>
</nav>
```

### CSS

```css
.tabs {
  display: flex;
  gap: 0.5rem;
  padding: 0.5rem 0 0.75rem;
  overflow-x: auto;
  overscroll-behavior-inline: contain;
  scrollbar-width: thin;
}

.tabs__link {
  flex: 0 0 auto;
  padding: 0.625rem 0.875rem;
  border: 1px solid #d1d5db;
  border-radius: 999px;
  color: #1f2937;
  white-space: nowrap;
  text-decoration: none;
}

.tabs__link[aria-current="page"] {
  color: white;
  background-color: #2563eb;
  border-color: #2563eb;
}

.tabs__link:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 2px;
}
```

---

# 최종 체크리스트

## 기본 동작

- [ ] `overflow` 기본값이 `visible`임을 이해했다.
- [ ] 고정 높이나 최대 높이가 overflow 조건을 만든다는 점을 확인했다.
- [ ] `hidden`, `scroll`, `auto`의 차이를 실제로 비교했다.
- [ ] 짧은 `.scroll` 박스의 실습 의도를 설명할 수 있다.
- [ ] 운영체제별 스크롤바 표시 차이를 고려했다.

## 축별 제어

- [ ] 가로와 세로 중 필요한 축을 선택했다.
- [ ] `overflow-x`, `overflow-y`를 반대로 지정하지 않았다.
- [ ] 항상 세로 스크롤 영역이 필요한지 판단했다.
- [ ] 필요할 때만 스크롤이면 `auto`를 검토했다.
- [ ] 긴 단어 때문에 불필요한 가로 스크롤이 생기지 않는지 확인했다.

## 가로 목록

- [ ] 원본 방식에서 `white-space: nowrap`이 있다.
- [ ] 자식이 인라인 수준 또는 고정 Flex 항목으로 유지된다.
- [ ] 전체 자식 너비가 부모보다 큰지 확인했다.
- [ ] inline-block 공백과 margin을 고려했다.
- [ ] Flexbox와 `gap`이 더 명확한지 검토했다.
- [ ] 항목이 축소되지 않도록 설정했다.

## 접근성과 UX

- [ ] 중요한 콘텐츠를 접근 방법 없이 잘라 버리지 않았다.
- [ ] 스크롤 영역의 포커스 접근성을 확인했다.
- [ ] 포커스 outline이 overflow에 잘리지 않는다.
- [ ] 스크롤 가능한 영역이라는 시각적 단서가 있다.
- [ ] 스크롤바를 무조건 숨기지 않았다.
- [ ] 모달과 중첩 스크롤에서 overscroll을 검토했다.

## 레이아웃 부작용

- [ ] hidden이 block formatting context를 만드는 영향을 이해했다.
- [ ] sticky의 조상 overflow를 확인했다.
- [ ] 그림자와 절대 위치 자식이 잘리지 않는지 확인했다.
- [ ] body에 overflow-x hidden으로 원인을 숨기지 않았다.
- [ ] `scrollWidth`, `clientWidth`로 실제 넘침을 확인했다.

## 원본 코드 검수

- [ ] 내 코드 너비 `130px`, 강사님 너비 `100px` 차이를 보존했다.
- [ ] 강사님 `width: 130px` 주석 실험값을 기록했다.
- [ ] 내 코드의 auto 실무 설명을 일반화하지 않았다.
- [ ] `div>div*5`를 HTML 주석으로 개선했다.
- [ ] 반복 `<br>`를 CSS 공간으로 대체했다.
- [ ] `lang="en"`을 `lang="ko"`로 개선했다.
- [ ] `Document` 제목을 학습 주제로 변경했다.

---

# 핵심 요약

- overflow는 콘텐츠가 요소의 박스보다 커져 경계를 넘는 상태다.
- `overflow`의 기본값은 `visible`이다.
- `visible`에서는 넘친 콘텐츠가 박스 밖에 표시될 수 있다.
- `hidden`은 넘친 부분을 잘라 보이지 않게 하지만 DOM 콘텐츠를 삭제하지 않는다.
- 중요한 콘텐츠를 hidden으로 자를 때는 전체 내용을 볼 방법이 필요하다.
- `scroll`은 콘텐츠가 짧아도 스크롤 영역을 만들 수 있다.
- 원본의 짧은 `.scroll` 박스는 `scroll`과 `auto`의 차이를 확인하기 위한 예제다.
- 스크롤바의 실제 표시 방식은 운영체제와 사용자 설정에 따라 달라진다.
- `auto`는 실제 overflow가 발생할 때 필요한 스크롤을 제공한다.
- `overflow: auto`는 실무에서도 모달, 코드, 테이블, 패널, 가로 목록에 자주 사용된다.
- `overflow-x`, `overflow-y`로 가로와 세로축을 분리할 수 있다.
- `overflow-y: scroll`은 세로 스크롤 영역을 일관되게 유지하는 데 사용할 수 있다.
- 내 코드의 `.box` 너비는 `130px`, 강사님 코드는 `100px`이다.
- 강사님 코드는 `width: 130px`을 주석 실험값으로 보존한다.
- 박스가 좁을수록 텍스트 줄 수가 늘어 세로 overflow가 더 쉽게 발생한다.
- 원본 가로 목록은 `white-space: nowrap`, `inline-block`, `overflow: auto`를 조합한다.
- `nowrap`이 없으면 자식이 다음 줄로 내려가 가로 스크롤이 생기지 않을 수 있다.
- inline-block 태그 사이 HTML 공백과 margin도 전체 너비에 영향을 준다.
- Flexbox의 `flex: 0 0 auto`와 `gap`은 현대적인 가로 스크롤 목록에 유용하다.
- `overflow: hidden`은 자식 그림자, 포커스 outline, 절대 위치 콘텐츠를 자를 수 있다.
- 조상 overflow는 sticky 동작과 스크롤 컨테이너 기준에도 영향을 줄 수 있다.
- 가로 overflow의 원인을 찾지 않고 body 전체에 hidden을 적용하면 문제를 숨길 수 있다.
- 실제 overflow는 `scrollHeight > clientHeight`, `scrollWidth > clientWidth`로 검사할 수 있다.
- 원본의 `div>div*5`는 화면에 노출되는 Emmet 문자열이므로 주석으로 처리한다.
- 반복 `<br>`는 최종 코드에서 CSS 여백이나 최소 높이로 대체한다.
# V3 렌더링 추적 카드 — 콘텐츠 크기와 박스 경계

콘텐츠가 지정 박스보다 클 때 overflow가 처리 방식을 정한다. `hidden`은 넘친 부분을 자르고, `auto`는 필요할 때 스크롤을 제공하며, 축별 속성도 사용할 수 있다.

overflow 효과에는 제한할 width/height 또는 max-size가 필요하다. Box Model의 박스 크기와 scrollWidth/clientWidth 등을 함께 확인한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/css/09_overflow.html`에서 실제 선택자·계산값·화면 차이를 확인한다.
