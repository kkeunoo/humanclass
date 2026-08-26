---
title: CSS Transform과 요소 변형
version: v3.0-encyclopedia
last_updated: 2026-08-07
status: Completed
---

# CSS Transform과 요소 변형

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `13_CSS_Transform과_요소변형.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_html/css/13_tranform.html`, `workspace_teacher/workspace_html/css/13_transform.html` |
| 핵심 범위 | `translate()`, `scale()`, `scaleX()`, `rotate()`, 복합 transform, transform 순서, 절대 위치 중앙 정렬 |
| 프로젝트 연결 | 카드 hover, 버튼 이동, 확대·축소, 회전 아이콘, 모달 중앙 정렬, 이미지 인터랙션 |

> 이 문서는 내 코드의 `13_tranform.html`과 강사님 코드의 `13_transform.html`을 비교해 `translate`, `scale`, `rotate`, 복합 Transform과 중앙 정렬의 실제 동작을 정리한다. 내 파일명의 `tranform` 오타와 `scaleX()`·`scale()` 차이는 그대로 기록하고, Transform 순서·기준점·접근성·성능까지 실무 패턴으로 연결한다.

---

# 학습 목표

- `transform`이 요소의 시각적 좌표계를 변형하는 속성임을 설명한다.
- `translate()`로 요소를 가로·세로 이동한다.
- `translate()`의 퍼센트가 부모가 아니라 요소 자신의 크기를 기준으로 계산된다는 점을 이해한다.
- `scale()`, `scaleX()`, `scaleY()`의 차이를 설명한다.
- `rotate()`의 양수와 음수 회전 방향을 이해한다.
- 여러 transform 함수를 한 선언에 조합한다.
- transform 함수의 작성 순서가 최종 결과에 영향을 준다는 점을 설명한다.
- transform이 일반 문서 흐름의 원래 공간을 유지한다는 점을 이해한다.
- `position: absolute`, `top: 50%`, `left: 50%`, `translate(-50%, -50%)`를 이용해 중앙 정렬한다.
- `transform-origin`의 역할을 이해한다.
- transition과 transform을 함께 사용해 부드러운 상태 변화를 만든다.
- hover뿐 아니라 focus와 reduced motion을 고려한다.
- 내 코드와 강사님 코드의 차이와 원본 파일명 오류를 찾는다.

---

# 1. Transform이란?

`transform`은 요소를 이동, 확대·축소, 회전, 기울이기 할 수 있는 CSS 속성입니다.

대표 함수:

```css
transform: translate(...);
transform: scale(...);
transform: rotate(...);
transform: skew(...);
```

여러 함수를 함께 사용할 수도 있습니다.

```css
transform:
  translate(20px, 10px)
  scale(1.2)
  rotate(10deg);
```

transform은 일반적으로 요소의 **시각적 표시 결과**를 바꾸며, 원래 레이아웃 공간 자체를 다시 계산하지 않습니다.

---

# 2. 원본 HTML 구조

내 코드와 강사님 코드는 다음 박스를 사용합니다.

```html
<div class="box">비교</div>
<div class="box translate">translate</div>
<div class="box scale">scale</div>
<div class="box rotate">rotate</div>
<div class="box total">total</div>
```

마지막에는 부모 안의 자식을 중앙에 배치하는 예제가 있습니다.

```html
<div class="parent">
  <div class="child"></div>
</div>
```

---

# 3. 원본 공통 `.box`

내 코드:

```css
.box {
  border: 1px solid red;
  width: 100px;
  height: 100px;
  background-color: green;
  color: white;
  margin: 30px;

  transition: transform 0.5s;
}
```

강사님 코드:

```css
.box {
  border:1px solid red;
  height: 100px;
  width: 100px;
  background-color: green;
  color: white;
  margin: 30px;

  transition: all .5s
}
```

실제 결과는 거의 같습니다.

차이:

- 내 코드: `border: 1px solid red`
- 강사님: `border:1px solid red`
- 내 코드: `0.5s`
- 강사님: `.5s`
- 내 코드: 마지막 세미콜론 있음
- 강사님: `transition: all .5s` 뒤 세미콜론 없음

마지막 선언이라 브라우저가 처리할 수 있지만 세미콜론을 작성하는 편이 좋습니다.

---

# 4. Transform과 Transition 연결

원본 공통 박스:

```css
transition: transform 0.5s;
```

hover 상태에서 transform 값이 바뀌므로 0.5초 동안 부드럽게 변형됩니다.

더 명확한 작성:

```css
.box {
  transition: transform 0.5s;
}
```

원본에서는 transform만 바뀌므로 `all`보다 필요한 속성을 직접 지정하는 편이 안전합니다.

---

# 5. `translate()`

기본 문법:

```css
transform: translate(x, y);
```

예:

```css
transform: translate(10px, 20px);
```

의미:

```text
오른쪽 10px
아래쪽 20px
```

축별 함수:

```css
transform: translateX(10px);
transform: translateY(20px);
```

---

# 6. 원본 translate 실험값

내 코드와 강사님 코드:

```css
.translate:hover {
  /* transform: translate(10px, 20px); */
  transform: translate(50%, 50%);
}
```

주석 처리된 값은 px 이동 실험이고, 실제 적용값은 퍼센트 이동입니다.

```text
x축 50%
y축 50%
```

---

# 7. Translate 퍼센트의 기준

중요:

```css
transform: translate(50%, 50%);
```

transform의 translate 퍼센트는 일반적으로 **변형되는 요소 자신의 크기**를 기준으로 계산됩니다.

원본 박스:

```css
width: 100px;
height: 100px;
```

따라서 대략:

```text
translateX(50%) → 자신의 너비 100px의 절반 = 50px
translateY(50%) → 자신의 높이 100px의 절반 = 50px
```

즉, 오른쪽 50px, 아래 50px 이동합니다.

이는 `position: absolute; left: 50%`의 퍼센트 기준과 다릅니다.

---

# 8. `left: 50%`와 `translateX(50%)` 차이

```css
left: 50%;
```

일반적으로 containing block의 너비를 기준으로 합니다.

```css
transform: translateX(50%);
```

요소 자신의 참조 박스 너비를 기준으로 합니다.

비교:

```text
left: 50%          → 부모 기준
translateX(50%)    → 자기 자신 기준
```

이 차이는 중앙 정렬 공식에서 매우 중요합니다.

---

# 9. Transform은 원래 공간을 유지한다

```css
.box:hover {
  transform: translate(100px, 0);
}
```

박스는 화면에서 오른쪽으로 이동하지만 원래 자리의 레이아웃 공간은 유지됩니다.

뒤 요소는 이동한 박스를 기준으로 다시 배치되지 않습니다.

따라서 이동한 요소가 다른 요소와 겹칠 수 있습니다.

이는 CSS 08의 `position: relative` 시각 이동과 비슷한 결과를 만들 수 있지만, 동작 원리와 사용 목적은 다릅니다.

---

# 10. `scale()`

기본 문법:

```css
transform: scale(x, y);
```

한 값:

```css
transform: scale(1.5);
```

x축과 y축을 모두 1.5배 확대합니다.

두 값:

```css
transform: scale(1.5, 0.8);
```

```text
가로 1.5배
세로 0.8배
```

---

# 11. 축별 Scale

```css
transform: scaleX(1.5);
transform: scaleY(1.5);
```

- `scaleX()`: 가로축만
- `scaleY()`: 세로축만

원본은 `scaleX(1.5)`를 실제 적용합니다.

---

# 12. 내 코드의 scale 주석

내 코드:

```css
.scale:hover {
  /* scale은 X축, Y축도 별개로 지정이 가능하다 */
  /* transform: scale(1.5); */
  transform: scaleX(1.5);
}
```

강사님:

```css
.scale:hover {
  /* transform: scale(1.5); */
  transform: scaleX(1.5);
}
```

내 코드에는 축별 확대가 가능하다는 설명이 추가되어 있습니다.

실제 결과:

```text
가로만 1.5배 확대
세로 크기는 유지
```

---

# 13. Scale 값의 의미

```text
scale(1)
```

원래 크기입니다.

```text
scale(1.5)
```

1.5배 확대합니다.

```text
scale(0.5)
```

절반 크기로 축소합니다.

```text
scale(0)
```

시각적으로 크기가 0이 됩니다.

```text
scale(-1)
```

해당 축을 뒤집는 반전 효과가 생길 수 있습니다.

---

# 14. Scale과 레이아웃

```css
transform: scale(1.5);
```

요소가 시각적으로 커져도 원래 레이아웃 공간은 그대로입니다.

따라서 주변 요소를 밀지 않고 겹칠 수 있습니다.

원본 `.box`의 margin이 `30px`이지만 1.5배 확대된 박스가 인접 요소와 겹치는지 확인해야 합니다.

---

# 15. `rotate()`

기본 문법:

```css
transform: rotate(30deg);
```

각도 단위:

```text
deg  → 도
turn → 회전 수
rad  → 라디안
grad → 그라디안
```

대표 사용:

```text
rotate(90deg)
rotate(0.5turn)
```

---

# 16. 원본 Rotate

내 코드와 강사님 코드:

```css
.rotate:hover {
  /* transform: rotate(30deg); */
  transform: rotate(-30deg);
}
```

실제 적용값은 음수 30도입니다.

일반적인 화면 좌표계에서:

```text
양수 각도 → 시계 방향
음수 각도 → 반시계 방향
```

따라서 `-30deg`는 반시계 방향으로 회전합니다.

---

# 17. 회전 중심

기본적으로 요소의 중심을 기준으로 회전합니다.

```css
transform-origin: center;
```

왼쪽 위를 기준:

```css
transform-origin: top left;
```

예:

```css
.door {
  transform-origin: left center;
}

.door:hover {
  transform: rotateY(45deg);
}
```

원본에는 `transform-origin`이 없으므로 기본 중심점을 사용합니다.

---

# 18. 복합 Transform

여러 함수를 공백으로 이어 작성합니다.

```css
transform:
  translate(50%, 50%)
  scale(1.5)
  rotate(-30deg);
```

원본 `.total`은 이동, 확대, 회전을 한 번에 적용합니다.

---

# 19. 내 코드와 강사님의 total 차이

내 코드:

```css
.total:hover {
  /* transform: rotate(30deg); */
  transform:
    translate(50%, 50%)
    scaleX(1.5)
    rotate(-30deg);
}
```

강사님:

```css
.total:hover {
  transform:
    translate(50%, 50%)
    scale(1.5)
    rotate(-30deg);
}
```

핵심 차이:

