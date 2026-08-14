---
title: SQL 정렬과 LIMIT
version: v2.0-final
last_updated: 2026-08-12
status: Completed
---

# SQL 정렬과 LIMIT

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `04_SQL_정렬과_LIMIT.md` |
| 분류 | `05_SQL` |
| 원본 기준 | `workspace_sql/Script.sql`, `workspace_teacher/workspace_sql/Script.sql` |
| DB 기준 자료 | `[DB]학습용_emp 신규-mariadb.sql` |
| DBMS | MariaDB |
| 핵심 범위 | `ORDER BY`, `ASC`, `DESC`, 다중 정렬, Alias 정렬, Column Position 정렬, `LIMIT`, Offset |
| 학습 범위 | Result Set 정렬, 우선순위 정렬, 상위 N개 조회, Paging 기초 |
| 다음 범위 제외 | Aggregate Function, 문자열·숫자·날짜 Function |
| 문서 형식 | SQL Developer-Wiki V2 확정 형식 |

> 이 문서는 `Script.sql`의 `ORDER BY`와 `LIMIT` 학습 구간을 기준으로 Result Set을 정렬하고 필요한 Row 수만 조회하는 방법을 정리한다.  
> 특히 **정렬을 지정하지 않은 SELECT의 Row 순서는 보장되지 않는다**는 점과, `LIMIT`을 Top-N·Paging에 사용할 때 안정적인 `ORDER BY`가 왜 필요한지를 함께 다룬다.

---

# 학습 목표

- `ORDER BY`의 역할을 설명할 수 있다.
- `ASC`와 `DESC`의 차이를 이해할 수 있다.
- 여러 Column을 순서대로 정렬할 수 있다.
- Alias를 기준으로 Result를 정렬할 수 있다.
- Column Position을 이용한 정렬의 장단점을 설명할 수 있다.
- `NULL`이 포함된 Column 정렬 시 DBMS 동작을 고려할 수 있다.
- `LIMIT`으로 조회 Row 수를 제한할 수 있다.
- Offset을 사용해 일정 Row를 건너뛸 수 있다.
- `ORDER BY` 없이 `LIMIT`만 사용하는 것이 안정적인 Top-N Query가 아님을 이해할 수 있다.
- Pagination에서 고유한 Tie-breaker 정렬이 필요한 이유를 설명할 수 있다.

---

# 1. `ORDER BY`란?

`ORDER BY`는 Query Result의 Row 순서를 정렬하는 Clause다.

```sql
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY sal;
```

`SAL`을 기준으로 Result를 정렬한다.

---

# 2. `ORDER BY`의 위치

기본 구조:

```sql
SELECT
    column_list
FROM table_name
WHERE condition
ORDER BY sort_expression;
```

`WHERE`가 있다면 Filtering 후 Result를 정렬한다.

```text
FROM
→ Table 대상 결정

WHERE
→ Row Filtering

SELECT
→ 출력 Expression 결정

ORDER BY
→ 최종 Result 정렬
```

---

# 3. 정렬을 생략한 Result 순서

다음 Query를 실행했을 때:

```sql
SELECT *
FROM emp;
```

현재 화면에 특정 순서로 보인다고 해서 그 순서가 항상 유지된다고 가정하면 안 된다.

```text
ORDER BY 없음
→ Result Row의 표현 순서를 보장하지 않음
```

Primary Key 순서나 Insert 순서처럼 보일 수 있어도, 필요한 순서가 있다면 반드시 `ORDER BY`를 명시한다.

---

# 4. `ASC`

오름차순 정렬이다.

```sql
SELECT
    ename,
    sal
FROM emp
ORDER BY sal ASC;
```

숫자는 작은 값에서 큰 값 순으로 정렬된다.

```text
낮은 급여
    ↓
높은 급여
```

---

# 5. `ASC`는 기본값

다음 두 Query는 같은 정렬 방향이다.

```sql
SELECT *
FROM emp
ORDER BY sal;
```

```sql
SELECT *
FROM emp
ORDER BY sal ASC;
```

정렬 방향을 생략하면 기본적으로 `ASC`다.

---

# 6. `DESC`

내림차순 정렬이다.

```sql
SELECT
    ename,
    sal
FROM emp
ORDER BY sal DESC;
```

