# 04. 함수 호출과 리다이렉트 — 같은 실행과 새로운 요청 구분 — 연습문제

[본문](../../04_FastAPI_Response_Redirect_의존성주입.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

직접 함수 호출과303·307응답의 차이를 설명한다. 호출 결과를 반환하지 않을 때의 None, 리다이렉트 대상의 방식 불일치, 쿼리 값을 주소에 다시 싣는 과정을 확인한다.

[본문 3절](../../04_FastAPI_Response_Redirect_의존성주입.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 요청과 결과 예상

**api.py**

```python
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/step1')
def step1(request: Request):
    return {'item': request.query_params.get('item')}

@app.get('/direct')
def direct(request: Request):
    return step1(request)

@app.get('/drop')
def drop(request: Request):
    step1(request)

@app.post('/go')
def go():
    return RedirectResponse(url='/step1', status_code=303)

@app.post('/keep')
def keep():
    return RedirectResponse(url='/step1', status_code=307)

@app.get('/carry')
def carry(request: Request):
    item = request.query_params.get('item')
    return RedirectResponse(url='/step1?item=' + str(item), status_code=307)
```

실행 전에 결과를 먼저 적는다. 상태·응답·서버 출력·변경된 자료를 구별한다.

<details>
<summary>풀이</summary>

| 흐름 | 첫 결과 | 다음 요청·결과 |
| --- | --- | --- |
| /direct?item=책 | 200, item책 | 새 요청 없음 |
| /drop?item=책 | 200, null | 새 요청 없음 |
| POST /go | 303, /step1 | GET /step1, item null |
| POST /keep | 307, /step1 | POST /step1, 405 |
| GET /carry?item=book | 307, 쿼리 포함 주소 | GET, item book |
| carry의 item에 A&B | 문자열 붙이기의 한계 | 다음 item은 A |

직접 호출 두 경로는 같은 step1을 쓰지만 direct만 반환값을 응답으로 돌려준다. drop은 값을 버려 null이다. go의 첫 응답은303이고 대상 주소에 쿼리가 없어 다음 GET의 item은 null이다. keep은307이므로 다음 POST가 GET전용 step1에서405가 된다. carry는 원본처럼 문자열로 쿼리를 붙인 새 재현이며 A&B입력은 구분자&와 섞여 다음 item이 A만 되는 한계를 함께 보인다.

| 처리 | 요청 수 관점 | item |
| --- | --- | --- |
| 직접 호출 | 최초 요청 하나 | 같은 request 쿼리 |
| 303 전송 | 첫 응답 | 아직 대상 실행 아님 |
| 대상 GET | 새 요청 | 대상 주소의 쿼리만 |
| 307 뒤 POST | 원래 방식으로 새 요청 | 대상이 그 방식 지원해야 함 |

</details>

## 문제 2. 이유 설명

1. step1(request)가 HTTP요청을 추가하는가?
2. 함수 호출 결과를 안 돌려주면?
3. POST307의 다음 방식은?
4. 첫 주소 item이 대상에 자동 복사되는가?
5. A&B를 그대로 붙이면 왜 손실되는가?

<details>
<summary>풀이</summary>

서버 안의 Python 호출이다. 바깥 반환이 없으면 None이다. POST를 유지한다. 대상 주소에 있는 값을 다시 읽는다. &가 쿼리 구분자로 해석되기 때문이다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| drop에 return 추가 | dict응답 | 호출 결과 전달 |
| keep의307을303으로 | 다음 GET 성공 | 방식 변경 |
| go대상에 ?item=book 추가 | 다음 item book | 주소에 값 포함 |
| carry에 item 생략 | 다음 문자열 None 가능 | str(None) |

<details>
<summary>막힐 때 확인</summary>

이동 뒤405면 원래 방식·상태·대상 등록 방식을 본다. item이 사라지면 대상 주소 쿼리를 확인한다. null이면 안쪽·바깥 return을 각각 본다. 브라우저가 이동을 자동으로 따라갔다면 마지막 화면만 보고 첫 응답을 놓치지 않는다.

</details>

## 채점과 복습

정상 값만 보지 말고 누락·잘못된 타입·없는 대상의 흐름도 설명한다. 새 예제는 별도 앱에서 확인하며 원본 DB나 외부 서비스의 성공을 대신 주장하지 않는다. TIP 확장은 필수 조건이 아니다. 정의→등록→입력→호출→반환→다음 요청을 연결할 수 있는지 검토한다.
