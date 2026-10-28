# 06. `GROUP BY`와 `HAVING` — 묶은 뒤 걸러 내기

[SQL 목차](README.md) · [이전: 집계 함수](05_SQL_집계함수.md) · [다음: 문자열 함수](07_SQL_문자열함수.md)

전체 사원 수 한 값이 아니라 **부서별·직업별** 값을 구하려면 행을 먼저 묶는다. 실제 원본에는 `WHERE`와 `HAVING`의 역할 차이, 그리고 내 코드의 그룹 기준 실수까지 남아 있다.

## 먼저: 같은 번호끼리 묶으면 무엇이 달라질까?

다음은 **설명용 세 행**이다. 10번 부서에 두 명, 20번 부서에 한 명이 있다.

| ENAME | DEPTNO | SAL |
| --- | ---: | ---: |
| CLARK | 10 | 2450 |
| KING | 10 | 5000 |
| SMITH | 20 | 800 |

`GROUP BY deptno` 뒤 `COUNT(*)`를 구하면 **10번: 2명, 20번: 1명**이다. 여기에 `HAVING COUNT(*) >= 2`를 붙이면 10번 부서만 남는다. 이 값은 원본 `EMP` 전체 집계가 아닌 작은 표의 결과다. 실제 코드의 부서·직업별 집계는 아래에서 비교한다.

<!-- chapter-toc -->

- [1. 부서별 집계와 두 열로 묶기](06_SQL_GROUP_BY와_HAVING.md#section-1)
- [2. `WHERE`는 행, `HAVING`은 그룹](06_SQL_GROUP_BY와_HAVING.md#section-2)
- [직접 확인할 질문](06_SQL_GROUP_BY와_HAVING.md#section-3)
- [추가로 알면 좋은 것](06_SQL_GROUP_BY와_HAVING.md#section-4)

<a id="section-1"></a>

## 1. 부서별 집계와 두 열로 묶기

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 331–341행 · **원본 발췌**

```sql
select deptno from emp
group by deptno;

select 
	deptno, count(*), sum(sal)
from emp
group by deptno;

select deptno, job, count(*)
from emp
group by deptno, job;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 361–379행 · **원본 발췌**

```sql
-- distinct와 비슷한 결과물을 검색할 수 있음
select deptno from emp
group by deptno;

-- group by와 집계함수를 같이 쓰면 '그룹별'이 가능
select 
	deptno, count(*), sum(sal) 
from emp
group by deptno;

-- 이렇게 쓰면 각 첫 번째것만 나오기 때문에 상위에 있는것은 group by에 넣어줘야 함
select deptno, job
from emp
group by deptno;

-- group by에 있는것을 select에 사용할 수 있음
select deptno, job, count(*)
from emp
group by deptno, job;
```

`GROUP BY deptno`는 같은 부서 번호의 사원을 한 그룹으로 만든다. `COUNT(*)`, `SUM(sal)`은 **부서마다** 계산된다. `GROUP BY deptno, job`은 같은 부서에서도 직업별로 나눈다. 내 372–374행은 `job`을 출력하면서 `deptno`만 그룹으로 묶는 실험이다. 그 그룹 안에 직업이 여러 개라면 어떤 `job`인지 정해지지 않아 설정에 따라 오류가 나거나 임의 값을 보일 수 있다. **강사님처럼 출력할 비집계 열을 그룹 기준에 함께 넣는 방식**이 이 예제의 의도에 맞다.

<a id="section-2"></a>

## 2. `WHERE`는 행, `HAVING`은 그룹

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 363–381행 · **원본 발췌**

```sql
-- 부서, 직업 별 평균이 2000 이상
SELECT 
    AVG(sal) AS avg_sal,
    deptno,
    job
FROM emp
GROUP BY deptno, job
HAVING AVG(sal) >= 2000;

SELECT 
    AVG(sal) AS avg_sal,
    deptno,
    job
FROM emp
where deptno = 10
GROUP BY deptno, job
HAVING deptno = 10; 
-- where 조건을 having에 적을 수 있지만
-- 통상 group by와 관련된 것만 적는다
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 402–416행 · **원본 발췌**

```sql
-- 부서, 직업 별 sal평균이 2000이상인 조건 식
select
	 avg(sal), deptno, job
from emp
group by deptno, job, sal
having avg(sal) >= 2000;

-- having은 group by에 조건식을 걸 수 있지만 실무에서 주로 사용하진 않음
select
	 avg(sal), deptno, job
from emp
group by deptno, job
having deptno = 10; 
-- where 조건을 having에 적을 수 있지만,
-- 통상 group by와 관련 된 것만 적는것이 좋다
```

강사님은 `GROUP BY deptno, job`으로 묶고 `HAVING AVG(sal) >= 2000`으로 **평균 급여가 기준 이상인 그룹**을 남긴다. 내 403–407행은 여기에 `sal`까지 그룹 기준으로 넣었다. 그러면 같은 부서·직업이라도 급여가 다른 사원은 **서로 다른 그룹**이 되어 “부서·직업별 평균”이라는 주석의 뜻과 달라진다. 이 경우 강사님처럼 `GROUP BY deptno, job`이 더 정확하다. 원본 코드는 그대로 보여 주되 결과 해석을 바로잡는다.

### 강사님 코드 — 먼저 행을 거르는 경우

출처: `teacher/workspace_sql/Script.sql` 383–391행 · **원본 발췌**

```sql
-- 직업 별로 연봉 1000 이상인 사람이 3명 이상인 경우만 출력 
select
	job, count(*) cnt
from emp
where sal >= 1000 
-- and cnt >= 3
-- and count(*) >= 3
group by job
having count(*) >= 3
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 418–428행 · **원본 발췌**

```sql
-- and에 cnt나 count를 써버리면, from부터 실행되기 때문에
-- 어떤 column인지 알 수 없어 having에 조건식을 줘서 조회해야 함
-- 직업 별로 연봉 1,000이상인 사람이 3명 이상인 경우 출력 조건식
select
	job, count(*) cnt
from emp
-- and cnt >= 3
-- and count(*) >= 3
where sal >= 1000
group by job
having count(*) >= 3
```

두 코드는 먼저 `WHERE sal >= 1000`으로 **급여가 낮은 사원 행을 제외**하고, `GROUP BY job`으로 직업별 묶음을 만든 다음 `HAVING COUNT(*) >= 3`으로 **3명 이상인 그룹**만 남긴다. 내 주석의 “`HAVING`은 실무에서 주로 사용하지 않는다”는 일반 규칙이 아니다. 이 문제에서는 `HAVING`이 정확히 필요한 자리다.

<a id="section-3"></a>

## 직접 확인할 질문

1. `GROUP BY deptno`와 `GROUP BY deptno, job`의 그룹 수는 왜 달라질 수 있는가?
2. 내 코드에 `sal`을 그룹 기준으로 더하면 평균의 의미가 어떻게 바뀌는가?
3. `sal >= 1000`과 `COUNT(*) >= 3`은 각각 어디에 적는가?

<a id="section-4"></a>

## 추가로 알면 좋은 것

그룹 기준에 없는 열을 허용하는지, 어떤 값을 보여 주는지는 SQL 모드에 영향을 받는다. 본문에서는 수업의 **그룹 기준을 명확히 적는 방법**을 먼저 익힌다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/06_SQL_GROUP_BY와_HAVING_연습문제.md) → [07. 문자열 함수](07_SQL_문자열함수.md)
