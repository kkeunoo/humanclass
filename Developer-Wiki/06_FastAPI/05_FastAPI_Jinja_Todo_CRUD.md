---
title: FastAPI Jinja Todo CRUD
version: v2.0-final
last_updated: 2026-08-25
status: Completed
---

# FastAPI Jinja Todo CRUD

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `05_FastAPI_Jinja_Todo_CRUD.md` |
| 분류 | `06_FastAPI` |
| 내 코드 | `workspace_python/02_todos/04_jinja_todo/api.py`, `templates/create.html`, `read.html`, `detail.html`, `update.html` |
| 강사님 코드 | `workspace_teacher/workspace_python/todos/04_jinja_todo/api.py`, `todo.py`, `templates/add.html`, `list.html`, `detail.html`, `update.html` |
| 핵심 범위 | Jinja 화면과 FastAPI CRUD 연결, Form, Pydantic, Path·Query, Redirect, PRG, Memory 저장소 |
| 제외 범위 | 학습 중인 `03_database` |
| 문서 형식 | FastAPI Developer-Wiki V2 |

> 이 문서는 `04_jinja_todo`의 화면 기반 Todo CRUD를 정리한다. 내 코드는 직접 구현한 Dict 기반 흐름을, 강사님 코드는 Pydantic Form Model과 Resource 식별 방식을 중심으로 비교한다.

---

# 학습 목표

- Jinja Page와 FastAPI Endpoint를 연결할 수 있다.
- 화면 표시 Route와 Data 처리 Route를 구분할 수 있다.
- Form Data로 Todo를 생성하고 수정할 수 있다.
- 목록, 상세, 생성, 수정, 삭제 흐름을 구현할 수 있다.
- Path Parameter와 Query Parameter의 설계 차이를 설명할 수 있다.
- `303` Redirect로 PRG Pattern을 적용할 수 있다.
- Dict와 Pydantic Model 기반 구현을 비교할 수 있다.
- GET 삭제와 Client 전달값 신뢰 문제를 수정할 수 있다.

---

# 1. 전체 화면 흐름

```text
GET  목록 Page
→ GET 생성 Form
→ POST 생성 처리
→ 303 Redirect
→ GET 목록 Page
→ GET 상세 Page
→ GET 수정 Form
→ POST 수정 처리
→ POST 삭제 처리
```

화면을 보여주는 GET과 Data를 변경하는 POST를 분리하는 것이 핵심이다.

---

# 2. Memory 저장소

수업에서는 List가 임시 Database 역할을 한다.

```python
todo_list = []
```

장점은 구조가 단순하고 CRUD Algorithm에 집중할 수 있다는 것이다. 단점은 Process를 재시작하면 모든 Data가 사라지고 여러 Worker 사이에서 Data를 공유할 수 없다는 것이다.

---

# 3. Create

## 3.1 내 코드

```python
@app.post('/create')
async def api_create(request: Request):
    data = await request.form()
    todo_id = data.get('id')
    item = data.get('item')

    if todo_id != '' and item != '':
        todo_list.append({'id': todo_id, 'item': item})
        return RedirectResponse('/read', status_code=303)

    return RedirectResponse('/create', status_code=303)
```

직접 Form Data를 추출해 Dict로 저장한다. 빈 문자열은 막지만 ID의 정수 변환, 길이, 중복 여부 검증은 없다.

## 3.2 강사님 코드

```python
class Todo(BaseModel):
    id: int
    item: str | None = None


@app.post('/api/add')
def add_todo(todo: Todo = Form()):
    todo_list.append(todo)
    return RedirectResponse('/list', status_code=303)
```

Pydantic Model로 Form Data의 구조와 Type을 검증한다. 원본의 `item: str = None`은 Annotation과 기본값이 어긋나므로 `str | None` 또는 필수 `str`로 표현하는 편이 정확하다.

---

# 4. Read 목록

```python
@app.get('/todos')
def list_page(request: Request):
    return templates.TemplateResponse(
        request,
        'list.html',
        {'todos': todo_list},
    )
```

```jinja2
{% if todos %}
    {% for todo in todos %}
        <a href="/todos/{{ todo.id }}">{{ todo.item }}</a>
    {% endfor %}
{% else %}
    <p>조회할 목록이 없습니다.</p>
{% endif %}
```

Jinja에서는 Dict의 Key와 객체 Attribute 모두 `todo.id` 형태로 접근할 수 있어 두 구현이 비슷해 보인다.

