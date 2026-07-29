# CSS Float와 Clear

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `10_CSS_Float와_Clear.md` |
| 분류 | `02_CSS` |
| 권장 선수 학습 | `09_CSS_Overflow와_스크롤.md` |
| 다음 학습 | `11_CSS_그림자와_시각효과.md` |
| 원본 기준 | `workspace_me/workspace_html/css/10_float.html`, `workspace_me/workspace_html/css/asset/css/10_float.css`, `workspace_teacher/workspace_html/css/10_float.html`, `workspace_teacher/workspace_html/css/asset/css/10_float.css` |
| 핵심 범위 | `float`, `clear`, clearfix, 텍스트 감싸기, 좌우 배치, 부모 높이 붕괴, 레거시 레이아웃 |
| 프로젝트 연결 | 기사 이미지 배치, 레거시 헤더, 좌우 버튼, 기존 코드 유지보수, Flexbox 전환 |

> 이 문서는 수업 원본의 `10_float.html`과 `10_float.css`를 기준으로 작성했습니다. 원본의 이미지 텍스트 감싸기, 좌우 박스 배치, 빈 요소의 `clear: both`, `::after` clearfix, 중앙 로고 예제를 보존하고, 부정확한 주석은 실제 float 동작에 맞게 설명했습니다. Flexbox와 Grid는 원본을 대체하는 **확장 학습**으로 구분합니다.

---

# 학습 목표

- `float`의 본래 목적이 텍스트가 이미지 주변을 흐르게 하는 것임을 설명한다.
- `float: left`와 `float: right`의 배치 방향을 구분한다.
- float 요소가 일반 블록 흐름에 미치는 영향을 이해한다.
- float가 `position: absolute`와 같은 새로운 레이어라는 설명이 왜 부정확한지 설명한다.
- float 요소가 blockification되는 동작을 이해한다.
- 여러 개의 `float: right`가 HTML 순서와 다르게 보일 수 있는 이유를 설명한다.
- 공간이 부족할 때 float 요소가 다음 줄로 내려가는 원리를 이해한다.
- `clear: left`, `right`, `both`의 역할을 설명한다.
- 빈 요소를 이용한 clear 방식의 장단점을 이해한다.
- `::after` clearfix가 부모 높이를 복구하는 원리를 설명한다.
- `display: flow-root`를 clearfix의 현대적인 대안으로 사용할 수 있다.
- 중앙 로고와 좌우 메뉴를 float로 구현한 원본 구조를 분석한다.
- `text-align: center`와 `inline-block`이 가운데 로고에 미치는 영향을 설명한다.
- float 기반 레이아웃을 Flexbox로 개선한다.
- 내 코드와 강사님 코드의 차이와 원본 오류를 찾는다.
- 의미 있는 이미지의 `alt` 누락과 외부 URL 의존성을 개선한다.

---

# 1. Float란?

`float`는 요소를 왼쪽이나 오른쪽으로 이동시키고, 뒤따르는 인라인 콘텐츠가 그 주변을 흐르게 만드는 속성입니다.

대표 값:

```css
float: none;
float: left;
float: right;
```

본래 대표 용도는 기사 안의 이미지 배치입니다.

```html
<article>
  <img src="news.webp" alt="기사 관련 사진">
  기사 본문...
</article>
```

```css
article img {
  float: right;
  width: 100px;
}
```

이미지는 오른쪽에 배치되고 본문 텍스트는 이미지의 왼쪽과 아래쪽을 따라 흐릅니다.

---

# 2. 원본 전체 구조

원본은 다음 순서로 구성됩니다.

1. 기사 이미지에 `float: right`
2. 숫자 박스 1, 2는 왼쪽 float
3. 숫자 박스 3, 4는 오른쪽 float
4. 빈 `div`에 `clear: both`
5. clearfix 부모 안의 좌우 박스
6. clearfix 헤더 안의 왼쪽 메뉴, 로고, 오른쪽 메뉴

내 코드에는 다음이 추가되어 있습니다.

- 더 자세한 float 주석
- `.test` 클래스
- 잘못된 맞춤법이 포함된 HTML 주석
- 사용되지 않는 `.coup div`
- 마지막 반복 `<br>`

---

# 3. 기사 이미지 float

내 코드와 강사님 코드:

```css
article img {
  width: 100px;
  float: right;
}
```

강사님 코드에는 실험값이 남아 있습니다.

```css
/* float: left; */
float: right;
```

최종 적용값은 `right`입니다.

화면 결과:

```text
본문 텍스트 ───────── [이미지]
본문 텍스트 ───────── [이미지]
본문 텍스트가 이미지 아래까지 이어짐
```

---

# 4. 텍스트가 이미지 주변을 흐르는 이유

float 요소는 일반 블록 요소처럼 한 줄 전체를 독점하지 않습니다.

뒤따르는 인라인 콘텐츠와 줄 상자는 float 박스가 차지한 영역을 피해서 배치됩니다.

```html
<article>
  <img class="article-image" src="photo.webp" alt="...">
  긴 본문 텍스트...
</article>
```

```css
.article-image {
  float: left;
  margin: 0 1rem 0.5rem 0;
}
```

텍스트와 이미지 사이에 여백을 주지 않으면 글자가 이미지에 너무 붙을 수 있습니다.

원본은 이미지 여백이 없으므로 다음처럼 개선할 수 있습니다.

```css
article img {
  float: right;
  width: 100px;
  margin: 0 0 0.5rem 1rem;
}
```

---

# 5. 원본 이미지 접근성

내 코드와 강사님 코드의 이미지:

```html
<img src="https://i.namu.wiki/...webp">
```

`alt` 속성이 없습니다.

이미지가 기사 내용과 관련된 의미 있는 콘텐츠라면:

```html
<img
  src="article.webp"
  alt="기사 내용을 설명하는 이미지"
>
```

장식 이미지라면:

```html
<img src="decoration.webp" alt="">
```

원본 URL은 외부 서버에 의존하므로 실제 프로젝트에서는 로컬 자산을 권장합니다.

