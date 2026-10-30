# 05. 화면 Todo CRUD — 폼의 값이 목록·상세·수정 화면으로 이어지는 길 — 연습문제

[본문](../../05_FastAPI_Jinja_Todo_CRUD.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

입력 화면 GET과 저장 POST를 구분한다. 폼 name→문자열 딕셔너리→리스트→템플릿의 연결을 설명한다. 최신 상세 조회·수정 뒤303·삭제 방식·중복 ID·누락과 빈 문자열의 차이를 원본과 개선안으로 나눈다.

[본문 3절](../../05_FastAPI_Jinja_Todo_CRUD.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 요청과 결과 예상

**api.py**

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory='templates')
todo_list = []

def find_todo(todo_id):
    for todo in todo_list:
        if todo['id'] == todo_id:
            return todo
    return None

@app.get('/create')
def create_page(request: Request):
    return templates.TemplateResponse(request, 'create.html')

@app.post('/create')
async def create(request: Request):
    data = await request.form()
    todo_id = (data.get('id') or '').strip()
    item = (data.get('item') or '').strip()
    if not todo_id or not item or find_todo(todo_id) is not None:
        return RedirectResponse('/create', status_code=303)
    todo_list.append({'id': todo_id, 'item': item})
    return RedirectResponse('/read', status_code=303)

@app.get('/read')
def read(request: Request):
    return templates.TemplateResponse(request, 'read.html', {'todos': todo_list})

@app.get('/detail/{todo_id}')
def detail(request: Request, todo_id: str):
    return templates.TemplateResponse(request, 'detail.html', {'todo': find_todo(todo_id)})

@app.get('/update/{todo_id}')
def update_page(request: Request, todo_id: str):
    return templates.TemplateResponse(request, 'update.html', {'todo': find_todo(todo_id)})

@app.post('/update')
async def update(request: Request):
    data = await request.form()
    todo = find_todo(data.get('id'))
    item = (data.get('item') or '').strip()
    if todo is not None and item:
        todo['item'] = item
    return RedirectResponse('/read', status_code=303)

@app.post('/delete/{todo_id}')
def delete(todo_id: str):
    remaining = []
    for todo in todo_list:
        if todo['id'] != todo_id:
            remaining.append(todo)
    todo_list[:] = remaining
    return RedirectResponse('/read', status_code=303)
```

**templates/create.html**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>추가</title></head><body>
<h1>Todo 추가</h1>
<form method="post" action="/create">
<label>ID <input name="id" required></label>
<label>내용 <input name="item" required></label>
<button type="submit">추가</button>
</form><a href="/read">목록</a>
</body></html>
```

**templates/read.html**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>목록</title></head><body>
<h1>Todo 목록</h1><a href="/create">추가</a>
{% if todos %}<ul>{% for todo in todos %}
<li><a href="/detail/{{ todo.id }}">{{ todo.id }}: {{ todo.item }}</a></li>
{% endfor %}</ul>{% else %}<p>자료가 없습니다.</p>{% endif %}
</body></html>
```

**templates/detail.html**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>상세</title></head><body>
{% if todo %}<h1>{{ todo.item }}</h1>
<p>ID {{ todo.id }}</p><a href="/update/{{ todo.id }}">수정</a>
<form method="post" action="/delete/{{ todo.id }}"><button type="submit">삭제</button></form>
{% else %}<p>없는 ID입니다.</p>{% endif %}
<a href="/read">목록</a></body></html>
```

**templates/update.html**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>수정</title></head><body>
{% if todo %}<form method="post" action="/update">
<input type="hidden" name="id" value="{{ todo.id }}">
<label>내용 <input name="item" value="{{ todo.item }}" required></label>
<button type="submit">수정 완료</button></form>
{% else %}<p>없는 ID입니다.</p>{% endif %}
<a href="/read">목록</a></body></html>
```

실행 전에 결과를 먼저 적는다. 상태·응답·서버 출력·변경된 자료를 구별한다.

<details>
<summary>풀이</summary>

| 순서 | 동작 | 상태·자료 |
| --- | --- | --- |
| 시작 | 목록 조회 | 빈 화면 안내 |
| 생성 | ID1·내용공부 | 303→/read, 문자열 dict 한 개 |
| 중복·누락 | 생성 재시도 | 303→/create, 추가 없음 |
| 수정 | ID1·내용복습 | 303→/read |
| 옛 item이 붙은 상세 | /detail/1?item=옛내용 | 현재 복습 표시 |
| GET 삭제 | /delete/1 | 405, 자료 유지 |
| POST 삭제 | /delete/1 | 303→/read, 빈 목록 |

처음 목록은 비어 있다. 폼의 id·item이 POST에 들어오면 누락을 빈 문자열로 바꾸고 양끝 공백을 정리한 뒤 저장한다. id는 숫자 변환을 하지 않아 문자열1이다. find_todo는 목록에서 해당 딕셔너리를 반환하므로 수정에서 item을 바꾸면 같은 목록 항목도 바뀐다. 수정 뒤303으로 새 GET목록을 요청한다. 상세는 주소의 item을 사용하지 않고 목록을 다시 찾아 최신 복습을 보여 준다. 삭제는 POST만 등록했으므로 GET으로 열어도 지워지지 않는다.

| 값 | 원본 학생 | 원본 강사님 | 새 예제 |
| --- | --- | --- | --- |
| id1 | 문자열 | 모델 정수 | 문자열 |
| 내용 위치 | dict키 | 모델속성 | dict키 |
| 상세 근거 | 주소 item | 목록 조회 | 목록 조회 |
| 수정 뒤 | POST의HTML |303GET |303GET |
| 삭제 | GET·remove | POST·pop/break | POST·남길 목록 |

</details>

## 문제 2. 이유 설명

1. 폼 문자열1과 모델 정수1은 같은 자료형인가?
2. None != 빈 문자열은 참인가?
3. 상세에서 주소 item을 믿으면 최신 값을 보장하는가?
4. find_todo가 반환한 dict수정은 목록에 반영되는가?
5. POST뒤303은 다음 화면의 방식을 어떻게 바꾸는가?

<details>
<summary>풀이</summary>

다르다. 참이므로 원본 누락 검사가 충분하지 않다. 보장하지 않는다. 같은 dict를 가리켜 내용 변경이 반영된다. 새 GET으로 조회하게 한다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 같은 ID로 다시 생성 | 새 예제 거부 | find_todo 중복 확인 |
| 폼에서 name=item 제거 | 새 예제 입력 화면 복귀 | 누락 처리 |
| 수정 뒤 옛 상세 주소 열기 | 새 예제 최신 내용 | ID로 다시 조회 |
| GET 삭제 주소 방문 |405 | POST만 등록 |
| 원본에 같은 ID연속 두 개 | remove반복이 하나를 남길 수 있음 | 인덱스 이동 |

<details>
<summary>막힐 때 확인</summary>

폼 키가 None이면 name을 먼저 본다. 수정이 안 되면 문자열과 정수 ID를 섞었는지 확인한다. 화면에 옛 내용이면 주소의 item과 실제 목록을 구별한다. 같은 항목이 남으면 중복 ID와 반복 중 삭제를 확인한다. 템플릿 li.id표기는 dict키도 읽으므로 서버의 저장 형식부터 본다.

</details>

## 채점과 복습

정상 값만 보지 말고 누락·잘못된 타입·없는 대상의 흐름도 설명한다. 새 예제는 별도 앱에서 확인하며 원본 DB나 외부 서비스의 성공을 대신 주장하지 않는다. TIP 확장은 필수 조건이 아니다. 정의→등록→입력→호출→반환→다음 요청을 연결할 수 있는지 검토한다.
