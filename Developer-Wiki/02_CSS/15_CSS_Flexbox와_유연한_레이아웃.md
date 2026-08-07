---
title: CSS Flexbox와 유연한 레이아웃
version: v2.0-final
last_updated: 2026-08-07
status: Completed
---

# CSS Flexbox와 유연한 레이아웃

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `15_CSS_Flexbox와_유연한_레이아웃.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_html/css/15_flex.html`, `workspace_teacher/workspace_html/css/15_flex.html` |
| 핵심 범위 | `display: flex`, main axis, cross axis, `flex-direction`, `flex-wrap`, `justify-content`, `align-items`, `align-content`, `order`, `flex-grow`, `flex-shrink`, `min-width` |
| 프로젝트 연결 | 헤더, 메뉴, 버튼 그룹, 카드 목록, 중앙 정렬, 반응형 행·열 전환, 남은 공간 분배 |

> 내 코드와 강사님 코드의 `15_flex.html`은 내용이 동일하다. 이 문서는 동일한 코드를 반복 비교하지 않고 Flex Container와 Item, 주축·교차축, 방향·줄바꿈·정렬·크기 분배의 동작을 분석한다. `gap`, `flex-basis`, 단축 속성, 시각 순서 접근성, 반응형 Header·Card 패턴까지 실무 기준으로 연결한다.

---

# 학습 목표

- Flexbox가 한 축을 중심으로 자식 요소를 배치하는 레이아웃 방식임을 설명한다.
- flex container와 flex item을 구분한다.
- main axis와 cross axis가 `flex-direction`에 따라 달라진다는 점을 이해한다.
- `row`, `row-reverse`, `column`, `column-reverse`의 차이를 설명한다.
- `nowrap`, `wrap`, `wrap-reverse`의 차이를 이해한다.
- `justify-content`가 main axis 정렬을 담당한다는 점을 설명한다.
- `align-items`가 한 줄 내부의 cross axis 정렬을 담당한다는 점을 설명한다.
- `align-content`가 여러 줄 전체의 cross axis 배치를 담당한다는 점을 설명한다.
- `order`가 시각적 순서를 바꾸지만 DOM 순서를 바꾸지 않는다는 점을 이해한다.
- `flex-grow`가 남은 양의 공간을 분배하는 비율임을 설명한다.
- `flex-shrink`가 부족한 공간에서 축소되는 비율에 관여한다는 점을 이해한다.
- `min-width`가 flex item 축소 한계를 만들 수 있음을 설명한다.
- 원본의 인라인 스타일 실험값을 보존하면서 클래스 기반 개선안을 작성한다.
- 내 코드와 강사님 코드가 완전히 동일함을 정확히 기록한다.
- Flexbox와 Grid의 사용 목적을 구분한다.

---

# 1. Flexbox란?

Flexbox는 부모 요소를 flex container로 만들고, 그 직계 자식 요소를 flex item으로 배치하는 CSS 레이아웃 방식입니다.

원본:

```css
.container {
  display: flex;
}
```

HTML:

```html
<div class="container">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
  <div class="item">4</div>
  <div class="item">5</div>
</div>
```

구분:

```text
.container
→ flex container

.container의 직계 자식 .item
→ flex item
```

손자 요소는 자동으로 `.container`의 flex item이 되지 않습니다.

---

# 2. 원본 전체 구조

원본은 하나의 고정 크기 컨테이너와 다섯 개의 item으로 구성됩니다.

```css
.container {
  border: 1px solid green;
  height: 300px;
  width: 300px;
  display: flex;
  flex-direction: row;
}
```

```css
.container .item {
  border: 1px solid red;
  background-color: brown;
  color: #fff;
}
```

각 item에는 일부 flex item 속성이 인라인 스타일로 지정되어 있습니다.

```html
<div class="item">1</div>
<div class="item" style="order: 1">2</div>
<div class="item" style="order: -1">3</div>
<div
  class="item"
  style="
    flex-grow: 0;
    flex-shrink: 3;
    min-width: 50px;
  "
>
  4
</div>
<div
  class="item"
  style="
    flex-grow: 0;
    flex-shrink: 2;
  "
>
  5
</div>
```

---

# 3. `display: flex`

```css
.container {
  display: flex;
}
```

이 선언은 `.container`의 직계 자식을 flex item으로 만듭니다.

기본적으로:

```text
flex-direction: row
flex-wrap: nowrap
justify-content: flex-start
align-items: stretch
align-content: stretch
```

단, 실제 보이는 결과는 item의 크기, 줄 수, container 크기에 따라 달라집니다.

---

# 4. `display: inline-flex`

원본 주석:

```css
/* display: inline-flex; */
```

`inline-flex`도 내부 자식을 flex item으로 배치합니다.

차이는 container 자신의 외부 배치 방식입니다.

| 값 | container의 외부 성격 | 내부 자식 |
| --- | --- | --- |
| `flex` | 블록 수준 flex container | flex item |
| `inline-flex` | 인라인 수준 flex container | flex item |

즉, 내부 Flexbox 동작은 유사하지만 부모 자신이 주변 요소와 배치되는 방식이 다릅니다.

---

# 5. Main axis와 Cross axis

Flexbox에는 두 축이 있습니다.

```text
main axis
→ flex item이 기본적으로 나열되는 방향

cross axis
→ main axis와 수직인 방향
```

원본 기본값:

```css
flex-direction: row;
```

따라서 일반적인 가로쓰기 환경에서:

```text
main axis  → 왼쪽에서 오른쪽
cross axis → 위에서 아래
```

---

# 6. 축은 항상 가로·세로로 고정되지 않는다

중요:

```text
main axis = 항상 가로
cross axis = 항상 세로
```

라고 외우면 안 됩니다.

`flex-direction: column`이면:

```text
main axis  → 세로
cross axis → 가로
```

즉, 정렬 속성을 이해할 때 먼저 `flex-direction`을 확인해야 합니다.

---

# 7. 원본 `flex-direction: row`

```css
/* main 축의 기본값 : 왼쪽에서 오른쪽으로 */
flex-direction: row;
```

일반적인 `direction: ltr` 환경에서는 item이 왼쪽에서 오른쪽으로 배치됩니다.

원본 HTML 순서:

```text
1, 2, 3, 4, 5
```

다만 원본에는 `order`가 있으므로 실제 시각 순서는 달라집니다.

---

# 8. `row-reverse`

원본 주석:

```css
/* 오른쪽에서 왼쪽으로 */
/* flex-direction: row-reverse; */
```

`row-reverse`는 main axis의 시작과 끝 방향을 뒤집습니다.

```css
.container {
  flex-direction: row-reverse;
}
```

주의:

- DOM 순서는 바뀌지 않는다.
- 시각적 배치 방향만 바뀐다.
- 키보드 탐색과 화면 읽기 순서는 DOM 순서를 따를 수 있다.

---

# 9. `column`

원본 주석:

```css
/* 위에서 아래로 */
/* flex-direction: column; */
```

