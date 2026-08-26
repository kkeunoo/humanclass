---
title: CSS 박스 모델
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# CSS 박스 모델

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `03_CSS_박스모델.md` |
| 분류 | `02_CSS` |
| 원본 기준 | `workspace_html/css/03_box.html`, `workspace_html/css/asset/css/03_box.css`, `workspace_teacher/workspace_html/css/03_box.html`, `workspace_teacher/workspace_html/css/asset/css/03_box.css` |
| 핵심 범위 | `width`, `height`, `min-width`, `max-width`, `margin`, `padding`, `border`, `border-radius`, `box-sizing`, 가운데 정렬, 마진 상쇄 |
| 프로젝트 연결 | 카드, 프로필 이미지, 채팅 말풍선, 반응형 컨테이너, 공통 Reset, 레이아웃 디버깅 |

> 이 문서는 내 코드와 강사님 코드의 `03_box.html`, `03_box.css`를 비교해 박스 크기·간격·테두리·가운데 정렬·마진 상쇄의 실제 동작을 정리한다. 원본의 부정확한 주석은 수정하고, `border-box`, `flow-root`, `gap`을 활용한 실무형 간격 설계까지 연결한다.

---

# 학습 목표

- 모든 HTML 요소가 박스로 계산된다는 의미를 설명한다.
- 콘텐츠, 패딩, 테두리, 마진의 위치를 구분한다.
- `width`와 `height`가 기본적으로 어느 영역을 지정하는지 설명한다.
- `margin`과 `padding`의 차이를 구분한다.
- 1개, 2개, 3개, 4개 축약형 값을 올바르게 해석한다.
- `border` 단축 속성과 개별 속성을 작성한다.
- `border-radius`로 원형 이미지와 말풍선을 만든다.
- `%`, `min-width`, `max-width`를 함께 사용한다.
- `margin-inline: auto`로 블록 요소를 가운데 정렬한다.
- `content-box`와 `border-box`의 실제 크기 차이를 계산한다.
- 세로 마진 상쇄가 발생하는 조건을 설명한다.
- 마진 상쇄를 무조건 `overflow: hidden`으로 해결하지 않는다.
- Reset CSS와 `box-sizing` 전역 설정을 작성한다.
- 내 코드와 강사님 코드를 비교하고 원본 설명을 보완한다.
- 개발자 도구에서 박스 모델 계산 결과를 확인한다.

---

# 1. CSS 박스 모델이란?

브라우저는 대부분의 HTML 요소를 사각형 박스로 계산합니다.

박스 모델은 다음 네 영역으로 구성됩니다.

```text
margin
└─ border
   └─ padding
      └─ content
```

HTML:

```html
<div class="card">
  박스 모델
</div>
```

CSS:

```css
.card {
  width: 300px;
  padding: 20px;
  border: 2px solid #333;
  margin: 30px;
}
```

각 영역의 역할:

| 영역 | 설명 |
| --- | --- |
| Content | 텍스트, 이미지 등 실제 콘텐츠 영역 |
| Padding | 콘텐츠와 테두리 사이의 안쪽 여백 |
| Border | 박스의 테두리 |
| Margin | 테두리 바깥쪽의 외부 여백 |

---

# 2. 박스 모델을 그림으로 이해하기

다음 CSS를 사용한다고 가정합니다.

```css
.box {
  width: 200px;
  height: 100px;
  padding: 20px;
  border: 5px solid black;
  margin: 30px;
}
```

기본 `box-sizing: content-box`에서는 `width`와 `height`가 콘텐츠 영역만 지정합니다.

가로 계산:

```text
콘텐츠 너비   200px
왼쪽 패딩      20px
오른쪽 패딩    20px
왼쪽 테두리     5px
오른쪽 테두리   5px
-------------------
실제 테두리 박스 너비 250px
```

마진까지 포함한 배치 공간:

```text
250px + 왼쪽 마진 30px + 오른쪽 마진 30px
= 310px
```

세로 계산도 같은 방식입니다.

---

# 3. `width`와 `height`

원본 코드:

```css
div.first {
  border: 1px solid red;
  width: 150px;
  height: 200px;
}
```

기본값인 `content-box`에서는 `width`와 `height`가 콘텐츠 영역의 크기를 지정합니다.

```text
content width  = 150px
content height = 200px
```

테두리와 패딩을 추가하면 실제 화면에서 차지하는 크기는 더 커질 수 있습니다.

---

# 4. `width`와 블록 요소

`div`는 기본적으로 블록 요소입니다.

`width`를 지정하지 않으면 일반적으로 사용 가능한 가로 공간을 채우도록 늘어납니다.

```css
.block {
  border: 1px solid red;
}
```

`width: auto`가 기본이며, 부모의 콘텐츠 영역 안에서 마진과 테두리 등을 고려해 사용 가능한 너비를 채웁니다.

다음처럼 고정 너비를 지정하면 해당 너비를 사용합니다.

```css
.block {
  width: 300px;
}
```

---

# 5. `height` 사용 시 주의

고정 높이는 콘텐츠가 많아질 때 넘침을 만들 수 있습니다.

```css
.box {
  height: 100px;
}
```

콘텐츠가 100px보다 길면 기본 `overflow: visible` 때문에 박스 밖으로 보일 수 있습니다.

실무에서는 콘텐츠가 늘어날 가능성이 있으면 다음을 검토합니다.

```css
.box {
  min-height: 100px;
}
```

`min-height`는 최소 높이를 보장하면서 콘텐츠가 늘어나면 함께 커질 수 있습니다.

---

# 6. `margin`

`margin`은 테두리 바깥쪽의 외부 여백입니다.

원본 내 코드 주석:

```text
margin은 border의 바깥 영역
```

이는 정확한 핵심 설명입니다.

```css
.second {
  margin-top: 50px;
  margin-right: 40px;
  margin-bottom: 30px;
  margin-left: 20px;
}
```

각 방향을 개별 지정할 수 있습니다.

---

# 7. `margin` 축약형

## 7.1 값 4개

```css
.box {
  margin: 50px 40px 30px 20px;
}
```

순서:

```text
top → right → bottom → left
```

시계 방향입니다.

| 방향 | 값 |
| --- | --- |
| 위 | `50px` |
| 오른쪽 | `40px` |
| 아래 | `30px` |
| 왼쪽 | `20px` |

## 7.2 값 3개

```css
.box {
  margin: 50px 40px 30px;
}
```

```text
top
right / left
bottom
```

## 7.3 값 2개

```css
.box {
  margin: 50px 40px;
}
```

```text
top / bottom
right / left
```

## 7.4 값 1개

```css
.box {
  margin: 30px;
}
```

상하좌우 모두 `30px`입니다.

---

# 8. 원본의 연속된 `margin` 선언

원본에는 다음 선언이 모두 순서대로 작성되어 있습니다.

```css
margin: 50px 40px 30px 20px;
margin: 50px 40px 30px;
margin: 50px 40px;
margin: 30px;
```

같은 중요도와 명시도를 가진 동일 속성이므로 마지막 선언만 최종 적용됩니다.

```css
margin: 30px;
```

앞의 선언들은 축약형 문법을 단계별로 설명하기 위한 학습 코드입니다.

실무 최종 코드에서는 필요한 선언 하나만 남깁니다.

---

# 9. 음수 마진

내 코드에는 다음 실습이 주석으로 남아 있습니다.

```css
/* margin-top: -50px; */
```

마진은 음수를 사용할 수 있습니다.

```css
.card {
  margin-top: -20px;
}
```

