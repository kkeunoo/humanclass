---
title: Python 클래스
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# Python 클래스

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `12_Python_클래스.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `02_Python_변수와_자료형_연산자.md`, `07_Python_딕셔너리와_집합.md`, `11_Python_함수.md` |
| 다음 학습 | `13_Python_상속과_다형성.md` |
| 원본 기준 | `workspace_python/12_class.py`, `workspace_teacher/workspace_python/_12_class.py` |
| 핵심 범위 | 클래스, 객체, 인스턴스, `__init__`, `self`, 인스턴스 속성, 클래스 속성, 인스턴스 메서드, `@staticmethod`, `@classmethod`, 캡슐화, Getter와 Setter |
| 실습 범위 | 멜론 차트 관리, 휴먼잡스 계정 관리, 노티드 지점 생성 |
| 종합 실습 | 별도 문서 `20_Python_종합실습.md`에서 관리 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 한 번에 나열하지 않는다.  
> 각 개념에서 필요한 코드만 발췌하고, 두 코드의 차이·실행 결과·동작 과정·실무 관점을 함께 설명한다.

---

# 개요

클래스는 여러 값을 단순히 묶는 문법이 아니다.

프로그램에서 하나의 대상을 표현하는 데이터와, 그 데이터를 사용하는 기능을 하나의 단위로 관리하기 위한 구조다.

예를 들어 회원을 표현한다면 다음 정보와 기능이 서로 관련되어 있다.

- 이름
- 나이
- 주소
- 자기소개
- 주소 변경
- 회원 정보 조회

이 값을 각각의 변수와 함수로 흩어 놓을 수도 있지만, 클래스에 묶으면 하나의 회원 객체로 관리할 수 있다.

```text
관련 데이터
+
관련 기능
    ↓
클래스에 정의
    ↓
필요한 만큼 객체 생성
    ↓
각 객체가 독립적인 상태 유지
```

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 클래스 | 객체를 만들기 위한 설계도 |
| 객체 | 프로그램에서 다루는 하나의 대상 |
| 인스턴스 | 특정 클래스로 생성된 실제 객체 |
| `__init__()` | 객체 생성 직후 초기 상태 설정 |
| `self` | 현재 메서드를 호출한 인스턴스 |
| 인스턴스 속성 | 각 객체가 개별적으로 가지는 값 |
| 클래스 속성 | 클래스 수준에서 공유하는 값 |
| 인스턴스 메서드 | 객체 상태를 사용하거나 변경하는 기능 |
| `@staticmethod` | 객체·클래스 상태 없이 동작하는 관련 기능 |
| `@classmethod` | 클래스 자체의 상태를 사용하는 기능 |
| 캡슐화 | 데이터와 변경 규칙을 클래스 내부에 묶는 설계 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 클래스와 인스턴스의 차이를 설명할 수 있다.
- `class` 문법으로 클래스를 정의할 수 있다.
- 클래스 이름을 PascalCase로 작성하는 이유를 이해한다.
- 객체 생성 시 `__init__()`이 자동으로 실행되는 흐름을 설명할 수 있다.
- `self`가 현재 인스턴스를 가리킨다는 점을 이해한다.
- 인스턴스마다 서로 다른 속성값을 저장할 수 있다.
- 인스턴스 메서드에서 현재 객체의 속성과 다른 메서드를 사용할 수 있다.
- 인스턴스 속성과 클래스 속성의 차이를 구분할 수 있다.
- `@staticmethod`와 `@classmethod`의 차이를 설명할 수 있다.
- 이중 밑줄 속성이 이름 변환을 통해 외부 접근을 어렵게 한다는 점을 이해한다.
- 캡슐화를 이용해 객체의 상태 변경 규칙을 클래스 내부에 둘 수 있다.
- Getter와 Setter 형태의 메서드를 작성할 수 있다.
- 한 객체를 다른 관리 객체의 리스트에 저장할 수 있다.
- 교육용 클래스와 실무형 클래스의 차이를 구분할 수 있다.

---

# 1. 클래스란?

클래스는 관련된 **데이터와 기능을 하나의 단위로 묶고**, 같은 구조의 객체를 반복해서 만들기 위한 설계도다.

```text
클래스 정의
    ↓
객체 생성
    ↓
인스턴스마다 상태 저장
    ↓
메서드로 상태 사용·변경
```

예를 들어 회원 정보를 각각의 변수와 함수로 따로 관리할 수도 있다.

```python
user_name = "홍길동"
user_age = 20

def introduce(name, age):
    print(f"저는 {name}이고 {age}살입니다.")
```

하지만 회원이 여러 명으로 늘어나면 관련 데이터를 하나의 단위로 묶는 편이 관리하기 쉽다.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"저는 {self.name}이고 {self.age}살입니다.")
```

> ✅ **핵심 정리**  
> 클래스는 설계도이고, 클래스로 생성된 실제 객체가 인스턴스다.

---

# 2. 클래스 정의와 객체 생성

## 2-1. 내 코드

```python
class Person:
    def __init__(self):
        print(1)
        self.hello = "안녕하세요"

    def greeting(self):
        print(self.hello)


james = Person()
james.greeting()
```

## 2-2. 강사님 코드

```python
class Person:
    def __init__(self):
        print(1)
        self.hello = "안녕하세요"

    def greeting(self):
        print(self.hello)


james = Person()
james.greeting()
```

두 코드는 클래스의 가장 기본적인 구조를 같은 방식으로 보여 준다.

## 2-3. 구성

| 요소 | 의미 |
| --- | --- |
| `class` | 클래스 정의 키워드 |
| `Person` | 클래스 이름 |
| `__init__` | 인스턴스 초기화 메서드 |
| `self` | 현재 인스턴스 |
| `self.hello` | 인스턴스 속성 |
| `greeting()` | 인스턴스 메서드 |
| `Person()` | 인스턴스 생성 |
| `james` | 생성된 인스턴스를 가리키는 변수 |

## 2-4. 실행

```python
james = Person()
james.greeting()
```

## 2-5. 출력 결과

```text
1
안녕하세요
```

## 2-6. 동작 과정

```text
Person() 실행
    ↓
새 Person 인스턴스 생성
    ↓
__init__(self) 자동 실행
    ↓
self.hello = "안녕하세요"
    ↓
생성된 객체를 james가 참조
    ↓
james.greeting() 호출
    ↓
self.hello 출력
```

## 2-7. 왜 사용할까?

- 같은 구조의 데이터를 여러 개 만들 수 있다.
- 데이터와 관련 기능을 함께 관리할 수 있다.
- 서로 다른 객체가 독립적인 상태를 가질 수 있다.
- 프로그램이 커져도 역할별로 코드를 나누기 쉽다.

## 2-8. 실무에서는?

실무에서는 `Person`처럼 너무 넓은 이름보다 역할을 구체적으로 드러내는 이름을 사용한다.

```python
class User:
    pass


class Product:
    pass


class BankAccount:
    pass
```

---

# 3. 클래스 이름 규칙

Python 클래스 이름은 일반적으로 **PascalCase**를 사용한다.

```python
class Person:
    pass


class BankAccount:
    pass


class HumanJobsAccount:
    pass
```

| 대상 | 권장 표기 |
| --- | --- |
| 클래스 | `PascalCase` |
| 함수·변수 | `snake_case` |
| 상수 | `UPPER_SNAKE_CASE` |

좋지 않은 예:

```python
class person:
    pass


class bank_account:
    pass
```

문법 오류는 아니지만 Python의 일반적인 코드 스타일과 맞지 않는다.

---

# 4. `__init__()`과 객체 생성 순서

`__init__()`은 인스턴스가 생성된 직후 자동으로 호출되는 초기화 메서드다.

## 4-1. 내 코드

```python
class Person:
    def __init__(self):
        print(1)


print(0)
james = Person()
print(2)
```

## 4-2. 강사님 코드

```python
class Person:
    def __init__(self):
        print(1)


print(0)
james = Person()
print(2)
```

