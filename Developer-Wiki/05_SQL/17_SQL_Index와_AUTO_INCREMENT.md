# 17. SQL Index와 AUTO_INCREMENT

> 검색 경로를 최적화하고 새로운 Row의 식별자를 자동 생성하는 방법

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | Index, Composite Index, `EXPLAIN`, `AUTO_INCREMENT`, `LAST_INSERT_ID()` |
| 기준 DBMS | MariaDB, InnoDB |
| 실습 Table | `EMP_INDEX_TEST`, `BOARD_PRACTICE` |
| 선수 학습 | PK·Unique·FK, DML, Transaction |
| 다음 학습 | Recursive CTE |
| 문서 버전 | V2 |

> 원본 `Script.sql`에서 Transaction 다음에 이어지는 Index, Index Hint, AUTO_INCREMENT 범위를 기준으로 구성했다. Index는 “만들면 무조건 빨라지는 기능”이 아니며 실행 계획과 실제 Data로 검증한다.

---

## 🎯 학습 목표

- Index의 역할과 읽기·쓰기 비용의 Trade-off를 설명한다.
- Primary·Unique·일반·복합 Index를 목적에 맞게 구분한다.
- 복합 Index의 Column 순서와 왼쪽 Prefix 원리를 이해한다.
- `SHOW INDEX`와 `EXPLAIN`으로 Index 후보와 실제 선택을 확인한다.
- Index Hint를 최후 수단으로 사용해야 하는 이유를 설명한다.
- AUTO_INCREMENT Column을 설계하고 생성된 값을 안전하게 조회한다.
- 삭제·실패·Rollback 때문에 번호 사이에 Gap이 생길 수 있음을 이해한다.

---

## 1. Index 기본 개념

### 1. Index는 검색을 위한 별도 자료구조다

책의 색인처럼 조건에 맞는 Row 위치를 빠르게 찾도록 돕는다.

### 2. Index가 없으면 많은 Row를 확인할 수 있다

```sql
SELECT empno, ename, sal
FROM emp_index_test
WHERE ename = 'SMITH';
```

적합한 Index가 없으면 전체 Table Scan이 선택될 수 있다.

### 3. Index가 있어도 반드시 사용되는 것은 아니다

Optimizer는 예상 비용을 비교해 Table Scan이 더 싸다고 판단할 수 있다.

### 4. Index도 Storage를 사용한다

Key 값과 Row 위치를 저장하고 유지하기 위한 공간이 필요하다.

### 5. DML 비용이 증가한다

`INSERT`, Indexed Column의 `UPDATE`, `DELETE` 때 관련 Index도 함께 변경해야 한다.

### 6. 핵심은 자주 쓰는 Query 최적화다

Column마다 무조건 Index를 만드는 것이 아니라 실제 `WHERE`, `JOIN`, `ORDER BY`, `GROUP BY` Pattern을 분석한다.

---

## 2. 실습 Table 준비

### 7. 원본 구조 복제

```sql
CREATE TABLE emp_index_test LIKE emp;
```

### 8. Data 복사

```sql
INSERT INTO emp_index_test
SELECT * FROM emp;
```

### 9. 현재 Index 확인

```sql
SHOW INDEX FROM emp_index_test;
```

### 10. 생성문 확인

```sql
SHOW CREATE TABLE emp_index_test;
```

`CREATE TABLE ... LIKE`는 원본의 Index 구조도 복제할 수 있으므로 “Index가 없는 상태”라고 가정하지 않는다.

---

## 3. Index 종류

### 11. Primary Key Index

```sql
PRIMARY KEY (empno)
```

Row를 유일하게 식별하며 InnoDB에서 Clustered Index의 기준이 된다.

### 12. Unique Index

```sql
CREATE UNIQUE INDEX ux_emp_index_email
ON emp_index_test (email);
```

중복을 금지하는 무결성 규칙과 검색 경로를 함께 제공한다.

### 13. 일반 Index

```sql
CREATE INDEX ix_emp_index_ename
ON emp_index_test (ename);
```

중복을 허용하며 검색 성능을 위한 접근 경로다.

### 14. Composite Index

```sql
CREATE INDEX ix_emp_index_dept_job
ON emp_index_test (deptno, job);
```

