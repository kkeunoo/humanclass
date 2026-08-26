# 20. SQL 종합실습

> SQL 01~19의 개념을 조회·보고서·Data 변경·성능 검증 Scenario로 완성하는 최종 실습

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | SELECT부터 Recursive CTE·Transaction·Index까지 통합 |
| 기준 DBMS | MariaDB, InnoDB |
| 조회 실습 | `EMP`, `DEPT`, `SALGRADE` |
| 변경 실습 | `_PRACTICE` 전용 Table |
| 선수 학습 | SQL 01~19 전체 |
| 문서 버전 | V3 Encyclopedia |
| V3 개정 | 입력 Data·중간 Result·실행 결과·원본 위치를 함께 기록하는 학습 복원 형식 |

> 조회 문제는 학습용 Sample Table을 사용한다. DDL·DML·Transaction 문제는 원본 `EMP`, `DEPT`를 직접 변경하지 않고 별도 `_PRACTICE` Table에서 실행한다.

---

## 🎯 학습 목표

- 자연어 요구사항을 Result Row, Join 관계, Filtering, 집계, 정렬로 분해한다.
- NULL·중복·경계값·동점·0행을 고려한 Query를 작성한다.
- JOIN, Subquery, CTE, Window 대체 Pattern 중 적절한 구조를 선택한다.
- DDL과 제약조건으로 안전한 실습 Schema를 설계한다.
- Preview·Transaction·영향 Row 검증을 포함한 DML을 수행한다.
- `EXPLAIN`을 사용해 Index 후보와 실제 접근 계획을 확인한다.
- Recursive CTE로 조직 계층을 안전하게 탐색한다.
- 결과뿐 아니라 작성 근거와 위험을 설명할 수 있다.

---

## 1. 실습 진행 방법

### 1. 문제를 바로 SQL로 옮기지 않는다

```text
한 Row의 의미
→ 필요한 Table과 관계
→ Row Filtering
→ Grouping과 집계
→ 표시 Column
→ 정렬과 LIMIT
```

### 2. 예상 결과를 먼저 적는다

Column명, Row 수 범위, NULL 가능성, 중복 허용 여부를 작성한다.

### 3. 단계별로 실행한다

`FROM + JOIN`부터 확인하고 `WHERE`, `GROUP BY`, `HAVING`, 표시·정렬을 순서대로 추가한다.

### 4. 정답을 보기 전에 검증한다

```text
NULL Data
경계값
동점
일치 Row 없음
여러 Row 일치
```

### 5. 정답은 유일하지 않을 수 있다

결과가 같더라도 가독성, NULL 의미, 중복, 성능, 유지보수 기준으로 비교한다.

---

## 2. 실습 환경 확인

### 6. Table 구조

```sql
DESCRIBE emp;
DESCRIBE dept;
DESCRIBE salgrade;
```

### 7. 제약조건과 Index

```sql
SHOW CREATE TABLE emp;
SHOW CREATE TABLE dept;
SHOW INDEX FROM emp;
SHOW INDEX FROM dept;
```

### 8. Session 환경

```sql
SELECT
    VERSION() AS mariadb_version,
    DATABASE() AS current_database,
    @@sql_mode AS sql_mode,
    @@autocommit AS autocommit_mode,
    @@time_zone AS session_time_zone;
```

### 9. Sample 규모

```sql
SELECT 'EMP' AS table_name, COUNT(*) AS row_count FROM emp
UNION ALL
SELECT 'DEPT', COUNT(*) FROM dept
UNION ALL
SELECT 'SALGRADE', COUNT(*) FROM salgrade;
```

---

## 3. Level 1 — SELECT와 조건

### 10. 문제 1 — 기본 사원 목록

사원 번호, 이름, 직무, 급여를 사원 번호순으로 조회한다.

### 11. 문제 2 — 복합 조건

20번 또는 30번 부서에서 급여가 1500 이상인 사원을 조회한다. 급여 내림차순, 같은 급여는 사원 번호순으로 정렬한다.

### 12. 문제 3 — LIKE

이름의 두 번째 글자가 `A`인 사원을 조회한다.

### 13. 문제 4 — NULL 구분

Commission이 NULL인 사원과 0인 사원을 서로 다른 상태 Label로 표시한다.

### 14. 문제 5 — Top-N

급여가 가장 높은 사원 3명을 조회한다. 동점에서도 결과 순서가 안정적이어야 한다.

---

## 4. Level 1 정답

### 15. 문제 1 정답

```sql
SELECT empno, ename, job, sal
FROM emp
ORDER BY empno;
```

### 16. 문제 2 정답

