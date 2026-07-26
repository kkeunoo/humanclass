---
title: CSS Display
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS Display

## 개념

`display`는 요소가 문서 흐름에서 배치되는 방식을 결정한다.

## 문법

```css
.block { display: block; }
.inline { display: inline; }
.inlineBlock { display: inline-block; }
.hidden { display: none; }
```

## 예제

```css
.menu a { display: inline-block; padding: 10px; }
```

## 실무 예제

가로 메뉴에서 링크에 너비와 여백을 주기 위해 `inline-block`을 사용할 수 있다.

## 주의사항

`display: none`은 공간도 제거한다. inline 요소는 width와 height 적용 방식이 다르다.

## 면접 포인트

block, inline, inline-block의 차이를 설명한다.

## 요약

배치 문제는 요소의 display 특성부터 확인한다.
