---
title: CSS Display와 요소 배치
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# CSS Display와 요소 배치

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `04_CSS_Display와_요소배치.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_html/css/04_display.html`, `workspace_html/css/asset/css/04_display.css`, `workspace_teacher/workspace_html/css/04_dispaly.html`, `workspace_teacher/workspace_html/css/asset/css/04_display.css` |
| 핵심 범위 | `block`, `inline`, `inline-block`, `none`, `table`, `table-cell`, `text-align`, `vertical-align`, 인라인 공백 |
| 프로젝트 연결 | 메뉴, 버튼, 배지, 카드 목록, 가운데 정렬, 요소 숨김, 레거시 테이블형 배치 |

> 이 문서는 내 코드와 강사님 코드의 `04_display.html`, `04_display.css`를 비교해 Block·Inline·Inline-block의 실제 배치와 정렬 방식을 정리한다. 잘못된 HTML 중첩과 인라인 박스 설명은 수정하고, 숨김 방식·접근성·Flex·Grid 대안까지 실무 기준으로 연결한다.

---

# 학습 목표

- `display`가 요소의 바깥쪽·안쪽 레이아웃 방식에 영향을 준다는 점을 설명한다.
- 블록 요소와 인라인 요소의 기본 흐름을 구분한다.
- 인라인 요소에서 `width`와 `height`가 기대대로 적용되지 않는 이유를 이해한다.
- 인라인 요소의 수평·수직 마진과 패딩 동작을 구분한다.
- `display: block`, `inline`, `inline-block`, `none`을 비교한다.
- `text-align`이 인라인 수준 콘텐츠를 정렬하는 속성임을 설명한다.
- `margin-inline: auto`가 블록 박스 가운데 정렬에 사용되는 조건을 설명한다.
- `vertical-align`이 일반 블록 요소의 수직 가운데 정렬 속성이 아님을 이해한다.
- `inline-block` 요소 사이의 HTML 공백이 화면 간격으로 나타나는 이유를 설명한다.
- `font-size: 0` 방식의 장단점을 이해한다.
- `display: none`이 레이아웃과 접근성 트리에서 요소를 제거한다는 점을 설명한다.
- `visibility: hidden`, `opacity: 0`, `hidden` 속성과의 차이를 구분한다.
- `display: table`, `table-cell`의 역할과 한계를 설명한다.
- 내 코드와 강사님 코드의 차이와 오류를 찾는다.
- 같은 목적을 Flexbox 또는 Grid로 더 명확하게 구현할 수 있는지 판단한다.

---

# 1. `display`란?

`display`는 요소가 레이아웃에서 어떤 종류의 박스로 참여하는지를 결정하는 핵심 속성입니다.

```css
.box {
  display: block;
}
```

대표 값:

- `block`
- `inline`
- `inline-block`
- `none`
- `table`
- `table-cell`
- `flex`
- `grid`

원본 CSS 04에서는 다음 값을 직접 실습합니다.

```text
block
inline
inline-block
none
table
table-cell
```

Flex와 Grid는 원본 04의 직접 범위는 아니므로 이 문서에서는 비교용 확장 학습으로만 다룹니다.

---

# 2. HTML 요소의 기본 `display`

브라우저의 기본 스타일시트는 요소마다 일반적인 `display` 값을 부여합니다.

대표 예:

| 요소 | 일반적인 기본값 |
| --- | --- |
| `div` | `block` |
| `p` | `block` |
| `h1` | `block` |
| `ul` | `block` |
| `span` | `inline` |
| `a` | `inline` |
| `strong` | `inline` |
| `img` | `inline` 계열의 대체 요소 |
| `table` | `table` |
| `td` | `table-cell` |

이 기본값은 HTML의 의미와 별개로 브라우저가 제공하는 표현 방식입니다.

CSS로 변경할 수 있습니다.

```css
span {
  display: block;
}
```

하지만 `display`를 바꿔도 HTML 요소의 의미가 바뀌는 것은 아닙니다.

```html
<span class="button-like">저장</span>
```

```css
.button-like {
  display: block;
}
```

위 `span`이 실제 버튼 의미를 갖게 되는 것은 아닙니다. 동작을 수행하는 요소라면 `<button>`을 사용하는 것이 적절합니다.

---

# 3. 원본의 첫 번째 블록 예제

HTML:

```html
<div id="div1">
  a<br>
  b
</div>
```

CSS:

```css
#div1 {
  border: 1px solid red;
}
```

`div`는 기본적으로 블록 요소입니다.

특징:

- 일반 흐름에서 새 줄에서 시작한다.
- 사용 가능한 가로 공간을 채우는 경향이 있다.
- 다음 블록 요소는 아래 줄에 배치된다.
- `width`, `height`, `margin`, `padding`을 일반 박스처럼 사용할 수 있다.

`<br>`는 같은 `div` 내부에서 줄을 강제로 바꿉니다.

---

# 4. 블록 요소의 너비

원본 내 코드 주석:

```text
block은 내가 가질 수 있는 최대너비를 가지고 있는 것이고
width로 지정해주는 것
```

방향은 맞지만 더 정확하게 정리하면 다음과 같습니다.

- 일반 블록 박스의 `width` 기본값은 `auto`다.
- `auto` 너비는 부모의 사용 가능한 콘텐츠 너비를 채우도록 계산되는 경우가 많다.
- 고정 `width`를 지정하면 해당 콘텐츠 너비를 사용한다.
- 마진, 패딩, 테두리와 `box-sizing`도 최종 크기에 영향을 준다.

```css
.block {
  width: 100px;
  height: 50px;
}
```

원본의 `.block`은 `100px × 50px` 콘텐츠 박스를 가집니다.

---

# 5. 블록 요소는 새 줄에서 시작한다

원본 HTML:

```html
<div class="block"></div>
<div class="block">두번째 block</div>
```

두 요소 모두 블록이므로 일반 문서 흐름에서 한 줄에 하나씩 배치됩니다.

원본 내 코드 주석:

```text
무조건 새로운 줄을 전체적으로 가지고 있기 때문에
두개의 div가 있더라도 한 줄씩 표시됨
```

보완:

- 일반 블록 흐름에서는 새 줄에 배치되는 것이 기본이다.
- `position`, `float`, Flexbox, Grid 등의 다른 레이아웃 문맥에서는 배치 방식이 달라질 수 있다.
- “항상 무조건”보다 “일반 문서 흐름에서 기본적으로”라고 설명하는 것이 정확하다.

---

# 6. 블록 요소 가운데 정렬

원본:

```css
.block {
  width: 100px;
  height: 50px;
  margin: 10px auto;
}
```

축약형 의미:

```text
위아래: 10px
좌우: auto
```

요소의 너비가 부모보다 작아 남는 가로 공간이 있으면 좌우 자동 마진이 그 공간을 나누어 가져 가운데 정렬됩니다.

논리 속성으로 작성하면:

```css
.block {
  width: 100px;
  margin-block: 10px;
  margin-inline: auto;
}
```

---

# 7. `inline` 요소란?

인라인 요소는 일반적으로 텍스트 흐름 안에 배치됩니다.

원본 HTML:

```html
<span class="inline">첫번째 inline</span>
<span class="inline">두번째 inline</span>
<span class="inline">세번째 inline</span>
```

기본 특징:

- 새 줄을 강제로 시작하지 않는다.
- 콘텐츠 길이만큼 인라인 방향의 공간을 차지한다.
- 같은 줄에 공간이 있으면 옆에 배치된다.
- 공간이 부족하면 텍스트처럼 줄바꿈될 수 있다.
- 일반 인라인 비대체 요소에는 `width`, `height`가 직접 적용되지 않는다.

---

# 8. 인라인 요소는 콘텐츠 흐름에 참여한다

원본 내 코드 주석:

```text
inline은 block과 다르게 content의 영역만 가지고 있기 때문에
옆에도 다른 content가 올 수 있음
```

조금 더 정확히 표현하면:

- 인라인 요소는 인라인 서식 문맥 안에서 텍스트와 함께 줄 상자를 구성한다.
- 자신의 콘텐츠와 수평 패딩·테두리 등을 포함한 만큼 줄 안에서 공간을 차지한다.
- 줄의 남은 공간이 부족하면 다음 줄로 일부 또는 전체가 이동할 수 있다.

`span`, `a`, `strong`은 문장 중 일부에 의미나 스타일을 부여할 때 적합합니다.

```html
<p>
  오늘은 <strong class="important">CSS display</strong>를 학습합니다.
</p>
```

