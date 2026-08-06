---
title: Python 반복문
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 반복문

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `09_Python_반복문.md` |
| 분류 | `04_Python` |
| 원본 기준 | `workspace_python/09_for.py`, `workspace_teacher/workspace_python/_09_for.py` |
| 핵심 범위 | `for`, `range()`, `reversed()`, 중첩 반복문, `while`, `break`, `continue`, 반복문 `else`, `random`, 문자열 반복 |
| 실습 범위 | 기본 반복, 구구단, 3단 묶음 출력, 주사위 반복, 피라미드, FizzBuzz, 값 검색 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 그대로 나열하지 않는다.  
> 반복문 구조와 실습 흐름에 필요한 코드만 발췌하고, 반복 횟수·종료 조건·중첩 구조·오류 가능성을 함께 설명한다.

---

# 개요

반복문은 같은 작업을 여러 번 실행할 때 사용한다.

```text
게시글 목록 출력
상품 목록 계산
구구단 생성
입력값 반복 확인
조건을 만족할 때까지 실행
    ↓
반복문 사용
```

Python의 대표적인 반복문은 `for`와 `while`이다.

```text
반복 가능한 객체의 값을 차례대로 처리
→ for

조건이 참인 동안 계속 실행
→ while
```

> [!IMPORTANT]
> 반복문에서 가장 중요한 것은 **무엇을 반복하는지**, **언제 종료되는지**, **반복마다 어떤 값이 바뀌는지**를 명확히 이해하는 것이다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| `for` | 반복 가능한 객체의 값을 차례대로 처리 |
| `range()` | 규칙적인 정수 범위 생성 |
| `reversed()` | 반복 순서를 역순으로 변경 |
| 중첩 반복문 | 반복문 안에 다른 반복문 작성 |
| `while` | 조건이 참인 동안 반복 |
| 반복 변수 | 현재 반복에서 사용하는 값 |
| `break` | 반복문 즉시 종료 |
| `continue` | 현재 반복만 건너뛰고 다음 반복 진행 |
| 반복문 `else` | `break` 없이 정상 종료될 때 실행 |
| 센티널 값 | 반복 종료 여부를 판단하는 특별한 값 |
| `random` | 난수 생성 기능 제공 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- `for`문의 기본 구조를 작성할 수 있다.
- `range()`의 시작값·종료값·증가값을 설명할 수 있다.
- `range()` 종료값이 포함되지 않는다는 점을 이해한다.
- `reversed()`로 역순 반복할 수 있다.
- `print()`의 `end`로 한 줄 출력을 제어할 수 있다.
- 중첩 반복문의 외부·내부 반복 순서를 설명할 수 있다.
- 구구단을 반복문으로 출력할 수 있다.
- 여러 단을 묶어 출력할 때 범위 검사가 필요한 이유를 이해한다.
- `random.random()`과 `random.randint()`의 차이를 구분할 수 있다.
- `while`문의 종료 조건을 설계할 수 있다.
- 센티널 값을 이용해 반복을 제어할 수 있다.
- `break`와 `continue`를 구분할 수 있다.
- 반복문 `else`의 실행 조건을 설명할 수 있다.
- 문자열 곱셈으로 공백과 별을 반복 출력할 수 있다.
- 피라미드 패턴을 반복문으로 만들 수 있다.
- FizzBuzz 조건의 순서가 중요한 이유를 설명할 수 있다.
- 무한 반복을 안전하게 종료할 수 있다.

---

# 1. `for` 기본 구조

## 1-1. 내 코드와 강사님 코드

```python
for i in range(5):
    print(i, end=" ")
```

## 1-2. 출력 결과

```text
0 1 2 3 4
```

## 1-3. 구성

| 요소 | 의미 |
| --- | --- |
| `for` | 반복문 시작 키워드 |
| `i` | 현재 반복값을 저장하는 변수 |
| `in` | 반복 가능한 객체에서 값을 꺼냄 |
| `range(5)` | 0부터 4까지의 범위 |
| `:` | 반복문 블록 시작 |
| 들여쓰기 | 반복할 코드 영역 |

