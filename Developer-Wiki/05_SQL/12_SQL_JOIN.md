# 12. JOIN — 같은 번호와 범위로 자료의 관계 연결하기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

사원 옆에 부서 이름을 보려면 서로 다른 표의 자료를 연결해야 한다. 어떤 행과 어떤 행을 짝지을지 조건을 정하는 것이 조인의 핵심이다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

모든 조합과 연결 조건이 있는 조인의 행 수를 구분한다. 표 별칭·동일 열 이름·ON·USING을 읽고 급여 등급의 범위 조인까지 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

JOIN은 두 표에서 조건에 맞는 행을 조합해 결과의 열로 보여 준다. 사원 한 명의 deptno와 부서의 deptno가 같으면 그 사원 옆에 dname을 연결할 수 있다. 표를 두 개 적었다는 이유만으로 DB가 원하는 관계를 자동 추측하지는 않는다.

| 구성 | 목적 | 예 |
| --- | --- | --- |
| FROM book_emp e | 대상·별칭 | e는 사원 표 |
| JOIN book_dept d | 연결할 표 | d는 부서 표 |
| ON e.deptno=d.deptno | 짝 조건 | 같은 부서 번호 |
| SELECT e.ename,d.dname | 필요한 결과 | 이름·부서 |

새 자료6명×부서4개를 조건 없이 조합하면24행이다. 연결 조건이 있으면 각 사원이 해당 부서 한 행과 맞아6행이다. 이것은 부서번호가 부서 표에서 고유하고 사원 번호가 유효하다는 자료 조건 때문이다. 조인이 언제나 왼쪽 표와 같은 행 수를 만든다는 규칙은 아니다.

