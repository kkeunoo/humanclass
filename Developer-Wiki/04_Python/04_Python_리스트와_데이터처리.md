---
title: Python 리스트와 데이터 처리
version: v3.0-encyclopedia
last_updated: 2026-08-06
status: Completed
---

# Python 리스트와 데이터 처리

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `04_Python_리스트와_데이터처리.md` |
| 분류 | `04_Python` |
| 원본 기준 | `workspace_python/04_list.py`, `workspace_teacher/workspace_python/_04_list.py` |
| 핵심 범위 | 리스트 생성, `range()`, 추가·삭제·정렬, 검색, 복사, 순회, `enumerate()`, 리스트 컴프리헨션, `map()`, 2차원 리스트 |
| 실습 범위 | 숫자 목록 생성, 리스트 변경, 값 검색, 복사 비교, 짝수 목록, 형 변환, 중첩 리스트 조회 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 한 번에 나열하지 않는다.  
> 리스트의 생성·변경·검색·순회·변환에 필요한 코드만 발췌하고, 메서드별 원본 변경 여부와 오류 조건을 함께 설명한다.

---

# 개요

리스트는 여러 값을 순서대로 저장하는 자료형이다.

```text
사용자 목록
상품 목록
점수 목록
게시글 목록
주문 내역
    ↓
여러 값을 하나의 변수로 관리
```

리스트를 사용하면 다음과 같은 작업을 할 수 있다.

```text
값 추가
값 삭제
값 검색
값 정렬
값 반복 처리
조건에 맞는 새 목록 생성
```

Python에서 리스트는 가장 자주 사용하는 자료형 중 하나이며, 이후 반복문·함수·클래스·파일 처리에서도 계속 사용된다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 리스트 | 여러 값을 순서대로 저장하는 변경 가능한 자료형 |
| 인덱스 | 각 값의 위치를 나타내는 번호 |
| `range()` | 일정한 규칙의 숫자 범위 생성 |
| `append()` | 값 하나를 리스트 끝에 추가 |
| `extend()` | 여러 값을 리스트 끝에 추가 |
| `insert()` | 지정 위치에 값 추가 |
| `remove()` | 처음 만나는 특정 값 삭제 |
| `pop()` | 값을 꺼내며 삭제 |
| `sort()` | 원본 리스트 정렬 |
| `reverse()` | 원본 순서 뒤집기 |
| `copy()` | 얕은 복사본 생성 |
| `enumerate()` | 인덱스와 값을 함께 순회 |
| 리스트 컴프리헨션 | 반복·조건을 이용해 새 리스트 생성 |
| `map()` | 모든 값에 같은 함수를 적용 |
| 2차원 리스트 | 리스트 안에 리스트를 저장한 구조 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 빈 리스트와 값이 있는 리스트를 만들 수 있다.
- `range()`의 시작·종료·증가값을 설명할 수 있다.
- 감소하는 숫자 범위를 만들 수 있다.
- 인덱스로 값을 조회하고 삭제할 수 있다.
- `append()`, `extend()`, `insert()`의 차이를 구분할 수 있다.
- `remove()`와 `pop()`의 차이를 설명할 수 있다.
- `sort()`, `reverse()`, 슬라이싱 역순의 차이를 이해한다.
- `index()`와 `count()`를 사용할 수 있다.
- 없는 값을 삭제하거나 검색할 때 발생하는 오류를 이해한다.
- 슬라이싱을 이용해 리스트 끝에 값을 추가할 수 있다.
- 빈 리스트의 Truthy/Falsy 동작을 이해한다.
- 단순 대입과 `copy()`의 차이를 설명할 수 있다.
- `is`와 `==`를 이용해 객체와 값의 차이를 확인할 수 있다.
- 튜플 언패킹과 다중 대입을 사용할 수 있다.
- `for`와 `enumerate()`로 리스트를 순회할 수 있다.
- 리스트 컴프리헨션으로 새 리스트를 만들 수 있다.
- `map()`으로 여러 값을 같은 방식으로 변환할 수 있다.
- 2차원 리스트의 특정 값을 조회할 수 있다.

---

# 1. 리스트 생성

## 1-1. 내 코드와 강사님 코드

```python
a = []
b = list()

print(type(a))
print(type(b))
```

## 1-2. 출력 결과

```text
<class 'list'>
<class 'list'>
```

`[]`와 `list()`는 모두 빈 리스트를 만든다.

## 1-3. 값이 있는 리스트

```python
numbers = [1, 2, 3]

print(numbers)
```

출력:

```text
[1, 2, 3]
```

## 1-4. 구성

| 요소 | 의미 |
| --- | --- |
| `[]` | 리스트 생성 기호 |
| `1, 2, 3` | 리스트에 저장된 값 |
| `numbers` | 리스트를 가리키는 변수 |

> [!TIP]
> 빈 리스트는 일반적으로 `[]`로 작성하는 경우가 많다.
>
> 다른 반복 가능한 객체를 리스트로 변환할 때는 `list()`를 사용한다.

---

# 2. 리스트의 특징

리스트는 다음 특징을 가진다.