---

# 9. 인라인 요소의 `width`와 `height`

원본:

```css
.inline {
  width: 200px;
  height: 100px;
}
```

일반적인 비대체 인라인 요소인 `span`에는 위 `width`, `height`가 기대한 박스 크기로 적용되지 않습니다.

```html
<span class="inline">첫번째 inline</span>
```

원본 주석:

```text
inline의 특징은 너비,높이가 적용되지 않는다
```

초기 학습 설명으로 유효합니다.

다만 이미지처럼 인라인 수준이면서 대체 요소인 경우에는 크기 속성이 적용될 수 있습니다.

```css
img {
  width: 200px;
  height: 100px;
}
```

따라서 정확한 표현은 다음과 같습니다.

```text
일반적인 비대체 inline 요소에는 width와 height가
일반 블록 박스처럼 적용되지 않는다.
```

---

# 10. 인라인 요소의 수평 마진

원본:

```css
.inline {
  margin: 30px 50px;
}
```

의미:

```text
위아래 마진: 30px
좌우 마진: 50px
```

일반 인라인 요소에서 좌우 마진은 인라인 흐름의 간격에 영향을 줍니다.

```css
.inline {
  margin-left: 50px;
  margin-right: 50px;
}
```

다른 인라인 콘텐츠를 좌우로 밀 수 있습니다.

---

# 11. 인라인 요소의 수직 마진

원본 주석:

```text
margin/padding은 좌/우는 가능하지만 상/하는 적용되지 않음
```

이 문장은 마진과 패딩을 같은 방식으로 묶어 설명하여 오해할 수 있습니다.

더 정확한 구분:

- 일반 인라인 요소의 좌우 마진은 인라인 배치에 영향을 준다.
- 위아래 마진은 일반적인 줄 배치의 높이 계산에 기대한 방식으로 영향을 주지 않는다.
- 위아래 마진값이 계산될 수 있어도 주변 줄을 블록처럼 밀어내는 효과를 기대하면 안 된다.
- 인라인 요소의 위아래 패딩과 테두리는 시각적으로 그려질 수 있다.
- 수직 패딩과 테두리가 인접 줄과 겹쳐 보일 수 있다.

따라서 인라인 요소에 큰 상하 간격이 필요하다면 `inline-block` 또는 다른 레이아웃을 검토합니다.

---

# 12. 인라인 요소의 패딩

원본:

```css
.inline {
  padding: 30px 50px;
  background-color: pink;
}
```

좌우 패딩은 인라인 흐름에서 실제 가로 공간을 늘립니다.

위아래 패딩도 배경과 테두리가 시각적으로 확장될 수 있습니다.

하지만 일반 인라인 요소의 줄 높이를 블록 박스처럼 안정적으로 확장하는 방식은 아닙니다.

원본 내 코드 주석:

```text
border에는 적용되지만 content에는 적용되지 않기때문에
상/하는 주지 않는게 좋음
좌/우는 적용이 됨
```

보다 정확한 설명:

- 상하 패딩과 테두리는 그려진다.
- 인라인 서식 문맥의 줄 높이와 주변 줄 배치가 기대와 다를 수 있다.
- 큰 상하 패딩이 필요한 UI 박스라면 `inline-block`, `flex`, `grid`가 적합하다.

---

# 13. 인라인 요소의 배경색

원본:

```css
.inline {
  background-color: pink;
}
```

배경은 콘텐츠와 패딩 영역에 그려집니다.

인라인 요소가 여러 줄로 나뉘면 배경도 줄 상자 조각마다 나뉘어 보일 수 있습니다.

```html
<span class="highlight">
  매우 길어서 여러 줄로 줄바꿈되는 텍스트
</span>
```

```css
.highlight {
  padding-inline: 0.25em;
  background-color: yellow;
}
```

본문 강조에는 적합하지만 고정 크기 카드나 버튼 구조에는 `inline-block`, Flexbox 등을 검토합니다.

---

# 14. `display: block`

원본 `.inline`에는 다음 코드가 주석 처리되어 있습니다.

```css
/* display:block; */
```

주석을 해제하면 `span`이 블록 박스처럼 배치됩니다.

```css
.inline {
  display: block;
}
```

변화:

- 새 줄에서 시작
- `width`, `height` 적용 가능
- 블록 마진과 패딩 사용 가능
- 사용 가능한 너비를 채우는 경향

하지만 HTML 의미는 여전히 `span`입니다.

텍스트 일부가 아니라 독립된 구조라면 처음부터 의미에 맞는 블록 요소를 사용하는 것이 좋습니다.

---

# 15. 인라인 안에 블록 요소를 넣은 원본

원본 HTML:

```html
<span class="inline">
  <div class="block">inline 안의 block</div>
</span>
```

내 코드 주석:

```text
inline안에는 block을 사용하지 않는 것이 좋다
```

이 구조는 단순히 “좋지 않다” 수준보다 명확한 HTML 유효성 문제가 있습니다.

`span`의 콘텐츠 모델에는 일반적인 `div` 같은 흐름 콘텐츠를 넣을 수 없습니다.

브라우저의 HTML 파서는 DOM을 자동 보정할 수 있어 개발자가 작성한 중첩과 실제 DOM이 달라질 수 있습니다.

올바른 구조:

```html
<div class="inline-wrapper">
  <div class="block">블록 콘텐츠</div>
</div>
```

또는 실제로 문장 안 콘텐츠라면:

```html
<span class="inline">
  인라인 콘텐츠
</span>
```

---

# 16. 브라우저의 DOM 자동 보정

잘못된 중첩:

```html
<span>
  <div>내용</div>
</span>
```

브라우저가 실제 DOM을 다음과 비슷하게 재구성할 수 있습니다.

```html
<span></span>
<div>내용</div>
<span></span>
```

정확한 보정 결과는 파싱 문맥에 따라 달라질 수 있습니다.

따라서 화면만 보고 “문제가 없다”고 판단하면 안 됩니다.

개발자 도구의 Elements 탭에서 실제 DOM 구조를 확인해야 합니다.

---

# 17. `display: inline`

원본:

```css
.parent > div {
  display: inline;
}
```

HTML의 `div` 요소를 인라인 박스로 바꿉니다.

```html
<div class="parent">
  <div class="child1">자식1</div>
  <div class="child2">자식2</div>
</div>
```

두 자식은 같은 줄에 배치될 수 있습니다.

그러나 다음 속성은 일반 블록처럼 동작하지 않습니다.

```css
.parent > div {
  width: 100px;
}
```

`display: inline`이므로 `width: 100px`은 일반적인 `span`과 마찬가지로 원하는 고정 너비를 만들지 않습니다.

---

# 18. `text-align`

원본 `.parent`:

```css
.parent {
  border: 1px dotted rgb(255, 0, 255);
  /* text-align: center; */
}
```

`text-align`은 블록 컨테이너 안의 인라인 수준 콘텐츠를 인라인 방향으로 정렬합니다.

```css
.parent {
  text-align: center;
}
```

정렬 대상:

- 텍스트
- 인라인 요소
- 인라인 블록 요소
- 인라인 수준 이미지

`text-align`은 블록 자식 자체를 직접 가운데 정렬하는 일반 속성이 아닙니다.

---

# 19. 자식에 `text-align`을 지정한 원본

원본:

```css
.parent > div {
  display: inline;
  text-align: center;
  width: 100px;
}
```

내 코드 주석:

```text
inline요소에 center정렬을 하더라도 이미 content영역이 꽉 차있기 때문에 의미가 없음
```

핵심은 다음과 같습니다.

- `text-align`은 요소 자신의 인라인 콘텐츠를 정렬한다.
- 일반 인라인 요소는 콘텐츠 너비에 맞춰 조각을 형성하므로 내부에 남는 가로 공간이 거의 없다.
- `width: 100px`도 일반 인라인 요소에 기대대로 적용되지 않는다.
- 따라서 눈에 보이는 가운데 정렬 효과가 나타나지 않는다.

부모에서 자식 인라인 박스를 가운데 정렬하려면:

```css
.parent {
  text-align: center;
}
```

자식 내부 텍스트를 고정 너비 안에서 가운데 정렬하려면:

```css
.parent > div {
  display: inline-block;
  width: 100px;
  text-align: center;
}
```

---

# 20. 블록 요소와 인라인 콘텐츠의 가운데 정렬 비교

