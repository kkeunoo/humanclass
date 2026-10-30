# 19. SQL 실무 코딩스타일 — 요구·관계·집계 단위를 드러내기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

이 장은 별도 수업 19번 원본이 아니라 실제 작성한 쿼리에서 읽기 쉬운 표현을 찾아 만든 새 복습이다. 줄바꿈뿐 아니라 연결 조건과 집계 대상을 읽는 사람이 설명할 수 있는지 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

필요한 결과 열·표 별칭·관계별 ON·그룹 키·정렬 기준을 명확히 적는다. 표현 정리와 실제 논리 수정, 더 좋은 코드와 목적이 다른 코드를 구별한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

SQL을 읽는 사람은 먼저 어떤 대상을 어떤 단위로 보여 주려는지 알아야 한다. 긴 한 줄을 여러 줄로 바꿔도 관계가 틀리면 정답이 되지 않는다. 반대로 같은 의미의 두 쿼리라면 연결과 필터가 구분된 쪽이 검토하기 편할 수 있다.

| 결정 | 먼저 적을 말 | 코드 표현 |
| --- | --- | --- |
| 결과 | 부서번호·이름·인원·최고−최저 | SELECT 열 명시 |
| 관계 | 부서의 사원 | JOIN ON 번호 대응 |
| 보존 | 사원 없는 부서도 | DEPT LEFT JOIN EMP |
| 집계 | 부서 단위 | 두 부서 열 GROUP BY |
| 인원 | 실제 사원만 | COUNT(e.empno) |
| 순서 | 부서번호순 | ORDER BY d.deptno |

별칭은 짧게 만드는 목적만이 아니다. e는 사원·d는 부서라고 먼저 정해 같은 이름 열의 출처를 보이게 한다. 집계 별칭 people·sal_gap은 결과 열을 설명한다. 다만 별칭 규칙·대문자·줄바꿈은 팀에서 일관되게 정할 수 있는 표현 선택이다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB JOIN](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax), [SELECT](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/select). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/19_SQL_실무_코딩스타일.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
SELECT
    d.deptno,
    d.dname,
    COUNT(e.empno) AS people,
    MAX(e.sal) - MIN(e.sal) AS sal_gap
FROM book_dept d
LEFT JOIN book_emp e ON e.deptno = d.deptno
GROUP BY d.deptno, d.dname
ORDER BY d.deptno;
```

한 명인 ALPHA의 최고·최저는 같은1300이므로 차이0이다. BETA는3000−1000=2000, GAMMA는1600−1500=100이다. EMPTY는 사원이 없어 인원0이지만 급여 차이는NULL이다. 0명과 차이0원을 자동으로 같은 뜻으로 만들지 않는다. 결과의 한 행은 사원이 아니라 부서다.

**가상 자료 기준 예상 결과:**

| 번호 | 부서 | 인원 | 급여 차이 |
| --- | --- | --- | --- |
| 10 | ALPHA | 1 | 0 |
| 20 | BETA | 3 | 2000 |
| 30 | GAMMA | 2 | 100 |
| 40 | EMPTY | 0 | NULL |



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

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

**발췌 바로 풀이:** 내 실제 부서별 차이 문제다. 기본 내부 조인 뒤 사원 없는 부서도 보는 LEFT 버전을 추가했다. 서로 다른 출력 범위를 같은 답의 스타일 차이만으로 보지 않는다.
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

**발췌 바로 풀이:** 내 원본에 한 줄 풀이와 관계마다 JOIN ON을 나눈 개선 풀이가 둘 다 있다. 교재가 원본에 없던 개선을 내 과거 작성물로 꾸민 것이 아니다.

내 SALES·등급 문제는 처음 한 줄로 관계를 적었다가 EMP–DEPT와 EMP–SALGRADE를 각각 나눠 적었다. 실제 개선 기록이므로 잘한 점으로 남긴다. 부서별 차이의 LEFT 추가는 단순 줄바꿈이 아니라 사원 없는 부서를 결과에 포함하는 동작 변경이다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

요구의 결과 단위 → SELECT 목록 → FROM 보존 대상 → JOIN별 관계 → WHERE 개인 조건 → GROUP BY 요약 단위 → HAVING 그룹 조건 → ORDER BY다. 이 순서는 작성·검토를 위한 질문이며 서버 실행 계획을 고정한 순서가 아니다. 각 별칭·결과 열의 정의를 현재 SQL 안에서 모두 확인할 수 있다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 실제 개선은 관계별 ON과 출력 열을 명시해 목적을 보이게 했다. **수정할 점:** 원본 평균 문제의 sal 그룹 추가는 줄바꿈 문제가 아니라 논리 수정 대상이다. **주의:** NULL을 보기 좋게0으로 바꾸는 것 역시 의미를 바꿀 수 있다. 필요한 경우 업무에서0과미정의 차이를 먼저 정한다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님과 내 코드를 길이로 평가하지 않는다. WHERE의 연도 누락은 강사님 조건이 더 정확했고 빈 등급 집계는 내 COUNT(사원값)가 더 정확했다. 이번 스타일 예제는 그 검토 기준을 하나로 연결한다. 같은 전체 코드를 두 번 싣기보다 실제로 나눠 쓴 내 개선을 인용한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 검토 질문 | 이번 답 |
| --- | --- |
| 한 행의 단위 | 부서 |
| 빠지면 안 되는 행 | 빈 부서 |
| 중복 집계 방지 | 부서번호·이름으로 그룹 |
| NULL의 뜻 | 계산할 급여 없음 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| LEFT를 내부 JOIN으로 | EMPTY 제외 | 보존 정책 변경 |
| COUNT(e.empno)를COUNT(*)로 | EMPTY1 | 빈 조합 행 포함 |
| 열 별칭만 변경 | 값 동일 | 표현 변경 |
| WHERE e.sal>2000 추가 | 낮은 급여·빈 부서 제외 | 입력 행 정책 변경 |

수정 뒤 결과가 달라졌으면 줄바꿈·이름만 바꿨는지 관계·조건·그룹도 바뀌었는지 본다. 여러 조인으로 인원이 커지면 관계의 매칭 수와 집계 단위를 확인한다. 예쁜 정렬만으로 의미 검토를 대신하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 팀 SQL 스타일 규칙·자동 포맷 도구·실행 계획·대용량 보고서 성능 설계는 추가 학습이다. 원본과 같은 결과를 원한다면 먼저 입력·행 단위·NULL 정책을 맞춘다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. INNER→LEFT는 표현만 바뀌는가?
2. 빈 부서 차이는 반드시0인가?
3. 별칭 변경은 결과 값도 바꾸는가?
4. 그룹에 sal을 잘못 넣은 문제는 들여쓰기로 해결되는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

보존 대상이 바뀐다. 기본 집계에서는 NULL이다. 이름만 일관되게 바꾸면 값은 같다. 그룹 기준 자체를 수정해야 한다.

</details>

| 개선 종류 | 예 |
| --- | --- |
| 표현 | 줄바꿈·별칭 |
| 논리 | 조건·그룹·보존 |
| 정책 | NULL·빈 그룹 의미 |

[장별 연습문제](실습/연습문제/19_SQL_실무_코딩스타일_연습문제.md) · 다음은 [종합실습](20_SQL_종합실습.md)이다.
