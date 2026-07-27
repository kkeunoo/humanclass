---
title: "CSS Float와 Shadow"
area: "CSS"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "30~50분"
---

# CSS Float와 Shadow

## 학습 목표

- 이미지 주변의 글 흐름을 만들고 그림자로 깊이감을 표현한다.
- 개발자 도구에서 최종 적용된 스타일을 확인한다.
- 해당 속성을 사용하는 이유를 설명한다.

## 왜 배우는가

CSS는 HTML 구조를 읽기 쉽고 사용하기 좋은 화면으로 표현합니다. 이 문서의 속성은 실제 UI의 크기, 간격, 배치와 상태 표현에 직접 사용됩니다.

## 기본 개념

```css
.article-image { float: left; margin-right: 16px; }
.article::after { content: ""; display: block; clear: both; }
.card { box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12); }
```

## 수업 예제

예제를 HTML 요소에 적용한 뒤 개발자 도구의 **Styles**와 **Computed**에서 최종 값을 확인합니다.

## 수업 문제

### 문제

이미지 오른쪽으로 글이 흐르게 하고 카드에는 부드러운 그림자를 적용하세요.

### 요구사항

- 이미지는 왼쪽으로 배치합니다.
- 이미지와 글 사이 간격은 16px입니다.
- 부모 영역에서 float 영향을 해제합니다.

### 직접 풀어 보기

해설을 열기 전에 선택자와 속성을 직접 작성하고 브라우저 너비 또는 요소 값을 바꾸어 확인합니다.

<details>
<summary>해설 보기</summary>

```css
.article-image { float: left; margin-right: 16px; }
.article::after { content: ""; display: block; clear: both; }
.card { box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12); }
```

### 풀이 설명

요구사항에 필요한 속성만 사용했습니다. 각 선언을 한 줄씩 제거해 보며 어떤 역할을 하는지 확인합니다.

</details>

## 자주 하는 실수

- float 해제를 하지 않아 부모 높이가 사라지는 경우
- 레이아웃 전체를 float로 구현하는 경우
- 너무 진한 그림자를 여러 요소에 반복하는 경우

## 실무 연결

float는 기사 이미지와 텍스트 흐름에, shadow는 카드나 팝업의 층을 구분할 때 사용합니다.

## 📌 더 알아보기

일반적인 레이아웃은 Flexbox나 Grid를 우선 사용하고, float는 텍스트 흐름이 필요한 경우에 사용합니다.

## 직접 해보기

- 속성값을 하나씩 변경하고 화면 차이를 비교한다.
- 개발자 도구에서 덮어쓴 선언과 최종 계산값을 확인한다.
- 같은 결과를 만들 수 있는 다른 속성이 있는지 기록한다.

## Check Point

- [ ] float가 문서 흐름에 미치는 영향을 설명할 수 있다.
- [ ] clear로 float 영향을 해제할 수 있다.
- [ ] box-shadow의 네 가지 기본 값을 읽을 수 있다.

## 최종 요약

이미지 주변의 글 흐름을 만들고 그림자로 깊이감을 표현한다.

## 복습 기록

- [ ] 예제를 직접 작성했다.
- [ ] 문제를 해설 없이 풀었다.
- [ ] 개발자 도구에서 적용 결과를 확인했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [CSS 배경과 투명도](CSS_Background_Opacity.md) |
| 다음 학습 | [CSS Transition과 Transform](CSS_Transition_Transform.md) |
