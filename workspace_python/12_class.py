
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