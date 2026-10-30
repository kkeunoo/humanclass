from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import RedirectResponse
from todo_service import find_todo, rename_todo

app = FastAPI()

@app.get('/todos/{todo_id}')
def read_todo(todo_id: int):
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail='없는 ID')
    return todo

@app.post('/todos/update')
def update_todo(todo_id: int = Form(), item: str = Form()):
    changed = rename_todo(todo_id, item)
    if not changed:
        raise HTTPException(status_code=404, detail='없는 ID')
    return RedirectResponse(f'/todos/{todo_id}', status_code=303)