| 목적 | 일반적인 방법 |
| --- | --- |
| 고정 너비 블록 박스 자체를 가운데 | `margin-inline: auto` |
| 부모 안의 텍스트·인라인 요소를 가운데 | 부모에 `text-align: center` |
| Flex 자식을 가운데 | `justify-content`, `align-items` |
| Grid 자식을 가운데 | `place-items` 또는 `place-content` |

원본 내 코드의 다음 설명은 좋은 출발점입니다.

```text
inline요소(text 등)은 text-align으로 정렬하며,
block요소는 margin: auto로
```

다만 현대 레이아웃에서는 Flex/Grid도 목적에 따라 사용합니다.

---

# 21. `inline-block`

`inline-block`은 바깥쪽 배치에서는 인라인 수준 박스로 참여하면서 내부적으로는 일반 박스 크기를 가질 수 있습니다.

원본 내 코드 주석:

```text
inline에 block의 볼륨감을 더한 것이며,
width,height,margin,padding을 모두 가질 수 있음
```

학습용 표현으로 이해하기 쉽습니다.

정리:

- 같은 줄에 나란히 놓일 수 있다.
- `width`, `height`를 지정할 수 있다.
- 상하좌우 패딩과 마진을 사용할 수 있다.
- 부모의 `text-align` 영향을 받는다.
- 기본적으로 텍스트의 기준선에 맞춰 정렬된다.

---

# 22. 원본의 `inline-block` 예제

```css
.parent2 {
  border: 1px dotted rgb(255, 0, 255);
  text-align: center;
}
```

```css
.parent2 > div {
  display: inline-block;
  width: 100px;
  height: 50px;
  margin: 30px;
  padding: 50px;
}
```

부모의 `text-align: center`가 두 인라인 블록 자식을 한 묶음의 인라인 콘텐츠처럼 가운데 정렬합니다.

각 자식은 `width`, `height`, `margin`, `padding`을 가질 수 있습니다.

기본 `content-box`라면 실제 테두리 박스는 지정 너비보다 커집니다.

가로:

```text
100px + 좌우 패딩 100px + 좌우 테두리 2px
= 202px
```

마진까지 포함하면 요소 하나가 수평으로 더 넓은 공간을 차지합니다.

---

# 23. `inline-block`과 `margin: auto`

원본 주석:

```text
margin auto는 내 땅 기준으로 보았을 때
inline요소로 땅이 없어 적용 안 됨
```

강사님 주석:

```text
내 땅이 없어서 적용 안됨
block만 됨
```

보다 정확한 설명:

- 인라인 수준 박스는 일반 블록의 자동 좌우 마진 배분 방식으로 가운데 정렬되지 않는다.
- `inline-block`의 좌우 `auto` 마진은 일반적으로 0처럼 계산된다.
- 부모에서 `text-align: center`를 사용하거나 Flex/Grid를 사용한다.

```css
.parent2 {
  text-align: center;
}
```

---

# 24. `inline-block`의 기준선 정렬

원본 `.parent3`에는 높이가 다른 콘텐츠가 있습니다.

```html
<div class="parent3">
  <div class="child1">목록1</div>
  <div class="child2 right">
    목록2<br>
    상세내용
  </div>
</div>
```

두 번째 요소에는 두 줄의 텍스트가 있습니다.

인라인 블록은 기본적으로 기준선에 맞춰 정렬됩니다.

```css
vertical-align: baseline;
```

따라서 박스의 위쪽이 서로 어긋나 보일 수 있습니다.

---

# 25. `vertical-align`

원본:

```css
.parent3 > div {
  display: inline-block;
  vertical-align: top;
}
```

`vertical-align: top`을 사용하면 인라인 서식 문맥의 줄 상자에서 인라인 블록의 위쪽을 맞출 수 있습니다.

대표 값:

- `baseline`
- `top`
- `middle`
- `bottom`
- 길이값
- 퍼센트

원본 주석:

```text
vertical은 세로정렬이며 inline에서만 적용 됨
(inline, inline-block)
```

보완:

- `vertical-align`은 인라인 수준 요소와 테이블 셀에 적용된다.
- 일반 블록 레이아웃의 자식을 부모 높이 가운데로 정렬하는 속성이 아니다.
- `display: table-cell`에서도 사용된다.

---

# 26. `vertical-align: middle`의 의미

인라인 요소에서 `middle`은 단순히 부모 박스의 정확한 기하학적 중앙을 뜻하지 않습니다.

기준선과 부모 글꼴의 x-height 등을 바탕으로 정렬됩니다.

따라서 일반 UI에서 완전한 수직 가운데 정렬이 필요하면 Flexbox가 더 예측 가능합니다.

```css
.box {
  display: flex;
  align-items: center;
}
```

원본 범위에서는 `vertical-align`의 인라인·테이블 셀 동작을 우선 이해합니다.

---

# 27. `inline-block` 사이의 공백

원본 내 코드 주석:

```text
4px 공백을 해소하기 위해 부모에 font-size 0을 주고,
하위 자식들에게 별도 font-size를 줌
```

HTML:

```html
<div class="child1">목록1</div>
<div class="child2">목록2</div>
```

두 태그 사이의 줄바꿈과 들여쓰기는 텍스트 공백 노드로 해석됩니다.

`inline-block`은 인라인 흐름에 참여하므로 이 공백이 화면 간격으로 나타납니다.

흔히 기본 글자 크기에서 약 `4px` 전후로 보이지만 정확한 크기는 글꼴과 글자 크기에 따라 달라집니다.

따라서 “항상 4px”이라고 고정해서 이해하면 안 됩니다.

---

# 28. `font-size: 0` 방식

원본:

```css
.parent3 {
  font-size: 0;
}
```

```css
.parent3 > div {
  font-size: 16px;
}
```

부모의 공백 텍스트 노드 크기를 0으로 만들어 인라인 블록 사이의 공백을 없앱니다.

자식 텍스트가 보이도록 글자 크기를 다시 설정합니다.

장점:

- 기존 인라인 블록 구조를 유지하면서 공백 제거 가능
- 간단한 레거시 레이아웃에서 사용 가능

주의:

- 자식 글자 크기를 반드시 복구해야 한다.
- 상속되는 글자 크기 체계를 깨뜨릴 수 있다.
- `rem`이 아닌 `em` 기반 자식 크기 계산에 영향을 줄 수 있다.
- 코드 의도가 처음 보는 사람에게 불명확할 수 있다.

---

# 29. 음수 마진으로 공백 제거

원본 주석 처리 코드:

```css
.parent3 > div.right {
  margin-left: -4px;
}
```

내 코드 주석:

```text
이렇게도 4px공백을 해소할 수 있지만
모바일일경우 아래로 내려가서 왼쪽으로 밀리기 때문에 비추천
```

강사님도 모바일에서 계속 적용되어 좋지 않다고 기록했습니다.

문제점:

- 실제 공백 폭이 항상 4px이라고 보장할 수 없다.
- 줄바꿈되면 다음 줄의 첫 요소가 왼쪽으로 당겨질 수 있다.
- 글꼴, 크기, 렌더링 환경에 의존한다.
- 의도를 추적하기 어렵다.

학습 예제로는 비교 가치가 있지만 실무 기본 해결책으로 권장하지 않습니다.

---

# 30. 태그 사이 공백 제거 방식

HTML 태그를 붙여 쓰면 공백 텍스트 노드를 없앨 수 있습니다.

```html
<div class="child1">목록1</div><div class="child2">
  목록2
</div>
```

또는 HTML 주석을 사이에 둘 수 있습니다.

```html
<div class="child1">목록1</div><!--
--><div class="child2">목록2</div>
```

하지만 가독성이 떨어집니다.

현대적인 나란히 배치에서는 Flexbox나 Grid가 더 명확합니다.

---

# 31. Flexbox로 인라인 블록 공백 해결

확장 학습:

```css
.parent3 {
  display: flex;
}
```

```css
.parent3 > div {
  width: 200px;
  min-height: 150px;
}
```

간격이 필요하면:

```css
.parent3 {
  display: flex;
  gap: 1rem;
}
```

장점:

- HTML 공백 노드의 영향을 받지 않는다.
- 수직 정렬을 `align-items`로 제어한다.
- 간격을 `gap`으로 명확하게 관리한다.
- 줄바꿈을 `flex-wrap`으로 설정할 수 있다.

```css
.parent3 {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  gap: 1rem;
}
```

---

# 32. 원본의 `-webkit-` 주석

내 코드 HTML:

```html
<!-- -webkit- 이라는 형태가 있는데,
이건 브라우저마다 hidden으로 있는 적용하는 방법 -->
```