요소를 다른 요소 쪽으로 당기는 효과를 낼 수 있습니다.

주의:

- 요소가 겹칠 수 있다.
- 레이아웃 의도를 이해하기 어려워질 수 있다.
- 반응형 화면에서 예상치 못한 문제가 생길 수 있다.
- 배치를 위한 주된 수단으로 남용하지 않는다.

겹침이 명확한 디자인이라면 `position`, `transform`, Grid 등의 대안도 검토합니다.

---

# 10. 논리 속성 `margin-inline`, `margin-block`

확장 학습입니다.

물리 방향 대신 글쓰기 방향을 기준으로 작성할 수 있습니다.

```css
.box {
  margin-inline: auto;
  margin-block: 2rem;
}
```

가로쓰기 한국어 문서에서는 일반적으로:

```text
margin-inline → left / right
margin-block  → top / bottom
```

장점:

- 좌우 언어와 세로 쓰기 대응에 유리
- 의도가 명확함
- `margin: 0 auto`보다 가운데 정렬 목적을 분명하게 표현 가능

---

# 11. `padding`

`padding`은 콘텐츠와 테두리 사이의 안쪽 여백입니다.

```css
.second {
  padding-top: 20px;
  padding-right: 15px;
  padding-bottom: 10px;
  padding-left: 5px;
}
```

원본 내 코드 주석:

```text
테두리 안쪽 영역인 padding도 margin과 같이 시계방향으로 돌아감
```

핵심 방향 규칙은 같습니다.

---

# 12. `padding` 축약형

`margin`과 동일한 축약 규칙을 사용합니다.

```css
.box {
  padding: 20px 15px 10px 5px;
}
```

```text
top right bottom left
```

```css
.box {
  padding: 20px 15px 10px;
}
```

```text
top / right-left / bottom
```

```css
.box {
  padding: 20px 15px;
}
```

```text
top-bottom / right-left
```

```css
.box {
  padding: 20px;
}
```

상하좌우 모두 적용합니다.

---

# 13. `padding`과 배경색

배경은 기본적으로 콘텐츠와 패딩 영역까지 그려집니다.

```css
.box {
  padding: 20px;
  background-color: yellow;
}
```

테두리까지 포함한 배경의 그려지는 범위는 `background-clip` 설정에 따라 달라질 수 있습니다.

기본 배경은 테두리 아래까지 확장될 수 있지만, 테두리 자체가 불투명하면 가려집니다.

`background-clip`은 배경 문서에서 더 자세히 다룰 수 있습니다.

---

# 14. `margin`과 `padding` 비교

| 구분 | `margin` | `padding` |
| --- | --- | --- |
| 위치 | 테두리 바깥 | 콘텐츠와 테두리 사이 |
| 배경색 | 표시되지 않음 | 배경색이 표시됨 |
| 음수 값 | 가능 | 불가 |
| 마진 상쇄 | 일부 세로 마진에서 발생 | 발생하지 않음 |
| 클릭 영역 | 늘리지 않음 | 요소 내부 클릭 영역 증가 |
| 대표 용도 | 요소 사이 간격 | 콘텐츠 내부 여백 |

버튼의 클릭 영역을 키울 때는 마진보다 패딩이 적절합니다.

```css
.button {
  padding: 0.75rem 1rem;
}
```

---

# 15. `border`

테두리는 콘텐츠와 패딩을 감싸는 선입니다.

개별 속성:

```css
.box {
  border-width: 1px;
  border-style: solid;
  border-color: red;
}
```

단축 속성:

```css
.box {
  border: 1px solid red;
}
```

구성:

```text
border-width border-style border-color
```

순서는 비교적 유연하지만 일반적으로 위 순서로 작성합니다.

---

# 16. 방향별 테두리

원본:

```css
border-top-width: 3px;
border-top-style: dotted;
border-top-color: blue;
```

위쪽 테두리만 설정합니다.

```css
border-left: 2px dashed green;
```

왼쪽 테두리를 단축형으로 설정합니다.

각 방향:

- `border-top`
- `border-right`
- `border-bottom`
- `border-left`

실무 예:

```css
.notice {
  border-left: 4px solid #2563eb;
  padding-left: 1rem;
}
```

---

# 17. 원본의 테두리 덮어쓰기

원본의 `.second`에는 다음 순서가 있습니다.

```css
border-top-width: 3px;
border-top-style: dotted;
border-top-color: blue;

border-left: 2px dashed green;

border: 1px solid red;
```

마지막 `border` 단축 속성은 네 방향의 폭, 스타일, 색상을 모두 다시 설정합니다.

따라서 최종적으로는:

```text
모든 방향: 1px solid red
```

앞의 파란 점선 위 테두리와 초록 파선 왼쪽 테두리는 덮어써집니다.

이는 단축 속성이 관련 개별 속성을 초기화할 수 있다는 중요한 예입니다.

---

# 18. 테두리 스타일

대표적인 값:

```css
.solid {
  border-style: solid;
}

.dashed {
  border-style: dashed;
}

.dotted {
  border-style: dotted;
}

.double {
  border-style: double;
}
```

`border-style`을 생략하면 기본값 `none`이므로 폭과 색상만 지정해도 테두리가 보이지 않을 수 있습니다.

```css
/* 보이지 않을 수 있음 */
.box {
  border-width: 1px;
  border-color: red;
}
```

```css
/* 표시됨 */
.box {
  border: 1px solid red;
}
```

---

# 19. `border-radius`

모서리를 둥글게 만듭니다.

```css
.box {
  border-radius: 16px;
}
```

원본:

```css
.second {
  border-radius: 50%;
}
```

`50%`는 각 모서리의 반지름을 박스 크기에 비례해 계산합니다.

요소가 정사각형이면 원처럼 보일 수 있습니다.

하지만 원본 `.second`는 기본 `content-box`이며 다음 값을 포함합니다.

```css
width: 150px;
height: 200px;
padding: 30px;
border: 1px solid red;
```

실제 테두리 박스는 가로와 세로가 다르므로 `border-radius: 50%`는 완전한 원이 아니라 타원형에 가까워집니다.

---

# 20. 원형 프로필 이미지

원본:

```css
.profile img {
  border: 1px solid #000;
  width: 200px;
  height: 200px;
  border-radius: 50%;
}
```

가로와 세로가 같으므로 원형이 됩니다.

다만 이미지 원본 비율이 다르면 찌그러질 수 있습니다.

실무 개선:

```css
.profile img {
  display: block;
  width: 200px;
  aspect-ratio: 1;
  border: 1px solid #000;
  border-radius: 50%;
  object-fit: cover;
}
```

`object-fit: cover`는 박스를 채우면서 이미지 비율을 유지하고 넘치는 부분을 잘라냅니다.

---

# 21. 원본 이미지 접근성 개선

원본 HTML:

```html
<img src="https://...webp">
```

`alt`가 없습니다.

의미 있는 프로필 이미지라면 설명을 제공합니다.

```html
<img
  src="profile.webp"
  alt="홍길동 프로필 사진"
>
```

장식용 이미지라면 빈 대체 텍스트를 사용합니다.

```html
<img src="decoration.webp" alt="">
```

또한 외부 사이트의 긴 이미지 주소는 변경되거나 차단될 수 있으므로 프로젝트 자산으로 관리하는 편이 안정적입니다.

---

# 22. 말풍선 모서리

원본:

```css
.chat.right {
  border-radius: 10px 0 10px 10px;
}
```

네 값의 순서:

```text
top-left
top-right
bottom-right
bottom-left
```

원본 내 코드 주석은 “11시 방향부터 시계방향”이라고 설명했습니다.