- 값의 순서를 유지한다.
- 같은 값을 여러 번 저장할 수 있다.
- 서로 다른 자료형을 함께 저장할 수 있다.
- 인덱스로 값을 조회할 수 있다.
- 생성 후 값을 추가·삭제·변경할 수 있다.

```python
data = [
    1,
    "Python",
    True,
    3.14,
]

print(data)
```

출력:

```text
[1, 'Python', True, 3.14]
```

> [!IMPORTANT]
> 서로 다른 자료형을 저장할 수는 있지만, 실제 데이터 목록은 같은 의미의 값으로 통일하는 편이 관리하기 쉽다.

---

# 3. `range()` 기본 구조

`range()`는 일정한 규칙의 정수 범위를 표현한다.

```python
numbers = range(10)

print(numbers)
print(list(numbers))
```

## 3-1. 출력 결과

```text
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

`range(10)`은 0부터 10 바로 앞까지의 숫자를 표현한다.

```text
시작
→ 0

종료
→ 10 미포함
```

> [!TIP]
> `range()` 자체는 리스트가 아니다.
>
> 실제 목록 형태로 확인하려면 `list()`로 변환한다.

---

# 4. 전달인자 하나인 `range()`

```python
numbers = range(5)

print(list(numbers))
```

출력:

```text
[0, 1, 2, 3, 4]
```

구조:

```python
range(stop)
```

```text
0부터 stop 바로 앞까지
```

---

# 5. 전달인자 두 개인 `range()`

## 5-1. 원본 코드

```python
numbers = range(5, 12)

print(list(numbers))
```

## 5-2. 출력 결과

```text
[5, 6, 7, 8, 9, 10, 11]
```

구조:

```python
range(start, stop)
```

`start`부터 `stop` 바로 앞까지 생성한다.

---

# 6. 시작값이 종료값보다 큰 경우

## 6-1. 원본 코드

```python
numbers = range(12, 5)

print(list(numbers))
```

## 6-2. 출력 결과

```text
[]
```

기본 증가값은 `1`이다.

```text
12에서 시작
    ↓
계속 증가해야 함
    ↓
5보다 작은 방향으로 갈 수 없음
    ↓
빈 범위
```

감소하는 범위가 필요하면 음수 증가값을 사용한다.

---

# 7. 전달인자 세 개인 `range()`

구조:

```python
range(start, stop, step)
```

## 7-1. 증가 범위

```python
numbers = range(
    -4,
    10,
    2,
)

print(list(numbers))
```

출력:

```text
[-4, -2, 0, 2, 4, 6, 8]
```

## 7-2. 감소 범위

내 코드에는 감소 범위 예제가 추가되어 있다.

```python
numbers = range(
    10,
    0,
    -1,
)

print(list(numbers))
```

출력:

```text
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

> [!IMPORTANT]
> `step`이 양수면 증가하고, 음수면 감소한다.
>
> 진행 방향과 시작·종료값이 맞지 않으면 빈 범위가 된다.

---

# 8. 리스트와 `range()` 연결

다음 두 코드는 같은 리스트를 만든다.

```python
numbers = [
    0,
    1,
    2,
    3,
    4,
    5,
]
```

```python
numbers = list(
    range(6)
)
```

출력:

```text
[0, 1, 2, 3, 4, 5]
```

연속된 숫자 목록은 `range()`를 사용하면 더 간결하다.

---

# 9. 인덱스

리스트의 각 값은 0부터 시작하는 인덱스를 가진다.

```python
numbers = [
    10,
    20,
    30,
]
```

```text
값      10  20  30
인덱스   0   1   2
음수    -3  -2  -1
```

조회:

```python
print(numbers[0])
print(numbers[-1])
```

출력:

```text
10
30
```

---

# 10. `del`로 인덱스 삭제

## 10-1. 원본 코드

```python
numbers = list(
    range(6)
)

del numbers[3]

print(numbers)
```

## 10-2. 출력 결과

```text
[0, 1, 2, 4, 5]
```

`del numbers[3]`은 인덱스 3의 값 `3`을 삭제한다.

> [!TIP]
> `del`은 위치를 기준으로 삭제한다.
>
> 특정 값을 기준으로 삭제하려면 `remove()`를 사용한다.

---

# 11. `+`로 새 리스트 만들기

```python
numbers = [
    0,
    1,
    2,
]

new_numbers = (
    numbers
    + [3]
)

print(numbers)
print(new_numbers)
```

출력:

```text
[0, 1, 2]
[0, 1, 2, 3]
```

`+`는 두 리스트를 합친 새 리스트를 만든다.

원본 `numbers`는 변경되지 않는다.

---

# 12. `+=`로 리스트 확장

```python
numbers = [
    0,
    1,
    2,
]

numbers += [3]

print(numbers)
```

출력:

```text
[0, 1, 2, 3]
```

리스트의 `+=`는 기존 리스트에 값을 확장하는 방식으로 동작한다.

---

# 13. `append()`

`append()`는 값 하나를 리스트 끝에 추가한다.

## 13-1. 원본 코드

```python
numbers = [
    0,
    1,
    2,
]

numbers.append(3)

print(numbers)
```

## 13-2. 출력 결과

```text
[0, 1, 2, 3]
```

## 13-3. 리스트를 추가하면

