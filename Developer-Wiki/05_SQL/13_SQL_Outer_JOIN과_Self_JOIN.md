# 13. SQL Outer JOIN과 Self JOIN

> 일치하지 않는 Row를 보존하고 같은 Table을 서로 다른 역할로 연결하는 방법

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | `LEFT JOIN`, `RIGHT JOIN`, Anti Join, Self Join |
| 기준 DBMS | MariaDB |
| 실습 테이블 | `EMP`, `DEPT` |
| 선수 학습 | ANSI `INNER JOIN`, `ON`, `WHERE`, Subquery, `UNION` |
| 다음 학습 | DDL과 제약조건 |
| 문서 버전 | V3 Encyclopedia |

> 원본 `Script.sql`의 기존 방식 Join과 ANSI JOIN 다음 범위를 기준으로 구성했다. `EMP.MGR`은 같은 `EMP` Table의 `EMPNO`를 논리적으로 참조하므로 사원–관리자 Self Join에 사용한다.

---

## 🎯 학습 목표

- INNER JOIN과 Outer Join의 Row 보존 차이를 설명한다.
- `LEFT JOIN`과 `RIGHT JOIN`에서 보존되는 Table을 판단한다.
- `ON`과 `WHERE`의 조건 위치가 Outer Join 결과에 미치는 영향을 이해한다.
- `IS NULL`을 사용해 일치하지 않는 Row를 찾는 Anti Join을 작성한다.
- 같은 `EMP` Table에 서로 다른 Alias를 부여하여 Self Join한다.
- 최고 관리자처럼 연결 대상이 없는 Row를 보존한다.
- Full Outer Join이 필요한 결과를 MariaDB에서 안전하게 조합한다.

---

## 1. Outer Join이 필요한 이유

### 1. INNER JOIN은 일치하는 Row만 남긴다

```sql
SELECT d.deptno, d.dname, e.empno, e.ename
FROM dept AS d
INNER JOIN emp AS e
    ON e.deptno = d.deptno;
```

사원이 없는 부서는 결과에서 제외된다.

### 2. 기준 Table의 모든 Row가 필요할 수 있다

```sql
SELECT d.deptno, d.dname, e.empno, e.ename
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno;
```

### 3. 일치하지 않는 쪽은 NULL로 채워진다

사원이 없는 부서는 `DEPT` Column은 유지되고 `EMP` Column이 `NULL`로 표시된다.

### 4. Outer Join의 핵심은 Row 보존이다

```text
INNER JOIN
→ 양쪽에 일치하는 Row만

LEFT JOIN
→ 왼쪽 Table의 모든 Row

RIGHT JOIN
→ 오른쪽 Table의 모든 Row
```

### 5. OUTER 키워드는 생략할 수 있다

`LEFT JOIN`과 `LEFT OUTER JOIN`, `RIGHT JOIN`과 `RIGHT OUTER JOIN`은 각각 같은 의미다.

---

## 2. LEFT JOIN

### 6. 왼쪽 Table을 보존한다

```sql
SELECT
    d.deptno,
    d.dname,
    e.empno,
    e.ename
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
ORDER BY d.deptno, e.empno;
```

### 7. 왼쪽과 오른쪽은 작성 위치를 뜻한다

```text
FROM dept AS d
LEFT JOIN emp AS e

왼쪽  → DEPT, 보존
오른쪽 → EMP, 일치하지 않으면 NULL
```

### 8. 부서가 여러 사원을 가지면 여러 Row가 된다

왼쪽 Row를 보존한다는 것이 결과가 부서당 한 Row라는 뜻은 아니다. 일치하는 사원이 여러 명이면 부서 Row가 사원 수만큼 반복된다.

### 9. LEFT JOIN 후 사원이 없는 부서를 찾는다

```sql
SELECT d.deptno, d.dname, d.loc
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
WHERE e.empno IS NULL;
```

### 10. NULL 검사는 오른쪽의 NOT NULL Key가 안전하다

`EMP.EMPNO`처럼 실제 일치 Row에서는 `NULL`일 수 없는 Column을 검사하면 “일치하지 않음”을 명확히 판단할 수 있다.

