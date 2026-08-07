---
title: CSS 투명도와 요소 숨김
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# CSS 투명도와 요소 숨김

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `05_CSS_투명도와_요소숨김.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_html/css/05_opacity.html`, `workspace_teacher/workspace_html/css/05_opacity.html` |
| 핵심 범위 | `visibility: hidden`, `display: none`, `opacity`, 레이아웃 공간, 상호작용, 접근성 |
| 프로젝트 연결 | 메뉴, 팝업, 모달, 아코디언, 로딩 상태, 페이드 전환, 시각적 숨김 |

> 이 문서는 내 코드와 강사님 코드의 `05_opacity.html`을 비교해 `visibility`, `display`, `opacity`가 화면·레이아웃·Pointer·Keyboard Focus·접근성 트리에 미치는 차이를 정리한다. 단순히 보이는지 여부만 비교하지 않고, 메뉴·모달·아코디언·로딩 상태에서 목적에 맞는 숨김 방식을 선택하도록 구성한다.

---

# 학습 목표

- 요소를 숨기는 여러 방식이 서로 다른 결과를 만든다는 점을 설명한다.
- `visibility: hidden`이 시각적으로 숨기면서 레이아웃 공간을 유지하는 것을 확인한다.
- `display: none`이 요소의 박스를 생성하지 않아 공간까지 제거하는 것을 설명한다.
- `opacity: 0`이 요소를 투명하게 만들 뿐 레이아웃과 상호작용 가능성을 자동으로 제거하지 않는다는 점을 이해한다.
- `opacity`의 값 범위와 자식 요소에 미치는 영향을 설명한다.
- 알파 채널 색상과 요소 전체 `opacity`의 차이를 구분한다.
- 숨김 방식에 따라 접근성 트리와 키보드 포커스가 어떻게 달라질 수 있는지 이해한다.
- `hidden`, `aria-hidden`, visually hidden 패턴을 구분한다.
- 팝업, 메뉴, 아코디언에서 목적에 맞는 숨김 방식을 선택한다.
- `display: none`과 `opacity`를 이용한 전환의 차이를 이해한다.
- 내 코드와 강사님 코드의 차이와 부정확한 설명을 찾아 개선한다.
- 개발자 도구로 레이아웃 공간과 상호작용 상태를 확인한다.

---

# 1. 원본 실습 구조

내 코드와 강사님 코드는 모두 다음 다섯 문단을 사용합니다.

```html
<p>첫번째</p>
<p class="hidden">두번째</p>
<p class="none">세번째</p>
<p class="opacity">네번째</p>
<p>다섯번째</p>
```

적용된 CSS:

```css
.hidden {
  visibility: hidden;
}

.none {
  display: none;
}

.opacity {
  opacity: 0;
}
```

화면에서 확인할 핵심 질문:

1. 두 번째 문단의 자리는 남아 있는가?
2. 세 번째 문단의 자리는 남아 있는가?
3. 네 번째 문단의 자리는 남아 있는가?
4. 보이지 않는 요소가 실제 문서 구조에는 존재하는가?
5. 마우스나 키보드로 상호작용할 수 있는가?

---

# 2. 원본 결과 한눈에 비교

| 클래스 | CSS | 화면 표시 | 레이아웃 공간 |
| --- | --- | --- | --- |
| `.hidden` | `visibility: hidden` | 보이지 않음 | 유지 |
| `.none` | `display: none` | 보이지 않음 | 제거 |
| `.opacity` | `opacity: 0` | 완전히 투명 | 유지 |

원본 화면의 문단 흐름은 개념적으로 다음과 같습니다.

```text
첫번째
[두번째가 차지하던 빈 공간]
[세번째는 공간도 없음]
[네번째가 차지하던 빈 공간]
다섯번째
```

두 번째와 네 번째는 화면에 글자가 보이지 않지만 원래 문단의 세로 공간은 남습니다.

세 번째는 레이아웃에서 빠지므로 공간도 사라집니다.

---

# 3. `visibility`

`visibility`는 요소의 표시 여부를 제어합니다.

대표 값:

- `visible`
- `hidden`
- `collapse`

기본값:

```css
visibility: visible;
```

원본:

```css
.hidden {
  visibility: hidden;
}
```

결과:

- 요소는 보이지 않는다.
- 원래 차지하던 레이아웃 공간은 유지된다.
- 자식도 기본적으로 보이지 않는다.
- 일반적으로 포인터 상호작용 대상에서 제외된다.
- 일반적으로 접근성 트리에서도 숨김으로 처리된다.

---

# 4. `visibility: hidden`의 공간 유지

HTML:

```html
<p>첫번째</p>
<p class="hidden">두번째</p>
<p>다섯번째</p>
```

CSS:

```css
.hidden {
  visibility: hidden;
}
```

두 번째 문단의 글자는 보이지 않지만 문단의 높이와 기본 마진은 남습니다.

따라서 첫 번째와 다섯 번째 사이에 빈 공간이 보입니다.

이 특징은 다음 상황에서 사용할 수 있습니다.

- 레이아웃 위치를 유지한 채 잠시 숨길 때
- 전환 애니메이션의 보조 속성
- 동일한 크기의 슬롯을 유지해야 할 때

단순히 공간까지 제거하려는 목적이라면 `display: none`이 더 적합할 수 있습니다.

---

# 5. `visibility`와 자식 요소

부모에 `visibility: hidden`을 지정하면 자식도 기본적으로 숨겨집니다.

```css
.parent {
  visibility: hidden;
}
```

```html
<div class="parent">
  <button>버튼</button>
</div>
```

다만 `visibility`는 상속되는 속성이므로 자식에서 다시 `visible`을 지정할 수 있습니다.

```css
.parent {
  visibility: hidden;
}

.parent__child {
  visibility: visible;
}
```

```html
<div class="parent">
  <span class="parent__child">
    다시 보이는 자식
  </span>
</div>
```

부모 박스의 공간은 계속 유지됩니다.

이러한 동작은 가능하지만 복잡한 UI 상태를 만들 수 있으므로 의도를 명확히 해야 합니다.

---

# 6. `display: none`

원본:

```css
.none {
  display: none;
}
```

`display: none`이 적용되면 요소는 일반 레이아웃에서 박스를 생성하지 않습니다.

결과:

