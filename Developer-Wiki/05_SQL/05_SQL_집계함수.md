# 05. 집계 함수 — 여러 행을 개수·합계·평균으로 요약하기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

여섯 사원을 한 번에 읽는 조회와 여섯 사원의 평균을 구하는 조회는 결과 단위가 다르다. 무엇을 세고 어떤 값을 제외하는지부터 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

COUNT(*)·COUNT(열)·SUM·AVG·MIN·MAX의 입력과 결과를 설명한다. NULL과 0의 집계 차이, 전체 집계와 개별 사원 이름을 섞은 문제를 구분한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

집계 함수는 여러 행의 값을 받아 요약 값을 만든다. 그룹을 지정하지 않은 전체 집계와 GROUP BY로 묶은 집계를 구별해야 한다. 집계 함수가 언제나 결과 전체를 한 행 한 칸으로 만든다는 주석은 지나치게 단순하다. 여러 집계 열을 선택할 수도 있고 그룹마다 행이 생길 수도 있다.

| 함수 | 입력의 의미 | NULL 처리 |
| --- | --- | --- |
| COUNT(*) | 조건에 맞는 행 | 행을 셈 |
| COUNT(comm) | comm 값이 있는 행 | NULL 제외·0 포함 |
| SUM(sal) | 급여 합계 | NULL 제외 |
| AVG(comm) | 수당 평균 | NULL을 분모에서도 제외 |
| MAX·MIN | 비교 가능한 가장 큰·작은 값 | NULL 제외 |

