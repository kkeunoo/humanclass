---
title: Python SQLite와 Transaction
version: v3.0-final
last_updated: 2026-08-25
status: Completed
---

# Python SQLite와 Transaction

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `06_Python_SQLite와_Transaction.md` |
| 분류 | `06_FastAPI` |
| 내 코드 | `workspace_python/02_todos/05_SQLite/sqlite.py`, `sqlite.db` |
| 강사님 코드 | `workspace_teacher/workspace_python/todos/05_SQLite/sqlite.py`, `sqlite.db` |
| 추가 메모 | Transaction, 업무 단위, Commit, Rollback |
| 핵심 범위 | SQLite 연결, Cursor, DDL·DML, Parameter Binding, Fetch, Row Factory, DTO, Transaction, Context Manager |
| 참고 전용 | 학습 중인 `03_database`의 DB Session·Commit·Rollback 방향 |
| 문서 형식 | FastAPI Developer-Wiki V2 |

> 이 문서는 완료된 `05_SQLite` 수업만 다룬다. `03_database`는 SQLite 다음에 MariaDB·SQLModel·Session으로 확장되는 흐름만 확인했으며 정식 내용에는 포함하지 않는다.

---

# 학습 목표

- SQLite의 특징과 Python `sqlite3` Module의 역할을 설명할 수 있다.
- Connection과 Cursor를 생성하고 종료할 수 있다.
- Table 생성과 CRUD SQL을 실행할 수 있다.
- Parameter Binding으로 값을 안전하게 전달할 수 있다.
- `fetchone()`과 `fetchall()`을 구분할 수 있다.
- `sqlite3.Row`를 Dict와 Pydantic DTO로 변환할 수 있다.
- `rowcount`의 의미를 설명할 수 있다.
- Transaction, Commit, Rollback과 업무 단위를 설명할 수 있다.
- Connection Context Manager의 실제 동작을 설명할 수 있다.

---

# 1. SQLite란?

SQLite는 별도 DB Server Process 없이 하나의 File에 Data를 저장하는 경량 관계형 Database다.

```text
Application
→ Python sqlite3 Module
→ sqlite.db File
```

학습, Test, Mobile·Desktop Application, 소규모 Local Data 저장에 유용하다. 여러 사용자가 동시에 대량으로 쓰는 Server 환경은 별도의 Client-Server DBMS가 더 적합할 수 있다.

Python 표준 Library에 `sqlite3`가 포함되므로 일반적으로 별도 pip 설치가 필요 없다.

## 1.1 sqlite.db는 어디에 만들어지는가?

```python
sqlite3.connect('sqlite.db')
```

상대 경로는 Python Process의 현재 작업 Directory를 기준으로 해석된다.

```text
현재 Directory가 05_SQLite
→ 05_SQLite/sqlite.db

다른 Directory에서 Python 실행
→ 예상과 다른 위치에 sqlite.db가 생성될 수 있음
```

안정적인 경로:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'sqlite.db'
connection = sqlite3.connect(DB_PATH)
```

같은 이름의 DB File이 여러 곳에 생기면 “Table이 없다”, “Data가 보이지 않는다”는 혼동이 발생할 수 있다.

---

# 2. Connection과 Cursor

```python
import sqlite3

connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()
```

| 객체 | 역할 |
| --- | --- |
| Connection | Database 연결과 Transaction 관리 |
| Cursor | SQL 실행과 결과 조회 |

```python
cursor.execute('SELECT 1')
connection.close()
```

변수명은 `connect`보다 객체의 의미가 명확한 `connection` 또는 `conn`을 권장한다.

## 2.1 실제 동작 순서

```text
sqlite3.connect()
→ DB File 열기 또는 새로 만들기
→ Connection 객체 반환

connection.cursor()
→ 해당 연결에 묶인 Cursor 생성

cursor.execute(sql, values)
→ SQL과 값을 SQLite Engine에 전달

fetchone()/fetchall()
→ 조회 결과를 Python 값으로 가져오기

commit()/rollback()
→ 변경 확정 또는 취소

