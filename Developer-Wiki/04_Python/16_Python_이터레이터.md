---
title: Python 이터레이터
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 이터레이터

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `16_Python_이터레이터.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `06_Python_리스트와_튜플.md`, `09_Python_반복문.md`, `11_Python_함수.md`, `12_Python_클래스.md` |
| 다음 학습 | `17_Python_제너레이터.md` |
| 문서 성격 | Python 확장 학습 문서 |
| 핵심 범위 | 반복 가능한 객체, 이터레이터, `iter()`, `next()`, `StopIteration`, 이터레이션 프로토콜, 사용자 정의 이터레이터 |
| 실습 범위 | 리스트 순회 원리, 직접 `next()` 호출, 숫자 범위 이터레이터, 역순 이터레이터 |
| 종합 실습 | 별도 문서 `20_Python_종합실습.md`에서 관리 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 Python의 `for`문이 내부적으로 어떻게 반복을 수행하는지 이해하기 위한 확장 문서다.  
> 단순 문법 암기보다 `iter()`와 `next()`가 어떻게 연결되는지, 반복이 끝났을 때 왜 `StopIteration`이 발생하는지에 집중한다.

---

# 개요

Python에서 다음 코드는 매우 익숙하다.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

출력 결과:

```text
10
20
30
```

겉으로는 `for`문이 리스트의 값을 하나씩 꺼내는 것처럼 보인다.

하지만 내부에서는 다음 흐름이 사용된다.

```text
반복 가능한 객체 준비
    ↓
iter()로 이터레이터 생성
    ↓
next()로 값 하나씩 요청
    ↓
더 이상 값이 없으면 StopIteration
    ↓
for문 종료
```

즉, `for`문은 이터레이터를 자동으로 사용한다.

> [!IMPORTANT]
> 이터레이터를 이해하면 `for`문, 제너레이터, 파일 순회, 대용량 데이터 처리의 기본 원리를 이해할 수 있다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 반복 가능한 객체(Iterable) | `iter()`로 이터레이터를 만들 수 있는 객체 |
| 이터레이터(Iterator) | `next()`로 값을 하나씩 꺼낼 수 있는 객체 |
| `iter()` | 반복 가능한 객체에서 이터레이터를 얻음 |
| `next()` | 이터레이터에서 다음 값을 하나 꺼냄 |
| `StopIteration` | 더 이상 꺼낼 값이 없음을 알리는 예외 |
| 이터레이션(Iteration) | 값을 하나씩 순서대로 처리하는 과정 |
| 이터레이션 프로토콜 | `__iter__()`와 `__next__()`로 이루어진 반복 규칙 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 반복 가능한 객체와 이터레이터의 차이를 설명할 수 있다.
- 리스트에서 `iter()`로 이터레이터를 만들 수 있다.
- `next()`로 값을 하나씩 꺼낼 수 있다.
- 반복이 끝나면 `StopIteration`이 발생하는 이유를 이해한다.
- `for`문이 내부적으로 `iter()`와 `next()`를 사용한다는 점을 설명할 수 있다.
- 이터레이터는 현재 위치를 기억한다는 점을 이해한다.
- 이터레이터는 한 번 소비하면 이전 위치로 자동 복구되지 않는다는 점을 안다.
- `__iter__()`와 `__next__()`를 구현해 사용자 정의 이터레이터를 만들 수 있다.
- 무한 이터레이터의 위험성을 이해한다.
- 이터레이터와 제너레이터의 관계를 설명할 수 있다.

---

# 1. 반복 가능한 객체란?

반복 가능한 객체는 `for`문으로 순회할 수 있고, `iter()`를 적용할 수 있는 객체다.

대표적인 반복 가능한 객체:

- 리스트
- 튜플
- 문자열
- 딕셔너리
- 집합
- `range`
- 파일 객체

```python
values = [1, 2, 3]

for value in values:
    print(value)
```

## 1-1. 반복 가능한지 확인

```python
values = [1, 2, 3]

iterator = iter(values)

