# 00. SQL 실습 데이터 — 표의 행·열과 원본 기록 읽기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

SQL의 결과는 문장뿐 아니라 현재 표의 내용에 달려 있다. 먼저 행과 열을 읽고 사원·부서 관계를 그린다. 원본 Script.sql은 학습 기록이므로 처음부터 끝까지 한 번에 실행하는 설치 파일로 취급하지 않는다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

행·열·값·표의 관계를 말로 설명한다. 제공 초기 자료와 변경 후 현재 상태, 새 가상 데이터를 구별한다. 어느 데이터베이스·표를 조회하는지 확인하고 필요한 문장만 읽는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

데이터베이스는 관련 자료를 구조에 맞춰 보관하고 조회하는 곳이다. 수업에서는 관계형 DB의 표를 사용한다. 표의 열은 이름·급여 같은 항목이고 행은 한 사원의 자료다. 한 칸은 특정 행의 특정 열 값이다. SQL은 그 자료에서 원하는 행·열·계산 결과를 요청하는 언어다.

| 용어 | EMP의 예 | 구별할 것 |
| --- | --- | --- |
| 표 | EMP | 화면에 보이는 결과 표와 원본 표 |
| 행 | SMITH라는 사원 한 명 | 같은 이름이 항상 같은 사원이라는 보장 없음 |
| 열 | EMPNO·ENAME·SAL | 열 이름과 실제 값 |
| 식별자 | EMPNO 7369 | 현재 행을 구별하는 번호 |
| 연결 열 | EMP.DEPTNO | 부서 표의 같은 번호와 대응 |

```text
EMP: 사원번호 / 이름 / 부서번호
                    20 ──→ DEPT: 20 / RESEARCH / DALLAS
```

원본 초기 자료는 부서 4개, 사원 14명, 급여 등급 5개다. 40번 부서는 초기 사원이 없다. 제공 SQL의 CREATE는 구조, INSERT는 행을 준비하고, 뒤의 SELECT는 읽는다. 구조·변경 문법은 후반 장에서 다시 다룬다. 아래 작은 가상 표는 그 초기 자료를 그대로 복사한 것이 아니며 이름도 다르다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB SELECT](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/select). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/00_SQL_실습데이터와_스크립트_읽기.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT deptno, dname FROM book_dept ORDER BY deptno;
SELECT empno, ename, deptno FROM book_emp ORDER BY empno;
```

첫 문장은 부서의 번호·이름을 보여 주고 둘째 문장은 사원 번호·이름·부서 번호를 보여 준다. ADA의 20과 BETA 부서의 20을 연결해 읽을 수 있다. 실제로 두 표를 합치는 JOIN은 12장에서 배운다. 같은 번호를 읽는 개념과 조인 실행을 구별한다.

**가상 자료 기준 예상 결과:**

| 부서번호 | 이름 |
| --- | --- |
| 10 | ALPHA |
| 20 | BETA |
| 30 | GAMMA |
| 40 | EMPTY |

두 번째 결과는 사원 6행이다. 사원번호 1–6의 부서번호는 차례로 20·30·20·10·20·30이다. 사원과 부서를 자동으로 합친 결과는 아니다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/학습용자료/[DB]학습용_emp 신규-mariadb.sql` 1–24행 · **원본 발췌**

```sql
USE human;

CREATE TABLE DEPT (
DEPTNO INT(2) PRIMARY KEY,
DNAME VARCHAR(14),
LOC VARCHAR(13)
);

CREATE TABLE EMP (
EMPNO INT(4) PRIMARY KEY,
ENAME VARCHAR(10),
JOB VARCHAR(9),
MGR INT(4),
HIREDATE DATE,
SAL DECIMAL(7,2),
COMM DECIMAL(7,2),
DEPTNO INT(2),
CONSTRAINT FK_DEPTNO FOREIGN KEY (DEPTNO) REFERENCES DEPT(DEPTNO)
);

INSERT INTO DEPT VALUES (10,'ACCOUNTING','NEW YORK');
INSERT INTO DEPT VALUES (20,'RESEARCH','DALLAS');
INSERT INTO DEPT VALUES (30,'SALES','CHICAGO');
INSERT INTO DEPT VALUES (40,'OPERATIONS','BOSTON');
```

