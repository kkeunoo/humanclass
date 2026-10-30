from fastapi import FastAPI, Request, Response, Cookie
from fastapi.responses import RedirectResponse, FileResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
PUBLIC_PATHS = ['/login', '/popup', '/cookie/set', '/cookie/read', '/cookie/delete']

@app.middleware('http')
async def login_check(request: Request, call_next):
    if request.url.path in PUBLIC_PATHS:
        return await call_next(request)
    if not request.session.get('isLogin'):
        return RedirectResponse('/login', status_code=302)
    return await call_next(request)

# This key is only for this standalone local exercise.
app.add_middleware(SessionMiddleware, secret_key='book-demo-signing-key-for-local-practice')

@app.get('/popup')
def popup():
    return FileResponse('cookie.html')

@app.get('/cookie/set')
def set_cookie(response: Response):
    response.set_cookie('key2', 'value2', max_age=10)
    response.set_cookie('key3', 'value3', max_age=1000, httponly=True)
    return {'message': '쿠키 설정'}

@app.get('/cookie/read')
def read_cookie(key3: str | None = Cookie(None)):
    return {'key3': key3}

@app.get('/cookie/delete')
def delete_cookie(response: Response):
    response.delete_cookie('key3')
    return {'message': '쿠키 삭제'}

@app.get('/login')
def login(request: Request):
    request.session['isLogin'] = True
    request.session['id'] = 'practice'
    return {'message': '실습 상태 저장'}

@app.get('/mypage')
def mypage(request: Request):
    return {'id': request.session.get('id')}

@app.get('/logout')
def logout(request: Request):
    request.session.clear()
    return {'message': '실습 상태 삭제'}
