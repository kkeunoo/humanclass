---
title: CSS 우선순위와 상속
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS 우선순위와 상속

## 개요

CSS는 하나의 요소에 여러 스타일이 동시에 적용될 수 있다.

예를 들어 하나의 버튼에 다음과 같이 여러 규칙이 존재할 수 있다.

```css
button {
    color: black;
}

.primary {
    color: blue;
}

#submit {
    color: red;
}
```

```html
<button
    id="submit"
    class="primary"
>
    저장
</button>
```

위 버튼은 어떤 색상이 적용될까?

정답은 **빨간색**이다.

브라우저는 여러 규칙 중 하나를 임의로 선택하는 것이 아니라 **Cascade(계단식 규칙)** 에 따라 우선순위를 계산하여 최종 스타일을 결정한다.

---

# 핵심 개념

CSS의 최종 스타일은 다음 요소를 종합하여 결정된다.

- Cascade
- 선택자 명시도(Specificity)
- 선언 순서(Source Order)
- !important
- 상속(Inheritance)

이 다섯 가지를 이해하면 대부분의 CSS 충돌 문제를 해결할 수 있다.

---

# Cascade란?

Cascade는 여러 CSS 규칙이 충돌할 때 어떤 규칙을 적용할지 결정하는 알고리즘이다.

브라우저는 다음 순서로 스타일을 비교한다.

```text
!important

↓

명시도(Specificity)

↓

작성 순서(Source Order)
```

같은 조건이라면 **나중에 작성된 규칙**이 적용된다.

---

# 명시도(Specificity)

명시도는 선택자의 "강도"를 의미한다.

선택자가 구체적일수록 우선순위가 높다.

대표적인 우선순위는 다음과 같다.

| 선택자 | 점수(개념적) |
|---|---:|
| Inline Style | 1000 |
| ID 선택자 | 100 |
| 클래스 / 속성 / 가상 클래스 | 10 |
| 태그 / 가상 요소 | 1 |
| 전체 선택자(*) | 0 |

> 위 점수는 이해를 돕기 위한 개념적인 수치이며, 실제 브라우저는 단순 합산 방식이 아닌 명시도 규칙에 따라 계산한다.

---

# 명시도 비교

```css
p {
    color: black;
}

.text {
    color: blue;
}

#message {
    color: red;
}
```

```html
<p
    id="message"
    class="text"
>
    Hello
</p>
```

적용 결과

```text
#message

↓

ID 선택자

↓

red
```

---

# 클래스보다 ID가 높은 이유

클래스는 여러 요소에서 재사용되지만,

ID는 문서 안에서 하나의 요소를 고유하게 식별한다.

그래서 더 높은 우선순위를 가진다.

---

# 여러 선택자의 명시도

```css
.card .title {
}
```

명시도

```
20
```

클래스 두 개

```css
#main .title {
}
```

명시도

```
110
```

ID + 클래스

---

# 태그보다 클래스

```css
p {
}
```

↓

1

```css
.notice {
}
```

↓

10

클래스가 적용된다.

---

# Inline Style

HTML

```html
<p style="color:red;">
```

Inline Style은 매우 높은 우선순위를 가진다.

실무에서는 유지보수를 위해 가능한 사용하지 않는다.

---

# !important

```css
p {

color:red !important;

}
```

`!important`는 일반 규칙보다 우선 적용된다.

그러나 남용하면 유지보수가 매우 어려워진다.

실무에서는

- 외부 라이브러리 수정
- 긴급 수정

정도를 제외하면 거의 사용하지 않는다.

---

# Source Order

명시도가 같다면

나중에 작성된 규칙이 적용된다.

```css
.notice{

color:red;

}

.notice{

color:blue;

}
```

결과

```text
blue
```

---

# 상속(Inheritance)

일부 CSS 속성은 부모 요소에서 자식 요소로 자동 전달된다.

예

```css
body{

color:#333;

}
```

```html
<body>

<p>

Hello

</p>

</body>
```

