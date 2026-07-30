# Python 튜플과 불변 자료형

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `05_Python_튜플과_불변자료형.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `04_Python_리스트와_컴프리헨션.md` |
| 다음 학습 | `06_Python_시퀀스.md` |
| 원본 기준 | `workspace_python/05_tuple.py`, `workspace_teacher/workspace_python/_05_tuple.py` |
| 핵심 범위 | 튜플 선언, 튜플 패킹, 한 요소 튜플, 쉼표의 역할, 불변성, 리스트·튜플 변환 |
| 보충 범위 | 빈 튜플, 인덱싱, 슬라이싱, 언패킹, `count()`, `index()`, 중첩 객체, 해시 가능성, 함수 반환값 |

> 이 문서는 내 코드의 `05_tuple.py`와 강사님 코드의 `_05_tuple.py`를 직접 비교해 작성했습니다. 원본에서 직접 다루는 범위는 튜플 선언, 괄호 없는 선언, 한 요소 튜플, 리스트와 튜플 사이의 자료형 변환입니다. 그 밖의 내용은 원본 개념을 정확하게 이해하기 위해 추가한 보충 학습입니다.

---

# 학습 목표

- 튜플의 자료형과 기본 특징을 설명할 수 있다.
- 소괄호를 사용하거나 생략하여 튜플을 만들 수 있다.
- 튜플을 만드는 핵심 문법이 괄호보다 쉼표라는 점을 이해한다.
- 한 요소 튜플에 쉼표가 반드시 필요한 이유를 설명할 수 있다.
- 빈 튜플을 `()` 또는 `tuple()`로 만들 수 있다.
- 리스트와 튜플의 공통점과 차이점을 구분할 수 있다.
- 튜플의 요소를 인덱싱하고 슬라이싱할 수 있다.
- 튜플 요소를 직접 변경할 수 없는 이유를 이해한다.
- 튜플 안에 변경 가능한 객체가 있을 때의 동작을 설명할 수 있다.
- `tuple()`과 `list()`로 자료형을 변환할 수 있다.
- 튜플 패킹과 언패킹을 사용할 수 있다.
- `count()`와 `index()`를 사용할 수 있다.
- 튜플이 함수 반환값과 딕셔너리 키에 활용되는 이유를 설명할 수 있다.
- 내 코드와 강사님 코드의 차이를 정리할 수 있다.
- 원본 주석의 부정확한 설명을 정확한 개념으로 수정할 수 있다.

---

# 1. 원본 코드

## 1.1 내 코드

```python
# 선언 (readonly list)
# a = () 처럼 빈 것으로 선언 불가하며, 값은 바꾸지 못 함
a = (1,2,3)
print(a, type(a))

# tuple은 ()없이도 선언해서 사용할 수 있음
b = 1,2,3
print(b, type(b))

# 값이 1개인 tuple을 선언하기 위해서는 ','를 써줘야 함
c = (3,)
print(c, type(c))
d = 4,
print(d, type(d))

# 아래와 같이 tuple > list , list > tuple 변경 가능
e = [1,2,3]
print(tuple(e))
f = (1,2,3)
print(list(f))
```

## 1.2 강사님 코드

```python
# 선언
a = (1,2,3)
print(a, type(a))

b = 1,2,3
print(b, type(b))

# 값이 하나인 튜플 선언
c = (3,)
d = 4,
print(d, type(d))
```

---

# 2. 원본 실행 결과

내 코드의 실행 결과는 다음과 같습니다.

```text
(1, 2, 3) <class 'tuple'>
(1, 2, 3) <class 'tuple'>
(3,) <class 'tuple'>
(4,) <class 'tuple'>
(1, 2, 3)
[1, 2, 3]
```

강사님 코드의 실행 결과는 다음과 같습니다.

```text
(1, 2, 3) <class 'tuple'>
(1, 2, 3) <class 'tuple'>
(4,) <class 'tuple'>
```

강사님 코드에서는 `c = (3,)`를 선언하지만 `c`는 출력하지 않습니다.

---

# 3. 튜플이란?

튜플(tuple)은 여러 값을 순서대로 저장하는 Python의 시퀀스 자료형입니다.

```python
numbers = (10, 20, 30)
```

자료형 확인:

```python
print(type(numbers))
```

출력:

```text
<class 'tuple'>
```

튜플은 다음 특징을 가집니다.

| 특징 | 설명 |
| --- | --- |
| 순서 유지 | 요소가 저장된 순서를 기억한다. |
| 인덱스 사용 | 첫 번째 요소의 인덱스는 `0`이다. |
| 중복 허용 | 같은 값을 여러 번 저장할 수 있다. |
| 여러 자료형 허용 | 숫자, 문자열, 리스트 등 다양한 객체를 저장할 수 있다. |
| 불변성 | 튜플이 만들어진 뒤 요소의 위치와 참조를 직접 변경할 수 없다. |

예:

```python
data = (1, "Python", True, 3.14)
```

---

# 4. 리스트와 튜플의 관계

내 코드에는 튜플을 다음처럼 설명한 주석이 있습니다.

```python
# 선언 (readonly list)
```

초기 학습에서는 튜플을 “수정할 수 없는 리스트와 비슷한 자료형”으로 이해할 수 있습니다. 그러나 튜플을 단순히 읽기 전용 리스트라고만 표현하면 일부 차이를 놓칠 수 있습니다.

리스트와 튜플은 모두 순서와 인덱스를 가지지만 목적과 동작이 다릅니다.

| 비교 | 리스트 | 튜플 |
| --- | --- | --- |
| 표기 | `[1, 2, 3]` | `(1, 2, 3)` |
| 자료형 | `list` | `tuple` |
| 요소 변경 | 가능 | 직접 변경 불가 |
| 요소 추가·삭제 | 가능 | 불가 |
| 주요 용도 | 계속 변하는 데이터 | 고정된 구조나 값의 묶음 |
| 메서드 수 | 많음 | 적음 |
| 딕셔너리 키 | 사용할 수 없음 | 조건을 만족하면 사용 가능 |

따라서 다음 표현이 더 정확합니다.

```text
튜플은 순서를 가진 불변 시퀀스 자료형이다.
```

---

# 5. 기본 튜플 선언

공통 원본:

```python
a = (1, 2, 3)

print(a, type(a))
```

출력:

```text
(1, 2, 3) <class 'tuple'>
```

소괄호 안에 값을 쉼표로 구분해 작성합니다.

```python
names = ("민수", "영희", "철수")
```

튜플은 서로 다른 자료형도 저장할 수 있습니다.

```python
profile = ("근욱", 30, True)
```

---

# 6. 괄호 없이 튜플 선언

공통 원본:

```python
b = 1, 2, 3

