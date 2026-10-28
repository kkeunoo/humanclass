# 09-02. `while`과 반복 제어 — 언제 멈출까

[Python 목차](README.md) · [이전: `for`](09-01_Python_for와_range.md)

양쪽 원본은 난수로 주사위 3이 나올 때까지 돌고, 마지막에 `while`–`else`와 `break`를 연습한다. 난수의 실제 횟수는 실행할 때마다 달라지므로 고정된 숫자로 외우지 않는다.

## 먼저: 반복을 멈추는 조건

`while`은 조건이 참인 동안 같은 블록을 반복한다. **반복 중 무엇이 바뀌어 조건이 거짓이 되는가?**를 먼저 찾는다.

```python
# 수업 문법으로 만든 설명용 재구성
number = 1
while number < 3:
    print(number)
    number += 1
# 출력: 1, 2를 각각 한 줄씩
```

첫 검사에서 1<3, 다음에는 2<3이어서 출력하고, 3<3이 거짓이 되면 멈춘다. 아래 주사위 원본에서는 `number += 1` 대신 **새 난수와 횟수**가 바뀌는지 추적한다.

<!-- chapter-toc -->

- [1. 주사위 3이 나올 때까지](09-02_Python_while과_반복제어.md#section-1)
- [2. `break`를 만나지 않았을 때의 `else`](09-02_Python_while과_반복제어.md#section-2)
- [3. 강사님 원본의 추가 반복 예시](09-02_Python_while과_반복제어.md#section-3)
- [직접 확인할 질문](09-02_Python_while과_반복제어.md#section-4)
- [추가로 알면 좋은 것](09-02_Python_while과_반복제어.md#section-5)

<a id="section-1"></a>

## 1. 주사위 3이 나올 때까지

### 강사님 코드

출처: `teacher/workspace_python/_09_for.py` 63–75행 · **원본 발췌**

```python
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
```

### 내 코드

출처: `me/workspace_python/09_for.py` 25–46행 · **원본 발췌**

```python
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
    
```

`random.randint(1, 6)`은 여기서 1부터 6까지의 정수를 하나 고른다. `dice != 3`인 동안 한 번 뽑을 때마다 `count`를 늘리고, 3이 나오면 그 횟수를 출력한다. 강사님은 `dice=-1`, 나는 `dice=0`으로 시작하지만 둘 다 처음에는 3이 아니므로 루프에 진입한다. 내 파일의 위쪽 주석 처리된 `while` 시도에는 정의되지 않은 `result`가 등장한다. **실행되는 것은 그 아래 `dice`를 사용한 버전**이다.

<a id="section-2"></a>

## 2. `break`를 만나지 않았을 때의 `else`

### 강사님 코드

출처: `teacher/workspace_python/_09_for.py` 92–101행 · **원본 발췌**

```python
a = 20
i = 0
while i < 10 :
    if i == a :
        print('찾음')
        break
    i += 1
else :
    print('못찾음')
# while의 else는 break를 만나지 않고 종료되는 경우 else문 실행 됨
```

### 내 코드

출처: `me/workspace_python/09_for.py` 101–110행 · **원본 발췌**

```python
a = 20
i = 0
while i < 10 :
    if i == a :
        print('찾음')
        break
    i += 1
else :
    print('못찾음')
# while의 else는 break를 만나지 않고 조건식에 의해 종료되는 경우 else문 실행 됨
```

두 파일 모두 `a=20`을 찾지만 `i`는 0부터 9까지만 검사한다. `i == a`가 참이 되는 때가 없으므로 `break`를 만나지 않고 `while` 조건이 거짓이 된다. 그 결과 `else`에서 **`못찾음`**을 출력한다. 여기서 `else`는 `if`의 `else`가 아니라 **`while`에 붙은 `else`**다. 반대로 찾은 순간 `break`로 나가면 그 `else`는 실행하지 않는다.

<a id="section-3"></a>

## 3. 강사님 원본의 추가 반복 예시

### 강사님 코드

출처: `teacher/workspace_python/_09_for.py` 78–91행 · **원본 발췌**

```python
import turtle as t
t.shape('turtle')

# while True :
#     print(1)


a = [  i*10 if i%2 == 0 else i for i in range(10)  ]
for i in range(10) :
    if i%2 == 0:
        a.append(i*10)
    else :
        a.append(i)

```

### 내 코드

출처: `me/workspace_python/09_for.py` 83–89행 · **원본 발췌**

```python
import turtle as t
t.shape('turtle')

# 터미널 무한반복 탈출은 Ctrl+C
# while True :
#     print(1)

```

강사님 파일은 `turtle`을 불러 모양을 지정하고, 리스트 컴프리헨션으로 만든 `a`에 이어 `for`로 값을 **다시 추가**한다. 따라서 주석처럼 “같은 결과의 두 방식 중 하나”로만 읽으면 실제 최종 리스트를 놓친다. 컴프리헨션으로 10개를 만든 뒤 다시 10개를 붙여 **20개**가 된다. 컴프리헨션 자체는 [리스트 참조·순회](04-02_Python_리스트참조와_컴프리헨션.md)에서 기본형을 다뤘다.

내 파일에도 `turtle` 호출과 주석 처리된 무한 반복 예시가 있다. `turtle`은 그래픽 창을 여는 도구이므로 여기서는 **코드를 읽는 근거**로만 사용했다. 반복을 멈추는 핵심은 실행되는 `while` 조건, `break`, `else`를 설명하는 데 있다.

<a id="section-4"></a>

## 직접 확인할 질문

1. `dice`를 처음에 `-1` 또는 `0`으로 둬도 같은 루프에 들어가는 이유는?
2. `a=20`을 찾는 코드에서 왜 `못찾음`이 나올까?
3. 강사님 리스트 `a`에는 마지막에 몇 개의 값이 있을까?

<a id="section-5"></a>

## 추가로 알면 좋은 것

난수를 재현하기 위한 시드 설정이나 `turtle` 그림을 만드는 상세 사용법은 두 원본의 반복문 핵심을 넘어간다. 이 장의 기준은 **실행되는 조건과 종료 경로**를 정확히 추적하는 것이다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/09-02_Python_while과_반복제어_연습문제.md) → [10-01. 텍스트 파일 읽고 쓰기](10-01_Python_텍스트파일_읽고쓰기.md)

