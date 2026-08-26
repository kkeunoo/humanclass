# ⚡ FastAPI Developer-Wiki

> **개념을 외우는 요약집이 아니라, 수업을 다시 재현할 수 있는 개인 강의 백과사전**

---

## 📌 문서 목적

이 Wiki는 FastAPI를 이미 잘 아는 사람을 위한 Keyword 요약이 아니다. 시간이 지나 내용을 잊어도 다음 질문에 스스로 답하고 코드를 다시 작성할 수 있도록 구성한다.

```text
이것은 무엇인가?
왜 배워야 하는가?
어디에서 값이 만들어지는가?
어떤 경로로 Server에 들어오는가?
FastAPI는 어떻게 받아들이는가?
함수는 언제 실행되는가?
내부에서는 어떤 순서로 처리되는가?
Terminal에는 무엇이 출력되는가?
Browser에는 어떤 결과가 보이는가?
실패하면 어떤 Status와 오류가 발생하는가?
내 코드와 강사님 코드의 어디에서 사용했는가?
다시 사용하려면 어떤 형태로 작성하는가?
```

---

## 🗺️ 학습 흐름

```text
가상환경과 Web API
        ↓
Router와 HTTP Request
        ↓
Jinja2 Server-side Rendering
        ↓
Response, Redirect, Dependency
        ↓
Jinja Todo 화면 CRUD
        ↓
SQLite와 Transaction
        ↓
Database 연동 과정으로 확장 예정
```

---

## 📚 Documentation

| 순서 | 문서 | 핵심 질문 |
| :---: | --- | --- |
| 01 | [FastAPI 가상환경과 웹 API 기초](./01_FastAPI_가상환경과_웹_API_기초.md) | Browser Request가 왜 Uvicorn과 FastAPI를 거치는가? |
| 02 | [Router, Request, Pydantic과 CRUD](./02_FastAPI_Router_Request_Pydantic_CRUD.md) | 주소창·Form·JSON·Header 값은 어디로 들어오는가? |
| 03 | [Jinja2 템플릿](./03_FastAPI_Jinja2_템플릿.md) | Python Data가 어떻게 완성된 HTML이 되는가? |
| 04 | [Response, Redirect와 의존성 주입](./04_FastAPI_Response_Redirect_의존성주입.md) | 반환값이 어떻게 Response가 되고 Redirect는 왜 두 번 요청되는가? |
| 05 | [Jinja Todo CRUD](./05_FastAPI_Jinja_Todo_CRUD.md) | 화면 입력값이 CRUD를 거쳐 다시 화면에 보이는 과정은 무엇인가? |
| 06 | [Python SQLite와 Transaction](./06_Python_SQLite와_Transaction.md) | Python 값이 어떻게 SQL과 DB File에 들어가고 확정·취소되는가? |

---

## 🧱 FastAPI V3 문서 규칙

각 문서는 가능한 한 다음 순서와 깊이를 유지한다.

### 1. 개념의 정체

- 정확한 정의
- 비슷한 개념과 차이
- 수업에서 등장한 배경

### 2. 학습 이유

- 이 개념이 해결하는 문제
- 배우지 않았을 때 생기는 문제
- 다음 수업과 연결되는 지점

### 3. 값과 정보의 출처

- 주소창에서 입력됐는가?
- HTML Form의 `name`에서 왔는가?
- JavaScript `fetch()` Body에서 왔는가?
- Browser가 자동 생성한 Header·Cookie인가?
- Python 함수나 DB 조회 결과에서 만들어졌는가?

### 4. 실제 처리 흐름

```text
Client 행동
→ HTTP Request
→ Uvicorn
→ Middleware
→ Router
→ Parameter/Pydantic 검증
→ Endpoint
→ Jinja·Service·Database
→ Response Model
→ HTTP Response
→ Browser 결과
```

### 5. 실행 가능한 예제

- 실행 명령
- 요청 URL 또는 Form·JSON
- Python Source
- Terminal `print` 결과
- Browser·JSON 결과
- 변경 전후 Memory·DB 상태

### 6. 원본 수업 연결

- 내 코드의 파일과 함수
- 강사님 코드의 파일과 함수
- 같은 점과 다른 점
- 왜 결과가 달라지는지

### 7. 오류와 Debugging

- 재현 조건
- Status Code
- Terminal 오류
- 원인
- 수정 방법

### 8. 다시 사용하기

- 개선된 통합 예제
- 실무 주의점
- 종합실습
- 정답과 해설
- 최종 체크리스트

---

## 🔍 복습 방법

문서를 눈으로만 읽지 않고 다음 순서로 확인한다.

```text
1. “왜 필요한가”를 자신의 말로 설명한다.
2. 문서의 Request·Data 흐름을 손으로 그린다.
3. 수업 원본의 해당 함수 위치를 연다.
4. Uvicorn 또는 Python 파일을 직접 실행한다.
5. Browser 주소창·Form·API Client에서 요청한다.
6. 개발자 도구 Network를 확인한다.
7. Terminal print와 Server Log를 확인한다.
8. Browser·JSON·DB 결과를 문서 예시와 비교한다.
9. 의도적으로 잘못된 값을 보내 오류를 확인한다.
10. 문서를 보지 않고 최소 예제를 다시 작성한다.
```

---

## 🧭 Request를 볼 때 항상 확인할 것

```text
누가 요청했는가?       → Browser, Form, fetch, API Client
어떤 Method인가?       → GET, POST, PUT, PATCH, DELETE
어떤 Path인가?         → /todos/10
값은 어디에 있는가?   → Path, Query, Header, Cookie, Body
Body 형식은 무엇인가? → JSON, Form, Multipart
어디서 검증되는가?    → FastAPI Parameter, Pydantic Model
어떤 함수가 실행되는가?
무엇을 반환하는가?
어떤 Status와 Body가 Client에 돌아가는가?
```

---

## 📂 수업 Source 기준

```text
내 코드
workspace_python/02_todos/
├── api.py
├── 01_router/
├── 02_jinja/
├── 03_response/
├── 04_jinja_todo/
└── 05_SQLite/

강사님 코드
workspace_teacher/workspace_python/todos/
├── api.py
├── 01_router/
├── 02_jinja/
├── 03_response/
├── 04_jinja_todo/
└── 05_SQLite/
```

학습 중인 후속 Database 자료는 다음 정식 문서 작업에서 다룬다.

---

## 📌 Wiki 운영 원칙

- 수업 Source에서 실제 사용한 함수와 연결한다.
- 원본의 오류·실험 Code와 개선 예제를 구분한다.
- 단순히 “사용한다”로 끝내지 않고 입력부터 결과까지 설명한다.
- Browser, Terminal, Memory, Database에서 보이는 결과를 구분한다.
- 동작하지 않는 예제도 왜 실패하는지 기록한다.
- Version 변화로 달라질 수 있는 문법은 실행 환경을 함께 기록한다.
- 아직 배우지 않은 후속 수업을 완료된 내용처럼 섞지 않는다.
- 문서를 읽은 뒤 Source 없이 최소 예제를 재작성할 수 있어야 완료로 판단한다.

---

## 📎 Navigation

| Previous | Home | Next |
| :---: | :---: | :---: |
| [🗄️ SQL](../05_SQL/README.md) | [🏠 Developer-Wiki](../README.md) | 진행 예정 |

