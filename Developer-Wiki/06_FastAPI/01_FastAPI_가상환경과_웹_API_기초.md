---
title: FastAPI 가상환경과 웹 API 기초
version: v3.0-final
last_updated: 2026-08-25
status: Completed
---

# FastAPI 가상환경과 웹 API 기초

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `01_FastAPI_가상환경과_웹_API_기초.md` |
| 분류 | `06_FastAPI` |
| 내 코드 | `workspace_python/02_todos/api.py`, `.gitignore`, `pyvenv.cfg`, `requirements.txt` |
| 강사님 코드 | `workspace_teacher/workspace_python/todos/api.py`, `run.cmd`, `pyvenv.cfg`, `requirements.txt` |
| 실행 환경 | Windows, Python 3.14.6, FastAPI 0.141.1, Uvicorn 0.52.1 |
| 핵심 범위 | Library와 Framework, Client와 Server, Port, 가상환경, Package 관리, FastAPI, Uvicorn, Routing, HTTP Method, REST API |
| 제외 범위 | 수업 진행 중인 `02_jinja`와 Template Rendering |
| 문서 형식 | FastAPI Developer-Wiki V2 |

> 이 문서는 완료된 `todos/api.py`와 가상환경 파일을 기준으로 FastAPI 수업의 출발점을 정리한다. `Lib`, `Scripts`, `Include` 내부 파일은 직접 작성한 코드가 아니므로 개별 분석하지 않고, 가상환경에서 맡는 역할만 설명한다.

---

# 학습 목표

- Library와 Framework의 차이를 설명할 수 있다.
- Client, Server, Web Server, Application Server의 역할을 구분할 수 있다.
- Port와 HTTP 기본 Port를 설명할 수 있다.
- `venv`로 독립적인 Python 환경을 만들고 활성화할 수 있다.
- FastAPI와 Uvicorn을 설치하고 서버를 실행할 수 있다.
- `requirements.txt`로 의존성을 기록하고 복원할 수 있다.
- Routing과 HTTP Method의 관계를 이해할 수 있다.
- REST, RESTful, REST API의 차이를 설명할 수 있다.
- 내 코드와 강사님 코드의 실제 차이를 구분할 수 있다.
- 가상환경에서 Git에 포함할 파일과 제외할 파일을 판단할 수 있다.

---

# 1. FastAPI란?

FastAPI는 Python으로 Web API를 만들기 위한 경량 ASGI Web Framework다.

```text
FastAPI
├── URL과 HTTP Method를 함수에 연결
├── Type Hint를 이용한 입력값 검증
├── Pydantic 기반 Data 처리
├── OpenAPI 문서 자동 생성
└── 비동기 함수 지원
```

FastAPI 자체가 Network Server Process를 직접 담당하는 것은 아니다. 실습에서는 ASGI Server인 Uvicorn이 FastAPI Application을 실행한다.

```text
Browser / Client
      ↓ HTTP Request
Uvicorn
      ↓ ASGI
FastAPI Application
      ↓
Response
```

## 1.1 각 구성요소가 실제로 하는 일

```text
Browser
→ 주소창, Form, fetch() 등으로 HTTP Request 생성

Operating System Network
→ IP와 Port를 기준으로 Request 전달

Uvicorn
→ Port 8000에서 연결을 기다리는 ASGI Server
→ HTTP Data를 Python ASGI Message로 변환

FastAPI
→ Method와 Path에 맞는 Route 검색
→ Parameter 추출·검증
→ Endpoint 함수 실행

Pydantic
→ 선언된 Type과 Model에 따라 Data 검증·변환

Starlette/FastAPI Response
→ 반환값을 Status, Header, Body가 있는 HTTP Response로 변환
```

`app = FastAPI()`는 Server를 즉시 여는 명령이 아니다. Route와 Middleware 등을 등록할 Application 객체를 만드는 명령이다. 실제 Port를 열고 Request를 받는 Process는 Uvicorn이다.

