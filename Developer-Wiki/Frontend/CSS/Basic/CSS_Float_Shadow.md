---
title: CSS Float와 Shadow
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS Float와 Shadow


## float

```css
.thumb { float: left; width: 120px; margin-right: 16px; }
.article::after { content: ''; display: block; clear: both; }
```

float는 원래 이미지 주변으로 텍스트를 흐르게 만드는 용도다. 오래된 레이아웃에서 사용되지만 새 정렬은 Flexbox가 더 적합하다.

## shadow

```css
.card { box-shadow: 0 8px 20px rgba(0,0,0,.15); }
.title { text-shadow: 1px 1px 2px rgba(0,0,0,.2); }
```

## 주의사항

그림자를 너무 강하게 사용하면 요소 경계가 무겁고 복잡해 보인다.
