# 04. 함수 호출과 리다이렉트 — 요청이 몇 번 일어날까

[FastAPI 목차](README.md) · [이전: Jinja](03_FastAPI_Jinja2_템플릿.md) · [다음: 화면 Todo](05_FastAPI_Jinja_Todo_CRUD.md)

두 원본은 `/step1`을 다른 함수에서 **직접 호출**하는 경우와 브라우저에 **리다이렉트 응답**을 보내는 경우를 비교한다. 기존 제목의 “의존성 주입”은 이 파일의 본문 구현이 아니므로 해당 개념은 실제 DB 세션 코드에서 다룬다.

## 1. 함수 직접 호출은 새 HTTP 요청이 아니다

### 강사님 코드

출처: `teacher/workspace_python/todos/03_response/api.py` 5–23행 · **원본 발췌**

```python
@app.get('/step1')
def step1(request:Request) :
    print('/step1 실행')
    data = request.query_params
    item = data.get('item')
    print(f'item: {item}')

    print('너무 복잡하고 정교해서 복붙하긴 좀 그런 곳')

@app.get('/step2')
def step2(request:Request) :
    print('/step2 실행')
    data = request.query_params
    item = data.get('item')
    print(f'item:{item} 관련 일 처리는 끝났고')

    print('step1으로 이동')
    # 1. forward 방식
    step1(request)
```

### 내 코드

출처: `me/workspace_python/02_todos/03_response/api.py` 5–23행 · **원본 발췌**

```python
@app.get('/step1')
def step1(request : Request) :
    print('/step1 실행')
    data = request.query_params
    item = data.get('item')
    print(f'item : {item}')

    print('너무 복잡하고 정교해서 복붙하기 좀 그런 곳')

@app.get('/step2')
def step2(request : Request) :
    print('/step2 실행')
    data = request.query_params
    item = data.get('item')
    print(f'item : {item} 관련 일처리는 끝났고')

    print('step1으로 이동')
    # 1. forward 방식
    step1(request)
```

`/step2` 요청을 받은 함수 안에서 `step1(request)`를 호출하면 **같은 서버 실행 흐름 안의 Python 함수 호출**이다. 브라우저가 `/step1`에 새로 요청을 보낸 것은 아니다. 원본 주석의 “forward 방식”은 비교를 돕는 표현이지만, HTTP 수준의 새 주소 이동으로 오해하지 않는다. `step1`의 반환값도 `/step2`에서 `return`하지 않아 `/step2`는 별도 값을 반환하지 않는다.

## 2. 리다이렉트는 브라우저가 다음 주소로 다시 간다

### 강사님 코드

출처: `teacher/workspace_python/todos/03_response/api.py` 25–40행 · **원본 발췌**

```python
from fastapi.responses import RedirectResponse
@app.post('/step3')
def step3(request:Request) :
    print('/step3 실행')
    data = request.query_params
    item = data.get('item')
    print(f'item:{item} 관련 일 처리는 끝났고')

    print('step1으로 이동')
    # 2. redirect 방식
    return RedirectResponse(
        url='/step1',
        status_code=303 # 기본값: 307
    )
    # 303 : 다시 올 때 Get으로 접속
    # 307 : 다시 올 때 원래 방식 유지
```

### 내 코드

출처: `me/workspace_python/02_todos/03_response/api.py` 25–38행 · **원본 발췌**

```python
from fastapi.responses import RedirectResponse
@app.get('/step3')
def step3(request : Request) :
    print('/step3 실행')
    data = request.query_params
    item = data.get('item')
    print(f'item : {item} 관련 일처리는 끝났고')

    print('step1으로 이동')
    # 2. redirect 방식
    return RedirectResponse(
        url = '/step1?item='+str(item),
        status_code = 307, # 기본값은 307
    )
```

강사님은 `POST /step3` 뒤 `303`으로 `/step1`에 이동시킨다. `303`은 다음 요청을 GET으로 보내게 하는 코드다. 나는 `GET /step3`에서 `307`을 반환하고 `/step1?item=...`로 값을 주소에 다시 싣는다. `307`은 원래 방식을 유지하므로 이 내 코드에서는 **GET 다음 GET**이다. 강사님 코드는 `url='/step1'`이라 첫 요청의 `item`을 다음 주소에 싣지 않는다. 따라서 `/step1`의 `query_params.get('item')`은 별도 값이 없으면 `None`이다. 어떤 값이 다음 요청까지 이어지는지 두 코드를 비교한다.

## 직접 확인할 질문

1. `step1(request)`는 브라우저 요청을 하나 더 만드는가?
2. 강사님 `303`과 내 `307`은 다음 요청 방식에서 어떻게 다른가?
3. 강사님 `/step1` 주소와 내 `/step1?item=...`에서 `item` 값은 어떻게 다른가?

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/04_FastAPI_Response_Redirect_의존성주입_연습문제.md)

## 추가로 알면 좋은 것

응답 본문·헤더의 세부 구성과 `Response` 클래스별 옵션은 이 파일에 직접 작성하지 않았다. `Depends(get_session)` 형태의 **의존성 주입**은 [07 DB와 SQLModel](07_FastAPI_MariaDB_SQLModel_사원_CRUD.md)의 실제 코드에서 배운다.
