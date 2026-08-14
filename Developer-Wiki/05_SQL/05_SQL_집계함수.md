---
title: SQL 집계함수
version: v2.0-final
last_updated: 2026-08-13
status: Completed
---

# SQL 집계함수

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `05_SQL_집계함수.md` |
| 분류 | `05_SQL` |
| 원본 기준 | `workspace_sql/Script.sql`, `workspace_teacher/workspace_sql/Script.sql` |
| DB 기준 자료 | `[DB]학습용_emp 신규-mariadb.sql` |
| DBMS | MariaDB |
| 핵심 범위 | `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, `DISTINCT`, `NULL`과 집계 |
| 다음 범위 제외 | 문자열·숫자·날짜 Function, `GROUP BY`, `HAVING` |
| 문서 형식 | SQL Developer-Wiki V2 확정 형식 |

> 여러 Row를 하나의 요약 결과로 계산하는 집계함수를 정리한다. 특히 `COUNT(*)`와 `COUNT(column)`, `NULL`, `DISTINCT`의 차이를 정확하게 구분한다.

# 학습 목표

- `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`을 사용할 수 있다.
- 집계함수와 `NULL`의 관계를 설명할 수 있다.
- `COUNT(*)`, `COUNT(column)`, `COUNT(DISTINCT column)`을 구분할 수 있다.
- Filtering 후 집계하는 흐름을 이해할 수 있다.
- Aggregate와 일반 Column을 함께 조회할 때 Grouping이 필요한 이유를 이해할 수 있다.

---

# 1. 집계함수란?

집계함수(Aggregate Function)는 여러 Row의 값을 하나의 요약값으로 계산한다.

```text
COUNT → 개수
SUM   → 합계
AVG   → 평균
MAX   → 최댓값
MIN   → 최솟값
```

---

# 2. 일반 SELECT와 집계 SELECT

일반 조회는 여러 Row를 반환하지만 집계는 여러 Row를 요약한다.

```sql
SELECT sal FROM emp;

SELECT AVG(sal) AS avg_sal
FROM emp;
```

---

# 3. COUNT(*)

전체 Row 수를 센다.

```sql
SELECT COUNT(*) AS employee_count
FROM emp;
```

`COUNT(*)`는 특정 Column의 NULL 여부와 관계없이 Result Row 자체를 센다.

---

# 4. COUNT(column)

특정 Column에서 `NULL`이 아닌 값의 개수를 센다.

```sql
SELECT COUNT(comm) AS commission_count
FROM emp;
```

---

# 5. COUNT(*)와 COUNT(column)

두 표현의 차이는 매우 중요하다.

```sql
SELECT
    COUNT(*) AS total_rows,
    COUNT(comm) AS comm_rows
