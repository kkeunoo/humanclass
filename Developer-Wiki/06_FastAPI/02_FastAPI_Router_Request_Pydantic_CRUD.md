---
title: FastAPI Router, Request, Pydantic과 CRUD
version: v3.0-final
last_updated: 2026-08-25
status: Completed
---

# FastAPI Router, Request, Pydantic과 CRUD

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `02_FastAPI_Router_Request_Pydantic_CRUD.md` |
| 분류 | `06_FastAPI` |
| 내 코드 | `workspace_python/02_todos/01_router/api.py`, `todo.py`, `model.py`, `crud.py`, `ajax.html`, CRUD 연습 파일 |
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

## 1.1 Import부터 Request 처리까지

```text
Uvicorn이 api Module Import
→ api.py에서 todo.py Import
→ todo.py의 Decorator가 todo_router에 Route 등록
→ api.py의 include_router()가 Main app에 Route 복사·포함
→ Server 시작 완료
→ Client Request 도착
→ Main app의 전체 Route 목록에서 일치 항목 검색
```

따라서 `todo.py` 파일이 존재하기만 해서는 Route가 Main Application에 연결되지 않는다. Import와 `include_router()`가 모두 필요하다.

```text
404가 발생할 때 확인
1. Router 파일이 Import되었는가?
2. Decorator가 APIRouter 객체에 붙었는가?
3. app.include_router()가 실행되었는가?
4. Prefix를 포함한 최종 Path가 맞는가?
```

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

## 3.1 Middleware가 받는 정보

Middleware는 Endpoint가 받는 것과 같은 Request 흐름을 더 바깥에서 감싼다.

```text
Request Method·Path·Header·Cookie
→ Middleware에서 확인 또는 변경
→ Endpoint로 전달
→ Endpoint Response
→ Middleware에서 Header 추가·시간 측정
→ Client 전송
```

예를 들어 처리 시간을 측정하면:

```python
import time
from fastapi import Request


@app.middleware('http')
async def add_process_time(request: Request, call_next):
    started = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - started
    response.headers['X-Process-Time'] = str(elapsed)
    return response
```

`call_next(request)`가 다음 Middleware 또는 Endpoint로 Request를 넘기는 지점이다.

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

## 4.1 Origin은 어디서 오는가?

Frontend가 다음 Page에서 실행된다고 가정한다.

```text
http://127.0.0.1:5500/index.html
```

JavaScript가 다음 API를 호출한다.

```text
http://127.0.0.1:8000/todos
```

Browser가 Request에 Origin Header를 넣는다.

```http
Origin: http://127.0.0.1:5500
```

FastAPI의 CORS Middleware는 이 값이 `allow_origins`에 허용됐는지 확인하고 Response에 허용 Header를 추가한다.

```http
Access-Control-Allow-Origin: http://127.0.0.1:5500
```

Browser는 Response Header를 검사한 뒤 JavaScript가 Response를 읽게 할지 차단할지 결정한다. Request가 Server에 전혀 도달하지 않았다는 뜻과는 다를 수 있다.

## 4.2 Preflight Request

일부 Cross-Origin Request 전에 Browser가 OPTIONS Request로 허용 여부를 미리 확인한다.

```http
OPTIONS /todos HTTP/1.1
Origin: http://127.0.0.1:5500
Access-Control-Request-Method: PUT
Access-Control-Request-Headers: content-type
```

이를 Preflight Request라고 한다. CORS Middleware가 OPTIONS에 적절히 응답하므로 일반적으로 별도 Endpoint를 만들 필요가 없다.

## 4.3 수업 코드

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

## 5.1 Request란?

`Request`는 Browser, JavaScript, Mobile App, API Client 또는 다른 Server가 FastAPI Server로 보낸 **HTTP Request 전체 정보에 접근하는 객체**다.

