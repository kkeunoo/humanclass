---
title: Python 제너레이터
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# Python 제너레이터

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `17_Python_제너레이터.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `11_Python_함수.md`, `16_Python_이터레이터.md` |
| 다음 학습 | `18_Python_정규표현식.md` |
| 문서 성격 | Python 확장 학습 문서 |
| 핵심 범위 | 제너레이터, `yield`, 실행 중단과 재개, 상태 유지, `next()`, `yield from`, 제너레이터 표현식 |
| 보충 범위 | `send()`, `throw()`, `close()`, 무한 제너레이터, 파일·대용량 데이터 처리 |
| 종합 실습 | 별도 문서 `20_Python_종합실습.md`에서 관리 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 제너레이터를 단순히 `yield` 문법으로 외우지 않고,  
> **함수의 실행 위치와 지역 변수가 어떻게 유지되는지** 이해하는 데 초점을 둔다.

---

# 개요

일반 함수는 호출되면 처음부터 끝까지 실행되고, `return`을 만나면 종료된다.

```text
일반 함수 호출
    ↓
처음부터 실행
    ↓
return
    ↓
값 반환
    ↓
함수 종료
```

제너레이터 함수는 `yield`를 만나면 값을 반환하면서 실행을 잠시 멈춘다.

```text
제너레이터 호출
    ↓
제너레이터 객체 생성
    ↓
next()
    ↓
yield까지 실행
    ↓
값 반환 + 현재 위치 저장
    ↓
다음 next()
    ↓
중단된 위치부터 이어서 실행
```

즉, 제너레이터는 값을 한 번에 모두 만들지 않고 **필요할 때 하나씩 생성**한다.

> [!IMPORTANT]
> 제너레이터 함수는 호출 즉시 내부 코드를 실행하지 않는다.
>
> 먼저 제너레이터 객체를 만들고, `next()`가 호출될 때 실제 실행을 시작한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 제너레이터 함수 | `yield`를 포함한 함수 |
| 제너레이터 객체 | 제너레이터 함수를 호출했을 때 반환되는 이터레이터 |
| `yield` | 값을 반환하고 함수 실행을 잠시 중단 |
| `next()` | 중단된 위치부터 실행을 재개 |
| 상태 유지 | 지역 변수와 실행 위치를 다음 호출까지 보존 |
| `StopIteration` | 제너레이터 실행이 끝났음을 알림 |
| 제너레이터 표현식 | 괄호를 사용한 간결한 제너레이터 생성 방식 |
| `yield from` | 다른 반복 가능한 객체의 값을 순서대로 전달 |
| `send()` | 제너레이터에 값을 전달하며 실행 재개 |
| `close()` | 제너레이터 종료 |
| `throw()` | 제너레이터 내부에 예외 전달 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 일반 함수와 제너레이터 함수의 차이를 설명할 수 있다.
- `yield`가 함수 종료가 아니라 실행 중단이라는 점을 이해한다.
- 제너레이터 함수를 호출하면 제너레이터 객체가 반환된다는 점을 안다.
- `next()`로 값을 하나씩 꺼낼 수 있다.
- 제너레이터가 지역 변수와 실행 위치를 유지한다는 점을 설명할 수 있다.
- 제너레이터 종료 시 `StopIteration`이 발생하는 이유를 이해한다.
- `for`문에서 제너레이터를 사용할 수 있다.
- 제너레이터 표현식을 작성할 수 있다.
- 리스트 컴프리헨션과 제너레이터 표현식을 비교할 수 있다.
- `yield from`으로 다른 반복 가능한 객체의 값을 전달할 수 있다.
- 무한 제너레이터를 안전하게 사용할 수 있다.
- `send()`, `close()`, `throw()`의 기본 목적을 설명할 수 있다.
- 파일과 대용량 데이터를 순차 처리할 때 제너레이터를 활용할 수 있다.
- 제너레이터가 항상 무조건 더 좋은 선택은 아니라는 점을 이해한다.

---

# 1. 일반 함수와 제너레이터 함수

## 1-1. 일반 함수

```python
def get_numbers():
    return [1, 2, 3]
```

실행:

```python
result = get_numbers()

print(result)
```

출력:

```text
[1, 2, 3]
```

일반 함수는 리스트 전체를 만든 뒤 한 번에 반환한다.

## 1-2. 제너레이터 함수

```python
def generate_numbers():
    yield 1
    yield 2
    yield 3
```

실행:

```python
generator = generate_numbers()

