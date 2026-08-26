# 10. SQL UNION과 UNION ALL

> 여러 SELECT 결과를 위아래로 결합하는 SQL 집합연산

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | `UNION`, `UNION ALL` |
| 기준 DBMS | MariaDB |
| 실습 테이블 | `EMP`, `DEPT` |
| 선수 학습 | `SELECT`, `WHERE`, `ORDER BY`, 함수, `CASE`, `GROUP BY`, `HAVING` |
| 다음 학습 | Subquery |
| 문서 버전 | V3 Encyclopedia |

> 원본 `Script.sql`에서 `CASE`와 Grouping 학습 뒤에 이어지는 집합연산 범위를 기준으로 구성했다. `GROUP BY`와 `HAVING`은 06번에서 먼저 정리했으므로, 10번은 다음 미작성 주제인 `UNION`과 `UNION ALL`을 다룬다.

---

## 🎯 학습 목표

- `UNION`과 `UNION ALL`의 공통점과 차이를 설명한다.
- 결합되는 SELECT의 Column 개수와 위치별 자료형을 맞춘다.
- 중복 제거가 필요한지 판단하여 적절한 연산자를 선택한다.
- 결과 Column명과 `ORDER BY`의 적용 범위를 이해한다.
- 서로 다른 형태의 결과를 `NULL`, Literal, `CAST`로 정렬한다.
- 집합연산 오류를 단계적으로 디버깅하고 실무 보고서 Query에 활용한다.

---

## 1. 집합연산이 필요한 이유

### 1. 여러 SELECT 결과를 하나로 합치기

`UNION` 계열 연산자는 두 Query의 결과를 세로 방향으로 이어 붙인다.

```text
첫 번째 SELECT 결과
        ↓
두 번째 SELECT 결과
        ↓
하나의 Result Set
```

### 2. JOIN과 방향이 다르다

```text
JOIN
→ 관계가 있는 Table의 Column을 가로로 결합

UNION / UNION ALL
→ 구조가 호환되는 SELECT 결과의 Row를 세로로 결합
```

### 3. 가장 단순한 UNION ALL

```sql
SELECT 'EMP' AS source_name, empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT 'DEPT', deptno, dname
FROM dept;
```

### 4. 집합연산의 기본 구조

```sql
SELECT column1, column2
FROM table1
UNION ALL
SELECT column1, column2
FROM table2;
```

각 SELECT를 집합연산의 **분기(Branch)** 라고 생각하면 구조를 이해하기 쉽다.

---

## 2. UNION ALL

### 5. UNION ALL은 모든 Row를 유지한다

```sql
SELECT deptno
FROM emp
UNION ALL
SELECT deptno
FROM dept;
```

`EMP`와 `DEPT`에서 나온 값이 같아도 제거하지 않는다.

### 6. 중복도 의미 있는 Data일 수 있다

```sql
SELECT job AS category
FROM emp
WHERE deptno = 20
UNION ALL
SELECT job
FROM emp
WHERE deptno = 30;
```

같은 직무를 가진 사원이 여러 명이라면 각 Row는 서로 다른 사원에서 온 관측값이다. 단순히 값이 같다고 제거하면 인원 정보가 사라진다.

### 7. Row 수는 각 분기 Row 수의 합이다

```sql
SELECT COUNT(*) AS row_count
FROM (
    SELECT empno
    FROM emp
    WHERE deptno = 10
    UNION ALL
    SELECT empno
    FROM emp
    WHERE deptno = 20
) AS combined_emp;
```

두 조건이 겹치지 않는다면 결과 Row 수는 각 부서 인원수의 합과 같다.

### 8. 중복 제거가 필요 없으면 UNION ALL을 우선 검토한다

`UNION ALL`은 중복 제거 단계를 요구하지 않는다. 따라서 중복을 허용해야 하거나 분기 간 중복이 발생하지 않는 구조라면 의도가 더 명확하다.

### 9. 출처 Column을 추가하면 결과를 추적하기 쉽다

```sql
SELECT 'DEPT10' AS source_group, empno, ename
FROM emp
WHERE deptno = 10
UNION ALL
SELECT 'DEPT20', empno, ename
FROM emp
WHERE deptno = 20;
```

