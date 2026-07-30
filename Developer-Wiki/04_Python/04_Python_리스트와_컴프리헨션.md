# Python 리스트와 컴프리헨션

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `04_Python_리스트와_컴프리헨션.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `00-01_Python_실행방식과_프로그래밍_패러다임.md`, `00-02_Python_오류와_예외.md`, `01_Python_출력과_주석.md`, `02_Python_변수와_자료형_연산자.md`, `03_Python_문자열과_포매팅.md` |
| 다음 학습 | `05_Python_튜플.md` |
| 원본 기준 | `workspace_python/04_list.py`, `workspace_teacher/workspace_python/_04_list.py` |
| 핵심 범위 | 리스트 생성, `range()`, 요소 추가·삭제, 정렬, 검색, 복사, 순회, `enumerate()`, 리스트 컴프리헨션, `map()`, 2차원 리스트 |

> 이 문서는 내 코드의 `04_list.py`와 강사님 코드의 `_04_list.py`를 직접 비교해 작성했습니다. 두 파일은 리스트 생성부터 추가·삭제·정렬·복사·반복 처리·컴프리헨션·2차원 리스트까지 다룹니다.

---

# 학습 목표

- 대괄호와 `list()`를 이용해 리스트를 생성할 수 있다.
- 리스트가 순서와 인덱스를 가지는 변경 가능한 자료형임을 설명할 수 있다.
- `range(start, stop, step)`의 동작 규칙을 이해한다.
- 인덱싱과 슬라이싱으로 리스트 요소 또는 부분 리스트에 접근할 수 있다.
- `del`, `append()`, `extend()`, `insert()`의 차이를 구분할 수 있다.
- `pop()`, `remove()`, `clear()`를 상황에 맞게 사용할 수 있다.
- `sort()`, `sorted()`, `reverse()`, `reversed()`의 차이를 설명할 수 있다.
- `index()`, `count()`, `in`을 이용해 값을 검색할 수 있다.
- 리스트 대입과 얕은 복사의 차이를 이해한다.
- `is`와 `==`로 객체 동일성과 값 동등성을 구분할 수 있다.
- `enumerate()`로 인덱스와 값을 함께 순회할 수 있다.
- 리스트 컴프리헨션의 기본 구조와 조건식을 이해한다.
- `map()`을 사용해 반복 가능한 객체의 요소를 변환할 수 있다.
- 2차원 리스트의 행과 열에 접근할 수 있다.
- 원본 코드에서 발생할 수 있는 `IndexError`, `ValueError`, `TypeError`를 설명할 수 있다.

---

# 1. 원본 코드 범위

두 원본은 다음 학습 흐름으로 구성되어 있습니다.

```text
빈 리스트 생성
→ range()와 list()
→ del
→ 리스트 연결
→ append()
→ sort()와 reverse()
→ pop()
→ insert()
→ extend()
→ remove()
→ index()와 count()
→ clear()
→ 슬라이싱 대입
→ 리스트 대입과 copy()
→ 구조 분해 대입
→ for 순회와 enumerate()
→ 최댓값 찾기
→ 리스트 컴프리헨션
→ map()
→ 2차원 리스트
→ 리스트 반복
```

내 코드는 강사님 코드보다 다음 실험을 추가로 포함합니다.

- 감소하는 `range(10, 0, -1)`
- 리스트에서 `find()`를 사용할 수 없다는 확인
- `a is b`와 `a == b` 비교
- `a[len(a):] = [500]` 슬라이싱 대입
- 빈 리스트의 길이와 Boolean 평가
- 마지막 인덱스를 반복문으로 찾는 예제
- 짝수 컴프리헨션을 별도로 출력하는 예제

강사님 코드에는 다음 확장 예제가 있습니다.

- `[i * 2 for i in range(10)]`
- 짝수에 대해 구구단 문자열을 만드는 컴프리헨션
- `f'2x{i}={2*i}'` 형태의 문자열 생성

---

# 2. 리스트란?

리스트는 여러 값을 순서대로 저장하는 Python의 대표적인 컬렉션 자료형입니다.

```python
numbers = [10, 20, 30]
names = ["민수", "영희", "철수"]
mixed = [1, "Python", True, 3.14]
```

리스트의 자료형은 `list`입니다.

```python
print(type(numbers))
```

출력:

```text
<class 'list'>
```

리스트는 다음 특징을 가집니다.

| 특징 | 설명 |
| --- | --- |
| 순서 유지 | 요소가 들어간 순서를 기억한다. |
| 인덱스 사용 | 첫 번째 요소의 인덱스는 `0`이다. |
| 변경 가능 | 생성한 뒤 요소를 추가·수정·삭제할 수 있다. |
| 중복 허용 | 같은 값을 여러 번 저장할 수 있다. |
| 서로 다른 자료형 허용 | 숫자, 문자열, Boolean, 다른 리스트 등을 함께 저장할 수 있다. |

```python
values = [1, 1, "hello", True, [10, 20]]
```

다만 실무에서는 한 리스트 안에 같은 의미와 비슷한 자료형의 값을 모으는 편이 코드 이해에 유리합니다.

---

# 3. 빈 리스트 생성

공통 원본:

```python
a = []
b = list()

print(type(a))
print(type(b))
```

출력:

```text
<class 'list'>
<class 'list'>
```

두 방식 모두 빈 리스트를 생성합니다.

```python
empty1 = []
empty2 = list()
```

일반적으로 단순한 빈 리스트는 `[]`를 더 자주 사용합니다.

`list()`는 다른 반복 가능한 객체를 리스트로 변환할 때 의미가 더 분명합니다.

```python
text = "ABC"

print(list(text))
```

출력:

```text
['A', 'B', 'C']
```

---

# 4. 값을 가진 리스트 생성

공통 원본:

```python
a = [1, 2, 3]
print(a)
```

출력:

```text
[1, 2, 3]
```

각 요소는 쉼표로 구분합니다.

```python
fruits = ["사과", "바나나", "복숭아"]
```

여러 줄로 작성할 수도 있습니다.

```python
fruits = [
    "사과",
    "바나나",
    "복숭아",
]
```

요소가 많거나 각 요소가 복잡할 때 여러 줄 형식이 읽기 좋습니다.

---

# 5. 리스트와 배열이라는 표현

내 코드 주석에는 리스트를 배열과 연결해 설명한 부분이 있습니다.

```python
# list는 배열의 선언보다 배열로 바꾸어주는 것
```

초기 학습에서는 리스트를 배열과 비슷한 자료 구조로 이해할 수 있습니다. 그러나 Python의 `list`와 다른 언어의 고정 길이 배열은 정확히 같은 개념은 아닙니다.

Python 리스트는 다음 기능을 기본으로 제공합니다.

- 길이를 동적으로 변경
- 서로 다른 자료형 저장
- 요소 추가와 삭제
- 슬라이싱
- 다양한 내장 메서드

따라서 문서에서는 Python 고유 자료형의 이름인 **리스트**를 기본 표현으로 사용합니다.

---

# 6. `range()`란?

`range()`는 일정한 규칙을 가진 정수 범위를 표현합니다.

```python
numbers = range(10)
print(numbers)
```

출력:

```text
range(0, 10)
```

`range()` 자체는 리스트가 아닙니다.

```python
print(type(range(10)))
```

출력:

```text
<class 'range'>
```

실제 숫자 목록을 확인하려면 `list()`로 변환할 수 있습니다.

```python
print(list(range(10)))
```

출력:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

`range()`는 모든 숫자를 미리 리스트로 만들지 않고 범위 규칙을 표현하므로 반복문에서 효율적으로 사용할 수 있습니다.

---

# 7. `range(stop)`

전달인자가 하나이면 `0`부터 `stop` 바로 앞까지 생성합니다.

공통 원본:

```python
c = range(10)

print(c)
print(list(c))
```

출력:

```text
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

일반 구조:

```python
range(stop)
```

`stop`은 포함되지 않습니다.

```text
시작: 0
종료: stop 미포함
증가량: 1
```

---

# 8. `range(start, stop)`

전달인자가 두 개이면 첫 번째 값부터 두 번째 값 바로 앞까지 생성합니다.

공통 원본:

```python
d = range(5, 12)
print(list(d))
```

출력:

```text
[5, 6, 7, 8, 9, 10, 11]
```

일반 구조:

```python
range(start, stop)
```

여기에서도 `stop`은 포함되지 않습니다.

---

# 9. 시작값이 종료값보다 큰 `range()`

공통 원본:

```python
e = range(12, 5)
print(list(e))
```

출력:

```text
[]
```

기본 증가량은 `1`입니다.

```text
12 → 13 → 14 → ...
```

이 방향으로는 `5`보다 작은 쪽으로 갈 수 없으므로 결과가 비어 있습니다.

감소하는 범위가 필요하다면 음수 `step`을 지정해야 합니다.

```python
print(list(range(12, 5, -1)))
```

출력:

```text
[12, 11, 10, 9, 8, 7, 6]
```

---

# 10. `range(start, stop, step)`

전달인자가 세 개이면 시작값, 종료 기준, 증가 또는 감소 간격을 지정합니다.

공통 원본:

```python
f = range(-4, 10, 2)
print(list(f))
```

출력:

```text
[-4, -2, 0, 2, 4, 6, 8]
```

일반 구조:

```python
range(start, stop, step)
```

| 인자 | 역할 |
| --- | --- |
| `start` | 시작값 |
| `stop` | 포함하지 않는 종료 기준 |
| `step` | 각 숫자 사이의 간격 |

---

# 11. 감소하는 `range()`

내 코드에만 다음 예제가 있습니다.

```python
f1 = range(10, 0, -1)
print(list(f1))
```

출력:

```text
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

`step`이 음수이면 값이 감소합니다.

여기에서도 `stop`인 `0`은 포함되지 않습니다.

```python
range(10, 0, -1)
```

은 다음 규칙입니다.

```text
10부터 시작
0보다 큰 동안 반복
매번 1씩 감소
```

---

# 12. `step`에는 0을 사용할 수 없다

다음 코드는 실행할 수 없습니다.

```python
range(1, 10, 0)
```

오류:

```text
ValueError: range() arg 3 must not be zero
```

증가량이 `0`이면 다음 값으로 이동할 수 없기 때문입니다.

---

# 13. `range()`를 리스트로 변환하기

공통 원본:

```python
a = [0, 1, 2, 3, 4, 5]
a = list(range(6))
```

두 결과는 같습니다.

```python
print([0, 1, 2, 3, 4, 5] == list(range(6)))
```

출력:

```text
True
```

연속된 정수 목록은 직접 모두 작성하는 것보다 `range()`를 이용하는 편이 간결합니다.

---

# 14. 리스트 인덱싱

리스트의 각 요소는 인덱스로 접근합니다.

```python
numbers = [10, 20, 30]

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

