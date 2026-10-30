# 09. 쿠키·세션·미들웨어 — 다음 요청이 이전 상태를 알아보는 과정

[FastAPI 목차](README.md) · [읽기 안내](00_FastAPI_상세백과_읽기법.md)

HTTP요청은 매번 새로 들어온다. 쿠키를 저장하고 다음 요청에 보내면 서버가 그 값을 읽어 상태를 이어갈 수 있다. 팝업 쿠키, 응답 쿠키, 세션 로그인 표시, 공통 경로 검사는 역할이 다르므로 하나씩 연결한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

브라우저 document.cookie와 서버 Cookie입력·set_cookie출력을 구분한다. 같은 응답 객체 반환, 만료 시간, HttpOnly, 세션 clear, 미들웨어 제외 경로·call_next를 설명한다. 원본의 로그인 표시는 비밀번호 검증이 아니라는 점을 유지한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

쿠키는 브라우저가 이름·값과 관련 속성을 저장하고 조건에 맞는 다음 요청에 보내는 자료다. document.cookie는 JavaScript에서 접근 가능한 쿠키를 읽고 쓴다. HttpOnly쿠키는 이 JavaScript경로에서 보이지 않지만 브라우저가 서버에 보내고 서버가 읽을 수 있다.

| 동작 | 위치 | 예 |
| --- | --- | --- |
| document.cookie대입 | 브라우저 | 팝업 닫기 상태 |
| Cookie(None) | 요청 함수 입력 | 없으면None |
| response.set_cookie | 응답 | 다음 요청에 쓸 값 저장 지시 |
| response.delete_cookie | 응답 | 같은 범위의 값 만료 지시 |
| request.session | 세션 미들웨어가 제공 | isLogin·id읽고 쓰기 |
| call_next(request) | 공통 검사 뒤 | 다음 처리로 전달 |

이 수업의 SessionMiddleware는 서명된 쿠키에 세션 데이터를 보관하는 방식이다. request.session이 Python딕셔너리처럼 보인다고 별도 서버 메모리 캐비넷이나 DB가 자동으로 생기는 것은 아니다. 서명은 변경 여부를 확인하는 장치이고 암호화와 다르다. 민감한 내용을 숨기는 저장소로 해석하지 않는다.

세션 쿠키라는 말도 구별한다. 만료 시간을 지정하지 않은 일반 쿠키와 SessionMiddleware가 관리하는 세션 데이터는 같은 단어가 들어가도 동일 개념이 아니다. 브라우저 종료 뒤 복원 여부는 브라우저 세션 복원 설정의 영향도 있어 “창을 닫으면 반드시 삭제”로 일반화하지 않는다.