---

## 3. UNION

### 10. UNION은 전체 결과에서 중복 Row를 제거한다

```sql
SELECT job
FROM emp
WHERE deptno = 20
UNION
SELECT job
FROM emp
WHERE deptno = 30;
```

중복 판단은 특정 Column 하나가 아니라 SELECT 목록 전체를 기준으로 한다.

### 11. 모든 Column 값이 같아야 중복이다

```sql
SELECT deptno, job
FROM emp
WHERE deptno IN (10, 20)
UNION
SELECT deptno, job
FROM emp
WHERE deptno IN (20, 30);
```

`DEPTNO`와 `JOB`이 모두 같은 Row만 하나로 합쳐진다.

### 12. 일부 Column만 같으면 다른 Row다

```sql
SELECT empno, job
FROM emp
WHERE deptno = 20
UNION
SELECT empno, job
FROM emp
WHERE deptno = 30;
```

`JOB`이 같아도 `EMPNO`가 다르면 중복이 아니다.

### 13. DISTINCT와 UNION의 관계

```text
SELECT DISTINCT
→ 한 SELECT 결과 내부의 중복 제거

UNION
→ 결합된 전체 SELECT 결과의 중복 제거
```

### 14. 중복 제거가 업무 요구사항인지 먼저 확인한다

사원 명단, 거래 이력, Log처럼 각 Row 자체가 의미를 가지면 `UNION ALL`이 자연스럽다. 여러 경로에서 수집한 고유 Category 목록처럼 유일한 값만 필요하면 `UNION`을 사용할 수 있다.

---

## 4. UNION과 UNION ALL 비교

### 15. 핵심 차이

| 항목 | `UNION` | `UNION ALL` |
|---|---|---|
| 중복 Row | 제거 | 유지 |
| 결과 의미 | 고유한 Row 집합 | 모든 Row의 연결 |
| 추가 처리 | 중복 제거 필요 | 단순 결합 |
| 권장 상황 | 중복 제거가 요구사항 | 중복 유지 또는 중복 불가능 |

### 16. 같은 입력으로 결과 차이 확인하기

```sql
SELECT 10 AS deptno
UNION
SELECT 10;
```

결과는 한 Row다.

```sql
SELECT 10 AS deptno
UNION ALL
SELECT 10;
```

결과는 두 Row다.

### 17. UNION이 항상 더 좋은 것은 아니다

중복이 생긴 원인을 모른 채 `UNION`으로 숨기면 Data 또는 Query 설계 문제를 놓칠 수 있다. 필요한 결과가 전체 이력이라면 중복처럼 보이는 Row도 보존해야 한다.

### 18. UNION ALL 뒤에 필요한 기준으로 집계할 수 있다

```sql
SELECT job, COUNT(*) AS employee_count
FROM (
    SELECT job
    FROM emp
    WHERE deptno = 20
    UNION ALL
    SELECT job
    FROM emp
    WHERE deptno = 30
) AS combined_jobs
GROUP BY job
ORDER BY job;
```

먼저 모든 Row를 보존한 뒤 바깥 Query에서 목적에 맞게 집계하는 방식이다.

---

## 5. 결합 조건: Column 개수와 순서

### 19. SELECT Column 개수가 같아야 한다

```sql
-- 오류: 첫 번째 SELECT는 2개, 두 번째 SELECT는 1개
-- SELECT empno, ename FROM emp
-- UNION ALL
-- SELECT deptno FROM dept;
```

### 20. 부족한 위치는 의미 있는 값으로 채운다

```sql
SELECT empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT deptno, dname
FROM dept;
```

### 21. Column은 이름이 아니라 위치끼리 대응한다

```sql
SELECT empno, ename
FROM emp
UNION ALL
SELECT deptno, dname
FROM dept;
```

첫 번째 위치의 `EMPNO`와 `DEPTNO`, 두 번째 위치의 `ENAME`과 `DNAME`이 각각 대응한다.

### 22. 의미가 다른 Column을 같은 위치에 두지 않는다

```sql
-- 개수와 자료형이 맞아도 의미가 잘못 연결된다.
-- SELECT empno, ename FROM emp
-- UNION ALL
-- SELECT deptno, loc FROM dept;
```

