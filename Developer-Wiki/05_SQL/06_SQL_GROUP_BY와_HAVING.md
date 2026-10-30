# 06. GROUP BY와 HAVING — 어떤 단위로 묶고 남길 것인가

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

부서마다 평균을 내는 것과 같은 급여마다 평균을 내는 것은 다른 질문이다. 그룹 기준을 적을 때 어떤 행을 같은 묶음으로 볼지 먼저 정한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

전체 집계와 부서·직업별 집계를 나눈다. WHERE는 행, HAVING은 그룹을 거르는 용도를 설명한다. 불필요한 sal 그룹 기준이 평균 의미를 바꾸는 이유를 확인한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

GROUP BY는 지정 열의 값 조합이 같은 행을 묶는다. 집계 함수는 각 묶음 안에서 따로 계산한다. deptno 하나면 부서 단위이고 deptno,job이면 부서·직업 조합 단위다. 기준을 더 적으면 구체적인 작은 그룹으로 나뉠 수 있다.

| 절 | 적용할 질문 | 예 |
| --- | --- | --- |
| WHERE | 어떤 사원 행을 먼저 포함하나? | sal>=1500 |
| GROUP BY | 무엇이 같은 행들을 묶나? | deptno |
| SELECT 집계 | 그룹의 어떤 값을 요약하나? | AVG(sal) |
| HAVING | 어떤 그룹만 남기나? | COUNT(*)>=2 |

GROUP BY deptno,job,sal을 쓰면 같은 부서·직업이어도 급여가 다르면 다른 그룹이다. “부서·직업별 평균”을 구하려는데 sal까지 기준에 넣으면 평균을 낼 묶음 자체를 잘못 만든 것이다. 그룹의 비집계 열을 보여 줄 때 그 그룹에서 하나로 정해지는지를 확인해야 한다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB GROUP BY](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/group-by), [SELECT](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/select). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/06_SQL_GROUP_BY와_HAVING.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT deptno, COUNT(*) AS people, SUM(sal) AS total_sal
FROM book_emp GROUP BY deptno ORDER BY deptno;
SELECT deptno, COUNT(*) AS people, AVG(sal) AS avg_sal
FROM book_emp WHERE sal >= 1500
GROUP BY deptno HAVING COUNT(*) >= 2 ORDER BY deptno;
```

첫 조회는 전원을 부서별로 묶는다. 둘째는 ADA 1000·DAN 1300을 먼저 제외한 다음 남은 사람을 묶는다. 20번은 CARA·ELLA, 30번은 BEN·FINN이고 두 그룹 모두 2명이므로 남는다. 10번은 필터 뒤 행이 없어 사라진다. HAVING은 그 뒤 그룹 수를 판단한다.

**가상 자료 기준 예상 결과:**

| 첫 조회 부서 | 인원 | 급여 합 |
| --- | --- | --- |
| 10 | 1 | 1300 |
| 20 | 3 | 7000 |
| 30 | 2 | 3100 |

둘째 조회는 20번 2명·평균3000, 30번 2명·평균1550이다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 361–379행 · **원본 발췌**

```sql
-- distinct와 비슷한 결과물을 검색할 수 있음
select deptno from emp
group by deptno;

-- group by와 집계함수를 같이 쓰면 '그룹별'이 가능
select 
	deptno, count(*), sum(sal) 
from emp
group by deptno;

-- 이렇게 쓰면 각 첫 번째것만 나오기 때문에 상위에 있는것은 group by에 넣어줘야 함
select deptno, job
from emp
group by deptno;

-- group by에 있는것을 select에 사용할 수 있음
select deptno, job, count(*)
from emp
group by deptno, job;
```

**발췌 바로 풀이:** `GROUP BY deptno`는 같은 부서 번호의 사원을 한 그룹으로 만든다. `COUNT(*)`, `SUM(sal)`은 **부서마다** 계산된다. `GROUP BY deptno, job`은 같은 부서에서도 직업별로 나눈다. 내 372–374행은 `job`을 출력하면서 `deptno`만 그룹으로 묶는 실험이다. 그 그룹 안에 직업이 여러 개라면 어떤 `job`인지 정해지지 않아 설정에 따라 오류가 나거나 임의 값을 보일 수 있다. **강사님처럼 출력할 비집계 열을 그룹 기준에 함께 넣는 방식**이 이 예제의 의도에 맞다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 402–416행 · **원본 발췌**

```sql
-- 부서, 직업 별 sal평균이 2000이상인 조건 식
select
	 avg(sal), deptno, job
from emp
group by deptno, job, sal
having avg(sal) >= 2000;

-- having은 group by에 조건식을 걸 수 있지만 실무에서 주로 사용하진 않음
select
	 avg(sal), deptno, job
from emp
group by deptno, job
having deptno = 10; 
-- where 조건을 having에 적을 수 있지만,
-- 통상 group by와 관련 된 것만 적는것이 좋다
```

**발췌 바로 풀이:** 강사님은 `GROUP BY deptno, job`으로 묶고 `HAVING AVG(sal) >= 2000`으로 **평균 급여가 기준 이상인 그룹**을 남긴다. 내 403–407행은 여기에 `sal`까지 그룹 기준으로 넣었다. 그러면 같은 부서·직업이라도 급여가 다른 사원은 **서로 다른 그룹**이 되어 “부서·직업별 평균”이라는 주석의 뜻과 달라진다. 이 경우 강사님처럼 `GROUP BY deptno, job`이 더 정확하다. 원본 코드는 그대로 보여 주되 결과 해석을 바로잡는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 418–428행 · **원본 발췌**

```sql
-- and에 cnt나 count를 써버리면, from부터 실행되기 때문에
-- 어떤 column인지 알 수 없어 having에 조건식을 줘서 조회해야 함
-- 직업 별로 연봉 1,000이상인 사람이 3명 이상인 경우 출력 조건식
select
	job, count(*) cnt