print(generator)
```

출력 형태:

```text
<generator object generate_numbers at ...>
```

함수를 호출했지만 `1`, `2`, `3`이 바로 출력되거나 반환되지 않는다.

## 1-3. 핵심 차이

| 구분 | 일반 함수 | 제너레이터 함수 |
| --- | --- | --- |
| 핵심 키워드 | `return` | `yield` |
| 호출 결과 | 계산된 값 | 제너레이터 객체 |
| 실행 시점 | 호출 즉시 | `next()` 또는 반복 시 |
| 상태 유지 | 함수 종료 후 사라짐 | 중단 위치와 지역 변수 유지 |
| 값 반환 방식 | 한 번에 반환 | 하나씩 반환 |

---

# 2. `yield`란?

`yield`는 값을 반환하면서 함수 실행을 잠시 멈춘다.

```python
def generate_numbers():
    yield 1
    yield 2
    yield 3
```

## 2-1. 실행

```python
generator = generate_numbers()

print(next(generator))
print(next(generator))
print(next(generator))
```

## 2-2. 출력 결과

```text
1
2
3
```

## 2-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `yield 1` | 첫 번째 값을 반환하고 실행을 멈추기 위해 |
| `yield 2` | 다음 호출에서 두 번째 값을 반환하기 위해 |
| `yield 3` | 다음 호출에서 세 번째 값을 반환하기 위해 |
| `next(generator)` | 제너레이터 실행을 시작하거나 재개하기 위해 |

> [!TIP]
> `yield`는 값을 반환하지만 함수가 완전히 종료되지는 않는다.
>
> 다음 `next()` 호출을 기다리며 현재 위치를 기억한다.

---

# 3. 제너레이터 함수는 호출 즉시 실행되지 않는다

```python
def sample_generator():
    print("함수 시작")
    yield 1
    print("함수 재개")
    yield 2
```

## 3-1. 객체 생성

```python
generator = sample_generator()

print("객체 생성 완료")
```

출력:

```text
객체 생성 완료
```

`함수 시작`은 아직 출력되지 않는다.

## 3-2. 첫 번째 `next()`

```python
print(next(generator))
```

출력:

```text
함수 시작
1
```

## 3-3. 두 번째 `next()`

```python
print(next(generator))
```

출력:

```text
함수 재개
2
```

## 3-4. 동작 과정

```text
sample_generator() 호출
    ↓
제너레이터 객체만 생성
    ↓
내부 코드 실행 안 됨

첫 번째 next()
    ↓
함수 시작부터 실행
    ↓
yield 1
    ↓
1 반환 + 실행 중단

두 번째 next()
    ↓
yield 1 다음 줄부터 재개
    ↓
함수 재개 출력
    ↓
yield 2
```

> [!IMPORTANT]
> 제너레이터 함수의 본문은 객체 생성 시점이 아니라 첫 번째 `next()` 호출 시점부터 실행된다.

---

# 4. 실행 위치와 지역 변수 유지

```python
def counter():
    number = 1

    while number <= 3:
        yield number
        number += 1
```

## 4-1. 실행

```python
generator = counter()

print(next(generator))
print(next(generator))
print(next(generator))
```

## 4-2. 출력 결과

```text
1
2
3
```

## 4-3. 상태 변화

```text
첫 번째 next()
number = 1
yield 1
현재 number = 1 상태로 중단

두 번째 next()
yield 다음 줄부터 재개
number += 1
number = 2
yield 2

세 번째 next()
number += 1
number = 3
yield 3
```

> [!IMPORTANT]
> 제너레이터는 지역 변수와 실행 위치를 다음 호출까지 유지한다.
>
> 일반 함수처럼 매번 처음부터 다시 실행되지 않는다.

---

# 5. 제너레이터 종료와 `StopIteration`

모든 `yield`가 끝난 뒤 다시 `next()`를 호출하면 `StopIteration`이 발생한다.

```python
def generate_numbers():
    yield 1
    yield 2
```

```python
generator = generate_numbers()

print(next(generator))
print(next(generator))
print(next(generator))
```

출력:

```text
1
2
StopIteration
```

## 5-1. 종료 흐름

```text
마지막 yield 반환
    ↓
다음 next()
    ↓
함수 끝까지 실행
    ↓
StopIteration 발생
```

`for`문은 이 예외를 자동으로 처리한다.

---

# 6. `for`문에서 제너레이터 사용

```python
def generate_numbers():
    yield 1
    yield 2
    yield 3
```

```python
for number in generate_numbers():
    print(number)
