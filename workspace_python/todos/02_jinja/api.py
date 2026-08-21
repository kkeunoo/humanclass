from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

@app.get('/hello')
def hello(request : Request) :
    print('/hello 실행')
    # 2026년 3월경부터 TemplateResponse의 인자값 순서가 변경되어 참고
    # request뒤에 파일명을 넣어준다면, 상단에 Jinja...directory='경로'에 가서 찾게 됨 (동기로 동작)
    # html로 인식하라는 header도 같이 포함해서 요청하는 것
    # html에서 사용할 땐 {{ ip }} 같이 넣어서 사용
    return templates.TemplateResponse(request, 'home.html', {
        'ip' : request.client.host,
        'msg' : '안니용?'
    })

@app.get('/youtube')
def youtube(request : Request) :
    print('/youtube 실행')
    return templates.TemplateResponse(request, 'youtube.html', {
        'like' : 3,
        'star' : 4,
        'bookmark' : ['동영상1','동영상2','동영상3','동영상4','동영상5']
    })

# 아래처럼 Jinja에 별도로 만든 함수를 환경변수에 넣어 사용할 수 있음
def price(value) :
    # print(f'{value:,}')
    return f'{ int(value) :,}'
# 사용자 Filter만들고 적용하기
# ['price] 는 Jinja에서 사용 할 필터 명
templates.env.filters['price'] = price

# 날짜 포매팅 필터
from datetime import datetime
def format_date(value, format='%Y-%m-%d %H:%M:%S') :
    v = datetime.fromisoformat(value)
    return v.strftime(format)
templates.env.filters['format_date'] = format_date

# Textarea의 \n을 <br>로 변환하고 HTML로 인식시키는 필터
# Markup 모듈로 innerHTML로 만들어 줄 수 있음 
def n2br(value) :
    from markupsafe import Markup
    return Markup(value.replace('\n', '<br>'))
templates.env.filters['n2br'] = n2br

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")