```css
.container {
  flex-direction: column;
}
```

일반적인 환경에서 main axis가 위에서 아래로 바뀝니다.

이때:

```text
justify-content
→ 세로 방향 정렬

align-items
→ 가로 방향 정렬
```

---

# 10. `column-reverse`

원본 주석:

```css
/* 아래에서 위로 */
/* flex-direction: column-reverse; */
```

main axis 방향을 세로 역방향으로 배치합니다.

시각적 순서를 뒤집는 용도로 사용할 수 있지만 콘텐츠의 의미 순서까지 뒤집어야 한다면 HTML 구조를 먼저 검토합니다.

---

# 11. `flex-wrap`

원본에는 세 값이 모두 주석으로 기록되어 있습니다.

```css
/* flex-wrap: nowrap; */
/* flex-wrap: wrap; */
/* flex-wrap: wrap-reverse; */
```

`flex-wrap`은 item이 한 줄에 모두 들어가지 않을 때 줄바꿈할지 결정합니다.

---

# 12. `nowrap`

원본 주석:

```css
/* 기본값, 한줄에 모든 item을 표시하려고 노력 */
/* flex-wrap: nowrap; */
```

정확한 핵심입니다.

```css
flex-wrap: nowrap;
```

기본값이며 한 줄에 유지하려고 합니다.

공간이 부족하면:

- item이 축소될 수 있다.
- 콘텐츠 때문에 충분히 축소되지 않을 수 있다.
- overflow가 생길 수 있다.

---

# 13. `wrap`

원본 주석:

```css
/* 넘치는 경우 다음줄로 (inline-block 처럼) */
/* cross축 start에서 end */
/* flex-wrap: wrap; */
```

```css
flex-wrap: wrap;
```

main axis 공간이 부족하면 다음 줄로 넘깁니다.

`row` 기준에서 일반적으로:

```text
첫 번째 줄
두 번째 줄
세 번째 줄
```

이 cross axis의 시작에서 끝 방향으로 쌓입니다.

---

# 14. “inline-block처럼” 주석 보완

원본:

```text
넘치는 경우 다음줄로 (inline-block 처럼)
```

보이는 결과가 줄바꿈된다는 점에서는 초보자에게 도움이 됩니다.

그러나 Flexbox의 줄 구성은 inline formatting context와 동일하지 않습니다.

정확한 보완:

```text
공간이 부족하면 flex line이 추가된다.
겉보기에는 inline-block 항목의 줄바꿈과 비슷할 수 있지만,
정렬과 공간 분배는 Flexbox 규칙을 따른다.
```

---

# 15. `wrap-reverse`

원본 주석:

```css
/* cross축의 end에서 start로 */
/* flex-wrap: wrap-reverse; */
```

```css
flex-wrap: wrap-reverse;
```

줄이 쌓이는 cross axis 방향을 반대로 만듭니다.

item 자체의 DOM 순서를 반대로 만드는 속성은 아닙니다.

---

# 16. `flex-flow`

원본에는 없지만 `flex-direction`과 `flex-wrap`을 함께 작성할 수 있습니다.

```css
.container {
  flex-flow: row wrap;
}
```

이는 다음과 같습니다.

```css
.container {
  flex-direction: row;
  flex-wrap: wrap;
}
```

확장 학습으로 구분합니다.

---

# 17. `justify-content`

원본에는 다음 값이 모두 주석으로 있습니다.

```css
/* justify-content: flex-start; */
/* justify-content: flex-end; */
/* justify-content: center; */
/* justify-content: space-between; */
/* justify-content: space-around; */
/* justify-content: space-evenly; */
```

`justify-content`는 **main axis 방향의 남은 공간**을 배치합니다.

---

# 18. `justify-content: flex-start`

원본 주석:

```css
/* 기본값, main축의 start 방향 정렬 */
```

```css
justify-content: flex-start;
```

item을 main-start 쪽에 모읍니다.

`row` + 일반적인 LTR 환경에서는 왼쪽입니다.

하지만 writing mode, direction, flex-direction에 따라 실제 방향은 달라질 수 있습니다.

---

# 19. `justify-content: flex-end`

```css
justify-content: flex-end;
```

main-end 방향으로 모읍니다.

`row` 기준으로 일반적인 LTR 환경에서는 오른쪽에 가깝습니다.

---

# 20. `justify-content: center`

```css
justify-content: center;
```

main axis 중앙에 item 묶음을 배치합니다.

중요:

- 각 item 사이 간격을 자동으로 같게 만드는 것은 아니다.
- item 전체 묶음을 가운데로 옮긴다.
- item 사이 간격은 `gap`으로 별도 지정할 수 있다.

---

# 21. `space-between`

원본 주석:

```text
남은 공간을 사이사이에 균등하게 배치
```

```css
justify-content: space-between;
```

특징:

- 첫 item은 main-start에 위치
- 마지막 item은 main-end에 위치
- item 사이의 남은 공간을 균등하게 분배
- 양 끝 바깥 여백은 생성하지 않음

---

# 22. `space-around`

원본 주석:

```text
item의 양쪽에 동일한 공간 배치
```

```css
justify-content: space-around;
```

각 item 양쪽에 같은 크기의 공간 몫을 줍니다.

그래서 컨테이너 양 끝의 실제 여백은 item 사이 간격의 절반처럼 보입니다.

---

# 23. `space-evenly`

원본 주석:

```text
모든 공간을 균등하게 배치
```

```css
justify-content: space-evenly;
```

다음 간격을 동일하게 배치합니다.

```text
컨테이너 시작 ↔ 첫 item
item ↔ item
마지막 item ↔ 컨테이너 끝
```

---

# 24. `gap`

원본에는 없지만 Flexbox에서 item 사이 간격을 만들 때 사용할 수 있습니다.

```css
.container {
  display: flex;
  gap: 1rem;
}
```

장점:

- 양 끝에 불필요한 margin이 생기지 않는다.
- 마지막 item의 margin 제거 규칙이 필요 없다.
- row와 column 간격을 구분할 수 있다.

```css
.container {
  row-gap: 1rem;
  column-gap: 2rem;
}
```

---

# 25. `align-items`

원본 주석:

```text
한 줄에 대한 cross축의 이야기
```

이 설명은 핵심을 잘 짚습니다.

```css
align-items: stretch;
align-items: flex-start;
align-items: flex-end;
align-items: center;
```

`align-items`는 각 flex line 안에서 item을 cross axis 방향으로 정렬합니다.

---

# 26. `align-items: stretch`

원본 주석:

```css
/* 기본값, cross축으로 쭉~ 늘리기 */
/* align-items: stretch; */
```

기본값입니다.

단, item의 cross size가 `auto`인 경우에 주로 늘어납니다.

예를 들어 `row` 방향에서 item에 고정 height가 없으면 line의 높이를 채우도록 늘어날 수 있습니다.

---

# 27. `align-items: flex-start`

```css
align-items: flex-start;
```

각 item을 cross-start 방향으로 정렬합니다.

`row` 기준에서 일반적으로 위쪽입니다.

