# 02. 라우터·입력값·Pydantic·메모리 CRUD

[FastAPI 목차](README.md) · [이전: 첫 앱](01_FastAPI_가상환경과_웹_API_기초.md) · [다음: Jinja 템플릿](03_FastAPI_Jinja2_템플릿.md)

이번 수업 코드는 한 파일의 경로를 `APIRouter`로 분리하고, **쿼리 문자열·폼·경로값·JSON 본문**을 받는다. 내 별도 Todo CRUD는 리스트에 항목을 넣고 찾고 고치고 삭제한다. 배운 입력 통로를 먼저 구분한다.

## 1. `APIRouter`를 앱에 포함

### 강사님 코드

출처: `teacher/workspace_python/todos/01_router/api.py` 1–26행 · **원본 발췌**

```python
from fastapi import FastAPI, Request, HTTPException

from todo import todo_router
from crud import crud_router

app = FastAPI()

# 크로스 도메인 CORS 해결 코드
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get('/')
def welcome() -> dict :
    return {
        "message": "Hello World2"
    }

app.include_router(todo_router)
# app.include_router(crud_router, prefix='/crud')
app.include_router(crud_router, prefix='/api/v1')
app.include_router(crud_router)
```

### 내 코드

출처: `me/workspace_python/02_todos/01_router/api.py` 1–28행 · **원본 발췌**

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

`todo_router`, `crud_router`에서 정의한 경로는 `app.include_router(...)`로 앱에 등록된다. 강사님은 같은 `crud_router`를 기본 경로와 `/api/v1` 접두 경로에 모두 포함해 주소가 달라질 수 있음을 보여 준다. 나는 기본 경로 한 번만 포함했다.

양쪽의 `CORSMiddleware`도 실제 수업 코드다. 브라우저 페이지와 API의 출처가 다를 때 응답을 읽을 수 있는 출처·요청 방식을 정하는 설정이다. 두 코드의 `allow_origins=["*"]`와 `allow_methods=["*"]`는 허용 범위를 넓게 둔 실습 값이다. `allow_headers`는 **허용할 요청 헤더 이름 설정**이며, `request.headers`로 헤더 값을 직접 읽는 코드가 아니다. CORS의 배포 정책과 세부 동작은 [추가편](추가편_기존자료_학습범위_분류.md)으로 둔다.

## 2. 쿼리 문자열과 폼

### 강사님 코드

출처: `teacher/workspace_python/todos/01_router/todo.py` 26–40행 · **원본 발췌**

```python
@todo_router.get('/todo/param')
async def todoParamGet(id : int, item:str = "") -> dict :
    print(id, item)
    return {
        "id": id,
        "item": item
    }

@todo_router.post('/todo/param')
async def todoParamPost(id : int = Form(), item:str = Form()) -> dict :
    print(id, item)
    return {
        "id": id,
        "item": item
    }
```

### 내 코드

출처: `me/workspace_python/02_todos/01_router/todo.py` 23–42행 · **원본 발췌**

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

`GET /todo/param?id=3&item=공부`의 `id`, `item`은 주소의 `?` 뒤 **쿼리 문자열**이다. `id: int`는 숫자로 해석하고, 숫자가 아니면 입력 검증 오류가 난다. `item: str = ''`는 생략할 수 있는 기본값이다. `POST`의 `id = Form()`, `item = Form()`은 HTML 폼의 `name`이 같은 값을 받는 방식이다. 강사님은 핵심 코드만, 나는 타입 오류와 기본값을 주석으로 더 풀어 적었다.

### 강사님 코드 — `Request`에서 직접 읽기

출처: `teacher/workspace_python/todos/01_router/todo.py` 42–59행 · **원본 발췌**

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

### 내 코드 — 완성되지 않은 직접 읽기 실습

출처: `me/workspace_python/02_todos/01_router/todo.py` 44–63행 · **원본 발췌**

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

강사님은 GET이면 `req.query_params`, 나머지 방식이면 `await req.form()`으로 분기한다. 내 코드는 GET 부분만 `data`에 넣고 POST·PUT·DELETE 분기에서 값을 넣지 않은 채 `data.get(...)`을 호출한다. 따라서 내 `/todo/param2`는 **GET 외 방식에서 `data`가 정의되지 않아 실패할 수 있다**. 내 코드도 실제 실습이므로 그대로 보여 주고, 이 부분은 강사님 방식이 완성도가 높다고 표시한다.

## 3. 경로값 검증과 Pydantic 모델

### 강사님 코드

출처: `teacher/workspace_python/todos/01_router/model.py` 1–9행 · **원본 발췌**

```python
from pydantic import BaseModel, Field

class Todo(BaseModel) :
    id:int
    item:str

class Todo2(BaseModel) :
    id:int = Field(ge=1, le=100)
    item:str = Field(min_length=2, max_length=20)
```

### 내 코드

출처: `me/workspace_python/02_todos/01_router/model.py` 1–15행 · **원본 발췌**

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

