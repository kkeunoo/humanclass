# 02. WHERE — 결과에 남길 행의 조건 정하기 — 연습문제

[본문](../../02_SQL_WHERE와_조건연산자.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

SELECT의 열 선택과 WHERE의 행 선택을 구분한다. AND 우선순위와 괄호를 설명하고 BETWEEN·IN의 의미를 원래 비교식과 연결한다.

[준비문 포함 전체 SQL](../책형_복습/02_SQL_WHERE와_조건연산자.sql)을 제공한다. [본문 3절](../../02_SQL_WHERE와_조건연산자.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT ename FROM book_emp
WHERE deptno = 30 OR deptno = 20 AND job = 'CLERK'
ORDER BY empno;
SELECT ename FROM book_emp
WHERE (deptno = 30 OR deptno = 20) AND job = 'CLERK'
ORDER BY empno;
SELECT ename FROM book_emp WHERE sal BETWEEN 1500 AND 3000 ORDER BY empno;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

| 조회 | 남는 이름 |
| --- | --- |
| 괄호 없는 OR·AND | ADA, BEN, FINN |
| OR 부분을 괄호로 묶음 | ADA |
| 급여 1500–3000 포함 | BEN, CARA, ELLA, FINN |

첫 조건은 30번 부서면 직업과 무관하게 통과하므로 BEN·FINN도 남는다. 둘째는 20 또는 30인 사람 중 CLERK만 남겨 ADA 한 명이다. 셋째는 급여가 정확히 1500인 FINN과 3000인 CARA·ELLA도 포함한다. 같은 데이터에서 괄호 한 쌍과 경계 조건의 영향을 비교한다.

</details>

## 문제 2. 이유 설명

1. BETWEEN은 상한을 포함하는가?
2. A OR B AND C는 어떤 묶음인가?
3. WHERE는 결과 열을 고르는가?
4. 문자 비교는 언제나 대소문자를 구분하는가?

<details>
<summary>풀이</summary>

포함한다. A OR (B AND C)다. 행을 거른다. 설정에 영향을 받으므로 언제나 그렇다고 할 수 없다.

| 사람 | 부서30? | 부서20·CLERK? | 첫 조건 | 둘째 조건 |
| --- | --- | --- | --- | --- |
| ADA | 아니오 | 예 | 통과 | 통과 |
| BEN | 예 | 아니오 | 통과 | 제외 |
| CARA | 아니오 | 아니오 | 제외 | 제외 |
| FINN | 예 | 아니오 | 통과 | 제외 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| BETWEEN 상한을 2999로 | CARA·ELLA 제외 | 경계값 3000 |
| CLERK를 SALESMAN으로 | 둘째 조건 BEN·FINN | 직업 기준 변경 |
| deptno IN (10,20) | ADA·CARA·DAN·ELLA | 두 부서 포함 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

원하는 직업 외 사람이 나오면 OR 범위와 괄호를 본다. 같은 행이 빠지면 >와 >=, BETWEEN 양 끝을 비교한다. 문자열 대소문자 실험은 DB 설정을 확인하지 않고 모든 환경의 규칙으로 외우지 않는다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
