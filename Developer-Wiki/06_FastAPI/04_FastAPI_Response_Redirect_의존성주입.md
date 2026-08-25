---
title: FastAPI Response, Redirect와 의존성 주입
version: v2.0-final
last_updated: 2026-08-25
status: Completed
---

# FastAPI Response, Redirect와 의존성 주입

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `04_FastAPI_Response_Redirect_의존성주입.md` |
| 분류 | `06_FastAPI` |
| 내 코드 | `workspace_python/02_todos/03_response/api.py` |
| 강사님 코드 | `workspace_teacher/workspace_python/todos/03_response/api.py` |
| 추가 메모 | 반환 Type Hint, `response_model`, 의존성 주입, Package 의존성 |
| 핵심 범위 | Response 검증, 함수 호출과 Forward, Redirect, 303·307, PRG, `Depends` |
| 참고 전용 | 학습 중인 `03_database`의 `Depends(get_session)` 흐름 |
| 문서 형식 | FastAPI Developer-Wiki V2 |

> 이 문서는 완료된 `03_response`와 2026-08-20 추가 메모를 정리한다. `03_database`는 의존성 주입이 다음 수업에서 DB Session으로 연결된다는 점만 확인했으며, 해당 코드 자체는 학습 문서 범위에 포함하지 않는다.

---

# 학습 목표

- Python 반환 Type Hint와 FastAPI Response 검증의 차이를 설명할 수 있다.
- `response_model`의 역할과 우선순위를 설명할 수 있다.
- 직접 함수 호출과 HTTP Forward를 구분할 수 있다.
- Redirect가 새로운 Client Request를 만드는 흐름을 설명할 수 있다.
- `303 See Other`와 `307 Temporary Redirect`를 구분할 수 있다.
- POST-Redirect-GET Pattern을 적용할 수 있다.
- FastAPI의 `Depends`를 이용한 의존성 주입을 설명할 수 있다.
- Package와 의존 Package의 설치 관계를 설명할 수 있다.

---

# 1. Response 처리 흐름

```text
Endpoint 반환값
→ Response Model/Field 검증 및 직렬화
→ JSON·HTML·Redirect 등 Response 생성
→ HTTP Status·Header·Body 전송
```

FastAPI는 Python 반환값을 그대로 전송하는 데 그치지 않고 Route 설정에 따라 검증하고 직렬화한다.

---

# 2. Python 반환 Type Hint

```python
def test() -> int:
    return 'ac'
```

Python 자체는 Type Hint만으로 함수 실행을 막지 않는다. 즉 일반 Python 함수는 `'ac'`를 반환할 수 있다. Type Hint는 IDE, 정적 분석기와 Framework가 활용하는 Metadata다.

FastAPI Route에서는 반환 Annotation으로 Response Field를 만들기 때문에 실제 응답 시 검증에 실패할 수 있다.

```python
@app.get('/')
def test() -> int:
    return 'ac'
```

`'ac'`는 정수로 변환할 수 없어 Response Validation Error가 발생한다. 단, `'1'`처럼 변환 가능한 값은 설정과 Type에 따라 정수로 직렬화될 수 있으므로 “문자열은 언제나 불가능”으로 외우지 않는다.

---

# 3. response_model

```python
@app.get('/', response_model=int)
def test():
    return 'ac'
```

`response_model`은 FastAPI에 응답 Data의 검증·직렬화·문서화 기준을 명시한다.

```python
@app.get('/', response_model=int)
def test() -> str:
    return 'ac'
```

두 기준이 동시에 있으면 명시한 `response_model=int`가 FastAPI Response Model로 사용된다. `-> str`은 함수의 Python Type 정보로 남지만 API Response Schema는 `response_model`을 따른다.

```text
response_model 지정됨 → response_model 기준
response_model 없음   → 반환 Type Annotation 활용
둘 다 없음            → 반환값을 기본 방식으로 직렬화
```

---

# 4. Pydantic Response Model

```python
from fastapi import FastAPI
from pydantic import BaseModel


class TodoResponse(BaseModel):
    id: int
    item: str


app = FastAPI()


@app.get('/todos/{todo_id}', response_model=TodoResponse)
def get_todo(todo_id: int):
    return {'id': todo_id, 'item': 'FastAPI'}
```

Response Model은 다음 역할을 한다.

- 반환 Data 검증
- JSON 직렬화
- 허용된 Field만 출력
- OpenAPI Schema 생성
- 자동 API 문서 반영

민감한 Field를 Response에서 제외하려면 Request/DB Model과 Response Model을 분리한다.

---

# 5. 수업의 step1

