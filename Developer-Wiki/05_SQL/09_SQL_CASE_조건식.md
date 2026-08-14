# 09. SQL CASE 조건식

> 조건에 따라 서로 다른 값을 반환하는 SQL의 분기 표현식

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | `CASE` 조건식 |
| 기준 DBMS | MariaDB |
| 실습 테이블 | `EMP`, `DEPT` |
| 선수 학습 | `SELECT`, `WHERE`, 집계함수, 문자열·숫자·날짜·NULL 함수 |
| 다음 학습 | `UNION`, `UNION ALL` |
| 문서 버전 | V2 |

> 이 문서의 `CASE`는 값을 반환하는 **표현식(Expression)** 이다. Stored Program에서 흐름을 제어하는 `CASE` 문과 구분한다.

---

## 🎯 학습 목표

- Simple CASE와 Searched CASE의 문법과 용도를 구분한다.
- `WHEN`의 평가 순서와 `ELSE` 생략 시 결과를 설명할 수 있다.
- `SELECT`, `ORDER BY`, `GROUP BY`, 집계함수 안에서 `CASE`를 활용한다.
- `NULL`, 자료형, 경계값 때문에 생기는 오류를 예방한다.
- 반복되는 조건을 정리하여 읽기 쉬운 Query를 작성한다.

---

## 1. CASE가 필요한 이유

### 1. 같은 Column 값을 사람이 읽기 쉬운 값으로 바꾸기

`EMP.DEPTNO`의 숫자 코드를 부서명처럼 표시할 수 있다.

```sql
SELECT
    ename,
    deptno,
    CASE deptno
        WHEN 10 THEN 'ACCOUNTING'
        WHEN 20 THEN 'RESEARCH'
        WHEN 30 THEN 'SALES'
        ELSE 'ETC'
    END AS dept_name
FROM emp;
```

### 2. 조건에 따라 결과를 분류하기

```sql
SELECT
    ename,
    sal,
    CASE
        WHEN sal >= 3000 THEN 'HIGH'
        WHEN sal >= 2000 THEN 'MIDDLE'
        ELSE 'LOW'
    END AS salary_level
FROM emp;
```

### 3. CASE는 값을 반환하는 표현식이다

`CASE`는 Row를 선택하는 Clause가 아니다. 각 Row에 대해 조건을 평가하고 하나의 값을 만든다.

```sql
SELECT CASE WHEN 10 > 5 THEN 'TRUE' ELSE 'FALSE' END AS result;
```

### 4. CASE의 기본 구성

```text
CASE
→ WHEN 조건 THEN 결과
→ ELSE 기본 결과
→ END
```

`CASE`를 시작했다면 반드시 `END`로 닫아야 한다.

---

## 2. Simple CASE

### 5. Simple CASE 문법

하나의 Expression을 여러 값과 동등 비교할 때 사용한다.

```sql
CASE expression
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ELSE default_result
END
```

### 6. 부서 번호를 부서명으로 변환하기

```sql
SELECT
    empno,
    ename,
    CASE deptno
        WHEN 10 THEN 'ACCOUNTING'
        WHEN 20 THEN 'RESEARCH'
        WHEN 30 THEN 'SALES'
        WHEN 40 THEN 'OPERATIONS'
        ELSE 'UNKNOWN'
    END AS dept_name
FROM emp;
```

### 7. 직무 코드를 한글 설명으로 변환하기

```sql
SELECT
    ename,
    job,
    CASE job
        WHEN 'CLERK' THEN '사무직'
        WHEN 'SALESMAN' THEN '영업직'
        WHEN 'MANAGER' THEN '관리자'
        WHEN 'ANALYST' THEN '분석가'
        WHEN 'PRESIDENT' THEN '대표'
        ELSE '기타'
    END AS job_name
FROM emp;
```

### 8. Simple CASE가 적합한 조건

다음처럼 같은 Expression에 대한 `=` 비교가 반복될 때 읽기 쉽다.

```sql
CASE deptno
    WHEN 10 THEN 'A'
    WHEN 20 THEN 'B'
    ELSE 'C'
END
```

