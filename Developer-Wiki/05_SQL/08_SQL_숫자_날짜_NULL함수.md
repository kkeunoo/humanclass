---
title: SQL 숫자·날짜·NULL 함수
version: v3.0-final
last_updated: 2026-08-13
status: Completed
---

# SQL 숫자·날짜·NULL 함수

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `08_SQL_숫자_날짜_NULL함수.md` |
| 분류 | `05_SQL` |
| 원본 기준 | `workspace_sql/Script.sql`, `workspace_teacher/workspace_sql/Script.sql` |
| DB 기준 자료 | `[DB]학습용_emp 신규-mariadb.sql` |
| DBMS | MariaDB |
| 핵심 범위 | `ROUND`, `CEIL`, `FLOOR`, `TRUNCATE`, `MOD`, `NOW`, `SYSDATE`, `DATE_FORMAT`, `STR_TO_DATE`, `IFNULL`, `COALESCE` |
| 학습 범위 | 반올림·올림·내림·버림·나머지, 현재 시각, 날짜 Formatting/Parsing, NULL 대체 |
| 다음 범위 제외 | `CASE`, `UNION`, Subquery, JOIN |
| 문서 형식 | SQL Developer-Wiki V3 백과사전 형식 |

> 이 문서는 `Script.sql`의 문자열 함수 다음 구간에 등장하는 숫자 함수, 날짜 함수, NULL 처리 함수를 정리한다.  
> 단순히 함수 결과만 외우지 않고 **양수·음수에서의 반올림/올림/내림 차이**, `NOW()`와 `SYSDATE()`의 의미 차이, 날짜를 문자열로 “표시”하는 것과 문자열을 날짜로 “해석”하는 것, `IFNULL()`과 `COALESCE()`의 역할 차이를 함께 이해한다.

---

# 학습 목표

- `ROUND()`로 반올림할 수 있다.
- `ROUND(value, digits)`의 두 번째 인수 의미를 설명할 수 있다.
- `CEIL()`과 `FLOOR()`를 양수·음수에서 구분할 수 있다.
- `TRUNCATE()`가 반올림이 아니라 자릿수 절삭이라는 점을 이해할 수 있다.
- `MOD()`로 나머지를 계산할 수 있다.
- `NOW()`와 `SYSDATE()`의 공통점과 차이를 설명할 수 있다.
- `DATE_FORMAT()`으로 날짜·시간 출력 형식을 변경할 수 있다.
- `STR_TO_DATE()`로 문자열을 날짜/시간 값으로 해석할 수 있다.
- `IFNULL()`과 `COALESCE()`로 NULL 대체값을 만들 수 있다.
- `NULL`이 포함된 산술식과 NULL 대체 후 산술식의 차이를 설명할 수 있다.

---

# 1. 숫자 함수란?

숫자 함수는 숫자 값을 입력받아 반올림, 올림, 내림, 절삭, 나머지 계산 같은 결과를 반환한다.

```text
ROUND
→ 반올림

CEIL
→ 올림

FLOOR
→ 내림

TRUNCATE
→ 지정 자릿수 이후 절삭

MOD
→ 나머지
```

---

# 2. ROUND

원본:

```sql
SELECT ROUND(3.14);
```

Result:

```text
3
```

소수점 이하를 반올림해 정수 결과를 만든다.

---

# 3. ROUND 두 번째 인수

```sql
SELECT ROUND(3.145, 2);
```

두 번째 인수는 **소수점 이하 몇 자리까지 남길지**를 지정한다.

```text
ROUND(value, 2)
→ 소수점 이하 2자리 기준
```

---

# 4. ROUND의 핵심

```sql
SELECT ROUND(123.4567, 2);
```

개념적으로:

```text
123.4567
→ 소수점 이하 2자리까지 남기기 위해 반올림
→ 123.46
```

---

# 5. ROUND는 단순 삭제가 아니다

```text
ROUND
→ 다음 자릿수를 보고 반올림

TRUNCATE
→ 다음 자릿수를 보고 올리지 않고 절삭
```

둘을 구분한다.

---

# 6. ROUND 음수 자릿수

MariaDB에서는 두 번째 인수에 음수를 사용해 정수부 자릿수를 기준으로 반올림할 수도 있다.

```sql
SELECT ROUND(1234.56, -2);
```