---

# 2. `range()`와 종료값

```python
for number in range(5):
    print(number)
```

출력:

```text
0
1
2
3
4
```

`range(5)`에서 `5`는 포함되지 않는다.

```text
시작값
→ 0

종료값
→ 5 미포함
```

> [!TIP]
> 1부터 5까지 반복하려면 `range(1, 6)`을 사용한다.

---

# 3. `print()`의 `end`

기본 `print()`는 출력 후 줄을 바꾼다.

```python
for number in range(5):
    print(number)
```

한 줄에 이어서 출력하려면 `end`를 지정한다.

```python
for number in range(5):
    print(number, end=" ")
```

출력:

```text
0 1 2 3 4
```

반복이 끝난 뒤 줄바꿈:

```python
for number in range(5):
    print(number, end=" ")

print()
```

---

# 4. 의미 있는 반복 변수

학습 예제에서는 `i`, `j`를 자주 사용하지만 실제 코드에서는 값의 의미를 표현하는 이름이 더 좋다.

기존:

```python
for i in range(5):
    print(i)
```

개선:

```python
for page_number in range(1, 6):
    print(page_number)
```

> [!TIP]
> 짧은 수학적 반복에서는 `i`, `j`도 사용할 수 있지만, 업무 데이터를 순회할 때는 `user`, `product`, `score`처럼 의미 있는 이름을 사용한다.

---

# 5. `reversed()`

## 5-1. 내 코드와 강사님 코드

```python
for i in reversed(range(5)):
    print(i, end=" ")
```

## 5-2. 출력 결과

```text
4 3 2 1 0
```

## 5-3. 정확한 역할

내 코드 주석에는 다음과 같이 기록되어 있다.

```text
reversed()는 뭐가 되었든 거꾸로 바꿔주는 역할
```

정확하게는 `reversed()`가 지원되는 시퀀스나 역순 반복 가능한 객체를 **역순으로 순회할 수 있는 이터레이터**로 반환한다.

> [!IMPORTANT]
> 원본 객체 자체를 변경하는 것이 아니다.

---

# 6. 감소하는 `range()`

역순 숫자 반복은 음수 증가값으로도 작성할 수 있다.

```python
for number in range(4, -1, -1):
    print(number, end=" ")
```

출력:

```text
4 3 2 1 0
```

## 6-1. 선택 기준

```text
기존 시퀀스를 역순으로 순회
→ reversed()

숫자의 시작·종료·간격을 직접 제어
→ range(start, stop, negative_step)
```

---

# 7. 중첩 반복문

반복문 안에 다른 반복문을 작성할 수 있다.

```python
for row in range(2):
    for column in range(3):
        print(row, column)
```

출력:

```text
0 0
0 1
0 2
1 0
1 1
1 2
```

## 7-1. 실행 순서

```text
외부 row = 0
    ↓
내부 column = 0, 1, 2 전부 실행
    ↓
외부 row = 1
    ↓
내부 column = 0, 1, 2 전부 실행
```

---

# 8. 중첩 반복 횟수

외부 반복이 2번, 내부 반복이 3번이면 내부 코드는 총 6번 실행된다.

```text
2 × 3
→ 6회
```

> [!WARNING]
> 중첩 반복문의 데이터 크기가 커지면 실행 횟수가 빠르게 증가할 수 있다.

---

# 9. 기본 구구단

## 9-1. 강사님 코드

```python
for dan in range(2, 10):
    for number in range(1, 10):
        print(
            f"{dan}x{number}="
            f"{dan * number}"
        )
```

## 9-2. 출력 일부

```text
2x1=2
2x2=4
...
9x9=81
```

## 9-3. 역할

| 반복문 | 역할 |
| --- | --- |
| 외부 반복문 | 2단부터 9단까지 선택 |
| 내부 반복문 | 각 단의 1부터 9까지 계산 |

