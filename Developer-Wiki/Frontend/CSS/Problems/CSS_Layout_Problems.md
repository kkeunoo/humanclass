---
title: CSS 레이아웃 문제 풀이
category: CSS Problems
last_updated: 2026-07-27
status: Active
---

# CSS 레이아웃 문제 풀이

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
