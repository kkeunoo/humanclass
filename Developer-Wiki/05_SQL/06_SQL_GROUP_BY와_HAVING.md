# SQL GROUP BY와 HAVING

> **V2 Final** · MariaDB · EMP 실습 기준  
> 선수 학습: `05_SQL_집계함수.md`

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `06_SQL_GROUP_BY와_HAVING.md` |
| 핵심 | `GROUP BY`, 다중 Grouping, `HAVING`, `WHERE` vs `HAVING` |
| 연결 | `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, `ORDER BY`, `LIMIT` |
| 주의 | `ONLY_FULL_GROUP_BY`, `NULL` Group, Query 논리 처리 순서 |

## 학습 목표

- 전체 집계와 Group별 집계를 구분한다.
- 부서별·직무별 집계를 작성한다.
- 다중 `GROUP BY`를 이해한다.
- `WHERE`와 `HAVING`의 역할을 구분한다.
- Grouping 결과를 정렬하고 제한한다.

---

# 1. GROUP BY란?

같은 값을 가진 Row를 하나의 Group으로 묶는다.

```sql
SELECT deptno
FROM emp
GROUP BY deptno;
```

```text
EMP 전체
→ DEPTNO가 같은 Row끼리 묶음
→ 부서별 Group 생성
```

# 2. 전체 집계와 Group 집계

```sql
-- 전체 평균
SELECT AVG(sal)
FROM emp;

-- 부서별 평균
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno;
```

`GROUP BY`가 없으면 전체가 하나의 집계 대상이고, 있으면 Group마다 집계 결과가 만들어진다.

# 3. 부서별 사원 수

```sql
SELECT
    deptno,
    COUNT(*) AS employee_count
FROM emp
GROUP BY deptno;
```

# 4. 부서별 급여 합계

```sql
SELECT
    deptno,
    SUM(sal) AS total_sal
FROM emp
GROUP BY deptno;
```

# 5. 부서별 평균 급여

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno;
```

# 6. 부서별 최고·최저 급여

```sql
SELECT
    deptno,
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal
FROM emp
GROUP BY deptno;
```

# 7. 여러 Aggregate 함께 사용

```sql
SELECT
    deptno,
    COUNT(*) AS employee_count,
    SUM(sal) AS total_sal,
    AVG(sal) AS avg_sal,
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal
FROM emp
GROUP BY deptno;
```

# 8. 직무별 Grouping

```sql
SELECT
    job,
    COUNT(*) AS employee_count,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY job;
```

Grouping 기준은 요구사항에 따라 달라진다.

# 9. SELECT Column과 GROUP BY

기본적으로 Grouping Query의 SELECT List는 다음처럼 생각한다.

```text
GROUP BY 기준 Column
+
Aggregate Function 결과
```

```sql
SELECT
    deptno,
    AVG(sal)
FROM emp
GROUP BY deptno;
```

# 10. 잘못된 Grouping 예제

```sql
SELECT
    ename,
    deptno,
    AVG(sal)
FROM emp
GROUP BY deptno;
```

한 부서에는 여러 `ENAME`이 있으므로 어느 이름을 Result에 표시해야 하는지 논리적으로 불명확하다.

# 11. ONLY_FULL_GROUP_BY

```sql
SELECT @@sql_mode;
```

`ONLY_FULL_GROUP_BY`가 활성화된 환경에서는 Grouping 의미가 불명확한 일반 Column 사용이 제한될 수 있다.

> Error가 나지 않는다고 논리적으로 좋은 Query라는 뜻은 아니다.

# 12. 다중 GROUP BY

```sql
SELECT
    deptno,
    job,
    COUNT(*) AS employee_count
FROM emp
GROUP BY
    deptno,
    job;
```

# 13. 다중 Grouping 해석

```text
DEPTNO + JOB
→ 하나의 복합 Group Key
```

예를 들어 `20 + CLERK`, `20 + ANALYST`, `30 + CLERK`는 각각 다른 Group이다.

