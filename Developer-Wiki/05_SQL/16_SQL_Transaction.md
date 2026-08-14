# 16. SQL Transaction

> 여러 DML을 하나의 업무 단위로 묶어 모두 확정하거나 모두 취소하는 방법

---

## 📌 문서 정보

| 항목 | 내용 |
|---|---|
| 학습 주제 | `START TRANSACTION`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`, `autocommit` |
| 기준 DBMS | MariaDB, InnoDB |
| 실습 Table | `ACCOUNT_PRACTICE`, `EMP_PRACTICE` |
| 선수 학습 | `INSERT`, `UPDATE`, `DELETE`, 제약조건 |
| 다음 학습 | Index와 AUTO_INCREMENT |
| 문서 버전 | V2 |

> 원본 `Script.sql`의 DML 다음 `COMMIT / ROLLBACK` 범위를 기준으로 구성했다. 안전한 실습을 위해 기존 학습용 원본 Table 대신 `_PRACTICE` Table을 사용한다.

---

## 🎯 학습 목표

- Transaction과 업무 단위의 관계를 설명한다.
- MariaDB의 기본 `autocommit` 상태를 확인하고 명시적 Transaction을 시작한다.
- `COMMIT`과 `ROLLBACK`으로 변경을 확정하거나 취소한다.
- `SAVEPOINT`로 Transaction의 일부만 되돌린다.
- DDL의 암시적 Commit 때문에 생기는 위험을 예방한다.
- 두 Session에서 변경 가시성과 Lock 대기를 관찰한다.
- Deadlock과 Lock Wait를 오류가 아닌 동시성 제어 관점에서 이해한다.

---

## 1. Transaction 기본 개념

### 1. 하나의 논리적 업무 단위

계좌 이체는 출금과 입금이 함께 성공해야 한다.

```text
송금 계좌 출금
        +
수신 계좌 입금
        =
하나의 Transaction
```

### 2. 일부만 성공하면 Data가 깨진다

출금만 반영되고 입금이 실패하면 전체 잔액이 맞지 않는다.

### 3. COMMIT은 변경을 확정한다

```sql
COMMIT;
```

현재 Transaction의 변경을 영구적으로 확정하고 Transaction을 종료한다.

### 4. ROLLBACK은 변경을 취소한다

```sql
ROLLBACK;
```

현재 Transaction의 미확정 DML을 되돌리고 Transaction을 종료한다.

### 5. Transaction을 지원하는 Engine이 필요하다

실습에서는 Transaction과 Row-level Lock을 지원하는 `InnoDB`를 사용한다.

---

## 2. ACID

### 6. Atomicity — 원자성

Transaction의 작업은 전부 성공하거나 전부 취소되어야 한다.

### 7. Consistency — 일관성

Transaction 전후에 PK, FK, 잔액 규칙 같은 무결성 조건이 유지되어야 한다.

### 8. Isolation — 격리성

동시에 실행되는 Transaction이 서로의 중간 상태에 부적절하게 간섭하지 않도록 한다.

### 9. Durability — 지속성

Commit된 변경은 장애가 발생해도 복구 가능한 형태로 유지되어야 한다.

### 10. ACID는 Application Logic도 필요하다

Database가 원자성과 무결성을 지원해도 “잔액은 음수가 될 수 없다” 같은 업무 규칙을 올바르게 설계하고 검증해야 한다.

---

## 3. autocommit

### 11. MariaDB의 기본값은 활성화다

```sql
SELECT @@autocommit;
```

일반적으로 `1`이면 각 DML 문장이 성공할 때 자동 Commit된다.

### 12. autocommit=1의 의미

```sql
UPDATE emp_practice
SET sal = sal + 100
WHERE empno = 9001;
```

명시적 Transaction이 아니라면 문장 완료 후 변경이 바로 확정될 수 있다.

### 13. START TRANSACTION으로 한시적으로 묶는다

```sql
START TRANSACTION;

