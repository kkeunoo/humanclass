# 15. SQL DML

> Table의 Row를 생성·수정·삭제하는 INSERT, UPDATE, DELETE

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | `INSERT`, `UPDATE`, `DELETE`, `INSERT ... SELECT` |
| 기준 DBMS | MariaDB, InnoDB |
| 실습 Table | `DEPT_PRACTICE`, `EMP_PRACTICE` |
| 선수 학습 | DDL, 제약조건, `SELECT`, `WHERE`, Subquery, JOIN |
| 다음 학습 | Transaction: `COMMIT`, `ROLLBACK` |
| 문서 버전 | V3 Encyclopedia |

> 원본 `Script.sql`의 DDL 다음 DML 범위를 기준으로 구성했다. 기존 학습용 `EMP`, `DEPT`를 직접 변경하지 않고 복제하거나 별도로 만든 실습 Table에서 실행한다.

---

## 🎯 학습 목표

- DML과 DDL의 역할을 구분한다.
- Column 목록을 명시하여 단일·다중 Row를 안전하게 입력한다.
- `INSERT ... SELECT`로 Query 결과를 다른 Table에 저장한다.
- `UPDATE`와 `DELETE` 전에 같은 조건의 `SELECT`로 대상을 검증한다.
- Primary Key, Foreign Key, `NOT NULL`, Default가 DML에 미치는 영향을 설명한다.
- 영향받은 Row 수와 변경 후 Data를 확인한다.
- 대량 변경을 작은 단위로 설계하고 Transaction 단원과 연결한다.

---

## 1. DML 기본 개념

### 1. DML은 Row Data를 변경한다

```text
INSERT
→ 새로운 Row 생성

UPDATE
→ 기존 Row의 Column 값 변경

DELETE
→ 조건에 맞는 기존 Row 삭제
```

### 2. SELECT와 먼저 연결한다

`UPDATE`와 `DELETE`의 `WHERE`는 `SELECT`에서 사용한 Filtering 논리와 같다. 변경 전에 대상 Row를 조회할 수 있다.

### 3. 실습 Table 준비 예시

```sql
CREATE TABLE dept_practice LIKE dept;
CREATE TABLE emp_practice LIKE emp;
```

`CREATE TABLE ... LIKE`는 구조 복제이며 Data까지 복사하지 않는다.

### 4. Data 복사

```sql
INSERT INTO dept_practice
SELECT * FROM dept;

INSERT INTO emp_practice
SELECT * FROM emp;
```

### 5. 변경 전 현재 상태 확인

```sql
SELECT * FROM dept_practice ORDER BY deptno;
SELECT * FROM emp_practice ORDER BY empno;
```

---

## 2. INSERT 기본

### 6. Column 목록을 명시한 단일 Row 입력

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES (50, 'DEVELOPMENT', 'SEOUL');
```

### 7. Column 목록과 값의 개수를 맞춘다

```text
(deptno, dname, loc)
→ 3개 Column

(50, 'DEVELOPMENT', 'SEOUL')
→ 3개 값
```

### 8. 값은 위치별로 대응한다

Column 목록의 첫 번째 값은 첫 번째 Column에 저장된다. 자료형뿐 아니라 의미도 같은 순서여야 한다.

### 9. Column 목록 생략은 피한다

```sql
-- 현재 전체 Column 순서에 의존한다.
INSERT INTO dept_practice
VALUES (60, 'DATA', 'BUSAN');
```

Table 구조가 바뀌면 실패하거나 잘못된 값이 연결될 수 있으므로 Column 목록을 권장한다.

### 10. 입력 결과 확인

```sql
SELECT deptno, dname, loc
FROM dept_practice
WHERE deptno = 50;
```

---

## 3. 여러 Row INSERT

### 11. 한 문장으로 여러 Row 입력

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES
    (60, 'DATA', 'BUSAN'),
    (70, 'SECURITY', 'DAEJEON'),
    (80, 'CLOUD', 'JEJU');
```

### 12. 모든 Row의 값 구조를 맞춘다

각 괄호는 같은 Column 목록을 사용하므로 값 개수와 위치가 모두 같아야 한다.

