# StateGraph에서 추천 경로를 분기하기 연습문제

[본문](../../04_StateGraph와_조건분기.md) · [문제 목록](README.md)

본문의 실행 파일로 예상과 실제를 비교한다. 먼저 아래 질문에 답하고 8절의 한 가지 변경을 실행해 본다.

1. `compile()`과 `invoke()`는 각각 무엇을 하는가?
2. `select` 뒤에서 영화 목록이 없는 CBF 요청은 어디로 가는가?

<details>
<summary>풀이와 확인 기준</summary>

1. `compile()`은 설정한 그래프를 실행할 객체로 만들고, `invoke()`는 입력 상태를 주어 실제 흐름을 실행한다.
2. `validator`가 `ERROR`를 반환해 오류 메시지 노드로 이동한다.

</details>