## 4-3. 출력 결과

```text
0
1
2
```

## 4-4. 동작 과정

```text
print(0)
    ↓
0 출력
    ↓
Person() 실행
    ↓
__init__() 자동 실행
    ↓
1 출력
    ↓
객체 생성 완료
    ↓
print(2)
    ↓
2 출력
```

## 4-5. `__init__()`은 생성자인가?

입문 단계에서는 흔히 생성자라고 부르지만, Python 내부에서 실제 객체 생성은 `__new__()`가 담당하고 `__init__()`은 생성된 객체를 초기화한다.

초보 단계에서는 다음처럼 이해해도 충분하다.

```text
Person()
→ 객체 생성
→ __init__()으로 초기 상태 설정
```

## 4-6. 직접 호출할 수 있을까?

원본 코드에는 다음 실습이 있다.

```python
b.__init__(1, 2)
```

문법적으로 실행되지만 일반적인 사용 방식은 아니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("홍길동", 20)
person.__init__("김영희", 30)
```

실행 후 기존 객체의 상태가 다시 초기화된다.

```text
person.name → 김영희
person.age  → 30
```

> `__init__()`은 직접 반복 호출하기보다 새 객체를 생성하거나, 상태 변경 전용 메서드를 따로 만드는 편이 좋다.

---

# 5. `self`

`self`는 **현재 메서드를 호출한 인스턴스 자신**을 가리킨다.

## 5-1. 내 코드

```python
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"저는 {self.name}이고 나이는 {self.age}입니다.")
```

## 5-2. 강사님 코드

```python
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"저는 {self.name}이고 나이는 {self.age}입니다.")
```

## 5-3. 실행

```python
a = Person2("이름", 20)
b = Person2("다른이름", 30)

a.greeting()
b.greeting()
```

## 5-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `self` | 현재 메서드를 호출한 인스턴스를 가리키기 위해 |
| `self.name` | 현재 인스턴스의 이름을 읽기 위해 |
| `self.age` | 현재 인스턴스의 나이를 읽기 위해 |
| `greeting()` | 현재 인스턴스의 정보를 출력하기 위해 |

> [!IMPORTANT]
> 인스턴스 메서드에서 객체의 속성을 사용하려면 `self`가 필요하다.
>
> `name`만 사용하면 지역 변수나 매개변수를 가리키고, `self.name`을 사용해야 객체 안에 저장된 값을 읽을 수 있다.

## 5-5. 출력 결과

```text
저는 이름이고 나이는 20입니다.
저는 다른이름이고 나이는 30입니다.
```

## 5-6. 동작 과정

```text
a.greeting()
    ↓
self는 a를 가리킴
    ↓
self.name → "이름"
self.age  → 20

b.greeting()
    ↓
self는 b를 가리킴
    ↓
self.name → "다른이름"
self.age  → 30
```

## 5-7. 내부 동작 이해

다음 호출은:

```python
a.greeting()
```

개념적으로 다음과 비슷하다.

```python
Person2.greeting(a)
```

`self`라는 이름은 문법적으로 강제된 이름은 아니지만, Python에서는 반드시 `self`를 사용하는 것이 관례다.

좋지 않은 예:

```python
class Person:
    def greeting(current_object):
        print(current_object.name)
```

권장:

```python
class Person:
    def greeting(self):
        print(self.name)
```

---

# 6. 인스턴스 속성

인스턴스 속성은 각 객체가 개별적으로 가지는 데이터다.

```python
self.name = name
self.age = age
```

## 6-1. 입력 예시

```python
a = Person2("이름", 20)
b = Person2("다른이름", 30)
```

## 6-2. 객체 상태

```text
a
├─ name: "이름"
└─ age: 20

b
├─ name: "다른이름"
└─ age: 30
```

같은 클래스로 생성했지만 서로 다른 객체이므로 속성값도 독립적으로 유지된다.

## 6-3. 원본 리스트와 비슷하게 이해하기

```python
list_a = [1, 2]
list_b = [3, 4]
```

`list_a`와 `list_b`가 서로 다른 리스트인 것처럼 `a`와 `b`도 서로 다른 인스턴스다.

---

# 7. 동적 속성 추가

Python에서는 생성 후 객체에 새 속성을 추가할 수 있다.

## 7-1. 원본 코드

```python
b.addr = "천안"
print(b.addr)
```

## 7-2. 출력 결과

```text
천안
```

하지만 `a`에는 `addr`이 없다.

```python
print(a.addr)
```

```text
AttributeError: 'Person2' object has no attribute 'addr'
```

## 7-3. 왜 주의해야 할까?

동적으로 속성을 추가하면 인스턴스마다 구조가 달라질 수 있다.

```text
a → name, age
b → name, age, addr
```

이 구조는 규모가 커질수록 어떤 객체에 어떤 속성이 있는지 예측하기 어렵게 만든다.

## 7-4. 권장 방식

필요한 속성은 `__init__()`에서 모두 선언한다.

```python
class Person:
    def __init__(self, name, age, address=None):
        self.name = name
        self.age = age
        self.address = address
```

## 7-5. 실행

```python
a = Person("이름", 20)
b = Person("다른이름", 30, "천안")

print(a.address)
print(b.address)
```

## 7-6. 출력 결과

```text
None
천안
```

---

# 8. 인스턴스 메서드

인스턴스 메서드는 첫 번째 매개변수로 `self`를 받고, 현재 객체의 상태를 사용하거나 변경한다.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"안녕하세요. 저는 {self.name}입니다.")
```

## 8-1. 실행

```python
person = Person("홍길동")
person.greeting()
```

## 8-2. 출력 결과

```text
안녕하세요. 저는 홍길동입니다.
```

## 8-3. 같은 객체의 다른 메서드 호출

내 코드에는 다음 구조가 있다.

```python
def hello(self):
    self.greeting()
```

현재 인스턴스의 다른 메서드는 `self.메서드명()`으로 호출한다.

```python
class Person:
    def greeting(self):
        print("안녕하세요")

    def introduce(self):
        self.greeting()
        print("반갑습니다")
```

---

# 9. 속성과 메서드 이름 충돌

내 초기 코드에는 다음 구조가 있었다.

```python
self.hello = "안녕하세요"

def hello(self):
    self.greeting()
```

인스턴스 속성 `hello`와 메서드 `hello()`의 이름이 같다.

```python
james.hello()
```

실행 시 `james.hello`가 문자열 속성을 가리키게 되어 다음 오류가 발생할 수 있다.

```text
TypeError: 'str' object is not callable
```

## 9-1. 개선

```python
class Person:
    def __init__(self):
        self.message = "안녕하세요"

    def say_hello(self):
        print(self.message)
```

## 9-2. 이름 규칙

| 역할 | 이름 예시 |
| --- | --- |
| 데이터 속성 | `message`, `name`, `balance` |
| 동작 메서드 | `say_hello()`, `get_name()`, `pay()` |

> 속성은 명사, 메서드는 동사 형태로 작성하면 역할을 구분하기 쉽다.

---

# 10. 비공개 속성과 이름 변환

Python에서는 이중 밑줄로 시작하는 속성을 이용해 외부 접근을 어렵게 할 수 있다.

## 10-1. 내 코드

```python
class Person3:
    def __init__(self, money):
        self.__money = money

    def pay(self, price):
        self.__money -= price
        print("남은 돈:", self.__money)
```

## 10-2. 강사님 코드

```python
class Person3:
    def __init__(self, money):
        self.__money = money

    def pay(self, price):
        self.__money -= price
        print("남은 돈:", self.__money)
```

## 10-3. 실행

```python
person = Person3(10000)
person.pay(3000)
```

## 10-4. 출력 결과

```text
남은 돈: 7000
```

## 10-5. 외부 접근

```python
print(person.__money)
```

```text
AttributeError
```

## 10-6. 실제 동작

`self.__money`는 내부적으로 다음과 비슷한 이름으로 변환된다.

