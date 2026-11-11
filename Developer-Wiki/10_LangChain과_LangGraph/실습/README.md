# LangChain과 LangGraph 실습 안내

[단원 목차](../README.md) · [문제 목록](연습문제/README.md) · [종합실습](../종합실습.md)

각 본문 3절의 `example.py`는 수업 환경의 Python으로 실행한다. 01~03은 `langchain-core`와 예제에 따라 Pydantic을 사용한다. 04와 종합실습에는 `langgraph`, 스타일 예제에는 Pydantic이 필요하다. 05는 표준 Python으로 실행한다. 수업 폴더의 가상환경 인터프리터로 확인할 수 있다.

```powershell
& 'D:/workspace/workspace_python/08_langgraph/Scripts/python.exe' '실습/책형_복습/04_StateGraph와_조건분기/example.py'
```

위 명령의 예제 경로는 이 단원 폴더를 현재 위치로 가정한다. 새 예제는 외부 모델·Elasticsearch에 요청하지 않는다. 원본 라우터의 동작을 보려면 원본 프로젝트의 서버 실행 환경, 설정, API 접근이 필요하다.

각 문제는 결과를 먼저 예상하고, 이유를 설명하고, 하나의 조건을 바꿔 다시 실행한다. 접힌 풀이에서 예상한 경로와 실제 출력이 같은지 비교한다.
