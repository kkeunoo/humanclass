# 01. SQL과 `SELECT` — 어느 표의 무엇을 볼까

[SQL 목차](README.md) · [다음: `WHERE`](02_SQL_WHERE와_조건연산자.md)

이 장은 강사님과 내 `Script.sql`의 첫 조회 구간을 따라간다. 실습 대상은 제공된 `EMP`(사원), `DEPT`(부서), `SALGRADE`(급여 등급) 표다. SQL 문장을 **적은 순서**와 데이터베이스가 조회를 **해석하는 흐름**은 다를 수 있다. 우선 `FROM`에서 대상을 고르고 `SELECT`에서 결과에 보여 줄 열을 정한다.

<!-- chapter-toc -->

- [1. 표 전체와 필요한 열](01_SQL_기초와_SELECT.md#section-1)
- [2. 중복값 제거와 결과 열 이름](01_SQL_기초와_SELECT.md#section-2)
- [직접 확인할 질문](01_SQL_기초와_SELECT.md#section-3)
- [추가로 알면 좋은 것](01_SQL_기초와_SELECT.md#section-4)

<a id="section-1"></a>

## 1. 표 전체와 필요한 열

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 6–15행 · **원본 발췌**

```sql
select * from emp;
select * from dept;
select * from salgrade;

select 100*12;

select empno from emp;

select empno, ename 
  from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 26–33행 · **원본 발췌**

```sql
-- 전체 사원
select * from emp;
-- 부서 별
select * from dept;
-- 연봉 등급표
select * from salgrade; 

select empno from emp;
```

`SELECT * FROM emp`는 `EMP`의 모든 열을 요청한다. `SELECT empno FROM emp`는 사원 번호만, `SELECT empno, ename FROM emp`는 사원 번호와 이름만 보여 준다. 강사님은 `select 100*12`도 실행해 표 없이 식의 계산 결과만 볼 수 있음을 보였다. **`*`와 특정 열의 차이**가 첫 학습 목표다. 열 이름과 행의 실제 값은 초기화 자료나 현재 데이터에 따라 확인한다.

<a id="section-2"></a>

## 2. 중복값 제거와 결과 열 이름

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 23–34행 · **원본 발췌**

```sql
select job from emp;
-- 중복 결과를 하나만 보여준다
select distinct job from emp;


select job as 직업 from emp;
select job as '직업 이름' from emp;
select job 직업 from emp;


select sal, sal*12 from emp;
select sal, comm, sal + comm from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 47–65행 · **원본 발췌**

```sql
select job from emp;
-- distinct로 중복 결과를 하나만 보이게 할 수 있다
select distinct job from emp; 

-- as로 가져오는 열 리스트의 이름을 변경할 수 있음
select job as 직업 from emp;
-- as로 띄어쓰기가 포함되는 경우 ''는 필수로 사용해야 함
select job as '직업 이름' from emp;
-- as도 생략이 가능하다
select job '직업 이름' from emp;

-- select에서 사칙연산을 이용하면 해당 값도 볼 수 있음
select sal, sal*12 from emp;

-- select에 바로 대입해도 값은 나오게 할 수 있음
select 100*12;

-- 기존 NULL에는 더하거나 빼도 NULL로 유지됨
select sal, comm , sal + comm from emp;
```

`job`만 출력하면 같은 직업 이름이 여러 행에 나온다. `DISTINCT job`은 **조회 결과의 중복**을 제거하며 원본 표를 삭제하거나 변경하지 않는다. `AS 직업`은 결과 열의 표시 이름을 바꾼다. `sal*12`는 급여에 12를 곱한 계산 열이다. `sal + comm`은 `comm`이 `NULL`이면 결과도 `NULL`이 될 수 있다. `NULL` 처리 방법은 [08 숫자·날짜·NULL 함수](08_SQL_숫자_날짜_NULL함수.md)에서 다시 본다.

### 강사님 코드가 더 명확한 부분

강사님은 `select job`과 `select distinct job`을 **연달아** 놓아 중복 제거 전후를 비교하기 쉽다. 내 코드도 같은 비교를 하지만, 뒤에 별칭과 계산을 한꺼번에 붙였다. 복습할 때는 한 문장씩 실행해 어떤 열이 달라졌는지 먼저 본다.

<a id="section-3"></a>

## 직접 확인할 질문

1. `SELECT *`와 `SELECT empno, ename`의 결과 열은 어떻게 다른가?
2. `DISTINCT job`을 실행하면 원본 `EMP` 행이 없어지는가?
3. `comm`이 `NULL`인 사원의 `sal + comm` 결과는 무엇인가?

<a id="section-4"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/01_SQL_기초와_SELECT_연습문제.md)

## 추가로 알면 좋은 것

실무에서는 필요한 열만 명시하면 조회 결과 구조를 읽고 유지하기 편하다. 다만 이 장의 본문은 **수업에서 작성한 조회·중복 제거·별칭·계산**이다. 서버의 상세 실행 계획이나 모든 SQL 방언의 별칭 문법은 이 단계의 필수 학습이 아니다.
