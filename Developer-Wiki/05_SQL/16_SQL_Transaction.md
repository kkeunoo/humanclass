# 16. 트랜잭션 — 변경을 확정하거나 되돌리기

[SQL 목차](README.md) · [이전: DML](15_SQL_DML.md) · [다음: 인덱스](17_SQL_Index와_AUTO_INCREMENT.md)

`COMMIT`은 현재 트랜잭션의 변경을 확정하고 `ROLLBACK`은 **아직 확정되지 않은 변경**을 되돌린다. 두 원본에는 `DELETE` 전후에 이를 시험한 흔적이 있다. **자동 커밋 설정과 이전 DDL 실행 여부**를 모르면 실제 남는 행을 하나의 고정 결과로 적을 수 없다.

<!-- chapter-toc -->

- [1. `DELETE` 뒤의 `ROLLBACK`](16_SQL_Transaction.md#section-1)
- [2. DDL과 DML의 경계](16_SQL_Transaction.md#section-2)
- [3. 실제 확인 순서](16_SQL_Transaction.md#section-3)
- [직접 확인할 질문](16_SQL_Transaction.md#section-4)
- [추가로 알면 좋은 것](16_SQL_Transaction.md#section-5)

<a id="section-1"></a>

## 1. `DELETE` 뒤의 `ROLLBACK`

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 789–803행 · **원본 발췌**

```sql
delete from emp2
where empno = 1002;
select * from emp2;

rollback;
select * from emp2;
select * from dept2;

commit;
rollback;
delete from emp2
where empno = 1013;
select * from emp2;
rollback;
select * from emp2;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 851–873행 · **원본 발췌**

```sql
-- DELETE
-- delete from table로 원하는 대상만 제거할 수 있음 (from은 필수)
delete from emp2
where empno = 1002;
select * from emp2;

delete from emp2;
select * from emp2;

-- DDL은 자동 commit이기 때문에 그 시점 전으로는 되돌릴 수 없음
-- rollback은 마지막 DDL(CREATE, ALTER, DROP)을 실행하기 전으로 롤백해줌
rollback;
select * from emp2;
select * from dept2;

commit;
rollback;

delete from emp2
where empno = 1012;

rollback;
select * from emp2;
```

강사님은 `EMPNO=1002`를 지우고 롤백한 뒤, `COMMIT`·`ROLLBACK`, 다시 `EMPNO=1013` 삭제·롤백을 놓았다. 앞선 입력을 그대로 따라간 상태라면 1002가 없어 첫 삭제는 0행일 수 있다. 내 파일은 **조건 없는 전체 삭제**도 시험한다. 삭제 뒤 롤백으로 돌아오는지 보려면 **같은 연결에서, 자동 커밋이 꺼진 상태의 미확정 변경인지**를 먼저 확인해야 한다. 원본 문장만으로 언제나 복구된다고 약속하지 않는다.

<a id="section-2"></a>

## 2. DDL과 DML의 경계

### 강사님 코드

출처: `teacher/workspace_sql/Script.sql` 683–693행 · **원본 발췌**

```sql
drop table emp4;
drop table dept3;

select * from emp_copy;
truncate table emp_copy;

select * from dept2;
drop table dept2;

select * from emp2;
drop table emp2;
```

### 내 코드

출처: `me/workspace_sql/Script.sql` 746–749행 · **원본 발췌**

```sql
-- truncate 버림으로 테이블의 내용도 버릴 수 있음
-- 이후 배우는 delete는 롤백이 되지만, truncate는 롤백이 불가능
select * from emp_copy;
truncate table emp_copy;
```

`DROP TABLE`은 표 자체를 없애고, `TRUNCATE TABLE`은 표의 모든 행을 비운다. 일반적인 MariaDB DDL은 암묵적 커밋을 동반할 수 있으므로 위 DML의 `ROLLBACK`과 같은 방식으로 취급하지 않는다. 내 주석 “롤백은 마지막 DDL을 실행하기 전으로 롤백”은 **반대로 이해하게 만드는 설명**이다. 이미 커밋된 DDL 이전 상태로 `ROLLBACK`만으로 돌아간다고 생각하면 안 된다.

<a id="section-3"></a>

## 3. 실제 확인 순서

실습할 때는 수업 표를 직접 변경하기 전에 **별도의 연습 표**에서 시작 상태를 조회하고, 자동 커밋 설정을 확인한 뒤, 한 문장만 변경하고 영향 행 수와 `SELECT`를 보고 `COMMIT` 또는 `ROLLBACK`을 선택한다. 이는 원본의 결과를 고정해 주장하는 절차가 아니라, 배운 문장을 안전하게 다시 확인하기 위한 읽기 순서다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `ROLLBACK`이 되돌릴 수 있는 것은 어떤 상태의 변경인가?
2. 조건 없는 `DELETE FROM emp2`의 대상은 몇 행인가?
3. `TRUNCATE TABLE`을 일반 `DELETE`와 같은 롤백 예제로 취급하면 왜 위험한가?

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/16_SQL_Transaction_연습문제.md)

## 추가로 알면 좋은 것

격리 수준·잠금·동시성 충돌·세이브포인트는 이 스크립트의 트랜잭션 범위를 넘어간다. 이 장은 **확정 전후와 DDL 경계**를 먼저 익힌다.
