# 18. SQL Recursive CTE

> 반복되는 숫자·날짜와 부모–자식 계층을 하나의 Query로 탐색하는 방법

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | `WITH RECURSIVE`, Anchor Member, Recursive Member, 계층·Sequence |
| 기준 DBMS | MariaDB |
| 실습 Table | `EMP`, `CATEGORY_PRACTICE` |
| 선수 학습 | CTE, `UNION ALL`, Self Join, `CASE`, 문자열·날짜 함수 |
| 다음 학습 | SQL 실무 코딩 스타일 |
| 문서 버전 | V3 Encyclopedia |

> 원본 `Script.sql`의 Index와 AUTO_INCREMENT 다음 Recursive CTE 범위를 기준으로 구성했다. `EMP.MGR → EMP.EMPNO` 관계를 이용해 조직 계층을 탐색하고 무한 재귀·자료형 확장 문제까지 MariaDB 기준으로 보완했다.

---

## 🎯 학습 목표

- 일반 CTE와 Recursive CTE의 차이를 설명한다.
- Anchor Member와 Recursive Member의 역할을 구분한다.
- 종료 조건이 새 Row를 만들지 못할 때 재귀가 끝나는 원리를 이해한다.
- 숫자·날짜 Sequence를 안전한 상한과 함께 생성한다.
- 조직·Category 계층의 깊이, 경로, Root를 조회한다.
- 순환 Data와 중복 경로 때문에 생기는 무한 반복을 방지한다.
- Anchor에서 재귀 Column의 자료형과 길이를 충분히 정의한다.
- `max_recursive_iterations`를 안전장치로 이해하고 논리 오류를 먼저 수정한다.

---

## 1. CTE 기본 개념

### 1. Query 안의 이름 있는 임시 결과

```sql
WITH high_salary AS (
    SELECT empno, ename, sal
    FROM emp
    WHERE sal >= 3000
)
SELECT *
FROM high_salary
ORDER BY empno;
```

### 2. CTE는 해당 문장에서만 존재한다

실제 영구 Table이나 View를 생성하지 않는다.

### 3. Derived Table보다 의미를 드러내기 쉽다

복잡한 중간 결과에 이름을 붙이고 Main Query에서 Table처럼 참조한다.

### 4. 일반 CTE는 자신을 참조하지 않는다

```text
Non-recursive CTE
→ 한 번 계산되는 이름 있는 Query 결과

Recursive CTE
→ CTE가 자신의 이전 결과를 참조하며 반복
```

---

## 2. Recursive CTE 구조

### 5. 기본 문법

```sql
WITH RECURSIVE cte_name (column_list) AS (
    anchor_query

    UNION ALL

    recursive_query
)
SELECT *
FROM cte_name;
```

### 6. Anchor Member

반복의 시작 Row를 만든다. CTE 자신을 참조하지 않는다.

### 7. Recursive Member

직전 반복에서 만들어진 CTE Row를 참조해 다음 Row를 만든다.

### 8. UNION ALL로 두 Member를 연결한다

Anchor 결과와 재귀 반복 결과를 하나로 모은다.

### 9. 종료 원리

Recursive Member가 더 이상 새 Row를 반환하지 않으면 반복이 끝난다.

### 10. 실행 흐름

```text
1. Anchor 실행
2. Anchor 결과로 Recursive Member 실행
3. 새 결과로 다시 Recursive Member 실행
4. 새 Row가 없으면 종료
5. 누적 Result 반환
```

---

## 3. 숫자 Sequence

### 11. 1부터 10까지 생성

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 10
)
SELECT n
FROM numbers;
```

### 12. Anchor는 1이다

```sql
SELECT 1 AS n
```

### 13. 다음 값은 n + 1이다

```sql
SELECT n + 1
FROM numbers
```

### 14. `WHERE n < 10`이 종료 조건이다

현재 값이 10이면 더 이상 11을 생성하지 않는다.

### 15. 경계값을 직접 계산한다

조건은 현재 Row에 적용된다. `n <= 10`으로 작성하면 11까지 생성될 수 있다.

### 16. 증가값 변경

```sql
WITH RECURSIVE even_numbers AS (
    SELECT 2 AS n
    UNION ALL
    SELECT n + 2
    FROM even_numbers
    WHERE n < 20
)
SELECT n FROM even_numbers;
```

---

## 4. 시작값·끝값 Parameter

### 17. Session 변수 활용 예제

```sql
SET @start_no = 5;
SET @end_no = 12;

