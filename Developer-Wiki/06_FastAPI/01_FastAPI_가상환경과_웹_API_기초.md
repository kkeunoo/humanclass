# 01. 첫 FastAPI — 주소와 방식이 Python 함수에 도착하기까지

[FastAPI 목차](README.md) · [읽기 안내](00_FastAPI_상세백과_읽기법.md)

웹 브라우저가 보낸 요청을 Python 함수가 받아 값을 돌려준다. 앱·서버·주소·방식·반환값을 구분하면 API를 처음 보는 사람도 한 요청이 지나가는 길을 설명할 수 있다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

FastAPI 앱과 실행 서버의 역할을 구별한다. GET·POST 경로 등록과 함수 호출·반환을 연결하고, JSON 문자열·HTML 문서·None과404를 나눈다. 가상환경 메모는 실행 준비로 표시한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

API는 프로그램이 다른 프로그램의 기능을 사용하도록 정한 접점이다. 이 수업은 HTTP 요청을 받아 Python 함수로 처리하는 웹 API를 만든다. 브라우저는 요청하는 클라이언트이고, FastAPI 앱은 어떤 주소·방식을 어느 함수로 처리할지 정의한다. Uvicorn은 그 앱을 실행하며 HTTP 요청을 받는 서버 프로그램이다.

| 자리 | 뜻 | 예 |
| --- | --- | --- |
| 호스트·포트 | 접속할 서버 위치 | 127.0.0.1:8000 |
| 경로 | 요청할 기능 주소 | /html |
| 방식 | 그 주소에 하는 요청 종류 | GET·POST |
| 경로 함수 | 등록된 Python 처리 | welcome·html |
| 반환값 | 응답 재료 | 딕셔너리·문자열·None |

```text
브라우저 GET / → Uvicorn → FastAPI 경로 선택 → welcome() → dict → JSON 응답
```

@app.get('/')는 등록할 때 요청을 보내는 명령이 아니다. 아래 함수를 GET /에 연결한다. 나중에 해당 요청이 왔을 때 프레임워크가 함수를 호출한다. 같은 경로라도 방식이 다르면 다른 함수를 등록할 수 있다. GET·POST가 있다고 HTTP 방식 전체가 네 개뿐인 것은 아니다.

딕셔너리 반환은 이 예제에서 JSON객체로 변환된다. 문자열에 h1태그가 있다고 자동 HTML문서 응답이 되지는 않는다. return없는 함수는 Python의None을 반환하고 여기서는 JSONnull이 된다. 등록된 경로의 None과 경로가 없는404는 다른 상태다.