### 13. 한 Row의 오류가 전체 문장에 영향을 줄 수 있다

중복 PK나 제약조건 위반이 포함되면 정상 Row까지 입력되지 않을 수 있다. 입력 전 Key와 참조값을 검증한다.

### 14. 너무 큰 단위로 한 문장을 만들지 않는다

대량 적재는 오류 복구, Packet 크기, Lock, Log, Transaction 크기를 고려해 적절한 Batch로 나눈다.

### 15. 입력된 Row 수 확인

```sql
SELECT ROW_COUNT() AS affected_rows;
```

`ROW_COUNT()`는 바로 앞 DML 뒤에 확인해야 의미가 있다.

---

## 4. NULL과 DEFAULT 입력

### 16. 선택 Column은 생략할 수 있다

```sql
INSERT INTO dept_practice (deptno, dname)
VALUES (90, 'AI');
```

`LOC`가 Nullable이면 NULL 또는 정의된 Default가 적용된다.

### 17. DEFAULT 키워드

```sql
INSERT INTO emp_practice
    (empno, ename, hiredate, sal, deptno)
VALUES
    (9001, 'KIM', '2026-08-14', DEFAULT, 50);
```

### 18. 명시적 NULL은 Default와 다르다

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES (91, 'LAB', NULL);
```

Nullable Column에 명시한 `NULL`은 “값 없음”이다.

### 19. NOT NULL 위반

```sql
-- ENAME이 NOT NULL이면 실패
-- INSERT INTO emp_practice (empno, ename)
-- VALUES (9002, NULL);
```

### 20. Default가 업무적으로 올바른지 확인한다

급여 미입력과 급여 0이 다른 의미라면 `DEFAULT 0`에 의존하지 않는다.

---

## 5. 날짜와 문자열 입력

### 21. ISO 형태의 날짜 Literal을 사용한다

```sql
INSERT INTO emp_practice
    (empno, ename, job, hiredate, sal, deptno)
VALUES
    (9003, 'LEE', 'DEVELOPER', '2026-08-14', 3500, 50);
```

### 22. 외부 문자열 형식은 명시적으로 변환한다

```sql
INSERT INTO emp_practice
    (empno, ename, hiredate, sal)
VALUES
    (9004, 'PARK', STR_TO_DATE('14/08/2026', '%d/%m/%Y'), 2800);
```

### 23. 숫자를 문자열로 넣는 암시적 변환에 의존하지 않는다

금액 Column에는 숫자를, 날짜 Column에는 날짜 값을 전달한다.

### 24. SQL 문자열의 작은따옴표

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES (92, 'R&D', 'SEOUL');
```

문자열 값은 작은따옴표로 표현한다.

---

## 6. INSERT ... SELECT

### 25. SELECT 결과를 직접 입력한다

```sql
INSERT INTO emp_practice
    (empno, ename, job, mgr, hiredate, sal, comm, deptno)
SELECT
    empno, ename, job, mgr, hiredate, sal, comm, deptno
FROM emp
WHERE deptno = 20;
```

### 26. 대상과 SELECT의 Column을 위치별로 맞춘다

Column명 자체가 같지 않아도 개수, 순서, 의미, 자료형이 호환되어야 한다.

### 27. SELECT만 먼저 실행한다

```sql
SELECT empno, ename, job, mgr, hiredate, sal, comm, deptno
FROM emp
WHERE deptno = 20;
```

입력될 Row와 값을 먼저 검증한다.

### 28. 중복 Key 가능성을 확인한다

```sql
SELECT source.empno
FROM emp AS source
JOIN emp_practice AS target
    ON target.empno = source.empno
WHERE source.deptno = 20;
```

### 29. 실행 후 Source와 Target Row 수를 비교한다

```sql
SELECT COUNT(*) FROM emp WHERE deptno = 20;
SELECT COUNT(*) FROM emp_practice WHERE deptno = 20;
```

### 30. CREATE TABLE ... SELECT와 구분한다

