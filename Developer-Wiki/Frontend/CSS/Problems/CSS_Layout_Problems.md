---
title: CSS 레이아웃 문제 풀이 정리
category: CSS
last_updated: 2026-07-27
status: Active
---

# CSS 레이아웃 문제 풀이 정리


## 출처 판단

개인 Workspace의 `hp_*`, `0702_*`, display 연습 파일과 강사 Workspace의 display 문제 파일을 비교해 공통 개념을 정리했다. 일부 파일은 이름이 깨져 작성자를 확실히 판별하기 어려워 공통 실습으로 취합했다.

## 문제 1: 두 박스를 같은 줄에 배치

```css
.parent { font-size: 0; }
.box {
  display: inline-block;
  width: 160px;
  padding: 20px;
  font-size: 16px;
  vertical-align: top;
}
```

### 비교 코멘트

수업 코드에서는 inline-block의 공백 문제와 vertical-align을 직접 확인했다. 실무에서는 같은 결과를 Flexbox로 더 단순하게 만들 수 있지만, 현재 학습 범위에서는 두 방식의 차이를 이해하는 것이 중요하다.

```css
.parent { display: flex; align-items: flex-start; gap: 0; }
```

## 문제 2: 중앙 정렬

```css
.box { width: 300px; margin: 0 auto; }
```

`margin:auto`는 block 요소와 명시된 너비가 있을 때 가로 중앙 정렬로 동작한다. inline 요소에는 같은 방식이 적용되지 않는다.

## 문제 3: 화면이 작아질 때 세로 배치

```css
.row { display: flex; gap: 20px; }
@media (max-width: 768px) { .row { flex-direction: column; } }
```

## 주의사항

문제를 풀 때 먼저 요소의 display 종류와 부모 레이아웃을 확인한다. 위치가 어긋났다고 바로 `position:absolute`를 사용하면 반응형에서 더 큰 문제가 생길 수 있다.