인덱스는 `0`부터 시작합니다.

| 인덱스 | 값 |
| ---: | ---: |
| `0` | `10` |
| `1` | `20` |
| `2` | `30` |

---

# 15. 음수 인덱스

음수 인덱스는 뒤에서부터 접근합니다.

```python
numbers = [10, 20, 30]

print(numbers[-1])
print(numbers[-2])
```

출력:

```text
30
20
```

| 음수 인덱스 | 위치 |
| ---: | --- |
| `-1` | 마지막 요소 |
| `-2` | 뒤에서 두 번째 요소 |
| `-3` | 뒤에서 세 번째 요소 |

원본의 최댓값 확인에서도 `a[-1]`을 사용합니다.

---

# 16. 존재하지 않는 인덱스와 `IndexError`

원본의 주석 처리된 코드:

```python
a = [1, 2, 3]

# print(a[3])
```

인덱스 `3`은 존재하지 않습니다.

실행하면 다음 오류가 발생합니다.

```text
IndexError: list index out of range
```

길이가 3인 리스트의 유효한 양수 인덱스는 `0`, `1`, `2`입니다.

```python
len(a)        # 3
a[len(a) - 1] # a[2]
```

---

# 17. 리스트 슬라이싱

슬라이싱은 리스트의 일부 범위를 새로운 리스트로 가져옵니다.

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
```

출력:

```text
[1, 2, 3]
```

기본 구조:

```python
리스트[start:stop:step]
```

문자열 슬라이싱과 마찬가지로 `stop` 인덱스는 포함하지 않습니다.

---

# 18. 범위를 벗어난 슬라이싱

공통 원본:

```python
a = [1, 2, 3]

print(a[len(a):])
print(a[3:])
```

출력:

```text
[]
[]
```

일반 인덱싱은 범위를 벗어나면 `IndexError`가 발생하지만, 슬라이싱은 가능한 범위까지만 처리합니다.

```python
a[100:]
```

결과:

```text
[]
```

이 차이는 다음과 같습니다.

| 표현 | 결과 |
| --- | --- |
| `a[3]` | 존재하지 않는 한 요소를 요구하므로 `IndexError` |
| `a[3:]` | 3번 위치부터 끝까지의 범위를 요구하므로 빈 리스트 |

---

# 19. `del` 문으로 요소 삭제

공통 원본:

```python
a = list(range(6))

del a[3]

print(a)
```

출력:

```text
[0, 1, 2, 4, 5]
```

`del`은 지정한 위치의 요소를 삭제합니다.

```python
del 리스트[인덱스]
```

범위도 삭제할 수 있습니다.

```python
numbers = [0, 1, 2, 3, 4, 5]

del numbers[1:4]

print(numbers)
```

출력:

```text
[0, 4, 5]
```

---

# 20. `del`과 메서드의 차이

`del`은 리스트 메서드가 아니라 Python 문장입니다.

```python
del numbers[0]
```

반면 다음은 리스트 객체의 메서드입니다.

```python
numbers.pop()
numbers.remove(10)
numbers.clear()
```

| 방식 | 기준 | 삭제한 값 반환 |
| --- | --- | :---: |
| `del a[index]` | 인덱스 | X |
| `a.pop(index)` | 인덱스 | O |
| `a.remove(value)` | 값 | X |
| `a.clear()` | 전체 | X |

---

# 21. `+`로 리스트 연결

공통 원본:

```python
a = a + [6]
print(a)
```

`+`는 두 리스트를 연결해 새로운 리스트를 만듭니다.

```python
left = [1, 2]
right = [3, 4]

result = left + right

print(result)
```

출력:

```text
[1, 2, 3, 4]
```

`left`와 `right` 자체는 변경되지 않습니다.

---

# 22. `+=`로 리스트 확장

공통 원본:

```python
a += [7]
print(a)
```

리스트에서 `+=`는 오른쪽의 반복 가능한 요소들을 현재 리스트에 추가합니다.

```python
numbers = [1, 2]
numbers += [3, 4]

print(numbers)
```

출력:

```text
[1, 2, 3, 4]
```

초기 학습 단계에서는 `extend()`와 유사한 결과로 이해할 수 있습니다.

```python
numbers.extend([5, 6])
```

---

# 23. 리스트에 리스트가 아닌 값을 더할 수 없다

다음 코드는 오류가 발생합니다.

```python
numbers = [1, 2, 3]
numbers + 4
```

오류:

```text
TypeError: can only concatenate list (not "int") to list
```

하나의 값을 추가하려면 `append()`를 사용합니다.

```python
numbers.append(4)
```

또는 오른쪽도 리스트로 작성해야 합니다.

```python
numbers += [4]
```

---

# 24. `append()`로 하나의 요소 추가

공통 원본:

```python
a.append(8)
print(a)
```

`append()`는 전달받은 객체 하나를 리스트 끝에 추가합니다.

```python
numbers = [1, 2]
numbers.append(3)

print(numbers)
```

출력:

```text
[1, 2, 3]
```

JavaScript의 배열에서 자주 사용하는 `push()`와 역할이 비슷하지만 Python 리스트 메서드 이름은 `append()`입니다.

---

# 25. `append()`에 리스트 전달하기

공통 원본:

```python
b = [9, 10]

a.append(b)

print(a)
```

결과의 마지막 요소는 리스트 하나입니다.

```text
[..., 8, [9, 10]]
```

`append()`는 전달한 리스트의 내부 요소를 하나씩 펼치지 않습니다.

```python
numbers = [1, 2]
numbers.append([3, 4])

print(numbers)
```

출력:

```text
[1, 2, [3, 4]]
```

전체 길이는 3입니다.

```python
print(len(numbers))
```

출력:

```text
3
```

---

# 26. `extend()`로 여러 요소 추가

공통 원본:

```python
c.extend([1, 2])
print(c)
```

`extend()`는 전달받은 반복 가능한 객체의 요소를 하나씩 현재 리스트 뒤에 추가합니다.

```python
numbers = [1, 2]
numbers.extend([3, 4])

print(numbers)
```

출력:

```text
[1, 2, 3, 4]
```

---

# 27. `append()`와 `extend()` 비교

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

| 메서드 | 전달값 처리 | 결과 |
| --- | --- | --- |
| `append(x)` | `x` 전체를 요소 하나로 추가 | 중첩 리스트 가능 |
| `extend(iterable)` | 내부 요소를 하나씩 추가 | 리스트 확장 |

---

# 28. `extend()`에는 반복 가능한 객체가 필요하다

다음 코드는 실행할 수 없습니다.

```python
numbers = [1, 2]
numbers.extend(3)
```

오류:

```text
TypeError: 'int' object is not iterable
```

문자열은 반복 가능한 객체이므로 각 문자가 추가됩니다.

```python
letters = []
letters.extend("ABC")

print(letters)
```

출력:

```text
['A', 'B', 'C']
```

문자열 전체를 요소 하나로 넣으려면 `append("ABC")`를 사용합니다.

---

# 29. `insert()`로 원하는 위치에 추가

공통 원본:

```python
c.insert(0, 100)
print(c)
```

기본 구조:

```python
리스트.insert(index, value)
```

예제:

```python
numbers = [20, 30]
numbers.insert(0, 10)

print(numbers)
```

출력:

```text
[10, 20, 30]
```

기존 요소들은 뒤로 이동합니다.

---

# 30. 범위를 넘는 `insert()` 인덱스

공통 원본:

```python
c.insert(10, 200)
```

현재 리스트 길이보다 큰 인덱스를 지정하면 끝에 추가됩니다.

```python
numbers = [1, 2, 3]
numbers.insert(100, 4)

print(numbers)
```

출력:

```text
[1, 2, 3, 4]
```

음수 인덱스도 사용할 수 있습니다.

```python
numbers.insert(-1, 99)
```

인덱스 처리 결과는 리스트 길이에 따라 달라질 수 있으므로, 명확한 위치가 필요하다면 실제 범위를 기준으로 작성하는 편이 좋습니다.

---

# 31. `pop()`으로 요소 꺼내기

공통 원본:

```python
d = c.pop()

print(c, d)
```

인자를 생략한 `pop()`은 마지막 요소를 제거하고 그 값을 반환합니다.

```python
numbers = [10, 20, 30]
removed = numbers.pop()

print(numbers)
print(removed)
```

출력:

```text
[10, 20]
30
```

삭제한 값을 이후 코드에서 사용해야 할 때 유용합니다.

---

# 32. 인덱스를 지정한 `pop()`

```python
numbers = [10, 20, 30]
removed = numbers.pop(0)

print(numbers)
print(removed)
```

출력:

```text
[20, 30]
10
```

기본 구조:

```python
리스트.pop()
리스트.pop(index)
```

존재하지 않는 인덱스를 지정하면 `IndexError`가 발생합니다.

---

# 33. 빈 리스트에서 `pop()` 사용

```python
items = []
items.pop()
```

오류:

```text
IndexError: pop from empty list
```

필요하다면 먼저 리스트가 비어 있지 않은지 확인합니다.

```python
if items:
    value = items.pop()
```

---

# 34. `remove()`로 값 삭제

공통 원본:

```python
a = [1, 2, 3, 4, 2]

a.remove(2)

print(a)
```

출력:

```text
[1, 3, 4, 2]
```

`remove(value)`는 왼쪽에서부터 검색해 처음 만나는 값 하나를 삭제합니다.

같은 값이 여러 개여도 한 번에 하나만 삭제합니다.

---

# 35. 존재하지 않는 값을 `remove()`하면 발생하는 오류

원본:

```python
if 5 in a:
    a.remove(5)
```

조건문을 사용하지 않고 바로 실행하면 다음 오류가 발생할 수 있습니다.

```python
a.remove(5)
```

오류:

```text
ValueError: list.remove(x): x not in list
```

원본은 `in`으로 존재 여부를 먼저 확인해 오류를 방지합니다.

```python
if target in a:
    a.remove(target)
```

---

# 36. 모든 같은 값 삭제하기

`remove()`는 첫 번째 값만 삭제합니다.

모든 같은 값을 제거하려면 반복하거나 새로운 리스트를 만들 수 있습니다.

```python
numbers = [1, 2, 3, 2, 4, 2]
target = 2

numbers = [
    value
    for value in numbers
    if value != target
]