`INSERT ... SELECT`는 이미 존재하는 Table에 Row를 넣는다. `CREATE TABLE ... SELECT`는 Table 생성까지 수행하며 제약조건·Index 복제 여부를 별도로 확인해야 한다.

---

## 7. Primary Key와 중복 입력

### 31. 중복 Primary Key는 거부된다

```sql
-- EMPNO 9001이 이미 있으면 오류
-- INSERT INTO emp_practice (empno, ename)
-- VALUES (9001, 'DUPLICATE');
```

### 32. 오류를 무조건 무시하지 않는다

`INSERT IGNORE`는 일부 오류를 Warning으로 바꾸거나 Row를 건너뛸 수 있다. 어떤 Data가 입력되지 않았는지 놓칠 수 있으므로 일반 해결책으로 사용하지 않는다.

### 33. 중복이면 갱신하는 Upsert

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES (50, 'DEVELOPMENT', 'SEOUL')
ON DUPLICATE KEY UPDATE
    dname = 'DEVELOPMENT',
    loc = 'SEOUL';
```

### 34. 어떤 Unique Key가 충돌하는지 확인한다

여러 Unique Index가 있는 Table에서는 의도하지 않은 충돌로 기존 Row가 갱신될 수 있다.

### 35. Upsert는 업무 의미가 있을 때 사용한다

“없으면 생성, 있으면 최신 상태로 변경”이 명확한 요구사항일 때 사용한다. 중복 Data 원인을 숨기는 도구가 아니다.

---

## 8. Foreign Key와 입력 순서

### 36. 부모 Row를 먼저 입력한다

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES (50, 'DEVELOPMENT', 'SEOUL');

INSERT INTO emp_practice
    (empno, ename, hiredate, sal, deptno)
VALUES
    (9005, 'CHOI', '2026-08-14', 3000, 50);
```

### 37. 존재하지 않는 부모 Key는 실패한다

```sql
-- DEPTNO 999가 부모 Table에 없으면 FK 오류
-- INSERT INTO emp_practice
--     (empno, ename, hiredate, sal, deptno)
-- VALUES
--     (9006, 'JUNG', '2026-08-14', 3000, 999);
```

### 38. Nullable FK에는 NULL을 넣을 수 있다

```sql
INSERT INTO emp_practice
    (empno, ename, hiredate, sal, deptno)
VALUES
    (9007, 'HAN', '2026-08-14', 2500, NULL);
```

### 39. FK 검사를 끄는 방식으로 해결하지 않는다

정상 입력 순서와 유효한 부모 Data를 준비한다. `foreign_key_checks=0`은 잘못된 관계를 만들 수 있다.

---

## 9. UPDATE 기본

### 40. 한 Row 수정

```sql
UPDATE emp_practice
SET sal = 3200
WHERE empno = 9005;
```

### 41. 여러 Column 수정

```sql
UPDATE emp_practice
SET
    job = 'SENIOR DEVELOPER',
    sal = 3800,
    deptno = 50
WHERE empno = 9005;
```

### 42. 현재 값을 사용한 계산

```sql
UPDATE emp_practice
SET sal = sal * 1.05
WHERE deptno = 50;
```

### 43. WHERE가 없으면 모든 Row가 대상이다

```sql
-- 전체 사원의 급여를 변경하므로 의도가 확실할 때만 실행
-- UPDATE emp_practice SET sal = sal * 1.05;
```

### 44. 같은 WHERE의 SELECT를 먼저 실행한다

```sql
SELECT empno, ename, sal
FROM emp_practice
WHERE deptno = 50;
```

### 45. 변경 후 다시 조회한다

```sql
SELECT empno, ename, sal
FROM emp_practice
WHERE deptno = 50
ORDER BY empno;
```

---

## 10. 조건부 UPDATE

### 46. CASE로 Row별 값을 다르게 변경한다

```sql
UPDATE emp_practice
SET sal = CASE
    WHEN job = 'MANAGER' THEN sal * 1.10
    WHEN job = 'DEVELOPER' THEN sal * 1.07
    ELSE sal * 1.03
END
WHERE deptno = 50;
```

### 47. CASE가 있어도 WHERE는 별개다