---

## 3. RIGHT JOIN

### 11. 오른쪽 Table을 보존한다

```sql
SELECT
    e.empno,
    e.ename,
    d.deptno,
    d.dname
FROM emp AS e
RIGHT JOIN dept AS d
    ON d.deptno = e.deptno
ORDER BY d.deptno, e.empno;
```

### 12. LEFT JOIN으로 바꿔 쓸 수 있다

```sql
SELECT
    e.empno,
    e.ename,
    d.deptno,
    d.dname
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
ORDER BY d.deptno, e.empno;
```

Table 순서를 바꾸면 같은 보존 방향을 `LEFT JOIN`으로 표현할 수 있다.

### 13. 실무에서는 LEFT JOIN으로 방향을 통일하기도 한다

항상 보존할 기준 Table을 먼저 작성하면 긴 Query의 흐름을 왼쪽에서 오른쪽으로 읽기 쉽다.

### 14. RIGHT JOIN이 틀린 문법은 아니다

업무 문장을 오른쪽 Table 중심으로 읽는 편이 자연스럽다면 사용할 수 있다. 팀의 일관성과 가독성을 기준으로 선택한다.

### 15. 방향을 바꿀 때 SELECT와 ORDER BY도 확인한다

Table 순서만 바꾸고 Alias 또는 정렬 기준을 잘못 바꾸지 않도록 결과 Column을 함께 검토한다.

---

## 4. ON과 WHERE의 중요한 차이

### 16. 오른쪽 Table 조건을 ON에 두기

```sql
SELECT d.deptno, d.dname, e.empno, e.ename, e.sal
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
   AND e.sal >= 2000
ORDER BY d.deptno, e.empno;
```

모든 부서를 보존하면서 급여 2000 이상인 사원만 연결한다.

### 17. 같은 조건을 WHERE에 두기

```sql
SELECT d.deptno, d.dname, e.empno, e.ename, e.sal
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
WHERE e.sal >= 2000
ORDER BY d.deptno, e.empno;
```

`EMP`가 연결되지 않은 Row의 `e.sal`은 `NULL`이고 조건이 True가 아니므로 제거된다.

### 18. WHERE 조건이 Outer Join의 보존 효과를 없앨 수 있다

오른쪽 Table Column을 `WHERE`에서 필수 조건으로 검사하면 결과가 사실상 INNER JOIN처럼 좁아질 수 있다.

### 19. 요구사항을 먼저 자연어로 구분한다

```text
모든 부서 + 조건에 맞는 사원
→ 오른쪽 조건을 ON

조건에 맞는 사원이 있는 부서만
→ 오른쪽 조건을 WHERE 또는 INNER JOIN 검토
```

### 20. 왼쪽 Table Filtering은 WHERE에 둘 수 있다

```sql
SELECT d.deptno, d.dname, e.empno, e.ename
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
WHERE d.loc IN ('DALLAS', 'CHICAGO');
```

보존 대상 중 필요한 부서만 선택한다.

---

## 5. NULL과 표시값

### 21. NULL은 연결 실패를 나타낼 수 있다

Outer Join에서 생성된 `NULL`은 오른쪽에 일치하는 Row가 없다는 뜻일 수 있다.

### 22. 원본 NULL과 생성된 NULL을 구분한다

오른쪽의 Nullable Column이 `NULL`인 것만으로는 연결 실패인지 실제 저장값이 NULL인지 구분하기 어렵다. Primary Key처럼 실제 Row에서 NULL이 불가능한 Column을 검사한다.

### 23. COALESCE로 화면 표시를 보완한다

```sql
SELECT
    d.deptno,
    d.dname,
    COALESCE(e.ename, '소속 사원 없음') AS employee_name
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
ORDER BY d.deptno, e.empno;
```

### 24. Key 자체를 문자열로 바꾸지 않는다

계산과 관계에 사용하는 Key는 원래 자료형을 유지하고, 사용자 표시용 Column에만 설명 Text를 적용한다.

### 25. NULL을 0으로 바꿀 때 의미를 확인한다

