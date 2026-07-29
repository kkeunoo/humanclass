# CSS Transition과 상태 변화

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `12_CSS_Transition과_상태변화.md` |
| 분류 | `02_CSS` |
| 권장 선수 학습 | `11_CSS_그림자와_시각효과.md` |
| 다음 학습 | `13_CSS_Transform.md` |
| 원본 기준 | `workspace_me/workspace_html/css/12_transition.html`, `workspace_teacher/workspace_html/css/12_transition.html` |
| 핵심 범위 | `transition`, `transition-property`, `transition-duration`, `transition-timing-function`, `transition-delay`, hover 진입·해제 차이 |
| 프로젝트 연결 | 버튼 hover, 카드 상태 변화, 메뉴 강조, 색상 전환, 크기 변화, 접근 가능한 인터랙션 |

> 원본 CSS 12는 별도의 외부 CSS 파일 없이 `12_transition.html` 내부 `<style>`에서 진행됩니다. 내 코드와 강사님 코드는 모두 `.box1`, `.box2`의 hover 상태를 비교하며, 공통 상태에 transition을 둘 때와 hover 상태에만 transition을 둘 때의 차이를 확인합니다. 이 문서는 원본의 두 박스 실습을 중심으로 정리하고, 개별 transition 속성, timing function, delay, 성능, 접근성, `prefers-reduced-motion`은 **확장 학습**으로 구분해 보완했습니다.

---

# 학습 목표

- CSS transition이 두 상태 사이의 값 변화를 시간에 따라 이어 주는 기능임을 설명한다.
- transition이 동작하려면 시작값과 종료값이 필요하다는 점을 이해한다.
- `transition` 단축 속성의 구성 순서를 설명한다.
- `transition-property`로 어떤 속성을 전환할지 지정한다.
- `transition-duration`에 초와 밀리초를 사용할 수 있다.
- 소수점 시간값을 사용할 수 있다는 원본 주석을 정확히 설명한다.
- 공통 상태에 transition을 둘 때 hover 진입과 해제 모두 부드럽게 동작하는 이유를 이해한다.
- hover 상태에만 transition을 둘 때 진입과 해제의 동작이 달라질 수 있음을 설명한다.
- `transition: all`의 편리함과 유지보수·성능 문제를 함께 이해한다.
- width와 height 애니메이션이 주변 레이아웃을 움직일 수 있다는 점을 설명한다.
- 색상, 그림자, transform 중심으로 더 안정적인 인터랙션을 작성한다.
- 키보드 사용자를 위해 `:focus-visible` 상태를 함께 제공한다.
- 움직임 감소 환경을 고려한다.
- 내 코드와 강사님 코드의 차이와 원본 주석을 비교한다.

---

# 1. CSS Transition이란?

Transition은 CSS 속성값이 한 상태에서 다른 상태로 바뀔 때 중간 과정을 자동으로 만들어 주는 기능입니다.

transition 없음:

```css
.box:hover {
  background-color: red;
}
```

마우스를 올리는 순간 즉시 초록색에서 빨간색으로 바뀝니다.

transition 있음:

```css
.box {
  transition: background-color 0.5s;
}

.box:hover {
  background-color: red;
}
```

0.5초 동안 색상이 점진적으로 변합니다.

---

# 2. 원본 HTML 구조

내 코드:

```html
<div class="box box1">박스</div>
<div class="box box2">박스</div>
```

강사님 코드:

```html
<div class="box box1">박스</div>
<div class="box box2">박스2</div>
```

차이:

| 요소 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 첫 번째 박스 | `박스` | `박스` |
| 두 번째 박스 | `박스` | `박스2` |

스타일 구조는 동일하며 두 번째 박스의 텍스트만 다릅니다.

---

# 3. 원본 공통 `.box`

내 코드:

```css
.box {
  border: 1px solid red;
  width: 100px;
  height: 100px;
  background: green;
  color: white;
  margin: 10px;

  /* width등 별개로 줄 수 있지만 보통 all로 사용하고 시간은 소수점도 가능 */
  /* transition: all 0.5s; */
  /* transition: width 1s; */
}
```

강사님 코드:

```css
.box {
  border: 1px solid red;
  height: 100px;
  width: 100px;
  background-color: green;
  color: white;
  margin: 10px;

  /* transition: all 0.5s; */
  /* transition: width 1s; */
}
```

실제 화면 결과는 같습니다.

---

# 4. 내 코드와 강사님 코드의 속성 차이

내 코드:

```css
background: green;
```

강사님:

```css
background-color: green;
```

현재는 단색만 사용하므로 결과는 같습니다.

차이:

- `background`는 배경 관련 속성을 함께 초기화할 수 있는 단축 속성
- `background-color`는 배경색만 변경

배경 이미지나 반복 설정이 함께 있다면 `background` 단축 속성을 나중에 작성할 때 기존 값을 초기화할 수 있습니다.

이 실습에서는 오류가 아닙니다.

---

# 5. Transition이 없는 `.box1`

원본:

```css
.box1:hover {
  background: red;
  border-radius: 50%;
  width: 200px;
  height: 200px;
}
```

강사님:

```css
.box1:hover {
  background-color: red;
  border-radius: 50%;
  width: 200px;
  height: 200px;
}
```

hover 시 다음 값이 즉시 변경됩니다.

```text
배경색: green → red
모서리: 0 → 50%
너비: 100px → 200px
높이: 100px → 200px
```

공통 `.box`의 transition이 주석 처리되어 있으므로 `.box1`은 중간 과정 없이 즉시 바뀝니다.

---

# 6. Transition이 hover에 있는 `.box2`

내 코드:

