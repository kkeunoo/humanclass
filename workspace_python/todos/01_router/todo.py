from fastapi import APIRouter, Form, Request

todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo')
# add_todo(todo: dict) 는 딕셔너리로 타입 지정하는 것
async def add_todo(todo: dict) -> dict :
    print('todo:', todo)
    todo_list.append(todo)
    return {
        "message" : "정상적으로 추가되었습니다."
    }

@todo_router.get('/todo')
async def retrieve_todos() -> dict :
    return {
        "todos" : todo_list
    }

# 인자값과, form에 name이 같을 경우 값을 쉽게 받을 수 있음
@todo_router.get('/todo/param')
# async def todoParamGet(id, item) -> dict :
async def todoParamGet(id : int, item : str = '') -> dict : # int로 지정하고 문자열을 넣었을 경우 422 Unprocessable Content 발생
    # item은 있지만 입력하지 않을 경우 ""빈 값이 들어가기 때문에 item자체가 안 들어왔다면 올바른 경로로 접근하지 않았을 수 있음
    # id는 int이기 때문에 빈 값일 때 ""가 들어가면 형변환이 안되어 에러 발생
    print(id, item) 
    return {
        "id" : id,
        "item" : item # 또는, 인자값이 2개지만 form에서 item을 없앴을 경우 값이 안 맞는다는 에러 발생
    }

# form에서 받으려면 fastspi Form을 import후 기본값을 Form()으로 지정
@todo_router.post('/todo/param')
async def todoParamPost(id : int = Form(), item : str = Form()) -> dict : 
    print(id, item) 
    return {
        "id" : id,
        "item" : item 
    }

# 아래처럼 Request를 import해서 사용할 수도 있음(POST일 때)
@todo_router.get('/todo/param2') # 조회
@todo_router.post('/todo/param2') #행동, 3개를 통틀어 사용하기도 함 form만 get,post지원, AJAX는 4개 모두 지원
@todo_router.put('/todo/param2')
@todo_router.delete('/todo/param2')
# 아래처럼 method를 받으면 get, post 두 가지 방식 모두 사용할 수 있음
async def todoParam(req: Request) -> dict : 
    if req.method == 'GET' :
        data = req.query_params
    else :
        data = await req.form()

    id = data.get('id')
    item = data.get('item')
    print(id, item, req.method) # POST method를 가져옴

    return {
        "id" : id,
        "item" : item 
    }


print(2, __name__)#
if __name__ == '__main__' :
    print('todo.py 파일 직접 실행')