백의 자리 기준 반올림과 같은 용도로 활용할 수 있다.

기본 수업에서는 `0` 이상 자릿수부터 확실히 이해한다.

---

# 7. CEIL

원본:

```sql
SELECT CEIL(3.14);
```

Result:

```text
4
```

`CEIL()`은 입력값보다 **크거나 같은 가장 작은 정수**를 반환한다.

---

# 8. CEIL 음수

원본:

```sql
SELECT CEIL(-3.14);
```

Result:

```text
-3
```

여기서 자주 헷갈린다.

```text
-3
→ -3.14보다 큼

-4
→ -3.14보다 작음
```

따라서 올림은 `-3`이다.

---

# 9. FLOOR

원본:

```sql
SELECT FLOOR(3.14);
```

Result:

```text
3
```

`FLOOR()`는 입력값보다 **작거나 같은 가장 큰 정수**를 반환한다.

---

# 10. FLOOR 음수

원본:

```sql
SELECT FLOOR(-3.14);
```

Result:

```text
-4
```

음수에서는 “소수점 버리기”라고 생각하면 틀리기 쉽다.

```text
FLOOR
→ 수직선에서 아래쪽 정수

-3.14
→ -4
```

---

# 11. CEIL과 FLOOR 비교

```sql
SELECT
    CEIL(3.14) AS ceil_positive,
    FLOOR(3.14) AS floor_positive,
    CEIL(-3.14) AS ceil_negative,
    FLOOR(-3.14) AS floor_negative;
```

핵심:

```text
3.14
CEIL  → 4
FLOOR → 3

-3.14
CEIL  → -3
FLOOR → -4
```

---

# 12. TRUNCATE

원본 내 코드:

```sql
SELECT TRUNCATE(-3.14, 0);
```

강사님 코드:

```sql
SELECT TRUNCATE(-3.14, 1);
```

구조:

```text
TRUNCATE(value, digits)
```

두 번째 인수는 필수이며 남길 소수 자릿수를 지정한다.

---

# 13. TRUNCATE 0자리

```sql
SELECT TRUNCATE(-3.14, 0);
```

소수점 이하를 절삭한다.

개념 결과:

```text
-3
```

`FLOOR(-3.14) = -4`와 다르다.

---

# 14. TRUNCATE 1자리

```sql
SELECT TRUNCATE(-3.14, 1);
```

Result:

```text
-3.1
```

강사님 원본은 이 형태를 사용한다.

---

# 15. FLOOR와 TRUNCATE 차이

음수에서 차이가 특히 명확하다.

```sql
SELECT
    FLOOR(-3.14),
    TRUNCATE(-3.14, 0);
```

```text
FLOOR
→ -4

TRUNCATE
→ -3
```

`TRUNCATE`는 0 방향으로 자릿수를 잘라내는 결과처럼 보일 수 있고, `FLOOR`는 항상 입력 이하의 정수 방향이다.

---

# 16. ROUND와 TRUNCATE 비교

```sql
SELECT
    ROUND(3.146, 2),
    TRUNCATE(3.146, 2);
```

개념:

```text
ROUND
→ 3.15

TRUNCATE
→ 3.14
```

---

# 17. MOD

원본:

```sql
SELECT MOD(10, 3);
```

Result:

```text
1
```

10을 3으로 나눈 나머지다.

---

# 18. MOD 활용

짝수/홀수 판단 같은 조건에도 사용할 수 있다.

```sql
SELECT MOD(10, 2);
```

```text
0
→ 2로 나누어 떨어짐
```

---

# 19. MOD와 `%`

DBMS에서는 `%` Operator도 나머지 계산에 지원될 수 있지만, 함수 형태인 `MOD()`를 사용하면 의도가 분명하다.

```sql
SELECT MOD(10, 3);
```

---

# 20. 숫자 함수와 Column

함수는 상수뿐 아니라 Column에도 적용한다.

```sql
SELECT
    ename,
    sal,
    ROUND(sal / 12, 2) AS monthly_value
FROM emp;
```

단, `SAL`의 지급 주기가 Schema에 명확히 정의되어 있지 않으므로 업무 의미를 임의로 단정하지 않는다.

---

# 21. 날짜·시간 함수란?

날짜 함수는 현재 날짜·시간을 조회하거나 표시 형식을 바꾸거나 문자열을 날짜 값으로 해석할 때 사용한다.

