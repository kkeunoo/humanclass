# 11-01. 함수와 반환값

[Python 목차](README.md) · [이전: 파일에서 단어 찾기](10-03_Python_파일에서_단어찾기.md) · [다음: 인자 전달](11-02_Python_함수_인자전달.md)

두 원본 `11_fn.py`는 함수를 정의하고 호출한 뒤, 출력과 반환의 차이를 확인한다. **정의한 뒤에 호출해야 한다**는 실행 순서부터 살펴보자.

<!-- chapter-toc -->

- [1. 정의, 호출, 출력과 반환](11-01_Python_함수와_반환값.md#section-1)
- [2. 값을 돌려주지 않는 `return`과 여러 값](11-01_Python_함수와_반환값.md#section-2)
- [3. 함수를 이어 호출하고 리스트를 바꾸기](11-01_Python_함수와_반환값.md#section-3)
- [직접 확인할 질문](11-01_Python_함수와_반환값.md#section-4)
- [추가로 알면 좋은 것](11-01_Python_함수와_반환값.md#section-5)

<a id="section-1"></a>

## 1. 정의, 호출, 출력과 반환

### 강사님 코드

출처: `teacher/workspace_python/_11_fn.py` 1–25행 · **원본 발췌**

```python
# hello()

def hello() :
    print('hello world')
hello()

a = hello
a()

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
```

### 내 코드

출처: `me/workspace_python/11_fn.py` 1–25행 · **원본 발췌**

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
```

`hello()`는 `def hello()`가 실행되어 이름이 만들어진 **뒤에** 호출한다. 내 파일 첫머리의 `# hello()`는 호출 전이었다면 이름 오류가 날 수 있음을 남긴 **주석**이다. `add`는 합을 `print`하지만 반환문이 없어 호출 결과는 `None`이다. `add2`는 합을 `return`하므로 호출한 자리에서 값 `3`을 받을 수 있다. 함수 첫 부분의 문자열은 `add.__doc__`로 읽는다. 내 함수의 두 번째 문자열은 함수 설명의 첫 문자열을 바꾸지 않는다.

강사님은 `a = hello; a()`로 **함수 자체를 변수에 넣어 호출**하는 예도 보여 준다. `a = hello()`처럼 괄호를 붙여 호출한 결과를 담는 것과 구분하자.

<a id="section-2"></a>

## 2. 값을 돌려주지 않는 `return`과 여러 값

### 강사님 코드

출처: `teacher/workspace_python/_11_fn.py` 27–43행 · **원본 발췌**

```python
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

```

### 내 코드

출처: `me/workspace_python/11_fn.py` 27–48행 · **원본 발췌**

```python
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
```

`not_ten(10)`은 `return`만 만나 함수가 끝나므로 `b`는 `None`이다. `add_sub(1,2)`는 `1+2=3`, `1-2=-1`을 **튜플 `(3, -1)`**로 반환한다. `d, e = add_sub(1,2)`는 그 두 값을 나누어 받는다. 내 코드의 `x = add_sub(1,2)`는 함수 안의 지역 변수 `x`를 직접 꺼내 온 것이 아니라 **함수의 반환값 튜플을 새로운 바깥 변수 `x`에 대입**한 것이다. 이 차이를 기억하면 지역 변수 설명과 충돌하지 않는다.

<a id="section-3"></a>

## 3. 함수를 이어 호출하고 리스트를 바꾸기

### 강사님 코드

출처: `teacher/workspace_python/_11_fn.py` 113–141행 · **원본 발췌**

```python
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
```

### 내 코드

출처: `me/workspace_python/11_fn.py` 109–138행 · **원본 발췌**

```python
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
```

`local_var()` 안의 `a2`는 함수 밖에서 바로 읽을 수 없다. 반면 `ref(b)`는 **같은 리스트 객체에 `append(4)`**를 하므로 호출 뒤 `b`는 `[1,2,3,4]`다. 강사님 함수는 바뀐 리스트를 `return`까지 하지만 호출한 자리에서 그 반환값을 저장하지 않는다. 내 함수에는 반환문이 없지만 `append`의 변경은 남는다. 이 현상은 내 주석의 “주소값이 들어간다”보다 **같은 변경 가능한 리스트를 참조한다**고 설명하는 편이 분명하다.

`fn2(fn1(10))`은 안쪽 `fn1`이 먼저 20을 만들고, 바깥 `fn2`가 200을 만든다. `print(fn1)`은 함수를 **호출하지 않고 함수 객체를 출력**하므로 결과 숫자가 나오지 않는다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `add(1,2)`의 화면 출력과 호출 결과는 각각 무엇일까?
2. 내 `x = add_sub(1,2)`에서 바깥 `x`의 자료형은?
3. `ref(b)`의 반환값을 저장하지 않아도 `b`가 바뀌는 이유는?

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/11-01_Python_함수와_반환값_연습문제.md)

## 추가로 알면 좋은 것

함수 객체의 출력에 포함되는 메모리 주소 같은 표시는 실행마다 달라질 수 있다. 이 원본에서는 함수의 **호출과 반환값**을 구분하는 것이 먼저다.

