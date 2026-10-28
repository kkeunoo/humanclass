# 11-02. 함수에 값을 전달하는 여러 방법

[Python 목차](README.md) · [이전: 함수와 반환값](11-01_Python_함수와_반환값.md) · [다음: `lambda`와 범위](11-03_Python_lambda와_변수범위.md)

인자를 넣는 방법을 한꺼번에 외우기보다 **정해진 개수 → 리스트 풀기 → 가변 인자 → 키워드 인자** 순서로 보면 두 원본의 예제가 연결된다.

## 먼저: 매개변수와 인자 구분

함수를 **정의할 때 받는 이름**은 매개변수, **호출할 때 실제로 넣는 값**은 인자다.

```python
# 수업 문법으로 만든 설명용 재구성
def greet(name, word='안녕'):
    print(name, word)

greet('민지')       # 민지 안녕
greet('민지', '반가워')  # 민지 반가워
```

두 번째 값을 생략했을 때만 기본값을 쓴다. 원본의 `*a`와 `**...`는 **몇 개를 어떤 이름으로 받는가**를 확장한 것이므로 이 기본 호출을 먼저 이해하자.

<!-- chapter-toc -->

- [1. 위치 인자, `*`로 풀기, 가변 인자](11-02_Python_함수_인자전달.md#section-1)
- [2. 키워드 인자와 딕셔너리 풀기](11-02_Python_함수_인자전달.md#section-2)
- [직접 확인할 질문](11-02_Python_함수_인자전달.md#section-3)
- [추가로 알면 좋은 것](11-02_Python_함수_인자전달.md#section-4)

<a id="section-1"></a>

## 1. 위치 인자, `*`로 풀기, 가변 인자

### 강사님 코드

출처: `teacher/workspace_python/_11_fn.py` 46–69행 · **원본 발췌**

```python
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
print_numbers2()

def print_numbers3(c, *a) :
    print(c)
    for b in a :
        print(b)
# def print_numbers4(*a, c) :
```

### 내 코드

출처: `me/workspace_python/11_fn.py` 50–76행 · **원본 발췌**

```python
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
```

`print_numbers(a,b,c)`는 세 값을 요구한다. `print_numbers(*[1,2,3])`의 `*`는 **리스트의 세 값을 각각 인자로 풀어** 넣는다. 반대로 `def print_numbers2(*a)`의 `*a`는 전달된 여러 위치 인자를 **튜플로 모은다**. 내 주석의 “전달인자에 `*`를 붙이면 튜플로 반환”은 정의할 때와 호출할 때의 역할을 섞어 쓴 것이다.

내 파일에 적힌 `def print_numbers3(*a, c)`는 문법상 **가능하다**. 다만 `c`를 호출할 때 `c=...`처럼 키워드로 전달해야 하므로, 초반 예제에서는 `def print_numbers3(c, *a)`가 읽기 쉽다. 강사님도 그 순서로 정의했다.

<a id="section-2"></a>

## 2. 키워드 인자와 딕셔너리 풀기

### 강사님 코드

출처: `teacher/workspace_python/_11_fn.py` 71–99행 · **원본 발췌**

```python
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
    return 1

info2(**x)

def info3(name, age, addr='비공개') :
    print(name, age, addr)

info3(1,2,3)
info3(1,2)
```

### 내 코드

출처: `me/workspace_python/11_fn.py` 78–105행 · **원본 발췌**

```python
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
```

`minus(y=5, x=2)`는 이름을 붙여 보내므로 선언 순서와 관계없이 `2-5=-3`을 출력한다. 딕셔너리 `x`를 `info(*x)`로 넣으면 **키 이름 두 개**가 위치 인자로 전달되어 `age='name'`, `name='age'`처럼 들어간다. `info(**x)`는 키를 **매개변수 이름**에 맞춰 전달해 실제 나이와 이름을 넣는다. `def info2(**a)`는 이렇게 전달된 여러 키워드 인자를 딕셔너리로 모은다.

`info3(name, age, addr='비공개')`에서 세 번째 값을 생략하면 `'비공개'`가 사용된다. 내 코드의 `info3(1,2)`는 이름에 숫자 1을 넣는 호출이지만, 이 함수는 자료형을 검사하지 않아 그대로 출력한다. 예제의 의도는 **기본값 적용**이다.

<a id="section-3"></a>

## 직접 확인할 질문

1. 호출하는 쪽의 `*a`와 정의하는 쪽의 `*a`는 어떻게 다를까?
2. 같은 딕셔너리 `x`를 `info(*x)`와 `info(**x)`에 넣으면 무엇이 출력될까?
3. `minus(y=5, x=2)`의 계산 순서는?

<a id="section-4"></a>

## 추가로 알면 좋은 것

매개변수를 위치 전용·키워드 전용으로 세밀하게 제한하는 문법은 이 원본의 중심이 아니다. 여기서는 **양쪽 코드가 실제로 호출한 인자 전달 방식**만 익히자.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/11-02_Python_함수_인자전달_연습문제.md) → [11-03. lambda와 변수 범위](11-03_Python_lambda와_변수범위.md)

