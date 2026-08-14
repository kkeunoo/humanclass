# 11. SQL 서브쿼리

> 하나의 SQL 안에 다른 SELECT를 포함하여 동적인 조건과 중간 결과를 만드는 방법

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | Subquery, Scalar Subquery, Multi-row Subquery, Correlated Subquery, Derived Table |
| 기준 DBMS | MariaDB |
| 실습 테이블 | `EMP`, `DEPT`, `SALGRADE` |
| 선수 학습 | `SELECT`, `WHERE`, 집계함수, `GROUP BY`, `HAVING`, `UNION` |
| 다음 학습 | JOIN |
| 문서 버전 | V2 |

> 원본 `Script.sql`에서 `UNION / UNION ALL` 다음에 이어지는 Subquery 범위를 기준으로 구성했다. 수업 예제를 보존하면서 “Subquery는 한 행만 반환해야 한다” 같은 과도한 일반화는 Scalar Subquery에만 해당하도록 바로잡았다.

---

## 🎯 학습 목표

- Subquery와 Main Query의 역할을 구분한다.
- Scalar·다중 행·다중 Column Subquery의 반환 형태를 설명한다.
- `=`, `IN`, `ANY`, `ALL`, `EXISTS`를 결과 형태에 맞게 선택한다.
- 상관 Subquery와 비상관 Subquery의 실행 논리를 구분한다.
- `FROM`절 Derived Table에 Alias를 지정하고 중간 집계를 활용한다.
- `NULL`, 다중 행 오류, 불필요한 중첩을 단계적으로 디버깅한다.

---

## 1. Subquery 기본 개념

### 1. Query 안의 Query

Subquery는 다른 SQL 문 안에 포함된 `SELECT`이다.

```sql
SELECT empno, ename, sal
FROM emp
WHERE sal > (
    SELECT AVG(sal)
    FROM emp
);
```

안쪽 Query가 평균 급여를 구하고, 바깥 Query가 그 값보다 급여가 높은 사원을 조회한다.

### 2. Main Query와 Subquery

```text
Subquery
→ 비교 기준이나 중간 결과를 만든다.

Main Query
→ Subquery 결과를 사용해 최종 Row와 Column을 결정한다.
```

### 3. 괄호로 감싼다

```sql
SELECT ename
FROM emp
WHERE deptno = (
    SELECT deptno
    FROM dept
    WHERE dname = 'SALES'
);
```

### 4. 안쪽부터 독립 실행해 본다

```sql
SELECT deptno
FROM dept
WHERE dname = 'SALES';
```

Subquery가 무엇을 몇 행 반환하는지 먼저 확인하면 전체 Query를 이해하기 쉽다.

### 5. 고정값 대신 Data에서 기준을 구한다

```sql
-- 고정값에 의존
SELECT ename, sal
FROM emp
WHERE sal > 2000;

-- 현재 Data의 평균을 기준으로 사용
SELECT ename, sal
FROM emp
WHERE sal > (SELECT AVG(sal) FROM emp);
```

---

## 2. 반환 형태로 분류하기

### 6. Subquery는 여러 형태의 결과를 반환할 수 있다

| 형태 | 행 수 | Column 수 | 대표 사용처 |
|---|---:|---:|---|
| Scalar | 0 또는 1 | 1 | 비교식, SELECT 표현식 |
| 단일 행 다중 Column | 0 또는 1 | 여러 개 | Row 비교 |
| 다중 행 단일 Column | 여러 개 | `IN`, `ANY`, `ALL` |
| Table 형태 | 여러 개 | 여러 개 | `FROM`의 Derived Table |

### 7. 모든 Subquery가 한 행만 반환해야 하는 것은 아니다

한 행 제한은 단일 값이 필요한 Scalar 문맥의 규칙이다. `IN`, `EXISTS`, Derived Table은 여러 행을 정상적으로 처리한다.

### 8. 연산자가 기대하는 결과 형태를 확인한다

```text
=, >, <
→ 보통 단일 값

IN, ANY, ALL
→ 여러 값 가능

EXISTS
→ Row 존재 여부

FROM (Subquery)
→ Table 형태
```

---

## 3. Scalar Subquery

### 9. Scalar Subquery는 1행 1열의 단일 값이다

