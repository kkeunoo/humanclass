---
title: CSS Transition과 Transform
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS Transition과 Transform

## 개념

transition은 상태 변화의 중간 과정을 만들고 transform은 이동·회전·확대·기울임을 적용한다.

## 문법

```css
.card { transition: transform 0.3s; }
.card:hover { transform: translateY(-4px) scale(1.02); }
```

## 예제

```css
.icon:hover { transform: rotate(10deg); }
```

## 실무 예제

카드나 버튼의 hover 반응을 부드럽게 표현한다.

## 주의사항

transition은 변화 전후 속성이 있어야 동작한다. 필요한 속성만 지정한다.

## 면접 포인트

transition과 animation의 차이를 현재 범위에서 간단히 설명하고, transform 함수의 종류를 구분한다.

## 요약

상태 변화는 transition, 시각적 변형은 transform을 사용한다.