이 주석은 `display`의 표준 값과 브라우저 접두사를 혼합해서 설명하고 있어 의미가 불명확합니다.

`-webkit-`은 WebKit 계열 엔진의 실험적 또는 비표준 구현에 사용된 벤더 접두사입니다.

예:

```css
-webkit-line-clamp: 2;
```

이는 `display: none`의 “브라우저마다 hidden으로 적용하는 방법”을 의미하지 않습니다.

브라우저 접두사 예:

- `-webkit-`
- `-moz-`
- `-ms-`
- `-o-`

현대 프로젝트에서는 빌드 도구의 Autoprefixer를 사용하거나 지원 현황을 확인한 뒤 필요한 접두사만 사용합니다.

---

# 33. `display: none`

원본:

```css
.hide {
  display: none;
}
```

HTML:

```html
글씨
<div class="hide">
  숨겨질 div : block
</div>
글씨
```

`display: none`이 적용되면 요소는 레이아웃에 박스를 생성하지 않습니다.

결과:

- 화면에 보이지 않는다.
- 원래 차지하던 공간도 사라진다.
- 일반적으로 접근성 트리에서도 제거된다.
- 내부 자식도 함께 표시되지 않는다.

원본 주석:

```text
브라우저에서 표시할 내용을 배치할 때 빠짐
```

핵심적으로 맞는 설명입니다.

---

# 34. `display: none`과 HTML 주석의 차이

원본 주석:

```text
주석은 영구제외
```

보완:

HTML 주석:

```html
<!--
<div>렌더링 대상이 아님</div>
-->
```

- 브라우저 DOM 요소로 생성되지 않는다.
- CSS나 일반 DOM 선택으로 표시할 수 없다.
- 개발자가 소스 코드를 수정해야 다시 요소로 사용할 수 있다.

`display: none`:

```html
<div class="hide">내용</div>
```

- DOM에는 요소가 존재한다.
- CSS 클래스 변경이나 JavaScript로 다시 표시할 수 있다.
- 데이터와 이벤트 상태가 유지될 수 있다.

---

# 35. JavaScript로 표시 상태 변경

원본 주석은 팝업을 JavaScript로 누르면 없앨 수 있다고 설명합니다.

HTML:

```html
<button
  class="popup-close"
  type="button"
>
  닫기
</button>

<div class="popup">
  팝업 내용
</div>
```

CSS:

```css
.popup.is-hidden {
  display: none;
}
```

JavaScript:

```js
const popup = document.querySelector(".popup");
const closeButton = document.querySelector(".popup-close");

closeButton.addEventListener("click", () => {
  popup.classList.add("is-hidden");
});
```

팝업과 모달은 포커스 이동, 키보드 닫기, 배경 상호작용 제한 등 접근성 요구도 함께 고려해야 합니다.

---

# 36. HTML `hidden` 속성

같은 목적에 표준 HTML 속성을 사용할 수도 있습니다.

```html
<div class="popup" hidden>
  팝업 내용
</div>
```

JavaScript:

```js
popup.hidden = false;
```

브라우저 기본 스타일은 일반적으로 다음과 비슷합니다.

```css
[hidden] {
  display: none;
}
```

단, 작성자 CSS에서 `display`를 강제로 지정하면 `hidden`의 기본 표현이 덮일 수 있으므로 프로젝트 규칙을 일관되게 유지합니다.

---

# 37. `display: none`과 접근성

`display: none` 요소는 일반적으로 스크린 리더 접근에서도 제외됩니다.

다음 경우에 적합합니다.

- 현재 열리지 않은 메뉴
- 닫힌 아코디언 패널
- 표시 전 팝업
- 조건에 따라 완전히 비활성화된 UI

다음 경우에는 주의합니다.

- 시각적으로만 숨기고 스크린 리더에는 제공해야 하는 텍스트
- 애니메이션이 필요한 접힘
- 레이아웃 공간을 유지해야 하는 요소

시각적으로만 숨기는 경우 별도의 visually-hidden 패턴을 사용합니다.

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

---

# 38. `visibility: hidden`

```css
.hidden {
  visibility: hidden;
}
```

특징:

- 화면에 보이지 않는다.
- 레이아웃 공간은 유지한다.
- 일반적으로 상호작용할 수 없다.
- 접근성 처리도 브라우저와 보조 기술에서 숨김으로 취급되는 것이 일반적이다.

비교:

```text
display: none      → 공간 제거
visibility: hidden → 공간 유지
```

---

# 39. `opacity: 0`

```css
.transparent {
  opacity: 0;
}
```

특징:

- 보이지 않지만 레이아웃 공간은 유지한다.
- 기본적으로 포인터 이벤트와 키보드 포커스 가능성이 남을 수 있다.
- 접근성 트리에서도 자동 제거되지 않는다.
- 전환 애니메이션에 사용할 수 있다.

완전히 비활성화할 필요가 있다면 추가 상태를 함께 설계합니다.

```css
.popup {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.popup.is-open {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}
```

투명도는 다음 CSS 05 문서에서 원본을 기준으로 더 자세히 다룹니다.

---

# 40. 숨김 방식 비교

| 방식 | 화면 표시 | 공간 | DOM 존재 | 일반 접근성 노출 | 상호작용 |
| --- | --- | --- | --- | --- | --- |
| HTML 주석 | 없음 | 없음 | 요소 없음 | 없음 | 없음 |
| `display: none` | 없음 | 없음 | 있음 | 일반적으로 없음 | 없음 |
| `hidden` | 없음 | 없음 | 있음 | 일반적으로 없음 | 없음 |
| `visibility: hidden` | 없음 | 유지 | 있음 | 일반적으로 없음 | 없음 |
| `opacity: 0` | 투명 | 유지 | 있음 | 남음 | 남을 수 있음 |
| visually hidden | 시각상 없음 | 거의 없음 | 있음 | 있음 | 요소에 따라 |

---

# 41. `display: table`

원본:

```css
.table {
  display: table;
}
```

`div`를 테이블 레이아웃의 테이블 박스처럼 동작하게 합니다.

```css
.table .td {
  display: table-cell;
}
```

자식은 테이블 셀 박스처럼 동작합니다.

이 방식은 실제 데이터 테이블 의미를 만들지는 않습니다.

```html
<div class="table">
  <div class="td">내용</div>
</div>
```

화면 표현만 테이블 레이아웃과 유사합니다.

---

# 42. `display: table-cell`과 `vertical-align`

원본:

```css
.table .td {
  display: table-cell;
  border: 1px solid red;
  height: 100px;
  vertical-align: middle;
}
```

테이블 셀에서는 `vertical-align: middle`로 셀 내부 콘텐츠를 세로 방향 가운데에 배치할 수 있습니다.

원본 실습의 목적은 다음과 같습니다.

```text
높이 100px인 셀 안에서 텍스트를 수직 가운데 정렬
```

가로 가운데까지 필요하면:

```css
.table .td {
  text-align: center;
  vertical-align: middle;
}
```

---

# 43. 실제 표와 CSS 테이블 레이아웃

실제 표 데이터:

```html
<table>
  <tr>
    <td>이름</td>
    <td>점수</td>
  </tr>
</table>
```

레이아웃 목적으로 만든 `div`:

```html
<div class="table-layout">
  <div class="table-layout__cell">내용</div>
</div>
```

차이:

- 실제 `<table>`은 표 데이터의 의미와 접근성 구조를 제공한다.
- `display: table`은 CSS 레이아웃 동작만 제공한다.
- 표 형식 데이터에는 실제 테이블 요소를 사용한다.
- 일반 UI 정렬에는 Flexbox나 Grid가 더 명확한 경우가 많다.

---

# 44. Flexbox로 수직 가운데 정렬

원본의 테이블 셀 수직 정렬을 현대적인 일반 UI로 바꾸면:

```css
.cell-like {
  display: flex;
  min-height: 100px;
  align-items: center;
  border: 1px solid red;
}
```

가로와 세로 모두 가운데:

```css
.cell-like {
  display: flex;
  min-height: 100px;
  align-items: center;
  justify-content: center;
}
```

Flexbox를 무조건 사용해야 한다는 뜻은 아닙니다.

실제 표라면 `<table>`, 간단한 인라인 기준선 정렬이라면 `vertical-align`, 일반 컴포넌트 정렬이라면 Flexbox처럼 목적에 맞게 선택합니다.

---

# 45. `display`와 HTML 의미

다음 두 코드는 시각적으로 비슷해질 수 있습니다.

```html
<a class="menu-item" href="/css">CSS</a>
```

