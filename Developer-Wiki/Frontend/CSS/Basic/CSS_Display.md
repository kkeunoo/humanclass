---
title: CSS Display
category: CSS
last_updated: 2026-07-27
version: v4.1
status: Active
---

# CSS Display

> [!IMPORTANT]
> **핵심 목표**  
> 이 문서는 수업 범위 안에서 `Display`의 개념, 사용 이유, 기본 문법, 예제, 실수 사례와 복습 질문을 한 번에 학습하도록 구성한다.

| 항목 | 내용 |
|---|---|
| 난이도 | ★★☆☆☆ |
| 예상 학습 시간 | 20~35분 |
| 이전 학습 | `CSS_Box_Model` |
| 다음 학습 | `CSS_Flexbox` |
| 문서 버전 | v4.1 · 2026-07-27 |

---

## 이번 문서에서 배우는 것

- `Display`이 무엇인지 자신의 말로 설명한다.
- 기본 문법을 읽고 실행 결과를 예상한다.
- 예제에서 입력 → 처리 → 출력의 흐름을 찾는다.
- 자주 발생하는 실수를 보고 원인을 설명한다.
- 수업 문제를 스스로 분석한 뒤 풀이와 비교한다.

## 왜 이 내용을 배우는가?

Display은(는) 이후 예제와 문제를 이해하기 위한 기본 도구다. 문법만 외우기보다 어떤 상황에서 필요하고, 코드가 어떤 순서로 동작하는지 이해해야 다른 문제에도 적용할 수 있다.

> [!TIP]
> 문법을 외우기 전에 **무엇을 해결하기 위한 문법인지** 먼저 확인한다. 같은 문법도 목적을 이해하면 다른 예제에서 다시 사용할 수 있다.


<!-- V4.1-QA-START -->
> [!NOTE]
> **💡 WHY — 왜 중요한가?**  
> `display`는 요소가 줄을 차지하는 방식과 자식 배치 방식을 결정한다. block, inline, inline-block, flex의 차이를 알아야 레이아웃 문제를 올바른 도구로 해결할 수 있다.

> [!TIP]
> **⭐ 실무 TIP**  
> 정렬 문제를 임시 margin으로 밀기보다 요소의 display 특성과 부모의 배치 방식을 먼저 확인한다.

> [!IMPORTANT]
> **📌 반드시 기억하기**  
> `display: none`은 요소가 차지하던 공간까지 제거한다.

> [!WARNING]
> **⚠️ 주제별 자주 하는 실수**  
> inline 요소에 width와 height를 적용하고 결과가 나오지 않는 것을 CSS 오류로 오해하기 쉽다.

> [!NOTE]
> **🏫 수업 메모**  
> 예제 코드를 실행한 뒤 값이나 선택자를 하나씩 바꾸고, 결과가 달라지는 이유를 자신의 말로 설명한다. 정답 코드보다 실행 순서와 오류 원인을 설명할 수 있는지가 더 중요하다.
<!-- V4.1-QA-END -->

## 학습 전 생각해 보기

1. 이 개념이 없으면 코드를 어떤 방식으로 작성해야 할까?
2. 현재 예제에서 입력값과 결과값은 무엇일까?
3. 코드 한 줄을 제거하면 어떤 변화가 생길까?

---

# 개념과 수업 예제

`display`는 요소가 한 줄에서 공간을 차지하는 방식과 자식 배치 방식을 결정한다.

## block

```css
.block-box {
  display: block;
  width: 200px;
  height: 60px;
  margin: 10px auto;
  border: 1px solid red;
}
```

- 기본적으로 새 줄에서 시작한다.
- 사용 가능한 가로 영역을 차지한다.
- width, height, 상하좌우 margin과 padding을 적용할 수 있다.
- `div`, `p`, `h1` 등이 대표적이다.

## inline

```css
.inline-box {
  display: inline;
  width: 200px;   /* 기대대로 적용되지 않음 */
  height: 60px;   /* 기대대로 적용되지 않음 */
  margin: 20px 40px; /* 좌우 중심으로 반영 */
  padding: 10px;
}
```

- 문장 흐름 안에서 옆으로 이어진다.
- 콘텐츠 크기만큼 공간을 차지한다.
- width와 height를 직접 지정하기 어렵다.
- `span`, `a` 등이 대표적이다.

## inline-block