## 1.2 하나의 요청이 처리되는 전체 순서

주소창에 다음을 입력했다고 가정한다.

```text
http://127.0.0.1:8000/?name=kim
```

Browser가 만드는 Request의 핵심은 다음과 같다.

```http
GET /?name=kim HTTP/1.1
Host: 127.0.0.1:8000
Accept: text/html,application/json
```

처리 순서:

```text
1. Browser가 127.0.0.1의 8000 Port로 GET Request 전송
2. Uvicorn이 Request 수신
3. FastAPI가 GET / Route 검색
4. Query Parameter name 추출
5. Type과 기본값 검증
6. Endpoint 함수 실행
7. 반환 Dict를 JSON으로 직렬화
8. HTTP Response 전송
9. Browser가 Response Body 표시
```

---

## 1.3 HTTP Request와 Response의 기본 구성

```text
HTTP Request
├── Request Line: Method, Path, Protocol
├── Header: Host, Content-Type, Cookie 등
└── Body: JSON, Form Data, File 등

HTTP Response
├── Status Line: 200, 404, 422 등
├── Header: Content-Type, Set-Cookie 등
└── Body: JSON, HTML, File 등
```

FastAPI 학습에서 Path·Query·Form·JSON·Header·Cookie를 구분하는 이유는 같은 값이라도 HTTP Message의 서로 다른 위치에서 들어오기 때문이다.

---

# 2. Library와 Framework의 차이

## 2.1 Library

Library는 필요한 기능을 개발자가 호출해서 사용하는 Code 모음이다.

```python
import random

number = random.randint(1, 10)
```

Application의 전체 실행 흐름은 개발자가 관리하고, 필요한 순간에 Library를 호출한다.

## 2.2 Framework

Framework는 Application의 기본 구조와 실행 흐름을 제공하고, 개발자가 정해진 위치에 Code를 작성하도록 한다.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Hello World'}
```

Uvicorn과 FastAPI가 Request를 받고 적절한 함수를 호출한다. 이를 흔히 **제어의 역전**이라고 설명한다.

| 구분 | Library | Framework |
| --- | --- | --- |
| 실행 흐름 | 내 Code가 Library를 호출 | Framework가 내 Code를 호출 |
| 주도권 | 개발자 Code | Framework |
| 예 | 표준 Library, Utility Package | FastAPI, Django |

FastAPI는 여러 Library를 내부적으로 활용하는 Framework다. 따라서 “경량 Framework + Library”보다는 **여러 Library 위에 구성된 경량 Web Framework**라고 정리하는 편이 정확하다.

---

# 3. Client와 Server

## 3.1 Client

Client는 Server에 Request를 보내고 Response를 사용하는 주체다.

```text
Web Browser
Mobile App
Frontend JavaScript
API Test Tool
다른 Backend Server
```

## 3.2 Server

Server는 Client의 Request를 받아 처리하고 Response를 제공하는 Program 또는 Computer를 뜻한다.

```text
Client: 무엇을 요청할 것인가?
Server: 요청을 어떻게 처리하고 무엇을 응답할 것인가?
```

“Server는 Client의 요청을 응답해 주는 것”이라는 메모의 방향은 맞다. 더 정확히는 **요청을 수신하고, 필요한 작업을 수행한 뒤, 응답을 반환하는 역할**이다.

---

# 4. Port

Port는 한 Computer에서 실행 중인 여러 Network Program을 구분하는 논리적인 번호다.

```text
127.0.0.1:8000
│         └── Port
└──────────── Host
```

대표적인 기본 Port는 다음과 같다.

| Protocol | 기본 Port |
| --- | ---: |
| HTTP | `80` |
| HTTPS | `443` |

실습에서 `8000`을 사용하는 이유는 개발 Server용으로 흔히 쓰이며 관리자 권한 없이 사용하기 편하기 때문이다. Port 번호가 다르면 Browser 관점에서 Origin도 달라질 수 있다.

## 4.1 Server Port와 Client Port

```text
Browser 127.0.0.1:53124
            ↓ Request
