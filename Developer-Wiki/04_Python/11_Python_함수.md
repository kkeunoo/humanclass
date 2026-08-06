---
title: Python 함수
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 함수

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `11_Python_함수.md` |
| 분류 | `04_Python` |
| 원본 기준 | `workspace_python/11_fn.py`, `workspace_teacher/workspace_python/_11_fn.py` |
| 핵심 범위 | 함수 정의·호출, 매개변수, 전달인자, `return`, 다중 반환, 언패킹, 가변 인자, 기본값, 함수 객체, 람다, `map()`, 변수 범위 |
| 보충 범위 | Docstring, 변경 가능한 객체, 함수 합성, 재귀, 타입 힌트, 순수 함수, LEGB |
| 실습 범위 | 사칙연산 함수, 사용자 정보 출력, 나이 목록 추출, 정렬 기준 함수, 성인 사용자 필터링 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드 전체를 한 번에 나열하지 않는다.  
> 함수의 정의·입력·반환·가변 인자·변수 범위에 필요한 핵심 코드만 발췌하고, 실행 결과와 실무 사용 이유를 함께 설명한다.

---

# 개요

함수는 특정 작업을 하나의 이름으로 묶은 재사용 가능한 코드 블록이다.

```text
입력값 전달
    ↓
함수 내부 처리
    ↓
결과 반환
```

함수를 사용하지 않으면 같은 작업을 여러 위치에 반복해서 작성하게 된다.

```python
print(10 + 20)
print(30 + 40)
print(50 + 60)
```

함수로 분리하면 계산 규칙을 한곳에서 관리할 수 있다.

```python
def add(a, b):
    return a + b


print(add(10, 20))
print(add(30, 40))
print(add(50, 60))
```

> [!IMPORTANT]
> 함수의 목적은 코드를 무조건 짧게 만드는 것이 아니다.
>
> 작업에 이름을 붙이고, 중복을 줄이며, 입력과 결과를 명확하게 분리하는 것이 핵심이다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 함수 정의 | 실행할 코드를 하나의 이름으로 선언 |
| 함수 호출 | 정의된 함수를 실제로 실행 |
| 매개변수 | 함수 정의에서 입력값을 받는 변수 |
| 전달인자 | 함수 호출 시 실제로 전달하는 값 |
| `return` | 함수 결과를 호출한 위치에 반환 |
| 위치 인자 | 전달 순서에 따라 매개변수와 연결 |
| 키워드 인자 | 매개변수 이름을 지정해 전달 |
| `*args` | 여러 위치 인자를 튜플로 받음 |
| `**kwargs` | 여러 키워드 인자를 딕셔너리로 받음 |
| 언패킹 | 시퀀스·딕셔너리 값을 여러 인자로 펼침 |
| 기본 매개변수 | 인자가 생략되었을 때 사용할 기본값 |
| 람다 표현식 | 짧은 함수를 한 표현식으로 작성 |
| 지역 변수 | 함수 내부에서 생성되고 사용되는 변수 |
| 전역 변수 | 함수 바깥에서 선언된 변수 |
| `nonlocal` | 가장 가까운 바깥 함수의 변수 사용 |
| LEGB | Python의 이름 검색 순서 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- `def`로 함수를 정의하고 호출할 수 있다.
- 함수가 정의된 뒤에 호출되어야 하는 이유를 설명할 수 있다.
- 매개변수와 전달인자를 구분할 수 있다.
- `print()`와 `return`의 차이를 설명할 수 있다.
- 값 없는 `return`이 `None`을 반환한다는 점을 이해한다.
- 여러 값을 반환하고 언패킹할 수 있다.
- 위치 인자와 키워드 인자를 사용할 수 있다.
- 리스트·튜플에 `*`, 딕셔너리에 `**`를 적용할 수 있다.
- `*args`와 `**kwargs`의 자료형을 설명할 수 있다.
- 기본 매개변수를 올바른 순서로 선언할 수 있다.
- 변경 가능한 기본값의 문제를 이해한다.
- 함수도 변수에 저장할 수 있는 객체임을 이해한다.
- 람다 표현식과 일반 함수의 선택 기준을 구분할 수 있다.
- `map()`과 정렬의 `key`에 함수를 전달할 수 있다.
- 변경 가능한 객체가 함수 안에서 수정될 수 있음을 이해한다.
- 지역·전역·비지역 변수의 범위를 구분할 수 있다.
- `global`과 `nonlocal`의 사용 목적을 설명할 수 있다.
- 재귀 함수에 종료 조건이 필요한 이유를 이해한다.
- 타입 힌트와 Docstring으로 함수 계약을 표현할 수 있다.
- 하나의 함수가 하나의 주요 책임을 담당하도록 작성할 수 있다.

---

# 1. 함수 정의

## 1-1. 내 코드

