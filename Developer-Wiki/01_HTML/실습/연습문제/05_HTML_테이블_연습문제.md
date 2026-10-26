# 05 HTML 테이블 — 연습문제

[해당 본문](../../05_HTML_테이블.md) · [장별 문제 목차](README.md)

**새로 구성한 문제**다. 먼저 강사님·내 코드의 실제 결과를 읽고 아래 조건을 직접 구현하거나 계산하자.

## 문제

과목·시간 열의 표에 데이터 두 행을 만들고, 맨 위에 표 제목을 넣자.

**확인 기준:** `caption`, 제목 행, 데이터 행 두 개가 나타난다.

<details>
<summary>해설 — 먼저 풀고 펼치기</summary>

```html
<table>
  <caption>복습 시간표</caption>
  <tr><th>과목</th><th>시간</th></tr>
  <tr><td>HTML</td><td>1시간</td></tr>
  <tr><td>CSS</td><td>1시간</td></tr>
</table>
```
`caption`은 표의 제목, `th`는 열 제목, `td`는 데이터다.

</details>

원본의 입력·구조·결과와 이 연습문제에서 바꾼 조건을 한 문장으로 비교해 보자.