```css
.box2:hover {
  background: red;
  border-radius: 50%;
  width: 200px;
  height: 200px;

  /* hover자체에 transition을 두면 hover자체에만 먹음 */
  transition: all 0.5s;
}
```

강사님:

```css
.box2:hover {
  background-color: red;
  border-radius: 50%;
  width: 200px;
  height: 200px;

  transition: all 0.5s;
}
```

마우스를 올려 hover 상태가 적용될 때 transition 선언도 함께 적용됩니다.

따라서 hover 진입 시에는 0.5초 동안 변화가 보일 수 있습니다.

---

# 7. Hover 해제 시 차이

마우스를 `.box2` 밖으로 이동하면 `:hover` 규칙 자체가 사라집니다.

이때 다음 선언도 사라집니다.

```css
transition: all 0.5s;
```

기본 `.box`에는 transition이 없으므로 원래 상태로 돌아갈 때는 즉시 복귀할 수 있습니다.

```text
마우스를 올림 → 부드럽게 커짐
마우스를 뺌 → 즉시 작아짐
```

이것이 내 코드 주석의 핵심 의도입니다.

---

# 8. 원본 주석 정확하게 표현하기

내 코드:

```text
hover자체에 transition을 두면 hover자체에만 먹음
```

초보자 관점에서 결과를 기억하기 좋은 표현입니다.

더 정확한 설명:

```text
transition을 :hover 규칙에만 작성하면
hover 상태로 진입할 때는 transition이 적용되지만,
hover가 해제되는 순간 해당 transition 선언도 사라지므로
기본 상태로 돌아가는 과정은 즉시 바뀔 수 있다.
```

---

# 9. 양방향 전환 만들기

transition을 기본 상태에 작성합니다.

```css
.box2 {
  transition: all 0.5s;
}

.box2:hover {
  background-color: red;
  border-radius: 50%;
  width: 200px;
  height: 200px;
}
```

이제:

```text
hover 진입 → 0.5초
hover 해제 → 0.5초
```

두 방향 모두 transition 선언을 가진 상태에서 변화가 계산됩니다.

---

# 10. Transition 기본 문법

단축 속성:

```css
transition:
  property
  duration
  timing-function
  delay;
```

예:

```css
.box {
  transition:
    width
    0.5s
    ease
    0s;
}
```

자주 쓰는 축약:

```css
.box {
  transition: width 0.5s;
}
```

생략된 값은 기본값을 사용합니다.

---

# 11. `transition-property`

어떤 CSS 속성을 전환할지 지정합니다.

```css
.box {
  transition-property: width;
}
```

여러 속성:

```css
.box {
  transition-property:
    background-color,
    border-radius,
    width,
    height;
}
```

단축 속성으로 작성:

```css
.box {
  transition:
    background-color 0.5s,
    border-radius 0.5s,
    width 0.5s,
    height 0.5s;
}
```

---

# 12. 원본 `transition: width 1s`

원본 주석:

```css
/* transition: width 1s; */
```

이 값을 활성화하면 width만 부드럽게 바뀝니다.

hover에서 함께 바뀌는 다음 속성은 즉시 변할 수 있습니다.

```text
background-color
border-radius
height
```

width만 1초 동안 전환됩니다.

이 예제는 transition property를 개별 지정할 수 있음을 보여 줍니다.

---

# 13. `transition-duration`

전환에 걸리는 시간입니다.

```css
.box {
  transition-duration: 0.5s;
}
```

지원 단위:

```text
s  → 초
ms → 밀리초
```

같은 시간:

```css
0.5s
500ms
```

0초:

```css
transition-duration: 0s;
```

중간 과정 없이 즉시 변경됩니다.

---

# 14. 소수점 시간값

내 코드 주석:

```text
시간은 소수점도 가능
```

정확합니다.

예:

```css
transition: all 0.25s;
transition: all 1.5s;
transition: all 0.075s;
```

너무 짧으면 사용자가 전환을 거의 느끼지 못하고, 너무 길면 UI 반응이 느리게 느껴질 수 있습니다.

일반적인 인터랙션은 프로젝트에 따라 약 `0.15s`~`0.3s` 범위를 자주 사용하지만, 원본에는 특정 권장 시간이 제시되어 있지 않습니다.

---

# 15. `transition-timing-function`

시간에 따라 변화하는 속도를 결정합니다.

대표 값:

```css
ease
linear
ease-in
ease-out
ease-in-out
```

기본값:

```css
ease
```

---

# 16. Timing function 비교

## `linear`

```css
transition-timing-function: linear;
```

처음부터 끝까지 일정한 속도입니다.

## `ease-in`

```css
transition-timing-function: ease-in;
```

천천히 시작해 빨라집니다.

## `ease-out`

```css
transition-timing-function: ease-out;
```

빠르게 시작해 천천히 끝납니다.

## `ease-in-out`

```css
transition-timing-function: ease-in-out;
```

천천히 시작하고 천천히 끝납니다.

UI hover에는 `ease`, `ease-out`, `ease-in-out`을 자주 검토합니다.

---

# 17. `cubic-bezier()`

속도 곡선을 직접 지정할 수 있습니다.

```css
.card {
  transition:
    transform
    0.25s
    cubic-bezier(0.2, 0.8, 0.2, 1);
}
```

원본에는 없는 확장 학습입니다.

팀 프로젝트에서는 반복되는 easing 값을 CSS 변수로 관리할 수 있습니다.

```css
:root {
  --ease-standard:
    cubic-bezier(0.2, 0.8, 0.2, 1);
}
```

---

# 18. `transition-delay`

전환이 시작되기 전 대기 시간입니다.

```css
.box {
  transition-delay: 0.2s;
}
```

단축 속성:

```css
.box {
  transition: width 0.5s ease 0.2s;
}
```

순서에서 시간값이 두 개면:

```text
첫 번째 시간 → duration
두 번째 시간 → delay
```

---

# 19. 여러 transition

```css
.box {
  transition:
    background-color 0.3s ease,
    border-radius 0.5s ease,
    transform 0.2s ease-out;
}
```

각 속성에 서로 다른 시간과 곡선을 줄 수 있습니다.

가독성을 위해 속성마다 줄을 나누는 것이 좋습니다.

---

# 20. `transition: all`

원본 주석:

```css
/* transition: all 0.5s; */
```

장점:

- 빠르게 실험 가능
- hover에서 바뀌는 여러 속성에 한 번에 적용
- 초보 학습에 단순함

주의:

- 의도하지 않은 속성도 전환될 수 있음
- 나중에 새 속성이 추가되면 자동으로 애니메이션됨
- 디버깅이 어려워질 수 있음
- 레이아웃 비용이 큰 속성까지 전환할 수 있음

실무에서는 필요한 속성을 명시하는 편이 안전합니다.

---

# 21. 원본에서 전환되는 속성

`all`을 사용하면 다음 변화가 모두 transition 대상이 됩니다.

```css
background-color
border-radius
width
height
```

내 코드에서는 `background` 단축 속성을 사용하지만 실제 단색 변화의 핵심은 배경색입니다.

명시적 작성:

```css
.box2 {
  transition:
    background-color 0.5s,
    border-radius 0.5s,
    width 0.5s,
    height 0.5s;
}
```

---

# 22. Transition 가능한 값

Transition은 중간값을 계산할 수 있는 속성에서 자연스럽게 동작합니다.

예:

```css
color
background-color
width
height
border-radius
opacity
transform
box-shadow
```

일부 속성은 중간 상태를 계산하기 어렵거나 discrete하게 바뀝니다.

예:

```css
display: none;
```

일반적인 transition만으로 `display: none`과 `block` 사이를 부드럽게 전환하기 어렵습니다.

---

# 23. 시작값과 종료값

transition에는 비교할 두 상태가 필요합니다.

기본:

```css
.box {
  width: 100px;
}
```

hover:

```css
.box:hover {
  width: 200px;
}
```

브라우저는 100px에서 200px 사이의 중간값을 계산합니다.

시작값이 `auto`이고 종료값이 고정 길이인 경우 일반 transition에서 원하는 결과가 나오지 않을 수 있습니다.

```css
.panel {
  height: auto;
}
```

```css
.panel.is-open {
  height: 300px;
}
```

이런 경우에는 다른 구현 방식을 검토합니다.

---

# 24. Width와 Height 전환의 레이아웃 영향

원본은 다음 속성을 변경합니다.

```css
width: 100px → 200px
height: 100px → 200px
```

박스의 실제 레이아웃 크기가 바뀌므로 주변 요소가 밀릴 수 있습니다.

브라우저는 여러 프레임에서 레이아웃을 다시 계산할 수 있습니다.

카드 확대 효과에서는 `transform: scale()`이 더 적절한 경우가 많습니다.

---

# 25. `transform: scale()` 대안

```css
.box {
  width: 100px;
  height: 100px;
  transition:
    background-color 0.5s,
    border-radius 0.5s,
    transform 0.5s;
}

.box:hover {
  background-color: red;
  border-radius: 50%;
  transform: scale(2);
}
```

차이:

| 방식 | 결과 |
| --- | --- |
| width/height | 실제 레이아웃 크기 변경 |
| transform scale | 시각적으로 확대, 원래 레이아웃 공간 유지 |

`scale(2)`는 주변 요소를 밀지 않으므로 겹침 여부와 충분한 공간을 확인해야 합니다.

---

# 26. Transform과 Transition

Transition은 변화 과정을 담당하고 transform은 변형값을 담당합니다.

```css
.card {
  transition: transform 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
}
```

역할:

```text
transform → 어디로 어떻게 변형할지
transition → 그 변형을 얼마나 부드럽게 진행할지
```

다음 문서에서 transform을 더 자세히 학습합니다.

---

# 27. Border-radius 전환

원본:

```css
border-radius: 50%;
```

기본값은 일반적으로 `0`에 가까운 사각형이고 hover에서 `50%`로 바뀝니다.

박스가 정사각형이므로 원형이 됩니다.

```text
100 × 100 → 원
200 × 200 → 원
```

너비와 높이가 다르면 `border-radius: 50%`는 타원 형태가 될 수 있습니다.

---

# 28. Background 전환

색상끼리는 중간 색상을 계산할 수 있습니다.

```css
background-color:
  green → red
```

따라서 transition 동안 중간 색상이 표시됩니다.

단축 속성보다 목적이 명확한 속성을 사용할 수 있습니다.

```css
.box {
  background-color: green;
}
```

```css
.box:hover {
  background-color: red;
}
```

---

# 29. Hover 영역이 움직이는 문제

원본 `.box2`가 100px에서 200px로 커지면 hover 가능한 영역도 함께 커집니다.

반대로 hover 해제 시 즉시 작아지면 포인터와 박스 경계가 빠르게 달라질 수 있습니다.

특정 배치에서는 다음과 같은 깜빡임이 생길 수 있습니다.

```text
hover로 커짐
→ 요소가 다른 위치를 밀어냄
→ 포인터가 요소 밖으로 이동
→ hover 해제
→ 다시 작아짐
```

가능하면 레이아웃 크기보다 색상, 그림자, transform을 사용합니다.

---

# 30. Box-sizing과 크기

원본:

```css
width: 100px;
height: 100px;
border: 1px solid red;
```

