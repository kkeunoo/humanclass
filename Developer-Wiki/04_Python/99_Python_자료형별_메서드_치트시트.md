# Python 자료형별 메서드 치트시트

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `99_Python_자료형별_메서드_치트시트.md` |
| 분류 | `04_Python` |
| 문서 성격 | 수업 진도와 분리된 참고용 부록 |
| 핵심 범위 | str, list, tuple, dict, set, number, 내장 함수 |
| 학습 기준 | 사용 가능한 자료형, 반환 타입, 원본 변경 여부 |
| 보충 범위 | 자료형 변환 후 다른 자료형의 메서드를 연결해서 사용하는 방법 |

> 이 문서는 Python의 메서드를 단순히 암기하지 않고,  
> **어떤 자료형에 속한 기능인지**, **무엇을 반환하는지**,  
> **원본 객체를 직접 변경하는지**를 구분하기 위한 참고 문서입니다.

---

# 학습 목표

- 문자열, 리스트, 튜플, 딕셔너리, 집합의 메서드를 구분한다.
- 메서드의 반환 타입을 예상한다.
- 원본 변경 메서드와 새 값을 만드는 함수를 구분한다.
- 직접 사용할 수 없는 메서드는 자료형 변환 후 사용한다.
- Python과 JavaScript에서 호출 방향이 다른 메서드를 비교한다.
- 수업에서 자주 사용한 기능과 알아두면 좋은 기능을 함께 익힌다.

---

# 1. 가장 먼저 기억할 원칙

Python의 메서드는 자료형에 따라 사용할 수 있는 대상이 다릅니다.

```python
"HTML,CSS,Python".split(",")       # str 메서드
"-".join(["HTML", "CSS"])          # str 메서드
[1, 2, 3].append(4)                # list 메서드
{"name": "Kim"}.keys()             # dict 메서드
```

Python의 `join()`은 JavaScript와 호출 방향이 다릅니다.

```javascript
// JavaScript
["HTML", "CSS"].join("-")
```

```python
# Python
"-".join(["HTML", "CSS"])
```

Python에서는 **연결 문자로 사용할 문자열**이 `join()`을 호출합니다.

---

# 2. 표 읽는 방법

| 표시 | 의미 |
| --- | --- |
| ✅ | 해당 자료형에서 사용할 수 있음 |
| ❌ | 해당 자료형에서 직접 사용할 수 없음 |
| 🔴 변경 | 원본 객체를 직접 변경함 |
| 🟢 유지 | 원본 객체를 변경하지 않음 |
| ⭐ | 수업 또는 기초 학습에서 자주 사용 |
| 💡 | 아직 사용하지 않았더라도 알아두면 좋은 기능 |

> `str`, `tuple`, `int`, `float`는 불변 자료형입니다.  
> 메서드를 실행해도 원본 자체가 수정되는 것이 아니라 새로운 값을 반환합니다.

---

# 3. 한눈에 보는 소속별 핵심 표