**발췌 바로 풀이:** `EMP.DEPTNO`는 `DEPT.DEPTNO`를 참조한다. 그래서 사원의 부서 번호로 부서 이름을 연결할 수 있다. 제공된 자료는 **부서 4개(10·20·30·40)**를 넣는다. 뒤에 사원 **14명**을 넣으며, `SALGRADE`에는 **급여 등급 5개**가 있다. 초기 자료 기준으로 40번 부서는 사원이 없어 [외부 조인](13_SQL_Outer_JOIN과_Self_JOIN.md)에서 좋은 확인 대상이 된다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/학습용자료/[DB]학습용_emp 신규-mariadb.sql` 26–40행 · **원본 발췌**

```sql
INSERT INTO EMP VALUES
(7369,'SMITH','CLERK',7902,STR_TO_DATE('17-12-1980','%d-%m-%Y'),800,NULL,20),
(7499,'ALLEN','SALESMAN',7698,STR_TO_DATE('20-2-1981','%d-%m-%Y'),1600,300,30),
(7521,'WARD','SALESMAN',7698,STR_TO_DATE('22-2-1981','%d-%m-%Y'),1250,500,30),
(7566,'JONES','MANAGER',7839,STR_TO_DATE('2-4-1981','%d-%m-%Y'),2975,NULL,20),
(7654,'MARTIN','SALESMAN',7698,STR_TO_DATE('28-9-1981','%d-%m-%Y'),1250,1400,30),
(7698,'BLAKE','MANAGER',7839,STR_TO_DATE('1-5-1981','%d-%m-%Y'),2850,NULL,30),
(7782,'CLARK','MANAGER',7839,STR_TO_DATE('9-6-1981','%d-%m-%Y'),2450,NULL,10),
(7788,'SCOTT','ANALYST',7566,STR_TO_DATE('13-7-1987','%d-%m-%Y'),3000,NULL,20),
(7839,'KING','PRESIDENT',NULL,STR_TO_DATE('17-11-1981','%d-%m-%Y'),5000,NULL,10),
(7844,'TURNER','SALESMAN',7698,STR_TO_DATE('8-9-1981','%d-%m-%Y'),1500,0,30),
(7876,'ADAMS','CLERK',7788,STR_TO_DATE('13-7-1987','%d-%m-%Y'),1100,NULL,20),
(7900,'JAMES','CLERK',7698,STR_TO_DATE('3-12-1981','%d-%m-%Y'),950,NULL,30),
(7902,'FORD','ANALYST',7566,STR_TO_DATE('3-12-1981','%d-%m-%Y'),3000,NULL,20),
(7934,'MILLER','CLERK',7782,STR_TO_DATE('23-1-1982','%d-%m-%Y'),1300,NULL,10);
```

**발췌 바로 풀이:** `EMPNO`는 사원 번호, `ENAME`은 이름, `MGR`은 관리자의 **사원 번호**, `HIREDATE`는 입사일, `SAL`은 급여, `COMM`은 수당, `DEPTNO`는 부서 번호다. 수업 주석에는 `SAL`을 “연봉”이라 부른 부분도 있지만, 이 표의 열 이름과 조회 코드는 `SAL`이라는 급여 값만 제공한다. **월급인지 연봉인지는 표 구조만으로 확정하지 않는다.**
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 1–31행 · **원본 발췌**

```sql
-- 주석
/* 
여러 줄 주석

EMPNO : 사원번호
MGR : 상사의 EMPNO
HIREDATE : 고용일
SAL : 연봉
COMM : 보너스
DEPTNO : 부서번호

SQL에서는 []를 써도되고 생략도 가능

SELECT [DISTINCT|ALL] 열_리스트
FROM 테이블_리스트
WHERE 검색_조건식
GROUP BY 그룹_기준열_리스트
HAVING 그룹_조건식
ORDER BY { 정열_기준열 [ASC|DESC][.] }
6개의 절로 사용 가능

*/

show processlist;

