# 📚 HumanClass Workspace

> **수업 원본 코드와 나만의 개발 강의 백과사전을 함께 관리하는 학습 Repository**

이 workspace는 HTML·CSS·JavaScript·Python·SQL·FastAPI 수업에서 직접 작성한 코드와 강사님 코드 비교 결과를 보존하고, 이를 다시 사용할 수 있는 Developer-Wiki로 발전시키기 위한 공간입니다.

---

## 🗂️ 구성과 역할

| 경로 | 역할 |
|---|---|
| [`Developer-Wiki/`](./Developer-Wiki/README.md) | 개념, 동작 과정, 코드 비교, 오류, 실습을 정리한 V3 개인 강의 백과사전 |
| [`workspace_html/`](./workspace_html/) | HTML, CSS, JavaScript 수업·과제 원본 |
| [`workspace_python/`](./workspace_python/) | Python, FastAPI, SQLite 수업·실습 원본 |
| [`workspace_sql/`](./workspace_sql/) | MariaDB SQL 수업 원본 |
| `BACKUP/` | 로컬 백업 자료이며 일반 학습 탐색 대상과 분리 |

---

## 📊 Developer-Wiki 현황

| 영역 | 문서 | 상태 | 바로가기 |
|---|---:|:---:|:---:|
| 메모리와 참조 | 1 | ✅ Complete | [Open](./Developer-Wiki/00_메모리와_참조%28Stack_Heap%29/01_메모리와_참조%28Stack_Heap%29.md) |
| HTML | 11 | ✅ V3 | [Open](./Developer-Wiki/01_HTML/README.md) |
| CSS | 18 | ✅ V3 | [Open](./Developer-Wiki/02_CSS/README.md) |
| JavaScript | 26 | ✅ V3 | [Open](./Developer-Wiki/03_JavaScript/README.md) |
| Python | 24 | ✅ V3 | [Open](./Developer-Wiki/04_Python/README.md) |
| SQL · MariaDB | 20 | ✅ V3 | [Open](./Developer-Wiki/05_SQL/README.md) |
| FastAPI · SQLite | 6 | 🔄 수업 범위 확장 중 | [Open](./Developer-Wiki/06_FastAPI/README.md) |
| 통합 용어 색인 | 1 | ✅ Reference | [Open](./Developer-Wiki/99_Developer-Wiki_통합_용어색인.md) |
| **합계** | **107** |  | [Developer-Wiki Home](./Developer-Wiki/README.md) |

문서 수는 과목별 README를 제외하고 V3 읽기법·참고 문서·통합 용어 색인을 포함한 Markdown 기준입니다.

---

## 🗺️ 전체 학습 로드맵

```text
HTML 문서 구조
→ CSS 화면 표현과 레이아웃
→ JavaScript DOM·이벤트·비동기 통신
→ Python 프로그래밍 기초와 객체
→ MariaDB SQL과 Transaction
→ FastAPI HTTP·Template·CRUD·SQLite
→ Database 연동
→ 이후 Java / JSP·Servlet / Spring / React
→ Team Project와 Portfolio
```

---

## 🔄 수업에서 Wiki까지의 작업 흐름

```text
수업 진행
→ workspace_*에서 내 코드 작성
→ 실행 결과와 오류 확인
→ 강사님 코드와 실제 차이 비교
→ 잘못된 메모와 코드를 원본/개선으로 구분
→ Developer-Wiki에 동작 과정과 결과 기록
→ 실수·디버깅·종합실습 보강
→ README 문서 수와 링크 갱신
→ Git Commit
```

---

## ▶️ 실행 환경 빠른 안내

### HTML · CSS · JavaScript

`workspace_html`을 포함한 workspace 최상위 폴더를 VS Code에서 열면 전체 과목을 함께 탐색할 수 있습니다. Live Server는 현재 연 HTML 파일 또는 VS Code workspace 설정의 서버 루트를 기준으로 동작합니다.

### Python

일반 Python 번호형 파일은 해당 파일을 직접 실행합니다. 현재 작업 폴더에 따라 상대 파일 경로가 달라질 수 있으므로 파일 입출력 예제에서는 실행 위치도 확인합니다.

### FastAPI

FastAPI 수업은 `workspace_python/02_todos`의 가상환경과 예제 폴더를 사용합니다. 활성화 후 실제 앱 파일과 변수명에 맞춰 Uvicorn을 실행합니다.

```powershell
cd workspace_python\02_todos
Scripts\activate
uvicorn api:app --port 8000 --reload
```

가상환경의 `Lib/site-packages`, `Scripts`, `Include`, `__pycache__`는 설치·실행 과정에서 만들어지는 파일입니다. 직접 작성한 학습 코드는 아니므로 일반적인 Wiki 원본 비교와 Git 관리 대상에서 제외합니다. 재현에 필요한 패키지는 `requirements.txt`로 관리합니다.

### SQL

`workspace_sql` 원본은 MariaDB 기준입니다. DDL·DML과 Transaction 예제는 현재 선택된 Database와 `autocommit`, commit/rollback 상태를 확인한 뒤 실행합니다.

---

## 📂 Repository 구조

```text
workspace/
├── README.md
├── Developer-Wiki/
│   ├── README.md
│   ├── 00_메모리와_참조(Stack_Heap)/
│   ├── 01_HTML/
│   ├── 02_CSS/
│   ├── 03_JavaScript/
│   ├── 04_Python/
│   ├── 05_SQL/
│   ├── 06_FastAPI/
│   └── 99_Developer-Wiki_통합_용어색인.md
├── workspace_html/
├── workspace_python/
├── workspace_sql/
└── BACKUP/
```

---

## 🔐 Repository 관리 원칙

- 수업 원본은 가능한 한 보존하고 수정·보완 내용은 Wiki에서 구분합니다.
- 내 코드와 강사님 코드의 차이는 실제 파일과 실행 결과를 근거로 기록합니다.
- API Key, Database Password, Discord Webhook 등 비밀정보는 Commit하지 않습니다.
- `.env`, 가상환경, cache, 자동 생성 파일, 로컬 DB 임시 파일은 `.gitignore` 정책을 확인합니다.
- README와 Wiki 내부 링크는 GitHub 상대 경로를 사용합니다.
- 수업이 끝나지 않은 영역은 완료로 표시하지 않습니다.
- 새 문서를 추가하면 과목 README, Developer-Wiki README, 최상위 README의 문서 수와 링크를 함께 갱신합니다.

---

## 📚 시작하기

[Developer-Wiki 전체 목차](./Developer-Wiki/README.md)에서 과목을 선택하거나, 처음부터 복습한다면 [HTML Wiki](./Developer-Wiki/01_HTML/README.md)에서 시작합니다.

> **배우고, 실행하고, 비교하고, 이해한 내용을 다시 사용할 수 있는 지식으로 남깁니다.**
