# 03. LIKE와 NULL — 글자 모양 검사와 알 수 없는 값 구분

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

이름의 일부를 찾는 조건과 수당이 알려지지 않은 조건은 다른 질문이다. 0·빈 문자열·NULL의 차이를 알아야 필터와 계산 결과를 정확히 읽을 수 있다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

%와 _의 길이 조건을 설명한다. IS NULL과 = NULL의 차이를 확인하고 문자 비교의 대소문자 설정을 일반화하지 않는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

LIKE는 문자열이 패턴에 맞는지 검사한다. %는 0글자 이상, _는 한 글자에 대응한다. S%는 S로 시작하는 값, %AM%는 AM이라는 연속 글자를 포함한 값이다. A 또는 M 중 아무 글자가 포함되면 된다는 뜻이 아니다.

NULL은 값이 알려져 있지 않거나 주어지지 않았음을 나타낸다. 숫자 0은 알고 있는 숫자이고 빈 문자열은 길이가 0인 문자열이므로 NULL과 다르다. NULL=무언가처럼 일반 비교를 하면 참이 아니라 알 수 없음이 될 수 있다. WHERE는 참인 행만 남기므로 = NULL로 값 없음을 찾으려 해도 원하는 행이 나오지 않는다.

| 조건 | 찾는 것 | 새 자료 결과 |
| --- | --- | --- |
| ename LIKE '_A%' | 두 번째 글자가 A | CARA, DAN |
| comm IS NULL | 수당 값 없음 | ADA, CARA, ELLA |
| comm = 0 | 수당 숫자 0 | DAN, FINN |
| comm = NULL | 값과 NULL 일반 비교 | 참인 행 없음 |

