# Python 시퀀스와 슬라이싱

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `06_Python_시퀀스와_슬라이싱.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `03_Python_문자열과_포매팅.md`, `04_Python_리스트와_컴프리헨션.md`, `05_Python_튜플과_불변자료형.md` |
| 다음 학습 | `07_Python_딕셔너리.md` |
| 원본 기준 | `workspace_python/06_sequence.py`, `workspace_teacher/workspace_python/_06_sequence.py` |
| 핵심 범위 | 시퀀스 공통 연산, `in`, `not in`, 연결, 반복, `len()`, UTF-8 인코딩, 인덱싱, 음수 인덱스, 슬라이싱, 슬라이스 대입, 역순 |
| 보충 범위 | 가변·불변 시퀀스, `range`, `slice`, `reversed()`, 얕은 복사, 다국어 데이터 연결 방식 |

> 이 문서는 내 코드의 `06_sequence.py`와 강사님 코드의 `_06_sequence.py`를 직접 비교해 작성했습니다. 원본에서 직접 확인할 수 있는 내용과 문서 이해를 위해 덧붙인 확장 학습을 구분해 설명합니다.

---

# 학습 목표

- Python에서 시퀀스가 무엇인지 설명할 수 있다.
- 문자열, 리스트, 튜플, `range`의 공통점과 차이점을 구분할 수 있다.
- `in`과 `not in`으로 요소 포함 여부를 확인할 수 있다.
- 같은 종류의 시퀀스를 `+`로 연결할 수 있다.
- 시퀀스에 정수를 곱해 반복된 새 시퀀스를 만들 수 있다.
- `len()`으로 시퀀스의 요소 개수를 구할 수 있다.
- 문자열의 문자 수와 UTF-8 바이트 수가 다를 수 있음을 설명할 수 있다.
- 양수 인덱스와 음수 인덱스로 요소에 접근할 수 있다.
- 범위를 벗어난 인덱싱이 `IndexError`를 발생시키는 이유를 안다.
- 슬라이싱의 `start`, `stop`, `step`을 설명할 수 있다.
- 슬라이싱에서 `stop`이 포함되지 않는다는 점을 이해한다.
- 음수 `step`을 이용해 역방향 슬라이싱을 작성할 수 있다.
- 일반 인덱싱과 슬라이싱의 범위 초과 동작 차이를 구분할 수 있다.
- 리스트의 슬라이스 대입으로 범위를 교체할 수 있다.
- 슬라이스 대입에서 교체 범위와 새 요소 개수가 달라도 되는 이유를 설명할 수 있다.
- 문자열과 튜플이 불변 시퀀스이고 리스트가 가변 시퀀스임을 안다.
- `[::-1]`이 원본을 변경하지 않고 역순의 새 시퀀스를 만든다는 점을 설명할 수 있다.
- 내 코드와 강사님 코드의 차이 및 개선점을 정리할 수 있다.

---

# 1. 원본 코드

## 1.1 내 코드

```python
a = [0, 10, 20, 30, 40] 
print(20 in a)                 # True
print(200 in a)                # False
print(not (200 in a))          # ! 대신 not 사용
print(200 not in a)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# range + range는 불가하지만,
# list나 tuple로 바꾸면 합칠 수 있음
print(c)

a = "hello"
b = "world"
c = a + b
print(c)

# JavaScript에서는 가능하지만,
# Python은 sequence끼리만 가능함
# c = a + 3
c = a + str(3)
print(c)

print("-" * 10)

print(len(a))
# len으로 감싸면 길이를 구할 수 있다
# 문자, 숫자, 튜플 등

hello = "안녕하세요"
b = hello.encode("utf-8")
print(len(b))
print(b)
print(hello[0])                # "안"

a = [1, 2, 3, 4]
print(a[0])                    # 1
print(a[-2])                   # 3

# IndexError: list index out of range
# print(a[100])

a = (1, 2, 3)
print(a[0])

# tuple은 readonly 형태이기 때문에 값은 바꿀 수 없다
# a[0] = 3

a = [1, 2, 3]
del a[0]
print(a)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:4])
print(a[4:-1])
print(a[4:100])

print(a[1:9:2])

print(a[:7])
print(a[5:])
print(a[:])

print(a[7:3])
print(a[7:3:-1])
print(a[8:4:-1])

print(a[-4:8])
print(a[-4:-2])

print(a)

a[2:5] = ["a", "b", "c"]
print(a)

print(a[2:5])

a[2:5] = [10, 20, 30, 40, 50]
print(a)

ko = ["책", "알약", "철판"]
en = ["book", "pill", "plate"]

view = ko
view = en

print(view[0])

a = "hello"
print(a[::-1])
```

## 1.2 강사님 코드

```python
a = [0, 10, 20, 30, 40]
print(20 in a)
print(200 in a)
print(not (200 in a))
print(200 not in a)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

a = "hello"
b = "world"
c = a + b
print(c)

# c = a + 3
c = a + str(3)
print(c)

print("-" * 10)

print(len(a))

hello = "안녕하세요"
b = hello.encode("utf-8")
print(len(b))
print(b)
print(hello[0])

a = [1, 2, 3, 4]
print(a[0])
print(a[-2])

a[0] = 2

# print(a[100])  # IndexError

a = (1, 2, 3)
print(a[0])

# a[0] = 3
# 튜플의 값은 바꿀 수 없다

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:4])
print(a[4:-1])
print(a[4:100])

print(a[1:9:2])

print(a[:7])
print(a[5:])
print(a[:])

print(a[7:3])
print(a[7:3:-1])
print(a[8:4:-1])

print(a[-4:8])
print(a[-4:-2])

print(a)

a[2:5] = ["a", "b", "c"]
print(a)

print(a[2:5])

a[2:5] = [10, 20, 30, 40, 50]
print(a)

ko = ["책", "알약", "철판"]
en = ["book", "pill", "plate"]

view = ko
view = en

print(view[0])

a = "hello"  # olleh
# a = "TENET"

