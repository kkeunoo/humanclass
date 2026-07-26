---
title: CSS 텍스트와 폰트
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS 텍스트와 폰트

## 개념

글꼴, 크기, 굵기, 정렬, 줄 높이와 장식을 조절한다.

## 문법

```css
.text {
    font-family: Arial, sans-serif;
    font-size: 16px;
    font-weight: 700;
    line-height: 1.6;
    text-align: center;
    text-decoration: none;
}
```

## 예제

```css
.ellipsis { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
```

## 실무 예제

버튼, 제목, 본문에 서로 다른 크기와 굵기를 적용하되 전체 페이지의 기준 글꼴은 공통으로 관리한다.

## 주의사항

웹 폰트가 로드되지 않을 때 사용할 대체 글꼴을 함께 적는다.

## 면접 포인트

font와 text 계열 속성의 역할을 구분한다.

## 요약

가독성을 위해 글자 크기, 행간, 정렬을 함께 조정한다.
