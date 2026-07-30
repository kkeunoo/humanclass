# Python 반복문

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `09_Python_반복문.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `02_Python_변수와_자료형_연산자.md`, `04_Python_리스트와_컴프리헨션.md`, `06_Python_시퀀스와_슬라이싱.md`, `08_Python_조건문.md` |
| 다음 학습 | Python Quiz 문서 |
| 원본 기준 | `workspace_python/09_for.py`, `workspace_teacher/workspace_python/_09_for.py` |
| 핵심 범위 | `for`, `range()`, `reversed()`, 중첩 반복문, 구구단, `random`, `while`, 센티널 값, 피라미드 출력, `turtle`, 무한 반복, `FizzBuzz` |
| 보충 범위 | 반복 가능 객체, `range` 경계값, 반복 변수, `break`와 `continue`, 난수 기반 반복, 문자열 누적과 문자열 곱셈, 반복문 설계 순서, 자주 발생하는 오류 |
| Quiz 처리 | 원본 실습은 본문에서 분석하며, 추가 문제와 상세 풀이 문서는 최종 Quiz 단계에서 별도 제작 |

> 이 문서는 내 코드의 `09_for.py`와 강사님 코드의 `_09_for.py`를 직접 비교해 작성했습니다. 두 파일은 `for`와 `range()`, 역순 반복, 중첩 반복문으로 구구단 출력, 난수와 `while`, 주사위 반복까지 같은 흐름을 공유합니다. 내 코드에는 피라미드, `FizzBuzz`, 주석 처리된 시행착오가 추가되어 있고, 강사님 코드에는 일반 구구단, 최대 단수를 확장한 3단 묶음 출력, 활성화된 무한 반복이 포함되어 있습니다.

---

# 학습 목표

- 반복문이 같은 작업을 여러 번 실행하는 제어문임을 설명할 수 있다.
- `for`가 반복 가능한 객체의 값을 차례대로 꺼내 실행한다는 점을 이해한다.
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`을 구분할 수 있다.
- `range()`의 종료값이 포함되지 않는다는 점을 안다.
- `reversed()`를 이용해 범위를 역순으로 순회할 수 있다.
- `end` 인자로 출력 줄바꿈을 제어할 수 있다.
- 중첩 반복문의 외부·내부 반복 횟수를 추적할 수 있다.
- 구구단을 한 단씩 또는 여러 단씩 출력할 수 있다.
- 경계값을 조건문으로 검사해 존재하는 단만 출력할 수 있다.
- 세 번째 반복문을 이용해 반복되는 출력 코드를 일반화할 수 있다.
- `random.random()`과 `random.randint()`의 반환 범위를 구분할 수 있다.
- `while`이 조건이 참인 동안 반복한다는 점을 설명할 수 있다.
- 센티널 값을 이용해 반복 종료 조건을 구성할 수 있다.
- 반복 횟수를 카운트하는 변수를 사용할 수 있다.
- 문자열 누적 방식과 문자열 곱셈 방식으로 피라미드를 출력할 수 있다.
- `while True`가 무한 반복이라는 점을 이해한다.
- 터미널에서 실행 중인 무한 반복을 `Ctrl+C`로 중단할 수 있다.
- `break`와 `continue`의 역할을 구분할 수 있다.
- 나머지 연산자와 조건문을 결합해 `FizzBuzz`를 작성할 수 있다.
- 여러 조건이 동시에 참일 수 있을 때 조건 순서가 중요함을 설명할 수 있다.
- 내 코드와 강사님 코드의 구조 및 실행 차이를 비교할 수 있다.
- 원본 코드의 주석 처리된 시행착오에서 오류 원인을 찾을 수 있다.

---
# 1. 원본 코드

## 1.1 내 코드

```python

for i in range(5) :
    print(i, end=' ')

print()

# reversed() 는 뭐가 되었든 거꾸로 바꿔주는 역할
for i in reversed(range(5)) :
    print(i, end=' ')

print()

# if는 아끼지 말고 쓰고 한 단계씩 조립하기!!
for i in range(2,10,3) :
    for j in range(1,10) :
        print(f'''{i} x {j} = {i*j}''', end=' ')
        if i+1 < 10 :
            print(f'''{i+1} x {j} = {(i+1)*j}''', end=' ')
        if i+2 < 10 :
            print(f'''{i+2} x {j} = {(i+2)*j}''', end=' ')
        print()
    print()

# import로 random을 불러와서 사용할 수 있음
import random
print( random.random() )
print( random.randint(1, 6) )

# 주사위 3이 몇 번만에 나오는지 출력하시오
# i = 0
# count = 0
# while i != 3 :
#     i = random.randint(1, 6)
#     count += int(1)
#     if result == 3 :
#         print( result )
#         print( f'{count}번' )

count = 0
dice = 0
while dice != 3 :
    dice = random.randint(1, 6)
    count += 1
    if dice == 3 :
        print(count)
    

print('-'*30)
# Pyramid_Python(JavaScript ver)
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

# Pyramid_Python(Python verFinal)
inputUser = int(input('줄 수 : '))
for j in range(1,inputUser+1) :
    print(' '*(inputUser-j),end='')
    print('*'*((j+j)-1),end='')
    print(' '*(inputUser-j))

# inputUser = int(input('줄 수 : '))
# # for i in range(1) :
# for j in range(1,inputUser+1) :
#     print(' '*(inputUser-j),end='')
#     print('*'*((j+j)-1),end='')
#     print(' '*(inputUser-j))
# # print()
# for i in range(1) :
#     for j in range(1,10,2) :
#         print('-'*(10-j),end='')
#         print('*'*j,end='')
#         print('-'*(10-j))
#     print()

import turtle as t
t.shape('turtle')

# 터미널 무한반복 탈출은 Ctrl+C
# while True :
#     print(1)

# Fizz, Buzz 3과 5의 공배수 Fizz!Buzz! / 3배수 Fizz! / 5배수 Buzz!
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

## 1.2 강사님 코드

```python
for i in range(5) :
    print(i, end=' ')
print()
for i in reversed(range(5)) :
    print(i, end=' ')


print('-'*30)
# 구구단
# j = 2
# for i in range(1, 9+1) :
#     print(f'2x{i}={2*i}')
# j = 3
# for i in range(1, 9+1) :
#     print(f'{j}x{i}={j*i}')

for j in range(2, 9+1) :
    for i in range(1, 9+1) :
        print(f'{j}x{i}={j*i}')


print('-'*30)
# 구구단인데 3단씩 옆으로
'''
2x1=2  3x1=3  4x1=4
...

5x1=5  6x1=6  7x1=7
...

8x1=8  9x1=9
'''