```text
높은 급여
    ↓
낮은 급여
```

---

# 7. 문자열 정렬

문자열 Column도 정렬할 수 있다.

```sql
SELECT
    empno,
    ename
FROM emp
ORDER BY ename ASC;
```

문자열의 실제 비교 순서는 Character Set과 Collation의 영향을 받을 수 있다.

---

# 8. 날짜 정렬

`HIREDATE`를 오래된 날짜부터 정렬:

```sql
SELECT
    ename,
    hiredate
FROM emp
ORDER BY hiredate ASC;
```

최근 입사일부터 정렬:

```sql
SELECT
    ename,
    hiredate
FROM emp
ORDER BY hiredate DESC;
```

---

# 9. 여러 Column 정렬

정렬 기준을 여러 개 지정할 수 있다.

```sql
SELECT
    ename,
    deptno,
    sal
FROM emp
ORDER BY
    deptno ASC,
    sal DESC;
```

---

# 10. 다중 정렬의 우선순위

앞에 작성한 Expression이 먼저 적용된다.

```text
1순위
→ DEPTNO ASC

2순위
→ 같은 DEPTNO 안에서 SAL DESC
```

즉 부서별로 묶여 보이고, 같은 부서에서는 급여가 높은 사원이 먼저 나온다.

---

# 11. 정렬 방향은 각각 지정한다

```sql
ORDER BY
    deptno ASC,
    sal DESC;
```

각 정렬 기준은 서로 다른 방향을 가질 수 있다.

---

# 12. 세 가지 기준 정렬

```sql
SELECT
    empno,
    ename,
    deptno,
    sal
FROM emp
ORDER BY
    deptno ASC,
    sal DESC,
    empno ASC;
```

`DEPTNO`와 `SAL`까지 같은 경우 `EMPNO`가 최종 Tie-breaker가 된다.

---

# 13. Tie란?

정렬 기준 값이 같은 Row가 여러 개 있는 상태다.

예:

```text
SAL = 3000
→ SCOTT
→ FORD
```

`ORDER BY sal DESC`만 사용하면 같은 `SAL`끼리의 상대 순서를 별도로 요구하지 않은 것이다.

---

# 14. 안정적인 정렬을 위한 Tie-breaker

순서가 반드시 결정되어야 한다면 고유한 Column을 추가한다.

```sql
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY
    sal DESC,
    empno ASC;
```

```text
1순위
→ SAL DESC

2순위
→ EMPNO ASC
```

---

# 15. SELECT하지 않은 Column으로 정렬

일반적인 Query에서는 출력하지 않은 Column을 정렬 기준으로 사용할 수도 있다.

```sql
SELECT
    ename,
    job
FROM emp
ORDER BY sal DESC;
```

Result에는 `SAL`이 표시되지 않지만 정렬에는 사용된다.

> [!NOTE]
> `DISTINCT`, Grouping 등 Query 형태에 따라 정렬 Expression에 추가 제약이 생길 수 있으므로 복잡한 Query에서는 별도로 확인한다.

---

# 16. Alias로 정렬

```sql
SELECT
    ename,
    sal AS salary
FROM emp
ORDER BY salary DESC;
```

`SELECT`에서 만든 Alias를 `ORDER BY`에서 사용할 수 있다.

---

# 17. 계산식 Alias 정렬

```sql
SELECT
    ename,
    sal * 12 AS sal_x_12
FROM emp
ORDER BY sal_x_12 DESC;
```

긴 Expression을 반복하지 않아도 되어 읽기 쉽다.

---

# 18. Expression으로 직접 정렬

Alias 없이도 가능하다.

```sql
SELECT
    ename,
    sal
FROM emp
ORDER BY sal * 12 DESC;
```

다만 같은 Expression이 `SELECT`에도 있다면 Alias가 더 읽기 좋을 수 있다.

---

# 19. Column Position 정렬

Result의 Column 순번을 사용할 수도 있다.

```sql
SELECT
    ename,
    sal
FROM emp
ORDER BY 2 DESC;
```

`2`는 SELECT List의 두 번째 항목인 `SAL`을 의미한다.

---

# 20. Position 정렬의 단점

다음 Query를 보자.

```sql
SELECT
    ename,
    sal
FROM emp
ORDER BY 2 DESC;
```

