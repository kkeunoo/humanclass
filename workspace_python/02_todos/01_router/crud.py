from fastapi import APIRouter, Request, Form
from model import TodoItems

crud_router = APIRouter()
# 아래처럼 prefix로 주소 앞 기본값을 설정해준다면, 모두 통일 됨
# crud_router = APIRouter( prefix='/crud' )

todo_list = []

d1 = {
    'id' : 1684,
    'item' : 'item1'
}
todo_list.append(d1)

d2 = {
    'id' : 29681,
    'item' : 'item2'
}
todo_list.append(d2)

# @crud_router.get('/crud/r') # read - select - get방식
# async def todoR(req : Request) :
#     if req.method == 'GET' :
#         data = req.query_params

#         id = data.get('todoID')
#         item = data.get('todoITEM')

#         if todo_list['id'] == id :
#             return f'{id}, {item}'

#     elif req.method == 'POST' :
#         data = await req.form()
#     elif req.method == 'PUT' :
#         data = await req.form()
#     else : 
#         data = await req.form()

@crud_router.post('/crud/c') # create - insert - post방식 / FORM
async def todoC(req : Request) :
    if req.method == 'POST' : # 생략 가능하지만 연습용
        data = await req.form()

        id = data.get('todoID')
        item = data.get('todoITEM')

        todo_list.append({
            'id' : int(id),
            'item' : item
        })
        return todo_list

@crud_router.get('/crud/r') # read - select - get방식 / FORM
async def todoR(todoID : int) :
    print(todoID)
    for todo in todo_list :
        # print(todo)
        # print(todo.get('id') == int(todoID))
        if todo.get('id') == todoID :
            return todo

@crud_router.put('/crud/u') # update - update - put방식 / AJAX
async def todoU(todoID : int, todoITEM : str) :
    for todo in todo_list :
        if todo.get('id') == todoID :
            todo['item'] = todoITEM
            return todo_list

@crud_router.delete('/crud/d') # delete - delete - delete방식 / AJAX
async def todoD(todoID : int) :
    result_todo = []

    for todo in todo_list :
        if todo.get('id') != todoID :
            result_todo.append(todo)

    todo_list[:] = result_todo
    return todo_list

    # todo_list = [ 
    #     todo for todo in todo_list if todo.get('id') != todoID 
    # ]
    # return todo_list

        


    

    




        