`CASE`는 새 값을 정하고 `WHERE`는 변경할 Row를 제한한다.

### 48. NULL 산술을 주의한다

```sql
UPDATE emp_practice
SET comm = COALESCE(comm, 0) + 100
WHERE job = 'SALESMAN';
```

### 49. Subquery 결과로 변경한다

```sql
UPDATE emp_practice
SET sal = (
    SELECT ROUND(AVG(source.sal), 2)
    FROM emp AS source
)
WHERE empno = 9007;
```

Scalar Subquery가 1행 1열을 반환하는지 확인한다.

### 50. FK Column 변경도 제약조건을 따른다

```sql
UPDATE emp_practice
SET deptno = 60
WHERE empno = 9005;
```

부모 `DEPT_PRACTICE`에 60번이 있어야 한다.

---

## 11. JOIN을 사용한 UPDATE

### 51. 다른 Table 조건으로 대상 선택

```sql
UPDATE emp_practice AS e
JOIN dept_practice AS d
    ON d.deptno = e.deptno
SET e.sal = e.sal * 1.05
WHERE d.loc = 'SEOUL';
```

### 52. 동일한 JOIN SELECT로 먼저 검증한다

```sql
SELECT e.empno, e.ename, e.sal, d.dname, d.loc
FROM emp_practice AS e
JOIN dept_practice AS d
    ON d.deptno = e.deptno
WHERE d.loc = 'SEOUL';
```

### 53. 일대다 JOIN에서 대상 중복을 점검한다

한 대상 Row가 Source 여러 Row와 결합되면 어떤 값으로 갱신할지 모호해질 수 있다. Source를 먼저 유일하게 만든다.

### 54. 복잡한 UPDATE는 중간 결과를 고정한다

임시 Table이나 검증 가능한 Stage Data를 사용하면 재현성과 감사가 쉬워진다.

---

## 12. DELETE 기본

### 55. 조건에 맞는 Row 삭제

```sql
DELETE FROM emp_practice
WHERE empno = 9007;
```

### 56. WHERE가 없으면 모든 Row를 삭제한다

```sql
-- 전체 Row 삭제
-- DELETE FROM emp_practice;
```

Table 구조는 유지되지만 전체 Data가 대상이다.

### 57. 삭제 전 SELECT

```sql
SELECT *
FROM emp_practice
WHERE empno = 9007;
```

### 58. 삭제 후 존재 여부 확인

```sql
SELECT COUNT(*) AS remaining_count
FROM emp_practice
WHERE empno = 9007;
```

### 59. 여러 조건 삭제

```sql
DELETE FROM emp_practice
WHERE deptno = 50
  AND hiredate < '2020-01-01';
```

조건의 경계값과 NULL을 확인한다.

---

## 13. Foreign Key와 DELETE

### 60. 부모 삭제가 제한될 수 있다

```sql
DELETE FROM dept_practice
WHERE deptno = 50;
```

참조하는 사원이 있으면 FK의 `ON DELETE` 규칙에 따라 실패하거나 자식에 동작이 전파된다.

### 61. 기본적으로 자식부터 처리한다

```sql
DELETE FROM emp_practice WHERE deptno = 50;
DELETE FROM dept_practice WHERE deptno = 50;
```

실제 업무에서는 삭제 대신 이력 보존이나 상태 변경이 필요한지도 검토한다.

### 62. CASCADE는 자동 삭제를 전파한다

`ON DELETE CASCADE`가 정의되어 있으면 부모 삭제 시 자식도 삭제된다. 실행 전 예상 자식 Row 수를 확인한다.

### 63. SET NULL은 관계만 해제한다

`ON DELETE SET NULL`이면 자식 Row는 남고 Foreign Key만 NULL이 된다.

### 64. SHOW CREATE TABLE로 규칙을 확인한다

```sql
SHOW CREATE TABLE emp_practice;
```

기억이나 추측으로 삭제 동작을 판단하지 않는다.

---

## 14. DELETE와 TRUNCATE 비교

### 65. DELETE는 조건을 사용할 수 있다

```sql
DELETE FROM emp_practice
WHERE deptno = 50;
```

