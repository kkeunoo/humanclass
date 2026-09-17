---
title: SQL 문자열 함수
version: v4.0-detailed-encyclopedia
last_updated: 2026-09-17
status: Completed
---

# SQL 문자열 함수

## 이 문서에서 바로 찾기

- [학습 목표](#sql-07-section-2)
- [개념에서 실제 실행까지 — 문자열 함수란? — 바이트·문자·표시 결과 구분](#sql-07-section-3)
- [50. 내 코드와 강사님 코드 비교](#sql-07-section-53)
- [57. Debugging](#sql-07-section-60)
- [58. 종합실습](#sql-07-section-61)
- [59. 정답과 해설](#sql-07-section-62)
- [60. 최종 체크리스트](#sql-07-section-63)
- [61. 핵심 요약](#sql-07-section-64)

<details>
<summary>상세 목차 전체 펼치기</summary>

- [문서 정보](#sql-07-section-1)
- [학습 목표](#sql-07-section-2)
- [개념에서 실제 실행까지 — 문자열 함수란? — 바이트·문자·표시 결과 구분](#sql-07-section-3)
- [1. 문자열 함수란?](#sql-07-section-4)
- [2. 함수는 Result를 만든다](#sql-07-section-5)
- [3. LOWER](#sql-07-section-6)
- [4. UPPER](#sql-07-section-7)
- [5. Column에 LOWER 적용](#sql-07-section-8)
- [6. Column에 UPPER 적용](#sql-07-section-9)
- [7. LIKE와 LOWER/UPPER](#sql-07-section-10)
- [8. Case 변환과 Collation](#sql-07-section-11)
- [9. 함수 적용과 Index](#sql-07-section-12)
- [10. LENGTH](#sql-07-section-13)
- [11. LENGTH를 “글자 수”라고만 하면 안 되는 이유](#sql-07-section-14)
- [12. 한글 LENGTH](#sql-07-section-15)
- [13. CHAR_LENGTH](#sql-07-section-16)
- [14. LENGTH vs CHAR_LENGTH](#sql-07-section-17)
- [15. CHARACTER_LENGTH](#sql-07-section-18)
- [16. LENGTH 조건](#sql-07-section-19)
- [17. 사용자 이름 길이는 CHAR_LENGTH 검토](#sql-07-section-20)
- [18. SUBSTRING](#sql-07-section-21)
- [19. MariaDB 문자열 위치는 1부터](#sql-07-section-22)
- [20. SUBSTRING 두 번째 위치부터](#sql-07-section-23)
- [21. SUBSTR](#sql-07-section-24)
- [22. SUBSTRING을 권장하는 이유](#sql-07-section-25)
- [23. 앞 두 글자 추출](#sql-07-section-26)
- [24. 시작 위치만 지정](#sql-07-section-27)
- [25. 음수 위치](#sql-07-section-28)
- [26. REPLACE](#sql-07-section-29)
- [27. REPLACE는 일치 항목을 치환](#sql-07-section-30)
- [28. REPLACE는 원본 Data를 UPDATE하지 않는다](#sql-07-section-31)
- [29. REPLACE와 Case](#sql-07-section-32)
- [30. LPAD](#sql-07-section-33)
- [31. LPAD 구조](#sql-07-section-34)
- [32. 목표 길이가 더 짧으면?](#sql-07-section-35)
- [33. RPAD](#sql-07-section-36)
- [34. 숫자에 LPAD](#sql-07-section-37)
- [35. 공백 Padding](#sql-07-section-38)
- [36. 이름 마스킹 문제](#sql-07-section-39)
- [37. 원래 이름 길이에 맞춘 마스킹](#sql-07-section-40)
- [38. 다국어 마스킹이라면 CHAR_LENGTH](#sql-07-section-41)
- [39. TRIM](#sql-07-section-42)
- [40. TRIM은 내부 공백을 제거하지 않는다](#sql-07-section-43)
- [41. LTRIM과 RTRIM](#sql-07-section-44)
- [42. CONCAT](#sql-07-section-45)
- [43. 구분자를 직접 넣는 CONCAT](#sql-07-section-46)
- [44. CONCAT과 NULL](#sql-07-section-47)
- [45. CONCAT에서 NULL 처리](#sql-07-section-48)
- [46. CONCAT_WS](#sql-07-section-49)
- [47. CONCAT_WS 구조](#sql-07-section-50)
- [48. CONCAT_WS와 NULL](#sql-07-section-51)
- [49. Oracle의 `||`와 MariaDB](#sql-07-section-52)
- [50. 내 코드와 강사님 코드 비교](#sql-07-section-53)
- [51. 개선된 통합 예제](#sql-07-section-54)
- [52. 실무 문자열 함수 기준](#sql-07-section-55)
- [53. LENGTH 리팩토링](#sql-07-section-56)
- [54. 마스킹 리팩토링](#sql-07-section-57)
- [55. CONCAT 리팩토링](#sql-07-section-58)
- [56. 자주 하는 실수](#sql-07-section-59)
- [57. Debugging](#sql-07-section-60)
- [58. 종합실습](#sql-07-section-61)
- [59. 정답과 해설](#sql-07-section-62)
- [60. 최종 체크리스트](#sql-07-section-63)
- [61. 핵심 요약](#sql-07-section-64)
- [마무리](#sql-07-section-65)
- [V3 동작 백과 — 문자열은 Row마다 어떻게 변환되는가?](#sql-07-section-66)

</details>

---

<a id="sql-07-section-1"></a>

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

<a id="sql-07-section-2"></a>

## 학습 목표

- 문자 길이·부분 문자열·결합과 원본 변경을 구분한다.
- 실제 입력·중간 상태·결과와 실패 조건을 직접 확인한다.

---

<a id="sql-07-section-3"></a>

## 개념에서 실제 실행까지 — 문자열 함수란? — 바이트·문자·표시 결과 구분

### 무엇이며 왜 배워야 할까?

문자열 함수는 저장된 텍스트나 상수에서 새로운 표시 결과를 만든다. SELECT REPLACE(...)는 원본을 UPDATE하는 명령이 아니다. 수업의 마스킹은 화면에 보여 줄 문자열을 만드는 예제이며 그것만으로 실제 데이터 접근 권한이 보호되지는 않는다.

LENGTH는 바이트 길이, CHAR_LENGTH는 문자 수다. 한글이 언제나 3바이트라는 규칙이 아니라 사용한 문자셋·문자에 따라 다르다. 아래는 utf8mb4 문자열임을 명시해 두 글자 6바이트를 재현한다. 영어 이름 데이터만 보면 두 함수 값이 같아 차이를 놓치기 쉽다.

MariaDB SUBSTRING의 시작 위치는 일반적으로 1부터이며 Python·JavaScript의 0부터 인덱스와 구분한다. LPAD/RPAD의 길이는 ‘추가할 개수’가 아니라 최종 목표 길이다. 목표가 원래보다 짧으면 문자열이 잘린다.

CONCAT은 일반 MariaDB 모드에서 인수 중 NULL이 있으면 NULL을 반환한다. CONCAT_WS는 구분자 뒤의 NULL 인수를 건너뛰지만 빈 문자열은 항목으로 유지한다. 특별한 SQL 모드는 동작에 영향을 줄 수 있어 환경 조건을 함께 기록한다.

### 입력은 어디에서 오는가?

EMP·DEPT·SALGRADE는 초기화 자료 그대로 준비된 상태다. EMP 14행, DEPT 4행, SALGRADE 5행이다. 다른 DML로 데이터를 바꿨다면 아래 결과와 달라질 수 있다. 상수 SELECT 예제는 테이블 없이도 실행할 수 있다.

### 실행 가능한 보충 SQL과 결과

아래는 원본의 개념을 작은 검증 범위로 정리한 보충 예제다. MariaDB 12.3.2, 일반 SQL 모드·InnoDB 기준에서 결과를 확인했다. 조회 SQL은 SQL 편집기의 Result Grid, 변경 SQL은 영향 행 표시와 사후 SELECT로 관찰한다. DBMS·모드·데이터 상태가 다르면 차이를 확인해야 한다.

```sql
SELECT LENGTH(_utf8mb4'한구') AS bytes_len,
       CHAR_LENGTH(_utf8mb4'한구') AS chars_len,
       SUBSTRING('SCOTT', 2, 3) AS part,
       LPAD('SCOTT', 3, '#') AS shortened;
SELECT CONCAT('A', NULL, 'B') AS normal_concat,
       CONCAT_WS('-', 'A', NULL, '', 'B') AS separated;
```

Result Grid의 열·행 값:

```text
bytes_len	chars_len	part	shortened
6	2	COT	SCO
normal_concat	separated
NULL	A--B
```

여러 SELECT가 있으면 위 출력에 결과 헤더가 다시 나타난다. 숫자의 표시 자릿수와 NULL 표시 모양은 클라이언트별로 달라질 수 있지만 값과 행의 의미를 먼저 비교한다.

### 논리적 처리와 상태 변화 — 단계별로 따라가기

1. utf8mb4로 지정한 한글의 바이트와 문자 수를 따로 계산한다.
2. SUBSTRING으로 SCOTT의 두 번째부터 세 글자 COT를 만든다.
3. LPAD 목표 길이 3이 원래 5보다 짧아 SCO로 잘린다.
4. CONCAT_WS가 NULL은 건너뛰고 빈 문자열은 남겨 구분자를 두 번 넣는다.

### 내 코드·강사님 코드의 어느 부분에 있었을까?


#### 내 코드: `workspace_sql/Script.sql` 262~271행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql
-- lpad(행/열, 자릿수, 문자열)
-- 대상의 자릿수를 맞춰주고 남으면 채워주는 것이기 때문에 아래 3으로 하면 3글자로 줄어듦
select lpad(ename, 10, '#'), ename from emp; 
select lpad(ename, 3, '#'), ename from emp; 

select rpad(ename, 10, '#'), ename from emp; 

select lpad(sal, 10, '0'), ename from emp; 
select lpad(ename, 10, ' '), ename from emp;
```

#### 강사님 코드: `workspace_teacher/workspace_sql/Script.sql` 225~234행

아래는 문맥을 확인하기 위한 발췌다. 주석에 적힌 설명이나 일부 SQL의 앞 상태까지 자동으로 정답이라고 간주하지 않는다. 발췌 조각 전체를 그대로 실행하라는 의미도 아니다.

```sql

-- 대상의 자리수를 맞춰주고 남으면 채워줌
select lpad(ename, 10, '#') from emp;
select lpad(ename, 3, '#') from emp;

select rpad(ename, 10, '#') from emp;

select lpad(sal, 10, '0') from emp;
select lpad(ename, 10, ' ') from emp;
```

두 원본의 lpad(ename,3,'#')는 길이 조정으로 원래 이름을 줄이는 예제다. 내 코드에 추가된 char_length는 LENGTH 메모를 문자 수와 구분하는 데 중요하다.

### 실무에서 사용하거나 디버깅할 때

표현식 결과와 저장 데이터 변경을 구분한다. 결과가 다르면 원본의 앞선 실행 상태, 입력 행 수, NULL·중복·경계값, 조인 후 행 수를 확인한다. 오류 없이 종료한 변경도 0행 대상일 수 있다. 실제 실행 순서·성능은 아래 본문의 논리 설명만으로 단정하지 말고 실행 계획·사후 조회로 검증한다.

### 이해 확인 실습

1. 같은 길이로 이름을 마스킹하려면 LENGTH와 CHAR_LENGTH 중 무엇을 먼저 검토할까?
2. SELECT REPLACE(ename,'A','X') 실행 후 원래 이름을 다시 SELECT하면?

<details>
<summary>정답과 판단 근거 펼치기</summary>

1. 문자 단위 목표라면 CHAR_LENGTH다. 바이트 길이를 목표로 사용하면 다국어에서 길이가 잘못될 수 있다.
2. 원래 이름 그대로다. SELECT 표현식은 저장 값을 UPDATE하지 않는다.

</details>

### 이 개념을 다시 사용할 수 있는지 확인

- [ ] 개념·필요성·입력 컬럼과 자료형을 내 말로 설명한다.
- [ ] 중간 행·그룹·관계와 최종 결과를 구분한다.
- [ ] 원본 코드의 앞 상태와 보충 예제의 조건을 구분한다.
- [ ] NULL·0행·중복·경계값 또는 변경 실패를 재검토한다.

---

<a id="sql-07-section-4"></a>

## 1. 문자열 함수란?

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

<a id="sql-07-section-5"></a>

## 2. 함수는 Result를 만든다

```sql
SELECT
    ename,
    LOWER(ename)
FROM emp;
```

`ENAME` 값을 변경해 저장하는 것이 아니라 Query Result에서 변환된 값을 반환한다.

---

<a id="sql-07-section-6"></a>

## 3. LOWER

문자열을 소문자로 변환한다.

```sql
SELECT LOWER('Human');
```

Result:

```text
human
```

---

<a id="sql-07-section-7"></a>

## 4. UPPER

문자열을 대문자로 변환한다.

```sql
SELECT UPPER('Human');
```

Result:

```text
HUMAN
```

---

<a id="sql-07-section-8"></a>

## 5. Column에 LOWER 적용

```sql
SELECT
    ename,
    LOWER(ename) AS lower_name
FROM emp;
```

---

<a id="sql-07-section-9"></a>

## 6. Column에 UPPER 적용

```sql
SELECT
    ename,
    UPPER(ename) AS upper_name
FROM emp;
```

---

<a id="sql-07-section-10"></a>

## 7. LIKE와 LOWER/UPPER

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

<a id="sql-07-section-11"></a>

## 8. Case 변환과 Collation

MariaDB에서 Case Sensitivity는 Collation에도 영향을 받는다.

따라서:

```sql
WHERE UPPER(ename) LIKE UPPER('%Am%')
```

이 항상 필요한 것은 아니다.

Case-insensitive Collation에서는 기본 비교만으로도 같은 결과가 나올 수 있다.

---

<a id="sql-07-section-12"></a>

## 9. 함수 적용과 Index

다음처럼 Indexed Column에 함수를 직접 적용하면 일반 Index 활용이 제한될 수 있다.

```sql
WHERE UPPER(ename) = 'SMITH'
```

성능이 중요한 Query는 Collation, Functional Index 지원 여부, 실행계획 등을 확인한다.

---

<a id="sql-07-section-13"></a>

## 10. LENGTH

원본:

```sql
SELECT
    LENGTH(ename),
    ename
FROM emp;
```

`LENGTH()`는 MariaDB에서 문자열의 **Byte 길이**를 반환한다.

---

<a id="sql-07-section-14"></a>

## 11. LENGTH를 “글자 수”라고만 하면 안 되는 이유

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

<a id="sql-07-section-15"></a>

## 12. 한글 LENGTH

UTF-8 계열 Character Set이라면:

```sql
SELECT LENGTH('가나다');
```

Character 수는 3이지만 Byte 수는 더 클 수 있다.

따라서 `LENGTH = 글자 수`라고 일반화하면 부정확하다.

---

<a id="sql-07-section-16"></a>

## 13. CHAR_LENGTH

Character 개수를 구하려면:

```sql
SELECT CHAR_LENGTH('가나다');
```

Result:

```text
3
```

---

<a id="sql-07-section-17"></a>

## 14. LENGTH vs CHAR_LENGTH

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

<a id="sql-07-section-18"></a>

## 15. CHARACTER_LENGTH

`CHAR_LENGTH()`의 동의 함수로 `CHARACTER_LENGTH()`도 사용할 수 있다.

```sql
SELECT CHARACTER_LENGTH('Human');
```

---

<a id="sql-07-section-19"></a>

## 16. LENGTH 조건

원본:

```sql
SELECT *
FROM emp
WHERE LENGTH(ename) = 4;
```

현재 EMP 이름이 영문 중심이라 Character 수 조건처럼 동작한다.

---

<a id="sql-07-section-20"></a>

## 17. 사용자 이름 길이는 CHAR_LENGTH 검토

다국어 이름을 실제 Character 수로 제한한다면:

```sql
SELECT *
FROM member
WHERE CHAR_LENGTH(name) = 4;
```

처럼 의미에 맞는 함수를 선택한다.

---

<a id="sql-07-section-21"></a>

## 18. SUBSTRING

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

<a id="sql-07-section-22"></a>

## 19. MariaDB 문자열 위치는 1부터

```sql
SELECT SUBSTRING('SMITH', 1, 2);
```

Result:

```text
SM
```

JavaScript나 Python의 Index 0과 혼동하지 않는다.

---

<a id="sql-07-section-23"></a>

## 20. SUBSTRING 두 번째 위치부터

```sql
SELECT SUBSTRING('SMITH', 2, 3);
```

Result:

```text
MIT
```

---

<a id="sql-07-section-24"></a>

## 21. SUBSTR

원본에는 다음도 있다.

```sql
SELECT
    SUBSTR(ename, 2, 3),
    ename
FROM emp;
```

MariaDB에서 `SUBSTR()`은 `SUBSTRING()`의 동의 함수로 사용할 수 있다.

---

<a id="sql-07-section-25"></a>

## 22. SUBSTRING을 권장하는 이유

두 함수가 같은 동작을 하더라도:

```sql
SUBSTRING(...)
```

이 이름만 보아도 “부분 문자열”이라는 목적을 이해하기 쉽다.

팀 Coding Convention에 맞춰 일관되게 사용한다.

---

<a id="sql-07-section-26"></a>

## 23. 앞 두 글자 추출

원본 문제:

```sql
SELECT SUBSTRING(ename, 1, 2)
FROM emp;
```

이름의 앞 두 Character를 반환한다.

---

<a id="sql-07-section-27"></a>

## 24. 시작 위치만 지정

```sql
SELECT SUBSTRING('SMITH', 3);
```

세 번째 Character부터 끝까지 반환할 수 있다.

---

<a id="sql-07-section-28"></a>

## 25. 음수 위치

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

<a id="sql-07-section-29"></a>

## 26. REPLACE

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

<a id="sql-07-section-30"></a>

## 27. REPLACE는 일치 항목을 치환

```sql
SELECT REPLACE('BANANA', 'A', '*');
```

Result:

```text
B*N*N*
```

문자열 안의 해당 일치 항목들을 치환한다.

---

<a id="sql-07-section-31"></a>

## 28. REPLACE는 원본 Data를 UPDATE하지 않는다

```sql
SELECT REPLACE(ename, 'A', '에이')
FROM emp;
```

Result에서만 변환된다.

실제 Table 값을 변경하려면 `UPDATE`가 필요하다.

---

<a id="sql-07-section-32"></a>

## 29. REPLACE와 Case

찾을 문자열의 Matching도 Character Set/Collation과 함수 특성을 구분해서 확인해야 한다.

실제 결과가 중요한 경우 Sample Data로 직접 검증한다.

---

<a id="sql-07-section-33"></a>

## 30. LPAD

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

<a id="sql-07-section-34"></a>

## 31. LPAD 구조

```text
LPAD(문자열, 목표길이, 채울문자열)
```

---

<a id="sql-07-section-35"></a>

## 32. 목표 길이가 더 짧으면?

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

<a id="sql-07-section-36"></a>

## 33. RPAD

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

<a id="sql-07-section-37"></a>

## 34. 숫자에 LPAD

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

<a id="sql-07-section-38"></a>

## 35. 공백 Padding

```sql
SELECT LPAD(ename, 10, ' ')
FROM emp;
```

고정 폭 Text처럼 보이게 만들 수 있지만 Web UI나 Report Layout은 Application/CSS 계층에서 처리하는 것이 더 적절한 경우도 많다.

---

<a id="sql-07-section-39"></a>

## 36. 이름 마스킹 문제

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

<a id="sql-07-section-40"></a>

## 37. 원래 이름 길이에 맞춘 마스킹

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

<a id="sql-07-section-41"></a>

## 38. 다국어 마스킹이라면 CHAR_LENGTH

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

<a id="sql-07-section-42"></a>

## 39. TRIM

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

<a id="sql-07-section-43"></a>

## 40. TRIM은 내부 공백을 제거하지 않는다

```text
'  a b  c  '
→ 'a b  c'
```

문자열 중간 공백은 유지된다.

---

<a id="sql-07-section-44"></a>

## 41. LTRIM과 RTRIM

왼쪽만:

```sql
SELECT LTRIM('   Human   ');
```

오른쪽만:

```sql
SELECT RTRIM('   Human   ');
```

---

<a id="sql-07-section-45"></a>

## 42. CONCAT

원본:

```sql
SELECT CONCAT(ename, job)
FROM emp;
```

여러 문자열을 하나로 연결한다.

---

<a id="sql-07-section-46"></a>

## 43. 구분자를 직접 넣는 CONCAT

```sql
SELECT CONCAT(ename, ' ', job)
FROM emp;
```

예:

```text
SMITH CLERK
```

---

<a id="sql-07-section-47"></a>

## 44. CONCAT과 NULL

MariaDB에서 `CONCAT()` 인수 중 `NULL`이 포함되면 전체 Result가 `NULL`이 될 수 있다.

```sql
SELECT CONCAT('A', NULL, 'B');
```

NULL을 빈 문자열처럼 자동 취급한다고 생각하면 안 된다.

---

<a id="sql-07-section-48"></a>

## 45. CONCAT에서 NULL 처리

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

<a id="sql-07-section-49"></a>

## 46. CONCAT_WS

원본:

```sql
SELECT CONCAT_WS('-', ename, job, empno)
FROM emp;
```

`WS`는 **With Separator** 의미다.

---

<a id="sql-07-section-50"></a>

## 47. CONCAT_WS 구조

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

<a id="sql-07-section-51"></a>

## 48. CONCAT_WS와 NULL

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

<a id="sql-07-section-52"></a>

## 49. Oracle의 `||`와 MariaDB

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

<a id="sql-07-section-53"></a>

## 50. 내 코드와 강사님 코드 비교

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

<a id="sql-07-section-54"></a>

## 51. 개선된 통합 예제

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

<a id="sql-07-section-55"></a>

## 52. 실무 문자열 함수 기준

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

<a id="sql-07-section-56"></a>

## 53. LENGTH 리팩토링

### Before

```sql
WHERE LENGTH(name) = 4
```

다국어 사용자 이름의 “4글자”가 요구사항이라면:

### After

```sql
WHERE CHAR_LENGTH(name) = 4
```

Byte와 Character 의미를 구분한다.

---

<a id="sql-07-section-57"></a>

## 54. 마스킹 리팩토링

### Before

```sql
RPAD(
    SUBSTRING(ename, 1, 2),
    6,
    '*'
)
```

무조건 길이 6으로 만든다.

### After

```sql
RPAD(
    SUBSTRING(ename, 1, 2),
    CHAR_LENGTH(ename),
    '*'
)
```

원본 Character 길이에 맞춘다.

---

<a id="sql-07-section-58"></a>

## 55. CONCAT 리팩토링

### Before

```sql
SELECT CONCAT(ename, job, deptno)
FROM emp;
```

값 경계가 불명확하다.

### After

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

<a id="sql-07-section-59"></a>

## 56. 자주 하는 실수

- `LENGTH`를 모든 문자열의 글자 수라고 생각한다.
- SQL 문자열 위치를 0부터 시작한다고 생각한다.
- `LPAD` 목표 길이가 짧으면 원본이 그대로 나온다고 생각한다.
- `TRIM`이 문자열 내부 모든 공백을 제거한다고 생각한다.
- `REPLACE`가 실제 Table Data를 수정한다고 생각한다.
- `CONCAT`에 NULL이 있어도 자동으로 빈 문자열이 된다고 생각한다.
- Oracle의 `||`를 MariaDB에서도 그대로 문자열 결합으로 사용한다.
- Display Formatting을 무조건 SQL 문자열 함수로 처리한다.

---

<a id="sql-07-section-60"></a>

## 57. Debugging

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

<a id="sql-07-section-61"></a>

## 58. 종합실습

### 문제 1

모든 사원의 이름과 이름의 Byte 길이, Character 길이를 조회하시오.

### 문제 2

사원 이름의 앞 두 Character만 조회하시오.

### 문제 3

이름의 두 번째 Character부터 세 Character를 조회하시오.

### 문제 4

이름에 포함된 `A`를 `*`로 변경해 조회하시오.

### 문제 5

이름의 앞 두 Character만 남기고 나머지를 `*`로 마스킹하시오.

### 문제 6

`ENAME`, `JOB`, `EMPNO`를 `-`로 연결하시오.

### 문제 7

다음 결과가 왜 예상과 다를 수 있는지 설명하시오.

```sql
SELECT LENGTH('가나다');
```

### 문제 8

다음 Query에서 원본 이름이 5글자여도 Result가 3글자가 될 수 있는 이유를 설명하시오.

```sql
SELECT LPAD(ename, 3, '#')
FROM emp;
```

---

<a id="sql-07-section-62"></a>

## 59. 정답과 해설

### 문제 1

```sql
SELECT
    ename,
    LENGTH(ename) AS byte_length,
    CHAR_LENGTH(ename) AS char_length
FROM emp;
```

### 문제 2

```sql
SELECT
    ename,
    SUBSTRING(ename, 1, 2) AS prefix
FROM emp;
```

### 문제 3

```sql
SELECT
    ename,
    SUBSTRING(ename, 2, 3) AS partial_name
FROM emp;
```

### 문제 4

```sql
SELECT
    ename,
    REPLACE(ename, 'A', '*') AS replaced_name
FROM emp;
```

### 문제 5

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

### 문제 6

```sql
SELECT
    CONCAT_WS('-', ename, job, empno) AS employee_info
FROM emp;
```

### 문제 7

MariaDB의 `LENGTH()`는 Character 개수가 아니라 Byte 길이를 반환한다. 다국어 문자열의 Character 수가 필요하면 `CHAR_LENGTH()`를 사용한다.

### 문제 8

`LPAD()`의 두 번째 인수는 최소 길이가 아니라 **최종 목표 길이**다. 원본이 목표 길이보다 길면 Result가 목표 길이에 맞게 잘릴 수 있다.

---

<a id="sql-07-section-63"></a>

## 60. 최종 체크리스트

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

<a id="sql-07-section-64"></a>

## 61. 핵심 요약

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

<a id="sql-07-section-65"></a>

## 마무리

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
<a id="sql-07-section-66"></a>

## V3 동작 백과 — 문자열은 Row마다 어떻게 변환되는가?

> 입력 범위 확인: 이 복습 부분의 작은 표는 처리 원리를 위한 가정·발췌이며 전체 초기화 EMP의 입력 전체가 아니다. FROM emp를 그대로 실행하면 모든 대상 사원을 처리한다. 수치는 작은 가정 입력의 결과인지 전체 14행 결과인지 구분한다. 실행·시간순 설명은 논리적 설명이며 물리적 평가 순서를 보장하지 않는다.

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

### Byte 수와 글자 수

```sql
SELECT LENGTH('한글'), CHAR_LENGTH('한글');
```

UTF-8 환경의 대표 결과:

```text
LENGTH('한글')      → 6 Byte
CHAR_LENGTH('한글') → 2 Character
```

문자 수 제한에는 `CHAR_LENGTH`, 저장 크기 확인에는 `LENGTH`의 의미를 검토한다.

### 함수와 Index

```sql
WHERE LOWER(ename) = 'smith'
```

Column에 함수를 적용하면 일반 Index를 그대로 활용하기 어려울 수 있다. 먼저 Collation과 저장 규칙을 확인하고 실행 계획으로 검증한다.

### 수업 원본에서 다시 찾기

| 개념 | 내 코드 검색 Anchor | 강사님 코드 검색 Anchor |
| --- | --- | --- |
| 대소문자 | `select lower('Human')` | 같은 Query |
| 길이 | `length(`, `char_length(` | 문자열 길이 구간 |
| 추출 | `substring(` | `substring(` |
| 치환 | `replace(` | `replace(` |
| Padding | `lpad(`, `rpad(` | 같은 함수 구간 |
| 결합 | `concat(` | `concat(` |

각 함수는 입력값, 반환값, NULL 입력 결과와 원본 Data 변경 여부를 따로 확인한다.