```css
.inline-block-box {
  display: inline-block;
  width: 160px;
  height: 80px;
  padding: 16px;
  vertical-align: top;
}
```

- 인라인처럼 같은 줄에 배치된다.
- 블록처럼 width, height, padding, margin을 줄 수 있다.
- 카드, 메뉴 항목처럼 “옆으로 놓되 크기도 제어”할 때 유용하다.

## 한눈에 비교하는 예제

```html
<div class="compare">
  <span class="item block">block</span>
  <span class="item inline">inline</span>
  <span class="item inline-block">inline-block</span>
</div>
```

```css
.item { border: 2px solid tomato; width: 160px; height: 60px; margin: 10px; }
.block { display: block; }
.inline { display: inline; }
.inline-block { display: inline-block; vertical-align: top; }
```

실행하면 block은 혼자 한 줄을 차지하고, inline은 크기 지정이 무시되며, inline-block은 같은 줄에 있으면서 크기가 유지된다.

## display: none

```css
.modal.is-hidden { display: none; }
```

요소를 화면과 레이아웃에서 모두 제거한다. 단순히 투명하게 만드는 `opacity: 0`과 다르다.

## inline-block 사이 공백

HTML 줄바꿈이나 공백이 실제 간격으로 보일 수 있다. 수업 코드처럼 부모에 `font-size: 0`을 주고 자식에서 글자 크기를 복원하는 방법이 있으나, 새 레이아웃에서는 Flexbox가 더 단순할 수 있다.

```css
.parent { font-size: 0; }
.parent > div { display: inline-block; font-size: 16px; vertical-align: top; }
```

## 주의사항

- `margin: 0 auto`는 가로 너비가 있는 block 요소에서 중앙 정렬할 때 주로 사용한다.
- inline 요소 내부에 block 요소를 무리하게 넣지 않는다.
- 숨김이 필요할 때 `display:none`, `visibility:hidden`, `opacity:0`의 차이를 구분한다.
- 자식 정렬이 목적이면 `display:flex`가 더 적합한지 먼저 판단한다.

---

# 수업 문제와 풀이

> [!IMPORTANT]
> 아래 문제는 별도 문제 폴더에 있던 내용을 이 개념 문서로 통합한 것이다. 먼저 문제를 읽고 직접 풀이한 뒤 해설과 비교한다.

개인 Workspace의 display·홈페이지 실습과 강사 Workspace의 CSS 문제 파일을 바탕으로, 결과 코드뿐 아니라 레이아웃을 판단하는 순서를 정리한다.

> [!TIP]
> 문제를 바로 코드로 옮기지 말고 **입력 → 처리 → 출력**을 먼저 한 줄씩 적는다. 그 다음 필요한 변수, 반복 횟수, 조건식을 정하면 코드가 단순해진다.

## CSS 문제를 풀기 전에 확인할 것

1. 해당 요소의 기본 `display` 값은 무엇인가?
2. 너비와 높이를 지정해야 하는가?
3. 가로 배치는 자식의 `inline-block`으로 만들지, 부모의 `flex`로 만들지 정한다.
4. 정렬 기준이 부모인지 자식인지 확인한다.
5. 모바일에서 줄바꿈 또는 세로 배치가 필요한지 확인한다.
6. 위치가 어긋났다고 바로 `position: absolute`를 사용하지 않는다.

---

## 문제 1. 두 박스를 같은 줄에 배치

### 방법 A. `inline-block`

```html
<div class="cards">
  <article class="card">첫 번째 카드</article>
  <article class="card">두 번째 카드</article>
</div>
```

```css
.cards {
  font-size: 0;
}

.card {
  display: inline-block;
  width: 200px;
  padding: 20px;
  box-sizing: border-box;
  font-size: 16px;
  vertical-align: top;
}
```

### 왜 `font-size: 0`을 사용하는가

HTML에서 태그 사이의 줄바꿈과 공백이 inline 요소 사이의 실제 여백으로 표시될 수 있다. 부모의 글자 크기를 0으로 만들고 자식에서 다시 복원하면 이 공백을 제거할 수 있다.

### 왜 `vertical-align: top`이 필요한가

`inline-block`은 기본적으로 글자의 기준선에 맞춰 정렬된다. 카드 높이가 다르면 아래쪽이 어긋나 보일 수 있으므로 위쪽 정렬을 지정한다.

### 방법 B. Flexbox