새 수당 6개는 NULL·300·NULL·0·NULL·0이다. 합은 300, 수당이 있는 행은 3개이므로 AVG(comm)는 100이다. 수당 없는 사람을 0원으로 정해 평균을 구하면 300/6=50으로 다른 질문이 된다. 무엇을 평균 내는지 업무 의미를 먼저 정한다. 이번 기본 쿼리는 실제 값이 있는 수당 평균이다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB COUNT](https://mariadb.com/docs/server/reference/sql-functions/aggregate-functions/count), [AVG](https://mariadb.com/docs/server/reference/sql-functions/aggregate-functions/avg), [SUM](https://mariadb.com/docs/server/reference/sql-functions/aggregate-functions/sum). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/05_SQL_집계함수.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT COUNT(*) AS people, COUNT(comm) AS known_comm,
       SUM(sal) AS total_sal, AVG(sal) AS avg_sal
FROM book_emp;
SELECT MIN(sal), MAX(sal), SUM(comm), AVG(comm) FROM book_emp;
SELECT COUNT(*) FROM book_emp WHERE sal > 99999;
```

COUNT(*)는 여섯 행 모두를 센다. COUNT(comm)는 NULL 세 행을 빼고 숫자 0 두 행과 300 한 행을 센다. 급여 합 11400을 여섯으로 나누면 1900이다. 마지막 조건을 통과하는 사원은 없지만 COUNT 결과 자체는 숫자 0을 담은 한 행이다.

**가상 자료 기준 예상 결과:**

| people | known_comm | total_sal | avg_sal |
| --- | --- | --- | --- |
| 6 | 3 | 11400 | 1900 |

둘째 결과는 1000·3000·300·100이다. 마지막 결과는 **0이라는 값이 있는 한 행**이며 0행이 아니다. 숫자 뒤 표시 소수 자릿수는 도구·DB에 따라 다를 수 있다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 226–231행 · **원본 발췌**

```sql
-- 집계 함수는 한 줄의 한 칸으로 나오며 group by와 잘 어울림
-- count는 특정 열 또는 행의 개수를 검색해줌, null은 빼고 세줌
select count(ename) from emp; 
select count(mgr) from emp;
select count(comm) from emp;
select count(*) from emp; -- *을 써서 모든 줄을 보는 경우가 많음
```

**발췌 바로 풀이:** `COUNT(*)`는 조건에 맞는 **행**을 세고, `COUNT(comm)`은 `comm` 값이 `NULL`이 아닌 행만 센다. `COUNT(ename)`도 이름이 `NULL`인 행은 제외한다. 그래서 수당이 없는 사원이 있다면 `COUNT(comm)`은 전체 사원 수보다 작다. 내 주석의 “집계 함수는 한 줄의 한 칸”은 전체 집계를 너무 단순화한 표현이다. `GROUP BY`를 더하면 **그룹마다 한 행씩** 나온다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 233–241행 · **원본 발췌**

```sql
-- min, max는 각 최소값, 최대값이며 문자열에 사용해도 a-z순
select max(sal) from emp;
select min(sal) from emp;

-- 해당 컬럼의 합을 구할 때 사용
select sum(sal) from emp;

-- 해당 컬럼의 평균치를 구할 때 사용
select avg(sal) from emp;
```

**발췌 바로 풀이:** `MAX(sal)`과 `MIN(sal)`은 급여의 양 끝값, `SUM(sal)`은 합계, `AVG(sal)`은 평균이다. 강사님은 숫자뿐 아니라 `MAX(ename)`, `MIN(ename)`도 넣어 문자에도 순서 비교가 적용됨을 보여 준다. 내 코드에는 이 문자열 비교가 없다. 다만 문자의 정렬 규칙은 DB 설정에 따라 달라질 수 있으므로 이름의 고정된 결과를 여기서 외우지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 243–245행 · **원본 발췌**

```sql
-- 집계함수는 1줄로 셀 병합을 허용하지 않기 때문에 
-- 다른 여러 줄이 나오는 함수와 사용 시 원하는 결과를 얻기 어려움
select count(*), ename from emp;
```

**발췌 바로 풀이:** `COUNT(*)`는 전체 결과를 요약하는데 `ename`은 한 행의 값이다. 그룹 기준 없이 둘을 섞으면 **어느 사원 이름인지 정해지지 않거나 SQL 모드에 따라 오류**가 될 수 있다. 내 주석의 “셀 병합”은 SQL의 실제 원리를 설명하지 못한다. 특정 사원의 이름과 함께 부서별 수를 보려면 어떤 그룹의 값을 보여 줄지 먼저 정해야 한다. 이어지는 [06장](06_SQL_GROUP_BY와_HAVING.md)에서 그 기준을 만든다.

내 COUNT(ename)·COUNT(mgr)·COUNT(comm)·COUNT(*)는 같은 표에서 어떤 열의 NULL을 빼는지 비교한다. 내 주석 “셀 병합”은 집계 원리를 설명하지 못한다. COUNT(*)와 ename을 그룹 없이 같이 선택하면 어느 사원의 이름인지 정하지 않은 문제가 생긴다. 이름 최댓값은 급여 최댓값을 가진 사원의 이름을 찾는 식도 아니다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

FROM 대상 → WHERE로 남긴 행 → 집계 함수가 각 열 값들을 읽음 → 결과 한 행의 집계 열들이다. MAX(sal)은 숫자 하나를 돌려줄 뿐 그 행 전체를 자동으로 돌려주지 않는다. 최고 급여 사원을 찾는 조건은 11장 서브쿼리와 연결한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 여러 열의 COUNT와 전체 행 수를 비교해 NULL의 영향을 관찰했다. **교정:** 집계를 셀 병합으로 이해하지 않는다. **문자 비교:** min/max 이름을 단순 a–z 규칙으로 일반화하지 말고 비교 설정을 고려한다. **요구 확인:** 급여 최댓값과 그 급여를 받는 사람 목록은 다른 출력 요구다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님은 MAX(ename)·MIN(ename)도 실행해 문자열 비교를 보였다. 내 코드는 급여 집계 중심이다. 필요 차이는 이 점이며 동일한 SUM·AVG를 두 번 인용하지 않는다. 두 원본의 COUNT(*)와 이름 혼합 실험은 SQL 모드에 따라 오류나 정해지지 않은 이름을 보일 수 있어 유효한 사원 선택 방법으로 가르치지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 수당 값 | 개수에 포함 | 합계 기여 | 평균 분모 기여 |
| --- | --- | --- | --- |
| NULL 3행 | 제외 | 제외 | 0 |
| 300 1행 | 포함 | 300 | 1 |
| 0 2행 | 포함 | 0 | 2 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| COUNT(comm)를 COUNT(*)로 | 6 | 행 전체 |
| WHERE deptno=20 추가 | 3명·급여합7000 | 집계 전 행 필터 |
| 집계 대상을 빈 조건으로 | COUNT 0, SUM·AVG NULL | 입력 없음의 함수별 차이 |

숫자가 작으면 NULL 제외와 WHERE 조건을 확인한다. 평균 분모를 전체 인원으로 자동 가정하지 않는다. 집계에 이름을 섞어 놓고 그 이름이 대표 사원이라고 생각하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 집계 결과를 각 사원 행 옆에 유지하는 윈도 함수, COUNT(DISTINCT 열)의 상세 응용, 반올림·금액 정밀도 설계는 추가 학습이다. 먼저 현재 집계의 입력 집합과 분모를 설명한다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. COUNT(comm)는 0을 제외하는가?
2. 새 자료 수당 평균은 50인가 100인가?
3. MAX(sal)이 이름도 반환하는가?
4. 빈 입력 COUNT 결과는 0행인가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

0은 포함한다. 실제 수당 값 3개 평균이므로 100이다. 숫자 최댓값만 반환한다. 0이라는 값의 한 행이다.

</details>

| 계산 | 먼저 볼 것 |
| --- | --- |
| 개수 | 행인가 NULL 아닌 값인가 |
| 평균 | 무엇이 분모에 포함되나 |
| 최대 | 값과 그 값을 가진 행 구별 |

[장별 연습문제](실습/연습문제/05_SQL_집계함수_연습문제.md) · 다음은 [GROUP BY·HAVING](06_SQL_GROUP_BY와_HAVING.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