`BaseModel`은 JSON 본문 같은 입력의 **필드 이름·자료형**을 정한다. `Field(ge=1, le=100)`은 범위, `Field(min_length=2, max_length=20)`은 문자열 길이를 검사한다. 여기서 놓치기 쉬운 차이는 강사님 `Todo`가 `id`, `item`인데 내 `Todo`는 `value1`, `value2`라는 것이다. 아래 `/todo43`와 `/todo/{todo_id}`에서 내 코드는 `todo.id`를 기대한다. **내 모델 그대로라면 `.id` 접근이 맞지 않는다.** 강사님 모델 이름은 그 경로와 맞지만, 강사님도 같은 리스트에 앞서 딕셔너리를 넣는 `/todo`를 실행했다면 `.id` 접근에서 자료형이 섞이는 문제가 생길 수 있다.

### 강사님 코드 — 경로·쿼리 제한

출처: `teacher/workspace_python/todos/01_router/todo.py` 83–119행 · **원본 발췌**

```python
# Valid, Validate 유효성 검증
from fastapi import Path
@todo_router.get('/todo2/{todo_id}')
async def get_single_todo2(todo_id: int = Path(gt=10, le=100)) -> dict :
    print('todo_id :', todo_id)

    for todo in todo_list:
        if todo.id == todo_id:
            return {
                'todo': todo
            }
    return {
        'message': 'id 없음'
    }

from typing import Annotated

ValidTodoId = Annotated[int, Path(ge=10)]

@todo_router.get('/todo3/{todo_id}')
# async def get_single_todo3(todo_id: Annotated[int, Path(ge=10)]) -> dict :
async def get_single_todo3(todo_id: ValidTodoId) -> dict :
    print('todo_id :', todo_id)

    for todo in todo_list:
        if todo.id == todo_id:
            return {
                'todo': todo
            }
    return {
        'message': 'id 없음'
    }

# get 방식일 때 즉 ? 뒤에 오는 query string
from fastapi import Query
@todo_router.get('/todo4')
def todo4(id:int = Query(gt=0, lt=10000)):
```

### 내 코드 — 경로·쿼리 제한

출처: `me/workspace_python/02_todos/01_router/todo.py` 188–225행 · **원본 발췌**

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

`/todo2/{todo_id}`의 `todo_id`는 **경로값**, `/todo4?id=...`의 `id`는 **쿼리값**이다. `Path(gt=10, le=100)`은 10 초과·100 이하, `Query(gt=0, lt=10000)`은 0 초과·10000 미만을 검사한다. 양쪽 코드 모두 `Annotated`로 재사용하는 경로값 형태도 실제 작성했다.

## 4. 내 리스트 CRUD와 강사님 방식

### 강사님 코드 — 폼 모델을 저장

출처: `teacher/workspace_python/todos/01_router/crud.py` 51–67행 · **원본 발췌**

```python
# 성공
# 위의 것과 같은 내용을 Annotated로 사용한 경우
async def crud_c(todo3: Annotated[Todo3, Form()]) :
    id = todo3.id
    item = todo3.item
    print(3, id, item, todo3)

    todo_list.append(todo3)

    return id, item

@crud_router.get('/crud')
async def crud() :
    print('/crud 실행')
    print(4, todo_list)

    return todo_list
```

### 내 코드 — 생성·조회

출처: `me/workspace_python/02_todos/01_router/crud.py` 40–61행 · **원본 발췌**

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

### 내 코드 — 수정·삭제

출처: `me/workspace_python/02_todos/01_router/crud.py` 63–79행 · **원본 발췌**

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

강사님은 `Annotated[Todo3, Form()]`으로 폼을 모델로 받은 뒤 리스트에 넣는다. 내 코드는 `await req.form()`에서 `todoID`, `todoITEM`을 꺼내 딕셔너리로 저장한다. 읽기는 입력 ID와 같은 항목을 찾고, 수정은 `todo['item']`을 바꾸며, 삭제는 다른 항목만 새 리스트에 모아 `todo_list[:]`로 **기존 리스트 내용을 교체**한다. 여기서는 메모리 리스트이므로 서버를 다시 시작하면 저장된 변경이 사라진다. 뒤의 Jinja Todo·DB 장과 구별한다.

## 직접 확인할 질문

1. `include_router`를 하지 않은 라우터의 경로는 앱에서 어떻게 되는가?
2. `GET /todo/param2`와 POST 요청에서 내 `data` 변수의 상태는 어떻게 다른가?
3. 내 `Todo(value1, value2)` 모델과 `.id`를 읽는 코드의 필드 이름은 맞는가?
4. 내 삭제 함수가 `todo_list[:]`를 쓰는 이유는 무엇인가?

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/02_FastAPI_Router_Request_Pydantic_CRUD_연습문제.md)

## 추가로 알면 좋은 것

`request.headers`를 읽는 예제와 `response_model` 설정은 두 수업 코드에서 확인되지 않았고, 사용자가 배우지 않았다고 확인했다. [추가편](추가편_기존자료_학습범위_분류.md)에만 둔다. 이 장의 본문은 실제로 작성한 **쿼리·폼·경로·모델·리스트 CRUD**다.