여러 Column을 정해진 순서로 묶는다.

### 15. Foreign Key Index

InnoDB Foreign Key Column에는 검사에 필요한 Index가 요구되며 적합한 Index가 없으면 자동 생성될 수 있다.

### 16. Full-text·Spatial 등은 목적이 다르다

일반 B-tree Index와 전문 검색, 공간 Data Index를 같은 기준으로 사용하지 않는다.

---

## 4. CREATE INDEX

### 17. 단일 Column Index 생성

```sql
CREATE INDEX ix_emp_index_job
ON emp_index_test (job);
```

### 18. 이름에 Table과 Column 역할을 담는다

```text
ix_emp_index_job
→ 일반 Index + Table + Column
```

### 19. ALTER TABLE로도 추가할 수 있다

```sql
ALTER TABLE emp_index_test
ADD INDEX ix_emp_index_sal (sal);
```

### 20. Unique Index 생성 전 중복 확인

```sql
SELECT email, COUNT(*) AS duplicate_count
FROM emp_index_test
WHERE email IS NOT NULL
GROUP BY email
HAVING COUNT(*) > 1;
```

### 21. 큰 Table의 Index 생성은 운영 영향을 준다

실행 시간, Lock 방식, 임시 공간, I/O, Replication 지연을 검토한다.

---

## 5. SHOW INDEX 읽기

### 22. Index 목록 조회

```sql
SHOW INDEX FROM emp_index_test;
```

### 23. Key_name

Index 이름을 나타낸다. Primary Key는 보통 `PRIMARY`로 표시된다.

### 24. Non_unique

`0`이면 중복을 허용하지 않고, `1`이면 중복을 허용한다.

### 25. Seq_in_index

복합 Index 안에서 Column의 순서를 나타낸다.

### 26. Column_name

해당 Index 위치에 사용된 Column이다.

### 27. Cardinality

서로 다른 값의 수에 대한 추정치다. 정확한 실시간 `COUNT(DISTINCT ...)` 결과로 오해하지 않는다.

### 28. Information Schema 조회

```sql
SELECT
    index_name,
    non_unique,
    seq_in_index,
    column_name,
    cardinality
FROM information_schema.statistics
WHERE table_schema = DATABASE()
  AND table_name = 'emp_index_test'
ORDER BY index_name, seq_in_index;
```

---

## 6. EXPLAIN 기본

### 29. 실제 실행 전에 계획 확인

```sql
EXPLAIN
SELECT empno, ename, job
FROM emp_index_test
WHERE job = 'MANAGER';
```

### 30. possible_keys

Optimizer가 사용할 수 있다고 판단한 Index 후보다.

### 31. key

실제로 선택된 Index다. `NULL`이면 Index를 사용하지 않았을 수 있다.

### 32. type

접근 방식의 범주다. `const`, `ref`, `range`, `index`, `ALL` 등을 Query 맥락과 함께 해석한다.

### 33. rows

검사할 것으로 추정하는 Row 수다. 실제 수가 아니라 통계 기반 추정치다.

### 34. Extra

`Using where`, `Using index`, `Using filesort`, Temporary Table 등 추가 작업 정보를 보여준다.

### 35. EXPLAIN 하나만으로 성능을 확정하지 않는다

실제 실행 시간, 반환 Row 수, Buffer 상태, Data 분포, 동시 부하까지 함께 본다.

---

## 7. 선택도와 Index 효율

### 36. 선택도

전체 Row 중 조건으로 좁혀지는 비율을 뜻한다.

### 37. 유일한 값은 선택도가 높다

```sql
WHERE empno = 7369
```

Primary Key 한 Row 조회는 Index 효율이 높다.

### 38. 값 종류가 적으면 선택도가 낮을 수 있다

```sql
WHERE status = 'ACTIVE'
```

대부분 Row가 `ACTIVE`라면 Index보다 Table Scan이 유리할 수 있다.

### 39. Data 규모가 작으면 Scan이 더 단순할 수 있다

Sample `EMP`처럼 Row가 적은 Table에서 Index가 선택되지 않아도 Index가 잘못됐다고 단정하지 않는다.