| 코드 | 확대 결과 |
| --- | --- |
| 내 코드 `scaleX(1.5)` | 가로만 1.5배 |
| 강사님 `scale(1.5)` | 가로·세로 모두 1.5배 |

따라서 두 원본의 `total` 결과는 동일하지 않습니다.

---

# 20. 내 코드 total 주석 문제

내 코드:

```css
/* transform: rotate(30deg); */
```

`.total`은 이동·확대·회전을 조합하는 예제인데 주석에는 회전 하나만 남아 있습니다.

이전 실험값이 복사된 것으로 보입니다.

개선:

```css
/*
  translate, scaleX, rotate를
  한 transform 선언에 조합
*/
```

원본 주석은 삭제하지 않고 실험 흔적으로 기록합니다.

---

# 21. Transform 함수 순서

다음 두 코드는 결과가 다를 수 있습니다.

```css
transform:
  translateX(100px)
  rotate(30deg);
```

```css
transform:
  rotate(30deg)
  translateX(100px);
```

transform 함수는 작성 순서에 따라 좌표계가 달라집니다.

쉽게 이해하면:

```text
먼저 작성된 함수와 뒤 함수가
행렬로 결합되며 최종 좌표가 달라질 수 있음
```

따라서 복합 transform의 순서는 디자인 결과의 일부입니다.

---

# 22. 원본 순서

원본:

```css
transform:
  translate(50%, 50%)
  scale(...)
  rotate(-30deg);
```

이 순서를 임의로 바꾸면 이동 방향과 최종 위치가 달라질 수 있습니다.

코드 리뷰에서는 함수 종류뿐 아니라 순서도 비교해야 합니다.

---

# 23. Transform 덮어쓰기

다음처럼 여러 번 작성하면 합쳐지지 않습니다.

```css
.box {
  transform: translateX(20px);
  transform: rotate(30deg);
}
```

최종 적용:

```css
transform: rotate(30deg);
```

두 효과를 함께 쓰려면 한 선언에 작성합니다.

```css
transform:
  translateX(20px)
  rotate(30deg);
```

---

# 24. 개별 Transform 속성 확장 학습

현대 CSS에서는 개별 속성을 사용할 수 있습니다.

```css
.box {
  translate: 20px 10px;
  scale: 1.2;
  rotate: 10deg;
}
```

기존 `transform` 함수와 브라우저 지원, 적용 순서 차이를 프로젝트 환경에서 확인해야 합니다.

원본은 전통적인 `transform` 함수 문법을 사용합니다.

---

# 25. 원본 중앙 정렬 부모

내 코드:

```css
.parent {
  border: 1px solid red;
  width: 40%;
  height: 40vh;

  position: relative;
}
```

강사님 코드도 같습니다.

부모의 역할:

- 너비 `40%`
- 높이 `40vh`
- 절대 위치 자식의 containing block
- 빨간 테두리로 영역 표시

---

# 26. 부모 너비 40%

```css
width: 40%;
```

퍼센트 너비는 일반적으로 containing block의 너비를 기준으로 계산합니다.

부모 `.parent`가 body 안의 일반 블록이므로 body의 사용 가능한 너비를 기준으로 약 40%가 됩니다.

---

# 27. 부모 높이 40vh

```css
height: 40vh;
```

`vh`는 뷰포트 높이를 기준으로 합니다.

```text
40vh → 뷰포트 높이의 40%
```

모바일에서는 브라우저 UI 변화로 뷰포트 단위가 다르게 느껴질 수 있습니다.

현대 단위:

```css
height: 40dvh;
```

원본은 기본 `vh` 학습 예제이므로 그대로 보존합니다.

---

# 28. 원본 중앙 정렬 자식

내 코드:

```css
.parent .child {
  border: 1px solid blue;
  width: 30%;
  height: 30%;

  position: absolute;

  top: 50%;
  left: 50%;

  transform: translate(-50%, -50%);
}
```

강사님:

```css
.parent .child {
  border: 1px solid blueviolet;
  width: 30%;
  height: 30%;

  position: absolute;
  top: 50%;
  left: 50%;

  transform: translate(-50%, -50%);
}
```

테두리 색상만 다릅니다.

```text
내 코드: blue
강사님: blueviolet
```

---

# 29. 중앙 정렬 계산 1단계

```css
top: 50%;
left: 50%;
```

자식의 **왼쪽 위 모서리**를 부모의 중앙점으로 이동시킵니다.

이 상태에서는 자식 전체가 중앙보다 오른쪽 아래에 위치합니다.

---

# 30. 중앙 정렬 계산 2단계

```css
transform: translate(-50%, -50%);
```

자식 자신의 너비와 높이 절반만큼 왼쪽과 위로 되돌립니다.

```text
translateX(-50%) → 자식 자신의 너비 절반
translateY(-50%) → 자식 자신의 높이 절반
```

결과적으로 자식의 중심이 부모의 중심과 일치합니다.

---

# 31. 중앙 정렬 기준 비교

```text
top: 50%, left: 50%
→ 부모 크기 기준

translate(-50%, -50%)
→ 자식 자신의 크기 기준
```

이 서로 다른 기준을 조합하는 것이 핵심입니다.

자식의 크기가 바뀌어도 중앙 정렬이 유지됩니다.

---

# 32. CSS 08의 calc 방식과 비교

고정 크기 계산:

```css
top: calc(400px / 2 - 100px / 2);
left: calc(400px / 2 - 100px / 2);
```

Transform 방식:

