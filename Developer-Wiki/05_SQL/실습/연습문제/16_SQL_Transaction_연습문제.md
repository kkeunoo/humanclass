# 16. 트랜잭션 — 확정 전 변경과 확정 후 상태 나누기 — 연습문제

[본문](../../16_SQL_Transaction.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

START TRANSACTION·COMMIT·ROLLBACK의 경계를 추적한다. 자동 커밋·지원 엔진·DDL 경계를 확인하고 원본의 롤백 주석을 바로 읽는다.

[준비문 포함 전체 SQL](../책형_복습/16_SQL_Transaction.sql)을 제공한다. [본문 3절](../../16_SQL_Transaction.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
START TRANSACTION;
DELETE FROM book_ledger WHERE id=1;
SELECT COUNT(*) FROM book_ledger;
ROLLBACK;
SELECT COUNT(*) FROM book_ledger;
START TRANSACTION;
DELETE FROM book_ledger WHERE id=1;
COMMIT;
ROLLBACK;
SELECT COUNT(*) FROM book_ledger;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

순서대로 COUNT는 **0 → 1 → 0**이다. 첫 삭제는 취소되어 돌아오고 두 번째 삭제는 확정되어 뒤 ROLLBACK으로 돌아오지 않는다.

준비에서 1행을 확정했다. 첫 트랜잭션에서 삭제하면 현재 COUNT는 0이지만 ROLLBACK 뒤 1이다. 다음 트랜잭션은 삭제 후 COMMIT하므로 그 뒤 ROLLBACK해도 0이다. 매번 같은 연결에서 관찰하며 원본 표가 아닌 book_ledger만 변경한다.

</details>

## 문제 2. 이유 설명

1. COMMIT 뒤 ROLLBACK으로 이전 삭제를 취소하는가?
2. 첫 삭제 대상 행이 없으면 취소 흐름을 관찰하기 좋은가?
3. 임시 표 COMMIT은 영구 표로 바꾸는가?
4. 원본 문장만으로 자동 커밋을 알 수 있는가?

<details>
<summary>풀이</summary>

이미 확정된 삭제는 취소하지 못한다. 변경이 없어 구분하기 어렵다. 임시 표 수명과 확정은 다르다. 당시 연결 설정 확인이 필요하다.

| 단계 | 행 수 | 확정 상태 |
| --- | --- | --- |
| 준비 | 1 | 초기 값 확정 |
| 첫 DELETE | 0 | 미확정 |
| ROLLBACK | 1 | 삭제 취소 |
| 두 번째 DELETE·COMMIT | 0 | 삭제 확정 |
| 뒤 ROLLBACK | 0 | 이전 확정은 그대로 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 첫 ROLLBACK을 COMMIT으로 | 그 뒤 행 수 0 | 삭제 확정 |
| DELETE 조건 id99 | 계속 1 | 일치 행 없음 |
| DELETE 대신 amount=200 UPDATE | 취소 뒤 100 | 미확정 수정 취소 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

되돌아오지 않으면 정말 미확정 DML인지·같은 연결인지·지원 엔진인지 본다. 일반 DDL의 암묵 커밋을 놓치지 않는다. 임시 표가 사라진 것과 행 삭제가 취소되지 않은 것은 다른 문제다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