# i = 2, 5, 8
i = 2
j = range(1, 10)
# for j in range(1, 10) :
#     print(f'{i}x{j}={i*j}  {i+1}x{j}={(i+1)*j}  {i+2}x{j}={(i+j)*1}')

# for i in range(2, 10, 3) :
#     for j in range(1, 10) :
#         if i+2 < 10 :
#             print(f'{i}x{j}={i*j}  {i+1}x{j}={(i+1)*j}  {i+2}x{j}={(i+j)*1}')
#         else :
#             print(f'{i}x{j}={i*j}  {i+1}x{j}={(i+1)*j}')

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


import random
print( random.random() )
print( random.randint(1, 6) )

print('-'*12)
# 주사위 3이 몇번만에 나오는지 출력
dice = -1
count = 0
while dice != 3 :
    dice = random.randint(1, 6)
    count += 1
    if dice == 3 :
        print(count)


import turtle as t
t.shape('turtle')

while True :
    print(1)
```

---
# 2. 반복문이란?

반복문은 같은 코드 또는 일정한 규칙을 가진 코드를 여러 번 실행하는 제어문입니다.

```text
반복할 데이터 또는 조건 준비
→ 반복할 때마다 코드 실행
→ 다음 값 또는 다음 상태로 이동
→ 종료 기준에 도달하면 반복 종료
```

Python의 대표 반복문은 `for`와 `while`입니다.

---
# 3. `for`와 `while` 비교

| 반복문 | 기준 | 적합한 상황 |
| --- | --- | --- |
| `for` | 반복 가능한 객체의 값 | 반복 대상이나 횟수가 비교적 명확할 때 |
| `while` | 조건식의 참·거짓 | 종료 시점을 조건으로 판단할 때 |

```python
for number in range(5):
    print(number)
```

```python
number = 0
while number < 5:
    print(number)
    number += 1
```

---
# 4. `for` 기본 구조

```python
for 반복변수 in 반복가능객체:
    실행문
```

예:

```python
for i in range(5):
    print(i)
```

`range(5)`가 제공하는 값을 하나씩 `i`에 대입하고 들여쓰기된 블록을 실행합니다.

---
# 5. 반복 변수의 역할

```python
for i in range(5):
    print(i)
```

반복할 때마다 `i`는 다음 값으로 바뀝니다.

```text
첫 번째 반복 → i = 0
두 번째 반복 → i = 1
세 번째 반복 → i = 2
네 번째 반복 → i = 3
다섯 번째 반복 → i = 4
```

반복 변수 이름은 문법적으로 자유롭지만 의미를 드러내는 이름이 좋습니다.

---
# 6. 원본의 첫 번째 `for`

공통 원본:

```python
for i in range(5):
    print(i, end=' ')
```

출력:

```text
0 1 2 3 4 
```

`range(5)`는 `0`부터 `4`까지 생성합니다.

---
# 7. `range(stop)`

```python
range(5)
```

의 범위:

```text
0, 1, 2, 3, 4
```

종료값 `5`는 포함되지 않습니다.

```text
시작값 기본값 → 0
증가값 기본값 → 1
종료값 → 미포함
```

---
# 8. 종료값이 포함되지 않는 이유

Python의 범위와 슬라이싱은 종료 위치를 포함하지 않는 규칙을 자주 사용합니다.

```python
range(0, 5)
```

반복 횟수는 `5 - 0`, 즉 다섯 번입니다. 길이 계산과 인덱스 범위를 연결하기 편리합니다.

---
# 9. `range(start, stop)`

```python
for i in range(2, 5):
    print(i)
```

출력:

```text
2
3
4
```

시작값은 포함하고 종료값은 포함하지 않습니다.

---
# 10. `range(start, stop, step)`

```python
for i in range(2, 10, 3):
    print(i)
```

출력:

```text
2
5
8
```

원본의 3단 묶음 구구단에서 시작 단이 `2`, `5`, `8`로 이동하는 데 사용됩니다.

---
# 11. 음수 `step`

감소하는 범위는 음수 간격으로 만들 수 있습니다.

```python
for i in range(4, -1, -1):
    print(i, end=' ')
```

출력:

```text
4 3 2 1 0
```

종료값 `-1`은 포함되지 않으므로 `0`까지 출력됩니다.

---
# 12. `range()`의 빈 범위

```python
for i in range(5, 0):
    print(i)
```

기본 간격은 `+1`인데 시작값이 종료값보다 크므로 생성되는 값이 없습니다. 감소하려면 세 번째 인자에 음수를 작성해야 합니다.

---
# 13. `print()`의 `end`

기본 `print()`는 출력 후 줄바꿈합니다.

```python
print(1)
print(2)
```

`end=' '`를 지정하면 줄바꿈 대신 공백을 출력합니다.

```python
print(1, end=' ')
print(2, end=' ')
```

출력:

```text
1 2 
```

---
# 14. 빈 `print()`로 줄바꿈

원본:

```python
for i in range(5):
    print(i, end=' ')

print()
```

반복문에서 줄바꿈을 막았으므로 빈 `print()`를 호출해 다음 출력 전에 줄을 바꿉니다.

---
# 15. `reversed()`

공통 원본:

```python
for i in reversed(range(5)):
    print(i, end=' ')
```

출력:

```text
4 3 2 1 0 
```

`reversed()`는 역순으로 순회할 수 있는 반복자를 반환합니다.

---
# 16. `reversed()`는 원본을 직접 수정하지 않는다

```python
numbers = range(5)
reverse_numbers = reversed(numbers)
```

`numbers` 자체가 바뀌는 것이 아니라 역순으로 값을 제공하는 별도 반복자가 만들어집니다.

---
# 17. `reversed()` 설명 보완

내 코드 주석:

```python
# reversed() 는 뭐가 되었든 거꾸로 바꿔주는 역할
```

`reversed()`가 모든 객체에 무조건 적용되는 것은 아닙니다. 일반적으로 역순 순회를 지원하는 시퀀스나 `__reversed__()`를 구현한 객체에 사용할 수 있습니다.

```python
reversed([1, 2, 3])
reversed("abc")
reversed(range(5))
```

집합처럼 순서 개념에 의존하지 않는 객체에는 그대로 사용할 수 없습니다.

---
# 18. `reversed(range())`와 음수 간격 비교

두 방식 모두 역순 범위를 만들 수 있습니다.

```python
reversed(range(5))
range(4, -1, -1)
```

첫 방식은 기존 범위를 역순으로 읽고, 두 번째 방식은 감소하는 범위를 직접 정의합니다.

---
# 19. 중첩 반복문

반복문 안에 다른 반복문을 작성할 수 있습니다.

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

외부 반복 한 번마다 내부 반복이 처음부터 끝까지 실행됩니다.

---
# 20. 중첩 반복문의 실행 횟수

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

외부 2회 × 내부 3회이므로 `print()`는 총 6회 실행됩니다.

---
# 21. 강사님 코드의 기본 구구단

```python
for j in range(2, 10):
    for i in range(1, 10):
        print(f'{j}x{i}={j*i}')
