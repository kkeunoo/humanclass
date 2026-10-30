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
