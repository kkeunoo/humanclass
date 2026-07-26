---
title: JavaScript DOM 생성과 삭제
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript DOM 생성과 삭제

## 개념

새 요소를 만들고 부모에 추가하거나 기존 요소를 제거할 수 있다.

## 문법

```javascript
const li = document.createElement("li");
li.textContent = "새 항목";
list.appendChild(li);
li.remove();
```

## 예제

```javascript
const button = document.createElement("button");
button.textContent = "삭제";
li.appendChild(button);
```

## 실무 예제

입력값으로 Todo 항목을 만들고 삭제 버튼으로 해당 항목을 제거한다.

## 주의사항

요소를 생성한 뒤 내용과 속성을 설정하고 마지막에 부모에 추가한다.

## 면접 포인트

createElement, appendChild, remove의 실행 순서를 설명한다.

## 요약

DOM 생성은 생성 → 설정 → 추가 순서로 진행한다.