```python
def hello():
    print("hello world")
```

## 1-2. 강사님 코드

```python
def hello():
    print("hello world")
```

두 코드는 동일하다.

## 1-3. 구성

| 요소 | 의미 |
| --- | --- |
| `def` | 함수 정의 키워드 |
| `hello` | 함수 이름 |
| `()` | 매개변수를 작성하는 위치 |
| `:` | 함수 블록 시작 |
| 들여쓰기 | 함수 내부 실행 코드 |

## 1-4. 설명

함수를 정의하는 순간에는 내부 코드가 실행되지 않는다.

```text
함수 정의
→ 사용할 작업을 등록

함수 호출
→ 등록된 작업을 실행
```

---

# 2. 함수 호출

```python
def hello():
    print("hello world")


hello()
```

## 2-1. 출력 결과

```text
hello world
```

함수 이름 뒤에 괄호를 붙이면 함수가 실행된다.

```python
hello
```

괄호가 없으면 함수 자체를 가리킬 뿐 실행하지 않는다.

---

# 3. 정의 전에 호출하면 발생하는 오류

## 3-1. 내 코드의 메모

```python
# hello()

def hello():
    print("hello world")
```

함수 정의 전에 주석을 제거하고 호출하면 오류가 발생한다.

```text
NameError: name 'hello' is not defined
```

## 3-2. 오류 원인

Python은 코드를 위에서 아래로 실행한다.

```text
hello() 호출
    ↓
아직 hello 함수 정의 없음
    ↓
NameError
```

## 3-3. 올바른 순서

```python
def hello():
    print("hello world")


hello()
```

---

# 4. 함수 이름 작성

함수 이름은 함수가 수행하는 동작을 표현하는 것이 좋다.

좋은 예:

```python
get_user()
calculate_total()
validate_email()
save_file()
```

좋지 않은 예:

```python
data()
work()
process()
test()
```

> [!TIP]
> 함수 이름은 일반적으로 동사 또는 동사구 형태의 `snake_case`로 작성한다.

---

# 5. 매개변수와 전달인자

## 5-1. 원본 코드

```python
def add(a, b):
    print(a + b)


add(1, 2)
```

## 5-2. 출력 결과

```text
3
```

## 5-3. 용어 구분

| 용어 | 코드 | 의미 |
| --- | --- | --- |
| 매개변수 | `a`, `b` | 함수 정의에서 값을 받는 변수 |
| 전달인자 | `1`, `2` | 함수 호출 시 실제로 전달하는 값 |

```text
add(1, 2)
    ↓
a = 1
b = 2
```

---

# 6. Docstring

## 6-1. 내 코드

```python
def add(a, b):
    "a + b를 출력함"
    print(a + b)
```

## 6-2. 강사님 코드

```python
def add(a, b):
    "a + b를 출력"
    print(a + b)
```

함수 본문의 첫 문자열은 Docstring으로 저장될 수 있다.

## 6-3. 실행

```python
print(add.__doc__)
```

## 6-4. 출력 결과

```text
a + b를 출력함
```

## 6-5. 권장 형태

```python
def add(a: int, b: int) -> int:
    """두 정수를 더한 결과를 반환한다."""
    return a + b
```

> [!IMPORTANT]
> 함수 중간에 작성한 문자열은 함수의 Docstring으로 사용되지 않는다.
>
> Docstring은 함수 본문의 첫 번째 문장에 작성한다.

---

# 7. `print()`와 `return`

## 7-1. 출력 함수

```python
def add_and_print(a, b):
    print(a + b)
```

호출:

```python
result = add_and_print(1, 2)

print(result)
```

출력:

```text
3
None
```

화면에는 계산 결과가 보이지만 함수가 값을 반환하지 않았으므로 `result`에는 `None`이 저장된다.

## 7-2. 반환 함수

```python
def add(a, b):
    return a + b
```

실행:

```python
result = add(1, 2)

print(result)
```

출력:

```text
3
```

## 7-3. 차이

| 방식 | 역할 |
| --- | --- |
| `print()` | 화면에 값을 표시 |
| `return` | 호출한 코드에 값을 전달 |

> [!IMPORTANT]
> 계산 함수는 결과를 출력하기보다 반환하도록 작성하면 다른 코드에서 재사용하기 쉽다.

---

# 8. 반환값 활용

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
print(result * 2)
```

출력:

```text
30
60
```

반환값은 다음 작업에 사용할 수 있다.

- 변수에 저장
- 다른 계산에 사용
- 조건문에 사용
- 다른 함수에 전달
- 파일 또는 데이터베이스에 저장

---

# 9. 값 없는 `return`

## 9-1. 원본 코드

```python
def not_ten(number):
    if number == 10:
        return

    print(number)
```

## 9-2. 실행

```python
result = not_ten(10)

