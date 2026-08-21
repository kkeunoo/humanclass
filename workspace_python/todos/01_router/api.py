from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from todo import todo_router
from crud import crud_router

app = FastAPI()

# CORS error : 크로스 도메인 에러 해결 코드
app.add_middleware (
    CORSMiddleware,
    # allow_origins는 어디에서 들어오던지 다 허용, IP를 입력하면 해당 IP만 접근할 수 있도록 가능
    # methods(방식_POST,GET등), headers(json등)도 모두 허용하겠다
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def welcome() -> dict: # -> dict는 딕셔너리 형태로 리턴하도록
    return {
        "message" : "Hello World2"
    }

# 불러 온 todo의 todo_router를 app에 추가
# include로 추가하면, 먼저 실행되기 때문에 2 todo가 먼저 프린트 됨
app.include_router(crud_router)
app.include_router(todo_router)

# Request에서 client.host 또는 port를 이용 시 접속 IP/PORT를 알 수 있음
@app.get('/ip')
def test(req : Request) :
    ip = req.client.host
    port = req.client.port
    print(ip)

    return f'당신의 IP/PORT : {ip}, {port}'

@app.get('/err')
def err() :
    print('/err 실행')

    # raise HTTPException 으로 Error를 발생시킬 수 있음
    raise HTTPException(
        status_code = 403,
        detail = '글씨 아무거나 dsadadwdas'
    )

@app.get('/html')
def html():
    return "<h1>Hello World</h1>"

print(1, __name__)

# __name__ 스페셜 변수로 직접 실행되는 main일 때 uvicorn실행
# import로 인해 api.py가 실행 될 때에는 main이 아니기에 실행 안 됨
if __name__ == '__main__' :
    print('api.py 파일 직접 실행')

    # 아래처럼 name이 main인 것을 이용해서 python 실행 시
    # uvicorn 서버가 실행되도록 if문을 작성할 수 있음
    import uvicorn
    # host를 0.0.0.0으로 해주면 다른 호스트도 접근할 수 있게 해줌(기본 값 : localhost)
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")