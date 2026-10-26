# 14. DDL과 제약조건 — 표의 구조 만들기

[SQL 목차](README.md) · [이전: 외부·자기 조인](13_SQL_Outer_JOIN과_Self_JOIN.md) · [다음: DML](15_SQL_DML.md)

`CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `TRUNCATE TABLE`은 조회 문장과 달리 표의 **구조나 저장된 행**을 바꾼다. 두 원본은 `EMP2`·`DEPT2` 같은 실습 표를 사용했지만, 그대로 한 번에 실행하면 이미 있는 표·외래 키·실패 실험과 충돌할 수 있다. 한 문장씩 현재 표 상태를 확인하며 읽는다.

<!-- chapter-toc -->

- [1. 표 만들기와 기본 제약](14_SQL_DDL과_제약조건.md#section-1)
- [2. 데이터까지 복사할까, 구조만 만들까](14_SQL_DDL과_제약조건.md#section-2)
- [3. 외래 키는 이미 있는 부모 키를 참조](14_SQL_DDL과_제약조건.md#section-3)
- [4. 열·표 이름 변경과 삭제](14_SQL_DDL과_제약조건.md#section-4)
- [직접 확인할 질문](14_SQL_DDL과_제약조건.md#section-5)
- [추가로 알면 좋은 것](14_SQL_DDL과_제약조건.md#section-6)

<a id="section-1"></a>

## 1. 표 만들기와 기본 제약

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 600–623행 · **원본 발췌**

```sql
-- DDL
-- create
desc emp;

create table emp2(
	empno int(4) primary key,
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7, 2), -- 총 7자리, 그 중 2자리 소수점
	comm decimal(7,2),
	deptno int(2)
);
select * from emp2;
desc emp2;

desc dept;
create table dept2 (
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);
select * from dept2;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 640–667행 · **원본 발췌**

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

`EMPNO`의 `PRIMARY KEY`는 사원 번호를 중복 없이 식별하고, `ENAME ... NOT NULL`은 이름을 비워 둘 수 없게 한다. `DECIMAL(7,2)`는 전체 정밀도와 소수 자리 수를 지정한다. `DESC emp2`는 만들어진 표의 구조를 확인하는 실습 명령이다. 내 코드에는 `DESC dept2`까지 있어 만든 두 표를 각각 확인한다.

<a id="section-2"></a>

## 2. 데이터까지 복사할까, 구조만 만들까

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 625–638행 · **원본 발췌**

```sql
-- 테이블 복사
create table emp_copy
as select * from emp;

select * from emp_copy;

create table emp_copy2
as select * from emp where 1 <> 1;

select * from emp_copy2;

create table dept3
as select * from dept where 1 != 1;
select * from dept3;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 669–684행 · **원본 발췌**

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

`CREATE TABLE emp_copy AS SELECT * FROM emp`는 조회 결과의 **행까지** 새 표에 담는다. `WHERE 1 <> 1`은 항상 거짓이므로 조회 결과 행이 없고, 새 표만 만든다. 다만 `CREATE TABLE ... AS SELECT`가 원본의 **모든 키·제약조건까지 그대로 복제**한다고 생각하면 안 된다. 두 원본은 복사 뒤 `SELECT`로 행 유무를 확인했다.

<a id="section-3"></a>

## 3. 외래 키는 이미 있는 부모 키를 참조

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 640–660행 · **원본 발췌**

```sql
create table emp3 (
	empno int(4),
	ename varchar(10) not null,
	job varchar(9),
	mgr int(4),
	hiredate date,
	sal decimal(7, 2), -- 총 7자리, 그 중 2자리 소수점
	comm decimal(7,2),
	deptno int(2),
	primary key (empno), 
	foreign key (deptno) references dept3(deptno)
);

-- 테이블 삭제
drop table dept3;

create table dept3 (
	deptno int(2) primary key,
	dname varchar(14),
	loc varchar(13)
);
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 686–711행 · **원본 발췌**

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

`EMP3.DEPTNO`가 `DEPT3.DEPTNO`를 참조하므로, 자식 표에 없는 부서 번호를 마음대로 넣을 수 없고 참조 중인 부모 표의 삭제도 막힐 수 있다. 여기에는 중요한 **실행 순서 함정**이 있다. 두 파일 모두 먼저 `CREATE TABLE dept3 AS SELECT ... WHERE 1 != 1`로 `DEPT3`를 만들고, 이어 `EMP3`에서 그 열을 외래 키로 참조하려 한다. 복사로 만든 `DEPT3`에는 기본 키가 명시되지 않았다. 해당 `EMP3` 생성이 성공했다고 단정할 수 없다. 뒤에서 `DEPT3`를 지우고 기본 키를 가진 형태로 다시 만드는 문장도 보인다. **스크립트는 완성된 순차 실행본이 아니라 실습 기록**이다.

<a id="section-4"></a>

## 4. 열·표 이름 변경과 삭제

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 662–687행 · **원본 발췌**

```sql
-- alter
alter table emp3
add gender varchar(10) not null default '남';
select * from emp3;

alter table emp3
change gender gender2 varchar(10);
select * from emp3;

alter table emp3
rename column gender2 to gender3;
select * from emp3;

alter table emp3
drop column gender;
select * from emp3;

alter table emp3
rename to emp4;
select * from emp4;

drop table emp4;
drop table dept3;

select * from emp_copy;
truncate table emp_copy;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 713–749행 · **원본 발췌**

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

`ALTER TABLE ... ADD`는 열 추가, `CHANGE`는 열 이름과 자료형을 함께 적는 변경, `RENAME COLUMN`은 열 이름 변경, `RENAME TO`는 표 이름 변경이다. 내 코드에서는 `gender` → `gender2` → `gender3`으로 이름을 바꾼 뒤 **`DROP COLUMN gender`**를 적었다. 그 시점에 `gender`는 이미 없으므로 그 삭제 문장은 실패할 수 있다. 이어 `DROP TABLE`과 `TRUNCATE TABLE`은 데이터에 큰 변화를 주므로 이 문서에서는 실행하지 않고 원본을 비교했다.

<a id="section-5"></a>

## 직접 확인할 질문

1. `PRIMARY KEY`와 `NOT NULL`은 각각 무엇을 제한하는가?
2. `CREATE TABLE ... AS SELECT ... WHERE 1 <> 1`에는 행이 들어가는가?
3. 내 코드에서 `DROP COLUMN gender` 이전에 열 이름은 어떻게 바뀌었는가?

<a id="section-6"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/14_SQL_DDL과_제약조건_연습문제.md)

## 추가로 알면 좋은 것

표 복사 시 제약조건 재현 방법, DBMS마다 다른 DDL 트랜잭션 처리, 운영 데이터 이전 절차는 별도 주제다. 이 장은 실제 원본의 **표 생성·복사·제약·변경 순서**를 정확히 읽는 데 집중한다.
