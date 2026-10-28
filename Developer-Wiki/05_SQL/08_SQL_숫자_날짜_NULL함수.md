# 08. 숫자·날짜·`NULL` 함수 — 계산 전후를 구분하기

[SQL 목차](README.md) · [이전: 문자열 함수](07_SQL_문자열함수.md) · [다음: `CASE`](09_SQL_CASE_조건식.md)

두 원본의 이 구간에는 숫자를 반올림·올림·내림·버림하는 함수, 현재 시각과 날짜 양식, `NULL` 수당을 0으로 대신하는 계산이 있다. 함수마다 **입력·자릿수·`NULL` 처리**를 구분한다.

## 먼저: 같은 음수라도 결과가 다르다

원본의 `-3.14`를 그대로 넣되 함수 하나씩 계산해 보자. 아래는 **설명용 결과표**다.

| 계산 | 결과 | 읽는 법 |
| --- | ---: | --- |
| `CEIL(-3.14)` | -3 | 더 큰 정수 쪽으로 올림 |
| `FLOOR(-3.14)` | -4 | 더 작은 정수 쪽으로 내림 |
| `TRUNCATE(-3.14, 0)` | -3 | 소수 부분을 버림 |

음수에서 “내림”과 “소수 부분 버림”을 같은 동작으로 외우면 `-4`와 `-3`을 혼동한다. 뒤의 `IFNULL(comm, 0)`은 이와 달리 **값이 없을 때 대신 넣을 값**을 정한다.

<!-- chapter-toc -->

- [1. 반올림·올림·내림·버림](08_SQL_숫자_날짜_NULL함수.md#section-1)
- [2. 현재 시각 표시와 문자열 날짜 변환](08_SQL_숫자_날짜_NULL함수.md#section-2)
- [3. `NULL` 수당을 계산에 넣기](08_SQL_숫자_날짜_NULL함수.md#section-3)
- [직접 확인할 질문](08_SQL_숫자_날짜_NULL함수.md#section-4)
- [추가로 알면 좋은 것](08_SQL_숫자_날짜_NULL함수.md#section-5)

<a id="section-1"></a>

## 1. 반올림·올림·내림·버림

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 242–258행 · **원본 발췌**

```sql
-- 반올림
select round(3.14);
select round(3.145, 2);

-- 올림
select ceil(3.14);
select ceil(-3.14);

-- 내림
select floor(3.14);
select floor(-3.14);

-- 버림
select truncate(-3.14, 1);

-- 나머지
select mod(10, 3);
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 282–298행 · **원본 발췌**

```sql
-- round는 반올림 할 수 있음, ','를 사용해서 소수점 범위도 지정할 수 있음
select round(3.14);
select round(3.145, 2);

-- ceil은 올림하는 것
select ceil(3.14);
select ceil(-3.14);

-- floor는 내림하는 것
select floor(3.14);
select floor(-3.14);

-- truncate는 두 번째 전달인자가 필수이며, 소수점 몇 자리인지 확인 후 버림
select truncate(-3.14, 0);

-- mod는 나머지를 구해줌
select mod(10, 3);
```

`ROUND`는 반올림, `CEIL`은 올림, `FLOOR`는 내림, `TRUNCATE`는 지정 자리 뒤를 버린다. 양쪽 모두 **음수**를 넣어 올림·내림이 0을 향해 움직이는 것과 같은 뜻이 아님을 볼 수 있다. 강사님은 `TRUNCATE(-3.14, 1)`, 나는 `TRUNCATE(-3.14, 0)`을 실행했다. 두 번째 인자가 다른 만큼 소수 첫째 자리 유지와 정수 부분 유지라는 비교가 된다. `MOD(10, 3)`은 나머지를 구한다.

<a id="section-2"></a>

## 2. 현재 시각 표시와 문자열 날짜 변환

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 260–268행 · **원본 발췌**

```sql
-- 현재 시간
select now();
select sysdate();

-- 날짜 출력 양식 지정
select DATE_FORMAT(now(), '%Y년 %m월 %d일 %H시 %i분 %s초');

-- 문자를 날짜 형으로 변화
select str_to_date('2026-08-07', '%Y-%m-%d');
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 300–308행 · **원본 발췌**

```sql
-- now(), sysdate()는 현재 시간을 알 수 있음
select now(); -- 서버시간
select sysdate();

-- date_format(시간, 양식) 으로 나오는 형식을 변경할 수 있음
select date_format(now(), '%Y년 %m월 %d일 %H시 %i분 %s초');

-- string의 일자를 date형태로 바꾸어 줌
select str_to_date('2026-08-07', '%Y-%m-%d');
```

`NOW()`와 `SYSDATE()`는 실행 시점에 따라 값이 달라진다. `DATE_FORMAT`은 지정한 양식의 **표시 문자열**을 만들고, `STR_TO_DATE`는 양식에 맞는 문자열을 날짜 값으로 바꾼다. 따라서 문서에 적힌 `2026-08-07`을 “오늘 날짜”로 읽으면 안 된다. 내 주석의 “`NOW()`는 서버시간”은 실행 환경에 따른 시간 설정 확인이 필요하다는 뜻으로 읽는다.

<a id="section-3"></a>

## 3. `NULL` 수당을 계산에 넣기

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 270–274행 · **원본 발췌**

```sql
select ifnull(comm, 0), comm from emp;
select coalesce(comm, 0), comm from emp;

select sal * 12 + comm from emp;
select sal * 12 + ifnull(comm, 0) from emp;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 310–315행 · **원본 발췌**

```sql
-- ifnull(행/열, 기본값) 이면 null일 경우 기본값으로 바꿔줌
select ifnull(comm, 0), comm from emp;
select coalesce(comm, 0), comm from emp;

select sal * 12 + comm from emp;
select sal * 12 + ifnull(comm, 0) from emp;
```

`sal * 12 + comm`에서 `comm`이 `NULL`이면 계산 전체도 `NULL`이다. `IFNULL(comm, 0)` 또는 `COALESCE(comm, 0)`로 **수당이 없을 때만 0을 대신** 넣으면 급여 계산을 계속할 수 있다. 이는 조회 결과의 계산 방식이며 원본 표의 `COMM` 값을 수정하는 문장이 아니다. 두 원본이 같은 예제를 실행했다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `FLOOR(-3.14)`와 `TRUNCATE(-3.14, 0)`은 같은 방향으로 움직이는가?
2. `DATE_FORMAT`과 `STR_TO_DATE`는 입력과 결과의 방향이 어떻게 다른가?
3. `comm`이 `NULL`일 때 `sal * 12 + comm`과 `sal * 12 + IFNULL(comm, 0)`은 어떻게 다른가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

시간대·서버 설정·날짜 함수의 세부 차이는 환경별 확인이 필요한 확장 주제다. 여기서는 실제 원본의 **함수 호출과 계산 결과의 형태**를 우선한다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/08_SQL_숫자_날짜_NULL함수_연습문제.md) → [09. CASE](09_SQL_CASE_조건식.md)
