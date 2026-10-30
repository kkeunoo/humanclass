# SQL 실제 문제 — 요구 문장의 대상·범위·빈 그룹을 코드로 옮기기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

이 장은 강사님 문제와 내가 실제 작성한 풀이를 다룬다. 새 종합 프로젝트와 구별하고, 답을 외우기보다 요구에서 빠진 조건과 빈 결과 반례를 찾아본다. 현재 원본에서 이동한 행 번호도 다시 대조했다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

연도 안팎 조건·부서별 급여차·기준 사원 조회·모든 등급 집계·등급과 부서 조건·자기 부서 평균의 실제 풀이를 설명한다. 강사님과 내 코드의 장단점을 요구 기준으로 판단한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

문제를 읽을 때 대상·범위·출력·정렬을 나눠 적는다. “1981년 입사자 중 최저 급여자”는 안쪽에서 1981년의 최저 급여를 구하는 것과, 바깥에서 1981년 사원을 고르는 것이 모두 필요하다. 다른 연도에 같은 급여를 받는 사람이 있을 수 있기 때문이다.

| 요구 표현 | 코드에서 확인 |
| --- | --- |
| ~중 | 안쪽 계산과 바깥 출력의 대상 범위 |
| 부서별 | GROUP BY의 부서 키 |
| 모든 등급 | 등급을 보존하는 외부 조인 |
| 사원 수 | 빈 조인 행이 아닌 실제 사원 키 COUNT |
| 같은 부서 평균 | 바깥 부서 번호와 안쪽 부서 번호 대응 |
| 내림차순·동점 | ORDER BY의 각 열 방향 |