FROM emp;
```

`COUNT(*)`는 전체 Row, `COUNT(comm)`은 `COMM IS NOT NULL`인 Row를 센다.

---

# 6. 0과 NULL의 COUNT 차이

`0`은 실제 값이므로 Count에 포함되지만 `NULL`은 `COUNT(column)`에서 제외된다.

```text
COMM = 0    → COUNT(comm)에 포함
COMM = NULL → COUNT(comm)에서 제외
```

---

# 7. COUNT(DISTINCT column)

중복을 제거한 값의 개수를 센다.

```sql
SELECT COUNT(DISTINCT job) AS job_type_count
FROM emp;
```

`NULL`은 제외되고 중복된 `JOB`도 하나로 계산된다.

---

# 8. DISTINCT 조회와 COUNT 비교

직무 종류 자체가 필요하면:

```sql
SELECT DISTINCT job
FROM emp;
```

직무 종류의 **개수**가 필요하면:

```sql
SELECT COUNT(DISTINCT job)
FROM emp;
```

---

# 9. SUM

숫자 값의 합계를 계산한다.

```sql
SELECT SUM(sal) AS total_sal
FROM emp;
```

---

# 10. SUM과 NULL

`SUM(column)`은 일반적으로 `NULL`을 제외하고 실제 값만 합산한다.

```sql
SELECT SUM(comm) AS total_comm
FROM emp;
```

이는 Row 단위의 `sal + comm`에서 `comm`이 NULL이면 결과가 NULL이 되는 것과 다르다.

---

# 11. AVG

평균을 계산한다.

```sql
SELECT AVG(sal) AS avg_sal
FROM emp;
```

개념적으로 `NULL`이 아닌 값의 합계 ÷ `NULL`이 아닌 값의 개수다.

---

# 12. AVG와 NULL

`COMM`이 NULL인 Row는 평균 계산 대상에서 제외된다.

```sql
SELECT AVG(comm) AS avg_comm
FROM emp;
```

따라서 이 값은 모든 사원을 분모로 한 평균이라고 단정하면 안 된다.

---

# 13. AVG(IFNULL(...))

다음 두 Query는 결과가 달라질 수 있다.

```sql
SELECT AVG(comm) FROM emp;
SELECT AVG(IFNULL(comm, 0)) FROM emp;
```

첫 번째는 NULL을 제외하고, 두 번째는 NULL을 0으로 바꾸어 평균에 포함한다.

---

# 14. NULL을 0으로 바꿀 때

기술적으로 가능하더라도 Business Rule을 먼저 확인한다.

```text
NULL → Commission 정보가 없거나 알 수 없음
0    → Commission 값이 실제로 0
```

둘은 의미가 다를 수 있다.

---

# 15. MAX

최댓값을 구한다.

```sql
SELECT MAX(sal) AS max_sal
FROM emp;
```

---

# 16. MIN

최솟값을 구한다.

```sql
SELECT MIN(sal) AS min_sal
FROM emp;
```

---

# 17. MAX와 MIN 함께 조회

한 Query에서 여러 집계 결과를 계산할 수 있다.

```sql
SELECT
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal
FROM emp;
```

---

# 18. 여러 집계함수 함께 사용

```sql
SELECT
    COUNT(*) AS employee_count,
    SUM(sal) AS total_sal,
    AVG(sal) AS avg_sal,
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal
FROM emp;
```

EMP 전체의 요약 정보를 한 Row로 확인할 수 있다.

---

# 19. WHERE와 집계함수

`WHERE`로 먼저 Row를 제한한 뒤 집계한다.

```sql
SELECT AVG(sal) AS avg_sal
FROM emp
WHERE deptno = 20;
```

```text
EMP → WHERE Filtering → Aggregate
```

---

# 20. 부서별 조건 집계의 기초

아직 `GROUP BY`를 사용하지 않고 특정 부서 하나만 조건으로 집계할 수 있다.

```sql
SELECT COUNT(*) AS employee_count
FROM emp
WHERE deptno = 30;
```

---

# 21. 조건과 MAX

CLERK 중 최고 급여:

```sql
SELECT MAX(sal) AS max_sal
FROM emp
WHERE job = 'CLERK';
```

---

# 22. 조건과 AVG

급여가 2000 이상인 사원의 평균:

```sql
SELECT AVG(sal) AS avg_sal
FROM emp
WHERE sal >= 2000;
```

---

# 23. 집계 결과는 원본 Row가 아니다

```sql
SELECT MAX(sal)
FROM emp;
```

이 Query는 **최고 급여 값**을 반환한다. 최고 급여를 받는 사원의 이름이나 전체 Row를 반환하는 것은 아니다.

---

# 24. 최고 급여 사원 이름의 함정

다음 Query는 의도가 명확하지 않다.

```sql
SELECT
    ename,
    MAX(sal)
FROM emp;
```

`MAX(sal)`은 전체를 집계하지만 `ENAME`은 어느 Row의 값인지 정의되지 않는다.

---

# 25. ONLY_FULL_GROUP_BY

MariaDB/MySQL 계열은 SQL Mode에 따라 잘못된 Grouping Query 검사가 달라질 수 있다.

```sql
SELECT @@sql_mode;
```

`ONLY_FULL_GROUP_BY`가 활성화된 환경에서는 집계되지 않은 일반 Column을 무분별하게 함께 SELECT하는 Query가 제한된다.

---

# 26. Aggregate와 일반 Column

부서별 평균을 원한다면 Grouping 기준이 필요하다.

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno;
```

`GROUP BY`는 이후 전용 단원에서 자세히 다룬다.

---

# 27. 집계함수는 SELECT에서만 사용하는가?