- 화면에 보이지 않는다.
- 원래 차지하던 공간도 사라진다.
- 자식 요소도 함께 렌더링 박스를 만들지 않는다.
- 일반적으로 접근성 트리에서도 제외된다.
- 키보드 포커스와 포인터 상호작용 대상이 아니다.

원본 내 코드 주석:

```text
자리까지 없어지기때문에 보통 display를 주로 씀
```

핵심 결과는 맞지만 “보통 display를 주로 쓴다”는 표현은 목적에 따라 달라집니다.

공간 제거가 필요하면 `display: none`이 적합하지만, 애니메이션·시각적 숨김·접근성 안내 등 다른 목적에는 다른 방식이 필요합니다.

---

# 7. `display: none`과 문서 구조

다음 요소는 DOM에 계속 존재합니다.

```html
<p class="none">세번째</p>
```

```css
.none {
  display: none;
}
```

JavaScript에서는 여전히 선택할 수 있습니다.

```js
const paragraph = document.querySelector(".none");

console.log(paragraph.textContent);
```

하지만 렌더링 박스를 만들지 않습니다.

클래스를 제거하면 다시 표시할 수 있습니다.

```js
paragraph.classList.remove("none");
```

---

# 8. HTML 주석과 `display: none`

HTML 주석:

```html
<!--
<p>세번째</p>
-->
```

`display: none`:

```html
<p class="none">세번째</p>
```

차이:

| 항목 | HTML 주석 | `display: none` |
| --- | --- | --- |
| DOM 요소 생성 | 안 됨 | 됨 |
| CSS 선택 | 불가 | 가능 |
| JS 선택 | 불가 | 가능 |
| 공간 | 없음 | 없음 |
| 다시 표시 | 소스 수정 필요 | 상태 변경 가능 |

동적으로 열고 닫는 메뉴나 팝업에는 DOM 요소가 필요하므로 주석보다 상태 속성이나 클래스를 사용합니다.

---

# 9. `opacity`

`opacity`는 요소 전체의 불투명도를 지정합니다.

범위:

```text
0   → 완전히 투명
1   → 완전히 불투명
0.5 → 절반 정도 불투명
```

원본:

```css
.opacity {
  opacity: 0;
}
```

내 코드에는 비교 실험용 값도 주석 처리되어 있습니다.

```css
/* opacity: 0.3; */
```

강사님 코드에는 다음 값이 주석 처리되어 있습니다.

```css
/* opacity: 0.7; */
```

`0.3`과 `0.7`은 서로 다른 실습값일 뿐 오류가 아닙니다.

---

# 10. `opacity: 0`의 핵심 동작

```css
.opacity {
  opacity: 0;
}
```

결과:

- 요소는 완전히 투명해진다.
- 레이아웃 공간은 유지된다.
- 요소의 박스는 계속 존재한다.
- 자식까지 함께 투명해진다.
- 기본적으로 포인터 이벤트 영역이 남을 수 있다.
- 키보드 포커스 가능한 자식이 남을 수 있다.
- 일반적으로 접근성 트리에서도 자동으로 제거되지 않는다.

따라서 `opacity: 0`은 “완전히 숨기고 비활성화한다”와 같은 의미가 아닙니다.

---

# 11. 내 코드의 설명 보완

내 코드 주석:

```text
visibility:hidden과 opacity:0은 동일하게 자리는 있으나 투명하게 만듦
```

두 방식 모두 **공간이 남고 눈에 보이지 않는다**는 점은 같습니다.

그러나 동작이 완전히 동일하지는 않습니다.

| 비교 | `visibility: hidden` | `opacity: 0` |
| --- | --- | --- |
| 공간 | 유지 | 유지 |
| 포인터 상호작용 | 일반적으로 불가 | 기본적으로 가능할 수 있음 |
| 키보드 포커스 | 일반적으로 제외 | 남을 수 있음 |
| 접근성 트리 | 일반적으로 숨김 | 보통 남음 |
| 자식만 다시 표시 | `visibility: visible` 가능 | 부모 투명도 때문에 불가 |
| 전환 | 가능 | 매우 자주 사용 |

따라서 원본 주석은 **시각적 결과만 비교한 설명**으로는 이해할 수 있지만, 실무 동작까지 동일하다고 받아들이면 안 됩니다.

---

# 12. 투명한 요소의 클릭 문제

HTML:

```html
<a class="transparent-link" href="/next">
  다음 페이지
</a>
```

CSS:

```css
.transparent-link {
  opacity: 0;
}
```

링크는 보이지 않지만 클릭 영역이 남을 수 있습니다.

사용자는 빈 공간을 클릭했는데 페이지가 이동하는 예상 밖의 경험을 할 수 있습니다.

완전히 비활성화하려면 상태에 맞는 방식이 필요합니다.

```css
.transparent-link {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}
```

또는 실제로 레이아웃에서도 제거해야 한다면:

```css
.transparent-link {
  display: none;
}
```

---

# 13. 키보드 포커스 문제

```html
<div class="panel">
  <button type="button">저장</button>
</div>
```

```css
.panel {
  opacity: 0;
}
```

패널은 보이지 않지만 내부 버튼이 탭 순서에 남을 수 있습니다.

사용자는 화면에 보이지 않는 버튼에 포커스가 이동해 혼란을 겪을 수 있습니다.

단순히 `opacity: 0`만 사용하지 말고 표시 상태에 맞춰 다음을 함께 관리합니다.

- `visibility`
- `display`
- `hidden`
- `inert`
- 포커스 이동
- ARIA 상태

---

# 14. `opacity`는 자식 전체에 적용된다

```css
.card {
  opacity: 0.5;
}
```

```html
<div class="card">
  <h2>제목</h2>
  <p>설명</p>
</div>
```

다음이 모두 함께 반투명해집니다.

- 배경
- 테두리
- 텍스트
- 이미지
- 자식 요소

자식에서 `opacity: 1`을 지정해도 부모의 합성 결과보다 더 불투명하게 복원할 수 없습니다.

```css
.card {
  opacity: 0.5;
}

.card__title {
  opacity: 1;
}
```

제목은 자신의 불투명도 1을 가지지만 부모 전체가 0.5로 합성되므로 최종적으로 완전 불투명해지지 않습니다.

---

# 15. 배경만 투명하게 만들기

잘못된 목적 사용:

```css
.card {
  opacity: 0.5;
}
```

배경뿐 아니라 글자와 자식까지 흐려집니다.

배경색만 반투명하게 만들려면 알파 채널을 사용합니다.