print(iterator)
```

출력 형태:

```text
<list_iterator object at ...>
```

리스트 자체가 바로 값을 꺼내는 이터레이터는 아니지만, `iter()`를 사용하면 리스트 이터레이터를 만들 수 있다.

---

# 2. 이터레이터란?

이터레이터는 `next()`를 호출할 때마다 다음 값을 하나씩 반환하는 객체다.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

출력 결과:

```text
10
20
30
```

## 2-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `numbers` | 반복할 원본 데이터를 저장하기 위해 |
| `iter(numbers)` | 리스트에서 이터레이터를 만들기 위해 |
| `iterator` | 현재 반복 위치를 가진 객체를 저장하기 위해 |
| `next(iterator)` | 다음 값을 하나씩 꺼내기 위해 |

## 2-2. 동작 과정

```text
iterator 생성
현재 위치: 첫 번째 값 이전

next()
    ↓
10 반환
현재 위치: 10 다음

next()
    ↓
20 반환
현재 위치: 20 다음

next()
    ↓
30 반환
현재 위치: 마지막 다음
```

> [!TIP]
> 이터레이터는 원본 데이터 전체를 한꺼번에 반환하지 않고, 요청할 때마다 값 하나를 반환한다.

---

# 3. `StopIteration`

이터레이터에서 모든 값을 꺼낸 뒤 다시 `next()`를 호출하면 `StopIteration`이 발생한다.

```python
numbers = [10, 20]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

출력:

```text
10
20
StopIteration
```

## 3-1. 왜 오류처럼 보일까?

`StopIteration`은 단순한 실패가 아니라 **반복이 끝났다는 신호**다.

```text
값 있음
→ next()가 값 반환

값 없음
→ StopIteration 발생
```

`for`문은 이 예외를 내부에서 자동으로 처리하고 반복을 종료한다.

> [!IMPORTANT]
> 직접 `next()`를 호출하면 `StopIteration`을 직접 볼 수 있지만, `for`문에서는 자동 처리되므로 보통 화면에 나타나지 않는다.

---

# 4. `for`문의 내부 동작

다음 코드:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

개념적으로 다음과 비슷하게 동작한다.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
    except StopIteration:
        break

    print(number)
```

## 4-1. 출력 결과

```text
10
20
30
```

## 4-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `iter(numbers)` | 반복에 사용할 이터레이터를 만들기 위해 |
| `while True` | 값이 끝날 때까지 계속 요청하기 위해 |
| `next(iterator)` | 다음 값을 얻기 위해 |
| `except StopIteration` | 더 이상 값이 없을 때 반복을 끝내기 위해 |
| `break` | 반복문을 종료하기 위해 |

> [!TIP]
> `for`문은 `StopIteration`을 직접 작성하지 않아도 안전하게 반복을 종료해 준다.

---

# 5. 반복 가능한 객체와 이터레이터 비교

| 구분 | 반복 가능한 객체 | 이터레이터 |
| --- | --- | --- |
| 역할 | 반복할 데이터를 제공 | 값을 하나씩 반환 |
| `iter()` 사용 | 가능 | 일반적으로 자기 자신 반환 |
| `next()` 사용 | 직접 불가능한 경우 많음 | 가능 |
| 현재 위치 저장 | 보통 하지 않음 | 저장함 |
| 예시 | 리스트, 문자열, 튜플 | `list_iterator`, `str_iterator` |

## 5-1. 리스트에 바로 `next()` 사용

```python
numbers = [1, 2, 3]

print(next(numbers))
```

발생 결과:

```text
TypeError
```

리스트는 반복 가능한 객체지만, 그 자체가 이터레이터는 아니다.

올바른 코드:

```python
iterator = iter(numbers)

print(next(iterator))
```

---

# 6. 이터레이터는 현재 위치를 기억한다

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

출력:

```text
10
20
```

다음 `next()`는 처음부터 시작하지 않는다.

```python
print(next(iterator))
```

출력:

```text
30
```

```text
이터레이터 내부 상태
→ 마지막으로 반환한 위치를 기억
→ 다음 호출에서 이어서 진행
```

---

# 7. 이터레이터는 한 번 소비된다

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

for number in iterator:
    print(number)

for number in iterator:
    print(number)
```