# 14. 다중 Grouping 평균

```sql
SELECT
    deptno,
    job,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY
    deptno,
    job;
```

# 15. GROUP BY와 NULL

Grouping Column에 여러 `NULL`이 있으면 Grouping에서는 하나의 Group으로 취급될 수 있다.

```sql
SELECT
    comm,
    COUNT(*)
FROM emp
GROUP BY comm;
```

이는 일반 비교의 `NULL = NULL → UNKNOWN`과 문맥이 다르다.

# 16. WHERE + GROUP BY

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
WHERE sal >= 1500
GROUP BY deptno;
```

`WHERE`로 Row를 먼저 제한한 뒤 남은 Row를 Grouping한다.

# 17. WHERE의 역할

```text
EMP
→ WHERE
→ 개별 Row Filtering
→ GROUP BY
→ Group 생성
→ Aggregate
```

# 18. HAVING이란?

`HAVING`은 Group 또는 Aggregate 결과를 Filtering한다.

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
HAVING AVG(sal) >= 2000;
```

# 19. WHERE와 HAVING

```text
WHERE
→ GROUP BY 전
→ Row Filtering

HAVING
→ GROUP BY 후
→ Group Filtering
```

# 20. WHERE에 Aggregate를 쓰는 오류

```sql
SELECT
    deptno,
    AVG(sal)
FROM emp
WHERE AVG(sal) >= 2000
GROUP BY deptno;
```

`WHERE` 단계에서는 아직 부서별 `AVG(sal)`이 만들어지지 않았다.

# 21. Aggregate 조건은 HAVING

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
HAVING AVG(sal) >= 2000;
```

# 22. COUNT 조건

사원이 4명 이상인 부서:

```sql
SELECT
    deptno,
    COUNT(*) AS employee_count
FROM emp
GROUP BY deptno
HAVING COUNT(*) >= 4;
```

# 23. SUM 조건

```sql
SELECT
    deptno,
    SUM(sal) AS total_sal
FROM emp
GROUP BY deptno
HAVING SUM(sal) >= 9000;
```

# 24. MAX 조건

```sql
SELECT
    deptno,
    MAX(sal) AS max_sal
FROM emp
GROUP BY deptno
HAVING MAX(sal) >= 3000;
```

# 25. WHERE와 HAVING 함께 사용

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
WHERE job <> 'CLERK'
GROUP BY deptno
HAVING AVG(sal) >= 2000;
```

# 26. 처리 흐름

```text
WHERE job <> 'CLERK'
→ Row Filtering

GROUP BY deptno
→ Group 생성

AVG(sal)
→ Group별 집계

HAVING AVG(sal) >= 2000
→ Group Filtering
```

# 27. WHERE로 가능한 조건

다음은 가능할 수 있다.

```sql
SELECT
    deptno,
    COUNT(*)
FROM emp
GROUP BY deptno
HAVING deptno = 20;
```

하지만 Grouping 전에 제거할 수 있는 Row 조건이라면 다음이 의도를 더 명확히 표현한다.

```sql
SELECT
    deptno,
    COUNT(*)
FROM emp
WHERE deptno = 20
GROUP BY deptno;
```

# 28. HAVING과 GROUP BY

`HAVING`은 Grouping Query에서 주로 사용하지만 Aggregate 전체 결과를 조건으로 검사할 때 명시적 `GROUP BY` 없이 사용할 수도 있다.

```sql
SELECT AVG(sal) AS avg_sal
FROM emp
HAVING AVG(sal) >= 2000;
```

초기 학습 기준은 `WHERE = Row`, `HAVING = Aggregate/Group`으로 잡는다.

# 29. GROUP BY + ORDER BY

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
ORDER BY avg_sal DESC;
```

# 30. Aggregate Alias로 정렬

```sql
SELECT
    deptno,
    COUNT(*) AS employee_count