### 9. Simple CASE의 한계

범위, 부등호, 여러 Column을 조합한 조건에는 적합하지 않다.

```sql
-- 잘못된 형태: WHEN 뒤에 범위 조건을 직접 둘 수 없다.
-- CASE sal WHEN sal >= 3000 THEN 'HIGH' END
```

이때는 Searched CASE를 사용한다.

---

## 3. Searched CASE

### 10. Searched CASE 문법

각 `WHEN` 뒤에 독립적인 조건을 작성한다.

```sql
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE default_result
END
```

### 11. 급여 구간 분류하기

```sql
SELECT
    ename,
    sal,
    CASE
        WHEN sal >= 3000 THEN 'HIGH'
        WHEN sal >= 2000 THEN 'MIDDLE'
        ELSE 'LOW'
    END AS salary_level
FROM emp;
```

### 12. 여러 Column을 함께 검사하기

```sql
SELECT
    ename,
    job,
    sal,
    CASE
        WHEN job = 'SALESMAN' AND sal >= 1500 THEN '우수 영업직'
        WHEN job = 'SALESMAN' THEN '영업직'
        WHEN sal >= 3000 THEN '고액 급여자'
        ELSE '일반 사원'
    END AS employee_type
FROM emp;
```

### 13. 날짜 조건 사용하기

```sql
SELECT
    ename,
    hiredate,
    CASE
        WHEN hiredate < '1981-01-01' THEN '1980년 이전 입사'
        WHEN hiredate < '1982-01-01' THEN '1981년 입사'
        ELSE '1982년 이후 입사'
    END AS hire_group
FROM emp;
```

### 14. NULL 검사하기

```sql
SELECT
    ename,
    comm,
    CASE
        WHEN comm IS NULL THEN '보너스 없음'
        WHEN comm = 0 THEN '보너스 0'
        ELSE '보너스 있음'
    END AS comm_status
FROM emp;
```

### 15. Simple CASE와 Searched CASE 선택 기준

| 상황 | 권장 형식 |
|---|---|
| 하나의 값과 여러 값의 동등 비교 | Simple CASE |
| 범위·부등호 비교 | Searched CASE |
| `AND`, `OR`, `IS NULL` 사용 | Searched CASE |
| 여러 Column을 함께 검사 | Searched CASE |

---

## 4. 평가 순서와 ELSE

### 16. 위에서 아래로 평가한다

`CASE`는 처음으로 True가 된 `WHEN`의 결과를 반환하고 종료한다.

```sql
SELECT
    sal,
    CASE
        WHEN sal >= 1000 THEN '1000 이상'
        WHEN sal >= 3000 THEN '3000 이상'
        ELSE '1000 미만'
    END AS wrong_level
FROM emp;
```

급여가 3000 이상이어도 첫 조건이 먼저 True가 되므로 `'1000 이상'`이 반환된다.

### 17. 범위 조건은 좁은 조건부터 배치한다

```sql
SELECT
    sal,
    CASE
        WHEN sal >= 3000 THEN '3000 이상'
        WHEN sal >= 1000 THEN '1000 이상'
        ELSE '1000 미만'
    END AS salary_level
FROM emp;
```

### 18. ELSE를 생략하면 NULL이 반환된다

```sql
SELECT
    ename,
    deptno,
    CASE deptno
        WHEN 10 THEN 'ACCOUNTING'
        WHEN 20 THEN 'RESEARCH'
    END AS dept_name
FROM emp;
```

`DEPTNO`가 10이나 20이 아니면 오류가 아니라 `NULL`이다.

### 19. 의도하지 않은 NULL을 막으려면 ELSE를 작성한다

```sql
SELECT
    CASE deptno
        WHEN 10 THEN 'ACCOUNTING'
        WHEN 20 THEN 'RESEARCH'
        ELSE 'OTHER'
    END AS dept_name
FROM emp;
```

### 20. 모든 조건이 False 또는 Unknown일 수 있다

`NULL`이 포함된 비교는 Unknown이 될 수 있다.