-- 전체 사원
select * from emp;
-- 부서 별
select * from dept;
-- 연봉 등급표
select * from salgrade; 
```

**발췌 바로 풀이:** 두 파일 모두 `EMP`, `DEPT`, `SALGRADE` 조회로 시작한다. 강사님은 첫 문장을 짧게 놓아 표 전체를 먼저 확인하기 쉽다. 내 첫 주석에는 SQL 절의 일반 모양을 미리 적었지만, 그 주석은 **실행 SQL 문장이 아니다**. `SHOW PROCESSLIST`도 조회 학습의 선행 조건은 아니다. 처음 복습할 때는 실제 `SELECT` 세 문장부터 읽는다.

초기화 자료는 DEPT를 먼저 만들고 EMP의 DEPTNO가 그 번호를 참조하도록 정의한다. 부서를 넣은 뒤 사원을 넣는다. MGR은 관리자의 사원 번호이고 부서 번호가 아니다. 내 SAL 연봉 메모는 당시 해석이며 자료 구조만으로 월·연 단위를 확정할 수 없다. 뒤에서 SAL×12를 계산한 사실도 원래 단위의 확정 근거가 되지 않는다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

학습용 초기화 SQL → EMP·DEPT·SALGRADE의 구조와 값 → 원본 Script.sql의 조회·변경 연습 → 현재 상태 순서다. Python import 함수가 연결되는 구조가 아니라 DB 연결에서 같은 표를 읽고 변경하는 흐름이다. 한 창이라도 연결이나 선택 DB가 다르면 대상을 다시 확인해야 한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 파일 첫 메모에 주요 열의 뜻과 절 순서를 정리해 복습 단서를 남겼다. **교정:** 문법 안내의 대괄호는 선택 항목 표시이며 MariaDB SQL에 무조건 그대로 적는 기호가 아니다. **상태 의존:** 뒤의 UPDATE·DELETE·DROP 같은 문장이 앞에서 본 결과를 바꿀 수 있다. 제공 초기 자료의 14명과 현재 DB 행 수를 같은 것으로 가정하지 않는다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



두 원본은 EMP·DEPT·SALGRADE 조회부터 시작한다. 같은 SELECT를 다시 인용하지 않고 데이터 의미를 먼저 읽는다. 강사님 첫 계산식은 표 없이 숫자 계산을 할 수 있음을 보여 주며 다음 장에서 연결한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 자료 | 초기 제공 상태 | 새 예제 |
| --- | --- | --- |
| 사원 | 14명·SMITH 등 | 6명·ADA 등 |
| 부서 | 4개·ACCOUNTING 등 | 4개·ALPHA 등 |
| 급여 등급 | 5개 | 이번 예제에는 없음 |
| 변경 기록 | Script.sql에 혼재 | 새 임시 자료만 준비 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 조회 열에서 dname 제거 | 부서번호만 표시 | 결과 열 선택 |
| 두 번째 조회에서 ename만 선택 | 이름 6행 | 행 삭제가 아님 |
| 정렬 방향을 DESC로 | 번호 내림차순 | 표시 순서 변경 |

표가 없다는 오류면 선택 DB·준비문 실행·같은 연결인지 확인한다. 행 수가 다르면 원본 초기 자료인지 변경된 자료인지 본다. 원본 전체 실행 오류 뒤 어느 상태가 남았는지 모르겠으면 무작정 다음 문장을 실행하지 말고 실제 표 상태부터 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 임시 표는 현재 연결에서 예제를 분리하기 위한 새 장치다. DB 설치·접속 권한·백업·운영 배포, 스키마 설계의 상세 정규화는 추가 학습이다. 실제 수업 데이터 초기화문과 이 교재 임시 표 준비문을 구별한다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. MGR은 부서 번호인가?
2. 제공 초기 사원 수와 새 예제 사원 수는?
3. 문법 안내 대괄호를 그대로 SQL에 모두 넣는가?
4. SELECT가 화면에 두 열만 보이면 나머지 열은 삭제되는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

관리자의 사원 번호다. 14명과 6명이다. 선택 문법 표기를 실제 기호와 구별한다. 조회 결과에 표시하지 않을 뿐 삭제하지 않는다.

</details>

| 먼저 볼 것 | 확인 |
| --- | --- |
| 대상 | DB·표·연결 |
| 상태 | 초기·변경 후·가상 자료 |
| 의미 | 열의 이름과 실제 단위 |

[장별 연습문제](실습/연습문제/00_SQL_실습데이터와_스크립트_읽기_연습문제.md) · 다음은 [SELECT](01_SQL_기초와_SELECT.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
