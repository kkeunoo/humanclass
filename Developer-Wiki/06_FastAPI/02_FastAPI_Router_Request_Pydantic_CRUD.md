---
title: FastAPI Router, Request, Pydantic과 CRUD
version: v2.0-final
last_updated: 2026-08-19
status: Completed
---

# FastAPI Router, Request, Pydantic과 CRUD

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `02_FastAPI_Router_Request_Pydantic_CRUD.md` |
| 분류 | `06_FastAPI` |
| 내 코드 | `workspace_python/todos/01_router/api.py`, `todo.py`, `model.py`, `crud.py`, `ajax.html`, CRUD 연습 파일 |
| 강사님 코드 | `workspace_teacher/workspace_python/todos/00_quiz`, `01_router/api.py`, `todo.py`, `model.py`, `crud.py`, `ajax.html`, `crud.html` |
| 실행 환경 | FastAPI 0.141.1, Pydantic 2.13.4, Starlette 1.6.0, Uvicorn 0.52.1 |
| 핵심 범위 | APIRouter, CORS, Middleware, Request, Form, Path, Query, Pydantic, HTTPException, CRUD, AJAX |
| 제외 범위 | 수업 진행 중인 `02_jinja`와 Template Rendering |
| 문서 형식 | FastAPI Developer-Wiki V2 |

> 이 문서는 완료된 `01_router` 수업을 기준으로 Router 분리, Request Data 처리, Pydantic 검증과 Memory 기반 Todo CRUD를 정리한다. 내 코드와 강사님 코드는 학습 시점과 실습 구현이 일부 다르므로 단순 우열이 아니라 실제 동작 차이와 수정할 부분을 구분한다.

---

# 학습 목표

- `APIRouter`로 Route를 Module별로 분리할 수 있다.
- `include_router()`의 역할을 설명할 수 있다.
- CORS가 발생하는 Origin 조건과 Middleware의 역할을 이해할 수 있다.
- `Request`에서 Method, Client, URL, Header, Cookie 등을 확인할 수 있다.
- Path Parameter와 Query Parameter를 구분할 수 있다.
- JSON Body, Form Data, Query String의 처리 방식을 구분할 수 있다.
- Pydantic Model로 입력값과 출력값을 검증할 수 있다.
- `Path`, `Query`, `Field`의 제한 조건을 사용할 수 있다.
- REST 방식의 CRUD Endpoint를 구현할 수 있다.
- 내 코드에서 발견된 실행 오류 가능성을 수정할 수 있다.

---

# 1. APIRouter가 필요한 이유

Route가 늘어나면 모든 Endpoint를 `api.py` 하나에 작성하기 어렵다.

```text
api.py
├── Application 생성
├── Middleware 설정
└── Router 등록

todo.py
└── Todo 관련 Route

crud.py
└── CRUD 관련 Route
```

`APIRouter`는 관련 Endpoint를 별도 Module로 묶는 도구다.

```python
from fastapi import APIRouter

todo_router = APIRouter()


@todo_router.get('/todos')
def get_todos():
    return []
```

Main Application에서 Router를 등록한다.

```python
from fastapi import FastAPI
from todo import todo_router

app = FastAPI()
app.include_router(todo_router)
```

`include_router()`는 Router에 등록된 Route를 Main Application의 Route 목록에 포함한다.

---

# 2. Router Prefix와 Tag

반복되는 Path는 Router 설정으로 통일할 수 있다.

```python
todo_router = APIRouter(
    prefix='/todos',
    tags=['todos'],
)


@todo_router.get('')
def get_todos():
    return []


@todo_router.get('/{todo_id}')
def get_todo(todo_id: int):
    return {'id': todo_id}
```

```text
최종 Path
GET /todos
GET /todos/{todo_id}
```

`tags`는 자동 생성 API 문서에서 Endpoint를 묶는 데 사용한다.

---

# 3. Middleware

Middleware는 Request가 Endpoint에 도달하기 전과 Response가 Client로 돌아가기 전 사이에서 공통 처리를 수행한다.

```text
Client
  ↓
Middleware 전처리
  ↓
Router / Endpoint
  ↓
Middleware 후처리
  ↓
Client
```

대표 용도는 다음과 같다.

- CORS Header 처리
- 인증과 권한 확인
- 요청·응답 Log
- 처리 시간 측정
- 공통 Header 추가

---

# 4. CORS

CORS는 **Cross-Origin Resource Sharing**이다. Browser가 다른 Origin의 Resource를 요청할 때 Server가 허용 범위를 Response Header로 알려주는 방식이다.