방향을 모서리 이름으로 기억하면 더 명확합니다.

```text
왼쪽 위 → 오른쪽 위 → 오른쪽 아래 → 왼쪽 아래
```

오른쪽 위만 `0`이므로 오른쪽 말풍선처럼 보입니다.

---

# 23. 말풍선 개선 예

```css
.chat {
  width: fit-content;
  max-width: min(80%, 24rem);
  padding: 0.5rem 0.75rem;
  border: 1px solid #222;
  background-color: #fee500;
}

.chat--right {
  margin-left: auto;
  border-radius: 0.75rem 0 0.75rem 0.75rem;
}
```

원본은 클래스가 `chat right`이므로 다음 선택자를 사용합니다.

```css
.chat.right {
}
```

실무에서는 상태나 변형을 명확히 하도록 다음 같은 클래스도 사용할 수 있습니다.

```html
<div class="chat chat--right">
```

---

# 24. `%` 너비

원본:

```css
.width {
  border: 1px solid red;
  width: 70%;
}
```

`width: 70%`는 보통 containing block의 콘텐츠 너비를 기준으로 계산됩니다.

부모 콘텐츠 너비가 `1000px`이라면:

```text
1000 × 0.7 = 700px
```

다만 원본에는 다음 제한이 함께 있습니다.

```css
min-width: 400px;
max-width: 600px;
```

최종 너비는 `400px`보다 작아지지 않고 `600px`보다 커지지 않습니다.

---

# 25. `min-width`와 `max-width`

```css
.width {
  width: 70%;
  min-width: 400px;
  max-width: 600px;
}
```

예시 계산:

| 부모 너비 | 70% | 제한 적용 후 |
| --- | --- | --- |
| `400px` | `280px` | `400px` |
| `700px` | `490px` | `490px` |
| `1000px` | `700px` | `600px` |

이 패턴은 유동 크기와 최소·최대 제한을 함께 사용합니다.

---

# 26. 작은 화면에서 `min-width` 주의

원본의 `min-width: 400px`은 모바일 화면이 320px 또는 375px일 때 가로 스크롤을 만들 수 있습니다.

실무에서는 다음처럼 작성할 수 있습니다.

```css
.width {
  width: min(70%, 600px);
  min-width: 0;
}
```

또는 좌우 여백을 포함한 반응형 컨테이너:

```css
.container {
  width: min(100% - 2rem, 600px);
  margin-inline: auto;
}
```

최소 너비가 실제 요구사항이라면 유지하되 작은 화면에서의 동작을 반드시 확인합니다.

---

# 27. `margin: auto` 가운데 정렬

원본:

```css
#auto {
  border: 1px solid red;
  width: 250px;
  margin: 10px auto;
}
```

두 값의 의미:

```text
위아래: 10px
좌우: auto
```

블록 요소의 너비가 사용 가능한 너비보다 작으면 남는 가로 공간을 좌우 자동 마진이 나누어 가지므로 가운데 정렬됩니다.

---

# 28. 원본 설명 보완

내 코드 주석:

```text
margin: auto는 너비가 100%가 아닌 경우에만 가능함
위, 아래는 auto가 먹지 않기 때문에 0 auto로 기재
```

더 정확하게 정리하면:

- 블록 요소의 가로 자동 마진은 사용 가능한 남는 공간이 있을 때 가운데 정렬에 사용할 수 있다.
- 요소가 이미 가로 공간을 모두 채우면 나눌 남는 공간이 없어 가운데 이동 효과가 보이지 않는다.
- 일반 문서 흐름에서 위아래 `auto` 마진은 가로 자동 마진과 같은 방식으로 수직 가운데 정렬을 만들지 않는다.
- Flex와 Grid에서는 세로 방향의 자동 마진도 다른 방식으로 유용하게 작동할 수 있다.

권장 표현:

```css
#auto {
  width: 250px;
  margin-block: 10px;
  margin-inline: auto;
}
```

---

# 29. `width: fit-content`

텍스트 길이만큼 너비를 잡고 가운데 정렬할 수 있습니다.

```css
.badge {
  width: fit-content;
  margin-inline: auto;
}
```

고정 너비 없이 콘텐츠 크기에 맞는 박스를 만들 수 있습니다.

브라우저 지원과 레이아웃 요구에 맞춰 사용합니다.

---

# 30. `box-sizing`

박스의 `width`와 `height`가 어느 영역까지 포함하는지를 결정합니다.

대표 값:

- `content-box`
- `border-box`

기본값은 일반적으로 `content-box`입니다.

---

# 31. `content-box`

```css
.box {
  width: 300px;
  height: 300px;
  padding: 50px;
  border: 1px solid red;
}
```

기본 `content-box`에서는:

```text
가로:
300 + 50 + 50 + 1 + 1
= 402px
```

```text
세로:
300 + 50 + 50 + 1 + 1
= 402px
```

마진은 박스 크기 자체가 아니라 바깥 배치 간격으로 추가됩니다.

원본 `.box`의 첫 번째 요소가 이 상태입니다.

---

# 32. `border-box`

원본:

```css
.box-sizing {
  padding: 50px;
  box-sizing: border-box;
}
```

이 요소는 `.box` 클래스도 함께 가지고 있습니다.

```html
<div class="box box-sizing">
```

따라서 다음 값이 함께 적용됩니다.

```css
width: 300px;
height: 300px;
padding: 50px;
border: 1px solid red;
box-sizing: border-box;
```

`border-box`에서는 지정한 `300px` 안에 콘텐츠, 패딩, 테두리가 포함됩니다.

가로 콘텐츠 영역:

```text
300 - 50 - 50 - 1 - 1
= 198px
```

전체 테두리 박스는 `300px`을 유지합니다.

---

# 33. `content-box`와 `border-box` 비교

| 구분 | `content-box` | `border-box` |
| --- | --- | --- |
| `width` 포함 범위 | 콘텐츠만 | 콘텐츠 + 패딩 + 테두리 |
| 패딩 추가 시 외부 크기 | 커짐 | 지정 너비 유지 |
| 계산 편의 | 복잡할 수 있음 | 실무에서 예측하기 쉬움 |
| 기본값 | 예 | 아니요 |

---

# 34. 전역 `box-sizing`

실무에서 자주 사용하는 초기 설정:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

이렇게 하면 대부분의 요소가 `width`와 `height` 안에 패딩과 테두리를 포함하여 계산됩니다.

장점:

- 반응형 너비 계산이 쉬워진다.
- `width: 100%` 입력 요소에 패딩을 추가해도 부모 밖으로 넘칠 가능성이 줄어든다.
- 컴포넌트 크기를 예측하기 쉽다.

---

# 35. Reset CSS

브라우저는 기본 스타일을 제공합니다.

원본:

```css
body {
  margin: 0;
  padding: 0;
}
```

브라우저의 기본 `body` 마진을 제거하는 실습입니다.

내 코드 주석:

```text
개발자페이지에서 보면 body에 기본값으로 margin이 들어가있음
reset css라고 부르기도 함
```

보완:

- `body { margin: 0; }`는 간단한 초기화의 일부입니다.
- 이것만으로 전체 Reset CSS가 완성되는 것은 아닙니다.
- 브라우저 기본 스타일은 제목, 목록, 버튼, 폼 등에도 존재합니다.

간단한 실무 초기화:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  font-size: 100%;
}

body {
  margin: 0;
}

img,
picture,
video {
  display: block;
  max-width: 100%;
}