> 📚 **출처 · 본문 설명 확인:** [FastAPI Cookie인자](https://fastapi.tiangolo.com/tutorial/cookie-params/), [응답 쿠키](https://fastapi.tiangolo.com/advanced/response-cookies/), [Starlette SessionMiddleware](https://starlette.dev/middleware/#sessionmiddleware). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-30.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. api.py와 cookie.html을 같은 폴더에 둔다. FastAPI·Uvicorn·itsdangerous가 필요하다. `uvicorn api:app --port 8000 --reload`로 실행한다. /popup은 JavaScript쿠키, /cookie/set·read·delete는 서버 쿠키, /login·mypage·logout은 세션 실험이다. 아래 서명키는 원본에서 복사하지 않은 교재 전용 값이다. /login방문만으로 상태를 넣는 동작 실습이며 실제 인증 기능은 아니다.



**[api.py](실습/책형_복습/09_FastAPI_Cookie_Session_로그인/api.py) — 새 예제 전체 파일**

```python
from fastapi import FastAPI, Request, Response, Cookie
from fastapi.responses import RedirectResponse, FileResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
PUBLIC_PATHS = ['/login', '/popup', '/cookie/set', '/cookie/read', '/cookie/delete']

@app.middleware('http')
async def login_check(request: Request, call_next):
    if request.url.path in PUBLIC_PATHS:
        return await call_next(request)
    if not request.session.get('isLogin'):
        return RedirectResponse('/login', status_code=302)
    return await call_next(request)

# This key is only for this standalone local exercise.
app.add_middleware(SessionMiddleware, secret_key='book-demo-signing-key-for-local-practice')

@app.get('/popup')
def popup():
    return FileResponse('cookie.html')

@app.get('/cookie/set')
def set_cookie(response: Response):
    response.set_cookie('key2', 'value2', max_age=10)
    response.set_cookie('key3', 'value3', max_age=1000, httponly=True)
    return {'message': '쿠키 설정'}

@app.get('/cookie/read')
def read_cookie(key3: str | None = Cookie(None)):
    return {'key3': key3}

@app.get('/cookie/delete')
def delete_cookie(response: Response):
    response.delete_cookie('key3')
    return {'message': '쿠키 삭제'}

@app.get('/login')
def login(request: Request):
    request.session['isLogin'] = True
    request.session['id'] = 'practice'
    return {'message': '실습 상태 저장'}

@app.get('/mypage')
def mypage(request: Request):
    return {'id': request.session.get('id')}

@app.get('/logout')
def logout(request: Request):
    request.session.clear()
    return {'message': '실습 상태 삭제'}
```

**[cookie.html](실습/책형_복습/09_FastAPI_Cookie_Session_로그인/cookie.html) — 새 예제 전체 파일**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>쿠키 팝업</title>
<style>.hide { display: none; }</style></head><body>
<section class="popup"><p>학습 팝업</p>
<label><input type="checkbox" class="chk">10초간 보지 않기</label>
<button class="close">닫기</button></section>
<p>체크 없이 닫으면 새로고침 뒤 다시 보입니다.</p>
<script>
function getCookieValue(key) {
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
        const parts = cookie.split('=');
        if (parts[0] === key) return parts[1];
    }
    return null;
}
const popup = document.querySelector('.popup');
if (getCookieValue('popup') === 'close') popup.classList.add('hide');
document.querySelector('.close').addEventListener('click', () => {
    popup.classList.add('hide');
    if (document.querySelector('.chk').checked) {
        document.cookie = 'popup=close; max-age=10';
    }
});
</script></body></html>
```

첫 Cookie입력은 None이다. set응답을 받은 같은 클라이언트가 다음 요청에 key3을 보내면 서버는 value3을 읽는다. 다른 클라이언트에는 없다. 삭제 응답 뒤에는 다시 None이다. 보호 경로는 로그인 표시가 없으면302로 /login에 보낸다. 로그인 표시를 저장한 클라이언트만 /mypage를 통과하고 clear뒤에는 다시302다. 팝업은 별도 cookie.html에서 이름·값이 맞는 쿠키를 읽어 숨긴다. 체크 없이 닫는 것과 만료 쿠키를 남기는 것은 다르다.

**요청과 예상 결과:**

| 상황 | 관찰 |
| --- | --- |
|쿠키 없음·삭제 뒤 | key3=None |
|같은 클라이언트·설정 뒤 | key3=value3 |
|다른 클라이언트 | 쿠키·세션 상태 없음 |
|미로그인 보호 경로 |302→/login |
|실습 로그인 뒤 |200, id=practice |
|로그아웃 뒤 | 보호 경로 다시302 |
|팝업 체크 후 닫기 |10초 만료 쿠키·재방문 숨김 |

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/05_cookie_session/cookie.html` 22–32행 · **원본 발췌**

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
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/05_cookie_session/cookie.html` 50–72행 · **원본 발췌**

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

**발췌 바로 풀이:** `document.cookie = "key=value"`로 쿠키를 만들고 `max-age=10`으로 10초 만료 값을 줄 수 있다. 강사님 팝업은 닫기 버튼과 체크박스를 확인하고 `showPopup` 쿠키를 기록한 뒤, 새로고침 때 그 쿠키가 있으면 숨긴다. 나는 `popup=close`를 기록하고 전체 쿠키 문자열을 순회한다. **내 반복문은 일치하지 않는 쿠키마다 팝업을 보이게 했다가, `popup=close`를 만나면 숨긴다.** 최종 표시 여부는 목록의 순서와 일치 항목 유무를 따라 확인해야 한다. 쿠키 이름·값을 정확히 찾아 판단하는 강사님 함수가 복습하기 더 명확하다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/05_cookie_session/cookie.py` 10–18행 · **원본 발췌**

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
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/05_cookie_session/cookie.py` 23–47행 · **원본 발췌**

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

**발췌 바로 풀이:** 실제로 반환할 TemplateResponse객체에 쿠키를 설정해 같은 객체를 반환한다. HttpOnly는 JavaScript의 document.cookie접근을 제한하며 모든 요청 전송을 막는 속성이 아니다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/05_cookie_session/cookie.py` 50–53행 · **원본 발췌**

