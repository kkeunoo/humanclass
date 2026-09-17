# FastAPI Cookie·Session·로그인 검사 Middleware

<a id="section-1"></a>

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 내·강사님 코드 | workspace_python/05_cookie_session/cookie.html, cookie.py, session.py, aop.py, templates/main.html |
| 범위 | JS Cookie·응답 Cookie·SessionMiddleware·StaticFiles·공통 로그인 검사 |
| 실습 성격 | /login 방문 시 임의 admin을 설정하는 모의 로그인, 실제 인증 구현 아님 |
| 비밀정보 | 원본 secret_key는 복사하지 않으며 개선 환경변수 사용 |
| 다음 수업 | 06_scikit_learn은 사용자 요청으로 보류 |

<a id="section-2"></a>

## 학습 목표

- Cookie가 저장되고 다음 요청에 포함되는 순서를 설명한다.
- 일반 서버 Session 개념과 수업의 서명 Cookie Session을 구분한다.
- 로그인 검사 Middleware의 위치·예외 경로·실패 흐름을 이해한다.

<a id="section-3"></a>

## 1. Cookie란? 서버의 Python dict와 무엇이 다른가?

Cookie는 브라우저가 보관하는 이름·값과 만료·전송 범위 등의 정보다. 서버의 Set-Cookie 응답 또는 JS document.cookie로 만들고, 이후 조건에 맞는 HTTP 요청에 Cookie 헤더를 포함한다. 모든 IP 정보나 모든 Form 값을 자동 담는 구조는 아니다. Domain·Path·Secure·SameSite·만료 조건에 따라 전송 여부가 결정된다.

```text
GET /main (첫 방문, 아직 no 쿠키 없음)
→ 서버 Cookie(no) 인자는 None
→ HTML·Set-Cookie 응답
→ 브라우저 쿠키 저장
→ HTML의 JS가 document.cookie="no=1234" 실행
→ 다음 GET /main
→ Cookie: no=1234; ... 전송
→ Cookie(no) 인자에 "1234"
```

첫 응답 HTML에서 실행한 JS는 이미 서버가 처리한 첫 요청의 no 값을 과거로 되돌려 바꾸지 않는다. 이 시점 차이를 알아야 'print가 None인데 브라우저에는 쿠키가 있다'를 이해할 수 있다.

<a id="section-4"></a>

## 2. JS Cookie·팝업 실습을 읽기

양쪽 cookie.html은 key=value인 세션 쿠키, max-age인 기간 쿠키, showPopup인 10초 숨김 상태를 연습한다. document.cookie="a=1"은 기존 전체 쿠키 문자열을 갈아 끼우는 것이 아니라 해당 쿠키를 설정하는 방식이다. 읽기는 접근 가능한 쿠키들을 "a=1; b=2" 형식으로 준다.

```javascript
document.cookie = "showPopup=true; max-age=10; path=/";
const entry = document.cookie.split("; ")
    .find(value => value.startsWith("showPopup="));
console.log(entry ? entry.slice("showPopup=".length) : null);
```

팝업 닫기 클릭 → CSS hide 추가는 즉시 화면 상태 변화다. 체크했을 때만 Cookie도 만들어 다음 새로고침에서 숨김을 유지한다. 쿠키 만료 후 기존 화면이 자동으로 새로고침되어 나타나는 것은 아니다. 다시 페이지 초기화 코드가 실행될 때 쿠키 없음으로 표시된다.

강사님 'heal' 반복 코드는 다른 이름의 쿠키마다 '힐 안합니다'를 출력할 수 있어 최종 heal 판정과 로그가 섞인다. 내·강사님 getCookieValue는 단순 split("=")로 값을 파싱하므로 값에 =나 인코딩된 문자가 있는 경우를 보강할 수 있다. 💡 쿠키 규칙은 프로토콜 값 처리에 맞춰 제한된 Key·인코딩을 사용하는 편이 명확하다.

<a id="section-5"></a>

## 3. Cookie()·Response.set_cookie()의 역할