| 메서드/함수 | str | list | tuple | set | dict | 반환 타입 | 원본 변경 |
| --- | :---: | :---: | :---: | :---: | :---: | --- | :---: |
| `split()` | ✅ | ❌ | ❌ | ❌ | ❌ | list | 🟢 유지 |
| `join()` | ✅ | ❌ | ❌ | ❌ | ❌ | str | 🟢 유지 |
| `replace()` | ✅ | ❌ | ❌ | ❌ | ❌ | str | 🟢 유지 |
| `strip()` | ✅ | ❌ | ❌ | ❌ | ❌ | str | 🟢 유지 |
| `find()` | ✅ | ❌ | ❌ | ❌ | ❌ | int | 🟢 유지 |
| `count()` | ✅ | ✅ | ✅ | ❌ | ❌ | int | 🟢 유지 |
| `index()` | ✅ | ✅ | ✅ | ❌ | ❌ | int | 🟢 유지 |
| `append()` | ❌ | ✅ | ❌ | ❌ | ❌ | `None` | 🔴 변경 |
| `extend()` | ❌ | ✅ | ❌ | ❌ | ❌ | `None` | 🔴 변경 |
| `insert()` | ❌ | ✅ | ❌ | ❌ | ❌ | `None` | 🔴 변경 |
| `remove()` | ❌ | ✅ | ❌ | ✅ | ❌ | `None` | 🔴 변경 |
| `pop()` | ❌ | ✅ | ❌ | ✅ | ✅ | 제거한 값 | 🔴 변경 |
| `sort()` | ❌ | ✅ | ❌ | ❌ | ❌ | `None` | 🔴 변경 |
| `reverse()` | ❌ | ✅ | ❌ | ❌ | ❌ | `None` | 🔴 변경 |
| `copy()` | ❌ | ✅ | ❌ | ✅ | ✅ | 같은 계열의 새 객체 | 🟢 유지 |
| `add()` | ❌ | ❌ | ❌ | ✅ | ❌ | `None` | 🔴 변경 |
| `update()` | ❌ | ❌ | ❌ | ✅ | ✅ | `None` | 🔴 변경 |
| `keys()` | ❌ | ❌ | ❌ | ❌ | ✅ | `dict_keys` | 🟢 유지 |
| `values()` | ❌ | ❌ | ❌ | ❌ | ✅ | `dict_values` | 🟢 유지 |
| `items()` | ❌ | ❌ | ❌ | ❌ | ✅ | `dict_items` | 🟢 유지 |
| `get()` | ❌ | ❌ | ❌ | ❌ | ✅ | 값 또는 기본값 | 🟢 유지 |

---

# 4. str 메서드

문자열은 순서를 가진 불변 시퀀스입니다.

```python
language = "Python"
```

## 4.1 str 메서드 표

| 메서드 | 반환 타입 | 원본 변경 | 설명 | 분류 |
| --- | --- | :---: | --- | :---: |
| `split()` | list | 🟢 유지 | 구분자로 문자열 분리 | ⭐ |
| `join()` | str | 🟢 유지 | 문자열 요소를 연결 | ⭐ |
| `replace()` | str | 🟢 유지 | 문자열 치환 | ⭐ |
| `strip()` | str | 🟢 유지 | 양쪽 공백 제거 | ⭐ |
| `lstrip()` | str | 🟢 유지 | 왼쪽 공백 제거 | 💡 |
| `rstrip()` | str | 🟢 유지 | 오른쪽 공백 제거 | 💡 |
| `find()` | int | 🟢 유지 | 위치 반환, 없으면 `-1` | ⭐ |
| `index()` | int | 🟢 유지 | 위치 반환, 없으면 예외 | 💡 |
| `count()` | int | 🟢 유지 | 등장 횟수 반환 | ⭐ |
| `startswith()` | bool | 🟢 유지 | 시작 문자열 확인 | 💡 |
| `endswith()` | bool | 🟢 유지 | 끝 문자열 확인 | 💡 |
| `upper()` | str | 🟢 유지 | 대문자 변환 | ⭐ |
| `lower()` | str | 🟢 유지 | 소문자 변환 | ⭐ |
| `capitalize()` | str | 🟢 유지 | 첫 문자를 대문자로 변환 | 💡 |
| `title()` | str | 🟢 유지 | 각 단어의 첫 글자를 대문자로 | 💡 |
| `isdigit()` | bool | 🟢 유지 | 숫자 문자로만 구성됐는지 | 💡 |
| `isalpha()` | bool | 🟢 유지 | 문자로만 구성됐는지 | 💡 |
| `isalnum()` | bool | 🟢 유지 | 문자 또는 숫자로만 구성됐는지 | 💡 |

## 4.2 `split()` — str에서 list로

```python
text = "HTML,CSS,Python"
languages = text.split(",")

print(languages)
print(type(languages))
```

출력:

```text
['HTML', 'CSS', 'Python']
<class 'list'>
```

자료형 흐름:

```text
str → split() → list
```

list로 바뀌었기 때문에 list 메서드를 사용할 수 있습니다.

