---
title: Python 상속과 다형성
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# Python 상속과 다형성

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `13_Python_상속과_다형성.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `11_Python_함수.md`, `12_Python_클래스.md` |
| 다음 학습 | `14_Python_예외처리.md` |
| 원본 기준 | `workspace_python/13_*.py`, `workspace_teacher/workspace_python/_13_*.py` |
| 핵심 범위 | 상속, 부모 클래스, 자식 클래스, 부모 생성자, `super()`, 메서드 오버라이딩, 다형성, 추상 클래스, `ABCMeta`, `@abstractmethod` |
| 실습 범위 | 학생 클래스, 챔피언 공격, 자동차 동작, 추상 학생 클래스 |
| 종합 실습 | 별도 문서 `20_Python_종합실습.md`에서 관리 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 한 번에 나열하지 않는다.  
> 각 개념에 필요한 코드만 발췌하고, 실행 결과·동작 과정·코드 사용 목적·주의점을 함께 설명한다.

---

# 개요

상속은 이미 만들어진 클래스의 속성과 메서드를 새로운 클래스가 이어받아 사용하는 기능이다.

```text
기존 클래스
    ↓
공통 기능 상속
    ↓
새 클래스에서 재사용
    ↓
필요한 기능만 추가하거나 변경
```

예를 들어 학생도 사람의 한 종류라면, 사람의 공통 기능을 다시 작성하지 않고 `Person` 클래스로부터 이어받을 수 있다.

```python
class Person:
    def greeting(self):
        print("안녕하세요")


class Student(Person):
    def study(self):
        print("공부합니다")
```

`Student`는 직접 정의한 `study()`뿐 아니라 부모 클래스의 `greeting()`도 사용할 수 있다.

상속을 사용하면 **공통 기능을 재사용**하고, 자식 클래스마다 **다른 동작을 구현**할 수 있다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 부모 클래스 | 공통 속성과 메서드를 제공하는 클래스 |
| 자식 클래스 | 부모 클래스를 상속받아 기능을 확장하는 클래스 |
| 상속 | 기존 클래스의 기능을 이어받는 구조 |
| `super()` | 부모 클래스의 메서드나 생성자를 호출하는 기능 |
| 오버라이딩 | 부모 메서드를 자식 클래스에서 다시 정의하는 것 |
| 다형성 | 같은 메서드 호출이 객체에 따라 다르게 동작하는 성질 |
| 추상 클래스 | 자식 클래스가 구현해야 할 메서드의 규칙을 정하는 클래스 |
| `@abstractmethod` | 자식 클래스가 반드시 구현해야 하는 메서드 표시 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 부모 클래스와 자식 클래스의 차이를 설명할 수 있다.
- `class 자식(부모)` 문법으로 상속 관계를 만들 수 있다.
- 자식 객체가 부모 메서드를 사용할 수 있다는 점을 이해한다.
- 부모와 자식 생성자의 실행 관계를 설명할 수 있다.
- 자식 생성자에서 `super().__init__()`이 필요한 경우를 구분할 수 있다.
- 부모 생성자에 필수 인자가 있을 때 자식이 값을 전달할 수 있다.
- 메서드 오버라이딩의 의미를 설명할 수 있다.
- 부모 기능을 유지하면서 새 기능을 추가할 수 있다.
- 같은 메서드 호출이 객체마다 다르게 동작하는 다형성을 이해한다.
- 반복문에서 서로 다른 자식 객체를 같은 방식으로 호출할 수 있다.
- 추상 클래스와 일반 클래스의 차이를 설명할 수 있다.
- `@abstractmethod`가 자식 클래스에 구현을 강제하는 이유를 이해한다.

---

# 1. 상속이란?

상속은 부모 클래스에 정의된 속성과 메서드를 자식 클래스가 이어받아 사용하는 기능이다.

## 1-1. 내 코드

```python
class Person:
    def greeting(self):
        print("안녕하세요")


class Student(Person):
    def study(self):
        print("공부하기")
        self.greeting()
```

## 1-2. 강사님 코드

```python
class Person:
    def greeting(self):
        print("안녕하세요")


class Student(Person):
    def study(self):
        print("공부하기")
        self.greeting()
```

두 코드는 같은 구조로 상속의 기본 동작을 보여 준다.

## 1-3. 구성

| 코드 | 사용하는 이유 |
| --- | --- |
| `class Person` | 공통 기능을 제공하는 부모 클래스를 정의하기 위해 |
| `class Student(Person)` | `Person`을 상속받는 자식 클래스를 정의하기 위해 |
| `study()` | 학생에게만 필요한 기능을 추가하기 위해 |
| `self.greeting()` | 상속받은 부모 메서드를 현재 학생 객체에서 호출하기 위해 |

## 1-4. 실행

```python
student = Student()

