# Python 클래스

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `12_Python_클래스.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `02_Python_변수와_자료형_연산자.md`, `07_Python_딕셔너리와_집합.md`, `11_Python_함수.md` |
| 다음 학습 | Python 예외 처리 및 종합 실습 |
| 원본 기준 | `workspace_python/12_class.py`, `workspace_teacher/workspace_python/_12_class.py` |
| 핵심 범위 | 클래스와 인스턴스, `__init__`, `self`, 인스턴스 속성, 인스턴스 메서드, 객체별 상태, 동적 속성, 비공개 속성과 메서드, 캡슐화 |
| 보충 범위 | 클래스 이름 규칙, 객체 생성 과정, 네임 맹글링, 속성 검증, 클래스 속성, 상속, `__str__`, 데이터 클래스, 객체 설계 원칙 |
| Quiz 처리 | 원본 실습은 본문에서 분석하며, 추가 문제와 상세 풀이 문서는 최종 Quiz 단계에서 별도 제작 |

> 이 문서는 내 코드의 `12_class.py`와 강사님 코드의 `_12_class.py`를 직접 비교해 작성했습니다. 두 파일은 `Person`, `Person2`, `Person3` 클래스를 통해 객체 생성, `__init__`, `self`, 인스턴스별 속성, 동적 속성 추가, 이중 밑줄을 이용한 비공개 속성과 메서드, 캡슐화까지 같은 흐름을 공유합니다. 내 코드는 메모리와 객체 독립성에 대한 설명이 더 많고, 강사님 코드는 핵심 동작을 간결하게 보여 줍니다.

---

# 학습 목표

- 클래스가 객체를 만들기 위한 설계도임을 설명할 수 있다.
- 인스턴스가 클래스로부터 생성된 실제 객체임을 이해한다.
- 클래스 이름을 일반적으로 PascalCase로 작성한다는 점을 안다.
- 객체 생성 시 `__init__()`가 자동으로 호출된다는 점을 이해한다.
- 인스턴스 메서드의 첫 매개변수로 `self`가 필요한 이유를 설명할 수 있다.
- `self.속성`이 각 인스턴스에 저장되는 상태임을 이해한다.
- 같은 클래스로 만든 인스턴스가 서로 다른 값을 가질 수 있음을 설명할 수 있다.
- 인스턴스 메서드끼리 `self`를 통해 호출할 수 있다.
- 객체에 동적으로 속성을 추가할 수 있지만 설계상 주의가 필요함을 안다.
- 이중 밑줄 속성과 메서드가 이름 변환을 통해 외부 접근을 어렵게 한다는 점을 이해한다.
- 캡슐화와 은닉화의 목적을 설명할 수 있다.
- 직접 속성에 접근하는 방식과 메서드를 통한 상태 변경의 차이를 구분할 수 있다.
- 내 코드와 강사님 코드의 구조 및 동작 차이를 비교할 수 있다.
- 클래스 속성, 상속, 특수 메서드의 기초 개념을 이해한다.

---


# 1. 원본 코드

## 1.1 내 코드

```python

# class명은 대부분 대문자로 시작 함
class Person:
    # __init__ 은 클래스가 생성될 때 자동으로 먼저 실행 되는 메소드
    def __init__(self) : 
        print(1)
        self.hello = '안녕하세요'

    def greeting(self): # class안에 def일 때 첫 번째 인자는 self가 필수
        # print('Hello Class')
        print(self.hello)

    def hello(self):
        self.greeting()

print(0)
james = Person()
print(2)
james.greeting()
# james.hello()

print(james)
print(type(james))

class Person2:
    def __init__(self, name, age) : 
        print('__init__실행')
        self.hello = '안녕하세요'
        self.name = name
        self.age = age

    def greeting(self): 
        print(f'{self.hello}! 저는 {self.name}이고 나이는 {self.age}입니다')

a = Person2('이름', 20) # Person2 class는 heap영역에 있고 a는 주소값을 가지고 있음
a.greeting()

print(a.hello) # 전달 인자가 없더라도, class내 존재하기 때문에 사용 가능
print(a.name)
print(a.age)

b = Person2('다른이름', 30) # a와는 다른 Person2를 바라보고 있는 것
b.greeting()
print(b.name)

b.addr = '천안' # 없는 항목을 추가해서 임시로 사용할 수도 있음
print(b.addr)
# print(a.addr) # a 에는 당연하게 값이 없음. a와 b는 다른 영역이기 때문

b.__init__(1,2) # 실행 됨, 다만 자동으로 실행되기 때문에 별도 실행 필요 없음

