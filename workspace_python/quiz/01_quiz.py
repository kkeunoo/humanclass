
'''
문제1
numbers = [3, 7, 10, 15, 22, 8, 13]
문제1-1 : 짝수만 따로 리스트로 만들어서 출력
문제1-2 : 홀수의 합
'''
print('\n문제1','- - '*10)
numbers = [3, 7, 10, 15, 22, 8, 13]
# print(len(numbers))

double = []
single = []
singleResult = 0

for i in range(len(numbers)) :
    if numbers[i] % 2 == 0 :
        double.append(numbers[i])
    else :
        single.append(numbers[i])
        singleResult += numbers[i]

print(f'짝수 : {double}, {type(double)}')
print(f'홀수 : {single}, {type(single)}')
print(f'홀수의 합 : {singleResult}')

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
'''

print('\n문제2','- - '*10)
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

# for i in cart.keys() 라고 한다면, i에 key값이 모두 저장이 되기 때문에
# 개수와 가격이라는 것은 동일해서 사과,바나나,복숭아,키위만 반복된다면 
# price에 누적으로 저장시키면 됨
for i in cart.keys() :
    fruitPrice += cart[i]['가격'] * cart[i]['개수']
    # fruitPrice += cart['사과']['가격'] * cart['사과']['개수']
    # fruitPrice += cart['바나나']['가격'] * cart['바나나']['개수']
    # fruitPrice += cart['복숭아']['가격'] * cart['복숭아']['개수']
    # fruitPrice += cart['키위']['가격'] * cart['키위']['개수']

print(f'총액 : {fruitPrice}')

'''
문제3
UP/DOWN 게임 만들기
단, 맞추면 몇번째에 맞췄는지도 출력
'''
print('\n문제3','- - '*10)
import random
com = random.randint(1,100)
user = -1
count = 0

# 시간 날 때 문자 입력받는 방어코드도 넣기
while com != user :
    user = int(input('숫자를 입력하세요.'))
    if com > user :
        print('UP 입니다.')
        count += 1
    elif com < user :
        print('DOWN 입니다.')
        count += 1
    elif com == user :
        print(f'정답입니다! 시도횟수 : {count}')
    

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
"아이디가 틀립니다", "비번이 틀립니다", "로그인 성공"
'''
print('\n문제4','- - '*10)
# users = {
#     "admin": "1234",
#     "guest": "guest",
#     "user1": "abcd"
# }
# logID = str(input('ID를 입력하세요 : '))
# logPW = str(input('PW를 입력하세요 : '))

# print(logID in users.keys())
# print(logPW in users.values())

# if logID in users.keys() and logID == 'admin' :
#     if logPW in users.values() and logPW == '1234' :
#         print('당신어드민~로그인 성공~')
#     else : 
#         print('패스워드가 틀렸습니다.')
# elif logID in users.keys() and logID == 'guest' :
#     if logPW in users.values() and logPW == 'guest' :
#         print('당신게스트~로그인 성공~')
#     else : 
#         print('패스워드가 틀렸습니다.')
# elif logID in users.keys() and logID == 'user1' :
#     if logPW in users.values() and logPW == 'abcd' :
#         print('당신유저~로그인 성공~')
#     else : 
#         print('패스워드가 틀렸습니다.')
# else :
#     print('아이디가 틀렸습니다.')
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}

logID = str(input('ID를 입력하세요 : '))
logPW = str(input('PW를 입력하세요 : '))

# logID를 쳤을 때 users에 있는 키값이 동일했을 경우 밸류값은 예시로 admin이라고 치면
# 자동적으로 user[logID]의 밸류기 때문에, '1234'라는 value를 받아올 수 있어 그걸로
# 입력받은 PW값과 비교하면 해결 됨
if logID in users.keys() :
    # print(users[logID])
    if logPW == users[logID] :
        print('로그인 성공!')
    else :
        print('비밀번호가 틀렸습니다.')
else :
    print('아이디가 틀렸습니다.')

'''
문제5
랜덤 투표 시스템
한번에 a, b, c 대상에 랜덤으로 투표
문제5-1 : 100번의 투표 결과를 출력하시오
문제5-2 : 그 중 가장 득표 많은 사람의 이름과 득표 수 출력
'''
print('\n문제5','- - '*10)
import random
keys = input('나나')
key = keys.split(' ')

a = 0 # 랜덤 값 1일때 투표
b = 0 # 랜덤 값 2일때 투표
c = 0 # 랜덤 값 3일때 투표

for i in range(0,100) :
    vote = random.randint(1, 3)
    if vote == 1 :
        a += 1
    elif vote == 2 :
        b += 1
    elif vote == 3 :
        c += 1

print(a, b, c)
print(keys)
print(key)

print(vote)