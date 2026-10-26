# 12. `JOIN` — 두 표의 관계를 연결하기

[SQL 목차](README.md) · [이전: 서브쿼리](11_SQL_서브쿼리.md) · [다음: 외부·자기 조인](13_SQL_Outer_JOIN과_Self_JOIN.md)

사원 `EMP`의 `DEPTNO`와 부서 `DEPT`의 `DEPTNO`를 연결하면 사원 이름 옆에 부서 이름을 보여 줄 수 있다. 급여 등급은 `SALGRADE`의 범위와 급여를 비교해 연결한다.

<!-- chapter-toc -->

- [1. 연결 조건 없는 두 표와 연결 조건 있는 두 표](#section-1)
- [2. 같은 열 이름을 구분하기](#section-2)
- [3. 급여와 등급의 범위 연결](#section-3)
- [4. `JOIN ... ON`과 `USING`](#section-4)
- [직접 확인할 질문](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 연결 조건 없는 두 표와 연결 조건 있는 두 표

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 491–502행 · **원본 발췌**

```sql
select * from dept;

select *
from emp, dept;

select *
from emp, dept
where emp.deptno = dept.deptno;

select *
from emp e, dept d
where e.deptno = d.deptno;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 527–539행 · **원본 발췌**

```sql
-- 이렇게 2개의 테이블을 이용하게 되면 곱연산(데카르트)되어 출력됨
select * 
from emp, dept;

-- 두 개의 테이블을 이용할 땐 아래와 같이 조건식에서 맞춰야 함
select * 
from emp, dept
where emp.deptno = dept.deptno;

-- 아래처럼 별칭을 주어서 사용할 수 있음
select * 
from emp e, dept d
where e.deptno = d.deptno;
```

`FROM emp, dept`만 쓰면 사원 각 행과 부서 각 행의 **모든 조합**이 나온다. `WHERE e.deptno = d.deptno`를 넣으면 같은 부서 번호인 조합만 남는다. 강사님과 나는 테이블 별칭 `e`, `d`도 사용했다. 조인 조건을 빠뜨리면 같은 사원·부서가 무관하게 묶여 행 수가 크게 늘어난다.

<a id="section-2"></a>

## 2. 같은 열 이름을 구분하기

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 504–512행 · **원본 발췌**

```sql
/*
select ename, dname, deptno
from emp e, dept d
where e.deptno = d.deptno;
*/

select 리얼허거덩거거덩거허.ename, d.dname, 리얼허거덩거거덩거허.deptno
from emp 리얼허거덩거거덩거허, dept d
where 리얼허거덩거거덩거허.deptno = d.deptno;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 541–551행 · **원본 발췌**

```sql
-- Column 'deptno' in SELECT is ambiguous
-- 두 테이블에 이름이 같기 때문에 뭘 지칭하는건지 모르겠다는 Error 발생
/*
select ename, dname, deptno 
from emp e, dept d
where e.deptno = d.deptno;
*/

select e.ename, d.dname, e.deptno 
from emp e, dept d
where e.deptno = d.deptno;
```

두 표 모두 `deptno` 열이 있으므로 단독 `SELECT deptno`는 어느 표인지 모호하다. `e.deptno` 또는 `d.deptno`처럼 쓴다. 강사님은 일부러 매우 긴 별칭을 쓴 실행 예제를 남겼고, 나는 `e`·`d`로 짧게 구분했다. **초보자 복습에는 내 짧은 별칭이 읽기 쉽다.** 핵심은 별칭 길이가 아니라 원본 표를 분명히 지정하는 것이다.

<a id="section-3"></a>

## 3. 급여와 등급의 범위 연결

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 516–530행 · **원본 발췌**

```sql
-- 스미스의 월급 등급은? 정답: 1
-- 이름, 월급, 등급, losal, hisal

select * from salgrade
where (800) >= losal and 800 <= hisal;

select sal from emp
where ename = 'SMITH';

select 
	ename, sal, grade, losal, hisal
from 
	emp e, salgrade s
where sal >= losal and sal <= hisal
and ename = 'SMITH';
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 555–567행 · **원본 발췌**

```sql
-- SMITH의 연봉 등급은? 정답 : 1
-- 이름, 월급, 등급, losal, hisal
select * from salgrade
where 800 >= losal and 800 <= hisal;

select sal from emp
where ename='SMITH'

select ename, sal, grade, hisal, losal
from emp e, salgrade s
-- where sal >= losal and sal <= hisal
where sal between losal and hisal
and ename='SMITH';
```

급여 등급은 부서 번호처럼 **같은 값끼리** 맞추지 않는다. `sal BETWEEN losal AND hisal`의 범위 안에 급여가 들어가는 등급을 찾는다. 강사님은 `sal >= losal AND sal <= hisal`로 풀어 쓰고, 나는 `BETWEEN`으로 줄였다. 양 끝을 포함한다는 [02장](02_SQL_WHERE와_조건연산자.md)의 규칙이 여기에도 적용된다.

<a id="section-4"></a>

## 4. `JOIN ... ON`과 `USING`

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 570–574행 · **원본 발췌**

```sql
select e.deptno
from emp e join dept d on (e.deptno = d.deptno);

select deptno
from emp e join dept d using(deptno);
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 600–606행 · **원본 발췌**

```sql
-- join을 쓸 때는 where가 아닌 on에 조건식 기재
select e.deptno
from emp e join dept d on(e.deptno = d.deptno);

-- using으로 같은 column을 합칠 수 있음
select deptno
from emp e join dept d using(deptno);
```

`JOIN ... ON e.deptno = d.deptno`는 연결 조건을 `ON`에 적는다. 두 표의 같은 이름 열을 연결할 때 `USING(deptno)`로도 쓸 수 있다. 내 주석 “JOIN을 쓸 때는 WHERE가 아닌 ON”은 **연결 조건을 분리해 읽기 좋다**는 취지로 이해한다. 위의 `FROM emp, dept WHERE ...` 방식도 수업 원본에 있는 유효한 조인이다.

<a id="section-5"></a>

## 직접 확인할 질문

1. `FROM emp, dept`에 관계 조건이 없으면 왜 행이 늘어나는가?
2. `deptno`를 `e.deptno`로 쓰는 이유는?
3. 급여 등급 연결은 `=`와 범위 조건 중 무엇을 쓰는가?

<a id="section-6"></a>

## 추가로 알면 좋은 것

조인 순서의 성능·옵티마이저 선택은 이 원본의 첫 학습 목표가 아니다. 먼저 **연결 열과 조인 결과의 행 보존 여부**를 확인한다.