기본 `content-box`라면 실제 바깥 크기는 테두리를 포함해 약 102px입니다.

hover:

```text
content 200px
+ border 2px
= 약 202px
```

프로젝트에서 다음 초기화를 사용할 수 있습니다.

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

그러면 선언한 width와 height 안에 border가 포함됩니다.

---

# 31. 원본 박스 텍스트 정렬

원본에는 텍스트 중앙 정렬이 없습니다.

```html
<div class="box box1">박스</div>
```

텍스트는 기본적으로 박스 왼쪽 위에 표시됩니다.

시각적으로 가운데 배치하려면:

```css
.box {
  display: grid;
  place-items: center;
}
```

이것은 원본 핵심 transition과 별개인 디자인 개선입니다.

---

# 32. Hover뿐 아니라 Focus

원본 요소는 `div`이므로 기본적으로 키보드 포커스를 받지 않습니다.

실제 버튼이라면:

```html
<button class="box" type="button">
  박스
</button>
```

```css
.box:hover,
.box:focus-visible {
  background-color: red;
  border-radius: 50%;
  transform: scale(1.1);
}
```

키보드 사용자가 동일한 상태 변화를 확인할 수 있습니다.

---

# 33. 실제 역할에 맞는 HTML

단순 시각 실습:

```html
<div class="box">박스</div>
```

클릭 동작:

```html
<button class="box" type="button">
  실행
</button>
```

페이지 이동:

```html
<a class="box" href="/css">
  CSS 문서
</a>
```

CSS hover 효과 때문에 의미 없는 `div`를 클릭 요소로 만들지 않습니다.

---

# 34. Focus outline

```css
.box:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}
```

transition 효과가 있어도 포커스 위치는 명확해야 합니다.

outline까지 느리게 transition하면 현재 위치를 빠르게 확인하기 어려울 수 있습니다.

포커스 outline은 즉시 표시하는 편이 안전합니다.

---

# 35. 움직임 감소 환경

```css
@media (prefers-reduced-motion: reduce) {
  .box {
    transition: none;
  }
}
```

움직임에 민감한 사용자는 시스템에서 애니메이션 감소를 설정할 수 있습니다.

색상 변화 자체는 유지하되 확대나 이동만 제거할 수도 있습니다.

```css
@media (prefers-reduced-motion: reduce) {
  .box {
    transition: background-color 0.01ms;
  }

  .box:hover,
  .box:focus-visible {
    transform: none;
  }
}
```

---

# 36. Transition과 접근성

확인 사항:

- 전환이 너무 느려 조작을 방해하지 않는가
- hover에만 중요한 정보를 숨기지 않았는가
- 키보드 focus 상태가 있는가
- 색상 변화만으로 상태를 전달하지 않는가
- 움직임 감소 설정을 고려했는가
- 크기 변화로 콘텐츠가 갑자기 밀리지 않는가

Transition은 장식이어야 하며 핵심 기능을 지연시키면 안 됩니다.

---

# 37. 색상만으로 상태 전달하지 않기

```css
.button:hover {
  background-color: red;
}
```

색상만으로 상태를 표현하면 일부 사용자가 차이를 알기 어려울 수 있습니다.

함께 사용할 수 있는 요소:

- 텍스트
- 아이콘
- 밑줄
- 테두리
- `aria-pressed`
- `aria-expanded`

예:

```html
<button
  class="toggle"
  type="button"
  aria-pressed="true"
>
  <span aria-hidden="true">✓</span>
  선택됨
</button>
```

---

# 38. Transition 성능

일반적으로 다음 속성은 레이아웃과 페인트 비용이 커질 수 있습니다.

```text
width
height
top
left
margin
padding
box-shadow
```

다음 속성은 상대적으로 애니메이션에 유리한 경우가 많습니다.

```text
transform
opacity
```

다만 실제 성능은 요소 크기, 개수, 브라우저, 장치에 따라 확인해야 합니다.

---

# 39. `will-change` 주의

```css
.card {
  will-change: transform;
}
```

브라우저 최적화를 힌트할 수 있지만 남용하면 메모리 사용이 늘어날 수 있습니다.

항상 적용하기보다 실제 성능 문제가 확인된 제한된 요소에서 사용합니다.

원본에는 없는 확장 학습입니다.

---

# 40. Transition 이벤트 확장 학습

JavaScript에서 transition 종료를 감지할 수 있습니다.

```js
const box = document.querySelector(".box");

box.addEventListener("transitionend", (event) => {
  console.log(event.propertyName);
});
```

주의:

- 전환되는 속성마다 이벤트가 발생할 수 있다.
- 사용자가 움직임 감소를 설정하면 이벤트 타이밍이 달라질 수 있다.
- 핵심 기능을 transition 종료에 과도하게 의존하지 않는다.

---

# 41. 문서 언어와 제목

내 코드와 강사님 코드:

```html
<html lang="en">
<title>Document</title>
```

본문은 한국어이므로:

```html
<html lang="ko">
<title>CSS Transition</title>
```

로 개선합니다.

---

# 42. 인라인 Style

원본은 `<style>` 안에서 실습합니다.

```html
<style>
  ...
</style>
```

한 파일에서 결과를 빠르게 확인하는 수업 예제로 적절합니다.

프로젝트에서는 외부 CSS를 사용할 수 있습니다.

```html
<link
  rel="stylesheet"
  href="asset/css/transition.css"
>
```

---

# 43. My Code 분석

## 43.1 장점

- 개별 속성 `width`만 transition할 수 있음을 주석으로 기록했다.
- `all`을 사용할 수 있다는 점을 설명했다.
- 소수점 시간값 사용 가능성을 기록했다.
- hover 상태에 transition을 둘 때의 차이를 설명했다.
- 강사님 코드보다 실습 의도를 복습하기 쉽다.