```python
languages = "HTML,CSS,Python".split(",")
languages.append("Java")

print(languages)
```

## 4.3 `join()` — 반복 가능한 문자열 데이터를 str로

```python
languages = ["HTML", "CSS", "Python"]
result = " → ".join(languages)

print(result)
```

출력:

```text
HTML → CSS → Python
```

자료형 흐름:

```text
list[str] → str.join() → str
```

숫자가 포함되면 바로 연결할 수 없습니다.

```python
values = ["apple", 1000, 3]
# ", ".join(values)  # TypeError
```

문자열로 변환해야 합니다.

```python
values = ["apple", 1000, 3]
result = ", ".join(map(str, values))

print(result)
```

출력:

```text
apple, 1000, 3
```

## 4.4 문자열 처리 연결

```python
text = "  html, css, python  "

result = " → ".join(
    item.upper()
    for item in text.strip().split(", ")
)

print(result)
```

자료형 흐름:

```text
str
  ↓ strip()
str
  ↓ split()
list
  ↓ generator expression
문자열 iterable
  ↓ join()
str
```

---

# 5. list 메서드

list는 여러 값을 순서대로 저장하는 가변 자료형입니다.

```python
fruits = ["apple", "banana", "peach"]
```

## 5.1 list 메서드 표

| 메서드 | 반환 타입 | 원본 변경 | 설명 | 분류 |
| --- | --- | :---: | --- | :---: |
| `append()` | `None` | 🔴 변경 | 하나의 값을 마지막에 추가 | ⭐ |
| `extend()` | `None` | 🔴 변경 | iterable의 요소를 각각 추가 | ⭐ |
| `insert()` | `None` | 🔴 변경 | 지정 위치에 값 추가 | ⭐ |
| `remove()` | `None` | 🔴 변경 | 일치하는 첫 값을 삭제 | ⭐ |
| `pop()` | 제거한 값 | 🔴 변경 | 지정 위치의 값을 제거하고 반환 | ⭐ |
| `clear()` | `None` | 🔴 변경 | 전체 요소 삭제 | 💡 |
| `sort()` | `None` | 🔴 변경 | 원본 리스트 정렬 | ⭐ |
| `reverse()` | `None` | 🔴 변경 | 원본 리스트 순서 반전 | ⭐ |
| `copy()` | list | 🟢 유지 | 얕은 복사본 반환 | 💡 |
| `count()` | int | 🟢 유지 | 값의 개수 반환 | ⭐ |
| `index()` | int | 🟢 유지 | 값의 첫 위치 반환 | ⭐ |

## 5.2 반환값이 `None`인 메서드

```python
numbers = [1, 2, 3]
result = numbers.append(4)

print(numbers)
print(result)
```

출력:

```text
[1, 2, 3, 4]
None
```

다음처럼 작성하면 실수입니다.

```python
numbers = [1, 2, 3]
numbers = numbers.append(4)

print(numbers)
```

출력:

```text
None
```

## 5.3 `append()` vs `extend()`

```python
numbers = [1, 2]
numbers.append([3, 4])

print(numbers)
```

출력:

```text
[1, 2, [3, 4]]
```

```python
numbers = [1, 2]
numbers.extend([3, 4])

print(numbers)
```

출력:

```text
[1, 2, 3, 4]
```

| 구분 | `append()` | `extend()` |
| --- | --- | --- |
| 추가 단위 | 객체 하나 | iterable의 각 요소 |
| 원본 변경 | 예 | 예 |
| 반환 | `None` | `None` |

## 5.4 `sort()` vs `sorted()`

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

```python
numbers = [3, 1, 2]
result = sorted(numbers)

print(numbers)
print(result)
```

출력:

```text
[3, 1, 2]
[1, 2, 3]
```

| 구분 | `list.sort()` | `sorted()` |
| --- | --- | --- |
| 종류 | list 메서드 | 내장 함수 |
| 원본 변경 | 예 | 아니오 |
| 반환 | `None` | 새 list |
| 대상 | list만 | 여러 iterable |

---

# 6. tuple 메서드

