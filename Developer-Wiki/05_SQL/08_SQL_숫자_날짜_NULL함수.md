# 08. 숫자·날짜·NULL 함수 — 입력 값과 결과 형태 이해하기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

같은 -3.14도 내림과 소수 부분 버림의 결과는 다르다. 날짜를 보여 주는 형식과 날짜 값을 만드는 것도 다르다. 각 함수가 받는 값과 돌려주는 값을 나누어 본다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

ROUND·CEIL·FLOOR·TRUNCATE·MOD 차이를 설명한다. 날짜 표시와 해석, 현재 시각의 변동성, NULL 대체와 원본 변경의 차이를 구분한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

수직선에서 -4는 -3보다 작다. CEIL은 더 큰 정수 쪽의 -3, FLOOR는 더 작은 정수 쪽의 -4를 선택한다. TRUNCATE(-3.14,0)는 소수 부분을 잘라 -3이 된다. “아래로 버린다” 같은 말만 외우면 음수에서 틀리기 쉽다.

| 함수 | 입력 → 결과 | 핵심 |
| --- | --- | --- |
| ROUND(3.14,1) | 3.14 → 3.1 | 반올림 자리 |
| CEIL(-3.14) | -3.14 → -3 | 큰 정수 방향 |
| FLOOR(-3.14) | -3.14 → -4 | 작은 정수 방향 |
| TRUNCATE(-3.14,1) | -3.14 → -3.1 | 지정 자리 뒤 버림 |
| MOD(10,3) | 10,3 → 1 | 나머지 |
| IFNULL(comm,0) | NULL → 0, 값 → 그대로 | 없을 때만 대체 |

