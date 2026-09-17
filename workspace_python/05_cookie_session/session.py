# pip install itsdangerous

from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware

from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key='Human1234$'
)
templates = Jinja2Templates(directory='templates/')

# 주소중에 /static으로 시작한다면, 해당 directory에서 찾아라 라는 기능
app.mount(
    "/static", # URL 경로
    StaticFiles(directory="static"), # 실제 폴더 명
    name="static" # Jinja에서 사용할 이름
)

# /login을 가면 로그인을 했다는 가정 하에 실습
@app.get('/login')
def login(request: Request):
    # 세션 저장 (브라우저마다 따로 관리되는)
    request.session['isLogin'] = True
    request.session['id'] = "admin"

@app.get('/mypage')
def mypage(request: Request):
    isLogin = request.session.get('isLogin', None) # None은 get기본값
    loginID = request.session.get('id', None)

    # 아래처럼 session을 설정해서 바로 mypage에 갈 경우 접근이 불가하고,
    # login 경로로 가서 session을 얻어 오면 접근 가능하도록 설정
    if isLogin is None :
        return "로그인 하세요"
    else :
        return f"ID: [{loginID}] 님 비밀스러운 공간에 오신 걸 환영합니다"

# session을 clear해주면서 logout되도록 사용할 수 있음
@app.get('/logout')
def logout(request: Request):
    # invalidate
    # clear를 했을 때 session 캐비넷을 아예 없애고, 다시 들어가면 새로운 캐비넷이 나옴
    request.session.clear()

    return "로그아웃"

# request로 Jinja에 return해주면 jinja.html에서도 request로 그대로 사용할 수 있음
@app.get('/')
def home(request: Request):
    return templates.TemplateResponse(request, 'main.html')

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('session:app', port=8000, reload=True, host="0.0.0.0")