---
title: JavaScript 조건문
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 조건문

## 개념

조건문은 참과 거짓에 따라 실행할 코드를 나눈다.

## 문법

```javascript
if (score >= 60) {
    console.log("합격");
} else {
    console.log("불합격");
}
```

## 예제

```javascript
switch (grade) {
    case "A": console.log("우수"); break;
    default: console.log("확인");
}
```

## 실무 예제

로그인 입력 누락, 점수 판정, 메뉴 선택처럼 상황에 따라 다른 동작을 실행한다.

## 주의사항

조건식의 범위와 순서를 확인한다. switch에서는 필요한 경우 break를 작성한다.

## 면접 포인트

if/else if/else와 switch의 사용 차이를 설명한다.

## 요약

조건문은 상태에 따라 실행 흐름을 분기한다.
