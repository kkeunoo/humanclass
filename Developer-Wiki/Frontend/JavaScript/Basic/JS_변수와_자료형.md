---
title: JavaScript 변수와 자료형
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 변수와 자료형

## 개념

변수는 값을 저장하는 이름이며 문자열, 숫자, 불리언, undefined, null 등 여러 자료형을 담을 수 있다.

## 문법

```javascript
let score = 80;
const name = "Kim";
let passed = true;
```

## 예제

```javascript
console.log(typeof score);
console.log(typeof name);
```

## 실무 예제

입력값, 계산 결과, DOM 요소를 의미 있는 변수명으로 저장한다.

## 주의사항

재할당이 필요 없으면 const를 우선 사용한다. 문자열과 숫자를 더할 때 자동 형 변환을 주의한다.

## 면접 포인트

let과 const의 차이, undefined와 null의 의미를 설명한다.

## 요약

변수는 값을 저장하고 자료형은 값의 종류를 나타낸다.
