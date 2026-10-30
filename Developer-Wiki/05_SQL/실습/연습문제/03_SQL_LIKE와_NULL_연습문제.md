# 03. LIKE와 NULL — 글자 모양 검사와 알 수 없는 값 구분 — 연습문제

[본문](../../03_SQL_LIKE와_NULL.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

%와 _의 길이 조건을 설명한다. IS NULL과 = NULL의 차이를 확인하고 문자 비교의 대소문자 설정을 일반화하지 않는다.

[준비문 포함 전체 SQL](../책형_복습/03_SQL_LIKE와_NULL.sql)을 제공한다. [본문 3절](../../03_SQL_LIKE와_NULL.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
SELECT ename FROM book_emp WHERE ename LIKE '_A%' ORDER BY empno;
SELECT ename FROM book_emp WHERE comm IS NULL ORDER BY empno;
SELECT ename FROM book_emp WHERE comm = 0 ORDER BY empno;
SELECT ename FROM book_emp WHERE comm = NULL ORDER BY empno;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

첫 결과 CARA·DAN, 둘째 ADA·CARA·ELLA, 셋째 DAN·FINN, 마지막은 **0행**이다. 마지막 결과가 NULL 한 칸이라는 뜻은 아니다.

_가 첫 글자 하나를, A가 둘째 글자를, %가 나머지 0글자 이상을 담당한다. 수당 검사 세 문장은 같은 열에서 알려지지 않은 값·0·일반 비교의 차이를 보여 준다. 값 없음이 0으로 자동 치환된다고 생각하면 둘째와 셋째 결과를 잘못 예상하게 된다.

</details>

## 문제 2. 이유 설명

1. %는 빈 문자열도 허용하는가?
2. _A%의 A는 몇 번째인가?
3. NULL과 0이 같은가?
4. =NULL 조회의 0행은 한 행의 NULL과 같은가?

<details>
<summary>풀이</summary>

허용한다. 두 번째다. 다르다. 0행은 결과 행이 없다는 뜻이고 NULL 한 행과 다르다.

| 값 | IS NULL | =0 | WHERE에 남을 조건 |
| --- | --- | --- | --- |
| NULL | 참 | 알 수 없음 | IS NULL |
| 0 | 거짓 | 참 | =0 |
| 300 | 거짓 | 거짓 | 해당 두 조건 없음 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 패턴 A% | ADA | 첫 글자 A |
| 패턴 ____ | CARA·ELLA·FINN | 정확히 네 글자 |
| IS NOT NULL | BEN·DAN·FINN | 값 있는 수당 |
| comm IS NULL을 comm=0으로 | 다른 두 행 | 상태와 숫자는 다름 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

결과가 안 나오면 패턴 길이·연속 글자·NULL 여부를 본다. 수당 없음이 안 잡히면 =NULL을 썼는지 확인한다. NOT 조건도 NULL에 자동으로 참이 되지 않으므로 알 수 없음의 의미를 유지한다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