```sql
SELECT empno, ename, deptno, sal
FROM emp
WHERE deptno IN (20, 30)
  AND sal >= 1500
ORDER BY sal DESC, empno;
```

### 17. 문제 3 정답

```sql
SELECT empno, ename
FROM emp
WHERE ename LIKE '_A%'
ORDER BY empno;
```

`_`는 정확히 한 글자, `%`는 0글자 이상이다.

### 18. 문제 4 정답

```sql
SELECT
    empno,
    ename,
    comm,
    CASE
        WHEN comm IS NULL THEN '미입력'
        WHEN comm = 0 THEN '지급액 0'
        ELSE '지급'
    END AS commission_status
FROM emp
ORDER BY empno;
```

### 19. 문제 5 정답

```sql
SELECT empno, ename, sal
FROM emp
ORDER BY sal DESC, empno
LIMIT 3;
```

`EMPNO`가 Tie-breaker 역할을 한다.

---

## 5. Level 2 — 함수와 CASE

### 20. 문제 6 — 이름 Masking

이름 앞 두 글자만 남기고 나머지를 `*`로 표시한다. 이름의 Character 길이를 유지한다.

### 21. 문제 7 — 급여·Commission 계산

각 사원의 총 보상액을 `SAL + COMM`으로 계산하되 Commission NULL은 0으로 처리한다.

### 22. 문제 8 — 입사 연도

사원 이름, 입사일, 입사 연도를 조회하고 입사 연도·사원 번호순으로 정렬한다.

### 23. 문제 9 — 급여 등급 Label

3000 이상 `HIGH`, 2000 이상 `MIDDLE`, 나머지 `LOW`로 분류한다.

### 24. 문제 10 — 사용자 정의 직무 정렬

`PRESIDENT → MANAGER → ANALYST → SALESMAN → CLERK → 기타` 순서로 정렬한다.

---

## 6. Level 2 정답

### 25. 문제 6 정답

```sql
SELECT
    ename,
    RPAD(
        SUBSTRING(ename, 1, 2),
        CHAR_LENGTH(ename),
        '*'
    ) AS masked_name
FROM emp
ORDER BY empno;
```

### 26. 문제 7 정답

```sql
SELECT
    empno,
    ename,
    sal,
    comm,
    sal + COALESCE(comm, 0) AS total_compensation
FROM emp
ORDER BY empno;
```

### 27. 문제 8 정답

```sql
SELECT
    empno,
    ename,
    hiredate,
    DATE_FORMAT(hiredate, '%Y') AS hire_year
FROM emp
ORDER BY hire_year, empno;
```

### 28. 문제 9 정답

```sql
SELECT
    empno,
    ename,
    sal,
    CASE
        WHEN sal >= 3000 THEN 'HIGH'
        WHEN sal >= 2000 THEN 'MIDDLE'
        ELSE 'LOW'
    END AS salary_level
FROM emp
ORDER BY sal DESC, empno;
```

### 29. 문제 10 정답

```sql
SELECT empno, ename, job, sal
FROM emp
ORDER BY
    CASE job
        WHEN 'PRESIDENT' THEN 1
        WHEN 'MANAGER' THEN 2
        WHEN 'ANALYST' THEN 3
        WHEN 'SALESMAN' THEN 4
        WHEN 'CLERK' THEN 5
        ELSE 6
    END,
    sal DESC,
    empno;
```

---

## 7. Level 3 — 집계와 Grouping

### 30. 문제 11 — 부서별 급여 통계

부서별 인원수, 급여 합계, 평균·최고·최저 급여를 조회한다.

### 31. 문제 12 — 조건부 집계

부서별 전체 인원, 급여 2000 이상 인원, 양수 Commission 지급 인원을 조회한다.

### 32. 문제 13 — HAVING

평균 급여가 2000 이상인 부서·직무 Group만 조회한다.

### 33. 문제 14 — NULL 포함 집계 차이

`COUNT(*)`, `COUNT(comm)`, `AVG(comm)`, `AVG(COALESCE(comm, 0))`을 한 Query에서 비교한다.

### 34. 문제 15 — 사원이 없는 부서 포함

모든 부서의 인원수를 표시한다. 사원이 없는 부서는 0명이어야 한다.

---

## 8. Level 3 정답

### 35. 문제 11 정답

```sql
SELECT
    deptno,
    COUNT(*) AS employee_count,
    SUM(sal) AS salary_sum,
    ROUND(AVG(sal), 2) AS avg_salary,
    MAX(sal) AS max_salary,
    MIN(sal) AS min_salary
FROM emp
GROUP BY deptno
ORDER BY deptno;
```

### 36. 문제 12 정답