원본의 핵심 함수:

```text
NOW
SYSDATE
DATE_FORMAT
STR_TO_DATE
```

---

# 22. NOW

원본:

```sql
SELECT NOW();
```

현재 Date와 Time을 반환한다.

대표 형태:

```text
YYYY-MM-DD HH:MM:SS
```

---

# 23. NOW는 서버/세션 시간 기준

`NOW()`가 반환하는 값은 Database Server의 현재 Time Zone 설정과 관련된다.

Application 사용자의 PC 시각이라고 단정하면 안 된다.

---

# 24. CURRENT_TIMESTAMP

`NOW()`와 함께 자주 사용하는 표준적인 표현이 있다.

```sql
SELECT CURRENT_TIMESTAMP;
```

MariaDB에서 현재 날짜와 시간을 얻는 용도로 사용할 수 있다.

---

# 25. SYSDATE

원본:

```sql
SELECT SYSDATE();
```

`NOW()`처럼 현재 날짜와 시간을 반환한다.

하지만 두 함수는 세부 동작이 완전히 같지는 않다.

---

# 26. NOW와 SYSDATE 차이

MariaDB 기준:

```text
NOW()
→ Statement가 시작된 시각을 기준으로 일정한 값

SYSDATE()
→ 함수가 실제 실행되는 시각
```

긴 Statement나 지연이 있는 상황에서는 차이가 드러날 수 있다.

---

# 27. NOW와 SYSDATE를 같은 함수라고만 외우면 안 되는 이유

원본 Comment:

```text
now(), sysdate()는 현재 시간을 알 수 있음
```

입문 설명으로는 맞다.

하지만 V2에서는 다음처럼 구분한다.

```text
공통점
→ 현재 날짜·시간 반환

차이
→ 평가 시점 의미가 다름
```

---

# 28. DATE_FORMAT

원본:

```sql
SELECT DATE_FORMAT(
    NOW(),
    '%Y년 %m월 %d일 %H시 %i분 %s초'
);
```

날짜 값을 원하는 문자열 형식으로 표시한다.

---

# 29. DATE_FORMAT 주요 Format

| Format | 의미 |
| --- | --- |
| `%Y` | 4자리 Year |
| `%m` | 2자리 Month |
| `%d` | 2자리 Day |
| `%H` | 24시간 Hour |
| `%i` | Minute |
| `%s` | Second |

---

# 30. Minute은 `%m`이 아니다

자주 하는 실수:

```text
%m
→ Month

%i
→ Minute
```

원본 Format:

```sql
'%Y년 %m월 %d일 %H시 %i분 %s초'
```

은 이 차이를 잘 보여 준다.

---

# 31. DATE_FORMAT의 Result

```sql
SELECT DATE_FORMAT(
    '2026-08-13 09:05:07',
    '%Y-%m-%d %H:%i:%s'
);
```

`DATE_FORMAT()`은 **표시용 문자열 결과**를 만든다는 점이 중요하다.

---

# 32. 날짜는 가능한 날짜형으로 보관

실제 Table에 날짜를 저장할 때:

```text
2026년 08월 13일
```

같은 Display 문자열 자체를 저장하기보다 `DATE`, `DATETIME`, `TIMESTAMP` Type으로 보관하고 출력 시 Formatting하는 방식을 우선 고려한다.

---

# 33. STR_TO_DATE

원본:

```sql
SELECT STR_TO_DATE(
    '2026-08-07',
    '%Y-%m-%d'
);
```

문자열을 Format에 맞춰 날짜/시간 값으로 해석한다.

---

# 34. DATE_FORMAT과 STR_TO_DATE는 반대 방향

```text
DATE_FORMAT
날짜/시간 값
→ 문자열

STR_TO_DATE
문자열
→ 날짜/시간 값
```

---

# 35. STR_TO_DATE Format 일치

```sql
SELECT STR_TO_DATE(
    '2026/08/13',
    '%Y/%m/%d'
);
```

입력 문자열과 Format이 서로 대응해야 한다.

---

# 36. 잘못된 날짜 문자열

잘못된 날짜/시간 입력은 `NULL`, Warning 또는 SQL Mode에 따른 Error와 관련될 수 있다.

따라서 외부 문자열을 날짜로 변환할 때는 Input Validation도 고려한다.