WITH RECURSIVE numbers AS (
    SELECT @start_no AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < @end_no
)
SELECT n FROM numbers;
```

### 18. 시작값이 끝값보다 큰 경우

Anchor는 조건과 무관하게 한 Row를 만들 수 있다. 잘못된 입력에서도 시작값이 나오는지 확인한다.

### 19. Anchor에도 유효성 조건 적용

```sql
WITH RECURSIVE numbers AS (
    SELECT @start_no AS n
    WHERE @start_no <= @end_no
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < @end_no
)
SELECT n FROM numbers;
```

### 20. Application Parameter는 Binding한다

문자열 조합으로 SQL을 만들지 말고 Prepared Statement Parameter를 사용한다.

---

## 5. 날짜 Sequence

### 21. 날짜 범위 생성

```sql
WITH RECURSIVE calendar AS (
    SELECT DATE('2026-08-01') AS calendar_date

    UNION ALL

    SELECT calendar_date + INTERVAL 1 DAY
    FROM calendar
    WHERE calendar_date < '2026-08-07'
)
SELECT calendar_date
FROM calendar;
```

### 22. DATE 자료형을 유지한다

표시 문자열이 아니라 날짜 계산 가능한 값으로 생성한다.

### 23. 월 단위 Sequence

```sql
WITH RECURSIVE months AS (
    SELECT DATE('2026-01-01') AS month_start
    UNION ALL
    SELECT month_start + INTERVAL 1 MONTH
    FROM months
    WHERE month_start < '2026-12-01'
)
SELECT DATE_FORMAT(month_start, '%Y-%m') AS year_month
FROM months;
```

### 24. Calendar와 집계를 LEFT JOIN한다

```sql
WITH RECURSIVE calendar AS (
    SELECT DATE('2026-08-01') AS calendar_date
    UNION ALL
    SELECT calendar_date + INTERVAL 1 DAY
    FROM calendar
    WHERE calendar_date < '2026-08-07'
)
SELECT
    c.calendar_date,
    COUNT(e.empno) AS hire_count
FROM calendar AS c
LEFT JOIN emp AS e
    ON e.hiredate = c.calendar_date
GROUP BY c.calendar_date
ORDER BY c.calendar_date;
```

### 25. Data가 없는 날짜도 0으로 표시한다

Calendar가 왼쪽 기준이므로 일치하는 Data가 없어도 날짜 Row는 보존된다.

---

## 6. 문자열과 반복

### 26. 반복 문자열 만들기

```sql
WITH RECURSIVE levels AS (
    SELECT 1 AS level_no, CAST('*' AS CHAR(20)) AS marker
    UNION ALL
    SELECT level_no + 1, CONCAT(marker, '*')
    FROM levels
    WHERE level_no < 5
)
SELECT level_no, marker
FROM levels;
```

### 27. Anchor에서 길이를 넉넉히 CAST한다

재귀 Column의 자료형과 길이는 Anchor 결과를 기준으로 정해진다.

### 28. Anchor 길이가 짧으면 오류 또는 잘림 위험이 있다

```sql
-- Anchor의 '*' 길이보다 재귀 결과가 길어진다.
-- SELECT 1, '*'
-- UNION ALL
-- SELECT level_no + 1, CONCAT(marker, '*') ...
```

현대 MariaDB Version은 손실 가능한 불일치를 오류로 감지할 수 있다.

### 29. 숫자 범위도 Anchor 자료형을 확인한다

재귀 계산 결과가 `INT` 범위를 넘을 가능성이 있으면 Anchor에서 `CAST(... AS BIGINT)` 등으로 넓힌다.

---

## 7. 조직 계층 Data

### 30. EMP의 자기 참조 관계

```text
EMP.EMPNO
→ 사원 식별자

EMP.MGR
→ 관리자 EMPNO
```

### 31. Root 사원

최상위 사원은 일반적으로 `MGR IS NULL`이다.

```sql
SELECT empno, ename, mgr
FROM emp
WHERE mgr IS NULL;
```

### 32. 직접 부하 직원

```sql
SELECT empno, ename, mgr
FROM emp
WHERE mgr = 7839;
```

### 33. Self Join은 고정 한 단계다

Self Join을 여러 번 이어 쓰면 정해진 깊이는 조회할 수 있지만 조직 깊이가 가변적이면 Recursive CTE가 적합하다.

---

## 8. 전체 조직도 조회

### 34. 기본 Recursive CTE

```sql
WITH RECURSIVE org AS (
    SELECT
        empno,
        ename,
        mgr,
        1 AS depth
    FROM emp
    WHERE mgr IS NULL

    UNION ALL

    SELECT
        child.empno,
        child.ename,
        child.mgr,
        parent.depth + 1
    FROM emp AS child
    JOIN org AS parent
        ON child.mgr = parent.empno
)
SELECT empno, ename, mgr, depth
FROM org
ORDER BY depth, mgr, empno;
```

### 35. Anchor는 최상위 사원이다

```sql
WHERE mgr IS NULL
```

### 36. Recursive Member는 자식을 찾는다

```sql
ON child.mgr = parent.empno
```

### 37. 깊이는 부모 + 1

Root를 1로 시작하면 직속 부하는 2, 다음 단계는 3이 된다.

### 38. CTE Column 목록을 명시할 수 있다

```sql
WITH RECURSIVE org (empno, ename, mgr, depth) AS (
    ...
)
SELECT * FROM org;
```

### 39. 최종 ORDER BY가 표시 순서를 정한다

재귀 생성 순서가 원하는 조직도 표시 순서를 자동 보장한다고 가정하지 않는다.

---

## 9. 들여쓰기와 경로

### 40. 깊이에 따른 들여쓰기

```sql
WITH RECURSIVE org AS (
    SELECT empno, ename, mgr, 1 AS depth
    FROM emp
    WHERE mgr IS NULL
    UNION ALL
    SELECT child.empno, child.ename, child.mgr, parent.depth + 1
    FROM emp AS child
    JOIN org AS parent ON child.mgr = parent.empno
)
SELECT
    empno,
    CONCAT(REPEAT('  ', depth - 1), ename) AS hierarchy_name,
    depth