## 43.2 개선점

- `all`을 “보통 사용한다”고 일반화하면 실무에서 불필요한 속성까지 전환될 수 있다.
- hover 상태에만 적용된 transition의 진입·해제 차이를 더 정확히 설명해야 한다.
- `background` 단축 속성보다 `background-color`가 의도가 명확하다.
- width와 height 전환은 주변 레이아웃을 움직일 수 있다.
- 키보드 focus 상태가 없다.
- 움직임 감소 환경을 고려하지 않았다.
- 문서 언어와 제목을 개선해야 한다.

---

# 44. Teacher Code 분석

## 44.1 장점

- `background-color`를 사용해 배경색 변경 의도가 명확하다.
- `.box1`과 `.box2` 비교가 간결하다.
- 공통 transition과 개별 width transition 실험값을 주석으로 남겼다.
- 두 번째 박스의 텍스트를 `박스2`로 지정해 비교 대상을 구분했다.
- 핵심 실습에 불필요한 설명이 적다.

## 44.2 개선점

- hover에만 transition을 작성했을 때 해제 시 즉시 돌아갈 수 있다는 설명이 없다.
- `all`의 주의점이 없다.
- width·height 전환의 레이아웃 비용을 설명하지 않는다.
- focus와 reduced motion이 없다.
- 문서 언어가 `en`이고 제목이 `Document`다.
- transition 구성 요소와 timing function 설명이 없다.

---

# 45. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 공통 배경 | `background` | `background-color` |
| width/height 순서 | width 후 height | height 후 width |
| transition 주석 | 상세 설명 추가 | 코드 예제만 |
| 소수점 시간 설명 | 있음 | 없음 |
| hover transition 설명 | 있음 | 없음 |
| 두 번째 박스 텍스트 | `박스` | `박스2` |
| 실제 결과 | 거의 동일 | 거의 동일 |
| 학습 성격 | 개인 복습 설명형 | 최소 수업 예제형 |

---

# 46. 원본 통합 개선 예제

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
  <title>CSS Transition</title>
  <link
    rel="stylesheet"
    href="asset/css/transition.css"
  >
</head>
<body>
  <main class="page">
    <h1>CSS Transition</h1>

    <section class="demo">
      <h2>Transition 없음</h2>
      <div class="box box--instant">
        박스 1
      </div>
    </section>

    <section class="demo">
      <h2>양방향 Transition</h2>
      <button
        class="box box--smooth"
        type="button"
      >
        박스 2
      </button>
    </section>
  </main>
</body>
</html>
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

.page {
  width: min(100% - 2rem, 50rem);
  margin-inline: auto;
  padding-block: 2rem;
}

.box {
  display: grid;
  width: 100px;
  height: 100px;
  margin: 1rem;
  border: 1px solid red;
  color: white;
  background-color: green;
  place-items: center;
}

.box--instant:hover {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background-color: red;
}

.box--smooth {
  font: inherit;
  cursor: pointer;
  transition:
    background-color 0.3s ease,
    border-radius 0.3s ease,
    transform 0.3s ease;
}

.box--smooth:hover,
.box--smooth:focus-visible {
  border-radius: 50%;
  background-color: red;
  transform: scale(1.25);
}

.box--smooth:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .box--smooth {
    transition: none;
  }

  .box--smooth:hover,
  .box--smooth:focus-visible {
    transform: none;
  }
}
```

---

# 47. 버튼 Hover 패턴

```css
.button {
  border: 1px solid #2563eb;
  color: white;
  background-color: #2563eb;
  transition:
    background-color 0.2s ease,
    border-color 0.2s ease;
}

.button:hover,
.button:focus-visible {
  border-color: #1d4ed8;
  background-color: #1d4ed8;
}
```

버튼 크기를 바꾸지 않아 주변 레이아웃이 흔들리지 않습니다.

---

# 48. 카드 Hover 패턴

```css
.card {
  transition:
    box-shadow 0.2s ease,
    transform 0.2s ease;
}

.card:hover,
.card:focus-within {
  transform: translateY(-4px);
  box-shadow:
    0 12px 30px
    rgb(0 0 0 / 16%);
}
```

카드 안 링크가 포커스되면 `:focus-within`으로 카드 전체를 강조할 수 있습니다.

---

# 49. 메뉴 링크 패턴

```css
.nav-link {
  color: #374151;
  text-decoration-color: transparent;
  transition:
    color 0.2s ease,
    text-decoration-color 0.2s ease;
}

