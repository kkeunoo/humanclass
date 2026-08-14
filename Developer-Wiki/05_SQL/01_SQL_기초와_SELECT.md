---
title: SQL 기초와 SELECT
version: v2.0-final
last_updated: 2026-08-12
status: Completed
---

# SQL 기초와 SELECT

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `01_SQL_기초와_SELECT.md` |
| 분류 | `05_SQL` |
| 원본 기준 | `workspace_sql/Script.sql`, `workspace_teacher/workspace_sql/Script.sql` |
| DB 기준 자료 | `[DB]학습용_emp 신규-mariadb.sql` |
| DBMS | MariaDB |
| 핵심 범위 | SQL Comment, Table 조회, `SELECT`, `*`, Column 선택, `DISTINCT`, Alias, 산술식, 상수 조회, `NULL` 산술 |
| 학습 범위 | SQL 실행 구조, 실습 Table 이해, SELECT List 작성, 결과 Column 이름 변경, 중복 제거 |
| 문서 형식 | SQL Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드의 `Script.sql` 초반부를 비교해 SQL Comment, 실습 Table, `SELECT`, Column 선택, `DISTINCT`, Alias, 산술식과 `NULL` 연산을 정리한다.  
> `[DB]학습용_emp 신규-mariadb.sql`은 `EMP`, `DEPT`, `BONUS`, `SALGRADE`를 준비하는 **실습 환경 기준 자료**로만 사용하고, 실제 학습 흐름은 `Script.sql`을 중심으로 분석한다.

---

# 학습 목표

- SQL과 Query의 기본 역할을 설명할 수 있다.
- MariaDB에서 한 줄·여러 줄 Comment를 작성할 수 있다.
- `SELECT ... FROM ...`의 기본 구조를 이해할 수 있다.
- `SELECT *`와 필요한 Column만 선택하는 방식의 차이를 설명할 수 있다.
- `DISTINCT`로 중복 Row를 제거할 수 있다.
- Alias를 이용해 결과 Column 이름을 읽기 쉽게 만들 수 있다.
- `SELECT` List에서 산술식을 계산할 수 있다.
- Table 없이 상수와 표현식을 조회할 수 있다.
- `NULL`이 포함된 산술 결과를 설명할 수 있다.
- 실습용 `EMP`, `DEPT`, `SALGRADE`, `BONUS` Table의 역할을 구분할 수 있다.
- 내 코드와 강사님 코드의 실제 차이와 잘못된 설명을 구분할 수 있다.

---

# 1. SQL이란?

SQL은 관계형 Database에서 Data를 조회하고 정의하고 변경하기 위한 언어다.

```text
SQL
→ Structured Query Language
```

대표적인 작업은 다음과 같다.

```text
SELECT
→ Data 조회

INSERT
→ Data 추가

UPDATE
→ Data 수정

DELETE
→ Data 삭제

CREATE
→ Database Object 생성

ALTER
→ Database Object 구조 변경

DROP
→ Database Object 삭제
```

이번 문서는 그중 **Data 조회의 출발점인 `SELECT`**를 다룬다.

---

# 2. Query란?

Database에 전달하는 SQL 명령을 일반적으로 Query라고 부른다.

```sql
SELECT *
FROM emp;
```

이 Query는 `emp` Table의 모든 Column과 모든 Row를 조회한다.

---

# 3. SQL Comment

## 3.1 한 줄 Comment

```sql
-- 전체 사원 조회
SELECT *
FROM emp;
```

`--` 뒤의 내용은 Comment로 처리된다.

MariaDB에서는 일반적으로 `--` 뒤에 공백을 두는 형태를 사용하는 것이 안전하다.

```sql
-- 올바른 Comment
```

---

## 3.2 여러 줄 Comment

```sql
/*
EMP Table의
사원 정보를 조회한다.
*/
SELECT *
FROM emp;
```

여러 줄 설명은 `/* ... */`로 작성할 수 있다.

---

# 4. 실습 Database 구조

이번 SQL 수업은 `[DB]학습용_emp 신규-mariadb.sql`에서 준비한 Sample Table을 사용한다.

```text
human Database
├── DEPT
├── EMP
├── BONUS
└── SALGRADE
```

---

# 5. `DEPT` Table

부서 정보를 저장한다.

| Column | 의미 |
| --- | --- |
| `DEPTNO` | 부서 번호 |
| `DNAME` | 부서 이름 |
| `LOC` | 부서 위치 |

