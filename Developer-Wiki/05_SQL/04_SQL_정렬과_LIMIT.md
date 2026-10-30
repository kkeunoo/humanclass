# 04. ORDER BY와 LIMIT — 순서를 정하고 필요한 구간 보기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

조회 결과의 위쪽 행이 무조건 가장 큰 값은 아니다. 무엇으로 정렬했는지, 동점은 어떻게 나누는지, 몇 행을 건너뛰는지 함께 읽는다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

ASC·DESC·여러 기준의 적용을 설명한다. LIMIT 개수와 offset,개수의 차이를 추적하고 동점이 있을 때 안정된 정렬 기준을 고른다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

ORDER BY는 결과의 순서를 요청한다. ASC는 오름차순이고 기본 방향이다. DESC는 내림차순이므로 내려가는 순서를 원하면 적어야 한다. 정렬 기준이 여러 개면 첫 열로 비교하고 같은 값일 때 다음 열을 비교한다. 뒤 기준이 앞 기준을 지워 버리는 것이 아니다.

| 표현 | 의미 | 새 예제 |
| --- | --- | --- |
| ORDER BY sal DESC | 큰 급여부터 | 3000 동점 있음 |
| sal DESC, empno ASC | 동점은 번호순 | CARA 다음 ELLA |
| LIMIT 2 | 앞 두 행 | 1·2번째 |
| LIMIT 1,2 | 한 행 건너뛰고 두 행 | 2·3번째 |

정렬 없이 LIMIT을 쓰면 “급여가 높은 사람”을 지정한 것이 아니다. 급여만 정렬하고 동점자를 자르면 어떤 동점 행이 먼저인지 확정되지 않을 수 있다. 고유 사원 번호를 마지막 기준으로 두면 이 데이터에서 순서를 명확히 만들 수 있다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB ORDER BY](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/order-by), [LIMIT](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/limit). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/04_SQL_정렬과_LIMIT.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT ename, sal FROM book_emp ORDER BY sal DESC, empno ASC LIMIT 2;
SELECT ename, sal FROM book_emp ORDER BY sal DESC, empno ASC LIMIT 1, 2;
```

전체 급여 순서는 CARA·ELLA·BEN·FINN·DAN·ADA다. CARA와 ELLA는 동점이어서 사원 번호로 나뉜다. 첫 쿼리는 앞 두 행, 둘째는 CARA 한 행을 건너뛴 다음 두 행을 보여 준다. LIMIT의 첫 숫자 1은 사원 번호 조건도, 가져올 개수도 아니다.

**가상 자료 기준 예상 결과:**

| 조회 | 첫 행 | 둘째 행 |
| --- | --- | --- |
| 앞 2행 | CARA 3000 | ELLA 3000 |
| 1행 건너뛰고 2행 | ELLA 3000 | BEN 1600 |



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 178–203행 · **원본 발췌**

```sql
-- order by로 정렬을 할 수 있음 
-- ASC:오름차순 → 생략 가능
select * from emp
order by sal asc;

-- DESC:내림차순 → 생략 가능
select * from emp
order by sal desc;

select * from emp
order by deptno;

-- column별 asc, desc를 부여할 수 있음
-- 앞의 desc를 먼저 적용하고 겹치는것이 나오면 뒤 asc 적용
select * from emp
order by deptno desc, job;

-- order by에 여러 칼럼인 경우 왼쪽부터 적용되고 동일한 값이 있는 경우 다음 조건 적용
-- deptno를 정렬하고, job을 정렬하고, empno를 정렬
select * from emp
order by deptno desc, job asc, empno;

-- 각 절의 순서를 지켜야 함, where이 order by 뒤에 갈 순 없음
select * from emp
where sal > 1000
order by deptno desc, job asc, empno;
```

**발췌 바로 풀이:** `ASC`는 오름차순이며 생략할 수 있다. `DESC`는 내림차순이다. `ORDER BY deptno DESC, job ASC, empno`는 **부서 번호 → 같은 부서 안의 직업 → 같은 직업 안의 사원 번호** 순서로 비교한다. 강사님은 동일한 조건에 `WHERE sal > 1000`을 더해, 조건절이 정렬절보다 앞에 오는 형태를 보여 준다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 205–216행 · **원본 발췌**

```sql
-- limit에 인자가 1개일 경우 보여 줄 검색 결과의 rows를 제한할 수 있음
select * from emp
where sal > 1000
order by deptno desc, job asc, empno
limit 3;

