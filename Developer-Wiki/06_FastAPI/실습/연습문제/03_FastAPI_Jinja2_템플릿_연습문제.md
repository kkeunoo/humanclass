# 03. Jinja 템플릿 — Python 값이 여러 HTML 파일을 거쳐 화면이 되기까지 — 연습문제

[본문](../../03_FastAPI_Jinja2_템플릿.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

문맥 값·표현식·제어문·주석을 구분한다. 반복·조건·상속·include·매크로 호출·필터의 실제 입력과 결과를 설명하고, 템플릿 import와 Python import가 같은 기능이 아니라는 점을 확인한다.

[본문 3절](../../03_FastAPI_Jinja2_템플릿.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 요청과 결과 예상

**api.py**

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

**templates/layout.html**

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

**templates/header.html**

```html
<header>Developer-Wiki 복습</header>
```

**templates/macros.html**

```html
{% macro card(title, text) %}
<section class="card"><h2>{{ title }}</h2><p>{{ text }}</p></section>
{% endmacro %}
```

**templates/page.html**

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

실행 전에 결과를 먼저 적는다. 상태·응답·서버 출력·변경된 자료를 구별한다.

<details>
<summary>풀이</summary>

| 요청·값 | 결과 HTML의 의미 |
| --- | --- |
| 기본 /page | 안니용?·별점4·높음·목록2개·15,000원·카드 |
| star=0 | 0 표시·낮음, if star 블록은 없음 |
| star=2.5 | 위 세 범위 외 |
| msg에 em태그 | 태그가 문자로 표시됨 |
| star=문자 | 422, 숫자 입력 검증 실패 |

page 함수의 문맥 dict가 자식 page.html에 전달된다. 자식은 layout.html을 부모로 삼고 content 블록을 채운다. 부모는 header 파일을 포함한다. bookmarks 두 항목을 돌며 loop.index는 1·2이고 처음·마지막 표시는 각각 달라진다. amount 문자열15000은 price 함수에서 정수 변환과 쉼표 서식 뒤 15,000으로 돌아온다. cards.card는 외부 macro 정의의 인자 둘을 받아 section을 만든다. msg의 태그는 기본 자동 이스케이프 상태에서 글자로 표시한다.

| 변환 | 입력 | 결과 |
| --- | --- | --- |
| 변수 출력 | msg | h1내용 |
| price 필터 | 문자열15000 | 문자열15,000 |
| for | 목록2항목 | li2개 |
| macro | 제목·내용 | section HTML |
| 상속 | content 블록 | 부모 main 안 내용 |

</details>

## 문제 2. 이유 설명

1. Jinja 문법을 브라우저가 실행하는가?
2. price 입력과 반환은?
3. macro 호출 정의는 어느 파일인가?
4. if star가0도 표시하는가?
5. Markup은 문자열을 정화하는가?

<details>
<summary>풀이</summary>

서버가 HTML을 완성한다. 값을 정수로 바꿔 쉼표 있는 문자열을 반환한다. 원본 macros.html·새 예제 templates/macros.html이다. 0은 거짓이다. HTML로 신뢰하도록 표시하며 정화하지 않는다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| star를0으로 | if star는 출력 없음 | 숫자0은 거짓 |
| star를2.5로 | 세 범위 외 | 조건의 틈 |
| bookmarks를 빈 리스트로 | li 없음 | 반복 대상 없음 |
| 필터 등록 이름만 변경 | 호출 이름과 불일치 | 필터 탐색 실패 |
| block 이름만 변경 | 부모 기대 영역을 못 채움 | 이름 대응 |

<details>
<summary>막힐 때 확인</summary>

TemplateNotFound면 폴더·파일명·작업 위치를 본다. 필터 없음 오류면 등록명과 템플릿 이름을 맞춘다. 빈 출력이 언제나 성공은 아니며 전달 안 한 변수가 단순 출력에서 비어 보일 수 있다. 같은 변수에 숫자 비교를 하면 오류가 날 수 있어 전달 자료부터 확인한다.

</details>

## 채점과 복습

정상 값만 보지 말고 누락·잘못된 타입·없는 대상의 흐름도 설명한다. 새 예제는 별도 앱에서 확인하며 원본 DB나 외부 서비스의 성공을 대신 주장하지 않는다. TIP 확장은 필수 조건이 아니다. 정의→등록→입력→호출→반환→다음 요청을 연결할 수 있는지 검토한다.