---

# 5. Detail

내 코드는 목록 Link에서 ID와 Item을 모두 Query String으로 전달한다.

```text
/detail?id=1&item=내용
```

이 방식은 사용자가 URL의 `item`을 수정할 수 있어 Server 저장값과 다른 내용이 표시될 수 있다. ID만 받고 Server의 List에서 다시 조회해야 한다.

```python
@app.get('/todos/{todo_id}')
def detail_page(request: Request, todo_id: int):
    todo = find_todo(todo_id)
    return templates.TemplateResponse(
        request,
        'detail.html',
        {'todo': todo},
    )
```

강사님 코드의 `/detail/{id}`가 Resource 식별 관점에서 더 안전하다.

---

# 6. Update

Update는 기존 Data를 조회해 Form에 표시한 뒤 변경값을 전송한다.

```jinja2
<form method="post" action="/todos/{{ todo.id }}/update">
    <input type="text" name="item" value="{{ todo.item }}">
    <button type="submit">수정</button>
</form>
```

```python
@app.post('/todos/{todo_id}/update')
def update_todo(todo_id: int, item: str = Form(min_length=1)):
    todo = find_todo(todo_id)
    todo.item = item
    return RedirectResponse(f'/todos/{todo_id}', status_code=303)
```

내 코드는 POST 처리 후 목록 Template을 바로 Rendering한다. Redirect로 GET 목록을 다시 요청하면 새로고침 시 Form 재전송을 방지할 수 있다.

---

# 7. Delete

내 코드는 GET Route로 삭제한다.

```python
@app.get('/delete/{id}')
```

GET은 조회를 위한 안전한 Method로 취급되며 Link Preview, Crawler, 재요청만으로도 실행될 수 있다. Data 삭제에 GET을 사용하지 않는다.

HTML Form은 기본적으로 GET과 POST만 지원하므로 수업 Page에서는 POST 처리 Route가 적절하다.

```jinja2
<form method="post" action="/todos/{{ todo.id }}/delete">
    <button type="submit">삭제</button>
</form>
```

```python
@app.post('/todos/{todo_id}/delete')
def delete_todo(todo_id: int):
    # 삭제 처리
    return RedirectResponse('/todos', status_code=303)
```

JavaScript API Client라면 `DELETE /todos/{id}`를 사용할 수 있다.

---

# 8. 검색 Helper와 404

반복되는 List 검색을 함수로 분리한다.

```python
from fastapi import HTTPException


def find_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail='Todo를 찾을 수 없습니다.')
```

원본들은 값이 없을 때 `None`을 Template에 전달하거나 화면이 비어 보일 수 있다. Resource가 없으면 `404`로 명확히 응답한다.

---

# 9. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 | 판단 |
| --- | --- | --- | --- |
| 저장 객체 | Dict | Pydantic `Todo` | 강사님 코드가 Type 검증에 유리 |
| 목록 URI | `/read` | `/list` | 둘 다 학습용, `/todos` 권장 |
| 생성 URI | GET·POST `/create` | GET `/add`, POST `/api/add` | 내 코드는 Page/처리 URI 통합 |
| 상세 식별 | Query에 ID·Item | Path에 ID | 강사님 방식이 저장값 재조회에 유리 |
| 수정 | Template 직접 반환 | 303 목록 Redirect | 강사님 방식이 PRG에 적합 |
| 삭제 | GET Path | POST Form | 강사님 방식이 안전 |
| UI | CSS가 포함된 자체 화면 | 기능 중심 기본 화면 | 내 코드가 시각적 완성도 보강 |

내 코드는 화면 구성과 전체 흐름을 직접 완성했다는 장점이 크다. Backend 설계는 강사님 코드의 Pydantic, Path ID, POST 삭제, PRG 방식을 결합하면 더 안전해진다.

---

# 10. 강사님 코드의 보완점

- `list`, `detail`, `apiAdd`처럼 함수 이름이 중복되거나 Built-in 이름과 겹치지 않게 고유 이름을 사용한다.
- `Todo.item`이 선택값이면 `str | None`, 필수라면 `str`로 선언한다.
- ID 중복을 검사한다.
- 없는 ID는 `404`를 반환한다.
- 수정·삭제 후 실제 변경 여부를 확인한다.
- Memory 저장소의 한계를 문서화한다.

---

# 11. 개선된 통합 Model

```python
from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: int = Field(ge=1)
    item: str = Field(min_length=1, max_length=100)
```