```

외부 반복은 단을 결정하고 내부 반복은 곱하는 수를 결정합니다.

```text
j → 2단부터 9단
 i → 1부터 9
```

---
# 22. 구구단 변수의 의미

구구단에서는 다음처럼 의미 있는 이름을 사용할 수도 있습니다.

```python
for dan in range(2, 10):
    for number in range(1, 10):
        print(f'{dan} x {number} = {dan * number}')
```

짧은 예제에서는 `i`, `j`가 흔하지만 반복 역할이 여러 개라면 이름을 구체화하면 읽기 쉽습니다.

---
# 23. 원본의 3단씩 출력 구조

내 코드:

```python
for i in range(2, 10, 3):
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}', end=' ')
        if i+1 < 10:
            print(f'{i+1} x {j} = {(i+1)*j}', end=' ')
        if i+2 < 10:
            print(f'{i+2} x {j} = {(i+2)*j}', end=' ')
        print()
    print()
```

외부 반복값은 `2`, `5`, `8`이며 각 시작 단에서 최대 세 단을 가로로 출력합니다.

---
# 24. 3단 묶음의 외부 반복값

```python
range(2, 10, 3)
```

결과:

```text
2, 5, 8
```

각 값은 묶음의 첫 단입니다.

```text
2 → 2, 3, 4단
5 → 5, 6, 7단
8 → 8, 9단
```

---
# 25. 마지막 묶음의 경계 검사

마지막 시작값 `8`에서 `i + 2`는 `10`입니다.

```python
if i + 2 < 10:
```

조건이 거짓이므로 10단을 출력하지 않습니다. 경계 검사가 없으면 의도하지 않은 10단까지 출력될 수 있습니다.

---
# 26. `if`를 단계적으로 조립하는 방식

내 코드 주석:

```python
# if는 아끼지 말고 쓰고 한 단계씩 조립하기!!
```

초기 구현에서는 각 경우를 명시적으로 작성해 실행 흐름을 확인하는 방식이 도움이 됩니다.

```python
print(i)
if i + 1 < 10:
    print(i + 1)
if i + 2 < 10:
    print(i + 2)
```

동작을 확인한 뒤 반복되는 패턴을 추가 반복문으로 일반화할 수 있습니다.

---
# 27. 강사님 코드의 일반화된 3단 묶음

```python
k = 14
for i in range(2, k+1, 3):
    for j in range(1, 10):
        for m in range(3):
            if i+m <= k:
                print(f'{i+m}x{j}={(i+m)*j}', end='	')
        print()
    print()
```

`m`이 `0`, `1`, `2`로 바뀌면서 현재 시작 단부터 최대 세 단을 출력합니다.

---
# 28. 세 번째 반복문의 역할

```python
for m in range(3):
```

은 다음 세 코드를 일반화합니다.

```python
print(i)
print(i + 1)
print(i + 2)
```

반복되는 코드의 차이가 일정한 숫자 변화라면 반복문으로 줄일 수 있습니다.

---
# 29. 최대 단수 `k`

강사님 코드는 최대 단수를 변수로 분리합니다.

```python
k = 14
```

```python
if i + m <= k:
```

덕분에 9단에 고정되지 않고 `k`를 바꾸어 출력 범위를 조정할 수 있습니다.

---
# 30. `< 10`과 `<= k` 비교

내 코드:

```python
if i + 1 < 10:
```

강사님 코드:

```python
if i + m <= k:
```

내 코드는 9단까지라는 고정 경계를 검사하고, 강사님 코드는 변수 `k`를 포함하는 동적 경계를 검사합니다.

---
# 31. 탭 출력 `	`

강사님 코드:

```python
print(..., end='	')
```

`	`는 탭 문자입니다. 여러 결과를 열처럼 띄우는 데 사용할 수 있지만 문자열 길이가 다르면 완벽하게 정렬되지 않을 수 있습니다.

---
# 32. 중첩 반복문을 읽는 순서

중첩 반복문은 바깥쪽부터 역할을 정합니다.

```text
외부 i → 단 묶음 시작값
중간 j → 곱하는 수
내부 m → 현재 묶음의 열 위치
```

각 반복 변수의 역할을 먼저 적으면 구조를 추적하기 쉽습니다.

---
# 33. `random` 모듈 가져오기

공통 원본:

```python
import random
```

`random` 모듈의 함수는 모듈 이름과 점을 사용해 호출합니다.

```python
random.random()
random.randint(1, 6)
```

---
# 34. `random.random()`

```python
print(random.random())
```

`0.0` 이상 `1.0` 미만의 실수를 반환합니다.

```text
0.0 <= 결과 < 1.0
```

실행할 때마다 결과가 달라질 수 있습니다.

---
# 35. `random.randint(a, b)`

```python
print(random.randint(1, 6))
```

양쪽 경계가 모두 포함됩니다.

```text
1, 2, 3, 4, 5, 6 중 하나
```

주사위 값을 만들기에 적합합니다.

---
# 36. 난수 결과는 고정되지 않는다

난수 예제는 실행할 때마다 출력이 달라질 수 있습니다. 따라서 문서나 테스트에서 특정 값이 반드시 나온다고 가정하면 안 됩니다.

재현 가능한 테스트가 필요할 때는 시드를 지정할 수 있습니다.

```python
random.seed(1)
```

다만 원본에는 시드 설정이 없습니다.

---
# 37. `while` 기본 구조

```python
while 조건식:
    실행문
```

조건이 참인 동안 블록을 반복합니다. 반복 블록 안에서 조건 결과가 언젠가 거짓이 되도록 상태를 변경해야 합니다.

---
# 38. 주사위 3이 나올 때까지 반복

공통 흐름:

```python
count = 0
dice = 0

while dice != 3:
    dice = random.randint(1, 6)
    count += 1
    if dice == 3:
        print(count)
```

주사위 값이 `3`이 될 때까지 반복하고 몇 번째 시도인지 출력합니다.

---
# 39. 센티널 값

센티널 값은 반복 시작 또는 종료를 구분하기 위해 사용하는 특별한 초기값이나 종료값입니다.

```python
dice = 0
```

주사위 실제 범위가 `1`부터 `6`이므로 `0`은 아직 던지지 않았음을 나타내는 초기값으로 사용할 수 있습니다.

---
# 40. 강사님 코드의 초기값 `-1`

```python
dice = -1
```

`-1`도 주사위 범위 밖의 값이므로 초기 센티널로 사용할 수 있습니다.

내 코드의 `0`과 강사님 코드의 `-1`은 이 반복에서 같은 목적을 수행합니다.

---
# 41. 카운터 변수

```python
count = 0
count += 1
```

주사위를 한 번 생성할 때마다 `count`를 1 증가시킵니다. 반복 횟수를 세려면 증가 위치가 실제 시도 위치와 일치해야 합니다.

---
# 42. 종료 조건과 출력 조건

```python
while dice != 3:
```

은 반복 지속 조건입니다.

```python
if dice == 3:
    print(count)
