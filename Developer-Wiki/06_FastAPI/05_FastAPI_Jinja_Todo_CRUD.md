# 05. 화면 Todo CRUD — 폼의 값이 목록·상세·수정 화면으로 이어지는 길

[FastAPI 목차](README.md) · [읽기 안내](00_FastAPI_상세백과_읽기법.md)

앞에서 따로 배운 폼·리스트·템플릿·리다이렉트를 하나의 작은 앱으로 연결한다. 화면을 만든다는 것은 HTML만 꾸미는 일이 아니다. 어떤 값이 저장되고, 다음 화면은 그 값을 어디에서 다시 읽는지까지 정해야 한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

입력 화면 GET과 저장 POST를 구분한다. 폼 name→문자열 딕셔너리→리스트→템플릿의 연결을 설명한다. 최신 상세 조회·수정 뒤303·삭제 방식·중복 ID·누락과 빈 문자열의 차이를 원본과 개선안으로 나눈다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

CRUD는 생성·조회·수정·삭제다. 이번 앱은 이 작업을 화면의 입력·링크·버튼에 연결한다. 같은 /create라도 GET은 폼을 보여 주고 POST는 입력을 처리한다. 주소만 같다고 같은 실행은 아니다.

| 연결 지점 | 실제 값·역할 | 확인할 질문 |
| --- | --- | --- |
| input의 name | 폼 전송 키 | id·item 이름이 맞나? |
| request.form() | 폼 데이터 | 숫자처럼 보여도 문자열인가? |
| todo_list | 서버 메모리 목록 | 저장 형식이 dict인가 모델인가? |
| 템플릿 문맥 | 화면에 넘길 자료 | list·todo 같은 이름이 맞나? |
| 상세 주소 | 찾아볼 ID | 내용을 주소에서 믿나, 목록에서 찾나? |
|303응답 | 다음 GET을 요청할 주소 | POST 처리와 화면 조회가 나뉘나? |

학생 원본은 {'id':'1','item':'공부'}라는 딕셔너리를 저장하고 강사님은 Todo 모델 객체를 저장한다. Python에서 전자는 키, 후자는 속성을 읽는다. Jinja의 점 표기는 딕셔너리 키도 찾을 수 있어 템플릿의 li.id만 보고 Python 모델이라고 판단하면 안 된다.

목록의 항목을 수정했는데 상세 주소에 옛 item을 붙여 둔다면 그 주소는 최신 저장 상태와 다를 수 있다. 상세 화면은 보통 식별자만 받고 서버의 현재 항목을 다시 찾는 방식이 목적에 맞다. 이번 예제는 그 개선을 담는다. 메모리 목록이므로 서버 재시작 뒤 보존되는 DB는 아니다.

