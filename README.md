# HumanClass Workspace

국비교육의 수업 코드와 [Developer-Wiki](Developer-Wiki/README.md)를 함께 보관하는 학습 공간이다. Wiki는 코드 발췌를 모은 목록에서 한 걸음 더 나아가 **개념·전체 예제·결과·풀이·비교·실습을 갖춘 나만의 교재**로 정리했다. 처음에는 과목 순서로, 나중에는 [용어색인](Developer-Wiki/99_Developer-Wiki_통합_용어색인.md)으로 다시 찾는다.

## 1. 학습 목차

| 순서 | 교재 | 복습할 질문 |
| --- | --- | --- |
| 00 | [메모리와 참조](Developer-Wiki/00_메모리와_참조%28Stack_Heap%29/README.md) | 같은 객체의 변경과 이름의 재할당을 어떻게 구별할까? |
| 01 | [HTML](Developer-Wiki/01_HTML/README.md) | 문서의 구조와 제출할 입력값을 어떻게 표현할까? |
| 02 | [CSS](Developer-Wiki/02_CSS/README.md) | 어떤 요소가 선택되고 크기·배치가 어떻게 정해질까? |
| 03 | [JavaScript](Developer-Wiki/03_JavaScript/README.md) | 이벤트 뒤 값·화면·요청이 어떻게 바뀔까? |
| 04 | [Python](Developer-Wiki/04_Python/README.md) | 자료·함수·객체·파일이 어떤 값을 주고받을까? |
| 05 | [SQL·MariaDB](Developer-Wiki/05_SQL/README.md) | 조건·조인·변경·확정 뒤 어떤 행이 남을까? |
| 06 | [FastAPI](Developer-Wiki/06_FastAPI/README.md) | 요청이 함수·화면·DB·파일·세션으로 어떻게 이어질까? |
| 07 | [데이터 분석·머신러닝](Developer-Wiki/07_데이터분석과_머신러닝/README.md) | 입력·정답·학습·예측·평가를 어떻게 구별할까? |
| 08 | [Elasticsearch·RAG](Developer-Wiki/08_Elasticsearch와_RAG/README.md) | 어떤 자료를 찾고 답변의 문맥으로 전달할까? |
| 09 | [영화 자료·추천·평가](Developer-Wiki/09_영화CSV_청크와_임베딩/README.md) | 영화 특징과 평점 관계로 각각 어떻게 찾고 추천할까? |

수업 원본은 workspace_html·workspace_python·workspace_sql에 있다. Wiki는 원본과 설명·새 예제를 구별한다. 09의 폴더명 08_langgraph가 그래프 실행 구현을 의미하지는 않는다. 현재 확인한 CSV·임베딩·검색·추천·평가를 기준으로 읽는다.

## 2. 한 장을 공부하는 순서

목표 → 개념 → 작은 전체 예제·결과 → 실제 코드 풀이 → 파일·함수 연결 → 장점·한계·개선 → 필요한 강사님 비교 → 추적·실험 → 하단 TIP·출처 → 복습 순서다. 안내·문제·색인은 역할에 맞게 구성했다.

과목별 본문 뒤에는 새 장별 문제 총 **144개**, 실제 수업 퀴즈가 있으면 그 비교, 실무 스타일, 종합실습이 이어진다. 문제는 예상·이유·한 가지 변경을 적고 접힌 풀이와 비교한다. 필요한 패키지·폴더·전체 파일은 각 예제에서 확인한다.

## 3. 출처와 학습 범위

강사님 코드는 유익한 차이에만 인용하고 내 코드에는 바로 풀이와 개선 이유를 붙였다. 원본 발췌는 독립 실행 파일과 구별하고 새 전체 예제·개선안·가상 입력을 표시했다. 📚는 외부 근거, 💡는 본문 하단의 추가 학습, 이후 첨부는 확인이 부족한 항목이다.

사용자 확인상 recall_at_k부터의 후반부는 빠진 수업의 강사님 코드를 옮긴 복습 자료다. 시작 경계는 추정이며 직접 작성 성과로 평가하지 않는다. 작업 중 바뀐 09 소스는 확보한 사본 기준임을 해당 목차에 적었다.

Lib/site-packages·Scripts·share·__pycache__·컴파일 생성물·.env·cfg 같은 설치·설정 생성물은 학습 코드 근거에서 제외했다. 가상환경 폴더 자체를 제외해 직접 작성한 소스까지 놓치지는 않았다. 실제 키·접속 비밀값은 공개 교재로 옮기지 않았다.

## 4. 실행과 확인

HTML·CSS·JavaScript는 브라우저와 개발자도구, Python은 해당 장의 인터프리터·작업 폴더를 확인한다. FastAPI 서버 실행과 Python 파일 직접 실행은 다르다. 데이터·추천 실습은 pandas·scikit-learn·Surprise처럼 장마다 필요한 환경이 다르다.

검증은 실제 작은 실행·브라우저·요청·로컬 DB와 정적 검사·고정 대역을 나누었다. 가상 자료의 높은 점수나 고정 AI 응답을 실제 서비스 성능이라고 설명하지 않는다. [현재 책형 검수 기록](Developer-Wiki/편집기록/책형_개편_진행기록.md)에서 확인 범위와 이후 첨부를 본다.

## 5. 문서 적용

문서 적용 대상은 **Developer-Wiki 폴더 전체와 이 최상위 README.md**다. 두 파일 묶음은 같은 시점의 결과를 사용한다. 수업 원본·가상환경·DB 파일을 문서와 함께 교체하지 않는다. 예전 과목 ZIP과 이전 개편의 최종 ZIP은 이번 책형 결과와 구별한다.

[교재 첫 화면](Developer-Wiki/README.md) · [편집 기록](Developer-Wiki/편집기록/README.md)

<!-- 이전 목차 주소 보존 -->
<a id="humanclass-workspace"></a>
<a id="wiki의-코드와-설명을-읽는-법"></a>
<a id="문서-적용과-기록"></a>
<a id="실행-환경"></a>
<a id="폴더와-학습-순서"></a>