print(numbers)
```

출력:

```text
[1, 3, 4]
```

이 예제는 리스트 컴프리헨션을 이용한 확장 학습입니다.

---

# 37. `clear()`로 전체 삭제

공통 원본:

```python
a.clear()
print(a)
```

출력:

```text
[]
```

`clear()`는 리스트 객체는 유지하면서 모든 요소를 제거합니다.

```python
items = [1, 2, 3]
items.clear()
```

강사님 코드에는 이어서 다음 대입도 있습니다.

```python
a = []
```

두 방식 모두 변수 `a`에서 빈 리스트를 확인할 수 있지만 객체 관점에서는 차이가 있습니다.

---

# 38. `clear()`와 `a = []`의 차이

```python
a = [1, 2, 3]
b = a

a.clear()

print(a)
print(b)
```

출력:

```text
[]
[]
```

`a`와 `b`가 같은 리스트를 참조하기 때문에 기존 리스트를 비우면 둘 다 빈 리스트로 보입니다.

반면:

```python
a = [1, 2, 3]
b = a

a = []

print(a)
print(b)
```

출력:

```text
[]
[1, 2, 3]
```

`a = []`는 `a`가 새 빈 리스트를 참조하도록 바꿀 뿐, 기존 리스트 자체를 비우지 않습니다.

---

# 39. `index()`로 값의 위치 찾기

공통 원본:

```python
a = [1, 2, 3, 4, 2, 4]

b = a.index(2)

print(b)
```

출력:

```text
1
```

`index(value)`는 처음 만난 값의 인덱스를 반환합니다.

같은 값이 여러 번 있어도 첫 번째 위치만 반환합니다.

---

# 40. 존재하지 않는 값을 `index()`로 찾기

원본의 주석 처리된 코드:

```python
# b = a.index(5)
```

실행하면 다음 오류가 발생합니다.

```text
ValueError: 5 is not in list
```

안전하게 사용하려면 먼저 `in`으로 확인할 수 있습니다.

```python
if target in a:
    position = a.index(target)
else:
    position = -1
```

---

# 41. 리스트에는 `find()`가 없다

내 코드의 주석:

```python
# b = a.find(5)
```

문자열에는 `find()`가 있지만 리스트에는 없습니다.

```python
text = "hello"
text.find("e")
```

리스트에서는 다음 방식을 사용합니다.

```python
target in items
items.index(target)
```

`find()`를 호출하면 다음 오류가 발생합니다.

```text
AttributeError: 'list' object has no attribute 'find'
```

---

# 42. `count()`로 값의 개수 확인

공통 원본:

```python
c = a.count(4)
print(c)
```

`count(value)`는 리스트 안에서 해당 값이 등장한 횟수를 반환합니다.

```python
numbers = [1, 2, 4, 2, 4, 4]

print(numbers.count(4))
```

출력:

```text
3
```

값이 없으면 오류가 아니라 `0`을 반환합니다.

```python
print(numbers.count(100))
```

출력:

```text
0
```

---

# 43. `in`과 `not in`

원본은 `remove()`를 실행하기 전에 `in`을 사용합니다.

```python
if 5 in a:
    a.remove(5)
```

`in`은 값의 포함 여부를 Boolean으로 반환합니다.

```python
numbers = [10, 20, 30]

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

존재 여부만 필요하다면 `index()`보다 `in`이 적합합니다.

---

# 44. `sort()`로 원본 정렬

공통 원본:

```python
c = [654, 156, 964, 15, 35]

c.sort()

print(c)
```

출력:

```text
[15, 35, 156, 654, 964]
```

`sort()`는 리스트 원본을 오름차순으로 정렬합니다.

```python
numbers.sort()
```

숫자 리스트는 숫자 크기를 기준으로 정렬합니다.

내 코드 주석에서 JavaScript 문자열 정렬과의 차이를 확인한 부분도 이 예제에 해당합니다.

---

# 45. `sort(reverse=True)`

공통 원본:

```python
c.sort(reverse=True)
print(c)
```

출력:

```text
[964, 654, 156, 35, 15]
```

`reverse=True`를 사용하면 내림차순으로 정렬합니다.

기본값은 `False`입니다.

```python
c.sort(reverse=False)
```

---

# 46. `sort()`의 반환값

`sort()`는 원본 리스트를 변경하고 일반적으로 `None`을 반환합니다.

```python
numbers = [3, 1, 2]

result = numbers.sort()

print(numbers)
print(result)
```

출력:

```text
[1, 2, 3]
None
```

따라서 다음처럼 작성하면 의도와 다르게 `numbers`가 `None`이 됩니다.

```python
numbers = numbers.sort()
```

개선:

```python
numbers.sort()
```

또는 새로운 정렬 리스트가 필요하면 `sorted()`를 사용합니다.

---

# 47. `sorted()`로 새 리스트 만들기

`sorted()`는 원본을 유지하고 정렬된 새 리스트를 반환합니다.

```python
numbers = [3, 1, 2]

sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)
```

출력:

```text
[3, 1, 2]
[1, 2, 3]
```

`sorted()`는 원본 코드에 직접 등장하지 않는 보충 개념입니다.

| 방식 | 원본 변경 | 반환값 |
| --- | :---: | --- |
| `list.sort()` | O | `None` |
| `sorted(iterable)` | X | 정렬된 새 리스트 |

---

# 48. 문자열 리스트 정렬

```python
names = ["banana", "Apple", "cherry"]

names.sort()

print(names)
```

문자열은 문자 코드와 대소문자 규칙에 따라 정렬됩니다.

대소문자를 무시한 정렬은 `key`를 사용할 수 있습니다.

```python
names.sort(key=str.lower)
```

`key` 사용은 원본 범위를 확장한 보충 학습입니다.

---

# 49. 슬라이싱 `[::-1]`로 역순 복사

공통 원본:

```python
c = c[::-1]
print(c)
```

`[::-1]`은 역순으로 된 새 리스트를 만듭니다.

```python
numbers = [1, 2, 3]
reversed_numbers = numbers[::-1]

print(numbers)
print(reversed_numbers)
```

출력:

```text
[1, 2, 3]
[3, 2, 1]
```

단, 원본 코드에서는 결과를 다시 `c`에 대입하므로 변수 `c`가 역순 리스트를 참조하게 됩니다.

```python
c = c[::-1]
```

---

# 50. `reverse()`로 원본 순서 뒤집기

공통 원본:

```python
c.reverse()
print(c)
```

`reverse()`는 정렬 기준을 적용하는 것이 아니라 현재 순서를 그대로 반대로 뒤집습니다.

```python
numbers = [3, 1, 2]
numbers.reverse()

print(numbers)
```

출력:

```text
[2, 1, 3]
```

이 결과는 오름차순이나 내림차순이라고 단정할 수 없습니다.

원본의 `c`는 직전에 정렬된 상태였기 때문에 결과가 정렬처럼 보일 뿐입니다.

---

# 51. `reverse()`와 내림차순 정렬의 차이

```python
numbers = [3, 1, 2]
```

순서 뒤집기:

```python
numbers.reverse()
# [2, 1, 3]
```

내림차순 정렬:

```python
numbers.sort(reverse=True)
# [3, 2, 1]
```

| 기능 | 의미 |
| --- | --- |
| `reverse()` | 현재 순서를 반대로 배치 |
| `sort(reverse=True)` | 값의 크기를 기준으로 내림차순 정렬 |

따라서 `reverse()`를 무조건 내림차순 정렬이라고 설명하면 정확하지 않습니다.

---

# 52. `reversed()`가 반환하는 객체

내 코드:

```python
a.reverse()
b = reversed(a)

print(b)
```

출력 형태:

```text
<list_reverseiterator object at ...>
```

`reversed()`는 즉시 리스트를 반환하지 않고 역방향 반복자(iterator)를 반환합니다.

내용을 리스트로 확인하려면 변환합니다.

```python
b = list(reversed(a))
print(b)
```

`reversed()`는 원본 리스트를 변경하지 않습니다.

---

# 53. `reverse()`, `reversed()`, `[::-1]` 비교

| 방식 | 원본 변경 | 결과 |
| --- | :---: | --- |
| `a.reverse()` | O | 반환값 `None` |
| `reversed(a)` | X | 역방향 반복자 |
| `a[::-1]` | X | 역순의 새 리스트 |

목적에 따라 선택합니다.

---

# 54. 슬라이싱 대입

공통 원본:

```python
a = [1, 2, 3]

a[3:] = [4, 5, 6]

print(a)
```

출력:

```text
[1, 2, 3, 4, 5, 6]
```

슬라이싱 대입은 특정 범위를 반복 가능한 객체의 요소들로 교체합니다.

```python
a[start:stop] = iterable
```

범위 길이와 새 요소 개수가 같을 필요는 없습니다.

```python
numbers = [1, 2, 3, 4]
numbers[1:3] = [20, 30, 40]

print(numbers)
```

출력:

```text
[1, 20, 30, 40, 4]
```

---

# 55. 슬라이싱 대입에는 반복 가능한 값이 필요하다

원본의 주석 처리된 코드:

```python
# a[3:] = 4
```

실행하면 다음 오류가 발생합니다.

```text
TypeError: can only assign an iterable
```

Python 버전과 슬라이스 형태에 따라 오류 문구가 조금 다르게 표시될 수 있지만 핵심 원인은 같습니다.

오른쪽에는 반복 가능한 객체가 필요합니다.

```python
a[3:] = [4]
```

---

# 56. 빈 슬라이스 위치에 요소 추가

내 코드:

```python
a[len(a):] = [500]

print(a)
```

`len(a)`는 리스트 끝의 바로 다음 삽입 위치를 나타냅니다.

따라서 다음과 비슷한 결과를 냅니다.

```python
a.append(500)
```

또는:

```python
a.extend([500])
```

하지만 목적이 단일 요소 추가라면 `append()`가 더 직관적입니다.

슬라이싱 대입은 범위 교체가 핵심 기능입니다.

---

# 57. 리스트 요소 수정

리스트는 변경 가능한 자료형이므로 인덱스에 새 값을 대입할 수 있습니다.

```python
numbers = [10, 20, 30]
numbers[1] = 200

print(numbers)
```

출력:

```text
[10, 200, 30]
```

문자열은 같은 방식으로 수정할 수 없지만 리스트는 가능합니다.

---

# 58. 빈 리스트의 Boolean 평가

내 코드:

```python
f = []

print(len(f))
print(not len(f))
```

출력:

```text
0
True
```

