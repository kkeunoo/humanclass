# 06. Python SQLite — 연결·SQL·행 자료·확정과 닫기를 끝까지 연결하기

[FastAPI 목차](README.md) · [읽기 안내](00_FastAPI_상세백과_읽기법.md)

메모리 Todo는 서버를 다시 시작하면 사라진다. 이번 수업은 HTTP경로가 아닌 sqlite3 Python실습으로, 파일 DB에 값을 저장하고 다시 연결해 읽는다. SQL을 실행하는 일과 Python객체로 가져오는 일, 변경확정과 자원닫기를 나눠 본다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

연결과 커서의 차이, ?매개변수와 한 항목 튜플, fetchone·fetchall·Row·DTO변환을 설명한다. commit·rollback·close와 with의 역할을 구분한다. 원본의 실행 순서와 전체 UPDATE범위를 확인한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

SQLite는 별도 MariaDB서버에 접속하지 않고 파일을 이용할 수 있는 관계형 DB다. sqlite3는 Python표준 모듈이다. connect는 DB연결 객체를 만들고 cursor는 그 연결에서 SQL을 실행하고 결과를 읽는 별도 객체다. 커서 자체가 연결 객체라는 원본 주석은 정확하지 않다.

| 단계 | Python호출 | 결과·역할 |
| --- | --- | --- |
| 연결 | sqlite3.connect(파일명) | DB연결 |
| 실행 준비 | connection.cursor() | SQL·결과를 다루는 커서 |
| 실행 | cursor.execute(SQL,매개변수) | 문장 실행 |
| 읽기 | fetchone·fetchall | 다음 한 행·남은 전체 행 |
| 확정·취소 | commit·rollback | 트랜잭션 경계 |
| 종료 | close | 연결 자원 닫기 |

?는 값의 자리다. SQL문자열에 사용자 값을 직접 이어붙이지 않고 두 번째 인자에 따로 전달한다. (20,)은 값 하나짜리 튜플이고 (20)은 정수20이다. 매개변수 개수와 ?개수를 맞춘다. 이것은 업무 범위나 필수값 검사까지 자동 수행한다는 뜻은 아니다.

기본 조회 한 행은 튜플이고 fetchall은 튜플들의 리스트다. fetchone은 더 읽을 행이 없으면 None이다. row_factory=sqlite3.Row는 열 이름으로도 접근하는 Row를 제공한다. Row 자체가 dict는 아니며 dict(row)로 새 딕셔너리를 만든다. DTO는 그 키들을 정의한 모델 필드로 전달해 얻는 별도 객체다.