아니다. 적절한 문맥에서는 `HAVING`, `ORDER BY` 등에서도 사용할 수 있다.

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
ORDER BY AVG(sal) DESC;
```

“집계함수는 SELECT에서만 사용한다”라고 일반화하면 부정확하다.

---

# 28. COUNT(1)

다음 형태도 볼 수 있다.

```sql
SELECT COUNT(1)
FROM emp;
```

전체 Row Count 목적이라면 `COUNT(*)`가 의도를 가장 직접적으로 표현한다.

---

# 29. COUNT(*)와 성능 오해

`COUNT(1)`이 항상 `COUNT(*)`보다 빠르다고 단정하지 않는다. 현대 DBMS Optimizer가 표현을 적절히 처리할 수 있으므로 실제 성능은 DBMS·Storage Engine·실행계획으로 확인한다.

---

# 30. COUNT(DISTINCT deptno)

```sql
SELECT COUNT(DISTINCT deptno)
FROM emp;
```

EMP에 **실제로 사원이 존재하는 서로 다른 부서 번호의 개수**를 센다.

---

# 31. EMP의 부서 수와 DEPT의 부서 수

다음 두 값은 의미가 다르다.

```sql
SELECT COUNT(DISTINCT deptno) FROM emp;
SELECT COUNT(*) FROM dept;
```

첫 번째는 사원이 있는 부서 종류 수, 두 번째는 DEPT에 등록된 전체 부서 수다.

---

# 32. 날짜의 MIN과 MAX

`MIN`, `MAX`는 숫자에만 사용하는 함수가 아니다.

```sql
SELECT
    MIN(hiredate) AS first_hiredate,
    MAX(hiredate) AS last_hiredate
FROM emp;
```

가장 이른 입사일과 가장 늦은 입사일을 구할 수 있다.

---

# 33. 문자열의 MIN과 MAX

문자열도 Collation 기준으로 비교할 수 있다.

```sql
SELECT
    MIN(ename),
    MAX(ename)
FROM emp;
```

다만 문자열의 최소·최대가 업무적으로 의미 있는지 확인한다.

---

# 34. Aggregate와 DISTINCT

함수 내부에 `DISTINCT`를 사용할 수 있다.

```sql
SELECT AVG(DISTINCT sal)
FROM emp;
```

중복 급여 값을 제거한 뒤 평균을 계산하므로 일반 평균과 의미가 다르다.

---

# 35. AVG와 AVG DISTINCT

```sql
SELECT AVG(sal) FROM emp;
SELECT AVG(DISTINCT sal) FROM emp;
```

첫 번째는 모든 사원의 급여를 평균내고, 두 번째는 중복된 급여 값을 제거한 뒤 평균낸다. 요구사항 없이 임의로 `DISTINCT`를 추가하지 않는다.

---

# 36. 집계 결과끼리 계산

```sql
SELECT
    MAX(sal) - MIN(sal) AS sal_diff
FROM emp;
```

최고 급여와 최저 급여의 차이를 바로 계산할 수 있다.

---

# 37. Expression 집계

Column뿐 아니라 Expression도 집계할 수 있다.

```sql
SELECT AVG(sal * 12) AS avg_sal_x_12
FROM emp;
```

---

# 38. 전체가 NULL인 경우

`SUM`, `AVG`, `MAX`, `MIN`은 NULL을 무시하지만, 집계 대상에 **NULL이 아닌 값이 하나도 없다면** 결과가 NULL이 될 수 있다.

```sql
SELECT AVG(comm)
FROM emp
WHERE 1 = 0;
```

“NULL을 무시한다 = 항상 숫자가 나온다”는 뜻은 아니다.

---

# 39. COUNT와 빈 Result

Row가 하나도 없어도 `COUNT(*)`는 0을 반환한다.

```sql
SELECT COUNT(*)
FROM emp
WHERE 1 = 0;
```

반면 같은 조건에서 `AVG(sal)` 등은 NULL이 될 수 있다.

---

# 40. 집계와 ORDER BY 연결

04번의 정렬과 결합할 수 있다.

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
ORDER BY avg_sal DESC;
```

Alias를 사용하면 집계 Expression을 반복하지 않아 읽기 쉽다.

---

# 41. 내 코드와 강사님 코드 비교

두 원본은 대체로 `COUNT → SUM → AVG → MAX → MIN → NULL과 집계` 흐름으로 진행한다.

| 항목 | 내 코드 | 강사님 코드 | V2 정리 |
| --- | --- | --- | --- |
| COUNT | 실습·Comment 상세 | 기본 문법 | Row Count |
| COUNT(column) | NULL 실험 | 기본 흐름 | NULL 제외 |
| SUM | 있음 | 있음 | 합계 |
| AVG | 있음 | 있음 | NULL 제외 평균 |
| MAX/MIN | 있음 | 있음 | 최댓값·최솟값 |
| DISTINCT | 추가 실험 가능 | 기본 범위 | 집계 의미 변화 |
| 일반 Column 혼합 | 시행착오 가능 | GROUP BY 연결 | SQL Mode 주의 |
| NULL | Comment 중심 | 기본 설명 | 함수별 차이 명확화 |