정확히 말하면 `len(f)`의 결과는 Boolean `False`가 아니라 정수 `0`입니다.

다만 조건식에서 `0`은 falsy로 평가됩니다.

```python
if not f:
    print("리스트가 비어 있습니다.")
```

빈 리스트 여부를 검사할 때는 다음 표현이 더 Python답고 직접적입니다.

```python
if not f:
```

반대로 요소가 하나 이상 있는지 확인하려면:

```python
if f:
```

---

# 59. 리스트 대입은 복사가 아니다

공통 원본:

```python
a = [1, 2, 3, 4, 5]
b = a

b[2] = 30

print(b)
print(a)
```

출력:

```text
[1, 2, 30, 4, 5]
[1, 2, 30, 4, 5]
```

`b = a`는 리스트의 요소를 새로 복사하는 것이 아닙니다.

두 변수가 같은 리스트 객체를 참조합니다.

```text
a ─┐
   ├──> [1, 2, 3, 4, 5]
b ─┘
```

따라서 `b`를 통해 요소를 수정하면 `a`에서도 같은 변경이 보입니다.

---

# 60. Python의 객체 참조 의미론

Python 변수는 값을 담는 상자라기보다 객체를 가리키는 이름으로 이해하는 편이 정확합니다.

```python
a = [1, 2, 3]
b = a
```

이 코드는 다음 의미입니다.

```text
리스트 객체 하나 생성
a가 그 객체를 참조
b도 같은 객체를 참조
```

이 개념은 사전 문서의 Python 객체 참조 의미론과 연결됩니다.

---

# 61. `copy()`로 얕은 복사

공통 원본:

```python
a = [1, 2, 3, 4, 5]
b = a.copy()

b[2] = 30

print(b)
print(a)
```

출력:

```text
[1, 2, 30, 4, 5]
[1, 2, 3, 4, 5]
```

`copy()`는 새로운 리스트 객체를 만듭니다.

```text
a ───> [1, 2, 3, 4, 5]
b ───> [1, 2, 3, 4, 5]
```

바깥 리스트 객체가 서로 다르기 때문에 `b[2]`를 바꿔도 `a[2]`는 바뀌지 않습니다.

---

# 62. `is`와 `==`

내 코드에만 다음 비교가 있습니다.

```python
a = [1, 2, 3, 4, 5]
b = a.copy()

print(a is b)
print(a == b)
```

출력:

```text
False
True
```

| 연산자 | 검사 대상 | 결과 |
| --- | --- | --- |
| `is` | 같은 객체인가 | `False` |
| `==` | 값이 같은가 | `True` |

두 리스트의 내용은 같지만 서로 다른 객체입니다.

`is`를 JavaScript의 엄격 동등 연산자처럼 이해하면 안 됩니다.

---

# 63. 슬라이싱으로 리스트 복사

다음 방식도 새로운 바깥 리스트를 만듭니다.

```python
a = [1, 2, 3]
b = a[:]

print(a is b)
print(a == b)
```

출력:

```text
False
True
```

일반적으로 의도를 명확하게 나타내려면 `copy()`가 읽기 쉽습니다.

---

# 64. 얕은 복사의 한계

`copy()`는 얕은 복사입니다.

중첩 리스트의 내부 객체까지 재귀적으로 새로 만들지는 않습니다.

```python
a = [[1, 2], [3, 4]]
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

바깥 리스트는 다르지만 내부 리스트는 공유합니다.

```text
a ───> [ ──> [1, 2], ──> [3, 4] ]
b ───> [ ──┘         ──┘          ]
```

---

# 65. 깊은 복사

중첩된 내부 객체까지 독립적으로 복사해야 한다면 `copy.deepcopy()`를 사용할 수 있습니다.

```python
from copy import deepcopy

a = [[1, 2], [3, 4]]
b = deepcopy(a)

b[0][0] = 100

print(a)
print(b)
```

출력:

```text
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]
```

깊은 복사는 원본 코드에 직접 등장하지 않는 보충 학습입니다.

---

# 66. 구조 분해 대입

공통 원본:

```python
c = (1, 2)

a = c[0]
b = c[1]
```

Python에서는 다음처럼 간단하게 작성할 수 있습니다.

```python
a, b = (1, 2)
```

출력 확인:

```python
print(a, b)
```

```text
1 2
```

오른쪽 요소 개수와 왼쪽 변수 개수가 맞아야 합니다.

---

# 67. 리스트도 구조 분해 대입 가능

```python
first, second, third = [10, 20, 30]

print(first)
print(second)
print(third)
```

출력:

```text
10
20
30
```

요소 개수가 맞지 않으면 `ValueError`가 발생합니다.

```python
a, b = [1, 2, 3]
```

오류:

```text
ValueError: too many values to unpack
```

---

# 68. 별표를 이용한 나머지 요소 받기

```python
first, *rest = [10, 20, 30, 40]

print(first)
print(rest)
```

출력:

```text
10
[20, 30, 40]
```

이 문법은 원본에는 직접 등장하지 않는 구조 분해의 확장 학습입니다.

---

# 69. 리스트 직접 순회

공통 원본:

```python
a = [10, 20, 30]

for i in a:
    print(i)
```

출력:

```text
10
20
30
```

리스트의 값을 읽기만 한다면 인덱스보다 요소를 직접 순회하는 방식이 간결합니다.

```python
for value in a:
    print(value)
```

변수 이름을 `i`보다 `value`처럼 의미 있게 작성하면 역할이 더 명확합니다.

---

# 70. `enumerate()`로 인덱스와 값 함께 얻기

공통 원본:

```python
for index, value in enumerate(a):
    print(index, value)
```

출력:

```text
0 10
1 20
2 30
```

`enumerate()`는 반복할 때 인덱스와 값을 함께 제공합니다.

기본 구조:

```python
for index, value in enumerate(iterable):
    ...
```

리스트 요소를 수정하거나 번호와 함께 출력할 때 유용합니다.

---

# 71. `enumerate(start=...)`

공통 원본:

```python
for index, value in enumerate(a, start=100):
    print(index, value)
```

출력:

```text
100 10
101 20
102 30
```

`start`는 출력 또는 전달되는 번호의 시작값을 바꿉니다.

리스트의 실제 인덱스가 100부터 바뀌는 것은 아닙니다.

```python
print(a[0])
```

여전히 첫 번째 요소는 인덱스 `0`으로 접근합니다.

---

# 72. `range(len(a))`와 직접 순회 비교

인덱스가 필요한 경우:

```python
for index in range(len(a)):
    print(index, a[index])
```

값만 필요한 경우:

```python
for value in a:
    print(value)
```

인덱스와 값이 모두 필요한 경우:

```python
for index, value in enumerate(a):
    print(index, value)
```

목적에 맞는 방식을 선택합니다.

---

# 73. 최댓값 찾기: 정렬 후 마지막 값

공통 원본:

```python
a = [7, 3, 5, 8, 4]

a.sort()

print(a[len(a) - 1])
print(a[-1])
```

출력:

```text
8
8
```

오름차순 정렬 후 마지막 요소가 가장 큰 값입니다.

`a[-1]`이 `a[len(a) - 1]`보다 간결합니다.

---

# 74. 최댓값만 필요할 때 `max()`

최댓값 하나만 필요하다면 전체 리스트를 정렬할 필요가 없습니다.

```python
a = [7, 3, 5, 8, 4]

print(max(a))
```

출력:

```text
8
```

정렬은 요소 전체 순서를 변경합니다.

`max()`는 원본 순서를 변경하지 않고 최댓값을 구합니다.

`max()`는 원본 코드의 목적을 기준으로 덧붙인 개선 방법입니다.

---

# 75. 반복문으로 마지막 요소 찾기

내 코드:

```python
for i in range(len(a)):
    if i == len(a) - 1:
        print(a[i])
```

이 코드는 인덱스가 마지막 위치일 때 값을 출력합니다.

학습용으로는 인덱스와 길이의 관계를 확인할 수 있습니다.

하지만 마지막 값만 필요하다면 다음이 더 직접적입니다.

```python
print(a[-1])
```

최댓값이 필요하다면:

```python
print(max(a))
```

---

# 76. 빈 리스트의 마지막 요소

```python
items = []
print(items[-1])
```

오류:

```text
IndexError: list index out of range
```

빈 리스트 가능성이 있다면 먼저 확인합니다.

```python
if items:
    print(items[-1])
```

또는 요구사항에 따라 기본값을 처리합니다.

---

# 77. 반복문으로 0부터 9까지 리스트 만들기

공통 원본:

```python
a = []

for i in range(10):
    a.append(i)

print(a)
```

출력:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

이 코드는 다음 과정을 반복합니다.

```text
빈 리스트 생성
→ range(10)에서 값 하나 꺼내기
→ append()로 추가
→ 반복 완료 후 출력
```

---

# 78. 리스트 컴프리헨션

공통 원본:

```python
a = [i for i in range(10)]
print(a)
```

출력:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

리스트 컴프리헨션은 반복 가능한 객체에서 값을 꺼내 새로운 리스트를 간결하게 만드는 문법입니다.

기본 구조:

```python
[표현식 for 변수 in 반복가능한객체]
```

원본 코드:

```python
[i for i in range(10)]
```

해석:

```text
range(10)에서 i를 하나씩 꺼내고
각 i를 그대로 새 리스트의 요소로 넣는다
```

---

# 79. 리스트 컴프리헨션과 일반 반복문 비교

일반 반복문:

```python
numbers = []

for i in range(10):
    numbers.append(i)
```

리스트 컴프리헨션:

```python
numbers = [i for i in range(10)]
```

두 결과는 같습니다.

컴프리헨션은 간결하지만 표현식과 조건이 지나치게 복잡해지면 일반 반복문이 더 읽기 좋습니다.

---

# 80. 값을 변환하는 리스트 컴프리헨션

강사님 코드:

```python
a = [i * 2 for i in range(10)]
```

결과:

```text
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

기본 구조에서 앞의 표현식이 새 리스트에 들어갈 값을 결정합니다.

```python
[i * 2 for i in range(10)]
```

```text
반복 변수: i
변환 표현식: i * 2
```

---

# 81. 조건이 있는 리스트 컴프리헨션

내 코드의 일반 반복문:

```python
a = []

for i in range(10):
    if i % 2 == 0:
        a.append(i)
```

컴프리헨션:

```python
a = [
    i
    for i in range(10)
    if i % 2 == 0
]
```

출력:

```text
[0, 2, 4, 6, 8]
```

기본 구조:

```python
[표현식 for 변수 in 반복가능한객체 if 조건식]
```

