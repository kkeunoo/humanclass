# 17. 인덱스와 `AUTO_INCREMENT` — 찾는 길과 자동 번호

[SQL 목차](README.md) · [이전: 트랜잭션](16_SQL_Transaction.md) · [다음: 재귀 CTE](18_SQL_Recursive_CTE.md)

양쪽 원본은 인덱스를 만들고 조회하며, 새 표의 사원 번호를 자동으로 늘렸다. **인덱스를 만들었다는 사실과 실제로 사용되었다는 사실은 다르다.** 수업 스크립트에는 실행 계획 측정 결과가 없으므로 성능 향상을 확정하지 않는다.

<!-- chapter-toc -->

- [1. `CREATE INDEX`와 강제 지정](#section-1)
- [2. 자동 번호와 `MAX(id)+1`의 차이](#section-2)
- [3. 문자열 길이 실험](#section-3)
- [직접 확인할 질문](#section-4)
- [추가로 알면 좋은 것](#section-5)

<a id="section-1"></a>

## 1. `CREATE INDEX`와 강제 지정

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 811–833행 · **원본 발췌**

```sql
select * from emp
order by empno desc;

-- index
create index idx_emp_empno_desc
on emp(empno desc);

select * from emp
order by empno desc;

select * from emp
where deptno = 10;

create index idx_emp_deptno
on emp(deptno);

select * from emp
where deptno = 10;

select *
from emp force index (idx_emp_deptno)
where deptno = 10
order by deptno;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 881–903행 · **원본 발췌**

```sql
select * from emp
where deptno = 10;

-- index 생성
create index idx_emp_empno_desc
on emp(empno desc);

-- index를 타면 emp (index) 형식으로 표시된다
-- 보통 데이터가 많았을 때 검색 속도가 빨라짐, 최신순은 역순(desc)로 검색하기도 함
select * from emp
order by empno desc;

create index idx_emp_deptno
on emp(deptno);

select * from emp
where deptno = 10;

-- 강제로 index를 타게 할 수 있음
select * 
from emp force index (idx_emp_deptno)
where deptno = 10
order by deptno;
```

`ON emp(deptno)`는 부서 번호 열에 인덱스를 만든다. `FORCE INDEX (idx_emp_deptno)`는 해당 인덱스를 사용하도록 힌트를 주는 실습이다. 내 주석의 “인덱스를 타면 emp (index) 형식으로 표시”는 **조회 결과 표만 보고 확인할 수 있는 일반 규칙이 아니다**. 이 두 파일에는 `EXPLAIN` 결과가 남아 있지 않다. 데이터가 작은 학습용 `EMP`에서는 인덱스를 만든 후에도 무조건 빨라진다고 말할 수 없다.

<a id="section-2"></a>

## 2. 자동 번호와 `MAX(id)+1`의 차이

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 839–856행 · **원본 발췌**

```sql
select max(empno)+1 from emp;

-- sequence
create table emp_auto (
	empno int auto_increment,
	ename varchar(50),

	primary key(empno)
);

insert into emp_auto (ename)
values ('민수');

select * from emp_auto;

insert into emp_auto (ename)
values ('민수2');
select * from emp_auto;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 911–928행 · **원본 발췌**

```sql
select max(empno)+1 from emp;

-- increment는 Primary Key일때만 가능
-- 아래처럼 함수형태로 만들어서 사용할 수 있다
create table emp_auto (
	empno int auto_increment, -- increment를 사용하면 자동증가 시킬 수 있음
	ename varchar(50),
	
	primary key(empno)
);

insert into emp_auto(ename)
values('근욱');
select * from emp_auto;

insert into emp_auto(ename)
values('근욱2');
select * from emp_auto;
```

`AUTO_INCREMENT` 열을 지정하면 `INSERT` 때 그 열을 생략하고 새 번호를 받는다. 두 원본 모두 `EMPNO`를 `PRIMARY KEY`로 만든 예제다. 내 주석의 “Primary Key일 때만 가능”은 너무 좁다. MariaDB에서는 자동 증가 열에 필요한 **키 조건**이 있고, 반드시 기본 키여야 하는 것은 아니다. `SELECT MAX(empno)+1`은 수업에서 같이 적어 본 계산이지만, 동시에 여러 입력이 일어나면 같은 다음 번호를 계산할 수 있어 자동 번호와 같은 보장이 아니다.

<a id="section-3"></a>

## 3. 문자열 길이 실험

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 835–837행 · **원본 발췌**

```sql
-- mariadb 한글 한 글자는 3Byte
select length('한구');
select length('ab');
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 905–909행 · **원본 발췌**

```sql
-- length로 확인하게 되면 문자열의 Byte가 나옴(한글은 3Byte)
select length('한구');
select length('ab');

select char_length('한구');
```

내 코드는 `LENGTH('한구')`와 `CHAR_LENGTH('한구')`를 함께 실행했다. `LENGTH`는 바이트 수, `CHAR_LENGTH`는 문자 수다. 한글이 몇 바이트인지는 **문자 인코딩 설정에 따른다**. 내 주석의 “한 글자는 3Byte”는 이 수업 환경 관찰로 읽는다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 인덱스를 생성한 사실만으로 조회 속도가 늘었다고 결론낼 수 있는가?
2. `MAX(empno)+1`과 `AUTO_INCREMENT`는 여러 사용자가 동시에 넣을 때 왜 다른가?
3. `LENGTH`와 `CHAR_LENGTH`의 단위는 각각 무엇인가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

`EXPLAIN`으로 실제 선택된 접근 경로를 읽고 여러 데이터 크기에서 시간을 비교하는 방법은 다음 학습에 유용하다. 기존 Wiki의 복합·커버링 인덱스 상세 구현은 두 `Script.sql`의 실제 실행 범위를 넘으므로 [추가편 분류](추가편_기존자료_학습범위_분류.md)에 둔다.