print(b, type(b))
```

출력:

```text
(1, 2, 3) <class 'tuple'>
```

Python에서는 소괄호를 생략해도 쉼표로 구분된 값은 튜플이 됩니다.

```python
coordinates = 10, 20
```

자료형:

```python
print(type(coordinates))
```

출력:

```text
<class 'tuple'>
```

---

# 7. 튜플을 만드는 핵심은 쉼표

튜플을 만드는 핵심 문법은 소괄호 자체보다 쉼표입니다.

```python
a = (1, 2, 3)
b = 1, 2, 3
```

두 변수 모두 튜플입니다.

```python
print(type(a))
print(type(b))
```

출력:

```text
<class 'tuple'>
<class 'tuple'>
```

소괄호는 다음 목적에도 사용됩니다.

- 연산 우선순위 지정
- 함수 호출
- 조건식 묶기
- 표현식 가독성 향상

따라서 소괄호가 있다고 무조건 튜플은 아닙니다.

---

# 8. 소괄호만으로는 튜플이 되지 않는다

```python
value = (3)

print(value)
print(type(value))
```

출력:

```text
3
<class 'int'>
```

`(3)`은 정수 `3`을 괄호로 묶은 표현식입니다.

한 요소 튜플을 만들려면 쉼표가 필요합니다.

```python
value = (3,)
```

---

# 9. 한 요소 튜플

공통 원본:

```python
c = (3,)
print(c, type(c))
```

출력:

```text
(3,) <class 'tuple'>
```

한 요소 튜플은 값 뒤에 쉼표를 반드시 작성합니다.

```python
single = ("Python",)
```

쉼표가 없으면 해당 값 자체의 자료형이 됩니다.

```python
not_tuple = ("Python")
```

자료형 비교:

```python
print(type(single))
print(type(not_tuple))
```

출력:

```text
<class 'tuple'>
<class 'str'>
```

---

# 10. 괄호 없는 한 요소 튜플

공통 원본:

```python
d = 4,

print(d, type(d))
```

출력:

```text
(4,) <class 'tuple'>
```

괄호를 생략해도 쉼표가 있으므로 튜플입니다.

```python
single = "Python",
```

다만 한 요소 튜플은 다음 형태가 의도를 더 분명하게 보여 줍니다.

```python
single = ("Python",)
```

---

# 11. 빈 튜플

내 코드 주석에는 다음 내용이 있습니다.

```python
# a = () 처럼 빈 것으로 선언 불가하며
```

이 설명은 정확하지 않습니다.

Python에서는 빈 튜플을 정상적으로 선언할 수 있습니다.

```python
empty = ()
```

자료형:

```python
print(empty)
print(type(empty))
```

출력:

```text
()
<class 'tuple'>
```

`tuple()`도 사용할 수 있습니다.

```python
empty = tuple()
```

두 방식 모두 빈 튜플을 만듭니다.

---

# 12. 빈 튜플과 빈 리스트

```python
empty_tuple = ()
empty_list = []
```

| 항목 | 빈 튜플 | 빈 리스트 |
| --- | --- | --- |
| 표기 | `()` | `[]` |
| 자료형 | `tuple` | `list` |
| 요소 추가 | 불가 | 가능 |
| Boolean 평가 | `False` | `False` |
| 길이 | `0` | `0` |

```python
print(len(empty_tuple))
print(bool(empty_tuple))
```

출력:

```text
0
False
```

---

# 13. `tuple()` 생성자

`tuple()`은 반복 가능한 객체를 튜플로 변환합니다.

```python
numbers = tuple([1, 2, 3])

print(numbers)
```

출력:

```text
(1, 2, 3)
```

문자열을 전달하면 각 문자가 요소가 됩니다.

```python
letters = tuple("ABC")

print(letters)
```

출력:

```text
('A', 'B', 'C')
```

`range()`도 튜플로 변환할 수 있습니다.

```python
numbers = tuple(range(5))

print(numbers)
```

출력:

```text
(0, 1, 2, 3, 4)
```

---

# 14. `tuple()`에 단일 정수 전달

다음 코드는 실행할 수 없습니다.

```python
tuple(3)
```

오류:

```text
TypeError: 'int' object is not iterable
```

`tuple()`은 반복 가능한 객체를 요구합니다.

정수 하나를 가진 튜플이 필요하면 다음처럼 작성합니다.

```python
single = (3,)
```

---

# 15. 리스트를 튜플로 변환

내 코드:

```python
e = [1, 2, 3]

print(tuple(e))
```

출력:

```text
(1, 2, 3)
```

`tuple()`은 리스트 요소를 같은 순서로 가진 새 튜플을 만듭니다.

```python
numbers_list = [1, 2, 3]
numbers_tuple = tuple(numbers_list)
```

자료형 비교:

```python
print(type(numbers_list))
print(type(numbers_tuple))
```

출력:

```text
<class 'list'>
<class 'tuple'>
```

---

# 16. 튜플을 리스트로 변환

내 코드:

```python
f = (1, 2, 3)

print(list(f))
```

출력:

```text
[1, 2, 3]
```

`list()`는 튜플 요소를 같은 순서로 가진 새 리스트를 만듭니다.

```python
numbers_tuple = (1, 2, 3)
numbers_list = list(numbers_tuple)
```

튜플 요소를 수정해야 한다면 리스트로 변환한 뒤 수정할 수 있습니다.

```python
numbers = (1, 2, 3)

converted = list(numbers)
converted[1] = 200

numbers = tuple(converted)

print(numbers)
```

출력:

```text
(1, 200, 3)
```

이 과정은 기존 튜플을 수정한 것이 아니라 새로운 객체들을 만들어 다시 대입한 것입니다.

---

# 17. 튜플의 인덱싱

튜플도 리스트처럼 인덱스를 사용합니다.

```python
numbers = (10, 20, 30)

print(numbers[0])
print(numbers[1])
print(numbers[2])
```

출력:

```text
10
20
30
```

첫 번째 요소의 인덱스는 `0`입니다.

---

# 18. 음수 인덱스

```python
numbers = (10, 20, 30)

print(numbers[-1])
print(numbers[-2])
```

출력:

```text
30
20
```

| 인덱스 | 위치 |
| ---: | --- |
| `-1` | 마지막 요소 |
| `-2` | 뒤에서 두 번째 요소 |
| `-3` | 뒤에서 세 번째 요소 |

---

# 19. 존재하지 않는 인덱스

```python
numbers = (10, 20, 30)

print(numbers[3])
```

오류:

```text
IndexError: tuple index out of range
```

길이가 3이면 사용할 수 있는 양수 인덱스는 `0`, `1`, `2`입니다.

---

# 20. 튜플 슬라이싱

튜플도 시퀀스이므로 슬라이싱을 지원합니다.

```python
numbers = (0, 1, 2, 3, 4, 5)

print(numbers[1:4])
```

출력:

```text
(1, 2, 3)
```

슬라이싱 결과도 튜플입니다.

```python
print(type(numbers[1:4]))
```

출력:

```text
<class 'tuple'>
```

---

# 21. 튜플 역순 슬라이싱

```python
numbers = (1, 2, 3, 4)