---

# 6. `.box` 공통 스타일

내 코드:

```css
.box {
  border: 1px solid red;
  width: 100px;
  height: 100px;
  margin: 10px;
}
```

강사님 코드도 실제 결과는 같습니다.

```css
.box {
  border: 1px solid red;
  width:100px;
  height: 100px;
  margin: 10px;
}
```

차이는 강사님 코드의 `width:100px`에 공백이 없다는 정도이며 문법 오류는 아닙니다.

---

# 7. `float: left`

원본:

```css
.box.left {
  float: left;
  border: 1px solid blue;
}
```

강사님 코드:

```css
.box.left {
  float: left;
  border-color: blue;
}
```

실제 보이는 결과는 유사합니다.

- 내 코드: 테두리 전체 단축 속성을 다시 선언
- 강사님 코드: 기존 테두리에서 색상만 변경

강사님 방식은 중복이 적습니다.

---

# 8. 여러 left float

HTML:

```html
<div class="box left">1</div>
<div class="box left">2</div>
```

공간이 충분하면 다음처럼 왼쪽부터 HTML 순서대로 배치됩니다.

```text
[1] [2]
```

각 박스의 외부 너비는 기본 `content-box` 기준으로 대략 다음과 같습니다.

```text
width 100px
+ border 좌우 2px
+ margin 좌우 20px
= 122px
```

부모의 사용 가능한 너비가 부족하면 다음 박스가 아래쪽으로 내려갑니다.

---

# 9. `float: right`

원본:

```css
.box.right {
  float: right;
  border: 1px solid green;
}
```

강사님:

```css
.box.right {
  float: right;
  border-color: green;
}
```

HTML 순서:

```html
<div class="box right">3</div>
<div class="box right">4</div>
```

화면 오른쪽에서는 다음처럼 보일 수 있습니다.

```text
[4] [3]
```

먼저 등장한 `3`이 오른쪽 끝을 차지하고, 다음 `4`는 그 왼쪽에 배치되기 때문입니다.

---

# 10. 내 코드의 right 주석

원본 주석:

```text
3,4를 쓰면 우측부터 나오게되고 줄이면 4가 아래로 내려감
```

첫 부분은 의도를 이해할 수 있습니다.

정확한 설명:

```text
right float는 각 요소가 가능한 한 오른쪽으로 이동한다.
먼저 등장한 3이 오른쪽 끝을 차지하고,
뒤의 4는 3의 왼쪽에 배치될 수 있다.
공간이 부족하면 뒤 요소가 아래 줄로 내려간다.
```

“줄이면”은 부모 너비를 줄인다는 의미로 보이므로 대상을 명시하는 것이 좋습니다.

---

# 11. Float와 일반 문서 흐름

float 요소는 일반적인 블록 흐름에서 벗어나지만 `absolute`처럼 완전히 독립된 좌표 레이어로 배치되는 것은 아닙니다.

뒤따르는 텍스트와 인라인 콘텐츠는 float 영역을 피합니다.

뒤따르는 블록 박스는 float 아래에 깔릴 수 있지만, 그 안의 줄 내용은 float를 피할 수 있습니다.

따라서 float를 다음처럼 이해해야 합니다.

```text
일반 블록 배치 규칙에서는 빠짐
하지만 주변 콘텐츠의 흐름에는 영향을 줌
```

---

# 12. 원본의 “새로운 층” 설명 보완

내 코드 주석:

```text
float도 absolute처럼 새로운 층에 선언되지만 좀 다르게 1개층만 생성
```

이 설명은 부정확합니다.

float는 stacking layer를 한 층 새로 만든다고 설명할 수 없습니다.

`position: absolute`와의 차이:

| 항목 | float | absolute |
| --- | --- | --- |
| 주된 목적 | 콘텐츠 감싸기 | 좌표 기반 위치 |
| 텍스트 흐름 | float 주변으로 흐름 | 일반적으로 뒤 콘텐츠가 박스를 피하지 않음 |
| 위치 오프셋 | `top`, `left` 사용 안 함 | 오프셋 사용 |
| 기준 부모 | 별도 positioned 부모 불필요 | containing block 필요 |
| 일반 흐름 공간 | 블록 흐름에서 빠짐 | 흐름에서 빠짐 |

---

# 13. Float의 blockification

내 코드 주석:

```text
float도 inline-block으로 변경 됨
```

정확히 `display: inline-block`으로 바뀐다고 단정하는 것은 부정확합니다.

float가 적용되면 요소의 바깥쪽 표시 유형이 blockification 규칙의 영향을 받습니다.

쉽게 기억하면:

```text
인라인 요소에 float를 주어도
독립적인 박스처럼 width와 height를 가질 수 있다.
```

하지만 계산된 표시 동작을 단순히 `inline-block`이라고 부르는 것은 정확하지 않습니다.

---

# 14. Float 요소의 너비

일반 블록 요소는 기본적으로 사용 가능한 너비를 채우는 경향이 있습니다.

float 요소는 `width: auto`일 때 콘텐츠에 맞춰 줄어드는 shrink-to-fit 동작을 할 수 있습니다.

원본은 모든 `.box`에 명시적 너비를 지정했습니다.

```css
.box {
  width: 100px;
}
```

따라서 shrink-to-fit 차이는 화면에서 직접 드러나지 않습니다.

---

# 15. `clear`

`clear`는 요소의 어느 쪽에 앞선 float가 존재할 수 없는지 지정합니다.

대표 값:

```css
clear: none;
clear: left;
clear: right;
clear: both;
```

예:

```css
.next-section {
  clear: both;
}
```

앞선 왼쪽과 오른쪽 float 아래로 이동합니다.

---

# 16. 원본의 빈 clear 요소

HTML:

```html
<div class="box left">1</div>
<div class="box left">2</div>
<div class="box right">3</div>
<div class="box right">4</div>
<div style="clear: both;"></div>

<div style="border: 1px solid red;">
  다른 내용의 시작
</div>
```

