from sqlmodel import create_engine, Session, SQLModel
from fastapi import FastAPI, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from sqlalchemy import text

from typing import Annotated
from DTO.EmpDTO import Emp_pr, Emp_pr_input

# FastAPI와 Jinja템플릿을 이용하기 위해 변수에 담아둠
app = FastAPI()
templates = Jinja2Templates(directory='templates/')

# DB에 로그인하기 위한 정보 입력 및 engine 구성
DATABASE_URL = 'mysql+pymysql://root:human1234$@127.0.0.1:3306/human'
engine = create_engine(DATABASE_URL, echo=True)

# 실 데이터들을 담아둘 빈 리스트 생성
emp_list = []

# DB에 접속해서 Sessin을 얻어오기 위한 함수 선언
def get_session():
    with Session(engine) as session :
        yield session
        # 정상적으로 세션을 가져와서 양보하면, 커밋
        session.commit() 

# SQLModel이고 table=true인것을 모두 찾아 create 진행
@app.on_event('startup')
def on_startup():
    SQLModel.metadata.create_all(engine)

# 추가 페이지 이동 시 화면 불러오기
@app.get('/emp/insert')
def emp_insert_loading(request: Request, count:int = -1):
    print('/emp/insert 이동')
    # 단순히 화면을 불러오는 것이기에 바로 리턴
    return templates.TemplateResponse(request, 'insert.html', {
        'count' : count
    })

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
    except :
        count = 0

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


 

# DB에서 데이터 모두 조회 후 화면 출력
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
    
@app.get('/emp/update')
def emp_update(
    request : Request,
    empno : int,
    session: Session = Depends(get_session)
) :
    print('/emp/update 진입')
    # print(empno)

    sql = text('''
        select * 
        from emp_pr
        where empno = :empno
    ''')

    result = session.execute(sql, {
        'empno' : empno
    }) 
    emp_list = result.mappings().fetchall() 

    return templates.TemplateResponse(request, 'update.html', {
        'empno' : emp_list[0]['empno'],
        'ename' : emp_list[0]['ename'],
        'job' : emp_list[0]['job'],
        'mgr' : emp_list[0]['mgr'],
        'hiredate' : emp_list[0]['hiredate'],
        'sal' : emp_list[0]['sal'],
        'comm' : emp_list[0]['comm'],
        'deptno' : emp_list[0]['deptno']
    })

@app.post('/emp/update')
async def emp_update_done(
    request : Request,
    emp : Annotated[Emp_pr, Form()],
    session: Session = Depends(get_session)
):
    print('/emp/update 완료')
    # data = await request.form()
    # print(data)

    # empno = data.get('empno')
    # ename = data.get('ename')
    # job = data.get('job')
    # mgr = data.get('mgr')
    # hiredate = data.get('hiredate')
    # sal = data.get('sal')
    # comm = data.get('comm')
    # deptno = data.get('deptno')

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

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('03_emp:app', port=8000, reload=True, host="0.0.0.0")