print("result:", result)
```

## 9-3. 출력 결과

```text
result: None
```

값 없는 `return`은 함수를 즉시 종료하고 `None`을 반환한다.

---

# 10. 조기 반환

`return`은 함수 마지막뿐 아니라 처리하지 않을 조건에서 먼저 종료하는 데 사용할 수 있다.

```python
def print_positive(number):
    if number <= 0:
        return

    print(number)
```

실행:

```python
print_positive(-1)
print_positive(10)
```

출력:

```text
10
```

> [!TIP]
> 잘못된 입력이나 처리하지 않을 조건을 먼저 반환하면 중첩 조건문을 줄일 수 있다.

---

# 11. 여러 값 반환

## 11-1. 내 코드와 강사님 코드

```python
def add_sub(a, b):
    add_result = a + b
    sub_result = a - b

    return add_result, sub_result
```

## 11-2. 하나의 변수로 받기

```python
result = add_sub(1, 2)

print(result)
print(type(result))
```

## 11-3. 출력 결과

```text
(3, -1)
<class 'tuple'>
```

쉼표로 여러 값을 반환하면 하나의 튜플로 묶인다.

---

# 12. 반환값 언패킹

```python
add_result, sub_result = (
    add_sub(1, 2)
)

print(add_result)
print(sub_result)
```

## 12-1. 출력 결과

```text
3
-1
```

튜플의 각 값을 여러 변수에 나누어 저장할 수 있다.

> [!WARNING]
> 반환값 개수와 변수 개수가 다르면 `ValueError`가 발생한다.

---

# 13. 위치 인자

## 13-1. 원본 코드

```python
def minus(x, y):
    return x - y


print(minus(5, 2))
```

## 13-2. 출력 결과

```text
3
```

위치 인자는 전달 순서대로 매개변수와 연결된다.

```text
5 → x
2 → y
```

---

# 14. 키워드 인자

```python
def minus(x, y):
    return x - y


print(
    minus(
        y=5,
        x=2,
    )
)
```

## 14-1. 출력 결과

```text
-3
```

매개변수 이름을 직접 지정하면 호출 순서와 관계없이 값을 전달할 수 있다.

---

# 15. 인자 개수 오류

```python
def add(a, b):
    return a + b


add(1, 2, 3)
```

발생 결과:

```text
TypeError
```

정의된 매개변수보다 많은 값을 전달했기 때문이다.

인자가 부족해도 `TypeError`가 발생한다.

---

# 16. 시퀀스 언패킹 `*`

## 16-1. 원본 코드

```python
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


numbers = [
    1,
    2,
    3,
]

print_numbers(*numbers)
```

## 16-2. 출력 결과

```text
1
2
3
```

`*numbers`는 리스트 원소를 각각의 위치 인자로 펼친다.

```text
[1, 2, 3]
    ↓
1, 2, 3
```

---

# 17. 딕셔너리에 `*`

```python
person = {
    "name": "Kim",
    "age": 30,
}


def info(age, name):
    print(age, name)


info(*person)
```

## 17-1. 출력 결과

```text
name age
```

딕셔너리에 `*`를 사용하면 키가 펼쳐진다.

```text
person의 키
→ "name", "age"
```

> [!WARNING]
> 딕셔너리의 키 순서에 의존해 위치 인자로 전달하는 방식은 함수 의미가 불명확해질 수 있다.
>
> 딕셔너리는 일반적으로 `**`로 키워드 인자 전달을 고려한다.

---

# 18. 딕셔너리에 `**`

```python
person = {
    "name": "Kim",
    "age": 30,
}


def info(age, name):
    print(age, name)


info(**person)
```

## 18-1. 출력 결과

```text
30 Kim
```

`**`는 다음 호출과 같은 의미다.

```python
info(
    name="Kim",
    age=30,
)
```

## 18-2. 조건

딕셔너리 키와 함수의 매개변수 이름이 일치해야 한다.

---

# 19. 가변 위치 인자 `*args`

## 19-1. 내 코드와 강사님 코드

```python
def print_numbers(*args):
    print(type(args))
    print(args)
```

실행:

```python
print_numbers(1)
print_numbers(1, 2, 3, 4)
print_numbers()
```

출력:

```text
<class 'tuple'>
(1,)
<class 'tuple'>
(1, 2, 3, 4)
<class 'tuple'>
()
```

여러 위치 인자는 튜플로 묶여 전달된다.

---

# 20. `args`는 관례적인 이름

다음 코드도 문법적으로 정상이다.

```python
def print_numbers(*values):
    print(values)
```

중요한 것은 변수 이름이 아니라 `*`다.

하지만 협업에서는 `*args`라는 관례적인 이름을 자주 사용한다.

---

# 21. 일반 매개변수와 `*args`

## 21-1. 원본 코드

```python
def print_numbers(first, *others):
    print(first)

    for number in others:
        print(number)
