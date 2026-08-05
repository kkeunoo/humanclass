
# class명은 대부분 대문자로 시작 함
# class는 변수가 None이 되거나 지역변수의 역할이 끝나거나 다른 값으로 덮어 씌워질 때 소멸할 때 메모리에서 사라짐
# self는 class가 생성 된 이후에 사용할 수 있음
# 지역변수, self변수, 정적 변수 등 언제 생기고 사라지는지도 잘 알아야 함
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

# 260804_추가수업
print('-'*30)
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

'''
문제1_멜론 차트 관리 시스템 (모든 곡을 리스트로 관리)
1-1. 한 곡에 해당하는 클래스부터 생성
1-2. 제목, 가수, 앨범명, 가사
1-3. 두 곡 이상 정보를 저장
1-4. 각 곡의 제목-가수명으로 출력
'''
print('문제1', '-'*30)
class Melon1 :
    allSong = [] # 이런 형태로 정적 메소드 선언하는건 좋지 않음

    def __init__(self, title, singer, album, words) :
        self.melonList = {
            "title" : title, 
            "singer" : singer, 
            "albem" : album, 
            "words" : words
        }
        Melon1.allSong.append(self.melonList)

    def print_sing(self) :
        print(self.melonList['title'], self.melonList['singer'], sep='-')
   
sing1 = Melon1('LOVE ATTACK', 'RESCENE (리센느)', 'SCENEDROME', '난나나나1')
sing2 = Melon1('갑자기', '아이오아이 (I.O.I)', 'I.O.I 3rd MINI ALBUM [I.O.I : LOOP]', '난나나나2')
sing3 = Melon1('REDRED', 'CORTIS (코르티스)', 'GREENGREEN', '난나나나3')
# sing4 = Melon('테스트', '테스트', '테스트') # 인자값 덜 넣었을 때 테스트

# print(sing1.melonList)
# print(sing2.melonList)
# print(sing3.melonList)
# print(Melon.allSong)

# list배열로 받아서 반복문으로 출력했으면 더 예쁘게 됨
sing1.print_sing()
sing2.print_sing()
sing3.print_sing()

'''
문제2_휴먼잡스 계정 관리 시스템
2-1. 내 계정에는 ID, PW, Addr이 있음
2-2. 모두 접근 제한 된 Private 변수이다
2-3. method를 이용해서 주소를 변경하거나,
     주소를 return하는 method를 만들어라
'''
print('문제2', '-'*30)
class Human :
    def __init__(self) :
        self.__id = ''
        self.__pw = ''
        self.__addr = ''

    def setAccount(self, id, pw, addr) : # 주소만 변경이 문제였기 때문에, 따로 나누어야 함
        self.__id = id
        self.__pw = pw
        self.__addr = addr

    def getAccount(self) :
        return self.__id, self.__pw, self.__addr

human1 = Human()
human1.setAccount('human', 1234, '동남구 대흥동')
# print(human1.__id) # 접근불가 확인
print(human1.getAccount())

'''
문제3_디저트 카페 노티드 창업을 위한 클래스 (__init__)
3-1. 상호, 자본금이 필수 요소
3-2. 노티드를 두 군데에 창업할 것이다
3-3. 하나를 창업할 때 필수 요소를 꼭 넣어야 생성되도록
'''
print('문제3', '-'*30)
class mKnotted : 
    def __init__(self, name, money):
        self.name = name
        self.money = money

k1 = mKnotted('천안점', 20000)
k2 = mKnotted('아산점', 50000)
# k3 = mKnotted('동남점')

print(k1.name, k1.money)
print(k2.name, k2.money)


class Melon :
    def __init__(self) :
        self.songList = []

    def appendSong(self, song) :
        self.songList.append(song)

m = Melon()
m.appendSong(sing1)




