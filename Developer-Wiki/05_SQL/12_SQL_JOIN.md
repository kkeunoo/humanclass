# 12. SQL JOIN

> 관계가 있는 여러 Table의 Row와 Column을 하나의 Result Set으로 결합하는 방법

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | 기존 방식 Join, ANSI `INNER JOIN`, `ON`, `USING`, 다중 Table Join |
| 기준 DBMS | MariaDB |
| 실습 테이블 | `EMP`, `DEPT`, `SALGRADE` |
| 선수 학습 | `SELECT`, `WHERE`, `GROUP BY`, Subquery |
| 다음 학습 | Outer Join과 Self Join |
| 문서 버전 | V2 |

> 원본 `Script.sql`의 기존 쉼표 방식 Join과 ANSI JOIN 학습 흐름을 함께 보존했다. 실무 작성은 관계 조건과 Filtering 조건을 분리할 수 있는 명시적 `JOIN ... ON` 문법을 기본으로 한다.

---

## 🎯 학습 목표

- JOIN이 필요한 이유와 UNION·Subquery와의 차이를 설명한다.
- `EMP.DEPTNO = DEPT.DEPTNO` 관계로 두 Table을 결합한다.
- 기존 쉼표 방식과 ANSI `INNER JOIN`을 서로 변환한다.
- `ON`과 `WHERE`, `USING`의 역할과 차이를 이해한다.
- Table Alias로 중복 Column과 모호한 Column 오류를 해결한다.
- 3개 이상의 Table과 범위 조건을 안전하게 연결한다.
- Row 증가, 누락된 조건, 중복 결과를 단계적으로 디버깅한다.

---

## 1. JOIN이 필요한 이유

### 1. Data가 여러 Table에 나뉘어 있다

`EMP`에는 사원과 부서 번호가 있고 `DEPT`에는 부서 이름과 위치가 있다.

```text
EMP.DEPTNO
→ 사원이 속한 부서 번호

DEPT.DEPTNO
→ 부서를 식별하는 번호
```

### 2. 사원 정보에 부서명을 붙인다

```sql
SELECT
    e.empno,
    e.ename,
    e.deptno,
    d.dname,
    d.loc
FROM emp AS e
INNER JOIN dept AS d
    ON d.deptno = e.deptno;
```

### 3. JOIN은 가로 방향 결합이다

```text
JOIN
→ 관계가 맞는 Row의 Column을 가로로 결합

UNION / UNION ALL
→ 구조가 호환되는 결과의 Row를 세로로 결합
```

### 4. JOIN 조건은 Row의 대응 관계를 정의한다

```sql
ON d.deptno = e.deptno
```

같은 번호를 가진 사원 Row와 부서 Row가 결합된다.

### 5. INNER JOIN은 일치하는 Row만 반환한다

`EMP.DEPTNO`와 일치하는 `DEPT.DEPTNO`가 없으면 해당 사원은 INNER JOIN 결과에 포함되지 않는다.

---

## 2. Cartesian Product

### 6. 조건 없이 두 Table을 나열하면 모든 조합이 만들어진다

```sql
SELECT e.empno, e.ename, d.deptno, d.dname
FROM emp AS e
CROSS JOIN dept AS d;
```

### 7. 결과 Row 수는 곱셈이다

```text
EMP 14행 × DEPT 4행
→ 56행
```

실제 Data가 다르면 Row 수도 달라진다.

### 8. CROSS JOIN은 의도적으로 모든 조합을 만들 때 사용한다

```sql
SELECT d.deptno, d.dname, g.grade
FROM dept AS d
CROSS JOIN salgrade AS g
ORDER BY d.deptno, g.grade;
```

### 9. 실수로 생긴 Cartesian Product를 구분한다

```sql
-- 관계 조건이 빠진 실수
SELECT e.ename, d.dname
FROM emp AS e, dept AS d;
```

### 10. 예상 Row 수보다 급격히 많으면 JOIN 조건을 확인한다

특히 Table을 하나 추가했을 때 결과가 곱절 이상 증가하면 그 Table과 기존 Table을 잇는 조건이 있는지 검토한다.

---

## 3. 기존 쉼표 방식 Join

### 11. 수업 원본의 기본 형태

```sql
SELECT e.empno, e.ename, e.deptno, d.dname
FROM emp AS e, dept AS d
WHERE e.deptno = d.deptno;
```

### 12. FROM에는 Table, WHERE에는 관계 조건을 둔다

