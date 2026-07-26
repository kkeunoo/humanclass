---
title: JavaScript 함수와 화살표 함수
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript 함수와 화살표 함수


```js
function add(a, b) {
  return a + b;
}

const multiply = (a, b) => a * b;
```

## 매개변수와 반환값

함수는 입력을 매개변수로 받고 결과를 return으로 돌려준다.

```js
function formatPrice(price) {
  return `${price.toLocaleString()}원`;
}
```

## 주의사항

- return 이후 코드는 실행되지 않는다.
- 같은 코드를 반복하면 함수로 분리할 수 있는지 검토한다.
- 화살표 함수와 일반 함수의 `this` 동작은 다르지만 현재 수업 범위에서는 콜백의 간결한 표현 중심으로 이해한다.
