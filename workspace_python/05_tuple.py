# 선언 (readonly list)
# a = () 처럼 빈 것으로 선언 불가하며, 값은 바꾸지 못 함
a = (1,2,3)
print(a, type(a))

# tuple은 ()없이도 선언해서 사용할 수 있음
b = 1,2,3
print(b, type(b))

# 값이 1개인 tuple을 선언하기 위해서는 ','를 써줘야 함
c = (3,)
print(c, type(c))
d = 4,
print(d, type(d))

# 아래와 같이 tuple > list , list > tuple 변경 가능
e = [1,2,3]
print(tuple(e))
f = (1,2,3)
print(list(f))