```sql
SELECT ename, sal
FROM emp
WHERE sal = (
    SELECT MAX(sal)
    FROM emp
);
```

`MAX(sal)`은 항상 한 개의 집계 결과를 반환하므로 Scalar 문맥에 적합하다.

### 10. SELECT 목록에서도 사용할 수 있다

```sql
SELECT
    empno,
    ename,
    sal,
    (SELECT ROUND(AVG(sal), 2) FROM emp) AS company_avg_sal
FROM emp;
```

### 11. 0행이면 NULL이 된다

```sql
SELECT (
    SELECT deptno
    FROM dept
    WHERE dname = 'NOT_EXISTS'
) AS result;
```

Scalar Subquery가 Row를 반환하지 않으면 오류가 아니라 `NULL`이 된다.

### 12. 2행 이상이면 오류가 발생한다

```sql
-- 여러 부서 번호가 반환될 수 있어 Scalar 비교에 부적합
-- SELECT ename
-- FROM emp
-- WHERE deptno = (SELECT deptno FROM dept);
```

MariaDB에서는 `Subquery returns more than 1 row` 오류가 발생한다.

### 13. 단일 행을 보장하는 기준이 필요하다

```sql
SELECT ename
FROM emp
WHERE deptno = (
    SELECT deptno
    FROM dept
    WHERE dname = 'SALES'
);
```

`DNAME`이 유일하다는 Schema 보장이 없다면 결과가 여러 행일 가능성도 검토해야 한다.

### 14. LIMIT 1로 문제를 숨기지 않는다

```sql
-- 어떤 Row가 선택되는지 명확하지 않으면 위험하다.
-- SELECT deptno FROM dept WHERE loc IS NOT NULL LIMIT 1
```

정말 한 Row만 필요한 이유와 정렬 기준이 있을 때만 `ORDER BY ... LIMIT 1`을 사용한다.

---

## 4. 다중 행 Subquery와 IN

### 15. 여러 값 중 하나와 일치하는지 검사한다

```sql
SELECT empno, ename, deptno
FROM emp
WHERE deptno IN (
    SELECT deptno
    FROM dept
    WHERE loc IN ('DALLAS', 'CHICAGO')
);
```

### 16. `IN (Subquery)`는 한 Column을 반환해야 한다

```sql
-- 오류: IN 왼쪽은 한 값인데 Subquery는 두 Column
-- WHERE deptno IN (SELECT deptno, dname FROM dept)
```

### 17. `IN`은 `= ANY`와 논리적으로 연결된다

```sql
SELECT ename, deptno
FROM emp
WHERE deptno = ANY (
    SELECT deptno
    FROM dept
    WHERE loc IN ('DALLAS', 'CHICAGO')
);
```

동등 비교 목록에는 일반적으로 `IN`이 더 읽기 쉽다.

### 18. Subquery가 0행이면 IN은 일치하지 않는다

```sql
SELECT ename
FROM emp
WHERE deptno IN (
    SELECT deptno
    FROM dept
    WHERE loc = 'NOT_EXISTS'
);
```

### 19. NOT IN과 NULL을 주의한다

```sql
SELECT ename, deptno
FROM emp
WHERE deptno NOT IN (
    SELECT deptno
    FROM dept
    WHERE deptno IS NOT NULL
);
```

Subquery 결과에 `NULL`이 섞이면 `NOT IN` 비교가 Unknown이 되어 예상과 달리 Row가 반환되지 않을 수 있다.

### 20. NULL 가능성이 있으면 NOT EXISTS를 검토한다

```sql
SELECT e.empno, e.ename, e.deptno
FROM emp AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM dept AS d
    WHERE d.deptno = e.deptno
);
```

---

## 5. ANY와 ALL

### 21. ANY는 하나라도 조건을 만족하면 True다

```sql
SELECT ename, sal
FROM emp
WHERE sal > ANY (
    SELECT sal
    FROM emp
    WHERE deptno = 30
);
```

30번 부서의 급여 중 적어도 하나보다 높은 사원을 조회한다.

### 22. ALL은 모든 값에 대해 조건을 만족해야 한다

```sql
SELECT ename, sal
FROM emp
WHERE sal > ALL (
    SELECT sal
    FROM emp
    WHERE deptno = 30
);
```

30번 부서의 모든 급여보다 높은 사원을 조회한다.

