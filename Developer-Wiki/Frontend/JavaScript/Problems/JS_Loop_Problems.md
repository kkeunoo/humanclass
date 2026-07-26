---
title: JavaScript 반복문 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript 반복문 문제 풀이


## 문제: 5부터 1까지 출력

```js
for (let i = 5; i >= 1; i--) console.log(i);
```

개인과 강사 풀이 모두 반복 시작값, 조건, 감소식을 직접 표현하는 공통 구조다.

## 문제: 1~5 홀짝 표시

```js
for (let i = 1; i <= 5; i++) {
  console.log(i, i % 2 === 0 ? '짝수' : '홀수');
}
```

## 문제: 주사위 두 개의 모든 경우

```js
for (let a = 1; a <= 6; a++) {
  for (let b = 1; b <= 6; b++) {
    console.log([a, b]);
  }
}
```

## 문제: 3이 나올 때까지 주사위

```js
let count = 0;
let dice;
do {
  dice = Math.floor(Math.random() * 6) + 1;
  count++;
} while (dice !== 3);
console.log(`${count}번 만에 3`);
```

### 비교 코멘트

개인 Workspace는 횟수와 게임 흐름을 더 자세히 작성했고, 강사 코드는 반복 조건 중심이었다. 랜덤 문제는 반복 전에 값이 필요한지에 따라 while과 do-while을 구분한다.

## 주의사항

중첩 반복문에서 같은 변수 이름을 재사용하지 않는다.