```css
.card {
  background-color: rgb(0 0 0 / 50%);
}
```

또는:

```css
.card {
  background-color: rgba(0, 0, 0, 0.5);
}
```

텍스트는 불투명하게 유지됩니다.

이 차이는 CSS 02 단위와 색상 문서의 알파 채널 내용과 연결됩니다.

---

# 16. `opacity` 값의 유효 범위

일반적으로 다음 범위로 사용합니다.

```css
.element {
  opacity: 0;
}

.element {
  opacity: 0.5;
}

.element {
  opacity: 1;
}
```

퍼센트 표기도 지원되는 환경에서는 사용할 수 있습니다.

```css
.element {
  opacity: 50%;
}
```

프로젝트에서는 숫자 또는 퍼센트 중 하나의 표기 방식을 일관되게 사용합니다.

범위를 벗어난 값은 계산 과정에서 유효 범위로 제한됩니다.

---

# 17. 숨김 방식 핵심 비교

| 방식 | 보임 | 공간 | 클릭 | 키보드 포커스 | 접근성 트리 |
| --- | --- | --- | --- | --- | --- |
| `display: none` | 아니요 | 제거 | 불가 | 제외 | 일반적으로 제외 |
| `visibility: hidden` | 아니요 | 유지 | 일반적으로 불가 | 일반적으로 제외 | 일반적으로 제외 |
| `opacity: 0` | 아니요 | 유지 | 남을 수 있음 | 남을 수 있음 | 일반적으로 남음 |
| HTML `hidden` | 아니요 | 제거 | 불가 | 제외 | 일반적으로 제외 |
| visually hidden | 시각상 아니요 | 거의 제거 | 요소에 따라 | 요소에 따라 | 유지 |

브라우저와 보조 기술의 세부 동작에는 차이가 있을 수 있으므로 중요한 UI는 실제 환경에서 테스트합니다.

---

# 18. HTML `hidden` 속성

HTML 자체에서 요소를 숨길 수 있습니다.

```html
<div class="notice" hidden>
  공지 내용
</div>
```

JavaScript:

```js
const notice = document.querySelector(".notice");

notice.hidden = false;
```

일반적으로 `hidden` 요소는 `display: none`과 비슷하게 화면과 접근성 트리에서 제외됩니다.

의미:

```text
현재 이 요소는 표시할 상태가 아니다.
```

상태를 HTML 속성에 직접 표현할 수 있다는 장점이 있습니다.

---

# 19. `aria-hidden`

```html
<div aria-hidden="true">
  장식 콘텐츠
</div>
```

`aria-hidden="true"`는 보조 기술에서 요소와 자식을 숨기기 위한 접근성 속성입니다.

중요:

- 화면에서 자동으로 숨기지 않는다.
- 레이아웃 공간을 제거하지 않는다.
- 포커스 가능한 요소에 무분별하게 사용하면 안 된다.

잘못된 예:

```html
<div aria-hidden="true">
  <button type="button">저장</button>
</div>
```

버튼은 화면에 보이고 키보드 포커스를 받을 수 있는데 스크린 리더에는 숨겨질 수 있어 인터페이스가 불일치합니다.

시각적 숨김과 접근성 숨김은 서로 다른 문제입니다.

---

# 20. visually hidden 패턴

화면에는 표시하지 않지만 스크린 리더에는 제공해야 하는 텍스트가 있습니다.

예:

```html
<a class="icon-link" href="/search">
  <svg aria-hidden="true">...</svg>
  <span class="visually-hidden">검색</span>
</a>
```

CSS:

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}
```

이 경우 `display: none`이나 `visibility: hidden`을 사용하면 스크린 리더에서도 숨겨질 수 있으므로 목적에 맞지 않습니다.

---

# 21. `inert` 속성 확장 학습

비활성 영역의 상호작용과 포커스를 막을 때 `inert`를 사용할 수 있습니다.

```html
<main inert>
  배경 콘텐츠
</main>
```

모달이 열렸을 때 뒤쪽 콘텐츠를 비활성화하는 용도로 고려할 수 있습니다.

`inert`는 다음 효과를 목표로 합니다.

- 포커스 이동 차단
- 사용자 입력 차단
- 접근성 탐색 제한

시각적으로 자동 숨김 처리하는 속성은 아닙니다.

브라우저 지원 범위와 모달 구현 전체를 함께 검토해야 합니다.

---

# 22. 팝업 닫기 상태

팝업을 완전히 닫은 상태에서는 다음처럼 사용할 수 있습니다.

```html
<div class="popup" hidden>
  팝업 내용
</div>
```

열기:

```js
popup.hidden = false;
```

닫기:

```js
popup.hidden = true;
```

장점:

- 상태가 HTML 속성에 명확하게 표현된다.
- 레이아웃과 포커스 대상에서 제거된다.
- JavaScript 코드가 간결하다.

모달이라면 추가로 다음을 처리합니다.

- 열릴 때 모달 내부로 포커스 이동
- 닫힐 때 열기 버튼으로 포커스 복귀
- `Escape` 키 닫기
- 배경 영역 비활성화
- 적절한 대화상자 역할과 이름

---

# 23. 메뉴 열기와 닫기

HTML:

```html
<button
  class="menu-button"
  type="button"
  aria-controls="main-menu"
  aria-expanded="false"
>
  메뉴
</button>

<nav id="main-menu" hidden>
  <a href="/html">HTML</a>
  <a href="/css">CSS</a>
</nav>
```

JavaScript:

```js
const button = document.querySelector(".menu-button");
const menu = document.querySelector("#main-menu");

button.addEventListener("click", () => {
  const willOpen = menu.hidden;

  menu.hidden = !willOpen;
  button.setAttribute(
    "aria-expanded",
    String(willOpen)
  );
});
```

표시 상태와 `aria-expanded` 값을 함께 변경합니다.

---

# 24. 아코디언 패널

```html
<button
  class="accordion-button"
  type="button"
  aria-expanded="false"
  aria-controls="answer-1"
>
  CSS란 무엇인가요?
</button>

<div id="answer-1" hidden>
  CSS는 웹 문서의 표현을 담당합니다.
</div>
```

닫힌 패널이 완전히 탐색 대상에서 제외되어야 한다면 `hidden` 또는 `display: none`을 사용할 수 있습니다.

높이 애니메이션이 필요하면 별도의 상태 설계가 필요합니다.

---

# 25. `display`는 단순 전환되지 않는다

다음 코드는 `display` 자체를 부드럽게 숫자처럼 변화시키지 못합니다.

```css
.panel {
  display: none;
  transition: display 0.3s;
}

