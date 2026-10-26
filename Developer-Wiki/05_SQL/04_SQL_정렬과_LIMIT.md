# 04. `ORDER BY`와 `LIMIT` — 어떤 순서로 몇 행 볼까

[SQL 목차](README.md) · [이전: `LIKE`와 `NULL`](03_SQL_LIKE와_NULL.md) · [다음: 집계 함수](05_SQL_집계함수.md)

`WHERE`가 행을 거른 뒤 `ORDER BY`가 결과 순서를 정하고 `LIMIT`이 보여 줄 행 수를 제한한다. 결과 몇 줄만 보고 싶을 때 **어떤 기준으로 앞줄을 정했는지**까지 함께 읽는다.

<!-- chapter-toc -->

- [1. 오름차순·내림차순과 여러 기준](#section-1)
- [2. `LIMIT` 한 개와 두 개](#section-2)
- [3. 조건과 정렬을 합친 문제](#section-3)
- [직접 확인할 질문](#section-4)
- [추가로 알면 좋은 것](#section-5)

<a id="section-1"></a>

## 1. 오름차순·내림차순과 여러 기준

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 144–170행 · **원본 발췌**

```sql
-- order by
select * from emp
order by sal;

-- asc : 오름차순, 생략 가능
select * from emp
order by sal asc; 

-- desc : 내림차순
select * from emp
order by sal desc;

select * from emp
order by deptno;

-- order by에 여러 컬럼이 적혀있는 경우
-- 왼쪽부터 적용되고 동일한 값이 있는 경우 다음 조건이 적용된다
select * from emp
order by deptno desc, job;

select * from emp
order by deptno desc, job asc, empno;

select * 
from emp
where sal > 1000
order by deptno desc, job asc, empno;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 178–203행 · **원본 발췌**

```sql
-- order by로 정렬을 할 수 있음 
-- ASC:오름차순 → 생략 가능
select * from emp
order by sal asc;

-- DESC:내림차순 → 생략 가능
select * from emp
order by sal desc;

select * from emp
order by deptno;

-- column별 asc, desc를 부여할 수 있음
-- 앞의 desc를 먼저 적용하고 겹치는것이 나오면 뒤 asc 적용
select * from emp
order by deptno desc, job;

-- order by에 여러 칼럼인 경우 왼쪽부터 적용되고 동일한 값이 있는 경우 다음 조건 적용
-- deptno를 정렬하고, job을 정렬하고, empno를 정렬
select * from emp
order by deptno desc, job asc, empno;

-- 각 절의 순서를 지켜야 함, where이 order by 뒤에 갈 순 없음
select * from emp
where sal > 1000
order by deptno desc, job asc, empno;
```

`ASC`는 오름차순이며 생략할 수 있다. `DESC`는 내림차순이다. `ORDER BY deptno DESC, job ASC, empno`는 **부서 번호 → 같은 부서 안의 직업 → 같은 직업 안의 사원 번호** 순서로 비교한다. 강사님은 동일한 조건에 `WHERE sal > 1000`을 더해, 조건절이 정렬절보다 앞에 오는 형태를 보여 준다.

<a id="section-2"></a>

## 2. `LIMIT` 한 개와 두 개

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 172–185행 · **원본 발췌**

```sql
-- limit : 보여줄 row의 수 제한
select * 
from emp
where sal > 1000
order by deptno desc, job asc, empno
limit 3;

-- limit offset, rows
-- offset만큼 건너뛰고 rows만큼 보여줌 
select * 
from emp
where sal > 1000
order by deptno desc, job asc, empno
limit 5, 3;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 205–216행 · **원본 발췌**

```sql
-- limit에 인자가 1개일 경우 보여 줄 검색 결과의 rows를 제한할 수 있음
select * from emp
where sal > 1000
order by deptno desc, job asc, empno
limit 3;

-- limit [offset][rows]
-- limit에 인자를 2개 줄 경우, offset만큼 건너 뛴 rows만큼 보여줌
select * from emp
where sal > 1000
order by deptno desc, job asc, empno
limit 5, 3;
```

`LIMIT 3`은 정렬된 결과의 앞 3행, `LIMIT 5, 3`은 **앞 5행을 건너뛰고 다음 3행**이다. 양쪽 코드에서 같은 형식으로 연습했다. 데이터가 변하면 몇 번째 행의 이름은 달라질 수 있다. 정렬 조건이 같을 때 순서를 안정적으로 읽으려면 내·강사님 코드처럼 마지막에 `empno`까지 확인하는 편이 좋다.

<a id="section-3"></a>

## 3. 조건과 정렬을 합친 문제

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 187–196행 · **원본 발췌**

```sql
-- 문제
-- 부서번호가 20또는 30인 사원 중에서
-- sal이 2000~3000 사이(포함)인 사원의
-- sal이 작은 순으로 출력하세요
-- sal이 같으면 이름을 내림차순으로 정렬
select * from emp
where
	(deptno = 20 or deptno = 30)
	and sal between 2000 and 3000
order by sal asc, ename desc;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 218–224행 · **원본 발췌**

```sql
-- 문제3 _ 부서 번호가 20 또는 30인 사원 중에서
-- 연봉이 2,000 ~ 3,000 사이(포함)인 사원의
-- 연봉이 작은 순으로 출력하시오
-- 연봉이 같으면 이름을 내림차순으로 정렬
select * from emp
where (deptno = 20 or deptno = 30) and (sal between 2000 and 3000)
order by sal, ename desc;
```

두 풀이 모두 부서 20·30, 급여 2,000~3,000 **양 끝 포함**, 급여 오름차순, 같은 급여면 이름 내림차순을 구현한다. 내 코드의 `ORDER BY sal`은 기본 오름차순이므로 강사님의 `sal ASC`와 같은 의도다. SQL 문장을 읽을 때는 **행 선택 → 정렬 → 몇 행만 보기** 순으로 스스로 풀어 보면 좋다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `LIMIT 5, 3`은 몇 번째 행부터 보여 주는가?
2. 급여가 같은 두 사원의 이름은 어떤 순서로 정렬되는가?
3. `WHERE`가 빠진 `LIMIT 3`과 현재 원본의 `LIMIT 3`은 대상 집합이 같은가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

대량 데이터의 페이지 이동 성능과 키셋 페이지네이션은 수업 스크립트의 본문 범위를 넘어간다. 여기서는 실제 사용한 **정렬 우선순위와 `LIMIT`의 건너뛰기**를 먼저 익힌다.
