---
title: SQL 문자열 함수
version: v3.0-final
last_updated: 2026-08-13
status: Completed
---

# SQL 문자열 함수

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `07_SQL_문자열함수.md` |
| 분류 | `05_SQL` |
| 원본 기준 | `workspace_sql/Script.sql`, `workspace_teacher/workspace_sql/Script.sql` |
| DB 기준 자료 | `[DB]학습용_emp 신규-mariadb.sql` |
| DBMS | MariaDB |
| 핵심 범위 | `LOWER`, `UPPER`, `LENGTH`, `CHAR_LENGTH`, `SUBSTRING`, `SUBSTR`, `REPLACE`, `LPAD`, `RPAD`, `TRIM`, `CONCAT`, `CONCAT_WS` |
| 학습 범위 | 문자열 길이, 대소문자 변환, 부분 문자열, 치환, Padding, 공백 제거, 문자열 결합 |
| 다음 범위 제외 | 숫자 함수, 날짜 함수, NULL 함수, `CASE` |
| 문서 형식 | SQL Developer-Wiki V3 백과사전 형식 |

> 이 문서는 내 코드와 강사님 코드의 `Script.sql` 문자열 함수 구간을 비교해 정리한다.  
> 원본의 `LENGTH`를 단순히 “글자 수”라고 설명한 부분을 보완해 **Byte 길이와 Character 길이의 차이**를 구분하고, `SUBSTRING`의 1-based 위치, `LPAD/RPAD`의 잘림 동작, `CONCAT`과 `NULL`, Oracle의 `||`와 MariaDB의 차이까지 실무 관점으로 연결한다.

---

# 학습 목표

- `LOWER`, `UPPER`로 문자열 Case를 변환할 수 있다.
- `LENGTH`와 `CHAR_LENGTH`의 차이를 설명할 수 있다.
- `SUBSTRING`, `SUBSTR`로 문자열 일부를 추출할 수 있다.
- MariaDB 문자열 위치가 기본적으로 1부터 시작한다는 점을 이해할 수 있다.
- `REPLACE`로 모든 일치 문자열을 치환할 수 있다.
- `LPAD`, `RPAD`로 목표 길이에 맞춰 문자열을 채울 수 있다.
- 목표 길이가 원본보다 짧을 때 문자열이 잘릴 수 있음을 이해할 수 있다.
- `TRIM`으로 양쪽 공백을 제거할 수 있다.
- `CONCAT`, `CONCAT_WS`로 여러 값을 결합할 수 있다.
- 문자열 함수와 `NULL`, Character Set, Collation의 관계를 고려할 수 있다.

---

# 1. 문자열 함수란?

문자열 함수는 문자열 값을 변환하거나 분석해 새로운 값을 반환한다.

```text
LOWER / UPPER
→ 대소문자 변환

LENGTH / CHAR_LENGTH
→ 길이 확인

SUBSTRING
→ 일부 추출

REPLACE
→ 문자열 치환

LPAD / RPAD
→ 길이 맞추기

TRIM
→ 양쪽 공백 제거

CONCAT
→ 문자열 결합
```

원본 Column 자체가 자동으로 변경되는 것은 아니다.

---

# 2. 함수는 Result를 만든다

```sql
SELECT
    ename,
    LOWER(ename)
FROM emp;
```

`ENAME` 값을 변경해 저장하는 것이 아니라 Query Result에서 변환된 값을 반환한다.

---

# 3. LOWER

문자열을 소문자로 변환한다.

```sql
SELECT LOWER('Human');
```

Result:

```text
human
```

---

# 4. UPPER

문자열을 대문자로 변환한다.

```sql
SELECT UPPER('Human');
```

Result:

```text
HUMAN
```

---

# 5. Column에 LOWER 적용

```sql
SELECT
    ename,
    LOWER(ename) AS lower_name
FROM emp;
```

---

# 6. Column에 UPPER 적용

```sql
SELECT
    ename,
    UPPER(ename) AS upper_name
FROM emp;
```

---

# 7. LIKE와 LOWER/UPPER

원본에는 다음 실험이 있다.

