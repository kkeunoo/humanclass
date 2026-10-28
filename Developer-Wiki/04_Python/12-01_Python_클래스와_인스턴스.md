# 12-01. 클래스와 인스턴스 — 같은 설계로 서로 다른 객체 만들기

[Python 목차](README.md) · [이전: 함수](11-03_Python_lambda와_변수범위.md) · [다음: 속성과 메서드](12-02_Python_클래스속성과_메서드.md)

양쪽 `12_class.py`는 `Person()`을 만들 때 `__init__`이 실행되는 순서부터 시작한다. 그 다음 `Person2`에서 같은 클래스로 만든 `a`와 `b`가 **서로 다른 값**을 갖는 것을 확인한다.

## 먼저: 클래스와 인스턴스

클래스는 같은 종류의 객체를 만드는 **설계**, 인스턴스는 그 설계로 실제 만든 객체다. 다음은 원본의 문법을 작은 크기로 다시 만든 설명용 예제다.

```python
class Person:
    def __init__(self, name):
        self.name = name

a = Person('민지')
b = Person('준호')
print(a.name)  # 민지
print(b.name)  # 준호
```

`__init__`은 각각의 `Person(...)`을 만들 때 실행된다. `self.name`은 그때 만들고 있는 **해당 인스턴스의 값**이다. `a.name`을 바꾼다고 `b.name`이 자동으로 바뀌지 않는 이유를 원본의 `Person2`와 비교하자.

<!-- chapter-toc -->

- [1. 생성과 `self`](12-01_Python_클래스와_인스턴스.md#section-1)
- [2. 생성자 인자와 인스턴스마다 다른 속성](12-01_Python_클래스와_인스턴스.md#section-2)
- [직접 확인할 질문](12-01_Python_클래스와_인스턴스.md#section-3)
- [추가로 알면 좋은 것](12-01_Python_클래스와_인스턴스.md#section-4)

<a id="section-1"></a>

## 1. 생성과 `self`

### 강사님 코드

출처: `teacher/workspace_python/_12_class.py` 2–24행 · **원본 발췌**

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
```

### 내 코드

출처: `me/workspace_python/12_class.py` 6–25행 · **원본 발췌**

```python
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
```

`print(0)` 뒤 `james = Person()`에서 `__init__` 안의 `print(1)`이 나오고, 그 다음 `print(2)`가 나온다. `james.greeting()`은 `self.hello`의 문자열 `'안녕하세요'`를 출력한다. `self`는 이 메서드를 호출한 **해당 인스턴스**를 가리키는 매개변수다.

두 클래스 모두 `self.hello`라는 **문자열 속성**과 `def hello(self)`라는 **메서드**를 같은 이름으로 정의했다. 생성 뒤 `james.hello`는 문자열 속성을 찾기 때문에 메서드처럼 `james.hello()`를 호출하면 문자열을 호출하려는 오류가 난다. 내 코드의 그 호출은 주석 처리되어 있다. 설명할 때는 `greeting()`처럼 이름이 겹치지 않는 메서드를 기준으로 읽는 편이 좋다.

<a id="section-2"></a>

## 2. 생성자 인자와 인스턴스마다 다른 속성

### 강사님 코드

출처: `teacher/workspace_python/_12_class.py` 27–49행 · **원본 발췌**

```python
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
```

### 내 코드

출처: `me/workspace_python/12_class.py` 28–52행 · **원본 발췌**

```python
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

```

`Person2('이름', 20)`의 값은 `a.name`, `a.age`에 저장되고, 다른 호출로 만든 `b`에는 별도의 `name`, `age`가 저장된다. `b.addr='천안'`은 **b에만** 속성을 추가한다. `a.addr`를 읽는 줄은 주석 처리된 이유가 있다. 마지막 `b.__init__(1,2)`는 생성자를 **직접 다시 호출**해 `b.name`, `b.age`를 1과 2로 바꾸지만, `b.addr`를 지우지는 않는다. 원래의 정상적인 사용은 객체를 만들 때 자동 호출되는 것이다.

내 메모에는 객체의 “힙 영역”이나 “주소값” 같은 설명이 적혀 있다. 이 단계에서 중요한 것은 메모리 배치의 암기가 아니라 **a와 b가 별개의 인스턴스**라서 한쪽에 넣은 속성이 다른 쪽에 생기지 않는다는 관찰이다.

<a id="section-3"></a>

## 직접 확인할 질문

1. `james = Person()` 주변에서 0, 1, 2는 어떤 순서로 나올까?
2. `b.addr='천안'` 뒤 `a.addr`를 바로 읽으면 어떻게 될까?
3. `james.hello()`가 `greeting()`과 다르게 동작하는 이유는?

<a id="section-4"></a>

## 추가로 알면 좋은 것

인스턴스 속성과 같은 이름의 메서드를 피하는 구체적인 이름 규칙은 원본에서 별도로 구현하지 않았다. 우선 **속성과 호출할 메서드의 이름을 겹치지 않게 짓는다**는 실무적 원칙만 연결해 보자.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/12-01_Python_클래스와_인스턴스_연습문제.md) → [12-02. 클래스 속성과 메서드](12-02_Python_클래스속성과_메서드.md)