> 📚 **출처 · 본문 설명 확인:** [Python sqlite3](https://docs.python.org/ko/3/library/sqlite3.html), [매개변수 전달](https://docs.python.org/ko/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries), [연결 문맥 관리자](https://docs.python.org/ko/3/library/sqlite3.html#how-to-use-the-connection-context-manager). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-30.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. example.py와 dept_store.py를 같은 새 연습 폴더에 저장하고 `python example.py`로 실행한다. Python표준 sqlite3만 필요하며 FastAPI서버·외부DB는 사용하지 않는다. 원본 sqlite.db와 다른 book_dept.sqlite를 현재 폴더에 만든다. 아래 예상은 처음 실행한 새 파일 기준이다. 재실행하면 기존 변경값이 남으므로 처음 결과를 비교할 때는 별도 새 연습 폴더를 사용한다.



**[dept_store.py](실습/책형_복습/06_Python_SQLite와_Transaction/dept_store.py) — 새 예제 전체 파일**

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

**[example.py](실습/책형_복습/06_Python_SQLite와_Transaction/example.py) — 새 예제 전체 파일**

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

prepare가 표와 세 행을 준비한다. find_dept는 새 연결에서20번을 읽어 Row→dict로 바꿔 반환한다. rename_dept는20번만 바꾸고 with구간이 정상 종료되면 확정한다. 그 뒤 새 연결의 조회에도 복습 강의실이 보인다. 99번은 없어 None이다. 마지막 실험은10번을 임시 변경한 뒤 ValueError를 with밖으로 전달해 취소되게 한다. finally의 close는 확정·취소와 별개로 연결을 닫는다.

**요청과 예상 결과:**

```text
{'deptno': 20, 'dname': '2강의실', 'loc': '수원'}
수정 행 1
{'deptno': 20, 'dname': '복습 강의실', 'loc': '수원'}
없는 번호 None
미확정 변경 취소
{'deptno': 10, 'dname': '1강의실', 'loc': '천안'}
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/05_SQLite/sqlite.py` 11–27행 · **원본 발췌**

```python
def create_dept() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor() # cursor는 위에 connect한 실제 연결 객체를 가져오는 것

    # cursor에 있는 SQL문을 실행
    # 보통 DDL은 autocommit이 되지만, 별도로 commit 해줘야 함
    # if not exists를 넣어주면 만약 없다면 실행하기에 중복생성 오류 방지 (Oracle은 없음)
    cursor.execute('''
        create table if not exists dept (
            deptno integer primary key,
            dname text not null,
            loc text
        )
    ''')
    # commit해주고 나면 연결 끊어주는 것 필요
    connect.commit()
    connect.close()
```

**발췌 바로 풀이:** `sqlite3.connect('sqlite.db')`로 DB 파일을 열고 `cursor()`로 SQL을 실행한다. `CREATE TABLE IF NOT EXISTS dept`는 아직 표가 없을 때 만든다. `DEPTNO`는 기본 키, `DNAME`은 비울 수 없는 열이다. 두 함수 모두 `commit()` 후 `close()`한다. `connect`와 `cursor`는 서로 다른 객체이며, 내 주석의 “커서는 연결 객체를 가져온 것”은 정확하지 않다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/05_SQLite/sqlite.py` 29–56행 · **원본 발췌**

```python
def insert_dept() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    # execute '?'의 경우 이 자리에 다른 것을 받아 넣으라는 것
    # SQL injection을 방지하기 위해 '?'를 쓰고 tuple로 값을 별도로 넣는 것이며,
    # '?'은 int면 int..등등 문자와 숫자 자료형을 한 번 걸러 변환해 줌
    cursor.execute('''
        insert into dept (deptno, dname, loc)
        values (?, ?, ?)
    ''', (10, '1강의실', '천안'))

    cursor.execute('''
        insert into dept (deptno, dname, loc)
        values (?, ?, ?)
    ''', (20, '2강의실', '수원'))

    cursor.execute('''
        insert into dept (deptno, dname, loc)
        values (?, ?, ?)
    ''', (30, '3강의실', '서울'))

    # cursor rowcount로 영향을 미친 열의 수를 알 수 있음
    # 가장 최근의 cursor가 영향을 끼친 줄의 수 만 나옴(3으로 나오지 않음)
    print('수정 개수:', cursor.rowcount)

    connect.commit()
    connect.close()
```

**발췌 바로 풀이:** `VALUES (?, ?, ?)`의 물음표는 SQL 문자열에 값을 직접 붙이지 않고 **별도 매개변수**로 전달하는 자리다. 두 코드는 10·20·30 부서를 넣는다. 이 방식은 값을 SQL 문법과 구분해 처리하며, 학생 주석의 “자료형을 한 번 걸러 변환한다”가 핵심 설명은 아니다. `cursor.rowcount`는 마지막 `execute()`가 영향을 준 행 수이므로 세 번의 `INSERT`를 누적한 3이 아니다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/05_SQLite/sqlite.py` 58–95행 · **원본 발췌**

```python
# select는 실행 후 결과를 다시 가져와야 함
def select_dept() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
    ''')

    rows = cursor.fetchall()
    print('fetchall 결과')
    print(rows)

    connect.close()

def select_dept_20() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
        where deptno = ?
    ''',(20,)) # where에 20을 바로 넣어도 좋지만 py에서 진행 시 ','후 튜플로 값 넣기 연습

    # cursor.execute('''
    #     select deptno, dname, loc
    #     from dept
    # ''')

    # fetchall 대신 fetchone으로 하면 원하는 값 하나만 튜플로 받아볼 수 있음 (fetchall은 리스트 안에 튜플)
    # 결과 하나만 구할 때 사용하며 where 조건이 없을 경우 제일 첫 번째 데이터값이 나옴 (에러 없으니 조심)
    rows = cursor.fetchone()
    print('fetchall 결과')
    print(rows)

    connect.close()
```

**발췌 바로 풀이:** `fetchall()`은 조회 결과의 모든 행을, `fetchone()`은 다음 한 행을 가져온다. `WHERE deptno = ?`에 `(20,)`을 넣는 이유는 **값 하나짜리 튜플**을 만들기 위해서다. 내 `select_dept_20()`은 `fetchone()`을 쓰면서 출력 문구를 `fetchall 결과`로 적었지만 실제 반환 형태는 한 행이다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/05_SQLite/sqlite.py` 116–167행 · **원본 발췌**

```python
def select_all_dict() :
    connect = sqlite3.connect('sqlite.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
    ''')

    rows = cursor.fetchall()
    print('fetchall 결과')
    # for i in range(len(rows)) :
    #     print(dict(rows[i]))

    result = []
    for row in rows :
        result.append(dict(row))
    print(result)

    result2 = [ dict(row) for row in rows]
    print(result2)

    connect.close()

from pydantic import BaseModel
# DTO = Data Transfer Object 데이터 변경 바구니 Java식 표현
class DeptDTO(BaseModel) :
# class DeptSchema(BaseModel) : # Python 식 표현
# class DeptModel(BaseModel) : # Python 식 표현
    deptno : int
    dname : str
    loc : str

def select_all_class() :
    connect = sqlite3.connect('sqlite.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
    ''')

    rows = cursor.fetchall()

    # 아래처럼 **로 DeptDTO에 넣을 때 딕셔너리로 분열하여 넣으면 Key=Value가 들어감
    # DeptDTO Pydantic에 형태에 맞게 넣을 때 사용 (고정 된 형태를 가지기 위해 Pydantic 사용)
    result2 = [ DeptDTO(**dict(row)) for row in rows]
    print(result2)

    connect.close()
```

**발췌 바로 풀이:** `row_factory = sqlite3.Row`를 연결에 설정하면 결과 행을 열 이름으로도 다룰 수 있다. `dict(row)`로 딕셔너리를 만들고, `DeptDTO(**dict(row))`로 `BaseModel` 객체를 만든다. 두 원본 모두 이 순서를 실제 연습했다. 단일 조회 결과가 `None`인 상황에서 바로 `dict(rows)`를 호출하면 실패할 수 있으므로 데이터가 있다는 전제가 필요하다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/05_SQLite/sqlite.py` 169–205행 · **원본 발췌**

```python
def update_dept() :
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    # cursor.execute('''
    #     update dept
    #     set dname = ?
    #     where deptno = ?
    # ''', ('좋은 강의실', 10))

    cursor.execute('''
        update dept
        set dname = ?
    ''', ('좋은 강의실',))

    # where 값을 주지 않으면 dept에 있는 dname을 모두 바꾸기 때문에 줄의 수 3개가 나옴
    print('수정 개수:', cursor.rowcount)

    connect.commit()
    connect.close()

def update_with() :
    # connect = sqlite3.connect('sqlite.db')
    # 성공하면 commit, 실패하면 rollback을 진행 함(file처럼 with를 사용해서)
    # close()까지 자동으로 해주기 때문에 'with'를 사용하면 더욱 편리함
    with sqlite3.connect('sqlite.db') as connect:
        cursor = connect.cursor()

        cursor.execute('''
            update dept
            set dname = ?
        ''', ('좋은 강의실',))

        print('수정 개수:', cursor.rowcount)

        # connect.commit()
        # connect.close()
```

**발췌 바로 풀이:** 원본 UPDATE에는 WHERE가 없어 모든 부서 이름을 바꾼다. rowcount는 열 수가 아니라 영향 행 수다. update_with의 with는 미확정 트랜잭션을 확정·취소하지만 연결 close를 대신하지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/05_SQLite/sqlite.py` 207–216행 · **원본 발췌**

```python
# create_dept()
# insert_dept()
# select_dept()
select_dept_20()
select_dict()
select_all_dict()
select_all_class()
update_dept()
update_with()
select_all_class()
```

**발췌 바로 풀이:** 원본은 표 생성·초기 입력 호출이 주석이다. 이전에 준비한 DB파일이 있는 상태를 전제하므로 새 폴더에서 그대로 실행하면 표가 없다는 오류가 날 수 있다.

내 create_dept→insert_dept는 함수로 정의되어 있지만 파일 끝에서는 호출하지 않는다. 대신 조회·Row변환·DTO변환·수정을 호출한다. update_dept와 update_with 모두 WHERE없이 dname을 바꿔 초기 세 부서 모두 변경될 수 있다. select_dept_20의 출력 문구는 fetchall결과지만 실제 호출은 fetchone이다. 마지막 INSERT의 rowcount는1이며 앞선 세 번을 누적한3이 아니다.

<a id="connections"></a>

## 5. import·함수·화면·저장이 연결되는 흐름

example.py의 import → dept_store.py의 정의 → prepare호출 → DB파일 → find_dept의 SELECT·fetchone → Row→dict반환 → 바깥 print다. 원본 select_all_class는 DeptDTO(**dict(row))로 deptno·dname·loc키를 클래스 필드에 전달한다. 반환 객체를 모아 출력한다. 새 예제는 DB흐름에 집중해 DTO를 추가하지 않았고 원본의 실제 DTO정의와 호출은 아래 발췌로 읽는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 원본은 튜플·딕셔너리·모델의 같은 행 변환을 비교했고 매개변수 전달과 커밋을 분리했다. **교정:** 커서는 연결 객체와 다르며 rowcount는 열 수가 아니다. **중요한 오해:** sqlite3연결의 with는 성공 시 확정·예외 시 취소를 다루지만 파일 open의 with처럼 연결을 닫지 않는다. **한계:** 오류를 with안에서 잡아 없애면 문맥 관리자가 예외를 못 보고 정상 종료로 판단할 수 있다. 새 예제는 예외를 밖에서 잡고 finally에서 닫는다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



두 원본에 with가 close까지 한다는 잘못된 주석이 있으므로 강사님 코드를 자동 모범 답으로 두지 않는다. 매개변수·조회 핵심은 같아 반복 인용하지 않는다. 새 개선의 명시적 close와 한 부서 WHERE를 당시 원본 수정본으로 표시하지 않는다. MariaDB의 일반 DDL암묵 커밋 규칙을 Python SQLite에 그대로 옮겨 설명하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 작업 | 현재 연결 | 다음 연결에서 관찰 |
| --- | --- | --- |
|20번 변경·정상 with끝 | 복습 강의실 | 확정값 보임 |
|10번 임시 변경 | 임시 이름 | 아직 미확정 |
|예외로 with종료 | 변경 취소 | 원래1강의실 |
|close | 연결 자원 닫힘 | 파일 삭제와 다름 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
|조회 번호20→99 | None | 일치 행 없음 |
|수정 번호99 | rowcount0 | 대상 없음 |
|예외 raise제거 | 임시 이름 확정 | 정상 with종료 |
|UPDATE의 WHERE제거 | 세 행 대상 | 조건 제한 없음 |
|매개변수(20,)를(20)으로 | 매개변수 전달 오류 | 정수는 한 항목 시퀀스가 아님 |

no such table이면 DB경로·작업 폴더·초기 함수 호출을 본다. 데이터가 남아 있으면 파일 DB와 메모리 리스트의 차이를 생각한다. dict(None)오류는 행이 없는 경우 검사를 확인한다. 잠금 문제는 미확정 트랜잭션과 닫지 않은 연결부터 보고 성급히 DB파일을 삭제하지 않는다.

**확인 범위:** 독립 Python파일을 별도 임시 폴더에서 실행해 출력·DB파일·해시 검증을 확인한다. 실제 외부 서비스·운영 DB·브라우저 공개 서버에 요청한 결과와 구별한다. 원본 전체 앱을 무조건 실행하지 않으며 별도 확인한 원본 구간은 검증 보고서에 기록한다. 사용자의 가상환경은 검사에 읽기만 사용하고 파일을 설치·수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** sqlite3의 autocommit·isolation_level 버전 차이, 동시 쓰기·잠금·WAL·contextlib.closing은 추가 학습이다. 본문은 현재 실습의 기본 연결 설정에서 확정·취소·닫기를 나눈다. [Python sqlite3 트랜잭션 제어](https://docs.python.org/ko/3/library/sqlite3.html#transaction-control)를 참고한다.

request.headers 직접 읽기와 response_model은 미학습으로 확인된 선택 확장이다. 본문에서 이 기능을 선행 조건으로 요구하지 않는다. 응답·입력 타입 표시와 response_model 설정도 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 커서와 연결은 같은 객체인가?
2. 한 값 매개변수(20,)에서 쉼표는 왜 필요한가?
3. fetchone의 행 없음은 빈 dict인가?
4. with가 연결 close도 하는가?
5. 마지막 execute의 rowcount가 세 번 INSERT누적값인가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

별도 객체다. 한 항목 튜플을 만든다. None이다. 확정·취소와 닫기는 별개다. 마지막 문장의 영향 행 수다.

</details>

| 구별 | 핵심 |
| --- | --- |
|연결·커서 | 자원·SQL실행 |
|fetch·변환 | 행 자료·dict/DTO |
|commit·close | 확정·닫기 |
|SQL조건 | 어느 행을 바꾸나 |

[장별 연습문제](실습/연습문제/06_Python_SQLite와_Transaction_연습문제.md) · 다음은 [MariaDB·SQLModel](07_FastAPI_MariaDB_SQLModel_사원_CRUD.md)이다.
