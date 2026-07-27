---
title: JavaScript 배열 문제 풀이
category: JavaScript Problems
last_updated: 2026-07-27
status: Active
---

# JavaScript 배열 문제 풀이

개인 `06_array.html`의 확장 문제와 강사 파일의 기본 문제를 비교해, 배열을 순회하고 검색하며 상태를 관리하는 방법을 정리한다.

> [!TIP]
> 문제를 바로 코드로 옮기지 말고 **입력 → 처리 → 출력**을 먼저 한 줄씩 적는다. 그 다음 필요한 변수, 반복 횟수, 조건식을 정하면 코드가 단순해진다.

## 배열 문제의 기본 흐름

1. 배열에 무엇이 저장되어 있는지 확인한다.
2. 필요한 결과가 개수, 값, 위치, 새 배열 중 무엇인지 결정한다.
3. 모든 요소를 봐야 하는지, 하나를 찾으면 끝내도 되는지 판단한다.
4. 원본 배열을 바꿔도 되는지 확인한다.
5. 빈 배열과 중복값도 테스트한다.

---

## 문제 1. 홀수 개수와 홀수 목록 구하기

### 문제 분석

- 모든 숫자를 확인해야 한다.
- 홀수이면 개수를 1 증가시킨다.
- 확인을 쉽게 하기 위해 홀수 값도 별도 배열에 저장한다.

```js
const numbers = [3, 4, 7, 5, 1, 6];
let count = 0;
const oddNumbers = [];

for (const number of numbers) {
  if (number % 2 !== 0) {
    count++;
    oddNumbers.push(number);
  }
}

console.log('홀수 개수:', count);
console.log('홀수 목록:', oddNumbers);
```

### 개인 풀이와 강사 풀이 비교

- 개인 풀이는 개수뿐 아니라 실제 홀수 목록을 함께 저장하여 결과 검증이 쉽다.
- 강사 풀이는 개수를 구하는 핵심 조건에 집중하여 구조가 간단하다.
- 문제에서 개수만 요구하더라도 학습 중에는 목록까지 확인하면 조건식 오류를 찾기 쉽다.

### 개선된 메서드 풀이

```js
const oddNumbers = numbers.filter(number => number % 2 !== 0);
console.log(oddNumbers.length, oddNumbers);
```

> [!NOTE]
> `filter()`는 현재 수업에서 다뤘을 때만 적극적으로 사용한다. 반복문 풀이를 먼저 이해한 뒤 메서드 풀이를 비교한다.

---

## 문제 2. 완주하지 못한 참가자 찾기

```js
const participants = ['나미', '우솝', '조로', '루피', '상디'];
const finishers = ['나미', '우솝', '루피', '상디'];

let missing = '';

for (const participant of participants) {
  if (!finishers.includes(participant)) {
    missing = participant;
    break;
  }
}

console.log(missing);
```

### 왜 `break`를 사용하는가

문제에서 미완주자가 한 명이라고 보장하면 찾은 뒤 나머지 요소를 볼 필요가 없다.

### 더 짧은 풀이

```js
const missing = participants.find(
  participant => !finishers.includes(participant)
);
```

### 주의사항

동명이인이 존재할 수 있는 문제라면 이름만 비교하는 방식은 정확하지 않다. 실제 서비스에서는 회원 번호 같은 고유값을 사용해야 한다.

---

## 문제 3. 좌석 예약 상태 관리

### 데이터 설계

좌석 10개를 `false`로 초기화하고 예약되면 해당 위치를 `true`로 변경한다.

```js
const seats = Array(10).fill(false);

function reserveSeat(seatNumber) {
  const index = seatNumber - 1;

  if (!Number.isInteger(seatNumber) || index < 0 || index >= seats.length) {
    return '존재하지 않는 좌석입니다.';
  }

  if (seats[index]) {
    return '이미 예약된 좌석입니다.';
  }

  seats[index] = true;
  return `${seatNumber}번 좌석이 예약되었습니다.`;
}

console.log(reserveSeat(3));
console.log(reserveSeat(3));
```

### 해결 과정

1. 사용자에게 보이는 좌석 번호는 1부터 시작한다.
2. 배열 인덱스는 0부터 시작하므로 1을 뺀다.
3. 범위 검사를 먼저 한다.
4. 이미 `true`인지 확인한다.
5. 예약 가능할 때만 값을 변경한다.

> [!WARNING]
> 상태를 변경하기 전에 반드시 유효성 검사를 끝낸다. 잘못된 좌석 번호로 배열 밖에 값을 추가하면 의도하지 않은 속성이 생길 수 있다.

---

## 문제 4. 중복 없는 로또 번호 생성

```js
const lotto = [];

while (lotto.length < 6) {
  const number = Math.floor(Math.random() * 45) + 1;

  if (!lotto.includes(number)) {
    lotto.push(number);
  }
}

lotto.sort((a, b) => a - b);
console.log(lotto);
```

### 단계별 해설

- 배열 길이가 6이 될 때까지 반복한다.
- 1부터 45 사이 숫자를 만든다.
- 이미 포함된 숫자가 아니라면 추가한다.
- 마지막에 오름차순으로 정렬한다.

### 자주 하는 실수

```js
lotto.sort();
```

기본 정렬은 값을 문자열처럼 비교한다. 숫자 정렬에서는 비교 함수를 전달한다.

```js
lotto.sort((a, b) => a - b);
```

---

## 문제 5. 숫자 야구 판정

### 문제를 작은 단계로 나누기

1. 정답 숫자 배열과 입력 숫자 배열을 준비한다.
2. 같은 위치에 같은 숫자가 있으면 스트라이크다.
3. 위치는 다르지만 정답 배열에 숫자가 있으면 볼이다.
4. 둘 다 아니면 아웃이다.

```js
const answer = [3, 7, 1];
const guess = [3, 1, 9];
let strike = 0;
let ball = 0;

for (let i = 0; i < answer.length; i++) {
  if (guess[i] === answer[i]) {
    strike++;
  } else if (answer.includes(guess[i])) {
    ball++;
  }
}

console.log(`${strike}S ${ball}B`);
```

### 개선 포인트

입력값에 중복 숫자가 없는지, 자리 수가 맞는지 먼저 검증하면 게임 로직과 예외 처리를 분리할 수 있다.

## 더 좋은 배열 풀이 습관

- 값이 아니라 인덱스가 필요한 문제인지 먼저 확인한다.
- 원본 변경 메서드와 새 배열 반환 메서드를 구분한다.
- `sort()`는 원본 배열을 변경한다.
- 찾는 대상이 하나면 `find`, 여러 개면 `filter`, 존재 여부만 필요하면 `includes` 또는 `some`을 고려한다.

## 추가 연습

1. 배열에서 최댓값과 최솟값을 반복문으로 구한다.
2. 중복된 값을 제외한 새 배열을 만든다.
3. 학생 점수 배열의 평균과 평균 이상 학생 수를 구한다.
4. 장바구니 배열에서 품절 상품을 제외한 총액을 계산한다.
