---
title: JavaScript 타이머와 비동기 기초
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 타이머와 비동기 기초

## 개념

타이머 함수는 코드를 즉시 실행하지 않고 지정 시간 뒤 또는 일정 간격마다 실행한다. 이를 통해 기본적인 비동기 실행 순서를 확인한다.

## 문법

```javascript
const timerId = setTimeout(function () {
    console.log("한 번 실행");
}, 1000);

const intervalId = setInterval(function () {
    console.log("반복 실행");
}, 1000);
```

## 예제

```javascript
console.log("시작");
setTimeout(function () { console.log("나중"); }, 0);
console.log("끝");
```

## 실무 예제

현재 시간을 1초마다 갱신하거나 안내 메시지를 일정 시간 뒤 숨긴다.

## 주의사항

반복 타이머는 필요할 때 clearInterval로 중지한다. 현재 자료의 비동기 범위는 타이머와 콜백 실행 순서까지다.

## 면접 포인트

setTimeout과 setInterval, 동기와 비동기의 출력 순서 차이를 설명한다.

## 요약

타이머는 작업을 예약하며 이후 코드는 먼저 진행될 수 있다.