> 📚 **출처 · 본문 설명 확인:** [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/), [Python 함수 반환](https://docs.python.org/ko/3/tutorial/controlflow.html#defining-functions). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. Python과 FastAPI·Uvicorn이 설치된 연습 환경에서 api.py가 있는 폴더로 이동해 `uvicorn api:app --port 8000 --reload`로 실행한다. api:app은 api.py의 app변수다. 주소창에는 http://127.0.0.1:8000/를 연다. 새로 준비한다면 내 학습 메모의 `python -m venv todos` → Windows PowerShell에서 `./todos/Scripts/Activate.ps1` → `python -m pip install fastapi uvicorn` 순서를 참고한다. 이는 api.py 원본 함수 코드가 아니라 실행 준비 메모다. 정책 때문에 활성화가 막히면 환경의 python.exe로 명령을 실행하는 방법을 별도로 확인한다.



**[api.py](실습/책형_복습/01_FastAPI_가상환경과_웹_API_기초/api.py) — 새 예제 전체 파일**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome() -> dict:
    return {'message': 'Hello World2'}

@app.get('/html')
def html():
    return '<h1>hello</h1>'

@app.post('/html')
def html_post():
    return '<h1>hello2</h1>'

@app.get('/no')
def no():
    print('들어왔음')
```

서버가 api.py를 읽을 때 app을 만들고 네 경로를 등록한다. GET /에서 welcome을 호출하면 message가 있는 딕셔너리가 응답이 된다. 주소창의 /html이 GET이므로 html_post가 아닌 html을 실행한다. POST는 /docs의 해당 항목에서 Try it out으로 보내거나 배운 폼·AJAX를 사용한다. /no의print는 서버터미널에 나오고 브라우저 응답 본문은null이다.

**요청과 예상 결과:**

| 요청 | 상태 | 응답 본문 |
| --- | --- | --- |
| GET / | 200 | {"message":"Hello World2"} |
| GET /html | 200 | JSON 문자열 h1태그 |
| POST /html | 200 | JSON 문자열 hello2태그 |
| GET /no | 200 | null |
| GET /missing | 404 | 없는 경로 안내 |
| PUT /html | 405 | 등록되지 않은 방식 |

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/api.py` 1–9행 · **원본 발췌**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome() -> dict:
    return {
        "message" : "Hello World2"
    }
```

**발췌 바로 풀이:** `app = FastAPI()`는 앱 객체를 만들고, `@app.get('/')`는 **GET /** 요청이 오면 아래 `welcome()`을 실행하도록 등록한다. 함수가 딕셔너리를 반환하므로 브라우저에는 JSON 형태의 `message`가 보인다. `-> dict`는 Python의 **반환형 표시**이고, 사용자가 배우지 않았다고 확인한 `response_model` 설정과 같지 않다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/api.py` 11–30행 · **원본 발췌**

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

**발췌 바로 풀이:** `GET /html`과 `POST /html`은 **주소는 같아도 방식이 달라** 서로 다른 함수에 연결된다. 주소창으로 이동하면 보통 GET이므로 POST 전용 함수만 있다면 그 방식으로는 호출되지 않는다. 문자열 `"<h1>hello</h1>"`을 그냥 반환한 것은 **HTML 문서 응답으로 렌더링한 예제가 아니다**. 화면에 실제 제목 태그를 만들려면 적절한 HTML 응답 방식이 필요하며, 이 점은 [04 응답과 리다이렉트](04_FastAPI_Response_Redirect_의존성주입.md)의 추가 설명으로 둔다.

내 앱의 welcome은 강사님과 같은 message를 반환한다. GET·POST /html의 함수를 각각 등록했다. 주소와 방식이 같은 중복 GET예시는 주석으로 막혀 있고 실제 활성 경로는 서로 다른 방식이다. 내 /no 주석의“원래404”는 잘못된 설명이다. 경로가 있고 함수가None을 반환하는 것이므로404를 의미하지 않는다.

<a id="connections"></a>

## 5. import·함수·화면·저장이 연결되는 흐름

fastapi 모듈의 FastAPI 클래스 가져오기 → 객체 app 생성 → 데코레이터가 경로 함수 등록 → Uvicorn이 api:app을 로드 → HTTP 요청 → 함수 본문 → 반환 → 응답이다. welcome 정의만 읽을 때는 함수 본문의 return이 실행되지 않는다. app2 주석이 없어도 동작은 같고 따옴표 종류도 이 예제 문자열의 값을 바꾸지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 같은 경로의 방식별 함수와 반환 없는 함수를 실험해 차이를 확인했다. **교정:** return이 없으면 404라는 주석은 틀리다. 문자열 태그 반환과 HTML 문서 응답도 구분한다. **수업용 단순화:** 중복 경로는 먼저 등록한 경로가 선택되는 상황을 관찰할 수 있지만 의도적인 API 설계 방법으로 권하지 않는다. **이름 개선:** html과 html_post처럼 방식을 드러내면 새 설명 예제에서는 읽기 쉽다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



핵심 동작이 같아 강사님 코드를 중복 인용하지 않는다. 강사님은 반환 없는 함수가 null이라는 메모를 남겼고 내 주석은 404라고 추측했다. 이 차이는 경로 존재와 반환값을 구분하는 교정에 유용하다. 같은 코드 길이나 따옴표 차이를 우열로 평가하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 시점 | 일어나는 일 | 화면·터미널 |
| --- | --- | --- |
| 앱 읽기 | 객체·경로 등록 | 서버 준비 |
| /no 요청 | no 본문 실행 | 터미널 들어왔음 |
| 반환 생략 | None | 응답 null |
| 미등록 경로 | 함수 선택 불가 | 404 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| message 문구 변경 | JSON 값 변경 | 반환 자료 변경 |
| /no에 return 3 추가 | 응답 3 | 반환값 생김 |
| GET 등록을 POST로 변경 | 주소창 GET은 405 | 방식 불일치 |
| 경로를 /hello로 변경 | 기존 주소 404 | 등록 주소 변경 |

서버가 안 뜨면 설치 환경·현재 폴더·api.py와 app 이름을 본다. 연결이 안 되면 실행 중인지·포트가 맞는지 확인한다. 404는 주소, 405는 방식, 422는 이후 입력 검증과 구별한다. 터미널 print가 브라우저에 안 보인다고 반환 실패로 판단하지 않는다.

**확인 범위:** 새 앱을 별도 임시 폴더에 복사해 프레임워크 요청·응답 흐름으로 확인한다. 실제 외부 서비스·운영 DB·브라우저 공개 서버에 요청한 결과와 구별한다. 원본 전체 앱을 무조건 실행하지 않으며 별도 확인한 원본 구간은 검증 보고서에 기록한다. 사용자의 가상환경은 검사에 읽기만 사용하고 파일을 설치·수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** HTMLResponse·응답 헤더 직접 조작·배포 서버·프록시·고급 가상환경 설정은 추가 학습이다. [FastAPI HTML 응답](https://fastapi.tiangolo.com/advanced/custom-response/#html-response)을 참고할 수 있다. request.headers와 response_model은 사용자가 미학습으로 확인한 항목이다.

request.headers 직접 읽기와 response_model은 미학습으로 확인된 선택 확장이다. 본문에서 이 기능을 선행 조건으로 요구하지 않는다. 응답·입력 타입 표시와 response_model 설정도 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. api:app의 두 이름은?
2. @app.get이 선언될 때 함수 본문도 호출되는가?
3. /no와 없는 주소의 상태는 다른가?
4. 서버 print가 응답 본문인가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

모듈 api와 그 안 app이다. 요청 때 호출된다. /no는 200·null이고 없는 주소는 404다. print는 서버 터미널 출력이다.

</details>

| 구별 | 질문 |
| --- | --- |
| 주소·방식 | 어느 경로의 어떤 요청인가 |
| 정의·호출 | 등록인가 요청 처리인가 |
| 출력·반환 | 터미널인가 응답인가 |

[장별 연습문제](실습/연습문제/01_FastAPI_가상환경과_웹_API_기초_연습문제.md) · 다음은 [라우터·입력·CRUD](02_FastAPI_Router_Request_Pydantic_CRUD.md)다.