student.study()
student.greeting()
```

## 1-5. 출력 결과

```text
공부하기
안녕하세요
안녕하세요
```

## 1-6. 동작 과정

```text
Student() 객체 생성
    ↓
Student 클래스에서 study() 확인
    ↓
student.study() 실행
    ↓
공부하기 출력
    ↓
self.greeting() 검색
    ↓
Student에 greeting() 없음
    ↓
부모 Person에서 greeting() 발견
    ↓
안녕하세요 출력
```

> [!IMPORTANT]
> 자식 클래스에 메서드가 없으면 Python은 부모 클래스에서 같은 이름의 메서드를 찾는다.

---

# 2. 부모 클래스와 자식 클래스

상속 관계에서는 클래스를 다음과 같이 부른다.

```text
Person
└─ 부모 클래스

Student
└─ 자식 클래스
```

다른 표현도 자주 사용한다.

| 구분 | 다른 표현 |
| --- | --- |
| 부모 클래스 | 슈퍼 클래스, 기반 클래스, Base Class |
| 자식 클래스 | 서브 클래스, 파생 클래스, Derived Class |

## 2-1. `is-a` 관계

상속은 일반적으로 **자식은 부모의 한 종류다**라는 관계가 자연스러울 때 사용한다.

```text
Student is a Person
학생은 사람이다
```

```text
Lamborghini is a Car
람보르기니는 자동차다
```

좋지 않은 예:

```text
Engine is a Car
엔진은 자동차다
```

엔진은 자동차의 한 종류가 아니라 자동차가 가지는 부품이므로 상속보다 포함 관계가 자연스럽다.

> [!TIP]
> “자식은 부모의 한 종류인가?”라는 질문이 자연스럽게 성립하는지 먼저 확인한다.

---

# 3. 상속받은 메서드 사용

자식 클래스는 부모의 공개 메서드를 자신의 메서드처럼 호출할 수 있다.

```python
student.greeting()
```

또한 자식 클래스 내부에서도 `self`를 통해 호출할 수 있다.

```python
class Student(Person):
    def study(self):
        self.greeting()
```

## 3-1. 왜 `self`를 사용할까?

`self`는 현재 `Student` 인스턴스를 가리킨다.

```text
self
→ 현재 Student 객체
→ Student에서 greeting() 검색
→ 없으면 Person에서 검색
```

> [!IMPORTANT]
> 상속받은 메서드도 현재 객체가 사용하는 기능이므로 `self.greeting()`처럼 호출한다.

---

# 4. 부모 생성자와 자식 생성자

부모와 자식 클래스 모두 `__init__()`을 가질 수 있다.

## 4-1. 내 코드

```python
class Person2:
    def __init__(self):
        print("Person2 __init__ 실행")
        self.hello = "방가"


class Student2(Person2):
    def __init__(self):
        print("Student2 __init__ 실행")
        super().__init__()
        self.school = "휴먼"
```

## 4-2. 강사님 코드

```python
class Person2:
    def __init__(self):
        print("Person2 __init__ 실행")
        self.hello = "방가"


class Student2(Person2):
    def __init__(self):
        print("Student2 __init__ 실행")
        super().__init__()
        self.school = "휴먼"
```

## 4-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `Student2(Person2)` | `Person2`의 기능을 상속받기 위해 |
| `Student2.__init__()` | 학생 객체의 초기 상태를 설정하기 위해 |
| `super().__init__()` | 부모 `Person2`의 초기화 코드도 실행하기 위해 |
| `self.hello` | 부모 생성자에서 저장하는 속성 |
| `self.school` | 자식 생성자에서 추가하는 속성 |

## 4-4. 실행

```python
student = Student2()

print(student.school)
print(student.hello)
```

## 4-5. 출력 결과

```text
Student2 __init__ 실행
Person2 __init__ 실행
휴먼
방가
```

## 4-6. 동작 과정

```text
Student2() 실행
    ↓
Student2.__init__() 실행
    ↓
Student2 __init__ 실행 출력
    ↓
super().__init__() 호출
    ↓
Person2.__init__() 실행
    ↓
self.hello = "방가"
    ↓
자식 생성자로 돌아옴
    ↓