문법적으로 실행되는 것과 올바른 보고서인 것은 다르다.

### 23. 공통 결과 Schema를 먼저 설계한다

```text
1번 Column: source_type
2번 Column: object_no
3번 Column: object_name
4번 Column: detail_text
```

각 분기가 이 구조에 맞는 값을 같은 순서로 반환하도록 작성한다.

---

## 6. 자료형 맞추기

### 24. 위치별 자료형은 서로 호환되어야 한다

```sql
SELECT empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT deptno, dname
FROM dept;
```

숫자 위치에는 숫자, 문자열 위치에는 문자열을 두는 것이 가장 안전하다.

### 25. CAST로 결과형을 명확히 한다

```sql
SELECT CAST(empno AS CHAR) AS object_code, ename AS object_name
FROM emp
UNION ALL
SELECT CONCAT('D-', deptno), dname
FROM dept;
```

### 26. NULL Placeholder를 사용할 수 있다

```sql
SELECT
    'EMP' AS source_type,
    empno AS object_no,
    ename AS object_name,
    job AS detail_text
FROM emp
UNION ALL
SELECT
    'DEPT',
    deptno,
    dname,
    NULL
FROM dept;
```

### 27. NULL에도 의도한 자료형을 표시할 수 있다

```sql
SELECT empno AS object_no, sal AS amount
FROM emp
UNION ALL
SELECT deptno, CAST(NULL AS DECIMAL(10, 2))
FROM dept;
```

복잡한 Query에서는 Typed NULL이 결과 Schema를 더 분명하게 만든다.

### 28. 날짜와 문자열을 무심코 섞지 않는다

표시용 Text가 목적이면 각 분기에서 `DATE_FORMAT`을 사용하고, 날짜 계산이 목적이면 날짜형을 유지한다.

```sql
SELECT ename AS object_name, DATE_FORMAT(hiredate, '%Y-%m-%d') AS event_date
FROM emp
UNION ALL
SELECT dname, NULL
FROM dept;
```

---

## 7. Column명과 Alias

### 29. 최종 Column명은 첫 번째 SELECT를 기준으로 한다

```sql
SELECT empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT deptno AS department_number, dname AS department_name
FROM dept;
```

최종 Header는 `OBJECT_NO`, `OBJECT_NAME`이다. 두 번째 분기의 Alias는 최종 Header를 바꾸지 않는다.

### 30. 첫 번째 SELECT의 Alias를 명확히 작성한다

```sql
SELECT
    'EMP' AS source_type,
    empno AS object_no,
    ename AS object_name
FROM emp
UNION ALL
SELECT 'DEPT', deptno, dname
FROM dept;
```

### 31. 분기별 Alias보다 공통 의미가 중요하다

`empno`, `deptno`를 합친 Column을 단순히 `empno`라고 두기보다 `object_no`처럼 두 Source를 포괄하는 이름이 적합하다.

---

## 8. ORDER BY와 LIMIT

### 32. 전체 결과 정렬은 마지막에 한 번 작성한다

```sql
SELECT 'EMP' AS source_type, empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT 'DEPT', deptno, dname
FROM dept
ORDER BY source_type, object_no;
```

### 33. ORDER BY는 결합된 전체 Result Set에 적용된다

마지막 `ORDER BY`는 바로 앞 SELECT에만 적용되는 것이 아니다.

### 34. 최종 결과 Column명을 사용한다

```sql
SELECT empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT deptno, dname
FROM dept
ORDER BY object_name, object_no;
```

### 35. Position 정렬도 가능하지만 주의한다

```sql
SELECT empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT deptno, dname
FROM dept
ORDER BY 2, 1;
```

Column 순서가 바뀌면 의미도 바뀌므로 유지보수에는 Alias가 더 안전하다.

### 36. 전체 결과의 Top-N

```sql
SELECT 'EMP' AS source_type, empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT 'DEPT', deptno, dname
FROM dept
ORDER BY object_no
LIMIT 5;
```

`LIMIT`도 마지막에 작성하면 결합된 전체 결과에 적용된다.