.panel.is-open {
  display: block;
}
```

전통적인 방식에서는 `display: none`인 동안 렌더링 박스가 없으므로 `opacity` 전환이 보이지 않습니다.

```css
.panel {
  display: none;
  opacity: 0;
  transition: opacity 0.3s;
}

.panel.is-open {
  display: block;
  opacity: 1;
}
```

위 코드만으로는 `display`가 바뀌는 순간의 전환 타이밍을 원하는 대로 만들기 어렵습니다.

---

# 26. 페이드 인·아웃 기본 패턴

```css
.popup {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(-0.5rem);
  transition:
    opacity 0.2s ease,
    transform 0.2s ease,
    visibility 0.2s;
}

.popup.is-open {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: translateY(0);
}
```

닫힌 상태:

- 투명
- 보이지 않음
- 클릭 불가
- 공간은 유지될 수 있음

팝업이 문서 흐름 바깥의 고정 위치 요소라면 공간 유지가 문제되지 않을 수 있습니다.

일반 문서 흐름 요소라면 닫힌 상태의 공간까지 제거해야 하는지 별도로 판단합니다.

---

# 27. `transition`과 `visibility`

`visibility`는 전환 지연과 함께 사용할 수 있습니다.

```css
.popup {
  opacity: 0;
  visibility: hidden;
  transition:
    opacity 0.2s,
    visibility 0s linear 0.2s;
}

.popup.is-open {
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}
```

닫힐 때:

1. `opacity`가 0으로 전환된다.
2. 전환이 끝난 뒤 `visibility: hidden`이 적용된다.

실제 구현에서는 프로젝트 브라우저 지원과 요구사항을 확인합니다.

---

# 28. 애니메이션 감소 설정

사용자가 움직임 감소를 요청한 경우를 고려합니다.

```css
@media (prefers-reduced-motion: reduce) {
  .popup {
    transition: none;
  }
}
```

숨김·표시 기능 자체는 유지하되 불필요한 이동이나 페이드 효과를 제거합니다.

---

# 29. 로딩 상태에서의 `opacity`

버튼을 비활성처럼 보이게 만들 수 있습니다.

```css
.button[aria-disabled="true"] {
  opacity: 0.5;
}
```

하지만 투명도만 낮춘다고 실제 비활성화되는 것은 아닙니다.

실제 버튼:

```html
<button type="button" disabled>
  처리 중
</button>
```

```css
.button:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}
```

링크에 `aria-disabled="true"`를 사용한다면 클릭 방지와 키보드 동작도 직접 처리해야 합니다.

---

# 30. 비활성 상태의 대비

```css
.button:disabled {
  opacity: 0.2;
}
```

지나치게 낮은 투명도는 텍스트를 읽기 어렵게 만들 수 있습니다.

비활성 상태도 사용자가 내용을 알아볼 수 있어야 합니다.

```css
.button:disabled {
  color: #6b7280;
  background-color: #e5e7eb;
  opacity: 1;
}
```

투명도만으로 상태를 전달하기보다 색상, 커서, 텍스트를 함께 설계합니다.

---

# 31. 호버 효과에서 `opacity`

```css
.thumbnail {
  opacity: 0.8;
  transition: opacity 0.2s;
}

.thumbnail:hover {
  opacity: 1;
}
```

주의:

- 중요한 정보가 기본 상태에서 너무 흐리지 않아야 한다.
- 터치 환경에서는 호버가 동일하게 작동하지 않을 수 있다.
- 키보드 사용자에게도 상태를 제공한다.

```css
.thumbnail:hover,
.thumbnail:focus-visible {
  opacity: 1;
}
```

---

# 32. 이미지 오버레이

배경만 반투명하게 만들고 텍스트는 선명하게 유지하는 예:

```html
<article class="image-card">
  <img
    class="image-card__image"
    src="course.webp"
    alt=""
  >
  <div class="image-card__overlay">
    <h2>CSS 과정</h2>
  </div>
</article>
```

```css
.image-card {
  position: relative;
}

.image-card__overlay {
  position: absolute;
  inset: 0;
  display: grid;
  color: white;
  background-color: rgb(0 0 0 / 55%);
  place-items: center;
}
```

오버레이 부모에 `opacity: 0.55`를 사용하면 글자도 함께 흐려질 수 있습니다.

---

# 33. 내 코드 분석

내 코드의 핵심 주석:

```css
/* 자리까지 없어지기때문에 보통 display를 주로 씀 */
.none {
  display: none;
}
```

```css
/* 글씨,그림 모두 투명도를 민들 수 있음 */
/* visibility:hidden과 opacity:0은 동일하게 자리는 있으나 투명하게 만듦 */
.opacity {
  /* opacity: 0.3; */
  opacity: 0;
}
```

## 33.1 장점

- `display: none`은 공간까지 없어진다는 점을 기록했다.
- `opacity`가 글자와 이미지 등 요소 전체에 적용된다는 방향을 설명했다.
- `visibility: hidden`과 `opacity: 0`이 공간을 유지한다는 공통점을 비교했다.
- `opacity: 0.3`을 주석으로 남겨 부분 투명도를 실험할 수 있게 했다.
- 강사님 코드보다 각 속성의 화면 결과를 설명하려는 주석이 많다.

---

# 34. 내 코드 개선점

## 34.1 문서 언어

원본:

```html
<html lang="en">
```

한국어 문서이므로:

```html
<html lang="ko">
```

가 적절합니다.

## 34.2 제목

```html
<title>Document</title>
```

문서 내용을 표현하도록 개선합니다.

```html
<title>CSS 투명도와 요소 숨김</title>
```

## 34.3 `민들` 오타

원본 주석:

```text
글씨,그림 모두 투명도를 민들 수 있음
```

정확한 표현:

```text
글씨와 그림을 포함한 요소 전체에 투명도를 적용할 수 있음
```

## 34.4 `display`를 주로 쓴다는 일반화

공간 제거 목적에는 적절하지만 모든 숨김 요구사항의 기본 정답은 아닙니다.

- 공간 제거: `display: none`, `hidden`
- 공간 유지: `visibility: hidden`
- 페이드 전환: `opacity` + 상태 제어
- 스크린 리더 전용 텍스트: visually hidden
- 보조 기술에서만 숨김: `aria-hidden`

목적에 따라 선택합니다.

## 34.5 `visibility`와 `opacity`가 동일하다는 표현

둘 다 공간이 남고 화면에 보이지 않을 수 있지만 상호작용과 접근성 동작이 다릅니다.

원본 문서에서 가장 중요하게 보완해야 할 설명입니다.

## 34.6 `opacity`와 비활성화

`opacity: 0` 또는 낮은 투명도만으로 클릭과 포커스가 제거되지 않습니다.

동적 UI에서는 실제 상태와 상호작용 제어를 함께 작성해야 합니다.

---

# 35. 강사님 코드 분석

강사님 코드는 설명 주석을 최소화하고 세 속성의 화면 차이를 직접 확인하도록 구성했습니다.

```css
.hidden {
  visibility: hidden;
}