```text
FROM emp e, dept d
→ 결합 대상 Table

WHERE e.deptno = d.deptno
→ 두 Table의 Row 대응 조건
```

### 13. Filtering 조건도 WHERE에 함께 작성된다

```sql
SELECT e.empno, e.ename, e.sal, d.dname
FROM emp AS e, dept AS d
WHERE e.deptno = d.deptno
  AND e.sal >= 2000;
```

### 14. 관계와 Filtering이 섞여 보인다

조건이 늘어나면 어떤 조건이 Table 관계이고 어떤 조건이 업무 Filtering인지 구분하기 어려워질 수 있다.

### 15. 쉼표 방식은 동작하지만 ANSI JOIN을 권장한다

MariaDB 공식 문서도 가독성, 확장성, 이식성 때문에 명시적 JOIN 문법을 권장한다.

---

## 4. ANSI INNER JOIN

### 16. 기본 문법

```sql
SELECT column_list
FROM table1 AS t1
INNER JOIN table2 AS t2
    ON t1.key_column = t2.key_column;
```

### 17. EMP와 DEPT 결합

```sql
SELECT
    e.empno,
    e.ename,
    e.job,
    d.dname,
    d.loc
FROM emp AS e
INNER JOIN dept AS d
    ON d.deptno = e.deptno;
```

### 18. INNER는 생략할 수 있다

```sql
SELECT e.ename, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

`JOIN`만 작성하면 여기서는 `INNER JOIN`과 같은 의미다.

### 19. 관계 조건은 ON에 둔다

```sql
ON d.deptno = e.deptno
```

### 20. Filtering 조건은 WHERE에 둔다

```sql
SELECT e.ename, e.sal, d.dname
FROM emp AS e
INNER JOIN dept AS d
    ON d.deptno = e.deptno
WHERE e.sal >= 2000;
```

### 21. 관계와 업무 조건이 분리된다

```text
ON
→ Table이 어떻게 연결되는가?

WHERE
→ 연결된 결과 중 어떤 Row가 필요한가?
```

---

## 5. Table Alias와 Column 한정

### 22. Alias로 Query를 간결하게 만든다

```sql
SELECT e.empno, e.ename, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

### 23. 두 Table에 같은 Column명이 있으면 한정한다

`DEPTNO`는 `EMP`와 `DEPT`에 모두 있으므로 `e.deptno` 또는 `d.deptno`로 작성한다.

### 24. 모호한 Column은 오류를 만든다

```sql
-- 오류 가능: deptno가 어느 Table의 Column인지 모호하다.
-- SELECT ename, deptno, dname
-- FROM emp AS e
-- JOIN dept AS d ON d.deptno = e.deptno;
```

### 25. Alias를 지정하면 원래 Table명 대신 Alias를 사용한다

```sql
-- e라는 Alias를 지정한 뒤에는 e.empno처럼 일관되게 작성한다.
SELECT e.empno, e.ename
FROM emp AS e;
```

### 26. 의미가 드러나는 Alias를 선택한다

간단한 Query의 `e`, `d`는 충분하다. 같은 Table이 여러 역할로 등장하면 `employee`, `manager`처럼 역할 중심 Alias가 더 명확할 수 있다.

### 27. SELECT *보다 필요한 Column을 명시한다

```sql
SELECT e.empno, e.ename, e.deptno, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

중복 Column과 불필요한 전송을 줄이고 결과 Schema를 명확히 한다.

---

## 6. ON과 WHERE

### 28. INNER JOIN에서는 같은 결과가 나올 수 있다

```sql
SELECT e.ename, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
   AND e.sal >= 2000;
```

```sql
SELECT e.ename, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
WHERE e.sal >= 2000;
```

현재 INNER JOIN에서는 결과가 같을 수 있다.

### 29. 의미에 따라 위치를 선택한다

`d.deptno = e.deptno`는 관계 조건이므로 `ON`, `e.sal >= 2000`은 최종 Row Filtering이므로 `WHERE`가 읽기 쉽다.

### 30. OUTER JOIN에서는 위치가 결과를 바꿀 수 있다

`ON`과 `WHERE`의 차이는 다음 단원의 `LEFT JOIN`에서 더 중요해진다. INNER JOIN의 결과만 보고 두 위치가 항상 같다고 일반화하지 않는다.

### 31. 여러 관계 조건도 ON에 작성한다

```sql
SELECT a.column1, b.column2
FROM table_a AS a
JOIN table_b AS b
    ON b.key1 = a.key1
   AND b.key2 = a.key2;