button,
input,
textarea,
select {
  font: inherit;
}
```

---

# 36. `body` 높이 `400vh`

원본:

```css
body {
  height: 400vh;
}
```

선택자와 스크롤 실습을 위해 페이지를 화면 높이의 네 배로 만든 것으로 볼 수 있습니다.

실무 페이지에서 콘텐츠 높이를 강제로 `400vh`로 지정하는 경우는 드뭅니다.

주의:

- 불필요한 긴 스크롤 생성
- 빈 영역 발생
- 콘텐츠 크기와 무관한 문서 높이

실습용 선언이라면 주석으로 목적을 명시합니다.

```css
/* 뷰포트 스크롤 확인용 임시 높이 */
body {
  min-height: 400vh;
}
```

최종 프로젝트에서는 제거합니다.

---

# 37. 마진 상쇄란?

영어로는 margin collapsing이라고 합니다.

수직 방향의 일부 블록 마진이 단순히 더해지지 않고 하나의 마진으로 합쳐지는 현상입니다.

원본 주석:

```text
세로 방향으로 붙어있을 때 또는 부모와 첫번째 자식간의
margin이 큰 값 하나만 적용되는 현상
```

핵심 방향은 맞지만 모든 마진이 단순히 “큰 값 하나”가 되는 것은 아닙니다.

양수와 음수 마진의 조합에 따라 계산 규칙이 달라집니다.

---

# 38. 형제 사이의 마진 상쇄

원본:

```css
#div2,
#div3 {
  margin: 30px;
}

#div3 {
  margin: 50px;
}
```

최종값:

```text
#div2 margin: 30px
#div3 margin: 50px
```

두 요소가 일반 블록 흐름에서 세로로 인접하면:

```text
#div2의 margin-bottom: 30px
#div3의 margin-top: 50px
```

둘이 더해져 `80px`이 되는 것이 아니라 보통 큰 양수 마진인 `50px`로 상쇄됩니다.

---

# 39. 부모와 첫 자식의 마진 상쇄

원본 구조:

```html
<div id="div1">
  <div id="div2">
    div2 내용
  </div>
  <div id="div3">
    div3 내용
  </div>
</div>
```

`#div1`에 테두리, 패딩, 인라인 콘텐츠 등이 없고 일반 블록 문맥이면 첫 자식 `#div2`의 위쪽 마진이 부모 바깥과 상쇄될 수 있습니다.

이 때문에 부모 내부 여백을 기대했지만 부모 전체가 아래로 이동한 것처럼 보일 수 있습니다.

---

# 40. 주석과 공백은 상쇄를 막는가?

원본에는 두 요소 사이에 HTML 주석이 있습니다.

```html
<!-- a -->
```

주석은 렌더링되는 인라인 콘텐츠 박스를 만들지 않으므로 일반적으로 마진 상쇄를 막지 않습니다.

원본의 주석 처리된 코드는 다음과 같습니다.

```html
<!-- <span style="font-size: 0px;">a</span> -->
```

실제 인라인 콘텐츠가 삽입되어 라인 박스를 만들면 조건이 달라져 상쇄가 막힐 수 있습니다.

하지만 마진 상쇄를 막기 위해 의미 없는 문자를 삽입하는 방식은 실무 해결책으로 권장하지 않습니다.

---

# 41. 마진 상쇄 계산 규칙

## 41.1 둘 다 양수

큰 값이 적용됩니다.

```text
30px과 50px → 50px
```

## 41.2 하나는 양수, 하나는 음수

가장 큰 양수와 가장 작은 음수의 합으로 볼 수 있습니다.

```text
50px과 -20px → 30px
```

## 41.3 둘 다 음수

절댓값이 더 큰 음수값이 적용됩니다.

```text
-30px과 -50px → -50px
```

입문 단계에서는 양수 형제 마진의 큰 값 하나가 적용되는 사례를 우선 이해합니다.

---

# 42. 마진 상쇄가 발생하지 않는 대표 상황

다음과 같은 경우 마진 상쇄가 발생하지 않거나 조건이 달라집니다.

- 가로 방향 마진
- Flex 컨테이너의 자식
- Grid 컨테이너의 자식
- 절대 위치 요소
- 플로팅 요소
- 부모에 패딩이나 테두리가 있어 부모와 자식 마진이 맞닿지 않는 경우
- 새로운 블록 서식 문맥을 만든 경우
- 인라인 콘텐츠나 높이 조건이 사이에 존재하는 경우

---

# 43. 원본의 해결 방법

원본은 다음 해결 방법을 제시합니다.

1. 마진 사이에 콘텐츠 넣기
2. 부모에 테두리 또는 패딩 넣기
3. 부모에 `overflow: hidden` 지정
4. 주석으로 `margin-top: -1px` 실험

학습상 현상을 확인하는 데 의미가 있습니다.

다만 실무에서는 각각의 부작용을 이해해야 합니다.

---

# 44. `overflow: hidden` 해결의 장단점

원본:

```css
#div1 {
  overflow: hidden;
}
```

이 선언은 새로운 블록 서식 문맥을 만드는 효과가 있어 부모와 자식의 마진 상쇄를 막을 수 있습니다.

하지만 원래 목적은 넘치는 콘텐츠를 숨기는 것입니다.

부작용:

- 그림자 잘림
- 드롭다운 잘림
- 포커스 테두리 잘림
- 내부 콘텐츠가 의도치 않게 숨겨짐

마진 상쇄만 해결하려고 사용할 때는 신중해야 합니다.

---

# 45. `display: flow-root`

마진 상쇄와 float 포함 등을 위해 새로운 블록 서식 문맥을 만들고 싶다면 의도가 명확한 방법입니다.

```css
#div1 {
  display: flow-root;
}
```

장점:

- 넘치는 콘텐츠를 숨기지 않는다.
- “새로운 블록 서식 문맥을 만든다”는 목적이 명확하다.
- `overflow: hidden`의 잘림 부작용을 피할 수 있다.

부모와 첫 자식 마진 문제를 해결하기 위해 실무에서 우선 검토할 수 있습니다.

---

# 46. 패딩으로 내부 간격 표현

부모 내부의 시작 여백이 필요하다면 자식의 위쪽 마진보다 부모 패딩이 더 의미에 맞을 수 있습니다.

```css
.parent {
  padding-top: 30px;
}

.child {
  margin-top: 0;
}
```

내부 여백은 `padding`, 요소 사이 간격은 `margin`이라는 기준을 사용하면 의도가 명확해집니다.

---

# 47. `gap` 사용

Flex 또는 Grid 레이아웃에서는 자식 사이 간격에 `gap`을 사용할 수 있습니다.

```css
.list {
  display: grid;
  gap: 2rem;
}
```

```html
<div class="list">
  <div>항목 1</div>
  <div>항목 2</div>
</div>
```

장점:

- 자식의 마지막 마진 제거가 필요 없다.
- 마진 상쇄가 없다.
- 부모가 간격 규칙을 관리한다.
- 행·열 간격을 명확하게 제어한다.

Flex와 Grid는 이후 문서에서 더 자세히 다룹니다.

---

# 48. `orig` 실습

원본:

```css
.orig {
  border: 1px solid red;
}
```

```html
<div class="orig">
  그냥 div
</div>
```

고정 너비를 지정하지 않은 일반 블록 `div`가 부모의 사용 가능한 너비를 채우는 모습을 확인하기 위한 예제로 볼 수 있습니다.

원본의 `.width`와 비교하면 다음 차이를 볼 수 있습니다.

```text
.orig  → width: auto
.width → width: 70%, min/max 제한
```

---

# 49. 내 코드 분석