```sql
SELECT
    deptno,
    COUNT(*) AS total_count,
    SUM(CASE WHEN sal >= 2000 THEN 1 ELSE 0 END) AS high_salary_count,
    SUM(CASE WHEN comm > 0 THEN 1 ELSE 0 END) AS commission_count
FROM emp
GROUP BY deptno
ORDER BY deptno;
```

### 37. 문제 13 정답

```sql
SELECT
    deptno,
    job,
    COUNT(*) AS employee_count,
    ROUND(AVG(sal), 2) AS avg_salary
FROM emp
GROUP BY deptno, job
HAVING AVG(sal) >= 2000
ORDER BY deptno, job;
```

`SAL`을 GROUP BY에 추가하면 의도보다 잘게 Grouping된다.

### 38. 문제 14 정답

```sql
SELECT
    COUNT(*) AS row_count,
    COUNT(comm) AS non_null_comm_count,
    ROUND(AVG(comm), 2) AS avg_paid_or_zero_comm,
    ROUND(AVG(COALESCE(comm, 0)), 2) AS avg_all_employee_comm
FROM emp;
```

두 평균의 분모가 다르다.

### 39. 문제 15 정답

```sql
SELECT
    d.deptno,
    d.dname,
    COUNT(e.empno) AS employee_count
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
GROUP BY d.deptno, d.dname
ORDER BY d.deptno;
```

`COUNT(*)`를 사용하면 사원이 없는 보존 Row까지 1로 셀 수 있다.

---

## 9. Level 4 — JOIN과 Subquery

### 40. 문제 16 — 사원·부서·급여 등급

사원 번호, 이름, 급여, 부서명, 위치, 급여 등급을 조회한다.

### 41. 문제 17 — 전체 평균 초과

전체 평균보다 급여가 높은 사원을 Scalar Subquery로 조회한다.

### 42. 문제 18 — 부서 평균 초과

자신의 부서 평균보다 급여가 높은 사원을 조회한다.

### 43. 문제 19 — 부서별 최고 급여자

각 부서에서 최고 급여를 받는 사원을 조회한다. 동점자는 모두 유지한다.

### 44. 문제 20 — 사원이 없는 부서

`NOT EXISTS` 방식으로 소속 사원이 없는 부서를 조회한다.

---

## 10. Level 4 정답

### 45. 문제 16 정답

```sql
SELECT
    e.empno,
    e.ename,
    e.sal,
    d.dname,
    d.loc,
    g.grade
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
JOIN salgrade AS g
    ON e.sal BETWEEN g.losal AND g.hisal
ORDER BY e.empno;
```

### 46. 문제 17 정답

```sql
SELECT empno, ename, sal
FROM emp
WHERE sal > (
    SELECT AVG(sal)
    FROM emp
)
ORDER BY sal DESC, empno;
```

### 47. 문제 18 정답

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

### 48. 문제 19 정답

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

### 49. 문제 20 정답

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

---

## 11. Level 5 — 집합·계층·보고서

### 50. 문제 21 — 통합 검색 결과

사원과 부서를 `OBJECT_TYPE`, `OBJECT_NO`, `OBJECT_NAME` 구조로 합친다.

### 51. 문제 22 — 사원과 관리자

모든 사원의 이름과 관리자 이름을 조회한다. 관리자가 없으면 `관리자 없음`으로 표시한다.

### 52. 문제 23 — Recursive 조직도

Root부터 전체 사원을 조회하고 깊이, 들여쓴 이름, 이름 경로를 표시한다.

### 53. 문제 24 — 날짜 Calendar

2026-08-01부터 2026-08-14까지 날짜를 생성하고 날짜별 입사자 수를 표시한다.

### 54. 문제 25 — 부서 보고서

모든 부서의 인원수, 평균 급여, 최고 급여자 수를 조회한다. 사원이 없는 부서도 포함한다.

---

## 12. Level 5 정답

### 55. 문제 21 정답

```sql
SELECT 'EMP' AS object_type, empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT 'DEPT', deptno, dname
FROM dept
ORDER BY object_type, object_no;
```

### 56. 문제 22 정답

```sql
SELECT
    employee.empno,
    employee.ename AS employee_name,
    COALESCE(manager.ename, '관리자 없음') AS manager_name
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
ORDER BY employee.empno;
```

### 57. 문제 23 정답

