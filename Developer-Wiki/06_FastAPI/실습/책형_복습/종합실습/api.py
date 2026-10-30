from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import store

app = FastAPI()
templates = Jinja2Templates(directory='templates')
store.prepare()

@app.get('/create')
def create_page(request: Request):
    return templates.TemplateResponse(request, 'create.html')

@app.post('/create')
def create(todo_id: int = Form(), item: str = Form()):
    item = item.strip()
    if not item or store.find(todo_id) is not None:
        return RedirectResponse('/create', status_code=303)
    store.create(todo_id, item)
    return RedirectResponse('/read', status_code=303)

@app.get('/read')
def read(request: Request):
    return templates.TemplateResponse(request, 'read.html', {'todos': store.list_all()})

@app.get('/detail/{todo_id}')
def detail(request: Request, todo_id: int):
    todo = store.find(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail='없는 ID')
    return templates.TemplateResponse(request, 'detail.html', {'todo': todo})

@app.get('/update/{todo_id}')
def update_page(request: Request, todo_id: int):
    todo = store.find(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail='없는 ID')
    return templates.TemplateResponse(request, 'update.html', {'todo': todo})

@app.post('/update')
def update(todo_id: int = Form(), item: str = Form()):
    if store.find(todo_id) is None:
        raise HTTPException(status_code=404, detail='없는 ID')
    if item.strip():
        store.rename(todo_id, item.strip())
    return RedirectResponse(f'/detail/{todo_id}', status_code=303)

@app.post('/delete/{todo_id}')
def delete(todo_id: int):
    store.delete(todo_id)
    return RedirectResponse('/read', status_code=303)
