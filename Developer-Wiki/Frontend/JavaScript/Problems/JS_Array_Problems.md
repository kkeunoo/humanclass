---
title: JavaScript 배열 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript 배열 문제 풀이


개인 `06_array.html`에는 홀수 개수, 완주자, 예약, 로또, 숫자야구 등 확장 풀이가 있었고 강사 파일에는 문제 요구사항과 핵심 풀이가 정리되어 있었다.

## 홀수 개수

```js
const numbers = [3, 4, 7, 5, 1, 6];
let count = 0;
const odds = [];
for (const number of numbers) {
  if (number % 2 !== 0) {
    count++;
    odds.push(number);
  }
}
```

### 비교 코멘트

개인 풀이는 홀수의 개수뿐 아니라 실제 홀수 값도 저장해 결과를 확인했다. 디버깅과 결과 설명에 유리한 접근이다.

## 완주하지 못한 참가자

```js
const participants = ['나미','우솝','조로','루피','상디'];
const finishers = ['나미','우솝','루피','상디'];
const missing = participants.find(name => !finishers.includes(name));
```

현재 학습 흐름에서 반복문으로 직접 비교해도 좋다. `find`와 `includes`는 코드를 짧게 만들지만 각 메서드의 반환값을 이해해야 한다.

## 좌석 예약

```js
const seats = Array(10).fill(false);
const seatNumber = 3;
if (seats[seatNumber - 1]) {
  console.log('이미 예약됨');
} else {
  seats[seatNumber - 1] = true;
}
```

## 중복 없는 로또

```js
const lotto = [];
while (lotto.length < 6) {
  const number = Math.floor(Math.random() * 45) + 1;
  if (!lotto.includes(number)) lotto.push(number);
}
lotto.sort((a, b) => a - b);
```

### 주의사항

`sort()`만 사용하면 문자열 순서로 정렬될 수 있으므로 숫자 비교 함수를 전달한다.
