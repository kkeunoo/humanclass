---
title: CSS 선택자와 문법
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS 선택자와 문법

## 개념

CSS는 선택자로 HTML 요소를 찾고 속성과 값으로 모양을 지정한다.

## 문법

```css
선택자 {
    속성: 값;
}
```

## 예제

```css
h1 { color: navy; }
.notice { font-weight: bold; }
#header { height: 80px; }
```

## 실무 예제

공통 디자인은 class로 묶고, 한 요소만 필요한 경우 id를 사용한다.

## 주의사항

선택 범위를 지나치게 넓히지 않는다. 같은 속성이 겹치면 선택자 우선순위와 작성 순서를 확인한다.

## 면접 포인트

태그·class·id 선택자의 차이와 우선순위를 설명한다.

## 요약

선택자와 선언 블록이 CSS의 기본 구조다.