집계 결과가 없는 것과 실제 값이 0인 것은 다를 수 있다. 업무 보고서에서 같은 의미로 취급할 때만 `COALESCE(..., 0)`을 사용한다.

---

## 6. Outer Join과 집계

### 26. 모든 부서의 사원 수

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

### 27. COUNT(*)를 주의한다

```sql
SELECT d.deptno, COUNT(*) AS row_count
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
GROUP BY d.deptno;
```

사원이 없는 부서도 보존된 한 Row가 있으므로 `COUNT(*)`는 1이 될 수 있다.

### 28. 일치한 사원 수는 COUNT(e.empno)

`COUNT(column)`은 `NULL`을 제외하므로 일치한 사원 수를 세는 데 적합하다.

### 29. 급여 합계의 NULL을 표시용 0으로 바꾸기

```sql
SELECT
    d.deptno,
    d.dname,
    COUNT(e.empno) AS employee_count,
    COALESCE(SUM(e.sal), 0) AS salary_sum
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
GROUP BY d.deptno, d.dname
ORDER BY d.deptno;
```

### 30. AVG가 NULL인 부서는 평균 대상이 없다

사원이 없는 부서의 `AVG(e.sal)`은 `NULL`이다. 0으로 표시할지는 보고서 의미에 따라 결정한다.

### 31. HAVING과 보존 결과를 함께 검토한다

```sql
SELECT d.deptno, d.dname, COUNT(e.empno) AS employee_count
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
GROUP BY d.deptno, d.dname
HAVING COUNT(e.empno) = 0;
```

---

## 7. Anti Join

### 32. 일치하지 않는 Row만 찾기

```sql
SELECT d.deptno, d.dname
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
WHERE e.empno IS NULL;
```

### 33. LEFT JOIN + IS NULL 패턴

```text
LEFT JOIN으로 기준 Row 보존
→ 오른쪽 Key가 NULL인 Row 선택
→ 대응 Row가 없는 대상
```

### 34. NOT EXISTS로도 표현할 수 있다

```sql
SELECT d.deptno, d.dname
FROM dept AS d
WHERE NOT EXISTS (
    SELECT 1
    FROM emp AS e
    WHERE e.deptno = d.deptno
);
```

### 35. NOT IN보다 NULL에 안전한 표현을 검토한다

`NOT IN`의 Subquery 결과에 NULL이 있으면 3-valued logic 때문에 예상과 다른 결과가 생길 수 있다. `NOT EXISTS` 또는 Anti Join이 의도를 더 직접 표현할 수 있다.

### 36. 오른쪽 Nullable 일반 Column을 검사하지 않는다

```sql
-- COMM은 실제 사원 Row에서도 NULL일 수 있으므로 연결 실패 판정에 부적합
-- WHERE e.comm IS NULL
```

### 37. Anti Join의 한 Row 의미를 확인한다

“사원이 없는 부서”, “주문이 없는 고객”, “등록되지 않은 코드”처럼 기준 대상 중 대응 Data가 없는 경우에 사용한다.

---

## 8. FULL OUTER JOIN 결과

### 38. 양쪽의 모든 Row가 필요한 경우

Full Outer Join은 양쪽의 일치 Row와 왼쪽에만 있는 Row, 오른쪽에만 있는 Row를 모두 반환한다.

### 39. MariaDB JOIN 문법에는 직접적인 FULL OUTER JOIN이 없다

MariaDB의 지원 JOIN 구문은 `LEFT`와 `RIGHT` Outer Join을 제공한다. `FULL OUTER JOIN`을 그대로 작성하는 방식에 의존하지 않는다.

### 40. LEFT JOIN과 반대쪽 미일치 Row를 UNION ALL한다

```sql
SELECT
    d.deptno AS dept_deptno,
    d.dname,
    e.empno,
    e.ename,
    e.deptno AS emp_deptno
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno

UNION ALL

SELECT
    d.deptno,
    d.dname,
    e.empno,
    e.ename,
    e.deptno
FROM emp AS e
LEFT JOIN dept AS d
    ON d.deptno = e.deptno
WHERE d.deptno IS NULL;
```

### 41. 두 번째 분기에서 미일치 Row만 선택한다

