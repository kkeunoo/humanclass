---
title: JavaScript 배열
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript 배열


```js
const fruits = ['apple', 'banana', 'orange'];
console.log(fruits[0]);
fruits.push('grape');
```

## 주요 메서드

```js
fruits.pop();
fruits.includes('apple');
fruits.indexOf('banana');
fruits.splice(1, 1);
```

## 반복

```js
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
```

## 복사 주의

```js
const copy = [...fruits];
```

배열은 참조형이므로 `const copy = fruits`는 같은 배열을 가리킨다.

## 실무 연결

예약 좌석, 참가자 명단, Todo 목록, 선택된 메뉴처럼 여러 값을 순서대로 관리할 때 사용한다.