```

은 목표값이 나온 순간 출력하는 조건입니다. 반복이 끝난 뒤 출력하도록 구조를 단순화할 수도 있습니다.

```python
while dice != 3:
    dice = random.randint(1, 6)
    count += 1

print(count)
```

---
# 43. 주석 처리된 시행착오의 변수 오류

내 코드 주석에는 다음 흐름이 있습니다.

```python
# i = random.randint(1, 6)
# if result == 3:
#     print(result)
```

난수는 `i`에 저장했지만 조건과 출력에서는 선언되지 않은 `result`를 사용합니다. 실행하면 `NameError`가 발생합니다. 같은 값을 다룰 때 변수 이름을 일관되게 사용해야 합니다.

---
# 44. `count += int(1)` 보완

주석 처리된 코드:

```python
count += int(1)
```

`int(1)`은 이미 정수인 `1`을 다시 정수로 변환하므로 필요하지 않습니다.

```python
count += 1
```

이 더 직접적입니다.

---
# 45. 확률적 반복의 횟수

주사위에서 3이 첫 번째에 나올 수도 있고 여러 번 뒤에 나올 수도 있습니다. 따라서 반복 횟수는 고정되지 않습니다.

조건상 언젠가 끝날 가능성은 매우 높지만 실행 횟수의 상한은 코드에 지정되어 있지 않습니다.

---
# 46. 무한 반복 위험

종료 상태가 바뀌지 않으면 `while`은 끝나지 않습니다.

```python
dice = 0
while dice != 3:
    count += 1
```

위 코드는 `dice`를 변경하지 않으므로 무한 반복입니다.

---
# 47. 피라미드 출력의 목표

내 코드는 입력한 줄 수에 맞춰 별 피라미드를 출력합니다.

줄 수가 4라면:

```text
   *
  ***
 *****
*******
```

각 줄은 왼쪽 공백, 별, 오른쪽 공백으로 구성됩니다.

---
# 48. 피라미드 줄별 규칙

전체 줄 수를 `n`, 현재 줄을 `j`라고 하면:

```text
왼쪽 공백 수 → n - j
별 수 → 2 × j - 1
오른쪽 공백 수 → n - j
```

현재 줄이 내려갈수록 공백은 하나씩 줄고 별은 두 개씩 늘어납니다.

---
# 49. JavaScript 방식의 문자열 누적

내 코드:

```python
inputUser = int(input('줄 수 : '))
for k in range(0, inputUser+1):
    result = ''
    for m in range(0, inputUser-k):
        result += ' '
    for i in range(0, (k+k)-1):
        result += '*'
    for j in range(0, inputUser-k):
        result += ' '
    print(result)
```

내부 반복문으로 공백과 별을 하나씩 문자열에 누적합니다.

---
# 50. 첫 번째 피라미드의 `k = 0`

```python
for k in range(0, inputUser + 1):
```

첫 반복에서 `k = 0`이면 별 반복 범위는:

```python
range(0, -1)
```

이 되어 별이 출력되지 않습니다. 따라서 맨 처음에 공백만 있는 줄이 하나 출력될 수 있습니다.

의도한 줄 수만 출력하려면 `range(1, inputUser + 1)`이 더 자연스럽습니다.

---
# 51. 문자열 누적 방식의 특징

```python
result += ' '
result += '*'
```

규칙을 단계별로 확인하기에는 직관적이지만 단순한 동일 문자 반복은 문자열 곱셈이 더 간결합니다.

---
# 52. Python 방식의 문자열 곱셈

내 코드의 최종 방식:

```python
inputUser = int(input('줄 수 : '))
for j in range(1, inputUser+1):
    print(' '*(inputUser-j), end='')
    print('*'*((j+j)-1), end='')
    print(' '*(inputUser-j))
```

문자열에 정수를 곱해 같은 문자를 원하는 개수만큼 생성합니다.

---
# 53. 별 개수 식 단순화

원본:

```python
(j + j) - 1
```

같은 의미:

```python
2 * j - 1
```

피라미드의 홀수 별 개수 규칙을 `2 * j - 1`로 표현하면 의미를 알아보기 쉽습니다.

---
# 54. 오른쪽 공백은 출력에 꼭 필요한가?

터미널에서 피라미드 모양만 확인한다면 오른쪽 공백은 보통 생략할 수 있습니다.

```python
for j in range(1, inputUser + 1):
    print(' ' * (inputUser - j) + '*' * (2 * j - 1))
```

다만 고정 너비 문자열을 만들거나 이후 다른 문자열과 결합한다면 오른쪽 공백도 의미가 있을 수 있습니다.

---
# 55. 문자열 결합으로 한 번에 출력

세 번의 `print()`를 하나로 합칠 수 있습니다.

```python
for line in range(1, height + 1):
    spaces = ' ' * (height - line)
    stars = '*' * (2 * line - 1)
    print(spaces + stars)
```

중간 값을 변수로 분리하면 규칙을 읽기 쉽습니다.

---
# 56. 입력값 검증

원본은 다음을 전제로 합니다.

```python
inputUser = int(input('줄 수 : '))
```

숫자가 아닌 문자열을 입력하면 `ValueError`가 발생합니다. 음수나 0을 입력하면 출력 줄이 없거나 의도와 다른 결과가 나올 수 있습니다. 본문 원본은 기본 반복 구조 학습에 초점을 두고 있어 별도 예외 처리는 포함하지 않습니다.

---
# 57. `turtle` 모듈

공통 원본 일부:

```python
import turtle as t
t.shape('turtle')
```

`turtle` 모듈을 `t`라는 별칭으로 가져옵니다. `shape('turtle')`은 거북이 커서 모양을 설정합니다.

---
# 58. GUI 환경과 `turtle`

`turtle`은 그래픽 창을 사용하는 표준 라이브러리입니다. GUI를 사용할 수 없는 환경이나 원격 터미널에서는 정상 동작하지 않을 수 있습니다.

반복문 학습 코드와 그래픽 코드를 같은 파일에서 실행하면 창 동작 때문에 이후 출력 확인 방식이 달라질 수 있습니다.

---
# 59. 강사님 코드의 무한 반복

강사님 코드 마지막:

```python
while True:
    print(1)
