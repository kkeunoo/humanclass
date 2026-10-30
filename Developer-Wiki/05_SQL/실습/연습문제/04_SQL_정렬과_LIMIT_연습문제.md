# 04. ORDER BY와 LIMIT — 순서를 정하고 필요한 구간 보기 — 연습문제

[본문](../../04_SQL_정렬과_LIMIT.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

ASC·DESC·여러 기준의 적용을 설명한다. LIMIT 개수와 offset,개수의 차이를 추적하고 동점이 있을 때 안정된 정렬 기준을 고른다.

[준비문 포함 전체 SQL](../책형_복습/04_SQL_정렬과_LIMIT.sql)을 제공한다. [본문 3절](../../04_SQL_정렬과_LIMIT.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT ename, sal FROM book_emp ORDER BY sal DESC, empno ASC LIMIT 2;
SELECT ename, sal FROM book_emp ORDER BY sal DESC, empno ASC LIMIT 1, 2;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

| 조회 | 첫 행 | 둘째 행 |
| --- | --- | --- |
| 앞 2행 | CARA 3000 | ELLA 3000 |
| 1행 건너뛰고 2행 | ELLA 3000 | BEN 1600 |

전체 급여 순서는 CARA·ELLA·BEN·FINN·DAN·ADA다. CARA와 ELLA는 동점이어서 사원 번호로 나뉜다. 첫 쿼리는 앞 두 행, 둘째는 CARA 한 행을 건너뛴 다음 두 행을 보여 준다. LIMIT의 첫 숫자 1은 사원 번호 조건도, 가져올 개수도 아니다.

</details>

## 문제 2. 이유 설명

1. DESC를 생략하면 내림차순인가?
2. LIMIT 5,3은 몇 행을 요청하는가?
3. 급여가 같을 때 empno는 왜 도움이 되는가?
4. LIMIT만으로 최고 급여를 고르는가?

<details>
<summary>풀이</summary>

기본은 ASC다. 다섯 행을 건너뛰고 세 행이다. 고유 번호로 동점 순서를 나눌 수 있다. 급여 정렬 요청이 필요하다.

| 전체 위치 | 이름 | 급여 | LIMIT 1,2 포함 |
| --- | --- | --- | --- |
| 1 | CARA | 3000 | 건너뜀 |
| 2 | ELLA | 3000 | 포함 |
| 3 | BEN | 1600 | 포함 |
| 4 | FINN | 1500 | 제외 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| DESC를 ASC로 | ADA부터 | 방향 변경 |
| LIMIT 0,2 | CARA·ELLA | 건너뛰지 않음 |
| LIMIT 2,2 | BEN·FINN | 두 행 건너뜀 |
| empno 정렬 제거 | 동점 순서 확정 못함 | 동일 급여 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

반대 순서면 DESC 유무를 본다. 페이지가 한 행씩 밀리면 offset은 0부터 건너뛸 수라는 점을 확인한다. 동일 조건인데 동점 위치가 달라지면 마지막 고유 기준이 있는지 확인한다. 정렬을 위한 표의 영구 데이터 순서 변경으로 이해하지 않는다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