### 37. 각 분기를 먼저 정렬하거나 제한하려면 감싼다

```sql
SELECT source_type, object_no, object_name
FROM (
    SELECT 'HIGH_SAL' AS source_type, empno AS object_no, ename AS object_name
    FROM emp
    ORDER BY sal DESC, empno
    LIMIT 3
) AS high_salary
UNION ALL
SELECT source_type, object_no, object_name
FROM (
    SELECT 'RECENT' AS source_type, empno AS object_no, ename AS object_name
    FROM emp
    ORDER BY hiredate DESC, empno
    LIMIT 3
) AS recent_hire
ORDER BY source_type, object_no;
```

내부 Top-N과 최종 전체 정렬은 서로 다른 단계다.

---

## 9. 내 코드와 강사님 코드 비교

### 38. 비교 기준

원본의 두 작성 흐름은 단순히 정답과 오답으로 나누기보다 **중복 보존 의도, 결과 추적성, 정렬 범위**를 중심으로 비교한다.

### 39. UNION으로 고유 값만 조회하는 형태

```sql
-- 내 코드에서 선택할 수 있는 형태
SELECT job
FROM emp
WHERE deptno = 20
UNION
SELECT job
FROM emp
WHERE deptno = 30;
```

두 부서에 존재하는 직무 종류의 고유 목록이 목적이면 적절하다.

### 40. UNION ALL로 원본 Row를 보존하는 형태

```sql
-- 강사님 코드와 함께 비교할 수 있는 형태
SELECT deptno, job
FROM emp
WHERE deptno = 20
UNION ALL
SELECT deptno, job
FROM emp
WHERE deptno = 30;
```

사원별 직무 Row를 모두 유지하려면 `UNION ALL`이 맞다. `DEPTNO`도 남겨 출처를 확인할 수 있다.

### 41. 차이는 연산자 하나가 아니라 결과 의미다

```text
UNION + JOB만 조회
→ 고유한 직무 종류

UNION ALL + DEPTNO, JOB 조회
→ 각 부서에서 발생한 모든 직무 Row
```

### 42. 공통 개선점

- 결과의 업무 의미를 먼저 한 문장으로 정의한다.
- 분기마다 Column 개수·순서·자료형을 맞춘다.
- Source를 구분해야 하면 Literal 또는 원본 Key를 남긴다.
- 전체 정렬은 마지막 `ORDER BY`로 명시한다.
- 중복을 숨기기 위한 `UNION` 사용은 피한다.

---

## 10. 개선된 통합 예제

### 43. 사원과 부서를 하나의 검색 목록으로 만들기

```sql
SELECT
    'EMPLOYEE' AS object_type,
    CAST(empno AS CHAR) AS object_code,
    ename AS object_name,
    CONCAT('JOB=', job, ', DEPT=', COALESCE(deptno, 'NULL')) AS detail_text
FROM emp
UNION ALL
SELECT
    'DEPARTMENT',
    CAST(deptno AS CHAR),
    dname,
    CONCAT('LOCATION=', loc)
FROM dept
ORDER BY object_type, object_code;
```

### 44. 부서별 요약과 전체 요약을 한 보고서로 만들기

```sql
SELECT
    CAST(deptno AS CHAR) AS group_code,
    COUNT(*) AS employee_count,
    ROUND(AVG(sal), 2) AS avg_salary,
    1 AS sort_order
FROM emp
GROUP BY deptno
UNION ALL
SELECT
    'TOTAL',
    COUNT(*),
    ROUND(AVG(sal), 2),
    2
FROM emp
ORDER BY sort_order, group_code;
```

`sort_order`를 결과에 포함하면 전체 합계를 마지막에 안정적으로 배치할 수 있다.

### 45. 서로 다른 조건의 대상자를 출처와 함께 결합하기

```sql
SELECT 'HIGH_SALARY' AS selected_by, empno, ename, sal
FROM emp
WHERE sal >= 3000
UNION ALL
SELECT 'COMMISSION' AS selected_by, empno, ename, sal
FROM emp
WHERE comm IS NOT NULL AND comm > 0
ORDER BY empno, selected_by;
```

