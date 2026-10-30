# 13-02. 재정의와 추상 클래스 — 같은 호출의 다른 동작과 구현 약속

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

부모 메서드를 그대로 쓰는 경우, 같은 이름을 다시 정의하는 경우, 부모 동작 뒤 자기 작업을 덧붙이는 경우를 나누어 본다. 그다음 자식이 반드시 채워야 할 메서드를 정하는 추상 클래스와 연결한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

재정의·부모 호출·다형성을 실제 출력으로 설명한다. 추상 메서드 구현과 인스턴스 생성 가능 여부, 같은 클래스 이름의 재정의, 문제 문구와 실제 완성 코드를 구별한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

재정의는 자식 클래스에 부모와 같은 이름의 메서드를 정의하는 것이다. 자식 인스턴스에서 호출하면 자식의 동작을 사용한다. 부모 구현도 함께 필요하면 super로 명시 호출한다. 재정의했다고 부모 동작이 자동으로 먼저 실행되는 것은 아니다.

| 클래스 상태 | 같은 attack 호출 | 부모 출력도 생기는가? |
| --- | --- | --- |
| 자식이 재정의 안 함 | 부모 attack | 부모 동작 |
| 자식이 새 attack만 정의 | 자식 attack | 자동으로는 아님 |
| 자식 attack에서 super 호출 | 부모 뒤 자식 작업 | 명시 호출한 순서대로 |

객체 목록에 같은 메서드 이름을 호출해도 실제 객체 종류에 따라 다른 구현을 사용할 수 있다. 이를 이 실습의 다형성 관점으로 읽는다. 단순히 함수 이름이 같다는 사실보다 각 객체가 어떤 구현을 찾는지가 핵심이다.

추상 클래스는 abc 도구로 구현할 메서드의 약속을 표시한 것이다. @abstractmethod가 남아 있는 클래스는 직접 인스턴스를 만들 수 없다. pass라는 본문 자체가 원인은 아니다. 일반 클래스의 pass 메서드는 호출해도 아무 일 없이 끝날 수 있지만 추상 표시가 있는 메서드는 구현 약속을 만든다.