### 40. 반환 Column과 Random I/O도 비용에 포함된다

많은 Row를 Index로 찾은 뒤 Table Data를 반복 접근하면 Scan보다 비쌀 수 있다.

---

## 8. Composite Index

### 41. Column 순서가 중요하다

```sql
CREATE INDEX ix_emp_dept_job_sal
ON emp_index_test (deptno, job, sal);
```

### 42. 왼쪽 Prefix

```text
(deptno)
→ 활용 가능

(deptno, job)
→ 활용 가능

(deptno, job, sal)
→ 활용 가능

(job)만
→ 이 Index의 선두 Column이 없어 제한적
```

### 43. WHERE 조건 작성 순서와 Index 순서는 다르다

```sql
WHERE job = 'MANAGER'
  AND deptno = 20
```

`AND` 표현 순서보다 Index 정의와 Optimizer 판단이 중요하다.

### 44. 범위 조건 뒤 Column 활용이 제한될 수 있다

```sql
WHERE deptno = 20
  AND sal >= 2000
  AND job = 'MANAGER'
```

Index Column 배치는 동등 조건, 범위, 정렬과 실제 Query Pattern을 함께 고려한다.

### 45. 단일 Index가 복합 Index의 Prefix와 중복될 수 있다

`INDEX(deptno)`와 `INDEX(deptno, job)`가 모두 필요한지 확인한다. 중복 Index는 쓰기와 Storage 비용을 만든다.

### 46. 복합 Index 설계는 한 Query만 보지 않는다

주요 Query 묶음, 선택도, 정렬, Join, 수정 빈도를 함께 평가한다.

---

## 9. ORDER BY와 Index

### 47. Index 순서로 정렬 비용을 줄일 수 있다

```sql
CREATE INDEX ix_emp_dept_sal
ON emp_index_test (deptno, sal);

EXPLAIN
SELECT empno, ename, sal
FROM emp_index_test
WHERE deptno = 20
ORDER BY sal;
```

### 48. WHERE와 ORDER BY를 함께 본다

선두 `DEPTNO`를 동등 조건으로 고정한 뒤 `SAL` 순서를 활용할 수 있는지 확인한다.

### 49. 정렬 방향과 Version·Index 정의를 확인한다

복합 정렬 방향이 섞이면 Index만으로 정렬을 해결하지 못할 수 있다.

### 50. filesort는 항상 Disk 정렬이라는 뜻이 아니다

`Using filesort`는 Index 순서가 아닌 별도 정렬 단계가 필요하다는 실행 계획 표현이다.

### 51. LIMIT가 있어도 안정적인 정렬이 필요하다

```sql
ORDER BY sal DESC, empno
LIMIT 10
```

동점 처리 Key까지 Index 설계와 함께 검토한다.

---

## 10. Covering Index

### 52. 필요한 Column을 Index만으로 충족한다

```sql
CREATE INDEX ix_emp_dept_job_ename
ON emp_index_test (deptno, job, ename);
```

### 53. EXPLAIN의 Using index

Query가 필요한 값을 Index에서 모두 얻는 Covering 접근 가능성을 나타낼 수 있다.

### 54. Covering만 위해 Index를 지나치게 넓히지 않는다

Index 크기와 DML 비용, Cache 효율이 나빠질 수 있다.

### 55. SELECT *는 Covering을 어렵게 한다

필요한 Column만 조회하면 Network와 Table 접근을 줄이고 Index 선택 가능성도 개선할 수 있다.

---

## 11. Index가 잘 사용되지 않는 조건

### 56. Leading Wildcard

```sql
WHERE ename LIKE '%MIT%'
```

일반 B-tree Index로 시작 위치를 좁히기 어렵다.

### 57. Indexed Column에 함수 적용

```sql
WHERE UPPER(ename) = 'SMITH'
```

일반 Column Index를 그대로 사용하기 어려울 수 있다. Collation, 생성 Column, 표현식 Index 지원과 설계를 검토한다.

### 58. 암시적 형 변환

Column 자료형과 비교값 자료형이 다르면 변환과 Index 사용에 영향을 줄 수 있다.

### 59. 많은 Row를 반환하는 조건

조건이 대부분 Row와 일치하면 Table Scan이 합리적일 수 있다.