FROM emp
GROUP BY deptno
ORDER BY employee_count DESC;
```

# 31. GROUP BY는 정렬이 아니다

```text
GROUP BY
→ Group 생성

ORDER BY
→ Result 순서 결정
```

Grouping Column 순으로 보이더라도 필요한 순서는 `ORDER BY`로 명시한다.

# 32. GROUP BY + HAVING + ORDER BY

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
HAVING AVG(sal) >= 1500
ORDER BY avg_sal DESC;
```

# 33. GROUP BY + LIMIT

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
ORDER BY avg_sal DESC
LIMIT 1;
```

평균 급여가 가장 높은 Group 한 개를 가져온다. 공동 1위를 모두 찾는 요구사항이라면 `LIMIT 1`만으로 충분하지 않다.

# 34. 논리적 Query 처리 순서

```text
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
ORDER BY
↓
LIMIT
```

학습을 위한 **논리적 처리 개념**이며 Optimizer의 실제 물리 실행 순서와 동일하다는 뜻은 아니다.

# 35. 작성 순서와 논리 순서

작성:

```text
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

논리:

```text
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

# 36. Alias와 HAVING

MariaDB에서는 SELECT Alias를 `HAVING`에서 사용할 수 있는 경우가 있다.

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
HAVING avg_sal >= 2000;
```

이식성과 명확성을 고려해 `HAVING AVG(sal) >= 2000`처럼 직접 표현하는 스타일도 사용한다.

# 37. COUNT(column)과 GROUP BY

```sql
SELECT
    deptno,
    COUNT(comm) AS commission_count
FROM emp
GROUP BY deptno;
```

각 Group 안에서도 `COUNT(comm)`은 `COMM IS NULL`인 Row를 제외한다.

# 38. DISTINCT와 Grouping

```sql
SELECT
    deptno,
    COUNT(DISTINCT job) AS job_type_count
FROM emp
GROUP BY deptno;
```

부서별 서로 다른 직무 종류 수를 계산한다.

# 39. Group별 급여 차이

```sql
SELECT
    deptno,
    MAX(sal) - MIN(sal) AS sal_diff
FROM emp
GROUP BY deptno;
```

05번의 Aggregate Expression을 Group별로 확장한 형태다.

# 40. 요구사항 분해법

```text
어떤 Row?
→ WHERE

무엇을 기준으로 묶음?
→ GROUP BY

무엇을 계산?
→ Aggregate

어떤 Group만?
→ HAVING

어떤 순서?
→ ORDER BY

몇 개?
→ LIMIT
```

# 41. 내 코드와 강사님 코드 비교

원본의 핵심 흐름은 다음과 같이 정리할 수 있다.

```text
GROUP BY
→ 집계함수 결합
→ 다중 Grouping
→ HAVING
→ WHERE와 HAVING 비교
→ ORDER BY 결합
```

내 코드는 결과 해석과 Comment가 더 상세하고, 강사님 코드는 대표 문법과 Query 중심이다.

V2에서는 `ONLY_FULL_GROUP_BY`, `NULL` Group, 논리적 Query 처리 순서와 Grouping/Sorting의 역할 차이까지 보완했다.

| 항목 | 내 코드 | 강사님 코드 | V2 정리 |
| --- | --- | --- | --- |
| GROUP BY | 실습·Comment | 기본 문법 | Group별 집계 |
| Aggregate | 있음 | 있음 | 05번과 연결 |
| 다중 Grouping | 있음 | 있음 | 복합 Group Key |
| HAVING | 있음 | 있음 | Group Filtering |
| WHERE 비교 | 설명 있음 | 대표 Query | Row vs Group |
| ORDER BY | 결합 실습 | 기본 결합 | Group과 정렬 분리 |
| NULL Group | 제한적 | 제한적 | V2 보완 |
| SQL Mode | 제한적 | 제한적 | `ONLY_FULL_GROUP_BY` |
| 처리 순서 | Comment 중심 | 문법 중심 | 논리적 순서 명시 |

