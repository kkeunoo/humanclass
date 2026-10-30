# 18. 재귀 CTE — 시작 행에서 다음 관계를 반복해 따라가기

[SQL 목차](README.md) · [실습 데이터](00_SQL_실습데이터와_스크립트_읽기.md)

한 번의 자기 조인은 관리자와 부하 한 단계를 연결한다. 계층을 여러 단계로 따라가려면 이전 단계의 결과를 다음 단계 연결에 사용한다. 두 원본에 실제 재귀 CTE가 있으므로 이 주제는 수업 본문이다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

시작 부분·반복 부분·종료를 설명한다. UNION ALL 양쪽 열 위치, 깊이·경로 정렬·들여쓰기의 역할을 구분하고 현재 원본의 부서 연결 추가를 반영한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

CTE는 WITH로 이름 붙인 조회 결과다. WITH RECURSIVE는 그 결과 이름을 반복 부분에서도 참조해 계층을 이어갈 수 있게 한다. 시작 부분은 루트 행을 고르고 반복 부분은 이전 단계 행을 부모로 가진 새 행을 찾는다. 더 찾을 행이 없으면 정상적인 이 계층의 반복이 끝난다.

| 부분 | 역할 | 새 예제 |
| --- | --- | --- |
| 시작 SELECT | 맨 위 관리자 | mgr IS NULL |
| UNION ALL | 다음 단계 결과 연결 | 시작과 같은 열 모양 |
| 재귀 SELECT | 이전행의 자식 찾기 | e.mgr=org.empno |
| depth+1 | 단계 증가 | 루트1·부하2·손아래3 |
| 바깥 SELECT | 완성된 결과 읽기 | 깊이·번호 순서 |

재귀함수라는 원본 비유와 달리 여기서 CREATE FUNCTION을 정의한 것은 아니다. 이름 붙인 조회를 스스로 참조하는 CTE구조다. 양쪽 결과 열은 별칭 이름이 아니라 위치로 대응하므로 같은 자리에 같은 의미·맞는 자료형이 와야 한다. 재귀 결과의 출력 순서도 바깥 ORDER BY로 명시한다.