```

복합 Key 관계는 필요한 모든 Column을 연결해야 한다.

---

## 7. USING

### 32. 같은 이름의 Column으로 결합할 때 사용할 수 있다

```sql
SELECT e.empno, e.ename, deptno, d.dname
FROM emp AS e
JOIN dept AS d
USING (deptno);
```

### 33. USING에는 Column명만 작성한다

```sql
USING (deptno)
```

`USING (e.deptno)`처럼 Table Alias를 붙이지 않는다.

### 34. 동일 이름이라는 전제가 필요하다

Column명이 다르면 `ON d.department_id = e.deptno`처럼 `ON`을 사용한다.

### 35. 결합 Column이 결과에서 하나로 다뤄진다

`USING (deptno)`를 사용하면 공통 Join Column을 `deptno`로 간결하게 조회할 수 있다.

### 36. 관계를 명시적으로 보여주려면 ON이 유연하다

```sql
SELECT e.empno, e.ename, e.deptno, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

Column명이 다르거나 복합 조건·범위 조건이 있으면 `ON`이 적합하다.

---

## 8. Equi Join과 Non-Equi Join

### 37. Equi Join은 등호로 연결한다

```sql
SELECT e.ename, e.deptno, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

### 38. Non-Equi Join은 등호 이외의 조건을 사용한다

`SALGRADE`는 사원의 급여가 어느 범위에 속하는지로 연결한다.

```sql
SELECT
    e.empno,
    e.ename,
    e.sal,
    g.grade,
    g.losal,
    g.hisal
FROM emp AS e
JOIN salgrade AS g
    ON e.sal BETWEEN g.losal AND g.hisal;
```

### 39. BETWEEN의 양쪽 경계를 포함한다

`BETWEEN g.losal AND g.hisal`은 하한과 상한을 모두 포함한다.

### 40. 범위가 겹치면 한 사원이 여러 등급과 결합될 수 있다

`SALGRADE`의 범위 설계가 서로 겹치지 않는지 확인해야 한다.

### 41. 범위에 빈 구간이 있으면 사원이 누락될 수 있다

INNER JOIN이므로 어떤 등급 범위에도 들어가지 않는 급여는 결과에서 제외된다.

---

## 9. 3개 이상의 Table JOIN

### 42. EMP, DEPT, SALGRADE 결합

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

### 43. JOIN을 하나씩 이어 쓴다

```text
EMP ↔ DEPT
→ 부서 번호로 연결

EMP ↔ SALGRADE
→ 급여 범위로 연결
```

### 44. 새 Table마다 연결 조건을 확인한다

Table 이름만 추가하고 `ON`을 빠뜨리면 의도하지 않은 모든 조합이 만들어질 수 있다.

### 45. 어느 Table을 기준으로 연결하는지 표시한다

`g`는 `d`가 아니라 `e.sal`과 연결된다. Alias를 사용하면 관계 Graph가 명확해진다.

### 46. Filtering은 JOIN 뒤 WHERE에 작성한다

```sql
SELECT e.ename, e.sal, d.dname, g.grade
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
JOIN salgrade AS g
    ON e.sal BETWEEN g.losal AND g.hisal
WHERE d.loc = 'DALLAS'
  AND g.grade >= 3