self.school = "휴먼"
```

> [!IMPORTANT]
> 자식 클래스가 자신의 `__init__()`을 정의하면 부모의 `__init__()`은 자동으로 함께 실행되지 않는다.
>
> 부모 초기화가 필요하면 자식 생성자에서 `super().__init__()`을 직접 호출한다.

---

# 5. `super()`란?

`super()`는 현재 클래스의 부모 클래스 기능에 접근할 때 사용한다.

```python
super().__init__()
```

위 코드는 부모 클래스의 `__init__()`을 호출한다.

일반 메서드에도 사용할 수 있다.

```python
super().attack()
```

## 5-1. 왜 부모 클래스 이름을 직접 쓰지 않을까?

다음처럼 직접 호출할 수도 있다.

```python
Person2.__init__(self)
```

하지만 다음 방식이 더 일반적이다.

```python
super().__init__()
```

이유:

- 현재 클래스의 부모 관계를 기준으로 동작한다.
- 부모 클래스 이름이 바뀌어도 수정 범위가 줄어든다.
- 다중 상속의 메서드 탐색 순서를 따를 수 있다.
- 코드의 의도가 명확하다.

> [!TIP]
> `super()`는 단순히 “부모 객체”를 의미하는 것이 아니라, 현재 클래스의 메서드 탐색 순서에서 다음 클래스의 기능을 호출하도록 돕는다.

---

# 6. 자식 생성자를 생략한 경우

자식 클래스가 `__init__()`을 직접 정의하지 않으면 부모 생성자를 사용할 수 있다.

## 6-1. 강사님 코드

```python
class Student3(Person2):
    def test(self):
        print("테스트")


student = Student3()
```

`Student3`에는 `__init__()`이 없으므로 부모 `Person2.__init__()`이 실행된다.

## 6-2. 출력 결과

```text
Person2 __init__ 실행
```

## 6-3. 개념적으로 이해하기

다음 구조와 비슷하게 동작한다.

```python
class Student3(Person2):
    def __init__(self):
        super().__init__()
```

다만 Python이 실제로 위 코드를 파일에 작성하는 것은 아니다. 자식 생성자가 없으므로 메서드 탐색 과정에서 부모 생성자를 찾아 호출하는 것이다.

> [!TIP]
> 부모 초기화만 그대로 사용할 경우 자식 생성자를 생략할 수 있다.

---

# 7. 부모 생성자에 필수 인자가 있는 경우

부모 생성자가 반드시 값을 받아야 한다면 자식 클래스도 그 값을 전달해야 한다.

## 7-1. 내 코드

```python
class Person3:
    def __init__(self, text):
        print("Person3 __init__ 실행")
        self.hello = "방가"
        self.text = text


class Student4(Person3):
    def __init__(self):
        super().__init__(None)
```

## 7-2. 강사님 코드

```python
class Person3:
    def __init__(self, text):
        print("Person3 __init__ 실행")
        self.hello = "방가"
        self.text = text


class Student4(Person3):
    def __init__(self):
        super().__init__(None)
```

원본에서는 매개변수 이름으로 `str`을 사용했지만, `str`은 Python 내장 자료형 이름이므로 `text`처럼 다른 이름을 사용하는 것이 좋다.

## 7-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `text` | 부모 객체 초기화에 필요한 값을 전달받기 위해 |
| `super().__init__(None)` | 부모 생성자의 필수 매개변수에 값을 전달하기 위해 |
| `self.text` | 부모 클래스가 관리하는 인스턴스 속성으로 저장하기 위해 |

## 7-4. 실행

```python
student = Student4()

print(student.hello)
print(student.text)
```

## 7-5. 출력 결과

```text
Person3 __init__ 실행
방가
None
```

## 7-6. 더 자연스러운 구조

자식 생성자도 값을 전달받도록 작성할 수 있다.

```python
class Student4(Person3):
    def __init__(self, text):
        super().__init__(text)
```

```python
student = Student4("학생 정보")
print(student.text)
```

```text
학생 정보
```

> [!WARNING]
> 부모 생성자에 필수 인자가 있는데 `super().__init__()`만 호출하면 `TypeError`가 발생한다.

---

# 8. 메서드 오버라이딩

오버라이딩은 부모 클래스의 메서드를 자식 클래스에서 같은 이름으로 다시 정의하는 것이다.

## 8-1. 내 코드

```python
class Person5:
    def hi(self):
        print("안녕하시오")


class Student5(Person5):
    def hi(self):
        print("야호")
```

## 8-2. 강사님 코드

```python
class Person5:
    def hi(self):
        print("안녕하시오")


class Student5(Person5):
    def hi(self):
        print("야호")
```

## 8-3. 실행

```python
student = Student5()
student.hi()
```

## 8-4. 출력 결과

```text
야호
```

## 8-5. 동작 과정

```text
student.hi() 호출
    ↓
Student5에서 hi() 검색
    ↓
Student5.hi() 발견
    ↓
자식 메서드 실행
    ↓
