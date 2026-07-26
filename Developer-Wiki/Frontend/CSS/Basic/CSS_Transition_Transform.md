---
title: CSS Transition과 Transform
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS Transition과 Transform


```css
.card {
  transition: transform .3s, box-shadow .3s;
}
.card:hover {
  transform: translateY(-6px) scale(1.02);
  box-shadow: 0 12px 24px rgba(0,0,0,.15);
}
```

## transform

- translate: 이동
- scale: 확대/축소
- rotate: 회전
- skew: 기울이기

## transition

변화할 속성, 시간, 속도 형태, 지연 시간을 지정한다.

```css
.button { transition: background-color .2s ease; }
```

## 주의사항

`transition: all`은 의도하지 않은 속성까지 애니메이션될 수 있으므로 필요한 속성을 명시한다.
