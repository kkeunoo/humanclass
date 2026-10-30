# 13-02. 재정의와 추상 클래스 — 같은 호출의 다른 동작과 구현 약속 — 연습문제

[본문](../../13-02_Python_메서드재정의와_추상클래스.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

재정의·부모 호출·다형성을 실제 출력으로 설명한다. 추상 메서드 구현과 인스턴스 생성 가능 여부, 같은 클래스 이름의 재정의, 문제 문구와 실제 완성 코드를 구별한다.

[전체 Python 파일](../책형_복습/13-02_Python_메서드재정의와_추상클래스.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../13-02_Python_메서드재정의와_추상클래스.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



```python
from abc import ABCMeta, abstractmethod
class Champ:
    def attack(self):
        print('기본 공격')
class MagicChamp(Champ):
    def attack(self):
        super().attack()
        print('추가 마법')
class BasicChamp(Champ):
    pass
for champ in [MagicChamp(), BasicChamp()]:
    champ.attack()
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    @abstractmethod
    def go_to_school(self):
        pass
class CourseStudent(StudentBase):
    def study(self):
        print('공부하기')
    def go_to_school(self):
        print('학교가기')
student = CourseStudent()
student.study()
student.go_to_school()
```

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
기본 공격
추가 마법
기본 공격
공부하기
학교가기
```

MagicChamp는 자기 attack 안에서 부모를 먼저 호출하므로 두 줄이고 BasicChamp는 부모 구현 한 줄이다. 두 추상 메서드를 채운 CourseStudent는 생성 가능하고 두 동작을 실제 호출했다. 원본은 a.study만 호출하므로 학교가기까지 출력한 것은 새 예제의 확인 범위다. import도 원본의 * 대신 사용하는 두 이름을 명시한 개선이다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. 재정의하면 부모 구현이 자동으로 먼저 실행되는가?
2. Tico가 start를 정의하지 않아도 무엇이 출력되는가?
3. 추상 클래스는 pass 때문에 생성이 안 되는가?
4. 원본 마지막 Student는 어느 클래스인가?

<details>
<summary>풀이</summary>

super 등으로 명시 호출해야 한다. 부모의 시동을 켭니다가 나온다. 추상 메서드 표시와 구현이 남아 있기 때문이다. StudentBase를 상속해 뒤에서 다시 정의한 Student다.

| 원본 호출 | 찾은 구현 | 실제 출력 |
| --- | --- | --- |
| Student5.hi | 자식 | 야호 |
| Lux.attack | 자식과 명시 super | 기본 공격 + 자식 문구 |
| Jax.attack | 부모 | 기본 공격 |
| Tico.start | 부모 | 시동을 켭니다 |
| 마지막 Student.study | 추상 메서드를 채운 자식 | 공부하기 |

추상 메서드 본문을 작성할 수 없거나 항상 무의미하다는 뜻은 아니다. 원본은 pass로 약속을 보여 주는 최소 예제다. 자식이 구현을 갖춰야 한다는 규칙과 부모 본문의 활용 설계는 다른 질문이다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| MagicChamp의 super 제거 | 추가 마법만 출력 | 부모 자동 실행 아님 |
| BasicChamp에 attack 추가 | 그 새 구현 사용 | 재정의 |
| CourseStudent의 한 구현 제거 | 생성 때 TypeError | 추상 메서드가 남음 |
| 마지막 메서드 호출 제거 | 해당 출력 없음 | 정의와 호출 분리 |

<details>
<summary>막힐 때 확인할 것</summary>

부모 문구가 두 번 보이면 super 호출과 바깥의 추가 호출을 확인한다. 예상한 자식 동작이 없으면 메서드 이름을 본다. 추상 클래스 생성 오류는 빠진 구현 이름을 읽는다. 동명 클래스가 여러 번 나오면 마지막 정의와 객체를 만든 시점을 함께 확인한다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