print(a[::-1])
```

---

# 2. 원본 실행 결과

두 파일의 핵심 출력은 거의 같습니다.

```text
True
False
True
True
[1, 2, 3, 4, 5, 6]
helloworld
hello3
----------
6
15
b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'
안
1
3
1
[2, 3]
[1, 2, 3]
[4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
[1, 3, 5, 7]
[0, 1, 2, 3, 4, 5, 6]
[5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[]
[7, 6, 5, 4]
[8, 7, 6, 5]
[6, 7]
[6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 'a', 'b', 'c', 5, 6, 7, 8, 9]
['a', 'b', 'c']
[0, 1, 10, 20, 30, 40, 50, 5, 6, 7, 8, 9]
book
olleh
```

강사님 코드에는 리스트 요소 변경 예제가 하나 더 있습니다.

```python
a[0] = 2
```

하지만 변경된 리스트를 바로 출력하지 않으므로 실행 결과에서 확인되지는 않습니다.

---

# 3. 시퀀스란?

시퀀스(sequence)는 여러 요소가 일정한 순서로 나열되어 있고, 각 요소에 위치를 나타내는 인덱스를 사용할 수 있는 자료형입니다.

대표적인 Python 시퀀스:

```text
str
list
tuple
range
bytes
bytearray
```

현재 학습 단계에서 가장 중요한 시퀀스는 다음 네 가지입니다.

| 자료형 | 예 | 변경 가능 여부 |
| --- | --- | --- |
| 문자열 `str` | `"hello"` | 불변 |
| 리스트 `list` | `[1, 2, 3]` | 가변 |
| 튜플 `tuple` | `(1, 2, 3)` | 불변 |
| 범위 `range` | `range(5)` | 불변 |

---

# 4. 시퀀스의 공통 기능

문자열, 리스트, 튜플, `range`는 다음과 같은 공통 기능을 가집니다.

```text
길이 확인
포함 여부 확인
인덱싱
슬라이싱
반복문 순회
일부 자료형의 연결
일부 자료형의 반복
```

예:

```python
text = "Python"
numbers = [10, 20, 30]
point = (100, 200)
indexes = range(5)
```

모두 `len()`을 사용할 수 있습니다.

```python
print(len(text))
print(len(numbers))
print(len(point))
print(len(indexes))
```

---

# 5. 순서가 있다는 의미

시퀀스는 요소의 위치가 중요합니다.

```python
numbers = [10, 20, 30]
```

다음 두 리스트는 같은 요소를 포함하지만 순서가 다릅니다.

```python
a = [10, 20, 30]
b = [30, 20, 10]

print(a == b)
```

출력:

```text
False
```

시퀀스에서 순서는 값의 일부입니다.

---

# 6. `in` 연산자

공통 원본:

```python
a = [0, 10, 20, 30, 40]

print(20 in a)
print(200 in a)
```

출력:

```text
True
False
```

`in`은 왼쪽 값이 오른쪽 객체 안에 포함되어 있는지 확인합니다.

```python
값 in 시퀀스
```

결과는 Boolean입니다.

---

# 7. `not in` 연산자

공통 원본:

```python
print(200 not in a)
```

출력:

```text
True
```

`not in`은 값이 포함되어 있지 않을 때 `True`입니다.

```python
값 not in 시퀀스
```

---

# 8. `not (값 in 시퀀스)`

공통 원본:

```python
print(not (200 in a))
```

출력:

```text
True
```

다음 두 표현은 같은 논리 결과를 만듭니다.

```python
not (200 in a)
200 not in a
```

보통 포함되지 않음을 표현할 때는 `not in`이 더 직접적입니다.

```python
if target not in numbers:
    print("값이 없습니다.")
```

---

# 9. Python의 논리 부정 연산자

내 코드 주석:

```python
# ! 대신 not 사용
```

Python에서는 논리 부정에 `not`을 사용합니다.

```python
not True
not False
```

`!` 단독은 Python 논리 부정 연산자가 아닙니다.

단, `!=`는 같지 않음을 비교하는 연산자입니다.

```python
10 != 20
```

---

# 10. 문자열에서 `in`

```python
text = "hello world"

print("hello" in text)
print("Python" in text)
```

출력:

```text
True
False
```

문자열에서는 한 문자뿐 아니라 연속된 부분 문자열도 검색할 수 있습니다.

```python
print("lo wo" in text)
```

출력:

```text
True
```

---

# 11. 리스트와 튜플에서 `in`

```python
numbers = [10, 20, 30]
point = (100, 200)

print(20 in numbers)
print(100 in point)
```

`in`은 각 요소와 값을 비교합니다.

중첩된 내부 요소까지 자동으로 재귀 검색하지는 않습니다.

```python
data = [[1, 2], [3, 4]]

print(1 in data)
print([1, 2] in data)
```

출력:

```text
False
True
```

---

# 12. `range`에서 `in`

```python
numbers = range(0, 10, 2)

print(4 in numbers)
print(5 in numbers)
```

출력:

```text
True
False
```

`range`도 시퀀스이므로 포함 여부를 확인할 수 있습니다.

---

# 13. 시퀀스 연결 `+`

공통 원본:

```python
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)
```

출력:

```text
[1, 2, 3, 4, 5, 6]
```

`+`는 두 리스트의 요소를 순서대로 연결한 새 리스트를 만듭니다.

기존 리스트는 변경되지 않습니다.

---

# 14. 문자열 연결

공통 원본:

```python
a = "hello"
b = "world"

c = a + b

print(c)
```

출력:

```text
helloworld
```

공백이 자동으로 추가되지는 않습니다.

공백이 필요하면 직접 포함해야 합니다.

```python
c = a + " " + b
```

---

# 15. 튜플 연결

```python
a = (1, 2, 3)
b = (4, 5, 6)

c = a + b

print(c)
```

출력:

```text
(1, 2, 3, 4, 5, 6)
```

튜플 연결도 새로운 튜플을 만듭니다.

---

# 16. 같은 종류의 시퀀스끼리 연결

내 코드 주석:

```python
# Python은 sequence 끼리만 가능함
```

이 설명은 조금 더 정확하게 다듬어야 합니다.

모든 시퀀스가 서로 자유롭게 연결되는 것은 아닙니다.

다음 코드는 오류입니다.

```python
[1, 2] + (3, 4)
```

```python
"hello" + ["world"]
```

같은 연결 규칙을 지원하는 호환 가능한 자료형끼리 연결해야 합니다.

```python
[1, 2] + [3, 4]
(1, 2) + (3, 4)
"hello" + "world"
```

---

# 17. 문자열과 숫자의 직접 연결

공통 원본의 주석 처리된 코드:

```python
# c = a + 3
```

문자열과 정수를 직접 더하면 오류가 발생합니다.

```text
TypeError: can only concatenate str (not "int") to str
```

Python은 숫자를 자동으로 문자열로 바꾸지 않습니다.

---

# 18. `str()`로 문자열 변환 후 연결

공통 원본:

```python
c = a + str(3)

print(c)
```

출력:

```text
hello3
```

정수를 문자열로 명시적으로 변환한 뒤 연결합니다.

```python
"hello" + str(3)
```

---

# 19. f-string을 이용한 연결

문자열과 다른 자료형을 함께 출력할 때는 f-string이 더 읽기 좋을 수 있습니다.

```python
word = "hello"
number = 3

result = f"{word}{number}"

print(result)
```

출력:

```text
hello3
```

이 내용은 원본에 직접 등장하지 않는 개선 예입니다.

---

# 20. `range + range`는 지원되지 않는다

내 코드 주석:

```python
# range + range는 불가
```

다음 코드는 오류가 발생합니다.

```python
range(3) + range(3, 6)
```

`range`는 일반 시퀀스 공통 기능을 많이 지원하지만 `+` 연결과 `*` 반복을 지원하지 않습니다.

리스트로 변환하면 연결할 수 있습니다.

```python
result = list(range(3)) + list(range(3, 6))
```

결과:

```text
[0, 1, 2, 3, 4, 5]
```

---

# 21. 시퀀스 반복 `*`

공통 원본:

```python
print("-" * 10)
```

출력:

```text
----------
```

문자열에 정수를 곱하면 해당 문자열이 반복된 새 문자열을 만듭니다.

```python
print("ab" * 3)
```

출력:

```text
ababab
```

---

# 22. 리스트 반복

```python
numbers = [1, 2] * 3

print(numbers)
```

출력:

```text
[1, 2, 1, 2, 1, 2]
```

원본 리스트를 변경하는 것이 아니라 새 리스트를 생성합니다.

---

# 23. 튜플 반복

```python
values = ("A", "B") * 2

print(values)
```

출력:

```text
('A', 'B', 'A', 'B')
```

---

# 24. `range`는 반복 연산을 지원하지 않는다

```python
range(3) * 2
```

오류:

```text
TypeError: unsupported operand type(s) for *: 'range' and 'int'
```

필요하다면 다른 시퀀스로 변환합니다.

```python
list(range(3)) * 2
```

---

# 25. `len()` 함수

공통 원본:

```python
print(len(a))
```

당시 `a`는 `"hello3"`이므로 출력은 다음과 같습니다.

```text
6
```

`len()`은 객체의 요소 개수를 반환합니다.

```python
len("hello")
len([1, 2, 3])
len((1, 2, 3))
len(range(10))
```

---

# 26. 숫자에는 `len()`을 사용할 수 없다

내 코드 주석에는 다음 표현이 있습니다.

```python
# 문자, 숫자, 튜플 등
```

이 중 “숫자” 부분은 부정확합니다.

다음 코드는 오류입니다.

```python
len(123)
```

오류:

```text
TypeError: object of type 'int' has no len()
```

`len()`은 길이 개념을 제공하는 객체에 사용합니다.

---

# 27. 문자열의 길이

```python
text = "hello"

print(len(text))
```

출력:

```text
5
```

문자열에서는 Python이 인식하는 문자 단위의 개수를 반환합니다.

---

# 28. 한글 문자열 길이

```python
hello = "안녕하세요"

print(len(hello))
```

출력:

```text
5
```

한글 다섯 글자가 있으므로 문자 길이는 5입니다.

---

# 29. UTF-8 인코딩

공통 원본:

```python
hello = "안녕하세요"
b = hello.encode("utf-8")

print(len(b))
print(b)
```

UTF-8 바이트 수는 다음과 같습니다.

```text
15
```

일반적인 한글 음절 하나가 UTF-8에서 3바이트로 인코딩되므로 다섯 글자는 15바이트입니다.

---

# 30. 문자열과 바이트열의 차이

```python
hello = "안녕하세요"
encoded = hello.encode("utf-8")
```

| 값 | 자료형 | 길이 기준 |
| --- | --- | --- |
| `hello` | `str` | 문자 개수 |
| `encoded` | `bytes` | 바이트 개수 |

```python
print(type(hello))
print(type(encoded))
```

출력:

```text
<class 'str'>
<class 'bytes'>
```

---

# 31. 인코딩 결과 출력

공통 원본:

```python
print(b)
```

출력은 다음과 비슷합니다.

```text
b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'
```

앞의 `b`는 `bytes` 객체임을 나타냅니다.

`\x..`는 각 바이트 값을 16진수 형태로 표현한 것입니다.

---

# 32. 디코딩

바이트열을 다시 문자열로 바꾸려면 같은 문자 인코딩을 사용해 디코딩합니다.

```python
decoded = b.decode("utf-8")

print(decoded)
```

출력:

```text
안녕하세요
```

인코딩과 디코딩:

```text
str
→ encode()
→ bytes

bytes
→ decode()
→ str
```

---

# 33. 문자 수와 저장 크기는 다르다

```python
text = "안녕하세요"

print(len(text))
print(len(text.encode("utf-8")))
```

출력:

```text
5
15
```

`len(str)`은 문자 수를, `len(bytes)`는 바이트 수를 반환합니다.

파일 크기나 네트워크 전송 크기를 다룰 때 이 차이가 중요합니다.

---

# 34. 인덱싱

인덱싱은 시퀀스에서 특정 위치의 요소 하나를 가져오는 기능입니다.

```python
시퀀스[인덱스]
```

첫 번째 요소의 인덱스는 `0`입니다.

---

# 35. 문자열 인덱싱

공통 원본:

```python
hello = "안녕하세요"

print(hello[0])
```

출력:

```text
안
```

문자열도 시퀀스이므로 각 문자에 인덱스로 접근할 수 있습니다.

---

# 36. 리스트 인덱싱

공통 원본:

```python
a = [1, 2, 3, 4]

print(a[0])
```

출력:

```text
1
```

양수 인덱스:

| 인덱스 | 값 |
| ---: | ---: |
| `0` | `1` |
| `1` | `2` |
| `2` | `3` |
| `3` | `4` |

---

# 37. 음수 인덱스

공통 원본:

```python
print(a[-2])
```

출력:

```text
3
```

음수 인덱스는 뒤에서부터 위치를 셉니다.

| 음수 인덱스 | 값 |
| ---: | ---: |
| `-1` | `4` |
| `-2` | `3` |
| `-3` | `2` |
| `-4` | `1` |

---

# 38. 양수와 음수 인덱스의 대응

길이가 4인 시퀀스:

```text
값       1   2   3   4
양수     0   1   2   3
음수    -4  -3  -2  -1
```

다음 두 표현은 같은 요소를 가리킵니다.

```python
a[2]
a[-2]
```

---

# 39. 범위를 벗어난 인덱스

공통 원본의 주석 처리된 코드:

```python
# print(a[100])
```

실행하면 다음 오류가 발생합니다.

```text
IndexError: list index out of range
```

존재하지 않는 요소 하나를 요청했기 때문입니다.

---

# 40. JavaScript와 범위 초과 접근 차이

내 코드 주석:

```python
# JavaScript만 undefined
```

일반적인 JavaScript 배열에서 없는 인덱스를 읽으면 `undefined`가 나올 수 있지만 Python 리스트는 `IndexError`를 발생시킵니다.

Python에서는 오류를 통해 잘못된 위치 접근을 즉시 확인할 수 있습니다.

---

# 41. 문자열 범위 초과 인덱스

```python
text = "hello"

print(text[100])
```

오류:

```text
IndexError: string index out of range
```

시퀀스 종류에 따라 오류 메시지의 자료형 이름이 달라집니다.

---

# 42. 튜플 인덱싱

공통 원본:

```python
a = (1, 2, 3)

print(a[0])
```

출력:

```text
1
```

튜플도 순서와 인덱스를 가진 시퀀스입니다.

---

# 43. 가변 시퀀스와 불변 시퀀스

| 자료형 | 요소 읽기 | 요소 변경 |
| --- | :---: | :---: |
| 문자열 | O | X |
| 리스트 | O | O |
| 튜플 | O | X |
| `range` | O | X |
| `bytes` | O | X |
| `bytearray` | O | O |

원본에서는 리스트와 튜플의 변경 가능 여부를 비교합니다.

---

# 44. 리스트 요소 변경

강사님 코드:

```python
a = [1, 2, 3, 4]
a[0] = 2
```

리스트는 가변 시퀀스이므로 요소를 변경할 수 있습니다.

```python
print(a)
```

결과:

```text
[2, 2, 3, 4]
```

강사님 원본에서는 변경 후 출력이 없어 결과가 화면에 나타나지 않습니다.

---

# 45. 튜플 요소 변경 불가

공통 원본의 주석 처리된 코드:

```python
# a[0] = 3
```

튜플에서 실행하면 다음 오류가 발생합니다.

```text
TypeError: 'tuple' object does not support item assignment
```

튜플은 불변 시퀀스입니다.

---

# 46. 문자열 요소 변경 불가

```python
text = "hello"
text[0] = "H"
```

오류:

```text
TypeError: 'str' object does not support item assignment
```

새 문자열을 만들어 다시 대입해야 합니다.

```python
text = "H" + text[1:]
```

---

# 47. 리스트 요소 삭제

내 코드에만 직접 등장합니다.

```python
a = [1, 2, 3]

del a[0]

print(a)
```

출력:

```text
[2, 3]
```

리스트는 가변 시퀀스이므로 인덱스로 요소를 삭제할 수 있습니다.

---

# 48. 튜플과 문자열에서 `del` 요소 삭제

다음 코드는 실행할 수 없습니다.

```python
values = (1, 2, 3)
del values[0]
```

```python
text = "hello"
del text[0]
```

불변 시퀀스의 요소를 직접 삭제할 수 없기 때문입니다.

변수 전체를 삭제하는 것은 별개입니다.

```python
del values
```

---

# 49. 슬라이싱이란?

슬라이싱(slicing)은 시퀀스의 일부 범위를 잘라 새로운 시퀀스로 가져오는 기능입니다.

기본 구조:

```python
시퀀스[start:stop]
```

`start`부터 시작하고 `stop`은 포함하지 않습니다.

---

# 50. 기본 슬라이싱

공통 원본:

```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:4])
```

출력:

```text
[1, 2, 3]
```

해석:

```text
인덱스 1부터 시작
인덱스 4 바로 앞까지
```

---

# 51. `stop`이 포함되지 않는 이유

슬라이싱의 종료 인덱스는 범위의 경계입니다.

```python
a[1:4]
```

가져오는 인덱스:

```text
1, 2, 3
```

요소 개수:

```python
4 - 1
```

결과 길이는 3입니다.

이 규칙은 `range()`와 비슷합니다.

---

# 52. 음수 인덱스가 포함된 슬라이싱

공통 원본:

```python
print(a[4:-1])
```

출력:

```text
[4, 5, 6, 7, 8]
```

`-1`은 마지막 요소 인덱스를 의미하지만 `stop`은 포함되지 않으므로 값 `9`는 제외됩니다.

---

# 53. 범위를 벗어난 슬라이싱

공통 원본:

```python
print(a[4:100])
```

출력:

```text
[4, 5, 6, 7, 8, 9]
```

슬라이싱에서는 종료 인덱스가 실제 길이를 넘어도 가능한 범위까지만 가져옵니다.

`IndexError`가 발생하지 않습니다.

---

# 54. 인덱싱과 슬라이싱의 범위 초과 차이

```python
a = [0, 1, 2]
```

인덱싱:

```python
a[100]
```

결과:

```text
IndexError
```

슬라이싱:

```python
a[100:200]
```

결과:

```text
[]
```

인덱싱은 요소 하나의 존재를 요구하지만 슬라이싱은 범위의 교집합을 반환합니다.

---

# 55. `step`을 포함한 슬라이싱

공통 원본:

```python
print(a[1:9:2])
```

출력:

```text
[1, 3, 5, 7]
```

기본 구조:

```python
시퀀스[start:stop:step]
```

해석:

```text
인덱스 1부터
인덱스 9 바로 앞까지
2칸씩 이동
```

---

# 56. 원본 주석의 표현 수정

내 코드 주석:

```python
# [시작INDEX, 끝INDEX, 반복INDEX]
```

슬라이싱 문법에서는 쉼표가 아니라 콜론을 사용합니다.

더 정확한 표현:

```python
# [시작 인덱스 : 종료 인덱스 : 이동 간격]
```

`step`은 “반복 인덱스”보다 “이동 간격” 또는 “증감값”이라고 표현하는 것이 자연스럽습니다.

---

# 57. 시작값 생략

공통 원본:

```python
print(a[:7])
```

출력:

```text
[0, 1, 2, 3, 4, 5, 6]
```

`start`를 생략하면 기본적으로 처음부터 시작합니다.

```python
a[:7]
```

은 다음과 비슷합니다.

```python
a[0:7]
```

---

# 58. 종료값 생략

공통 원본:

```python
print(a[5:])
```

출력:

```text
[5, 6, 7, 8, 9]
```

`stop`을 생략하면 시퀀스 끝까지 가져옵니다.

---

# 59. 시작과 종료 모두 생략

공통 원본:

```python
print(a[:])
```

출력:

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

전체 범위를 새 시퀀스로 가져옵니다.

리스트에서는 얕은 복사에 사용할 수 있습니다.

---

# 60. 리스트 전체 슬라이싱과 복사

```python
original = [1, 2, 3]
copied = original[:]