내·강사님 cookie.py는 no: str | None = Cookie(None)와 yes: Annotated[..., Cookie()] = None으로 요청 쿠키를 읽는다. 기본값 None은 없는 Cookie를 허용한다는 뜻이다. response.set_cookie는 앞으로 브라우저가 저장할 쿠키를 응답 헤더에 설정한다. 둘은 방향이 반대다.

원본은 templates.TemplateResponse(...)를 response 변수에 넣은 다음 set_cookie하고 그 객체를 반환한다. 다른 Response를 새로 만들어 반환하면 설정한 헤더가 사라질 수 있다. Cookie를 설정한 바로 그 응답을 반환하는 것을 확인한다.

```python
# 원본 main() 안에서 TemplateResponse를 만든 뒤 적용한 방식

## 목차

- [문서 정보](#section-1)
- [학습 목표](#section-2)
- [1. Cookie란? 서버의 Python dict와 무엇이 다른가?](#section-3)
- [2. JS Cookie·팝업 실습을 읽기](#section-4)
- [3. Cookie()·Response.set_cookie()의 역할](#section-5)
- [4. Session이란? 수업 SessionMiddleware는 어디에 저장하는가?](#section-6)
- [5. 내 코드와 강사님 코드 비교](#section-7)
- [6. AOP·Middleware·StaticFiles의 처리 순서](#section-8)
- [7. 독립 실행 가능한 Session 흐름 예제](#section-9)
- [8. 실무 지침·자주 하는 실수·디버깅](#section-10)
- [9. 종합실습](#section-11)
- [10. 정답과 해설](#section-12)
- [최종 체크리스트](#section-13)
- [핵심 요약](#section-14)

response.set_cookie("key2", "value2", max_age=10)
response.set_cookie("key3", "value3", max_age=1000, httponly=True)
return response
```

강사님 key3 주석의 '10초'는 max_age=1000과 다르다. HttpOnly는 JS document.cookie로 읽는 접근을 막는 속성이지 서버로 전송하지 않는다는 뜻이 아니다. 쿠키 탈취·CSRF·로그인 권한의 모든 문제를 단독으로 해결하지도 않는다.

delete_cookie는 같은 이름·Domain·Path에 대해 만료되는 Set-Cookie를 보낸다. 원본 return '{"message":...}'는 Python 문자열이라 JSON 객체처럼 썼어도 실제 기본 응답은 JSON 문자열이다. 개선은 return {"message":"삭제 완료"}다.

<a id="section-6"></a>

## 4. Session이란? 수업 SessionMiddleware는 어디에 저장하는가?

