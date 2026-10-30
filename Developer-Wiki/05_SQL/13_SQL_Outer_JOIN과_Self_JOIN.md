# 13. 외부 조인과 자기 조인 — 보존할 대상과 각 표의 역할

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

관리자가 없는 사원도, 사원이 없는 부서도 보고 싶을 수 있다. 일치하는 쌍만 보여 주는 것과 왼쪽 전체를 남기는 것의 차이를 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

LEFT·RIGHT의 보존 방향과 매칭 없는 열의 NULL을 설명한다. 같은 표를 사원·관리자 역할로 나누고 부서당 반드시 한 행이 아니라는 점을 확인한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

내부 조인은 조건에 맞는 쌍을 남긴다. LEFT JOIN은 왼쪽 행을 모두 보존하고 오른쪽에서 맞는 행이 없으면 오른쪽 결과 열을 NULL로 채운다. 일치하는 오른쪽 행이 여러 개면 왼쪽 행도 여러 결과 행으로 조합된다. 왼쪽의 “열을 한 번씩 출력”하는 기능이 아니라 행 보존이다.

| 요구 | 왼쪽 | 오른쪽 | 조건 |
| --- | --- | --- | --- |
| 모든 부서와 사원 | 부서 | 사원 | 부서번호 |
| 모든 사원과 관리자 | 사원 역할 EMP | 관리자 역할 EMP | 사원.mgr=관리자.empno |