```css
top: 50%;
left: 50%;
transform: translate(-50%, -50%);
```

Transform 방식의 장점:

- 부모 고정 크기를 몰라도 됨
- 자식 고정 크기를 몰라도 됨
- 반응형 크기에 대응
- 계산식 수정이 적음

---

# 33. Flexbox·Grid 중앙 정렬과 비교

겹침이나 절대 위치가 필요하지 않다면 Grid가 더 간단합니다.

```css
.parent {
  display: grid;
  place-items: center;
}
```

Flexbox:

```css
.parent {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

선택 기준:

| 목적 | 권장 |
| --- | --- |
| 일반적인 중앙 배치 | Grid/Flex |
| 다른 콘텐츠 위에 겹치는 요소 | absolute + transform |
| 모달·오버레이 패널 | fixed/absolute + transform 또는 Grid |
| 배지·아이콘 | absolute |

---

# 34. Transform과 Stacking Context

transform 값이 `none`이 아니면 새로운 stacking context를 만들 수 있습니다.

```css
.card {
  transform: translateY(0);
}
```

이로 인해 `z-index` 동작이 예상과 달라질 수 있습니다.

CSS 08에서 배운 stacking context와 연결됩니다.

확인:

- 부모 transform
- 자식 fixed 요소
- z-index 그룹
- overflow 잘림

---

# 35. Transform과 Fixed 기준

특정 조상에 transform이 적용되면 그 안의 `position: fixed` 요소가 뷰포트가 아니라 해당 조상을 기준으로 동작하는 것처럼 보일 수 있습니다.

```css
.wrapper {
  transform: translateZ(0);
}
```

```css
.fixed-child {
  position: fixed;
}
```

따라서 성능 최적화 목적으로 무조건 transform을 부모에 추가하지 않습니다.

---

# 36. Transform과 Overflow

scale이나 rotate로 요소가 부모 밖으로 나가면 부모의 overflow 설정에 따라 잘릴 수 있습니다.

```css
.wrapper {
  overflow: hidden;
}

.card:hover {
  transform: scale(1.2);
}
```

그림자와 마찬가지로 확대된 부분이 잘리는지 확인합니다.

---

# 37. Transform과 글자 선명도

소수점 이동이나 확대·회전 시 글자가 약간 흐릿하게 보일 수 있습니다.

```css
transform: translateX(0.5px);
```

브라우저의 픽셀 렌더링과 장치 배율에 따라 결과가 달라집니다.

중요한 본문 텍스트를 크게 확대·회전하는 효과는 가독성을 확인합니다.

---

# 38. Hover뿐 아니라 Focus

원본은 `div:hover`를 사용합니다.

실제 클릭 요소라면:

```html
<button class="box scale" type="button">
  확대
</button>
```

```css
.scale:hover,
.scale:focus-visible {
  transform: scale(1.1);
}
```

키보드 사용자도 같은 피드백을 받을 수 있습니다.

---

# 39. Focus Outline

```css
.box:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}
```

transform으로 확대하거나 이동해도 포커스 표시가 잘리는지 확인합니다.

부모의 `overflow: hidden`이 outline을 자를 수 있습니다.

---

# 40. Reduced Motion

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

회전, 확대, 큰 이동은 움직임에 민감한 사용자에게 불편할 수 있습니다.

색상이나 테두리 상태를 대체 피드백으로 제공할 수 있습니다.

---

# 41. Transform Origin

```css
transform-origin: center center;
```

기본값은 일반적으로 요소 중심입니다.

다른 예:

```css
transform-origin: top left;
transform-origin: 0 0;
transform-origin: 100% 50%;
```

회전과 확대의 기준점을 변경합니다.

```css
.menu-icon {
  transform-origin: center;
}
```

---

# 42. 3D Transform 확장 학습

대표 함수:

```text
rotateX()
rotateY()
rotateZ()
translateZ()
scaleZ()
```

원근감:

```css
.scene {
  perspective: 800px;
}
```

원본 CSS 13은 2D transform만 다룹니다.

3D transform은 확장 개념으로만 구분합니다.

---

# 43. 문서 언어와 제목

내 코드와 강사님 코드:

```html
<html lang="en">
<title>Document</title>
```

본문은 한국어를 포함하므로:

```html
<html lang="ko">
<title>CSS Transform</title>
```

로 개선합니다.

---

# 44. 원본 파일명 오타

내 코드 파일:

```text
13_tranform.html
```

강사님 파일:

```text
13_transform.html
```

내 코드 파일명에서 `transform`의 `s`가 빠졌습니다.

문서 링크나 수업 목차에서 `13_transform.html`을 예상하면 파일을 찾지 못할 수 있습니다.

개선 권장:

```text
13_tranform.html
→ 13_transform.html
```

다만 이 문서에서는 원본 오류를 숨기지 않고 두 이름을 모두 기록합니다.

---

# 45. 강사님 세미콜론 누락

강사님 코드:

```css
transition: all .5s
```

규칙의 마지막 선언이므로 브라우저가 처리할 수 있습니다.

권장:

```css
transition: transform 0.5s;
```

이후 속성을 추가할 때 문법 오류를 방지하고 코드 스타일을 일관되게 유지합니다.

---

# 46. 반복 `<br>`

내 코드 마지막:

```html
<br><br><br><br><br><br><br><br><br><br>
```

강사님 코드에는 없습니다.

하단 여백 목적이라면:

```css
body {
  padding-bottom: 10rem;
}
```

로 대체합니다.

학습 결과와 무관하다면 제거합니다.

---

# 47. 빈 Child 요소

원본:

```html
<div class="child"></div>
```

내 코드에는 여는 태그와 닫는 태그 사이에 빈 줄이 있습니다.

```html
<div class="child">

