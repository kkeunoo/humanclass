# 07 FastAPI MariaDB SQLModel 사원 CRUD — 연습문제

[원본 비교 본문](../../07_FastAPI_MariaDB_SQLModel_사원_CRUD.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**다. 강사님이 낸 시험이나 내 당시 구현 코드가 아니다. 본문의 강사님 코드와 내 코드를 읽고 답을 예상한다. 외부 DB·API를 실제로 호출하지 않아도 풀 수 있다.

## 문제

`GET /emp/deptno?deptno=20`의 20을 SQL에 넣을 때 PyMySQL과 SQLModel은 각각 어떤 자리표시자와 값 전달 형태를 쓰는가? 변경을 저장할 때는 무엇을 확인해야 하는가?

<details>
<summary>정답과 확인할 점</summary>

PyMySQL 원본은 SQL의 `%s` 자리에 `(deptno,)`를 별도로 전달한다. SQLModel 원본은 `:deptno` 자리에 `{'deptno': deptno}`를 넘긴다. `INSERT`·`UPDATE`·`DELETE` 후에는 변경이 `commit()`으로 확정됐는지, 오류가 났다면 `rollback()` 경로를 탔는지 확인한다. 메모리 리스트 CRUD와 저장 위치도 다르다.

입력→처리→결과의 실제 원본 사례는 [본문](../../07_FastAPI_MariaDB_SQLModel_사원_CRUD.md)에서 확인한다.

</details>

## 추가로 알면 좋은 것

본문에 없는 기능을 추가했다면 실제 수업 구현과 구별해 기록한다. 외부 서비스의 실제 응답이나 미완성 코드를 성공 사례로 가정하지 않는다.
