# 03. `LIKE`와 `NULL` — 글자 패턴과 값 없음

[SQL 목차](README.md) · [이전: `WHERE`](02_SQL_WHERE와_조건연산자.md) · [다음: 정렬과 `LIMIT`](04_SQL_정렬과_LIMIT.md)

이름을 패턴으로 찾는 조건과 `NULL`을 찾는 조건은 다르게 쓴다. 양쪽 `Script.sql`에 실제 문제와 오답 비교가 남아 있다.

## 먼저: 글자 패턴과 값 없음은 다른 질문

다음은 수업 문법을 한눈에 보기 위한 **설명용 작은 표**다. 원본 `EMP`의 전체 결과가 아니다.

| ENAME | COMM |
| --- | ---: |
| SMITH | `NULL` |
| SCOTT | 0 |
| ALLEN | 300 |

`ename LIKE 'S%'`라면 이 표에서는 **SMITH와 SCOTT**이 남는다. `comm IS NULL`이라면 **SMITH만** 남는다. SCOTT의 `0`은 금액이 0인 값이고 `NULL`은 값이 없는 상태이므로 서로 다르게 검사한다. 아래 원본에서 패턴의 `%`와 한 글자 `_`의 차이를 이어 확인하자.

<!-- chapter-toc -->

- [1. `%`와 `_`의 차이](03_SQL_LIKE와_NULL.md#section-1)
- [2. 대소문자 실험을 읽는 법](03_SQL_LIKE와_NULL.md#section-2)
- [3. `= NULL` 대신 `IS NULL`](03_SQL_LIKE와_NULL.md#section-3)
- [직접 확인할 질문](03_SQL_LIKE와_NULL.md#section-4)
- [추가로 알면 좋은 것](03_SQL_LIKE와_NULL.md#section-5)

<a id="section-1"></a>

## 1. `%`와 `_`의 차이

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 96–113행 · **원본 발췌**

```sql
-- % : 모든 글자를 뜻 함(심지어 글씨가 없어도 포함)
select * from emp
where ename like 'S%';

select * from emp
where ename like '%N';

select * from emp
where ename like '%AM%';

-- _ : 아무 글자 딱 하나
select * from emp
where ename like '_L%';

-- 문제
-- 이름이 5글자인 사람만 출력
select * from emp
where ename like '_____';
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 127–146행 · **원본 발췌**

```sql
-- % 는 모든 글자를 뜻 함(심지어 글씨가 없더라도 포함)
-- '문자열%', '%문자열'로 문자열로 시작하거나 끝나는 값을 검색할 수 있음
select * from emp
-- where ename like 'SCOTT';
where ename like 'S%';

select * from emp
where ename like '%N';

-- '%문자열%'은 A로 시작하거나, 끝나거나, 포함한 검색 값
select * from emp
where ename like '%AM%';

-- '_' underscore는 한 글자 아무거나이고, 두번째 글자가 L인 값을 검색
select * from emp
where ename like '_L%';

-- 문제4 _ 이름이 5글자인 사람만 출력 (나중에 length가 따로 있음)
select * from emp
where ename like '_____';
```

`'S%'`는 S로 시작하는 이름, `'%N'`은 N으로 끝나는 이름, `'%AM%'`은 가운데를 포함해 AM이 이어지는 이름을 찾는다. `%`는 **0글자 이상**, `_`는 **정확히 한 글자**에 대응한다. 그래서 `'_____'`는 길이가 5글자인 이름을 찾는다. 내 원본의 `'_L%'`에서 두 번째 글자가 L이다.

<a id="section-2"></a>

## 2. 대소문자 실험을 읽는 법

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 115–123행 · **원본 발췌**

```sql
select 'Human';
select lower('Human');
select upper('Human');

-- 문제
-- 'Am'을 이용해서 am이 이름 중간에 들어가는 사람만 출력
-- (mariaDB는 like에서 대소문자 구분 원래 안함)
select * from emp
where lower(ename) like lower('%Am%');
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 148–161행 · **원본 발췌**

```sql
select 'HUMAN';
select lower('Human');
select upper('Human');

-- 문제5 _ 사용자가 'Am'을 이용해서 am이 이름 중간에 들어가는 사람만 출력
-- MariaDB에서 대/소문자를 구분하지 않아 현재 출력값은 같음
select * from emp
where upper(ename) like upper('%Am%');
select * from emp
where lower(ename) like lower('%Am%');

-- 문제6 _ 부서 10 또는 20의 사원 중, 이름에 A가 들어가는 사원만 출력
select * from emp
where (deptno in (10,20)) and ename like '%A%'
```

강사님은 `lower(ename) LIKE lower('%Am%')`, 나는 `upper`와 `lower`를 각각 사용했다. 이 자료가 대상으로 삼은 MariaDB 실습에서는 대소문자를 구분하지 않는 비교 결과를 관찰한 것으로 적혀 있다. 그렇다고 모든 문자열 비교·모든 DB 설정에서 항상 같다고 일반화하지 않는다. 내 6번 문제의 `(deptno IN (10,20)) AND ename LIKE '%A%'`는 **부서와 이름 조건을 함께** 적용한 실제 풀이이고, 강사님 해당 줄은 문제만 적고 답은 비워 두었다.

<a id="section-3"></a>

## 3. `= NULL` 대신 `IS NULL`

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 129–141행 · **원본 발췌**

```sql
select * from emp;

select * from emp
where comm = null;

select * from emp
where comm < 100;

select * from emp
where comm is null;

select * from emp
where comm is not null;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 163–176행 · **원본 발췌**

```sql
select * from emp;

select * from emp
where comm = null;

select * from emp
where comm < 100;

-- Query에서 null상태는 'is null' 또는 'is not null'로 구분한다
select * from emp
where comm is null;

select * from emp
where comm is not null;
```

두 원본 모두 `comm = null`을 시험해 보고 `comm IS NULL`과 `comm IS NOT NULL`을 이어서 썼다. `NULL`은 **값이 없음**을 나타내므로 `= NULL`은 참이 되지 않는다. 수당 정보가 없는 행은 `IS NULL`로 찾는다. `comm < 100`도 `NULL` 수당을 가진 행을 포함하지 않는다. `NULL`을 숫자 0과 같은 값으로 읽지 않는다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 이름 `SMITH`는 `'S%'`, `'%N'`, `'_____'` 중 어디에 맞는가?
2. `comm = null`과 `comm IS NULL`의 결과가 다른 이유는?
3. 내 6번 문제에는 강사님 문제 문장에 없는 어떤 실제 풀이가 들어갔는가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

문자 비교 규칙(콜레이션), 인덱스와 `LIKE`의 성능은 환경에 따라 다르다. 이 장의 필수 범위는 원본에서 실행한 **패턴 문자와 `IS NULL` 조건**이다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/03_SQL_LIKE와_NULL_연습문제.md) → [04. 정렬과 LIMIT](04_SQL_정렬과_LIMIT.md)
