# 11. 서브쿼리 — 다른 조회 결과를 조건으로 쓰기

[SQL 목차](README.md) · [이전: `UNION`](10_SQL_UNION과_UNION_ALL.md) · [다음: `JOIN`](12_SQL_JOIN.md)

한 문장 안에서 먼저 다른 값을 찾아야 할 때 괄호 안의 `SELECT`를 쓴다. 두 원본의 WARD 급여, 전체 평균, 부서별 최고 급여, 부서별 평균 실습을 차례로 본다.

<!-- chapter-toc -->

- [1. 한 값과 비교하기](11_SQL_서브쿼리.md#section-1)
- [2. 여러 값과 `IN`](11_SQL_서브쿼리.md#section-2)
- [3. `FROM` 안의 조회 결과](11_SQL_서브쿼리.md#section-3)
- [직접 확인할 질문](11_SQL_서브쿼리.md#section-4)
- [추가로 알면 좋은 것](11_SQL_서브쿼리.md#section-5)

<a id="section-1"></a>

## 1. 한 값과 비교하기

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 419–430행 · **원본 발췌**

```sql
-- 'WARD'의 연봉만 출력
select sal 
from emp
where ename = 'WARD'; 

select * from emp
where sal > (select sal 
			 from emp
			 where ename = 'WARD');

select * from emp
where sal > (select avg(sal) from emp);
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 450–462행 · **원본 발췌**

```sql
select sal 
from emp
where ename = 'WARD'

-- 서브쿼리로 중첩해서 사용할 수 있음
select * from emp
where sal > (select sal 
			 from emp
			 where ename = 'WARD');

-- 서브쿼리에서 column이 두개이거나, 여러 줄이면 안 됨
select * from emp
where sal > (select avg(sal) from emp);
```

안쪽 `SELECT sal FROM emp WHERE ename = 'WARD'`가 WARD의 급여를 구하고, 바깥 `WHERE sal > (...)`가 그보다 급여가 높은 사원을 찾는다. `AVG(sal)`도 전체 평균 **한 값**을 돌려 주므로 `>` 오른쪽에 넣을 수 있다. 내 주석 “서브쿼리는 여러 줄이면 안 됨”은 이 **한 값 비교 연산자**의 경우에만 해당한다. 다음 `IN`에서는 여러 행을 쓸 수 있다.

<a id="section-2"></a>

## 2. 여러 값과 `IN`

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 432–448행 · **원본 발췌**

```sql
-- 부서 별 최고 연봉자
-- 1. 부서 별 최고 연봉
select max(sal)
from emp
group by deptno;

select ename, sal
from emp
-- where sal = 3000 or sal = 2850 or sal = 5000;
where sal in (3000, 2850, 5000);

select ename, sal, deptno
from emp
-- where sal = 3000 or sal = 2850 or sal = 5000;
where sal in (	select max(sal)
				from emp
				group by deptno);
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 464–480행 · **원본 발췌**

```sql
-- 부서 별 최고 연봉자
-- 1. 부서 별 최고 연봉을 뽑아라
select max(sal)
from emp
group by deptno;

-- 아래처럼 서브쿼리로 넣어 한 번에 처리할 수 있음
select ename, sal
from emp
-- where sal = 3000 or sal = 2850 or sal = 5000;
where sal in (3000, 2850, 5000);

select ename, sal
from emp
where sal in (  select max(sal)
				from emp
			  	group by deptno);
```

안쪽 `GROUP BY deptno`는 **부서별 최대 급여 값들**을 만든다. 바깥 `sal IN (...)`은 그 값 중 하나와 같은 급여의 사원을 고른다. 이 코드는 “자기 부서에서 최고 급여인 사원”과 **완전히 같은 조건은 아니다**. 다른 부서의 최고 급여와 우연히 같은 급여를 받는 사원도 들어올 수 있기 때문이다. 실제 작성한 풀이의 한계를 본문에서 분명히 한다.

<a id="section-3"></a>

## 3. `FROM` 안의 조회 결과

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 467–488행 · **원본 발췌**

```sql
-- having 없이 서브쿼리로 해결해보자
-- 1. 부서 별 평균 연봉 출력
select avg(sal)
from emp
group by deptno;
-- 2. 부서 별 평균 연봉이 2000 이상인 부서만 출력
-- having 사용
select avg(sal) avg_sal
from emp
-- where avg_sal >= 2000 -- 별칭은 select 이후에 사용 가능
-- where avg(sal) >= 2000 -- 집계 함수 사용 불가
group by deptno
having avg(sal) >= 2000;

-- 서브쿼리 사용
select *
from (
	select avg(sal) avg_sal
	from emp
	group by deptno
) a
where avg_sal >= 2000;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 502–524행 · **원본 발췌**

```sql
-- having 없이 서브쿼리로 해결
-- 1. 부서 별 평균 연보 출력
select avg(sal)
from emp
group by deptno;
-- 2. 부서 별 평균 연봉이 2000이상인 부서만 출력
select avg(sal) avg_sal
from emp
-- where avg_sal >= 2000 → 사용 불가하며, select 이후(group by)에 사용 가능
-- where avg(sal) >= 2000 → 집계함수는 사용 불가능
group by deptno
having avg(sal) >= 2000;

-- 서브쿼리 사용
-- from 에 서브쿼리를 넣었을 때 별칭 필요
-- 위에 having 사용한 것을 from에 넣어 사용할 수 있음
select *
from (
	select avg(sal) avg_sal
	from emp
	group by deptno
) a
where avg_sal >= 2000;
```

먼저 부서별 평균을 만든 결과를 임시 결과처럼 `FROM (...) a`에 놓고, 바깥에서 `avg_sal >= 2000`을 검사한다. 같은 목표를 `HAVING AVG(sal) >= 2000`으로 더 짧게 쓸 수 있다. **강사님 코드가 간결한 부분**은 바로 `HAVING` 버전이다. 하지만 `FROM` 서브쿼리도 실제 수업에서 배운 방식이므로 본문에 남긴다. 두 코드 모두 평균만 출력해 부서 번호가 보이지 않는다. “어느 부서인가”까지 보려면 그룹 기준도 결과 열로 함께 출력해야 한다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `>` 오른쪽의 WARD 서브쿼리는 왜 한 값이어야 하는가?
2. `IN (SELECT MAX(sal) ... GROUP BY deptno)`가 다른 부서의 사원도 포함할 수 있는 이유는?
3. 부서 번호 없이 평균만 표시하면 무엇을 확인하기 어려운가?

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/11_SQL_서브쿼리_연습문제.md)

## 추가로 알면 좋은 것

상관 서브쿼리나 동점자의 정확한 부서별 최고 급여 조회는 다음 학습에 유용하다. 다만 본문은 원본의 **단일 값·여러 값·`FROM` 서브쿼리**를 읽는 데 집중한다.
