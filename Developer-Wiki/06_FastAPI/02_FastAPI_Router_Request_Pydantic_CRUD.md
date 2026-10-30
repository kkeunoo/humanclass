# 02. 라우터와 입력·CRUD — 받은 값이 목록의 항목이 되기까지

[FastAPI 목차](README.md) · [읽기 안내](00_FastAPI_상세백과_읽기법.md)

요청의 값은 주소·경로·폼·JSON 본문처럼 서로 다른 곳에 있다. 라우터를 파일로 나눈 뒤에도 어느 모델을 가져오고 어떤 목록을 읽고 바꾸는지 전체 연결을 볼 수 있어야 한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

APIRouter의 정의와 앱 등록, 네 입력 통로, 모델 필드와 사용 이름을 연결한다. 리스트 생성·조회·수정·삭제의 결과와 없는 항목·검증 실패를 설명한다. 원본의 GET 외 data 누락과 모델 이름 불일치를 교정한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

라우터는 관련 주소·함수 등록을 모아 놓는 객체다. 모듈에서 라우터를 만들고 앱이 include_router로 포함해야 그 앱에서 요청을 받는다. Python import가 파일을 읽고 이름을 연결하는 일과 include_router가 경로를 앱에 등록하는 일을 구별한다.

| 입력 | 요청 예 | 함수에서 읽는 자리 |
| --- | --- | --- |
| 쿼리 | /todos?id=1 | 경로에 없는 일반 인자·Query |
| 경로 | /todos/1 | {todo_id}·Path |
| 폼 | 이름 있는 HTML 입력 | Form·await request.form() |
| JSON 본문 | id·item 객체 | BaseModel 인자 |

쿼리·폼에서 온 숫자는 전송 때 문자열이지만 int로 선언하면 프레임워크가 해석·검사한다. Request에서 직접 data.get으로 읽은 값은 자동으로 같은 모델 검사를 거친 것이 아니다. 값이 없거나 형식이 틀리면 어느 단계에서 실패하는지 나눠 읽는다.

Pydantic 모델은 데이터 필드의 이름·자료형·제한을 선언한다. id와 item으로 정의했다면 todo.id·todo.item을 읽는다. 원본처럼 value1·value2로 정의하고 .id를 읽으면 이름이 어긋난다. Python 딕셔너리와 모델도 다르다. 딕셔너리는 todo['id'] 또는 get, 모델은 정의한 속성으로 읽는다.

CRUD는 생성·조회·수정·삭제의 네 작업을 뜻한다. 메모리 리스트는 같은 앱 프로세스에서 공유하는 예제 저장소이며 서버 재시작 뒤 유지되는 DB가 아니다. 같은 ID를 중복해서 넣는지, 없을 때 무엇을 반환할지도 따로 정해야 한다.

