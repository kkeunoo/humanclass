# 06. Python SQLite — 파일 DB에 넣고 읽고 확정하기

[FastAPI 목차](README.md) · [이전: 화면 Todo](05_FastAPI_Jinja_Todo_CRUD.md) · [다음: MariaDB 사원 CRUD](07_FastAPI_MariaDB_SQLModel_사원_CRUD.md)

이 파일은 FastAPI 라우터가 아니라 **Python의 `sqlite3` 실습**이다. 앞의 Todo는 서버 메모리 리스트였고, 여기서는 `sqlite.db` 파일에 부서 행을 저장한다. 강사님과 내 파일 모두 표 생성·입력·조회·수정 함수를 실제로 작성했다.

## 1. 연결·커서·표 만들기

### 강사님 코드

출처: `teacher/workspace_python/todos/05_SQLite/sqlite.py` 1–16행 · **원본 발췌**

```python
import sqlite3

def create_dept():
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    cursor.execute('''
        create table if not exists dept (
            deptno integer primary key,
            dname text not null,
            loc text
        )   
    ''')

    connect.commit()
    connect.close()
```

### 내 코드

출처: `me/workspace_python/02_todos/05_SQLite/sqlite.py` 11–27행 · **원본 발췌**

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

`sqlite3.connect('sqlite.db')`로 DB 파일을 열고 `cursor()`로 SQL을 실행한다. `CREATE TABLE IF NOT EXISTS dept`는 아직 표가 없을 때 만든다. `DEPTNO`는 기본 키, `DNAME`은 비울 수 없는 열이다. 두 함수 모두 `commit()` 후 `close()`한다. `connect`와 `cursor`는 서로 다른 객체이며, 내 주석의 “커서는 연결 객체를 가져온 것”은 정확하지 않다.

## 2. `?` 자리에 값을 따로 전달

### 강사님 코드

출처: `teacher/workspace_python/todos/05_SQLite/sqlite.py` 18–47행 · **원본 발췌**

```python
def insert_dept():
    connect = sqlite3.connect('sqlite.db')
    cursor = connect.cursor()

    # a = (10, '1강의실', '천안')
    # cursor.execute(f'''
    #     insert into dept (deptno, dname, loc)
    #     values ({a[0]}, {a[1]}, {a[2]})
    # ''')
    # SQL Injection 공격 방지
    cursor.execute(f'''
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

    # 가장 최근의 cursor가 영향을 끼친 줄의 수
    print('수정 개수:', cursor.rowcount)

    connect.commit()
    connect.close()
```

### 내 코드

출처: `me/workspace_python/02_todos/05_SQLite/sqlite.py` 29–56행 · **원본 발췌**

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

`VALUES (?, ?, ?)`의 물음표는 SQL 문자열에 값을 직접 붙이지 않고 **별도 매개변수**로 전달하는 자리다. 두 코드는 10·20·30 부서를 넣는다. 이 방식은 값을 SQL 문법과 구분해 처리하며, 학생 주석의 “자료형을 한 번 걸러 변환한다”가 핵심 설명은 아니다. `cursor.rowcount`는 마지막 `execute()`가 영향을 준 행 수이므로 세 번의 `INSERT`를 누적한 3이 아니다.

## 3. 여러 행과 한 행 읽기

### 강사님 코드

출처: `teacher/workspace_python/todos/05_SQLite/sqlite.py` 49–84행 · **원본 발췌**

```python
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
    ''', (20,))
    # cursor.execute('''
    #     select deptno, dname, loc
    #     from dept
    # ''')

    # fetchone : 결과 하나만 구할 때
    # 결과가 여러개라도 첫번째 하나만 가져온다 (에러 없음)
    rows = cursor.fetchone()
    print('fetchone 결과')
    print(rows)

    connect.close()
```

### 내 코드

출처: `me/workspace_python/02_todos/05_SQLite/sqlite.py` 58–95행 · **원본 발췌**

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

`fetchall()`은 조회 결과의 모든 행을, `fetchone()`은 다음 한 행을 가져온다. `WHERE deptno = ?`에 `(20,)`을 넣는 이유는 **값 하나짜리 튜플**을 만들기 위해서다. 내 `select_dept_20()`은 `fetchone()`을 쓰면서 출력 문구를 `fetchall 결과`로 적었지만 실제 반환 형태는 한 행이다.

### 강사님 코드 — 열 이름으로 접근

출처: `teacher/workspace_python/todos/05_SQLite/sqlite.py` 111–158행 · **원본 발췌**

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
    print(rows)

    result = []
    for row in rows:
        result.append(dict(row))
    print(result)

    result2 = [ dict(row) for row in rows ]
    print(result2)

    connect.close()