> 📚 **출처 · 본문 설명 확인:** [Python 상속·메서드 재정의](https://docs.python.org/ko/3/tutorial/classes.html#inheritance), [abc 공식 문서](https://docs.python.org/ko/3/library/abc.html). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/13-02_Python_메서드재정의와_추상클래스.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



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

MagicChamp는 자기 attack 안에서 부모를 먼저 호출하므로 두 줄이고 BasicChamp는 부모 구현 한 줄이다. 두 추상 메서드를 채운 CourseStudent는 생성 가능하고 두 동작을 실제 호출했다. 원본은 a.study만 호출하므로 학교가기까지 출력한 것은 새 예제의 확인 범위다. import도 원본의 * 대신 사용하는 두 이름을 명시한 개선이다.

**예상 출력 또는 관찰:**

```text
기본 공격
추가 마법
기본 공격
공부하기
학교가기
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/13_상속.py` 74–103행

```python
class Person5 :
    def hi(self) :
        print('안녕하시오')

class Student5(Person5) :
    def hi(self) :
        print('야호')

s5 = Student5()
s5.hi()

class Champ :
    def attack(self) :
        print('기본 공격')

class Lux(Champ) :
    def attack(self) :
        super().attack()
        print('데마시~~~~~~아!!!')

class Jax(Champ) :
    def defence(self) :
        print('절대 지켜')

c1 = Lux()
c2 = Jax()
cList = [c1, c2]

for c in cList :
    c.attack()
```

**발췌 바로 풀이:** `Student5.hi()`는 부모의 `hi()`와 같은 이름을 새로 정의하므로 `s5.hi()`는 **`야호`**를 출력한다. `Lux.attack()`은 먼저 `super().attack()`으로 부모의 `기본 공격`을 출력하고 자기 문장을 이어 출력한다. `Jax`는 `attack()`을 다시 정의하지 않아 부모 `Champ.attack()`을 그대로 사용한다. `cList`를 돌면 두 객체에 같은 `attack()` 호출을 해도 **실제 객체 종류에 맞는 동작**이 나온다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/13_상속.py` 123–151행

```python
class Car :
    def start(self) :
        print('시동을 켭니다')

    def accel(self) :
        print('속도를 높입니다')

class Lambo(Car) :
    def start(self) :
        super().start()
        print('Lambo : 바라랑~')

    def accel(self) :
        super().accel()
        print('Lambo : 스아앙~')

class Tico(Car) :
    def accel(self) :
        super().accel()
        print('Tico : 덜덜덜덜')

c1 = Lambo()
c2 = Tico()

carList = [c1, c2]

for c in carList :
    c.start()
    c.accel()
```

**발췌 바로 풀이:** 강사님 대응 파일에는 `Car` 과제 **설명만** 있고 `Car`·람보르기니·티코 클래스 구현은 없다. 내 파일에는 `Car`, `Lambo`, `Tico`를 실제로 만들었다. `Lambo.start()`·`Lambo.accel()`은 각각 부모 메서드를 부른 뒤 자기 문장을 덧붙인다. `Tico`는 `accel()`만 재정의하므로 `start()`는 부모 문장이 그대로 나오고, `accel()`은 부모 문장 뒤 티코 문장이 이어진다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/13_상속.py` 153–181행

```python
# 추상 클래스 사용하기 (abc.ABCmeta, @abc, @abstractmethod 사용 할 수 있음)
from abc import * 

# @abstractmethod를 사용하려면, metaclass는 사용해주어야 함
class StudentBase(metaclass=ABCMeta) :
    @abstractmethod
    def study(self) :
        pass

    @abstractmethod
    def go_to_school(self) :
        # print(123) 처럼 넣어두어도 override를 자식에서 해야 하기 때문에, 무의미
        pass

class Student(StudentBase) :
    def study(self) :
        print('공부하기')
    def go_to_school(self): # 부모의 abstract method를 강제할 수 있음
        print('학교가기')

a = Student()
# 부모에는 study, go_to_school이 있는데 study만 사용했을 경우 아래와 같은 Error 발생 (abstract 'go_to_school' method를 사용하지 않았다)
# TypeError: Can't instantiate abstract class Student without an implementation for abstract method 'go_to_school'
a.study() 

# 부모에는 'pass'이고 구현되어 있지 않았기 때문에, 생성할 수 없음
# TypeError: Can't instantiate abstract class StudentBase without an implementation for abstract methods 'go_to_school', 'study'
# b = StudentBase()
```

**발췌 바로 풀이:** `StudentBase`에는 `@abstractmethod`를 붙인 `study`와 `go_to_school`이 있다. 자식 `Student`는 두 메서드를 모두 정의하므로 `a=Student()`를 만들고 `a.study()`를 호출할 수 있다. 부모 `StudentBase()`를 직접 만드는 줄은 양쪽 모두 주석 처리됐다. 내 파일의 주석처럼 두 메서드 중 하나를 빠뜨린 자식도 아직 추상 메서드가 남아 있어 객체를 만들 수 없다.

내 Student5.hi는 야호, Lux.attack은 기본 공격 뒤 자기 문구다. Jax는 attack을 재정의하지 않아 기본 공격을 쓴다. 내 Car·Lambo·Tico는 실제 구현이지만 강사님 대응 구간은 과제 설명뿐이다. Tico는 accel만 재정의하여 start는 부모 시동 문구가 나온다. 마지막 Student는 앞의 동명 클래스가 아니라 StudentBase를 상속해 다시 정의한 클래스다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

cList에서 객체 하나 받기 → 그 객체의 attack 조회 → 자식 구현 여부 확인 → 필요하면 super로 부모 실행 → 다음 객체 순서다. abc에서 가져온 ABCMeta·abstractmethod의 이름을 추상 기반 정의에 사용한다. StudentBase → 자식 두 메서드 구현 → Student() 생성 → study() 호출이다. 정의와 실제 호출을 구분하여 go_to_school이 정의만 되었어도 출력까지 있었던 것으로 세지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 자동차 과제는 실제 클래스를 구현하고 같은 start·accel 호출을 반복한다. **교정:** Tico 시동이 없다는 메모와 달리 상속한 start가 실행된다. 추상 클래스는 pass라서 생성이 막힌다는 설명도 고친다. **구현 선택:** super 호출이 있어 부모 문구까지 출력하는데 과제에서 자식 소리만 요구했다면 요구와 비교해야 한다. 실행 코드를 출력 기준으로 읽되 요구 충족 평가는 별도다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



공격·추상 클래스 핵심은 같아 강사님 구현을 반복하지 않는다. 자동차 대응은 강사님 문제와 내 구현의 비교이며 존재하지 않는 강사님 완성 코드를 만들어 인용하지 않는다. 같은 이름 Student가 파일 안에서 다시 정의되어 마지막 호출의 의미가 바뀌는 점은 양쪽 공통이다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 호출 | 찾은 구현 | 실제 출력 |
| --- | --- | --- |
| Student5.hi | 자식 | 야호 |
| Lux.attack | 자식과 명시 super | 기본 공격 + 자식 문구 |
| Jax.attack | 부모 | 기본 공격 |
| Tico.start | 부모 | 시동을 켭니다 |
| 마지막 Student.study | 추상 메서드를 채운 자식 | 공부하기 |

추상 메서드 본문을 작성할 수 없거나 항상 무의미하다는 뜻은 아니다. 원본은 pass로 약속을 보여 주는 최소 예제다. 자식이 구현을 갖춰야 한다는 규칙과 부모 본문의 활용 설계는 다른 질문이다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| MagicChamp의 super 제거 | 추가 마법만 출력 | 부모 자동 실행 아님 |
| BasicChamp에 attack 추가 | 그 새 구현 사용 | 재정의 |
| CourseStudent의 한 구현 제거 | 생성 때 TypeError | 추상 메서드가 남음 |
| 마지막 메서드 호출 제거 | 해당 출력 없음 | 정의와 호출 분리 |

부모 문구가 두 번 보이면 super 호출과 바깥의 추가 호출을 확인한다. 예상한 자식 동작이 없으면 메서드 이름을 본다. 추상 클래스 생성 오류는 빠진 구현 이름을 읽는다. 동명 클래스가 여러 번 나오면 마지막 정의와 객체를 만든 시점을 함께 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 다중 상속 탐색·추상 기반의 고급 설계 패턴·Protocol·동적 메서드 교체는 추가 학습이다. 기본은 현재 자식의 재정의와 명시 부모 호출·필수 구현을 구별하는 것이다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 재정의하면 부모 구현이 자동으로 먼저 실행되는가?
2. Tico가 start를 정의하지 않아도 무엇이 출력되는가?
3. 추상 클래스는 pass 때문에 생성이 안 되는가?
4. 원본 마지막 Student는 어느 클래스인가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

super 등으로 명시 호출해야 한다. 부모의 시동을 켭니다가 나온다. 추상 메서드 표시와 구현이 남아 있기 때문이다. StudentBase를 상속해 뒤에서 다시 정의한 Student다.

</details>

| 질문 | 확인 |
| --- | --- |
| 같은 이름? | 실제 자식 구현 |
| 부모도 실행? | 명시 super 호출 |
| 생성 가능? | 남은 추상 메서드 |
| 어느 클래스? | 정의 순서·생성 시점 |

[장별 연습문제](실습/연습문제/13-02_Python_메서드재정의와_추상클래스_연습문제.md) · 다음은 [예외 처리 심화](14-01_Python_예외처리_심화.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