```

조건이 항상 `True`이므로 사용자가 중단하거나 프로세스가 종료될 때까지 `1`을 계속 출력합니다.

---
# 60. `while True`의 사용 목적

무한 반복은 항상 잘못된 문법은 아닙니다. 입력 루프, 서버 대기, 게임 루프처럼 명시적인 종료 명령이 있을 때 자주 사용합니다.

```python
while True:
    command = input('명령: ')
    if command == 'quit':
        break
```

반드시 종료 경로를 함께 설계해야 합니다.

---
# 61. 터미널에서 `Ctrl+C`

내 코드 주석:

```python
# 터미널 무한반복 탈출은 Ctrl+C
```

터미널에서 실행 중인 Python 프로그램에 인터럽트 신호를 보내며 일반적으로 `KeyboardInterrupt`로 중단됩니다.

---
# 62. `break`

`break`는 가장 가까운 반복문을 즉시 종료합니다.

```python
while True:
    value = input('종료하려면 q: ')
    if value == 'q':
        break
```

중첩 반복문에서는 현재 `break`가 포함된 가장 안쪽 반복문만 종료합니다.

---
# 63. `continue`

`continue`는 현재 반복의 남은 코드를 건너뛰고 다음 반복으로 이동합니다.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

출력:

```text
0
1
3
4
```

---
# 64. `pass`, `break`, `continue` 비교

| 문장 | 역할 |
| --- | --- |
| `pass` | 아무 동작 없이 현재 흐름 계속 |
| `break` | 반복문 즉시 종료 |
| `continue` | 현재 회차의 나머지를 건너뛰고 다음 회차로 이동 |

세 문장은 서로 대체 관계가 아닙니다.

---
# 65. `for-else`와 `while-else`

Python 반복문에는 선택적으로 `else`를 붙일 수 있습니다.

```python
for number in range(3):
    print(number)
else:
    print('정상 종료')
```

`break` 없이 반복이 끝나면 `else` 블록이 실행됩니다. 원본에는 직접 등장하지 않지만 반복문 문법에서 알아둘 수 있는 보충 개념입니다.

---
# 66. FizzBuzz의 목표

내 코드 마지막은 `0`부터 `99`까지 값을 검사해 다음 규칙으로 출력합니다.

```text
3과 5의 공배수 → Fizz!Buzz!
3의 배수 → Fizz!
5의 배수 → Buzz!
그 외 → 숫자
```

---
# 67. 원본 FizzBuzz 코드

```python
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz!Buzz!')
    elif i % 3 == 0:
        print('Fizz!')
    elif i % 5 == 0:
        print('Buzz!')
    else:
        print(i)
```

---
# 68. 나머지 연산자와 배수 검사

```python
i % 3 == 0
```

은 `i`를 3으로 나눈 나머지가 0인지 검사합니다. 나머지가 0이면 3의 배수입니다.

---
# 69. 공배수 조건을 먼저 검사하는 이유

15는 3의 배수이면서 5의 배수입니다.

```python
if i % 3 == 0:
```

을 먼저 작성하면 15에서 바로 `Fizz!`가 실행되고 뒤의 조건은 검사하지 않습니다. 더 구체적인 공배수 조건을 먼저 배치해야 합니다.

---
# 70. FizzBuzz와 `0`

원본은 `range(100)`이므로 `0`부터 시작합니다.

수학적으로 `0 % 3 == 0`이고 `0 % 5 == 0`이므로 첫 출력은 `Fizz!Buzz!`입니다.

일반적인 FizzBuzz가 1부터 100까지를 의도한다면:

```python
for i in range(1, 101):
```

을 사용합니다. 원본의 범위는 문법 오류가 아니라 시작값 선택의 차이입니다.

---
# 71. 100의 포함 여부

```python
range(100)
```

은 `0`부터 `99`까지입니다. 숫자 100은 포함되지 않습니다.

1부터 100까지 포함하려면:

```python
range(1, 101)
```

---
# 72. 공배수 조건의 다른 표현

```python
i % 3 == 0 and i % 5 == 0
```

은 다음처럼 15의 배수 검사로 표현할 수도 있습니다.

```python
i % 15 == 0
```

원본 표현은 3과 5의 두 조건을 직접 보여 주므로 학습 목적에 명확합니다.

---
# 73. 반복문과 조건문의 결합

반복문은 값을 차례대로 제공하고 조건문은 각 값을 분류합니다.

```text
for → 다음 숫자 선택
if/elif/else → 숫자에 맞는 출력 선택
```

FizzBuzz, 필터링, 검색, 집계에서 자주 사용하는 구조입니다.

---
# 74. 반복 중 누적

반복문은 문자열뿐 아니라 숫자도 누적할 수 있습니다.

```python
total = 0
for number in range(1, 6):
    total += number

print(total)
```

출력:

```text
15
```

---
# 75. 반복 중 리스트에 저장

```python
squares = []
for number in range(1, 6):
    squares.append(number ** 2)
```

반복 결과를 나중에 사용해야 한다면 리스트 등에 저장할 수 있습니다. 출력만 하면 결과를 다시 사용하기 어렵습니다.

---
# 76. 반복 변수를 사용하지 않는 경우

반복 횟수만 필요하고 값은 사용하지 않을 때 관례적으로 `_`를 사용할 수 있습니다.

```python
for _ in range(3):
    print('실행')
```

`_`도 실제 변수이지만 사용하지 않을 의도를 나타냅니다.

---
# 77. 반복 중 변수의 마지막 값

```python
for i in range(5):
    pass

print(i)
```

반복이 한 번 이상 실행되었다면 반복 후 `i`에는 마지막 값 `4`가 남습니다. 그러나 빈 범위라면 변수가 한 번도 대입되지 않아 이후 접근에서 오류가 날 수 있습니다.

---
# 78. 반복문에서 컬렉션 직접 순회

`range()`만 반복할 수 있는 것은 아닙니다.

```python
for fruit in ['사과', '바나나', '키위']:
    print(fruit)
```

문자열, 리스트, 튜플, 딕셔너리 등 반복 가능한 객체를 사용할 수 있습니다.

---
# 79. 딕셔너리 반복과 연결

```python
user = {'name': '홍길동', 'age': 30}

for key, value in user.items():
    print(key, value)
```

07번에서 학습한 `items()`는 반복문에서 키와 값을 함께 꺼낼 때 사용합니다.

---
# 80. `enumerate()` 보충

반복 대상의 값과 순번이 함께 필요할 수 있습니다.

```python
fruits = ['사과', '바나나']

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

원본에는 직접 등장하지 않지만 인덱스를 별도로 증가시키는 코드를 줄일 수 있습니다.

