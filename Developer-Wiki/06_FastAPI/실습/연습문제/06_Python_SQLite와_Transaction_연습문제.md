# 06 Python SQLite와 Transaction — 연습문제

[원본 비교 본문](../../06_Python_SQLite와_Transaction.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**다. 강사님이 낸 시험이나 내 당시 구현 코드가 아니다. 본문의 강사님 코드와 내 코드를 읽고 답을 예상한다. 외부 DB·API를 실제로 호출하지 않아도 풀 수 있다.

## 문제

SQLite INSERT 뒤 저장을 확정하려면 연결에 무엇을 호출하는가? 또 `with sqlite3.connect(...) as connect:` 블록을 벗어나기만 하면 연결의 `close()`도 자동으로 호출되는가?

<details>
<summary>정답과 확인할 점</summary>

`connect.commit()`으로 트랜잭션을 확정한다. `with sqlite3.connect(...) as connect:`는 정상 종료 때 미확정 변경을 커밋하고 예외가 나면 롤백하지만 **연결을 자동으로 닫지는 않는다**. 강사님·내 원본 주석에 적힌 자동 닫힘 설명을 그대로 외우지 않도록 구분한다. 원본의 `?` 자리와 `(20,)` 전달 값도 함께 확인하자.

입력→처리→결과의 실제 원본 사례는 [본문](../../06_Python_SQLite와_Transaction.md)에서 확인한다.

</details>

## 추가로 알면 좋은 것

본문에 없는 기능을 추가했다면 실제 수업 구현과 구별해 기록한다. 외부 서비스의 실제 응답이나 미완성 코드를 성공 사례로 가정하지 않는다.
