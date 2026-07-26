---
title: JavaScript 반복문
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 반복문

## 개념

반복문은 같은 코드를 조건이나 횟수에 따라 여러 번 실행한다.

## 문법

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}

let n = 0;
while (n < 5) {
    n++;
}
```

## 예제

```javascript
for (let i = 1; i <= 5; i++) {
    console.log("*".repeat(i));
}
```

## 실무 예제

배열의 항목 출력, 구구단, 피라미드 문제처럼 반복 규칙이 있는 작업에 사용한다.

## 주의사항

종료 조건과 증감식을 확인해 무한 반복을 방지한다.

## 면접 포인트

for와 while을 언제 선택하는지 설명한다.

## 요약

횟수가 분명하면 for, 조건 중심이면 while을 고려한다.