```

실행:

```python
print_numbers(
    1,
    2,
    3,
    4,
)
```

출력:

```text
1
2
3
4
```

첫 번째 값은 `first`, 나머지 값은 `others` 튜플에 저장된다.

---

# 22. 가변 키워드 인자 `**kwargs`

## 22-1. 원본 코드

```python
def print_info(**kwargs):
    for key, value in (
        kwargs.items()
    ):
        print(key, value)
```

실행:

```python
print_info(
    name="Kim",
    age=30,
)
```

출력:

```text
name Kim
age 30
```

여러 키워드 인자는 딕셔너리로 묶여 전달된다.

---

# 23. 기본 매개변수

## 23-1. 원본 코드

```python
def info(
    name,
    age,
    address="비공개",
):
    print(
        name,
        age,
        address,
    )
```

실행:

```python
info("Kim", 30)
info("Lee", 25, "서울")
```

출력:

```text
Kim 30 비공개
Lee 25 서울
```

값을 생략하면 기본값을 사용한다.

---

# 24. 기본 매개변수 순서

기본값 없는 매개변수는 기본값 있는 매개변수보다 앞에 와야 한다.

잘못된 코드:

```text
def info(name="익명", age):
    pass
```

발생 결과:

```text
SyntaxError
```

올바른 코드:

```python
def info(
    age,
    name="익명",
):
    pass
```

---

# 25. 변경 가능한 기본값 주의

잘못된 코드:

```python
def add_item(
    item,
    items=[],
):
    items.append(item)

    return items
```

실행:

```python
print(add_item("A"))
print(add_item("B"))
```

출력:

```text
['A']
['A', 'B']
```

기본 리스트가 호출 사이에 공유된다.

## 25-1. 개선

```python
def add_item(
    item,
    items=None,
):
    if items is None:
        items = []

    items.append(item)

    return items
```

출력:

```text
['A']
['B']
```

---

# 26. 지역 변수

## 26-1. 원본 코드

```python
def local_var():
    value = 10

    print(value)


local_var()
```

출력:

```text
10
```

`value`는 함수 내부에서 생성된 지역 변수다.

함수 밖에서 접근하면 `NameError`가 발생한다.

---

# 27. 전역 변수 읽기

```python
value = 10


def show_value():
    print(value)


show_value()
```

출력:

```text
10
```

함수 내부에 같은 이름의 지역 변수가 없으면 전역 변수를 읽을 수 있다.

---

# 28. 지역 변수 우선

## 28-1. 원본 코드

```python
value = 10


def show_value():
    value = 20

    print(
        "함수 내부:",
        value,
    )


show_value()

print(
    "함수 외부:",
    value,
)
```

출력:

```text
함수 내부: 20
함수 외부: 10
```

함수 내부의 `value`와 외부의 `value`는 서로 다른 변수다.

---

# 29. `global`

## 29-1. 원본 코드

```python
value = 10


def change_value():
    global value

    value = 20


change_value()

print(value)
```

출력:

```text
20
```

`global`은 함수 내부에서 전역 변수에 값을 대입하겠다고 선언한다.

> [!WARNING]
> `global`을 과도하게 사용하면 함수가 외부 상태에 의존하게 된다.
>
> 가능하면 입력값을 받고 결과를 반환하는 구조를 우선 고려한다.

---

# 30. `nonlocal`

중첩 함수에서 가장 가까운 바깥 함수의 변수를 수정할 때 사용한다.

```python
def outer():
    value = 10

    def inner():
        nonlocal value

        value = 20

    inner()

    print(value)


outer()
```

출력:

```text
20
```

`nonlocal`은 전역 변수가 아니라 바깥 함수 범위의 변수를 대상으로 한다.

---

# 31. LEGB 규칙

Python은 이름을 다음 순서로 찾는다.

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

| 범위 | 의미 |
| --- | --- |
| Local | 현재 함수 내부 |
| Enclosing | 바깥 함수 영역 |
| Global | 모듈 전체 영역 |
| Built-in | Python 내장 이름 |

원본의 지역 변수·전역 변수·`nonlocal` 예제는 이 검색 순서를 보여 준다.

---

# 32. 변경 가능한 객체 전달

## 32-1. 원본 코드

```python
def append_number(values):
    values.append(4)


numbers = [
    1,
    2,
    3,
]

append_number(numbers)

print(numbers)
```

출력:

```text
[1, 2, 3, 4]
```

리스트 객체 내부를 함수 안에서 변경했기 때문에 호출한 쪽에서도 변경이 보인다.

---

# 33. 새 객체 대입과 내부 변경

## 33-1. 새 객체 대입

```python
def replace_values(values):
    values = [
        9,
        9,
        9,
    ]


numbers = [
    1,
    2,
    3,
]

replace_values(numbers)

