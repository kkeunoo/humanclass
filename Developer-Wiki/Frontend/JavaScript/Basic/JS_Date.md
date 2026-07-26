---
title: JavaScript Date
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript Date


```js
const now = new Date();
console.log(now.getFullYear());
console.log(now.getMonth() + 1);
console.log(now.getDate());
```

`getMonth()`는 0부터 시작하므로 사람이 보는 월은 1을 더한다.

```js
const future = new Date();
future.setDate(future.getDate() + 7);
```

## 실무 연결

현재 시간 표시, 마감일 계산, 날짜 비교에 사용한다.

## 주의사항

문자열 날짜 형식과 시간대에 따라 결과가 달라질 수 있다. 수업 단계에서는 Date 객체의 생성과 기본 getter/setter에 집중한다.