조건식이 참인 값만 새 리스트에 포함합니다.

---

# 82. `list(generator expression)` 방식

내 코드:

```python
a = list(
    i
    for i in range(10)
    if i % 2 == 0
)
```

이 코드는 리스트 컴프리헨션과 비슷한 결과를 만듭니다.

```python
a = [
    i
    for i in range(10)
    if i % 2 == 0
]
```

다만 내부 문법은 엄밀히 말해 제너레이터 표현식이고, `list()`가 그 결과를 리스트로 소비합니다.

리스트를 바로 만들 목적이라면 리스트 컴프리헨션이 더 직접적입니다.

---

# 83. 문자열을 만드는 컴프리헨션

강사님 코드:

```python
a = list(
    f"2x{i}={2 * i}"
    for i in range(10)
    if i % 2 == 0
)

print(a)
```

결과:

```text
['2x0=0', '2x2=4', '2x4=8', '2x6=12', '2x8=16']
```

각 숫자를 그대로 저장하는 대신 f-string으로 변환한 문자열을 저장합니다.

```text
반복: 0부터 9
조건: 짝수
결과: 구구단 문자열
```

---

# 84. 조건식이 앞에 오는 컴프리헨션

다음 형태는 필터가 아니라 조건에 따라 결과값을 선택합니다.

```python
labels = [
    "짝수" if i % 2 == 0 else "홀수"
    for i in range(5)
]
```

출력:

```text
['짝수', '홀수', '짝수', '홀수', '짝수']
```

두 문법의 위치를 구분해야 합니다.

필터:

```python
[i for i in numbers if 조건]
```

조건부 표현식:

```python
[참값 if 조건 else 거짓값 for i in numbers]
```

이 내용은 원본 범위를 확장한 보충 학습입니다.

---

# 85. 컴프리헨션을 지나치게 복잡하게 만들지 않기

다음처럼 중첩 조건과 여러 표현이 계속 이어지면 읽기 어려워질 수 있습니다.

```python
result = [
    ...
    for ...
    if ...
]
```

다음 기준을 사용할 수 있습니다.

- 한 줄로 읽었을 때 의미가 바로 보이면 컴프리헨션
- 조건이 여러 단계이면 일반 반복문
- 중간 디버깅이 필요하면 일반 반복문
- 부수 효과가 목적이면 일반 반복문

컴프리헨션은 리스트 생성이 목적일 때 사용합니다.

---

# 86. `enumerate()`로 리스트 요소를 직접 수정

공통 원본:

```python
a = [1.2, 2.5, 3.7, 4.6, -3.5]

for i, value in enumerate(a):
    a[i] = int(value)

print(a)
```

출력:

```text
[1, 2, 3, 4, -3]
```

`int()`는 실수의 소수 부분을 0 방향으로 버립니다.

```python
int(3.7)   # 3
int(-3.5)  # -3
```

반올림이 아닙니다.

---

# 87. 반복 중 요소 변수만 바꿔도 원본은 바뀌지 않는다

```python
numbers = [1, 2, 3]

for value in numbers:
    value = value * 10

print(numbers)
```

출력:

```text
[1, 2, 3]
```

`value`라는 반복 변수에 새 값을 대입했을 뿐 리스트 인덱스에 대입하지 않았습니다.

원본 요소를 교체하려면 인덱스를 사용합니다.

```python
for index, value in enumerate(numbers):
    numbers[index] = value * 10
```

---

# 88. `map()`으로 요소 변환

공통 원본:

```python
a = [1.2, 2.5, 3.7, 4.6, -3.5]

a = list(map(int, a))

print(a)
```

출력:

```text
[1, 2, 3, 4, -3]
```

`map()`은 반복 가능한 객체의 각 요소를 지정한 함수에 전달합니다.

기본 구조:

```python
map(function, iterable)
```

원본 코드의 처리 흐름:

```text
리스트에서 실수를 하나씩 꺼낸다
→ int()에 전달한다
→ 변환 결과를 순서대로 만든다
→ list()로 최종 리스트를 만든다
```

---

# 89. `map()`은 리스트를 직접 반환하지 않는다

Python 3에서 `map()`은 map 객체를 반환합니다.

```python
result = map(int, [1.2, 2.5])

print(result)
```

출력 형태:

```text
<map object at ...>
```

내용을 리스트로 확인하려면 다음처럼 변환합니다.

```python
result = list(map(int, [1.2, 2.5]))
```

---

# 90. `map()`과 리스트 컴프리헨션 비교

`map()`:

```python
numbers = list(map(int, values))
```

리스트 컴프리헨션:

```python
numbers = [int(value) for value in values]
```

둘 다 같은 결과를 만들 수 있습니다.

| 방식 | 장점 |
| --- | --- |
| `map()` | 이미 존재하는 함수를 모든 요소에 적용할 때 간결 |
| 컴프리헨션 | 변환식과 조건을 눈으로 읽기 쉬움 |

단순한 `int`, `str`, `float` 변환에는 둘 다 자주 사용됩니다.

---

# 91. 2차원 리스트

공통 원본:

```python
a = [
    [10, 20],
    [30, 40],
    [50, 60],
]
```

리스트 안에 리스트가 들어 있는 구조입니다.

```text
[
    [10, 20],
    [30, 40],
    [50, 60]
]
```

행과 열처럼 이해할 수 있습니다.

| 행 인덱스 | 값 |
| ---: | --- |
| `0` | `[10, 20]` |
| `1` | `[30, 40]` |
| `2` | `[50, 60]` |

---

# 92. 2차원 리스트의 길이

공통 원본:

```python
print(len(a))
```

출력:

```text
3
```

바깥 리스트의 요소는 내부 리스트 3개이므로 길이는 3입니다.

첫 번째 행의 열 개수:

```python
print(len(a[0]))
```

출력:

```text
2
```

---

# 93. 2차원 리스트 요소 접근

공통 원본:

```python
print(a[1][0])
```

출력:

```text
30
```

접근 순서:

```text
a[1]    → [30, 40]
a[1][0] → 30
```

일반 구조:

```python
리스트[행_인덱스][열_인덱스]
```

---

# 94. 2차원 리스트 순회

```python
matrix = [
    [10, 20],
    [30, 40],
    [50, 60],
]

for row in matrix:
    for value in row:
        print(value)
```

출력:

```text
10
20
30
40
50
60
```

바깥 반복문은 행을, 안쪽 반복문은 각 행의 요소를 순회합니다.

이 예제는 이후 반복문 문서와 연결됩니다.

---

# 95. 3차원 리스트의 기본 구조

2차원 리스트 안에 다시 리스트 계층을 추가하면 3차원 구조를 표현할 수 있습니다.

```python
data = [
    [
        [1, 2],
        [3, 4],
    ],
    [
        [5, 6],
        [7, 8],
    ],
]
```

접근:

```python
print(data[1][0][1])
```

출력:

```text
6
```

```text
data[1]       → 두 번째 묶음
data[1][0]    → 그 안의 첫 번째 행
data[1][0][1] → 그 행의 두 번째 값
```

3차원 리스트는 원본에 직접 등장하지 않지만, 2차원 리스트의 구조를 확장한 보충 개념입니다.

---

# 96. 리스트 반복 연산자 `*`

공통 원본:

```python
print([0] * 10)
```

출력:

```text
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

리스트에 정수를 곱하면 요소가 해당 횟수만큼 반복됩니다.

```python
print(["A", "B"] * 3)
```

출력:

```text
['A', 'B', 'A', 'B', 'A', 'B']
```

---

# 97. 중첩 리스트를 `*`로 만들 때 주의점

다음 코드는 같은 내부 리스트 참조를 반복합니다.

```python
matrix = [[0] * 3] * 3

matrix[0][0] = 1

print(matrix)
```

출력:

```text
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

세 행이 독립적인 리스트가 아니라 같은 내부 리스트를 참조하기 때문입니다.

독립된 행을 만들려면 컴프리헨션을 사용합니다.

```python
matrix = [
    [0] * 3
    for _ in range(3)
]
```

이제 한 행을 수정해도 다른 행에는 영향을 주지 않습니다.

```python
matrix[0][0] = 1

print(matrix)
```

출력:

```text
[[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

# 98. 사용하지 않는 반복 변수 `_`

리스트의 행을 일정 횟수 생성할 때 반복값 자체가 필요하지 않을 수 있습니다.

```python
matrix = [
    [0] * 3
    for _ in range(3)
]
```

`_`는 관례적으로 해당 반복값을 사용하지 않겠다는 의미를 나타냅니다.

문법적으로 일반 변수이지만, 코드 독자에게 사용하지 않는 값이라는 의도를 전달합니다.

---

# 99. 스택과 리스트

내 코드 주석에는 스택을 프링글스 통에 비유한 설명이 있습니다.

스택은 마지막에 넣은 데이터를 먼저 꺼내는 구조입니다.

```text
Last In, First Out
LIFO
```

리스트로 간단한 스택을 만들 수 있습니다.

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack.pop())
print(stack.pop())
```

출력:

```text
C
B
```

`append()`로 뒤에 넣고 `pop()`으로 뒤에서 꺼냅니다.

---

# 100. 큐와 리스트

큐는 먼저 넣은 데이터를 먼저 꺼내는 구조입니다.

```text
First In, First Out
FIFO
```

리스트로 표현하면 다음과 같습니다.

```python
queue = []

queue.append("A")
queue.append("B")
queue.append("C")

print(queue.pop(0))
```

출력:

```text
A
```

다만 리스트의 앞쪽에서 삭제하면 나머지 요소들을 이동해야 하므로 데이터가 많을 때 비효율적일 수 있습니다.

실무에서는 `collections.deque`를 사용할 수 있습니다.

```python
from collections import deque

queue = deque()

queue.append("A")
queue.append("B")

print(queue.popleft())
```

`deque`는 원본 주석의 큐 개념을 정확히 연결하기 위한 보충 내용입니다.

---

# 101. 리스트 메서드 반환값 정리

| 메서드 | 원본 변경 | 주요 반환값 |
| --- | :---: | --- |
| `append(x)` | O | `None` |
| `extend(iterable)` | O | `None` |
| `insert(i, x)` | O | `None` |
| `remove(x)` | O | `None` |
| `pop()` | O | 삭제한 요소 |
| `clear()` | O | `None` |
| `sort()` | O | `None` |
| `reverse()` | O | `None` |
| `copy()` | X | 새 리스트 |
| `index(x)` | X | 첫 번째 인덱스 |
| `count(x)` | X | 등장 횟수 |