---

# 10. 구구단을 3단씩 묶기

내 코드와 강사님 코드에는 여러 단을 옆으로 묶어 출력하는 예제가 있다.

```python
for start_dan in range(2, 10, 3):
    for number in range(1, 10):
        for offset in range(3):
            dan = start_dan + offset

            if dan < 10:
                print(
                    f"{dan}x{number}="
                    f"{dan * number}",
                    end="\t",
                )

        print()

    print()
```

## 10-1. 출력 구조

```text
2단 3단 4단
5단 6단 7단
8단 9단
```

---

# 11. 범위 검사가 필요한 이유

마지막 묶음은 8단과 9단만 존재한다.

```text
start_dan = 8

8 + 0
→ 8단

8 + 1
→ 9단

8 + 2
→ 10단, 출력 범위 초과
```

따라서 다음 조건이 필요하다.

```python
if dan < 10:
    ...
```

내 코드의 메모처럼 복잡한 코드는 한 번에 만들기보다 조건을 단계별로 조립하는 방식이 좋다.

---

# 12. 중복 코드 줄이기

내 코드의 초기 방식은 각 단을 개별 `if`로 처리한다.

```python
if start_dan + 1 < 10:
    ...

if start_dan + 2 < 10:
    ...
```

강사님 코드의 최종 방식은 `offset` 반복문으로 중복을 줄인다.

```python
for offset in range(3):
    dan = start_dan + offset

    if dan <= max_dan:
        ...
```

> [!TIP]
> 비슷한 코드가 숫자만 바뀌며 반복되면 반복문으로 한 단계 더 일반화할 수 있는지 확인한다.

---

# 13. 최대 단수 확장

강사님 코드는 최대 단수를 변수로 관리한다.

```python
max_dan = 14

for start_dan in range(
    2,
    max_dan + 1,
    3,
):
    ...
```

`9`를 여러 위치에 직접 작성하는 것보다 확장하기 쉽다.

```text
정책값 직접 반복
→ 수정 위치가 많음

max_dan 변수
→ 한 곳에서 변경
```

---

# 14. `random` 모듈

## 14-1. 원본 코드

```python
import random
```

`random`은 난수를 생성하는 표준 라이브러리 모듈이다.

## 14-2. import 위치

실무에서는 일반적으로 파일 상단에 import를 모아 작성한다.

```python
import random


# 실행 코드
```

---

# 15. `random.random()`

```python
import random

value = random.random()

print(value)
```

출력 예:

```text
0.428193...
```

`0.0` 이상 `1.0` 미만의 실수를 반환한다.

```text
0.0 <= value < 1.0
```

실행할 때마다 결과가 달라질 수 있다.

---

# 16. `random.randint()`

```python
import random

value = random.randint(1, 6)

print(value)
```

출력 예:

```text
4
```

`randint(1, 6)`은 양쪽 끝값을 모두 포함한다.

```text
1 <= value <= 6
```

주사위처럼 정수 범위 난수가 필요할 때 사용할 수 있다.

---

# 17. `while` 기본 구조

```text
while 조건식:
    반복할 코드
```

조건식이 참인 동안 계속 실행한다.

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

출력:

```text
0
1
2
```

---

# 18. `while`에서 값 변경

다음 코드에서 `count += 1`이 없다면 조건이 계속 참이므로 무한 반복된다.

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

```text
초기값 설정
    ↓
조건 확인
    ↓
코드 실행
    ↓
조건에 사용되는 값 변경
    ↓
다시 조건 확인
```

> [!IMPORTANT]
> `while`문을 작성할 때는 조건을 언젠가 거짓으로 만드는 코드가 있는지 반드시 확인한다.

---

# 19. 센티널 값

특정 값이 나올 때까지 반복하는 경우, 그 값을 센티널 값으로 사용할 수 있다.

주사위 예제에서는 `3`이 반복 종료를 결정하는 값이다.

