# Developer-Wiki 통합 용어 색인

> **Keyword Index & Glossary** — 용어의 뜻을 짧게 확인하고, 가장 자세한 설명과 실제 사용 문서로 바로 이동하기 위한 Developer-Wiki의 통합 찾아보기다.

---

## 1. 이 문서를 사용하는 방법

각 항목은 다음 기준으로 정리한다.

| 구분 | 의미 |
|---|---|
| 용어 | 수업·문서에서 사용하는 대표 이름 |
| 뜻 | 처음 다시 봐도 기억을 되살릴 수 있는 짧은 설명 |
| 핵심 문서 | 해당 용어를 가장 자세히 설명하는 위치 |
| 관련 위치 | 다른 과목이나 실제 흐름에서 함께 확인할 문서 |
| 함께 검색 | 같은 뜻, 약어, 연관 표현 |

파일에 단어가 한 번 등장한다고 모두 색인에 넣지는 않는다. 다시 학습할 가치가 있는 개념을 선정하고, 단순 등장 위치보다 **가장 자세한 설명 → 실제 적용 위치** 순서로 연결한다.

---

## 2. 상황별 빠른 찾아보기

| 궁금한 상황 | 찾아볼 Keyword | 먼저 볼 문서 |
|---|---|---|
| Framework와 Library 차이가 기억나지 않는다 | Framework, Library, 제어의 역전 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) |
| 주소창·폼·JSON 값이 서버 어디로 들어오는지 궁금하다 | Request, Path, Query, Body, Form | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) |
| `[a-zA-Z]`처럼 문자를 필터링하고 싶다 | 정규표현식, 문자 클래스, 범위 | [Python 정규표현식](./04_Python/18_Python_정규표현식.md) |
| HTML 입력값이 왜 문자열인지 궁금하다 | form, input.value, name/value | [HTML 폼](./01_HTML/07_HTML_폼과_입력요소.md), [JavaScript 폼 값](./03_JavaScript/13_JavaScript_DOM_폼요소와_입력값처리.md) |
| CSS가 적용되지 않거나 덮어써진다 | 선택자, 캐스케이드, 우선순위, 상속 | [CSS 선택자](./02_CSS/01_CSS_선택자와_적용방법.md) |
| 요소가 생각한 위치에 나타나지 않는다 | 박스 모델, display, position, containing block | [CSS 박스 모델](./02_CSS/03_CSS_박스모델.md), [CSS Position](./02_CSS/08_CSS_Position과_요소위치.md) |
| 클릭했을 때 함수가 언제 실행되는지 궁금하다 | Event, Listener, Callback, Event Loop | [JavaScript 이벤트 루프](./03_JavaScript/14_JavaScript_동기비동기와_이벤트루프.md) |
| API 응답이 바로 값으로 나오지 않는다 | Promise, async/await, Fetch, Response | [AJAX와 Fetch](./03_JavaScript/20_JavaScript_AJAX와_Fetch_API.md) |
| 변수 두 개를 바꿨는데 값이 같이 변한다 | 참조, Stack, Heap, Mutable | [메모리와 참조](./00_메모리와_참조%28Stack_Heap%29/01_메모리와_참조%28Stack_Heap%29.md) |
| Python 함수 결과가 화면에 안 보인다 | print, return, None | [Python 함수](./04_Python/11_Python_함수.md) |
| 반복문이 값을 하나씩 가져오는 원리가 궁금하다 | Iterable, Iterator, Generator | [Python 이터레이터](./04_Python/16_Python_이터레이터.md) |
| SQL에서 데이터가 중복되거나 행 수가 늘어난다 | JOIN, 조인 조건, 카디널리티 | [SQL JOIN](./05_SQL/12_SQL_JOIN.md) |
| SQL 변경을 취소하거나 확정하고 싶다 | Transaction, COMMIT, ROLLBACK | [SQL Transaction](./05_SQL/16_SQL_Transaction.md) |
| FastAPI 반환값과 실제 HTTP 응답의 차이가 궁금하다 | Response, response_model, Status Code | [FastAPI Response](./06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) |
| 브라우저 요청이 CORS로 차단된다 | Origin, CORS, Middleware | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) |
| SQLite 데이터 변경이 저장되지 않는다 | Connection, Cursor, Transaction, commit | [Python SQLite](./06_FastAPI/06_Python_SQLite와_Transaction.md) |

---

## 3. 공통 개발·실행 개념