---

# 37. DATE_FORMAT과 정렬

날짜를 먼저 문자열로 Formatting한 뒤 그 문자열 기준으로 정렬하면 Format에 따라 실제 시간 순서와 다르게 보일 수 있다.

날짜 순 정렬이 필요하면 원본 날짜 Column을 기준으로 정렬한다.

```sql
SELECT
    hiredate,
    DATE_FORMAT(hiredate, '%Y년 %m월 %d일') AS hire_text
FROM emp
ORDER BY hiredate;
```

---

# 38. NULL 처리 함수

원본:

```sql
SELECT
    IFNULL(comm, 0),
    comm
FROM emp;
```

```sql
SELECT
    COALESCE(comm, 0),
    comm
FROM emp;
```

NULL을 대체하는 대표 함수다.

---

# 39. IFNULL

구조:

```text
IFNULL(value, fallback)
```

첫 번째 값이 NULL이 아니면 그대로 반환하고, NULL이면 두 번째 값을 반환한다.

---

# 40. IFNULL 예제

```sql
SELECT
    ename,
    comm,
    IFNULL(comm, 0) AS safe_comm
FROM emp;
```

```text
COMM = 300
→ 300

COMM = NULL
→ 0
```

---

# 41. COALESCE

`COALESCE()`는 인수 목록에서 **첫 번째 NULL이 아닌 값**을 반환한다.

```sql
SELECT COALESCE(NULL, NULL, 100, 200);
```

Result:

```text
100
```

---

# 42. COALESCE 두 인수

```sql
SELECT COALESCE(comm, 0)
FROM emp;
```

인수가 두 개일 때는 `IFNULL(comm, 0)`과 같은 목적의 결과를 만들 수 있다.

---

# 43. IFNULL과 COALESCE 차이

```text
IFNULL(a, b)
→ 두 인수
→ a가 NULL이면 b

COALESCE(a, b, c, ...)
→ 여러 후보
→ 첫 번째 non-NULL
```

여러 fallback 후보가 필요하면 `COALESCE()`가 더 자연스럽다.

---

# 44. COALESCE 활용 예

```sql
SELECT COALESCE(
    nickname,
    display_name,
    username,
    'unknown'
)
FROM member;
```

앞의 값부터 확인해 처음 존재하는 값을 반환하는 방식이다.

---

# 45. NULL 산술 원본

원본:

```sql
SELECT
    sal * 12 + comm
FROM emp;
```

`COMM`이 `NULL`이면 전체 산술 Result도 `NULL`이 된다.

---

# 46. NULL 대체 후 산술

원본:

```sql
SELECT
    sal * 12 + IFNULL(comm, 0)
FROM emp;
```

`COMM`이 NULL인 경우 계산용으로 0을 사용한다.

---

# 47. NULL을 0으로 바꾸는 것은 Business Rule

다음 두 상태는 다를 수 있다.

```text
COMM = NULL
→ 값 없음 / 알 수 없음

COMM = 0
→ 값이 실제로 0
```

따라서 `IFNULL(comm, 0)`을 사용할 때 “업무적으로 NULL을 0으로 간주해도 되는가?”를 확인한다.

---

# 48. IFNULL은 Data를 수정하지 않는다

```sql
SELECT IFNULL(comm, 0)
FROM emp;
```

Table의 실제 `COMM` 값을 0으로 UPDATE하는 것이 아니다.

Query Result에서 대체된 값을 반환한다.

---

# 49. NULL 처리와 집계함수

05번과 연결:

```sql
SELECT AVG(comm)
FROM emp;
```

```text
NULL
→ 평균 계산에서 제외
```

반면:

```sql
SELECT AVG(IFNULL(comm, 0))
FROM emp;
```

```text
NULL
→ 0으로 변환
→ 평균 계산에 포함
```

Result 의미가 달라질 수 있다.

---

# 50. NULL 처리와 문자열 결합

07번과 연결:

```sql
SELECT CONCAT(
    ename,
    ' / ',
    IFNULL(comm, 0)
)
FROM emp;
```

NULL 때문에 전체 `CONCAT` Result가 NULL이 되는 상황을 피할 수 있다.

---

# 51. 내 코드와 강사님 코드 비교

두 원본은 다음 순서가 거의 동일하다.

