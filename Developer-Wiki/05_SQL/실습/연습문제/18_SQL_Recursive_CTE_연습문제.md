# 18. 재귀 CTE — 시작 행에서 다음 관계를 반복해 따라가기 — 연습문제

[본문](../../18_SQL_Recursive_CTE.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

시작 부분·반복 부분·종료를 설명한다. UNION ALL 양쪽 열 위치, 깊이·경로 정렬·들여쓰기의 역할을 구분하고 현재 원본의 부서 연결 추가를 반영한다.

[준비문 포함 전체 SQL](../책형_복습/18_SQL_Recursive_CTE.sql)을 제공한다. [본문 3절](../../18_SQL_Recursive_CTE.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
WITH RECURSIVE org(empno,ename,mgr,depth) AS (
 SELECT empno,ename,mgr,1 FROM book_emp WHERE mgr IS NULL
 UNION ALL
 SELECT e.empno,e.ename,e.mgr,org.depth+1
 FROM book_emp e JOIN org ON e.mgr=org.empno
)
SELECT empno,ename,mgr,depth FROM org ORDER BY depth,empno;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

| 사원번호 | 이름 | 관리자번호 | 깊이 |
| --- | --- | --- | --- |
| 3 | CARA | NULL | 1 |
| 1 | ADA | 3 | 2 |
| 2 | BEN | 3 | 2 |
| 5 | ELLA | 3 | 2 |
| 6 | FINN | 3 | 2 |
| 4 | DAN | 1 | 3 |

이 장만 DAN의 관리자를 ADA 1번으로 바꾼 새 자료다. CARA에서 시작해 부하 ADA·BEN·ELLA·FINN을 얻고, 그중 ADA의 부하 DAN을 다음에 찾는다. 세 번째 단계 뒤에는 더 연결할 자식이 없어 끝난다. 깊이 정렬은 조직 경로순 정렬과 다른 선택이며 원본의 sort_key와 구분한다.

</details>

## 문제 2. 이유 설명

1. 시작 SELECT는 무엇을 고르는가?
2. 다음 단계의 연결 열은?
3. UNION ALL의 대응은 이름인가 위치인가?
4. 현재 내 원본에 새로 붙은 부서 정보를 예전 주석 차이만으로 설명해도 되는가?

<details>
<summary>풀이</summary>

루트 행이다. 자식 mgr과 이전 empno다. 위치다. 현재 열·조인을 다시 읽어야 한다.

| 반복 | 새로 찾은 행 | 깊이 |
| --- | --- | --- |
| 시작 | CARA | 1 |
| 첫 연결 | ADA·BEN·ELLA·FINN | 2 |
| 다음 연결 | DAN | 3 |
| 다음 연결 | 없음 | 종료 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| DAN 관리자를 3으로 | DAN 깊이 2 | 직접 부하 |
| 시작 조건을 empno=1로 | ADA·DAN만 | 다른 시작점 |
| depth 증가를 제거 | 깊이 표시 부정확 | 관계 탐색과 표시 값은 별개 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

계층이 빠지면 시작 행·부모 키·부서 내부 조인을 본다. 열 자료가 이상하면 UNION ALL의 각 위치를 비교한다. 경로가 잘리면 시작 열의 자료형·폭을 확인한다. 순환 가능 자료를 무제한 반복 시험으로 넣지 않고 별도 정책부터 정한다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