동일 이름의 열이 양쪽에 있으면 e.deptno처럼 출처를 붙인다. USING(deptno)는 같은 이름 열을 연결하는 수업 문법이다. ON과 USING은 출력 열의 모양에서 차이가 있을 수 있어 SELECT * 결과까지 무조건 같다고 외우지 않는다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB JOIN syntax](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/12_SQL_JOIN.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT COUNT(*) FROM book_emp e, book_dept d;
SELECT e.ename, d.dname
FROM book_emp e JOIN book_dept d ON e.deptno=d.deptno
ORDER BY e.empno;
SELECT e.ename, e.sal, e.deptno
FROM book_emp e JOIN (
 SELECT deptno, MAX(sal) AS max_sal FROM book_emp GROUP BY deptno
) top_sal ON e.deptno=top_sal.deptno AND e.sal=top_sal.max_sal
ORDER BY e.empno;
```

둘째 조회는 부서번호가 같은 한 부서를 각 사원과 연결한다. 셋째는 새 개선 예제다. 부서별 최대 급여 표를 만든 뒤 부서번호와 급여 두 조건을 함께 연결해 자기 부서 최고 급여 사원을 고른다. 11장의 GUS 반례를 추가하더라도20번 최대3000과 맞지 않아 빠진다. 이 장 기본 데이터는 다시6명이다.

**가상 자료 기준 예상 결과:**

첫 결과 **24**. 둘째 결과 ADA–BETA, BEN–GAMMA, CARA–BETA, DAN–ALPHA, ELLA–BETA, FINN–GAMMA. 셋째는 BEN·CARA·DAN·ELLA 네 명이다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 527–539행 · **원본 발췌**

```sql
-- 이렇게 2개의 테이블을 이용하게 되면 곱연산(데카르트)되어 출력됨
select * 
from emp, dept;

-- 두 개의 테이블을 이용할 땐 아래와 같이 조건식에서 맞춰야 함
select * 
from emp, dept
where emp.deptno = dept.deptno;

-- 아래처럼 별칭을 주어서 사용할 수 있음
select * 
from emp e, dept d
where e.deptno = d.deptno;
```

**발췌 바로 풀이:** `FROM emp, dept`만 쓰면 사원 각 행과 부서 각 행의 **모든 조합**이 나온다. `WHERE e.deptno = d.deptno`를 넣으면 같은 부서 번호인 조합만 남는다. 강사님과 나는 테이블 별칭 `e`, `d`도 사용했다. 조인 조건을 빠뜨리면 같은 사원·부서가 무관하게 묶여 행 수가 크게 늘어난다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 541–551행 · **원본 발췌**

```sql
-- Column 'deptno' in SELECT is ambiguous
-- 두 테이블에 이름이 같기 때문에 뭘 지칭하는건지 모르겠다는 Error 발생
/*
select ename, dname, deptno 
from emp e, dept d
where e.deptno = d.deptno;
*/

select e.ename, d.dname, e.deptno 
from emp e, dept d
where e.deptno = d.deptno;
```

**발췌 바로 풀이:** 두 표 모두 `deptno` 열이 있으므로 단독 `SELECT deptno`는 어느 표인지 모호하다. `e.deptno` 또는 `d.deptno`처럼 쓴다. 강사님은 일부러 매우 긴 별칭을 쓴 실행 예제를 남겼고, 나는 `e`·`d`로 짧게 구분했다. **초보자 복습에는 내 짧은 별칭이 읽기 쉽다.** 핵심은 별칭 길이가 아니라 원본 표를 분명히 지정하는 것이다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 555–567행 · **원본 발췌**

```sql
-- SMITH의 연봉 등급은? 정답 : 1
-- 이름, 월급, 등급, losal, hisal
select * from salgrade
where 800 >= losal and 800 <= hisal;

select sal from emp
where ename='SMITH'

select ename, sal, grade, hisal, losal
from emp e, salgrade s
-- where sal >= losal and sal <= hisal
where sal between losal and hisal
and ename='SMITH';
```

**발췌 바로 풀이:** 급여 등급은 부서 번호처럼 **같은 값끼리** 맞추지 않는다. `sal BETWEEN losal AND hisal`의 범위 안에 급여가 들어가는 등급을 찾는다. 강사님은 `sal >= losal AND sal <= hisal`로 풀어 쓰고, 나는 `BETWEEN`으로 줄였다. 양 끝을 포함한다는 [02장](02_SQL_WHERE와_조건연산자.md)의 규칙이 여기에도 적용된다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 600–606행 · **원본 발췌**

```sql
-- join을 쓸 때는 where가 아닌 on에 조건식 기재
select e.deptno
from emp e join dept d on(e.deptno = d.deptno);

-- using으로 같은 column을 합칠 수 있음
select deptno
from emp e join dept d using(deptno);
```

**발췌 바로 풀이:** `JOIN ... ON e.deptno = d.deptno`는 연결 조건을 `ON`에 적는다. 두 표의 같은 이름 열을 연결할 때 `USING(deptno)`로도 쓸 수 있다. 내 주석 “JOIN을 쓸 때는 WHERE가 아닌 ON”은 **연결 조건을 분리해 읽기 좋다**는 취지로 이해한다. 위의 `FROM emp, dept WHERE ...` 방식도 수업 원본에 있는 유효한 조인이다.

내 쉼표 조인은 WHERE로 두 부서번호를 맞췄고 뒤에는 JOIN ON을 사용했다. 모호한 deptno 오류 예문은 주석으로 보존돼 있다. 같은 이름 열의 출처를 붙인 내 e·d 별칭은 추적하기 쉽다. 급여 등급은 같은 번호가 아니라 sal BETWEEN losal AND hisal로 범위를 연결했다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

사원 부서번호 → 같은 번호 부서행 → 이름·부서명 결과다. 범위 조인은 사원 급여 → 등급의 하한·상한 → 포함하는 등급이다. 셋째 개선은 안쪽 GROUP BY → deptno·max_sal 결과 표 → 바깥 두 열 대응 → 최고 사원이다. 필요한 중간 정의를 쿼리 안에 모두 실었다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 모호한 열 오류를 기록하고 별칭으로 고쳤으며 BETWEEN 범위 조인도 작성했다. **주석 보완:** JOIN을 쓰면 WHERE는 못 쓴다는 뜻은 아니다. ON에는 연결 조건을, WHERE에는 추가 필터를 나누면 읽기 좋다. **개선:** 11장의 최대 급여 문제는 부서 키를 함께 대응하면 요구를 정확히 표현한다. 이 개선 쿼리는 당시 제출 풀이가 아니다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님은 긴 별칭 예시와 두 부등식 범위 연결을, 나는 짧은 e·d와 BETWEEN을 사용했다. 두 범위식은 양끝 포함으로 같은 의도다. 별칭이 짧다는 이유만으로 항상 더 좋다는 규칙도 아니다. 이 작은 예제에서는 e·d의 의미를 먼저 정의해 읽기 편하게 한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 사원 | 번호 | 맞는 부서 | 결과 한 쌍 |
| --- | --- | --- | --- |
| ADA | 20 | BETA | ADA–BETA |
| BEN | 30 | GAMMA | BEN–GAMMA |
| DAN | 10 | ALPHA | DAN–ALPHA |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| ON 조건을 제거한 조합 조회 | 24조합 | 관련 없는 조합도 포함 |
| WHERE e.deptno=20 추가 | ADA·CARA·ELLA | 조인 뒤 요청 필터 |
| GUS20·1600 추가 | 최고 사원에 GUS 없음 | 자기 부서 최대와 불일치 |

행이 폭증하면 연결 조건·중복 키를 본다. 모호한 열 오류면 표 별칭을 붙인다. 사원 수와 결과 행 수가 다르다고 무조건 오류로 판단하지 말고 관계의1대다·매칭 없음 여부를 본다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 조인 알고리즘·실행 계획·인덱스 비용·다대다 집계 중복은 추가 학습이다. 현재는 원본의 연결 키와 범위 조건을 명확히 읽는다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 조건 없는6명×4부서 조합은?
2. sal IN 최대목록의 부족한 대응은?
3. 등급 범위 조인도 같은 값끼리만 가능한가?
4. deptno를 모호하지 않게 쓰려면?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

24행이다. 부서번호 대응이다. 부등식·BETWEEN 같은 범위 조건도 쓴다. e.deptno처럼 출처를 붙인다.

</details>

| 확인 | 질문 |
| --- | --- |
| 관계 | 무엇과 무엇을 연결하나 |
| 조건 | 값·범위·두 키가 맞나 |
| 개수 | 키 중복과 매칭 없음은? |

[장별 연습문제](실습/연습문제/12_SQL_JOIN_연습문제.md) · 다음은 [외부·자기 조인](13_SQL_Outer_JOIN과_Self_JOIN.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
