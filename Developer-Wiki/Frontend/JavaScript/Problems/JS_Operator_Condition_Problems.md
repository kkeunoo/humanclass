---
title: JavaScript 연산자 조건문 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript 연산자 조건문 문제 풀이


## 문제 출처

개인 `02_op.html`, `03_if.html`과 강사 동일 파일의 `// 문제` 구간을 비교했다.

## 문제: 양수와 음수 판별

### 개인 풀이 특징

개인 코드는 prompt 입력값을 그대로 비교하면서 숫자가 아닌 경우를 마지막 else에서 처리하려 했다. 출력 메시지와 검증 주석이 상세했다.

```js
const input = prompt('숫자를 입력하세요.');
const value = Number(input);

if (input === null || input.trim() === '' || Number.isNaN(value)) {
  console.log('숫자만 입력하세요.');
} else if (value >= 0) {
  console.log('양수입니다.');
} else {
  console.log('음수입니다.');
}
```

### 강사 풀이 특징

강사 코드는 핵심 조건식을 짧게 제시하여 분기 구조를 빠르게 확인하는 데 초점을 두었다.

### 비교 코멘트

개인 풀이의 장점은 예외 상황을 고민한 점이다. 다만 `prompt` 문자열의 자동 형 변환에 의존하면 빈 문자열이 0으로 처리될 수 있으므로 명시적 변환과 검증을 먼저 하는 편이 안전하다.

## 문제: 홀수 짝수

```js
const value = Number(prompt('정수를 입력하세요.'));
if (!Number.isInteger(value)) {
  console.log('정수를 입력하세요.');
} else if (value % 2 === 0) {
  console.log('짝수');
} else {
  console.log('홀수');
}
```

개인 코드의 `!q2_result % 2 == 0`은 연산 우선순위 때문에 읽기 어렵다. `value % 2 !== 0`으로 직접 작성하는 것이 명확하다.

## 문제: 교통수단 선택

```js
if (money >= 7000) console.log('택시타자');
else if (money >= 3000) console.log('버스타자');
else console.log('걸어가자');
```

큰 범위부터 검사하면 `money < 7000`을 반복할 필요가 없다.

## 문제: 35분 후 시간

```js
let hour = 3;
let minute = 51 + 35;
if (minute >= 60) {
  hour += Math.floor(minute / 60);
  minute %= 60;
}
if (hour >= 24) hour %= 24;
```

## 학습 포인트

입력 검증과 핵심 알고리즘을 분리하면 코드가 읽기 쉬워진다.