FROM org
ORDER BY depth, empno;
```

### 41. 이름 경로 만들기

```sql
WITH RECURSIVE org AS (
    SELECT
        empno,
        ename,
        mgr,
        1 AS depth,
        CAST(ename AS CHAR(500)) AS name_path
    FROM emp
    WHERE mgr IS NULL

    UNION ALL

    SELECT
        child.empno,
        child.ename,
        child.mgr,
        parent.depth + 1,
        CONCAT(parent.name_path, ' > ', child.ename)
    FROM emp AS child
    JOIN org AS parent
        ON child.mgr = parent.empno
)
SELECT empno, ename, depth, name_path
FROM org;
```

### 42. ID 경로는 안정적인 식별에 유용하다

```sql
CAST(CONCAT('/', empno, '/') AS CHAR(1000)) AS id_path
```

이름은 중복·변경될 수 있으므로 Cycle 검사와 정렬에는 ID 경로가 더 안전하다.

### 43. 경로 길이를 충분히 확보한다

예상 최대 깊이와 ID·이름 길이를 계산해 Anchor에서 `CAST`한다.

### 44. 표시 경로와 검색 경로를 분리한다

사용자용 `name_path`와 검증용 `id_path`는 목적이 다르다.

---

## 10. 특정 Root의 하위 조직

### 45. 특정 사원을 Anchor로 선택한다

```sql
WITH RECURSIVE sub_org AS (
    SELECT empno, ename, mgr, 0 AS relative_depth
    FROM emp
    WHERE empno = 7566

    UNION ALL

    SELECT
        child.empno,
        child.ename,
        child.mgr,
        parent.relative_depth + 1
    FROM emp AS child
    JOIN sub_org AS parent
        ON child.mgr = parent.empno
)
SELECT *
FROM sub_org
ORDER BY relative_depth, empno;
```

### 46. Anchor 자신도 결과에 포함된다

Root 제외가 필요하면 최종 Query에서 `WHERE relative_depth > 0`을 적용한다.

### 47. 존재하지 않는 Root면 0행이다

Anchor가 Row를 만들지 못하므로 Recursive Member도 실행할 출발점이 없다.

### 48. Parameter 유효성을 별도로 확인한다

결과 0행이 “하위 직원 없음”인지 “Root 없음”인지 구분하려면 Anchor 대상 존재를 먼저 검사한다.

---

## 11. 상위 관리자 탐색

### 49. 아래에서 위로 이동한다

```sql
WITH RECURSIVE manager_chain AS (
    SELECT empno, ename, mgr, 0 AS distance
    FROM emp
    WHERE empno = 7369

    UNION ALL

    SELECT
        manager.empno,
        manager.ename,
        manager.mgr,
        child.distance + 1
    FROM emp AS manager
    JOIN manager_chain AS child
        ON manager.empno = child.mgr
)
SELECT *
FROM manager_chain
ORDER BY distance;
```

### 50. 연결 방향이 하위 탐색과 반대다

```text
하위 탐색
→ child.mgr = parent.empno

상위 탐색
→ manager.empno = child.mgr
```

### 51. 시작 사원 제외

```sql
WHERE distance > 0
```

최종 Query에서 관리자만 남긴다.

### 52. MGR가 NULL이면 종료된다

최상위 관리자 이후 Join할 Row가 없어 재귀가 끝난다.

---

## 12. 여러 Root와 Forest

### 53. Root가 여러 개일 수 있다

```sql
WHERE mgr IS NULL
```

조건에 맞는 모든 Root가 Anchor에 들어간다.

### 54. Root ID를 함께 전달한다

```sql
WITH RECURSIVE org AS (
    SELECT
        empno,
        ename,
        mgr,
        empno AS root_empno,
        1 AS depth
    FROM emp
    WHERE mgr IS NULL

    UNION ALL

    SELECT
        child.empno,
        child.ename,
        child.mgr,
        parent.root_empno,
        parent.depth + 1
    FROM emp AS child
    JOIN org AS parent
        ON child.mgr = parent.empno
)
SELECT * FROM org
ORDER BY root_empno, depth, empno;
```

### 55. Root별 집계

```sql
SELECT root_empno, COUNT(*) AS organization_size, MAX(depth) AS max_depth
FROM org
GROUP BY root_empno;
```

이 Query는 위 CTE와 같은 문장 안에서 사용해야 한다.

---

## 13. Category Tree 예제

### 56. Category Table

```sql
CREATE TABLE category_practice (
    category_id INT NOT NULL,
    parent_id INT NULL,
    category_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (category_id),
    CONSTRAINT fk_category_parent
        FOREIGN KEY (parent_id)
        REFERENCES category_practice (category_id)
) ENGINE = InnoDB;
```

### 57. Sample Data

```sql
INSERT INTO category_practice
    (category_id, parent_id, category_name)
