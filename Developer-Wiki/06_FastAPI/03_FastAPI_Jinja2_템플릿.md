---
title: FastAPI Jinja2 템플릿
version: v2.0-final
last_updated: 2026-08-25
status: Completed
---

# FastAPI Jinja2 템플릿

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `03_FastAPI_Jinja2_템플릿.md` |
| 분류 | `06_FastAPI` |
| 내 코드 | `workspace_python/02_todos/02_jinja/api.py`, `templates/*.html` |
| 강사님 코드 | `workspace_teacher/workspace_python/todos/02_jinja/api.py`, `templates/*.html` |
| 핵심 범위 | `Jinja2Templates`, `TemplateResponse`, 변수, 주석, 조건문, 반복문, 상속, Include, Block, Macro, Filter, Autoescape |
| 제외 범위 | 학습 중인 `03_database` |
| 문서 형식 | FastAPI Developer-Wiki V2 |

> 이 문서는 완료된 `02_jinja` 수업만 다룬다. FastAPI가 Data를 준비하고 Jinja2가 HTML을 Rendering하는 흐름을 실제 코드 순서대로 정리한다.

---

# 학습 목표

- Server-side Rendering과 Template Engine의 역할을 설명할 수 있다.
- FastAPI에서 `Jinja2Templates`를 설정할 수 있다.
- `TemplateResponse`로 Request와 Context를 전달할 수 있다.
- Jinja 변수, 주석, 조건문과 반복문을 사용할 수 있다.
- Template 상속, Include, Block과 `super()`를 구분할 수 있다.
- 기본 Filter와 사용자 정의 Filter를 사용할 수 있다.
- Macro로 반복되는 HTML 구조를 재사용할 수 있다.
- Autoescape와 `Markup` 사용 시 보안 위험을 설명할 수 있다.
- 내 코드와 강사님 코드의 실제 차이를 설명할 수 있다.

---

# 1. Template Engine과 Server-side Rendering

Jinja2는 Python Data와 HTML Template을 결합해 최종 HTML을 만드는 Template Engine이다.

```text
Browser Request
→ FastAPI Endpoint
→ Python Data 준비
→ Jinja2 Template Rendering
→ 완성된 HTML Response
```

```html
MSG: {{ msg }}
```

`{{ msg }}` 자리에 FastAPI가 전달한 값이 들어간 HTML을 Browser가 받는다.

---

# 2. 설치와 기본 설정

```powershell
python -m pip install jinja2
```

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')
```

`directory`는 Template 파일을 찾을 기준 Directory다. 실행 위치가 달라지면 상대 경로가 어긋날 수 있으므로 Uvicorn을 Project Directory에서 실행한다.

---

# 3. TemplateResponse

## 3.1 수업 코드

```python
@app.get('/hello')
def hello(request: Request):
    return templates.TemplateResponse(
        request,
        'home.html',
        {
            'ip': request.client.host,
            'msg': '안녕?',
        },
    )