</div>
```

두 결과는 같습니다.

중앙 위치를 테두리로 확인하는 시각 실습이므로 내용이 없어도 목적을 수행합니다.

접근성 관점에서 실제 콘텐츠가 없는 장식 박스라면 별도 의미를 부여할 필요는 없습니다.

---

# 48. 내 코드 분석

## 48.1 장점

- `scale`이 x축과 y축을 별도로 지정할 수 있음을 설명했다.
- transition을 `0.5s`로 완전한 표기와 세미콜론으로 작성했다.
- 중앙 정렬 자식의 테두리를 단순한 `blue`로 구분했다.
- translate, scaleX, rotate를 조합해 복합 변형을 직접 실습했다.
- 하단 공간을 확보해 결과 확인을 쉽게 하려 한 것으로 보인다.

## 48.2 개선점

- 파일명이 `13_tranform.html`로 오타다.
- `.total`이 강사님과 달리 `scaleX(1.5)`를 사용한다.
- `.total` 주석이 복합 transform이 아니라 이전 rotate 실험값만 설명한다.
- `transition: all`보다 `transform`을 명시하는 편이 좋다.
- 반복 `<br>`를 CSS 여백으로 대체한다.
- hover만 있고 focus 상태가 없다.
- 문서 언어와 제목을 개선한다.

---

# 49. 강사님 코드 분석

## 49.1 장점

- 파일명이 정확한 `13_transform.html`이다.
- translate, scaleX, rotate, total을 최소 코드로 비교한다.
- `.total`에서 `scale(1.5)`를 사용해 가로와 세로를 모두 확대한다.
- 중앙 정렬 공식을 간결하게 보여 준다.
- 내 코드의 반복 `<br>`가 없다.
- 자식 테두리를 `blueviolet`으로 구분해 부모와 시각적으로 잘 분리한다.

## 49.2 개선점

- `transition: all .5s` 뒤 세미콜론이 없다.
- 필요한 속성인 `transform`만 transition하도록 개선할 수 있다.
- translate 퍼센트 기준 설명이 없다.
- transform 함수 순서 설명이 없다.
- focus와 reduced motion이 없다.
- 문서 언어가 `en`이고 제목이 `Document`다.

---

# 50. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 파일명 | `13_tranform.html` | `13_transform.html` |
| transition 표기 | `all 0.5s;` | `all .5s` |
| scale 설명 | x·y축 별도 가능 주석 | 주석 없음 |
| 단일 scale | `scaleX(1.5)` | `scaleX(1.5)` |
| total scale | `scaleX(1.5)` | `scale(1.5)` |
| total 결과 | 가로만 확대 | 가로·세로 확대 |
| child 테두리 | `blue` | `blueviolet` |
| 반복 `<br>` | 10개 | 없음 |
| 중앙 정렬 | 동일 | 동일 |
| 학습 성격 | 주석 추가 복습형 | 간결한 수업형 |

---

# 51. 원본 통합 개선 예제

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
  <title>CSS Transform</title>
  <link
    rel="stylesheet"
    href="asset/css/transform.css"
  >
</head>
<body>
  <main class="page">
    <h1>CSS Transform</h1>

    <div class="demo-list">
      <button class="box" type="button">
        비교
      </button>

      <button
        class="box box--translate"
        type="button"
      >
        translate
      </button>

      <button
        class="box box--scale"
        type="button"
      >
        scale
      </button>

      <button
        class="box box--rotate"
        type="button"
      >
        rotate
      </button>

      <button
        class="box box--total"
        type="button"
      >
        total
      </button>
    </div>

    <section class="parent">
      <div class="child">
        중앙
      </div>
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
  width: min(100% - 2rem, 60rem);
  margin-inline: auto;
  padding-block: 2rem;
}

.demo-list {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
}

.box {
  display: grid;
  width: 100px;
  height: 100px;
  border: 1px solid red;
  color: white;
  background-color: green;
  cursor: pointer;
  place-items: center;
  transition: transform 0.5s ease;
}

.box--translate:hover,
.box--translate:focus-visible {
  transform: translate(50%, 50%);
}

.box--scale:hover,
.box--scale:focus-visible {
  transform: scaleX(1.5);
}

.box--rotate:hover,
.box--rotate:focus-visible {
  transform: rotate(-30deg);
}

.box--total:hover,
.box--total:focus-visible {
  transform:
    translate(50%, 50%)
    scale(1.5)
    rotate(-30deg);
}

.box:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}

.parent {
  position: relative;
  width: 40%;
  min-width: 15rem;
  height: 40vh;
  margin-top: 5rem;
  border: 1px solid red;
}

.child {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 30%;
  height: 30%;
  border: 1px solid blueviolet;
  transform: translate(-50%, -50%);
}

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

---

# 52. 카드 Hover 패턴

```css
.card {
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;
}

.card:hover,
.card:focus-within {
  transform:
    translateY(-4px)
    scale(1.02);
  box-shadow:
    0 12px 30px
    rgb(0 0 0 / 16%);
}
```

작은 이동과 확대를 조합할 수 있습니다.

---

# 53. 아이콘 회전 패턴

```css
.accordion__icon {
  transition: transform 0.2s ease;
}

