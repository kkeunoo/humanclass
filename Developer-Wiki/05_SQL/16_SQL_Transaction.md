# 16. 트랜잭션 — 확정 전 변경과 확정 후 상태 나누기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

ROLLBACK은 과거의 아무 시점으로 돌아가는 기능이 아니다. 현재 트랜잭션에서 아직 확정하지 않은 변경을 되돌린다. 같은 삭제라도 언제 확정했는지에 따라 결과가 달라진다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

START TRANSACTION·COMMIT·ROLLBACK의 경계를 추적한다. 자동 커밋·지원 엔진·DDL 경계를 확인하고 원본의 롤백 주석을 바로 읽는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

트랜잭션은 여러 DB 변경을 하나의 작업 단위로 다루는 경계다. 명시적으로 시작하고 변경을 살핀 뒤 COMMIT으로 확정하거나 ROLLBACK으로 취소할 수 있다. 지원 엔진의 미확정 DML이라는 조건이 필요하다. 이미 COMMIT한 변경을 나중 ROLLBACK만으로 되돌릴 수는 없다.

| 상태 | 같은 연결에서 관찰 | ROLLBACK |
| --- | --- | --- |
| DELETE 직후·미확정 | 행이 안 보임 | 삭제 취소 가능 |
| DELETE 후 COMMIT | 행이 안 보임 | 이미 확정한 삭제는 복구 안 됨 |
| 일반 영구 DDL 실행 | 암묵 커밋 경계 가능 | DML과 같이 취급 못 함 |