V2에서는 원본 흐름을 유지하면서 `COUNT(*)`와 `COUNT(column)`, `DISTINCT`, SQL Mode, 전체 NULL 집계까지 보완한다.

---

# 42. 개선된 통합 예제

```sql
-- 전체 사원 수
SELECT COUNT(*) AS employee_count
FROM emp;

-- Commission 값이 있는 사원 수
SELECT COUNT(comm) AS commission_count
FROM emp;

-- 직무 종류 수
SELECT COUNT(DISTINCT job) AS job_type_count
FROM emp;

-- 급여 요약
SELECT
    SUM(sal) AS total_sal,
    AVG(sal) AS avg_sal,
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal
FROM emp;

-- 부서 30의 급여 요약
SELECT
    COUNT(*) AS employee_count,
    AVG(sal) AS avg_sal
FROM emp
WHERE deptno = 30;
```

---

# 43. 실무 집계 기준

```text
전체 Row 수               → COUNT(*)
특정 Column의 값 존재 수  → COUNT(column)
서로 다른 값 개수         → COUNT(DISTINCT column)
합계                       → SUM
평균                       → AVG
최댓값 / 최솟값            → MAX / MIN
```

항상 `NULL`과 Business Meaning을 함께 확인한다.

---

# 44. COUNT 리팩토링

전체 Row 수가 목적이라면 다음이 가장 직접적이다.

```sql
SELECT COUNT(*) AS employee_count
FROM emp;
```

PK인 `EMPNO`를 `COUNT(empno)`해도 현재 결과는 같을 수 있지만 “전체 Row 수”라는 의도는 `COUNT(*)`가 더 명확하다.

---

# 45. NULL 평균 리팩토링

`AVG(comm)`이 틀린 것은 아니다. 다만 “모든 사원의 평균 Commission이며 NULL은 0”이라는 요구사항이라면:

```sql
SELECT AVG(IFNULL(comm, 0)) AS avg_comm
FROM emp;
```

업무 규칙이 실제로 `NULL → 0`일 때만 사용한다.

---

# 46. 집계 Alias 리팩토링

## Before

```sql
SELECT COUNT(*), AVG(sal), MAX(sal)
FROM emp;
```

## After

```sql
SELECT
    COUNT(*) AS employee_count,
    AVG(sal) AS avg_sal,
    MAX(sal) AS max_sal
FROM emp;
```

Result의 의미가 바로 보인다.

---

# 47. 자주 하는 실수

- `COUNT(*)`가 NULL Row를 제외한다고 생각한다.
- `COUNT(comm)`을 전체 사원 수라고 생각한다.
- `AVG`가 NULL을 자동으로 0으로 바꾼다고 생각한다.
- 이유 없이 `AVG(IFNULL(..., 0))`을 사용한다.
- `MAX(sal)`이 최고 급여 사원의 전체 Row를 반환한다고 생각한다.
- Aggregate와 일반 Column을 Grouping 없이 섞는다.
- `COUNT(1)`이 항상 더 빠르다고 단정한다.
- `DISTINCT`를 습관적으로 넣어 집계 의미를 바꾼다.

---

# 48. Debugging

집계 결과가 예상과 다르면 확인한다.

```text
1. COUNT(*)인가 COUNT(column)인가?
2. 집계 Column에 NULL이 있는가?
3. DISTINCT를 사용했는가?
4. WHERE에서 먼저 제외된 Row가 있는가?
5. NULL을 0으로 바꾸는 것이 업무 규칙인가?
6. 일반 Column과 Aggregate를 함께 SELECT했는가?
7. GROUP BY가 필요한가?
8. ONLY_FULL_GROUP_BY 설정은 어떤가?
9. MAX/MIN 값과 해당 Row 정보를 혼동하지 않았는가?
```

---

# 49. 종합실습