# 42. 개선된 통합 예제

```sql
-- 부서별 급여 요약
SELECT
    deptno,
    COUNT(*) AS employee_count,
    SUM(sal) AS total_sal,
    AVG(sal) AS avg_sal,
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal
FROM emp
GROUP BY deptno
ORDER BY deptno ASC;

-- 부서 + 직무별 평균
SELECT
    deptno,
    job,
    COUNT(*) AS employee_count,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY
    deptno,
    job
ORDER BY
    deptno,
    job;

-- CLERK 제외 후 평균 2000 이상인 부서
SELECT
    deptno,
    COUNT(*) AS employee_count,
    AVG(sal) AS avg_sal
FROM emp
WHERE job <> 'CLERK'
GROUP BY deptno
HAVING AVG(sal) >= 2000
ORDER BY avg_sal DESC;
```

# 43. 실무 Grouping 기준

```text
1. 대상 Row 결정
2. Group Key 결정
3. Aggregate 결정
4. Row 조건은 WHERE
5. Group 조건은 HAVING
6. 순서는 ORDER BY
7. 개수 제한은 LIMIT
```

# 44. 요구사항을 Query로 변환

요구사항:

```text
CLERK를 제외하고
부서별 평균 급여를 계산한 뒤
평균이 2000 이상인 부서만
평균 급여가 높은 순으로 조회
```

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
WHERE job <> 'CLERK'
GROUP BY deptno
HAVING AVG(sal) >= 2000
ORDER BY avg_sal DESC;
```

# 45. GROUP BY 리팩토링

## Before

```sql
SELECT
    deptno,
    ename,
    AVG(sal)
FROM emp
GROUP BY deptno;
```

## After

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno;
```

Group을 대표하지 못하는 일반 Column을 제거한다.

# 46. WHERE / HAVING 리팩토링

## Before

```sql
SELECT deptno, COUNT(*)
FROM emp
GROUP BY deptno
HAVING deptno = 20;
```

## After

```sql
SELECT deptno, COUNT(*)
FROM emp
WHERE deptno = 20
GROUP BY deptno;
```

Grouping 전에 Filtering 가능한 Row 조건은 `WHERE`가 더 명확하다.

# 47. 자주 하는 실수

- `GROUP BY`가 자동 정렬한다고 생각한다.
- 일반 Column을 Grouping 의미 없이 SELECT한다.
- Aggregate 조건을 `WHERE`에 작성한다.
- 모든 조건을 `HAVING`에 몰아넣는다.
- 다중 `GROUP BY`를 독립된 Group으로 오해한다.
- `HAVING`은 무조건 명시적 `GROUP BY`와만 사용한다고 생각한다.
- Grouping의 NULL 처리를 일반 `NULL = NULL` 비교와 동일하게 해석한다.

# 48. Debugging

```text
1. GROUP BY 기준이 요구사항과 맞는가?
2. SELECT 일반 Column이 Group Key와 맞는가?
3. COUNT(*)와 COUNT(column)을 혼동하지 않았는가?
4. WHERE에서 필요한 Row를 먼저 제거하지 않았는가?
5. Aggregate 조건을 WHERE에 작성하지 않았는가?
6. HAVING의 Aggregate가 맞는가?
7. 다중 Group Key를 정확히 이해했는가?
8. NULL Group이 존재하는가?
9. ONLY_FULL_GROUP_BY 영향을 받는가?
10. 필요한 순서를 ORDER BY로 지정했는가?
```

# 49. 종합실습

1. 부서별 사원 수를 조회하시오.
2. 직무별 평균 급여를 조회하시오.
3. 부서별 급여 합계, 평균, 최고, 최저를 조회하시오.
4. 부서와 직무별 사원 수를 조회하시오.
5. 사원이 4명 이상인 부서만 조회하시오.
6. 평균 급여가 2000 이상인 직무만 조회하시오.
7. 급여 1500 이상 사원만 대상으로 부서별 평균을 구하시오.
8. `CLERK`를 제외하고 부서별 평균을 구한 뒤 평균 2000 이상만 내림차순 조회하시오.
9. `WHERE AVG(sal) >= 2000`이 잘못된 이유를 설명하시오.

