# 02 FastAPI Router Request Pydantic CRUD — 연습문제

[원본 비교 본문](../../02_FastAPI_Router_Request_Pydantic_CRUD.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**다. 강사님이 낸 시험이나 내 당시 구현 코드가 아니다. 본문의 강사님 코드와 내 코드를 읽고 답을 예상한다. 외부 DB·API를 실제로 호출하지 않아도 풀 수 있다.

## 문제

내 Todo처럼 `await request.form()`에서 `id`와 `item`을 꺼내려면 어떤 이름을 조회하는가?

<details>
<summary>정답과 확인할 점</summary>

`data = await request.form()` 다음 `data.get("id")`, `data.get("item")`을 읽는다. `request.headers`는 이 본문 연습의 대상이 아니다.

입력→처리→결과의 실제 원본 사례는 [본문](../../02_FastAPI_Router_Request_Pydantic_CRUD.md)에서 확인한다.

</details>

## 추가로 알면 좋은 것

본문에 없는 기능을 추가했다면 실제 수업 구현과 구별해 기록한다. 외부 서비스의 실제 응답이나 미완성 코드를 성공 사례로 가정하지 않는다.