한 사원이 두 조건을 모두 만족하면 두 Row가 나온다. 조건별 선발 이력을 보존하려는 의도다.

### 46. 고유 사원 명단만 필요할 때

```sql
SELECT empno, ename
FROM emp
WHERE sal >= 3000
UNION
SELECT empno, ename
FROM emp
WHERE comm IS NOT NULL AND comm > 0
ORDER BY empno;
```

이번에는 선발 사유가 아니라 고유 사원 명단이 목적이므로 `UNION`이 적합하다.

---

## 11. 실무 활용 지침

### 47. 먼저 결과 한 Row의 의미를 정한다

```text
한 Row = 한 사원
한 Row = 한 선발 사유
한 Row = 한 직무 종류
한 Row = 한 부서 요약
```

Row의 의미가 정해져야 중복 제거 여부도 결정할 수 있다.

### 48. 분기별 필터는 각 SELECT의 WHERE에 둔다

```sql
SELECT 'DEPT10' AS source_group, empno, ename
FROM emp
WHERE deptno = 10
UNION ALL
SELECT 'DEPT30', empno, ename
FROM emp
WHERE deptno = 30;
```

### 49. 전체 결과 필터는 Derived Table 또는 CTE로 감싼다

```sql
WITH combined AS (
    SELECT 'EMP' AS source_type, empno AS object_no, ename AS object_name
    FROM emp
    UNION ALL
    SELECT 'DEPT', deptno, dname
    FROM dept
)
SELECT source_type, object_no, object_name
FROM combined
WHERE object_name LIKE 'S%'
ORDER BY source_type, object_no;
```

### 50. 반복되는 보고서 Schema를 문서화한다

Column의 이름뿐 아니라 의미, 자료형, NULL 허용 여부를 정하면 새 분기를 추가할 때 오류가 줄어든다.

### 51. 성능 판단도 요구사항 다음이다

중복 제거가 필요하면 `UNION`을 사용해야 한다. 다만 필요하지 않은 중복 제거를 습관적으로 추가하지 않는다. 실행 계획과 실제 Data 규모로 확인한다.

---

## 12. 자주 하는 실수

### 52. Column 개수를 다르게 작성한다

오류가 나면 각 SELECT를 따로 실행한 뒤 SELECT 목록의 개수를 센다.

### 53. Column 순서를 뒤바꾼다

```sql
-- 이름과 번호의 위치가 뒤바뀐 잘못된 설계
-- SELECT empno, ename FROM emp
-- UNION ALL
-- SELECT dname, deptno FROM dept;
```

### 54. 중복이 싫다는 이유만으로 UNION을 사용한다

중복처럼 보이는 Row가 실제로는 서로 다른 사건이나 사원을 나타낼 수 있다. 먼저 Primary Key 또는 Source Column을 조회해 원인을 확인한다.

### 55. 각 SELECT 뒤에 ORDER BY를 바로 작성한다

집합 전체 정렬은 마지막에 한 번 작성한다. 분기별 Top-N이 목적이면 각 분기를 Derived Table로 감싼다.

### 56. 두 번째 SELECT의 Alias로 정렬한다

최종 Column명은 첫 번째 SELECT에서 결정된다. 마지막 `ORDER BY`에는 최종 Alias를 사용한다.

### 57. 숫자·문자열·날짜를 무계획하게 섞는다

암시적 형 변환에 의존하지 말고 공통 결과 Schema를 정한 뒤 필요하면 `CAST`한다.

### 58. UNION으로 JOIN을 대신한다

사원 Row에 부서명을 붙이는 작업은 세로 결합이 아니라 관계에 따른 가로 결합이므로 JOIN을 사용한다.

---

## 13. 디버깅 방법

### 59. 각 SELECT를 독립 실행한다

각 분기의 Column 개수, 순서, 자료형, Row 수를 먼저 확인한다.

### 60. LIMIT 0으로 결과 Header를 확인한다

```sql
SELECT 'EMP' AS source_type, empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT 'DEPT', deptno, dname
FROM dept
LIMIT 0;
```

Client에 따라 Data 없이 최종 Column 구조를 빠르게 확인할 수 있다.

### 61. 출처 Column을 임시로 추가한다

