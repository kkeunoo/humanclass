# 📚 Developer-Wiki

> **나만의 수업 강의 백과사전 — Learn • Understand • Trace • Compare • Reuse**

수업에서 작성한 내 코드와 강사님 코드를 근거로, 시간이 지나 내용을 잊어도 개념을 다시 이해하고 직접 작성할 수 있도록 정리한 개발 학습 Wiki입니다.

단순히 “이 문법은 이렇게 쓴다”에서 끝나지 않습니다. 값과 정보가 어디에서 들어오고, 내부에서 어떤 순서로 처리되며, 화면·터미널·데이터베이스에는 어떤 결과가 나타나는지 추적합니다.

---

## 📊 현재 문서 현황

문서 수는 각 폴더의 `README.md`를 제외하고, V3 공통 읽기법과 `99_` 참고 문서를 포함한 실제 Markdown 파일 기준입니다.

| 순서 | 영역 | 문서 | 상태 | 시작하기 |
|:---:|---|---:|:---:|:---:|
| 00 | 🧠 메모리와 참조 | 1 | ✅ Complete | [Open](./00_메모리와_참조%28Stack_Heap%29/01_메모리와_참조%28Stack_Heap%29.md) |
| 01 | 📄 HTML | 11 | ✅ V3 | [Open](./01_HTML/README.md) |
| 02 | 🎨 CSS | 18 | ✅ V3 | [Open](./02_CSS/README.md) |
| 03 | ⚡ JavaScript | 26 | ✅ V3 | [Open](./03_JavaScript/README.md) |
| 04 | 🐍 Python | 24 | ✅ V3 | [Open](./04_Python/README.md) |
| 05 | 🗄️ SQL · MariaDB | 20 | ✅ V3 | [Open](./05_SQL/README.md) |
| 06 | 🚀 FastAPI | 6 | 🔄 수업 범위 확장 중 | [Open](./06_FastAPI/README.md) |
| **합계** | **7개 영역** | **106** |  |  |

> FastAPI는 현재 완료된 `01~06` 문서만 포함합니다. 학습 중인 `workspace_python/03_database`는 수업이 끝난 뒤 원본을 다시 검토하여 추가합니다.

---

## 🧭 권장 학습 순서

```text
HTML: 문서 구조와 데이터 입력
  ↓
CSS: 선택자와 화면 배치·렌더링
  ↓
JavaScript: 상태·DOM·이벤트·비동기 통신
  ↓
Python: 자료형·제어문·함수·객체·파일
  ↓
SQL / MariaDB: 데이터 조회·변경·설계·트랜잭션
  ↓
FastAPI: HTTP 요청·응답·템플릿·CRUD·SQLite
  ↓
Database 연동과 이후 Backend 수업으로 확장
```

`00_메모리와_참조(Stack_Heap)`는 변수, 객체, 배열·리스트, 함수, 클래스의 참조 관계가 헷갈릴 때 과목 순서와 관계없이 다시 확인합니다.

---

## 🔎 V3 개인 강의 백과사전 원칙

각 문서는 가능한 범위에서 다음 질문에 답합니다.

1. 이것은 무엇인가?
2. 왜 배우며 어떤 문제를 해결하는가?
3. 값이나 요청은 어디에서 들어오는가?
4. 언어·브라우저·서버·DB는 어떻게 받아들이는가?
5. 실제 내부 처리와 실행 순서는 무엇인가?
6. 실행 전후의 값, 자료형, 객체, DOM, 데이터는 어떻게 달라지는가?
7. Console·화면·Terminal·Network·DB에는 무엇이 나타나는가?
8. 실패하면 어떤 오류, 예외, HTTP 상태가 발생하는가?
9. 내 코드와 강사님 코드의 어디에서 사용했는가?
10. 시간이 지난 뒤 직접 다시 작성할 수 있는가?

---

## 🧱 공통 문서 구조

```text
문서 정보와 원본 출처
→ 학습 목표와 학습 이유
→ 번호형 핵심 개념
→ 값의 출처와 내부 동작
→ 내 코드 / 강사님 코드 비교
→ 수정 사항과 확장 설명
→ 개선된 통합 예제
→ 실제 실행 결과와 활용 방법
→ 흔한 실수와 디버깅
→ 종합 실습
→ 정답과 해설
→ 최종 체크리스트
→ 핵심 요약과 V3 추적 카드
```