`column`이면 cross axis가 가로가 되므로 일반적인 LTR 환경에서는 왼쪽에 가깝습니다.

---

# 28. `align-items: flex-end`

```css
align-items: flex-end;
```

cross-end 방향으로 정렬합니다.

`row` 기준에서 일반적으로 아래쪽입니다.

---

# 29. `align-items: center`

```css
align-items: center;
```

cross axis 중앙에 정렬합니다.

Flexbox 중앙 정렬:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

`row` 기준에서는 가로·세로 중앙처럼 보입니다.

---

# 30. `align-items: baseline`

원본에는 없지만 텍스트 기준선 정렬에 사용할 수 있습니다.

```css
.container {
  align-items: baseline;
}
```

서로 다른 글자 크기의 버튼이나 텍스트를 기준선에 맞출 때 유용합니다.

---

# 31. `align-content`

원본 주석:

```text
여러 줄에 대한 cross축의 이야기
```

정확한 핵심입니다.

```css
align-content: stretch;
align-content: flex-start;
align-content: flex-end;
align-content: center;
align-content: space-between;
align-content: space-around;
align-content: space-evenly;
```

여러 flex line 전체를 cross axis 방향으로 배치합니다.

---

# 32. `align-content`가 작동하려면

보통 다음 조건이 필요합니다.

```text
1. flex-wrap으로 여러 줄이 만들어짐
2. container의 cross size에 남는 공간이 있음
```

한 줄만 있으면 `align-content`의 효과를 확인하기 어렵습니다.

원본도 주석에서 먼저 다음을 제시합니다.

```css
/* flex-wrap: wrap; */
```

---

# 33. `align-items`와 `align-content` 비교

| 속성 | 대상 | 주로 필요한 조건 |
| --- | --- | --- |
| `align-items` | 각 줄 안의 item | 한 줄이어도 적용 |
| `align-content` | 여러 줄의 line 묶음 | wrap과 여러 줄 필요 |

쉽게 구분:

```text
align-items
→ item 정렬

align-content
→ line 정렬
```

---

# 34. 원본 Container 크기

```css
height: 300px;
width: 300px;
```

고정된 정사각형 컨테이너입니다.

장점:

- justify와 align 결과를 눈으로 확인하기 쉽다.
- 여러 줄을 만들 때 영역이 명확하다.

한계:

- 반응형 레이아웃에는 고정 너비가 불리할 수 있다.
- 작은 화면에서 overflow 여부를 확인해야 한다.

확장 개선:

```css
.container {
  width: min(100%, 300px);
  min-height: 300px;
}
```

---

# 35. 원본 Item 크기

원본 `.item`에는 실제 width와 height가 없습니다.

```css
.container .item {
  border: 1px solid red;
  background-color: brown;
  color: #fff;

  /* width: 100px; */
  /* width: 100px; */
}
```

두 줄 모두 같은 주석입니다.

```css
/* width: 100px; */
/* width: 100px; */
```

이는 중복 주석입니다.

두 번째 값이 원래 height 실험이었는지는 원본만으로 확정할 수 없습니다.

따라서 조용히 `height`로 고치지 않고 다음처럼 기록합니다.

```text
width 주석이 두 번 반복되어 있다.
의도는 원본만으로 확정할 수 없다.
```

---

# 36. Item 기본 크기

width가 지정되지 않은 flex item은 콘텐츠와 flex sizing 규칙을 바탕으로 크기가 결정됩니다.

원본 item 콘텐츠:

```text
1
2
3
4
5
```

짧은 한 글자이므로 기본 상태에서 각 item은 비교적 작은 너비로 보입니다.

container에 남는 공간이 많아도 `flex-grow` 기본값이 0이므로 자동으로 남은 공간을 채우지 않습니다.

---

# 37. Flex item 기본값

개념적으로 자주 설명하는 기본값:

```css
flex-grow: 0;
flex-shrink: 1;
flex-basis: auto;
```

단축 속성으로 자주 표현하면:

```css
flex: 0 1 auto;
```

원본 item 1, 2, 3은 별도 grow·shrink를 지정하지 않았으므로 기본값의 영향을 받습니다.

---

# 38. `order`

원본:

```html
<div class="item" style="order: 1">2</div>
<div class="item" style="order: -1">3</div>
```

`order`는 flex item의 시각적 배치 순서를 조정합니다.

기본값:

```css
order: 0;
```

원본 값:

| Item | order |
| --- | --- |
| 1 | 0 |
| 2 | 1 |
| 3 | -1 |
| 4 | 0 |
| 5 | 0 |

---

# 39. 원본의 시각 순서

같은 order 값에서는 DOM 순서가 유지됩니다.

따라서 일반적인 `row` 방향의 시각 순서:

```text
3 → 1 → 4 → 5 → 2
```

이유:

```text
order -1
→ 3이 먼저

order 0
→ 1, 4, 5가 DOM 순서대로

order 1
→ 2가 마지막
```

---

# 40. Order는 DOM을 바꾸지 않는다

HTML 순서:

```text
1 → 2 → 3 → 4 → 5
```

시각 순서:

```text
3 → 1 → 4 → 5 → 2
```

화면 읽기 프로그램과 키보드 탐색 순서는 여전히 DOM 순서를 따를 수 있습니다.

따라서 중요한 의미 순서를 `order`만으로 바꾸면 안 됩니다.

---

# 41. Order 사용이 적절한 경우

적절할 수 있는 예:

- 장식 요소 위치 조정
- 반응형에서 보조 버튼의 시각 위치 변경
- 동일한 의미 그룹 안의 제한적인 재배치

주의해야 하는 예:

- 문장 순서
- 단계별 절차
- 폼 입력 순서
- 주요 내비게이션 의미 순서
- 카드 읽기 순서

가능하면 HTML을 올바른 의미 순서로 작성합니다.

---

# 42. `flex-grow`

원본 item 4와 5:

```html
style="flex-grow: 0; ..."
```

`flex-grow`는 main axis에 **남는 양의 공간**이 있을 때 item이 얼마나 늘어날지 결정하는 비율입니다.

기본값:

```css
flex-grow: 0;
```

원본에서 두 item 모두 0이므로 남은 공간을 늘어나서 차지하지 않습니다.

---

# 43. Grow 비율 예제

```css
.item--a {
  flex-grow: 1;
}

.item--b {
  flex-grow: 2;
}
```

남는 공간을 비율상:

```text
A : B = 1 : 2
```

로 분배합니다.

주의:

최종 전체 너비가 정확히 1:2가 된다는 뜻은 아닙니다.

기본 크기에 남은 공간이 추가되는 방식이기 때문입니다.

---

# 44. `flex-shrink`

원본:

```html
<div
  class="item"
  style="
    flex-grow: 0;
    flex-shrink: 3;
    min-width: 50px;
  "
>
  4
</div>
```

```html
<div
  class="item"
  style="
    flex-grow: 0;
    flex-shrink: 2;
  "
>
  5
</div>
```