```

출력:

```text
1
2
3
```

`for`문은 내부적으로 다음과 비슷하게 동작한다.

```python
generator = generate_numbers()

while True:
    try:
        number = next(generator)
    except StopIteration:
        break

    print(number)
```

> [!TIP]
> 직접 `next()`를 호출해야 할 특별한 이유가 없다면 일반적으로 `for`문이 더 안전하고 읽기 쉽다.

---

# 7. `return`과 `yield` 차이

## 7-1. `return`

```python
def normal_function():
    return 1
    return 2
```

실행:

```python
print(normal_function())
```

출력:

```text
1
```

첫 번째 `return`에서 함수가 종료되므로 두 번째 `return`은 실행되지 않는다.

## 7-2. `yield`

```python
def generator_function():
    yield 1
    yield 2
```

실행:

```python
for value in generator_function():
    print(value)
```

출력:

```text
1
2
```

## 7-3. 비교

| 구분 | `return` | `yield` |
| --- | --- | --- |
| 값 반환 | 한 번 | 여러 번 가능 |
| 함수 실행 | 종료 | 일시 중단 |
| 다음 호출 | 새로 함수 호출 | 중단 위치부터 재개 |
| 상태 유지 | 종료 후 사라짐 | 유지됨 |
| 반환 객체 | 일반 값 | 제너레이터 객체를 통해 값 제공 |

---

# 8. 제너레이터 안의 `return`

제너레이터 함수 안에서도 `return`을 사용할 수 있다.

```python
def generate_numbers():
    yield 1
    return
    yield 2
```

실행:

```python
for number in generate_numbers():
    print(number)
```

출력:

```text
1
```

`return`을 만나면 제너레이터가 종료된다.

```text
yield 1
    ↓
다음 실행에서 return
    ↓
StopIteration
```

> [!WARNING]
> 제너레이터 안의 `return`은 값을 계속 반환하는 기능이 아니라 제너레이터를 종료하는 역할을 한다.

---

# 9. `yield`를 반복문과 함께 사용

```python
def generate_range(start, stop):
    current = start

    while current <= stop:
        yield current
        current += 1
```

## 9-1. 실행

```python
for number in generate_range(1, 5):
    print(number)
```

## 9-2. 출력 결과

```text
1
2
3
4
5
```

## 9-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `current` | 현재 반환할 값을 저장하기 위해 |
| `while` | 종료 조건까지 값을 계속 생성하기 위해 |
| `yield current` | 현재 값을 반환하고 실행을 멈추기 위해 |
| `current += 1` | 다음 실행에서 다음 값을 준비하기 위해 |

---

# 10. 사용자 정의 이터레이터와 제너레이터 비교

16번 문서에서 다음과 같은 이터레이터를 만들었다.

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration

        value = self.current
        self.current -= 1

        return value
```

같은 기능을 제너레이터로 작성하면 더 짧아진다.

```python
def countdown(start):
    while start >= 1:
        yield start
        start -= 1
```

## 10-1. 실행

```python
for number in countdown(3):
    print(number)
```

출력:

```text
3
2
1
```

## 10-2. 비교

| 구분 | 사용자 정의 이터레이터 | 제너레이터 |
| --- | --- | --- |
| 구현 요소 | 클래스, `__iter__()`, `__next__()` | 함수와 `yield` |
| 상태 관리 | 직접 속성으로 관리 | Python이 자동 관리 |
| 종료 처리 | 직접 `StopIteration` 발생 | 함수 종료 시 자동 발생 |
| 코드 길이 | 상대적으로 김 | 짧음 |
| 복잡한 객체 상태 | 유리할 수 있음 | 단순 순차 처리에 유리 |

> [!TIP]
> 단순히 값을 순서대로 생성하는 기능은 제너레이터가 더 간결한 경우가 많다.

---

# 11. 제너레이터 표현식

리스트 컴프리헨션과 비슷한 문법으로 제너레이터를 만들 수 있다.

## 11-1. 리스트 컴프리헨션

```python
numbers = [
    number * 2
    for number in range(1, 4)
]

print(numbers)
```

출력:

```text
[2, 4, 6]
```

## 11-2. 제너레이터 표현식

```python
numbers = (
    number * 2
    for number in range(1, 4)
)

print(numbers)
```

출력 형태:

```text
<generator object ...>
```

값 확인:

```python
print(next(numbers))
print(next(numbers))
print(next(numbers))
```

출력:

```text
2
4
6
```

## 11-3. 문법 차이

