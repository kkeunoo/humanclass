from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome() -> dict:
    return {'message': 'Hello World2'}

@app.get('/html')
def html():
    return '<h1>hello</h1>'

@app.post('/html')
def html_post():
    return '<h1>hello2</h1>'

@app.get('/no')
def no():
    print('들어왔음')
