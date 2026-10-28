# SQL 실습. 강사님 문제와 내 실제 풀이 비교

[SQL 목차](README.md) · [이전: 재귀 CTE](18_SQL_Recursive_CTE.md)

강사님 `Script.sql` 뒤쪽에는 **7개 문제와 풀이**, 내 `Script.sql`에는 그에 대응하는 직접 작성한 풀이와 시험문제 풀이가 있다. 이 장은 기존 Wiki가 새로 만든 종합 프로젝트가 아니라 **실제 원본의 문제**를 메인에 놓는다. 모든 결과는 학습용 `EMP`·`DEPT`·`SALGRADE`의 현재 행에 따라 달라진다.

## 먼저: 문제 문장과 조건을 나누어 읽기

첫 문제인 “1981년 입사자 중 최저 급여자”는 **① 1981년 입사한 행을 고르고 → ② 그 안에서 최저 급여를 구하고 → ③ 해당 연도와 그 급여를 모두 만족하는 사원을 찾는** 순서다. 제공된 초기 자료에서는 1981년 입사한 JAMES의 급여가 950이어서 이 값이 최솟값이다. 이것은 **초기 자료를 기준으로 한 예상 결과**이며, 표를 바꿨다면 다시 계산해야 한다.

| 확인할 부분 | 빠뜨리면 생기는 일 |
| --- | --- |
| 안쪽 최저 급여 계산의 입사 연도 | 다른 연도의 급여가 섞임 |
| 바깥 사원 조회의 입사 연도 | 다른 연도에서 우연히 같은 급여를 받는 사원도 나올 수 있음 |

아래 원본 비교에서 강사님은 두 곳에 연도를 적용했고, 나는 안쪽에만 적용했다. 다른 문제도 **요구 조건 → 실제 SQL → 결과 범위**를 같은 방식으로 비교한다.

<!-- chapter-toc -->