---
# 81. 자주 하는 실수: 콜론 누락

잘못된 코드:

```python
for i in range(5)
    print(i)
```

반복문 머리 끝에는 콜론이 필요합니다.

```python
for i in range(5):
    print(i)
```

---
# 82. 자주 하는 실수: 들여쓰기 누락

```python
for i in range(5):
print(i)
```

반복할 블록은 들여쓰기해야 합니다. Python은 들여쓰기로 반복문 범위를 결정합니다.

---
# 83. 자주 하는 실수: 종료값 포함으로 착각

```python
for i in range(1, 10):
```

은 `1`부터 `9`까지입니다. 10까지 포함하려면 종료값을 11로 지정합니다.

---
# 84. 자주 하는 실수: `step`에 0 사용

```python
range(1, 10, 0)
```

간격 0은 다음 값으로 이동할 수 없으므로 `ValueError`가 발생합니다.

---
# 85. 자주 하는 실수: 감소 범위 방향 불일치

```python
range(5, 0, 1)
```

시작값은 크지만 간격이 양수이므로 빈 범위입니다.

```python
range(5, 0, -1)
```

처럼 방향에 맞는 간격을 사용해야 합니다.

---
# 86. 자주 하는 실수: `while` 상태 미변경

```python
count = 0
while count < 5:
    print(count)
```

`count`가 바뀌지 않아 무한 반복됩니다.

```python
count += 1
```

처럼 종료 조건에 영향을 주는 변경이 필요합니다.

---
# 87. 자주 하는 실수: 증가 위치 오류

```python
while dice != 3:
    count += 1
    dice = random.randint(1, 6)
```

이 구조도 시도 횟수는 맞게 셀 수 있지만, 어떤 동작을 한 번의 시도로 볼지 명확히 해야 합니다. 카운터 증가는 실제 반복 작업과 가까운 위치에 두는 것이 읽기 쉽습니다.

---
# 88. 자주 하는 실수: 변수 이름 불일치

```python
dice = random.randint(1, 6)
if result == 3:
    ...
```

저장 변수와 검사 변수가 다르면 `NameError` 또는 잘못된 상태 검사가 발생합니다.

---
# 89. 자주 하는 실수: 내부 반복 변수 혼동

중첩 반복문에서 `i`, `j`, `m`의 역할을 혼동하면 계산식이 달라질 수 있습니다.

```python
(i + j) * 1
```

과

```python
(i + 2) * j
```

은 전혀 다른 계산입니다. 강사님 주석 처리된 초기 구구단 코드에는 이러한 시행착오가 남아 있으며, 최종 코드는 `(i + m) * j`로 일반화합니다.

---
# 90. 자주 하는 실수: 너무 깊은 중첩

반복문과 조건문이 여러 단계로 중첩되면 흐름을 추적하기 어려워집니다.

다음 방법을 고려할 수 있습니다.

```text
반복되는 부분을 함수로 분리
중간 결과를 변수로 분리
continue로 불필요한 중첩 감소
반복 변수에 의미 있는 이름 사용
```

---
# 91. 자주 하는 실수: 난수 결과를 고정값으로 예상

```python
random.randint(1, 6)
```

은 실행할 때마다 달라질 수 있습니다. 한 번 실행한 출력값을 프로그램의 고정 동작으로 문서화하면 안 됩니다.

---
# 92. 자주 하는 실수: FizzBuzz 조건 순서

```python
if i % 3 == 0:
    print('Fizz')
elif i % 5 == 0:
    print('Buzz')
elif i % 15 == 0:
    print('FizzBuzz')
```

15는 첫 조건에서 이미 처리되므로 마지막 조건에 도달하지 않습니다. 공배수 조건을 먼저 작성합니다.

---
# 93. 반복문 설계 순서

```text
1. 무엇을 반복할지 정한다.
2. 횟수 기반인지 조건 기반인지 결정한다.
3. for 또는 while을 선택한다.
4. 반복 변수와 상태 변수의 역할을 정한다.
5. 시작값과 종료값을 확인한다.
6. 반복할 때마다 무엇이 변하는지 확인한다.
7. 종료 조건에 실제로 도달하는지 확인한다.
8. 경계값과 첫 번째·마지막 반복을 테스트한다.
9. 중첩 횟수가 예상과 맞는지 확인한다.
```

---
# 94. 반복 횟수 추적 방법

중첩 반복문을 이해하기 어려우면 작은 범위로 줄여 출력합니다.

```python
for i in range(2):
    print('외부 시작', i)
    for j in range(3):
        print('  내부', j)
    print('외부 종료', i)
```

반복문의 진입과 종료를 표시하면 실행 순서를 확인할 수 있습니다.

---
# 95. 경계값 테스트

`range(1, n + 1)`을 사용할 때 다음 값을 확인할 수 있습니다.

```text
n = 0
n = 1
n = 2
```

피라미드에서는:

```text
입력 0 → 출력 없음
입력 1 → 별 1개
입력 2 → 1개, 3개
```

작은 경계값은 범위 오류를 찾기 좋습니다.

---
# 96. My Code vs Teacher Code

## 전체 흐름 비교

| 항목 | 내 코드 | 강사님 코드 | 분석 |
| --- | --- | --- | --- |
| 기본 `for` | `range(5)` | 동일 | 같은 순방향 반복 |
| 역순 반복 | `reversed(range(5))` | 동일 | 같은 역순 출력 |
| 빈 줄 처리 | 역순 뒤 `print()` 포함 | 역순 뒤 명시적 빈 `print()` 없음 | 이후 구분선 출력 위치가 다를 수 있음 |
| 기본 구구단 | 없음 | 2단~9단 세로 출력 | 강사님 코드에 기본 단계 포함 |
| 3단 묶음 | 세 개의 출력과 두 `if` | 세 번째 `for`로 일반화 | 강사님 코드가 최대 단수 확장에 유리 |
| 최대 단수 | 9단 고정 | `k = 14` | 강사님 코드가 변수로 범위 제어 |
| 난수 | 동일 | 동일 | `random()`과 `randint()` 사용 |
| 주사위 초기값 | `0` | `-1` | 둘 다 실제 범위 밖 센티널 |
| 주사위 출력 | 3이 나오면 내부에서 출력 | 동일 | 구조 거의 동일 |
| 주석 시행착오 | `result` 변수 오류 흔적 | 구구단 계산식 시행착오 | 학습 과정 기록 위치가 다름 |
| 피라미드 | 두 방식 포함 | 없음 | 내 코드에만 추가 |
| `turtle` | 포함 | 포함 | 같은 모듈 별칭과 모양 설정 |
| 무한 반복 | 주석 처리 | 활성화 | 강사님 파일은 직접 실행 시 계속 출력 |
| FizzBuzz | 포함 | 없음 | 내 코드에만 추가 |

