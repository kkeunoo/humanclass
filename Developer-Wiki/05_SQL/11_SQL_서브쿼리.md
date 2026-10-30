# 11. 서브쿼리 — 안쪽 결과의 모양을 바깥에서 사용하기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

전체 평균을 먼저 구해 그보다 높은 급여의 사원을 찾는다. 안쪽 조회가 값 하나인지 여러 행인지, 임시 결과 표인지에 따라 바깥에서 쓰는 방식이 달라진다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

스칼라·여러 값 IN·FROM 안 조회의 역할을 설명한다. 부서별 최대 급여 값 목록과 자기 부서 최고 급여 사원을 구분한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

서브쿼리는 다른 SQL 문장 안에 들어간 조회다. > 오른쪽처럼 값 하나가 필요한 자리에는 한 열·한 행의 결과가 맞아야 한다. IN은 여러 후보 값 중 같은 값이 있는지 검사한다. FROM 안의 조회는 그 결과를 표처럼 바깥 조회 대상으로 사용한다.

| 위치 | 결과 모양 | 예 |
| --- | --- | --- |
| sal > (SELECT AVG...) | 한 값 | 전체 평균과 비교 |
| sal IN (SELECT MAX... GROUP BY...) | 한 열 여러 행 | 최대 급여 값 목록과 비교 |
| FROM (SELECT...) 별칭 | 여러 열·행 | 요약 결과를 다시 필터 |

“서브쿼리는 여러 줄이면 안 된다”는 원본 주석은 모든 경우의 규칙이 아니다. 값 하나가 필요한 자리와 여러 후보를 받는 자리를 구분해야 한다. 읽을 때 안쪽 결과를 먼저 적는 방법은 이해를 위한 것이고 실제 서버가 무조건 안쪽 전체를 먼저 실행한다는 뜻은 아니다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB Subqueries](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries), [Scalar Subqueries](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-scalar-subqueries). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/11_SQL_서브쿼리.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
INSERT INTO book_emp VALUES (7,'GUS','CLERK',3,1600,NULL,20);
```

표 생성·삽입 문법은 14·15장에서 설명한다. TEMPORARY는 원래 수업 구문으로 승격한 것이 아니라 예제 자료를 연결 안에서만 쓰기 위한 새 실행 장치다. 기존 영구 EMP·DEPT를 바꾸는 준비문이 아니다. 임시 표의 상세 수명·권한은 아래 TIP에서 구별한다.

</details>

```sql
SELECT ename, sal FROM book_emp
WHERE sal > (SELECT AVG(sal) FROM book_emp) ORDER BY empno;
SELECT ename, sal, deptno FROM book_emp
WHERE sal IN (SELECT MAX(sal) FROM book_emp GROUP BY deptno) ORDER BY empno;
SELECT deptno, avg_sal FROM (
 SELECT deptno, AVG(sal) AS avg_sal FROM book_emp GROUP BY deptno
) summary WHERE avg_sal >= 2000 ORDER BY deptno;
```

전체 급여13000을 7로 나눈 평균 약1857.14보다 큰 사람은 CARA·ELLA다. 부서별 최대 값은 1300·3000·1600이다. GUS는 20번의 최고3000보다 적지만 30번의 최고1600과 같아 둘째 결과에 들어온다. 이것이 “최대 값 목록 중 하나”와 “자기 부서 최고”의 차이다. 마지막은 부서 평균 표를 안쪽에서 만들고 그 결과의 avg_sal을 바깥 WHERE에서 검사한다.

**가상 자료 기준 예상 결과:**

이번 준비 자료만 GUS 한 명을 추가하여 **7명**이다. 첫 결과 CARA·ELLA, 둘째 BEN·CARA·DAN·ELLA·GUS, 셋째 20번 부서·평균2150이다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 450–462행 · **원본 발췌**

```sql
select sal 
from emp
where ename = 'WARD'

-- 서브쿼리로 중첩해서 사용할 수 있음
select * from emp
where sal > (select sal 
			 from emp
			 where ename = 'WARD');

-- 서브쿼리에서 column이 두개이거나, 여러 줄이면 안 됨
select * from emp
where sal > (select avg(sal) from emp);
```

**발췌 바로 풀이:** 안쪽 `SELECT sal FROM emp WHERE ename = 'WARD'`가 WARD의 급여를 구하고, 바깥 `WHERE sal > (...)`가 그보다 급여가 높은 사원을 찾는다. `AVG(sal)`도 전체 평균 **한 값**을 돌려 주므로 `>` 오른쪽에 넣을 수 있다. 내 주석 “서브쿼리는 여러 줄이면 안 됨”은 이 **한 값 비교 연산자**의 경우에만 해당한다. 다음 `IN`에서는 여러 행을 쓸 수 있다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 464–480행 · **원본 발췌**

```sql
-- 부서 별 최고 연봉자
-- 1. 부서 별 최고 연봉을 뽑아라
select max(sal)
from emp
group by deptno;

-- 아래처럼 서브쿼리로 넣어 한 번에 처리할 수 있음
select ename, sal
from emp
-- where sal = 3000 or sal = 2850 or sal = 5000;
where sal in (3000, 2850, 5000);

select ename, sal
from emp
where sal in (  select max(sal)
				from emp
			  	group by deptno);
