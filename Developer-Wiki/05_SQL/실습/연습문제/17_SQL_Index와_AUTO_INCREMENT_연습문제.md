# 17. 인덱스와 자동 번호 — 찾는 경로와 새 행 식별자 구분 — 연습문제

[본문](../../17_SQL_Index와_AUTO_INCREMENT.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

CREATE INDEX·FORCE INDEX의 목적과 측정 한계를 설명한다. AUTO_INCREMENT와 MAX+1 계산을 구분한다. 실제 사용한 LENGTH·CHAR_LENGTH의 단위도 복습한다.

[준비문 포함 전체 SQL](../책형_복습/17_SQL_Index와_AUTO_INCREMENT.sql)을 제공한다. [본문 3절](../../17_SQL_Index와_AUTO_INCREMENT.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
CREATE INDEX book_idx_dept ON book_emp(deptno);
SELECT ename FROM book_emp WHERE deptno=20 ORDER BY empno;
DROP TEMPORARY TABLE IF EXISTS book_auto;
CREATE TEMPORARY TABLE book_auto (
 empno INT AUTO_INCREMENT PRIMARY KEY, ename VARCHAR(20)
);
INSERT INTO book_auto(ename) VALUES('ADA'),('BEN');
SELECT empno,ename FROM book_auto ORDER BY empno;
SELECT LENGTH('한구'),CHAR_LENGTH('한구');
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

부서20 조회는 **ADA·CARA·ELLA**다. 새 자동 번호 표는 일반적인 증가폭1·시작1 설정에서 **1·ADA / 2·BEN**을 예상한다. 문자열이 UTF-8이고 일반 MariaDB 모드라면 한구는 바이트길이6·문자수2다.

인덱스를 만든 뒤에도 같은 조건의 결과 이름은 같다. 결과가 같다는 사실로 속도 개선을 입증할 수 없다. 자동 번호 표에는 이름만 넣고 번호 열은 생략한다. DB가 번호를 만든다. 마지막은 같은 문자열의 바이트와 문자 단위를 나누는 실제 배운 함수 비교다.

</details>

## 문제 2. 이유 설명

1. 인덱스 만들면 반드시 빠른가?
2. AUTO_INCREMENT는 함수 호출인가?
3. MAX+1이 동시성 충돌을 막는가?
4. LENGTH와 CHAR_LENGTH단위는?

<details>
<summary>풀이</summary>

보장할 수 없다. 열 속성이다. 두 사용자가 같은 값을 계산할 수 있다. 일반 모드 바이트·문자 수다.

| 단계 | 인덱스 | 자동 번호 |
| --- | --- | --- |
| 정의 | 열 경로 생성 | 열의 생성 속성 지정 |
| 사용 | 서버가 조건에 맞는 경로 선택 | 번호 생략 INSERT |
| 결과 | 조건 행 목록 | 번호 포함 새 행 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 부서 조건20→10 | DAN | 필터 값 변경 |
| 자동 번호 이름 하나 추가 | 새 번호 생성 | INSERT추가 |
| LENGTH대상ab | 일반 UTF-8바이트2·문자2 | 영문두글자 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

인덱스 이름이 이미 있으면 같은 연결에서 준비를 반복했는지 확인한다. 번호가 예상1·2가 아니면 현재 표 상태·증가설정을 본다. 빠르다고 느낀 한 번의 실행으로 보편적 성능을 결론내리지 않는다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