```sql
SELECT 'BRANCH_1' AS debug_source, empno, ename
FROM emp
WHERE deptno = 20
UNION ALL
SELECT 'BRANCH_2', empno, ename
FROM emp
WHERE deptno = 30;
```

### 62. UNION ALL로 먼저 Row를 관찰한다

중복 제거 전 결과를 확인하면 어떤 Row가 겹치는지 알 수 있다. 그 후 요구사항이 고유 집합이라면 `UNION`으로 바꾼다.

### 63. 분기별 Row 수와 최종 Row 수를 비교한다

```sql
SELECT source_name, COUNT(*) AS row_count
FROM (
    SELECT 'DEPT20' AS source_name, empno
    FROM emp
    WHERE deptno = 20
    UNION ALL
    SELECT 'DEPT30', empno
    FROM emp
    WHERE deptno = 30
) AS debug_rows
GROUP BY source_name;
```

### 64. 복잡한 집합연산은 CTE로 이름을 붙인다

분기마다 업무 의미를 나타내는 이름을 붙이면 조건과 Column Mapping을 검증하기 쉽다.

---

## 14. 종합실습

### 65. 문제 1 — 고유 직무 목록

20번 부서와 30번 부서에 존재하는 직무의 고유 목록을 조회한다.

### 66. 문제 2 — 모든 사원 Row 유지

10번 부서와 20번 부서 사원을 하나로 합치되, 소속 부서와 모든 사원 Row를 유지한다.

### 67. 문제 3 — 통합 검색 목록

사원과 부서를 `OBJECT_TYPE`, `OBJECT_NO`, `OBJECT_NAME` 구조로 합치고 Type과 번호순으로 정렬한다.

### 68. 문제 4 — 부서별 요약과 전체 합계

부서별 인원수와 급여 합계를 조회하고 마지막 Row에 전체 인원수와 전체 급여 합계를 추가한다.

### 69. 문제 5 — 두 선발 조건 비교

급여 3000 이상 또는 Commission이 양수인 사원의 고유 명단을 만든다. 같은 사원이 두 조건을 만족해도 한 번만 표시한다.

---

## 15. 정답과 해설

### 70. 문제 1 정답

```sql
SELECT job
FROM emp
WHERE deptno = 20
UNION
SELECT job
FROM emp
WHERE deptno = 30
ORDER BY job;
```

직무의 고유 목록이 목적이므로 `UNION`을 사용한다.

### 71. 문제 2 정답

```sql
SELECT deptno, empno, ename
FROM emp
WHERE deptno = 10
UNION ALL
SELECT deptno, empno, ename
FROM emp
WHERE deptno = 20
ORDER BY deptno, empno;
```

사원 Row를 모두 유지해야 하므로 `UNION ALL`을 사용한다.

### 72. 문제 3 정답

```sql
SELECT 'EMP' AS object_type, empno AS object_no, ename AS object_name
FROM emp
UNION ALL
SELECT 'DEPT', deptno, dname
FROM dept
ORDER BY object_type, object_no;
```

첫 번째 SELECT의 Alias가 최종 Header가 된다.

### 73. 문제 4 정답

```sql
SELECT
    CAST(deptno AS CHAR) AS group_name,
    COUNT(*) AS employee_count,
    SUM(sal) AS salary_sum,
    1 AS sort_order
FROM emp
GROUP BY deptno
UNION ALL
SELECT
    'TOTAL',
    COUNT(*),
    SUM(sal),
    2
FROM emp
ORDER BY sort_order, group_name;
```

부서별 집계와 전체 집계는 결과 Schema가 같으므로 세로로 결합할 수 있다.

### 74. 문제 5 정답

```sql
SELECT empno, ename
FROM emp
WHERE sal >= 3000
UNION
SELECT empno, ename
FROM emp
WHERE comm IS NOT NULL AND comm > 0
ORDER BY empno;
```

고유 사원 명단이 목적이므로 두 조건을 모두 만족하는 사원의 동일한 `EMPNO`, `ENAME` Row는 하나로 합쳐진다.

---

## 16. 최종 체크리스트

### 75. 문법 체크