print(numbers)
```

출력:

```text
[1, 2, 3]
```

## 33-2. 내부 변경

```python
def change_values(values):
    values[0] = 100


change_values(numbers)

print(numbers)
```

출력:

```text
[100, 2, 3]
```

> [!IMPORTANT]
> 함수에 “주소값이 복사된다”고만 이해하기보다, 객체 참조가 전달되고 가변 객체의 내부 변경이 공유된다고 이해하는 것이 정확하다.

---

# 34. 함수 합성

## 34-1. 원본 코드

```python
def add_ten(value):
    return value + 10


def multiply_ten(value):
    return value * 10
```

단계별 실행:

```python
value = 10
added_value = add_ten(value)
result = multiply_ten(
    added_value
)

print(result)
```

출력:

```text
200
```

함수 호출을 연결할 수도 있다.

```python
result = multiply_ten(
    add_ten(10)
)

print(result)
```

출력:

```text
200
```

---

# 35. 함수도 객체다

## 35-1. 원본 코드

```python
print(add_ten)
```

출력 형태:

```text
<function add_ten at 0x...>
```

함수 이름 뒤에 괄호를 붙이지 않으면 함수 객체 자체를 가리킨다.

```python
operation = add_ten

print(operation(5))
```

출력:

```text
15
```

Python에서 함수는 변수에 저장하고 다른 함수에 전달할 수 있는 일급 객체다.

---

# 36. 람다 표현식

## 36-1. 원본 코드

```python
add_ten = (
    lambda value: value + 10
)

print(add_ten(5))
```

출력:

```text
15
```

다음 일반 함수와 같은 역할이다.

```python
def add_ten(value):
    return value + 10
```

## 36-2. 특징

- 이름 없이 작성 가능
- 하나의 표현식만 작성 가능
- 표현식 결과가 자동 반환
- 짧은 기준 함수에 적합

---

# 37. 람다 사용 기준

적절한 예:

```python
people.sort(
    key=lambda person: (
        person["age"]
    )
)
```

복잡한 예:

```python
result = lambda value: (
    value * 2
    if value > 0
    else (
        value - 10
        if value < -5
        else 0
    )
)
```

조건이 복잡하면 일반 함수로 분리하는 것이 좋다.

> [!TIP]
> 이름과 설명이 필요한 로직은 일반 함수로 작성한다.

---

# 38. `map()`

## 38-1. 원본 코드

```python
values = [
    "1",
    "2",
]

numbers = list(
    map(
        int,
        values,
    )
)

print(numbers)
```

출력:

```text
[1, 2]
```

`map()`은 반복 가능한 객체의 각 값을 함수에 전달한다.

```text
"1" → int("1") → 1
"2" → int("2") → 2
```

---

# 39. `map()`에 사용자 함수 전달

```python
def add_ten(value):
    return value + 10


numbers = [
    1,
    2,
]

result = list(
    map(
        add_ten,
        numbers,
    )
)

print(result)
```

출력:

```text
[11, 12]
```

람다를 직접 전달할 수도 있다.

```python
result = list(
    map(
        lambda value: value + 10,
        numbers,
    )
)
```

---

# 40. `map()`과 리스트 컴프리헨션

```python
numbers = list(
    map(
        int,
        values,
    )
)
```

```python
numbers = [
    int(value)
    for value in values
]
```

선택 기준:

```text
기존 함수 그대로 적용
→ map() 검토

변환식과 조건이 함께 있음
→ 리스트 컴프리헨션 검토
```

둘 중 더 읽기 쉬운 방식을 선택한다.

---

# 41. 정렬의 `key`

## 41-1. 원본 코드

```python
people = [
    {
        "name": "이름1",
        "age": 25,
    },
    {
        "name": "이름2",
        "age": 23,
    },
    {
        "name": "이름3",
        "age": 30,
    },
]

people.sort(
    key=lambda person: (
        person["age"]
    )
)

print(people)
```

출력 순서:

```text
23세 → 25세 → 30세
```

`key`에는 각 요소에서 정렬 기준값을 반환하는 함수를 전달한다.

---

# 42. 출력 함수와 반환 함수

## 42-1. 원본 출력 함수

```python
def print_ages(people):
    for person in people:
        print(
            person["age"]
        )
```

실행 결과:

```text
25
23
30
```

## 42-2. 반환 함수

```python
def get_ages(people):
    return [
        person["age"]
        for person in people
    ]
```

실행:

```python
ages = get_ages(people)

print(ages)
```

출력:

```text
[25, 23, 30]
```

반환 함수는 결과를 출력·저장·정렬·테스트 등 다른 작업에 재사용할 수 있다.

---

# 43. 재귀 함수

재귀 함수는 함수가 자기 자신을 호출하는 구조다.

```python
def countdown(number):
    if number == 0:
        return

    print(number)

    countdown(
        number - 1
    )
