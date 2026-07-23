---
title: HTML 표 태그
version: v1.0
last_updated: 2026-07-21
status: Completed
---

# HTML 표 태그

## 개요

표(Table)는 행(Row)과 열(Column)로 구성된 데이터를 구조적으로 표현하는 요소이다.

HTML에서는 `<table>`을 사용하여 표를 만들며, 가격표, 회원 목록, 시간표, 통계 자료, 성적표처럼 **행과 열의 관계를 가진 데이터**를 표현할 때 사용한다.

과거에는 웹 페이지의 레이아웃을 만들기 위해 표를 사용하기도 했지만, 현재는 CSS 레이아웃(Flexbox, Grid)을 사용하며 `<table>`은 데이터 표현에만 사용하는 것이 원칙이다.

---

# 핵심 개념

표는 다음 요소들로 구성된다.

| 태그 | 역할 |
|------|------|
| `<table>` | 표 전체 |
| `<caption>` | 표 제목 |
| `<thead>` | 표 머리글 |
| `<tbody>` | 표 본문 |
| `<tfoot>` | 표 바닥글 |
| `<tr>` | 행(Row) |
| `<th>` | 제목 셀 |
| `<td>` | 데이터 셀 |

---

# table 태그

`<table>`은 표 전체를 감싸는 요소이다.

```html
<table>

</table>
```

모든 표 요소는 `<table>` 내부에 작성한다.

---

# tr 태그

`tr`은 Table Row의 약자이다.

표의 한 행을 의미한다.

```html
<tr>

</tr>
```

---

# td 태그

`td`는 Table Data의 약자이다.

실제 데이터를 나타내는 셀이다.

```html
<tr>

    <td>HTML</td>

    <td>Frontend</td>

</tr>
```

---

# th 태그

`th`는 Table Header의 약자이다.

제목 셀을 의미한다.

```html
<tr>

    <th>과목</th>

    <th>분류</th>

</tr>
```

브라우저는 기본적으로 굵게 가운데 정렬하여 표시할 수 있지만, 중요한 것은 **제목이라는 의미**이다.

---

# 가장 기본적인 표

```html
<table>

    <tr>

        <th>과목</th>

        <th>기간</th>

    </tr>

    <tr>

        <td>HTML</td>

        <td>2주</td>

    </tr>

    <tr>

        <td>CSS</td>

        <td>3주</td>

    </tr>

</table>
```

---

# caption

표의 제목을 제공한다.

```html
<table>

    <caption>

        웹 개발 교육 과정

    </caption>

</table>
```

`caption`은 접근성 측면에서도 도움이 된다.

---

# thead

표의 머리 영역이다.

```html
<thead>

    <tr>

        <th>과목</th>

        <th>기간</th>

    </tr>

</thead>
```

---

# tbody

실제 데이터 영역이다.

```html
<tbody>

    <tr>

        <td>HTML</td>

        <td>2주</td>

    </tr>

</tbody>
```

---

# tfoot

합계나 요약 정보를 작성한다.

```html
<tfoot>

    <tr>

        <td>총 기간</td>

        <td>24주</td>

    </tr>

</tfoot>
```

---

# 전체 구조

```html
<table>

    <caption>

        웹 개발 과정

    </caption>

    <thead>

    </thead>

    <tbody>

    </tbody>

    <tfoot>

    </tfoot>

</table>
```

---

# colspan

여러 열을 하나로 합친다.

```html
<td colspan="2">

    모집 중

</td>
```

---

# rowspan

여러 행을 하나로 합친다.

```html
<td rowspan="2">

    Frontend

</td>
```

---

# scope 속성

제목 셀의 범위를 명확하게 지정한다.

```html
<th scope="col">

    과목

</th>
```

```html
<th scope="row">

    HTML

</th>
```

대표적인 값

| 값 | 의미 |
|------|------|
| col | 열 제목 |
| row | 행 제목 |

---

# 표 접근성

좋은 예

```html
<table>

    <caption>

        교육 과정

    </caption>

</table>
```

머리글은 `th`를 사용한다.

```html
<th scope="col">

```

---

# border 속성

과거에는

```html
<table border="1">
```

처럼 작성했다.

현재는 CSS를 사용한다.

```css
table {

    border-collapse: collapse;

}
```

---

# border-collapse

```css
table {

    border-collapse: collapse;

}
```

셀 테두리를 하나로 합친다.

---

# 실무 활용

표는 다음과 같은 데이터에 적합하다.

- 회원 목록
- 주문 내역
- 성적표
- 가격표
- 시간표
- 통계
- 관리자 페이지

---

# 표를 사용하면 안 되는 경우

레이아웃