`p`는 별도로 `color`를 지정하지 않아도 부모의 글자색을 상속받는다.

---

# 상속되는 대표 속성

| 속성 | 상속 여부 |
|---|---|
| color | O |
| font-family | O |
| font-size | O |
| line-height | O |
| text-align | O |
| visibility | O |
| cursor | O |

---

# 상속되지 않는 대표 속성

| 속성 | 상속 여부 |
|---|---|
| margin | X |
| padding | X |
| border | X |
| width | X |
| height | X |
| background | X |
| display | X |
| position | X |

---

# inherit

부모 요소의 값을 명시적으로 상속받는다.

```css
button{

color:inherit;

}
```

부모의 글자색을 그대로 사용한다.

---

# initial

속성을 브라우저 기본값으로 되돌린다.

```css
button{

color:initial;

}
```

---

# unset

상속되는 속성은 inherit처럼,

상속되지 않는 속성은 initial처럼 동작한다.

```css
color:unset;
```

---

# revert

브라우저 또는 사용자 스타일 단계로 되돌린다.

```css
all: revert;
```

브라우저 기본 스타일을 활용할 때 사용할 수 있다.

---

# all 속성

모든 CSS 속성을 한 번에 초기화할 수 있다.

```css
button{

all:unset;

}
```

주의

모든 스타일이 초기화되므로 필요한 속성을 다시 지정해야 한다.

---

# 명시도 계산 예제

```css
h1 {
}
```

→ 태그 1개

```css
.title {
}
```

→ 클래스 1개

```css
#header {
}
```

→ ID 1개

```css
header .title {
}
```

→ 태그 + 클래스

```css
#header .title {
}
```

→ ID + 클래스

---

# :is()와 :where()

둘 다 여러 선택자를 묶는다.

```css
:is(header,main){

}
```

`is()`는 내부 선택자의 명시도를 반영한다.

---

```css
:where(header,main){

}
```

`where()`는 명시도가 항상 0이다.

실무에서는 기본 스타일을 작성할 때 유용하다.

---

# DevTools 활용

브라우저 개발자 도구(F12)의 **Styles** 패널에서는

- 어떤 규칙이 적용되었는지
- 어떤 규칙이 덮어쓰기 되었는지
- 취소선이 그어진 이유
- 적용된 선택자의 파일과 위치

를 확인할 수 있다.

CSS가 적용되지 않을 때 가장 먼저 확인해야 하는 도구이다.

---

# 실무 활용

우선순위와 상속은 다음과 같은 상황에서 자주 사용된다.

- 공통 버튼 스타일 작성
- 테마 변경
- 다크 모드
- 컴포넌트 스타일 재사용
- 외부 라이브러리 스타일 재정의
- 디자인 시스템 구축

---

# 실무 예제 프로젝트

## HTML

```html
<header id="header">

    <h1 class="title">
        Developer Academy
    </h1>

</header>

<section class="card">

    <h2 class="title">
        HTML 과정
    </h2>

    <button class="button button-primary">
        신청하기
    </button>

</section>
```

## CSS

```css
body {
    color: #333;
    font-family: Arial, sans-serif;
}

.title {
    color: royalblue;
}

#header .title {
    color: crimson;
}

.button {
    color: inherit;
    padding: 12px 20px;
}

.button-primary {
    background: royalblue;
    color: white;
}

.button-primary:hover {
    background: navy;
}
```

---

# 예제 분석

```css
.title {
}
```

↓

모든 title 클래스

---

```css
#header .title {
}
```

↓

ID + 클래스

↓

더 높은 명시도

↓

crimson 적용

---

```css
.button{

color:inherit;

}
```

↓

body의 color를 상속받음

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|---|---|
| Cascade | CSS 적용 규칙 |
| Specificity | 명시도 |
| Source Order | 선언 순서 |
| Inline Style | 인라인 스타일 |
| !important | 최우선 선언 |
| Inheritance | 상속 |
| inherit | 부모 값 사용 |
| initial | 기본값 복원 |
| unset | 상황에 따라 상속 또는 초기화 |
| revert | 이전 스타일 단계로 복원 |
| all | 모든 속성 제어 |