```sql
SELECT *
FROM emp
WHERE UPPER(ename) LIKE UPPER('%Am%');
```

```sql
SELECT *
FROM emp
WHERE LOWER(ename) LIKE LOWER('%Am%');
```

검색값과 Column을 같은 Case로 변환하는 방식이다.

---

# 8. Case 변환과 Collation

MariaDB에서 Case Sensitivity는 Collation에도 영향을 받는다.

따라서:

```sql
WHERE UPPER(ename) LIKE UPPER('%Am%')
```

이 항상 필요한 것은 아니다.

Case-insensitive Collation에서는 기본 비교만으로도 같은 결과가 나올 수 있다.

---

# 9. 함수 적용과 Index

다음처럼 Indexed Column에 함수를 직접 적용하면 일반 Index 활용이 제한될 수 있다.

```sql
WHERE UPPER(ename) = 'SMITH'
```

성능이 중요한 Query는 Collation, Functional Index 지원 여부, 실행계획 등을 확인한다.

---

# 10. LENGTH

원본:

```sql
SELECT
    LENGTH(ename),
    ename
FROM emp;
```

`LENGTH()`는 MariaDB에서 문자열의 **Byte 길이**를 반환한다.

---

# 11. LENGTH를 “글자 수”라고만 하면 안 되는 이유

영문 ASCII 문자열에서는:

```sql
SELECT LENGTH('SMITH');
```

결과:

```text
5
```

영문 1 Character가 일반적으로 1 Byte이므로 글자 수처럼 보인다.

하지만 한글에서는 다를 수 있다.

---

# 12. 한글 LENGTH

UTF-8 계열 Character Set이라면:

```sql
SELECT LENGTH('가나다');
```

Character 수는 3이지만 Byte 수는 더 클 수 있다.

따라서 `LENGTH = 글자 수`라고 일반화하면 부정확하다.

---

# 13. CHAR_LENGTH

Character 개수를 구하려면:

```sql
SELECT CHAR_LENGTH('가나다');
```

Result:

```text
3
```

---

# 14. LENGTH vs CHAR_LENGTH

```sql
SELECT
    LENGTH('가나다') AS byte_length,
    CHAR_LENGTH('가나다') AS char_length;
```

```text
LENGTH
→ Byte 길이

CHAR_LENGTH
→ Character 개수
```

---

# 15. CHARACTER_LENGTH

`CHAR_LENGTH()`의 동의 함수로 `CHARACTER_LENGTH()`도 사용할 수 있다.

```sql
SELECT CHARACTER_LENGTH('Human');
```

---

# 16. LENGTH 조건

원본:

```sql
SELECT *
FROM emp
WHERE LENGTH(ename) = 4;
```

현재 EMP 이름이 영문 중심이라 Character 수 조건처럼 동작한다.

---

# 17. 사용자 이름 길이는 CHAR_LENGTH 검토

다국어 이름을 실제 Character 수로 제한한다면:

```sql
SELECT *
FROM member
WHERE CHAR_LENGTH(name) = 4;
```

처럼 의미에 맞는 함수를 선택한다.

---

# 18. SUBSTRING

원본:

```sql
SELECT
    SUBSTRING(ename, 2, 3),
    ename
FROM emp;
```

구조:

```text
SUBSTRING(문자열, 시작위치, 길이)
```

---

# 19. MariaDB 문자열 위치는 1부터

```sql
SELECT SUBSTRING('SMITH', 1, 2);
```

Result:

```text
SM
```

JavaScript나 Python의 Index 0과 혼동하지 않는다.

---

# 20. SUBSTRING 두 번째 위치부터

```sql
SELECT SUBSTRING('SMITH', 2, 3);
```

Result:

```text
MIT
```

---

# 21. SUBSTR

원본에는 다음도 있다.

```sql
SELECT
    SUBSTR(ename, 2, 3),
    ename
FROM emp;
```

MariaDB에서 `SUBSTR()`은 `SUBSTRING()`의 동의 함수로 사용할 수 있다.

---

# 22. SUBSTRING을 권장하는 이유

두 함수가 같은 동작을 하더라도:

```sql
SUBSTRING(...)
```