| Keyword | 뜻 | 핵심 문서 | 관련 위치·함께 검색 |
|---|---|---|---|
| Algorithm · 알고리즘 | 입력을 원하는 출력으로 바꾸는 명확한 처리 절차 | [Python 종합실습](./04_Python/20_Python_종합실습.md) | 조건문, 반복문, 함수, 문제 해결 |
| Application · 애플리케이션 | 사용자의 목적을 수행하도록 여러 기능을 결합한 프로그램 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | App, Program, Server |
| Client · 클라이언트 | 서버에 요청을 보내고 응답을 사용하는 주체 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | Browser, Request, Server |
| Server · 서버 | Client의 요청을 받아 처리하고 응답하는 프로그램 또는 환경 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | Uvicorn, FastAPI, Response |
| Library · 라이브러리 | 개발자 코드가 필요할 때 호출해 사용하는 기능 모음 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | Framework와 차이, Package |
| Framework · 프레임워크 | 애플리케이션의 구조와 실행 흐름을 제공하고 정해진 지점에서 개발자 코드를 호출하는 기반 | [FastAPI 웹 API 기초 — 2.2](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | Library, 제어의 역전, FastAPI |
| Runtime · 런타임 | 작성된 코드가 실제로 실행되는 환경과 시점 | [Python 실행 방식](./04_Python/00-01_Python_실행방식과_프로그래밍_패러다임.md) | Browser Runtime, Python Interpreter |
| Package · 패키지 | 설치·배포하거나 관련 모듈을 묶는 단위 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | pip, requirements.txt, Module |
| Module · 모듈 | 다른 코드에서 가져와 재사용할 수 있는 Python 파일 또는 코드 단위 | [Python 모듈과 import](./04_Python/15_Python_모듈과_import.md) | import, `__name__`, Package |
| Environment Variable · 환경변수 | 운영체제가 프로세스에 전달하는 이름·값 설정 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | PATH, Secret, API Key |
| Virtual Environment · venv | 프로젝트별 Python 실행 환경과 설치 패키지를 격리하는 폴더 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | activate, pip, requirements.txt |
| Dependency · 의존성 | 한 코드나 패키지가 실행되기 위해 필요로 하는 다른 기능 | [FastAPI Response와 의존성 주입](./06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) | DI, pip dependency |
| Dependency Injection · 의존성 주입 | 필요한 객체나 값을 함수 내부에서 직접 만들지 않고 외부 흐름이 제공하는 방식 | [FastAPI Response와 의존성 주입](./06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) | `Depends`, 재사용, 테스트 |
| MVC Pattern | Model·View·Controller로 데이터, 화면, 요청 제어 책임을 나누는 설계 패턴 | [FastAPI Jinja Todo CRUD](./06_FastAPI/05_FastAPI_Jinja_Todo_CRUD.md) | Model, Template, Router |
| Debugging · 디버깅 | 관찰 가능한 증거를 이용해 문제 원인을 좁히고 수정하는 과정 | [Python 오류와 예외](./04_Python/00-02_Python_오류와_예외.md) | Console, Traceback, Network, 최소 재현 |
| Serialization · 직렬화 | 메모리의 객체나 값을 저장·전송 가능한 문자열 또는 바이트 형식으로 바꾸는 것 | [Python 파일과 직렬화](./04_Python/10_Python_파일입출력과_직렬화.md) | JSON, pickle, 역직렬화 |
| Stack · 스택 | 함수 호출과 지역 실행 정보 등을 후입선출 구조로 다루는 개념 | [메모리와 참조](./00_메모리와_참조%28Stack_Heap%29/01_메모리와_참조%28Stack_Heap%29.md) | Call Stack, Frame, Heap |
| Heap · 힙 | 실행 중 생성된 객체가 관리되는 메모리 영역을 설명할 때 사용하는 개념 | [메모리와 참조](./00_메모리와_참조%28Stack_Heap%29/01_메모리와_참조%28Stack_Heap%29.md) | Object, Reference, GC |
| Reference · 참조 | 변수나 컬렉션이 객체 자체를 복제하지 않고 같은 객체를 가리키는 관계 | [메모리와 참조](./00_메모리와_참조%28Stack_Heap%29/01_메모리와_참조%28Stack_Heap%29.md) | 얕은 복사, 동일성, Mutable |

---

## 4. HTML · CSS Keyword

| Keyword | 뜻 | 핵심 문서 | 관련 위치·함께 검색 |
|---|---|---|---|
| HTML | 콘텐츠의 구조와 의미를 요소로 표현하는 마크업 언어 | [HTML 기초](./01_HTML/01_HTML_기초와_문서구조.md) | Tag, Element, DOM |
| Tag · 태그 | HTML 파서에 요소의 시작·종료와 종류를 알리는 마크업 표기 | [HTML 기본 태그](./01_HTML/02_HTML_기본태그.md) | Element와 차이, Attribute |
| Element · 요소 | 시작 태그·속성·콘텐츠·종료 태그로 구성되어 DOM 노드가 되는 단위 | [HTML V3 읽기법](./01_HTML/00_HTML_V3_동작_백과_읽기법.md) | Node, DOM, Tag |
| Attribute · 속성 | HTML 요소에 주소, 이름, 상태 같은 추가 정보를 제공하는 값 | [HTML 기본 태그](./01_HTML/02_HTML_기본태그.md) | `href`, `src`, `id`, `name` |
| Semantic HTML · 시맨틱 HTML | 모양보다 콘텐츠의 역할과 의미에 맞는 요소를 사용하는 방식 | [HTML 시맨틱 태그](./01_HTML/08_HTML_시맨틱태그와_페이지구조.md) | header, nav, main, article |
| Accessibility · 접근성 | 장애·환경·입력 방식과 관계없이 콘텐츠와 기능을 사용할 수 있게 하는 품질 | [HTML 실무 스타일](./01_HTML/09_HTML_실무_코딩스타일.md) | label, alt, keyboard, ARIA |
| URL · 경로 | 브라우저가 문서와 자원의 위치를 식별하는 주소 | [HTML 링크와 경로](./01_HTML/03_HTML_링크와_경로.md) | 상대 경로, 절대 URL, 404 |
| Form · 폼 | 사용자 입력을 컨트롤의 `name=value` 쌍으로 모아 제출하는 HTML 구조 | [HTML 폼](./01_HTML/07_HTML_폼과_입력요소.md) | action, method, input, submit |
| CSS | HTML 요소의 표시, 크기, 위치와 시각적 표현을 지정하는 스타일 언어 | [CSS V3 읽기법](./02_CSS/00_CSS_V3_동작_백과_읽기법.md) | CSSOM, Layout, Paint |
| Selector · 선택자 | CSS 규칙을 적용할 DOM 요소를 찾는 표현식 | [CSS 선택자](./02_CSS/01_CSS_선택자와_적용방법.md) | class, id, pseudo-class |
| Cascade · 캐스케이드 | 여러 CSS 선언 중 최종 적용 선언을 결정하는 규칙 체계 | [CSS 선택자](./02_CSS/01_CSS_선택자와_적용방법.md) | 중요도, 우선순위, 작성 순서 |
| Specificity · 우선순위 | 같은 요소와 속성에 경쟁하는 선택자의 구체성을 비교하는 값 | [CSS 선택자](./02_CSS/01_CSS_선택자와_적용방법.md) | inline, id, class, element |
| Inheritance · 상속 | 일부 CSS 속성의 계산값이 부모에서 자식으로 전달되는 동작 | [CSS 선택자](./02_CSS/01_CSS_선택자와_적용방법.md) | computed style, initial, inherit |
| Box Model · 박스 모델 | content·padding·border·margin으로 요소 크기와 간격을 계산하는 구조 | [CSS 박스 모델](./02_CSS/03_CSS_박스모델.md) | content-box, border-box |
| Display | 요소가 만드는 박스 유형과 배치 흐름을 정하는 CSS 속성 | [CSS Display](./02_CSS/04_CSS_Display와_요소배치.md) | block, inline, none |
| Position | 요소의 위치 기준과 offset 적용 방식을 정하는 CSS 속성 | [CSS Position](./02_CSS/08_CSS_Position과_요소위치.md) | relative, absolute, fixed, sticky |
| Containing Block | percentage나 absolute 위치 계산의 기준이 되는 조상 영역 | [CSS Position](./02_CSS/08_CSS_Position과_요소위치.md) | position, percentage |
| Overflow | 콘텐츠가 요소 박스 경계를 넘을 때 자르거나 스크롤하는 방식 | [CSS Overflow](./02_CSS/09_CSS_Overflow와_스크롤.md) | hidden, auto, scroll |
| Responsive Web · 반응형 | viewport와 콘텐츠 조건에 따라 레이아웃을 적응시키는 설계 | [CSS 미디어 쿼리](./02_CSS/14_CSS_미디어쿼리와_반응형.md) | breakpoint, viewport, mobile first |
| Media Query | 미디어 특성 조건이 참일 때 CSS 규칙을 적용하는 문법 | [CSS 미디어 쿼리](./02_CSS/14_CSS_미디어쿼리와_반응형.md) | `@media`, width, breakpoint |
| Flexbox | 주축·교차축과 남는 공간을 기준으로 item을 배치하는 1차원 레이아웃 | [CSS Flexbox](./02_CSS/15_CSS_Flexbox와_유연한_레이아웃.md) | container, item, justify, align |
| Transition | CSS 계산값이 바뀔 때 중간 상태를 시간에 따라 보간하는 기능 | [CSS Transition](./02_CSS/12_CSS_Transition과_상태변화.md) | hover, duration, easing |
| Transform | layout 자리와 별개로 요소의 그려지는 결과를 이동·회전·확대하는 기능 | [CSS Transform](./02_CSS/13_CSS_Transform과_요소변형.md) | translate, rotate, scale |

---

## 5. JavaScript · Browser Keyword

| Keyword | 뜻 | 핵심 문서 | 관련 위치·함께 검색 |
|---|---|---|---|
| DOM | 브라우저가 HTML을 객체 노드의 트리로 표현한 Document Object Model | [DOM 선택과 조작](./03_JavaScript/11_JavaScript_DOM_선택과_속성_클래스조작.md) | document, Element, Node |
| BOM | 페이지 밖의 브라우저 창·주소·기록·환경을 다루는 Browser Object Model | [BOM과 지도 API](./03_JavaScript/18_JavaScript_BOM과_지도우편번호API.md) | window, location, history |
| Variable · 변수 | 값을 다시 사용하기 위해 이름을 연결하는 기능 | [JavaScript 변수](./03_JavaScript/01_JavaScript_변수와_자료형.md) | `let`, `const`, scope |
| Type Coercion · 형 변환 | 연산 과정에서 값의 자료형이 명시적 또는 암묵적으로 바뀌는 동작 | [JavaScript 연산자](./03_JavaScript/02_JavaScript_연산자.md) | Number, String, `===`, truthy |
| Array · 배열 | 여러 값을 순서와 index로 관리하는 JavaScript 객체 | [JavaScript 배열](./03_JavaScript/06_JavaScript_배열과_배열메서드.md) | map, filter, push, sort |
| Function · 함수 | 입력을 받아 코드를 실행하고 결과를 반환할 수 있는 재사용 단위 | [JavaScript 함수](./03_JavaScript/08_JavaScript_함수와_콜백_타이머.md) | parameter, argument, return |
| Callback · 콜백 | 다른 함수나 API에 전달되어 특정 시점에 호출되는 함수 | [JavaScript 함수와 타이머](./03_JavaScript/08_JavaScript_함수와_콜백_타이머.md) | Event Listener, Timer, async |
| Arrow Function · 화살표 함수 | 간결한 함수 표현식이며 자체 `this`를 만들지 않는 JavaScript 함수 형태 | [화살표 함수](./03_JavaScript/09_JavaScript_화살표함수와_TV상태관리.md) | lexical this, callback |
| Event · 이벤트 | 클릭·입력·제출·로딩처럼 브라우저에서 발생한 동작 정보 | [DOM 이벤트](./03_JavaScript/15_JavaScript_DOM이벤트와_키보드스크롤제어.md) | Event 객체, target, listener |
| Event Listener | 특정 이벤트가 발생했을 때 실행할 콜백을 등록하는 기능 | [DOM 이벤트](./03_JavaScript/15_JavaScript_DOM이벤트와_키보드스크롤제어.md) | `addEventListener`, callback |
| Event Propagation · 이벤트 전파 | 이벤트가 조상에서 target으로 내려가고 다시 올라가는 과정 | [폼 이벤트와 전파](./03_JavaScript/17_JavaScript_폼이벤트와_이벤트전파_실전문제.md) | capture, target, bubble |
| preventDefault | 링크 이동·폼 제출 같은 브라우저 기본 동작을 막는 Event 메서드 | [폼 이벤트와 전파](./03_JavaScript/17_JavaScript_폼이벤트와_이벤트전파_실전문제.md) | submit, default action |
| Event Loop | 호출 스택과 작업 큐를 확인하며 실행 가능한 비동기 작업을 전달하는 동작 모델 | [동기·비동기와 이벤트 루프](./03_JavaScript/14_JavaScript_동기비동기와_이벤트루프.md) | Call Stack, Task, Microtask |
| Synchronous · 동기 | 앞 작업이 끝나야 다음 문장을 실행하는 기본 처리 흐름 | [동기·비동기](./03_JavaScript/14_JavaScript_동기비동기와_이벤트루프.md) | Call Stack, blocking |
| Asynchronous · 비동기 | 완료를 기다리는 동안 다른 작업을 진행하고 나중에 결과를 처리하는 방식 | [동기·비동기](./03_JavaScript/14_JavaScript_동기비동기와_이벤트루프.md) | callback, Promise, timer |
| Promise | 비동기 작업의 대기·성공·실패 상태와 미래 결과를 표현하는 객체 | [AJAX와 Fetch](./03_JavaScript/20_JavaScript_AJAX와_Fetch_API.md) | pending, fulfilled, rejected |
| async / await | Promise 기반 비동기 코드를 순차적으로 읽히게 작성하는 문법 | [AJAX와 Fetch](./03_JavaScript/20_JavaScript_AJAX와_Fetch_API.md) | Promise, try/catch |
| AJAX | 페이지 전체를 다시 열지 않고 서버와 데이터를 교환해 일부 화면을 갱신하는 방식 | [AJAX와 Fetch](./03_JavaScript/20_JavaScript_AJAX와_Fetch_API.md) | Fetch, XMLHttpRequest |
| Fetch API | 브라우저에서 HTTP 요청을 보내고 Promise로 Response를 받는 Web API | [AJAX와 Fetch](./03_JavaScript/20_JavaScript_AJAX와_Fetch_API.md) | `response.ok`, json, CORS |
| XMLHttpRequest · XHR | 이벤트와 상태값으로 HTTP 통신을 처리하는 전통적인 브라우저 API | [Discord Webhook과 XHR](./03_JavaScript/22_JavaScript_Discord_Webhook과_XMLHttpRequest.md) | readyState, status, AJAX |
| JSON | 객체·배열·문자열·숫자 등을 텍스트로 교환하는 데이터 형식 | [JavaScript JSON](./03_JavaScript/19_JavaScript_JSON과_객체직렬화.md) | stringify, parse, 직렬화 |
| Regular Expression · 정규표현식 | 문자열의 검색·검사·추출·치환 규칙을 표현하는 패턴 문법 | [Python 정규표현식](./04_Python/18_Python_정규표현식.md) | regex, regexp, [a-zA-Z], JavaScript 문자열 |
| Character Class · 문자 클래스 | 대괄호 안에 허용할 문자 집합이나 범위를 지정하는 정규식 구성 | [Python 정규표현식 — 문자 범위](./04_Python/18_Python_정규표현식.md) | `[a-z]`, `[A-Z]`, `\d`, 부정 클래스 |
| `[a-zA-Z]` | 영문 소문자 a~z 또는 대문자 A~Z 한 글자와 일치하는 문자 범위 | [Python 정규표현식 — 9. 문자 범위](./04_Python/18_Python_정규표현식.md) | `[a-Z]`는 올바른 연속 범위가 아님 |

---

## 6. Python Keyword

| Keyword | 뜻 | 핵심 문서 | 관련 위치·함께 검색 |
|---|---|---|---|
| Interpreter · 인터프리터 | Python 소스와 바이트코드를 읽고 실행하는 프로그램 | [Python 실행 방식](./04_Python/00-01_Python_실행방식과_프로그래밍_패러다임.md) | bytecode, Python VM |
| Object · 객체 | 자료형, 값, 동작과 정체성을 가진 Python 실행 단위 | [Python 클래스](./04_Python/12_Python_클래스.md) | instance, reference, type |
| Mutable · 변경 가능 | 객체 생성 후 내부 상태나 원소를 바꿀 수 있는 성질 | [Python 리스트](./04_Python/04_Python_리스트와_데이터처리.md) | list, dict, set, alias |
| Immutable · 불변 | 객체 생성 후 그 객체의 값을 직접 바꿀 수 없는 성질 | [Python 튜플](./04_Python/05_Python_튜플과_불변자료형.md) | str, tuple, 새 객체 |
| Sequence · 시퀀스 | 순서·index·slice 규칙을 공유하는 자료형 계열 | [Python 시퀀스](./04_Python/06_Python_시퀀스와_슬라이싱.md) | str, list, tuple, range |
| Slice · 슬라이싱 | `start:stop:step`으로 시퀀스의 범위를 선택하는 문법 | [Python 시퀀스](./04_Python/06_Python_시퀀스와_슬라이싱.md) | index, 음수, 얕은 복사 |
| Dictionary · 딕셔너리 | 해시 가능한 key와 value의 연결을 저장하는 자료형 | [Python 딕셔너리와 집합](./04_Python/07_Python_딕셔너리와_집합.md) | dict, key, get, hash |
| Set · 집합 | 중복 없이 해시 가능한 값을 보관하는 자료형 | [Python 딕셔너리와 집합](./04_Python/07_Python_딕셔너리와_집합.md) | 합집합, 교집합, 포함 검사 |
| Scope · 변수 범위 | 이름을 찾고 사용할 수 있는 코드 영역 | [Python 함수](./04_Python/11_Python_함수.md) | local, global, LEGB |
| Class · 클래스 | 객체의 상태와 관련 동작을 정의하고 인스턴스를 만드는 설계 | [Python 클래스](./04_Python/12_Python_클래스.md) | instance, self, `__init__` |
| Inheritance · 상속 | 자식 클래스가 부모의 속성과 메서드를 이어받아 확장하는 기능 | [Python 상속](./04_Python/13_Python_상속과_다형성.md) | override, super, MRO |
| Polymorphism · 다형성 | 같은 호출이 실제 객체 유형에 따라 다른 구현을 실행하는 성질 | [Python 상속](./04_Python/13_Python_상속과_다형성.md) | overriding, duck typing |
| Exception · 예외 | 실행 중 정상 흐름을 계속할 수 없음을 나타내는 객체와 전달 메커니즘 | [Python 예외 처리](./04_Python/14_Python_예외처리.md) | try, except, raise, finally |
| Traceback | 예외가 발생해 전달된 함수 호출 경로와 위치 정보 | [Python 오류와 예외](./04_Python/00-02_Python_오류와_예외.md) | 마지막 줄, 예외 클래스, line |
| Iterable · 이터러블 | `iter()`로 이터레이터를 제공할 수 있는 객체 | [Python 이터레이터](./04_Python/16_Python_이터레이터.md) | for, collection, iterator |
| Iterator · 이터레이터 | 현재 위치를 기억하고 `next()`로 값을 하나씩 제공하는 객체 | [Python 이터레이터](./04_Python/16_Python_이터레이터.md) | StopIteration, iter, next |
| Generator · 제너레이터 | `yield`에서 실행 상태를 멈추고 요청 때 다시 이어가는 이터레이터 | [Python 제너레이터](./04_Python/17_Python_제너레이터.md) | yield, lazy evaluation |
| File Object · 파일 객체 | 파일 읽기·쓰기와 위치·닫기 상태를 관리하는 Python 객체 | [Python 파일 입출력](./04_Python/10_Python_파일입출력과_직렬화.md) | open, with, encoding |
| `print` | 값을 문자열 표현으로 바꿔 표준 출력에 보내는 함수 | [Python 출력](./04_Python/01_Python_출력과_주석.md) | stdout, sep, end |
| `return` | 함수 실행을 끝내고 호출한 위치로 값을 돌려주는 문장 | [Python 함수](./04_Python/11_Python_함수.md) | 반환값, None, print와 차이 |

---

## 7. SQL · Database Keyword

| Keyword | 뜻 | 핵심 문서 | 관련 위치·함께 검색 |
|---|---|---|---|
| DBMS | 데이터베이스를 생성·조회·변경·관리하는 소프트웨어 | [SQL 기초](./05_SQL/01_SQL_기초와_SELECT.md) | MariaDB, SQLite, Database |
| Table · 테이블 | 행과 열 구조로 같은 종류의 데이터를 저장하는 관계형 객체 | [SQL DDL](./05_SQL/14_SQL_DDL과_제약조건.md) | row, column, schema |
| SELECT | 테이블이나 쿼리 결과에서 필요한 데이터를 조회하는 문장 | [SQL SELECT](./05_SQL/01_SQL_기초와_SELECT.md) | projection, alias, result set |
| WHERE | 각 행에 조건을 적용해 조회·변경 대상을 제한하는 절 | [SQL WHERE](./05_SQL/02_SQL_WHERE와_조건연산자.md) | 비교, AND, OR, IN |
| LIKE | `%`, `_` wildcard를 사용해 문자열 패턴을 비교하는 SQL 연산자 | [SQL LIKE와 NULL](./05_SQL/03_SQL_LIKE와_NULL.md) | wildcard, escape, 정규식과 차이 |
| NULL | 값이 없거나 알려지지 않았음을 나타내며 일반 비교 대신 IS NULL을 사용하는 상태 | [SQL LIKE와 NULL](./05_SQL/03_SQL_LIKE와_NULL.md) | three-valued logic, COALESCE |
| Aggregate Function · 집계함수 | 여러 행을 계산해 COUNT·SUM·AVG·MIN·MAX 같은 요약값을 만드는 함수 | [SQL 집계함수](./05_SQL/05_SQL_집계함수.md) | NULL 처리, group |
| GROUP BY | 같은 기준값의 행을 그룹으로 묶어 그룹별 집계를 계산하는 절 | [GROUP BY와 HAVING](./05_SQL/06_SQL_GROUP_BY와_HAVING.md) | aggregate, grouping |
| HAVING | GROUP BY로 만들어진 그룹과 집계 결과를 필터링하는 절 | [GROUP BY와 HAVING](./05_SQL/06_SQL_GROUP_BY와_HAVING.md) | WHERE와 차이, aggregate |
| CASE | 조건에 따라 행별 결과값을 선택하는 SQL 조건식 | [SQL CASE](./05_SQL/09_SQL_CASE_조건식.md) | WHEN, THEN, ELSE |
| UNION | 두 조회 결과를 세로로 합치고 중복을 제거하는 집합 연산 | [SQL UNION](./05_SQL/10_SQL_UNION과_UNION_ALL.md) | UNION ALL, column 호환 |
| Subquery · 서브쿼리 | 다른 SQL 문 내부에서 먼저 또는 연관되어 사용되는 조회 | [SQL 서브쿼리](./05_SQL/11_SQL_서브쿼리.md) | scalar, IN, EXISTS, correlated |
| JOIN | 관련 열의 조건으로 여러 테이블의 행을 하나의 결과로 결합하는 연산 | [SQL JOIN](./05_SQL/12_SQL_JOIN.md) | INNER, ON, cardinality |
| OUTER JOIN | 일치하지 않는 한쪽 행도 NULL과 함께 결과에 남기는 조인 | [Outer JOIN](./05_SQL/13_SQL_Outer_JOIN과_Self_JOIN.md) | LEFT, RIGHT, unmatched row |
| SELF JOIN | 하나의 테이블에 서로 다른 별칭을 주어 자기 자신과 조인하는 방식 | [Self JOIN](./05_SQL/13_SQL_Outer_JOIN과_Self_JOIN.md) | hierarchy, employee-manager |
| DDL | 테이블·제약조건 같은 DB 구조를 정의하거나 변경하는 SQL 분류 | [SQL DDL](./05_SQL/14_SQL_DDL과_제약조건.md) | CREATE, ALTER, DROP |
| DML | 테이블의 실제 행을 추가·수정·삭제하는 SQL 분류 | [SQL DML](./05_SQL/15_SQL_DML.md) | INSERT, UPDATE, DELETE |
| Constraint · 제약조건 | DB에 저장될 수 있는 데이터 규칙을 스키마 수준에서 보장하는 기능 | [SQL DDL과 제약조건](./05_SQL/14_SQL_DDL과_제약조건.md) | NOT NULL, UNIQUE, CHECK, FK |
| Primary Key · 기본키 | 각 행을 유일하게 식별하며 NULL을 허용하지 않는 키 | [SQL DDL과 제약조건](./05_SQL/14_SQL_DDL과_제약조건.md) | PK, UNIQUE, AUTO_INCREMENT |
| Foreign Key · 외래키 | 다른 테이블의 후보키를 참조해 관계와 참조 무결성을 보장하는 제약 | [SQL DDL과 제약조건](./05_SQL/14_SQL_DDL과_제약조건.md) | FK, referential integrity |
| Transaction · 트랜잭션 | 여러 데이터 변경을 하나의 논리적 업무 단위로 처리하는 범위 | [SQL Transaction](./05_SQL/16_SQL_Transaction.md) | ACID, commit, rollback |
| COMMIT | 현재 트랜잭션의 변경을 확정해 영구 반영하는 명령 | [SQL Transaction](./05_SQL/16_SQL_Transaction.md) | autocommit, SQLite commit |
| ROLLBACK | 아직 확정하지 않은 트랜잭션 변경을 취소하는 명령 | [SQL Transaction](./05_SQL/16_SQL_Transaction.md) | savepoint, commit 이후 불가 |
| Index · 인덱스 | 특정 열 값으로 행을 더 빠르게 찾도록 별도 탐색 구조를 유지하는 DB 객체 | [SQL Index](./05_SQL/17_SQL_Index와_AUTO_INCREMENT.md) | scan, selectivity, write cost |
| AUTO_INCREMENT | 새 행에 증가하는 정수값을 자동 생성하는 MariaDB 열 속성 | [SQL Index와 AUTO_INCREMENT](./05_SQL/17_SQL_Index와_AUTO_INCREMENT.md) | PK, sequence, last id |
| CTE | 이름을 붙인 임시 쿼리 결과를 한 SQL 문에서 재사용하는 표현 | [Recursive CTE](./05_SQL/18_SQL_Recursive_CTE.md) | WITH, anchor, recursive member |

---

## 8. HTTP · FastAPI Keyword

| Keyword | 뜻 | 핵심 문서 | 관련 위치·함께 검색 |
|---|---|---|---|
| HTTP | Client와 Server가 요청·응답을 교환하는 Web 통신 규칙 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | method, URL, header, body |
| Port · 포트 | 한 컴퓨터에서 요청을 받을 네트워크 프로그램을 구분하는 번호 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | 80, 443, 8000, localhost |
| API | 서로 다른 프로그램이 정해진 방식으로 기능과 데이터를 요청하도록 제공하는 접점 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | Web API, endpoint, contract |
| REST | Resource를 URL로 표현하고 HTTP 의미를 활용하는 API 설계 원칙 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | RESTful, CRUD, stateless |
| CRUD | 데이터의 Create·Read·Update·Delete 네 가지 기본 작업 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | POST, GET, PUT/PATCH, DELETE |
| HTTP Method | 요청의 의도를 나타내는 GET·POST·PUT·PATCH·DELETE 등의 값 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | CRUD, idempotent, route |
| Routing · 라우팅 | HTTP method와 path를 해석해 실행할 endpoint 함수를 선택하는 과정 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | Router, endpoint, decorator |
| Endpoint | 특정 HTTP method와 URL로 접근할 수 있는 API 기능의 접점 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | path operation, route |
| Request · 요청 | Client가 Server에 보내는 method, URL, header, cookie, body 등의 정보 묶음 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | Starlette Request, Browser, HTTP |
| Path Parameter · 경로 매개변수 | URL 경로의 일부로 Resource 식별값을 전달하는 입력 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | `/todos/{id}`, Path, validation |
| Query Parameter · 쿼리 매개변수 | URL의 `?key=value` 부분으로 선택 조건이나 옵션을 전달하는 입력 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | Query, search, pagination |
| Header | HTTP 요청·응답의 본문 밖에서 형식·인증·캐시 같은 부가정보를 전달하는 영역 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | Content-Type, Authorization |
| Cookie | Browser가 저장했다가 같은 범위의 요청 Header에 함께 보내는 작은 문자열 정보 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | session, Set-Cookie, security |
| Request Body | POST·PUT·PATCH 등에서 구조화된 데이터를 전송하는 HTTP 본문 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | JSON, Pydantic, Form |
| Request 객체 | 이미 들어온 HTTP 요청의 URL·method·headers·cookies 등 원본 정보에 접근하는 객체 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | `request.url`, `request.headers` |
| Response · 응답 | Server가 Client에 보내는 status, headers, body의 정보 묶음 | [FastAPI Response](./06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) | JSONResponse, HTMLResponse |
| Status Code · 상태 코드 | HTTP 요청 처리 결과를 2xx·3xx·4xx·5xx 숫자로 표현한 값 | [FastAPI Response](./06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) | 200, 201, 302/303, 404, 422 |
| Redirect · 리다이렉트 | Server가 3xx와 Location을 보내 Browser에 다른 URL을 다시 요청하게 하는 응답 | [FastAPI Response](./06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) | RedirectResponse, PRG |
| Pydantic | 입력·출력 데이터의 자료형, 구조와 검증 규칙을 선언하는 Python Library | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | BaseModel, DTO, validation |
| DTO | 계층이나 프로그램 사이에서 전달할 데이터 구조를 정의하는 객체 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | Data Transfer Object, Schema |
| Validation · 검증 | 외부 값이 요구 자료형·범위·길이·형식에 맞는지 확인하는 과정 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | Path, Query, gt/ge/lt/le, 422 |
| response_model | FastAPI가 endpoint 반환값을 지정 Schema로 검증·변환·문서화하도록 하는 설정 | [FastAPI Response](./06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) | return annotation, output validation |
| Middleware · 미들웨어 | endpoint 전후에서 여러 요청에 공통 처리를 적용하는 계층 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | CORS, logging, request pipeline |
| Origin | URL의 scheme·host·port 조합으로 브라우저가 출처를 구분하는 기준 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | `http://localhost:5500`, 8000 |
| CORS | 다른 Origin의 JavaScript 요청을 Server 응답 Header로 허용할지 판단하는 Browser 보안 규칙 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) | preflight, middleware, same-origin |
| ASGI | Python 비동기 Web Server와 Application이 요청·응답을 주고받는 표준 인터페이스 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | Uvicorn, FastAPI, async |
| Uvicorn | FastAPI ASGI Application을 실제 Port에서 실행하고 요청을 전달하는 Server | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) | `uvicorn api:app`, reload |
| Jinja2 | Python 데이터를 이용해 Server에서 최종 HTML 문자열을 만드는 Template Engine | [FastAPI Jinja2](./06_FastAPI/03_FastAPI_Jinja2_템플릿.md) | template, context, SSR |
| Template · 템플릿 | 고정 HTML 구조와 동적으로 주입할 값·제어문을 함께 정의한 파일 | [FastAPI Jinja2](./06_FastAPI/03_FastAPI_Jinja2_템플릿.md) | render, context, layout, macro |
| SSR · Server-Side Rendering | Server가 데이터를 반영한 완성 HTML을 만들어 Browser에 응답하는 렌더링 방식 | [FastAPI Jinja2](./06_FastAPI/03_FastAPI_Jinja2_템플릿.md) | Jinja2, HTMLResponse |
| SQLite | 별도 Server 없이 하나의 파일 중심으로 사용하는 경량 관계형 DBMS | [Python SQLite](./06_FastAPI/06_Python_SQLite와_Transaction.md) | connection, cursor, transaction |
| Connection | Python 프로그램과 Database 사이의 작업 세션과 Transaction을 관리하는 객체 | [Python SQLite](./06_FastAPI/06_Python_SQLite와_Transaction.md) | connect, commit, rollback, close |
| Cursor | SQL 실행과 결과 행 순회를 담당하는 Database 객체 | [Python SQLite](./06_FastAPI/06_Python_SQLite와_Transaction.md) | execute, fetchone, fetchall |