UPDATE emp_practice
SET sal = sal + 100
WHERE empno = 9001;

COMMIT;
```

### 14. SET autocommit=0

```sql
SET autocommit = 0;
```

현재 Session의 자동 Commit을 끈다. 이후 Transaction 종료와 Session 상태를 명확히 관리해야 한다.

### 15. 실무에서는 명시적 범위를 선호한다

연결 전체의 `autocommit`을 장시간 끄기보다 필요한 업무 구간에 `START TRANSACTION`을 사용하는 방식이 이해하기 쉽다.

### 16. autocommit을 다시 1로 바꿀 때 주의한다

활성 Transaction이 있다면 `SET autocommit = 1`이 암시적 Commit을 일으킬 수 있다.

---

## 4. START TRANSACTION

### 17. 명시적 시작

```sql
START TRANSACTION;
```

### 18. BEGIN도 사용할 수 있다

```sql
BEGIN;
```

일반 SQL Session에서는 Transaction 시작 의미로 사용할 수 있다. Stored Program의 Block 문법과 혼동을 피하려면 `START TRANSACTION`이 명확하다.

### 19. Transaction 상태 확인

```sql
SELECT @@in_transaction;
```

현재 Session이 Transaction 안에 있으면 `1`, 아니면 `0`이다.

### 20. 시작 전에 미완료 Transaction을 확인한다

`START TRANSACTION`은 기존 Transaction이 있다면 암시적으로 Commit할 수 있으므로 중첩 Transaction처럼 사용하지 않는다.

### 21. Transaction 종료는 반드시 명시한다

정상 완료는 `COMMIT`, 검증 실패와 오류는 `ROLLBACK`으로 끝낸다.

---

## 5. COMMIT

### 22. 여러 DML을 확정한다

```sql
START TRANSACTION;

UPDATE emp_practice
SET sal = sal + 100
WHERE empno = 9001;

UPDATE emp_practice
SET sal = sal - 100
WHERE empno = 9002;

COMMIT;
```

### 23. Commit 전 검증한다

```sql
SELECT empno, ename, sal
FROM emp_practice
WHERE empno IN (9001, 9002)
ORDER BY empno;
```

같은 Session에서는 자신의 미확정 변경을 볼 수 있다.

### 24. COMMIT 후 되돌리려면 새 작업이 필요하다

Commit된 DML을 일반 `ROLLBACK`으로 취소할 수 없다. 반대 DML 또는 Backup 복구가 필요하다.

### 25. Commit은 Lock을 해제한다

Transaction이 가진 Row Lock과 Metadata Lock은 종료 시 해제된다.

### 26. Commit을 늦게 잊지 않는다

사용자 입력이나 외부 API 응답을 기다리며 Transaction을 오래 유지하면 Lock과 Resource 사용이 증가한다.

---

## 6. ROLLBACK

### 27. 전체 Transaction 취소

```sql
START TRANSACTION;

UPDATE emp_practice
SET sal = sal * 10
WHERE empno = 9001;

ROLLBACK;
```

### 28. 취소 전후를 확인한다

```sql
SELECT empno, sal
FROM emp_practice
WHERE empno = 9001;
```

### 29. 오류가 나면 자동으로 전체 취소된다고 가정하지 않는다

일부 문장 오류 후에도 Transaction이 계속 활성화될 수 있다. Application은 예외 처리에서 명시적으로 `ROLLBACK`해야 한다.

### 30. Connection 종료 시 미확정 변경

정상적인 InnoDB Transaction이 Commit되지 않은 채 Connection이 종료되면 미확정 변경은 Rollback된다. 이를 업무 제어 방식으로 의존하지 않는다.

### 31. DDL은 ROLLBACK 대상이 아닐 수 있다

`CREATE`, `ALTER`, `DROP`, `TRUNCATE`는 암시적 Commit을 일으키므로 DML과 같은 방식으로 되돌릴 수 있다고 생각하지 않는다.

---

## 7. 계좌 이체 통합 예제

### 32. 실습 Table

```sql
CREATE TABLE account_practice (
    account_id INT NOT NULL,
    owner_name VARCHAR(50) NOT NULL,
    balance DECIMAL(12, 2) NOT NULL,
    PRIMARY KEY (account_id)
) ENGINE = InnoDB;
```

### 33. Sample Data

```sql
INSERT INTO account_practice (account_id, owner_name, balance)
VALUES
    (1, 'KIM', 10000),
    (2, 'LEE', 5000);
