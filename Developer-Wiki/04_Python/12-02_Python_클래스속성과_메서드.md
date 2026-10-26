# 12-02. 속성 숨기기, 클래스 속성, 정적·클래스 메서드

[Python 목차](README.md) · [이전: 클래스와 인스턴스](12-01_Python_클래스와_인스턴스.md) · [다음: 클래스 실습](12-03_Python_클래스_과제비교.md)

두 원본은 `Person3`로 이중 밑줄 속성의 동작을 보고, `Knotted`의 공통 상호, `Calc`의 정적 메서드, `Person4`의 생성 수를 확인한다.

<!-- chapter-toc -->

- [1. 이중 밑줄 속성의 실제 동작](#section-1)
- [2. 공통 속성과 정적 메서드](#section-2)
- [3. 클래스 메서드와 생성 수](#section-3)
- [직접 확인할 질문](#section-4)
- [추가로 알면 좋은 것](#section-5)

<a id="section-1"></a>

## 1. 이중 밑줄 속성의 실제 동작

### 강사님 코드

출처: `teacher/workspace_python/_12_class.py` 53–78행 · **원본 발췌**

```python
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
```

### 내 코드

출처: `me/workspace_python/12_class.py` 55–81행 · **원본 발췌**

```python
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

`a=Person3(10000)` 뒤 `a.pay(3000)`을 두 번 실행하면 `__money`는 **7000, 4000** 순으로 줄어든다. 중간의 `a.__money=...`는 클래스 안에서 쓰는 기존 `__money`를 바꾼 것이 아니라, **별도의 새 속성**을 인스턴스에 붙인다. 그래서 두 번째 `pay` 계산에 그 큰 숫자가 쓰이지 않는다.

원본 주석의 “외부로 노출되지 않는다”는 표현은 **완전한 접근 차단**으로 읽지 말자. Python의 이중 밑줄은 이름을 바꾸어 우연한 충돌이나 직접 접근을 어렵게 하는 방식이다. 지금은 `pay()`처럼 클래스가 제공한 메서드로 상태를 바꾸는 사용법을 먼저 익히면 된다.

<a id="section-2"></a>

## 2. 공통 속성과 정적 메서드

### 강사님 코드

출처: `teacher/workspace_python/_12_class.py` 81–114행 · **원본 발췌**

```python
class Knotted :

    brand = '노티드-디저트맛집'

    def __init__(self, name, addr) :
        # self.brand = '노티드-디저트맛집'
        self.name = name
        self.addr = addr
    def info(self):
        print(self.name)

k1 = Knotted('천안점', '천안')
k2 = Knotted('아산점', '아산')

print(k1.name, k1.brand)
print(k2.name, k2.brand)

print(k1.name, Knotted.brand)
print(k2.name, Knotted.brand)

class Calc :
    PI = 3.141592

    def __init__(self):
        self.meet = 200

    @staticmethod
    def add(x, y):
        return x + y

    def plus(self, x, y):
        return Calc.add(x, y)

print( Calc.add(1,2) * Calc.PI )
```

### 내 코드

출처: `me/workspace_python/12_class.py` 84–125행 · **원본 발췌**

```python
class Knotted :
    # 입구에서 선언하면 모든 Knotted라는 class가 공통적으로 가지고 있게 됨
    # 정적속성(static attribute) : 클래스를 생성하지 않고 사용이 가능하기 때문에, 메모리의 static영역에 존재(self 사용 못 함)
    # self는 생성 된 이후에나 사용이 가능하기 때문
    brand = '노티드-디저트맛집'

    def __init__(self, name, addr) :
        # self.brand = '노티드-디저트맛집'
        self.name = name
        self.addr = addr
    def info(self): # 공통적으로 쓰는 것 중에는, static 또는 method 영역이라고 불리는 공간이 있음
        print(self.name)

k1 = Knotted('천안점', '천안') # @staticmethod를 사용하면, 이것처럼 생성 없이 사용할 순 있으나,
k2 = Knotted('아산점', '아산') # 메모리에 바로 올라가있기 때문에 낭비가 될 순 있음 (각 장점, 단점)

print(k1.name, k1.brand) # 이렇게 하면 brand가 공통이라도, k1의 주소를 거쳐 지나감
print(k2.name, k2.brand) 

print(k1.name, Knotted.brand) # 이 방식이 더욱 빠르게 공통 영역에 접근할 수 있음
print(k2.name, Knotted.brand)

print('-'*30)
class Calc :
    PI = 3.141592

    def __init__(self) :
        self.meat = 200

    # 공통으로 사용할 수 있도록 선언, 데코레이터라고 부름
    # self는 생성을 해야 사용할 수 있는 것이기 때문에, 클래스나 스태틱으로 선언을 해두면 미사용
    @staticmethod 
    def add(x, y) :
    # def add(self, x, y) :
        # print(self.meat)
        return x + y

    def plus(self, x, y) :
        return self.add(x, y) # == return Calc.add(x, y)

print( Calc.add(1,2) * Calc.PI ) # class명.함수 로 접근하면 정적메소드
# print( Calc.add(Calc(), 1,2) * Calc.PI ) # add에 self를 넣었을 때 첫 번째 인자에 생성을 해줘야 사용 가능
```

`Knotted.brand`는 클래스에 정의된 **공통 속성**이다. `k1.name`과 `k2.name`은 각각 다르지만 두 인스턴스에서 읽은 `brand`는 같다. 내 주석의 “static 영역에 있다”, “클래스 이름으로 접근하면 더 빠르다”는 말은 이 예제로 확인한 결과가 아니다. 우선 **클래스에 속한 값과 인스턴스마다 다른 값**을 구분하자.

`Calc.add`에는 `@staticmethod`가 붙어 `Calc.add(1,2)`처럼 인스턴스를 만들지 않고 호출한다. `PI`도 클래스 속성이라 `Calc.PI`로 읽는다. 내 코드는 `plus`에서 `self.add(x,y)`를, 강사님은 `Calc.add(x,y)`를 썼다. 둘 다 이 예제에서는 같은 덧셈 결과를 얻는다.

<a id="section-3"></a>

## 3. 클래스 메서드와 생성 수

### 강사님 코드

출처: `teacher/workspace_python/_12_class.py` 116–143행 · **원본 발췌**

```python
class Person4:
    count = 0

    def __init__(self) :
        Person4.count += 1

    @classmethod
    def print_count(cls) :
        print(f'{cls.count}명 생성 됨')

p1 = Person4()
p2 = Person4()
p3 = Person4()
Person4.print_count()


class Account:
    def __init__(self):
        self.__balance = 0

    def setBalance(self, money):
        self.__balance = money

    def getBalance(self):
        return self.__balance

a1 = Account()
# a1.balance = 99999
```

### 내 코드

출처: `me/workspace_python/12_class.py` 127–153행 · **원본 발췌**

```python
class Person4 :
    count = 0

    def __init__(self) :
        Person4.count += 1

    @classmethod
    def print_count(cls) :
        print(f'{cls.count}명 생성됨')

p1 = Person4()
p2 = Person4()
p3 = Person4()
Person4.print_count()

class Account :
    def __init__(self) :
        self.__balance = 0

    def setBalance(self, money) :
        self.__balance = money

    def getBalance(self) :
        return self.__balance

a1 = Account()
# a1.balance = 99999
```

`Person4.count`는 클래스에 저장한 생성 수다. 세 번 `Person4()`를 호출하면 `__init__`에서 1씩 늘어 **3**이 된다. `@classmethod`가 붙은 `print_count(cls)`는 클래스의 `count`를 읽어 출력한다. 두 파일의 출력 문구는 조금 다르지만 카운트 방식은 같다. 아래 `Account`는 `setBalance()`와 `getBalance()`를 정의하지만, 두 원본 모두 `a1=Account()`까지만 실행한다. **잔액을 변경하거나 조회하는 호출은 없다.**

<a id="section-4"></a>

## 직접 확인할 질문

1. `a.__money=999999...` 뒤 두 번째 `pay(3000)`의 남은 돈은 얼마일까?
2. `k1.name`과 `k2.name`은 다른데 `Knotted.brand`는 왜 하나의 값일까?
3. `Person4.print_count()`가 출력하는 수는?

<a id="section-5"></a>

## 추가로 알면 좋은 것

이중 밑줄의 이름 변경 방식과 메서드 호출 시 클래스 상속이 끼어들 때의 차이는 뒤의 상속 장과 연결해 볼 수 있다. 이 장에서는 원본의 **직접 호출과 출력**을 기준으로 삼는다.