.none {
  display: none;
}

.opacity {
  /* opacity: 0.7; */
  opacity: 0;
}
```

## 35.1 장점

- 예제가 매우 간결하다.
- 세 속성을 같은 문단 구조에서 바로 비교할 수 있다.
- `opacity: 0.7`과 `opacity: 0`을 번갈아 실험할 수 있다.
- 불필요한 외부 파일 없이 하나의 HTML에서 실행할 수 있다.

---

# 36. 강사님 코드 개선점

## 36.1 문서 언어

```html
<html lang="en">
```

한국어 본문이므로 `lang="ko"`가 적절합니다.

## 36.2 문서 제목

```html
<title>Document</title>
```

학습 주제가 드러나지 않습니다.

```html
<title>CSS Opacity</title>
```

또는 한국어 제목을 사용합니다.

## 36.3 결과 설명 부족

강사님 코드는 코드 결과를 관찰하는 데 적합하지만 다음 차이를 직접 설명하지 않습니다.

- 공간 유지 여부
- 상호작용 여부
- 접근성 트리
- 포커스
- 애니메이션 가능성

수업 설명과 함께 사용된 것으로 보이며, 독립 복습 문서에서는 보완이 필요합니다.

## 36.4 `opacity: 0.7`

오류는 아니지만 주석을 해제하면 “숨김”이 아니라 “70% 불투명” 상태입니다.

문서에서는 다음처럼 구분해야 합니다.

```text
opacity: 0.7 → 반투명
opacity: 0   → 완전 투명
```

---

# 37. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 구조 | 동일한 다섯 문단 | 동일한 다섯 문단 |
| `visibility` | 코드만 | 코드만 |
| `display: none` | 공간 제거 주석 추가 | 코드만 |
| `opacity` 실험값 | `0.3` | `0.7` |
| 공간 비교 | 주석으로 설명 | 직접 관찰 중심 |
| 부정확한 부분 | `visibility`와 `opacity`를 동일하게 표현 | 별도 설명 없음 |
| 오타 | 주석에 `민들` | 확인된 주석 오타 없음 |
| 문서 언어 | `lang="en"` | `lang="en"` |
| 제목 | `Document` | `Document` |
| 학습 성격 | 관찰 설명 추가형 | 최소 실습형 |

두 코드의 실행 구조와 최종 적용값은 거의 같습니다.

차이는 내 코드에 학습 주석이 추가되었고 부분 투명도 실험값이 다르다는 점입니다.

---

# 38. 원본을 개선한 기본 비교 예제

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
  <title>CSS 투명도와 요소 숨김</title>
  <link
    rel="stylesheet"
    href="asset/css/opacity.css"
  >
</head>
<body>
  <main class="page">
    <h1>CSS 숨김 방식 비교</h1>

    <section class="comparison">
      <p>첫 번째</p>
      <p class="is-invisible">
        두 번째: visibility hidden
      </p>
      <p class="is-not-displayed">
        세 번째: display none
      </p>
      <p class="is-transparent">
        네 번째: opacity zero
      </p>
      <p>다섯 번째</p>
    </section>
  </main>
</body>
</html>
```

## CSS

```css
body {
  margin: 0;
  font-family: sans-serif;
}

.page {
  width: min(100% - 2rem, 48rem);
  margin-inline: auto;
  padding-block: 2rem;
}

.comparison p {
  padding: 1rem;
  border: 1px solid #d1d5db;
}

.is-invisible {
  visibility: hidden;
}

.is-not-displayed {
  display: none;
}

.is-transparent {
  opacity: 0;
}
```

클래스 이름이 결과를 설명하도록 개선했습니다.

---

# 39. 실무 상태 클래스

```css
.is-hidden {
  display: none;
}
```

```css
.is-invisible {
  visibility: hidden;
}
```

```css
.is-transparent {
  opacity: 0;
}
```

이름을 구분해야 각 상태의 의도가 분명해집니다.

프로젝트에서 `.hidden`이라는 하나의 클래스가 서로 다른 숨김 방식을 의미하도록 섞어 사용하지 않습니다.

---

# 40. 상태 속성 중심 설계

가능하면 HTML의 상태 속성을 활용할 수 있습니다.

```html
<button
  aria-expanded="false"
  aria-controls="panel"
>
  상세보기
</button>

<div id="panel" hidden>
  상세 내용
</div>
```

CSS:

```css
[hidden] {
  display: none;
}
```

JavaScript:

```js
button.addEventListener("click", () => {
  const willOpen = panel.hidden;

  panel.hidden = !willOpen;
  button.setAttribute(
    "aria-expanded",
    String(willOpen)
  );
});
```

상태가 클래스와 ARIA에 따로 흩어지지 않도록 관리합니다.

---

# 41. 접근 가능한 모달 기본 구조

```html
<button
  class="modal-open"
  type="button"
>
  설정 열기
</button>

<div
  class="modal"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  hidden
>
  <div class="modal__panel">
    <h2 id="modal-title">
      설정
    </h2>

    <button
      class="modal-close"
      type="button"
    >
      닫기
    </button>
  </div>
</div>
```

`hidden`만 추가한다고 접근 가능한 모달이 완성되는 것은 아닙니다.

필요한 기능:

- 열릴 때 포커스 이동
- 모달 내부 포커스 순환
- 닫힐 때 원래 버튼으로 포커스 복귀
- `Escape` 키 처리
- 배경 클릭 정책
- 배경 콘텐츠 비활성화

---

# 42. 페이드 모달 예제

