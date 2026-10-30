# 07. 문자열 함수 — 한 글자 위치·결과 길이·원본 변경 구별 — 연습문제

[본문](../../07_SQL_문자열함수.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

SUBSTR 위치와 길이, LENGTH의 단위, REPLACE·TRIM·LPAD·RPAD·CONCAT의 역할을 설명한다. 원래 길이 가리기와 고정 별표 문제를 구별한다.

[준비문 포함 전체 SQL](../책형_복습/07_SQL_문자열함수.sql)을 제공한다. [본문 3절](../../07_SQL_문자열함수.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT SUBSTR('SMITH', 2, 3) AS part, TRIM('  a b  ') AS cleaned;
SELECT REPLACE('ADA', 'A', '*') AS replaced;
SELECT RPAD(SUBSTR('SMITH', 1, 2), 5, '*') AS masked;
SELECT RPAD(SUBSTR('SMITH', 1, 2), 6, '*') AS fixed;
SELECT CONCAT_WS('-', 'ADA', 'CLERK', 1) AS label;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

| 식 | 예상 값 |
| --- | --- |
| SUBSTR·TRIM | MIT / a b |
| REPLACE | *D* |
| 원래 길이 5로 RPAD | SM*** |
| 고정 길이 6으로 RPAD | SM**** |
| CONCAT_WS | ADA-CLERK-1 |

SMITH에서 2번째 M부터 세 글자를 읽으면 MIT다. TRIM 뒤에도 a와 b 사이 한 칸은 남는다. ADA의 A 두 곳을 모두 *로 바꾼 결과는 *D*다. 앞 두 글자 SM을 남겨 총길이5로 채우면 별표3개, 총길이6이면 별표4개다. CONCAT_WS의 첫 인자 -는 값이 아니라 각 값 사이 구분자다.

</details>

## 문제 2. 이유 설명

1. SUBSTR의 세 번째 인자는 끝 위치인가?
2. RPAD 두 번째 인자는 추가 글자 수인가?
3. SELECT REPLACE가 원본을 수정하는가?
4. 일반 모드 LENGTH는 글자 수인가?

<details>
<summary>풀이</summary>

읽을 개수다. 최종 길이다. 조회 결과만 바뀐다. 바이트 길이이며 영문 예제에서는 같아 보일 수 있다.

| 단계 | 값 | 다음 인자 |
| --- | --- | --- |
| 원본 | SMITH | SUBSTR 대상 |
| SUBSTR(1,2) | SM | RPAD 대상 |
| LENGTH(SMITH) | 5 | 최종 길이 |
| RPAD | SM*** | 결과 표시 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| SUBSTR 시작을 1로 | SMI | 첫 글자부터 세 개 |
| 총길이 6을 4로 | SM** | 전체 네 글자 |
| TRIM 입력의 중간 공백 증가 | 중간 공백 유지 | 양끝만 제거 |
| REPLACE 대상 A를 D로 | A*A | 일치 글자 변경 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

한 글자 어긋나면 SQL 위치1과 Python 인덱스0을 구별한다. 별표가 너무 많으면 최종 길이와 추가 개수를 혼동했는지 본다. 한글 길이는 현재 문자셋·SQL 모드와 LENGTH 단위를 확인한다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