`flex-shrink`는 item들의 기본 크기 합이 container보다 클 때 축소에 참여하는 정도를 나타냅니다.

기본값:

```css
flex-shrink: 1;
```

---

# 45. Shrink 값이 크면

단순한 학습 표현:

```text
flex-shrink 값이 더 크면
부족한 공간에서 더 많이 줄어드는 경향
```

하지만 실제 축소량은 shrink 값만으로 정해지지 않습니다.

다음도 영향을 줍니다.

- flex base size
- item의 콘텐츠
- min-width
- 다른 item의 shrink 값
- 전체 부족 공간

따라서 `3`이 `2`보다 무조건 최종 너비가 정확히 1.5배 더 줄어든다고 단정하면 안 됩니다.

---

# 46. `min-width: 50px`

원본 item 4:

```css
min-width: 50px;
```

item 4는 축소되더라도 최소 너비 50px 아래로 내려가지 않도록 제한합니다.

즉:

```text
flex-shrink: 3
→ 많이 줄어들려는 비율

min-width: 50px
→ 50px 아래 축소 제한
```

두 규칙이 함께 작동합니다.

---

# 47. `min-width: auto`와 긴 콘텐츠

Flex item의 기본 최소 크기 때문에 긴 텍스트가 충분히 줄어들지 않는 경우가 있습니다.

실무에서 말줄임표나 축소를 허용하려면 다음이 필요할 수 있습니다.

```css
.flex-item {
  min-width: 0;
}
```

예:

```css
.title {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

원본에는 긴 콘텐츠가 없으므로 확장 학습입니다.

---

# 48. `flex-basis`

원본에는 직접 등장하지 않지만 grow와 shrink를 이해할 때 중요합니다.

```css
.item {
  flex-basis: 100px;
}
```

main axis 방향의 초기 기준 크기를 지정합니다.

`row`에서는 주로 너비와 관련되고, `column`에서는 주로 높이와 관련됩니다.

---

# 49. `flex` 단축 속성

```css
flex:
  flex-grow
  flex-shrink
  flex-basis;
```

예:

```css
.item {
  flex: 1 1 0;
}
```

자주 사용하는 값:

```css
flex: 1;
flex: auto;
flex: none;
```

정확한 계산 의도를 위해 팀 규칙에 맞게 명시합니다.

---

# 50. `flex: 1`

흔히 다음처럼 사용합니다.

```css
.item {
  flex: 1;
}
```

여러 item에 동일하게 적용하면 남는 공간을 균등하게 분배하는 형태로 자주 사용됩니다.

다만 `flex: 1`의 세부 해석은 단순히 `flex-grow: 1` 하나만 지정한 것과 완전히 동일하게 설명하면 안 됩니다.

---

# 51. `align-self`

특정 item 하나만 cross axis에서 다르게 정렬할 수 있습니다.

```css
.item--special {
  align-self: flex-end;
}
```

container의 `align-items` 값을 해당 item에 개별적으로 덮어씁니다.

원본에는 없는 확장 학습입니다.

---

# 52. Inline style 분석

원본은 다음처럼 인라인 스타일을 사용합니다.

```html
<div class="item" style="order: 1">2</div>
```

학습 장점:

- item별 값을 바로 확인하기 쉽다.
- 각 실험 대상이 명확하다.

실무 한계:

- HTML과 스타일이 섞인다.
- 재사용이 어렵다.
- 여러 요소 수정이 번거롭다.
- 명시도가 높아 덮어쓰기 불편하다.

---

# 53. 클래스 기반 개선

```html
<div class="item item--last">2</div>
<div class="item item--first">3</div>
<div class="item item--shrink-3">4</div>
<div class="item item--shrink-2">5</div>
```

```css
.item--last {
  order: 1;
}

.item--first {
  order: -1;
}

.item--shrink-3 {
  min-width: 50px;
  flex: 0 3 auto;
}

.item--shrink-2 {
  flex: 0 2 auto;
}
```

---

# 54. 원본 Emmet 문자열

원본 body:

```text
div.container>div.item*5
```

이는 Emmet 축약 문법이 그대로 화면에 표시되는 텍스트입니다.

의도한 Emmet:

```text
div.container>div.item*5
```

에디터에서 확장하면:

```html
<div class="container">
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
</div>
```

브라우저 화면에 필요 없다면 삭제하거나 HTML 주석으로 남깁니다.

```html
<!-- Emmet: div.container>div.item*5 -->
```

---

# 55. 문서 언어와 제목

원본:

```html
<html lang="en">
<title>Document</title>
```

본문 주석과 학습 맥락이 한국어이므로:

```html
<html lang="ko">
<title>CSS Flexbox</title>
```

로 개선합니다.

---

# 56. 원본의 중복 Width 주석

```css
/* width: 100px; */
/* width: 100px; */
```

두 줄이 완전히 같습니다.

QA 결과:

```text
중복 주석 발견
```

조용히 하나를 height로 변경하지 않습니다.

개선 가능한 방식:

```css
/* width: 100px; */
```

또는 실제로 높이도 실험하려는 의도가 확인된 경우에만:

```css
/* width: 100px; */
/* height: 100px; */
```

로 수정합니다.

---

# 57. `border`와 Box sizing

원본 container:

```css
width: 300px;
height: 300px;
border: 1px solid green;
```

기본 `content-box`이면 실제 바깥 크기는 대략:

```text
302px × 302px
```

item에도 border가 있으므로 크기 계산에 포함됩니다.

전역 개선:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

---

# 58. Flexbox와 Margin

원본 item에는 margin이 없습니다.

item 사이 간격을 만들려면:

```css
.item {
  margin-right: 1rem;
}
```

보다 다음이 간단합니다.

```css
.container {
  gap: 1rem;
}
```

`gap`은 정렬용 남은 공간과 item 사이의 고정 간격을 구분하기 쉽습니다.

---

# 59. Flexbox와 Auto margin

특정 item을 main-end로 밀 수 있습니다.

```css
.logout {
  margin-left: auto;
}
```

가로 메뉴 예:

```html
<nav class="nav">
  <a href="/">홈</a>
  <a href="/docs">문서</a>
  <a class="logout" href="/logout">로그아웃</a>
</nav>
```

`order`보다 의미 순서를 유지하면서 시각적 간격을 만들 수 있습니다.

---

# 60. 완전 중앙 정렬

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

`row` 기준:

```text
justify-content → 가로 중앙
align-items     → 세로 중앙
```

하지만 `column`으로 바꾸면 축의 역할도 바뀝니다.

속성 이름을 가로·세로로 외우지 않고 main·cross 축으로 이해합니다.

---

# 61. 반응형 Row와 Column

```css
.card-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

@media (min-width: 48rem) {
  .card-list {
    flex-direction: row;
  }
}
```

모바일에서 세로, 넓은 화면에서 가로로 전환할 수 있습니다.

CSS 14 미디어 쿼리와 연결됩니다.

---

# 62. 반응형 Wrap 카드

```css
.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  flex: 1 1 15rem;
}
```

의미:

```text
grow 1
→ 남는 공간 확장 가능

