# 09. 쿠키·세션·로그인 검사 실습

[FastAPI 목차](README.md) · [이전: 파일 업로드](08_FastAPI_파일업로드_다운로드.md)

양쪽 `05_cookie_session`의 `cookie.py`, `session.py`, `aop.py`에 있는 흐름을 순서대로 본다. 소스에 직접 적힌 세션 비밀키는 Wiki로 복사하지 않았다.

## 먼저: 세 장면을 구분하기

이 장의 **쿠키 만들기**, **세션 값 읽기**, **미들웨어에서 경로 검사**는 서로 이어지지만 같은 코드 한 줄이 아니다. 다음은 두 원본의 실행 흐름을 줄인 **설명용 결과표**다.

| 장면 | 입력 또는 상태 | 확인할 결과 |
| --- | --- | --- |
| 브라우저 팝업 | 닫기 버튼을 누르고 체크박스가 선택됨 | 짧은 만료 시간을 둔 팝업 쿠키를 기록 |
| 세션 실습 | `/login` 방문 뒤 같은 브라우저에서 `/mypage` 방문 | `isLogin` 값이 있어 ID가 포함된 문구를 반환 |
| 공통 경로 검사 | `isLogin` 없이 보호 경로 방문 | `/login`으로 리다이렉트 |

`/login`은 비밀번호 검사 없이 값을 넣는 **수업 동작 실습**이다. 따라서 두 번째 줄을 실제 인증 성공 결과로 해석하지 않는다. 이제 강사님과 내 쿠키 이름·조회 방식, 세션 조건을 각각 비교하자.

## 브라우저 JavaScript로 쿠키 쓰고 읽기

### 강사님 코드

출처: `teacher/workspace_python/05_cookie_session/cookie.html` 25–36행 · **원본 발췌**

```html
        window.onload = () => {
            document.querySelector('#btn1').addEventListener('click', () => {
                // 만료일이 없는 
                // 세션 쿠키 생성
                document.cookie = "key=value"
            })

            document.querySelector('#btn2').addEventListener('click', () => {
                // max-age : 만료일, 단위는 초
                document.cookie = `mode=attack; max-age=${60 * 60 * 2}`
                document.cookie = `heal=full; max-age=${60 * 60 * 24}`
            })
```

출처: `teacher/workspace_python/05_cookie_session/cookie.html` 67–85행 · **원본 발췌**

```html
            document.querySelector('.popup .close').addEventListener('click', function(event){

                console.log(event.target.parentElement.parentElement)
                // 팝업
                event.target.parentElement.parentElement.classList.add('hide')

                // 체크박스
                console.log(event.target.parentElement.querySelector('.chk').checked)
                if (event.target.parentElement.querySelector('.chk').checked){
                    // 쿠키 먹이기
                    document.cookie = `showPopup=true; max-age=10`
                }

            })

            value = getCookieValue('showPopup')
            if(value != null){
                document.querySelector('.popup').classList.add('hide')
            }
```

출처: `teacher/workspace_python/05_cookie_session/cookie.html` 89–102행 · **원본 발췌**

```html
    function getCookieValue(key){
        cookies = document.cookie.split('; ')
        for (cookie of cookies) {
            console.log(cookie)

            name = cookie.split('=')[0]
            value = cookie.split('=')[1]

            if (name == key) {
                return value
            }
        }
        return null
    }
```

### 내 코드

출처: `me/workspace_python/05_cookie_session/cookie.html` 22–32행 · **원본 발췌**

```html
            window.onload = ()=>{
                document.querySelector('#btn1').addEventListener('click', ()=>{
                    // 만료일이 없는 홈페이지 기본 Session cookie 설정법 
                    // Session cookie는 브라우저 탭끼리 공유되지만, 브라우저가 꺼지면 사라짐
                    document.cookie = "key=value"
                })
                document.querySelector('#btn2').addEventListener('click', ()=>{
                    // 'name=value'후에 ';'를 쓰고 'max-age=초'로 만료시간 설정 가능
                    document.cookie = `mode=attack; max-age=${60*60*2}`
                    document.cookie = `heal=full; max-age=${60*60*24}`
                })
```

출처: `me/workspace_python/05_cookie_session/cookie.html` 50–72행 · **원본 발췌**

```html
                // 1. 닫기 버튼 클릭 시 무조건 팝업 안 보이게 처리
                // 2. 닫을 때 체크가 되어있다면 10초짜리 쿠키 설정
                // 3. 새로고침 시에 쿠키가 있다면 팝업 안 보이게 처리
                document.querySelector('.close').addEventListener('click', ()=>{
                    document.querySelector('.popup').classList.add('hide')
                    chk = document.querySelector('.chk')
                    
                    if(chk.checked == true) {
                        document.cookie = 'popup=close; max-age=10'
                    }
                })

                cookies = document.cookie.split('; ')
                console.log(cookies)
                for(i=0; i<cookies.length; i++) {
                    if(cookies[i] != 'popup=close') {
                        document.querySelector('.popup').classList.remove('hide')
                    } else {
                        document.querySelector('.popup').classList.add('hide')
                        break
                    }
                }
            }
```