내 코드는 강사님 코드에 박스 모델의 의미와 축약형 규칙을 상세히 주석으로 추가했습니다.

## 49.1 장점

- `width`, `height`가 콘텐츠 영역의 크기라는 점을 기록했다.
- `margin`과 `padding`의 위치를 구분했다.
- 축약형 1·2·3·4개 규칙을 모두 정리했다.
- 음수 마진 실험을 주석으로 보존했다.
- `border` 개별 속성과 단축 속성을 비교했다.
- `border-radius`의 모서리 순서를 설명했다.
- `%` 너비에 `min-width`, `max-width`를 함께 사용하는 이유를 기록했다.
- `margin: auto`의 가운데 정렬 조건을 설명했다.
- `content-box`와 `border-box`의 차이를 주석으로 남겼다.
- 브라우저 기본 `body` 마진을 Reset과 연결했다.
- 마진 상쇄의 발생 조건과 해결법을 정리했다.
- 강사님 코드의 텍스트를 복사하면서도 일부 설명을 더 구체화했다.

---

# 50. 내 코드 개선점

## 50.1 `lang="en"`

본문이 한국어이므로 다음이 적절합니다.

```html
<html lang="ko">
```

## 50.2 `alt` 누락

```html
<img src="...">
```

의미에 맞는 대체 텍스트를 추가해야 합니다.

## 50.3 `boder`, `widht`, `magin` 오타

원본 주석에 다음 오타가 있습니다.

```text
boder
widht
magin
```

정확한 표기:

```text
border
width
margin
```

코드 실행에는 영향을 주지 않지만 문서에서는 수정하고 원본 오타였음을 설명해야 합니다.

## 50.4 `border-image` 설명

내 코드 주석:

```text
border-image로 굵기를 크게 한 뒤에 이미지도 넣을 수 있음
```

실제 `border-image`는 이미지 소스를 테두리에 그리는 별도 속성 체계입니다.

단순히 테두리를 굵게 한 뒤 이미지를 넣는 기능으로 이해하면 부족합니다.

```css
.frame {
  border: 20px solid transparent;
  border-image: url("frame.png") 30 round;
}
```

이 단원에서는 실제 코드가 없으므로 개념만 언급하고 상세 내용은 배경·테두리 문서로 넘기는 것이 좋습니다.

## 50.5 `margin: auto` 설명

“너비가 100%가 아닌 경우에만 가능”보다는 “남는 가로 공간이 있을 때 좌우 자동 마진으로 가운데 정렬 효과가 나타난다”가 정확합니다.

## 50.6 `overflow: hidden`을 주로 사용한다는 설명

현상은 해결할 수 있지만 콘텐츠 잘림 부작용이 있습니다.

실무에서는:

```css
display: flow-root;
```

부모 패딩, Flex/Grid의 `gap` 등을 함께 검토합니다.

## 50.7 프로필 이미지 비율

고정 `width`와 `height`만 지정하면 이미지가 찌그러질 수 있습니다.

```css
object-fit: cover;
```

를 추가합니다.

## 50.8 `height: 400vh`

스크롤 실습 목적이 아니라면 제거합니다.

---

# 51. 강사님 코드 분석

강사님 코드는 다음 순서로 박스 모델을 실습합니다.

1. 고정 너비와 높이
2. `margin` 개별 속성
3. `margin` 축약형
4. `padding`
5. `border`
6. `border-radius`
7. 원형 이미지
8. 말풍선
9. 유동 너비와 최소·최대 너비
10. 자동 마진 가운데 정렬
11. `box-sizing`
12. 브라우저 기본 `body` 여백 초기화
13. 마진 상쇄

한 파일에서 박스 모델의 주요 개념을 순서대로 확인하기 좋은 구조입니다.

---

# 52. 강사님 코드 개선점

## 52.1 `lang="en"`

한국어 문서이므로 `lang="ko"`가 적절합니다.

## 52.2 이미지 `alt`

프로필 이미지에 대체 텍스트가 없습니다.

## 52.3 외부 이미지 주소

긴 외부 주소는 실습 중 변경되거나 접근이 차단될 수 있습니다.

프로젝트 로컬 자산을 권장합니다.

## 52.4 반복 선언

```text
margin-top: 50px;
margin-right: 40px;
...
margin: 50px 40px 30px 20px;
margin: 50px 40px 30px;
margin: 50px 40px;
margin: 30px;
```

수업용 문법 비교에는 적절하지만 최종 코드에서는 마지막 값만 적용됩니다.

## 52.5 테두리 개별 설정 덮어쓰기

```text
border-top-...
border-left: ...
border: 1px solid red;
```

마지막 단축 속성이 앞의 개별 설정을 덮습니다.

이 결과를 명시적으로 설명하면 학습 효과가 높아집니다.

## 52.6 `overflow: hidden`

마진 상쇄 해결에는 작동하지만 콘텐츠 잘림 위험이 있습니다.

`display: flow-root`를 함께 소개하는 것이 좋습니다.

## 52.7 `body { padding: 0; }`

브라우저 기본 `body` 패딩은 일반적으로 0이므로 실질적인 변화는 `margin: 0`에서 발생합니다.

초기화 규칙으로 함께 적을 수는 있지만 “브라우저 기본 패딩 제거”라고 단정하지 않습니다.

---

# 53. 내 코드와 강사님 코드 비교

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 설명량 | 각 속성의 영역과 축약 규칙을 상세히 기록 | 핵심 주석 중심 |
| 음수 마진 | 주석으로 실험 보존 | 없음 |
| `border-image` | 주석으로 언급 | 없음 |
| `%` 너비 | 최소·최대 폭 의미 설명 | 코드 중심 |
| 가운데 정렬 | 조건과 이유를 상세 설명 | 간단한 예 |
| `box-sizing` | 포함 영역을 주석으로 설명 | 선언 중심 |
| Reset | 개발자 도구의 기본 마진과 연결 | 코드만 배치 |
| 마진 상쇄 | 발생 조건과 해결법을 자세히 기록 | 요약 설명 |
| 오타 | 주석에 `boder`, `widht`, `magin` 존재 | 상대적으로 적음 |
| HTML 텍스트 | “가로 방향 가운데 알아서 정렬” | “가로 방향 가운데” |
| 학습 성격 | 복습 노트형 | 수업 진행형 |

---

# 54. 원본 통합 개선 예제

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
  <title>CSS 박스 모델</title>
  <link rel="stylesheet" href="asset/css/box-model.css">
</head>
<body>
  <main class="page">
    <h1 class="page__title">CSS 박스 모델</h1>

    <section class="profile-card">
      <img
        class="profile-card__image"
        src="asset/images/profile.webp"
        alt="홍길동 프로필 사진"
      >
      <h2 class="profile-card__name">홍길동</h2>
      <p class="profile-card__description">
        웹 개발을 학습하고 있습니다.
      </p>
    </section>

    <section class="chat-list" aria-label="대화 내용">
      <p class="chat chat--right">자니?</p>
      <p class="chat chat--right">자?</p>
    </section>

    <section class="box-comparison">
      <div class="demo-box demo-box--content">
        content-box
      </div>

      <div class="demo-box demo-box--border">
        border-box
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
  color: #222;
  font-family: sans-serif;
}

.page {
  width: min(100% - 2rem, 48rem);
  margin-inline: auto;
  padding-block: 2rem;
}

.profile-card {
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 1rem;
}

.profile-card__image {
  display: block;
  width: 10rem;
  aspect-ratio: 1;
  margin-inline: auto;
  border-radius: 50%;
  object-fit: cover;
}

