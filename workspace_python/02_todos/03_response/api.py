from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/step1')
def step1(request : Request) :
    print('/step1 실행')
    data = request.query_params
    item = data.get('item')
    print(f'item : {item}')

    print('너무 복잡하고 정교해서 복붙하기 좀 그런 곳')

@app.get('/step2')
def step2(request : Request) :
    print('/step2 실행')
    data = request.query_params
    item = data.get('item')
    print(f'item : {item} 관련 일처리는 끝났고')

    print('step1으로 이동')
    # 1. forward 방식
    step1(request)

from fastapi.responses import RedirectResponse
@app.get('/step3')
def step3(request : Request) :
    print('/step3 실행')
    data = request.query_params
    item = data.get('item')
    print(f'item : {item} 관련 일처리는 끝났고')

    print('step1으로 이동')
    # 2. redirect 방식
    return RedirectResponse(
        url = '/step1?item='+str(item),
        status_code = 307, # 기본값은 307
    )

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")