```sql
WITH RECURSIVE org AS (
    SELECT
        empno,
        ename,
        mgr,
        1 AS depth,
        CAST(ename AS CHAR(1000)) AS name_path,
        CAST(CONCAT('/', empno, '/') AS CHAR(1000)) AS id_path
    FROM emp
    WHERE mgr IS NULL

    UNION ALL

    SELECT
        child.empno,
        child.ename,
        child.mgr,
        parent.depth + 1,
        CONCAT(parent.name_path, ' > ', child.ename),
        CONCAT(parent.id_path, child.empno, '/')
    FROM emp AS child
    JOIN org AS parent
        ON child.mgr = parent.empno
    WHERE parent.depth < 20
      AND parent.id_path NOT LIKE CONCAT('%/', child.empno, '/%')
)
SELECT
    empno,
    CONCAT(REPEAT('  ', depth - 1), ename) AS hierarchy_name,
    mgr,
    depth,
    name_path
FROM org
ORDER BY id_path;
```

### 58. 문제 24 정답

```sql
WITH RECURSIVE calendar AS (
    SELECT DATE('2026-08-01') AS calendar_date
    UNION ALL
    SELECT calendar_date + INTERVAL 1 DAY
    FROM calendar
    WHERE calendar_date < '2026-08-14'
)
SELECT
    c.calendar_date,
    COUNT(e.empno) AS hire_count
FROM calendar AS c
LEFT JOIN emp AS e
    ON e.hiredate = c.calendar_date
GROUP BY c.calendar_date
ORDER BY c.calendar_date;
```

### 59. 문제 25 정답

```sql
WITH employee_rank AS (
    SELECT
        e.empno,
        e.deptno,
        e.sal,
        CASE
            WHEN e.sal = (
                SELECT MAX(e2.sal)
                FROM emp AS e2
                WHERE e2.deptno = e.deptno
            ) THEN 1
            ELSE 0
        END AS is_top_salary
    FROM emp AS e
)
SELECT
    d.deptno,
    d.dname,
    COUNT(er.empno) AS employee_count,
    ROUND(AVG(er.sal), 2) AS avg_salary,
    COALESCE(SUM(er.is_top_salary), 0) AS top_salary_employee_count
FROM dept AS d
LEFT JOIN employee_rank AS er
    ON er.deptno = d.deptno
GROUP BY d.deptno, d.dname
ORDER BY d.deptno;
```

동점 최고 급여자는 모두 계산된다.

---

## 13. Level 6 — 실습 Schema 설계

### 60. Scenario

부서와 프로젝트, 프로젝트 참여자를 관리하는 실습 Schema를 만든다.

### 61. 요구사항

```text
부서
→ 자동 증가 ID, 이름 Unique

프로젝트
→ 자동 증가 ID, 부서 FK, 이름, 상태, 시작일

참여자
→ 프로젝트 ID + 사원 번호 복합 PK
→ 참여 역할과 등록 시각
```

### 62. 문제 26 — Table 생성

`department_practice`, `project_practice`, `project_member_practice`를 생성한다.

### 63. 문제 27 — Sample 입력

부서 2개, 프로젝트 2개, 참여자 3개를 입력하고 자동 생성 ID를 확인한다.

---

## 14. Level 6 정답

### 64. 문제 26 정답

```sql
CREATE TABLE department_practice (
    department_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_department_practice PRIMARY KEY (department_id),
    CONSTRAINT ux_department_practice_name UNIQUE (department_name)
) ENGINE = InnoDB;

CREATE TABLE project_practice (
    project_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    department_id BIGINT UNSIGNED NOT NULL,
    project_name VARCHAR(200) NOT NULL,
    project_status VARCHAR(20) NOT NULL DEFAULT 'PLANNED',
    start_date DATE NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_project_practice PRIMARY KEY (project_id),
    CONSTRAINT fk_project_department
        FOREIGN KEY (department_id)
        REFERENCES department_practice (department_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    INDEX ix_project_department_status (department_id, project_status)
) ENGINE = InnoDB;

CREATE TABLE project_member_practice (
    project_id BIGINT UNSIGNED NOT NULL,
    empno INT NOT NULL,
    member_role VARCHAR(50) NOT NULL,
    joined_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_project_member PRIMARY KEY (project_id, empno),
    CONSTRAINT fk_project_member_project
        FOREIGN KEY (project_id)
        REFERENCES project_practice (project_id)
        ON DELETE CASCADE
) ENGINE = InnoDB;
```

### 65. 문제 27 정답

