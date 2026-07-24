a = 10
print(a)

b = 5 / 2
print(b)

# ZeroDivisionError: division by zero : 0으로 나눌 수 없다라는 에러 발생
# b = 5 / 0
# print(b)

'''
//는 버림이 아니라, 내림임 양수 2.5의 경우 내리면 2가 되지만,
-5 // 2는 -2.5여야 하지만 음수기 때문에 -3으로 감
'''
c = 5 // 2
print(c) # value: 2

# //은 나눈 뒤 나머지를 내림
d = -5 // 2 # value: -3
print(d)

# **은 제곱연산자(거듭제곱) 값 ** 제곱수
e = 4 ** 2
print(e)

# e++ , e-- 는 없음
# e = e + 1
# e += 1
e **= 2
print(e)

# //와 다르게 int로 정수를 만드는건 소수점자리를 버림
print( int(2.4) )
print( int(-2.4) )
# parseInt처럼 정수로 바꿔주지만, py에서는 문자도 정수로 바꿔줌
print( int('10')+1 )
# ValueError: invalid literal for int() with base 10: 'a'
# javascript에서 NaN이 나오는 것 처럼 허용되지 않는 문자
# print( int('a') )

# 소수점은 16자리까지는 믿어 출력하고, 그 이후는 나오지 않음
print( 0.123456789012345678901234567890 )

# type of처럼 type을 알아내는 것
# <class 'int'>
print( type(10) )

# <class 'str'>
print( type('10') )

# 1.6이 나와야 하지만, 부동소수점 때문에 1.5999999..6이 나옴
print( 4.3 - 2.7 )
print( 4.3 - 2.7 == 1.6 ) #을 하면 'false'가 나옴

# 실수와 정수는 원칙적으로 자료형이 다르지만, 
# 내부적으로 5를 5.0으로 형변환하여 계산값이 나옴
print ( 4.2 + 5 )
# print ( 4.2 + float(5) )이 원칙상은 맞는 형태

# float은 값을 실수로 만들어줌
print ( float(5) )
print ( float('5.2') )

a = 10
b = '오백원'
# 전통적인 swap이 아래와 같이 변수를 만들어 넣어놓고 값을 바꾸는 것
c = a
a = b
b = c
# python은 아래와 같이 swap이 가능
a, b = b, a
print(a) # 오백원
print(b) # 10

# 사용자가 입력한 값을 출력해주는 것
# a = input()
# print(a)

a = input('입력하세요:')
print(a)

# python 에서는 문자 + 숫자가 안 됨 (웬만해선 숫자를 문자로 바꿔주지만 py는 논외)
# print( 'a'+ 1 )
print( 'a'+ 'b' )

print(1,2)
# print의 기본값 (띄어쓰기 및 엔터가 나옴)
print(1, 2, sep=" ")
print(1, end='\n')

print(1, 2, sep=",")
print(1, 2, sep="")

# 아래와 같이 필요할 때만 \n하도록 할 수 있음
print(1, 2, end='', sep='') #end와 sep도 같이 쓸 수 있음
print(1, 2, end='')
print(2, end='\n')

x = 4
# 아래는 +(+4)를 인식하여 나옴
print(++x)
# 아래는 -(-4)를 인식하여 나옴
print(--x)
# 아래처럼 증감연산자는 없음, 오타로 인식함
# print(x++)

# 정수와 float의 값이 같은지?
print( 1 == 1.0 )
# 정수와 float의 값과 타입까지 같은지? (is를 사용)
print( 1 is 1.0 )
print( 1 is not 1.0 )

# 괄호가 없을 때 무조건 and(논리곱)가 먼저 계산 됨, 그렇기에 True
# ex) 논리합or[1+1=2,1+0=1], 논리곱and[1x1=1,1x0=0]
print(not False or not True and False)

# ex) if( a != undefined && a.length == 3)
# 이라고 했을 때 a가 이미 undefined면 뒤 a.length 부터 읽지 않기 때문에,
# 논리연산자보다 !=, ==이 우선순위가 높음

# if문에 들어가면 True가 나오는게 맞지만, 변수에 들어가게 되면 살아있는 값이 나옴
# a = False
a = '글씨'
# 변수는 살아있으나 값이 없을 때 아래처럼 방법을 사용 a가 없다면 b사용
b = a or '쉬는시간'
print( b )

# python에서는 이렇게 사용할 수 있음 (true)
print (3 < 5 < 7)
print (1 + 3 < 7)