```

### 34. 이체 Transaction

```sql
START TRANSACTION;

UPDATE account_practice
SET balance = balance - 1000
WHERE account_id = 1
  AND balance >= 1000;

UPDATE account_practice
SET balance = balance + 1000
WHERE account_id = 2;

SELECT account_id, owner_name, balance
FROM account_practice
WHERE account_id IN (1, 2)
ORDER BY account_id;

COMMIT;
```

### 35. 출금 성공 Row 수를 확인한다

첫 UPDATE의 `ROW_COUNT()`가 1인지 확인해야 잔액 부족 상태에서 입금만 진행되는 문제를 막을 수 있다.

### 36. 수신 계좌 존재도 확인한다

두 번째 UPDATE의 영향 Row가 1인지 검증한다. 하나라도 실패하면 전체 `ROLLBACK`한다.

### 37. 전체 잔액 불변 조건

수수료가 없다면 두 계좌 합계는 이체 전후 같아야 한다.

```sql
SELECT SUM(balance) AS total_balance
FROM account_practice
WHERE account_id IN (1, 2);
```

---

## 8. SAVEPOINT

### 38. Transaction 내부의 이름 있는 지점

```sql
START TRANSACTION;

UPDATE emp_practice
SET sal = sal + 100
WHERE empno = 9001;

SAVEPOINT after_first_update;
```

### 39. Savepoint 이후 작업

```sql
UPDATE emp_practice
SET sal = sal + 500
WHERE empno = 9002;
```

### 40. 일부만 되돌리기

```sql
ROLLBACK TO SAVEPOINT after_first_update;
```

첫 번째 변경은 남고 Savepoint 이후 변경이 취소된다.

### 41. Savepoint 제거

```sql
RELEASE SAVEPOINT after_first_update;
```

변경을 Commit하는 것이 아니라 Savepoint 이름만 제거한다.

### 42. 마지막에 전체 Transaction을 종료한다

```sql
COMMIT;
```

`ROLLBACK TO SAVEPOINT`만 실행하면 Transaction은 계속 활성 상태다.

### 43. COMMIT·전체 ROLLBACK 시 Savepoint도 사라진다

종료된 Transaction의 Savepoint는 다시 사용할 수 없다.

### 44. Savepoint 이후 획득한 Lock이 모두 즉시 해제된다고 가정하지 않는다

MariaDB 문서상 `ROLLBACK TO SAVEPOINT` 후에도 이후 획득한 Lock이 유지될 수 있다. 긴 Transaction을 Savepoint로만 관리하지 않는다.

---

## 9. DDL과 암시적 COMMIT

### 45. 위험한 조합

```sql
START TRANSACTION;

UPDATE emp_practice
SET sal = sal + 100
WHERE empno = 9001;

ALTER TABLE emp_practice
ADD COLUMN memo VARCHAR(100);