> 📚 **출처 · 본문 설명 확인:** [MariaDB Recursive CTE overview](https://mariadb.com/docs/server/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview). 실제 수업 문법의 의미를 확인한 근거다. 아래 표·가상 데이터·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제.** [준비부터 포함한 전체 SQL](실습/책형_복습/18_SQL_Recursive_CTE.sql)을 제공한다. 원본 EMP와 다른 가상 자료 book_emp·book_dept를 쓴다. MariaDB에 연결한 SQL 편집기에서 연습용 DB를 선택하고 같은 연결의 준비문 → 조회문 순서로 실행한다. 연결을 바꾸면 임시 표는 이어지지 않는다. 새 연결에서 실행하거나 준비문으로 다시 시작한다.

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
UPDATE book_emp SET mgr=1 WHERE empno=4;
```

표 생성·삽입 문법은 14·15장에서 설명한다. TEMPORARY는 원래 수업 구문으로 승격한 것이 아니라 예제 자료를 연결 안에서만 쓰기 위한 새 실행 장치다. 기존 영구 EMP·DEPT를 바꾸는 준비문이 아니다. 임시 표의 상세 수명·권한은 아래 TIP에서 구별한다.

</details>

```sql
WITH RECURSIVE org(empno,ename,mgr,depth) AS (
 SELECT empno,ename,mgr,1 FROM book_emp WHERE mgr IS NULL
 UNION ALL
 SELECT e.empno,e.ename,e.mgr,org.depth+1
 FROM book_emp e JOIN org ON e.mgr=org.empno
)
SELECT empno,ename,mgr,depth FROM org ORDER BY depth,empno;
```

이 장만 DAN의 관리자를 ADA 1번으로 바꾼 새 자료다. CARA에서 시작해 부하 ADA·BEN·ELLA·FINN을 얻고, 그중 ADA의 부하 DAN을 다음에 찾는다. 세 번째 단계 뒤에는 더 연결할 자식이 없어 끝난다. 깊이 정렬은 조직 경로순 정렬과 다른 선택이며 원본의 sort_key와 구분한다.

**가상 자료 기준 예상 결과:**

| 사원번호 | 이름 | 관리자번호 | 깊이 |
| --- | --- | --- | --- |
| 3 | CARA | NULL | 1 |
| 1 | ADA | 3 | 2 |
| 2 | BEN | 3 | 2 |
| 5 | ELLA | 3 | 2 |
| 6 | FINN | 3 | 2 |
| 4 | DAN | 1 | 3 |



**검증 범위:** 공통 조회의 행·값은 별도 SQLite 메모리 DB에서 교차 확인하고 MariaDB 공식 문법과 대조한다. MariaDB 서버에 접속해 실행한 결과는 아니다. 문자열 비교 설정·숫자 표시 자릿수·오류·실행 계획 등 DB별 차이를 같은 결과라고 단정하지 않는다. D 드라이브 원본 Script.sql을 통째로 실행하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 930–939행 · **원본 발췌**

```sql
-- 무한 대댓글
select 
	empno, ename, mgr, 1 as Level
from emp
where mgr is null
union all
select 
	empno, ename, mgr, 2 as Level
from emp
where mgr = 7839;
```

**발췌 바로 풀이:** `mgr IS NULL`은 맨 위 관리자 행을, `mgr = 7839`는 특정 관리자의 바로 아래 사원을 가져온다. `UNION ALL`로 둘을 붙이면 **1단계·2단계까지만** 직접 적은 것이다. 아래 단계까지 자동으로 내려가지는 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 941–962행 · **원본 발췌**

```sql
-- 아래처럼 재귀함수로 각 Level을 부여할 수 있다
with recursive emp_recu as (
	select 
		empno, ename, mgr, de.dname, job,
		lpad(ename, length(ename), ' '),
		1 as level,
		cast(ename as char(200)) as sort_key
	from emp as em
	join dept as de on (em.deptno = de.deptno)
	where mgr is null
	union all
	select
		e.empno, e.ename, e.mgr, d.dname, e.job,
		lpad(e.ename, er.level*4+length(e.ename), ' '),
		er.Level+1 as level,
		concat(er.sort_key, '-', cast(e.ename as char(200))) as sort_key
	from emp e
		join emp_recu er on (e.mgr = er.empno)
		join dept as d on (e.deptno = d.deptno)
)
select * from emp_recu
order by sort_key;
```

**발췌 바로 풀이:** 현재 원본은 이전 Wiki와 달라 부서명 dname·직업 job을 추가했고 시작·반복 양쪽에서 DEPT를 연결한다. 양쪽 열 개수와 위치가 함께 늘었다. 예전의 괄호·대소문자 차이만 있는 설명으로 현재 코드를 대체하지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_sql/Script.sql` 1009–1038행 · **원본 발췌**

```sql
with recursive comment_recu as (
    select
        comment_code,
        member_code,
        member_id,
        comment_content,
        date_format(comment_time, '%Y.%m.%d %H:%i') as comment_time,
        lpad(member_id, length(member_id), ' '),
        1 as level,
        cast(member_id as char(200)) as sort_key
    from
        comment c join member m using(member_code)
    where
        parent_comment_code is null
        and board_code = :board_code
    union all
    select
        c.comment_code as comment_code,
        m.member_id as member_id,
        c.comment_content as comment_content,
        c.parent_comment_code as parent_comment_code,
        date_format(c.comment_time, '%Y.%m.%d %H:%i') as comment_time,
        lpad(m.member_id, (cr.level * 4)+ length(m.member_id), ' '),
        cr.level + 1 as level,
        concat(cr.sort_key, '-', cast(m.member_id as char(200))) as sort_key
    from
        comment c join member m using(member_code)
    join comment_recu cr on
        c.parent_comment_code = cr.comment_code
    )
```

**발췌 바로 풀이:** 댓글 응용 시도다. 시작과 반복의2·3·4번째 열 의미가 달라 단순히 열 개수가 같다는 이유로 완성 결과라 볼 수 없다. :board_code바인딩과 테이블 구조·최종 SELECT가 필요한 별도 문맥이다.

양쪽 두 단계 UNION ALL 시도는 특정 관리자의 바로 아래까지만 적는다. 실제 WITH RECURSIVE는 e.mgr=er.empno로 다음 단계를 찾고 level을 늘린다. 내 현재 941–962행은 DEPT 조인을 추가해 부서명·직업까지 보인다. 원본의 CAST(ename AS CHAR(200))는 길어지는 정렬 경로의 열 폭을 미리 확보하려는 뜻이고 LPAD는 화면 들여쓰기다. 연결·깊이·표시·정렬을 같은 역할로 보지 않는다.

<a id="connections"></a>

## 5. 자료·조건·결과가 연결되는 흐름

루트 SELECT → 재귀 이름 emp_recu → 자식의 mgr과 이전 empno 연결 → level+1·경로 문자열 → 더 없을 때 종료 → 바깥 ORDER BY sort_key다. 내 추가 댓글은 parent_comment_code와 comment_code로 관계를 바꾼 시도다. 양쪽 SELECT의 위치를 맞추고 최종 결과를 읽는 문장·바인딩 값까지 준비해야 완전한 실행 예제가 된다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 관리자 관계를 댓글 부모·자식에 적용해 보려 했고 현재는 부서 정보도 연결했다. **교정:** 댓글 시작 2·3·4열은 member_code·member_id·comment_content인데 반복은 member_id·comment_content·parent_comment_code라 어긋난다. **조건:** 각 사원이 부서와 매칭되어야 현재 내부 부서 조인에서 남는다. **한계:** 순환 검사·깊이 제한 정책은 구현돼 있지 않아 정상 트리 전제를 읽어야 한다.

원본 오류·수업용 단순화·목적별 선택을 구별한다. 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_sql/Script.sql` 871–889행 · **원본 발췌**

```sql
with recursive emp_recu as (
	select 
		empno, ename, mgr,
		lpad(ename, length(ename), ' '),
		1 as level,
		cast(ename as char(200)) as sort_key
	from emp
	where mgr is null
	union all
	select
		e.empno, e.ename, e.mgr, 
		lpad(e.ename, (er.level*4)+length(e.ename), ' '),
		er.level+1 as level,
		concat(er.sort_key, '-', cast(e.ename as char(200))) as sort_key
	from emp e
		join emp_recu er on (e.mgr = er.empno)
)
select * from emp_recu
order by sort_key;
```

강사님 재귀 부분만 필요해 인용한다. 두 원본의 부모 연결 원리는 같지만 현재 내 코드에는 부서명·직업이 추가되어 있다. 강사님 구현과 내 현재 구현을 예전 행 범위로 비교하지 않는다. 댓글의 직접 대응 강사님 예제는 없으므로 완성 정답이라고 만들지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 반복 | 새로 찾은 행 | 깊이 |
| --- | --- | --- |
| 시작 | CARA | 1 |
| 첫 연결 | ADA·BEN·ELLA·FINN | 2 |
| 다음 연결 | DAN | 3 |
| 다음 연결 | 없음 | 종료 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| DAN 관리자를 3으로 | DAN 깊이 2 | 직접 부하 |
| 시작 조건을 empno=1로 | ADA·DAN만 | 다른 시작점 |
| depth 증가를 제거 | 깊이 표시 부정확 | 관계 탐색과 표시 값은 별개 |

계층이 빠지면 시작 행·부모 키·부서 내부 조인을 본다. 열 자료가 이상하면 UNION ALL의 각 위치를 비교한다. 경로가 잘리면 시작 열의 자료형·폭을 확인한다. 순환 가능 자료를 무제한 반복 시험으로 넣지 않고 별도 정책부터 정한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 순환 탐지·최대 반복 설정·깊이 제한·긴 경로 정렬·계층 자료의 다른 설계는 추가 학습이다. 본문은 실제 수업의 시작·다음 행 연결을 설명한다. 외부 댓글 테이블 구조가 없으면 현재 메모의 실행 결과는 이후 첨부 자료와 함께 판단한다.

예제 실행 장치인 임시 표는 [MariaDB CREATE TABLE](https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-table)의 TEMPORARY 설명을 참고한다. 본문 쿼리와 준비 장치를 구별하며 선택 확장을 필수 문제로 요구하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 시작 SELECT는 무엇을 고르는가?
2. 다음 단계의 연결 열은?
3. UNION ALL의 대응은 이름인가 위치인가?
4. 현재 내 원본에 새로 붙은 부서 정보를 예전 주석 차이만으로 설명해도 되는가?

<details>
<summary>풀이 — 먼저 직접 설명한 뒤 펼치기</summary>

루트 행이다. 자식 mgr과 이전 empno다. 위치다. 현재 열·조인을 다시 읽어야 한다.

</details>

| 부분 | 역할 |
| --- | --- |
| 시작 | 루트 |
| 반복 | 다음 관계 |
| level | 깊이 |
| sort_key | 결과 정렬 |

[장별 연습문제](실습/연습문제/18_SQL_Recursive_CTE_연습문제.md) · 다음은 [실제 문제 비교](실습_SQL_원본문제_비교.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