print(numbers[::-1])
```

출력:

```text
(4, 3, 2, 1)
```

기존 튜플을 수정하는 것이 아니라 역순의 새 튜플을 만듭니다.

---

# 22. 튜플의 불변성

튜플은 불변 자료형입니다.

```python
numbers = (10, 20, 30)
numbers[1] = 200
```

오류:

```text
TypeError: 'tuple' object does not support item assignment
```

튜플이 만들어진 뒤에는 다음 작업을 직접 수행할 수 없습니다.

- 특정 인덱스의 요소 교체
- `append()`로 요소 추가
- `remove()`로 요소 삭제
- 슬라이싱 대입
- `sort()`로 원본 정렬
- `reverse()`로 원본 순서 반전

---

# 23. 튜플에는 `append()`가 없다

```python
numbers = (1, 2, 3)
numbers.append(4)
```

오류:

```text
AttributeError: 'tuple' object has no attribute 'append'
```

튜플은 길이를 변경하는 리스트 메서드를 제공하지 않습니다.

새 요소를 포함한 튜플이 필요하다면 새로운 튜플을 만들어야 합니다.

```python
numbers = numbers + (4,)
```

결과:

```text
(1, 2, 3, 4)
```

---

# 24. 튜플 연결

튜플끼리는 `+`로 연결할 수 있습니다.

```python
left = (1, 2)
right = (3, 4)

result = left + right

print(result)
```

출력:

```text
(1, 2, 3, 4)
```

기존 튜플을 변경하는 것이 아니라 새로운 튜플을 생성합니다.

---

# 25. 튜플과 리스트를 직접 연결할 수 없다

```python
(1, 2) + [3, 4]
```

오류:

```text
TypeError: can only concatenate tuple (not "list") to tuple
```

자료형을 맞춰야 합니다.

```python
result = (1, 2) + tuple([3, 4])
```

---

# 26. 튜플 반복

튜플에 정수를 곱하면 요소가 반복된 새 튜플이 만들어집니다.

```python
values = ("A", "B") * 3

print(values)
```

출력:

```text
('A', 'B', 'A', 'B', 'A', 'B')
```

원본은 변경되지 않습니다.

---

# 27. 튜플에 값이 포함되어 있는지 확인

```python
numbers = (10, 20, 30)

print(20 in numbers)
print(100 in numbers)
print(100 not in numbers)
```

출력:

```text
True
False
True
```

`in`과 `not in`은 튜플에서도 사용할 수 있습니다.

---

# 28. 튜플 길이

```python
numbers = (10, 20, 30)

print(len(numbers))
```

출력:

```text
3
```

한 요소 튜플의 길이는 1입니다.

```python
print(len((3,)))
```

출력:

```text
1
```

---

# 29. 튜플의 `count()`

튜플은 값의 등장 횟수를 확인하는 `count()`를 제공합니다.

```python
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
```

출력:

```text
3
```

값이 없으면 `0`을 반환합니다.

```python
print(numbers.count(100))
```

출력:

```text
0
```

---

# 30. 튜플의 `index()`

`index()`는 값이 처음 등장하는 위치를 반환합니다.

```python
numbers = (10, 20, 30, 20)

print(numbers.index(20))
```

출력:

```text
1
```

같은 값이 여러 개 있어도 첫 번째 인덱스를 반환합니다.

---

# 31. 존재하지 않는 값과 `index()`

```python
numbers = (10, 20, 30)

print(numbers.index(100))
```

오류:

```text
ValueError: tuple.index(x): x not in tuple
```

안전하게 사용하려면 먼저 포함 여부를 확인할 수 있습니다.

```python
target = 100

if target in numbers:
    print(numbers.index(target))
```

---

# 32. 튜플 메서드가 적은 이유

리스트는 내용을 변경하기 위한 여러 메서드를 제공합니다.

```text
append()
extend()
insert()
remove()
pop()
clear()
sort()
reverse()
```

튜플은 불변이므로 이러한 변경 메서드가 필요하지 않습니다.

튜플에서 대표적으로 사용하는 메서드는 다음 두 가지입니다.

```text
count()
index()
```

그 밖의 공통 기능은 내장 함수와 연산자로 사용합니다.

```python
len(values)
value in values
min(values)
max(values)
sum(values)
sorted(values)
```

---

# 33. `sorted()`와 튜플

`sorted()`는 튜플을 정렬할 수 있지만 결과는 리스트입니다.

```python
numbers = (3, 1, 2)

result = sorted(numbers)

print(result)
print(type(result))
```

출력:

```text
[1, 2, 3]
<class 'list'>
```

정렬된 튜플이 필요하다면 다시 변환합니다.

```python
result = tuple(sorted(numbers))
```

---

# 34. 튜플 패킹

여러 값을 하나의 튜플로 묶는 것을 튜플 패킹(tuple packing)이라고 합니다.

```python
point = 10, 20
```

다음 값들이 하나의 튜플에 묶입니다.

```text
10
20
```

결과:

```text
(10, 20)
```

공통 원본의 다음 코드가 패킹 예입니다.

```python
b = 1, 2, 3
```

---

# 35. 튜플 언패킹

튜플의 요소를 여러 변수에 나누어 대입하는 것을 언패킹이라고 합니다.

```python
point = (10, 20)

x, y = point

print(x)
print(y)
```

출력:

```text
10
20
```

왼쪽 변수 개수와 오른쪽 요소 개수가 같아야 합니다.

---

# 36. 패킹과 언패킹을 한 줄에서 사용

```python
name, age, active = "근욱", 30, True
```

오른쪽에서는 튜플 패킹이 일어나고, 왼쪽에서는 언패킹이 일어납니다.

결과적으로 각 변수에 하나씩 값이 들어갑니다.

```python
print(name)
print(age)
print(active)
```

---

# 37. 언패킹 개수 불일치

```python
a, b = (1, 2, 3)
```

오류:

```text
ValueError: too many values to unpack
```

반대의 경우:

```python
a, b, c = (1, 2)
```

오류:

```text
ValueError: not enough values to unpack
```

요소 개수와 변수 개수를 맞춰야 합니다.

---

# 38. 별표 언패킹

나머지 요소를 리스트로 받을 수 있습니다.

```python
first, *rest = (10, 20, 30, 40)

print(first)
print(rest)
```

출력:

```text
10
[20, 30, 40]
```

별표 변수에는 튜플이 아니라 리스트가 저장됩니다.

---

# 39. 앞과 뒤 요소 분리

```python
first, *middle, last = (10, 20, 30, 40, 50)

print(first)
print(middle)
print(last)
```

출력:

```text
10
[20, 30, 40]
50
```

하나의 언패킹 표현식에서 별표 변수는 하나만 사용할 수 있습니다.

---

# 40. 변수 교환과 튜플

Python에서는 임시 변수를 직접 만들지 않고 값을 교환할 수 있습니다.

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

출력:

```text
20 10
```

오른쪽 값이 먼저 패킹되고 왼쪽 변수에 언패킹되는 방식으로 이해할 수 있습니다.

---

# 41. 함수가 여러 값을 반환하는 것처럼 보이는 이유

```python
def get_position():
    return 10, 20
```

호출:

```python
result = get_position()

print(result)
print(type(result))
```

출력:

```text
(10, 20)
<class 'tuple'>
```

Python 함수는 실제로 튜플 하나를 반환합니다.

언패킹하면 여러 값을 각각 받은 것처럼 사용할 수 있습니다.

```python
x, y = get_position()
```

---

# 42. `divmod()`와 튜플

Python 내장 함수 `divmod()`는 몫과 나머지를 튜플로 반환합니다.

```python
result = divmod(17, 5)