이 이름만 보아도 “부분 문자열”이라는 목적을 이해하기 쉽다.

팀 Coding Convention에 맞춰 일관되게 사용한다.

---

# 23. 앞 두 글자 추출

원본 문제:

```sql
SELECT SUBSTRING(ename, 1, 2)
FROM emp;
```

이름의 앞 두 Character를 반환한다.

---

# 24. 시작 위치만 지정

```sql
SELECT SUBSTRING('SMITH', 3);
```

세 번째 Character부터 끝까지 반환할 수 있다.

---

# 25. 음수 위치

MariaDB에서는 음수 위치를 이용해 뒤에서부터 위치를 계산할 수 있다.

```sql
SELECT SUBSTRING('SMITH', -2);
```

Result:

```text
TH
```

기본 학습에서는 양수 위치부터 확실히 익힌다.

---

# 26. REPLACE

원본:

```sql
SELECT
    REPLACE(ename, 'A', '에이'),
    ename
FROM emp;
```

구조:

```text
REPLACE(문자열, 찾을문자열, 바꿀문자열)
```

---

# 27. REPLACE는 일치 항목을 치환

```sql
SELECT REPLACE('BANANA', 'A', '*');
```

Result:

```text
B*N*N*
```

문자열 안의 해당 일치 항목들을 치환한다.

---

# 28. REPLACE는 원본 Data를 UPDATE하지 않는다

```sql
SELECT REPLACE(ename, 'A', '에이')
FROM emp;
```

Result에서만 변환된다.

실제 Table 값을 변경하려면 `UPDATE`가 필요하다.

---

# 29. REPLACE와 Case

찾을 문자열의 Matching도 Character Set/Collation과 함수 특성을 구분해서 확인해야 한다.

실제 결과가 중요한 경우 Sample Data로 직접 검증한다.

---

# 30. LPAD

왼쪽에 문자열을 채워 목표 길이에 맞춘다.

```sql
SELECT
    LPAD(ename, 10, '#'),
    ename
FROM emp;
```

예:

```text
SMITH
→ #####SMITH
```

---

# 31. LPAD 구조

```text
LPAD(문자열, 목표길이, 채울문자열)
```

---

# 32. 목표 길이가 더 짧으면?

원본:

```sql
SELECT LPAD(ename, 3, '#')
FROM emp;
```

원본 문자열이 3보다 길다면 단순히 Padding을 하지 않는 것이 아니라 **목표 길이에 맞게 잘릴 수 있다.**

예:

```sql
SELECT LPAD('SMITH', 3, '#');
```

Result:

```text
SMI
```

---

# 33. RPAD

오른쪽에 문자열을 채운다.

```sql
SELECT RPAD(ename, 10, '#')
FROM emp;
```

예:

```text
SMITH#####
```

---

# 34. 숫자에 LPAD

원본:

```sql
SELECT
    LPAD(sal, 10, '0'),
    ename
FROM emp;
```

문자열 함수에 숫자를 전달하면 MariaDB의 Type Conversion이 개입할 수 있다.

표시 Format 목적이라면 결과가 문자열이라는 점을 이해한다.

---

# 35. 공백 Padding

```sql
SELECT LPAD(ename, 10, ' ')
FROM emp;
```

고정 폭 Text처럼 보이게 만들 수 있지만 Web UI나 Report Layout은 Application/CSS 계층에서 처리하는 것이 더 적절한 경우도 많다.

---

# 36. 이름 마스킹 문제

강사님 원본:

```sql
SELECT
    RPAD(
        SUBSTRING(ename, 1, 2),
        6,
        '*'
    )
FROM emp;
```

앞 두 글자를 남기고 전체 길이를 6으로 맞춘다.

---

# 37. 원래 이름 길이에 맞춘 마스킹

원본 개선 문제:

```sql
SELECT
    RPAD(
        SUBSTRING(ename, 1, 2),
        LENGTH(ename),
        '*'
    )
FROM emp;
```

```text
WARD
→ WA**

SMITH
→ SM***
```

영문 EMP Data에서는 잘 동작한다.

---

# 38. 다국어 마스킹이라면 CHAR_LENGTH