print(original == copied)
print(original is copied)
```

출력:

```text
True
False
```

바깥 리스트는 새 객체가 만들어집니다.

중첩 객체까지 깊게 복사되는 것은 아닙니다.

---

# 61. 문자열 전체 슬라이싱

```python
text = "hello"
copied = text[:]
```

문자열은 불변 객체이므로 구현 최적화에 따라 같은 객체가 재사용될 수도 있습니다.

값 복사 목적에서는 객체 동일성보다 결과 문자열의 내용에 집중해야 합니다.

---

# 62. 시작이 종료보다 큰 정방향 슬라이싱

공통 원본:

```python
print(a[7:3])
```

출력:

```text
[]
```

기본 `step`은 `1`이므로 오른쪽으로 이동합니다.

인덱스 7에서 시작해 인덱스 3 방향으로 갈 수 없기 때문에 빈 리스트입니다.

---

# 63. 역방향 슬라이싱

공통 원본:

```python
print(a[7:3:-1])
```

출력:

```text
[7, 6, 5, 4]
```

`step`이 `-1`이면 왼쪽으로 이동합니다.

`stop` 인덱스 3은 포함하지 않습니다.

---

# 64. 또 다른 역방향 슬라이싱

공통 원본:

```python
print(a[8:4:-1])
```

출력:

```text
[8, 7, 6, 5]
```

가져오는 인덱스:

```text
8, 7, 6, 5
```

인덱스 4는 종료 경계이므로 제외됩니다.

---

# 65. 음수 `step`의 방향

```python
a[start:stop:-1]
```

다음 조건이 필요합니다.

```text
start가 stop보다 오른쪽에 있어야 함
```

예:

```python
a[8:4:-1]
```

반대로:

```python
a[4:8:-1]
```

은 빈 결과입니다.

---

# 66. 역방향 전체 슬라이싱

```python
a[::-1]
```

`start`와 `stop`을 생략하고 `step`을 `-1`로 설정합니다.

시퀀스 전체를 역순으로 만든 새 시퀀스를 반환합니다.

---

# 67. 음수 시작 인덱스

공통 원본:

```python
print(a[-4:8])
```

출력:

```text
[6, 7]
```

길이가 10인 리스트에서 `-4`는 양수 인덱스 `6`과 같습니다.

```text
-4 → 6
```

따라서 다음과 같은 결과입니다.

```python
a[6:8]
```

---

# 68. 음수 시작과 음수 종료

공통 원본:

```python
print(a[-4:-2])
```

출력:

```text
[6, 7]
```

인덱스 대응:

```text
-4 → 6
-2 → 8
```

따라서 다음과 같습니다.

```python
a[6:8]
```

---

# 69. 슬라이싱 인덱스 정규화

Python은 음수 인덱스를 시퀀스 길이를 기준으로 해석합니다.

길이가 10일 때:

| 음수 | 대응 양수 |
| ---: | ---: |
| `-1` | `9` |
| `-2` | `8` |
| `-3` | `7` |
| `-4` | `6` |

개념적으로 다음 관계를 사용할 수 있습니다.

```text
양수 위치 = 길이 + 음수 인덱스
```

---

# 70. 슬라이싱 반환 자료형

슬라이싱 결과는 일반적으로 원본과 같은 계열의 시퀀스입니다.

```python
print(type("hello"[1:3]))
print(type([1, 2, 3][1:3]))
print(type((1, 2, 3)[1:3]))
print(type(range(10)[1:3]))
```

출력:

```text
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'range'>
```

---

# 71. `range` 슬라이싱

```python
numbers = range(0, 20, 2)
part = numbers[2:6]

