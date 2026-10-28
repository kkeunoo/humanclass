# 07. 문자열 함수 — 이름을 자르고 붙이고 채우기

[SQL 목차](README.md) · [이전: `GROUP BY`](06_SQL_GROUP_BY와_HAVING.md) · [다음: 숫자·날짜·`NULL` 함수](08_SQL_숫자_날짜_NULL함수.md)

강사님과 나는 `ENAME`(사원 이름)을 가지고 길이 확인, 일부 추출, 바꾸기, 채우기, 합치기를 연습했다. 함수 이름을 외우기보다 **입력 문자열이 어떤 결과 열로 바뀌는지** 따라간다.

## 먼저: 함수의 입력과 결과 한 개

원본에 등장하는 `SUBSTR` 문법을 문자열 한 개에 적용해 보자. 이것은 사원 표 전체를 조회한 원본 발췌가 아니라 **설명용 재구성**이다.

```sql
SELECT SUBSTR('SMITH', 2, 3);
-- 결과: MIT
```

시작 위치 `2`는 두 번째 글자 `M`, 길이 `3`은 `M`·`I`·`T` 세 글자를 뜻한다. 아래 실제 원본에서는 같은 함수를 `ENAME` 열에 적용해 **사원마다 결과가 달라지는 것**을 확인한다.

<!-- chapter-toc -->

