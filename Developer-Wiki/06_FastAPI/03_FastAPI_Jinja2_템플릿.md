# 03. Jinja 템플릿 — Python 값을 HTML에 넣기

[FastAPI 목차](README.md) · [이전: 라우터와 입력값](02_FastAPI_Router_Request_Pydantic_CRUD.md) · [다음: 응답과 리다이렉트](04_FastAPI_Response_Redirect_의존성주입.md)

앞 장에서 딕셔너리나 문자열을 그대로 반환했다면, 이번 코드는 **템플릿 파일과 Python 데이터**를 합쳐 HTML 화면을 만든다. 두 원본의 `/hello`, `/youtube`와 실제 템플릿을 함께 본다.

## 1. 템플릿 파일에 값 전달

### 강사님 코드

출처: `teacher/workspace_python/todos/02_jinja/api.py` 1–25행 · **원본 발췌**

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 템플릿 폴더를 지정하면서 생성
templates = Jinja2Templates(directory='templates/')

@app.get('/hello')
def hello(request:Request) :
    print('/hello 실행')
    return templates.TemplateResponse(request, 'home.html', {
        'ip': request.client.host,
        'msg': '안뇽?'
    })

@app.get('/youtube')
def youtube(request:Request) :
    print('/youtube 실행')

    return templates.TemplateResponse(request, 'youtube.html', {
        'like': 3,
        'star': 1.5,
        'bookmark': ['동영상1', '동영상2', '동영상3', '동영상4', '동영상5' ]
    })
```

### 내 코드

출처: `me/workspace_python/02_todos/02_jinja/api.py` 1–26행 · **원본 발췌**

```python
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
```

`Jinja2Templates(directory='templates/')`는 템플릿 폴더를 정한다. `TemplateResponse(request, 'home.html', {'ip': ..., 'msg': ...})`는 템플릿에 두 값을 전달해 HTML 응답을 만든다. 내 `msg`는 `안니용?`, 강사님은 `안뇽?`라서 실제 표시 문구가 다르다. `/youtube`도 `like`, `star`, `bookmark` 목록을 보낸다. 강사님 `star=1.5`, 나는 `star=4`다.

## 2. 내장 반복과 조건이 있는 실제 템플릿

### 강사님 코드

출처: `teacher/workspace_python/todos/02_jinja/templates/youtube.html` 31–38행 · **원본 발췌**

```html
{% block star %}
<div>
    {% if star %}
        star를 전달 받았다<br>

        {% if star >= 0 %}
            별점이 있습니다<br>
        {% endif %}