```

| 인자 | 역할 |
| --- | --- |
| `request` | 현재 HTTP Request |
| `'home.html'` | Rendering할 Template 이름 |
| `dict` | Template에서 사용할 Context |

Context의 Key가 Template 변수명이 된다.

```html
YOUR IP: {{ ip }}<br>
MSG: {{ msg }}
```

---

# 4. Jinja 표현식과 주석

## 4.1 값 출력

```jinja2
{{ msg }}
{{ like }}
```

## 4.2 Jinja 주석

```jinja2
{# Browser에 출력되지 않는 Jinja 주석 #}
```

HTML 주석은 Rendering 결과에 남을 수 있다.

```html
<!-- HTML Source에서 확인될 수 있는 주석 -->
```

민감한 정보는 HTML 주석에도 적지 않는다.

---

# 5. 조건문

```jinja2
{% if star > 3 %}
    별점이 높아요: {{ star }}
{% elif star == 3 %}
    별점이 중간입니다: {{ star }}
{% elif 0 <= star <= 2 %}
    별점이 낮아요: {{ star }}
{% else %}
    별점이 올바르지 않습니다.
{% endif %}
```

값이 전달되지 않은 변수를 단순 출력하면 기본 Undefined 설정에서는 빈 값처럼 보일 수 있지만, 비교·연산하면 오류가 발생할 수 있다. 필요한 값은 FastAPI Context에서 명확히 전달하거나 `default` Filter를 사용한다.

```jinja2
{{ star2 | default('기본값') }}
{{ star2 | d('기본값') }}
```

---

# 6. 반복문과 Loop 변수

```jinja2
{% for item in bookmark %}
    <div>
        {{ loop.index }}. {{ item }}
        first={{ loop.first }}
        last={{ loop.last }}
    </div>
{% endfor %}
```

| 변수 | 의미 |
| --- | --- |
| `loop.index` | 1부터 시작하는 순번 |
| `loop.index0` | 0부터 시작하는 순번 |
| `loop.first` | 첫 번째 반복 여부 |
| `loop.last` | 마지막 반복 여부 |

---

# 7. Template 상속

공통 Layout을 부모 Template로 만들고 Page별 영역만 자식 Template에서 작성한다.

## 7.1 부모 Template

```jinja2
<!DOCTYPE html>
<html lang="ko">
<head>
    <title>{% block title %}{% endblock %}</title>
    <style>{% block css %}{% endblock %}</style>
</head>
<body>
    {% include 'header.html' %}
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

## 7.2 자식 Template

```jinja2
{% extends 'layout.html' %}

{% block title %}동영상 페이지{% endblock %}

{% block content %}
    {{ super() }}
    <div>좋아요 {{ like }}</div>
{% endblock %}
```

- `extends`: 부모 Template 상속
- `block`: 자식이 채우거나 덮어쓸 영역
- `super()`: 부모 Block의 기존 내용 유지
- Block 밖의 일반 HTML은 상속 구조에서 기대한 위치에 출력되지 않을 수 있다.

---

# 8. Include와 Import

## 8.1 Include

```jinja2
{% include 'header.html' %}
```

HTML 조각을 현재 위치에 삽입한다. Header, Footer처럼 공통 화면 조각에 적합하다.

## 8.2 Import

```jinja2
{% import 'macros.html' as macros %}
{{ macros.render_card('제목', '내용') }}
```

다른 Template의 Macro를 Namespace로 가져온다.

---

# 9. Macro

Macro는 반복되는 HTML 구조를 함수처럼 재사용한다.

```jinja2
{% macro render_card(title, text) %}
<article class="card">
    <h2>{{ title }}</h2>
    <p>{{ text }}</p>
</article>
{% endmacro %}
```

```jinja2
{{ render_card('제목 1', '내용 1') }}
{{ render_card('제목 2', '내용 2') }}
```

수업의 `macros.html`처럼 재사용 Macro를 별도 파일에 모을 수 있다.

---

# 10. 기본 Filter

```jinja2
{{ text | length }}
{{ text | truncate(10, True, '...') }}
{{ '3.14' | int }}
{{ missing | default('기본값') }}
```

Filter는 `|` 왼쪽의 값을 가공해 출력한다.

---

# 11. 사용자 정의 Filter

## 11.1 금액 표시

```python
def price(value):
    return f'{int(value):,}'

templates.env.filters['price'] = price
```

```jinja2
{{ 15000 | price }}원
```

## 11.2 날짜 표시

```python
from datetime import datetime


def format_date(value, fmt='%Y-%m-%d %H:%M:%S'):
    parsed = datetime.fromisoformat(value)
    return parsed.strftime(fmt)


templates.env.filters['format_date'] = format_date
```

내 코드는 함수명과 Filter 이름을 `format_date`로 통일했다. 강사님 코드는 `format_data`를 사용하므로 오타로 단정하기보다 실제 등록 이름과 Template 사용 이름이 일치하는지가 중요하다.

---

# 12. Autoescape와 Markup

Jinja2는 HTML Template에서 문자열을 Escape해 Script 삽입 위험을 줄인다.

```jinja2
{{ '<h1>Hello</h1>' }}
```

`Markup`은 값을 안전한 HTML이라고 표시한다.

```python
from markupsafe import Markup


def n2br(value):
    escaped = Markup.escape(value)
    return Markup('<br>'.join(escaped.splitlines()))
```

원본의 다음 형태는 입력값에 악성 HTML이 있을 때 XSS 위험이 있다.

```python
Markup(value.replace('\n', '<br>'))
```

사용자 입력을 먼저 Escape한 뒤 필요한 `<br>`만 추가해야 한다.

---

# 13. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 | 판단 |
| --- | --- | --- | --- |
| `/hello`, `/youtube` | 동일 흐름 | 동일 흐름 | 핵심 구조 동일 |
| 별점 | `4` | `1.5` | 조건문 결과만 다름 |
| 날짜 Filter | `format_date` | `format_data` | 등록명과 사용명은 각 코드 안에서 일치 |
| `truncate` | 추가 실습 | 없음 | 내 코드에 Filter 실습 보강 |
| Layout 기본 Content | 설명형 Text | 임시 Text | 내 코드가 의도 설명에 유리 |
| Macro | 외부·내부 Macro | 동일 | 구조 동일 |

---

# 14. 개선된 통합 예제

```python
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / 'templates')


@app.get('/videos')
def videos(request: Request):
    return templates.TemplateResponse(
        request,
        'youtube.html',
        {
            'like': 3,
            'star': 4,
            'bookmark': ['동영상 1', '동영상 2'],
        },
    )
```

절대 기준 경로를 만들면 Uvicorn 실행 Directory가 달라져도 Template 경로를 안정적으로 찾을 수 있다.

---

# 15. 자주 하는 실수와 Debugging

| 증상 | 원인 | 해결 |
| --- | --- | --- |
| Template를 못 찾음 | 실행 위치 또는 Directory 오류 | `BASE_DIR` 기준 경로 사용 |
| 변수가 비어 있음 | Context Key 누락 | Python Dict와 Template 이름 비교 |
| Undefined 오류 | 없는 값으로 비교·연산 | 기본값 전달 또는 `default` 사용 |
| Block 밖 내용이 안 보임 | 상속 Template 구조 위반 | 모든 Page 내용을 Block 안에 작성 |
| Filter를 찾지 못함 | 등록명과 사용명 불일치 | `env.filters` Key 확인 |
| HTML이 그대로 보임 | Autoescape 작동 | 안전한 Data만 제한적으로 Markup 처리 |

---

# 16. 종합실습

1. 공통 `layout.html`을 만든다.
2. `header.html`을 Include한다.
3. 자식 Page에서 Title, CSS, Content Block을 재정의한다.
4. FastAPI에서 이름, 별점, 목록을 Context로 전달한다.
5. 조건문으로 별점 등급을 출력한다.
6. 반복문과 `loop.index`로 목록 번호를 출력한다.
7. 금액 Filter와 안전한 줄바꿈 Filter를 등록한다.
8. Card Macro를 별도 파일에서 Import한다.

---

# 17. 정답 핵심

```jinja2
{% extends 'layout.html' %}
{% import 'macros.html' as macros %}

{% block title %}동영상 목록{% endblock %}

{% block content %}
    {% if star >= 4 %}<strong>추천</strong>{% endif %}

    {% for video in bookmark %}
        {{ macros.render_card(loop.index, video) }}
    {% else %}
        <p>목록이 없습니다.</p>
    {% endfor %}
{% endblock %}
```

부모 Layout은 전체 구조를, 자식은 Page별 내용만 담당한다. 반복 구조는 Macro로 옮기고 Python에서 전달하는 Context Key를 명확하게 유지한다.

---

# 최종 체크리스트

- [ ] `TemplateResponse`의 Request, Template, Context를 설명할 수 있다.
- [ ] `{{ }}`, `{% %}`, `{# #}`를 구분할 수 있다.
- [ ] 조건문과 반복문을 작성할 수 있다.
- [ ] `extends`, `block`, `super`, `include`를 구분할 수 있다.
- [ ] Macro와 Filter를 구분할 수 있다.
- [ ] 없는 변수와 기본값을 안전하게 처리할 수 있다.
- [ ] Autoescape와 `Markup`의 XSS 위험을 설명할 수 있다.
- [ ] Template 경로 오류를 Debugging할 수 있다.

---

# 핵심 요약

```text
Jinja2 = Python Data + HTML Template
Context Key = Template 변수명
extends/block = Layout 상속
include = HTML 조각 삽입
macro = HTML 구조 재사용
filter = 값 가공
Markup = 신뢰할 수 있는 HTML에만 제한적으로 사용
```