첫 번째 반복 출력:

```text
1
2
3
```

두 번째 반복에서는 아무것도 출력되지 않는다.

이미 이터레이터가 끝까지 소비되었기 때문이다.

## 7-1. 다시 반복하려면

원본 반복 가능한 객체에서 새 이터레이터를 만든다.

```python
iterator = iter(numbers)

for number in iterator:
    print(number)
```

> [!WARNING]
> 이터레이터는 자동으로 처음 위치로 돌아가지 않는다.
>
> 같은 데이터를 다시 순회하려면 새 이터레이터를 만들거나 원본 반복 가능한 객체를 다시 사용한다.

---

# 8. 리스트는 여러 번 반복할 수 있는 이유

리스트는 반복 가능한 객체이므로 `for`문을 실행할 때마다 새 이터레이터가 만들어진다.

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)

for number in numbers:
    print(number)
```

두 번 모두 정상 출력된다.

```text
첫 번째 for
→ iter(numbers)로 새 이터레이터 생성

두 번째 for
→ iter(numbers)로 또 다른 새 이터레이터 생성
```

리스트 자체가 소비되는 것이 아니라, 매번 생성된 이터레이터가 소비된다.

---

# 9. 문자열 이터레이터

문자열도 반복 가능한 객체다.

```python
text = "ABC"

iterator = iter(text)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

출력:

```text
A
B
C
```

다음 호출:

```python
print(next(iterator))
```

결과:

```text
StopIteration
```

---

# 10. 딕셔너리 이터레이터

딕셔너리를 기본 순회하면 키가 나온다.

```python
user = {
    "name": "홍길동",
    "age": 20,
}

iterator = iter(user)

print(next(iterator))
print(next(iterator))
```

출력:

```text
name
age
```

값이나 키·값 쌍을 반복하려면 다음 메서드를 사용한다.

```python
iter(user.values())
iter(user.items())
```

## 10-1. 실행 예시

```python
iterator = iter(user.items())

print(next(iterator))
print(next(iterator))
```

출력:

```text
('name', '홍길동')
('age', 20)
```

---

# 11. `range`와 이터레이터

`range`도 반복 가능한 객체다.

```python
numbers = range(1, 4)

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

출력:

```text
1
2
3
```

`range`는 전체 숫자 리스트를 미리 만들지 않고 범위 정보를 바탕으로 값을 제공한다.

```text
range(1, 1000000)
→ 백만 개 숫자를 리스트로 미리 저장하지 않음
→ 필요한 순서대로 값을 제공
```

> [!TIP]
> 이터레이터 구조는 데이터를 한 번에 모두 메모리에 올리지 않고 순차적으로 처리할 수 있게 해 준다.

---

# 12. `iter()`에 종료값 전달

`iter()`는 함수와 종료값을 함께 전달하는 형태도 지원한다.

```python
iterator = iter(호출할_함수, 종료값)
```

함수를 반복 호출하고 반환값이 종료값과 같아지면 반복을 끝낸다.

## 12-1. 예시

```python
values = iter(
    lambda: input("값 입력: "),
    "종료",
)

for value in values:
    print("입력값:", value)
```

입력 예:

```text
값 입력: 안녕
입력값: 안녕
값 입력: Python
입력값: Python
값 입력: 종료
```

`"종료"`는 반복 결과에 포함되지 않고 종료 조건으로 사용된다.

> [!TIP]
> 이 형태는 특정 함수의 반환값이 종료 신호가 될 때 사용할 수 있다.

---

# 13. 이터레이션 프로토콜

Python에서 이터레이터로 동작하려면 다음 메서드가 필요하다.

```python
__iter__()
__next__()
```

## 13-1. `__iter__()`

이터레이터 객체를 반환한다.

```python
def __iter__(self):
    return self
```

## 13-2. `__next__()`

다음 값을 반환한다.

값이 끝나면 `StopIteration`을 발생시킨다.

```python
def __next__(self):
    if 더_이상_값이_없음:
        raise StopIteration

    return 다음_값
