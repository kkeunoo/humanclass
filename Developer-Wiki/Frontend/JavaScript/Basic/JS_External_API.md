---
title: JavaScript 지도와 외부 API
category: JavaScript
last_updated: 2026-07-27
status: Active
---

# JavaScript 지도와 외부 API


강사 Workspace에서 지도, Gemini, Discord 연동 실습이 확인되어 수업 범위에 포함한다.

## 공통 흐름

1. 서비스에서 키 또는 토큰 발급
2. 문서에 따라 요청 주소와 매개변수 구성
3. 비동기 요청
4. 응답 JSON 확인
5. 필요한 데이터만 DOM에 출력

## 지도 예제 흐름

```js
const position = { lat: 37.5665, lng: 126.9780 };
// 지도 객체 생성 후 position을 중심 좌표로 사용
```

## 보안 주의사항

- 실제 API 키, 봇 토큰, 웹훅 주소는 Git에 커밋하지 않는다.
- 예제에는 `YOUR_API_KEY` 같은 자리표시자를 사용한다.
- 오류 응답을 화면에 그대로 노출하지 않는다.
