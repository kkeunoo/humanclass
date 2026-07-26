---
title: CSS 배경과 투명도
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS 배경과 투명도

## 개념

배경 속성은 색상과 이미지를 표현하고 `opacity`는 요소 전체의 투명도를 조절한다.

## 문법

```css
.hero {
    background-image: url("../img/bg.png");
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}
```

## 예제

```css
.overlay { background-color: rgba(0, 0, 0, 0.5); }
```

## 실무 예제

배경 이미지 위에 반투명 레이어를 놓아 텍스트 가독성을 높인다.

## 주의사항

부모에 `opacity`를 주면 자식도 투명해진다. 배경만 투명하게 하려면 알파 색상을 사용한다.

## 면접 포인트

`opacity`와 알파 색상의 차이를 설명한다.

## 요약

배경과 콘텐츠 투명도를 구분해 사용한다.