```text
주사위가 3이 아님
→ 반복

주사위가 3
→ 종료
```

---

# 20. 주사위 3이 나올 때까지 반복

## 20-1. 내 코드와 강사님 코드

```python
import random

count = 0
dice = 0

while dice != 3:
    dice = random.randint(1, 6)
    count += 1

    if dice == 3:
        print(count)
```

## 20-2. 출력 예

```text
5
```

난수이므로 실행마다 횟수가 달라진다.

---

# 21. 주사위 코드 단순화

반복문이 종료된 후에는 이미 `dice == 3`이므로 내부 `if` 없이 출력할 수 있다.

```python
import random

count = 0
dice = 0

while dice != 3:
    dice = random.randint(1, 6)
    count += 1

print(count)
```

> [!TIP]
> 반복 종료 조건과 같은 조건을 반복문 내부에서 다시 검사하고 있다면 중복 여부를 확인한다.

---

# 22. 초기값 선택

강사님 코드는 `dice = -1`, 내 코드는 `dice = 0`을 사용한다.

두 값 모두 주사위에서 나올 수 없는 값이므로 첫 반복을 시작할 수 있다.

```python
dice = 0
```

또는 무한 반복과 `break`를 사용할 수 있다.

```python
while True:
    dice = random.randint(1, 6)

    if dice == 3:
        break
```

---

# 23. `break`

`break`는 현재 반복문을 즉시 종료한다.

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

출력:

```text
0
1
2
3
4
```

`number == 5`가 되면 반복문 밖으로 이동한다.

---

# 24. 중첩 반복문의 `break`

`break`는 가장 가까운 반복문 하나만 종료한다.

```python
for row in range(3):
    for column in range(3):
        if column == 1:
            break

        print(row, column)
```

출력:

```text
0 0
1 0
2 0
```

내부 반복문만 종료되고 외부 반복문은 계속 진행된다.

---

# 25. `continue`

`continue`는 현재 반복의 남은 코드를 건너뛰고 다음 반복으로 이동한다.

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

출력:

```text
0
1
3
4
```

## 25-1. `break`와 비교

| 키워드 | 동작 |
| --- | --- |
| `break` | 반복문 전체 종료 |
| `continue` | 현재 반복만 건너뜀 |

---

# 26. 반복문 `else`

내 코드와 강사님 코드에는 `while·else` 예제가 있다.

```python
target = 20
number = 0

while number < 10:
    if number == target:
        print("찾음")
        break

    number += 1
else:
    print("못찾음")
```

출력:

```text
못찾음
```

---

# 27. 반복문 `else` 실행 조건

`else`는 조건식이 거짓이 되어 정상 종료되었을 때 실행된다.

```text
break로 종료
→ else 실행 안 함

조건식이 거짓이 되어 종료
→ else 실행
```

> [!IMPORTANT]
> 반복문 `else`는 조건문의 `else`와 연결된 것이 아니라 반복문 자체와 연결된다.

---

# 28. 검색과 반복문 `else`

```python
numbers = [10, 20, 30]
target = 25

for number in numbers:
    if number == target:
        print("찾음")
        break
else:
    print("못찾음")
```

출력:

```text
못찾음
```

검색 성공 여부를 위한 별도 불리언 변수를 만들지 않아도 된다.

---

# 29. `for`와 `while` 선택 기준

```text
반복 횟수나 대상이 명확
→ for

조건이 만족될 때까지 반복
→ while

무한 반복 후 특정 조건에서 종료
→ while True + break
```

예:

```text
사용자 목록 순회
→ for

올바른 입력이 들어올 때까지 요청
→ while
```

---

# 30. 문자열 반복

문자열에 정수를 곱하면 문자열을 반복할 수 있다.

```python
print("-" * 10)
print("*" * 5)
```

출력:

```text
----------
*****
```

패턴 출력에서 반복문 없이 한 줄의 공백과 별을 만들 수 있다.

---

# 31. 문자열 누적 방식