`document.cookie = "key=value"`로 쿠키를 만들고 `max-age=10`으로 10초 만료 값을 줄 수 있다. 강사님 팝업은 닫기 버튼과 체크박스를 확인하고 `showPopup` 쿠키를 기록한 뒤, 새로고침 때 그 쿠키가 있으면 숨긴다. 나는 `popup=close`를 기록하고 전체 쿠키 문자열을 순회한다. **내 반복문은 일치하지 않는 쿠키마다 팝업을 보이게 했다가, `popup=close`를 만나면 숨긴다.** 최종 표시 여부는 목록의 순서와 일치 항목 유무를 따라 확인해야 한다. 쿠키 이름·값을 정확히 찾아 판단하는 강사님 함수가 복습하기 더 명확하다.

## 쿠키 읽기와 응답에 설정하기

### 강사님 코드

출처: `teacher/workspace_python/05_cookie_session/cookie.py` 11–18행 · **원본 발췌**

```python
@app.get('/main')
def main(
    request: Request,
    response: Response,

    no: str | None = Cookie(None),
    yes: Annotated[str|None, Cookie()] = None,
):
```

출처: `teacher/workspace_python/05_cookie_session/cookie.py` 23–43행 · **원본 발췌**

```python
    response = templates.TemplateResponse(request, 'main.html')

    response.set_cookie(
        key='key',
        value='value'
    )

    response.set_cookie(
        key='key2',
        value='value2',
        max_age=10      # 10초 후 만료
    )

    response.set_cookie(
        key='key3',
        value='value3',
        max_age=1000,   # 10초 후 만료
        httponly=True   # javascript로 수정 불가           
    )

    return response
```

### 내 코드

출처: `me/workspace_python/05_cookie_session/cookie.py` 10–18행 · **원본 발췌**

```python
@app.get('/main')
def main(
    request: Request,
    response: Response,
    # Cookie는 지워질 수 있기에 None으로 해두면 좋음(단, 인증같은 필요 시 필수)
    # js에서 no, yes 쿠키를 넣어놓고 아래처럼 전달인자로 받을 수 있음
    no: str | None = Cookie(None), 
    yes: Annotated[str|None, Cookie()] = None
):
```

출처: `me/workspace_python/05_cookie_session/cookie.py` 23–47행 · **원본 발췌**

```python
    response = templates.TemplateResponse(request, 'main.html')

    response.set_cookie(
        key='key',
        value='value'
    )

    response.set_cookie(
        key='key2',
        value='value2',
        max_age=10 # 10초 후 만료
    )

    # httponly=True를 주면 js에서 수정하지 못하게 할 수 있음
    response.set_cookie(
        key='key3',
        value='value3',
        max_age=1000,
        httponly=True
    )

    # 이렇게 return을 하면 다른 response 객체이기 때문에, 위 response가 안 먹힘
    # 하여 response에 따로 TemplateResponse를 담아 return
    # return templates.TemplateResponse(request, 'main.html')
    return response
```

`Cookie(None)`과 `Annotated[..., Cookie()] = None`은 요청에 쿠키가 없을 때 `None`을 받을 수 있게 한다. `TemplateResponse`를 만든 다음 **그 응답 객체**에 `set_cookie()`를 호출하고 같은 객체를 반환해야 설정한 쿠키가 응답에 실린다. `max_age=10`은 10초, `max_age=1000`은 1000초다. 강사님 원본의 두 번째 값을 ‘10초’라고 쓴 주석은 값과 다르다. `httponly=True`는 브라우저 JavaScript의 `document.cookie`로 해당 쿠키를 읽지 못하도록 한다. 내 주석의 ‘수정하지 못하게’보다 이 설명이 정확하다.

### 쿠키 삭제: 양쪽 코드

출처: `teacher/workspace_python/05_cookie_session/cookie.py` 45–48행 · **원본 발췌**

```python
@app.get('/delete/cookie')
def delete_cookie(response: Response):
    response.delete_cookie('key3')
    return '{"message":"쿠키 key3 삭제 완료"}'
```

출처: `me/workspace_python/05_cookie_session/cookie.py` 50–53행 · **원본 발췌**

```python
@app.get('/delete/cookie')
def delete_cookie(response: Response):
    response.delete_cookie('key3')
    return '{"message" : "쿠키 key3 삭제 완료"}'
```

`delete_cookie('key3')`는 삭제용 쿠키 헤더를 응답에 설정한다. 두 함수는 주입받은 `response`에 이를 설정한 뒤 **문자열을 반환**한다. 실제 반환 응답 객체에 삭제 헤더가 반영되는지는 실행하여 확인해야 하며, 아래의 세션 로그인과는 별개다.

## 세션 값으로 화면 분기

### 강사님 코드

출처: `teacher/workspace_python/05_cookie_session/session.py` 27–47행 · **원본 발췌**