부모 Person5.hi()는 자동 실행되지 않음
```

## 8-6. 왜 사용할까?

부모가 제공하는 공통 메서드 이름은 유지하면서 자식 객체마다 다른 동작을 만들기 위해 사용한다.

```text
부모: attack()
자식 Lux: attack()
자식 다른 챔피언: attack()
```

호출하는 쪽은 모두 `attack()`을 사용하지만 실제 동작은 객체마다 다를 수 있다.

> [!IMPORTANT]
> 자식 클래스에 같은 이름의 메서드가 있으면 부모 메서드보다 자식 메서드가 먼저 실행된다.

---

# 9. 부모 메서드를 유지하면서 기능 추가

오버라이딩할 때 부모 기능을 완전히 없애지 않고 추가 기능을 이어서 실행할 수 있다.

## 9-1. 내 코드

```python
class Champ:
    def attack(self):
        print("기본 공격")


class Lux(Champ):
    def attack(self):
        super().attack()
        print("데마시~~~~~~아!!!")
```

## 9-2. 강사님 코드

```python
class Champ:
    def attack(self):
        print("기본 공격")


class Lux(Champ):
    def attack(self):
        super().attack()
        print("데마시~~~~~~아!!!")
```

## 9-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `Champ.attack()` | 모든 챔피언의 기본 공격을 정의하기 위해 |
| `Lux.attack()` | 럭스만의 공격 동작으로 재정의하기 위해 |
| `super().attack()` | 부모의 기본 공격도 유지하기 위해 |
| `print("데마시...")` | 럭스만의 추가 공격을 실행하기 위해 |

## 9-4. 실행

```python
lux = Lux()
lux.attack()
```

## 9-5. 출력 결과

```text
기본 공격
데마시~~~~~~아!!!
```

## 9-6. 동작 과정

```text
lux.attack()
    ↓
Lux.attack() 실행
    ↓
super().attack()
    ↓
Champ.attack() 실행
    ↓
기본 공격 출력
    ↓
Lux.attack()으로 복귀
    ↓
럭스 추가 공격 출력
```

> [!TIP]
> 부모 동작을 유지하면서 자식 기능을 추가하려면 오버라이딩한 메서드 안에서 `super().메서드()`를 호출한다.

---

# 10. 다형성이란?

다형성은 **같은 메서드 호출이 객체의 실제 클래스에 따라 다르게 동작하는 성질**이다.

```text
같은 호출
attack()
    ↓
Lux 객체 → Lux.attack()
Jax 객체 → Jax가 상속받은 Champ.attack()
```

## 10-1. 수업 코드

```python
class Champ:
    def attack(self):
        print("기본 공격")


class Lux(Champ):
    def attack(self):
        super().attack()
        print("데마시~~~~~~아!!!")


class Jax(Champ):
    def defence(self):
        print("절대 지켜")
```

```python
champions = [
    Lux(),
    Jax(),
]

for champion in champions:
    champion.attack()
```

## 10-2. 출력 결과

```text
기본 공격
데마시~~~~~~아!!!
기본 공격
```

## 10-3. 객체마다 실행되는 메서드

| 객체 | 호출 | 실행 메서드 |
| --- | --- | --- |
| `Lux()` | `attack()` | `Lux.attack()` |
| `Jax()` | `attack()` | 부모 `Champ.attack()` |

`Lux`는 `attack()`을 오버라이딩했고, `Jax`는 오버라이딩하지 않았기 때문에 부모 메서드를 사용한다.

## 10-4. 왜 유용할까?

호출하는 코드는 각 객체의 정확한 클래스를 검사할 필요가 없다.

좋지 않은 방식:

```python
for champion in champions:
    if isinstance(champion, Lux):
        champion.attack()
    elif isinstance(champion, Jax):
        champion.attack()
```

다형성을 활용한 방식:

```python
for champion in champions:
    champion.attack()
```

> [!IMPORTANT]
> 다형성의 핵심은 “객체 종류를 검사해서 분기하는 것”이 아니라, 같은 메서드를 호출하고 각 객체가 자신의 방식으로 동작하게 만드는 것이다.

---

# 11. 자동차 상속 실습

## 11-1. 문제

부모 `Car` 클래스는 다음 기능을 가진다.

```text
start()
→ 시동을 켭니다

accel()
→ 속도를 높입니다
```

자식 클래스:

- `Lambo`: 시동과 가속 기능을 확장
- `Tico`: 가속 기능만 확장

## 11-2. 내 코드

```python
class Car:
    def start(self):
        print("시동을 켭니다")

    def accel(self):
        print("속도를 높입니다")


class Lambo(Car):
    def start(self):
        super().start()
        print("Lambo : 바라랑~")

    def accel(self):
        super().accel()
        print("Lambo : 스아앙~")