```text
리스트 컴프리헨션
[표현식 for 변수 in 반복가능객체]

제너레이터 표현식
(표현식 for 변수 in 반복가능객체)
```

---

# 12. 리스트 컴프리헨션과 제너레이터 표현식 비교

| 구분 | 리스트 컴프리헨션 | 제너레이터 표현식 |
| --- | --- | --- |
| 기호 | `[]` | `()` |
| 결과 | 리스트 | 제너레이터 |
| 값 생성 | 즉시 전체 생성 | 필요할 때 하나씩 |
| 인덱스 접근 | 가능 | 일반적으로 불가능 |
| 여러 번 순회 | 가능 | 한 번 소비되는 경우 많음 |
| 대용량 처리 | 메모리 부담 가능 | 지연 처리에 유리 |

## 12-1. 언제 리스트가 더 좋을까?

- 결과 전체가 바로 필요함
- 인덱스로 접근해야 함
- 여러 번 반복해야 함
- 데이터 크기가 작음

## 12-2. 언제 제너레이터가 더 좋을까?

- 값을 한 번만 순서대로 처리함
- 데이터가 매우 큼
- 파일이나 네트워크 데이터를 스트리밍함
- 모든 결과를 미리 만들 필요가 없음

> [!IMPORTANT]
> 제너레이터가 항상 더 좋은 것은 아니다.
>
> 전체 결과가 필요하거나 여러 번 접근해야 한다면 리스트가 더 단순하고 적합할 수 있다.

---

# 13. 제너레이터는 한 번 소비된다

```python
generator = (
    number
    for number in range(1, 4)
)

print(list(generator))
print(list(generator))
```

출력:

```text
[1, 2, 3]
[]
```

첫 번째 `list()`가 모든 값을 소비했다.

## 13-1. 다시 사용하려면

새 제너레이터를 만든다.

```python
generator = (
    number
    for number in range(1, 4)
)
```

> [!WARNING]
> 제너레이터는 자동으로 처음 위치로 돌아가지 않는다.

---

# 14. `yield from`

`yield from`은 다른 반복 가능한 객체의 값을 하나씩 대신 전달한다.

## 14-1. 일반 `yield`

```python
def generate_numbers():
    for number in [1, 2, 3]:
        yield number
```

## 14-2. `yield from`

```python
def generate_numbers():
    yield from [1, 2, 3]
```

두 코드는 같은 값을 반환한다.

## 14-3. 실행

```python
for number in generate_numbers():
    print(number)
```

출력:

```text
1
2
3
```

## 14-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `yield from` | 다른 반복 가능한 객체의 값을 순서대로 전달하기 위해 |
| `[1, 2, 3]` | 전달할 원본 데이터 |

> [!TIP]
> 반복 가능한 객체의 값을 그대로 전달할 때 `for`와 `yield`를 반복 작성하지 않아도 된다.

---

# 15. 여러 제너레이터 연결

```python
def first_numbers():
    yield 1
    yield 2


def second_numbers():
    yield 3
    yield 4


def all_numbers():
    yield from first_numbers()
    yield from second_numbers()
```

## 15-1. 실행

```python
for number in all_numbers():
    print(number)
```

## 15-2. 출력 결과

```text
1
2
3
4
```

## 15-3. 구조

```text
all_numbers()
├─ first_numbers() 값 전달
│  ├─ 1
│  └─ 2
│
└─ second_numbers() 값 전달
   ├─ 3
   └─ 4
```

---

# 16. 무한 제너레이터

종료 조건 없이 값을 계속 생성할 수 있다.

```python
def infinite_counter():
    number = 1

    while True:
        yield number
        number += 1
```

## 16-1. 안전하게 사용

```python
for number in infinite_counter():
    print(number)

    if number == 5:
        break
```

출력:

```text
1
2
3
4
5
```

> [!WARNING]
> 무한 제너레이터는 외부에 반드시 종료 조건이 있어야 한다.

---

# 17. 제너레이터로 파일 한 줄씩 처리

```python
def read_lines(file_path):
    with open(
        file_path,
        "r",
        encoding="utf-8",
    ) as file:
        for line in file:
            yield line.strip()
```

## 17-1. 실행

```python
for line in read_lines("data.txt"):
    print(line)
```

## 17-2. 동작 과정

```text
파일 열기
    ↓
한 줄 읽기
    ↓
yield
    ↓
호출한 쪽에서 처리
    ↓
다음 요청 시 다음 줄 읽기
```

파일 전체를 리스트로 만들지 않고 한 줄씩 처리할 수 있다.