.nav-link:hover,
.nav-link:focus-visible {
  color: #2563eb;
  text-decoration-color: currentColor;
}
```

링크의 클릭 영역이나 레이아웃 크기를 바꾸지 않고 상태를 표현합니다.

---

# 50. Transition이 작동하지 않을 때 점검

1. 시작값과 종료값이 실제로 다른가?
2. transition이 변화 전 상태에 적용되어 있는가?
3. duration이 `0s`가 아닌가?
4. property 이름이 바뀌는 속성과 일치하는가?
5. `display`처럼 일반 transition이 어려운 속성인가?
6. 시작값 또는 종료값이 `auto`인가?
7. 더 높은 우선순위 규칙이 덮고 있는가?
8. `prefers-reduced-motion` 규칙이 transition을 제거했는가?
9. hover가 실제 요소에 적용되는가?
10. 개발자 도구에서 Computed 값을 확인했는가?

---

# 51. Hover 해제가 즉시 되는 경우 점검

1. transition이 `:hover` 안에만 있는가?
2. 기본 상태에 transition이 있는가?
3. hover가 해제될 때 property가 달라지는가?
4. class가 JavaScript로 즉시 제거되는가?
5. duration이 상태마다 다르게 지정됐는가?
6. 마우스 이동으로 요소 자체가 움직여 hover가 풀리는가?
7. width/height 변화가 포인터 영역을 바꾸는가?
8. transition shorthand가 뒤에서 초기화되는가?
9. 모바일 터치 환경인가?
10. 양방향 동작이 실제 요구사항인지 확인했는가?

---

# 52. 자주 하는 실수

## 52.1 Transition을 hover에만 작성

진입은 부드럽고 해제는 즉시 될 수 있습니다.

## 52.2 모든 요소에 `all`

예상하지 못한 속성까지 애니메이션될 수 있습니다.

## 52.3 Duration 단위 누락

```css
transition: width 0.5;
```

시간 단위가 없어 유효하지 않습니다.

```css
transition: width 0.5s;
```

## 52.4 Width·height 확대 남용

주변 요소가 밀리고 레이아웃 계산 비용이 커질 수 있습니다.

## 52.5 Hover만 제공

키보드와 터치 사용자가 같은 상태를 확인하지 못할 수 있습니다.

## 52.6 너무 긴 Transition

버튼이 느리게 반응하는 것처럼 느껴질 수 있습니다.

## 52.7 `display: none`을 바로 Transition

일반적인 방식으로 중간 상태를 만들기 어렵습니다.

## 52.8 시작값이 `auto`

고정 길이와 자연스럽게 보간되지 않을 수 있습니다.

## 52.9 색상만으로 상태 전달

아이콘, 텍스트, ARIA 상태를 함께 검토합니다.

## 52.10 Reduced motion 미고려

움직임에 민감한 사용자에게 불편할 수 있습니다.

---

# 53. 면접·복습 포인트

## Q1. CSS transition은 무엇인가요?

한 CSS 상태에서 다른 상태로 값이 바뀔 때 중간값을 시간에 따라 자동으로 만들어 주는 기능입니다.

## Q2. Transition을 기본 상태에 작성하는 이유는 무엇인가요?

hover 진입뿐 아니라 hover 해제 시에도 같은 transition 선언이 유지되어 양방향 전환이 가능하기 때문입니다.

## Q3. `transition: width 1s`는 무엇을 의미하나요?

width 속성만 1초 동안 전환합니다.

## Q4. `transition: all 0.5s`의 단점은 무엇인가요?

의도하지 않은 속성까지 전환될 수 있고 이후 추가된 속성도 자동으로 애니메이션되어 디버깅과 성능 관리가 어려워질 수 있습니다.

## Q5. Duration에서 `0.5s`와 `500ms`는 같은가요?

같습니다.

## Q6. Timing function은 무엇을 결정하나요?

전환 시간 동안 변화 속도가 어떻게 진행되는지를 결정합니다.

## Q7. Width와 height 대신 transform을 사용하는 이유는 무엇인가요?

실제 레이아웃 크기를 변경하지 않아 주변 요소 이동과 레이아웃 계산을 줄일 수 있기 때문입니다.

## Q8. Transition과 animation의 차이는 무엇인가요?

Transition은 보통 상태 변화가 필요하고 두 상태 사이를 연결합니다. Animation은 keyframes로 여러 단계를 정의하고 자동 반복이나 재생을 구성할 수 있습니다.

## Q9. Hover 효과에 focus 상태가 필요한 이유는 무엇인가요?

키보드 사용자는 hover를 사용할 수 없으므로 같은 시각적 피드백과 포커스 위치 확인이 필요합니다.

## Q10. `prefers-reduced-motion`은 왜 사용하나요?

시스템에서 움직임 감소를 요청한 사용자에게 불필요한 확대, 이동, 애니메이션을 줄이기 위해 사용합니다.

---

# Problems

## 문제 1. Width Transition

`.box`의 너비 변화만 1초 동안 전환하세요.

## 문제 2. All Transition

모든 전환 가능한 속성을 0.5초 동안 전환하세요.

## 문제 3. 개별 속성

배경색은 0.2초, border-radius는 0.4초 동안 전환하세요.

## 문제 4. Timing Function

transform을 0.3초 동안 `ease-out`으로 전환하세요.

## 문제 5. Delay

opacity를 0.5초 동안 전환하되 0.2초 뒤 시작하세요.

## 문제 6. 소수점 시간

75밀리초를 초 단위 소수점으로 작성하세요.

## 문제 7. Hover 위치 오류

다음 코드의 문제를 설명하세요.

```css
.box:hover {
  width: 200px;
  transition: width 0.5s;
}
```

## 문제 8. 양방향 전환

문제 7을 hover 진입과 해제 모두 0.5초가 되도록 수정하세요.

## 문제 9. 원본 Box1

기본 100px 초록 사각형이 hover 시 200px 빨간 원으로 즉시 변하도록 작성하세요.

## 문제 10. 원본 Box2 개선

문제 9와 같은 변화가 양방향 0.5초로 동작하도록 작성하세요.

## 문제 11. `all` 개선

원본에서 실제로 바뀌는 네 속성만 명시하세요.

## 문제 12. Background 속성

단색 배경만 변경할 때 `background`보다 `background-color`가 더 명확한 이유를 설명하세요.

## 문제 13. Transform 대안

width와 height를 200px로 바꾸는 대신 `scale(2)`를 사용하세요.

## 문제 14. Focus

hover와 키보드 focus에서 같은 상태가 되도록 작성하세요.

## 문제 15. Outline

focus 시 파란색 3px outline과 3px offset을 제공하세요.

## 문제 16. Reduced Motion

움직임 감소 환경에서 transition과 transform을 제거하세요.

## 문제 17. 레이아웃 변화

width와 height transition이 주변 요소에 미칠 수 있는 영향을 설명하세요.

## 문제 18. Display

`display: none`에서 `display: block`으로 일반 transition이 어려운 이유를 설명하세요.

## 문제 19. Auto 값

`height: auto`와 `height: 300px` 사이 transition이 원하는 대로 동작하지 않을 수 있는 이유를 설명하세요.

## 문제 20. Transition Token

기본 duration과 easing을 CSS 변수로 선언하세요.

## 문제 21. 접근성

색상 변화만으로 버튼 선택 상태를 전달하지 않도록 HTML과 CSS를 개선하세요.

## 문제 22. 종합 카드

다음 요구사항을 만족하는 카드 링크를 작성하세요.

- 실제 `<a>` 사용
- 기본 그림자
- hover와 focus 시 위로 `4px` 이동
- 큰 그림자
- transform과 box-shadow만 transition
- duration `0.2s`
- `ease-out`
- focus outline
- reduced motion 대응
- 카드 목록은 Grid와 gap 사용
- 색상 변화만으로 상태를 전달하지 않음

---

# Answers & Explanations

## 정답 1

```css
.box {
  transition: width 1s;
}
```

## 정답 2

```css
.box {
  transition: all 0.5s;
}
```

학습 실험에는 간단하지만 실무에서는 필요한 속성 명시를 검토합니다.

## 정답 3

```css
.box {
  transition:
    background-color 0.2s,
    border-radius 0.4s;
}
```

## 정답 4

```css
.box {
  transition:
    transform 0.3s ease-out;
}
```

## 정답 5

```css
.box {
  transition:
    opacity 0.5s ease 0.2s;
}
```

## 정답 6

```text
0.075s
```

## 정답 7

transition이 hover 상태 안에만 있으므로 hover 진입 시에는 적용될 수 있지만 hover가 해제되면 transition 선언도 사라져 즉시 원래 너비로 돌아갈 수 있습니다.

## 정답 8

```css
.box {
  width: 100px;
  transition: width 0.5s;
}

