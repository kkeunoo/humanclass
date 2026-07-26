---
title: CSS Flexbox
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS Flexbox


Flexbox는 한 방향으로 자식 요소를 정렬하는 레이아웃 방식이다.

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}
```

## 축 이해

`flex-direction: row`에서는 가로가 주축, 세로가 교차축이다.

- justify-content: 주축 정렬
- align-items: 교차축 정렬
- gap: 항목 사이 간격
- flex-wrap: 줄바꿈 여부

## 자식 크기

```css
.sidebar { flex: 0 0 240px; }
.content { flex: 1; }
```

## 실무 예제

헤더 로고와 메뉴, 카드 목록, 버튼 묶음, 좌우 레이아웃에 활용한다.

## 주의사항

`justify-content`가 기대대로 동작하려면 컨테이너에 남는 공간이 있어야 한다.
