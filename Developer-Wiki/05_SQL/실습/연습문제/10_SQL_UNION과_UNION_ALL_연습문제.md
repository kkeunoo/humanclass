# 10. UNION과 UNION ALL — 조회 결과를 세로로 이어 붙이기 — 연습문제

[본문](../../10_SQL_UNION과_UNION_ALL.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

UNION·UNION ALL의 결과 행 수를 예상한다. 양쪽 열 개수·대응 위치를 맞추고 JOIN처럼 가로로 붙이는 것과 구별한다.

[준비문 포함 전체 SQL](../책형_복습/10_SQL_UNION과_UNION_ALL.sql)을 제공한다. [본문 3절](../../10_SQL_UNION과_UNION_ALL.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT ename FROM book_emp WHERE deptno=10
UNION
SELECT ename FROM book_emp WHERE deptno=10
ORDER BY ename;
SELECT ename FROM book_emp WHERE deptno=10
UNION ALL
SELECT ename FROM book_emp WHERE deptno=10
ORDER BY ename;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

첫 결과 **DAN 한 행**, 둘째 **DAN 두 행**이다. 원본 book_emp는 여전히 여섯 행이다.

10번 부서는 DAN 한 명이다. 같은 조회를 두 번 실행해 결과를 붙일 때 UNION은 같은 결과 행을 하나로 남긴다. UNION ALL은 각 조회에서 나온 한 행씩 두 행이다. 같은 이름 두 줄이 나왔다고 원본에 사원이 복제된 것은 아니다.

</details>

## 문제 2. 이유 설명

1. UNION은 원본 행을 삭제하는가?
2. 중복 판단은 첫 열만인가?
3. UNION ALL이면 원본 사원이 늘어나는가?
4. 양쪽 열 개수가 달라도 되는가?

<details>
<summary>풀이</summary>

조회 결과만 중복 제거한다. 행 전체다. 원본은 변하지 않는다. 열 개수를 맞춰야 한다.

| 단계 | UNION | UNION ALL |
| --- | --- | --- |
| 첫 조회 | DAN | DAN |
| 둘째 조회 | DAN | DAN |
| 붙인 결과 | DAN | DAN, DAN |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 둘째 부서를 30으로 | DAN·BEN·FINN | 서로 다른 이름 |
| 둘째 SELECT 열 하나 추가 | 열 수 오류 | 결과 모양 불일치 |
| UNION을 UNION ALL로 | 중복 유지 | 정책 변경 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

열 수 오류면 양쪽 SELECT 목록을 세어 본다. 중복이 안 없어지면 선택한 열 전체 값이 같은지 본다. 결과 표시 순서는 ORDER BY 없이 보장된 것으로 외우지 않는다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
