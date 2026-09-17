# 19. SQL 실무 코딩 스타일

> 읽기 쉽고 검증 가능하며 안전하게 변경할 수 있는 MariaDB SQL 작성 기준

---

## 이 문서에서 바로 찾기

- [학습 목표](#sql-19-section-2)
- [개념에서 실제 실행까지 — SQL 리팩토링이란? — 같은 질문을 더 분명하게 표현](#sql-19-section-3)
- [21. 내 코드와 강사님 코드 비교](#sql-19-section-24)
- [26. 종합실습](#sql-19-section-29)
- [27. 정답과 해설](#sql-19-section-30)
- [28. 최종 체크리스트](#sql-19-section-31)
- [29. 핵심 요약](#sql-19-section-32)

<details>
<summary>상세 목차 전체 펼치기</summary>

- [📌 문서 정보](#sql-19-section-1)
- [학습 목표](#sql-19-section-2)
- [개념에서 실제 실행까지 — SQL 리팩토링이란? — 같은 질문을 더 분명하게 표현](#sql-19-section-3)
- [1. 좋은 SQL의 기준](#sql-19-section-4)
- [2. Keyword와 Identifier 표기](#sql-19-section-5)
- [3. Table·Column Naming](#sql-19-section-6)
- [4. Alias](#sql-19-section-7)
- [5. SELECT Formatting](#sql-19-section-8)
- [6. SELECT * 사용 기준](#sql-19-section-9)
- [7. WHERE와 조건식](#sql-19-section-10)
- [8. NULL 작성 기준](#sql-19-section-11)
- [9. JOIN 스타일](#sql-19-section-12)
- [10. GROUP BY와 집계](#sql-19-section-13)
- [11. CASE와 계산식](#sql-19-section-14)
- [12. Subquery와 CTE](#sql-19-section-15)
- [13. UNION 스타일](#sql-19-section-16)
- [14. Parameter Binding](#sql-19-section-17)
- [15. 안전한 DML 스타일](#sql-19-section-18)
- [16. Transaction 스타일](#sql-19-section-19)
- [17. DDL·Schema 스타일](#sql-19-section-20)
- [18. Index·성능 스타일](#sql-19-section-21)
- [19. Comment와 문서화](#sql-19-section-22)
- [20. SQL_MODE와 환경](#sql-19-section-23)
- [21. 내 코드와 강사님 코드 비교](#sql-19-section-24)
- [22. 개선된 통합 예제](#sql-19-section-25)
- [23. 실무 Code Review 절차](#sql-19-section-26)
- [24. 자주 하는 실수](#sql-19-section-27)
- [25. 디버깅 방법](#sql-19-section-28)
- [26. 종합실습](#sql-19-section-29)
- [27. 정답과 해설](#sql-19-section-30)
- [28. 최종 체크리스트](#sql-19-section-31)
- [29. 핵심 요약](#sql-19-section-32)
- [📎 다음 문서](#sql-19-section-33)
- [🔬 V3 백과사전식 SQL 작성 절차](#sql-19-section-34)

</details>

---

<a id="sql-19-section-1"></a>

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | Naming, Formatting, Query Design, 안전한 DML, Review·성능 기준 |
| 기준 DBMS | MariaDB, InnoDB |
| 적용 범위 | `SELECT`, JOIN, CTE, DDL, DML, Transaction, Index |
| 선수 학습 | SQL 01~18 전체 |
| 다음 학습 | SQL 종합실습 |
| 문서 버전 | V3 Encyclopedia |

> 이 문서는 새 문법을 추가하는 단원이 아니라 지금까지 학습한 SQL을 협업 가능한 Production Code로 정리하는 기준이다. 팀 Convention이 있다면 팀 규칙을 우선하되, 한 Repository 안에서는 일관성을 유지한다.

---

<a id="sql-19-section-2"></a>

## 학습 목표

- 관계·필터·열·정렬·경계 검증 기준을 적용한다.
- 실제 입력·중간 상태·결과와 실패 조건을 직접 확인한다.

---

<a id="sql-19-section-3"></a>

## 개념에서 실제 실행까지 — SQL 리팩토링이란? — 같은 질문을 더 분명하게 표현

### 무엇이며 왜 배워야 할까?

SQL 리팩토링은 보기 좋게 줄만 바꾸는 작업이 아니다. 같은 업무 질문과 결과 계약을 유지하면서 관계·조건·집계·변경 범위를 읽기 쉽게 표현하고 검증하는 일이다. INNER와 LEFT를 바꾸거나 NULL을 0으로 바꾸거나 DISTINCT를 추가하면 결과 계약이 달라질 수 있어 ‘정리’와 ‘기능 변경’을 구분한다.

여러 테이블 JOIN 뒤에 조건을 몰아서 적으면 어떤 관계가 빠졌는지 찾기 어렵다. 각 JOIN에 관련 ON을 두고 SELECT 열에 출처 별칭을 붙이면 관계와 표시 목적이 드러난다. 어느 조건이 WHERE에서 사원을 제한하는지와 어떤 조건이 ON에서 급여 구간을 연결하는지도 구분한다.

대용량 데이터에서 날짜 열에 YEAR·SUBSTRING을 씌워 필터하는 방식은 인덱스 활용 측면에서 검토할 대상이다. 범위 조건은 날짜 의미를 직접 표현하고, DATETIME까지 확장할 때 연말 자정 뒤의 값을 누락하지 않도록 반열린 구간을 쓴다. 이것만으로 실제 계획·시간 개선을 입증한 것은 아니다.

💡 19번은 별도 수업 구현 파일이 아니라 앞선 SQL을 다시 사용할 작성·검수 기준이다. 원본에서 내 ‘문제6 개선’처럼 명시적 JOIN으로 정리한 사례와 연결한다.

### 입력은 어디에서 오는가?

초기화 자료의 EMP·DEPT 또는 SQL 안에서 직접 만든 CTE를 사용한다. 각 코드에 명시된 입력을 읽고 전체 EMP와 작은 가상 입력을 구분한다.

### 실행 가능한 보충 SQL과 결과

아래는 원본의 개념을 작은 검증 범위로 정리한 보충 예제다. MariaDB 12.3.2, 일반 SQL 모드·InnoDB 기준에서 결과를 확인했다. 조회 SQL은 SQL 편집기의 Result Grid, 변경 SQL은 영향 행 표시와 사후 SELECT로 관찰한다. DBMS·모드·데이터 상태가 다르면 차이를 확인해야 한다.

```sql
SELECT COUNT(*) AS hired_count,
       MIN(hiredate) AS first_hired,
       MAX(hiredate) AS last_hired
FROM emp
WHERE hiredate >= '1981-01-01'
  AND hiredate < '1982-01-01';
```

Result Grid의 열·행 값:

```text
hired_count	first_hired	last_hired
10	1981-02-20	1981-12-03
```

여러 SELECT가 있으면 위 출력에 결과 헤더가 다시 나타난다. 숫자의 표시 자릿수와 NULL 표시 모양은 클라이언트별로 달라질 수 있지만 값과 행의 의미를 먼저 비교한다.

### 논리적 처리와 상태 변화 — 단계별로 따라가기

1. 1981년 1월 1일 이상, 1982년 1월 1일 미만으로 입력 사원을 제한한다.
2. COUNT로 선택된 전체 10명을 확인한다.
3. MIN/MAX로 선택 범위의 실제 최소·최대 입사일을 관찰한다.
4. 원래 연도 질문을 유지하면서 문자열 추출 대신 날짜 조건을 직접 사용한다.

### 내 코드·강사님 코드의 어느 부분에 있었을까?


#### 내 코드: `workspace_sql/Script.sql` 1068~1077행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
-- group by e.ename
order by s.grade desc, e.sal desc, e.ename desc; 

-- 문제6 개선
select e.ename, e.sal, s.grade, d.dname
from emp e 
	join dept d
		on (e.deptno = d.deptno)
	join salgrade s
		on (e.sal between s.losal and s.hisal)
```

#### 강사님 코드: `workspace_teacher/workspace_sql/Script.sql` 1003~1012행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
단, 급여 등급 3 이상만 조회.
급여 등급 내림차순, 등급이 같은 경우 급여 내림차순, 급여가 같은 경우 이름 내림차순
*/
select e.ename, e.sal, s.grade, d.dname
from salgrade s
	left outer join emp e 
		on (e.sal <= s.hisal and e.sal >= s.losal)
	left outer join dept d
		on(e.deptno = d.deptno)
where s.grade >= 3
```

내 문제1의 마지막 풀이에는 바깥 연도 조건이 없어 다른 해의 같은 최소급여 사원도 들어갈 수 있다. 강사님은 바깥에서 hiredate like '1981%'를 확인한다. 더 명확한 범위 조건은 바깥·안쪽 모두의 업무 대상을 맞춘다.

### 실무에서 사용하거나 디버깅할 때

표현식 결과와 저장 데이터 변경을 구분한다. 결과가 다르면 원본의 앞선 실행 상태, 입력 행 수, NULL·중복·경계값, 조인 후 행 수를 확인한다. 오류 없이 종료한 변경도 0행 대상일 수 있다. 실제 실행 순서·성능은 아래 본문의 논리 설명만으로 단정하지 말고 실행 계획·사후 조회로 검증한다.

### 1981년 최저급여 — 바깥·안쪽 범위를 일치시키기

내 원본의 문제1 최종 풀이에서 빠진 바깥 연도 조건을 보완했다. 최소급여를 계산한 집합과 그 급여를 가진 사원을 찾는 집합 모두 1981년으로 제한한다. 다른 해의 동급여 사원이 있어도 잘못 포함되지 않는다.

```sql
SELECT ename,sal,hiredate FROM emp
WHERE hiredate>='1981-01-01' AND hiredate<'1982-01-01'
AND sal=(SELECT MIN(sal) FROM emp
 WHERE hiredate>='1981-01-01' AND hiredate<'1982-01-01')
ORDER BY empno;
```

검증 결과:

```text
ename	sal	hiredate
JAMES	950.00	1981-12-03
```

### 이해 확인 실습

1. DATETIME 조건에 <= '1981-12-31'을 쓰면 연말 하루 전체를 보장하는가?
2. 조회 결과만 동일하면 LEFT JOIN을 INNER JOIN으로 바꿔도 항상 리팩토링인가?

<details>
<summary>정답과 판단 근거 펼치기</summary>

1. 아니다. 자정으로 해석되어 이후 시간이 빠질 수 있다. <'1982-01-01'로 다음 경계 전까지 표현한다.
2. 현재 데이터에서만 같을 수 있다. 빈 관계를 보존하는 계약이 달라지면 기능 변경이다.

</details>

### 이 개념을 다시 사용할 수 있는지 확인

- [ ] 개념·필요성·입력 컬럼과 자료형을 내 말로 설명한다.
- [ ] 중간 행·그룹·관계와 최종 결과를 구분한다.
- [ ] 원본 코드의 앞 상태와 보충 예제의 조건을 구분한다.
- [ ] NULL·0행·중복·경계값 또는 변경 실패를 재검토한다.

---

<a id="sql-19-section-4"></a>

## 1. 좋은 SQL의 기준

### 1. 정확성

요구사항과 같은 Row·Column·집계 결과를 반환해야 한다.

### 2. 가독성

다른 개발자가 관계와 Filtering, 집계 의도를 빠르게 설명할 수 있어야 한다.

### 3. 안전성

NULL, 중복, 경계값, 전체 DML, Transaction 실패를 고려해야 한다.

### 4. 성능

필요한 Data만 읽고 실제 실행 계획과 운영 규모에서 허용 가능한 비용이어야 한다.

### 5. 유지보수성

Schema와 요구사항 변경 시 수정 범위와 영향이 명확해야 한다.

### 6. 이식성과 Version 명시

MariaDB 전용 문법을 사용할 수 있지만 지원 Version과 다른 DBMS와의 차이를 문서화한다.

---

<a id="sql-19-section-5"></a>

## 2. Keyword와 Identifier 표기

### 7. Keyword는 대문자로 통일한다

```sql
SELECT empno, ename
FROM emp
WHERE deptno = 20
ORDER BY empno;
```

MariaDB는 보통 Keyword 대소문자를 구분하지 않지만 시각적 구분을 위해 Convention을 정한다.

### 8. Identifier는 소문자 snake_case를 권장한다

```text
employee_id
created_at
department_summary
```

### 9. 예약어를 이름으로 사용하지 않는다

`order`, `group`, `rank` 같은 예약어·향후 예약 가능 이름은 Backtick 의존과 이식성 문제를 만든다.

### 10. Backtick은 필요한 경우에만 사용한다

```sql
SELECT `select`
FROM legacy_table;
```

기존 Schema 때문에 필요할 수 있지만 새 설계에서는 단순한 비예약어 이름을 선택한다.

### 11. 한글·공백 Identifier를 피한다

표시용 Alias에는 사용할 수 있어도 물리 Schema 이름은 Tool·Migration·외부 연동을 고려해 단순하게 정한다.

### 12. 이름에 자료형을 중복하지 않는다

`user_name_varchar`보다 `user_name`처럼 업무 의미를 표현한다.

---

<a id="sql-19-section-6"></a>

## 3. Table·Column Naming

### 13. 단수·복수 규칙을 팀에서 통일한다

`employee` 또는 `employees` 중 하나를 선택하고 Repository 안에서 혼용하지 않는다.

<a id="index-section-32"></a>

### 14. Primary Key Naming

```text
employee_id
department_id
order_id
```

여러 Table을 JOIN할 때 Source와 의미가 명확하다.

### 15. Foreign Key는 참조 대상 의미를 유지한다

`employee.department_id → department.department_id`처럼 관계를 쉽게 추적할 수 있게 한다.

### 16. Boolean 성격은 긍정형을 선호한다

```text
is_active
has_permission
is_deleted
```

`is_not_disabled` 같은 이중 부정은 조건을 어렵게 만든다.

### 17. 날짜·시간 Suffix

```text
created_at, updated_at
birth_date, start_date
```

`_at`과 `_date`로 시간 포함 여부를 구분하는 Convention을 사용할 수 있다.

### 18. 단위를 이름에 포함한다

```text
timeout_seconds
size_bytes
amount_krw
```

단위 혼동 가능성이 있으면 명시한다.

---

<a id="sql-19-section-7"></a>

## 4. Alias

### 19. 짧지만 역할이 드러나는 Alias

```sql
SELECT e.empno, e.ename, d.dname
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

<a id="index-section-39"></a>

### 20. Self Join은 역할 이름을 쓴다

```sql
SELECT
    employee.ename AS employee_name,
    manager.ename AS manager_name
FROM emp AS employee
LEFT JOIN emp AS manager
    ON manager.empno = employee.mgr;
```

### 21. Derived Table·CTE는 결과 의미로 이름 짓는다

```text
dept_summary
monthly_sales
eligible_customers
```

### 22. 계산 Column Alias는 단위를 설명한다

```sql
ROUND(AVG(sal), 2) AS avg_salary
```

### 23. Alias에 작은따옴표를 쓰지 않는다

작은따옴표는 문자열 Literal 의미가 중심이다. 일반 Identifier Alias를 사용한다.

### 24. 같은 의미에 다른 Alias를 혼용하지 않는다

한 Query에서 `dept`, `department`, `d`를 무계획하게 섞지 않는다.

---

<a id="sql-19-section-8"></a>

## 5. SELECT Formatting

### 25. 한 Column씩 줄바꿈한다

```sql
SELECT
    e.empno,
    e.ename,
    e.job,
    e.sal,
    d.dname AS department_name
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno;
```

### 26. 짧은 Query는 한 줄도 가능하다

```sql
SELECT COUNT(*) AS employee_count FROM emp;
```

일관성과 읽기 비용을 기준으로 선택한다.

### 27. Clause는 새로운 줄에서 시작한다

```text
SELECT
FROM
JOIN / ON
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
```

### 28. 논리 처리 흐름을 이해한다

```text
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

작성 순서와 논리적 평가 순서는 다르다.

### 29. 세미콜론으로 문장을 끝낸다

여러 문장을 실행하는 Script에서 경계를 명확히 한다.

---

<a id="sql-19-section-9"></a>

## 6. SELECT * 사용 기준

### 30. 탐색 단계에서는 사용할 수 있다

```sql
SELECT * FROM emp LIMIT 10;
```

### 31. Application Query는 Column을 명시한다

```sql
SELECT empno, ename, job
FROM emp
ORDER BY empno;
```

### 32. Schema 변경 영향 감소

Column 추가·순서 변경이 API Response, Mapping, Network 비용에 예기치 않게 영향을 주는 것을 줄인다.

### 33. JOIN의 중복 Column 방지

`SELECT *`는 양쪽 `DEPTNO`처럼 의미가 겹치는 Column을 함께 반환한다.

### 34. Covering Index 가능성

필요한 Column만 조회하면 Index만으로 Query를 처리할 가능성도 높아질 수 있다.

---

<a id="sql-19-section-10"></a>

## 7. WHERE와 조건식

### 35. 하나의 조건은 한 줄에 작성한다

```sql
WHERE e.deptno = 20
  AND e.sal >= 2000
  AND e.job IN ('MANAGER', 'ANALYST')
```

### 36. AND·OR 혼합은 괄호로 의도를 표현한다

```sql
WHERE e.deptno = 20
  AND (
      e.job = 'MANAGER'
      OR e.sal >= 3000
  )
```

### 37. 범위 경계를 명확히 한다

```sql
WHERE amount >= 1000
  AND amount < 2000
```

Inclusive·Exclusive 경계를 요구사항과 함께 기록한다.

### 38. 날짜·시간은 반열린 구간을 권장한다

```sql
WHERE created_at >= '2026-08-01 00:00:00'
  AND created_at <  '2026-09-01 00:00:00'
```

월말 마지막 Microsecond를 계산하는 방식보다 안전하다.

### 39. Column에 함수를 적용하기 전에 Index를 고려한다

```sql
-- WHERE DATE(created_at) = '2026-08-14'
```

날짜 범위 조건이 일반 Index 사용에 유리할 수 있다.

### 40. 불필요한 `WHERE 1 = 1`을 남기지 않는다

Dynamic Query Builder 내부 목적이 아니라면 최종 SQL에서는 제거한다.

---

<a id="sql-19-section-11"></a>

## 8. NULL 작성 기준

### 41. 등호로 비교하지 않는다

```sql
WHERE comm IS NULL
```

### 42. NULL과 0·빈 문자열을 구분한다

업무 상태가 다르면 Query와 Schema에서도 별도로 처리한다.

### 43. COALESCE는 의미가 같을 때만 사용한다

```sql
COALESCE(comm, 0) AS commission_amount
```

미입력과 0 지급을 같은 표시로 처리해도 되는지 확인한다.

### 44. NOT IN의 NULL을 확인한다

```sql
WHERE deptno NOT IN (
    SELECT deptno
    FROM blocked_department
    WHERE deptno IS NOT NULL
)
```

또는 `NOT EXISTS`를 검토한다.

### 45. Outer Join 미일치는 NOT NULL Key로 판정한다

Nullable 일반 Column이 아니라 오른쪽 PK를 `IS NULL`로 검사한다.

---

<a id="sql-19-section-12"></a>

## 9. JOIN 스타일

### 46. ANSI JOIN을 사용한다

```sql
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
```

### 47. 쉼표 Join을 새 Code에 사용하지 않는다

관계 조건과 Filtering 조건이 모두 WHERE에 섞이고 누락된 조건을 찾기 어렵다.

### 48. 관계는 ON, Filtering은 WHERE

```sql
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
WHERE e.sal >= 2000
```

<a id="index-section-73"></a>

### 49. Outer Join의 오른쪽 조건 위치를 검토한다

모든 왼쪽 Row를 보존하려면 오른쪽 연결 제한을 `ON`에 둔다.

### 50. Join Key를 양쪽 Alias로 한정한다

```sql
ON order_item.order_id = customer_order.order_id
```

### 51. Join 전 Cardinality를 정의한다

1:1, 1:N, N:M 중 어떤 관계인지 알아야 중복과 집계 변화를 예측할 수 있다.

### 52. DISTINCT로 잘못된 JOIN을 숨기지 않는다

누락된 조건과 정상적인 일대다 관계를 먼저 확인한다.

---

<a id="sql-19-section-13"></a>

## 10. GROUP BY와 집계

### 53. 일반 Column을 Grouping 기준에 맞춘다

```sql
SELECT d.deptno, d.dname, COUNT(*) AS employee_count
FROM emp AS e
JOIN dept AS d ON d.deptno = e.deptno
GROUP BY d.deptno, d.dname;
```

### 54. ONLY_FULL_GROUP_BY에 맞는 Query를 작성한다

현재 환경에서 Mode가 꺼져 실행된다고 비결정적 일반 Column을 선택하지 않는다.

<a id="index-section-80"></a>

### 55. WHERE와 HAVING을 구분한다

```text
WHERE
→ Grouping 전 Row Filtering

HAVING
→ Grouping 후 집계 결과 Filtering
```

### 56. COUNT 대상을 의도에 맞게 고른다

Outer Join에서 일치 Row 수는 `COUNT(right_table.pk)`가 적합하다.

### 57. 집계 전 Join Row를 확인한다

일대다 Join으로 `SUM`이나 `COUNT`가 부풀려지지 않는지 상세 결과를 먼저 조회한다.

### 58. Alias에 집계 의미와 단위를 담는다

```text
employee_count
total_amount_krw
avg_processing_seconds
```

---

<a id="sql-19-section-14"></a>

## 11. CASE와 계산식

### 59. 조건은 위에서 아래로 읽힌다

좁거나 우선순위가 높은 조건을 먼저 둔다.

### 60. ELSE를 의도적으로 작성한다

생략 시 NULL이 반환되어도 되는지 확인한다.

### 61. 결과 자료형을 통일한다

숫자와 표시 문자열을 같은 CASE에 섞지 않는다.

### 62. 조건부 집계의 분모를 확인한다

```sql
AVG(CASE WHEN deptno = 20 THEN sal END)
```

`ELSE 0`을 추가하면 의미가 달라진다.

### 63. 반복되는 긴 CASE를 CTE로 분리한다

분류 규칙이 기준 Data라면 Mapping Table과 JOIN도 검토한다.

---

<a id="sql-19-section-15"></a>

## 12. Subquery와 CTE

### 64. 반환 형태를 먼저 정의한다

Scalar인지 다중 Row인지 Table 형태인지 확인한다.

### 65. 같은 Subquery를 반복하지 않는다

Derived Table, CTE, JOIN으로 한 번 계산하는 구조를 검토한다.

### 66. CTE 이름으로 처리 단계를 설명한다

```sql
WITH dept_summary AS (
    SELECT deptno, COUNT(*) AS employee_count, AVG(sal) AS avg_salary
    FROM emp
    GROUP BY deptno
)
SELECT *
FROM dept_summary
WHERE avg_salary >= 2000;
```

### 67. CTE가 자동 성능 개선은 아니다

가독성 도구로 사용하고 실제 Optimizer 처리와 실행 계획을 확인한다.

### 68. 깊은 중첩을 단계별 결과로 푼다

각 CTE의 한 Row 의미를 Comment나 이름으로 설명한다.

### 69. Recursive CTE는 종료·Cycle·자료형을 명시한다

Server 반복 제한만 믿지 않는다.

---

<a id="sql-19-section-16"></a>

## 13. UNION 스타일

### 70. 공통 Result Schema를 먼저 정한다

각 Branch의 Column 개수, 순서, 의미, 자료형을 맞춘다.

### 71. 중복 보존 여부를 요구사항으로 결정한다

모든 사건·Row가 필요하면 `UNION ALL`, 고유 집합이 필요하면 `UNION`을 사용한다.

### 72. 첫 SELECT에 최종 Alias를 둔다

Result Column명은 첫 Branch를 기준으로 정해진다.

### 73. 전체 ORDER BY는 마지막에 작성한다

각 Branch의 Top-N은 별도 괄호·Derived Table로 목적을 명확히 한다.

### 74. UNION으로 중복 원인을 숨기지 않는다

잘못된 JOIN이나 Source 중복을 먼저 진단한다.

---

<a id="sql-19-section-17"></a>

## 14. Parameter Binding

### 75. 값을 문자열로 연결하지 않는다

```text
나쁜 방식
→ "... WHERE user_id = " + input

좋은 방식
→ WHERE user_id = ?
```

### 76. Prepared Statement Parameter

```sql
SELECT empno, ename
FROM emp
WHERE deptno = ?
  AND sal >= ?;
```

### 77. SQL Injection 방지

Binding은 값과 SQL 구조를 분리한다.

### 78. Identifier는 일반 값 Parameter로 Binding할 수 없다

Table명, Column명, `ASC / DESC` 같은 SQL 구조는 허용 목록으로 검증한 뒤 안전하게 조합한다.

<a id="index-section-108"></a>

### 79. LIKE 값도 Parameter화한다

Wildcard를 Application에서 의도적으로 붙이거나 SQL 함수로 결합하되 사용자 입력의 Pattern 의미를 정의한다.

### 80. Log에는 민감값을 노출하지 않는다

SQL Template, 실행 시간, Parameter Type과 필요 최소 정보만 남기고 개인정보·Credential을 Masking한다.

---

<a id="sql-19-section-18"></a>

## 15. 안전한 DML 스타일

### 81. INSERT Column 목록 명시

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES (?, ?, ?);
```

### 82. UPDATE·DELETE 전 Preview

```sql
SELECT empno, ename, sal
FROM emp_practice
WHERE deptno = 50;
```

같은 FROM·JOIN·WHERE로 대상 Key와 예상값을 확인한다.

### 83. Key 기반 WHERE

가능하면 승인된 Primary Key 목록이나 안정적인 업무 Key로 변경 대상을 고정한다.

### 84. 영향 Row 수 검증

`ROW_COUNT()` 또는 Connector의 Affected Rows가 예상 범위와 같은지 확인한다.

### 85. 전체 변경은 의도를 Comment와 승인으로 명시한다

WHERE 없는 UPDATE·DELETE가 정말 필요한 경우에도 대상 Count, Backup, Transaction, Review를 준비한다.

### 86. IGNORE로 오류를 숨기지 않는다

누락·변환 Warning을 조사하고 Data 품질 문제를 해결한다.

### 87. 운영 Script는 재실행 가능성을 설계한다

중복 실행 시 결과, 멱등성, 완료 Marker, 실패 재시작 지점을 정의한다.

---

<a id="sql-19-section-19"></a>

## 16. Transaction 스타일

### 88. 업무 단위와 Transaction 경계를 맞춘다

```text
START TRANSACTION
→ Lock·검증
→ DML
→ 영향 Row·불변 조건 확인
→ COMMIT 또는 ROLLBACK
```

### 89. 모든 종료 경로를 처리한다

성공은 Commit, SQL 오류·검증 실패·Timeout은 Rollback한다.

### 90. DDL을 DML Transaction에 섞지 않는다

암시적 Commit 위험 때문에 Schema Migration과 Data 변경을 분리한다.

### 91. Transaction을 짧게 유지한다

외부 API, 사용자 입력, 긴 계산을 Transaction 안에서 기다리지 않는다.

### 92. Lock 순서를 통일한다

같은 여러 Row를 변경하는 업무는 ID 오름차순처럼 일관된 순서로 Lock한다.

### 93. Deadlock 재시도는 전체 업무 단위로 수행한다

부분 문장만 반복하지 않고 멱등성과 최대 재시도 횟수를 설계한다.

---

<a id="sql-19-section-20"></a>

## 17. DDL·Schema 스타일

### 94. 자료형에 업무 근거를 둔다

금액은 `DECIMAL`, 시간은 날짜·시간 자료형, Identifier는 예상 범위를 고려한 정수를 사용한다.

### 95. NOT NULL과 DEFAULT 의미를 문서화한다

오류를 피하기 위한 임의 Default보다 실제 업무 상태를 표현한다.

<a id="index-section-128"></a>

### 96. Constraint 이름을 명시한다

```text
pk_employee
fk_employee_department
ux_user_email
```

### 97. Foreign Key 동작을 의도적으로 선택한다

`RESTRICT`, `CASCADE`, `SET NULL`의 Data 수명주기를 Review한다.

### 98. Migration 전 기존 Data를 진단한다

NULL, 중복, 길이, 범위, FK 위반을 확인한다.

### 99. 파괴적 DDL은 복구 계획을 요구한다

`DROP`, `TRUNCATE`, Column 삭제·축소 전 Backup, Dependency, Downtime을 검토한다.

---

<a id="sql-19-section-21"></a>

## 18. Index·성능 스타일

### 100. Query를 먼저 측정한다

빈도, 실행 시간, 검사 Row, 반환 Row, Data 분포를 확인한다.

### 101. EXPLAIN으로 계획을 읽는다

`possible_keys`, `key`, `type`, `rows`, `Extra`를 함께 해석한다.

### 102. ANALYZE 계열은 실제 실행임을 인식한다

MariaDB의 `ANALYZE` 또는 `ANALYZE FORMAT=JSON`은 Statement를 실행하고 Runtime 통계를 수집하므로 변경 문장과 무거운 Query에 특히 주의한다.

### 103. 복합 Index의 순서를 Query와 맞춘다

동등 조건, 범위, 정렬, 주요 Query 조합과 왼쪽 Prefix를 검토한다.

### 104. Hint는 최후 수단이다

통계, Query, Index를 개선할 수 없는 근거가 있고 지속적인 성능 Test가 있을 때 사용한다.

### 105. 작은 Sample의 실행 계획을 일반화하지 않는다

운영과 유사한 Row 수와 분포에서 검증한다.

### 106. 성능 개선 전후 Correctness를 비교한다

빠른 Query가 원래와 다른 Row를 반환하면 개선이 아니다.

---

<a id="sql-19-section-22"></a>

## 19. Comment와 문서화

### 107. 무엇보다 왜를 설명한다

```sql
-- 월말 23:59:59 계산 대신 다음 달 시작 미만으로 경계를 고정한다.
WHERE created_at >= :month_start
  AND created_at <  :next_month_start
```

### 108. Code를 그대로 번역하는 Comment는 줄인다

```sql
-- 급여가 2000 이상
WHERE sal >= 2000
```

### 109. 업무 규칙의 출처를 기록한다

Ticket, 정책 Version, Data Contract와 연결한다.

### 110. 임시 Debug SQL을 Production Code에 남기지 않는다

무제한 SELECT, 강제 Index, Session 설정 변경을 정리한다.

### 111. 위험한 Script에는 실행 전 조건을 적는다

대상 환경, 예상 Row 수, Backup 위치, 승인자, Rollback 절차를 포함한다.

---

<a id="sql-19-section-23"></a>

## 20. SQL_MODE와 환경

### 112. 현재 Mode 확인

```sql
SELECT @@sql_mode, @@global.sql_mode;
```

### 113. Strict Mode를 고려한다

엄격하지 않은 환경에서는 잘못된 값이 변환·잘림과 Warning으로 처리될 수 있다.

### 114. ONLY_FULL_GROUP_BY에 맞춘다

Mode가 활성화되지 않은 개발 환경에서도 결정적인 Grouping Query를 작성한다.

### 115. 개발·Test·운영 설정을 맞춘다

SQL_MODE, Time Zone, Character Set, Collation, Isolation Level 차이를 관리한다.

### 116. Version 차이를 명시한다

MariaDB 기능과 문법을 MySQL 또는 다른 DBMS와 같다고 가정하지 않는다.

---

<a id="sql-19-section-24"></a>

## 21. 내 코드와 강사님 코드 비교

### 117. 동작 중심의 압축된 Query

```sql
select e.*, d.dname from emp e, dept d where e.deptno=d.deptno and e.sal>=2000 order by e.sal desc;
```

### 118. 구조를 분리한 개선 Query

```sql
SELECT
    e.empno,
    e.ename,
    e.job,
    e.sal,
    d.dname AS department_name
FROM emp AS e
JOIN dept AS d
    ON d.deptno = e.deptno
WHERE e.sal >= 2000
ORDER BY e.sal DESC, e.empno;
```

### 119. 직접 실행하는 변경

```sql
UPDATE emp_practice
SET sal = sal * 1.05
WHERE deptno = 20;
```

### 120. 검증 가능한 변경 흐름

```sql
SELECT empno, ename, sal, ROUND(sal * 1.05, 2) AS new_sal
FROM emp_practice
WHERE deptno = 20
ORDER BY empno;

START TRANSACTION;

UPDATE emp_practice
SET sal = ROUND(sal * 1.05, 2)
WHERE deptno = 20;

SELECT ROW_COUNT() AS affected_rows;

-- 검증 결과에 따라 COMMIT 또는 ROLLBACK
```

### 121. 비교 결론

- 실행 결과뿐 아니라 의도와 위험이 Code에 보여야 한다.
- ANSI JOIN, 명시적 Column, 안정적인 ORDER BY를 사용한다.
- 경계값·NULL·중복·0행을 기본 Test Case로 둔다.
- DML은 Preview와 Transaction, 영향 Row 검증을 포함한다.
- 성능 변경은 Plan과 실제 측정으로 증명한다.

---

<a id="sql-19-section-25"></a>

## 22. 개선된 통합 예제

### 122. 요구사항

부서별로 급여 2000 이상인 사원 수와 평균 급여를 조회한다. 사원이 없는 부서도 표시하고 평균이 높은 부서부터 정렬한다.

### 123. 구조화된 Query

```sql
WITH eligible_employee AS (
    SELECT
        empno,
        deptno,
        sal
    FROM emp
    WHERE sal >= 2000
),
department_report AS (
    SELECT
        d.deptno,
        d.dname,
        COUNT(e.empno) AS employee_count,
        ROUND(AVG(e.sal), 2) AS avg_salary
    FROM dept AS d
    LEFT JOIN eligible_employee AS e
        ON e.deptno = d.deptno
    GROUP BY
        d.deptno,
        d.dname
)
SELECT
    deptno,
    dname,
    employee_count,
    avg_salary
FROM department_report
ORDER BY
    avg_salary IS NULL,
    avg_salary DESC,
    deptno;
```

### 124. 구성 이유

```text
eligible_employee
→ Row Filtering 단계

department_report
→ LEFT JOIN과 Grouping 단계

Main Query
→ 최종 표시와 정렬 단계
```

### 125. NULL 평균 처리

사원이 없는 부서의 평균은 0이 아니라 계산 대상 없음이므로 `NULL`을 유지하고 마지막에 정렬한다.

---

<a id="sql-19-section-26"></a>

## 23. 실무 Code Review 절차

### 126. 요구사항 확인

한 Row의 의미, 필수 Column, 중복, NULL, 정렬, Paging 조건을 문장으로 확인한다.

### 127. Schema 확인

PK, FK, Nullability, 자료형, Index, Cardinality를 확인한다.

### 128. Correctness Review

경계값, NULL, 0행, 다중 일치, 동점, 중복 경로를 Test한다.

### 129. Safety Review

DML 대상, Transaction, Cascade, 암시적 Commit, 재실행 결과를 검토한다.

### 130. Performance Review

실제 Parameter 범위로 EXPLAIN과 측정을 수행하고 반환 Data 크기를 확인한다.

### 131. 운영 Review

Timeout, Lock, Monitoring, Rollback, Version·설정 차이, 개인정보 Log를 확인한다.

---

<a id="sql-19-section-27"></a>

## 24. 자주 하는 실수

### 132. Formatting만 좋은 SQL을 좋은 SQL로 평가한다

정확성, 안전성, 실행 계획이 먼저다.

### 133. 지나치게 짧은 Alias를 남발한다

Table이 많거나 Self Join이면 역할을 잃는다.

### 134. 모든 Logic을 한 Query에 압축한다

CTE나 단계별 검증으로 이해 가능한 단위로 나눈다.

### 135. DISTINCT로 중복을 제거하고 원인을 끝낸다

관계 Cardinality와 JOIN 조건을 확인한다.

### 136. 날짜 끝값에 23:59:59를 사용한다

정밀도가 더 높은 Timestamp Row를 누락할 수 있으므로 다음 구간 시작 미만을 사용한다.

### 137. Parameter Binding 없이 SQL을 조합한다

Injection과 Quoting 오류를 만든다.

### 138. EXPLAIN만 보고 실제 실행이 빠르다고 단정한다

Estimate와 Runtime은 다를 수 있다.

### 139. 환경의 느슨한 SQL_MODE에 의존한다

운영 또는 Version 변경 시 오류·다른 결과가 발생할 수 있다.

---

<a id="sql-19-section-28"></a>

## 25. 디버깅 방법

### 140. Query를 Clause 단위로 줄인다

`FROM + JOIN`부터 Row 수를 확인하고 WHERE, Grouping, HAVING, 정렬을 순서대로 추가한다.

### 141. Key와 중간 계산값을 표시한다

숨겨진 Join Key, CASE Boolean, 경계값, 원본·변환 날짜를 함께 조회한다.

### 142. COUNT를 단계별로 기록한다

각 CTE와 JOIN 전후 Row 수를 비교해 중복·누락 지점을 찾는다.

### 143. NULL Test Data를 만든다

NULL, 0, 빈 문자열, 미일치 FK, 사원이 없는 부서 같은 Case를 검증한다.

### 144. 동점과 안정적 정렬을 확인한다

ORDER BY 값이 같은 Row를 만들고 PK Tie-breaker가 있는지 본다.

<a id="index-section-185"></a>

### 145. SQL_MODE와 Session 상태를 기록한다

```sql
SELECT
    VERSION() AS mariadb_version,
    @@sql_mode AS sql_mode,
    @@time_zone AS session_time_zone,
    @@autocommit AS autocommit_mode;
```

### 146. 최소 재현 Query를 만든다

불필요한 Column·Join·조건을 제거해 오류가 남는 가장 작은 SQL과 Sample Data로 분리한다.

---

<a id="sql-19-section-29"></a>

## 26. 종합실습

### 147. 문제 1 — Formatting 개선

쉼표 Join, `SELECT *`, 한 줄 조건으로 작성된 사원·부서 Query를 ANSI JOIN과 명시적 Column으로 개선한다.

### 148. 문제 2 — 날짜 조건 개선

`DATE(created_at) = '2026-08-14'` 조건을 반열린 날짜·시간 범위로 바꾼다.

### 149. 문제 3 — 안전한 UPDATE

30번 부서 사원의 급여를 3% 인상하는 Preview, Transaction, 영향 Row 검증 흐름을 작성한다.

### 150. 문제 4 — NULL 안전 Anti Join

사원이 없는 부서를 `NOT EXISTS`와 `LEFT JOIN ... IS NULL` 두 방식으로 작성한다.

### 151. 문제 5 — Code Review

부서별 평균 급여 Query에서 잘못된 Grouping, 불안정한 정렬, 불필요한 `SELECT *`, 강제 Index가 있는지 검토한다.

---

<a id="sql-19-section-30"></a>

## 27. 정답과 해설

### 152. 문제 1 정답

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
    ON d.deptno = e.deptno
WHERE e.sal >= 2000
ORDER BY e.sal DESC, e.empno;
```

### 153. 문제 2 정답

```sql
WHERE created_at >= '2026-08-14 00:00:00'
  AND created_at <  '2026-08-15 00:00:00'
```

Column에 함수를 적용하지 않고 모든 시간 정밀도를 포함한다.

### 154. 문제 3 정답

```sql
SELECT empno, ename, sal, ROUND(sal * 1.03, 2) AS new_sal
FROM emp_practice
WHERE deptno = 30
ORDER BY empno;

START TRANSACTION;

UPDATE emp_practice
SET sal = ROUND(sal * 1.03, 2)
WHERE deptno = 30;

SELECT ROW_COUNT() AS affected_rows;

SELECT empno, ename, sal
FROM emp_practice
WHERE deptno = 30
ORDER BY empno;

-- 검증 후 COMMIT, 문제 시 ROLLBACK
```

### 155. 문제 4 정답

```sql
SELECT d.deptno, d.dname
FROM dept AS d
WHERE NOT EXISTS (
    SELECT 1
    FROM emp AS e
    WHERE e.deptno = d.deptno
);
```

```sql
SELECT d.deptno, d.dname
FROM dept AS d
LEFT JOIN emp AS e
    ON e.deptno = d.deptno
WHERE e.empno IS NULL;
```

### 156. 문제 5 해설

- SELECT 일반 Column과 `GROUP BY`가 일치하는지 확인한다.
- `ORDER BY avg_salary DESC, deptno`처럼 Tie-breaker를 둔다.
- 필요한 Result Column만 선택한다.
- `FORCE INDEX` 전에 EXPLAIN, 통계, Index 설계와 실제 측정을 검토한다.
- JOIN 전후 Row 수로 평균이 중복 때문에 부풀지 않았는지 확인한다.

---

<a id="sql-19-section-31"></a>

## 28. 최종 체크리스트

### 157. 읽기·정확성 체크

- [ ] 한 Result Row의 의미를 한 문장으로 설명할 수 있는가?
- [ ] Identifier·Alias·Formatting이 일관적인가?
- [ ] JOIN Cardinality, NULL, 경계값, 동점을 검증했는가?
- [ ] 정렬이 필요하면 명시적이고 안정적인 ORDER BY가 있는가?

### 158. 안전성 체크

- [ ] 값은 Parameter Binding하는가?
- [ ] DML 전에 대상 Preview와 예상 Row를 확인했는가?
- [ ] 모든 Transaction 종료 경로가 처리되는가?
- [ ] DDL·Cascade·재실행의 영향을 검토했는가?

### 159. 성능·운영 체크

- [ ] 실제 Data 범위에서 EXPLAIN과 측정을 수행했는가?
- [ ] 과도한 Result와 N+1 Query 가능성을 확인했는가?
- [ ] Index 읽기 이점과 DML 비용을 함께 평가했는가?
- [ ] Version, SQL_MODE, Time Zone, Collation 차이를 확인했는가?

---

<a id="sql-19-section-32"></a>

## 29. 핵심 요약

### 160. 실무 SQL 핵심 문장

```text
좋은 SQL
→ 정확하고 읽기 쉬우며 안전하고 측정 가능

Formatting
→ Clause와 역할을 시각적으로 분리

JOIN
→ 관계는 ON, Filtering은 WHERE, Cardinality 확인

NULL·날짜
→ 3-valued logic과 반열린 시간 범위 고려

DML
→ Preview → Transaction → 영향 Row·값 검증

성능
→ EXPLAIN + 실제 측정, Hint는 최후 수단

협업
→ 팀 Convention과 Code Review Checklist 유지
```

### 161. 최종 정리

실무 SQL의 품질은 짧거나 화려한 문법이 아니라 **다른 사람이 결과와 위험을 검증할 수 있는가**로 결정된다. 한 Row의 의미와 관계를 먼저 정의하고, NULL·경계값·중복을 Test하며, 변경 문장은 Preview와 Transaction으로 보호한다. 성능은 Index 추측이 아니라 실행 계획과 운영 규모의 측정으로 증명하고, 이 모든 기준을 팀의 Review 절차로 반복한다.

---

<a id="sql-19-section-33"></a>

## 📎 다음 문서

다음 문서는 SQL 01~19의 개념을 하나의 Scenario로 해결하는 종합실습이다.

```text
20_SQL_종합실습.md
```

---

<a id="sql-19-section-34"></a>

## 🔬 V3 백과사전식 SQL 작성 절차

자연어 요구사항:

```text
20·30번 부서에서 급여 1500 이상인 사원의
부서별 인원과 평균 급여를 구하고
평균 급여가 높은 순서로 보여 주세요.
```

분해:

```text
기준 Table → EMP
대상 Row   → DEPTNO IN (20, 30), SAL >= 1500
Group      → DEPTNO
출력       → DEPTNO, COUNT(*), AVG(SAL)
정렬       → AVG(SAL) DESC, DEPTNO ASC
```

```sql
SELECT
    e.deptno,
    COUNT(*) AS employee_count,
    ROUND(AVG(e.sal), 2) AS average_salary
FROM emp AS e
WHERE e.deptno IN (20, 30)
  AND e.sal >= 1500
GROUP BY e.deptno
ORDER BY average_salary DESC, e.deptno ASC;
```

단계별로 `FROM·WHERE → GROUP BY·COUNT → AVG → ORDER BY` 순서로 추가하며 중간 Row와 Group 수를 기록한다.

### 원본으로 돌아가기

`Script.sql`에서 Keyword 한 줄만 찾지 말고 앞의 문제 Comment, 입력 Data 확인 Query와 다음 Result 확인 Query를 함께 읽는다.

```text
SELECT 문제 → 예상 Column·Row 기록
DML 문제   → 같은 WHERE의 SELECT 선행
JOIN 문제  → 각 Table과 관계 Column 확인
집계 문제  → Group 전 대상 Row 확인
성능 문제  → EXPLAIN 전후 비교
```

### Review 질문

- NULL·중복·0행·경계값·동점을 예상했는가?
- JOIN으로 Row가 증가하거나 사라지지 않는가?
- WHERE 없는 UPDATE·DELETE가 아닌가?
- Parameter Binding을 사용하는가?
- Transaction 경계가 업무 단위와 같은가?
- Index는 실행 계획으로 검증했는가?
- 다음 학습자가 입력부터 결과까지 재현할 수 있는가?