### 66. TRUNCATE는 전체 Row를 제거한다

```sql
TRUNCATE TABLE emp_practice;
```

### 67. Transaction 성격이 다르다

InnoDB의 `DELETE`는 Transaction DML로 다룰 수 있지만 `TRUNCATE`는 DDL로 처리되어 암시적 Commit을 발생시킨다.

### 68. AUTO_INCREMENT 처리도 다르다

`TRUNCATE`는 Counter를 초기화하지만 일반적인 `DELETE`는 기존 다음 번호 흐름을 유지한다.

### 69. 전체 삭제라도 목적에 맞게 선택한다

Rollback 가능성, Trigger, FK, Logging, 감사, 성능을 함께 고려한다.

---

## 15. 영향받은 Row 확인

### 70. 실행 직후 ROW_COUNT()

```sql
UPDATE emp_practice
SET sal = sal + 100
WHERE deptno = 50;

SELECT ROW_COUNT() AS affected_rows;
```

### 71. UPDATE의 기본 Affected Rows

MariaDB Client 설정에 따라 표현 차이가 있을 수 있지만 기본적으로 실제 값이 변경된 Row 수가 중요하다. 조건에 일치했어도 같은 값으로 설정하면 Changed Row 수와 다를 수 있다.

### 72. 예상 수와 비교한다

```sql
SELECT COUNT(*) AS expected_rows
FROM emp_practice
WHERE deptno = 50;
```

변경 전에 기록한 예상 Row 수와 DML 결과를 비교한다.

### 73. Row 수만으로 값의 정확성을 보장하지 않는다

Sample Row, 합계, 최소·최대, 업무 불변 조건도 함께 검증한다.

### 74. 변경 전후 집계 비교

```sql
SELECT deptno, COUNT(*) AS employee_count, SUM(sal) AS salary_sum
FROM emp_practice
GROUP BY deptno
ORDER BY deptno;
```

---

## 16. Safe Update와 LIMIT

### 75. sql_safe_updates

`sql_safe_updates`가 활성화되면 Key를 적절히 사용하는 WHERE나 LIMIT 없이 UPDATE·DELETE하는 실수를 차단할 수 있다.

```sql
SELECT @@sql_safe_updates;
```

### 76. 안전 모드를 끄는 것으로 해결하지 않는다

오류가 발생하면 먼저 Key 기반 조건과 대상 Query를 개선한다.

### 77. LIMIT만으로 대상 의미를 만들지 않는다

```sql
-- 어떤 한 Row인지 안정적으로 정의되지 않을 수 있다.
-- DELETE FROM emp_practice LIMIT 1;
```

### 78. ORDER BY + LIMIT도 업무 Key를 대신하지 않는다

MariaDB는 단일 Table UPDATE·DELETE에서 제한 문법을 지원할 수 있지만 복제 안전성, 동점, 실행 순서가 문제가 될 수 있다. Primary Key 목록을 먼저 확정하는 방식을 우선한다.

### 79. Key 목록을 고정한 변경

```sql
UPDATE emp_practice
SET sal = sal + 100
WHERE empno IN (9001, 9003, 9005);
```

---

## 17. 내 코드와 강사님 코드 비교

### 80. 전체 Column 순서에 의존한 INSERT

```sql
INSERT INTO dept_practice
VALUES (50, 'DEVELOPMENT', 'SEOUL');
```

### 81. Column 목록을 명시한 개선 방식

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES (50, 'DEVELOPMENT', 'SEOUL');
```

### 82. 바로 실행하는 UPDATE

```sql
UPDATE emp_practice
SET sal = sal * 1.10
WHERE deptno = 50;
```

### 83. SELECT 검증을 포함한 개선 흐름

```sql
SELECT empno, ename, sal, sal * 1.10 AS new_sal
FROM emp_practice
WHERE deptno = 50
ORDER BY empno;