### 23. `> ALL`과 MAX의 관계

```sql
SELECT ename, sal
FROM emp
WHERE sal > (
    SELECT MAX(sal)
    FROM emp
    WHERE deptno = 30
);
```

Subquery가 비어 있지 않고 비교값에 `NULL`이 없다는 전제에서는 `> ALL`과 유사하게 해석할 수 있다. 빈 집합과 NULL의 논리는 다를 수 있으므로 무조건 같은 식으로 치환하지 않는다.

### 24. `< ALL`은 모든 값보다 작다는 뜻이다

```sql
SELECT ename, sal
FROM emp
WHERE sal < ALL (
    SELECT sal
    FROM emp
    WHERE job = 'MANAGER'
);
```

### 25. ANY와 ALL은 자연어로 먼저 읽는다

```text
> ANY
→ 하나보다만 커도 된다.

> ALL
→ 전부보다 커야 한다.
```

---

## 6. EXISTS와 NOT EXISTS

### 26. EXISTS는 Row 존재 여부만 검사한다

```sql
SELECT d.deptno, d.dname
FROM dept AS d
WHERE EXISTS (
    SELECT 1
    FROM emp AS e
    WHERE e.deptno = d.deptno
);
```

소속 사원이 한 명이라도 있는 부서만 조회한다.

### 27. SELECT 목록의 값은 중요하지 않다

`EXISTS`는 Subquery가 Row를 반환하는지만 확인하므로 `SELECT 1`, `SELECT *`, `SELECT e.empno`는 존재 판정 관점에서 같은 의미다.

### 28. NOT EXISTS는 일치하는 Row가 없어야 True다

```sql
SELECT d.deptno, d.dname
FROM dept AS d
WHERE NOT EXISTS (
    SELECT 1
    FROM emp AS e
    WHERE e.deptno = d.deptno
);
```

### 29. EXISTS는 상관 조건과 자주 사용한다

안쪽 Query의 `d.deptno`가 바깥 Query의 현재 부서 Row를 참조한다.

### 30. 존재 여부가 목적이면 불필요한 집계를 하지 않는다

```sql
-- 존재 여부를 직접 표현
SELECT d.deptno, d.dname
FROM dept AS d
WHERE EXISTS (
    SELECT 1
    FROM emp AS e
    WHERE e.deptno = d.deptno
      AND e.sal >= 3000
);
```

---

## 7. Correlated Subquery

### 31. 바깥 Row를 참조하는 Subquery

```sql
SELECT e.empno, e.ename, e.deptno, e.sal
FROM emp AS e
WHERE e.sal > (
    SELECT AVG(e2.sal)
    FROM emp AS e2
    WHERE e2.deptno = e.deptno
);
```

각 사원의 급여를 그 사원이 속한 부서의 평균과 비교한다.

### 32. Alias로 범위를 명확히 한다

```text
e
→ Main Query의 현재 사원

e2
→ Subquery에서 평균을 계산할 사원 집합
```

### 33. 비상관 Subquery와 차이

```sql
-- 전체 평균: 바깥 Row를 참조하지 않음
SELECT ename, sal
FROM emp
WHERE sal > (SELECT AVG(sal) FROM emp);
```

```sql
-- 부서 평균: 바깥 Row의 deptno를 참조
SELECT e.ename, e.sal
FROM emp AS e
WHERE e.sal > (
    SELECT AVG(e2.sal)
    FROM emp AS e2
    WHERE e2.deptno = e.deptno
);
```

### 34. 상관 조건을 빠뜨리면 의미가 바뀐다

`WHERE e2.deptno = e.deptno`를 빼면 부서 평균이 아니라 전체 평균과 비교하게 된다.

### 35. 자기 자신을 포함하는지 확인한다

부서 평균에는 현재 사원도 포함된다. “자신을 제외한 동료 평균”이라면 조건을 추가한다.

```sql
SELECT e.empno, e.ename, e.sal
FROM emp AS e
WHERE e.sal > (
    SELECT AVG(e2.sal)
    FROM emp AS e2
    WHERE e2.deptno = e.deptno
      AND e2.empno <> e.empno
);
```

### 36. 동료가 없으면 AVG 결과는 NULL이다

