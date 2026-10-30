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