ROLLBACK;
```

`ALTER TABLE` 전에 기존 DML이 암시적으로 Commit될 수 있으므로 급여 변경이 Rollback되지 않을 수 있다.

### 46. 주요 암시적 Commit 문장

```text
CREATE / ALTER / DROP
TRUNCATE
START TRANSACTION
SET autocommit = 1
일부 관리 문장
```

### 47. DDL과 DML 배포를 분리한다

Schema Migration과 Data Migration의 실행 순서, 실패 복구 방식을 각각 설계한다.

### 48. Temporary Table도 완전한 예외가 아니다

일부 Temporary Table DDL은 암시적 Commit을 일으키지 않을 수 있지만 그 DDL 자체가 Rollback되는 것은 아니다. 일반 DDL처럼 주의한다.

### 49. Transaction 안에서 문장 종류를 확인한다

외부 Library나 Migration Tool이 실행하는 DDL까지 포함해 Transaction 경계를 검토한다.

---

## 10. 두 Session과 변경 가시성

### 50. Session A에서 미확정 변경

```sql
-- Session A
START TRANSACTION;

UPDATE account_practice
SET balance = balance - 500
WHERE account_id = 1;

SELECT balance
FROM account_practice
WHERE account_id = 1;
```

### 51. Session B에서 조회

```sql
-- Session B
SELECT balance
FROM account_practice
WHERE account_id = 1;
```

Isolation Level과 Snapshot 시점에 따라 Session B는 Commit 전 값을 볼 수 있다.

### 52. Session A가 COMMIT

```sql
-- Session A
COMMIT;
```

### 53. Session B의 Transaction 상태도 중요하다

Session B가 이미 장기 Transaction의 Snapshot을 사용 중이면 A의 Commit 후에도 같은 SELECT에서 이전 값을 볼 수 있다.

### 54. 실습은 서로 다른 Connection에서 수행한다

같은 Query Editor의 같은 Connection에서는 두 Session 동시성을 관찰할 수 없다.

---

## 11. Isolation Level

### 55. 현재 격리 수준 확인

```sql
SELECT @@tx_isolation;
```

MariaDB Version과 환경에 따라 변수 이름을 확인한다.

### 56. READ UNCOMMITTED

다른 Transaction의 미확정 변경을 볼 수 있어 Dirty Read가 가능하다.

### 57. READ COMMITTED

각 문장은 다른 Transaction이 Commit한 Data를 읽는다. 같은 Transaction 안에서도 반복 조회 결과가 달라질 수 있다.

### 58. REPEATABLE READ

InnoDB의 일반적인 기본 격리 수준으로, Transaction의 일관된 Snapshot을 유지한다.

### 59. SERIALIZABLE

동시 실행을 더 엄격하게 제한하여 직렬 실행에 가까운 일관성을 제공하지만 대기와 충돌 비용이 커질 수 있다.

### 60. 격리 수준은 높을수록 무조건 좋은 것이 아니다

일관성 요구, 동시성, Lock, 재시도 비용을 함께 고려한다.

### 61. 변경은 명확한 Transaction 전에 설정한다

```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
```

운영 표준과 Connection Pool 설정을 먼저 확인한다.

---

## 12. Lock 기본

### 62. UPDATE는 대상에 Exclusive Lock을 획득한다

다른 Transaction이 같은 Index Record를 변경하려 하면 대기할 수 있다.

### 63. InnoDB Lock은 Index Record 기반이다

효율적인 Key 조건이 없으면 더 넓은 Record나 범위가 영향을 받을 수 있다.

### 64. Transaction이 끝나야 Lock이 해제된다

`COMMIT` 또는 `ROLLBACK`을 빠뜨리면 다른 Session이 오래 대기할 수 있다.

### 65. SELECT ... FOR UPDATE

```sql
START TRANSACTION;

SELECT account_id, balance
FROM account_practice
WHERE account_id IN (1, 2)
ORDER BY account_id
FOR UPDATE;
```

변경 전에 대상 Row를 Locking Read로 읽는다.

### 66. FOR UPDATE 후 검증과 변경

```sql
UPDATE account_practice
SET balance = balance - 1000
WHERE account_id = 1
  AND balance >= 1000;

UPDATE account_practice
SET balance = balance + 1000
WHERE account_id = 2;