class Person3:
    def __init__(self, money) : 
        self.hello = '안녕하세요'
        self.__money = money
        self.___money = money

    def pay(self, price) :
        self.__money -= price
        print('남은 돈 : ', self.__money)
        self.__study()

    def __study(self) :
        print('히히 나 혼자 레벨 업')

a = Person3(10000)
a.pay(3000)

print(a.hello)
# print(a.money) # __속성을 하면 비공개로 전환되어 속성이 없다고 에러가 출력됨
a.__money = 9999999 # 비공개여서 없다고 뜨지만, 추가되는 것
a.pay(3000)
# a.__study() # AttributeError: 'Person3' object has no attribute '__study'

# __붙은 변수나 함수는 내부에서는 접근 가능하나, 외부에서는 노출되지 않는다
# 캡슐화 뜨는 은닉화
# print(a.___money) # 이미 __가 있기 때문에 뒤에 더 붙인다고 해도 오류 남 (__ + _money)
```

## 1.2 강사님 코드

```python

class Person :

    # __init__
    # 클래스가 생성될 때
    # 자동으로 먼저 실행되는 메소드
    def __init__(self):
        print(1)
        self.hello = '안녕하세요'

    def greeting(self):
        # print('Hello Class')
        print(self.hello)

    def hello(self):
        self.greeting()

print(0)
james = Person()
print(2)
james.greeting()

print(james)
print(type(james))


class Person2 :
    def __init__(self, name, age):
        print('__init__ 실행')
        self.hello = '안녕하세요'
        self.name = name
        self.age = age

    def greeting(self):
        print(f'{self.hello}! 저는 {self.name}이고 나이는 {self.age}입니다')

a = Person2('이름', 20)
a.greeting()
print( a.hello )
print( a.name )

b = Person2('다른이름', 30)
b.greeting()
print( b.name )

b.addr = '천안'
print(b.addr)

# print(a.addr)
b.__init__(1,2) # 실행 됨


class Person3 :
    def __init__(self, money):
        self.hello = '안녕하세요'
        self.__money = money
        self.___money = money

    def pay(self, price):
        self.__money -= price
        print('남은 돈 : ', self.__money)
        self.__study()

    def __study(self):
        print('히히 나 혼자 레벨 업')

a = Person3(10000)
a.pay(3000)
print(a.hello)
# print(a.__money)
a.__money = 99999999 # 이건 변수 추가
a.pay(3000)
# a.__study()

# __붙은 변수나 함수는
# 내부에서는 접근 가능하고
# 외부로 노출되지 않는다
# 캡슐화, 은닉화
# print(a.___money) # __ + _money
```

---


# 2. 클래스란?

클래스는 데이터와 기능을 하나의 단위로 묶어 객체를 만들기 위한 설계도입니다.

```text
클래스
→ 객체 생성
→ 인스턴스
```

예:

```python
class Person:
    pass

james = Person()
```

`Person`은 클래스이고 `james`는 `Person` 클래스로 만든 인스턴스입니다.

---

# 3. 클래스 이름 규칙

Python 클래스 이름은 일반적으로 PascalCase를 사용합니다.

```python
class Person:
    pass

class BankAccount:
    pass
```

단어의 첫 글자를 대문자로 작성합니다.

---

# 4. 인스턴스 생성

```python
james = Person()
```

클래스 이름 뒤에 괄호를 붙여 호출하면 새 인스턴스가 생성됩니다.

각 인스턴스는 고유한 객체입니다.

---

# 5. `__init__()`

```python
class Person:
    def __init__(self):
        print("초기화")
```

`__init__()`는 인스턴스가 생성된 직후 자동으로 호출되는 초기화 메서드입니다.

---

# 6. 객체 생성 순서

원본:

```python
print(0)
james = Person()
print(2)
```

출력 흐름:

```text
0
1
2
```

`Person()`을 실행하는 순간 `__init__()` 내부의 `print(1)`이 먼저 실행됩니다.

---

# 7. `self`

```python
class Person:
    def greeting(self):
        print("Hello")
```

`self`는 현재 메서드를 호출한 인스턴스 자신을 가리킵니다.

```python
james.greeting()
```

호출 과정은 개념적으로 다음과 비슷합니다.

```python
Person.greeting(james)
```

---

# 8. 인스턴스 메서드

클래스 내부에 정의되고 첫 매개변수로 `self`를 받는 함수입니다.

```python
class Person:
    def greeting(self):
        print("안녕하세요")
```

---

# 9. 인스턴스 속성

```python
class Person:
    def __init__(self):
        self.hello = "안녕하세요"
