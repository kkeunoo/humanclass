# 04. 함수 호출과 리다이렉트 — 같은 실행과 새로운 요청 구분

[FastAPI 목차](README.md) · [읽기 안내](00_FastAPI_상세백과_읽기법.md)

서버 함수 안에서 다른 함수를 부르는 것과 브라우저에게 다른 주소로 요청하라고 응답하는 것은 다르다. 요청 횟수·주소·방식·전달 값·return을 따로 추적한다. 기존 파일명은 유지하지만 실제 의존성 주입은 DB 장에서 배운다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

직접 함수 호출과303·307응답의 차이를 설명한다. 호출 결과를 반환하지 않을 때의 None, 리다이렉트 대상의 방식 불일치, 쿼리 값을 주소에 다시 싣는 과정을 확인한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

함수 직접 호출은 Python의 실행 흐름이다. step2 안에서 step1(request)를 호출하면 이미 받은 request 객체를 같은 서버 안의 함수에 전달한다. 새로운 HTTP 요청이 생기지 않고 브라우저 주소도 그 호출만으로 바뀌지 않는다. 호출한 함수가 값을 반환하더라도 바깥 함수가 그 값을 return해야 바깥 경로의 응답에 사용된다.

리다이렉트는 이동 대상 주소와 상태를 응답으로 보내는 것이다. 이를 따르는 클라이언트가 다음 요청을 새로 보낸다. 응답을 보냈다는 사실과 클라이언트가 실제로 다음 요청을 수행했다는 사실도 구별한다.

| 응답 | 이 실습에서의 다음 요청 | 값의 유지 |
| --- | --- | --- |
| 303 | POST 뒤 GET으로 대상 조회 | 대상 주소·새 요청에 있는 것 |
| 307 | 원래 방식 유지 | 원래 방식·본문을 유지하는 이동 |
| 함수 직접 호출 | 새 HTTP 요청 없음 | 같은 request 객체 사용 가능 |

처음 주소의 쿼리가 대상 주소에 자동으로 붙는다고 가정하지 않는다. /step1로 보내면 기존 item쿼리가 없는 새 요청이고 /step1?item=책으로 보내야 그 주소의 쿼리를 읽을 수 있다. 307에서 POST를 유지했는데 대상은 GET전용이면405가 될 수 있다. 이동했으니 무조건 성공이라는 규칙이 아니다.

