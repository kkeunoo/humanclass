from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from todo import todo_router

app = FastAPI()

app.add_middleware (
    CORSMiddleware,
    # allow_origins는 어디에서 들어오던지 다 허용, IP를 입력하면 해당 IP만 접근할 수 있도록 가능
    # methods(방식), headers(json등)도 모두 허용하겠다
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def welcome() -> dict:
    return {
        "message" : "Hello World2"
    }

# 불러 온 todo의 todo_router를 app에 추가
# include로 추가하면, 먼저 실행되기 때문에 2 todo가 먼저 프린트 됨
app.include_router(todo_router)

print(1, __name__)

if __name__ == '__main__' :
    print('api.py 파일 직접 실행')

    # 아래처럼 name이 main인 것을 이용해서 python 실행 시
    # uvicorn 서버가 실행되도록 if문을 작성할 수 있음
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True)