UPDATE emp_practice
SET sal = sal * 1.10
WHERE deptno = 50;
```

### 84. 비교 결론

- INSERT는 대상 Column을 명시한다.
- UPDATE·DELETE는 동일 WHERE의 SELECT를 먼저 실행한다.
- 영향 Row 수와 변경된 값을 모두 확인한다.
- `IGNORE`, Upsert, CASCADE는 요구사항이 명확할 때 사용한다.
- 안전 모드를 끄거나 LIMIT를 붙이는 것으로 잘못된 조건을 숨기지 않는다.

---

## 18. 개선된 통합 예제

### 85. 신규 부서와 사원 입력

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES (50, 'DEVELOPMENT', 'SEOUL');

INSERT INTO emp_practice
    (empno, ename, job, hiredate, sal, comm, deptno)
VALUES
    (9001, 'KIM', 'DEVELOPER', '2026-08-14', 3200, NULL, 50),
    (9002, 'LEE', 'DEVELOPER', '2026-08-14', 3000, NULL, 50),
    (9003, 'PARK', 'MANAGER', '2026-08-14', 4200, 500, 50);
```

### 86. 변경 대상 Preview와 UPDATE

```sql
SELECT
    empno,
    ename,
    sal AS old_sal,
    ROUND(sal * 1.05, 2) AS new_sal
FROM emp_practice
WHERE deptno = 50
  AND job = 'DEVELOPER'
ORDER BY empno;

UPDATE emp_practice
SET sal = ROUND(sal * 1.05, 2)
WHERE deptno = 50
  AND job = 'DEVELOPER';
```

### 87. 삭제 대상 Preview와 DELETE

```sql
SELECT empno, ename, deptno
FROM emp_practice
WHERE empno = 9002;

DELETE FROM emp_practice
WHERE empno = 9002;

SELECT ROW_COUNT() AS deleted_rows;
```

---

## 19. 실무 DML 절차

### 88. 변경 전 Checklist

```text
정확한 Database와 Table인가?
WHERE 대상은 몇 Row인가?
Key 기반으로 식별되는가?
FK·Unique·NOT NULL 위반 가능성은 없는가?
Backup 또는 복구 Query가 준비됐는가?
```

### 89. Preview Query를 보관한다

변경 DML과 같은 JOIN·WHERE 조건의 SELECT를 Code Review와 작업 기록에 함께 남긴다.

### 90. 대량 변경은 Batch로 나눈다

Lock 시간, Undo Log, Replication 지연, 실패 재시작 범위를 줄이기 위해 안정적인 Key 기준으로 나눈다.

### 91. 변경 전 값을 별도로 보존한다

감사나 복구가 필요하면 대상 Key와 기존 값을 Backup Table 또는 승인된 Export에 보관한다.

### 92. 실행 후 업무 불변 조건을 검증한다

PK 중복 0, FK 위반 0, 필수값 NULL 0, 합계 변화가 승인 범위와 일치하는지 확인한다.

### 93. Transaction 경계를 명시한다

여러 DML이 하나의 업무 단위라면 다음 단원에서 `START TRANSACTION`, `COMMIT`, `ROLLBACK`으로 원자성을 보장한다.

---

## 20. 자주 하는 실수

### 94. INSERT Column 목록을 생략한다

Table 구조 변경에 취약하고 값의 의미를 Review하기 어렵다.

### 95. UPDATE·DELETE의 WHERE를 빠뜨린다

전체 Row가 대상이 된다. 실행 전 SELECT와 Row 수 확인을 습관화한다.

### 96. 날짜를 지역별 문자열로 바로 넣는다

명확한 날짜 Literal 또는 `STR_TO_DATE`를 사용한다.

### 97. INSERT SELECT의 Column 순서를 잘못 맞춘다

Source와 Target을 위치별로 한 줄씩 대조한다.

### 98. 중복 오류를 IGNORE로 숨긴다

왜 중복이 발생했는지와 누락된 Row를 추적하기 어려워진다.

### 99. 부모 Row보다 자식 Row를 먼저 넣는다

Foreign Key 위반이 발생한다.

### 100. CASCADE 범위를 확인하지 않고 부모를 삭제한다

예상보다 많은 자식 Row가 함께 삭제될 수 있다.

### 101. Affected Rows만 보고 완료한다

값의 정확성과 집계·무결성까지 검증한다.

---

## 21. 디버깅 방법