.accordion-button[aria-expanded="true"]
.accordion__icon {
  transform: rotate(180deg);
}
```

상태는 `aria-expanded`로 전달하고 transform은 시각적 보조 역할을 합니다.

---

# 54. 메뉴 열기 아이콘

```css
.menu-button__line {
  transform-origin: center;
  transition: transform 0.2s ease;
}
```

열린 상태에서 선을 회전해 X 모양을 만들 수 있습니다.

시각 효과만으로 열림 상태를 전달하지 않고 `aria-expanded`를 함께 사용합니다.

---

# 55. 중앙 모달 패턴

Grid 방식:

```css
.modal {
  display: grid;
  position: fixed;
  inset: 0;
  place-items: center;
}
```

Transform 방식:

```css
.modal__panel {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

둘 다 가능하며 전체 오버레이 구조에는 Grid가 더 단순할 수 있습니다.

---

# 56. Transform이 작동하지 않을 때 점검

1. 선택자가 실제 요소와 일치하는가?
2. hover나 focus 상태가 발생하는가?
3. 뒤의 transform 선언이 덮어쓰는가?
4. 여러 transform을 별도 선언으로 작성했는가?
5. transition만 있고 hover transform 값이 없는가?
6. 부모 overflow에 잘려 보이지 않는가?
7. translate 이동량이 너무 작지 않은가?
8. scale 기준점이 예상과 다른가?
9. reduced motion 규칙이 transform을 제거했는가?
10. 개발자 도구에서 계산된 transform matrix를 확인했는가?

---

# 57. 중앙 정렬이 어긋날 때 점검

1. 부모에 `position: relative`가 있는가?
2. 자식에 `position: absolute`가 있는가?
3. `top: 50%`, `left: 50%`가 모두 있는가?
4. `translate(-50%, -50%)`의 부호가 음수인가?
5. 더 가까운 positioned 조상이 있는가?
6. 자식에 다른 transform이 덮어쓰는가?
7. transform을 별도 선언해 중앙 이동이 사라졌는가?
8. 부모의 padding과 border를 확인했는가?
9. 자식 크기가 0이 아닌가?
10. Grid 중앙 정렬이 더 적절한 구조인가?

---

# 58. 자주 하는 실수

## 58.1 Translate 퍼센트를 부모 기준으로 이해

transform의 퍼센트 translate는 요소 자신을 기준으로 합니다.

## 58.2 여러 transform을 별도 선언

뒤 선언이 앞 선언을 덮어씁니다.

## 58.3 함수 순서 무시

translate와 rotate 순서를 바꾸면 결과가 달라질 수 있습니다.

## 58.4 Scale이 레이아웃을 밀 것으로 기대

원래 공간은 유지되어 주변 요소와 겹칠 수 있습니다.

## 58.5 Width 확대와 scale을 동일하게 이해

width는 레이아웃 크기를 바꾸고 scale은 시각적 크기를 바꿉니다.

## 58.6 `rotate(-30deg)` 방향 혼동

음수는 일반적으로 반시계 방향입니다.

## 58.7 중앙 정렬에서 translate 부호 오류

`50%`가 아니라 `-50%`로 자신의 절반을 되돌려야 합니다.

## 58.8 Transform 때문에 stacking context 생성

z-index 관계가 달라질 수 있습니다.

## 58.9 Hover만 제공

키보드와 터치 사용자를 고려해야 합니다.

## 58.10 파일명 철자 오류

내 원본의 `13_tranform.html`처럼 링크와 경로 문제를 만들 수 있습니다.

---


# 종합실습

## 문제 1. Pixel 이동

요소를 오른쪽 `10px`, 아래 `20px` 이동하세요.

## 문제 2. 퍼센트 이동

요소 자신의 너비와 높이 절반만큼 오른쪽 아래로 이동하세요.

## 문제 3. Translate 기준

`translateX(50%)`의 퍼센트 기준을 설명하세요.

## 문제 4. 가로 확대

요소의 가로 크기만 1.5배 확대하세요.

## 문제 5. 전체 확대

요소의 가로와 세로를 모두 1.5배 확대하세요.

## 문제 6. 축소

요소를 원래 크기의 70%로 축소하세요.

## 문제 7. 반시계 회전

요소를 반시계 방향으로 30도 회전하세요.

## 문제 8. 복합 Transform

오른쪽·아래로 자신의 50%만큼 이동하고, 전체 1.5배 확대하고, 반시계 30도 회전하세요.

## 문제 9. 덮어쓰기

다음 코드의 최종 결과를 설명하세요.

```css
.box {
  transform: translateX(20px);
  transform: rotate(30deg);
}
```

## 문제 10. 함수 순서

다음 두 transform이 같은 결과인지 설명하세요.

```css
transform:
  translateX(100px)
  rotate(30deg);
```

```css
transform:
  rotate(30deg)
  translateX(100px);
```

## 문제 11. Transform Origin

요소의 왼쪽 중앙을 기준으로 회전하도록 작성하세요.

## 문제 12. 중앙 정렬 부모

절대 위치 자식의 기준이 되는 `.parent`를 작성하세요.

## 문제 13. 중앙 정렬 자식

자식의 크기를 몰라도 부모 정중앙에 배치하는 코드를 작성하세요.

## 문제 14. 기준 비교

중앙 정렬에서 `top: 50%`와 `translateY(-50%)`의 기준 차이를 설명하세요.

## 문제 15. 내 코드와 강사님 차이

`.total`의 `scaleX(1.5)`와 `scale(1.5)` 결과 차이를 설명하세요.

## 문제 16. 파일명 오류

내 코드의 원본 파일명 오류를 찾아 올바른 이름을 작성하세요.

## 문제 17. Transition 개선

원본의 `transition: all 0.5s`를 필요한 속성만 지정하도록 수정하세요.

## 문제 18. Focus 상태

hover와 keyboard focus에서 같은 scale 효과를 적용하세요.

## 문제 19. Reduced Motion

움직임 감소 환경에서 transition과 transform을 제거하세요.

## 문제 20. Grid 중앙 정렬

절대 위치가 필요 없는 자식을 Grid로 중앙 정렬하세요.

## 문제 21. Stacking Context

transform이 `z-index` 문제에 영향을 줄 수 있는 이유를 설명하세요.

## 문제 22. 종합 카드

다음 요구사항을 만족하는 카드 링크를 작성하세요.

- 실제 `<a>` 요소
- 기본 위치 유지
- hover·focus 시 위로 4px 이동
- 1.02배 확대
- 그림자 강화
- transform과 box-shadow만 transition
- focus outline
- reduced motion 대응
- 카드 목록에 Grid와 gap
- 부모 overflow로 확대가 잘리지 않도록 구성

---

# 정답과 해설

## 정답 1

```css
.box {
  transform: translate(10px, 20px);
}
```

## 정답 2

```css
.box {
  transform: translate(50%, 50%);
}
```

## 정답 3

변형되는 요소 자신의 참조 박스 너비를 기준으로 계산합니다.

## 정답 4

```css
.box {
  transform: scaleX(1.5);
}
```

## 정답 5

```css
.box {
  transform: scale(1.5);
}
```

## 정답 6

```css
.box {
  transform: scale(0.7);
}
```

## 정답 7

```css
.box {
  transform: rotate(-30deg);
}
```

## 정답 8

```css
.box {
  transform:
    translate(50%, 50%)
    scale(1.5)
    rotate(-30deg);
}
```

## 정답 9

최종 적용값은 다음 하나입니다.

```css
transform: rotate(30deg);
```

뒤 선언이 앞의 translate 선언 전체를 덮어씁니다.

## 정답 10

같은 결과가 아닐 수 있습니다. Transform 함수는 순서대로 결합되며 회전된 좌표계에서 이동하는 결과와 이동 후 회전하는 결과가 달라질 수 있습니다.

## 정답 11

```css
.box {
  transform-origin: left center;
}
```

## 정답 12

```css
.parent {
  position: relative;
}
```

실제 크기도 필요합니다.

```css
.parent {
  position: relative;
  width: 40%;
  height: 40vh;
}
```

## 정답 13

```css
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

## 정답 14

`top: 50%`는 부모 containing block의 높이를 기준으로 자식의 위쪽 위치를 정합니다. `translateY(-50%)`는 자식 자신의 높이 절반만큼 위로 이동합니다.

## 정답 15

```text
scaleX(1.5)
→ 가로만 1.5배

scale(1.5)
→ 가로와 세로 모두 1.5배
```

따라서 내 코드와 강사님 코드의 total 결과는 다릅니다.

## 정답 16

```text
원본: 13_tranform.html
개선: 13_transform.html
```

## 정답 17

```css
.box {
  transition: transform 0.5s;
}
```

## 정답 18

```css
.box:hover,
.box:focus-visible {
  transform: scale(1.1);
}
```

## 정답 19

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

## 정답 20

```css
.parent {
  display: grid;
  place-items: center;
}
```

## 정답 21

`none`이 아닌 transform은 새로운 stacking context를 만들 수 있습니다. 자식의 `z-index`는 해당 stacking context 안에서 제한되므로 다른 부모 그룹과의 레이어 순서가 예상과 달라질 수 있습니다.

## 정답 22

### HTML

```html
<div class="card-list">
  <a class="learning-card" href="/css/transform">
    <h2>CSS Transform</h2>
    <p>
      이동, 확대, 회전을 학습합니다.
    </p>
    <span class="learning-card__action">
      학습하기 →
    </span>
  </a>

  <a class="learning-card" href="/css/media">
    <h2>CSS Media Query</h2>
    <p>
      반응형 웹을 학습합니다.
    </p>
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
  padding: 1rem;
}

