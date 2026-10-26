# 05. Jinja Todo — 화면에서 목록 만들고 고치기

[FastAPI 목차](README.md) · [이전: 응답과 리다이렉트](04_FastAPI_Response_Redirect_의존성주입.md) · [다음: SQLite](06_Python_SQLite와_Transaction.md)

이전 장의 리스트 CRUD를 **HTML 화면과 폼**에 연결한 수업이다. 강사님은 `Todo` 모델 객체를 리스트에 넣고, 나는 폼에서 꺼낸 `id`, `item` 문자열을 **딕셔너리**에 담았다. 두 저장 형태가 달라서 조회·수정 코드도 다르다. 둘 다 메모리 리스트이며 데이터베이스 저장은 아직 아니다.

## 1. 입력 화면과 생성 처리

### 강사님 코드

출처: `teacher/workspace_python/todos/04_jinja_todo/api.py` 29–47행 · **원본 발췌**

```python
@app.get('/add')
def add(request: Request) :
    print('/add 실행')
    return templates.TemplateResponse(
        request, 
        'add.html'
    )

@app.post('/api/add')
def apiAdd(todo:Todo = Form()):
    print('/api/add 실행')
    print('todo:', todo)

    todo_list.append(todo)

    return RedirectResponse(
        url='/list',
        status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
    )
```

### 내 코드

출처: `me/workspace_python/02_todos/04_jinja_todo/api.py` 10–45행 · **원본 발췌**

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

강사님은 `GET /add`로 화면을 보여 주고 `POST /api/add`에서 `Todo = Form()`으로 값을 받아 저장한다. 나는 `GET /create`와 `POST /create`를 나누고 `await request.form()`에서 직접 값을 꺼낸다. 입력이 빈 문자열이면 다시 입력 화면으로 보내는 분기도 내 코드에 있다. **강사님은 모델 필드를 사용**하고 **나는 문자열 딕셔너리를 사용**한다. 두 코드 모두 저장 후 `303`으로 목록 페이지에 새 GET 요청을 보낸다.

## 2. 목록과 상세 화면

### 강사님 코드

출처: `teacher/workspace_python/todos/04_jinja_todo/api.py` 17–27행 · **원본 발췌**

```python
@app.get('/list')
def list(request: Request) :
    print('/list')

    return templates.TemplateResponse(
        request, 
        'list.html',
        {
            'list': todo_list
        }
    )
```

출처: `teacher/workspace_python/todos/04_jinja_todo/api.py` 49–67행 · **원본 발췌**

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

### 내 코드

출처: `me/workspace_python/02_todos/04_jinja_todo/api.py` 47–54행 · **원본 발췌**

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

출처: `me/workspace_python/02_todos/04_jinja_todo/api.py` 79–93행 · **원본 발췌**

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

강사님 `/detail/{id}`는 서버의 `todo_list`에서 **해당 ID를 다시 찾아** `detail.html`에 보낸다. 내 `/detail?id=...&item=...`은 **주소에서 받은 `id`, `item`을 그대로 화면에 넘긴다**. 목록에서 항목이 수정된 뒤 옛 주소를 열면 내 상세 화면은 최신 저장 값을 보장하지 않는다. 여기서는 강사님 조회 방식이 실제 저장 상태와 더 잘 맞는다. 내 코드는 목록을 전달하는 `read.html` 화면과 쿼리값을 보여 주는 `detail.html`을 분리해 연습했다.

## 3. 수정 화면과 수정 처리

### 강사님 코드

출처: `teacher/workspace_python/todos/04_jinja_todo/api.py` 69–102행 · **원본 발췌**

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

### 내 코드

출처: `me/workspace_python/02_todos/04_jinja_todo/api.py` 56–77행 · **원본 발췌**

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

강사님은 수정 화면을 다시 조회한 객체로 채우고, POST에서 같은 `id` 객체의 `item`을 바꾼 뒤 목록으로 리다이렉트한다. 나는 `POST /read`에서 폼의 `id`와 같은 딕셔너리를 찾아 `todo['item']`을 바꾸고 **곧바로 `read.html`을 반환**한다. 내 방식에서는 수정 완료 뒤 주소가 `/read`의 POST 상태에 머문다. 강사님의 303 리다이렉트는 새 GET 목록으로 이동시킨다는 점에서 흐름을 따라가기 쉽다.

## 4. 삭제 처리

### 강사님 코드

출처: `teacher/workspace_python/todos/04_jinja_todo/api.py` 104–118행 · **원본 발췌**

```python
@app.post('/api/delete')
def apiAdd(todo:Todo = Form()):
    print('/api/delete 실행')
    print('todo:', todo)

    for i in range(len(todo_list)) :
        if todo_list[i].id == todo.id:
            todo_list.pop(i)
            break

    return RedirectResponse(
        # url='/detail/'+todo.id,
        url='/list',
        status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다
    )
```

### 내 코드

출처: `me/workspace_python/02_todos/04_jinja_todo/api.py` 111–126행 · **원본 발췌**

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

강사님은 `POST /api/delete`에서 `id`가 같은 모델 객체를 찾아 리스트에서 제거한다. 나는 `GET /delete/{id}`에서 딕셔너리를 찾아 제거한다. 둘 다 실제 원본이지만, **목록을 바꾸는 삭제를 GET 경로로 열 수 있는 내 방식**은 주소 방문만으로 삭제가 일어나는 문제가 있다. 이 작업에는 강사님의 POST 방식이 더 적절하다. 두 코드는 삭제 뒤 303으로 목록을 다시 요청한다.

## 직접 확인할 질문

1. 강사님 목록의 항목과 내 목록의 항목은 각각 어떤 자료형인가?
2. 내 상세 화면은 저장된 최신 값을 다시 조회하는가?
3. 내 삭제 경로를 주소창에서 열면 왜 항목이 없어질 수 있는가?

## 추가로 알면 좋은 것

로그인별 목록 분리, 영구 저장, 중복 ID 검사, 삭제 전 확인 화면은 이 Todo 실습에 구현되지 않았다. 다음 장의 SQLite부터 **메모리와 파일 저장의 차이**를 배운다.