> 📚 **출처 · 본문 설명 확인:** [FastAPI 여러 파일 앱](https://fastapi.tiangolo.com/tutorial/bigger-applications/), [쿼리 인자](https://fastapi.tiangolo.com/tutorial/query-params/), [요청 본문](https://fastapi.tiangolo.com/tutorial/body/), [폼](https://fastapi.tiangolo.com/tutorial/request-forms/). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. api.py·models.py·routes.py를 같은 폴더에 둔다. 설치된 연습 환경에서 `python -m pip install fastapi uvicorn python-multipart`가 필요하고 `uvicorn api:app --port 8000 --reload`로 실행한다. 이 작업 중에는 패키지를 새로 설치하지 않고 기존 수업 환경을 읽어 검증했다. /docs에서 경로·방식·JSON·폼 입력을 구분해 보낼 수 있다. 아래 요청은 표의 순서대로 보내며 초기 목록은 비어 있다.



**[api.py](실습/책형_복습/02_FastAPI_Router_Request_Pydantic_CRUD/api.py) — 새 예제 전체 파일**

```python
from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)
```

**[models.py](실습/책형_복습/02_FastAPI_Router_Request_Pydantic_CRUD/models.py) — 새 예제 전체 파일**

```python
from pydantic import BaseModel, Field

class Todo(BaseModel):
    id: int = Field(ge=1, le=100)
    item: str = Field(min_length=2, max_length=20)
```

**[routes.py](실습/책형_복습/02_FastAPI_Router_Request_Pydantic_CRUD/routes.py) — 새 예제 전체 파일**

```python
from fastapi import APIRouter, Form, Path
from models import Todo

router = APIRouter()
todo_list = []

@router.get('/param')
def param(id: int, item: str = ''):
    return {'id': id, 'item': item}

@router.post('/form')
def form(id: int = Form(), item: str = Form()):
    return {'id': id, 'item': item}

@router.post('/todos')
def create(todo: Todo):
    todo_list.append(todo)
    return todo

@router.get('/todos/{todo_id}')
def read(todo_id: int = Path(ge=1, le=100)):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    return {'message': '없는 ID'}

@router.put('/todos/{todo_id}')
def update(todo_id: int, item: str):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = item
            return todo
    return {'message': '없는 ID'}

@router.delete('/todos/{todo_id}')
def delete(todo_id: int):
    remaining = []
    for todo in todo_list:
        if todo.id != todo_id:
            remaining.append(todo)
    todo_list[:] = remaining
    return todo_list
```

api가 routes의 router를 가져오고, routes는 models의 Todo를 가져온다. POST /todos에 JSON을 주면 모델을 만든 뒤 같은 todo_list에 넣는다. 조회는 .id를 비교해 항목을 반환한다. PUT의 item은 이 예제에서 쿼리 인자라 주소 뒤 ?item=복습에 둔다. DELETE는 남길 항목을 새 리스트에 모아 기존 리스트 내용 전체를 바꾼다. 새 모델·함수의 정의를 세 파일 모두 제공했다.

**요청과 예상 결과:**

| 순서 | 요청·입력 | 상태·결과 |
| --- | --- | --- |
| 1 | GET /param?id=3 | 200, id3·item빈문자열 |
| 2 | id=x 또는 id누락 | 422 |
| 3 | POST /form id3·item공부 | 200, 숫자3·문자열공부 |
| 4 | POST /todos {id:1,item:공부} | 200, 항목 생성 |
| 5 | GET /todos/1 | 생성한 항목 |
| 6 | GET /todos/0 | 422, 경계 실패 |
| 7 | GET /todos/2 | 200, 없는 ID 안내 |
| 8 | item한글자 생성 | 422, 길이 실패 |
| 9 | PUT /todos/1?item=복습 | 항목 내용 복습 |
| 10 | DELETE /todos/1 | [] |
| 11 | 다시 GET /todos/1 | 없는 ID 안내 |

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/01_router/api.py` 1–28행 · **원본 발췌**

```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from todo import todo_router
from crud import crud_router

app = FastAPI()

# CORS error : 크로스 도메인 에러 해결 코드
app.add_middleware (
    CORSMiddleware,
    # allow_origins는 어디에서 들어오던지 다 허용, IP를 입력하면 해당 IP만 접근할 수 있도록 가능
    # methods(방식_POST,GET등), headers(json등)도 모두 허용하겠다
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def welcome() -> dict: # -> dict는 딕셔너리 형태로 리턴하도록
    return {
        "message" : "Hello World2"
    }

# 불러 온 todo의 todo_router를 app에 추가
# include로 추가하면, 먼저 실행되기 때문에 2 todo가 먼저 프린트 됨
app.include_router(crud_router)
app.include_router(todo_router)
```

**발췌 바로 풀이:** `todo_router`, `crud_router`에서 정의한 경로는 `app.include_router(...)`로 앱에 등록된다. 강사님은 같은 `crud_router`를 기본 경로와 `/api/v1` 접두 경로에 모두 포함해 주소가 달라질 수 있음을 보여 준다. 나는 기본 경로 한 번만 포함했다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/01_router/todo.py` 23–42행 · **원본 발췌**

```python
# 인자값과, form에 name이 같을 경우 값을 쉽게 받을 수 있음
@todo_router.get('/todo/param')
# async def todoParamGet(id, item) -> dict :
async def todoParamGet(id : int, item : str = '') -> dict : # int로 지정하고 문자열을 넣었을 경우 422 Unprocessable Content 발생
    # item은 있지만 입력하지 않을 경우 ""빈 값이 들어가기 때문에 item자체가 안 들어왔다면 올바른 경로로 접근하지 않았을 수 있음
    # id는 int이기 때문에 빈 값일 때 ""가 들어가면 형변환이 안되어 에러 발생
    print(id, item) 
    return {
        "id" : id,
        "item" : item # 또는, 인자값이 2개지만 form에서 item을 없앴을 경우 값이 안 맞는다는 에러 발생
    }

# form에서 받으려면 fastspi Form을 import후 기본값을 Form()으로 지정
@todo_router.post('/todo/param')
async def todoParamPost(id : int = Form(), item : str = Form()) -> dict : 
    print(id, item) 
    return {
        "id" : id,
        "item" : item 
    }
```

**발췌 바로 풀이:** `GET /todo/param?id=3&item=공부`의 `id`, `item`은 주소의 `?` 뒤 **쿼리 문자열**이다. `id: int`는 숫자로 해석하고, 숫자가 아니면 입력 검증 오류가 난다. `item: str = ''`는 생략할 수 있는 기본값이다. `POST`의 `id = Form()`, `item = Form()`은 HTML 폼의 `name`이 같은 값을 받는 방식이다. 강사님은 핵심 코드만, 나는 타입 오류와 기본값을 주석으로 더 풀어 적었다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/01_router/todo.py` 44–63행 · **원본 발췌**

```python
# 아래처럼 Request를 import해서 사용할 수도 있음(POST일 때)
@todo_router.get('/todo/param2') # 조회
@todo_router.post('/todo/param2') #행동, 3개를 통틀어 사용하기도 함 form만 get,post지원, AJAX는 4개 모두 지원
@todo_router.put('/todo/param2')
@todo_router.delete('/todo/param2')
# 아래처럼 method를 받으면 get, post 두 가지 방식 모두 사용할 수 있음
# req: Request = req의 형태가 Request로
# Request에는 path도 있는데, path를 사용 시 포트 이후 ? 앞까지의 주소를 얻어올 수 있음
async def todoParam(req: Request) -> dict : 
    if req.method == 'GET' :
        data = req.query_params

    id = data.get('id')
    item = data.get('item')
    print(id, item, req.method) # POST method를 가져옴

    return {
        "id" : id,
        "item" : item 
    }
```

**발췌 바로 풀이:** 강사님은 GET이면 `req.query_params`, 나머지 방식이면 `await req.form()`으로 분기한다. 내 코드는 GET 부분만 `data`에 넣고 POST·PUT·DELETE 분기에서 값을 넣지 않은 채 `data.get(...)`을 호출한다. 따라서 내 `/todo/param2`는 **GET 외 방식에서 `data`가 정의되지 않아 실패할 수 있다**. 내 코드도 실제 실습이므로 그대로 보여 주고, 이 부분은 강사님 방식이 완성도가 높다고 표시한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/01_router/model.py` 1–15행 · **원본 발췌**

```python
from pydantic import BaseModel, Field

# pydantic BaseModel 사용해보기, 미리 자료형 선언
class Todo(BaseModel) :
    value1 : int
    value2 : str

# POST에서 Body영역으로 들어오는것을 잡아주는것들 Field로 쓸 수 있다
class Todo2(BaseModel) :
    id : int = Field(ge=1, le=100)
    item : str = Field(min_length=2, max_length=20)

class TodoItems(BaseModel) :
    todoID : int
    todoITEM : str
```

**발췌 바로 풀이:** `BaseModel`은 JSON 본문 같은 입력의 **필드 이름·자료형**을 정한다. `Field(ge=1, le=100)`은 범위, `Field(min_length=2, max_length=20)`은 문자열 길이를 검사한다. 여기서 놓치기 쉬운 차이는 강사님 `Todo`가 `id`, `item`인데 내 `Todo`는 `value1`, `value2`라는 것이다. 아래 `/todo43`와 `/todo/{todo_id}`에서 내 코드는 `todo.id`를 기대한다. **내 모델 그대로라면 `.id` 접근이 맞지 않는다.** 강사님 모델 이름은 그 경로와 맞지만, 강사님도 같은 리스트에 앞서 딕셔너리를 넣는 `/todo`를 실행했다면 `.id` 접근에서 자료형이 섞이는 문제가 생길 수 있다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/01_router/todo.py` 188–225행 · **원본 발췌**

```python
# Valid, Validate 유효성 검증
from fastapi import Path
@todo_router.get('/todo2/{todo_id}') # Path(gt=10, le=100) : 10초과 100이하
async def get_single_todo2(todo_id : int = Path(gt=10, le=100)) -> dict : # gt(greater than) = 10으로 10보다 크다로 사용할 수 있음
    print('todo_id :', todo_id)
    for todo in todo_list :
        if todo.id == todo_id:
            return {
                "todo" : todo
            }
        
    return {
        "message" : "없는 ID 입니다"
    }

from typing import Annotated # Annotated : 주석이라는 뜻

# 변수에 넣어서 가져다 쓸 수 있음
ValidTodoId = Annotated[int, Path(ge=10)]
@todo_router.get('/todo3/{todo_id}') 
# async def get_single_todo3(todo_id : Annotated[int, Path(ge=10)]) -> dict : # Annotated에 자료형, Path를 넣어 검증가능
async def get_single_todo3(todo_id : ValidTodoId) -> dict : 
    print('todo_id :', todo_id)
    for todo in todo_list :
        if todo.id == todo_id:
            return {
                "todo" : todo
            }
        
    return {
        "message" : "없는 ID 입니다"
    }

# GET방식일 때 Path와 달리 경로변수가 아닌 것들은 Query 사용 (?뒤에 오는 query string)
from fastapi import Query
@todo_router.get('/todo4') 
def todo4(id:int = Query(gt=0, lt=10000)) :
    print(id)
```

**발췌 바로 풀이:** `/todo2/{todo_id}`의 `todo_id`는 **경로값**, `/todo4?id=...`의 `id`는 **쿼리값**이다. `Path(gt=10, le=100)`은 10 초과·100 이하, `Query(gt=0, lt=10000)`은 0 초과·10000 미만을 검사한다. 양쪽 코드 모두 `Annotated`로 재사용하는 경로값 형태도 실제 작성했다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/01_router/crud.py` 40–61행 · **원본 발췌**

```python
@crud_router.post('/crud/c') # create - insert - post방식 / FORM
async def todoC(req : Request) :
    if req.method == 'POST' : # 생략 가능하지만 연습용
        data = await req.form()

        id = data.get('todoID')
        item = data.get('todoITEM')

        todo_list.append({
            'id' : int(id),
            'item' : item
        })
        return todo_list

@crud_router.get('/crud/r') # read - select - get방식 / FORM
async def todoR(todoID : int) :
    print(todoID)
    for todo in todo_list :
        # print(todo)
        # print(todo.get('id') == int(todoID))
        if todo.get('id') == todoID :
            return todo
```
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/01_router/crud.py` 63–79행 · **원본 발췌**

```python
@crud_router.put('/crud/u') # update - update - put방식 / AJAX
async def todoU(todoID : int, todoITEM : str) :
    for todo in todo_list :
        if todo.get('id') == todoID :
            todo['item'] = todoITEM
            return todo_list

@crud_router.delete('/crud/d') # delete - delete - delete방식 / AJAX
async def todoD(todoID : int) :
    result_todo = []

    for todo in todo_list :
        if todo.get('id') != todoID :
            result_todo.append(todo)

    todo_list[:] = result_todo
    return todo_list
```

**발췌 바로 풀이:** 강사님은 `Annotated[Todo3, Form()]`으로 폼을 모델로 받은 뒤 리스트에 넣는다. 내 코드는 `await req.form()`에서 `todoID`, `todoITEM`을 꺼내 딕셔너리로 저장한다. 읽기는 입력 ID와 같은 항목을 찾고, 수정은 `todo['item']`을 바꾸며, 삭제는 다른 항목만 새 리스트에 모아 `todo_list[:]`로 **기존 리스트 내용을 교체**한다. 여기서는 메모리 리스트이므로 서버를 다시 시작하면 저장된 변경이 사라진다. 뒤의 Jinja Todo·DB 장과 구별한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/01_router/crud.py` 1–23행 · **원본 발췌**

```python
from fastapi import APIRouter, Request, Form
from model import TodoItems

crud_router = APIRouter()
# 아래처럼 prefix로 주소 앞 기본값을 설정해준다면, 모두 통일 됨
# crud_router = APIRouter( prefix='/crud' )

todo_list = []

d1 = {
    'id' : 1684,
    'item' : 'item1'
}
todo_list.append(d1)

d2 = {
    'id' : 29681,
    'item' : 'item2'
}
todo_list.append(d2)

# @crud_router.get('/crud/r') # read - select - get방식
# async def todoR(req : Request) :
```

**발췌 바로 풀이:** 실제 crud.py의 목록 선언과 초기 두 딕셔너리를 보완 인용했다. 모델 TodoItems는 가져왔지만 이 CRUD에서는 폼을 직접 읽어 딕셔너리로 저장한다. 조회·수정은 get으로 그 키를 읽는다. 원본 ID1684와29681을 새 예제 ID1과 혼동하지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/01_router/todo.py` 71–158행 · **원본 발췌**

```python
'''
@todo_router.get('/problem/99')
async def problemGet(problem_99 : int) : 
    print(problem_99) 

    result = ''
    if 2 <= problem_99 <= 9 :
        for i in range(1,10) :
            problemResult = problem_99 * i 
            result += f'{problem_99} x {i} = {problemResult} '
    else :
        return f'2단부터 9단까지만 입력해주세요.'
    print(result)
    return result

'''
문제 2
클라이언트에서
- 숫자 두 개를 입력
파이썬에서
- 두 개의 합을 출력
'''
@todo_router.get('/problem/plus')
async def problemGet(problem_plus1 : int, problem_plus2 : int) : 
    print(problem_plus1 + problem_plus2)
    result = problem_plus1 + problem_plus2
    return result

'''
문제 3
웹에서
- 숫자 2개와 연산자를 입력
- 2, "-", 3
파이썬에서
- 결과 출력
- 화면에도 출력
'''
@todo_router.get('/problem/calc')
async def problemGet(problem_calc1 : int, problem_calc2 : int, problem_calc3) : 
    result = 0
    print(problem_calc1, type(problem_calc1))
    print(problem_calc2, type(problem_calc2))
    print(problem_calc3, type(problem_calc3))

    # operator = str(problem_calc3)
    if problem_calc3 == '-' :
        result = problem_calc1 - problem_calc2
    elif problem_calc3 == '+' :
        result = problem_calc1 + problem_calc2
    elif problem_calc3 == '%' :
        result = problem_calc1 % problem_calc2
    elif problem_calc3 == '/' :
        result = problem_calc1 / problem_calc2
    elif problem_calc3 == '*' :
        result = problem_calc1 * problem_calc2
    else :
        return f'- , + , % , / , * 만 입력하세요.'
    print(result)
    return result

@todo_router.get('/problem/practice')
async def problemGet(problem_practice) :
    value = []
    value.append(problem_practice)

    try:
        valueSplit = ''.join(value).split(';')
        valueSplit[0] = int(valueSplit[0])
        valueSplit[1] = int(valueSplit[1])
        valueSplit[2] = str(valueSplit[2])

        result = 0
        if valueSplit[2] == '-' :
            result = valueSplit[0] - valueSplit[1]
        elif valueSplit[2] == '+' :
            result = valueSplit[0] + valueSplit[1]
        elif valueSplit[2] == '*' :
            result = valueSplit[0] * valueSplit[1]
        elif valueSplit[2] == '/' :
            result = valueSplit[0] / valueSplit[1]
        elif valueSplit[2] == '%' :
            result = valueSplit[0] % valueSplit[1]
        else :
            return f'연산자는 - , + , % , / , * 만 입력하세요.'

        return result
    except :
        return f'연산자를 정확히 입력하세요.'
```

**발췌 바로 풀이:** 원본의 실제 구구단·두 수 합·연산자·세미콜론 입력 실습이다. 단순 설명 예제가 아니라 내가 작성한 경로다. 구구단은2~9만 허용하고 결과 문자열을 누적한다. 합은 숫자로 반환한다. 계산기는 연산자 갈래를 고르며 나눗셈·나머지의0 제수는 첫 계산기에서 처리하지 않는다. 세미콜론 버전의 넓은 except는 칸 수·정수·0 제수 등의 서로 다른 실패를 같은 연산자 안내로 숨긴다.

내 todo.py의 GET /todo/param에서 item은 기본값이 있어 생략하면 빈 문자열이며 반드시 오류가 나는 것은 아니다. /param2는 GET만 data에 대입하므로 다른 방식에서는 UnboundLocalError가 날 수 있다. 원본 Todo는 value1·value2인데 단일 조회는 .id를 읽고 리스트에는 dict도 섞일 수 있어 두 종류의 불일치가 있다. 별도 crud.py는 딕셔너리 키를 일관되게 get으로 읽는다. 계산 실습의 같은 problemGet 이름은 다시 정의되지만 각 데코레이터 등록은 해당 시점 함수 객체를 기억하므로 이름 재정의만으로 앞 주소가 자동 삭제되는 것은 아니다.

<a id="connections"></a>

## 5. import·함수·화면·저장이 연결되는 흐름

api.py의 include_router → routes.py의 router → 경로 함수 → models.py의 Todo 필드 검사 → todo_list → 응답이다. 실제 원본의 api.py는 todo·crud 두 모듈을 가져온다. import 때 모듈의 일반 print가 실행될 수 있지만 include_router가 그 모듈을 먼저 import시킨다고 뒤집어 설명하지 않는다. 강사님은 crud 라우터를 기본 주소와 /api/v1 접두 주소에 모두 등록했고 내 앱은 기본 주소 한 번이다. CORS 설정의 allow_headers는 허용 헤더 이름 설정이며 request.headers 직접 읽기와 다르다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내가 입력 통로·타입·오류를 메모하고 별도 CRUD에서 실제 생성·조회·수정·삭제를 완성했다. 슬라이스 대입으로 목록 객체를 유지한 점도 Python 참조와 연결된다. **실제 오류:** GET 외 data 미정의, 모델 필드와 .id 불일치, dict·모델 혼합 가능성은 별개로 교정한다. **한계:** 원본 생성의 int(id)는 누락·비숫자에 실패할 수 있고 중복 ID를 막지 않는다. 새 예제도 중복 ID 정책·수정 문자열 길이 검사는 추가하지 않았으므로 생성 모델 검증이 수정 속성 대입까지 자동 검사한다고 설명하지 않는다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_python/todos/01_router/todo.py` 42–59행 · **원본 발췌**

```python
@todo_router.get('/todo/param2')
@todo_router.post('/todo/param2')
@todo_router.put('/todo/param2')
@todo_router.delete('/todo/param2')
async def todoParam(req : Request) -> dict :
    if req.method == 'GET':
        data = req.query_params
    else :
        data = await req.form()

    id = data.get('id')
    item = data.get('item')
    print(id, item, req.method)

    return {
        "id": id,
        "item": item
    }
```

Request 직접 읽기의 분기 비교만 필요해 강사님 코드를 인용한다. 강사님은 GET 외에서 await req.form()으로 data를 정의해 내 누락을 보완한다. 다만 모든 POST·PUT·DELETE 본문이 언제나 폼이라는 규칙은 아니다. 실제 받기로 정한 입력 형식이 폼인 예제다. 모델 이름은 원래 정의와 사용을 맞춰야 하며 강사님 id·item과 내 value1·value2 차이는 계속 전파해 읽는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 단계 | 값·형태 | 결과 |
| --- | --- | --- |
| JSON 수신 | id1·item공부 | 모델 필드 검사 |
| append | Todo 객체 | 목록 한 항목 |
| GET 경로1 | 정수1 | .id 일치 |
| PUT 쿼리 | item복습 | 속성 변경 |
| DELETE | 남길 목록[] | 기존 목록 내용 교체 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| include_router 제거 | 해당 주소404 | 앱 미등록 |
| JSON id를0으로 | 422 | 생성 필드 ge1 |
| GET 없는 ID2 | 200 안내 | 현재 설계 |
| 같은 ID 다시 생성 | 중복 추가 | 중복 검사 없음 |
| 수정 item 한 글자 | 현재 예제 허용 | 생성 검증과 속성 대입 차이 |

422면 입력 위치·필드 이름·필수값·타입·범위를 본다. ID 없음 안내가 200인지 404인지 현재 설계를 구분한다. 모델에 없는 속성 오류면 정의 필드를 확인한다. 목록에 dict와 모델이 섞이면 어느 읽기 방식을 썼는지 본다. /param2의 data 오류는 입력값 변환보다 앞선 분기 누락이다.

**확인 범위:** 새 앱을 별도 임시 폴더에 복사해 프레임워크 요청·응답 흐름으로 확인한다. 실제 외부 서비스·운영 DB·브라우저 공개 서버에 요청한 결과와 구별한다. 원본 전체 앱을 무조건 실행하지 않으며 별도 확인한 원본 구간은 검증 보고서에 기록한다. 사용자의 가상환경은 검사에 읽기만 사용하고 파일을 설치·수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** response_model·request.headers 직접 읽기·세부 CORS 배포 정책·모델 대입 검증 설정·정교한404/409 설계·영구 저장은 선택 확장이다. 기본 CRUD는 실제 배운 메모리 목록이며 의도적으로 DB 앱인 것처럼 꾸미지 않는다.

request.headers 직접 읽기와 response_model은 미학습으로 확인된 선택 확장이다. 본문에서 이 기능을 선행 조건으로 요구하지 않는다. 응답·입력 타입 표시와 response_model 설정도 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. item 기본값이 있으면 쿼리에서 생략할 수 있는가?
2. /param2 POST에서 data는 정의되는가?
3. value1 모델에 .id가 있는가?
4. 생성 Field 검증이 수정 대입도 자동 검사하는가?
5. 원본 슬라이스 대입과 이름 재대입의 차이는?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

기본값을 쓴다. 원본은 GET 분기만 있어 정의되지 않는다. 없다. 기본 설정의 생성 검증과 속성 대입은 구분한다. 슬라이스는 기존 목록 객체의 내용을 바꾸고 이름 대입은 다른 객체에 이름을 연결할 수 있다.

</details>

| 확인 | 핵심 |
| --- | --- |
| 입력 | 경로·쿼리·폼·JSON |
| 모델 | 정의 필드·실제 속성 |
| 목록 | dict·모델·공유 상태 |
| 실패 | 검증·없는 대상·분기 누락 |

[장별 연습문제](실습/연습문제/02_FastAPI_Router_Request_Pydantic_CRUD_연습문제.md) · 다음은 [Jinja 템플릿](03_FastAPI_Jinja2_템플릿.md)이다.