```text
사용자가 Browser 주소창에 URL 입력
또는 HTML Form 제출
또는 JavaScript fetch() 실행
        ↓
Client가 HTTP Request 생성
        ↓
Network를 통해 Uvicorn에 도착
        ↓
Uvicorn이 ASGI 형식으로 FastAPI에 전달
        ↓
FastAPI/Starlette가 Request 객체로 제공
        ↓
Router가 Method와 Path를 비교해 Endpoint 실행
```

FastAPI의 `Request`는 내부적으로 Starlette가 제공하는 Request 객체다. HTTP Method, URL, Header, Cookie, Client 주소와 Body 등에 접근할 수 있다.

```python
from fastapi import Request


@app.get('/request-info')
def request_info(request: Request):
    return {'method': request.method}
```

Parameter 이름은 꼭 `request`일 필요는 없지만 Type을 `Request`로 선언해야 FastAPI가 현재 요청 객체를 전달한다.

```python
def request_info(req: Request):
    return {'method': req.method}
```

---

## 5.2 주소창 URL은 어떻게 들어오는가?

Browser 주소창에 다음 URL을 입력했다고 가정한다.

```text
http://127.0.0.1:8000/todos/10?keyword=python&page=2#result
```

각 부분은 다음처럼 구분된다.

| URL 부분 | 이름 | Request에서 확인 |
| --- | --- | --- |
| `http` | Scheme | `request.url.scheme` |
| `127.0.0.1` | Host | `request.url.hostname` |
| `8000` | Port | `request.url.port` |
| `/todos/10` | Path | `request.url.path` |
| `10` | Path Parameter | `request.path_params['todo_id']` |
| `keyword=python&page=2` | Query String | `request.query_params` |
| `#result` | Fragment | Server로 전송되지 않음 |

주소창에서 URL을 직접 열면 Browser는 일반적으로 GET Request를 보낸다.

```http
GET /todos/10?keyword=python&page=2 HTTP/1.1
Host: 127.0.0.1:8000
```

`#result` 같은 Fragment는 Browser 화면 내부 위치를 나타내며 HTTP Request에 포함되지 않는다. 따라서 FastAPI의 `Request`에서는 읽을 수 없다.

---

## 5.3 Path와 Path Parameter

Route가 다음과 같다면:

```python
@app.get('/todos/{todo_id}')
def get_todo(todo_id: int, request: Request):
    return {
        'path': request.url.path,
        'path_params': request.path_params,
        'todo_id': todo_id,
    }
```

다음 주소로 요청했을 때:

```text
http://127.0.0.1:8000/todos/10
```

FastAPI는 `/todos/{todo_id}`와 `/todos/10`을 비교해 `10`을 Path Parameter로 추출한다.

```text
request.url.path
→ /todos/10

request.path_params
→ {'todo_id': '10'}

함수 인자 todo_id: int
→ 10
```

`request.path_params`의 원본 값은 문자열 기반이지만, 함수 인자로 `todo_id: int`를 선언하면 FastAPI가 검증·변환한다. 일반적으로 직접 Dictionary를 읽는 방식보다 함수 인자로 선언하는 방식을 권장한다.

---

## 5.4 Query String

주소창에서 `?` 뒤에 붙는 값이 Query String이다.

```text
http://127.0.0.1:8000/todos?keyword=python&page=2
```

```python
@app.get('/todos')
def get_todos(request: Request):
    keyword = request.query_params.get('keyword')
    page = request.query_params.get('page')
    return {'keyword': keyword, 'page': page}
```

```text
request.query_params
→ QueryParams('keyword=python&page=2')

request.query_params.get('keyword')
→ 'python'

request.query_params.get('page')
→ '2'
```

직접 읽은 Query 값은 기본적으로 문자열이다. FastAPI 함수 인자로 선언하면 Type 검증을 받을 수 있다.

```python
@app.get('/todos')
def get_todos(keyword: str = '', page: int = 1):
    return {'keyword': keyword, 'page': page}
```

```text
?page=abc
→ int 변환 실패
→ 422 Validation Error
```

---

## 5.5 HTTP Method

```python
request.method
```

Client가 보낸 Method를 문자열로 확인한다.

