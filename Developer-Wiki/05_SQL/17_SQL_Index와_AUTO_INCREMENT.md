# 17. 인덱스와 자동 번호 — 찾는 경로와 새 행 식별자 구분

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

인덱스는 값을 찾을 때 활용할 수 있는 별도 구조이고 자동 번호는 새 행의 번호를 부여하는 기능이다. 조회 결과가 같다는 것과 조회가 빨라졌다는 것은 다른 판단이다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

CREATE INDEX·FORCE INDEX의 목적과 측정 한계를 설명한다. AUTO_INCREMENT와 MAX+1 계산을 구분한다. 실제 사용한 LENGTH·CHAR_LENGTH의 단위도 복습한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

책 뒤의 색인은 특정 단어가 어디 있는지 찾도록 돕는다. DB 인덱스도 열의 값을 찾는 경로를 제공하는 구조라는 비유로 이해할 수 있다. 하지만 인덱스를 만들었다고 모든 조회가 그것을 사용하거나 모든 상황에서 빨라지는 것은 아니다. 자료량·조건·다른 비용에 따라 서버가 경로를 고른다.

| 기능 | 목적 | 보장하지 않는 것 |
| --- | --- | --- |
| CREATE INDEX | 조회 경로 준비 | 사용·속도 향상 자동 확정 |
| FORCE INDEX | 경로 선택에 힌트 | 항상 최적 성능 |
| AUTO_INCREMENT | 입력 때 번호 생성 | 끊김 없는 업무 순번 |
| MAX(empno)+1 | 현재 최대+1 계산 | 동시 입력 충돌 방지 |
| LENGTH·CHAR_LENGTH | 바이트·문자 수 | 모든 인코딩에서 같은 값 |

