# Python 함수

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `11_Python_함수.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `02_Python_변수와_자료형_연산자.md`, `04_Python_리스트와_컴프리헨션.md`, `07_Python_딕셔너리와_집합.md`, `09_Python_반복문.md` |
| 다음 학습 | `12_Python_클래스.md` |
| 원본 기준 | `workspace_python/11_fn.py`, `workspace_teacher/workspace_python/_11_fn.py` |
| 핵심 범위 | 함수 정의와 호출, 매개변수와 인자, `return`, 다중 반환, 위치·키워드 인자, 가변 인자, 언패킹, 기본값, 지역·전역·비지역 변수, 람다, `map()`, 정렬 기준 함수 |
| 보충 범위 | Docstring, 함수 객체, 참조 전달, 함수 합성, 순수 함수, 타입 힌트, 재귀, 이름 충돌, LEGB 규칙 |
| Quiz 처리 | 원본 실습은 본문에서 분석하며, 추가 문제와 상세 풀이 문서는 최종 Quiz 단계에서 별도 제작 |

> 이 문서는 내 코드의 `11_fn.py`와 강사님 코드의 `_11_fn.py`를 직접 비교해 작성했습니다. 두 파일은 함수 선언과 호출, `return`, 여러 값 반환, 위치 인자와 키워드 인자, `*args`, `**kwargs`, 기본값, 리스트 참조, 함수 합성, 람다, `map()`, 정렬, 지역·전역·비지역 변수까지 같은 흐름을 공유합니다. 내 코드는 각 개념에 대한 주석과 실행 결과 분석이 더 많고, 강사님 코드는 함수와 람다 표현을 대응시켜 비교하는 예제가 더 명확합니다.

---

# 학습 목표

- 함수가 특정 작업을 하나의 이름으로 묶는 구조임을 설명할 수 있다.
- 함수를 정의한 뒤 호출해야 실행된다는 점을 이해한다.
- 매개변수와 전달인자의 차이를 구분할 수 있다.
- `return`과 `print()`의 역할을 구분할 수 있다.
- 값 없이 `return`하면 `None`이 반환된다는 점을 안다.
- 여러 값을 반환하면 튜플로 묶인다는 점을 이해한다.
- 위치 인자와 키워드 인자를 구분할 수 있다.
- 리스트와 튜플에 `*`, 딕셔너리에 `**`를 사용해 언패킹할 수 있다.
- `*args`와 `**kwargs`의 자료형과 사용 목적을 설명할 수 있다.
- 기본 매개변수를 올바른 순서로 선언할 수 있다.
- 지역 변수와 전역 변수의 범위를 구분할 수 있다.
- `global`과 `nonlocal`의 역할을 이해한다.
- 함수가 변수에 저장되고 다른 함수에 전달될 수 있음을 설명할 수 있다.
- 람다 표현식이 짧은 함수를 표현하는 문법임을 이해한다.
- `map()`과 정렬의 `key` 인자에 함수를 전달할 수 있다.
- 변경 가능한 객체가 함수 안에서 수정될 수 있음을 이해한다.
- 내 코드와 강사님 코드의 구현 차이를 비교할 수 있다.

---


# 1. 원본 코드

## 1.1 내 코드

```python
# NameError: name 'hello' is not defined. Did you mean: 'help'?
# 선언되기 전에 함수를 먼저 실행하면 Name 에러 발생 (인터프리터로 위부터 한 줄씩 진행되기 때문에)
# hello() 

def hello() :
    print('hello world')

hello()

def add(a, b) :
    "a + b를 출력함"
    print( a + b )
    "a + b를 출력함2"

add(1,2)
print(add.__doc__) # doc는 document의 함수 첫 줄 string을 출력할 수 있음

def add2(a, b) :
    return a + b

c = add2(1, 2)
print(c)

def 아낌없이주는함수() :
    return 100

def not_ten(a) :
    if a == 10 :
        return # return 값이 없을 때 'none' 반환, else처럼 사용할 수 있음
    print(a)

b = not_ten(10)
print('b : ', b)

def add_sub(a,b) :
    x = a + b
    y = a - b
    return x, y

c = add_sub(1, 2) 
print(c, type(c)) # 하나에 받았을 경우 튜플로 반환 됨 (return x,y 가 튜플이기 때문)

