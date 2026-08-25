from fastapi import APIRouter, Form, Request, Depends
from pydantic import BaseModel

crud_router = APIRouter()

todo_list = []

class Todo(BaseModel) :
    id : int = -1
    item : str = ''

@crud_router.post('/practice/c')
def crud_api_c(todo : Todo) :
    print('/practice/c 실행')
    print(todo)
    todo_list.append(todo)
    return todo

@crud_router.get('/practice/r')
def crud_api_r() :
    print('/practice/r 실행')
    print(todo_list)
    return todo_list

@crud_router.get('/practice/r/{id}')
def crud_api_detail(id : int) :
    print('/practice/r/id')

    result = None
    for todo in todo_list:
        if todo.id == id:
            print(todo)
            result = todo

    return result