COMMIT;
```

### 67. Lock 대상 순서를 통일한다

여러 Transaction이 계좌 ID 오름차순처럼 같은 순서로 Row를 잠그면 Deadlock 가능성을 줄일 수 있다.

---

## 13. Lock Wait와 Deadlock

### 68. Lock Wait

한 Transaction이 가진 Lock을 다른 Transaction이 기다리는 정상적인 동시성 상황이다.

### 69. Deadlock

```text
Transaction A
→ Row 1 Lock 보유, Row 2 대기

Transaction B
→ Row 2 Lock 보유, Row 1 대기
```

서로 상대방의 Lock을 기다리면 진행할 수 없다.

### 70. InnoDB는 한 Transaction을 희생시킨다

Deadlock을 감지하면 일부 Transaction을 Rollback하여 순환을 끊는다.

### 71. Deadlock은 재시도 가능한 오류로 설계한다

Application은 해당 업무 Transaction 전체를 처음부터 다시 실행할 수 있어야 한다.

### 72. 최신 Deadlock 확인

```sql
SHOW ENGINE INNODB STATUS;
```

`LATEST DETECTED DEADLOCK` 영역에서 관련 문장과 Lock을 확인할 수 있다.

### 73. Lock Wait 진단

MariaDB Version에 따라 `sys.innodb_lock_waits` 같은 View로 대기와 차단 Session을 확인할 수 있다.

### 74. Transaction을 짧게 유지한다

외부 통신, 사용자 승인, 긴 계산은 가능하면 Transaction 밖에서 처리한다.

### 75. 조건과 Index를 점검한다

불필요하게 넓은 범위를 Scan하고 Lock하지 않도록 안정적인 Key와 실행 계획을 확인한다.

---

## 14. 실패 처리 Pattern

### 76. 기본 Application 흐름

```text
START TRANSACTION
→ 대상 Lock·검증
→ DML 실행
→ 영향 Row와 업무 규칙 확인
→ 성공이면 COMMIT
→ 실패면 ROLLBACK
```

### 77. SQL Client 수동 실습

```sql
START TRANSACTION;

UPDATE account_practice
SET balance = balance - 1000
WHERE account_id = 1
  AND balance >= 1000;

SELECT ROW_COUNT() AS withdrawn_rows;

-- 결과가 1일 때 다음 단계를 실행한다.
UPDATE account_practice
SET balance = balance + 1000
WHERE account_id = 2;

SELECT ROW_COUNT() AS deposited_rows;

-- 두 결과가 모두 1이고 합계가 맞으면 COMMIT, 아니면 ROLLBACK한다.
```

### 78. SQL 문장만으로 분기되지 않는 점을 이해한다

수동 Client에서는 결과를 보고 결정하지만 Application에서는 예외 처리와 조건문으로 Commit·Rollback을 제어한다.

### 79. 실패 후 Connection을 Pool에 반환하지 않는다

Rollback과 상태 정리 없이 Connection을 재사용하면 다음 요청에 이전 Transaction 상태가 섞일 수 있다.

### 80. 재시도는 멱등성을 고려한다

Deadlock 재시도 시 중복 이체나 중복 주문이 생기지 않도록 업무 Key와 처리 이력을 설계한다.

---

## 15. 내 코드와 강사님 코드 비교

### 81. DML 후 즉시 COMMIT

```sql
UPDATE emp_practice
SET sal = sal + 100
WHERE empno = 9001;

COMMIT;
```

단일 변경을 확정하는 문법은 맞지만 여러 업무 단계와 검증 흐름이 보이지 않는다.

### 82. 명시적 Transaction과 검증

```sql
START TRANSACTION;

UPDATE emp_practice
SET sal = sal + 100
WHERE empno = 9001;

SELECT ROW_COUNT() AS affected_rows;

SELECT empno, ename, sal
FROM emp_practice
WHERE empno = 9001;

