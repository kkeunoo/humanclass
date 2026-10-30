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
