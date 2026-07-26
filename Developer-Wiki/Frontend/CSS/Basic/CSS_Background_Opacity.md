---
title: CSS 배경과 투명도
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS 배경과 투명도


```css
.hero {
  background-color: #eef4ff;
  background-image: url('../img/hero.png');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
```

## background-size

- `cover`: 영역을 가득 채운다. 이미지 일부가 잘릴 수 있다.
- `contain`: 이미지 전체가 보인다. 빈 공간이 생길 수 있다.

## opacity

```css
.disabled-card { opacity: 0.5; }
```

opacity는 요소와 자식 전체에 적용된다. 배경만 투명하게 하려면 rgba 색상을 사용한다.

```css
.overlay { background: rgba(0, 0, 0, 0.45); }
```

## 주의사항

`opacity:0`인 요소는 보이지 않아도 공간을 차지하고 클릭 대상이 될 수 있다.