빈 `div`가 양쪽 float 아래로 내려가면서 다음 콘텐츠가 float 옆으로 올라오지 않게 합니다.

---

# 17. 빈 clear 요소의 장단점

장점:

- 동작을 이해하기 쉽다.
- 빠르게 실습할 수 있다.

단점:

- 디자인 문제를 해결하기 위한 의미 없는 HTML이 추가된다.
- 인라인 스타일을 사용한다.
- 여러 위치에 반복하면 유지보수가 어렵다.
- 구조와 표현의 분리가 약해진다.

최종 코드에서는 clearfix 또는 `flow-root`를 고려합니다.

---

# 18. 내 코드의 clear 주석 보완

원본:

```text
float을 clear:both로 내린다고 해도 그 층에 남아있음
```

`clear`는 float 요소 자체를 원래 흐름으로 돌려놓는 속성이 아닙니다.

`clear`가 적용된 **뒤 요소**를 선행 float 아래로 이동시킵니다.

정확한 표현:

```text
clear: both는 앞의 float를 해제하거나 삭제하지 않는다.
clear가 적용된 요소가 양쪽 float 아래에서 시작하도록 배치한다.
```

---

# 19. `.test` 방식

내 코드에는 다음 주석이 있습니다.

```css
/* .test {
  clear: both;
} */
```

HTML:

```html
<div class="test" style="border: 1px solid red;">
  다른 내용의 시작
</div>
```

이 주석을 해제하면 `.test` 자체가 앞선 float 아래로 내려갑니다.

```css
.test {
  clear: both;
}
```

빈 요소를 별도로 추가하는 것보다 의미 있는 다음 콘텐츠에 clear를 주는 방법입니다.

하지만 매번 다음 형제에 clear를 지정해야 한다는 단점이 있습니다.

---

# 20. 부모 높이 붕괴

부모 안의 자식이 모두 float이면 부모가 자식의 높이를 정상적으로 포함하지 못할 수 있습니다.

```html
<div class="wrapper">
  <div class="left">왼쪽</div>
  <div class="right">오른쪽</div>
</div>
```

```css
.left {
  float: left;
}

.right {
  float: right;
}
```

부모에 배경색이나 테두리를 주면 높이가 거의 0처럼 보일 수 있습니다.

이를 흔히 float로 인한 부모 높이 붕괴라고 설명합니다.

---

# 21. 원본 clearfix

내 코드와 강사님 코드:

```css
.clearFix:after {
  content: "";
  display: block;
  clear: both;
}
```

가상 요소가 부모의 마지막 자식처럼 생성됩니다.

그 가상 요소에 `clear: both`가 적용되어 양쪽 float 아래로 내려갑니다.

부모는 이 가상 요소의 높이 위치까지 포함하게 되어 float 자식의 높이를 감싸는 것처럼 보입니다.

---

# 22. `:after`와 `::after`

원본:

```css
.clearFix:after
```

동작하며 오래된 브라우저 호환 때문에 한 개 콜론 표기가 널리 사용됐습니다.

현대 권장 표기:

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
```

가상 요소임을 명확히 하기 위해 `::after`를 사용합니다.

원본 클래스명은 `clearFix`로 F가 대문자입니다.

프로젝트에서는 다음처럼 이름 규칙을 통일할 수 있습니다.

```css
.clearfix
```

---

# 23. 더 전통적인 clearfix 형태

```css
.clearfix::before,
.clearfix::after {
  display: table;
  content: "";
}

.clearfix::after {
  clear: both;
}
```

과거에는 마진 상쇄 등 추가 상황까지 다루기 위해 사용됐습니다.

원본의 단순한 `display: block` 방식은 현재 실습 구조에서 float 높이 복구를 확인하기에 충분합니다.

---

# 24. `display: flow-root`

현대적인 대안:

```css
.wrapper {
  display: flow-root;
}
```

`flow-root`는 새로운 블록 서식 문맥을 만들어 float 자식을 부모 안에 포함시킵니다.

```html
<div class="wrapper">
  <div class="box left">왼쪽</div>
  <div class="box right">오른쪽</div>
</div>
```

```css
.wrapper {
  display: flow-root;
}
```

장점:

- 가상 요소가 필요 없다.
- 클래스 이름이 구현 목적을 더 직접적으로 표현한다.
- overflow를 잘라내지 않는다.

---

# 25. `overflow: hidden` clearfix 대안 주의

다음 방식도 과거에 사용됐습니다.

```css
.wrapper {
  overflow: hidden;
}
```

새 블록 서식 문맥을 만들어 float를 감쌀 수 있습니다.

하지만 다음 부작용이 있습니다.

- 자식 그림자 잘림
- 팝업과 배지 잘림
- 포커스 outline 잘림
- 실제 overflow 콘텐츠 손실

float를 감싸기 위한 목적이라면 `flow-root`가 더 명확합니다.

---

# 26. 원본 HTML 주석 오타

내 코드:

```html
<!-- 이런 형태로 감싸사 float을 초기화시켜주기도 함 -->
```

`감싸사`는 오타로 보입니다.

개선:

```html
<!-- 이런 형태로 감싸서 float의 영향을 정리하기도 함 -->
```

또한 clearfix가 float 속성을 “초기화”하는 것은 아닙니다.

부모가 float 자식 높이를 포함하도록 만드는 방식이라고 설명하는 편이 정확합니다.

---

# 27. 원본 두 번째 clearfix 예제

HTML:

```html
<div class="clearFix">
  <div class="box left">왼쪽</div>
  <div class="box right">오른쪽</div>
</div>

<div style="border: 1px solid red;">
  다른 내용의 시작
</div>
```

clearfix가 없다면 다음 콘텐츠가 float 박스의 옆이나 부모 영역과 겹쳐 보일 수 있습니다.

clearfix가 있으면 부모 높이가 float 자식을 포함하고 다음 콘텐츠는 부모 다음에서 시작합니다.

---

# 28. 원본 헤더 예제

내 코드:

```html
<div class="clearFix header">
  <div class="box left">왼쪽</div>
  <div class="box logo">로고</div>
  <div class="box right">오른쪽</div>
