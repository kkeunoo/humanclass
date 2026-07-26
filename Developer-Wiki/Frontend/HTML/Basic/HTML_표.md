---
title: HTML 표
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# HTML 표

## 개념

표는 행과 열로 연결된 데이터를 표현한다.

## 문법

```html
<table>
    <tr>
        <th>이름</th>
        <th>점수</th>
    </tr>
    <tr>
        <td>홍길동</td>
        <td>90</td>
    </tr>
</table>
```

## 예제

```html
<td colspan="2">합계</td>
```

## 실무 예제

시간표, 성적표, 상품 비교처럼 행과 열 관계가 중요한 데이터를 표현한다.

## 주의사항

레이아웃 배치 목적으로 표를 사용하지 않는다. `rowspan`, `colspan` 사용 시 실제 칸 수를 계산한다.

## 면접 포인트

`th`와 `td`, `rowspan`과 `colspan`의 역할을 설명한다.

## 요약

표는 관계가 있는 행·열 데이터를 표현할 때 사용한다.