```python
numbers = [1, 2]
extra_numbers = [3, 4]

numbers.append(
    extra_numbers
)

print(numbers)
```

출력:

```text
[1, 2, [3, 4]]
```

리스트 전체가 값 하나로 추가된다.

> [!IMPORTANT]
> `append()`는 전달받은 객체 하나를 추가한다.
>
> 리스트 안의 여러 값을 각각 추가하는 기능은 `extend()`다.

---

# 14. `extend()`

`extend()`는 반복 가능한 객체의 각 값을 리스트 끝에 추가한다.

```python
numbers = [1, 2]

numbers.extend(
    [3, 4]
)

print(numbers)
```

출력:

```text
[1, 2, 3, 4]
```

## 14-1. `append()`와 비교

```python
a = [1, 2]
a.append([3, 4])

b = [1, 2]
b.extend([3, 4])

print(a)
print(b)
```

출력:

```text
[1, 2, [3, 4]]
[1, 2, 3, 4]
```

---

# 15. `insert()`

`insert()`는 지정한 인덱스에 값을 추가한다.

## 15-1. 원본 코드

```python
numbers = [
    10,
    20,
    30,
]

numbers.insert(
    0,
    100,
)

print(numbers)
```

## 15-2. 출력 결과

```text
[100, 10, 20, 30]
```

## 15-3. 범위를 넘는 인덱스

```python
numbers.insert(
    100,
    200,
)

print(numbers)
```

출력:

```text
[100, 10, 20, 30, 200]
```

인덱스가 리스트 길이보다 크면 끝에 추가된다.

---

# 16. 추가 메서드 비교

| 방식 | 동작 |
| --- | --- |
| `append(value)` | 값 하나를 끝에 추가 |
| `extend(values)` | 여러 값을 끝에 추가 |
| `insert(index, value)` | 지정 위치에 값 하나 추가 |
| `+` | 합쳐진 새 리스트 반환 |
| `+=` | 기존 리스트 확장 |

> [!TIP]
> 어떤 값이 추가되는지 먼저 생각한다.
>
> 값 하나면 `append()`, 여러 값이면 `extend()`를 우선 고려한다.

---

# 17. `remove()`

`remove()`는 처음 만나는 특정 값을 삭제한다.

## 17-1. 원본 코드

```python
numbers = [
    1,
    2,
    3,
    4,
    2,
]

numbers.remove(2)

print(numbers)
```

## 17-2. 출력 결과

```text
[1, 3, 4, 2]
```

첫 번째 `2`만 삭제된다.

## 17-3. 없는 값 삭제

```python
numbers.remove(5)
```

발생 결과:

```text
ValueError
```

안전하게 삭제:

```python
if 5 in numbers:
    numbers.remove(5)
```

---

# 18. `pop()`

`pop()`은 값을 삭제하면서 반환한다.

## 18-1. 마지막 값 꺼내기

```python
numbers = [
    10,
    20,
    30,
]

removed_value = (
    numbers.pop()
)

print(numbers)
print(removed_value)
```

출력:

```text
[10, 20]
30
```

## 18-2. 특정 인덱스

```python
numbers = [
    10,
    20,
    30,
]

removed_value = (
    numbers.pop(0)
)

print(numbers)
print(removed_value)
```

출력:

```text
[20, 30]
10
```

## 18-3. `remove()`와 비교

| 메서드 | 기준 | 반환값 |
| --- | --- | --- |
| `remove(value)` | 특정 값 | 없음 |
| `pop(index)` | 특정 위치 | 삭제한 값 |

---

# 19. 스택과 큐

내 코드에는 스택과 큐를 설명한 메모가 있다.

```text
스택
→ 뒤에서 넣고 뒤에서 꺼냄

큐
→ 뒤에서 넣고 앞에서 꺼냄
```

## 19-1. 리스트로 스택 구현

```python
stack = []

stack.append("A")
stack.append("B")

print(stack.pop())
print(stack.pop())
```

출력:

```text
B
A
```

## 19-2. 큐 주의점

리스트에서 `pop(0)`을 반복하면 앞쪽 값을 이동시키는 비용이 발생한다.

실무에서 큐가 필요하면 `collections.deque`를 우선 고려한다.

---

# 20. `sort()`

`sort()`는 원본 리스트를 정렬한다.

## 20-1. 오름차순

```python
numbers = [
    654,
    156,
    964,
    15,
    35,
]

numbers.sort()

print(numbers)
```

출력:

```text
[15, 35, 156, 654, 964]
```

## 20-2. 내림차순

```python
numbers.sort(
    reverse=True
)

print(numbers)
```

출력:

```text
[964, 654, 156, 35, 15]
```

## 20-3. 반환값 주의

```python
numbers = [3, 1, 2]

result = numbers.sort()

print(result)
```

출력:

```text
None
```

> [!IMPORTANT]
> `sort()`는 원본을 변경하고 `None`을 반환한다.

---

# 21. `sorted()`

원본을 유지하고 정렬된 새 리스트가 필요하면 `sorted()`를 사용할 수 있다.

```python
numbers = [3, 1, 2]

sorted_numbers = sorted(
    numbers
)

print(numbers)
print(sorted_numbers)
```

출력:

