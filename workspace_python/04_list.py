
a = []
b = list()
print(type(a))
print(type(b))

a = [1,2,3]
print(a)

# 전달인자가 하나인 경우, 0번부터 시작해서 숫자 바로 앞까지(0~9)를 만들어라
c = range(10)
print(c)
# list는 배열의 선언보다 배열로 바꾸어주는 것
print(list(c)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 전달인자가 두개인 경우, 첫 번째 두 번째 바로 앞까지
d = range(5, 12)
print(list(d)) # [5, 6, 7, 8, 9, 10, 11]

e = range(12, 5)
print(list(e)) # value: [] 빈 배열

# 전달인자가 세개인 경우 첫 번째 부터, 두 번째 바로 앞까지, 세 번째 값 씩 건너 뛰기(step)
f = range(-4, 10, 2)
print(list(f)) # [-4, -2, 0, 2, 4, 6, 8]
f1 = range(10,0,-1)
print(list(f1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

a = [0,1,2,3,4,5]
a = list(range(6))

del a[3]
print( a )

a = a + [6]
print( a )

a += [7]
print( a )
 
a.append(8) # python 에서는 list에 push대신 append로 붙일 수 있음
print( a )

b = [9,10] # concat개념이 아니라, append는 단순하게 하나를 추가하는 것
print( b , type(b) )
a.append(b)
print( a , type(a) ) # [0, 1, 2, 4, 5, 6, 7, 8, [9, 10]] <class 'list'>

print(':='*30)
c = [654,156,964,15,35]
c.sort() # 오름차순 원본이 바뀜, [15, 35, 156, 654, 964]
print( c ) # JavaScript와 다르게 sort는 15 156이 아닌, 숫자 크기대로 정렬해줌
c.sort(reverse=True) # sort의 기본값은 reverse=False (오름차순)
print( c )
print(':='*30)

c = c[::-1] # -1은 원본을 바꾸지 않음, [964, 654, 156, 35, 15]
print( c )

c.reverse() # 내림차순 원본이 바뀜, [15, 35, 156, 654, 964]
print( c )

d = c.pop()
print(c, d)

c.insert(0,100) # 0번째에 100추가
print(c)

c.insert(10,200) # 10번째에 200추가인데, 범위를 넘어서도 끝으로 들어감
print(c)

# extend는 insert, append와 다르게 여러 개의 리스트 값을 원본에 추가해줌
c.extend([1,2])
print(c)

# remove는 처음 만나는 값을 찾아서 지워준다
a = [1,2,3,4,2]
a.remove(2)
print(a)

if 5 in a : # in으로 값이 있을 때 실행하도록 진행
    a.remove(5) # 없는 값의 경우 에러 발생

a = [1,2,3,4,2,4]
b = a.index(2)
print(b)
# b = a.index(5) # 없는 값의 경우 에러 발생
# b = a.find(5) # 리스트에서 find는 사용할 수 없음

# stack과 queue란?
# stack은 프링글스통 기존 스택 설명과 같이 넣을 때 뒤로가고 뺄 때도 뒤에서
# queue는 넣을 때 뒤로가고 뺄 때는 제일 앞에서
c = a.count(4)
print(c)

a.reverse()
print(a)
b = reversed(a)
print(b)

a.clear() # a = [] 는 동일하게 사용할 수 있음
print(a)

a = [1,2,3]
print( a[len(a):] )
# print( a[3] ) # a[3] 으로 하면 IndexError: list index out of range 발생
print( a[3:] ) # :을 넣으면 에러는 나지 않음

# a[3:] = 4 # TypeError: must assign iterable to extended slice 에러는 반복될 수 있는 배열같은 것이 필요
a[3:] = [4,5,6] # extend처럼 비슷하게 사용할 수 있음, append는 단독 1개이기 때문에 다름
print(a)

a[len(a):] = [500] # a의 길이는 3이고 3: (3부터)라는 뜻이기 때문에, index 3에 500추가
print(a)

f = [] # 비어있으면 False
print( len(f) ) # False
print( not len(f) ) # True

a = [1,2,3,4,5]
b = a # 이렇게 넣으면 a = b의 주소값이 동일해지기 때문에, index값을 바꾸면 두개가 모두 바뀜
b[2] = 30
print(b)
print(a)

a = [1,2,3,4,5]
b = a.copy() # copy를 이용하면 모든 요소를 아예 복사해오기 때문에, 이럴 땐 주소값이 달라져 개별 값만 바꿔짐
b[2] = 30
print(b)
print(a)

a = [1,2,3,4,5]
b = a.copy() 
print( a is b ) # False (주소값이 다르기 때문에 주소까지 전부 같지 않음)
print( a == b ) # True (안에 있는 값은 같음)

# 아래 두개는 동일한 것, Python에서는 간단하게 가능
c = (1,2)
a = c[0]
b = c[1]
print(a, b)

a, b = (1,2)
print(a, b)

a = [10,20,30]
for i in a :
    print(i)

# enumerate(인자)는 index, value를 같이 뽑아낼 수 있는 함수
for index, value in enumerate(a) :
    print(index, value)

# 아래처럼 인자와 ,를 쓰게되면 start로 시작 index를 조절할 수 있음
for index, value in enumerate(a, start=100) :
    print(index, value)

# 제일 큰 값을 찾기 위해 오름차순으로 정렬
a = [7,3,5,8,4]
a.sort()
print(a[len(a)-1])
print(a[-1])

# index, value 한 번 더 확인
# for index, value in enumerate(a) :
#     print(index, value)

# a의 len만큼 i를 돌게하고, 만약 i가 리스트의 마지막 일 때 그 값 출력
for i in range(len(a)) :
    if i == len(a)-1 :
        print(a[i])

# a 배열에 0~9를 넣음

a = []
for i in range(10) :
    a.append(i)
print(a)

# for i in range(10)의 i를 배열로 만들어라
a = [ i for i in range(10) ] 
print(a)

a = []
for i in range(10) :
    if i % 2 == 0 :
        a.append(i)
print(a)

a = list( i for i in range(10) if i % 2 == 0 )
print(a)

# 값을 int로 바꿔서 저장
a = [1.2, 2.5, 3.7, 4.6, -3.5]
for i, value in enumerate(a) :
    a[i] = int(value)
print(a)

# 두번째 반복되는 것을 하나씩 꺼내서, 첫 번째 함수에 넣고
# 결과를 배열로 만들어 주는 것이 map과 int
a = [1.2, 2.5, 3.7, 4.6, -3.5]
a = list(map(int, a))
print(a)

a = [
    [10,20],
    [30,40],
    [50,60]
]
print(len(a))
print(a[1][0])

print('-'*20)
print([0]*10)