# 📚 HumanClass Workspace

> **Learn • Compare • Improve • Archive**
>
> AI · Software Engineering 과정을 학습하며 작성한 **실습 코드와 Developer-Wiki를 함께 관리하는 학습 저장소**입니다.  
> 코드를 직접 작성하고, 비교하고, 개선한 뒤 다시 활용할 수 있는 문서로 축적하는 것을 목표로 합니다.

---

## ✨ About

`workspace`는 수업에서 작성하는 원본 실습 코드와 이를 정리한 Developer-Wiki를 한 Repository에서 관리합니다.

| 영역 | 역할 |
|---|---|
| 💻 Practice | HTML · CSS · JavaScript · Python · SQL 실습 코드 작성 |
| 📚 Documentation | 학습 내용을 Markdown 기반 Developer-Wiki로 정리 |
| 🔍 Compare | 내 코드와 강사 코드의 실제 차이 비교 |
| 🚀 Improve | 오류 분석, Refactoring, 실무 작성 방식 보완 |
| 📝 Archive | 학습 과정과 문제 해결 기록을 지속적으로 축적 |

---

## 📊 Current Progress

### Developer-Wiki

| Subject | Documents | Status | Documentation |
|:---|---:|:---:|:---:|
| 📄 HTML | 10 | ✅ Complete | [Open](./Developer-Wiki/01_HTML/README.md) |
| 🎨 CSS | 17 | ✅ Complete | [Open](./Developer-Wiki/02_CSS/README.md) |
| ⚡ JavaScript | 25 | ✅ Complete | [Open](./Developer-Wiki/03_JavaScript/README.md) |
| 🐍 Python | 24 | ✅ Complete | [Open](./Developer-Wiki/04_Python/README.md) |
| **Total** | **76** | **Complete** | [Developer-Wiki](./Developer-Wiki/README.md) |

> 문서 수는 각 Subject 폴더의 `README.md`를 제외한 실제 학습 Markdown 파일을 기준으로 계산했습니다.

---

## 🗺️ Learning Roadmap

```text
Frontend Foundation
HTML
  ↓
CSS
  ↓
JavaScript
  │
  ├──────────────┐
  ↓              ↓
Python        Database
                 ↓
                Java
                 ↓
            JSP / Servlet
                 ↓
       Spring / Spring Boot
                 ↓
               React
                 ↓
             AI Agent
                 ↓
           Team Project
                 ↓
             Portfolio
```

| ✅ Completed Wiki | 🧪 Practice | 🚧 Next | 🌱 Future |
|---|---|---|---|
| HTML | Frontend | Java | Spring Framework |
| CSS | Python | Database | Spring Boot |
| JavaScript | SQL | JSP / Servlet | React |
| Python |  |  | AI Agent |
|  |  |  | Team Project |
|  |  |  | Portfolio |

---

## 📖 Developer-Wiki

> 수업 코드를 그대로 보관하는 공간과, 학습 내용을 다시 읽을 수 있도록 정리하는 공간을 분리합니다.

[📚 Developer-Wiki Home](./Developer-Wiki/README.md)

| Order | Subject | 핵심 학습 | Link |
|:---:|---|---|:---:|
| 01 | 📄 HTML | Document Structure · Semantic HTML · Form · Accessibility | [Open](./Developer-Wiki/01_HTML/README.md) |
| 02 | 🎨 CSS | Selector · Box Model · Layout · Responsive · Animation | [Open](./Developer-Wiki/02_CSS/README.md) |
| 03 | ⚡ JavaScript | Variable · Function · DOM · Event · Async · API | [Open](./Developer-Wiki/03_JavaScript/README.md) |
| 04 | 🐍 Python | Data Type · Collection · Control Flow · Function · OOP | [Open](./Developer-Wiki/04_Python/README.md) |

각 Subject는 공통적으로 다음 흐름을 사용합니다.

```text
기초 개념
    ↓
예제와 실습
    ↓
코드 비교
    ↓
오류와 개선
    ↓
실무 코딩 스타일
    ↓
종합실습
```

---

## 💻 Practice Workspaces

### 🌐 Frontend Workspace

[Open `workspace_html`](./workspace_html/)

HTML 수업을 시작점으로 CSS와 JavaScript 실습까지 함께 관리하는 Frontend 작업 공간입니다.

```text
workspace_html/
├── HTML 실습
├── css/
├── javascript/
├── asset/
└── 과제 및 평가/
```

주요 학습 영역:

- HTML Document와 Tag
- Link · List · Table · Form
- CSS Selector · Box Model · Layout
- Responsive Web
- JavaScript Variable · Function · DOM · Event
- AJAX · Fetch API · 외부 API 연동

---

### 🐍 Python Workspace

[Open `workspace_python`](./workspace_python/)

Python 문법 실습, Quiz, Exam, File 처리, Function과 Class 관련 코드를 관리합니다.

```text
workspace_python/
├── 01_hello.py
├── 02_var.py
├── ...
├── quiz/
├── exam/
├── fn/
└── 실습 및 평가 자료
```

주요 학습 영역:

- Variable과 Data Type
- String과 Collection
- Condition과 Loop
- File I/O
- Function
- Class와 Object
- Exception
- Module
- Quiz와 평가 문제