FastAPI 127.0.0.1:8000
```

- `8000`: Uvicorn이 계속 열어 두고 기다리는 Server Port
- `53124`: Browser가 해당 연결에 임시로 사용하는 Client Port

주소창의 `:8000`은 Server가 받을 Port를 지정한다. `request.client.port`에서 확인되는 값은 보통 Browser 측 임시 Port이므로 서로 다르다.

## 4.2 Port를 생략했을 때

```text
http://example.com  → 기본적으로 80
https://example.com → 기본적으로 443
```

`http://127.0.0.1:8000`처럼 기본값이 아닌 Port는 URL에 직접 적어야 한다.

---

# 5. Python 가상환경

## 5.1 필요한 이유

Project마다 필요한 Package와 Version이 다를 수 있다.

```text
Project A → FastAPI 0.x
Project B → 다른 Version 또는 다른 Package
```

가상환경은 Project별 Python 실행 환경과 Package를 분리한다.

## 5.2 수업에서 사용한 생성 방식

```powershell
cd D:\workspace\workspace_python
python -m venv todos
cd todos
Scripts\activate
```

활성화되면 Command Prompt 앞에 환경 이름이 표시된다.

```text
(todos) D:\workspace\workspace_python\todos>
```

## 5.3 권장 구조

수업에서는 `todos` 자체를 가상환경으로 만든 뒤 그 안에 Source를 작성했다. 동작은 가능하지만 Source와 자동 생성 파일이 섞인다.

```text
권장 구조

todos/
├── .venv/
├── api.py
├── 01_router/
├── requirements.txt
└── .gitignore
```

```powershell
mkdir todos
cd todos
python -m venv .venv
.venv\Scripts\activate
```

---

# 6. 가상환경 자동 생성 파일

| 경로 | 역할 | Git 관리 |
| --- | --- | :---: |
| `pyvenv.cfg` | 원본 Python 경로와 Version 등 환경 정보 | 제외 |
| `Scripts/` | Python, pip, 활성화 Script, 실행 파일 | 제외 |
| `Lib/site-packages/` | 설치된 외부 Package | 제외 |
| `Include/` | C 확장용 Header 영역 | 제외 |
| `__pycache__/` | 실행 중 생성되는 Bytecode Cache | 제외 |
| `*.pyc` | Compile된 Python Bytecode | 제외 |
| `requirements.txt` | 환경을 재현할 Package 목록 | 포함 |

`pyvenv.cfg`에는 사용자 PC의 절대 경로가 기록된다. 다른 PC로 가상환경 폴더를 복사하기보다 `requirements.txt`를 이용해 새로 만드는 것이 안전하다.

---

# 7. Package 설치와 환경 재현

## 7.1 설치

```powershell
python -m pip install fastapi uvicorn python-multipart
```

- `fastapi`: Web Framework
- `uvicorn`: ASGI Server
- `python-multipart`: HTML Form Data 처리에 필요

Jinja 수업을 시작한 이후에는 다음 Package도 필요하지만, 이번 문서의 학습 범위에서는 제외한다.

```powershell
python -m pip install jinja2
```

## 7.2 의존성 저장

모든 설치가 끝난 뒤 실행한다.

```powershell
python -m pip freeze > requirements.txt
```

현재 첨부된 `requirements.txt`에는 FastAPI와 Pydantic 등은 있지만, 실제 환경에 설치된 `uvicorn`, `python-multipart`, `jinja2`가 빠져 있다. Package 설치 전이나 중간에 생성한 파일로 보이므로 수업 완료 후 다시 생성해야 한다.

## 7.3 환경 복원

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

---

# 8. 환경변수 PATH 문제

`python`, `pip`, `uvicorn` 명령을 찾지 못한다면 다음을 먼저 확인한다.

```powershell
python --version
python -m pip --version
where python
where pip
```