```sql
SELECT
    comm,
    CASE
        WHEN comm > 0 THEN '지급'
        ELSE '미지급 또는 NULL'
    END AS status
FROM emp;
```

`NULL`을 별도로 구분하려면 `WHEN comm IS NULL`을 먼저 작성한다.

---

## 5. CASE와 NULL

### 21. `CASE column WHEN NULL`은 NULL을 찾지 못한다

```sql
-- 잘못된 예
SELECT
    CASE comm
        WHEN NULL THEN 'NULL'
        ELSE 'NOT NULL'
    END AS comm_status
FROM emp;
```

`NULL = NULL`은 True가 아니므로 이 방식으로 NULL을 판별할 수 없다.

### 22. NULL은 `IS NULL`로 검사한다

```sql
SELECT
    CASE
        WHEN comm IS NULL THEN 'NULL'
        ELSE 'NOT NULL'
    END AS comm_status
FROM emp;
```

### 23. NULL과 0은 서로 다르다

```sql
SELECT
    ename,
    comm,
    CASE
        WHEN comm IS NULL THEN '미입력'
        WHEN comm = 0 THEN '0원'
        ELSE CONCAT(comm, ' 지급')
    END AS comm_info
FROM emp;
```

### 24. IFNULL과 CASE의 역할 차이

단순한 NULL 대체는 `IFNULL`이 간결하다.

```sql
SELECT ename, IFNULL(comm, 0) AS comm FROM emp;
```

여러 조건으로 분기하거나 설명 값을 만들 때는 `CASE`가 적합하다.

```sql
SELECT
    ename,
    CASE
        WHEN comm IS NULL THEN '미지급'
        WHEN comm = 0 THEN '지급액 0'
        ELSE '지급'
    END AS comm_status
FROM emp;
```

---

## 6. CASE 결과의 자료형

### 25. THEN과 ELSE는 가능한 한 같은 종류로 맞춘다

```sql
SELECT
    CASE
        WHEN sal >= 3000 THEN 'HIGH'
        ELSE 'LOW'
    END AS salary_level
FROM emp;
```

### 26. 숫자와 문자열을 섞지 않는다

```sql
-- 동작하더라도 암시적 형 변환과 해석 혼란을 만들 수 있다.
SELECT
    CASE
        WHEN sal >= 3000 THEN 1
        ELSE 'LOW'
    END AS mixed_result
FROM emp;
```

다음처럼 숫자 또는 문자열 중 하나로 통일한다.

```sql
SELECT
    CASE
        WHEN sal >= 3000 THEN 1
        ELSE 0
    END AS high_salary_flag
FROM emp;
```

### 27. 날짜 결과도 형식을 통일한다

```sql
SELECT
    ename,
    CASE
        WHEN hiredate IS NULL THEN '미상'
        ELSE DATE_FORMAT(hiredate, '%Y-%m-%d')
    END AS hiredate_text
FROM emp;
```

### 28. 표시용 값과 계산용 값을 분리한다

```sql
SELECT
    ename,
    sal,
    CASE WHEN sal >= 3000 THEN 1 ELSE 0 END AS high_salary_flag,
    CASE WHEN sal >= 3000 THEN '고액' ELSE '일반' END AS salary_label
FROM emp;
```

---

## 7. SELECT 이외의 CASE 활용

### 29. ORDER BY에서 사용자 정의 순서 만들기

```sql
SELECT ename, job, sal
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
    sal DESC;
```

### 30. CASE Alias로 정렬하기

```sql
SELECT
    ename,
    sal,
    CASE
        WHEN sal >= 3000 THEN 1
        WHEN sal >= 2000 THEN 2
        ELSE 3
    END AS salary_rank
FROM emp
ORDER BY salary_rank, sal DESC;
```

### 31. GROUP BY에서 같은 분류식 사용하기

```sql
SELECT
    CASE
        WHEN sal >= 3000 THEN 'HIGH'
        WHEN sal >= 2000 THEN 'MIDDLE'
        ELSE 'LOW'
    END AS salary_level,
    COUNT(*) AS employee_count
FROM emp
GROUP BY
    CASE
        WHEN sal >= 3000 THEN 'HIGH'
        WHEN sal >= 2000 THEN 'MIDDLE'
        ELSE 'LOW'
    END;
```

