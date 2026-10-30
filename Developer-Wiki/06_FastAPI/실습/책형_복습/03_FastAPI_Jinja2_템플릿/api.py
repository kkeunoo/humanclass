from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

def price(value):
    return f'{int(value):,}'

templates.env.filters['price'] = price

@app.get('/page')
def page(request: Request, msg: str = '안니용?', star: float = 4):
    return templates.TemplateResponse(request, 'page.html', {
        'msg': msg, 'star': star, 'amount': '15000',
        'bookmarks': ['동영상1', '동영상2']
    })
