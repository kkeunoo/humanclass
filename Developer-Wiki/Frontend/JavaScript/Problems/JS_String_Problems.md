---
title: JavaScript 문자열 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript 문자열 문제 풀이


## 이메일에서 아이디 추출

```js
const email = 'student@example.com';
const id = email.slice(0, email.indexOf('@'));
```

## 날짜 문자열에서 월과 분 추출

```js
const value = '2026-07-14 12:43:19';
const [date, time] = value.split(' ');
const month = date.split('-')[1];
const minute = time.split(':')[1];
```

## 이메일 마스킹

```js
const email = 'developer@example.com';
const [id, domain] = email.split('@');
const visible = id.slice(0, 2);
const masked = visible + '*'.repeat(Math.max(0, id.length - 2));
console.log(`${masked}@${domain}`);
```

### 개인 풀이와 강사 풀이 비교

강사 코드는 slice, indexOf, split 등 학습한 문자열 메서드의 핵심 사용법에 집중했다. 개인 코드는 가려지는 글자 수와 출력 모양을 더 세밀하게 다루었다. 개인 풀이의 확장 방향은 좋지만, id 길이가 2보다 짧은 경우도 고려해야 한다.
