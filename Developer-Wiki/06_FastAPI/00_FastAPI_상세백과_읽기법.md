# FastAPI 상세백과 읽기법

## 문서의 역할

이 문서는 강의의 반복 설명·예제·종합실습을 줄이지 않는 상세백과다. 앞부분의 '개념에서 실제 실행까지'는 입력부터 결과까지 따라가는 보강 설명이고 기존 번호형 본문은 개별 개념을 다시 찾는 기준이다. 핵심만 빨리 찾는 독자는 목차와 체크리스트를, 처음 복습하는 독자는 보강→본문→실습→답안 순서를 이용한다.

## 실습을 준비하는 순서

1. 수업 코드가 있는 폴더와 가상환경을 별도로 확인한다.
2. 실행하는 Python의 경로와 패키지 설치 목록을 확인한다.
3. 기본·Router·Jinja 등 서로 다른 api.py를 같은 모듈로 착각하지 않는다.
4. 해당 폴더에서 Uvicorn을 실행한다. Jinja templates와 업로드 uploads의 상대 경로를 확인한다.
5. 요청 URL·method·Header·Body와 응답 status·Header·Body를 각각 기록한다.
6. 터미널 print·서버 저장소·화면 결과를 함께 대조한다.
7. DB 변경은 전용 테스트 데이터에서 진행한다. 실제 수업 DB를 자동 변경하지 않는다.

PowerShell 활성화는 .\\Scripts\\Activate.ps1, cmd는 Scripts\\activate.bat 형태다. 활성화하지 않고 해당 환경 Scripts/python.exe를 직접 실행해도 된다. 기존 예제 중 powershell로 표시한 Scripts\\activate 명령은 수업 cmd 입력을 기록한 부분이므로 현재 셸에 맞게 선택한다.

## 입력 위치별 찾기

| 질문 | 문서 |
| --- | --- |
| 가상환경·포트·Framework와 Library | 01 |
| Request·Form·JSON·Path·Query·CORS | 02 |
| HTML이 언제 만들어지는가 | 03 |
| 응답 검증·Redirect·Depends | 04 |
| Form과 Todo 상태 변화·PRG | 05 |
| sqlite3·바인딩·commit·rollback | 06 |
| MariaDB·Engine·Session·사원 CRUD·해시 | 07 |
| multipart·UploadFile·파일 경로·FileResponse | 08 |
| Cookie·서명 Session·Middleware·StaticFiles | 09 |

## 실습 중 결과를 해석하기

코드 조각은 원본의 해당 개념만 발췌한 것이므로 imports·app·저장소가 생략될 수 있다. '독립 예제'라고 표기한 코드를 별도 파일에 저장하고 실행한다. 원본 코드·개선 계약·설명용 샘플·실제 검증 출력은 구분한다. UUID·임시 포트·객체 주소는 매번 달라질 수 있다.

ASGI 테스트 클라이언트는 응답·상태·렌더링 HTML을 검사하지만 실제 브라우저의 CORS 차단·쿠키 전송 정책·DOM 표시를 그대로 구현하지 않는다. 그 부분은 Network·Console·쿠키 저장소로 직접 확인한다.

## 빠른 실패 분류

404는 경로/대상 없음, 405는 method 불일치, 422는 선언된 입력 규칙 실패, 500은 서버 구현/응답 검증/외부 자원 실패일 수 있다. '브라우저에서 안 된다'만으로 원인을 단정하지 않는다. 파일 저장이나 DB execute 성공과 HTTP 성공 응답은 다른 사건이다.

## 보강 표시와 보류

💡는 수업 원본에 없거나 실무 안전성을 위해 덧붙인 설명이다. 보안 예제도 완성된 운영 시스템이라고 단정하지 않는다. 06_scikit_learn은 이번 산출물에 포함하지 않았으며 missing CSV·강사님 코드 비교를 임의로 채우지 않는다.