tuple은 순서를 가진 불변 시퀀스입니다.

```python
numbers = (10, 20, 10, 30)
```

| 메서드 | 반환 타입 | 원본 변경 | 설명 |
| --- | --- | :---: | --- |
| `count()` | int | 🟢 유지 | 특정 값의 개수 |
| `index()` | int | 🟢 유지 | 특정 값의 첫 위치 |

tuple에는 `append()`, `remove()`, `sort()`가 없습니다.

list로 변환하여 수정할 수 있습니다.

```python
numbers = (1, 2, 3)

converted = list(numbers)
converted.append(4)
numbers = tuple(converted)

print(numbers)
```

자료형 흐름:

```text
tuple → list() → list → append() → tuple() → tuple
```

---

# 7. dict 메서드

dict는 키와 값의 쌍으로 데이터를 저장하는 가변 자료형입니다.

```python
user = {
    "name": "Kim",
    "age": 20,
    "job": "developer"
}
```

## 7.1 dict 메서드 표

| 메서드 | 반환 타입 | 원본 변경 | 설명 | 분류 |
| --- | --- | :---: | --- | :---: |
| `keys()` | `dict_keys` | 🟢 유지 | 키 뷰 반환 | ⭐ |
| `values()` | `dict_values` | 🟢 유지 | 값 뷰 반환 | ⭐ |
| `items()` | `dict_items` | 🟢 유지 | `(키, 값)` 뷰 반환 | ⭐ |
| `get()` | 값 또는 기본값 | 🟢 유지 | 안전하게 값 조회 | ⭐ |
| `update()` | `None` | 🔴 변경 | 여러 항목 추가·수정 | ⭐ |
| `pop()` | 제거한 값 | 🔴 변경 | 키를 삭제하고 값 반환 | ⭐ |
| `popitem()` | tuple | 🔴 변경 | 마지막 항목 삭제·반환 | 💡 |
| `setdefault()` | 값 | 조건부 변경 | 없으면 기본값 저장 | 💡 |
| `clear()` | `None` | 🔴 변경 | 전체 삭제 | 💡 |
| `copy()` | dict | 🟢 유지 | 얕은 복사 | 💡 |
| `fromkeys()` | dict | 🟢 유지 | 키들로 새 dict 생성 | 💡 |

## 7.2 dict의 키를 문자열로 연결

Python의 `dict.keys()`는 반복 가능한 `dict_keys`를 반환합니다.

```python
user = {
    "name": "Kim",
    "age": 20,
    "job": "developer"
}

result = ", ".join(user.keys())

print(result)
```

출력:

```text
name, age, job
```

`join()`은 list만 받는 것이 아니라 문자열로 이루어진 iterable을 받을 수 있습니다.

## 7.3 dict의 값을 문자열로 연결

값이 모두 문자열이면 바로 연결할 수 있습니다.

```python
user = {
    "name": "Kim",
    "job": "developer"
}

result = " / ".join(user.values())

print(result)
```

숫자가 포함된 경우 문자열로 변환해야 합니다.

```python
user = {
    "name": "Kim",
    "age": 20,
    "job": "developer"
}

result = " / ".join(map(str, user.values()))

print(result)
```

출력:

```text
Kim / 20 / developer
```

## 7.4 dict를 문장으로 변환

```python
user = {
    "name": "Kim",
    "age": 20,
    "job": "developer"
}

result = ", ".join(
    f"{key}: {value}"
    for key, value in user.items()
)

print(result)
```

출력:

```text
name: Kim, age: 20, job: developer
```

자료형 흐름:

```text
dict
  ↓ items()
dict_items
  ↓ comprehension
문자열 iterable
  ↓ join()
str
```

## 7.5 dict 필터링

```python
scores = {
    "html": 90,
    "css": 70,
    "javascript": 95,
    "python": 80
}

passed = {
    subject: score
    for subject, score in scores.items()
    if score >= 80
}

print(passed)
```

출력:

```text
{'html': 90, 'javascript': 95, 'python': 80}
```