환경변수에 경로를 추가해야 할 수도 있지만, 무조건 PATH부터 수정하는 것은 권장하지 않는다.

```text
1. Python 설치 여부 확인
2. 가상환경 활성화 여부 확인
3. python -m pip 형태로 실행
4. 그래도 찾지 못할 때 PATH 확인
```

가상환경을 활성화하면 해당 환경의 `Scripts` 경로가 현재 Terminal의 PATH 앞쪽에 임시로 추가된다.

---

# 9. FastAPI 기본 Application

## 9.1 내 코드

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome() -> dict:
    return {
        'message': 'Hello World2'
    }
```

## 9.2 동작 구조

```text
GET /
→ @app.get('/')가 Request와 일치
→ welcome() 실행
→ dict 반환
→ JSON Response 생성
```

FastAPI가 Python `dict`를 JSON Response로 변환한다.

## 9.3 반환값은 Browser에 어떻게 보이는가?

```python
return {'message': 'Hello World2'}
```

FastAPI는 대략 다음과 같은 HTTP Response를 만든다.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"message":"Hello World2"}
```

Python `dict` 자체가 Network로 이동하는 것이 아니다. JSON 문자열로 직렬화된 뒤 Response Body에 들어간다.

반환문이 없으면 Python 함수는 `None`을 반환하고 FastAPI는 이를 JSON `null`로 직렬화한다. 이는 `404`가 아니다. Route는 정상적으로 존재하고 실행되었기 때문이다.

```text
Route 없음                    → 404 Not Found
Route는 있지만 Method 다름   → 405 Method Not Allowed
입력값 검증 실패             → 422 Validation Error
Route 실행 후 None 반환       → 200 OK + null
```

---

# 10. Uvicorn으로 Server 실행

```powershell
uvicorn api:app --port 8000 --reload
```

| 부분 | 의미 |
| --- | --- |
| `api` | `api.py` Module 이름 |
| `app` | `FastAPI()`를 저장한 변수 이름 |
| `--port 8000` | Server가 사용할 Port |
| `--reload` | Source 변경 시 개발 Server 재시작 |

강사님은 다음 `run.cmd`도 사용했다.

```bat
uvicorn api:app --port 8000 --reload
```

명령을 반복해서 입력하는 대신 실행 Script로 관리한 예다.

> `--reload`는 개발 편의 기능이다. 운영 환경 설정으로 그대로 사용하지 않는다.

---

# 11. Routing

Routing은 들어온 Request의 URL과 HTTP Method를 분석해 실행할 함수를 연결하는 과정이다.

```python
@app.get('/html')
def html():
    return '<h1>hello</h1>'

@app.post('/html')
def html2():
    return '<h1>hello2</h1>'
```

```text
GET  /html → html()
POST /html → html2()
```

“사용자가 원하는 것을 파악하는 것”은 Routing의 직관적인 설명이다. 기술적으로는 **HTTP Method와 Path를 기준으로 처리 함수인 Endpoint를 선택하는 것**이다.

같은 Method와 Path를 중복 등록하면 의도와 다른 함수가 먼저 선택될 수 있으므로 중복 Route를 만들지 않는다.

## 11.1 Route는 언제 등록되는가?

Python Module이 Import될 때 Decorator가 실행되어 Route 정보가 Application에 등록된다.

```python
@app.get('/html')
def html():
    return 'hello'
```

등록되는 핵심 정보:

```text
Method   → GET
Path     → /html
Endpoint → html 함수
```

Request가 올 때마다 Decorator가 다시 Route를 만드는 것이 아니다. Application 시작 과정에서 등록된 Route 목록을 Request마다 조회한다.

## 11.2 Router가 판단하는 값

주소 전체가 아니라 주로 Method와 Path가 Route 선택 기준이다.

```text
GET /html?lang=ko
```

```text
Method → GET
Path   → /html
Query  → lang=ko
```

Query String은 보통 Route 선택이 아니라 선택된 Endpoint의 입력값으로 사용된다.

---

