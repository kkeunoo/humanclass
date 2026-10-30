from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/step1')
def step1(request: Request):
    return {'item': request.query_params.get('item')}

@app.get('/direct')
def direct(request: Request):
    return step1(request)

@app.get('/drop')
def drop(request: Request):
    step1(request)

@app.post('/go')
def go():
    return RedirectResponse(url='/step1', status_code=303)

@app.post('/keep')
def keep():
    return RedirectResponse(url='/step1', status_code=307)

@app.get('/carry')
def carry(request: Request):
    item = request.query_params.get('item')
    return RedirectResponse(url='/step1?item=' + str(item), status_code=307)