## 7.6 `get()`과 대괄호 접근

```python
user = {"name": "Kim"}

print(user.get("age"))
print(user.get("age", 0))
```

출력:

```text
None
0
```

```python
print(user["age"])  # KeyError
```

존재하지 않을 수 있는 키는 `get()`으로 접근하면 안전합니다.

---

# 8. set 메서드

set은 중복을 허용하지 않는 가변 집합 자료형입니다.

```python
skills = {"HTML", "CSS", "Python"}
```

## 8.1 set 메서드 표

| 메서드 | 반환 타입 | 원본 변경 | 설명 | 분류 |
| --- | --- | :---: | --- | :---: |
| `add()` | `None` | 🔴 변경 | 값 하나 추가 | ⭐ |
| `update()` | `None` | 🔴 변경 | 여러 값 추가 | ⭐ |
| `remove()` | `None` | 🔴 변경 | 값을 삭제, 없으면 예외 | ⭐ |
| `discard()` | `None` | 🔴 변경 | 값을 삭제, 없어도 예외 없음 | 💡 |
| `pop()` | 제거한 값 | 🔴 변경 | 임의의 값 제거 | 💡 |
| `clear()` | `None` | 🔴 변경 | 전체 삭제 | 💡 |
| `copy()` | set | 🟢 유지 | 얕은 복사 | 💡 |
| `union()` | set | 🟢 유지 | 합집합 | ⭐ |
| `intersection()` | set | 🟢 유지 | 교집합 | ⭐ |
| `difference()` | set | 🟢 유지 | 차집합 | ⭐ |
| `issubset()` | bool | 🟢 유지 | 부분집합 여부 | 💡 |
| `issuperset()` | bool | 🟢 유지 | 상위집합 여부 | 💡 |
| `isdisjoint()` | bool | 🟢 유지 | 서로소 여부 | 💡 |

set에는 `join()` 메서드가 없습니다.

하지만 Python의 `str.join()`은 iterable을 받을 수 있으므로 문자열 set은 연결할 수 있습니다.

```python
skills = {"HTML", "CSS", "Python"}

result = ", ".join(sorted(skills))

print(result)
```

정렬하지 않으면 set의 출력 순서는 기대한 순서와 다를 수 있습니다.

자료형 흐름:

```text
set → sorted() → list → str.join() → str
```

---

# 9. 숫자 자료형과 관련 함수

Python의 `int`와 `float`는 문자열이나 리스트처럼 많은 변경 메서드를 제공하지 않습니다.

| 함수/메서드 | 입력 | 반환 타입 | 설명 |
| --- | --- | --- | --- |
| `int()` | 숫자·문자열 | int | 정수 변환 |
| `float()` | 숫자·문자열 | float | 실수 변환 |
| `str()` | 모든 객체 | str | 문자열 변환 |
| `round()` | 숫자 | int 또는 float | 반올림 |
| `abs()` | 숫자 | 숫자 | 절댓값 |
| `pow()` | 숫자 | 숫자 | 거듭제곱 |
| `divmod()` | 숫자 두 개 | tuple | 몫과 나머지 |
| `bit_length()` | int | int | 정수 표현에 필요한 비트 수 |

```python
price = 1234.567

print(round(price, 2))
print(f"{price:.2f}")
```

---

# 10. 알아두면 좋은 내장 함수

Python에서는 자료형 메서드 외에도 내장 함수를 자주 사용합니다.

