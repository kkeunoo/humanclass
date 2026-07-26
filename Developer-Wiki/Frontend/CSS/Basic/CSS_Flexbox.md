---
title: CSS Flexbox
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS Flexbox

## 개념

Flexbox는 한 방향으로 요소를 정렬하고 간격을 조절하는 레이아웃 방식이다.

## 문법

```css
.container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 16px;
}
```

## 예제

```css
.item { flex: 1; }
```

## 실무 예제

내비게이션, 카드 목록, 가운데 정렬, 모바일 세로 배치에 활용한다.

## 주의사항

주축은 flex-direction에 따라 바뀐다. justify-content와 align-items가 어떤 축을 제어하는지 확인한다.

## 면접 포인트

주축·교차축, container 속성과 item 속성을 설명한다.

## 요약

Flexbox는 한 방향 정렬과 유연한 크기 분배에 적합하다.