Sample Data:

```text
10  ACCOUNTING  NEW YORK
20  RESEARCH    DALLAS
30  SALES       CHICAGO
40  OPERATIONS  BOSTON
```

`DEPTNO`는 Primary Key다.

---

# 6. `EMP` Table

사원 정보를 저장한다.

| Column | 의미 |
| --- | --- |
| `EMPNO` | 사원 번호 |
| `ENAME` | 사원 이름 |
| `JOB` | 직무 |
| `MGR` | 관리자 사원 번호 |
| `HIREDATE` | 입사일 |
| `SAL` | 급여 |
| `COMM` | Commission |
| `DEPTNO` | 부서 번호 |

`EMPNO`는 Primary Key이고 `DEPTNO`는 `DEPT.DEPTNO`를 참조하는 Foreign Key다.

```text
EMP.DEPTNO
    ↓
DEPT.DEPTNO
```

> [!NOTE]
> 원본 Comment에는 `SAL : 연봉`, `COMM : 보너스`라고 적혀 있다.  
> 하지만 Sample EMP Data 자체는 특정 지급 주기를 Schema로 명시하지 않으므로 문서에서는 `SAL`을 **급여**, `COMM`을 **Commission**으로 설명한다.

---

# 7. `SALGRADE` Table

급여 범위에 따른 Grade를 저장한다.

| Column | 의미 |
| --- | --- |
| `GRADE` | 급여 등급 |
| `LOSAL` | 등급 최소 급여 |
| `HISAL` | 등급 최대 급여 |

Sample:

```text
1  700   1200
2  1201  1400
3  1401  2000
4  2001  3000
5  3001  9999
```

이 Table은 `EMP`와 Foreign Key로 직접 연결된 것은 아니다.

추후 다음과 같은 범위 조건으로 연결한다.

```sql
e.sal BETWEEN s.losal AND s.hisal
```

---

# 8. `BONUS` Table

Bonus 관련 실습을 위한 Table이다.

```text
BONUS
├── ENAME
├── JOB
├── SAL
└── COMM
```

현재 초기 Sample Data는 별도로 Insert되지 않는다.

---

# 9. 가장 기본적인 `SELECT`

```sql
SELECT *
FROM emp;
```

구조:

```text
SELECT
→ 무엇을 조회할지 지정

FROM
→ 어느 Table에서 조회할지 지정
```

---

# 10. `SELECT *`

`*`는 해당 Table의 모든 Column을 의미한다.

```sql
SELECT *
FROM emp;
```

`EMP`의 다음 Column들이 모두 결과에 포함된다.

```text
EMPNO
ENAME
JOB
MGR
HIREDATE
SAL
COMM
DEPTNO
```

---

# 11. `SELECT *`는 언제 사용할까?

학습·탐색 단계에서는 편리하다.

```sql
SELECT *
FROM emp;
```

하지만 실제 Application Query에서는 필요한 Column만 명시하는 편이 좋다.

```sql
SELECT
    empno,
    ename,
    job
FROM emp;
```

이유:

- 필요한 Data가 명확하다.
- Schema에 Column이 추가되어도 결과 구조가 불필요하게 바뀌지 않는다.
- Network로 전달하는 Data를 줄일 수 있다.
- Code Review에서 Query 목적을 이해하기 쉽다.

---

# 12. 여러 Table 확인

원본에서는 다음 Query로 Sample Table을 먼저 확인한다.

```sql
SELECT *
FROM emp;

SELECT *
FROM dept;

SELECT *
FROM salgrade;
```

각 Table이 어떤 Data를 가지고 있는지 탐색하는 단계다.

---

# 13. 특정 Column 조회

모든 Column이 아니라 필요한 Column만 지정할 수 있다.

```sql
SELECT empno
FROM emp;
```

결과에는 사원 번호 Column만 나온다.

---

# 14. 여러 Column 조회

`,`로 여러 Column을 나열한다.

```sql
SELECT
    empno,
    ename
FROM emp;
```

결과:

```text
EMPNO | ENAME
```

---

# 15. SQL 줄바꿈과 들여쓰기

다음 두 Query는 의미가 같다.

```sql
SELECT empno, ename FROM emp;
```

```sql
SELECT
    empno,
    ename
FROM emp;
```