d, e = add_sub(1,2)
print(d, type(d), e, type(e)) # 두 곳에 나누어 받았을 땐 튜플이 아닌, 해당 자료형

x = add_sub(1,2) # add_sub에 있는 지역변수이기 때문에 사용할 수 있음
# x = add_sub(1,2,3) # TypeError: add_sub() takes 2 positional arguments but 3 were given 전달인자가 넘었을 때 발생
print(x)

def print_numbers(a, b, c) :
    print(a)
    print(b)
    print(c)
print_numbers(10, 20, 30)

a = [1,2,3]
print(a)
print(*a) # 1, 2, 3 이 들어간 것과 같음
# print_numbers(a) # TypeError: print_numbers() missing 2 required positional arguments: 'b' and 'c'
print_numbers(*a)

# 전달인자에 *를 붙일 경우 'tuple'로 반환해 줌, '가변인수'라고 부름
def print_numbers2(*a) :
    print(type(a), a)
    for b in a :
        print(b)

print_numbers2(1)
print_numbers2(1,2,3,4)

# def print_numbers3(*a, c) : # 어디까지가 c인지 분간이 어렵기 때문에, *은 뒤에
def print_numbers3(c, *a) :
    print(c)
    for b in a :
        print(b)
print_numbers3(1,2,3,4)

def minus(x, y) :
    print(x - y)

minus(5,2)
minus(y=5,x=2) # keyword를 지정하면 순서에 상관없이 넣을 수 있음

x = {
    'name' : '정근욱',
    'age' : 30
}

def info(age, name) :
    print(age,name)

# info(x) # 전달인자가 1개이기 때문에 불가
info(*x) # 딕셔너리의 경우 list와 tuple처럼 * 한개를 쓰면 key값만 나옴 (.keys()와 같다)
info(**x) # key=value 형태로 출력 됨

def info2(**a) :
    for k, v in a.items() :
        print(k,v)

info2(**x)

def info3(name, age, addr='비공개') : # 함수에 기본값을 지정할 수 있음
    print(name, age, addr)
info3(1,2,3)
info3(1,2) # 기본값을 지정해두었을 때 전달인자를 안 줘도 오류 없이 기본값 출력

# 재귀호출 예시는 없으나, 폴더 내 전체 자료를 찾는 등 (폴더면 호출해서 또 들어감)에 쓰임

def local_var() :
    a2 = 10
    print(a2)

local_var()
# print(a2) # local_var의 지역변수이기 때문에 사용 불가

def ref(a) :
    a.append(4)

b = [1,2,3]
ref(b) # 전달인자 또는 =으로 가게되면 stack의 주소값이 들어감 + 원본 변경
print(b)

def fn1(a) :
    return a + 10
def fn2(a) :
    return a * 10

c = 10
b = fn1(c) # 20
print(b)
d = fn2(b) # 200
print(d)

e = fn2( fn1(c) )
print(e)

# 전달인자에 함수 자체만 주었을 때 변수 취급하며 껍데기가 나옴( <function fn1 at 0x0000021CF3C13CC0> )
print(fn1)

def ten(x) :
    return x + 10
print( ten(5) )

ten2 = lambda x: x + 10 # 람다표현식으로 사용할 수 있음
print( ten2(5) )
print( (lambda x: x + 10)(5) )

a = ['1','2']
b = [int(a[0]), int(a[1])]
c = list(map(int, a))
print(a, b, c)

d = list(map(ten2,c)) # 아래와 같이 lambda식을 바로 넣을 수 있음
print(d)

e = list(map(lambda x: x + 10,c)) 
print(e)


sqr = lambda x: x ** 2
print(sqr(3))

sum = lambda x, y: x + y
print(sum(3,5))

info = [{
        'name' : '이름1',
        'age' : 25
    }, {
        'name' : '이름2',
        'age' : 23
    }, {
        'name' : '이름3',
        'age' : 30
    }]
#함수로 나이만 출력

# print(*info[0].values())

def age(info) :
    for i in info :
        print(*i.values())

age(info)

def print_age(info) :
    for p in info :
        print(p['age'])
print_age(info)

print_age2 = lambda info : [p['age'] for p in info]
print(print_age2(info))

info.sort(key = lambda x : x['age'])
print(info)