- [1. 길이와 일부 추출](07_SQL_문자열함수.md#section-1)
- [2. 바꾸기·채우기·공백 지우기](07_SQL_문자열함수.md#section-2)
- [3. 붙이기와 별표 가리기 문제](07_SQL_문자열함수.md#section-3)
- [직접 확인할 질문](07_SQL_문자열함수.md#section-4)
- [추가로 알면 좋은 것](07_SQL_문자열함수.md#section-5)

<a id="section-1"></a>

## 1. 길이와 일부 추출

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 215–221행 · **원본 발췌**

```sql
select length(ename), ename from emp;
select * from emp
where length(ename) = 4;

-- 대상의 몇 번째부터 몇 개를 잘라오기
select substring(ename, 2, 3), ename from emp;
select substr(ename, 2, 3), ename from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 247–256행 · **원본 발췌**

```sql
-- length로 길이를 알 수 있음
select length(ename), ename from emp;

select * from emp
where length(ename) = 4;

-- substring(행/열, 시작, 개수)
-- 대상의 몇 번째부터 몇 개를 잘라오는게 substring
select substring(ename, 2, 3), ename from emp;
select substr(ename, 2, 3), ename from emp;
```

`SUBSTRING(ename, 2, 3)`은 이름의 **2번째 문자부터 3개**를 가져온다. 내 코드는 같은 뜻의 `SUBSTR`도 함께 사용했다. `LENGTH(ename)`은 문자열의 **바이트 길이**를 반환한다. 이 실습의 영문 이름에서는 문자 수와 같아 보이지만, 한글 이름의 글자 수를 뜻한다고 일반화하지 않는다. 강사님·내 코드 모두 영문 이름 길이로 조건을 실습했다.

<a id="section-2"></a>

## 2. 바꾸기·채우기·공백 지우기

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 223–235행 · **원본 발췌**

```sql
-- 전부 교체
select replace(ename, 'A', '에이'), ename from emp;

-- 대상의 자리수를 맞춰주고 남으면 채워줌
select lpad(ename, 10, '#') from emp;
select lpad(ename, 3, '#') from emp;

select rpad(ename, 10, '#') from emp;

select lpad(sal, 10, '0') from emp;
select lpad(ename, 10, ' ') from emp;

select trim('  a b  c  ');
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 258–273행 · **원본 발췌**

```sql
-- replace(행/열, 대상, 바꿀 문자열)
-- replace는 행/열 대상을 전부 바꿔줌
select replace(ename, 'A', '에이'), ename from emp;

-- lpad(행/열, 자릿수, 문자열)
-- 대상의 자릿수를 맞춰주고 남으면 채워주는 것이기 때문에 아래 3으로 하면 3글자로 줄어듦
select lpad(ename, 10, '#'), ename from emp; 
select lpad(ename, 3, '#'), ename from emp; 

select rpad(ename, 10, '#'), ename from emp; 

select lpad(sal, 10, '0'), ename from emp; 
select lpad(ename, 10, ' '), ename from emp; 

-- trim은 양쪽 공백을 제거해줌
select trim('  a b  c  ');
```

`REPLACE(ename, 'A', '에이')`는 조회 결과의 해당 글자를 바꿔 보여 준다. 원본 `EMP` 값이 수정되는 `UPDATE`가 아니다. `LPAD`와 `RPAD`는 지정한 길이에 맞춰 **왼쪽·오른쪽을 채운다**. 길이를 원본보다 짧게 주면 잘릴 수 있다. `TRIM`은 양끝 공백을 없앤다. 단어 사이의 공백까지 지운다고 읽지 않는다.

<a id="section-3"></a>

## 3. 붙이기와 별표 가리기 문제

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 237–240행 · **원본 발췌**

```sql
select concat(ename, job) from emp;
select concat(ename, ' ', job) from emp;
-- 오라클에서 합치기 ename || job으로 사용 가능
select concat_ws('-', ename, job, empno) from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 275–280행 · **원본 발췌**

```sql
-- concat으로 column을 한 줄로 합칠 수 있음
-- Oracle에서는 ename || job으로 합치기 사용 할 수 있음
select concat(ename, job) from emp;
select concat(ename, ' ', job) from emp;
-- concat_ws(with seperator)로 구분자를 사용하여 합칠 수 있음
select concat_ws('-', ename, job, empno) from emp;
```

`CONCAT(ename, ' ', job)`은 이름과 직업 사이에 공백을 끼워 붙인다. `CONCAT_WS('-', ename, job, empno)`는 `-`를 구분자로 쓴다. 두 원본 모두 이름 앞 두 글자 뒤를 별표로 채우는 실제 문제도 풀었다.

### 강사님 코드 — 이름 길이만큼 별표 채우기

출처: `teacher/workspace_sql/Script.sql` 294–299행 · **원본 발췌**

```sql
-- ename의 앞 두 글자만 원본 그대로 출력하고
-- 나머지 이름 만큼의 * 출력
-- WARD >> WA**, SMITH >> SM***
select
	rpad(substring(ename, 1, 2), length(ename), '*')
from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 320–326행 · **원본 발췌**

```sql
-- ename의 앞 두 글자만 원본 그대로 출력하고,
-- 4개의 *표를 붙여서 출력
select rpad(substr(ename, 1, 2), 6, '*'), ename from emp;

-- ename의 앞 두 글자만 원본 그대로 출력하고
-- 나머지 이름 만큼의 *를 출력 
select rpad(substr(ename, 1, 2), length(ename), '*'), ename from emp;
```

강사님은 `RPAD(SUBSTRING(ename, 1, 2), LENGTH(ename), '*')`, 나는 `RPAD(SUBSTR(...), LENGTH(ename), '*')` 형태다. 둘 다 앞 두 글자를 남기고 **원래 이름 길이까지** `*`로 채운다. 내 코드의 앞 문장은 길이 6으로 고정해 “별표 4개”를 붙이는 별도 문제이고, 뒤 문장이 이름 길이에 맞춘 풀이이다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `SUBSTRING('SMITH', 2, 3)`은 어느 글자를 가져오는가?
2. 길이 4인 이름에 `RPAD(앞 두 글자, LENGTH(ename), '*')`를 적용하면 별표는 몇 개인가?
3. `REPLACE`가 원본 표의 값을 바꾸는가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

다국어 문자열의 글자 수가 필요할 때 `CHAR_LENGTH` 같은 별도 함수가 있다. 원본의 핵심은 `LENGTH`를 **영문 실습 데이터에 적용한 결과**와 문자열 가공 순서를 읽는 것이다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/07_SQL_문자열함수_연습문제.md) → [08. 숫자·날짜·NULL 함수](08_SQL_숫자_날짜_NULL함수.md)
