# 09. `CASE` — 조건에 따라 결과 열 만들기

[SQL 목차](README.md) · [이전: 숫자·날짜·`NULL` 함수](08_SQL_숫자_날짜_NULL함수.md) · [다음: `UNION`](10_SQL_UNION과_UNION_ALL.md)

`CASE`는 조회 결과의 값을 조건에 따라 골라 만든다. 두 원본 모두 직업별 급여 계산과 수당의 `NULL` 처리에 사용했다. 여기서는 원본 표를 수정하는 `UPDATE`와 구분한다.

## 먼저: 조건에 따라 한 칸의 값을 만들기

원본의 `CLERK` 계산을 사원 한 명으로 줄여 보자. `job='CLERK'`, `sal=800`이면 `sal * 1.05`의 결과는 **840**이다. `CASE`는 그 행에 대해 840을 **조회 결과 열로 보여 줄 뿐**, 저장된 `sal=800`을 바꾸지 않는다. 다음은 원본 문법을 줄인 **설명용 재구성**이다.

```sql
CASE job
    WHEN 'CLERK' THEN sal * 1.05
    ELSE sal
END
```

전체 원본에는 SALESMAN 분기까지 있고, 같은 조건을 직접 적는 두 번째 `CASE` 형식도 이어진다.

<!-- chapter-toc -->

- [1. 직업 값을 바로 비교하는 형식](09_SQL_CASE_조건식.md#section-1)
- [2. 조건식을 직접 적는 형식](09_SQL_CASE_조건식.md#section-2)
- [3. `NULL` 수당을 0으로 표시](09_SQL_CASE_조건식.md#section-3)
- [직접 확인할 질문](09_SQL_CASE_조건식.md#section-4)
- [추가로 알면 좋은 것](09_SQL_CASE_조건식.md#section-5)

<a id="section-1"></a>

## 1. 직업 값을 바로 비교하는 형식

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 304–311행 · **원본 발췌**

```sql
select 
	job, sal,
	case job
		when 'CLERK' then sal * 1.05
		when 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 331–340행 · **원본 발췌**

```sql
-- case문은 end로 무조건 닫아주어야 함
-- when과 then으로 조건을 줘서 바꿀 수 있음
select 
	job, sal, 
	case job
		when 'CLERK' then sal * 1.05
		when 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;
```

`CASE job` 뒤의 `WHEN 'CLERK'`는 각 행의 `job` 값과 비교한다. CLERK면 `sal * 1.05`, SALESMAN이면 `sal * 1.03`, 어느 쪽도 아니면 `ELSE sal`을 `upsal` 열에 보여 준다. 급여 원본 값은 그대로이며, `END`로 식을 닫는다.

<a id="section-2"></a>

## 2. 조건식을 직접 적는 형식

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 313–320행 · **원본 발췌**

```sql
select 
	job, sal,
	case 
		when job = 'CLERK' then sal * 1.05
		when job = 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 342–350행 · **원본 발췌**

```sql
-- case옆에 바로 쓰지 않으면 where조건 if처럼 진행할 수 있음
select 
	job, sal, 
	case 
		when job = 'CLERK' then sal * 1.05
		when job = 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;
```

이번에는 `CASE` 뒤에 열 이름을 붙이지 않고 `WHEN job = 'CLERK'`처럼 **참·거짓 조건식**을 쓴다. 이 예제의 결과는 위 형식과 같은 의도다. 내 주석의 “`WHERE`처럼 진행”은 조건을 쓰는 모양을 빗댄 것이며, 이 `CASE` 자체가 행을 버리는 `WHERE` 절은 아니다.

<a id="section-3"></a>

## 3. `NULL` 수당을 0으로 표시

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 322–328행 · **원본 발췌**

```sql
select
	sal, comm,
	case
		when comm is null then 0
		else comm
	end
from emp;	
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 352–359행 · **원본 발췌**

```sql
-- if, null로 아래처럼 null일 때 0으로 바꿀 수 있음
select 
	sal, comm,
	case 
		when comm is null then 0
		else comm
	end
from emp;
```

`comm IS NULL`인 행만 결과 열에 0을 표시하고, 값이 있으면 원래 `comm`을 표시한다. [08장](08_SQL_숫자_날짜_NULL함수.md)의 `IFNULL`도 같은 문제를 짧게 푸는 방법이다. 어느 방법이든 이 `SELECT`만으로 표 안의 수당이 0으로 저장되지는 않는다.

<a id="section-4"></a>

## 직접 확인할 질문

1. CLERK·SALESMAN 외의 직업은 어떤 급여가 표시되는가?
2. 두 `CASE` 형식은 `WHEN` 뒤에 무엇을 적는지가 어떻게 다른가?
3. `CASE`를 쓴 `SELECT`가 실제 급여를 바꾸는가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

복잡한 중첩 `CASE`와 인덱스에 미치는 영향은 이 수업 예제의 핵심이 아니다. 우선 실제 코드의 **두 형식과 `ELSE`·`END`**를 읽는다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/09_SQL_CASE_조건식_연습문제.md) → [10. UNION과 UNION ALL](10_SQL_UNION과_UNION_ALL.md)