</div>
```

강사님 코드:

```html
<div class="clearFix header">
  <div class="box left">왼쪽 메뉴</div>
  <div class="box logo">로고</div>
  <div class="box right">장바구니</div>
</div>
```

강사님 코드는 각 영역의 역할이 더 구체적입니다.

---

# 29. 중앙 로고 스타일

원본:

```css
.logo {
  border: 1px solid red;
  width: 200px;
  /* margin: 0 auto; */
  display: inline-block;
}

.header {
  text-align: center;
}
```

`.header`의 `text-align: center`는 내부 인라인 수준 콘텐츠인 `.logo`를 가운데 정렬합니다.

`.logo`가 `inline-block`이므로 가운데 정렬 대상이 됩니다.

왼쪽과 오른쪽 메뉴는 float이므로 일반 인라인 흐름에서 빠져 양쪽에 배치됩니다.

---

# 30. `margin: auto` 주석

내 코드:

```css
/* margin: 0 auto; */
```

강사님:

```css
/* margin: auto */
```

`.logo`가 `display: inline-block`이면 좌우 `margin: auto`로 일반 블록처럼 가운데 정렬되지 않습니다.

원본은 `text-align: center`를 부모에 지정해 가운데 정렬합니다.

블록 요소와 자동 마진을 사용하려면:

```css
.logo {
  display: block;
  width: 200px;
  margin-inline: auto;
}
```

하지만 float 좌우 메뉴와 함께 사용할 때 겹침과 실제 중앙 기준을 별도로 검토해야 합니다.

---

# 31. Float 헤더의 중앙 정렬 한계

좌우 영역의 너비가 다르면 로고가 시각적으로 페이지 전체 정중앙에 있더라도 메뉴와 겹칠 수 있습니다.

예:

```text
왼쪽 메뉴 100px
로고 200px
오른쪽 장바구니 100px
```

현재 원본은 좌우 박스가 같은 너비라 비교적 균형이 맞습니다.

하지만 실제 서비스에서 왼쪽 메뉴가 더 길어지면 float 방식은 유지보수가 어려워질 수 있습니다.

---

# 32. Flexbox 헤더 개선

```css
.header {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
}

.header__left {
  justify-self: start;
}

.header__logo {
  justify-self: center;
}

.header__right {
  justify-self: end;
}
```

Grid를 사용하면 중앙 로고를 페이지 기준으로 안정적으로 가운데 배치하기 쉽습니다.

Flexbox 방식:

```css
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
```

Flexbox는 좌우 배치에는 간단하지만 중앙 항목이 항상 페이지의 정확한 정중앙이 되는 것은 좌우 너비에 따라 달라질 수 있습니다.

---

# 33. Float를 사용하기 적절한 경우

현재도 다음 상황에서는 float가 의미 있습니다.

- 기사 이미지 주변 텍스트 감싸기
- 문서 편집 스타일의 삽화
- 레거시 코드 유지보수
- `shape-outside`와 결합한 텍스트 흐름

```css
.article-image {
  float: left;
  margin: 0 1rem 0.5rem 0;
}
```

페이지의 전체 레이아웃에는 Flexbox와 Grid를 우선 검토합니다.

---

# 34. Float를 레이아웃에 사용하던 이유

Flexbox와 Grid가 널리 사용되기 전에는 다음 구조에 float를 많이 사용했습니다.

- 다단 레이아웃
- 좌측 사이드바와 본문
- 가로 내비게이션
- 좌우 헤더
- 카드 그리드

이 때문에 기존 서비스 코드에서는 clearfix 패턴을 자주 발견할 수 있습니다.

학습 목적:

```text
새 프로젝트에서 무조건 사용하기보다
기존 코드를 이해하고 유지보수할 수 있도록 학습
```

---

# 35. 사용되지 않는 `.coup div`

내 코드 CSS:

```css
.coup div {
  border: 1px solid red;
  width: 100px;
  height: 100px;
}
```

현재 `10_float.html`에는 `.coup` 클래스가 없습니다.

따라서 이 규칙은 현재 문서에서 사용되지 않습니다.

가능한 해석:

- 이전 실습 코드의 흔적
- 작성 예정이던 예제
- 클래스명 오타

원본에서는 삭제하지 않고 “현재 HTML에서 미사용”으로 기록합니다.

최종 프로젝트에서는 필요성을 확인한 뒤 제거합니다.

---

# 36. 인라인 스타일

원본 HTML:

```html
<div style="clear: both;"></div>
```

```html
<div style="border: 1px solid red;">
  다른 내용의 시작
</div>
```

학습 과정에서 속성을 바로 확인하기에는 편리하지만, 반복 사용과 유지보수를 위해 클래스가 좋습니다.

```css
.clear-both {
  clear: both;
}

