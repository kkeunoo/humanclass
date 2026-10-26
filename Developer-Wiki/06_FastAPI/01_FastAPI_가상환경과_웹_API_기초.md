# 01. 첫 FastAPI — 경로와 요청 방식

[FastAPI 목차](README.md) · [다음: 라우터와 입력값](02_FastAPI_Router_Request_Pydantic_CRUD.md)

강사님과 내 첫 `api.py`는 `FastAPI()` 앱을 만들고 **주소(`/`)와 요청 방식(GET)**을 함수에 연결한다. 가상환경은 실행 준비이지만 양쪽 Python 원본 안에 독립적인 가상환경 구현은 없다. 이 장의 본문은 실제 앱 코드부터 읽는다.

## 1. 주소 하나에 함수 하나 연결

### 강사님 코드

출처: `teacher/workspace_python/todos/api.py` 1–10행 · **원본 발췌**

```python
from fastapi import FastAPI

app = FastAPI()
# app2 = FastAPI()

@app.get('/')
def welcome() -> dict :
    return {
        "message": "Hello World2"
    }
```

### 내 코드

출처: `me/workspace_python/02_todos/api.py` 1–9행 · **원본 발췌**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome() -> dict:
    return {
        "message" : "Hello World2"
    }
```

`app = FastAPI()`는 앱 객체를 만들고, `@app.get('/')`는 **GET /** 요청이 오면 아래 `welcome()`을 실행하도록 등록한다. 함수가 딕셔너리를 반환하므로 브라우저에는 JSON 형태의 `message`가 보인다. `-> dict`는 Python의 **반환형 표시**이고, 사용자가 배우지 않았다고 확인한 `response_model` 설정과 같지 않다.

## 2. 같은 주소, 다른 요청 방식

### 강사님 코드

출처: `teacher/workspace_python/todos/api.py` 12–27행 · **원본 발췌**

```python
# 주소와 방식이 같은 게 있다면 먼저 선언한 것만 실행된다
@app.get('/html')
def html() :
    return "<h1>hello</h1>"

# @app.get('/html')
# def html2() :
#     return "<h1>hello2</h1>"
@app.post('/html')
def html2() :
    return "<h1>hello2</h1>"

@app.get('/no')
def no() :
    print('들어왔음')
# return 이 없으면 null을 돌려준다(fastAPI 한정)
```

### 내 코드

출처: `me/workspace_python/02_todos/api.py` 11–30행 · **원본 발췌**

```python
# post일 때 127.0.0.1:60114 - "GET /html HTTP/1.1" 405 Method Not Allowed 발생
# 주소창에 기존에 배운 form과 ajax 빼고는 post로 보낼 수 없음
# 원래 위와 같으면 에러가 나야하는데, 동작은 됨
# 다만, 주소와 방식이 같은것이 있다면 먼저 선언한 것만 실행된다
# 아래처럼 get, post 방식이 다르면 동작이 가능하며 주소 1개로 4개방식을 사용 가능
@app.get("/html")
def html():
    return "<h1>hello</h1>"
# @app.get("/html")
# def html2():
#     return "<h1>hello2</h1>"
@app.post("/html")
def html2():
    return "<h1>hello2</h1>"


# 원래 return이 없어 404에러가 떠야 하지만, fastapi 한정으로 null로 응답해줌
@app.get("/no")
def no():
    print('들어왔음')
```

`GET /html`과 `POST /html`은 **주소는 같아도 방식이 달라** 서로 다른 함수에 연결된다. 주소창으로 이동하면 보통 GET이므로 POST 전용 함수만 있다면 그 방식으로는 호출되지 않는다. 문자열 `"<h1>hello</h1>"`을 그냥 반환한 것은 **HTML 문서 응답으로 렌더링한 예제가 아니다**. 화면에 실제 제목 태그를 만들려면 적절한 HTML 응답 방식이 필요하며, 이 점은 [04 응답과 리다이렉트](04_FastAPI_Response_Redirect_의존성주입.md)의 추가 설명으로 둔다.

`/no` 함수에는 `return`이 없다. Python에서는 암묵적으로 `None`을 반환하고, 이 간단한 FastAPI 예제에서는 JSON `null` 응답으로 직렬화된다. 내 주석의 “원래 404가 떠야 한다”는 틀리다. 경로는 이미 등록되어 있어서 **404가 아니라 정상 경로**다.

## 직접 확인할 질문

1. `GET /` 요청에서 실행되는 함수는 무엇인가?
2. `GET /html`과 `POST /html`은 왜 다른 함수에 갈 수 있는가?
3. `return` 없는 `/no`를 404라고 설명하면 왜 틀린가?

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/01_FastAPI_가상환경과_웹_API_기초_연습문제.md)

## 추가로 알면 좋은 것

**개인 학습 메모 — 원본 코드 발췌 아님.** 첨부 메모에는 Windows에서 `python -m venv todos`로 가상환경을 만들고 활성화한 뒤 FastAPI와 Uvicorn을 설치해 `uvicorn api:app --port 8000 --reload`로 실행한 흐름이 적혀 있다. `api:app`의 앞부분은 Python 파일 이름, 뒷부분은 그 파일의 앱 변수 이름이다. 이 순서는 앱 코드의 동작 원리와 별개인 **실행 준비 기록**이다. 메모의 명령을 현재 환경의 설치 보증으로 읽지 않는다.

HTML 전용 응답 클래스와 배포 설정의 세부 사용법은 이 첫 원본 코드에 직접 구현되지 않았다. 이 장에서는 **앱·경로·방식·반환**을 먼저 익힌다.
