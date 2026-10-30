# 06. Python SQLite — 연결·SQL·행 자료·확정과 닫기를 끝까지 연결하기 — 연습문제

[본문](../../06_Python_SQLite와_Transaction.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

연결과 커서의 차이, ?매개변수와 한 항목 튜플, fetchone·fetchall·Row·DTO변환을 설명한다. commit·rollback·close와 with의 역할을 구분한다. 원본의 실행 순서와 전체 UPDATE범위를 확인한다.

[본문 3절](../../06_Python_SQLite와_Transaction.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 요청과 결과 예상

**dept_store.py**

```python
import sqlite3

DB_FILE = 'book_dept.sqlite'

def prepare():
    connection = sqlite3.connect(DB_FILE)
    try:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS dept (deptno INTEGER PRIMARY KEY, dname TEXT NOT NULL, loc TEXT)')
        cursor.execute('SELECT COUNT(*) FROM dept')
        if cursor.fetchone()[0] == 0:
            for row in [(10, '1강의실', '천안'), (20, '2강의실', '수원'), (30, '3강의실', '서울')]:
                cursor.execute('INSERT INTO dept(deptno,dname,loc) VALUES(?,?,?)', row)
        connection.commit()
    finally:
        connection.close()

def find_dept(deptno):
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT deptno,dname,loc FROM dept WHERE deptno=?', (deptno,))
        row = cursor.fetchone()
        return dict(row) if row is not None else None
    finally:
        connection.close()

def rename_dept(deptno, name):
    connection = sqlite3.connect(DB_FILE)
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute('UPDATE dept SET dname=? WHERE deptno=?', (name, deptno))
            changed = cursor.rowcount
        return changed
    finally:
        connection.close()
```

**example.py**

```python
import sqlite3
from dept_store import DB_FILE, prepare, find_dept, rename_dept

prepare()
print(find_dept(20))
print('수정 행', rename_dept(20, '복습 강의실'))
print(find_dept(20))
print('없는 번호', find_dept(99))

connection = sqlite3.connect(DB_FILE)
try:
    with connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE dept SET dname=? WHERE deptno=?', ('임시 이름', 10))
        raise ValueError('취소 실험')
except ValueError:
    print('미확정 변경 취소')
finally:
    connection.close()
print(find_dept(10))
```

실행 전에 결과를 먼저 적는다. 상태·응답·서버 출력·변경된 자료를 구별한다.

<details>
<summary>풀이</summary>

```text
{'deptno': 20, 'dname': '2강의실', 'loc': '수원'}
수정 행 1
{'deptno': 20, 'dname': '복습 강의실', 'loc': '수원'}
없는 번호 None
미확정 변경 취소
{'deptno': 10, 'dname': '1강의실', 'loc': '천안'}
```

prepare가 표와 세 행을 준비한다. find_dept는 새 연결에서20번을 읽어 Row→dict로 바꿔 반환한다. rename_dept는20번만 바꾸고 with구간이 정상 종료되면 확정한다. 그 뒤 새 연결의 조회에도 복습 강의실이 보인다. 99번은 없어 None이다. 마지막 실험은10번을 임시 변경한 뒤 ValueError를 with밖으로 전달해 취소되게 한다. finally의 close는 확정·취소와 별개로 연결을 닫는다.

| 작업 | 현재 연결 | 다음 연결에서 관찰 |
| --- | --- | --- |
|20번 변경·정상 with끝 | 복습 강의실 | 확정값 보임 |
|10번 임시 변경 | 임시 이름 | 아직 미확정 |
|예외로 with종료 | 변경 취소 | 원래1강의실 |
|close | 연결 자원 닫힘 | 파일 삭제와 다름 |

</details>

## 문제 2. 이유 설명

1. 커서와 연결은 같은 객체인가?
2. 한 값 매개변수(20,)에서 쉼표는 왜 필요한가?
3. fetchone의 행 없음은 빈 dict인가?
4. with가 연결 close도 하는가?
5. 마지막 execute의 rowcount가 세 번 INSERT누적값인가?

<details>
<summary>풀이</summary>

별도 객체다. 한 항목 튜플을 만든다. None이다. 확정·취소와 닫기는 별개다. 마지막 문장의 영향 행 수다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
|조회 번호20→99 | None | 일치 행 없음 |
|수정 번호99 | rowcount0 | 대상 없음 |
|예외 raise제거 | 임시 이름 확정 | 정상 with종료 |
|UPDATE의 WHERE제거 | 세 행 대상 | 조건 제한 없음 |
|매개변수(20,)를(20)으로 | 매개변수 전달 오류 | 정수는 한 항목 시퀀스가 아님 |

<details>
<summary>막힐 때 확인</summary>

no such table이면 DB경로·작업 폴더·초기 함수 호출을 본다. 데이터가 남아 있으면 파일 DB와 메모리 리스트의 차이를 생각한다. dict(None)오류는 행이 없는 경우 검사를 확인한다. 잠금 문제는 미확정 트랜잭션과 닫지 않은 연결부터 보고 성급히 DB파일을 삭제하지 않는다.

</details>

## 채점과 복습

정상 값만 보지 말고 누락·잘못된 타입·없는 대상의 흐름도 설명한다. 새 예제는 별도 앱에서 확인하며 원본 DB나 외부 서비스의 성공을 대신 주장하지 않는다. TIP 확장은 필수 조건이 아니다. 정의→등록→입력→호출→반환→다음 요청을 연결할 수 있는지 검토한다.
