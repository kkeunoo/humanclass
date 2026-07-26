---
title: JavaScript 변수와 자료형
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript 변수와 자료형


```js
let age = 30;
const course = 'JavaScript';
let isComplete = false;
let selected = null;
```

## let과 const

- `let`: 값이 바뀔 수 있는 변수
- `const`: 다시 대입하지 않을 값

```js
let count = 0;
count += 1;
const maxCount = 10;
```

## 주요 자료형

- string, number, boolean
- undefined, null
- object, array

```js
console.log(typeof 'hello'); // string
console.log(typeof 10);      // number
```

## 형 변환

```js
const input = '42';
const value = Number(input);
console.log(value + 8); // 50
```

## 주의사항

`prompt()`의 결과는 문자열이다. 숫자 계산 전에 `Number()`로 변환하고 `Number.isNaN()`으로 유효성을 확인한다.