```

출처: `teacher/workspace_python/todos/02_jinja/templates/youtube.html` 75–82행 · **원본 발췌**

```html
{% block bookmark %}
    bookmark 블럭 <br>
    {% for bm in bookmark %}
        <div>
            {{loop.index}}. {{bm}} {{loop.first}} {{loop.last}}
        </div>
    {% endfor %}
{% endblock %}
```

### 내 코드

출처: `me/workspace_python/02_todos/02_jinja/templates/youtube.html` 36–43행 · **원본 발췌**

```html
    {% if star %}
        star를 전달 받았다<br>

        {% if star >= 0 %}
            별점이 있습니다.<br>
        {% endif %}
        {#
            만약 {% if star2 >= 0 %} 처럼 받지 않은 변수를
```

출처: `me/workspace_python/02_todos/02_jinja/templates/youtube.html` 77–84행 · **원본 발췌**

```html
{% block bookmark %}
    bookmark 블럭<br>
    {% for bm in bookmark %}
        <div>
            {{ loop.index }}. {{ bm }} {{ loop.first }} {{ loop.last }}
        </div>
    {% endfor %}
{% endblock %}
```

`{{ 값 }}`은 값을 출력하고, `{% for ... %}`와 `{% if ... %}`는 반복·조건을 처리한다. Python에서 보낸 `bookmark`의 5개 문자열을 화면에 차례로 보여 준다. 템플릿의 HTML은 브라우저가 해석할 최종 문서의 재료이며, `/html`에서 단순 문자열을 반환한 예제와 다르다.

## 3. 상속·포함·매크로로 화면 재사용

### 강사님 코드

출처: `teacher/workspace_python/todos/02_jinja/templates/youtube.html` 1–1행 · **원본 발췌**

```html
{% extends 'layout.html' %}
```

출처: `teacher/workspace_python/todos/02_jinja/templates/layout.html` 37–45행 · **원본 발췌**

```html
<body>
    <div class="container">
        <!-- <header>
            <div>logo, menu</div>
        </header> -->
        {# 다른 html 가져오기 #}
        {% include 'header.html' %}
    
        <div class="wrap">
```

출처: `teacher/workspace_python/todos/02_jinja/templates/youtube.html` 110–138행 · **원본 발췌**

```html
{# 외부에 매크로 모아두고 사용하기 #}
{% import 'macros.html' as macros %}

{% block macro %}
<!-- 
    <div class="card">
        <h2>제목</h2>
        <div>
            내용
        </div>
    </div>
 -->
    {{ render_card('제목1', '내용1') }}
    {{ render_card('제목2', '내용2') }}
    {{ macros.render_card2('제목3', '내용3') }}
{% endblock %}

{# macro 매크로명(전달인자 들) #}
{% macro render_card(title, text) %}
    <div class="card">
        <h2>{{title}}</h2>
        <div>
            {{text}}
        </div>
        <div>
            {{like}}
        </div>
    </div>
{% endmacro %}
```

### 내 코드

출처: `me/workspace_python/02_todos/02_jinja/templates/youtube.html` 1–1행 · **원본 발췌**

```html
{% extends 'layout.html' %}
```

출처: `me/workspace_python/02_todos/02_jinja/templates/layout.html` 41–49행 · **원본 발췌**

```html
    <body>
        <div class="container">
            <!-- <header>
                <div>logo, menu</div>
            </header> -->
            {# include로 쓰거나, block으로 써도 됨 #}
            {% include 'header.html' %}
    
            <div class="wrap">
```

출처: `me/workspace_python/02_todos/02_jinja/templates/youtube.html` 113–140행 · **원본 발췌**

```html
{# 외부 파일 한 곳에 macro를 모아두고 import하여 사용하는 방법 #}
{% import 'macros.html' as macros %}

{% block macro %}
    <!-- <div class="card">
        <h2>제목</h2>
        <div>
            내용
        </div>
    </div> -->

    {{ render_card('제목1', '내용1') }}
    {{ render_card('제목2', '내용2') }}
    {{ macros.render_card2('제목3', '내용3') }}
{% endblock %}

{# 아래처럼 macro의 형식을 만들어놓고 인자값만 준다면 위처럼 편하게 사용 가능 #}
{% macro render_card(title, text) %}
    <div class="card">
        <h2>{{ title }}</h2>
        <div>
            {{ text }}
        </div>
        <div>
            {{ like }}
        </div>
    </div>
{% endmacro %}
```

`extends`는 공통 `layout.html`을 부모로 삼는다. 그 안의 `include 'header.html'`은 별도 헤더를 넣는다. `import 'macros.html' as macros` 뒤의 `macros.render_card2(...)`는 외부 파일의 매크로를 호출한다. 두 코드에 모두 있는 실제 템플릿 재사용 실습이므로 본문에 둔다. 내 `macros.html`은 카드 번호 `[3]`까지 표시하지만 강사님 `render_card3`에는 그 접두 표시가 없다. 복습할 때는 **부모 레이아웃 → 자식 블록 → 포함 파일과 매크로** 순서로 화면 조합을 따라가면 된다.

## 4. 사용자 필터의 이름도 비교하기

### 강사님 코드

출처: `teacher/workspace_python/todos/02_jinja/api.py` 27–45행 · **원본 발췌**

```python
def price(value) :
    return f'{ int(value) :,}'
# 사용자 필터 만들고 적용하기
# ['price'] : Jinja에서 사용할 필터 이름
templates.env.filters['price'] = price

# 날짜 포멧
from datetime import datetime
def format_data(value, format="%Y-%m-%d %H:%M:%S"):
    v = datetime.fromisoformat(value)
    return v.strftime(format)
templates.env.filters['format_data'] = format_data

# textarea의 엔터 문자인 \n을 <br>로 바꾸고 HTML로 인식 시키는 필터

def n2br(value):
    from markupsafe import Markup # innerHTML로 만들어 주는 모듈
    return Markup(value.replace('\n', '<br>'))
templates.env.filters['n2br'] = n2br
```

### 내 코드

출처: `me/workspace_python/02_todos/02_jinja/api.py` 28–48행 · **원본 발췌**

```python
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
```

`price`는 숫자에 쉼표를 넣고, 날짜 필터는 ISO 형식 문자열을 날짜로 바꿔 출력 형식을 만든다. 강사님 필터 이름은 `format_data`, 내 것은 `format_date`다. 템플릿에서 호출할 이름과 등록 이름이 같아야 한다. `n2br`는 줄바꿈을 `<br>`로 바꾼 뒤 `Markup`으로 HTML로 취급하게 한다. **사용자 입력을 무조건 신뢰해 HTML로 바꾸는 일반 규칙으로 확대하지 않는다.** 여기서는 수업 코드의 동작을 읽는다.

## 직접 확인할 질문

1. `/hello`의 `ip`, `msg`는 템플릿 파일에서 만들어지는가, Python 함수에서 전달되는가?
2. 강사님과 내 `star` 값은 각각 무엇인가?
3. `extends`, `include`, `import`는 각각 어느 파일을 재사용하는가?
4. 내 템플릿이 `format_data`를 호출하면 등록한 필터 이름과 맞는가?

## 추가로 알면 좋은 것

Jinja의 자동 이스케이프와 HTML 신뢰 경계는 실제 서비스를 만들 때 중요하지만, 이 장에서는 원본에 있는 **값 전달·반복·조건·템플릿 재사용·필터 등록**을 먼저 다룬다.