Origin은 다음 세 요소의 조합이다.

```text
Scheme + Host + Port
```

```text
http://127.0.0.1:5500
http://127.0.0.1:8000
```

Port가 다르므로 두 주소는 서로 다른 Origin이다. Browser에서 실행되는 JavaScript가 `5500`에서 `8000`으로 Request를 보내면 CORS 정책의 영향을 받는다.

> “내부적으로 들어가는 것은 괜찮지만 AJAX는 불가”라기보다, CORS는 주로 **Browser가 Script 기반 Cross-Origin Request를 제한하는 보안 정책**이다. Server 간 Request나 주소창 이동과는 적용 방식이 다르다.

## 4.1 수업 코드

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)
```

학습 중에는 편리하지만 운영 환경에서는 Origin과 Method를 필요한 범위로 제한한다.

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://example.com'],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['Content-Type', 'Authorization'],
)
```

---

# 5. Request 객체

FastAPI의 `Request`는 들어온 HTTP Request의 상세 정보에 접근할 때 사용한다.

```python
from fastapi import Request


@app.get('/request-info')
def request_info(request: Request):
    return {
        'method': request.method,
        'path': request.url.path,
        'url': str(request.url),
        'headers': dict(request.headers),
        'cookies': request.cookies,
        'client_host': request.client.host if request.client else None,
        'client_port': request.client.port if request.client else None,
    }
```

| 속성 | 내용 |
| --- | --- |
| `request.method` | GET, POST 등 Method |
| `request.url.path` | URL의 Path |
| `request.url` | 전체 URL 정보 |
| `request.headers` | Request Header |
| `request.cookies` | Cookie |
| `request.query_params` | Query String |
| `request.client` | Client Host와 Port |
| `await request.form()` | Form Data |
| `await request.json()` | JSON Body |

Proxy나 Load Balancer 뒤에서는 `request.client.host`가 실제 사용자 IP가 아니라 Proxy 주소일 수 있다.

---

# 6. Parameter가 들어오는 위치

## 6.1 Path Parameter

Resource를 식별하는 값이 URL Path에 포함된다.

```python
@todo_router.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    return {'id': todo_id}
```

```text
GET /todos/10
```

## 6.2 Query Parameter

Path에 선언되지 않은 함수 인자는 기본적으로 Query Parameter로 처리된다.

```python
@todo_router.get('/todos')
def search_todos(keyword: str = '', page: int = 1):
    return {'keyword': keyword, 'page': page}
```

```text
GET /todos?keyword=python&page=1
```

## 6.3 Form Data

HTML Form에서 전송한 값을 받을 때 사용한다.

```python
from fastapi import Form


@todo_router.post('/todos/form')
def create_todo_form(
    todo_id: int = Form(),
    item: str = Form(),
):
    return {'id': todo_id, 'item': item}
```

`Form()`을 사용하려면 `python-multipart` Package가 필요하다.

## 6.4 JSON Body

Pydantic Model을 함수 인자로 선언하면 JSON Request Body로 처리한다.

```python
@todo_router.post('/todos')
def create_todo(todo: Todo):
    return todo
```

---

# 7. Path와 Query 검증

## 7.1 비교 연산 조건

| 옵션 | 의미 | 조건 |
| --- | --- | --- |
| `gt` | Greater Than | 초과 `>` |
| `ge` | Greater Than or Equal | 이상 `>=` |
| `lt` | Less Than | 미만 `<` |
| `le` | Less Than or Equal | 이하 `<=` |

`lt`의 정확한 표현은 **Less Than**이다. “Little Than”이 아니다.

## 7.2 Path 검증

```python
from typing import Annotated
from fastapi import Path

TodoId = Annotated[int, Path(ge=1, le=10_000)]


@todo_router.get('/todos/{todo_id}')
def get_todo(todo_id: TodoId):
    return {'id': todo_id}
```

## 7.3 Query 검증

```python
from typing import Annotated
from fastapi import Query


@todo_router.get('/todos')
def search_todos(
    keyword: Annotated[str, Query(min_length=2, max_length=30)] = '',
):
    return {'keyword': keyword}
```

경로변수라면 `Path`, Query String이라면 `Query`를 사용한다.

---

# 8. Pydantic과 DTO

Pydantic `BaseModel`은 Data의 Field와 Type, Validation Rule을 선언한다.

```python
from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: int = Field(ge=1, le=10_000)
    item: str = Field(min_length=2, max_length=100)
```