```text
_Person3__money
```

이를 **네임 맹글링(Name Mangling)**이라고 한다.

```text
__money
    ↓
_Person3__money
```

이 기능은 완전한 보안 기능이 아니다. 실수로 직접 접근하거나 하위 클래스의 속성과 충돌하는 일을 줄이는 기능에 가깝다.

---

# 11. 외부에서 같은 이름을 대입하면?

원본 코드:

```python
person.__money = 9999999
```

이 코드는 내부의 비공개 속성을 변경하지 않는다. 외부에 새로운 `__money` 속성을 추가한다.

```text
내부 속성
_Person3__money → 7000

외부에서 추가한 속성
__money → 9999999
```

그 뒤 다시 `pay()`를 호출하면 내부 속성을 사용한다.

```python
person.pay(3000)
```

```text
남은 돈: 4000
```

---

# 12. 비공개 메서드

## 12-1. 원본 코드

```python
class Person3:
    def pay(self, price):
        self.__study()

    def __study(self):
        print("히히 나 혼자 레벨 업")
```

클래스 내부에서는 호출할 수 있다.

```python
person.pay(3000)
```

하지만 외부에서 직접 호출하면 일반적으로 오류가 발생한다.

```python
person.__study()
```

```text
AttributeError
```

---

# 13. 캡슐화

캡슐화는 관련된 데이터와 동작을 클래스 안에 묶고, 객체 상태가 정해진 규칙을 통해서만 변경되도록 설계하는 것이다.

좋지 않은 예:

```python
account.balance = -100000
```

개선:

```python
account.withdraw(100000)
```

메서드 안에서 잔액 검증을 수행할 수 있다.

```python
class Account:
    def __init__(self, balance=0):
        self.__balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            print("출금액은 0보다 커야 합니다.")
            return

        if amount > self.__balance:
            print("잔액이 부족합니다.")
            return

        self.__balance -= amount
```

## 13-1. 왜 사용할까?

- 잘못된 값을 저장하지 못하게 한다.
- 상태 변경 규칙을 한곳에 모은다.
- 클래스 내부 구현을 바꿔도 외부 코드의 영향을 줄인다.
- 객체가 항상 유효한 상태를 유지하게 한다.

---

# 14. Getter와 Setter

원본 코드에서는 비공개 속성에 값을 저장하고 읽기 위해 메서드를 사용한다.

## 14-1. 내 코드

```python
class Account:
    def __init__(self):
        self.__balance = 0

    def setBalance(self, money):
        self.__balance = money

    def getBalance(self):
        return self.__balance
```

## 14-2. Getter와 Setter의 역할

**Getter는 값을 가져오기(읽기) 위한 메서드**다.

```python
def getBalance(self):
    return self.__balance
```

**Setter는 값을 변경하기 위한 메서드**다.

```python
def setBalance(self, money):
    self.__balance = money
```

## 14-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `self` | 현재 `Account` 인스턴스를 가리키기 위해 |
| `money` | 새로 저장할 잔액을 전달받기 위해 |
| `self.__balance` | 현재 객체의 비공개 잔액을 읽거나 변경하기 위해 |
| `return` | Getter가 읽은 값을 호출한 곳으로 돌려주기 위해 |

> [!IMPORTANT]
> Getter와 Setter는 인스턴스의 값을 다루므로 `self`를 사용해야 한다.
>
> `self`가 없으면 어떤 `Account` 객체의 잔액을 읽고 변경해야 하는지 알 수 없다.

## 14-4. 강사님 코드

```python
class Account:
    def __init__(self):
        self.__balance = 0

    def setBalance(self, money):
        self.__balance = money

    def getBalance(self):
        return self.__balance
```

## 14-5. 실행 예시

```python
account = Account()
account.setBalance(10000)

print(account.getBalance())
```

## 14-6. 출력 결과

```text
10000
```

## 14-7. 동작 과정

```text
Account() 생성
    ↓
__balance = 0
    ↓
setBalance(10000)
    ↓
__balance = 10000
    ↓
getBalance()
    ↓
10000 반환
```

## 14-8. 이름 개선

Python 함수와 메서드는 보통 snake_case를 사용한다.

```python
class Account:
    def set_balance(self, money):
        self.__balance = money

    def get_balance(self):
        return self.__balance
```

## 14-9. 검증 추가

```python
class Account:
    def __init__(self):
        self.__balance = 0

    def set_balance(self, money):
        if money < 0:
            raise ValueError("잔액은 음수일 수 없습니다.")

        self.__balance = money

    def get_balance(self):
        return self.__balance
```

## 14-10. 실무에서는 `property`

Python에서는 단순한 Getter와 Setter를 직접 호출하는 대신 `property`를 사용하는 경우가 많다.

> 💡 **알아두기 — `property`란?**
>
> `property`는 메서드를 일반 속성처럼 사용할 수 있게 만드는 Python 기능이다.
>
> 외부 코드는 `account.get_balance()` 또는 `account.set_balance(10000)`처럼 메서드를 직접 호출하지 않고 다음처럼 사용할 수 있다.
>
> `account.balance = 10000`처럼 값을 대입하고 `print(account.balance)`처럼 값을 읽을 수 있다.
>
> 겉으로는 일반 변수처럼 보이지만, 값을 읽을 때는 Getter 역할의 메서드가 실행되고 값을 대입할 때는 Setter 역할의 메서드가 실행된다.

### Getter/Setter 메서드 방식

```python
account.set_balance(10000)
print(account.get_balance())
```

### `property` 방식

```python
account.balance = 10000
print(account.balance)
```

두 방식 모두 값을 읽고 변경할 수 있지만, `property` 방식은 사용하는 코드가 더 자연스럽다.

```python
class Account:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, money):
        if money < 0:
            raise ValueError("잔액은 음수일 수 없습니다.")

        self.__balance = money
```

### 실행

```python
account = Account()
account.balance = 10000

print(account.balance)
```

### 출력 결과

```text
10000
```

### 동작 과정

```text
account.balance = 10000
    ↓
@balance.setter가 붙은 balance() 실행
    ↓
money < 0 검사
    ↓
self.__balance = 10000

print(account.balance)
    ↓
@property가 붙은 balance() 실행
    ↓
self.__balance 반환
    ↓
10000 출력
```

### Getter와 Setter 대신 무조건 사용해야 할까?

항상 그런 것은 아니다.

| 상황 | 추천 방식 |
| --- | --- |
| 단순히 값을 읽고 쓰기만 함 | 공개 속성 직접 사용 |
| 값을 읽을 때 계산이나 가공이 필요함 | `property` |
| 값을 변경할 때 검증이 필요함 | `property` + Setter |
| 명령 성격이 강한 동작 | 일반 메서드 |
| 복잡한 처리나 여러 값 변경 | 일반 메서드 |

예를 들어 잔액을 변경하는 모든 동작을 단순 대입으로 표현하는 것은 적절하지 않을 수 있다.

```python
account.balance = account.balance - 3000
```

이 경우에는 결제라는 의미가 드러나는 메서드가 더 적절하다.

```python
account.pay(3000)
```

> 📌 **왜 사용할까?**
>
> 외부 코드에는 속성처럼 간단한 인터페이스를 제공하면서, 클래스 내부에서는 값 검증·계산·가공 로직을 실행하기 위해 사용한다.

> ⚠️ **주의**
>
> Java처럼 모든 속성에 기계적으로 Getter와 Setter를 만들 필요는 없다. Python에서는 특별한 검증이나 계산이 없다면 공개 속성을 직접 사용하는 것도 자연스럽다.

---

# 15. 클래스 속성

클래스 속성은 특정 인스턴스가 아니라 클래스 자체에 저장되는 값이다.

## 15-1. 내 코드

```python
class Knotted:
    brand = "노티드-디저트맛집"

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
```

## 15-2. 강사님 코드

```python
class Knotted:
    brand = "노티드-디저트맛집"

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
```

## 15-3. 실행

