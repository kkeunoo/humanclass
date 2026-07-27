
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

c = [654,156,964,15,35]
c.sort() # 오름차순 원본이 바뀜, [15, 35, 156, 654, 964]
print( c ) # JavaScript와 다르게 sort는 15 156이 아닌, 숫자 크기대로 정렬해줌

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