shrink 1
→ 공간 부족 시 축소 가능

basis 15rem
→ 초기 기준 너비
```

카드가 공간에 따라 줄바꿈됩니다.

---

# 63. Flexbox와 Grid 비교

| 기준 | Flexbox | Grid |
| --- | --- | --- |
| 핵심 | 한 축 중심 | 행과 열의 2차원 |
| 메뉴·버튼 줄 | 적합 | 가능 |
| 카드 행·열 정렬 | 가능 | Grid가 더 명확할 수 있음 |
| 콘텐츠 크기 중심 | 강점 | 가능 |
| 명확한 열 구조 | 제한적 | 강점 |

선택 기준:

```text
한 방향의 정렬과 분배
→ Flexbox

행과 열을 함께 제어
→ Grid
```

둘은 경쟁 관계가 아니라 함께 사용합니다.

---

# 64. Flex item이 줄어들지 않을 때

점검:

1. `flex-shrink: 0`인가?
2. `min-width`가 큰가?
3. 기본 `min-width: auto`가 콘텐츠 크기를 보존하는가?
4. 긴 단어가 줄바꿈되지 않는가?
5. 이미지에 고정 width가 있는가?
6. `white-space: nowrap`이 적용됐는가?
7. container보다 basis 합이 큰가?
8. box-sizing을 확인했는가?
9. overflow가 item 내부에서 발생하는가?
10. `min-width: 0`이 필요한가?

---

# 65. Flex item이 늘어나지 않을 때

점검:

1. `flex-grow`가 0인가?
2. container에 남는 공간이 있는가?
3. main axis가 예상 방향인가?
4. item의 max-width가 제한하는가?
5. `flex-basis`가 어떻게 계산되는가?
6. 다른 item도 grow를 가지는가?
7. 고정 width와 flex 단축 속성이 충돌하는가?
8. container가 실제로 flex인가?
9. item이 직계 자식인가?
10. 개발자 도구의 flex overlay를 확인했는가?

---

# 66. `justify-content`가 안 보일 때

`justify-content`는 남는 공간이 있어야 차이가 보입니다.

원본 item은 작고 container는 300px이므로 기본 상태에서 남는 공간이 있어 실험하기 좋습니다.

반대로 item 합계가 container를 꽉 채우면 다음 값들의 차이가 거의 없을 수 있습니다.

```text
flex-start
center
space-between
```

먼저 container와 item의 실제 크기를 확인합니다.

---

# 67. `align-content`가 안 보일 때

가장 흔한 원인:

```text
한 줄뿐임
```

다음처럼 여러 줄을 만듭니다.

```css
.container {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
}

.item {
  width: 120px;
}
```

300px container에서 120px item 여러 개라면 여러 줄이 만들어질 수 있습니다.

---

# 68. `align-items: stretch`가 안 보일 때

item에 고정 cross size가 있으면 stretch 효과가 제한됩니다.

예:

```css
.item {
  height: 50px;
}
```

`row` container에서 이미 height가 지정되면 line 높이를 채우도록 자동 stretch되지 않습니다.

원본 item에는 height가 없어 기본 stretch 실험에 적합합니다.

---

# 69. `order`가 안 보일 때

점검:

1. 대상이 flex item인가?
2. 부모가 `display: flex` 또는 `inline-flex`인가?
3. order 값이 실제로 다른가?
4. 같은 order끼리 DOM 순서가 유지되는가?
5. `row-reverse`와 함께 사용해 혼동하는가?
6. CSS가 인라인 스타일을 덮을 수 있는가?
7. Grid item에도 order가 적용되는지 확인하는가?
8. 화면 순서와 DOM 순서를 구분하는가?

---

# 70. 접근성: 시각 순서와 읽기 순서

원본의 `order` 실험은 CSS 동작을 이해하는 데 유용합니다.

그러나 실제 콘텐츠에서 시각 순서와 DOM 순서가 다르면:

- 키보드 focus 이동이 화면과 다르게 느껴질 수 있다.
- 화면 읽기 순서가 시각 순서와 다를 수 있다.
- 숫자 단계나 문맥이 혼란스러울 수 있다.

따라서 의미 순서는 HTML에서 먼저 올바르게 작성합니다.

---

# 71. 반응형에서 Order 사용 주의

모바일에서 특정 요소를 위로 보이게 하기 위해:

```css
.sidebar {
  order: -1;
}
```

를 사용할 수 있습니다.

하지만 모바일에서 먼저 읽혀야 하는 콘텐츠라면 HTML 순서를 변경하는 것이 더 적절할 수 있습니다.

시각적 편의와 의미 순서를 구분합니다.

---

# 72. 내 코드 분석

## 72.1 장점

- main axis와 cross axis 용어를 주석으로 반복해 학습한다.
- `flex-direction` 네 값을 한 자리에서 비교할 수 있다.
- `flex-wrap` 세 값을 주석으로 보존했다.
- `justify-content`의 주요 분배 값을 모두 기록했다.
- `align-items`와 `align-content`를 한 줄·여러 줄 기준으로 구분했다.
- `order`, `flex-grow`, `flex-shrink`, `min-width`를 실제 item별 값으로 실험한다.
- 고정 크기 container라 정렬 결과를 눈으로 확인하기 쉽다.

## 72.2 개선점

- 강사님 코드와 완전히 동일하므로 개인 설명 차이는 없다.
- `width: 100px` 주석이 두 번 중복되어 있다.
- Emmet 문자열이 화면에 그대로 표시된다.
- 인라인 스타일을 클래스 기반으로 분리할 수 있다.
- `order`의 접근성 문제 설명이 없다.
- `flex-grow`, `flex-shrink`의 계산 원리 설명이 부족하다.
- `gap`, `flex-basis`, `flex` 단축 속성이 없다.
- 문서 언어와 제목이 콘텐츠에 맞지 않는다.
- 고정 300px 크기를 반응형으로 개선할 수 있다.

---

# 73. 강사님 코드 분석

## 73.1 장점

- 내 코드와 동일한 구성으로 Flexbox 핵심 container 속성을 폭넓게 실습한다.
- main axis와 cross axis 기준의 설명이 포함되어 있다.
- `align-items`와 `align-content`의 대상을 구분한다.
- item 속성인 `order`, grow, shrink를 container 속성과 함께 확인할 수 있다.
- 복잡한 외부 CSS 없이 한 HTML 파일에서 빠르게 실험할 수 있다.

## 73.2 개선점

- 내 코드와 동일하므로 별도 차이는 없다.
- 중복 width 주석의 의도를 확인할 수 없다.
- 인라인 스타일 사용으로 유지보수가 어렵다.
- 시각적 순서와 DOM 순서 차이에 대한 안내가 없다.
- shrink 계산과 min-width 상호작용 설명이 없다.
- Emmet 축약 문자열이 실제 본문에 표시된다.
- 접근성과 반응형 실무 예제가 없다.

---

# 74. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 파일명 | `15_flex.html` | `15_flex.html` |
| HTML | 동일 | 동일 |
| CSS | 동일 | 동일 |
| 주석 | 동일 | 동일 |
| 인라인 style | 동일 | 동일 |
| item 내용 | 동일 | 동일 |
| 중복 width 주석 | 있음 | 있음 |
| Emmet 문자열 | 표시됨 | 표시됨 |
| 차이 | 없음 | 없음 |

> 이번 단원은 두 원본이 완전히 동일합니다. 존재하지 않는 차이를 만들어 내지 않고 공통 코드의 장점과 개선점을 분석합니다.

---

# 75. 원본 보존 코드

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
    .container {
      border: 1px solid green;
      height: 300px;
      width: 300px;

      display: flex;
      /* display: inline-flex; */

      /* main 축의 기본값 : 왼쪽에서 오른쪽으로 */
      flex-direction: row;

      /* 오른쪽에서 왼쪽으로 */
      /* flex-direction: row-reverse; */

      /* 위에서 아래로 */
      /* flex-direction: column; */

      /* 아래에서 위로 */
      /* flex-direction: column-reverse; */

      /* 기본값, 한줄에 모든 item을 표시하려고 노력 */
      /* flex-wrap: nowrap; */

      /* 넘치는 경우 다음줄로 (inline-block 처럼) */
      /* cross축 start에서 end */
      /* flex-wrap: wrap; */

      /* cross축의 end에서 start로 */
      /* flex-wrap: wrap-reverse; */

      /* 기본값, main축의 start 방향 정렬 */
      /* justify-content: flex-start; */

      /* main축의 end 방향 정렬 */
      /* justify-content: flex-end; */

      /* main축의 가운데 정렬 */
      /* justify-content: center; */

      /* 남은 공간을 사이사이에 균등하게 배치 */
      /* justify-content: space-between; */

      /* item의 양쪽에 동일한 공간 배치 */
      /* justify-content: space-around; */

      /* 모든 공간을 균등하게 배치 */
      /* justify-content: space-evenly; */

      /* 한 줄에 대한 cross축의 이야기 */
      /* 기본값, cross축으로 쭉~ 늘리기 */
      /* align-items: stretch; */

      /* cross축의 start 방향 정렬 */
      /* align-items: flex-start; */

      /* cross축의 end 방향 정렬 */
      /* align-items: flex-end; */

      /* cross축의 중앙 정렬 */
      /* align-items: center; */

      /* 여러 줄에 대한 cross축의 이야기*/
      /* flex-wrap: wrap; */

      /* 기본값, 각 줄의 높이를 꽉 채운 상태 */
      /* align-content: stretch; */

      /* cross축 기준 start, end, 중앙 */
      /* align-content: flex-start; */
      /* align-content: flex-end; */
      /* align-content: center; */
      /* align-content: space-between; */
      /* align-content: space-around; */
      /* align-content: space-evenly; */
    }

    .container .item {
      border: 1px solid red;
      background-color: brown;
      color: #fff;

      /* width: 100px; */
      /* width: 100px; */
    }
  </style>
</head>

<body>
  div.container>div.item*5

  <div class="container">
    <div class="item">1</div>
    <div class="item" style="order: 1">2</div>
    <div class="item" style="order: -1">3</div>
    <div
      class="item"
      style="
        flex-grow: 0;
        flex-shrink: 3;
        min-width: 50px;
      "
    >
      4
    </div>
    <div
      class="item"
      style="
        flex-grow: 0;
        flex-shrink: 2;
      "
    >
      5
    </div>
  </div>
</body>
</html>
```

