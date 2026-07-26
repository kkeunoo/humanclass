---
title: CSS Media Query
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS Media Query


```css
.cards { display: flex; gap: 20px; }

@media (max-width: 768px) {
  .cards { flex-direction: column; }
  .desktop-menu { display: none; }
}
```

## 모바일 대응 원칙

- 고정 너비 대신 `%`, `max-width`를 함께 사용한다.
- 작은 화면에서 가로 배치를 세로로 전환한다.
- 클릭 영역을 너무 작게 만들지 않는다.
- 긴 메뉴는 아코디언이나 모바일 메뉴로 바꾼다.

## 주의사항

미디어 쿼리에서 기존 스타일을 전부 다시 쓰지 말고 달라지는 속성만 덮어쓴다.