```sql
INSERT INTO department_practice (department_name)
VALUES ('PLATFORM');
SET @platform_department_id = LAST_INSERT_ID();

INSERT INTO department_practice (department_name)
VALUES ('DATA');
SET @data_department_id = LAST_INSERT_ID();

INSERT INTO project_practice
    (department_id, project_name, project_status, start_date)
VALUES
    (@platform_department_id, 'API Renewal', 'ACTIVE', '2026-08-01');
SET @api_project_id = LAST_INSERT_ID();

INSERT INTO project_practice
    (department_id, project_name, project_status, start_date)
VALUES
    (@data_department_id, 'Data Warehouse', 'PLANNED', '2026-09-01');
SET @dw_project_id = LAST_INSERT_ID();

INSERT INTO project_member_practice
    (project_id, empno, member_role)
VALUES
    (@api_project_id, 7369, 'DEVELOPER'),
    (@api_project_id, 7566, 'LEAD'),
    (@dw_project_id, 7788, 'ANALYST');
```

Application에서는 Session 변수를 대신해 같은 Connection의 생성 ID 반환 API를 사용한다.

---

## 15. Level 7 — 안전한 DML과 Transaction

### 66. 문제 28 — 프로젝트 이동

`API Renewal` 프로젝트를 DATA 부서로 이동한다. Target ID와 영향 Row를 검증하고 Transaction으로 처리한다.

### 67. 문제 29 — 프로젝트와 참여자 삭제

`Data Warehouse` 프로젝트와 종속 참여자를 삭제한다. Cascade 범위와 예상 Row를 먼저 확인한다.

### 68. 문제 30 — 실패 복구

프로젝트 이동 후 존재하지 않는 사원을 참여자로 넣어 오류가 발생하면 전체 변경을 취소하는 흐름을 작성한다.

---

## 16. Level 7 정답

### 69. 문제 28 정답

```sql
SELECT project_id, project_name, department_id
FROM project_practice
WHERE project_name = 'API Renewal';

SELECT department_id, department_name
FROM department_practice
WHERE department_name = 'DATA';

START TRANSACTION;

UPDATE project_practice
SET department_id = @data_department_id
WHERE project_id = @api_project_id;

SELECT ROW_COUNT() AS affected_rows;

SELECT project_id, project_name, department_id
FROM project_practice
WHERE project_id = @api_project_id;

-- 정확히 1행이고 값이 맞으면 COMMIT
COMMIT;
```

### 70. 문제 29 정답

```sql
SHOW CREATE TABLE project_member_practice;

SELECT p.project_id, p.project_name, COUNT(pm.empno) AS member_count
FROM project_practice AS p
LEFT JOIN project_member_practice AS pm
    ON pm.project_id = p.project_id
WHERE p.project_name = 'Data Warehouse'
GROUP BY p.project_id, p.project_name;

START TRANSACTION;

DELETE FROM project_practice
WHERE project_id = @dw_project_id;

SELECT ROW_COUNT() AS deleted_projects;

SELECT COUNT(*) AS remaining_members
FROM project_member_practice
WHERE project_id = @dw_project_id;

-- 결과 확인 후 COMMIT 또는 ROLLBACK
COMMIT;
```

### 71. 문제 30 정답

```sql
START TRANSACTION;

UPDATE project_practice
SET department_id = @data_department_id
WHERE project_id = @api_project_id;

INSERT INTO project_member_practice
    (project_id, empno, member_role)
VALUES
    (@api_project_id, 999999, 'DEVELOPER');

-- INSERT가 제약조건 오류로 실패하면 Application 예외 처리에서 실행한다.
ROLLBACK;
```

`EMPNO`에 FK가 실제 정의되지 않았다면 오류가 나지 않는다. 해당 무결성이 필요하면 참조 대상 Table과 FK를 설계해야 한다는 점도 핵심이다.

---

## 17. Level 8 — Index와 실행 계획

### 72. 문제 31 — 주요 Query

부서별 상태로 프로젝트를 조회하고 시작일 내림차순 Paging하는 Query를 작성한다.

### 73. 문제 32 — Index 검증

기존 `(department_id, project_status)` Index와 `(department_id, project_status, start_date, project_id)` 후보를 비교한다.

### 74. 문제 33 — 잘못된 Hint 제거

근거 없이 사용된 `FORCE INDEX`를 제거하고 전후 실행 계획과 실제 Data 규모로 판단한다.

---

## 18. Level 8 정답

### 75. 문제 31 정답

```sql
SELECT
    project_id,
    project_name,
    project_status,
    start_date
FROM project_practice
WHERE department_id = ?
  AND project_status = ?
ORDER BY start_date DESC, project_id DESC
LIMIT 20;
```

### 76. 문제 32 정답

