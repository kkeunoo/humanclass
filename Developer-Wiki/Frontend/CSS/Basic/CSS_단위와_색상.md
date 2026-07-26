---
title: CSS 단위와 색상
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS 단위와 색상

## 개념

크기는 px, %, em, rem, vw, vh 등으로 표현하고 색상은 이름, 16진수, rgb 계열로 지정한다.

## 문법

```css
.box {
    width: 50%;
    font-size: 1rem;
    color: #333;
    background-color: rgb(240, 240, 240);
}
```

## 예제

```css
.overlay { background-color: rgba(0, 0, 0, 0.4); }
```

## 실무 예제

고정 크기와 상대 크기를 구분해 반응형 화면의 너비와 글자 크기를 지정한다.

## 주의사항

`em`은 기준 요소에 따라 누적될 수 있다. `%`는 어떤 부모 속성을 기준으로 하는지 확인한다.

## 면접 포인트

절대 단위와 상대 단위, `rgb`와 `rgba`의 차이를 설명한다.

## 요약

단위는 기준을, 색상 표기는 값과 투명도를 결정한다.