print(part)
print(list(part))
```

출력:

```text
range(4, 12, 2)
[4, 6, 8, 10]
```

`range`를 슬라이싱하면 새로운 `range` 객체가 만들어질 수 있습니다.

---

# 72. 문자열 슬라이싱

```python
text = "Python"

print(text[1:4])
```

출력:

```text
yth
```

문자열 슬라이싱도 `stop`을 포함하지 않습니다.

---

# 73. 튜플 슬라이싱

```python
numbers = (0, 1, 2, 3, 4)

print(numbers[1:4])
```

출력:

```text
(1, 2, 3)
```

결과도 튜플입니다.

---

# 74. 슬라이스 대입

공통 원본:

```python
a[2:5] = ["a", "b", "c"]
```

슬라이스 대입은 리스트의 특정 범위를 새로운 반복 가능한 객체의 요소들로 교체합니다.

기본 구조:

```python
리스트[start:stop] = iterable
```

리스트는 가변 시퀀스이므로 가능합니다.

---

# 75. 같은 개수로 교체

초기 리스트:

```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

대입:

```python
a[2:5] = ["a", "b", "c"]
```

교체되는 기존 요소:

```text
2, 3, 4
```

새 요소:

```text
"a", "b", "c"
```

결과:

```text
[0, 1, 'a', 'b', 'c', 5, 6, 7, 8, 9]
```

---

# 76. 교체된 범위 다시 확인

공통 원본:

```python
print(a[2:5])
```

출력:

```text
['a', 'b', 'c']
```

대입 이후 같은 슬라이스를 읽으면 교체된 요소가 반환됩니다.

---

# 77. 더 많은 요소로 교체

공통 원본:

```python
a[2:5] = [10, 20, 30, 40, 50]
```

교체 범위는 3개 요소이지만 새 요소는 5개입니다.

결과:

```text
[0, 1, 10, 20, 30, 40, 50, 5, 6, 7, 8, 9]
```

리스트 길이가 2만큼 늘어납니다.

---

# 78. 더 적은 요소로 교체

```python
numbers = [0, 1, 2, 3, 4, 5]

numbers[1:5] = [100]

print(numbers)
```

출력:

```text
[0, 100, 5]
```

교체 범위와 새 요소 개수가 같을 필요는 없습니다.

---

# 79. 빈 반복 가능한 객체로 교체

```python
numbers = [0, 1, 2, 3, 4]

numbers[1:4] = []

print(numbers)
```

출력:

```text
[0, 4]
```

해당 범위의 요소를 삭제하는 효과가 있습니다.

---

# 80. 빈 슬라이스에 대입

```python
numbers = [1, 2, 3]

numbers[1:1] = [10, 20]

print(numbers)
```

출력:

```text
[1, 10, 20, 2, 3]
```

빈 범위 위치에 새 요소가 삽입됩니다.

---

# 81. 슬라이스 대입에는 반복 가능한 객체가 필요

```python
numbers = [1, 2, 3]

numbers[1:2] = 100
```

오류:

```text
TypeError: can only assign an iterable
```

오른쪽을 리스트나 튜플 등 반복 가능한 객체로 작성해야 합니다.

```python
numbers[1:2] = [100]
```

---

# 82. 문자열을 슬라이스 대입하면

```python
letters = ["A", "B", "C"]

letters[1:2] = "XY"

print(letters)
```

출력:

```text
['A', 'X', 'Y', 'C']
```

문자열은 반복 가능한 객체이므로 각 문자가 하나씩 들어갑니다.

문자열 전체를 요소 하나로 넣으려면 리스트로 감쌉니다.

```python
letters[1:2] = ["XY"]
```

---

# 83. 확장 슬라이스 대입의 제한

`step`이 1이 아닌 슬라이스에 대입하면 교체 요소 개수가 맞아야 합니다.

```python
numbers = [0, 1, 2, 3, 4, 5]

numbers[::2] = [10, 20, 30]
```

결과:

```text
[10, 1, 20, 3, 30, 5]
```

그러나 개수가 맞지 않으면 `ValueError`가 발생합니다.

```python
numbers[::2] = [10]
```

---

# 84. 문자열과 튜플은 슬라이스 대입 불가

```python
text = "hello"
text[1:3] = "AB"
```

```python
values = (1, 2, 3)
values[1:2] = (100,)
```

둘 다 불변 시퀀스이므로 오류가 발생합니다.

---

# 85. 다국어 리스트 원본 예제

공통 원본:

```python
ko = ["책", "알약", "철판"]
en = ["book", "pill", "plate"]

view = ko
view = en

print(view[0])
```

출력:

```text
book
```

`view = ko` 다음에 즉시 `view = en`이 실행되므로 `view`는 최종적으로 영어 리스트를 참조합니다.

---

# 86. 변수 재대입의 의미

```python
view = ko
view = en
```

처리 흐름:

```text
view가 ko 리스트를 참조
→ 다음 줄에서
view가 en 리스트를 참조하도록 변경
```

`ko`나 `en` 리스트 자체가 변경된 것은 아닙니다.

---

# 87. 언어 선택에 조건문 사용

원본의 의도를 실제 언어 선택으로 확장하면 다음처럼 작성할 수 있습니다.

```python
language = "ko"

if language == "ko":
    view = ko
else:
    view = en
```

조건문은 이후 문서에서 자세히 학습합니다.

---

# 88. 두 리스트를 인덱스로 연결하는 방식

원본 주석에는 같은 위치의 번역어를 비교해 교차할 수 있다는 설명이 있습니다.

```python
ko = ["책", "알약", "철판"]
en = ["book", "pill", "plate"]
```

인덱스 관계:

| 인덱스 | 한국어 | 영어 |
| ---: | --- | --- |
| `0` | 책 | book |
| `1` | 알약 | pill |
| `2` | 철판 | plate |

두 리스트의 순서가 정확히 유지되어야 합니다.

---

# 89. 병렬 리스트의 위험

다음 문제가 발생할 수 있습니다.

- 한쪽 리스트에 값 추가 누락
- 순서가 서로 달라짐
- 길이가 서로 달라짐
- 특정 단어의 연결 관계가 코드에 명확하지 않음

따라서 번역 관계를 표현할 때는 이후 학습할 딕셔너리가 더 적합할 수 있습니다.

