class Wallet:
    def __init__(self, money):
        self.__money = money
    def pay(self, price):
        self.__money -= price
        return self.__money
wallet = Wallet(10000)
print(wallet.pay(3000))
wallet.__money = 9999999
print(wallet.pay(3000))
class Shop:
    brand = '연습 빵집'
    def __init__(self, branch):
        self.branch = branch
a = Shop('천안')
b = Shop('아산')
print(a.branch, b.branch, Shop.brand)
class Calc:
    @staticmethod
    def add(x, y):
        return x + y
print(Calc.add(1, 2))
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def get_count(cls):
        return cls.count
p1 = Counter()
p2 = Counter()
p3 = Counter()
print(Counter.get_count())