```text
Header

Sidebar

Content

Footer
```

이런 화면은 표가 아니라

- Flexbox
- Grid

를 사용한다.

---

# 실무 예제 프로젝트

```html
<table>

    <caption>

        웹 개발 교육 과정

    </caption>

    <thead>

        <tr>

            <th scope="col">과정</th>

            <th scope="col">기간</th>

            <th scope="col">난이도</th>

        </tr>

    </thead>

    <tbody>

        <tr>

            <td>HTML</td>

            <td>2주</td>

            <td>입문</td>

        </tr>

        <tr>

            <td>CSS</td>

            <td>3주</td>

            <td>기초</td>

        </tr>

        <tr>

            <td>JavaScript</td>

            <td>6주</td>

            <td>중급</td>

        </tr>

    </tbody>

    <tfoot>

        <tr>

            <td colspan="3">

                총 교육 기간 : 24주

            </td>

        </tr>

    </tfoot>

</table>
```

---

# 이번 문서에서 새롭게 배운 내용

| 개념 | 설명 |
|------|------|
| table | 표 전체 |
| tr | 행 |
| td | 데이터 |
| th | 제목 셀 |
| caption | 표 제목 |
| thead | 머리 |
| tbody | 본문 |
| tfoot | 바닥 |
| colspan | 열 병합 |
| rowspan | 행 병합 |
| scope | 제목 범위 |
| border-collapse | 테두리 병합 |

---

# 자주 하는 실수

## 1.

레이아웃을 표로 만든다.

→ Flexbox나 Grid를 사용한다.

---

## 2.

모든 셀을 td로 만든다.

→ 제목은 th를 사용한다.

---

## 3.

caption을 생략한다.

→ 표의 목적을 설명하는 제목을 제공하는 것이 좋다.

---

## 4.

thead를 사용하지 않는다.

→ 큰 표에서는 구조를 나누는 것이 좋다.

---

## 5.

border 속성을 사용한다.

```html
<table border="1">
```

→ CSS 사용

---

## 6.

colspan, rowspan 사용 후 셀 개수를 맞추지 않는다.

표 구조가 깨질 수 있다.

---

## 7.

scope를 생략한다.

행과 열 제목을 명확히 전달하기 위해 필요할 수 있다.

---

## 8.

표로 페이지 레이아웃을 만든다.

현대 웹에서는 사용하지 않는다.

---

# 면접 포인트

### Q1.

table과 div의 차이는?

→ table은 표 데이터, div는 일반적인 레이아웃과 그룹화에 사용한다.

---

### Q2.

thead와 tbody를 왜 나누나요?

구조를 명확하게 표현하고 스타일링, 접근성, 스크립트 처리에 도움이 된다.

---

### Q3.

caption은 왜 사용하나요?

표의 제목을 제공하여 사용자가 표의 목적을 이해하기 쉽게 한다.

---

### Q4.

th와 td의 차이는?

th는 제목 셀, td는 데이터 셀이다.

---

### Q5.

colspan과 rowspan의 차이는?

- colspan: 여러 열 병합
- rowspan: 여러 행 병합

---

### Q6.

scope는 왜 사용하나요?

제목 셀이 어떤 데이터와 연결되는지 보조 기술에 전달하기 위해 사용한다.

---

### Q7.

레이아웃을 table로 만들면 안 되는 이유는?

표는 데이터를 표현하는 의미를 가지며, 레이아웃은 CSS(Flexbox, Grid)로 구현하는 것이 적절하다.

---

# 핵심 정리

- `<table>`은 행과 열로 구성된 데이터를 표현한다.
- `<tr>`은 행, `<th>`는 제목 셀, `<td>`는 데이터 셀이다.
- `<caption>`은 표의 제목을 제공한다.
- `<thead>`, `<tbody>`, `<tfoot>`으로 표를 의미 있게 구분할 수 있다.
- `colspan`은 열 병합, `rowspan`은 행 병합에 사용한다.
- `scope`는 제목 셀의 범위를 명확하게 전달한다.
- 표의 테두리와 디자인은 CSS로 작성한다.
- 레이아웃을 만들기 위해 `<table>`을 사용하지 않는다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|------|------|----------|
| v1.0 | 2026-07-21 | 최초 작성 |
| v1.0 | 2026-07-21 | table, tr, th, td 설명 추가 |
| v1.0 | 2026-07-21 | caption, thead, tbody, tfoot 추가 |
| v1.0 | 2026-07-21 | colspan, rowspan, scope 설명 추가 |
| v1.0 | 2026-07-21 | 접근성 및 실무 예제 추가 |
| v1.0 | 2026-07-21 | 자주 하는 실수와 면접 포인트 추가 |