| 함수 | 반환 타입 | 원본 변경 | 설명 |
| --- | --- | :---: | --- |
| `len()` | int | 🟢 유지 | 길이 |
| `type()` | type | 🟢 유지 | 자료형 확인 |
| `isinstance()` | bool | 🟢 유지 | 특정 자료형인지 확인 |
| `list()` | list | 🟢 유지 | list로 변환 |
| `tuple()` | tuple | 🟢 유지 | tuple로 변환 |
| `set()` | set | 🟢 유지 | set으로 변환 |
| `dict()` | dict | 🟢 유지 | dict 생성·변환 |
| `str()` | str | 🟢 유지 | 문자열 변환 |
| `sorted()` | list | 🟢 유지 | 정렬된 새 list |
| `reversed()` | iterator | 🟢 유지 | 역순 iterator |
| `enumerate()` | enumerate | 🟢 유지 | 인덱스와 값을 함께 제공 |
| `zip()` | zip | 🟢 유지 | 여러 iterable을 묶음 |
| `map()` | map | 🟢 유지 | 각 요소 변환 |
| `filter()` | filter | 🟢 유지 | 조건에 맞는 요소 선택 |
| `sum()` | 숫자 | 🟢 유지 | 합계 |
| `min()` | 요소 | 🟢 유지 | 최솟값 |
| `max()` | 요소 | 🟢 유지 | 최댓값 |
| `any()` | bool | 🟢 유지 | 하나라도 참인지 |
| `all()` | bool | 🟢 유지 | 모두 참인지 |

## 10.1 `enumerate()`

```python
languages = ["HTML", "CSS", "Python"]

for index, language in enumerate(languages, start=1):
    print(index, language)
```

## 10.2 `zip()`

```python
subjects = ["HTML", "CSS", "Python"]
scores = [90, 80, 95]

result = dict(zip(subjects, scores))

print(result)
```

출력:

```text
{'HTML': 90, 'CSS': 80, 'Python': 95}
```

자료형 흐름:

```text
list + list → zip() → zip 객체 → dict() → dict
```

## 10.3 `map()`과 `filter()`

```python
numbers = [1, 2, 3, 4, 5]

result = list(
    map(
        lambda number: number * 10,
        filter(lambda number: number % 2 == 1, numbers)
    )
)

print(result)
```

초기 학습에서는 리스트 컴프리헨션이 더 읽기 쉬운 경우가 많습니다.

```python
result = [
    number * 10
    for number in numbers
    if number % 2 == 1
]
```

---

# 11. 자주 헷갈리는 기능 비교

## 11.1 `split()` vs `join()`

| 구분 | `split()` | `join()` |
| --- | --- | --- |
| 소속 | str | str |
| 호출 대상 | 분리할 문자열 | 연결 문자 |
| 변환 | str → list | 문자열 iterable → str |
| 원본 변경 | 없음 | 없음 |

```python
array = "HTML,CSS".split(",")
string = ",".join(["HTML", "CSS"])
```

## 11.2 `append()` vs `extend()`

| 구분 | `append()` | `extend()` |
| --- | --- | --- |
| 추가 | 객체 하나 | 각 요소 |
| 반환 | `None` | `None` |
| 원본 변경 | 있음 | 있음 |

## 11.3 `remove()` vs `pop()`

| 구분 | `remove(value)` | `pop(index)` |
| --- | --- | --- |
| 기준 | 값 | 위치 |
| 반환 | `None` | 제거한 값 |
| 원본 변경 | 있음 | 있음 |

## 11.4 `find()` vs `index()`

| 구분 | `find()` | `index()` |
| --- | --- | --- |
| 없을 때 | `-1` | `ValueError` |
| 반환 | int | int |
| 사용 대상 | str | str, list, tuple |

## 11.5 `dict.get()` vs `dict[key]`

| 구분 | `get()` | 대괄호 접근 |
| --- | --- | --- |
| 키 없음 | `None` 또는 기본값 | `KeyError` |
| 키 있음 | 값 | 값 |

## 11.6 `set.remove()` vs `set.discard()`

| 구분 | `remove()` | `discard()` |
| --- | --- | --- |
| 값 없음 | `KeyError` | 오류 없음 |
| 원본 변경 | 있음 | 있음 |

---

# 12. 자료형 변환 연결 예제

## 12.1 dict → 문자열

```python
product = {
    "name": "keyboard",
    "price": 50000,
    "stock": 3
}

summary = " | ".join(
    f"{key}={value}"
    for key, value in product.items()
)

print(summary)
```

출력:

```text
name=keyboard | price=50000 | stock=3
```

## 12.2 str → list → 필터링 → str