```

실행:

```python
countdown(3)
```

출력:

```text
3
2
1
```

## 43-1. 종료 조건

```text
number == 0
→ 더 이상 호출하지 않음
```

> [!WARNING]
> 종료 조건이 없거나 도달하지 못하면 재귀 호출이 계속되어 `RecursionError`가 발생할 수 있다.

---

# 44. 재귀 함수 활용

원본에서는 폴더 안의 하위 폴더를 계속 탐색하는 예시를 메모했다.

```text
현재 폴더 확인
    ↓
파일이면 출력
    ↓
폴더이면 같은 함수 다시 호출
```

다음 상황에서 재귀를 사용할 수 있다.

- 폴더 구조 탐색
- 트리 구조
- 조직도
- 댓글의 대댓글 구조
- 수학적 재귀 정의

단순 반복으로 해결하기 쉬운 문제라면 반복문이 더 이해하기 쉬울 수 있다.

---

# 45. 내장 함수 이름 덮어쓰기

원본에는 다음 이름이 사용된다.

```python
sum = (
    lambda x, y: x + y
)
```

`sum`은 Python 내장 함수 이름이므로 다른 이름을 사용하는 것이 좋다.

개선:

```python
add = (
    lambda x, y: x + y
)
```

다음 이름도 변수나 함수 이름으로 덮어쓰지 않는 것이 좋다.

```text
sum
list
dict
str
print
input
type
```

---

# 46. 이름 재사용 주의

원본에서는 `info`를 함수 이름으로 사용한 뒤 리스트 변수 이름으로 다시 사용한다.

```text
def info(...):
    ...


info = [
    ...
]
```

두 번째 대입 이후에는 기존 함수 이름을 사용할 수 없다.

개선:

```text
def print_user_info(...):
    ...


people = [
    ...
]
```

> [!IMPORTANT]
> 같은 범위에서 함수 이름과 변수 이름을 재사용하면 이전 객체에 접근하기 어려워진다.

---

# 47. 타입 힌트

```python
def add(
    a: int,
    b: int,
) -> int:
    return a + b
```

## 47-1. 구성

| 코드 | 의미 |
| --- | --- |
| `a: int` | `a`에 정수를 기대 |
| `b: int` | `b`에 정수를 기대 |
| `-> int` | 정수 반환을 기대 |

타입 힌트는 기본적으로 실행 시 자료형을 강제하지 않는다.

코드 이해와 정적 분석에 도움을 준다.

---

# 48. 순수 함수

순수 함수는 같은 입력에 항상 같은 결과를 반환하고 외부 상태를 변경하지 않는다.

```python
def calculate_total(
    price: int,
    quantity: int,
) -> int:
    return price * quantity
```

실행:

```python
print(
    calculate_total(
        45000,
        2,
    )
)
```

출력:

```text
90000
```

순수 함수는 테스트와 재사용이 쉽다.

---

# 49. 실무형 함수 예제

성인 사용자 이름 목록을 반환하는 함수다.

```python
def get_adult_names(
    people: list[
        dict[str, object]
    ],
) -> list[str]:
    """성인 사용자 이름 목록을 반환한다."""
    return [
        str(person["name"])
        for person in people
        if int(person["age"]) >= 19
    ]
```

## 49-1. 입력값

```python
people = [
    {
        "name": "Kim",
        "age": 21,
    },
    {
        "name": "Lee",
        "age": 17,
    },
    {
        "name": "Park",
        "age": 28,
    },
]
```

## 49-2. 실행

```python
adult_names = get_adult_names(
    people
)