DATE_FORMAT은 날짜 값을 지정한 양식의 문자열로 보여 준다. STR_TO_DATE는 문자열을 양식에 따라 날짜 값으로 읽는다. 방향이 반대다. NOW·SYSDATE는 현재 시각 관련 함수라 고정 문서의 날짜와 항상 같은 값을 내지 않는다. 세부 시각 평가 차이는 TIP이다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB DATE_FORMAT](https://mariadb.com/docs/server/reference/sql-functions/date-time-functions/date_format), [TRUNCATE](https://mariadb.com/docs/server/reference/sql-functions/numeric-functions/truncate), [IFNULL](https://mariadb.com/docs/server/reference/sql-functions/control-flow-functions/ifnull). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/08_SQL_숫자_날짜_NULL함수.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

<details>
<summary>예제 준비 전체 SQL — 현재 장의 학습 문법과 구별</summary>

```sql
DROP TEMPORARY TABLE IF EXISTS book_emp;
CREATE TEMPORARY TABLE book_emp (
    empno INT PRIMARY KEY, ename VARCHAR(20), job VARCHAR(20),
    mgr INT, sal DECIMAL(8,2), comm DECIMAL(8,2), deptno INT
);
INSERT INTO book_emp VALUES
(1,'ADA','CLERK',3,1000,NULL,20),
(2,'BEN','SALESMAN',3,1600,300,30),
(3,'CARA','MANAGER',NULL,3000,NULL,20),
(4,'DAN','CLERK',3,1300,0,10),
(5,'ELLA','ANALYST',3,3000,NULL,20),
(6,'FINN','SALESMAN',3,1500,0,30);
DROP TEMPORARY TABLE IF EXISTS book_dept;
CREATE TEMPORARY TABLE book_dept (deptno INT PRIMARY KEY, dname VARCHAR(20));
INSERT INTO book_dept VALUES (10,'ALPHA'),(20,'BETA'),(30,'GAMMA'),(40,'EMPTY');
```

표 생성·삽입 문법은 14·15장에서 설명한다. TEMPORARY는 원래 수업 구문으로 승격한 것이 아니라 예제 자료를 연결 안에서만 쓰기 위한 새 실행 장치다. 기존 영구 EMP·DEPT를 바꾸는 준비문이 아니다. 임시 표의 상세 수명·권한은 아래 TIP에서 구별한다.

</details>

```sql
SELECT ROUND(3.14,1), CEIL(-3.14), FLOOR(-3.14), TRUNCATE(-3.14,0), MOD(10,3);
SELECT DATE_FORMAT('2026-08-07 13:05:09', '%Y-%m-%d %H:%i:%s') AS display_time;
SELECT STR_TO_DATE('07-08-2026', '%d-%m-%Y') AS parsed_date;
SELECT ename, sal + comm AS raw_total, sal + IFNULL(comm,0) AS filled_total
FROM book_emp WHERE empno IN (1,2,4) ORDER BY empno;
```

음수의 CEIL과 FLOOR가 다른 쪽으로 움직인다. 날짜의 %m은 월, %i는 분이므로 Python strftime의 분 표기와 혼동하지 않는다. ADA 수당은 NULL이라 덧셈 결과가 NULL이지만 IFNULL이 계산 중 0을 제공하면 1000을 유지한다. BEN은 300, DAN은 이미 0이어서 원래 값이 그대로 사용된다. IFNULL이 테이블에 0을 저장한 것은 아니다.

**가상 자료 기준 예상 결과:**

첫 결과는 **3.1·-3·-4·-3·1**. 날짜 표시는 **2026-08-07 13:05:09**, 날짜 해석 값은 **2026-08-07**이다.

| 이름 | raw_total | filled_total |
| --- | --- | --- |
| ADA | NULL | 1000 |
| BEN | 1900 | 1900 |
| DAN | 1300 | 1300 |

수당 조회 한 문장은 SQLite에서 교차 확인했다. 숫자·날짜 함수는 MariaDB 공식 정의와 고정 인자에 따른 예상 결과이며 해당 서버에서 실행하지 않았다. SQLite의 같은 이름 함수로 모든 MariaDB 동작을 대체 검증했다고 표시하지 않는다.

**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 282–298행 · **원본 발췌**

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

**발췌 바로 풀이:** `ROUND`는 반올림, `CEIL`은 올림, `FLOOR`는 내림, `TRUNCATE`는 지정 자리 뒤를 버린다. 양쪽 모두 **음수**를 넣어 올림·내림이 0을 향해 움직이는 것과 같은 뜻이 아님을 볼 수 있다. 강사님은 `TRUNCATE(-3.14, 1)`, 나는 `TRUNCATE(-3.14, 0)`을 실행했다. 두 번째 인자가 다른 만큼 소수 첫째 자리 유지와 정수 부분 유지라는 비교가 된다. `MOD(10, 3)`은 나머지를 구한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 300–308행 · **원본 발췌**

```sql
-- now(), sysdate()는 현재 시간을 알 수 있음
select now(); -- 서버시간
select sysdate();

-- date_format(시간, 양식) 으로 나오는 형식을 변경할 수 있음
select date_format(now(), '%Y년 %m월 %d일 %H시 %i분 %s초');

-- string의 일자를 date형태로 바꾸어 줌
select str_to_date('2026-08-07', '%Y-%m-%d');
```

**발췌 바로 풀이:** `NOW()`와 `SYSDATE()`는 실행 시점에 따라 값이 달라진다. `DATE_FORMAT`은 지정한 양식의 **표시 문자열**을 만들고, `STR_TO_DATE`는 양식에 맞는 문자열을 날짜 값으로 바꾼다. 따라서 문서에 적힌 `2026-08-07`을 “오늘 날짜”로 읽으면 안 된다. 내 주석의 “`NOW()`는 서버시간”은 실행 환경에 따른 시간 설정 확인이 필요하다는 뜻으로 읽는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 310–315행 · **원본 발췌**

```sql
-- ifnull(행/열, 기본값) 이면 null일 경우 기본값으로 바꿔줌
select ifnull(comm, 0), comm from emp;
select coalesce(comm, 0), comm from emp;

select sal * 12 + comm from emp;
select sal * 12 + ifnull(comm, 0) from emp;
```

**발췌 바로 풀이:** `sal * 12 + comm`에서 `comm`이 `NULL`이면 계산 전체도 `NULL`이다. `IFNULL(comm, 0)` 또는 `COALESCE(comm, 0)`로 **수당이 없을 때만 0을 대신** 넣으면 급여 계산을 계속할 수 있다. 이는 조회 결과의 계산 방식이며 원본 표의 `COMM` 값을 수정하는 문장이 아니다. 두 원본이 같은 예제를 실행했다.

내 TRUNCATE는 소수0자리, 강사님은 소수1자리라 결과가 -3과 -3.1로 다르다. 같은 코드로 뭉뚱그리지 않는다. 두 원본의 NOW·SYSDATE 출력은 현재 상태에 따라 바뀐다. 수당 계산에서는 두 원본 모두 IFNULL·COALESCE와 원래 NULL 덧셈을 비교했다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

함수 인자 → 각 함수 반환값 → SELECT 결과 열이다. sal*12+IFNULL(comm,0)은 먼저 수당 대체 값을 얻고 급여 계산과 더한다. 문자열 날짜 해석은 초기 EMP 입력의 STR_TO_DATE와 연결한다. 사용자 정의 함수의 숨은 구현이 아니라 DB 내장 함수의 명시된 의미를 읽는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 양수·음수를 같이 사용하고 NULL 대체 전후를 비교했다. **설명 보완:** 올림·내림은 수직선 방향으로 설명해야 음수에도 맞다. **단위:** sal*12를 무조건 연봉으로 확정하지 않는다. **환경:** NOW가 항상 PC 화면 시계와 같은 시간대라는 주장은 연결 설정 확인 없이는 할 수 없다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



같은 함수 목록은 다시 인용하지 않는다. TRUNCATE 두 번째 인자가 1과 0이라는 실제 차이를 남겨 어떤 자리까지 보존하는지 설명한다. 성능이나 실무 우열의 차이가 아니라 의도한 자릿수 차이다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 수당 | IFNULL 반환 | sal+comm | sal+대체값 |
| --- | --- | --- | --- |
| NULL | 0 | NULL | 급여 유지 |
| 300 | 300 | 급여+300 | 급여+300 |
| 0 | 0 | 급여 | 급여 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| TRUNCATE 자리0→1 | -3.1 | 소수1자리 유지 |
| IFNULL 기본값100 | ADA 1100 | 없는 수당만 대체 |
| %i를 %m으로 | 분 자리에 08 | 월 표시로 변경 |
| 고정 날짜를 NOW로 | 실행 시각에 따라 다름 | 동적인 입력 |

음수 결과가 다르면 FLOOR와 TRUNCATE를 구별한다. 날짜 변환이 실패하면 문자열 순서와 양식이 맞는지 본다. 수당 합계가 NULL이면 계산 전에 어떤 대체 정책을 쓸지 정한다. 원래 NULL의 업무 의미를 지우고 무조건 0으로 대체해야 한다는 규칙은 아니다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 정확한 수치와 근사 수치의 반올림 차이, NOW·SYSDATE 평가 시점·시간대·로케일·잘못된 날짜 처리 SQL 모드는 추가 학습이다. [MariaDB 날짜 함수](https://mariadb.com/docs/server/reference/sql-functions/date-time-functions)를 참고한다. 현재 예제는 고정 인자로 기본 방향을 이해하는 데 집중한다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. FLOOR(-3.14)와 TRUNCATE(-3.14,0)는?
2. DATE_FORMAT과 STR_TO_DATE의 방향은?
3. IFNULL은 NULL을 영구 변경하는가?
4. %m과 %i는 무엇인가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

-4와 -3이다. 날짜→표시 문자열, 문자열→날짜 값이다. 조회 계산에서 대체값을 쓴다. 월과 분이다.

</details>

| 선택 | 질문 |
| --- | --- |
| 숫자 | 방향·자릿수 |
| 날짜 | 표시인가 해석인가 |
| NULL | 없음의 의미와 대체 정책 |

[장별 연습문제](실습/연습문제/08_SQL_숫자_날짜_NULL함수_연습문제.md) · 다음은 [CASE](09_SQL_CASE_조건식.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