COMMIT;
```

### 83. 오류 후 ROLLBACK을 생략한 형태

일부 문장이 실패했다고 전체 Transaction이 항상 자동 취소된다고 가정하면 이전 성공 DML이 남을 수 있다.

### 84. 예외 시 명시적 ROLLBACK

```text
try
→ START TRANSACTION
→ DML
→ 검증
→ COMMIT

catch
→ ROLLBACK
→ 오류 기록 또는 재시도
```

### 85. 비교 결론

- Transaction 시작과 종료를 Code에서 명시한다.
- Commit 전에 영향 Row와 업무 불변 조건을 검증한다.
- 오류 처리에서 전체 Rollback을 수행한다.
- DDL을 DML Transaction 안에 섞지 않는다.
- Deadlock은 분석과 함께 제한된 재시도 대상으로 설계한다.

---

## 16. 개선된 통합 예제

### 86. 이체 전 Lock과 검증

```sql
START TRANSACTION;

SELECT account_id, owner_name, balance
FROM account_practice
WHERE account_id IN (1, 2)
ORDER BY account_id
FOR UPDATE;
```

### 87. 출금과 입금

```sql
UPDATE account_practice
SET balance = balance - 1000
WHERE account_id = 1
  AND balance >= 1000;

SELECT ROW_COUNT() AS withdrawn_rows;

UPDATE account_practice
SET balance = balance + 1000
WHERE account_id = 2;

SELECT ROW_COUNT() AS deposited_rows;
```

### 88. 최종 검증

```sql
SELECT account_id, owner_name, balance
FROM account_practice
WHERE account_id IN (1, 2)
ORDER BY account_id;

SELECT SUM(balance) AS total_balance
FROM account_practice
WHERE account_id IN (1, 2);
```

두 UPDATE가 각각 1행이고 잔액과 합계가 정상일 때만 `COMMIT`한다. 아니면 `ROLLBACK`한다.

---

## 17. 실무 Transaction 지침

### 89. Transaction 범위를 업무 단위와 맞춘다

너무 작으면 일부 성공 상태가 생기고, 너무 크면 Lock과 충돌 비용이 커진다.

### 90. Network 호출을 Transaction 밖에 둔다

외부 결제·메일·API는 Database Rollback으로 취소되지 않는다. Outbox, 상태 Machine, 보상 Transaction 같은 별도 Pattern이 필요할 수 있다.

### 91. 모든 종료 경로를 확인한다

성공, 검증 실패, SQL 오류, Timeout, 사용자 취소에서 Commit 또는 Rollback이 정확히 실행되는지 검토한다.

### 92. Transaction 안에서 사용자 입력을 기다리지 않는다

Lock 보유 시간이 길어지고 다른 요청을 막을 수 있다.

### 93. 재시도 가능한 오류를 분류한다

Deadlock과 일부 Lock Timeout은 재시도할 수 있지만 제약조건 위반과 잘못된 Data를 같은 방식으로 반복하지 않는다.

### 94. 관측 가능성을 준비한다

Transaction ID 또는 업무 요청 ID, 실행 시간, 영향 Row, 오류, 재시도 횟수를 Log로 남긴다.

### 95. Connection 설정을 확인한다

Connection Pool의 autocommit, Isolation Level, Timeout이 Application 기대와 일치하는지 확인한다.

---

## 18. 자주 하는 실수

### 96. autocommit=1을 모르고 ROLLBACK한다

이미 문장별 Commit된 변경은 Rollback되지 않는다.

### 97. Transaction 안에 DDL을 실행한다

암시적 Commit으로 앞선 DML이 예상보다 일찍 확정될 수 있다.

### 98. 오류 발생 후 Commit한다

실패한 문장 이전의 성공 DML이 남아 일부 성공 상태가 확정될 수 있다.

### 99. SAVEPOINT Rollback 후 Transaction이 끝났다고 생각한다

`ROLLBACK TO SAVEPOINT` 후에도 최종 `COMMIT` 또는 전체 `ROLLBACK`이 필요하다.

### 100. 장시간 Transaction을 유지한다

Lock, Undo, Purge, Metadata 변경 대기와 운영 장애 위험이 커진다.

### 101. 두 Session 실습을 같은 Connection에서 한다

동시성과 격리 수준의 차이를 관찰할 수 없다.

### 102. Deadlock을 Database 오류로만 취급한다

동시 Transaction에서 발생 가능한 정상적 충돌이므로 Lock 순서와 재시도 전략을 설계한다.

### 103. Commit 후 ROLLBACK으로 복구하려 한다

Commit 이후에는 보상 DML이나 Backup 복구가 필요하다.

---

## 19. 디버깅 방법

### 104. Session 상태 확인

```sql
SELECT
    @@autocommit AS autocommit_mode,
    @@in_transaction AS in_transaction;