```

`self.hello`는 각 인스턴스에 저장되는 속성입니다.

---

# 10. 속성 사용

```python
class Person:
    def greeting(self):
        print(self.hello)
```

인스턴스 메서드에서는 `self.속성명`으로 현재 객체의 상태를 사용합니다.

---

# 11. 메서드에서 다른 메서드 호출

원본:

```python
def hello(self):
    self.greeting()
```

같은 인스턴스의 다른 메서드는 `self.메서드명()`으로 호출합니다.

---

# 12. 클래스와 인스턴스 타입

```python
print(james)
print(type(james))
```

`type(james)`는 `james`가 `Person` 클래스의 인스턴스임을 보여 줍니다.

---

# 13. 생성자 인자

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

객체 생성 시 필요한 값을 전달할 수 있습니다.

```python
person = Person("홍길동", 20)
```

---

# 14. 매개변수와 속성

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

오른쪽 `name`, `age`는 매개변수이고, 왼쪽 `self.name`, `self.age`는 인스턴스 속성입니다.

---

# 15. 객체별 상태

```python
a = Person2("이름", 20)
b = Person2("다른이름", 30)
```

`a`와 `b`는 같은 클래스로 만들었지만 서로 다른 속성값을 가집니다.

```text
a.name → 이름
b.name → 다른이름
```

---

# 16. 인스턴스는 독립적이다

```python
b.addr = "천안"
```

`b`에 추가한 `addr` 속성은 `a`에 자동으로 생기지 않습니다.

```python
print(a.addr)
```

`a`에는 해당 속성이 없으므로 `AttributeError`가 발생합니다.

---

# 17. 동적 속성 추가

Python은 실행 중 인스턴스에 새 속성을 추가할 수 있습니다.

```python
person.address = "천안"
```

하지만 인스턴스마다 속성 구조가 달라질 수 있어 유지보수성이 떨어질 수 있습니다.

가능하면 필요한 속성은 `__init__()`에서 명시합니다.

---

# 18. 권장 초기화 방식

```python
class Person:
    def __init__(
        self,
        name: str,
        age: int,
        address: str | None = None,
    ):
        self.name = name
        self.age = age
        self.address = address
```

모든 인스턴스가 같은 속성 구조를 갖게 됩니다.

---

# 19. `__init__()` 직접 호출

원본:

```python
b.__init__(1, 2)
```

문법적으로 실행할 수 있지만 일반적으로 직접 호출하지 않습니다.

`__init__()`는 객체 생성 시 자동 실행되는 초기화 메서드입니다. 이미 존재하는 객체를 다시 초기화하면 기존 상태가 예상치 않게 바뀔 수 있습니다.

---

# 20. 상태와 행동 묶기

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"안녕하세요. 저는 {self.name}입니다.")
```

클래스는 데이터인 속성과 동작인 메서드를 함께 묶습니다.

---

# 21. 캡슐화

캡슐화는 객체의 상태와 동작을 하나의 클래스 안에 묶고, 상태 변경 규칙을 메서드로 관리하는 설계 방식입니다.

```text
속성을 외부에서 직접 수정
→ 잘못된 상태 가능

메서드를 통해 수정
→ 검증과 규칙 적용 가능
```

---

# 22. 비공개 속성

원본:

```python
self.__money = money
```

이중 밑줄로 시작하는 속성은 클래스 외부에서 직접 접근하기 어렵게 이름이 변환됩니다.

---

# 23. 이름 변환(Name Mangling)

```python
self.__money
```

내부적으로 대략 다음과 같은 이름으로 변환됩니다.

```text
_Person3__money
```

완전한 보안 기능이라기보다 실수로 외부에서 접근하거나 하위 클래스와 이름이 충돌하는 것을 줄이는 장치입니다.

---

# 24. 비공개 메서드

```python
def __study(self):
    print("히히 나 혼자 레벨 업")
```

클래스 내부에서는 호출할 수 있습니다.

```python
self.__study()
```

외부에서 다음처럼 호출하면 일반적으로 `AttributeError`가 발생합니다.

```python
person.__study()
```

---

# 25. 외부에서 같은 이름을 대입한 경우

원본:

```python
a.__money = 9999999
```

이 코드는 기존 비공개 속성을 바꾸는 것이 아니라 외부에 `__money`라는 별도 속성을 새로 추가합니다.

내부의 `self.__money`는 이름 변환된 다른 속성입니다.

---

# 26. `pay()` 메서드

```python
def pay(self, price):
    self.__money -= price
    print("남은 돈:", self.__money)
```

