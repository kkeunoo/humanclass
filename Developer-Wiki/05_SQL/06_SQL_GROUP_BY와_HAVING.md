# SQL GROUP BY와 HAVING

> **V3 Encyclopedia** · MariaDB · EMP 실습 기준  
> 선수 학습: `05_SQL_집계함수.md`

## 이 문서에서 바로 찾기

- [학습 목표](#sql-06-section-2)
- [개념에서 실제 실행까지 — GROUP BY와 HAVING이란? — 행을 묶은 뒤 그룹을 검사](#sql-06-section-3)
- [41. 내 코드와 강사님 코드 비교](#sql-06-section-44)
- [48. Debugging](#sql-06-section-51)
- [49. 종합실습](#sql-06-section-52)
- [50. 정답과 해설](#sql-06-section-53)
- [51. 최종 체크리스트](#sql-06-section-54)
- [52. 핵심 요약](#sql-06-section-55)

<details>
<summary>상세 목차 전체 펼치기</summary>

- [문서 정보](#sql-06-section-1)
- [학습 목표](#sql-06-section-2)
- [개념에서 실제 실행까지 — GROUP BY와 HAVING이란? — 행을 묶은 뒤 그룹을 검사](#sql-06-section-3)
- [1. GROUP BY란?](#sql-06-section-4)
- [2. 전체 집계와 Group 집계](#sql-06-section-5)
- [3. 부서별 사원 수](#sql-06-section-6)
- [4. 부서별 급여 합계](#sql-06-section-7)
- [5. 부서별 평균 급여](#sql-06-section-8)
- [6. 부서별 최고·최저 급여](#sql-06-section-9)
- [7. 여러 Aggregate 함께 사용](#sql-06-section-10)
- [8. 직무별 Grouping](#sql-06-section-11)
- [9. SELECT Column과 GROUP BY](#sql-06-section-12)
- [10. 잘못된 Grouping 예제](#sql-06-section-13)
- [11. ONLY_FULL_GROUP_BY](#sql-06-section-14)
- [12. 다중 GROUP BY](#sql-06-section-15)
- [13. 다중 Grouping 해석](#sql-06-section-16)
- [14. 다중 Grouping 평균](#sql-06-section-17)
- [15. GROUP BY와 NULL](#sql-06-section-18)
- [16. WHERE + GROUP BY](#sql-06-section-19)
- [17. WHERE의 역할](#sql-06-section-20)
- [18. HAVING이란?](#sql-06-section-21)
- [19. WHERE와 HAVING](#sql-06-section-22)
- [20. WHERE에 Aggregate를 쓰는 오류](#sql-06-section-23)
- [21. Aggregate 조건은 HAVING](#sql-06-section-24)
- [22. COUNT 조건](#sql-06-section-25)
- [23. SUM 조건](#sql-06-section-26)
- [24. MAX 조건](#sql-06-section-27)
- [25. WHERE와 HAVING 함께 사용](#sql-06-section-28)
- [26. 처리 흐름](#sql-06-section-29)
- [27. WHERE로 가능한 조건](#sql-06-section-30)
- [28. HAVING과 GROUP BY](#sql-06-section-31)
- [29. GROUP BY + ORDER BY](#sql-06-section-32)
- [30. Aggregate Alias로 정렬](#sql-06-section-33)
- [31. GROUP BY는 정렬이 아니다](#sql-06-section-34)
- [32. GROUP BY + HAVING + ORDER BY](#sql-06-section-35)
- [33. GROUP BY + LIMIT](#sql-06-section-36)
- [34. 논리적 Query 처리 순서](#sql-06-section-37)
- [35. 작성 순서와 논리 순서](#sql-06-section-38)
- [36. Alias와 HAVING](#sql-06-section-39)
- [37. COUNT(column)과 GROUP BY](#sql-06-section-40)
- [38. DISTINCT와 Grouping](#sql-06-section-41)
- [39. Group별 급여 차이](#sql-06-section-42)
- [40. 요구사항 분해법](#sql-06-section-43)
- [41. 내 코드와 강사님 코드 비교](#sql-06-section-44)
- [42. 개선된 통합 예제](#sql-06-section-45)
- [43. 실무 Grouping 기준](#sql-06-section-46)
- [44. 요구사항을 Query로 변환](#sql-06-section-47)
- [45. GROUP BY 리팩토링](#sql-06-section-48)
- [46. WHERE / HAVING 리팩토링](#sql-06-section-49)
- [47. 자주 하는 실수](#sql-06-section-50)
- [48. Debugging](#sql-06-section-51)
- [49. 종합실습](#sql-06-section-52)
- [50. 정답과 해설](#sql-06-section-53)
- [51. 최종 체크리스트](#sql-06-section-54)
- [52. 핵심 요약](#sql-06-section-55)
- [마무리](#sql-06-section-56)
- [V3 동작 백과 — Row가 Group으로 묶이고 다시 걸러지는 과정](#sql-06-section-57)

</details>

---

<a id="sql-06-section-1"></a>

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `06_SQL_GROUP_BY와_HAVING.md` |
| 핵심 | `GROUP BY`, 다중 Grouping, `HAVING`, `WHERE` vs `HAVING` |
| 연결 | `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`, `ORDER BY`, `LIMIT` |
| 주의 | `ONLY_FULL_GROUP_BY`, `NULL` Group, Query 논리 처리 순서 |

<a id="sql-06-section-2"></a>

## 학습 목표

- 행 필터와 그룹 필터 및 그룹 기준의 의미를 구분한다.
- 실제 입력·중간 상태·결과와 실패 조건을 직접 확인한다.

---

<a id="sql-06-section-3"></a>

## 개념에서 실제 실행까지 — GROUP BY와 HAVING이란? — 행을 묶은 뒤 그룹을 검사

### 무엇이며 왜 배워야 할까?

GROUP BY는 같은 기준 값을 가진 행을 묶어 그룹 단위로 집계한다. 부서별 평균은 부서마다 한 그룹, 부서·직무별 평균은 그 두 값의 조합마다 한 그룹이다. 그룹 기준에 sal을 추가하면 같은 부서·직무라도 급여마다 쪼개지므로 다른 질문이 된다.

WHERE는 집계 전 입력 행을 걸러 내고 HAVING은 집계된 그룹을 걸러 낸다. ‘급여 1000 이상인 사람을 모아 직무별 인원이 3명 이상인 직무’에서는 먼저 급여 조건을 적용해야 한다. 모든 사원을 센 뒤 HAVING만 적용하면 세는 대상이 다르다.

FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY→LIMIT은 이해를 위한 논리적 순서다. 옵티마이저의 실제 실행 방식이 반드시 이 순서의 물리적 반복이라는 뜻은 아니다. MariaDB는 HAVING에서 선택 별칭을 사용할 수 있는 등 이름 해석 규칙도 있으므로 이 순서만으로 모든 별칭 사용을 단정하지 않는다.

### 입력은 어디에서 오는가?

EMP·DEPT·SALGRADE는 초기화 자료 그대로 준비된 상태다. EMP 14행, DEPT 4행, SALGRADE 5행이다. 다른 DML로 데이터를 바꿨다면 아래 결과와 달라질 수 있다. 상수 SELECT 예제는 테이블 없이도 실행할 수 있다.

### 실행 가능한 보충 SQL과 결과

아래는 원본의 개념을 작은 검증 범위로 정리한 보충 예제다. MariaDB 12.3.2, 일반 SQL 모드·InnoDB 기준에서 결과를 확인했다. 조회 SQL은 SQL 편집기의 Result Grid, 변경 SQL은 영향 행 표시와 사후 SELECT로 관찰한다. DBMS·모드·데이터 상태가 다르면 차이를 확인해야 한다.

```sql
SELECT job, COUNT(*) AS employee_count
FROM emp
WHERE sal >= 1000
GROUP BY job
HAVING COUNT(*) >= 3
ORDER BY job;
```

Result Grid의 열·행 값:

```text
job	employee_count
MANAGER	3
SALESMAN	4
```

여러 SELECT가 있으면 위 출력에 결과 헤더가 다시 나타난다. 숫자의 표시 자릿수와 NULL 표시 모양은 클라이언트별로 달라질 수 있지만 값과 행의 의미를 먼저 비교한다.

### 논리적 처리와 상태 변화 — 단계별로 따라가기

1. WHERE sal>=1000에서 SMITH와 JAMES를 제거한다.
2. 남은 행을 job별로 묶는다.
3. CLERK는 2명, SALESMAN은 4명, MANAGER는 3명 등으로 집계한다.
4. HAVING COUNT(*)>=3에서 MANAGER와 SALESMAN만 남기고 job으로 정렬한다.

### 내 코드·강사님 코드의 어느 부분에 있었을까?


#### 내 코드: `workspace_sql/Script.sql` 403~412행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
select
	 avg(sal), deptno, job
from emp
group by deptno, job, sal
having avg(sal) >= 2000;

-- having은 group by에 조건식을 걸 수 있지만 실무에서 주로 사용하진 않음
select
	 avg(sal), deptno, job
from emp
```

#### 강사님 코드: `workspace_teacher/workspace_sql/Script.sql` 367~376행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
    job
FROM emp
GROUP BY deptno, job
HAVING AVG(sal) >= 2000;

SELECT 
    AVG(sal) AS avg_sal,
    deptno,
    job
FROM emp
```

내 원본의 부서·직무 평균 예제에는 GROUP BY deptno,job,sal이 있어 급여별로 다시 쪼개진다. 강사님 대응 평균 예제는 GROUP BY deptno,job이며 질문의 기준이 다르다. ‘그룹 밖 열은 첫 값’이라는 내 메모는 보장된 규칙이 아니며 ONLY_FULL_GROUP_BY에서는 오류가 날 수 있다.

### 실무에서 사용하거나 디버깅할 때

표현식 결과와 저장 데이터 변경을 구분한다. 결과가 다르면 원본의 앞선 실행 상태, 입력 행 수, NULL·중복·경계값, 조인 후 행 수를 확인한다. 오류 없이 종료한 변경도 0행 대상일 수 있다. 실제 실행 순서·성능은 아래 본문의 논리 설명만으로 단정하지 말고 실행 계획·사후 조회로 검증한다.

### 원본 평균 문제를 작은 입력으로 다시 확인

내 원본에 있는 GROUP BY deptno,job,sal의 의미를 줄인 데이터로 재현한다. 부서·직무가 같은 1000과 2000을 한 그룹으로 평균하면 1500이다. sal까지 묶으면 급여별 그룹으로 나뉘어 1000·2000이 그대로 나온다. SQL 오류 없이 질문 자체가 달라지는 논리 오류다.

```sql
WITH sample(deptno,job,sal) AS (
 SELECT 10,'CLERK',1000 UNION ALL SELECT 10,'CLERK',2000
)
SELECT deptno,job,AVG(sal) AS avg_salary FROM sample GROUP BY deptno,job;
WITH sample(deptno,job,sal) AS (
 SELECT 10,'CLERK',1000 UNION ALL SELECT 10,'CLERK',2000
)
SELECT deptno,job,sal,AVG(sal) AS avg_salary FROM sample
GROUP BY deptno,job,sal ORDER BY sal;
```

검증 결과:

```text
deptno	job	avg_salary
10	CLERK	1500.0000
deptno	job	sal	avg_salary
10	CLERK	1000	1000.0000
10	CLERK	2000	2000.0000
```

### 이해 확인 실습

1. 위 SQL에서 WHERE를 빼면 CLERK 그룹이 남을까?
2. WHERE sal>=1000을 HAVING AVG(sal)>=1000으로 바꾸면 같은 사람을 세는가?

<details>
<summary>정답과 판단 근거 펼치기</summary>

1. 남는다. 전체 CLERK는 4명이므로 HAVING을 만족한다.
2. 아니다. 앞 조건은 집계 입력 행을 제한하고 뒤 조건은 전체 평균으로 그룹을 제한한다.

</details>

### 이 개념을 다시 사용할 수 있는지 확인

- [ ] 개념·필요성·입력 컬럼과 자료형을 내 말로 설명한다.
- [ ] 중간 행·그룹·관계와 최종 결과를 구분한다.
- [ ] 원본 코드의 앞 상태와 보충 예제의 조건을 구분한다.
- [ ] NULL·0행·중복·경계값 또는 변경 실패를 재검토한다.

---

<a id="sql-06-section-4"></a>

## 1. GROUP BY란?

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

<a id="sql-06-section-5"></a>

## 2. 전체 집계와 Group 집계

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

<a id="sql-06-section-6"></a>

## 3. 부서별 사원 수

```sql
SELECT
    deptno,
    COUNT(*) AS employee_count
FROM emp
GROUP BY deptno;
```

<a id="sql-06-section-7"></a>

## 4. 부서별 급여 합계

```sql
SELECT
    deptno,
    SUM(sal) AS total_sal
FROM emp
GROUP BY deptno;
```

<a id="sql-06-section-8"></a>

## 5. 부서별 평균 급여

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno;
```

<a id="sql-06-section-9"></a>

## 6. 부서별 최고·최저 급여

```sql
SELECT
    deptno,
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal
FROM emp
GROUP BY deptno;
```

<a id="sql-06-section-10"></a>

## 7. 여러 Aggregate 함께 사용

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

<a id="sql-06-section-11"></a>

## 8. 직무별 Grouping

```sql
SELECT
    job,
    COUNT(*) AS employee_count,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY job;
```

Grouping 기준은 요구사항에 따라 달라진다.

<a id="sql-06-section-12"></a>

## 9. SELECT Column과 GROUP BY

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

<a id="sql-06-section-13"></a>

## 10. 잘못된 Grouping 예제

```sql
SELECT
    ename,
    deptno,
    AVG(sal)
FROM emp
GROUP BY deptno;
```

한 부서에는 여러 `ENAME`이 있으므로 어느 이름을 Result에 표시해야 하는지 논리적으로 불명확하다.

<a id="sql-06-section-14"></a>

## 11. ONLY_FULL_GROUP_BY

```sql
SELECT @@sql_mode;
```

`ONLY_FULL_GROUP_BY`가 활성화된 환경에서는 Grouping 의미가 불명확한 일반 Column 사용이 제한될 수 있다.

> Error가 나지 않는다고 논리적으로 좋은 Query라는 뜻은 아니다.

<a id="sql-06-section-15"></a>

## 12. 다중 GROUP BY

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

<a id="sql-06-section-16"></a>

## 13. 다중 Grouping 해석

```text
DEPTNO + JOB
→ 하나의 복합 Group Key
```

예를 들어 `20 + CLERK`, `20 + ANALYST`, `30 + CLERK`는 각각 다른 Group이다.

<a id="sql-06-section-17"></a>

## 14. 다중 Grouping 평균

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

<a id="sql-06-section-18"></a>

## 15. GROUP BY와 NULL

Grouping Column에 여러 `NULL`이 있으면 Grouping에서는 하나의 Group으로 취급될 수 있다.

```sql
SELECT
    comm,
    COUNT(*)
FROM emp
GROUP BY comm;
```

이는 일반 비교의 `NULL = NULL → UNKNOWN`과 문맥이 다르다.

<a id="sql-06-section-19"></a>

## 16. WHERE + GROUP BY

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
WHERE sal >= 1500
GROUP BY deptno;
```

`WHERE`로 Row를 먼저 제한한 뒤 남은 Row를 Grouping한다.

<a id="sql-06-section-20"></a>

## 17. WHERE의 역할

```text
EMP
→ WHERE
→ 개별 Row Filtering
→ GROUP BY
→ Group 생성
→ Aggregate
```

<a id="sql-06-section-21"></a>

## 18. HAVING이란?

`HAVING`은 Group 또는 Aggregate 결과를 Filtering한다.

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
HAVING AVG(sal) >= 2000;
```

<a id="sql-06-section-22"></a>

## 19. WHERE와 HAVING

```text
WHERE
→ GROUP BY 전
→ Row Filtering

HAVING
→ GROUP BY 후
→ Group Filtering
```

<a id="sql-06-section-23"></a>

## 20. WHERE에 Aggregate를 쓰는 오류

```sql
SELECT
    deptno,
    AVG(sal)
FROM emp
WHERE AVG(sal) >= 2000
GROUP BY deptno;
```

`WHERE` 단계에서는 아직 부서별 `AVG(sal)`이 만들어지지 않았다.

<a id="sql-06-section-24"></a>

## 21. Aggregate 조건은 HAVING

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
HAVING AVG(sal) >= 2000;
```

<a id="sql-06-section-25"></a>

## 22. COUNT 조건

사원이 4명 이상인 부서:

```sql
SELECT
    deptno,
    COUNT(*) AS employee_count
FROM emp
GROUP BY deptno
HAVING COUNT(*) >= 4;
```

<a id="sql-06-section-26"></a>

## 23. SUM 조건

```sql
SELECT
    deptno,
    SUM(sal) AS total_sal
FROM emp
GROUP BY deptno
HAVING SUM(sal) >= 9000;
```

<a id="sql-06-section-27"></a>

## 24. MAX 조건

```sql
SELECT
    deptno,
    MAX(sal) AS max_sal
FROM emp
GROUP BY deptno
HAVING MAX(sal) >= 3000;
```

<a id="sql-06-section-28"></a>

## 25. WHERE와 HAVING 함께 사용

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
WHERE job <> 'CLERK'
GROUP BY deptno
HAVING AVG(sal) >= 2000;
```

<a id="sql-06-section-29"></a>

## 26. 처리 흐름

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

<a id="sql-06-section-30"></a>

## 27. WHERE로 가능한 조건

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

<a id="sql-06-section-31"></a>

## 28. HAVING과 GROUP BY

`HAVING`은 Grouping Query에서 주로 사용하지만 Aggregate 전체 결과를 조건으로 검사할 때 명시적 `GROUP BY` 없이 사용할 수도 있다.

```sql
SELECT AVG(sal) AS avg_sal
FROM emp
HAVING AVG(sal) >= 2000;
```

초기 학습 기준은 `WHERE = Row`, `HAVING = Aggregate/Group`으로 잡는다.

<a id="sql-06-section-32"></a>

## 29. GROUP BY + ORDER BY

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
ORDER BY avg_sal DESC;
```

<a id="sql-06-section-33"></a>

## 30. Aggregate Alias로 정렬

```sql
SELECT
    deptno,
    COUNT(*) AS employee_count
FROM emp
GROUP BY deptno
ORDER BY employee_count DESC;
```

<a id="sql-06-section-34"></a>

## 31. GROUP BY는 정렬이 아니다

```text
GROUP BY
→ Group 생성

ORDER BY
→ Result 순서 결정
```

Grouping Column 순으로 보이더라도 필요한 순서는 `ORDER BY`로 명시한다.

<a id="sql-06-section-35"></a>

## 32. GROUP BY + HAVING + ORDER BY

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
HAVING AVG(sal) >= 1500
ORDER BY avg_sal DESC;
```

<a id="sql-06-section-36"></a>

## 33. GROUP BY + LIMIT

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

<a id="sql-06-section-37"></a>

## 34. 논리적 Query 처리 순서

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

<a id="sql-06-section-38"></a>

## 35. 작성 순서와 논리 순서

작성:

```text
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

논리:

```text
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

<a id="sql-06-section-39"></a>

## 36. Alias와 HAVING

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

<a id="sql-06-section-40"></a>

## 37. COUNT(column)과 GROUP BY

```sql
SELECT
    deptno,
    COUNT(comm) AS commission_count
FROM emp
GROUP BY deptno;
```

각 Group 안에서도 `COUNT(comm)`은 `COMM IS NULL`인 Row를 제외한다.

<a id="sql-06-section-41"></a>

## 38. DISTINCT와 Grouping

```sql
SELECT
    deptno,
    COUNT(DISTINCT job) AS job_type_count
FROM emp
GROUP BY deptno;
```

부서별 서로 다른 직무 종류 수를 계산한다.

<a id="sql-06-section-42"></a>

## 39. Group별 급여 차이

```sql
SELECT
    deptno,
    MAX(sal) - MIN(sal) AS sal_diff
FROM emp
GROUP BY deptno;
```

05번의 Aggregate Expression을 Group별로 확장한 형태다.

<a id="sql-06-section-43"></a>

## 40. 요구사항 분해법

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

<a id="sql-06-section-44"></a>

## 41. 내 코드와 강사님 코드 비교

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

<a id="sql-06-section-45"></a>

## 42. 개선된 통합 예제

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

<a id="sql-06-section-46"></a>

## 43. 실무 Grouping 기준

```text
1. 대상 Row 결정
2. Group Key 결정
3. Aggregate 결정
4. Row 조건은 WHERE
5. Group 조건은 HAVING
6. 순서는 ORDER BY
7. 개수 제한은 LIMIT
```

<a id="sql-06-section-47"></a>

## 44. 요구사항을 Query로 변환

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

<a id="sql-06-section-48"></a>

## 45. GROUP BY 리팩토링

### Before

```sql
SELECT
    deptno,
    ename,
    AVG(sal)
FROM emp
GROUP BY deptno;
```

### After

```sql
SELECT
    deptno,
    AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno;
```

Group을 대표하지 못하는 일반 Column을 제거한다.

<a id="sql-06-section-49"></a>

## 46. WHERE / HAVING 리팩토링

### Before

```sql
SELECT deptno, COUNT(*)
FROM emp
GROUP BY deptno
HAVING deptno = 20;
```

### After

```sql
SELECT deptno, COUNT(*)
FROM emp
WHERE deptno = 20
GROUP BY deptno;
```

Grouping 전에 Filtering 가능한 Row 조건은 `WHERE`가 더 명확하다.

<a id="sql-06-section-50"></a>

## 47. 자주 하는 실수

- `GROUP BY`가 자동 정렬한다고 생각한다.
- 일반 Column을 Grouping 의미 없이 SELECT한다.
- Aggregate 조건을 `WHERE`에 작성한다.
- 모든 조건을 `HAVING`에 몰아넣는다.
- 다중 `GROUP BY`를 독립된 Group으로 오해한다.
- `HAVING`은 무조건 명시적 `GROUP BY`와만 사용한다고 생각한다.
- Grouping의 NULL 처리를 일반 `NULL = NULL` 비교와 동일하게 해석한다.

<a id="sql-06-section-51"></a>

## 48. Debugging

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

<a id="sql-06-section-52"></a>

## 49. 종합실습

1. 부서별 사원 수를 조회하시오.
2. 직무별 평균 급여를 조회하시오.
3. 부서별 급여 합계, 평균, 최고, 최저를 조회하시오.
4. 부서와 직무별 사원 수를 조회하시오.
5. 사원이 4명 이상인 부서만 조회하시오.
6. 평균 급여가 2000 이상인 직무만 조회하시오.
7. 급여 1500 이상 사원만 대상으로 부서별 평균을 구하시오.
8. `CLERK`를 제외하고 부서별 평균을 구한 뒤 평균 2000 이상만 내림차순 조회하시오.
9. `WHERE AVG(sal) >= 2000`이 잘못된 이유를 설명하시오.

<a id="sql-06-section-53"></a>

## 50. 정답과 해설

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

<a id="sql-06-section-54"></a>

## 51. 최종 체크리스트

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

<a id="sql-06-section-55"></a>

## 52. 핵심 요약

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

<a id="sql-06-section-56"></a>

## 마무리

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
<a id="sql-06-section-57"></a>

## V3 동작 백과 — Row가 Group으로 묶이고 다시 걸러지는 과정

> 입력 범위 확인: 이 복습 부분의 작은 표는 처리 원리를 위한 가정·발췌이며 전체 초기화 EMP의 입력 전체가 아니다. FROM emp를 그대로 실행하면 모든 대상 사원을 처리한다. 수치는 작은 가정 입력의 결과인지 전체 14행 결과인지 구분한다. 실행·시간순 설명은 논리적 설명이며 물리적 평가 순서를 보장하지 않는다.

<a id="index-section-74"></a>

### 기존 네 행 그룹 표의 입력을 CTE로 재현

기존 V3의 부서30·2명·평균1425는 네 행 가상 입력의 결과다. 전체 EMP로 실행한 결과라고 오해하지 않도록 아래에서 입력 자체를 명시한다.

```sql
WITH sample(ename,deptno,sal) AS (
 SELECT 'SMITH',20,800 UNION ALL SELECT 'JONES',20,2975 UNION ALL
 SELECT 'ALLEN',30,1600 UNION ALL SELECT 'WARD',30,1250
)
SELECT deptno,COUNT(*) AS emp_count,AVG(sal) AS avg_sal
FROM sample WHERE sal>=1000 GROUP BY deptno HAVING COUNT(*)>=2 ORDER BY deptno;
```

```text
deptno	emp_count	avg_sal
30	2	1425.0000
```

아래 기존 표는 이 작은 입력을 손으로 따라가는 복습 설명이다.


### 왜 배워야 하는가?

전체 평균 한 개가 아니라 부서별·직무별 통계를 만들려면 어떤 Row끼리 같은 집단인지 정의해야 한다.

입력:

```text
ENAME | DEPTNO | SAL
SMITH | 20     | 800
JONES | 20     | 2975
ALLEN | 30     | 1600
WARD  | 30     | 1250
```

```sql
SELECT deptno, COUNT(*) AS emp_count, AVG(sal) AS avg_sal
FROM emp
WHERE sal >= 1000
GROUP BY deptno
HAVING COUNT(*) >= 2
ORDER BY deptno;
```

실제 논리 흐름:

```text
FROM emp
→ WHERE sal >= 1000: SMITH 제외
→ GROUP BY deptno: 20번 Group, 30번 Group 생성
→ COUNT·AVG: Group별 계산
→ HAVING COUNT(*) >= 2: 사원 2명 이상 Group만 유지
→ SELECT Result Column 구성
→ ORDER BY deptno
```

중간 상태:

```text
20번 Group → JONES 1명 → HAVING에서 제외
30번 Group → ALLEN, WARD 2명 → 유지
```

결과:

```text
DEPTNO | EMP_COUNT | AVG_SAL
30     | 2         | 1425
```

### WHERE와 HAVING이 다른 이유

`WHERE` 단계에는 아직 Group과 `COUNT(*)`가 만들어지지 않았다. Aggregate 조건은 Group 계산 이후인 `HAVING`에서 평가한다.

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 검색 Anchor | 강사님 코드 검색 Anchor |
| --- | --- | --- |
| 부서 Group | `group by deptno` | 같은 Query |
| 다중 Group | `group by deptno, job` | 다중 Grouping 구간 |
| Group 조건 | `having` | `having` |
| 논리 순서 | WHERE·GROUP·HAVING 통합 Query | 같은 실습 구간 |

복잡한 Query는 각 단계 뒤에 어떤 Row 또는 Group이 남는지 손으로 적어 보면 이해하기 쉽다.
