---
title: "JavaScript 변수와 자료형"
area: "JavaScript"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★☆☆☆"
estimated_time: "35~55분"
---

# JavaScript 변수와 자료형

## 학습 목표

- 변수에 값을 저장하고 문자열, 숫자, 불리언 자료형을 구분한다.
- 예제의 실행 순서를 설명한다.
- 현재까지 배운 문법으로 문제를 해결한다.

## 왜 배우는가

JavaScript는 값과 화면을 연결하고 사용자 행동에 반응하게 만듭니다. 새로운 문법을 짧게 쓰는 것보다 실행 흐름을 정확히 이해하는 것이 우선입니다.

## 기본 개념

```javascript
let name = '근욱';
let age = 20;
let isStudent = true;

console.log(name, typeof name);
console.log(age, typeof age);
console.log(isStudent, typeof isStudent);
```

## 수업 예제

예제를 직접 입력한 뒤 변수값과 실행 순서를 `console.log()`로 확인합니다.

## 수업 문제

### 문제

이름, 나이, 수강 여부를 변수에 저장하고 값과 자료형을 출력하세요.

### 요구사항

- `let` 또는 `const`를 사용합니다.
- 문자열, 숫자, 불리언을 각각 한 번 이상 사용합니다.
- `typeof`로 각 자료형을 확인합니다.

### 직접 풀어 보기

해설을 열기 전에 입력값, 처리 과정, 출력 결과를 나누어 적고 코드를 작성합니다.

<details>
<summary>해설 보기</summary>

```javascript
const name = '홍길동';
let age = 20;
const isStudent = true;

console.log(name, typeof name);
console.log(age, typeof age);
console.log(isStudent, typeof isStudent);
```

### 풀이 설명

현재 문서까지 배운 문법을 중심으로 작성했습니다. 먼저 기본 풀이를 이해한 뒤 더 알아보기의 짧은 문법과 비교합니다.

</details>

## 자주 하는 실수

- 변수 선언 없이 값을 사용하는 경우
- 숫자를 따옴표로 감싸 문자열로 저장하는 경우
- 변하지 않는 값에도 무조건 let을 사용하는 경우

## 실무 연결

사용자 정보, 상품 가격, 화면 상태처럼 프로그램이 다루는 모든 값은 변수에 저장됩니다.

## 📌 더 알아보기

`null`과 `undefined`는 값이 없음을 표현하지만 의미와 발생 시점이 다릅니다. 기본 자료형을 익힌 뒤 비교합니다.

## 직접 해보기

- 예제의 값과 조건을 변경하고 결과를 예상한다.
- 중간 변수값을 출력해 실행 흐름을 확인한다.
- 오류가 발생한 줄과 오류 메시지를 읽고 원인을 기록한다.

## Check Point

- [ ] let과 const의 차이를 설명할 수 있다.
- [ ] 문자열·숫자·불리언을 구분할 수 있다.
- [ ] typeof로 자료형을 확인할 수 있다.

## 최종 요약

변수에 값을 저장하고 문자열, 숫자, 불리언 자료형을 구분한다.

## 복습 기록

- [ ] 예제를 직접 입력했다.
- [ ] 기본 풀이를 해설 없이 작성했다.
- [ ] 더 알아보기 문법과 기본 풀이를 비교했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [JavaScript README](../README.md) |
| 다음 학습 | [JavaScript 연산자와 조건문](JS_Operator_Condition.md) |