x = 10
def foo() :
    x = 20
    print('foo 안에서 x:', x) # 안에 선언 된 지역변수가 있으면, 해당 값을 가져옴
foo()
print('foo 밖에서 x:', x) # 전역변수를 가져오기 때문에, 10이 됨

def foo2() :
    print('foo 안에서 선언없음 x:', x) # 안에 선언 된 지역변수가 없으면, 전역변수 값을 가져옴
foo2()

def foo3() :
    global x # global로 전역변수 값을 바꿀 수 있음
    x = 20
foo3()
print('foo3 이후의 x:', x)

# 함수 안에서 변수 우선 순위
'''
    1. 먼저 지역 변수 찾기
    2. 없으면 전역 변수 찾기
    3. 없으면 에러(not defined)
'''

x = 10
def test(z) :
    return z + 2
x = test(x)

def test2() :
    global x
    x = x+2

x = 10
y = 20
def test3() :
    global x, y # global 함수에 2개도 지정할 수 있음
    x = 11 
    y = 12
test3()
print(x, y)

# nonlocal로 윗 부모에게 찾아갈 수 있음
def A():
    x = 10
    y = 20

    def B():
        x = 30

        def C():
            nonlocal x, y
            print(x)
            print(y)
        C()

    B()

A()
```

## 1.2 강사님 코드

```python
# hello()

def hello() :
    print('hello world')
hello()

def add(a, b) :
    # __doc__
    # 함수 첫줄의 주석 글씨를 출력해준다
    "a + b를 출력"
    print( a+b )
add(1,2)
print(add.__doc__)

def add2(a,b) :
    return a+b

c = add2(1,2)
print(c)

def 아낌없이주는함수() :
    return 100

def not_ten(a) :
    if a == 10 :
        return
    print(a)

b = not_ten(10)
print('b:', b)

def add_sub(a, b):
    x = a + b
    y = a - b
    # return (x, y)
    return x, y
c = add_sub(1, 2)
print(type(c), c)
d, e = add_sub(1, 2)

# x = add_sub(1,2, 3)

def print_numbers(a,b,c) :
    print(a)
    print(b)
    print(c)
a = [1,2,3]
print(a)
print(*a)
# print_numbers(a)
print_numbers(*a)

def print_numbers2(*a) :
    print( type(a), a )
    for b in a :
        print(b)

print_numbers2(1)
print_numbers2(1,2,3,4)

def print_numbers3(c, *a) :
    print(c)
    for b in a :
        print(b)
# def print_numbers4(*a, c) :

def minus(x, y) :
    print(x-y)

minus(5, 2)
minus(y=5, x=2)

x = {
    'name': '최민수',
    'age': 20
}
def info(age, name):
    print(age, name)

info(*x) # 딕셔너리의 경우 *는 key만 추출 (.keys()와 같다)
info(**x) # key=value, key=value
# dict(name='민수', age=10)

def info2(**a):
    for k, v in a.items() :
        print(k, v)
info2(**x)

def info3(name, age, addr='비공개') :
    print(name, age, addr)

info3(1,2,3)
info3(1,2)


'''

def 파일출력(경로) :
    경로 안의 모든 목록 뽑아오기
    if not folder :
        print(경로, 파일명)
    elif folder :
         파일출력(folder)

'''

def local_var():
    a2 = 10
    print(a2)

local_var()
# print(a2) # a2는 local_var의 지역 변수라서 현 시점엔 없다

def ref(a) :
    a.append(4)
    return a

b = [1,2,3]
ref(b)
print(b)

def fn1(a) :
    return a + 10
def fn2(a) :
    return a * 10
c = 10
b = fn1(c) # 20
d = fn2(b) # 200
print(d)

e = fn2( fn1(c) )
print(e)

print( fn1 )
# print = 2

def ten(x) :
    return x + 10

ten2 = lambda x : x+10
print( ten2(5) )
print( (lambda x : x+10)(5) )


a = ['1', '2']
b = [int(a[0]), int(a[1])]
c = list( map(int, a) )
print(a, b, c)

d = list(  map(ten2, c)  )
print(d)

e = list(  map(lambda x : x+10, c)  )
print(e)


def square(x) :
    # return x * x
    return x ** 2

def sum(x, y):
    return x + y