### 102. SHOW CREATE TABLE로 제약조건 확인

```sql
SHOW CREATE TABLE emp_practice;
```

### 103. 중복 Key 확인

```sql
SELECT empno, COUNT(*) AS duplicate_count
FROM emp_practice
GROUP BY empno
HAVING COUNT(*) > 1;
```

### 104. FK 부모 존재 확인

```sql
SELECT d.deptno, d.dname
FROM dept_practice AS d
WHERE d.deptno = 50;
```

### 105. Preview에 새 값까지 표시한다

```sql
SELECT empno, sal AS old_sal, ROUND(sal * 1.05, 2) AS new_sal
FROM emp_practice
WHERE deptno = 50;
```

### 106. 변경 직후 ROW_COUNT 확인

```sql
SELECT ROW_COUNT() AS affected_rows;
```

다른 문장을 실행하기 전에 확인한다.

### 107. 변경 후 Key 목록 재조회

```sql
SELECT empno, ename, sal, deptno
FROM emp_practice
WHERE empno IN (9001, 9002, 9003)
ORDER BY empno;
```

### 108. 오류를 최소 Row로 재현한다

대량 입력에서 실패하면 한 Row와 필요한 부모 Data만 남겨 제약조건, 자료형, 길이 문제를 분리한다.

---

## 22. 종합실습

### 109. 문제 1 — 부서 다중 입력

60번 DATA, 70번 SECURITY 부서를 Column 목록을 명시하여 한 문장으로 입력한다.

### 110. 문제 2 — 사원 입력

부서 60에 속한 신규 사원 2명을 입력한다. 날짜와 급여 자료형을 올바르게 사용한다.

### 111. 문제 3 — INSERT SELECT

원본 `EMP`에서 30번 부서 사원을 `EMP_PRACTICE`로 복사한다. 실행 전 대상과 중복 Key를 확인한다.

### 112. 문제 4 — 조건부 급여 수정

60번 부서 사원의 급여를 5% 인상한다. 먼저 기존·예상 급여를 조회한다.

### 113. 문제 5 — 안전한 삭제

70번 부서를 삭제하되 소속 사원 존재 여부와 Foreign Key 동작을 먼저 확인한다.

---

## 23. 정답과 해설

### 114. 문제 1 정답

```sql
INSERT INTO dept_practice (deptno, dname, loc)
VALUES
    (60, 'DATA', 'BUSAN'),
    (70, 'SECURITY', 'DAEJEON');
```

### 115. 문제 2 정답

```sql
INSERT INTO emp_practice
    (empno, ename, job, hiredate, sal, deptno)
VALUES
    (9101, 'SEO', 'ANALYST', '2026-08-14', 3100, 60),
    (9102, 'YUN', 'DEVELOPER', '2026-08-14', 2900, 60);
```

부모 60번 부서가 먼저 존재해야 한다.

### 116. 문제 3 정답

```sql
SELECT e.empno, e.ename
FROM emp AS e
LEFT JOIN emp_practice AS p
    ON p.empno = e.empno
WHERE e.deptno = 30
  AND p.empno IS NULL;

INSERT INTO emp_practice
    (empno, ename, job, mgr, hiredate, sal, comm, deptno)
SELECT
    e.empno, e.ename, e.job, e.mgr, e.hiredate, e.sal, e.comm, e.deptno
FROM emp AS e
LEFT JOIN emp_practice AS p
    ON p.empno = e.empno
WHERE e.deptno = 30
  AND p.empno IS NULL;
```

Target에 없는 Key만 복사한다. 부모 `DEPT_PRACTICE`에 30번 부서가 있어야 한다.

### 117. 문제 4 정답

```sql
SELECT empno, ename, sal, ROUND(sal * 1.05, 2) AS new_sal
FROM emp_practice
WHERE deptno = 60
ORDER BY empno;

UPDATE emp_practice
SET sal = ROUND(sal * 1.05, 2)
WHERE deptno = 60;

SELECT ROW_COUNT() AS affected_rows;
```

### 118. 문제 5 정답