```python
k1 = Knotted("천안점", "천안")
k2 = Knotted("아산점", "아산")

print(k1.name, Knotted.brand)
print(k2.name, Knotted.brand)
```

## 15-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `brand` | 모든 지점이 함께 사용하는 브랜드명을 저장하기 위해 |
| `self.name` | 각 지점의 이름을 개별 저장하기 위해 |
| `self.addr` | 각 지점의 주소를 개별 저장하기 위해 |
| `Knotted.brand` | 클래스 공통값임을 명확하게 표현하기 위해 |

> [!IMPORTANT]
> 지점마다 달라지는 값은 인스턴스 속성으로, 모든 지점이 공유하는 값은 클래스 속성으로 작성한다.

## 15-5. 출력 결과

```text
천안점 노티드-디저트맛집
아산점 노티드-디저트맛집
```

## 15-6. 구조

```text
Knotted 클래스
└─ brand: "노티드-디저트맛집"

k1 인스턴스
├─ name: "천안점"
└─ addr: "천안"

k2 인스턴스
├─ name: "아산점"
└─ addr: "아산"
```

## 15-7. 인스턴스로도 접근할 수 있지만

```python
print(k1.brand)
```

가능하다. 하지만 클래스 공통값임을 드러내려면 다음 방식이 더 명확하다.

```python
print(Knotted.brand)
```

---

# 16. 인스턴스 속성과 클래스 속성 비교

| 구분 | 인스턴스 속성 | 클래스 속성 |
| --- | --- | --- |
| 선언 위치 | 보통 `__init__()` 내부 | 클래스 블록 내부 |
| 접근 | `self.name`, `object.name` | `ClassName.brand` |
| 저장 대상 | 각 인스턴스 | 클래스 |
| 값 공유 | 인스턴스마다 다름 | 기본적으로 공통 |
| 예시 | 이름, 나이, 주소 | 브랜드명, 생성 개수, 고정 상수 |

---

# 17. 변경 가능한 클래스 속성 주의

내 멜론 코드에는 다음 구조가 있다.

```python
class Melon1:
    allSong = []
```

리스트는 변경 가능한 객체이므로 모든 인스턴스가 같은 리스트를 공유한다.

```python
class Example:
    values = []


a = Example()
b = Example()

a.values.append(1)

print(b.values)
```

출력:

```text
[1]
```

`a`를 통해 추가했지만 클래스 속성 리스트를 공유하므로 `b`에서도 보인다.

## 17-1. 언제 문제가 될까?

인스턴스별로 별도의 목록이 필요하다면 클래스 속성 리스트를 사용하면 안 된다.

권장:

```python
class Melon:
    def __init__(self):
        self.song_list = []
```

각 `Melon` 인스턴스마다 독립적인 노래 목록을 가진다.

---

# 18. 정적 메서드 `@staticmethod`

정적 메서드는 클래스 내부에 정의되지만 `self`나 `cls`를 받지 않는 메서드다.

즉, 특정 인스턴스의 상태도 사용하지 않고 클래스 속성도 사용하지 않는다.

```text
인스턴스 상태 필요 없음
+
클래스 상태 필요 없음
+
클래스 주제와는 관련 있음
    ↓
@staticmethod
```

> 💡 **알아두기 — 왜 클래스 안에 둘까?**
>
> 일반 함수로 작성해도 동작하지만, 해당 기능이 특정 클래스의 역할과 밀접하게 관련되어 있다는 점을 표현하기 위해 클래스 안에 둘 수 있다.
>
> 예를 들어 숫자 계산 기능을 `Calculator` 클래스에 모으거나, 회원 입력값 검사 기능을 `UserValidator` 클래스에 모을 수 있다.

## 18-1. 내 코드

```python
class Calc:
    PI = 3.141592

    @staticmethod
    def add(x, y):
        return x + y
```

## 18-2. 강사님 코드

```python
class Calc:
    PI = 3.141592

    @staticmethod
    def add(x, y):
        return x + y
```

## 18-3. 실행

```python
result = Calc.add(1, 2) * Calc.PI
print(result)
```

## 18-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `@staticmethod` | 이 메서드가 인스턴스나 클래스 상태를 사용하지 않음을 나타내기 위해 |
| `x`, `y` | 계산할 두 값을 전달받기 위해 |
| `return` | 계산 결과를 호출한 곳으로 돌려주기 위해 |
| `Calc.PI` | 클래스에 저장된 공통 상수를 사용하기 위해 |
| `Calc.add()` | 객체를 만들지 않고 클래스 이름으로 기능을 호출하기 위해 |

> [!TIP]
> `@staticmethod` 안에서는 `self`를 사용하지 않는다.
>
> 이 예제의 `add()`는 현재 객체의 이름이나 잔액 같은 인스턴스 정보가 전혀 필요하지 않고, 전달받은 `x`와 `y`만으로 계산할 수 있기 때문이다.

> [!WARNING]
> 정적 메서드 안에서 `self.name`처럼 객체 속성을 사용해야 한다면 `@staticmethod`가 아니라 인스턴스 메서드로 작성해야 한다.

## 18-5. 출력 결과

```text
9.424776
```

## 18-6. 동작 과정

```text
Calc.add(1, 2)
    ↓
3 반환
    ↓
Calc.PI 읽기
    ↓
3 × 3.141592
    ↓
9.424776
```

## 18-7. 왜 사용할까?

다음 계산은 객체의 이름, 주소, 잔액 같은 상태와 관계가 없다.

```python
Calc.add(10, 20)
```

`10`과 `20`만 있으면 결과를 계산할 수 있으므로 `self`가 필요하지 않다.

또한 클래스 속성인 `count`, `brand` 등을 변경하지 않으므로 `cls`도 필요하지 않다.

```python
class NumberValidator:
    @staticmethod
    def is_positive(number):
        return number > 0
```

### 입력 및 실행

```python
print(NumberValidator.is_positive(10))
print(NumberValidator.is_positive(-3))
```

### 출력 결과

```text
True
False
```

### 적합한 사용 예

- 숫자 계산
- 문자열 형식 검사
- 이메일·전화번호 형식 검사
- 단위 변환
- 날짜 형식 검사
- 클래스와 관련된 단순 변환 기능

### 적합하지 않은 사용 예

다음 기능은 현재 회원 객체의 상태를 사용하므로 인스턴스 메서드가 적절하다.

```python
class User:
    def change_address(self, address):
        self.address = address
```

다음 기능은 클래스 전체의 생성 개수를 사용하므로 클래스 메서드가 적절하다.

```python
class User:
    count = 0

    @classmethod
    def print_count(cls):
        print(cls.count)
```

## 18-8. 언제 일반 함수가 더 나을까?

클래스와 연관성이 약한 단순 도우미 함수라면 모듈 수준의 일반 함수가 더 자연스러울 수 있다.

```python
def add(x, y):
    return x + y
```

| 질문 | 판단 |
| --- | --- |
| 특정 객체의 상태를 사용하는가? | 인스턴스 메서드 |
| 클래스 전체의 상태를 사용하는가? | 클래스 메서드 |
| 상태는 사용하지 않지만 클래스 역할과 밀접한가? | 정적 메서드 |
| 클래스와의 관련성도 약한가? | 일반 함수 |

> ⚠️ **주의**
>
> `@staticmethod`를 사용할 수 있다는 이유만으로 모든 도우미 함수를 클래스 안에 넣지는 않는다. 클래스의 책임과 관련성이 분명할 때 사용한다.

---

# 19. 클래스 메서드 `@classmethod`

클래스 메서드는 첫 번째 매개변수로 `cls`를 받고 현재 클래스 자체에 접근하는 메서드다.

인스턴스 하나의 상태가 아니라 클래스 속성처럼 모든 객체와 관련된 공통 상태를 다룰 때 사용한다.

```text
특정 객체 하나가 아닌
클래스 전체의 정보 사용
    ↓
cls로 현재 클래스 접근
    ↓
@classmethod
```