### 32. CASE를 이용한 조건부 집계

```sql
SELECT
    COUNT(*) AS total_count,
    SUM(CASE WHEN deptno = 10 THEN 1 ELSE 0 END) AS dept10_count,
    SUM(CASE WHEN deptno = 20 THEN 1 ELSE 0 END) AS dept20_count,
    SUM(CASE WHEN deptno = 30 THEN 1 ELSE 0 END) AS dept30_count
FROM emp;
```

### 33. 조건에 맞는 급여만 합계 내기

```sql
SELECT
    SUM(CASE WHEN job = 'SALESMAN' THEN sal ELSE 0 END) AS salesman_salary_sum,
    SUM(CASE WHEN job = 'CLERK' THEN sal ELSE 0 END) AS clerk_salary_sum
FROM emp;
```

### 34. 조건별 평균 계산 시 ELSE 선택에 주의한다

```sql
SELECT
    AVG(CASE WHEN deptno = 30 THEN sal END) AS dept30_avg_sal
FROM emp;
```

`ELSE`를 생략하면 조건에 맞지 않는 Row는 `NULL`이 되고 `AVG`에서 제외된다. `ELSE 0`을 쓰면 전체 Row 수를 기준으로 0까지 평균에 포함되어 의미가 달라진다.

### 35. WHERE와 CASE를 혼동하지 않는다

```sql
-- 30번 부서 Row만 조회
SELECT ename, sal
FROM emp
WHERE deptno = 30;
```

```sql
-- 모든 Row를 유지하면서 30번 부서 여부를 표시
SELECT
    ename,
    CASE WHEN deptno = 30 THEN 'Y' ELSE 'N' END AS is_dept30
FROM emp;
```

---

## 8. 내 코드와 강사님 코드 비교

### 36. 비교 기준

원본 실습의 차이는 정답과 오답으로만 나누지 않는다. 결과가 같다면 문법 선택, 범위의 경계, 가독성 관점에서 비교한다.

### 37. Simple CASE 형태

```sql
-- 내 코드 스타일
SELECT
    ename,
    deptno,
    CASE deptno
        WHEN 10 THEN 'ACCOUNTING'
        WHEN 20 THEN 'RESEARCH'
        WHEN 30 THEN 'SALES'
        ELSE 'ETC'
    END AS dept_name
FROM emp;
```

### 38. 같은 의미의 Searched CASE 형태

```sql
-- 강사님 코드와 함께 비교할 수 있는 형태
SELECT
    ename,
    deptno,
    CASE
        WHEN deptno = 10 THEN 'ACCOUNTING'
        WHEN deptno = 20 THEN 'RESEARCH'
        WHEN deptno = 30 THEN 'SALES'
        ELSE 'ETC'
    END AS dept_name
FROM emp;
```

두 Query의 결과는 같다. 단순 동등 비교만 반복한다면 Simple CASE가 짧고, 조건을 확장할 가능성이 크다면 Searched CASE가 유연하다.

### 39. 급여 등급 조건의 경계 비교

```sql
-- 명시적인 하한·상한 방식
SELECT
    ename,
    sal,
    CASE
        WHEN sal >= 3000 THEN 'A'
        WHEN sal >= 2000 AND sal < 3000 THEN 'B'
        ELSE 'C'
    END AS grade
FROM emp;
```

### 40. 평가 순서를 활용한 개선 방식

```sql
SELECT
    ename,
    sal,
    CASE
        WHEN sal >= 3000 THEN 'A'
        WHEN sal >= 2000 THEN 'B'
        ELSE 'C'
    END AS grade
FROM emp;
```

두 방식은 현재 조건에서 같은 결과를 낸다. 두 번째 방식은 앞 조건에서 3000 이상을 이미 제거했으므로 간결하다. 첫 번째 방식은 각 범위가 독립적으로 보인다는 장점이 있다.

### 41. 비교 결론