```python
@app.get('/step1')
def step1(request: Request):
    data = request.query_params
    item = data.get('item')
    print(f'item: {item}')
```

Query Parameter를 `Request`에서 직접 읽는다. FastAPI에서는 다음처럼 명시적으로 선언하는 편이 검증과 문서화에 유리하다.

```python
@app.get('/step1')
def step1(item: str | None = None):
    return {'item': item}
```

---

# 6. 함수 직접 호출과 Forward

수업의 `step2()`는 `step1(request)`를 직접 호출한다.

```python
@app.get('/step2')
def step2(request: Request):
    # 앞 작업
    step1(request)
```

이 코드는 같은 Process 안에서 Python 함수를 호출한다. Browser URL이 바뀌지 않고 Network Request도 추가되지 않는다는 점은 Forward와 비슷해 보이지만, FastAPI Router가 `/step1`으로 Request를 다시 Dispatch하는 **정식 HTTP Forward 기능은 아니다**.

또한 `step1()`의 반환값을 사용하지 않으므로 Response에도 반영되지 않는다.

```python
return step1(request)
```

처럼 반환하면 함수 결과는 사용할 수 있지만 여전히 단순 함수 호출이다. 공통 Logic은 별도 Service 함수로 추출하는 편이 명확하다.

---

# 7. Redirect

Redirect Response는 Client에게 다른 URL로 다시 요청하라고 알린다.

```python
from fastapi.responses import RedirectResponse


@app.post('/step3')
def step3(item: str):
    return RedirectResponse(
        url=f'/step1?item={item}',
        status_code=303,
    )
```

```text
POST /step3
← 303 Location: /step1?item=...
GET /step1?item=...
```

Redirect는 Browser가 새로운 Request를 보내므로 URL과 Request 흐름이 실제로 바뀐다.

---

# 8. 303과 307

| Status | 이름 | Redirect 후 Method |
| ---: | --- | --- |
| `303` | See Other | 일반적으로 GET으로 전환 |
| `307` | Temporary Redirect | 기존 Method와 Body 유지 |

Form POST 처리 후 목록 Page로 이동할 때는 `303`이 적합하다.

```text
POST 저장
→ 303 Redirect
→ GET 목록
```

이를 POST-Redirect-GET, PRG Pattern이라고 한다. 새로고침으로 POST가 중복 제출되는 문제를 줄인다.

---

# 9. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 | 영향 |
| --- | --- | --- | --- |
| `/step3` Method | GET | POST | 강사님 코드가 PRG 학습 의도에 적합 |
| Redirect Status | 307 | 303 | 내 코드는 Method 유지, 강사님은 GET 전환 |
| Query 전달 | URL에 `item` 연결 | `/step1`만 지정 | 내 코드는 값 유지, 강사님은 값 소실 |
| URL 생성 | 문자열 연결 | 고정 URL | 특수문자를 위해 안전한 Encoding 필요 |

두 코드의 장점을 결합하면 **POST + 303 + 안전한 Query Encoding**이 된다.

```python
from urllib.parse import urlencode

query = urlencode({'item': item})
return RedirectResponse(url=f'/step1?{query}', status_code=303)
```

---

# 10. 의존성 주입

의존성 주입, Dependency Injection은 함수가 필요한 객체를 내부에서 직접 만들기보다 외부에서 제공받도록 하는 설계 방식이다.

```python
from fastapi import Depends, FastAPI

app = FastAPI()


def get_settings():
    return {'service_name': 'Todo API'}


@app.get('/info')
def info(settings: dict = Depends(get_settings)):
    return settings
```

FastAPI는 Request 처리 중 `get_settings()`를 실행하고 그 결과를 `settings`에 주입한다.

```text
Endpoint가 필요한 것 선언
→ FastAPI가 Dependency 해결
→ 결과를 Parameter에 주입
→ Endpoint 실행
```

`classmethod`는 Class에 묶인 Method 호출 방식이고 의존성 주입은 객체 생성과 제공 책임을 분리하는 Pattern이므로 같은 개념이 아니다.

---

# 11. yield Dependency

DB Session처럼 사용 후 정리가 필요한 Resource는 `yield`를 사용할 수 있다.

```python
def get_resource():
    resource = open_resource()
    try:
        yield resource
    finally:
        resource.close()
```

```text
yield 이전  → Resource 준비
Endpoint    → Resource 사용
yield 이후  → Commit/Rollback/Close 같은 정리
```

학습 중인 `03_database`에서 `Depends(get_session)`으로 이어지는 이유가 바로 이 구조다. 해당 DB 구현은 이번 문서에 포함하지 않는다.

---

