# 13. 외부 조인과 자기 조인 — 보존할 대상과 각 표의 역할 — 연습문제

[본문](../../13_SQL_Outer_JOIN과_Self_JOIN.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

LEFT·RIGHT의 보존 방향과 매칭 없는 열의 NULL을 설명한다. 같은 표를 사원·관리자 역할로 나누고 부서당 반드시 한 행이 아니라는 점을 확인한다.

[준비문 포함 전체 SQL](../책형_복습/13_SQL_Outer_JOIN과_Self_JOIN.sql)을 제공한다. [본문 3절](../../13_SQL_Outer_JOIN과_Self_JOIN.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT d.deptno, d.dname, e.ename
FROM book_dept d LEFT JOIN book_emp e ON d.deptno=e.deptno
ORDER BY d.deptno,e.empno;
SELECT e.ename AS employee, manager.ename AS manager_name
FROM book_emp e LEFT JOIN book_emp manager ON e.mgr=manager.empno
ORDER BY e.empno;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

부서 조회는 **7행**이다. 마지막은 40·EMPTY·NULL이며 사원이 없는 부서도 남는다. 관리자 조회는 사원6행, CARA만 관리자 이름 NULL이고 나머지 다섯은 CARA다.

사원이 여럿인 부서20은 세 행, 부서30은 두 행이 된다. 부서40은 사원 없이도 한 행이다. 둘째에서 CARA.mgr은 NULL이라 일치하는 관리자 번호가 없지만 왼쪽 사원이므로 남는다. 같은 book_emp를 별칭 둘로 읽을 뿐 데이터 복제를 한 것은 아니다.

</details>

## 문제 2. 이유 설명

1. 모든 부서를 남길 왼쪽 표는?
2. 사원 없는 부서 이름도 NULL이 되는가?
3. 같은 표 별칭 둘은 표를 복사하는가?
4. 왼쪽4부서면 결과도 반드시4행인가?

<details>
<summary>풀이</summary>

부서 표다. 왼쪽 부서 이름은 있고 오른쪽 사원 열이 NULL이다. 두 역할로 조회한다. 매칭 수에 따라 여러 행이다.

| 왼쪽 부서 | 일치 사원 수 | 결과 행 수 |
| --- | --- | --- |
| 10 | 1 | 1 |
| 20 | 3 | 3 |
| 30 | 2 | 2 |
| 40 | 0 | 1(NULL 사원) |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| LEFT를 내부 JOIN으로 | 부서40 제외·6행 | 맞는 쌍만 |
| 관리자 LEFT를 내부 JOIN으로 | CARA 제외·5행 | mgr NULL |
| 부서 뒤 WHERE e.sal>2000 추가 | 부서40 제외 | 오른쪽 NULL은 조건 참 아님 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

없어야 할 부서가 사라지면 내부 조인인지, 오른쪽 열 조건이 WHERE에 있는지 본다. 사원과 관리자 이름이 뒤집히면 SELECT 별칭을 확인한다. NULL 표시와 빈 문자열·0은 구별한다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