.box:hover {
  width: 200px;
}
```

## 정답 9

```css
.box {
  width: 100px;
  height: 100px;
  background-color: green;
}

.box:hover {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background-color: red;
}
```

## 정답 10

```css
.box {
  width: 100px;
  height: 100px;
  background-color: green;
  transition:
    width 0.5s,
    height 0.5s,
    border-radius 0.5s,
    background-color 0.5s;
}

.box:hover {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background-color: red;
}
```

## 정답 11

```css
.box {
  transition:
    background-color 0.5s,
    border-radius 0.5s,
    width 0.5s,
    height 0.5s;
}
```

## 정답 12

`background`는 이미지, 반복, 위치 등 여러 배경 관련 속성을 초기화할 수 있는 단축 속성입니다. 배경색만 변경한다면 `background-color`가 의도를 명확하게 표현하고 기존 배경 설정을 유지하기 쉽습니다.

## 정답 13

```css
.box {
  width: 100px;
  height: 100px;
  transition:
    transform 0.5s,
    background-color 0.5s,
    border-radius 0.5s;
}

.box:hover {
  transform: scale(2);
  background-color: red;
  border-radius: 50%;
}
```

## 정답 14

```css
.box:hover,
.box:focus-visible {
  background-color: red;
  border-radius: 50%;
  transform: scale(1.1);
}
```

## 정답 15

```css
.box:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}
```

## 정답 16

```css
@media (prefers-reduced-motion: reduce) {
  .box {
    transition: none;
  }

  .box:hover,
  .box:focus-visible {
    transform: none;
  }
}
```

## 정답 17

실제 박스 크기가 프레임마다 바뀌어 주변 요소가 밀리거나 위치가 변경될 수 있습니다. 브라우저가 반복해서 레이아웃을 계산해야 하므로 많은 요소에서 사용하면 성능 부담이 커질 수 있습니다.

## 정답 18

`display`는 일반적으로 중간값을 계산하는 연속적인 속성이 아니라 상태가 즉시 바뀌는 discrete 속성이기 때문입니다.

## 정답 19

브라우저가 `auto`의 수치값을 일반적인 길이값처럼 직접 보간하기 어렵기 때문입니다. `max-height`, Grid 행, transform, JavaScript 측정 등 다른 방식을 검토합니다.

## 정답 20

```css
:root {
  --duration-fast: 0.2s;
  --ease-out:
    cubic-bezier(0, 0, 0.2, 1);
}
```

사용:

```css
.card {
  transition:
    transform
    var(--duration-fast)
    var(--ease-out);
}
```

## 정답 21

### HTML

```html
<button
  class="choice"
  type="button"
  aria-pressed="true"
>
  <span aria-hidden="true">✓</span>
  선택됨
</button>
```

### CSS

```css
.choice[aria-pressed="true"] {
  border-color: #2563eb;
  background-color: #dbeafe;
  font-weight: 700;
}
```

색상뿐 아니라 체크 아이콘, 텍스트, 굵기, ARIA 상태를 제공합니다.

## 정답 22

### HTML

```html
<div class="card-list">
  <a class="learning-card" href="/css/transition">
    <h2>CSS Transition</h2>
    <p>상태 변화의 중간 과정을 학습합니다.</p>
    <span class="learning-card__action">
      학습하기 →
    </span>
  </a>

  <a class="learning-card" href="/css/transform">
    <h2>CSS Transform</h2>
    <p>요소의 이동과 확대를 학습합니다.</p>
    <span class="learning-card__action">
      학습하기 →
    </span>
  </a>
</div>
```

### CSS

```css
.card-list {
  display: grid;
  gap: 2rem;
}