.chat-list {
  display: grid;
  gap: 0.5rem;
  margin-block: 2rem;
}

.chat {
  width: fit-content;
  max-width: 80%;
  margin: 0;
  padding: 0.5rem 0.75rem;
  border: 1px solid #333;
  background-color: #fee500;
}

.chat--right {
  margin-left: auto;
  border-radius: 0.75rem 0 0.75rem 0.75rem;
}

.box-comparison {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.demo-box {
  width: 12rem;
  height: 12rem;
  padding: 2rem;
  border: 0.25rem solid #dc2626;
}

.demo-box--content {
  box-sizing: content-box;
}

.demo-box--border {
  box-sizing: border-box;
}
```

---

# 55. 실무 컨테이너 패턴

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

의미:

- 작은 화면: 좌우 `1rem` 여백
- 큰 화면: 최대 `72rem`
- 항상 가운데 정렬

원본의 다음 조합을 더 반응형으로 개선한 패턴입니다.

```css
width: 70%;
min-width: 400px;
max-width: 600px;
margin: 10px auto;
```

---

# 56. 카드 패턴

```css
.card {
  padding: 1.5rem;
  border: 1px solid #d1d5db;
  border-radius: 1rem;
  background-color: white;
}
```

카드 사이 간격은 부모에서 관리합니다.

```css
.card-list {
  display: grid;
  gap: 1rem;
}
```

각 카드에 `margin-bottom`을 반복하는 것보다 마지막 항목 예외 처리가 줄어듭니다.

---

# 57. 박스 그림자와 크기

```css
.card {
  box-shadow: 0 8px 24px rgb(0 0 0 / 12%);
}
```

`box-shadow`는 시각적으로 영역을 확장하지만 일반적인 문서 흐름에서 레이아웃 크기를 늘리지는 않습니다.

다만 주변 요소와 겹쳐 보이거나 `overflow: hidden` 부모에서 잘릴 수 있습니다.

원본의 마진 상쇄 해결을 위해 `overflow: hidden`을 사용할 때 그림자가 잘릴 수 있다는 점과 연결됩니다.

---

# 58. 입력 요소와 `border-box`

```css
.form-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #aaa;
}
```

`content-box`라면 `width: 100%`에 패딩과 테두리가 추가되어 부모보다 넓어질 수 있습니다.

전역 `border-box`를 적용하면 지정 너비 안에 패딩과 테두리가 포함됩니다.

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

---

# 59. `outline`과 `border`

포커스 표시에는 `outline`을 사용할 수 있습니다.

```css
.button:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 3px;
}
```

차이:

| 구분 | `border` | `outline` |
| --- | --- | --- |
| 박스 모델 크기 | 포함됨 | 일반적으로 포함되지 않음 |
| 모서리별 설정 | 가능 | 제한적 |
| 포커스 표시 | 가능하지만 크기 변화 주의 | 자주 사용 |
| 공간 차지 | 함 | 하지 않음 |

포커스 때 테두리 폭을 늘리면 레이아웃이 움직일 수 있습니다.

`outline`은 크기 변화 없이 강조할 수 있습니다.

---

# 60. 개발자 도구 박스 모델 패널

브라우저 개발자 도구에서 요소를 선택하면 Computed 영역에 박스 모델 그림이 표시됩니다.

확인 항목:

- content 너비와 높이
- padding 각 방향
- border 각 방향
- margin 각 방향
- 최종 계산된 `box-sizing`

원본의 두 `.box` 요소를 비교하면 다음을 직접 확인할 수 있습니다.

```text
content-box 요소:
테두리 박스 약 402 × 402px

border-box 요소:
테두리 박스 300 × 300px
```

---

# 61. 크기가 예상보다 클 때 점검 순서

1. `box-sizing`이 무엇인가?
2. `width`에 패딩과 테두리가 추가되고 있는가?
3. 부모가 `%` 너비의 기준인가?
4. `min-width` 또는 `max-width`가 제한하고 있는가?
5. 기본 `body` 마진이 남아 있는가?
6. 이미지가 인라인 요소라 아래쪽 공백을 만들고 있는가?
7. 고정 높이보다 콘텐츠가 많은가?
8. `width: 100vw`로 가로 스크롤이 생기는가?
9. 마진이 상쇄되고 있는가?
10. 개발자 도구의 계산값은 무엇인가?

---

# 62. 간격이 예상과 다를 때 점검 순서

1. `margin`인지 `padding`인지 확인한다.
2. 축약형의 값 순서를 확인한다.
3. 뒤쪽 동일 속성이 앞 선언을 덮었는지 확인한다.
4. 세로 마진 상쇄가 발생하는지 확인한다.
5. 부모와 첫 자식 마진이 맞닿는지 확인한다.
6. Flex/Grid의 `gap`을 사용할 수 있는지 검토한다.
7. 음수 마진이 있는지 확인한다.
8. 브라우저 기본 제목·문단 마진이 남아 있는지 확인한다.
9. 논리 속성과 물리 속성이 동시에 덮어쓰는지 확인한다.
10. Styles 패널에서 취소선 처리된 선언을 확인한다.

---

# 63. 자주 하는 실수

## 63.1 `width`가 최종 너비라고 생각

기본 `content-box`에서는 패딩과 테두리가 추가됩니다.

## 63.2 마진과 패딩 혼동

배경색과 클릭 영역이 필요한 내부 간격은 패딩입니다.

## 63.3 축약형 순서 혼동

4개 값은 위, 오른쪽, 아래, 왼쪽입니다.

## 63.4 단축 속성으로 개별 설정 덮어쓰기

```css
border-left: 4px solid blue;
border: 1px solid red;
```

최종 왼쪽 테두리도 빨간색 1px이 됩니다.

## 63.5 원을 만들면서 가로·세로 크기를 다르게 지정

`border-radius: 50%`만으로 완전한 원이 되지 않습니다.

## 63.6 이미지에 `object-fit` 누락

고정 가로·세로 비율이 원본과 다르면 찌그러집니다.

## 63.7 작은 화면에서 큰 `min-width`

가로 스크롤을 만들 수 있습니다.

## 63.8 `margin: auto`만 작성하고 너비가 꽉 참

남는 가로 공간이 없으면 가운데 이동이 보이지 않습니다.

## 63.9 마진 상쇄를 무조건 합산

세로 인접 마진은 상쇄될 수 있습니다.

## 63.10 `overflow: hidden`을 부작용 없이 사용

그림자, 포커스, 드롭다운이 잘릴 수 있습니다.

---


# 종합실습

## 문제 1. 박스 모델 계산

다음 요소의 테두리 박스 가로 크기를 계산하세요.

```css
.box {
  width: 200px;
  padding: 20px;
  border: 5px solid black;
}
```

`box-sizing`은 기본값입니다.

## 문제 2. 마진 포함 배치 공간

문제 1의 요소에 다음 마진이 추가됐습니다.

```css
margin: 30px;
```

좌우 마진까지 포함한 가로 배치 공간을 계산하세요.

## 문제 3. 축약형 해석

다음 마진의 각 방향 값을 작성하세요.

```css
margin: 10px 20px 30px 40px;
```

## 문제 4. 값 3개 해석

```css
padding: 10px 20px 30px;
```

각 방향의 값을 작성하세요.

## 문제 5. 값 2개 해석

```css
margin: 12px 24px;
```

각 방향의 값을 작성하세요.

## 문제 6. 최종 마진

다음 코드의 최종 마진을 작성하세요.

```css
.box {
  margin-top: 50px;
  margin: 20px 30px;
  margin: 10px;
}
```

## 문제 7. 테두리 덮어쓰기

다음 코드의 최종 왼쪽 테두리를 작성하세요.

```css
.box {
  border-left: 4px dashed green;
  border: 1px solid red;
}
```

## 문제 8. 원형 이미지

가로·세로 `160px`의 원형 프로필 이미지를 작성하세요.

조건:

- 검은색 1px 테두리
- 원형
- 원본 비율 유지
- 넘치는 부분 잘라내기

## 문제 9. 말풍선

오른쪽 위 모서리만 각지게 하고 나머지는 `12px` 둥근 말풍선을 작성하세요.

## 문제 10. 최소·최대 너비

`.panel`이 부모 너비의 `70%`를 사용하되 최소 `320px`, 최대 `640px`이 되도록 작성하세요.

## 문제 11. 반응형 개선

문제 10의 `min-width: 320px`이 매우 작은 화면에서 가로 스크롤을 만들지 않도록 개선하세요.

최대 너비 `640px`, 좌우 최소 여백 `1rem`, 가운데 정렬 조건을 사용하세요.

## 문제 12. 가운데 정렬

너비 `300px`인 블록 요소를 가로 가운데 정렬하고 위아래 마진을 `20px`로 지정하세요.

## 문제 13. `content-box` 계산

다음 박스의 실제 테두리 박스 크기를 계산하세요.

```css
.box {
  width: 300px;
  height: 200px;
  padding: 25px;
  border: 2px solid black;
}
```

## 문제 14. `border-box` 계산

문제 13에 `box-sizing: border-box`를 추가했습니다.

1. 최종 테두리 박스 크기
2. 콘텐츠 영역의 가로와 세로 크기

를 계산하세요.

## 문제 15. 전역 설정

모든 요소와 `::before`, `::after`에 `border-box`를 적용하세요.

## 문제 16. Reset

브라우저 기본 `body` 마진을 제거하세요.

## 문제 17. 형제 마진 상쇄

첫 번째 블록의 아래 마진이 `30px`, 두 번째 블록의 위 마진이 `50px`입니다.

둘 다 양수이고 일반 블록 흐름에서 맞닿아 있을 때 실제 간격은 얼마인가요?

## 문제 18. 부모와 자식 마진

부모와 첫 자식의 위쪽 마진 상쇄를 막되 넘치는 콘텐츠를 숨기지 않는 방법을 작성하세요.

## 문제 19. 의미 있는 간격

다음 목록의 각 항목 사이를 `1rem` 띄우고 마지막 항목 예외 규칙을 만들지 않도록 작성하세요.

```html
<div class="card-list">
  <article>카드 1</article>
  <article>카드 2</article>
  <article>카드 3</article>
