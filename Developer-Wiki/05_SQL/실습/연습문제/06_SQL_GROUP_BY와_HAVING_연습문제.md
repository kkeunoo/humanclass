# 06. GROUP BY와 HAVING — 어떤 단위로 묶고 남길 것인가 — 연습문제

[본문](../../06_SQL_GROUP_BY와_HAVING.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

전체 집계와 부서·직업별 집계를 나눈다. WHERE는 행, HAVING은 그룹을 거르는 용도를 설명한다. 불필요한 sal 그룹 기준이 평균 의미를 바꾸는 이유를 확인한다.

[준비문 포함 전체 SQL](../책형_복습/06_SQL_GROUP_BY와_HAVING.sql)을 제공한다. [본문 3절](../../06_SQL_GROUP_BY와_HAVING.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT deptno, COUNT(*) AS people, SUM(sal) AS total_sal
FROM book_emp GROUP BY deptno ORDER BY deptno;
SELECT deptno, COUNT(*) AS people, AVG(sal) AS avg_sal
FROM book_emp WHERE sal >= 1500
GROUP BY deptno HAVING COUNT(*) >= 2 ORDER BY deptno;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

| 첫 조회 부서 | 인원 | 급여 합 |
| --- | --- | --- |
| 10 | 1 | 1300 |
| 20 | 3 | 7000 |
| 30 | 2 | 3100 |

둘째 조회는 20번 2명·평균3000, 30번 2명·평균1550이다.

첫 조회는 전원을 부서별로 묶는다. 둘째는 ADA 1000·DAN 1300을 먼저 제외한 다음 남은 사람을 묶는다. 20번은 CARA·ELLA, 30번은 BEN·FINN이고 두 그룹 모두 2명이므로 남는다. 10번은 필터 뒤 행이 없어 사라진다. HAVING은 그 뒤 그룹 수를 판단한다.

</details>

## 문제 2. 이유 설명

1. 부서·직업별 평균에 sal을 더 묶으면 같은가?
2. 개인 급여 조건은 WHERE인가 HAVING인가?
3. 그룹 인원 조건은 어디에 쓰는가?
4. GROUP BY가 언제나 입력 전원을 유지하는 결과를 내는가?

<details>
<summary>풀이</summary>

같지 않다. 급여별로 더 나뉜다. 개인 급여는 WHERE, 그룹 인원은 HAVING이 적합하다. 결과는 사원 행 단위가 아니라 그룹 단위로 바뀐다.

| 단계 | 남은 사원 | 그룹 |
| --- | --- | --- |
| 전체 | 6명 | 아직 없음 |
| sal>=1500 | BEN·CARA·ELLA·FINN | 아직 없음 |
| 부서로 묶음 | 같은 네 명 | 20·30 두 그룹 |
| COUNT>=2 | 같은 두 그룹 | 모두 통과 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| HAVING COUNT>=3 | 둘째 조회 0행 | 남은 각 그룹 2명 |
| WHERE 제거 | 20번3명·30번2명 | 집계에 포함한 행 변경 |
| 첫 조회에 sal 그룹 추가 | 부서 안 급여별 분할 | 기준 변경 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

평균이 개별 급여처럼 보이면 그룹 기준에 sal이 들어갔는지 본다. 오류 없이 job이 보이더라도 의도한 대표값인지 확정하지 않는다. SQL 모드가 허용하는 모호한 구문과 원하는 결과가 같은 것은 아니다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