- [ ] 모든 SELECT의 Column 개수가 같은가?
- [ ] 같은 위치의 자료형이 호환되는가?
- [ ] Column 순서가 공통 결과 Schema와 일치하는가?
- [ ] 전체 `ORDER BY`와 `LIMIT`을 마지막에 작성했는가?

### 76. 논리 체크

- [ ] 결과 한 Row의 업무 의미를 정의했는가?
- [ ] 중복을 제거해야 하는 이유가 명확한가?
- [ ] Source 구분이 필요하면 출처 Column을 남겼는가?
- [ ] `UNION`이 Query 문제를 숨기고 있지 않은가?

### 77. 품질 체크

- [ ] 첫 SELECT에 공통 의미의 Alias를 작성했는가?
- [ ] 암시적 형 변환 대신 필요한 `CAST`를 사용했는가?
- [ ] 분기별 Top-N과 전체 Top-N을 구분했는가?
- [ ] 세로 결합은 UNION, 가로 결합은 JOIN이라는 목적이 맞는가?

---

## 17. 핵심 요약

### 78. UNION 핵심 문장

```text
UNION ALL
→ 모든 Row를 그대로 세로 결합

UNION
→ 세로 결합 후 SELECT 목록 전체 기준으로 중복 제거

결합 조건
→ Column 개수 동일, 위치별 의미와 자료형 호환

최종 Column명
→ 첫 번째 SELECT 기준

ORDER BY
→ 마지막에 작성하여 전체 결과에 적용
```

### 79. 최종 정리

`UNION`과 `UNION ALL`의 선택 기준은 단순히 중복이 보이는지가 아니라 **결과 한 Row가 무엇을 의미하는가**이다. 모든 사건과 Source Row를 보존하려면 `UNION ALL`, 여러 경로에서 얻은 고유 대상을 만들려면 `UNION`을 사용한다. 작성 전에는 공통 결과 Schema를 정하고, 작성 후에는 각 분기와 전체 결과의 Row 수·자료형·정렬 범위를 검증한다.

---

## 📎 다음 문서

다음 원본 흐름은 Subquery이다.

```text
11_SQL_서브쿼리.md
```

---

## 🔬 V3 동작 백과 — 두 Result Set은 어떻게 합쳐지는가?

```sql
SELECT empno, ename, 'HIGH' AS source
FROM emp
WHERE sal >= 3000

UNION ALL

SELECT empno, ename, 'DEPT10' AS source
FROM emp
WHERE deptno = 10;
```

```text
첫 SELECT 독립 실행
→ 급여 3000 이상 Result Set A

두 번째 SELECT 독립 실행
→ 10번 부서 Result Set B

UNION ALL
→ A 아래에 B를 그대로 이어 붙임
→ 같은 사원이 양쪽에 있으면 두 번 출력
```

`UNION`이라면 결합 후 **선택한 모든 Column 조합**이 같은 Row를 중복 제거한다. 위 예제는 `source` 값이 다르므로 같은 사원도 완전히 같은 Row가 아니어서 남을 수 있다.

### Column 위치가 의미를 결정한다

```sql
SELECT empno, ename FROM emp
UNION ALL
SELECT deptno, dname FROM dept;
```

```text
첫 번째 Result Column명 → EMPNO, ENAME
두 번째 SELECT의 DEPTNO → 첫 번째 Column 위치로 들어감
두 번째 SELECT의 DNAME  → 두 번째 Column 위치로 들어감
```

Column 이름이 아니라 **개수·순서·호환 가능한 Type**이 맞아야 한다.

### UNION과 UNION ALL 선택

```text
중복까지 업무 Data로 의미 있음 → UNION ALL
완전히 같은 Result Row 제거 필요 → UNION
확신이 없다는 이유로 UNION 사용 → 중복 제거 비용과 Data 손실 가능
```

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 Anchor | 강사님 코드 Anchor |
| --- | --- | --- |
| 중복 포함 결합 | `union all` | `union all` |
| 중복 제거 결합 | `union` | `union` |
| 정렬 | 집합 Query 뒤 `order by` | 같은 구간 |

각 SELECT를 따로 실행해 Row 수를 기록한 뒤 결합 결과의 Row 수와 비교한다.