```css
.menu-item {
  display: block;
}
```

```html
<div class="menu-item">CSS</div>
```

하지만 의미와 기능은 다릅니다.

- `<a>`는 링크다.
- `<div>`는 의미 없는 블록 컨테이너다.
- `display`는 의미를 바꾸지 않는다.
- 키보드 조작과 보조 기술 정보는 HTML 요소에 따라 달라진다.

스타일 목적 때문에 의미 없는 요소를 선택하지 않습니다.

---

# 46. `display`의 바깥쪽과 안쪽 개념

현대 CSS에서는 `display`를 바깥쪽과 안쪽 표시 유형의 조합으로 이해할 수 있습니다.

```css
.box {
  display: inline flex;
}
```

의미:

- 바깥쪽: 인라인 수준 박스
- 안쪽: Flex 레이아웃

일반적으로 많이 사용하는 축약값:

```css
display: block;
display: inline;
display: inline-block;
display: flex;
display: inline-flex;
display: grid;
display: inline-grid;
```

입문 단계에서는 각 키워드의 실질적 배치 결과를 우선 익히면 됩니다.

---

# 47. `display: contents` 확장 학습

```css
.wrapper {
  display: contents;
}
```

요소 자신의 박스는 생성하지 않고 자식들이 부모 레이아웃에 직접 참여하는 것처럼 만들 수 있습니다.

주의:

- 요소 자체의 배경, 테두리, 패딩 박스가 사라진다.
- 접근성 관련 브라우저 이슈를 확인해야 한다.
- 초보 단계에서 구조 문제를 우회하는 만능 해결책으로 사용하지 않는다.

원본 04에는 없는 확장 개념입니다.

---

# 48. 내 코드 분석

내 코드는 강사님 코드에 각 표시 방식의 특성과 관찰 결과를 상세하게 추가했습니다.

## 48.1 장점

- 블록이 새 줄에 배치되고 너비를 가질 수 있음을 설명했다.
- 인라인이 콘텐츠 흐름 안에 배치된다는 점을 기록했다.
- 인라인의 `width`, `height`, 마진, 패딩 동작을 비교했다.
- `text-align`과 `margin: auto`의 용도를 구분했다.
- `inline-block`이 너비·높이·여백을 가질 수 있음을 설명했다.
- 기준선 때문에 높이가 다른 인라인 블록이 어긋나는 이유를 기록했다.
- `vertical-align: top` 사용 목적을 설명했다.
- 인라인 블록 사이 공백을 `font-size: 0`으로 제거하는 과정을 기록했다.
- 음수 마진 방식이 모바일 줄바꿈에서 문제될 수 있음을 설명했다.
- `display: none`이 배치에서 빠진다는 점을 기록했다.
- CSS 테이블 셀의 수직 가운데 정렬을 실습했다.

---

# 49. 내 코드 개선점

## 49.1 `lang="en"`

본문이 한국어이므로:

```html
<html lang="ko">
```

가 적절합니다.

## 49.2 Emmet 문자열이 화면에 노출됨

원본 HTML:

```text
div.block*2
```

이 문자열은 HTML 주석이 아니므로 화면에 그대로 표시됩니다.

Emmet 메모라면 주석으로 남깁니다.

```html
<!-- Emmet: div.block*2 -->
```

## 49.3 잘못된 HTML 중첩

```html
<span class="inline">
  <div class="block">inline 안의 block</div>
</span>
```

`span` 안에 `div`를 넣는 구조는 유효하지 않습니다.

HTML 문법상 `span`은 일반적인 Flow Content인 `div`를 자식으로 가질 수 없습니다. Browser가 DOM을 자동 보정할 수 있으므로 작성한 중첩과 실제 DOM 구조가 달라질 수 있습니다.

## 49.4 인라인 패딩 설명

“상하는 적용되지 않는다”라고 단정하면 안 됩니다.

상하 패딩과 테두리는 시각적으로 그려지지만 일반 블록처럼 줄 배치를 안정적으로 밀어내지 않습니다.

## 49.5 “가짜 border” 표현

원본 주석:

```text
실제로 content영역은 밀리지 않은 것, 가짜 border
```

테두리는 실제 렌더링되는 테두리입니다.

다만 인라인 서식 문맥에서 상하 패딩과 테두리가 인접 줄의 배치 높이에 기대한 방식으로 반영되지 않는 것입니다.

## 49.6 `-webkit-` 설명

브라우저 접두사와 `hidden`은 서로 다른 개념입니다.

`-webkit-`은 WebKit 계열 구현용 접두사이며 표시 숨김 방식 자체를 뜻하지 않습니다.

## 49.7 4px 고정 표현

인라인 블록 사이 공백은 글꼴과 글자 크기에 따라 달라질 수 있습니다.

“약 4px로 보이는 경우가 많다”라고 설명하는 것이 정확합니다.

## 49.8 팝업 숨김 설명

`display: none`만으로 팝업 접근성이 완성되는 것은 아닙니다.

포커스 관리, 닫기 버튼, 키보드 조작도 필요합니다.

## 49.9 `br` 반복

문서 끝의 여러 `<br>`은 스크롤 공간을 만들기 위한 실습으로 보이지만 실제 레이아웃 간격에는 CSS를 사용해야 합니다.

```css
body {
  padding-bottom: 20rem;
}
```

실습 목적이 끝나면 제거합니다.

---

# 50. 강사님 코드 분석

강사님 코드는 다음 순서로 진행됩니다.

1. 블록 요소
2. 인라인 요소
3. 인라인 내부 블록 실험
4. `display: inline`
5. `text-align`
6. `display: inline-block`
7. 기준선과 `vertical-align`
8. 인라인 블록 공백
9. `display: none`
10. `display: table`
11. `display: table-cell`

한 파일에서 기본 표시 방식의 차이를 단계적으로 확인하기 좋습니다.

---

# 51. 강사님 코드 개선점

## 51.1 파일명 오타

강사님 HTML 파일명:

```text
04_dispaly.html
```

`display` 철자가 바뀌어 있습니다.

권장 파일명:

```text
04_display.html
```

CSS 파일명은 `04_display.css`로 올바르게 작성되어 있습니다.

## 51.2 `lang="en"`

한국어 본문이므로 `lang="ko"`가 적절합니다.

## 51.3 Emmet 문자열 노출

```text
div.block*2
```

화면 콘텐츠로 노출됩니다.

주석으로 처리해야 합니다.

## 51.4 잘못된 `span > div`

내 코드와 동일하게 유효하지 않은 중첩입니다.

## 51.5 인라인 수직 패딩 설명

“좌우는 되고 위아래는 적용 안됨”보다 실제 렌더링과 줄 상자 영향을 구분해야 합니다.

## 51.6 긴 `<br>` 반복

문서 하단에 매우 많은 `<br>`가 있습니다.

이는 콘텐츠 구조가 아니라 인위적인 공간 생성입니다.

실제 문서에서는 CSS 마진·패딩 또는 테스트 전용 최소 높이를 사용합니다.

## 51.7 `display: table`의 의미 설명 부족

CSS 테이블 레이아웃이 실제 표의 의미를 제공하지 않는다는 점을 함께 설명하면 접근성 관점이 보완됩니다.

---

# 52. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| HTML 파일명 | `04_display.html` | `04_dispaly.html` 오타 |
| 블록 설명 | 최대 너비, 새 줄 배치 상세 설명 | 예제 중심 |
| 인라인 설명 | 콘텐츠 영역과 줄바꿈 설명 추가 | 너비·높이 중심 |
| 패딩 설명 | 배경, 테두리, 콘텐츠 영향 해석 추가 | 좌우·상하 차이 요약 |
| 정렬 | `text-align`과 `margin: auto` 비교 | 코드 중심 |
| `inline-block` | “block의 볼륨감” 설명 추가 | 내 땅이 없다는 비유 |
| 기준선 | 두 줄 콘텐츠의 어긋남 이유 설명 | `vertical-align` 중심 |
| 공백 제거 | 모바일 음수 마진 문제 상세 설명 | 같은 문제 간단 기록 |
| 벤더 접두사 | `-webkit-` 관련 부정확한 주석 추가 | 해당 주석 없음 |
| 숨김 | 팝업과 JavaScript 연결 설명 | 코드만 제공 |
| 문서 하단 | `<br>` 10개 | `<br>` 약 50개 |
| 학습 성격 | 상세 복습 노트형 | 수업 진행형 |

---