```sql
SHOW CREATE TABLE emp_practice;

SELECT empno, ename
FROM emp_practice
WHERE deptno = 70;

-- 자식이 없거나 승인된 방식으로 먼저 처리된 후 실행한다.
DELETE FROM dept_practice
WHERE deptno = 70;
```

FK의 `ON DELETE` 규칙을 확인하지 않은 상태에서 부모 삭제를 실행하지 않는다.

---

## 24. 최종 체크리스트

### 119. INSERT 체크

- [ ] 대상 Column 목록을 명시했는가?
- [ ] 값의 개수·순서·자료형이 일치하는가?
- [ ] PK 중복과 FK 부모 존재를 확인했는가?
- [ ] NULL과 Default의 의미가 올바른가?

### 120. UPDATE·DELETE 체크

- [ ] 같은 WHERE의 SELECT를 먼저 실행했는가?
- [ ] 예상 대상 Row 수와 Key 목록을 기록했는가?
- [ ] WHERE가 빠지거나 너무 넓지 않은가?
- [ ] CASCADE와 Trigger 등 연쇄 영향을 확인했는가?

### 121. 실행 후 체크

- [ ] `ROW_COUNT()`와 예상 Row 수를 비교했는가?
- [ ] 변경된 값과 업무 집계를 재검증했는가?
- [ ] PK·FK·NOT NULL 무결성이 유지되는가?
- [ ] Transaction의 Commit 또는 Rollback 결정을 명확히 했는가?

---

## 25. 핵심 요약

### 122. DML 핵심 문장

```text
INSERT
→ Column 목록과 값의 위치를 명시

INSERT ... SELECT
→ SELECT 결과를 기존 Table에 입력

UPDATE
→ SET으로 새 값, WHERE로 대상 제한

DELETE
→ WHERE에 맞는 Row 삭제

안전한 DML
→ 동일 조건 SELECT → 예상 Row 확인 → DML → ROW_COUNT와 값 검증
```

### 123. 최종 정리

DML의 핵심은 문법보다 **정확히 어떤 Row가 어떤 값으로 바뀌는지 실행 전에 증명하는 것**이다. INSERT는 Column 목록과 제약조건을 확인하고, UPDATE·DELETE는 같은 조건의 SELECT를 먼저 실행한다. 실행 후에는 영향 Row 수뿐 아니라 Key, 값, 집계, 참조 무결성을 검증하며, 여러 변경을 하나의 업무 단위로 처리하는 방법은 다음 Transaction 단원에서 다룬다.

---

## 📎 다음 문서

다음 원본 흐름은 DML 변경을 확정하거나 취소하는 Transaction이다.

```text
16_SQL_Transaction.md
```

---

## 🔬 V3 동작 백과 — 입력값이 실제 Row 변경으로 이어지는 과정

```sql
UPDATE dept2
SET loc = 'BUSAN'
WHERE deptno = 50;
```

```text
WHERE로 대상 Row 탐색
→ SET Expression 계산
→ 자료형·제약조건 검사
→ 일치 Row 변경
→ Affected Rows 반환
→ Transaction Commit 시 확정
```

안전한 실행:

```text
1. 같은 WHERE로 SELECT
2. 예상 PK와 Row 수 기록
3. Transaction 시작
4. INSERT·UPDATE·DELETE 실행
5. Affected Rows 확인
6. 변경 후 SELECT
7. 맞으면 COMMIT, 아니면 ROLLBACK
```

INSERT는 입력값을 Column 위치에 연결한 뒤 PK·FK·NOT NULL 등을 검사한다. DELETE는 부모 Row를 참조하는 자식 Row가 있으면 FK 정책에 따라 거부되거나 정의한 참조 동작을 수행한다.

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 Anchor | 강사님 코드 Anchor |
| --- | --- | --- |
| INSERT | `insert into dept2` | 같은 Query |
| UPDATE | `update dept2` | UPDATE 구간 |
| DELETE | `delete from` | DELETE 구간 |
| 영향 Row | 실행 결과·Row Count Comment | DML 실습 구간 |

원본 EMP·DEPT가 아니라 복사한 실습 Table에서 변경 Query를 재현한다.