나중에 SELECT List 순서를 바꾸면 `2`가 가리키는 의미도 바뀐다.

```text
ORDER BY 2
→ 짧음
→ 하지만 의도가 덜 명확함
→ SELECT List 변경에 취약
```

실무에서는 Column Name이나 Alias를 우선하는 편이 유지보수에 좋다.

---

# 21. `NULL` 정렬

`COMM`처럼 `NULL`이 있는 Column도 정렬할 수 있다.

```sql
SELECT
    ename,
    comm
FROM emp
ORDER BY comm ASC;
```

`NULL`의 기본 정렬 위치는 DBMS와 정렬 방향에 따라 차이가 있을 수 있으므로 다른 DBMS의 동작을 그대로 가정하지 않는다.

---

# 22. MariaDB에서 NULL 위치를 명시적으로 제어

`NULL`을 마지막으로 보내고 싶다면 Boolean Expression을 활용할 수 있다.

```sql
SELECT
    ename,
    comm
FROM emp
ORDER BY
    comm IS NULL,
    comm ASC;
```

해석:

```text
COMM IS NULL
→ 값이 있으면 0
→ NULL이면 1

ASC
→ 값이 있는 Row 먼저
→ NULL Row 나중
```

---

# 23. NULL을 먼저 정렬

```sql
SELECT
    ename,
    comm
FROM emp
ORDER BY
    comm IS NOT NULL,
    comm ASC;
```

업무 요구에 맞춰 NULL 위치를 명시적으로 표현할 수 있다.

---

# 24. `WHERE`와 `ORDER BY`

먼저 조건으로 Row를 제한하고 그 결과를 정렬한다.

```sql
SELECT
    ename,
    job,
    sal
FROM emp
WHERE deptno = 30
ORDER BY sal DESC;
```

```text
DEPTNO = 30
→ Filtering

SAL DESC
→ 남은 Row 정렬
```

---

# 25. `LIKE`와 `ORDER BY`

03번 내용과 연결:

```sql
SELECT
    empno,
    ename
FROM emp
WHERE ename LIKE 'S%'
ORDER BY ename ASC;
```

Pattern으로 찾은 Row를 이름순으로 정렬한다.

---

# 26. `IN`과 `ORDER BY`

```sql
SELECT
    empno,
    ename,
    deptno,
    sal
FROM emp
WHERE deptno IN (10, 20, 30)
ORDER BY
    deptno ASC,
    sal DESC;
```

02번의 Filtering과 이번 정렬을 함께 사용할 수 있다.

---

# 27. `LIMIT`란?

MariaDB에서 Result Row 수를 제한할 때 사용한다.

```sql
SELECT *
FROM emp
LIMIT 5;
```

최대 5개의 Row만 반환한다.

---

# 28. `LIMIT`의 위치

```sql
SELECT
    column_list
FROM table_name
WHERE condition
ORDER BY sort_expression
LIMIT row_count;
```

일반적인 작성 순서에서 `LIMIT`은 뒤쪽에 위치한다.

---

# 29. `LIMIT 1`

```sql
SELECT *
FROM emp
LIMIT 1;
```

한 Row만 반환한다.

하지만 어떤 Row인지 의미 있게 정하려면 `ORDER BY`가 필요하다.

---

# 30. 최고 급여 사원 1명

```sql
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY
    sal DESC,
    empno ASC
LIMIT 1;
```

가장 높은 `SAL`부터 정렬한 뒤 한 Row만 가져온다.

> [!IMPORTANT]
> 최고 급여가 같은 사원이 여러 명이라면 `LIMIT 1`은 그중 한 명만 반환한다. “공동 1위 전부”가 요구사항이라면 다른 Query가 필요하다.

---

# 31. 급여 상위 3개 Row

```sql
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY
    sal DESC,
    empno ASC
LIMIT 3;
```

`ORDER BY`가 먼저 의미 있는 순서를 만든 뒤 `LIMIT 3`으로 앞의 3개 Row를 가져온다.

---

# 32. `LIMIT`만 사용한 Top-N의 문제

```sql
SELECT *
FROM emp
LIMIT 3;
```

이 Query는 “급여 상위 3명”이 아니다.