```css
.cards {
  display: flex;
  align-items: flex-start;
  gap: 20px;
}

.card {
  width: 200px;
  padding: 20px;
  box-sizing: border-box;
}
```

### 두 방법 비교

| 항목 | inline-block | flex |
|---|---|---|
| 배치 기준 | 각 자식 요소 | 부모 컨테이너 |
| 요소 사이 공백 | HTML 공백 영향을 받을 수 있음 | `gap`으로 명확히 지정 |
| 수직 정렬 | `vertical-align` 사용 | `align-items` 사용 |
| 현재 학습 목적 | display 특성 이해 | 실무형 1차원 레이아웃 |

> [!TIP]
> 수업에서 `inline-block`을 배우는 이유는 단지 옛 방식이기 때문이 아니라, inline과 block의 차이를 직접 이해하기 좋기 때문이다. 실무 레이아웃에서는 Flexbox가 더 단순한 경우가 많다.

---

## 문제 2. 고정 너비 박스를 가로 중앙에 배치

```css
.box {
  width: 300px;
  margin: 0 auto;
}
```

### 동작 조건

- 요소가 block 계열이어야 한다.
- 부모보다 작은 명시적 너비가 있어야 남는 공간이 생긴다.
- 왼쪽과 오른쪽 `auto`가 남는 공간을 나누어 가진다.

### 작동하지 않는 예

```css
span {
  margin: 0 auto;
}
```

`span`은 기본 inline 요소라 한 줄 전체 공간을 차지하지 않는다.

### 해결

```css
span {
  display: block;
  width: 300px;
  margin: 0 auto;
}
```

---

## 문제 3. 카드 내부 내용을 세로·가로 중앙 정렬

```css
.card {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 200px;
}
```

### 축을 구분하기

기본 `flex-direction: row`에서:

- `justify-content`는 가로 방향 정렬
- `align-items`는 세로 방향 정렬

`flex-direction: column`으로 바뀌면 두 축의 역할도 시각적으로 바뀐다.

> [!WARNING]
> 자식 요소에 `justify-content`를 적어도 그 요소 자체가 flex 컨테이너가 아니면 효과가 없다. 정렬 속성은 보통 자식들을 배치하는 부모에 지정한다.

---

## 문제 4. 화면이 작아질 때 세로 배치

```css
.product-list {
  display: flex;
  gap: 20px;
}

.product {
  flex: 1;
  min-width: 0;
}

@media (max-width: 768px) {
  .product-list {
    flex-direction: column;
  }
}
```

### 해결 과정

1. 데스크톱에서는 가로 배치한다.
2. 작은 화면에서는 가로 공간이 부족해진다.
3. 미디어 쿼리에서 부모의 방향만 `column`으로 변경한다.
4. 카드별 위치를 absolute로 다시 계산할 필요가 없다.

---

## 문제 5. 이미지 위에 배지 배치

```html
<div class="thumbnail">
  <img src="product.jpg" alt="상품">
  <span class="badge">NEW</span>
</div>
```

```css
.thumbnail {
  position: relative;
}

.thumbnail img {
  display: block;
  width: 100%;
}

.badge {
  position: absolute;
  top: 12px;
  right: 12px;
}
```

### 왜 부모에 `position: relative`를 쓰는가

absolute 요소가 가장 가까운 position 지정 조상을 기준으로 위치하도록 만들기 위해서다. 부모에 좌표를 직접 주지 않아도 기준점 역할을 할 수 있다.

### absolute를 써도 좋은 경우

- 이미지 위 배지
- 닫기 버튼
- 장식 요소
- 입력창 내부 아이콘

### 피해야 하는 경우

페이지 전체의 일반적인 카드와 문단 배치를 absolute로 만들면 내용이 늘어날 때 겹치고 반응형 대응이 어려워진다.

---

## 개인 풀이와 강사 풀이를 비교하는 기준

| 확인 항목 | 개인 풀이에서 배울 점 | 강사 풀이에서 배울 점 |
|---|---|---|
| 과정 | 여러 속성을 바꾸며 결과를 확인한 흔적 | 핵심 속성만 사용한 최소 구조 |
| 예외 | 화면 크기와 텍스트 길이를 추가로 고려 | 수업 목표가 되는 개념에 집중 |
| 개선 | 중복 선언과 임시값을 정리할 필요 | 실제 프로젝트에서는 반응형 조건 보강 필요 |