일반적인 서버 Session 설명은 서버 저장소의 데이터를 Session ID로 찾는 방식이지만, **이번 Starlette SessionMiddleware는 서명된 Cookie에 Session 데이터를 담는 방식**이다. request.session은 서버에서 dict처럼 읽고 수정하지만, 그 내용이 암호화되어 서버에만 감춰지는 것은 아니다. 서명은 변경 여부를 검증하고 암호화는 내용을 숨기는 다른 기능이다. 비밀번호·민감 정보를 Session에 넣지 않는다. [Starlette 공식 Session 설명](https://starlette.dev/middleware/#sessionmiddleware)

원본 secret_key가 코드에 있으므로 신규 설명에서는 복사하지 않는다. 키는 충분히 무작위인 비밀 설정으로 관리하고 바뀌면 기존 서명 Cookie가 더 이상 유효하지 않을 수 있다. 여러 서버 인스턴스는 동일 정책과 비밀 키 관리가 필요하다.

```text
/login 요청
→ request.session["isLogin"]=True, ["id"]="admin"
→ SessionMiddleware가 데이터와 서명으로 Cookie 응답 작성
→ 브라우저 저장
→ /mypage 요청에 session Cookie 포함
→ SessionMiddleware가 서명 검증·session 복원
→ endpoint가 id·isLogin 읽음
```

쿠키가 변조되거나 만료되어 유효하지 않으면 로그인 데이터가 복원되지 않는다. 하지만 쿠키를 복사·탈취당한 상황에 대한 대응이나 사용자별 서버 강제 로그아웃은 이 학습 구조만으로 해결되지 않는다.

<a id="section-7"></a>

## 5. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| session.py | 로그인 None 검사 후 mypage 메시지 | 동일한 모의 로그인 흐름 |
| aop.py | 공통 검사·예외 경로·static 허용 | 동일 |
| aop 서버 포트 | 8100 | 8000 |
| Session 로그인 | /login 방문만으로 admin 설정 | 동일 |
| 로그아웃 | request.session.clear() | 동일 |
| key3 기간 | 1000초 | 코드 1000초, 주석 10초 교정 |
| 비밀 키 | 하드코딩 | 하드코딩, 재노출 금지 |

원본은 인증 ID·비밀번호를 확인하지 않으므로 실제 로그인 완료 시스템이 아니다. /login은 session 저장 관찰을 위한 실습이다. None 검사만으로 False를 로그인 상태로 착각할 수 있고 aop는 'isLogin Key가 존재'하는 것만 검사하므로 False가 들어 있어도 통과할 수 있다. 개선은 명시적인 값과 사용자 권한을 확인한다.

<a id="section-8"></a>

## 6. AOP·Middleware·StaticFiles의 처리 순서

AOP는 여러 기능에 반복되는 공통 관심사(인증 검사·로깅 등)를 분리하려는 접근이다. 수업은 HTTP Middleware로 로그인 검사를 공통화했다. 함수마다 같은 if를 복사하지 않도록 요청 전·후에 공통 처리를 배치한다.

aop.py에서는 login_check를 등록한 뒤 add_middleware(SessionMiddleware, ...)한다. 세션을 읽는 login_check보다 SessionMiddleware가 먼저 요청을 감싸 session을 준비해야 한다. 순서를 바꾸면 request.session 접근 시 SessionMiddleware가 필요하다는 오류가 날 수 있다.

```text
HTTP 요청
→ SessionMiddleware: 서명 검증·session 준비
→ login_check: Path·session 검사
→ 허용 시 call_next
→ Router 또는 StaticFiles
→ 응답
→ SessionMiddleware: Cookie 작성
```

EXCLUDE_PATH의 /login은 검사에서 제외해야 Redirect가 다시 /login으로 돌아가는 루프를 막는다. /static 제외는 로그인 화면의 CSS도 받아오게 한다. 원본 startswith("/static")는 /static-other도 통과시키므로 개선은 path=="/static" or path.startswith("/static/")처럼 경계를 확인한다.

StaticFiles의 URL /static은 실제 디스크 폴더 static과 이름이 같아야만 하는 것은 아니다. mount의 경로와 directory가 연결한다. name="static"은 Jinja url_for("static", path="/css/main.css")가 URL을 만드는 등록 이름이다. 폴더 누락은 서버 시작 단계에서도 오류가 날 수 있다.

<a id="section-9"></a>

## 7. 독립 실행 가능한 Session 흐름 예제

💡 다음은 원본을 그대로 합친 코드가 아니라, 외부 템플릿·DB 없이 Session과 검사 순서를 재현하는 보강용 api.py다. 실제 인증은 포함하지 않는다.

```python
import os
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

@app.middleware("http")
async def login_check(request: Request, call_next):
    if request.url.path in {"/login", "/logout"}:
        return await call_next(request)
    if request.session.get("isLogin") is not True:
        return RedirectResponse("/login", status_code=303)
    return await call_next(request)

app.add_middleware(
    SessionMiddleware,
    secret_key=os.environ["SESSION_SECRET"],
    same_site="lax",
    https_only=False,  # 로컬 HTTP 실습; 운영 HTTPS는 True 검토
)

@app.get("/login")
def demo_login(request: Request):
    request.session.update({"isLogin": True, "id": "admin"})
    return {"message": "모의 로그인"}

@app.get("/mypage")
def mypage(request: Request):
    return {"id": request.session["id"]}

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return {"message": "로그아웃"}
```

PowerShell에서 $env:SESSION_SECRET에 전용 실습용 무작위 값을 설정한 뒤 python -m uvicorn api:app으로 실행한다. fastapi·uvicorn·itsdangerous가 필요하다. 환경변수가 없으면 시작 실패하도록 해서 고정 기본 비밀 키를 쓰지 않는다.

첫 GET /mypage는 303 /login. 브라우저가 자동 이동하면 /login의 모의 로그인 때문에 곧바로 세션이 생긴다. 303 자체를 확인하려면 테스트 도구의 Redirect 자동 추적을 끈다. /login 응답 후 같은 쿠키 저장소로 /mypage를 요청하면 {"id":"admin"}. 다른 브라우저 쿠키 저장소에서는 여전히 로그인 전이다. /logout 이후에는 Session 쿠키 만료 응답을 받고 다시 /mypage는 303이다.

이 예제는 관찰용 GET 로그인·로그아웃을 유지했으며 운영 변경 요청은 POST와 CSRF 보호 등으로 보강한다. HTTPS에서 Secure, HttpOnly, SameSite, 만료, 인증·인가·로그아웃 정책을 함께 검토해야 한다.

<a id="section-10"></a>

## 8. 실무 지침·자주 하는 실수·디버깅

| 증상 | 확인 |
| --- | --- |
| 첫 print가 None | Cookie 설정은 다음 요청에 반영되는지 |
| JS에 key3이 안 보임 | HttpOnly이면 정상, Network Cookie 확인 |
| 로그인했는데 다시 Redirect | 동일 브라우저·Host·Cookie 정책·포트·서명 키 |
| Redirect 무한 반복 | /login 예외 경로가 맞는지 |
| request.session 오류 | SessionMiddleware 설치·등록 순서 |
| CSS 못 읽음 | static 디렉터리·mount 경로·검사 예외 |
| 로그아웃 후 화면 그대로 | 현재 HTML과 다음 요청의 세션 상태는 별개 |

쿠키는 일반적으로 포트별 독립 저장소가 아니므로 8000·8100 같은 같은 Host의 서비스에서 이름 충돌을 주의한다. 127.0.0.1과 localhost는 다른 Host다. 다른 Origin의 fetch에는 credentials 설정과 CORS credentials 허용, SameSite 등 조건을 함께 확인한다.

<a id="section-11"></a>

## 9. 종합실습

쿠키 없는 요청·모의 로그인·mypage·logout·재요청을 같은 테스트 클라이언트로 순서대로 확인한다. Session 쿠키를 가진 클라이언트 A와 없는 B를 구분한다. isLogin=False이면 검사에서 거부되는지 확인한다. /static/...와 /static-other의 예외 처리를 비교하고, 브라우저 팝업 10초 만료와 새로고침 시점을 구분한다.

<a id="section-12"></a>

## 10. 정답과 해설

<details><summary>session dict를 썼으니 민감한 데이터가 서버에만 남을까?</summary>

이번 Middleware는 서명 Cookie 기반이라 데이터가 클라이언트 Cookie에 담긴다. 서명은 변조 방지이지 암호화가 아니다. 사용자 식별·최소 상태만 넣고 민감 정보는 넣지 않는다.

</details>

<details><summary>모의 로그인 후 새 클라이언트로 mypage를 열면 왜 안 될까?</summary>

서버의 전역 로그인 True가 아니라 각 요청이 보내는 Cookie에서 상태를 복원하기 때문이다. 같은 서버를 방문해도 쿠키 저장소가 다르면 별도 로그인 상태다.

</details>

<a id="section-13"></a>

## 최종 체크리스트

- [ ] Cookie 읽기와 Set-Cookie 응답 방향을 구분한다.
- [ ] HttpOnly가 서버 전송을 막는다는 오해를 하지 않는다.
- [ ] 원본 Session이 서명 Cookie 방식임을 설명한다.
- [ ] /login은 모의 로그인이라는 한계를 안다.
- [ ] Middleware 순서·예외 경로·static 경계를 점검한다.
- [ ] Session 비밀 키를 코드·문서에 하드코딩하지 않는다.
- [ ] CSRF·인증·인가를 CORS와 혼동하지 않는다.

<a id="section-14"></a>

## 핵심 요약

Cookie 저장 → 다음 요청의 Cookie Header → SessionMiddleware 복원 → 공통 검사 → endpoint → 응답 Cookie. 서명은 암호화가 아니며 수업의 모의 로그인은 실제 인증 검증이 아니다.