```text
ROUND
→ CEIL
→ FLOOR
→ TRUNCATE
→ MOD
→ NOW / SYSDATE
→ DATE_FORMAT
→ STR_TO_DATE
→ IFNULL / COALESCE
→ NULL 포함 산술 비교
```

내 코드에는 함수별 의미 Comment가 더 자세하고, 강사님 코드는 간결한 대표 Query 중심이다.

---

## 51.1 ROUND

내 코드:

```text
round는 반올림 할 수 있음,
','를 사용해서 소수점 범위도 지정
```

강사님:

```text
반올림
```

V2에서는 두 번째 인수가 남길 자릿수라는 의미까지 명확히 정리한다.

---

## 51.2 CEIL / FLOOR

두 원본 모두:

```sql
SELECT CEIL(3.14);
SELECT CEIL(-3.14);

SELECT FLOOR(3.14);
SELECT FLOOR(-3.14);
```

양수와 음수를 함께 실험한 것이 중요하다.

V2에서는 음수에서 `CEIL=-3`, `FLOOR=-4`가 되는 이유를 수직선 기준으로 설명한다.

---

## 51.3 TRUNCATE 차이

내 코드:

```sql
SELECT TRUNCATE(-3.14, 0);
```

강사님 코드:

```sql
SELECT TRUNCATE(-3.14, 1);
```

둘 다 올바른 예제이며 확인하는 자릿수만 다르다.

```text
0
→ 소수점 이하 모두 절삭

1
→ 소수점 이하 1자리 유지
```

---

## 51.4 MOD

두 코드 모두:

```sql
SELECT MOD(10, 3);
```

나머지 `1`을 확인하는 기본 예제다.

---

## 51.5 NOW / SYSDATE

두 코드 모두 두 함수를 연속으로 실행한다.

```sql
SELECT NOW();
SELECT SYSDATE();
```

원본은 둘을 “현재 시간”으로 묶어 소개한다.

V2에서는 Statement 시작 시각 기준인 `NOW()`와 실제 함수 실행 시각인 `SYSDATE()`의 세부 차이까지 보완한다.

---

## 51.6 DATE_FORMAT

두 코드 모두:

```sql
SELECT DATE_FORMAT(
    NOW(),
    '%Y년 %m월 %d일 %H시 %i분 %s초'
);
```

같은 Format을 사용한다.

---

## 51.7 STR_TO_DATE

두 코드 모두:

```sql
SELECT STR_TO_DATE(
    '2026-08-07',
    '%Y-%m-%d'
);
```

문자열을 날짜형으로 해석하는 반대 방향 변환을 학습한다.

---

## 51.8 IFNULL / COALESCE

두 코드 모두:

```sql
SELECT IFNULL(comm, 0), comm
FROM emp;

SELECT COALESCE(comm, 0), comm
FROM emp;
```

원본에서는 거의 같은 결과를 비교한다.

V2에서는:

```text
IFNULL
→ 두 값

COALESCE
→ 여러 후보 중 첫 non-NULL
```

로 범용성 차이를 추가한다.

---

## 51.9 NULL 산술

두 코드 모두:

```sql
SELECT sal * 12 + comm
FROM emp;

SELECT sal * 12 + IFNULL(comm, 0)
FROM emp;
```

NULL이 산술 전체를 NULL로 만드는 경우와 대체값을 사용한 경우를 직접 비교한다.

---

## 51.10 원본 비교 요약

| 항목 | 내 코드 | 강사님 코드 | V2 정리 |
| --- | --- | --- | --- |
| ROUND | 상세 Comment | 기본 | 반올림·자릿수 |
| CEIL | 양수/음수 | 동일 | 입력 이상 최소 정수 |
| FLOOR | 양수/음수 | 동일 | 입력 이하 최대 정수 |
| TRUNCATE | `-3.14, 0` | `-3.14, 1` | 둘 다 기록 |
| MOD | 있음 | 있음 | 나머지 |
| NOW | 서버시간 Comment | 현재 시간 | Statement 시작 기준 |
| SYSDATE | NOW와 함께 설명 | 현재 시간 | 실제 실행 시각 |
| DATE_FORMAT | Format 설명 | 기본 | Date → String |
| STR_TO_DATE | String→Date 설명 | 기본 | String → Date/Time |
| IFNULL | NULL→기본값 | 기본 | 두 인수 |
| COALESCE | IFNULL과 비교 | 기본 | 첫 non-NULL |
| NULL 산술 | 상세 | 동일 | Business Rule 보완 |

