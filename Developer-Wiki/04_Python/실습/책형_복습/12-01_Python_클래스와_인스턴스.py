class Person:
    def __init__(self, name, age):
        print('초기화', name)
        self.name = name
        self.age = age
    def greeting(self):
        print(f'{self.name}, {self.age}세')
print('만들기 전')
a = Person('민지', 20)
b = Person('준호', 30)
print('만들기 뒤')
a.greeting()
b.greeting()
a.name = '수정한 이름'
print(a.name, b.name)
c = a
c.age = 21
print(a.age, c is a, a is b)
b.address = '천안'
print(b.address)