print(result)
```

출력:

```text
(3, 2)
```

언패킹:

```python
quotient, remainder = divmod(17, 5)
```

---

# 43. `enumerate()`가 제공하는 값

다음 반복문에서:

```python
names = ["민수", "영희"]

for item in enumerate(names):
    print(item, type(item))
```

각 반복 결과는 튜플입니다.

```text
(0, '민수') <class 'tuple'>
(1, '영희') <class 'tuple'>
```

보통 다음처럼 바로 언패킹합니다.

```python
for index, name in enumerate(names):
    print(index, name)
```

---

# 44. 딕셔너리의 `items()`와 튜플

딕셔너리의 `items()`를 순회하면 키와 값이 튜플 형태로 제공됩니다.

```python
user = {
    "name": "근욱",
    "age": 30,
}

for item in user.items():
    print(item)
```

출력:

```text
('name', '근욱')
('age', 30)
```

보통 다음처럼 언패킹합니다.

```python
for key, value in user.items():
    print(key, value)
```

이 내용은 이후 딕셔너리 문서와 연결됩니다.

---

# 45. 튜플 안에 리스트 저장

튜플은 서로 다른 자료형을 저장할 수 있습니다.

```python
data = (1, [10, 20], "Python")
```

튜플 자체의 요소 위치는 바꿀 수 없습니다.

```python
data[1] = [100, 200]
```

오류:

```text
TypeError: 'tuple' object does not support item assignment
```

---

# 46. 튜플 안의 리스트는 변경할 수 있다

다음 코드는 실행됩니다.

```python
data = (1, [10, 20], "Python")

data[1].append(30)

print(data)
```

출력:

```text
(1, [10, 20, 30], 'Python')
```

튜플의 두 번째 요소가 다른 객체를 참조하도록 교체된 것은 아닙니다.

기존에 참조하던 리스트 객체의 내부 내용이 변경된 것입니다.

---

# 47. 튜플의 불변성은 얕은 개념이다

튜플의 불변성은 다음을 의미합니다.

```text
튜플 내부의 요소 참조를 직접 교체할 수 없다.
```

다음 의미는 아닙니다.

```text
튜플 안에 들어 있는 모든 객체가 반드시 불변이다.
```

예:

```python
data = ([1, 2],)
```

튜플 요소 자체는 같은 리스트 객체를 계속 참조하지만 그 리스트는 변경 가능합니다.

---

# 48. 중첩 튜플

튜플 안에 튜플을 저장할 수 있습니다.

```python
matrix = (
    (10, 20),
    (30, 40),
)
```

접근:

```python
print(matrix[1][0])
```

출력:

```text
30
```

중첩 튜플의 모든 요소가 불변 객체라면 전체 구조를 고정된 값 묶음으로 사용하기 좋습니다.

---

# 49. 튜플과 객체 동일성

```python
a = (1, 2, 3)
b = tuple(a)

print(a == b)
print(a is b)
```

`tuple()`에 이미 튜플을 전달하면 Python 구현에서 같은 객체가 반환될 수 있습니다.

따라서 객체 동일성을 확인하려는 목적으로 특정 결과를 가정해서는 안 됩니다.

값 비교가 목적이면 `==`를 사용합니다.

```python
print(a == b)
```

---

# 50. `==`와 `is`

| 연산자 | 의미 |
| --- | --- |
| `==` | 두 객체의 값이 같은지 비교 |
| `is` | 두 변수가 정확히 같은 객체를 참조하는지 비교 |

튜플의 내용 비교는 일반적으로 `==`를 사용합니다.

```python
a = (1, 2, 3)
b = (1, 2, 3)

print(a == b)
```

출력:

```text
True
```

객체 동일성은 구현과 최적화의 영향을 받을 수 있으므로 값 비교에 `is`를 사용하면 안 됩니다.

---

# 51. 튜플과 해시 가능성

딕셔너리 키와 집합 요소는 해시 가능한 객체여야 합니다.

튜플은 내부 요소가 모두 해시 가능하면 자신도 해시 가능합니다.

```python
point = (10, 20)

data = {
    point: "좌표",
}

print(data[(10, 20)])
```

출력:

```text
좌표
```

이 때문에 좌표나 복합 키를 표현할 때 튜플을 사용할 수 있습니다.

---

# 52. 리스트를 포함한 튜플은 해시할 수 없다

```python
key = ([1, 2], 3)

data = {
    key: "값",
}
```

오류:

```text
TypeError: unhashable type: 'list'
```

튜플 바깥이 불변이어도 내부에 해시 불가능한 리스트가 들어 있으면 전체 튜플도 딕셔너리 키로 사용할 수 없습니다.

---

# 53. 튜플을 집합 요소로 사용

```python
points = {
    (0, 0),
    (10, 20),
    (0, 0),
}

print(points)
```

중복 튜플은 집합에서 하나로 처리됩니다.

단, 각 튜플 내부 요소가 모두 해시 가능해야 합니다.

---

# 54. 튜플을 사용하는 대표 상황

튜플은 다음과 같은 상황에 적합합니다.

- 좌표처럼 값의 개수와 의미가 고정된 데이터
- 함수에서 여러 결과를 묶어 반환
- 언패킹을 위한 임시 값 묶음
- 딕셔너리의 복합 키
- 변경되면 안 되는 설정값
- 여러 레코드를 순회할 때 한 행의 값 묶음
- `enumerate()`가 제공하는 인덱스와 값
- 딕셔너리 `items()`가 제공하는 키와 값

---

# 55. 리스트가 더 적합한 상황

다음과 같은 경우에는 리스트가 더 자연스럽습니다.

- 요소를 계속 추가해야 하는 경우
- 요소를 삭제해야 하는 경우
- 정렬 상태를 원본에서 바꿔야 하는 경우
- 사용자 입력에 따라 길이가 계속 달라지는 경우
- 장바구니처럼 내용이 자주 변하는 경우
- 작업 목록처럼 상태에 따라 변경되는 경우

자료형은 단순히 성능이 아니라 데이터의 의미와 변경 여부를 기준으로 선택합니다.

---

# 56. 소괄호가 필요한 대표 상황

튜플 패킹에서 괄호는 생략할 수 있지만 다음 상황에서는 괄호를 쓰는 편이 명확하거나 필요합니다.

함수 인자로 튜플 하나 전달:

```python
def print_value(value):
    print(value)

print_value((1, 2))
```

한 요소 튜플:

```python
single = (1,)
```

여러 줄 튜플:

```python
config = (
    "localhost",
    3306,
    "database",
)
```

중첩 구조:

```python
points = (
    (0, 0),
    (10, 20),
)
```

---

# 57. 함수 인자에서 쉼표의 의미

```python
print((1, 2))
```

이 코드는 튜플 하나를 `print()`에 전달합니다.

반면:

```python
print(1, 2)
```

이 코드는 두 개의 인자를 `print()`에 전달합니다.

출력은 비슷해 보일 수 있지만 함수가 받는 인자 구조가 다릅니다.

---

# 58. 반환문에서 괄호 생략

```python
def get_user():
    return "근욱", 30
```

다음 코드와 같은 튜플을 반환합니다.

```python
def get_user():
    return ("근욱", 30)