원본을 변경하는 메서드 상당수는 `None`을 반환합니다.

---

# 102. 원본 전체 실행 결과 핵심

원본의 주요 출력 흐름은 다음과 같습니다.

```text
<class 'list'>
<class 'list'>
[1, 2, 3]

range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

[5, 6, 7, 8, 9, 10, 11]
[]

[-4, -2, 0, 2, 4, 6, 8]

[0, 1, 2, 4, 5]
[0, 1, 2, 4, 5, 6]
[0, 1, 2, 4, 5, 6, 7]
[0, 1, 2, 4, 5, 6, 7, 8]
[0, 1, 2, 4, 5, 6, 7, 8, [9, 10]]

[15, 35, 156, 654, 964]
[964, 654, 156, 35, 15]

...
```

두 파일은 대부분 같은 핵심 결과를 확인합니다. 다만 내 코드에는 추가 출력과 실험이 있어 전체 출력 줄 수가 더 많습니다.

---

# 103. 내 코드와 강사님 코드 공통점

두 코드 모두 다음 내용을 포함합니다.

- `[]`와 `list()`로 빈 리스트 생성
- `range()`를 리스트로 변환
- `range()`의 인자 개수에 따른 차이
- `del`로 요소 삭제
- `+`, `+=`, `append()`로 요소 추가
- 리스트를 `append()`했을 때 중첩되는 결과
- `sort()`와 `reverse=True`
- 슬라이싱을 이용한 역순
- `reverse()`
- `pop()`
- `insert()`
- `extend()`
- `remove()`
- `index()`와 `count()`
- `clear()`
- 범위를 벗어난 슬라이싱
- 슬라이싱 대입
- 같은 객체 참조와 `copy()`
- 구조 분해 대입
- 리스트 직접 순회
- `enumerate()`
- 최댓값 확인
- 일반 반복문과 컴프리헨션
- `map(int, ...)`
- 2차원 리스트
- `[0] * 10`

---

# 104. 내 코드와 강사님 코드 차이

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 감소 `range()` | `range(10, 0, -1)` 추가 | 없음 |
| `append()` 설명 | JavaScript `push()` 및 중첩 의미 상세 | 핵심 결과 중심 |
| 정렬 설명 | 숫자 크기 정렬과 원본 변경 주석 | 오름차순·내림차순 중심 |
| `find()` | 리스트에 없음을 주석으로 확인 | 없음 |
| `clear()` 후 재대입 | `clear()`만 출력 | `clear()` 후 `a = []` |
| 끝 슬라이스 대입 | `a[len(a):] = [500]` 추가 | 없음 |
| 빈 리스트 평가 | `len()`과 `not len()` 확인 | 없음 |
| 복사 비교 | `is`, `==` 출력 추가 | 복사 후 값 변경까지만 |
| 최댓값 반복문 | 마지막 인덱스 조건 예제 추가 | 없음 |
| 두 배 컴프리헨션 | 없음 | `[i * 2 for i in range(10)]` |
| 짝수 컴프리헨션 | 짝수 값 자체 저장 | 구구단 문자열 저장 |
| `map()` 입력 | 새 실수 리스트를 다시 선언 | 직전 변환된 `a`를 그대로 사용 |
| 주석 양 | 세부 해석과 오류 설명이 많음 | 수업 핵심 중심으로 간결 |

---

# 105. 내 코드의 장점

- `range()`의 증가와 감소 방향을 직접 비교했습니다.
- `append()`와 `extend()`의 차이를 주석으로 구분했습니다.
- 존재하지 않는 값을 `remove()`하기 전에 `in`을 사용하는 방어 코드를 포함했습니다.
- 리스트에는 문자열의 `find()`가 없다는 점을 확인했습니다.
- 슬라이싱과 일반 인덱싱의 범위 초과 차이를 실험했습니다.
- 같은 객체 참조와 `copy()` 결과를 출력으로 비교했습니다.
- `is`와 `==`의 차이를 실제 리스트 객체로 확인했습니다.
- 일반 반복문과 컴프리헨션을 나란히 작성해 변환 과정을 이해하기 좋습니다.
- `enumerate()`를 이용해 실수 리스트를 직접 수정하는 과정을 포함했습니다.
- 2차원 리스트의 행 길이와 특정 요소 접근을 확인했습니다.

---

# 106. 내 코드의 개선점

- 주석에서 `len(f)`의 결과를 `False`라고 표현했지만 실제 반환값은 정수 `0`입니다.
- `reverse()`를 내림차순이라고 설명하면 일반적인 경우에는 부정확합니다. 현재 순서를 뒤집는 메서드입니다.
- `copy()`가 “모든 요소를 아예 복사”한다고 표현하면 중첩 리스트의 얕은 복사 한계를 놓칠 수 있습니다.
- `a[len(a):] = [500]`의 주석에서 당시 리스트 길이를 고정값 3으로 설명하면 앞선 변경 상태와 맞지 않을 수 있습니다.
- 최댓값 하나를 찾기 위해 리스트 전체를 정렬하면 원본 순서가 바뀌고 불필요한 작업이 생깁니다. `max()`가 더 직접적입니다.
- 마지막 요소를 찾기 위해 `range(len(a))` 전체를 순회할 필요는 없습니다. `a[-1]`을 사용할 수 있습니다.
- `list(i for ...)`보다 리스트 컴프리헨션 `[i for ...]`이 리스트 생성 의도를 더 직접적으로 보여 줍니다.
- 변수 이름 `a`, `b`, `c`, `d`가 반복되어 각 리스트의 역할을 파악하기 어렵습니다.
- 메서드별 실험을 같은 변수에 계속 이어서 수행해 중간 상태를 추적하기 어렵습니다.
- 출력 구분선이 `':='`와 `'-='` 등으로 달라 비교 시 불필요한 차이가 생깁니다.

---

# 107. 강사님 코드의 장점

- 리스트의 주요 메서드를 학습 순서대로 간결하게 배치했습니다.
- `range()`의 인자 개수에 따른 기본 규칙을 짧은 주석으로 정리했습니다.
- `append()`에 리스트를 전달했을 때 중첩 리스트가 되는 결과를 명확히 보여 줍니다.
- `insert()`의 범위 초과 동작을 직접 확인합니다.
- 일반 반복문, 컴프리헨션, 값 변환 컴프리헨션을 연속해서 비교합니다.
- `f'2x{i}={2*i}'`를 통해 컴프리헨션이 단순 숫자 복사뿐 아니라 문자열 생성에도 사용됨을 보여 줍니다.
- `enumerate()`와 `map()`을 짧은 코드로 소개합니다.
- 2차원 리스트 접근 예제가 간결합니다.

---

# 108. 강사님 코드의 개선점

- 감소하는 `range()` 예제가 없어 음수 `step`의 동작을 직접 확인하기 어렵습니다.
- `reverse()`가 정렬이 아니라 순서 반전이라는 설명이 부족합니다.
- `reversed()`와 `sorted()`의 차이는 다루지 않습니다.
- `copy()`가 얕은 복사라는 설명이 없습니다.
- `index()`와 `remove()`의 예외 종류를 구체적으로 설명하지 않습니다.
- `map()` 직전에 이미 `a`를 정수로 바꾼 뒤 다시 `map(int, a)`를 적용하여 변환 효과가 눈에 잘 드러나지 않습니다.
- 컴프리헨션 결과를 만드는 중간 코드가 일부 출력 없이 연속 재대입되어 각 단계 결과를 확인하기 어렵습니다.
- 변수 `b = 7`은 이후 최댓값 예제에서 사용되지 않습니다.
- 큐를 리스트로 구현할 때의 성능 문제나 `deque`는 다루지 않습니다.
- 중첩 리스트를 `*`로 생성할 때 참조 공유 문제가 생길 수 있다는 설명이 없습니다.

---

# 109. 개선된 대표 코드

```python
numbers = list(range(1, 6))

print("원본:", numbers)

numbers.append(6)
print("append:", numbers)

numbers.extend([7, 8])
print("extend:", numbers)

numbers.insert(0, 0)
print("insert:", numbers)

removed = numbers.pop()
print("pop 결과:", removed)
print("pop 이후:", numbers)

if 3 in numbers:
    numbers.remove(3)

print("remove 이후:", numbers)

ascending = sorted(numbers)
descending = sorted(
    numbers,
    reverse=True,
)

print("오름차순 새 리스트:", ascending)
print("내림차순 새 리스트:", descending)
print("원본 유지:", numbers)

copied = numbers.copy()

print("같은 객체:", numbers is copied)
print("같은 값:", numbers == copied)
```

이 예제는 다음 원칙을 반영합니다.

- 변수 이름으로 역할 표현
- 원본을 유지하려면 `sorted()` 사용
- 삭제 전 포함 여부 확인
- `pop()` 반환값 활용
- 객체 동일성과 값 동등성 분리

---

# 110. 개선된 컴프리헨션 예제

```python
numbers = list(range(10))

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

squared_even_numbers = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

labels = [
    f"{number}: 짝수"
    if number % 2 == 0
    else f"{number}: 홀수"
    for number in numbers
]

print(even_numbers)
print(squared_even_numbers)
print(labels)
```

컴프리헨션의 역할을 각각 분리해 변수 이름으로 표현했습니다.

---

# 111. 실무 활용 예제: 장바구니 항목 추가

```python
cart = []

cart.append({
    "name": "사과",
    "price": 1000,
    "quantity": 3,
})

cart.append({
    "name": "바나나",
    "price": 2000,
    "quantity": 2,
})

print(cart)
```

리스트는 여러 상품을 순서대로 저장하고, 각 상품은 이후 학습할 딕셔너리로 표현할 수 있습니다.

---

# 112. 실무 활용 예제: 입력값 정리

```python
raw_values = [
    " 10 ",
    "20",
    " 30",
]

numbers = [
    int(value.strip())
    for value in raw_values
]

print(numbers)
```

출력:

```text
[10, 20, 30]
```

문자열 메서드, 형 변환, 리스트 컴프리헨션을 함께 사용합니다.

---

# 113. 실무 활용 예제: 중복을 유지한 필터링

```python
scores = [55, 80, 90, 55, 70, 40]

passed_scores = [
    score
    for score in scores
    if score >= 60
]

print(passed_scores)
```

출력:

```text
[80, 90, 70]
```

리스트는 순서와 중복을 유지합니다.

중복 제거는 이후 집합 개념과 연결됩니다.

---

# 114. 실무 활용 예제: 번호와 함께 메뉴 출력