두 사용자가 같은 MAX값을 보고 같은 다음 번호를 계산할 수 있다. AUTO_INCREMENT는 단순 SELECT계산을 대신하는 번호 생성 기능이다. 수업에서는 기본 키로 만들었지만 MariaDB의 요건을 “기본 키일 때만 가능”으로 줄이면 부정확하다. 필요한 키·엔진 조건은 공식 문서를 확인한다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB CREATE INDEX](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-index), [AUTO_INCREMENT](https://mariadb.com/docs/server/reference/data-types/auto_increment), [CHAR_LENGTH](https://mariadb.com/docs/server/reference/sql-functions/string-functions/char_length). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/17_SQL_Index와_AUTO_INCREMENT.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
CREATE INDEX book_idx_dept ON book_emp(deptno);
SELECT ename FROM book_emp WHERE deptno=20 ORDER BY empno;
DROP TEMPORARY TABLE IF EXISTS book_auto;
CREATE TEMPORARY TABLE book_auto (
 empno INT AUTO_INCREMENT PRIMARY KEY, ename VARCHAR(20)
);
INSERT INTO book_auto(ename) VALUES('ADA'),('BEN');
SELECT empno,ename FROM book_auto ORDER BY empno;
SELECT LENGTH('한구'),CHAR_LENGTH('한구');
```

인덱스를 만든 뒤에도 같은 조건의 결과 이름은 같다. 결과가 같다는 사실로 속도 개선을 입증할 수 없다. 자동 번호 표에는 이름만 넣고 번호 열은 생략한다. DB가 번호를 만든다. 마지막은 같은 문자열의 바이트와 문자 단위를 나누는 실제 배운 함수 비교다.

**가상 자료 기준 예상 결과:**

부서20 조회는 **ADA·CARA·ELLA**다. 새 자동 번호 표는 일반적인 증가폭1·시작1 설정에서 **1·ADA / 2·BEN**을 예상한다. 문자열이 UTF-8이고 일반 MariaDB 모드라면 한구는 바이트길이6·문자수2다.

인덱스 생성 뒤 동일 조건의 결과 행만 SQLite에서 교차 확인했다. MariaDB AUTO_INCREMENT·문자셋·접근 경로·속도를 실행 검증하지 않았다. 자동 번호와 한글 길이는 명시한 설정 조건의 예상이다.

**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 881–903행 · **원본 발췌**

```sql
select * from emp
where deptno = 10;

-- index 생성
create index idx_emp_empno_desc
on emp(empno desc);

-- index를 타면 emp (index) 형식으로 표시된다
-- 보통 데이터가 많았을 때 검색 속도가 빨라짐, 최신순은 역순(desc)로 검색하기도 함
select * from emp
order by empno desc;

create index idx_emp_deptno
on emp(deptno);

select * from emp
where deptno = 10;

-- 강제로 index를 타게 할 수 있음
select * 
from emp force index (idx_emp_deptno)
where deptno = 10
order by deptno;
```

**발췌 바로 풀이:** `ON emp(deptno)`는 부서 번호 열에 인덱스를 만든다. `FORCE INDEX (idx_emp_deptno)`는 해당 인덱스를 사용하도록 힌트를 주는 실습이다. 내 주석의 “인덱스를 타면 emp (index) 형식으로 표시”는 **조회 결과 표만 보고 확인할 수 있는 일반 규칙이 아니다**. 이 두 파일에는 `EXPLAIN` 결과가 남아 있지 않다. 데이터가 작은 학습용 `EMP`에서는 인덱스를 만든 후에도 무조건 빨라진다고 말할 수 없다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 911–928행 · **원본 발췌**

```sql
select max(empno)+1 from emp;

-- increment는 Primary Key일때만 가능
-- 아래처럼 함수형태로 만들어서 사용할 수 있다
create table emp_auto (
	empno int auto_increment, -- increment를 사용하면 자동증가 시킬 수 있음
	ename varchar(50),
	
	primary key(empno)
);

insert into emp_auto(ename)
values('근욱');
select * from emp_auto;

insert into emp_auto(ename)
values('근욱2');
select * from emp_auto;
```

**발췌 바로 풀이:** `AUTO_INCREMENT` 열을 지정하면 `INSERT` 때 그 열을 생략하고 새 번호를 받는다. 두 원본 모두 `EMPNO`를 `PRIMARY KEY`로 만든 예제다. 내 주석의 “Primary Key일 때만 가능”은 너무 좁다. MariaDB에서는 자동 증가 열에 필요한 **키 조건**이 있고, 반드시 기본 키여야 하는 것은 아니다. `SELECT MAX(empno)+1`은 수업에서 같이 적어 본 계산이지만, 동시에 여러 입력이 일어나면 같은 다음 번호를 계산할 수 있어 자동 번호와 같은 보장이 아니다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 905–909행 · **원본 발췌**

```sql
-- length로 확인하게 되면 문자열의 Byte가 나옴(한글은 3Byte)
select length('한구');
select length('ab');

select char_length('한구');
```

**발췌 바로 풀이:** 내 코드는 `LENGTH('한구')`와 `CHAR_LENGTH('한구')`를 함께 실행했다. `LENGTH`는 바이트 수, `CHAR_LENGTH`는 문자 수다. 한글이 몇 바이트인지는 **문자 인코딩 설정에 따른다**. 내 주석의 “한 글자는 3Byte”는 이 수업 환경 관찰로 읽는다.

내 파일은 EMPNO와 DEPTNO인덱스를 만들고 FORCE INDEX를 썼다. 실행 계획 결과는 남아 있지 않으므로 “emp(index) 표시” 메모만으로 사용 여부를 확정하지 않는다. 자동 번호를 함수 형태라고 적었지만 CREATE TABLE의 열 속성이다. 내 원본에는 CHAR_LENGTH도 실제로 있어 이 개념을 TIP으로만 내리지 않는다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

표·열 → 인덱스 생성 → 조건 조회의 경로 선택이라는 흐름과, 자동 번호 열 정의 → 그 열을 생략한 INSERT → 번호가 채워진 행 조회라는 흐름을 나눈다. 같은 함수처럼 불러 쓰는 구조가 아니다. 길이 함수는 문자열을 인자로 받아 바이트·문자 개수 값을 반환한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 같은 조회를 인덱스 전후에 놓고 자동 번호를 생략한 입력도 작성했다. **교정:** 생성 사실·사용 사실·성능 개선은 별개다. AUTO_INCREMENT는 사용자 정의 함수가 아니다. **조건:** 한글 한 글자3바이트는 현재 문자셋 조건의 관찰이며 모든 문자·모드에서 고정 규칙이 아니다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 기본 인덱스·자동 번호 구조는 같고 입력 이름만 다르다. 내 CHAR_LENGTH추가 비교는 문자 단위 이해에 도움이 된다. 강사님도 인덱스 속도 측정 결과를 남긴 것은 아니므로 성능 우열의 근거로 삼지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 단계 | 인덱스 | 자동 번호 |
| --- | --- | --- |
| 정의 | 열 경로 생성 | 열의 생성 속성 지정 |
| 사용 | 서버가 조건에 맞는 경로 선택 | 번호 생략 INSERT |
| 결과 | 조건 행 목록 | 번호 포함 새 행 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 부서 조건20→10 | DAN | 필터 값 변경 |
| 자동 번호 이름 하나 추가 | 새 번호 생성 | INSERT추가 |
| LENGTH대상ab | 일반 UTF-8바이트2·문자2 | 영문두글자 |

인덱스 이름이 이미 있으면 같은 연결에서 준비를 반복했는지 확인한다. 번호가 예상1·2가 아니면 현재 표 상태·증가설정을 본다. 빠르다고 느낀 한 번의 실행으로 보편적 성능을 결론내리지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** EXPLAIN·복합/커버링 인덱스·쓰기 비용·실제 시간 측정, 자동 번호 공백·동시성·복제 설정의 상세 의미는 추가 학습이다. [EXPLAIN](https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain)을 참고하되 수업에 측정 결과가 있었다고 쓰지 않는다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 인덱스 만들면 반드시 빠른가?
2. AUTO_INCREMENT는 함수 호출인가?
3. MAX+1이 동시성 충돌을 막는가?
4. LENGTH와 CHAR_LENGTH단위는?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

보장할 수 없다. 열 속성이다. 두 사용자가 같은 값을 계산할 수 있다. 일반 모드 바이트·문자 수다.

</details>

| 구별 | 판단 |
| --- | --- |
| 성능 | 생성·사용·측정 |
| 번호 | 계산·DB생성 |
| 길이 | 바이트·문자 |

[장별 연습문제](실습/연습문제/17_SQL_Index와_AUTO_INCREMENT_연습문제.md) · 다음은 [재귀CTE](18_SQL_Recursive_CTE.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
