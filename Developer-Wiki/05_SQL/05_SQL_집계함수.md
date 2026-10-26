# 05. 집계 함수 — 여러 행을 한 값으로 요약하기

[SQL 목차](README.md) · [이전: 정렬과 `LIMIT`](04_SQL_정렬과_LIMIT.md) · [다음: `GROUP BY`](06_SQL_GROUP_BY와_HAVING.md)

집계 함수는 사원 여러 행에서 **개수·최댓값·최솟값·합계·평균**을 계산한다. 결과를 한 값으로 요약하는 함수와 각 사원 이름을 그대로 출력하는 일을 혼동하지 않도록 원본의 실험을 비교한다.

<!-- chapter-toc -->

- [1. `COUNT(*)`와 `COUNT(열)`](05_SQL_집계함수.md#section-1)
- [2. 최대·최소·합계·평균](05_SQL_집계함수.md#section-2)
- [3. 요약값과 한 사원의 이름을 섞을 때](05_SQL_집계함수.md#section-3)
- [직접 확인할 질문](05_SQL_집계함수.md#section-4)
- [추가로 알면 좋은 것](05_SQL_집계함수.md#section-5)

<a id="section-1"></a>

## 1. `COUNT(*)`와 `COUNT(열)`

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 198–202행 · **원본 발췌**

```sql
-- 집계 함수
select count(ename) from emp;
select count(mgr) from emp;
select count(comm) from emp; -- null은 개수에서 제외
select count(*) from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 226–231행 · **원본 발췌**

```sql
-- 집계 함수는 한 줄의 한 칸으로 나오며 group by와 잘 어울림
-- count는 특정 열 또는 행의 개수를 검색해줌, null은 빼고 세줌
select count(ename) from emp; 
select count(mgr) from emp;
select count(comm) from emp;
select count(*) from emp; -- *을 써서 모든 줄을 보는 경우가 많음
```

`COUNT(*)`는 조건에 맞는 **행**을 세고, `COUNT(comm)`은 `comm` 값이 `NULL`이 아닌 행만 센다. `COUNT(ename)`도 이름이 `NULL`인 행은 제외한다. 그래서 수당이 없는 사원이 있다면 `COUNT(comm)`은 전체 사원 수보다 작다. 내 주석의 “집계 함수는 한 줄의 한 칸”은 전체 집계를 너무 단순화한 표현이다. `GROUP BY`를 더하면 **그룹마다 한 행씩** 나온다.

<a id="section-2"></a>

## 2. 최대·최소·합계·평균

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 204–211행 · **원본 발췌**

```sql
select max(sal) from emp;
select min(sal) from emp;
select max(ename) from emp;
select min(ename) from emp;

select sum(sal) from emp;

select avg(sal) from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 233–241행 · **원본 발췌**

```sql
-- min, max는 각 최소값, 최대값이며 문자열에 사용해도 a-z순
select max(sal) from emp;
select min(sal) from emp;

-- 해당 컬럼의 합을 구할 때 사용
select sum(sal) from emp;

-- 해당 컬럼의 평균치를 구할 때 사용
select avg(sal) from emp;
```

`MAX(sal)`과 `MIN(sal)`은 급여의 양 끝값, `SUM(sal)`은 합계, `AVG(sal)`은 평균이다. 강사님은 숫자뿐 아니라 `MAX(ename)`, `MIN(ename)`도 넣어 문자에도 순서 비교가 적용됨을 보여 준다. 내 코드에는 이 문자열 비교가 없다. 다만 문자의 정렬 규칙은 DB 설정에 따라 달라질 수 있으므로 이름의 고정된 결과를 여기서 외우지 않는다.

<a id="section-3"></a>

## 3. 요약값과 한 사원의 이름을 섞을 때

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 213–213행 · **원본 발췌**

```sql
select count(*), ename from emp; -- 원하는 결과가 안나온다
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 243–245행 · **원본 발췌**

```sql
-- 집계함수는 1줄로 셀 병합을 허용하지 않기 때문에 
-- 다른 여러 줄이 나오는 함수와 사용 시 원하는 결과를 얻기 어려움
select count(*), ename from emp;
```

`COUNT(*)`는 전체 결과를 요약하는데 `ename`은 한 행의 값이다. 그룹 기준 없이 둘을 섞으면 **어느 사원 이름인지 정해지지 않거나 SQL 모드에 따라 오류**가 될 수 있다. 내 주석의 “셀 병합”은 SQL의 실제 원리를 설명하지 못한다. 특정 사원의 이름과 함께 부서별 수를 보려면 어떤 그룹의 값을 보여 줄지 먼저 정해야 한다. 이어지는 [06장](06_SQL_GROUP_BY와_HAVING.md)에서 그 기준을 만든다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `COUNT(*)`와 `COUNT(comm)`은 `NULL` 수당 행을 각각 어떻게 처리하는가?
2. `MAX(sal)`은 최고 급여 사원의 **이름**까지 알려 주는가?
3. `COUNT(*)` 옆에 `ename`을 아무 기준 없이 놓으면 왜 해석이 곤란한가?

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/05_SQL_집계함수_연습문제.md)

## 추가로 알면 좋은 것

중앙값·분산 같은 통계 함수와 윈도 함수는 이 수업 코드의 현재 집계 범위가 아니다. 이 장은 실제 작성한 다섯 집계 함수와 `NULL` 제외 규칙을 먼저 다룬다.