VALUES
    (1, NULL, '개발'),
    (2, 1, 'Backend'),
    (3, 1, 'Frontend'),
    (4, 2, 'Database'),
    (5, 2, 'API'),
    (6, 3, 'CSS');
```

### 58. Category 경로 조회

```sql
WITH RECURSIVE category_tree AS (
    SELECT
        category_id,
        parent_id,
        category_name,
        1 AS depth,
        CAST(category_name AS CHAR(500)) AS category_path
    FROM category_practice
    WHERE parent_id IS NULL

    UNION ALL

    SELECT
        child.category_id,
        child.parent_id,
        child.category_name,
        parent.depth + 1,
        CONCAT(parent.category_path, ' > ', child.category_name)
    FROM category_practice AS child
    JOIN category_tree AS parent
        ON child.parent_id = parent.category_id
)
SELECT *
FROM category_tree
ORDER BY category_path;
```

### 59. FK만으로 모든 Cycle을 막지 못한다

자기 자신을 부모로 지정하거나 여러 Row가 순환하는 관계는 별도의 Validation이 필요하다.

---

## 14. UNION ALL과 UNION

### 60. UNION ALL은 중복 Row를 유지한다

Tree처럼 각 Node에 부모가 하나이고 순환이 없다면 일반적으로 효율적이고 의도가 명확하다.

### 61. UNION은 전체 Row 중복을 제거한다

Graph 탐색에서 동일한 완전 Row가 반복되는 것을 막는 데 도움이 될 수 있다.

### 62. Depth나 Path가 달라지면 같은 Node도 다른 Row다

`UNION`을 사용해도 `depth`가 계속 변하면 순환을 차단하지 못할 수 있다.

### 63. 중복 제거를 Cycle 방지와 동일시하지 않는다

어떤 Column 조합으로 방문 여부를 판단할지 명시적으로 설계한다.

### 64. Tree와 Graph를 구분한다

한 Node에 부모가 하나인 Tree인지, 여러 경로가 가능한 Graph인지에 따라 중복 결과의 의미가 달라진다.

---

## 15. Cycle 문제

### 65. 자기 참조 Cycle

```text
사원 100의 MGR = 100
```

자신을 계속 다음 Row로 찾을 수 있다.

### 66. 여러 Node Cycle

```text
A의 부모 = B
B의 부모 = C
C의 부모 = A
```

### 67. Path로 방문 Node 확인

```sql
WITH RECURSIVE org AS (
    SELECT
        empno,
        ename,
        mgr,
        1 AS depth,
        CAST(CONCAT('/', empno, '/') AS CHAR(2000)) AS id_path
    FROM emp
    WHERE mgr IS NULL

    UNION ALL

    SELECT
        child.empno,
        child.ename,
        child.mgr,
        parent.depth + 1,
        CONCAT(parent.id_path, child.empno, '/')
    FROM emp AS child
    JOIN org AS parent
        ON child.mgr = parent.empno
    WHERE parent.id_path NOT LIKE CONCAT('%/', child.empno, '/%')
)
SELECT * FROM org;
```

### 68. 구분자를 포함해 오탐을 줄인다

ID 1을 찾다가 11과 일치하지 않도록 `/1/` 형태로 저장한다.

### 69. Path 문자열 검사는 큰 Graph에서 비용이 크다

Data Modeling, 제약, 입력 Validation, MariaDB Version의 Cycle 기능 등을 함께 검토한다.

### 70. MariaDB의 CYCLE ... RESTRICT

지원 Version에서는 완화된 MariaDB 문법으로 특정 Column의 Cycle을 제한할 수 있다.

```sql
WITH RECURSIVE graph_walk (from_id, to_id) AS (
    SELECT from_id, to_id
    FROM graph_edge
    WHERE from_id = 1
    UNION ALL
    SELECT e.from_id, e.to_id
    FROM graph_edge AS e
    JOIN graph_walk AS w
        ON e.from_id = w.to_id
)
CYCLE from_id, to_id RESTRICT
SELECT * FROM graph_walk;
```

운영 MariaDB Version과 표준 SQL 문법 차이를 확인한다.

---

## 16. 재귀 제한

### 71. 현재 제한 확인

```sql
SELECT @@max_recursive_iterations;
```

### 72. 무한 반복 방지 안전장치

Recursive Member가 계속 Row를 만들면 Server가 설정된 반복 한도에서 중단한다.

### 73. Version별 기본값이 다를 수 있다

MariaDB 10.6 이상 문서의 기본값은 1000이지만 실제 환경 값을 조회한다.

### 74. 제한을 높이기 전에 논리를 검사한다

종료 조건, Cycle, 예상 최대 깊이, Anchor 범위를 먼저 확인한다.

### 75. Session 범위 설정

```sql
SET SESSION max_recursive_iterations = 2000;
```

필요성과 Resource 영향을 검토한 경우에만 변경한다.

### 76. 작은 업무 상한을 Query에도 둔다

```sql
WHERE parent.depth < 20
```

조직 최대 깊이가 20이라는 업무 규칙이 있다면 Server 한도와 별도로 명시한다.

---

## 17. 자료형과 CAST

### 77. Anchor가 CTE Column 자료형을 결정한다

Recursive Member 결과는 Anchor가 정의한 형태에 맞아야 한다.

### 78. Path 문자열은 넓게 CAST한다

```sql
CAST(ename AS CHAR(1000)) AS name_path
```

### 79. 숫자 증가는 BIGINT 검토

```sql
CAST(1 AS SIGNED INTEGER) AS n
```

예상 범위가 크면 적합한 더 넓은 자료형을 사용한다.

### 80. Anchor와 Recursive Member의 Column 개수를 맞춘다

각 위치의 의미와 자료형도 호환되어야 한다.

### 81. NULL의 자료형을 명시할 수 있다

```sql
CAST(NULL AS SIGNED INTEGER) AS parent_id
```

복잡한 CTE에서 Column 계약을 명확히 한다.

### 82. 암시적 변환에 의존하지 않는다

경로, 날짜, 숫자 누적 결과를 의도한 자료형으로 명시한다.

---

## 18. 정렬과 탐색 순서

### 83. Recursive CTE가 출력 순서를 보장하지 않는다

최종 `ORDER BY`가 없으면 계층 생성 순서대로 표시된다고 가정하지 않는다.

### 84. Depth 중심 정렬

```sql
ORDER BY depth, empno;
```

같은 Level을 묶어 보는 Breadth-first 형태의 표시다.

### 85. Path 중심 정렬

```sql
ORDER BY id_path;
```

경로 Encoding이 정렬 가능한 형태인지 확인한다.

### 86. 숫자 ID 문자열의 사전식 정렬 문제

`/1/10/`이 `/1/2/`보다 먼저 올 수 있다. 고정 길이 Padding 또는 별도 Sort Path를 설계한다.

### 87. Sort Path 예제

```sql
CAST(LPAD(empno, 10, '0') AS CHAR(2000)) AS sort_path
```

재귀 단계에서는 부모 경로와 Padding된 ID를 결합한다.

### 88. 표시 Path와 Sort Path를 분리한다

사람이 읽는 이름 경로와 안정적인 정렬용 Key는 별도 Column으로 관리한다.

---

## 19. 집계와 계층

### 89. Level별 인원수

```sql
WITH RECURSIVE org AS (
    SELECT empno, ename, mgr, 1 AS depth
    FROM emp WHERE mgr IS NULL
    UNION ALL
    SELECT child.empno, child.ename, child.mgr, parent.depth + 1
    FROM emp AS child
    JOIN org AS parent ON child.mgr = parent.empno
)
SELECT depth, COUNT(*) AS employee_count
FROM org
GROUP BY depth
ORDER BY depth;
```

### 90. 전체 조직 깊이

```sql
SELECT MAX(depth) AS organization_depth
FROM org;
```

같은 CTE 문장 안의 Main Query로 사용한다.

### 91. 관리자별 모든 하위 인원

각 관리자를 Anchor로 별도 탐색하면 하위 인원 수를 계산할 수 있지만 Data 규모에 따라 결과가 크게 늘어난다.

### 92. 직접 부하와 전체 하위 조직을 구분한다

`WHERE mgr = manager_id`는 직접 부하만, Recursive CTE는 모든 깊이의 Descendant를 찾는다.

### 93. 중복 경로가 집계를 부풀릴 수 있다

Graph 구조에서는 한 Node가 여러 경로로 도달 가능하다. Row의 의미가 Node인지 Path인지 먼저 정한다.

---

## 20. 내 코드와 강사님 코드 비교

### 94. 종료 조건 없는 숫자 생성

```sql
-- Recursive Member가 계속 Row를 생성한다.
-- WITH RECURSIVE numbers AS (
--     SELECT 1 AS n
--     UNION ALL
--     SELECT n + 1 FROM numbers
-- )
-- SELECT * FROM numbers;
```

### 95. 명확한 상한을 둔 개선 방식

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 10
)
SELECT n FROM numbers;
```