SQL은 일반적인 공백과 줄바꿈 자체보다 Token 구조를 기준으로 해석한다.

실무에서는 긴 Query를 읽기 쉽게 줄바꿈한다.

---

# 16. Keyword 대소문자

MariaDB SQL Keyword는 일반적으로 대소문자를 구분하지 않는다.

```sql
select *
from emp;
```

```sql
SELECT *
FROM emp;
```

둘 다 실행할 수 있다.

실무 문서에서는 Keyword를 대문자로 통일하면 Column·Table 이름과 구분하기 쉽다.

```sql
SELECT
    empno,
    ename
FROM emp;
```

---

# 17. `WHERE 1 != 1`로 Column 구조 확인

내 코드에는 다음 실험이 있다.

```sql
SELECT *
FROM emp
WHERE 1 != 1;
```

`1 != 1`은 항상 False이므로 Row는 반환되지 않는다.

하지만 Result Set의 Column Header는 확인할 수 있다.

```text
결과 Row
→ 0개

Column Metadata
→ 확인 가능
```

이 방식은 학습 실험으로 사용할 수 있지만 Table Schema를 확인하는 정식 방법은 아니다.

MariaDB에서는 다음 명령이 더 명확하다.

```sql
DESCRIBE emp;
```

또는:

```sql
SHOW COLUMNS
FROM emp;
```

---

# 18. IDE의 Table 이동 기능은 SQL 문법이 아니다

내 코드에는 다음 Comment가 있다.

```text
Ctrl + 클릭으로 Table명을 볼 수 있음
```

이 기능은 DBeaver나 IDE가 제공하는 Navigation 기능일 수 있다.

```text
SQL 문법
≠
Database Client 기능
```

환경이 달라지면 Shortcut도 달라질 수 있으므로 SQL 개념과 도구 기능을 구분한다.

---

# 19. `DISTINCT`

중복된 결과를 제거하고 싶을 때 사용한다.

```sql
SELECT job
FROM emp;
```

`JOB`은 여러 사원이 같은 값을 가질 수 있다.

예:

```text
CLERK
SALESMAN
SALESMAN
MANAGER
...
```

---

# 20. `SELECT DISTINCT`

```sql
SELECT DISTINCT job
FROM emp;
```

중복된 `JOB` 값을 하나씩만 반환한다.

예상되는 종류:

```text
CLERK
SALESMAN
MANAGER
ANALYST
PRESIDENT
```

---

# 21. `DISTINCT`는 Row 조합에 적용된다

다음 Query를 보자.

```sql
SELECT DISTINCT
    deptno,
    job
FROM emp;
```

`DISTINCT`는 `DEPTNO`만 따로, `JOB`만 따로 중복 제거하는 것이 아니다.

```text
(DEPTNO, JOB)
```

**선택된 전체 Column 조합이 같은 Row**를 중복으로 판단한다.

---

# 22. `ALL`

`SELECT`의 기본 동작은 중복을 허용한다.

```sql
SELECT ALL job
FROM emp;
```

일반적으로 `ALL`은 생략한다.

```sql
SELECT job
FROM emp;
```

두 Query는 같은 의미다.

---

# 23. 원본의 SELECT 문법 설명 교정

내 코드 원본에는 다음 설명이 있다.

```text
SELECT [DISTINCT|ALL] 열_리스트
FROM 테이블_리스트
WHERE 검색_조건식
GROUP BY 그룹_기준열_리스트
HAVING 그룹_조건식
ORDER BY ...
6개의 절로 사용 가능
```

전체 Query 흐름을 미리 보는 설명으로는 의미가 있다.

하지만 다음 부분은 수정해야 한다.

```text
SQL에서는 []를 써도 되고 생략도 가능
```

문법 설명서의 `[]`는 보통 **선택 사항(Optional)** 을 표현하기 위한 Meta Notation이지, MariaDB Query에서 그대로 작성하는 문자가 아니다.

즉:

```text
SELECT [DISTINCT | ALL] ...
```

의 의미는:

```text
DISTINCT 또는 ALL을
필요에 따라 선택해서 작성할 수 있다.
```

라는 뜻이다.

다음처럼 실제 Query에 대괄호를 넣는 의미가 아니다.

```sql
-- MariaDB SELECT 문법으로 사용하지 않는다.
SELECT [DISTINCT] job
FROM emp;
```

---