```

괄호 생략이 가능하더라도 여러 줄이거나 구조가 복잡하면 괄호를 사용하는 편이 읽기 좋습니다.

---

# 59. 튜플 순회

튜플도 반복 가능한 객체입니다.

```python
numbers = (10, 20, 30)

for number in numbers:
    print(number)
```

출력:

```text
10
20
30
```

리스트 순회와 동일한 방식으로 값을 읽을 수 있습니다.

---

# 60. `enumerate()`와 튜플 순회

```python
names = ("민수", "영희", "철수")

for index, name in enumerate(names):
    print(index, name)
```

출력:

```text
0 민수
1 영희
2 철수
```

튜플은 수정할 수 없지만 번호와 값을 읽는 순회는 가능합니다.

---

# 61. 튜플 컴프리헨션은 없다

다음 표현은 튜플 컴프리헨션이 아닙니다.

```python
result = (i for i in range(5))
```

자료형 확인:

```python
print(type(result))
```

출력:

```text
<class 'generator'>
```

튜플이 필요하면 `tuple()`로 변환합니다.

```python
result = tuple(i for i in range(5))
```

또는 간단히:

```python
result = tuple(range(5))
```

---

# 62. 리스트 컴프리헨션과 튜플 생성 비교

리스트 컴프리헨션:

```python
numbers = [i * 2 for i in range(5)]
```

튜플 생성:

```python
numbers = tuple(i * 2 for i in range(5))
```

출력:

```text
(0, 2, 4, 6, 8)
```

소괄호 안의 표현은 제너레이터 표현식이고 `tuple()`이 결과를 소비합니다.

---

# 63. 튜플 정렬 결과를 튜플로 유지

```python
numbers = (5, 2, 4, 1, 3)

sorted_numbers = tuple(sorted(numbers))

print(sorted_numbers)
```

출력:

```text
(1, 2, 3, 4, 5)
```

원본 `numbers`는 변경되지 않습니다.

---

# 64. 튜플을 수정하는 것처럼 보이는 재대입

```python
numbers = (1, 2, 3)
numbers = numbers + (4,)
```

최종 결과:

```text
(1, 2, 3, 4)
```

이 코드는 기존 튜플에 요소를 추가한 것이 아닙니다.

처리 과정:

```text
기존 튜플 (1, 2, 3)
+ 새 튜플 (4,)
→ 새로운 튜플 (1, 2, 3, 4)
→ 변수 numbers가 새 튜플을 참조
```

---

# 65. 튜플 안 리스트에 `+=`를 사용할 때 주의

```python
data = ([1, 2],)
```

다음 표현은 예상하기 어려운 동작과 오류를 만들 수 있습니다.

```python
data[0] += [3]
```

리스트의 내부 변경이 먼저 일어난 뒤 튜플 요소에 다시 대입하려는 과정에서 `TypeError`가 발생할 수 있습니다.

따라서 튜플 안의 변경 가능한 객체를 수정할 때는 의도를 명확히 작성합니다.

```python
data[0].append(3)
```

하지만 고정된 구조를 기대한다면 애초에 내부에도 불변 객체를 사용하는 편이 안전합니다.

---

# 66. 튜플과 메모리·성능

일반적으로 튜플은 같은 요소를 가진 리스트보다 구조가 단순하고 변경 기능이 적어 메모리 사용이 작거나 순회가 약간 빠를 수 있습니다.

그러나 자료형 선택의 가장 중요한 기준은 다음과 같습니다.

```text
이 데이터가 변경되어야 하는가?
고정된 값의 묶음이라는 의미를 전달해야 하는가?
```

아주 작은 성능 차이만 보고 모든 리스트를 튜플로 바꾸는 것은 적절하지 않습니다.

---

# 67. 튜플은 완전한 상수가 아니다

튜플 변수 자체는 다른 객체로 다시 대입할 수 있습니다.

```python
numbers = (1, 2, 3)
numbers = (10, 20)
```

이것은 허용됩니다.

불변이라는 말은 변수 이름을 다시 사용할 수 없다는 뜻이 아닙니다.

```text
튜플 객체 내부의 요소 참조를 바꿀 수 없다.
```

변수가 다른 튜플을 참조하게 만드는 재대입은 가능합니다.

---

# 68. 튜플과 상수 관례

Python에는 일반 변수의 재대입을 강제로 막는 문법이 없습니다.

상수처럼 사용하려는 값은 관례적으로 대문자 이름을 사용합니다.

```python
RGB_RED = (255, 0, 0)
DEFAULT_POSITION = (0, 0)
```

튜플을 사용하면 내부 요소 변경은 막을 수 있지만 변수 전체의 재대입까지 언어가 막아 주는 것은 아닙니다.

---

# 69. 명명 튜플과 데이터 클래스

일반 튜플은 인덱스로 접근합니다.

```python
user = ("근욱", 30)

print(user[0])
print(user[1])
```

요소 의미가 많아지면 인덱스만으로 이해하기 어려울 수 있습니다.

이후 학습에서는 다음 대안을 만날 수 있습니다.

- `collections.namedtuple`
- `typing.NamedTuple`
- `dataclasses.dataclass`

예:

```python
from typing import NamedTuple

class User(NamedTuple):
    name: str
    age: int

user = User("근욱", 30)

