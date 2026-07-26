---
title: CSS Float와 Shadow
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS Float와 Shadow

## 개념

float는 요소를 좌우로 띄워 주변 콘텐츠가 감싸게 하고, shadow는 글자나 박스에 그림자를 준다.

## 문법

```css
.photo { float: left; margin-right: 16px; }
.clear { clear: both; }
.card { box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
```

## 예제

```css
.title { text-shadow: 1px 1px 2px #999; }
```

## 실무 예제

이미지 옆에 본문을 흐르게 하거나 카드에 약한 그림자를 적용한다.

## 주의사항

일반 레이아웃은 Flexbox를 우선 고려한다. 그림자를 과하게 사용하면 가독성이 떨어진다.

## 면접 포인트

float 해제 방법과 box-shadow 구성값을 설명한다.

## 요약

float는 감싸기, shadow는 깊이 표현에 사용한다.
