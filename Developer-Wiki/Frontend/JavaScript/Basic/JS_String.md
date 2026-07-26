---
title: JavaScript 문자열
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript 문자열


```js
const email = 'student@example.com';
const at = email.indexOf('@');
const id = email.slice(0, at);
```

## 주요 기능

- length: 길이
- indexOf / includes: 검색
- slice / substring: 일부 추출
- replace: 치환
- split: 배열로 분리
- trim: 앞뒤 공백 제거

```js
const date = '2026-07-14 12:43:19';
const [day, time] = date.split(' ');
const month = day.split('-')[1];
const minute = time.split(':')[1];
```

## 주의사항

문자열 인덱스는 0부터 시작한다. 개인정보를 가리는 예제에서는 원본 길이를 유지하는지 확인한다.
