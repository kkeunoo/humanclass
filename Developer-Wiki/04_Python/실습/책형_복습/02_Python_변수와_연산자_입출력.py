price = 1000
typed = input('수량: ')
count = int(typed)
total = price * count
print('총액', total, sep=': ')
print(5 / 2, 5 // 2, -5 // 2)
print(int(-2.4))
a = 10
b = '오백원'
c = a
a = b
b = c
print('첫 교환', a, b)
a, b = b, a
print('둘째 교환', a, b)
x = 4
print(++x, --x, x)
print(1 == 1.0)
print(not False or not True and False)
print('글씨' or '쉬는시간')
print(1, 2, sep='', end='')
print(3)