# 12. HTTP Method

| Method | 대표 목적 | CRUD |
| --- | --- | --- |
| `GET` | Resource 조회 | Read |
| `POST` | Resource 생성 또는 처리 요청 | Create |
| `PUT` | Resource 전체 교체 | Update |
| `PATCH` | Resource 일부 수정 | Update |
| `DELETE` | Resource 삭제 | Delete |

메모에는 “GET, POST, PUT, PATCH”가 중요하다고 되어 있지만 CRUD를 완성하려면 `DELETE`도 함께 기억해야 한다.

주소창에서 URL을 직접 여는 동작은 일반적으로 GET Request다. POST·PUT·PATCH·DELETE는 HTML Form, JavaScript, API Client 등을 이용한다.

## 12.1 Method는 어디에서 정하는가?

```text
주소창·Link 클릭
→ 일반적으로 GET

<form method="post">
→ POST

fetch(url, {method: 'PUT'})
→ PUT

API Test Tool의 Method 선택
→ 선택한 GET/POST/PUT/PATCH/DELETE
```

Browser 주소창에는 URL만 입력하므로 POST나 DELETE를 직접 지정할 수 없다.

## 12.2 같은 Path, 다른 Method

```python
@app.get('/html')
def show_html():
    return '화면 조회'


@app.post('/html')
def submit_html():
    return '데이터 처리'
```

```text
GET /html  → show_html()
POST /html → submit_html()
```

Path가 같아도 Method가 다르면 서로 다른 Route다.

---

# 13. REST, RESTful, REST API

## 13.1 REST

REST는 Resource를 URI로 표현하고 HTTP의 규칙을 활용하는 Architecture Style이다.

## 13.2 REST API

REST 원칙을 적용해 설계한 HTTP API를 REST API라고 한다.

## 13.3 RESTful

REST 원칙을 비교적 잘 따르는 설계나 System을 RESTful하다고 표현한다.

## 13.4 CRUD URI 비교

동작을 URL에 넣는 방식도 실행되지만, REST 관점에서는 Resource 이름과 HTTP Method를 조합하는 편이 일관적이다.

| 작업 | 동작 중심 URI | REST 방식 예시 |
| --- | --- | --- |
| 생성 | `POST /board/add` | `POST /boards` |
| 목록 조회 | `GET /board` | `GET /boards` |
| 한 건 조회 | `GET /board/read?id=1` | `GET /boards/1` |
| 전체 수정 | `PUT /board/update` | `PUT /boards/1` |
| 일부 수정 | `PATCH /board/update` | `PATCH /boards/1` |
| 삭제 | `DELETE /board/delete` | `DELETE /boards/1` |

```text
URI는 명사형 Resource
동작은 HTTP Method
```

---

# 14. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 | 판단 |
| --- | --- | --- | --- |
| FastAPI 생성 | `app = FastAPI()` | 동일 | 동일 |
| `/` Response | `Hello World2` | 동일 | 동일 |
| `/html` | GET과 POST 분리 | 동일 | 동일 |
| `/no` | 반환문 없음 | 동일 | `null` Response 학습 |
| Server 실행 | Terminal 명령 중심 | `run.cmd` 포함 | 강사님 코드에 반복 실행 Script 추가 |
| 설명 | Method와 Route 동작 Comment 보강 | 핵심 Comment | 내 코드가 실험 기록이 더 많음 |

두 코드의 핵심 실행 결과는 거의 같다. 내 코드는 같은 Path에 서로 다른 Method를 연결하는 이유와 반환값이 없을 때의 동작을 더 자세히 기록했다.

---

# 15. 수정·보완된 통합 예제

```python
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

app = FastAPI(title='Todo API')


@app.get('/')
def welcome() -> dict[str, str]:
    return {'message': 'Hello World'}


@app.get('/html', response_class=HTMLResponse)
def html() -> str:
    return '<h1>Hello</h1>'


@app.post('/messages', status_code=status.HTTP_201_CREATED)
def create_message() -> dict[str, str]:
    return {'message': 'created'}
```