자신을 제외한 같은 부서 사원이 없으면 Scalar Subquery의 집계 결과는 `NULL`이며, `sal > NULL`은 True가 아니다.

---

## 8. SELECT절 Subquery

### 37. 각 Row에 계산된 기준값을 함께 표시한다

```sql
SELECT
    e.empno,
    e.ename,
    e.sal,
    (
        SELECT ROUND(AVG(e2.sal), 2)
        FROM emp AS e2
        WHERE e2.deptno = e.deptno
    ) AS dept_avg_sal
FROM emp AS e;
```

### 38. 부서명을 Scalar Subquery로 가져올 수 있다

```sql
SELECT
    e.empno,
    e.ename,
    (
        SELECT d.dname
        FROM dept AS d
        WHERE d.deptno = e.deptno
    ) AS dept_name
FROM emp AS e;
```

### 39. 기준 Table 값 조회는 JOIN도 비교한다

```sql
SELECT e.empno, e.ename, d.dname AS dept_name
FROM emp AS e
LEFT JOIN dept AS d
    ON d.deptno = e.deptno;
```

여러 Column을 함께 가져오거나 관계를 명확히 표현하려면 JOIN이 더 자연스러운 경우가 많다.

### 40. 반복되는 Scalar Subquery를 줄인다

같은 조건의 Subquery를 Column마다 반복하지 말고 JOIN, CTE, Derived Table로 한 번 계산하는 방식을 검토한다.

---

## 9. FROM절 Subquery와 Derived Table

### 41. Subquery 결과를 임시 Table처럼 사용한다

```sql
SELECT dept_summary.deptno, dept_summary.avg_sal
FROM (
    SELECT deptno, ROUND(AVG(sal), 2) AS avg_sal
    FROM emp
    GROUP BY deptno
) AS dept_summary
WHERE dept_summary.avg_sal >= 2000;
```

### 42. MariaDB에서는 Derived Table에 Alias가 필요하다

```sql
-- AS dept_summary가 없으면 사용할 수 없다.
SELECT *
FROM (
    SELECT deptno, COUNT(*) AS employee_count
    FROM emp
    GROUP BY deptno
) AS dept_summary;
```

### 43. 안쪽 Query가 중간 결과를 만든다

```text
안쪽 Query
→ 부서별 평균 급여 계산

바깥 Query
→ 계산된 평균을 Filtering·정렬
```

### 44. 집계 결과에 다시 계산할 수 있다

```sql
SELECT
    MAX(dept_summary.avg_sal) AS max_department_avg,
    MIN(dept_summary.avg_sal) AS min_department_avg
FROM (
    SELECT deptno, AVG(sal) AS avg_sal
    FROM emp
    GROUP BY deptno
) AS dept_summary;
```

### 45. CTE로 같은 구조를 더 읽기 쉽게 표현할 수 있다

```sql
WITH dept_summary AS (
    SELECT deptno, COUNT(*) AS employee_count, AVG(sal) AS avg_sal
    FROM emp
    GROUP BY deptno
)
SELECT deptno, employee_count, ROUND(avg_sal, 2) AS avg_sal
FROM dept_summary
WHERE avg_sal >= 2000
ORDER BY deptno;
```

---

## 10. 다중 Column Subquery

### 46. 한 행의 여러 값을 함께 비교한다

```sql
SELECT empno, ename, deptno, job
FROM emp
WHERE (deptno, job) = (
    SELECT deptno, job
    FROM emp
    WHERE empno = 7369
);
```

### 47. 여러 Tuple과 비교하려면 IN을 사용한다

```sql
SELECT empno, ename, deptno, job
FROM emp
WHERE (deptno, job) IN (
    SELECT deptno, job
    FROM emp
    WHERE sal >= 3000
);
```

### 48. 위치와 자료형을 맞춘다

`(deptno, job)`은 Subquery의 첫 번째 `deptno`, 두 번째 `job`과 위치별로 비교된다.

### 49. 단순 관계 조회라면 JOIN이 더 명확할 수 있다

다중 Column Subquery가 복잡해지면 무엇을 연결하는지 `JOIN ... ON`으로 표현하는 방식을 함께 검토한다.

---

## 11. 내 코드와 강사님 코드 비교

### 50. 비교 기준

원본의 Subquery 예제는 결과만 맞는지보다 **반환 행 수, 비교 연산자, NULL, 읽기 쉬운 구조**를 기준으로 비교한다.