```css
.modal {
  position: fixed;
  inset: 0;
  display: grid;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  background-color: rgb(0 0 0 / 50%);
  transition:
    opacity 0.2s ease,
    visibility 0.2s ease;
  place-items: center;
}

.modal.is-open {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}
```

이 패턴은 모달이 `position: fixed`이므로 닫힌 상태에서 공간을 유지해도 일반 문서 흐름에는 영향을 주지 않습니다.

JavaScript와 접근성 상태를 함께 관리해야 합니다.

---

# 43. 로딩 플레이스홀더

레이아웃 공간을 유지해야 한다면 `visibility`가 유용할 수 있습니다.

```css
.card__content.is-loading {
  visibility: hidden;
}
```

대신 같은 공간에 스켈레톤 UI를 표시할 수 있습니다.

```html
<div class="card">
  <div class="card__skeleton">
    로딩 중
  </div>

  <div class="card__content is-loading">
    실제 콘텐츠
  </div>
</div>
```

실제 구현에서는 두 요소의 겹침과 접근성 안내를 설계해야 합니다.

---

# 44. 요소가 보이지 않을 때 점검 순서

1. `display: none`이 적용됐는가?
2. 상위 요소에 `display: none`이 있는가?
3. `visibility: hidden`이 상속됐는가?
4. `opacity: 0`인가?
5. 글자색과 배경색이 같은가?
6. 요소가 다른 요소 뒤에 가려졌는가?
7. 크기가 0인가?
8. 화면 밖으로 이동했는가?
9. `hidden` 속성이 있는가?
10. 미디어 쿼리나 상태 클래스가 덮고 있는가?

개발자 도구의 Styles와 Computed 영역을 함께 확인합니다.

---

# 45. 빈 공간이 남을 때 점검 순서

1. `visibility: hidden`인가?
2. `opacity: 0`인가?
3. 요소 자체는 숨겼지만 마진이 남아 있는가?
4. 부모에 고정 높이가 있는가?
5. 가상 요소가 공간을 차지하는가?
6. 절대 위치가 아닌 일반 흐름 요소인가?
7. `min-height`가 지정되어 있는가?
8. 브라우저 기본 문단 마진이 남아 있는가?
9. 투명한 자식이 공간을 유지하는가?
10. 개발자 도구 박스 모델에서 실제 크기를 확인했는가?

---

# 46. 보이지 않는 요소가 클릭될 때 점검

1. `opacity: 0`만 사용했는가?
2. `pointer-events`가 활성 상태인가?
3. 내부 링크나 버튼이 탭 순서에 남아 있는가?
4. `visibility: hidden`이 필요한가?
5. `display: none` 또는 `hidden`이 목적에 맞는가?
6. `aria-hidden`만 사용해 화면 상태와 불일치하지 않는가?
7. 닫힌 팝업이 화면 위에 겹쳐 있는가?
8. `z-index`가 높은 투명 레이어가 있는가?
9. 상태 클래스 제거가 실패했는가?
10. JavaScript 이벤트가 상위 요소에 연결되어 있는가?

---

# 47. 자주 하는 실수

## 47.1 `visibility: hidden`과 `opacity: 0`을 완전히 동일하게 이해

공간은 둘 다 유지하지만 상호작용과 접근성 동작이 다릅니다.

## 47.2 `opacity: 0`이면 클릭도 사라진다고 생각

투명한 요소의 클릭 영역은 남을 수 있습니다.

## 47.3 부모 `opacity`를 자식에서 복구하려고 함

자식 `opacity: 1`만으로 부모 합성 투명도를 취소할 수 없습니다.

## 47.4 배경만 투명하게 하려고 부모에 `opacity`

텍스트와 이미지까지 함께 투명해집니다.

## 47.5 `display: none`에 단순 전환 적용

렌더링 박스가 없어 전통적인 페이드 전환이 기대대로 작동하지 않습니다.

## 47.6 시각적 숨김에 `display: none`

스크린 리더에도 숨겨질 가능성이 높으므로 visually hidden 패턴과 목적이 다릅니다.

## 47.7 `aria-hidden`을 CSS 숨김 속성으로 이해

화면 표현을 바꾸지 않습니다.

## 47.8 비활성 버튼에 투명도만 적용

실제 클릭과 키보드 동작은 계속 가능할 수 있습니다.

## 47.9 닫힌 메뉴의 `aria-expanded` 미갱신

화면 상태와 접근성 상태가 불일치합니다.

## 47.10 낮은 투명도로 텍스트 대비 훼손

비활성 상태도 내용을 읽을 수 있어야 합니다.

---


# 종합실습

## 문제 1. 원본 결과

다음 요소 중 레이아웃 공간이 유지되는 클래스를 모두 작성하세요.

```css
.hidden {
  visibility: hidden;
}

.none {
  display: none;
}

.opacity {
  opacity: 0;
}
```

## 문제 2. 공간 제거

`.notice`를 화면과 레이아웃에서 완전히 제거하세요.

## 문제 3. 공간 유지 숨김

`.notice`의 공간은 유지하면서 보이지 않게 하세요.

## 문제 4. 완전 투명

`.notice`를 완전히 투명하게 하되 레이아웃 공간은 유지하세요.

## 문제 5. 부분 투명도

`.image`를 70% 불투명하게 작성하세요.

## 문제 6. 배경만 투명

검정 배경을 50% 불투명하게 만들되 내부 글자는 완전히 불투명하게 유지하세요.

## 문제 7. 부모와 자식

부모에 `opacity: 0.5`가 적용된 상태에서 자식에 `opacity: 1`을 지정하면 자식이 완전히 불투명해지는지 설명하세요.

## 문제 8. 투명 링크

다음 링크는 보이지 않지만 클릭될 수 있습니다. 완전히 상호작용하지 않도록 CSS를 개선하세요.

```css
.link {
  opacity: 0;
}
```

## 문제 9. HTML 숨김

다음 팝업을 HTML 속성으로 숨기세요.

```html
<div class="popup">내용</div>
```

## 문제 10. JavaScript 표시

문제 9의 팝업을 JavaScript로 다시 표시하세요.

## 문제 11. ARIA 상태

버튼으로 메뉴를 열 때 `aria-expanded`을 `true`로 변경하고 메뉴의 `hidden`을 제거하세요.

## 문제 12. visually hidden

검색 아이콘 링크에 스크린 리더용 “검색” 텍스트를 추가하고 화면에서는 숨기세요.

