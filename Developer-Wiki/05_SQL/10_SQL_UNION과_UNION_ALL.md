# 10. SQL UNION과 UNION ALL

> 여러 SELECT 결과를 위아래로 결합하는 SQL 집합연산

---

## 이 문서에서 바로 찾기

- [학습 목표](#sql-10-section-2)
- [개념에서 실제 실행까지 — UNION과 UNION ALL이란? — 행 집합을 위아래로 결합](#sql-10-section-3)
- [4. UNION과 UNION ALL 비교](#sql-10-section-7)
- [9. 내 코드와 강사님 코드 비교](#sql-10-section-12)
- [14. 종합실습](#sql-10-section-17)
- [15. 정답과 해설](#sql-10-section-18)
- [16. 최종 체크리스트](#sql-10-section-19)
- [17. 핵심 요약](#sql-10-section-20)

<details>
<summary>상세 목차 전체 펼치기</summary>

- [📌 문서 정보](#sql-10-section-1)
- [학습 목표](#sql-10-section-2)
- [개념에서 실제 실행까지 — UNION과 UNION ALL이란? — 행 집합을 위아래로 결합](#sql-10-section-3)
- [1. 집합연산이 필요한 이유](#sql-10-section-4)
- [2. UNION ALL](#sql-10-section-5)
- [3. UNION](#sql-10-section-6)
- [4. UNION과 UNION ALL 비교](#sql-10-section-7)
- [5. 결합 조건: Column 개수와 순서](#sql-10-section-8)
- [6. 자료형 맞추기](#sql-10-section-9)
- [7. Column명과 Alias](#sql-10-section-10)
- [8. ORDER BY와 LIMIT](#sql-10-section-11)
- [9. 내 코드와 강사님 코드 비교](#sql-10-section-12)
- [10. 개선된 통합 예제](#sql-10-section-13)
- [11. 실무 활용 지침](#sql-10-section-14)
- [12. 자주 하는 실수](#sql-10-section-15)
- [13. 디버깅 방법](#sql-10-section-16)
- [14. 종합실습](#sql-10-section-17)
- [15. 정답과 해설](#sql-10-section-18)
- [16. 최종 체크리스트](#sql-10-section-19)
- [17. 핵심 요약](#sql-10-section-20)
- [📎 다음 문서](#sql-10-section-21)
- [🔬 V3 동작 백과 — 두 Result Set은 어떻게 합쳐지는가?](#sql-10-section-22)

</details>

---

<a id="sql-10-section-1"></a>

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

<a id="sql-10-section-2"></a>

## 학습 목표

- 열 위치·중복 제거·최종 정렬을 구분한다.
- 실제 입력·중간 상태·결과와 실패 조건을 직접 확인한다.

---

<a id="sql-10-section-3"></a>

## 개념에서 실제 실행까지 — UNION과 UNION ALL이란? — 행 집합을 위아래로 결합

### 무엇이며 왜 배워야 할까?

UNION은 SELECT 결과를 위아래로 결합한다. JOIN처럼 관계에 따라 열을 옆으로 붙이는 기능과 다르다. 대응 열은 이름이 아니라 위치로 연결되므로 열 개수와 의미·자료형 호환을 확인해야 한다. 같은 자리의 ‘부서번호’와 ‘급여’를 합치면 문법상 가능해도 해석이 틀릴 수 있다.

UNION은 결과 행 전체의 중복을 제거하고 UNION ALL은 반복되는 결과를 유지한다. 급여만 선택하면 서로 다른 사원이라도 같은 급여 결과가 중복 제거될 수 있다. 사원번호까지 선택하면 다른 행으로 구분된다. 업무상 중복의 정의와 선택 열을 함께 판단한다.

결합했다고 첫 SELECT의 순서가 최종 출력 순서로 보장되지 않는다. 전체 결과에 ORDER BY를 적용한다. 중복 제거 비용 때문에 UNION ALL이 적합한 경우가 많지만 중복을 제거해야 하는 질문에 무조건 ALL을 적용하면 요구사항이 바뀐다.

### 입력은 어디에서 오는가?

EMP·DEPT·SALGRADE는 초기화 자료 그대로 준비된 상태다. EMP 14행, DEPT 4행, SALGRADE 5행이다. 다른 DML로 데이터를 바꿨다면 아래 결과와 달라질 수 있다. 상수 SELECT 예제는 테이블 없이도 실행할 수 있다.

### 실행 가능한 보충 SQL과 결과

아래는 원본의 개념을 작은 검증 범위로 정리한 보충 예제다. MariaDB 12.3.2, 일반 SQL 모드·InnoDB 기준에서 결과를 확인했다. 조회 SQL은 SQL 편집기의 Result Grid, 변경 SQL은 영향 행 표시와 사후 SELECT로 관찰한다. DBMS·모드·데이터 상태가 다르면 차이를 확인해야 한다.

```sql
SELECT 10 AS deptno
UNION
SELECT 10;
SELECT 10 AS deptno
UNION ALL
SELECT 10;
```

Result Grid의 열·행 값:

```text
deptno
10
deptno
10
10
```

여러 SELECT가 있으면 위 출력에 결과 헤더가 다시 나타난다. 숫자의 표시 자릿수와 NULL 표시 모양은 클라이언트별로 달라질 수 있지만 값과 행의 의미를 먼저 비교한다.

### 논리적 처리와 상태 변화 — 단계별로 따라가기

1. 첫 가지에서 부서 10의 값을 만들고 같은 값을 두 번째 가지에도 만든다.
2. UNION은 두 결과에서 동일한 10행을 하나로 정리한다.
3. UNION ALL은 두 가지의 10행을 모두 남긴다.
4. 예제는 입력 크기를 작게 줄인 보충 코드이며 원본 emp 전체 행 결합과 구분한다.

### 내 코드·강사님 코드의 어느 부분에 있었을까?


#### 내 코드: `workspace_sql/Script.sql` 439~448행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
union
select * from emp where deptno = 10;

-- union all은 겹치더라도 나오게 함, union보다 활용도가 높음
select * from emp where deptno = 10
union all
select * from emp where deptno = 10;

select * from emp
where sal > 1250;
```

#### 강사님 코드: `workspace_teacher/workspace_sql/Script.sql` 404~413행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
select * from emp where deptno = 10;

select * from emp where deptno = 10
union all
select * from emp where deptno = 10;

/*
select ename from emp where deptno = 10
union all
select ename, sal from emp where deptno = 10;
```

두 원본은 10부서 사원을 같은 조건으로 두 번 결합한다. 초기화 데이터에서 UNION은 3행, UNION ALL은 6행이다. DISTINCT처럼 결과의 모든 열 조합을 기준으로 판단한다.

### 실무에서 사용하거나 디버깅할 때

표현식 결과와 저장 데이터 변경을 구분한다. 결과가 다르면 원본의 앞선 실행 상태, 입력 행 수, NULL·중복·경계값, 조인 후 행 수를 확인한다. 오류 없이 종료한 변경도 0행 대상일 수 있다. 실제 실행 순서·성능은 아래 본문의 논리 설명만으로 단정하지 말고 실행 계획·사후 조회로 검증한다.

### 이해 확인 실습

1. 사원 둘의 급여가 3000이면 sal만 UNION한 결과에 두 번 남을까?
2. 같은 세 사원을 두 번 UNION ALL하면? UNION이면?

<details>
<summary>정답과 판단 근거 펼치기</summary>

1. 남지 않는다. sal만 선택한 동일 결과 행은 하나로 제거된다. ALL이면 반복을 유지한다.
2. 각 결과 열이 같다는 조건에서 6행과 3행이다. 중복의 기준은 결과 행 전체다.

</details>

### 이 개념을 다시 사용할 수 있는지 확인

- [ ] 개념·필요성·입력 컬럼과 자료형을 내 말로 설명한다.
- [ ] 중간 행·그룹·관계와 최종 결과를 구분한다.
- [ ] 원본 코드의 앞 상태와 보충 예제의 조건을 구분한다.
- [ ] NULL·0행·중복·경계값 또는 변경 실패를 재검토한다.

---

<a id="sql-10-section-4"></a>

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

<a id="sql-10-section-5"></a>

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

<a id="sql-10-section-6"></a>

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

<a id="sql-10-section-7"></a>

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

<a id="sql-10-section-8"></a>

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

<a id="sql-10-section-9"></a>

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

<a id="sql-10-section-10"></a>

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

<a id="sql-10-section-11"></a>

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

<a id="sql-10-section-12"></a>

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

<a id="sql-10-section-13"></a>

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

<a id="sql-10-section-14"></a>

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

<a id="sql-10-section-15"></a>

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

<a id="sql-10-section-16"></a>

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

<a id="index-section-91"></a>

### 64. 복잡한 집합연산은 CTE로 이름을 붙인다

분기마다 업무 의미를 나타내는 이름을 붙이면 조건과 Column Mapping을 검증하기 쉽다.

---

<a id="sql-10-section-17"></a>

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

<a id="sql-10-section-18"></a>

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

<a id="sql-10-section-19"></a>

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

<a id="sql-10-section-20"></a>

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

<a id="sql-10-section-21"></a>

## 📎 다음 문서

다음 원본 흐름은 Subquery이다.

```text
11_SQL_서브쿼리.md
```

---

<a id="sql-10-section-22"></a>

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
