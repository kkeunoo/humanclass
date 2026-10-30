# 14. DDL과 제약조건 — 자료를 넣기 전에 표의 규칙 만들기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

조회는 현재 행을 읽지만 DDL은 그 자료를 담는 구조를 만든다. 열 이름·자료형·키·필수값·참조 관계를 정하고 변경 순서에 따라 실제 상태가 달라짐을 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

CREATE·ALTER·DROP·TRUNCATE의 대상과 차이를 설명한다. PRIMARY KEY·NOT NULL·FOREIGN KEY·DECIMAL 의미를 구분하고 조회 복사가 모든 제약 복제는 아니라는 점을 확인한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

표를 만들 때 열의 이름과 자료형을 적는다. 값의 규칙을 제약조건으로 선언하면 잘못된 자료가 저장되지 않도록 DB가 검사한다. 기본 키는 행을 식별하는 키이며 중복·NULL을 허용하지 않는다. NOT NULL은 값이 없음을 금지하지만 빈 문자열까지 자동으로 금지하는 것은 아니다.

| 항목 | 규칙 | 주의 |
| --- | --- | --- |
| INT | 정수 값 | INT(4)가 숫자 네 자리 최대라는 뜻은 아님 |
| VARCHAR(10) | 최대 길이를 정한 문자열 | 상세 문자셋·모드 영향 별도 |
| DECIMAL(7,2) | 전체 정밀도7·소수2 | 소수 앞까지7자리가 아님 |
| PRIMARY KEY | 행 식별·중복/NULL 금지 | 복합 키도 가능 |
| NOT NULL | NULL 금지 | 빈 문자열과 구별 |
| FOREIGN KEY | 다른 표 키와 참조 관계 | 부모·키·엔진·자료형 조건 확인 |

CREATE TABLE AS SELECT는 조회 결과의 열과 행을 새 표로 만드는 방식이다. WHERE 1<>1이면 행은 없다. 원본의 모든 키·제약·속성을 완전히 복제한 것으로 보면 안 된다. ALTER는 기존 구조, DROP은 표 자체, TRUNCATE는 전체 행을 비우는 문법이며 MariaDB 트랜잭션과의 경계도16장에서 다룬다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table), [ALTER TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/alter/alter-table). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/14_SQL_DDL과_제약조건.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
DROP TEMPORARY TABLE IF EXISTS book_rules;
CREATE TEMPORARY TABLE book_rules (
 empno INT NOT NULL PRIMARY KEY, ename VARCHAR(20) NOT NULL
);
INSERT INTO book_rules(empno,ename) VALUES(1,'ADA');
SELECT empno,ename FROM book_rules;
ALTER TABLE book_rules ADD note VARCHAR(20);
SELECT empno,ename,note FROM book_rules;
```

CREATE가 규칙을 만들고 INSERT가 실제 ADA행을 넣는다. ALTER ADD로 note열을 늘리면 기존 행에도 새 열을 볼 수 있으며 값을 지정하지 않아NULL이다. 같은 empno를 다시 쓰면 기본 키 중복이고 ename=NULL은 필수값 제약 위반이다. 코드의 INT NOT NULL PRIMARY KEY는 두 테스트 엔진의 차이를 피하려 명시적으로 적었다.

**가상 자료 기준 예상 결과:**

열 추가 전은 **1·ADA 한 행**, 추가 후는 **1·ADA·NULL 한 행**이다. 별도 실험으로 같은 번호1 재입력, 이름NULL 입력은 제약에 걸린다. 실패 실험은 위 정상 전체 코드에 섞지 않았다.

새 임시 표의 생성·행·열 추가·기본 키/NOT NULL 거부를 SQLite에서 교차 확인했다. MariaDB의 정확한 오류 번호·DDL 암묵 커밋·외래 키 작동은 이 교차 실행으로 증명하지 않는다. 이 임시 표에는 외래 키를 선언하지 않았다.

**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 640–667행 · **원본 발췌**

```sql
-- DDL의 시작 _ CREATE TABLE
-- desc TABLE은 구조를 알려주는 디스크립션 명령어
desc emp;

-- foreign key는 참조 할 테이블이 있어야 가능하기 때문에, PK만 먼저 쓴 것
-- 만약, dept2에 deptno가 10~40일 때 emp2에 값을 넣을 때 그 외의 것은 넣지 못하도록
-- unique + not null = primary key
create table emp2(
	empno int(4) primary key,
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7,2), -- 총 7자리 중, 소수점 2자리
	comm decimal(7,2),
	deptno int(2)
);
select * from emp2;
desc emp2;