### 96. 짧은 Anchor Path

```sql
-- 재귀 중 문자열이 길어지는 구조
-- SELECT ename AS name_path ...
```

### 97. CAST로 결과 계약을 명시

```sql
SELECT CAST(ename AS CHAR(500)) AS name_path
FROM emp
WHERE mgr IS NULL;
```

### 98. Self Join 반복 방식

```sql
SELECT employee.ename, manager.ename, senior.ename
FROM emp AS employee
LEFT JOIN emp AS manager ON manager.empno = employee.mgr
LEFT JOIN emp AS senior ON senior.empno = manager.mgr;
```

고정 2단계 조회에는 명확하지만 깊이가 변하면 JOIN을 계속 추가해야 한다.

### 99. Recursive CTE 방식

전체 깊이를 같은 구조로 반복하며 `depth`, `path`를 함께 계산할 수 있다.

### 100. 비교 결론

- 종료 조건과 최대 예상 깊이를 먼저 정한다.
- Anchor에서 재귀 결과가 성장할 자료형을 확보한다.
- Tree인지 Graph인지 확인하고 Cycle 방식을 설계한다.
- 출력 순서는 최종 `ORDER BY`로 명시한다.
- 고정 한두 단계는 Self Join이 더 단순할 수 있다.

---

## 21. 개선된 통합 예제

