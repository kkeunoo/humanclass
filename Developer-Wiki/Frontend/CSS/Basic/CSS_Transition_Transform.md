---
title: "CSS Transition과 Transform"
area: "CSS"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "30~50분"
---

# CSS Transition과 Transform

## 학습 목표

- 상태 변화에 애니메이션을 적용하고 요소를 이동·확대·회전한다.
- 개발자 도구에서 최종 적용된 스타일을 확인한다.
- 해당 속성을 사용하는 이유를 설명한다.

## 왜 배우는가

CSS는 HTML 구조를 읽기 쉽고 사용하기 좋은 화면으로 표현합니다. 이 문서의 속성은 실제 UI의 크기, 간격, 배치와 상태 표현에 직접 사용됩니다.

## 기본 개념

```css
.button {
    transition: transform 0.2s, box-shadow 0.2s;
}
.button:hover {
    transform: translateY(-2px);
}
```

## 수업 예제

예제를 HTML 요소에 적용한 뒤 개발자 도구의 **Styles**와 **Computed**에서 최종 값을 확인합니다.

## 수업 문제

### 문제

버튼에 마우스를 올리면 부드럽게 위로 이동하고 약간 확대되게 하세요.

### 요구사항

- 변화 시간은 0.2초입니다.
- 이동과 확대는 transform 한 줄에 함께 작성합니다.
- 레이아웃 위치를 직접 변경하지 않습니다.

### 직접 풀어 보기

해설을 열기 전에 선택자와 속성을 직접 작성하고 브라우저 너비 또는 요소 값을 바꾸어 확인합니다.

<details>
<summary>해설 보기</summary>

```css
.button { transition: transform 0.2s; }
.button:hover { transform: translateY(-2px) scale(1.03); }
```

### 풀이 설명

요구사항에 필요한 속성만 사용했습니다. 각 선언을 한 줄씩 제거해 보며 어떤 역할을 하는지 확인합니다.

</details>

## 자주 하는 실수

- 기본 상태가 아닌 hover 상태에만 transition을 작성하는 경우
- 모든 속성에 `transition: all`을 무분별하게 사용하는 경우
- 과도한 움직임으로 사용성을 떨어뜨리는 경우

## 실무 연결

버튼 피드백, 카드 hover, 메뉴 열림과 같은 짧은 상태 변화에 사용합니다.

## 📌 더 알아보기

`cubic-bezier()`와 여러 단계 애니메이션은 더 세밀한 움직임을 만들지만 기본 transition 이후에 학습합니다.

## 직접 해보기

- 속성값을 하나씩 변경하고 화면 차이를 비교한다.
- 개발자 도구에서 덮어쓴 선언과 최종 계산값을 확인한다.
- 같은 결과를 만들 수 있는 다른 속성이 있는지 기록한다.

## Check Point

- [ ] transition의 대상·시간을 지정할 수 있다.
- [ ] translate, scale, rotate의 역할을 설명할 수 있다.
- [ ] 여러 transform 함수를 한 선언에 작성할 수 있다.

## 최종 요약

상태 변화에 애니메이션을 적용하고 요소를 이동·확대·회전한다.

## 복습 기록

- [ ] 예제를 직접 작성했다.
- [ ] 문제를 해설 없이 풀었다.
- [ ] 개발자 도구에서 적용 결과를 확인했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [CSS Float와 Shadow](CSS_Float_Shadow.md) |
| 다음 학습 | [CSS 미디어 쿼리](CSS_Media_Query.md) |