## CSS 문제를 더 잘 푸는 방법

- 개발자 도구에서 적용된 스타일과 취소된 스타일을 확인한다.
- 요소의 실제 크기를 Box Model 패널에서 확인한다.
- 임시로 `outline: 1px solid`를 넣어 부모와 자식 경계를 본다.
- 한 번에 여러 속성을 바꾸지 말고 하나씩 변경한다.
- 고정 높이는 콘텐츠가 늘어날 때 잘릴 수 있으므로 `min-height`도 고려한다.

```css
/* 디버깅용 */
* {
  outline: 1px solid rgba(255, 0, 0, 0.15);
}
```

> [!IMPORTANT]
> 디버깅용 전체 outline은 원인을 찾은 뒤 제거한다. 실제 배포 스타일에 남기지 않는다.

## 추가 연습

1. 같은 너비의 카드 3개를 Flexbox로 배치한다.
2. 모바일에서 카드가 한 줄씩 표시되게 한다.
3. 카드 제목 길이가 달라도 버튼 위치가 맞도록 만든다.
4. 이미지 비율을 유지하면서 카드 너비에 맞춘다.


---

# 자주 하는 실수

- 예제 코드를 그대로 복사하고 각 줄의 역할을 확인하지 않는 실수
- 입력값과 출력값의 자료형을 확인하지 않는 실수
- 한 번에 많은 코드를 작성해 오류가 발생한 위치를 찾기 어렵게 만드는 실수
- 브라우저 또는 콘솔에서 직접 결과를 확인하지 않는 실수

> [!WARNING]
> 오류가 발생하면 코드를 한꺼번에 바꾸지 않는다. 선택 결과, 변수값, 자료형, 조건식 결과를 `console.log()` 또는 출력문으로 하나씩 확인한다.

# 실무 연결

수업에서 배운 문법은 작은 UI와 데이터 처리의 기본이 된다. 실무 사례를 볼 때도 새로운 기술 이름보다 **현재 코드가 어떤 값을 받고, 어떤 조건으로 처리하고, 무엇을 바꾸는지**에 집중한다.

# 직접 해보기

1. 문서의 첫 번째 예제를 직접 입력해 실행한다.
2. 값 하나를 바꾸고 실행 결과를 예상한 뒤 확인한다.
3. 조건이나 반복 횟수를 변경해 본다.
4. 오류가 발생하도록 일부 코드를 바꾸고 오류 메시지를 읽는다.
5. 예제를 보지 않고 핵심 부분을 다시 작성한다.

# Check Point

- [ ] 이 개념을 한 문장으로 설명할 수 있다.
- [ ] 왜 필요한지 예를 들어 설명할 수 있다.
- [ ] 기본 예제의 실행 순서를 말할 수 있다.
- [ ] 자주 하는 실수 한 가지와 해결 방법을 설명할 수 있다.
- [ ] 예제를 보지 않고 비슷한 코드를 작성할 수 있다.

# 예상 면접 질문

1. Display은(는) 무엇인가요?
2. Display을(를) 사용하는 이유는 무엇인가요?
3. 이 문서의 기본 예제를 말로 설명해 보세요.
4. 학습 중 가장 자주 발생할 수 있는 실수는 무엇인가요?

# 최종 요약

- `Display`의 이름만 외우지 않고 필요한 이유와 동작 순서를 함께 이해한다.
- 작은 예제를 실행하고 값을 바꾸면서 결과를 비교한다.
- 문제를 풀 때 입력 → 처리 → 출력으로 나눈다.
- 오류 메시지와 중간값을 확인하는 습관을 만든다.
- 다음 문서 `CSS_Flexbox`로 넘어가기 전에 Check Point를 확인한다.

# 복습 기록

| 복습 시점 | 완료 | 이해도 메모 |
|---|---|---|
| 학습 당일 | [ ] |  |
| 1일 후 | [ ] |  |
| 7일 후 | [ ] |  |
| 30일 후 | [ ] |  |

## 다음 문서를 보기 전에

아래 질문에 답할 수 있다면 다음 문서로 넘어간다.

1. 이 개념은 어떤 문제를 해결하는가?
2. 기본 문법을 직접 작성할 수 있는가?
3. 가장 흔한 실수는 무엇이며 왜 발생하는가?

➡️ **다음 학습:** `CSS_Flexbox`
