# CSS 미디어 쿼리와 반응형 메뉴

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `14_CSS_미디어쿼리와_반응형.md` |
| 분류 | `02_CSS` |
| 권장 선수 학습 | `13_CSS_Transform과_요소변형.md` |
| 다음 학습 | 이후 CSS 원본 순서 확인 |
| 원본 기준 | `workspace_me/workspace_html/css/14_media.html`, `workspace_teacher/workspace_html/css/14_media.html` |
| 핵심 범위 | `@media`, `screen`, `max-width`, `min-width`, 모바일 메뉴, 인접 형제 선택자, `opacity`, 반응형 레이아웃 |
| 프로젝트 연결 | 모바일 내비게이션, 햄버거 메뉴, 브레이크포인트, 데스크톱·모바일 UI 전환 |

> 내 코드와 강사님 코드의 `14_media.html`은 내용이 완전히 동일합니다. 이 문서는 동일한 원본을 중복 비교하지 않고, 공통 코드의 의도와 문제점을 분석합니다. 원본의 오류나 한계는 조용히 수정하지 않고 그대로 보존한 뒤 개선 방향을 설명합니다.

---

# 학습 목표

- 미디어 쿼리가 특정 미디어 환경이나 화면 조건에서 CSS를 선택적으로 적용하는 기능임을 설명한다.
- `@media screen and (max-width: 600px)`의 의미를 이해한다.
- `max-width`와 `min-width`의 차이를 구분한다.
- 데스크톱 메뉴를 모바일 세로 메뉴로 변경한다.
- 요소를 `display: none`과 `display: inline`으로 전환하는 원리를 이해한다.
- `opacity: 0`이 요소를 완전히 제거하지 않는다는 점을 설명한다.
- `position: relative`와 `top`을 이용한 시각적 이동을 이해한다.
- `span:hover + ul`의 인접 형제 선택자 구조를 설명한다.
- hover 상태에 transition을 둘 때 닫힘 전환이 즉시 될 수 있음을 이해한다.
- 모바일에서 hover에만 의존하는 메뉴의 한계를 설명한다.
- 메뉴 열기 요소에는 `span`보다 `button`이 적절한 이유를 이해한다.
- 내 코드와 강사님 코드가 동일하다는 점을 정확히 기록한다.
- 접근성, 키보드 조작, 터치 환경을 고려한 반응형 메뉴로 개선한다.

---

# 1. 반응형 웹이란?

반응형 웹은 화면 크기와 입력 환경에 맞춰 레이아웃과 인터페이스를 조정하는 방식입니다.

예:

```text
넓은 화면
→ 메뉴를 가로로 배치

좁은 화면
→ 메뉴를 세로로 배치
→ 메뉴 열기 버튼 표시
```

반응형 디자인은 단순히 요소 크기를 줄이는 것이 아닙니다.

다음 항목을 함께 고려합니다.

- 콘텐츠 읽기 순서
- 메뉴 조작 방법
- 터치 영역
- 글자 크기
- 이미지 크기
- 가로 스크롤
- 키보드 접근성
- 화면 방향

---

# 2. 미디어 쿼리 기본 문법

```css
@media media-type and (condition) {
  /* 조건을 만족할 때 적용할 CSS */
}
```

원본:

```css
@media screen 
and (max-width: 600px)
{
  ...
}
```

한 줄로 작성할 수도 있습니다.

```css
@media screen and (max-width: 600px) {
  ...
}
```

---

# 3. 원본 미디어 타입 `screen`

```css
@media screen and (max-width: 600px)
```

`screen`은 화면 장치를 대상으로 합니다.

대표 미디어 타입:

```text
all
screen
print
```

현재는 미디어 타입을 생략하고 조건만 작성하는 경우도 많습니다.

```css
@media (max-width: 600px) {
  ...
}
```

원본의 `screen` 사용은 문법적으로 올바릅니다.

---

# 4. `max-width: 600px`

```css
@media (max-width: 600px)
```

뷰포트 너비가 600px 이하일 때 내부 CSS가 적용됩니다.

```text
600px 이하 → 미디어 쿼리 적용
601px 이상 → 기본 CSS 적용
```

경계값인 600px도 조건에 포함됩니다.

---

# 5. 원본의 주석 처리된 `min-width`

```css
/* and (min-width: 500px) */
```

주석을 해제하면 조건은 다음과 같습니다.

```css
@media screen
and (max-width: 600px)
and (min-width: 500px)
```

적용 범위:

```text
500px 이상
그리고
600px 이하
```

즉, 500px부터 600px 사이에서만 적용됩니다.

---

# 6. `max-width`와 `min-width`

## `max-width`

```css
@media (max-width: 600px)
```

화면이 600px 이하일 때 적용합니다.

작은 화면을 대상으로 하는 규칙에서 자주 사용합니다.

## `min-width`

```css
@media (min-width: 600px)
```

화면이 600px 이상일 때 적용합니다.

모바일 우선 설계에서 넓은 화면을 확장할 때 자주 사용합니다.

---

# 7. 데스크톱 우선과 모바일 우선

원본은 기본 상태가 가로 메뉴이고, 600px 이하에서 세로 메뉴로 변경됩니다.

```text
기본 CSS → 데스크톱 형태
max-width 미디어 쿼리 → 모바일 형태
```

이를 데스크톱 우선 방식으로 볼 수 있습니다.

모바일 우선 예:

```css
li {
  display: block;
  width: 100%;
}

@media (min-width: 601px) {
  li {
    display: inline-block;
    width: 100px;
  }
}
```

어느 방식이 무조건 정답인 것은 아니지만 프로젝트 전체에서 기준을 일관되게 유지합니다.

---

# 8. 원본 기본 `ul`

```css
ul {
  border: 1px solid blue;
  list-style: none;
  padding-left: 0;
}
```

각 속성의 역할:

```text
border
→ 메뉴 목록 범위 확인

list-style: none
→ 기본 글머리표 제거

padding-left: 0
→ 브라우저 기본 왼쪽 들여쓰기 제거
```

브라우저 기본 `ul`에는 위·아래 margin도 있을 수 있습니다.

완전히 초기화하려면:

```css
ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
```

---

# 9. 원본 기본 `li`

```css
li {
  border: 1px solid red;
  display: inline-block;
  width: 100px;
  height: 50px;
  line-height: 50px;
  text-align: center;
}
```

결과:

- 각 메뉴 항목이 가로로 배치된다.
- 각 항목의 콘텐츠 너비는 100px이다.
- 높이는 50px이다.
- 텍스트가 가로 중앙에 놓인다.
- `line-height: 50px`로 한 줄 텍스트를 세로 중앙에 가까이 배치한다.

---

# 10. `inline-block` 메뉴

`inline-block`은 인라인처럼 한 줄에 배치되면서 width와 height를 가질 수 있습니다.

```css
li {
  display: inline-block;
}
```

원본 메뉴:

```html
<li>메일</li>
<li>블로그</li>
<li>웹툰</li>
<li>카페</li>
```

넓은 화면에서는 한 줄에 배치됩니다.

---

# 11. Inline-block 사이 공백

HTML 줄바꿈과 들여쓰기는 inline-block 사이에 작은 공백을 만들 수 있습니다.

```html
<li>메일</li>
<li>블로그</li>
```

각 메뉴가 정확히 붙어야 한다면 Flexbox가 더 명확할 수 있습니다.

```css
ul {
  display: flex;
}
```

원본은 inline-block 학습 구조를 그대로 보존합니다.

---

# 12. `line-height` 세로 중앙 정렬

원본:

```css
height: 50px;
line-height: 50px;
```

한 줄 텍스트에서 줄 높이와 박스 높이를 같게 지정해 세로 중앙처럼 보이게 합니다.

한계:

- 텍스트가 두 줄이면 깨진다.
- 폰트와 브라우저에 따라 시각적 중앙이 다를 수 있다.
- 아이콘과 텍스트 조합에 불편하다.

현대적인 방식:

```css
li {
  display: grid;
  place-items: center;
}
```

또는 실제 링크에 Flexbox를 사용합니다.

---

# 13. 원본 기본 `span`

```css
span {
  display: none;
}
```

넓은 화면에서는 햄버거 메뉴 문구를 숨깁니다.

HTML:

```html
<span>햄버거 메뉴(메뉴열기)</span>
```

모바일 미디어 쿼리 안에서 다시 표시합니다.

---

# 14. 모바일에서 메뉴 항목 변경

```css
li {
  display: block;
  width: 100%;
}
```

모바일에서는 메뉴 항목이 세로로 배치됩니다.

```text
메일
블로그
웹툰
카페
```

`display: block`으로 한 줄씩 배치하고 `width: 100%`로 부모 너비를 채웁니다.

---

# 15. `width: 100%`와 Border

원본은 기본 `box-sizing: content-box`입니다.

```css
li {
  width: 100%;
  border: 1px solid red;
}
```

실제 바깥 너비는 다음처럼 될 수 있습니다.

```text
콘텐츠 너비 100%
+ 왼쪽 border 1px
+ 오른쪽 border 1px
```

부모 너비보다 2px 넓어져 가로 overflow가 발생할 수 있습니다.

개선:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

또는:

```css
li {
  width: auto;
}
```

---

# 16. 모바일에서 Span 표시

```css
span {
  display: inline;
}
```

600px 이하에서 햄버거 메뉴 문구를 표시합니다.

원본은 `inline`을 사용합니다.

버튼 형태라면 다음이 더 적절할 수 있습니다.

```css
.menu-button {
  display: inline-flex;
}
```

---

# 17. 모바일 `ul` 숨김 방식

원본:

```css
ul {
  /* display: none; */
  opacity: 0;
  position: relative;
  top: -20px;
}
```

주석 처리된 `display: none` 대신 opacity와 위치 이동을 사용합니다.

초기 모바일 상태:

```text
투명도 0
원래 위치보다 위로 20px 이동
레이아웃 공간은 유지
```

---

# 18. `opacity: 0`의 중요한 특징

```css
opacity: 0;
```

보이지 않지만 요소 자체는 남아 있습니다.

따라서:

- 레이아웃 공간을 차지한다.
- 링크가 있다면 키보드 포커스를 받을 수 있다.
- 포인터 이벤트를 받을 수 있다.
- 화면 읽기 프로그램에서 접근될 수 있다.
- `display: none`처럼 제거되지 않는다.

원본의 `li`에는 링크가 없지만 실제 내비게이션으로 확장하면 숨겨진 메뉴가 조작될 수 있습니다.

---

# 19. `display: none`과 비교

| 속성 | 화면 표시 | 공간 | 포인터 | 키보드·접근성 트리 |
| --- | --- | --- | --- | --- |
| `display: none` | 숨김 | 제거 | 불가 | 일반적으로 제거 |
| `opacity: 0` | 투명 | 유지 | 가능 | 유지 |
| `visibility: hidden` | 숨김 | 유지 | 일반적으로 불가 | 접근 제한 가능 |

Transition을 위해 opacity를 사용한다면 다른 상태도 함께 관리해야 합니다.

```css
.menu {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}
```

열린 상태:

```css
.menu.is-open {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}
```

---

# 20. `position: relative`와 `top`

원본:

```css
position: relative;
top: -20px;
```

요소의 원래 레이아웃 공간은 유지하면서 화면상 위치만 위로 20px 이동합니다.

열릴 때:

```css
top: 0px;
```

원래 시각적 위치로 돌아옵니다.

Transform을 사용하면 의도가 더 명확할 수 있습니다.

```css
transform: translateY(-20px);
```

열린 상태:

```css
transform: translateY(0);
```

---

# 21. 원본 인접 형제 선택자

```css
span:hover + ul
```

의미:

```text
hover 중인 span의
바로 다음 형제 ul
```

HTML 구조가 정확히 다음과 같아야 합니다.

```html
<span>메뉴 열기</span>
<ul>...</ul>
```

중간에 다른 요소가 들어가면 선택되지 않습니다.

```html
<span>메뉴 열기</span>
<p>설명</p>
<ul>...</ul>
```

이 구조에서는 `+ ul`이 동작하지 않습니다.

---

# 22. 원본 Hover 상태

```css
span:hover + ul {
  transition: all .5s;
  /* display: block; */
  opacity: 1;
  top: 0px;
}
```

span에 마우스를 올리면 바로 뒤의 ul이 보입니다.

전환되는 값:

```text
opacity: 0 → 1
top: -20px → 0
```

---

# 23. Transition 위치 문제

원본은 transition을 열린 hover 상태에만 작성합니다.

```css
span:hover + ul {
  transition: all .5s;
}
```

결과:

```text
메뉴 열림
→ 0.5초 동안 전환 가능

hover 해제
→ transition 선언도 사라짐
→ 즉시 닫힐 수 있음
```

CSS 12에서 학습한 문제와 같습니다.

양방향 전환을 원하면 기본 `ul`에 작성합니다.

```css
ul {
  transition:
    opacity 0.5s,
    transform 0.5s;
}
```

---

# 24. `transition: all` 개선

원본:

```css
transition: all .5s;
```

실제로 변화시키는 속성만 작성하는 편이 좋습니다.

```css
transition:
  opacity 0.5s,
  transform 0.5s;
```

`top`보다 transform을 사용하면 레이아웃 계산 부담을 줄이는 데 유리할 수 있습니다.

---

# 25. 원본 메뉴가 유지되지 않는 문제

선택자는 다음과 같습니다.

```css
span:hover + ul
```

마우스를 span에서 ul로 이동하면 span의 hover가 해제됩니다.

그러면 메뉴가 즉시 닫히거나 사라져 메뉴 항목을 클릭하기 어려울 수 있습니다.

```text
span에 마우스 올림
→ 메뉴 표시

메뉴로 포인터 이동
→ span hover 해제
→ 메뉴 숨김
```

이는 원본 예제의 가장 중요한 실사용 한계입니다.

---

# 26. Hover 영역 확장 방법

CSS만 사용하는 간단한 방법으로 공통 부모에 hover를 적용할 수 있습니다.

```html
<nav class="menu">
  <button class="menu__button">
    메뉴 열기
  </button>

  <ul class="menu__list">
    ...
  </ul>
</nav>
```

```css
.menu:hover .menu__list,
.menu:focus-within .menu__list {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
```

부모 내부에 포인터가 있는 동안 메뉴가 유지됩니다.

하지만 모바일 터치와 열린 상태 관리에는 JavaScript 버튼 방식이 더 명확합니다.

---

# 27. 모바일에서 Hover의 한계

터치 환경에는 전통적인 마우스 hover가 없습니다.

브라우저에 따라:

- 첫 탭이 hover처럼 동작할 수 있다.
- 한 번 열린 상태가 유지될 수 있다.
- 전혀 예상과 다르게 동작할 수 있다.
- 메뉴 항목을 선택하기 전에 닫힐 수 있다.

모바일 햄버거 메뉴의 핵심 동작을 hover에만 의존하면 안 됩니다.

---

# 28. `span`의 의미 문제

원본:

```html
<span>햄버거 메뉴(메뉴열기)</span>
```

`span`은 일반 인라인 텍스트 요소입니다.

기본적으로:

- 키보드 Tab 포커스를 받지 않는다.
- Enter·Space로 실행되지 않는다.
- 버튼 역할이 전달되지 않는다.
- 열린 상태를 표현할 수 없다.

실제 메뉴 열기에는 `button`을 사용합니다.

---

# 29. 접근 가능한 메뉴 버튼

```html
<button
  class="menu-button"
  type="button"
  aria-expanded="false"
  aria-controls="primary-menu"
>
  메뉴 열기
</button>
```

의미:

```text
aria-expanded
→ 메뉴가 열렸는지 전달

aria-controls
→ 어떤 메뉴를 제어하는지 연결
```

열린 상태에서는 JavaScript가 다음처럼 변경합니다.

```html
aria-expanded="true"
```

---

# 30. 원본 `li`에 링크가 없음

원본:

```html
<li>메일</li>
```

실제 메뉴라면 링크가 필요합니다.

```html
<li>
  <a href="/mail">메일</a>
</li>
```

클릭 가능한 영역을 항목 전체로 만들려면 링크에 레이아웃을 적용합니다.

```css
.menu__link {
  display: flex;
  min-height: 50px;
  align-items: center;
  justify-content: center;
}
```

---

# 31. 시맨틱 내비게이션

```html
<nav aria-label="주요 메뉴">
  <ul>
    ...
  </ul>
</nav>
```

`nav`는 주요 탐색 영역임을 나타냅니다.

페이지에 여러 nav가 있으면 `aria-label`로 목적을 구분합니다.

```html
<nav aria-label="상단 주요 메뉴">
```

---

# 32. CSS만 사용하는 Focus-within 예제

```css
.menu__list {
  opacity: 0;
  visibility: hidden;
  transform: translateY(-1rem);
  transition:
    opacity 0.2s ease,
    transform 0.2s ease,
    visibility 0s linear 0.2s;
}

.menu:hover .menu__list,
.menu:focus-within .menu__list {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
  transition-delay: 0s;
}
```

키보드로 버튼이나 링크에 포커스가 있는 동안 메뉴가 유지됩니다.

다만 열린 상태를 명시적으로 토글하는 버튼과 JavaScript 방식이 사용자 제어에 더 적합합니다.

---

# 33. JavaScript 토글 방식

HTML:

```html
<button
  class="menu-button"
  type="button"
  aria-expanded="false"
  aria-controls="primary-menu"
>
  메뉴 열기
</button>

<ul id="primary-menu" hidden>
  ...
</ul>
```

JavaScript:

```js
const button =
  document.querySelector(".menu-button");

const menu =
  document.querySelector("#primary-menu");

button.addEventListener("click", () => {
  const isOpen =
    button.getAttribute("aria-expanded")
    === "true";

  button.setAttribute(
    "aria-expanded",
    String(!isOpen)
  );

  menu.hidden = isOpen;
});
```

이 방식은 터치, 마우스, 키보드에서 명확하게 동작합니다.

---

# 34. `hidden`과 Transition

`hidden`은 보통 `display: none` 효과를 가지므로 opacity 전환이 바로 동작하지 않습니다.

부드러운 애니메이션이 필요하다면 상태 클래스로 다음을 함께 관리할 수 있습니다.

```css
.menu__list {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(-0.75rem);
}

.menu__list.is-open {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: translateY(0);
}
```

접근성 트리와 focus 관리까지 구현 목적에 맞게 확인해야 합니다.

---

# 35. 메뉴 닫기 동작

실제 모바일 메뉴에는 다음 동작을 검토합니다.

- 버튼을 다시 누르면 닫기
- Escape 키로 닫기
- 메뉴 바깥 클릭 시 닫기
- 메뉴 링크 선택 후 닫기
- 화면이 데스크톱 크기로 바뀌면 상태 초기화
- focus가 보이지 않는 곳에 남지 않도록 관리