.next-content {
  border: 1px solid red;
}
```

다만 의미 없는 빈 clear 요소 자체는 최종 구조에서 제거하는 것이 더 좋습니다.

---

# 37. 반복 `<br>`

내 코드 마지막:

```html
<br><br><br><br><br><br><br><br><br><br>
```

강사님 코드에는 반복 `<br>`가 없습니다.

내 코드의 하단 공간 확보용으로 보입니다.

개선:

```css
body {
  padding-bottom: 10rem;
}
```

또는 테스트 목적이 끝나면 제거합니다.

---

# 38. 문서 언어와 제목

내 코드와 강사님 코드:

```html
<html lang="en">
<title>Document</title>
```

본문은 한국어를 포함하므로:

```html
<html lang="ko">
<title>CSS Float와 Clear</title>
```

로 개선합니다.

---

# 39. My Code 분석

## 39.1 장점

- float와 absolute가 다르다는 점을 설명하려 했다.
- 왼쪽과 오른쪽 float의 화면 순서를 기록했다.
- 부모 너비가 줄어들 때 다음 줄로 내려가는 현상을 설명했다.
- `clear: both`와 clearfix의 차이를 실습했다.
- `.test { clear: both; }` 대안을 주석으로 남겼다.
- 중앙 로고를 `inline-block`과 `text-align`으로 배치했다.
- 강사님 코드보다 복습용 설명이 많다.

## 39.2 개선점

- float가 새로운 한 개 레이어를 만든다는 설명은 부정확하다.
- float가 정확히 `inline-block`이 된다는 설명도 부정확하다.
- clear가 float를 초기화하거나 float 자체를 내리는 것은 아니다.
- “감싸사” 오타를 수정해야 한다.
- `.coup div`는 현재 HTML에서 사용되지 않는다.
- 이미지에 `alt`가 없다.
- 외부 이미지 URL에 의존한다.
- 반복 `<br>`가 있다.
- 테두리는 `border-color`만 바꾸면 중복을 줄일 수 있다.

---

# 40. Teacher Code 분석

## 40.1 장점

- 이미지 float의 본래 텍스트 감싸기 용도를 간결하게 보여 준다.
- `float: left` 실험값을 주석으로 남겼다.
- `.box`의 공통 테두리에서 색상만 변경해 중복이 적다.
- 빈 clear 요소와 clearfix를 모두 보여 준다.
- 헤더 문구가 `왼쪽 메뉴`, `장바구니`로 역할 중심이다.
- 내 코드에 있는 미사용 `.coup`과 반복 `<br>`가 없다.

## 40.2 개선점

- 이미지의 `alt`가 없다.
- 외부 이미지 URL을 사용한다.
- 인라인 스타일을 사용한다.
- 문서 언어가 `en`이다.
- 제목이 `Document`다.
- clearfix의 동작 설명이 코드에 없다.
- float 기반 헤더의 반응형 한계를 설명하지 않는다.
- `margin: auto` 주석에 세미콜론이 없지만 주석이므로 실행에는 영향이 없다.

---

# 41. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기사 본문 | 3회 반복 | 4회 반복 |
| 이미지 float | `right` | `right`, `left` 실험 주석 |
| left 테두리 | `border` 전체 재선언 | `border-color`만 변경 |
| right 테두리 | `border` 전체 재선언 | `border-color`만 변경 |
| float 설명 | 상세하지만 일부 부정확 | 설명 거의 없음 |
| 다음 콘텐츠 클래스 | `.test` 추가 | 클래스 없음 |
| clearfix HTML 주석 | 있음, `감싸사` 오타 | 없음 |
| 미사용 규칙 | `.coup div` | 없음 |
| 헤더 문구 | 왼쪽 / 오른쪽 | 왼쪽 메뉴 / 장바구니 |
| 반복 `<br>` | 10개 | 없음 |
| 학습 성격 | 개인 복습 주석형 | 최소 수업 예제형 |

---

# 42. 원본 통합 개선 예제

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
  <title>CSS Float와 Clear</title>
  <link
    rel="stylesheet"
    href="asset/css/float.css"
  >
</head>
<body>
  <main class="page">
    <article class="article">
      <h1>Float 이미지</h1>

      <img
        class="article__image"
        src="asset/images/article.webp"
        alt="기사 내용과 관련된 예제 이미지"
      >

      <p>
        긴 기사 본문이 이미지 주변으로 흐르는
        float의 본래 사용 목적을 확인합니다.
      </p>
    </article>

    <section class="float-demo">
      <h2>좌우 Float</h2>

      <div class="float-demo__group">
        <div class="box box--left">왼쪽</div>
        <div class="box box--right">오른쪽</div>
      </div>
    </section>

    <header class="site-header">
      <nav class="site-header__left">
        왼쪽 메뉴
      </nav>

      <a class="site-header__logo" href="/">
        로고
      </a>

      <a class="site-header__right" href="/cart">
        장바구니
      </a>
    </header>
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

.article {
  display: flow-root;
}

.article__image {
  float: right;
  width: 100px;
  margin: 0 0 0.75rem 1rem;
}

.float-demo__group {
  display: flow-root;
  border: 1px solid #d1d5db;
}

.box {
  width: 100px;
  height: 100px;
  margin: 10px;
  border: 1px solid;
}

.box--left {
  float: left;
  border-color: blue;
}

.box--right {
  float: right;
  border-color: green;
}

.site-header {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  margin-top: 3rem;
}

.site-header__left {
  justify-self: start;
}

.site-header__logo {
  justify-self: center;
}

.site-header__right {
  justify-self: end;
}
```

---

# 43. 기사 이미지 실무 패턴

```css
.article__image {
  float: left;
  width: min(40%, 15rem);
  margin:
    0
    1rem
    0.75rem
    0;
}
```

작은 화면에서는 float를 해제할 수 있습니다.

```css
@media (max-width: 36rem) {
  .article__image {
    float: none;
    display: block;
    width: 100%;
    margin:
      0
      0
      1rem;
  }
}
```

---

# 44. `shape-outside` 확장 학습

float 요소 주변의 텍스트 흐름 모양을 조절할 수 있습니다.

```css
.profile {
  float: left;
  width: 10rem;
  aspect-ratio: 1;
  margin-right: 1rem;
  border-radius: 50%;
  shape-outside: circle(50%);
}
```

원형 이미지 주위를 따라 텍스트가 흐를 수 있습니다.

원본에는 없는 확장 학습입니다.

---

# 45. 개발자 도구 확인 항목

- 요소에 적용된 최종 `float`
- float 박스의 실제 외부 너비
- 오른쪽 float의 화면 순서
- 부모의 계산 높이
- `::after` 가상 요소 생성 여부
- `clear: both`의 최종 위치
- 미사용 `.coup` 규칙
- 취소선 처리된 스타일
- 이미지 외부 URL 로드 상태

---

# 46. 부모 높이가 0일 때 점검

1. 자식이 모두 float인가?
2. 부모에 clearfix가 있는가?
3. `::after`에 `content`가 있는가?
4. 가상 요소가 `display: block`인가?
5. `clear: both`가 적용됐는가?
6. 클래스명이 `clearFix`와 정확히 일치하는가?
7. `display: flow-root`가 더 적절한가?
8. overflow를 사용해 콘텐츠가 잘리고 있지 않은가?
9. 부모 높이를 고정값으로 억지 지정하려는가?
10. 개발자 도구에서 가상 요소를 확인했는가?