```text
[3, 1, 2]
[1, 2, 3]
```

## 21-1. 선택 기준

```text
원본 변경 가능
→ list.sort()

원본 유지 필요
→ sorted()
```

---

# 22. 슬라이싱으로 역순 만들기

## 22-1. 원본 코드

```python
numbers = [
    15,
    35,
    156,
    654,
    964,
]

reversed_numbers = (
    numbers[::-1]
)

print(reversed_numbers)
```

## 22-2. 출력 결과

```text
[964, 654, 156, 35, 15]
```

`[::-1]`은 역순의 새 리스트를 만든다.

원본은 변경되지 않는다.

---

# 23. `reverse()`

`reverse()`는 원본 리스트의 순서를 뒤집는다.

```python
numbers = [
    15,
    35,
    156,
]

numbers.reverse()

print(numbers)
```

출력:

```text
[156, 35, 15]
```

## 23-1. 비교

| 방식 | 원본 변경 | 결과 |
| --- | --- | --- |
| `numbers[::-1]` | 아니오 | 새 리스트 |
| `numbers.reverse()` | 예 | `None` |
| `reversed(numbers)` | 아니오 | 이터레이터 |

---

# 24. `reversed()`

```python
numbers = [
    1,
    2,
    3,
]

result = reversed(
    numbers
)

print(result)
print(list(result))
```

출력 형태:

```text
<list_reverseiterator object at ...>
[3, 2, 1]
```

`reversed()`는 리스트 자체가 아니라 이터레이터를 반환한다.

---

# 25. `index()`

`index()`는 처음 만나는 값의 위치를 반환한다.

## 25-1. 원본 코드

```python
numbers = [
    1,
    2,
    3,
    4,
    2,
    4,
]

position = numbers.index(2)

print(position)
```

## 25-2. 출력 결과

```text
1
```

없는 값을 검색하면 오류가 발생한다.

```python
numbers.index(5)
```

발생 결과:

```text
ValueError
```

> [!IMPORTANT]
> 문자열에는 `find()`가 있지만 리스트에는 `find()`가 없다.

포함 여부만 필요하면 `in`을 사용한다.

```python
print(5 in numbers)
```

---

# 26. `count()`

`count()`는 특정 값이 몇 번 나타나는지 반환한다.

```python
numbers = [
    1,
    2,
    3,
    4,
    2,
    4,
]

print(numbers.count(4))
```

출력:

```text
2
```

---

# 27. `clear()`

`clear()`는 리스트의 모든 값을 삭제한다.

```python
numbers = [
    1,
    2,
    3,
]

numbers.clear()

print(numbers)
```

출력:

```text
[]
```

다음과 비슷해 보인다.

```python
numbers = []
```

하지만 차이가 있다.

```text
clear()
→ 기존 리스트 객체를 비움

numbers = []
→ 변수에 새로운 빈 리스트를 대입
```

다른 변수가 같은 리스트를 참조하고 있다면 결과가 달라질 수 있다.

---

# 28. 범위를 벗어난 인덱스와 슬라이싱

## 28-1. 인덱스 조회

```python
numbers = [
    1,
    2,
    3,
]

print(numbers[3])
```

발생 결과:

```text
IndexError
```

## 28-2. 슬라이싱

```python
print(numbers[3:])
print(numbers[len(numbers):])
```

출력:

```text
[]
[]
```

슬라이싱은 범위를 넘더라도 가능한 범위 안에서 결과를 반환한다.

> [!TIP]
> 단일 인덱스 조회는 값이 반드시 있어야 하지만, 슬라이싱은 빈 리스트를 반환할 수 있다.

---

# 29. 슬라이스 대입

## 29-1. 리스트 끝에 여러 값 추가

```python
numbers = [
    1,
    2,
    3,
]

numbers[3:] = [
    4,
    5,
    6,
]

print(numbers)
```

출력:

```text
[1, 2, 3, 4, 5, 6]
```

## 29-2. 반복 가능한 값 필요

```python
numbers[3:] = 4
```

발생 결과:

```text
TypeError
```

슬라이스에는 리스트처럼 반복 가능한 객체를 대입해야 한다.

## 29-3. 길이를 이용한 끝 추가

```python
numbers = [
    1,
    2,
    3,
]

numbers[len(numbers):] = [
    500
]

print(numbers)
```

출력:

```text
[1, 2, 3, 500]
```

---

# 30. 빈 리스트와 Truthy/Falsy

## 30-1. 원본 코드

```python
values = []

print(len(values))
print(not len(values))
```

## 30-2. 출력 결과

```text
0
True
```

빈 리스트는 Falsy로 평가된다.

더 Python다운 표현:

```python
if not values:
    print("목록이 비어 있습니다.")
```

출력:

```text
목록이 비어 있습니다.
```

> [!TIP]
> 비어 있는지만 확인할 때는 `len(values) == 0`보다 `not values`를 우선 고려한다.

---

# 31. 리스트 단순 대입

## 31-1. 원본 코드

```python
a = [
    1,
    2,
    3,
    4,
    5,
]

b = a

b[2] = 30

print(b)
print(a)
```

## 31-2. 출력 결과

```text
[1, 2, 30, 4, 5]
[1, 2, 30, 4, 5]
```