print(user.name)
print(user.age)
```

이 내용은 튜플의 실무 확장 개념이며 원본에는 직접 등장하지 않습니다.

---

# 70. 내 코드와 강사님 코드 공통점

두 코드 모두 다음 내용을 다룹니다.

- `(1, 2, 3)` 형태의 튜플 선언
- `type()`으로 `tuple` 자료형 확인
- 괄호 없이 `1, 2, 3`으로 튜플 선언
- 한 요소 튜플에 쉼표 사용
- 괄호 없는 한 요소 튜플
- 튜플의 기본 출력 형식

---

# 71. 내 코드와 강사님 코드 차이

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 튜플 설명 | `readonly list`라고 표현 | 선언 중심 |
| 빈 튜플 설명 | 빈 튜플 선언이 불가능하다고 주석 | 관련 설명 없음 |
| 불변성 설명 | 값 변경 불가 주석 | 관련 설명 없음 |
| `c` 출력 | `(3,)`과 자료형 출력 | 선언만 하고 출력하지 않음 |
| 리스트 → 튜플 | `tuple(e)` 예제 있음 | 없음 |
| 튜플 → 리스트 | `list(f)` 예제 있음 | 없음 |
| 주석 양 | 개념 설명이 더 많음 | 최소한의 수업 메모 |
| 코드 범위 | 변환까지 확장 | 튜플 선언에 집중 |

---

# 72. 내 코드의 장점

- 튜플을 처음 접할 때 리스트와 비교해 이해하려는 시도가 있습니다.
- 괄호를 생략해도 튜플을 만들 수 있음을 확인합니다.
- 한 요소 튜플에 쉼표가 필요하다는 핵심 문법을 정확히 기록했습니다.
- `(3,)`과 `4,` 두 형태를 모두 출력해 확인합니다.
- 리스트를 튜플로, 튜플을 리스트로 변환하는 예제를 추가했습니다.
- 각 결과에 `type()`을 함께 출력해 자료형을 눈으로 확인할 수 있습니다.

---

# 73. 내 코드의 개선점

- 빈 튜플은 `()`로 정상적으로 만들 수 있으므로 “빈 것으로 선언 불가”라는 주석을 수정해야 합니다.
- 튜플을 `readonly list`라고만 표현하면 튜플 자체의 의미와 해시 가능성 같은 차이를 놓칠 수 있습니다.
- “값은 바꾸지 못함”을 튜플 안의 모든 객체가 절대 변경되지 않는다는 뜻으로 오해할 수 있습니다.
- 변수 이름 `a`, `b`, `c`, `d`, `e`, `f`만으로는 각 예제의 목적을 파악하기 어렵습니다.
- PEP 8에 맞게 쉼표 뒤에 공백을 넣으면 읽기 좋습니다.
- 변환 결과의 자료형도 함께 출력하면 리스트·튜플 변환을 더 분명하게 확인할 수 있습니다.
- 불변성 오류를 주석 처리한 예제로 보여 주면 리스트와의 차이가 더 명확해집니다.
- `tuple()`이 반복 가능한 객체를 받는다는 설명이 없습니다.

---

# 74. 강사님 코드의 장점

- 튜플 선언의 핵심 형태를 매우 간결하게 보여 줍니다.
- 괄호가 없어도 튜플이 된다는 점을 코드로 확인합니다.
- 한 요소 튜플에서 쉼표가 필요하다는 핵심을 포함합니다.
- 복잡한 확장 내용 없이 튜플 선언 문법에 집중합니다.

---

# 75. 강사님 코드의 개선점

- `c = (3,)`를 선언하지만 출력하지 않아 결과 확인이 빠져 있습니다.
- 튜플의 불변성에 대한 실행 예제가 없습니다.
- 빈 튜플 선언을 다루지 않습니다.
- 리스트와 튜플의 변환을 다루지 않습니다.
- 인덱싱과 슬라이싱을 다루지 않습니다.
- 패킹과 언패킹이라는 용어를 설명하지 않습니다.
- 튜플의 `count()`와 `index()`를 다루지 않습니다.
- 변수 이름이 모두 한 글자라 학습 목적이 코드에 드러나지 않습니다.

---

# 76. 정확하게 수정한 원본 주석

기존 주석:

```python
# 선언 (readonly list)
# a = () 처럼 빈 것으로 선언 불가하며, 값은 바꾸지 못 함
```

개선:

```python
# 튜플은 순서를 가진 불변 시퀀스 자료형이다.
# 빈 튜플은 () 또는 tuple()로 만들 수 있다.
# 튜플 요소의 참조는 직접 변경할 수 없다.
```

기존 주석:

```python
# tuple은 ()없이도 선언해서 사용할 수 있음
```

개선:

```python
# 튜플을 만드는 핵심 문법은 쉼표이므로,
# 여러 요소 튜플에서는 소괄호를 생략할 수 있다.
```

기존 주석:

```python
# 값이 1개인 tuple을 선언하기 위해서는 ','를 써줘야 함
```

개선:

```python
# 한 요소 튜플은 값 뒤에 쉼표가 반드시 필요하다.
```

---

# 77. 개선된 대표 코드

```python
empty_tuple = ()

numbers = (1, 2, 3)
packed_numbers = 1, 2, 3
single_number = (3,)

print(empty_tuple, type(empty_tuple))
print(numbers, type(numbers))
print(packed_numbers, type(packed_numbers))
print(single_number, type(single_number))

numbers_list = list(numbers)
numbers_tuple = tuple(numbers_list)

print(numbers_list, type(numbers_list))
print(numbers_tuple, type(numbers_tuple))
```

---

# 78. 불변성 확인 예제

```python
numbers = (10, 20, 30)

print(numbers[0])
print(numbers[1:])
print(len(numbers))

# numbers[0] = 100
# TypeError:
# 'tuple' object does not support item assignment
```

오류가 발생하는 코드는 주석 처리해 학습 파일 전체가 중단되지 않도록 할 수 있습니다.

---

# 79. 패킹과 언패킹 대표 예제

```python
user = "근욱", 30, True

name, age, active = user

print(name)
print(age)
print(active)
```

출력:

```text
근욱
30
True
```

---

# 80. 실무 활용 예제: 좌표

```python
position = (120, 350)

x, y = position

print(f"x: {x}")
print(f"y: {y}")
```

좌표는 요소 개수와 의미가 고정되어 있어 튜플로 표현하기 좋습니다.

---

# 81. 실무 활용 예제: RGB 색상

```python
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

red, green, blue = RED

print(red, green, blue)
```

색상 채널 값처럼 구조가 고정된 데이터에 사용할 수 있습니다.

---

# 82. 실무 활용 예제: 함수 반환값

```python
def calculate(number1, number2):
    total = number1 + number2
    difference = number1 - number2

    return total, difference

total, difference = calculate(10, 3)

print(total)
print(difference)
```

함수는 `(13, 7)`이라는 튜플 하나를 반환하고 호출부에서 언패킹합니다.

---

# 83. 실무 활용 예제: 딕셔너리 복합 키

```python
seat_status = {
    (1, 1): "예약",
    (1, 2): "가능",
    (2, 1): "가능",
}

print(seat_status[(1, 1)])
```

행과 열 좌표를 하나의 튜플로 묶어 키로 사용했습니다.

---

# 84. 실무 활용 예제: 데이터 행 순회

```python
users = [
    ("민수", 90),
    ("영희", 85),
    ("철수", 92),
]

for name, score in users:
    print(f"{name}: {score}점")
