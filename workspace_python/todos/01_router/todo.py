from fastapi import APIRouter, Form, Request
from model import Todo

todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo')
# add_todo(todo: dict) 는 딕셔너리로 타입 지정하는 것
async def add_todo(todo: dict) -> dict :
    print('todo:', todo)
    todo_list.append(todo)
    return { # post또는 get으로 요청을 준 client에게 돌려주는 return 값
        "message" : "정상적으로 추가되었습니다."
    }

@todo_router.get('/todo')
async def retrieve_todos() -> dict :
    return {
        "todos" : todo_list
    }

# 인자값과, form에 name이 같을 경우 값을 쉽게 받을 수 있음
@todo_router.get('/todo/param')
# async def todoParamGet(id, item) -> dict :
async def todoParamGet(id : int, item : str = '') -> dict : # int로 지정하고 문자열을 넣었을 경우 422 Unprocessable Content 발생
    # item은 있지만 입력하지 않을 경우 ""빈 값이 들어가기 때문에 item자체가 안 들어왔다면 올바른 경로로 접근하지 않았을 수 있음
    # id는 int이기 때문에 빈 값일 때 ""가 들어가면 형변환이 안되어 에러 발생
    print(id, item) 
    return {
        "id" : id,
        "item" : item # 또는, 인자값이 2개지만 form에서 item을 없앴을 경우 값이 안 맞는다는 에러 발생
    }

# form에서 받으려면 fastspi Form을 import후 기본값을 Form()으로 지정
@todo_router.post('/todo/param')
async def todoParamPost(id : int = Form(), item : str = Form()) -> dict : 
    print(id, item) 
    return {
        "id" : id,
        "item" : item 
    }

# 아래처럼 Request를 import해서 사용할 수도 있음(POST일 때)
@todo_router.get('/todo/param2') # 조회
@todo_router.post('/todo/param2') #행동, 3개를 통틀어 사용하기도 함 form만 get,post지원, AJAX는 4개 모두 지원
@todo_router.put('/todo/param2')
@todo_router.delete('/todo/param2')
# 아래처럼 method를 받으면 get, post 두 가지 방식 모두 사용할 수 있음
# req: Request = req의 형태가 Request로
async def todoParam(req: Request) -> dict : 
    if req.method == 'GET' :
        data = req.query_params
    else :
        data = await req.form()

    id = data.get('id')
    item = data.get('item')
    print(id, item, req.method) # POST method를 가져옴

    return {
        "id" : id,
        "item" : item 
    }

'''
문제 1
브라우저에서
- input에 몇 단입력
파이썬에서
- 해당 구구단의 단 출력
'''
@todo_router.get('/problem/99')
async def problemGet(problem_99 : int) : 
    print(problem_99) 

    result = ''
    if 2 <= problem_99 <= 9 :
        for i in range(1,10) :
            problemResult = problem_99 * i 
            result += f'{problem_99} x {i} = {problemResult} '
    else :
        return f'2단부터 9단까지만 입력해주세요.'
    print(result)
    return result

'''
문제 2
클라이언트에서
- 숫자 두 개를 입력
파이썬에서
- 두 개의 합을 출력
'''
@todo_router.get('/problem/plus')
async def problemGet(problem_plus1 : int, problem_plus2 : int) : 
    print(problem_plus1 + problem_plus2)
    result = problem_plus1 + problem_plus2
    return result

'''
문제 3
웹에서
- 숫자 2개와 연산자를 입력
- 2, "-", 3
파이썬에서
- 결과 출력
- 화면에도 출력
'''
@todo_router.get('/problem/calc')
async def problemGet(problem_calc1 : int, problem_calc2 : int, problem_calc3) : 
    result = 0
    print(problem_calc1, type(problem_calc1))
    print(problem_calc2, type(problem_calc2))
    print(problem_calc3, type(problem_calc3))

    # operator = str(problem_calc3)
    if problem_calc3 == '-' :
        result = problem_calc1 - problem_calc2
    elif problem_calc3 == '+' :
        result = problem_calc1 + problem_calc2
    elif problem_calc3 == '%' :
        result = problem_calc1 % problem_calc2
    elif problem_calc3 == '/' :
        result = problem_calc1 / problem_calc2
    elif problem_calc3 == '*' :
        result = problem_calc1 * problem_calc2
    else :
        return f'- , + , % , / , * 만 입력하세요.'
    print(result)
    return result

@todo_router.get('/problem/practice')
async def problemGet(problem_practice) :
    value = []
    value.append(problem_practice)

    try:
        valueSplit = ''.join(value).split(';')
        valueSplit[0] = int(valueSplit[0])
        valueSplit[1] = int(valueSplit[1])
        valueSplit[2] = str(valueSplit[2])

        result = 0
        if valueSplit[2] == '-' :
            result = valueSplit[0] - valueSplit[1]
        elif valueSplit[2] == '+' :
            result = valueSplit[0] + valueSplit[1]
        elif valueSplit[2] == '*' :
            result = valueSplit[0] * valueSplit[1]
        elif valueSplit[2] == '/' :
            result = valueSplit[0] / valueSplit[1]
        elif valueSplit[2] == '%' :
            result = valueSplit[0] % valueSplit[1]
        else :
            return f'연산자는 - , + , % , / , * 만 입력하세요.'

        return result
    except :
        return f'연산자를 정확히 입력하세요.'
    
    # print(value)
    # print(valueSplit)
    # print(result)

# FastAPI 43P 실습자료기에 /todo43
@todo_router.post('/todo43')
@todo_router.get('/todo43')
def add_todo43(todo: Todo) -> dict :
    print(f'todo: {todo}')
    todo_list.append(todo)
    return { 
        'code': 'SUCC 200 OK'
    }

print(2, __name__)#
if __name__ == '__main__' :
    print('todo.py 파일 직접 실행')