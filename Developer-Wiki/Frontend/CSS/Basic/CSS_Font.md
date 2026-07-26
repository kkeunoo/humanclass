---
title: CSS 글꼴과 텍스트
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS 글꼴과 텍스트


```css
body {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #222;
}
.title { font-weight: 700; text-align: center; }
```

## 주요 속성

- `font-family`: 글꼴 후보 순서
- `font-size`: 글자 크기
- `font-weight`: 굵기
- `line-height`: 줄 높이
- `letter-spacing`: 글자 사이 간격
- `text-align`: 인라인 콘텐츠 정렬
- `text-decoration`: 밑줄 등 장식

## 주의사항

- `text-align:center`는 요소 자체가 아니라 내부 인라인 콘텐츠를 정렬한다.
- 지나치게 작은 line-height는 여러 줄 문장의 가독성을 떨어뜨린다.