```

**발췌 바로 풀이:** 안쪽 `GROUP BY deptno`는 **부서별 최대 급여 값들**을 만든다. 바깥 `sal IN (...)`은 그 값 중 하나와 같은 급여의 사원을 고른다. 이 코드는 “자기 부서에서 최고 급여인 사원”과 **완전히 같은 조건은 아니다**. 다른 부서의 최고 급여와 우연히 같은 급여를 받는 사원도 들어올 수 있기 때문이다. 실제 작성한 풀이의 한계를 본문에서 분명히 한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 502–524행 · **원본 발췌**

```sql
-- having 없이 서브쿼리로 해결
-- 1. 부서 별 평균 연보 출력
select avg(sal)
from emp
group by deptno;
-- 2. 부서 별 평균 연봉이 2000이상인 부서만 출력
select avg(sal) avg_sal
from emp
-- where avg_sal >= 2000 → 사용 불가하며, select 이후(group by)에 사용 가능
-- where avg(sal) >= 2000 → 집계함수는 사용 불가능
group by deptno
having avg(sal) >= 2000;

-- 서브쿼리 사용
-- from 에 서브쿼리를 넣었을 때 별칭 필요
-- 위에 having 사용한 것을 from에 넣어 사용할 수 있음
select *
from (
	select avg(sal) avg_sal
	from emp
	group by deptno
) a
where avg_sal >= 2000;
```

**발췌 바로 풀이:** 먼저 부서별 평균을 만든 결과를 임시 결과처럼 `FROM (...) a`에 놓고, 바깥에서 `avg_sal >= 2000`을 검사한다. 같은 목표를 `HAVING AVG(sal) >= 2000`으로 더 짧게 쓸 수 있다. **강사님 코드가 간결한 부분**은 바로 `HAVING` 버전이다. 하지만 `FROM` 서브쿼리도 실제 수업에서 배운 방식이므로 본문에 남긴다. 두 코드 모두 평균만 출력해 부서 번호가 보이지 않는다. “어느 부서인가”까지 보려면 그룹 기준도 결과 열로 함께 출력해야 한다.

내 원본은 WARD 급여·전체 평균·부서별 최대 값·FROM 안 평균 결과를 작성했다. 원본 초기 WARD급여는1250이지만 이름 열이 일반적으로 유일하다고 보장하지는 않는다. 부서별 MAX를 sal IN에 넣는 풀이에는 부서 번호 대응이 없어 다른 부서 최대와 같은 급여도 포함될 수 있다. FROM 안 별칭은 바깥에서 읽을 결과 표의 이름이다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

안쪽 결과 한 값·후보 목록·결과 표 → 바깥 연산자·FROM이 요구하는 모양 → 최종 조건이다. 별칭 summary의 avg_sal은 안쪽에서 생성한 결과 열이라 바깥 WHERE에서 읽는다. 같은 SELECT 단계의 집계 값을 WHERE에 바로 쓰는 문제와 다르다. 원본 첫 조회의 세미콜론이 없으면 편집기 실행 범위에 따라 다음 SELECT와 붙을 수 있어 문장 경계도 확인한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 먼저 독립 조회로 값을 확인한 다음 괄호 안에 넣어 연결했다. **한계:** sal만 대응한 IN으로 자기 부서 최고를 완전히 표현하지 못한다. **새 반례:** GUS를 추가해 현재 제공 데이터에서는 숨을 수 있는 문제를 보여 준다. **개선 방향:** 12장 JOIN을 배운 뒤 부서번호와 최대급여 두 조건을 함께 연결한다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 원본에 같은 sal IN 한계가 있다. 강사님 코드도 자동 정답으로 삼지 않고 요구를 기준으로 평가한다. 이 위치에서는 같은 긴 쿼리를 두 번 붙이기보다 새 반례로 부족한 대응 조건을 분명히 했다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 부서 | 최고 급여 | GUS와 관계 |
| --- | --- | --- |
| 10 | 1300 | 다름 |
| 20 | 3000 | 자기 부서 최고는 아님 |
| 30 | 1600 | 다른 부서 값과 같음 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| GUS 급여를 1599로 | 둘째에서 제외 | 최대 값 목록에 없음 |
| 비교 >를 >=로 | 평균과 같은 값 있을 때 포함 | 경계 변경 |
| 바깥 평균기준2150으로 | 20번 유지 | >= 경계 포함 |

스칼라 자리에서 여러 행이 나오면 안쪽 조회를 따로 실행해 모양을 본다. MariaDB 다중 행 오류를 SQLite의 관대한 동작으로 대신 검증하지 않는다. 자기 그룹 최고가 아닌 사람이 나오면 값뿐 아니라 그룹 키도 대응했는지 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** EXISTS·다중 열 비교·서브쿼리 최적화의 상세 응용은 추가 학습이다. 상관 서브쿼리는 실제 시험 풀이에 있으므로 [원본 문제 비교](실습_SQL_원본문제_비교.md) 본문에서 바깥 사원과 같은 부서 평균을 구하는 흐름으로 설명한다. [JOIN](12_SQL_JOIN.md)에서는 최대 급여의 부서 키 대응을 이어 본다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 모든 서브쿼리는 한 행이어야 하는가?
2. 새 GUS가 둘째 결과에 들어오는 이유는?
3. FROM 안 조회 별칭은 무엇인가?
4. 강사님과 같은 풀이면 요구를 항상 만족하는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

사용 위치에 따라 다르다. 다른 부서 최대급여1600과 같아서다. 조회 결과를 표처럼 읽는 이름이다. 요구와 반례로 따로 검토해야 한다.

</details>

| 읽는 순서 | 확인 |
| --- | --- |
| 안쪽 | 한 값·후보·표 |
| 바깥 | 연산자가 받는 모양 |
| 대응 | 그룹 키가 빠졌나 |

[장별 연습문제](실습/연습문제/11_SQL_서브쿼리_연습문제.md) · 다음은 [JOIN](12_SQL_JOIN.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
