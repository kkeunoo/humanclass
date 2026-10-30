# 12. JOIN — 같은 번호와 범위로 자료의 관계 연결하기 — 연습문제

[본문](../../12_SQL_JOIN.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

모든 조합과 연결 조건이 있는 조인의 행 수를 구분한다. 표 별칭·동일 열 이름·ON·USING을 읽고 급여 등급의 범위 조인까지 연결한다.

[준비문 포함 전체 SQL](../책형_복습/12_SQL_JOIN.sql)을 제공한다. [본문 3절](../../12_SQL_JOIN.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT COUNT(*) FROM book_emp e, book_dept d;
SELECT e.ename, d.dname
FROM book_emp e JOIN book_dept d ON e.deptno=d.deptno
ORDER BY e.empno;
SELECT e.ename, e.sal, e.deptno
FROM book_emp e JOIN (
 SELECT deptno, MAX(sal) AS max_sal FROM book_emp GROUP BY deptno
) top_sal ON e.deptno=top_sal.deptno AND e.sal=top_sal.max_sal
ORDER BY e.empno;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

첫 결과 **24**. 둘째 결과 ADA–BETA, BEN–GAMMA, CARA–BETA, DAN–ALPHA, ELLA–BETA, FINN–GAMMA. 셋째는 BEN·CARA·DAN·ELLA 네 명이다.

둘째 조회는 부서번호가 같은 한 부서를 각 사원과 연결한다. 셋째는 새 개선 예제다. 부서별 최대 급여 표를 만든 뒤 부서번호와 급여 두 조건을 함께 연결해 자기 부서 최고 급여 사원을 고른다. 11장의 GUS 반례를 추가하더라도20번 최대3000과 맞지 않아 빠진다. 이 장 기본 데이터는 다시6명이다.

</details>

## 문제 2. 이유 설명

1. 조건 없는6명×4부서 조합은?
2. sal IN 최대목록의 부족한 대응은?
3. 등급 범위 조인도 같은 값끼리만 가능한가?
4. deptno를 모호하지 않게 쓰려면?

<details>
<summary>풀이</summary>

24행이다. 부서번호 대응이다. 부등식·BETWEEN 같은 범위 조건도 쓴다. e.deptno처럼 출처를 붙인다.

| 사원 | 번호 | 맞는 부서 | 결과 한 쌍 |
| --- | --- | --- | --- |
| ADA | 20 | BETA | ADA–BETA |
| BEN | 30 | GAMMA | BEN–GAMMA |
| DAN | 10 | ALPHA | DAN–ALPHA |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| ON 조건을 제거한 조합 조회 | 24조합 | 관련 없는 조합도 포함 |
| WHERE e.deptno=20 추가 | ADA·CARA·ELLA | 조인 뒤 요청 필터 |
| GUS20·1600 추가 | 최고 사원에 GUS 없음 | 자기 부서 최대와 불일치 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

행이 폭증하면 연결 조건·중복 키를 본다. 모호한 열 오류면 표 별칭을 붙인다. 사원 수와 결과 행 수가 다르다고 무조건 오류로 판단하지 말고 관계의1대다·매칭 없음 여부를 본다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
