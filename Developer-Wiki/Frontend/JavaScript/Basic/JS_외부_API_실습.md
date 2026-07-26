---
title: JavaScript 외부 API 실습
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 외부 API 실습

## 개념

Gemini와 Discord 실습은 입력값을 JSON 요청으로 만들고 외부 서비스의 응답을 처리하는 흐름을 익히기 위한 예제다.

## 문법

```javascript
fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
})
.then(function (response) { return response.json(); })
.then(function (data) { console.log(data); });
```

## 예제

```javascript
result.textContent = data.result;
```

## 실무 예제

사용자 입력 → 요청 데이터 생성 → API 호출 → 응답 확인 → 화면 출력 또는 Webhook 전달 순서로 구현한다.

## 주의사항

API 키, 토큰, Webhook URL을 GitHub에 직접 커밋하지 않는다. 응답 구조는 서비스마다 다르므로 콘솔로 먼저 확인한다.

## 면접 포인트

POST 요청의 headers, body, JSON 변환과 비동기 응답 흐름을 설명한다.

## 요약

외부 API 실습의 핵심은 요청 작성, JSON 변환, 응답 처리, 비밀정보 보호다.
