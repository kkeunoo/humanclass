# 07. 사원 DB CRUD — 입력 모델·세션·매개변수·화면·커밋 연결하기

[FastAPI 목차](README.md) · [읽기 안내](00_FastAPI_상세백과_읽기법.md)

이 장은 PyMySQL 직접 조회에서 SQLModel 세션을 이용한 사원 화면으로 이어진다. 목록이 보인다는 사실만으로 저장까지 이해한 것은 아니다. 요청마다 누가 연결을 열고, 어느 값이 SQL에 전달되며, 언제 변경을 확정하는지까지 읽는다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

드라이버·엔진·세션·결과·모델의 역할을 구분한다. Depends(get_session)의 실제 정의와 yield 전후를 설명한다. PyMySQL %s와 text의 이름 매개변수, 테이블 모델과 입력 모델, 빈 입력 검증, 조회 없음·저장 실패·커밋 위치를 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

PyMySQL은 Python에서 MySQL/MariaDB 계열 서버에 연결하는 드라이버다. SQLModel은 모델 선언과 SQLAlchemy의 DB기능을 함께 사용할 수 있게 한다. 이 수업은 SQLModel을 썼어도 대부분 text로 SQL을 직접 작성한다. 모든 ORM기능을 사용한 수업으로 확대하지 않는다.

| 구성 | 역할 | 혼동하지 않을 것 |
| --- | --- | --- |
| DB서버 | 실제 구조와 행 보관 | FastAPI앱과 별개 |
| 드라이버 | DB와 통신 | PyMySQL |
| engine | 연결 설정·연결 제공의 중심 | 사원 한 행이 아님 |
| Session | DB작업·트랜잭션의 작업 단위 | sqlite3.Cursor와 같은 객체가 아님 |
| text(SQL) | 텍스트 SQL객체 구성 | 서버에서 미리 실행해 항상 빨라지는 기능 아님 |
| result.mappings() | 열 이름 기반 결과 읽기 | 입력 모델 생성과 다름 |
| 입력 모델 | 폼 필드·타입·변환 | table=True 모델과 목적 구분 |

Depends(get_session)은 요청 함수가 사용할 세션을 FastAPI가 준비하게 하는 선언이다. Depends(get_session())처럼 지금 호출한 값을 넣는 모양과 다르다. get_session의 with Session(engine)이 세션을 열고 yield에서 요청 함수에 제공한다. 요청 처리가 끝나면 yield뒤와 정리 과정으로 이어진다. 제너레이터의 상세 내부 구현까지 배우지 않았더라도 이 실제 자원 흐름은 본문에서 읽을 수 있다.

%s·?·:deptno는 라이브러리가 기대하는 자리 표기가 다르다. 공통 목적은 값과 SQL문법을 분리해 전달하는 것이다. text를 썼다는 이유만으로 문자열 이어붙이기가 안전해지는 것은 아니다. 이름 매개변수와 따로 전달한 dict가 핵심이다.