> 📚 **출처 · 본문 설명 확인:** [FastAPI 폼](https://fastapi.tiangolo.com/tutorial/request-forms/), [템플릿](https://fastapi.tiangolo.com/advanced/templates/), [HTTP의 조회용 방식 의미](https://www.rfc-editor.org/rfc/rfc9110.html#name-safe-methods). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-30.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. api.py와 templates의 네 파일을 아래 구조로 저장한다. FastAPI·Uvicorn·Jinja2·python-multipart가 필요하다. 준비된 가상환경에서 api.py 폴더를 열고 `uvicorn api:app --port 8000 --reload`로 실행한다. /create에서 입력을 시작한다. 새 예제는 원본과 같은 문자열 딕셔너리를 사용하지만 공백 정리·중복 거부·현재 상세 조회·POST 삭제·수정 뒤303을 보완했다. 당시 내 제출 코드가 아니다.



**[api.py](실습/책형_복습/05_FastAPI_Jinja_Todo_CRUD/api.py) — 새 예제 전체 파일**

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

**[templates/create.html](실습/책형_복습/05_FastAPI_Jinja_Todo_CRUD/templates/create.html) — 새 예제 전체 파일**

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

**[templates/read.html](실습/책형_복습/05_FastAPI_Jinja_Todo_CRUD/templates/read.html) — 새 예제 전체 파일**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>목록</title></head><body>
<h1>Todo 목록</h1><a href="/create">추가</a>
{% if todos %}<ul>{% for todo in todos %}
<li><a href="/detail/{{ todo.id }}">{{ todo.id }}: {{ todo.item }}</a></li>
{% endfor %}</ul>{% else %}<p>자료가 없습니다.</p>{% endif %}
</body></html>
```

**[templates/detail.html](실습/책형_복습/05_FastAPI_Jinja_Todo_CRUD/templates/detail.html) — 새 예제 전체 파일**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>상세</title></head><body>
{% if todo %}<h1>{{ todo.item }}</h1>
<p>ID {{ todo.id }}</p><a href="/update/{{ todo.id }}">수정</a>
<form method="post" action="/delete/{{ todo.id }}"><button type="submit">삭제</button></form>
{% else %}<p>없는 ID입니다.</p>{% endif %}
<a href="/read">목록</a></body></html>
```

**[templates/update.html](실습/책형_복습/05_FastAPI_Jinja_Todo_CRUD/templates/update.html) — 새 예제 전체 파일**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>수정</title></head><body>
{% if todo %}<form method="post" action="/update">
<input type="hidden" name="id" value="{{ todo.id }}">
<label>내용 <input name="item" value="{{ todo.item }}" required></label>
<button type="submit">수정 완료</button></form>
{% else %}<p>없는 ID입니다.</p>{% endif %}
<a href="/read">목록</a></body></html>
```

처음 목록은 비어 있다. 폼의 id·item이 POST에 들어오면 누락을 빈 문자열로 바꾸고 양끝 공백을 정리한 뒤 저장한다. id는 숫자 변환을 하지 않아 문자열1이다. find_todo는 목록에서 해당 딕셔너리를 반환하므로 수정에서 item을 바꾸면 같은 목록 항목도 바뀐다. 수정 뒤303으로 새 GET목록을 요청한다. 상세는 주소의 item을 사용하지 않고 목록을 다시 찾아 최신 복습을 보여 준다. 삭제는 POST만 등록했으므로 GET으로 열어도 지워지지 않는다.

**요청과 예상 결과:**

| 순서 | 동작 | 상태·자료 |
| --- | --- | --- |
| 시작 | 목록 조회 | 빈 화면 안내 |
| 생성 | ID1·내용공부 | 303→/read, 문자열 dict 한 개 |
| 중복·누락 | 생성 재시도 | 303→/create, 추가 없음 |
| 수정 | ID1·내용복습 | 303→/read |
| 옛 item이 붙은 상세 | /detail/1?item=옛내용 | 현재 복습 표시 |
| GET 삭제 | /delete/1 | 405, 자료 유지 |
| POST 삭제 | /delete/1 | 303→/read, 빈 목록 |

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/04_jinja_todo/api.py` 10–45행 · **원본 발췌**

```python
# Create 페이지 불러오기
@app.get('/create')
def api_create_page(request : Request) :
    print('/create 진입')
    return templates.TemplateResponse(request, 'create.html')

# Create하여 todo_list에 append
@app.post('/create')
async def api_create(request : Request) :
    print('/create 보내기')
    # form으로 id, item 받아옴
    data = await request.form()

    id = data.get('id')
    item = data.get('item')
    print(id, item)
    # 공백일 때를 방지하기 위해 공백이 아닌 경우에 추가
    if id != '' and item != '' :
        print('/create 추가완료')
        todo_list.append({
            'id' : id,
            'item' : item
        })

        # 추가 되었으면 전체 목록 페이지로 이동하도록 구성
        return RedirectResponse(
            url = '/read',
            status_code = 303, # 기본값은 307
        )
    # 공백인 경우 다시 페이지를 리다이렉트하여 다시 입력하도록 구성
    else :
        print('/create 비어있음 다시시도')
        return RedirectResponse(
            url = '/create',
            status_code = 303, # 기본값은 307
        )
```

**발췌 바로 풀이:** 원본은 빈 문자열만 비교한다. name 자체가 없으면 data.get은 None인데 None은 빈 문자열과 달라 조건을 통과한다. 공백 여러 칸도 통과한다. 새 예제는 누락·공백을 먼저 정리하는 보완이다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/04_jinja_todo/api.py` 47–54행 · **원본 발췌**

```python
# Read 페이지 불러오기
@app.get('/read')
def api_read_page(request : Request) :
    print('/read 진입')
    # Read 페이지에서 todo_list를 Jinja로 사용할 수 있도록 구성
    return templates.TemplateResponse(request, 'read.html', {
        'list' : todo_list
    }) 
```
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/04_jinja_todo/api.py` 79–93행 · **원본 발췌**

```python
# Detail 페이지 불러오기
@app.get('/detail')
def api_detail_page(request : Request) :
    print('/detail 진입')
    # print(request.query_params)
    data = request.query_params

    id = data.get('id')
    item = data.get('item')

    # Detail 페이지에서 id와 item을 사용하여 출력할 수 있도록 구성
    return templates.TemplateResponse(request, 'detail.html', {
        'id' : id,
        'item' : item
    })
```

**발췌 바로 풀이:** 원본 상세는 저장 목록을 검색하지 않고 쿼리의 id·item을 그대로 전달한다. 주소의 내용이 현재 목록과 달라도 그 주소 값을 보여 줄 수 있다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/04_jinja_todo/api.py` 56–77행 · **원본 발췌**

```python
# Update 완료 후 Read 페이지 다시 불러오기
@app.post('/read')
async def api_read_update(request : Request) :
    print('/read 수정완료')
    data = await request.form()
    # print(data)

    # Print로 변경 된 값 잘 들어가는지 확인
    id = data.get('id')
    item = data.get('item')
    print('변경값:', id, item)

    # ID가 같을 때 해당 ID의 값 변경
    for todo in todo_list :
        # print(todo['id'])
        if todo['id'] == id :
            todo['item'] = item

    # Read 페이지에서 Update된 List를 사용하여 출력할 수 있도록 구성
    return templates.TemplateResponse(request, 'read.html', {
        'list' : todo_list
    })
```

**발췌 바로 풀이:** 강사님은 수정 화면을 다시 조회한 객체로 채우고, POST에서 같은 `id` 객체의 `item`을 바꾼 뒤 목록으로 리다이렉트한다. 나는 `POST /read`에서 폼의 `id`와 같은 딕셔너리를 찾아 `todo['item']`을 바꾸고 **곧바로 `read.html`을 반환**한다. 내 방식에서는 수정 완료 뒤 주소가 `/read`의 POST 상태에 머문다. 강사님의 303 리다이렉트는 새 GET 목록으로 이동시킨다는 점에서 흐름을 따라가기 쉽다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/04_jinja_todo/api.py` 111–126행 · **원본 발췌**

```python
@app.get('/delete/{id}')
async def api_delete_page(id) :
    print('/delete 진입')
    print(id)
    # data = await request.form()
    # print(data)

    for todo in todo_list :
        if todo['id'] == id :
            todo_list.remove(todo)
            print('/delete 삭제완료')

    return RedirectResponse(
        url = '/read',
        status_code = 303, # 기본값은 307
    )
```

**발췌 바로 풀이:** 반복 중 같은 리스트에서 remove하면 뒤 항목의 위치가 당겨진다. 같은 ID가 연속 중복된 원본 자료에서는 일부를 건너뛸 수 있다. GET 삭제와 별개인 목록 변경 문제다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/04_jinja_todo/api.py` 1–8행 · **원본 발췌**

```python
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

todo_list = []
```
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/04_jinja_todo/api.py` 95–109행 · **원본 발췌**

```python
@app.post('/update')
async def api_update_page(request : Request) :
    print('/update 진입')
    data = await request.form()
    # print(await request.form())
    print(data)

    id = data.get('id')
    item = data.get('item')
    print(id, item)

    return templates.TemplateResponse(request, 'update.html', {
        'id' : id,
        'item' : item
    })
```

**발췌 바로 풀이:** 빠져 있던 실제 수정 화면 함수 정의다. 폼으로 받은 id·item을 그대로 update.html에 넘기며 현재 목록을 다시 찾지 않는다. 수정 화면의 값과 저장 원본의 신뢰 범위를 구별한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/04_jinja_todo/templates/read.html` 116–145행 · **원본 발췌**

```html
    </div>
</body>
</html>
```

내 실제 생성은 문자열 dict를 쓰고 빈 문자열이면 입력 화면으로 돌려보낸다. 목록 화면은 list라는 문맥 이름으로 todo_list를 받는다. 상세와 수정 준비 화면은 전달된 item을 그대로 보여 주고, 수정 저장은 ID가 같은 목록 항목들을 바꾼 뒤 곧바로 HTML을 반환한다. 새로고침하면 POST 재전송을 물을 수 있는 흐름이다. 내 삭제는 GET과 반복 중 remove, 강사님은 POST와 pop 후 break다. 둘의 삭제 개수 정책도 중복 ID 상황에서 확인해야 한다.

<a id="connections"></a>

## 5. import·함수·화면·저장이 연결되는 흐름

create.html의 name → POST /create → request.form → todo_list.append →303의Location → GET /read → read.html 반복 → ID 링크 → 상세 함수 → 현재 항목 → detail.html이다. 수정은 숨은 id입력과 item입력 → POST /update → find_todo → dict 변경 →303 → 목록이다. 새 helper find_todo의 전체 정의를 위에 실었다. 원본 강사님이 import한 Todo는 todo.py에서 id:int·item:str을 정의한 모델이며 학생 원본에는 이 모델 import가 없다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 앱은 생성·목록·상세·수정·삭제 페이지를 직접 연결하고 입력 실패의 돌아갈 경로도 만들었다. **실제 한계:** 빈 문자열 검사만으로 누락·공백은 잡지 못하고, 상세 주소가 최신 자료의 근거가 되지 않는다. **개선:** 현재 목록 조회와 수정 뒤303은 강사님 방식이 목적에 더 맞다. **삭제:** 주소 방문만으로 변경되는 GET보다 POST로 요청 의도를 나누는 편이 적절하다. 새 예제는 중복 ID도 거부하지만 입력 오류 사유 안내·로그인 분리·ID에 들어갈 URL 특수문자 정책은 단순화했다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_python/todos/04_jinja_todo/api.py` 49–67행 · **원본 발췌**

```python
@app.get('/detail/{id}')
def detail(request: Request, id:int):
    print('/detail/{id} 실행')
    print('id:', id)

    result = None
    for todo in todo_list:
        print(todo)
        if todo.id == id:
            result = todo

    print('result', result)
    return templates.TemplateResponse(
        request, 
        'detail.html',
        {
            'todo': result
        }
    )
```

출처: `D:/workspace_teacher/workspace_python/todos/04_jinja_todo/api.py` 69–102행 · **원본 발췌**

```python
@app.get('/update')
def detail(request: Request, id:int):
    print('/update')
    print('id', id)

    result = None
    for todo in todo_list:
        print(todo)
        if todo.id == id:
            result = todo

    print('result', result)
    return templates.TemplateResponse(
        request, 
        'update.html',
        {
            'todo': result
        }
    )

@app.post('/api/update')
def apiAdd(todo:Todo = Form()):
    print('/api/update 실행')
    print('todo:', todo)

    for t in todo_list:
        if t.id == todo.id:
            t.item = todo.item

    return RedirectResponse(
        # url='/detail/'+todo.id,
        url='/list',
        status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
    )
```

저장 객체를 다시 조회하는 상세와 수정 후303부분만 필요한 비교로 인용한다. 강사님은 경로 id:int와 Todo.id를 맞춰 검색한다. 내 문자열 dict와는 자료형까지 다르므로 코드를 그대로 붙이면 안 된다. 새 개선 예제는 학생의 문자열 저장을 유지한 채 조회·응답 흐름만 보완했다. 강사님 삭제도 중복 ID를 모두 지우는 코드가 아니라 첫 일치 후break라는 점을 분명히 한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 값 | 원본 학생 | 원본 강사님 | 새 예제 |
| --- | --- | --- | --- |
| id1 | 문자열 | 모델 정수 | 문자열 |
| 내용 위치 | dict키 | 모델속성 | dict키 |
| 상세 근거 | 주소 item | 목록 조회 | 목록 조회 |
| 수정 뒤 | POST의HTML |303GET |303GET |
| 삭제 | GET·remove | POST·pop/break | POST·남길 목록 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 같은 ID로 다시 생성 | 새 예제 거부 | find_todo 중복 확인 |
| 폼에서 name=item 제거 | 새 예제 입력 화면 복귀 | 누락 처리 |
| 수정 뒤 옛 상세 주소 열기 | 새 예제 최신 내용 | ID로 다시 조회 |
| GET 삭제 주소 방문 |405 | POST만 등록 |
| 원본에 같은 ID연속 두 개 | remove반복이 하나를 남길 수 있음 | 인덱스 이동 |

폼 키가 None이면 name을 먼저 본다. 수정이 안 되면 문자열과 정수 ID를 섞었는지 확인한다. 화면에 옛 내용이면 주소의 item과 실제 목록을 구별한다. 같은 항목이 남으면 중복 ID와 반복 중 삭제를 확인한다. 템플릿 li.id표기는 dict키도 읽으므로 서버의 저장 형식부터 본다.

**확인 범위:** 새 앱을 별도 임시 폴더에 복사해 프레임워크 요청·응답 흐름으로 확인한다. 실제 외부 서비스·운영 DB·브라우저 공개 서버에 요청한 결과와 구별한다. 원본 전체 앱을 무조건 실행하지 않으며 별도 확인한 원본 구간은 검증 보고서에 기록한다. 사용자의 가상환경은 검사에 읽기만 사용하고 파일을 설치·수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 로그인별 저장소·영구 DB·변경 사유 안내·URL 인코딩·CSRF보호·정교한 상태 코드·동시 요청 제어는 추가 학습이다. 새 예제의 POST변경만으로 인증·보안이 완성됐다고 설명하지 않는다. 원래 목록 공유와 재시작 소실은 다음 SQLite·DB본문으로 이어진다.

request.headers 직접 읽기와 response_model은 미학습으로 확인된 선택 확장이다. 본문에서 이 기능을 선행 조건으로 요구하지 않는다. 응답·입력 타입 표시와 response_model 설정도 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 폼 문자열1과 모델 정수1은 같은 자료형인가?
2. None != 빈 문자열은 참인가?
3. 상세에서 주소 item을 믿으면 최신 값을 보장하는가?
4. find_todo가 반환한 dict수정은 목록에 반영되는가?
5. POST뒤303은 다음 화면의 방식을 어떻게 바꾸는가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

다르다. 참이므로 원본 누락 검사가 충분하지 않다. 보장하지 않는다. 같은 dict를 가리켜 내용 변경이 반영된다. 새 GET으로 조회하게 한다.

</details>

| 복습 지점 | 질문 |
| --- | --- |
| 입력 | name·누락·빈값·공백 |
| 저장 | dict·모델·ID형 |
| 조회 | 주소값인가현재자료인가 |
| 변경 | POST·반환·다음GET |

[장별 연습문제](실습/연습문제/05_FastAPI_Jinja_Todo_CRUD_연습문제.md) · 다음은 [Python SQLite](06_Python_SQLite와_Transaction.md)다.