### 60. OR 조건

서로 다른 Column의 복잡한 `OR`는 하나의 복합 Index로 해결되지 않을 수 있다. Query 재작성은 결과 의미를 보존하며 검증한다.

### 61. NOT 또는 부정 조건

제외되는 Row가 적으면 결국 대부분 Data를 읽게 되어 Index 효율이 낮을 수 있다.

---

## 12. Index Hint

### 62. USE INDEX

```sql
SELECT empno, ename
FROM emp_index_test USE INDEX (ix_emp_index_job)
WHERE job = 'MANAGER';
```

Optimizer가 고려할 Index를 제안한다.

### 63. FORCE INDEX

```sql
SELECT empno, ename
FROM emp_index_test FORCE INDEX (ix_emp_index_job)
WHERE job = 'MANAGER';
```

지정 Index를 강하게 우선하도록 하고 Table Scan 비용을 높게 평가하게 한다.

### 64. IGNORE INDEX

```sql
SELECT empno, ename
FROM emp_index_test IGNORE INDEX (ix_emp_index_job)
WHERE job = 'MANAGER';
```

특정 Index를 후보에서 제외한다.

### 65. Hint 전에 통계와 Query를 점검한다

Data 분포, 통계, 조건, 불필요한 형 변환, Index 설계를 먼저 확인한다.

### 66. Hint는 Data 변화에 취약하다

현재는 빠르더라도 Data 규모와 분포, MariaDB Version이 바뀌면 강제 계획이 느려질 수 있다.

### 67. EXPLAIN과 실제 측정 없이 FORCE INDEX를 사용하지 않는다

Optimizer의 선택이 틀렸다는 근거와 지속적인 검증 절차가 있을 때만 사용한다.

---

## 13. DROP INDEX와 변경

### 68. Index 삭제

```sql
DROP INDEX ix_emp_index_job
ON emp_index_test;
```

### 69. ALTER TABLE 방식

```sql
ALTER TABLE emp_index_test
DROP INDEX ix_emp_index_sal;
```

### 70. 삭제 전 사용 Query를 조사한다

Slow Query, 실행 계획, Application SQL, FK 의존 여부를 확인한다.

### 71. Index DDL은 Transaction Rollback 대상이 아니다

생성·삭제 전 Backup보다 재생성 DDL, 운영 영향과 복구 절차를 준비한다.

### 72. 변경 후 EXPLAIN을 다시 비교한다

Index 존재 여부가 아니라 실제 주요 Query의 Plan과 성능을 검증한다.

---

## 14. 과도한 Index의 문제

### 73. INSERT 비용

새 Row마다 모든 관련 Index에 Entry를 추가한다.

### 74. UPDATE 비용

Indexed Column이 바뀌면 기존 Entry 제거와 새 Entry 추가가 필요하다.

### 75. DELETE 비용

Table Data와 Index Entry를 함께 제거한다.

### 76. Storage와 Memory 비용

큰 Index는 Disk 공간과 Buffer Pool을 차지한다.

### 77. Optimizer 후보 증가

비슷한 Index가 너무 많으면 관리가 복잡해지고 통계와 선택 문제를 조사하기 어려워진다.

### 78. 정기적으로 중복·미사용 후보를 검토한다

단, 짧은 관측 기간의 “미사용” 통계만으로 즉시 삭제하지 않는다. 월말·배치 Query도 고려한다.

---

## 15. AUTO_INCREMENT 기본

### 79. 자동 식별자 생성

```sql
CREATE TABLE board_practice (
    board_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (board_id)
) ENGINE = InnoDB;
```

### 80. INSERT에서 ID를 생략한다

```sql
INSERT INTO board_practice (title, content)
VALUES ('첫 글', '내용');
```

### 81. NULL 또는 DEFAULT도 자동 생성을 요청할 수 있다

```sql
INSERT INTO board_practice (board_id, title)
VALUES (DEFAULT, '두 번째 글');
```

### 82. Table당 하나의 AUTO_INCREMENT Column

해당 Column은 Key로 정의되어야 하며 InnoDB의 복합 Key에서는 선두 위치 조건도 확인한다.

### 83. 충분한 정수 범위를 선택한다

