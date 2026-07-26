---
title: HTML 목록과 표
category: HTML
last_updated: 2026-07-27
status: Active
---

# HTML 목록과 표


## 목록

```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>

<ol>
  <li>파일 생성</li>
  <li>코드 작성</li>
  <li>브라우저 확인</li>
</ol>
```

`ul`은 순서가 중요하지 않은 목록, `ol`은 순서가 있는 목록이다. 항목은 반드시 `li`로 작성한다.

## 표

```html
<table>
  <caption>수강 현황</caption>
  <thead>
    <tr><th>이름</th><th>과목</th></tr>
  </thead>
  <tbody>
    <tr><td>홍길동</td><td>JavaScript</td></tr>
  </tbody>
</table>
```

- `tr`: 행
- `th`: 제목 셀
- `td`: 데이터 셀
- `thead`, `tbody`: 표의 구조 구분

## 실무 연결

상품 목록이나 관리자 데이터처럼 행과 열의 관계가 명확한 데이터에 표를 사용한다. 단순한 화면 배치를 위해 `table`을 사용하지 않는다.

## 주의사항

`rowspan`, `colspan`을 사용할 때 실제 행과 열의 개수를 계산해야 셀이 밀리지 않는다.
