---
title: "CSS display"
area: "CSS"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★☆☆☆"
estimated_time: "30~50분"
---

# CSS display

## 학습 목표

- block, inline, inline-block, none의 차이를 이해하고 기본 배치 방식을 변경한다.
- 개발자 도구에서 최종 적용된 스타일을 확인한다.
- 해당 속성을 사용하는 이유를 설명한다.

## 왜 배우는가

CSS는 HTML 구조를 읽기 쉽고 사용하기 좋은 화면으로 표현합니다. 이 문서의 속성은 실제 UI의 크기, 간격, 배치와 상태 표현에 직접 사용됩니다.

## 기본 개념

```css
.link { display: inline-block; }
.hidden { display: none; }
.panel { display: block; }
```

`display`는 요소가 화면에서 차지하는 방식과 주변 요소와의 배치 관계를 결정합니다.

## 수업 예제

예제를 HTML 요소에 적용한 뒤 개발자 도구의 **Styles**와 **Computed**에서 최종 값을 확인합니다.

## 수업 문제

### 문제

두 링크를 가로로 배치하고 각 링크에 너비와 안쪽 여백을 적용하세요.

### 요구사항

- 링크는 줄바꿈 없이 가로로 배치합니다.
- 각 링크에 너비를 지정할 수 있어야 합니다.
- Flexbox는 사용하지 않습니다.

### 직접 풀어 보기

해설을 열기 전에 선택자와 속성을 직접 작성하고 브라우저 너비 또는 요소 값을 바꾸어 확인합니다.

<details>
<summary>해설 보기</summary>

```css
.menu-link {
    display: inline-block;
    width: 120px;
    padding: 12px;
    text-align: center;
}
```

### 풀이 설명

요구사항에 필요한 속성만 사용했습니다. 각 선언을 한 줄씩 제거해 보며 어떤 역할을 하는지 확인합니다.

</details>

## 자주 하는 실수

- 인라인 요소에 width와 height가 그대로 적용될 것으로 기대하는 경우
- 숨김 처리 후 공간이 남는 방식과 사라지는 방식을 혼동하는 경우
- 배치 문제를 모두 display 하나로 해결하려는 경우

## 실무 연결

내비게이션 링크, 버튼형 링크, 숨김 영역의 기본 표시 방식을 조절할 때 사용합니다.

## 📌 더 알아보기

이후 Flexbox와 Grid를 배우면 복잡한 가로·세로 정렬을 더 편리하게 구현할 수 있습니다.

## 직접 해보기

- 속성값을 하나씩 변경하고 화면 차이를 비교한다.
- 개발자 도구에서 덮어쓴 선언과 최종 계산값을 확인한다.
- 같은 결과를 만들 수 있는 다른 속성이 있는지 기록한다.

## Check Point

- [ ] block과 inline의 차이를 설명할 수 있다.
- [ ] inline-block이 필요한 상황을 설명할 수 있다.
- [ ] `display: none`의 결과를 예상할 수 있다.

## 최종 요약

block, inline, inline-block, none의 차이를 이해하고 기본 배치 방식을 변경한다.

## 복습 기록

- [ ] 예제를 직접 작성했다.
- [ ] 문제를 해설 없이 풀었다.
- [ ] 개발자 도구에서 적용 결과를 확인했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [CSS 박스 모델](CSS_Box_Model.md) |
| 다음 학습 | [CSS Position과 Overflow](CSS_Position_Overflow.md) |