## 문제 13. `aria-hidden`

장식용 SVG를 스크린 리더에서 숨기세요.

## 문제 14. 잘못된 접근성

다음 코드의 문제를 설명하세요.

```html
<div aria-hidden="true">
  <button type="button">저장</button>
</div>
```

## 문제 15. 페이드 패널

닫힌 상태에서 투명하고 클릭되지 않으며 접근 가능한 탐색 대상에서도 제외되도록 `.panel`의 기본 상태를 작성하세요.

조건:

- `opacity`
- `visibility`
- `pointer-events`

사용

## 문제 16. 열린 패널

문제 15의 `.panel.is-open` 상태를 작성하세요.

## 문제 17. 움직임 감소

사용자가 움직임 감소를 선호할 때 `.panel`의 전환을 제거하세요.

## 문제 18. 비활성 버튼

버튼을 실제 비활성화하고 시각적으로 흐리게 표현하세요.

## 문제 19. 원본 설명 수정

다음 주석을 정확하게 수정하세요.

```css
/* visibility:hidden과 opacity:0은 동일하게 자리는 있으나 투명하게 만듦 */
```

## 문제 20. 원본 오타 수정

다음 주석의 오타와 표현을 수정하세요.

```css
/* 글씨,그림 모두 투명도를 민들 수 있음 */
```

## 문제 21. 다섯 문단 비교

원본과 같은 다섯 문단을 만들고 두 번째는 `visibility`, 세 번째는 `display`, 네 번째는 `opacity`로 숨기세요. 각 문단에 테두리를 추가해 공간 차이가 보이도록 하세요.

## 문제 22. 종합 메뉴 토글

다음 요구사항을 만족하는 모바일 메뉴 토글을 작성하세요.

- 실제 `<button>` 사용
- 메뉴는 처음에 `hidden`
- 버튼에 `aria-controls`
- 버튼에 `aria-expanded`
- 클릭 시 메뉴 열기·닫기
- 화면 상태와 `aria-expanded` 동기화
- 숨겨진 메뉴는 포커스 대상에서 제외
- 메뉴 링크에 키보드 포커스 표시

---

# 정답과 해설

## 정답 1

공간이 유지되는 클래스:

```text
.hidden
.opacity
```

`.none`은 `display: none`이므로 공간도 제거됩니다.

## 정답 2

```css
.notice {
  display: none;
}
```

또는 HTML 상태를 사용할 수 있습니다.

```html
<div class="notice" hidden>
  안내
</div>
```

## 정답 3

```css
.notice {
  visibility: hidden;
}
```

## 정답 4

```css
.notice {
  opacity: 0;
}
```

상호작용과 접근성 노출은 자동 제거되지 않을 수 있습니다.

## 정답 5

```css
.image {
  opacity: 0.7;
}
```

## 정답 6

```css
.card {
  color: white;
  background-color: rgb(0 0 0 / 50%);
}
```

부모 전체 `opacity`를 사용하지 않았으므로 글자는 불투명하게 유지됩니다.

## 정답 7

완전히 불투명해지지 않습니다.

```css
.parent {
  opacity: 0.5;
}

.child {
  opacity: 1;
}
```

부모와 자식 전체 결과가 부모의 0.5 불투명도로 합성됩니다.

## 정답 8

```css
.link {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}
```

레이아웃 공간까지 제거해야 한다면:

```css
.link {
  display: none;
}
```

가 더 명확합니다.

## 정답 9

```html
<div class="popup" hidden>
  내용
</div>
```

## 정답 10

```js
const popup = document.querySelector(".popup");

popup.hidden = false;
```

## 정답 11

```js
const button = document.querySelector(".menu-button");
const menu = document.querySelector("#main-menu");

menu.hidden = false;
button.setAttribute("aria-expanded", "true");
```

## 정답 12

```html
<a class="search-link" href="/search">
  <svg aria-hidden="true">...</svg>
  <span class="visually-hidden">검색</span>
</a>
```

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}
```

## 정답 13

```html
<svg aria-hidden="true">
  ...
</svg>
```

장식용 이미지라는 전제입니다.

## 정답 14

부모의 `aria-hidden="true"` 때문에 내부 버튼이 스크린 리더에서는 숨겨질 수 있지만 화면과 키보드 포커스에서는 남을 수 있습니다.

보이는 상호작용 요소와 접근성 정보가 불일치하므로 사용하면 안 됩니다.

## 정답 15

```css
.panel {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition:
    opacity 0.2s ease,
    visibility 0.2s ease;
}
```

`visibility: hidden`이 접근성과 포커스 탐색에서 숨김 상태를 보완합니다.

## 정답 16

```css
.panel.is-open {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}
```

## 정답 17

```css
@media (prefers-reduced-motion: reduce) {
  .panel {
    transition: none;
  }
}
```

## 정답 18

```html
<button
  class="submit-button"
  type="submit"
  disabled
>
  처리 중
</button>
```

```css
.submit-button:disabled {
  cursor: not-allowed;
  opacity: 0.55;
}
```

실제 `disabled` 속성이 동작을 막습니다.

## 정답 19

```css
/*
  visibility: hidden과 opacity: 0은 모두 공간을 유지하고
  화면에 보이지 않을 수 있다.
  그러나 opacity: 0은 클릭, 포커스, 접근성 노출이
  남을 수 있으므로 동작은 동일하지 않다.
*/
```

## 정답 20

```css
/*
  opacity는 글자와 이미지를 포함한 요소 전체와
  자식 요소의 불투명도에 영향을 준다.
*/
```

## 정답 21

### HTML

```html
<section class="comparison">
  <p>첫 번째</p>
  <p class="hidden">두 번째</p>
  <p class="none">세 번째</p>
  <p class="opacity">네 번째</p>
  <p>다섯 번째</p>
</section>
```

### CSS

```css
.comparison p {
  margin: 0.5rem 0;
  padding: 1rem;
  border: 1px solid #333;
}

.hidden {
  visibility: hidden;
}

.none {
  display: none;
}

.opacity {
  opacity: 0;
}
```

테두리 박스의 존재 여부를 통해 공간 차이를 확인할 수 있습니다.

## 정답 22

### HTML

```html
<button
  class="menu-button"
  type="button"
  aria-controls="mobile-menu"
  aria-expanded="false"
>
  메뉴 열기
</button>

<nav
  class="mobile-menu"
  id="mobile-menu"
  aria-label="모바일 메뉴"
  hidden
