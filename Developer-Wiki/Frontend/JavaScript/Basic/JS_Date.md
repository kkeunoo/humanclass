---
title: JavaScript Date
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript Date

## 개념

Date 객체는 날짜와 시간을 생성하고 연도, 월, 일, 요일, 시각을 가져오는 데 사용한다.

## 문법

```javascript
const now = new Date();
console.log(now.getFullYear());
console.log(now.getMonth() + 1);
console.log(now.getDate());
```

## 예제

```javascript
const days = ["일", "월", "화", "수", "목", "금", "토"];
console.log(days[now.getDay()]);
```

## 실무 예제

현재 시계나 D-Day 계산의 기초로 사용한다.

## 주의사항

월은 0부터 시작한다. 현재 시간을 갱신하려면 반복 실행 때마다 새 Date 객체를 생성한다.

## 면접 포인트

getDate와 getDay, 월에 1을 더하는 이유를 설명한다.

## 요약

Date는 날짜·시간 값을 만들고 필요한 단위를 메서드로 가져온다.