```sql
EXPLAIN
SELECT project_id, project_name, project_status, start_date
FROM project_practice
WHERE department_id = @data_department_id
  AND project_status = 'ACTIVE'
ORDER BY start_date DESC, project_id DESC
LIMIT 20;

CREATE INDEX ix_project_dept_status_start_id
ON project_practice
    (department_id, project_status, start_date, project_id);

EXPLAIN
SELECT project_id, project_name, project_status, start_date
FROM project_practice
WHERE department_id = @data_department_id
  AND project_status = 'ACTIVE'
ORDER BY start_date DESC, project_id DESC
LIMIT 20;
```

Sample Data가 너무 적으면 차이가 의미 없으므로 운영과 유사한 분포에서 측정한다.

### 77. 문제 33 해설

```text
1. Hint 없는 Plan 확인
2. Cardinality·통계·Data 분포 확인
3. 후보 Index와 Query 구조 검토
4. 실제 실행 시간과 읽은 Row 비교
5. Hint가 지속적으로 우월할 근거가 있을 때만 사용
```

---

## 19. 내 코드와 강사님 코드 비교

### 78. 결과만 빠르게 만드는 방식

```sql
SELECT *
FROM emp e, dept d
WHERE e.deptno = d.deptno
  AND e.sal >= (SELECT AVG(sal) FROM emp)
ORDER BY e.sal DESC;
```

### 79. 검증 가능한 구조로 개선

```sql
WITH salary_standard AS (
    SELECT AVG(sal) AS company_avg_salary
    FROM emp
)
SELECT
    e.empno,
    e.ename,
    e.sal,
    d.deptno,
    d.dname,
    ROUND(s.company_avg_salary, 2) AS company_avg_salary
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
CROSS JOIN salary_standard AS s
WHERE e.sal >= s.company_avg_salary
ORDER BY e.sal DESC, e.empno;
```

CTE 이름으로 평균 급여라는 기준값의 역할을 드러낸다.

### 80. 최종 권장 형태

```sql
WITH salary_standard AS (
    SELECT AVG(sal) AS company_avg_salary
    FROM emp
)
SELECT
    e.empno,
    e.ename,
    e.sal,
    d.deptno,
    d.dname,
    ROUND(s.company_avg_salary, 2) AS company_avg_salary
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
CROSS JOIN salary_standard AS s
WHERE e.sal >= s.company_avg_salary
ORDER BY e.sal DESC, e.empno;
```

### 81. 비교 결론

- 학습 중 짧은 Query는 문법 확인에 유용하다.
- 최종 Code는 명시적 Column과 ANSI JOIN을 사용한다.
- 평균 같은 기준값은 이름 있는 단계로 분리할 수 있다.
- 안정적인 정렬과 NULL·동점 조건을 포함한다.
- 성능 변경 전후에는 결과 동일성을 먼저 검증한다.

---

## 20. 개선된 최종 통합 예제

### 82. 요구사항

모든 부서의 사원 현황을 조회한다. 부서별 인원수, 평균 급여, 부서 최고 급여자, 급여 2000 이상 인원, 관리자 없는 인원을 표시한다. 사원이 없는 부서도 포함한다.

### 83. 통합 Query

```sql
WITH employee_enriched AS (
    SELECT
        e.empno,
        e.ename,
        e.deptno,
        e.sal,
        e.mgr,
        MAX(e.sal) OVER (PARTITION BY e.deptno) AS dept_max_salary
    FROM emp AS e
),
department_report AS (
    SELECT
        d.deptno,
        d.dname,
        d.loc,
        COUNT(e.empno) AS employee_count,
        ROUND(AVG(e.sal), 2) AS avg_salary,
        SUM(CASE WHEN e.sal = e.dept_max_salary THEN 1 ELSE 0 END)
            AS top_salary_employee_count,
        SUM(CASE WHEN e.sal >= 2000 THEN 1 ELSE 0 END)
            AS high_salary_count,
        SUM(CASE WHEN e.empno IS NOT NULL AND e.mgr IS NULL THEN 1 ELSE 0 END)
            AS no_manager_count
    FROM dept AS d
    LEFT JOIN employee_enriched AS e
        ON e.deptno = d.deptno
    GROUP BY d.deptno, d.dname, d.loc
)
SELECT
    deptno,
    dname,
    loc,
    employee_count,
    avg_salary,
    top_salary_employee_count,
    high_salary_count,
    no_manager_count
FROM department_report
ORDER BY deptno;
```

### 84. Window Function 범위 Note

`MAX(...) OVER (PARTITION BY ...)`는 원본 앞 단원에서 본격적으로 다루지 않은 확장 문법이다. Window Function을 사용하지 않는 대안은 Correlated Subquery 또는 부서별 최대 급여 CTE를 JOIN하는 것이다.

### 85. 기존 학습 범위만 사용하는 대안

