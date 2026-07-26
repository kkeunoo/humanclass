---
title: CSS 미디어 쿼리
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS 미디어 쿼리

## 개념

화면 너비 같은 조건에 따라 CSS를 덮어써 반응형 화면을 만든다.

## 문법

```css
@media screen and (max-width: 768px) {
    .container { width: 100%; }
}
```

## 예제

```css
.menu { display: flex; }
@media screen and (max-width: 768px) {
    .menu { flex-direction: column; }
}
```

## 실무 예제

데스크톱의 가로 메뉴를 모바일에서 세로 메뉴로 변경한다.

## 주의사항

브레이크포인트를 기기 이름으로 외우기보다 실제 레이아웃이 깨지는 지점을 기준으로 잡는다.

## 면접 포인트

반응형 디자인과 max-width 조건의 동작을 설명한다.

## 요약

미디어 쿼리는 화면 조건에 따라 기존 스타일을 재정의한다.