증가 속도와 보존 기간을 고려해 `INT UNSIGNED` 또는 `BIGINT UNSIGNED` 등을 선택한다.

### 84. AUTO_INCREMENT는 업무상 연속 번호가 아니다

고유 식별자 생성 도구이지 누락 없는 영수증·증빙 번호를 보장하는 Sequence가 아니다.

---

## 16. LAST_INSERT_ID()

### 85. 생성된 ID 확인

```sql
INSERT INTO board_practice (title, content)
VALUES ('새 글', '본문');

SELECT LAST_INSERT_ID() AS new_board_id;
```

### 86. 현재 Connection에 종속된다

다른 Connection이 중간에 INSERT해도 자신의 `LAST_INSERT_ID()` 값을 가져온다.

### 87. MAX(id)로 찾지 않는다

```sql
-- 동시 INSERT 환경에서 자신의 Row라는 보장이 없다.
-- SELECT MAX(board_id) FROM board_practice;
```

### 88. 다중 Row INSERT

```sql
INSERT INTO board_practice (title)
VALUES ('A'), ('B'), ('C');

SELECT LAST_INSERT_ID();
```

MariaDB의 `LAST_INSERT_ID()`는 최근 INSERT가 생성한 첫 AUTO_INCREMENT 값을 반환한다.

### 89. 오류 직후 값은 신뢰하지 않는다

INSERT가 오류로 실패했다면 `LAST_INSERT_ID()`가 정의되지 않은 상태일 수 있으므로 성공 여부를 먼저 확인한다.

### 90. 수동 ROLLBACK 후에도 값이 이전 값으로 복원되지 않는다

Transaction이 취소됐더라도 Session의 함수 결과를 “현재 존재하는 Row ID”로 가정하지 않는다.

---

## 17. AUTO_INCREMENT Gap

### 91. 삭제된 ID는 자동 재사용되지 않는다

```sql
DELETE FROM board_practice
WHERE board_id = 2;
```

다음 INSERT가 반드시 2를 사용하지 않는다.

### 92. Rollback도 Gap을 만들 수 있다

```sql
START TRANSACTION;

INSERT INTO board_practice (title)
VALUES ('취소할 글');

ROLLBACK;
```

예약된 번호가 소실되어 다음 번호가 건너뛸 수 있다.

### 93. 실패·IGNORE·동시 Insert도 Gap 원인이 된다

번호가 연속이라는 전제로 Row 수나 누락 Data를 판단하지 않는다.

### 94. ID 차이로 삭제 여부를 단정하지 않는다

Gap은 정상 동작일 수 있다. 감사에는 별도의 Event·상태 이력이 필요하다.

### 95. ID 순서와 정확한 시간 순서는 다르다

대체로 증가하지만 Transaction Commit 순서, 동시성, 명시적 값 입력을 고려하면 정확한 업무 시간은 Timestamp로 관리한다.

---

## 18. 시작값과 초기화

### 96. 다음 시작값 설정

```sql
ALTER TABLE board_practice
AUTO_INCREMENT = 1000;
```

다음 값은 설정값 또는 현재 최대값보다 큰 유효 값에 따라 결정된다.

### 97. 높은 명시적 값 입력

```sql
INSERT INTO board_practice (board_id, title)
VALUES (2000, '명시적 ID');
```

향후 자동 생성 값이 영향을 받을 수 있다.

### 98. TRUNCATE의 초기화

```sql
TRUNCATE TABLE board_practice;
```

전체 Row를 제거하고 AUTO_INCREMENT Counter를 초기화한다. DDL이며 암시적 Commit에 주의한다.

### 99. DELETE 후 번호를 억지로 재정렬하지 않는다

PK를 변경하면 FK, Log, 외부 참조가 깨질 수 있다.

### 100. AUTO_INCREMENT 값을 화면 순번으로 사용하지 않는다

화면의 1, 2, 3 순번은 `ROW_NUMBER()` 같은 조회 결과 표현으로 다루고 영구 ID와 구분한다.

---

## 19. 내 코드와 강사님 코드 비교

### 101. Index 생성만 확인한 형태

```sql
CREATE INDEX ix_emp_job
ON emp_index_test (job);
```