# 53. 원본 통합 개선 예제

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
  <title>CSS Display</title>
  <link
    rel="stylesheet"
    href="asset/css/display.css"
  >
</head>
<body>
  <main class="page">
    <h1 class="page__title">
      CSS Display
    </h1>

    <section class="demo-section">
      <h2>Block</h2>

      <div class="block-demo">
        첫 번째 블록
      </div>

      <div class="block-demo">
        두 번째 블록
      </div>
    </section>

    <section class="demo-section">
      <h2>Inline</h2>

      <p>
        <span class="inline-demo">첫 번째</span>
        <span class="inline-demo">두 번째</span>
        <span class="inline-demo">세 번째</span>
      </p>
    </section>

    <section class="demo-section">
      <h2>Inline Block</h2>

      <div class="inline-block-list">
        <div class="inline-block-item">
          항목 1
        </div>
        <div class="inline-block-item">
          항목 2<br>
          상세 내용
        </div>
      </div>
    </section>

    <section class="demo-section">
      <h2>Hidden Content</h2>

      <button
        class="toggle-button"
        type="button"
        aria-controls="notice"
        aria-expanded="true"
      >
        안내문 숨기기
      </button>

      <div class="notice" id="notice">
        표시 상태를 변경할 안내문입니다.
      </div>
    </section>
  </main>

  <script src="asset/js/display.js"></script>
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
  color: #222;
  font-family: sans-serif;
}

.page {
  width: min(100% - 2rem, 60rem);
  margin-inline: auto;
  padding-block: 2rem;
}

.demo-section {
  margin-block: 3rem;
}

.block-demo {
  width: min(100%, 20rem);
  margin-block: 0.75rem;
  margin-inline: auto;
  padding: 1rem;
  border: 1px solid #dc2626;
}

.inline-demo {
  padding-inline: 0.5em;
  border: 1px solid #dc2626;
  background-color: #fce7f3;
}

.inline-block-list {
  text-align: center;
  font-size: 0;
}

.inline-block-item {
  display: inline-block;
  width: 10rem;
  min-height: 6rem;
  padding: 1rem;
  border: 1px solid #dc2626;
  vertical-align: top;
  font-size: 1rem;
}

.notice.is-hidden {
  display: none;
}
```

## JavaScript

```js
const button = document.querySelector(".toggle-button");
const notice = document.querySelector(".notice");

button.addEventListener("click", () => {
  const isHidden = notice.classList.toggle("is-hidden");

  button.setAttribute(
    "aria-expanded",
    String(!isHidden)
  );

  button.textContent = isHidden
    ? "안내문 표시하기"
    : "안내문 숨기기";
});
```

---

# 54. Flexbox로 개선한 나란히 배치

원본 인라인 블록 레이아웃:

```css
.parent3 {
  font-size: 0;
}

.parent3 > div {
  display: inline-block;
  vertical-align: top;
  font-size: 16px;
}
```

Flexbox 개선:

```css
.item-list {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  gap: 1rem;
}
```

```css
.item-list__item {
  width: 12rem;
  min-height: 8rem;
  padding: 1rem;
  border: 1px solid red;
}
```

Flexbox에서는 HTML 공백 제거용 `font-size: 0`이 필요하지 않습니다.

---

# 55. Grid로 개선한 카드 목록

```css
.card-list {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(12rem, 1fr));
  gap: 1rem;
}
```

화면 너비에 따라 열 개수가 자동으로 조절됩니다.

원본 04에서는 Flex/Grid 문법을 직접 다루지 않으므로, 현재는 다음 정도만 기억합니다.

```text
텍스트 흐름 일부 → inline
크기 있는 인라인 UI → inline-block
일반 세로 흐름 → block
1차원 정렬 → flex
2차원 행·열 → grid
```

---

# 56. 버튼에 `inline-block`이 필요한가?

브라우저 기본 버튼은 자체적인 버튼 표현과 박스 동작을 가집니다.

링크를 버튼처럼 표현할 때는 다음 패턴이 사용되기도 합니다.

```css
.button-link {
  display: inline-block;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  text-decoration: none;
}
```

하지만 역할은 여전히 링크입니다.

- 페이지 이동: `<a>`
- 현재 페이지 동작: `<button>`

시각적 `display`와 의미를 구분합니다.

---

# 57. 이미지 아래 공백과 인라인 기준선

`img`는 기본적으로 인라인 수준 대체 요소로 기준선에 맞춰 배치됩니다.

```html
<div class="image-wrapper">
  <img src="photo.jpg" alt="">
</div>
```

이미지 아래에 작은 공백이 보일 수 있습니다.

해결 방법:

```css
img {
  display: block;
}
```

또는 인라인 정렬을 유지한다면:

```css
img {
  vertical-align: middle;
}
```

원인은 `margin`이나 `padding`이 아니라 텍스트 기준선을 위한 공간일 수 있습니다.

---

# 58. `display: none` 전환 애니메이션 주의

다음은 부드럽게 전환되지 않습니다.

```css
.panel {
  display: none;
  transition: opacity 0.3s;
}

.panel.is-open {
  display: block;
}
```

`display`는 일반적으로 `block`과 `none` 사이를 단순한 숫자처럼 보간하지 않습니다.

전환이 필요하면 상태에 따라 다음 속성을 조합할 수 있습니다.

```css
.panel {
  opacity: 0;
  visibility: hidden;
  transform: translateY(-0.5rem);
  transition:
    opacity 0.2s,
    transform 0.2s,
    visibility 0.2s;
}

