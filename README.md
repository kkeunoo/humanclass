# HumanClass Workspace

수업에서 직접 작성한 코드를 보존하고, 강사님 코드와 비교해 다시 공부할 수 있도록 정리한 [Developer-Wiki](Developer-Wiki/README.md)를 함께 관리한다. 처음 읽을 때는 과목 README의 순서를 따르고, 기억나는 단어가 있다면 [통합 용어색인](Developer-Wiki/99_Developer-Wiki_통합_용어색인.md)에서 찾는다.

## 폴더와 학습 순서

| 순서 | Wiki | 수업 원본에서 주로 살펴볼 것 |
| --- | --- | --- |
| 00 | [메모리와 참조](Developer-Wiki/00_%EB%A9%94%EB%AA%A8%EB%A6%AC%EC%99%80_%EC%B0%B8%EC%A1%B0%28Stack_Heap%29/README.md) | 변수·리스트를 읽을 때 참조와 변경 확인 |
| 01 | [HTML](Developer-Wiki/01_HTML/README.md) | `workspace_html`의 문서·폼 |
| 02 | [CSS](Developer-Wiki/02_CSS/README.md) | `workspace_html`의 선택자·배치 |
| 03 | [JavaScript](Developer-Wiki/03_JavaScript/README.md) | `workspace_html`의 DOM·이벤트·요청 |
| 04 | [Python](Developer-Wiki/04_Python/README.md) | `workspace_python`의 자료형·함수·객체·파일 |
| 05 | [SQL·MariaDB](Developer-Wiki/05_SQL/README.md) | `workspace_sql`의 조회·변경·재귀 CTE |
| 06 | [FastAPI](Developer-Wiki/06_FastAPI/README.md) | `workspace_python`의 라우터·DB·파일·세션 |
| 07 | [데이터 분석·기초 머신러닝](Developer-Wiki/07_데이터분석과_머신러닝/README.md) | `06_scikit_learn`의 와인 CSV 분류 |
| 08 | [Elasticsearch·RAG](Developer-Wiki/08_Elasticsearch와_RAG/README.md) | `07_elastic`의 색인·검색·임베딩·질문응답 |
| 09 | [영화 CSV·청크·임베딩](Developer-Wiki/09_영화CSV_청크와_임베딩/README.md) | `08_langgraph`의 **현재 구현된** CSV 가공과 임베딩 준비 |

00은 Python에서 같은 객체의 변경이 헷갈릴 때 펼치는 연결 자료다. 01부터 순서대로 읽어도 된다. 09의 폴더 이름은 `08_langgraph`지만 현재 양쪽 코드에 LangGraph 그래프 실행은 없다. 제목보다 실제 코드를 기준으로 범위를 정했다.

## Wiki의 코드와 설명을 읽는 법

본문은 강사님 원본 발췌를 먼저, 내 원본 발췌를 아래에 놓는다. 실제 실행 코드와 주석이 다르면 실행 코드를 기준으로 설명한다. **추가로 알면 좋은 것**은 현재 확인된 수업 본문 밖의 보충이고, **이후 첨부**는 아직 원본이나 학습 범위를 확인할 자료가 부족한 항목이다. 이전 실습의 오류와 `pass` 상태도 감추지 않고 [편집·검증 기록](Developer-Wiki/편집기록/README.md)에 범위를 적었다.

`workspace_html`, `workspace_python`, `workspace_sql`은 기존 수업 원본이다. Wiki를 적용할 때 이 세 폴더나 그 안의 프로젝트 폴더를 통째로 바꾸지 않는다. 가상환경이 자동으로 만든 `Lib/site-packages`, `Scripts`, `share`, `__pycache__`, `.pyc`, `.env`, `*.cfg`는 학습 코드나 공개 문서의 근거로 사용하지 않았다.

## 실행 환경

HTML·CSS·JavaScript는 브라우저에서 열고 Elements·Console·Network로 확인한다. Python 파일 직접 실행과 FastAPI 서버 실행은 다르므로 프로젝트 폴더와 인터프리터를 먼저 확인한다. 예를 들어 `workspace_python/02_todos`의 새 연습 환경은 다음처럼 실행할 수 있다.

```powershell
cd workspace_python/02_todos
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install fastapi uvicorn jinja2 python-multipart
.\.venv\Scripts\python.exe -m uvicorn api:app --port 8000 --reload
```

DB, 업로드, 세션, Elasticsearch, 외부 임베딩 API를 쓰는 과제는 각각 다른 의존성·서버·설정이 필요하다. Wiki는 원본 코드의 설명과 정적 대조를 제공하며 모든 외부 서비스의 현재 실행 성공을 보증하지 않는다. 비밀 값이나 `.env`는 GitHub에 올리지 않는다.

## 문서 적용과 기록

이 README와 `Developer-Wiki` 폴더는 **같은 시점의 한 묶음**으로 적용한다. 과목 ZIP은 각 단원의 중간 산출물이고, [Developer-Wiki 첫 화면](Developer-Wiki/README.md)과 색인은 통합본을 기준으로 한다. 수업 원본·가상환경·DB 데이터는 문서 적용 대상이 아니다. 전체 검토 내용은 [통합 검증 기록](Developer-Wiki/편집기록/98_Developer-Wiki_전체_검토기록.md)에 남겼다.