print(square(3)) # 9
print(sum(3, 5)) # 8
# lambda로 변경해보자
sqr = lambda x : x**2
add = lambda x,y : x+y
print( sqr(3) )    # 9
print( add(3, 5) ) # 8

info = [
    {
        'name': '이름1', 
        'age' : 25
    }, {
        'name': '이름2', 
        'age' : 23
    }, {
        'name': '이름3', 
        'age' : 30
    }]
# 함수로
# 나이만 출력
def print_age(info) :
    for p in info :
        print(p['age'])
print_age(info)
# lambda로도 만들어보자
print_age2 = lambda info : [p['age'] for p in info]
print(print_age2(info))

def age(info):
    return info['age']
info.sort(key = age)
info.sort(key = lambda x : x['age'])
print(info)

x = 10 # 전역변수, global 변수
def foo():
    x = 20  # 지역변수
    print('foo 안에서 x:', x)
foo()
print('foo 밖에서 x:', x)

def foo2():
    print('foo2 안에서 x:', x) #전역 변수 읽기는 됨
foo2()

def foo3():
    global x
    x = 20
foo3()
print('foo3 이후에 x:', x)

# 함수 안에서 변수 우선 순위
'''
    1. 먼저 지역 변수 찾기
    2. 없으면 전역 변수 찾기
    3. 없으면 에러 
'''
x = 10
def test(z):
    return z + 2
x = test(x)

def test2():
    global x
    x = x+2

x = 10
y = 20
def test3():
    global x, y
    x = 11
    y = 12


def A():
    x = 10
    y = 20

    def B():
        x = 30

        def C():
            nonlocal x, y
            print(x)
            print(y)
        C()

    B()

A()
```

---


# 2. 함수란?

함수는 관련된 코드를 하나의 이름으로 묶은 재사용 가능한 코드 블록입니다.

```text
입력
→ 함수 내부 처리
→ 결과 반환
```

함수를 사용하면 중복을 줄이고 코드의 역할을 분리할 수 있습니다.

---

# 3. 함수 정의

```python
def hello():
    print("hello world")
```

구성:

| 요소 | 의미 |
| --- | --- |
| `def` | 함수 정의 키워드 |
| `hello` | 함수 이름 |
| `()` | 매개변수 작성 위치 |
| `:` | 함수 블록 시작 |
| 들여쓰기 | 함수 내부 코드 |

---

# 4. 함수 호출

```python
hello()
```

함수는 정의만으로 실행되지 않습니다. 함수 이름 뒤에 괄호를 붙여 호출해야 합니다.

---

# 5. 정의 전에 호출하면 발생하는 오류

```python
hello()

def hello():
    print("hello")
```

Python은 위에서 아래로 실행되므로 호출 시점에 함수가 정의되어 있지 않으면 `NameError`가 발생합니다.

---

# 6. 매개변수와 전달인자

```python
def add(a, b):
    return a + b

result = add(1, 2)
```

| 용어 | 예 | 의미 |
| --- | --- | --- |
| 매개변수 | `a`, `b` | 함수 정의에서 입력을 받는 변수 |
| 전달인자 | `1`, `2` | 함수 호출 시 실제로 전달하는 값 |

---

# 7. Docstring

원본:

```python
def add(a, b):
    "a + b를 출력함"
    print(a + b)
```

함수 본문의 첫 문자열은 Docstring으로 사용됩니다.

```python
print(add.__doc__)
```

권장 형식:

```python
def add(a: int, b: int) -> int:
    """두 정수를 더한 결과를 반환한다."""
    return a + b
```

---

# 8. `print()`와 `return`

```python
def add(a, b):
    print(a + b)
```

이 함수는 결과를 화면에 출력하지만 호출한 곳에 값을 돌려주지 않습니다.

```python
def add(a, b):
    return a + b
```

이 함수는 결과를 호출한 곳에 반환합니다.

---

# 9. 반환값 저장

```python
result = add(1, 2)
print(result)
```

`return`한 값은 변수에 저장하거나 다른 식에 바로 사용할 수 있습니다.

---

# 10. 값 없는 `return`

```python
def not_ten(number):
    if number == 10:
        return

    print(number)
```

값 없이 `return`하면 함수가 즉시 종료되고 `None`이 반환됩니다.

---

# 11. 조기 반환

```python
def divide(a, b):
    if b == 0:
        return None

    return a / b