첫 번째 `LEFT JOIN`에 이미 일치 Row가 포함되어 있으므로 두 번째 분기는 `WHERE d.deptno IS NULL`로 사원 쪽에만 있는 Row를 추가한다.

### 42. UNION만으로 중복을 숨기지 않는다

`UNION ALL`과 명시적인 Anti Join 조건으로 각 분기의 역할을 드러내는 편이 안전하다.

### 43. 실습 Schema에서는 FK 때문에 반대쪽 미일치가 없을 수 있다

`EMP.DEPTNO → DEPT.DEPTNO` Foreign Key가 유효하면 존재하지 않는 부서 번호를 가진 사원은 저장되지 않는다. 문법과 실제 결과를 구분한다.

---

## 9. Self Join 기본

### 44. 같은 Table을 두 번 사용하는 Join

```sql
SELECT
    employee.empno,
    employee.ename AS employee_name,
    manager.empno AS manager_empno,
    manager.ename AS manager_name
FROM emp AS employee
JOIN emp AS manager
    ON manager.empno = employee.mgr;
```

### 45. Table은 같지만 역할이 다르다

```text
employee
→ 관리자를 찾을 사원 Row

manager
→ EMPNO가 사원의 MGR와 일치하는 관리자 Row
```

### 46. Self Join은 별도의 JOIN 종류가 아니다

같은 Table을 서로 다른 Alias로 두 번 참조하는 작성 Pattern이다. `INNER JOIN`, `LEFT JOIN` 등 필요한 Join 방식과 함께 사용한다.

### 47. Alias가 필수에 가깝다

같은 Column명이 양쪽에 모두 있으므로 역할별 Alias 없이는 관계를 읽기 어렵고 Column이 모호해진다.

### 48. 연결 방향을 정확히 읽는다

```sql
ON manager.empno = employee.mgr
```

사원 Row의 `MGR` 값이 관리자 Row의 `EMPNO`를 가리킨다.

---

## 10. 사원–관리자 Self Join

### 49. INNER Self Join의 누락

최고 관리자는 `MGR`가 `NULL`이므로 일치하는 관리자 Row가 없고 INNER JOIN 결과에서 제외된다.

### 50. 모든 사원을 보존하려면 LEFT Self Join

```sql
SELECT
    employee.empno,
    employee.ename AS employee_name,
    employee.job,
    employee.mgr,
    manager.ename AS manager_name
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
ORDER BY employee.empno;
```

### 51. 관리자 없는 사원 표시

```sql
SELECT
    employee.ename AS employee_name,
    COALESCE(manager.ename, '관리자 없음') AS manager_name
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
ORDER BY employee.empno;
```

### 52. 최고 관리자 찾기

```sql
SELECT employee.empno, employee.ename
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
WHERE manager.empno IS NULL;
```

### 53. MGR 자체가 NULL인지 찾는 방식도 가능하다

```sql
SELECT empno, ename
FROM emp
WHERE mgr IS NULL;
```

이 Query는 “관리자 번호가 미입력”인 사원을 찾는다. Self Join Anti Join은 “입력된 MGR를 포함해 실제 관리자 Row가 연결되지 않음”까지 탐지할 수 있다.

### 54. Data 무결성에 따라 결과 의미가 달라진다

`EMP.MGR`에 실제 Foreign Key 제약이 없다면 존재하지 않는 `EMPNO`가 입력될 가능성도 고려해야 한다.

---

## 11. 여러 단계의 Self Join

### 55. 사원–관리자–상위 관리자

```sql
SELECT
    employee.ename AS employee_name,
    manager.ename AS manager_name,
    senior_manager.ename AS senior_manager_name
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
LEFT JOIN emp AS senior_manager
    ON senior_manager.empno = manager.mgr
ORDER BY employee.empno;
```

### 56. 단계마다 새로운 Alias를 사용한다

같은 `EMP` Table이어도 `employee`, `manager`, `senior_manager`는 서로 다른 역할과 현재 Row를 가진다.

### 57. 고정 단계 Self Join의 한계

조직 깊이가 바뀌거나 몇 단계인지 알 수 없다면 JOIN을 계속 추가하는 방식은 확장성이 낮다.