```text
ORDER BY 없음
→ 원하는 순위 정의 없음

LIMIT 3
→ 단지 Result에서 최대 3 Row
```

---

# 33. Offset

일정 Row를 건너뛴 뒤 조회할 수 있다.

```sql
SELECT
    empno,
    ename
FROM emp
ORDER BY empno
LIMIT 5 OFFSET 5;
```

의미:

```text
앞의 5 Row
→ 건너뜀

그 다음 최대 5 Row
→ 반환
```

---

# 34. MariaDB의 `LIMIT offset, row_count`

MariaDB에서는 다음 형태도 사용할 수 있다.

```sql
SELECT
    empno,
    ename
FROM emp
ORDER BY empno
LIMIT 5, 5;
```

의미:

```text
offset = 5
row_count = 5
```

---

# 35. 두 LIMIT 문법 비교

```sql
LIMIT 5 OFFSET 10
```

과:

```sql
LIMIT 10, 5
```

는 같은 의미다.

주의할 점:

```text
LIMIT row_count OFFSET offset
→ 개수 먼저

LIMIT offset, row_count
→ offset 먼저
```

순서가 다르다.

---

# 36. Paging 기초

페이지당 5개씩 보여 준다고 가정한다.

1 Page:

```sql
SELECT
    empno,
    ename
FROM emp
ORDER BY empno
LIMIT 5 OFFSET 0;
```

2 Page:

```sql
SELECT
    empno,
    ename
FROM emp
ORDER BY empno
LIMIT 5 OFFSET 5;
```

3 Page:

```sql
SELECT
    empno,
    ename
FROM emp
ORDER BY empno
LIMIT 5 OFFSET 10;
```

---

# 37. Offset 계산

```text
offset
=
(page - 1) × pageSize
```

예:

```text
page = 3
pageSize = 5

offset
= (3 - 1) × 5
= 10
```

---

# 38. Pagination과 안정적인 정렬

다음 Query는 Paging 용도로 불안정하다.

```sql
SELECT *
FROM emp
ORDER BY sal DESC
LIMIT 5 OFFSET 5;
```

`SAL`이 같은 Row의 순서가 명확하지 않기 때문이다.

고유한 Tie-breaker를 추가한다.

```sql
SELECT *
FROM emp
ORDER BY
    sal DESC,
    empno ASC
LIMIT 5 OFFSET 5;
```

---

# 39. 큰 Offset의 성능

Offset Pagination은 뒤 페이지로 갈수록 많은 Row를 건너뛰어야 할 수 있다.

```sql
LIMIT 20 OFFSET 100000;
```

Data가 매우 많다면 성능 문제가 될 수 있다.

실무에서는 상황에 따라 마지막으로 본 Key를 기준으로 다음 Page를 조회하는 Keyset Pagination도 검토한다.

---

# 40. Keyset Pagination 개념

예를 들어 `EMPNO`가 증가하는 순서라면:

```sql
SELECT
    empno,
    ename
FROM emp
WHERE empno > 7566
ORDER BY empno ASC
LIMIT 5;
```

```text
OFFSET으로 N개를 건너뛰기
대신
마지막 Key 이후부터 조회
```

현재 수업 범위를 넘어가는 실무 확장 개념으로 이해하면 된다.

---

# 41. 내 코드와 강사님 코드 비교

원본의 핵심 흐름은 다음과 같다.

```text
ORDER BY
→ ASC / DESC
→ 여러 Column 정렬
→ LIMIT
```

내 코드는 실습 Comment와 결과 해석이 더 많고, 강사님 코드는 문법 중심으로 간결하게 진행한다.

V2에서는 두 흐름을 유지하면서 **Result 순서 보장, Tie-breaker, Pagination 안정성**을 추가했다.

---

## 41.1 기본 ORDER BY

원본에서는 급여나 Column 값을 기준으로 정렬하는 예제를 사용한다.

V2 기본형:

```sql
SELECT *
FROM emp
ORDER BY sal;
```

`ASC`가 생략된 오름차순이다.

---

## 41.2 DESC

내림차순은 다음처럼 작성한다.

```sql
SELECT *
FROM emp
ORDER BY sal DESC;
```

급여가 높은 Row부터 확인할 수 있다.

---

## 41.3 다중 정렬

원본의 여러 정렬 기준은 다음 원칙으로 읽는다.