IS NULL은 이 상태 자체를 검사한다. LOWER·UPPER는 문자열 변환 함수다. 대소문자를 맞추는 원본 사용은 읽을 수 있지만, MariaDB라는 이름만으로 모든 비교가 대소문자를 무시한다고 확정하지 않는다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB LIKE](https://mariadb.com/docs/server/reference/sql-functions/string-functions/like), [NULL Values](https://mariadb.com/docs/server/reference/data-types/null-values). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/03_SQL_LIKE와_NULL.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT ename FROM book_emp WHERE ename LIKE '_A%' ORDER BY empno;
SELECT ename FROM book_emp WHERE comm IS NULL ORDER BY empno;
SELECT ename FROM book_emp WHERE comm = 0 ORDER BY empno;
SELECT ename FROM book_emp WHERE comm = NULL ORDER BY empno;
```

_가 첫 글자 하나를, A가 둘째 글자를, %가 나머지 0글자 이상을 담당한다. 수당 검사 세 문장은 같은 열에서 알려지지 않은 값·0·일반 비교의 차이를 보여 준다. 값 없음이 0으로 자동 치환된다고 생각하면 둘째와 셋째 결과를 잘못 예상하게 된다.

**가상 자료 기준 예상 결과:**

첫 결과 CARA·DAN, 둘째 ADA·CARA·ELLA, 셋째 DAN·FINN, 마지막은 **0행**이다. 마지막 결과가 NULL 한 칸이라는 뜻은 아니다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 127–146행 · **원본 발췌**

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

**발췌 바로 풀이:** `'S%'`는 S로 시작하는 이름, `'%N'`은 N으로 끝나는 이름, `'%AM%'`은 가운데를 포함해 AM이 이어지는 이름을 찾는다. `%`는 **0글자 이상**, `_`는 **정확히 한 글자**에 대응한다. 그래서 `'_____'`는 길이가 5글자인 이름을 찾는다. 내 원본의 `'_L%'`에서 두 번째 글자가 L이다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 148–161행 · **원본 발췌**

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

**발췌 바로 풀이:** 강사님은 `lower(ename) LIKE lower('%Am%')`, 나는 `upper`와 `lower`를 각각 사용했다. 이 자료가 대상으로 삼은 MariaDB 실습에서는 대소문자를 구분하지 않는 비교 결과를 관찰한 것으로 적혀 있다. 그렇다고 모든 문자열 비교·모든 DB 설정에서 항상 같다고 일반화하지 않는다. 내 6번 문제의 `(deptno IN (10,20)) AND ename LIKE '%A%'`는 **부서와 이름 조건을 함께** 적용한 실제 풀이이고, 강사님 해당 줄은 문제만 적고 답은 비워 두었다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 163–176행 · **원본 발췌**

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

**발췌 바로 풀이:** 두 원본 모두 `comm = null`을 시험해 보고 `comm IS NULL`과 `comm IS NOT NULL`을 이어서 썼다. `NULL`은 **값이 없음**을 나타내므로 `= NULL`은 참이 되지 않는다. 수당 정보가 없는 행은 `IS NULL`로 찾는다. `comm < 100`도 `NULL` 수당을 가진 행을 포함하지 않는다. `NULL`을 숫자 0과 같은 값으로 읽지 않는다.

내 원본은 S로 시작·N으로 끝·AM 포함·두 번째 L·길이 다섯을 각각 작성했다. %AM% 주석의 “A로 시작하거나…”라는 표현은 실제 조건보다 느슨하다. 실제로는 AM 두 글자가 이어져야 한다. 강사님 답이 비어 있는 부서·이름 결합 문제에는 내 IN과 AND 풀이가 있다. 뒤의 IS NULL 사용과 =NULL 실험은 참인 행만 남기는 WHERE 규칙으로 읽는다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

문자열 값 → 패턴의 위치·길이 판단 또는 NULL 상태 검사 → 조건 결과 → 참인 행의 이름 출력이다. LOWER·UPPER를 쓰면 함수의 반환 문자열을 LIKE 양쪽에 전달하는 구조다. Python 사용자 정의 함수를 import한 코드가 아니라 DB 내장 함수다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 패턴별 의미와 IS NULL 실험을 남겼고 결합 조건도 직접 풀었다. **교정:** AM을 A 또는 M으로 읽거나 NULL을 0으로 읽지 않는다. **조건 의존:** 대소문자는 collation에 따른다. **한계:** 패턴 검색은 의미 검색이 아니며 %는 반드시 한 글자 이상이라는 뜻도 아니다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님 LOWER 한 가지와 내 LOWER·UPPER 두 가지는 대소문자 변환을 비교하는 자료다. 양쪽에 같은 핵심 패턴이 있어 중복 인용을 줄였다. 내 추가 풀이가 있는 문제를 강사님 완성 정답과 비교했다고 꾸미지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 값 | IS NULL | =0 | WHERE에 남을 조건 |
| --- | --- | --- | --- |
| NULL | 참 | 알 수 없음 | IS NULL |
| 0 | 거짓 | 참 | =0 |
| 300 | 거짓 | 거짓 | 해당 두 조건 없음 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 패턴 A% | ADA | 첫 글자 A |
| 패턴 ____ | CARA·ELLA·FINN | 정확히 네 글자 |
| IS NOT NULL | BEN·DAN·FINN | 값 있는 수당 |
| comm IS NULL을 comm=0으로 | 다른 두 행 | 상태와 숫자는 다름 |

결과가 안 나오면 패턴 길이·연속 글자·NULL 여부를 본다. 수당 없음이 안 잡히면 =NULL을 썼는지 확인한다. NOT 조건도 NULL에 자동으로 참이 되지 않으므로 알 수 없음의 의미를 유지한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** %·_ 자체를 검색하는 이스케이프, 이진 비교·상세 collation, 정규식 검색은 추가 학습이다. [LIKE 공식 문서](https://mariadb.com/docs/server/reference/sql-functions/string-functions/like)에 조건을 확인한다. LIKE를 복잡한 정규식 문법과 혼동하지 않는다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. %는 빈 문자열도 허용하는가?
2. _A%의 A는 몇 번째인가?
3. NULL과 0이 같은가?
4. =NULL 조회의 0행은 한 행의 NULL과 같은가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

허용한다. 두 번째다. 다르다. 0행은 결과 행이 없다는 뜻이고 NULL 한 행과 다르다.

</details>

| 질문 | 표현 |
| --- | --- |
| 글자 모양 | LIKE |
| 값 없음 | IS NULL |
| 숫자 0 | =0 |

[장별 연습문제](실습/연습문제/03_SQL_LIKE와_NULL_연습문제.md) · 다음은 [정렬·LIMIT](04_SQL_정렬과_LIMIT.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
