---
title: JavaScript DOM 요소 선택
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript DOM 요소 선택

## 개념

DOM은 HTML 문서를 객체로 다루는 구조이며 JavaScript는 선택한 요소를 읽고 변경한다.

## 문법

```javascript
const title = document.querySelector("h1");
const items = document.querySelectorAll(".item");
const box = document.getElementById("box");
```

## 예제

```javascript
items.forEach(function (item) {
    console.log(item);
});
```

## 실무 예제

버튼, 입력창, 메뉴, 모달처럼 조작할 대상을 선택한다.

## 주의사항

querySelector는 첫 요소 또는 null, querySelectorAll은 NodeList를 반환한다. 여러 요소에 classList를 바로 사용할 수 없다.

## 면접 포인트

querySelector와 querySelectorAll의 반환값 차이를 설명한다.

## 요약

DOM 조작은 올바른 요소 선택에서 시작한다.
