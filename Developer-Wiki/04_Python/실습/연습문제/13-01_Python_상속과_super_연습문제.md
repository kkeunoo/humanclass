# 13-01 Python 상속과 super — 연습문제

[원본 비교 본문](../../13-01_Python_상속과_super.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**다. 강사님이 낸 원본 문제나 내 당시 풀이가 아니다. 본문에서 강사님 코드와 내 코드를 먼저 읽고, 결과를 예상한 다음 답을 펼친다.

## 문제

부모 `Person.__init__`이 `self.name`을 만들고 자식 `Student.__init__`이 `self.grade`를 만든다. 자식 생성자에서 부모 초기화를 생략하면 `student.name`을 읽을 수 있을까? 어떤 호출을 넣어야 할까?

<details>
<summary>정답과 확인할 점</summary>

자식이 자신의 `__init__`을 정의하면 이 문제에서는 부모 생성자를 자동으로 실행했다고 가정하지 않는다. `super().__init__(name)`을 호출해 부모가 `self.name`을 만들게 해야 한다. 그 뒤 `self.grade = grade`를 저장한다. 호출을 빼면 이름 속성이 없어 `student.name`을 읽을 때 `AttributeError`가 날 수 있다. 양쪽 원본의 초기화 전후 결과를 비교하자.


</details>