### 101. 안전한 조직도 CTE

```sql
WITH RECURSIVE org AS (
    SELECT
        empno,
        ename,
        mgr,
        empno AS root_empno,
        1 AS depth,
        CAST(CONCAT('/', empno, '/') AS CHAR(2000)) AS id_path,
        CAST(ename AS CHAR(2000)) AS name_path,
        CAST(LPAD(empno, 10, '0') AS CHAR(2000)) AS sort_path
    FROM emp
    WHERE mgr IS NULL

    UNION ALL

    SELECT
        child.empno,
        child.ename,
        child.mgr,
        parent.root_empno,
        parent.depth + 1,
        CONCAT(parent.id_path, child.empno, '/'),
        CONCAT(parent.name_path, ' > ', child.ename),
        CONCAT(parent.sort_path, '/', LPAD(child.empno, 10, '0'))
    FROM emp AS child
    JOIN org AS parent
        ON child.mgr = parent.empno
    WHERE parent.depth < 20
      AND parent.id_path NOT LIKE CONCAT('%/', child.empno, '/%')
)
SELECT
    empno,
    CONCAT(REPEAT('  ', depth - 1), ename) AS hierarchy_name,
    mgr,
    root_empno,
    depth,
    name_path
FROM org
ORDER BY sort_path;
```

### 102. 안전장치의 역할

```text
depth < 20
→ 업무 최대 깊이

id_path NOT LIKE ...
→ 현재 경로에서 같은 ID 재방문 방지

CAST(... CHAR(2000))
→ 재귀 중 늘어나는 경로 길이 확보

sort_path
→ 안정적인 계층 표시 순서
```

### 103. 누락된 계층 Data 찾기

```sql
SELECT child.empno, child.ename, child.mgr
FROM emp AS child
LEFT JOIN emp AS manager
    ON manager.empno = child.mgr
WHERE child.mgr IS NOT NULL
  AND manager.empno IS NULL;
```

Recursive CTE 실행 전에 존재하지 않는 부모 참조를 진단한다.

---

## 22. 실무 활용 지침

### 104. 출발점과 이동 방향을 문장으로 적는다

```text
Root에서 Descendant로 내려가는가?
특정 Node에서 Ancestor로 올라가는가?
```

### 105. 한 Result Row의 의미를 정한다

한 Node인지, 한 경로인지, Root–Descendant 관계인지에 따라 중복 제거와 집계가 달라진다.

### 106. 예상 최대 깊이와 최대 Result 수를 계산한다

Graph의 분기 수가 크면 깊이가 작아도 Row 수가 폭발할 수 있다.

### 107. 입력 단계에서 계층 무결성을 검증한다

존재하는 부모, 자기 참조 금지, Cycle 금지 규칙을 Application과 Database 설계에 반영한다.

### 108. Server 제한은 마지막 안전망이다

`max_recursive_iterations`에 의존해 잘못된 Query를 정상 종료시키지 않는다.

### 109. 자주 조회하는 계층은 Modeling을 검토한다

Adjacency List 외에 Closure Table, Materialized Path 등 읽기·쓰기 Pattern에 맞는 구조를 검토할 수 있다.

### 110. 실행 계획과 실제 크기를 측정한다

Parent Key Index, Anchor 선택도, 각 Level Row 수, Path 계산 비용을 확인한다.

---

## 23. 자주 하는 실수

### 111. WITH에서 RECURSIVE를 빠뜨린다

CTE가 자신을 참조한다면 `WITH RECURSIVE`를 사용한다.

### 112. 종료 조건을 빠뜨리거나 경계를 잘못 쓴다

숫자 Sequence에서 마지막 값과 다음 생성값을 직접 대입해 본다.

