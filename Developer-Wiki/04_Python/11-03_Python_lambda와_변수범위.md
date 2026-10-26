# 11-03. `lambda`, `map`, 정렬과 변수의 범위

[Python 목차](README.md) · [이전: 인자 전달](11-02_Python_함수_인자전달.md)

두 원본은 짧은 함수를 `lambda`로 표현하고 `map`·정렬에 사용한다. 뒤에서는 함수 안팎의 같은 이름이 어느 값을 가리키는지 `global`·`nonlocal`로 확인한다.

<!-- chapter-toc -->

- [1. `lambda`와 `map`](#section-1)
- [2. 나이 출력과 정렬 기준 함수](#section-2)
- [3. 지역 변수, 전역 변수, 바깥 함수의 변수](#section-3)
- [직접 확인할 질문](#section-4)
- [추가로 알면 좋은 것](#section-5)

<a id="section-1"></a>

## 1. `lambda`와 `map`

### 강사님 코드

출처: `teacher/workspace_python/_11_fn.py` 143–175행 · **원본 발췌**

```python
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
```

### 내 코드

출처: `me/workspace_python/11_fn.py` 140–165행 · **원본 발췌**

```python
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

```

`lambda x: x+10`은 값을 하나 받아 10을 더해 **돌려주는 짧은 함수**다. `map(int, ['1','2'])`은 각 문자열에 `int`를 적용하고, 원본은 `list(...)`로 결과를 확인한다. `map(ten2, c)`는 각 숫자에 10을 더한다. 강사님은 `square`, `sum` 함수를 `lambda` 버전과 비교하고, 나는 `sqr`, `sum`을 `lambda`로 직접 작성했다. 여기서 `sum`이라는 이름은 Python의 기본 제공 `sum`도 가리킬 수 있어, 학습 예시에서는 **이름이 겹친다**는 점을 알아 두면 좋다.

<a id="section-2"></a>

## 2. 나이 출력과 정렬 기준 함수

### 강사님 코드

출처: `teacher/workspace_python/_11_fn.py` 177–202행 · **원본 발췌**

```python
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
```

### 내 코드

출처: `me/workspace_python/11_fn.py` 166–195행 · **원본 발췌**

```python
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
```

`print_age(info)`는 각 딕셔너리의 `'age'` 값을 출력한다. `print_age2 = lambda info: [p['age'] for p in info]`는 나이 목록을 **반환**하므로, 두 코드 모두 `print(print_age2(info))`처럼 결과를 출력한다. 강사님은 `info.sort(key=age)`와 `key=lambda ...`를 둘 다 실행하고, 나는 `lambda` 버전만 실행한다. 둘 다 `'age'` 값으로 오름차순 정렬하므로 결과는 23, 25, 30세 순서다.

<a id="section-3"></a>

## 3. 지역 변수, 전역 변수, 바깥 함수의 변수

### 강사님 코드

출처: `teacher/workspace_python/_11_fn.py` 204–260행 · **원본 발췌**

```python
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

### 내 코드

출처: `me/workspace_python/11_fn.py` 197–255행 · **원본 발췌**

```python
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

처음 `x=10`일 때 `foo()` 안의 `x=20`은 **별도의 지역 변수**라서 함수 밖 `x`는 여전히 10이다. `foo2()`는 함수 안에 `x`를 새로 지정하지 않아 밖의 값을 읽는다. `foo3()`는 `global x`를 써서 밖의 `x`를 20으로 바꾼다.

아래의 `A`–`B`–`C`에서는 `nonlocal x, y`가 바로 바깥 한 단계만 무조건 가리킨다는 뜻이 아니다. `C`에서 가장 가까운 **함수를 둘러싼 범위**의 `x`는 `B`의 30, `y`는 `A`의 20이다. 이 파일에서 실행하는 일은 두 값을 **읽어 출력**하는 것이다. 내 코드의 `test3()`은 호출해 전역 `x`, `y`를 바꾸고 출력하지만, 강사님 파일은 `test3`을 **정의만** 해 두었다. 그래서 두 파일 끝부분의 실제 실행 흐름을 같다고 보면 안 된다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `lambda` 함수 자체를 전달하는 것과 그 호출 결과를 전달하는 것은 어떻게 다를까?
2. `foo()`를 호출한 직후 함수 밖 `x`는 몇일까?
3. `C()` 안에서 `nonlocal`로 찾아 읽는 `x`, `y`는 각각 어디에 있을까?

<a id="section-5"></a>

## 추가로 알면 좋은 것

이 범위 찾기 규칙을 더 복잡한 중첩 함수나 클로저 구현으로 넓히는 것은 이 원본의 학습 목표가 아니다. 실제 실행된 예제의 **어느 이름을 읽고 바꾸는지**부터 추적하자.