```python
translations = {
    "책": "book",
    "알약": "pill",
    "철판": "plate",
}
```

이 내용은 원본 구조를 개선하기 위한 확장 학습입니다.

---

# 90. `zip()`으로 병렬 시퀀스 묶기

```python
ko = ["책", "알약", "철판"]
en = ["book", "pill", "plate"]

for korean, english in zip(ko, en):
    print(korean, english)
```

출력:

```text
책 book
알약 pill
철판 plate
```

`zip()`은 같은 위치의 요소를 튜플로 묶어 순회할 수 있게 합니다.

이 내용은 원본에 직접 등장하지 않는 보충 학습입니다.

---

# 91. 문자열 역순

공통 원본:

```python
a = "hello"

print(a[::-1])
```

출력:

```text
olleh
```

`step`이 `-1`이므로 문자열을 끝에서 처음 방향으로 읽습니다.

---

# 92. 문자열 원본은 변경되지 않는다

```python
text = "hello"
reversed_text = text[::-1]

print(text)
print(reversed_text)
```

출력:

```text
hello
olleh
```

문자열은 불변 시퀀스이므로 역순의 새 문자열이 만들어집니다.

---

# 93. 회문 확인

강사님 코드에는 다음 주석이 있습니다.

```python
# a = "TENET"
```

`TENET`은 앞에서 읽어도 뒤에서 읽어도 같은 문자열입니다.

```python
text = "TENET"

print(text == text[::-1])
```

출력:

```text
True
```

이러한 문자열을 회문(palindrome)이라고 합니다.

---

# 94. 대소문자와 공백을 고려한 회문

```python
text = "Tenet"

normalized = text.lower()

print(normalized == normalized[::-1])
```

복잡한 문장에서는 공백과 문장 부호 제거가 추가로 필요할 수 있습니다.

이는 문자열 처리 확장 학습입니다.

---

# 95. `reversed()`와 `[::-1]`

```python
text = "hello"

result = reversed(text)

print(result)
```

`reversed()`는 역방향 반복자를 반환합니다.

문자열로 만들려면 다음처럼 결합합니다.

```python
result = "".join(reversed(text))
```

반면:

```python
text[::-1]
```

은 즉시 역순 문자열을 반환합니다.

---

# 96. `slice` 객체

슬라이싱 문법은 `slice` 객체로 표현할 수도 있습니다.

```python
part = slice(1, 9, 2)

numbers = list(range(10))

print(numbers[part])
```

출력:

```text
[1, 3, 5, 7]
```

`slice(start, stop, step)`은 같은 슬라이스 규칙을 여러 시퀀스에 재사용할 때 사용할 수 있습니다.

---

# 97. 슬라이스의 기본값

```python
slice(None, None, None)
```

은 다음과 비슷합니다.

```python
[:]
```

역순:

```python
slice(None, None, -1)
```

은 다음과 같습니다.

```python
[::-1]
```

---

# 98. 시퀀스 반복 순회

모든 시퀀스는 `for` 문으로 순회할 수 있습니다.

```python
for value in [10, 20, 30]:
    print(value)
```

문자열:

```python
for char in "ABC":
    print(char)
```

튜플:

```python
for value in (1, 2, 3):
    print(value)
```

`range`:

```python
for number in range(3):
    print(number)
```

---

# 99. 인덱스가 필요하지 않다면 직접 순회

값만 필요할 때:

```python
names = ["민수", "영희", "철수"]

for name in names:
    print(name)
```

인덱스를 사용하지 않아도 됩니다.

---

# 100. 인덱스와 값이 모두 필요하면 `enumerate()`

```python
names = ["민수", "영희", "철수"]

for index, name in enumerate(names):
    print(index, name)
```

`range(len(names))`보다 의도가 명확한 경우가 많습니다.

---

# 101. 시퀀스 비교

같은 종류의 시퀀스는 요소를 앞에서부터 순서대로 비교합니다.

```python
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] < [1, 2, 4])
```

문자열도 사전식 순서로 비교할 수 있습니다.

```python
print("apple" < "banana")
```

비교 기준은 자료형과 요소 비교 가능 여부에 따라 달라집니다.

---

# 102. `min()`과 `max()`

숫자 시퀀스:

```python
numbers = [7, 3, 9, 1]

print(min(numbers))
print(max(numbers))
```

출력:

```text
1
9
```

문자열:

```python
print(min("python"))
print(max("python"))
```

문자 코드 순서에 따라 결과가 결정됩니다.

---

# 103. `sum()`

숫자로 구성된 시퀀스는 `sum()`으로 합계를 구할 수 있습니다.

```python
numbers = [10, 20, 30]

print(sum(numbers))
```

출력:

```text
60
```

문자열 연결에는 `sum()`을 사용하지 않습니다.

```python
"".join(strings)
```

을 사용합니다.

---

# 104. `sorted()`

```python
numbers = (3, 1, 2)

result = sorted(numbers)

print(result)
```

출력:

```text
[1, 2, 3]
```

`sorted()`는 입력 시퀀스 종류와 관계없이 일반적으로 리스트를 반환합니다.

---

# 105. `reversed()`

```python
numbers = [1, 2, 3]

result = reversed(numbers)

print(list(result))
```

출력:

```text
[3, 2, 1]
```

원본 리스트는 변경되지 않습니다.

---

# 106. `range`의 특징

`range()`는 정수 범위를 표현하는 불변 시퀀스입니다.

```python
numbers = range(0, 10, 2)
```

이 객체는 다음 규칙을 저장합니다.

```text
시작값: 0
종료 기준: 10
증가량: 2
```

실제 값 확인:

```python
print(list(numbers))
```

---

# 107. `range` 인덱싱

```python
numbers = range(10, 20, 2)

print(numbers[0])
print(numbers[-1])
```

출력:

```text
10
18
```

`range`도 인덱싱을 지원합니다.

---

# 108. `range` 불변성

```python
numbers = range(5)

numbers[0] = 100
```

오류:

```text
TypeError: 'range' object does not support item assignment
```

---

# 109. `range`의 메모리 효율 개념

```python
range(1_000_000)
```

은 백만 개 정수 리스트를 미리 만드는 방식과 다릅니다.

범위 규칙을 저장하고 필요할 때 값을 계산합니다.

```python
list(range(1_000_000))
```

로 변환하면 실제 백만 개 요소를 가진 리스트가 만들어집니다.

이 내용은 원본 주석의 `range + range` 설명을 보완한 확장 개념입니다.

---

# 110. `bytes`도 시퀀스

원본의 UTF-8 인코딩 결과는 `bytes` 객체입니다.

```python
encoded = "ABC".encode("utf-8")
```

인덱싱:

```python
print(encoded[0])
```

출력:

```text
65
```

`bytes`를 인덱싱하면 한 글자 문자열이 아니라 해당 바이트의 정수값이 반환됩니다.

---

# 111. `bytes` 슬라이싱

```python
encoded = b"ABC"

print(encoded[1:])
```

출력:

```text
b'BC'
```

슬라이싱 결과는 다시 `bytes`입니다.

---

# 112. `bytearray`

`bytearray`는 변경 가능한 바이트 시퀀스입니다.

```python
data = bytearray(b"ABC")

data[0] = 97

print(data)
```

출력:

```text
bytearray(b'aBC')
```

`bytes`와 `bytearray`는 원본의 인코딩 예제를 이해하기 위한 확장 학습입니다.

---

# 113. My Code vs Teacher Code

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 포함 연산 | 동일 | 동일 |
| `not` 설명 | `!` 대신 사용한다고 주석 | 별도 설명 없음 |
| 리스트 연결 | `range` 연결 제한 설명 추가 | 결과 중심 |
| 문자열+정수 | JavaScript 비교 주석 추가 | 오류 코드만 주석 |
| `len()` 설명 | 문자·숫자·튜플이라고 설명 | 설명 없음 |
| UTF-8 인코딩 | 동일 | 동일 |
| 음수 인덱스 | 뒤에서 몇 번째인지 설명 | 출력만 확인 |
| 리스트 요소 변경 | 없음 | `a[0] = 2` 실행 |
| 리스트 요소 삭제 | `del a[0]` 예제 추가 | 없음 |
| 튜플 불변성 | `readonly` 표현 | 값 변경 불가 설명 |
| 슬라이싱 | 상세 주석 다수 | 결과 중심 |
| 다국어 리스트 | 인덱스 대응 설명 추가 | 변수 재대입만 |
| 역순 문자열 | `"hello"` | `"hello"`와 `"TENET"` 주석 |

---

# 114. 내 코드의 장점