---

## 9. 혼동하기 쉬운 용어 비교

| 혼동하는 용어 | 핵심 차이 | 자세히 보기 |
|---|---|---|
| Library vs Framework | 내 코드가 Library를 호출하는가, Framework가 정해진 시점에 내 코드를 호출하는가 | [FastAPI 웹 API 기초](./06_FastAPI/01_FastAPI_가상환경과_웹_API_기초.md) |
| Tag vs Element | Tag는 마크업 표기, Element는 브라우저가 구조로 다루는 전체 단위 | [HTML V3 읽기법](./01_HTML/00_HTML_V3_동작_백과_읽기법.md) |
| id vs name | id는 DOM·label 연결 식별자, name은 폼 제출 데이터의 key | [HTML 폼](./01_HTML/07_HTML_폼과_입력요소.md) |
| display:none vs visibility:hidden vs opacity:0 | 박스 제거, 공간 유지 숨김, 투명하지만 상호작용 가능 상태의 차이 | [CSS 요소 숨김](./02_CSS/05_CSS_투명도와_요소숨김.md) |
| `==` vs `===` | JavaScript의 암묵적 변환 비교와 자료형까지 같은 엄격 비교 | [JavaScript 연산자](./03_JavaScript/02_JavaScript_연산자.md) |
| print vs return | 표준 출력에 표시하는 함수와 호출자에게 값을 돌려주는 문장 | [Python 함수](./04_Python/11_Python_함수.md) |
| Iterable vs Iterator | iterator를 만들 수 있는 객체와 다음 값을 직접 제공하는 상태 객체 | [Python 이터레이터](./04_Python/16_Python_이터레이터.md) |
| WHERE vs HAVING | 행을 그룹화 전에 거르는 절과 그룹·집계 결과를 거르는 절 | [GROUP BY와 HAVING](./05_SQL/06_SQL_GROUP_BY와_HAVING.md) |
| UNION vs JOIN | 결과를 세로로 합치는 집합 연산과 관련 열로 가로 결합하는 연산 | [SQL UNION](./05_SQL/10_SQL_UNION과_UNION_ALL.md), [SQL JOIN](./05_SQL/12_SQL_JOIN.md) |
| DELETE vs DROP | 테이블의 행을 삭제하는 DML과 테이블 구조 자체를 제거하는 DDL | [SQL DML](./05_SQL/15_SQL_DML.md), [SQL DDL](./05_SQL/14_SQL_DDL과_제약조건.md) |
| Path vs Query | URL 경로에 포함된 Resource 식별값과 `?key=value` 선택 옵션 | [FastAPI Request와 CRUD](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) |
| Request vs Response | Client가 Server로 보내는 정보와 Server가 Client로 돌려주는 정보 | [FastAPI Request](./06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md), [FastAPI Response](./06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) |
| return annotation vs response_model | Python 함수의 반환 의도 표기와 FastAPI가 실제 HTTP 출력에 적용하는 검증·변환 설정 | [FastAPI Response](./06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) |
| MariaDB vs SQLite | Server 방식의 DBMS와 파일 내장 방식의 경량 DBMS | [SQL 기초](./05_SQL/01_SQL_기초와_SELECT.md), [Python SQLite](./06_FastAPI/06_Python_SQLite와_Transaction.md) |