```text
GET
POST
PUT
PATCH
DELETE
```

```python
@app.api_route('/method', methods=['GET', 'POST'])
def method(request: Request):
    return {'method': request.method}
```

일반적으로는 하나의 함수에서 Method를 분기하기보다 `@app.get`, `@app.post`처럼 Route를 분리하는 것이 읽기 쉽고 자동 문서에도 명확하다.

---

## 5.6 Header는 어디서 들어오는가?

Header는 Client와 Server가 Request에 대한 부가 정보를 전달하는 영역이다. Browser가 자동으로 넣는 Header도 있고 JavaScript나 API Client가 직접 추가하는 Header도 있다.

```http
GET /todos HTTP/1.1
Host: 127.0.0.1:8000
User-Agent: Mozilla/5.0 ...
Accept: text/html
Cookie: session_id=abc123
```

```python
@app.get('/headers')
def headers(request: Request):
    return {
        'user_agent': request.headers.get('user-agent'),
        'accept': request.headers.get('accept'),
        'content_type': request.headers.get('content-type'),
    }
```

대표 Header:

| Header | 역할 |
| --- | --- |
| `Host` | 요청 대상 Host와 Port |
| `User-Agent` | Browser·Client 정보 |
| `Accept` | Client가 받고 싶은 응답 형식 |
| `Content-Type` | Request Body의 Data 형식 |
| `Authorization` | 인증 정보 |
| `Cookie` | Browser가 저장했다가 함께 보내는 Cookie |
| `Origin` | CORS 판단에 사용하는 요청 Origin |

Header 이름은 대소문자를 구분하지 않는다. Password나 Token 같은 민감한 Header 전체를 Log에 출력하지 않는다.

---

## 5.7 Cookie는 어디서 들어오는가?

Server가 이전 Response에서 Cookie를 설정하면 Browser가 저장하고, 조건이 맞는 다음 Request의 `Cookie` Header에 포함한다.

```text
Server Response
Set-Cookie: session_id=abc123
        ↓
Browser 저장
        ↓
다음 Request
Cookie: session_id=abc123
```

```python
@app.get('/cookies')
def cookies(request: Request):
    session_id = request.cookies.get('session_id')
    return {'session_id': session_id}
```

Cookie는 Client가 보내는 값이므로 변조 가능성을 고려해야 한다. 중요한 값은 서명하거나 Server Session과 연결해 검증한다.

---

## 5.8 Request Body는 어디서 들어오는가?

Body는 주소창 URL이 아니라 Form 제출, JavaScript `fetch`, Mobile App 또는 API Client가 보내는 본문 Data다.

### JSON Body

```javascript
fetch('http://127.0.0.1:8000/todos', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({id: 1, item: 'FastAPI 공부'})
});
```

```python
@app.post('/todos/raw-json')
async def raw_json(request: Request):
    data = await request.json()
    return data
```

권장 방식은 Pydantic Model을 직접 선언하는 것이다.

```python
@app.post('/todos')
def create_todo(todo: Todo):
    return todo
```

### HTML Form Body

```html
<form method="post" action="/todos/form">
    <input type="text" name="id">
    <input type="text" name="item">
    <button type="submit">전송</button>
</form>
```

```python
@app.post('/todos/raw-form')
async def raw_form(request: Request):
    data = await request.form()
    return {
        'id': data.get('id'),
        'item': data.get('item'),
    }
```

함수 Parameter에 `Form()`을 선언하는 방식이 검증과 문서화에 유리하다.

```python
@app.post('/todos/form')
def create_form(
    todo_id: int = Form(),
    item: str = Form(min_length=1),
):
    return {'id': todo_id, 'item': item}
```

| 전송 방식 | 일반적인 `Content-Type` | 읽는 방법 |
| --- | --- | --- |
| JSON | `application/json` | Pydantic Model, `await request.json()` |
| HTML Form | `application/x-www-form-urlencoded` | `Form()`, `await request.form()` |
| 파일 Form | `multipart/form-data` | `UploadFile`, `Form()` |

