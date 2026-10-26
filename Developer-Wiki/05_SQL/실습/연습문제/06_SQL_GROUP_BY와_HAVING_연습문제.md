# 06 SQL GROUP BY와 HAVING — 연습문제

[원본 비교 본문](../../06_SQL_GROUP_BY와_HAVING.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**이며 강사님 원본 문제나 내 당시 풀이가 아니다. `Script.sql`에는 상태를 바꾸는 문장이 있으므로 원본 전체를 실행하지 말고, 먼저 쿼리의 의미와 결과를 예상한다.

## 문제

부서별 사원 수를 세는 쿼리에서 `GROUP BY`에는 무엇을 적는가?

<details>
<summary>정답과 확인할 점</summary>

`SELECT deptno, COUNT(*) FROM emp GROUP BY deptno;`이다. 부서 번호로 행을 묶는다.

강사님 코드와 내 실제 코드의 작성 방식은 [본문](../../06_SQL_GROUP_BY와_HAVING.md)에서 비교한다.

</details>

## 추가로 알면 좋은 것

DBMS 설정이나 데이터 상태에 따라 결과가 달라질 수 있다. 추가 기능은 본문의 **추가로 알면 좋은 것**을 통해 분리해 읽는다.