desc dept;
create table dept2(
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);
select * from dept2;
desc dept2;
```

**발췌 바로 풀이:** `EMPNO`의 `PRIMARY KEY`는 사원 번호를 중복 없이 식별하고, `ENAME ... NOT NULL`은 이름을 비워 둘 수 없게 한다. `DECIMAL(7,2)`는 전체 정밀도와 소수 자리 수를 지정한다. `DESC emp2`는 만들어진 표의 구조를 확인하는 실습 명령이다. 내 코드에는 `DESC dept2`까지 있어 만든 두 표를 각각 확인한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 669–684행 · **원본 발췌**

```sql
-- 테이블 구조 복사 (as로 모든것을 가져올 수 있음)
create table emp_copy 
as select * from emp;

select * from emp_copy;
desc emp_copy;

-- 아래처럼 내용물 없이 False를 줘서 껍데기만 들고올 수 있음
create table emp_copy2
as select * from emp where 1 <> 1;

select * from emp_copy2;

create table dept3
as select * from dept where 1 != 1;
select * from dept3;
```

**발췌 바로 풀이:** `CREATE TABLE emp_copy AS SELECT * FROM emp`는 조회 결과의 **행까지** 새 표에 담는다. `WHERE 1 <> 1`은 항상 거짓이므로 조회 결과 행이 없고, 새 표만 만든다. 다만 `CREATE TABLE ... AS SELECT`가 원본의 **모든 키·제약조건까지 그대로 복제**한다고 생각하면 안 된다. 두 원본은 복사 뒤 `SELECT`로 행 유무를 확인했다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 686–711행 · **원본 발췌**

```sql
create table emp3 (
	empno int(4),
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7,2),
	comm decimal(7,2),
	deptno int(2),
	primary key (empno), -- 여러 개가 필요할 때 직접적으로 안 주고 하단에 별도 작성 가능
	foreign key (deptno) references dept3(deptno) -- foreign key는 primary key만 잡힘
);

desc dept3;
-- 테이블 삭제
drop table dept3;

create table dept3(
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);
desc dept3;
desc emp3;
-- 이렇게 한 번 참조해두고 나면, dept3을 먼저 지울 수 없고
-- 지우게 된다면 emp3를 먼저 지우과서 dept3을 지워야 함 (emp3 → dept3를 바라보고 있기 때문)
```

**발췌 바로 풀이:** `EMP3.DEPTNO`가 `DEPT3.DEPTNO`를 참조하므로, 자식 표에 없는 부서 번호를 마음대로 넣을 수 없고 참조 중인 부모 표의 삭제도 막힐 수 있다. 여기에는 중요한 **실행 순서 함정**이 있다. 두 파일 모두 먼저 `CREATE TABLE dept3 AS SELECT ... WHERE 1 != 1`로 `DEPT3`를 만들고, 이어 `EMP3`에서 그 열을 외래 키로 참조하려 한다. 복사로 만든 `DEPT3`에는 기본 키가 명시되지 않았다. 해당 `EMP3` 생성이 성공했다고 단정할 수 없다. 뒤에서 `DEPT3`를 지우고 기본 키를 가진 형태로 다시 만드는 문장도 보인다. 내 주석의 “외래 키는 기본 키만 참조”는 모든 경우의 규칙으로 넓히지 않는다. **이 실습에서는 참조 대상 `DEPT3.DEPTNO`가 키로 준비됐는지** 먼저 확인해야 한다. 스크립트는 완성된 순차 실행본이 아니라 실습 기록이다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 713–749행 · **원본 발췌**

```sql
-- ALTER TABLE (테이블 수정)
-- 열 추가 및 열 삭제
alter table emp3 
add gender varchar(10) not null default '남';
select * from emp3;

-- 열을 바꿀 때 자료형은 다시 써줘야 함
alter table emp3
change gender gender2 varchar(10);
select * from emp3;

-- 최신 Oracle방식은 자료형을 쓰지 않아도 됨
-- 단, 실무에서 먹히지 않는 곳도 있기 때문에 유의해야 함
alter table emp3
rename column gender2 to gender3;
select * from emp3;

alter table emp3
drop column gender;
select * from emp3;

-- rename to로 테이블명도 변경할 수 있다
alter table emp3
rename to emp4;
select * from emp3;
select * from emp4;

drop table emp4;
select * from emp4;
-- emp4를 먼저 지웠기 때문에, 참조되는 부모 dept3을 지울 수 있음
drop table dept3;
select * from dept3;