---

# 47. float 순서가 예상과 다를 때 점검

1. `left`인지 `right`인지 확인한다.
2. HTML 등장 순서를 확인한다.
3. 오른쪽 float는 먼저 나온 요소가 더 오른쪽인지 확인한다.
4. 부모의 사용 가능한 너비를 확인한다.
5. 각 박스의 margin과 border를 포함한 외부 너비를 계산한다.
6. 앞선 float가 공간을 차지하고 있는지 확인한다.
7. `clear`가 중간에 적용됐는지 확인한다.
8. 이미지 float가 같은 영역에 있는지 확인한다.
9. 미디어 쿼리에서 float가 변경되는지 확인한다.
10. Flex/Grid로 전환할 수 있는 레이아웃인지 검토한다.

---

# 48. 자주 하는 실수

## 48.1 float를 absolute와 같은 레이어로 이해

주변 텍스트 흐름에 영향을 주므로 동작이 다릅니다.

## 48.2 float가 무조건 inline-block이 된다고 설명

blockification을 단순화한 표현이며 정확하지 않습니다.

## 48.3 clear가 float 자체를 해제한다고 생각

clear가 적용된 뒤 요소의 시작 위치를 조절합니다.

## 48.4 부모 높이 붕괴를 고정 높이로 해결

콘텐츠 변화에 취약합니다. clearfix 또는 flow-root를 사용합니다.

## 48.5 모든 레이아웃을 float로 구현

Flexbox와 Grid가 더 적절한 경우가 많습니다.

## 48.6 오른쪽 float의 순서 혼동

먼저 나온 요소가 더 오른쪽을 차지할 수 있습니다.

## 48.7 이미지에 여백 미지정

텍스트가 이미지에 너무 붙습니다.

## 48.8 의미 없는 빈 clear 요소 반복

HTML 구조가 불필요하게 늘어납니다.

## 48.9 overflow hidden으로 무조건 clearfix

그림자, 포커스, 팝업이 잘릴 수 있습니다.

## 48.10 사용되지 않는 CSS 방치

원본의 `.coup div`처럼 현재 HTML과 연결되지 않는 규칙이 남을 수 있습니다.

---

# 49. 면접·복습 포인트

## Q1. Float의 본래 목적은 무엇인가요?

이미지 같은 요소를 한쪽에 배치하고 뒤따르는 텍스트가 그 주변으로 흐르게 만드는 것입니다.

## Q2. float 요소는 일반 흐름에 남아 있나요?

일반 블록 흐름에서는 빠지지만 주변 줄 내용과 텍스트 흐름에는 영향을 줍니다.

## Q3. `float: right` 요소가 여러 개면 순서가 어떻게 보이나요?

먼저 등장한 요소가 가능한 가장 오른쪽을 차지하고, 뒤 요소가 그 왼쪽에 배치될 수 있습니다.

## Q4. `clear: both`는 무엇을 하나요?

clear가 적용된 요소가 앞선 왼쪽·오른쪽 float 아래에서 시작하도록 배치합니다.

## Q5. Clearfix가 필요한 이유는 무엇인가요?

자식이 모두 float일 때 부모가 자식 높이를 포함하지 못하는 문제를 해결하기 위해 사용합니다.

## Q6. 원본 clearfix는 어떻게 작동하나요?

부모의 `::after` 가상 요소를 만들고 `clear: both`를 적용해 float 아래까지 부모의 흐름을 확장합니다.

## Q7. Clearfix의 현대적인 대안은 무엇인가요?

`display: flow-root`를 사용할 수 있습니다.

## Q8. float가 적용되면 요소는 inline-block이 되나요?

정확히 inline-block으로 설정되는 것은 아니며 blockification 규칙에 따라 독립적인 박스처럼 동작합니다.

## Q9. 새 레이아웃에 float보다 Flexbox와 Grid가 권장되는 이유는 무엇인가요?

행·열 정렬, 간격, 반응형 배치를 더 명확하고 안정적으로 제어할 수 있기 때문입니다.

## Q10. Float가 현재도 유용한 상황은 무엇인가요?

기사 이미지 주변 텍스트 감싸기와 레거시 레이아웃 유지보수입니다.

---

# Problems

## 문제 1. 기사 이미지

기사 이미지를 왼쪽에 배치하고 텍스트가 오른쪽과 아래로 흐르게 하세요.

## 문제 2. 이미지 여백

문제 1의 이미지와 오른쪽 텍스트 사이에 `1rem`, 이미지 아래에 `0.5rem` 여백을 주세요.

## 문제 3. 오른쪽 float 순서

다음 코드의 일반적인 화면 순서를 오른쪽부터 작성하세요.

```html
<div class="right">3</div>
<div class="right">4</div>
```

```css
.right {
  float: right;
}
```

## 문제 4. Clear

앞선 왼쪽과 오른쪽 float 아래에서 `.next`가 시작하도록 작성하세요.

## 문제 5. 빈 요소 방식

원본처럼 빈 요소로 양쪽 float를 clear하는 HTML을 작성하세요.

## 문제 6. 빈 요소 방식의 단점

문제 5 방식의 단점을 두 가지 작성하세요.

## 문제 7. Clearfix

`.clearfix` 부모가 float 자식 높이를 포함하도록 `::after`를 작성하세요.

## 문제 8. Flow-root

문제 7을 한 줄의 현대적인 CSS로 대체하세요.

## 문제 9. 원본 설명 수정

다음 주석을 정확하게 수정하세요.

```text
float도 absolute처럼 새로운 층에 선언됨
```

## 문제 10. Blockification

다음 주석이 부정확한 이유를 설명하세요.

```text
float도 inline-block으로 변경됨
```

## 문제 11. 왼쪽과 오른쪽 박스