from emp
-- and cnt >= 3
-- and count(*) >= 3
where sal >= 1000
group by job
having count(*) >= 3
```

**발췌 바로 풀이:** 두 코드는 먼저 `WHERE sal >= 1000`으로 **급여가 낮은 사원 행을 제외**하고, `GROUP BY job`으로 직업별 묶음을 만든 다음 `HAVING COUNT(*) >= 3`으로 **3명 이상인 그룹**만 남긴다. 내 주석의 “`HAVING`은 실무에서 주로 사용하지 않는다”는 일반 규칙이 아니다. 이 문제에서는 `HAVING`이 정확히 필요한 자리다.

내 첫 그룹 실험은 deptno만 묶고 job을 같이 선택한다. 같은 부서에 여러 직업이 있으면 어느 job을 보여 줄지 정해지지 않는다. 뒤의 deptno,job 그룹은 두 기준을 함께 지정한다. 평균 문제의 deptno,job,sal은 요구보다 기준이 하나 많다. 실무에서 HAVING을 거의 쓰지 않는다는 메모도 일반 규칙이 아니며 원본 COUNT 조건에 필요한 절이다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

사원 행 → WHERE 조건 → 그룹 키 조합 → 각 그룹의 집계 → HAVING → 결과·정렬이다. WHERE에서 그룹 COUNT를 바로 조건으로 쓰려는 원본 주석의 시도는 그룹을 만들기 전 행 조건과 집계 후 조건을 섞는다. 이는 물리 실행을 단순히 FROM부터 한 줄씩 실행한다는 뜻이 아니라 논리적 역할 차이다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 그룹의 키를 한 개·두 개로 바꾸고 WHERE와 HAVING을 실제로 연결했다. **실제 요구 불충족:** 부서·직업 평균 문제에 sal까지 묶으면 다른 결과 단위다. **개선:** 출력할 열·집계의 분모·그룹 키를 먼저 적은 뒤 쿼리를 작성한다. WHERE로 제한할 행 조건과 그룹 조건을 분리하면 의도가 읽기 쉽다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_sql/Script.sql` 363–381행 · **원본 발췌**

```sql
-- 부서, 직업 별 평균이 2000 이상
SELECT 
    AVG(sal) AS avg_sal,
    deptno,
    job
FROM emp
GROUP BY deptno, job
HAVING AVG(sal) >= 2000;

SELECT 
    AVG(sal) AS avg_sal,
    deptno,
    job
FROM emp
where deptno = 10
GROUP BY deptno, job
HAVING deptno = 10; 
-- where 조건을 having에 적을 수 있지만
-- 통상 group by와 관련된 것만 적는다
```

비교가 필요한 평균 문제만 인용한다. 강사님은 deptno,job으로 묶어 요구한 단위의 평균을 구한다. 내 sal 추가와 의미가 다르므로 이 부분은 강사님 방식으로 고치면 좋다. 같은 주제의 모든 쿼리를 양쪽에서 반복하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 단계 | 남은 사원 | 그룹 |
| --- | --- | --- |
| 전체 | 6명 | 아직 없음 |
| sal>=1500 | BEN·CARA·ELLA·FINN | 아직 없음 |
| 부서로 묶음 | 같은 네 명 | 20·30 두 그룹 |
| COUNT>=2 | 같은 두 그룹 | 모두 통과 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| HAVING COUNT>=3 | 둘째 조회 0행 | 남은 각 그룹 2명 |
| WHERE 제거 | 20번3명·30번2명 | 집계에 포함한 행 변경 |
| 첫 조회에 sal 그룹 추가 | 부서 안 급여별 분할 | 기준 변경 |

평균이 개별 급여처럼 보이면 그룹 기준에 sal이 들어갔는지 본다. 오류 없이 job이 보이더라도 의도한 대표값인지 확정하지 않는다. SQL 모드가 허용하는 모호한 구문과 원하는 결과가 같은 것은 아니다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** ONLY_FULL_GROUP_BY 같은 SQL 모드의 상세 판정, ROLLUP·윈도 함수·집계 최적화는 추가 학습이다. 현재 문제는 그룹 키와 비집계 열을 명확히 맞추는 방식으로 해결한다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 부서·직업별 평균에 sal을 더 묶으면 같은가?
2. 개인 급여 조건은 WHERE인가 HAVING인가?
3. 그룹 인원 조건은 어디에 쓰는가?
4. GROUP BY가 언제나 입력 전원을 유지하는 결과를 내는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

같지 않다. 급여별로 더 나뉜다. 개인 급여는 WHERE, 그룹 인원은 HAVING이 적합하다. 결과는 사원 행 단위가 아니라 그룹 단위로 바뀐다.

</details>

| 절 | 단위 |
| --- | --- |
| WHERE | 개별 행 |
| GROUP BY | 묶음 기준 |
| HAVING | 집계된 그룹 |

[장별 연습문제](실습/연습문제/06_SQL_GROUP_BY와_HAVING_연습문제.md) · 다음은 [문자열 함수](07_SQL_문자열함수.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
