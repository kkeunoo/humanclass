# 13-02. 메서드 재정의와 추상 클래스

[Python 목차](README.md) · [이전: 상속과 `super`](13-01_Python_상속과_super.md)

같은 이름의 메서드를 자식에서 다시 정의하면 자식의 동작이 선택된다. 두 원본의 인사·공격 예제로 이를 확인하고, 마지막에 **반드시 구현할 메서드**를 표시한 추상 클래스 예제로 넘어간다.

## 먼저: 같은 이름인데 다른 동작

부모의 메서드를 자식에서 **같은 이름으로 다시 정의**하면 자식 객체를 통해 호출할 때 자식 쪽 구현이 사용된다. 다음은 원본의 상속 문법을 축약한 설명용 재구성이다.

```python
class Person:
    def hello(self):
        return '안녕'

class Student(Person):
    def hello(self):
        return '학생입니다'

print(Student().hello())  # 학생입니다
```

자식에서 `hello`를 정의하지 않으면 부모의 `hello`를 물려받는다. 원본의 추상 클래스는 이 기본 재정의에서 한 걸음 더 나아가 **자식이 구현해야 하는 메서드**를 표시한 예다. 두 개념을 같은 것으로 뭉뚱그리지 말자.

<!-- chapter-toc -->

- [1. 자식 메서드가 부모 메서드를 바꿔 쓰기](13-02_Python_메서드재정의와_추상클래스.md#section-1)
- [2. 자동차 과제: 강사님 문제와 내 실제 구현](13-02_Python_메서드재정의와_추상클래스.md#section-2)
- [3. 추상 클래스에서 요구한 메서드 구현하기](13-02_Python_메서드재정의와_추상클래스.md#section-3)
- [직접 확인할 질문](13-02_Python_메서드재정의와_추상클래스.md#section-4)
- [추가로 알면 좋은 것](13-02_Python_메서드재정의와_추상클래스.md#section-5)

<a id="section-1"></a>

## 1. 자식 메서드가 부모 메서드를 바꿔 쓰기

### 강사님 코드

출처: `teacher/workspace_python/_13_상속.py` 57–85행 · **원본 발췌**

```python
class Person5:
    def hi(self):
        print('안녕하시오')

class Student5(Person5):
    def hi(self):
        print('야호')

s5 = Student5()
s5.hi()

class Champ :
    def attack(self):
        print('기본 공격')

class Lux(Champ) :
    def attack(self):
        super().attack()
        print('데마시~~~~~~아!!!')

class Jax(Champ):
    def defence(self):
        print('절대 지켜')

c1 = Lux()
c2 = Jax()
cList = [c1, c2]
for c in cList:
    c.attack()
```

### 내 코드

출처: `me/workspace_python/13_상속.py` 74–103행 · **원본 발췌**

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

`Student5.hi()`는 부모의 `hi()`와 같은 이름을 새로 정의하므로 `s5.hi()`는 **`야호`**를 출력한다. `Lux.attack()`은 먼저 `super().attack()`으로 부모의 `기본 공격`을 출력하고 자기 문장을 이어 출력한다. `Jax`는 `attack()`을 다시 정의하지 않아 부모 `Champ.attack()`을 그대로 사용한다. `cList`를 돌면 두 객체에 같은 `attack()` 호출을 해도 **실제 객체 종류에 맞는 동작**이 나온다.

<a id="section-2"></a>

## 2. 자동차 과제: 강사님 문제와 내 실제 구현

### 강사님 코드 — 문제 문구

출처: `teacher/workspace_python/_13_상속.py` 88–102행 · **원본 발췌**

```python
# 문제4
'''
부모 Car 클래스
def start(self)
    print('시동을 켭니다')
def accel(self)
    print('속도를 높입니다')

자식 람보르기니
시동걸면 "바랑~"
엑셀을 밟으면 "스~아~앙"

자식 티코
엑셀을 밟으면 "부다다당"
'''
```

### 내 코드 — 구현

출처: `me/workspace_python/13_상속.py` 123–151행 · **원본 발췌**

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

강사님 대응 파일에는 `Car` 과제 **설명만** 있고 `Car`·람보르기니·티코 클래스 구현은 없다. 내 파일에는 `Car`, `Lambo`, `Tico`를 실제로 만들었다. `Lambo.start()`·`Lambo.accel()`은 각각 부모 메서드를 부른 뒤 자기 문장을 덧붙인다. `Tico`는 `accel()`만 재정의하므로 `start()`는 부모 문장이 그대로 나오고, `accel()`은 부모 문장 뒤 티코 문장이 이어진다.

내 문제 메모에는 “티코 시동 걸면 아무것도 없고”라고 적혀 있지만 **실제 실행 결과는 부모 `Car.start()`의 `시동을 켭니다`가 나온다**. 또 과제 문구와 구현의 의성어는 다르다. 이 장에서는 실행 코드 결과를 기준으로 읽는다.

<a id="section-3"></a>

## 3. 추상 클래스에서 요구한 메서드 구현하기

### 강사님 코드

출처: `teacher/workspace_python/_13_상속.py` 104–124행 · **원본 발췌**

```python
from abc import *
# 부모 전용 클래스
class StudentBase(metaclass=ABCMeta) :
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self) :
        pass

class Student(StudentBase) :
    def study(self):
        print('공부하기')
    def go_to_school(self) :
        print('학교가기')

a = Student()
a.study()

# b = StudentBase()
```

### 내 코드

출처: `me/workspace_python/13_상속.py` 153–181행 · **원본 발췌**

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

`StudentBase`에는 `@abstractmethod`를 붙인 `study`와 `go_to_school`이 있다. 자식 `Student`는 두 메서드를 모두 정의하므로 `a=Student()`를 만들고 `a.study()`를 호출할 수 있다. 부모 `StudentBase()`를 직접 만드는 줄은 양쪽 모두 주석 처리됐다. 내 파일의 주석처럼 두 메서드 중 하나를 빠뜨린 자식도 아직 추상 메서드가 남아 있어 객체를 만들 수 없다.

여기서 `Student`라는 이름은 파일 앞부분의 `Student(Person)`에서 이미 한 번 썼다. 뒤에서 `class Student(StudentBase)`로 **이름을 다시 지정**하므로 마지막의 `Student()`는 앞의 인사 학생이 아니라 **추상 기반 클래스를 상속한 학생**이다. 두 원본 모두 이렇게 쓰고 있다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `Lux.attack()`과 `Jax.attack()`의 출력은 어떻게 다를까?
2. 내 `Tico.start()` 호출은 실제로 어느 클래스의 메서드를 실행할까?
3. 파일 마지막 `Student()`는 어느 `Student` 클래스를 뜻할까?

<a id="section-5"></a>

## 추가로 알면 좋은 것

여러 상속 단계에서의 메서드 선택 순서와 추상 클래스의 설계 패턴은 이 원본보다 넓은 주제다. 먼저 **자식이 재정의했는지**, **부모 메서드를 `super()`로 다시 부르는지**를 구분하자.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/13-02_Python_메서드재정의와_추상클래스_연습문제.md) → [14-01. 예외 처리 심화](14-01_Python_예외처리_심화.md)