### 58. 가변 깊이는 Recursive CTE를 검토한다

전체 관리 계층을 임의 깊이로 탐색하는 방법은 이후 Recursive CTE 단원에서 다룬다.

### 59. 순환 관계를 점검한다

잘못된 Data로 사원이 자신을 관리자라고 가리키거나 관리자 관계가 순환하면 계층 해석에 문제가 생긴다.

---

## 12. Outer Join과 다중 Table

### 60. 사원을 보존하며 부서와 관리자 연결

```sql
SELECT
    employee.empno,
    employee.ename AS employee_name,
    d.dname,
    manager.ename AS manager_name
FROM emp AS employee
LEFT JOIN dept AS d
    ON d.deptno = employee.deptno
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
ORDER BY employee.empno;
```

### 61. 기준 Table은 EMP다

모든 사원을 보존하려는 보고서이므로 `EMP AS employee`를 왼쪽 기준으로 둔다.

### 62. 각 LEFT JOIN은 자신의 연결 조건을 가진다

```text
employee ↔ d
→ DEPTNO

employee ↔ manager
→ MGR = EMPNO
```

### 63. 중간 오른쪽 Table에 의존하는 Join을 주의한다

관리자 다음의 상위 관리자를 연결하면 앞 단계 관리자 Row가 `NULL`일 때 다음 단계도 연결되지 않는다.

### 64. WHERE로 오른쪽 Table을 필터링하면 보존 범위가 달라진다

다중 Outer Join일수록 각 조건이 `ON`인지 `WHERE`인지 한 단계씩 확인한다.

---

## 13. 내 코드와 강사님 코드 비교

### 65. INNER Self Join 형태

```sql
-- 관리자 Row가 있는 사원만 조회되는 형태
SELECT e.ename AS employee_name, m.ename AS manager_name
FROM emp AS e
JOIN emp AS m
    ON m.empno = e.mgr;
```

### 66. LEFT Self Join으로 개선

```sql
-- 최고 관리자를 포함한 모든 사원 보존
SELECT
    e.ename AS employee_name,
    COALESCE(m.ename, '관리자 없음') AS manager_name
FROM emp AS e
LEFT JOIN emp AS m
    ON m.empno = e.mgr;
```

### 67. 오른쪽 조건을 WHERE에 둔 형태

```sql
-- 급여 2000 이상 사원이 없는 부서는 제거될 수 있다.
SELECT d.dname, e.ename, e.sal
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
WHERE e.sal >= 2000;
```

### 68. 보존 의도를 유지하도록 ON으로 이동

```sql
SELECT d.dname, e.ename, e.sal
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
   AND e.sal >= 2000;
```

### 69. 비교 결론

- 모든 기준 Row가 필요하면 보존할 Table을 왼쪽에 둔다.
- 오른쪽 Row의 연결 조건은 `ON`, 최종 결과 제외 조건은 `WHERE`로 구분한다.
- Self Join은 역할을 드러내는 Alias가 핵심이다.
- 관리자 없는 사원까지 필요하면 LEFT Self Join을 사용한다.
- NULL 표시와 관계 존재 판단을 혼동하지 않는다.

---

## 14. 개선된 통합 예제

### 70. 전체 부서 인원 현황

```sql
SELECT
    d.deptno,
    d.dname,
    d.loc,
    COUNT(e.empno) AS employee_count,
    COALESCE(SUM(e.sal), 0) AS salary_sum,
    ROUND(AVG(e.sal), 2) AS avg_salary
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
GROUP BY d.deptno, d.dname, d.loc
ORDER BY d.deptno;
```

### 71. 사원·부서·관리자 통합 보고서

```sql
SELECT
    employee.empno,
    employee.ename AS employee_name,
    employee.job,
    employee.sal,
    COALESCE(d.dname, '부서 없음') AS department_name,
    manager.empno AS manager_empno,
    COALESCE(manager.ename, '관리자 없음') AS manager_name
FROM emp AS employee
LEFT JOIN dept AS d
    ON d.deptno = employee.deptno
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
ORDER BY d.deptno, employee.empno;
```