```text
앞 Column
→ 1순위

뒤 Column
→ 앞 값이 같은 Row의 다음 기준
```

V2에서는 다음처럼 Formatting한다.

```sql
ORDER BY
    deptno ASC,
    sal DESC;
```

---

## 41.4 ORDER BY 없는 순서

원본 수업에서는 화면에 출력된 순서를 기준으로 Query를 관찰할 수 있다.

하지만 V2에서는 다음을 명확하게 추가한다.

```text
ORDER BY를 작성하지 않았다면
업무적으로 필요한 Row 순서를 보장한다고 가정하지 않는다.
```

---

## 41.5 LIMIT

원본의 `LIMIT`은 Row 수를 줄이는 기본 문법으로 학습한다.

V2에서는:

```text
LIMIT
→ Result 개수 제한

ORDER BY + LIMIT
→ 의미 있는 Top-N 가능
```

으로 역할을 분리한다.

---

## 41.6 LIMIT과 정렬

다음은 단순 3 Row다.

```sql
SELECT *
FROM emp
LIMIT 3;
```

다음은 급여 기준 상위 3 Row다.

```sql
SELECT *
FROM emp
ORDER BY sal DESC
LIMIT 3;
```

둘의 의미는 완전히 다르다.

---

## 41.7 원본 비교 요약

| 항목 | 내 코드 | 강사님 코드 | V2 정리 |
| --- | --- | --- | --- |
| ORDER BY | 실습·Comment 상세 | 문법 중심 | Result 정렬 |
| ASC | 있음 | 있음 | 기본 정렬 방향 |
| DESC | 있음 | 있음 | 내림차순 |
| 다중 정렬 | 있음 | 있음 | 앞 Expression 우선 |
| Alias 정렬 | 학습 흐름에서 활용 가능 | 기본 예제 중심 | 읽기 좋은 정렬 기준 |
| Position 정렬 | 문법 실험 가능 | 문법 실험 가능 | 가능하지만 유지보수상 비권장 |
| NULL 정렬 | 상세 설명 제한 | 상세 설명 제한 | 명시적 NULL 위치 제어 추가 |
| LIMIT | 있음 | 있음 | Row 개수 제한 |
| OFFSET | 기본 실습 범위 | 기본 실습 범위 | Paging과 연결 |
| 순서 보장 | 상세 설명 제한 | 상세 설명 제한 | ORDER BY 필요 |
| Tie-breaker | 상세 설명 제한 | 상세 설명 제한 | 안정적 순서에 필요 |
| Paging | 기초 | 기초 | 안정적 ORDER BY 강조 |

---

# 42. 개선된 통합 예제

```sql
-- 급여가 높은 순
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY
    sal DESC,
    empno ASC;

-- 부서 오름차순, 같은 부서에서는 급여 내림차순
SELECT
    empno,
    ename,
    deptno,
    sal
FROM emp
ORDER BY
    deptno ASC,
    sal DESC,
    empno ASC;

-- 부서 20 또는 30에서 급여 상위 5 Row
SELECT
    empno,
    ename,
    deptno,
    sal
FROM emp
WHERE deptno IN (20, 30)
ORDER BY
    sal DESC,
    empno ASC
LIMIT 5;

-- 두 번째 Page: 5개씩
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY
    sal DESC,
    empno ASC
LIMIT 5 OFFSET 5;
```

---

# 43. 실무 정렬 기준

```text
1. 필요한 순서가 있다면 ORDER BY를 반드시 명시한다.
2. ASC / DESC를 의도에 맞게 작성한다.
3. 다중 정렬은 우선순위를 앞에서부터 읽는다.
4. 순서가 반드시 고정되어야 하면 Tie-breaker를 추가한다.
5. Column Position보다 Column Name / Alias를 우선한다.
6. NULL 위치가 중요하면 명시적으로 제어한다.
7. LIMIT으로 순위를 만들려면 먼저 ORDER BY를 정의한다.
```

---

# 44. ORDER BY 리팩토링

## Before

```sql
SELECT *
FROM emp
ORDER BY 6 DESC;
```

## After

```sql
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY sal DESC;
```

Column Position보다 이름을 사용하면 Query 의도가 더 명확하다.

---

# 45. Top-N 리팩토링