> 💡 **알아두기 — `cls`란?**
>
> `self`가 현재 인스턴스를 가리킨다면 `cls`는 현재 클래스를 가리킨다.
>
> `Person4.print_count()`를 호출하면 `cls`는 `Person4`가 된다. 클래스 이름을 직접 쓰지 않고 `cls`를 사용하면 상속되는 클래스에서도 현재 호출한 클래스를 기준으로 동작할 수 있다.

## 19-1. 내 코드

```python
class Person4:
    count = 0

    def __init__(self):
        Person4.count += 1

    @classmethod
    def print_count(cls):
        print(f"{cls.count}명 생성됨")
```

## 19-2. 강사님 코드

```python
class Person4:
    count = 0

    def __init__(self):
        Person4.count += 1

    @classmethod
    def print_count(cls):
        print(f"{cls.count}명 생성 됨")
```

## 19-3. 실행

```python
p1 = Person4()
p2 = Person4()
p3 = Person4()

Person4.print_count()
```

## 19-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `count` | 생성된 `Person4` 객체의 전체 개수를 저장하기 위해 |
| `Person4.count += 1` | 객체가 생성될 때마다 클래스 속성 값을 증가시키기 위해 |
| `@classmethod` | 메서드가 현재 클래스를 자동으로 전달받게 하기 위해 |
| `cls` | 현재 클래스를 가리키기 위해 |
| `cls.count` | 클래스 속성 `count`를 읽기 위해 |
| `print_count()` | 클래스 전체에 저장된 생성 개수를 출력하기 위해 |

> [!TIP]
> 이 예제에서 `@classmethod`를 사용하는 핵심 이유는 **인스턴스 하나의 값이 아니라 클래스에 저장된 `count`를 사용하기 위해서**다.
>
> `p1`, `p2`, `p3`가 각각 다른 객체여도 `count`는 `Person4` 클래스에 하나만 존재한다.

> [!IMPORTANT]
> 클래스 메서드에서는 `self` 대신 `cls`를 사용한다.
>
> `self`는 객체 하나를 가리키고, `cls`는 클래스 전체를 가리키기 때문이다.

## 19-5. 출력 결과

```text
3명 생성됨
```

## 19-6. 동작 과정

```text
Person4.count = 0
    ↓
p1 생성 → count = 1
    ↓
p2 생성 → count = 2
    ↓
p3 생성 → count = 3
    ↓
Person4.print_count()
    ↓
cls는 Person4를 가리킴
    ↓
3명 생성됨 출력
```

## 19-7. `cls`를 사용하는 이유

클래스 이름을 직접 사용하면 현재 코드가 특정 클래스 이름에 강하게 묶인다.

```python
Person4.count
```

클래스 메서드 안에서 `cls`를 사용하면 현재 메서드를 호출한 클래스를 기준으로 접근할 수 있다.

```python
@classmethod
def print_count(cls):
    print(cls.count)
```

### `self`와 `cls` 비교

| 구분 | `self` | `cls` |
| --- | --- | --- |
| 가리키는 대상 | 현재 인스턴스 | 현재 클래스 |
| 사용 메서드 | 인스턴스 메서드 | 클래스 메서드 |
| 주요 접근 대상 | 인스턴스 속성 | 클래스 속성 |
| 대표 예 | 주소 변경, 잔액 차감 | 생성 개수, 공통 설정 |

### 클래스 메서드가 적합한 상황

- 생성된 객체 수 관리
- 클래스 공통 설정 조회·변경
- 대체 생성자 작성
- 문자열이나 딕셔너리에서 객체 생성
- 하위 클래스에서도 같은 생성 규칙 재사용

상속까지 고려하면 클래스 이름을 직접 쓰는 것보다 `type(self)` 또는 `cls`를 활용하는 구조가 더 유연할 수 있다.

```python
class Person:
    count = 0

    def __init__(self):
        type(self).count += 1
```

클래스 메서드는 대체 생성자를 만들 때도 자주 사용한다.

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, value):
        name, age = value.split(",")
        return cls(name, int(age))
```

### 실행

```python
user = User.from_string("홍길동,20")

print(user.name)
print(user.age)
```

### 출력 결과

```text
홍길동
20
```

---

# 20. 인스턴스 메서드·정적 메서드·클래스 메서드 비교

| 구분 | 첫 매개변수 | 접근 대상 | 대표 사용 |
| --- | --- | --- | --- |
| 인스턴스 메서드 | `self` | 인스턴스·클래스 상태 | 객체 상태 조회·변경 |
| 정적 메서드 | 없음 | 직접 접근 없음 | 클래스와 관련된 독립 기능 |
| 클래스 메서드 | `cls` | 클래스 상태 | 클래스 속성 관리, 대체 생성자 |

```python
class Example:
    class_value = 10

    def instance_method(self):
        return self.class_value

    @staticmethod
    def static_method(x, y):
        return x + y

    @classmethod
    def class_method(cls):
        return cls.class_value
```

## 20-1. 어떤 메서드를 선택할까?

```text
현재 객체의 속성이 필요한가?
    ├─ 예 → 인스턴스 메서드
    └─ 아니오
         ↓
클래스 속성이 필요한가?
    ├─ 예 → 클래스 메서드
    └─ 아니오
         ↓
기능이 클래스 역할과 밀접한가?
    ├─ 예 → 정적 메서드
    └─ 아니오 → 일반 함수
```

> [!IMPORTANT]
> 데코레이터 이름부터 외우기보다 **이 기능이 어떤 값을 사용해야 하는지** 먼저 판단한다.
>
> - 객체의 속성 사용 → 인스턴스 메서드
> - 클래스 속성 사용 → 클래스 메서드
> - 둘 다 사용하지 않음 → 정적 메서드 또는 일반 함수

---

# 21. 실습 1: 멜론 차트 관리 시스템

## 21-1. 문제

다음 정보를 가진 노래 객체를 만든다.

- 제목
- 가수명
- 앨범명
- 가사

두 곡 이상을 저장하고 각 곡을 다음 형식으로 출력한다.

```text
제목-가수명
```

---

## 21-2. 내 코드

```python
class Melon1:
    allSong = []

    def __init__(self, title, singer, album, words):
        self.melonList = {
            "title": title,
            "singer": singer,
            "albem": album,
            "words": words,
        }

        Melon1.allSong.append(self.melonList)

    def print_sing(self):
        print(
            self.melonList["title"],
            self.melonList["singer"],
            sep="-",
        )
```

## 21-3. 강사님 코드

```python
class Song:
    def __init__(self, title, singer, album, lyric):
        self.title = title
        self.singer = singer
        self.album = album
        self.lyric = lyric


s1 = Song(
    "LOVE ATTACK",
    "RESCENE (리센느)",
    "SCENEDROME",
    "라부 어택",
)

s2 = Song(
    "갑자기",
    "아이오아이 (I.O.I)",
    "I.O.I 3rd MINI ALBUM",
    "써든 어택",
)

melon = [s1, s2]

for song in melon:
    print(f"{song.title}-{song.singer}")
```

## 21-4. 코드 비교

| 구분 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 한 곡 표현 | `Melon1` 내부 딕셔너리 | `Song` 객체 |
| 전체 목록 | 클래스 속성 `allSong` | 일반 리스트 `melon` |
| 출력 | 각 인스턴스의 메서드 호출 | 리스트 반복 |
| 장점 | 생성과 동시에 전체 목록에 저장 | 한 곡의 책임이 명확함 |
| 주의점 | 모든 객체가 하나의 가변 리스트 공유 | 관리 기능이 별도 객체로 분리되지 않음 |

## 21-5. 실행 예시

```python
song1 = Song(
    "LOVE ATTACK",
    "RESCENE (리센느)",
    "SCENEDROME",
    "라부 어택",
)

song2 = Song(
    "갑자기",
    "아이오아이 (I.O.I)",
    "I.O.I 3rd MINI ALBUM",
    "써든 어택",
)