- [1. 1981년 입사자 중 최저 급여자](실습_SQL_원본문제_비교.md#section-1)
- [2. 부서별 최고·최저 급여 차이](실습_SQL_원본문제_비교.md#section-2)
- [3. BLAKE보다 급여가 높고 JONES와 직업이 같은 사람](실습_SQL_원본문제_비교.md#section-3)
- [4. 모든 급여 등급의 사원 수](실습_SQL_원본문제_비교.md#section-4)
- [5. 등급·부서 조건을 함께 거는 문제](실습_SQL_원본문제_비교.md#section-5)
- [6. 내 시험문제 풀이와 강사님 마지막 문제](실습_SQL_원본문제_비교.md#section-6)
- [직접 확인할 질문](실습_SQL_원본문제_비교.md#section-7)
- [추가로 알면 좋은 것](실습_SQL_원본문제_비교.md#section-8)

<a id="section-1"></a>

## 1. 1981년 입사자 중 최저 급여자

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 935–944행 · **원본 발췌**

```sql
select min(sal) from emp
where hiredate >= '1981-01-01' and hiredate <= '1981-12-31';

select * from emp
where sal = 950;

select * from emp
where sal = (select min(sal) from emp
			 where hiredate >= '1981-01-01' and hiredate <= '1981-12-31')
and hiredate like '1981%';
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 974–987행 · **원본 발췌**

```sql
-- 문제1 최종풀이
select ename, sal, hiredate 
from emp
where sal = (	select min(sal)
				from emp
				where substr(HIREDATE, 1, 4) = '1981');

-- 문제1 개선풀이
select ename, sal, hiredate 
from emp
where sal = (	select min(sal)
				from emp
				where hiredate 
					between date '1981-01-01' and date '1981-12-31');
```

두 풀이 모두 먼저 **1981년 입사자의 최저 급여 값**을 구한다. 강사님은 바깥 조회에도 `hiredate LIKE '1981%'`를 넣어 입사 연도를 제한했다. 내 “최종풀이”와 “개선풀이”는 바깥 `WHERE sal = (...)`만 있어, **다른 연도에 같은 급여를 받는 사원**이 있다면 함께 나온다. 내 날짜 범위식은 안쪽 집계 대상을 읽기 좋지만 바깥의 입사 연도 조건이 빠졌다는 점은 별도로 고쳐야 한다. 강사님 코드가 이 조건을 더 정확히 보존한다.

<a id="section-2"></a>

## 2. 부서별 최고·최저 급여 차이

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 948–963행 · **원본 발췌**

```sql
/*
각 부서 별
급여가 가장 높은 사원 가장 낮은 사원의 차이를 조회하시오
출력 : 부서명, 차이 금액
*/

select deptno, max(sal), min(sal) from emp
group by deptno;
select * from emp
where deptno = 10
order by sal;

select dept.dname, max(emp.sal) - min(emp.sal) 
from emp, dept
where emp.deptno = dept.deptno
group by emp.deptno, dept.dname;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 989–1003행 · **원본 발췌**

```sql
-- 문제2 _ 각 부서별 급여가 가장 높은 사원과, 가장 낮은 사원의 차이를 조회하시오.
-- 부서명, 차이 금액 출력
select * from emp e;
select * from dept;

-- 문제2 최종풀이
select d.dname, max(e.sal) - min(e.sal) as salCalc
from emp e join dept d using(deptno)
group by d.deptno, d.dname;

-- 문제2 각 부서별? 빈 부서도 포함해보기
select d.dname, max(e.sal) - min(e.sal) as salCalc
from dept d 
	left outer join emp e using(deptno)
group by d.deptno, d.dname;
```

두 기본 풀이 모두 부서별로 묶어 `MAX(sal) - MIN(sal)`을 구한다. 내 추가 풀이에서는 `DEPT`를 왼쪽에 둔 `LEFT JOIN`으로 **사원이 없는 부서**도 결과에 남긴다. 이때 급여가 전혀 없으면 차이 계산은 `NULL`이며 0이라고 단정하지 않는다. 강사님 기본 풀이와 내 첫 풀이의 `EMP` 출발은 사원 없는 부서를 표시하지 않는다.

<a id="section-3"></a>

## 3. BLAKE보다 급여가 높고 JONES와 직업이 같은 사람

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 965–980행 · **원본 발췌**

```sql
/*
BLAKE보다 높은 연봉을 받는 사람들 출력
 */
select sal from emp
where ename = 'BLAKE';

select * from emp
where sal > (select sal from emp
				where ename = 'BLAKE');

/*
 * JONES랑 같은 job을 가진 사람들
 */
select * from emp
where job = (select job from emp
				where ename = 'JONES');
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 1023–1043행 · **원본 발췌**

```sql
-- 문제3 _ BLAKE보다 높은 연봉을 받는 사람들 출력
select * from emp;

select sal from emp
where ename = 'BLAKE';

-- 문제3 최종풀이
select ename, sal from emp
where sal > (	select sal from emp
				where ename = 'BLAKE');

-- 문제4 _ JONES와 같은 JOB을 가진 사람들을 출력
select * from emp;

select job from emp
where ename = 'JONES';

-- 문제4 최종풀이
select ename, job from emp
where job = (	select job from emp
				where ename = 'JONES');
```

각 문제에서 안쪽 조회로 BLAKE의 `SAL`, JONES의 `JOB`을 먼저 얻고 바깥 조건에서 비교한다. 두 원본의 핵심 조건은 같다. 나는 결과 열을 `ENAME, SAL` 또는 `ENAME, JOB`으로 좁혔고, 강사님은 `SELECT *`로 전체 열을 봤다. 답을 설명할 때는 **문제가 요구한 열만 보이는 내 코드**가 결과를 읽기 쉽다.

<a id="section-4"></a>

## 4. 모든 급여 등급의 사원 수

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 983–999행 · **원본 발췌**

```sql
/*
 * 급여 등급 별 사원 수를 등급 오름차순으로 정렬
단, 모든 등급을 표시한다
 */

select s.grade, count(*)
from salgrade s
	left outer join emp e 
		on (e.sal <= s.hisal and e.sal >= s.losal)
group by s.grade
order by s.grade;

select count(e.ename) 사원수,grade 등급
from emp e,salgrade s
where sal>=losal and
sal<=hisal
group by grade desc;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 1045–1055행 · **원본 발췌**

```sql
-- 문제5 _ 급여 등급 별 사원 수를 등급 오름차순으로 정렬
-- 단, 모든 등급을 표시한다 (몇 등급에 몇 명)
select * from emp;
select * from salgrade;

-- 문제5 최종풀이
select s.grade, count(e.ENAME) as gradeCount
from salgrade s left outer join emp e
on (e.sal between s.losal and s.hisal)
group by s.grade
order by s.grade asc;
```

문제의 “**모든 등급**” 때문에 `SALGRADE`가 왼쪽이어야 한다. 두 최종 풀이 모두 그렇게 연결한다. 그러나 강사님의 첫 풀이 `COUNT(*)`는 사원이 없는 등급에도 `LEFT JOIN`의 **빈 사원 열을 가진 한 행**을 세어 1로 표시할 수 있다. 내 `COUNT(e.ENAME)`은 실제로 연결된 사원 이름만 세므로 **0명인 등급을 0명**으로 표시한다. 이 문제에서는 내 코드의 집계 대상이 더 정확하다. 강사님 뒤의 `EMP` 출발 풀이(995–999행)는 빈 등급을 남기지 않아 요구사항과 다르다.

<a id="section-5"></a>

## 5. 등급·부서 조건을 함께 거는 문제

### 강사님 코드 — 등급 3 이상

출처: `teacher/workspace_sql/Script.sql` 1001–1013행 · **원본 발췌**

```sql
/*
이름, 급여, 급여 등급, 부서 이름 조회
단, 급여 등급 3 이상만 조회.
급여 등급 내림차순, 등급이 같은 경우 급여 내림차순, 급여가 같은 경우 이름 내림차순
*/
select e.ename, e.sal, s.grade, d.dname
from salgrade s
	left outer join emp e 
		on (e.sal <= s.hisal and e.sal >= s.losal)
	left outer join dept d
		on(e.deptno = d.deptno)
where s.grade >= 3
order by s.grade desc, sal desc, ename desc;
```

### 내 코드 — 등급 3 이상

출처: `me/workspace_sql/Script.sql` 1071–1082행 · **원본 발췌**

```sql
-- 문제6 개선
select e.ename, e.sal, s.grade, d.dname
from emp e 
	join dept d
		on (e.deptno = d.deptno)
	join salgrade s
		on (e.sal between s.losal and s.hisal)
where s.grade >= 3
order by 
	s.grade desc, 
	e.sal desc, 
	e.ename desc; 
```

나는 `EMP → DEPT → SALGRADE`를 각각 `JOIN ... ON`으로 분리해 연결했다. 강사님은 `SALGRADE`를 왼쪽에 놓고 `LEFT JOIN`을 썼다. `WHERE s.grade >= 3`은 **등급 표의 값**을 검사하므로, 해당 등급에 사원이 없어도 사원 이름이 `NULL`인 행이 남을 수 있다. 문제는 실제 사원 이름을 조회하므로 내 `JOIN` 풀이가 대상 행을 더 정확히 고르고 연결 조건도 읽기 쉽다.

### 강사님 코드 — SALES·2 또는 3등급

출처: `teacher/workspace_sql/Script.sql` 1015–1025행 · **원본 발췌**

```sql
/*
부서명이 SALES인 사원 중
급여 등급이 2 또는 3인 사원을 급여 내림차순으로 정렬
 */
select *
from emp e
left outer join salgrade s on (e.sal <= s.hisal and e.sal >= s.losal)
left outer join dept d on (e.deptno = d.deptno)
where d.dname = 'SALES'
and s.grade in (2, 3)
order by sal desc;
```

### 내 코드 — SALES·2 또는 3등급

출처: `me/workspace_sql/Script.sql` 1084–1103행 · **원본 발췌**

```sql
-- 문제7 _ 부서명이 SALES인 사원 중, 급여 등급이 2또는 3인 사원을 급여 내림차순으로 정렬
select * from emp;
select * from dept;

-- 문제7 최종풀이
select e.ename, e.sal, s.grade, d.dname
from emp e join dept d join salgrade s on (e.deptno = d.deptno) and (e.sal between s.losal and s.hisal)
where d.dname = 'SALES' and (s.grade = 2 or s.grade = 3)
order by e.sal desc;

-- 문제7 개선
select e.ename, e.sal, s.grade, d.dname
from emp e 
	join dept d 
		on (e.deptno = d.deptno)
	join salgrade s
		on (e.sal between s.losal and s.hisal)
where d.dname = 'SALES' 
	and (s.grade = 2 or s.grade = 3)
order by e.sal desc;
```

두 코드는 모두 SALES 부서에서 급여 등급 2·3인 사원을 급여 내림차순으로 출력한다. 내 풀이에는 한 줄 `JOIN` 버전과 각 관계를 나눠 쓴 “개선” 버전이 **둘 다 실제 원본에 있다**. 초보자에게는 `EMP.DEPTNO = DEPT.DEPTNO`와 `EMP.SAL BETWEEN LOSAL AND HISAL`을 각각 보이는 개선 버전이 더 읽기 좋다.

<a id="section-6"></a>

## 6. 내 시험문제 풀이와 강사님 마지막 문제

### 강사님 코드 — 자신의 부서 평균보다 높은 사원

출처: `teacher/workspace_sql/Script.sql` 1079–1107행 · **원본 발췌**

```sql

select * 
from emp e1
where sal > (select avg(sal)
				from emp e2 
				where e2.deptno = e1.deptno
				group by deptno);


select deptno, avg(sal)
from emp
group by deptno;


select *
from emp e, (select deptno, avg(sal) avg_sal
				from emp
				group by deptno) a
where e.deptno = a.deptno
and e.sal > a.avg_sal;


select *
from emp e
	left outer join (select deptno, avg(sal) avg_sal
				from emp
				group by deptno) a
	on e.deptno = a.deptno
where  e.sal > a.avg_sal;
```

### 내 코드 — 시험문제에서 작성한 상관 서브쿼리

출처: `me/workspace_sql/Script.sql` 1134–1146행 · **원본 발췌**

```sql
select e.ename, d.dname, e.sal, (
	select round(avg(e2.sal),0)
	from emp e2
	where e2.deptno = e.deptno
) as salAvg
from dept d
join emp e on e.deptno = d.deptno
where e.sal > (
	select avg(e2.sal)
	from emp e2
	where e2.deptno = e.deptno
)
order by d.dname, e.sal desc;
```

내 시험문제 풀이에서는 `e2.deptno = e.deptno`로 **현재 사원과 같은 부서**의 평균을 구한다. 강사님 원본도 같은 문제를 상관 서브쿼리와 `FROM`의 부서별 평균 결과 연결로 각각 풀었다. 내 바깥 조회는 부서 이름과 반올림한 평균도 표시한다. 평균을 표시할 때만 `ROUND(...,0)`을 적용하고, 비교 조건에는 반올림하지 않은 `AVG`를 사용한다.

<a id="section-7"></a>

## 직접 확인할 질문

1. 내 1981년 최저 급여 풀이에서 바깥 연도 조건이 없으면 어떤 사원이 더 나올 수 있는가?
2. 사원이 없는 급여 등급을 `COUNT(*)`와 `COUNT(e.ENAME)`은 각각 몇 명으로 세는가?
3. 내 시험문제의 안쪽 `e2.deptno = e.deptno`가 빠지면 어떤 평균과 비교하게 되는가?

<a id="section-8"></a>

## 추가로 알면 좋은 것

기존 Wiki의 8단계 종합 프로젝트, 보고서 전용 새 테이블, 고급 성능 측정은 두 `Script.sql`의 이 문제 원본 그대로는 아니다. 그런 연습은 [추가편 분류](추가편_기존자료_학습범위_분류.md)에 둔다. 이 장의 본문은 **직접 작성한 문제와 결과 해석**이다.