> [!TIP]
> 대용량 파일은 `read()`로 전체를 한 번에 읽기보다 줄 단위 제너레이터로 처리하면 메모리 부담을 줄일 수 있다.

---

# 18. 데이터 필터링 제너레이터

```python
def get_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number
```

## 18-1. 실행

```python
numbers = range(1, 11)

for number in get_even_numbers(numbers):
    print(number)
```

## 18-2. 출력 결과

```text
2
4
6
8
10
```

## 18-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `for number in numbers` | 입력 데이터를 하나씩 확인하기 위해 |
| `number % 2 == 0` | 짝수인지 검사하기 위해 |
| `yield number` | 조건을 만족한 값만 반환하기 위해 |

---

# 19. 데이터 변환 제너레이터

```python
def square_numbers(numbers):
    for number in numbers:
        yield number ** 2
```

실행:

```python
for number in square_numbers([1, 2, 3]):
    print(number)
```

출력:

```text
1
4
9
```

제너레이터는 값을 필터링하거나 변환하는 단계에 적합하다.

---

# 20. 제너레이터 파이프라인

여러 제너레이터를 연결해 데이터를 단계별로 처리할 수 있다.

```python
def get_numbers():
    for number in range(1, 11):
        yield number


def filter_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def square(numbers):
    for number in numbers:
        yield number ** 2
```

## 20-1. 실행

```python
numbers = get_numbers()
even_numbers = filter_even(numbers)
squared_numbers = square(even_numbers)

for number in squared_numbers:
    print(number)
```

## 20-2. 출력 결과

```text
4
16
36
64
100
```

## 20-3. 처리 흐름

```text
1~10 생성
    ↓
짝수만 통과
    ↓
제곱
    ↓
최종 값 하나씩 출력
```

각 단계는 전체 결과를 미리 만들지 않고 값 하나씩 전달한다.

---

# 21. `send()`

`send()`는 제너레이터 실행을 재개하면서 값을 전달할 수 있다.

```python
def receiver():
    value = yield "준비 완료"

    print("전달받은 값:", value)
```

## 21-1. 실행

```python
generator = receiver()

print(next(generator))
generator.send("Python")
```

출력:

```text
준비 완료
전달받은 값: Python
```

## 21-2. 동작 과정

```text
next(generator)
    ↓
yield "준비 완료"
    ↓
문자열 반환 + 중단

generator.send("Python")
    ↓
yield 표현식의 결과로 "Python" 전달
    ↓
value = "Python"
    ↓
출력
```

## 21-3. 첫 실행 주의

아직 시작하지 않은 제너레이터에는 일반 값을 바로 보낼 수 없다.

잘못된 코드:

```python
generator = receiver()
generator.send("Python")
```

발생 결과:

```text
TypeError
```

먼저 시작해야 한다.

```python
next(generator)
```

또는:

```python
generator.send(None)
```

> [!IMPORTANT]
> `send()`는 제너레이터와 양방향으로 값을 주고받는 기능이지만, 일반적인 데이터 생성에는 자주 필요하지 않다.
>
> 기본적인 제너레이터 사용에서는 `yield`, `for`, `next()`를 우선 이해하면 충분하다.

---

# 22. `close()`

`close()`는 제너레이터를 종료한다.

```python
def generate_numbers():
    yield 1
    yield 2
    yield 3
```

```python
generator = generate_numbers()

print(next(generator))

generator.close()

print(next(generator))
```

첫 번째 출력:

```text
1
```

`close()` 이후 `next()`를 호출하면 `StopIteration`이 발생한다.

## 22-1. 언제 사용할까?

- 더 이상 값을 받을 필요가 없을 때
- 제너레이터 내부 정리 작업을 실행해야 할 때
- 외부에서 반복을 명시적으로 중단할 때

---

# 23. `GeneratorExit`

`close()`가 호출되면 제너레이터 내부에는 `GeneratorExit`이 전달된다.

```python
def generate_numbers():
    try:
        yield 1
        yield 2
    finally:
        print("제너레이터 정리")
```

```python
generator = generate_numbers()

print(next(generator))
generator.close()
```

출력:

```text
1
제너레이터 정리
```

> [!TIP]
> 제너레이터 내부의 `finally`를 이용해 자원 정리 코드를 작성할 수 있다.

---

# 24. `throw()`

`throw()`는 제너레이터가 중단된 위치에 예외를 전달한다.

```python
def generate_numbers():
    try:
        yield 1
        yield 2
    except ValueError as error:
        print("예외 처리:", error)
```