-- limit [offset][rows]
-- limit에 인자를 2개 줄 경우, offset만큼 건너 뛴 rows만큼 보여줌
select * from emp
where sal > 1000
order by deptno desc, job asc, empno
limit 5, 3;
```

**발췌 바로 풀이:** `LIMIT 3`은 정렬된 결과의 앞 3행, `LIMIT 5, 3`은 **앞 5행을 건너뛰고 다음 3행**이다. 양쪽 코드에서 같은 형식으로 연습했다. 데이터가 변하면 몇 번째 행의 이름은 달라질 수 있다. 정렬 조건이 같을 때 순서를 안정적으로 읽으려면 내·강사님 코드처럼 마지막에 `empno`까지 확인하는 편이 좋다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 218–224행 · **원본 발췌**

```sql
-- 문제3 _ 부서 번호가 20 또는 30인 사원 중에서
-- 연봉이 2,000 ~ 3,000 사이(포함)인 사원의
-- 연봉이 작은 순으로 출력하시오
-- 연봉이 같으면 이름을 내림차순으로 정렬
select * from emp
where (deptno = 20 or deptno = 30) and (sal between 2000 and 3000)
order by sal, ename desc;
```

**발췌 바로 풀이:** 두 풀이 모두 부서 20·30, 급여 2,000~3,000 **양 끝 포함**, 급여 오름차순, 같은 급여면 이름 내림차순을 구현한다. 내 코드의 `ORDER BY sal`은 기본 오름차순이므로 강사님의 `sal ASC`와 같은 의도다. SQL 문장을 읽을 때는 **행 선택 → 정렬 → 몇 행만 보기** 순으로 스스로 풀어 보면 좋다.

내 원본은 sal·deptno·job·empno의 정렬을 비교하고 WHERE가 ORDER BY보다 앞에 와야 함을 메모했다. LIMIT 5,3은 다섯 행을 건너뛰고 세 행이다. 마지막 복합 문제는 부서·급여 조건 뒤 급여 오름차순과 동점 이름 내림차순을 적용한다. 각 절의 목적과 작성 순서를 나누어 본다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

FROM의 대상 → WHERE에 맞는 행 → 결과 열 → ORDER BY 비교 기준 → LIMIT 구간을 논리적으로 추적한다. 서버 물리 실행을 그대로 묘사한 고정 파이프라인은 아니다. 함수 정의 파일의 연결 대신 행들이 필터·정렬·구간 선택을 통과하는 흐름이다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 여러 기준과 조건·정렬·제한을 실제로 조합했다. **원본 주석 교정:** “DESC: 내림차순 → 생략 가능”은 틀렸다. ASC가 기본이므로 DESC를 빼면 같은 내림차순 요청이 아니다. **개선:** 결과 구간을 재현하려면 동점까지 나눌 기준을 확인한다. 원본의 마지막 empno 기준은 이 점에서 유용하다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님은 ASC 생략 가능과 DESC를 구분한다. 같은 정렬 쿼리를 반복 인용하지 않고 내 DESC 주석의 실제 오류를 바로잡는다. 양쪽 모두 여러 열·empno 정렬을 작성했으므로 한쪽만 안정된 기준을 썼다고 평가하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 전체 위치 | 이름 | 급여 | LIMIT 1,2 포함 |
| --- | --- | --- | --- |
| 1 | CARA | 3000 | 건너뜀 |
| 2 | ELLA | 3000 | 포함 |
| 3 | BEN | 1600 | 포함 |
| 4 | FINN | 1500 | 제외 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| DESC를 ASC로 | ADA부터 | 방향 변경 |
| LIMIT 0,2 | CARA·ELLA | 건너뛰지 않음 |
| LIMIT 2,2 | BEN·FINN | 두 행 건너뜀 |
| empno 정렬 제거 | 동점 순서 확정 못함 | 동일 급여 |

반대 순서면 DESC 유무를 본다. 페이지가 한 행씩 밀리면 offset은 0부터 건너뛸 수라는 점을 확인한다. 동일 조건인데 동점 위치가 달라지면 마지막 고유 기준이 있는지 확인한다. 정렬을 위한 표의 영구 데이터 순서 변경으로 이해하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 대규모 페이지의 offset 비용·키 기반 페이지 처리·인덱스와 정렬의 관계는 추가 학습이다. 현재는 수업의 LIMIT 구간과 정렬 기준을 정확히 읽는다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. DESC를 생략하면 내림차순인가?
2. LIMIT 5,3은 몇 행을 요청하는가?
3. 급여가 같을 때 empno는 왜 도움이 되는가?
4. LIMIT만으로 최고 급여를 고르는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

기본은 ASC다. 다섯 행을 건너뛰고 세 행이다. 고유 번호로 동점 순서를 나눌 수 있다. 급여 정렬 요청이 필요하다.

</details>

| 단계 | 핵심 |
| --- | --- |
| 정렬 | 열마다 방향 |
| 동점 | 다음 기준 |
| 제한 | 건너뛸 수·개수 |

[장별 연습문제](실습/연습문제/04_SQL_정렬과_LIMIT_연습문제.md) · 다음은 [집계](05_SQL_집계함수.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
