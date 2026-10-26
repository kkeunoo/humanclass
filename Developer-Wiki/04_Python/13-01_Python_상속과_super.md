# 13-01. 상속과 `super()` — 부모 기능 이어받기

[Python 목차](README.md) · [이전: 클래스 과제](12-03_Python_클래스_과제비교.md) · [다음: 재정의와 추상 클래스](13-02_Python_메서드재정의와_추상클래스.md)

양쪽 `13_상속.py`는 `Student(Person)`으로 부모의 메서드를 쓰고, 부모 생성자가 있을 때 `super().__init__()`을 호출하는 예를 연습한다.

<!-- chapter-toc -->

- [1. 부모의 메서드 사용하기](#section-1)
- [2. 자식 생성자에서 부모 생성자 실행하기](#section-2)
- [3. 부모 생성자에 필수 인자가 있을 때](#section-3)
- [직접 확인할 질문](#section-4)
- [추가로 알면 좋은 것](#section-5)

<a id="section-1"></a>

## 1. 부모의 메서드 사용하기

### 강사님 코드

출처: `teacher/workspace_python/_13_상속.py` 2–13행 · **원본 발췌**

```python
class Person:
    def greeting(self) :
        print('안녕하세요')

class Student(Person):
    def study(self):
        print('공부하기')
        self.greeting()

s1 = Student()
s1.study()
s1.greeting()
```

### 내 코드

출처: `me/workspace_python/13_상속.py` 4–15행 · **원본 발췌**

```python
class Person :
    def greeting(self) :
        print('안녕하세요')

class Student(Person) : # class에 클래스명()로 상속을 받아올 수 있음
    def study(self) :
        print('공부하기')
        self.greeting() # 상속을 받으면, 부모에 있는것도 self로 가져올 수 있음

s1 = Student()
s1.study()
s1.greeting()
```

`Student`에는 `study()`만 직접 정의했지만 `Person`을 상속했으므로 `self.greeting()`과 `s1.greeting()`을 호출할 수 있다. `study()`를 한 번 호출하면 `공부하기`와 `안녕하세요`가 나오고, 이어 `s1.greeting()`으로 `안녕하세요`가 한 번 더 나온다. 내 주석의 `s1.hello`는 부모 클래스에도 없는 속성이므로 실행하지 않는다.

<a id="section-2"></a>

## 2. 자식 생성자에서 부모 생성자 실행하기

### 강사님 코드

출처: `teacher/workspace_python/_13_상속.py` 15–39행 · **원본 발췌**

```python
class Person2:
    def __init__(self):
        print('Person2 __init__ 실행')
        self.hello = '방가'

class Student2(Person2):
    def __init__(self):
        print('Student2 __init__ 실행')
        super().__init__()
        self.school = '휴먼'

s2 = Student2()
print( s2.school )
print( s2.hello )


class Student3(Person2):
    # 기본 생성자
    # def __init__(self):
    #     super().__init__()

    def test(self):
        print('테스트')
print('-'*30)
a = Student3()
```

### 내 코드

출처: `me/workspace_python/13_상속.py` 18–52행 · **원본 발췌**

```python
class Person2 :
    def __init__(self) :
        print('Person2 __init__ 실행')
        self.hello = '방가'

class Student2(Person2) :
    def __init__(self) :
        print('Student2 __init__ 실행')
        super().__init__() # 자식도 init을 쓰고 부모의 init이 있을 경우, 가져와서 실행시켜줘야 함
        self.school = '휴먼'
'''
자식이 init(기본 생성자)을 생성하지 않았을 때 
class Person :
    def __init__(self) :
        print('Person2 __init__ 실행')
class Student(Person) :
    pass
    
       ↓

class Student(Person) :
    def __init__(self) :
        super().__init__()

이 자동으로 생성 됨

단, 부모 생성자에 전달 인자가 필수인 경우
직접 __init__을 정의해서 사용해야 한다
'''

s2 = Student2()
print( s2.school )
print( s2.hello )
# print( s2.hello ) # 부모의 init을 실행하기 전이면, 에러 발생 
# (AttributeError: 'Student2' object has no attribute 'hello')
```

`Student2`가 자기 `__init__`을 정의하면 그 안에서 `super().__init__()`을 호출해 부모가 만드는 `hello`를 준비한다. 따라서 `Student2 __init__ 실행` 뒤 `Person2 __init__ 실행`이 출력되고 `s2.hello`를 읽을 수 있다. 반면 강사님 `Student3`은 자기 생성자를 정의하지 않아 부모 `Person2.__init__`이 그대로 사용된다. 내 파일에서는 이 경우를 삼중 따옴표 **설명 메모**로 적었고, 실제 `Student3` 클래스를 만들지는 않았다.

내 메모의 “부모 생성자가 자동으로 생성된다”는 표현은 그대로 받아들이기보다, **자식이 생성자를 따로 정의하지 않으면 부모의 생성자 동작을 이어받는다**고 이해하면 정확하다.

<a id="section-3"></a>

## 3. 부모 생성자에 필수 인자가 있을 때

### 강사님 코드

출처: `teacher/workspace_python/_13_상속.py` 41–55행 · **원본 발췌**

```python
class Person3:
    def __init__(self, str):
        print('Person3 __init__ 실행')
        self.hello = '방가'
        self.str = str

class Student4(Person3):
    # 기본 생성자의
    # super의 __init__ 전달 인자는 없으므로
    # 전달 인자가 필수인 경우 생략 불가능
    def __init__(self):
        super().__init__(None)

s4 = Student4()
print(s4.hello)
```

### 내 코드

출처: `me/workspace_python/13_상속.py` 56–70행 · **원본 발췌**

```python
class Person3 :
    def __init__(self, str) : # 부모가 명백하게 전달인자가 있는 경우, 생략 불가
        print('Person3 __init__ 실행')
        self.hello = '방가'
        self.str = str

class Student4(Person3) :
    # 기본 생성자 super의 __init__ 전달인자는 없으므로,
    # 전달 인자가 필수인 경우 생략할 수 없음
    def __init__(self) :
        super().__init__(None)
    pass

s4 = Student4()
print(s4.hello)
```

`Person3.__init__(self, str)`는 `str` 값을 요구한다. 그래서 두 원본의 `Student4.__init__`은 `super().__init__(None)`처럼 **값 하나를 넘겨** 부모를 초기화한다. 그 뒤 `s4.hello`는 부모가 넣은 `'방가'`다. 여기서 `str`은 매개변수 이름으로 쓴 것이고, Python의 기본형 이름 `str`과 겹친다. 이 예제를 이해할 때는 “부모 생성자에 필요한 인자를 전달한다”는 관계가 핵심이다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `Student`에 `greeting()`이 없어도 호출할 수 있는 이유는?
2. 내 파일에 강사님 `Student3`과 같은 실제 클래스가 있는가?
3. `Student4`가 `super().__init__(None)`을 부르는 이유는?

<a id="section-5"></a>

## 추가로 알면 좋은 것

여러 부모 클래스를 함께 상속할 때 `super()`가 어느 클래스를 찾는지에 대한 상세 규칙은 두 원본의 범위를 넘는다. 여기서는 **한 부모 클래스**를 상속한 실제 호출 순서를 먼저 익힌다.

