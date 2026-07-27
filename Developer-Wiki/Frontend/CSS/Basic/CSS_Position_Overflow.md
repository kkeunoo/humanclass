---
title: "CSS Position과 Overflow"
area: "CSS"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★☆☆☆"
estimated_time: "30~50분"
---

# CSS Position과 Overflow

## 학습 목표

- position 기준을 이해하고 넘치는 콘텐츠를 제어한다.
- 개발자 도구에서 최종 적용된 스타일을 확인한다.
- 해당 속성을 사용하는 이유를 설명한다.

## 왜 배우는가

CSS는 HTML 구조를 읽기 쉽고 사용하기 좋은 화면으로 표현합니다. 이 문서의 속성은 실제 UI의 크기, 간격, 배치와 상태 표현에 직접 사용됩니다.

## 기본 개념

```css
.card { position: relative; }
.badge { position: absolute; top: 12px; right: 12px; }
.scroll-box { max-height: 160px; overflow: auto; }
```

## 수업 예제

예제를 HTML 요소에 적용한 뒤 개발자 도구의 **Styles**와 **Computed**에서 최종 값을 확인합니다.

## 수업 문제

### 문제

카드 오른쪽 위에 배지를 배치하고 긴 설명 영역에는 스크롤을 적용하세요.

### 요구사항

- 배지는 카드 영역을 기준으로 배치합니다.
- 배지는 위와 오른쪽에서 각각 12px 떨어집니다.
- 설명 영역의 최대 높이는 160px입니다.

### 직접 풀어 보기

해설을 열기 전에 선택자와 속성을 직접 작성하고 브라우저 너비 또는 요소 값을 바꾸어 확인합니다.

<details>
<summary>해설 보기</summary>

```css
.card { position: relative; }
.badge { position: absolute; top: 12px; right: 12px; }
.description { max-height: 160px; overflow: auto; }
```

### 풀이 설명

요구사항에 필요한 속성만 사용했습니다. 각 선언을 한 줄씩 제거해 보며 어떤 역할을 하는지 확인합니다.

</details>

## 자주 하는 실수

- 기준 부모에 `position: relative`를 지정하지 않는 경우
- 고정 높이로 인해 콘텐츠가 잘리는 경우
- 모든 요소에 absolute를 사용해 문서 흐름을 무너뜨리는 경우

## 실무 연결

알림 배지, 카드 위 라벨, 고정 헤더, 스크롤 패널 같은 UI에 사용합니다.

## 📌 더 알아보기

`fixed`는 브라우저 화면을 기준으로, `sticky`는 스크롤 위치와 부모 범위를 기준으로 동작합니다.

## 직접 해보기

- 속성값을 하나씩 변경하고 화면 차이를 비교한다.
- 개발자 도구에서 덮어쓴 선언과 최종 계산값을 확인한다.
- 같은 결과를 만들 수 있는 다른 속성이 있는지 기록한다.

## Check Point

- [ ] relative와 absolute의 기준 관계를 설명할 수 있다.
- [ ] top/right/bottom/left를 사용할 수 있다.
- [ ] overflow auto와 hidden의 차이를 설명할 수 있다.

## 최종 요약

position 기준을 이해하고 넘치는 콘텐츠를 제어한다.

## 복습 기록

- [ ] 예제를 직접 작성했다.
- [ ] 문제를 해설 없이 풀었다.
- [ ] 개발자 도구에서 적용 결과를 확인했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [CSS display](CSS_Display.md) |
| 다음 학습 | [CSS Flexbox](CSS_Flexbox.md) |