내 코드의 첫 피라미드 방식은 빈 문자열에 공백과 별을 반복해 더한다.

```python
row_text = ""

for _ in range(3):
    row_text += " "

for _ in range(5):
    row_text += "*"

print(row_text)
```

작은 학습 예제에서는 동작하지만, 반복적으로 문자열을 연결하면 새 문자열이 계속 생성된다.

---

# 32. 피라미드 규칙

줄 수가 5일 때 각 줄의 규칙은 다음과 같다.

```text
1번째 줄
공백 4개 + 별 1개

2번째 줄
공백 3개 + 별 3개

3번째 줄
공백 2개 + 별 5개
```

공식:

```text
왼쪽 공백
→ 전체 줄 수 - 현재 줄

별 개수
→ 현재 줄 × 2 - 1
```

---

# 33. Python 방식 피라미드

## 33-1. 내 코드 최종 방식

```python
line_count = int(
    input("줄 수: ")
)

for line in range(
    1,
    line_count + 1,
):
    spaces = " " * (
        line_count - line
    )
    stars = "*" * (
        line * 2 - 1
    )

    print(spaces + stars)
```

## 33-2. 입력

```text
4
```

## 33-3. 출력 결과

```text
   *
  ***
 *****
*******
```

---

# 34. 기존 피라미드와 개선 피라미드

기존 방식:

```text
공백 반복문
별 반복문
오른쪽 공백 반복문
문자열 누적
```

개선 방식:

```text
공백 문자열 곱셈
별 문자열 곱셈
한 번에 출력
```

> [!TIP]
> Python에서는 반복 가능한 값의 곱셈과 슬라이싱 같은 기본 기능을 이용하면 중첩 반복을 줄일 수 있다.

---

# 35. 오른쪽 공백은 필요한가?

콘솔에 피라미드를 출력할 때 오른쪽 공백은 화면 모양에 영향을 주지 않는 경우가 많다.

```python
print(spaces + stars)
```

파일에 고정 너비 데이터를 저장하거나 후속 문자열 처리가 필요할 때만 오른쪽 공백을 고려한다.

---

# 36. FizzBuzz

내 코드에는 FizzBuzz 실습이 있다.

규칙:

```text
3과 5의 공배수
→ Fizz!Buzz!

3의 배수
→ Fizz!

5의 배수
→ Buzz!

그 외
→ 숫자 출력
```

---

# 37. FizzBuzz 코드

```python
for number in range(1, 101):
    if (
        number % 3 == 0
        and number % 5 == 0
    ):
        print("Fizz!Buzz!")
    elif number % 3 == 0:
        print("Fizz!")
    elif number % 5 == 0:
        print("Buzz!")
    else:
        print(number)
```

`range(1, 101)`을 사용해 일반적인 FizzBuzz 범위인 1부터 100까지 출력한다.

---

# 38. FizzBuzz 조건 순서

공배수 조건을 먼저 확인해야 한다.

잘못된 순서:

```python
if number % 3 == 0:
    print("Fizz!")
elif (
    number % 3 == 0
    and number % 5 == 0
):
    print("Fizz!Buzz!")
```

15는 첫 번째 조건에서 이미 처리되므로 공배수 분기에 도달하지 못한다.

```text
더 구체적인 조건
→ 먼저

더 넓은 조건
→ 나중
```

---

# 39. 0과 FizzBuzz

내 원본은 `range(100)`을 사용하므로 0부터 시작한다.

0은 모든 0이 아닌 정수의 배수로 볼 수 있으므로 첫 출력이 `Fizz!Buzz!`가 된다.

일반적인 문제 의도가 1부터 100이면 다음처럼 작성한다.

```python
range(1, 101)
```

---

# 40. 조건 표현식과 리스트 컴프리헨션

강사님 코드에는 짝수만 10배로 만드는 예제가 있다.

```python
numbers = [
    number * 10
    if number % 2 == 0
    else number
    for number in range(10)
]

print(numbers)
```