ORDER BY e.sal DESC, e.empno;
```

---

## 10. JOIN과 집계

### 47. 부서별 사원 수와 평균 급여

```sql
SELECT
    d.deptno,
    d.dname,
    COUNT(*) AS employee_count,
    ROUND(AVG(e.sal), 2) AS avg_salary
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
GROUP BY d.deptno, d.dname
ORDER BY d.deptno;
```

### 48. SELECT의 일반 Column은 GROUP BY와 맞춘다

`d.deptno`, `d.dname`을 조회하므로 두 Column을 Grouping 기준에 포함한다.

### 49. JOIN 뒤 Row 증가가 집계값에 영향을 준다

일대다 관계의 Table을 추가하면 기존 한 Row가 여러 Row로 늘어 `COUNT`, `SUM`, `AVG`가 달라질 수 있다.

### 50. DISTINCT로 무조건 숨기지 않는다

중복처럼 보이는 결과가 정상적인 일대다 관계인지 먼저 확인한다. 잘못된 JOIN을 `DISTINCT`로 덮으면 집계 오류의 원인이 남는다.

### 51. 집계 전 결과를 먼저 관찰한다

```sql
SELECT e.empno, e.ename, d.deptno, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
ORDER BY e.empno;
```

원본 Row 관계를 확인한 뒤 `GROUP BY`를 추가한다.

---

## 11. JOIN과 Subquery 비교

### 52. IN Subquery로 조회

```sql
SELECT e.empno, e.ename, e.deptno
FROM emp AS e
WHERE e.deptno IN (
    SELECT d.deptno
    FROM dept AS d
    WHERE d.loc = 'DALLAS'
);
```

### 53. JOIN으로 조회

```sql
SELECT e.empno, e.ename, e.deptno
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
WHERE d.loc = 'DALLAS';
```

### 54. 필요한 결과 Column으로 선택한다

부서명과 위치까지 필요하면 JOIN이 자연스럽다. 단순한 존재·포함 검사라면 `IN`이나 `EXISTS`가 요구사항을 직접 표현할 수 있다.

### 55. 어느 방식이 항상 더 빠르다고 단정하지 않는다

MariaDB Optimizer가 Query를 변환할 수 있으므로 실제 Schema, Index, Data 분포를 바탕으로 `EXPLAIN`을 확인한다.

---

## 12. 내 코드와 강사님 코드 비교

### 56. 기존 방식 Join

```sql
-- 수업 초반 또는 내 코드에서 사용한 형태
SELECT e.ename, e.deptno, d.dname
FROM emp AS e, dept AS d
WHERE e.deptno = d.deptno
  AND e.sal >= 2000;
```

### 57. ANSI JOIN으로 개선한 형태

```sql
-- 강사님 코드와 함께 비교할 수 있는 명시적 형태
SELECT e.ename, e.deptno, d.dname
FROM emp AS e
INNER JOIN dept AS d
    ON d.deptno = e.deptno
WHERE e.sal >= 2000;
```

두 Query는 현재 INNER JOIN 조건에서 같은 결과를 만든다. 두 번째는 관계 조건과 Filtering 조건이 구분된다.

### 58. 전체 Column을 조회하는 형태

```sql
SELECT *
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

학습 중 구조 확인에는 유용하지만 `DEPTNO`처럼 중복된 Column과 불필요한 Column이 함께 나온다.

### 59. 필요한 Column만 선택한 형태

```sql
SELECT
    e.empno,
    e.ename,
    e.job,
    e.sal,
    d.deptno,
    d.dname,
    d.loc
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

### 60. 비교 결론

- 쉼표 방식은 원본 이해와 변환 연습용으로 남긴다.
- 새 Query는 ANSI `JOIN ... ON`을 기본으로 한다.
- 관계 조건은 `ON`, 결과 Filtering은 `WHERE`로 구분한다.
- 공통 Column은 반드시 Table Alias로 한정한다.
- 중복 제거 전에 관계의 Cardinality와 JOIN 조건을 확인한다.

---

## 13. 개선된 통합 예제

### 61. 사원·부서·급여 등급 보고서

```sql
SELECT
    e.empno,
    e.ename,
    e.job,
    e.sal,
    d.deptno,
    d.dname,
    d.loc,
    g.grade,
    CONCAT(g.losal, ' ~ ', g.hisal) AS grade_range
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
JOIN salgrade AS g
    ON e.sal BETWEEN g.losal AND g.hisal
WHERE e.sal >= 1500
ORDER BY d.deptno, e.sal DESC, e.empno;
```

### 62. 지역별·등급별 집계 보고서

```sql
SELECT
    d.loc,
    g.grade,
    COUNT(*) AS employee_count,
    SUM(e.sal) AS salary_sum,
    ROUND(AVG(e.sal), 2) AS avg_salary
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
JOIN salgrade AS g
    ON e.sal BETWEEN g.losal AND g.hisal