close()
→ OS Resource와 DB 연결 해제
```

Cursor가 DB File 자체는 아니다. SQL을 실행하고 결과 위치를 관리하는 객체이며 실제 연결과 Transaction은 Connection이 관리한다.

---

# 3. Table 생성

```python
def create_dept():
    connection = sqlite3.connect('sqlite.db')
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dept (
                deptno INTEGER PRIMARY KEY,
                dname TEXT NOT NULL,
                loc TEXT
            )
        ''')
        connection.commit()
    finally:
        connection.close()
```

`IF NOT EXISTS`는 Table이 이미 있을 때 중복 생성 오류를 막는다.

DDL의 Transaction 동작은 DBMS와 Driver 설정에 따라 차이가 있으므로 “DDL은 언제나 Auto Commit”으로 일반화하지 않는다. Python `sqlite3`에서는 Transaction 경계를 명시적으로 관리하는 습관이 안전하다.

---

# 4. Insert와 Parameter Binding

```python
cursor.execute(
    '''
    INSERT INTO dept (deptno, dname, loc)
    VALUES (?, ?, ?)
    ''',
    (10, '1강의실', '천안'),
)
```

`?`는 값을 SQL 문자열에 직접 합치지 않고 Driver에 별도로 전달하는 Placeholder다.

```python
# 사용하지 않기
sql = f"INSERT INTO dept VALUES ({deptno}, '{dname}', '{loc}')"
```

Parameter Binding의 핵심은 다음과 같다.

- SQL Injection 위험 감소
- 따옴표와 Escape 처리 위임
- Python 값을 SQLite가 이해할 값으로 Adapt
- SQL 구조와 Data 분리

원본 Comment의 “자료형을 한 번 걸러 변환한다”는 표현은 일부 방향은 맞지만, Pydantic처럼 업무 규칙을 검증하는 기능은 아니다. ID 범위나 문자열 길이는 별도 검증이 필요하다.

## 4.1 값은 어떻게 SQL에 들어가는가?

Python Code:

```python
sql = 'INSERT INTO dept (deptno, dname, loc) VALUES (?, ?, ?)'
values = (10, '1강의실', '천안')
print('sql:', sql)
print('values:', values)
cursor.execute(sql, values)
```

Terminal:

```text
sql: INSERT INTO dept (deptno, dname, loc) VALUES (?, ?, ?)
values: (10, '1강의실', '천안')
```

Driver 내부 흐름:

```text
SQL 구조와 Tuple을 별도 인자로 받음
→ 첫 번째 ?에 10 Binding
→ 두 번째 ?에 '1강의실' Binding
→ 세 번째 ?에 '천안' Binding
→ SQLite가 INSERT 실행
→ 아직 Commit 전이면 Transaction의 미확정 변경
```

값을 문자열 치환해 완성된 SQL을 직접 만드는 방식이 아니다.

---

# 5. 한 개짜리 Tuple

```python
cursor.execute(
    'SELECT * FROM dept WHERE deptno = ?',
    (20,),
)
```

`(20,)`의 쉼표가 한 개짜리 Tuple을 만든다.

```python
(20)   # int
(20,)  # tuple
```

---

# 6. fetchone과 fetchall

```python
row = cursor.fetchone()
rows = cursor.fetchall()
```

| Method | 반환 |
| --- | --- |
| `fetchone()` | 다음 Row 하나 또는 `None` |
| `fetchall()` | 남아 있는 모든 Row의 List |

`fetchone()`은 결과가 여러 건이어도 첫 Row만 가져온다. “한 건만 있어야 한다”는 검증을 대신하지 않으므로 SQL 조건과 Constraint를 함께 확인한다.

## 6.1 실제 반환 형태

Table Data:

```text
10 | 1강의실 | 천안
20 | 2강의실 | 수원
```

```python
one = cursor.fetchone()
print(one, type(one))
```

```text
(10, '1강의실', '천안') <class 'tuple'>
```

다시 SQL을 실행한 후:

```python
all_rows = cursor.fetchall()
print(all_rows, type(all_rows))
```

```text
[(10, '1강의실', '천안'), (20, '2강의실', '수원')] <class 'list'>
```

`fetchone()`을 먼저 호출하고 같은 Cursor에서 `fetchall()`을 호출하면 첫 Row 다음의 남은 결과만 가져온다는 점에 주의한다.

---

# 7. sqlite3.Row와 Dict

기본 조회 Row는 Tuple 형태다.

```python
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
```

이후 조회 결과를 Dict로 바꿀 수 있다.

```python
rows = cursor.fetchall()
result = [dict(row) for row in rows]
```

`row_factory`는 Cursor 생성 전에 Connection에 설정하는 것이 명확하다.

## 7.1 변환 과정과 출력

```python
row = cursor.fetchone()
print(row)
print(row['deptno'])
print(dict(row))
```

예시 출력:

```text
<sqlite3.Row object at 0x...>
20
{'deptno': 20, 'dname': '2강의실', 'loc': '수원'}
```

`sqlite3.Row`는 Column 순서와 Column 이름 접근을 모두 지원한다. JSON이나 Pydantic에 넘기기 전 `dict(row)`로 명확히 변환할 수 있다.

---

# 8. Pydantic DTO로 변환

```python
from pydantic import BaseModel


class DeptDTO(BaseModel):
    deptno: int
    dname: str
    loc: str | None = None
```

```python
departments = [DeptDTO(**dict(row)) for row in rows]
```

`**dict(row)`는 Dict의 Key·Value를 Keyword Argument로 펼친다.

```text
{'deptno': 10, 'dname': '1강의실', 'loc': '천안'}
→ DeptDTO(deptno=10, dname='1강의실', loc='천안')
```

DTO는 Data Transfer Object다. “데이터 변경 바구니”보다는 **계층 사이에서 Data를 전달하는 구조화된 객체**라고 정리한다.

---

# 9. Update와 WHERE

```python
cursor.execute(
    '''
    UPDATE dept
    SET dname = ?
    WHERE deptno = ?
    ''',
    ('좋은 강의실', 10),
)
```

원본 실습의 활성화된 Update에는 `WHERE`가 없어 모든 Row가 변경된다.

```sql
UPDATE dept
SET dname = '좋은 강의실';
```

Update와 Delete 전에 다음을 확인한다.

```text
1. 같은 WHERE로 SELECT 실행
2. 대상 Row 확인
3. Transaction 시작
4. UPDATE/DELETE 실행
5. rowcount 확인
6. Commit 또는 Rollback
```

---

# 10. rowcount

```python
print(cursor.rowcount)
```

`rowcount`는 가장 최근 SQL 실행으로 영향을 받은 **Row 수**다. 원본의 “열의 수”라는 표현은 Column과 혼동되므로 “행의 수”로 교정한다.

세 번의 Insert를 각각 `execute()`했다면 마지막 실행의 Row 수만 확인하게 된다. 여러 Data는 `executemany()`로 처리할 수 있다.

```python
cursor.executemany(
    'INSERT INTO dept VALUES (?, ?, ?)',
    [
        (10, '1강의실', '천안'),
        (20, '2강의실', '수원'),
        (30, '3강의실', '서울'),
    ],
)
```

---

# 11. Transaction

Transaction은 Database의 상태를 바꾸는 하나의 논리적인 업무 단위다.

```text
Transaction 시작
→ SQL 1
→ SQL 2
→ SQL 3
→ 모두 성공: COMMIT
→ 하나라도 실패: ROLLBACK
```

예를 들어 계좌 이체는 출금과 입금이 하나의 업무 단위다.

```text
A 계좌 출금
B 계좌 입금
```

둘 중 하나만 반영되면 안 되므로 함께 Commit하거나 함께 Rollback해야 한다.

## 11.1 DB에서 실제 상태가 바뀌는 시점

```python
connection.execute(
    'UPDATE dept SET dname = ? WHERE deptno = ?',
    ('새 강의실', 10),
)
print('UPDATE 실행 완료, 아직 Commit 전')
connection.commit()
print('Commit 완료')
```

```text
execute 직후
→ 현재 Connection에서는 변경값을 볼 수 있음
→ 아직 Transaction이 확정되지 않은 상태

commit 이후
→ 변경 확정
→ 다음 Transaction 경계 시작 가능
```

오류가 발생하면:

```python
try:
    connection.execute(...)
    connection.execute(...)
    connection.commit()
except Exception as error:
    print('error:', error)
    connection.rollback()
    print('rollback 완료')
```

Terminal 예시:

```text
error: UNIQUE constraint failed: dept.deptno
rollback 완료
```

Rollback 후에는 같은 Transaction에서 수행한 미확정 변경이 취소된다.

---

# 12. Commit과 Rollback

## 12.1 Commit

```python
connection.commit()
```

현재 Transaction의 변경을 확정한다.

## 12.2 Rollback

```python
connection.rollback()
```

현재 Transaction에서 아직 Commit하지 않은 변경을 취소한다.

## 12.3 Transaction 경계

메모의 `commit~rollback`, `commit~commit`은 다음처럼 정리할 수 있다.

```text
이전 Commit 이후
→ 여러 변경 작업
→ 다음 Commit 또는 Rollback까지
= 하나의 Transaction 경계
```

Commit이 완료된 변경은 이후 Rollback으로 되돌릴 수 없다. 이미 Commit한 Data를 되돌리려면 반대 작업을 새 Transaction으로 수행하거나 Backup·복구 기능이 필요하다.

---

# 13. Context Manager의 정확한 동작

원본은 다음 구조를 사용한다.

```python
with sqlite3.connect('sqlite.db') as connection:
    cursor = connection.cursor()
    cursor.execute(...)
```

Connection Context Manager는 Block이 정상 종료되면 Commit하고 예외가 발생하면 Rollback한다. 하지만 **Connection을 자동으로 Close하는 기능으로 이해하면 안 된다.** 명시적인 종료가 필요하다.

```python
connection = sqlite3.connect('sqlite.db')
try:
    with connection:
        connection.execute(...)
finally:
    connection.close()
```

또는 Closing Context를 함께 사용할 수 있다.

```python
from contextlib import closing
import sqlite3


with closing(sqlite3.connect('sqlite.db')) as connection:
    with connection:
        connection.execute(...)
```

## 13.1 정상 종료와 예외 종료

정상 종료:

```text
with Block 진입
→ UPDATE 실행
→ 예외 없이 Block 종료
→ Connection Context Manager가 Commit
→ Connection은 여전히 별도 Close 필요
```

예외 종료:

```text
with Block 진입
→ 첫 SQL 실행
→ 다음 SQL에서 예외
→ Connection Context Manager가 Rollback
→ 예외는 바깥으로 전달
→ Connection은 별도 Close 필요
```

---

# 14. 안전한 Transaction 예제

```python
import sqlite3


def update_department(deptno: int, dname: str) -> int:
    connection = sqlite3.connect('sqlite.db')
    try:
        cursor = connection.execute(
            '''
            UPDATE dept
            SET dname = ?
            WHERE deptno = ?
            ''',
            (dname, deptno),
        )

        if cursor.rowcount != 1:
            raise ValueError('수정 대상은 정확히 한 건이어야 합니다.')

        connection.commit()
        return cursor.rowcount
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
```

`except`에서 오류를 출력하고 끝내기보다 Rollback 후 다시 발생시키면 호출자가 실패를 알 수 있다.

---

# 15. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 | 판단 |
| --- | --- | --- | --- |
| Table·CRUD | 동일 | 동일 | 학습 흐름 동일 |
| Comment | Parameter Binding·WHERE 위험 상세 | 핵심 설명 | 내 코드가 학습 기록 보강 |
| DTO 설명 | Java·Python 명칭 Comment | Model만 제시 | DTO 개념 교정 필요 |
| 실행 함수 | 여러 조회·수정 함수 호출 | `update_with()` 중심 | 내 코드는 실행 시 전체 Update 반복에 주의 |
| Context Manager | Close도 자동이라고 기록 | 동일 취지 | Commit/Rollback은 자동, Close는 별도 |

---

# 16. 실무 지침

- SQL 문자열에 사용자 값을 직접 합치지 않는다.
- Update·Delete 전에 같은 WHERE의 Select 결과를 확인한다.
- Connection은 `finally`에서 반드시 종료한다.
- Transaction의 업무 단위를 너무 크거나 작게 잡지 않는다.
- 예외를 숨기지 말고 Rollback 후 상위로 전달한다.
- `sqlite.db`가 Source가 필요한 초기 Data인지 Runtime Data인지 구분해 Git 관리 여부를 결정한다.
- DDL Migration과 Sample Data Script를 DB File과 별도로 관리하면 재현성이 좋아진다.

---

# 17. 자주 하는 실수와 Debugging

| 증상 | 원인 | 해결 |
| --- | --- | --- |
| `UNIQUE constraint failed` | 같은 PK 재삽입 | 기존 Data 확인 또는 Test DB 초기화 |
| 모든 Row가 수정됨 | WHERE 누락 | 먼저 SELECT로 대상 확인 |
| 변경이 저장되지 않음 | Commit 누락 | Transaction 성공 후 Commit |
| 일부 작업만 반영 | 업무 단위를 나눠 Commit | 관련 SQL을 한 Transaction으로 처리 |
| DB Lock | Connection 장기 유지 | Transaction을 짧게 유지하고 Close |
| `dict(row)` 오류 | Row Factory 미설정 | Cursor 전에 `row_factory` 설정 |
| Rollback이 안 됨 | 이미 Commit 완료 | Commit 이전에만 Rollback 가능 |

---

## 17.1 수업 원본에서 다시 찾기

| 배운 개념 | 내 코드 함수 | 강사님 코드 함수 | 다시 확인할 내용 |
| --- | --- | --- | --- |
| DB 연결·Table 생성 | `create_dept()` | `create_dept()` | Connect, Cursor, DDL, Commit, Close |
| Parameter Insert | `insert_dept()` | `insert_dept()` | `?`와 Tuple Binding |
| 전체 조회 | `select_dept()` | `select_dept()` | `fetchall()`의 List·Tuple 결과 |
| 한 건 조회 | `select_dept_20()` | 같은 함수 | `(20,)`, `fetchone()` |
| Row → Dict | `select_dict()` | 같은 함수 | `row_factory`, `dict(row)` |
| 전체 Dict 변환 | `select_all_dict()` | 같은 함수 | 반복문과 List Comprehension |
| Row → DTO | `select_all_class()` | 같은 함수 | `DeptDTO(**dict(row))` |
| WHERE Update | `update_dept()`의 주석 Code | 같은 위치 | 한 Row 수정 |
| 전체 Update 위험 | `update_dept()`의 실행 Code | 같은 위치 | WHERE 누락과 `rowcount` |
| Transaction Context | `update_with()` | `update_with()` | 정상 Commit·예외 Rollback, Close 별도 |
| Transaction 메모 | 2026-08-24 개인 메모 | 다음 DB 수업으로 확장 | 업무 단위와 경계 |

## 17.2 실행 전 주의

현재 `sqlite.py` 하단에는 여러 함수 호출이 활성화되어 있어 파일을 한 번 실행하면 조회뿐 아니라 전체 Update도 실행된다.

```python
select_dept_20()
select_dict()
select_all_dict()
select_all_class()
update_dept()
update_with()
select_all_class()
```

복습할 때는 한 번에 하나만 활성화한다.

```python
if __name__ == '__main__':
    select_all_class()
```

실행 전후 확인:

```text
1. 실행할 함수 한 개 확인
2. 함수 내부 SQL과 WHERE 확인
3. 실행 전 SELECT 결과 출력
4. SQL 실행
5. rowcount 출력
6. Commit 또는 Rollback 확인
7. 실행 후 SELECT 결과 비교
8. Connection Close 확인
```

---

# 18. 종합실습

1. `dept` Table을 생성한다.
2. Parameter Binding으로 세 부서를 한 번에 추가한다.
3. 전체 조회 결과를 Dict List로 변환한다.
4. Dict를 `DeptDTO` List로 변환한다.
5. 특정 부서 하나만 수정한다.
6. 수정 Row 수가 1이 아니면 Rollback한다.
7. 성공하면 Commit하고 실패하면 Rollback한다.
8. 성공·실패와 관계없이 Connection을 Close한다.
9. `WHERE` 없는 Update의 위험을 설명한다.

---

# 19. 정답 핵심

```python
import sqlite3
from pydantic import BaseModel


class DeptDTO(BaseModel):
    deptno: int
    dname: str
    loc: str | None = None


def get_departments() -> list[DeptDTO]:
    connection = sqlite3.connect('sqlite.db')
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            'SELECT deptno, dname, loc FROM dept ORDER BY deptno'
        ).fetchall()
        return [DeptDTO(**dict(row)) for row in rows]
    finally:
        connection.close()
```

---

# 최종 체크리스트

- [ ] SQLite와 Server형 DBMS의 기본 차이를 설명할 수 있다.
- [ ] Connection과 Cursor의 역할을 구분할 수 있다.
- [ ] Parameter Binding을 사용할 수 있다.
- [ ] `fetchone()`과 `fetchall()`을 구분할 수 있다.
- [ ] `sqlite3.Row`를 Dict와 DTO로 변환할 수 있다.
- [ ] `rowcount`가 Row 수임을 설명할 수 있다.
- [ ] Transaction을 논리적 업무 단위로 설명할 수 있다.
- [ ] Commit과 Rollback의 경계를 설명할 수 있다.
- [ ] 이미 Commit한 변경은 Rollback할 수 없음을 설명할 수 있다.
- [ ] Connection Context Manager가 Close까지 담당하지 않음을 설명할 수 있다.
- [ ] Update·Delete 전에 WHERE를 검증할 수 있다.

---

# 핵심 요약

```text
SQLite = File 기반 관계형 Database
Connection = 연결·Transaction 관리
Cursor = SQL 실행·결과 조회
? Placeholder = SQL과 값을 분리
row_factory = Row를 이름 기반으로 접근
DTO = 조회 Data의 구조화
Transaction = 하나의 논리적 업무 단위
Commit = 변경 확정
Rollback = 미확정 변경 취소
with connection = Commit/Rollback 관리, Close는 별도
```
