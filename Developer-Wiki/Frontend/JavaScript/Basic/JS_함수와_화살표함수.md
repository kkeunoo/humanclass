---
title: JavaScript 함수와 화살표 함수
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 함수와 화살표 함수

## 개념

함수는 반복할 코드를 이름으로 묶고 매개변수와 반환값을 사용할 수 있다.

## 문법

```javascript
function add(a, b) {
    return a + b;
}

const multiply = (a, b) => a * b;
```

## 예제

```javascript
function greet(name) {
    console.log(name + "님 안녕하세요");
}
greet("홍길동");
```

## 실무 예제

계산, 검증, 화면 변경을 함수로 분리해 중복을 줄인다.

## 주의사항

return 이후 코드는 실행되지 않는다. 화살표 함수의 축약 문법은 기본 함수 구조를 이해한 뒤 사용한다.

## 면접 포인트

매개변수와 인수, return의 역할을 설명한다.

## 요약

함수는 입력을 받아 작업하고 결과를 반환할 수 있는 재사용 단위다.
