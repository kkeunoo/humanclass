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