다국어 문자열이라면 Character 수 기준으로:

```sql
SELECT
    RPAD(
        SUBSTRING(name, 1, 2),
        CHAR_LENGTH(name),
        '*'
    )
FROM member;
```

를 검토한다.

---

# 39. TRIM

원본:

```sql
SELECT TRIM('  a b  c  ');
```

기본 `TRIM()`은 문자열 양 끝의 Space를 제거한다.

Result:

```text
a b  c
```

---

# 40. TRIM은 내부 공백을 제거하지 않는다

```text
'  a b  c  '
→ 'a b  c'
```

문자열 중간 공백은 유지된다.

---

# 41. LTRIM과 RTRIM

왼쪽만:

```sql
SELECT LTRIM('   Human   ');
```

오른쪽만:

```sql
SELECT RTRIM('   Human   ');
```

---

# 42. CONCAT

원본:

```sql
SELECT CONCAT(ename, job)
FROM emp;
```

여러 문자열을 하나로 연결한다.

---

# 43. 구분자를 직접 넣는 CONCAT

```sql
SELECT CONCAT(ename, ' ', job)
FROM emp;
```

예:

```text
SMITH CLERK
```

---

# 44. CONCAT과 NULL

MariaDB에서 `CONCAT()` 인수 중 `NULL`이 포함되면 전체 Result가 `NULL`이 될 수 있다.

```sql
SELECT CONCAT('A', NULL, 'B');
```

NULL을 빈 문자열처럼 자동 취급한다고 생각하면 안 된다.

---

# 45. CONCAT에서 NULL 처리

업무상 NULL을 빈 문자열로 처리해야 한다면:

```sql
SELECT CONCAT(
    ename,
    ' ',
    IFNULL(job, '')
)
FROM emp;
```

실제 의미가 맞는지 확인한 뒤 사용한다.

---

# 46. CONCAT_WS

원본:

```sql
SELECT CONCAT_WS('-', ename, job, empno)
FROM emp;
```

`WS`는 **With Separator** 의미다.

---

# 47. CONCAT_WS 구조

```text
CONCAT_WS(구분자, 값1, 값2, 값3 ...)
```

예:

```sql
SELECT CONCAT_WS('-', 'A', 'B', 'C');
```

Result:

```text
A-B-C
```

---

# 48. CONCAT_WS와 NULL

`CONCAT_WS()`는 Separator 뒤의 `NULL` 인수를 건너뛸 수 있다.

```sql
SELECT CONCAT_WS('-', 'A', NULL, 'C');
```

Result:

```text
A-C
```

단, Separator 자체가 `NULL`이면 Result도 `NULL`이 될 수 있다.

---

# 49. Oracle의 `||`와 MariaDB

원본 Comment:

```text
Oracle에서는 ename || job으로 합치기 사용 가능
```

Oracle에서는 `||`가 문자열 결합 Operator다.

MariaDB에서는 기본 SQL Mode에서 `||`를 같은 의미로 가정하면 안 된다.

```sql
SELECT CONCAT(ename, job)
FROM emp;
```

MariaDB에서는 `CONCAT()`을 사용하는 것이 명확하다.

---

# 50. 내 코드와 강사님 코드 비교

두 원본의 문자열 함수 구간은 거의 같은 순서다.

```text
LENGTH
→ SUBSTRING / SUBSTR
→ REPLACE
→ LPAD / RPAD
→ TRIM
→ CONCAT / CONCAT_WS
```

내 코드에는 각 함수의 Argument 의미와 추가 Comment가 더 많고, 강사님 코드는 핵심 Query와 마스킹 문제까지 이어진다.