from pydantic import BaseModel
class DeptDTO(BaseModel):
# class DeptSchema(BaseModel):
# class DeptModel(BaseModel):
    deptno: int
    dname: str
    loc: str

def select_all_class() :
    connect = sqlite3.connect('sqlite.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()

    cursor.execute('''
        select deptno, dname, loc
        from dept
    ''')

    rows = cursor.fetchall()

    result2 = [ DeptDTO(**dict(row)) for row in rows ]
    print(result2)

    connect.close()
```

### 내 코드 — 딕셔너리·모델로 바꾸기

출처: `me/workspace_python/02_todos/05_SQLite/sqlite.py` 116–167행 · **원본 발췌**

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

`row_factory = sqlite3.Row`를 연결에 설정하면 결과 행을 열 이름으로도 다룰 수 있다. `dict(row)`로 딕셔너리를 만들고, `DeptDTO(**dict(row))`로 `BaseModel` 객체를 만든다. 두 원본 모두 이 순서를 실제 연습했다. 단일 조회 결과가 `None`인 상황에서 바로 `dict(rows)`를 호출하면 실패할 수 있으므로 데이터가 있다는 전제가 필요하다.

## 4. 수정과 `with`의 실제 범위

### 강사님 코드

출처: `teacher/workspace_python/todos/05_SQLite/sqlite.py` 161–199행 · **원본 발췌**

```python
def update_dept():
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

    # 가장 최근의 cursor가 영향을 끼친 줄의 수
    print('수정 개수:', cursor.rowcount)

    connect.commit()
    connect.close()


def update_with():
    # connect = sqlite3.connect('sqlite.db')

    # 성공하면 commit, 실패하면 rollback하고
    # close까지 자동으로 해준다
    with sqlite3.connect('sqlite.db') as connect:
        cursor = connect.cursor()

        cursor.execute('''
            update dept
            set dname = ?
        ''', ('좋은 강의실',))

        # 가장 최근의 cursor가 영향을 끼친 줄의 수
        print('수정 개수:', cursor.rowcount)

        # connect.commit()
        # connect.close()
```

### 내 코드

출처: `me/workspace_python/02_todos/05_SQLite/sqlite.py` 169–205행 · **원본 발췌**

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

`UPDATE dept SET dname = ?`에 `WHERE`가 없어서 **모든 부서 이름**이 바뀐다. 주석 처리된 `WHERE deptno = ?` 버전과 차이를 읽는다. `with sqlite3.connect(...) as connect:`는 정상 종료 시 미확정 변경을 **커밋**하고 예외가 나면 **롤백**하는 연결 컨텍스트 관리자다. 그러나 이것만으로 **연결의 `close()`까지 자동 실행되는 것은 아니다**. 강사님·내 주석 모두 자동 닫힘이라고 적었지만 그 설명은 틀리다.

## 5. 파일 끝의 실행 순서

### 강사님 코드

출처: `teacher/workspace_python/todos/05_SQLite/sqlite.py` 204–213행 · **원본 발췌**

```python
# create_dept()
# # insert_dept()
# select_dept()

# select_dept_20()
# select_dict()
# select_all_dict()
# select_all_class()
# update_dept()
update_with()
```

### 내 코드

출처: `me/workspace_python/02_todos/05_SQLite/sqlite.py` 207–216행 · **원본 발췌**

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

강사님 파일은 마지막에 `update_with()`만 호출하고, 내 파일은 `select_dept_20()`부터 여러 함수를 호출한다. 두 파일 모두 **`create_dept()`와 `insert_dept()` 호출을 주석 처리**했다. 따라서 완전히 새 폴더에서 실행하면 `sqlite.db` 파일은 만들어질 수 있어도 `dept` 표가 없어 **첫 SQL 실행에서 실패**한다. 이전에 표를 만든 실습 상태를 전제로 한 기록임을 명시한다.

## 직접 확인할 질문

1. `(20,)`의 쉼표는 왜 필요한가?
2. `UPDATE`에서 `WHERE`를 빼면 어떤 부서가 바뀌는가?
3. `with sqlite3.connect(...)`가 자동으로 처리하는 것과 처리하지 않는 것은?
4. 새 폴더에서 원본 파일만 실행하면 왜 `dept` 조회·수정이 실패하는가?

## 추가로 알면 좋은 것

연결을 확실히 닫는 자원 관리 패턴과 동시 쓰기·잠금은 다음에 알면 좋다. 본문은 원본의 **연결·매개변수·조회·수정·커밋/롤백**을 먼저 다룬다.
