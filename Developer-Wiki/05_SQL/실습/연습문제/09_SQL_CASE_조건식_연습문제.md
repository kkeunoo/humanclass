# 09. CASE — 조건에 맞는 값을 결과 열에 넣기 — 연습문제

[본문](../../09_SQL_CASE_조건식.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

단순 CASE와 조건식 CASE를 구분한다. WHEN 순서·ELSE·END의 의미와 원본 급여가 바뀌지 않는 이유를 설명한다.

[준비문 포함 전체 SQL](../책형_복습/09_SQL_CASE_조건식.sql)을 제공한다. [본문 3절](../../09_SQL_CASE_조건식.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

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

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

사원번호순 adjusted는 **1050·1648·3000·1365·3000·1545**다. band는 **기본·중간·높음·기본·높음·중간**이다. 원본 sal은 1000·1600·3000·1300·3000·1500 그대로다.

ADA는 CLERK라 5%, BEN은 SALESMAN이라 3% 증가한 값을 결과로 계산한다. CARA는 두 직업이 아니어서 원래 급여다. 둘째 CASE는 3000 이상을 먼저 검사하므로 3000인 사람이 중간에 들어가지 않는다. CASE는 표시용 분류일 뿐 급여 저장 변경이 아니다.

</details>

## 문제 2. 이유 설명

1. CASE가 행을 제거하는가?
2. 두 WHEN에 모두 맞으면?
3. ELSE 없고 일치도 없으면?
4. END 뒤 별칭은 원본 열 이름 변경인가?

<details>
<summary>풀이</summary>

제거하지 않는다. 먼저 맞는 갈래다. NULL이다. 결과 표시 이름이다.

| 급여 | >=3000 | >=1500 | 선택 |
| --- | --- | --- | --- |
| 1000 | 거짓 | 거짓 | 기본 |
| 1600 | 거짓 | 참 | 중간 |
| 3000 | 참 | 뒤 갈래 불필요 | 높음 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 두 급여 WHEN 순서 바꾸기 | 3000도 중간 | 먼저 맞는 갈래 |
| ELSE sal 제거 | 두 직업 외 NULL | 일치 없음 |
| CASE 결과 별칭만 변경 | 값 동일 | 표시 이름 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

범위 분류가 이상하면 겹치는 조건의 순서를 본다. 빈 값이 생기면 ELSE가 빠졌는지 확인한다. CASE 결과를 보고 원본 변경 여부를 추측하지 말고 UPDATE와 구분한다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