```python
@app.get('/delete/cookie')
def delete_cookie(response: Response):
    response.delete_cookie('key3')
    return '{"message" : "쿠키 key3 삭제 완료"}'
```

**발췌 바로 풀이:** FastAPI가 주입한 Response에 삭제 설정을 추가한 뒤 문자열을 반환한 형태다. 일반 데이터 반환에서는 이 임시 Response의 쿠키 설정이 최종 응답으로 전달된다. 별도 Response객체를 새로 만들어 반환하는 경우와 구별한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/05_cookie_session/session.py` 25–51행 · **원본 발췌**

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

**발췌 바로 풀이:** 방문 즉시 isLogin·id를 넣는 실습이다. isLogin is None검사는 False와 다르며 값이False여도 else로 갈 수 있다. clear는 세션 데이터 매핑을 비우는 것이지 서버에 자동 생성된 캐비넷을 파괴하는 구현이 아니다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/05_cookie_session/aop.py` 46–58행 · **원본 발췌**

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

**발췌 바로 풀이:** `request.url.path`가 제외 경로이거나 `/static`으로 시작하면 `call_next(request)`로 통과시킨다. 그 외 경로에 `isLogin`이 없으면 `/login`으로 302 이동한다. 내 파일에는 이전 시도가 주석으로 많이 남아 있고, **실제로 실행되는 분기는 46–58행**이다. 강사님 코드는 제외 목록 `EXCLUDE_PATH`를 함수 앞에 정의한다. 미들웨어의 목적은 여러 경로에 같은 검사를 반복하지 않는 것이다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/05_cookie_session/aop.py` 7–12행 · **원본 발췌**

```python
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount(
```

내 팝업 반복은 일치하지 않는 쿠키마다 보이게 하고 정확한 popup=close를 만나면 숨긴 뒤break한다. 따라서 그 항목이 있으면 뒤 쿠키가 다시 보이게 하는 구조는 아니며, 없을 때만 보인다. 강사님 함수처럼 한 번 찾아 결정하면 의도를 읽기 쉽다. 원본의 key3 max_age1000은1000초이며10초라는 강사님 주석은 틀렸다. 원본 로그인은 isLogin없음과False를 구별하지 못하는 조건이 있고, aop의 존재 검사도 False값이 들어 있으면 통과할 수 있다.

<a id="connections"></a>

## 5. import·함수·화면·저장이 연결되는 흐름

쿠키 설정 응답 → 클라이언트 저장 → 다음 요청 Cookie입력 또는 SessionMiddleware복원 → request.session → login_check → call_next → 경로 함수 → 응답이다. 미들웨어가 세션을 읽으려면 SessionMiddleware가 그 바깥에서 먼저 준비해야 한다. 새 예제는 로그인 검사 등록 뒤 SessionMiddleware를 추가해 요청 방향에서 세션이 먼저 준비되게 했다. 제외 목록도 전체 정의를 제공했다. 원본의 비밀키 줄은 옮기지 않았다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 쿠키·세션·공통 경로 검사는 각각 실제로 동작을 분리해 기록했다. 같은 응답 객체에 set_cookie를 추가해야 함을 적은 것도 중요하다. **교정:** None검사·키 존재 검사·참인 상태 검사는 다르다. 새 예제는 not get으로False도 통과시키지 않는 보완이다. **설명 보완:** SessionMiddleware는 서버 DB세션 구현이 아니라 서명 쿠키 방식이다. **한계:** /login에는 계정·비밀번호 검사가 없으므로 이를 인증 성공 구현으로 소개하지 않는다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_python/05_cookie_session/cookie.html` 89–102행 · **원본 발췌**

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

쿠키 이름을 찾는 함수만 비교상 필요해 강사님 인용을 남겼다. 내 코드의 최종 상태가 반드시 쿠키 순서에 따라 뒤집히는 것처럼 과장하지 않고 break까지 추적했다. 강사님도 값 속의 등호·변수 선언 등 상세 쿠키파서로 완성한 것은 아니며 현재 단순 이름값 예제를 읽는 함수다. 동일한 세션 함수는 중복 인용하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 상태 | 다음 요청에 전달 | 보호 경로 |
| --- | --- | --- |
|처음 | 세션 없음 |302 |
|login응답 뒤 | 서명 세션 쿠키 | 통과 |
|다른 클라이언트 | 해당 쿠키 없음 |302 |
|clear응답 뒤 | 만료·제거 |302 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
|팝업 체크 없이 닫기 | 새로고침 뒤 다시 보임 | 상태 쿠키 없음 |
|쿠키 popup값을다르게 | 새 예제에서 팝업 보임 | 이름과값 모두 확인 |
|로그인 True를False로 | 새 보호 검사 거부 | 진릿값 검사 |
|/login을 제외 목록에서 제거 | 로그인 이동 반복 가능 | 진입 경로도 검사됨 |

쿠키가 안 읽히면 같은 호스트·경로·클라이언트·만료를 확인한다. HttpOnly쿠키가 document.cookie에 안 보여도 서버에서는 받을 수 있다. request.session준비 오류면 미들웨어 등록 순서를 본다. /docs까지 리다이렉트되면 현재 제외 목록에 없는 경로라는 점을 확인한다. 새 예제는 설명한 진입 주소를 기준으로 한다.

**확인 범위:** 새 앱을 별도 임시 폴더에 복사해 프레임워크 요청·응답 흐름으로 확인한다. 실제 외부 서비스·운영 DB·브라우저 공개 서버에 요청한 결과와 구별한다. 원본 전체 앱을 무조건 실행하지 않으며 별도 확인한 원본 구간은 검증 보고서에 기록한다. 사용자의 가상환경은 검사에 읽기만 사용하고 파일을 설치·수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 서명키 관리·HTTPS·SameSite·CSRF·실제 자격 증명 검사·서버 저장형 세션·엄격한 쿠키파서·세션 복원 정책은 추가 학습이다. 서명됐다는 말과 내용이 암호화돼 숨겨졌다는 말을 구별한다. request.headers직접 읽기와 response_model은 이 수업 본문에 요구하지 않는다.

request.headers 직접 읽기와 response_model은 미학습으로 확인된 선택 확장이다. 본문에서 이 기능을 선행 조건으로 요구하지 않는다. 응답·입력 타입 표시와 response_model 설정도 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. Cookie입력과set_cookie는 같은 시점인가?
2. HttpOnly면 서버도 쿠키를 못 읽는가?
3. isLogin키가 있다는 것과True인 것은 같은가?
4. clear는 무엇을 비우는가?
5. 원본 /login은 비밀번호를 검증하는가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

이전 요청 입력과 다음 요청을 위한 응답 설정이다. 서버는 받을 수 있다. False값이 있는 경우가 다르다. 세션 데이터 매핑이다. 방문만으로 상태를 넣는다.

</details>

| 구분 | 질문 |
| --- | --- |
|쿠키 | 저장·전송·만료·JS접근 |
|세션 | 복원된 상태·서명 |
|미들웨어 | 제외·거부·통과 |
|인증 | 실제 자격 검증이 있나 |

[장별 연습문제](실습/연습문제/09_FastAPI_Cookie_Session_로그인_연습문제.md) · 다음은 [실무 스타일](실무_코딩스타일.md)이다.