### 72. 부서별 고액 급여자 포함 현황

```sql
SELECT
    d.deptno,
    d.dname,
    COUNT(e.empno) AS high_salary_count
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
   AND e.sal >= 3000
GROUP BY d.deptno, d.dname
ORDER BY d.deptno;
```

급여 3000 이상 사원이 없어도 부서는 결과에 남는다.

---

## 15. 실무 활용 지침

### 73. 보존할 기준 집합을 먼저 정한다

```text
모든 부서가 필요한가?
모든 사원이 필요한가?
일치하는 대상만 필요한가?
```

### 74. 한 Row의 의미를 정의한다

부서별 한 Row인지, 사원별 한 Row인지, 사원–관리자 관계별 한 Row인지에 따라 Join과 집계가 달라진다.

### 75. ON 조건과 WHERE 조건을 문장으로 읽는다

`ON`은 어떤 오른쪽 Row를 연결할지, `WHERE`는 최종 결과에서 어떤 Row를 남길지 결정한다.

### 76. Self Join Alias는 역할 이름을 사용한다

`e1`, `e2`도 가능하지만 계층 관계에서는 `employee`, `manager`가 유지보수에 유리하다.

### 77. 계층 무결성을 별도로 검증한다

자기 참조, 존재하지 않는 관리자, 순환 관계, 비정상적인 깊이를 점검한다.

### 78. 성능은 EXPLAIN과 실제 Data로 판단한다

Join Key의 Index와 Data 분포가 중요하다. Outer Join이라는 이유만으로 성능을 단정하지 않는다.

---

## 16. 자주 하는 실수

### 79. 보존할 Table을 반대로 둔다

`LEFT JOIN`의 왼쪽이 어떤 Table인지 FROM절을 그대로 읽는다.

### 80. 오른쪽 조건을 WHERE에 두어 Row를 제거한다

“모든 왼쪽 Row”가 요구사항이면 오른쪽 조건의 위치를 먼저 점검한다.

### 81. COUNT(*)로 일치 Row 수를 센다

Outer Join의 보존 Row까지 세므로 오른쪽의 NOT NULL Key를 `COUNT`한다.

### 82. Nullable Column으로 미일치를 판정한다

원본 Data에서도 NULL일 수 있는 Column 대신 Primary Key 또는 NOT NULL Key를 검사한다.

### 83. Self Join 방향을 반대로 연결한다

```sql
-- 올바른 사원 → 관리자 관계
ON manager.empno = employee.mgr
```

### 84. INNER Self Join으로 최고 관리자를 누락한다

모든 사원 보고서라면 `LEFT JOIN`이 필요한지 확인한다.

### 85. FULL OUTER JOIN을 그대로 작성한다

MariaDB의 실제 지원 구문을 확인하고 `LEFT JOIN + 반대쪽 Anti Join + UNION ALL` 패턴을 사용한다.

### 86. COALESCE가 Data를 바꾼다고 생각한다

`COALESCE`는 Query 결과의 표시값을 반환할 뿐 원본 Table을 수정하지 않는다.

---

## 17. 디버깅 방법

### 87. INNER JOIN 결과와 비교한다

```sql
SELECT COUNT(*) AS inner_count
FROM dept AS d
JOIN emp AS e ON e.deptno = d.deptno;

SELECT COUNT(*) AS left_count
FROM dept AS d
LEFT JOIN emp AS e ON e.deptno = d.deptno;
```

### 88. 양쪽 Key를 함께 표시한다

```sql
SELECT
    d.deptno AS left_deptno,
    e.deptno AS right_deptno,
    e.empno
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
ORDER BY d.deptno, e.empno;
```

### 89. WHERE를 제거해 보존 Row를 확인한다

Outer Join 결과가 예상보다 적으면 오른쪽 Table을 참조하는 `WHERE` 조건을 잠시 제거하고 비교한다.

### 90. ON 조건별 Boolean을 검증한다

필터를 별도 Query에서 먼저 실행해 어떤 Row가 연결 대상인지 확인한다.

### 91. 관리자 Key를 직접 비교한다