</div>
```

## 문제 20. 원본 오류 개선

다음 원본 코드를 접근성과 이미지 비율을 고려해 개선하세요.

```html
<div class="profile">
  <img src="https://example.com/profile.webp">
</div>
```

```css
.profile img {
  width: 200px;
  height: 200px;
  border-radius: 50%;
}
```

## 문제 21. 오버플로 디버깅

다음 입력 요소가 부모보다 넓어질 수 있는 이유와 해결 방법을 작성하세요.

```css
input {
  width: 100%;
  padding: 20px;
  border: 2px solid black;
}
```

## 문제 22. 종합 카드

다음 요구사항의 프로필 카드를 작성하세요.

- 최대 너비 `24rem`
- 작은 화면에서 좌우 `1rem` 여백
- 가운데 정렬
- 내부 여백 `1.5rem`
- 테두리와 둥근 모서리
- 원형 프로필 이미지
- 이미지 크기 `8rem`
- 이미지 비율 유지
- 제목과 설명 간격
- 전역 `border-box`
- 접근 가능한 이미지 대체 텍스트

---

# 정답과 해설

## 정답 1

```text
200 + 20 + 20 + 5 + 5
= 250px
```

기본 `content-box`이므로 패딩과 테두리가 추가됩니다.

## 정답 2

```text
테두리 박스 250px
+ 왼쪽 마진 30px
+ 오른쪽 마진 30px
= 310px
```

## 정답 3

```text
top: 10px
right: 20px
bottom: 30px
left: 40px
```

## 정답 4

```text
top: 10px
right: 20px
bottom: 30px
left: 20px
```

## 정답 5

```text
top: 12px
right: 24px
bottom: 12px
left: 24px
```

## 정답 6

마지막 선언이 모든 방향을 덮습니다.

```text
top: 10px
right: 10px
bottom: 10px
left: 10px
```

## 정답 7

```text
1px solid red
```

`border` 단축 속성이 이전 `border-left` 관련 값을 덮습니다.

## 정답 8

```css
.profile-image {
  display: block;
  width: 160px;
  aspect-ratio: 1;
  border: 1px solid #000;
  border-radius: 50%;
  object-fit: cover;
}
```

## 정답 9

```css
.chat--right {
  padding: 0.5rem 0.75rem;
  border: 1px solid #222;
  border-radius: 12px 0 12px 12px;
  background-color: #fee500;
}
```

순서는 왼쪽 위, 오른쪽 위, 오른쪽 아래, 왼쪽 아래입니다.

## 정답 10

```css
.panel {
  width: 70%;
  min-width: 320px;
  max-width: 640px;
}
```

## 정답 11

```css
.panel {
  width: min(100% - 2rem, 640px);
  margin-inline: auto;
}
```

작은 화면에서도 좌우 `1rem` 여백을 남기고 가로 스크롤 위험을 줄입니다.

## 정답 12

```css
.box {
  width: 300px;
  margin: 20px auto;
}
```

논리 속성:

```css
.box {
  width: 300px;
  margin-block: 20px;
  margin-inline: auto;
}
```

## 정답 13

가로:

```text
300 + 25 + 25 + 2 + 2
= 354px
```

세로:

```text
200 + 25 + 25 + 2 + 2
= 254px
```

최종 테두리 박스는 `354px × 254px`입니다.

## 정답 14

최종 테두리 박스:

```text
300px × 200px
```

콘텐츠 가로:

```text
300 - 25 - 25 - 2 - 2
= 246px
```

콘텐츠 세로:

```text
200 - 25 - 25 - 2 - 2
= 146px
```

## 정답 15

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

## 정답 16

```css
body {
  margin: 0;
}
```

## 정답 17

정답은 `50px`입니다.

두 양수 수직 마진이 상쇄되면 큰 값이 적용됩니다.

## 정답 18

```css
.parent {
  display: flow-root;
}
```

새로운 블록 서식 문맥을 만들면서 `overflow: hidden`처럼 넘치는 콘텐츠를 자르지 않습니다.

내부 여백 목적이라면 다음도 가능합니다.

```css
.parent {
  padding-top: 1px;
}
```

다만 실제 디자인 간격에 맞는 패딩값을 사용하는 것이 좋습니다.

## 정답 19

```css
.card-list {
  display: grid;
  gap: 1rem;
}
```

부모가 자식 사이 간격을 관리하므로 마지막 항목 예외가 필요 없습니다.

## 정답 20

```html
<div class="profile">
  <img
    class="profile__image"
    src="asset/images/profile.webp"
    alt="홍길동 프로필 사진"
  >
