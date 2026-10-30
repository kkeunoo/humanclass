# 01. 첫 FastAPI — 주소와 방식이 Python 함수에 도착하기까지 — 연습문제

[본문](../../01_FastAPI_가상환경과_웹_API_기초.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

FastAPI 앱과 실행 서버의 역할을 구별한다. GET·POST 경로 등록과 함수 호출·반환을 연결하고, JSON 문자열·HTML 문서·None과404를 나눈다. 가상환경 메모는 실행 준비로 표시한다.

[본문 3절](../../01_FastAPI_가상환경과_웹_API_기초.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 요청과 결과 예상

**api.py**

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

실행 전에 결과를 먼저 적는다. 상태·응답·서버 출력·변경된 자료를 구별한다.

<details>
<summary>풀이</summary>

| 요청 | 상태 | 응답 본문 |
| --- | --- | --- |
| GET / | 200 | {"message":"Hello World2"} |
| GET /html | 200 | JSON 문자열 h1태그 |
| POST /html | 200 | JSON 문자열 hello2태그 |
| GET /no | 200 | null |
| GET /missing | 404 | 없는 경로 안내 |
| PUT /html | 405 | 등록되지 않은 방식 |

서버가 api.py를 읽을 때 app을 만들고 네 경로를 등록한다. GET /에서 welcome을 호출하면 message가 있는 딕셔너리가 응답이 된다. 주소창의 /html이 GET이므로 html_post가 아닌 html을 실행한다. POST는 /docs의 해당 항목에서 Try it out으로 보내거나 배운 폼·AJAX를 사용한다. /no의print는 서버터미널에 나오고 브라우저 응답 본문은null이다.

| 시점 | 일어나는 일 | 화면·터미널 |
| --- | --- | --- |
| 앱 읽기 | 객체·경로 등록 | 서버 준비 |
| /no 요청 | no 본문 실행 | 터미널 들어왔음 |
| 반환 생략 | None | 응답 null |
| 미등록 경로 | 함수 선택 불가 | 404 |

</details>

## 문제 2. 이유 설명

1. api:app의 두 이름은?
2. @app.get이 선언될 때 함수 본문도 호출되는가?
3. /no와 없는 주소의 상태는 다른가?
4. 서버 print가 응답 본문인가?

<details>
<summary>풀이</summary>

모듈 api와 그 안 app이다. 요청 때 호출된다. /no는 200·null이고 없는 주소는 404다. print는 서버 터미널 출력이다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| message 문구 변경 | JSON 값 변경 | 반환 자료 변경 |
| /no에 return 3 추가 | 응답 3 | 반환값 생김 |
| GET 등록을 POST로 변경 | 주소창 GET은 405 | 방식 불일치 |
| 경로를 /hello로 변경 | 기존 주소 404 | 등록 주소 변경 |

<details>
<summary>막힐 때 확인</summary>

서버가 안 뜨면 설치 환경·현재 폴더·api.py와 app 이름을 본다. 연결이 안 되면 실행 중인지·포트가 맞는지 확인한다. 404는 주소, 405는 방식, 422는 이후 입력 검증과 구별한다. 터미널 print가 브라우저에 안 보인다고 반환 실패로 판단하지 않는다.

</details>

## 채점과 복습

정상 값만 보지 말고 누락·잘못된 타입·없는 대상의 흐름도 설명한다. 새 예제는 별도 앱에서 확인하며 원본 DB나 외부 서비스의 성공을 대신 주장하지 않는다. TIP 확장은 필수 조건이 아니다. 정의→등록→입력→호출→반환→다음 요청을 연결할 수 있는지 검토한다.