외부에서는 잔액을 직접 수정하지 않고 `pay()`를 통해 변경합니다.

이 구조는 상태 변경 규칙을 클래스 내부에 모을 수 있습니다.

---

# 27. 검증이 필요한 이유

현재 원본은 잔액보다 큰 금액도 차감할 수 있습니다.

개선:

```python
def pay(self, price):
    if price <= 0:
        raise ValueError("결제 금액은 0보다 커야 합니다.")

    if price > self.__money:
        raise ValueError("잔액이 부족합니다.")

    self.__money -= price
```

---

# 28. 잔액 조회 메서드

```python
def get_balance(self):
    return self.__money
```

외부에서 상태를 읽어야 한다면 공개 메서드를 제공할 수 있습니다.

---

# 29. 개선된 계좌 클래스

```python
class Wallet:
    def __init__(self, balance: int = 0):
        if balance < 0:
            raise ValueError(
                "초기 잔액은 음수일 수 없습니다."
            )

        self.__balance = balance

    def pay(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError(
                "결제 금액은 0보다 커야 합니다."
            )

        if amount > self.__balance:
            raise ValueError(
                "잔액이 부족합니다."
            )

        self.__balance -= amount

    def get_balance(self) -> int:
        return self.__balance
```

---

# 30. 클래스 속성

인스턴스가 아니라 클래스 자체에 속하는 값입니다.

```python
class Person:
    species = "human"
```

모든 인스턴스가 기본적으로 같은 클래스 속성을 공유합니다.

```python
print(Person.species)
```

---

# 31. 인스턴스 속성과 클래스 속성

```python
class Person:
    species = "human"

    def __init__(self, name):
        self.name = name
```

| 종류 | 예 | 저장 위치 |
| --- | --- | --- |
| 클래스 속성 | `species` | 클래스 |
| 인스턴스 속성 | `name` | 각 인스턴스 |

---

# 32. `__str__()`

객체를 사람이 읽기 좋은 문자열로 표현할 때 사용합니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
```

```python
print(Person("홍길동", 20))
```

---

# 33. 상속

기존 클래스의 속성과 메서드를 이어받아 새 클래스를 만들 수 있습니다.

```python
class Student(Person):
    def study(self):
        print("공부합니다.")
```

`Student`는 `Person`의 기능을 사용할 수 있습니다.

---

# 34. `super()`

부모 클래스의 메서드를 호출할 때 사용합니다.

```python
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
```

---

# 35. 내 코드의 장점

- 클래스 생성과 `__init__()` 실행 순서를 출력으로 확인했다.
- `self` 속성과 메서드 호출 관계를 직접 보여 준다.
- 같은 클래스로 만든 객체가 독립적이라는 점을 설명했다.
- 동적 속성 추가와 인스턴스별 차이를 확인했다.
- 비공개 속성에 외부에서 같은 이름을 대입해도 내부 값이 바뀌지 않는 점을 실습했다.
- 캡슐화와 은닉화의 목적을 주석으로 기록했다.
- 객체가 메모리에서 서로 다른 대상을 가리킨다는 점을 의식했다.

---

# 36. 내 코드 개선점

- `Person` 클래스에서 속성 이름 `hello`와 메서드 이름 `hello()`가 겹친다.
- 인스턴스 속성이 메서드 이름을 가릴 수 있어 혼란을 만든다.
- `__init__()`를 외부에서 직접 호출하는 예제는 학습 후 주의사항을 더 명확히 해야 한다.
- 동적 속성 추가는 가능하지만 실제 설계에서는 초기화 시 선언하는 편이 좋다.
- 결제 금액과 잔액 검증이 없다.
- 비공개 속성이 완전한 보안 기능이라는 오해를 피해야 한다.
- 클래스별 책임과 이름을 더 구체적으로 만들 수 있다.

---

# 37. 이름 충돌 문제

원본 `Person`:

```python
self.hello = "안녕하세요"

def hello(self):
    self.greeting()
```

인스턴스 속성 `hello`가 문자열로 저장되면 같은 이름의 메서드 접근을 가릴 수 있습니다.

권장:

```python
self.message = "안녕하세요"

def say_hello(self):
    self.greeting()
