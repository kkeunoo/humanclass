---
title: "CSS Flexbox"
area: "CSS"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "30~50분"
---

# CSS Flexbox

## 학습 목표

- 주축과 교차축을 이해하고 요소를 한 방향으로 정렬한다.
- 개발자 도구에서 최종 적용된 스타일을 확인한다.
- 해당 속성을 사용하는 이유를 설명한다.

## 왜 배우는가

CSS는 HTML 구조를 읽기 쉽고 사용하기 좋은 화면으로 표현합니다. 이 문서의 속성은 실제 UI의 크기, 간격, 배치와 상태 표현에 직접 사용됩니다.

## 기본 개념

```css
.card-list {
    display: flex;
    gap: 16px;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}
```

## 수업 예제

예제를 HTML 요소에 적용한 뒤 개발자 도구의 **Styles**와 **Computed**에서 최종 값을 확인합니다.

## 수업 문제

### 문제

세 개의 카드를 가로로 배치하고 화면이 좁아지면 다음 줄로 이동하게 하세요.

### 요구사항

- 부모 요소에 Flexbox를 적용합니다.
- 카드 사이 간격은 16px입니다.
- 공간이 부족하면 줄바꿈합니다.

### 직접 풀어 보기

해설을 열기 전에 선택자와 속성을 직접 작성하고 브라우저 너비 또는 요소 값을 바꾸어 확인합니다.

<details>
<summary>해설 보기</summary>

```css
.card-list {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}
.card { flex: 1 1 220px; }
```

### 풀이 설명

요구사항에 필요한 속성만 사용했습니다. 각 선언을 한 줄씩 제거해 보며 어떤 역할을 하는지 확인합니다.

</details>

## 자주 하는 실수

- 자식 요소에만 `display: flex`를 적용하는 경우
- 주축과 교차축을 혼동하는 경우
- 너비 조건 없이 무조건 한 줄 배치를 강제하는 경우

## 실무 연결

헤더 메뉴, 버튼 그룹, 카드 목록, 폼 행 등 현대적인 레이아웃에서 널리 사용합니다.

## 📌 더 알아보기

`flex-grow`, `flex-shrink`, `flex-basis`는 남는 공간의 분배와 줄어드는 방식을 세밀하게 조절합니다.

## 직접 해보기

- 속성값을 하나씩 변경하고 화면 차이를 비교한다.
- 개발자 도구에서 덮어쓴 선언과 최종 계산값을 확인한다.
- 같은 결과를 만들 수 있는 다른 속성이 있는지 기록한다.

## Check Point

- [ ] 부모에 `display: flex`를 적용할 수 있다.
- [ ] justify-content와 align-items의 차이를 설명할 수 있다.
- [ ] flex-wrap으로 줄바꿈을 만들 수 있다.

## 최종 요약

주축과 교차축을 이해하고 요소를 한 방향으로 정렬한다.

## 복습 기록

- [ ] 예제를 직접 작성했다.
- [ ] 문제를 해설 없이 풀었다.
- [ ] 개발자 도구에서 적용 결과를 확인했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [CSS Position과 Overflow](CSS_Position_Overflow.md) |
| 다음 학습 | [CSS 배경과 투명도](CSS_Background_Opacity.md) |