| 항목 | 내 코드 | 강사님 코드 | V2 정리 |
| --- | --- | --- | --- |
| LOWER/UPPER | LIKE 앞에서 추가 실습 | 유사 흐름 | Case 변환 |
| LENGTH | “길이” 설명 | 기본 Query | Byte 길이 |
| CHAR_LENGTH | 후반 추가 학습 | 초기 구간 없음 | Character 수 |
| SUBSTRING | 시작·개수 설명 | 동일 | 1-based |
| SUBSTR | 있음 | 있음 | SUBSTRING 동의 함수 |
| REPLACE | “전부 바꿈” 설명 | 동일 | 일치 문자열 치환 |
| LPAD | 자릿수·잘림 설명 | 기본 | 목표 길이보다 길면 잘림 |
| RPAD | 있음 | 있음 | 오른쪽 Padding |
| TRIM | 양쪽 공백 설명 | 동일 | 내부 공백 유지 |
| CONCAT | 상세 Comment | 기본 | NULL 주의 |
| CONCAT_WS | Separator 설명 | 기본 | NULL 인수 처리 차이 |
| 마스킹 | 일부 확장 | 문제 2개 | LENGTH/CHAR_LENGTH 연결 |
| Oracle `||` | Comment 있음 | Comment 있음 | MariaDB와 구분 |

---

# 51. 개선된 통합 예제

```sql
-- 이름 Case
SELECT
    ename,
    LOWER(ename) AS lower_name,
    UPPER(ename) AS upper_name
FROM emp;

-- Byte / Character 길이
SELECT
    ename,
    LENGTH(ename) AS byte_length,
    CHAR_LENGTH(ename) AS char_length
FROM emp;

-- 앞 두 Character
SELECT
    ename,
    SUBSTRING(ename, 1, 2) AS prefix
FROM emp;

-- 이름 마스킹
SELECT
    ename,
    RPAD(
        SUBSTRING(ename, 1, 2),
        CHAR_LENGTH(ename),
        '*'
    ) AS masked_name
FROM emp;

-- 문자열 결합
SELECT
    CONCAT_WS(
        ' / ',
        ename,
        job,
        deptno
    ) AS employee_info
FROM emp;
```

---

# 52. 실무 문자열 함수 기준

```text
Case 변환
→ LOWER / UPPER

Byte 크기
→ LENGTH

사용자가 인식하는 Character 수
→ CHAR_LENGTH

일부 추출
→ SUBSTRING

치환
→ REPLACE

고정 길이 표현
→ LPAD / RPAD

양 끝 공백 제거
→ TRIM

값 연결
→ CONCAT

구분자 포함 연결
→ CONCAT_WS
```

---

# 53. LENGTH 리팩토링

## Before

```sql
WHERE LENGTH(name) = 4
```

다국어 사용자 이름의 “4글자”가 요구사항이라면:

## After

```sql
WHERE CHAR_LENGTH(name) = 4
```

Byte와 Character 의미를 구분한다.

---

# 54. 마스킹 리팩토링

## Before

```sql
RPAD(
    SUBSTRING(ename, 1, 2),
    6,
    '*'
)
```

무조건 길이 6으로 만든다.

## After

```sql
RPAD(
    SUBSTRING(ename, 1, 2),
    CHAR_LENGTH(ename),
    '*'
)
```

원본 Character 길이에 맞춘다.

---

# 55. CONCAT 리팩토링

## Before

```sql
SELECT CONCAT(ename, job, deptno)
FROM emp;
```

값 경계가 불명확하다.

## After

```sql
SELECT CONCAT_WS(
    ' / ',
    ename,
    job,
    deptno
)
FROM emp;
```

구분자가 있어 읽기 쉽다.

---

# 56. 자주 하는 실수

- `LENGTH`를 모든 문자열의 글자 수라고 생각한다.
- SQL 문자열 위치를 0부터 시작한다고 생각한다.
- `LPAD` 목표 길이가 짧으면 원본이 그대로 나온다고 생각한다.
- `TRIM`이 문자열 내부 모든 공백을 제거한다고 생각한다.
- `REPLACE`가 실제 Table Data를 수정한다고 생각한다.
- `CONCAT`에 NULL이 있어도 자동으로 빈 문자열이 된다고 생각한다.
- Oracle의 `||`를 MariaDB에서도 그대로 문자열 결합으로 사용한다.
- Display Formatting을 무조건 SQL 문자열 함수로 처리한다.

---

# 57. Debugging

