# 02. 라우터와 입력·CRUD — 받은 값이 목록의 항목이 되기까지 — 연습문제

[본문](../../02_FastAPI_Router_Request_Pydantic_CRUD.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

APIRouter의 정의와 앱 등록, 네 입력 통로, 모델 필드와 사용 이름을 연결한다. 리스트 생성·조회·수정·삭제의 결과와 없는 항목·검증 실패를 설명한다. 원본의 GET 외 data 누락과 모델 이름 불일치를 교정한다.

[본문 3절](../../02_FastAPI_Router_Request_Pydantic_CRUD.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 요청과 결과 예상

**api.py**

```python
from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)
```

**models.py**

```python
from pydantic import BaseModel, Field

class Todo(BaseModel):
    id: int = Field(ge=1, le=100)
    item: str = Field(min_length=2, max_length=20)
```

**routes.py**

```python
from fastapi import APIRouter, Form, Path
from models import Todo

router = APIRouter()
todo_list = []

@router.get('/param')
def param(id: int, item: str = ''):
    return {'id': id, 'item': item}

@router.post('/form')
def form(id: int = Form(), item: str = Form()):
    return {'id': id, 'item': item}

@router.post('/todos')
def create(todo: Todo):
    todo_list.append(todo)
    return todo

@router.get('/todos/{todo_id}')
def read(todo_id: int = Path(ge=1, le=100)):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    return {'message': '없는 ID'}

@router.put('/todos/{todo_id}')
def update(todo_id: int, item: str):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = item
            return todo
    return {'message': '없는 ID'}

@router.delete('/todos/{todo_id}')
def delete(todo_id: int):
    remaining = []
    for todo in todo_list:
        if todo.id != todo_id:
            remaining.append(todo)
    todo_list[:] = remaining
    return todo_list
```

실행 전에 결과를 먼저 적는다. 상태·응답·서버 출력·변경된 자료를 구별한다.

<details>
<summary>풀이</summary>

| 순서 | 요청·입력 | 상태·결과 |
| --- | --- | --- |
| 1 | GET /param?id=3 | 200, id3·item빈문자열 |
| 2 | id=x 또는 id누락 | 422 |
| 3 | POST /form id3·item공부 | 200, 숫자3·문자열공부 |
| 4 | POST /todos {id:1,item:공부} | 200, 항목 생성 |
| 5 | GET /todos/1 | 생성한 항목 |
| 6 | GET /todos/0 | 422, 경계 실패 |
| 7 | GET /todos/2 | 200, 없는 ID 안내 |
| 8 | item한글자 생성 | 422, 길이 실패 |
| 9 | PUT /todos/1?item=복습 | 항목 내용 복습 |
| 10 | DELETE /todos/1 | [] |
| 11 | 다시 GET /todos/1 | 없는 ID 안내 |

api가 routes의 router를 가져오고, routes는 models의 Todo를 가져온다. POST /todos에 JSON을 주면 모델을 만든 뒤 같은 todo_list에 넣는다. 조회는 .id를 비교해 항목을 반환한다. PUT의 item은 이 예제에서 쿼리 인자라 주소 뒤 ?item=복습에 둔다. DELETE는 남길 항목을 새 리스트에 모아 기존 리스트 내용 전체를 바꾼다. 새 모델·함수의 정의를 세 파일 모두 제공했다.

| 단계 | 값·형태 | 결과 |
| --- | --- | --- |
| JSON 수신 | id1·item공부 | 모델 필드 검사 |
| append | Todo 객체 | 목록 한 항목 |
| GET 경로1 | 정수1 | .id 일치 |
| PUT 쿼리 | item복습 | 속성 변경 |
| DELETE | 남길 목록[] | 기존 목록 내용 교체 |

</details>

## 문제 2. 이유 설명

1. item 기본값이 있으면 쿼리에서 생략할 수 있는가?
2. /param2 POST에서 data는 정의되는가?
3. value1 모델에 .id가 있는가?
4. 생성 Field 검증이 수정 대입도 자동 검사하는가?
5. 원본 슬라이스 대입과 이름 재대입의 차이는?

<details>
<summary>풀이</summary>

기본값을 쓴다. 원본은 GET 분기만 있어 정의되지 않는다. 없다. 기본 설정의 생성 검증과 속성 대입은 구분한다. 슬라이스는 기존 목록 객체의 내용을 바꾸고 이름 대입은 다른 객체에 이름을 연결할 수 있다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| include_router 제거 | 해당 주소404 | 앱 미등록 |
| JSON id를0으로 | 422 | 생성 필드 ge1 |
| GET 없는 ID2 | 200 안내 | 현재 설계 |
| 같은 ID 다시 생성 | 중복 추가 | 중복 검사 없음 |
| 수정 item 한 글자 | 현재 예제 허용 | 생성 검증과 속성 대입 차이 |

<details>
<summary>막힐 때 확인</summary>

422면 입력 위치·필드 이름·필수값·타입·범위를 본다. ID 없음 안내가 200인지 404인지 현재 설계를 구분한다. 모델에 없는 속성 오류면 정의 필드를 확인한다. 목록에 dict와 모델이 섞이면 어느 읽기 방식을 썼는지 본다. /param2의 data 오류는 입력값 변환보다 앞선 분기 누락이다.

</details>

## 채점과 복습

정상 값만 보지 말고 누락·잘못된 타입·없는 대상의 흐름도 설명한다. 새 예제는 별도 앱에서 확인하며 원본 DB나 외부 서비스의 성공을 대신 주장하지 않는다. TIP 확장은 필수 조건이 아니다. 정의→등록→입력→호출→반환→다음 요청을 연결할 수 있는지 검토한다.
