---
title: "CSS 박스 모델"
area: "CSS"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★☆☆☆"
estimated_time: "30~50분"
---

# CSS 박스 모델

## 학습 목표

- content, padding, border, margin을 구분하고 요소의 전체 크기를 계산한다.
- 개발자 도구에서 최종 적용된 스타일을 확인한다.
- 해당 속성을 사용하는 이유를 설명한다.

## 왜 배우는가

CSS는 HTML 구조를 읽기 쉽고 사용하기 좋은 화면으로 표현합니다. 이 문서의 속성은 실제 UI의 크기, 간격, 배치와 상태 표현에 직접 사용됩니다.

## 기본 개념

```css
.card {
    width: 300px;
    padding: 20px;
    border: 1px solid #ccc;
    margin: 16px;
    box-sizing: border-box;
}
```

`box-sizing: border-box`를 사용하면 지정한 너비 안에 padding과 border가 포함됩니다.

## 수업 예제

예제를 HTML 요소에 적용한 뒤 개발자 도구의 **Styles**와 **Computed**에서 최종 값을 확인합니다.

## 수업 문제

### 문제

너비 320px 안에 안쪽 여백과 테두리가 포함되는 카드 스타일을 작성하세요.

### 요구사항

- 카드 너비는 320px입니다.
- 안쪽 여백은 24px입니다.
- 테두리는 1px 실선입니다.
- 전체 너비가 320px을 넘지 않게 합니다.

### 직접 풀어 보기

해설을 열기 전에 선택자와 속성을 직접 작성하고 브라우저 너비 또는 요소 값을 바꾸어 확인합니다.

<details>
<summary>해설 보기</summary>

```css
.card {
    width: 320px;
    padding: 24px;
    border: 1px solid #ccc;
    box-sizing: border-box;
}
```

### 풀이 설명

요구사항에 필요한 속성만 사용했습니다. 각 선언을 한 줄씩 제거해 보며 어떤 역할을 하는지 확인합니다.

</details>

## 자주 하는 실수

- margin과 padding을 반대로 사용하는 경우
- 기본 content-box 상태에서 실제 너비를 잘못 계산하는 경우
- 고정 높이를 지정해 콘텐츠가 넘치는 경우

## 실무 연결

카드, 버튼, 입력창의 크기와 간격은 박스 모델을 기반으로 계산됩니다.

## 📌 더 알아보기

프로젝트에서는 보통 모든 요소에 `box-sizing: border-box`를 적용해 크기 계산을 단순화합니다.

## 직접 해보기

- 속성값을 하나씩 변경하고 화면 차이를 비교한다.
- 개발자 도구에서 덮어쓴 선언과 최종 계산값을 확인한다.
- 같은 결과를 만들 수 있는 다른 속성이 있는지 기록한다.

## Check Point

- [ ] content, padding, border, margin을 구분할 수 있다.
- [ ] 요소의 실제 너비를 계산할 수 있다.
- [ ] `border-box`의 역할을 설명할 수 있다.

## 최종 요약

content, padding, border, margin을 구분하고 요소의 전체 크기를 계산한다.

## 복습 기록

- [ ] 예제를 직접 작성했다.
- [ ] 문제를 해설 없이 풀었다.
- [ ] 개발자 도구에서 적용 결과를 확인했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [CSS 글꼴과 텍스트](CSS_Font.md) |
| 다음 학습 | [CSS display](CSS_Display.md) |
