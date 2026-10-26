# 02. 변수·연산자·입력과 출력

[Python 목차](README.md) · [이전: 출력과 주석](01_Python_출력과_주석.md)

양쪽 `02_var.py`는 변수에 값을 담고 계산·형변환·입력·출력을 연습한 파일이다. **코드에 적힌 예상과 실제 값이 다른 부분**을 함께 읽으면 나중에 다시 봐도 덜 헷갈린다.

<!-- chapter-toc -->

- [1. 나눗셈과 나머지](#section-1)
- [2. 자료형 변환과 실수 비교](#section-2)
- [3. 두 변수의 값 바꾸기](#section-3)
- [4. 입력값과 print의 구분자](#section-4)
- [5. 비교·논리 연산](#section-5)
- [직접 확인할 질문](#section-6)
- [추가로 알면 좋은 것](#section-7)

<a id="section-1"></a>

## 1. 나눗셈과 나머지

### 강사님 코드

출처: `teacher/workspace_python/_02_var.py` 1–23행 · **원본 발췌**

```python
a = 10
print(a)

b = 5 / 2
print(b)

# b = 5 / 0 # ZeroDivisionError: division by zero
# print(b)

c = 5 // 2
print(c)

d = -5 // 2 # 내림
print(d)

e = 4 ** 2 # 제곱
print(e)

# e++ # 없음
# e-- # 없음
e = e + 1
e **= 2
print(e)
```

### 내 코드

출처: `me/workspace_python/02_var.py` 1–30행 · **원본 발췌**

```python
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
```

`5 / 2`는 `2.5`, `5 // 2`는 `2`, `5 % 2`는 나머지 `1`, `5 ** 2`는 `25`다. 내 주석의 “`//`은 나머지를 내림”은 정확한 설명이 아니다. `//`는 나눗셈 결과에서 **아래쪽 정수로 내려가는 몫**이고, 나머지를 구하는 기호는 `%`다. 특히 음수에서는 단순히 소수 부분만 자르는 `int()`와 결과가 달라질 수 있다.

`e++`·`e--`는 이 언어의 증감 연산자가 아니므로 주석 처리되어 있다. 원본은 `e += 1`처럼 다시 대입해 값을 바꾼다.

<a id="section-2"></a>

## 2. 자료형 변환과 실수 비교

### 강사님 코드

출처: `teacher/workspace_python/_02_var.py` 25–42행 · **원본 발췌**

```python
print( int(2.4) )
print( int(-2.4) ) # 소수점 버림
print( int('10')+1 )
# print( int('a') )

print(0.12345678901234567890123456789)


print( type(10) )
print( type('10') )

print( 4.3 - 2.7 == 1.6 )


print(4.2 + 5)

print( float(5) )
print( float('5.2') )
```

### 내 코드

출처: `me/workspace_python/02_var.py` 32–62행 · **원본 발췌**

```python
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
```

`int(2.4)`는 `2`, `int(-2.4)`는 `-2`다. **0 방향으로 소수 부분을 버리는 변환**이므로 음수에서 `//`와 같지 않다. `int('10') + 1`은 `11`이고, 숫자로 해석할 수 없는 `'a'`를 `int`에 넣는 줄은 주석 처리되어 있다. `float('5.2')`는 문자열을 실수로 변환한다.

`4.3 - 2.7 == 1.6`의 결과는 원본 환경에서 `False`다. 이 차이는 실수 표현의 한계와 관련된다. 내 주석의 “소수점 16자리까지 믿을 수 있다”는 모든 수에 적용되는 규칙은 아니다. 결과를 확인하고, 정확한 소수 계산이 필요할 때에는 목적에 맞는 별도 방법을 선택해야 한다. 그 구현은 이번 수업 본문의 필수 범위가 아니다.

<a id="section-3"></a>

## 3. 두 변수의 값 바꾸기

### 강사님 코드

출처: `teacher/workspace_python/_02_var.py` 44–54행 · **원본 발췌**

```python
a = 10
b = '오백원'

# 전통적인 swap
c = a 
a = b
b = c

a, b = b, a
print(a) # 오백원
print(b) # 10
```

### 내 코드

출처: `me/workspace_python/02_var.py` 64–73행 · **원본 발췌**

```python
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
```

강사님은 임시 변수 `c`를 써서 `a`와 `b`를 **한 번** 바꾼다. 나는 같은 교환 뒤에 `a, b = b, a`를 다시 실행했다. 따라서 내 코드의 최종 값은 **원래 상태인 `a=10`, `b='오백원'`**이다. 내 `print(a) # 오백원`, `print(b) # 10` 주석은 이 실제 결과와 맞지 않는다. 튜플처럼 묶어 대입하는 Python 교환법 자체는 간결하지만, 여기서는 두 방법을 연달아 실행해 두 번 바꾼 점이 핵심이다.

<a id="section-4"></a>

## 4. 입력값과 print의 구분자

### 강사님 코드

출처: `teacher/workspace_python/_02_var.py` 56–67행 · **원본 발췌**

```python
a = input('입력하세요:')
print(a)

# print( 'a'+ 1 )
print( 'a'+ 'b' )

print(1,2)
print(1, 2, sep=" ")
print(1, 2, sep=",")

print(1, 2, end='', sep=" ")
print(2, end='\n')
```

### 내 코드

출처: `me/workspace_python/02_var.py` 75–97행 · **원본 발췌**

```python
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
```

`input('입력하세요:')`는 사용자가 입력할 때까지 기다린다. 받은 값은 문자열이므로 숫자 계산이 필요하면 알맞게 변환한다. `print(1, 2)`는 기본적으로 사이에 공백을 넣고 끝에서 줄을 바꾼다. `sep`은 여러 값 **사이**, `end`는 출력 **끝**에 붙일 내용을 바꾼다. 내 코드처럼 둘을 함께 지정할 수도 있다. 여러 `print`가 이어지므로 `end=''`의 결과는 다음 출력과 붙어 보인다.

<a id="section-5"></a>

## 5. 비교·논리 연산

### 강사님 코드

출처: `teacher/workspace_python/_02_var.py` 69–83행 · **원본 발췌**

```python
x = 4
print(++x)
# print(x++)

print( 1 == 1.0 )
print( 1 is 1.0 ) # === 즉, 타입까지 같다
print( 1 is not 1.0 ) # !==

print(1, False or False and not False)

a = '글씨'
b = a or '쉬는시간'
print( b )

print(3 < 5 < 7)
```

### 내 코드

출처: `me/workspace_python/02_var.py` 99–130행 · **원본 발췌**

```python
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
```

`++x`는 `x`를 증가시키는 문장이 아니라 단항 `+`를 두 번 적용한 식이다. 내 `--x`도 단항 `-`를 두 번 적용하므로 `x`를 감소시키지 않는다. `x++`처럼 뒤에 붙이는 증감 문법은 없다.

`1 == 1.0`은 값 비교라 `True`다. 원본 주석은 `is`를 “값과 타입까지 같다”는 비교처럼 설명하지만, Python의 `is`는 **같은 객체를 가리키는지** 확인한다. 타입 비교의 대체재가 아니며 숫자 값 비교에는 `==`를 쓴다. 두 원본의 `1 is 1.0`은 `False`다.

`and`가 `or`보다 먼저 계산되고, `a or '쉬는시간'`은 `a`가 참으로 평가되는 값이면 그 값 자체를 돌려준다. 그래서 `a='글씨'`라면 `b`도 `'글씨'`다. `3 < 5 < 7`처럼 비교를 연결한 식도 실제 수업 코드에 있다.

<a id="section-6"></a>

## 직접 확인할 질문

1. 내 파일에서 변수 교환을 한 번만 한 뒤와 두 번 한 뒤의 `a`, `b`는 각각 무엇일까?
2. `int(-2.4)`와 `-5 // 2`는 왜 다를까?
3. `++x`를 출력한 다음 `x`의 값이 바뀌었을까?

<a id="section-7"></a>

## 추가로 알면 좋은 것

금액처럼 소수의 정확성이 중요한 계산에서는 부동소수점 대신 목적에 맞는 표현을 검토한다. 이 수업 원본은 실수 비교에서 예상과 다른 결과가 나올 수 있음을 관찰하는 단계까지다.