---

# 52. 개선된 통합 예제

```sql
-- 숫자 함수 비교
SELECT
    ROUND(3.146, 2) AS rounded,
    CEIL(-3.14) AS ceiled,
    FLOOR(-3.14) AS floored,
    TRUNCATE(-3.14, 1) AS truncated,
    MOD(10, 3) AS remainder;

-- 현재 시간과 Formatting
SELECT
    NOW() AS current_datetime,
    DATE_FORMAT(
        NOW(),
        '%Y-%m-%d %H:%i:%s'
    ) AS formatted_datetime;

-- 문자열을 날짜로 변환
SELECT STR_TO_DATE(
    '2026-08-13',
    '%Y-%m-%d'
) AS parsed_date;

-- NULL 처리
SELECT
    ename,
    sal,
    comm,
    IFNULL(comm, 0) AS safe_comm,
    sal * 12 + IFNULL(comm, 0) AS calculated_value
FROM emp;
```

---

# 53. 실무 함수 선택 기준

```text
반올림
→ ROUND

위쪽 정수
→ CEIL

아래쪽 정수
→ FLOOR

자릿수 절삭
→ TRUNCATE

나머지
→ MOD
```

```text
현재 날짜·시간
→ NOW / CURRENT_TIMESTAMP

표시 문자열
→ DATE_FORMAT

문자열 Parsing
→ STR_TO_DATE
```

```text
NULL 대체 후보 1개
→ IFNULL

여러 후보 중 첫 값
→ COALESCE
```

---

# 54. 숫자 함수 리팩토링

요구사항이 “소수점 2자리 반올림”이라면:

```sql
ROUND(value, 2)
```

요구사항이 “소수점 2자리까지만 남기고 절삭”이라면:

```sql
TRUNCATE(value, 2)
```

함수 이름이 비슷하다고 바꿔 쓰지 않는다.

---

# 55. 날짜 Formatting 리팩토링

## Before

날짜 Column을 문자열처럼 직접 가공해 저장하거나 비교한다.

## After

```sql
SELECT
    hiredate,
    DATE_FORMAT(
        hiredate,
        '%Y-%m-%d'
    ) AS hiredate_text
FROM emp
ORDER BY hiredate;
```

Date Type은 Date Type으로 유지하고 표시할 때 Formatting한다.

---

# 56. NULL 처리 리팩토링

## Before

```sql
SELECT
    sal * 12 + comm
FROM emp;
```

NULL 때문에 계산 결과가 사라질 수 있다.

## After

업무상 NULL을 0으로 계산하는 것이 맞다면:

```sql
SELECT
    sal * 12 + IFNULL(comm, 0)
FROM emp;
```

---

# 57. 자주 하는 실수

- `CEIL(-3.14)`을 `-4`라고 생각한다.
- `FLOOR(-3.14)`을 `-3`이라고 생각한다.
- `TRUNCATE`를 반올림 함수라고 생각한다.
- `TRUNCATE`의 두 번째 인수를 생략한다.
- `NOW()`와 `SYSDATE()`를 내부 의미까지 완전히 같은 함수라고 생각한다.
- `%m`을 Minute로 착각한다.
- `DATE_FORMAT()` 결과를 Date Type 그대로라고 생각한다.
- `STR_TO_DATE()`의 Format과 입력 문자열 형태를 맞추지 않는다.
- `IFNULL()`이 실제 Table의 NULL 값을 수정한다고 생각한다.
- `COALESCE()`가 두 인수만 받을 수 있다고 생각한다.
- NULL을 무조건 0으로 바꾸는 것이 안전하다고 생각한다.

---

# 58. Debugging

```text
1. ROUND와 TRUNCATE 중 요구사항에 맞는가?
2. CEIL/FLOOR 음수 결과를 반대로 생각하지 않았는가?
3. TRUNCATE 두 번째 자릿수 값이 맞는가?
4. 날짜 Format의 %m과 %i를 구분했는가?
5. 입력 문자열과 STR_TO_DATE Format이 일치하는가?
6. NOW 결과의 Time Zone을 확인했는가?
7. NOW와 SYSDATE의 평가 시점 차이가 중요한 상황인가?
8. NULL 대체가 실제 Business Rule과 맞는가?
9. IFNULL과 COALESCE 중 의도에 맞는 함수를 선택했는가?
10. NULL 대체 전후 Aggregate 의미가 바뀌지 않는가?
```

