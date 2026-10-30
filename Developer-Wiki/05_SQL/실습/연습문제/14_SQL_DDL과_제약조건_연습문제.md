# 14. DDL과 제약조건 — 자료를 넣기 전에 표의 규칙 만들기 — 연습문제

[본문](../../14_SQL_DDL과_제약조건.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

CREATE·ALTER·DROP·TRUNCATE의 대상과 차이를 설명한다. PRIMARY KEY·NOT NULL·FOREIGN KEY·DECIMAL 의미를 구분하고 조회 복사가 모든 제약 복제는 아니라는 점을 확인한다.

[준비문 포함 전체 SQL](../책형_복습/14_SQL_DDL과_제약조건.sql)을 제공한다. [본문 3절](../../14_SQL_DDL과_제약조건.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
DROP TEMPORARY TABLE IF EXISTS book_rules;
CREATE TEMPORARY TABLE book_rules (
 empno INT NOT NULL PRIMARY KEY, ename VARCHAR(20) NOT NULL
);
INSERT INTO book_rules(empno,ename) VALUES(1,'ADA');
SELECT empno,ename FROM book_rules;
ALTER TABLE book_rules ADD note VARCHAR(20);
SELECT empno,ename,note FROM book_rules;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

열 추가 전은 **1·ADA 한 행**, 추가 후는 **1·ADA·NULL 한 행**이다. 별도 실험으로 같은 번호1 재입력, 이름NULL 입력은 제약에 걸린다. 실패 실험은 위 정상 전체 코드에 섞지 않았다.

CREATE가 규칙을 만들고 INSERT가 실제 ADA행을 넣는다. ALTER ADD로 note열을 늘리면 기존 행에도 새 열을 볼 수 있으며 값을 지정하지 않아NULL이다. 같은 empno를 다시 쓰면 기본 키 중복이고 ename=NULL은 필수값 제약 위반이다. 코드의 INT NOT NULL PRIMARY KEY는 두 테스트 엔진의 차이를 피하려 명시적으로 적었다.

</details>

## 문제 2. 이유 설명

1. NOT NULL이 빈 문자열도 금지하는가?
2. DECIMAL(7,2)의 전체 정밀도는?
3. AS SELECT가 모든 키를 복제하는가?
4. gender3으로 바꾼 뒤 gender를 지우면?

<details>
<summary>풀이</summary>

아니다. 전체7자리 중 소수2다. 모든 제약 복제를 보장하지 않는다. 그 이름이 없어 실패할 수 있다.

| 단계 | 표의 열 | 행 |
| --- | --- | --- |
| CREATE | empno·ename | 없음 |
| INSERT | 동일 | 1·ADA |
| ADD note | empno·ename·note | 1·ADA·NULL |
| 원본 rename 실험 | gender→gender2→gender3 | 현재 이름 갱신 필요 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 같은 번호1 삽입 | 중복 거부 | 기본 키 |
| ename에 NULL | 거부 | NOT NULL |
| ename에 빈 문자열 | NOT NULL만으로는 막지 않음 | NULL과 다름 |
| 새 note에 값 지정 | 해당 값 표시 | 새 열의 행 값 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

이미 표가 있으면 현재 대상과 준비 절차를 확인한다. 외래 키 생성 실패는 부모 존재뿐 아니라 키·열 규칙·지원 엔진을 본다. 열 없음 오류면 앞선 rename 이후 이름을 확인한다. 임시 표로 실험했다고 영구 DDL도 롤백될 것으로 추측하지 않는다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