## Before

```sql
SELECT *
FROM emp
LIMIT 3;
```

## After

```sql
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY
    sal DESC,
    empno ASC
LIMIT 3;
```

“상위 3명”이라는 요구사항에는 정렬 기준이 필요하다.

---

# 46. Paging 리팩토링

## Before

```sql
SELECT *
FROM emp
LIMIT 5 OFFSET 5;
```

## After

```sql
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY empno ASC
LIMIT 5 OFFSET 5;
```

Paging은 Page 간 Row 순서가 안정적이어야 한다.

---

# 47. 자주 하는 실수

## 47.1 SELECT 결과는 항상 PK 순이라고 생각

`ORDER BY`가 없다면 필요한 순서를 보장한다고 가정하지 않는다.

## 47.2 `DESC`를 첫 Column에만 쓰면 뒤 Column에도 적용된다고 생각

각 정렬 Expression의 방향을 따로 읽는다.

## 47.3 다중 정렬의 우선순위를 뒤에서부터 읽음

앞 Expression이 먼저다.

## 47.4 `ORDER BY 2`를 과도하게 사용

SELECT List 변경에 취약하다.

## 47.5 `LIMIT 3`을 “상위 3개”라고 생각

순위 기준인 `ORDER BY`가 먼저 필요하다.

## 47.6 같은 정렬값의 순서를 항상 같다고 생각

Tie-breaker가 없으면 업무적으로 안정된 순서를 기대하지 않는다.

## 47.7 Paging에서 ORDER BY를 생략

Page 이동 시 Row의 일관된 순서를 기대하기 어렵다.

---

# 48. Debugging

정렬이나 LIMIT 결과가 예상과 다르면 확인한다.

```text
1. ORDER BY Column이 맞는가?
2. ASC / DESC 방향이 맞는가?
3. 다중 정렬의 첫 번째 기준이 맞는가?
4. 같은 값이 있을 때 Tie-breaker가 필요한가?
5. NULL의 위치가 요구사항과 맞는가?
6. LIMIT 전에 원하는 ORDER BY가 있는가?
7. OFFSET과 row_count 순서를 혼동하지 않았는가?
8. Pagination의 정렬 기준이 고유하게 결정되는가?
```

---

# 49. 종합실습

## 문제 1

모든 사원을 급여가 낮은 순서로 조회하시오.

---

## 문제 2

모든 사원을 급여가 높은 순서로 조회하시오.

---

## 문제 3

부서 번호는 오름차순, 같은 부서에서는 급여가 높은 순서로 조회하시오.

---

## 문제 4

이름이 `S`로 시작하는 사원을 이름 오름차순으로 조회하시오.

---

## 문제 5

급여가 가장 높은 Row 1개를 조회하시오.

같은 급여일 경우 사원 번호가 작은 Row를 먼저 선택한다.

---

## 문제 6

급여가 높은 순서의 상위 3 Row를 조회하시오.

같은 급여는 사원 번호 오름차순으로 정렬한다.

---

## 문제 7

사원 번호 오름차순으로 정렬한 뒤 처음 5 Row를 건너뛰고 다음 5 Row를 조회하시오.

---

## 문제 8

다음 두 Query의 의미 차이를 설명하시오.

```sql
SELECT *
FROM emp
LIMIT 3;
```

```sql
SELECT *
FROM emp
ORDER BY sal DESC
LIMIT 3;
```

---

# 50. 정답과 해설

## 문제 1

```sql
SELECT *
FROM emp
ORDER BY sal ASC;
```

`ASC`는 생략할 수도 있다.

---

## 문제 2

```sql
SELECT *
FROM emp
ORDER BY sal DESC;
```

---

## 문제 3

```sql
SELECT *
FROM emp
ORDER BY
    deptno ASC,
    sal DESC;
```

먼저 부서를 정렬하고 같은 부서 안에서 급여를 내림차순 정렬한다.

---

## 문제 4

```sql
SELECT
    empno,
    ename
FROM emp
WHERE ename LIKE 'S%'
ORDER BY ename ASC;
```

---

## 문제 5

```sql
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY
    sal DESC,
    empno ASC
LIMIT 1;
```

---

## 문제 6

