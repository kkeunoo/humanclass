
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