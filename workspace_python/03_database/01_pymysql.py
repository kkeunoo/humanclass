# pip install fastapi uvicorn jinja2 pymysql

import pymysql
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

def get_connect(): 
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306, # mysql 또는 MariaDB 기본 Port
        database='human',
        user='root',
        password='human1234$',
        cursorclass=pymysql.cursors.DictCursor
    )

    return conn

def emp_list_deptno20():
    # SQLite3를 했던 것과 다르게 이것은 close를 별도로 해주어야 함
    connect = get_connect()

    try:
        with connect.cursor() as cursor :

            # pymysql은 SQLite와 다르게 '?'대신 '%s'를 사용
            sql = '''
                select * from emp
                where deptno = %s
            '''

            cursor.execute(sql, (20,))

            emp_list = cursor.fetchall()
            print(emp_list)
    except Exception as e :
        print(e)
    finally :
        connect.close()

# emp_list_deptno20()

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

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")