---

## 5.9 Client IP와 Port

```python
@app.get('/client')
def client(request: Request):
    if request.client is None:
        return {'host': None, 'port': None}

    return {
        'host': request.client.host,
        'port': request.client.port,
    }
```

```text
request.client.host
→ Request를 FastAPI에 연결한 상대 Host

request.client.port
→ 해당 연결에서 Client가 사용한 임시 Port
```

Client Port는 사용자가 접속한 Server Port `8000`과 다르다.

```text
Client 127.0.0.1:52341
             ↓
Server 127.0.0.1:8000
```

Proxy, Load Balancer 또는 Container 뒤에서는 `request.client.host`가 실제 사용자 IP가 아니라 바로 앞 Proxy의 IP일 수 있다. 전달 Header를 신뢰하려면 신뢰할 Proxy 설정이 함께 필요하다.

---

## 5.10 Request에서 자주 확인하는 정보

```python
from fastapi import Request


@app.get('/request-info')
def request_info(request: Request):
    return {
        'method': request.method,
        'path': request.url.path,
        'url': str(request.url),
        'query': dict(request.query_params),
        'path_params': request.path_params,
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
| `request.path_params` | Router가 추출한 Path Parameter |
| `request.client` | Client Host와 Port |
| `request.state` | Middleware와 Endpoint 사이에서 공유할 요청별 값 |
| `await request.form()` | Form Data |
| `await request.json()` | JSON Body |
| `await request.body()` | 가공하지 않은 Raw Body Byte |

---

## 5.11 Request를 직접 읽을 때와 함수 인자로 받을 때

둘 다 가능하지만 목적이 다르다.

```python
# Request를 직접 읽기
@app.get('/search/raw')
def search_raw(request: Request):
    page = request.query_params.get('page')
```

```python
# FastAPI Parameter 선언
@app.get('/search')
def search(page: int = 1):
    return {'page': page}
```

| 방식 | 장점 | 적합한 경우 |
| --- | --- | --- |
| `Request` 직접 접근 | HTTP Request 전체를 자유롭게 확인 | Header, Cookie, Client, Raw Body, Middleware 정보 |
| 함수 Parameter 선언 | Type 변환, 검증, OpenAPI 문서 자동화 | Path, Query, Form, JSON 입력값 |

업무 Data는 함수 Parameter와 Pydantic Model로 받고, HTTP Request 자체의 상세 정보가 필요할 때 `Request`를 함께 사용하는 것이 좋다.

---

## 5.12 한 Request를 전체적으로 읽는 예제

요청 URL:

```text
POST http://127.0.0.1:8000/todos/10?mode=edit
```

JSON Body:

```json
{
  "item": "FastAPI Request 공부"
}
```

Endpoint:

```python
from fastapi import Request


@app.post('/todos/{todo_id}')
async def inspect_request(todo_id: int, request: Request):
    body = await request.json()

    return {
        'method': request.method,
        'scheme': request.url.scheme,
        'host': request.url.hostname,
        'port': request.url.port,
        'path': request.url.path,
        'todo_id': todo_id,
        'query': dict(request.query_params),
        'content_type': request.headers.get('content-type'),
        'cookies': request.cookies,
        'body': body,
    }
```

```text
주소창·요청 URL
├── /todos/10 → Path와 todo_id
└── ?mode=edit → Query Parameter

HTTP Header
└── Content-Type, Cookie, Authorization 등

HTTP Body
└── JSON의 item
```

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

## 8.1 JSON이 Model로 들어오는 과정

Client가 보내는 Body:

```json
{
  "id": 10,
  "item": "FastAPI 공부"
}
```

```python
@app.post('/todos')
def create_todo(todo: Todo):
    return todo