print(adult_names)
```

## 49-3. 출력 결과

```text
['Kim', 'Park']
```

## 49-4. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| `people` | 사용자 딕셔너리 목록 입력 |
| `list[dict[str, object]]` | 입력 자료형 의도 표현 |
| `-> list[str]` | 문자열 리스트 반환 의도 |
| 리스트 컴프리헨션 | 조건에 맞는 이름 목록 생성 |
| `age >= 19` | 성인 사용자 필터링 |
| `return` | 결과를 호출한 위치에 전달 |

## 49-5. 왜 출력하지 않고 반환할까?

반환된 목록은 다음 작업에 다시 사용할 수 있다.

- 화면 출력
- 파일 저장
- API 응답
- 정렬
- 개수 계산
- 자동 테스트

---

# 50. 내 코드와 강사님 코드 비교

| 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 정의 전 호출 | `NameError` 원인 메모 | 호출 코드를 주석 처리 |
| Docstring | 첫 문자열과 중간 문자열 비교 | 첫 문자열 중심 |
| `return` | `None` 반환을 상세 메모 | 기본 실행 흐름 |
| 여러 값 반환 | 튜플과 언패킹 자료형 확인 | 튜플 반환 중심 |
| `*`, `**` | 오류 조건과 딕셔너리 동작 상세 | 핵심 언패킹 예제 |
| 기본값 | 함수 정의와 호출 설명 | 기본 사용 중심 |
| 객체 변경 | 원본 리스트 변경을 주소값으로 메모 | 리스트 변경 결과 확인 |
| 함수 객체 | 출력 결과와 함수 합성 확인 | 함수 객체 출력 |
| 람다 | 여러 형태 직접 실습 | 일반 함수와 대응 비교 |
| 변수 범위 | 지역·전역·`global`·`nonlocal` 상세 | LEGB 흐름 중심 |

## 50-1. 내 코드의 장점

- 함수 정의 전 호출 오류를 정확히 기록했다.
- 반환값과 `None`, 튜플 언패킹을 직접 확인했다.
- `*args`, `**kwargs`, 딕셔너리 언패킹의 차이를 자세히 실습했다.
- 함수 객체·람다·`map()`·정렬 기준을 연결했다.
- 지역·전역·비지역 변수까지 단계적으로 확인했다.

## 50-2. 내 코드의 개선점

- `sum` 같은 내장 함수 이름을 덮어쓰지 않아야 한다.
- `info` 함수 이름을 리스트 변수 이름으로 다시 사용하지 않아야 한다.
- 가변 객체 전달은 단순히 “주소값이 들어간다”보다 객체 참조와 내부 변경으로 설명하는 것이 정확하다.
- 출력 함수와 결과 반환 함수의 역할을 구분하면 재사용성이 높아진다.
- `global` 사용보다 반환값을 이용한 상태 변경을 우선 고려할 수 있다.

## 50-3. 강사님 코드의 장점

- 일반 함수와 람다 표현식을 나란히 비교한다.
- 위치·키워드 인자와 가변 인자를 한 흐름에서 실습한다.
- 정렬의 `key`에 일반 함수와 람다를 모두 전달한다.
- 지역·전역·`global`·`nonlocal`의 차이를 단계적으로 보여 준다.
- 재귀 함수의 실제 사용 상황을 폴더 탐색과 연결한다.

## 50-4. 강사님 코드의 보충점

- 타입 힌트와 Docstring의 실무형 작성 예제가 필요하다.
- 변경 가능한 기본값의 문제가 필요하다.
- 함수가 한 가지 주요 책임을 담당해야 한다는 설명이 필요하다.
- 재귀 함수의 종료 조건과 `RecursionError`를 보충할 필요가 있다.

---

# 51. 기존 코드에서 개선 코드로 바꾼 이유

## 51-1. 출력에서 반환으로

기존:

```python
def add(a, b):
    print(a + b)
```

개선:

```python
def add(a, b):
    return a + b
```

이유:

- 결과를 다른 계산에 재사용할 수 있다.
- 함수 테스트가 쉽다.
- 출력 방식과 계산 로직을 분리할 수 있다.

## 51-2. 의미 있는 매개변수 이름

기존:

```python
def ref(a):
    a.append(4)
```

개선:

```python
def append_number(
    numbers,
):
    numbers.append(4)
```

## 51-3. 전역 변수 대신 반환값

기존:

```python
global value
value = value + 2
```

개선:

```python
def add_two(value):
    return value + 2


value = add_two(value)
```

## 51-4. 복잡한 람다 대신 일반 함수

기존:

```python
key=lambda person: (
    0
    if person["active"]
    else 1
)
```

조건 설명이 필요하다면:

```python
def get_priority(person):
    if person["active"]:
        return 0

    return 1
```

---

# 52. 대표 오류로 이해하기

## 52-1. 정의 전에 호출

```text
hello()

def hello():
    print("hello")
```

발생 결과:

```text
NameError
```

---

## 52-2. 전달인자 개수 불일치

```python
def add(a, b):
    return a + b


add(1)
```

발생 결과:

```text
TypeError
```

---

## 52-3. 딕셔너리 키와 매개변수 불일치

```python
person = {
    "user_name": "Kim",
}


def info(name):
    print(name)


info(**person)
```

발생 결과:

```text
TypeError
```

---

## 52-4. 기본 매개변수 순서 오류

```text
def info(name="익명", age):
    pass
```

발생 결과:

```text
SyntaxError
```

---

## 52-5. 지역 변수 외부 접근

```python
def create_value():
    value = 10


create_value()

print(value)
```

발생 결과:

```text
NameError
```

---

## 52-6. 종료 조건 없는 재귀

```python
def repeat():
    repeat()