문법 학습에는 유효하지만 Query가 실제 Index를 선택하는지 알 수 없다.

### 102. 전후 EXPLAIN을 포함한 개선 흐름

```sql
EXPLAIN
SELECT empno, ename
FROM emp_index_test
WHERE job = 'MANAGER';

CREATE INDEX ix_emp_job
ON emp_index_test (job);

EXPLAIN
SELECT empno, ename
FROM emp_index_test
WHERE job = 'MANAGER';
```

### 103. FORCE INDEX를 바로 사용한 형태

```sql
SELECT empno, ename
FROM emp_index_test FORCE INDEX (ix_emp_job)
WHERE job = 'MANAGER';
```

### 104. Optimizer 선택을 먼저 분석하는 방식

통계와 선택도, 반환 Row 수, 복합 Index, Query 조건을 확인한 뒤 Hint 유무의 실제 성능을 비교한다.

### 105. AUTO_INCREMENT 뒤 MAX 조회

```sql
-- 동시성에 안전하지 않다.
-- SELECT MAX(board_id) FROM board_practice;
```

### 106. LAST_INSERT_ID 사용

```sql
INSERT INTO board_practice (title)
VALUES ('새 글');

SELECT LAST_INSERT_ID() AS board_id;
```

### 107. 비교 결론

- Index 생성 전후에 같은 Query의 Plan과 성능을 비교한다.
- Hint는 통계·Query·Index 설계를 검토한 뒤 사용한다.
- 복합 Index는 Column 순서와 주요 Query 묶음을 기준으로 설계한다.
- 생성 ID는 같은 Connection의 `LAST_INSERT_ID()`로 얻는다.
- AUTO_INCREMENT의 Gap을 오류로 처리하거나 재번호화하지 않는다.

---

## 20. 개선된 통합 예제

### 108. 게시글 Table과 검색 Index

```sql
CREATE TABLE board_practice (
    board_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    category VARCHAR(30) NOT NULL,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (board_id),
    INDEX ix_board_category_created (category, created_at, board_id)
) ENGINE = InnoDB;
```

### 109. Insert와 생성 ID 조회

```sql
INSERT INTO board_practice (category, title, content)
VALUES ('SQL', 'Index 학습', 'Composite Index와 EXPLAIN');

SELECT LAST_INSERT_ID() AS new_board_id;
```

### 110. 주요 Query 실행 계획

```sql
EXPLAIN
SELECT board_id, title, created_at
FROM board_practice
WHERE category = 'SQL'
ORDER BY created_at DESC, board_id DESC
LIMIT 20;
```

### 111. Keyset Pagination 연결

```sql
SELECT board_id, title, created_at
FROM board_practice
WHERE category = 'SQL'
  AND (created_at, board_id) < ('2026-08-14 12:00:00', 1000)
ORDER BY created_at DESC, board_id DESC
LIMIT 20;
```

실제 Index 방향과 MariaDB Version의 계획을 `EXPLAIN`으로 확인한다.

---

## 21. 실무 Index 절차

### 112. 느린 Query를 먼저 수집한다

추측으로 Index를 만들지 말고 실제 빈도, 실행 시간, 검사 Row, 부하 시점을 확인한다.

### 113. Query의 한 Row 의미와 반환량을 확인한다

잘못된 JOIN이나 과도한 결과를 Index로만 해결하지 않는다.

### 114. 후보 Index 설계

```text
동등 조건
→ 범위 조건
→ 정렬·Grouping
→ 필요한 반환 Column
```

항상 같은 공식은 아니며 Data 분포와 Query 조합으로 검증한다.

### 115. 전후 측정

같은 Data·조건에서 Plan, 실행 시간, 읽은 Row, DML 영향과 Index 크기를 비교한다.

### 116. 배포 후 관찰

Production Data 분포와 동시 부하에서 읽기 개선과 쓰기 비용을 다시 확인한다.

### 117. 제거 계획도 준비한다

문제가 생기면 정확한 Index 이름으로 복구할 수 있도록 생성·삭제 DDL과 승인 절차를 보관한다.

---

## 22. 자주 하는 실수

### 118. 모든 Column에 Index를 만든다