상관 서브쿼리는 안쪽 조회가 바깥 행의 값을 참조하는 형태다. 현재 사원의 부서 번호를 기준으로 같은 부서 평균을 구한다. 전체 평균 한 값을 모든 사원에게 공통으로 비교하는 것과 다르다. 내 시험 원본에 실제로 있으므로 이를 미학습 TIP으로 내리지 않는다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB Correlated Subqueries](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/correlated-subqueries), [COUNT](https://mariadb.com/docs/server/reference/sql-functions/aggregate-functions/count). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/실습_SQL_원본문제_비교.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
DROP TEMPORARY TABLE IF EXISTS book_grade;
CREATE TEMPORARY TABLE book_grade(grade INT PRIMARY KEY,losal INT,hisal INT);
INSERT INTO book_grade VALUES(1,0,1200),(2,1201,2000),(3,2001,4000),(4,4001,9999);
DROP TEMPORARY TABLE IF EXISTS book_year;
CREATE TEMPORARY TABLE book_year(ename VARCHAR(10),hiredate DATE,sal INT);
INSERT INTO book_year VALUES('A','1981-02-01',1000),('B','1980-02-01',1000),('C','1981-03-01',1500);
```

표 생성·삽입 문법은 14·15장에서 설명한다. TEMPORARY는 원래 수업 구문으로 승격한 것이 아니라 예제 자료를 연결 안에서만 쓰기 위한 새 실행 장치다. 기존 영구 EMP·DEPT를 바꾸는 준비문이 아니다. 임시 표의 상세 수명·권한은 아래 TIP에서 구별한다.

</details>

```sql
SELECT ename FROM book_year WHERE sal=(
 SELECT MIN(sal) FROM book_year WHERE hiredate BETWEEN '1981-01-01' AND '1981-12-31'
) ORDER BY ename;
SELECT ename FROM book_year WHERE sal=(
 SELECT MIN(sal) FROM book_year WHERE hiredate BETWEEN '1981-01-01' AND '1981-12-31'
) AND hiredate BETWEEN '1981-01-01' AND '1981-12-31' ORDER BY ename;
SELECT g.grade,COUNT(*) AS joined_rows,COUNT(e.empno) AS people
FROM book_grade g LEFT JOIN book_emp e ON e.sal BETWEEN g.losal AND g.hisal
GROUP BY g.grade ORDER BY g.grade;
SELECT e.ename,e.sal FROM book_emp e
WHERE e.sal>(SELECT AVG(other.sal) FROM book_emp other WHERE other.deptno=e.deptno)
ORDER BY e.empno;
```

첫 반례의 B는 1980년 입사지만 1981년 최저 1000과 같아서 잘못 포함된다. 두 번째 쿼리가 바깥 연도를 더 검사해 제외한다. 빈 등급 4는 외부 조인으로 남은 한 행을 COUNT(*)가 1로 세지만 사원 키는 NULL이라 COUNT(e.empno)는 0이다. 마지막 쿼리는 현재 e의 deptno를 안쪽 other.deptno와 맞춰 각 부서 평균을 계산한다. 이들은 원본 초기 자료와 다른 새 반례다.

**가상 자료 기준 예상 결과:**

연도조건을 안쪽에만 쓰면 **A·B**, 바깥에도 쓰면 **A**다.

| 등급 | 조인 결과 행 수 COUNT(*) | 실제 인원 COUNT(e.empno) |
| --- | --- | --- |
| 1 | 1 | 1 |
| 2 | 3 | 3 |
| 3 | 2 | 2 |
| 4 | 1 | 0 |

자기 부서 평균 초과는 **BEN1600·CARA3000·ELLA3000**이다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 1060–1073행 · **원본 발췌**

```sql
-- 문제1 최종풀이
select ename, sal, hiredate 
from emp
where sal = (	select min(sal)
				from emp
				where substr(HIREDATE, 1, 4) = '1981');

-- 문제1 개선풀이
select ename, sal, hiredate 
from emp
where sal = (	select min(sal)
				from emp
				where hiredate 
					between date '1981-01-01' and date '1981-12-31');
```

**발췌 바로 풀이:** 현재 1060행부터다. 내 두 풀이 모두 안쪽에서 연도를 제한하지만 바깥 연도가 빠졌다. 제공 초기 자료에서 결과가 같더라도 새 반례로 조건 누락을 확인할 수 있다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 1075–1089행 · **원본 발췌**

```sql
-- 문제2 _ 각 부서별 급여가 가장 높은 사원과, 가장 낮은 사원의 차이를 조회하시오.
-- 부서명, 차이 금액 출력
select * from emp e;
select * from dept;

-- 문제2 최종풀이
select d.dname, max(e.sal) - min(e.sal) as salCalc
from emp e join dept d using(deptno)
group by d.deptno, d.dname;

-- 문제2 각 부서별? 빈 부서도 포함해보기
select d.dname, max(e.sal) - min(e.sal) as salCalc
from dept d 
	left outer join emp e using(deptno)
group by d.deptno, d.dname;
```

**발췌 바로 풀이:** 두 기본 풀이 모두 부서별로 묶어 `MAX(sal) - MIN(sal)`을 구한다. 내 추가 풀이에서는 `DEPT`를 왼쪽에 둔 `LEFT JOIN`으로 **사원이 없는 부서**도 결과에 남긴다. 이때 급여가 전혀 없으면 차이 계산은 `NULL`이며 0이라고 단정하지 않는다. 강사님 기본 풀이와 내 첫 풀이의 `EMP` 출발은 사원 없는 부서를 표시하지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 1109–1129행 · **원본 발췌**

```sql
-- 문제3 _ BLAKE보다 높은 연봉을 받는 사람들 출력
select * from emp;

select sal from emp
where ename = 'BLAKE';

-- 문제3 최종풀이
select ename, sal from emp
where sal > (	select sal from emp
				where ename = 'BLAKE');

-- 문제4 _ JONES와 같은 JOB을 가진 사람들을 출력
select * from emp;

select job from emp
where ename = 'JONES';

-- 문제4 최종풀이
select ename, job from emp
where job = (	select job from emp
				where ename = 'JONES');
```

**발췌 바로 풀이:** 각 문제에서 안쪽 조회로 BLAKE의 `SAL`, JONES의 `JOB`을 먼저 얻고 바깥 조건에서 비교한다. 두 원본의 핵심 조건은 같다. 나는 결과 열을 `ENAME, SAL` 또는 `ENAME, JOB`으로 좁혔고, 강사님은 `SELECT *`로 전체 열을 봤다. 답을 설명할 때는 **문제가 요구한 열만 보이는 내 코드**가 결과를 읽기 쉽다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 1131–1141행 · **원본 발췌**

```sql
-- 문제5 _ 급여 등급 별 사원 수를 등급 오름차순으로 정렬
-- 단, 모든 등급을 표시한다 (몇 등급에 몇 명)
select * from emp;
select * from salgrade;

-- 문제5 최종풀이
select s.grade, count(e.ENAME) as gradeCount
from salgrade s left outer join emp e
on (e.sal between s.losal and s.hisal)
group by s.grade
order by s.grade asc;
```

**발췌 바로 풀이:** 모든 등급을 왼쪽에 두고 COUNT(e.ENAME)으로 실제 이름을 센다. 초기 자료에서 이름은 값이 있지만 일반적으로 사원 수는 NULL이 불가능한 식별 키를 세면 더 명확하다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 1157–1168행 · **원본 발췌**

```sql
-- 문제6 개선
select e.ename, e.sal, s.grade, d.dname
from emp e 
	join dept d
		on (e.deptno = d.deptno)
	join salgrade s
		on (e.sal between s.losal and s.hisal)
where s.grade >= 3
order by 
	s.grade desc, 
	e.sal desc, 
	e.ename desc; 
```

**발췌 바로 풀이:** 나는 `EMP → DEPT → SALGRADE`를 각각 `JOIN ... ON`으로 분리해 연결했다. 강사님은 `SALGRADE`를 왼쪽에 놓고 `LEFT JOIN`을 썼다. `WHERE s.grade >= 3`은 **등급 표의 값**을 검사하므로, 해당 등급에 사원이 없어도 사원 이름이 `NULL`인 행이 남을 수 있다. 문제는 실제 사원 이름을 조회하므로 내 `JOIN` 풀이가 대상 행을 더 정확히 고르고 연결 조건도 읽기 쉽다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 1170–1189행 · **원본 발췌**

```sql
-- 문제7 _ 부서명이 SALES인 사원 중, 급여 등급이 2또는 3인 사원을 급여 내림차순으로 정렬
select * from emp;
select * from dept;

-- 문제7 최종풀이
select e.ename, e.sal, s.grade, d.dname
from emp e join dept d join salgrade s on (e.deptno = d.deptno) and (e.sal between s.losal and s.hisal)
where d.dname = 'SALES' and (s.grade = 2 or s.grade = 3)
order by e.sal desc;

-- 문제7 개선
select e.ename, e.sal, s.grade, d.dname
from emp e 
	join dept d 
		on (e.deptno = d.deptno)
	join salgrade s
		on (e.sal between s.losal and s.hisal)
where d.dname = 'SALES' 
	and (s.grade = 2 or s.grade = 3)
order by e.sal desc;
```

**발췌 바로 풀이:** 두 코드는 모두 SALES 부서에서 급여 등급 2·3인 사원을 급여 내림차순으로 출력한다. 내 풀이에는 한 줄 `JOIN` 버전과 각 관계를 나눠 쓴 “개선” 버전이 **둘 다 실제 원본에 있다**. 초보자에게는 `EMP.DEPTNO = DEPT.DEPTNO`와 `EMP.SAL BETWEEN LOSAL AND HISAL`을 각각 보이는 개선 버전이 더 읽기 좋다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 1220–1232행 · **원본 발췌**

```sql
select e.ename, d.dname, e.sal, (
	select round(avg(e2.sal),0)
	from emp e2
	where e2.deptno = e.deptno
) as salAvg
from dept d
join emp e on e.deptno = d.deptno
where e.sal > (
	select avg(e2.sal)
	from emp e2
	where e2.deptno = e.deptno
)
order by d.dname, e.sal desc;
```

**발췌 바로 풀이:** 바깥 e의 부서 번호를 안쪽 e2가 참조한다. 표시 평균만 ROUND하고 비교에는 원래 AVG를 쓴다. 표시용 반올림 때문에 판정 기준을 바꾸지 않는 장점이다.

| 실제 문제 | 내 코드와 비교 판단 |
| --- | --- |
| 1981년 최저 | 바깥 연도 조건 누락·강사님은 두 범위 적용 |
| 부서 최고−최저 | 기본 집계 같음·내 추가 LEFT는 빈 부서도 표시하며 차이는 NULL |
| BLAKE 급여·JONES 직업 | 안쪽 기준 값과 바깥 비교 같음·내 출력 열 명시 |
| 모든 등급 사원 수 | 내 COUNT(이름)이 빈 등급 0 처리에 더 적합 |
| 등급 3 이상 사원 | 내 내부 조인은 실제 매칭 사원 대상·강사님 LEFT는 빈 등급 행이 남을 수 있음 |
| SALES·등급 2/3 | 내 실제 개선본이 각 관계의 ON을 나눔 |
| 자기 부서 평균 초과 | 실제 상관 조건·반올림 표시와 비교 분리 |

실제 초기 자료의 1981년 최저 급여는 JAMES 950이다. 새 연도 반례의 A 1000과 구별한다. 원본 전체 실행 결과를 고정해서 옮긴 표가 아니라 요구와 실제 조건의 대응을 검토한 것이다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

문제 문장 → 원래 입력 표 → 안쪽 계산 대상 → 바깥 출력 대상 → 조인 보존 방향 → 집계 대상 → 정렬이다. 내 상관 쿼리의 e2.deptno=e.deptno에서 오른쪽 e는 바깥 사원이다. e2와 e를 별도 역할로 구별해야 전체 평균으로 잘못 읽지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 원래 풀이와 개선 풀이를 둘 다 남기고 각 ON을 분리했다. 빈 등급에 COUNT(사원 이름)을 써 강사님 COUNT(*)의 한계를 피했다. **아쉬운 점:** 연도 최저 문제는 바깥 조건이 빠졌다. **보완:** 이름은 NULL 가능성에 영향받으므로 일반적인 인원 집계에서는 사원 키를 세는 선택도 가능하다. 교재의 COUNT(empno)는 새 개선이며 원본 COUNT(ENAME)를 바꿔 인용한 것이 아니다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_sql/Script.sql` 935–944행 · **원본 발췌**

```sql
select min(sal) from emp
where hiredate >= '1981-01-01' and hiredate <= '1981-12-31';

select * from emp
where sal = 950;

select * from emp
where sal = (select min(sal) from emp
			 where hiredate >= '1981-01-01' and hiredate <= '1981-12-31')
and hiredate like '1981%';
```

출처: `D:/workspace_teacher/workspace_sql/Script.sql` 983–999행 · **원본 발췌**

```sql
/*
 * 급여 등급 별 사원 수를 등급 오름차순으로 정렬
단, 모든 등급을 표시한다
 */

select s.grade, count(*)
from salgrade s
	left outer join emp e 
		on (e.sal <= s.hisal and e.sal >= s.losal)
group by s.grade
order by s.grade;

select count(e.ename) 사원수,grade 등급
from emp e,salgrade s
where sal>=losal and
sal<=hisal
group by grade desc;
```

필요한 차이인 연도 조건과 빈 등급 COUNT 두 부분만 강사님 인용을 남긴다. 강사님은 연도를 안팎에 적용한 점이 더 정확하고 나는 빈 등급을 0으로 세는 점이 더 정확하다. 어느 한쪽을 항상 모범 답으로 두지 않는다. 강사님 등급 집계의 뒤 내부 조인도 빈 등급을 보존하지 못해 요구와 다르다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 반례 | 빠진 확인 | 영향 |
| --- | --- | --- |
| 다른 연도 같은 최저 급여 | 바깥 연도 | 대상 아닌 사원 추가 |
| 빈 등급 | COUNT 대상 | 0명을 1명으로 표시 |
| 다른 부서 평균 | 상관 부서 키 | 개인의 기준 평균 변경 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| B 연도를 1981로 | 올바른 결과도 A·B | 대상 범위 내 동점 |
| 빈 등급에 사원 1명 추가 | 두 COUNT 모두 1 | 실제 매칭 생김 |
| 상관 부서 조건 제거 | 전체 평균 초과로 바뀜 | 그룹 대응 없음 |

초기 자료에서 같은 결과면 조건 누락이 없다는 뜻은 아니다. 경계·빈 그룹·다른 그룹의 동점 반례를 생각한다. LEFT JOIN 뒤 COUNT(*)와 실제 사원 키 COUNT를 구별한다. 평균 표시와 조건 비교에 다른 반올림을 적용했는지도 본다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 업무 정의가 복잡한 집계의 테스트 데이터 설계·NULL 가능 열과 식별 키 선택·실행 계획 측정은 추가 학습이다. 실제 상관 쿼리는 수업 원본이므로 본문에서 설명하고 그 밖의 고급 최적화와 나눈다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 1981년 최저를 안쪽에서만 구하면 충분한가?
2. 빈 외부 조인의 COUNT(*)는 왜 1인가?
3. COUNT(e.empno)가 0인 이유는?
4. 자기 부서 조건이 없으면 어떤 평균인가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

바깥 사원의 연도도 확인해야 한다. 보존된 빈 매칭 행 한 개를 센다. 오른쪽 사원 키가 NULL이기 때문이다. 전체 표 평균이 된다.

</details>

| 요구 | 반드시 볼 것 |
| --- | --- |
| ~중 | 안팎 범위 |
| 모두 | 보존 방향 |
| 인원 | 실제 키 집계 |
| 자기 부서 | 상관 키 |

[장별 연습문제](실습/연습문제/실습_SQL_원본문제_비교_연습문제.md) · 다음은 [실무 스타일](19_SQL_실무_코딩스타일.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
<a id="section-7"></a>
<a id="section-8"></a>