```

---

# 14. 사용자 정의 이터레이터

1부터 지정한 숫자까지 반환하는 이터레이터를 만들 수 있다.

```python
class NumberIterator:
    def __init__(self, stop):
        self.current = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration

        value = self.current
        self.current += 1

        return value
```

## 14-1. 실행

```python
numbers = NumberIterator(3)

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

## 14-2. 출력 결과

```text
1
2
3
```

## 14-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `self.current` | 현재 반환할 숫자를 저장하기 위해 |
| `self.stop` | 반복 종료 기준을 저장하기 위해 |
| `__iter__()` | 객체를 이터레이터로 사용할 수 있게 하기 위해 |
| `return self` | 현재 객체 자체가 이터레이터이기 때문에 |
| `__next__()` | 다음 값을 하나씩 반환하기 위해 |
| `raise StopIteration` | 반복 종료를 알리기 위해 |
| `self.current += 1` | 다음 호출에서 다음 숫자를 반환하기 위해 |

---

# 15. 사용자 정의 이터레이터의 동작 과정

```text
NumberIterator(3)
    ↓
current = 1
stop = 3

next()
→ 1 반환
→ current = 2

next()
→ 2 반환
→ current = 3

next()
→ 3 반환
→ current = 4

next()
→ current > stop
→ StopIteration
```

---

# 16. 사용자 정의 이터레이터를 `for`문에서 사용

```python
numbers = NumberIterator(3)

for number in numbers:
    print(number)
```

출력 결과:

```text
1
2
3
```

`for`문은 자동으로 다음 메서드를 사용한다.

```text
iter(numbers)
→ numbers.__iter__()

next(numbers)
→ numbers.__next__()
```

---

# 17. 반복 가능한 객체와 이터레이터를 분리하기

앞의 `NumberIterator`는 객체 자체가 이터레이터이므로 한 번 소비하면 다시 사용할 수 없다.

반복 가능한 객체와 이터레이터를 분리하면 매번 새 이터레이터를 만들 수 있다.

```python
class NumberRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return NumberIterator(self.stop)
```

## 17-1. 실행

```python
numbers = NumberRange(3)

for number in numbers:
    print(number)

for number in numbers:
    print(number)
```

출력:

```text
1
2
3
1
2
3
```

## 17-2. 구조

```text
NumberRange
→ 반복 가능한 객체
→ iter() 호출 시 새 NumberIterator 생성

NumberIterator
→ 현재 위치를 기억
→ next()로 값 반환
```

> [!IMPORTANT]
> 여러 번 반복해야 하는 객체는 `__iter__()`에서 새로운 이터레이터를 반환하도록 설계할 수 있다.

---

# 18. 역순 이터레이터 예제

지정한 숫자부터 1까지 역순으로 반환하는 이터레이터다.

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

## 18-1. 실행

```python
countdown = Countdown(3)

for number in countdown:
    print(number)
```

## 18-2. 출력 결과

```text
3
2
1
```

## 18-3. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `start` | 시작 숫자를 전달받기 위해 |
| `self.current -= 1` | 호출할 때마다 숫자를 감소시키기 위해 |
| `self.current < 1` | 종료 조건을 확인하기 위해 |
| `StopIteration` | 반복이 끝났음을 알리기 위해 |

---

# 19. 무한 이터레이터

종료 조건 없이 계속 값을 반환하는 이터레이터를 만들 수도 있다.

```python
class InfiniteCounter:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current
```

## 19-1. 주의할 실행

```python
counter = InfiniteCounter()

for number in counter:
    print(number)
```

반복이 끝나지 않는다.

## 19-2. 안전하게 사용

```python
counter = InfiniteCounter()

for number in counter:
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
> 무한 이터레이터는 반드시 외부 종료 조건과 함께 사용해야 한다.

---

# 20. `next()`의 기본값

`next()`는 두 번째 인자로 기본값을 받을 수 있다.

```python
next(iterator, 기본값)
```

이터레이터가 끝나면 `StopIteration` 대신 기본값을 반환한다.

## 20-1. 실행

```python
numbers = iter([10, 20])