## 24-1. 실행

```python
generator = generate_numbers()

print(next(generator))
generator.throw(ValueError("잘못된 값"))
```

출력:

```text
1
예외 처리: 잘못된 값
```

> [!WARNING]
> `throw()`는 고급 제어 기능이다.
>
> 일반적인 순차 데이터 처리에서는 거의 필요하지 않으며, 남용하면 코드 흐름을 이해하기 어려워질 수 있다.

---

# 25. 전통적인 코루틴과 `send()`

제너레이터의 `send()`를 활용한 패턴을 전통적인 코루틴이라고 부르기도 한다.

```python
def accumulator():
    total = 0

    while True:
        value = yield total
        total += value
```

하지만 현대 Python의 비동기 작업에서는 일반적으로 다음 문법을 사용한다.

```python
async def fetch_data():
    ...
```

```python
await fetch_data()
```

> [!TIP]
> 전통적인 제너레이터 기반 코루틴은 개념만 간단히 알아두면 충분하다.
>
> 현재 실무의 비동기 프로그래밍은 주로 `async`와 `await`를 사용한다.

---

# 26. 제너레이터와 메모리

리스트는 전체 결과를 미리 저장한다.

```python
numbers = [
    number * 2
    for number in range(1_000_000)
]
```

제너레이터는 필요한 시점에 하나씩 계산한다.

```python
numbers = (
    number * 2
    for number in range(1_000_000)
)
```

## 26-1. 차이

```text
리스트
→ 전체 값 생성
→ 전체 값 저장

제너레이터
→ 다음 값 요청
→ 그때 계산
→ 하나씩 전달
```

## 26-2. 주의점

제너레이터 자체가 무조건 모든 메모리 문제를 해결하는 것은 아니다.

다음과 같이 원본이 이미 큰 리스트라면 그 리스트는 메모리에 존재한다.

```python
source = list(range(1_000_000))

generator = (
    number * 2
    for number in source
)
```

> [!IMPORTANT]
> 제너레이터의 메모리 장점은 원본 데이터도 스트리밍되거나 지연 생성될 때 가장 크다.

---

# 27. 제너레이터의 장점

- 값을 필요한 시점에 생성할 수 있다.
- 대용량 데이터를 순차 처리하기 좋다.
- 사용자 정의 이터레이터보다 코드가 짧다.
- 파일·네트워크·데이터베이스 결과를 스트리밍하기 좋다.
- 처리 단계를 파이프라인으로 연결할 수 있다.
- 상태를 자동으로 유지한다.

---

# 28. 제너레이터의 단점

- 한 번 소비하면 다시 사용할 수 없는 경우가 많다.
- 인덱스로 바로 접근할 수 없다.
- 전체 길이를 바로 알기 어렵다.
- 중간 상태를 추적하기 어려울 수 있다.
- 작은 데이터에서는 리스트보다 오히려 복잡할 수 있다.
- `send()`, `throw()` 등을 과도하게 사용하면 흐름이 어려워진다.

---

# 29. 제너레이터가 적합한 상황

- 대용량 파일 한 줄씩 처리
- 로그 데이터 순차 처리
- 네트워크 응답 스트리밍
- 데이터베이스 결과 순회
- 무한 수열
- 필터링·변환 파이프라인
- 전체 결과가 필요하지 않은 계산
- 한 번만 순회할 데이터

---

# 30. 제너레이터가 적합하지 않은 상황

- 결과 전체를 여러 번 사용해야 함
- 인덱스 접근이 필요함
- 데이터 크기가 매우 작음
- 전체 길이를 자주 확인해야 함
- 정렬·역순·수정이 자주 필요함
- 단순 리스트가 더 읽기 쉬움

> [!TIP]
> 성능을 이유로 무조건 제너레이터를 사용하기보다, 데이터 흐름과 사용 방식을 먼저 판단한다.

---

# 31. 대표 오류로 이해하기

## 31-1. 함수 호출 결과를 값으로 착각

```python
def generate_numbers():
    yield 1
    yield 2


result = generate_numbers()

print(result)
```

출력은 숫자 목록이 아니라 제너레이터 객체다.

값을 확인하려면:

```python
print(list(result))
```

---

## 31-2. 제너레이터 재사용

```python
generator = generate_numbers()

print(list(generator))
print(list(generator))
```

출력:

```text
[1, 2]
[]
```

첫 번째 변환에서 모두 소비되었다.

---