공통 `.box` 테두리는 유지하고 `.left`는 파랑, `.right`는 초록 테두리색만 적용하세요.

## 문제 12. 부모 높이

float 자식만 있는 부모의 배경색이 보이지 않는 이유를 설명하세요.

## 문제 13. 중앙 로고

원본 방식처럼 왼쪽과 오른쪽 영역은 float하고 로고는 `inline-block`, 부모는 `text-align: center`로 작성하세요.

## 문제 14. Grid 개선

문제 13을 3열 Grid로 개선하여 로고를 가운데 배치하세요.

## 문제 15. Alt

의미 있는 기사 이미지에 적절한 `alt`를 추가하세요.

## 문제 16. 외부 URL

외부 이미지 URL을 로컬 `asset/images/article.webp`로 변경하세요.

## 문제 17. 오타 수정

다음 원본 주석을 수정하세요.

```text
이런 형태로 감싸사 float을 초기화
```

## 문제 18. 미사용 CSS

HTML에 `.coup`이 없는데 `.coup div` 규칙이 있습니다. 코드 리뷰에서 어떻게 처리해야 하는지 작성하세요.

## 문제 19. 반복 BR

하단 여백을 위한 `<br>` 10개를 CSS로 대체하세요.

## 문제 20. 반응형 기사

데스크톱에서는 이미지가 왼쪽으로 float하고 `36rem` 이하에서는 float를 해제해 전체 너비로 표시하세요.

## 문제 21. Float 너비

`100px` 너비, 좌우 `10px` margin, 좌우 `1px` border인 content-box float 박스의 대략적인 외부 너비를 계산하세요.

## 문제 22. 종합 레거시 개선

다음 요구사항을 만족하세요.

- 원본 float 기사 예제는 유지
- 기사 부모는 float 자식을 포함
- 이미지에 alt와 여백
- 좌우 헤더는 Grid로 교체
- 가운데 로고가 좌우 콘텐츠 너비와 무관하게 중앙
- 모바일에서 1열 헤더
- CSS 변수로 테두리색 관리
- 의미 없는 clear div 제거
- 반복 `<br>` 제거

---

# Answers & Explanations

## 정답 1

```css
.article-image {
  float: left;
}
```

## 정답 2

```css
.article-image {
  float: left;
  margin: 0 1rem 0.5rem 0;
}
```

## 정답 3

```text
오른쪽부터 3, 4
```

화면을 왼쪽에서 읽으면 `4, 3`처럼 보일 수 있습니다.

## 정답 4

```css
.next {
  clear: both;
}
```

## 정답 5

```html
<div class="left">왼쪽</div>
<div class="right">오른쪽</div>
<div style="clear: both;"></div>
```

## 정답 6

예:

```text
1. 의미 없는 HTML 요소가 추가된다.
2. 인라인 스타일이나 반복 마크업으로 유지보수가 어려워진다.
```

## 정답 7

```css
.clearfix::after {
  display: block;
  clear: both;
  content: "";
}
```

## 정답 8

```css
.wrapper {
  display: flow-root;
}
```

## 정답 9

```text
float는 absolute처럼 독립 좌표 레이어를 만드는 속성이 아니다.
일반 블록 흐름에서는 빠지지만 주변 텍스트와 줄 내용이
float 영역을 피해 흐르도록 영향을 준다.
```

## 정답 10

float가 적용될 때 요소는 blockification 규칙의 영향을 받아 독립적인 박스처럼 동작하지만, CSS 값이 단순히 `display: inline-block`으로 설정되는 것은 아닙니다.

## 정답 11

```css
.box {
  border: 1px solid red;
}

.box.left {
  float: left;
  border-color: blue;
}

.box.right {
  float: right;
  border-color: green;
}
```

## 정답 12

float 자식은 일반 블록 흐름에서 빠지기 때문에 부모가 자식의 높이를 일반적인 방식으로 계산하지 못할 수 있습니다.

clearfix나 `display: flow-root`로 해결합니다.

## 정답 13

```css
.header {
  text-align: center;
}

.header__left {
  float: left;
}

.header__logo {
  display: inline-block;
  width: 200px;
}

.header__right {
  float: right;
}
```

부모에는 clearfix가 필요합니다.

## 정답 14

```css
.header {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
}

.header__left {
  justify-self: start;
}

.header__logo {
  justify-self: center;
}

.header__right {
  justify-self: end;
}
```

## 정답 15

```html
<img
  src="article.webp"
  alt="기사 내용을 설명하는 예제 이미지"
>
```

실제 이미지 내용에 맞게 작성합니다.

## 정답 16

```html
<img
  src="asset/images/article.webp"
  alt="기사 내용을 설명하는 예제 이미지"
>
```

## 정답 17

```text
이런 형태로 부모를 감싸고 clearfix를 적용해
부모가 float 자식의 높이를 포함하도록 만들기도 함
```

## 정답 18

현재 HTML에서 사용되지 않는 규칙임을 확인하고, 다른 페이지나 JavaScript에서 동적으로 사용하는지 검색한 뒤 필요 없으면 제거합니다. 근거 없이 바로 삭제하거나 남겨 두지 않습니다.

## 정답 19

```css
body {
  padding-bottom: 10rem;
}
```

## 정답 20

```css
.article-image {
  float: left;
  width: min(40%, 15rem);
  margin: 0 1rem 0.5rem 0;
}

@media (max-width: 36rem) {
  .article-image {
    float: none;
    display: block;
    width: 100%;
    margin: 0 0 1rem;
  }
}
```

## 정답 21

```text
100px + 20px + 2px = 122px
```

## 정답 22

### HTML

```html
<article class="article">
  <img
    class="article__image"
    src="asset/images/article.webp"
    alt="기사 내용을 설명하는 이미지"
  >
  <p>기사 본문...</p>
</article>

<header class="site-header">
  <nav class="site-header__left">
    왼쪽 메뉴
  </nav>

  <a class="site-header__logo" href="/">
    로고
  </a>

  <a class="site-header__right" href="/cart">
    장바구니
  </a>
</header>
```

