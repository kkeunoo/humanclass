---
title: "CSS 배경과 투명도"
area: "CSS"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "30~50분"
---

# CSS 배경과 투명도

## 학습 목표

- 배경색과 배경 이미지를 설정하고 투명도의 적용 범위를 구분한다.
- 개발자 도구에서 최종 적용된 스타일을 확인한다.
- 해당 속성을 사용하는 이유를 설명한다.

## 왜 배우는가

CSS는 HTML 구조를 읽기 쉽고 사용하기 좋은 화면으로 표현합니다. 이 문서의 속성은 실제 UI의 크기, 간격, 배치와 상태 표현에 직접 사용됩니다.

## 기본 개념

```css
.hero {
    background-color: #f5f5f5;
    background-image: url("images/hero.jpg");
    background-size: cover;
    background-position: center;
}
.overlay { background-color: rgba(0, 0, 0, 0.5); }
```

## 수업 예제

예제를 HTML 요소에 적용한 뒤 개발자 도구의 **Styles**와 **Computed**에서 최종 값을 확인합니다.

## 수업 문제

### 문제

배경 이미지를 영역에 가득 채우고 반투명 오버레이를 추가하세요.

### 요구사항

- 배경 이미지는 중앙을 기준으로 채웁니다.
- 이미지 반복을 막습니다.
- 오버레이만 반투명하게 만듭니다.

### 직접 풀어 보기

해설을 열기 전에 선택자와 속성을 직접 작성하고 브라우저 너비 또는 요소 값을 바꾸어 확인합니다.

<details>
<summary>해설 보기</summary>

```css
.hero {
    background: url("images/hero.jpg") center / cover no-repeat;
}
.overlay { background-color: rgba(0, 0, 0, 0.5); }
```

### 풀이 설명

요구사항에 필요한 속성만 사용했습니다. 각 선언을 한 줄씩 제거해 보며 어떤 역할을 하는지 확인합니다.

</details>

## 자주 하는 실수

- `opacity`를 부모에 적용해 자식 텍스트까지 투명해지는 경우
- 배경 이미지 경로를 CSS 파일 위치 기준으로 계산하지 않는 경우
- cover와 contain의 차이를 확인하지 않는 경우

## 실무 연결

히어로 배너, 카드 배경, 이미지 위 텍스트 가독성 확보에 사용합니다.

## 📌 더 알아보기

여러 배경 이미지를 쉼표로 구분해 겹쳐 사용할 수도 있지만 기본 배경 속성을 익힌 뒤 적용합니다.

## 직접 해보기

- 속성값을 하나씩 변경하고 화면 차이를 비교한다.
- 개발자 도구에서 덮어쓴 선언과 최종 계산값을 확인한다.
- 같은 결과를 만들 수 있는 다른 속성이 있는지 기록한다.

## Check Point

- [ ] background-color와 background-image를 사용할 수 있다.
- [ ] cover와 contain의 차이를 설명할 수 있다.
- [ ] opacity와 rgba 투명도의 차이를 설명할 수 있다.

## 최종 요약

배경색과 배경 이미지를 설정하고 투명도의 적용 범위를 구분한다.

## 복습 기록

- [ ] 예제를 직접 작성했다.
- [ ] 문제를 해설 없이 풀었다.
- [ ] 개발자 도구에서 적용 결과를 확인했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [CSS Flexbox](CSS_Flexbox.md) |
| 다음 학습 | [CSS Float와 Shadow](CSS_Float_Shadow.md) |
