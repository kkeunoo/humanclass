---
title: CSS Position과 Overflow
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# CSS Position과 Overflow

## 개념

position은 요소의 위치 기준을 정하고 overflow는 지정 영역을 넘친 내용을 처리한다.

## 문법

```css
.parent { position: relative; }
.child { position: absolute; top: 0; right: 0; }
.box { overflow: auto; }
```

## 예제

```css
.header { position: fixed; top: 0; left: 0; width: 100%; }
```

## 실무 예제

카드 안 배지를 오른쪽 위에 놓을 때 부모를 relative, 배지를 absolute로 설정한다.

## 주의사항

absolute 요소의 기준이 될 가장 가까운 position 지정 조상을 확인한다. fixed 요소가 콘텐츠를 가리지 않게 여백을 확보한다.

## 면접 포인트

static, relative, absolute, fixed의 차이를 설명한다.

## 요약

위치 기준과 넘침 처리 방식을 함께 확인한다.
