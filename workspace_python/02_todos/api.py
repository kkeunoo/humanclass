from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome() -> dict:
    return {
        "message" : "Hello World2"
    }

# post일 때 127.0.0.1:60114 - "GET /html HTTP/1.1" 405 Method Not Allowed 발생
# 주소창에 기존에 배운 form과 ajax 빼고는 post로 보낼 수 없음
# 원래 위와 같으면 에러가 나야하는데, 동작은 됨
# 다만, 주소와 방식이 같은것이 있다면 먼저 선언한 것만 실행된다
# 아래처럼 get, post 방식이 다르면 동작이 가능하며 주소 1개로 4개방식을 사용 가능
@app.get("/html")
def html():
    return "<h1>hello</h1>"
# @app.get("/html")
# def html2():
#     return "<h1>hello2</h1>"
@app.post("/html")
def html2():
    return "<h1>hello2</h1>"


# 원래 return이 없어 404에러가 떠야 하지만, fastapi 한정으로 null로 응답해줌
@app.get("/no")
def no():
    print('들어왔음')