---

# 76. 원본 통합 개선 예제

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
  <title>CSS Flexbox</title>
  <link
    rel="stylesheet"
    href="asset/css/flex.css"
  >
</head>

<body>
  <main class="page">
    <h1>CSS Flexbox</h1>

    <!-- Emmet: div.container>div.item*5 -->
    <div class="container">
      <div class="item">1</div>
      <div class="item item--last">2</div>
      <div class="item item--first">3</div>
      <div class="item item--shrink-3">4</div>
      <div class="item item--shrink-2">5</div>
    </div>
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

.container {
  display: flex;
  width: min(100%, 300px);
  min-height: 300px;
  gap: 0.5rem;
  border: 1px solid green;
}

.item {
  display: grid;
  min-width: 0;
  padding: 0.75rem;
  border: 1px solid red;
  color: white;
  background-color: brown;
  place-items: center;
}

.item--last {
  order: 1;
}

.item--first {
  order: -1;
}

.item--shrink-3 {
  min-width: 50px;
  flex: 0 3 auto;
}

.item--shrink-2 {
  flex: 0 2 auto;
}
```

---

# 77. 헤더 실무 패턴

## HTML

```html
<header class="site-header">
  <a class="logo" href="/">
    Developer Wiki
  </a>

  <nav class="site-nav" aria-label="주요 메뉴">
    <a href="/html">HTML</a>
    <a href="/css">CSS</a>
    <a href="/javascript">JavaScript</a>
  </nav>

  <a class="login" href="/login">
    로그인
  </a>
</header>
```

## CSS

```css
.site-header {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.site-nav {
  display: flex;
  gap: 1rem;
}

.login {
  margin-left: auto;
}
```

DOM 순서를 유지하면서 auto margin으로 마지막 요소를 오른쪽에 배치합니다.

---

# 78. 버튼 그룹

```css
.button-group {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}
```

버튼이 많으면 작은 화면에서 자연스럽게 다음 줄로 넘어갑니다.

```css
.button-group button {
  min-height: 44px;
}
```

터치 영역도 함께 고려합니다.

---

# 79. 동일 너비 버튼

```css
.button-group {
  display: flex;
  gap: 1rem;
}

.button-group > button {
  flex: 1;
}
```

각 버튼이 남은 공간을 균등하게 나눕니다.

긴 텍스트가 있는 버튼은 실제 화면에서 줄바꿈과 최소 너비를 확인합니다.

---

# 80. 카드 목록

```css
.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  min-width: 0;
  flex: 1 1 16rem;
}
```

카드는 약 16rem을 기준으로 줄바꿈되고 남은 공간을 나누어 가질 수 있습니다.

열 정렬을 엄격하게 맞춰야 한다면 Grid를 검토합니다.

---

# 81. 미디어 객체 패턴

```html
<article class="media">
  <img
    class="media__image"
    src="profile.webp"
    alt="사용자 프로필"
  >

  <div class="media__body">
    <h2>사용자 이름</h2>
    <p>소개 문장...</p>
  </div>
