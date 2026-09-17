# pin install fastapi jinja2 uvicorn
from fastapi import FastAPI, Cookie, Request, Response
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

# Cookie는 서버 접속 시 IP정보 등 모두 들고 가기에 form으로 보냈던 것 등과 다름
@app.get('/main')
def main(
    request: Request,
    response: Response,
    # Cookie는 지워질 수 있기에 None으로 해두면 좋음(단, 인증같은 필요 시 필수)
    # js에서 no, yes 쿠키를 넣어놓고 아래처럼 전달인자로 받을 수 있음
    no: str | None = Cookie(None), 
    yes: Annotated[str|None, Cookie()] = None
):
    print('no : ', no)
    print('yes : ', yes)

    # 아래처럼 response에 Jinja와 쿠키값까지 같이 리턴
    response = templates.TemplateResponse(request, 'main.html')

    response.set_cookie(
        key='key',
        value='value'
    )

    response.set_cookie(
        key='key2',
        value='value2',
        max_age=10 # 10초 후 만료
    )

    # httponly=True를 주면 js에서 수정하지 못하게 할 수 있음
    response.set_cookie(
        key='key3',
        value='value3',
        max_age=1000,
        httponly=True
    )

    # 이렇게 return을 하면 다른 response 객체이기 때문에, 위 response가 안 먹힘
    # 하여 response에 따로 TemplateResponse를 담아 return
    # return templates.TemplateResponse(request, 'main.html')
    return response

# py에서는 아래처럼 cookie를 삭제할 수 있으나 많이 사용하진 않음
@app.get('/delete/cookie')
def delete_cookie(response: Response):
    response.delete_cookie('key3')
    return '{"message" : "쿠키 key3 삭제 완료"}'
    

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('cookie:app', port=8000, reload=True, host="0.0.0.0")