원본은 미디어 쿼리와 hover 학습이 목적이므로 이러한 동작은 포함하지 않습니다.

---

# 36. 브레이크포인트 선택

원본:

```css
max-width: 600px
```

600px은 학습용 고정값입니다.

실무에서 브레이크포인트는 특정 기기 이름보다 콘텐츠가 깨지는 지점을 기준으로 선택합니다.

```text
메뉴가 한 줄에 들어가지 않음
→ 그 직전 너비에서 모바일 메뉴로 전환
```

디자인 시스템에서는 공통 변수를 사용할 수도 있습니다.

CSS 미디어 쿼리에서는 일반 사용자 지정 속성을 조건값으로 직접 사용하는 데 제한이 있으므로 빌드 도구나 사전 처리기를 활용하기도 합니다.

---

# 37. 뷰포트 Meta 태그

원본:

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1.0"
>
```

모바일 브라우저가 페이지의 CSS 픽셀 너비를 기기 화면 너비에 맞추도록 합니다.

반응형 페이지에서 매우 중요합니다.

이 태그가 없으면 모바일에서 미디어 쿼리가 예상과 다르게 보일 수 있습니다.

---

# 38. 화면 너비와 요소 너비

미디어 쿼리의 `width`는 일반적으로 뷰포트 조건을 검사합니다.

```css
@media (max-width: 600px)
```

특정 컴포넌트의 부모 너비가 아니라 전체 뷰포트를 기준으로 합니다.

컴포넌트 자체의 공간에 따라 스타일을 바꾸려면 Container Query를 검토할 수 있습니다.

---

# 39. Container Query 확장 학습

```css
.card-wrapper {
  container-type: inline-size;
}
```

```css
@container (max-width: 30rem) {
  .card {
    grid-template-columns: 1fr;
  }
}
```

원본에는 없는 확장 개념입니다.

페이지 전체 너비가 아니라 컴포넌트가 놓인 실제 공간에 따라 스타일을 변경할 수 있습니다.

---

# 40. 화면 방향 조건

```css
@media (orientation: landscape) {
  ...
}
```

```css
@media (orientation: portrait) {
  ...
}
```

화면 방향만으로 레이아웃을 결정하기보다 실제 사용 가능한 너비와 콘텐츠를 함께 고려합니다.

---

# 41. Hover 가능 여부 조건

```css
@media (hover: hover) and (pointer: fine) {
  .menu-item:hover {
    ...
  }
}
```

정밀 포인터와 hover를 지원하는 환경에만 hover 효과를 적용할 수 있습니다.

터치 중심 환경:

```css
@media (hover: none) {
  ...
}
```

원본처럼 모바일 메뉴의 핵심 열기 기능을 hover에 맡기는 것보다 버튼 토글을 사용합니다.

---

# 42. Reduced Motion

메뉴의 이동과 opacity transition을 줄일 수 있습니다.

```css
@media (prefers-reduced-motion: reduce) {
  .menu__list {
    transition: none;
  }
}
```

메뉴 기능은 유지하고 장식적 움직임만 제거합니다.

---

# 43. Print 미디어 쿼리

```css
@media print {
  .menu-button,
  nav {
    display: none;
  }
}
```

화면용 내비게이션을 인쇄물에서 숨길 수 있습니다.

원본의 `screen` 미디어 타입과 연결되는 확장 학습입니다.

---

# 44. 원본 문서 언어와 제목

내 코드와 강사님 코드:

```html
<html lang="en">
<title>Document</title>
```

본문은 한국어이므로:

```html
<html lang="ko">
<title>CSS 미디어 쿼리</title>
```

로 개선합니다.

---

# 45. 내 코드와 강사님 코드 동일성

두 파일의 HTML과 CSS는 문자 내용 기준으로 동일합니다.

동일한 항목:

- 문서 구조
- viewport meta
- `ul`, `li`, `span` 스타일
- `max-width: 600px`
- 주석 처리된 `min-width: 500px`
- `opacity: 0`
- `position: relative`
- `top: -20px`
- `span:hover + ul`
- `transition: all .5s`
- 메뉴 문구와 항목

따라서 My Code vs Teacher Code에서 존재하지 않는 차이를 만들어서는 안 됩니다.

---

# 46. 공통 코드의 장점

- 미디어 쿼리의 기본 문법을 간단하게 보여 준다.
- 넓은 화면의 가로 메뉴를 좁은 화면에서 세로 메뉴로 전환한다.
- `max-width`와 주석 처리된 `min-width`를 함께 실험할 수 있다.
- `display: none` 대신 opacity를 사용해 transition 가능성을 실습한다.
- 인접 형제 선택자 `+`를 실제 UI 변화에 연결한다.
- viewport meta 태그가 포함되어 있다.
- 코드가 짧아 브라우저 크기를 조절하며 결과를 확인하기 쉽다.

---

# 47. 공통 코드의 개선점

- `span`은 실제 메뉴 버튼으로 적절하지 않다.
- 메뉴 항목이 링크가 아니다.
- 모바일 핵심 기능을 hover에 의존한다.
- span에서 ul로 이동하면 hover가 해제되어 메뉴 사용이 어렵다.
- opacity 0인 메뉴가 공간과 상호작용 가능성을 유지한다.
- transition이 hover 상태에만 있어 닫힐 때 즉시 사라질 수 있다.
- `transition: all`이 불필요하게 넓다.
- `top`보다 transform이 전환에 더 적절할 수 있다.
- 모바일 `li width: 100%`에 border가 더해져 overflow 가능성이 있다.
- inline-block 사이 공백이 생길 수 있다.
- `line-height` 세로 중앙은 한 줄 텍스트에만 적합하다.
- `ul` 기본 margin을 제거하지 않았다.
- 문서 언어와 제목이 콘텐츠에 맞지 않는다.

---

# 48. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 파일명 | `14_media.html` | `14_media.html` |
| HTML | 동일 | 동일 |
| CSS | 동일 | 동일 |
| 주석 | 동일 | 동일 |
| 메뉴 문구 | 동일 | 동일 |
| 브레이크포인트 | `600px` | `600px` |
| 숨김 방식 | opacity | opacity |
| 열기 방식 | `span:hover + ul` | `span:hover + ul` |
| 차이 | 없음 | 없음 |

> 이번 문서는 내 코드와 강사님 코드가 동일하므로 장단점을 억지로 분리하지 않습니다. 공통 코드 분석과 개선안을 중심으로 학습합니다.

---

# 49. 원본 보존 코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >
  <title>Document</title>

  <style>
    ul {
      border: 1px solid blue;
      list-style: none;
      padding-left: 0;
    }

    li {
      border: 1px solid red;
      display: inline-block;
      width: 100px;
      height: 50px;
      line-height: 50px;
      text-align: center;
    }

    span {
      display: none;
    }

    @media screen
    and (max-width: 600px)
    /* and (min-width: 500px) */
    {
      li {
        display: block;
        width: 100%;
      }

      span {
        display: inline;
      }

      ul {
        /* display: none; */
        opacity: 0;
        position: relative;
        top: -20px;
      }

      span:hover + ul {
        transition: all .5s;
        /* display: block; */
        opacity: 1;
        top: 0px;
      }
    }
  </style>
</head>

<body>
  <span>햄버거 메뉴(메뉴열기)</span>

  <ul>
    <li>메일</li>
    <li>블로그</li>
    <li>웹툰</li>
    <li>카페</li>
  </ul>
</body>
</html>
```

