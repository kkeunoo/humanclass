# 10. UNION과 UNION ALL — 조회 결과를 세로로 이어 붙이기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

같은 한 행을 두 번 가져와 붙였을 때 중복을 남길지 정한다. 원본 표에 행을 추가하는 INSERT와 조회 결과를 합치는 UNION을 구분한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

UNION·UNION ALL의 결과 행 수를 예상한다. 양쪽 열 개수·대응 위치를 맞추고 JOIN처럼 가로로 붙이는 것과 구별한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

UNION은 두 조회 결과를 위아래로 붙이면서 결과 행 전체가 같은 중복을 제거한다. UNION ALL은 중복도 모두 남긴다. SELECT ename,sal에서 이름이 같아도 급여가 다르면 결과 행 전체가 같지는 않다. 첫 열만 기준으로 중복을 없애는 것으로 이해하지 않는다.

| 연산 | 붙이는 방향 | 중복 | 원본 변경 |
| --- | --- | --- | --- |
| UNION | 같은 모양의 행을 세로로 | 제거 | 없음 |
| UNION ALL | 같은 모양의 행을 세로로 | 유지 | 없음 |
| JOIN | 관계에 맞는 열을 가로로 | 조건에 따른 행 조합 | 조회 자체는 없음 |

양쪽 결과 열의 개수는 같아야 한다. 열의 의미도 같은 위치끼리 대응하게 정한다. 이름 열 아래 급여 열을 넣어 문법상 값이 보이더라도 읽는 사람에게 올바른 자료가 되지는 않는다. 두 결과가 입력 순서대로 정렬 보장된다고 가정하지 않는다. 최종 순서는 ORDER BY로 요청한다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB UNION](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/union). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/10_SQL_UNION과_UNION_ALL.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT ename FROM book_emp WHERE deptno=10
UNION
SELECT ename FROM book_emp WHERE deptno=10
ORDER BY ename;
SELECT ename FROM book_emp WHERE deptno=10
UNION ALL
SELECT ename FROM book_emp WHERE deptno=10
ORDER BY ename;
```

10번 부서는 DAN 한 명이다. 같은 조회를 두 번 실행해 결과를 붙일 때 UNION은 같은 결과 행을 하나로 남긴다. UNION ALL은 각 조회에서 나온 한 행씩 두 행이다. 같은 이름 두 줄이 나왔다고 원본에 사원이 복제된 것은 아니다.

**가상 자료 기준 예상 결과:**

첫 결과 **DAN 한 행**, 둘째 **DAN 두 행**이다. 원본 book_emp는 여전히 여섯 행이다.



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 437–445행 · **원본 발췌**

```sql
-- union으로 겹치는것을 제외하고 합쳐서 한 번에 보여줄 수 있음
select * from emp where deptno = 10
union
select * from emp where deptno = 10;

-- union all은 겹치더라도 나오게 함, union보다 활용도가 높음
select * from emp where deptno = 10
union all
select * from emp where deptno = 10;
```

**발췌 바로 풀이:** 두 `SELECT`가 똑같은 행 집합을 만든다. `UNION`은 같은 결과 행을 한 번만 남기고, `UNION ALL`은 양쪽 행을 모두 남긴다. 따라서 이번 예제에서는 `UNION ALL` 결과 행 수가 한쪽 조회의 **두 배**다. 원본 `EMP`에서 사원이 복제되는 것은 아니다.

내 원본은 실제 EMP 10번 부서 조회를 똑같이 두 번 붙여 차이를 비교한다. 강사님에는 열 하나와 두 개를 붙이려는 반례가 주석으로 막혀 있다. 실행되지 않은 반례를 정상 실행 결과처럼 적지 않는다. 내 “UNION ALL 활용도가 높음” 메모는 모든 문제에서 우월하다는 규칙이 아니다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

첫 SELECT의 결과 행 목록 + 둘째 SELECT의 같은 열 구조 → 중복 정책 → 최종 결과·정렬이다. 입력 테이블이 반드시 서로 달라야 하는 것도 아니다. 같은 표의 다른 조건 결과를 합칠 수 있다. 함수 import 대신 두 결과의 구조가 연결되는 지점을 읽는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 같은 쿼리를 반복해 중복 여부 한 가지만 비교했다. **설계 판단:** 중복을 의미 있게 보존할지·제거할지 요구에 따라 고른다. **확장 주의:** UNION ALL이 항상 더 좋은 답이라거나 UNION이 원본 중복을 삭제한다는 설명은 틀리다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_sql/Script.sql` 410–414행 · **원본 발췌**

```sql
/*
select ename from emp where deptno = 10
union all
select ename, sal from emp where deptno = 10;
*/
```

열 개수 불일치 반례만 비교상 필요해 인용한다. 강사님 코드는 주석 처리되어 원본 실행에는 포함되지 않는다. 내 원본에는 그 반례가 없어 새 문제를 풀 때 양쪽 열 모양을 확인하는 점검 항목으로 사용한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 단계 | UNION | UNION ALL |
| --- | --- | --- |
| 첫 조회 | DAN | DAN |
| 둘째 조회 | DAN | DAN |
| 붙인 결과 | DAN | DAN, DAN |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 둘째 부서를 30으로 | DAN·BEN·FINN | 서로 다른 이름 |
| 둘째 SELECT 열 하나 추가 | 열 수 오류 | 결과 모양 불일치 |
| UNION을 UNION ALL로 | 중복 유지 | 정책 변경 |

열 수 오류면 양쪽 SELECT 목록을 세어 본다. 중복이 안 없어지면 선택한 열 전체 값이 같은지 본다. 결과 표시 순서는 ORDER BY 없이 보장된 것으로 외우지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 결과 자료형 변환·중복 제거 비용·여러 UNION의 정렬·LIMIT 범위는 추가 학습이다. 현재는 행 전체와 대응 열을 기준으로 읽는다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. UNION은 원본 행을 삭제하는가?
2. 중복 판단은 첫 열만인가?
3. UNION ALL이면 원본 사원이 늘어나는가?
4. 양쪽 열 개수가 달라도 되는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

조회 결과만 중복 제거한다. 행 전체다. 원본은 변하지 않는다. 열 개수를 맞춰야 한다.

</details>

| 선택 | 목적 |
| --- | --- |
| UNION | 중복 제거 결과 |
| UNION ALL | 모든 결과 행 |
| 열 대응 | 개수·위치·의미 |

[장별 연습문제](실습/연습문제/10_SQL_UNION과_UNION_ALL_연습문제.md) · 다음은 [서브쿼리](11_SQL_서브쿼리.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