```python
menus = [
    "입금",
    "출금",
    "잔액 보기",
    "종료",
]

for number, menu in enumerate(
    menus,
    start=1,
):
    print(f"{number}. {menu}")
```

출력:

```text
1. 입금
2. 출금
3. 잔액 보기
4. 종료
```

사용자에게 보여 주는 번호는 1부터 시작하되 실제 리스트 인덱스는 0부터 유지할 수 있습니다.

---

# 115. 실무 활용 예제: 표 형태 데이터

```python
rows = [
    ["이름", "점수"],
    ["민수", 90],
    ["영희", 85],
]

for row in rows:
    print(
        " | ".join(
            map(str, row)
        )
    )
```

출력:

```text
이름 | 점수
민수 | 90
영희 | 85
```

숫자가 포함되어 있으므로 `map(str, row)`로 문자열 변환 후 `join()`합니다.

---

# 116. 자주 하는 실수: `append()`와 `extend()` 혼동

```python
numbers = [1, 2]
numbers.append([3, 4])
```

예상:

```text
[1, 2, 3, 4]
```

실제:

```text
[1, 2, [3, 4]]
```

내부 요소를 펼쳐 추가하려면:

```python
numbers.extend([3, 4])
```

---

# 117. 자주 하는 실수: `sort()` 결과를 다시 대입

잘못된 예:

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

# 118. 자주 하는 실수: `reverse()`를 내림차순 정렬로 이해

```python
numbers = [3, 1, 2]
numbers.reverse()
```

결과:

```text
[2, 1, 3]
```

내림차순이 필요하면:

```python
numbers.sort(reverse=True)
```

---

# 119. 자주 하는 실수: 없는 값을 바로 삭제

```python
numbers = [1, 2, 3]
numbers.remove(10)
```

오류:

```text
ValueError: list.remove(x): x not in list
```

개선:

```python
if 10 in numbers:
    numbers.remove(10)
```

---

# 120. 자주 하는 실수: 없는 값의 인덱스 조회

```python
numbers = [1, 2, 3]
position = numbers.index(10)
```

오류:

```text
ValueError: 10 is not in list
```

존재 여부만 필요하면:

```python
10 in numbers
```

인덱스가 필요하면 포함 여부를 먼저 확인합니다.

---

# 121. 자주 하는 실수: 범위를 벗어난 인덱스

```python
numbers = [1, 2, 3]
print(numbers[3])
```

오류:

```text
IndexError: list index out of range
```

마지막 요소:

```python
numbers[-1]
```

인덱스 유효성 확인:

```python
if 0 <= index < len(numbers):
    print(numbers[index])
```

---

# 122. 자주 하는 실수: 리스트 대입을 복사로 생각하기

```python
original = [1, 2, 3]
copied = original

copied[0] = 100
```

두 변수 모두 같은 변경을 확인합니다.

독립된 바깥 리스트가 필요하면:

```python
copied = original.copy()
```

중첩 구조까지 독립적으로 복사하려면 요구사항에 따라 `deepcopy()`를 검토합니다.

---

# 123. 자주 하는 실수: 얕은 복사로 중첩 리스트까지 독립적이라고 생각하기

```python
original = [[1], [2]]
copied = original.copy()

copied[0].append(100)

print(original)
```

출력:

```text
[[1, 100], [2]]
```

내부 리스트는 공유됩니다.

---

# 124. 자주 하는 실수: 빈 리스트에서 `pop()`

```python
stack = []
stack.pop()
```

오류:

```text
IndexError: pop from empty list
```

개선:

```python
if stack:
    value = stack.pop()
```

---

# 125. 자주 하는 실수: `range()`의 종료값 포함

```python
list(range(1, 5))
```

결과:

```text
[1, 2, 3, 4]
```

`5`는 포함되지 않습니다.

1부터 5까지 필요하면:

```python
range(1, 6)
```

---

# 126. 자주 하는 실수: 감소 범위에서 양수 `step`

```python
list(range(5, 0))
```

결과:

```text
[]
```

감소 방향:

```python
list(range(5, 0, -1))
```

---

# 127. 자주 하는 실수: 슬라이싱 대입에 단일 정수 사용

```python
numbers = [1, 2, 3]
numbers[3:] = 4
```

오류:

```text
TypeError
```

반복 가능한 형태로 작성합니다.

```python
numbers[3:] = [4]
```

단일 요소 추가가 목적이면:

```python
numbers.append(4)
```

---

# 128. 자주 하는 실수: `reversed()`를 바로 리스트처럼 출력

```python
numbers = [1, 2, 3]
result = reversed(numbers)

print(result)
```

반복자 객체 정보가 출력됩니다.

내용 확인:

```python
print(list(result))
```

---

# 129. 자주 하는 실수: 중첩 리스트를 곱셈으로 생성

```python
matrix = [[0] * 3] * 3
```

내부 행이 같은 리스트를 참조할 수 있습니다.

개선:

```python
matrix = [
    [0] * 3
    for _ in range(3)
]
```

---

# 130. 면접·복습 질문 1

## 리스트의 주요 특징은 무엇인가?

리스트는 순서를 유지하고 인덱스를 사용하며, 생성 후 요소를 추가·수정·삭제할 수 있는 변경 가능한 컬렉션입니다. 중복 값을 허용하고 서로 다른 자료형도 저장할 수 있습니다.

---

# 131. 면접·복습 질문 2

## `append()`와 `extend()`의 차이는 무엇인가?

`append()`는 전달한 객체 전체를 요소 하나로 추가합니다. `extend()`는 반복 가능한 객체의 각 요소를 하나씩 현재 리스트에 추가합니다.

---

# 132. 면접·복습 질문 3

## `sort()`와 `sorted()`의 차이는 무엇인가?

`sort()`는 리스트 원본을 변경하고 `None`을 반환합니다. `sorted()`는 원본을 유지하고 정렬된 새 리스트를 반환하며, 리스트 외의 반복 가능한 객체에도 사용할 수 있습니다.

---

# 133. 면접·복습 질문 4

## `reverse()`와 `sort(reverse=True)`의 차이는 무엇인가?

`reverse()`는 현재 요소 순서를 반대로 뒤집습니다. `sort(reverse=True)`는 값의 정렬 기준에 따라 내림차순으로 재배치합니다.

---

# 134. 면접·복습 질문 5

## `b = a`와 `b = a.copy()`의 차이는 무엇인가?

`b = a`는 두 변수가 같은 리스트 객체를 참조합니다. `b = a.copy()`는 바깥 리스트를 새로 만드는 얕은 복사이므로 바깥 리스트는 서로 다른 객체가 됩니다.

---

# 135. 면접·복습 질문 6

## 얕은 복사란 무엇인가?

새로운 바깥 컨테이너는 만들지만 내부에 포함된 중첩 객체의 참조는 그대로 공유하는 복사입니다. 내부 객체까지 독립적으로 복사하려면 깊은 복사가 필요할 수 있습니다.

---

# 136. 면접·복습 질문 7

## `range(10, 0, -1)`에서 0이 포함되지 않는 이유는 무엇인가?

`range()`의 `stop` 값은 증가 또는 감소 방향과 관계없이 포함되지 않는 종료 기준이기 때문입니다.

---

# 137. 면접·복습 질문 8

## 리스트 컴프리헨션의 기본 구조는 무엇인가?

```python
[표현식 for 변수 in 반복가능한객체]
```

조건 필터를 추가하면:

```python
[표현식 for 변수 in 반복가능한객체 if 조건식]
```

---

# 138. 면접·복습 질문 9

## `enumerate()`를 사용하는 이유는 무엇인가?

반복 가능한 객체를 순회하면서 현재 순번과 값을 함께 얻기 위해 사용합니다. `range(len(...))`와 인덱싱을 조합하는 것보다 의도가 명확한 경우가 많습니다.

---

# 139. 면접·복습 질문 10

## `map()`은 무엇을 반환하는가?

Python 3의 `map()`은 변환 결과를 순차적으로 제공하는 map 객체를 반환합니다. 리스트가 필요하면 `list(map(...))`로 변환합니다.

---

# 140. Problems

## 문제 1

다음 두 빈 리스트 생성 방식의 자료형을 출력하세요.

```python
a = []
b = list()
```

---

## 문제 2

`range()`를 이용해 다음 리스트를 만드세요.

```text
[1, 2, 3, 4, 5]
```

---

## 문제 3

`range()`를 이용해 다음 리스트를 만드세요.

```text
[10, 8, 6, 4, 2]
```

---

## 문제 4

다음 리스트에서 인덱스 `2`의 값을 출력하세요.

```python
numbers = [10, 20, 30, 40]
```

---

## 문제 5

다음 리스트의 마지막 값을 양수 인덱스를 계산하지 않고 출력하세요.

```python
numbers = [10, 20, 30, 40]
```

---

## 문제 6

다음 리스트에서 값 `30`을 `300`으로 수정하세요.

```python
numbers = [10, 20, 30, 40]
```

---

## 문제 7

다음 리스트의 인덱스 `1`부터 `3` 바로 앞까지 슬라이싱하세요.

```python
numbers = [0, 1, 2, 3, 4]
```

---

## 문제 8

다음 리스트에서 인덱스 `2`의 요소를 `del`로 삭제하세요.

```python
numbers = [10, 20, 30, 40]
```

---

## 문제 9

다음 리스트 끝에 숫자 `4`를 요소 하나로 추가하세요.

```python
numbers = [1, 2, 3]
```

---

## 문제 10

다음 리스트 뒤에 `[4, 5]`의 내부 요소를 각각 추가하세요.

```python
numbers = [1, 2, 3]
```

---

## 문제 11

다음 리스트의 인덱스 `1` 위치에 `15`를 추가하세요.

```python
numbers = [10, 20, 30]
```

---

## 문제 12

다음 리스트의 마지막 요소를 꺼내 `removed`에 저장하세요.

```python
numbers = [10, 20, 30]
```

---

## 문제 13

다음 리스트에서 처음 등장하는 값 `2`를 삭제하세요.

```python
numbers = [1, 2, 3, 2]
```

---

## 문제 14

값 `100`이 리스트에 있을 때만 삭제하도록 작성하세요.

```python
numbers = [10, 20, 30]
```

---

## 문제 15

다음 리스트에서 값 `4`가 등장하는 횟수를 출력하세요.

```python
numbers = [4, 1, 4, 2, 4]
```

---

## 문제 16

다음 리스트에서 값 `20`의 첫 번째 인덱스를 출력하세요.

```python
numbers = [10, 20, 30, 20]
```

---

