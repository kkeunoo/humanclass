# 07. 문자열 함수 — 한 글자 위치·결과 길이·원본 변경 구별

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

문자열 함수는 값을 받아 새로운 문자열이나 숫자를 결과로 만든다. 글자를 자르고 붙여 보여 줬다고 원본 이름이 수정된 것은 아니다. 입력·인자·반환 결과를 한 줄씩 읽는다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

SUBSTR 위치와 길이, LENGTH의 단위, REPLACE·TRIM·LPAD·RPAD·CONCAT의 역할을 설명한다. 원래 길이 가리기와 고정 별표 문제를 구별한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

SUBSTRING 또는 SUBSTR의 시작 위치는 이 수업의 일반 MariaDB 모드에서 1부터 읽는다. Python의 인덱스 0과 섞으면 한 글자씩 어긋난다. SUBSTR(문자열,2,3)은 두 번째부터 세 글자다. 세 번째까지라는 끝 위치를 뜻하지 않는다.

| 함수 | 입력에서 정할 것 | 반환 결과 |
| --- | --- | --- |
| LENGTH | 대상 문자열 | 일반 모드 바이트 길이 |
| SUBSTR | 시작·개수 | 부분 문자열 |
| REPLACE | 찾을 글자·바꿀 글자 | 치환 문자열 |
| TRIM | 대상 문자열 | 양끝 공백 제거 |
| LPAD·RPAD | 최종 길이·채울 글자 | 왼쪽·오른쪽 길이 맞춤 |
| CONCAT | 이어 붙일 값들 | 연결 문자열 |
| CONCAT_WS | 구분자·값들 | 구분자를 넣은 연결 |