Form에서 Model을 받는다.

```python
from typing import Annotated
from fastapi import Form


TodoForm = Annotated[Todo, Form()]


@app.post('/todos')
def create_todo(todo: TodoForm):
    if any(saved.id == todo.id for saved in todo_list):
        raise HTTPException(status_code=409, detail='이미 존재하는 ID입니다.')

    todo_list.append(todo)
    return RedirectResponse('/todos', status_code=303)
```

---

# 12. 개선된 Route 설계

| 목적 | Method | URI |
| --- | --- | --- |
| 목록 | GET | `/todos` |
| 생성 Form | GET | `/todos/new` |
| 생성 처리 | POST | `/todos` |
| 상세 | GET | `/todos/{id}` |
| 수정 Form | GET | `/todos/{id}/edit` |
| 수정 처리 | POST | `/todos/{id}/update` |
| 삭제 처리 | POST | `/todos/{id}/delete` |

HTML Form 제약을 반영한 Server-rendered Page 설계다. 순수 REST API라면 PUT/PATCH와 DELETE를 사용한다.

---

# 13. 실무 지침

- HTML의 `action`과 `href`에 Host·Port를 Hard Coding하지 말고 상대 URL을 사용한다.
- 사용자에게 받은 Item 값을 URL에 다시 싣지 말고 Server에서 ID로 조회한다.
- Data 변경 후 `303` Redirect로 PRG를 적용한다.
- 삭제는 GET Link가 아니라 POST Form 또는 DELETE Request로 처리한다.
- Input 검증은 HTML 속성만 믿지 말고 Server에서도 수행한다.
- 실제 Service에서는 CSRF 방어, 인증·권한, Database Transaction을 추가한다.

---

# 14. 자주 하는 실수와 Debugging

| 증상 | 원인 | 해결 |
| --- | --- | --- |
| ID 비교 실패 | 내 코드는 Form ID가 문자열 | Model에서 `int` 검증 |
| 상세값 조작 | Item을 Query로 전달 | ID만 받고 Server에서 재조회 |
| 새로고침 시 중복 처리 | POST 후 Template 직접 반환 | 303 Redirect |
| 삭제가 예기치 않게 실행 | GET 삭제 | POST 또는 DELETE 사용 |
| 없는 ID에서 화면 오류 | `None` Template 접근 | 404 처리 |
| 재시작 후 Data 소실 | Memory List | 이후 DB 저장소 연결 |

---

# 15. 종합실습

1. Pydantic `Todo` Model을 작성한다.
2. 목록·생성·상세·수정·삭제 Page를 연결한다.
3. ID는 Path Parameter로 사용한다.
4. 상세 Page는 ID로 Server List를 다시 조회한다.
5. 중복 ID는 `409`, 없는 ID는 `404`로 처리한다.
6. 수정·삭제는 POST 처리 후 `303` Redirect한다.
7. Template URL에서 Host와 Port Hard Coding을 제거한다.
8. Server 재시작 후 Data가 사라지는 이유를 설명한다.

---

# 16. 정답 흐름

```text
GET /todos/new
→ 생성 Form

POST /todos
→ Form Model 검증
→ List 추가
→ 303 /todos

GET /todos/{id}
→ Server에서 ID 조회
→ 상세 Rendering

POST /todos/{id}/update
→ 기존 객체 수정
→ 303 /todos/{id}

POST /todos/{id}/delete
→ List에서 삭제
→ 303 /todos
```

---

# 최종 체크리스트

- [ ] 화면 Route와 처리 Route를 구분할 수 있다.
- [ ] Form Data를 Pydantic Model로 검증할 수 있다.
- [ ] 목록·상세·생성·수정·삭제 화면을 연결할 수 있다.
- [ ] 상세 조회에 ID만 전달해야 하는 이유를 설명할 수 있다.
- [ ] GET으로 삭제하면 안 되는 이유를 설명할 수 있다.
- [ ] 303 Redirect로 PRG를 적용할 수 있다.
- [ ] 중복 ID와 없는 ID를 HTTP Error로 처리할 수 있다.
- [ ] Memory 저장소의 한계를 설명할 수 있다.

---

# 핵심 요약

```text
GET = Page·Data 조회
POST = Form Data 변경
ID만 전달하고 저장값은 Server에서 재조회
Pydantic = Form 구조와 Type 검증
303 = POST 후 GET으로 이동
삭제 GET 금지
Memory List = 학습용, 재시작 시 Data 소실
```
