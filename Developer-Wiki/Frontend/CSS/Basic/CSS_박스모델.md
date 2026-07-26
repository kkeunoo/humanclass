---
title: CSS 박스 모델
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS 박스 모델

## 개념

요소는 content, padding, border, margin 영역으로 구성된다.

## 문법

```css
.box {
    width: 200px;
    padding: 20px;
    border: 1px solid #333;
    margin: 10px;
    box-sizing: border-box;
}
```

## 예제

```css
* { box-sizing: border-box; }
```

## 실무 예제

카드의 내부 여백과 카드 사이 간격을 padding과 margin으로 구분한다.

## 주의사항

기본 `content-box`에서는 padding과 border가 지정 너비 밖에 더해진다. margin 겹침도 확인한다.

## 면접 포인트

박스 모델의 네 영역과 `box-sizing`의 차이를 설명한다.

## 요약

크기 문제는 박스 모델의 각 영역부터 확인한다.
