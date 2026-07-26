---
title: JavaScript 문자열
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 문자열

## 개념

문자열은 문자의 순서이며 길이 확인, 검색, 분리, 치환, 공백 제거 메서드를 사용할 수 있다.

## 문법

```javascript
const text = " JavaScript ";
console.log(text.length);
console.log(text.trim());
console.log(text.indexOf("Script"));
console.log(text.split("a"));
```

## 예제

```javascript
const email = "user@example.com";
const parts = email.split("@");
```

## 실무 예제

사용자 입력의 앞뒤 공백을 제거하고 필요한 부분을 잘라 화면에 출력한다.

## 주의사항

문자열 메서드는 대부분 원본을 직접 바꾸지 않고 새 값을 반환한다.

## 면접 포인트

length, indexOf, substring, split, replace, trim의 용도를 설명한다.

## 요약

문자열 메서드는 입력값과 출력 문장을 가공할 때 사용한다.