>
  <a href="/html">HTML</a>
  <a href="/css">CSS</a>
  <a href="/javascript">JavaScript</a>
</nav>
```

### CSS

```css
.mobile-menu {
  padding: 1rem;
}

.mobile-menu a {
  display: block;
  padding: 0.75rem;
}

.mobile-menu a:focus-visible,
.menu-button:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 2px;
}
```

### JavaScript

```js
const button = document.querySelector(".menu-button");
const menu = document.querySelector("#mobile-menu");

button.addEventListener("click", () => {
  const willOpen = menu.hidden;

  menu.hidden = !willOpen;

  button.setAttribute(
    "aria-expanded",
    String(willOpen)
  );

  button.textContent = willOpen
    ? "메뉴 닫기"
    : "메뉴 열기";
});
```

`hidden` 상태에서는 메뉴 링크가 일반적인 탭 순서와 접근성 탐색에서 제외됩니다.

---

# 최종 체크리스트

## 원본 개념

- [ ] `visibility: hidden`이 공간을 유지하는지 확인했다.
- [ ] `display: none`이 공간까지 제거하는지 확인했다.
- [ ] `opacity: 0`이 공간을 유지하는지 확인했다.
- [ ] `opacity: 0.3`과 `0.7`은 부분 투명도 실험값임을 이해했다.
- [ ] 다섯 문단의 실제 배치 결과를 비교했다.

## 상호작용

- [ ] `opacity: 0` 요소의 클릭 영역이 남지 않는지 확인했다.
- [ ] 보이지 않는 링크나 버튼이 탭 순서에 남지 않는지 확인했다.
- [ ] 닫힌 메뉴와 팝업의 실제 상호작용을 차단했다.
- [ ] 비활성 버튼에는 실제 `disabled` 상태를 사용했다.
- [ ] 투명도만으로 기능 상태를 표현하지 않았다.

## 접근성

- [ ] `display: none`과 `visibility: hidden`은 일반적으로 접근성 트리에서도 숨겨짐을 이해했다.
- [ ] `opacity: 0`은 자동으로 접근성에서 숨기지 않음을 확인했다.
- [ ] `aria-hidden`을 시각적 숨김 속성으로 사용하지 않았다.
- [ ] 포커스 가능한 자식이 있는 곳에 `aria-hidden="true"`를 사용하지 않았다.
- [ ] 스크린 리더 전용 텍스트에는 visually hidden 패턴을 사용했다.
- [ ] 메뉴·아코디언의 `aria-expanded`를 화면 상태와 동기화했다.

## 투명도

- [ ] `opacity` 값이 0에서 1 사이인지 확인했다.
- [ ] 부모의 `opacity`가 자식 전체에 영향을 준다는 점을 확인했다.
- [ ] 배경만 투명하게 할 때 알파 색상을 사용했다.
- [ ] 낮은 투명도로 텍스트 대비가 지나치게 약해지지 않는지 확인했다.
- [ ] 호버 효과를 키보드 포커스에서도 제공했다.

## 애니메이션

- [ ] `display: none` 자체를 단순 페이드 전환하려 하지 않았다.
- [ ] 페이드 상태에 `visibility`와 `pointer-events`를 함께 검토했다.
- [ ] 닫힌 상태의 포커스 가능성을 확인했다.
- [ ] `prefers-reduced-motion`을 고려했다.
- [ ] 애니메이션 때문에 기능 상태가 지연되지 않는지 확인했다.

## 원본 코드 검수

- [ ] `lang="en"`을 `lang="ko"`로 개선했다.
- [ ] `title`을 학습 내용에 맞게 작성했다.
- [ ] 주석의 `민들` 오타를 수정했다.
- [ ] “보통 display를 주로 사용”이라는 설명을 목적별 선택으로 보완했다.
- [ ] `visibility`와 `opacity`가 완전히 동일하지 않다고 설명했다.
- [ ] 내 코드와 강사님 코드의 부분 투명도 값 차이를 오류로 처리하지 않았다.

---

# 핵심 요약

- 원본 CSS 05는 `visibility: hidden`, `display: none`, `opacity: 0`을 다섯 문단으로 비교한다.
- `visibility: hidden`은 요소를 보이지 않게 하지만 레이아웃 공간은 유지한다.
- `display: none`은 요소가 렌더링 박스를 만들지 않아 공간도 제거한다.
- `opacity: 0`은 요소를 완전히 투명하게 하지만 박스는 계속 존재한다.
- `visibility: hidden`과 `opacity: 0`은 공간이 남는다는 공통점만 있을 뿐 동작이 완전히 같지는 않다.
- `opacity: 0` 요소는 포인터 이벤트, 키보드 포커스, 접근성 노출이 남을 수 있다.
- `display: none`과 `visibility: hidden` 요소는 일반적으로 접근성 트리에서도 숨겨진다.
- `opacity`는 텍스트, 이미지, 테두리와 모든 자식 요소에 함께 영향을 준다.
- 부모의 `opacity`는 자식의 `opacity: 1`만으로 취소할 수 없다.
- 배경만 반투명하게 만들려면 요소 전체 `opacity`가 아니라 알파 채널 색상을 사용한다.
- HTML `hidden` 속성은 현재 표시되지 않는 상태를 명확하게 표현할 수 있다.
- `aria-hidden`은 보조 기술에서 숨기는 속성이며 화면 표현을 자동으로 바꾸지 않는다.
- 화면에는 숨기고 스크린 리더에는 제공하려면 visually hidden 패턴을 사용한다.
- 페이드 전환에는 `opacity`와 함께 `visibility`, `pointer-events`를 관리해야 한다.
- `display: none`은 전통적인 단순 전환으로 부드럽게 보간되지 않는다.
- 비활성 상태는 투명도만 낮추지 말고 실제 `disabled` 또는 동작 차단을 함께 적용한다.
- 메뉴와 아코디언은 표시 상태와 `aria-expanded`를 동기화해야 한다.
- 내 코드의 `민들`은 주석 오타이며, `visibility`와 `opacity`를 동일하다고 한 설명은 실무 관점에서 보완해야 한다.
- 강사님 코드의 `opacity: 0.7`과 내 코드의 `opacity: 0.3`은 서로 다른 부분 투명도 실험값이다.
- 숨김 방식은 공간, 상호작용, 접근성, 애니메이션 목적에 따라 선택해야 한다.
