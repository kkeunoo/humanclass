# 10. `UNION`과 `UNION ALL` — 두 조회 결과 붙이기

[SQL 목차](README.md) · [이전: `CASE`](09_SQL_CASE_조건식.md) · [다음: 서브쿼리](11_SQL_서브쿼리.md)

두 원본은 **같은 부서 10 조회를 두 번** 붙여 중복 제거 여부를 눈으로 비교한다.

<!-- chapter-toc -->

- [1. 중복을 지울까, 남길까](10_SQL_UNION과_UNION_ALL.md#section-1)
- [2. 열 모양도 맞아야 한다](10_SQL_UNION과_UNION_ALL.md#section-2)
- [직접 확인할 질문](10_SQL_UNION과_UNION_ALL.md#section-3)
- [추가로 알면 좋은 것](10_SQL_UNION과_UNION_ALL.md#section-4)

<a id="section-1"></a>

## 1. 중복을 지울까, 남길까

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 402–408행 · **원본 발췌**

```sql
select * from emp where deptno = 10
union
select * from emp where deptno = 10;

select * from emp where deptno = 10
union all
select * from emp where deptno = 10;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 437–445행 · **원본 발췌**

```sql
-- union으로 겹치는것을 제외하고 합쳐서 한 번에 보여줄 수 있음
select * from emp where deptno = 10
union
select * from emp where deptno = 10;

-- union all은 겹치더라도 나오게 함, union보다 활용도가 높음
select * from emp where deptno = 10
union all
select * from emp where deptno = 10;
```

두 `SELECT`가 똑같은 행 집합을 만든다. `UNION`은 같은 결과 행을 한 번만 남기고, `UNION ALL`은 양쪽 행을 모두 남긴다. 따라서 이번 예제에서는 `UNION ALL` 결과 행 수가 한쪽 조회의 **두 배**다. 원본 `EMP`에서 사원이 복제되는 것은 아니다.

<a id="section-2"></a>

## 2. 열 모양도 맞아야 한다

### 강사님 코드 — 실행하지 않은 반례

출처: `teacher/workspace_sql/Script.sql` 410–414행 · **원본 발췌**

```sql
/*
select ename from emp where deptno = 10
union all
select ename, sal from emp where deptno = 10;
*/
```

강사님은 한쪽은 `ename` 하나, 다른 쪽은 `ename, sal` 두 열인 쿼리를 **주석으로 막았다**. 결과를 세로로 붙이려면 양쪽 `SELECT`의 열 개수가 같아야 한다. 실제 실행 문장으로 오해해 오류를 정상 결과처럼 적지 않는다.

### 내 코드

내 원본에서는 앞의 `SELECT *` 두 문장이 비교 대상이다. 별도 열 수 불일치 반례는 없다.

<a id="section-3"></a>

## 직접 확인할 질문

1. 같은 부서 조회를 두 번 `UNION`하면 행이 두 배가 되는가?
2. `UNION ALL`을 쓰면 왜 두 배가 되는가?
3. 양쪽 조회의 열 개수가 달라도 붙일 수 있는가?

<a id="section-4"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/10_SQL_UNION과_UNION_ALL_연습문제.md)

## 추가로 알면 좋은 것

여러 조회를 붙일 때의 정렬·자료형 변환·성능 차이는 수업의 짧은 비교 밖의 주제다. 이 장의 본문은 **중복 제거 유무와 같은 열 모양**이다.
