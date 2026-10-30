# 01. SELECT — 원본 자료에서 결과의 열을 고르기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

SELECT는 저장된 자료를 바꾸지 않고 읽는 조회의 출발점이다. 별표·열 이름·계산식·별칭·중복 제거가 각각 결과를 어떻게 바꾸는지 나누어 본다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

결과 행과 열을 구별한다. DISTINCT가 적용되는 열 조합과 결과 별칭의 의미를 설명한다. 계산 결과가 원본 열을 변경하는 대입은 아니라는 점을 확인한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

SELECT는 결과에 보여 줄 열이나 식을 선택한다. FROM은 그 값을 읽을 표를 지정한다. SELECT 100*12처럼 표 없이 계산할 수도 있다. SELECT *의 별표는 모든 열을 요청하는 표시이고, sal*12 안의 별표는 곱셈이다.

| 문장 요소 | 역할 | 원본 표 변경 |
| --- | --- | --- |
| 열 이름 | 지정 열 표시 | 없음 |
| * | 모든 열 요청 | 없음 |
| 계산식 | 결과 값 계산 | 없음 |
| AS 별칭 | 결과 열의 이름 | 없음 |
| DISTINCT | 선택 결과 중복 제거 | 없음 |

DISTINCT deptno, job은 부서만 중복 제거하는 것이 아니라 두 값의 조합이 같은 결과 행을 한 번씩 보여 준다. 원본에서 중복 사원을 지우는 DELETE가 아니다. AS는 결과 표의 표시 이름이며 영구 열 이름을 변경하는 DDL도 아니다. 이름에 공백이 없다면 읽기 쉬운 별칭을 줄 수 있다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB SELECT](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/select). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/01_SQL_기초와_SELECT.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT 100 * 12 AS calculated;
SELECT empno, ename, sal * 12 AS scaled_sal FROM book_emp ORDER BY empno;
SELECT DISTINCT job FROM book_emp ORDER BY job;
```

첫 SELECT는 표를 읽지 않고 계산한다. 둘째는 각 사원 행의 급여를 12배해 scaled_sal 열로 표시한다. 셋째는 같은 직업을 한 번씩 보여 주며 사원 수가 줄어 저장된 것은 아니다. 원래 급여의 기간 단위를 정하지 않았으므로 scaled_sal을 무조건 연봉이라 부르지 않는다. 정렬은 결과를 재현하기 위해 덧붙였고 04장에서 자세히 배운다.

**가상 자료 기준 예상 결과:**

첫 결과: **1200**. 둘째 결과: 사원 6행, 계산값은 12000·19200·36000·15600·36000·18000. 마지막 결과: ANALYST·CLERK·MANAGER·SALESMAN 네 직업이다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 26–33행 · **원본 발췌**

```sql
-- 전체 사원
select * from emp;
-- 부서 별
select * from dept;
-- 연봉 등급표
select * from salgrade; 

select empno from emp;
```

**발췌 바로 풀이:** `SELECT * FROM emp`는 `EMP`의 모든 열을 요청한다. `SELECT empno FROM emp`는 사원 번호만, `SELECT empno, ename FROM emp`는 사원 번호와 이름만 보여 준다. 강사님은 `select 100*12`도 실행해 표 없이 식의 계산 결과만 볼 수 있음을 보였다. **`*`와 특정 열의 차이**가 첫 학습 목표다. 열 이름과 행의 실제 값은 초기화 자료나 현재 데이터에 따라 확인한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 47–65행 · **원본 발췌**

```sql
select job from emp;
-- distinct로 중복 결과를 하나만 보이게 할 수 있다
select distinct job from emp; 

-- as로 가져오는 열 리스트의 이름을 변경할 수 있음
select job as 직업 from emp;
-- as로 띄어쓰기가 포함되는 경우 ''는 필수로 사용해야 함
select job as '직업 이름' from emp;
-- as도 생략이 가능하다
select job '직업 이름' from emp;

-- select에서 사칙연산을 이용하면 해당 값도 볼 수 있음
select sal, sal*12 from emp;

-- select에 바로 대입해도 값은 나오게 할 수 있음
select 100*12;