```sql
WITH dept_max_salary AS (
    SELECT deptno, MAX(sal) AS max_salary
    FROM emp
    GROUP BY deptno
),
employee_enriched AS (
    SELECT
        e.empno,
        e.deptno,
        e.sal,
        e.mgr,
        m.max_salary
    FROM emp AS e
    JOIN dept_max_salary AS m
        ON m.deptno = e.deptno
)
SELECT
    d.deptno,
    d.dname,
    d.loc,
    COUNT(e.empno) AS employee_count,
    ROUND(AVG(e.sal), 2) AS avg_salary,
    SUM(CASE WHEN e.sal = e.max_salary THEN 1 ELSE 0 END)
        AS top_salary_employee_count,
    SUM(CASE WHEN e.sal >= 2000 THEN 1 ELSE 0 END)
        AS high_salary_count,
    SUM(CASE WHEN e.empno IS NOT NULL AND e.mgr IS NULL THEN 1 ELSE 0 END)
        AS no_manager_count
FROM dept AS d
LEFT JOIN employee_enriched AS e
    ON e.deptno = d.deptno
GROUP BY d.deptno, d.dname, d.loc
ORDER BY d.deptno;
```

---

## 21. 실수·디버깅 종합

### 86. 예상보다 Row가 많다

JOIN 조건 누락, N:M 관계, UNION ALL, Recursive 경로 중복을 확인한다.

### 87. 예상보다 Row가 적다

INNER JOIN 누락, 오른쪽 Column의 WHERE 조건, NULL 비교, 날짜 경계를 확인한다.

### 88. 집계값이 크다

집계 전 상세 Join Row를 조회하고 한 원본 Row가 몇 번 반복되는지 센다.

### 89. Scalar Subquery 오류

Subquery만 실행해 Row 수를 확인하고 `=`, `IN`, 집계 중 맞는 형태를 선택한다.

### 90. NOT IN 결과가 없다

Subquery에 NULL이 있는지 확인하고 `NOT EXISTS`를 검토한다.

### 91. Recursive CTE가 끝나지 않는다

종료 조건, Cycle, Path 방문 검사, `max_recursive_iterations`를 확인한다.

### 92. UPDATE·DELETE 영향 Row가 너무 많다

즉시 Commit하지 말고 Transaction 안에서 Key 목록을 조회한 뒤 Rollback한다.

### 93. Index가 선택되지 않는다

Table 크기, 선택도, 통계, 자료형 변환, 함수, 반환 Row 비율을 확인한다.

---

## 22. 실무 제출 Checklist

### 94. 요구사항

- [ ] Result 한 Row의 의미를 정의했는가?
- [ ] NULL과 중복의 업무 의미를 정했는가?
- [ ] 정렬·Paging·동점 규칙이 명확한가?

### 95. Query 정확성

- [ ] JOIN 관계와 Cardinality를 설명할 수 있는가?
- [ ] 경계값, 0행, 다중 일치 Case를 Test했는가?
- [ ] Grouping 전후 Row 수와 집계 분모를 확인했는가?

### 96. 변경 안전성

- [ ] 원본 학습 Table 대신 실습 Table을 사용하는가?
- [ ] DML Preview와 예상 영향 Row가 있는가?
- [ ] Transaction의 모든 성공·실패 경로가 처리되는가?
- [ ] DDL 암시적 Commit과 Cascade를 확인했는가?

### 97. 성능

- [ ] 실제 규모와 Parameter로 실행 계획을 확인했는가?
- [ ] 필요한 Column과 Row만 조회하는가?
- [ ] Index의 읽기 이점과 쓰기 비용을 함께 평가했는가?
- [ ] Hint 없이 해결할 방법을 먼저 검토했는가?

### 98. Code 품질

- [ ] Keyword, Naming, Alias, 들여쓰기가 일관적인가?
- [ ] Prepared Statement Parameter를 사용하는가?
- [ ] Comment가 “왜”와 위험을 설명하는가?
- [ ] Version·SQL_MODE·Time Zone 차이를 확인했는가?

---

## 23. 최종 자기평가

### 99. 기초

- [ ] SELECT 목록과 Alias를 명확히 작성한다.
- [ ] WHERE, NULL, LIKE, 정렬, LIMIT를 정확히 사용한다.

### 100. 집계·조회 설계

- [ ] 집계함수, GROUP BY, HAVING의 처리 단계를 설명한다.
- [ ] CASE, Subquery, UNION, JOIN을 요구사항에 맞게 선택한다.

### 101. 관계·계층

- [ ] INNER·Outer·Self Join의 Row 보존 차이를 설명한다.
- [ ] Recursive CTE의 Anchor·재귀·종료·Cycle을 설계한다.