GROUP BY d.loc, g.grade
HAVING COUNT(*) >= 1
ORDER BY d.loc, g.grade;
```

### 63. 관계를 단계적으로 읽는다

```text
1. EMP에서 사원을 가져온다.
2. DEPTNO로 DEPT를 연결한다.
3. SAL 범위로 SALGRADE를 연결한다.
4. WHERE로 필요한 사원을 남긴다.
5. GROUP BY가 있으면 결합된 Row를 집계한다.
6. ORDER BY로 최종 결과를 정렬한다.
```

---

## 14. 실무 활용 지침

### 64. 관계를 먼저 Diagram처럼 적는다

```text
EMP.DEPTNO = DEPT.DEPTNO
EMP.SAL BETWEEN SALGRADE.LOSAL AND SALGRADE.HISAL
```

### 65. 예상 Cardinality를 정한다

```text
사원 1명 → 부서 1개
사원 1명 → 급여 등급 1개
부서 1개 → 사원 여러 명
```

실제 결과가 예상과 다르면 Data 또는 조건을 점검한다.

### 66. Foreign Key와 JOIN은 같은 개념이 아니다

Foreign Key는 Data 무결성을 보장하는 Schema 제약이고, JOIN은 Query에서 Row를 결합하는 연산이다. FK가 없어도 Join할 수 있지만 관계의 유효성을 별도로 책임져야 한다.

### 67. Index를 추측으로 강제하지 않는다

Join Key의 Index는 성능에 중요할 수 있지만 `FORCE INDEX`를 먼저 사용하지 말고 `EXPLAIN`과 실제 실행을 확인한다.

### 68. SELECT 목록과 정렬 기준을 명시한다

Application Query는 `SELECT *`와 정렬 없는 결과 순서에 의존하지 않는다.

---

## 15. 자주 하는 실수

### 69. JOIN 조건을 빠뜨린다

결과 Row가 두 Table Row 수의 곱처럼 증가하면 관계 조건을 확인한다.

### 70. 잘못된 Column끼리 연결한다

```sql
-- 이름이 비슷하다는 이유만으로 의미가 다른 값을 연결하면 안 된다.
-- ON e.empno = d.deptno
```

### 71. 모호한 Column명을 그대로 사용한다

공통 이름은 `e.deptno`, `d.deptno`처럼 Source를 명확히 한다.

### 72. ON에 모든 업무 조건을 몰아넣는다

INNER JOIN에서 결과가 같더라도 관계와 Filtering의 의도를 나누어 작성한다.

### 73. USING에 한정된 Column명을 작성한다

```sql
-- 잘못된 형태
-- USING (e.deptno)

-- 올바른 형태
USING (deptno)
```

### 74. 중복 Row를 DISTINCT로 먼저 제거한다

중복 원인이 누락된 조건인지 정상적인 일대다 관계인지 먼저 조사한다.

### 75. INNER JOIN으로 보존되지 않는 Row를 놓친다

일치하지 않는 Row도 보여야 한다면 다음 단원의 `LEFT JOIN` 같은 Outer Join이 필요하다.

---

## 16. 디버깅 방법

### 76. 각 Table을 독립적으로 확인한다

```sql
SELECT empno, ename, deptno FROM emp ORDER BY empno;
SELECT deptno, dname, loc FROM dept ORDER BY deptno;
```

### 77. Join Key만 먼저 조회한다

```sql
SELECT e.empno, e.deptno AS emp_deptno, d.deptno AS dept_deptno
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
ORDER BY e.empno;
```

### 78. Table을 하나씩 추가한다

먼저 `EMP ↔ DEPT` 결과를 확인하고 그 다음 `SALGRADE`를 추가한다.

### 79. COUNT로 단계별 Row 수를 비교한다

```sql
SELECT COUNT(*) AS emp_count FROM emp;

SELECT COUNT(*) AS joined_count
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

### 80. 일치하지 않는 Key를 찾는다

```sql
SELECT e.empno, e.ename, e.deptno
FROM emp AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM dept AS d
    WHERE d.deptno = e.deptno
);
```

### 81. EXPLAIN으로 실행 계획을 확인한다

```sql
EXPLAIN
SELECT e.empno, e.ename, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

### 82. 범위 Join의 중복을 검사한다

```sql
SELECT e.empno, COUNT(*) AS matched_grade_count
FROM emp AS e
JOIN salgrade AS g
    ON e.sal BETWEEN g.losal AND g.hisal
GROUP BY e.empno
HAVING COUNT(*) <> 1;
```

결과가 있다면 급여 등급 범위의 겹침이나 빈 구간을 확인한다.

---

## 17. 종합실습

### 83. 문제 1 — 사원과 부서 정보

사원 번호, 이름, 부서 번호, 부서명, 부서 위치를 ANSI INNER JOIN으로 조회한다.

### 84. 문제 2 — 특정 지역 사원

`DALLAS`에서 근무하는 사원의 이름, 직무, 급여, 부서명을 조회한다.

### 85. 문제 3 — 급여 등급

각 사원의 이름, 급여, 급여 등급과 등급 범위를 조회한다.

### 86. 문제 4 — 3개 Table 통합

사원 이름, 부서명, 위치, 급여, 급여 등급을 조회하고 부서 번호와 급여 내림차순으로 정렬한다.

### 87. 문제 5 — 부서별 집계

부서별 사원 수, 급여 합계, 평균 급여를 조회한다. 부서 번호와 부서명을 함께 표시한다.

---

## 18. 정답과 해설

### 88. 문제 1 정답

```sql
SELECT e.empno, e.ename, e.deptno, d.dname, d.loc
FROM emp AS e
INNER JOIN dept AS d
    ON d.deptno = e.deptno
