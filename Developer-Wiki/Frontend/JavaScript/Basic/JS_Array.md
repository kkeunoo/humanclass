---
title: "JavaScript 배열"
area: "JavaScript"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "35~55분"
---

# JavaScript 배열

## 학습 목표

- 배열에 여러 값을 저장하고 반복문으로 처리한다.
- 예제의 실행 순서를 설명한다.
- 현재까지 배운 문법으로 문제를 해결한다.

## 왜 배우는가

JavaScript는 값과 화면을 연결하고 사용자 행동에 반응하게 만듭니다. 새로운 문법을 짧게 쓰는 것보다 실행 흐름을 정확히 이해하는 것이 우선입니다.

## 기본 개념

```javascript
const numbers = [10, 20, 30];
numbers.push(40);

for (let number of numbers) {
    console.log(number);
}
```

## 수업 예제

예제를 직접 입력한 뒤 변수값과 실행 순서를 `console.log()`로 확인합니다.

## 수업 문제

### 문제

숫자 배열에서 홀수만 새 배열에 저장하고 결과를 출력하세요.

### 요구사항

- 기본 풀이는 for...of와 if문을 사용합니다.
- 홀수를 저장할 빈 배열을 만듭니다.
- `push()`로 값을 추가합니다.

### 직접 풀어 보기

해설을 열기 전에 입력값, 처리 과정, 출력 결과를 나누어 적고 코드를 작성합니다.

<details>
<summary>해설 보기</summary>

```javascript
const numbers = [1, 2, 3, 4, 5];
const oddNumbers = [];

for (let number of numbers) {
    if (number % 2 !== 0) {
        oddNumbers.push(number);
    }
}

console.log(oddNumbers);
```

### 풀이 설명

현재 문서까지 배운 문법을 중심으로 작성했습니다. 먼저 기본 풀이를 이해한 뒤 더 알아보기의 짧은 문법과 비교합니다.

</details>

## 자주 하는 실수

- 배열의 첫 인덱스를 1로 생각하는 경우
- querySelectorAll 결과와 단일 요소를 같은 방식으로 다루는 경우
- 반복문 안에서 원본 배열을 의도치 않게 변경하는 경우

## 실무 연결

상품 목록, 게시글 목록, 선택된 값처럼 여러 데이터를 순서대로 관리할 때 사용합니다.

## 📌 더 알아보기

### filter()로 작성하기

배열 고차 메서드를 배운 뒤에는 같은 문제를 다음처럼 작성할 수 있습니다.

```javascript
const oddNumbers = numbers.filter(function (number) {
    return number % 2 !== 0;
});
```

## 직접 해보기

- 예제의 값과 조건을 변경하고 결과를 예상한다.
- 중간 변수값을 출력해 실행 흐름을 확인한다.
- 오류가 발생한 줄과 오류 메시지를 읽고 원인을 기록한다.

## Check Point

- [ ] 배열의 인덱스와 length를 사용할 수 있다.
- [ ] push와 pop의 역할을 설명할 수 있다.
- [ ] 반복문으로 배열 전체를 순회할 수 있다.

## 최종 요약

배열에 여러 값을 저장하고 반복문으로 처리한다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 기본 풀이를 해설 없이 작성했다.
- [ ] 더 알아보기 문법과 기본 풀이를 비교했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [JavaScript 문자열](JS_String.md) |
| 다음 학습 | [JavaScript DOM 선택과 변경](JS_DOM.md) |