### 51. 평균을 직접 반복하는 방식

```sql
-- 고정 기준 또는 수동 확인에 가까운 형태
SELECT ename, sal
FROM emp
WHERE sal > 2073.21;
```

Data가 바뀌면 평균값도 달라지므로 Query의 기준이 오래 유지되지 않는다.

### 52. 평균을 Subquery로 계산하는 방식

```sql
SELECT ename, sal
FROM emp
WHERE sal > (
    SELECT AVG(sal)
    FROM emp
);
```

기준값의 출처가 Query 안에 드러나고 현재 Data에 맞춰 다시 계산된다.

### 53. `=`로 다중 행 결과를 비교한 형태

```sql
-- Subquery가 여러 부서를 반환하면 오류
-- SELECT ename, deptno
-- FROM emp
-- WHERE deptno = (
--     SELECT deptno FROM dept WHERE loc IN ('DALLAS', 'CHICAGO')
-- );
```

### 54. 결과 형태에 맞게 IN으로 개선한다

```sql
SELECT ename, deptno
FROM emp
WHERE deptno IN (
    SELECT deptno
    FROM dept
    WHERE loc IN ('DALLAS', 'CHICAGO')
);
```

### 55. 비교 결론

- 단일 값이 보장되면 Scalar Subquery와 단일 행 연산자를 사용한다.
- 여러 값이 가능하면 `IN`, `ANY`, `ALL`, `EXISTS` 중 의미에 맞게 선택한다.
- 기준값을 수동 복사하지 말고 Query 안에서 계산한다.
- 반복되는 Subquery는 JOIN, Derived Table, CTE로 정리한다.
- 실행 결과뿐 아니라 0행·2행 이상·NULL 상황까지 검증한다.

---

## 12. 개선된 통합 예제

### 56. 부서 평균보다 급여가 높은 사원 보고서

```sql
WITH dept_summary AS (
    SELECT deptno, AVG(sal) AS avg_sal
    FROM emp
    GROUP BY deptno
)
SELECT
    e.empno,
    e.ename,
    e.deptno,
    e.sal,
    ROUND(ds.avg_sal, 2) AS dept_avg_sal,
    ROUND(e.sal - ds.avg_sal, 2) AS difference
FROM emp AS e
JOIN dept_summary AS ds
    ON ds.deptno = e.deptno
WHERE e.sal > ds.avg_sal
ORDER BY e.deptno, difference DESC, e.empno;
```

### 57. 고액 급여자가 존재하는 부서 조회

```sql
SELECT d.deptno, d.dname, d.loc
FROM dept AS d
WHERE EXISTS (
    SELECT 1
    FROM emp AS e
    WHERE e.deptno = d.deptno
      AND e.sal >= 3000
)
ORDER BY d.deptno;
```

### 58. 부서별 최고 급여 사원 조회

```sql
SELECT e.empno, e.ename, e.deptno, e.sal
FROM emp AS e
WHERE e.sal = (
    SELECT MAX(e2.sal)
    FROM emp AS e2
    WHERE e2.deptno = e.deptno
)
ORDER BY e.deptno, e.empno;
```

동점자가 있으면 모두 반환한다. `LIMIT 1`로 임의의 한 명만 남기지 않는다.

---

## 13. 실무 활용 지침

### 59. Subquery 결과의 계약을 먼저 적는다

```text
몇 행인가?
몇 Column인가?
NULL이 가능한가?
중복이 가능한가?
```

### 60. 존재 확인과 값 반환을 구분한다

값 목록이 필요하면 `IN`, Row 존재 여부만 필요하면 `EXISTS`가 의도를 잘 드러낸다.

### 61. JOIN과 Subquery를 결과 의미로 선택한다

두 방식 중 하나가 항상 빠르다고 단정하지 않는다. 관계를 펼쳐 여러 Column을 가져오면 JOIN, 계산된 단일 기준이나 존재 검사는 Subquery가 읽기 쉬울 수 있다. 실제 성능은 실행 계획과 Data로 확인한다.

### 62. Alias를 짧고 구체적으로 작성한다

같은 Table을 중첩해서 사용하면 `e`, `e2`처럼 Scope를 구분하고, Derived Table에는 `dept_summary`처럼 역할을 나타내는 이름을 준다.