songs = [song1, song2]

for song in songs:
    print(f"{song.title}-{song.singer}")
```

## 21-6. 출력 결과

```text
LOVE ATTACK-RESCENE (리센느)
갑자기-아이오아이 (I.O.I)
```

## 21-7. 실무형 개선

한 곡의 정보와 여러 곡을 관리하는 역할을 분리한다.

```python
class Song:
    def __init__(
        self,
        title,
        singer,
        album,
        lyric,
    ):
        self.title = title
        self.singer = singer
        self.album = album
        self.lyric = lyric

    def get_summary(self):
        return f"{self.title}-{self.singer}"


class MelonChart:
    def __init__(self):
        self.song_list = []

    def add_song(self, song):
        self.song_list.append(song)

    def print_chart(self):
        for song in self.song_list:
            print(song.get_summary())
```

### 입력 및 실행

```python
chart = MelonChart()

chart.add_song(
    Song(
        "LOVE ATTACK",
        "RESCENE (리센느)",
        "SCENEDROME",
        "라부 어택",
    )
)

chart.add_song(
    Song(
        "갑자기",
        "아이오아이 (I.O.I)",
        "I.O.I 3rd MINI ALBUM",
        "써든 어택",
    )
)

chart.print_chart()
```

### 출력 결과

```text
LOVE ATTACK-RESCENE (리센느)
갑자기-아이오아이 (I.O.I)
```

### 객체 관계

```text
MelonChart
└─ song_list
   ├─ Song 객체 1
   └─ Song 객체 2
```

### 왜 이 구조가 좋을까?

- `Song`은 한 곡의 정보만 담당한다.
- `MelonChart`는 여러 곡의 추가·조회·출력을 담당한다.
- 노래 정보와 목록 관리 책임이 분리된다.
- 나중에 삭제, 검색, 정렬 기능을 추가하기 쉽다.

---

# 22. 실습 2: 휴먼잡스 계정 관리 시스템

## 22-1. 문제

계정은 다음 데이터를 가진다.

- ID
- 비밀번호
- 주소

모든 값은 외부 직접 접근을 제한하고, 메서드로 주소를 변경하거나 조회한다.

---

## 22-2. 내 코드

```python
class Human:
    def __init__(self):
        self.__id = ""
        self.__pw = ""
        self.__addr = ""

    def setAccount(self, id, pw, addr):
        self.__id = id
        self.__pw = pw
        self.__addr = addr

    def getAccount(self):
        return self.__id, self.__pw, self.__addr
```

## 22-3. 강사님 코드

```python
class HumanJobs:
    def __init__(self):
        self.__id = None
        self.__pw = ""
        self.__addr = ""

    def setAddr(self, addr):
        if addr:
            self.__addr = addr
        else:
            print("주소를 다시 입력하세요")

    def getAddr(self):
        return self.__addr
```

## 22-4. 코드 비교

| 구분 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 변경 범위 | 계정 전체 변경 | 주소만 변경 |
| 문제 요구 반영 | ID·PW·주소를 한 번에 설정 | 주소 변경 요구에 집중 |
| 검증 | 없음 | 빈 주소 검사 |
| 반환 | 계정 전체 튜플 | 주소만 반환 |

문제에서 요구한 핵심은 주소 변경과 조회이므로 강사님 코드가 요구사항에 더 정확히 맞는다.

## 22-5. 실행 예시

```python
account = HumanJobs()
account.setAddr("천안")

print(account.getAddr())
```

## 22-6. 출력 결과

```text
천안
```

## 22-7. 빈 값 입력

```python
account.setAddr("")
```

```text
주소를 다시 입력하세요
```

## 22-8. 실무형 개선

```python
class HumanJobsAccount:
    def __init__(self, user_id, password, address):
        self.__user_id = user_id
        self.__password = password
        self.__address = address

    def change_address(self, address):
        address = address.strip()

        if not address:
            raise ValueError("주소를 입력해야 합니다.")

        self.__address = address

    def get_address(self):
        return self.__address
```

### 입력 및 실행

```python
account = HumanJobsAccount(
    "human",
    "1234",
    "천안시 동남구",
)

account.change_address("천안시 서북구")

print(account.get_address())
```

### 출력 결과

```text
천안시 서북구
```

### 왜 이렇게 작성할까?

- 객체 생성 시 필수 계정 정보를 받는다.
- 주소 변경 기능만 별도 메서드로 둔다.
- 빈 문자열이나 공백만 있는 주소를 차단한다.
- 비밀번호는 외부에 반환하지 않는다.

> 실제 서비스에서는 비밀번호 원문을 객체나 데이터베이스에 그대로 저장하지 않고 안전한 해시 방식으로 처리한다.

---

# 23. 실습 3: 노티드 지점 생성

## 23-1. 문제

노티드 지점을 만들 때 다음 값이 필수다.

- 상호
- 자본금

두 지점을 생성한다.

---

## 23-2. 내 코드

```python
class MKnotted:
    def __init__(self, name, money):
        self.name = name
        self.money = money


k1 = MKnotted("천안점", 20000)
k2 = MKnotted("아산점", 50000)
```

## 23-3. 강사님 코드

```python
class Knotted2:
    def __init__(self, 상호, 자본금):
        self.상호 = 상호
        self.자본금 = 자본금


k1 = Knotted2("천안점", 10000)
```

## 23-4. 실행 예시

```python
k1 = MKnotted("천안점", 20000)
k2 = MKnotted("아산점", 50000)

print(k1.name, k1.money)
print(k2.name, k2.money)
```

## 23-5. 출력 결과

```text
천안점 20000
아산점 50000
```

## 23-6. 필수 인자를 누락하면?

```python
k3 = MKnotted("동남점")
```

```text
TypeError: MKnotted.__init__() missing 1 required positional argument
```

`__init__()`에 기본값이 없기 때문에 지점 이름과 자본금을 모두 전달해야 생성된다.

## 23-7. 실무형 개선

```python
class KnottedStore:
    BRAND_NAME = "노티드"

    def __init__(self, branch_name, capital):
        branch_name = branch_name.strip()

        if not branch_name:
            raise ValueError("지점명을 입력해야 합니다.")

        if capital <= 0:
            raise ValueError("자본금은 0보다 커야 합니다.")

        self.branch_name = branch_name
        self.capital = capital

    def get_summary(self):
        return (
            f"{self.BRAND_NAME} {self.branch_name} "
            f"- 자본금: {self.capital:,}원"
        )
```

### 입력 및 실행

```python
store1 = KnottedStore("천안점", 20_000_000)
store2 = KnottedStore("아산점", 50_000_000)

print(store1.get_summary())
print(store2.get_summary())
```

### 출력 결과

```text
노티드 천안점 - 자본금: 20,000,000원
노티드 아산점 - 자본금: 50,000,000원
```

---

# 24. 객체를 다른 객체에 저장하기

원본 마지막에는 `Song` 객체를 `Melon` 객체의 리스트에 저장하는 구조가 있다.

## 24-1. 원본 코드

```python
class Melon:
    def __init__(self):
        self.songList = []

    def appendSong(self, song):
        self.songList.append(song)


melon = Melon()
melon.appendSong(sing1)
```

## 24-2. 핵심 개념

리스트에는 숫자나 문자열뿐 아니라 객체도 저장할 수 있다.

```python
song_list = [song1, song2]
```

각 요소는 `Song` 인스턴스다.

```python
for song in song_list:
    print(song.title)
```

## 24-3. 왜 중요한가?

실무 프로그램은 여러 객체가 서로 관계를 맺는 구조로 만들어진다.

```text
주문 객체
└─ 주문 상품 객체 목록

게시판 객체
└─ 게시글 객체 목록

장바구니 객체
└─ 상품 객체 목록