- `in`, `not in`, `not (...)`을 함께 비교했습니다.
- Python의 논리 부정이 `not`이라는 점을 기록했습니다.
- `range`끼리 직접 연결할 수 없다는 점을 주석으로 남겼습니다.
- 문자열과 정수를 직접 연결할 수 없다는 점을 다른 언어와 비교해 확인했습니다.
- UTF-8 인코딩 후 바이트 길이와 출력값을 확인했습니다.
- 음수 인덱스를 뒤쪽 위치 접근과 연결해 설명했습니다.
- 범위를 벗어난 인덱스 접근의 오류 이름을 기록했습니다.
- 튜플의 불변성을 오류 예제와 연결했습니다.
- 리스트 요소 삭제 예제를 추가했습니다.
- 정방향, 역방향, 음수 인덱스 슬라이싱을 폭넓게 실험했습니다.
- 슬라이스 대입에서 요소 개수가 증가하는 경우까지 확인했습니다.
- 문자열 역순을 간결하게 확인했습니다.

---

# 115. 내 코드의 개선점

- `len()`은 숫자에 사용할 수 없으므로 “문자, 숫자, 튜플 등”이라는 주석을 수정해야 합니다.
- “Python은 sequence끼리만 더할 수 있다”는 설명은 너무 넓습니다. 호환되는 같은 종류의 시퀀스 연결이라고 설명하는 편이 정확합니다.
- `tuple`을 단순히 `readonly`라고만 표현하면 내부에 가변 객체가 있을 때의 차이를 놓칠 수 있습니다.
- 슬라이싱 주석의 `[시작INDEX, 끝INDEX, 반복INDEX]`는 쉼표 대신 콜론을 사용해야 합니다.
- `step`을 “반복 인덱스”보다 이동 간격이라고 설명하는 편이 정확합니다.
- 변수 이름 `a`, `b`, `c`가 반복되어 현재 자료형을 추적하기 어렵습니다.
- `view = ko` 직후 `view = en`을 실행하여 첫 번째 대입의 효과를 확인할 수 없습니다.
- 병렬 번역 리스트의 관계가 인덱스에 의존하므로 딕셔너리나 `zip()` 사용을 검토할 수 있습니다.
- 코드 영역별 구분 출력이 없어 실행 결과가 어느 예제의 것인지 찾기 어렵습니다.
- 리스트 슬라이스 대입 전후의 길이도 출력하면 변화가 더 명확합니다.

---

# 116. 강사님 코드의 장점

- 시퀀스 공통 연산을 짧은 코드로 순서 있게 보여 줍니다.
- 포함 여부, 연결, 반복, 길이를 한 흐름에서 확인할 수 있습니다.
- UTF-8 인코딩과 한글 첫 문자 접근을 함께 다룹니다.
- 리스트의 가변성과 튜플의 불변성을 나란히 보여 줍니다.
- 슬라이싱의 시작, 종료, 간격, 음수 인덱스를 폭넓게 실습합니다.
- 리스트 슬라이스 대입에서 길이가 달라질 수 있음을 보여 줍니다.
- `TENET` 주석을 통해 역순 문자열과 회문을 연결할 여지가 있습니다.
- 내 코드보다 주석이 적어 실행 흐름을 빠르게 볼 수 있습니다.

---

# 117. 강사님 코드의 개선점

- `a[0] = 2` 이후 리스트를 출력하지 않아 변경 결과를 확인하기 어렵습니다.
- `range`가 어떤 시퀀스 공통 기능을 지원하고 어떤 기능을 지원하지 않는지 설명이 없습니다.
- `len(b)`가 문자 길이가 아니라 UTF-8 바이트 길이라는 설명이 없습니다.
- 일반 인덱싱과 슬라이싱의 범위 초과 차이를 설명하지 않습니다.
- 음수 `step`에서 시작과 종료 방향이 왜 중요한지 설명하지 않습니다.
- `view = ko`가 바로 덮어써져 의미가 드러나지 않습니다.
- 병렬 리스트 방식의 위험과 대안이 없습니다.
- 문자열과 튜플의 불변성을 같은 시퀀스 관점으로 연결하지 않습니다.
- `[::-1]`이 원본을 변경하지 않는다는 설명이 없습니다.
- `slice` 객체, `reversed()`, `zip()` 같은 관련 개념은 다루지 않습니다.

---

# 118. 정확하게 수정한 원본 주석

기존:

```python
# Python은 sequence 끼리만 가능함
```

개선:

```python
# + 연결을 지원하는 호환 가능한 같은 종류의
# 시퀀스끼리 연결할 수 있다.
```

기존:

```python
# len으로 감싸면 길이를 구할 수 있다
# 문자, 숫자, 튜플 등
```

개선:

```python
# len()은 길이를 제공하는 문자열, 리스트,
# 튜플, range 같은 객체에 사용할 수 있다.
# int와 float 같은 숫자에는 사용할 수 없다.
```

기존:

```python
# [시작INDEX,끝INDEX,반복INDEX]
```

개선:

```python
# [시작 인덱스 : 종료 인덱스 : 이동 간격]
```

기존:

```python
# tuple은 readonly 형태기 때문에 값은 바꿀 수 없다
```

개선:

```python
# 튜플은 불변 시퀀스이므로
# 요소 참조를 인덱스로 직접 교체할 수 없다.
```

---

# 119. 개선된 대표 코드

```python
numbers = [0, 10, 20, 30, 40]

print("20 포함:", 20 in numbers)
print("200 미포함:", 200 not in numbers)

left = [1, 2, 3]
right = [4, 5, 6]

combined = left + right

print("연결:", combined)
print("원본 left:", left)
print("원본 right:", right)

text = "안녕하세요"
encoded = text.encode("utf-8")

print("문자 수:", len(text))
print("UTF-8 바이트 수:", len(encoded))
print("첫 문자:", text[0])
```

---

# 120. 개선된 슬라이싱 예제

```python
numbers = list(range(10))

print("1~3:", numbers[1:4])
print("짝수 위치:", numbers[::2])
print("뒤의 네 개:", numbers[-4:])
print("전체 복사:", numbers[:])
print("전체 역순:", numbers[::-1])

numbers[2:5] = [20, 30, 40, 50]

print("슬라이스 대입:", numbers)
```

---

# 121. 실무 활용 예제: 페이지 일부 가져오기

```python
articles = [
    "게시글 1",
    "게시글 2",
    "게시글 3",
    "게시글 4",
    "게시글 5",
    "게시글 6",
]

page_size = 2
page = 2

start = (page - 1) * page_size
stop = start + page_size

current_page = articles[start:stop]

print(current_page)
```

출력:

```text
['게시글 3', '게시글 4']
```

페이지네이션에서 슬라이싱을 사용할 수 있습니다.

---

# 122. 실무 활용 예제: 파일 확장자 확인

```python
filename = "report.pdf"

if filename[-4:] == ".pdf":
    print("PDF 파일입니다.")
```

더 일반적으로는 문자열 메서드 `endswith()`가 의도를 잘 보여 줍니다.

```python
if filename.endswith(".pdf"):
    print("PDF 파일입니다.")
```

---

# 123. 실무 활용 예제: 일부 데이터 마스킹

```python
phone = "01012345678"

masked = phone[:3] + "****" + phone[-4:]

print(masked)
```

출력:

```text
010****5678
```

문자열은 불변이므로 여러 슬라이스를 연결해 새 문자열을 만듭니다.

---

# 124. 실무 활용 예제: 최근 기록

```python
logs = [
    "로그 1",
    "로그 2",
    "로그 3",
    "로그 4",
    "로그 5",
]

recent = logs[-3:]

print(recent)
```

출력:

```text
['로그 3', '로그 4', '로그 5']
```

---

# 125. 실무 활용 예제: 역순 처리

```python
history = [
    "첫 번째",
    "두 번째",
    "세 번째",
]

latest_first = history[::-1]

print(latest_first)
```

원본을 유지하면서 최신 순서로 표시할 수 있습니다.

---

# 126. 실무 활용 예제: 다국어 데이터

병렬 리스트:

```python
korean_words = ["책", "알약", "철판"]
english_words = ["book", "pill", "plate"]

for korean, english in zip(
    korean_words,
    english_words,
):
    print(f"{korean}: {english}")
```

더 명확한 관계 표현:

```python
translations = {
    "책": "book",
    "알약": "pill",
    "철판": "plate",
}
```

---

# 127. 자주 하는 실수: `in`의 검색 범위

```python
data = [[1, 2], [3, 4]]

print(1 in data)
```

결과:

```text
False
```

`in`은 바깥 리스트의 요소인 `[1, 2]`, `[3, 4]`와 비교합니다.

내부까지 자동 탐색하지 않습니다.

---

# 128. 자주 하는 실수: `!` 사용

```python
!True
```

Python 논리 부정 문법이 아닙니다.

```python
not True
```

를 사용합니다.

---

# 129. 자주 하는 실수: 다른 시퀀스 종류 연결

```python
[1, 2] + (3, 4)
```

오류가 발생합니다.

자료형을 맞춥니다.

```python
[1, 2] + list((3, 4))
```

---

# 130. 자주 하는 실수: 문자열과 숫자 직접 연결

```python
"age: " + 30
```

`TypeError`가 발생합니다.

```python
"age: " + str(30)
```

또는:

```python
f"age: {30}"
```

---

# 131. 자주 하는 실수: 숫자에 `len()`

```python
len(12345)
```