> 📚 **출처 · 본문 설명 확인:** [Starlette RedirectResponse](https://www.starlette.io/responses/#redirectresponse), [HTTP 표준 RFC9110 · 303](https://www.rfc-editor.org/rfc/rfc9110.html#name-303-see-other)·[307](https://www.rfc-editor.org/rfc/rfc9110.html#name-307-temporary-redirect). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. FastAPI·Uvicorn이 설치된 환경에서 api.py 하나를 새 폴더에 저장하고 `uvicorn api:app --port 8000 --reload`로 실행한다. /docs에서 POST를 보내거나 배운 폼·AJAX로 확인한다. 응답 이동을 자동으로 따라가는 브라우저는 첫303/307이 안 보일 수 있으므로 개발자도구 Network의 첫 응답과 다음 요청을 나눠 본다.



**[api.py](실습/책형_복습/04_FastAPI_Response_Redirect_의존성주입/api.py) — 새 예제 전체 파일**

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

직접 호출 두 경로는 같은 step1을 쓰지만 direct만 반환값을 응답으로 돌려준다. drop은 값을 버려 null이다. go의 첫 응답은303이고 대상 주소에 쿼리가 없어 다음 GET의 item은 null이다. keep은307이므로 다음 POST가 GET전용 step1에서405가 된다. carry는 원본처럼 문자열로 쿼리를 붙인 새 재현이며 A&B입력은 구분자&와 섞여 다음 item이 A만 되는 한계를 함께 보인다.

**요청과 예상 결과:**

| 흐름 | 첫 결과 | 다음 요청·결과 |
| --- | --- | --- |
| /direct?item=책 | 200, item책 | 새 요청 없음 |
| /drop?item=책 | 200, null | 새 요청 없음 |
| POST /go | 303, /step1 | GET /step1, item null |
| POST /keep | 307, /step1 | POST /step1, 405 |
| GET /carry?item=book | 307, 쿼리 포함 주소 | GET, item book |
| carry의 item에 A&B | 문자열 붙이기의 한계 | 다음 item은 A |

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/03_response/api.py` 5–23행 · **원본 발췌**

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

**발췌 바로 풀이:** `/step2` 요청을 받은 함수 안에서 `step1(request)`를 호출하면 **같은 서버 실행 흐름 안의 Python 함수 호출**이다. 브라우저가 `/step1`에 새로 요청을 보낸 것은 아니다. 원본 주석의 “forward 방식”은 비교를 돕는 표현이지만, HTTP 수준의 새 주소 이동으로 오해하지 않는다. `step1`의 반환값도 `/step2`에서 `return`하지 않아 `/step2`는 별도 값을 반환하지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/03_response/api.py` 25–38행 · **원본 발췌**

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

**발췌 바로 풀이:** 강사님은 `POST /step3` 뒤 `303`으로 `/step1`에 이동시킨다. `303`은 다음 요청을 GET으로 보내게 하는 코드다. 나는 `GET /step3`에서 `307`을 반환하고 `/step1?item=...`로 값을 주소에 다시 싣는다. `307`은 원래 방식을 유지하므로 이 내 코드에서는 **GET 다음 GET**이다. 강사님 코드는 `url='/step1'`이라 첫 요청의 `item`을 다음 주소에 싣지 않는다. 따라서 `/step1`의 `query_params.get('item')`은 별도 값이 없으면 `None`이다. 어떤 값이 다음 요청까지 이어지는지 두 코드를 비교한다.

두 원본의 step2는 step1(request)를 부르지만 return하지 않는다. 원본 step1도 print만 하고 return이 없으므로 모두 응답은 null이다. 새 step1의 dict 반환은 바깥 return의 차이를 보이기 위한 설명용 변경이다. 강사님 step3은 POST 뒤303·/step1, 내 step3은 GET 뒤307·쿼리 포함 주소라 다음 방식과 item이 달라진다.

<a id="connections"></a>

## 5. import·함수·화면·저장이 연결되는 흐름

직접 호출: GET /step2 → step2함수 → 같은 request로 step1호출 → 바깥 함수 끝 → 응답. 리다이렉트: 첫 HTTP요청 → RedirectResponse객체 반환 → 클라이언트가 Location주소 읽기 → 상태에 맞는 새 요청 → 대상 함수다. RedirectResponse는 실제 수업에서 가져온 응답 클래스이며 추가로 알면 좋은 request.headers 직접 읽기와 다르다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 item을 다음 주소에 다시 실어 값이 이어지는지 실험했다. **교정:** 주석의 forward는 Python 함수 재사용에 빗댄 표현이며 브라우저 주소 이동이 아니다. **설계 선택:** GET 다음 GET에는307이 동작하지만 POST 저장 뒤 조회라면303으로 방식을 바꾸는 의미를 따로 본다. **한계:** 단순 문자열 붙이기는 특수문자의 쿼리 값을 보존하지 못하며 item 없음도 문자열 None으로 만들 수 있다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_python/todos/03_response/api.py` 25–40행 · **원본 발췌**

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

의미가 다른 step3 비교만 강사님 인용을 남긴다. 강사님303은 POST 다음 GET대상에 맞지만 기존 item을 대상 주소에 싣지 않는다. 내307은 원래 GET을 유지하며 값을 싣지만 인코딩 한계가 있다. 목적을 정하지 않고303이나307한쪽이 언제나 좋다고 평가하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 처리 | 요청 수 관점 | item |
| --- | --- | --- |
| 직접 호출 | 최초 요청 하나 | 같은 request 쿼리 |
| 303 전송 | 첫 응답 | 아직 대상 실행 아님 |
| 대상 GET | 새 요청 | 대상 주소의 쿼리만 |
| 307 뒤 POST | 원래 방식으로 새 요청 | 대상이 그 방식 지원해야 함 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| drop에 return 추가 | dict응답 | 호출 결과 전달 |
| keep의307을303으로 | 다음 GET 성공 | 방식 변경 |
| go대상에 ?item=book 추가 | 다음 item book | 주소에 값 포함 |
| carry에 item 생략 | 다음 문자열 None 가능 | str(None) |

이동 뒤405면 원래 방식·상태·대상 등록 방식을 본다. item이 사라지면 대상 주소 쿼리를 확인한다. null이면 안쪽·바깥 return을 각각 본다. 브라우저가 이동을 자동으로 따라갔다면 마지막 화면만 보고 첫 응답을 놓치지 않는다.

**확인 범위:** 새 앱을 별도 임시 폴더에 복사해 프레임워크 요청·응답 흐름으로 확인한다. 실제 외부 서비스·운영 DB·브라우저 공개 서버에 요청한 결과와 구별한다. 원본 전체 앱을 무조건 실행하지 않으며 별도 확인한 원본 구간은 검증 보고서에 기록한다. 사용자의 가상환경은 검사에 읽기만 사용하고 파일을 설치·수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 쿼리 인코딩은 urllib.parse.urlencode 같은 도구를 추가로 볼 수 있다. [Python URL도구](https://docs.python.org/ko/3/library/urllib.parse.html#urllib.parse.urlencode)를 참고한다. 응답 클래스의 상세 옵션·보안 리다이렉트 검사·PRG설계의 확장은 선택 학습이다. Depends 실제 사용은07DB장 본문에 있으므로 미학습 전체로 분류하지 않는다.

request.headers 직접 읽기와 response_model은 미학습으로 확인된 선택 확장이다. 본문에서 이 기능을 선행 조건으로 요구하지 않는다. 응답·입력 타입 표시와 response_model 설정도 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. step1(request)가 HTTP요청을 추가하는가?
2. 함수 호출 결과를 안 돌려주면?
3. POST307의 다음 방식은?
4. 첫 주소 item이 대상에 자동 복사되는가?
5. A&B를 그대로 붙이면 왜 손실되는가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

서버 안의 Python 호출이다. 바깥 반환이 없으면 None이다. POST를 유지한다. 대상 주소에 있는 값을 다시 읽는다. &가 쿼리 구분자로 해석되기 때문이다.

</details>

| 구별 | 확인 |
| --- | --- |
| 직접 호출 | 같은 요청·바깥 return |
| 리다이렉트 | 첫 응답·새 요청 |
| 상태 | 303방식 변경·307유지 |
| 값 | 대상 주소·인코딩 |

[장별 연습문제](실습/연습문제/04_FastAPI_Response_Redirect_의존성주입_연습문제.md) · 다음은 [화면 Todo CRUD](05_FastAPI_Jinja_Todo_CRUD.md)다.