출력:

```text
[0, 1, 20, 3, 40, 5, 60, 7, 80, 9]
```

같은 로직을 일반 반복문으로 작성할 수도 있다.

---

# 41. 리스트 컴프리헨션과 반복문 비교

컴프리헨션:

```python
numbers = [
    number * 10
    if number % 2 == 0
    else number
    for number in range(10)
]
```

일반 반복문:

```python
numbers = []

for number in range(10):
    if number % 2 == 0:
        numbers.append(
            number * 10
        )
    else:
        numbers.append(number)
```

단순 변환은 컴프리헨션이 적합하지만, 처리 단계가 복잡하면 일반 반복문이 더 읽기 쉽다.

---

# 42. 무한 반복

```python
while True:
    print(1)
```

조건이 항상 참이므로 계속 실행된다.

터미널에서 실행 중이라면 일반적으로 `Ctrl + C`로 중단할 수 있다.

> [!WARNING]
> 무한 반복에는 정상 종료 경로 또는 외부 중단 방법이 반드시 있어야 한다.

---

# 43. 안전한 무한 반복

```python
while True:
    command = input(
        "명령어(exit 종료): "
    )

    if command == "exit":
        break

    print("입력:", command)
```

사용자가 `exit`를 입력하면 반복이 종료된다.

---

# 44. `turtle` 모듈

원본에는 다음 코드가 있다.

```python
import turtle as t

t.shape("turtle")
```

`turtle`은 화면에 거북이를 움직이며 그림을 그리는 학습용 그래픽 모듈이다.

`as t`는 모듈 이름에 별칭을 지정한 것이다.

```text
import turtle as t
→ turtle을 t라는 이름으로 사용
```

---

# 45. `turtle` 실행 환경 주의

`turtle`은 GUI 창을 사용한다.

다음 환경에서는 정상 표시되지 않을 수 있다.

- GUI가 없는 서버
- 일부 온라인 실행기
- 원격 터미널
- 창 표시가 제한된 환경

반복문 자체와 그래픽 환경 문제를 구분해야 한다.

---

# 46. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 기본 반복 | `range(5)`와 `reversed()` | 동일 |
| 구구단 | 3단 묶음 출력 중심 | 기본 전체 구구단과 확장 묶음 출력 |
| 중복 제거 | 각 단을 개별 `if`로 처리 | `offset` 반복문으로 일반화 |
| 난수 | 주사위 시행착오 주석 포함 | 완성된 주사위 코드 중심 |
| 피라미드 | 누적 방식과 Python 방식 모두 포함 | 별도 피라미드 없음 |
| FizzBuzz | 0부터 99까지 실행 | 별도 FizzBuzz 없음 |
| 리스트 변환 | 별도 없음 | 조건 표현식 컴프리헨션 포함 |
| 반복문 `else` | 설명 메모 포함 | 동일 예제 포함 |
| 무한 반복 | 주석 처리 | 원본에서 활성화된 코드가 있었음 |

## 46-1. 내 코드의 장점

- 3단씩 구구단을 출력하는 과정을 단계별로 직접 구현했다.
- 잘못 작성한 주사위 코드를 주석으로 남겨 수정 과정을 확인할 수 있다.
- 피라미드의 일반 반복 방식과 Python 문자열 곱셈 방식을 비교했다.
- FizzBuzz와 반복문 `else`까지 추가로 실습했다.

## 46-2. 내 코드의 개선점

- `reversed()`가 모든 객체 자체를 뒤집는 것은 아니다.
- 주사위 코드의 주석 버전에는 정의되지 않은 `result` 변수가 있다.
- 피라미드 변수 `inputUser`는 `line_count`처럼 snake_case로 개선할 수 있다.
- FizzBuzz를 1부터 100으로 구현하려면 `range(1, 101)`이 적합하다.
- import는 파일 상단에 모아 작성하는 것이 좋다.

## 46-3. 강사님 코드의 장점