## 핵심 차이

내 코드는 수업 내용을 바탕으로 피라미드와 FizzBuzz까지 추가 실습했으며, 3단 묶음을 먼저 명시적인 `if` 구조로 조립했습니다. 강사님 코드는 기본 구구단에서 시작한 뒤 세 번째 반복문을 사용해 최대 14단까지 일반화했습니다.

강사님 코드의 마지막 `while True`는 활성화되어 있으므로 파일을 그대로 실행하면 수동 중단 전까지 끝나지 않습니다. 내 코드에서는 같은 무한 반복이 주석 처리되어 있어 이후 FizzBuzz까지 실행될 수 있습니다.

---
# 97. 원본 코드의 실행 순서 주의

내 코드에는 두 번의 `input()`과 `turtle` 그래픽 호출이 있습니다.

```text
기본 반복 출력
→ 구구단
→ 난수
→ 주사위 while
→ 첫 번째 피라미드 입력
→ 두 번째 피라미드 입력
→ turtle 창
→ FizzBuzz
```

실행 환경과 입력 대기 때문에 모든 출력이 한 번에 나타나지 않을 수 있습니다.

강사님 코드는 마지막 무한 반복 때문에 프로그램이 자연 종료되지 않습니다.

---
# 98. 복습 질문

## 질문 1

`range(5)`가 생성하는 값은 무엇인가?

## 질문 2

`range(2, 10, 3)`의 값은 무엇인가?

## 질문 3

`reversed(range(5))`는 어떤 순서로 값을 제공하는가?

## 질문 4

중첩 반복문에서 외부 3회, 내부 4회라면 내부 실행문은 총 몇 번 실행되는가?

## 질문 5

`random.randint(1, 6)`에서 6이 나올 수 있는가?

## 질문 6

`while` 반복이 무한 반복이 되는 대표 원인은 무엇인가?

## 질문 7

`break`와 `continue`의 차이는 무엇인가?

## 질문 8

피라미드의 `j`번째 줄 별 개수는 어떻게 계산하는가?

## 질문 9

FizzBuzz에서 공배수 조건을 먼저 검사해야 하는 이유는 무엇인가?

## 질문 10

원본의 `range(100)`은 1부터 100까지인가?

---
# 99. Problems

다음 문제는 반복문 핵심 문법을 확인하기 위한 복습 문제입니다. 전체 Python 단원의 종합 Quiz와 상세 분석은 별도 Quiz 문서에서 진행합니다.

## 문제 1

`for`와 `range()`를 사용해 `0 1 2 3 4`를 한 줄에 출력하세요.

## 문제 2

`5 4 3 2 1`을 역순으로 출력하세요.

## 문제 3

`range(2, 11, 2)`가 제공하는 값을 적으세요.

## 문제 4

2단을 1부터 9까지 출력하세요.

## 문제 5

2단부터 9단까지 중첩 반복문으로 출력하세요.

## 문제 6

1부터 100까지 숫자의 합을 구하세요.

## 문제 7

1부터 20까지 짝수만 출력하세요.

## 문제 8

주사위를 반복해서 던져 6이 나오면 반복을 끝내고 시도 횟수를 출력하세요.

## 문제 9

`while`로 1부터 5까지 출력하세요.

## 문제 10

높이 5인 왼쪽 정렬 별 삼각형을 출력하세요.

## 문제 11

높이 5인 중앙 정렬 피라미드를 출력하세요.

## 문제 12

1부터 100까지 FizzBuzz를 출력하세요.

## 문제 13

다음 코드가 무한 반복되는 이유를 설명하세요.

```python
count = 0
while count < 3:
    print(count)
```

## 문제 14

다음 코드의 출력에서 빠지는 숫자를 적으세요.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

## 문제 15

다음 `break`가 외부 반복문까지 종료하는지 설명하세요.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
```

---
# 100. Answers

## 정답 1

```python
for i in range(5):
    print(i, end=' ')
```

## 정답 2

```python
for i in range(5, 0, -1):
    print(i, end=' ')
```

또는:

```python
for i in reversed(range(1, 6)):
    print(i, end=' ')
```

## 정답 3

```text
2, 4, 6, 8, 10
```

## 정답 4

```python
for number in range(1, 10):
    print(f'2 x {number} = {2 * number}')
```

## 정답 5

```python
for dan in range(2, 10):
    for number in range(1, 10):
        print(f'{dan} x {number} = {dan * number}')
```

## 정답 6

```python
total = 0
for number in range(1, 101):
    total += number

print(total)
```

## 정답 7

```python
for number in range(2, 21, 2):
    print(number)
```

## 정답 8

```python
import random

count = 0
dice = 0

while dice != 6:
    dice = random.randint(1, 6)
    count += 1

print(count)
```

## 정답 9

```python
number = 1
while number <= 5:
    print(number)
    number += 1
```

## 정답 10

```python
for line in range(1, 6):
    print('*' * line)
```

## 정답 11

```python
height = 5
for line in range(1, height + 1):
    print(' ' * (height - line) + '*' * (2 * line - 1))
```

## 정답 12

```python
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('Fizz!Buzz!')
    elif number % 3 == 0:
        print('Fizz!')
    elif number % 5 == 0:
        print('Buzz!')
    else:
        print(number)
