# 07. 사원 DB CRUD — 입력 모델·세션·매개변수·화면·커밋 연결하기 — 연습문제

[본문](../../07_FastAPI_MariaDB_SQLModel_사원_CRUD.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

드라이버·엔진·세션·결과·모델의 역할을 구분한다. Depends(get_session)의 실제 정의와 yield 전후를 설명한다. PyMySQL %s와 text의 이름 매개변수, 테이블 모델과 입력 모델, 빈 입력 검증, 조회 없음·저장 실패·커밋 위치를 연결한다.

[본문 3절](../../07_FastAPI_MariaDB_SQLModel_사원_CRUD.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 요청과 결과 예상

**models.py**

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

**db.py**

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

**api.py**

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

**templates/employees.html**

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

실행 전에 결과를 먼저 적는다. 상태·응답·서버 출력·변경된 자료를 구별한다.

<details>
<summary>풀이</summary>

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

모델 모듈을 읽으면 table=True인 BookEmp가 구조 메타데이터에 등록된다. init_db는 그 구조를 새 파일에 만든다. 요청은 Depends를 통해 세션을 받고 입력 모델의 comm빈칸은 None으로 바뀐다. INSERT는 별도 dict값을 바인딩하고 commit한다. 다음 상세 요청은 새 세션에서 저장된 행을 읽는다. 같은 기본 키 INSERT는 실패해rollback하고 원래 행을 유지한다. 수정·삭제는 WHERE번호와rowcount를 확인한다. SQL에는원본의전체사원8열대신학습에필요한5열만사용한새예제다.

| 단계 | 객체·자료 | 읽을 것 |
| --- | --- | --- |
|입력 | EmpInput | 필드·validator |
|자원 | Session | 의존성 정의·수명 |
|실행 | text와 dict | SQL과 값 분리 |
|결과 | mappings·rowcount | 조회 행·변경 수 |
|확정 | commit/rollback | 성공·실패 경계 |

</details>

## 문제 2. 이유 설명

1. %s와 :deptno는 어떤 공통 역할인가?
2. Depends에 get_session을 넘기는 이유는?
3. table=True없는 입력 모델도 create_all로 표가 되는가?
4. 전체 dict를 빈 문자열과 비교하면 각 필드가 정리되는가?
5. SQLModel을 쓰면 모든 SQL이 ORM자동 생성인가?

<details>
<summary>풀이</summary>

SQL문법과 값을 분리한다. FastAPI가 요청 자원을 제공하도록 함수를 등록한다. 테이블 모델로 등록되지 않는다. 각 필드 처리와 다르다. 원본은 text SQL을 직접 작성한다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
|부서20→30조회 | 빈 목록 | 자료 조건 불일치 |
|같은 번호 삽입 | 실패 뒤 원본 행 유지 | 키 제약·rollback |
|없는 번호 수정 | changed0 | WHERE 일치 행 없음 |
|table=True제거 후 새 DB준비 | 해당 모델 표 미등록 | 입력 모델과 표 모델 차이 |
|comm에 비숫자 |422 | 모델 타입 검증 |

<details>
<summary>막힐 때 확인</summary>

연결 단계 오류와 SQL실행 단계 오류를 먼저 나눈다. 표 없음이면 모델 등록·선택 DB·실제 표명을 본다. validator는 필드 입력인지 전체 입력인지 확인한다. 없는 사원을 조회하면0행을 처리하는 반환 분기를 본다. SQLite 새 예제가 통과했다고 실제 MariaDB의 키·접속·SQL모드까지 검증된 것으로 보지 않는다.

</details>

## 채점과 복습

정상 값만 보지 말고 누락·잘못된 타입·없는 대상의 흐름도 설명한다. 새 예제는 별도 앱에서 확인하며 원본 DB나 외부 서비스의 성공을 대신 주장하지 않는다. TIP 확장은 필수 조건이 아니다. 정의→등록→입력→호출→반환→다음 요청을 연결할 수 있는지 검토한다.