1. EMP 전체 사원 수를 조회하시오.
2. Commission 값이 존재하는 사원 수를 조회하시오.
3. 서로 다른 직무의 개수를 조회하시오.
4. 전체 급여 합계와 평균을 조회하시오.
5. 최고 급여와 최저 급여를 조회하시오.
6. 부서 30의 사원 수와 평균 급여를 조회하시오.
7. 최고 급여와 최저 급여의 차이를 `sal_diff`로 조회하시오.
8. `AVG(comm)`과 `AVG(IFNULL(comm, 0))`의 차이를 설명하시오.
9. `SELECT ename, MAX(sal) FROM emp;`가 최고 급여 사원 이름을 정확히 구하는 Query가 아닌 이유를 설명하시오.

---

# 50. 정답과 해설

```sql
-- 1
SELECT COUNT(*) AS employee_count FROM emp;

-- 2
SELECT COUNT(comm) AS commission_count FROM emp;

-- 3
SELECT COUNT(DISTINCT job) AS job_type_count FROM emp;

-- 4
SELECT
    SUM(sal) AS total_sal,
    AVG(sal) AS avg_sal
FROM emp;

-- 5
SELECT
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal
FROM emp;

-- 6
SELECT
    COUNT(*) AS employee_count,
    AVG(sal) AS avg_sal
FROM emp
WHERE deptno = 30;

-- 7
SELECT
    MAX(sal) - MIN(sal) AS sal_diff
FROM emp;
```

8번은 첫 Query가 NULL을 제외하고, 두 번째 Query는 NULL을 0으로 바꾸어 평균에 포함하므로 분모와 합계가 달라질 수 있다.

9번은 `MAX(sal)`이 전체 Row를 집계하는 반면 `ENAME`은 어느 Row의 값을 선택할지 정의하지 않았기 때문이다. 최고 급여 사원 정보는 이후 Subquery 등으로 정확하게 구한다.

---

# 51. 최종 체크리스트

- [ ] `COUNT(*)`와 `COUNT(column)`의 차이를 설명할 수 있는가?
- [ ] `COUNT(DISTINCT column)`을 사용할 수 있는가?
- [ ] `SUM`, `AVG`, `MAX`, `MIN`을 사용할 수 있는가?
- [ ] 집계함수가 일반적으로 NULL을 제외함을 이해하는가?
- [ ] 0과 NULL의 차이를 집계 관점에서 설명할 수 있는가?
- [ ] `AVG(comm)`과 `AVG(IFNULL(comm, 0))`의 차이를 아는가?
- [ ] WHERE Filtering 후 집계할 수 있는가?
- [ ] `MAX(sal)`이 최고 급여 사원의 전체 Row가 아님을 아는가?
- [ ] Aggregate와 일반 Column 혼합 시 Grouping을 고려하는가?
- [ ] `ONLY_FULL_GROUP_BY`가 관련될 수 있음을 아는가?
- [ ] `COUNT(1)`이 항상 더 빠르다고 단정하지 않는가?
- [ ] `DISTINCT`가 집계 의미를 바꿀 수 있음을 이해하는가?
- [ ] 날짜에도 MIN/MAX를 사용할 수 있는가?
- [ ] 빈 Result에서 COUNT와 다른 Aggregate의 차이를 이해하는가?
- [ ] 집계 결과에 의미 있는 Alias를 붙일 수 있는가?

---

# 52. 핵심 요약

```text
COUNT(*)                  → 전체 Row
COUNT(column)             → NULL이 아닌 값
COUNT(DISTINCT column)    → NULL 제외 + 중복 제거

SUM → 합계
AVG → 평균
MAX → 최댓값
MIN → 최솟값

AVG(comm)
→ NULL 제외

AVG(IFNULL(comm, 0))
→ NULL을 0으로 포함
→ 의미가 달라질 수 있음

WHERE
→ 먼저 Row Filtering
→ 그 결과를 Aggregate

MAX(sal)
→ 최고 급여 값
→ 최고 급여 사원의 전체 정보는 아님
```

---

# 마무리

집계함수의 핵심은 함수 이름을 외우는 것이 아니라 **어떤 Row와 어떤 값을 계산 대상으로 삼는지** 이해하는 것이다.

```text
WHERE로 대상 Row 결정
    ↓
COUNT / SUM / AVG / MAX / MIN 선택
    ↓
NULL 처리 확인
    ↓
DISTINCT 필요 여부 판단
    ↓
집계 결과의 업무 의미 해석
```

이 기준을 이해하면 이후 `GROUP BY`에서 부서별·직무별처럼 Group을 나누어 집계하는 Query로 자연스럽게 확장할 수 있다.