### CSS

```css
:root {
  --color-border: #d1d5db;
}

.article {
  display: flow-root;
}

.article__image {
  float: left;
  width: min(40%, 15rem);
  margin: 0 1rem 0.75rem 0;
}

.site-header {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  border: 1px solid var(--color-border);
}

.site-header__left {
  justify-self: start;
}

.site-header__logo {
  justify-self: center;
}

.site-header__right {
  justify-self: end;
}

@media (max-width: 36rem) {
  .article__image {
    float: none;
    display: block;
    width: 100%;
    margin: 0 0 1rem;
  }

  .site-header {
    grid-template-columns: 1fr;
    gap: 0.75rem;
    text-align: center;
  }

  .site-header__left,
  .site-header__logo,
  .site-header__right {
    justify-self: center;
  }
}
```

---

# Final Checklist

## Float 기본

- [ ] float의 본래 목적이 텍스트 감싸기임을 이해했다.
- [ ] `left`, `right`의 배치 방향을 확인했다.
- [ ] 오른쪽 float의 화면 순서를 확인했다.
- [ ] 부모 너비가 부족할 때 줄바꿈되는지 확인했다.
- [ ] margin과 border를 포함한 외부 너비를 계산했다.

## 흐름과 Clear

- [ ] float를 absolute와 같은 레이어로 설명하지 않았다.
- [ ] blockification을 inline-block 변경으로 단정하지 않았다.
- [ ] clear가 float 자체를 삭제하지 않음을 이해했다.
- [ ] 의미 없는 빈 clear 요소를 최소화했다.
- [ ] 다음 콘텐츠에 clear를 직접 줄지 부모를 감쌀지 결정했다.

## 부모 높이

- [ ] float 자식만 있는 부모 높이를 확인했다.
- [ ] clearfix의 `content`, `display`, `clear`를 확인했다.
- [ ] `:after`를 `::after`로 개선할 수 있는지 확인했다.
- [ ] `display: flow-root`를 검토했다.
- [ ] clearfix 목적으로 hidden을 쓸 때 잘림 부작용을 확인했다.

## 접근성

- [ ] 의미 있는 이미지에 `alt`를 제공했다.
- [ ] 외부 이미지 URL 의존성을 줄였다.
- [ ] 이미지와 텍스트 사이 여백을 제공했다.
- [ ] 모바일에서 float 이미지가 너무 좁아지지 않는지 확인했다.
- [ ] 실제 메뉴에는 의미 있는 링크와 내비게이션 구조를 사용했다.

## 레이아웃 개선

- [ ] 전체 페이지 레이아웃에 Flexbox나 Grid가 더 적절한지 검토했다.
- [ ] 가운데 로고가 좌우 콘텐츠와 겹치지 않는지 확인했다.
- [ ] 모바일 헤더 배치를 확인했다.
- [ ] 레거시 float 코드를 무조건 삭제하지 않고 의도를 먼저 파악했다.

## 원본 코드 검수

- [ ] `lang="en"`을 `lang="ko"`로 개선했다.
- [ ] `Document` 제목을 학습 주제로 변경했다.
- [ ] 내 코드의 “새로운 층” 설명을 보완했다.
- [ ] 내 코드의 “inline-block 변경” 설명을 보완했다.
- [ ] `감싸사` 오타를 수정했다.
- [ ] `.coup div`가 미사용임을 기록했다.
- [ ] 반복 `<br>`를 CSS 공간으로 대체했다.
- [ ] 내 코드와 강사님의 테두리 선언 차이를 보존했다.
- [ ] 강사님의 역할 중심 헤더 문구를 기록했다.

---

# Key Summary

- float는 이미지 주변으로 텍스트를 흐르게 하는 것이 본래 목적이다.
- `float: left`는 요소를 왼쪽에, `float: right`는 오른쪽에 배치한다.
- 여러 right float에서는 먼저 나온 요소가 더 오른쪽을 차지할 수 있다.
- float 요소는 일반 블록 흐름에서는 빠지지만 주변 텍스트 흐름에는 영향을 준다.
- float를 absolute와 같은 새 레이어라고 설명하는 것은 부정확하다.
- float 요소가 정확히 inline-block으로 변경된다고 단정할 수 없다.
- blockification에 의해 독립적인 박스처럼 동작할 수 있다.
- 부모 너비가 부족하면 뒤의 float 요소가 아래쪽으로 내려간다.
- `clear: both`는 clear가 적용된 요소를 앞선 양쪽 float 아래에서 시작하게 한다.
- clear는 float 요소 자체를 제거하거나 초기화하지 않는다.
- 원본의 빈 clear div는 학습에는 쉽지만 의미 없는 HTML을 추가한다.
- float 자식만 있는 부모는 자식 높이를 포함하지 못할 수 있다.
- 원본 clearfix는 `::after` 가상 요소에 `clear: both`를 적용한다.
- `display: flow-root`는 clearfix의 현대적인 대안이다.
- `overflow: hidden`도 float를 감쌀 수 있지만 콘텐츠와 포커스를 자를 수 있다.
- 원본 헤더는 좌우 메뉴를 float하고 로고를 inline-block으로 가운데 정렬한다.
- `text-align: center`는 부모 안의 inline-block 로고를 가운데 정렬한다.
- 실제 헤더 레이아웃은 Grid의 `1fr auto 1fr` 구조가 더 안정적일 수 있다.
- 내 코드는 float 설명이 풍부하지만 “새로운 층”, “inline-block 변경”, “초기화” 표현을 수정해야 한다.
- 내 코드의 `감싸사`는 오타다.
- 내 코드의 `.coup div`는 현재 HTML에서 사용되지 않는다.
- 강사님 코드는 `border-color`만 바꿔 중복이 적고 헤더 영역 이름이 더 구체적이다.
- 두 원본 모두 이미지의 `alt`가 없고 외부 이미지 URL을 사용한다.
- float는 새 레이아웃의 기본 도구라기보다 기사형 텍스트 감싸기와 레거시 코드 이해에 중요하다.
