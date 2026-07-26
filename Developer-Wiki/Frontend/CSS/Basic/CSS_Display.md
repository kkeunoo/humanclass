---
title: CSS Display
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS Display


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
