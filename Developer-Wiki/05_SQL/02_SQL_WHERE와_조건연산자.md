# 02. `WHERE` — 어떤 행을 남길까

[SQL 목차](README.md) · [이전: `SELECT`](01_SQL_기초와_SELECT.md) · [다음: `LIKE`와 `NULL`](03_SQL_LIKE와_NULL.md)

`SELECT`가 결과 열을 고른다면 `WHERE`는 조건에 맞는 **행**을 고른다. 두 원본 모두 부서·직업·급여를 조건으로 사용했다.

## 먼저: 한 행이 남는지 판단하기

다음은 조건의 결과를 읽기 위한 **설명용 작은 표**다. 원본 `EMP` 전체를 줄인 것이며, 아래 세 행이 실제 표의 모든 사원이라는 뜻은 아니다.

| ENAME | DEPTNO | JOB |
| --- | ---: | --- |
| SMITH | 20 | CLERK |
| JONES | 20 | MANAGER |
| ALLEN | 30 | SALESMAN |

```sql
-- 위 세 행만 놓고 결과를 예상하는 설명용 재구성
SELECT ename FROM emp WHERE deptno = 20;
```

이 세 행 중에서는 **SMITH와 JONES**가 남고 ALLEN은 빠진다. `AND job = 'CLERK'`를 더하면 **SMITH만** 남는다. 실제 원본 표에는 이 밖의 사원도 있으므로 이 이름 목록을 전체 실행 결과로 외우지 않는다.

<!-- chapter-toc -->

- [1. 한 조건과 여러 조건](02_SQL_WHERE와_조건연산자.md#section-1)
- [2. 경계값과 `BETWEEN`](02_SQL_WHERE와_조건연산자.md#section-2)
- [3. 같은 열의 여러 값: `IN`](02_SQL_WHERE와_조건연산자.md#section-3)
- [직접 확인할 질문](02_SQL_WHERE와_조건연산자.md#section-4)
- [추가로 알면 좋은 것](02_SQL_WHERE와_조건연산자.md#section-5)

<a id="section-1"></a>

## 1. 한 조건과 여러 조건

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 39–54행 · **원본 발췌**

```sql
select * 
from emp
where deptno = 20;

select *
from emp
where deptno = 20 and job='CLERK';

select * from emp
where deptno = 20 or  job='CLERK';

select * from emp
where deptno = 30 or deptno = 20 and job = 'CLERK';

select * from emp
where (deptno = 30 or deptno = 20) and job = 'CLERK';
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 70–90행 · **원본 발췌**

```sql
-- where로 조건을 걸어 볼 수 있음
select * 
from emp
where deptno = 20;

-- where의 값일 땐 '대/소문자'를 구분 함, and로 여러가지의 조건
select * 
from emp
where deptno = 20 and job = 'CLERK';

-- job이 CLERK이거나, deptno이 20인 사람은 or로 출력
select * from emp
where deptno = 20 or job = 'CLERK';

-- and가 or보다 우선순위이기 때문에, 필요 시 괄호 활용
-- 아래는 deptno = 20 and job = 'CLERK' 가 먼저 필터링 됨
select * from emp
where deptno = 30 or deptno = 20 and job = 'CLERK';

select * from emp
where (deptno = 30 or deptno = 20) and job = 'CLERK';
```

`deptno = 20 AND job = 'CLERK'`는 **둘 다 참**인 사원만 남긴다. `OR`는 어느 한쪽이 참이면 남긴다. `AND`가 `OR`보다 먼저 결합하므로 `deptno = 30 OR deptno = 20 AND job = 'CLERK'`와 `(deptno = 30 OR deptno = 20) AND job = 'CLERK'`는 결과가 다를 수 있다. 업무 문장의 “또는 … 이면서 …” 범위가 헷갈리면 괄호로 묶는다.

<a id="section-2"></a>

## 2. 경계값과 `BETWEEN`

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 68–83행 · **원본 발췌**

```sql
-- 문제1
-- 급여가 2000 이상이고 3000 미만인 사원을 출력
select * from emp
where sal >= 2000 and sal < 3000;

-- between A and B
-- A 이상 and B 이하
select * from emp
where sal between 2000 and 3000;

-- 문제2
-- job이 CLERK 이거나 급여가 2000초과 이면서 부서 번호 10인 사원만 출력
select * from emp
where
	job = 'CLERK'
	or (sal > 2000 and deptno = 10)
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 105–116행 · **원본 발췌**

```sql
-- 문제1 _ 급여가 2,000이상이고 3,000미만인 사원
select * from emp
where SAL >= 2000 and SAL < 3000;

-- between을 쓰면 범위를 지정해서 볼 수 있음
-- between A and B 는 이상/이하만 가능
select * from emp
where sal between 2000 and 3000;

-- 문제2 _ job이 CLERK 이거나 급여가 2,000초과 이면서 부서번호가 10인 사원만 출력
select * from emp
where job = 'CLERK' or (SAL > 2000 and DEPTNO = 10);
```

“2,000 이상 **3,000 미만**”은 `sal >= 2000 AND sal < 3000`이다. `BETWEEN 2000 AND 3000`은 **양 끝을 포함**하므로 같은 조건으로 바꾸면 3,000인 사원까지 포함한다. 강사님은 문제 풀이 옆에 `BETWEEN`의 양 끝 포함을 바로 주석으로 표시해 이 차이를 확인하기 좋다. 내 코드 역시 별개 문장으로 둘을 실습했다.

<a id="section-3"></a>

## 3. 같은 열의 여러 값: `IN`

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 85–94행 · **원본 발췌**

```sql
select * from emp
where deptno = 20 or deptno = 30 or deptno = 10;

-- 컬럼이 같고 or로 연결되어 있는 경우
-- in으로 간편하게 표현 가능
select * from emp
where deptno in (20, 30);

select * from emp
where deptno not in (20, 30);
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 118–125행 · **원본 발췌**

```sql
-- where에서 컬럼이 같고 or일 때 줄일 수 있는 방법 (in)
-- select * from emp
-- where deptno = 20 or deptno = 30
select * from emp
where deptno in (20, 30)

select * from emp
where deptno not in (20, 30)
```

`deptno IN (20, 30)`은 부서 번호가 **20 또는 30**인 행을 고른다. `NOT IN`은 이 목록에 없는 값을 고른다. 내 두 문장에는 끝 세미콜론이 없으므로 편집기에서 여러 문장을 함께 실행할 때는 문장 경계를 확인한다. `NULL`이 포함된 `NOT IN`의 복잡한 동작은 지금의 원본 예제에 없으므로 기본 규칙처럼 암기하지 않는다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 3,000인 사원이 첫 번째 급여 문제에 포함되는가? `BETWEEN`에는 포함되는가?
2. 괄호 앞뒤의 두 `OR`·`AND` 식은 어느 사원에서 달라질 수 있는가?
3. 부서 20·30을 `OR`와 `IN`으로 각각 어떻게 쓸까?

<a id="section-5"></a>

## 추가로 알면 좋은 것

복잡한 조건에서 `NULL`의 삼값 논리와 `NOT IN`의 특수한 경우는 별도 주제다. 이 장에서는 실제 수업의 **비교 연산·괄호·경계값·`IN`**을 먼저 정확히 읽는다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/02_SQL_WHERE와_조건연산자_연습문제.md) → [03. LIKE와 NULL](03_SQL_LIKE와_NULL.md)
