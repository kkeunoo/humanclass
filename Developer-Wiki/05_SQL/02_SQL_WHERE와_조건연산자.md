---
title: SQL WHERE와 조건연산자
version: v4.0-detailed-encyclopedia
last_updated: 2026-09-17
status: Completed
---

# SQL WHERE와 조건연산자

## 이 문서에서 바로 찾기

- [학습 목표](#sql-02-section-2)
- [개념에서 실제 실행까지 — WHERE란? — 각 행을 조건으로 통과시키기](#sql-02-section-3)
- [4. 기본 비교연산자](#sql-02-section-7)
- [5. 숫자 비교](#sql-02-section-8)
- [10. 문자열 비교와 대/소문자](#sql-02-section-13)
- [28. `BETWEEN`과 비교연산자 변환](#sql-02-section-31)
- [41. 내 코드와 강사님 코드 비교](#sql-02-section-44)
- [48. Debugging](#sql-02-section-51)
- [49. 종합실습](#sql-02-section-52)
- [50. 정답과 해설](#sql-02-section-53)

<details>
<summary>상세 목차 전체 펼치기</summary>

- [문서 정보](#sql-02-section-1)
- [학습 목표](#sql-02-section-2)
- [개념에서 실제 실행까지 — WHERE란? — 각 행을 조건으로 통과시키기](#sql-02-section-3)
- [1. `WHERE`란?](#sql-02-section-4)
- [2. `WHERE`의 위치](#sql-02-section-5)
- [3. `WHERE`는 Row를 제한한다](#sql-02-section-6)
- [4. 기본 비교연산자](#sql-02-section-7)
- [5. 숫자 비교](#sql-02-section-8)
- [6. `>`와 `<`](#sql-02-section-9)
- [7. `>=`와 `<=`](#sql-02-section-10)
- [8. 문자열 조건](#sql-02-section-11)
- [9. 문자열 Quote를 빠뜨리면?](#sql-02-section-12)
- [10. 문자열 비교와 대/소문자](#sql-02-section-13)
- [11. Collation 확인](#sql-02-section-14)
- [12. `AND`](#sql-02-section-15)
- [13. `AND` 진리표](#sql-02-section-16)
- [14. `OR`](#sql-02-section-17)
- [15. `OR` 진리표](#sql-02-section-18)
- [16. `AND`와 `OR` 혼합](#sql-02-section-19)
- [17. 우선순위 해석](#sql-02-section-20)
- [18. 괄호를 사용한 조건 변경](#sql-02-section-21)
- [19. 괄호를 권장하는 이유](#sql-02-section-22)
- [20. `NOT`](#sql-02-section-23)
- [21. `!=`](#sql-02-section-24)
- [22. `<>`](#sql-02-section-25)
- [23. `NOT`, `!=`, `<>`의 관계](#sql-02-section-26)
- [24. 문제 1: 급여 범위](#sql-02-section-27)
- [25. 범위 조건은 경계값이 중요하다](#sql-02-section-28)
- [26. `BETWEEN`](#sql-02-section-29)
- [27. `BETWEEN A AND B`의 포함 범위](#sql-02-section-30)
- [28. `BETWEEN`과 비교연산자 변환](#sql-02-section-31)
- [29. 문제 1과 `BETWEEN`은 완전히 같은가?](#sql-02-section-32)
- [30. `BETWEEN`의 순서](#sql-02-section-33)
- [31. 문제 2: `OR`와 `AND`](#sql-02-section-34)
- [32. 문제 2의 괄호가 중요한 이유](#sql-02-section-35)
- [33. 같은 Column에 여러 `OR`](#sql-02-section-36)
- [34. `IN`](#sql-02-section-37)
- [35. `IN`과 `OR`](#sql-02-section-38)
- [36. 세 값의 `IN`](#sql-02-section-39)
- [37. `NOT IN`](#sql-02-section-40)
- [38. `NOT IN`과 `NOT`](#sql-02-section-41)
- [39. `NOT IN`과 `NULL` 주의](#sql-02-section-42)
- [40. 조건식 Formatting](#sql-02-section-43)
- [41. 내 코드와 강사님 코드 비교](#sql-02-section-44)
- [42. 개선된 통합 예제](#sql-02-section-45)
- [43. 실무 조건식 작성 기준](#sql-02-section-46)
- [44. `AND`와 `OR` 리팩토링](#sql-02-section-47)
- [45. 범위 조건 리팩토링](#sql-02-section-48)
- [46. 문자열 조건 실무 주의](#sql-02-section-49)
- [47. 자주 하는 실수](#sql-02-section-50)
- [48. Debugging](#sql-02-section-51)
- [49. 종합실습](#sql-02-section-52)
- [50. 정답과 해설](#sql-02-section-53)
- [51. 최종 체크리스트](#sql-02-section-54)
- [52. 핵심 요약](#sql-02-section-55)
- [마무리](#sql-02-section-56)
- [V3 동작 백과 — WHERE는 어떤 Row를 남기는가?](#sql-02-section-57)

</details>

---

<a id="sql-02-section-1"></a>

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `02_SQL_WHERE와_조건연산자.md` |
| 분류 | `05_SQL` |
| 원본 기준 | `workspace_sql/Script.sql`, `workspace_teacher/workspace_sql/Script.sql` |
| DB 기준 자료 | `[DB]학습용_emp 신규-mariadb.sql` |
| DBMS | MariaDB |
| 핵심 범위 | `WHERE`, 비교연산자, `AND`, `OR`, `NOT`, 연산자 우선순위, `BETWEEN`, `IN`, `NOT IN` |
| 학습 범위 | Row Filtering, 숫자·문자 조건, 복합 조건, 범위 조건, 다중 값 조건 |
| 다음 범위 제외 | `LIKE`, `IS NULL`, `ORDER BY`, `LIMIT` |
| 문서 형식 | SQL Developer-Wiki V3 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드의 `Script.sql`에서 `WHERE` 조건식부터 `IN`, `NOT IN`까지를 비교해 정리한다.  
> 원본의 조건식 자체는 대부분 올바르지만, **문자열 대/소문자 비교 설명**, `AND`·`OR` 우선순위 해석, `BETWEEN`의 포함 범위, `NOT`과 `!=`·`<>`의 관계를 더 정확하게 보완한다.

---

<a id="sql-02-section-2"></a>

## 학습 목표

- AND·OR 우선순위와 경계값을 중간 행으로 확인한다.
- 실제 입력·중간 상태·결과와 실패 조건을 직접 확인한다.

---

<a id="sql-02-section-3"></a>

## 개념에서 실제 실행까지 — WHERE란? — 각 행을 조건으로 통과시키기

### 무엇이며 왜 배워야 할까?

WHERE는 입력 행마다 조건을 평가하고 참인 행만 결과 후보로 남기는 절이다. 열 선택과 행 선택은 다른 일이다. 이름만 SELECT해도 WHERE에서는 급여나 부서 조건을 사용할 수 있다.

AND는 두 조건 모두 참이어야 하고 OR는 둘 중 하나면 된다. MariaDB에서 AND가 OR보다 먼저 결합되므로 deptno=30 OR deptno=20 AND job='CLERK'는 30부서 전체 또는 20부서 사무직을 뜻한다. 두 부서의 사무직만 원하면 괄호로 부서 조건을 묶는다. 의도한 자연어를 먼저 써야 어떤 괄호가 필요한지 판단할 수 있다.

BETWEEN은 양끝을 포함한다. 2000 이상 3000 미만과 2000~3000 포함은 다른 질문이다. 또한 NULL인 값과의 일반 비교는 UNKNOWN이며 WHERE는 TRUE만 통과시킨다. 문자열의 대소문자 일치 여부는 collation의 영향을 받으므로 무조건 구분한다고 외우지 않는다.

### 입력은 어디에서 오는가?

EMP·DEPT·SALGRADE는 초기화 자료 그대로 준비된 상태다. EMP 14행, DEPT 4행, SALGRADE 5행이다. 다른 DML로 데이터를 바꿨다면 아래 결과와 달라질 수 있다. 상수 SELECT 예제는 테이블 없이도 실행할 수 있다.

### 실행 가능한 보충 SQL과 결과

아래는 원본의 개념을 작은 검증 범위로 정리한 보충 예제다. MariaDB 12.3.2, 일반 SQL 모드·InnoDB 기준에서 결과를 확인했다. 조회 SQL은 SQL 편집기의 Result Grid, 변경 SQL은 영향 행 표시와 사후 SELECT로 관찰한다. DBMS·모드·데이터 상태가 다르면 차이를 확인해야 한다.

```sql
SELECT empno, ename, deptno, job
FROM emp
WHERE (deptno = 30 OR deptno = 20)
  AND job = 'CLERK'
ORDER BY empno;
```

Result Grid의 열·행 값:

```text
empno	ename	deptno	job
7369	SMITH	20	CLERK
7876	ADAMS	20	CLERK
7900	JAMES	30	CLERK
```

여러 SELECT가 있으면 위 출력에 결과 헤더가 다시 나타난다. 숫자의 표시 자릿수와 NULL 표시 모양은 클라이언트별로 달라질 수 있지만 값과 행의 의미를 먼저 비교한다.

### 논리적 처리와 상태 변화 — 단계별로 따라가기

1. EMP의 각 행에서 부서 번호를 검사한다.
2. 괄호 안의 20 또는 30 조건을 묶는다.
3. 그 결과와 job='CLERK'를 AND로 결합한다.
4. 두 조건이 참인 SMITH·ADAMS·JAMES만 남겨 사원번호로 정렬한다.

### 내 코드·강사님 코드의 어느 부분에 있었을까?


#### 내 코드: `workspace_sql/Script.sql` 84~93행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
-- and가 or보다 우선순위이기 때문에, 필요 시 괄호 활용
-- 아래는 deptno = 20 and job = 'CLERK' 가 먼저 필터링 됨
select * from emp
where deptno = 30 or deptno = 20 and job = 'CLERK';

select * from emp
where (deptno = 30 or deptno = 20) and job = 'CLERK';

select * from emp
where sal = 3000;
```

#### 강사님 코드: `workspace_teacher/workspace_sql/Script.sql` 48~57행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
where deptno = 20 or  job='CLERK';

select * from emp
where deptno = 30 or deptno = 20 and job = 'CLERK';

select * from emp
where (deptno = 30 or deptno = 20) and job = 'CLERK';

select * from emp
where sal = 3000;
```

두 원본의 괄호 전·후 질의는 같은 결과를 다른 방식으로 표현한 것이 아니다. 논리 조건 자체가 바뀐다. 내 코드의 문자 대소문자 메모는 실제 MariaDB collation 조건을 함께 확인해야 한다.

### 실무에서 사용하거나 디버깅할 때

표현식 결과와 저장 데이터 변경을 구분한다. 결과가 다르면 원본의 앞선 실행 상태, 입력 행 수, NULL·중복·경계값, 조인 후 행 수를 확인한다. 오류 없이 종료한 변경도 0행 대상일 수 있다. 실제 실행 순서·성능은 아래 본문의 논리 설명만으로 단정하지 말고 실행 계획·사후 조회로 검증한다.

### 이해 확인 실습

1. 괄호를 빼면 SALES 부서의 SALESMAN도 포함될까?
2. sal>=2000 AND sal<3000을 BETWEEN 2000 AND 3000으로 바꿔도 같은가?

<details>
<summary>정답과 판단 근거 펼치기</summary>

1. 포함된다. 30부서 조건만으로 OR의 첫 가지가 참이다.
2. 아니다. BETWEEN은 3000도 포함한다. 경계값 포함 여부를 요구사항에서 먼저 정한다.

</details>

### 이 개념을 다시 사용할 수 있는지 확인

- [ ] 개념·필요성·입력 컬럼과 자료형을 내 말로 설명한다.
- [ ] 중간 행·그룹·관계와 최종 결과를 구분한다.
- [ ] 원본 코드의 앞 상태와 보충 예제의 조건을 구분한다.
- [ ] NULL·0행·중복·경계값 또는 변경 실패를 재검토한다.

---

<a id="sql-02-section-4"></a>

## 1. `WHERE`란?

`WHERE`는 Table의 모든 Row 중 **조건을 만족하는 Row만 선택**하는 Clause다.

```sql
SELECT *
FROM emp
WHERE deptno = 20;
```

흐름:

```text
EMP 전체 Row
    ↓
DEPTNO = 20 조건 평가
    ↓
조건이 True인 Row만 Result에 포함
```

---

<a id="sql-02-section-5"></a>

## 2. `WHERE`의 위치

기본 구조:

```sql
SELECT
    column_list
FROM table_name
WHERE condition;
```

예:

```sql
SELECT
    empno,
    ename,
    deptno
FROM emp
WHERE deptno = 20;
```

---

<a id="sql-02-section-6"></a>

## 3. `WHERE`는 Row를 제한한다

`SELECT` List와 `WHERE`는 역할이 다르다.

```text
SELECT
→ 어떤 Column을 보여줄지 결정

WHERE
→ 어떤 Row를 보여줄지 결정
```

예:

```sql
SELECT
    ename,
    job
FROM emp
WHERE deptno = 20;
```

```text
Column
→ ENAME, JOB만 출력

Row
→ DEPTNO가 20인 사원만 출력
```

---

<a id="sql-02-section-7"></a>

## 4. 기본 비교연산자

| 연산자 | 의미 |
| --- | --- |
| `=` | 같다 |
| `!=` | 같지 않다 |
| `<>` | 같지 않다 |
| `>` | 크다 |
| `>=` | 크거나 같다 |
| `<` | 작다 |
| `<=` | 작거나 같다 |

---

<a id="sql-02-section-8"></a>

## 5. 숫자 비교

```sql
SELECT *
FROM emp
WHERE sal = 3000;
```

`SAL`이 정확히 `3000`인 Row를 조회한다.

---

<a id="sql-02-section-9"></a>

## 6. `>`와 `<`

```sql
SELECT *
FROM emp
WHERE sal > 2000;
```

```sql
SELECT *
FROM emp
WHERE sal < 3000;
```

숫자 범위를 Filtering할 수 있다.

---

<a id="sql-02-section-10"></a>

## 7. `>=`와 `<=`

```sql
SELECT *
FROM emp
WHERE sal >= 2000;
```

```sql
SELECT *
FROM emp
WHERE sal <= 3000;
```

등호가 포함되므로 경계값도 Result에 포함된다.

---

<a id="sql-02-section-11"></a>

## 8. 문자열 조건

문자열 Literal은 Quote로 감싼다.

```sql
SELECT *
FROM emp
WHERE job = 'CLERK';
```

`CLERK`는 Column 이름이 아니라 문자열 값이므로 Quote가 필요하다.

---

<a id="sql-02-section-12"></a>

## 9. 문자열 Quote를 빠뜨리면?

### 잘못된 의도

```sql
SELECT *
FROM emp
WHERE job = CLERK;
```

Database는 `CLERK`를 문자열이 아니라 Identifier로 해석하려고 할 수 있다.

### 올바른 형태

```sql
SELECT *
FROM emp
WHERE job = 'CLERK';
```

---

<a id="sql-02-section-13"></a>

## 10. 문자열 비교와 대/소문자

내 코드에는 다음 Comment가 있다.

```text
where의 값일 땐 '대/소문자'를 구분 함
```

이 설명은 MariaDB 전체에 일반화하면 부정확하다.

문자열 비교의 대/소문자 구분 여부는 **Collation**에 영향을 받는다.

```text
Case-insensitive Collation
→ 'CLERK'와 'clerk'를 같게 비교할 수 있음

Case-sensitive / Binary Collation
→ 대/소문자를 구분할 수 있음
```

즉 다음 Query의 결과는 Column의 Collation에 따라 달라질 수 있다.

```sql
SELECT *
FROM emp
WHERE job = 'clerk';
```

---

<a id="sql-02-section-14"></a>

## 11. Collation 확인

Column 정의와 Collation을 확인할 수 있다.

```sql
SHOW FULL COLUMNS
FROM emp;
```

Database 기본 Character Set과 Collation도 확인할 수 있다.

```sql
SELECT
    @@character_set_database,
    @@collation_database;
```

> [!IMPORTANT]
> “MariaDB는 문자열 비교 시 무조건 대/소문자를 구분한다” 또는 “무조건 구분하지 않는다”라고 단정하지 않는다.

---

<a id="sql-02-section-15"></a>

## 12. `AND`

모든 조건이 True여야 한다.

```sql
SELECT *
FROM emp
WHERE deptno = 20
  AND job = 'CLERK';
```

조건:

```text
DEPTNO = 20
AND
JOB = 'CLERK'
```

둘 다 만족하는 Row만 Result에 포함된다.

---

<a id="sql-02-section-16"></a>

## 13. `AND` 진리표

| 조건 A | 조건 B | `A AND B` |
|:---:|:---:|:---:|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

<a id="sql-02-section-17"></a>

## 14. `OR`

둘 중 하나 이상이 True면 Result에 포함된다.

```sql
SELECT *
FROM emp
WHERE deptno = 20
   OR job = 'CLERK';
```

---

<a id="sql-02-section-18"></a>

## 15. `OR` 진리표

| 조건 A | 조건 B | `A OR B` |
|:---:|:---:|:---:|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

<a id="sql-02-section-19"></a>

## 16. `AND`와 `OR` 혼합

원본:

```sql
SELECT *
FROM emp
WHERE deptno = 30
   OR deptno = 20
  AND job = 'CLERK';
```

SQL에서 일반적으로 `AND`가 `OR`보다 우선순위가 높다.

따라서 이 조건은 다음처럼 해석된다.

```sql
WHERE deptno = 30
   OR (
        deptno = 20
        AND job = 'CLERK'
   );
```

---

<a id="sql-02-section-20"></a>

## 17. 우선순위 해석

위 Query의 조건:

```text
DEPTNO = 30
OR
(
    DEPTNO = 20
    AND JOB = 'CLERK'
)
```

즉:

- 부서 30 사원은 직무와 관계없이 포함
- 부서 20은 `CLERK`만 포함

---

<a id="sql-02-section-21"></a>

## 18. 괄호를 사용한 조건 변경

원본:

```sql
SELECT *
FROM emp
WHERE (deptno = 30 OR deptno = 20)
  AND job = 'CLERK';
```

이번에는 `OR` 부분을 먼저 그룹으로 묶었다.

```text
(
    DEPTNO = 30
    OR
    DEPTNO = 20
)
AND
JOB = 'CLERK'
```

결과 의미:

```text
부서 20 또는 30
그리고
직무가 CLERK
```

---

<a id="sql-02-section-22"></a>

## 19. 괄호를 권장하는 이유

SQL Engine이 우선순위를 알고 있어도 복잡한 조건은 괄호로 의도를 드러내는 편이 좋다.

### Before

```sql
WHERE a = 1
   OR b = 2
  AND c = 3
```

### After

```sql
WHERE a = 1
   OR (
        b = 2
        AND c = 3
   )
```

Code Review에서 해석 오류를 줄일 수 있다.

---

<a id="sql-02-section-23"></a>

## 20. `NOT`

조건의 결과를 반대로 만든다.

```sql
SELECT *
FROM emp
WHERE NOT (sal = 3000);
```

의미:

```text
SAL = 3000
→ False로 반전

SAL != 3000
→ True
```

---

<a id="sql-02-section-24"></a>

## 21. `!=`

MariaDB에서 “같지 않다” 조건으로 사용할 수 있다.

```sql
SELECT *
FROM emp
WHERE sal != 3000;
```

---

<a id="sql-02-section-25"></a>

## 22. `<>`

SQL 표준 형태의 “같지 않다” 연산자다.

```sql
SELECT *
FROM emp
WHERE sal <> 3000;
```

---

<a id="sql-02-section-26"></a>

## 23. `NOT`, `!=`, `<>`의 관계

원본에서는 다음 세 Query를 연속으로 비교한다.

```sql
SELECT *
FROM emp
WHERE sal != 3000;
```

```sql
SELECT *
FROM emp
WHERE sal <> 3000;
```

```sql
SELECT *
FROM emp
WHERE NOT (sal = 3000);
```

`SAL`이 `NULL`이 아닌 현재 Sample Data에서는 같은 Row 집합을 얻을 수 있다.

하지만 `NULL`이 포함된 비교에서는 SQL의 `UNKNOWN` 개념이 있으므로 단순 Boolean 언어처럼만 생각하면 안 된다.

`NULL` 조건은 03번에서 자세히 다룬다.

---

<a id="sql-02-section-27"></a>

## 24. 문제 1: 급여 범위

원본 문제:

```text
급여가 2,000 이상이고
3,000 미만인 사원
```

정답:

```sql
SELECT *
FROM emp
WHERE sal >= 2000
  AND sal < 3000;
```

범위:

```text
2000
→ 포함

3000
→ 제외
```

수학식으로 표현하면:

```text
2000 <= SAL < 3000
```

---

<a id="sql-02-section-28"></a>

## 25. 범위 조건은 경계값이 중요하다

다음을 비교한다.

```sql
WHERE sal >= 2000
  AND sal < 3000
```

```sql
WHERE sal >= 2000
  AND sal <= 3000
```

첫 번째는 `3000`을 제외하고 두 번째는 포함한다.

---

<a id="sql-02-section-29"></a>

## 26. `BETWEEN`

범위 조건을 간결하게 작성할 수 있다.

```sql
SELECT *
FROM emp
WHERE sal BETWEEN 2000 AND 3000;
```

---

<a id="sql-02-section-30"></a>

## 27. `BETWEEN A AND B`의 포함 범위

원본 Comment:

```text
between A and B 는 이상/이하만 가능
```

의도는 맞지만 더 정확하게 표현하면 다음과 같다.

```text
value BETWEEN A AND B
→ value >= A AND value <= B
```

즉 **양 끝값을 모두 포함**한다.

---

<a id="sql-02-section-31"></a>

## 28. `BETWEEN`과 비교연산자 변환

```sql
WHERE sal BETWEEN 2000 AND 3000
```

은 다음과 같은 의미다.

```sql
WHERE sal >= 2000
  AND sal <= 3000
```

---

<a id="sql-02-section-32"></a>

## 29. 문제 1과 `BETWEEN`은 완전히 같은가?

아니다.

문제 1:

```sql
WHERE sal >= 2000
  AND sal < 3000
```

`BETWEEN` 예제:

```sql
WHERE sal BETWEEN 2000 AND 3000
```

차이:

```text
SAL = 3000

문제 1
→ 제외

BETWEEN
→ 포함
```

이 차이를 정확하게 구분해야 한다.

---

<a id="sql-02-section-33"></a>

## 30. `BETWEEN`의 순서

일반적인 범위는 작은 값부터 큰 값 순으로 작성한다.

```sql
WHERE sal BETWEEN 2000 AND 3000;
```

다음을 같은 의미라고 가정하면 안 된다.

```sql
WHERE sal BETWEEN 3000 AND 2000;
```

MariaDB의 일반적인 `BETWEEN` 비교에서는 Lower Bound와 Upper Bound를 자동 교환하지 않는다.

---

<a id="sql-02-section-34"></a>

## 31. 문제 2: `OR`와 `AND`

원본 문제:

```text
JOB이 CLERK이거나
급여가 2,000 초과이면서
부서 번호가 10인 사원
```

정답:

```sql
SELECT *
FROM emp
WHERE job = 'CLERK'
   OR (
        sal > 2000
        AND deptno = 10
   );
```

---

<a id="sql-02-section-35"></a>

## 32. 문제 2의 괄호가 중요한 이유

`AND`가 먼저 평가되므로 괄호 없이도 같은 결과가 나올 수 있다.

```sql
WHERE job = 'CLERK'
   OR sal > 2000
  AND deptno = 10
```

하지만 읽는 사람에게 의도를 더 명확하게 전달하려면 다음이 좋다.

```sql
WHERE job = 'CLERK'
   OR (
        sal > 2000
        AND deptno = 10
   )
```

---

<a id="sql-02-section-36"></a>

## 33. 같은 Column에 여러 `OR`

강사님 코드:

```sql
SELECT *
FROM emp
WHERE deptno = 20
   OR deptno = 30
   OR deptno = 10;
```

같은 `DEPTNO` Column을 여러 값과 비교하고 있다.

---

<a id="sql-02-section-37"></a>

## 34. `IN`

같은 Column이 여러 값 중 하나인지 확인할 때 간결하게 작성할 수 있다.

```sql
SELECT *
FROM emp
WHERE deptno IN (20, 30);
```

---

<a id="sql-02-section-38"></a>

## 35. `IN`과 `OR`

다음 두 조건은 같은 의미다.

```sql
WHERE deptno = 20
   OR deptno = 30
```

```sql
WHERE deptno IN (20, 30)
```

값이 많아질수록 `IN`이 읽기 쉽다.

---

<a id="sql-02-section-39"></a>

## 36. 세 값의 `IN`

```sql
SELECT *
FROM emp
WHERE deptno IN (10, 20, 30);
```

다음 `OR` 조건과 대응한다.

```sql
WHERE deptno = 10
   OR deptno = 20
   OR deptno = 30
```

---

<a id="sql-02-section-40"></a>

## 37. `NOT IN`

목록에 포함되지 않는 값을 찾는다.

```sql
SELECT *
FROM emp
WHERE deptno NOT IN (20, 30);
```

현재 Sample Data에서는 부서 번호가 20 또는 30이 아닌 사원을 조회한다.

---

<a id="sql-02-section-41"></a>

## 38. `NOT IN`과 `NOT`

다음처럼 이해할 수 있다.

```sql
WHERE deptno NOT IN (20, 30)
```

개념적으로:

```sql
WHERE NOT (
    deptno IN (20, 30)
)
```

---

<a id="sql-02-section-42"></a>

## 39. `NOT IN`과 `NULL` 주의

`NOT IN`의 목록이나 비교 대상에 `NULL`이 섞이면 예상과 다른 결과가 나올 수 있다.

예:

```sql
WHERE deptno NOT IN (20, 30, NULL)
```

SQL의 `NULL` 비교는 `UNKNOWN`을 만들 수 있기 때문에 단순히 “20과 30과 NULL이 아닌 값”으로 생각하면 안 된다.

이 내용은 `NULL` 조건 단원에서 다시 다룬다.

---

<a id="sql-02-section-43"></a>

## 40. 조건식 Formatting

### Before

```sql
select * from emp
where job = 'CLERK' or (SAL > 2000 and DEPTNO = 10);
```

### After

```sql
SELECT *
FROM emp
WHERE job = 'CLERK'
   OR (
        sal > 2000
        AND deptno = 10
   );
```

복합 조건은 줄바꿈과 괄호를 이용해 구조가 보이게 작성한다.

---

<a id="sql-02-section-44"></a>

## 41. 내 코드와 강사님 코드 비교

두 원본의 `WHERE` 학습 순서는 거의 동일하다.

```text
WHERE 기본
→ AND
→ OR
→ AND/OR 우선순위
→ 괄호
→ 비교연산자
→ NOT
→ 범위 문제
→ BETWEEN
→ 복합 문제
→ IN
→ NOT IN
```

내 코드는 Comment와 문제 해설이 더 상세하고, 강사님 코드는 기본 Query를 간결하게 보여 준다.

---

### 41.1 `WHERE deptno = 20`

두 코드 모두 동일하다.

```sql
SELECT *
FROM emp
WHERE deptno = 20;
```

`WHERE`의 첫 기본 예제다.

---

### 41.2 문자열 대/소문자 설명

내 코드:

```text
where의 값일 땐 '대/소문자'를 구분 함
```

강사님 코드에는 해당 설명이 없다.

이 부분은 V2에서 다음처럼 교정한다.

```text
문자열 비교의 대/소문자 구분
→ MariaDB 전체에서 고정되지 않음
→ Column·Expression의 Collation에 따라 달라질 수 있음
```

---

### 41.3 `AND`

내 코드:

```sql
WHERE deptno = 20
  AND job = 'CLERK';
```

강사님 코드도 같은 조건을 사용한다.

구조 차이는 거의 없다.

---

### 41.4 `OR`

두 코드:

```sql
WHERE deptno = 20
   OR job = 'CLERK';
```

같은 의미를 학습한다.

---

### 41.5 `AND` 우선순위

두 코드 모두 다음 Query를 사용한다.

```sql
SELECT *
FROM emp
WHERE deptno = 30
   OR deptno = 20
  AND job = 'CLERK';
```

내 코드에는 `AND`가 먼저 평가된다는 Comment가 추가되어 있다.

이 설명은 맞다.

V2에서는 괄호를 사용해 실제 평가 구조까지 명시한다.

---

### 41.6 괄호 조건

두 코드 모두 다음 Query를 사용한다.

```sql
SELECT *
FROM emp
WHERE (deptno = 30 OR deptno = 20)
  AND job = 'CLERK';
```

앞 Query와 Result가 달라질 수 있음을 비교하는 중요한 예제다.

---

### 41.7 `!=`, `<>`, `NOT`

두 코드 모두 다음 세 형태를 비교한다.

```sql
WHERE sal != 3000
```

```sql
WHERE sal <> 3000
```

```sql
WHERE NOT (sal = 3000)
```

내 코드 Comment에는 다음 설명이 있다.

```text
not은 != , <>도 사용할 수 있음
```

의도는 “같지 않다 조건을 여러 형태로 표현할 수 있다”는 뜻이지만, `NOT` 자체가 `!=` 연산자의 다른 표기라고 단정하기보다는 **조건 전체를 반전시키는 논리연산자**라고 구분하는 편이 정확하다.

---

### 41.8 문제 1

두 코드 모두:

```sql
SELECT *
FROM emp
WHERE sal >= 2000
  AND sal < 3000;
```

정확하게 문제 조건을 구현한다.

---

### 41.9 `BETWEEN`

두 코드 모두:

```sql
SELECT *
FROM emp
WHERE sal BETWEEN 2000 AND 3000;
```

내 코드:

```text
이상/이하만 가능
```

강사님 코드:

```text
A 이상 and B 이하
```

V2에서는 다음으로 통일한다.

```text
BETWEEN A AND B
→ >= A AND <= B
→ 양 끝값 포함
```

---

### 41.10 문제 2

내 코드:

```sql
SELECT *
FROM emp
WHERE job = 'CLERK'
   OR (sal > 2000 AND deptno = 10);
```

강사님 코드:

```sql
SELECT *
FROM emp
WHERE
    job = 'CLERK'
    OR (sal > 2000 AND deptno = 10)
```

내용은 동일하고 Formatting만 조금 다르다.

---

### 41.11 강사님 코드의 세 부서 `OR`

강사님 코드에는 다음 Query가 추가되어 있다.

```sql
SELECT *
FROM emp
WHERE deptno = 20
   OR deptno = 30
   OR deptno = 10;
```

바로 뒤 `IN`으로 줄일 수 있는 이유를 보여 주는 좋은 비교 예제다.

---

### 41.12 내 코드의 `IN`

내 코드는 다음 Comment로 원리를 설명한다.

```text
where에서 컬럼이 같고 or일 때 줄일 수 있는 방법 (in)
```

핵심 방향은 맞다.

더 정확하게는:

```text
같은 Expression이
여러 값 중 하나와 일치하는지 확인
→ IN
```

으로 이해한다.

---

### 41.13 `NOT IN`

두 코드 모두:

```sql
SELECT *
FROM emp
WHERE deptno NOT IN (20, 30);
```

같은 예제를 사용한다.

---

### 41.14 원본 비교 요약

| 항목 | 내 코드 | 강사님 코드 | V2 정리 |
| --- | --- | --- | --- |
| WHERE 기본 | 있음 | 있음 | Row Filtering |
| 문자열 Case 설명 | 대/소문자 구분한다고 설명 | 없음 | Collation에 따라 결정 |
| AND | 있음 | 있음 | 모두 True |
| OR | 있음 | 있음 | 하나 이상 True |
| 우선순위 | Comment 상세 | Query 중심 | `AND`가 `OR`보다 우선 |
| 괄호 | 있음 | 있음 | 의도 명확화 |
| `!=` | 있음 | 있음 | 같지 않음 |
| `<>` | 있음 | 있음 | SQL 표준 Not Equal |
| `NOT` | `!=`와 묶어 설명 | Query만 있음 | 조건 전체 반전 |
| 문제 1 | 있음 | 있음 | 2000 포함, 3000 제외 |
| BETWEEN | 포함 범위 설명 | 포함 범위 설명 | 양 끝값 포함 |
| 문제 2 | 있음 | 있음 | OR + AND 그룹 |
| 세 부서 OR | Comment로 축약 예시 | 실제 Query | IN 변환 예제 |
| IN | 있음 | 있음 | 동일 Expression 다중 값 비교 |
| NOT IN | 있음 | 있음 | 값 집합 제외 |

---

<a id="sql-02-section-45"></a>

## 42. 개선된 통합 예제

```sql
-- 부서 20의 사원
SELECT
    empno,
    ename,
    job,
    sal,
    deptno
FROM emp
WHERE deptno = 20;

-- 부서 20의 CLERK
SELECT
    empno,
    ename,
    job,
    deptno
FROM emp
WHERE deptno = 20
  AND job = 'CLERK';

-- 부서 20 또는 30
SELECT
    empno,
    ename,
    deptno
FROM emp
WHERE deptno IN (20, 30);

-- 부서 20 또는 30의 CLERK
SELECT
    empno,
    ename,
    job,
    deptno
FROM emp
WHERE deptno IN (20, 30)
  AND job = 'CLERK';

-- 급여 2000 이상 3000 미만
SELECT
    empno,
    ename,
    sal
FROM emp
WHERE sal >= 2000
  AND sal < 3000;

-- 급여 2000 이상 3000 이하
SELECT
    empno,
    ename,
    sal
FROM emp
WHERE sal BETWEEN 2000 AND 3000;
```

---

<a id="sql-02-section-46"></a>

## 43. 실무 조건식 작성 기준

복잡한 `WHERE`는 다음 기준으로 작성한다.

```text
1. 조건 하나당 의미를 명확히 한다.
2. AND와 OR를 한 줄에 몰아쓰지 않는다.
3. 우선순위에 의존하기보다 필요한 괄호를 사용한다.
4. 같은 Column의 여러 값은 IN을 검토한다.
5. 범위의 경계값 포함 여부를 먼저 확인한다.
6. 문자열 비교의 Collation을 확인한다.
7. NULL이 포함될 가능성을 고려한다.
```

---

<a id="sql-02-section-47"></a>

## 44. `AND`와 `OR` 리팩토링

### Before

```sql
SELECT *
FROM emp
WHERE deptno = 10
   OR deptno = 20
   OR deptno = 30;
```

### After

```sql
SELECT *
FROM emp
WHERE deptno IN (10, 20, 30);
```

같은 Column 비교가 반복되면 `IN`이 더 읽기 쉽다.

---

<a id="sql-02-section-48"></a>

## 45. 범위 조건 리팩토링

### 포함 범위

```sql
WHERE sal BETWEEN 2000 AND 3000
```

### 상한 제외

```sql
WHERE sal >= 2000
  AND sal < 3000
```

`BETWEEN`을 무조건 짧다는 이유로 사용하지 않고 **경계 조건**에 맞춰 선택한다.

---

<a id="sql-02-section-49"></a>

## 46. 문자열 조건 실무 주의

다음 Query:

```sql
SELECT *
FROM emp
WHERE job = 'clerk';
```

Result가 나오는지 여부만 보고 “SQL은 대소문자를 구분하지 않는다”고 결론 내리면 안 된다.

확인 순서:

```text
Column Type
    ↓
Character Set
    ↓
Collation
    ↓
Comparison Expression
```

---

<a id="sql-02-section-50"></a>

## 47. 자주 하는 실수

### 47.1 `AND`와 `OR` 우선순위를 반대로 이해

`AND`가 `OR`보다 먼저 평가된다.

### 47.2 괄호 없이 긴 조건 작성

동작은 맞아도 유지보수가 어렵다.

### 47.3 `BETWEEN`이 끝값을 제외한다고 생각

양 끝값을 포함한다.

### 47.4 문제 1을 `BETWEEN 2000 AND 3000`으로 변경

문제는 `3000 미만`이므로 결과가 달라진다.

### 47.5 `IN`을 Column 여러 개 비교 기능이라고 생각

기본 형태는 **하나의 Expression을 값 목록과 비교**한다.

### 47.6 `NOT`을 단순히 `!=` 기호의 다른 이름으로 생각

`NOT`은 논리 조건을 반전시키는 Operator다.

### 47.7 문자열 Case Sensitivity를 MariaDB 전체 특성으로 단정

Collation을 확인해야 한다.

---

<a id="sql-02-section-51"></a>

## 48. Debugging

조건 결과가 예상과 다르면 다음을 확인한다.

```text
1. Column 값 자체를 먼저 SELECT했는가?
2. 숫자와 문자열 Type을 혼동하지 않았는가?
3. 문자열 Literal에 Quote를 사용했는가?
4. AND/OR 우선순위를 확인했는가?
5. 괄호 위치가 의도와 맞는가?
6. BETWEEN 끝값 포함 여부를 확인했는가?
7. IN 목록 값이 올바른가?
8. 문자열 Collation을 확인했는가?
9. NULL이 조건에 포함될 가능성이 있는가?
```

---

<a id="sql-02-section-52"></a>

## 49. 종합실습

### 문제 1

부서 번호가 `30`인 사원의 사원 번호, 이름, 직무를 조회하시오.

---

### 문제 2

급여가 `1500` 이상인 사원의 이름과 급여를 조회하시오.

---

### 문제 3

직무가 `MANAGER`가 아니면서 부서 번호가 `20`인 사원을 조회하시오.

---

### 문제 4

부서 번호가 `10`, `20`, `30` 중 하나인 사원을 `IN`으로 조회하시오.

---

### 문제 5

부서 번호가 `20`, `30`이 아닌 사원을 조회하시오.

---

### 문제 6

급여가 `2000 이상 3000 미만`인 사원을 조회하시오.

`BETWEEN`을 사용하지 않는다.

---

### 문제 7

급여가 `2000 이상 3000 이하`인 사원을 `BETWEEN`으로 조회하시오.

---

### 문제 8

부서 번호가 `20 또는 30`이고 직무가 `CLERK`인 사원을 조회하시오.

---

### 문제 9

직무가 `CLERK`이거나, `급여가 2000 초과이면서 부서 번호가 10`인 사원을 조회하시오.

의도가 보이도록 괄호를 사용한다.

---

<a id="sql-02-section-53"></a>

## 50. 정답과 해설

### 문제 1

```sql
SELECT
    empno,
    ename,
    job
FROM emp
WHERE deptno = 30;
```

---

### 문제 2

```sql
SELECT
    ename,
    sal
FROM emp
WHERE sal >= 1500;
```

---

### 문제 3

```sql
SELECT *
FROM emp
WHERE job <> 'MANAGER'
  AND deptno = 20;
```

`!=`도 MariaDB에서 사용할 수 있다.

---

### 문제 4

```sql
SELECT *
FROM emp
WHERE deptno IN (10, 20, 30);
```

같은 Column에 대한 여러 `OR`를 `IN`으로 간결하게 표현한다.

---

### 문제 5

```sql
SELECT *
FROM emp
WHERE deptno NOT IN (20, 30);
```

---

### 문제 6

```sql
SELECT *
FROM emp
WHERE sal >= 2000
  AND sal < 3000;
```

`3000`은 제외한다.

---

### 문제 7

```sql
SELECT *
FROM emp
WHERE sal BETWEEN 2000 AND 3000;
```

양 끝값을 모두 포함한다.

---

### 문제 8

```sql
SELECT *
FROM emp
WHERE deptno IN (20, 30)
  AND job = 'CLERK';
```

---

### 문제 9

```sql
SELECT *
FROM emp
WHERE job = 'CLERK'
   OR (
        sal > 2000
        AND deptno = 10
   );
```

괄호로 `AND` 조건 Group을 명확히 표현한다.

---

<a id="sql-02-section-54"></a>

## 51. 최종 체크리스트

- [ ] `WHERE`가 Row를 Filtering한다는 점을 설명할 수 있는가?
- [ ] `SELECT` List와 `WHERE`의 역할 차이를 이해하는가?
- [ ] `=`로 같은 값을 비교할 수 있는가?
- [ ] `!=`, `<>`로 같지 않음을 표현할 수 있는가?
- [ ] `>`, `>=`, `<`, `<=` 경계값 차이를 이해하는가?
- [ ] 문자열 Literal에 Quote를 사용할 수 있는가?
- [ ] 문자열 대/소문자 비교가 Collation에 따라 달라질 수 있음을 아는가?
- [ ] `AND` 조건은 모두 True여야 한다는 점을 이해하는가?
- [ ] `OR` 조건은 하나 이상 True면 된다는 점을 이해하는가?
- [ ] `AND`가 `OR`보다 먼저 평가된다는 점을 설명할 수 있는가?
- [ ] 괄호로 조건 Group을 명확하게 만들 수 있는가?
- [ ] `NOT`이 조건을 반전시키는 Operator임을 이해하는가?
- [ ] `NOT`과 `!=`가 완전히 같은 문법 요소가 아님을 아는가?
- [ ] `BETWEEN A AND B`가 A와 B를 모두 포함한다는 점을 설명할 수 있는가?
- [ ] `2000 이상 3000 미만`과 `BETWEEN 2000 AND 3000`의 차이를 설명할 수 있는가?
- [ ] `IN`으로 같은 Column의 여러 값 조건을 표현할 수 있는가?
- [ ] `NOT IN`으로 값 목록을 제외할 수 있는가?
- [ ] `NOT IN`과 `NULL` 조합에 주의가 필요함을 알고 있는가?
- [ ] 복합 조건을 읽기 쉽게 줄바꿈할 수 있는가?
- [ ] 실제 Result가 이상할 때 우선순위·괄호·Collation을 점검할 수 있는가?

---

<a id="sql-02-section-55"></a>

## 52. 핵심 요약

```text
WHERE
→ Row Filtering
```

```text
=
→ 같다

!= / <>
→ 같지 않다

> / >= / < / <=
→ 크기 비교
```

```text
AND
→ 모든 조건 만족

OR
→ 하나 이상 만족

NOT
→ 조건 결과 반전
```

```text
AND
→ OR보다 우선순위 높음

복잡한 조건
→ 괄호로 의도 명확화
```

```text
BETWEEN A AND B
→ >= A
AND
→ <= B
```

```text
IN (10, 20, 30)
→ 같은 Expression이
  여러 값 중 하나인지 확인

NOT IN
→ 해당 값 목록 제외
```

```text
문자열 대/소문자 비교
→ MariaDB 전체에 고정된 규칙 아님
→ Collation 확인
```

---

<a id="sql-02-section-56"></a>

## 마무리

`WHERE`의 핵심은 단순히 조건문을 붙이는 것이 아니다.

```text
어떤 Row를 원하는지 정의하고
    ↓
조건을 작은 단위로 나누고
    ↓
AND / OR 관계를 결정하고
    ↓
경계값을 확인하고
    ↓
필요한 경우 괄호와 IN으로 의도를 명확하게 만드는 것
```

이 흐름을 이해하면 다음 단계인 `LIKE`, Pattern 검색, `NULL` 조건도 훨씬 자연스럽게 확장할 수 있다.
<a id="sql-02-section-57"></a>

## V3 동작 백과 — WHERE는 어떤 Row를 남기는가?

> 입력 범위 확인: 이 복습 부분의 작은 표는 처리 원리를 위한 가정·발췌이며 전체 초기화 EMP의 입력 전체가 아니다. FROM emp를 그대로 실행하면 모든 대상 사원을 처리한다. 수치는 작은 가정 입력의 결과인지 전체 14행 결과인지 구분한다. 실행·시간순 설명은 논리적 설명이며 물리적 평가 순서를 보장하지 않는다.

<a id="index-section-118"></a>

### 기존 작은 입력 표를 실행 가능한 CTE로 재현

기존 V3 복습 표는 세 행만 있다고 가정한 설명이다. 실제 초기화 EMP의 같은 조건에서는 JONES·SCOTT·ADAMS·FORD가 남는다. 작은 표의 JONES 한 행을 얻으려면 아래처럼 표에 해당하는 입력을 별도로 만든다.

```sql
WITH sample(empno,ename,deptno,sal) AS (
 SELECT 7369,'SMITH',20,800 UNION ALL
 SELECT 7566,'JONES',20,2975 UNION ALL
 SELECT 7499,'ALLEN',30,1600
)
SELECT empno,ename,deptno,sal FROM sample
WHERE deptno=20 AND sal>=1000 ORDER BY empno;
```

```text
empno	ename	deptno	sal
7566	JONES	20	2975
```

아래 기존 표는 이 작은 입력을 손으로 따라가는 복습 설명이다.


### 왜 배워야 하는가?

Table 전체가 아니라 필요한 Row만 읽어야 업무 질문에 답하고, 불필요한 Data 처리와 위험한 전체 수정·삭제를 피할 수 있다.

### 조건값은 어디서 오는가?

SQL에 직접 작성할 수도 있고 Application의 검색 Form·API Parameter에서 전달받을 수도 있다.

```sql
SELECT empno, ename, deptno, sal
FROM emp
WHERE deptno = 20
  AND sal >= 1000;
```

```text
FROM emp에서 후보 Row 구성
→ Row마다 deptno = 20 평가
→ True인 Row에 sal >= 1000 평가
→ 두 조건이 모두 True인 Row만 유지
→ SELECT Column으로 Result 생성
```

입력:

```text
ENAME | DEPTNO | SAL
SMITH | 20     | 800
JONES | 20     | 2975
ALLEN | 30     | 1600
```

결과:

```text
JONES | 20 | 2975
```

SMITH는 급여 조건이 False이고 ALLEN은 부서 조건이 False라 제외된다.

### AND·OR의 실제 평가

```sql
WHERE deptno = 20
   OR deptno = 30 AND sal >= 2000
```

`AND`가 먼저 평가되므로 다음과 같다.

```text
deptno = 20 OR (deptno = 30 AND sal >= 2000)
```

의도가 “20·30번 부서 모두 급여 2000 이상”이라면 괄호가 필요하다.

```sql
WHERE (deptno = 20 OR deptno = 30)
  AND sal >= 2000;
```

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 검색 Anchor | 강사님 코드 검색 Anchor |
| --- | --- | --- |
| 기본 조건 | `where deptno = 20` | 같은 Query |
| AND·OR | `and`, `or` 조건 실습 | 같은 조건 구간 |
| 범위 | `between` | `between` |
| 목록 | ` in (` | ` in (` |
| 부정 | `not in`, `!=`, `<>` | 같은 연산자 구간 |

실행 전 조건을 말로 읽고, 실행 후 예상 Row와 실제 Row가 같은지 비교한다.
