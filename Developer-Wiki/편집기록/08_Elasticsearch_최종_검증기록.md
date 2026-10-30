> **이전 개편 이력:** 당시 판단·수치를 보존한 기록이다. 현재 책형 상태는 [최신 기록](책형_개편_진행기록.md)을 따른다.

# 08 Elasticsearch·RAG 검증 기록

[08 단원 목차](../08_Elasticsearch와_RAG/README.md) · [편집기록 목차](README.md)

2026-10-26. `D:\workspace_teacher\workspace_python\07_elastic`와 `D:\workspace\workspace_python\07_elastic`의 `api.py`, `run.py`, `util.py`, 두 라우터를 확인하고 README와 본문 5장을 작성했다. 코드에서 실제 호출하는 흐름을 본문으로 삼고 `.env`·접속키·가상환경 설치물은 제외했다.

- **원본 비교:** 강사님 원본을 먼저, 내 원본을 아래에 놓았다. 출처·행 번호가 있는 발췌 34곳을 두 폴더의 현재 파일과 대조했다.
- **중요 차이:** 강사님 `select_all`은 만든 `results` 대신 원본 `response`를 반환한다. 강사님 삽입의 `document.get(id, -1)`과 내 `document.get('id', -1)`도 구별했다. 내 `ask_gemini`의 실행 코드는 함수명과 달리 GPT 호출이다.
- **공통 개선점:** `text` 분석과 벡터 임베딩을 혼동한 주석, `doc2 = doc`에 따른 청크별 자료 공유, 벡터는 청크로 만들면서 `_source['content']`에 원본문서를 남기는 흐름을 분리해 설명했다.
- **실행 한계:** Elasticsearch·외부 AI 서비스의 실제 응답, 호출 성공, 검색 품질은 확인하지 않았다. 인덱스 생성·문서 적재·삭제 요청도 보내지 않았다.

다음은 양쪽 `08_langgraph` 폴더에서 **실제 코드가 구현한 영화 CSV 가공·청크·임베딩**을 09로 정리한다. 폴더명만 근거로 LangGraph 그래프 실행을 완료 항목에 넣지 않는다.