`b = a`는 리스트 값을 새로 복사하지 않는다.

두 변수가 같은 리스트 객체를 가리킨다.

```text
a ─┐
   ├→ 같은 리스트 객체
b ─┘
```

---

# 32. `copy()`

## 32-1. 원본 코드

```python
a = [
    1,
    2,
    3,
    4,
    5,
]

b = a.copy()

b[2] = 30

print(b)
print(a)
```

## 32-2. 출력 결과

```text
[1, 2, 30, 4, 5]
[1, 2, 3, 4, 5]
```

`copy()`는 새로운 리스트 객체를 만든다.

## 32-3. 동일성과 값 비교

```python
a = [
    1,
    2,
    3,
]

b = a.copy()

print(a is b)
print(a == b)
```

출력:

```text
False
True
```

| 표현 | 의미 |
| --- | --- |
| `a is b` | 같은 객체인지 확인 |
| `a == b` | 내부 값이 같은지 확인 |

---

# 33. 얕은 복사 주의

`copy()`는 얕은 복사다.

중첩 리스트의 내부 객체는 공유될 수 있다.

```python
a = [
    [1, 2],
    [3, 4],
]

b = a.copy()

b[0][0] = 100

print(a)
print(b)
```

출력:

```text
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
```

중첩 구조를 완전히 분리하려면 `copy.deepcopy()`를 검토한다.

---

# 34. 튜플 언패킹

## 34-1. 기존 방식

```python
values = (
    1,
    2,
)

a = values[0]
b = values[1]
```

## 34-2. Python 방식

```python
a, b = (
    1,
    2,
)

print(a)
print(b)
```

## 34-3. 출력 결과

```text
1
2
```

오른쪽의 값을 왼쪽 변수에 순서대로 대입한다.

---

# 35. 리스트 직접 순회

## 35-1. 원본 코드

```python
numbers = [
    10,
    20,
    30,
]

for number in numbers:
    print(number)
```

## 35-2. 출력 결과

```text
10
20
30
```

인덱스가 필요하지 않으면 값을 직접 순회하는 방식이 가장 자연스럽다.

---

# 36. `enumerate()`

`enumerate()`는 인덱스와 값을 함께 반환한다.

## 36-1. 원본 코드

```python
numbers = [
    10,
    20,
    30,
]

for index, value in enumerate(
    numbers
):
    print(index, value)
```

## 36-2. 출력 결과

```text
0 10
1 20
2 30
```

## 36-3. 시작 인덱스 지정

```python
for index, value in enumerate(
    numbers,
    start=100,
):
    print(index, value)
```

출력:

```text
100 10
101 20
102 30
```

> [!TIP]
> 인덱스가 필요하면 `range(len(numbers))`보다 `enumerate(numbers)`를 우선 고려한다.

---

# 37. 가장 큰 값 찾기

## 37-1. 원본 방식

```python
numbers = [
    7,
    3,
    5,
    8,
    4,
]

numbers.sort()

print(numbers[-1])
```

출력:

```text
8
```

정렬 후 마지막 값을 가져올 수 있다.

## 37-2. 더 직접적인 방식

```python
numbers = [
    7,
    3,
    5,
    8,
    4,
]

print(max(numbers))
```

출력:

```text
8
```

> [!IMPORTANT]
> 가장 큰 값 하나만 필요하다면 전체 정렬보다 `max()`가 의도를 더 직접적으로 표현한다.

---

# 38. `range(len())` 사용 기준

원본에는 인덱스를 이용해 마지막 값을 찾는 반복문이 있다.

```python
for index in range(
    len(numbers)
):
    if index == (
        len(numbers) - 1
    ):
        print(numbers[index])
```

동작하지만 마지막 값만 필요하다면 다음이 더 간단하다.

```python
print(numbers[-1])
```

## 38-1. 언제 `range(len())`을 사용할까?

- 인덱스로 여러 위치를 직접 수정해야 할 때
- 앞뒤 값의 위치를 계산해야 할 때
- 인덱스 범위 자체가 핵심일 때

단순 순회는 직접 값 순회 또는 `enumerate()`가 더 읽기 쉽다.

---

# 39. 반복문으로 리스트 만들기

## 39-1. 원본 코드

```python
numbers = []

for number in range(10):
    numbers.append(number)

print(numbers)
```

## 39-2. 출력 결과

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```text
빈 리스트 생성
    ↓
0~9 반복
    ↓
append()
    ↓
새 값 추가
```

---

# 40. 리스트 컴프리헨션

같은 코드를 리스트 컴프리헨션으로 작성할 수 있다.

```python
numbers = [
    number
    for number in range(10)
]

print(numbers)
```

출력:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 40-1. 기본 구조

```python
[
    표현식
    for 변수 in 반복가능객체
]
```

## 40-2. 값 변환

강사님 코드에는 값을 두 배로 만드는 예제가 있다.

```python
numbers = [
    number * 2
    for number in range(5)
]

print(numbers)
```

출력:

```text
[0, 2, 4, 6, 8]
```

---

# 41. 조건이 있는 리스트 컴프리헨션

## 41-1. 반복문 방식

```python
even_numbers = []

for number in range(10):
    if number % 2 == 0:
        even_numbers.append(
            number
        )
```