멜론 차트 객체
└─ 노래 객체 목록
```

이 구조를 객체 합성 또는 포함 관계의 기초로 볼 수 있다.

---

# 25. 실무에서는 어떻게 클래스를 설계할까?

## 25-1. 클래스 하나에 하나의 주요 책임

좋지 않은 예:

```python
class App:
    def create_user(self):
        pass

    def add_song(self):
        pass

    def open_store(self):
        pass
```

서로 관련 없는 기능이 한 클래스에 섞여 있다.

권장:

```python
class UserAccount:
    pass


class Song:
    pass


class MelonChart:
    pass


class KnottedStore:
    pass
```

## 25-2. 유효하지 않은 상태를 막기

```python
class Product:
    def __init__(self, name, price):
        if not name.strip():
            raise ValueError("상품명을 입력해야 합니다.")

        if price < 0:
            raise ValueError("가격은 음수일 수 없습니다.")

        self.name = name
        self.price = price
```

## 25-3. 외부가 내부 구현에 과도하게 의존하지 않게 하기

좋지 않은 예:

```python
account._HumanJobsAccount__address = "서울"
```

권장:

```python
account.change_address("서울")
```

## 25-4. 타입 힌트 사용

```python
class Song:
    def __init__(
        self,
        title: str,
        singer: str,
        album: str,
        lyric: str,
    ) -> None:
        self.title = title
        self.singer = singer
        self.album = album
        self.lyric = lyric
```

타입 힌트는 실행을 강제하지 않지만 입력값과 속성의 의도를 명확하게 만든다.

---

# 26. 데이터 저장 중심 클래스와 `dataclass`

속성 저장이 중심인 단순 클래스는 `dataclass`로 간결하게 표현할 수 있다.

```python
from dataclasses import dataclass


@dataclass
class Song:
    title: str
    singer: str
    album: str
    lyric: str
```

## 26-1. 실행

```python
song = Song(
    "LOVE ATTACK",
    "RESCENE (리센느)",
    "SCENEDROME",
    "라부 어택",
)

print(song)
```

## 26-2. 출력 결과

```text
Song(title='LOVE ATTACK', singer='RESCENE (리센느)', album='SCENEDROME', lyric='라부 어택')
```

`dataclass`는 `__init__()`, `__repr__()`, 비교 기능 등을 자동으로 생성한다.

> 클래스 문법을 충분히 이해한 뒤 사용하는 것이 좋다.

---

# 27. 객체의 문자열 표현 `__str__()`

객체를 `print()`했을 때 사람이 읽기 좋은 내용을 출력하려면 `__str__()`을 정의할 수 있다.

```python
class Song:
    def __init__(self, title, singer):
        self.title = title
        self.singer = singer

    def __str__(self):
        return f"{self.title}-{self.singer}"
```

## 27-1. 실행

```python
song = Song("LOVE ATTACK", "RESCENE")
print(song)
```

## 27-2. 출력 결과

```text
LOVE ATTACK-RESCENE
```

---

# 28. 메모리와 객체 참조 이해

내 코드 주석에는 클래스와 객체가 메모리에서 어떻게 다뤄지는지 생각한 흔적이 있다.

초보 단계에서는 다음처럼 이해하면 된다.

```text
a = Person2("이름", 20)

a 변수
    ↓
Person2 인스턴스를 참조
    ↓
인스턴스 안에 name, age 저장
```

```text
b = Person2("다른이름", 30)

b 변수
    ↓
다른 Person2 인스턴스를 참조
```

변수에 `None`을 대입하거나 다른 객체로 덮어쓰면 기존 객체를 더 이상 참조하지 않을 수 있다.

```python
a = None
```

어떤 곳에서도 객체를 참조하지 않으면 Python의 가비지 컬렉션 대상이 될 수 있다.

> 객체가 즉시 메모리에서 사라지는 시점은 구현과 참조 관계에 따라 달라질 수 있으므로, “변수가 끝나면 반드시 즉시 삭제된다”라고 단정하지 않는다.

---


# 29. 대표 오류로 이해하기

정상 코드만 보는 것보다 **어떤 코드에서 오류가 발생하고, 왜 수정해야 하는지** 함께 확인하면 클래스의 동작을 더 정확히 이해할 수 있다.

## 29-1. 인스턴스 메서드에서 `self`를 생략한 경우

### 잘못된 코드

```python
class Person:
    def greeting():
        print("안녕하세요")


person = Person()
person.greeting()
```

### 발생 결과

```text
TypeError
```

### 오류 원인

`person.greeting()`을 호출하면 Python은 호출한 객체 `person`을 메서드의 첫 번째 인자로 자동 전달한다.

하지만 `greeting()`에는 이를 받을 매개변수가 없으므로 오류가 발생한다.

### 올바른 코드

```python
class Person:
    def greeting(self):
        print("안녕하세요")


person = Person()
person.greeting()
```

> [!IMPORTANT]
> 현재 객체의 속성이나 메서드를 사용하는 인스턴스 메서드는 첫 번째 매개변수로 `self`를 받아야 한다.

---

## 29-2. 인스턴스 속성을 저장하지 않은 경우

### 잘못된 코드

```python
class Person:
    def __init__(self, name):
        name = name
```

이 코드는 전달받은 값을 지역 변수에 다시 대입할 뿐, 객체에는 저장하지 않는다.

### 올바른 코드

```python
class Person:
    def __init__(self, name):
        self.name = name
```

```text
name
→ __init__()이 전달받은 매개변수

self.name
→ 현재 객체에 저장되는 인스턴스 속성
```

---

## 29-3. 클래스 속성 리스트를 의도하지 않게 공유한 경우

### 주의할 코드

```python
class Cart:
    items = []
```

```python
cart1 = Cart()
cart2 = Cart()

cart1.items.append("노트북")

print(cart2.items)
```

### 출력 결과

```text
['노트북']
```

`items`가 클래스 속성이므로 `cart1`과 `cart2`가 같은 리스트를 공유한다.

### 인스턴스별 목록이 필요한 경우

```python
class Cart:
    def __init__(self):
        self.items = []
```

> [!WARNING]
> 리스트·딕셔너리·집합처럼 변경 가능한 객체를 클래스 속성으로 선언하면 모든 인스턴스가 함께 변경 내용을 볼 수 있다.

---

# 30. 객체와 데이터가 저장되는 구조

클래스 속성과 인스턴스 속성이 어디에 저장되는지 다음 구조로 이해할 수 있다.

```text
Person 클래스
│
├─ 클래스 속성
│  └─ count: 2
│
├─ person1 인스턴스
│  ├─ name: "홍길동"
│  └─ age: 20
│
└─ person2 인스턴스
   ├─ name: "김영희"
   └─ age: 30
```

- `count`는 클래스에 하나만 존재한다.
- `name`, `age`는 각 인스턴스에 따로 저장된다.
- `person1.name`을 변경해도 `person2.name`은 바뀌지 않는다.
- 클래스 속성은 클래스 전체에 관련된 공통 상태를 표현할 때 사용한다.

---

# 31. 기존 코드에서 개선 코드로 바꾼 이유

실무형 코드는 단순히 문법을 어렵게 바꾼 코드가 아니다. **객체의 역할을 분리하고 잘못된 상태를 방지하기 위해** 구조를 개선한 코드다.

## 31-1. 멜론 예제

```text
기존 구조
Melon1
├─ 한 곡의 정보 저장
├─ 전체 노래 목록 저장
└─ 노래 출력
```

한 클래스가 여러 역할을 담당한다.

```text
개선 구조
Song
└─ 한 곡의 정보 담당

