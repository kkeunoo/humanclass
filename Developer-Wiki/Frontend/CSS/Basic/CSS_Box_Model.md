---
title: CSS 박스 모델
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS 박스 모델


모든 요소는 콘텐츠, padding, border, margin으로 이루어진 사각형 박스로 계산된다.

```css
* { box-sizing: border-box; }
.card {
  width: 300px;
  padding: 20px;
  border: 1px solid #ccc;
  margin: 20px auto;
}
```

## box-sizing 비교

- `content-box`: width는 콘텐츠 너비다. padding과 border가 바깥으로 더해진다.
- `border-box`: width 안에 padding과 border가 포함된다.

## margin과 padding

- margin: 요소 바깥쪽 간격
- padding: 테두리 안쪽 간격

## 실무 예제

```css
.product-card {
  width: 100%;
  max-width: 360px;
  padding: 24px;
  border: 1px solid #ddd;
  border-radius: 12px;
  margin: 0 auto;
}
```

## 주의사항

인라인 요소에는 width와 height가 기대대로 적용되지 않는다. 크기 제어가 필요하면 `inline-block`이나 `block`을 검토한다.