---

# 50. CSS 중심 개선 예제

이 예제는 원본의 형제 구조를 최대한 유지하되 hover와 focus 문제를 줄입니다.

## HTML

```html
<nav class="menu" aria-label="주요 메뉴">
  <button
    class="menu__button"
    type="button"
    aria-expanded="false"
    aria-controls="primary-menu"
  >
    메뉴 열기
  </button>

  <ul class="menu__list" id="primary-menu">
    <li>
      <a href="/mail">메일</a>
    </li>
    <li>
      <a href="/blog">블로그</a>
    </li>
    <li>
      <a href="/webtoon">웹툰</a>
    </li>
    <li>
      <a href="/cafe">카페</a>
    </li>
  </ul>
</nav>
```

## CSS

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: sans-serif;
}

.menu__button {
  display: none;
}

.menu__list {
  display: flex;
  margin: 0;
  padding: 0;
  border: 1px solid blue;
  list-style: none;
}

.menu__list a {
  display: flex;
  min-width: 100px;
  min-height: 50px;
  align-items: center;
  justify-content: center;
  border: 1px solid red;
  color: inherit;
  text-decoration: none;
}

.menu__list a:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: -3px;
}

@media (max-width: 600px) {
  .menu__button {
    display: inline-flex;
    min-height: 44px;
    align-items: center;
  }

  .menu__list {
    flex-direction: column;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transform: translateY(-20px);
    transition:
      opacity 0.2s ease,
      transform 0.2s ease;
  }

  .menu:hover .menu__list,
  .menu:focus-within .menu__list {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transform: translateY(0);
  }

  .menu__list a {
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .menu__list {
    transition: none;
  }
}
```

이 방식도 CSS hover와 focus 기반이므로 실제 모바일 메뉴에는 JavaScript 토글을 권장합니다.

---

# 51. 실무형 버튼 토글 예제

## HTML

```html
<nav class="site-nav" aria-label="주요 메뉴">
  <button
    class="site-nav__toggle"
    type="button"
    aria-expanded="false"
    aria-controls="site-menu"
  >
    <span aria-hidden="true">☰</span>
    <span class="site-nav__toggle-text">
      메뉴
    </span>
  </button>

  <ul class="site-nav__menu" id="site-menu">
    <li>
      <a href="/mail">메일</a>
    </li>
    <li>
      <a href="/blog">블로그</a>
    </li>
    <li>
      <a href="/webtoon">웹툰</a>
    </li>
    <li>
      <a href="/cafe">카페</a>
    </li>
  </ul>
</nav>
```

## CSS

```css
.site-nav__toggle {
  display: none;
}

.site-nav__menu {
  display: flex;
  margin: 0;
  padding: 0;
  list-style: none;
}

.site-nav__menu a {
  display: flex;
  min-width: 100px;
  min-height: 50px;
  align-items: center;
  justify-content: center;
  color: inherit;
  text-decoration: none;
}

@media (max-width: 600px) {
  .site-nav__toggle {
    display: inline-flex;
    min-width: 44px;
    min-height: 44px;
    align-items: center;
    gap: 0.5rem;
  }

  .site-nav__menu {
    display: none;
    flex-direction: column;
  }

  .site-nav__toggle[aria-expanded="true"]
  + .site-nav__menu {
    display: flex;
  }
}
```

## JavaScript

```js
const toggle =
  document.querySelector(".site-nav__toggle");

toggle.addEventListener("click", () => {
  const isOpen =
    toggle.getAttribute("aria-expanded")
    === "true";

  toggle.setAttribute(
    "aria-expanded",
    String(!isOpen)
  );
});
```

---

# 52. 모바일 우선 개선 예제

```css
.site-nav__toggle {
  display: inline-flex;
}

.site-nav__menu {
  display: none;
  flex-direction: column;
}

.site-nav__toggle[aria-expanded="true"]
+ .site-nav__menu {
  display: flex;
}

@media (min-width: 601px) {
  .site-nav__toggle {
    display: none;
  }

  .site-nav__menu {
    display: flex;
    flex-direction: row;
  }
}
```

기본을 모바일로 작성하고 넓은 화면에서 확장합니다.

---

# 53. Breakpoint에서 상태 초기화

모바일에서 메뉴를 연 뒤 화면을 넓혔다가 다시 줄일 때 상태가 예상과 다를 수 있습니다.

CSS 구조를 다음처럼 만들면 데스크톱에서는 `aria-expanded` 값과 관계없이 메뉴를 표시할 수 있습니다.

```css
@media (min-width: 601px) {
  .site-nav__menu {
    display: flex;
  }
}
```

JavaScript로 화면 변화에 따라 상태를 초기화할 수도 있지만 꼭 필요한지 먼저 판단합니다.

---

# 54. 터치 영역

모바일 버튼과 링크는 충분한 클릭 영역을 제공합니다.

```css
.menu-button,
.menu-link {
  min-width: 44px;
  min-height: 44px;
}
```

44px은 흔히 참고하는 목표 크기이며 프로젝트 지침과 사용자 환경에 맞게 확인합니다.

텍스트가 작더라도 실제 클릭 영역은 충분해야 합니다.

---

# 55. 메뉴 아이콘 접근성

아이콘과 텍스트를 함께 제공:

```html
<button type="button">
  <span aria-hidden="true">☰</span>
  <span>메뉴 열기</span>
</button>
```

아이콘만 사용할 경우 접근 가능한 이름을 제공합니다.

```html
<button
  type="button"
  aria-label="주요 메뉴 열기"
>
  <span aria-hidden="true">☰</span>
</button>
```

열린 상태에서 label을 “메뉴 닫기”로 바꾸는 것도 검토합니다.

---

# 56. 메뉴가 보이지 않을 때 점검

1. 현재 뷰포트가 600px 이하인가?
2. viewport meta 태그가 있는가?
3. `span`과 `ul`이 바로 인접한 형제인가?
4. span 위에 실제 hover가 발생하는가?
5. `opacity: 0`이 다른 규칙에 의해 유지되는가?
6. transition만 있고 opacity 1 규칙이 없는가?
7. 미디어 쿼리 괄호가 올바른가?
8. 다른 CSS가 `display: none`을 적용하는가?
9. 터치 환경에서 hover를 기대하고 있는가?
10. 개발자 도구에서 미디어 쿼리 활성 상태를 확인했는가?

---

# 57. 메뉴가 클릭되지 않을 때 점검

1. span에서 ul로 이동하며 hover가 해제되는가?
2. opacity 0 요소가 포인터를 가로막는가?
3. 메뉴 항목에 실제 링크가 있는가?
4. `pointer-events: none`이 열린 상태에서도 남아 있는가?
5. 다른 요소의 z-index가 메뉴보다 높은가?
6. 부모 overflow에 메뉴가 잘리는가?
7. 모바일에서 hover 동작을 사용하고 있는가?
8. 버튼에 click 이벤트가 연결됐는가?
9. `aria-expanded`와 CSS 선택자가 일치하는가?
10. 키보드 Enter와 Space로 조작 가능한가?

---

# 58. 가로 Overflow 점검

1. `li { width: 100%; }`에 border가 추가됐는가?
2. `box-sizing: border-box`가 적용됐는가?
3. ul의 기본 padding이 남아 있는가?
4. body 기본 margin이 영향을 주는가?
5. 긴 메뉴 문구가 줄바꿈되지 않는가?
6. 고정 너비 100px 항목이 좁은 화면에 남아 있는가?
7. inline-block 공백이 총너비에 더해지는가?
8. 메뉴 아이콘이 바깥으로 이동했는가?
9. transform 이동이 화면 밖으로 나가는가?
10. body에 무조건 overflow-x hidden을 적용하려는가?

---

# 59. 자주 하는 실수

## 59.1 모바일 메뉴를 Hover로만 열기

터치와 키보드 환경에서 안정적으로 사용할 수 없습니다.

## 59.2 Span을 버튼처럼 사용

키보드 조작과 역할 전달이 부족합니다.

## 59.3 Opacity 0이면 완전히 숨겨졌다고 생각

공간, 포인터, focus 가능성이 남을 수 있습니다.

## 59.4 Transition을 Hover 상태에만 작성

열릴 때만 부드럽고 닫힐 때 즉시 사라질 수 있습니다.

## 59.5 `transition: all`

의도하지 않은 속성까지 전환될 수 있습니다.

## 59.6 Width 100%와 Border 계산 누락

기본 content-box에서 부모보다 넓어질 수 있습니다.

## 59.7 메뉴 항목을 Link 없이 작성

실제 내비게이션 기능과 의미가 없습니다.

## 59.8 Breakpoint를 기기 이름만으로 선택

콘텐츠가 실제로 깨지는 지점을 기준으로 검토합니다.

## 59.9 `line-height`를 다중 행 중앙 정렬에 사용

텍스트가 두 줄이 되면 레이아웃이 깨질 수 있습니다.

## 59.10 내 코드와 강사님 코드에 없는 차이를 만들어 냄

이번 원본은 완전히 동일하므로 공통 분석으로 처리해야 합니다.

---

# 60. 면접·복습 포인트

## Q1. 미디어 쿼리란 무엇인가요?

화면 너비, 출력 매체, 사용자 환경 같은 조건에 따라 CSS를 선택적으로 적용하는 기능입니다.

## Q2. `max-width: 600px`은 무엇을 의미하나요?

뷰포트 너비가 600px 이하일 때 해당 규칙을 적용합니다.

## Q3. `min-width`와 `max-width`의 차이는 무엇인가요?

`min-width`는 지정값 이상, `max-width`는 지정값 이하에서 적용됩니다.

## Q4. 원본은 모바일 우선인가요?

기본이 가로 메뉴이고 max-width에서 모바일 형태로 바뀌므로 데스크톱 우선에 가깝습니다.

## Q5. `span:hover + ul`은 무엇을 선택하나요?

hover 상태인 span의 바로 다음 형제 ul을 선택합니다.

## Q6. 원본 메뉴가 실제 사용하기 어려운 이유는 무엇인가요?

span에서 ul로 포인터를 이동하면 span hover가 해제되어 메뉴가 닫힐 수 있고, 모바일 터치에는 hover가 안정적이지 않기 때문입니다.

## Q7. `opacity: 0`과 `display: none`의 차이는 무엇인가요?

opacity 0은 요소와 공간이 남지만 display none은 레이아웃과 일반 접근 경로에서 요소를 제거합니다.

## Q8. 메뉴 열기에 `button`을 사용해야 하는 이유는 무엇인가요?

키보드 조작, 역할, 포커스, 활성화 동작을 기본 제공하기 때문입니다.

## Q9. `aria-expanded`는 무엇을 전달하나요?

제어하는 메뉴나 영역이 현재 열려 있는지 닫혀 있는지를 보조 기술에 전달합니다.

## Q10. 브레이크포인트는 어떻게 선택하나요?

특정 기기 이름보다 콘텐츠와 레이아웃이 실제로 깨지는 지점을 기준으로 선택합니다.

---

# Problems

## 문제 1. Max-width

뷰포트가 600px 이하일 때 배경색을 변경하는 미디어 쿼리를 작성하세요.

## 문제 2. Min-width

뷰포트가 601px 이상일 때 메뉴를 가로 배치하세요.

## 문제 3. 범위 조건

500px 이상 600px 이하에서만 적용되는 미디어 쿼리를 작성하세요.

## 문제 4. 모바일 세로 메뉴

600px 이하에서 li를 한 줄씩 세로로 배치하고 부모 너비를 채우도록 작성하세요.

## 문제 5. Box-sizing

문제 4에서 border 때문에 가로 overflow가 발생하지 않도록 작성하세요.

## 문제 6. 원본 선택자

`span:hover + ul`이 선택하는 요소를 설명하세요.

## 문제 7. 인접 구조

다음 구조에서 원본 선택자가 동작하지 않는 이유를 설명하세요.

```html
<span>메뉴</span>
<p>설명</p>
<ul>...</ul>
```

## 문제 8. Opacity 문제

`opacity: 0`으로 숨긴 메뉴가 가질 수 있는 문제를 세 가지 작성하세요.

## 문제 9. 숨김 상태 개선

opacity 전환을 유지하면서 숨김 상태에서 포인터 조작을 막도록 작성하세요.

## 문제 10. Transition 위치

열림과 닫힘 모두 부드럽게 동작하도록 transition 위치를 수정하세요.

## 문제 11. Transform 이동

`top: -20px` 대신 transform으로 위로 20px 이동하세요.

## 문제 12. Hover 유지

버튼과 메뉴를 감싼 부모에 hover가 있는 동안 메뉴가 유지되도록 작성하세요.

## 문제 13. Focus-within

키보드 포커스가 메뉴 내부에 있을 때도 메뉴가 보이도록 작성하세요.

## 문제 14. 의미 있는 버튼

원본 span을 접근 가능한 메뉴 버튼으로 바꾸세요.

## 문제 15. ARIA 연결

버튼이 `primary-menu`를 제어하고 닫힌 상태임을 표현하세요.

## 문제 16. 실제 메뉴 링크

메일 메뉴 항목을 실제 링크로 작성하세요.

## 문제 17. JavaScript 토글

버튼 클릭 시 `aria-expanded` 값을 true와 false로 전환하는 코드를 작성하세요.

## 문제 18. Reduced Motion

움직임 감소 환경에서 메뉴 transition을 제거하세요.

## 문제 19. 원본 동일성

내 코드와 강사님 코드의 CSS 14 차이를 작성하세요.

## 문제 20. Mobile First

기본은 세로 메뉴, 601px 이상에서 가로 메뉴가 되도록 작성하세요.

## 문제 21. Hover 환경 조건

실제 hover를 지원하는 정밀 포인터 환경에서만 hover 장식을 적용하세요.

## 문제 22. 종합 반응형 메뉴

다음 요구사항을 만족하는 메뉴를 작성하세요.

- `nav`, `button`, `ul`, `a` 사용
- 600px 이하에서 버튼 표시
- 모바일 기본 메뉴 닫힘
- 버튼 클릭으로 열고 닫기
- `aria-expanded`, `aria-controls`
- 데스크톱에서 메뉴 항상 표시
- Flexbox 사용
- 링크 최소 높이 44px
- focus-visible 표시
- opacity와 transform 전환
- 숨김 상태에서 visibility와 pointer-events 관리
- reduced motion 대응

---

# Answers & Explanations

## 정답 1

```css
@media (max-width: 600px) {
  body {
    background-color: #f3f4f6;
  }
}
```

## 정답 2

```css
@media (min-width: 601px) {
  ul {
    display: flex;
  }
}
```

## 정답 3

```css
@media
  (min-width: 500px)
  and (max-width: 600px) {
  ...
}
```

## 정답 4

```css
@media (max-width: 600px) {
  li {
    display: block;
    width: 100%;
  }
}
```

## 정답 5

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

## 정답 6

hover 상태인 span의 바로 다음 형제인 ul을 선택합니다.

## 정답 7

인접 형제 선택자 `+`는 바로 다음 형제만 선택합니다. span 다음에 p가 있으므로 ul은 선택되지 않습니다.

## 정답 8

예:

```text
1. 레이아웃 공간을 계속 차지한다.
2. 링크와 버튼이 포커스될 수 있다.
3. 포인터 이벤트를 받을 수 있다.
```

접근성 트리에서도 남을 수 있습니다.

## 정답 9

```css
.menu {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}
```

열린 상태:

```css
.menu.is-open {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}
```

## 정답 10

```css
ul {
  transition:
    opacity 0.5s,
    transform 0.5s;
}

span:hover + ul {
  opacity: 1;
  transform: translateY(0);
}
```

transition을 기본 상태에 둡니다.

## 정답 11

```css
ul {
  transform: translateY(-20px);
}
```

열린 상태:

```css
span:hover + ul {
  transform: translateY(0);
}
```

## 정답 12

```css
.menu:hover .menu__list {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}
```

## 정답 13

```css
.menu:focus-within .menu__list {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}
```

## 정답 14

```html
<button class="menu-button" type="button">
  메뉴 열기
</button>
```

## 정답 15

```html
<button
  class="menu-button"
  type="button"
  aria-expanded="false"
  aria-controls="primary-menu"
>
  메뉴 열기
</button>
```

## 정답 16

```html
<li>
  <a href="/mail">메일</a>
</li>
```

## 정답 17

```js
const button =
  document.querySelector(".menu-button");

button.addEventListener("click", () => {
  const isOpen =
    button.getAttribute("aria-expanded")
    === "true";

  button.setAttribute(
    "aria-expanded",
    String(!isOpen)
  );
});
```

## 정답 18

```css
@media (prefers-reduced-motion: reduce) {
  .menu__list {
    transition: none;
  }
}
```

## 정답 19

차이가 없습니다. 두 원본의 HTML, CSS, 주석, 문구가 모두 동일합니다.

## 정답 20

```css
ul {
  display: flex;
  flex-direction: column;
}

@media (min-width: 601px) {
  ul {
    flex-direction: row;
  }
}
```

## 정답 21

```css
@media (hover: hover) and (pointer: fine) {
  .menu-link:hover {
    background-color: #f3f4f6;
  }
}
```

## 정답 22

### HTML

```html
<nav class="site-nav" aria-label="주요 메뉴">
  <button
    class="site-nav__toggle"
    type="button"
    aria-expanded="false"
    aria-controls="site-menu"
  >
    <span aria-hidden="true">☰</span>
    <span>메뉴</span>
  </button>

  <ul class="site-nav__menu" id="site-menu">
    <li>
      <a href="/mail">메일</a>
    </li>
    <li>
      <a href="/blog">블로그</a>
    </li>
    <li>
      <a href="/webtoon">웹툰</a>
    </li>
    <li>
      <a href="/cafe">카페</a>
    </li>
  </ul>
</nav>
```

### CSS

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

.site-nav__toggle {
  display: none;
}

.site-nav__menu {
  display: flex;
  margin: 0;
  padding: 0;
  list-style: none;
}

.site-nav__menu a {
  display: flex;
  min-width: 100px;
  min-height: 44px;
  align-items: center;
  justify-content: center;
  color: inherit;
  text-decoration: none;
}

.site-nav__menu a:focus-visible,
.site-nav__toggle:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}

@media (max-width: 600px) {
  .site-nav__toggle {
    display: inline-flex;
    min-width: 44px;
    min-height: 44px;
    align-items: center;
    gap: 0.5rem;
  }

  .site-nav__menu {
    flex-direction: column;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transform: translateY(-20px);
    transition:
      opacity 0.2s ease,
      transform 0.2s ease;
  }

  .site-nav__toggle[aria-expanded="true"]
  + .site-nav__menu {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transform: translateY(0);
  }

  .site-nav__menu a {
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .site-nav__menu {
    transition: none;
  }
}
```

### JavaScript

```js
const toggle =
  document.querySelector(".site-nav__toggle");

toggle.addEventListener("click", () => {
  const expanded =
    toggle.getAttribute("aria-expanded")
    === "true";

  toggle.setAttribute(
    "aria-expanded",
    String(!expanded)
  );
});
```

데스크톱에서는 모바일 미디어 쿼리의 숨김 규칙이 적용되지 않으므로 메뉴가 항상 표시됩니다.

---

# Final Checklist

## 미디어 쿼리 기본

- [ ] viewport meta 태그가 있다.
- [ ] `max-width`와 `min-width`를 구분했다.
- [ ] 경계값 포함 여부를 확인했다.
- [ ] 브레이크포인트를 콘텐츠 기준으로 선택했다.
- [ ] 데스크톱 우선 또는 모바일 우선 전략을 일관되게 사용했다.
- [ ] 개발자 도구로 실제 미디어 쿼리 활성 상태를 확인했다.

## 메뉴 레이아웃

- [ ] 데스크톱에서 메뉴가 가로로 표시된다.
- [ ] 모바일에서 메뉴가 세로로 표시된다.
- [ ] inline-block 공백 영향을 확인했다.
- [ ] `width: 100%`와 border 계산을 확인했다.
- [ ] `box-sizing: border-box`를 적용했다.
- [ ] ul의 기본 margin과 padding을 정리했다.
- [ ] 한 줄 line-height 중앙 정렬의 한계를 이해했다.

## 숨김과 전환

- [ ] opacity 0이 요소를 제거하지 않음을 이해했다.
- [ ] 숨김 상태에서 visibility를 관리했다.
- [ ] 숨김 상태에서 pointer-events를 차단했다.
- [ ] transition을 기본 상태에 작성했다.
- [ ] `all` 대신 필요한 속성을 지정했다.
- [ ] top 대신 transform을 검토했다.
- [ ] reduced motion 환경을 고려했다.

## 접근성과 조작

- [ ] 메뉴 열기에 button을 사용했다.
- [ ] `aria-expanded`를 제공했다.
- [ ] `aria-controls`로 메뉴와 연결했다.
- [ ] 메뉴 항목에 실제 a 요소를 사용했다.
- [ ] 키보드 Enter와 Space로 버튼을 조작할 수 있다.
- [ ] focus-visible 표시가 있다.
- [ ] 모바일 핵심 기능을 hover에만 의존하지 않았다.
- [ ] 메뉴를 닫는 방법이 있다.

## 원본 코드 검수

- [ ] 내 코드와 강사님 코드가 동일함을 확인했다.
- [ ] 존재하지 않는 코드 차이를 만들지 않았다.
- [ ] `span:hover + ul`의 인접 형제 조건을 설명했다.
- [ ] span에서 ul로 이동할 때 메뉴가 닫히는 문제를 설명했다.
- [ ] `opacity: 0`의 상호작용 문제를 설명했다.
- [ ] hover 상태에만 transition이 있는 문제를 설명했다.
- [ ] 모바일 width 100%와 border overflow 가능성을 설명했다.
- [ ] `lang="en"`과 `Document`를 개선했다.

---

# Key Summary

- 미디어 쿼리는 화면 크기와 사용자 환경에 따라 CSS를 선택적으로 적용한다.
- 원본 `@media screen and (max-width: 600px)`은 화면 너비 600px 이하에서 적용된다.
- 주석 처리된 `min-width: 500px`을 함께 사용하면 500px 이상 600px 이하 범위가 된다.
- 원본은 기본 가로 메뉴를 작은 화면에서 세로 메뉴로 바꾸는 데스크톱 우선 구조다.
- `inline-block`은 메뉴 항목을 가로로 배치하지만 HTML 공백의 영향을 받을 수 있다.
- `line-height: 50px`은 한 줄 텍스트의 간단한 세로 중앙 정렬 방식이다.
- 모바일에서 `li { width: 100%; }`와 border를 함께 사용하면 content-box 기준으로 가로 overflow가 생길 수 있다.
- `box-sizing: border-box`를 적용하면 border를 선언 너비 안에 포함할 수 있다.
- 원본의 span은 넓은 화면에서 숨겨지고 600px 이하에서 표시된다.
- `opacity: 0`은 메뉴를 보이지 않게 하지만 공간과 상호작용 가능성을 남긴다.
- `display: none`은 레이아웃에서 요소를 제거하지만 일반 opacity transition을 바로 적용하기 어렵다.
- `span:hover + ul`은 hover 중인 span의 바로 다음 형제 ul만 선택한다.
- span과 ul 사이에 다른 요소가 있으면 인접 형제 선택자가 동작하지 않는다.
- span에서 ul로 포인터를 옮기면 hover가 해제되어 메뉴가 닫힐 수 있다.
- 모바일 터치 환경에서 hover는 핵심 메뉴 동작으로 적합하지 않다.
- 실제 메뉴 열기에는 span보다 button을 사용한다.
- 버튼에는 `aria-expanded`와 `aria-controls`를 제공한다.
- 실제 메뉴 항목에는 a 요소를 사용한다.
- transition을 hover 상태에만 작성하면 닫힐 때 즉시 사라질 수 있다.
- transition은 기본 상태에 작성하고 opacity와 transform만 명시하는 편이 좋다.
- 내 코드와 강사님 코드의 CSS 14 원본은 완전히 동일하다.
- 이번 비교에서는 존재하지 않는 차이를 만들어 내지 않고 공통 장점과 문제점을 분석했다.
