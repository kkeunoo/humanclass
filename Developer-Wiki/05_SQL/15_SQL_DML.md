# 15. DML — 행 넣기·고치기·지우기

[SQL 목차](README.md) · [이전: DDL](14_SQL_DDL과_제약조건.md) · [다음: 트랜잭션](16_SQL_Transaction.md)

`INSERT`, `UPDATE`, `DELETE`는 실제 저장된 행을 바꾼다. 두 원본에는 성공 예제와 **일부러 오류를 내거나 0행만 바꾸는 예제**가 섞여 있다. 처음부터 끝까지 일괄 실행한 결과라고 읽지 않는다.

<!-- chapter-toc -->

- [1. 열을 모두 넣기와 일부 열만 넣기](#section-1)
- [2. 제약조건이 막는 입력](#section-2)
- [3. `UPDATE`와 `DELETE`의 대상 행](#section-3)
- [직접 확인할 질문](#section-4)
- [추가로 알면 좋은 것](#section-5)

<a id="section-1"></a>

## 1. 열을 모두 넣기와 일부 열만 넣기

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 714–738행 · **원본 발췌**

```sql
insert into dept2
values (
	10,
	'휴먼',
	'천안'
);




insert into emp2
values (
	1000, 
	'최민수', 
	'MANAGER', 
	2000, 
	'2026-08-09',
	4000,
	100,
	10
);
select * from emp2;

insert into emp2 (empno, ename, sal, comm, deptno)
values (1001, '강사최민수', 4100, 150, 10);
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 778–803행 · **원본 발췌**

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

열 목록을 쓰지 않으면 표의 열 순서에 맞춰 **모든 열 값**을 넣는다. 열 목록을 적으면 필요한 열만 지정하고 나머지는 기본값 또는 허용된 `NULL`이 된다. 강사님은 `강사최민수`, 나는 `홍길동`을 넣어 같은 구조를 연습했다. 실제 이름과 숫자는 각각 원본 그대로 둔다.

<a id="section-2"></a>

## 2. 제약조건이 막는 입력

### 강사님 코드 — 주석으로 남긴 실패 실험

출처: `teacher/workspace_sql/Script.sql` 740–759행 · **원본 발췌**

```sql
-- ename은 not null 제한. 
-- insert에 누락하면 null이 들어간다
-- 그래서 에러 발생
/*
insert into emp2 (empno, sal, comm, deptno)
values (1001, 4100, 150, 10);
*/

-- primary key
-- unique + not null
/*
insert into emp2 (empno, ename, sal, comm, deptno)
values (1001, '강사', 4100, 150, 10);
*/

-- dept 테이블에 deptno 20값이 없어서 에러
/*
insert into emp2 (empno, ename, sal, comm, deptno)
values (1002, '강사', 4100, 150, 20);
*/
```

### 내 코드 — 오류 기록과 주석 문장

출처: `me/workspace_sql/Script.sql` 805–819행 · **원본 발췌**

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

이름을 빼면 `NOT NULL`, 기존 사원 번호를 다시 넣으면 `PRIMARY KEY`, 부모 `DEPT2`에 없는 부서 번호를 넣으면 `FOREIGN KEY`에 걸린다. **강사님 코드는 실패 문장을 블록 주석으로 막았고**, 내 코드는 오류 문구와 실패 문장을 주석으로 보관했다. 실제 실행 결과는 현재 테이블 상태에 달리므로 오류 번호만 외우지 않는다.

<a id="section-3"></a>

## 3. `UPDATE`와 `DELETE`의 대상 행

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 769–803행 · **원본 발췌**

```sql
-- update
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

select * from dept2;
update dept2
set deptno = 20
where deptno = 10;


delete from emp2
where empno = 1002;
select * from emp2;

rollback;
select * from emp2;
select * from dept2;

commit;
rollback;
delete from emp2
where empno = 1013;
select * from emp2;
rollback;
select * from emp2;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 828–858행 · **원본 발췌**

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

`UPDATE emp2 SET sal = 1000, comm = 200`에는 `WHERE`가 없어 **모든 행**이 대상이다. 반면 `WHERE empno = 1002`가 있으면 그 번호만 대상이다. 다만 양쪽 원본의 앞선 성공 `INSERT`는 1000, 1001, 1012–1014를 넣었고 **1002를 성공적으로 넣은 문장은 보이지 않는다**. 같은 실습 상태라면 그 `UPDATE`와 강사님의 `DELETE WHERE empno = 1002`는 0행을 바꾼다. 내 파일의 `DELETE FROM emp2`에는 조건이 없어 모든 행을 삭제하는 문장도 있다. 이 문서에서는 원본 표를 변경하지 않고 범위를 읽었다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `INSERT`에서 열 목록을 생략하면 값은 어떤 순서로 넣어야 하는가?
2. `UPDATE`에 `WHERE`가 없으면 어느 행이 대상인가?
3. 원본의 성공한 입력만 기준으로 `EMPNO=1002`가 있는가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

대량 입력과 UPSERT, 변경 전후 행 수 점검 절차는 실무에서 유용하다. 본문은 수업에서 실제 쓴 **세 DML의 대상 행과 제약조건**을 읽는 데 맞춘다.
