---
title: JavaScript 연산자와 조건문
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript 연산자와 조건문


## 연산자

```js
const total = price * quantity;
const isAdult = age >= 20;
const canEnter = isAdult && hasTicket;
```

## 비교 연산자

가능하면 값과 자료형을 함께 비교하는 `===`, `!==`를 사용한다.

```js
console.log(1 === '1'); // false
console.log(1 == '1');  // true
```

## if

```js
if (score >= 90) {
  console.log('A');
} else if (score >= 80) {
  console.log('B');
} else {
  console.log('C');
}
```

## switch

```js
switch (menu) {
  case 'coffee': console.log('커피'); break;
  case 'tea': console.log('차'); break;
  default: console.log('메뉴 없음');
}
```

## 주의사항

조건 범위는 큰 값부터 검사한다. 입력값 검증 없이 비교하면 빈 문자열이 0처럼 변환되는 등 예상하지 못한 결과가 생길 수 있다.