```

조건을 만족하지 않을 때 일찍 함수를 종료하면 중첩을 줄일 수 있습니다.

---

# 12. 여러 값 반환

```python
def add_sub(a, b):
    return a + b, a - b
```

실제로는 튜플이 반환됩니다.

```python
result = add_sub(1, 2)
print(result)
print(type(result))
```

---

# 13. 반환값 언패킹

```python
add_result, sub_result = add_sub(1, 2)
```

튜플의 각 값을 여러 변수에 나누어 저장할 수 있습니다.

---

# 14. 위치 인자

```python
def minus(x, y):
    return x - y

minus(5, 2)
```

전달한 순서대로 매개변수에 들어갑니다.

---

# 15. 키워드 인자

```python
minus(y=5, x=2)
```

매개변수 이름을 지정하면 호출 순서와 관계없이 값을 전달할 수 있습니다.

---

# 16. 인자 개수 오류

```python
def add(a, b):
    return a + b

add(1, 2, 3)
```

정의된 매개변수보다 많은 인자를 전달하면 `TypeError`가 발생합니다.

---

# 17. 시퀀스 언패킹 `*`

원본:

```python
numbers = [10, 20, 30]
print_numbers(*numbers)
```

`*numbers`는 리스트 요소를 각각의 위치 인자로 펼칩니다.

```text
[10, 20, 30]
→ 10, 20, 30
```

---

# 18. 딕셔너리에 `*`

```python
person = {
    "name": "정근욱",
    "age": 30,
}

info(*person)
```

딕셔너리에 `*`를 사용하면 키가 펼쳐집니다.

```text
"name", "age"
```

---

# 19. 딕셔너리에 `**`

```python
info(**person)
```

`**`는 딕셔너리를 키워드 인자로 펼칩니다.

```text
name="정근욱", age=30
```

딕셔너리 키와 함수 매개변수 이름이 일치해야 합니다.

---

# 20. 가변 위치 인자 `*args`

```python
def print_numbers(*args):
    print(type(args))
    print(args)
```

`*args`는 전달된 여러 위치 인자를 튜플로 받습니다.

```python
print_numbers(1, 2, 3)
```

---

# 21. `args`라는 이름은 관례

다음 코드도 문법적으로 가능합니다.

```python
def print_numbers(*values):
    print(values)
```

중요한 것은 변수 이름이 아니라 앞의 `*`입니다.

---

# 22. 일반 매개변수와 `*args`

```python
def print_numbers(first, *others):
    print(first)
    print(others)
```

일반 위치 매개변수를 먼저 쓰고 가변 위치 인자를 뒤에 배치합니다.

---

# 23. 가변 키워드 인자 `**kwargs`

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
```

`**kwargs`는 여러 키워드 인자를 딕셔너리로 받습니다.

---

# 24. 기본 매개변수

```python
def info(name, age, address="비공개"):
    print(name, age, address)
```

호출 시 값을 생략하면 기본값이 사용됩니다.

```python
info("홍길동", 20)
```

---

# 25. 기본값 매개변수 순서

기본값이 없는 매개변수는 기본값이 있는 매개변수보다 앞에 와야 합니다.

잘못된 예:

```python
def info(name="익명", age):
    pass
```

올바른 예:

```python
def info(age, name="익명"):
    pass
```

---

# 26. 지역 변수

```python
def local_var():
    value = 10
    print(value)
```

함수 안에서 만든 변수는 기본적으로 함수 내부에서만 사용할 수 있습니다.

---

# 27. 전역 변수

```python
value = 10

def show_value():
    print(value)
```

함수 내부에 같은 이름의 지역 변수가 없으면 전역 변수를 읽을 수 있습니다.

---

# 28. 지역 변수 우선

```python
value = 10

def show_value():
    value = 20
    print(value)
```

함수 안의 `value`는 지역 변수이므로 전역 변수와 별개입니다.

---

# 29. `global`

```python
value = 10

def change_value():
    global value
    value = 20
```

`global`은 함수 내부에서 전역 변수에 값을 대입하겠다고 선언합니다.

과도하게 사용하면 함수의 외부 상태 의존성이 커지므로 가능한 한 반환값을 사용하는 편이 좋습니다.

---