class Tico(Car):
    def accel(self):
        super().accel()
        print("Tico : 덜덜덜덜")
```

강사님 코드에는 문제 설명까지만 있고, 내 코드에서 실제 구현을 완성했다.

## 11-3. 실행

```python
cars = [
    Lambo(),
    Tico(),
]

for car in cars:
    car.start()
    car.accel()
```

## 11-4. 출력 결과

```text
시동을 켭니다
Lambo : 바라랑~
속도를 높입니다
Lambo : 스아앙~
시동을 켭니다
속도를 높입니다
Tico : 덜덜덜덜
```

## 11-5. 객체별 동작

| 객체 | `start()` | `accel()` |
| --- | --- | --- |
| `Lambo` | 부모 기능 + 람보르기니 기능 | 부모 기능 + 람보르기니 기능 |
| `Tico` | 부모 기능 그대로 사용 | 부모 기능 + 티코 기능 |

## 11-6. 객체 관계

```text
Car
├─ start()
└─ accel()

Lambo(Car)
├─ start() 오버라이딩
└─ accel() 오버라이딩

Tico(Car)
├─ start() 상속
└─ accel() 오버라이딩
```

## 11-7. 개선된 코드

클래스 이름은 실제 이름과 역할이 더 명확하게 드러나게 작성한다.

```python
class Car:
    def start(self):
        print("시동을 켭니다.")

    def accelerate(self):
        print("속도를 높입니다.")


class Lamborghini(Car):
    def start(self):
        super().start()
        print("바라랑~")

    def accelerate(self):
        super().accelerate()
        print("스아앙~")


class Tico(Car):
    def accelerate(self):
        super().accelerate()
        print("덜덜덜덜")
```

### 개선된 점

- `accel`을 `accelerate`로 작성해 의미를 명확히 했다.
- 출력 문장과 클래스 이름을 일관되게 정리했다.
- 공통 동작은 부모 클래스에 유지했다.
- 차량별 차이만 자식 클래스에서 구현했다.

---

# 12. 추상 클래스

추상 클래스는 직접 완성된 객체를 만드는 목적보다, 자식 클래스가 따라야 할 공통 규칙을 정의하는 클래스다.

```text
추상 클래스
    ↓
필수 메서드 이름과 구조 정의
    ↓
자식 클래스에서 반드시 구현
```

## 12-1. 수업 코드

```python
from abc import ABCMeta, abstractmethod


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass
```

## 12-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `ABCMeta` | 클래스를 추상 클래스 형태로 만들기 위해 |
| `metaclass=ABCMeta` | 추상 메서드 규칙을 적용하기 위해 |
| `@abstractmethod` | 자식이 반드시 구현해야 하는 메서드를 표시하기 위해 |
| `pass` | 부모에서 구체적인 동작을 작성하지 않고 구조만 정의하기 위해 |

> [!TIP]
> 현대 Python에서는 `ABC`를 상속하는 방식도 자주 사용한다.

```python
from abc import ABC, abstractmethod


class StudentBase(ABC):
    @abstractmethod
    def study(self):
        pass
```

---

# 13. 추상 메서드 구현

추상 클래스를 상속한 자식은 모든 추상 메서드를 구현해야 한다.

## 13-1. 내 코드

```python
class Student(StudentBase):
    def study(self):
        print("공부하기")

    def go_to_school(self):
        print("학교가기")
```

## 13-2. 강사님 코드

```python
class Student(StudentBase):
    def study(self):
        print("공부하기")

    def go_to_school(self):
        print("학교가기")
```

## 13-3. 실행

```python
student = Student()

student.study()
student.go_to_school()
```

## 13-4. 출력 결과

```text
공부하기
학교가기
```

## 13-5. 동작 과정

```text
StudentBase
├─ study() 구현 요구
└─ go_to_school() 구현 요구

Student
├─ study() 구현 완료
└─ go_to_school() 구현 완료
    ↓
Student 객체 생성 가능
```

> [!IMPORTANT]
> 추상 메서드 중 하나라도 구현하지 않으면 자식 클래스의 객체를 생성할 수 없다.

---

# 14. 추상 메서드를 구현하지 않은 경우

## 14-1. 잘못된 코드

```python
class Student(StudentBase):
    def study(self):
        print("공부하기")
```

`go_to_school()`을 구현하지 않았다.

## 14-2. 객체 생성

```python
student = Student()
```

## 14-3. 발생 결과

```text
TypeError: Can't instantiate abstract class Student
with abstract method go_to_school
```

## 14-4. 오류 원인

`StudentBase`가 `go_to_school()` 구현을 필수로 지정했지만 자식 클래스가 구현하지 않았기 때문이다.

## 14-5. 올바른 코드

```python
class Student(StudentBase):
    def study(self):
        print("공부하기")

    def go_to_school(self):
        print("학교가기")