```

## 정답 13

`count`가 반복문 안에서 증가하지 않으므로 조건 `count < 3`이 계속 참입니다.

## 정답 14

숫자 `2`가 출력되지 않습니다.

## 정답 15

가장 안쪽의 `for j`만 종료합니다. 외부 `for i`는 다음 반복을 계속합니다.

---
# 101. Final Checklist

- [ ] 반복문이 같은 작업을 여러 번 실행하는 제어문임을 설명할 수 있다.
- [ ] `for`와 `while`의 선택 기준을 구분할 수 있다.
- [ ] `for 변수 in 반복가능객체:` 구조를 작성할 수 있다.
- [ ] 반복 변수가 매 반복마다 다음 값을 받는다는 점을 안다.
- [ ] `range(stop)`이 0부터 시작함을 안다.
- [ ] `range()`의 종료값이 포함되지 않음을 안다.
- [ ] `range(start, stop)`을 작성할 수 있다.
- [ ] `range(start, stop, step)`을 작성할 수 있다.
- [ ] 양수와 음수 `step`의 방향을 구분할 수 있다.
- [ ] `step=0`이 허용되지 않음을 안다.
- [ ] 빈 범위가 만들어지는 조건을 설명할 수 있다.
- [ ] `print(..., end=' ')`로 줄바꿈을 제어할 수 있다.
- [ ] 빈 `print()`로 줄을 바꿀 수 있다.
- [ ] `reversed()`로 역순 순회할 수 있다.
- [ ] `reversed()`가 원본을 직접 뒤집어 수정하는 것이 아님을 안다.
- [ ] `reversed()`가 모든 객체에 무조건 적용되는 것은 아님을 안다.
- [ ] 중첩 반복문의 실행 순서를 추적할 수 있다.
- [ ] 외부 반복 횟수와 내부 반복 횟수로 총 실행 횟수를 계산할 수 있다.
- [ ] 중첩 반복문으로 구구단을 출력할 수 있다.
- [ ] 세 단씩 옆으로 출력하는 구조를 이해한다.
- [ ] 마지막 묶음에서 경계 검사가 필요한 이유를 안다.
- [ ] 반복되는 세 개의 출력을 세 번째 반복문으로 일반화할 수 있다.
- [ ] 최대 단수를 변수로 분리할 수 있다.
- [ ] 탭 문자 `\t`의 역할을 안다.
- [ ] `import random`으로 난수 모듈을 사용할 수 있다.
- [ ] `random.random()`의 범위를 안다.
- [ ] `random.randint(a, b)`가 양쪽 경계를 포함함을 안다.
- [ ] 난수 출력이 실행마다 달라질 수 있음을 안다.
- [ ] `while 조건식:`의 기본 구조를 작성할 수 있다.
- [ ] `while` 조건이 참인 동안 반복함을 안다.
- [ ] 센티널 값의 목적을 설명할 수 있다.
- [ ] 반복 횟수를 카운터로 셀 수 있다.
- [ ] 주사위 목표값이 나올 때까지 반복할 수 있다.
- [ ] `while` 안에서 종료 조건에 영향을 주는 상태를 변경할 수 있다.
- [ ] 변수 이름 불일치에서 `NameError`가 발생할 수 있음을 안다.
- [ ] 불필요한 `int(1)` 변환을 제거할 수 있다.
- [ ] 확률적 반복의 횟수가 고정되지 않음을 안다.
- [ ] 피라미드의 공백과 별 개수 규칙을 설명할 수 있다.
- [ ] 문자열 누적으로 피라미드를 만들 수 있다.
- [ ] 문자열 곱셈으로 같은 문자를 반복할 수 있다.
- [ ] 첫 피라미드 코드의 `k=0`이 빈 별 줄을 만들 수 있음을 안다.
- [ ] `2 * line - 1`로 홀수 개의 별을 계산할 수 있다.
- [ ] 숫자가 아닌 입력에서 `ValueError`가 발생할 수 있음을 안다.
- [ ] `turtle` 모듈이 GUI 환경을 사용할 수 있음을 안다.
- [ ] `while True`가 무한 반복임을 안다.
- [ ] 터미널에서 `Ctrl+C`로 실행을 중단할 수 있음을 안다.
- [ ] `break`가 가장 가까운 반복문을 종료함을 안다.
- [ ] `continue`가 현재 회차의 남은 코드를 건너뜀을 안다.
- [ ] `pass`, `break`, `continue`를 구분할 수 있다.
- [ ] 반복문의 `else`가 `break` 없이 종료될 때 실행됨을 안다.
- [ ] 나머지 연산자로 배수를 검사할 수 있다.
- [ ] FizzBuzz의 공배수 조건을 먼저 검사할 수 있다.
- [ ] `range(100)`이 0부터 99까지임을 안다.
- [ ] 1부터 100까지는 `range(1, 101)`임을 안다.
- [ ] 반복문과 조건문을 결합해 값을 분류할 수 있다.
- [ ] 반복 중 숫자 또는 문자열을 누적할 수 있다.
- [ ] 반복 결과를 리스트에 저장할 수 있다.
- [ ] 반복값을 사용하지 않을 때 `_`를 사용할 수 있다.
- [ ] 리스트와 딕셔너리를 직접 순회할 수 있다.
- [ ] `enumerate()`로 인덱스와 값을 함께 얻을 수 있다.
- [ ] 콜론과 들여쓰기 오류를 찾을 수 있다.
- [ ] 감소 범위에서 간격 방향을 올바르게 지정할 수 있다.
- [ ] 중첩 반복 변수의 역할을 구분할 수 있다.
- [ ] 내 코드와 강사님 코드의 3단 묶음 구현 차이를 설명할 수 있다.
- [ ] 강사님 코드의 활성화된 무한 반복이 이후 자연 종료를 막음을 안다.
- [ ] 내 코드에만 피라미드와 FizzBuzz가 포함됨을 안다.
- [ ] 반복문의 첫 값, 마지막 값, 종료 조건을 검토할 수 있다.
- [ ] 추가 종합 문제의 상세 풀이가 최종 Quiz 문서에서 진행됨을 확인했다.

---
# 102. Key Summary

기본 `for`:

```python
for value in iterable:
    print(value)
```

`range()`:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

```text
시작값 포함
종료값 미포함
step 기본값 1
```

순방향과 역방향:

```python
for i in range(5):
    print(i, end=' ')

for i in reversed(range(5)):
    print(i, end=' ')
```

중첩 반복문:

```python
for dan in range(2, 10):
    for number in range(1, 10):
        print(f'{dan} x {number} = {dan * number}')
```

기본 `while`:

```python
while condition:
    print('조건이 참인 동안 반복')
```

주사위 반복:

```python
import random

count = 0
dice = 0

while dice != 3:
    dice = random.randint(1, 6)
    count += 1

print(count)
```

피라미드:

```python
height = 5

for line in range(1, height + 1):
    spaces = ' ' * (height - line)
    stars = '*' * (2 * line - 1)
    print(spaces + stars)
```

반복 흐름 제어:

```text
pass
→ 아무 동작 없이 계속

continue
→ 현재 회차 나머지 생략

break
→ 가장 가까운 반복문 종료
```

FizzBuzz:

```python
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('Fizz!Buzz!')
    elif number % 3 == 0:
        print('Fizz!')
    elif number % 5 == 0:
        print('Buzz!')
    else:
        print(number)
```

원본 핵심 흐름:

```text
for와 range
→ reversed
→ 중첩 반복문
→ 구구단
→ 반복 코드 일반화
→ random
→ while과 센티널
→ 피라미드
→ turtle
→ 무한 반복
→ FizzBuzz
```

반복문은 단순히 같은 문장을 되풀이하는 문법이 아닙니다. 반복 대상, 시작값, 종료값, 증가 규칙, 상태 변화, 종료 조건을 함께 설계해야 합니다. 특히 중첩 반복문에서는 각 변수의 역할을 분리하고, `while`에서는 조건이 실제로 거짓이 될 수 있는지 확인해야 의도하지 않은 무한 반복을 피할 수 있습니다.