# 24. Alias란?

Alias는 Result Set의 Column 이름을 임시로 바꾸는 기능이다.

```sql
SELECT job AS 직업
FROM emp;
```

원본 Column은 `JOB`이지만 Result Header는 `직업`으로 표시된다.

Database의 실제 Column Name이 변경되는 것은 아니다.

---

# 25. `AS`

```sql
SELECT job AS 직업
FROM emp;
```

`AS`를 사용하면 Alias임을 명확하게 읽을 수 있다.

---

# 26. `AS` 생략

MariaDB에서는 Column Alias의 `AS`를 생략할 수도 있다.

```sql
SELECT job 직업
FROM emp;
```

동작할 수 있지만 긴 Query에서는 `AS`를 명시하면 의도가 더 분명하다.

---

# 27. 공백이 포함된 Alias

원본에는 다음 Query가 있다.

```sql
SELECT job AS '직업 이름'
FROM emp;
```

MariaDB에서는 `SELECT` List Alias에 문자열 Quote가 허용되는 문맥이 있어 이 Query가 동작할 수 있다.

하지만 Alias는 Column Identifier처럼 다루는 편이 더 명확하다.

```sql
SELECT job AS `직업 이름`
FROM emp;
```

또는 공백을 제거한다.

```sql
SELECT job AS 직업이름
FROM emp;
```

> [!TIP]
> SQL Mode와 DBMS 차이를 줄이고 Identifier라는 의도를 분명히 하려면 MariaDB에서는 Backtick 사용을 검토한다.

---

# 28. Alias는 Result에만 적용된다

```sql
SELECT
    job AS 직업
FROM emp;
```

Table Schema는 그대로다.

```text
EMP.JOB
→ 그대로 유지

Result Header
→ 직업
```

---

# 29. Alias를 사용하는 이유

- 긴 표현식을 읽기 쉽게 만든다.
- Report Header를 의미 있게 만든다.
- Function 결과에 이름을 붙인다.
- Join 시 같은 Column 이름을 구분하기 쉽다.

예:

```sql
SELECT
    sal,
    sal * 12 AS annualized_sal
FROM emp;
```

---

# 30. SELECT List에서 산술식 사용

Column 값을 이용해 계산할 수 있다.

```sql
SELECT
    sal,
    sal * 12
FROM emp;
```

각 Row의 `SAL`에 12를 곱한 결과가 함께 출력된다.

---

# 31. 계산 결과에는 Alias를 붙인다

## Before

```sql
SELECT
    sal,
    sal * 12
FROM emp;
```

## After

```sql
SELECT
    sal,
    sal * 12 AS sal_x_12
FROM emp;
```

계산식의 의미를 Result Header에서 바로 확인할 수 있다.

> [!NOTE]
> Sample Schema는 `SAL`의 지급 주기를 직접 명시하지 않는다. 따라서 `sal * 12`를 무조건 “연봉”이라고 단정하기보다 **12배 계산 예제**로 이해하는 것이 정확하다.

---

# 32. Table 없이 계산

MariaDB에서는 단순 표현식을 Table 없이 조회할 수 있다.

```sql
SELECT 100 * 12;
```

Result:

```text
1200
```

---

# 33. 문자열 상수 조회

```sql
SELECT 'HUMAN';
```

Result:

```text
HUMAN
```

이런 Query는 Function이나 Expression 결과를 빠르게 확인할 때 유용하다.

---

# 34. 여러 표현식 조회

```sql
SELECT
    100 * 12 AS result,
    'HUMAN' AS text_value;
```

Table 없이도 여러 Expression을 Result Set으로 만들 수 있다.

---

# 35. `NULL`

`NULL`은 숫자 `0`이나 빈 문자열이 아니다.

```text
NULL
→ 값이 없거나 알 수 없는 상태
```

`EMP.COMM`에는 여러 `NULL` 값이 존재한다.

---

# 36. `NULL`이 포함된 산술

원본:

```sql
SELECT
    sal,
    comm,
    sal + comm
FROM emp;
```

`COMM`이 `NULL`이면 계산 결과도 `NULL`이 된다.

```text
SAL = 800
COMM = NULL

SAL + COMM
→ NULL
```

---

# 37. 왜 `NULL + 숫자 = NULL`인가?

`NULL`은 “0”이 아니라 **알 수 없는 값**이다.