repeat()
```

발생 결과:

```text
RecursionError
```

---

# 53. 자주 하는 실수

## 53-1. 함수 정의만 하고 호출하지 않음

함수 내부 코드는 실행되지 않는다.

## 53-2. 정의 전에 함수 호출

`NameError`가 발생한다.

## 53-3. `print()` 결과를 반환값으로 생각

`return`이 없으면 `None`이 반환된다.

## 53-4. 위치 인자 순서를 잘못 전달

계산 결과가 달라질 수 있다.

## 53-5. `*`와 `**`를 혼동

`*`는 위치 인자, `**`는 키워드 인자를 펼친다.

## 53-6. 딕셔너리 키와 매개변수 이름 불일치

`TypeError`가 발생한다.

## 53-7. 기본값 없는 매개변수를 뒤에 작성

`SyntaxError`가 발생한다.

## 53-8. 리스트를 기본값으로 직접 사용

호출 사이에 같은 리스트가 공유될 수 있다.

## 53-9. 함수 내부에서 가변 객체를 의도하지 않게 변경

호출한 쪽의 원본 데이터가 바뀔 수 있다.

## 53-10. `global`을 과도하게 사용

함수의 외부 상태 의존성이 커진다.

## 53-11. 복잡한 로직을 람다로 작성

가독성이 떨어질 수 있다.

## 53-12. 내장 함수 이름을 변수나 함수로 사용

기존 내장 함수를 호출할 수 없게 된다.

## 53-13. 함수 이름을 다른 변수로 덮어씀

이전 함수 객체에 접근하기 어려워진다.

## 53-14. 재귀 함수의 종료 조건 누락

`RecursionError`가 발생한다.

---

# 54. 핵심 요약

```text
def
→ 함수 정의

함수이름()
→ 함수 호출

매개변수
→ 정의에서 입력받는 변수

전달인자
→ 호출할 때 전달하는 값
```

```text
print()
→ 화면 출력

return
→ 결과 반환

return 값 없음
→ None 반환

여러 값 return
→ 튜플 반환
```

```text
*
→ 위치 인자 언패킹

**
→ 키워드 인자 언패킹

*args
→ 튜플

**kwargs
→ 딕셔너리
```

```text
Local
→ 현재 함수

Enclosing
→ 바깥 함수

Global
→ 모듈 전체

Built-in
→ Python 내장
```

---

# 55. 최종 체크리스트

- [ ] `def`로 함수를 정의할 수 있는가?
- [ ] 함수 이름 뒤 괄호로 호출할 수 있는가?
- [ ] 함수 정의 전에 호출하면 안 되는 이유를 이해했는가?
- [ ] 매개변수와 전달인자를 구분할 수 있는가?
- [ ] Docstring을 함수 첫 문장에 작성할 수 있는가?
- [ ] `print()`와 `return`의 차이를 설명할 수 있는가?
- [ ] 값 없는 `return`이 `None`을 반환함을 이해했는가?
- [ ] 여러 반환값을 튜플로 받을 수 있는가?
- [ ] 반환값을 언패킹할 수 있는가?
- [ ] 위치 인자와 키워드 인자를 사용할 수 있는가?
- [ ] 리스트·튜플을 `*`로 펼칠 수 있는가?
- [ ] 딕셔너리를 `**`로 펼칠 수 있는가?
- [ ] `*args`가 튜플임을 이해했는가?
- [ ] `**kwargs`가 딕셔너리임을 이해했는가?
- [ ] 기본 매개변수 순서를 올바르게 작성했는가?
- [ ] 변경 가능한 기본값을 직접 사용하지 않는가?
- [ ] 지역 변수와 전역 변수를 구분할 수 있는가?
- [ ] `global`과 `nonlocal`의 차이를 설명할 수 있는가?
- [ ] LEGB 규칙을 이해했는가?
- [ ] 가변 객체의 내부 변경이 원본에 반영될 수 있음을 이해했는가?
- [ ] 함수 객체를 변수에 저장할 수 있는가?
- [ ] 람다와 일반 함수의 선택 기준을 구분할 수 있는가?
- [ ] `map()`에 함수를 전달할 수 있는가?
- [ ] 정렬의 `key`에 기준 함수를 전달할 수 있는가?
- [ ] 재귀 함수에 종료 조건을 작성했는가?
- [ ] 내장 함수 이름을 덮어쓰지 않는가?
- [ ] 타입 힌트로 입력과 반환 의도를 표현할 수 있는가?
- [ ] 함수 하나가 하나의 주요 책임을 담당하는가?

---

# 마무리

함수의 핵심은 코드를 단순히 묶는 것에서 끝나지 않는다.

```text
작업에 명확한 이름을 붙이고
    ↓
입력값을 매개변수로 받고
    ↓
처리 결과를 return으로 반환하고
    ↓
변수 범위와 객체 변경을 관리하며
    ↓
다른 코드에서 안전하게 재사용하는 것
```

이 흐름을 이해하면 다음 클래스 문서에서 데이터와 관련 동작을 하나의 객체로 묶는 구조를 더 자연스럽게 학습할 수 있다.
