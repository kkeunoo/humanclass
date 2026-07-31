
for i in range(5) :
    print(i, end=' ')

print()

# reversed() 는 뭐가 되었든 거꾸로 바꿔주는 역할
for i in reversed(range(5)) :
    print(i, end=' ')

print()

# if는 아끼지 말고 쓰고 한 단계씩 조립하기!!
for i in range(2,10,3) :
    for j in range(1,10) :
        print(f'''{i} x {j} = {i*j}''', end=' ')
        if i+1 < 10 :
            print(f'''{i+1} x {j} = {(i+1)*j}''', end=' ')
        if i+2 < 10 :
            print(f'''{i+2} x {j} = {(i+2)*j}''', end=' ')
        print()
    print()

# import로 random을 불러와서 사용할 수 있음
import random
print( random.random() )
print( random.randint(1, 6) )

# 주사위 3이 몇 번만에 나오는지 출력하시오
# i = 0
# count = 0
# while i != 3 :
#     i = random.randint(1, 6)
#     count += int(1)
#     if result == 3 :
#         print( result )
#         print( f'{count}번' )

count = 0
dice = 0
while dice != 3 :
    dice = random.randint(1, 6)
    count += 1
    if dice == 3 :
        print(count)
    

print('-'*30)
# Pyramid_Python(JavaScript ver)
inputUser = int(input('줄 수 : '))
for k in range(0,inputUser+1) :
    result = ''
    for m in range(0,inputUser-k) :
        result += ' '
    for i in range(0,(k+k)-1) : 
        result += '*'
    for j in range(0,inputUser-k) :
        result += ' '

    print(result)

# Pyramid_Python(Python verFinal)
inputUser = int(input('줄 수 : '))
for j in range(1,inputUser+1) :
    print(' '*(inputUser-j),end='')
    print('*'*((j+j)-1),end='')
    print(' '*(inputUser-j))

# inputUser = int(input('줄 수 : '))
# # for i in range(1) :
# for j in range(1,inputUser+1) :
#     print(' '*(inputUser-j),end='')
#     print('*'*((j+j)-1),end='')
#     print(' '*(inputUser-j))
# # print()
# for i in range(1) :
#     for j in range(1,10,2) :
#         print('-'*(10-j),end='')
#         print('*'*j,end='')
#         print('-'*(10-j))
#     print()

import turtle as t
t.shape('turtle')

# 터미널 무한반복 탈출은 Ctrl+C
# while True :
#     print(1)

# Fizz, Buzz 3과 5의 공배수 Fizz!Buzz! / 3배수 Fizz! / 5배수 Buzz!
for i in range(100) :
    if i % 3 == 0 and i % 5 == 0 :
        print('Fizz!Buzz!')
    elif i % 3 == 0 :
        print('Fizz!')
    elif i % 5 == 0 :
        print('Buzz!')
    else :
        print(i)

a = 20
i = 0
while i < 10 :
    if i == a :
        print('찾음')
        break
    i += 1
else :
    print('못찾음')
# while의 else는 break를 만나지 않고 조건식에 의해 종료되는 경우 else문 실행 됨