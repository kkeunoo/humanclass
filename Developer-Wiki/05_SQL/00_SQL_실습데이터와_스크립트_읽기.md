# 00. SQL 실습 데이터와 원본 스크립트 읽기

[SQL 목차](README.md) · [다음: `SELECT`](01_SQL_기초와_SELECT.md)

SQL 코드는 **입력 표가 무엇인지** 모르면 결과를 이해하기 어렵다. 수업 자료에는 `EMP`(사원), `DEPT`(부서), `SALGRADE`(급여 등급)를 만드는 파일이 있다. 이 장은 본문을 읽기 전에 필요한 표의 관계와 스크립트 사용법만 정리한다.

## 먼저: 표의 한 행을 읽기

표는 **열(항목)**과 **행(한 건의 자료)**으로 읽는다. 제공된 초기 자료에서 `DEPT`의 한 행은 다음과 같다. 이것은 원본의 데이터를 읽기 쉽게 줄인 **설명용 표**다.

| DEPTNO | DNAME | LOC |
| --- | --- | --- |
| 10 | ACCOUNTING | NEW YORK |

`DEPTNO=10`은 부서 번호, `DNAME`은 부서 이름이다. 뒤에서 `EMP`의 어떤 사원이 `DEPTNO=10`을 가지면 같은 번호를 통해 이 부서와 연결할 수 있다. 그 연결을 실제 SQL로 작성하는 법은 [12 JOIN](12_SQL_JOIN.md)에서 배우므로 지금은 두 표에 공통 번호가 있다는 것만 확인하자.

<!-- chapter-toc -->

- [1. 표는 어디에서 왔나](00_SQL_실습데이터와_스크립트_읽기.md#section-1)
- [2. 강사님·내 스크립트의 시작](00_SQL_실습데이터와_스크립트_읽기.md#section-2)
- [3. 스크립트는 한 번에 전부 실행하지 않는다](00_SQL_실습데이터와_스크립트_읽기.md#section-3)
- [직접 확인할 질문](00_SQL_실습데이터와_스크립트_읽기.md#section-4)
- [추가로 알면 좋은 것](00_SQL_실습데이터와_스크립트_읽기.md#section-5)

<a id="section-1"></a>

## 1. 표는 어디에서 왔나

출처: `me/workspace_sql/학습용자료/[DB]학습용_emp 신규-mariadb.sql` 1–24행 · **원본 발췌**

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

`EMP.DEPTNO`는 `DEPT.DEPTNO`를 참조한다. 그래서 사원의 부서 번호로 부서 이름을 연결할 수 있다. 제공된 자료는 **부서 4개(10·20·30·40)**를 넣는다. 뒤에 사원 **14명**을 넣으며, `SALGRADE`에는 **급여 등급 5개**가 있다. 초기 자료 기준으로 40번 부서는 사원이 없어 [외부 조인](13_SQL_Outer_JOIN과_Self_JOIN.md)에서 좋은 확인 대상이 된다.

### 실제 입력 예시

출처: `me/workspace_sql/학습용자료/[DB]학습용_emp 신규-mariadb.sql` 26–40행 · **원본 발췌**

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

`EMPNO`는 사원 번호, `ENAME`은 이름, `MGR`은 관리자의 **사원 번호**, `HIREDATE`는 입사일, `SAL`은 급여, `COMM`은 수당, `DEPTNO`는 부서 번호다. 수업 주석에는 `SAL`을 “연봉”이라 부른 부분도 있지만, 이 표의 열 이름과 조회 코드는 `SAL`이라는 급여 값만 제공한다. **월급인지 연봉인지는 표 구조만으로 확정하지 않는다.**

<a id="section-2"></a>

## 2. 강사님·내 스크립트의 시작

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 1–10행 · **원본 발췌**

```sql
-- 주석
/*
범위 주석
*/

select * from emp;
select * from dept;
select * from salgrade;

select 100*12;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 1–31행 · **원본 발췌**

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

두 파일 모두 `EMP`, `DEPT`, `SALGRADE` 조회로 시작한다. 강사님은 첫 문장을 짧게 놓아 표 전체를 먼저 확인하기 쉽다. 내 첫 주석에는 SQL 절의 일반 모양을 미리 적었지만, 그 주석은 **실행 SQL 문장이 아니다**. `SHOW PROCESSLIST`도 조회 학습의 선행 조건은 아니다. 처음 복습할 때는 실제 `SELECT` 세 문장부터 읽는다.

<a id="section-3"></a>

## 3. 스크립트는 한 번에 전부 실행하지 않는다

뒤쪽에는 표를 만들고 지우는 문장, 의도적으로 실패하는 문장, 순서에 따라 결과가 달라지는 변경·롤백 문장이 섞여 있다. `Script.sql`은 **수업 중 작성한 실험 기록**이므로 위에서 아래로 한 번에 실행하는 배포용 파일로 보지 않는다. 이 Wiki도 원본의 문장을 바꾸지 않고, 각 장에서 읽어야 하는 몇 행을 골라 비교한다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `EMP.MGR`은 관리자 이름인가, 관리자 사원 번호인가?
2. 초기 `DEPT`는 몇 부서이고, 그중 사원이 없는 부서는 어느 번호인가?
3. 왜 `Script.sql` 전체를 한 번에 실행하면 안 되는가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

DB를 새로 설치·초기화하는 절차와 운영 데이터 마이그레이션은 현재 수업 코드 비교의 본문 범위를 넘는다. 여기서는 제공된 **입력 표와 두 `Script.sql`을 읽는 기준**만 잡는다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/00_SQL_실습데이터와_스크립트_읽기_연습문제.md) → [01. SELECT](01_SQL_기초와_SELECT.md)