.learning-card {
  display: block;
  padding: 1.5rem;
  border: 1px solid #d1d5db;
  border-radius: 1rem;
  color: inherit;
  text-decoration: none;
  box-shadow:
    0 2px 8px
    rgb(0 0 0 / 10%);
  transition:
    transform 0.2s ease-out,
    box-shadow 0.2s ease-out;
}

.learning-card:hover,
.learning-card:focus-visible {
  transform: translateY(-4px);
  box-shadow:
    0 12px 30px
    rgb(0 0 0 / 18%);
}

.learning-card:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}

.learning-card__action {
  display: inline-block;
  margin-top: 1rem;
  font-weight: 700;
}

@media (prefers-reduced-motion: reduce) {
  .learning-card {
    transition: none;
  }

  .learning-card:hover,
  .learning-card:focus-visible {
    transform: none;
  }
}
```

---

# Final Checklist

## Transition 기본

- [ ] 시작 상태와 종료 상태가 실제로 다르다.
- [ ] transition을 변화 전 기본 상태에 작성했다.
- [ ] property와 duration 순서를 확인했다.
- [ ] 시간 단위 `s` 또는 `ms`를 작성했다.
- [ ] 소수점 시간값을 올바르게 사용했다.
- [ ] timing function과 delay를 구분했다.

## 속성 선택

- [ ] 무조건 `all`을 사용하지 않았다.
- [ ] 실제로 바뀌는 속성만 명시했다.
- [ ] 단색 변경에는 `background-color`를 검토했다.
- [ ] width와 height 변화가 꼭 필요한지 확인했다.
- [ ] transform과 opacity로 대체할 수 있는지 검토했다.
- [ ] `auto` 값과 discrete 속성의 한계를 이해했다.

## 상호작용

- [ ] hover 진입과 해제 모두 의도대로 동작한다.
- [ ] 키보드 focus 상태가 있다.
- [ ] focus outline이 즉시 보인다.
- [ ] 실제 역할에 맞는 button 또는 a를 사용했다.
- [ ] 터치 환경에서 핵심 기능을 사용할 수 있다.
- [ ] 색상 변화만으로 상태를 전달하지 않았다.

## 접근성과 움직임

- [ ] `prefers-reduced-motion`을 고려했다.
- [ ] 확대와 이동이 과도하지 않다.
- [ ] transition이 기능 실행을 불필요하게 지연하지 않는다.
- [ ] 시각 효과 없이도 콘텐츠와 기능을 이해할 수 있다.
- [ ] 레이아웃 이동이 포인터와 포커스를 방해하지 않는다.

## 성능과 유지보수

- [ ] width·height 전환의 레이아웃 비용을 확인했다.
- [ ] 많은 요소에 큰 그림자 transition을 남용하지 않았다.
- [ ] 공통 duration과 easing을 변수로 관리했다.
- [ ] `will-change`를 남용하지 않았다.
- [ ] 실제 저사양 모바일에서 테스트했다.
- [ ] 개발자 도구에서 transition property를 확인했다.

## 원본 코드 검수

- [ ] `lang="en"`을 `lang="ko"`로 개선했다.
- [ ] `Document` 제목을 학습 주제로 변경했다.
- [ ] 내 코드의 hover transition 설명을 정확하게 보완했다.
- [ ] 내 코드의 소수점 시간 설명을 보존했다.
- [ ] `background`와 `background-color` 차이를 오류로 처리하지 않았다.
- [ ] 강사님 두 번째 박스의 `박스2` 차이를 보존했다.
- [ ] 원본의 `transition: width 1s` 실험값을 설명했다.
- [ ] 원본의 `transition: all 0.5s` 장단점을 설명했다.

---

# Key Summary

- CSS transition은 두 상태 사이의 속성값 변화를 시간에 따라 부드럽게 연결한다.
- transition이 동작하려면 시작값과 종료값이 필요하다.
- 단축 속성은 property, duration, timing function, delay 순서로 작성할 수 있다.
- duration에는 `s`와 `ms`를 사용하며 소수점 초도 가능하다.
- 원본의 `transition: width 1s`는 width만 1초 동안 전환한다.
- 원본의 `transition: all 0.5s`는 여러 전환 가능한 속성을 한 번에 처리한다.
- `all`은 편리하지만 의도하지 않은 속성까지 전환할 수 있다.
- transition을 hover 규칙에만 두면 hover 진입에는 적용되고 해제 시 즉시 복귀할 수 있다.
- 양방향 전환을 원하면 transition을 기본 상태에 작성한다.
- 원본 `.box1`은 transition이 없어 즉시 크기와 색상이 바뀐다.
- 원본 `.box2`는 hover 규칙 안에 transition이 있어 진입과 해제 동작이 다를 수 있다.
- 내 코드는 `background`, 강사님 코드는 `background-color`를 사용하며 현재 단색 결과는 같다.
- 강사님의 두 번째 박스 텍스트는 `박스2`, 내 코드는 `박스`다.
- width와 height transition은 실제 레이아웃 크기를 바꿔 주변 요소를 밀 수 있다.
- 시각적 확대에는 `transform: scale()`이 더 적절한 경우가 많다.
- transform과 opacity는 일반적으로 transition 성능에 유리한 경우가 많다.
- hover 효과는 키보드 사용자를 위해 `:focus-visible`과 함께 제공한다.
- focus outline은 transition 효과와 별개로 명확하게 보여야 한다.
- 색상 변화만으로 선택이나 상태를 전달하지 않는다.
- 움직임에 민감한 사용자를 위해 `prefers-reduced-motion`을 고려한다.
- transition은 장식적 개선이며 핵심 기능의 실행을 지연시키지 않아야 한다.