과목별 실행 환경이 다르므로 확인 도구도 구분합니다.

| 영역 | 실행 결과를 확인하는 곳 |
|---|---|
| HTML | Elements, Network, Accessibility Tree |
| CSS | Styles, Computed, Box Model, Layout |
| JavaScript | Console, Elements, Network, Event 흐름 |
| Python | Terminal, `print()`, 반환값, Traceback |
| SQL | MariaDB 결과 집합, 영향받은 행, 실행 계획, Transaction 상태 |
| FastAPI | Browser, Swagger UI, Terminal, HTTP 상태, Response, DB |

---

## 📚 과목별 핵심 문서

| 과목 | 실무 정리 | 종합 실습 | 참고 문서 |
|---|---|---|---|
| HTML | [09 실무 코딩 스타일](./01_HTML/09_HTML_실무_코딩스타일.md) | [10 종합실습](./01_HTML/10_HTML_종합실습.md) | [V3 읽기법](./01_HTML/00_HTML_V3_동작_백과_읽기법.md) |
| CSS | [16 실무 코딩 스타일](./02_CSS/16_CSS_실무_코딩스타일.md) | [17 종합실습](./02_CSS/17_CSS_종합실습.md) | [V3 읽기법](./02_CSS/00_CSS_V3_동작_백과_읽기법.md) |
| JavaScript | [23 실무 코딩 스타일](./03_JavaScript/23_JavaScript_실무_코딩스타일.md) | [24 종합실습](./03_JavaScript/24_JavaScript_종합실습.md) | [메서드 치트시트](./03_JavaScript/99_JavaScript_자료형별_메서드_치트시트.md) |
| Python | [19 실무 코딩 스타일](./04_Python/19_Python_실무_코딩스타일.md) | [20 종합실습](./04_Python/20_Python_종합실습.md) | [메서드 치트시트](./04_Python/99_Python_자료형별_메서드_치트시트.md) |
| SQL | [19 실무 코딩 스타일](./05_SQL/19_SQL_실무_코딩스타일.md) | [20 종합실습](./05_SQL/20_SQL_종합실습.md) | 각 번호형 문서의 체크리스트 |
| FastAPI | [README 학습 흐름](./06_FastAPI/README.md) | Todo CRUD·SQLite 문서 | Request·Response 실행 추적 |

---

## 📂 Wiki 구조

```text
Developer-Wiki/
├── README.md
├── 00_메모리와_참조(Stack_Heap)/
├── 01_HTML/
├── 02_CSS/
├── 03_JavaScript/
├── 04_Python/
├── 05_SQL/
└── 06_FastAPI/
```

---

## 📌 관리 정책

- 수업 원본과 Wiki 설명을 구분하고 실제 파일명을 기준으로 연결합니다.
- 내 코드와 강사님 코드에 없는 내용은 `Wiki 확장 학습`으로 표시합니다.
- 원본의 오류·오탈자와 개선 코드를 섞지 않고 각각 설명합니다.
- API Key, Password, Webhook URL 같은 비밀값은 문서에 기록하지 않습니다.
- 내부 링크는 GitHub에서 동작하는 상대 경로를 사용합니다.
- 문서 추가·삭제 시 과목 README와 이 README의 문서 수를 함께 갱신합니다.
- `venv`, `Lib/site-packages`, `__pycache__`, DB 임시 파일은 학습 원본과 구분하며 자동 생성물은 Wiki에 복사하지 않습니다.

---

## 🔄 복습 방법

```text
README에서 학습 위치 확인
→ V3 읽기법으로 실행 환경 확인
→ 본문을 읽기 전에 결과를 먼저 예측
→ 내 코드 직접 실행
→ 강사님 코드와 차이 비교
→ Console/Terminal/Network/DB 결과 기록
→ 예제의 이름과 입력값을 바꾸어 재작성
→ 체크리스트와 종합실습으로 확인
```

> 배웠던 내용을 “본 적 있다”에서 끝내지 않고, 다시 설명하고 실행하고 수정할 수 있는 지식으로 남깁니다.