```python
@app.get('/login')
def login(request: Request):
    # 세선 저장
    request.session['isLogin'] = True
    request.session['id'] = "admin"

@app.get('/mypage')
def mypage(request: Request):
    isLogin = request.session.get('isLogin', None)
    id = request.session.get('id', None)
    if isLogin is None :
        return "로그인 하세요"
    else :
        return f"id: [{id}] 비밀스러운 공간에 오신 걸 환영합니다."

@app.get('/logout')
def logout(request: Request):
    # invalidate
    request.session.clear();

    return "로그아웃"
```

### 내 코드

출처: `me/workspace_python/05_cookie_session/session.py` 25–51행 · **원본 발췌**

```python
# /login을 가면 로그인을 했다는 가정 하에 실습
@app.get('/login')
def login(request: Request):
    # 세션 저장 (브라우저마다 따로 관리되는)
    request.session['isLogin'] = True
    request.session['id'] = "admin"

@app.get('/mypage')
def mypage(request: Request):
    isLogin = request.session.get('isLogin', None) # None은 get기본값
    loginID = request.session.get('id', None)

    # 아래처럼 session을 설정해서 바로 mypage에 갈 경우 접근이 불가하고,
    # login 경로로 가서 session을 얻어 오면 접근 가능하도록 설정
    if isLogin is None :
        return "로그인 하세요"
    else :
        return f"ID: [{loginID}] 님 비밀스러운 공간에 오신 걸 환영합니다"

# session을 clear해주면서 logout되도록 사용할 수 있음
@app.get('/logout')
def logout(request: Request):
    # invalidate
    # clear를 했을 때 session 캐비넷을 아예 없애고, 다시 들어가면 새로운 캐비넷이 나옴
    request.session.clear()

    return "로그아웃"
```

두 파일 모두 `SessionMiddleware`를 설정하고 `request.session`에 `isLogin`과 `id`를 넣는다. `/mypage`는 `isLogin`이 없으면 로그인 안내를 반환하고, `/logout`은 `clear()`로 세션 값을 지운다. `/login`은 비밀번호를 검사하지 않고 방문 즉시 로그인 상태로 표시하는 **동작 실습**이다. 실제 로그인 기능으로 사용하면 안 된다.

## 미들웨어에서 접근 검사

### 강사님 코드

출처: `teacher/workspace_python/05_cookie_session/aop.py` 22–52행 · **원본 발췌**

```python
EXCLUDE_PATH = [
    '/join',
    '/login'
]

@app.middleware('http')
async def login_check(request: Request, call_next):

    # 로그인 검사 제외
    url_path = request.url.path
    print('url_path', url_path)
    # if url_path != '/login' :
    if url_path in EXCLUDE_PATH or url_path.startswith('/static'):
        # 제외 경로거나
        # /static으로 시작한다면
        # 그냥 통과
        return await call_next(request)
    else :
    # if url_path not in EXCLUDE_PATH or not url_path.startswith('/static'):

        # 세션에 로그인 정보가 없으면 로그인 페이지로 이동
        # isLogin = request.session.get('isLogin', None)
        # if not isLogin :
        # if isLogin is None :
        if 'isLogin' not in request.session :
            return RedirectResponse(
                url='/login',
                status_code = 302
            )
        else :
            return await call_next(request)
```

### 내 코드

출처: `me/workspace_python/05_cookie_session/aop.py` 46–58행 · **원본 발췌**

```python
    url_path = request.url.path
    print('urp_path', url_path)

    if url_path in EXCLUDE_PATH or url_path.startswith('/static'):
        return await call_next(request)
    else :
        if 'isLogin' not in request.session :
            return RedirectResponse (
                url='/login',
                status_code = 302
            )
        else :
            return await call_next(request)
```

`request.url.path`가 제외 경로이거나 `/static`으로 시작하면 `call_next(request)`로 통과시킨다. 그 외 경로에 `isLogin`이 없으면 `/login`으로 302 이동한다. 내 파일에는 이전 시도가 주석으로 많이 남아 있고, **실제로 실행되는 분기는 46–58행**이다. 강사님 코드는 제외 목록 `EXCLUDE_PATH`를 함수 앞에 정의한다. 미들웨어의 목적은 여러 경로에 같은 검사를 반복하지 않는 것이다.

## 직접 확인할 질문

1. `set_cookie()`를 호출한 응답 객체와 실제 반환한 객체는 같은가?
2. `/login`을 방문할 때 어떤 검증이 수행되는가?
3. `/static` 경로가 로그인 검사를 통과하는 이유는 무엇인가?

## 추가로 알면 좋은 것

실서비스 인증에는 자격 증명 검사, 세션 비밀키 관리, 보호 경로 설계가 필요하다. 이 수업 파일의 `/login`은 인증 예제가 아닌 세션·미들웨어 동작 예제다. `request.headers`로 요청 헤더를 직접 읽는 별도 수업 예제는 이 원본들에서 확인되지 않았다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/09_FastAPI_Cookie_Session_로그인_연습문제.md) → [FastAPI 실무 스타일](실무_코딩스타일.md)