MelonChart
├─ 여러 Song 객체 저장
├─ 노래 추가
└─ 차트 출력
```

### 개선된 점

- 한 곡의 정보와 여러 곡의 관리 역할을 분리했다.
- 목록 검색·삭제·정렬 기능을 추가하기 쉬워졌다.
- 클래스 속성 리스트의 의도하지 않은 공유를 피했다.

## 31-2. 계정 예제

```text
기존 구조
→ ID, 비밀번호, 주소를 한 번에 변경
→ 입력값 검증 없음
→ 비밀번호까지 외부로 반환
```

```text
개선 구조
→ 생성할 때 필수 계정 정보 저장
→ 주소 변경 기능만 별도 메서드로 분리
→ 빈 주소 검증
→ 비밀번호는 외부에 반환하지 않음
```

## 31-3. 노티드 예제

```text
기존 구조
→ 지점명과 자본금을 그대로 저장
```

```text
개선 구조
→ 빈 지점명 차단
→ 0 이하 자본금 차단
→ 브랜드명은 클래스 공통값으로 관리
→ 출력 형식을 메서드로 제공
```

> [!TIP]
> 개선 코드는 짧기 때문에 좋은 것이 아니라, **역할이 명확하고 잘못된 값을 막으며 이후 기능을 추가하기 쉽기 때문에** 좋은 코드다.

---

# 32. 자주 하는 실수

## 29-1. `self` 누락

```python
class Person:
    def greeting():
        print("안녕하세요")
```

```python
person = Person()
person.greeting()
```

```text
TypeError
```

권장:

```python
def greeting(self):
    print("안녕하세요")
```

---

## 29-2. 속성과 메서드 이름을 같게 작성

```python
self.hello = "안녕하세요"

def hello(self):
    pass
```

문자열 속성이 메서드를 가릴 수 있다.

---

## 29-3. 인스턴스 속성과 지역 변수 혼동

```python
class Person:
    def __init__(self, name):
        name = name
```

이 코드는 인스턴스에 값을 저장하지 않는다.

권장:

```python
self.name = name
```

---

## 29-4. 필요한 속성을 일부 인스턴스에만 추가

```python
b.addr = "천안"
```

`a.addr`는 존재하지 않을 수 있다.

---

## 29-5. 변경 가능한 클래스 속성 공유

```python
class Cart:
    items = []
```

모든 인스턴스가 같은 리스트를 공유한다.

권장:

```python
class Cart:
    def __init__(self):
        self.items = []
```

---

## 29-6. `__init__()` 직접 반복 호출

이미 생성된 객체의 상태가 예상치 않게 초기화될 수 있다.

---

## 29-7. 이중 밑줄을 완전한 보안으로 착각

이중 밑줄은 이름 변환이며 완전한 접근 차단 기능이 아니다.

---

## 29-8. Getter로 민감 정보 전체 반환

```python
return self.__id, self.__pw, self.__addr
```

비밀번호처럼 민감한 정보는 반환하지 않는 편이 좋다.

---

## 29-9. 클래스가 필요 없는 기능까지 모두 클래스에 넣기

단순한 독립 함수가 더 적절한 경우도 있다.

---

# 33. 면접·복습 포인트

## Q1. 클래스와 인스턴스의 차이는 무엇인가요?

클래스는 객체를 만들기 위한 설계도이고, 인스턴스는 클래스로 생성된 실제 객체다.

## Q2. `self`는 무엇인가요?

현재 인스턴스를 가리키는 첫 번째 매개변수다. 인스턴스 속성과 메서드에 접근할 때 사용한다.

## Q3. `__init__()`은 언제 실행되나요?

인스턴스가 생성된 직후 자동으로 실행되어 초기 상태를 설정한다.

## Q4. 인스턴스 속성과 클래스 속성의 차이는 무엇인가요?

인스턴스 속성은 각 객체에 개별 저장되고, 클래스 속성은 클래스에 저장되어 기본적으로 공유된다.

## Q5. `@staticmethod`는 언제 사용하나요?

클래스 주제와 관련은 있지만 인스턴스나 클래스 상태가 필요하지 않은 기능에 사용한다.

## Q6. `@classmethod`는 언제 사용하나요?

클래스 상태를 사용하거나 변경할 때, 또는 대체 생성자를 만들 때 사용한다.

## Q7. `self`와 `cls`의 차이는 무엇인가요?

`self`는 현재 인스턴스, `cls`는 현재 클래스를 가리킨다.

## Q8. 이중 밑줄 속성은 완전히 비공개인가요?

아니다. 이름 변환을 통해 외부 직접 접근을 어렵게 할 뿐 완전한 보안 기능은 아니다.

## Q9. 캡슐화는 왜 필요한가요?

객체 상태 변경 규칙을 클래스 내부에 모으고 유효하지 않은 상태를 방지하기 위해 필요하다.

## Q10. 클래스 속성으로 리스트를 사용할 때 주의할 점은 무엇인가요?

모든 인스턴스가 같은 리스트를 공유하므로 인스턴스별 목록이 필요하다면 `__init__()`에서 리스트를 생성해야 한다.

## Q11. 객체를 리스트에 저장할 수 있나요?

가능하다. 리스트의 각 요소가 객체를 참조하며 반복문으로 각 객체의 속성과 메서드를 사용할 수 있다.

---

# 34. 핵심 요약

```text
class
→ 객체를 만들기 위한 설계도

인스턴스
→ 클래스로 생성된 실제 객체

__init__
→ 객체 생성 직후 초기 상태 설정

self
→ 현재 인스턴스

인스턴스 속성
→ 객체마다 개별 저장

클래스 속성
→ 클래스 수준에서 공유

인스턴스 메서드
→ self로 객체 상태 사용

@staticmethod
→ self와 cls가 필요 없는 관련 기능

@classmethod
→ cls로 클래스 상태 사용

__속성
→ 이름 변환을 통한 외부 접근 제한

캡슐화
→ 상태와 변경 규칙을 클래스 내부에 묶기
```

---

# 35. 최종 체크리스트

- [ ] 클래스 이름을 PascalCase로 작성했는가?
- [ ] 인스턴스별 데이터는 `self.속성`으로 저장했는가?
- [ ] 필요한 속성을 `__init__()`에서 일관되게 초기화했는가?
- [ ] 속성과 메서드 이름이 충돌하지 않는가?
- [ ] 클래스 공통값과 인스턴스별 값을 구분했는가?
- [ ] 변경 가능한 클래스 속성을 의도 없이 공유하지 않았는가?
- [ ] 상태 변경 전에 필요한 검증을 수행하는가?
- [ ] 민감한 정보를 외부에 그대로 노출하지 않는가?
- [ ] 클래스 하나가 너무 많은 책임을 맡고 있지 않은가?
- [ ] 단순 함수로 충분한 기능을 불필요하게 클래스에 넣지 않았는가?

---

# 마무리

클래스는 단순히 `class` 문법을 사용하는 것이 목적이 아니다.

```text
관련 데이터와 기능을 묶고
    ↓
각 객체가 독립적인 상태를 가지며
    ↓
정해진 메서드를 통해 상태를 사용·변경하고
    ↓
여러 객체가 서로 관계를 맺도록 설계하는 것
```

이 핵심 흐름을 이해해야 이후의 상속, 다형성, 추상 클래스와 같은 객체지향 개념도 자연스럽게 연결할 수 있다.

# V3 동작 백과 보강 — 클래스 정의에서 메서드 호출까지

클래스 문을 실행하면 클래스 객체가 만들어진다. `Person("Kim")`처럼 호출하면 보통 `__new__`가 인스턴스를 만들고 `__init__`가 초기 상태를 설정한다. `person.introduce()`는 클래스에서 메서드를 찾아 인스턴스를 첫 인수 `self`로 자동 전달한다.

```python
class Person:
    species = "human"
    def __init__(self, name):
        self.name = name
    def introduce(self):
        return f"저는 {self.name}입니다."

person = Person("Kim")
print(person.name)
print(person.introduce())
```

```text
Kim
저는 Kim입니다.
```

인스턴스 속성은 객체별 상태이고 클래스 속성은 클래스 수준에서 공유된다. 초기화하지 않은 속성을 읽으면 `AttributeError`다.

**원본 연결:** 내 코드 `workspace_python/12_class.py`, 강사님 코드 `workspace_python/_12_class.py`의 생성자, 인스턴스·클래스 속성, 메서드, 객체 관계 예제를 기반으로 한다.