# 50. 정답과 해설

```sql
-- 1
SELECT deptno, COUNT(*) AS employee_count
FROM emp
GROUP BY deptno;

-- 2
SELECT job, AVG(sal) AS avg_sal
FROM emp
GROUP BY job;

-- 3
SELECT
    deptno,
    SUM(sal) AS total_sal,
    AVG(sal) AS avg_sal,
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal
FROM emp
GROUP BY deptno;

-- 4
SELECT deptno, job, COUNT(*) AS employee_count
FROM emp
GROUP BY deptno, job;

-- 5
SELECT deptno, COUNT(*) AS employee_count
FROM emp
GROUP BY deptno
HAVING COUNT(*) >= 4;

-- 6
SELECT job, AVG(sal) AS avg_sal
FROM emp
GROUP BY job
HAVING AVG(sal) >= 2000;

-- 7
SELECT deptno, AVG(sal) AS avg_sal
FROM emp
WHERE sal >= 1500
GROUP BY deptno;

-- 8
SELECT deptno, AVG(sal) AS avg_sal
FROM emp
WHERE job <> 'CLERK'
GROUP BY deptno
HAVING AVG(sal) >= 2000
ORDER BY avg_sal DESC;
```

9번은 `WHERE` 단계에서 아직 Group별 `AVG(sal)`이 만들어지지 않았기 때문이다. Aggregate 결과 조건은 `HAVING`을 사용한다.

# 51. 최종 체크리스트

- [ ] 전체 집계와 Group 집계를 구분하는가?
- [ ] 부서별·직무별 집계를 작성할 수 있는가?
- [ ] 다중 `GROUP BY`를 이해하는가?
- [ ] 일반 Column과 Aggregate의 Grouping 관계를 이해하는가?
- [ ] `ONLY_FULL_GROUP_BY`를 알고 있는가?
- [ ] `WHERE`는 Row 조건임을 이해하는가?
- [ ] `HAVING`은 Group/Aggregate 조건임을 이해하는가?
- [ ] Aggregate 조건에 `HAVING`을 사용할 수 있는가?
- [ ] `WHERE AVG(...)`가 잘못된 이유를 설명할 수 있는가?
- [ ] `WHERE`와 `HAVING`을 함께 사용할 수 있는가?
- [ ] Group 결과를 `ORDER BY`로 정렬할 수 있는가?
- [ ] `GROUP BY`가 정렬을 보장하지 않음을 아는가?
- [ ] NULL Group의 개념을 이해하는가?
- [ ] 논리적 Query 처리 순서를 설명할 수 있는가?
- [ ] 요구사항을 SQL Clause로 단계적으로 변환할 수 있는가?

# 52. 핵심 요약

```text
GROUP BY
→ 같은 값을 가진 Row를 Group으로 묶음

WHERE
→ Grouping 전 Row Filtering

HAVING
→ Grouping 후 Group Filtering

GROUP BY deptno, job
→ DEPTNO + JOB 조합이 Group Key

GROUP BY
→ Group 생성

ORDER BY
→ Result 정렬

LIMIT
→ Result 개수 제한

논리적 흐름
FROM
→ WHERE
→ GROUP BY
→ HAVING
→ SELECT
→ ORDER BY
→ LIMIT
```

# 마무리

`GROUP BY`와 `HAVING`은 다음 흐름으로 이해하면 된다.

```text
대상 Row 결정
→ Group Key 결정
→ Group별 Aggregate 계산
→ HAVING으로 Group 제한
→ ORDER BY로 정렬
→ 필요하면 LIMIT
```

이 구조가 잡히면 복잡한 집계 문제도 단계별로 분해해서 해결할 수 있다.