LPAD·RPAD 두 번째 인자는 추가할 글자 수가 아니라 최종 길이다. 원본보다 짧게 지정하면 줄어들 수 있다. TRIM은 중간 공백을 모두 제거하지 않는다. 이 함수들을 SELECT에서 쓴 결과는 원본 열을 변경한 UPDATE가 아니다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB SUBSTRING](https://mariadb.com/docs/server/reference/sql-functions/string-functions/substring), [LENGTH](https://mariadb.com/docs/server/reference/sql-functions/string-functions/length), [RPAD](https://mariadb.com/docs/server/reference/sql-functions/string-functions/rpad). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/07_SQL_문자열함수.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT SUBSTR('SMITH', 2, 3) AS part, TRIM('  a b  ') AS cleaned;
SELECT REPLACE('ADA', 'A', '*') AS replaced;
SELECT RPAD(SUBSTR('SMITH', 1, 2), 5, '*') AS masked;
SELECT RPAD(SUBSTR('SMITH', 1, 2), 6, '*') AS fixed;
SELECT CONCAT_WS('-', 'ADA', 'CLERK', 1) AS label;
```

SMITH에서 2번째 M부터 세 글자를 읽으면 MIT다. TRIM 뒤에도 a와 b 사이 한 칸은 남는다. ADA의 A 두 곳을 모두 *로 바꾼 결과는 *D*다. 앞 두 글자 SM을 남겨 총길이5로 채우면 별표3개, 총길이6이면 별표4개다. CONCAT_WS의 첫 인자 -는 값이 아니라 각 값 사이 구분자다.

**가상 자료 기준 예상 결과:**

| 식 | 예상 값 |
| --- | --- |
| SUBSTR·TRIM | MIT / a b |
| REPLACE | *D* |
| 원래 길이 5로 RPAD | SM*** |
| 고정 길이 6으로 RPAD | SM**** |
| CONCAT_WS | ADA-CLERK-1 |

SUBSTR·TRIM·REPLACE 두 조회는 메모리 DB에서 교차 확인했다. RPAD·CONCAT_WS 결과는 공식 문법과 인자 길이 계산으로 확인한 예상이며 이 환경의 MariaDB 실행 결과가 아니다.

**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 247–256행 · **원본 발췌**

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

**발췌 바로 풀이:** `SUBSTRING(ename, 2, 3)`은 이름의 **2번째 문자부터 3개**를 가져온다. 내 코드는 같은 뜻의 `SUBSTR`도 함께 사용했다. `LENGTH(ename)`은 문자열의 **바이트 길이**를 반환한다. 이 실습의 영문 이름에서는 문자 수와 같아 보이지만, 한글 이름의 글자 수를 뜻한다고 일반화하지 않는다. 강사님·내 코드 모두 영문 이름 길이로 조건을 실습했다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 258–273행 · **원본 발췌**

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

**발췌 바로 풀이:** `REPLACE(ename, 'A', '에이')`는 조회 결과의 해당 글자를 바꿔 보여 준다. 원본 `EMP` 값이 수정되는 `UPDATE`가 아니다. `LPAD`와 `RPAD`는 지정한 길이에 맞춰 **왼쪽·오른쪽을 채운다**. 길이를 원본보다 짧게 주면 잘릴 수 있다. `TRIM`은 양끝 공백을 없앤다. 단어 사이의 공백까지 지운다고 읽지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 275–280행 · **원본 발췌**

```sql
-- concat으로 column을 한 줄로 합칠 수 있음
-- Oracle에서는 ename || job으로 합치기 사용 할 수 있음
select concat(ename, job) from emp;
select concat(ename, ' ', job) from emp;
-- concat_ws(with seperator)로 구분자를 사용하여 합칠 수 있음
select concat_ws('-', ename, job, empno) from emp;
```

**발췌 바로 풀이:** `CONCAT(ename, ' ', job)`은 이름과 직업 사이에 공백을 끼워 붙인다. `CONCAT_WS('-', ename, job, empno)`는 `-`를 구분자로 쓴다. 두 원본 모두 이름 앞 두 글자 뒤를 별표로 채우는 실제 문제도 풀었다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 320–326행 · **원본 발췌**

```sql
-- ename의 앞 두 글자만 원본 그대로 출력하고,
-- 4개의 *표를 붙여서 출력
select rpad(substr(ename, 1, 2), 6, '*'), ename from emp;

-- ename의 앞 두 글자만 원본 그대로 출력하고
-- 나머지 이름 만큼의 *를 출력 
select rpad(substr(ename, 1, 2), length(ename), '*'), ename from emp;
```

**발췌 바로 풀이:** 강사님은 `RPAD(SUBSTRING(ename, 1, 2), LENGTH(ename), '*')`, 나는 `RPAD(SUBSTR(...), LENGTH(ename), '*')` 형태다. 둘 다 앞 두 글자를 남기고 **원래 이름 길이까지** `*`로 채운다. 내 코드의 앞 문장은 길이 6으로 고정해 “별표 4개”를 붙이는 별도 문제이고, 뒤 문장이 이름 길이에 맞춘 풀이이다.

내 원본은 영문 이름의 LENGTH와 SUBSTR를 함께 실행했다. 영문에서는 바이트와 글자 수가 같아 보이지만 한글까지 같은 설명으로 넓히면 안 된다. 마스킹 첫 쿼리는 총길이6 고정, 다음 쿼리는 원래 이름 길이를 사용한다. 이름이 원래 두 글자보다 짧으면 “별표 네 개”라는 설명도 그대로 성립하지 않으므로 입력 전제를 읽는다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

안쪽 SUBSTR가 앞 두 글자 반환 → 그 문자열이 RPAD 첫 인자 → LENGTH(원래 이름)가 최종 길이 → 별표로 나머지 채움 → 결과 열 표시 순서다. 중첩 함수를 읽을 때 가장 안쪽 계산을 표로 풀면 좋다. DB 내장 함수이며 외부 Python 함수 정의가 필요한 호출은 아니다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 원본을 같이 출력해 변환 전후를 비교했고 RPAD 길이가 짧으면 잘린다는 점도 기록했다. **교정:** 함수가 열 전체를 저장 변경한다는 뜻으로 REPLACE 주석을 읽지 않는다. **단위:** LENGTH는 일반 모드의 바이트 길이이며 글자 수와 구별한다. **한계:** 이름 일부를 별표로 바꾸는 화면 예시가 완전한 익명화·개인정보 보호를 보장하는 것은 아니다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 SUBSTR·SUBSTRING·RPAD가 핵심상 같아 전체를 중복 인용하지 않는다. 내 고정 길이와 원래 길이 두 풀이도 각각 문제에 맞다. 길이 값의 목적을 기준으로 비교해야 한쪽을 무조건 더 좋다고 평가하지 않을 수 있다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 단계 | 값 | 다음 인자 |
| --- | --- | --- |
| 원본 | SMITH | SUBSTR 대상 |
| SUBSTR(1,2) | SM | RPAD 대상 |
| LENGTH(SMITH) | 5 | 최종 길이 |
| RPAD | SM*** | 결과 표시 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| SUBSTR 시작을 1로 | SMI | 첫 글자부터 세 개 |
| 총길이 6을 4로 | SM** | 전체 네 글자 |
| TRIM 입력의 중간 공백 증가 | 중간 공백 유지 | 양끝만 제거 |
| REPLACE 대상 A를 D로 | A*A | 일치 글자 변경 |

한 글자 어긋나면 SQL 위치1과 Python 인덱스0을 구별한다. 별표가 너무 많으면 최종 길이와 추가 개수를 혼동했는지 본다. 한글 길이는 현재 문자셋·SQL 모드와 LENGTH 단위를 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 상세 Unicode 처리·식별자와 문자열 인용·함수와 인덱스의 관계는 선택 확장이다. CHAR_LENGTH 자체는 내 원본 뒤쪽에 실제 사용이 있어 [17장](17_SQL_Index와_AUTO_INCREMENT.md) 본문에서 LENGTH와 비교한다. 해당 함수까지 미학습으로 분류하지 않는다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. SUBSTR의 세 번째 인자는 끝 위치인가?
2. RPAD 두 번째 인자는 추가 글자 수인가?
3. SELECT REPLACE가 원본을 수정하는가?
4. 일반 모드 LENGTH는 글자 수인가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

읽을 개수다. 최종 길이다. 조회 결과만 바뀐다. 바이트 길이이며 영문 예제에서는 같아 보일 수 있다.

</details>

| 흔한 혼동 | 구별 |
| --- | --- |
| 시작·개수 | 끝 인덱스 아님 |
| 최종 길이 | 추가 길이 아님 |
| 조회 변환 | 저장 수정 아님 |

[장별 연습문제](실습/연습문제/07_SQL_문자열함수_연습문제.md) · 다음은 [숫자·날짜·NULL 함수](08_SQL_숫자_날짜_NULL함수.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