-- 기존 NULL에는 더하거나 빼도 NULL로 유지됨
select sal, comm , sal + comm from emp;
```

**발췌 바로 풀이:** `job`만 출력하면 같은 직업 이름이 여러 행에 나온다. `DISTINCT job`은 **조회 결과의 중복**을 제거하며 원본 표를 삭제하거나 변경하지 않는다. `AS 직업`은 결과 열의 표시 이름을 바꾼다. `sal*12`는 급여에 12를 곱한 계산 열이다. `sal + comm`은 `comm`이 `NULL`이면 결과도 `NULL`이 될 수 있다. `NULL` 처리 방법은 [08 숫자·날짜·NULL 함수](08_SQL_숫자_날짜_NULL함수.md)에서 다시 본다.

내 원본은 전체 표·특정 열 조회 뒤 job 중복·별칭·계산을 이어 썼다. sal+comm에서 COMM이 NULL이면 합도 NULL이 된다는 메모가 있다. 결과 열을 고르는 일과 각 행의 계산을 구별하면 한 문장에서 무엇이 달라졌는지 설명할 수 있다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

FROM emp에서 대상 자료를 읽는다고 생각하고 SELECT의 열·식으로 결과의 모양을 만든다. 이는 이해를 위한 논리적 흐름이며 서버의 물리 실행 순서를 고정한 설명이 아니다. 다른 파일에서 가져온 함수는 없고 SUM 같은 집계와 일반 계산식 차이는 05장에서 다룬다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** DISTINCT 전후와 AS 유무를 실제로 비교했다. **교정:** 공백 별칭에 작은따옴표가 언제나 유일하게 가능한 표기라는 메모는 좁은 설명이다. 이 수업 MariaDB 예문에서는 그 표기를 사용했으며 식별자 인용 방식의 상세 차이는 TIP으로 둔다. **설계 선택:** *는 빠른 탐색에 편하고 필요한 열 명시는 반환 구조를 읽기 쉽게 한다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님과 내 핵심 SELECT가 같아 중복 인용하지 않는다. 양쪽 모두 job과 DISTINCT job을 이어 놓았다. 이전 해설처럼 내 코드만 비교가 불가능하게 한꺼번에 배치했다고 평가할 근거는 없다. 새 교재는 별칭·중복·계산을 각각 한 가지 변화로 읽게 분리했다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 새 예제 변화 | 결과 행 | 결과 의미 |
| --- | --- | --- |
| 사원 열 조회 | 6 | 사원별 값 |
| job만 조회 | 6 | 직업 중복 포함 |
| DISTINCT job | 4 | 직업 종류 |
| sal*12 | 6 | 각 행 계산 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| DISTINCT 제거 | job 6행 | 중복 허용 |
| 곱하기 12를 2로 | 계산 열만 변경 | 원본 sal 불변 |
| 별칭을 annual_value로 | 표시 이름만 변경 | 값 계산은 동일 |

열을 못 찾으면 실제 표의 열 이름을 확인한다. DISTINCT 뒤 행 수가 예상과 다르면 선택한 열 조합 전체를 본다. 원본 sal이 바뀌었을 것으로 생각하지 말고 SELECT 결과와 UPDATE 변경을 구별한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 식별자 인용과 별칭을 다른 절에서 사용할 수 있는 범위, SELECT *와 스키마 변경의 관계, 실행 계획은 추가 학습이다. [SELECT 공식 문서](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/select)에서 현재 DB 문법을 확인한다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. SELECT sal*12는 sal을 저장 변경하는가?
2. DISTINCT job은 사원을 삭제하는가?
3. DISTINCT deptno, job은 어떤 단위로 중복을 판단하는가?
4. 별칭은 원래 열 이름을 바꾸는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

아니다. 조회 계산이다. 사원을 삭제하지 않는다. 두 열 값의 조합 전체다. 별칭은 결과 이름이다.

</details>

| 표현 | 역할 |
| --- | --- |
| FROM | 대상 |
| SELECT | 표시할 열·식 |
| DISTINCT | 결과 중복 제거 |
| AS | 결과 이름 |

[장별 연습문제](실습/연습문제/01_SQL_기초와_SELECT_연습문제.md) · 다음은 [WHERE](02_SQL_WHERE와_조건연산자.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