```

---

# 38. 강사님 코드의 장점

- 클래스 생성과 메서드 호출 흐름을 최소 코드로 보여 준다.
- `Person`, `Person2`, `Person3`로 학습 범위를 단계적으로 확장한다.
- 인스턴스별 속성 차이를 직접 확인한다.
- 외부에서 추가한 `__money`가 내부 비공개 속성과 다르다는 점을 보여 준다.
- 캡슐화와 은닉화 개념으로 자연스럽게 연결한다.

---

# 39. 데이터 클래스

데이터 저장이 중심인 클래스는 `dataclass`로 간결하게 작성할 수 있습니다.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    address: str | None = None
```

자동으로 초기화 메서드와 문자열 표현 등을 만들어 줍니다.

---

# 40. 객체 설계 기준

좋은 클래스는 다음을 고려합니다.

- 한 클래스는 하나의 명확한 책임을 가진다.
- 속성은 객체가 반드시 가져야 할 상태를 표현한다.
- 메서드는 그 상태와 관련된 행동을 표현한다.
- 잘못된 상태가 만들어지지 않도록 검증한다.
- 외부가 내부 구현에 과도하게 의존하지 않게 한다.
- 이름은 역할이 분명하게 드러나게 작성한다.

---

# 41. 실무형 예제

```python
class Student:
    def __init__(
        self,
        name: str,
        scores: list[int] | None = None,
    ):
        self.name = name
        self.scores = (
            scores.copy()
            if scores is not None
            else []
        )

    def add_score(self, score: int) -> None:
        if not 0 <= score <= 100:
            raise ValueError(
                "점수는 0부터 100 사이여야 합니다."
            )

        self.scores.append(score)

    def get_average(self) -> float:
        if not self.scores:
            return 0.0

        return sum(self.scores) / len(self.scores)
```

---

# 42. 자주 하는 실수

### 42.1 인스턴스 메서드에서 `self` 누락

호출 시 `TypeError`가 발생합니다.

### 42.2 `self.속성` 대신 지역 변수만 사용

초기화가 끝나면 인스턴스에 값이 저장되지 않습니다.

### 42.3 서로 다른 인스턴스가 같은 값이라고 착각

같은 클래스로 만들어도 객체는 독립적입니다.

### 42.4 동적 속성에 지나치게 의존

인스턴스마다 구조가 달라질 수 있습니다.

### 42.5 속성과 메서드에 같은 이름 사용

인스턴스 속성이 메서드를 가릴 수 있습니다.

### 42.6 이중 밑줄을 완전한 보안 기능으로 오해

이름 변환을 통한 접근 제한 관례에 가깝습니다.

### 42.7 `__init__()`를 일반 메서드처럼 반복 호출

기존 객체 상태가 예상치 않게 초기화될 수 있습니다.

### 42.8 모든 값을 외부에서 직접 수정

검증 규칙을 적용하기 어려워집니다.

---

# 43. 면접·복습 포인트

### Q1. 클래스와 인스턴스의 차이는 무엇인가요?

클래스는 객체를 만들기 위한 설계도이고, 인스턴스는 그 클래스로 만든 실제 객체입니다.

### Q2. `self`는 무엇인가요?

현재 메서드를 호출한 인스턴스 자신을 가리키는 매개변수입니다.

### Q3. `__init__()`은 언제 실행되나요?

인스턴스가 생성된 직후 자동으로 실행됩니다.

### Q4. 인스턴스 속성과 클래스 속성의 차이는 무엇인가요?

인스턴스 속성은 각 객체에 저장되고, 클래스 속성은 클래스 수준에서 공유됩니다.

### Q5. 이중 밑줄 속성은 완전히 접근할 수 없나요?

아닙니다. 이름 변환을 통해 직접 접근을 어렵게 할 뿐 완전한 보안 기능은 아닙니다.

### Q6. 캡슐화의 목적은 무엇인가요?

객체 상태와 동작을 묶고, 상태 변경 규칙을 클래스 내부에서 관리하기 위해서입니다.

### Q7. 객체에 실행 중 새 속성을 추가할 수 있나요?

가능하지만 객체 구조의 일관성을 해칠 수 있어 필요한 속성은 초기화 시 선언하는 편이 좋습니다.

### Q8. 속성과 메서드 이름이 같으면 어떤 문제가 생길 수 있나요?

인스턴스 속성이 메서드를 가려 메서드 호출이 불가능해질 수 있습니다.

---

# 최종 정리

```text
class로 설계도를 만든다.
→ 클래스 호출로 인스턴스를 생성한다.
→ __init__에서 초기 상태를 저장한다.
→ self로 현재 객체의 속성과 메서드에 접근한다.
→ 각 인스턴스는 독립적인 상태를 가진다.
→ 상태 변경은 메서드로 관리한다.
→ 캡슐화로 객체의 규칙과 일관성을 지킨다.
```
