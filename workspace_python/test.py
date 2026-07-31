'''
product = "키보드"
price = 89000
quantity = 2
amount = price * quantity

print(f"상품명 : {product}")
print(f"단가   : {price:>10,}원")
print(f"수량   : {quantity:>10}개")
print(f"합계   : {amount:>10,}원")
'''

'''
문제1
numbers = [3, 7, 10, 15, 22, 8, 13]
문제1-1 : 짝수만 따로 리스트로 만들어서 출력
문제1-2 : 홀수의 합

numbers = [3, 7, 10, 15, 22, 8, 13]

even = []
odd = []
for number in numbers :
    if number % 2 == 0 :
        even.append(number)
    elif number % 2 != 0 :
        odd.append(number)

print(even)
print(odd, sum(odd))
'''

'''
문제 2
cart = {
    '사과': {
        '가격': 1000,
        '개수': 3
    },
    '바나나': {
        '가격': 2000,
        '개수': 4
    },
    '복숭아': {
        '가격': 1500,
        '개수': 2
    },
    '키위': {
        '가격': 2200,
        '개수': 5
    }
}
다 샀을 때 가격은?

cart = {
    '사과': {
        '가격': 1000,
        '개수': 3
    },
    '바나나': {
        '가격': 2000,
        '개수': 4
    },
    '복숭아': {
        '가격': 1500,
        '개수': 2
    },
    '키위': {
        '가격': 2200,
        '개수': 5
    }
}
fruitPrice = 0

for fruit in cart :
    fruitPrice += cart[fruit]['가격'] * cart[fruit]['개수']

print(fruitPrice)
'''

'''
문제3
UP/DOWN 게임 만들기
단, 맞추면 몇번째에 맞췄는지도 출력
'''



'''
문제4
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}
이런 경우 
id/pw를 입력 받거나 변수에 넣어두고
id/pw가 맞는지 틀리는지 판단해서
"아이디가 없습니다", "비번이 틀립니다", "로그인 성공"

users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}

logID = str(input('아이디를 입력하세요 : '))
logPW = str(input('패스워드를 입력하세요 : '))

if logID in users :
    if logPW == users[logID] :
        print('로그인 성공!')
    else :
        print('비밀번호가 틀렸습니다.')
else :
    print('아이디가 틀렸습니다.')
'''

'''
문제5
랜덤 투표 시스템
한번에 a, b, c 대상에 랜덤으로 투표
문제5-1 : 100번의 투표 결과를 출력하시오
문제5-2 : 그 중 가장 득표 많은 사람의 이름과 득표 수 출력
'''
# import random

# candidate = {}

# # if candidate.get('a', {}) :
# candidate['a'] = 1
# candidate['b'] = 1
# candidate['c'] = 1

# print(candidate) 
# print(max(candidate)) 

# candidate = {
#     'a' : 0,
#     'b' : 0,
#     'c' : 0
# }

# for canD in candidate :
#     # print(canD)
#     # print(candidate[canD])
#     print(candidate.get(canD))
#     if candidate.get(canD) :
#         candidate[canD] += 1

# print(candidate)

# print(candidate.get('a', {}) )

# if candidate.get('a', {}) == {} :
#     candidate['a'] = 1
# else :


# for human in candidate :
#     if candidate.get(human, {}) :
#         human += 1
#     else :
#         candidate['a'] = 1

import random
candidate = ['a','b','c']
voteGet = {}

for i in range(100) :
    vote = random.choice(candidate)

    voteGet[vote] = voteGet.get(vote, 0) + 1

print(voteGet)
print(max(voteGet) , voteGet[max(voteGet)])

# print(vote)