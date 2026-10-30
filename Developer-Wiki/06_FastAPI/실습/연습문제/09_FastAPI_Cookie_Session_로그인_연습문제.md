# 09. 쿠키·세션·미들웨어 — 다음 요청이 이전 상태를 알아보는 과정 — 연습문제

[본문](../../09_FastAPI_Cookie_Session_로그인.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

브라우저 document.cookie와 서버 Cookie입력·set_cookie출력을 구분한다. 같은 응답 객체 반환, 만료 시간, HttpOnly, 세션 clear, 미들웨어 제외 경로·call_next를 설명한다. 원본의 로그인 표시는 비밀번호 검증이 아니라는 점을 유지한다.

[본문 3절](../../09_FastAPI_Cookie_Session_로그인.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 요청과 결과 예상

**api.py**

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

**cookie.html**

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

실행 전에 결과를 먼저 적는다. 상태·응답·서버 출력·변경된 자료를 구별한다.

<details>
<summary>풀이</summary>

| 상황 | 관찰 |
| --- | --- |
|쿠키 없음·삭제 뒤 | key3=None |
|같은 클라이언트·설정 뒤 | key3=value3 |
|다른 클라이언트 | 쿠키·세션 상태 없음 |
|미로그인 보호 경로 |302→/login |
|실습 로그인 뒤 |200, id=practice |
|로그아웃 뒤 | 보호 경로 다시302 |
|팝업 체크 후 닫기 |10초 만료 쿠키·재방문 숨김 |

첫 Cookie입력은 None이다. set응답을 받은 같은 클라이언트가 다음 요청에 key3을 보내면 서버는 value3을 읽는다. 다른 클라이언트에는 없다. 삭제 응답 뒤에는 다시 None이다. 보호 경로는 로그인 표시가 없으면302로 /login에 보낸다. 로그인 표시를 저장한 클라이언트만 /mypage를 통과하고 clear뒤에는 다시302다. 팝업은 별도 cookie.html에서 이름·값이 맞는 쿠키를 읽어 숨긴다. 체크 없이 닫는 것과 만료 쿠키를 남기는 것은 다르다.

| 상태 | 다음 요청에 전달 | 보호 경로 |
| --- | --- | --- |
|처음 | 세션 없음 |302 |
|login응답 뒤 | 서명 세션 쿠키 | 통과 |
|다른 클라이언트 | 해당 쿠키 없음 |302 |
|clear응답 뒤 | 만료·제거 |302 |

</details>

## 문제 2. 이유 설명

1. Cookie입력과set_cookie는 같은 시점인가?
2. HttpOnly면 서버도 쿠키를 못 읽는가?
3. isLogin키가 있다는 것과True인 것은 같은가?
4. clear는 무엇을 비우는가?
5. 원본 /login은 비밀번호를 검증하는가?

<details>
<summary>풀이</summary>

이전 요청 입력과 다음 요청을 위한 응답 설정이다. 서버는 받을 수 있다. False값이 있는 경우가 다르다. 세션 데이터 매핑이다. 방문만으로 상태를 넣는다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
|팝업 체크 없이 닫기 | 새로고침 뒤 다시 보임 | 상태 쿠키 없음 |
|쿠키 popup값을다르게 | 새 예제에서 팝업 보임 | 이름과값 모두 확인 |
|로그인 True를False로 | 새 보호 검사 거부 | 진릿값 검사 |
|/login을 제외 목록에서 제거 | 로그인 이동 반복 가능 | 진입 경로도 검사됨 |

<details>
<summary>막힐 때 확인</summary>

쿠키가 안 읽히면 같은 호스트·경로·클라이언트·만료를 확인한다. HttpOnly쿠키가 document.cookie에 안 보여도 서버에서는 받을 수 있다. request.session준비 오류면 미들웨어 등록 순서를 본다. /docs까지 리다이렉트되면 현재 제외 목록에 없는 경로라는 점을 확인한다. 새 예제는 설명한 진입 주소를 기준으로 한다.

</details>

## 채점과 복습

정상 값만 보지 말고 누락·잘못된 타입·없는 대상의 흐름도 설명한다. 새 예제는 별도 앱에서 확인하며 원본 DB나 외부 서비스의 성공을 대신 주장하지 않는다. TIP 확장은 필수 조건이 아니다. 정의→등록→입력→호출→반환→다음 요청을 연결할 수 있는지 검토한다.