메모의 “data transform object”는 수정이 필요하다. DTO는 **Data Transfer Object**의 약자다.

```text
DTO
→ Layer 또는 System 사이에서 Data를 전달하기 위한 객체
```

Pydantic Model을 DTO나 Request Schema처럼 사용할 수 있지만 Pydantic Model 자체와 DTO가 완전히 같은 개념은 아니다.

또한 “항상 DB Column과 일치시킨다”보다는 목적에 따라 Model을 분리하는 것이 좋다.

```python
class TodoCreate(BaseModel):
    item: str = Field(min_length=2, max_length=100)


class TodoUpdate(BaseModel):
    item: str = Field(min_length=2, max_length=100)


class TodoResponse(BaseModel):
    id: int
    item: str
```

Request에서 허용할 값과 Database Column, Response로 공개할 값은 서로 다를 수 있다.

---

# 9. Validation 오류

Type이나 제한 조건을 만족하지 않으면 FastAPI가 Endpoint 실행 전에 Validation Error Response를 반환한다.

```text
정수 Parameter에 문자열 전달
Path(ge=10)에 5 전달
Field(min_length=2)에 한 글자 전달
```

일반적으로 이런 입력 검증 실패는 `422 Unprocessable Content` Response로 확인할 수 있다.

---

# 10. HTTPException

의도적으로 HTTP Error Response를 만들 때 사용한다.

```python
from fastapi import HTTPException


@todo_router.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    todo = None

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail='Todo를 찾을 수 없습니다.',
        )

    return todo
```

수업 코드의 `/err`는 `403`을 발생시키지만, 단순히 Data를 찾지 못한 경우에는 `404 Not Found`가 의미에 더 적합하다. `403 Forbidden`은 요청 대상은 알지만 권한 때문에 거부할 때 사용한다.

---

# 11. CRUD와 HTTP Method

| CRUD | Database | HTTP Method | REST Endpoint 예시 |
| --- | --- | --- | --- |
| Create | `INSERT` | POST | `POST /todos` |
| Read | `SELECT` | GET | `GET /todos`, `GET /todos/{id}` |
| Update | `UPDATE` | PUT/PATCH | `PUT /todos/{id}` |
| Delete | `DELETE` | DELETE | `DELETE /todos/{id}` |

수업의 `/crud/c`, `/crud/r`, `/crud/u`, `/crud/d`는 CRUD와 Method를 연결해 이해하기 좋은 학습용 Route다. 개선 예제에서는 URI에 동사 대신 Resource를 사용한다.

---

# 12. 내 코드와 강사님 코드 비교

## 12.1 Main Router 등록 순서

```python
# 내 코드
app.include_router(crud_router)
app.include_router(todo_router)
```

```python
# 강사님 코드
app.include_router(todo_router)
app.include_router(crud_router)
```

두 Router의 Method와 Path가 겹치지 않으면 등록 순서에 따른 결과 차이는 없다. 겹치는 Route가 있다면 먼저 등록된 Route가 예상치 못하게 선택될 수 있으므로 Path 중복을 피해야 한다.

## 12.2 Request 처리

내 `todoParam()`은 GET일 때만 `data`를 만든다.

```python
if req.method == 'GET':
    data = req.query_params

id = data.get('id')
```

POST·PUT·DELETE에서는 `data`가 정의되지 않아 `UnboundLocalError`가 발생할 수 있다. 강사님 코드처럼 나머지 Method를 처리해야 한다.

```python
if req.method == 'GET':
    data = req.query_params
else:
    data = await req.form()
```

## 12.3 Pydantic Model Field

내 코드:

```python
class Todo(BaseModel):
    value1: int
    value2: str
```

하지만 Router에서는 `todo.id`를 조회한다.

```python
if todo.id == todo_id:
```

강사님 코드는 `id`, `item`으로 통일되어 있다.

```python
class Todo(BaseModel):
    id: int
    item: str
```

내 Model도 실제 사용 Field에 맞춰 수정해야 한다.

## 12.4 CRUD 입력 방식

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| Create | `Request.form()`에서 직접 추출 | Pydantic Model + `Form()` 또는 JSON |
| Read | Query Parameter 직접 선언 | `Depends()` Model, Path Parameter 예제 |
| Update | Query Parameter | JSON Body Model |
| Delete | Query Parameter, 새 List 구성 | JSON Body Model, `pop()` |
| 저장 형식 | `dict` | Pydantic 객체 |

