# 15. DML — 어떤 행을 넣고 바꾸고 지우는가

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

INSERT·UPDATE·DELETE는 조회 결과만 꾸미는 문장이 아니다. 실제 행을 바꾸므로 대상 조건과 변경 전후를 같은 데이터에서 따라간다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

열 목록과 VALUES의 대응, UPDATE의 기존 값 사용, DELETE 대상 조건을 설명한다. 제약 오류·0행 변경·전체 행 변경을 구분한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

INSERT는 새 행을 넣고 UPDATE는 기존 행의 열 값을 바꾸며 DELETE는 행을 지운다. 이름이 비슷해도 SELECT의 계산과 UPDATE의 대입은 다르다. UPDATE SET sal=sal+100은 각 대상 행의 기존 급여를 읽고 새 값으로 저장한다.

| 문장 | 대상 | 조건이 없을 때 |
| --- | --- | --- |
| INSERT | 새 행 | VALUES의 열 대응 확인 |
| UPDATE | 기존 행의 값 | 모든 행 대상 |
| DELETE | 기존 행 | 모든 행 대상 |

INSERT에 열 목록을 쓰면 그 순서와 VALUES를 대응한다. 생략한 열은 기본값·NULL 허용 여부에 영향을 받는다. 필수값·중복 키·부모 참조 제약을 위반하면 실패한다. 조건에 맞는 기존 행이 없으면 UPDATE·DELETE가0행을 대상으로 끝날 수도 있다. SQL이 실행됐다는 사실과 실제 자료가 바뀌었다는 사실을 구별한다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB INSERT](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [UPDATE](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/changing-deleting-data/update), [DELETE](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/changing-deleting-data/delete). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/15_SQL_DML.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
```

표 생성·삽입 문법은 14·15장에서 설명한다. TEMPORARY는 원래 수업 구문으로 승격한 것이 아니라 예제 자료를 연결 안에서만 쓰기 위한 새 실행 장치다. 기존 영구 EMP·DEPT를 바꾸는 준비문이 아니다. 임시 표의 상세 수명·권한은 아래 TIP에서 구별한다.

</details>

```sql
INSERT INTO book_emp(empno,ename,job,mgr,sal,comm,deptno)
VALUES(7,'GUS','CLERK',3,1200,NULL,20);
SELECT empno,ename,sal FROM book_emp WHERE empno=7;
UPDATE book_emp SET sal=sal+100 WHERE empno=7;
SELECT empno,ename,sal FROM book_emp WHERE empno=7;
DELETE FROM book_emp WHERE empno=7;
SELECT COUNT(*) FROM book_emp;
```

열 목록의 순서대로 GUS자료를 넣는다. 다음 UPDATE는7번만 선택해 기존1200에100을 더한다. DELETE도7번만 지우므로 원래 여섯 사람은 남는다. 마지막 COUNT를 확인하면 삭제 대상과 전체 표 삭제가 다르다는 점을 볼 수 있다.

**가상 자료 기준 예상 결과:**

삽입 뒤 **7·GUS·1200**, 수정 뒤 **7·GUS·1300**, 삭제 뒤 전체 인원은 원래의 **6명**이다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 778–803행 · **원본 발췌**

```sql
insert into dept2
values (
	10,
	'휴먼',
	'천안'
);
select * from dept2;

-- column을 지정하지 않았을 경우에는 values에 모두 적어야 함
insert into emp2
values (
	1000, 
	'정근욱', 
	'MANAGER', 
	2000, 
	'2026-08-09', 
	4000,
	100,
	10
);
select * from emp2;

-- 기존에 default가 되어있거나, NOT NULL이 아닌 경우 넣고 싶은 column 값만 넣을 수 있음
insert into emp2 (empno, ename, sal, comm, deptno)
values (1001, '홍길동', 4100, 150, 10);
select * from emp2;
```

**발췌 바로 풀이:** 열 목록을 쓰지 않으면 표의 열 순서에 맞춰 **모든 열 값**을 넣는다. 열 목록을 적으면 필요한 열만 지정하고 나머지는 기본값 또는 허용된 `NULL`이 된다. 강사님은 `강사최민수`, 나는 `홍길동`을 넣어 같은 구조를 연습했다. 실제 이름과 숫자는 각각 원본 그대로 둔다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 805–819행 · **원본 발췌**

```sql
-- ename은 insert 누락 시 NULL이 들어가나 NOT NULL 제한이 있기에 에러 발생
-- SQL Error [1364] [HY000]: (conn=5) Field 'ename' doesn't have a default value
-- insert into emp2 (empno, sal, comm, deptno)
-- values (1001, 4100, 150, 10);

-- Primaty key이며 unique와 not null 형태이기 때문에 중복값이 들어갈 수 없는 오류(Duplicate) 발생
-- SQL Error [1062] [23000]: (conn=5) Duplicate entry '1001' for key 'PRIMARY'
-- insert into emp2 (empno, ename, sal, comm, deptno)
-- values (1001, '홍길동', 4100, 150, 10);

-- dept 테이블에 deptno '20'값이 없기 때문에 발생되는 에러
-- SQL Error [1452] [23000]: (conn=5) Cannot add or update a child row: 
-- a foreign key constraint fails (`human`.`emp2`, CONSTRAINT `1` FOREIGN KEY (`deptno`) REFERENCES `dept2` (`deptno`))
-- insert into emp2 (empno, ename, sal, comm, deptno)
-- values (1002, '홍길동', 4100, 150, 20);
```

**발췌 바로 풀이:** 이름을 빼면 `NOT NULL`, 기존 사원 번호를 다시 넣으면 `PRIMARY KEY`, 부모 `DEPT2`에 없는 부서 번호를 넣으면 `FOREIGN KEY`에 걸린다. **강사님 코드는 실패 문장을 블록 주석으로 막았고**, 내 코드는 오류 문구와 실패 문장을 주석으로 보관했다. 실제 실행 결과는 현재 테이블 상태에 달리므로 오류 번호만 외우지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 828–858행 · **원본 발췌**

```sql
-- UPDATE
-- where문을 사용하지 않았을 땐 모든 값이 바뀌기 때문에 조심해야 함
update emp2
set 
	sal = 1000,
	comm = 200;
select * from emp2;

update emp2
set 
	sal = sal * 1.1,
	comm = comm * 1.2
where empno = 1002;
select * from emp2;

-- dept 테이블에서도 서로 참조를 하고 있기 때문에 변경할 수 없음
-- SQL Error [1451] [23000]: (conn=5) Cannot delete or update a parent row: 
-- a foreign key constraint fails (`human`.`emp2`, CONSTRAINT `1` FOREIGN KEY (`deptno`) REFERENCES `dept2` (`deptno`))
select * from dept2;
update dept2
set deptno = 20
where deptno = 10;

-- DELETE
-- delete from table로 원하는 대상만 제거할 수 있음 (from은 필수)
delete from emp2
where empno = 1002;
select * from emp2;

delete from emp2;
select * from emp2;
```

**발췌 바로 풀이:** `UPDATE emp2 SET sal = 1000, comm = 200`에는 `WHERE`가 없어 **모든 행**이 대상이다. 반면 `WHERE empno = 1002`가 있으면 그 번호만 대상이다. 다만 양쪽 원본의 앞선 성공 `INSERT`는 1000, 1001, 1012–1014를 넣었고 **1002를 성공적으로 넣은 문장은 보이지 않는다**. 같은 실습 상태라면 그 `UPDATE`와 강사님의 `DELETE WHERE empno = 1002`는 0행을 바꾼다. 내 파일의 `DELETE FROM emp2`에는 조건이 없어 모든 행을 삭제하는 문장도 있다. 이 문서에서는 원본 표를 변경하지 않고 범위를 읽었다.

내 원본은 모든 열 INSERT와 일부 열 INSERT를 비교하고 실제 오류문구를 주석으로 남겼다. 첫 UPDATE에는 WHERE가 없어 전체가 바뀐다. 뒤의1002번 UPDATE·DELETE는 해당 행이 있어야 바뀐다. 앞선 성공 INSERT기록만 기준으로1002는 없어0행일 수 있다. 내 마지막 조건 없는 DELETE는 표의 모든 행을 대상으로 한다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

표의 현재 구조·제약 → 열/값 대응 INSERT → 현재 존재 행 → WHERE대상 → SET계산 또는 삭제 → SELECT로 상태 확인이다. 다른 파일의 함수 호출은 없고 같은 연결에서 공유하는 표의 상태가 다음 문장 입력이 된다. SQL편집기에서 일부 문장만 실행했으면 앞선 상태도 달라질 수 있다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 원본은 성공 입력과 오류를 주석으로 구별하고 WHERE누락 영향을 적었다. **교정:** 부모·자식이 서로 똑같이 참조한다고 이해하지 말고 실제 외래 키 방향과 제약을 읽는다. **개선:** 먼저 같은 WHERE의 SELECT로 대상을 확인하고 필요한 열 목록을 INSERT에 명시하면 목적을 추적하기 좋다. 원본의0행 변경을 성공 수정으로 설명하지 않는다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 입력 이름은 다르지만 열 구조와 제약 실험은 같은 목적이다. 사람 이름의 차이는 우열 기준이 아니다. 강사님1002번도 같은 상태 전제에서는0행일 수 있다. 중복된 전체 DML을 인용하지 않고 대상 행과 실제 주석을 중심으로 읽는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 단계 | GUS존재 | GUS급여 | 총 인원 |
| --- | --- | --- | --- |
| 시작 | 없음 | 없음 | 6 |
| INSERT | 있음 | 1200 | 7 |
| UPDATE | 있음 | 1300 | 7 |
| DELETE | 없음 | 없음 | 6 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| UPDATE번호를99로 | GUS1200유지 | 일치행 없음 |
| DELETE번호를99로 | 총7명유지 | 삭제대상 없음 |
| WHERE없는UPDATE를 별도 새 예제에서 비교 | 전체 대상 | 행 제한 없음 |

변경이 없으면 조건 행이 존재하는지 본다. 여러 행이 바뀌면 WHERE조건 범위를 확인한다. 중복 키 오류는 새 번호·기존행을 구분하고 필수값 누락은 실제 구조를 본다. 결과값만 보고 영향 행 수와 DB설정을 혼동하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** UPSERT·대량 입력·변경 이력·동시성 처리·일관된 영향행 보고는 추가 학습이다. 이번 기본은 세 DML의 대상·제약·상태변화다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. UPDATE에서WHERE를 빼면?
2. 없는99번을 지우면 반드시오류인가?
3. SELECT sal+100과 UPDATE SET sal=sal+100은 같은가?
4. INSERT의열목록 순서는 무엇과 맞추나?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

모든행이 대상이다. 일치행0개일 수 있다. 조회계산과 저장변경이다. VALUES각값과 대응한다.

</details>

| 변경 | 점검 |
| --- | --- |
| INSERT | 열·값·제약 |
| UPDATE | 조건·기존값 |
| DELETE | 조건·전체대상 |

[장별 연습문제](실습/연습문제/15_SQL_DML_연습문제.md) · 다음은 [트랜잭션](16_SQL_Transaction.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