> 📚 **출처 · 본문 설명 확인:** [PyMySQL 조회 예](https://pymysql.readthedocs.io/en/latest/user/examples.html), [SQLModel 세션 의존성](https://sqlmodel.tiangolo.com/tutorial/fastapi/session-with-dependency/), [SQLAlchemy text](https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.text). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-30.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. 새 예제는 실제 DB암호 없이 재현하도록 MariaDB대신 앞 장에서 배운 SQLite파일에 같은 세션·text·폼·커밋 흐름을 구성했다. MariaDB연결 성공을 확인한 예제가 아니다. api.py·db.py·models.py·templates/employees.html을 같은 구조로 둔다. fastapi·uvicorn·jinja2·python-multipart·sqlmodel이 필요하다. api.py폴더에서 `uvicorn api:app --port 8000 --reload`로 실행하고 /emp/select를 연다. book_emp.sqlite라는 새 파일을 만든다. connect_args는 이 SQLite웹 예제의 실행 준비 설정이며 상세 동시성 학습은 TIP이다.



**[models.py](실습/책형_복습/07_FastAPI_MariaDB_SQLModel_사원_CRUD/models.py) — 새 예제 전체 파일**

```python
from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import field_validator

class BookEmp(SQLModel, table=True):
    empno: int = Field(primary_key=True)
    ename: str
    deptno: int
    sal: float
    comm: Optional[float] = None

class EmpInput(SQLModel):
    empno: int
    ename: str
    deptno: int
    sal: float
    comm: Optional[float] = None

    @field_validator('comm', mode='before')
    @classmethod
    def empty_to_none(cls, value):
        return None if value == '' else value
```

**[db.py](실습/책형_복습/07_FastAPI_MariaDB_SQLModel_사원_CRUD/db.py) — 새 예제 전체 파일**

```python
from sqlmodel import SQLModel, Session, create_engine
from models import BookEmp

engine = create_engine('sqlite:///book_emp.sqlite', connect_args={'check_same_thread': False})

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
```

**[api.py](실습/책형_복습/07_FastAPI_MariaDB_SQLModel_사원_CRUD/api.py) — 새 예제 전체 파일**

```python
from typing import Annotated
from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from sqlalchemy import text
from models import EmpInput
from db import init_db, get_session

app = FastAPI()
templates = Jinja2Templates(directory='templates')
init_db()

@app.get('/emp/select')
def select_employees(request: Request, session: Session = Depends(get_session)):
    result = session.execute(text('SELECT empno,ename,deptno,sal,comm FROM bookemp ORDER BY empno'))
    return templates.TemplateResponse(request, 'employees.html', {'employees': result.mappings().fetchall()})

@app.get('/emp/deptno')
def by_department(deptno: int, session: Session = Depends(get_session)):
    result = session.execute(text('SELECT empno,ename FROM bookemp WHERE deptno=:deptno ORDER BY empno'), {'deptno': deptno})
    return [dict(row) for row in result.mappings().fetchall()]

@app.post('/emp/insert')
def insert_employee(emp: Annotated[EmpInput, Form()], session: Session = Depends(get_session)):
    try:
        session.execute(text('INSERT INTO bookemp(empno,ename,deptno,sal,comm) VALUES(:empno,:ename,:deptno,:sal,:comm)'), {
            'empno': emp.empno, 'ename': emp.ename, 'deptno': emp.deptno,
            'sal': emp.sal, 'comm': emp.comm
        })
        session.commit()
    except Exception:
        session.rollback()
        return RedirectResponse('/emp/select?count=0', status_code=303)
    return RedirectResponse('/emp/select', status_code=303)

@app.get('/emp/detail')
def detail(empno: int, session: Session = Depends(get_session)):
    result = session.execute(text('SELECT empno,ename,deptno,sal,comm FROM bookemp WHERE empno=:empno'), {'empno': empno})
    row = result.mappings().fetchone()
    return dict(row) if row is not None else {'message': '없는 사원'}

@app.post('/emp/update')
def update_employee(empno: int = Form(), ename: str = Form(), session: Session = Depends(get_session)):
    result = session.execute(text('UPDATE bookemp SET ename=:ename WHERE empno=:empno'), {'empno': empno, 'ename': ename})
    session.commit()
    return {'changed': result.rowcount}

@app.post('/emp/delete')
def delete_employee(empno: int = Form(), session: Session = Depends(get_session)):
    result = session.execute(text('DELETE FROM bookemp WHERE empno=:empno'), {'empno': empno})
    session.commit()
    return {'changed': result.rowcount}
```

**[templates/employees.html](실습/책형_복습/07_FastAPI_MariaDB_SQLModel_사원_CRUD/templates/employees.html) — 새 예제 전체 파일**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>사원 복습</title></head><body>
<h1>사원 목록</h1>
{% if employees %}<ul>{% for emp in employees %}
<li>{{ emp.empno }} {{ emp.ename }} / 부서{{ emp.deptno }} / 급여{{ emp.sal }} / 수당{{ emp.comm }}</li>
{% endfor %}</ul>{% else %}<p>자료 없음</p>{% endif %}
<form method="post" action="/emp/insert">
<input name="empno" placeholder="사원번호" required>
<input name="ename" placeholder="이름" required>
<input name="deptno" placeholder="부서번호" required>
<input name="sal" placeholder="급여" required>
<input name="comm" placeholder="수당: 비워도 됨">
<button type="submit">추가</button></form>
<form method="post" action="/emp/update"><input name="empno" placeholder="번호" required><input name="ename" placeholder="새 이름" required><button>수정</button></form>
<form method="post" action="/emp/delete"><input name="empno" placeholder="번호" required><button>삭제</button></form>
</body></html>
```

모델 모듈을 읽으면 table=True인 BookEmp가 구조 메타데이터에 등록된다. init_db는 그 구조를 새 파일에 만든다. 요청은 Depends를 통해 세션을 받고 입력 모델의 comm빈칸은 None으로 바뀐다. INSERT는 별도 dict값을 바인딩하고 commit한다. 다음 상세 요청은 새 세션에서 저장된 행을 읽는다. 같은 기본 키 INSERT는 실패해rollback하고 원래 행을 유지한다. 수정·삭제는 WHERE번호와rowcount를 확인한다. SQL에는원본의전체사원8열대신학습에필요한5열만사용한새예제다.

**요청과 예상 결과:**

| 요청·상황 | 결과 |
| --- | --- |
| 첫 목록 | 자료 없음 |
| 정상 생성 |303, 다음 조회에 사원1 저장 |
| comm빈칸 | DB NULL·JSON null |
| 같은 번호 생성 |303 count=0, 원래 행 유지 |
|20번 부서 조회 | 공부사원 한 행 |
| 없는99번 수정 | changed0 |
|1번 수정·다시 조회 | 복습사원 |
| 삭제·다시 상세 | 없는 사원 안내 |

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/03_database/01_pymysql.py` 46–70행 · **원본 발췌**

```python
@app.get('/emp/deptno')
def emp_list_deptno(deptno: int, request: Request):
    connect = get_connect()

    emp_list = []
    try:
        with connect.cursor() as cursor :

            sql = '''
                select * from emp
                where deptno = %s
            '''

            cursor.execute(sql, (deptno,))

            emp_list = cursor.fetchall()
            print(emp_list)
    except Exception as e :
        print(e)
    finally :
        connect.close()

    return templates.TemplateResponse(request, 'list.html', {
        'emp_list' : emp_list
    })
```

**발췌 바로 풀이:** get_connect 호출은 try밖이다. 연결을 얻은 뒤 SQL오류는 except에서 빈 목록으로 이어질 수 있지만 연결 생성 자체가 실패하면 이 try가 잡지 못한다. 이전 “연결 실패도 빈 목록”이라는 설명을 이 위치에 맞게 교정한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/03_database/02_sqlmodel.py` 38–76행 · **원본 발췌**

```python
def get_session():
    # SQLite에서 cursor가 session같은 역할
    with Session(engine) as session :
        yield session
        session.commit() # 정상 세션이 실행되었을 떄 commit하면 좋음

# 서버를 실행할 때 실행되게끔 할 수 있음(테이블 생성)
@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get('/emp/deptno')
def emp_list_deptno(
    request: Request,
    deptno: int,
    session: Session = Depends(get_session)
):
    emp_list = []
    try:
        # '%s'로 인자값을 받았던 것 보다 더 안전한 방식(text)
        # text는 sql문을 실행하기 전에 미리 컴파일 해둠(실행속도 증가)
        # :변수명은 DB에서 변수를 사용하는 방식
        sql = text('''
            select * 
            from emp3
            where deptno = :deptno
        ''')

        # fetch와 다르게 결과를 돌려주기에 변수에 담아 사용
        result = session.execute(sql, {'deptno': deptno}) 
        # emp_list = result.all() # fetchall과 같은 기능
        # emp_list = result.fetchall()
        # cursorclass=pymysql.cursors.DictCursor 와 다르게 mappings()로 변환 가능
        emp_list = result.mappings().fetchall() 
        print(emp_list)

        return templates.TemplateResponse(request, 'list.html', {
            'emp_list' : emp_list
        })
```

**발췌 바로 풀이:** yield가 세션을 제공하고 요청 뒤 commit이 이어진다. Session은 sqlite3.Cursor와 같은 객체가 아니며 text를 썼다는 사실만으로 안전성·속도 우열이 입증되지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/03_database/DTO/EmpDTO.py` 6–21행 · **원본 발췌**

```python
class Emp3(SQLModel, table=True):
    # tablename이 없다면 클래스명이 테이블명이 됨
    # __tablename__ = 'emp' 

    empno: int = Field(primary_key = True)
    ename: str
    job: str
    # mgr: int | None = None # null이 있다면 none으로 처리하는 필터
    mgr: Optional[int] = None
    hiredate: str
    sal: float
    # comm: float | None = None
    comm: Optional[float] = None
    deptno: int = Field(
        foreign_key='dept3.deptno'
    )
```

**발췌 바로 풀이:** 강사님 `Emp3(SQLModel)`에는 `table=True`가 없고, 내 `Emp3(SQLModel, table=True)`에는 있다. 따라서 `SQLModel.metadata.create_all(engine)`이 **강사님 `Emp3`을 자동으로 테이블 등록하는 예제라고 읽으면 안 된다**. 내 모델은 테이블 모델로 지정돼 있다. 실제 DB에 `emp3`가 이미 있는지와 새로 생성되는지는 실행 환경을 따로 확인해야 한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/03_database/03_emp.py` 120–143행 · **원본 발췌**

```python
@app.get('/emp/select')
def emp_select(    
    request: Request,
    # count:int,
    session: Session = Depends(get_session)
):
    print('/emp/select 진입')
    sql = text('''
        select * 
        from emp_pr
    ''')

    result = session.execute(sql) 
    emp_list = result.mappings().fetchall() 
    # print('req : ',request)
    # print('session : ', session)
    # print('result : ', result)
    # print('emp_list : ', emp_list)

    return templates.TemplateResponse(request, 'select.html', {
        'emp_list' : emp_list,
        # 'count' : count
    })

```
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/03_database/03_emp.py` 144–175행 · **원본 발췌**

```python
# 수정 페이지 이동 시 화면 불러오기 + 새로 데이터 조회
@app.get('/emp/detail')
def emp_detail(
    request: Request,
    empno: int,
    session: Session = Depends(get_session)
) :
    print('/emp/detail 진입')

    url = text('''
        select *
        from emp_pr
        where empno = :empno
    ''')

    # session 실행으로 DB url로 이동하여 가져온 cursor값을 result에 저장
    result = session.execute(url, {
        'empno' : empno
    })
    emp_list = result.mappings().fetchall()

    for emp in emp_list :
        return templates.TemplateResponse(request, 'detail.html', {
            'empno' : emp['empno'],
            'ename' : emp['ename'],
            'job' : emp['job'],
            'mgr' : emp['mgr'],
            'hiredate' : emp['hiredate'],
            'sal' : emp['sal'],
            'comm' : emp['comm'],
            'deptno' : emp['deptno']
        })
```

**발췌 바로 풀이:** 강사님은 `emp3`, 나는 `emp_pr`를 조회한다. 목록은 여러 행을 템플릿으로 넘기고, 상세는 사원 번호 조건으로 한 사람을 찾는다. 강사님은 `fetchone()`으로 한 행, 나는 `fetchall()` 뒤 첫 행을 반복문에서 반환한다. 내 상세 코드에서 **결과가 0행이면 반복문에 들어가지 않아 응답을 명시적으로 반환하지 않는다**. 사원이 없을 때의 화면은 완성되지 않았다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/03_database/03_emp.py` 43–102행 · **원본 발췌**

```python
# DB에 POST로 데이터 추가
@app.post('/emp/insert')
async def emp_insert(
    request: Request,
    emp : Annotated[Emp_pr_input, Form()], 
    session: Session = Depends(get_session)
):
    print('/emp/insert 실행')
    # POST Form으로 받아오기 위해 form() 설정
    # data = await request.form()
    # print(data)
    print('Annotated EMP : ',emp)

    # empno = data.get('empno')
    # ename = data.get('ename')
    # job = data.get('job')
    # mgr = data.get('mgr')
    # hiredate = data.get('hiredate')
    # sal = data.get('sal')
    # comm = data.get('comm')
    # deptno = data.get('deptno')
    # print(empno, ename, job, mgr, hiredate, sal, comm, deptno)

    # DB에 insert시 테이블명, 값 작성
    count = -1
    try:
        sql = text('''
            insert into emp_pr (empno, ename, job, mgr, hiredate, sal, comm, deptno)
            values (:empno, :ename, :job, :mgr, :hiredate, :sal, :comm, :deptno)
        ''')

        result = session.execute(sql, {
            'empno' : emp.empno,
            'ename' : emp.ename,
            'job' : emp.job,
            'mgr' : emp.mgr,
            'hiredate' : emp.hiredate,
            'sal' : emp.sal,
            'comm' : emp.comm,
            'deptno' : emp.deptno
        }) 
        print('실행 결과로 영향을 받은 row 수 : ',result.rowcount)
        count = result.rowcount
        session.commit()
    except :
        count = 0
        session.rollback()

    if count == 0 :
        return RedirectResponse(
            url = f'/emp/insert?count={count}',
            status_code = 303, # 기본값은 307
        )

    else :
        return RedirectResponse(
            # url = f'/emp/select?count={count}',
            url = '/emp/select',
            status_code = 303, # 기본값은 307
        )
```

**발췌 바로 풀이:** 강사님은 `Emp3 = Form()`으로, 나는 `Annotated[Emp_pr_input, Form()]`으로 입력을 받는다. `INSERT`의 `:empno` 같은 이름에 각 모델의 값을 매핑한다. 내 코드는 성공하면 `session.commit()` 후 `/emp/select`로, 실패하면 `rollback()` 후 입력 화면으로 **303 리다이렉트**한다. 강사님도 입력 값과 SQL 매개변수를 분리해 보이며 결과 행 수를 검사한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/03_database/03_emp.py` 227–264행 · **원본 발췌**

```python
    sql = text('''
        update emp_pr
        set ename = :ename, 
            job = :job, 
            mgr = :mgr, 
            hiredate = :hiredate, 
            sal = :sal, 
            comm = :comm, 
            deptno = :deptno
        where empno = :empno
    ''')

    # result = session.execute(sql, {
    #     'empno' : empno,
    #     'ename' : ename,
    #     'job' : job,
    #     'mgr' : mgr,
    #     'hiredate' : hiredate,
    #     'sal' : sal,
    #     'comm' : comm,
    #     'deptno' : deptno
    # })
    result = session.execute(sql, {
        'empno' : emp.empno,
        'ename' : emp.ename,
        'job' : emp.job,
        'mgr' : emp.mgr,
        'hiredate' : emp.hiredate,
        'sal' : emp.sal,
        'comm' : emp.comm,
        'deptno' : emp.deptno
    }) 
    print('실행 결과로 영향을 받은 row 수 : ',result.rowcount)

    return RedirectResponse(
        url = '/emp/select',
        status_code = 303, # 기본값은 307
    )
```
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/03_database/03_emp.py` 266–288행 · **원본 발췌**

```python
@app.post('/emp/delete')
async def emp_delete(
    request: Request,
    session: Session = Depends(get_session)
):
    print('/emp/delete 실행')
    data = await request.form()
    empno = data.get('empno')

    sql = text('''
        delete from emp_pr
        where empno = :empno
    ''')

    result = session.execute(sql, {
        'empno' : empno
    }) 
    print('실행 결과로 영향을 받은 row 수 : ',result.rowcount)

    return RedirectResponse(
        url = '/emp/select',
        status_code = 303, # 기본값은 307
    )
```

**발췌 바로 풀이:** 수정과 삭제 모두 `WHERE empno = :empno`로 **대상 사원**을 지정한다. 강사님은 수정·삭제 함수 안에서 `commit()`을 호출한다. 내 수정·삭제는 함수 안의 명시적 커밋 대신 `get_session()`의 `yield` 뒤 `session.commit()`에 의존한다. 예외를 함수 안에서 잡아 숨기는 방식과 세션 종료 시점이 결과에 영향을 줄 수 있으므로 실제 DB 상태를 확인해야 한다. 이 코드는 학습용 구현이며 “요청을 보내면 항상 안전하게 저장된다”는 보장은 없다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/03_database/DTO/EmpDTO.py` 23–66행 · **원본 발췌**

```python
class Emp_pr(SQLModel, table=True):
    # 아래처럼 하면 Auto increment가 가능함
    empno: int | None = Field(
        default=None, 
        primary_key=True
    )
    ename: str
    job: str
    mgr: Optional[int] = None
    hiredate: str
    sal: float
    comm: Optional[float] = None
    deptno: int

class Emp_pr_input(SQLModel):
    # 아래처럼 하면 Auto increment가 가능함
    empno: int | None = Field(
        default=None, 
        primary_key=True
    )
    ename: str
    job: str
    mgr: Optional[int] = None
    hiredate: str
    sal: float
    comm: Optional[float] = None
    deptno: int

    # 값을 검증해주는 데코레이터
    # 'comm'에 값을 넣기 전(mode='before')에 def함수를 실행시켜라
    @field_validator('comm', 'mgr', mode='before')
    @classmethod
    def empty_to_None1(cls, value):
        if value == "":
            return None
        else :
            return value
        # return None if value == "" else value
        # return value if value != "" else None

    @model_validator(mode='before')
    @classmethod
    def empty_to_None2(cls, value):
        return value if value != "" else None
```

**발췌 바로 풀이:** Emp_pr은 테이블 모델, Emp_pr_input은 입력 모델이다. field_validator는 comm·mgr의 각 입력 빈 문자열을 None으로 바꾼다. model_validator는 입력 전체를 받으므로 전체 dict와 빈 문자열을 비교한 것만으로 각 필드를 한꺼번에 정리하지는 못한다.

내 PyMySQL은 emp를 조회하고 SQLModel 기초는 emp3, 사원 앱은 emp_pr을 쓴다. 같은 표의 같은 결과로 섞지 않는다. 내 상세는 fetchall 뒤 반복문 안 return이라0행이면 반환 없이 끝날 수 있다. 내 생성은 명시적 commit/rollback이 있지만 수정·삭제는 get_session의 yield 뒤 commit에 의존한다. 강사님 Emp3에 table=True가 없어 metadata.create_all이 그 클래스를 표로 만든다고 설명하면 틀린다. 학생의 Emp3·Emp_pr에는 table=True가 있다.

<a id="connections"></a>

## 5. import·함수·화면·저장이 연결되는 흐름

원본 입력 화면의 name → Emp_pr_input 필드 → validator → emp_insert의 SQL값 dict → Session.execute → result.rowcount → commit/rollback →303 → 목록 SELECT → mappings행 → 템플릿이다. 새 예제는 models.py에서 BookEmp·EmpInput을 모두 정의하고 db.py의 init_db·get_session도 제공한다. 원본 get_connect는 pymysql.connect로 연결을 반환하는 준비 함수다. 계정·암호·연결 주소가 있는 실제 줄은 인용하지 않으며 그 값을 추측해 새 예제에 넣지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 앱은 입력 모델과 테이블 모델을 나누고 매개변수 바인딩·실패 롤백·저장 뒤 이동을 직접 연결했다. **교정:** text는 실행 속도를 자동 보장하지 않고 Session이 Cursor 그 자체도 아니다. **한계:** 조회 오류를 빈 목록으로 숨기면 정상0명과 구별하기 어렵다. 생성 시 모델 검증·DB제약·rowcount는 서로 다른 검사다. **개선 선택:** 새 예제는 변경 함수에서 commit위치를 명시해 원본의 yield 뒤 확정과 구분했다. 원본의 응답 후 정리·실패 전파를 임의로 완성했다고 쓰지 않는다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_python/03_database/DTO/EmpDTO.py` 5–13행 · **원본 발췌**

```python
class Emp3(SQLModel):
    # 없으면 클래스명이 테이블 명이 된다
    # __tablename__ = "emp"

    # empno: int = Field(primary_key = True)
    empno: int | None = Field(
        default = None,         # auto_increment
        primary_key = True
    )
```

출처: `D:/workspace_teacher/workspace_python/03_database/03_emp.py` 97–138행 · **원본 발췌**

```python
    count = 0
    try:
        # db에 넣기
        query = text('''
            insert into emp3 (empno, ename, job, mgr, hiredate, sal, comm, deptno)
            values (
                :empno,
                :ename,
                :job,
                :mgr,
                :hiredate,
                :sal,
                :comm,
                :deptno
            )
        ''')
        result = session.execute(query, {
            'empno': empDTO.empno,
            'ename': empDTO.ename,
            'job': empDTO.job,
            'mgr': empDTO.mgr,
            'hiredate': empDTO.hiredate,
            'sal': empDTO.sal,
            'comm': empDTO.comm,
            'deptno': empDTO.deptno
        })
        
        # rowcount
        # insert, update, delete등을 통해 
        # 영향을 받은 줄의 수
        count = result.rowcount
        
        # commit : auto commit이 아닌 경우 직접 확정해야 한다
        session.commit()
    except:
        print('오류! except로 빠짐')
        # 오류 추적 내용 출력
        traceback.print_exc()
        
        # 제약 조건 등의 오류 발생 시
        # 모두 되돌리기
        session.rollback()
```

테이블 등록 차이와 생성의 commit/rollback부분만 비교상 필요해 강사님 인용을 남긴다. 강사님 예문도 table=True누락 등 현재 파일의 상태 한계가 있다. 양쪽 어느 방식을 쓰든 실제 DB표 존재·키·입력·세션 경계를 확인해야 한다. 강사님이 도움이 되는 부분은 저장 결과 행 수와 실패 경로가 명시된 흐름이며 학생도 생성에서 같은 원칙을 작성했다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 단계 | 객체·자료 | 읽을 것 |
| --- | --- | --- |
|입력 | EmpInput | 필드·validator |
|자원 | Session | 의존성 정의·수명 |
|실행 | text와 dict | SQL과 값 분리 |
|결과 | mappings·rowcount | 조회 행·변경 수 |
|확정 | commit/rollback | 성공·실패 경계 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
|부서20→30조회 | 빈 목록 | 자료 조건 불일치 |
|같은 번호 삽입 | 실패 뒤 원본 행 유지 | 키 제약·rollback |
|없는 번호 수정 | changed0 | WHERE 일치 행 없음 |
|table=True제거 후 새 DB준비 | 해당 모델 표 미등록 | 입력 모델과 표 모델 차이 |
|comm에 비숫자 |422 | 모델 타입 검증 |

연결 단계 오류와 SQL실행 단계 오류를 먼저 나눈다. 표 없음이면 모델 등록·선택 DB·실제 표명을 본다. validator는 필드 입력인지 전체 입력인지 확인한다. 없는 사원을 조회하면0행을 처리하는 반환 분기를 본다. SQLite 새 예제가 통과했다고 실제 MariaDB의 키·접속·SQL모드까지 검증된 것으로 보지 않는다.

**확인 범위:** 새 앱을 별도 임시 폴더에 복사해 프레임워크 요청·응답 흐름으로 확인한다. 실제 외부 서비스·운영 DB·브라우저 공개 서버에 요청한 결과와 구별한다. 원본 전체 앱을 무조건 실행하지 않으며 별도 확인한 원본 구간은 검증 보고서에 기록한다. 사용자의 가상환경은 검사에 읽기만 사용하고 파일을 설치·수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 환경변수로 접속 정보 분리·세션 실패 전파·연결 풀·동시성·비동기 DB·마이그레이션·금액 정밀도 설계는 추가 학습이다. SQLite의 check_same_thread설정은 이 로컬 웹 예제를 위한 준비이며 모든 DB에 같은 옵션을 붙이는 규칙이 아니다. request.headers·response_model은 이번 수업 본문에 추가하지 않는다.

request.headers 직접 읽기와 response_model은 미학습으로 확인된 선택 확장이다. 본문에서 이 기능을 선행 조건으로 요구하지 않는다. 응답·입력 타입 표시와 response_model 설정도 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. %s와 :deptno는 어떤 공통 역할인가?
2. Depends에 get_session을 넘기는 이유는?
3. table=True없는 입력 모델도 create_all로 표가 되는가?
4. 전체 dict를 빈 문자열과 비교하면 각 필드가 정리되는가?
5. SQLModel을 쓰면 모든 SQL이 ORM자동 생성인가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

SQL문법과 값을 분리한다. FastAPI가 요청 자원을 제공하도록 함수를 등록한다. 테이블 모델로 등록되지 않는다. 각 필드 처리와 다르다. 원본은 text SQL을 직접 작성한다.

</details>

| 층 | 확인 |
| --- | --- |
|입력 | 폼·모델·빈 값 |
|자원 | engine·Session·Depends |
|SQL | 값 바인딩·WHERE |
|결과 | 행·없음·rowcount |
|저장 | commit·rollback |

[장별 연습문제](실습/연습문제/07_FastAPI_MariaDB_SQLModel_사원_CRUD_연습문제.md) · 다음은 [해시 실습](07-02_비밀번호_해시_실습.md)이다.
