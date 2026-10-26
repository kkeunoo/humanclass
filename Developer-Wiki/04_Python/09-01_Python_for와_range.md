# 09-01. `for`와 `range` — 정해진 횟수 반복하기

[Python 목차](README.md) · [이전: 조건문](08_Python_조건문.md) · [다음: `while`](09-02_Python_while과_반복제어.md)

양쪽 `09_for.py`에서 공통으로 먼저 등장하는 것은 `range`, 거꾸로 읽기, **중첩 `for`로 구구단 만들기**다. 별 피라미드와 FizzBuzz도 양쪽의 별도 퀴즈 파일에서 확인된다. 파일이 다른 두 풀이를 나란히 놓고 실제 반복 범위와 출력을 비교한다.

<!-- chapter-toc -->

- [1. `range(5)`와 `reversed`](#section-1)
- [2. 두 겹 반복으로 구구단 만들기](#section-2)
- [3. 별 피라미드 — 같은 모양을 만드는 다른 반복](#section-3)
- [4. FizzBuzz — 반복 시작값부터 비교하기](#section-4)
- [직접 확인할 질문](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. `range(5)`와 `reversed`

### 강사님 코드

출처: `teacher/workspace_python/_09_for.py` 1–5행 · **원본 발췌**

```python
for i in range(5) :
    print(i, end=' ')
print()
for i in reversed(range(5)) :
    print(i, end=' ')
```

### 내 코드

출처: `me/workspace_python/09_for.py` 2–9행 · **원본 발췌**

```python
for i in range(5) :
    print(i, end=' ')

print()

# reversed() 는 뭐가 되었든 거꾸로 바꿔주는 역할
for i in reversed(range(5)) :
    print(i, end=' ')
```

`range(5)`로 꺼내는 값은 **0, 1, 2, 3, 4**다. `reversed(range(5))`는 이를 반대로 꺼낸다. `print(..., end=' ')`는 출력 뒤에 줄바꿈 대신 공백을 붙이고, 인자 없는 `print()`는 다음 줄로 옮긴다. 내 주석의 “`reversed()`는 뭐가 되었든 거꾸로”는 너무 넓다. 여기서는 `range`를 거꾸로 읽는 동작만 확인한다.

<a id="section-2"></a>

## 2. 두 겹 반복으로 구구단 만들기

### 강사님 코드

출처: `teacher/workspace_python/_09_for.py` 17–19행 · **원본 발췌**

```python
for j in range(2, 9+1) :
    for i in range(1, 9+1) :
        print(f'{j}x{i}={j*i}')
```

### 내 코드

출처: `me/workspace_python/09_for.py` 14–23행 · **원본 발췌**

```python
for i in range(2,10,3) :
    for j in range(1,10) :
        print(f'''{i} x {j} = {i*j}''', end=' ')
        if i+1 < 10 :
            print(f'''{i+1} x {j} = {(i+1)*j}''', end=' ')
        if i+2 < 10 :
            print(f'''{i+2} x {j} = {(i+2)*j}''', end=' ')
        print()
    print()

```

강사님 코드는 바깥 `j`가 **2단부터 9단**, 안쪽 `i`가 **1부터 9**를 돈다. 내 코드는 바깥 `i`가 `2, 5, 8`을 돌며 한 줄에 3단씩 나란히 놓는다. 마지막 8단에서는 `i+2 < 10`이 거짓이라 10단을 출력하지 않는다. 같은 중첩 반복이지만 **반복 변수의 역할과 출력 모양**이 다르다.

### 강사님 코드 — 가로로 3단씩 출력

출처: `teacher/workspace_python/_09_for.py` 47–60행 · **원본 발췌**

```python
k = 14
for i in range(2, k+1, 3) :
    for j in range(1, 9+1) :
        # print(f'{i}x{j}={i*j}', end='  ') 
        # if i+1 <= k :
        #     print(f'{i+1}x{j}={(i+1)*j}', end='  ')
        # if i+2 <= k :
        #     print(f'{i+2}x{j}={(i+2)*j}', end='  ')
        # print()
        for m in range(3) :
            if i+m <= k :
                print(f'{i+m}x{j}={(i+m)*j}', end='\t') 
        print()
    print()
```

강사님은 마지막에 `k=14`까지 범위를 늘려, 안쪽의 `for m in range(3)`과 `if i+m <= k`로 끝단을 검사한다. 내 코드처럼 각 단을 따로 `if`로 검사해도 된다. 초보자는 먼저 내 `i+1`, `i+2`의 출력 조건을 따라가고, 그 다음 강사님이 `m`으로 중복을 줄인 부분을 비교하면 좋다. 두 구현 모두 **실제 원본에 있는 방식**이다.

<a id="section-3"></a>

## 3. 별 피라미드 — 같은 모양을 만드는 다른 반복

### 강사님 코드

강사님 `퀴즈/피라미드.py`의 실행 부분이다. `line`을 입력받고 `j`를 **1부터 `line-1`까지** 반복한다. 좌우 공백 대신 `-`를 넣어 모양을 확인하며, 별은 가운데 두 반복으로 붙인다. 따라서 입력이 5라면 **4줄**이 출력된다.

출처: `teacher/workspace_python/퀴즈/피라미드.py` 134–147행 · **원본 발췌**

```python
line = int(input('줄 입력 : '))
m = '*'
s = '-'
for j in range(1, line):
    string = ''
    for i in range(1, line-j):
        string += s
    for i in range(1, j+1):
        string += m
    for i in range(1, j):
        string += m
    for i in range(1, line-j):
        string += s
    print(string)
```

### 내 코드 — 첫 풀이

출처: `me/workspace_python/09_for.py` 50–60행 · **원본 발췌**

```python
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
```

### 내 코드 — 문자열 반복을 쓴 풀이

출처: `me/workspace_python/09_for.py` 63–67행 · **원본 발췌**

```python
inputUser = int(input('줄 수 : '))
for j in range(1,inputUser+1) :
    print(' '*(inputUser-j),end='')
    print('*'*((j+j)-1),end='')
    print(' '*(inputUser-j))
```

첫 풀이에서 `k=0`인 첫 줄에는 별이 **0개**이고 공백만 출력된다. 두 번째 풀이에서는 `j=1`부터 시작하여 첫 줄부터 별 1개가 나온다. 따라서 같은 `inputUser`를 넣어도 출력 줄 수와 첫 줄이 다르다. 두 번째 풀이의 `' ' * (inputUser-j)`와 `'*' * ((j+j)-1)`은 앞에서 배운 **문자열 반복**을 활용해 중첩 반복문을 줄였다. 강사님은 `-`를 붙여 양쪽 모양을 표시하고, 내 코드는 공백으로 들여쓴다. 모두 실제 실습 코드다.

<a id="section-4"></a>

## 4. FizzBuzz — 반복 시작값부터 비교하기

### 강사님 코드

강사님 풀이에는 별도 `퀴즈/fizzbuzz.py`가 있다. **1부터 100까지** 반복하고, 숫자를 먼저 출력한 뒤 3과 5의 공배수·3의 배수·5의 배수를 차례로 검사한다.

출처: `teacher/workspace_python/퀴즈/fizzbuzz.py` 9–17행 · **원본 발췌**

```python
for i in range(1, 101) :
    print(i, end=' ')
    if i % 3 == 0 and i % 5 == 0 :
        print('fizzbuzz', end='')
    elif i % 3 == 0 :
        print('fizz', end='')
    elif i % 5 == 0 :
        print('buzz', end='')
    print()
```

### 내 코드

출처: `me/workspace_python/09_for.py` 91–99행 · **원본 발췌**

```python
for i in range(100) :
    if i % 3 == 0 and i % 5 == 0 :
        print('Fizz!Buzz!')
    elif i % 3 == 0 :
        print('Fizz!')
    elif i % 5 == 0 :
        print('Buzz!')
    else :
        print(i)
```

두 코드 모두 3과 5의 공배수 조건을 먼저 검사한 다음 각각의 배수를 검사한다. 내 `range(100)`은 **0부터 99까지**이므로, `0`에서도 `0 % 3 == 0`과 `0 % 5 == 0`이 참이 되어 첫 출력이 `Fizz!Buzz!`다. 반면 강사님 `range(1, 101)`의 첫 값은 1이다. 문제를 “1부터 100까지”로 생각하고 내 코드를 읽으면 결과를 잘못 예측할 수 있다.

<a id="section-5"></a>

## 직접 확인할 질문

1. `range(5)`에서 5가 출력되지 않는 이유는?
2. 내 구구단에서 8단 옆에 10단이 나오지 않는 이유는?
3. 별 피라미드 두 풀이의 첫 줄은 어떻게 다를까?

<a id="section-6"></a>

## 추가로 알면 좋은 것

`range` 객체와 `reversed`의 내부 구현이나 큰 데이터에서의 메모리 사용법은 이 원본의 학습 목표가 아니다. 먼저 **시작·끝·간격**과 두 겹 반복에서 각 변수의 역할을 읽는 데 집중하자.