```sql
SELECT
    employee.empno,
    employee.ename,
    employee.mgr,
    manager.empno AS matched_manager_empno,
    manager.ename AS matched_manager_name
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
ORDER BY employee.empno;
```

### 92. 연결되지 않는 관리자 번호를 찾는다

```sql
SELECT employee.empno, employee.ename, employee.mgr
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
WHERE employee.mgr IS NOT NULL
  AND manager.empno IS NULL;
```

### 93. 집계 전 상세 Row를 확인한다

`GROUP BY`를 제거하고 원본 결합 결과를 확인한 후 `COUNT`, `SUM`을 적용한다.

### 94. EXPLAIN으로 실행 계획을 확인한다

```sql
EXPLAIN
SELECT employee.ename, manager.ename AS manager_name
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr;
```

---

## 18. 종합실습

### 95. 문제 1 — 모든 부서와 사원

사원이 없는 부서까지 포함하여 부서 번호, 부서명, 사원 번호, 사원명을 조회한다.

### 96. 문제 2 — 사원이 없는 부서

`LEFT JOIN + IS NULL` 방식으로 소속 사원이 없는 부서를 조회한다.

### 97. 문제 3 — 전체 부서별 인원수

사원이 없는 부서도 0명으로 표시하여 부서별 인원수를 조회한다.

### 98. 문제 4 — 사원과 관리자

모든 사원의 이름과 관리자 이름을 조회한다. 관리자가 없으면 `관리자 없음`으로 표시한다.

### 99. 문제 5 — 사원·부서·관리자 통합

모든 사원의 번호, 이름, 부서명, 관리자 이름을 조회하고 사원 번호순으로 정렬한다.

---

## 19. 정답과 해설

### 100. 문제 1 정답

```sql
SELECT d.deptno, d.dname, e.empno, e.ename
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
ORDER BY d.deptno, e.empno;
```

보존 대상인 `DEPT`를 왼쪽에 둔다.

### 101. 문제 2 정답

```sql
SELECT d.deptno, d.dname, d.loc
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
WHERE e.empno IS NULL
ORDER BY d.deptno;
```

실제 사원 Row에서는 NULL이 될 수 없는 `EMPNO`로 미일치를 판정한다.

### 102. 문제 3 정답

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

`COUNT(*)`가 아니라 `COUNT(e.empno)`를 사용해야 사원이 없는 부서가 0명으로 계산된다.

### 103. 문제 4 정답

```sql
SELECT
    employee.ename AS employee_name,
    COALESCE(manager.ename, '관리자 없음') AS manager_name
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
ORDER BY employee.empno;
```

같은 `EMP` Table을 사원과 관리자 역할로 나누고 모든 사원을 보존한다.

### 104. 문제 5 정답

```sql
SELECT
    employee.empno,
    employee.ename AS employee_name,
    COALESCE(d.dname, '부서 없음') AS department_name,
    COALESCE(manager.ename, '관리자 없음') AS manager_name
FROM emp AS employee
LEFT JOIN dept AS d
    ON d.deptno = employee.deptno
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr
ORDER BY employee.empno;
```

기준은 사원이므로 두 관계 모두 `EMP AS employee`에서 시작하는 LEFT JOIN으로 연결한다.

---

## 20. 최종 체크리스트

### 105. 문법 체크

- [ ] 보존할 Table을 `LEFT JOIN`의 왼쪽에 두었는가?
- [ ] Self Join에 역할별 Alias를 지정했는가?
- [ ] 사원–관리자 조건이 `manager.empno = employee.mgr`인가?
- [ ] 직접 지원되지 않는 `FULL OUTER JOIN` 문법에 의존하지 않았는가?

### 106. 논리 체크

- [ ] 오른쪽 조건을 `ON`과 `WHERE` 중 의도에 맞는 위치에 두었는가?
- [ ] 미일치 판정에 NOT NULL Key를 사용했는가?
- [ ] 모든 사원 또는 모든 부서가 실제로 보존되는가?
- [ ] 최고 관리자와 사원이 없는 부서의 NULL 결과를 검토했는가?

### 107. 집계·품질 체크

