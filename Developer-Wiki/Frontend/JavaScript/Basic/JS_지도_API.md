---
title: JavaScript 지도 API
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# JavaScript 지도 API

## 개념

지도 실습은 외부 스크립트를 불러와 지도 객체, 중심 좌표, 확대 수준과 마커를 설정하는 과정이다.

## 문법

```javascript
const container = document.querySelector("#map");
const options = {
    center: new kakao.maps.LatLng(37.5, 127.0),
    level: 3
};
const map = new kakao.maps.Map(container, options);
```

## 예제

```javascript
const marker = new kakao.maps.Marker({ position: options.center });
marker.setMap(map);
```

## 실무 예제

장소 목록과 지도 중심 이동, 상세 페이지 연결로 확장할 수 있다.

## 주의사항

API 키와 허용 도메인 설정을 확인한다. 현재 범위에서는 지도 생성과 마커 표시까지만 정리한다.

## 면접 포인트

외부 라이브러리 객체를 DOM 컨테이너에 연결하는 흐름을 설명한다.

## 요약

외부 지도 스크립트 로드 후 컨테이너와 옵션으로 지도를 생성한다.