# 30. `nonlocal`

중첩 함수에서 가장 가까운 바깥 함수의 변수를 수정할 때 사용합니다.

```python
def outer():
    value = 10

    def inner():
        nonlocal value
        value = 20

    inner()
    print(value)
```

---

# 31. LEGB 규칙

Python은 이름을 다음 순서로 찾습니다.

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

원본의 지역·전역·`nonlocal` 실습은 이 규칙을 보여 줍니다.

---

# 32. 변경 가능한 객체 전달

원본:

```python
def ref(values):
    values.append(4)

numbers = [1, 2, 3]
ref(numbers)
print(numbers)
```

리스트는 변경 가능한 객체이므로 함수 내부에서 수정하면 원본에도 반영됩니다.

---

# 33. 새 객체 대입과 내부 수정의 차이

```python
def replace(values):
    values = [9, 9, 9]
```

매개변수에 새 리스트를 대입하는 것은 외부 변수 자체를 바꾸지 않습니다.

```python
def mutate(values):
    values.append(9)
```

리스트 객체 내부를 수정하면 호출한 쪽에서도 변경이 보입니다.

---

# 34. 함수 합성

원본:

```python
def fn1(value):
    return value + 10

def fn2(value):
    return value * 10

result = fn2(fn1(10))
```

한 함수의 반환값을 다른 함수의 입력으로 전달할 수 있습니다.

---

# 35. 함수도 객체다

```python
print(fn1)
```

함수를 호출하지 않고 이름만 사용하면 함수 객체 자체를 가리킵니다.

```python
operation = fn1
print(operation(5))
```

---

# 36. 람다 표현식

```python
ten = lambda x: x + 10
```

다음 일반 함수와 같은 역할입니다.

```python
def ten(x):
    return x + 10
```

람다는 하나의 표현식만 작성할 수 있습니다.

---

# 37. 람다를 적합하게 사용하는 곳

람다는 짧고 한 번만 사용할 함수에 적합합니다.

```python
numbers.sort(key=lambda number: -number)
```

복잡한 로직은 일반 함수로 작성하는 편이 가독성이 좋습니다.

---

# 38. `map()`

```python
values = ["1", "2"]
numbers = list(map(int, values))
```

`map()`은 반복 가능한 객체의 각 요소에 함수를 적용합니다.

```text
"1" → int("1") → 1
"2" → int("2") → 2
```

---

# 39. `map()`과 리스트 컴프리헨션

```python
numbers = list(map(int, values))
```

```python
numbers = [int(value) for value in values]
```

둘 다 가능하며, 단순 변환 함수는 `map()`, 조건이나 복합 표현이 있으면 리스트 컴프리헨션이 읽기 쉬운 경우가 많습니다.

---

# 40. 정렬의 `key`

```python
people.sort(key=lambda person: person["age"])
```

`key`에는 각 요소에서 정렬 기준값을 반환하는 함수를 전달합니다.

---

# 41. 원본의 나이 출력 함수

```python
def print_age(people):
    for person in people:
        print(person["age"])
```

함수는 출력 역할만 담당합니다.

람다 버전:

```python
get_ages = lambda people: [person["age"] for person in people]
```

람다 버전은 나이 목록을 반환합니다.

두 코드는 출력과 반환이라는 역할이 다릅니다.

---

# 42. 내 코드의 장점

- 각 개념의 실행 결과와 오류 원인을 주석으로 기록했다.
- `*`, `**`, `*args`, `**kwargs`의 차이를 직접 비교했다.
- 전역·지역·비지역 변수까지 단계적으로 실습했다.
- 함수 합성과 함수 객체를 확인했다.
- `map()`, 람다, 정렬 기준을 연결했다.
- 원본 리스트 변경 여부를 직접 확인했다.

---

# 43. 내 코드 개선점

- `sum`이라는 변수 이름은 내장 함수 `sum()`을 가린다.
- `info`라는 함수 이름을 뒤에서 리스트 변수로 다시 사용한다.
- 한 파일에 너무 많은 개념이 연속되어 있어 함수별 구역 분리가 필요하다.
- 출력용 함수와 반환용 함수의 목적이 일부 혼재되어 있다.
- 타입 힌트와 Docstring을 일관되게 적용할 수 있다.
- 전역 변수 수정 예제는 학습 목적 외 실제 코드에서는 최소화하는 편이 좋다.