```

리스트는 여러 행을 저장하고 각 행은 고정된 두 값을 가진 튜플로 표현합니다.

---

# 85. 자주 하는 실수: 한 요소 튜플의 쉼표 누락

잘못된 예:

```python
value = (3)
```

자료형:

```text
int
```

개선:

```python
value = (3,)
```

자료형:

```text
tuple
```

---

# 86. 자주 하는 실수: 빈 튜플을 만들 수 없다고 생각하기

빈 튜플은 다음 두 방식으로 만들 수 있습니다.

```python
a = ()
b = tuple()
```

둘 다 정상적인 튜플입니다.

---

# 87. 자주 하는 실수: 튜플 요소 수정

```python
numbers = (1, 2, 3)
numbers[0] = 100
```

오류:

```text
TypeError: 'tuple' object does not support item assignment
```

새 튜플을 만들어 변수에 다시 대입해야 합니다.

---

# 88. 자주 하는 실수: 튜플에 `append()` 사용

```python
numbers = (1, 2, 3)
numbers.append(4)
```

오류:

```text
AttributeError
```

계속 변경해야 하는 데이터라면 리스트가 더 적합합니다.

---

# 89. 자주 하는 실수: `tuple(3)`

```python
value = tuple(3)
```

정수는 반복 가능한 객체가 아니므로 `TypeError`가 발생합니다.

한 요소 튜플:

```python
value = (3,)
```

---

# 90. 자주 하는 실수: 튜플과 리스트 직접 연결

```python
result = (1, 2) + [3, 4]
```

두 피연산자의 자료형이 달라 `TypeError`가 발생합니다.

```python
result = (1, 2) + tuple([3, 4])
```

---

# 91. 자주 하는 실수: 괄호가 튜플을 만든다고만 생각하기

```python
value = (10)
```

이 값은 정수입니다.

```python
value = 10,
```

이 값은 튜플입니다.

핵심은 쉼표입니다.

---

# 92. 자주 하는 실수: 튜플 내부 객체도 모두 불변이라고 생각하기

```python
data = ([1, 2],)
data[0].append(3)
```

튜플 요소가 참조하는 리스트 자체는 변경 가능합니다.

고정된 전체 구조가 필요하면 내부에도 불변 객체를 사용해야 합니다.

---

# 93. 자주 하는 실수: 튜플 컴프리헨션

```python
result = (i for i in range(5))
```

이 결과는 튜플이 아니라 제너레이터입니다.

튜플 변환:

```python
result = tuple(i for i in range(5))
```

---

# 94. 자주 하는 실수: 언패킹 개수 불일치

```python
x, y = (10, 20, 30)
```

오류:

```text
ValueError: too many values to unpack
```

요소 개수를 맞추거나 별표 언패킹을 사용합니다.

```python
x, *rest = (10, 20, 30)
```

---

# 95. 면접·복습 질문 1

## 튜플이란 무엇인가?

튜플은 순서를 유지하고 인덱스를 사용하는 불변 시퀀스 자료형입니다. 중복 값을 허용하며 여러 자료형의 객체를 저장할 수 있습니다.

---

# 96. 면접·복습 질문 2

## 튜플을 만드는 핵심 문법은 무엇인가?

소괄호보다 쉼표가 핵심입니다. `1, 2, 3`은 튜플이며 한 요소 튜플은 `(1,)`처럼 반드시 쉼표를 포함해야 합니다.

---

# 97. 면접·복습 질문 3

## 빈 튜플을 만들 수 있는가?

가능합니다.

```python
empty1 = ()
empty2 = tuple()
```

---

# 98. 면접·복습 질문 4

## `(3)`과 `(3,)`의 차이는 무엇인가?

`(3)`은 정수 `3`을 괄호로 묶은 표현식이고, `(3,)`은 한 요소 튜플입니다.

---

# 99. 면접·복습 질문 5

## 리스트와 튜플의 가장 큰 차이는 무엇인가?

리스트는 요소를 추가·수정·삭제할 수 있는 변경 가능한 자료형이고, 튜플은 요소 참조를 직접 변경할 수 없는 불변 자료형입니다.

---

# 100. 면접·복습 질문 6

## 튜플 안의 리스트는 변경할 수 있는가?

튜플 요소가 참조하는 리스트 객체의 내부는 변경할 수 있습니다. 튜플의 불변성은 요소 참조의 직접 교체를 막는 것이며 내부 객체까지 모두 불변으로 만드는 것은 아닙니다.

---

# 101. 면접·복습 질문 7

## 튜플 패킹과 언패킹은 무엇인가?

여러 값을 튜플 하나로 묶는 것을 패킹이라 하고, 튜플 요소를 여러 변수에 나누어 대입하는 것을 언패킹이라고 합니다.

---

# 102. 면접·복습 질문 8

## 함수에서 여러 값을 반환하면 실제 자료형은 무엇인가?

쉼표로 여러 값을 반환하면 하나의 튜플로 패킹되어 반환됩니다. 호출부에서는 이를 언패킹할 수 있습니다.

---

# 103. 면접·복습 질문 9

## 튜플은 언제 딕셔너리 키로 사용할 수 있는가?

튜플 내부의 모든 요소가 해시 가능할 때 딕셔너리 키로 사용할 수 있습니다. 리스트처럼 해시 불가능한 객체를 포함하면 사용할 수 없습니다.

---

# 104. 면접·복습 질문 10

## `(i for i in range(5))`는 튜플인가?

아닙니다. 제너레이터 표현식입니다. 튜플이 필요하면 `tuple(i for i in range(5))`로 변환합니다.

---

# 105. Problems

## 문제 1

빈 튜플을 두 가지 방법으로 선언하세요.

---

## 문제 2

다음 값을 가진 튜플을 소괄호를 사용해 선언하세요.

```text
10, 20, 30
```

---

## 문제 3

소괄호 없이 `1`, `2`, `3`을 가진 튜플을 선언하세요.

---

## 문제 4

문자열 `"Python"` 하나만 가진 튜플을 선언하세요.

---

## 문제 5

다음 두 변수의 자료형을 출력하고 차이를 설명하세요.

```python
a = (3)
b = (3,)
```

---

## 문제 6

다음 튜플의 첫 번째 요소를 출력하세요.

```python
numbers = (10, 20, 30)
```

---

## 문제 7

다음 튜플의 마지막 요소를 음수 인덱스로 출력하세요.

```python
numbers = (10, 20, 30)
```

---

## 문제 8

다음 튜플에서 인덱스 1부터 4 바로 앞까지 슬라이싱하세요.

```python
numbers = (0, 1, 2, 3, 4, 5)
```

---

## 문제 9

다음 튜플에 값 `4`를 포함한 새 튜플을 만들어 다시 `numbers`에 대입하세요.

```python
numbers = (1, 2, 3)
```

---

## 문제 10

다음 리스트를 튜플로 변환하세요.

```python
numbers = [1, 2, 3]
```

---

## 문제 11

다음 튜플을 리스트로 변환하세요.

```python
numbers = (1, 2, 3)
```

---

## 문제 12

다음 튜플에서 값 `2`가 등장하는 횟수를 출력하세요.

```python
numbers = (1, 2, 2, 3, 2)
```

---

## 문제 13

다음 튜플에서 값 `30`의 첫 번째 인덱스를 출력하세요.

```python
numbers = (10, 20, 30, 20)
```

---

## 문제 14

다음 튜플을 `name`, `age` 변수로 언패킹하세요.

```python
user = ("근욱", 30)
```

---

## 문제 15

다음 튜플에서 첫 번째 값은 `first`, 마지막 값은 `last`, 중간 값들은 `middle`에 저장하세요.

```python
numbers = (10, 20, 30, 40, 50)
```

---

## 문제 16

두 변수의 값을 튜플 패킹과 언패킹을 이용해 교환하세요.

```python
a = 10
b = 20
```

---

## 문제 17

이름과 점수를 튜플로 반환하는 함수를 작성하세요.

```text
이름: 민수
점수: 90
```

---

## 문제 18

다음 튜플의 각 값을 반복문으로 출력하세요.

```python
colors = ("red", "green", "blue")
```

---

## 문제 19

다음 튜플을 번호와 값으로 함께 출력하세요.

```python
colors = ("red", "green", "blue")
```

---

## 문제 20

0부터 4까지의 값을 가진 튜플을 `range()`와 `tuple()`로 만드세요.

---

## 문제 21

1부터 5까지 각 숫자의 제곱을 가진 튜플을 만드세요.

예상 결과:

```text
(1, 4, 9, 16, 25)
```

---

## 문제 22

다음 튜플을 오름차순으로 정렬한 새 튜플을 만드세요.

```python
numbers = (3, 1, 2)
```

---

## 문제 23

다음 튜플에서 `40`을 출력하세요.

```python
matrix = (
    (10, 20),
    (30, 40),
)
```

---

## 문제 24

좌표 `(10, 20)`을 딕셔너리 키로 사용하고 값 `"출발점"`을 저장하세요.

---

## 문제 25

다음 코드가 오류를 발생시키는 이유를 설명하세요.

```python
data = {
    ([1, 2], 3): "값",
}
```

---

# 106. Answers

## 정답 1

```python
a = ()
b = tuple()

