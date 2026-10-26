# 10 SQL UNION과 UNION ALL — 연습문제

[원본 비교 본문](../../10_SQL_UNION과_UNION_ALL.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**이며 강사님 원본 문제나 내 당시 풀이가 아니다. `Script.sql`에는 상태를 바꾸는 문장이 있으므로 원본 전체를 실행하지 말고, 먼저 쿼리의 의미와 결과를 예상한다.

## 문제

같은 행이 두 SELECT 결과에 있으면 `UNION`과 `UNION ALL` 결과 행 수는 어떻게 다른가?

<details>
<summary>정답과 확인할 점</summary>

`UNION`은 중복 행을 제거하고 `UNION ALL`은 중복 행도 유지한다.

강사님 코드와 내 실제 코드의 작성 방식은 [본문](../../10_SQL_UNION과_UNION_ALL.md)에서 비교한다.

</details>

## 추가로 알면 좋은 것

DBMS 설정이나 데이터 상태에 따라 결과가 달라질 수 있다. 추가 기능은 본문의 **추가로 알면 좋은 것**을 통해 분리해 읽는다.
