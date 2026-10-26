# 13. 외부 조인과 자기 조인 — 없는 관계도 보이게 하기

[SQL 목차](README.md) · [이전: `JOIN`](12_SQL_JOIN.md) · [다음: 테이블 만들기](14_SQL_DDL과_제약조건.md)

같은 `EMP` 표를 사원과 관리자 역할로 두 번 사용하면 **자기 조인**, 부서에 사원이 없어도 부서를 남기면 **외부 조인**이다. 두 원본의 관리자 찾기와 모든 부서 보기 문제를 비교한다.

<!-- chapter-toc -->

- [1. 같은 표를 두 역할로 사용](#section-1)
- [2. `LEFT OUTER JOIN`이 남기는 쪽](#section-2)
- [3. 사원이 없는 부서도 출력하는 문제](#section-3)
- [직접 확인할 질문](#section-4)
- [추가로 알면 좋은 것](#section-5)

<a id="section-1"></a>

## 1. 같은 표를 두 역할로 사용

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 532–556행 · **원본 발췌**

```sql
select * from emp;

select 
	mgr 
from emp
where ename = 'SMITH';

select 
	ename
from emp
where empno = 7902;

select 
	ename
from emp
where empno = (select 
					mgr 
				from emp
				where ename = 'SMITH');

-- mgr이 null인 것은 빠졌다
select e1.ename, e2.ename
from emp e1, emp e2
where e1.mgr = e2.empno
and e1.ename = 'SMITH';
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 569–585행 · **원본 발췌**

```sql
select * from emp;

select mgr 
from emp
where ename = 'SMITH';

select ename
from emp
where empno = (	select mgr 
				from emp
				where ename = 'SMITH');		
-- 위 코드를 같은 테이블을 동시 조인하여 결과값도 알 수 있다
-- mgr이 null인 것은 빠져서 결과값은 총 14개 중 13개만 나옴
select e2.ename, e1.ename
from emp e1, emp e2
where e1.mgr = e2.empno
and e1.ename = 'SMITH';
```

사원의 `mgr`에는 관리자의 `empno`가 들어 있다. `EMP e1`을 사원, `EMP e2`를 관리자로 놓고 `e1.mgr = e2.empno`로 연결한다. 강사님은 SMITH의 관리자만, 나는 관리자·사원 이름 두 값을 같이 보여 준다. 관리자 번호가 `NULL`인 사원은 이 **내부 조인** 결과에서 빠진다. 내 주석의 “14개 중 13개”는 그 실습 데이터에 대한 관찰이지 모든 데이터의 고정 규칙이 아니다.

<a id="section-2"></a>

## 2. `LEFT OUTER JOIN`이 남기는 쪽

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 576–586행 · **원본 발췌**

```sql
select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	join emp e2 on e1.mgr = e2.empno;

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	left outer join emp e2 on e1.mgr = e2.empno;

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	right outer join emp e2 on e1.mgr = e2.empno;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 615–626행 · **원본 발췌**

```sql
select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	join emp e2 on e1.mgr = e2.empno;

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	left outer join emp e2 on e1.mgr = e2.empno;
	-- left outer는 왼쪽에 있는 column 대상이 한 번은 무조건 나오게 해주는 것

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	right outer join emp e2 on e1.mgr = e2.empno;
```

강사님·내 코드 모두 내부 조인, 왼쪽 외부 조인, 오른쪽 외부 조인을 비교한다. `EMP e1 LEFT JOIN EMP e2`는 **왼쪽 `e1`의 모든 사원**을 남긴다. 연결할 관리자가 없으면 오른쪽 관리자 열은 `NULL`이다. `RIGHT JOIN`은 반대로 오른쪽 `e2`의 행을 남긴다. 어느 표를 왼쪽에 두었는지 먼저 읽어야 결과를 예상할 수 있다.

<a id="section-3"></a>

## 3. 사원이 없는 부서도 출력하는 문제

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 590–598행 · **원본 발췌**

```sql
-- 문제
-- deptno, dname, empno, ename
-- 모든 부서가 다 나오게
-- 부서번호 오름차순, 이름 오름차순

select deptno, dname, empno, ename
from dept d
	left outer join emp e using(deptno)
order by deptno, ename;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 631–638행 · **원본 발췌**

```sql
-- 문제 
-- deptno, dname, empno, ename 출력
-- 모든 부서가 다 나오게 해야 함
-- 부서 번호 별 오름차순, 같다면 이름 오름차순
select d.deptno, dname, empno, ename
from dept d
	left outer join emp e on (d.deptno = e.deptno)
order by deptno asc, ename asc;
```

“모든 부서”가 요구사항이면 **`DEPT d`를 왼쪽**에 놓고 `LEFT JOIN EMP e`를 한다. 연결되는 사원이 없어도 부서 행은 남고 사원 번호·이름은 `NULL`이다. 강사님은 `USING(deptno)`, 나는 `ON (d.deptno = e.deptno)`를 썼다. 둘 다 부서 번호 오름차순, 이름 오름차순이다. 결과가 부서당 반드시 한 행은 아니다. 사원이 여럿이면 그 부서가 여러 행에 나온다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `e1.mgr = e2.empno`에서 `e1`과 `e2`는 각각 어떤 역할인가?
2. “모든 부서”를 남기려면 어느 표가 `LEFT JOIN`의 왼쪽이어야 하는가?
3. 사원이 없는 부서의 사원 이름 열에는 무엇이 표시되는가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

모든 관계를 빠짐없이 결합하는 전체 외부 조인과 계층형 관리자 탐색은 이 장의 실제 코드보다 넓은 주제다. 본문은 원본의 **자기 조인과 LEFT·RIGHT 비교**에 맞춘다.