---

# 59. 종합실습

## 문제 1

`3.146`을 소수점 이하 2자리로 반올림하시오.

## 문제 2

`-3.14`에 `CEIL`, `FLOOR`, `TRUNCATE(..., 0)`를 각각 적용해 비교하시오.

## 문제 3

10을 3으로 나눈 나머지를 구하시오.

## 문제 4

현재 날짜와 시간을 조회하시오.

## 문제 5

현재 날짜와 시간을 다음 형태로 출력하시오.

```text
2026-08-13 10:30:15
```

## 문제 6

문자열 `'2026/08/13'`을 Date 값으로 변환하시오.

## 문제 7

EMP의 `COMM`이 NULL이면 0으로 표시하시오.

## 문제 8

`COALESCE(NULL, NULL, 300, 400)`의 Result와 이유를 설명하시오.

## 문제 9

`sal * 12 + comm`과 `sal * 12 + IFNULL(comm, 0)`의 차이를 설명하시오.

---

# 60. 정답과 해설

## 문제 1

```sql
SELECT ROUND(3.146, 2);
```

---

## 문제 2

```sql
SELECT
    CEIL(-3.14) AS ceil_value,
    FLOOR(-3.14) AS floor_value,
    TRUNCATE(-3.14, 0) AS truncate_value;
```

개념 결과:

```text
CEIL
→ -3

FLOOR
→ -4

TRUNCATE
→ -3
```

---

## 문제 3

```sql
SELECT MOD(10, 3);
```

---

## 문제 4

```sql
SELECT NOW();
```

---

## 문제 5

```sql
SELECT DATE_FORMAT(
    NOW(),
    '%Y-%m-%d %H:%i:%s'
);
```

---

## 문제 6

```sql
SELECT STR_TO_DATE(
    '2026/08/13',
    '%Y/%m/%d'
);
```

---

## 문제 7

```sql
SELECT
    ename,
    comm,
    IFNULL(comm, 0) AS safe_comm
FROM emp;
```

---

## 문제 8

```sql
SELECT COALESCE(
    NULL,
    NULL,
    300,
    400
);
```

첫 번째 NULL이 아닌 값 `300`을 반환한다.

---

## 문제 9

첫 번째 Query는 `COMM`이 NULL이면 전체 산술 결과도 NULL이 된다.

두 번째 Query는 `COMM`이 NULL일 때 계산용 0으로 대체한다.

단, NULL을 0으로 간주하는 것이 실제 업무 의미와 맞아야 한다.

---

# 61. 최종 체크리스트

- [ ] `ROUND()`를 사용할 수 있는가?
- [ ] `ROUND(value, digits)`의 자릿수를 설명할 수 있는가?
- [ ] `CEIL()`의 의미를 설명할 수 있는가?
- [ ] `FLOOR()`의 의미를 설명할 수 있는가?
- [ ] 음수에서 CEIL/FLOOR 결과를 정확히 예측할 수 있는가?
- [ ] `TRUNCATE()`와 `ROUND()`를 구분할 수 있는가?
- [ ] `TRUNCATE()`의 두 번째 인수가 필수임을 아는가?
- [ ] `MOD()`로 나머지를 구할 수 있는가?
- [ ] `NOW()`로 현재 날짜·시간을 조회할 수 있는가?
- [ ] `NOW()`와 `SYSDATE()`의 평가 시점 차이를 이해하는가?
- [ ] `DATE_FORMAT()`을 사용할 수 있는가?
- [ ] `%m` Month와 `%i` Minute를 구분할 수 있는가?
- [ ] `STR_TO_DATE()`를 사용할 수 있는가?
- [ ] `DATE_FORMAT`과 `STR_TO_DATE`의 변환 방향을 구분하는가?
- [ ] `IFNULL()`을 사용할 수 있는가?
- [ ] `COALESCE()`가 첫 번째 non-NULL 값을 반환함을 아는가?
- [ ] `IFNULL`과 `COALESCE`의 차이를 설명할 수 있는가?
- [ ] NULL이 포함된 산술 결과를 이해하는가?
- [ ] NULL→0 대체가 Business Rule을 바꿀 수 있음을 고려하는가?
- [ ] 함수 적용 결과가 원본 Data를 자동 수정하지 않음을 이해하는가?