### 63. 깊은 중첩은 단계별 이름으로 풀어낸다

Subquery가 여러 단계로 중첩되면 CTE를 사용해 각 중간 결과의 의미를 드러낸다.

---

## 14. 자주 하는 실수

### 64. 다중 행 결과에 `=`를 사용한다

Subquery를 단독 실행해 행 수를 확인하고, 여러 값이 정상이라면 `IN` 등의 연산자로 바꾼다.

### 65. NOT IN의 NULL을 놓친다

Subquery Column의 `NULL`을 제거하거나 의미상 적합하면 `NOT EXISTS`로 표현한다.

### 66. Derived Table Alias를 생략한다

MariaDB의 `FROM (SELECT ...)` 뒤에는 사용할 이름을 지정한다.

### 67. 상관 조건의 Alias를 잘못 연결한다

안쪽과 바깥쪽에서 같은 Table을 쓰더라도 서로 다른 Alias를 지정하고 어느 Scope의 Column인지 확인한다.

### 68. Scalar Subquery에서 여러 Column을 선택한다

단일 값 비교에는 한 Column만 반환해야 한다. 여러 Column을 비교하려면 Row Constructor 또는 다른 구조를 사용한다.

### 69. Subquery에 불필요한 ORDER BY를 넣는다

정렬이 결과 선택에 영향을 주는 `LIMIT`과 함께 쓰는 경우가 아니라면 최종 표시 순서는 Main Query에서 정한다.

### 70. 무조건 Subquery가 느리거나 JOIN이 빠르다고 단정한다

MariaDB Optimizer가 Query를 변환할 수 있으므로 `EXPLAIN`과 실제 실행 조건으로 확인한다.

---

## 15. 디버깅 방법

### 71. Subquery만 실행한다

```sql
SELECT AVG(sal)
FROM emp;
```

예상한 행 수와 값인지 먼저 확인한다.

### 72. COUNT로 반환 행 수를 확인한다

```sql
SELECT COUNT(*) AS subquery_row_count
FROM dept
WHERE loc IN ('DALLAS', 'CHICAGO');
```

### 73. NULL을 직접 확인한다

```sql
SELECT deptno
FROM dept
WHERE deptno IS NULL;
```

특히 `NOT IN`에 사용되는 Column은 NULL 가능성을 점검한다.

### 74. 상관값을 결과에 함께 표시한다

```sql
SELECT
    e.empno,
    e.deptno,
    e.sal,
    (
        SELECT AVG(e2.sal)
        FROM emp AS e2
        WHERE e2.deptno = e.deptno
    ) AS debug_dept_avg
FROM emp AS e
ORDER BY e.deptno, e.empno;
```

### 75. EXPLAIN으로 실행 계획을 확인한다

```sql
EXPLAIN
SELECT d.deptno, d.dname
FROM dept AS d
WHERE EXISTS (
    SELECT 1
    FROM emp AS e
    WHERE e.deptno = d.deptno
);
```

### 76. 복잡한 Query는 단계별로 조립한다

1. Subquery를 독립 실행한다.
2. Main Query의 원본 Column만 조회한다.
3. Subquery를 SELECT 목록에 붙여 기준값을 확인한다.
4. `WHERE` 조건을 적용한다.
5. 마지막에 정렬과 표시 형식을 추가한다.

---

## 16. 종합실습

### 77. 문제 1 — 전체 평균 이상 급여

전체 평균 급여 이상을 받는 사원의 번호, 이름, 급여를 조회한다.

### 78. 문제 2 — 특정 지역 부서의 사원

`DALLAS` 또는 `CHICAGO`에 있는 부서 소속 사원을 Subquery로 조회한다.

### 79. 문제 3 — 사원이 없는 부서

소속 사원이 한 명도 없는 부서를 `NOT EXISTS`로 조회한다.

### 80. 문제 4 — 부서 평균 초과 사원

각 사원의 급여가 자신의 부서 평균보다 높은 사원을 조회한다.

### 81. 문제 5 — 부서별 최고 급여 사원

부서별 최고 급여를 받는 사원을 조회한다. 동점자는 모두 표시한다.

---

## 17. 정답과 해설

### 82. 문제 1 정답