```text
1. LENGTH와 CHAR_LENGTH 중 무엇이 필요한가?
2. SUBSTRING 시작 위치를 0으로 착각하지 않았는가?
3. SUBSTRING의 세 번째 인수가 “끝 위치”가 아니라 길이인지 확인했는가?
4. LPAD/RPAD 목표 길이가 원본보다 짧지 않은가?
5. TRIM 후 내부 공백이 남는 것이 정상인지 확인했는가?
6. CONCAT 인수에 NULL이 있는가?
7. CONCAT_WS Separator가 NULL인가?
8. Case 비교가 Collation 영향을 받는가?
9. 문자열 함수 때문에 Index 사용이 제한되는지 실행계획을 확인했는가?
```

---

# 58. 종합실습

## 문제 1

모든 사원의 이름과 이름의 Byte 길이, Character 길이를 조회하시오.

## 문제 2

사원 이름의 앞 두 Character만 조회하시오.

## 문제 3

이름의 두 번째 Character부터 세 Character를 조회하시오.

## 문제 4

이름에 포함된 `A`를 `*`로 변경해 조회하시오.

## 문제 5

이름의 앞 두 Character만 남기고 나머지를 `*`로 마스킹하시오.

## 문제 6

`ENAME`, `JOB`, `EMPNO`를 `-`로 연결하시오.

## 문제 7

다음 결과가 왜 예상과 다를 수 있는지 설명하시오.

```sql
SELECT LENGTH('가나다');
```

## 문제 8

다음 Query에서 원본 이름이 5글자여도 Result가 3글자가 될 수 있는 이유를 설명하시오.

```sql
SELECT LPAD(ename, 3, '#')
FROM emp;
```

---

# 59. 정답과 해설

## 문제 1

```sql
SELECT
    ename,
    LENGTH(ename) AS byte_length,
    CHAR_LENGTH(ename) AS char_length
FROM emp;
```

## 문제 2

```sql
SELECT
    ename,
    SUBSTRING(ename, 1, 2) AS prefix
FROM emp;
```

## 문제 3

```sql
SELECT
    ename,
    SUBSTRING(ename, 2, 3) AS partial_name
FROM emp;
```

## 문제 4

```sql
SELECT
    ename,
    REPLACE(ename, 'A', '*') AS replaced_name
FROM emp;
```

## 문제 5

```sql
SELECT
    ename,
    RPAD(
        SUBSTRING(ename, 1, 2),
        CHAR_LENGTH(ename),
        '*'
    ) AS masked_name
FROM emp;
```

## 문제 6

```sql
SELECT
    CONCAT_WS('-', ename, job, empno) AS employee_info
FROM emp;
```

## 문제 7

MariaDB의 `LENGTH()`는 Character 개수가 아니라 Byte 길이를 반환한다. 다국어 문자열의 Character 수가 필요하면 `CHAR_LENGTH()`를 사용한다.

## 문제 8

`LPAD()`의 두 번째 인수는 최소 길이가 아니라 **최종 목표 길이**다. 원본이 목표 길이보다 길면 Result가 목표 길이에 맞게 잘릴 수 있다.

---

# 60. 최종 체크리스트

- [ ] `LOWER`, `UPPER`를 사용할 수 있는가?
- [ ] Case 변환과 Collation의 관계를 이해하는가?
- [ ] `LENGTH`가 Byte 길이임을 아는가?
- [ ] `CHAR_LENGTH`가 Character 수임을 아는가?
- [ ] `SUBSTRING` 위치가 1부터 시작함을 이해하는가?
- [ ] `SUBSTRING(string, start, length)`를 작성할 수 있는가?
- [ ] `SUBSTR`와 `SUBSTRING`의 관계를 아는가?
- [ ] `REPLACE`가 Query Result를 변환할 뿐 원본 Data를 수정하지 않음을 아는가?
- [ ] `LPAD`, `RPAD`를 사용할 수 있는가?
- [ ] 목표 길이가 짧으면 문자열이 잘릴 수 있음을 아는가?
- [ ] `TRIM`이 양 끝 공백을 제거함을 이해하는가?
- [ ] `TRIM`이 내부 공백은 유지함을 아는가?
- [ ] `CONCAT`의 NULL 동작에 주의하는가?
- [ ] `CONCAT_WS`를 사용할 수 있는가?
- [ ] `CONCAT_WS`와 `CONCAT`의 차이를 이해하는가?
- [ ] Oracle `||`와 MariaDB 문자열 결합 방식을 구분하는가?
- [ ] 다국어 문자열 마스킹에 `CHAR_LENGTH`를 고려하는가?
- [ ] Display Formatting과 Data Processing의 책임을 구분하는가?

