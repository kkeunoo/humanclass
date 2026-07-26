---
title: JavaScript 반복문
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript 반복문


## for

```js
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

## while

```js
let count = 0;
while (count < 3) {
  console.log(count);
  count++;
}
```

## 중첩 반복문

```js
for (let i = 1; i <= 6; i++) {
  for (let j = 1; j <= 6; j++) {
    console.log(i, j);
  }
}
```

## break와 continue

- break: 반복 종료
- continue: 현재 반복만 건너뜀

## 주의사항

while문에서는 조건을 변화시키는 코드가 빠지면 무한 반복이 발생한다.
