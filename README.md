# HumanClass Workspace

수업 원본 코드와, 다시 이해하고 사용할 수 있도록 정리한 Developer-Wiki를 함께 관리하는 학습 workspace다.

## 구성과 역할

| 경로 | 역할 |
| --- | --- |
| [Developer-Wiki](Developer-Wiki/README.md) | 개념·실제 처리·원본 비교·오류·실습·정답을 연결하는 개인 강의 백과사전 |
| [workspace_html](workspace_html/) | HTML·CSS·JavaScript 수업 원본 |
| [workspace_python](workspace_python/) | Python·FastAPI·DB 연동·파일·쿠키·세션 수업 원본 |
| [workspace_sql](workspace_sql/) | MariaDB SQL 수업 원본 |

강사님 최신 자료와 내 원본의 실제 차이는 Wiki에서 해당 함수·용어 설명에 필요한 조각으로 비교한다. 이 안내는 원본 코드나 실행 환경을 새로 작성했다는 뜻이 아니다.

## 공부할 문서 찾기

| 영역 | 학습·참고 MD | 안내·검토·README 포함 MD | 바로가기 |
| --- | ---: | ---: | --- |
| 메모리와 참조 | 1 | 2 | [시작하기](Developer-Wiki/00_%EB%A9%94%EB%AA%A8%EB%A6%AC%EC%99%80_%EC%B0%B8%EC%A1%B0%28Stack_Heap%29/README.md) |
| HTML | 10 | 13 | [시작하기](Developer-Wiki/01_HTML/README.md) |
| CSS | 17 | 20 | [시작하기](Developer-Wiki/02_CSS/README.md) |
| JavaScript | 25 | 28 | [시작하기](Developer-Wiki/03_JavaScript/README.md) |
| Python | 24 | 27 | [시작하기](Developer-Wiki/04_Python/README.md) |
| SQL · MariaDB | 20 | 23 | [시작하기](Developer-Wiki/05_SQL/README.md) |
| FastAPI | 9 | 12 | [시작하기](Developer-Wiki/06_FastAPI/README.md) |
| **파트 합계** | **106** | **125** | |

Developer-Wiki 전체는 상위 README·통합 색인·전체 검토기록까지 **128개 MD**, 이 README를 포함한 문서 적용본은 **129개 MD**다. 집계 기준은 [Developer-Wiki README](Developer-Wiki/README.md)에 명시했다.

[통합 용어색인](Developer-Wiki/99_Developer-Wiki_통합_용어색인.md)에서 Framework·Request·정규표현식·Transaction·Session·UploadFile처럼 기억나는 이름으로 찾는다.

## 작성·보류 범위

00_메모리와_참조부터 06_FastAPI까지 승인된 리팩토링을 통합했다. FastAPI 문서는 `02_todos`, `03_database`, `04_fileupload`, `05_cookie_session`까지 작성했다. 개인 실험 `00_CSS`는 제외하고 `06_scikit_learn`은 GitHub pull과 추가 자료 전달 전까지 보류한다.

## 실행 환경을 구분하기

### HTML·CSS·JavaScript

Browser·Live Server로 정적 HTML을 열고 Elements·Console·Network를 확인한다. 여러 폴더를 workspace로 연 경우 서버 루트와 열린 HTML 위치를 함께 확인한다. 폴더를 옮기는 것만으로 Python 서버가 실행되는 것은 아니다.

### Python·FastAPI

일반 Python 파일 실행과 Uvicorn 서버 실행은 다르다. 먼저 사용할 Interpreter와 작업 폴더를 확인한다. Jinja는 Live Server가 아니라 Python 서버에서 HTML을 생성한다.

현재 ZIP에서 가상환경 자동 생성 파일이 빠져 있을 수 있다. 다른 PC의 venv를 복사하기보다 별도로 만들고 의존성을 설치한다. 아래는 기본 api.py가 있는 `workspace_python/02_todos`에서 실행하는 새 연습 환경 예시다.

```powershell
cd workspace_python/02_todos
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install fastapi uvicorn jinja2 python-multipart
.\.venv\Scripts\python.exe -m uvicorn api:app --port 8000 --reload
```

기존 환경이 있다면 그 Python을 사용해도 된다. Router·Jinja 예제는 각 api.py가 있는 폴더와 templates 경로에 맞춰 실행한다. DB 수업은 sqlmodel·pymysql, Session 수업은 itsdangerous, 해시 수업은 Argon2 backend 등 추가 의존성을 확인한다. 첨부 requirements의 누락과 검증 버전은 과목 검토기록에서 구분한다.

PowerShell 활성화는 .\\Scripts\\Activate.ps1, cmd는 Scripts\\activate.bat이다. 활성화 없이 해당 환경의 Python을 직접 실행하면 셸 활성화 문제를 피할 수 있다. --reload는 코드 변경 때 서버를 재시작하는 개발 기능이지 브라우저 자동 새로고침·메모리 데이터 저장 기능이 아니다.

### MariaDB·SQLite

MariaDB는 별도 서버 접속, SQLite는 프로그램 내 DB 파일 연결이다. SQL Driver의 placeholder·DDL·transaction·close 규칙을 동일하게 일반화하지 않는다. 변경 예제는 대상 DB·WHERE·transaction 경계를 확인하고 별도 연습 데이터에서 실행한다.

## 수업에서 Wiki까지

수업 원본 작성 → 실제 입력·출력 확인 → 강사님 코드와 부분 비교 → 오류·개선 구분 → 정의·이유·처리 순서·결과 설명 → 실습·정답 보강 → README·색인 갱신 → 검토 → Git commit.

원본을 이미 아는 사람이 빠르게 훑는 요약만 만들지 않는다. 이해를 위한 반복·예제·문제는 유지하고 과도한 분할이나 반복 제목 같은 탐색 비용을 줄인다.

## 이번 압축의 적용 방법

압축 루트의 README.md는 workspace 최상단에, Developer-Wiki는 같은 이름의 폴더에 적용한다. 기존 파트 분류와 파일명을 유지했고 색인의 설명 위치 링크를 위해 본문에 명시 anchor를 추가했다. 따라서 상위 README·색인만 골라 적용하지 말고 통합 Developer-Wiki도 함께 적용한다.

**문서 적용본이며 원본 코드·venv·DB·업로드 파일은 포함하지 않는다.** workspace_html·workspace_python·workspace_sql은 기존 폴더를 유지한다. 적용 전 문서 백업을 권장한다. 오래된 분할판이 남아 있다면 메모리의 통합 학습 파일과 README가 현재 읽을 기준이다. 이번 압축은 사용자 폴더의 오래된 파일을 자동 삭제하지 않는다.

## 저장소 관리와 주의

비밀 값·.env·가상환경·cache·로컬 실행 데이터는 공개 저장소에 올리지 않는다. 기존 수업 원본에 하드코딩된 DB 계정 정보와 Session 비밀 키는 별도 환경 설정으로 정리할 필요가 있다. 이번 작업은 Wiki 통합이며 원본 코드를 자동 변경하지 않았다.

새 수업 자료가 완성되면 실제 원본을 전달받아 범위를 확인한 뒤 추가한다. 작성하지 않은 과목·기능을 완료로 표시하지 않는다. 최종 변경 내역과 검증 한계는 [전체 검토기록](Developer-Wiki/98_Developer-Wiki_전체_검토기록.md)을 확인한다.