```

### 105. Engine 확인

```sql
SHOW TABLE STATUS LIKE 'account_practice';
```

### 106. Transaction 시작·종료를 한 줄씩 추적한다

Application Log에 시작, DML, 영향 Row, Commit·Rollback, 오류를 순서대로 남긴다.

### 107. 두 Connection에서 재현한다

Session A에서 `FOR UPDATE` 후 대기시키고 Session B에서 같은 Row를 UPDATE하여 Lock Wait를 관찰한다.

### 108. Deadlock 정보 확인

```sql
SHOW ENGINE INNODB STATUS;
```

### 109. 열린 Transaction을 찾는다

운영 권한과 MariaDB Version에 맞는 Information Schema 또는 Performance Schema View를 사용해 오래 열린 Transaction을 조사한다.

### 110. 최소 두 Row로 Deadlock을 재현한다

Session A와 B가 같은 두 Row를 반대 순서로 잠그도록 구성해 원인을 확인하고 Lock 순서를 통일한다.

### 111. 암시적 Commit 의심 시 문장 목록을 확인한다

Transaction 사이에 DDL, `START TRANSACTION`, `SET autocommit=1`, 관리 문장이 포함됐는지 확인한다.

---

## 20. 종합실습

### 112. 문제 1 — Commit 실습

명시적 Transaction에서 9001번 사원의 급여를 100 증가시키고 변경값을 확인한 뒤 Commit한다.

### 113. 문제 2 — Rollback 실습

9002번 사원의 급여를 임시로 10배 변경하고 조회한 뒤 Rollback하여 원래 값으로 돌아왔는지 확인한다.

### 114. 문제 3 — Savepoint 실습

두 사원의 급여를 순서대로 수정하되 첫 변경 후 Savepoint를 만들고 두 번째 변경만 취소한 뒤 첫 변경을 Commit한다.

### 115. 문제 4 — 계좌 이체

1번 계좌에서 2번 계좌로 500을 이체한다. 두 계좌를 Lock하고 영향 Row와 총잔액을 확인한다.

### 116. 문제 5 — DDL 암시적 Commit 분석

DML 사이에 `ALTER TABLE`을 넣으면 왜 마지막 ROLLBACK이 첫 DML을 취소하지 못할 수 있는지 설명한다.

---

## 21. 정답과 해설

### 117. 문제 1 정답

```sql
START TRANSACTION;

UPDATE emp_practice
SET sal = sal + 100
WHERE empno = 9001;

SELECT empno, ename, sal
FROM emp_practice
WHERE empno = 9001;

COMMIT;
```

### 118. 문제 2 정답

```sql
START TRANSACTION;

UPDATE emp_practice
SET sal = sal * 10
WHERE empno = 9002;

SELECT empno, sal
FROM emp_practice
WHERE empno = 9002;

ROLLBACK;

SELECT empno, sal
FROM emp_practice
WHERE empno = 9002;
```

### 119. 문제 3 정답

```sql
START TRANSACTION;