```

```text
Content-Type: application/json 확인
→ Request Body Byte 읽기
→ JSON을 Python Dict로 변환
→ Todo Model의 Field 이름 비교
→ id를 int로 검증
→ item을 str·길이 규칙으로 검증
→ 성공하면 Todo 객체를 함수에 전달
→ 실패하면 함수 실행 전 422 응답
```

Endpoint 안에서 `print(todo)`가 실행되지 않았다면 검증 단계에서 먼저 실패했을 가능성이 있다.

## 8.2 Model과 Request 객체의 차이

```text
Request
→ Method, URL, Header, Cookie, Body 등 HTTP 전체 정보

Pydantic Model
→ Body 중 업무에 필요한 Data의 구조와 검증 결과
```

둘을 동시에 받을 수도 있다.

```python
@app.post('/todos')
def create_todo(todo: Todo, request: Request):
    return {
        'client': request.client.host if request.client else None,
        'todo': todo,
    }
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

## 9.1 422 detail 읽기

```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["query", "id"],
      "msg": "Input should be a valid integer",
      "input": "abc"
    }
  ]
}
```

| Field | 의미 |
| --- | --- |
| `type` | 검증 실패 종류 |
| `loc` | 값이 들어온 위치와 이름 |
| `msg` | 오류 설명 |
| `input` | 실제 입력값 |

`loc`의 첫 값으로 `path`, `query`, `body` 등을 확인하면 어디에서 잘못 들어왔는지 빠르게 찾을 수 있다.

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

## 18.1 수업 원본에서 다시 찾기

| 배운 개념 | 내 코드 파일·위치 | 강사님 코드 파일·위치 | 다시 확인할 내용 |
| --- | --- | --- | --- |
| Main Application | `01_router/api.py` | `01_router/api.py` | `FastAPI()`와 Router 등록 |
| CORS Middleware | `01_router/api.py`의 `app.add_middleware()` | 같은 위치 | Origin·Method·Header 허용 |
| Request Client | `01_router/api.py`의 `/ip` | 같은 Route | `request.client.host`, Port |
| HTTPException | `01_router/api.py`의 `/err` | 강사님 원본에는 없음 | 의도적인 Error Response |
| APIRouter | `01_router/todo.py` | 같은 파일 | `todo_router = APIRouter()` |
| Query Parameter | `todoParamGet()` | `todoParamGet()` | 주소창 `?id=...&item=...` |
| Form Data | `todoParamPost()` | `todoParamPost()` | HTML Form `name`과 `Form()` |
| Raw Request 분기 | `todoParam()` | `todoParam()` | GET Query와 그 외 Form 처리 차이 |
| JSON Body | `add_todo()` | `add_todo()` | JSON Dict가 함수 인자로 들어오는 과정 |
| Pydantic Model | `model.py` | `model.py` | Field 이름과 Type 검증 |
| Path 검증 | `get_single_todo2()`, `get_single_todo3()` | 같은 함수 | `Path`, `Annotated`, `ge`, `gt`, `le` |
| Query 검증 | `todo4()` | `todo4()` | `Query(gt=0, lt=10000)` |
| CRUD | `crud.py`의 `todoC/R/U/D()` | `crud.py`의 Form·AJAX CRUD | Create·Read·Update·Delete 흐름 |
| Browser AJAX | `ajax.html` | `ajax.html` | JSON·Query Request를 Browser가 만드는 방법 |

## 18.2 Request를 직접 재현하는 주소

```text
GET 기본
http://127.0.0.1:8000/

Client 정보
http://127.0.0.1:8000/ip

Query Parameter
http://127.0.0.1:8000/todo/param?id=10&item=study

Path Parameter
http://127.0.0.1:8000/todo/10

Path 검증 실패
http://127.0.0.1:8000/todo2/5

Query 검증 실패
http://127.0.0.1:8000/todo4?id=10000
```

각 Request에서 다음 세 곳을 함께 확인한다.

```text
Browser 주소창·화면
→ 어떤 URL을 요청했고 무엇을 받았는가?

Browser 개발자 도구 Network
→ Method, Status, Header, Query, Response는 무엇인가?

Uvicorn Terminal
→ 어떤 Endpoint의 print가 실행되고 어떤 Log가 남는가?
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