숫자에는 길이가 정의되어 있지 않아 `TypeError`가 발생합니다.

숫자의 자릿수가 필요하다면 요구사항에 따라 문자열로 변환할 수 있습니다.

```python
len(str(12345))
```

---

# 132. 자주 하는 실수: 문자 수와 바이트 수 혼동

```python
text = "안녕하세요"
```

```python
len(text)
```

은 5이고:

```python
len(text.encode("utf-8"))
```

은 15입니다.

둘은 서로 다른 단위를 측정합니다.

---

# 133. 자주 하는 실수: 마지막 인덱스를 `len()` 그대로 사용

```python
numbers = [10, 20, 30]

print(numbers[len(numbers)])
```

오류:

```text
IndexError
```

마지막 양수 인덱스는:

```python
len(numbers) - 1
```

더 간단히:

```python
numbers[-1]
```

---

# 134. 자주 하는 실수: 슬라이싱 종료값 포함

```python
numbers[1:4]
```

은 인덱스 `1`, `2`, `3`을 가져옵니다.

인덱스 `4`는 포함하지 않습니다.

---

# 135. 자주 하는 실수: 역방향 슬라이싱의 방향

```python
numbers[2:8:-1]
```

시작점에서 왼쪽으로 이동하지만 종료점은 오른쪽에 있으므로 빈 결과입니다.

```python
numbers[8:2:-1]
```

처럼 시작과 종료 방향을 맞춰야 합니다.

---

# 136. 자주 하는 실수: `step`을 0으로 지정

```python
numbers[::0]
```

오류:

```text
ValueError: slice step cannot be zero
```

이동 간격은 0일 수 없습니다.

---

# 137. 자주 하는 실수: 범위 초과 슬라이싱도 오류라고 생각하기

```python
numbers[100:200]
```

일반적으로 빈 시퀀스를 반환합니다.

```python
numbers[100]
```

과 동작이 다릅니다.

---

# 138. 자주 하는 실수: `a[:]`를 같은 객체라고 생각하기

리스트에서:

```python
copied = original[:]
```

바깥 리스트는 새 객체입니다.

```python
original is copied
```

결과는 `False`입니다.

단, 중첩 내부 객체는 공유할 수 있습니다.

---

# 139. 자주 하는 실수: 슬라이스 대입 오른쪽에 단일 정수

```python
numbers[1:3] = 100
```

반복 가능한 객체가 아니므로 오류입니다.

```python
numbers[1:3] = [100]
```

---

# 140. 자주 하는 실수: 문자열을 한 요소로 넣으려다 분해

```python
letters[1:2] = "XY"
```

결과에는 `"X"`와 `"Y"`가 별도 요소로 들어갑니다.

문자열 전체를 하나의 요소로 넣으려면:

```python
letters[1:2] = ["XY"]
```

---

# 141. 자주 하는 실수: 불변 시퀀스 슬라이스 대입

```python
text[1:3] = "AB"
```

문자열은 불변이므로 실행할 수 없습니다.

새 문자열을 구성합니다.

```python
text = text[:1] + "AB" + text[3:]
```

---

# 142. 자주 하는 실수: `[::-1]`이 원본을 뒤집는다고 생각하기

```python
numbers = [1, 2, 3]

numbers[::-1]

print(numbers)
```

출력:

```text
[1, 2, 3]
```

반환값을 사용해야 합니다.

```python
reversed_numbers = numbers[::-1]
```

원본을 직접 뒤집으려면 리스트의 `reverse()`를 사용합니다.

---

# 143. 자주 하는 실수: 병렬 리스트 순서 불일치

```python
ko = ["책", "알약"]
en = ["pill", "book"]
```

같은 인덱스가 올바른 번역 관계를 나타내지 않습니다.

관계가 중요한 데이터는 딕셔너리 또는 구조화된 객체를 검토합니다.

---

# 144. 면접·복습 질문 1

## 시퀀스란 무엇인가?

시퀀스는 요소가 순서대로 나열되어 있고 각 요소에 인덱스로 접근할 수 있는 자료형입니다. 문자열, 리스트, 튜플, `range` 등이 대표적입니다.

---

# 145. 면접·복습 질문 2

## `in`과 `not in`은 무엇을 반환하는가?

값의 포함 여부를 나타내는 Boolean 값을 반환합니다.

---

# 146. 면접·복습 질문 3

## 모든 시퀀스를 `+`로 서로 연결할 수 있는가?

아닙니다. `+` 연결을 지원하는 호환 가능한 같은 종류의 시퀀스끼리 연결해야 합니다. 리스트와 튜플을 직접 더할 수 없고 `range`도 직접 연결할 수 없습니다.

---

# 147. 면접·복습 질문 4

## `len("안녕하세요")`와 UTF-8 바이트 길이가 다른 이유는 무엇인가?

`len(str)`은 문자 개수를 반환하지만 인코딩된 `bytes`의 `len()`은 실제 바이트 개수를 반환하기 때문입니다.

---

# 148. 면접·복습 질문 5

## 인덱싱과 슬라이싱의 범위 초과 동작은 어떻게 다른가?

존재하지 않는 단일 인덱스 접근은 `IndexError`를 발생시킵니다. 슬라이싱은 실제 범위와 겹치는 부분만 반환하므로 범위를 넘어도 일반적으로 오류가 발생하지 않습니다.

---

# 149. 면접·복습 질문 6

## `a[1:9:2]`에서 각 값의 의미는 무엇인가?

인덱스 1부터 시작하고 인덱스 9는 포함하지 않으며 2칸씩 이동합니다.

---

# 150. 면접·복습 질문 7

## `a[7:3]`이 빈 결과인 이유는 무엇인가?

기본 `step`은 1이라 오른쪽으로 이동합니다. 시작 인덱스 7에서 종료 기준 3 방향으로 갈 수 없기 때문입니다.

---

# 151. 면접·복습 질문 8

## 슬라이스 대입에서 교체 범위와 새 요소 개수가 달라도 되는가?

`step`이 1인 일반 슬라이스 대입에서는 가능합니다. 새 요소가 더 많으면 리스트 길이가 늘고 더 적으면 줄어듭니다.

---

# 152. 면접·복습 질문 9

## 문자열, 리스트, 튜플 중 가변 시퀀스는 무엇인가?

리스트가 가변 시퀀스입니다. 문자열과 튜플은 불변 시퀀스입니다.

---

# 153. 면접·복습 질문 10

## `a[::-1]`은 무엇을 반환하는가?

원본 시퀀스의 요소를 역순으로 배치한 새 시퀀스를 반환합니다. 원본 자체를 변경하지 않습니다.

---

# 154. Problems

## 문제 1

다음 리스트에 값 `20`이 포함되어 있는지 출력하세요.

```python
numbers = [10, 20, 30]
```

---

## 문제 2

다음 리스트에 값 `100`이 포함되어 있지 않은지 `not in`으로 출력하세요.

```python
numbers = [10, 20, 30]
```

---

## 문제 3

다음 두 리스트를 연결한 새 리스트를 만드세요.

```python
left = [1, 2, 3]
right = [4, 5, 6]
```

---

## 문제 4

문자열 `"Python"`과 숫자 `3`을 연결해 `"Python3"`을 만드세요.

---

## 문제 5

문자 `=`를 20개 출력하세요.

---

## 문제 6

문자열 `"안녕하세요"`의 문자 수를 출력하세요.

---

## 문제 7

문자열 `"안녕하세요"`를 UTF-8로 인코딩한 바이트 수를 출력하세요.

---

## 문제 8

다음 리스트의 첫 번째 요소를 출력하세요.

```python
numbers = [10, 20, 30, 40]
```

---

## 문제 9

다음 리스트의 뒤에서 두 번째 요소를 출력하세요.

```python
numbers = [10, 20, 30, 40]
```

---

## 문제 10

다음 문자열의 첫 문자를 출력하세요.

```python
text = "Python"
```

---

## 문제 11

다음 리스트에서 인덱스 1부터 4 바로 앞까지 슬라이싱하세요.

```python
numbers = [0, 1, 2, 3, 4, 5]
```

---

## 문제 12

다음 리스트에서 인덱스 2부터 끝까지 가져오세요.

```python
numbers = [0, 1, 2, 3, 4, 5]
```

---

## 문제 13

다음 리스트에서 처음부터 인덱스 4 바로 앞까지 가져오세요.

```python
numbers = [0, 1, 2, 3, 4, 5]
```

---

## 문제 14

다음 리스트의 전체를 슬라이싱해 새 리스트를 만드세요.

```python
numbers = [1, 2, 3]
```

---

## 문제 15