- 값의 단순 매핑: Simple CASE가 간결하다.
- 범위와 복합 조건: Searched CASE가 적합하다.
- 겹치는 조건: 우선순위를 먼저 확인한다.
- 경계값: `2000`, `3000`처럼 경계에 있는 Data로 반드시 검증한다.
- 어느 스타일이든 `ELSE`, Alias, 들여쓰기를 명확히 한다.

---

## 9. 개선된 통합 예제

### 42. 사원 정보 보고서 만들기

```sql
SELECT
    empno,
    ename,
    job,
    deptno,
    CASE deptno
        WHEN 10 THEN 'ACCOUNTING'
        WHEN 20 THEN 'RESEARCH'
        WHEN 30 THEN 'SALES'
        WHEN 40 THEN 'OPERATIONS'
        ELSE 'UNKNOWN'
    END AS dept_name,
    sal,
    CASE
        WHEN sal >= 3000 THEN 'HIGH'
        WHEN sal >= 2000 THEN 'MIDDLE'
        ELSE 'LOW'
    END AS salary_level,
    CASE
        WHEN comm IS NULL THEN '미입력'
        WHEN comm = 0 THEN '없음'
        ELSE CONCAT(comm, ' 지급')
    END AS commission_info
FROM emp
ORDER BY
    CASE
        WHEN sal >= 3000 THEN 1
        WHEN sal >= 2000 THEN 2
        ELSE 3
    END,
    sal DESC,
    empno;
```

### 43. 부서별 조건부 집계 보고서 만들기

```sql
SELECT
    deptno,
    COUNT(*) AS employee_count,
    SUM(CASE WHEN sal >= 3000 THEN 1 ELSE 0 END) AS high_salary_count,
    SUM(CASE WHEN comm IS NOT NULL THEN 1 ELSE 0 END) AS commission_count,
    SUM(CASE WHEN job = 'MANAGER' THEN sal ELSE 0 END) AS manager_salary_sum,
    ROUND(AVG(sal), 2) AS avg_salary
FROM emp
GROUP BY deptno
ORDER BY deptno;
```

### 44. JOIN이 가능한 코드 변환은 JOIN을 우선 검토한다

부서 번호를 부서명으로 바꾸는 고정 `CASE`는 학습에는 유용하지만, 실제 기준 정보가 `DEPT`에 있다면 JOIN이 변경에 강하다.

```sql
SELECT
    e.empno,
    e.ename,
    e.deptno,
    COALESCE(d.dname, 'UNKNOWN') AS dept_name
FROM emp AS e
LEFT JOIN dept AS d
    ON e.deptno = d.deptno;
```

`CASE`는 분류 규칙에, 기준 테이블의 값을 가져오는 작업은 JOIN에 사용하는 것이 자연스럽다.

---

## 10. 자주 하는 실수

### 45. END를 빠뜨린다

```sql
-- 오류
-- SELECT CASE WHEN sal >= 3000 THEN 'HIGH' ELSE 'LOW' AS salary_level
-- FROM emp;
```

Alias는 `END` 뒤에 작성한다.

```sql
SELECT
    CASE WHEN sal >= 3000 THEN 'HIGH' ELSE 'LOW' END AS salary_level
FROM emp;
```

### 46. WHEN 순서를 반대로 작성한다

넓은 조건을 먼저 두면 뒤의 좁은 조건이 실행되지 않는다.

```sql
-- sal >= 3000 조건에 도달할 수 없음
CASE
    WHEN sal >= 1000 THEN 'MIDDLE'
    WHEN sal >= 3000 THEN 'HIGH'
    ELSE 'LOW'
END
```

### 47. NULL을 등호로 비교한다

```sql
-- 잘못된 조건
-- WHEN comm = NULL THEN '미입력'

-- 올바른 조건
WHEN comm IS NULL THEN '미입력'
```

### 48. 경계값을 겹치거나 비워 둔다

```sql
CASE
    WHEN sal > 3000 THEN 'HIGH'
    WHEN sal < 2000 THEN 'LOW'
    ELSE 'MIDDLE'
END
```