# 12. FastAPI와 Package 의존성

```powershell
python -m pip install fastapi
```

pip는 FastAPI Package Metadata에 선언된 필수 의존 Package도 함께 설치한다. 예를 들면 FastAPI가 사용하는 Starlette와 Pydantic 등이 있다.

하지만 모든 개발·운영 도구가 자동 설치되는 것은 아니다.

```text
fastapi 설치
→ FastAPI 필수 의존 Package 설치
→ Uvicorn, Jinja2, python-multipart 등은 사용 방식에 따라 별도 설치 가능
```

실습 환경에서는 다음처럼 명시적으로 관리하는 편이 이해하기 쉽다.

```powershell
python -m pip install fastapi uvicorn jinja2 python-multipart
python -m pip freeze > requirements.txt
```

---

# 13. 개선된 통합 예제

```python
from urllib.parse import urlencode

from fastapi import Depends, FastAPI, Form
from fastapi.responses import RedirectResponse

app = FastAPI()


def normalize_item(item: str = Form(min_length=1)) -> str:
    return item.strip()


@app.get('/step1', response_model=dict[str, str])
def step1(item: str = ''):
    return {'item': item}


@app.post('/step3')
def step3(item: str = Depends(normalize_item)):
    # 저장 등 업무 처리
    query = urlencode({'item': item})
    return RedirectResponse(
        url=f'/step1?{query}',
        status_code=303,
    )
```

---

# 14. 자주 하는 실수와 Debugging

| 문제 | 원인 | 해결 |
| --- | --- | --- |
| Response Validation Error | 반환값이 Model과 불일치 | 반환 Type·Field 확인 |
| POST가 Redirect 후 반복됨 | 307로 Method 유지 | PRG라면 303 사용 |
| Query 값이 사라짐 | Redirect URL에 값 없음 | 필요 값 Encode 또는 Session 사용 |
| 특수문자 URL 오류 | 문자열로 Query 연결 | `urlencode` 사용 |
| 함수 호출 결과 없음 | 반환값을 버림 | `return` 또는 Service 함수 분리 |
| Dependency 실행 안 됨 | `Depends()` 선언 누락 | Parameter 선언 확인 |

---

# 15. 종합실습

1. `TodoResponse` Pydantic Model을 작성한다.
2. `response_model=TodoResponse`를 지정한다.
3. 의도적으로 잘못된 반환값을 넣고 검증 오류를 확인한다.
4. POST Form을 처리하는 `/save`를 만든다.
5. 처리 후 `303`으로 `/result`에 Redirect한다.
6. Query String은 `urlencode`로 만든다.
7. 입력값 정리 함수를 Dependency로 주입한다.
8. 직접 함수 호출과 Redirect의 Network 차이를 설명한다.

---

# 16. 정답 핵심

```python
from urllib.parse import urlencode

from fastapi import Depends, FastAPI, Form
from fastapi.responses import RedirectResponse
from pydantic import BaseModel


class TodoResponse(BaseModel):
    item: str


app = FastAPI()


def clean_item(item: str = Form(min_length=1)) -> str:
    return item.strip()


@app.post('/save')
def save(item: str = Depends(clean_item)):
    query = urlencode({'item': item})
    return RedirectResponse(f'/result?{query}', status_code=303)


@app.get('/result', response_model=TodoResponse)
def result(item: str):
    return {'item': item}
```

---

# 최종 체크리스트

- [ ] Python Type Hint 자체는 Runtime 강제가 아님을 설명할 수 있다.
- [ ] FastAPI 반환 Annotation의 Response 검증 역할을 설명할 수 있다.
- [ ] `response_model`이 명시되면 그 Model이 응답 기준임을 설명할 수 있다.
- [ ] 직접 함수 호출과 Redirect를 구분할 수 있다.
- [ ] 303과 307의 Method 처리 차이를 설명할 수 있다.
- [ ] PRG Pattern을 구현할 수 있다.
- [ ] `Depends`와 `classmethod`를 구분할 수 있다.
- [ ] `yield` Dependency의 준비·사용·정리 흐름을 설명할 수 있다.
- [ ] pip가 필수 의존 Package를 함께 설치한다는 의미를 설명할 수 있다.

---

# 핵심 요약

```text
Type Hint = Python Metadata
response_model = FastAPI 응답 검증·직렬화·문서화 기준
함수 직접 호출 ≠ HTTP Forward
Redirect = Client가 새 Request 전송
303 = GET 전환, PRG에 적합
307 = 기존 Method 유지
Depends = 필요한 객체·값을 FastAPI가 주입
pip = 선언된 필수 의존 Package도 함께 설치
```