다음 리스트에서 짝수 인덱스의 값만 가져오세요.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
```

---

## 문제 16

다음 리스트를 역순으로 만든 새 리스트를 출력하세요.

```python
numbers = [1, 2, 3, 4, 5]
```

---

## 문제 17

다음 문자열을 역순으로 출력하세요.

```python
text = "sequence"
```

---

## 문제 18

다음 리스트의 마지막 세 요소를 슬라이싱하세요.

```python
numbers = [10, 20, 30, 40, 50]
```

---

## 문제 19

다음 리스트에서 인덱스 2부터 5 바로 앞의 요소를 `"A"`, `"B"`, `"C"`로 교체하세요.

```python
values = [0, 1, 2, 3, 4, 5]
```

---

## 문제 20

다음 리스트의 인덱스 1부터 4 바로 앞 범위를 `[100]` 하나로 교체하세요.

```python
values = [0, 1, 2, 3, 4]
```

---

## 문제 21

다음 리스트의 인덱스 2 위치에 `10`, `20`을 슬라이스 대입으로 삽입하세요.

```python
values = [1, 2, 3]
```

---

## 문제 22

다음 문자열이 회문인지 확인하세요.

```python
text = "TENET"
```

---

## 문제 23

다음 두 리스트의 같은 위치 요소를 `zip()`으로 함께 출력하세요.

```python
ko = ["책", "알약", "철판"]
en = ["book", "pill", "plate"]
```

---

## 문제 24

`range(0, 10, 2)`에 숫자 `6`이 포함되어 있는지 출력하세요.

---

## 문제 25

다음 `range` 객체에서 두 번째 값부터 네 번째 값 바로 앞까지 슬라이싱하고 리스트로 출력하세요.

```python
numbers = range(0, 20, 2)
```

---

# 155. Answers

## 정답 1

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

---

## 정답 2

```python
numbers = [10, 20, 30]

print(100 not in numbers)
```

---

## 정답 3

```python
left = [1, 2, 3]
right = [4, 5, 6]

combined = left + right

print(combined)
```

---

## 정답 4

```python
result = "Python" + str(3)

print(result)
```

또는:

```python
result = f"Python{3}"
```

---

## 정답 5

```python
print("=" * 20)
```

---

## 정답 6

```python
text = "안녕하세요"

print(len(text))
```

---

## 정답 7

```python
text = "안녕하세요"
encoded = text.encode("utf-8")

print(len(encoded))
```

---

## 정답 8

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
```

---

## 정답 9

```python
numbers = [10, 20, 30, 40]

print(numbers[-2])
```

---

## 정답 10

```python
text = "Python"

print(text[0])
```

---

## 정답 11

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
```

---

## 정답 12

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[2:])
```

---

## 정답 13

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[:4])
```

---

## 정답 14

```python
numbers = [1, 2, 3]

copied = numbers[:]

print(copied)
```

---

## 정답 15

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7]

print(numbers[::2])
```

---

## 정답 16

```python
numbers = [1, 2, 3, 4, 5]

reversed_numbers = numbers[::-1]

print(reversed_numbers)
```

---

## 정답 17

```python
text = "sequence"

print(text[::-1])
```

---

## 정답 18

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[-3:])
```

---

## 정답 19

```python
values = [0, 1, 2, 3, 4, 5]

values[2:5] = ["A", "B", "C"]

print(values)
```

---

## 정답 20

```python
values = [0, 1, 2, 3, 4]

values[1:4] = [100]

print(values)
```

---

## 정답 21

```python
values = [1, 2, 3]

values[2:2] = [10, 20]

print(values)
```

---

## 정답 22

```python
text = "TENET"

print(text == text[::-1])
```

---

## 정답 23

```python
ko = ["책", "알약", "철판"]
en = ["book", "pill", "plate"]

for korean, english in zip(ko, en):
    print(korean, english)
```

---

## 정답 24

```python
numbers = range(0, 10, 2)

print(6 in numbers)
```

---

## 정답 25

```python
numbers = range(0, 20, 2)

part = numbers[1:4]

print(list(part))
```

결과:

```text
[2, 4, 6]
```

---

# 156. Final Checklist

- [ ] 시퀀스가 순서를 가진 자료형임을 설명할 수 있다.
- [ ] 문자열, 리스트, 튜플, `range`가 시퀀스임을 안다.
- [ ] 가변 시퀀스와 불변 시퀀스를 구분할 수 있다.
- [ ] `in`과 `not in`으로 포함 여부를 확인할 수 있다.
- [ ] `not (x in sequence)`와 `x not in sequence`의 관계를 안다.
- [ ] Python의 논리 부정 연산자가 `not`임을 안다.
- [ ] 리스트끼리 `+`로 연결할 수 있다.
- [ ] 문자열끼리 `+`로 연결할 수 있다.
- [ ] 튜플끼리 `+`로 연결할 수 있다.
- [ ] 리스트와 튜플을 직접 더할 수 없음을 안다.
- [ ] `range + range`가 지원되지 않음을 안다.
- [ ] 문자열과 숫자를 직접 연결할 수 없음을 안다.
- [ ] `str()` 또는 f-string으로 자료형을 맞출 수 있다.
- [ ] 시퀀스에 정수를 곱해 반복된 결과를 만들 수 있다.
- [ ] `range`는 `*` 반복을 지원하지 않음을 안다.
- [ ] `len()`이 길이를 제공하는 객체에 사용됨을 안다.
- [ ] 숫자에는 `len()`을 바로 사용할 수 없음을 안다.
- [ ] 문자열 문자 수와 UTF-8 바이트 수를 구분할 수 있다.
- [ ] `encode()`와 `decode()`의 방향을 설명할 수 있다.
- [ ] 양수와 음수 인덱스로 요소에 접근할 수 있다.
- [ ] 범위를 벗어난 인덱싱이 `IndexError`를 발생시킴을 안다.
- [ ] 리스트 요소를 변경하고 삭제할 수 있다.
- [ ] 튜플과 문자열 요소를 직접 변경할 수 없음을 안다.
- [ ] 슬라이싱의 `start`, `stop`, `step`을 설명할 수 있다.
- [ ] 슬라이싱에서 `stop`이 포함되지 않음을 안다.
- [ ] 시작값과 종료값을 생략할 수 있다.
- [ ] 범위를 벗어난 슬라이싱이 오류를 발생시키지 않을 수 있음을 안다.
- [ ] 음수 인덱스를 슬라이싱에 사용할 수 있다.
- [ ] 음수 `step`으로 역방향 슬라이싱을 작성할 수 있다.
- [ ] 시작과 종료 방향이 `step`과 맞아야 함을 안다.
- [ ] `step`으로 0을 사용할 수 없음을 안다.
- [ ] `[:]`로 리스트의 얕은 복사를 만들 수 있다.
- [ ] 슬라이스 대입으로 리스트 범위를 교체할 수 있다.
- [ ] 슬라이스 대입으로 리스트 길이가 달라질 수 있음을 안다.
- [ ] 슬라이스 대입 오른쪽에 반복 가능한 객체가 필요함을 안다.
- [ ] 문자열을 슬라이스 대입하면 문자 단위로 분해될 수 있음을 안다.
- [ ] 병렬 리스트의 인덱스 관계와 위험을 이해한다.
- [ ] `zip()`으로 같은 위치의 요소를 함께 순회할 수 있다.
- [ ] `[::-1]`이 역순의 새 시퀀스를 반환함을 안다.
- [ ] 회문을 역순 비교로 확인할 수 있다.
- [ ] `reversed()`와 `[::-1]`의 결과 형태 차이를 설명할 수 있다.
- [ ] `range`도 인덱싱과 슬라이싱을 지원함을 안다.
- [ ] `bytes`가 바이트 시퀀스임을 이해한다.
- [ ] 내 코드와 강사님 코드의 차이 및 개선점을 설명할 수 있다.

---

# 157. Key Summary

```text
sequence
→ 순서가 있는 요소의 모음
→ 인덱싱 가능
→ 슬라이싱 가능
→ 반복문 순회 가능
```

대표 시퀀스:

```text
str       불변
list      가변
tuple     불변
range     불변
bytes     불변
bytearray 가변
```

포함 여부:

```python
value in sequence
value not in sequence
```

연결:

```python
[1, 2] + [3, 4]
"hello" + "world"
(1, 2) + (3, 4)
```

반복:

```python
"-" * 10
[0] * 5
("A",) * 3
```

길이:

```python
len(sequence)
```

문자와 바이트:

```python
text = "안녕하세요"

len(text)
# 5

len(text.encode("utf-8"))
# 15
```

인덱싱:

```python
sequence[0]
sequence[-1]
```

슬라이싱:

```python
sequence[start:stop:step]
```

```text
start
→ 시작 위치

stop
→ 포함하지 않는 종료 경계

step
→ 이동 간격
```

전체:

```python
sequence[:]
```

역순:

```python
sequence[::-1]
```

리스트 슬라이스 대입:

```python
numbers[2:5] = [10, 20, 30, 40]
```

```text
일반 인덱싱 범위 초과
→ IndexError

슬라이싱 범위 초과
→ 가능한 범위 또는 빈 시퀀스
```

시퀀스는 문자열, 리스트, 튜플, `range`를 각각 따로 외우는 대신 공통 동작을 하나의 개념으로 연결해 이해하도록 도와줍니다. 이후 반복문과 데이터 처리에서는 이 공통 규칙을 계속 사용하게 됩니다.