.panel.is-open {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
```

접힘 높이 애니메이션은 별도의 설계가 필요합니다.

---

# 59. 개발자 도구로 `display` 확인하기

Elements 탭에서 요소를 선택하고 Styles 또는 Computed 영역에서 확인합니다.

- 실제 계산된 `display`
- 브라우저 기본 스타일 출처
- `width`, `height`가 취소선인지
- `text-align` 상속 여부
- `vertical-align` 적용 여부
- `display: none` 규칙 출처

잘못된 `span > div` 구조는 Elements 탭에서 브라우저가 자동 보정한 DOM을 확인합니다.

---

# 60. 요소가 옆으로 배치되지 않을 때 점검

1. 자식이 블록 요소인가?
2. `display: inline` 또는 `inline-block`이 적용됐는가?
3. 자식의 전체 너비가 부모보다 큰가?
4. 패딩, 테두리, 마진까지 계산했는가?
5. HTML 공백이 추가 간격을 만드는가?
6. `white-space` 설정이 영향을 주는가?
7. 부모가 Flex 또는 Grid인지?
8. 미디어 쿼리에서 `display`가 변경되는가?
9. 숨김 클래스가 적용됐는가?
10. 개발자 도구의 Computed `display`는 무엇인가?

---

# 61. 가운데 정렬이 안 될 때 점검

## 블록 박스 자체

```css
.box {
  width: 300px;
  margin-inline: auto;
}
```

확인:

- 너비가 부모보다 작은가?
- 남는 가로 공간이 있는가?
- 요소가 일반 블록 흐름인가?

## 인라인·인라인 블록 자식

```css
.parent {
  text-align: center;
}
```

확인:

- `text-align`을 부모에 지정했는가?
- 자식이 인라인 수준 박스인가?

## Flex

```css
.parent {
  display: flex;
  justify-content: center;
}
```

축 방향을 확인합니다.

---

# 62. 수직 정렬이 안 될 때 점검

1. 요소가 인라인 또는 인라인 블록인가?
2. 테이블 셀인가?
3. 일반 블록 요소에 `vertical-align`을 사용하고 있지 않은가?
4. 기준선 정렬 때문에 위쪽이 어긋나는가?
5. `vertical-align: top`이 목적에 맞는가?
6. 완전한 가운데 정렬은 Flex/Grid가 적절한가?
7. 부모 높이가 실제로 존재하는가?
8. `line-height`로 한 줄 텍스트만 임시 정렬하려는가?
9. 콘텐츠가 두 줄 이상이 될 수 있는가?
10. 개발자 도구에서 줄 상자와 박스 크기를 확인했는가?

---

# 63. 자주 하는 실수

## 63.1 블록 요소는 언제나 화면 전체 너비라고 단정

일반 흐름에서 `width: auto`일 때 사용 가능한 너비를 채우는 경향이 있습니다. 고정 너비나 다른 레이아웃 문맥에서는 달라집니다.

## 63.2 인라인에 `width`, `height`를 지정하고 적용 기대

일반 비대체 인라인 요소에는 블록처럼 적용되지 않습니다.

## 63.3 인라인 수직 패딩이 전혀 표시되지 않는다고 생각

패딩과 배경은 보일 수 있지만 줄 배치에 기대한 방식으로 공간을 만들지 않습니다.

## 63.4 자식에 `text-align: center`를 주면 자식 박스가 가운데로 간다고 생각

`text-align`은 그 요소 내부의 인라인 콘텐츠를 정렬합니다.

## 63.5 `inline-block`에 `margin: auto`

일반 블록의 좌우 자동 마진 방식으로 가운데 정렬되지 않습니다.

## 63.6 `vertical-align`을 모든 수직 가운데 정렬에 사용

인라인 수준 요소와 테이블 셀의 정렬 속성입니다.

## 63.7 인라인 블록 간격을 항상 4px로 가정

글꼴과 글자 크기에 따라 달라질 수 있습니다.

## 63.8 음수 마진으로 공백 고정 제거

줄바꿈과 반응형 환경에서 문제가 생길 수 있습니다.

## 63.9 `display: none` 요소가 스크린 리더에는 항상 보인다고 생각

일반적으로 접근성 트리에서도 제거됩니다.

## 63.10 `display: table`이 실제 테이블 의미를 만든다고 생각

CSS 레이아웃 동작만 만들며 데이터 표의 의미는 제공하지 않습니다.

---


# 종합실습

## 문제 1. 기본 표시 방식

다음 요소의 일반적인 기본 `display`를 작성하세요.

1. `div`
2. `span`
3. `p`
4. `a`
5. `td`

## 문제 2. 블록 배치

너비 `200px`, 높이 `80px`인 블록 요소를 만들고 가로 가운데 정렬하세요.

## 문제 3. 인라인 크기

다음 코드에서 `span`의 `width: 200px`, `height: 100px`이 일반 블록처럼 적용되지 않는 이유를 설명하세요.

```css
span {
  width: 200px;
  height: 100px;
}
```

## 문제 4. 인라인 블록

문제 3의 `span`이 같은 줄에 배치되면서 너비와 높이를 갖도록 수정하세요.

## 문제 5. 부모 기준 가운데 정렬

두 개의 `inline-block` 자식을 부모 안에서 가로 가운데 정렬하세요.

## 문제 6. 내부 텍스트 정렬

너비 `120px`인 인라인 블록 내부의 텍스트를 가운데 정렬하세요.

## 문제 7. 잘못된 HTML 수정

다음 구조를 유효한 HTML로 수정하세요.

```html
<span class="wrapper">
  <div class="box">내용</div>
</span>
```

## 문제 8. 기준선 문제

높이가 다른 두 인라인 블록의 위쪽을 맞추세요.

## 문제 9. 공백 원인

다음 두 인라인 블록 사이에 화면 간격이 생기는 이유를 설명하세요.

```html
<div class="item">1</div>
<div class="item">2</div>
```

## 문제 10. `font-size: 0`

부모의 `font-size: 0`으로 공백을 제거하고 자식 글자 크기를 `1rem`으로 복구하세요.

## 문제 11. 더 나은 공백 해결

문제 9의 항목들을 Flexbox로 나란히 배치하고 간격을 `1rem`으로 지정하세요.

## 문제 12. 요소 숨김

`.notice`를 레이아웃 공간까지 제거하여 숨기세요.

## 문제 13. 공간 유지 숨김

`.notice`를 화면에서 숨기되 원래 공간은 유지하세요.

## 문제 14. 투명하지만 상호작용이 남는 방식

요소를 완전히 투명하게 만드는 속성을 작성하고, 이것이 `display: none`과 다른 점을 설명하세요.

## 문제 15. HTML `hidden`

다음 요소를 HTML 속성으로 숨기세요.

```html
<div class="popup">팝업</div>
```

## 문제 16. 테이블 셀 수직 정렬

높이 `120px`인 CSS 테이블 셀 안의 텍스트를 수직 가운데 정렬하세요.

## 문제 17. 실제 표 선택

학생 이름과 점수를 행과 열로 표현해야 합니다. `div`에 `display: table`을 사용해야 할지 실제 `<table>`을 사용해야 할지 선택하고 이유를 작성하세요.

## 문제 18. 이미지 아래 공백

인라인 이미지 아래에 작은 공백이 보입니다. 블록 이미지로 바꾸어 해결하세요.

## 문제 19. 원본 오류 수정

다음 원본 요소를 수정하세요.

```html
div.block*2
<div class="block"></div>
<div class="block">두번째 block</div>
```

Emmet 메모는 화면에 표시되지 않아야 합니다.

## 문제 20. 파일명 오타

강사님 원본의 `04_dispaly.html`을 올바른 이름으로 수정하세요.

## 문제 21. 숨김 토글

버튼을 누르면 안내문에 `.is-hidden` 클래스를 토글하고 `aria-expanded`도 함께 변경하는 JavaScript를 작성하세요.

## 문제 22. 종합 메뉴

다음 요구사항의 메뉴를 작성하세요.

- 실제 링크 요소 사용
- 데스크톱에서는 한 줄 배치
- 항목별 패딩 적용
- 링크 내부 텍스트 가운데 정렬
- 항목 사이 `0.5rem` 간격
- 작은 화면에서는 줄바꿈 가능
- HTML 공백 제거 핵 사용 금지
- 음수 마진 사용 금지
- 키보드 포커스 표시
- 현재 페이지는 `aria-current="page"`로 표시

---

# 정답과 해설

## 정답 1

| 요소 | 일반적인 기본값 |
| --- | --- |
| `div` | `block` |
| `span` | `inline` |
| `p` | `block` |
| `a` | `inline` |
| `td` | `table-cell` |

브라우저 기본 스타일시트에 따른 일반적인 값입니다.

## 정답 2

```css
.box {
  width: 200px;
  height: 80px;
  margin-inline: auto;
  border: 1px solid red;
}
```

블록 요소에 남는 가로 공간이 있어야 자동 마진의 가운데 정렬 효과가 나타납니다.

## 정답 3

`span`은 일반적인 비대체 인라인 요소입니다.

인라인 서식 문맥에서 텍스트 흐름에 참여하므로 `width`, `height`가 일반 블록 박스처럼 크기를 만들지 않습니다.

## 정답 4

```css
span {
  display: inline-block;
  width: 200px;
  height: 100px;
}
```

같은 줄에 참여하면서 박스 크기를 가질 수 있습니다.

## 정답 5

```css
.parent {
  text-align: center;
}

.parent > .item {
  display: inline-block;
}
```

부모의 `text-align`이 인라인 수준 자식을 가운데 정렬합니다.

## 정답 6

```css
.item {
  display: inline-block;
  width: 120px;
  text-align: center;
}
```

이번 `text-align`은 자식 박스 내부 텍스트를 정렬합니다.

## 정답 7

```html
<div class="wrapper">
  <div class="box">내용</div>
</div>
```

문장 안의 인라인 콘텐츠가 목적이라면 내부도 `span` 계열로 구성해야 합니다.

## 정답 8

```css
.item {
  display: inline-block;
  vertical-align: top;
}
```

기본 기준선 정렬 대신 위쪽을 맞춥니다.

## 정답 9

태그 사이의 줄바꿈과 들여쓰기가 텍스트 공백 노드로 해석되고, 인라인 블록은 인라인 흐름에 참여하기 때문에 그 공백이 화면 간격으로 나타납니다.

## 정답 10

```css
.parent {
  font-size: 0;
}

.parent > .item {
  display: inline-block;
  font-size: 1rem;
}
```

자식 글자 크기를 복구해야 합니다.

## 정답 11

```css
.parent {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
```

자식에 `inline-block`과 공백 제거 핵이 필요하지 않습니다.

## 정답 12

```css
.notice {
  display: none;
}
```

레이아웃 박스가 생성되지 않습니다.

## 정답 13

```css
.notice {
  visibility: hidden;
}
```

보이지 않지만 공간은 유지합니다.

## 정답 14

```css
.notice {
  opacity: 0;
}
```

요소는 투명하지만 레이아웃 공간이 유지되고 기본적으로 상호작용이나 접근성 노출이 남을 수 있습니다.

## 정답 15

```html
<div class="popup" hidden>
  팝업
</div>
```

## 정답 16

```css
.table {
  display: table;
}

.cell {
  display: table-cell;
  height: 120px;
  vertical-align: middle;
}
```

## 정답 17

실제 `<table>`을 사용합니다.

학생 이름과 점수는 행과 열의 관계를 가진 표 데이터이므로 실제 테이블 요소가 의미와 접근성 구조를 제공합니다.

## 정답 18

```css
img {
  display: block;
}
```

기준선 아래 문자 하강부 공간이 사라집니다.

## 정답 19

```html
<!-- Emmet: div.block*2 -->
<div class="block"></div>
<div class="block">
  두 번째 block
</div>
```

Emmet 표현은 HTML 주석으로 남깁니다.

## 정답 20

```text
04_display.html
```

`display` 철자를 사용합니다.

## 정답 21

### HTML

```html
<button
  class="toggle-button"
  type="button"
  aria-controls="notice"
  aria-expanded="true"
>
  안내문 숨기기
</button>

<div class="notice" id="notice">
  안내 내용
</div>
```

### CSS

```css
.notice.is-hidden {
  display: none;
}
```

### JavaScript

```js
const button = document.querySelector(".toggle-button");
const notice = document.querySelector(".notice");

button.addEventListener("click", () => {
  const isHidden = notice.classList.toggle("is-hidden");

  button.setAttribute(
    "aria-expanded",
    String(!isHidden)
  );

  button.textContent = isHidden
    ? "안내문 표시하기"
    : "안내문 숨기기";
});
```

## 정답 22

### HTML

```html
<nav class="main-nav" aria-label="주요 메뉴">
  <ul class="main-nav__list">
    <li class="main-nav__item">
      <a
        class="main-nav__link"
        href="/html"
      >
        HTML
      </a>
    </li>

    <li class="main-nav__item">
      <a
        class="main-nav__link"
        href="/css"
        aria-current="page"
      >
        CSS
      </a>
    </li>

    <li class="main-nav__item">
      <a
        class="main-nav__link"
        href="/javascript"
      >
        JavaScript
      </a>
    </li>
  </ul>
</nav>
```

### CSS

```css
.main-nav__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.main-nav__link {
  display: block;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  color: #1f2937;
  text-align: center;
  text-decoration: none;
}

.main-nav__link:hover {
  background-color: #f3f4f6;
}

.main-nav__link:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 2px;
}

.main-nav__link[aria-current="page"] {
  color: white;
  background-color: #2563eb;
}
```

Flexbox가 HTML 공백을 간격으로 처리하지 않으며 `gap`으로 명확하게 간격을 관리합니다.

---

# 최종 체크리스트

## 기본 표시 방식

- [ ] 블록과 인라인의 일반 흐름 차이를 설명할 수 있다.
- [ ] 블록 요소의 `width: auto` 동작을 확인했다.
- [ ] 일반 인라인 요소에 `width`, `height`를 기대하지 않았다.
- [ ] 대체 인라인 요소는 크기 동작이 다를 수 있음을 확인했다.
- [ ] `display`가 HTML 의미를 바꾸지 않는다는 점을 확인했다.

## 정렬

- [ ] 블록 박스 가운데 정렬에 남는 가로 공간이 있는지 확인했다.
- [ ] 인라인 수준 자식 정렬은 부모의 `text-align`을 사용했다.
- [ ] 자식 내부 텍스트 정렬과 자식 박스 정렬을 구분했다.
- [ ] `vertical-align`을 일반 블록 수직 가운데 정렬에 사용하지 않았다.
- [ ] 기준선 어긋남에 `vertical-align: top`이 적절한지 확인했다.
- [ ] 복잡한 정렬은 Flex/Grid가 더 명확한지 검토했다.

## 인라인 블록

- [ ] 태그 사이 공백이 화면 간격이 될 수 있음을 확인했다.
- [ ] 공백 크기를 무조건 4px로 가정하지 않았다.
- [ ] `font-size: 0` 사용 시 자식 글자 크기를 복구했다.
- [ ] 음수 마진으로 공백을 제거하지 않았다.
- [ ] 줄바꿈이 필요한 환경에서 Flexbox를 검토했다.
- [ ] `gap`으로 간격을 관리할 수 있는지 확인했다.

## 숨김

- [ ] `display: none`이 공간을 제거함을 확인했다.
- [ ] `visibility: hidden`은 공간을 유지함을 확인했다.
- [ ] `opacity: 0`은 상호작용과 접근성 노출이 남을 수 있음을 확인했다.
- [ ] HTML `hidden` 속성을 사용할 수 있는지 검토했다.
- [ ] 시각적으로만 숨길 콘텐츠에 `display: none`을 사용하지 않았다.
- [ ] 동적 팝업과 메뉴에 포커스와 ARIA 상태를 함께 설계했다.

## HTML과 접근성

- [ ] `span` 안에 `div`를 넣지 않았다.
- [ ] 화면 결과뿐 아니라 실제 DOM 자동 보정을 확인했다.
- [ ] 링크와 버튼의 의미를 `display`로 대체하지 않았다.
- [ ] 표 데이터에는 실제 `<table>`을 사용했다.
- [ ] 현재 메뉴에 `aria-current`를 적용했다.
- [ ] 키보드 포커스 표시를 제공했다.

## 원본 코드 검수

- [ ] 내 코드의 `lang="en"`을 `lang="ko"`로 개선했다.
- [ ] 강사님 파일명 `04_dispaly.html` 오타를 확인했다.
- [ ] `div.block*2`를 HTML 주석으로 변경했다.
- [ ] 인라인 수직 패딩 설명을 정확히 보완했다.
- [ ] “가짜 border” 표현을 실제 인라인 렌더링 동작으로 수정했다.
- [ ] `-webkit-` 주석과 숨김 개념을 분리했다.
- [ ] 반복 `<br>`로 공간을 만들지 않았다.
- [ ] `display: table`이 실제 표 의미를 만들지 않는다고 설명했다.

---

# 핵심 요약

- `display`는 요소가 레이아웃에 어떤 종류의 박스로 참여하는지를 결정한다.
- `div`는 일반적으로 `block`, `span`은 일반적으로 `inline`이다.
- 일반 블록 요소는 새 줄에서 시작하고 사용 가능한 너비를 채우는 경향이 있다.
- 너비가 제한된 블록 박스는 좌우 자동 마진으로 가운데 정렬할 수 있다.
- 일반 인라인 요소는 텍스트 흐름에 참여하며 `width`, `height`가 블록처럼 적용되지 않는다.
- 인라인 요소의 좌우 마진과 패딩은 인라인 배치에 영향을 준다.
- 인라인의 상하 패딩과 테두리는 보일 수 있지만 일반 블록처럼 안정적인 수직 공간을 만들지 않는다.
- `display: block`을 적용해도 HTML 요소의 의미는 바뀌지 않는다.
- `span` 안에 `div`를 넣는 원본 구조는 유효하지 않은 HTML이다.
- `display: inline`으로 바꾼 `div`에는 고정 너비가 기대대로 적용되지 않는다.
- `text-align`은 블록 컨테이너 안의 인라인 수준 콘텐츠를 정렬한다.
- 블록 박스 자체 가운데 정렬과 내부 텍스트 정렬은 서로 다른 문제다.
- `inline-block`은 같은 줄에 배치되면서 너비, 높이, 패딩, 마진을 가질 수 있다.
- 인라인 블록은 기본적으로 기준선에 정렬되므로 높이가 다르면 위쪽이 어긋날 수 있다.
- `vertical-align`은 인라인 수준 요소와 테이블 셀에 적용된다.
- HTML 태그 사이 공백은 인라인 블록 사이의 화면 간격으로 나타날 수 있다.
- `font-size: 0`은 공백을 제거할 수 있지만 자식 글자 크기 복구와 상속 문제를 고려해야 한다.
- 음수 마진으로 공백을 제거하는 방식은 반응형 줄바꿈에서 문제가 될 수 있다.
- Flexbox의 `gap`은 인라인 블록 공백 핵보다 명확한 대안이다.
- `display: none`은 화면과 레이아웃에서 요소를 제거하고 일반적으로 접근성 트리에서도 숨긴다.
- `visibility: hidden`은 공간을 유지하고, `opacity: 0`은 투명하지만 상호작용이 남을 수 있다.
- `display: table-cell`은 수직 정렬에 사용할 수 있지만 실제 표 의미를 제공하지 않는다.
- 표 데이터에는 실제 `<table>`을 사용한다.
- 원본의 `-webkit-` 주석은 벤더 접두사와 요소 숨김을 혼합한 부정확한 설명이다.
- 강사님 HTML 파일명 `04_dispaly.html`에는 `display` 철자 오타가 있다.
- 원본의 Emmet 문자열과 반복 `<br>`는 최종 문서 콘텐츠에서 정리해야 한다.
