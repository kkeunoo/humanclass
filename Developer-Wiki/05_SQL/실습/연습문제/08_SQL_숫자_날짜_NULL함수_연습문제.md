# 08. 숫자·날짜·NULL 함수 — 입력 값과 결과 형태 이해하기 — 연습문제

[본문](../../08_SQL_숫자_날짜_NULL함수.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

ROUND·CEIL·FLOOR·TRUNCATE·MOD 차이를 설명한다. 날짜 표시와 해석, 현재 시각의 변동성, NULL 대체와 원본 변경의 차이를 구분한다.

[준비문 포함 전체 SQL](../책형_복습/08_SQL_숫자_날짜_NULL함수.sql)을 제공한다. [본문 3절](../../08_SQL_숫자_날짜_NULL함수.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT ROUND(3.14,1), CEIL(-3.14), FLOOR(-3.14), TRUNCATE(-3.14,0), MOD(10,3);
SELECT DATE_FORMAT('2026-08-07 13:05:09', '%Y-%m-%d %H:%i:%s') AS display_time;
SELECT STR_TO_DATE('07-08-2026', '%d-%m-%Y') AS parsed_date;
SELECT ename, sal + comm AS raw_total, sal + IFNULL(comm,0) AS filled_total
FROM book_emp WHERE empno IN (1,2,4) ORDER BY empno;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

첫 결과는 **3.1·-3·-4·-3·1**. 날짜 표시는 **2026-08-07 13:05:09**, 날짜 해석 값은 **2026-08-07**이다.

| 이름 | raw_total | filled_total |
| --- | --- | --- |
| ADA | NULL | 1000 |
| BEN | 1900 | 1900 |
| DAN | 1300 | 1300 |

음수의 CEIL과 FLOOR가 다른 쪽으로 움직인다. 날짜의 %m은 월, %i는 분이므로 Python strftime의 분 표기와 혼동하지 않는다. ADA 수당은 NULL이라 덧셈 결과가 NULL이지만 IFNULL이 계산 중 0을 제공하면 1000을 유지한다. BEN은 300, DAN은 이미 0이어서 원래 값이 그대로 사용된다. IFNULL이 테이블에 0을 저장한 것은 아니다.

</details>

## 문제 2. 이유 설명

1. FLOOR(-3.14)와 TRUNCATE(-3.14,0)는?
2. DATE_FORMAT과 STR_TO_DATE의 방향은?
3. IFNULL은 NULL을 영구 변경하는가?
4. %m과 %i는 무엇인가?

<details>
<summary>풀이</summary>

-4와 -3이다. 날짜→표시 문자열, 문자열→날짜 값이다. 조회 계산에서 대체값을 쓴다. 월과 분이다.

| 수당 | IFNULL 반환 | sal+comm | sal+대체값 |
| --- | --- | --- | --- |
| NULL | 0 | NULL | 급여 유지 |
| 300 | 300 | 급여+300 | 급여+300 |
| 0 | 0 | 급여 | 급여 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| TRUNCATE 자리0→1 | -3.1 | 소수1자리 유지 |
| IFNULL 기본값100 | ADA 1100 | 없는 수당만 대체 |
| %i를 %m으로 | 분 자리에 08 | 월 표시로 변경 |
| 고정 날짜를 NOW로 | 실행 시각에 따라 다름 | 동적인 입력 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

음수 결과가 다르면 FLOOR와 TRUNCATE를 구별한다. 날짜 변환이 실패하면 문자열 순서와 양식이 맞는지 본다. 수당 합계가 NULL이면 계산 전에 어떤 대체 정책을 쓸지 정한다. 원래 NULL의 업무 의미를 지우고 무조건 0으로 대체해야 한다는 규칙은 아니다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
