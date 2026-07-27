a = 'hello'
b = "world"

# 변수에 넣지 않으면 메모리에 남았다 다음줄로 가기 때문에 주석으로도 사용
c = '''여기에
여러 줄
넣을 수 있다'''

d = """여러 줄
쌉 가능"""

# 'he\'s name is "name"' 이라고 했을 때 \를 붙이면 탈출하며 문자로 사용 가능

b = 32.5
# c = "지금 온도는 " + b +"도 입니다." # 이것처럼 하면 str + int + str이기에 안 됨
c = "지금 온도는 " + str(b) +"도 입니다."
print(c)

# f를 사용하면 벡틱처럼 사용할 수 있음(fomentic)
d = f"지금 온도는 {b}도 입니다."
print(d)

# 아래처럼 {index}를 사용하고 해당 자리에 format(index)이 들어가도록 사용 가능
e = "지금 온도는 {0}도 입니다".format(b)
print(e)

f = f'''
<div>
    지금 온도는 {b}도 입니다
</div>
'''
print(f)

# 정수로 값이 나옴
g = '지금 온도는 %d도 입니다' % b
print(g)

# float으로 선언 가능
h = '지금 온도는 %f도 입니다' % b
print(h)

i = '_hello'
print(len(i))

# 'l' 이 몇 개인지 셀 수 있음
print( i.count('l') )
print( i.find('l') ) # find는 indexOf처럼 자리수를 볼 수 있음
print( i.find('z') ) # indexOf와 동일하게 값이 없을 때 -1 반환

print( i.index('l') )
# print( i.index('z') ) # index는 없으면 err msg가 나옴, ValueError: substring not found

print( i.rfind('l') ) # rear 뒤에서부터 indexOf

print( i.replace('l','w') ) # replace는 모두 바꿔줌

j = '그럼 저기서 하나만 바꾸고 싶으면요?'
k = j.split()
print(k)

m = [1,2,3]
a,b,c = m