UPDATE emp_practice
SET sal = sal + 100
WHERE empno = 9001;

SAVEPOINT first_update_done;

UPDATE emp_practice
SET sal = sal + 500
WHERE empno = 9002;

ROLLBACK TO SAVEPOINT first_update_done;
RELEASE SAVEPOINT first_update_done;

COMMIT;
```

### 120. 문제 4 정답

```sql
START TRANSACTION;

SELECT account_id, balance
FROM account_practice
WHERE account_id IN (1, 2)
ORDER BY account_id
FOR UPDATE;

UPDATE account_practice
SET balance = balance - 500
WHERE account_id = 1
  AND balance >= 500;

SELECT ROW_COUNT() AS withdrawn_rows;

UPDATE account_practice
SET balance = balance + 500
WHERE account_id = 2;

SELECT ROW_COUNT() AS deposited_rows;

SELECT account_id, balance
FROM account_practice
WHERE account_id IN (1, 2)
ORDER BY account_id;

-- 두 UPDATE가 각각 1행이고 검증이 정상일 때 실행한다.
COMMIT;
```

검증이 실패하면 `COMMIT` 대신 `ROLLBACK`한다.

### 121. 문제 5 정답

`ALTER TABLE`은 암시적 Commit을 발생시킬 수 있다. 따라서 `ALTER` 전에 실행된 미확정 DML이 먼저 Commit되고, 뒤의 `ROLLBACK`은 이미 확정된 변경을 취소하지 못한다. DDL과 DML Migration을 분리하고 각각의 복구 계획을 세운다.

---

## 22. 최종 체크리스트

### 122. 시작 전 체크

- [ ] Table Engine이 Transaction을 지원하는가?
- [ ] `@@autocommit`과 Isolation Level을 확인했는가?
- [ ] Transaction 범위가 하나의 업무 단위와 일치하는가?
- [ ] DDL이나 외부 Network 호출이 섞이지 않았는가?

### 123. 실행 중 체크

- [ ] 변경 대상을 안정적인 Key로 Lock·조회했는가?
- [ ] 각 DML의 영향 Row 수를 검증했는가?
- [ ] 업무 불변 조건과 최종 값을 확인했는가?
- [ ] Lock 획득 순서가 다른 Transaction과 일관적인가?

### 124. 종료 체크

- [ ] 모든 성공 경로에서 `COMMIT`하는가?
- [ ] 모든 실패 경로에서 `ROLLBACK`하는가?
- [ ] Savepoint 후에도 전체 Transaction을 종료했는가?
- [ ] Deadlock 재시도와 Connection 상태 초기화가 준비됐는가?

---

## 23. 핵심 요약

### 125. Transaction 핵심 문장

```text
START TRANSACTION
→ 업무 Transaction 시작

COMMIT
→ 현재 변경 확정 및 Lock 해제

ROLLBACK
→ 미확정 변경 전체 취소

SAVEPOINT
→ Transaction 내부의 부분 복구 지점

autocommit=1
→ 명시적 Transaction 밖에서는 문장별 자동 확정

DDL
→ 암시적 Commit 가능, DML Transaction과 분리
```

### 126. 최종 정리

Transaction의 핵심은 `COMMIT`과 `ROLLBACK` 문법이 아니라 **업무상 함께 성공해야 하는 변경의 경계를 정확히 정하는 것**이다. 시작 전에 Connection 상태를 확인하고, 실행 중에는 대상 Lock·영향 Row·불변 조건을 검증하며, 모든 종료 경로에서 Commit 또는 Rollback을 보장한다. 동시 환경에서는 짧은 Transaction, 일관된 Lock 순서, Deadlock 재시도까지 하나의 설계로 다룬다.

---

## 📎 다음 문서

다음 원본 흐름은 검색 성능과 식별자 생성을 다루는 Index와 AUTO_INCREMENT이다.

```text
17_SQL_Index와_AUTO_INCREMENT.md
```
