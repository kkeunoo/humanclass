---
title: JavaScript 배열
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 배열

## 개념

배열은 여러 값을 순서대로 저장하며 인덱스는 0부터 시작한다.

## 문법

```javascript
const fruits = ["apple", "banana"];
fruits.push("orange");
console.log(fruits[0]);
```

## 예제

```javascript
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}
```

## 실무 예제

상품명, 메뉴, 점수처럼 같은 종류의 값을 묶어 반복 처리한다.

## 주의사항

마지막 인덱스는 length - 1이다. 원본 배열을 바꾸는 메서드인지 확인한다.

## 면접 포인트

배열과 일반 변수의 차이, push/pop/shift/unshift의 방향을 설명한다.

## 요약

배열은 순서가 있는 여러 값을 저장하고 반복문과 함께 사용한다.