### 102. 변경·운영

- [ ] DDL과 제약조건으로 무결성을 설계한다.
- [ ] DML을 Preview·Transaction·검증 흐름으로 실행한다.
- [ ] Index와 AUTO_INCREMENT의 Trade-off를 설명한다.

### 103. 실무 수준

- [ ] Query 결과뿐 아니라 위험·성능·복구 방법까지 Review한다.
- [ ] 다른 개발자가 유지보수할 수 있는 SQL을 작성한다.

---

## 24. 핵심 요약

### 104. SQL 전체 흐름

```text
요구사항 분석
→ 한 Row의 의미·NULL·중복·정렬 정의

Query 구성
→ FROM/JOIN → WHERE → GROUP BY/HAVING → SELECT → ORDER BY/LIMIT

검증
→ 경계값·0행·다중 일치·동점·단계별 Row 수

변경
→ Preview → Transaction → DML → 영향 Row·불변 조건 → COMMIT/ROLLBACK

성능
→ 실제 Query 수집 → EXPLAIN → Index 후보 → 전후 측정

협업
→ Naming·Formatting·Parameter Binding·Code Review
```

### 105. 최종 정리

SQL 학습의 완성은 문법을 많이 기억하는 것이 아니라 **요구사항을 검증 가능한 Result와 안전한 변경 절차로 변환하는 능력**이다. 조회에서는 한 Row의 의미와 관계·NULL·중복을 먼저 정의하고, 변경에서는 Preview와 Transaction을 사용한다. 성능은 Index를 추측하지 않고 실행 계획과 실제 규모로 측정하며, 최종 SQL은 다른 개발자가 결과와 위험을 설명할 수 있는 형태로 남긴다.

---

## 📎 SQL V3 Series 완료

```text
01 SQL 기초와 SELECT
02 WHERE와 조건연산자
03 LIKE와 NULL
04 정렬과 LIMIT
05 집계함수
06 GROUP BY와 HAVING
07 문자열함수
08 숫자·날짜·NULL함수
09 CASE 조건식
10 UNION과 UNION ALL
11 서브쿼리
12 JOIN
13 Outer JOIN과 Self JOIN
14 DDL과 제약조건
15 DML
16 Transaction
17 Index와 AUTO_INCREMENT
18 Recursive CTE
19 실무 코딩스타일
20 종합실습
```

SQL Developer-Wiki V3 01~20 학습 복원 과정 완성.

---

## 🔬 V3 종합실습 실행 기록법

### 수업 원본으로 돌아가기

내 코드와 강사님 코드의 `workspace_sql/Script.sql`에서 문제의 핵심 Keyword를 검색하고, 해당 Query 앞의 문제 Comment와 뒤의 확인 Query까지 함께 읽는다. 종합실습의 답과 원본이 다르면 결과 Row·NULL·중복·경계값을 기준으로 실제 차이를 설명한다.

정답 Query만 저장하지 않고 다음을 함께 기록한다.

```text
1. 문제를 자신의 말로 다시 설명
2. 예상 Result Column 작성
3. 기준 Table·관계 Column 기록
4. 입력 Row 확인 Query 실행
5. Query를 한 단계씩 조립
6. 단계별 Row·Group 수 기록
7. 최종 Result Grid 기록
8. NULL·중복·경계값·동점 Test
9. 실패 Query와 Error Message 기록
10. 내 코드·강사님 코드 비교
11. 개선 Query와 이유 작성
12. EXPLAIN 또는 Transaction 결과 확인
```

예를 들어 “부서별 최고 급여와 사원 수”를 풀 때는 먼저 부서·급여순 원본 Row를 조회하고, 그다음 `GROUP BY`, `MAX`, `COUNT`를 추가한다. 사원이 없는 부서까지 보여야 한다면 EMP만 Grouping하는 답으로 충분하지 않으며 DEPT 기준 LEFT JOIN이 필요하다는 추가 질문까지 이어가야 한다.

### V3 최종 체크리스트

- [ ] 입력 Table과 예상 Result Column을 먼저 기록했다.
- [ ] Query를 단계별로 실행하고 Row·Group 수를 확인했다.
- [ ] NULL·중복·0행·경계값·동점을 Test했다.
- [ ] 실패 Query와 Error Message를 함께 기록했다.
- [ ] 내 코드와 강사님 코드의 원본 위치를 찾았다.
- [ ] DML은 변경 전후와 Affected Rows를 확인했다.
- [ ] Transaction은 Commit·Rollback 결과를 확인했다.
- [ ] Index는 EXPLAIN으로 실제 선택 여부를 확인했다.