```python
text = "apple, banana, peach, kiwi"

result = " / ".join(
    fruit.upper()
    for fruit in text.split(", ")
    if len(fruit) >= 5
)

print(result)
```

출력:

```text
APPLE / BANANA / PEACH
```

## 12.3 set → list → str

```python
tags = {"python", "html", "python", "css"}

result = ", ".join(sorted(tags))

print(result)
```

## 12.4 tuple → list → 수정 → tuple

```python
numbers = (1, 2, 3)

converted = list(numbers)
converted.append(4)
result = tuple(converted)

print(result)
```

## 12.5 두 list → dict → 문자열

```python
keys = ["name", "age", "job"]
values = ["Kim", 20, "developer"]

user = dict(zip(keys, values))

summary = ", ".join(
    f"{key}: {value}"
    for key, value in user.items()
)

print(summary)
```

## 12.6 list[dict] → 필터링 → 문자열

```python
products = [
    {"name": "apple", "price": 1000},
    {"name": "banana", "price": 2000},
    {"name": "peach", "price": 1500}
]

result = ", ".join(
    product["name"]
    for product in products
    if product["price"] >= 1500
)

print(result)
```

출력:

```text
banana, peach
```

---

# 13. 오류를 만났을 때 확인 순서

다음 오류가 나왔다고 가정합니다.

```text
AttributeError: 'dict' object has no attribute 'append'
```

확인 순서:

1. 변수의 현재 자료형을 확인한다.
2. 사용한 메서드가 어느 자료형에 속하는지 확인한다.
3. 다른 자료형으로 변환해서 사용할 수 있는지 확인한다.
4. 메서드의 반환값이 `None`인지 확인한다.
5. 원본을 변경하는 메서드인지 확인한다.

```python
print(value)
print(type(value))
print(isinstance(value, list))
```

dict에 새 키와 값을 추가하려는 목적이라면:

```python
user["age"] = 20
```

여러 항목을 추가하려면:

```python
user.update({
    "age": 20,
    "job": "developer"
})
```

dict의 값들을 list처럼 처리하려면:

```python
values = list(user.values())
values.append("new value")
```

다만 이 list를 수정해도 원래 dict가 자동으로 변경되는 것은 아닙니다.

---

# 14. 최종 체크리스트

- [ ] `split()`이 str을 list로 바꾼다는 것을 안다.
- [ ] Python의 `join()` 호출 방향을 설명할 수 있다.
- [ ] `append()`, `extend()`, `sort()`가 `None`을 반환한다는 것을 안다.
- [ ] tuple은 직접 수정할 수 없다는 것을 안다.
- [ ] `dict.keys()`, `values()`, `items()`의 차이를 안다.
- [ ] dict의 숫자 값을 `join()`하려면 `str` 변환이 필요함을 안다.
- [ ] set의 순서를 보장할 수 없으므로 필요하면 `sorted()`를 사용한다.
- [ ] `sort()`와 `sorted()`의 원본 변경 차이를 안다.
- [ ] `remove()`와 `pop()`의 반환값 차이를 안다.
- [ ] 메서드 체이닝과 변환 과정에서 현재 자료형을 추적할 수 있다.

---

# 핵심 요약

```text
str.split() : str → list
str.join()  : 문자열 iterable → str

list.append() : 원본 변경, 반환 None
list.extend() : 원본 변경, 반환 None
list.sort()   : 원본 변경, 반환 None
sorted()      : 원본 유지, 새 list 반환

dict.keys()   : dict_keys
dict.values() : dict_values
dict.items()  : dict_items

list()  : iterable → list
tuple() : iterable → tuple
set()   : iterable → set
dict()  : 키-값 데이터 → dict

enumerate() : 인덱스와 값
zip()       : 여러 iterable 묶기
map()       : 요소 변환
filter()    : 요소 선택
```

메서드 이름만 외우기보다 다음 세 가지를 함께 기억합니다.

```text
1. 어떤 자료형에서 사용하는가?
2. 무엇을 반환하는가?
3. 원본을 변경하는가?
```
