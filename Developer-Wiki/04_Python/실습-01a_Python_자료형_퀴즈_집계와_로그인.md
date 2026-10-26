# 실습 01-1. 자료형 퀴즈 — 집계와 로그인

[Python 목차](README.md) · [다음: 난수 문제](실습-01b_Python_자료형_퀴즈_난수문제.md)

강사님 `퀴즈/문제-자료형.py`와 내 `quiz/01_quiz.py`에는 **같은 다섯 문제의 실제 풀이**가 있다. 앞의 01–15장에서 배운 리스트·딕셔너리·조건문·반복문을 함께 사용하는 수업 실습이므로 정규 본문에 둔다. 이 장은 결과가 정해지는 1·2·4번 문제를 비교한다.

<!-- chapter-toc -->

- [1. 짝수 리스트와 홀수의 합](실습-01a_Python_자료형_퀴즈_집계와_로그인.md#section-1)
- [2. 장바구니의 총액](실습-01a_Python_자료형_퀴즈_집계와_로그인.md#section-2)
- [3. 아이디와 비밀번호를 짝으로 검사하기](실습-01a_Python_자료형_퀴즈_집계와_로그인.md#section-3)
- [직접 확인할 질문](실습-01a_Python_자료형_퀴즈_집계와_로그인.md#section-4)
- [추가로 알면 좋은 것](실습-01a_Python_자료형_퀴즈_집계와_로그인.md#section-5)

<a id="section-1"></a>

## 1. 짝수 리스트와 홀수의 합

### 강사님 코드

출처: `teacher/workspace_python/퀴즈/문제-자료형.py` 1–20행 · **원본 발췌**

```python
print('문제1')
numbers = [3, 7, 10, 15, 22, 8, 13]
even = []
for num in numbers :
    if num % 2 == 0 :
        even.append(num)
print(even)


even = [num for num in numbers if num % 2 == 0]
print(even)

odd = [num for num in numbers if num % 2 != 0]
print(123, sum(odd))
hap = 0
for num in numbers :
    if (num % 2 != 0) :
        hap += num
print(hap)
print( sum(num for num in numbers if num % 2 != 0) )
```

### 내 코드

출처: `me/workspace_python/quiz/01_quiz.py` 8–25행 · **원본 발췌**

```python
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
```

두 코드는 같은 `numbers`에서 짝수 `[10,22,8]`과 홀수 합 **38**을 만든다. 강사님은 먼저 반복문으로 짝수를 담고 그 아래 **리스트 컴프리헨션으로 같은 결과를 다시** 만들었다. 홀수 합도 목록을 만든 뒤 `sum`하거나 반복문으로 누적하는 두 방식을 실행한다. `print(123, sum(odd))`의 `123`은 합계에 더해진 값이 아니라 함께 출력한 별도 숫자다. 내 코드는 `range(len(numbers))`로 위치를 읽어 짝수·홀수 목록을 만들고, 홀수는 `singleResult`에 누적한다. 어느 쪽이든 `% 2`가 짝수·홀수를 나누는 조건이다.

<a id="section-2"></a>

## 2. 장바구니의 총액

### 강사님 코드

출처: `teacher/workspace_python/퀴즈/문제-자료형.py` 22–55행 · **원본 발췌**

```python
print('문제2')
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
print( cart['사과']['가격'] )

apple = cart['사과']['가격'] * cart['사과']['개수']
banana = cart['바나나']['가격'] * cart['바나나']['개수']

for a in cart :
    print(a)
b = cart.keys()
for a in b :
    print(a)

total = 0
for fruit in cart :
    total += cart[fruit]['가격'] * cart[fruit]['개수']
print(total)
```

### 내 코드

출처: `me/workspace_python/quiz/01_quiz.py` 50–82행 · **원본 발췌**

```python
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
```

각 과일의 `가격 × 개수`를 더하면 **25,000**이다. 강사님은 `for fruit in cart`로 키를 순회하고, 나는 `for i in cart.keys()`로 같은 키를 순회한다. `cart[i]['가격']`과 `cart[i]['개수']`는 **같은 과일의 안쪽 딕셔너리**에서 읽는다. 내 코드의 과일별 계산 줄들은 주석이라 실제 합계에는 중복 반영되지 않는다. 강사님은 사과·바나나만 별도 변수로도 계산하지만, 전체 합계는 마지막 반복문으로 구한다.

<a id="section-3"></a>

## 3. 아이디와 비밀번호를 짝으로 검사하기

### 강사님 코드

출처: `teacher/workspace_python/퀴즈/문제-자료형.py` 80–103행 · **원본 발췌**

```python
print('문제4')
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}

id = 'admin'
pw = '1234'
# id = input('id:')
# pw = input('pw:')

# key 없으면 에러
# if users['admin2'] == '1234' :
#     print('로그인 성공')

# print('admin2' in users)
if id in users :
    if users[id] == pw :
        print('로그인 성공')
    else :
        print('비밀번호가 틀립니다')
else :
    print('아이디가 없습니다')
```

### 내 코드

출처: `me/workspace_python/quiz/01_quiz.py` 149–169행 · **원본 발췌**

```python
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

```

둘 다 **검사 대상 아이디가 딕셔너리의 키인지 먼저** 확인하고, 그 아이디의 값인 비밀번호와 검사 대상 비밀번호를 비교한다. 강사님은 `id='admin'`, `pw='1234'`를 변수에 고정하고, 나는 `input()`으로 두 값을 받는다. 내 위쪽의 계정별로 분기하던 긴 시도는 주석이며, 위 발췌가 실제 실행되는 풀이이다. `비밀번호`가 다른 계정에 존재하기만 하면 통과하는 검사가 아니라, **해당 아이디의 비밀번호와 일치해야** 성공한다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 짝수 목록과 홀수 합은 각각 무엇인가?
2. 장바구니에서 `cart[i]`는 바깥 딕셔너리의 무엇을 읽는가?
3. 다른 계정의 올바른 비밀번호를 입력해도 로그인되면 안 되는 이유는?

<a id="section-5"></a>

## 추가로 알면 좋은 것

이 수업 실습의 계정 딕셔너리는 메모리 안의 문자열 비교 예제다. 실제 서비스의 사용자 인증이나 비밀번호 저장 방법까지 구현한 코드는 아니다.