-- truncate 버림으로 테이블의 내용도 버릴 수 있음
-- 이후 배우는 delete는 롤백이 되지만, truncate는 롤백이 불가능
select * from emp_copy;
truncate table emp_copy;
```

**발췌 바로 풀이:** `ALTER TABLE ... ADD`는 열 추가, `CHANGE`는 열 이름과 자료형을 함께 적는 변경, `RENAME COLUMN`은 열 이름 변경, `RENAME TO`는 표 이름 변경이다. **두 원본 모두** `gender` → `gender2` → `gender3`으로 이름을 바꾼 뒤 `DROP COLUMN gender`를 적었다. 그 시점에 `gender`는 이미 없으므로 그 삭제 문장은 실패할 수 있다. 이어 `DROP TABLE`과 `TRUNCATE TABLE`은 데이터에 큰 변화를 주므로 이 문서에서는 실행하지 않고 원본을 비교했다.

내 EMP2는 기본 키·이름 필수·급여 정밀도를 정의하고 DESC로 확인한다. 복사한 DEPT3에 키가 없는 상태에서 EMP3 외래 키를 만들려는 구간은 성공을 보장하지 않는다. gender→gender2→gender3으로 바꾼 뒤 DROP COLUMN gender는 이미 없는 이름을 지우려는 문장이다. 표를 emp4로 바꾼 뒤 emp3 조회도 새 이름 상태와 맞지 않는다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

부모 표·참조 키 준비 → 자식 표 참조 선언 → 입력 → 구조 변경 → 그때의 열·표 이름으로 조회 순서다. 원본 기록은 실패·재생성 시도가 섞여 있어 파일 순서 전체가 성공 경로가 아니다. 외래 키를 TEMPORARY 예제에서 재현한 것이 아니라 원본 영구 표 정의에서 설명한다. MariaDB 임시 표는 외래 키 기능의 대체 실습이 아니다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** CREATE 뒤 DESC·SELECT를 확인해 구조와 행을 나눴다. **교정:** AS SELECT로 “모든 것”을 가져온다는 주석은 제약까지 자동 보존한다고 읽지 않는다. 외래 키는 기본 키만 참조한다는 일반화도 실제 키·엔진 요건을 더 확인해야 한다. **순서 오류:** 이름 변경 뒤 이전 열을 삭제하는 문제는 양쪽에 있다. **개선:** 현재 구조 이름을 단계마다 확인하고 해당 상태를 기준으로 다음 문장을 적는다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님도 gender이름 변경 뒤 옛 이름 삭제를 적어 같은 함정이 있다. 강사님 원본이라는 이유만으로 성공하는 완성 설치본으로 제시하지 않는다. 내 DESC추가 확인은 구조 추적에 도움이 된다. 기본구문은 중복 인용하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 단계 | 표의 열 | 행 |
| --- | --- | --- |
| CREATE | empno·ename | 없음 |
| INSERT | 동일 | 1·ADA |
| ADD note | empno·ename·note | 1·ADA·NULL |
| 원본 rename 실험 | gender→gender2→gender3 | 현재 이름 갱신 필요 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 같은 번호1 삽입 | 중복 거부 | 기본 키 |
| ename에 NULL | 거부 | NOT NULL |
| ename에 빈 문자열 | NOT NULL만으로는 막지 않음 | NULL과 다름 |
| 새 note에 값 지정 | 해당 값 표시 | 새 열의 행 값 |

이미 표가 있으면 현재 대상과 준비 절차를 확인한다. 외래 키 생성 실패는 부모 존재뿐 아니라 키·열 규칙·지원 엔진을 본다. 열 없음 오류면 앞선 rename 이후 이름을 확인한다. 임시 표로 실험했다고 영구 DDL도 롤백될 것으로 추측하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 정확한 외래 키 인덱스 요건·CASCADE 정책·제약 복제·스키마 이전 도구는 추가 학습이다. [MariaDB Foreign Keys](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys)에서 현재 엔진 조건을 확인한다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. NOT NULL이 빈 문자열도 금지하는가?
2. DECIMAL(7,2)의 전체 정밀도는?
3. AS SELECT가 모든 키를 복제하는가?
4. gender3으로 바꾼 뒤 gender를 지우면?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

아니다. 전체7자리 중 소수2다. 모든 제약 복제를 보장하지 않는다. 그 이름이 없어 실패할 수 있다.

</details>

| 구별 | 대상 |
| --- | --- |
| 구조 | CREATE·ALTER |
| 표 삭제 | DROP |
| 행 전체 비움 | TRUNCATE |
| 규칙 | 키·NULL·참조 |

[장별 연습문제](실습/연습문제/14_SQL_DDL과_제약조건_연습문제.md) · 다음은 [DML](15_SQL_DML.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
