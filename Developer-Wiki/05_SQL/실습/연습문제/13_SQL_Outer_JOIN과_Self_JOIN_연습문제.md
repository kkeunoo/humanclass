# 13 SQL Outer JOIN과 Self JOIN — 연습문제

[원본 비교 본문](../../13_SQL_Outer_JOIN과_Self_JOIN.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**이며 강사님 원본 문제나 내 당시 풀이가 아니다. `Script.sql`에는 상태를 바꾸는 문장이 있으므로 원본 전체를 실행하지 말고, 먼저 쿼리의 의미와 결과를 예상한다.

## 문제

사원이 없는 부서도 목록에 남기려면 어느 표를 기준으로 외부 조인할 것인가?

<details>
<summary>정답과 확인할 점</summary>

`DEPT`를 기준으로 `EMP`를 LEFT JOIN한다. INNER JOIN이면 사원이 없는 부서는 빠진다.

강사님 코드와 내 실제 코드의 작성 방식은 [본문](../../13_SQL_Outer_JOIN과_Self_JOIN.md)에서 비교한다.

</details>

## 추가로 알면 좋은 것

DBMS 설정이나 데이터 상태에 따라 결과가 달라질 수 있다. 추가 기능은 본문의 **추가로 알면 좋은 것**을 통해 분리해 읽는다.