.learning-card {
  display: block;
  padding: 1.5rem;
  border: 1px solid #d1d5db;
  border-radius: 1rem;
  color: inherit;
  background-color: white;
  text-decoration: none;
  box-shadow:
    0 2px 8px
    rgb(0 0 0 / 10%);
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;
}

.learning-card:hover,
.learning-card:focus-visible {
  transform:
    translateY(-4px)
    scale(1.02);
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

# 최종 체크리스트

## Transform 기본

- [ ] `translate`, `scale`, `rotate`의 역할을 구분했다.
- [ ] translate 퍼센트 기준이 요소 자신임을 이해했다.
- [ ] scale 값 `1`, `1.5`, `0.5`의 의미를 이해했다.
- [ ] 음수 rotate 방향을 확인했다.
- [ ] transform이 원래 레이아웃 공간을 유지함을 확인했다.

## 복합 Transform

- [ ] 여러 함수를 한 transform 선언에 작성했다.
- [ ] 별도 transform 선언으로 앞 값을 덮어쓰지 않았다.
- [ ] 함수 순서가 결과에 영향을 주는지 확인했다.
- [ ] 내 코드의 `scaleX`와 강사님의 `scale` 차이를 확인했다.
- [ ] transform-origin이 적절한지 검토했다.

## 중앙 정렬

- [ ] 부모에 `position: relative`가 있다.
- [ ] 자식에 `position: absolute`가 있다.
- [ ] `top: 50%`, `left: 50%`가 있다.
- [ ] `translate(-50%, -50%)`의 부호가 정확하다.
- [ ] 부모 기준과 자식 기준 퍼센트를 구분했다.
- [ ] Grid/Flex가 더 간단한 구조인지 검토했다.

## 상호작용과 접근성

- [ ] transition은 `transform`만 명시했다.
- [ ] hover와 focus-visible을 함께 제공했다.
- [ ] focus outline이 보인다.
- [ ] 실제 동작에는 button 또는 a를 사용했다.
- [ ] reduced motion 환경을 고려했다.
- [ ] 이동·회전 효과 없이도 기능을 이해할 수 있다.

## 레이아웃과 성능

- [ ] scale 요소가 주변 콘텐츠와 겹치지 않는다.
- [ ] 부모 overflow에 확대 영역이 잘리지 않는다.
- [ ] transform이 stacking context를 만드는 영향을 확인했다.
- [ ] fixed 자식 기준이 달라지지 않는지 확인했다.
- [ ] 소수점 변형으로 글자가 흐려지지 않는지 확인했다.
- [ ] 많은 요소에 과도한 transform 효과를 사용하지 않았다.

## 원본 코드 검수

- [ ] 내 파일명 `13_tranform.html` 오타를 기록했다.
- [ ] 강사님 파일명 `13_transform.html`과 비교했다.
- [ ] 내 total의 `scaleX(1.5)`를 보존했다.
- [ ] 강사님 total의 `scale(1.5)`를 보존했다.
- [ ] child 테두리 `blue`와 `blueviolet` 차이를 보존했다.
- [ ] 강사님 transition 세미콜론 누락을 기록했다.
- [ ] 내 코드의 반복 `<br>`를 개선했다.
- [ ] `lang="en"`과 `Document`를 개선했다.

---

# 핵심 요약

- `transform`은 요소를 이동, 확대·축소, 회전, 기울이는 시각적 변형 속성이다.
- transform은 일반적으로 원래 레이아웃 공간을 유지한다.
- `translate(x, y)`는 요소를 x축과 y축으로 이동한다.
- transform translate의 퍼센트는 요소 자신의 크기를 기준으로 한다.
- `left: 50%`는 부모 기준이고 `translateX(-50%)`는 자식 자신 기준이다.
- 원본 `translate(50%, 50%)`는 100px 박스를 대략 오른쪽·아래 50px 이동한다.
- `scale(1.5)`는 가로와 세로를 모두 1.5배 확대한다.
- `scaleX(1.5)`는 가로만 1.5배 확대한다.
- 내 코드의 total은 `scaleX(1.5)`, 강사님 코드는 `scale(1.5)`이므로 결과가 다르다.
- `rotate(-30deg)`는 일반적으로 반시계 방향 회전이다.
- transform-origin은 회전과 확대의 기준점을 결정한다.
- 여러 transform 함수는 한 선언 안에 공백으로 조합한다.
- 여러 transform 선언을 따로 쓰면 뒤 선언이 앞 선언을 덮어쓴다.
- transform 함수의 순서는 최종 위치와 방향에 영향을 준다.
- 원본 중앙 정렬은 `top: 50%`, `left: 50%`, `translate(-50%, -50%)`를 사용한다.
- `top`과 `left`는 부모 크기를, translate 음수 퍼센트는 자식 크기를 기준으로 한다.
- 일반적인 중앙 정렬에는 Grid나 Flexbox가 더 간단할 수 있다.
- `none`이 아닌 transform은 stacking context를 만들 수 있다.
- 부모 transform은 fixed 자식의 기준과 레이어 동작에 영향을 줄 수 있다.
- hover transform은 키보드 사용자를 위해 focus-visible과 함께 제공한다.
- 움직임에 민감한 사용자를 위해 prefers-reduced-motion을 고려한다.
- 내 원본 파일명 `13_tranform.html`에는 `s`가 빠진 철자 오류가 있다.
- 강사님 코드의 `transition: all .5s`는 마지막 세미콜론이 없지만 현재는 처리될 수 있다.
- 내 코드의 반복 `<br>`는 CSS 여백으로 대체하는 것이 좋다.
# V3 렌더링 추적 카드 — 레이아웃 뒤 시각 좌표 변환

transform은 layout에서 잡힌 자리 자체를 다시 배치하기보다 그려지는 결과를 이동·회전·확대·기울인다. 여러 함수의 작성 순서에 따라 결과가 달라진다.

translate로 이동해도 주변 요소는 원래 자리를 기준으로 배치될 수 있다. DevTools transform matrix와 transform-origin을 확인한다. 내 원본 파일명 `13_tranform.html`의 오탈자는 실제 경로 그대로 구분한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/css/13_tranform.html (강사님 원본은 13_transform.html)`에서 실제 선택자·계산값·화면 차이를 확인한다.
