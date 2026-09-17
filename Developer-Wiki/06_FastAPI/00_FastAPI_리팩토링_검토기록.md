# FastAPI 리팩토링 검토기록

## 최종 범위와 보류

기존 01–06 문서와 README를 재구성·보강하고, 사용자 추가 허용에 따라 03_database·04_fileupload·05_cookie_session을 07–09 문서로 정식 작성했다. 00_CSS는 분석·문서화 범위에서 제외했다. 06_scikit_learn은 원본 CSV와 강사님 코드가 확인되지 않아 질문했고, 사용자 요청에 따라 GitHub pull 이후로 보류했다.

## 세부 질문으로 나눈 검토와 결론

| 질문 | 검토 결과·조치 |
| --- | --- |
| 단순 UI 변경인가? | 요청 정보의 출처·변환·처리·실패·저장 상태를 새 설명과 예제로 보강했다. |
| 이해용 내용을 줄였나? | 기존 6개 본문의 코드·출력 338블록과 번호형 주제 109개를 유지했다. 목표만 간략화했다. |
| 초보자가 혼자 실행할 수 있나? | 독립 예제와 부분 조각을 구분하고 경로·환경·전송 위치·예상 출력·확인 절차를 추가했다. |
| 숙련자도 빠르게 찾을 수 있나? | 고유 링크 목차·원본 함수 표·실패 표·최종 체크리스트를 이용한다. |
| 교사 코드를 무조건 정답으로 보나? | 혼합 Todo 저장·선택 파일 None 접근·삭제 count 미초기화 등 교사 코드도 교정했다. |
| 미학습 내용을 원본처럼 썼나? | 실무 안전 보강은 💡 또는 개선 표기로 구분했다. |
| 실제 출력인가? | 실행 검증과 설명용 샘플을 구분하고 UUID·포트 같은 가변값을 고정 결과로 쓰지 않았다. |
| README·용어색인 전부 끝났나? | FastAPI README만 갱신했다. 전체 README·통합 색인·교차 검토는 파트 승인 이후 통합 단계다. |

## 찾아서 수정한 문제

1. Python return annotation 자체가 int 반환을 강제한다는 메모와 FastAPI response_model을 구분했다.
2. 내 todoParam의 non-GET data 미초기화를 원본 재현으로 확인했다. 강사님은 Form 분기가 있다.
3. 양쪽 Todo 목록의 dict/모델 혼합 저장으로 todo.id 접근이 실패하는 사례를 재현했다.
4. 내 Todo는 value1/value2, 교사 Todo는 id/item이므로 이름만 보고 필드를 같다고 해설하지 않았다.
5. if star는 0도 False다. 누락·None·0을 구분하도록 설명했다.
6. Jinja 필터 Environment와 OS 환경변수를 구분하고 Markup이 HTML 정화가 아니라고 설명했다.
7. 내 GET+307 Redirect를 무조건 잘못됐다고 판단하지 않고 교사 POST+303과 비교했다.
8. 직접 함수 호출은 새 요청·새 라우팅이 아니라고 설명했다.
9. 내 Form 빈 문자열 검사만으로 None·공백·누락 검증이 완료되지 않는다고 바로잡았다.
10. sqlite3 with는 연결 close가 아니라 transaction 관리다. 원본 양쪽 주석을 교정했다.
11. MariaDB와 SQLite DDL·transaction 규칙을 동일하게 일반화하지 않았다.
12. text()가 %s보다 무조건 안전·빠르다는 내 메모와 Session=Cursor 비유를 교정했다.
13. 최신 교사 Emp3에는 table=True가 없어 metadata 등록을 과거 문서대로 단정하지 않았다.
14. DB 조회 누락·commit 실패·오류를 catch하고 null 반환하는 경우를 구분했다.
15. 파일2는 print만 하고 저장하지 않는다. 선택 File(None)은 None 검사도 필요하다.
16. UUID와 exists는 경로·권한 검증의 대체가 아니다. 제한 저장·실패 정리 예제를 추가했다.
17. SessionMiddleware는 서버 저장소 Session이 아니라 서명 Cookie 방식이다. 서명과 암호화를 구분했다.
18. key3 max_age=1000의 '10초' 주석, Cookie가 모든 IP/Form 정보를 담는다는 메모를 교정했다.
19. 원본 비밀번호·Session 비밀 키를 신규 문서에 재노출하지 않았다.
20. 수업 /login은 방문만으로 admin을 설정하는 모의 로그인이다. 실제 인증 완료라고 쓰지 않았다.

## 실행 검증

별도 작업 폴더에 패키지를 설치했고 사용자 venv·수업 MariaDB·SQLite DB는 수정하지 않았다.

| 환경 | 검증 버전 |
| --- | --- |
| Python | 3.12.14 |
| FastAPI / Starlette | 0.141.1 / 1.6.0 |
| Pydantic | 2.13.5 |
| Jinja2 | 3.1.6 |
| SQLModel / SQLAlchemy | 0.0.42 / 2.0.54 |
| Uvicorn | 0.53.0 |
| 테스트 클라이언트 | httpx 0.28.1; Starlette가 httpx2 권장을 안내하는 deprecation 경고 있음 |

검증 대상: 기본 Query·HTML·404·405, 통합 Todo CRUD·201·204·404, Request 경로/Query/Header/Cookie 추출, 422, Jinja autoescape·0 조건·줄바꿈, 응답 검증 500, DI 출력, 메모리 Todo 상태, sqlite3 결과 소비·rollback·commit, Argon2 verify, 업로드 바이트·필수 누락·413·중간 파일 정리·다운로드·경로 거부, Cookie Session 로그인·별도 클라이언트·로그아웃, 내·교사 원본 Redirect, 입력 DTO의 빈 문자열 처리, SQLAlchemy mapping·수정·없는 조회, 내·교사 todoParam·dict 혼합 오류.

실행 검증 총 44개 조건을 통과했다. SQLAlchemy helper는 격리 SQLite에서 실행해 로직과 바인딩·mapping을 확인한 것으로 MariaDB 접속 검증이라고 주장하지 않는다. 원본 MariaDB 앱 전체·실제 human 데이터의 CRUD·급여 변경은 실행하지 않았다.

## 검증의 한계

TestClient는 실제 브라우저 CORS 차단·document.cookie·HTML 시각 표시를 구현하지 않는다. HTML 문자열·헤더·응답을 검사한 것과 브라우저를 직접 열어 본 것을 구분한다. 파일 보안 보강도 운영 수준 인증·권한·악성 파일 검사·동시 접근 방어를 모두 완성한 구현은 아니다.

현재 ZIP에는 pyvenv.cfg가 없는 위치도 있다. 기존 문서의 해당 위치는 과거 환경 학습 기록이며 최신 파일 존재를 보장하지 않는다. 버전은 첨부 requirements 기록과 이번 검증 환경을 구분했다. 파일명의 인코딩이 깨진 자료는 내용을 확인하되 임의 이름으로 원본 이름을 확정하지 않았다.

## 구조 검증과 최종 판단

기존 코드/출력은 6개 문서에서 동일 내용을 보존하며 오류를 포함한 원본 학습 조각은 교정 설명과 함께 둔다. 기존 README의 학습 흐름 블록은 추가 범위에 맞춰 갱신했다. Markdown fence·단일 문서 제목·details·문서 링크·고유 목차 anchor·순차 주제를 검사했다.

최종 판단: 수업 원본에 연결되는 상세 설명을 유지하고 입력·처리·결과·실패를 구체화했다. 사용자 승인 후 전체 파트의 교차 용어·링크·READMEs·색인에 대해 다시 검토해야 한다.

