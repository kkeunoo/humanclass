# 07. FastAPI와 MariaDB — 조회에서 사원 CRUD까지

[FastAPI 목차](README.md) · [이전: SQLite](06_Python_SQLite와_Transaction.md)

이 장은 `03_database`의 **PyMySQL 조회 → SQLModel 세션 → 사원 화면 CRUD** 순서로 읽는다. 강사님과 내 파일에는 DB 연결 주소와 암호가 직접 들어 있어 그 줄은 Wiki에 옮기지 않았다. 여기의 원본 발췌는 요청·SQL·결과 처리 부분만 정확히 인용한다. 사용자가 제외한 `03_database/00_CSS` 개인 실험은 근거로 쓰지 않는다.

## 1. PyMySQL에서 부서 번호를 매개변수로 조회

### 강사님 코드

출처: `teacher/workspace_python/03_database/01_pymysql.py` 52–76행 · **원본 발췌**

```python
@app.get('/emp/deptno')
def emp_list_deptno(deptno:int, request:Request):
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
        'emp_list': emp_list
    })
```

### 내 코드

출처: `me/workspace_python/03_database/01_pymysql.py` 46–70행 · **원본 발췌**

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

`GET /emp/deptno?deptno=20`에서 받은 `deptno: int`가 SQL의 `%s` 자리에 **별도 매개변수**로 들어간다. SQLite의 `?`와 모양은 다르지만 문자열 이어 붙이기 대신 값을 따로 전달한다는 역할은 같다. `fetchall()`로 결과 행을 받고 `list.html`에 `emp_list`로 전달한다. 두 코드 모두 `finally`에서 연결을 닫는다. DB 연결 실패나 조회 오류가 있으면 빈 목록이 화면에 전달될 수 있으므로 “항상 사원 목록이 나온다”고 단정하지 않는다.

## 2. `Depends(get_session)`과 `:deptno`

### 강사님 코드

출처: `teacher/workspace_python/03_database/02_sqlmodel.py` 29–64행 · **원본 발췌**

```python
def get_session():
    with Session(engine) as session :
        yield session
        session.commit()

@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get('/emp/deptno')
def emp_list_deptno(
    request:Request,
    deptno:int,
    session:Session = Depends(get_session)
):
    emp_list = []
    try:
        # text : sql문을 실행하기 전에 미리 컴파일 해둔다
        sql = text('''
            select *
            from emp3
            where deptno = :deptno
        ''')

        result = session.execute(sql, {'deptno': deptno})
        # emp_list = result.fetchall()
        # emp_list = result.all()
        emp_list = result.mappings().fetchall()
        print(emp_list)
        
    except Exception as e :
        print(e)

    return templates.TemplateResponse(request, 'list.html', {
        'emp_list': emp_list
    })
```

### 내 코드

출처: `me/workspace_python/03_database/02_sqlmodel.py` 38–76행 · **원본 발췌**

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

`get_session()`은 `Session(engine)`을 열어 `yield`로 요청 함수에 제공한다. `session: Session = Depends(get_session)`가 그 연결을 받는 **의존성 주입**이다. 조회 SQL은 `:deptno`를 사용하고 `session.execute(sql, {'deptno': deptno})`에서 값을 따로 전달한다. `result.mappings().fetchall()`은 열 이름으로 읽을 수 있는 결과를 만든다. 내 주석의 “`text()`가 `%s`보다 더 안전하고 실행 속도가 증가”는 이 두 파일의 측정으로 입증된 비교가 아니다. 핵심은 **매개변수 바인딩과 세션 수명**이다.

### 강사님 모델과 내 모델의 중요한 차이

출처: `teacher/workspace_python/03_database/DTO/EmpDTO.py` 5–13행 · **원본 발췌**

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

출처: `me/workspace_python/03_database/DTO/EmpDTO.py` 6–21행 · **원본 발췌**

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

강사님 `Emp3(SQLModel)`에는 `table=True`가 없고, 내 `Emp3(SQLModel, table=True)`에는 있다. 따라서 `SQLModel.metadata.create_all(engine)`이 **강사님 `Emp3`을 자동으로 테이블 등록하는 예제라고 읽으면 안 된다**. 내 모델은 테이블 모델로 지정돼 있다. 실제 DB에 `emp3`가 이미 있는지와 새로 생성되는지는 실행 환경을 따로 확인해야 한다.

## 3. 화면 목록·상세 조회

### 강사님 코드

출처: `teacher/workspace_python/03_database/03_emp.py` 31–66행 · **원본 발췌**

```python
def get_session():
    with Session(engine) as session :
        yield session
        session.commit()

@app.get("/list")
def list(
    request:Request,
    session:Session = Depends(get_session) ) :

    try:
        # DB
        # 1. DB 접속
        #     전달 인자의 session:Session = Depends(get_session) ) :

        # 2. sql 준비
        query = text(f'''
            select * from emp3
        ''')
        print('>> 1 >> ', query)

        # 3. 실행
        #   select만 결과가 있다
        result = session.execute(query)
        print('>> 2 >> ', result)

        # 4. 결과 활용
        # emp_list = result.fetchall()
        # print('>> 3 >> fetchall >> ', emp_list)

        emp_list = result.mappings().fetchall()
        print('>> 4 >> .mappings().fetchall() >> ', emp_list)

        return templates.TemplateResponse(request, 'list.html', {
            'emp_list': emp_list
        })
```

출처: `teacher/workspace_python/03_database/03_emp.py` 162–181행 · **원본 발췌**

