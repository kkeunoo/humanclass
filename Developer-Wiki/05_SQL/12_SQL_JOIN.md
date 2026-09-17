# 12. SQL JOIN

> 관계가 있는 여러 Table의 Row와 Column을 하나의 Result Set으로 결합하는 방법

---

## 이 문서에서 바로 찾기

- [학습 목표](#sql-12-section-2)
- [개념에서 실제 실행까지 — JOIN이란? — 관계에 맞는 행 쌍 만들기](#sql-12-section-3)
- [11. JOIN과 Subquery 비교](#sql-12-section-14)
- [12. 내 코드와 강사님 코드 비교](#sql-12-section-15)
- [17. 종합실습](#sql-12-section-20)
- [18. 정답과 해설](#sql-12-section-21)
- [19. 최종 체크리스트](#sql-12-section-22)
- [20. 핵심 요약](#sql-12-section-23)

<details>
<summary>상세 목차 전체 펼치기</summary>

- [📌 문서 정보](#sql-12-section-1)
- [학습 목표](#sql-12-section-2)
- [개념에서 실제 실행까지 — JOIN이란? — 관계에 맞는 행 쌍 만들기](#sql-12-section-3)
- [1. JOIN이 필요한 이유](#sql-12-section-4)
- [2. Cartesian Product](#sql-12-section-5)
- [3. 기존 쉼표 방식 Join](#sql-12-section-6)
- [4. ANSI INNER JOIN](#sql-12-section-7)
- [5. Table Alias와 Column 한정](#sql-12-section-8)
- [6. ON과 WHERE](#sql-12-section-9)
- [7. USING](#sql-12-section-10)
- [8. Equi Join과 Non-Equi Join](#sql-12-section-11)
- [9. 3개 이상의 Table JOIN](#sql-12-section-12)
- [10. JOIN과 집계](#sql-12-section-13)
- [11. JOIN과 Subquery 비교](#sql-12-section-14)
- [12. 내 코드와 강사님 코드 비교](#sql-12-section-15)
- [13. 개선된 통합 예제](#sql-12-section-16)
- [14. 실무 활용 지침](#sql-12-section-17)
- [15. 자주 하는 실수](#sql-12-section-18)
- [16. 디버깅 방법](#sql-12-section-19)
- [17. 종합실습](#sql-12-section-20)
- [18. 정답과 해설](#sql-12-section-21)
- [19. 최종 체크리스트](#sql-12-section-22)
- [20. 핵심 요약](#sql-12-section-23)
- [📎 다음 문서](#sql-12-section-24)
- [🔬 V3 동작 백과 — 서로 다른 Table의 Row는 어떻게 한 Row가 되는가?](#sql-12-section-25)

</details>

---

<a id="sql-12-section-1"></a>

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | 기존 방식 Join, ANSI `INNER JOIN`, `ON`, `USING`, 다중 Table Join |
| 기준 DBMS | MariaDB |
| 실습 테이블 | `EMP`, `DEPT`, `SALGRADE` |
| 선수 학습 | `SELECT`, `WHERE`, `GROUP BY`, Subquery |
| 다음 학습 | Outer Join과 Self Join |
| 문서 버전 | V3 Encyclopedia |

> 원본 `Script.sql`의 기존 쉼표 방식 Join과 ANSI JOIN 학습 흐름을 함께 보존했다. 실무 작성은 관계 조건과 Filtering 조건을 분리할 수 있는 명시적 `JOIN ... ON` 문법을 기본으로 한다.

---

<a id="sql-12-section-2"></a>

## 학습 목표

- 조인 조건·관계 다중성·별칭·필터를 이해한다.
- 실제 입력·중간 상태·결과와 실패 조건을 직접 확인한다.

---

<a id="sql-12-section-3"></a>

## 개념에서 실제 실행까지 — JOIN이란? — 관계에 맞는 행 쌍 만들기

### 무엇이며 왜 배워야 할까?

JOIN은 여러 테이블의 행을 관계 조건으로 연결하여 필요한 열을 함께 반환한다. EMP의 DEPTNO와 DEPT의 DEPTNO를 연결하면 사원 데이터에 부서 이름을 붙일 수 있다. 테이블을 단순히 둘 적기만 하면 관계를 아는 것이 아니며 조건 없는 조합은 곱집합을 만들 수 있다.

초기화 데이터의 EMP 14행과 DEPT 4행을 무조건 조합하면 56쌍이다. 부서 번호 일치 조건이 관계에 맞는 쌍만 선택한다. 부서의 PK는 같은 부서번호 한 행을 보장하지만 부서 하나에는 여러 사원이 있으므로 전체 14행이 한 행으로 줄지 않는다.

별칭 e,d는 같은 이름 열의 출처를 명확하게 한다. ON은 관계 조건, WHERE는 결과의 필터를 표현하는 데 기본적으로 나눠 쓴다. 여러 JOIN에서는 각 연결 옆에 자기 ON을 두어 어떤 조건이 빠졌는지 찾기 쉽게 한다. DISTINCT로 중복처럼 보이는 결과를 가리기 전에 관계가 일대다인지, 키가 중복되었는지 확인한다.

### 입력은 어디에서 오는가?

EMP·DEPT·SALGRADE는 초기화 자료 그대로 준비된 상태다. EMP 14행, DEPT 4행, SALGRADE 5행이다. 다른 DML로 데이터를 바꿨다면 아래 결과와 달라질 수 있다. 상수 SELECT 예제는 테이블 없이도 실행할 수 있다.

### 실행 가능한 보충 SQL과 결과

아래는 원본의 개념을 작은 검증 범위로 정리한 보충 예제다. MariaDB 12.3.2, 일반 SQL 모드·InnoDB 기준에서 결과를 확인했다. 조회 SQL은 SQL 편집기의 Result Grid, 변경 SQL은 영향 행 표시와 사후 SELECT로 관찰한다. DBMS·모드·데이터 상태가 다르면 차이를 확인해야 한다.

```sql
SELECT e.empno, e.ename, d.dname
FROM emp AS e
JOIN dept AS d ON d.deptno = e.deptno
WHERE e.deptno = 10
ORDER BY e.empno;
```

Result Grid의 열·행 값:

```text
empno	ename	dname
7782	CLARK	ACCOUNTING
7839	KING	ACCOUNTING
7934	MILLER	ACCOUNTING
```

여러 SELECT가 있으면 위 출력에 결과 헤더가 다시 나타난다. 숫자의 표시 자릿수와 NULL 표시 모양은 클라이언트별로 달라질 수 있지만 값과 행의 의미를 먼저 비교한다.

### 논리적 처리와 상태 변화 — 단계별로 따라가기

1. EMP e와 DEPT d를 부서 번호 일치로 연결한다.
2. 10부서에서는 세 사원이 같은 ACCOUNTING 한 부서와 각각 연결된다.
3. WHERE로 10부서 사원만 남긴다.
4. 출처를 붙인 사원 열과 부서명을 선택하고 사원번호로 정렬한다.

### 내 코드·강사님 코드의 어느 부분에 있었을까?


#### 내 코드: `workspace_sql/Script.sql` 526~535행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql

-- 이렇게 2개의 테이블을 이용하게 되면 곱연산(데카르트)되어 출력됨
select * 
from emp, dept;

-- 두 개의 테이블을 이용할 땐 아래와 같이 조건식에서 맞춰야 함
select * 
from emp, dept
where emp.deptno = dept.deptno;
```

<a id="index-section-11"></a>

#### 강사님 코드: `workspace_teacher/workspace_sql/Script.sql` 491~500행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
select * from dept;

select *
from emp, dept;

select *
from emp, dept
where emp.deptno = dept.deptno;

select *
```

내·강사님 원본은 쉼표와 WHERE로 연결한 방식에서 JOIN ON으로 이어진다. 강사님 특이한 한글 별칭도 가능하지만 실무에서는 역할을 드러내는 짧고 일관된 이름이 읽기 쉽다. USING은 같은 이름의 연결 열을 편하게 지정하지만 그 열이 모든 키 조건을 충분히 표현하는지 확인한다.

### 실무에서 사용하거나 디버깅할 때

표현식 결과와 저장 데이터 변경을 구분한다. 결과가 다르면 원본의 앞선 실행 상태, 입력 행 수, NULL·중복·경계값, 조인 후 행 수를 확인한다. 오류 없이 종료한 변경도 0행 대상일 수 있다. 실제 실행 순서·성능은 아래 본문의 논리 설명만으로 단정하지 말고 실행 계획·사후 조회로 검증한다.

### 이해 확인 실습

1. EMP와 DEPT를 조건 없이 연결하면 14행일까 56행일까?
2. 조인 후 사원 한 명이 여러 행이면 DISTINCT를 먼저 추가해야 하는가?

<details>
<summary>정답과 판단 근거 펼치기</summary>

1. 현재 자료에서는 56행이다. 관련 부서만 연결하는 조건이 없다.
2. 아니다. 관계 다중성·중복 키·빠진 조건을 먼저 확인한다. 정상 일대다라면 여러 행이 맞을 수 있다.

</details>

### 이 개념을 다시 사용할 수 있는지 확인

- [ ] 개념·필요성·입력 컬럼과 자료형을 내 말로 설명한다.
- [ ] 중간 행·그룹·관계와 최종 결과를 구분한다.
- [ ] 원본 코드의 앞 상태와 보충 예제의 조건을 구분한다.
- [ ] NULL·0행·중복·경계값 또는 변경 실패를 재검토한다.

---

<a id="sql-12-section-4"></a>

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

<a id="index-section-19"></a>

### 4. JOIN 조건은 Row의 대응 관계를 정의한다

```sql
ON d.deptno = e.deptno
```

같은 번호를 가진 사원 Row와 부서 Row가 결합된다.

### 5. INNER JOIN은 일치하는 Row만 반환한다

`EMP.DEPTNO`와 일치하는 `DEPT.DEPTNO`가 없으면 해당 사원은 INNER JOIN 결과에 포함되지 않는다.

---

<a id="sql-12-section-5"></a>

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

<a id="sql-12-section-6"></a>

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

<a id="sql-12-section-7"></a>

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

<a id="sql-12-section-8"></a>

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

<a id="sql-12-section-9"></a>

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

<a id="index-section-50"></a>

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

<a id="sql-12-section-10"></a>

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

<a id="sql-12-section-11"></a>

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

<a id="sql-12-section-12"></a>

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

<a id="sql-12-section-13"></a>

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

<a id="index-section-72"></a>

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

<a id="sql-12-section-14"></a>

## 11. JOIN과 Subquery 비교

<a id="index-section-77"></a>

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

<a id="sql-12-section-15"></a>

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

<a id="sql-12-section-16"></a>

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

<a id="sql-12-section-17"></a>

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

<a id="index-section-94"></a>

### 66. Foreign Key와 JOIN은 같은 개념이 아니다

Foreign Key는 Data 무결성을 보장하는 Schema 제약이고, JOIN은 Query에서 Row를 결합하는 연산이다. FK가 없어도 Join할 수 있지만 관계의 유효성을 별도로 책임져야 한다.

### 67. Index를 추측으로 강제하지 않는다

Join Key의 Index는 성능에 중요할 수 있지만 `FORCE INDEX`를 먼저 사용하지 말고 `EXPLAIN`과 실제 실행을 확인한다.

### 68. SELECT 목록과 정렬 기준을 명시한다

Application Query는 `SELECT *`와 정렬 없는 결과 순서에 의존하지 않는다.

---

<a id="sql-12-section-18"></a>

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

<a id="sql-12-section-19"></a>

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

<a id="index-section-111"></a>

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

<a id="sql-12-section-20"></a>

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

<a id="sql-12-section-21"></a>

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

<a id="sql-12-section-22"></a>

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

<a id="sql-12-section-23"></a>

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

<a id="sql-12-section-24"></a>

## 📎 다음 문서

다음 원본 흐름은 일치하지 않는 Row를 보존하는 Outer Join과 같은 Table을 역할별로 연결하는 Self Join이다.

```text
13_SQL_Outer_JOIN과_Self_JOIN.md
```

---

<a id="sql-12-section-25"></a>

## 🔬 V3 동작 백과 — 서로 다른 Table의 Row는 어떻게 한 Row가 되는가?

```sql
SELECT e.empno, e.ename, e.deptno, d.dname
FROM emp AS e
JOIN dept AS d
  ON d.deptno = e.deptno;
```

입력 관계:

```text
EMP:  SMITH, DEPTNO=20
DEPT: DEPTNO=20, DNAME=RESEARCH
```

논리 흐름:

```text
EMP Row와 DEPT Row 후보 비교
→ ON d.deptno = e.deptno 평가
→ 20 = 20 True
→ 두 Row의 Column을 한 Result Row로 결합
```

결과:

```text
7369 | SMITH | 20 | RESEARCH
```

### JOIN 조건이 없을 때

EMP 14행, DEPT 4행이라면 Cartesian Product는 최대 다음 Row를 만든다.

```text
14 × 4 = 56행
```

결과가 갑자기 많아지면 JOIN 누락이나 1:N 관계를 먼저 확인한다.

### ON과 WHERE

```text
ON
→ 어떤 Row끼리 관계를 맺는지 정의

WHERE
→ 관계가 만들어진 뒤 어떤 Result Row를 남길지 제한
```

INNER JOIN에서는 일부 조건을 서로 옮겨도 결과가 같을 수 있지만 관계 조건과 검색 조건을 구분하면 읽기 쉽고 Outer JOIN에서 의미가 보존된다.

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 Anchor | 강사님 코드 Anchor |
| --- | --- | --- |
| ANSI INNER JOIN | `from emp e join dept d` | 같은 Query |
| ON | `on(e.deptno = d.deptno)` | `on (e.deptno = d.deptno)` |
| 기존 쉼표 Join | `from emp e, dept d` | Join 초기 구간 |
| Non-Equi | `salgrade`와 급여 범위 | 같은 실습 |
| 다중 Table | JOIN이 두 번 이상인 Query | 다중 Join 구간 |

각 Table을 따로 조회해 PK·FK 값과 Row 수를 확인하고, JOIN 후 Row 수가 왜 그렇게 나왔는지 설명한다.