---

# 62. 핵심 요약

```text
ROUND
→ 반올림

CEIL
→ 입력값 이상인 최소 정수

FLOOR
→ 입력값 이하인 최대 정수

TRUNCATE
→ 지정 자릿수 이후 절삭

MOD
→ 나머지
```

```text
NOW
→ 현재 날짜·시간
→ Statement 시작 시각 기준

SYSDATE
→ 현재 날짜·시간
→ 함수 실행 시각 기준
```

```text
DATE_FORMAT
→ Date/Time → String

STR_TO_DATE
→ String → Date/Time
```

```text
IFNULL(a, b)
→ a가 NULL이면 b

COALESCE(a, b, c...)
→ 첫 번째 non-NULL 값
```

```text
NULL 포함 산술
→ NULL

IFNULL로 대체
→ 계산 가능
→ 단, Business Rule 확인
```

---

# 마무리

08번의 함수들은 서로 다른 영역처럼 보이지만 공통점이 있다.

```text
입력값 확인
    ↓
함수의 정확한 변환 규칙 확인
    ↓
반환 Type과 의미 확인
    ↓
NULL과 경계값 확인
    ↓
업무 요구사항에 맞는 함수 선택
```

숫자에서는 **반올림과 절삭**, 날짜에서는 **값과 표시 문자열**, NULL에서는 **값 없음과 실제 0**을 정확히 구분하는 것이 핵심이다.

다음 단원에서는 이러한 함수 결과와 조건식을 결합해 `CASE`로 Row마다 다른 값을 반환하는 방법을 학습한다.
# V3 동작 백과 — 숫자·날짜·NULL 값은 어떻게 바뀌는가?

## 숫자 함수의 실제 차이

```sql
SELECT
    ROUND(3.56, 1) AS rounded,
    TRUNCATE(3.56, 1) AS truncated,
    CEIL(-3.14) AS ceiled,
    FLOOR(-3.14) AS floored;
```

```text
ROUND(3.56, 1)    → 3.6  반올림
TRUNCATE(3.56, 1) → 3.5  잘라냄
CEIL(-3.14)       → -3   더 큰 정수 방향
FLOOR(-3.14)      → -4   더 작은 정수 방향
```

음수에서 CEIL과 FLOOR를 단순히 “절댓값 올림·내림”으로 이해하면 틀린다. 수직선 방향으로 판단한다.

## 날짜값은 어디서 오는가?

```sql
SELECT NOW(), CURRENT_TIMESTAMP;
```

값은 사용자 PC 화면 시간이 아니라 MariaDB Server와 Session의 시간 설정을 기준으로 만들어진다. 같은 Query 안에서 `NOW()`는 일반적으로 일관된 기준 시각을 제공한다.

```sql
SELECT DATE_FORMAT(NOW(), '%Y-%m-%d %H:%i:%s');
```

```text
2026-08-26 14:30:05
```

`%m`은 Month, `%i`는 Minute다.

## NULL 대체가 계산을 바꾸는 과정

```sql
SELECT sal, comm, sal + IFNULL(comm, 0) AS total_pay
FROM emp;
```

```text
COMM=300  → IFNULL=300 → SAL+300
COMM=NULL → IFNULL=0   → SAL+0
```

대체값 0이 업무적으로 “수당 없음”을 의미할 때만 사용한다.

## 수업 원본에서 다시 찾기

| 개념 | 내 코드 검색 Anchor | 강사님 코드 검색 Anchor |
| --- | --- | --- |
| 반올림 | `select round(3.14)` | 같은 Query |
| 올림·내림 | `ceil(`, `floor(` | 같은 함수 구간 |
| 자르기 | `truncate(` | `truncate(` |
| 현재 시각 | `now()` | 날짜 함수 구간 |
| Format | `date_format(` | `date_format(` |
| 문자열→날짜 | `str_to_date(` | 같은 함수 구간 |
| NULL 대체 | `ifnull(`, `coalesce(` | NULL 함수 구간 |

함수 결과의 Type, Server 시간대, NULL 대체 전후를 Result Grid에서 함께 확인한다.
