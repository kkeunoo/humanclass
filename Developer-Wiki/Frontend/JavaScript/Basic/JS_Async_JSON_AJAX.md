---
title: JavaScript 비동기 JSON AJAX
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript 비동기 JSON AJAX


## 타이머와 실행 순서

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
console.log('3');
// 1, 3, 2
```

## JSON

```js
const text = '{"name":"kim","age":20}';
const user = JSON.parse(text);
const again = JSON.stringify(user);
```

## AJAX 기본 흐름

```js
fetch('https://example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

## 실무 연결

페이지 전체를 새로고침하지 않고 서버 데이터를 받아 목록을 갱신한다.

## 주의사항

- 네트워크 요청은 즉시 완료되지 않는다.
- 응답 상태와 데이터 구조를 확인한다.
- 외부 API 키를 소스 코드에 그대로 공개하지 않는다.
