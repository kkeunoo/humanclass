# 03. Jinja 템플릿 — Python 값이 여러 HTML 파일을 거쳐 화면이 되기까지

[FastAPI 목차](README.md) · [읽기 안내](00_FastAPI_상세백과_읽기법.md)

템플릿은 HTML 자리에 Python 값을 채워 최종 문서를 만드는 도구다. 값을 전달하는 함수만 보거나 HTML의 중괄호만 보면 화면이 어떻게 완성되는지 놓치기 쉽다. 부모·자식·포함 파일·매크로·필터 정의를 함께 읽는다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

문맥 값·표현식·제어문·주석을 구분한다. 반복·조건·상속·include·매크로 호출·필터의 실제 입력과 결과를 설명하고, 템플릿 import와 Python import가 같은 기능이 아니라는 점을 확인한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

브라우저가 Jinja 문법을 실행하는 것은 아니다. 서버가 템플릿을 읽고 전달한 값으로 HTML을 완성한 뒤 브라우저에 보낸다. {{ msg }}는 결과에 값을 넣고 {% for %}·{% if %}는 결과를 만드는 반복·조건이다. {# ... #}는 Jinja 주석이다.

| 문법 | 하는 일 | 자료의 흐름 |
| --- | --- | --- |
| {{ 변수 }} | 값 출력 | Python 문맥→문자열 |
| {% for ... %} | 반복 생성 | 목록→여러 HTML 항목 |
| {% if ... %} | 조건 생성 | 값·식→선택한 HTML |
| extends·block | 공통 틀과 교체 영역 | 부모→자식 블록 |
| include | 다른 파일의 내용 포함 | 헤더 등 작은 조각 |
| import·macro | 재사용 템플릿 기능 | 매개변수→HTML 조각 |
| 값 &#124; 필터 | 값 변환 | 입력→함수 결과→출력 |

부모 layout에 block content가 있으면 자식이 같은 이름 block으로 내용을 채운다. extends만 적고 부모가 제공하지 않는 위치에 임의 HTML을 쓰면 기대한 자리에 나타나지 않을 수 있다. include는 파일 조각을 넣는 것이고 macro는 인자를 받아 반복 사용할 HTML을 만드는 기능이다.

필터 price는 템플릿 이름일 뿐, Python에서는 일반 함수를 정의한 뒤 templates.env.filters에 등록한다. 등록 이름·템플릿 호출 이름이 같아야 한다. env는 템플릿 환경 객체이지 운영체제 환경변수를 저장한 곳이라는 뜻이 아니다.

> 📚 **출처 · 본문 설명 확인:** [FastAPI Templates](https://fastapi.tiangolo.com/advanced/templates/), [Jinja 템플릿 문법](https://jinja.palletsprojects.com/en/stable/templates/), [MarkupSafe의 문자열 표시](https://markupsafe.palletsprojects.com/en/stable/escaping/). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. api.py 옆에 templates 폴더와 아래 네 파일을 같은 이름으로 둔다. FastAPI·Uvicorn 외 jinja2가 필요하다. 새 환경 준비 명령은 `python -m pip install fastapi uvicorn jinja2`이며 이 작업에서는 기존 수업 환경을 읽기만 했다. api.py 폴더에서 `uvicorn api:app --port 8000 --reload`를 실행하고 /page를 연다. 상대 템플릿 경로는 현재 작업 폴더를 기준으로 찾는다.



**[api.py](실습/책형_복습/03_FastAPI_Jinja2_템플릿/api.py) — 새 예제 전체 파일**

```python
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
```

**[templates/layout.html](실습/책형_복습/03_FastAPI_Jinja2_템플릿/templates/layout.html) — 새 예제 전체 파일**

```html
<!DOCTYPE html>
<html lang="ko">
<head><meta charset="UTF-8"><title>복습 화면</title></head>
<body>
{% include 'header.html' %}
<main>{% block content %}{% endblock %}</main>
</body>
</html>
```

**[templates/header.html](실습/책형_복습/03_FastAPI_Jinja2_템플릿/templates/header.html) — 새 예제 전체 파일**

```html
<header>Developer-Wiki 복습</header>
```

**[templates/macros.html](실습/책형_복습/03_FastAPI_Jinja2_템플릿/templates/macros.html) — 새 예제 전체 파일**

```html
{% macro card(title, text) %}
<section class="card"><h2>{{ title }}</h2><p>{{ text }}</p></section>
{% endmacro %}
```

**[templates/page.html](실습/책형_복습/03_FastAPI_Jinja2_템플릿/templates/page.html) — 새 예제 전체 파일**

```html
{% extends 'layout.html' %}
{% import 'macros.html' as cards %}
{% block content %}
<h1>{{ msg }}</h1>
<p>별점 {{ star }}</p>
{% if star %}<p>참으로 판단한 별점</p>{% endif %}
{% if star > 3 %}<p>높음</p>
{% elif star == 3 %}<p>중간</p>
{% elif star >= 0 and star <= 2 %}<p>낮음</p>
{% else %}<p>위 세 범위 외</p>{% endif %}
<ul>{% for bookmark in bookmarks %}
<li>{{ loop.index }}. {{ bookmark }} / 첫번째={{ loop.first }} / 마지막={{ loop.last }}</li>
{% endfor %}</ul>
<p>{{ amount | price }}원</p>
<p>{{ missing | default('기본값') }}</p>
{{ cards.card('카드 제목', '카드 내용') }}
{% endblock %}
```

page 함수의 문맥 dict가 자식 page.html에 전달된다. 자식은 layout.html을 부모로 삼고 content 블록을 채운다. 부모는 header 파일을 포함한다. bookmarks 두 항목을 돌며 loop.index는 1·2이고 처음·마지막 표시는 각각 달라진다. amount 문자열15000은 price 함수에서 정수 변환과 쉼표 서식 뒤 15,000으로 돌아온다. cards.card는 외부 macro 정의의 인자 둘을 받아 section을 만든다. msg의 태그는 기본 자동 이스케이프 상태에서 글자로 표시한다.

**요청과 예상 결과:**

| 요청·값 | 결과 HTML의 의미 |
| --- | --- |
| 기본 /page | 안니용?·별점4·높음·목록2개·15,000원·카드 |
| star=0 | 0 표시·낮음, if star 블록은 없음 |
| star=2.5 | 위 세 범위 외 |
| msg에 em태그 | 태그가 문자로 표시됨 |
| star=문자 | 422, 숫자 입력 검증 실패 |

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/02_jinja/api.py` 1–26행 · **원본 발췌**

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

**발췌 바로 풀이:** `Jinja2Templates(directory='templates/')`는 템플릿 폴더를 정한다. `TemplateResponse(request, 'home.html', {'ip': ..., 'msg': ...})`는 템플릿에 두 값을 전달해 HTML 응답을 만든다. 내 `msg`는 `안니용?`, 강사님은 `안뇽?`라서 실제 표시 문구가 다르다. `/youtube`도 `like`, `star`, `bookmark` 목록을 보낸다. 강사님 `star=1.5`, 나는 `star=4`다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/02_jinja/templates/youtube.html` 36–43행 · **원본 발췌**

```html
    {% if star %}
        star를 전달 받았다<br>

        {% if star >= 0 %}
            별점이 있습니다.<br>
        {% endif %}
        {#
            만약 {% if star2 >= 0 %} 처럼 받지 않은 변수를
```
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/02_jinja/templates/youtube.html` 77–84행 · **원본 발췌**

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

**발췌 바로 풀이:** `{{ 값 }}`은 값을 출력하고, `{% for ... %}`와 `{% if ... %}`는 반복·조건을 처리한다. Python에서 보낸 `bookmark`의 5개 문자열을 화면에 차례로 보여 준다. 템플릿의 HTML은 브라우저가 해석할 최종 문서의 재료이며, `/html`에서 단순 문자열을 반환한 예제와 다르다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/02_jinja/templates/youtube.html` 1–1행 · **원본 발췌**

```html
{% extends 'layout.html' %}
```
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/02_jinja/templates/layout.html` 41–49행 · **원본 발췌**

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
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/02_jinja/templates/youtube.html` 113–140행 · **원본 발췌**

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

**발췌 바로 풀이:** `extends`는 공통 `layout.html`을 부모로 삼는다. 그 안의 `include 'header.html'`은 별도 헤더를 넣는다. `import 'macros.html' as macros` 뒤의 `macros.render_card2(...)`는 외부 파일의 매크로를 호출한다. 두 코드에 모두 있는 실제 템플릿 재사용 실습이므로 본문에 둔다. 내 `macros.html`은 카드 번호 `[3]`까지 표시하지만 강사님 `render_card3`에는 그 접두 표시가 없다. 복습할 때는 **부모 레이아웃 → 자식 블록 → 포함 파일과 매크로** 순서로 화면 조합을 따라가면 된다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/02_jinja/api.py` 28–48행 · **원본 발췌**

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

**발췌 바로 풀이:** `price`는 숫자에 쉼표를 넣고, 날짜 필터는 ISO 형식 문자열을 날짜로 바꿔 출력 형식을 만든다. 강사님 필터 이름은 `format_data`, 내 것은 `format_date`다. 템플릿에서 호출할 이름과 등록 이름이 같아야 한다. `n2br`는 줄바꿈을 `<br>`로 바꾼 뒤 `Markup`으로 HTML로 취급하게 한다. **사용자 입력을 무조건 신뢰해 HTML로 바꾸는 일반 규칙으로 확대하지 않는다.** 여기서는 수업 코드의 동작을 읽는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/02_jinja/templates/macros.html` 1–11행 · **원본 발췌**

```html
{% macro render_card2(title, text) %}
    <div class="card">
        <h2>[2]{{ title }}</h2>
        <div>
            [2]{{ text }}
        </div>
        <div>
            [2]{{ like }}
        </div>
    </div>
{% endmacro %}
```

**발췌 바로 풀이:** 이전 발췌에서 호출만 보였던 외부 render_card2의 전체 정의를 보완했다. 인자 title·text는 채워지지만 여기 like는 인자가 아니며 기본 import는 요청 문맥 전체를 자동 공유하지 않는다. 따라서 외부 매크로의 like가 같이 전달된다고 추정하지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/02_todos/02_jinja/templates/layout.html` 56–81행 · **원본 발췌**

```html
                <div class="main">
                    컨텐츠 영역<br>
                    <!-- block 시작 -->
                    {# 자식이 덮어 쓸 블럭(youtube에서 덮어 씀) #}
                    {% block youtube %}
                        Content Test Layout
                    {% endblock %}
                    <!-- block 끝 -->
                </div>
                <div>
                    {% block star %}
                    {% endblock %}
                </div>
                <div>
                    {% block bookmark %}
                    {% endblock %}
                </div>
                <div>
                    {% block filter %}
                    {% endblock %}
                </div>
            </div>
            
            <div>
                {% block macro %}
                {% endblock %}
```

**발췌 바로 풀이:** 자식의 youtube·star·bookmark·filter·macro 블록이 들어갈 실제 부모 영역이다. 자식이 같은 이름으로 작성한 블록이 해당 위치를 채우며 include 헤더와 역할이 다르다.

내 /hello는 msg가 안니용?이고 강사님은 안뇽?이다. /youtube의 별점은 내4·강사님1.5라 같은 분기 결과라고 외우지 않는다. 원본 if star는0에서 거짓이므로 그 안의 별점 있음 문구가 안 나올 수 있다. 높음>3·중간==3·낮음0~2는2초과3미만을 낮음에 넣지 않는다. 원본 default·d·length·truncate·int 필터, 외부 macro와 로컬 macro를 같은 호출 구조에서 읽는다.

<a id="connections"></a>

## 5. import·함수·화면·저장이 연결되는 흐름

api.py의 Jinja2Templates → templates 폴더 → youtube의 extends → layout의 block·include → 외부 macros의 정의 → 전달 문맥의 값·필터 호출 → 완성 HTML 응답이다. 원본 price는 int(value) 뒤 쉼표 서식, format_date는 datetime.fromisoformat(value) 뒤 strftime(format), n2br는 replace로 개행을 br태그로 바꾼 뒤 Markup으로 표시한다. 내 등록 이름 format_date와 강사님 format_data는 서로 다르며 템플릿도 등록명에 맞아야 한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 문맥·반복·블록·사용자 필터를 실제 파일로 나눠 구현했다. **주석 교정:** TemplateResponse 인자 변경 시점을2026년3월이라고 고정한 메모는 근거가 없으며 공식 문서는 FastAPI0.108.0·Starlette0.29.0 이전과 이후를 구분한다. **필터 교정:** env.filters는 OS 환경변수가 아니다. **한계:** Markup은 입력을 정화하는 필터가 아니라 HTML로 신뢰하도록 표시하므로 n2br에 아무 사용자 입력을 넣는 일반 규칙으로 확대하지 않는다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



같은 기본 문법은 중복 인용하지 않는다. 별점·문구·날짜 필터 등록명 차이는 실제 출력을 바꾼다. 어느 문구가 더 좋다는 평가가 아니라 입력과 함수 등록이 결과에 어떻게 영향을 주는지 비교한다. 외부 macro를 호출만 설명하지 않고 누락했던 정의 파일까지 연결했다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 변환 | 입력 | 결과 |
| --- | --- | --- |
| 변수 출력 | msg | h1내용 |
| price 필터 | 문자열15000 | 문자열15,000 |
| for | 목록2항목 | li2개 |
| macro | 제목·내용 | section HTML |
| 상속 | content 블록 | 부모 main 안 내용 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| star를0으로 | if star는 출력 없음 | 숫자0은 거짓 |
| star를2.5로 | 세 범위 외 | 조건의 틈 |
| bookmarks를 빈 리스트로 | li 없음 | 반복 대상 없음 |
| 필터 등록 이름만 변경 | 호출 이름과 불일치 | 필터 탐색 실패 |
| block 이름만 변경 | 부모 기대 영역을 못 채움 | 이름 대응 |

TemplateNotFound면 폴더·파일명·작업 위치를 본다. 필터 없음 오류면 등록명과 템플릿 이름을 맞춘다. 빈 출력이 언제나 성공은 아니며 전달 안 한 변수가 단순 출력에서 비어 보일 수 있다. 같은 변수에 숫자 비교를 하면 오류가 날 수 있어 전달 자료부터 확인한다.

**확인 범위:** 새 앱을 별도 임시 폴더에 복사해 프레임워크 요청·응답 흐름으로 확인한다. 실제 외부 서비스·운영 DB·브라우저 공개 서버에 요청한 결과와 구별한다. 원본 전체 앱을 무조건 실행하지 않으며 별도 확인한 원본 구간은 검증 보고서에 기록한다. 사용자의 가상환경은 검사에 읽기만 사용하고 파일을 설치·수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 자동 이스케이프·HTML 신뢰 경계·Markup과 escape의 상세 차이, 외부 macro의 with context, 엄격한 미정의 변수 설정은 추가 학습이다. [Jinja 공식 문서](https://jinja.palletsprojects.com/en/stable/templates/)와 [MarkupSafe](https://markupsafe.palletsprojects.com/en/stable/escaping/)를 참고한다. 원본 Markup 사용은 본문에서 동작을 설명하되 안전한 입력으로 자동 변환한다고 가르치지 않는다.

request.headers 직접 읽기와 response_model은 미학습으로 확인된 선택 확장이다. 본문에서 이 기능을 선행 조건으로 요구하지 않는다. 응답·입력 타입 표시와 response_model 설정도 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. Jinja 문법을 브라우저가 실행하는가?
2. price 입력과 반환은?
3. macro 호출 정의는 어느 파일인가?
4. if star가0도 표시하는가?
5. Markup은 문자열을 정화하는가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

서버가 HTML을 완성한다. 값을 정수로 바꿔 쉼표 있는 문자열을 반환한다. 원본 macros.html·새 예제 templates/macros.html이다. 0은 거짓이다. HTML로 신뢰하도록 표시하며 정화하지 않는다.

</details>

| 역할 | 문법·정의 |
| --- | --- |
| 값 | 문맥 dict·{{ }} |
| 구조 | extends·block·include |
| 기능 | macro·필터 정의 |
| 응답 | 완성 HTML |

[장별 연습문제](실습/연습문제/03_FastAPI_Jinja2_템플릿_연습문제.md) · 다음은 [함수 호출·리다이렉트](04_FastAPI_Response_Redirect_의존성주입.md)다.