print(a, type(a))
print(b, type(b))
```

---

## 정답 2

```python
numbers = (10, 20, 30)
```

---

## 정답 3

```python
numbers = 1, 2, 3
```

---

## 정답 4

```python
language = ("Python",)
```

---

## 정답 5

```python
a = (3)
b = (3,)

print(type(a))
print(type(b))
```

`a`는 정수이고 `b`는 한 요소 튜플입니다. 한 요소 튜플에는 쉼표가 필요합니다.

---

## 정답 6

```python
numbers = (10, 20, 30)

print(numbers[0])
```

---

## 정답 7

```python
numbers = (10, 20, 30)

print(numbers[-1])
```

---

## 정답 8

```python
numbers = (0, 1, 2, 3, 4, 5)

print(numbers[1:4])
```

---

## 정답 9

```python
numbers = (1, 2, 3)

numbers = numbers + (4,)

print(numbers)
```

---

## 정답 10

```python
numbers = [1, 2, 3]

converted = tuple(numbers)

print(converted)
```

---

## 정답 11

```python
numbers = (1, 2, 3)

converted = list(numbers)

print(converted)
```

---

## 정답 12

```python
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
```

---

## 정답 13

```python
numbers = (10, 20, 30, 20)

print(numbers.index(30))
```

---

## 정답 14

```python
user = ("근욱", 30)

name, age = user

print(name)
print(age)
```

---

## 정답 15

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

---

## 정답 16

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

---

## 정답 17

```python
def get_student():
    return "민수", 90

name, score = get_student()

print(name)
print(score)
```

---

## 정답 18

```python
colors = ("red", "green", "blue")

for color in colors:
    print(color)
```

---

## 정답 19

```python
colors = ("red", "green", "blue")

for index, color in enumerate(colors):
    print(index, color)
```

---

## 정답 20

```python
numbers = tuple(range(5))

print(numbers)
```

---

## 정답 21

```python
squares = tuple(
    number ** 2
    for number in range(1, 6)
)

print(squares)
```

---

## 정답 22

```python
numbers = (3, 1, 2)

sorted_numbers = tuple(sorted(numbers))

print(numbers)
print(sorted_numbers)
```

---

## 정답 23

```python
matrix = (
    (10, 20),
    (30, 40),
)

print(matrix[1][1])
```

---

## 정답 24

```python
positions = {
    (10, 20): "출발점",
}

print(positions[(10, 20)])
```

---

## 정답 25

튜플 안에 리스트가 포함되어 있습니다. 리스트는 변경 가능한 자료형이므로 해시할 수 없습니다. 내부에 해시 불가능한 객체를 가진 튜플도 딕셔너리 키로 사용할 수 없습니다.

---

# 107. Final Checklist

- [ ] 튜플이 순서를 가진 불변 시퀀스임을 설명할 수 있다.
- [ ] `(1, 2, 3)` 형태로 튜플을 선언할 수 있다.
- [ ] 괄호 없이 `1, 2, 3`으로 튜플을 선언할 수 있다.
- [ ] 튜플 생성의 핵심 문법이 쉼표임을 안다.
- [ ] `(3)`과 `(3,)`의 차이를 설명할 수 있다.
- [ ] 빈 튜플을 `()`와 `tuple()`로 만들 수 있다.
- [ ] `tuple()`이 반복 가능한 객체를 받는다는 점을 안다.
- [ ] 리스트를 튜플로 변환할 수 있다.
- [ ] 튜플을 리스트로 변환할 수 있다.
- [ ] 튜플의 요소를 인덱스로 읽을 수 있다.
- [ ] 튜플을 슬라이싱할 수 있다.
- [ ] 튜플 요소를 직접 변경할 수 없음을 안다.
- [ ] 튜플에 `append()`가 없는 이유를 설명할 수 있다.
- [ ] 튜플 연결과 반복이 새 튜플을 만든다는 점을 안다.
- [ ] `in`, `len()`, `count()`, `index()`를 사용할 수 있다.
- [ ] 튜플 패킹과 언패킹을 사용할 수 있다.
- [ ] 언패킹 변수 개수 불일치 오류를 설명할 수 있다.
- [ ] 별표 언패킹을 사용할 수 있다.
- [ ] 변수 교환에 패킹과 언패킹을 사용할 수 있다.
- [ ] 함수가 여러 값을 튜플로 반환한다는 점을 이해한다.
- [ ] `enumerate()` 결과가 튜플 형태임을 안다.
- [ ] 튜플 안의 변경 가능한 객체는 수정될 수 있음을 설명할 수 있다.
- [ ] 튜플의 불변성이 내부 모든 객체의 불변성을 보장하지 않음을 안다.
- [ ] 내부 요소가 모두 해시 가능할 때 튜플을 딕셔너리 키로 사용할 수 있음을 안다.
- [ ] `(i for i in range(...))`가 튜플이 아니라 제너레이터임을 안다.
- [ ] 정렬된 튜플이 필요할 때 `tuple(sorted(...))`을 사용할 수 있다.
- [ ] 리스트와 튜플 중 데이터 의미에 맞는 자료형을 선택할 수 있다.
- [ ] 내 코드의 빈 튜플 관련 주석이 잘못되었음을 설명할 수 있다.
- [ ] `readonly list`라는 비유의 장점과 한계를 설명할 수 있다.

---

# 108. Key Summary

```text
tuple
→ 순서를 유지하는 불변 시퀀스
→ 인덱스 사용
→ 중복 허용
→ 요소 참조를 직접 변경할 수 없음
```

```python
a = (1, 2, 3)
b = 1, 2, 3
```

두 변수 모두 튜플입니다.

```text
튜플 생성의 핵심
→ 소괄호보다 쉼표
```

한 요소 튜플:

```python
single = (3,)
```

빈 튜플:

```python
empty1 = ()
empty2 = tuple()
```

자료형 변환:

```python
tuple([1, 2, 3])
list((1, 2, 3))
```

패킹:

```python
point = 10, 20
```

언패킹:

```python
x, y = point
```

불변성:

```python
numbers = (1, 2, 3)

# numbers[0] = 100
# TypeError
```

튜플 내부에 리스트가 있다면:

```python
data = ([1, 2],)
data[0].append(3)
```

튜플의 요소 참조는 그대로지만 내부 리스트는 변경될 수 있습니다.

```text
딕셔너리 키로 사용
→ 튜플 내부의 모든 요소가 해시 가능해야 함
```

튜플은 단순히 “수정할 수 없는 리스트”가 아니라, 값의 구조와 의미가 고정되어 있음을 코드에 표현하는 자료형입니다.
