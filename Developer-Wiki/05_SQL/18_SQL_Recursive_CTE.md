# 18. 재귀 CTE — 관리자 관계를 여러 단계로 따라가기

[SQL 목차](README.md) · [이전: 인덱스](17_SQL_Index와_AUTO_INCREMENT.md) · [다음: 실제 문제 풀이](실습_SQL_원본문제_비교.md)

`EMP.MGR`에는 관리자의 사원 번호가 들어 있다. 한 단계의 자기 조인은 [13장](13_SQL_Outer_JOIN과_Self_JOIN.md)에서 봤다. 재귀 CTE는 이 관계를 **관리자 → 부하 → 그 부하의 부하**로 반복해서 따라간다. 두 원본에 실제로 긴 쿼리가 있으므로 이 주제도 본문이다.

## 먼저: 세 사람을 단계로 읽기

제공된 초기 `EMP` 자료의 일부를 **설명용 관계표**로 줄였다.

| 사원 | EMPNO | MGR | 단계 |
| --- | ---: | ---: | ---: |
| KING | 7839 | `NULL` | 1 |
| JONES | 7566 | 7839 | 2 |
| SCOTT | 7788 | 7566 | 3 |

`MGR IS NULL`인 KING에서 시작한다. 다음에는 `JONES.MGR = KING.EMPNO`, 그다음에는 `SCOTT.MGR = JONES.EMPNO`를 따라간다. 두 단계만 직접 `UNION ALL`로 쓴 첫 실습은 SCOTT까지 자동으로 내려가지 못한다. 재귀 CTE의 반복 부분이 이 연결을 계속 만든다.

<!-- chapter-toc -->

- [1. 두 단계만 직접 적은 첫 시도](18_SQL_Recursive_CTE.md#section-1)
- [2. `WITH RECURSIVE`의 시작 부분과 반복 부분](18_SQL_Recursive_CTE.md#section-2)
- [3. 이후 내 댓글 계층 연습의 열 순서 점검](18_SQL_Recursive_CTE.md#section-3)
- [직접 확인할 질문](18_SQL_Recursive_CTE.md#section-4)
- [추가로 알면 좋은 것](18_SQL_Recursive_CTE.md#section-5)

<a id="section-1"></a>

## 1. 두 단계만 직접 적은 첫 시도

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 859–869행 · **원본 발췌**

```sql
-- 무한 대댓글

select 
	empno, ename, mgr, 1 as level
from emp
where mgr is null
union all
select 
	empno, ename, mgr, 2 as level
from emp
where mgr = 7839;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 930–939행 · **원본 발췌**

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

`mgr IS NULL`은 맨 위 관리자 행을, `mgr = 7839`는 특정 관리자의 바로 아래 사원을 가져온다. `UNION ALL`로 둘을 붙이면 **1단계·2단계까지만** 직접 적은 것이다. 아래 단계까지 자동으로 내려가지는 않는다.

<a id="section-2"></a>

## 2. `WITH RECURSIVE`의 시작 부분과 반복 부분

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 871–889행 · **원본 발췌**

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

### 내 코드

출처: `me/workspace_sql/Script.sql` 941–960행 · **원본 발췌**

```sql
-- 아래처럼 재귀함수로 각 Level을 부여할 수 있다
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
		lpad(e.ename, er.level*4+length(e.ename), ' '),
		er.Level+1 as level,
		concat(er.sort_key, '-', cast(e.ename as char(200))) as sort_key
	from emp e
		join emp_recu er on (e.mgr = er.empno)
)
select * from emp_recu
order by sort_key;
```

첫 `SELECT`는 `mgr IS NULL`인 **시작 행**을 만든다. `UNION ALL` 뒤의 `SELECT`는 이전 단계 `emp_recu er`의 사원 번호를 새 사원 `e.mgr`와 연결해 다음 단계를 만든다. `er.level+1`이 깊이를 늘리고, `sort_key`는 이름 경로를 이어 붙여 출력 순서를 만든다. `LPAD`는 레벨에 맞춰 들여쓴 모습을 보여 주기 위한 열이다.

양쪽 코드의 핵심 연결 조건은 `e.mgr = er.empno`로 같다. 내 코드의 `Level` 대소문자와 들여쓰기 식의 괄호 차이는 실습 표현 차이이며, **시작 행과 다음 행의 연결**이 핵심이다. 원본 데이터가 바뀌면 조직도 행 수와 모양도 바뀐다.

<a id="section-3"></a>

## 3. 이후 내 댓글 계층 연습의 열 순서 점검

새로 받은 내 `Script.sql`에는 위 조직도 예제를 **댓글의 부모·자식 관계**로 바꾸려는 시도가 더 있다. 강사님 원본에 같은 댓글 테이블 예제는 없으므로, 위의 강사님 `emp_recu`와 연결 원리만 비교한다. 아래는 **내 코드의 추가 원본 발췌**이며 완성·실행 확인된 예제로 취급하지 않는다.

출처: `D:/workspace/workspace_sql/Script.sql` 1009–1038행 · **내 코드 원본 발췌**

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

`c.parent_comment_code = cr.comment_code`는 조직도 코드의 `e.mgr = er.empno`처럼 **부모 행과 자식 행을 잇는 조건**이다. 그러나 `UNION ALL` 양쪽의 열은 **이름이 아니라 위치**로 대응한다. 시작 부분의 2·3·4번째 열은 `member_code`, `member_id`, `comment_content`인데, 반복 부분의 같은 자리는 `member_id`, `comment_content`, `parent_comment_code`다. 개수는 같아도 뜻과 자료형이 어긋나므로 이 상태의 조회 결과를 올바른 댓글 계층이라고 설명할 수 없다. `:board_code`도 사용 중인 SQL 클라이언트가 값을 바인딩할 때만 통하는 표기다. 먼저 양쪽 SELECT의 각 열 위치를 맞추는 것이 다음 수정 과제다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 시작 부분에서 왜 `mgr IS NULL`을 쓰는가?
2. 다음 단계의 `e.mgr = er.empno`는 어떤 두 사원을 연결하는가?
3. 두 단계만 적은 첫 시도와 재귀 CTE는 어디까지 내려갈 수 있다는 점이 다른가?
4. 추가 댓글 연습에서 양쪽 SELECT의 두 번째 열은 각각 무엇인가?

<a id="section-5"></a>

## 추가로 알면 좋은 것

조직도에 순환 참조가 있거나 계층이 매우 깊을 때의 제한·중단 방법은 실제 원본에 구현되지 않았다. 기본 본문에서는 **두 원본이 작성한 시작·반복 구조**를 읽는다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/18_SQL_Recursive_CTE_연습문제.md) → [실제 문제 풀이 비교](실습_SQL_원본문제_비교.md)