## 41-2. 컴프리헨션 방식

```python
even_numbers = [
    number
    for number in range(10)
    if number % 2 == 0
]

print(even_numbers)
```

## 41-3. 출력 결과

```text
[0, 2, 4, 6, 8]
```

> [!TIP]
> 단순한 변환과 필터링에는 리스트 컴프리헨션이 적합하다.
>
> 조건과 처리 단계가 복잡하면 일반 반복문이 더 읽기 쉽다.

---

# 42. 문자열을 만드는 컴프리헨션

강사님 코드에는 구구단 문자열 예제가 있다.

```python
results = [
    f"2x{number}={2 * number}"
    for number in range(10)
    if number % 2 == 0
]

print(results)
```

출력:

```text
['2x0=0', '2x2=4', '2x4=8', '2x6=12', '2x8=16']
```

컴프리헨션의 표현식에는 f-string도 사용할 수 있다.

---

# 43. 반복문으로 형 변환

## 43-1. 원본 코드

```python
numbers = [
    1.2,
    2.5,
    3.7,
    4.6,
    -3.5,
]

for index, value in enumerate(
    numbers
):
    numbers[index] = int(value)

print(numbers)
```

## 43-2. 출력 결과

```text
[1, 2, 3, 4, -3]
```

`int()`는 소수 부분을 0 방향으로 제거한다.

---

# 44. `map()`

`map()`은 반복 가능한 객체의 각 값을 함수에 전달한다.

## 44-1. 원본 코드

```python
numbers = [
    1.2,
    2.5,
    3.7,
    4.6,
    -3.5,
]

converted_numbers = list(
    map(
        int,
        numbers,
    )
)

print(converted_numbers)
```

## 44-2. 출력 결과

```text
[1, 2, 3, 4, -3]
```

## 44-3. 동작 과정

```text
numbers의 값 하나씩 꺼냄
    ↓
int()에 전달
    ↓
변환 결과 생성
    ↓
map 객체 반환
    ↓
list()로 리스트 변환
```

## 44-4. 컴프리헨션과 비교

```python
converted_numbers = [
    int(number)
    for number in numbers
]
```

두 방식 모두 사용할 수 있다.

단순 변환은 리스트 컴프리헨션이 더 읽기 쉬운 경우가 많다.

---

# 45. 2차원 리스트

리스트 안에 리스트를 저장할 수 있다.

## 45-1. 원본 코드

```python
matrix = [
    [10, 20],
    [30, 40],
    [50, 60],
]
```

## 45-2. 행 개수

```python
print(len(matrix))
```

출력:

```text
3
```

## 45-3. 특정 값 조회

```python
print(matrix[1][0])
```

출력:

```text
30
```

```text
matrix[1]
→ 두 번째 리스트 [30, 40]

matrix[1][0]
→ 그 리스트의 첫 번째 값 30
```

---

# 46. 리스트 반복

## 46-1. 원본 코드

```python
print([0] * 10)
```

## 46-2. 출력 결과

```text
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

같은 값을 여러 개 가진 초기 리스트를 만들 수 있다.

## 46-3. 중첩 리스트 주의

```python
matrix = [
    [0] * 3
] * 3
```

각 행이 같은 내부 리스트를 공유할 수 있다.

안전한 생성:

```python
matrix = [
    [0] * 3
    for _ in range(3)
]
```

---

# 47. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| `range()` | 감소 범위 예제 추가 | 기본 1·2·3개 인자 중심 |
| 추가 메서드 | `append()`와 `extend()` 차이를 상세 기록 | 핵심 동작 중심 |
| 정렬 | JavaScript 정렬과 비교 메모 | Python 정렬 예제 중심 |
| 스택·큐 | 개념 메모 추가 | 직접 설명 없음 |
| 슬라이싱 | 길이를 이용한 끝 추가 예제 추가 | 기본 슬라이스 대입 |
| 복사 | `is`, `==` 비교 추가 | 단순 대입과 `copy()` 비교 |
| 최대값 | 여러 방식으로 마지막 값 확인 | 정렬 후 마지막 값 |
| 컴프리헨션 | 기본·짝수 예제 | 변환·조건·f-string 예제 |
| `map()` | 원본 실수 목록에 다시 적용 | 반복 변환 후 `map()` 적용 |

## 47-1. 내 코드의 장점

- 메서드별 차이와 오류 조건을 자세히 기록했다.
- 감소 범위, 스택·큐, 슬라이싱 대입을 추가로 실험했다.
- 단순 대입과 복사의 객체 차이를 직접 확인했다.
- `enumerate()`, 컴프리헨션, `map()`의 목적을 메모했다.

## 47-2. 내 코드의 개선점

- `append()`와 `extend()`를 JavaScript 개념에만 연결하기보다 Python 동작을 우선 설명해야 한다.
- `reverse()`는 내림차순 정렬이 아니라 현재 순서를 뒤집는 메서드다.
- 가장 큰 값 하나를 찾기 위해 전체 정렬할 필요는 없다.
- `copy()`는 중첩 객체까지 완전히 복사하는 깊은 복사가 아니다.
- 빈 리스트 검사는 `not values`로 더 직접적으로 작성할 수 있다.

## 47-3. 강사님 코드의 장점

- 리스트의 생성부터 변환까지 주요 기능을 한 흐름으로 실습한다.
- 반복문과 리스트 컴프리헨션을 비교할 수 있다.
- `enumerate()`와 `map()`의 기본 동작을 직접 확인할 수 있다.
- 오류 예제를 주석 처리해 정상 실행과 함께 비교할 수 있다.

## 47-4. 강사님 코드의 보충점

- `append()`와 `extend()`의 중첩 결과 차이를 더 명확히 설명할 필요가 있다.
- `sort()`, `reverse()`, `reversed()`의 원본 변경 여부를 구분해야 한다.
- `copy()`가 얕은 복사라는 설명이 필요하다.
- 리스트 최대값에는 `max()`를 사용할 수 있다는 보충이 필요하다.

---

# 48. 기존 코드에서 개선 코드로 바꾼 이유

## 48-1. 직접 순회

기존:

```python
for index in range(
    len(numbers)
):
    print(numbers[index])