ORDER BY e.empno;
```

두 Table의 공통 관계인 `DEPTNO`를 `ON`에서 연결한다.

### 89. 문제 2 정답

```sql
SELECT e.ename, e.job, e.sal, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
WHERE d.loc = 'DALLAS'
ORDER BY e.empno;
```

관계는 `ON`, 지역 Filtering은 `WHERE`에 둔다.

### 90. 문제 3 정답

```sql
SELECT e.ename, e.sal, g.grade, g.losal, g.hisal
FROM emp AS e
JOIN salgrade AS g
    ON e.sal BETWEEN g.losal AND g.hisal
ORDER BY g.grade, e.sal, e.empno;
```

등호가 아닌 급여 범위로 연결하는 Non-Equi Join이다.

### 91. 문제 4 정답

```sql
SELECT e.ename, d.dname, d.loc, e.sal, g.grade
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
JOIN salgrade AS g
    ON e.sal BETWEEN g.losal AND g.hisal
ORDER BY d.deptno, e.sal DESC, e.empno;
```

각 Table이 어떤 Column과 연결되는지 두 개의 `ON` 조건으로 표현한다.

### 92. 문제 5 정답

```sql
SELECT
    d.deptno,
    d.dname,
    COUNT(*) AS employee_count,
    SUM(e.sal) AS salary_sum,
    ROUND(AVG(e.sal), 2) AS avg_salary
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
GROUP BY d.deptno, d.dname
ORDER BY d.deptno;
```

INNER JOIN이므로 사원이 존재하는 부서만 집계된다. 사원이 없는 부서까지 표시하는 방법은 다음 Outer Join 단원에서 다룬다.

---

## 19. 최종 체크리스트

### 93. 문법 체크

- [ ] 각 JOIN에 필요한 `ON` 또는 `USING`이 있는가?
- [ ] 동일 이름의 Column을 Table Alias로 한정했는가?
- [ ] `USING`에는 한정하지 않은 공통 Column명만 작성했는가?
- [ ] 필요한 Column만 SELECT 목록에 작성했는가?

### 94. 논리 체크

- [ ] 관계 조건과 결과 Filtering 조건을 구분했는가?
- [ ] 예상한 1:1, 1:N 관계와 실제 Row 수가 일치하는가?
- [ ] INNER JOIN에서 누락되는 불일치 Row가 있어도 되는가?
- [ ] 범위 Join의 구간이 겹치거나 비어 있지 않은가?

### 95. 품질 체크

- [ ] 새 Query는 명시적 ANSI JOIN으로 작성했는가?
- [ ] 중복을 `DISTINCT`로 숨기기 전에 원인을 확인했는가?
- [ ] 3개 이상 Table의 연결 관계를 모두 설명할 수 있는가?
- [ ] 성능을 `EXPLAIN`과 실제 Data로 검증했는가?

---

## 20. 핵심 요약

### 96. JOIN 핵심 문장

```text
INNER JOIN
→ 관계 조건과 일치하는 Row만 결합

ON
→ Table 사이의 관계 조건

WHERE
→ 결합된 결과의 Filtering 조건

USING
→ 양쪽에 이름이 같은 Join Column을 간결하게 지정

Equi Join
→ 등호로 연결

Non-Equi Join
→ 범위 등 등호 이외의 조건으로 연결
```

### 97. 최종 정리

JOIN의 핵심은 문법보다 **Table 사이의 관계와 결과 Row 수를 예측하는 것**이다. 새 Query는 `JOIN ... ON`으로 관계를 명시하고, Filtering은 `WHERE`로 분리한다. Table을 추가할 때마다 연결 조건과 Cardinality를 확인하고, 예상하지 못한 중복이나 누락은 `DISTINCT`보다 Join Key와 원본 Data부터 점검한다.

---

## 📎 다음 문서

다음 원본 흐름은 일치하지 않는 Row를 보존하는 Outer Join과 같은 Table을 역할별로 연결하는 Self Join이다.

```text
13_SQL_Outer_JOIN과_Self_JOIN.md
```