```text
800 + 알 수 없는 값
→ 결과도 알 수 없음
```

따라서:

```sql
SELECT 10 + NULL;
```

결과는 `NULL`이다.

---

# 38. `COMM = 0`과 `COMM IS NULL`은 다르다

Sample Data의 `TURNER`는 `COMM = 0`이다.

```text
0
→ 값이 실제로 0

NULL
→ 값 자체가 없음 / 알 수 없음
```

이 차이는 추후 `WHERE`, Aggregate Function, `IFNULL`에서 중요하다.

---

# 39. `NULL`을 0처럼 계산하려면

추후 NULL Function 단원에서 자세히 다루지만 예를 들면 다음처럼 처리할 수 있다.

```sql
SELECT
    sal,
    comm,
    sal + IFNULL(comm, 0) AS total
FROM emp;
```

`COMM`이 `NULL`일 때만 계산용으로 `0`을 대신 사용한다.

---

# 40. SQL 문장 끝의 Semicolon

```sql
SELECT *
FROM emp;
```

`;`는 SQL Statement의 끝을 구분한다.

Database Client에서는 한 Statement만 선택 실행할 때 없어도 실행되는 경우가 있지만 여러 Statement를 Script로 실행할 때는 명확하게 작성하는 습관이 좋다.

---

# 41. 내 코드와 강사님 코드 비교

두 `Script.sql`의 초반 학습 순서는 거의 같다.

```text
Comment
→ EMP·DEPT·SALGRADE 조회
→ 상수 계산
→ 특정 Column 조회
→ 여러 Column 조회
→ DISTINCT
→ Alias
→ 산술 계산
→ NULL 산술
```

내 코드는 설명 Comment가 더 많고, 일부 실험 Query가 추가되어 있다.

---

## 41.1 Comment 설명

### 내 코드

```sql
-- 주석
/*
여러 줄 주석
*/
```

### 강사님 코드

```sql
-- 주석
/*
범위 주석
*/
```

개념은 동일하다.

---

## 41.2 Column 설명

내 코드에는 `EMP` Column 의미를 미리 기록해 두었다.

```text
EMPNO : 사원번호
MGR : 상사의 EMPNO
HIREDATE : 고용일
SAL : 연봉
COMM : 보너스
DEPTNO : 부서번호
```

강사님 코드에는 이 상세 Comment가 없다.

다만 `SAL`과 `COMM`은 Schema의 실제 의미에 맞춰 다음처럼 표현하는 편이 더 안전하다.

```text
SAL
→ 급여

COMM
→ Commission
```

---

## 41.3 SELECT 전체 Clause 설명

내 코드에는 다음 전체 구조가 미리 작성되어 있다.

```text
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```

강사님 코드에는 초반부에 해당 전체 문법 설명이 없다.

학습 Roadmap으로는 유용하지만 01번에서는 `SELECT`와 `FROM`만 먼저 확실히 이해하고 나머지는 각 단원에서 자세히 다루는 편이 좋다.

---

## 41.4 `SELECT 100 * 12` 위치

강사님 코드는 Table 조회 직후 다음 계산을 먼저 실행한다.

```sql
SELECT 100 * 12;
```

내 코드는 `SAL * 12` 실습 뒤에 실행한다.

둘 다 같은 기능을 확인한다.

---

## 41.5 `WHERE 1 != 1`

내 코드에는 다음 실험이 추가되어 있다.

```sql
SELECT *
FROM emp
WHERE 1 != 1;
```

강사님 코드에는 없다.

Result Row 없이 Column Header를 확인하는 실험으로는 의미가 있지만 Schema 확인은 다음 명령이 더 직접적이다.

```sql
DESCRIBE emp;
```

---

## 41.6 여러 Column Formatting

강사님 코드는 한 줄 방식과 여러 줄 방식을 모두 보여 준다.

```sql
SELECT empno, ename
FROM emp;
```

```sql
SELECT
    empno,
    ename
FROM emp;
```

내 코드에는 여러 줄 작성이 중심이다.

실무에서는 Column이 많아지면 한 줄에 하나씩 배치하는 형식이 Diff와 Review에 유리하다.

---

## 41.7 `DISTINCT`

두 코드 모두 같은 개념을 실습한다.

```sql
SELECT job
FROM emp;

SELECT DISTINCT job
FROM emp;
```

내 코드의 Comment가 조금 더 상세하다.