print(next(numbers, None))
print(next(numbers, None))
print(next(numbers, None))
```

출력:

```text
10
20
None
```

> [!TIP]
> 반복 종료를 예외로 처리하지 않고 특정 기본값으로 확인하고 싶을 때 사용할 수 있다.

---

# 21. 파일 객체도 이터레이터다

파일 객체는 줄 단위로 순회할 수 있다.

```python
with open(
    "data.txt",
    "r",
    encoding="utf-8",
) as file:
    print(next(file))
```

또는:

```python
with open(
    "data.txt",
    "r",
    encoding="utf-8",
) as file:
    for line in file:
        print(line.strip())
```

파일 전체를 한 번에 읽지 않고 한 줄씩 처리할 수 있다.

```text
대용량 파일
→ 한 줄씩 읽기
→ 메모리 사용량 감소
```

---

# 22. 이터레이터를 사용하는 대표 기능

Python의 많은 기능이 이터레이터를 기반으로 동작한다.

- `for`
- `enumerate`
- `zip`
- `map`
- `filter`
- `reversed`
- 파일 객체
- 제너레이터
- 일부 데이터베이스 결과 객체

예:

```python
numbers = [10, 20, 30]

iterator = enumerate(numbers)

print(next(iterator))
print(next(iterator))
```

출력:

```text
(0, 10)
(1, 20)
```

---

# 23. `map()`도 이터레이터를 반환한다

Python 3의 `map()`은 이터레이터를 반환한다.

```python
numbers = [1, 2, 3]

mapped = map(
    lambda number: number * 2,
    numbers,
)

print(next(mapped))
print(next(mapped))
print(next(mapped))
```

출력:

```text
2
4
6
```

리스트가 필요하면 변환한다.

```python
mapped = map(
    lambda number: number * 2,
    numbers,
)

result = list(mapped)

print(result)
```

출력:

```text
[2, 4, 6]
```

> [!IMPORTANT]
> `list(mapped)`로 모두 소비한 뒤에는 같은 `mapped` 이터레이터에서 다시 값을 꺼낼 수 없다.

---

# 24. 이터레이터와 메모리

이터레이터는 값을 요청할 때 하나씩 제공할 수 있어 대용량 데이터 처리에 유리하다.

리스트:

```python
numbers = list(range(1_000_000))
```

많은 값을 메모리에 저장한다.

이터레이터 기반 처리:

```python
numbers = iter(range(1_000_000))
```

필요한 순서대로 값을 꺼낸다.

다만 모든 이터레이터가 항상 메모리를 적게 사용하는 것은 아니다.

원본 객체가 이미 큰 리스트라면 그 리스트는 메모리에 존재한다.

```text
큰 리스트
→ 이미 메모리에 전체 데이터 존재
→ 이터레이터를 만들어도 원본 리스트는 그대로 존재
```

> [!IMPORTANT]
> 이터레이터 자체가 항상 메모리를 절약하는 것이 아니라, **데이터를 처음부터 지연 생성하거나 스트리밍 방식으로 제공할 때** 효과가 크다.

---

# 25. 이터레이터와 리스트 비교

| 구분 | 리스트 | 이터레이터 |
| --- | --- | --- |
| 값 저장 | 전체 값을 저장 | 다음 값 생성 또는 참조 |
| 인덱스 접근 | 가능 | 일반적으로 불가능 |
| 여러 번 순회 | 가능 | 한 번 소비되는 경우 많음 |
| 현재 위치 | 별도로 없음 | 내부에 저장 |
| 메모리 | 전체 데이터 크기에 영향 | 지연 처리 시 유리 |
| `next()` | 직접 불가능 | 가능 |

---

# 26. 이터레이터와 제너레이터

제너레이터는 이터레이터를 더 간단하게 만드는 방법이다.

사용자 정의 이터레이터:

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

제너레이터:

```python
def countdown(start):
    while start >= 1:
        yield start
        start -= 1