```sql
SELECT
    empno,
    ename,
    sal
FROM emp
ORDER BY
    sal DESC,
    empno ASC
LIMIT 3;
```

---

## 문제 7

```sql
SELECT
    empno,
    ename
FROM emp
ORDER BY empno ASC
LIMIT 5 OFFSET 5;
```

MariaDB에서는 다음 형태도 가능하다.

```sql
SELECT
    empno,
    ename
FROM emp
ORDER BY empno ASC
LIMIT 5, 5;
```

---

## 문제 8

첫 Query:

```text
정렬 기준 없음
→ Result에서 최대 3 Row
```

두 번째 Query:

```text
SAL DESC로 정렬
→ 급여가 높은 Row부터
→ 최대 3 Row
```

따라서 “급여 상위 3 Row”라는 의미는 두 번째 Query에만 있다.

---

# 51. 최종 체크리스트

- [ ] `ORDER BY`의 역할을 설명할 수 있는가?
- [ ] `ORDER BY`가 없는 Result 순서를 업무적으로 보장된 것으로 가정하지 않는가?
- [ ] `ASC`가 오름차순임을 아는가?
- [ ] `ASC`가 기본값임을 아는가?
- [ ] `DESC`가 내림차순임을 아는가?
- [ ] 문자열과 날짜도 정렬할 수 있는가?
- [ ] 여러 Column을 기준으로 정렬할 수 있는가?
- [ ] 다중 정렬은 앞 Expression이 우선임을 이해하는가?
- [ ] 각 Column마다 ASC / DESC를 지정할 수 있는가?
- [ ] Tie가 무엇인지 설명할 수 있는가?
- [ ] 안정적인 순서가 필요할 때 Tie-breaker를 추가할 수 있는가?
- [ ] Alias로 정렬할 수 있는가?
- [ ] Column Position 정렬의 단점을 이해하는가?
- [ ] NULL 위치가 중요할 때 명시적으로 정렬할 수 있는가?
- [ ] `WHERE`와 `ORDER BY`를 함께 사용할 수 있는가?
- [ ] `LIMIT`으로 Row 수를 제한할 수 있는가?
- [ ] `LIMIT 1`만으로 어떤 Row가 선택될지 의미가 정해지지 않는다는 점을 이해하는가?
- [ ] Top-N Query에 `ORDER BY`가 필요한 이유를 설명할 수 있는가?
- [ ] `LIMIT row_count OFFSET offset`을 사용할 수 있는가?
- [ ] `LIMIT offset, row_count` 문법의 인자 순서를 구분할 수 있는가?
- [ ] Pagination Offset을 계산할 수 있는가?
- [ ] Pagination에 안정적인 정렬이 필요한 이유를 이해하는가?
- [ ] 큰 Offset의 성능 문제 가능성을 알고 있는가?

---

# 52. 핵심 요약

```text
ORDER BY
→ Result Row 정렬
```

```text
ASC
→ 오름차순
→ 기본값

DESC
→ 내림차순
```

```text
ORDER BY
    deptno ASC,
    sal DESC

→ DEPTNO 1순위
→ 같은 부서에서 SAL 2순위
```

```text
ORDER BY 없음
→ 필요한 Result 순서를 보장한다고 가정하지 않음
```

```text
LIMIT 5
→ 최대 5 Row
```

```text
LIMIT 5 OFFSET 10
→ 10 Row 건너뛰고
→ 최대 5 Row
```

```text
Top-N
→ ORDER BY로 순위 기준 정의
→ LIMIT으로 개수 제한
```

```text
Pagination
→ 안정적인 ORDER BY
→ 필요하면 고유 Tie-breaker 추가
```

---

# 마무리

정렬과 `LIMIT`의 핵심은 단순히 Result를 보기 좋게 만드는 데 있지 않다.

```text
원하는 순서를 ORDER BY로 정의하고
    ↓
동점 Row의 순서가 중요하면 Tie-breaker를 추가하고
    ↓
필요한 Row 수를 LIMIT으로 제한하고
    ↓
Paging에서는 같은 정렬 규칙을 계속 유지하는 것
```

이 기준을 이해하면 이후 Aggregate Function에서 “가장 큰 값”, “가장 작은 값”, “상위 결과”를 다룰 때도 Query의 의미를 정확하게 구분할 수 있다.
