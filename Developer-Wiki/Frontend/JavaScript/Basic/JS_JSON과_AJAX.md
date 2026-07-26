---
title: JavaScript JSON과 AJAX
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript JSON과 AJAX

## 개념

JSON은 데이터를 문자열로 주고받는 형식이고 AJAX는 페이지 전체 새로고침 없이 외부 데이터를 요청하는 방식이다.

## 문법

```javascript
const obj = JSON.parse('{"name":"Kim"}');
const text = JSON.stringify(obj);

fetch(url)
    .then(function (response) { return response.json(); })
    .then(function (data) { console.log(data); });
```

## 예제

```javascript
const xhr = new XMLHttpRequest();
xhr.open("GET", url);
xhr.send();
```

## 실무 예제

받은 JSON 데이터를 DOM 목록이나 결과 영역에 출력한다.

## 주의사항

JSON의 문자열과 키는 큰따옴표를 사용한다. 요청 실패 가능성과 응답 구조를 확인한다. 비밀 키를 공개 저장소에 올리지 않는다.

## 면접 포인트

JSON.parse와 stringify, fetch와 XMLHttpRequest의 공통 목적을 설명한다.

## 요약

JSON은 데이터 형식이고 AJAX는 비동기 통신 방식이다.