```

개선:

```python
for number in numbers:
    print(number)
```

이유:

- 값만 필요할 때 인덱스를 만들 필요가 없다.
- 코드의 목적이 더 명확하다.

## 48-2. 인덱스와 값

기존:

```python
for index in range(
    len(numbers)
):
    value = numbers[index]
```

개선:

```python
for index, value in enumerate(
    numbers
):
    ...
```

## 48-3. 최대값

기존:

```python
numbers.sort()
largest = numbers[-1]
```

개선:

```python
largest = max(numbers)
```

## 48-4. 빈 목록 확인

기존:

```python
if len(values) == 0:
    ...
```

개선:

```python
if not values:
    ...
```

## 48-5. 원본 유지 정렬

기존:

```python
numbers.sort()
```

원본을 유지해야 한다면:

```python
sorted_numbers = sorted(
    numbers
)
```

---

# 49. 실무형 예제: 상품 재고 목록

```python
products = [
    {
        "name": "Keyboard",
        "price": 45000,
        "stock": 5,
    },
    {
        "name": "Mouse",
        "price": 25000,
        "stock": 0,
    },
    {
        "name": "Monitor",
        "price": 210000,
        "stock": 3,
    },
]

available_products = [
    product
    for product in products
    if product["stock"] > 0
]

sorted_products = sorted(
    available_products,
    key=lambda product: (
        product["price"]
    ),
)

for number, product in enumerate(
    sorted_products,
    start=1,
):
    print(
        f'{number}. '
        f'{product["name"]} / '
        f'{product["price"]:,}원 / '
        f'재고 {product["stock"]}개'
    )
```

## 49-1. 출력 결과

```text
1. Keyboard / 45,000원 / 재고 5개
2. Monitor / 210,000원 / 재고 3개
```

## 49-2. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| 리스트 안의 딕셔너리 | 여러 상품 정보를 구조적으로 저장 |
| 리스트 컴프리헨션 | 재고가 있는 상품만 필터링 |
| `sorted()` | 원본을 유지하며 가격순 정렬 |
| `lambda` | 상품 가격을 정렬 기준으로 반환 |
| `enumerate()` | 출력 순번과 상품을 함께 사용 |
| f-string | 가격과 재고를 읽기 좋은 문자열로 출력 |

---

# 50. 대표 오류로 이해하기

## 50-1. 없는 인덱스 조회

```python
numbers = [1, 2, 3]

print(numbers[3])
```

발생 결과:

```text
IndexError
```

---

## 50-2. 없는 값 삭제

```python
numbers = [1, 2, 3]

numbers.remove(5)
```

발생 결과:

```text
ValueError
```

---

## 50-3. 없는 값의 인덱스 검색

```python
numbers = [1, 2, 3]

numbers.index(5)
```

발생 결과:

```text
ValueError
```

---

## 50-4. 빈 리스트에서 `pop()`

```python
numbers = []

numbers.pop()
```

발생 결과:

```text
IndexError
```

---

## 50-5. `sort()` 반환값 저장

```python
numbers = [3, 1, 2]

numbers = numbers.sort()

print(numbers)
```

출력:

```text
None
```

개선:

```python
numbers.sort()
```

또는:

```python
numbers = sorted(numbers)
```

---

## 50-6. 단순 대입을 복사로 착각

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
```

출력:

```text
[1, 2, 3, 4]
```

같은 리스트를 공유하기 때문이다.

---

# 51. 자주 하는 실수

## 51-1. `range()`의 종료값이 포함된다고 생각

종료값 바로 앞까지만 생성한다.

## 51-2. 감소 범위에 양수 `step` 사용

진행 방향이 맞지 않아 빈 범위가 된다.

## 51-3. `append()`가 리스트 내부 값을 펼친다고 생각

전달한 리스트 전체가 값 하나로 추가된다.

## 51-4. `extend()`에 숫자 하나 전달

숫자는 반복 가능한 객체가 아니므로 오류가 발생한다.

## 51-5. `remove()`가 모든 같은 값을 삭제한다고 생각

처음 만나는 값 하나만 삭제한다.

## 51-6. `sort()`와 `reverse()`를 같은 기능으로 이해