---

# 자주 하는 실수

## 1.

클래스보다 ID가 항상 좋은 선택이라고 생각한다.

→ 스타일링은 클래스를 우선 사용한다.

---

## 2.

`!important`를 남용한다.

→ 유지보수가 매우 어려워진다.

---

## 3.

같은 명시도에서 먼저 작성한 규칙이 적용된다고 생각한다.

→ 나중에 작성한 규칙이 적용된다.

---

## 4.

모든 CSS 속성이 상속된다고 생각한다.

→ `margin`, `padding`, `border`, `background` 등은 상속되지 않는다.

---

## 5.

`inherit`와 `initial`을 혼동한다.

- `inherit` → 부모 값을 사용
- `initial` → 브라우저 기본값으로 초기화

---

## 6.

`all: unset`을 사용하고 버튼 스타일이 모두 사라지는 이유를 이해하지 못한다.

→ 모든 속성을 초기화하기 때문이다.

---

## 7.

CSS가 적용되지 않을 때 코드만 계속 수정한다.

→ DevTools의 Styles 패널에서 실제 적용 여부를 먼저 확인한다.

---

## 8.

명시도를 높이기 위해 선택자를 지나치게 길게 작성한다.

→ 유지보수가 어려워지고 재사용성이 떨어진다.

---

# 면접 포인트

### Q1.

Cascade란 무엇인가요?

→ 여러 CSS 규칙이 충돌할 때 최종 스타일을 결정하는 알고리즘이다.

---

### Q2.

명시도(Specificity)란 무엇인가요?

→ 선택자의 우선순위를 계산하는 규칙이다.

---

### Q3.

클래스와 ID 중 어느 것이 우선인가요?

→ ID 선택자가 더 높은 명시도를 가진다.

---

### Q4.

`!important`는 언제 사용하는 것이 좋나요?

→ 외부 라이브러리 수정이나 예외적인 상황에서만 제한적으로 사용한다.

---

### Q5.

상속되는 속성과 상속되지 않는 속성의 예를 들어보세요.

- 상속: `color`, `font-family`
- 비상속: `margin`, `padding`, `background`

---

### Q6.

`inherit`, `initial`, `unset`, `revert`의 차이를 설명해 보세요.

→ 각각 부모 상속, 초기값 복원, 상황에 따른 상속/초기화, 이전 스타일 단계 복원의 역할을 한다.

---

### Q7.

CSS가 적용되지 않을 때 가장 먼저 확인해야 하는 것은 무엇인가요?

→ 브라우저 DevTools의 Styles 패널에서 어떤 규칙이 적용되거나 덮어쓰기 되었는지 확인한다.

---

# 핵심 정리

- CSS는 Cascade 규칙에 따라 최종 스타일을 결정한다.
- 명시도가 높은 선택자가 우선 적용된다.
- 명시도가 같다면 나중에 작성한 규칙이 적용된다.
- `!important`는 매우 높은 우선순위를 가지지만 남용을 피해야 한다.
- 일부 속성만 부모로부터 상속된다.
- `inherit`, `initial`, `unset`, `revert`는 각각 다른 방식으로 값을 제어한다.
- DevTools는 CSS 충돌을 분석하는 가장 중요한 도구이다.
- 유지보수를 위해 명시도를 과도하게 높이지 않는 것이 좋다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-22 | 최초 작성 |
| v1.0 | 2026-07-22 | Cascade와 명시도 설명 추가 |
| v1.0 | 2026-07-22 | 상속 및 inherit, initial, unset, revert 정리 |
| v1.0 | 2026-07-22 | DevTools를 활용한 CSS 디버깅 내용 추가 |
| v1.0 | 2026-07-22 | 실무 예제 프로젝트 추가 |
| v1.0 | 2026-07-22 | 자주 하는 실수와 면접 포인트 추가 |