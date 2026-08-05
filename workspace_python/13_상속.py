
# 캡슐화, 상속, 다형성이 있다면 '객체 지향 언어' 라고 부름

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
# print(s1.hello)

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

# 만약 Person2에 init이 아니고, 일반 함수였다면 불러와서 실행 됨

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

# method override : 자식이 동일한 것을 선언했을 경우,
# 부모에 있던 것을 덮어씀 / 부모가 있는것에서 새로운 기능 등 추가해서 사용하기 위해서
class Person5 :
    def hi(self) :
        print('안녕하시오')

class Student5(Person5) :
    def hi(self) :
        print('야호')

s5 = Student5()
s5.hi()

class Champ :
    def attack(self) :
        print('기본 공격')

class Lux(Champ) :
    def attack(self) :
        super().attack()
        print('데마시~~~~~~아!!!')

class Jax(Champ) :
    def defence(self) :
        print('절대 지켜')

c1 = Lux()
c2 = Jax()
cList = [c1, c2]

for c in cList :
    c.attack()

'''
문제4_부모 Car class가 있음
4-1. 부모에는 
def start(self) :
    print('시동을 켭니다')
def accel(self) :
    print('속도를 높입니다')

4-2. 자식에는 람보르기니
시동걸면 "바랑~"
엑셀을 밟으면 "스~아~앙~'

4-3. 티코 (accel만 override)
시동 걸면 아무것도 없고,
엑셀을 밟으면 "덜덜덜덜"

'''

class Car :
    def start(self) :
        print('시동을 켭니다')

    def accel(self) :
        print('속도를 높입니다')

class Lambo(Car) :
    def start(self) :
        super().start()
        print('Lambo : 바라랑~')

    def accel(self) :
        super().accel()
        print('Lambo : 스아앙~')

class Tico(Car) :
    def accel(self) :
        super().accel()
        print('Tico : 덜덜덜덜')

c1 = Lambo()
c2 = Tico()

carList = [c1, c2]

for c in carList :
    c.start()
    c.accel()

# 추상 클래스 사용하기 (abc.ABCmeta, @abc, @abstractmethod 사용 할 수 있음)
from abc import * 

# @abstractmethod를 사용하려면, metaclass는 사용해주어야 함
class StudentBase(metaclass=ABCMeta) :
    @abstractmethod
    def study(self) :
        pass

    @abstractmethod
    def go_to_school(self) :
        # print(123) 처럼 넣어두어도 override를 자식에서 해야 하기 때문에, 무의미
        pass

class Student(StudentBase) :
    def study(self) :
        print('공부하기')
    def go_to_school(self): # 부모의 abstract method를 강제할 수 있음
        print('학교가기')

a = Student()
# 부모에는 study, go_to_school이 있는데 study만 사용했을 경우 아래와 같은 Error 발생 (abstract 'go_to_school' method를 사용하지 않았다)
# TypeError: Can't instantiate abstract class Student without an implementation for abstract method 'go_to_school'
a.study() 

# 부모에는 'pass'이고 구현되어 있지 않았기 때문에, 생성할 수 없음
# TypeError: Can't instantiate abstract class StudentBase without an implementation for abstract methods 'go_to_school', 'study'
# b = StudentBase()
