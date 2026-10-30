# 15. DML — 어떤 행을 넣고 바꾸고 지우는가 — 연습문제

[본문](../../15_SQL_DML.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 퀴즈·내 풀이와 구별하며, 새 book_emp 가상 데이터와 원본 EMP 초기 자료를 혼동하지 않는다.

## 목표와 준비

열 목록과 VALUES의 대응, UPDATE의 기존 값 사용, DELETE 대상 조건을 설명한다. 제약 오류·0행 변경·전체 행 변경을 구분한다.

[준비문 포함 전체 SQL](../책형_복습/15_SQL_DML.sql)을 제공한다. [본문 3절](../../15_SQL_DML.md#example)의 같은 연결·새 임시 표·입력 행을 확인한다. D 드라이브 원본 전체를 실행해 준비하는 문제가 아니다.

## 문제 1. 행·열·값 예상

```sql
INSERT INTO book_emp(empno,ename,job,mgr,sal,comm,deptno)
VALUES(7,'GUS','CLERK',3,1200,NULL,20);
SELECT empno,ename,sal FROM book_emp WHERE empno=7;
UPDATE book_emp SET sal=sal+100 WHERE empno=7;
SELECT empno,ename,sal FROM book_emp WHERE empno=7;
DELETE FROM book_emp WHERE empno=7;
SELECT COUNT(*) FROM book_emp;
```

결과 행 수·열 의미·각 값을 적는다. 빈 결과 0행과 NULL 한 칸을 구별한다.

<details>
<summary>풀이</summary>

삽입 뒤 **7·GUS·1200**, 수정 뒤 **7·GUS·1300**, 삭제 뒤 전체 인원은 원래의 **6명**이다.

열 목록의 순서대로 GUS자료를 넣는다. 다음 UPDATE는7번만 선택해 기존1200에100을 더한다. DELETE도7번만 지우므로 원래 여섯 사람은 남는다. 마지막 COUNT를 확인하면 삭제 대상과 전체 표 삭제가 다르다는 점을 볼 수 있다.

</details>

## 문제 2. 이유 설명

1. UPDATE에서WHERE를 빼면?
2. 없는99번을 지우면 반드시오류인가?
3. SELECT sal+100과 UPDATE SET sal=sal+100은 같은가?
4. INSERT의열목록 순서는 무엇과 맞추나?

<details>
<summary>풀이</summary>

모든행이 대상이다. 일치행0개일 수 있다. 조회계산과 저장변경이다. VALUES각값과 대응한다.

| 단계 | GUS존재 | GUS급여 | 총 인원 |
| --- | --- | --- | --- |
| 시작 | 없음 | 없음 | 6 |
| INSERT | 있음 | 1200 | 7 |
| UPDATE | 있음 | 1300 | 7 |
| DELETE | 없음 | 없음 | 6 |

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| UPDATE번호를99로 | GUS1200유지 | 일치행 없음 |
| DELETE번호를99로 | 총7명유지 | 삭제대상 없음 |
| WHERE없는UPDATE를 별도 새 예제에서 비교 | 전체 대상 | 행 제한 없음 |

한 행씩 골라 예상하고 실행한다. 다음 실험 전에 원래 준비 자료로 돌아간다.

<details>
<summary>막힐 때 확인</summary>

변경이 없으면 조건 행이 존재하는지 본다. 여러 행이 바뀌면 WHERE조건 범위를 확인한다. 중복 키 오류는 새 번호·기존행을 구분하고 필수값 누락은 실제 구조를 본다. 결과값만 보고 영향 행 수와 DB설정을 혼동하지 않는다.

</details>

## 채점과 복습

값만 맞히지 말고 대상·상태·조건·NULL·정렬을 설명한다. 원본 코드와 새 개선안을 구별한다. 이 예제의 공통 조회 결과는 SQLite 메모리 DB 교차 확인이며 MariaDB 서버 실행 확인은 아니다. 공식 문법과 DB별 설정의 차이를 본문에서 확인한다. TIP 선택 확장은 필수 정답이 아니다.