> Python 실행 과정에서 생성되는 Cache, Virtual Environment 내부 파일 등은 학습 코드와 구분해서 관리합니다.

---

### 🗄️ SQL Workspace

[Open `workspace_sql`](./workspace_sql/)

Database 수업에서 사용하는 SQL Script와 실습 Query를 관리하는 공간입니다.

주요 학습 방향:

- SQL Script 작성
- Table과 Data 조회
- MariaDB 기반 실습
- Database 학습 내용 확장

SQL 학습이 본격화되면 Developer-Wiki의 다음 Subject로 연결할 수 있습니다.

---

## 📂 Repository Structure

```text
workspace/
├── README.md
├── .gitignore
│
├── Developer-Wiki/
│   ├── README.md
│   ├── 00_자료구조_정리(Stack_Heap)/
│   ├── 01_HTML/
│   ├── 02_CSS/
│   ├── 03_JavaScript/
│   └── 04_Python/
│
├── workspace_html/
│   ├── css/
│   ├── javascript/
│   ├── asset/
│   └── ...
│
├── workspace_python/
│   ├── quiz/
│   ├── exam/
│   ├── fn/
│   └── ...
│
├── workspace_sql/
│   └── SQL 실습 자료
│
└── BACKUP/
    └── Local Backup
```

> `BACKUP/`은 `.gitignore`에 등록된 Local Backup 영역으로, GitHub 학습 콘텐츠와 분리해서 관리합니다.

---

## 🔄 Workspace Workflow

```text
수업 진행
    ↓
workspace_* 에서 직접 실습
    ↓
실행 결과와 오류 확인
    ↓
내 코드와 강사 코드 비교
    ↓
Developer-Wiki 문서화
    ↓
실무 관점 보완 및 Refactoring
    ↓
README Navigation 갱신
    ↓
Git Commit
```

실습 코드와 Wiki를 분리함으로써 **원본 학습 흔적은 유지하면서 문서는 더 정확하고 읽기 좋은 형태로 개선**할 수 있습니다.

---

## ⭐ Documentation Principles

Developer-Wiki는 다음 기준을 유지합니다.

- ✅ 실제 수업·실습 코드 기반
- ✅ 내 코드와 강사 코드 비교
- ✅ 존재하지 않는 차이는 임의로 만들지 않음
- ✅ 원본 오류와 개선 방향을 구분
- ✅ 실행 결과뿐 아니라 동작 원리 설명
- ✅ 대표 오류와 Debugging 과정 정리
- ✅ 실무 작성 방식과 Refactoring 보완
- ✅ Subject별 실무 코딩 스타일 제공
- ✅ Subject별 종합실습 제공
- ✅ GitHub 상대 경로 Navigation 사용
- ✅ README와 상세 문서의 구조를 지속적으로 통일

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Frontend | HTML5 · CSS3 · JavaScript |
| Programming | Python |
| Database | SQL · MariaDB |
| Documentation | Markdown |
| Editor | Visual Studio Code |
| Version Control | Git · GitHub |

---

## 🗃️ Repository Policy

### Git으로 관리하는 것

- 수업 실습 Source Code
- Developer-Wiki Markdown 문서
- README
- 학습에 필요한 Text·SQL·Asset
- Project 설정 중 Repository에 필요한 파일

### Git에서 제외하는 것

`.gitignore` 기준으로 다음 자료는 Repository와 분리합니다.

- `BACKUP/`
- 제출용 PDF·PNG·ZIP 일부
- Python Cache
- 임시 Test·평가 파일 일부
- 불필요한 생성 파일

Binary File이나 자동 생성 파일은 학습 기록에 반드시 필요한 경우가 아니라면 Source와 분리해서 관리합니다.

---

## 🧭 Quick Navigation

| Area | Description | Link |
|---|---|:---:|
| 📚 Developer-Wiki | 정리된 학습 문서 | [Open](./Developer-Wiki/README.md) |
| 🌐 Frontend Practice | HTML · CSS · JavaScript 실습 | [Open](./workspace_html/) |
| 🐍 Python Practice | Python 실습 · Quiz · Exam | [Open](./workspace_python/) |
| 🗄️ SQL Practice | Database · SQL 실습 | [Open](./workspace_sql/) |

---

## 🚀 Future Roadmap

- [x] HTML Wiki
- [x] CSS Wiki
- [x] JavaScript Wiki
- [x] Python Wiki
- [ ] Java
- [ ] Database Developer-Wiki
- [ ] JSP / Servlet
- [ ] Spring Framework
- [ ] Spring Boot
- [ ] React
- [ ] AI Agent
- [ ] Team Project
- [ ] Portfolio

---

## 📌 Repository Goal

이 Repository의 목표는 많은 파일을 저장하는 것이 아닙니다.

```text
Learn
  ↓
Practice
  ↓
Compare
  ↓
Debug
  ↓
Improve
  ↓
Document
  ↓
Reuse
```

수업에서 작성한 코드를 **왜 그렇게 동작하는지 설명할 수 있는 지식으로 바꾸고**, 해결한 문제와 개선 과정을 이후 Project에서도 다시 사용할 수 있도록 축적합니다.

---

## 📚 HumanClass

> **Learn • Compare • Improve • Archive**

**Keep Learning. Keep Building. Keep Improving.**