</div>
```

```css
.profile__image {
  display: block;
  width: 200px;
  aspect-ratio: 1;
  border-radius: 50%;
  object-fit: cover;
}
```

의미 있는 이미지라는 가정에서 대체 텍스트를 제공했습니다.

## 정답 21

기본 `content-box`에서는 `width: 100%`에 좌우 패딩과 테두리가 추가되므로 부모보다 넓어질 수 있습니다.

```css
input {
  box-sizing: border-box;
  width: 100%;
  padding: 20px;
  border: 2px solid black;
}
```

전역 설정도 가능합니다.

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

## 정답 22

### HTML

```html
<article class="profile-card">
  <img
    class="profile-card__image"
    src="asset/images/profile.webp"
    alt="홍길동 프로필 사진"
  >

  <h2 class="profile-card__name">
    홍길동
  </h2>

  <p class="profile-card__description">
    사용자 경험을 고민하는 웹 개발자입니다.
  </p>
</article>
```

### CSS

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

.profile-card {
  width: min(100% - 2rem, 24rem);
  margin-inline: auto;
  padding: 1.5rem;
  border: 1px solid #d1d5db;
  border-radius: 1rem;
  background-color: #fff;
}

.profile-card__image {
  display: block;
  width: 8rem;
  aspect-ratio: 1;
  margin-inline: auto;
  border-radius: 50%;
  object-fit: cover;
}

.profile-card__name {
  margin-block: 1rem 0;
  text-align: center;
}

.profile-card__description {
  margin-block: 0.5rem 0;
  color: #6b7280;
  line-height: 1.6;
  text-align: center;
}
```

---

# 최종 체크리스트

## 박스 모델

- [ ] 콘텐츠, 패딩, 테두리, 마진의 위치를 구분했다.
- [ ] `width`와 `height`가 어떤 박스를 기준으로 하는지 확인했다.
- [ ] 패딩과 테두리를 포함한 실제 크기를 계산했다.
- [ ] 고정 높이보다 `min-height`가 적절한지 검토했다.
- [ ] `content-box`와 `border-box`를 구분했다.
- [ ] 전역 `box-sizing` 설정을 적용했다.

## 간격

- [ ] `margin`과 `padding`의 목적을 구분했다.
- [ ] 축약형 1·2·3·4개 순서를 확인했다.
- [ ] 뒤쪽 선언이 앞 선언을 덮지 않는지 확인했다.
- [ ] 음수 마진을 불필요하게 사용하지 않았다.
- [ ] Flex/Grid 자식 간격에는 `gap`을 검토했다.
- [ ] 부모 내부 여백은 패딩으로 표현할 수 있는지 확인했다.

## 테두리와 이미지

- [ ] 단축 속성이 개별 테두리 설정을 덮는지 확인했다.
- [ ] 원형 요소의 가로·세로 비율이 같은지 확인했다.
- [ ] 고정 이미지 박스에 `object-fit`을 적용했다.
- [ ] 의미 있는 이미지에 `alt`를 작성했다.
- [ ] 외부 이미지 주소 의존성을 줄였다.
- [ ] 포커스 표시에는 레이아웃 변화가 적은 `outline`을 검토했다.

## 반응형 크기

- [ ] 큰 `min-width`가 모바일 가로 스크롤을 만들지 않는지 확인했다.
- [ ] `%` 너비의 containing block을 확인했다.
- [ ] 최대 너비와 좌우 여백을 함께 설계했다.
- [ ] 가운데 정렬에 남는 가로 공간이 있는지 확인했다.
- [ ] `width: min(100% - 2rem, ...)` 패턴을 검토했다.

## 마진 상쇄

- [ ] 수직 형제 마진이 상쇄되는지 확인했다.
- [ ] 부모와 첫 자식의 마진이 맞닿는지 확인했다.
- [ ] 의미 없는 콘텐츠로 상쇄를 막지 않았다.
- [ ] `overflow: hidden`의 잘림 부작용을 확인했다.
- [ ] `display: flow-root`, 패딩, `gap`을 대안으로 검토했다.

## 원본 코드 검수

- [ ] `lang="ko"`로 수정했다.
- [ ] 이미지 `alt` 누락을 보완했다.
- [ ] `boder`, `widht`, `magin` 오타를 수정했다.
- [ ] 실습용 `height: 400vh`의 목적을 확인했다.
- [ ] 연속된 축약형 중 최종 적용값을 설명했다.
- [ ] `border` 단축 속성이 앞의 개별 설정을 덮는 점을 설명했다.
- [ ] `margin: auto` 설명을 남는 공간 기준으로 보완했다.
- [ ] Reset CSS를 `body` 초기화 하나로만 정의하지 않았다.

---

# 핵심 요약

- 대부분의 HTML 요소는 콘텐츠, 패딩, 테두리, 마진으로 구성된 박스로 계산된다.
- 기본 `content-box`에서는 `width`와 `height`가 콘텐츠 영역만 지정한다.
- 패딩과 테두리는 기본적으로 지정 너비와 높이 바깥에 추가된다.
- `border-box`에서는 콘텐츠, 패딩, 테두리가 지정 너비와 높이 안에 포함된다.
- 실무에서는 `*`, `::before`, `::after`에 `box-sizing: border-box`를 자주 적용한다.
- `margin`은 외부 간격, `padding`은 내부 간격이다.
- 마진은 음수가 가능하지만 패딩은 음수를 사용할 수 없다.
- 축약형 4개 값은 위, 오른쪽, 아래, 왼쪽 순서다.
- 같은 속성을 여러 번 작성하면 같은 중요도와 명시도에서는 뒤의 선언이 적용된다.
- `border` 단축 속성은 앞에서 지정한 방향별 폭, 스타일, 색상을 덮을 수 있다.
- 정사각형 요소에 `border-radius: 50%`를 적용하면 원형을 만들 수 있다.
- 고정 크기 이미지에는 `object-fit: cover`를 사용해 비율 왜곡을 막을 수 있다.
- `width`, `min-width`, `max-width`를 함께 사용하면 유동 크기의 범위를 제한할 수 있다.
- 큰 `min-width`는 작은 화면에서 가로 스크롤을 만들 수 있다.
- 블록 요소는 남는 가로 공간이 있을 때 좌우 자동 마진으로 가운데 정렬할 수 있다.
- `margin-inline: auto`는 가로 가운데 정렬 의도를 명확하게 표현한다.
- 일부 수직 마진은 더해지지 않고 상쇄된다.
- 두 양수 형제 마진은 일반적으로 더 큰 값 하나로 상쇄된다.
- 부모와 첫 자식의 마진도 조건에 따라 상쇄될 수 있다.
- `overflow: hidden`은 상쇄를 막을 수 있지만 콘텐츠와 그림자를 자를 수 있다.
- `display: flow-root`는 넘침을 숨기지 않고 새로운 블록 서식 문맥을 만드는 대안이다.
- Flex와 Grid의 `gap`은 자식 사이 간격을 부모에서 안정적으로 관리한다.
- 원본의 `body { margin: 0; }`은 간단한 Reset의 일부이며 전체 Reset CSS와 같지는 않다.
- 내 코드는 강사님 코드보다 설명이 풍부하지만 일부 주석 오타와 과도하게 단정한 설명을 수정할 필요가 있다.
# V3 렌더링 추적 카드 — 콘텐츠에서 바깥 크기까지

모든 요소는 content, padding, border, margin 영역으로 계산된다. 기본 content-box는 width가 콘텐츠만 뜻하고 border-box는 padding과 border를 지정 너비 안에 포함한다.

width 200px, 좌우 padding 20px, 좌우 border 5px라면 content-box 바깥 너비는 250px다. DevTools Box Model에서 각 영역을 직접 대조한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/css/03_box.html 및 asset/css/03_box.css`에서 실제 선택자·계산값·화면 차이를 확인한다.