---

## 10. 색인 유지 규칙

- 새 수업 문서가 완성되면 새 Keyword와 기존 Keyword의 관련 위치를 함께 검토한다.
- 핵심 문서는 용어가 가장 많이 등장한 파일이 아니라 가장 정확하고 자세히 설명하는 파일로 정한다.
- 영어·한글·약어를 함께 기록한다. 예: `Dependency Injection · 의존성 주입 · DI`.
- 단순 함수·메서드 이름은 과목별 `99_` 치트시트에 두고, 여러 문서를 연결하는 개념만 통합 색인에 올린다.
- 문서 이름이 변경되면 이 색인의 상대 링크도 함께 수정한다.
- 아직 수업하지 않은 내용을 완료된 강의 내용처럼 추가하지 않는다.
- 실제 Secret, API Key, Password, Webhook URL은 Keyword 설명에도 기록하지 않는다.

---

## 11. 다음에 추가할 수 있는 Keyword

FastAPI의 `03_database` 수업이 완료되면 다음 용어를 원본과 대조해 추가한다.

```text
ORM · Entity · Repository · Session
Database URL · Connection Pool
Migration · Relationship
N+1 Query · Lazy/Eager Loading
```

> 용어를 외우는 것이 목적이 아니다. 용어를 발견했을 때 **정의 → 동작 → 실제 사용 문서 → 함께 쓰이는 개념**으로 이동할 수 있게 만드는 것이 이 색인의 목적이다.