</article>
```

```css
.media {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.media__image {
  flex: 0 0 5rem;
  width: 5rem;
}

.media__body {
  min-width: 0;
  flex: 1;
}
```

---

# 82. Footer 배치

```css
.footer {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
```

`space-between`만으로 간격을 해결하지 않고 `gap`을 함께 사용하면 줄바꿈 시에도 간격을 유지하기 쉽습니다.

---

# 83. 반응형 내비게이션

```css
.nav {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

@media (min-width: 48rem) {
  .nav {
    flex-direction: row;
    align-items: center;
  }
}
```

CSS 14의 모바일 우선 미디어 쿼리와 연결됩니다.

---

# 84. Flexbox 디버깅

브라우저 개발자 도구에서 확인할 항목:

- flex container 배지
- main axis 방향
- item 크기
- grow와 shrink 값
- free space
- flex line 개수
- gap
- min-width
- overflow
- order
- computed flex-basis

테두리를 임시로 추가하는 것도 유용합니다.

```css
* {
  outline: 1px solid rgb(255 0 0 / 20%);
}
```

실제 배포 전 제거합니다.

---

# 85. 자주 하는 실수

## 85.1 Main axis를 항상 가로로 이해

`column`에서는 main axis가 세로입니다.

## 85.2 `justify-content`를 항상 가로 정렬로 이해

main axis 정렬이므로 direction에 따라 방향이 바뀝니다.

## 85.3 `align-items`와 `align-content` 혼동

items는 item, content는 여러 line 묶음을 정렬합니다.

## 85.4 한 줄인데 `align-content` 사용

여러 줄이 아니면 효과를 확인하기 어렵습니다.

## 85.5 `order`로 의미 순서 변경

시각 순서와 DOM 순서가 달라 접근성 문제가 생길 수 있습니다.

## 85.6 Grow 비율을 최종 전체 너비 비율로 단정

남은 공간 분배 비율이지 전체 너비가 곧바로 같은 비율이 되는 것은 아닙니다.

## 85.7 Shrink 값을 단순 비율로만 계산

basis, min-width, 콘텐츠 크기도 영향을 줍니다.

## 85.8 긴 텍스트가 줄어들지 않음

flex item에 `min-width: 0`이 필요할 수 있습니다.

## 85.9 모든 스타일을 인라인으로 작성

재사용과 유지보수가 어려워집니다.

## 85.10 두 원본에 없는 차이를 만들어 냄

CSS 15의 내 코드와 강사님 코드는 완전히 동일합니다.

---


# 종합실습

## 문제 1. Flex Container

`.container`의 직계 자식을 flex item으로 만드세요.

## 문제 2. Inline Flex

컨테이너가 주변 요소와 인라인 수준으로 배치되면서 내부는 Flexbox가 되도록 작성하세요.

## 문제 3. Row Reverse

item을 main axis 역방향으로 배치하세요.

## 문제 4. Column

item을 위에서 아래로 배치하세요.

## 문제 5. Wrap

공간이 부족하면 item을 다음 flex line으로 넘기세요.

## 문제 6. Main Axis 중앙

item 묶음을 main axis 중앙에 정렬하세요.

## 문제 7. Cross Axis 중앙

한 줄 내부 item을 cross axis 중앙에 정렬하세요.

## 문제 8. 완전 중앙 정렬

row 방향 container 안에서 item을 가로·세로 중앙에 배치하세요.

## 문제 9. Space Between

첫 item과 마지막 item은 양 끝에 두고 사이 공간을 균등 분배하세요.

## 문제 10. Gap

item 사이에 16px 간격을 추가하세요.

## 문제 11. Align Content

여러 줄 전체를 cross axis 중앙에 배치하세요.

## 문제 12. Order 계산

원본의 item 1~5가 일반적인 row 방향에서 어떤 시각 순서로 보이는지 작성하세요.

## 문제 13. Order 접근성

`order`로 중요한 콘텐츠 순서를 바꿀 때 발생할 수 있는 문제를 설명하세요.

## 문제 14. Grow

두 item이 남은 공간을 1:2 비율로 분배하도록 작성하세요.

## 문제 15. Shrink

item A는 shrink 3, item B는 shrink 2가 되도록 작성하세요.

## 문제 16. Minimum Width

item이 50px 아래로 줄어들지 않도록 작성하세요.

## 문제 17. Flex 단축 속성

grow 0, shrink 3, basis auto를 단축 속성으로 작성하세요.

## 문제 18. 말줄임표

flex item 안의 긴 제목이 축소되고 한 줄 말줄임표가 되도록 작성하세요.

## 문제 19. 중복 원본 주석

원본 `.item`에서 중복된 주석을 찾아 설명하세요.

## 문제 20. 원본 동일성

내 코드와 강사님 코드의 차이를 작성하세요.

## 문제 21. 반응형 카드

카드가 약 15rem을 기준으로 줄바꿈하고 남은 공간을 채우도록 작성하세요.

## 문제 22. 종합 Header

다음 요구사항을 만족하는 header를 작성하세요.

- 로고, nav, 로그인 링크
- Flexbox 사용
- 수직 중앙 정렬
- 요소 사이 gap
- 로그인 링크를 main-end로 밀기
- nav 내부도 Flexbox
- 모바일에서는 세로 배치
- 48rem 이상에서 가로 배치
- DOM 순서와 시각 순서를 동일하게 유지
- focus-visible 표시

---

# 정답과 해설

## 정답 1

```css
.container {
  display: flex;
}
```

## 정답 2

```css
.container {
  display: inline-flex;
}
```

## 정답 3

```css
.container {
  display: flex;
  flex-direction: row-reverse;
}
```

## 정답 4

```css
.container {
  display: flex;
  flex-direction: column;
}
```

## 정답 5

```css
.container {
  display: flex;
  flex-wrap: wrap;
}
```

## 정답 6

```css
.container {
  display: flex;
  justify-content: center;
}
```

## 정답 7

```css
.container {
  display: flex;
  align-items: center;
}
```

## 정답 8

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

## 정답 9

```css
.container {
  display: flex;
  justify-content: space-between;
}
```

## 정답 10

```css
.container {
  display: flex;
  gap: 16px;
}
```

## 정답 11

```css
.container {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
}
```

여러 줄과 남는 cross axis 공간이 있어야 차이가 보입니다.

## 정답 12

```text
3 → 1 → 4 → 5 → 2
```

order -1인 3이 먼저, order 0인 1·4·5가 DOM 순서대로, order 1인 2가 마지막입니다.

## 정답 13

시각적 순서만 바뀌고 DOM, 키보드 탐색, 화면 읽기 순서는 그대로일 수 있어 사용자가 서로 다른 순서를 경험할 수 있습니다.

## 정답 14

```css
.item-a {
  flex-grow: 1;
}

.item-b {
  flex-grow: 2;
}
```

남는 공간을 1:2 비율로 분배합니다.

## 정답 15

```css
.item-a {
  flex-shrink: 3;
}

.item-b {
  flex-shrink: 2;
}
```

실제 축소량에는 기준 크기와 최소 크기도 영향을 줍니다.

## 정답 16

```css
.item {
  min-width: 50px;
}
```

## 정답 17

```css
.item {
  flex: 0 3 auto;
}
```

## 정답 18

```css
.title {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

부모 또는 해당 item이 실제로 축소 가능한 Flexbox 구조인지도 확인합니다.

## 정답 19

```css
/* width: 100px; */
/* width: 100px; */
```

같은 주석이 두 번 반복되어 있습니다. 두 번째가 height였다고 원본만으로 확정할 수 없으므로 임의로 바꾸지 않습니다.

## 정답 20

차이가 없습니다. 두 파일은 HTML, CSS, 주석, 인라인 스타일, 텍스트까지 동일합니다.

## 정답 21

```css
.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  flex: 1 1 15rem;
}
```

## 정답 22

### HTML

```html
<header class="site-header">
  <a class="site-header__logo" href="/">
    Developer Wiki
  </a>

  <nav
    class="site-header__nav"
    aria-label="주요 메뉴"
  >
    <a href="/html">HTML</a>
    <a href="/css">CSS</a>
    <a href="/javascript">JavaScript</a>
  </nav>

  <a class="site-header__login" href="/login">
    로그인
  </a>
</header>
```

### CSS

```css
.site-header {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 1rem;
  padding: 1rem;
}

.site-header__nav {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.site-header a:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}

@media (min-width: 48rem) {
  .site-header {
    flex-direction: row;
    align-items: center;
  }

  .site-header__nav {
    flex-direction: row;
    align-items: center;
  }

  .site-header__login {
    margin-left: auto;
  }
}
```

HTML 의미 순서를 유지하면서 margin-left auto로 로그인 링크를 main-end 쪽으로 배치합니다.

---

# 최종 체크리스트

## Flex Container

- [ ] 부모에 `display: flex` 또는 `inline-flex`를 적용했다.
- [ ] flex item이 직계 자식인지 확인했다.
- [ ] main axis와 cross axis를 구분했다.
- [ ] `flex-direction`에 따라 축 방향이 바뀜을 확인했다.
- [ ] `flex-wrap` 여부를 결정했다.
- [ ] container의 실제 크기와 overflow를 확인했다.

## 정렬

- [ ] `justify-content`가 main axis 정렬임을 이해했다.
- [ ] `align-items`가 item의 cross axis 정렬임을 이해했다.
- [ ] `align-content`가 여러 line 정렬임을 이해했다.
- [ ] 한 줄에서 align-content를 기대하지 않았다.
- [ ] 남는 공간이 없을 때 justify-content 차이가 작을 수 있음을 확인했다.
- [ ] item 간격에는 `gap`을 검토했다.

## Flex Item

- [ ] `order` 기본값이 0임을 이해했다.
- [ ] 시각 순서와 DOM 순서를 구분했다.
- [ ] 중요한 의미 순서를 order로 바꾸지 않았다.
- [ ] grow는 남는 공간을 분배한다.
- [ ] shrink는 부족한 공간의 축소에 관여한다.
- [ ] basis와 min-width가 크기 계산에 영향을 준다.
- [ ] 긴 콘텐츠에 `min-width: 0`이 필요한지 확인했다.
- [ ] 인라인 스타일보다 클래스를 검토했다.

## 반응형과 실무

- [ ] 고정 300px 너비가 작은 화면에서 안전한지 확인했다.
- [ ] 모바일에서 column, 넓은 화면에서 row 전환을 검토했다.
- [ ] 카드 목록에 wrap과 gap을 사용했다.
- [ ] 2차원 정렬이 필요하면 Grid를 검토했다.
- [ ] auto margin으로 특정 item을 끝으로 밀 수 있음을 이해했다.
- [ ] 개발자 도구의 Flexbox overlay를 확인했다.

## 접근성

- [ ] DOM 순서가 의미 있는 읽기 순서다.
- [ ] row-reverse와 order가 키보드 순서를 혼란스럽게 하지 않는다.
- [ ] 클릭 요소는 실제 a 또는 button이다.
- [ ] focus-visible 표시가 있다.
- [ ] 시각적 재배치 없이도 콘텐츠 구조가 이해된다.
- [ ] 반응형에서도 읽기 순서가 유지된다.

## 원본 코드 검수

- [ ] 내 코드와 강사님 코드가 동일함을 확인했다.
- [ ] 존재하지 않는 차이를 만들지 않았다.
- [ ] 중복 `width: 100px` 주석을 기록했다.
- [ ] 중복 주석의 의도를 임의로 height로 확정하지 않았다.
- [ ] 화면에 표시되는 Emmet 문자열을 기록했다.
- [ ] 인라인 `order`, grow, shrink 값을 보존했다.
- [ ] item 4의 `min-width: 50px`을 보존했다.
- [ ] `lang="en"`과 `Document`를 개선했다.

---

# 핵심 요약

- Flexbox는 flex container의 직계 자식을 flex item으로 배치한다.
- `display: flex`는 블록 수준, `inline-flex`는 인라인 수준 container를 만든다.
- Flexbox는 main axis와 cross axis를 기준으로 동작한다.
- main axis는 항상 가로가 아니며 `flex-direction`에 따라 달라진다.
- `row`는 일반적인 LTR 환경에서 왼쪽에서 오른쪽으로 배치한다.
- `row-reverse`, `column-reverse`는 시각 방향을 뒤집지만 DOM 순서를 바꾸지 않는다.
- `flex-wrap: nowrap`은 한 줄 유지가 기본값이다.
- `wrap`은 공간 부족 시 새로운 flex line을 만든다.
- `wrap-reverse`는 line이 쌓이는 cross axis 방향을 뒤집는다.
- `justify-content`는 main axis의 남는 공간을 정렬·분배한다.
- `align-items`는 각 line 안의 item을 cross axis로 정렬한다.
- `align-content`는 여러 flex line 전체를 cross axis로 배치한다.
- `align-content`는 여러 줄과 남는 cross axis 공간이 있어야 효과를 확인하기 쉽다.
- `gap`은 Flexbox item 사이 간격을 명확하게 관리한다.
- 원본 `order` 값에 따른 시각 순서는 `3 → 1 → 4 → 5 → 2`다.
- `order`는 DOM과 키보드·읽기 순서를 바꾸지 않으므로 중요한 의미 순서에 남용하지 않는다.
- `flex-grow`는 남는 양의 공간을 분배하는 비율이다.
- `flex-shrink`는 부족한 공간에서 축소되는 정도에 관여한다.
- 실제 shrink 계산에는 basis, 콘텐츠, min-width도 영향을 준다.
- 원본 item 4는 shrink 3이지만 `min-width: 50px` 아래로 줄어들 수 없다.
- 긴 flex item 콘텐츠가 축소되지 않으면 `min-width: 0`을 검토한다.
- 원본 `.item`에는 `width: 100px` 주석이 두 번 반복되어 있다.
- 두 번째 주석의 의도를 원본만으로 확정할 수 없으므로 임의로 height로 수정하지 않는다.
- 원본의 Emmet 문자열은 실제 화면에 텍스트로 표시된다.
- 내 코드와 강사님 코드의 CSS 15 원본은 완전히 동일하다.
- 한 축 중심의 정렬에는 Flexbox, 행과 열을 함께 제어할 때는 Grid가 더 적합할 수 있다.