이 규칙에서 정확히 2000과 3000이 어디에 속하는지 의도와 일치하는지 확인한다.

### 49. CASE로 Row Filtering을 대신한다

필요 없는 Row까지 조회한 뒤 Label만 붙이지 말고, Row 자체를 제외해야 한다면 `WHERE`를 사용한다.

### 50. 너무 긴 CASE를 반복한다

같은 분류식이 여러 곳에서 반복되면 CTE나 Derived Table로 한 번 계산하는 방식을 고려한다.

```sql
WITH classified_emp AS (
    SELECT
        e.*,
        CASE
            WHEN sal >= 3000 THEN 'HIGH'
            WHEN sal >= 2000 THEN 'MIDDLE'
            ELSE 'LOW'
        END AS salary_level
    FROM emp AS e
)
SELECT salary_level, COUNT(*) AS employee_count
FROM classified_emp
GROUP BY salary_level;
```

---

## 11. 디버깅 방법

### 51. 조건을 Boolean 결과로 먼저 확인한다

```sql
SELECT
    ename,
    sal,
    sal >= 3000 AS is_high,
    sal >= 2000 AS is_middle_or_high
FROM emp
ORDER BY sal;
```

### 52. 경계값을 직접 만든다

```sql
SELECT
    test_sal,
    CASE
        WHEN test_sal >= 3000 THEN 'HIGH'
        WHEN test_sal >= 2000 THEN 'MIDDLE'
        ELSE 'LOW'
    END AS salary_level
FROM (
    SELECT 1999 AS test_sal
    UNION ALL SELECT 2000
    UNION ALL SELECT 2999
    UNION ALL SELECT 3000
) AS boundary_test;
```

### 53. ELSE에 임시 진단 값을 넣는다

```sql
SELECT
    ename,
    deptno,
    CASE deptno
        WHEN 10 THEN 'ACCOUNTING'
        WHEN 20 THEN 'RESEARCH'
        WHEN 30 THEN 'SALES'
        ELSE CONCAT('CHECK:', COALESCE(deptno, 'NULL'))
    END AS dept_result
FROM emp;
```

### 54. NULL·0·양수를 나누어 검증한다

```sql
SELECT
    comm,
    CASE
        WHEN comm IS NULL THEN 'NULL'
        WHEN comm = 0 THEN 'ZERO'
        WHEN comm > 0 THEN 'POSITIVE'
        ELSE 'OTHER'
    END AS test_result
FROM emp
ORDER BY comm;
```

### 55. 복잡한 Query는 단계별로 실행한다

1. 원본 Column만 조회한다.
2. `CASE` 결과 Column을 추가한다.
3. 경계값과 NULL을 확인한다.
4. 집계 또는 정렬을 추가한다.
5. 최종 Alias와 표시 형식을 정리한다.

---

## 12. 종합실습

### 56. 문제 1 — 부서명 표시

사원명, 부서 번호, 부서명을 조회한다. 10은 `ACCOUNTING`, 20은 `RESEARCH`, 30은 `SALES`, 나머지는 `OTHER`로 표시한다.

### 57. 문제 2 — 급여 등급 분류

급여가 3000 이상이면 `A`, 2000 이상이면 `B`, 1000 이상이면 `C`, 나머지는 `D`로 표시한다.

### 58. 문제 3 — Commission 상태 구분

`COMM`이 NULL이면 `미입력`, 0이면 `없음`, 양수이면 `지급`으로 표시한다.

### 59. 문제 4 — 직무별 사용자 정의 정렬

`PRESIDENT → MANAGER → ANALYST → SALESMAN → CLERK → 기타` 순서로 조회하고, 같은 직무 안에서는 급여가 높은 사원부터 표시한다.

### 60. 문제 5 — 부서별 조건부 집계

부서별 전체 인원, 급여 2000 이상 인원, Commission을 받은 인원을 조회한다.

---

## 13. 정답과 해설

### 61. 문제 1 정답

