# 09. CASE — 조건에 맞는 값을 결과 열에 넣기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

행을 남길지 판단하는 WHERE와 그 행의 결과 값을 고르는 CASE는 다르다. 직업별 급여 계산과 수당 표시를 같은 행 위에서 비교한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

단순 CASE와 조건식 CASE를 구분한다. WHEN 순서·ELSE·END의 의미와 원본 급여가 바뀌지 않는 이유를 설명한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

CASE는 조건에 따라 결과 값 하나를 고르는 식이다. CASE job WHEN 값 THEN 결과는 job과 각 값을 비교한다. CASE WHEN 조건 THEN 결과는 각 조건이 참인지 검사한다. 하나의 값을 비교할 때는 앞 형식이, 서로 다른 범위·NULL 상태를 판단할 때는 뒤 형식이 읽기 편할 수 있다.

| 구성 | 역할 | 확인 |
| --- | --- | --- |
| CASE 뒤 비교 값 | 단순 형식의 대상 | job |
| WHEN | 비교 값 또는 조건 | CLERK / sal>=3000 |
| THEN | 해당 결과 | sal*1.05 |
| ELSE | 일치하는 갈래 없음 | sal |
| END | 식 끝 | 별칭을 뒤에 붙일 수 있음 |

여러 조건이 겹치면 먼저 맞는 갈래의 결과를 고른다. 모든 갈래를 각각 실행해 여러 값을 더하는 구조가 아니다. ELSE를 빼고 맞는 갈래도 없으면 NULL이 된다. CASE에서 결과를 정한다고 행 자체가 빠지거나 원본 열이 변경되지는 않는다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB CASE operator](https://mariadb.com/docs/server/reference/sql-functions/control-flow-functions/case-operator). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/09_SQL_CASE_조건식.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT ename, job, sal,
 CASE job WHEN 'CLERK' THEN sal*1.05
          WHEN 'SALESMAN' THEN sal*1.03 ELSE sal END AS adjusted
FROM book_emp ORDER BY empno;
SELECT ename,
 CASE WHEN sal >= 3000 THEN '높음'
      WHEN sal >= 1500 THEN '중간' ELSE '기본' END AS band
FROM book_emp ORDER BY empno;
```

ADA는 CLERK라 5%, BEN은 SALESMAN이라 3% 증가한 값을 결과로 계산한다. CARA는 두 직업이 아니어서 원래 급여다. 둘째 CASE는 3000 이상을 먼저 검사하므로 3000인 사람이 중간에 들어가지 않는다. CASE는 표시용 분류일 뿐 급여 저장 변경이 아니다.

**가상 자료 기준 예상 결과:**

사원번호순 adjusted는 **1050·1648·3000·1365·3000·1545**다. band는 **기본·중간·높음·기본·높음·중간**이다. 원본 sal은 1000·1600·3000·1300·3000·1500 그대로다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 331–340행 · **원본 발췌**

```sql
-- case문은 end로 무조건 닫아주어야 함
-- when과 then으로 조건을 줘서 바꿀 수 있음
select 
	job, sal, 
	case job
		when 'CLERK' then sal * 1.05
		when 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;
```

**발췌 바로 풀이:** `CASE job` 뒤의 `WHEN 'CLERK'`는 각 행의 `job` 값과 비교한다. CLERK면 `sal * 1.05`, SALESMAN이면 `sal * 1.03`, 어느 쪽도 아니면 `ELSE sal`을 `upsal` 열에 보여 준다. 급여 원본 값은 그대로이며, `END`로 식을 닫는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 342–350행 · **원본 발췌**

```sql
-- case옆에 바로 쓰지 않으면 where조건 if처럼 진행할 수 있음
select 
	job, sal, 
	case 
		when job = 'CLERK' then sal * 1.05
		when job = 'SALESMAN' then sal * 1.03
		else sal
	end as upsal
from emp;
```

**발췌 바로 풀이:** 이번에는 `CASE` 뒤에 열 이름을 붙이지 않고 `WHEN job = 'CLERK'`처럼 **참·거짓 조건식**을 쓴다. 이 예제의 결과는 위 형식과 같은 의도다. 내 주석의 “`WHERE`처럼 진행”은 조건을 쓰는 모양을 빗댄 것이며, 이 `CASE` 자체가 행을 버리는 `WHERE` 절은 아니다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 352–359행 · **원본 발췌**

```sql
-- if, null로 아래처럼 null일 때 0으로 바꿀 수 있음
select 
	sal, comm,
	case 
		when comm is null then 0
		else comm
	end
from emp;
```

**발췌 바로 풀이:** `comm IS NULL`인 행만 결과 열에 0을 표시하고, 값이 있으면 원래 `comm`을 표시한다. [08장](08_SQL_숫자_날짜_NULL함수.md)의 `IFNULL`도 같은 문제를 짧게 푸는 방법이다. 어느 방법이든 이 `SELECT`만으로 표 안의 수당이 0으로 저장되지는 않는다.

내 코드와 강사님 코드는 같은 직업별 계산을 두 CASE 형식으로 썼다. 내 “WHERE조건 if처럼”이라는 메모는 조건식 모양의 비유일 뿐 CASE가 행을 버리는 WHERE라는 뜻은 아니다. 수당 NULL을 0으로 고르는 마지막 CASE는 IFNULL과 같은 목적의 이 예제 결과를 만든다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

각 행 job·sal → CASE의 갈래 검사 → 해당 THEN 또는 ELSE 값 → adjusted라는 별칭 → 결과 행이다. 조건식 형식은 첫 참 갈래를 고른다. 결과의 여러 열 중 한 열만 CASE로 만들 수도 있으며 다른 열·행 수는 그대로 유지된다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 두 형식을 실제로 비교하고 END가 필요함을 적었다. **설명 보완:** 조건 판단과 행 필터를 구별한다. **개선:** 여러 범위가 겹치면 좁은 높은 기준부터 놓는 등 정책이 드러나게 쓴다. 단순히 WHEN 개수만 늘려 정확해지는 것은 아니다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



동일한 계산을 반복 인용할 필요가 없어 내 실제 원본을 중심으로 두 형식을 설명한다. 강사님 코드가 항상 더 낫다는 전제 없이 이 경우 양쪽 의미가 같음을 남긴다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 급여 | >=3000 | >=1500 | 선택 |
| --- | --- | --- | --- |
| 1000 | 거짓 | 거짓 | 기본 |
| 1600 | 거짓 | 참 | 중간 |
| 3000 | 참 | 뒤 갈래 불필요 | 높음 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 두 급여 WHEN 순서 바꾸기 | 3000도 중간 | 먼저 맞는 갈래 |
| ELSE sal 제거 | 두 직업 외 NULL | 일치 없음 |
| CASE 결과 별칭만 변경 | 값 동일 | 표시 이름 |

범위 분류가 이상하면 겹치는 조건의 순서를 본다. 빈 값이 생기면 ELSE가 빠졌는지 확인한다. CASE 결과를 보고 원본 변경 여부를 추측하지 말고 UPDATE와 구분한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 결과 자료형 결정·조건 집계·복잡한 중첩 CASE는 추가 학습이다. 현재는 한 행에서 한 결과 값을 고르는 식의 의미를 먼저 익힌다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. CASE가 행을 제거하는가?
2. 두 WHEN에 모두 맞으면?
3. ELSE 없고 일치도 없으면?
4. END 뒤 별칭은 원본 열 이름 변경인가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

제거하지 않는다. 먼저 맞는 갈래다. NULL이다. 결과 표시 이름이다.

</details>

| 구별 | 핵심 |
| --- | --- |
| WHERE | 행 선택 |
| CASE | 값 선택 |
| UPDATE | 저장 변경 |

[장별 연습문제](실습/연습문제/09_SQL_CASE_조건식_연습문제.md) · 다음은 [UNION](10_SQL_UNION과_UNION_ALL.md)이다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