```

---

# 15. 추상 클래스는 직접 생성할 수 있을까?

다음 코드는 실행할 수 없다.

```python
student_base = StudentBase()
```

`StudentBase`에는 구현되지 않은 추상 메서드가 있으므로 객체 생성이 제한된다.

```text
추상 클래스
→ 규칙 정의 목적

구현 클래스
→ 실제 객체 생성 목적
```

> [!WARNING]
> 추상 클래스는 자식 클래스의 설계 규칙을 제공하는 목적이므로, 일반적으로 직접 인스턴스를 생성하지 않는다.

---

# 16. 추상 클래스와 일반 부모 클래스 비교

| 구분 | 일반 부모 클래스 | 추상 클래스 |
| --- | --- | --- |
| 객체 생성 | 가능 | 추상 메서드가 있으면 불가능 |
| 메서드 구현 강제 | 없음 | `@abstractmethod`로 가능 |
| 주요 목적 | 공통 기능 재사용 | 공통 규칙과 인터페이스 정의 |
| 자식 구현 누락 | 실행 전 강제되지 않음 | 객체 생성 시 오류 |
| 예시 | `Car`, `Person` | `StudentBase`, `PaymentBase` |

---

# 17. 추상 클래스와 다형성 연결

추상 클래스는 여러 자식 클래스가 같은 메서드 이름을 반드시 가지게 만들 수 있다.

```python
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
```

```python
class CardPayment(Payment):
    def pay(self, amount):
        print(f"카드로 {amount:,}원 결제")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"현금으로 {amount:,}원 결제")
```

## 17-1. 실행

```python
payments = [
    CardPayment(),
    CashPayment(),
]

for payment in payments:
    payment.pay(10000)
```

## 17-2. 출력 결과

```text
카드로 10,000원 결제
현금으로 10,000원 결제
```

같은 `pay()` 호출이 객체마다 다르게 동작한다.

```text
Payment 추상 클래스
└─ pay() 구현 강제

CardPayment
└─ 카드 결제 방식 구현

CashPayment
└─ 현금 결제 방식 구현
```

---

# 18. 상속을 사용할 때의 기준

상속은 중복을 줄일 수 있지만 항상 정답은 아니다.

## 18-1. 상속이 적합한 경우

- 자식이 부모의 한 종류인 관계
- 공통 메서드와 속성이 명확함
- 자식 클래스가 부모 인터페이스를 자연스럽게 따름
- 같은 메서드로 여러 객체를 처리할 필요가 있음

## 18-2. 상속이 부적합한 경우

- 단순히 코드 몇 줄을 재사용하려는 목적
- 부모와 자식의 의미 관계가 자연스럽지 않음
- 부모 변경이 모든 자식에 큰 영향을 줌
- 기능을 포함하는 관계가 더 자연스러움

예:

```text
Car has an Engine
자동차는 엔진을 가진다
```

이 관계는 상속보다 포함이 자연스럽다.

```python
class Engine:
    def start(self):
        print("엔진 시작")


class Car:
    def __init__(self):
        self.engine = Engine()
```

---

# 19. 메서드 탐색 순서

메서드를 호출하면 Python은 현재 클래스부터 부모 방향으로 메서드를 찾는다.

```text
Lux.attack()
    ↓
Lux에서 attack() 검색
    ↓
있음 → Lux.attack() 실행
```

```text
Jax.attack()
    ↓
Jax에서 attack() 검색
    ↓
없음
    ↓
Champ에서 attack() 검색
    ↓
있음 → Champ.attack() 실행
```

이 탐색 순서를 MRO(Method Resolution Order)라고 한다.

간단히 확인할 수 있다.

```python
print(Lux.mro())
```

출력 형태:

```text
[Lux, Champ, object]
```

> [!TIP]
> 단일 상속에서는 현재 클래스 → 부모 클래스 → `object` 순서로 이해하면 충분하다.

---

# 20. 모든 클래스의 최상위 부모 `object`

Python의 모든 클래스는 기본적으로 `object`를 상속한다.

```python
class Person:
    pass
```

개념적으로 다음과 비슷하다.

```python
class Person(object):
    pass
```

따라서 사용자 정의 클래스도 `__str__()`, `__repr__()` 같은 기본 특수 메서드 구조를 사용할 수 있다.

---

# 21. 기존 코드에서 개선 코드로 바꾼 이유

## 21-1. 부모 생성자 인자 이름 개선

기존:

```python
def __init__(self, str):
    self.str = str
