# 02. WHERE — 결과에 남길 행의 조건 정하기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

같은 사원 표에서도 부서·직업·급여 조건에 따라 남는 사람이 달라진다. AND·OR·괄호·경계값을 한 행씩 판단하면 긴 조건도 읽을 수 있다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

SELECT의 열 선택과 WHERE의 행 선택을 구분한다. AND 우선순위와 괄호를 설명하고 BETWEEN·IN의 의미를 원래 비교식과 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

WHERE는 각 행의 값으로 조건을 판단하여 참인 행을 남긴다. deptno=20은 20을 변수에 대입하는 Python 문장이 아니라 같은지 비교하는 SQL 조건이다. AND는 양쪽 조건이 모두 참일 때, OR는 적어도 하나가 참일 때 참이다. NULL이 끼는 논리는 다음 장에서 별도로 다룬다.

| 표현 | 읽는 말 | 경계 |
| --- | --- | --- |
| sal >= 2000 AND sal < 3000 | 2000 이상, 3000 미만 | 3000 제외 |
| sal BETWEEN 2000 AND 3000 | 두 값 사이 | 양 끝 포함 |
| deptno IN (10,20) | 10 또는 20에 속함 | 같은 열의 여러 후보 |
| A OR B AND C | A 또는 B와 C 모두 | AND가 먼저 결합 |
| (A OR B) AND C | A나 B이면서 C | 괄호가 범위 표시 |