자동 커밋이 켜져 있으면 명시적 트랜잭션 밖의 DML이 바로 확정될 수 있다. 새 예제는 START TRANSACTION으로 범위를 명시하고 지원 엔진 InnoDB를 지정한다. 임시 표의 수명과 트랜잭션 확정은 별개다. 이 예제의 COMMIT은 현재 연결 임시 표의 행 변경을 확정하는 뜻이지 연결 종료 뒤에도 임시 표를 영구 보관한다는 뜻이 아니다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB START TRANSACTION](https://mariadb.com/docs/server/reference/sql-statements/transactions/start-transaction), [COMMIT](https://mariadb.com/docs/server/reference/sql-statements/transactions/commit), [ROLLBACK](https://mariadb.com/docs/server/reference/sql-statements/transactions/rollback). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/16_SQL_Transaction.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

<details>
<summary>예제 준비 전체 SQL — 현재 장의 학습 문법과 구별</summary>

```sql
DROP TEMPORARY TABLE IF EXISTS book_emp;
CREATE TEMPORARY TABLE book_emp (
    empno INT PRIMARY KEY, ename VARCHAR(20), job VARCHAR(20),
    mgr INT, sal DECIMAL(8,2), comm DECIMAL(8,2), deptno INT
);
INSERT INTO book_emp VALUES
(1,'ADA','CLERK',3,1000,NULL,20),
(2,'BEN','SALESMAN',3,1600,300,30),
(3,'CARA','MANAGER',NULL,3000,NULL,20),
(4,'DAN','CLERK',3,1300,0,10),
(5,'ELLA','ANALYST',3,3000,NULL,20),
(6,'FINN','SALESMAN',3,1500,0,30);
DROP TEMPORARY TABLE IF EXISTS book_dept;
CREATE TEMPORARY TABLE book_dept (deptno INT PRIMARY KEY, dname VARCHAR(20));
INSERT INTO book_dept VALUES (10,'ALPHA'),(20,'BETA'),(30,'GAMMA'),(40,'EMPTY');
DROP TEMPORARY TABLE IF EXISTS book_ledger;
CREATE TEMPORARY TABLE book_ledger (id INT PRIMARY KEY,amount INT) ENGINE=InnoDB;
INSERT INTO book_ledger VALUES(1,100);
COMMIT;
```

표 생성·삽입 문법은 14·15장에서 설명한다. TEMPORARY는 원래 수업 구문으로 승격한 것이 아니라 예제 자료를 연결 안에서만 쓰기 위한 새 실행 장치다. 기존 영구 EMP·DEPT를 바꾸는 준비문이 아니다. 임시 표의 상세 수명·권한은 아래 TIP에서 구별한다.

</details>

```sql
START TRANSACTION;
DELETE FROM book_ledger WHERE id=1;
SELECT COUNT(*) FROM book_ledger;
ROLLBACK;
SELECT COUNT(*) FROM book_ledger;
START TRANSACTION;
DELETE FROM book_ledger WHERE id=1;
COMMIT;
ROLLBACK;
SELECT COUNT(*) FROM book_ledger;
```

준비에서 1행을 확정했다. 첫 트랜잭션에서 삭제하면 현재 COUNT는 0이지만 ROLLBACK 뒤 1이다. 다음 트랜잭션은 삭제 후 COMMIT하므로 그 뒤 ROLLBACK해도 0이다. 매번 같은 연결에서 관찰하며 원본 표가 아닌 book_ledger만 변경한다.

**가상 자료 기준 예상 결과:**

순서대로 COUNT는 **0 → 1 → 0**이다. 첫 삭제는 취소되어 돌아오고 두 번째 삭제는 확정되어 뒤 ROLLBACK으로 돌아오지 않는다.

행 변경·확정·취소 흐름은 SQLite의 별도 트랜잭션으로 교차 확인했다. START TRANSACTION을 BEGIN으로 대응하고 ENGINE 선언·준비 단계의 COMMIT을 제거했다. SQLite에서는 활성 트랜잭션이 없을 때 ROLLBACK이 오류이므로 확정 뒤 마지막 ROLLBACK 자체를 실행하지 않고 확정 상태가 유지됨을 확인했다. MariaDB의 빈 트랜잭션 명령·엔진·자동 커밋·DDL 경계까지 SQLite로 확인했다고 표시하지 않는다.

**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 851–873행 · **원본 발췌**

```sql
-- DELETE
-- delete from table로 원하는 대상만 제거할 수 있음 (from은 필수)
delete from emp2
where empno = 1002;
select * from emp2;

delete from emp2;
select * from emp2;

-- DDL은 자동 commit이기 때문에 그 시점 전으로는 되돌릴 수 없음
-- rollback은 마지막 DDL(CREATE, ALTER, DROP)을 실행하기 전으로 롤백해줌
rollback;
select * from emp2;
select * from dept2;

commit;
rollback;

delete from emp2
where empno = 1012;

rollback;
select * from emp2;
```

**발췌 바로 풀이:** 강사님은 `EMPNO=1002`를 지우고 롤백한 뒤, `COMMIT`·`ROLLBACK`, 다시 `EMPNO=1013` 삭제·롤백을 놓았다. 앞선 입력을 그대로 따라간 상태라면 1002가 없어 첫 삭제는 0행일 수 있다. 내 파일은 **조건 없는 전체 삭제**도 시험한다. 삭제 뒤 롤백으로 돌아오는지 보려면 **같은 연결에서, 자동 커밋이 꺼진 상태의 미확정 변경인지**를 먼저 확인해야 한다. 원본 문장만으로 언제나 복구된다고 약속하지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 746–749행 · **원본 발췌**

```sql
-- truncate 버림으로 테이블의 내용도 버릴 수 있음
-- 이후 배우는 delete는 롤백이 되지만, truncate는 롤백이 불가능
select * from emp_copy;
truncate table emp_copy;
```

**발췌 바로 풀이:** `DROP TABLE`은 표 자체를 없애고, `TRUNCATE TABLE`은 표의 모든 행을 비운다. 일반적인 MariaDB DDL은 암묵적 커밋을 동반할 수 있으므로 위 DML의 `ROLLBACK`과 같은 방식으로 취급하지 않는다. 내 주석 “롤백은 마지막 DDL을 실행하기 전으로 롤백”은 **반대로 이해하게 만드는 설명**이다. 이미 커밋된 DDL 이전 상태로 `ROLLBACK`만으로 돌아간다고 생각하면 안 된다.

내 원본에는 특정 번호 삭제와 전체 삭제 뒤 ROLLBACK이 있다. “마지막 DDL 실행하기 전으로 롤백”이라는 주석은 반대로 오해하게 한다. 이미 DDL 등으로 확정된 이전 상태로 자동 복귀하는 것이 아니다. 대상 번호 1002가 없으면 처음 삭제 자체가 0행일 수 있어 복구 시험으로도 충분하지 않다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

시작 상태 확인 → 트랜잭션 경계 → DML → 현재 연결 조회 → 확정 또는 취소 → 다시 조회다. 편집기의 자동 커밋·연결·표 엔진·앞선 DDL은 전제 조건이다. 같은 파일 문장을 읽었다고 실행 당시 이 설정까지 알 수 있는 것은 아니다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 원본에 COMMIT·ROLLBACK 전후 조회가 있어 확인하려는 의도가 보인다. **교정:** 확정 이전 변경과 확정 이후를 나눠 설명한다. **개선:** 실제 존재하는 행을 넣고 시작 값을 확인하는 별도 실습이 취소 흐름을 보기에 좋다. **상태 주의:** 원본 전체 파일의 유일한 고정 결과를 주장하지 않는다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽은 삭제·조회·ROLLBACK을 실험했지만 내 파일에는 조건 없는 전체 삭제도 있다. 어느 쪽이든 자동 커밋과 앞선 상태를 모르면 복구를 보장하지 못한다. 같은 구문 재인용 대신 새 독립 예제로 경계를 보인다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 단계 | 행 수 | 확정 상태 |
| --- | --- | --- |
| 준비 | 1 | 초기 값 확정 |
| 첫 DELETE | 0 | 미확정 |
| ROLLBACK | 1 | 삭제 취소 |
| 두 번째 DELETE·COMMIT | 0 | 삭제 확정 |
| 뒤 ROLLBACK | 0 | 이전 확정은 그대로 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 첫 ROLLBACK을 COMMIT으로 | 그 뒤 행 수 0 | 삭제 확정 |
| DELETE 조건 id99 | 계속 1 | 일치 행 없음 |
| DELETE 대신 amount=200 UPDATE | 취소 뒤 100 | 미확정 수정 취소 |

되돌아오지 않으면 정말 미확정 DML인지·같은 연결인지·지원 엔진인지 본다. 일반 DDL의 암묵 커밋을 놓치지 않는다. 임시 표가 사라진 것과 행 삭제가 취소되지 않은 것은 다른 문제다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 격리 수준·잠금·동시성 충돌·SAVEPOINT는 추가 학습이다. [암묵 커밋 문장 목록](https://mariadb.com/docs/server/reference/sql-statements/transactions/sql-statements-that-cause-an-implicit-commit)을 참고해 DDL 경계를 확인할 수 있다. 모든 DDL의 예외까지 외우는 문제로 확대하지 않는다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. COMMIT 뒤 ROLLBACK으로 이전 삭제를 취소하는가?
2. 첫 삭제 대상 행이 없으면 취소 흐름을 관찰하기 좋은가?
3. 임시 표 COMMIT은 영구 표로 바꾸는가?
4. 원본 문장만으로 자동 커밋을 알 수 있는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

이미 확정된 삭제는 취소하지 못한다. 변경이 없어 구분하기 어렵다. 임시 표 수명과 확정은 다르다. 당시 연결 설정 확인이 필요하다.

</details>

| 확인 | 핵심 |
| --- | --- |
| 경계 | 시작·확정·취소 |
| 전제 | 연결·엔진·자동 커밋 |
| DDL | 암묵 커밋 예외 구분 |

[장별 연습문제](실습/연습문제/16_SQL_Transaction_연습문제.md) · 다음은 [인덱스·자동 번호](17_SQL_Index와_AUTO_INCREMENT.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