## 31-3. 시작 전 `send()` 호출

```python
generator = receiver()
generator.send("Python")
```

발생 결과:

```text
TypeError
```

먼저 `next(generator)` 또는 `generator.send(None)`이 필요하다.

---

## 31-4. 종료 조건 없는 무한 제너레이터

```python
def numbers():
    number = 1

    while True:
        yield number
        number += 1
```

외부에서 종료하지 않으면 반복이 끝나지 않는다.

---

## 31-5. `yield`와 `return` 혼동

```python
def generate_numbers():
    yield 1
    return
    yield 2
```

`return` 이후 값은 생성되지 않는다.

---

## 31-6. 전체 결과가 필요한데 제너레이터만 유지

```python
generator = (
    number * 2
    for number in range(3)
)
```

여러 번 사용해야 한다면 리스트로 변환하거나 처음부터 리스트 컴프리헨션을 고려한다.

---

# 32. 제너레이터 구조

```text
제너레이터 함수 호출
    ↓
제너레이터 객체 생성
    ↓
next() / for
    ↓
yield까지 실행
    ↓
값 반환
    ↓
실행 위치·지역 변수 저장
    ↓
다음 요청에서 이어서 실행
```

```text
함수 종료
    ↓
StopIteration
    ↓
반복 종료
```

---

# 33. 기존 방식에서 개선된 이해

## 33-1. `yield`를 여러 번 값을 반환하는 `return`으로 이해

기존 이해:

```text
yield
→ 값을 여러 번 반환
```

개선된 이해:

```text
yield
→ 값 반환
→ 현재 실행 상태 저장
→ 함수 일시 중단
→ 다음 호출에서 재개
```

## 33-2. 제너레이터를 메모리 절약 기능으로만 이해

개선된 이해:

```text
제너레이터
→ 지연 실행
→ 순차 처리
→ 상태 유지
→ 스트리밍 처리
```

메모리 절약은 그 결과 중 하나다.

## 33-3. 리스트보다 항상 좋다고 이해

제너레이터는 한 번 순회하는 대용량 처리에 강하지만, 전체 결과 접근과 반복 사용에는 리스트가 더 적합할 수 있다.

---

# 34. 자주 하는 실수

## 34-1. 제너레이터 함수를 호출하면 즉시 실행된다고 생각

첫 `next()` 또는 반복 시 실행된다.

## 34-2. `yield`가 함수 종료라고 생각

실행 위치와 지역 변수를 유지한 채 일시 중단된다.

## 34-3. 소비한 제너레이터를 다시 사용

두 번째 순회에서는 값이 없을 수 있다.

## 34-4. 제너레이터에 인덱스 접근

일반적으로 `generator[0]`처럼 사용할 수 없다.

## 34-5. 무한 제너레이터에 종료 조건 없음

프로그램이 끝나지 않을 수 있다.

## 34-6. `send()`를 시작 전에 호출

일반 값을 보내기 전에 제너레이터를 먼저 시작해야 한다.

## 34-7. `return` 이후에도 `yield`가 실행된다고 생각

`return`은 제너레이터를 종료한다.

## 34-8. 제너레이터면 무조건 메모리가 적게 든다고 생각

원본 데이터가 이미 전체 리스트라면 원본 메모리는 그대로 사용된다.

## 34-9. 작은 데이터에도 복잡한 제너레이터 파이프라인 사용

단순 리스트가 더 읽기 쉬울 수 있다.

## 34-10. `send()`, `throw()`, `close()`를 과도하게 사용

코드 흐름이 복잡해질 수 있다.

---

# 35. 면접·복습 포인트

## Q1. 제너레이터란 무엇인가요?

값을 한 번에 모두 만들지 않고 요청할 때마다 하나씩 생성하는 이터레이터다.

## Q2. 제너레이터 함수는 어떻게 구분하나요?

함수 내부에 `yield`가 있으면 제너레이터 함수가 된다.

## Q3. 제너레이터 함수를 호출하면 바로 실행되나요?

아니다. 제너레이터 객체가 생성되고 첫 `next()` 또는 반복 시 실행된다.

## Q4. `yield`와 `return`의 차이는 무엇인가요?

`return`은 값을 반환하고 함수를 종료하지만, `yield`는 값을 반환하고 실행 상태를 유지한 채 중단한다.

## Q5. 제너레이터는 어떤 상태를 유지하나요?

현재 실행 위치와 지역 변수 값을 유지한다.

## Q6. 제너레이터가 끝나면 어떤 예외가 발생하나요?