---

# 44. 강사님 코드의 장점

- 일반 함수와 람다 표현을 나란히 비교한다.
- `*args`, `**kwargs`, 딕셔너리 언패킹 예제가 명확하다.
- 정렬 기준 함수를 일반 함수와 람다 두 방식으로 보여 준다.
- 지역 변수, 전역 변수, `global`, `nonlocal`의 흐름이 단계적이다.
- 재귀 함수의 용도를 폴더 탐색 예시로 제시한다.

---

# 45. 재귀 함수

함수가 자기 자신을 호출하는 구조입니다.

```python
def countdown(number):
    if number == 0:
        return

    print(number)
    countdown(number - 1)
```

재귀 함수에는 반드시 종료 조건이 필요합니다.

---

# 46. 타입 힌트를 적용한 함수

```python
def add(a: int, b: int) -> int:
    return a + b
```

타입 힌트는 실행을 강제하지 않지만 함수의 입력과 반환 의도를 명확하게 보여 줍니다.

---

# 47. 순수 함수

같은 입력에 항상 같은 결과를 반환하고 외부 상태를 변경하지 않는 함수입니다.

```python
def calculate_total(price: int, quantity: int) -> int:
    return price * quantity
```

순수 함수는 테스트와 재사용이 쉽습니다.

---

# 48. 실무형 함수 예제

```python
def get_adult_names(
    people: list[dict[str, object]],
) -> list[str]:
    """성인 사용자 이름 목록을 반환한다."""
    return [
        str(person["name"])
        for person in people
        if int(person["age"]) >= 19
    ]
```

---

# 49. 자주 하는 실수

### 49.1 함수 정의 전에 호출

`NameError`가 발생합니다.

### 49.2 `print()`한 값을 반환값으로 착각

`return`이 없으면 반환값은 `None`입니다.

### 49.3 인자 개수 불일치

`TypeError`가 발생합니다.

### 49.4 `*`와 `**` 혼동

`*`는 위치 인자, `**`는 키워드 인자 언패킹입니다.

### 49.5 딕셔너리 키와 매개변수 이름 불일치

`**dict` 호출 시 `TypeError`가 발생합니다.

### 49.6 기본값 매개변수 순서 오류

기본값 없는 매개변수가 뒤에 오면 문법 오류가 발생합니다.

### 49.7 변경 가능한 기본값 사용

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

호출 사이에 리스트가 공유될 수 있습니다.

권장:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

### 49.8 내장 함수 이름 덮어쓰기

`sum`, `list`, `dict`, `print` 등을 변수명으로 사용하지 않는 것이 좋습니다.

---

# 50. 면접·복습 포인트

### Q1. 매개변수와 전달인자의 차이는 무엇인가요?

매개변수는 함수 정의에서 입력을 받는 변수이고, 전달인자는 호출 시 실제로 넘기는 값입니다.

### Q2. `return`과 `print()`의 차이는 무엇인가요?

`print()`는 화면에 출력하고, `return`은 호출한 곳에 값을 돌려줍니다.

### Q3. 여러 값을 반환하면 어떤 자료형이 되나요?

튜플로 묶여 반환됩니다.

### Q4. `*args`의 자료형은 무엇인가요?

튜플입니다.

### Q5. `**kwargs`의 자료형은 무엇인가요?

딕셔너리입니다.

### Q6. `global`과 `nonlocal`의 차이는 무엇인가요?

`global`은 전역 변수를, `nonlocal`은 가장 가까운 바깥 함수의 변수를 대상으로 합니다.

### Q7. 함수도 변수에 저장할 수 있나요?

가능합니다. Python에서 함수는 일급 객체입니다.

### Q8. 람다는 언제 사용하나요?

짧고 단순하며 한 번만 필요한 함수를 표현할 때 사용합니다.

---

# 최종 정리

```text
함수를 정의한다.
→ 입력은 매개변수로 받는다.
→ 처리 결과는 return으로 반환한다.
→ *와 **로 인자를 언패킹한다.
→ 가변 인자는 튜플과 딕셔너리로 받는다.
→ 변수 범위는 LEGB 규칙으로 이해한다.
→ 짧은 기준 함수는 람다로 표현할 수 있다.
```
