# LangChain과 LangGraph

[전체 Wiki](../README.md) · [이전 영화 추천](../09_영화CSV_청크와_임베딩/README.md) · [용어 색인](../99_Developer-Wiki_통합_용어색인.md)

## 1. 이 단원에서 연결하는 것

영화의 후보와 점수는 09에서 만들었다. 여기서는 메시지를 만들고 모델의 출력 형식을 정리한 다음, 영화 후보를 설명한다. 질문에 따라 CBF·CF·BM25를 선택하고 필수 입력을 검사하는 단계는 LangGraph에서 읽는다.

## 2. 읽는 순서

- [모델 호출과 대화 메시지](01_모델호출과_메시지.md)
- [출력 파서와 구조화 출력](02_출력파서와_구조화출력.md)
- [영화 추천 결과를 설명하는 체인](03_영화추천결과_설명체인.md)
- [StateGraph에서 추천 경로를 분기하기](04_StateGraph와_조건분기.md)
- [추천 노드에서 후보를 최종 상태로 전달하기](05_추천노드와_최종상태.md)
- [실무 코딩스타일](실무_코딩스타일.md)
- [종합실습](종합실습.md)
- [실습 환경](실습/README.md) · [장별 연습문제 6개](실습/연습문제/README.md)

## 3. 실제 코드와 복습 예제

2026-11-09 양쪽 `workspace_python/08_langgraph`의 `api.py`, `router/langchain_router.py`, `router/langgraph_router.py`, `router/es_router.py`와 패키지 목록을 대조했다. ‘내 폴더’는 현재 저장된 코드의 위치를 가리킨다. 개인 풀이·공동 풀이·옮겨 온 코드라는 근거가 있는 경우만 작성 경위를 구별한다. 양쪽 그래프의 조건 간선에서 재현한 오류와 수정 예시는 [04장](04_StateGraph와_조건분기.md)에서 확인한다.

3절의 복습 예제는 외부 호출 대신 고정 입력이나 모델 대역을 사용한다. 원본의 모델 응답·ES 접속·실제 추천 품질은 별도 검증 범위다. 메모에만 있는 LangSmith 추적, batch와 병렬 실행, itemgetter, passthrough, synthesize의 상세 실습은 이후 첨부로 둔다.

[전체 Wiki](../README.md) · [실습 안내](실습/README.md)