## 문제 17

다음 리스트를 오름차순으로 정렬하되 원본을 유지하세요.

```python
numbers = [3, 1, 2]
```

---

## 문제 18

다음 리스트의 현재 순서를 원본에서 직접 반대로 뒤집으세요.

```python
numbers = [3, 1, 2]
```

---

## 문제 19

다음 리스트의 최댓값을 원본 정렬 없이 출력하세요.

```python
numbers = [7, 3, 5, 8, 4]
```

---

## 문제 20

다음 코드에서 `a`가 함께 바뀌는 이유를 설명하세요.

```python
a = [1, 2, 3]
b = a
b[0] = 100
```

---

## 문제 21

`a`의 바깥 리스트와 독립적인 새 리스트 `b`를 만드세요.

```python
a = [1, 2, 3]
```

---

## 문제 22

다음 리스트를 인덱스와 값으로 함께 출력하세요.

```python
names = ["민수", "영희", "철수"]
```

출력 예:

```text
0 민수
1 영희
2 철수
```

---

## 문제 23

번호를 1부터 시작해 메뉴를 출력하세요.

```python
menus = ["입금", "출금", "종료"]
```

출력 예:

```text
1 입금
2 출금
3 종료
```

---

## 문제 24

일반 반복문과 `append()`를 사용해 0부터 9까지의 리스트를 만드세요.

---

## 문제 25

리스트 컴프리헨션을 사용해 0부터 9까지의 리스트를 만드세요.

---

## 문제 26

리스트 컴프리헨션을 사용해 0부터 20 미만의 짝수 리스트를 만드세요.

---

## 문제 27

리스트 컴프리헨션을 사용해 1부터 5까지 각 숫자의 제곱을 저장하세요.

예상 결과:

```text
[1, 4, 9, 16, 25]
```

---

## 문제 28

다음 실수 리스트를 `map()`과 `int()`를 사용해 정수 리스트로 변환하세요.

```python
values = [1.2, 2.5, 3.7]
```

---

## 문제 29

다음 2차원 리스트에서 `40`을 출력하세요.

```python
matrix = [
    [10, 20],
    [30, 40],
    [50, 60],
]
```

---

## 문제 30

3행 4열의 모든 값이 0인 독립적인 2차원 리스트를 컴프리헨션으로 만드세요.

---

# 141. Answers

## 정답 1

```python
a = []
b = list()

print(type(a))
print(type(b))
```

---

## 정답 2

```python
numbers = list(range(1, 6))
print(numbers)
```

---

## 정답 3

```python
numbers = list(range(10, 0, -2))
print(numbers)
```

---

## 정답 4

```python
numbers = [10, 20, 30, 40]

print(numbers[2])
```

---

## 정답 5

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])
```

---

## 정답 6

```python
numbers = [10, 20, 30, 40]

numbers[2] = 300

print(numbers)
```

---

## 정답 7

```python
numbers = [0, 1, 2, 3, 4]

print(numbers[1:3])
```

---

## 정답 8

```python
numbers = [10, 20, 30, 40]

del numbers[2]

print(numbers)
```

---

## 정답 9

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

---

## 정답 10

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])

print(numbers)
```

---

## 정답 11

```python
numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
```

---

## 정답 12

```python
numbers = [10, 20, 30]

removed = numbers.pop()

print(numbers)
print(removed)
```

---

## 정답 13

```python
numbers = [1, 2, 3, 2]

numbers.remove(2)

print(numbers)
```

---

## 정답 14

```python
numbers = [10, 20, 30]

if 100 in numbers:
    numbers.remove(100)
```

---

## 정답 15

```python
numbers = [4, 1, 4, 2, 4]

print(numbers.count(4))
```

---

## 정답 16

```python
numbers = [10, 20, 30, 20]

print(numbers.index(20))
```

---

## 정답 17

```python
numbers = [3, 1, 2]

sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)
```

---

## 정답 18

```python
numbers = [3, 1, 2]

numbers.reverse()

print(numbers)
```

---

## 정답 19

```python
numbers = [7, 3, 5, 8, 4]

print(max(numbers))
```

---

## 정답 20

`b = a`는 새 리스트를 복사하지 않고 `a`와 `b`가 같은 리스트 객체를 참조하게 합니다. 따라서 `b[0]`을 수정하면 같은 객체를 보는 `a`에서도 변경이 확인됩니다.

---

## 정답 21

```python
a = [1, 2, 3]
b = a.copy()
```

---

## 정답 22

```python
names = ["민수", "영희", "철수"]

for index, name in enumerate(names):
    print(index, name)
```

---

## 정답 23

```python
menus = ["입금", "출금", "종료"]

for number, menu in enumerate(
    menus,
    start=1,
):
    print(number, menu)
```

---

## 정답 24

```python
numbers = []

for i in range(10):
    numbers.append(i)

print(numbers)
```

---

## 정답 25

```python
numbers = [
    i
    for i in range(10)
]

print(numbers)
```

---

## 정답 26

```python
even_numbers = [
    i
    for i in range(20)
    if i % 2 == 0
]

print(even_numbers)
```

---

## 정답 27

```python
squares = [
    number ** 2
    for number in range(1, 6)
]

print(squares)
```

---

## 정답 28

```python
values = [1.2, 2.5, 3.7]

numbers = list(map(int, values))

print(numbers)
```

---

## 정답 29

```python
matrix = [
    [10, 20],
    [30, 40],
    [50, 60],
]

print(matrix[1][1])
```

---

## 정답 30

```python
matrix = [
    [0] * 4
    for _ in range(3)
]

print(matrix)
```

---

# 142. Final Checklist

- [ ] `[]`와 `list()`로 리스트를 생성할 수 있다.
- [ ] 리스트가 순서와 인덱스를 가진 변경 가능한 자료형임을 설명할 수 있다.
- [ ] `range(stop)`의 범위를 설명할 수 있다.
- [ ] `range(start, stop)`에서 `stop`이 포함되지 않음을 안다.
- [ ] `range(start, stop, step)`으로 증가 및 감소 범위를 만들 수 있다.
- [ ] 리스트 인덱싱과 슬라이싱의 차이를 구분할 수 있다.
- [ ] 범위를 벗어난 인덱싱과 슬라이싱의 동작 차이를 안다.
- [ ] `del`로 요소 또는 범위를 삭제할 수 있다.
- [ ] `append()`와 `extend()`의 차이를 설명할 수 있다.
- [ ] `insert()`로 지정 위치에 값을 추가할 수 있다.
- [ ] `pop()`의 반환값을 활용할 수 있다.
- [ ] `remove()`가 첫 번째 일치 값만 삭제함을 안다.
- [ ] `index()`가 값이 없을 때 `ValueError`를 발생시킴을 안다.
- [ ] 리스트에는 문자열의 `find()`가 없음을 안다.
- [ ] `count()`와 `in`을 사용할 수 있다.
- [ ] `sort()`와 `sorted()`의 차이를 설명할 수 있다.
- [ ] `reverse()`와 내림차순 정렬을 구분할 수 있다.
- [ ] `reversed()`가 반복자를 반환함을 안다.
- [ ] 슬라이싱 대입에 반복 가능한 객체가 필요함을 안다.
- [ ] 빈 리스트의 Boolean 평가를 이해한다.
- [ ] `b = a`가 복사가 아니라 같은 객체 참조임을 설명할 수 있다.
- [ ] `copy()`가 얕은 복사임을 설명할 수 있다.
- [ ] 중첩 리스트에서 얕은 복사의 한계를 이해한다.
- [ ] `is`와 `==`의 차이를 리스트 예제로 설명할 수 있다.
- [ ] 구조 분해 대입을 사용할 수 있다.
- [ ] 리스트를 직접 순회할 수 있다.
- [ ] `enumerate()`로 번호와 값을 함께 얻을 수 있다.
- [ ] 최댓값만 필요할 때 `max()`를 사용할 수 있다.
- [ ] 일반 반복문과 리스트 컴프리헨션을 서로 변환할 수 있다.
- [ ] 조건이 있는 리스트 컴프리헨션을 작성할 수 있다.
- [ ] `map()`으로 요소의 자료형을 변환할 수 있다.
- [ ] 2차원 리스트의 행과 열에 접근할 수 있다.
- [ ] 3차원 리스트의 기본 접근 구조를 이해한다.
- [ ] 중첩 리스트를 `*`로 생성할 때 참조 공유를 주의한다.
- [ ] 리스트로 스택을 구현할 수 있다.
- [ ] 큐에는 필요에 따라 `deque`가 적절함을 안다.

---

# 143. Key Summary

```text
list
→ 순서를 유지하는 변경 가능한 컬렉션
→ 인덱스는 0부터 시작
→ 중복 허용
→ 서로 다른 자료형 저장 가능
```

```text
range(stop)
→ 0부터 stop 바로 앞까지

range(start, stop)
→ start부터 stop 바로 앞까지

range(start, stop, step)
→ step 간격으로 증가 또는 감소
```

```text
append(x)
→ x 전체를 요소 하나로 추가

extend(iterable)
→ 내부 요소를 하나씩 추가

insert(index, x)
→ 지정 위치에 추가
```

```text
del a[index]
→ 인덱스로 삭제

pop(index)
→ 인덱스로 삭제하고 삭제값 반환

remove(value)
→ 첫 번째 일치 값을 삭제

clear()
→ 모든 요소 삭제
```

```text
sort()
→ 원본 정렬
→ 반환값 None

sorted()
→ 원본 유지
→ 정렬된 새 리스트
```

```text
reverse()
→ 현재 순서를 원본에서 반전

reversed()
→ 역방향 반복자

a[::-1]
→ 역순 새 리스트
```

```text
b = a
→ 같은 리스트 객체 참조

b = a.copy()
→ 새로운 바깥 리스트
→ 얕은 복사
```

```text
a is b
→ 같은 객체인지 비교

a == b
→ 값이 같은지 비교
```

```text
[value for value in iterable]
→ 기본 리스트 컴프리헨션

[value for value in iterable if condition]
→ 조건 필터가 있는 컴프리헨션
```

```text
enumerate(iterable)
→ 인덱스와 값을 함께 순회

map(function, iterable)
→ 각 요소를 함수로 변환

matrix[row][column]
→ 2차원 리스트 접근
```

리스트는 Python에서 가장 자주 사용하는 자료 구조 중 하나입니다. 단순히 값을 모아 두는 데서 끝나지 않고, 반복문·조건문·컴프리헨션·함수와 결합해 데이터를 가공하는 핵심 기반이 됩니다.