---

## 41.8 Alias 차이

내 코드:

```sql
SELECT job AS 직업
FROM emp;

SELECT job AS '직업 이름'
FROM emp;

SELECT job '직업 이름'
FROM emp;
```

강사님 코드:

```sql
SELECT job AS 직업
FROM emp;

SELECT job AS '직업 이름'
FROM emp;

SELECT job 직업
FROM emp;
```

둘 다 `AS` 사용과 생략을 실습한다.

실무 문서에서는 공백 Alias를 사용할 때 다음처럼 Identifier임을 명확하게 표시하는 방식을 권장한다.

```sql
SELECT job AS `직업 이름`
FROM emp;
```

---

## 41.9 산술식

두 코드 모두 다음 Query를 사용한다.

```sql
SELECT
    sal,
    sal * 12
FROM emp;
```

내 코드는 `SELECT 100 * 12`를 이어서 실행해 Table 없이 Expression을 계산할 수 있다는 점도 설명한다.

---

## 41.10 `NULL` 산술

두 코드 모두 다음 Query를 사용한다.

```sql
SELECT
    sal,
    comm,
    sal + comm
FROM emp;
```

`COMM`이 `NULL`이면 결과도 `NULL`이 된다는 중요한 기초 실험이다.

---

## 41.11 원본 비교 요약

| 항목 | 내 코드 | 강사님 코드 | V2 정리 |
| --- | --- | --- | --- |
| Comment | 상세 | 간단 | `--`, `/* */` 구분 |
| EMP Column 설명 | 있음 | 없음 | Schema 기준으로 의미 보완 |
| 전체 SELECT Clause | 미리 설명 | 없음 | 01번은 `SELECT`·`FROM` 중심 |
| `[]` 설명 | 실제 작성 가능한 것처럼 표현 가능 | 없음 | Syntax Diagram의 Optional 표기 |
| Table 확인 | EMP·DEPT·SALGRADE | 동일 | 실습 DB 구조와 연결 |
| `WHERE 1 != 1` | 있음 | 없음 | 탐색 실험, Schema는 `DESCRIBE` 권장 |
| DISTINCT | 있음 | 있음 | 선택 Column 조합 기준 중복 제거 |
| Alias | 상세 | 기본 | Identifier Quote 기준 보완 |
| 산술식 | 있음 | 있음 | 계산 결과 Alias 권장 |
| NULL 산술 | 있음 | 있음 | `NULL`은 0이 아님 |
| SAL 설명 | 연봉 | 직접 설명 없음 | 지급 주기 불명확 → 급여로 표현 |
| IDE Shortcut | 설명 있음 | 없음 | SQL 문법과 Client 기능 구분 |

---

# 42. 개선된 기본 예제

```sql
-- 사원 Table 전체 구조를 확인
DESCRIBE emp;

-- 필요한 Column 조회
SELECT
    empno,
    ename,
    job,
    sal
FROM emp;

-- 직무 종류만 중복 없이 조회
SELECT DISTINCT
    job
FROM emp;

-- Alias 적용
SELECT
    empno AS employee_no,
    ename AS employee_name,
    job AS job_name
FROM emp;

-- 산술식과 Alias
SELECT
    ename,
    sal,
    sal * 12 AS sal_x_12
FROM emp;

-- NULL이 포함된 계산
SELECT
    ename,
    sal,
    comm,
    sal + comm AS sal_plus_comm
FROM emp;
```

---

# 43. 실무 Query Formatting

## Before

```sql
select empno,ename,job,sal from emp;
```

## After

```sql
SELECT
    empno,
    ename,
    job,
    sal
FROM emp;
```

다음 기준을 사용하면 읽기 쉽다.

```text
SQL Keyword
→ 대문자

SELECT Column
→ 한 줄에 하나씩

FROM / WHERE / GROUP BY
→ Clause마다 줄 분리

Alias
→ 의미 있는 이름

Statement
→ ; 로 종료
```

---

# 44. `SELECT *` 리팩토링

## Before

```sql
SELECT *
FROM emp;
```

## After

```sql
SELECT
    empno,
    ename,
    job,
    sal,
    deptno
FROM emp;
```

탐색 단계에서는 `*`가 편하지만 Application Query에서는 필요한 Column을 명시한다.

---

# 45. Alias 리팩토링

## Before

```sql
SELECT
    sal * 12
FROM emp;
```