문자열에 HTML Tag가 들어 있다고 해서 항상 HTML Response가 되는 것은 아니다. HTML을 응답하려면 `HTMLResponse`를 명시하는 편이 정확하다.

---

# 16. Docker, VMware, Cloud 기초

## 16.1 Docker와 VMware

| 구분 | Docker Container | VMware Virtual Machine |
| --- | --- | --- |
| 가상화 대상 | OS 수준 | Hardware 수준 |
| Kernel | Host Kernel 공유 | Guest OS별 Kernel |
| 크기·시작 속도 | 비교적 가볍고 빠름 | 비교적 무겁고 느림 |
| 격리 | Process 중심 | OS 단위 |
| 용도 | 배포 환경 표준화, Service 격리 | 완전한 OS 환경, 강한 독립성 |

`venv`는 Python Package 환경만 분리한다. Docker처럼 OS 수준으로 Application을 격리하지 않는다.

```text
venv   → Python 실행 환경과 Package 분리
Docker → Application과 실행 환경을 Container로 격리
VM     → Guest OS 전체를 가상화
```

## 16.2 AWS와 Azure

AWS와 Azure는 Server, Database, Storage, Network, Container 등 다양한 자원을 제공하는 Cloud Platform이다. FastAPI Application은 이후 VM, Container Service 또는 Platform Service에 배포할 수 있다.

---

# 17. MVC와 WYSIWYG 메모

- **MVC**: Application을 Model, View, Controller 역할로 나누는 Architecture Pattern이다. API 중심 FastAPI Project에서는 Router, Service, Repository, Schema 등으로 책임을 분리하는 구조도 많이 사용한다.
- **WYSIWYG**: “What You See Is What You Get”의 약자로, 편집 화면에서 보이는 모습과 최종 결과가 유사한 편집 방식을 뜻한다. FastAPI 핵심 개념은 아니며 Web Editor나 CMS를 다룰 때 연결되는 용어다.

---

# 18. 자주 하는 실수

## 18.1 가상환경 활성화 없이 설치

```text
문제: Package가 Global Python에 설치됨
확인: where python, python -m pip --version
해결: 가상환경을 활성화한 뒤 설치
```

## 18.2 Package 설치 전에 `pip freeze`

```text
문제: requirements.txt에 필요한 Package가 누락됨
해결: 설치 완료 후 다시 생성
```

## 18.3 `uvicorn` 명령을 찾지 못함

```powershell
python -m uvicorn api:app --port 8000 --reload
```

Module 실행 방식은 PATH 문제를 줄이는 데 도움이 된다.

## 18.4 Source와 가상환경을 함께 Commit

`Lib`, `Scripts`, `Include`, `pyvenv.cfg`는 다른 환경에서 재생성할 파일이다. 저장소에는 Source와 `requirements.txt`를 중심으로 관리한다.

---

## 18.5 수업 원본에서 다시 찾기

| 배운 개념 | 내 코드 위치 | 강사님 코드 위치 | 무엇을 확인하는가 |
| --- | --- | --- | --- |
| FastAPI Application | `02_todos/api.py`의 `app = FastAPI()` | `todos/api.py` | Application 객체 생성 |
| GET `/` | `02_todos/api.py`의 `welcome()` | `todos/api.py`의 `welcome()` | Dict가 JSON Response가 되는 과정 |
| 같은 Path, 다른 Method | `02_todos/api.py`의 두 `/html` Route | `todos/api.py`의 두 `/html` Route | GET과 POST가 별도 Route인 이유 |
| 반환문 없음 | `02_todos/api.py`의 `no()` | `todos/api.py`의 `no()` | Python `None`이 JSON `null`이 되는 결과 |
| 가상환경 설정 | `02_todos/pyvenv.cfg` | `todos/pyvenv.cfg` | Python Version과 절대 경로 |
| 설치 Package 기록 | `02_todos/requirements.txt` | `todos/requirements.txt` | 환경 재현에 필요한 Package 목록 |
| 반복 실행 명령 | Terminal에서 Uvicorn 실행 | `todos/run.cmd` | `api:app`, Port, Reload 의미 |