```

두 코드 모두 값을 하나씩 반환한다.

제너레이터는 다음 문서에서 자세히 다룬다.

```text
17_Python_제너레이터.md
```

---

# 27. 기존 방식에서 개선된 이해

## 27-1. `for`문을 단순 반복 문법으로만 이해

기존 이해:

```text
for문
→ 값을 하나씩 꺼냄
```

개선된 이해:

```text
for문
→ iter()로 이터레이터 생성
→ next() 반복 호출
→ StopIteration에서 종료
```

## 27-2. `range`를 숫자 리스트로 이해

기존 이해:

```text
range
→ 숫자 목록
```

개선된 이해:

```text
range
→ 범위를 표현하는 반복 가능한 객체
→ 필요한 값을 순서대로 제공
```

## 27-3. `map()`을 리스트로 이해

Python 3에서 `map()`은 리스트가 아니라 이터레이터다.

필요한 경우 `list()`로 변환한다.

---

# 28. 대표 오류로 이해하기

## 28-1. 리스트에 바로 `next()` 사용

잘못된 코드:

```python
numbers = [1, 2, 3]

print(next(numbers))
```

발생 결과:

```text
TypeError
```

올바른 코드:

```python
iterator = iter(numbers)

print(next(iterator))
```

---

## 28-2. 끝난 이터레이터에서 다시 `next()` 호출

```python
iterator = iter([1])

print(next(iterator))
print(next(iterator))
```

두 번째 호출에서 `StopIteration`이 발생한다.

---

## 28-3. 소비한 이터레이터 재사용

```python
iterator = iter([1, 2, 3])

print(list(iterator))
print(list(iterator))
```

출력:

```text
[1, 2, 3]
[]
```

첫 번째 `list()`가 이터레이터를 모두 소비했다.

---

## 28-4. `__next__()`에서 종료 조건 누락

```python
class Counter:
    def __next__(self):
        self.current += 1
        return self.current
```

무한히 값을 반환할 수 있다.

의도한 무한 반복이 아니라면 `StopIteration` 조건이 필요하다.

---

## 28-5. `__iter__()`에서 잘못된 값 반환

```python
class Numbers:
    def __iter__(self):
        return [1, 2, 3]
```

`__iter__()`는 리스트가 아니라 이터레이터를 반환해야 한다.

개선:

```python
class Numbers:
    def __iter__(self):
        return iter([1, 2, 3])
```

---

# 29. 이터레이터 구조

```text
Iterable
└─ __iter__()
   └─ Iterator 반환

Iterator
├─ __iter__()
│  └─ 자기 자신 반환
│
└─ __next__()
   ├─ 다음 값 반환
   └─ 종료 시 StopIteration
```

```text
for value in iterable
    ↓
iterator = iter(iterable)
    ↓
value = next(iterator)
    ↓
StopIteration
    ↓
