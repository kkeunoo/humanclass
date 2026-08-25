# pip install sqlmodel

from sqlmodel import create_engine, Session, SQLModel
from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates

from sqlalchemy import text

# SQLModel.metadata에 등록시키고,
# create_all로 테이블이 없으면 만들어 주고 
# EmpDTO의 class Emp3(SQLModel, table=True): 전달인자 두 개를 적으면 자동 생성
from DTO.EmpDTO import Emp3
from DTO.DeptDTO import Dept3

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

# 아래 형태로 사용하기도 함
# DATABASE_URL = (
#     'mysql+pymysql://'
#     'root'
#     ':human1234$'
# )

# DATABASE_URL = 'SQL+DRIVER(pymysql)://ID:PW@IP:PORT/DATABASE명
# SQLite는 한 번에 한 곳에서만 접속이 가능해서, {"check_same_thred": False} 를 사용하기도 함
DATABASE_URL = 'mysql+pymysql://root:human1234$@127.0.0.1:3306/human'
engine = create_engine(DATABASE_URL, echo=True)
# engine = create_engine(
#     DATABASE_URL, 
#     echo=True, 
#     # commit을 실행 안 해도 Autocommit을 할 수 있다(단, 롤백 할 수 없어 좋지 않음)
#     execution_options={
#         'isolation_level': 'AUTOCOMMIT'
#     } 
# )

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

    except Exception as e :
        print(e)

@app.get('/emp/update/sal')
def update_sal(
    per: int,
    session: Session = Depends(get_session)
):
    upsal = 1 + (per / 100) 
    print('upsal', upsal)

    try:
        sql = text('''
            update emp3
            set sal = sal * :upsal
            where deptno = 30
        ''')

        result = session.execute(sql, {'upsal': upsal}) 
        # session.commit()
        print('실행 결과로 영향을 받은 row 수 : ',result.rowcount)
    except Exception as e:
        print('ERR',e)
        session.rollback() # except발생 시 롤백


if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('02_sqlmodel:app', port=8000, reload=True, host="0.0.0.0")