자기 조인은 같은 표를 두 역할로 읽는 것이다. 표를 복사해 새 영구 표를 만드는 뜻이 아니다. e는 사원, manager는 관리자처럼 역할 별칭을 붙이면 같은 이름 열의 의미가 드러난다. RIGHT JOIN은 오른쪽을 보존하므로 순서를 바꾸면 보존 대상도 다시 읽어야 한다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB JOIN syntax](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/13_SQL_Outer_JOIN과_Self_JOIN.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT d.deptno, d.dname, e.ename
FROM book_dept d LEFT JOIN book_emp e ON d.deptno=e.deptno
ORDER BY d.deptno,e.empno;
SELECT e.ename AS employee, manager.ename AS manager_name
FROM book_emp e LEFT JOIN book_emp manager ON e.mgr=manager.empno
ORDER BY e.empno;
```

사원이 여럿인 부서20은 세 행, 부서30은 두 행이 된다. 부서40은 사원 없이도 한 행이다. 둘째에서 CARA.mgr은 NULL이라 일치하는 관리자 번호가 없지만 왼쪽 사원이므로 남는다. 같은 book_emp를 별칭 둘로 읽을 뿐 데이터 복제를 한 것은 아니다.

**가상 자료 기준 예상 결과:**

부서 조회는 **7행**이다. 마지막은 40·EMPTY·NULL이며 사원이 없는 부서도 남는다. 관리자 조회는 사원6행, CARA만 관리자 이름 NULL이고 나머지 다섯은 CARA다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 569–585행 · **원본 발췌**

```sql
select * from emp;

select mgr 
from emp
where ename = 'SMITH';

select ename
from emp
where empno = (	select mgr 
				from emp
				where ename = 'SMITH');		
-- 위 코드를 같은 테이블을 동시 조인하여 결과값도 알 수 있다
-- mgr이 null인 것은 빠져서 결과값은 총 14개 중 13개만 나옴
select e2.ename, e1.ename
from emp e1, emp e2
where e1.mgr = e2.empno
and e1.ename = 'SMITH';
```

**발췌 바로 풀이:** 사원의 `mgr`에는 관리자의 `empno`가 들어 있다. `EMP e1`을 사원, `EMP e2`를 관리자로 놓고 `e1.mgr = e2.empno`로 연결한다. 강사님은 사원·관리자 순서로, 나는 관리자·사원 순서로 두 이름을 출력한다. 다만 두 실제 쿼리 모두 `AND e1.ename = 'SMITH'`가 있으므로 **SMITH 한 사람의 연결만** 확인한다. 내 주석의 “14개 중 13개”는 그 `SMITH` 조건이 없는 전체 내부 조인을 상정한 설명이며, 위 문장의 실제 행 수가 아니다. 관리자 번호가 `NULL`인 사원은 전체 내부 조인을 하더라도 빠진다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 615–626행 · **원본 발췌**

```sql
select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	join emp e2 on e1.mgr = e2.empno;

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	left outer join emp e2 on e1.mgr = e2.empno;
	-- left outer는 왼쪽에 있는 column 대상이 한 번은 무조건 나오게 해주는 것

select e1.empno, e1.ename, e2.empno, e2.ename
from emp e1
	right outer join emp e2 on e1.mgr = e2.empno;
```

**발췌 바로 풀이:** 강사님·내 코드 모두 내부 조인, 왼쪽 외부 조인, 오른쪽 외부 조인을 비교한다. `EMP e1 LEFT JOIN EMP e2`는 **왼쪽 `e1`의 모든 사원**을 남긴다. 연결할 관리자가 없으면 오른쪽 관리자 열은 `NULL`이다. `RIGHT JOIN`은 반대로 오른쪽 `e2`의 행을 남긴다. 어느 표를 왼쪽에 두었는지 먼저 읽어야 결과를 예상할 수 있다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 631–638행 · **원본 발췌**

```sql
-- 문제 
-- deptno, dname, empno, ename 출력
-- 모든 부서가 다 나오게 해야 함
-- 부서 번호 별 오름차순, 같다면 이름 오름차순
select d.deptno, dname, empno, ename
from dept d
	left outer join emp e on (d.deptno = e.deptno)
order by deptno asc, ename asc;
```

**발췌 바로 풀이:** “모든 부서”가 요구사항이면 **`DEPT d`를 왼쪽**에 놓고 `LEFT JOIN EMP e`를 한다. 연결되는 사원이 없어도 부서 행은 남고 사원 번호·이름은 `NULL`이다. 강사님은 `USING(deptno)`, 나는 `ON (d.deptno = e.deptno)`를 썼다. 둘 다 부서 번호 오름차순, 이름 오름차순이다. 결과가 부서당 반드시 한 행은 아니다. 사원이 여럿이면 그 부서가 여러 행에 나온다.

내 SMITH 조회는 e1을 사원, e2를 관리자로 두고 e1.ename=SMITH 조건을 포함한다. “14명 중13명” 메모는 그 필터가 없는 전체 내부 자기 조인을 가정한 말이며 실제 해당 쿼리 행 수가 아니다. 실제 초기 SMITH만 조회하면 관리자FORD와 한 쌍이다. 모든 부서 문제는 DEPT를 왼쪽에 두어 요구를 맞췄다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

왼쪽 보존 대상 한 행 → 오른쪽 조건 일치 행들 → 쌍을 만듦 → 없으면 오른쪽 NULL 결과 → 정렬이다. 자기 조인은 사원 행의 mgr → 관리자 역할 행의 empno → 관리자 ename이다. 관리자 자신의 사원정보를 읽는 별칭과 현재 사원의 별칭을 바꿔 쓰지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내부·LEFT·RIGHT를 실제로 비교하고 모든 부서 문제도 풀었다. **교정:** 왼쪽 column을 한 번 보장한다는 주석은 왼쪽 행 보존으로 설명해야 한다. **개수:** 모든 부서가 나온다고 부서 수4와 결과 행 수가 같아지는 것은 아니다. **개선:** 보존 대상·연결 대상·별칭 의미를 먼저 적으면 조인 방향 실수를 줄일 수 있다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님은 USING, 나는 ON을 썼지만 모든 부서를 왼쪽에 둔 핵심은 같다. 같은 정답을 두 번 인용하기보다 결과에서 부서40이 남는 이유와 부서별 여러 행을 추적했다. 관리자·사원 출력 순서는 양쪽 달라 열 이름을 붙이면 읽기 쉽다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 왼쪽 부서 | 일치 사원 수 | 결과 행 수 |
| --- | --- | --- |
| 10 | 1 | 1 |
| 20 | 3 | 3 |
| 30 | 2 | 2 |
| 40 | 0 | 1(NULL 사원) |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| LEFT를 내부 JOIN으로 | 부서40 제외·6행 | 맞는 쌍만 |
| 관리자 LEFT를 내부 JOIN으로 | CARA 제외·5행 | mgr NULL |
| 부서 뒤 WHERE e.sal>2000 추가 | 부서40 제외 | 오른쪽 NULL은 조건 참 아님 |

없어야 할 부서가 사라지면 내부 조인인지, 오른쪽 열 조건이 WHERE에 있는지 본다. 사원과 관리자 이름이 뒤집히면 SELECT 별칭을 확인한다. NULL 표시와 빈 문자열·0은 구별한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** ON의 조건과 WHERE의 조건이 외부 조인에서 만드는 상세 차이, FULL OUTER JOIN 대체는 추가 학습이다. 재귀 계층 탐색은 실제 수업 코드가 있어 18장 본문에서 이어 간다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 모든 부서를 남길 왼쪽 표는?
2. 사원 없는 부서 이름도 NULL이 되는가?
3. 같은 표 별칭 둘은 표를 복사하는가?
4. 왼쪽4부서면 결과도 반드시4행인가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

부서 표다. 왼쪽 부서 이름은 있고 오른쪽 사원 열이 NULL이다. 두 역할로 조회한다. 매칭 수에 따라 여러 행이다.

</details>

| 순서 | 확인 |
| --- | --- |
| 보존 | 왼쪽인가 오른쪽인가 |
| 매칭 | 어떤 키인가 |
| NULL | 어느 쪽이 없었나 |

[장별 연습문제](실습/연습문제/13_SQL_Outer_JOIN과_Self_JOIN_연습문제.md) · 다음은 [DDL·제약](14_SQL_DDL과_제약조건.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