```

문제:

- `str` 내장 자료형 이름을 가린다.
- 값의 의미가 불분명하다.

개선:

```python
def __init__(self, text):
    self.text = text
```

## 21-2. 자식 생성자에 값 전달

기존:

```python
super().__init__(None)
```

문제:

- `None`을 넣는 이유가 명확하지 않다.
- 실제 값이 필요한 구조라면 잘못된 상태가 될 수 있다.

개선:

```python
def __init__(self, text):
    super().__init__(text)
```

## 21-3. 메서드 이름 개선

기존:

```python
def accel(self):
    pass
```

개선:

```python
def accelerate(self):
    pass
```

더 긴 이름이지만 기능의 의미가 명확하다.

> [!TIP]
> 개선 코드는 단순히 짧거나 어려운 코드가 아니라, **역할과 데이터의 의미가 분명하고 잘못된 상태를 줄이는 코드**다.

---

# 22. 대표 오류로 이해하기

## 22-1. 부모 생성자를 호출하지 않은 경우

### 잘못된 코드

```python
class Person:
    def __init__(self):
        self.name = "홍길동"


class Student(Person):
    def __init__(self):
        self.school = "휴먼"


student = Student()
print(student.name)
```

### 발생 결과

```text
AttributeError
```

### 오류 원인

자식 `Student.__init__()`이 실행되었지만 부모 `Person.__init__()`을 호출하지 않아 `name` 속성이 생성되지 않았다.

### 올바른 코드

```python
class Student(Person):
    def __init__(self):
        super().__init__()
        self.school = "휴먼"
```

---

## 22-2. 부모 생성자 필수 인자를 누락한 경우

```python
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self):
        super().__init__()
```

```text
TypeError
```

수정:

```python
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
```

---

## 22-3. 추상 메서드를 일부만 구현한 경우

```python
class Student(StudentBase):
    def study(self):
        print("공부하기")
```

`go_to_school()`이 누락되어 객체를 생성할 수 없다.

---

## 22-4. 오버라이딩하면서 부모 기능을 잃은 경우

```python
class Lux(Champ):
    def attack(self):
        print("특수 공격")
```

이 코드는 부모의 기본 공격을 실행하지 않는다.

부모 기능도 필요하다면:

```python
class Lux(Champ):
    def attack(self):
        super().attack()
        print("특수 공격")
```

---

# 23. 클래스 관계 구조

```text
Person
└─ Student
   ├─ Person.greeting() 상속
   └─ Student.study() 추가
```

```text
Car
├─ Lamborghini
│  ├─ start() 오버라이딩
│  └─ accelerate() 오버라이딩
│
└─ Tico
   ├─ start() 상속
   └─ accelerate() 오버라이딩
```

```text
StudentBase (추상 클래스)
├─ study() 구현 강제
└─ go_to_school() 구현 강제
    ↓
Student
├─ study() 구현
└─ go_to_school() 구현
```

---

# 24. 자주 하는 실수

## 24-1. 상속 관계가 자연스럽지 않은데 상속 사용

코드 재사용만을 위해 의미 없는 부모·자식 관계를 만들면 구조가 복잡해진다.

## 24-2. 자식 생성자에서 부모 생성자 호출 누락

부모 속성이 초기화되지 않을 수 있다.

## 24-3. 부모 생성자 인자 누락

필수 인자를 전달하지 않으면 `TypeError`가 발생한다.

## 24-4. 오버라이딩과 새 메서드 정의 혼동

부모와 같은 이름으로 다시 정의해야 오버라이딩이다.

## 24-5. 부모 기능도 필요하지만 `super()` 호출 누락

자식 메서드만 실행되고 부모 동작은 사라진다.

## 24-6. 모든 자식 객체가 같은 메서드를 가진다고 가정

공통 부모나 추상 클래스가 보장하지 않으면 일부 객체에서 `AttributeError`가 발생할 수 있다.

## 24-7. 추상 메서드 구현 누락

객체 생성 시 `TypeError`가 발생한다.

## 24-8. 내장 이름을 매개변수로 사용

`str`, `list`, `dict` 같은 이름을 변수로 사용하면 내장 기능을 가릴 수 있다.

## 24-9. 상속 계층을 지나치게 깊게 설계

부모 기능을 추적하기 어려워지고 변경 영향 범위가 커진다.

---

# 25. 면접·복습 포인트

## Q1. 상속이란 무엇인가요?

기존 클래스의 속성과 메서드를 새로운 클래스가 이어받아 재사용하거나 확장하는 기능이다.

## Q2. 부모 클래스와 자식 클래스의 차이는 무엇인가요?

부모 클래스는 공통 기능을 제공하고, 자식 클래스는 부모 기능을 이어받아 추가하거나 변경한다.

## Q3. `super()`는 왜 사용하나요?

부모 생성자나 부모 메서드를 현재 상속 구조에 맞게 호출하기 위해 사용한다.

## Q4. 자식 클래스가 `__init__()`을 정의하면 부모 생성자도 자동 실행되나요?

아니다. 부모 초기화가 필요하면 `super().__init__()`을 직접 호출해야 한다.

## Q5. 오버라이딩이란 무엇인가요?

부모 클래스의 메서드를 자식 클래스에서 같은 이름으로 다시 정의하는 것이다.

## Q6. 다형성이란 무엇인가요?

같은 메서드 호출이 객체의 실제 클래스에 따라 서로 다르게 동작하는 성질이다.

## Q7. 추상 클래스는 왜 사용하나요?

여러 자식 클래스가 반드시 구현해야 할 공통 메서드 규칙을 정하기 위해 사용한다.

## Q8. 추상 메서드를 구현하지 않으면 어떻게 되나요?

해당 자식 클래스의 인스턴스를 생성할 수 없고 `TypeError`가 발생한다.

## Q9. 상속과 포함 관계는 어떻게 구분하나요?

“자식은 부모의 한 종류다”가 자연스러우면 상속, “객체가 다른 객체를 가진다”가 자연스러우면 포함 관계를 고려한다.

## Q10. 오버라이딩할 때 부모 메서드도 실행하려면 어떻게 하나요?

자식 메서드 안에서 `super().메서드명()`을 호출한다.

---

# 26. 핵심 요약

```text
상속
→ 부모의 공통 기능을 자식이 이어받음