```python
@app.get('/detail/{empno}')
def detail(
    request:Request, 
    empno:int, 
    session:Session = Depends(get_session)):

    print('/detail/{empno}', empno)

    query = text('''
        select * from emp3
        where empno = :empno
    ''')

    result = session.execute(query, {'empno': empno})
    emp = result.mappings().fetchone()
    print(emp)

    return templates.TemplateResponse(request, 'detail.html', {
        'emp': emp
    })
```

### 내 코드

출처: `me/workspace_python/03_database/03_emp.py` 120–143행 · **원본 발췌**

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

출처: `me/workspace_python/03_database/03_emp.py` 144–175행 · **원본 발췌**

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

강사님은 `emp3`, 나는 `emp_pr`를 조회한다. 목록은 여러 행을 템플릿으로 넘기고, 상세는 사원 번호 조건으로 한 사람을 찾는다. 강사님은 `fetchone()`으로 한 행, 나는 `fetchall()` 뒤 첫 행을 반복문에서 반환한다. 내 상세 코드에서 **결과가 0행이면 반복문에 들어가지 않아 응답을 명시적으로 반환하지 않는다**. 사원이 없을 때의 화면은 완성되지 않았다.

## 4. 추가·수정·삭제의 저장 위치

### 강사님 코드 — 추가

출처: `teacher/workspace_python/03_database/03_emp.py` 84–90행 · **원본 발췌**

```python
@app.post('/api/add')
def api_add(
        # empno: int = Form(), # 이거 한번 쓰면 이 다음에 못씀
        request:Request,
        empDTO: Emp3 = Form(),
        session:Session = Depends(get_session),
) :
```

출처: `teacher/workspace_python/03_database/03_emp.py` 97–138행 · **원본 발췌**

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

출처: `teacher/workspace_python/03_database/03_emp.py` 147–160행 · **원본 발췌**

```python
    print('count : ', count)

    if count == 0 :
        # insert 실패
        return RedirectResponse(
            url=f'/add?count={count}',
            status_code=303
        )
    else :
        # insert 성공
        return RedirectResponse(
            url='/list',
            status_code=303
        )
```

### 내 코드 — 추가

출처: `me/workspace_python/03_database/03_emp.py` 43–102행 · **원본 발췌**

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

강사님은 `Emp3 = Form()`으로, 나는 `Annotated[Emp_pr_input, Form()]`으로 입력을 받는다. `INSERT`의 `:empno` 같은 이름에 각 모델의 값을 매핑한다. 내 코드는 성공하면 `session.commit()` 후 `/emp/select`로, 실패하면 `rollback()` 후 입력 화면으로 **303 리다이렉트**한다. 강사님도 입력 값과 SQL 매개변수를 분리해 보이며 결과 행 수를 검사한다.

### 강사님 코드 — 수정·삭제 대상

출처: `teacher/workspace_python/03_database/03_emp.py` 218–247행 · **원본 발췌**

```python
        query = text('''
            update 
                emp3
            set 
                ename = :ename,
                job = :job,
                mgr = :mgr,
                hiredate = :hiredate,
                sal = :sal,
                comm = :comm,
                deptno = :deptno
            where
                empno = :empno
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
        count = result.rowcount
        session.commit()
    except:
        print('오류! except로 빠짐')
        traceback.print_exc()
        session.rollback()
```

출처: `teacher/workspace_python/03_database/03_emp.py` 270–285행 · **원본 발췌**

```python
@app.post('/api/delete')
def delete(empno:int = Form(), session:Session = Depends(get_session)) :
    print('/api/delete', empno)

    try :
        query = text('''
            delete from emp3
            where empno = :empno
        ''')
        result = session.execute(query, {'empno': empno})
        count = result.rowcount
        session.commit()
    except:
        print('오류! except로 빠짐')
        traceback.print_exc()
        session.rollback()
```

### 내 코드 — 수정·삭제 대상

출처: `me/workspace_python/03_database/03_emp.py` 227–264행 · **원본 발췌**

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

출처: `me/workspace_python/03_database/03_emp.py` 266–288행 · **원본 발췌**

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

수정과 삭제 모두 `WHERE empno = :empno`로 **대상 사원**을 지정한다. 강사님은 수정·삭제 함수 안에서 `commit()`을 호출한다. 내 수정·삭제는 함수 안의 명시적 커밋 대신 `get_session()`의 `yield` 뒤 `session.commit()`에 의존한다. 예외를 함수 안에서 잡아 숨기는 방식과 세션 종료 시점이 결과에 영향을 줄 수 있으므로 실제 DB 상태를 확인해야 한다. 이 코드는 학습용 구현이며 “요청을 보내면 항상 안전하게 저장된다”는 보장은 없다.

## 직접 확인할 질문

1. PyMySQL의 `%s`와 SQLModel의 `:deptno`는 값 전달에서 어떤 공통 역할을 하는가?
2. `Depends(get_session)`이 함수에 제공하는 것은 무엇인가?
3. 강사님 `Emp3(SQLModel)`과 내 `Emp3(SQLModel, table=True)`는 무엇이 다른가?
4. 내 상세 조회에서 사원 번호가 없으면 어떤 분기가 실행되는가?

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/07_FastAPI_MariaDB_SQLModel_사원_CRUD_연습문제.md)

## 추가로 알면 좋은 것

연결 정보를 환경 변수로 분리하기, DB 연결 실패를 사용자 화면에 알리기, 트랜잭션 예외를 세밀하게 처리하기는 유용한 다음 학습이다. 기존 Wiki의 `response_model`·`request.headers` 설명은 사용자 확인상 배우지 않았고, 실제 이 수업 코드에도 없어 [추가편](추가편_기존자료_학습범위_분류.md)에만 둔다.