## After

```sql
SELECT
    sal * 12 AS sal_x_12
FROM emp;
```

Expression에는 의미 있는 Alias를 붙인다.

---

# 46. `NULL` 산술 리팩토링

## Before

```sql
SELECT
    sal + comm
FROM emp;
```

`COMM`이 `NULL`이면 Result도 `NULL`이다.

## After

Business Rule상 `NULL Commission`을 계산에서 0으로 봐야 한다면:

```sql
SELECT
    sal + IFNULL(comm, 0) AS total_amount
FROM emp;
```

단, `NULL`을 0으로 바꾸는 것이 실제 업무 규칙과 맞는지 먼저 확인해야 한다.

---

# 47. 자주 하는 실수

## 47.1 `SELECT *`만 계속 사용

필요한 Column을 명시하는 습관을 들인다.

## 47.2 `DISTINCT`를 성능 문제 해결용으로 무조건 사용

Join이나 Data Model 문제 때문에 중복이 생긴 경우 원인을 먼저 확인한다.

## 47.3 Alias가 실제 Column을 Rename한다고 생각

Alias는 Query Result의 임시 이름이다.

## 47.4 `'직업 이름'`을 모든 DBMS의 Identifier Quote라고 생각

DBMS별 Quote 규칙이 다를 수 있다.

MariaDB의 Identifier는 Backtick을 사용할 수 있다.

## 47.5 `NULL = 0`이라고 생각

`NULL`은 값이 없거나 알 수 없는 상태다.

## 47.6 `SAL * 12`를 Schema 확인 없이 연봉이라고 단정

Sample Schema에 지급 주기 의미가 명확히 정의되어 있는지 확인한다.

## 47.7 Syntax Diagram의 `[]`를 실제 SQL 문자로 작성

문법 문서에서 `[]`는 선택 사항을 나타내는 Meta Notation일 수 있다.

---

# 48. Debugging

Query가 실행되지 않을 때 먼저 확인한다.

```text
1. Table 이름이 맞는가?
2. Column 이름이 맞는가?
3. Comma가 빠지지 않았는가?
4. Quote가 닫혔는가?
5. Statement 끝의 Semicolon이 필요한 상황인가?
6. 현재 Database가 human인가?
7. Alias 문법이 현재 DBMS에서 유효한가?
```

현재 Database 확인:

```sql
SELECT DATABASE();
```

Table 확인:

```sql
SHOW TABLES;
```

Column 확인:

```sql
DESCRIBE emp;
```

---

# 49. 종합실습

다음 문제를 직접 작성한다.

## 문제 1

`EMP` Table의 사원 번호, 이름, 직무만 조회하시오.

출력 Column:

```text
EMPNO
ENAME
JOB
```

---

## 문제 2

`EMP` Table에서 중복되지 않는 부서 번호만 조회하시오.

---

## 문제 3

사원 이름과 급여를 조회하되 Result Header를 다음처럼 표시하시오.

```text
사원이름
급여
```

---

## 문제 4

사원 이름, 급여, 급여의 12배 값을 조회하시오.

12배 값의 Alias는 `sal_x_12`로 작성한다.

---

## 문제 5

`COMM`이 `NULL`인 사원에서 `SAL + COMM`이 어떤 결과가 되는지 직접 확인하고 이유를 설명하시오.

---

## 문제 6

Table 없이 다음 계산 결과를 조회하시오.

```text
250 * 4
```

Alias는 `result`로 작성한다.

---

## 문제 7

`JOB`과 `DEPTNO`의 중복되지 않는 조합을 조회하시오.

---

# 50. 정답과 해설

## 문제 1

```sql
SELECT
    empno,
    ename,
    job
FROM emp;
```

필요한 Column만 선택한다.

---

## 문제 2

```sql
SELECT DISTINCT
    deptno
FROM emp;
```

`DISTINCT`로 중복 부서 번호를 제거한다.

---

## 문제 3

```sql
SELECT
    ename AS `사원이름`,
    sal AS `급여`
FROM emp;
```

Alias는 Result Header만 변경한다.

---

## 문제 4

```sql
SELECT
    ename,
    sal,
    sal * 12 AS sal_x_12
FROM emp;
```

`SELECT` List에서 Column을 이용한 산술식을 작성할 수 있다.

---

## 문제 5

