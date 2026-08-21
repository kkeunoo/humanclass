from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

todo_list = []

# Create 페이지 불러오기
@app.get('/create')
def api_create_page(request : Request) :
    print('/create 진입')
    return templates.TemplateResponse(request, 'create.html')

# Create하여 todo_list에 append
@app.post('/create')
async def api_create(request : Request) :
    print('/create 보내기')
    # form으로 id, item 받아옴
    data = await request.form()

    id = data.get('id')
    item = data.get('item')
    print(id, item)
    # 공백일 때를 방지하기 위해 공백이 아닌 경우에 추가
    if id != '' and item != '' :
        print('/create 추가완료')
        todo_list.append({
            'id' : id,
            'item' : item
        })

        # 추가 되었으면 전체 목록 페이지로 이동하도록 구성
        return RedirectResponse(
            url = '/read',
            status_code = 303, # 기본값은 307
        )
    # 공백인 경우 다시 페이지를 리다이렉트하여 다시 입력하도록 구성
    else :
        print('/create 비어있음 다시시도')
        return RedirectResponse(
            url = '/create',
            status_code = 303, # 기본값은 307
        )

# Read 페이지 불러오기
@app.get('/read')
def api_read_page(request : Request) :
    print('/read 진입')
    # Read 페이지에서 todo_list를 Jinja로 사용할 수 있도록 구성
    return templates.TemplateResponse(request, 'read.html', {
        'list' : todo_list
    }) 

# Update 완료 후 Read 페이지 다시 불러오기
@app.post('/read')
async def api_read_update(request : Request) :
    print('/read 수정완료')
    data = await request.form()
    # print(data)

    # Print로 변경 된 값 잘 들어가는지 확인
    id = data.get('id')
    item = data.get('item')
    print('변경값:', id, item)

    # ID가 같을 때 해당 ID의 값 변경
    for todo in todo_list :
        # print(todo['id'])
        if todo['id'] == id :
            todo['item'] = item

    # Read 페이지에서 Update된 List를 사용하여 출력할 수 있도록 구성
    return templates.TemplateResponse(request, 'read.html', {
        'list' : todo_list
    })

# Detail 페이지 불러오기
@app.get('/detail')
def api_detail_page(request : Request) :
    print('/detail 진입')
    # print(request.query_params)
    data = request.query_params

    id = data.get('id')
    item = data.get('item')

    # Detail 페이지에서 id와 item을 사용하여 출력할 수 있도록 구성
    return templates.TemplateResponse(request, 'detail.html', {
        'id' : id,
        'item' : item
    })

@app.post('/update')
async def api_update_page(request : Request) :
    print('/update 진입')
    data = await request.form()
    # print(await request.form())
    print(data)

    id = data.get('id')
    item = data.get('item')
    print(id, item)

    return templates.TemplateResponse(request, 'update.html', {
        'id' : id,
        'item' : item
    })

@app.get('/delete/{id}')
async def api_delete_page(id) :
    print('/delete 진입')
    print(id)
    # data = await request.form()
    # print(data)

    for todo in todo_list :
        if todo['id'] == id :
            todo_list.remove(todo)
            print('/delete 삭제완료')

    return RedirectResponse(
        url = '/read',
        status_code = 303, # 기본값은 307
    )

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")