내 코드는 기본 CRUD Algorithm을 직접 이해하는 데 유리하고, 강사님 코드는 입력 Data를 Model로 묶는 다양한 방식을 보여준다.

---

# 13. 내 코드의 추가 수정 사항

## 13.1 중복 함수 이름

여러 실습 Endpoint에서 `problemGet`을 반복 사용한다. Route 등록 자체는 가능하지만 Debugging과 자동 문서의 Operation ID 관리에 불리하다.

```python
def multiplication_table(): ...
def add_numbers(): ...
def calculate(): ...
```

의도가 드러나는 고유한 이름을 사용한다.

## 13.2 포괄적인 `except`

```python
except:
    return '연산자를 정확히 입력하세요.'
```

모든 예외를 숨기므로 원인 파악이 어렵다.

```python
except (ValueError, IndexError, ZeroDivisionError) as error:
    return {'error': str(error)}
```

## 13.3 Memory 저장소

`todo_list`는 Process Memory에 있으므로 Server 재시작 시 Data가 사라진다. 학습용으로는 적절하지만 실제 Service에서는 Database 또는 영속 저장소가 필요하다.

## 13.4 사용하지 않는 Import

`crud.py`의 `Form`, `TodoItems`처럼 사용하지 않는 Import는 제거한다. Source의 실제 의존성과 가독성이 좋아진다.

---

# 14. 개선된 통합 CRUD 예제

```python
from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status
from pydantic import BaseModel, Field

todo_router = APIRouter(prefix='/todos', tags=['todos'])


class TodoCreate(BaseModel):
    item: str = Field(min_length=2, max_length=100)


class TodoUpdate(BaseModel):
    item: str = Field(min_length=2, max_length=100)


class TodoResponse(BaseModel):
    id: int
    item: str


TodoId = Annotated[int, Path(ge=1)]
todo_list: list[TodoResponse] = []
next_id = 1


@todo_router.post(
    '',
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_todo(data: TodoCreate) -> TodoResponse:
    global next_id

    todo = TodoResponse(id=next_id, item=data.item)
    todo_list.append(todo)
    next_id += 1
    return todo


@todo_router.get('', response_model=list[TodoResponse])
def get_todos() -> list[TodoResponse]:
    return todo_list


@todo_router.get('/{todo_id}', response_model=TodoResponse)
def get_todo(todo_id: TodoId) -> TodoResponse:
    for todo in todo_list:
        if todo.id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail='Todo를 찾을 수 없습니다.')


@todo_router.put('/{todo_id}', response_model=TodoResponse)
def update_todo(todo_id: TodoId, data: TodoUpdate) -> TodoResponse:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            updated = TodoResponse(id=todo_id, item=data.item)
            todo_list[index] = updated
            return updated

    raise HTTPException(status_code=404, detail='Todo를 찾을 수 없습니다.')


@todo_router.delete('/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: TodoId) -> None:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)
            return

    raise HTTPException(status_code=404, detail='Todo를 찾을 수 없습니다.')
```

Main Application:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from todo import todo_router

app = FastAPI(title='Todo API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:5500'],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['Content-Type'],
)

app.include_router(todo_router)
```

---

# 15. MVC Pattern과 FastAPI 구조

MVC는 역할을 다음처럼 분리한다.

```text
Model      → Data와 Business 규칙
View       → 사용자에게 보여 줄 화면
Controller → Request를 받고 처리 흐름 연결
```

API 중심 FastAPI Project는 MVC 이름을 그대로 사용하지 않을 수도 있다.

```text
app/
├── routers/       # HTTP Request와 Response
├── schemas/       # Pydantic Model
├── services/      # Business Logic
├── repositories/  # Database 접근
└── main.py         # Application 생성과 Router 등록
```

핵심은 Folder 이름보다 **관심사와 책임을 분리하는 것**이다.

---

# 16. AJAX와 API Request

AJAX는 Page 전체를 다시 불러오지 않고 JavaScript로 HTTP Request를 보내는 방식이다.

```javascript
const response = await fetch('http://127.0.0.1:8000/todos', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ item: 'FastAPI 복습' }),
});