이 표는 개념을 잊었을 때 실제 수업 Source로 돌아가기 위한 Index다. 먼저 문서 설명을 읽고 해당 함수를 직접 실행해 결과를 다시 확인한다.

---

## 18.6 직접 재현하기

```powershell
cd D:\workspace\workspace_python\02_todos
Scripts\activate
python -m uvicorn api:app --port 8000 --reload
```

확인 순서:

```text
1. Browser에서 http://127.0.0.1:8000/ 열기
2. JSON message 확인
3. 주소창에서 /html 열어 GET 결과 확인
4. 주소창으로 POST를 보낼 수 없는 이유 확인
5. /no에서 null과 200 Status 확인
6. 존재하지 않는 /unknown에서 404 비교
```

---

# 19. Debugging 순서

```text
1. 가상환경 활성화 표시 확인
2. python --version 확인
3. python -m pip show fastapi 확인
4. 현재 Directory와 api.py 확인
5. uvicorn의 module:variable 이름 확인
6. Port 충돌 확인
7. Terminal Traceback의 마지막 예외 확인
8. Browser Network 또는 API Response 확인
```

---

# 20. 종합실습

다음 요구사항을 만족하는 기본 API를 작성한다.

1. `.venv` 가상환경을 생성한다.
2. FastAPI와 Uvicorn을 설치한다.
3. `GET /`에서 `{"message": "Todo API"}`를 반환한다.
4. `GET /health`에서 Server 상태를 반환한다.
5. `POST /boards`에서 생성 완료 Message를 반환한다.
6. Uvicorn을 Port `8000`에서 `--reload`로 실행한다.
7. 설치 Package를 `requirements.txt`에 저장한다.
8. `.venv`, `__pycache__`, `*.pyc`를 `.gitignore`에 추가한다.

---

# 21. 정답과 해설

```python
from fastapi import FastAPI, status

app = FastAPI(title='Todo API')


@app.get('/')
def root() -> dict[str, str]:
    return {'message': 'Todo API'}


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@app.post('/boards', status_code=status.HTTP_201_CREATED)
def create_board() -> dict[str, str]:
    return {'message': 'created'}
```

```gitignore
.venv/
venv/
__pycache__/
*.py[cod]
```

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install fastapi uvicorn
python -m uvicorn api:app --port 8000 --reload
python -m pip freeze > requirements.txt
```

---

# 최종 체크리스트

- [ ] Library와 Framework의 제어 흐름 차이를 설명할 수 있다.
- [ ] Client와 Server의 역할을 설명할 수 있다.
- [ ] Port `80`, `443`, 실습 Port `8000`을 구분할 수 있다.
- [ ] `venv`를 생성하고 활성화할 수 있다.
- [ ] 가상환경 자동 생성 파일을 Git에서 제외할 수 있다.
- [ ] `requirements.txt`를 생성하고 복원할 수 있다.
- [ ] FastAPI와 Uvicorn의 역할을 구분할 수 있다.
- [ ] Routing을 Method와 Path의 연결로 설명할 수 있다.
- [ ] GET, POST, PUT, PATCH, DELETE의 목적을 구분할 수 있다.
- [ ] REST, RESTful, REST API를 구분할 수 있다.
- [ ] Resource 중심 URI를 설계할 수 있다.

---

# 핵심 요약

```text
FastAPI = Python Web API Framework
Uvicorn = FastAPI Application을 실행하는 ASGI Server
venv = Project별 Python Package 환경 분리
requirements.txt = 환경 재현을 위한 의존성 목록
Routing = HTTP Method + Path를 Endpoint에 연결
REST = Resource 중심 URI + HTTP 규칙 활용
Source는 Commit, 가상환경은 재생성
```