부모 클래스
→ 공통 속성과 메서드 제공

자식 클래스
→ 부모 기능을 재사용·추가·변경

super()
→ 부모 생성자 또는 부모 메서드 호출

오버라이딩
→ 부모 메서드를 자식에서 같은 이름으로 재정의

다형성
→ 같은 메서드 호출이 객체마다 다르게 동작

추상 클래스
→ 자식 클래스가 따라야 할 규칙 정의

@abstractmethod
→ 자식 클래스의 메서드 구현 강제
```

---

# 27. 최종 체크리스트

- [ ] 부모와 자식의 관계가 의미상 자연스러운가?
- [ ] 자식 클래스가 부모 기능을 실제로 재사용하는가?
- [ ] 자식 생성자에서 부모 초기화가 필요한지 확인했는가?
- [ ] 부모 생성자의 필수 인자를 정확히 전달했는가?
- [ ] 오버라이딩한 메서드에서 부모 기능도 필요한지 확인했는가?
- [ ] 같은 메서드로 여러 객체를 처리할 수 있는가?
- [ ] 추상 클래스의 모든 추상 메서드를 구현했는가?
- [ ] `str`, `list`, `dict` 같은 내장 이름을 변수로 사용하지 않았는가?
- [ ] 상속보다 포함 관계가 더 자연스럽지는 않은가?
- [ ] 상속 계층이 지나치게 깊어지지 않았는가?

---

# 마무리

상속의 목적은 단순히 코드를 짧게 만드는 것이 아니다.

```text
공통 기능을 부모에 모으고
    ↓
자식 클래스는 필요한 차이만 구현하고
    ↓
같은 메서드 이름으로 여러 객체를 처리하며
    ↓
추상 클래스로 필수 규칙을 보장하는 것
```

이 흐름을 이해하면 객체지향 프로그램에서 여러 클래스가 어떤 관계로 설계되고 동작하는지 더 쉽게 파악할 수 있다.

# V3 동작 백과 보강 — 메서드를 찾고 재정의된 코드를 고르는 과정

자식 객체에서 메서드를 호출하면 Python은 해당 클래스부터 MRO(Method Resolution Order)를 따라 부모 클래스로 올라가며 이름을 찾는다. 자식이 같은 이름을 정의하면 그 메서드가 선택되는 오버라이딩이 일어난다. `super()`는 MRO의 다음 구현을 호출한다.

```python
class Animal:
    def sound(self): return "소리"
class Dog(Animal):
    def sound(self): return "멍멍"

for animal in [Animal(), Dog()]:
    print(animal.sound())
```

```text
소리
멍멍
```

호출 코드는 같지만 실제 객체의 클래스에 따라 실행 메서드가 달라지는 것이 다형성이다. 부모 초기화가 필요한데 호출하지 않으면 필수 속성이 없어 `AttributeError`가 날 수 있다.

**원본 연결:** 내 코드 `workspace_python/13_상속.py`, 강사님 코드 `workspace_python/_13_상속.py`의 상속, 오버라이딩, `super`, 추상화 예제를 기반으로 한다.