`StopIteration`이 발생한다.

## Q7. 제너레이터 표현식과 리스트 컴프리헨션의 차이는 무엇인가요?

제너레이터 표현식은 값을 지연 생성하고, 리스트 컴프리헨션은 전체 리스트를 즉시 생성한다.

## Q8. `yield from`은 왜 사용하나요?

다른 반복 가능한 객체나 제너레이터의 값을 순서대로 전달하기 위해 사용한다.

## Q9. 제너레이터가 메모리에 유리한 이유는 무엇인가요?

전체 결과를 한 번에 저장하지 않고 필요한 값을 하나씩 생성할 수 있기 때문이다.

## Q10. 제너레이터는 여러 번 순회할 수 있나요?

일반적으로 한 번 소비되며, 다시 사용하려면 새 제너레이터를 만들어야 한다.

## Q11. `send()`는 무엇을 하나요?

제너레이터 실행을 재개하면서 중단된 `yield` 표현식에 값을 전달한다.

## Q12. 전통적인 코루틴은 실무에서 많이 사용하나요?

현재는 제너레이터 기반 코루틴보다 `async`와 `await`를 사용하는 비동기 방식이 더 일반적이다.

---

# 36. 핵심 요약

```text
제너레이터 함수
→ yield 포함

함수 호출
→ 제너레이터 객체 생성

next()
→ 실행 시작 또는 재개

yield
→ 값 반환
→ 상태 저장
→ 실행 중단

함수 종료
→ StopIteration
```

```text
리스트
→ 전체 결과 즉시 생성

제너레이터
→ 필요한 값 하나씩 생성
```

```text
yield from
→ 다른 반복 가능한 객체의 값 전달

send()
→ 제너레이터에 값 전달

close()
→ 제너레이터 종료

throw()
→ 제너레이터 내부에 예외 전달
```

---

# 37. 최종 체크리스트

- [ ] 일반 함수와 제너레이터 함수의 차이를 설명할 수 있는가?
- [ ] 제너레이터 함수 호출 시 즉시 실행되지 않는다는 점을 이해했는가?
- [ ] `yield`가 실행 중단이라는 점을 이해했는가?
- [ ] `next()`가 중단 위치부터 실행을 재개한다는 점을 아는가?
- [ ] 지역 변수와 실행 위치가 유지된다는 점을 이해했는가?
- [ ] 제너레이터 종료 시 `StopIteration`이 발생함을 아는가?
- [ ] 제너레이터 표현식을 작성할 수 있는가?
- [ ] 리스트 컴프리헨션과 선택 기준을 구분할 수 있는가?
- [ ] 소비한 제너레이터는 다시 사용할 수 없음을 아는가?
- [ ] `yield from`을 사용할 수 있는가?
- [ ] 무한 제너레이터에 종료 조건이 있는가?
- [ ] `send()` 사용 전 제너레이터를 시작했는가?
- [ ] 제너레이터가 항상 최선은 아니라는 점을 이해했는가?
- [ ] 원본 데이터까지 지연 생성되는지 확인했는가?

---

# 마무리

제너레이터의 핵심은 단순히 메모리를 절약하는 것이 아니다.

```text
값을 필요한 시점에 생성하고
    ↓
현재 실행 상태를 유지하며
    ↓
다음 요청에서 이어서 실행하고
    ↓
대용량 데이터와 스트리밍 흐름을 순차 처리하는 것
```

이 원리를 이해하면 파일 처리, 데이터 파이프라인, 네트워크 응답, 데이터베이스 결과 처리에서 왜 제너레이터가 사용되는지 자연스럽게 이해할 수 있다.

# V3 동작 백과 보강 — 호출과 실행이 분리되는 함수

`yield`가 있는 함수를 호출하면 본문을 바로 실행하지 않고 제너레이터 객체를 반환한다. `next()` 요청 때 `yield`까지 실행하고 상태를 보관하며, 다음 요청은 멈춘 다음 줄부터 재개한다.

```python
def numbers():
    print("시작")
    yield 1
    print("재개")
    yield 2
gen = numbers()
print("생성 완료")
print(next(gen)); print(next(gen))
```

출력 순서는 `생성 완료`, `시작`, `1`, `재개`, `2`다. 호출 순간 `시작`이 출력되지 않는 점이 핵심이다. 모든 값을 미리 만들지 않아 대용량 처리에 유리하다.

**원본 연결:** 반복문과 파일 처리의 지연·순차 처리 원리를 확장한 **Wiki 확장 학습**이다.