반복 종료
```

---

# 30. 자주 하는 실수

## 30-1. 반복 가능한 객체와 이터레이터를 같은 것으로 생각

리스트는 반복 가능하지만 그 자체에 `next()`를 직접 사용할 수 없다.

## 30-2. 이터레이터가 자동으로 처음으로 돌아간다고 생각

한 번 소비한 이터레이터는 새로 만들지 않는 한 다시 사용할 수 없다.

## 30-3. `StopIteration`을 일반 오류로만 생각

이터레이터가 반복 종료를 알리는 정상적인 신호다.

## 30-4. `__next__()`에서 현재 위치를 변경하지 않음

같은 값만 계속 반환할 수 있다.

## 30-5. `__next__()`에서 종료 조건 누락

무한 이터레이터가 될 수 있다.

## 30-6. `__iter__()`에서 이터레이터가 아닌 객체 반환

`TypeError`가 발생할 수 있다.

## 30-7. 이미 소비한 `map`, `zip`, `enumerate` 재사용

두 번째 순회에서는 값이 나오지 않을 수 있다.

## 30-8. 이터레이터면 무조건 메모리가 절약된다고 생각

원본 데이터가 이미 큰 리스트라면 원본 리스트는 메모리에 남아 있다.

## 30-9. 이터레이터에서 인덱스 접근 시도

일반적으로 `iterator[0]`처럼 사용할 수 없다.

## 30-10. 무한 이터레이터에 종료 조건을 두지 않음

프로그램이 끝나지 않을 수 있다.

---

# 31. 면접·복습 포인트

## Q1. 반복 가능한 객체란 무엇인가요?

`iter()`를 적용할 수 있고 `for`문으로 순회할 수 있는 객체다.

## Q2. 이터레이터란 무엇인가요?

`next()`를 호출할 때마다 다음 값을 하나씩 반환하고 현재 위치를 기억하는 객체다.

## Q3. `iter()`는 무엇을 반환하나요?

반복 가능한 객체에서 이터레이터를 반환한다.

## Q4. `next()`는 무엇을 하나요?

이터레이터에서 다음 값을 하나 반환한다.

## Q5. `StopIteration`은 언제 발생하나요?

이터레이터에서 더 이상 반환할 값이 없을 때 발생한다.

## Q6. `for`문은 `StopIteration`을 어떻게 처리하나요?

내부에서 자동으로 처리하고 반복을 종료한다.

## Q7. 리스트와 이터레이터의 차이는 무엇인가요?

리스트는 전체 값을 저장하고 여러 번 순회할 수 있지만, 이터레이터는 현재 위치를 기억하며 한 번 소비되는 경우가 많다.

## Q8. 사용자 정의 이터레이터에 필요한 메서드는 무엇인가요?

`__iter__()`와 `__next__()`가 필요하다.

## Q9. `__iter__()`는 일반적으로 무엇을 반환하나요?

이터레이터 객체를 반환하며, 이터레이터 자신이라면 `self`를 반환한다.

## Q10. 이터레이터가 메모리에 유리한 이유는 무엇인가요?

값을 한 번에 모두 생성하지 않고 필요한 시점에 하나씩 처리할 수 있기 때문이다.

## Q11. 이터레이터를 다시 처음부터 사용하려면 어떻게 해야 하나요?

원본 반복 가능한 객체에서 새 이터레이터를 만든다.

## Q12. 이터레이터와 제너레이터의 관계는 무엇인가요?

제너레이터는 `yield`를 사용해 이터레이터를 더 간단하게 만드는 방법이다.

---

# 32. 핵심 요약

```text
Iterable
→ 반복 가능한 객체
→ iter() 사용 가능

Iterator
→ next() 사용 가능
→ 현재 위치 기억

iter()
→ 이터레이터 생성

next()
→ 다음 값 반환

StopIteration
→ 반복 종료 신호
```

```text
for문 내부
→ iter()
→ next()
→ StopIteration 처리
```

```text
사용자 정의 이터레이터
→ __iter__()
→ __next__()
→ 종료 시 raise StopIteration
```

---

# 33. 최종 체크리스트

- [ ] 반복 가능한 객체와 이터레이터를 구분할 수 있는가?
- [ ] 리스트에서 `iter()`로 이터레이터를 만들 수 있는가?
- [ ] `next()`로 값을 하나씩 꺼낼 수 있는가?
- [ ] 반복 종료 시 `StopIteration`이 발생하는 이유를 이해했는가?
- [ ] `for`문의 내부 흐름을 설명할 수 있는가?
- [ ] 이터레이터가 현재 위치를 기억한다는 점을 이해했는가?
- [ ] 소비한 이터레이터는 다시 사용할 수 없음을 알고 있는가?
- [ ] `__iter__()`가 올바른 이터레이터를 반환하는가?
- [ ] `__next__()`에서 다음 위치로 이동하는가?
- [ ] 종료 조건에서 `StopIteration`을 발생시키는가?
- [ ] 무한 이터레이터에 외부 종료 조건이 있는가?
- [ ] 이터레이터의 메모리 장점을 과장해서 이해하지 않았는가?

---

# 마무리

이터레이터의 핵심은 값을 한꺼번에 다루는 것이 아니라, **필요할 때 하나씩 요청하고 현재 위치를 이어서 관리하는 것**이다.

```text
반복 가능한 객체 준비
    ↓
이터레이터 생성
    ↓
값 하나씩 요청
    ↓
현재 위치 기억
    ↓
값이 끝나면 StopIteration
```

이 원리를 이해하면 다음 문서에서 다룰 제너레이터의 `yield`가 왜 필요한지 자연스럽게 연결할 수 있다.