쓰기와 Storage 비용만 늘고 실제 Query에는 도움이 되지 않을 수 있다.

### 119. 복합 Index Column 순서를 무시한다

왼쪽 Prefix와 동등·범위·정렬 조건을 고려한다.

### 120. Index 존재만 확인하고 사용 여부를 보지 않는다

`SHOW INDEX`와 `EXPLAIN`은 서로 다른 질문에 답한다.

### 121. Sample Data의 Plan을 운영에도 그대로 가정한다

Row 수와 분포가 달라지면 Optimizer 선택도 달라질 수 있다.

### 122. FORCE INDEX로 문제를 고정한다

Data 변화에 따라 더 나쁜 계획을 강제할 수 있다.

### 123. AUTO_INCREMENT를 연속 업무번호로 사용한다

Rollback과 실패만으로도 Gap이 생긴다.

### 124. MAX(id)로 방금 생성한 ID를 찾는다

동시 Connection의 Insert와 경쟁한다. `LAST_INSERT_ID()`를 사용한다.

### 125. 삭제 후 ID를 재번호화한다

참조 무결성과 외부 식별자가 깨질 수 있다.

---

## 23. 디버깅 방법

### 126. Index 정의 확인

```sql
SHOW INDEX FROM emp_index_test;
SHOW CREATE TABLE emp_index_test;
```

### 127. Query 전후 EXPLAIN 비교

```sql
EXPLAIN
SELECT empno, ename
FROM emp_index_test
WHERE deptno = 20
  AND job = 'MANAGER';
```

### 128. 실제 선택도 확인

```sql
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT deptno) AS distinct_departments,
    COUNT(DISTINCT job) AS distinct_jobs
FROM emp_index_test;
```

### 129. 조건의 자료형과 함수 확인

`SHOW CREATE TABLE`로 Column 자료형을 확인하고 암시적 변환과 함수 적용을 점검한다.

### 130. 중복 Index 후보 확인

같은 선두 Column을 가진 Index와 완전히 같은 Column 조합을 목록으로 비교한다.

### 131. AUTO_INCREMENT 상태 확인

```sql
SHOW TABLE STATUS LIKE 'board_practice';
```

표시값은 다음 후보에 대한 Metadata이며 동시성 환경에서 미리 ID를 예약하는 용도로 사용하지 않는다.

### 132. Insert 직후 Connection에서 확인

```sql
SELECT LAST_INSERT_ID();
```

오류 여부와 같은 Connection인지 확인한다.

### 133. Rollback Gap 재현

실습 Table에서 Transaction Insert → ID 확인 → Rollback → 재Insert 순으로 실행해 Gap이 정상적으로 생길 수 있음을 확인한다.

---

## 24. 종합실습

### 134. 문제 1 — 단일 Index

`EMP_INDEX_TEST.JOB`에 일반 Index를 만들고 직무 조회의 실행 계획을 전후 비교한다.

### 135. 문제 2 — 복합 Index

부서별 직무 조건과 급여 정렬 Query를 위한 `(DEPTNO, JOB, SAL)` Index를 만들고 왼쪽 Prefix 활용 가능 조건을 설명한다.

### 136. 문제 3 — Index Metadata

Information Schema에서 `EMP_INDEX_TEST`의 Index명, Unique 여부, Column 순서를 조회한다.

### 137. 문제 4 — AUTO_INCREMENT

자동 증가 PK를 가진 게시글 Table을 만들고 한 Row를 입력한 뒤 생성 ID를 안전하게 조회한다.

### 138. 문제 5 — Gap 검증

Transaction 안에서 게시글을 입력하고 Rollback한 뒤 다시 입력하여 ID가 연속되지 않을 수 있음을 확인한다.

---

## 25. 정답과 해설

### 139. 문제 1 정답

```sql
EXPLAIN
SELECT empno, ename
FROM emp_index_test
WHERE job = 'MANAGER';

CREATE INDEX ix_emp_index_job
ON emp_index_test (job);

EXPLAIN
SELECT empno, ename
FROM emp_index_test
WHERE job = 'MANAGER';
```

작은 Sample에서는 Index가 선택되지 않을 수도 있다.

### 140. 문제 2 정답