### 113. Anchor와 Recursive Column 수가 다르다

`UNION ALL` 양쪽 SELECT의 개수와 위치를 맞춘다.

### 114. Anchor 문자열 길이가 너무 짧다

경로가 늘어날 수 있도록 `CAST`로 충분한 길이를 정의한다.

### 115. EMP Join 방향을 반대로 쓴다

하위 탐색은 `child.mgr = parent.empno`다.

### 116. UNION만으로 Cycle을 해결하려 한다

Depth·Path가 바뀌면 동일 Node도 다른 Row가 된다.

### 117. 재귀 제한만 크게 올린다

무한 반복이 더 오래 실행되어 Resource만 더 소비할 수 있다.

### 118. 결과가 생성 순서대로 나온다고 가정한다

최종 `ORDER BY`와 안정적인 Sort Key를 사용한다.

### 119. CTE를 영구 결과로 생각한다

CTE는 해당 SQL 문장에서만 참조할 수 있다.

---

## 24. 디버깅 방법

### 120. Anchor만 실행한다

```sql
SELECT empno, ename, mgr
FROM emp
WHERE mgr IS NULL;
```

### 121. 한 단계 Self Join으로 관계 확인

```sql
SELECT parent.empno, child.empno, child.mgr
FROM emp AS parent
JOIN emp AS child
    ON child.mgr = parent.empno
ORDER BY parent.empno, child.empno;
```

### 122. 임시 Depth 상한을 작게 둔다

```sql
WHERE parent.depth < 3
```

각 Level이 어떻게 늘어나는지 관찰한다.

### 123. Level별 Row 수를 집계한다

```sql
SELECT depth, COUNT(*) AS row_count
FROM org
GROUP BY depth
ORDER BY depth;
```

같은 CTE 문장 안에서 실행한다.

### 124. ID Path를 출력한다

같은 Node가 반복되거나 Cycle이 있는지 확인한다.

### 125. 고아 Node를 찾는다

부모 Key가 있지만 실제 부모 Row가 없는 Data를 Anti Join으로 확인한다.

### 126. 현재 재귀 제한 확인

```sql
SELECT @@max_recursive_iterations;
```

### 127. 자료형 오류 시 Anchor CAST를 확인한다

Recursive Member가 만드는 최대 문자열 길이와 숫자 범위를 계산한다.

### 128. EXPLAIN 사용

```sql
EXPLAIN
WITH RECURSIVE org AS (
    SELECT empno, mgr, 1 AS depth
    FROM emp WHERE mgr IS NULL
    UNION ALL
    SELECT child.empno, child.mgr, parent.depth + 1
    FROM emp AS child
    JOIN org AS parent ON child.mgr = parent.empno
)
SELECT * FROM org;
```

지원 범위와 출력은 MariaDB Version에 따라 확인한다.

---

## 25. 종합실습

### 129. 문제 1 — 숫자 Sequence

1부터 20까지 정수를 Recursive CTE로 생성한다.

### 130. 문제 2 — 날짜 Calendar

2026-08-01부터 2026-08-14까지 날짜를 하루 단위로 생성한다.

### 131. 문제 3 — 전체 조직도

`EMP`의 Root부터 모든 사원을 조회하고 깊이와 들여쓴 이름을 표시한다.

### 132. 문제 4 — 특정 사원의 관리자 Chain

7369번 사원부터 최상위 관리자까지 거리와 함께 조회한다.

### 133. 문제 5 — 경로와 Cycle 방지

조직도에 ID 경로와 이름 경로를 추가하고 현재 경로에 이미 있는 사원을 다시 방문하지 않도록 한다.

---

## 26. 정답과 해설

### 134. 문제 1 정답

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 20
)
SELECT n
FROM numbers;
```

### 135. 문제 2 정답

```sql
WITH RECURSIVE calendar AS (
    SELECT DATE('2026-08-01') AS calendar_date
    UNION ALL
    SELECT calendar_date + INTERVAL 1 DAY
    FROM calendar
    WHERE calendar_date < '2026-08-14'
)
SELECT calendar_date
FROM calendar;
```

### 136. 문제 3 정답

```sql
WITH RECURSIVE org AS (
    SELECT empno, ename, mgr, 1 AS depth
    FROM emp
    WHERE mgr IS NULL
    UNION ALL
    SELECT child.empno, child.ename, child.mgr, parent.depth + 1
    FROM emp AS child
    JOIN org AS parent
        ON child.mgr = parent.empno
)
SELECT
    empno,
    CONCAT(REPEAT('  ', depth - 1), ename) AS hierarchy_name,
    mgr,
    depth
