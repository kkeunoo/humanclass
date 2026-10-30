numbers = [3, 7, 10, 15, 22, 8, 13]
even = []
odd_total = 0
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd_total += number
print(even, odd_total)
cart = {'사과': {'가격': 1000, '개수': 3}, '바나나': {'가격': 2000, '개수': 4}}
total = 0
for fruit in cart:
    total += cart[fruit]['가격'] * cart[fruit]['개수']
print('작은 장바구니', total)
users = {'admin': '1234', 'guest': 'guest'}
user = 'guest'
password = '1234'
if user not in users:
    print('아이디 없음')
elif users[user] != password:
    print('그 아이디의 비밀번호와 다름')
else:
    print('일치')