- 기본 구구단에서 3단 묶음 확장까지 점진적으로 발전한다.
- 최대 단수를 변수로 관리하고 `offset` 반복문으로 중복을 줄였다.
- `while`, 난수, 리스트 컴프리헨션, 반복문 `else`까지 폭넓게 실습한다.

## 46-4. 강사님 코드의 보충점

- 활성화된 무한 반복은 뒤 코드를 실행하지 못하게 할 수 있어 주석 처리 또는 종료 조건이 필요하다.
- 리스트 컴프리헨션 예제에서 기존 리스트를 초기화하지 않으면 이전 값이 남을 수 있다.
- 반복문 `else`의 `break` 관계를 더 명확히 설명할 필요가 있다.

---

# 47. 기존 코드에서 개선 코드로 바꾼 이유

## 47-1. 변수명 개선

기존:

```python
inputUser = 5
```

개선:

```python
line_count = 5
```

Python 변수명 관례인 snake_case를 사용하고 값의 의미를 표현한다.

## 47-2. 구구단 중복 제거

기존:

```python
if start_dan + 1 < 10:
    ...

if start_dan + 2 < 10:
    ...
```

개선:

```python
for offset in range(3):
    dan = start_dan + offset

    if dan <= max_dan:
        ...
```

## 47-3. 주사위 중복 조건 제거

기존:

```python
while dice != 3:
    ...

    if dice == 3:
        print(count)
```

개선:

```python
while dice != 3:
    ...

print(count)
```

## 47-4. 피라미드 문자열 곱셈

기존:

```python
for _ in range(space_count):
    result += " "
```

개선:

```python
spaces = " " * space_count
```

---

# 48. 실무형 예제: 재고 있는 상품 검색

```python
products = [
    {
        "name": "Keyboard",
        "stock": 0,
    },
    {
        "name": "Mouse",
        "stock": 3,
    },
    {
        "name": "Monitor",
        "stock": 5,
    },
]

target_name = "Mouse"

for product in products:
    if (
        product["name"]
        != target_name
    ):
        continue

    if product["stock"] <= 0:
        print("재고가 없습니다.")
    else:
        print(
            f'{product["name"]}: '
            f'재고 {product["stock"]}개'
        )

    break
else:
    print("상품을 찾을 수 없습니다.")
```

## 48-1. 출력 결과

```text
Mouse: 재고 3개
```

## 48-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `for product in products` | 상품 목록 순회 |
| `continue` | 대상이 아닌 상품 건너뛰기 |
| 재고 조건문 | 품절 여부 확인 |
| `break` | 상품을 찾은 뒤 검색 종료 |
| 반복문 `else` | 끝까지 찾지 못한 경우 처리 |

---

# 49. 대표 오류로 이해하기

## 49-1. 들여쓰기 누락

```text
for number in range(3):
print(number)
```

발생 결과:

```text
IndentationError
```

---

## 49-2. 종료값 포함 착각

```python
for number in range(1, 5):
    print(number)
```

출력은 1부터 4까지다.

---

## 49-3. `while` 값 변경 누락

```python
count = 0

while count < 3:
    print(count)
```

무한 반복된다.

---

## 49-4. 정의되지 않은 변수 사용

내 코드의 주석 처리된 초기 주사위 코드에는 다음 조건이 있다.

```text
if result == 3:
```

`result`가 정의되지 않았다면 `NameError`가 발생한다.

개선:

```python
if dice == 3:
    ...
```

---

## 49-5. `break`가 모든 중첩 반복을 종료한다고 생각

가장 가까운 반복문 하나만 종료한다.

---

## 49-6. FizzBuzz 조건 순서 오류

3의 배수 조건을 공배수 조건보다 먼저 작성하면 15가 `Fizz!`로만 출력된다.

---

# 50. 자주 하는 실수

## 50-1. `range()`의 종료값이 포함된다고 생각

종료값 바로 앞까지만 반복한다.

## 50-2. 반복 변수 이름이 항상 `i`여야 한다고 생각