---

# 61. 핵심 요약

```text
LOWER / UPPER
→ Case 변환
```

```text
LENGTH
→ Byte 길이

CHAR_LENGTH
→ Character 수
```

```text
SUBSTRING(str, start, length)
→ 일부 문자열 추출
→ 기본 위치 1부터
```

```text
REPLACE
→ 일치 문자열 치환
```

```text
LPAD
→ 왼쪽 채우기

RPAD
→ 오른쪽 채우기

목표 길이가 짧음
→ 문자열이 잘릴 수 있음
```

```text
TRIM
→ 양 끝 공백 제거
→ 내부 공백 유지
```

```text
CONCAT
→ 문자열 연결
→ NULL 주의

CONCAT_WS
→ Separator 포함 연결
→ 일부 NULL 인수 건너뜀
```

---

# 마무리

문자열 함수에서 가장 중요한 것은 함수 이름보다 **길이·위치·NULL·Character Set의 의미를 정확하게 구분하는 것**이다.

```text
Byte가 필요한가?
Character 수가 필요한가?
    ↓
어디부터 몇 Character를 자를까?
    ↓
치환할까, Padding할까?
    ↓
NULL이 들어올 수 있는가?
    ↓
DB에서 처리할지 Application에서 처리할지 판단
```

이 기준을 이해하면 다음 숫자·날짜·NULL 함수도 단순 암기가 아니라 **입력 → 변환 → Result** 흐름으로 이해할 수 있다.
# V3 동작 백과 — 문자열은 Row마다 어떻게 변환되는가?

문자열 함수는 원본 Column을 자동 수정하지 않는다. SELECT 과정에서 각 Row의 입력값으로 새로운 Result 값을 만든다.

```sql
SELECT
    ename,
    LOWER(ename) AS lower_name,
    CHAR_LENGTH(ename) AS char_count,
    CONCAT(ename, ' 사원') AS label
FROM emp
WHERE empno = 7369;
```

입력:

```text
EMPNO=7369, ENAME='SMITH'
```

함수 실행:

```text
LOWER('SMITH')        → 'smith'
CHAR_LENGTH('SMITH')  → 5
CONCAT('SMITH',' 사원') → 'SMITH 사원'
```

결과:

```text
ENAME | LOWER_NAME | CHAR_COUNT | LABEL
SMITH | smith      | 5          | SMITH 사원
```

## Byte 수와 글자 수

```sql
SELECT LENGTH('한글'), CHAR_LENGTH('한글');
```

UTF-8 환경의 대표 결과:

```text
LENGTH('한글')      → 6 Byte
CHAR_LENGTH('한글') → 2 Character
```

문자 수 제한에는 `CHAR_LENGTH`, 저장 크기 확인에는 `LENGTH`의 의미를 검토한다.

## 함수와 Index

```sql
WHERE LOWER(ename) = 'smith'
```

Column에 함수를 적용하면 일반 Index를 그대로 활용하기 어려울 수 있다. 먼저 Collation과 저장 규칙을 확인하고 실행 계획으로 검증한다.

## 수업 원본에서 다시 찾기

| 개념 | 내 코드 검색 Anchor | 강사님 코드 검색 Anchor |
| --- | --- | --- |
| 대소문자 | `select lower('Human')` | 같은 Query |
| 길이 | `length(`, `char_length(` | 문자열 길이 구간 |
| 추출 | `substring(` | `substring(` |
| 치환 | `replace(` | `replace(` |
| Padding | `lpad(`, `rpad(` | 같은 함수 구간 |
| 결합 | `concat(` | `concat(` |

각 함수는 입력값, 반환값, NULL 입력 결과와 원본 Data 변경 여부를 따로 확인한다.