```sql
CREATE INDEX ix_emp_dept_job_sal
ON emp_index_test (deptno, job, sal);

EXPLAIN
SELECT empno, ename, sal
FROM emp_index_test
WHERE deptno = 20
  AND job = 'MANAGER'
ORDER BY sal;
```

선두부터 `(DEPTNO)`, `(DEPTNO, JOB)`, 전체 조합 Query가 주요 활용 후보이며 `JOB`만으로는 왼쪽 선두가 비어 있다.

### 141. 문제 3 정답

```sql
SELECT
    index_name,
    non_unique,
    seq_in_index,
    column_name
FROM information_schema.statistics
WHERE table_schema = DATABASE()
  AND table_name = 'emp_index_test'
ORDER BY index_name, seq_in_index;
```

### 142. 문제 4 정답

```sql
CREATE TABLE board_practice (
    board_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (board_id)
) ENGINE = InnoDB;

INSERT INTO board_practice (title)
VALUES ('AUTO_INCREMENT 실습');

SELECT LAST_INSERT_ID() AS new_board_id;
```

### 143. 문제 5 정답

```sql
START TRANSACTION;

INSERT INTO board_practice (title)
VALUES ('Rollback할 글');

SELECT LAST_INSERT_ID() AS rolled_back_id;

ROLLBACK;

INSERT INTO board_practice (title)
VALUES ('다시 입력한 글');

SELECT LAST_INSERT_ID() AS committed_id;
```

Rollback된 Row의 예약 번호는 재사용되지 않을 수 있으므로 Gap은 정상이다.

---

## 26. 최종 체크리스트

### 144. Index 설계 체크

- [ ] 실제 주요 Query와 Data 분포를 기준으로 설계했는가?
- [ ] 복합 Index의 Column 순서와 왼쪽 Prefix를 검토했는가?
- [ ] 기존 Index와 중복되지 않는가?
- [ ] 읽기 개선과 DML·Storage 비용을 함께 측정했는가?

### 145. 실행 계획 체크

- [ ] `SHOW INDEX`와 `EXPLAIN`을 모두 확인했는가?
- [ ] `possible_keys`, `key`, `rows`, `Extra`를 Query 맥락에서 읽었는가?
- [ ] Sample과 운영 Data의 차이를 고려했는가?
- [ ] Hint 없이 해결할 방법을 먼저 검토했는가?

### 146. AUTO_INCREMENT 체크

- [ ] 충분한 정수 범위와 Key를 사용했는가?
- [ ] INSERT에서 자동 증가 Column을 생략했는가?
- [ ] 생성 ID를 같은 Connection의 `LAST_INSERT_ID()`로 얻었는가?
- [ ] Gap과 Rollback을 정상 동작으로 처리하는가?

---

## 27. 핵심 요약

### 147. Index와 AUTO_INCREMENT 핵심 문장

```text
Index
→ 검색 경로 개선, 대신 Storage와 DML 유지 비용 발생

Composite Index
→ Column 순서와 왼쪽 Prefix가 핵심

SHOW INDEX
→ 존재와 구조 확인

EXPLAIN
→ Optimizer의 실제 접근 계획 확인

FORCE INDEX
→ 측정과 근거가 있는 최후 수단

AUTO_INCREMENT
→ 고유 식별자 자동 생성, 연속 번호 보장 아님

LAST_INSERT_ID()
→ 같은 Connection이 생성한 ID 확인
```

### 148. 최종 정리

Index의 목적은 Index 자체를 사용하는 것이 아니라 중요한 Query의 전체 비용을 줄이는 것이다. 실제 Query와 Data 분포를 기준으로 설계하고, `EXPLAIN`과 측정으로 읽기 개선이 쓰기·Storage 비용보다 가치 있는지 확인한다. AUTO_INCREMENT는 동시 환경에서 편리한 고유 식별자를 제공하지만 Gap 없는 순번은 보장하지 않으며, 생성된 값은 `MAX(id)`가 아니라 같은 Connection의 `LAST_INSERT_ID()`로 가져온다.

---

## 📎 다음 문서

다음 원본 흐름은 계층과 반복 구조를 조회하는 Recursive CTE이다.

```text
18_SQL_Recursive_CTE.md
```
