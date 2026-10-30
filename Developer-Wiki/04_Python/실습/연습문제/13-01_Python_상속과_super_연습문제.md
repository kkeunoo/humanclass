# 13-01. 상속과 super — 같은 인스턴스의 부모 초기화 이어가기 — 연습문제

[본문](../../13-01_Python_상속과_super.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

부모 메서드 조회와 자식 초기화를 설명한다. 자식이 __init__을 정의한 경우와 물려받는 경우, 부모의 필수 인자를 넘기는 두 방법을 비교한다.

[전체 Python 파일](../책형_복습/13-01_Python_상속과_super.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../13-01_Python_상속과_super.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



```python
class Person:
    def __init__(self, name):
        print('부모 초기화', name)
        self.name = name
    def greeting(self):
        print('안녕하세요', self.name)
class Student(Person):
    def __init__(self, name, grade):
        print('자식 초기화 시작')
        super().__init__(name)
        self.grade = grade
        print('자식 초기화 끝')
    def study(self):
        self.greeting()
        print(self.grade, '학년 공부')
class InheritedStudent(Person):
    pass
a = Student('민지', 3)
a.study()
b = InheritedStudent('준호')
b.greeting()
```

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
자식 초기화 시작
부모 초기화 민지
자식 초기화 끝
안녕하세요 민지
3 학년 공부
부모 초기화 준호
안녕하세요 준호
```

Student는 자기 초기화를 정의하므로 시작 문구 뒤 super로 Person 초기화를 호출하고 grade를 넣어 끝낸다. greeting은 Student에 없지만 Person에서 찾아 self.name을 읽는다. InheritedStudent는 초기화를 정의하지 않아 Person의 것을 사용하며 이름 인자 준호를 정상 전달한다. 이 둘을 함께 보면 부모의 필수 인자 때문에 자식 초기화가 무조건 필요하다는 오해를 피할 수 있다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. 자식에 greeting이 없어도 호출되는 이유는?
2. 부모가 name을 요구하면 자식 __init__ 정의가 항상 필수인가?
3. super 초기화는 새 부모 객체를 추가로 만드는가?

<details>
<summary>풀이</summary>

부모에서 메서드를 찾아 사용한다. 물려받은 초기화에 생성 인자를 전달할 수 있어 항상 필수는 아니다. 같은 자식 인스턴스에 부모의 준비 작업을 수행한다.

| 원본 동작 | 생성되는 속성 | 출력 순서 |
| --- | --- | --- |
| Student2 초기화 진입 | 아직 school·hello 준비 전 | 자식 초기화 문구 |
| 부모 초기화 호출 | hello='방가' | 부모 초기화 문구 |
| 자식의 다음 대입 | school='휴먼' | 이후 두 속성 출력 |
| Student4에서 None 전달 | hello·str=None | 부모 문구와 방가 |

super 호출을 지운다고 모든 부모 메서드가 사라지는 것은 아니다. 다만 부모 초기화가 만들던 속성이 준비되지 않을 수 있다. 메서드를 상속하는 것과 그 메서드가 사용할 데이터의 준비는 연결해서 확인해야 한다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| Student의 super 호출 제거 | greeting 때 name 조회 오류 | 준비한 대입 누락 |
| InheritedStudent 호출의 이름 생략 | 필수 인자 오류 | 물려받은 초기화도 인자 필요 |
| 자식 grade만 변경 | 부모 name 그대로 | 별도 속성 |
| greeting을 자식에 정의 | 자식 동작 사용 | 재정의는 다음 장에서 연결 |

<details>
<summary>막힐 때 확인할 것</summary>

속성이 없으면 어느 초기화가 그것을 만드는지 찾아 호출 여부를 본다. 생성 인수 오류는 실제 사용하는 __init__ 정의를 확인한다. 부모를 쓴다는 이유만으로 별도 부모 인스턴스가 자동 생겼다고 그리지 않는다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
