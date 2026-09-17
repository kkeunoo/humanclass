---
title: SQL LIKE와 NULL
version: v4.0-detailed-encyclopedia
last_updated: 2026-09-17
status: Completed
---

# SQL LIKE와 NULL

## 이 문서에서 바로 찾기

- [학습 목표](#sql-03-section-2)
- [개념에서 실제 실행까지 — LIKE와 NULL이란? — 패턴과 알 수 없는 값](#sql-03-section-3)
- [36. `NULL`이 포함된 비교](#sql-03-section-39)
- [43. 내 코드와 강사님 코드 비교](#sql-03-section-46)
- [49. Debugging](#sql-03-section-52)
- [50. 종합실습](#sql-03-section-53)
- [51. 정답과 해설](#sql-03-section-54)
- [52. 최종 체크리스트](#sql-03-section-55)
- [53. 핵심 요약](#sql-03-section-56)

<details>
<summary>상세 목차 전체 펼치기</summary>

- [문서 정보](#sql-03-section-1)
- [학습 목표](#sql-03-section-2)
- [개념에서 실제 실행까지 — LIKE와 NULL이란? — 패턴과 알 수 없는 값](#sql-03-section-3)
- [1. `LIKE`란?](#sql-03-section-4)
- [2. 기본 구조](#sql-03-section-5)
- [3. `%` Wildcard](#sql-03-section-6)
- [4. Prefix 검색](#sql-03-section-7)
- [5. Suffix 검색](#sql-03-section-8)
- [6. Contains 검색](#sql-03-section-9)
- [7. `%`는 0글자도 허용한다](#sql-03-section-10)
- [8. `_` Wildcard](#sql-03-section-11)
- [9. `%`와 `_`의 차이](#sql-03-section-12)
- [10. 특정 길이 Pattern](#sql-03-section-13)
- [11. 두 번째 Character 조건](#sql-03-section-14)
- [12. 세 번째 Character 조건](#sql-03-section-15)
- [13. Prefix + Length](#sql-03-section-16)
- [14. `LIKE`와 대/소문자](#sql-03-section-17)
- [15. Collation 확인](#sql-03-section-18)
- [16. `NOT LIKE`](#sql-03-section-19)
- [17. `NOT LIKE` 해석](#sql-03-section-20)
- [18. 여러 `LIKE` 조건](#sql-03-section-21)
- [19. `LIKE`와 `AND`](#sql-03-section-22)
- [20. `%A%`를 무조건 사용하면 안 되는 이유](#sql-03-section-23)
- [21. `LIKE`는 정확히 일치 검색이 아니다](#sql-03-section-24)
- [22. `LIKE` Pattern 안의 `%`와 `_`](#sql-03-section-25)
- [23. `NULL`이란?](#sql-03-section-26)
- [24. `NULL`과 0](#sql-03-section-27)
- [25. `NULL`과 빈 문자열](#sql-03-section-28)
- [26. `NULL = NULL`은 True인가?](#sql-03-section-29)
- [27. 왜 `NULL = NULL`이 True가 아닌가?](#sql-03-section-30)
- [28. `COMM = NULL`의 문제](#sql-03-section-31)
- [29. `IS NULL`](#sql-03-section-32)
- [30. `IS NOT NULL`](#sql-03-section-33)
- [31. `= NULL`과 `IS NULL`](#sql-03-section-34)
- [32. `!= NULL`의 문제](#sql-03-section-35)
- [33. `<> NULL`도 같은 문제](#sql-03-section-36)
- [34. `NOT (comm IS NULL)`](#sql-03-section-37)
- [35. `NULL`이 포함된 산술](#sql-03-section-38)
- [36. `NULL`이 포함된 비교](#sql-03-section-39)
- [37. WHERE에서 Unknown](#sql-03-section-40)
- [38. `NOT IN`과 `NULL`](#sql-03-section-41)
- [39. `NOT IN`의 개념적 전개](#sql-03-section-42)
- [40. `NOT IN (..., NULL)`의 문제](#sql-03-section-43)
- [41. Subquery의 `NOT IN`도 주의](#sql-03-section-44)
- [42. `LIKE`와 `NULL`](#sql-03-section-45)
- [43. 내 코드와 강사님 코드 비교](#sql-03-section-46)
- [44. 개선된 통합 예제](#sql-03-section-47)
- [45. 실무 Pattern 검색 기준](#sql-03-section-48)
- [46. LIKE 성능 주의](#sql-03-section-49)
- [47. NULL 조건 실무 기준](#sql-03-section-50)
- [48. 자주 하는 실수](#sql-03-section-51)
- [49. Debugging](#sql-03-section-52)
- [50. 종합실습](#sql-03-section-53)
- [51. 정답과 해설](#sql-03-section-54)
- [52. 최종 체크리스트](#sql-03-section-55)
- [53. 핵심 요약](#sql-03-section-56)
- [마무리](#sql-03-section-57)
- [V3 동작 백과 — Pattern과 Unknown은 어떻게 평가되는가?](#sql-03-section-58)

</details>

---

<a id="sql-03-section-1"></a>

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `03_SQL_LIKE와_NULL.md` |
| 분류 | `05_SQL` |
| 원본 기준 | `workspace_sql/Script.sql`, `workspace_teacher/workspace_sql/Script.sql` |
| DB 기준 자료 | `[DB]학습용_emp 신규-mariadb.sql` |
| DBMS | MariaDB |
| 핵심 범위 | `LIKE`, `%`, `_`, `NOT LIKE`, `IS NULL`, `IS NOT NULL`, `NULL` 비교, `NOT IN`과 `NULL` |
| 학습 범위 | 문자열 Pattern Matching, Wildcard, NULL 조건식, Unknown 비교 |
| 다음 범위 제외 | `ORDER BY`, `LIMIT`, Aggregate Function |
| 문서 형식 | SQL Developer-Wiki V3 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드의 `Script.sql`에서 `LIKE`와 `NULL` 조건을 비교해 정리한다.  
> `%`, `_`의 의미와 Pattern 검색을 정리하고, `NULL = NULL`이 True가 아닌 이유, `IS NULL`·`IS NOT NULL`의 필요성, `NOT IN`에 `NULL`이 섞일 때 발생할 수 있는 문제까지 연결한다.

---

<a id="sql-03-section-2"></a>

## 학습 목표

- 와일드카드와 TRUE·FALSE·UNKNOWN을 구분한다.
- 실제 입력·중간 상태·결과와 실패 조건을 직접 확인한다.

---

<a id="sql-03-section-3"></a>

## 개념에서 실제 실행까지 — LIKE와 NULL이란? — 패턴과 알 수 없는 값

### 무엇이며 왜 배워야 할까?

LIKE는 문자열이 패턴에 맞는지 검사한다. %는 0개 이상의 문자, _는 정확히 한 문자를 뜻한다. '%AM%'는 AM이 연속으로 들어간 이름을 찾는 조건이며 단순히 A나 M 하나가 있다는 뜻이 아니다. 대소문자 동작은 문자열 collation을 확인한다.

NULL은 0·빈 문자열과 다른 ‘값이 없거나 알 수 없음’을 나타낸다. COMM=NULL 비교는 값 없음인지 확인하는 문법이 아니다. NULL과의 일반 비교 결과는 UNKNOWN이며 WHERE에서 제거된다. IS NULL은 값 없음 여부를 판정한다.

NOT IN 목록에 NULL이 있으면 예상 밖의 누락이 생긴다. 20 NOT IN(10,NULL)은 ‘20은 10과 다르고 NULL과도 다르다’인데 후반 비교를 확정할 수 없다. 따라서 그 행이 TRUE로 통과하지 못한다. NULL이 낀 조건을 단순한 참·거짓 두 상태만으로 해석하면 안 된다.

### 입력은 어디에서 오는가?

EMP·DEPT·SALGRADE는 초기화 자료 그대로 준비된 상태다. EMP 14행, DEPT 4행, SALGRADE 5행이다. 다른 DML로 데이터를 바꿨다면 아래 결과와 달라질 수 있다. 상수 SELECT 예제는 테이블 없이도 실행할 수 있다.

### 실행 가능한 보충 SQL과 결과

아래는 원본의 개념을 작은 검증 범위로 정리한 보충 예제다. MariaDB 12.3.2, 일반 SQL 모드·InnoDB 기준에서 결과를 확인했다. 조회 SQL은 SQL 편집기의 Result Grid, 변경 SQL은 영향 행 표시와 사후 SELECT로 관찰한다. DBMS·모드·데이터 상태가 다르면 차이를 확인해야 한다.

```sql
SELECT ename, comm,
       CASE WHEN comm IS NULL THEN 'missing'
            WHEN comm = 0 THEN 'zero'
            ELSE 'present' END AS comm_state
FROM emp
WHERE empno IN (7369, 7499, 7844)
ORDER BY empno;
SELECT NULL = NULL AS normal_comparison,
       NULL IS NULL AS null_test,
       20 NOT IN (10, NULL) AS exclusion;
```

Result Grid의 열·행 값:

```text
ename	comm	comm_state
SMITH	NULL	missing
ALLEN	300.00	present
TURNER	0.00	zero
normal_comparison	null_test	exclusion
NULL	1	NULL
```

여러 SELECT가 있으면 위 출력에 결과 헤더가 다시 나타난다. 숫자의 표시 자릿수와 NULL 표시 모양은 클라이언트별로 달라질 수 있지만 값과 행의 의미를 먼저 비교한다.

### 논리적 처리와 상태 변화 — 단계별로 따라가기

1. COMM이 NULL인지 IS NULL로 판정한다.
2. CASE가 각 행의 보너스 상태 표시를 만든다. 결과 표시이며 데이터 저장 변경은 아니다.
3. 대상 세 명에는 NULL·양수·0 상태가 각각 존재한다.
4. 별도 상수 SELECT로 일반 비교와 NOT IN의 UNKNOWN을 확인한다.

### 내 코드·강사님 코드의 어느 부분에 있었을까?


#### 내 코드: `workspace_sql/Script.sql` 163~172행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
select * from emp;

select * from emp
where comm = null;

select * from emp
where comm < 100;

-- Query에서 null상태는 'is null' 또는 'is not null'로 구분한다
select * from emp
```

#### 강사님 코드: `workspace_teacher/workspace_sql/Script.sql` 129~138행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
select * from emp;

select * from emp
where comm = null;

select * from emp
where comm < 100;

select * from emp
where comm is null;
```

두 원본 모두 comm=null과 IS NULL을 대비한다. 앞 SQL이 문법 오류를 내는 것이 아니라 조건이 TRUE인 행을 얻지 못한다는 점이 중요하다.

### 실무에서 사용하거나 디버깅할 때

표현식 결과와 저장 데이터 변경을 구분한다. 결과가 다르면 원본의 앞선 실행 상태, 입력 행 수, NULL·중복·경계값, 조인 후 행 수를 확인한다. 오류 없이 종료한 변경도 0행 대상일 수 있다. 실제 실행 순서·성능은 아래 본문의 논리 설명만으로 단정하지 말고 실행 계획·사후 조회로 검증한다.

### 이해 확인 실습

1. TURNER의 comm=0도 IS NULL로 통과할까?
2. comm<>NULL과 NOT(comm IS NULL)은 같은가?

<details>
<summary>정답과 판단 근거 펼치기</summary>

1. 아니다. 0은 실제 숫자 값이며 NULL 상태와 다르다.
2. 아니다. 전자는 일반 비교의 UNKNOWN, 후자는 NULL 여부의 부정이다.

</details>

### 이 개념을 다시 사용할 수 있는지 확인

- [ ] 개념·필요성·입력 컬럼과 자료형을 내 말로 설명한다.
- [ ] 중간 행·그룹·관계와 최종 결과를 구분한다.
- [ ] 원본 코드의 앞 상태와 보충 예제의 조건을 구분한다.
- [ ] NULL·0행·중복·경계값 또는 변경 실패를 재검토한다.

---

<a id="sql-03-section-4"></a>

## 1. `LIKE`란?

`LIKE`는 문자열 값이 특정 Pattern과 일치하는지 확인할 때 사용한다.

```sql
SELECT *
FROM emp
WHERE ename LIKE 'S%';
```

이 Query는 이름이 `S`로 시작하는 사원을 찾는다.

---

<a id="sql-03-section-5"></a>

## 2. 기본 구조

```sql
SELECT
    column_list
FROM table_name
WHERE column_name LIKE 'pattern';
```

예:

```sql
SELECT
    empno,
    ename
FROM emp
WHERE ename LIKE 'S%';
```

---

<a id="sql-03-section-6"></a>

## 3. `%` Wildcard

`%`는 **길이 0 이상인 임의의 문자열**을 의미한다.

```text
%
→ 아무 Character도 없을 수 있음
→ 1개 이상일 수도 있음
→ 여러 Character일 수도 있음
```

예:

```sql
WHERE ename LIKE 'S%'
```

의미:

```text
S
S로 시작하는 모든 문자열
```

---

<a id="sql-03-section-7"></a>

## 4. Prefix 검색

문자열이 특정 값으로 시작하는지 확인한다.

```sql
SELECT *
FROM emp
WHERE ename LIKE 'S%';
```

예상 Sample:

```text
SMITH
SCOTT
```

---

<a id="sql-03-section-8"></a>

## 5. Suffix 검색

특정 값으로 끝나는 문자열을 찾는다.

```sql
SELECT *
FROM emp
WHERE ename LIKE '%S';
```

의미:

```text
마지막 Character가 S
```

---

<a id="sql-03-section-9"></a>

## 6. Contains 검색

문자열 내부에 특정 Pattern이 포함되는지 확인한다.

```sql
SELECT *
FROM emp
WHERE ename LIKE '%A%';
```

이름 어딘가에 `A`가 있는 Row를 찾는다.

---

<a id="sql-03-section-10"></a>

## 7. `%`는 0글자도 허용한다

Pattern:

```sql
LIKE 'S%'
```

은 다음도 Matching 가능하다.

```text
S
SMITH
SCOTT
```

`%` 부분은 Character가 없어도 된다.

---

<a id="sql-03-section-11"></a>

## 8. `_` Wildcard

`_`는 정확히 **한 Character 위치**를 의미한다.

```sql
SELECT *
FROM emp
WHERE ename LIKE '_MITH';
```

첫 Character는 어떤 값이든 가능하고 뒤에는 `MITH`가 와야 한다.

Sample Data에서는:

```text
SMITH
```

가 Matching된다.

---

<a id="sql-03-section-12"></a>

## 9. `%`와 `_`의 차이

```text
%
→ 0개 이상의 Character

_
→ 정확히 1개의 Character
```

예:

```sql
LIKE 'S%'
```

```text
S
SMITH
SCOTT
```

예:

```sql
LIKE 'S____'
```

```text
S + 정확히 4글자
→ 총 5글자
```

---

<a id="sql-03-section-13"></a>

## 10. 특정 길이 Pattern

5글자 이름 중 `S`로 시작하는 경우:

```sql
SELECT *
FROM emp
WHERE ename LIKE 'S____';
```

`_`가 4개이므로:

```text
S + 4 Character
→ 총 5 Character
```

---

<a id="sql-03-section-14"></a>

## 11. 두 번째 Character 조건

두 번째 Character가 `A`인 이름:

```sql
SELECT *
FROM emp
WHERE ename LIKE '_A%';
```

해석:

```text
첫 번째 Character
→ 아무 값

두 번째 Character
→ A

그 뒤
→ 아무 길이
```

---

<a id="sql-03-section-15"></a>

## 12. 세 번째 Character 조건

세 번째 Character가 `A`:

```sql
SELECT *
FROM emp
WHERE ename LIKE '__A%';
```

---

<a id="sql-03-section-16"></a>

## 13. Prefix + Length

`S`로 시작하고 총 5글자인 이름:

```sql
SELECT *
FROM emp
WHERE ename LIKE 'S____';
```

`S%`와 달리 길이가 고정된다.

---

<a id="sql-03-section-17"></a>

## 14. `LIKE`와 대/소문자

02번에서 정리한 것처럼 문자열 Pattern Matching의 대/소문자 구분 여부도 Collation 영향을 받을 수 있다.

```sql
SELECT *
FROM emp
WHERE ename LIKE 's%';
```

이 Query가 `SMITH`를 찾는지는 Column Collation에 따라 달라질 수 있다.

---

<a id="sql-03-section-18"></a>

## 15. Collation 확인

```sql
SHOW FULL COLUMNS
FROM emp;
```

또는 Database 기본 Collation:

```sql
SELECT
    @@collation_database;
```

> [!IMPORTANT]
> `LIKE`가 대/소문자를 무조건 구분한다고 단정하지 않는다.

---

<a id="sql-03-section-19"></a>

## 16. `NOT LIKE`

Pattern과 일치하지 않는 Row를 찾는다.

```sql
SELECT *
FROM emp
WHERE ename NOT LIKE 'S%';
```

`S`로 시작하지 않는 이름을 조회한다.

---

<a id="sql-03-section-20"></a>

## 17. `NOT LIKE` 해석

```sql
WHERE ename NOT LIKE 'S%'
```

개념적으로:

```sql
WHERE NOT (
    ename LIKE 'S%'
)
```

---

<a id="sql-03-section-21"></a>

## 18. 여러 `LIKE` 조건

이름이 `S` 또는 `A`로 시작하는 사원:

```sql
SELECT *
FROM emp
WHERE ename LIKE 'S%'
   OR ename LIKE 'A%';
```

---

<a id="sql-03-section-22"></a>

## 19. `LIKE`와 `AND`

직무가 `CLERK`이고 이름이 `S`로 시작:

```sql
SELECT *
FROM emp
WHERE job = 'CLERK'
  AND ename LIKE 'S%';
```

---

<a id="sql-03-section-23"></a>

## 20. `%A%`를 무조건 사용하면 안 되는 이유

다음 Query는 편리하다.

```sql
WHERE ename LIKE '%A%'
```

하지만 Leading Wildcard가 있는 Pattern은 Index 활용이 제한될 수 있다.

```text
'A%'
→ Prefix 검색
→ Index 활용 가능성이 상대적으로 높음

'%A%'
→ 앞부분이 고정되지 않음
→ Index 활용이 어려울 수 있음
```

정확한 성능은 실행계획과 DBMS 조건을 확인해야 한다.

---

<a id="sql-03-section-24"></a>

## 21. `LIKE`는 정확히 일치 검색이 아니다

다음 두 Query는 목적이 다르다.

```sql
WHERE job = 'CLERK'
```

```sql
WHERE job LIKE 'CLERK'
```

Wildcard가 없다면 결과가 같을 수 있지만 정확히 같은 값을 찾는 목적이라면 `=`이 더 명확하다.

---

<a id="sql-03-section-25"></a>

## 22. `LIKE` Pattern 안의 `%`와 `_`

`%`, `_`는 Pattern 문자로 동작한다.

실제 문자 `%`나 `_` 자체를 검색하려면 Escape 전략이 필요하다.

MariaDB에서는 `ESCAPE` Clause를 사용할 수 있다.

```sql
SELECT *
FROM sample
WHERE code LIKE 'A\_%' ESCAPE '\';
```

이 단원에서는 기본 Pattern 검색만 다룬다.

---

<a id="sql-03-section-26"></a>

## 23. `NULL`이란?

`NULL`은 값이 0이라는 뜻이 아니다.

```text
NULL
→ 값이 없음
→ 또는 알 수 없음
```

---

<a id="sql-03-section-27"></a>

## 24. `NULL`과 0

```text
0
→ 실제 숫자 값

NULL
→ 값 자체가 없음 / 알 수 없음
```

Sample EMP Data:

```text
TURNER.COMM
→ 0

여러 사원의 COMM
→ NULL
```

둘은 다르다.

---

<a id="sql-03-section-28"></a>

## 25. `NULL`과 빈 문자열

```text
''
→ 길이 0인 문자열 값

NULL
→ 값이 없음 / 알 수 없음
```

MariaDB에서는 둘을 같은 것으로 보면 안 된다.

---

<a id="sql-03-section-29"></a>

## 26. `NULL = NULL`은 True인가?

아니다.

```sql
SELECT NULL = NULL;
```

Result:

```text
NULL
```

즉 SQL의 Truth Value 관점에서:

```text
True
False
Unknown
```

중 `Unknown`에 해당한다.

---

<a id="sql-03-section-30"></a>

## 27. 왜 `NULL = NULL`이 True가 아닌가?

`NULL`은 특정 값이 아니라 “알 수 없음” 상태다.

```text
알 수 없는 값
=
알 수 없는 값

→ 서로 같은 값이라고 확정할 수 없음
→ Unknown
```

---

<a id="sql-03-section-31"></a>

## 28. `COMM = NULL`의 문제

잘못된 조건:

```sql
SELECT *
FROM emp
WHERE comm = NULL;
```

이 조건은 우리가 원하는 “COMM 값이 없는 Row” 검색으로 동작하지 않는다.

---

<a id="sql-03-section-32"></a>

## 29. `IS NULL`

`NULL` 여부를 확인할 때 사용한다.

```sql
SELECT *
FROM emp
WHERE comm IS NULL;
```

`COMM` 값이 없는 Row를 조회한다.

---

<a id="sql-03-section-33"></a>

## 30. `IS NOT NULL`

```sql
SELECT *
FROM emp
WHERE comm IS NOT NULL;
```

`COMM` 값이 존재하는 Row를 조회한다.

---

<a id="sql-03-section-34"></a>

## 31. `= NULL`과 `IS NULL`

### 잘못된 방식

```sql
WHERE comm = NULL
```

### 올바른 방식

```sql
WHERE comm IS NULL
```

---

<a id="sql-03-section-35"></a>

## 32. `!= NULL`의 문제

다음도 원하는 결과가 아니다.

```sql
WHERE comm != NULL
```

`NULL` 비교는 Unknown이 될 수 있다.

올바른 방식:

```sql
WHERE comm IS NOT NULL
```

---

<a id="sql-03-section-36"></a>

## 33. `<> NULL`도 같은 문제

```sql
WHERE comm <> NULL
```

대신:

```sql
WHERE comm IS NOT NULL
```

---

<a id="sql-03-section-37"></a>

## 34. `NOT (comm IS NULL)`

다음도 의미상 가능하다.

```sql
WHERE NOT (
    comm IS NULL
)
```

하지만 더 직접적인 표현은:

```sql
WHERE comm IS NOT NULL
```

이다.

---

<a id="sql-03-section-38"></a>

## 35. `NULL`이 포함된 산술

01번에서 본 예:

```sql
SELECT
    sal,
    comm,
    sal + comm
FROM emp;
```

`COMM`이 `NULL`이면 Result도 `NULL`이 된다.

---

<a id="sql-03-section-39"></a>

## 36. `NULL`이 포함된 비교

```sql
SELECT *
FROM emp
WHERE comm > 100;
```

`COMM`이 `NULL`인 Row는 이 조건을 True로 만들 수 없다.

결과적으로 Filtering된다.

---

<a id="sql-03-section-40"></a>

## 37. WHERE에서 Unknown

`WHERE`는 조건이 **True인 Row만** Result에 포함한다.

```text
True
→ 포함

False
→ 제외

Unknown
→ 제외
```

그래서 `comm = NULL` 같은 조건은 원하는 Row를 찾지 못한다.

---

<a id="sql-03-section-41"></a>

## 38. `NOT IN`과 `NULL`

02번에서 예고한 중요한 주의사항이다.

```sql
SELECT *
FROM emp
WHERE deptno NOT IN (20, 30, NULL);
```

이 Query는 단순히 “20, 30, NULL이 아닌 값”이라고 생각하면 안 된다.

---

<a id="sql-03-section-42"></a>

## 39. `NOT IN`의 개념적 전개

```sql
deptno NOT IN (20, 30)
```

은 개념적으로 다음 조건과 유사하게 이해할 수 있다.

```sql
deptno <> 20
AND deptno <> 30
```

하지만 목록에 `NULL`이 추가되면:

```sql
deptno <> NULL
```

이 비교가 Unknown이 된다.

---

<a id="sql-03-section-43"></a>

## 40. `NOT IN (..., NULL)`의 문제

```text
True
AND
True
AND
Unknown

→ Unknown
```

WHERE에서는 Unknown Row가 Result에서 제외된다.

따라서 `NOT IN`의 목록에 `NULL`이 들어가면 예상보다 Result가 크게 줄거나 0건이 될 수 있다.

---

<a id="sql-03-section-44"></a>

## 41. Subquery의 `NOT IN`도 주의

추후 Subquery 단원에서 다음 형태를 만나게 된다.

```sql
WHERE deptno NOT IN (
    SELECT deptno
    FROM some_table
)
```

Subquery Result에 `NULL`이 포함될 가능성이 있으면 의도와 다른 결과가 나올 수 있다.

그때는 Data 조건을 확인하거나 `NOT EXISTS` 같은 대안을 검토할 수 있다.

---

<a id="sql-03-section-45"></a>

## 42. `LIKE`와 `NULL`

`NULL`은 문자열이 아니므로 Pattern Matching 결과도 Unknown이 될 수 있다.

```sql
SELECT *
FROM emp
WHERE comm LIKE '%0%';
```

`COMM`은 숫자 Column이기도 하고, `NULL` Row에 대해서는 정상 문자열 Pattern 의미로 생각하면 안 된다.

`LIKE`는 문자열 Pattern 검색 목적에 맞는 Column에 사용한다.

---

<a id="sql-03-section-46"></a>

## 43. 내 코드와 강사님 코드 비교

두 원본은 `LIKE`, Wildcard, `NULL` 조건을 비슷한 순서로 학습한다.

```text
LIKE
→ %
→ _
→ Pattern 문제
→ NULL 비교
→ IS NULL
→ IS NOT NULL
```

내 코드는 설명 Comment가 더 많고, 강사님 코드는 Query 중심이다.

---

### 43.1 `%` 설명

내 코드에는 `%`를 “몇 글자든 가능”하다고 설명하는 Comment가 있다.

핵심적으로 맞다.

V2에서는 더 정확하게:

```text
%
→ 0 Character 이상
```

으로 정리한다.

---

### 43.2 `_` 설명

두 코드 모두 `_` Pattern을 실습한다.

V2에서는:

```text
_
→ 정확히 1 Character
```

로 명확히 정리한다.

---

### 43.3 Starts With Pattern

두 코드 모두:

```sql
WHERE ename LIKE 'S%'
```

형태를 사용한다.

---

### 43.4 Contains Pattern

원본에는 `%A%` 형태의 Query가 있다.

```sql
WHERE ename LIKE '%A%'
```

V2에서는 Contains 검색과 Leading Wildcard 성능 가능성까지 추가 설명한다.

---

### 43.5 Position Pattern

두 코드 모두 `_`를 사용한 위치 조건을 실습한다.

예:

```sql
WHERE ename LIKE '_A%'
```

Pattern의 Character 위치를 이해하는 핵심 예제다.

---

### 43.6 `NULL = NULL`

원본에서는 `NULL` 비교가 일반 값 비교와 다르다는 흐름을 학습한다.

V2에서는 SQL의 `Unknown` 개념까지 연결한다.

---

### 43.7 `IS NULL`

두 코드 모두 `COMM`이 없는 Row를 찾을 때 다음 형태를 사용한다.

```sql
WHERE comm IS NULL
```

올바른 방식이다.

---

### 43.8 `IS NOT NULL`

두 코드 모두:

```sql
WHERE comm IS NOT NULL
```

형태를 사용한다.

---

### 43.9 `NULL` 설명 보완

원본에서는 `NULL`을 “값 없음” 중심으로 설명한다.

V2에서는 다음을 분리한다.

```text
0
→ 숫자 값

''
→ 빈 문자열 값

NULL
→ 값 없음 / 알 수 없음
```

---

### 43.10 문자열 대/소문자

02번과 동일하게 `LIKE`도 Collation 영향을 받을 수 있다.

원본 설명에서 단순 Case Sensitive로 단정하는 부분이 있다면 V2에서는 Collation 기준으로 정리한다.

---

### 43.11 원본 비교 요약

| 항목 | 내 코드 | 강사님 코드 | V2 정리 |
| --- | --- | --- | --- |
| LIKE | 설명 상세 | Query 중심 | Pattern Matching |
| `%` | 여러 글자 | 동일 흐름 | 0개 이상 Character |
| `_` | 한 글자 | 동일 흐름 | 정확히 1 Character |
| Prefix 검색 | 있음 | 있음 | `'S%'` |
| Contains 검색 | 있음 | 있음 | `'%A%'` |
| 대/소문자 | 단정 표현 가능 | 별도 설명 적음 | Collation에 따라 결정 |
| `= NULL` | 비교 흐름 있음 | 비교 흐름 있음 | Unknown 발생 |
| `IS NULL` | 있음 | 있음 | NULL 여부 확인 |
| `IS NOT NULL` | 있음 | 있음 | 값 존재 여부 확인 |
| 0 vs NULL | 일부 설명 | 일부 설명 | 완전히 다른 값 |
| NOT IN + NULL | 상세 설명 없음 | 상세 설명 없음 | V2에서 중요 주의사항 추가 |

---

<a id="sql-03-section-47"></a>

## 44. 개선된 통합 예제

```sql
-- S로 시작하는 이름
SELECT
    empno,
    ename
FROM emp
WHERE ename LIKE 'S%';

-- 이름에 A 포함
SELECT
    empno,
    ename
FROM emp
WHERE ename LIKE '%A%';

-- 두 번째 Character가 A
SELECT
    empno,
    ename
FROM emp
WHERE ename LIKE '_A%';

-- S로 시작하지 않는 이름
SELECT
    empno,
    ename
FROM emp
WHERE ename NOT LIKE 'S%';

-- Commission이 없는 사원
SELECT
    empno,
    ename,
    comm
FROM emp
WHERE comm IS NULL;

-- Commission 값이 있는 사원
SELECT
    empno,
    ename,
    comm
FROM emp
WHERE comm IS NOT NULL;
```

---

<a id="sql-03-section-48"></a>

## 45. 실무 Pattern 검색 기준

```text
정확히 같은 값
→ =

특정 Prefix
→ LIKE 'ABC%'

특정 Suffix
→ LIKE '%ABC'

포함 검색
→ LIKE '%ABC%'

정확한 위치
→ _ 활용
```

---

<a id="sql-03-section-49"></a>

## 46. LIKE 성능 주의

다음 Pattern은 실행계획 관점에서 차이가 날 수 있다.

```sql
WHERE name LIKE 'ABC%'
```

```sql
WHERE name LIKE '%ABC%'
```

Prefix가 고정된 첫 Query가 Index 활용에 더 유리할 가능성이 있다.

실제 성능 판단은:

```sql
EXPLAIN
SELECT ...
```

으로 확인한다.

---

<a id="sql-03-section-50"></a>

## 47. NULL 조건 실무 기준

```text
NULL 찾기
→ IS NULL

NULL 아닌 값
→ IS NOT NULL

NULL을 0으로 계산해야 함
→ IFNULL / COALESCE 검토

NULL과 직접 = 비교
→ 사용하지 않음
```

---

<a id="sql-03-section-51"></a>

## 48. 자주 하는 실수

### 48.1 `%`가 최소 1글자라고 생각

0글자도 가능하다.

### 48.2 `_`가 여러 글자를 의미한다고 생각

정확히 한 Character다.

### 48.3 정확히 같은 값 검색에도 항상 LIKE 사용

`=`이 더 명확한 경우가 많다.

### 48.4 `LIKE`는 무조건 대/소문자를 구분한다고 생각

Collation을 확인한다.

### 48.5 `NULL = NULL`이 True라고 생각

Result는 Unknown이다.

### 48.6 `comm = NULL`

`IS NULL`을 사용한다.

### 48.7 `comm != NULL`

`IS NOT NULL`을 사용한다.

### 48.8 `NULL`을 0과 같은 값으로 생각

둘은 완전히 다르다.

### 48.9 `NOT IN` 목록에 `NULL`이 있어도 문제없다고 생각

Unknown 때문에 Result가 예상과 달라질 수 있다.

---

<a id="sql-03-section-52"></a>

## 49. Debugging

LIKE나 NULL 조건 결과가 예상과 다르면 확인한다.

```text
1. Pattern 앞뒤의 % 위치가 맞는가?
2. _ 개수가 원하는 Character 위치와 맞는가?
3. 문자열 Case Sensitivity와 Collation을 확인했는가?
4. 정확 일치라면 LIKE보다 =이 적절하지 않은가?
5. Column 값에 NULL이 존재하는가?
6. = NULL을 사용하지 않았는가?
7. IS NULL / IS NOT NULL을 사용했는가?
8. NOT IN 목록 또는 Subquery 결과에 NULL이 있는가?
```

---

<a id="sql-03-section-53"></a>

## 50. 종합실습

### 문제 1

이름이 `S`로 시작하는 사원의 이름을 조회하시오.

---

### 문제 2

이름에 `A`가 포함된 사원을 조회하시오.

---

### 문제 3

두 번째 Character가 `A`인 이름을 조회하시오.

---

### 문제 4

이름이 `S`로 시작하지 않는 사원을 조회하시오.

---

### 문제 5

Commission 값이 없는 사원의 이름과 `COMM`을 조회하시오.

---

### 문제 6

Commission 값이 존재하는 사원을 조회하시오.

---

### 문제 7

`COMM = NULL` Query가 왜 원하는 결과를 만들지 못하는지 설명하시오.

---

### 문제 8

다음 조건의 차이를 설명하시오.

```sql
ENAME LIKE 'S%'
```

```sql
ENAME LIKE 'S____'
```

---

### 문제 9

`NOT IN (10, 20, NULL)`이 위험한 이유를 설명하시오.

---

<a id="sql-03-section-54"></a>

## 51. 정답과 해설

### 문제 1

```sql
SELECT
    ename
FROM emp
WHERE ename LIKE 'S%';
```

---

### 문제 2

```sql
SELECT *
FROM emp
WHERE ename LIKE '%A%';
```

---

### 문제 3

```sql
SELECT *
FROM emp
WHERE ename LIKE '_A%';
```

---

### 문제 4

```sql
SELECT *
FROM emp
WHERE ename NOT LIKE 'S%';
```

---

### 문제 5

```sql
SELECT
    ename,
    comm
FROM emp
WHERE comm IS NULL;
```

---

### 문제 6

```sql
SELECT *
FROM emp
WHERE comm IS NOT NULL;
```

---

### 문제 7

`NULL`은 일반 값이 아니라 알 수 없는 상태다.

```sql
comm = NULL
```

은 True/False가 아니라 Unknown이 될 수 있다.

따라서:

```sql
comm IS NULL
```

을 사용한다.

---

### 문제 8

```sql
ENAME LIKE 'S%'
```

```text
S로 시작
→ 길이 제한 없음
```

```sql
ENAME LIKE 'S____'
```

```text
S로 시작
→ 뒤에 정확히 4 Character
→ 총 5 Character
```

---

### 문제 9

`NOT IN`은 내부적으로 여러 “같지 않다” 비교로 이해할 수 있다.

`NULL`과의 비교는 Unknown이 되므로 전체 조건이 Unknown이 되어 WHERE에서 제외될 수 있다.

---

<a id="sql-03-section-55"></a>

## 52. 최종 체크리스트

- [ ] `LIKE`가 문자열 Pattern Matching에 사용된다는 점을 설명할 수 있는가?
- [ ] `%`가 0 Character 이상을 의미한다는 점을 이해하는가?
- [ ] `_`가 정확히 1 Character를 의미한다는 점을 이해하는가?
- [ ] Prefix 검색을 작성할 수 있는가?
- [ ] Suffix 검색을 작성할 수 있는가?
- [ ] Contains 검색을 작성할 수 있는가?
- [ ] 특정 Character 위치 검색을 `_`로 작성할 수 있는가?
- [ ] `NOT LIKE`를 사용할 수 있는가?
- [ ] 정확 일치 검색에서 `=`과 `LIKE`의 차이를 이해하는가?
- [ ] `LIKE`의 Case Sensitivity가 Collation에 영향을 받을 수 있음을 아는가?
- [ ] `NULL`과 0이 다르다는 점을 설명할 수 있는가?
- [ ] `NULL`과 빈 문자열이 다르다는 점을 설명할 수 있는가?
- [ ] `NULL = NULL`이 True가 아니라는 점을 이해하는가?
- [ ] WHERE가 True인 Row만 반환한다는 점을 이해하는가?
- [ ] `IS NULL`을 사용할 수 있는가?
- [ ] `IS NOT NULL`을 사용할 수 있는가?
- [ ] `= NULL`, `!= NULL`, `<> NULL`을 피해야 함을 아는가?
- [ ] `NULL`이 포함된 산술 결과를 설명할 수 있는가?
- [ ] `NOT IN` 목록에 NULL이 섞이면 위험할 수 있음을 이해하는가?
- [ ] LIKE 결과가 이상할 때 Pattern·Collation·NULL을 점검할 수 있는가?

---

<a id="sql-03-section-56"></a>

## 53. 핵심 요약

```text
LIKE
→ 문자열 Pattern Matching
```

```text
%
→ 0 Character 이상

_
→ 정확히 1 Character
```

```text
'S%'
→ S로 시작

'%S'
→ S로 끝남

'%S%'
→ S 포함

'_A%'
→ 두 번째 Character가 A
```

```text
NULL
→ 0이 아님
→ 빈 문자열이 아님
→ 값 없음 / 알 수 없음
```

```text
comm = NULL
→ 사용하지 않음

comm IS NULL
→ NULL 확인

comm IS NOT NULL
→ 값 존재 확인
```

```text
WHERE
→ True만 Result에 포함

False
→ 제외

Unknown
→ 제외
```

```text
NOT IN (..., NULL)
→ Unknown 발생 가능
→ 예상과 다른 Result 주의
```

---

<a id="sql-03-section-57"></a>

## 마무리

`LIKE`와 `NULL`은 SQL 초반에 자주 혼동되는 영역이다.

```text
문자열 검색은 Pattern을 정확히 읽고
    ↓
%와 _의 길이 의미를 구분하고
    ↓
정확 일치와 Pattern 검색을 구분하고
    ↓
NULL을 일반 값처럼 비교하지 않고
    ↓
IS NULL / IS NOT NULL을 사용하는 것
```

이 기준을 이해하면 다음 단계의 `ORDER BY`, `LIMIT`, Function, Aggregate Query에서도 조건 결과를 훨씬 정확하게 해석할 수 있다.
<a id="sql-03-section-58"></a>

## V3 동작 백과 — Pattern과 Unknown은 어떻게 평가되는가?

> 입력 범위 확인: 이 복습 부분의 작은 표는 처리 원리를 위한 가정·발췌이며 전체 초기화 EMP의 입력 전체가 아니다. FROM emp를 그대로 실행하면 모든 대상 사원을 처리한다. 수치는 작은 가정 입력의 결과인지 전체 14행 결과인지 구분한다. 실행·시간순 설명은 논리적 설명이며 물리적 평가 순서를 보장하지 않는다.

### LIKE가 필요한 이유

사용자가 이름 전체를 정확히 모르는 검색, 접두어·접미어·포함 검색을 처리한다.

```sql
SELECT ename
FROM emp
WHERE ename LIKE 'S%';
```

```text
'S%' Pattern
→ 첫 Character는 S
→ 뒤에는 0글자 이상 허용

SMITH → True
SCOTT → True
ALLEN → False
```

`_`는 정확히 한 글자다.

```text
'_A%'
→ 첫 글자는 무엇이든 한 글자
→ 두 번째 글자는 A
→ 그 뒤는 0글자 이상
```

### NULL은 왜 비교연산자로 찾지 못하는가?

```sql
WHERE comm = NULL
```

```text
COMM 값과 “알 수 없는 값” 비교
→ True 또는 False를 결정할 수 없음
→ Unknown
→ WHERE는 True만 남기므로 Row 제외
```

따라서 상태를 검사한다.

```sql
WHERE comm IS NULL;
```

### NOT IN과 NULL 실제 결과

```sql
WHERE deptno NOT IN (10, NULL)
```

개념적으로:

```text
deptno <> 10 AND deptno <> NULL
→ 두 번째 비교가 Unknown
→ 전체가 True가 되지 못함
→ 예상과 달리 Row가 나오지 않을 수 있음
```

Subquery의 `NOT IN`을 사용할 때도 반환값에 `NULL`이 있는지 확인한다.

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 검색 Anchor | 강사님 코드 검색 Anchor |
| --- | --- | --- |
| Prefix LIKE | `ename like 'S%` | 같은 Query |
| `%`, `_` | `like` Pattern 연습 | LIKE 구간 |
| NULL 조회 | `is null` | `is null` |
| NULL 제외 | `is not null` | 같은 Query |
| 잘못된 비교 | `= null` | NULL 비교 구간 |

Result가 0행이면 “Data가 없음”으로 단정하지 말고 Pattern, Collation과 Unknown 평가를 확인한다.