```sql
SELECT empno, ename, sal
FROM emp
WHERE sal >= (
    SELECT AVG(sal)
    FROM emp
)
ORDER BY sal DESC, empno;
```

`AVG`는 한 값을 반환하므로 Scalar Subquery에 적합하다.

### 83. 문제 2 정답

```sql
SELECT empno, ename, deptno
FROM emp
WHERE deptno IN (
    SELECT deptno
    FROM dept
    WHERE loc IN ('DALLAS', 'CHICAGO')
)
ORDER BY deptno, empno;
```

여러 부서 번호가 반환될 수 있으므로 `IN`을 사용한다.

### 84. 문제 3 정답

```sql
SELECT d.deptno, d.dname, d.loc
FROM dept AS d
WHERE NOT EXISTS (
    SELECT 1
    FROM emp AS e
    WHERE e.deptno = d.deptno
)
ORDER BY d.deptno;
```

일치하는 사원 Row가 없는 부서만 남는다.

### 85. 문제 4 정답

```sql
SELECT e.empno, e.ename, e.deptno, e.sal
FROM emp AS e
WHERE e.sal > (
    SELECT AVG(e2.sal)
    FROM emp AS e2
    WHERE e2.deptno = e.deptno
)
ORDER BY e.deptno, e.sal DESC, e.empno;
```

Subquery가 Main Query의 현재 `DEPTNO`를 참조하는 Correlated Subquery다.

### 86. 문제 5 정답

```sql
SELECT e.empno, e.ename, e.deptno, e.sal
FROM emp AS e
WHERE e.sal = (
    SELECT MAX(e2.sal)
    FROM emp AS e2
    WHERE e2.deptno = e.deptno
)
ORDER BY e.deptno, e.empno;
```

최고 급여 값과 같은 모든 사원을 반환하므로 동점자도 유지된다.

---

## 18. 최종 체크리스트

### 87. 문법 체크

- [ ] Subquery를 괄호로 감쌌는가?
- [ ] Scalar 문맥에서 1행 1열을 보장하는가?
- [ ] 여러 값에는 `IN`, `ANY`, `ALL` 등 적절한 연산자를 사용했는가?
- [ ] Derived Table에 Alias를 지정했는가?

### 88. 논리 체크

- [ ] Subquery가 0행 또는 여러 행일 때 결과를 검토했는가?
- [ ] `NOT IN` 대상에 `NULL`이 들어갈 수 있는가?
- [ ] Correlated Subquery의 바깥·안쪽 Alias가 올바른가?
- [ ] 자기 자신을 포함하는 계산인지 확인했는가?

### 89. 품질 체크

- [ ] 반복되는 Subquery를 JOIN·CTE로 정리할 필요가 없는가?
- [ ] 존재 여부만 필요할 때 `EXISTS`를 검토했는가?
- [ ] 불필요한 `ORDER BY`와 임의의 `LIMIT 1`을 사용하지 않았는가?
- [ ] 성능 판단을 추측이 아니라 `EXPLAIN`으로 확인했는가?

---

## 19. 핵심 요약

### 90. Subquery 핵심 문장

```text
Scalar Subquery
→ 1행 1열, 0행이면 NULL, 여러 행이면 오류

IN
→ 여러 값 중 하나와 일치

ANY / ALL
→ 하나라도 / 모든 값과 비교

EXISTS
→ 반환 값이 아니라 Row 존재 여부 확인

Correlated Subquery
→ 안쪽 Query가 바깥 Query의 현재 Row를 참조

Derived Table
→ FROM절의 Subquery 결과를 Table처럼 사용하고 Alias 지정
```

### 91. 최종 정리

Subquery의 핵심은 중첩 자체가 아니라 **안쪽 Query가 몇 행·몇 Column을 반환하는지** 정확히 아는 것이다. 단일 값에는 Scalar Subquery, 값 목록에는 `IN`·`ANY`·`ALL`, 존재 판정에는 `EXISTS`, 중간 Table에는 Derived Table을 사용한다. 복잡해지면 Alias, 독립 실행, CTE, `EXPLAIN`으로 구조와 실행을 검증한다.

---

## 📎 다음 문서

다음 원본 흐름은 기존 방식과 ANSI 문법을 포함한 JOIN이다.

```text
12_SQL_JOIN.md
```