```sql
SELECT
    ename,
    deptno,
    CASE deptno
        WHEN 10 THEN 'ACCOUNTING'
        WHEN 20 THEN 'RESEARCH'
        WHEN 30 THEN 'SALES'
        ELSE 'OTHER'
    END AS dept_name
FROM emp;
```

같은 Column의 동등 비교이므로 Simple CASE가 적합하다.

### 62. 문제 2 정답

```sql
SELECT
    ename,
    sal,
    CASE
        WHEN sal >= 3000 THEN 'A'
        WHEN sal >= 2000 THEN 'B'
        WHEN sal >= 1000 THEN 'C'
        ELSE 'D'
    END AS salary_grade
FROM emp;
```

큰 값부터 검사해야 등급이 올바르게 나뉜다.

### 63. 문제 3 정답

```sql
SELECT
    ename,
    comm,
    CASE
        WHEN comm IS NULL THEN '미입력'
        WHEN comm = 0 THEN '없음'
        WHEN comm > 0 THEN '지급'
        ELSE '확인 필요'
    END AS comm_status
FROM emp;
```

NULL과 0은 서로 다른 상태이므로 별도 조건으로 처리한다.

### 64. 문제 4 정답

```sql
SELECT ename, job, sal
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

마지막 `EMPNO`는 급여까지 같은 경우에도 결과 순서를 안정적으로 만든다.

### 65. 문제 5 정답

```sql
SELECT
    deptno,
    COUNT(*) AS total_count,
    SUM(CASE WHEN sal >= 2000 THEN 1 ELSE 0 END) AS salary_2000_count,
    SUM(CASE WHEN comm IS NOT NULL AND comm > 0 THEN 1 ELSE 0 END) AS commission_count
FROM emp
GROUP BY deptno
ORDER BY deptno;
```

`SUM(CASE ... THEN 1 ELSE 0 END)`은 조건을 만족하는 Row 수를 세는 대표적인 조건부 집계 Pattern이다.

---

## 14. 최종 체크리스트

### 66. 문법 체크

- [ ] `CASE`를 `END`로 닫았는가?
- [ ] Alias를 `END` 뒤에 작성했는가?
- [ ] 범위 조건에는 Searched CASE를 사용했는가?
- [ ] NULL 비교에 `IS NULL` 또는 `IS NOT NULL`을 사용했는가?

### 67. 논리 체크

- [ ] 겹치는 조건을 좁거나 우선순위가 높은 조건부터 배치했는가?
- [ ] `ELSE` 생략 시 NULL이 반환되어도 괜찮은가?
- [ ] 경계값이 빠지거나 중복되지 않는가?
- [ ] NULL과 0을 의도대로 구분했는가?

### 68. 품질 체크

- [ ] `THEN`과 `ELSE` 결과의 자료형이 일관적인가?
- [ ] 반복되는 긴 `CASE`를 CTE나 Derived Table로 정리할 필요가 없는가?
- [ ] 기준 테이블의 값은 하드코딩보다 JOIN이 적합하지 않은가?
- [ ] 사용자 정의 정렬에 안정적인 Tie-breaker가 있는가?

---

## 15. 핵심 요약

### 69. CASE 핵심 문장

```text
Simple CASE
→ 하나의 값을 여러 값과 동등 비교

Searched CASE
→ 범위, NULL, 복합 조건 비교

WHEN
→ 위에서 아래로 평가하고 첫 True에서 종료

ELSE 생략
→ 어떤 WHEN도 선택되지 않으면 NULL

조건부 집계
→ SUM(CASE WHEN 조건 THEN 1 ELSE 0 END)
```

### 70. 최종 정리

`CASE`는 SQL 안에서 조건에 따라 값을 만드는 핵심 표현식이다. 문법 자체보다 중요한 것은 **조건의 순서, 경계값, NULL, 결과 자료형**이다. Row를 제외하려면 `WHERE`, 기준 테이블의 값을 가져오려면 `JOIN`, 조건별 값을 만들거나 집계하려면 `CASE`를 선택한다.

---

## 📎 다음 문서

다음 원본 흐름은 집합연산이다.

```text
10_SQL_UNION과_UNION_ALL.md
```
