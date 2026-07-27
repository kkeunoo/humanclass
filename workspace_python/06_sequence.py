
a = [0, 10, 20, 30, 40] 
print( 20 in a  ) #True
print( 200 in a  ) #False
print( not ( 200 in a  ) ) # !대신 not 사용
print( 200 not in a )

a = [1,2,3]
b = [4,5,6]
c = a + b # range + range는 불가하지만, list나 tuple로 바꾸면 합칠 수 있음
print( c )

a = 'hello'
b = 'world'
c = a+b
print(c)

# javascript에서는 가능하지만, python은 sequence 끼리만 가능함
# c = a + 3 
c = a + str(3) 
print(c)

print('-' * 10)

print( len(a) ) # len으로 감싸면 길이를 구할 수 있다(문자,숫자,튜플 등)

hello = '안녕하세요'
b = hello.encode('utf-8')
print( len(b) )
print(b)
print(hello[0]) # '안'

a = [1,2,3,4]
print(a[0]) # 1
print(a[-2]) # 3 (-는 뒤에서 몇 번째 index)

# IndexError: list index out of range
# print(a[100]) # 배열의 범위를 벗어나면 error발생, javascript만 undefined

a = (1,2,3)
print(a[0])
# tuple은 'readonly' 형태기 때문에 값은 바꿀 수 없다
# a[0] = 3 # TypeError: 'tuple' object does not support item assignment
a = [1,2,3]
del a[0]
print(a)

a = [0,1,2,3,4,5,6,7,8,9]
print( a[1:4] ) # index 1~4 앞까지 새 리스트로 생성 (slice)
print( a[4:-1] )
print( a[4:100] ) # 범위를 벗어나도 에러는 없음

print( a[1:9:2] ) # [시작INDEX,끝INDEX,반복INDEX]

print( a[:7] ) # 처음부터 [:끝INDEX] 까지
print( a[5:] ) # [시작INDEX] 부터 끝까지
print( a[:] ) # 배열에 있는 전체 다

print( a[7:3] ) # 이건 값이 나오지 않음
print( a[7:3:-1] ) # 여기서 -1은, -1씩 뒤부터 출력
print( a[8:4:-1] ) # 여기서 -1은, -1씩 뒤부터 출력

print( a[-4:8] ) # 결과값 6,7 : 뒤의 4번째부터 8바로 앞까지
print( a[-4:-2] ) # 결과값 6,7 : 뒤의 4번째부터 뒤의 2번째까지

print( a )
a[2:5] = ['a', 'b', 'c']
print( a )

print( a[2:5] )
a[2:5] = [10, 20, 30, 40, 50] # 원하는 자리에 원하는 값으로 바꿀 수 있음
print( a )

ko = ['책', '알약', '철판']
en = ['book', 'pill', 'plate']

# 같은 key에 번역 된 말을 써놓고 몇 번째 자리인지 비교해서 교차하기도 함
view = ko
view = en

print( view[0] ) 

a = 'hello'
print( a[::-1] )