const data = await response.json();
console.log(data);
```

Frontend가 `5500`, FastAPI가 `8000`에서 실행된다면 CORS 설정이 필요하다.

---

# 17. 자주 하는 실수

| 문제 | 원인 | 해결 |
| --- | --- | --- |
| `422` | Type 또는 Validation 실패 | Request 위치와 Schema 확인 |
| `405` | URL은 있지만 Method 불일치 | Route Decorator와 Client Method 확인 |
| CORS 오류 | 다른 Origin을 Server가 허용하지 않음 | 허용 Origin·Method·Header 설정 |
| `python-multipart` 오류 | Form 처리 Package 미설치 | `pip install python-multipart` |
| `AttributeError` | Model Field와 접근 이름 불일치 | `id`, `item` 등 이름 통일 |
| `UnboundLocalError: data` | 특정 분기에서 변수 미할당 | 모든 Method 분기에서 값 설정 |
| 수정·삭제가 안 됨 | 문자열 ID와 정수 ID 비교 | Type Hint 또는 명시적 변환 |
| 재시작 후 목록 소멸 | Memory List 사용 | 학습용 특성 이해, 이후 DB 연결 |

---

# 18. Debugging 순서

```text
1. Request URL과 HTTP Method 확인
2. Browser Network에서 Request Payload 확인
3. Content-Type 확인
4. Path, Query, Form, JSON 중 Data 위치 확인
5. 422 Response의 detail 확인
6. Terminal Traceback 마지막 줄 확인
7. Router가 include_router()로 등록됐는지 확인
8. Model Field 이름과 실제 접근 이름 비교
9. CORS의 Scheme, Host, Port 비교
10. Memory Data의 현재 상태 출력
```

---

# 19. 종합실습

다음 조건을 만족하는 Todo API를 작성한다.

1. `api.py`, `todo.py`, `model.py`로 파일을 분리한다.
2. `todo_router`에 `/todos` Prefix를 지정한다.
3. Todo 생성, 전체 조회, 상세 조회, 수정, 삭제를 구현한다.
4. `id`는 1 이상만 허용한다.
5. `item`은 2자 이상 100자 이하만 허용한다.
6. 없는 ID를 조회·수정·삭제하면 `404`를 반환한다.
7. 생성 성공 시 `201`, 삭제 성공 시 `204`를 반환한다.
8. `http://127.0.0.1:5500`만 CORS Origin으로 허용한다.
9. Server 재시작 시 Data가 사라지는 이유를 설명한다.

---

# 20. 정답과 해설

핵심 구현은 14절의 통합 CRUD 예제를 사용한다.

```text
api.py
→ FastAPI Application 생성
→ CORS Middleware 설정
→ todo_router 등록

model.py
→ TodoCreate, TodoUpdate, TodoResponse 선언

todo.py
→ /todos CRUD Endpoint
→ Path와 Field Validation
→ HTTPException 처리
```

Memory List는 학습 범위에서 Database 역할을 임시로 대신한다. 따라서 Process가 종료되면 List도 함께 사라진다. 이후 Database 수업과 연결할 때 Repository Layer와 실제 Table로 교체할 수 있다.

---

# 최종 체크리스트

- [ ] `APIRouter`와 `include_router()`의 역할을 설명할 수 있다.
- [ ] Middleware의 Request·Response 처리 위치를 설명할 수 있다.
- [ ] Origin이 Scheme, Host, Port로 구성됨을 설명할 수 있다.
- [ ] CORS가 Browser의 Cross-Origin Request와 관련됨을 설명할 수 있다.
- [ ] `Request`에서 Method, Path, Header, Cookie, Client 정보를 읽을 수 있다.
- [ ] Path, Query, Form, JSON Body를 구분할 수 있다.
- [ ] `gt`, `ge`, `lt`, `le`를 구분할 수 있다.
- [ ] `min_length`, `max_length`로 문자열을 검증할 수 있다.
- [ ] DTO가 Data Transfer Object의 약자임을 설명할 수 있다.
- [ ] Pydantic Model과 Database Model을 목적에 맞게 분리할 수 있다.
- [ ] REST 방식의 CRUD Endpoint를 구현할 수 있다.
- [ ] `404`, `405`, `422`의 원인을 구분할 수 있다.
- [ ] 내 코드의 Model Field 불일치와 Request 분기 오류를 수정할 수 있다.

---

# 핵심 요약

```text
APIRouter = 관련 Endpoint를 Module로 분리
Middleware = Endpoint 전후의 공통 처리
CORS = Browser Cross-Origin Request 허용 정책
Path = Resource 식별값
Query = 조회·검색 조건
Form = HTML Form Data
Pydantic = Type과 Data Validation
DTO = Data Transfer Object
CRUD = POST, GET, PUT/PATCH, DELETE
Memory List = Server 재시작 시 초기화되는 학습용 저장소
```