`sort()`는 값의 크기 기준 정렬, `reverse()`는 현재 순서 반전이다.

## 51-7. `sort()` 결과를 변수에 저장

`None`이 저장된다.

## 51-8. 리스트에 `find()` 사용

리스트에는 `find()`가 없다.

## 51-9. 슬라이싱과 단일 인덱스 오류를 같은 방식으로 생각

슬라이싱은 범위를 넘으면 빈 리스트를 반환할 수 있다.

## 51-10. `b = a`를 복사로 이해

두 변수가 같은 객체를 가리킨다.

## 51-11. `copy()`가 중첩 객체까지 완전히 분리한다고 생각

얕은 복사이므로 내부 객체를 공유할 수 있다.

## 51-12. 값만 필요한데 `range(len())` 사용

직접 순회가 더 간단하다.

## 51-13. 복잡한 처리를 리스트 컴프리헨션 한 줄에 작성

가독성이 떨어질 수 있다.

## 51-14. 중첩 리스트를 `[[0] * n] * n`으로 생성

각 행이 같은 내부 리스트를 공유할 수 있다.

---

# 52. 핵심 요약

```text
[]
list()
→ 리스트 생성

range()
→ 숫자 범위

append()
→ 값 하나 추가

extend()
→ 여러 값 추가

insert()
→ 지정 위치 추가
```

```text
del
→ 인덱스로 삭제

remove()
→ 값으로 삭제

pop()
→ 삭제하며 반환

clear()
→ 전체 삭제
```

```text
sort()
→ 원본 정렬

sorted()
→ 새 정렬 리스트

reverse()
→ 원본 순서 반전

[::-1]
→ 역순 새 리스트
```

```text
index()
→ 값 위치

count()
→ 값 개수

copy()
→ 얕은 복사

enumerate()
→ 인덱스와 값

map()
→ 같은 함수 적용
```

---

# 53. 최종 체크리스트

- [ ] 빈 리스트와 값이 있는 리스트를 만들 수 있는가?
- [ ] `range()`의 종료값이 포함되지 않음을 이해했는가?
- [ ] 증가·감소 범위를 만들 수 있는가?
- [ ] 인덱스로 값을 조회하고 삭제할 수 있는가?
- [ ] `append()`, `extend()`, `insert()`를 구분할 수 있는가?
- [ ] `remove()`와 `pop()`을 구분할 수 있는가?
- [ ] `sort()`가 원본을 변경하고 `None`을 반환함을 이해했는가?
- [ ] `sorted()`로 원본을 유지할 수 있는가?
- [ ] `reverse()`, `reversed()`, `[::-1]`을 구분할 수 있는가?
- [ ] `index()`와 `count()`를 사용할 수 있는가?
- [ ] 슬라이싱과 단일 인덱스의 범위 초과 차이를 이해했는가?
- [ ] 빈 리스트를 `not values`로 검사할 수 있는가?
- [ ] 단순 대입과 `copy()`의 차이를 이해했는가?
- [ ] 얕은 복사의 한계를 이해했는가?
- [ ] 튜플 언패킹을 사용할 수 있는가?
- [ ] 값만 필요할 때 직접 순회할 수 있는가?
- [ ] 인덱스가 필요할 때 `enumerate()`를 사용할 수 있는가?
- [ ] 리스트 컴프리헨션으로 변환·필터링할 수 있는가?
- [ ] `map()`으로 모든 값을 변환할 수 있는가?
- [ ] 2차원 리스트의 특정 값을 조회할 수 있는가?
- [ ] 중첩 리스트 초기화 시 객체 공유를 주의하는가?

---

# 마무리

리스트 처리의 핵심은 여러 값을 저장하는 것에서 끝나지 않는다.

```text
값을 순서대로 저장하고
    ↓
필요한 값을 추가·삭제하고
    ↓
검색·정렬하고
    ↓
반복문으로 처리하고
    ↓
조건에 맞는 새 리스트로 변환하는 것
```

이 흐름을 이해하면 이후 튜플·딕셔너리·집합과 반복문을 더 자연스럽게 연결할 수 있다.

# V3 동작 백과 보강 — 리스트의 참조와 변경

리스트는 여러 객체의 참조를 순서대로 보관하는 변경 가능한 객체다. `append(x)`는 `x` 하나를 끝에 넣고, `extend(iterable)`은 반복 가능한 값의 원소를 차례로 넣는다. 두 메서드는 원본 리스트를 바꾸며 반환값은 `None`이다.

```python
a = [1, 2]
b = a
c = a.copy()
a.append(3)
print(a)
print(b)
print(c)
```

```text
[1, 2, 3]
[1, 2, 3]
[1, 2]
```

`b = a`는 복사가 아니라 같은 리스트를 가리키는 이름을 하나 더 만든다. `copy()`는 새 바깥 리스트를 만들지만 내부에 중첩된 객체까지 복제하는 깊은 복사는 아니다. 인덱스 범위를 벗어나면 `IndexError`가 발생한다.

**원본 연결:** 내 코드 `workspace_python/04_list.py`, 강사님 코드 `workspace_python/_04_list.py`의 생성, 추가·삭제, 정렬, 반복 처리 예제를 기반으로 한다.