```sql
SELECT
    ename,
    sal,
    comm,
    sal + comm AS result
FROM emp;
```

`COMM`이 `NULL`인 Row의 Result는 `NULL`이다.

```text
숫자 + 알 수 없는 값
→ 결과도 알 수 없음
```

---

## 문제 6

```sql
SELECT
    250 * 4 AS result;
```

Table 없이 Expression을 계산할 수 있다.

---

## 문제 7

```sql
SELECT DISTINCT
    job,
    deptno
FROM emp;
```

`DISTINCT`는 `(JOB, DEPTNO)` 전체 조합을 기준으로 중복을 제거한다.

---

# 51. 최종 체크리스트

- [ ] SQL과 Query의 기본 역할을 설명할 수 있는가?
- [ ] `--` 한 줄 Comment를 작성할 수 있는가?
- [ ] `/* ... */` 여러 줄 Comment를 작성할 수 있는가?
- [ ] `SELECT`와 `FROM`의 역할을 구분할 수 있는가?
- [ ] `SELECT *`의 의미를 설명할 수 있는가?
- [ ] 필요한 Column만 선택할 수 있는가?
- [ ] 여러 Column을 `,`로 나열할 수 있는가?
- [ ] SQL Keyword와 Identifier를 구분해 읽을 수 있는가?
- [ ] `EMP`, `DEPT`, `SALGRADE`, `BONUS`의 역할을 구분할 수 있는가?
- [ ] `EMP.EMPNO`가 Primary Key임을 알고 있는가?
- [ ] `EMP.DEPTNO`가 `DEPT.DEPTNO`를 참조함을 이해하는가?
- [ ] `SALGRADE`가 범위 조건으로 활용되는 Table임을 이해하는가?
- [ ] `DISTINCT`가 중복 Row 조합을 제거한다는 점을 설명할 수 있는가?
- [ ] `ALL`이 기본 동작임을 이해하는가?
- [ ] Alias가 실제 Schema를 변경하지 않는다는 점을 아는가?
- [ ] 공백 Alias의 Quote 방식을 구분할 수 있는가?
- [ ] `SELECT` List에서 산술식을 사용할 수 있는가?
- [ ] 계산 결과에 의미 있는 Alias를 붙일 수 있는가?
- [ ] Table 없이 상수와 Expression을 조회할 수 있는가?
- [ ] `NULL`이 0과 다르다는 점을 설명할 수 있는가?
- [ ] `NULL`이 포함된 산술 결과가 `NULL`이 되는 이유를 이해하는가?
- [ ] Syntax Diagram의 `[]`를 실제 Query 문법과 구분할 수 있는가?
- [ ] IDE Shortcut과 SQL 문법을 구분할 수 있는가?
- [ ] `DESCRIBE emp`로 Schema를 확인할 수 있는가?
- [ ] 실무 Query에서 필요한 Column을 명시하는 습관을 이해하는가?
- [ ] SQL Statement 끝에 Semicolon을 일관되게 작성하는가?

---

# 52. 핵심 요약

```text
SELECT
→ 조회할 Column 또는 Expression 지정

FROM
→ 조회할 Table 지정
```

```text
*
→ 모든 Column

Column List
→ 필요한 Column만 조회
```

```text
DISTINCT
→ 선택된 Column 조합의 중복 제거
```

```text
AS
→ Result Column Alias
→ 실제 Schema는 변경하지 않음
```

```text
SELECT sal * 12
→ Column 기반 계산

SELECT 100 * 12
→ Table 없는 Expression 계산
```

```text
NULL
→ 0이 아님
→ 값이 없거나 알 수 없는 상태

숫자 + NULL
→ NULL
```

```text
EMP
→ 사원

DEPT
→ 부서

SALGRADE
→ 급여 범위 등급

BONUS
→ Bonus 실습 Table
```

---

# 마무리

SQL의 첫 단계에서 가장 중요한 것은 복잡한 문법을 외우는 것이 아니다.

```text
어느 Table에서
    ↓
어떤 Column을
    ↓
어떤 형태로 조회할 것인지
```

를 명확하게 표현하는 것이다.

`SELECT`와 `FROM`, 필요한 Column 선택, `DISTINCT`, Alias, Expression과 `NULL`의 기본 동작을 정확히 이해하면 이후 `WHERE`, Function, Grouping, Subquery, JOIN으로 자연스럽게 확장할 수 있다.