FROM org
ORDER BY depth, mgr, empno;
```

### 137. 문제 4 정답

```sql
WITH RECURSIVE manager_chain AS (
    SELECT empno, ename, mgr, 0 AS distance
    FROM emp
    WHERE empno = 7369
    UNION ALL
    SELECT manager.empno, manager.ename, manager.mgr, child.distance + 1
    FROM emp AS manager
    JOIN manager_chain AS child
        ON manager.empno = child.mgr
)
SELECT empno, ename, mgr, distance
FROM manager_chain
ORDER BY distance;
```

### 138. 문제 5 정답

```sql
WITH RECURSIVE org AS (
    SELECT
        empno,
        ename,
        mgr,
        1 AS depth,
        CAST(CONCAT('/', empno, '/') AS CHAR(2000)) AS id_path,
        CAST(ename AS CHAR(2000)) AS name_path
    FROM emp
    WHERE mgr IS NULL

    UNION ALL

    SELECT
        child.empno,
        child.ename,
        child.mgr,
        parent.depth + 1,
        CONCAT(parent.id_path, child.empno, '/'),
        CONCAT(parent.name_path, ' > ', child.ename)
    FROM emp AS child
    JOIN org AS parent
        ON child.mgr = parent.empno
    WHERE parent.depth < 20
      AND parent.id_path NOT LIKE CONCAT('%/', child.empno, '/%')
)
SELECT empno, ename, mgr, depth, id_path, name_path
FROM org
ORDER BY id_path;
```

---

## 27. 최종 체크리스트

### 139. 구조 체크

- [ ] `WITH RECURSIVE`를 사용했는가?
- [ ] Anchor가 올바른 시작 Row를 반환하는가?
- [ ] Recursive Member가 CTE를 정확한 방향으로 참조하는가?
- [ ] 양쪽 SELECT의 Column 개수·위치·자료형이 맞는가?

### 140. 종료·안전 체크

- [ ] 새 Row 생성을 멈추는 종료 조건이 있는가?
- [ ] Cycle이 가능한 Data인지 확인했는가?
- [ ] 업무 Depth 상한과 Server 반복 제한을 확인했는가?
- [ ] Graph의 Result Row 폭증 가능성을 계산했는가?

### 141. 결과 품질 체크

- [ ] 성장하는 Path와 숫자에 충분한 Anchor 자료형을 지정했는가?
- [ ] Node와 Path 중 한 Row의 의미가 명확한가?
- [ ] 최종 `ORDER BY`와 안정적인 Sort Path가 있는가?
- [ ] 고아 Node와 잘못된 부모 관계를 사전 검증했는가?

---

## 28. 핵심 요약

### 142. Recursive CTE 핵심 문장

```text
Anchor Member
→ 최초 시작 Row

Recursive Member
→ 이전 결과를 참조해 다음 Row 생성

종료
→ Recursive Member가 새 Row를 만들지 못할 때

UNION ALL
→ Anchor와 모든 반복 결과 누적

계층 이동
→ child.parent_id = parent.id

CAST
→ Anchor에서 성장할 Column의 자료형·길이 확보

max_recursive_iterations
→ 무한 반복 방지용 Server 안전장치
```

### 143. 최종 정리

Recursive CTE의 핵심은 반복 문법이 아니라 **출발점, 다음 Row를 찾는 관계, 종료 조건**을 정확히 정의하는 것이다. 숫자와 날짜에는 명확한 상한을 두고, 계층에는 이동 방향·최대 깊이·Cycle 방지를 설계한다. 경로나 누적값이 성장하면 Anchor에서 충분한 자료형을 지정하고, 최종 출력 순서는 별도의 Sort Path와 `ORDER BY`로 보장한다.

---

## 📎 다음 문서

다음 단계는 지금까지 학습한 SQL을 유지보수 가능한 형태로 정리하는 실무 코딩 스타일이다.

```text
19_SQL_실무_코딩스타일.md
```

---

## 🔬 V3 동작 백과 — 재귀 Result는 반복마다 어떻게 늘어나는가?

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 5
)
SELECT n FROM numbers;
```

```text
Anchor → 1
1차 → 2
2차 → 3
3차 → 4
4차 → 5
다음 n < 5 False → 종료
```

최종 Result는 `1, 2, 3, 4, 5`다.

조직도에서는 Anchor가 최상위 Row를 만들고, Recursive Member가 이전 단계의 `EMPNO`와 다음 사원의 `MGR`을 연결하면서 Level과 Path를 늘린다.

종료 조건이나 관계가 잘못되면 Cycle과 과도한 반복이 발생한다. Path가 길어질 때는 Anchor에서 충분한 길이로 `CAST`한다.

```sql
CAST(ename AS CHAR(1000)) AS path
```

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 Anchor | 강사님 코드 Anchor |
| --- | --- | --- |
| 재귀 시작 | `with recursive emp_recu` | 같은 Query |
| Anchor | CTE의 첫 SELECT | 같은 위치 |
| 반복 Member | `union all` 뒤 SELECT | 같은 위치 |
| 조직 연결 | `mgr`, `empno` 관계 | 계층 Query |

작은 종료값과 Level·Path Column을 출력해 반복 단계를 먼저 확인한다.