- [ ] 일치 Row 수에 `COUNT(right_table.key)`를 사용했는가?
- [ ] `COALESCE`로 바꾼 표시값의 업무 의미가 올바른가?
- [ ] 일대다 결합으로 Row가 늘어나는 것을 고려했는가?
- [ ] 가변 깊이 계층은 Recursive CTE가 더 적합하지 않은가?

---

## 21. 핵심 요약

### 108. Outer Join과 Self Join 핵심 문장

```text
LEFT JOIN
→ 왼쪽 모든 Row 보존, 미일치 오른쪽 Column은 NULL

RIGHT JOIN
→ 오른쪽 모든 Row 보존

ON의 오른쪽 조건
→ 왼쪽 Row를 보존하며 연결 대상 제한

WHERE의 오른쪽 조건
→ NULL 보존 Row를 제거할 수 있음

Self Join
→ 같은 Table을 역할별 Alias로 여러 번 참조

사원–관리자
→ manager.empno = employee.mgr
```

### 109. 최종 정리

Outer Join은 단순히 NULL을 만드는 문법이 아니라 **어느 집합을 반드시 보존할지 결정하는 연산**이다. 기준 Table과 조건 위치를 먼저 정하고, 집계에서는 보존 Row와 실제 일치 Row를 구분한다. Self Join에서는 같은 Table보다 각 Alias의 역할이 중요하며, 사원–관리자처럼 연결 대상이 없는 최상위 Row까지 필요하면 LEFT Self Join을 사용한다.

---

## 📎 다음 문서

다음 원본 흐름은 Table 구조를 정의하고 무결성을 설정하는 DDL과 제약조건이다.

```text
14_SQL_DDL과_제약조건.md
```

---

## 🔬 V3 동작 백과 — 일치하지 않는 Row와 같은 Table의 관계

### LEFT JOIN에서 NULL이 만들어지는 과정

```sql
SELECT d.deptno, d.dname, e.ename
FROM dept AS d
LEFT JOIN emp AS e
  ON e.deptno = d.deptno;
```

```text
DEPT Row를 기준으로 모두 유지
→ 같은 DEPTNO의 EMP 검색
→ 있으면 결합 Row 생성
→ 없으면 EMP 쪽 Column을 NULL로 채움
```

```text
DEPTNO | DNAME      | ENAME
10     | ACCOUNTING | CLARK
40     | OPERATIONS | NULL
```

여기서 `NULL`은 EMP Table에 NULL 사원명이 저장됐다는 뜻이 아니라 **JOIN 상대 Row가 없어서 Result에 만들어진 NULL**이다.

### ON과 WHERE가 결과를 바꾸는 이유

```sql
-- 기준 부서는 유지하고 조건에 맞는 사원만 연결
LEFT JOIN emp AS e
  ON e.deptno = d.deptno
 AND e.sal >= 3000
```

```sql
-- JOIN 후 sal 조건이 True인 Row만 유지
LEFT JOIN emp AS e
  ON e.deptno = d.deptno
WHERE e.sal >= 3000
```

두 번째 Query는 상대가 없는 Row의 `e.sal`이 NULL이므로 WHERE에서 제외되어 Outer JOIN 의미가 약해진다.

### Self Join

```sql
SELECT e.ename AS employee, m.ename AS manager
FROM emp AS e
LEFT JOIN emp AS m
  ON m.empno = e.mgr;
```

같은 EMP Table을 `e`와 `m`이라는 두 역할로 읽는다.

```text
사원 Row의 MGR
→ 관리자 역할 m의 EMPNO와 비교
→ 관리자 이름 연결
```

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 Anchor | 강사님 코드 Anchor |
| --- | --- | --- |
| LEFT JOIN | `left join` | `left join` |
| RIGHT JOIN | `right join` | `right join` |
| Self Join | `mgr`와 `empno`를 연결하는 Query | 같은 실습 |
| Outer 조건 위치 | ON·WHERE 비교 Query | Outer Join 구간 |

기준 Table이 무엇인지 먼저 말하고, 일치하지 않은 Row가 어느 쪽 NULL로 나타나는지 예상한 뒤 실행한다.