조건을 적은 순서와 서버의 실제 평가·최적화 순서를 같은 것으로 단정하지 않는다. 우선순위는 식의 의미를 해석하는 규칙이다. 자연어의 “또는”이 어디까지 묶이는지 애매하면 괄호를 써 의도를 드러낸다. 값을 필터링할 때 열을 지우는 것이 아니라 행을 남긴다는 점도 중요하다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB SELECT · WHERE](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/select), [BETWEEN](https://mariadb.com/docs/server/reference/sql-structure/operators/comparison-operators/between-and). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/02_SQL_WHERE와_조건연산자.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT ename FROM book_emp
WHERE deptno = 30 OR deptno = 20 AND job = 'CLERK'
ORDER BY empno;
SELECT ename FROM book_emp
WHERE (deptno = 30 OR deptno = 20) AND job = 'CLERK'
ORDER BY empno;
SELECT ename FROM book_emp WHERE sal BETWEEN 1500 AND 3000 ORDER BY empno;
```

첫 조건은 30번 부서면 직업과 무관하게 통과하므로 BEN·FINN도 남는다. 둘째는 20 또는 30인 사람 중 CLERK만 남겨 ADA 한 명이다. 셋째는 급여가 정확히 1500인 FINN과 3000인 CARA·ELLA도 포함한다. 같은 데이터에서 괄호 한 쌍과 경계 조건의 영향을 비교한다.

**가상 자료 기준 예상 결과:**

| 조회 | 남는 이름 |
| --- | --- |
| 괄호 없는 OR·AND | ADA, BEN, FINN |
| OR 부분을 괄호로 묶음 | ADA |
| 급여 1500–3000 포함 | BEN, CARA, ELLA, FINN |



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 70–90행 · **원본 발췌**

```sql
-- where로 조건을 걸어 볼 수 있음
select * 
from emp
where deptno = 20;

-- where의 값일 땐 '대/소문자'를 구분 함, and로 여러가지의 조건
select * 
from emp
where deptno = 20 and job = 'CLERK';

-- job이 CLERK이거나, deptno이 20인 사람은 or로 출력
select * from emp
where deptno = 20 or job = 'CLERK';

-- and가 or보다 우선순위이기 때문에, 필요 시 괄호 활용
-- 아래는 deptno = 20 and job = 'CLERK' 가 먼저 필터링 됨
select * from emp
where deptno = 30 or deptno = 20 and job = 'CLERK';

select * from emp
where (deptno = 30 or deptno = 20) and job = 'CLERK';
```

**발췌 바로 풀이:** `deptno = 20 AND job = 'CLERK'`는 **둘 다 참**인 사원만 남긴다. `OR`는 어느 한쪽이 참이면 남긴다. `AND`가 `OR`보다 먼저 결합하므로 `deptno = 30 OR deptno = 20 AND job = 'CLERK'`와 `(deptno = 30 OR deptno = 20) AND job = 'CLERK'`는 결과가 다를 수 있다. 업무 문장의 “또는 … 이면서 …” 범위가 헷갈리면 괄호로 묶는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 105–116행 · **원본 발췌**

```sql
-- 문제1 _ 급여가 2,000이상이고 3,000미만인 사원
select * from emp
where SAL >= 2000 and SAL < 3000;

-- between을 쓰면 범위를 지정해서 볼 수 있음
-- between A and B 는 이상/이하만 가능
select * from emp
where sal between 2000 and 3000;

-- 문제2 _ job이 CLERK 이거나 급여가 2,000초과 이면서 부서번호가 10인 사원만 출력
select * from emp
where job = 'CLERK' or (SAL > 2000 and DEPTNO = 10);
```

**발췌 바로 풀이:** “2,000 이상 **3,000 미만**”은 `sal >= 2000 AND sal < 3000`이다. `BETWEEN 2000 AND 3000`은 **양 끝을 포함**하므로 같은 조건으로 바꾸면 3,000인 사원까지 포함한다. 강사님은 문제 풀이 옆에 `BETWEEN`의 양 끝 포함을 바로 주석으로 표시해 이 차이를 확인하기 좋다. 내 코드 역시 별개 문장으로 둘을 실습했다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 118–125행 · **원본 발췌**

```sql
-- where에서 컬럼이 같고 or일 때 줄일 수 있는 방법 (in)
-- select * from emp
-- where deptno = 20 or deptno = 30
select * from emp
where deptno in (20, 30)

select * from emp
where deptno not in (20, 30)
```

**발췌 바로 풀이:** `deptno IN (20, 30)`은 부서 번호가 **20 또는 30**인 행을 고른다. `NOT IN`은 이 목록에 없는 값을 고른다. 내 두 문장에는 끝 세미콜론이 없으므로 편집기에서 여러 문장을 함께 실행할 때는 문장 경계를 확인한다. `NULL`이 포함된 `NOT IN`의 복잡한 동작은 지금의 원본 예제에 없으므로 기본 규칙처럼 암기하지 않는다.

내 코드는 부서 20·CLERK 조건에서 AND/OR를 바꾸고 괄호 전후를 비교했다. 급여 문제에서는 2000 이상 3000 미만을 비교식으로, BETWEEN 실험에서는 3000까지 포함해 썼다. 같은 결과라고 묶으면 경계의 차이를 놓친다. IN은 같은 열에 여러 후보를 비교하는 실제 원본 문법이다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

대상 표 → 각 행의 부서·직업·급여 읽기 → 조건식 의미 판단 → 참인 행 → SELECT 열 → 표시 순서 순서로 추적한다. 새 예제의 ORDER BY는 결과 확인용이고 상세 설명은 04장이다. WHERE는 다른 파일의 def를 호출하는 것이 아니라 DB의 조건식을 적용한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** AND 우선순위와 괄호의 필요성을 메모하고 실제 두 문장을 작성했다. **교정:** 값의 대소문자를 언제나 구분한다는 내 주석은 일반화할 수 없다. 문자열 비교는 열·비교식의 collation에 영향을 받는다. **경계:** BETWEEN으로 바꿀 때 미만·이하가 같은지 먼저 확인한다. 가독성을 위해 괄호를 쓰는 개선은 의미를 명확히 보여 주려는 선택이다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 모두 괄호 전후와 경계 문제를 풀어 핵심이 같다. 기계적으로 강사님 코드를 반복하지 않는다. 강사님 예문이 정답인 이유도 코드 길이가 아니라 문제의 “포함/미만”과 조건 묶음에 맞는지를 기준으로 판단한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 사람 | 부서30? | 부서20·CLERK? | 첫 조건 | 둘째 조건 |
| --- | --- | --- | --- | --- |
| ADA | 아니오 | 예 | 통과 | 통과 |
| BEN | 예 | 아니오 | 통과 | 제외 |
| CARA | 아니오 | 아니오 | 제외 | 제외 |
| FINN | 예 | 아니오 | 통과 | 제외 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| BETWEEN 상한을 2999로 | CARA·ELLA 제외 | 경계값 3000 |
| CLERK를 SALESMAN으로 | 둘째 조건 BEN·FINN | 직업 기준 변경 |
| deptno IN (10,20) | ADA·CARA·DAN·ELLA | 두 부서 포함 |

원하는 직업 외 사람이 나오면 OR 범위와 괄호를 본다. 같은 행이 빠지면 >와 >=, BETWEEN 양 끝을 비교한다. 문자열 대소문자 실험은 DB 설정을 확인하지 않고 모든 환경의 규칙으로 외우지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 상세 연산자 우선순위와 collation·최적화·인덱스 영향은 선택 학습이다. [MariaDB 연산자 우선순위](https://mariadb.com/docs/server/reference/sql-structure/operators/operator-precedence)에서 확인할 수 있다. 본문은 실제 조건 문장의 의미와 결과를 우선한다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. BETWEEN은 상한을 포함하는가?
2. A OR B AND C는 어떤 묶음인가?
3. WHERE는 결과 열을 고르는가?
4. 문자 비교는 언제나 대소문자를 구분하는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

포함한다. A OR (B AND C)다. 행을 거른다. 설정에 영향을 받으므로 언제나 그렇다고 할 수 없다.

</details>

| 확인 | 질문 |
| --- | --- |
| 묶음 | AND·OR·괄호 |
| 경계 | 초과·이상·미만·이하 |
| 대상 | 행과 열 구별 |

[장별 연습문제](실습/연습문제/02_SQL_WHERE와_조건연산자_연습문제.md) · 다음은 [LIKE·NULL](03_SQL_LIKE와_NULL.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