데이터 의미에 맞는 이름을 사용할 수 있다.

## 50-3. `reversed()`가 원본을 변경한다고 생각

역순 이터레이터를 반환한다.

## 50-4. 중첩 반복의 실행 횟수를 계산하지 않음

데이터가 커지면 성능 문제가 생길 수 있다.

## 50-5. `while` 종료 조건에 사용되는 값을 변경하지 않음

무한 반복이 발생한다.

## 50-6. `randint()`의 끝값이 제외된다고 생각

양쪽 끝값을 모두 포함한다.

## 50-7. `break`와 `continue` 혼동

`break`는 종료, `continue`는 다음 반복이다.

## 50-8. 반복문 `else`가 항상 실행된다고 생각

`break`로 종료되면 실행되지 않는다.

## 50-9. 문자열 누적 반복을 무조건 사용

문자열 곱셈으로 더 간단히 작성할 수 있는지 확인한다.

## 50-10. FizzBuzz의 넓은 조건을 먼저 작성

공배수 조건이 실행되지 않는다.

## 50-11. 무한 반복 뒤에 코드를 작성

반복이 종료되지 않으면 뒤 코드는 실행되지 않는다.

## 50-12. `turtle` 오류를 반복문 오류로 판단

GUI 실행 환경 문제일 수 있다.

---

# 51. 핵심 요약

```text
for
→ 반복 가능한 객체 순회

range()
→ 정수 범위 생성

reversed()
→ 역순 순회

중첩 반복문
→ 반복 안에서 다시 반복
```

```text
while
→ 조건이 참인 동안 반복

break
→ 반복 종료

continue
→ 현재 반복 건너뛰기

반복문 else
→ break 없이 종료될 때 실행
```

```text
random.random()
→ 0.0 이상 1.0 미만 실수

random.randint(a, b)
→ a 이상 b 이하 정수

문자열 * 정수
→ 문자열 반복
```

---

# 52. 최종 체크리스트

- [ ] `for`문의 기본 구조를 작성할 수 있는가?
- [ ] `range()`의 종료값이 포함되지 않음을 이해했는가?
- [ ] `end`로 반복 출력 형식을 조절할 수 있는가?
- [ ] `reversed()`로 역순 순회할 수 있는가?
- [ ] 감소하는 `range()`를 작성할 수 있는가?
- [ ] 중첩 반복문의 실행 순서를 설명할 수 있는가?
- [ ] 구구단을 중첩 반복문으로 출력할 수 있는가?
- [ ] 중복된 분기를 반복문으로 일반화할 수 있는가?
- [ ] `random.random()`과 `randint()`를 구분할 수 있는가?
- [ ] `while`의 종료 조건을 설계할 수 있는가?
- [ ] 센티널 값을 이용해 반복을 제어할 수 있는가?
- [ ] `break`와 `continue`를 구분할 수 있는가?
- [ ] 반복문 `else`의 실행 조건을 설명할 수 있는가?
- [ ] 문자열 곱셈으로 패턴을 출력할 수 있는가?
- [ ] 피라미드의 공백과 별 개수 규칙을 설명할 수 있는가?
- [ ] FizzBuzz 조건을 올바른 순서로 작성할 수 있는가?
- [ ] 무한 반복에 종료 경로를 만들 수 있는가?
- [ ] `turtle` 실행 환경 문제를 구분할 수 있는가?

---

# 마무리

반복문의 핵심은 코드를 여러 번 실행하는 것에서 끝나지 않는다.

```text
반복할 대상을 정하고
    ↓
현재 반복값을 사용하고
    ↓
필요한 조건을 검사하고
    ↓
종료 시점을 명확히 만들고
    ↓
중복 코드를 더 일반적인 구조로 개선하는 것
```

이 흐름을 이해하면 이후 함수에서 반복 로직을 분리하고, 클래스와 파일 처리에서 여러 데이터를 안정적으로 다룰 수 있다.
